#!/usr/bin/env python3
"""
build_site.py — whole-site "Press" renderer for MAM5020F.

Reads the CONTENT from the live docs/ tree (each page's .content body) plus the
sitemap from docs/index.html and the term data from glossary.json, and writes a
fully Press-styled mirror into redesign/site/. The live docs/ is never touched.

  python3 build_site.py            # render the whole site
  python3 build_site.py week-1     # render only pages whose href starts week-1/
"""
import os, re, html, sys, json, shutil
from urllib.parse import unquote, quote

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOCS = os.path.join(ROOT, "content")   # content source (formerly docs/)
OUT  = os.path.join(ROOT, "docs")      # published GitHub Pages output
GLOSSARY = os.path.join(ROOT, "glossary.json")
INDEX_SRC = os.path.join(DOCS, "index.html")

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,400&display=swap" rel="stylesheet">')

CSS = r"""
:root{--blue:#003A70;--blue2:#2a5298;--paper:#f5f2ea;--card:#fffdf8;--ink:#23201b;--ink2:#3f3a32;--mut:#6a6256;--lbl:#736a5c;--rule:#ddd5c5;--rule2:#cfc6b5;--amber:#7c5c12}
html{font-size:100%}
*{margin:0;padding:0;box-sizing:border-box}
::selection{background:var(--blue);color:#fff}
body{background:var(--paper);color:var(--ink);font-family:'Newsreader',serif}
img{max-width:100%}
.brandrule{height:4px;background:var(--blue)}
/* ---- three-column shell ---- */
.shell{max-width:1880px;margin:0 auto;padding:0 44px;display:grid;grid-template-columns:218px minmax(0,1fr) 248px;column-gap:64px;align-items:start}
.maincol{min-width:0;max-width:1340px;margin-left:auto;margin-right:auto}
.leftnav,.rightrail{position:sticky;top:30px;align-self:start;padding-top:46px;max-height:calc(100vh - 40px);overflow-y:auto}
.leftnav::-webkit-scrollbar,.rightrail::-webkit-scrollbar{width:0}
.leftnav .back{font-family:'Fraunces';font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;color:var(--blue);text-decoration:none;display:block;margin-bottom:26px}
.leftnav .back:hover{color:var(--blue2)}
.leftnav .navwk{font-family:'Fraunces';font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:var(--lbl);margin-bottom:7px;line-height:1.5}
.leftnav .navhd{font-family:'Fraunces';font-weight:500;font-size:.95rem;color:var(--ink);margin-bottom:12px;padding-bottom:11px;border-bottom:1px solid var(--rule)}
.toc{display:flex;flex-direction:column}
.toc .lesson{font-family:'Newsreader';font-size:.97rem;line-height:1.3;color:var(--ink2);text-decoration:none;padding:6px 0;display:block;transition:color .15s}
.toc .lesson:hover{color:var(--blue)}
.toc .lesson.cur{color:var(--blue);font-weight:500}
.toc .subs{display:flex;flex-direction:column;margin:3px 0 10px;border-left:1px solid var(--rule)}
.toc .subs a{font-family:'Newsreader';font-size:.86rem;line-height:1.32;color:var(--mut);text-decoration:none;padding:5px 0 5px 14px;margin-left:-1px;border-left:2px solid transparent;transition:color .15s,border-color .15s}
.toc .subs a:hover{color:var(--blue)}
.toc .subs a.on{color:var(--blue);border-left-color:var(--blue)}
.rightrail .rmeta{font-family:'Fraunces';font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--lbl);line-height:2;margin-bottom:26px;padding-bottom:20px;border-bottom:1px solid var(--rule)}
.rightrail .snote{margin-bottom:24px;font-family:'Newsreader';font-size:.93rem;line-height:1.5;color:var(--ink2)}
.rightrail .snote .sk{font-family:'Fraunces';font-weight:500;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin-bottom:5px}
.rightrail .rhd{font-family:'Fraunces';font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;color:var(--lbl);margin:0 0 12px}
/* ---- lesson header (in maincol) ---- */
.ahead{padding:44px 0 30px;border-bottom:1px solid var(--rule)}
.ahead .eyebrow{font-family:'Fraunces';font-size:.8rem;letter-spacing:.24em;text-transform:uppercase;color:var(--blue);margin-bottom:22px}
.ahead h1{font-family:'Fraunces';font-optical-sizing:auto;font-weight:400;font-size:clamp(2.3rem,4.6vw,3.2rem);line-height:1.04;letter-spacing:-.012em;color:var(--blue);margin:0 0 16px}
.ahead .deck{font-family:'Newsreader';font-style:italic;font-size:1.28rem;line-height:1.4;color:var(--mut);max-width:600px}
/* ---- lesson body ---- */
.abody{padding:30px 0 56px}
.abody p{font-size:1.48rem;line-height:1.64;color:var(--ink);margin:0 0 27px;text-wrap:pretty}
.abody p.drop::first-letter{font-family:'Fraunces';font-weight:500;font-size:3.9rem;line-height:.8;float:left;margin:.32rem .7rem 0 0;color:var(--blue)}
.abody strong{font-weight:600}.abody em{font-style:italic}
.abody a{color:var(--blue);text-decoration:none;border-bottom:1px solid var(--rule2)}.abody a:hover{border-color:var(--blue)}
.abody h2.section-title{font-family:'Fraunces';font-weight:400;font-size:1.9rem;line-height:1.1;color:var(--blue);border-top:1px solid var(--rule);padding-top:34px;margin:44px 0 16px;scroll-margin-top:24px}
.abody h3{font-family:'Fraunces';font-weight:500;font-size:1.32rem;color:var(--ink);margin:26px 0 10px}
.abody h4{font-family:'Fraunces';font-weight:500;font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--blue);margin:0 0 9px}
.abody ul,.abody ol{margin:0 0 22px;padding:0;list-style:none}
.abody li{font-size:1.33rem;line-height:1.56;color:var(--ink2);margin-bottom:11px;padding-left:24px;position:relative}
.abody ul>li::before{content:'';position:absolute;left:0;top:.7em;width:9px;height:1px;background:var(--blue)}
.abody ol{counter-reset:li}.abody ol>li{counter-increment:li}
.abody ol>li::before{content:counter(li)'.';position:absolute;left:0;top:0;font-family:'Fraunces';color:var(--blue);font-size:1rem}
.abody .intro-text{border-left:2px solid var(--blue);padding:2px 0 2px 22px;margin:0 0 34px}
.abody .intro-text h2{font-family:'Fraunces';font-weight:500;font-size:.8rem;letter-spacing:.2em;text-transform:uppercase;color:var(--blue);margin-bottom:10px}
.abody .intro-text p{font-size:1.31rem;color:var(--ink2)}.abody .intro-text p:last-child{margin-bottom:0}
.abody .card-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin:26px 0;align-items:start}
.abody .card{background:var(--card);border:1px solid var(--rule);border-radius:3px;padding:22px 24px}
.abody .card h3{font-family:'Fraunces';font-weight:500;font-size:1.16rem;color:var(--blue);margin:0 0 8px}
.abody .card p{font-size:1.21rem;line-height:1.5;color:var(--ink2);margin:0}
.abody .highlight-box{background:var(--blue);color:#fbf7ee;padding:30px 32px;margin:34px 0}
.abody .highlight-box h3{font-family:'Fraunces';font-weight:500;font-size:1.45rem;color:#fff;margin:0 0 12px}
.abody .highlight-box p,.abody .highlight-box li{font-family:'Newsreader';font-size:1.28rem;line-height:1.58;color:#e9e2d2;margin:0 0 8px}
.abody .highlight-box strong{color:#fff}.abody .highlight-box a{color:#fff;border-bottom-color:rgba(255,255,255,.5)}
.abody .highlight-box ul li::before{background:#bcd0e6}
.abody .info-box,.abody .technical-detail,.abody .case-study,.abody .decision-framework{background:var(--card);border:1px solid var(--rule);border-left:3px solid var(--blue);padding:22px 26px;margin:28px 0}
.abody .info-box p,.abody .info-box li,.abody .technical-detail p,.abody .technical-detail li,.abody .case-study p,.abody .case-study li,.abody .decision-framework p,.abody .decision-framework li{font-family:'Newsreader';font-size:1.24rem;line-height:1.58;color:var(--ink2);margin:0 0 8px}
.abody .case-study h3,.abody .decision-framework h3{font-family:'Fraunces';font-weight:500;font-size:1.22rem;color:var(--blue);margin:0 0 8px}
.abody .warning-box{background:#f6eedb;border-left:3px solid var(--amber);padding:22px 26px;margin:28px 0}
.abody .warning-box h4{color:var(--amber)}
.abody .warning-box p,.abody .warning-box li{font-family:'Newsreader';font-size:1.04rem;line-height:1.6;color:#574d33;margin:0 0 8px}
.abody table{width:100%;border-collapse:collapse;margin:26px 0;font-family:'Newsreader';font-size:1.01rem}
.abody th{font-family:'Fraunces';font-weight:500;font-size:.74rem;letter-spacing:.1em;text-transform:uppercase;color:var(--blue);text-align:left;padding:10px 14px 10px 0;border-bottom:1.5px solid var(--blue)}
.abody td{padding:11px 14px 11px 0;border-bottom:1px solid var(--rule);color:var(--ink2);line-height:1.5;vertical-align:top}
.abody .step-list{list-style:none;counter-reset:s;padding:0;margin:26px 0}
.abody .step-list>li{counter-increment:s;position:relative;padding:2px 0 22px 56px;border:0;margin:0;font-size:1.12rem;color:var(--ink2)}
.abody .step-list>li::before{content:counter(s);position:absolute;left:0;top:-4px;font-family:'Fraunces';font-weight:400;font-size:2.2rem;color:var(--blue);line-height:1}
.abody .step-list>li::after{content:none}
.abody .code-block,.abody pre{background:#04233f;color:#e9e3d6;font-family:'SF Mono',Menlo,Consolas,monospace;font-size:.85rem;line-height:1.6;padding:18px 22px;margin:26px 0;overflow-x:auto;border-left:3px solid var(--blue2);white-space:pre-wrap}
.abody .code-block *{font-family:inherit}
.abody code{font-family:'SF Mono',Menlo,Consolas,monospace;font-size:.86em;background:#ece4d3;padding:1px 5px;color:#7a4a12}
.abody .code-block code,.abody pre code{background:none;color:inherit;padding:0}
.abody .resource-placeholder{background:var(--card);border:1px solid var(--rule);border-top:3px solid var(--blue);padding:22px 26px;margin:26px 0}
.abody .resource-placeholder h4{color:var(--blue)}
.abody .resource-placeholder p{font-family:'Newsreader';font-size:1.02rem;line-height:1.55;color:var(--ink2);margin:0 0 6px}
/* ===== baseline + bespoke long-tail components ===== */
.abody{font-size:1.33rem;line-height:1.62}
.abody .section{margin:0 0 8px}
.abody .part-title,.abody .intro-section h3{font-family:'Fraunces';font-weight:500;font-size:1.3rem;color:var(--blue);margin:26px 0 10px}
/* callout boxes */
.abody .analogy-box,.abody .how-it-works,.abody .key-concepts,.abody .research-applications,.abody .instructor-box,.abody .prompt-example,.abody .empty-note,.abody .caveat-item,.abody .architecture-examples,.abody .model-details,.abody .paywalled-section,.abody .video-section,.abody .intro-section{background:var(--card);border:1px solid var(--rule);border-left:3px solid var(--blue);padding:20px 24px;margin:24px 0;border-radius:3px}
.abody .cm,.abody .comment{color:#9fb0c7;background:none;border:0;padding:0;margin:0;font-family:inherit;font-style:normal}
.abody .analogy-box p,.abody .how-it-works p,.abody .key-concepts p,.abody .research-applications p,.abody .instructor-box p,.abody .prompt-example p,.abody .intro-section p,.abody .empty-note p{font-family:'Newsreader';font-size:1.05rem;line-height:1.6;color:var(--ink2);margin:0 0 8px}
.abody .empty-note{font-style:italic;color:var(--mut)}
/* generic cards + grids */
.abody .tool-card,.abody .category-card,.abody .objective-card,.abody .level-card,.abody .architecture-card,.abody .phase-card,.abody .comparison-card,.abody .audience-card,.abody .week-card,.abody .paper-card,.abody .structure-item{background:var(--card);border:1px solid var(--rule);padding:18px 22px;margin:14px 0;border-radius:3px}
.abody .category-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:18px;margin:22px 0;align-items:start}
.abody .category-grid>*{margin:0}
.abody .model-list{margin:10px 0 0;padding:0}
/* callouts nested inside cards must stay compact, not squeeze the text to one word per line */
.abody .category-card .model-details,.abody .card .model-details,.abody .category-card .info-box,.abody .card .info-box,.abody .category-card .highlight-box,.abody .card .highlight-box,.abody .category-card .technical-detail,.abody .card .technical-detail,.abody .category-card .analogy-box,.abody .card .analogy-box{padding:13px 16px;margin:13px 0 0}
.abody .category-card .model-details p,.abody .card .model-details p,.abody .category-card .highlight-box p,.abody .card .highlight-box p,.abody .category-card .info-box p,.abody .card .info-box p,.abody .category-card .technical-detail p,.abody .card .technical-detail p{font-size:1.04rem;line-height:1.5;margin:0 0 6px}
.abody .objective-number,.abody .num{font-family:'Fraunces';font-weight:400;font-size:1.6rem;color:var(--blue);line-height:1}
/* topic list */
.abody .topics-list{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:6px 24px;margin:18px 0}
.abody .topic-item{font-family:'Newsreader';font-size:1.06rem;line-height:1.4;color:var(--ink2);padding:6px 0 6px 18px;position:relative}
.abody .topic-item::before{content:'';position:absolute;left:0;top:.65em;width:9px;height:1px;background:var(--blue)}
/* timeline (handles era/description and date/title/content variants) */
.abody .timeline-items,.abody .timeline,.abody .timeline-section{margin:22px 0}
.abody .timeline-item{position:relative;padding:0 0 20px 26px;margin-left:4px;border-left:2px solid var(--rule)}
.abody .timeline-item:last-child{border-left-color:transparent;padding-bottom:0}
.abody .timeline-marker,.abody .marker-circle{display:none}
.abody .timeline-era,.abody .timeline-date,.abody .era-badge{position:relative;font-family:'Fraunces';font-weight:500;font-size:.74rem;letter-spacing:.1em;text-transform:uppercase;color:var(--blue);margin-bottom:5px}
.abody .timeline-item>.timeline-era::before,.abody .timeline-item>.timeline-date::before,.abody .timeline-item>.era-badge::before{content:'';position:absolute;left:-33px;top:1px;width:11px;height:11px;border-radius:50%;background:var(--blue);border:2px solid var(--paper)}
.abody .timeline-title{font-family:'Fraunces';font-weight:500;font-size:1.12rem;color:var(--ink);margin-bottom:4px}
.abody .timeline-description,.abody .timeline-content{font-family:'Newsreader';font-size:1.06rem;line-height:1.55;color:var(--ink2)}
.abody .timeline-description strong,.abody .timeline-content strong{color:var(--ink)}
/* stats */
.abody .stat-box{display:flex;flex-direction:column;gap:5px;background:var(--card);border:1px solid var(--rule);border-left:3px solid var(--blue);padding:16px 20px;margin:20px 0;border-radius:3px}
.abody .stat-number{font-family:'Fraunces';font-weight:500;font-size:2rem;color:var(--blue);line-height:1}
.abody .stat-label{font-family:'Newsreader';font-size:.95rem;line-height:1.45;color:var(--mut)}
/* discussion questions */
.abody .question-set{margin:24px 0}
.abody .q-tag{display:inline-block;font-family:'Fraunces';font-weight:500;font-size:.64rem;letter-spacing:.1em;text-transform:uppercase;color:#fff;background:var(--blue);padding:2px 9px;border-radius:3px;margin-right:9px;vertical-align:middle}
/* paper cards */
.abody .paper-title{font-family:'Fraunces';font-weight:500;font-size:1.14rem;color:var(--blue);margin:0 0 4px}
.abody .paper-meta{font-family:'Newsreader';font-style:italic;font-size:.95rem;color:var(--mut);margin:0 0 8px}
.abody .paper-actions{display:flex;flex-wrap:wrap;gap:14px;margin-top:8px;align-items:center}
.abody .source-link,.abody .tool-url{font-family:'Fraunces';font-size:.85rem;color:var(--blue)}
.abody .access,.abody .tool-pricing,.abody .sublesson-tag{font-family:'Fraunces';font-size:.68rem;letter-spacing:.06em;text-transform:uppercase;color:var(--mut)}
/* inline badges + indicators */
.abody .level-tag,.abody .card-label,.abody .verdict{display:inline-block;font-family:'Fraunces';font-size:.66rem;letter-spacing:.1em;text-transform:uppercase;color:var(--blue);background:#ece4d3;padding:2px 8px;border-radius:3px}
.abody .verdict-yes{color:#2c6e3f}.abody .verdict-no{color:#9a2f2f}
.abody .risk-high{color:#9a2f2f;font-weight:600}.abody .risk-low{color:#2c6e3f;font-weight:600}
.abody .prompt-label{display:block;font-family:'Fraunces';font-weight:500;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin-bottom:6px}
/* video — restore responsive 16:9 (the source kept this in <head>, which we drop) */
.abody .video-container{position:relative;width:100%;padding-bottom:56.25%;height:0;overflow:hidden;margin:26px 0;border-radius:3px;background:#04233f}
.abody .video-container iframe,.abody .video-container img,.abody .video-container>a,.abody .video-container video{position:absolute;top:0;left:0;width:100%;height:100%;border:0;object-fit:cover}
.abody .video-section iframe{width:100%;aspect-ratio:16/9;border:0;border-radius:3px}
.abody .video-badge{font-family:'Fraunces';font-weight:500;font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin-bottom:8px}
/* very slight curve on the boxes */
.abody .highlight-box,.abody .info-box,.abody .technical-detail,.abody .case-study,.abody .decision-framework,.abody .warning-box,.abody .code-block,.abody pre,.abody .resource-placeholder{border-radius:3px}
.prevnext{padding:28px 0 60px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:16px;border-top:1px solid var(--rule)}
.prevnext a{display:flex;flex-direction:column;gap:5px;text-decoration:none;max-width:46%}
.prevnext .d{font-family:'Fraunces';font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--lbl)}
.prevnext .pt{font-family:'Fraunces';font-size:1rem;color:var(--blue)}
.prevnext .next{text-align:right;margin-left:auto}
@media(max-width:980px){.shell{grid-template-columns:1fr;column-gap:0}.leftnav,.rightrail{position:static;padding-top:0;max-height:none;overflow:visible}.leftnav{margin:24px 0 6px;padding-bottom:18px;border-bottom:1px solid var(--rule)}.toc{flex-flow:row wrap;gap:6px 18px}.toc .subs{display:none}.rightrail{margin-top:30px;padding-top:24px;border-top:1px solid var(--rule)}}
/* ---- INDEX / landing ---- */
.iwrap{max-width:1400px;margin:0 auto;padding:0 36px}
.icover{display:grid;grid-template-columns:1.5fr 1fr;gap:64px;align-items:end;padding:52px 0 38px;border-bottom:1px solid var(--rule)}
.icover .eyebrow{font-family:'Fraunces';font-size:.8rem;letter-spacing:.22em;text-transform:uppercase;color:var(--blue);margin-bottom:22px}
.icover h1{font-family:'Fraunces';font-optical-sizing:auto;font-weight:400;font-size:clamp(2.9rem,5vw,4.4rem);line-height:1.0;letter-spacing:-.015em;color:var(--blue)}
.icover .sub{font-family:'Newsreader';font-style:italic;font-size:1.32rem;line-height:1.35;color:var(--mut);margin-top:18px}
.iintro p{font-size:1.16rem;line-height:1.62;color:var(--ink2)}
.iintro .links{margin-top:20px;display:flex;flex-wrap:wrap;gap:22px}
.iintro .links a{font-family:'Fraunces';font-size:1.04rem;color:var(--blue);text-decoration:none;border-bottom:1px solid var(--rule2);padding-bottom:2px}
.iintro .links a:hover{border-color:var(--blue)}
.weeks{column-count:2;column-gap:60px;padding:38px 0 12px}
.wcell{break-inside:avoid;-webkit-column-break-inside:avoid;padding-bottom:32px;margin-bottom:4px}
.wlabel{font-family:'Fraunces';font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--lbl);margin-bottom:8px}
.wlabel b{color:var(--blue);font-weight:600}
.wcell h3{font-family:'Fraunces';font-weight:500;font-size:1.46rem;color:var(--blue);margin:0 0 6px;line-height:1.1}
.lessons{list-style:none;margin:12px 0 0;padding:0}
.lessons li{border-top:1px solid var(--rule)}
.lessons a{display:block;font-size:1.08rem;color:var(--ink2);text-decoration:none;padding:9px 0;line-height:1.32;transition:color .15s,padding .15s}
.lessons a:hover{color:var(--blue);padding-left:6px}
.ifoot{border-top:1px solid var(--rule);margin-top:18px}
.ifoot .in{max-width:1400px;margin:0 auto;padding:24px 36px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;font-family:'Fraunces';font-size:.85rem;color:var(--lbl)}
.ifoot a{color:var(--blue);text-decoration:none}
@media(max-width:860px){.icover{grid-template-columns:1fr;gap:26px;align-items:start}.weeks{column-count:1}}
/* ---- GLOSSARY ---- */
.gloss .ga{font-family:'Fraunces';font-weight:400;font-size:1.7rem;color:var(--blue);border-top:1px solid var(--rule);padding-top:22px;margin:38px 0 6px;scroll-margin-top:24px}
.gloss .gentry{padding:13px 0;border-top:1px solid var(--rule)}
.gloss .ga + .gentry{border-top:0}
.gloss .gt{font-family:'Fraunces';font-weight:500;font-size:1.12rem;color:var(--ink);margin-bottom:4px}
.gloss .gd{font-family:'Newsreader';font-size:1.05rem;line-height:1.55;color:var(--ink2)}
.gloss .toc .lesson{font-family:'Fraunces';letter-spacing:.05em}
/* ---- reader text-size control ---- */
.tsize{position:fixed;right:18px;bottom:18px;z-index:300;display:flex;align-items:flex-end;gap:1px;background:var(--card);border:1px solid var(--rule2);border-radius:7px;padding:3px 5px;box-shadow:0 2px 12px rgba(40,30,10,.1)}
.tsize button{font-family:'Fraunces';color:var(--mut);background:none;border:0;border-radius:4px;cursor:pointer;line-height:1;padding:5px 8px;transition:background .15s,color .15s}
.tsize button:nth-child(1){font-size:13px}
.tsize button:nth-child(2){font-size:16px}
.tsize button:nth-child(3){font-size:20px}
.tsize button:hover{color:var(--blue)}
.tsize button[aria-pressed="true"]{background:var(--blue);color:#fff}
.tsize button:focus-visible{outline:2px solid var(--blue);outline-offset:2px}
@media print{.tsize{display:none}}
@media(max-width:600px){.tsize{right:10px;bottom:10px}}
/* ---- hideable margins: labelled controls at the top of the reading column ---- */
.sidebarctl{display:flex;justify-content:flex-end;gap:8px;margin:0;padding:8px 0 0}
.sidebarctl .vbtn{font-family:'Fraunces';font-size:.8rem;color:var(--mut);background:var(--card);border:1px solid var(--rule2);border-radius:6px;cursor:pointer;padding:6px 12px;white-space:nowrap}
.sidebarctl .vbtn:hover{color:var(--blue);border-color:var(--blue)}
.sidebarctl .vbtn:focus-visible{outline:2px solid var(--blue);outline-offset:2px}
.vbtn .ls{display:none}
html.hl .vbtn[data-m="l"] .lh{display:none}
html.hl .vbtn[data-m="l"] .ls{display:inline}
html.hr .vbtn[data-m="r"] .lh{display:none}
html.hr .vbtn[data-m="r"] .ls{display:inline}
@media(min-width:981px){
  /* keep the columns + gaps in place; just blank the sidebar content */
  html.hl .leftnav{visibility:hidden}
  html.hr .rightrail{visibility:hidden}
}
@media(max-width:980px){.sidebarctl{display:none}}
@media print{.sidebarctl{display:none}}
"""

SPY = ("<script>const L=[...document.querySelectorAll('.toc .subs a')],S=L.map(a=>document.querySelector(a.getAttribute('href')));"
       "const o=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){L.forEach(l=>l.classList.remove('on'));"
       "const i=S.indexOf(e.target);if(i>=0)L[i].classList.add('on')}})},{rootMargin:'-8% 0px -82% 0px'});S.forEach(s=>s&&o.observe(s));</script>")

# ---------- transforms (ported from build_press.py) ----------
def strip_tags(s): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s or '')).strip()
_EMOJI = re.compile("[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF"
                    "\U00002B00-\U00002BFF\U0000231A-\U0000231B\U000023E9-\U000023FA"
                    "\U0000FE00-\U0000FE0F‍]+")
def _is_emoji_cp(cp):
    return (0x1F000 <= cp <= 0x1FAFF or 0x2600 <= cp <= 0x27BF or 0x1F1E6 <= cp <= 0x1F1FF
            or 0x2B00 <= cp <= 0x2BFF or 0x231A <= cp <= 0x231B or 0x23E9 <= cp <= 0x23FA
            or 0xFE00 <= cp <= 0xFE0F or cp == 0x200D)
def strip_emoji(s):
    s = re.sub(r'&#(\d+);', lambda m: '' if _is_emoji_cp(int(m.group(1))) else m.group(0), s or '')
    s = re.sub(r'&#x([0-9a-fA-F]+);', lambda m: '' if _is_emoji_cp(int(m.group(1), 16)) else m.group(0), s or '')
    return _EMOJI.sub('', s).strip()
def strip_heading_emoji(c):
    return re.sub(r'(<h[1-4][^>]*>)(.*?)(?=</h[1-4]>|<)', lambda m: m.group(1) + strip_emoji(m.group(2)).lstrip(), c)
def strip_inline(c):
    def fix(m):
        d = [x for x in m.group(1).split(';') if x.strip() and not re.match(r'\s*(color|background[\w-]*|font-family|font-size|line-height|font-weight|list-style[\w-]*|padding[\w-]*)\s*:', x, re.I)]
        return (' style="' + ';'.join(d) + '"') if d else ''
    return re.sub(r'\s*style="([^"]*)"', fix, c)
def inner_div(src, cls):
    s = re.search(r'<div class="' + re.escape(cls) + r'"[^>]*>', src)
    if not s: return ""
    i = s.end(); depth = 1
    for m in re.finditer(r'<div\b[^>]*>|</div>', src[i:]):
        depth += -1 if m.group().startswith('</div') else 1
        if depth == 0: return src[i:i + m.start()]
    return src[i:]

def relhref(target, frm):
    """relative href from page `frm` to page `target` (both root-relative, may be %-encoded)."""
    t = unquote(target); f = unquote(frm)
    rel = os.path.relpath(t, os.path.dirname(f) or '.')
    return quote(rel)

ANALYTICS = ('<script data-goatcounter="https://mam5020f.goatcounter.com/count" '
             'async src="//gc.zgo.at/count.js"></script>')

# reader text-size + hidden-margin state: pre-paint setter in <head> (no flash)
TS_HEAD = ('<script>try{var d=document.documentElement,s=localStorage.getItem("mam-textsize");'
           'if(s)d.style.fontSize=(["100%","112%","125%"][s]||"100%");'
           'if(localStorage.getItem("mam-hide-left")=="1")d.classList.add("hl");'
           'if(localStorage.getItem("mam-hide-right")=="1")d.classList.add("hr");}catch(e){}</script>')

# reshow tabs + collapse/expand wiring for the side margins (shell pages only)
MARGIN_BODY = ('<div class="sidebarctl">'
               '<button class="vbtn" type="button" data-m="l"><span class="lh">&laquo; Hide left sidebar</span><span class="ls">&raquo; Show left sidebar</span></button>'
               '<button class="vbtn" type="button" data-m="r"><span class="lh">Hide right sidebar &raquo;</span><span class="ls">&laquo; Show right sidebar</span></button>'
               '</div>'
               '<script>document.addEventListener("click",function(e){'
               'var t=e.target.closest?e.target.closest("[data-m]"):null;if(!t)return;'
               'var m=t.getAttribute("data-m"),k=m=="l"?"mam-hide-left":"mam-hide-right",c=m=="l"?"hl":"hr";'
               'var on=localStorage.getItem(k)=="1";try{localStorage.setItem(k,on?"0":"1");}catch(e){}'
               'document.documentElement.classList.toggle(c,!on);});</script>')
TS_BODY = ('<div class="tsize" role="group" aria-label="Text size">'
           '<button type="button" data-ts="0" aria-label="Default text size">A</button>'
           '<button type="button" data-ts="1" aria-label="Larger text size">A</button>'
           '<button type="button" data-ts="2" aria-label="Largest text size">A</button></div>'
           '<script>(function(){var S=["100%","112%","125%"],K="mam-textsize";'
           'function ap(i){document.documentElement.style.fontSize=S[i]||S[0];'
           'var b=document.querySelectorAll(".tsize button");'
           'for(var k=0;k<b.length;k++)b[k].setAttribute("aria-pressed",k==i?"true":"false");}'
           'var v=0;try{v=parseInt(localStorage.getItem(K))||0;}catch(e){}ap(v);'
           'document.addEventListener("click",function(e){var t=e.target.closest?e.target.closest(".tsize button"):null;'
           'if(!t)return;var i=parseInt(t.getAttribute("data-ts"))||0;ap(i);'
           'try{localStorage.setItem(K,i);}catch(e){}});})();</script>')

def page(title, body, script=""):
    return ('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
            f'<title>{html.escape(title)}</title>{FONTS}<style>{CSS}</style>{TS_HEAD}</head>'
            f'<body>{body}{script}{TS_BODY}{ANALYTICS}</body></html>')

# ---------- sitemap ----------
def parse_sitemap():
    src = open(INDEX_SRC, encoding="utf-8").read()
    sections = []
    for b in src.split('<div class="week-section">')[1:]:
        numm = re.search(r'<div class="week-number"[^>]*>(.*?)</div>', b, re.S)
        titm = re.search(r'<h2>(.*?)</h2>', b, re.S)
        if not titm: continue
        rawnum = numm.group(1) if numm else ''
        num = strip_tags(strip_emoji(rawnum))
        title = html.unescape(strip_tags(titm.group(1)))
        timm = re.search(r'<span class="week-time">(.*?)</span>', b, re.S)
        tm = html.unescape(strip_tags(timm.group(1))) if timm else ''
        lessons = []
        for u in re.findall(r'<ul class="lesson-list"[^>]*>(.*?)</ul>', b, re.S):
            for am in re.finditer(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', u, re.S):
                lessons.append({'href': html.unescape(am.group(1)), 'title': html.unescape(strip_tags(am.group(2)))})
        label = f"Week {num}" if num.isdigit() else title
        sections.append({'num': num, 'label': label, 'title': title, 'time': tm, 'lessons': lessons})
    return sections

# ---------- lesson render ----------
def render_lesson(L, section, flat, idx, defs, lessonterms):
    href = L['href']
    fs = os.path.join(DOCS, unquote(href))
    src = open(fs, encoding="utf-8").read()
    h1m = re.search(r'<h1[^>]*>(.*?)</h1>', src, re.S)
    h1 = html.unescape(strip_emoji(strip_tags(h1m.group(1)))) if h1m else L['title']
    dm = re.search(r'</h1>\s*(?:</[^>]+>\s*)*?<p[^>]*>(.*?)</p>', src, re.S)
    deck = html.unescape(strip_tags(dm.group(1))) if dm else ''
    c = inner_div(src, "content") or inner_div(src, "container")
    if not c.strip(): raise ValueError("no .content/.container body found")
    c = re.sub(r'\n*<!-- (PAGE-NAV|SCORM-HOOK|ANALYTICS)-START -->.*?-END -->', '', c, flags=re.S)
    c = re.sub(r'href="\s+', 'href="', c)  # trim malformed leading-space hrefs from source
    c = strip_emoji(strip_inline(c))       # remove decorative emoji throughout the body
    c = re.sub(r'(<(?:strong|b|em|h[1-4]|p|li|div)[^>]*>)\s+', r'\1', c)  # tidy space left by stripped emoji
    c = re.sub(r'(</h2>\s*)<p>', r'\1<p class="drop">', c, count=1)
    secs = []
    def _sec(m):
        secs.append(html.unescape(strip_emoji(strip_tags(m.group(1)))))
        return f'<h2 class="section-title" id="s{len(secs)}">{strip_emoji(m.group(1))}</h2>'
    c = re.sub(r'<h2 class="section-title"[^>]*>(.*?)</h2>', _sec, c, flags=re.S)
    words = len(strip_tags(c).split()); rt = max(1, round(words / 200))

    # left nav: this section's lessons, current one expanded
    subs = ''.join(f'<a href="#s{i+1}">{html.escape(t)}</a>' for i, t in enumerate(secs))
    items = ''
    for sl in section['lessons']:
        rel = relhref(sl['href'], href)
        if sl['href'] == href:
            items += f'<a class="lesson cur" href="{rel}">{html.escape(sl["title"])}</a><div class="subs">{subs}</div>'
        else:
            items += f'<a class="lesson" href="{rel}">{html.escape(sl["title"])}</a>'
    back = relhref('index.html', href)
    leftnav = ('<div class="leftnav">'
               f'<a class="back" href="{back}">&larr; All lessons</a>'
               f'<div class="navwk">{html.escape(section["label"])} &middot; {html.escape(section["title"])}</div>'
               f'<nav class="toc">{items}</nav></div>')

    # right rail: metadata + key terms
    meta = html.escape(section['label'])
    if section['num'].isdigit():
        meta += f'<br>Lesson {idx_in_section(section, href)}'
    meta += f'<br>{rt} min read'
    terms = lessonterms.get(unquote(href), [])
    snotes = ''
    for term in terms[:4]:
        d = defs.get(term)
        if d:
            snotes += f'<div class="snote"><div class="sk">{html.escape(term)}</div>{d["definition"]}</div>'
    rail_terms = (f'<div class="rhd">Key terms</div>{snotes}') if snotes else ''
    rightrail = (f'<div class="rightrail"><div class="rmeta">{meta}</div>{rail_terms}</div>')

    # prev / next
    pn = ''
    prev = flat[idx - 1] if idx > 0 else None
    nxt = flat[idx + 1] if idx < len(flat) - 1 else None
    if prev or nxt:
        left = (f'<a href="{relhref(prev["href"], href)}"><span class="d">&larr; Previous</span>'
                f'<span class="pt">{html.escape(prev["title"])}</span></a>') if prev else '<span></span>'
        right = (f'<a class="next" href="{relhref(nxt["href"], href)}"><span class="d">Next &rarr;</span>'
                 f'<span class="pt">{html.escape(nxt["title"])}</span></a>') if nxt else '<span></span>'
        pn = f'<div class="prevnext">{left}{right}</div>'

    main = (MARGIN_BODY + '<div class="ahead"><div class="eyebrow">MAM5020F &mdash; Generative AI for Research</div>'
            f'<h1>{html.escape(h1)}</h1>' + (f'<div class="deck">{html.escape(deck)}</div>' if deck else '') + '</div>'
            f'<div class="abody">{c}</div>{pn}')
    body = ('<div class="brandrule"></div><div class="shell">' + leftnav +
            '<div class="maincol">' + main + '</div>' + rightrail + '</div>')
    out = os.path.join(OUT, unquote(href))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(page(h1 + " — MAM5020F", body, SPY))
    return words

def idx_in_section(section, href):
    for i, sl in enumerate(section['lessons']):
        if sl['href'] == href: return i + 1
    return 1

# ---------- index render ----------
def render_index(sections):
    cells = []
    for s in sections:
        num = s['num']
        if num.isdigit(): tag = f"Week&nbsp;{num}"
        elif num: tag = num.upper()
        else: tag = "Advanced"
        time = f' &middot; {html.escape(s["time"])}' if s['time'] else ''
        li = ''.join(f'<li><a href="{relhref(x["href"], "index.html")}">{html.escape(x["title"])}</a></li>' for x in s['lessons'])
        cells.append(f'<div class="wcell"><div class="wlabel"><b>{tag}</b>{time}</div>'
                     f'<h3>{html.escape(s["title"])}</h3><ul class="lessons">{li}</ul></div>')
    body = ('<div class="brandrule"></div>'
            '<div class="iwrap">'
            '<div class="icover">'
            '<div><div class="eyebrow">University of Cape Town &middot; MAM5020F &middot; 2026</div>'
            '<h1>Generative AI for Research</h1>'
            '<div class="sub">A postgraduate course on how generative AI is changing research practice.</div></div>'
            '<div class="iintro"><p>From literature reviews to data analysis, writing to ethics. No prior programming, '
            'machine learning, or computer science background required.</p>'
            '<div class="links"><a href="glossary.html">Glossary &rarr;</a>'
            '<a href="papers/index.html">Papers to read &rarr;</a>'
            '<a href="about.html">About &rarr;</a></div></div>'
            '</div>'
            '<div class="weeks">' + ''.join(cells) + '</div>'
            '</div>'
            '<div class="ifoot"><div class="in"><span>MAM5020F 2026</span>'
            '<span>&copy; 2026 Jonathan Shock &middot; CC BY 4.0</span></div></div>')
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(page("MAM5020F — Generative AI for Research", body))

# ---------- glossary page ----------
def render_glossary(terms):
    def first(t):
        c = t.strip()[:1].upper()
        return c if c.isalpha() else '#'
    terms = sorted(terms, key=lambda d: d['term'].lower())
    groups = {}
    for t in terms:
        groups.setdefault(first(t['term']), []).append(t)
    letters = sorted(groups)
    nav = ''.join(f'<a class="lesson" href="#L{L}">{L}</a>' for L in letters)
    leftnav = ('<div class="leftnav">'
               '<a class="back" href="index.html">&larr; All lessons</a>'
               f'<div class="navwk">Reference</div><nav class="toc">{nav}</nav></div>')
    blocks = ''
    for L in letters:
        blocks += f'<h2 class="ga" id="L{L}">{html.escape(L)}</h2>'
        for t in groups[L]:
            blocks += (f'<div class="gentry"><div class="gt">{html.escape(t["term"])}</div>'
                       f'<div class="gd">{t["definition"]}</div></div>')
    rightrail = (f'<div class="rightrail"><div class="rmeta">Glossary<br>{len(terms)} terms<br>MAM5020F</div></div>')
    main = (MARGIN_BODY + '<div class="ahead"><div class="eyebrow">MAM5020F &mdash; Generative AI for Research</div>'
            '<h1>Glossary</h1><div class="deck">Key terms used across the course, in plain language.</div></div>'
            f'<div class="abody gloss">{blocks}</div>')
    body = ('<div class="brandrule"></div><div class="shell">' + leftnav +
            '<div class="maincol">' + main + '</div>' + rightrail + '</div>')
    open(os.path.join(OUT, "glossary.html"), "w", encoding="utf-8").write(page("Glossary — MAM5020F", body))

# ---------- synthetic sections for pages outside the index sitemap ----------
def papers_section():
    pdir = os.path.join(DOCS, "papers")
    if not os.path.isdir(pdir): return None
    files = [f for f in os.listdir(pdir) if f.endswith(".html")]
    def k(f):
        if f == "index.html": return (-1, 0)
        m = re.search(r'week-(\d+)', f); return (0, int(m.group(1)) if m else 99)
    files.sort(key=k)
    lessons = []
    for f in files:
        if f == "index.html": t = "Overview"
        else:
            m = re.search(r'week-(\d+)', f); t = f"Week {m.group(1)}" if m else f[:-5]
        lessons.append({'href': f'papers/{f}', 'title': t})
    return {'num': '', 'label': 'Reading', 'title': 'Papers to read', 'lessons': lessons}

def about_section():
    p = os.path.join(DOCS, "about.html")
    if not os.path.exists(p): return None
    return {'num': '', 'label': '', 'title': 'About', 'lessons': [{'href': 'about.html', 'title': 'About the course'}]}

# ---------- main ----------
def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    gl = json.load(open(GLOSSARY, encoding="utf-8"))
    defs = {t['term']: t for t in gl['terms']}
    lessonterms = {unquote(k): v for k, v in gl['lessons'].items()}
    sections = parse_sitemap()
    os.makedirs(OUT, exist_ok=True)
    # copy every non-HTML asset (images, advanced/files downloads, etc.) into the site
    for dp, _, fns in os.walk(DOCS):
        for fn in fns:
            if fn.endswith(".html"): continue
            rel = os.path.relpath(os.path.join(dp, fn), DOCS)
            dest = os.path.join(OUT, rel)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.copy2(os.path.join(dp, fn), dest)
    render_index(sections)
    render_glossary(gl['terms'])

    # the 15 index sections share one flat order (sequential course flow);
    # papers + about are their own self-contained groups.
    main_flat = [l for s in sections for l in s['lessons']]
    groups = [(s, main_flat) for s in sections]
    ps = papers_section()
    if ps: groups.append((ps, ps['lessons']))
    ab = about_section()
    if ab: groups.append((ab, ab['lessons']))

    done = 0; errs = []; seen = set()
    for section, flat in groups:
        pos = {l['href']: i for i, l in enumerate(flat)}
        for L in section['lessons']:
            if only and not unquote(L['href']).startswith(only): continue
            seen.add(unquote(L['href']))
            try:
                render_lesson(L, section, flat, pos[L['href']], defs, lessonterms)
                done += 1
            except Exception as e:
                errs.append(f"{L['href']}: {e}")

    # report orphans (docs html not in sitemap)
    all_html = set()
    for dp, _, fns in os.walk(DOCS):
        for fn in fns:
            if fn.endswith('.html'):
                all_html.add(os.path.relpath(os.path.join(dp, fn), DOCS))
    orphans = sorted(h for h in all_html if h not in seen and h != 'index.html')

    print(f"rendered {done} lesson pages -> {OUT}")
    if errs:
        print(f"\n{len(errs)} ERRORS:")
        for e in errs: print("  -", e)
    tocs = [o for o in orphans if o.endswith('Table of Contents.html')]
    other = [o for o in orphans if o not in tocs]
    print(f"\nintentionally omitted (redundant with the new left nav): {len(tocs)} Tables of Contents")
    if other:
        print(f"STILL UNHANDLED ({len(other)}):")
        for o in other: print("  -", o)
    else:
        print("every other page handled.")

if __name__ == "__main__":
    main()
