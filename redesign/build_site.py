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
         '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,600&display=swap" rel="stylesheet">')

CSS = r"""
:root{--blue:#003A70;--fs-tag:max(.7rem,11px);--fs-lbl:max(.8rem,11.5px);--fs-mono:.85rem;--fs-nav:.95rem;--fs-meta:1.05rem;--fs-sub:1.12rem;--fs-code:1.12rem;--fs-box:1.28rem;--fs-h3:1.35rem;--fs-list:1.37rem;--fs-h3lg:1.45rem;--fs-body:1.52rem;--fs-boxtext:1.37rem;--fs-subhead:1.7rem;--blue2:#2a5298;--paper:#ffffff;--card:#ffffff;--ink:#23201b;--ink2:#3f3a32;--mut:#6a6256;--lbl:#736a5c;--rule:#dde1e6;--rule2:#c9ced5;--amber:#7c5c12}
html{font-size:85%}
*{margin:0;padding:0;box-sizing:border-box}
::selection{background:var(--blue);color:#fff}
body{background:var(--paper);color:var(--ink);font-family:'Newsreader',serif}
img{max-width:100%}
/* reading measure: cap text blocks; tables, figures and grids keep the full canvas */
.abody p,.abody li,.abody h2.section-title,.abody h3,.abody h4,.abody .intro-text,.abody blockquote{max-width:48rem}
.abody h2.section-title,.abody h3,.abody h4,.ahead h1,.icover h1,.wcell h3,.ahead .eyebrow,.icover .eyebrow{overflow-wrap:break-word;hyphens:auto}
.brandrule{height:4px;background:var(--blue)}
.mobnav{display:none}
/* ---- three-column shell ---- */
.shell{max-width:1880px;margin:0 auto;padding:0 44px;display:grid;grid-template-columns:218px minmax(0,58rem) 248px;justify-content:center;column-gap:64px;align-items:start}
.maincol{min-width:0;max-width:1340px;margin-left:0;margin-right:0}
.leftnav,.rightrail{position:sticky;top:30px;align-self:start;padding-top:46px;max-height:calc(100vh - 40px);overflow-y:auto;scrollbar-width:thin}
.leftnav .back,.mobnav .back{font-family:'Fraunces';font-size:var(--fs-lbl);letter-spacing:.1em;text-transform:uppercase;color:var(--blue);text-decoration:none;display:block;margin-bottom:26px}
.leftnav .back:hover,.mobnav .back:hover{color:var(--blue2)}
.leftnav .navwk,.mobnav .navwk{font-family:'Fraunces';font-size:var(--fs-tag);letter-spacing:.18em;text-transform:uppercase;color:var(--lbl);margin-bottom:7px;line-height:1.5}
.leftnav .navhd{font-family:'Fraunces';font-weight:500;font-size:var(--fs-nav);color:var(--ink);margin-bottom:12px;padding-bottom:11px;border-bottom:1px solid var(--rule)}
.toc{display:flex;flex-direction:column}
.toc .lesson{font-family:'Newsreader';font-size:var(--fs-meta);line-height:1.3;color:var(--ink2);text-decoration:none;padding:6px 0;display:block;transition:color .15s}
.toc .lesson:hover{color:var(--blue)}
.toc .lesson.cur{color:var(--blue);font-weight:500}
.toc .subs{display:flex;flex-direction:column;margin:3px 0 10px;border-left:1px solid var(--rule)}
.toc .subs a{font-family:'Newsreader';font-size:var(--fs-nav);line-height:1.32;color:var(--mut);text-decoration:none;padding:5px 0 5px 14px;margin-left:-1px;border-left:2px solid transparent;transition:color .15s,border-color .15s}
.toc .subs a:hover{color:var(--blue)}
.toc .subs a.on{color:var(--blue);border-left-color:var(--blue)}
.rightrail .rmeta{font-family:'Fraunces';font-size:var(--fs-tag);letter-spacing:.1em;text-transform:uppercase;color:var(--lbl);line-height:2;margin-bottom:26px;padding-bottom:20px;border-bottom:1px solid var(--rule)}
.rightrail .snote,.mobnav .snote{margin-bottom:24px;font-family:'Newsreader';font-size:var(--fs-meta);line-height:1.5;color:var(--ink2)}
.rightrail .snote .sk a,.mobnav .snote .sk a{color:inherit;text-decoration:none;border-bottom:1px dotted var(--rule2)}
.rightrail .snote .sk a:hover,.mobnav .snote .sk a:hover{color:var(--blue2);border-bottom-color:var(--blue2)}
.rightrail .snote .sk,.mobnav .snote .sk{font-family:'Fraunces';font-weight:500;font-size:var(--fs-tag);letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin-bottom:5px}
.rightrail .rhd{font-family:'Fraunces';font-size:var(--fs-tag);letter-spacing:.16em;text-transform:uppercase;color:var(--lbl);margin:0 0 12px}
/* ---- lesson header (in maincol) ---- */
.ahead{padding:44px 0 30px;border-bottom:1px solid var(--rule)}
.ahead .eyebrow{font-family:'Fraunces';font-size:var(--fs-lbl);letter-spacing:.24em;text-transform:uppercase;color:var(--blue);margin-bottom:22px}
.ahead h1{font-family:'Fraunces';font-optical-sizing:auto;font-weight:400;font-size:clamp(2.3rem,4.6vw,3.2rem);line-height:1.04;letter-spacing:-.012em;color:var(--blue);margin:0 0 16px}
.ahead .deck{font-family:'Newsreader';font-style:italic;font-size:var(--fs-box);line-height:1.4;color:var(--mut);max-width:600px}
/* ---- lesson body ---- */
.abody{padding:30px 0 56px}
.abody p{font-size:var(--fs-body);line-height:1.64;color:var(--ink);margin:0 0 27px;text-wrap:pretty}
.abody p.drop::first-letter{font-family:'Fraunces';font-weight:500;font-size:3.9rem;line-height:.8;float:left;margin:.32rem .7rem 0 0;color:var(--blue)}
.abody strong{font-weight:600}.abody em{font-style:italic}
.abody a{color:var(--blue);text-decoration:none;border-bottom:1px solid var(--blue2)}.abody a:hover{border-color:var(--blue)}
.abody h2.section-title{font-family:'Fraunces';font-weight:400;font-size:1.9rem;line-height:1.1;color:var(--blue);border-top:1px solid var(--rule);padding-top:34px;margin:44px 0 16px;scroll-margin-top:24px}
.abody h3:not(.lbl){font-family:'Fraunces';font-weight:500;font-size:var(--fs-subhead);color:var(--ink);margin:26px 0 10px}
.abody h1{font-family:'Fraunces';font-weight:500;font-size:var(--fs-subhead);color:var(--blue);margin:0 0 10px;max-width:48rem}
.abody h2:not(.section-title){font-family:'Fraunces';font-weight:500;font-size:var(--fs-subhead);color:var(--blue);margin:30px 0 12px;max-width:48rem}
.abody .highlight-box h2{color:#fff;margin-top:0}
.abody .info-box h2,.abody .warning-box h2,.abody .resource-placeholder h2,.abody .technical-detail h2,.abody .case-study h2{margin-top:0}
.abody h5,.abody h6{font-family:'Fraunces';font-weight:500;font-size:var(--fs-body);color:var(--ink);margin:18px 0 8px}
.abody :is(h4,h3.lbl){font-family:'Fraunces';font-weight:500;font-size:var(--fs-lbl);letter-spacing:.14em;text-transform:uppercase;color:var(--blue);margin:0 0 9px}
.abody :is(h4,h3.lbl).h4long{font-size:var(--fs-body);letter-spacing:0;text-transform:none;line-height:1.35}
.abody ul,.abody ol{margin:0 0 22px;padding:0;list-style:none}
.abody li{font-size:var(--fs-body);line-height:1.56;color:var(--ink2);margin-bottom:11px;padding-left:24px;position:relative}
.abody ul>li::before{content:'';position:absolute;left:0;top:.7em;width:9px;height:1px;background:var(--blue)}
.abody ol{counter-reset:li}.abody ol>li{counter-increment:li}
.abody ol>li::before{content:counter(li)'.';position:absolute;left:0;top:0;font-family:'Fraunces';color:var(--blue);font-size:var(--fs-meta)}
.abody .intro-text{border-left:2px solid var(--blue);padding:2px 0 2px 22px;margin:0 0 34px}
.abody .intro-text h2{font-family:'Fraunces';font-weight:500;font-size:var(--fs-lbl);letter-spacing:.2em;text-transform:uppercase;color:var(--blue);margin-bottom:10px}
.abody .intro-text p{font-size:var(--fs-body);color:var(--ink2)}.abody .intro-text p:last-child{margin-bottom:0}
.abody .card-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin:26px 0;align-items:start}
/* Every grid hugs the reading measure, so its right edge matches the callout boxes at any width.
   Long-card grids (grid-wide) stack single-column: two columns inside 820px would give ~402px
   cards, no better than the 3-across this rule exists to escape. Only genuinely wide content
   still breaks out to the full canvas. */
.abody :is(.card-grid,.category-grid){max-width:calc(48rem + 52px)}
/* Exactly 4 short cards: cap at 2 columns so they sit 2x2, never 3+1 with an orphan.
   Done via a 340px track minimum, not a viewport guard: 3 tracks would need a ~1068px
   container, impossible inside the 820px cap, and narrow containers fall to 1 column
   naturally (a viewport guard mis-fired at 1024px, where sidebars shrink the column). */
.abody :is(.card-grid,.category-grid):not(.grid-wide):has(> :nth-child(4)):not(:has(> :nth-child(5))){grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr))}
.abody :is(.card-grid,.category-grid).grid-wide{grid-template-columns:1fr}
.abody :is(.card-grid,.category-grid):has(table,figure,pre,iframe,svg){max-width:none}
.afoot{max-width:calc(48rem + 52px);margin:52px 0 60px;padding-top:22px;border-top:1px solid var(--rule)}
.afoot p{font-family:'Newsreader';font-size:var(--fs-lbl);line-height:1.6;color:var(--lbl);margin:0 0 6px}
.afoot .alic{color:var(--mut)}
.afoot a{color:var(--blue);text-decoration:underline;text-underline-offset:2px}
.abody .card{background:var(--card);border:1px solid var(--rule);border-radius:3px;padding:22px 24px}
.abody .card h3:not(.lbl){font-family:'Fraunces';font-weight:500;font-size:var(--fs-subhead);color:var(--blue);margin:0 0 8px}
.abody .card p{font-size:var(--fs-boxtext);line-height:1.5;color:var(--ink2);margin:0}
.abody .highlight-box{background:var(--blue);color:#fbf7ee;padding:30px 32px;margin:34px 0}
.abody .highlight-box h3:not(.lbl){font-family:'Fraunces';font-weight:500;font-size:var(--fs-subhead);color:#fff;margin:0 0 12px}
.abody .highlight-box p,.abody .highlight-box li{font-family:'Newsreader';font-size:var(--fs-boxtext);line-height:1.58;color:#e9e2d2;margin:0 0 8px}
.abody .highlight-box strong{color:#fff}.abody .highlight-box a{color:#fff;border-bottom-color:rgba(255,255,255,.5)}
.abody .highlight-box ul li::before{background:#bcd0e6}
.abody .info-box,.abody .technical-detail,.abody .case-study,.abody .decision-framework{background:var(--card);border:1px solid var(--rule);border-left:3px solid var(--blue);padding:22px 26px;margin:28px 0}
.abody :is(.info-box,.technical-detail,.case-study,.decision-framework,.warning-box,.resource-placeholder,.highlight-box,.verdict){max-width:calc(48rem + 52px)}
.abody :is(.info-box,.technical-detail,.case-study,.decision-framework,.warning-box,.resource-placeholder,.highlight-box,.verdict):has(table,.card-grid,.category-grid,figure,pre,.video-container,iframe,svg){max-width:none}
.abody .info-box p,.abody .info-box li,.abody .technical-detail p,.abody .technical-detail li,.abody .case-study p,.abody .case-study li,.abody .decision-framework p,.abody .decision-framework li,.abody .resource-placeholder p,.abody .resource-placeholder li{font-family:'Newsreader';font-size:var(--fs-boxtext);line-height:1.58;color:var(--ink2);margin:0 0 8px}
.abody .technical-detail{border-left-color:var(--mut)}
.abody .technical-detail :is(h4,h3.lbl){color:var(--mut)}
.abody .case-study{border-left-color:#b07a1e}
.abody .case-study>h3:not(.lbl):first-child::before{content:'Case study';display:block;font-family:'Fraunces';font-weight:500;font-size:var(--fs-tag);letter-spacing:.16em;text-transform:uppercase;color:var(--amber);margin-bottom:7px}
.abody .case-study h3:not(.lbl),.abody .decision-framework h3:not(.lbl){font-family:'Fraunces';font-weight:500;font-size:var(--fs-subhead);color:var(--blue);margin:0 0 8px}
.abody .warning-box{background:#f6eedb;border-left:3px solid var(--amber);padding:22px 26px;margin:28px 0}
.abody .warning-box :is(h4,h3.lbl){color:var(--amber)}
.abody .warning-box p,.abody .warning-box li{font-family:'Newsreader';font-size:var(--fs-boxtext);line-height:1.6;color:#574d33;margin:0 0 8px}
.abody .tscroll{overflow-x:auto;margin:26px 0}.abody .tscroll>table{margin:0}
.abody table{width:100%;border-collapse:collapse;margin:26px 0;font-family:'Newsreader';font-size:var(--fs-boxtext)}
.abody th{font-family:'Fraunces';font-weight:500;font-size:var(--fs-tag);letter-spacing:.1em;text-transform:uppercase;color:var(--blue);text-align:left;padding:10px 14px 10px 0;border-bottom:1.5px solid var(--blue)}
.abody td{padding:11px 14px 11px 0;border-bottom:1px solid var(--rule);color:var(--ink2);line-height:1.5;vertical-align:top}
.abody .step-list{list-style:none;counter-reset:s;padding:0;margin:26px 0}
.abody .step-list>li{counter-increment:s;position:relative;padding:2px 0 22px 56px;border:0;margin:0;font-size:var(--fs-body);color:var(--ink2)}
.abody .step-list>li::before{content:counter(s);position:absolute;left:0;top:-4px;font-family:'Fraunces';font-weight:400;font-size:2.2rem;color:var(--blue);line-height:1}
.abody .step-list>li::after{content:none}
.abody .code-block,.abody pre{background:#04233f;color:#e9e3d6;font-family:'SF Mono',Menlo,Consolas,monospace;font-size:var(--fs-mono);line-height:1.6;padding:18px 22px;margin:26px 0;overflow-x:auto;border-left:3px solid var(--blue2);white-space:pre-wrap}
.abody .code-block *{font-family:inherit}
.abody code{font-family:'SF Mono',Menlo,Consolas,monospace;font-size:var(--fs-code);background:#eef1f5;padding:1px 5px;color:#7a4a12;overflow-wrap:anywhere}
/* In a heading or a table cell, code takes the container's step: the prose step would dwarf an
   11.2px header, and an em multiplier lands off-scale (.85em of a 12.8px h4 = 10.88px). */
.abody :is(h1,h2,h3,h4,h5,h6,th,td) code{font-size:1em}
/* small is otherwise unstyled and falls through to the UA default (.8333em) = off-scale */
.abody small{font-size:var(--fs-meta)}
.abody :is(th,td) small{font-size:1em}
.abody .code-block code,.abody pre code{background:none;color:inherit;padding:0}
.abody .resource-placeholder{background:var(--card);border:1px solid var(--rule);border-top:3px solid var(--blue);padding:22px 26px;margin:26px 0}
.abody .resource-placeholder :is(h4,h3.lbl){color:var(--blue)}
/* ===== baseline + bespoke long-tail components ===== */
.abody{font-size:var(--fs-body);line-height:1.62}
.abody .intro-section p{font-size:var(--fs-body)}
.abody .empty-note p{font-size:var(--fs-meta)}
/* explanatory SVG diagrams (figure.diagram) */
.abody figure.diagram{margin:46px 0}
.abody figure.diagram>svg{display:block;width:100%;height:auto;border-radius:3px}
@media(max-width:600px){.abody figure.diagram{overflow-x:auto}.abody figure.diagram>svg{min-width:560px}}
.abody figure.diagram figcaption{font-family:'Fraunces';font-style:italic;font-size:var(--fs-meta);line-height:1.45;color:var(--lbl);text-align:center;margin-top:16px}
.abody .section{margin:0 0 8px}
.abody .part-title,.abody .intro-section h3:not(.lbl){font-family:'Fraunces';font-weight:500;font-size:var(--fs-subhead);color:var(--blue);margin:26px 0 10px}
/* callout boxes */
.abody .analogy-box,.abody .how-it-works,.abody .key-concepts,.abody .research-applications,.abody .instructor-box,.abody .prompt-example,.abody .empty-note,.abody .caveat-item,.abody .architecture-examples,.abody .model-details,.abody .paywalled-section,.abody .video-section,.abody .intro-section{background:var(--card);border:1px solid var(--rule);border-left:3px solid var(--blue);padding:20px 24px;margin:24px 0;border-radius:3px}
.abody .cm,.abody .comment{color:#9fb0c7;background:none;border:0;padding:0;margin:0;font-family:inherit;font-style:normal}
.abody .analogy-box p,.abody .how-it-works p,.abody .key-concepts p,.abody .research-applications p,.abody .instructor-box p,.abody .prompt-example p,.abody .intro-section p,.abody .empty-note p{font-family:'Newsreader';font-size:var(--fs-boxtext);line-height:1.6;color:var(--ink2);margin:0 0 8px}
.abody .empty-note{font-style:italic;color:var(--mut)}
/* generic cards + grids */
.abody .tool-card,.abody .category-card,.abody .objective-card,.abody .level-card,.abody .architecture-card,.abody .phase-card,.abody .comparison-card,.abody .audience-card,.abody .week-card,.abody .paper-card,.abody .structure-item{background:var(--card);border:1px solid var(--rule);padding:18px 22px;margin:14px 0;border-radius:3px}
.abody .category-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:18px;margin:22px 0;align-items:start}
.abody .category-grid>*{margin:0}
.abody .model-list{margin:10px 0 0;padding:0}
/* callouts nested inside cards must stay compact, not squeeze the text to one word per line */
.abody .category-card .model-details,.abody .card .model-details,.abody .category-card .info-box,.abody .card .info-box,.abody .category-card .highlight-box,.abody .card .highlight-box,.abody .category-card .technical-detail,.abody .card .technical-detail,.abody .category-card .analogy-box,.abody .card .analogy-box{padding:13px 16px;margin:13px 0 0}
.abody .category-card .model-details p,.abody .card .model-details p,.abody .category-card .highlight-box p,.abody .card .highlight-box p,.abody .category-card .info-box p,.abody .card .info-box p,.abody .category-card .technical-detail p,.abody .card .technical-detail p{font-size:var(--fs-boxtext);line-height:1.5;margin:0 0 6px}
.abody .objective-number,.abody .num{font-family:'Fraunces';font-weight:400;font-size:1.6rem;color:var(--blue);line-height:1}
/* topic list */
.abody .topics-list{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:6px 24px;margin:18px 0}
.abody .topic-item{font-family:'Newsreader';font-size:var(--fs-body);line-height:1.4;color:var(--ink2);padding:6px 0 6px 18px;position:relative}
.abody .topic-item::before{content:'';position:absolute;left:0;top:.65em;width:9px;height:1px;background:var(--blue)}
/* timeline (handles era/description and date/title/content variants) */
.abody .timeline-items,.abody .timeline,.abody .timeline-section{margin:22px 0}
.abody .timeline-item{position:relative;padding:0 0 20px 26px;margin-left:4px;border-left:2px solid var(--rule)}
.abody .timeline-item:last-child{border-left-color:transparent;padding-bottom:0}
.abody .timeline-marker,.abody .marker-circle{display:none}
.abody .timeline-era,.abody .timeline-date,.abody .era-badge{position:relative;font-family:'Fraunces';font-weight:500;font-size:var(--fs-tag);letter-spacing:.1em;text-transform:uppercase;color:var(--blue);margin-bottom:5px}
.abody .timeline-item>.timeline-era::before,.abody .timeline-item>.timeline-date::before,.abody .timeline-item>.era-badge::before{content:'';position:absolute;left:-33px;top:1px;width:11px;height:11px;border-radius:50%;background:var(--blue);border:2px solid var(--paper)}
.abody .timeline-title{font-family:'Fraunces';font-weight:500;font-size:var(--fs-body);color:var(--ink);margin-bottom:4px}
.abody .timeline-description,.abody .timeline-content{font-family:'Newsreader';font-size:var(--fs-boxtext);line-height:1.55;color:var(--ink2)}
.abody .timeline-description strong,.abody .timeline-content strong{color:var(--ink)}
/* stats */
.abody .stat-box{display:flex;flex-direction:column;gap:5px;background:var(--card);border:1px solid var(--rule);border-left:3px solid var(--blue);padding:16px 20px;margin:20px 0;border-radius:3px}
.abody .stat-number{font-family:'Fraunces';font-weight:500;font-size:2rem;color:var(--blue);line-height:1}
.abody .stat-label{font-family:'Newsreader';font-size:var(--fs-nav);line-height:1.45;color:var(--mut)}
/* discussion questions */
.abody .question-set{margin:24px 0}
.abody .q-tag{display:inline-block;font-family:'Fraunces';font-weight:500;font-size:var(--fs-tag);letter-spacing:.1em;text-transform:uppercase;color:#fff;background:var(--blue);padding:2px 9px;border-radius:3px;margin-right:9px;vertical-align:middle}
/* paper cards */
.abody .paper-title{font-family:'Fraunces';font-weight:500;font-size:var(--fs-body);color:var(--blue);margin:0 0 4px}
.abody .paper-meta{font-family:'Newsreader';font-style:italic;font-size:var(--fs-meta);color:var(--mut);margin:0 0 8px}
.abody .paper-actions{display:flex;flex-wrap:wrap;gap:14px;margin-top:8px;align-items:center}
.abody .source-link,.abody .tool-url{font-family:'Fraunces';font-size:var(--fs-mono);color:var(--blue)}
.abody .tool-pricing,.abody .sublesson-tag{font-family:'Fraunces';font-size:var(--fs-tag);letter-spacing:.06em;text-transform:uppercase;color:var(--mut)}
.abody .access{font-family:'Newsreader';font-size:var(--fs-meta);line-height:1.5;color:var(--mut)}
/* inline badges + indicators */
.abody .level-tag,.abody .card-label{display:inline-block;font-family:'Fraunces';font-size:var(--fs-tag);letter-spacing:.1em;text-transform:uppercase;color:var(--blue);background:#eef1f5;padding:2px 8px;border-radius:3px}
.abody .verdict{background:var(--card);border:1px solid var(--rule);border-left:3px solid var(--mut);padding:16px 20px;margin:0 0 14px;border-radius:3px}
.abody .verdict p{font-size:var(--fs-boxtext);line-height:1.55;color:var(--ink2);margin:0}
.abody .verdict-yes{border-left-color:#2c6e3f}.abody .verdict-no{border-left-color:#9a2f2f}
.abody .verdict-yes strong{color:#2c6e3f}.abody .verdict-no strong{color:#9a2f2f}
.abody .card.risk-low{border-left:3px solid #2c6e3f}
.abody .card.risk-medium{border-left:3px solid #b07a1e}
.abody .card.risk-high{border-left:3px solid #9a2f2f}
.abody .prompt-label{display:block;font-family:'Fraunces';font-weight:500;font-size:var(--fs-tag);letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin-bottom:6px}
/* video — restore responsive 16:9 (the source kept this in <head>, which we drop) */
.abody .video-container{position:relative;width:100%;padding-bottom:56.25%;height:0;overflow:hidden;margin:26px 0;border-radius:3px;background:#04233f}
.abody .video-container iframe,.abody .video-container img,.abody .video-container>a,.abody .video-container video{position:absolute;top:0;left:0;width:100%;height:100%;border:0;object-fit:cover}
.abody{overflow-wrap:break-word}
.abody .video-section iframe{width:100%;aspect-ratio:16/9;border:0;border-radius:3px}
.abody iframe{max-width:100%}
.abody iframe[src*="youtube"]{height:auto;aspect-ratio:16/9}
.abody a.ytlink{display:inline-flex;align-items:center;gap:13px;background:var(--card);border:1px solid var(--rule);border-left:3px solid #c4302b;border-radius:3px;padding:13px 20px;margin:10px 0;font-family:'Fraunces';font-size:var(--fs-sub);color:var(--blue);text-decoration:none;line-height:1.2}
.abody a.ytlink:hover{border-color:#c4302b}
.abody a.ytlink .ytpl{color:#c4302b;font-size:var(--fs-box);line-height:1}
.abody a.ytlink small{display:block;font-family:'Newsreader';font-size:var(--fs-lbl);color:var(--lbl);font-style:italic;margin-top:3px}
.abody .video-badge{font-family:'Fraunces';font-weight:500;font-size:var(--fs-tag);letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin-bottom:8px}
/* very slight curve on the boxes */
.abody .highlight-box,.abody .info-box,.abody .technical-detail,.abody .case-study,.abody .decision-framework,.abody .warning-box,.abody .code-block,.abody pre,.abody .resource-placeholder{border-radius:3px}
.prevnext{padding:28px 0 60px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:16px;border-top:1px solid var(--rule)}
.prevnext a{display:flex;flex-direction:column;gap:5px;text-decoration:none;max-width:46%}
.prevnext .d{font-family:'Fraunces';font-size:var(--fs-tag);letter-spacing:.14em;text-transform:uppercase;color:var(--lbl)}
.prevnext .pt{font-family:'Fraunces';font-size:var(--fs-meta);color:var(--blue)}
.prevnext .next{text-align:right;margin-left:auto}
@media(max-width:980px){.shell{grid-template-columns:1fr;column-gap:0}.maincol{width:100%;margin:0}.abody{overflow-wrap:break-word}.abody table{display:block;overflow-x:auto}.leftnav,.rightrail{display:none}.mobnav{display:block;margin:20px 0 2px}}
.mobnav details{background:var(--card);border:1px solid var(--rule);border-radius:3px;margin-bottom:10px}.mobnav summary{padding:12px 16px;font-family:'Fraunces';font-weight:500;font-size:var(--fs-lbl);letter-spacing:.14em;text-transform:uppercase;color:var(--blue);cursor:pointer}.mobnav .mnbody{padding:4px 16px 14px}.mobnav .back{margin-bottom:14px}.mobnav .snote{margin-top:16px}
/* 981-1240px: two columns; key terms move into the in-column panel, contents stay in the left sidebar */
@media(min-width:981px) and (max-width:1240px){.shell{grid-template-columns:218px minmax(0,1fr)}.rightrail{display:none}.mobnav{display:block;margin:20px 0 2px}.mobnav>details:first-child{display:none}.mobnav:not(:has(>details+details)){display:none}}
/* ---- INDEX / landing ---- */
.iwrap{max-width:1400px;margin:0 auto;padding:0 36px}
.icover{display:grid;grid-template-columns:1.5fr 1fr;gap:64px;align-items:end;padding:52px 0 38px;border-bottom:1px solid var(--rule)}
.icover .eyebrow{font-family:'Fraunces';font-size:var(--fs-lbl);letter-spacing:.22em;text-transform:uppercase;color:var(--blue);margin-bottom:22px}
.icover h1{font-family:'Fraunces';font-optical-sizing:auto;font-weight:400;font-size:clamp(2.9rem,5vw,4.4rem);line-height:1.0;letter-spacing:-.015em;color:var(--blue)}
.icover .sub{font-family:'Newsreader';font-style:italic;font-size:var(--fs-h3);line-height:1.35;color:var(--mut);margin-top:18px}
.iintro p{font-size:var(--fs-sub);line-height:1.62;color:var(--ink2)}
.iintro .links{margin-top:20px;display:flex;flex-wrap:wrap;gap:22px}
.iintro .links a{font-family:'Fraunces';font-size:var(--fs-meta);color:var(--blue);text-decoration:none;border-bottom:1px solid var(--rule2);padding-bottom:2px}
.iintro .links a:hover{border-color:var(--blue)}
.part{padding:30px 0 0}
.phead{font-family:'Fraunces';font-weight:400;font-size:1.45rem;color:var(--ink);border-bottom:1px solid var(--rule2);padding-bottom:10px;margin:0 0 28px}
.phead span{font-family:'Fraunces';font-weight:500;font-size:var(--fs-lbl);letter-spacing:.18em;text-transform:uppercase;color:var(--blue);margin-right:12px}
.pgrid{display:grid;grid-template-columns:1fr 1fr;gap:10px 56px;align-items:start}
.wcell{display:flex;gap:18px;padding-bottom:30px;min-width:0}
.wnum{font-family:'Fraunces';font-weight:500;font-size:2.5rem;line-height:.9;color:var(--blue);min-width:46px;text-align:right}
.wbody{flex:1;min-width:0}
.wrow{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:4px 14px}
.wtime{font-family:'Fraunces';font-size:var(--fs-tag);letter-spacing:.12em;text-transform:uppercase;color:var(--lbl);white-space:nowrap}
.wcell.lite .wnum{color:var(--lbl);font-size:1.4rem;padding-top:8px}
.wcell.lite h3{font-size:var(--fs-h3)}
.wcell h3{font-family:'Fraunces';font-weight:500;font-size:var(--fs-h3lg);color:var(--blue);margin:0 0 6px;line-height:1.1}
.lessons{list-style:none;margin:12px 0 0;padding:0}
.lessons li{border-top:1px solid var(--rule)}
.lessons a{display:block;font-size:var(--fs-meta);color:var(--ink2);text-decoration:none;padding:9px 0;line-height:1.32;transition:color .15s,padding .15s}
.lessons a:hover{color:var(--blue);padding-left:6px}
.ifoot{border-top:1px solid var(--rule);margin-top:18px}
.ifoot .in{max-width:1400px;margin:0 auto;padding:24px 36px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;font-family:'Fraunces';font-size:var(--fs-mono);color:var(--lbl)}
.ifoot a{color:var(--blue);text-decoration:none}
@media(max-width:860px){.icover{grid-template-columns:1fr;gap:26px;align-items:start}.pgrid{grid-template-columns:1fr}}
/* ---- GLOSSARY ---- */
.gloss .ga{font-family:'Fraunces';font-weight:400;font-size:1.7rem;color:var(--blue);border-top:1px solid var(--rule);padding-top:22px;margin:38px 0 6px;scroll-margin-top:24px}
.gloss .gentry{padding:13px 0;border-top:1px solid var(--rule)}
.gloss .ga + .gentry{border-top:0}
.gloss .gt{font-family:'Fraunces';font-weight:500;font-size:var(--fs-h3);color:var(--ink);margin-bottom:4px}
.gloss .gd{font-family:'Newsreader';font-size:var(--fs-box);line-height:1.55;color:var(--ink2)}
.gloss .toc .lesson{font-family:'Fraunces';letter-spacing:.05em}
/* ---- reader text-size control ---- */
.tsize{position:fixed;right:18px;bottom:18px;z-index:300;display:flex;align-items:flex-end;gap:1px;background:var(--card);border:1px solid var(--rule2);border-radius:7px;padding:3px 5px;box-shadow:0 2px 12px rgba(0,20,40,.1)}
.tsize button{font-family:'Fraunces';color:var(--mut);background:none;border:0;border-radius:4px;cursor:pointer;line-height:1;padding:5px 8px;transition:background .15s,color .15s}
.tsize button:nth-child(1){font-size:13px}
.tsize button:nth-child(2){font-size:16px}
.tsize button:nth-child(3){font-size:20px}
.tsize button:hover{color:var(--blue)}
.tsize button[aria-pressed="true"]{background:var(--blue);color:#fff}
.tsize button:focus-visible{outline:2px solid var(--blue);outline-offset:2px}
.rightrail .tsize{position:static;display:inline-flex;box-shadow:none;margin:0 0 22px}
@media print{.tsize,.rightrail .tsize{display:none}}
@media(min-width:1241px){body:has(.rightrail)>.tsize{display:none}html.hr .rightrail .tsize{visibility:visible}}
@media(max-width:600px){.tsize{right:10px;bottom:10px;padding:2px 3px}.tsize button{padding:3px 6px}.tsize button:nth-child(1){font-size:11px}.tsize button:nth-child(2){font-size:13px}.tsize button:nth-child(3){font-size:16px}.shell{padding:0 22px}}
/* ---- hideable margins: a labelled toggle at the top of each margin ---- */
.navtoggle{display:flex;align-items:center;font-family:'Fraunces';font-size:var(--fs-lbl);letter-spacing:.04em;color:var(--mut);background:none;border:0;cursor:pointer;padding:0;margin:0 0 18px;text-align:left}
.navtoggle:hover{color:var(--blue)}
.navtoggle:focus-visible{outline:2px solid var(--blue);outline-offset:3px;border-radius:3px}
.navtoggle .ls{display:none}
.skip{position:absolute;left:-9999px;top:8px;z-index:400;background:var(--blue);color:#fff;padding:8px 14px;font-family:'Fraunces';font-size:var(--fs-lbl);text-decoration:none}.skip:focus{left:8px}
html.hl .navtoggle[data-m="l"] .lh{display:none}
html.hl .navtoggle[data-m="l"] .ls{display:inline}
html.hr .navtoggle[data-m="r"] .lh{display:none}
html.hr .navtoggle[data-m="r"] .ls{display:inline}
@media(min-width:981px){
  /* keep columns + gaps; blank the sidebar but keep its toggle clickable */
  html.hl .leftnav{visibility:hidden}
  html.hr .rightrail{visibility:hidden}
  html.hl .leftnav .navtoggle{visibility:visible}
  html.hr .rightrail .navtoggle{visibility:visible}
}
@media(max-width:980px){.navtoggle{display:none}}
@media print{.navtoggle{display:none}}
@media print{.abody .highlight-box,.abody .highlight-box :not(code){background:none!important;color:var(--ink)!important}.abody .highlight-box{border:1px solid var(--blue)}.abody :is(.code-block,pre){background:none;color:var(--ink);border:1px solid var(--rule2)}.abody .cm,.abody .comment{color:var(--mut)}.mobnav,.prevnext{display:none}}
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
        # a border drawn round padding that has just been removed would sit on the text: drop it too
        if re.search(r'(^|;)\s*padding[\w-]*\s*:', m.group(1), re.I):
            d = [x for x in d if not re.match(r'\s*border[\w-]*\s*:', x, re.I)]
        return (' style="' + ';'.join(d) + '"') if d else ''
    return re.sub(r'\s*style="([^"]*)"', fix, c)

# YouTube videos whose owners disabled off-site embedding (verified in-browser).
# Their iframes render as "Video unavailable"; swap them for an honest link-card.
KNOWN_DEAD_VIDEOS = {"Ub3GoFaUcds", "sOPDGQjFcuM"}
def fix_dead_videos(c):
    def rep(m):
        vid = m.group(1)
        if vid not in KNOWN_DEAD_VIDEOS:
            return m.group(0)
        url = f"https://www.youtube.com/watch?v={vid}"
        return (f'<a class="ytlink" href="{url}" target="_blank" rel="noopener">'
                f'<span class="ytpl" aria-hidden="true">&#9654;</span>'
                f'<span class="ytlt">Watch on YouTube'
                f'<small>this video only plays on YouTube &middot; opens in a new tab</small></span></a>')
    return re.sub(r'<iframe\b[^>]*?/embed/([A-Za-z0-9_-]+)[^>]*>\s*(?:</iframe>)?', rep, c)

# Card grids whose cards carry long prose become unreadable towers at 3-4
# columns. Measure at build time; 3+ cards averaging >=45 words get a class
# that widens the tracks so they lay out two-across.
def widen_long_grids(c):
    out = []; i = 0
    pat = re.compile(r'<div class="(card-grid|category-grid)">')
    while True:
        m = pat.search(c, i)
        if not m:
            out.append(c[i:]); break
        j = m.end(); depth = 1; end = len(c)
        for mm in re.finditer(r'<div\b|</div>', c[j:]):
            depth += 1 if mm.group() == '<div' else -1
            if depth == 0:
                end = j + mm.start(); break
        block = c[j:end]
        cards = len(re.findall(r'<div class="(?:card|tool-card|category-card)[" ]', block))
        words = len(strip_tags(block).split())
        cls = m.group(1)
        # cards >= 3 is deliberate, not an off-by-one. Two-card grids are almost always contrast
        # pairs read ACROSS ("What AI Does Well | What AI Can Miss", "Strengths | Limitations",
        # some with tick/cross markers); grid-wide stacks single-column, which would destroy the
        # comparison. Relaxing this to >= 2 restyles 49 such pairs site-wide. Jonathan reviewed
        # them on 2026-07-16 and chose to keep them side-by-side, accepting ~402px cards.
        if cards >= 3 and words / cards >= 45:
            cls += ' grid-wide'
        out.append(c[i:m.start()]); out.append(f'<div class="{cls}">')
        i = j
    return ''.join(out)

# h4 is styled as a short spaced-capitals label ("What it is"). Headings longer than
# H4_LABEL_WORDS words (sentences, full citations) are hard to read that way, so they get
# class h4long, set in ordinary type.
# Headings inside SVG, <pre> code samples, scripts and styles are left alone. Inline <code> is
# not skipped, since headings contain it.
H4_LABEL_WORDS = 7
H4_SKIP = re.compile(r'<(svg|pre|script|style|textarea)\b.*?</\1\s*>', re.S | re.I)
H4_TAG = re.compile(r'<h4\b((?:[^>"\']|"[^"]*"|\'[^\']*\')*)>(.*?)</h4\s*>', re.S | re.I)
H4_CLASS = re.compile(r'(\s)class\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s"\'>]+))', re.I)
def mark_long_h4(c):
    def _mark(m):
        attrs, inner = m.group(1), m.group(2)
        words = strip_tags(re.sub(r'<br\b[^>]*>', ' ', inner, flags=re.I)).split()
        if len(words) <= H4_LABEL_WORDS:
            return m.group(0)
        cm = H4_CLASS.search(attrs)
        if cm:
            old = next(g for g in cm.groups()[1:] if g is not None)
            attrs = attrs[:cm.start()] + f'{cm.group(1)}class="h4long {html.escape(old, quote=True)}"' + attrs[cm.end():]
        else:
            attrs += ' class="h4long"'
        return f'<h4{attrs}>{inner}</h4>'
    out, i = [], 0
    for s in H4_SKIP.finditer(c):
        out.append(H4_TAG.sub(_mark, c[i:s.start()])); out.append(s.group(0))
        i = s.end()
    out.append(H4_TAG.sub(_mark, c[i:]))
    return ''.join(out)

H_TAG = re.compile(r'<(/?)h([234])\b((?:[^>"\']|"[^"]*"|\'[^\']*\')*)>', re.I)
def relevel_h4(c):
    """An h4 straight under an h2 skips a level for screen readers; make it h3.lbl (same look)."""
    out, i, state = [], 0, [None]
    def walk(seg):
        res, j, open_stack = [], 0, []
        for m in H_TAG.finditer(seg):
            close, lv, attrs = m.group(1), m.group(2), m.group(3)
            tag = m.group(0)
            if not close:
                if lv in '23': state[0] = lv
                if lv == '4' and state[0] == '2':
                    cm = H4_CLASS.search(attrs)
                    if cm:
                        old = next(g for g in cm.groups()[1:] if g is not None)
                        attrs = attrs[:cm.start()] + f'{cm.group(1)}class="lbl {html.escape(old, quote=True)}"' + attrs[cm.end():]
                    else:
                        attrs += ' class="lbl"'
                    tag = f'<h3{attrs}>'; open_stack.append('3')
                elif lv == '4':
                    open_stack.append('4')
            elif lv == '4':
                tag = f'</h{open_stack.pop() if open_stack else "4"}>'
            res.append(seg[j:m.start()]); res.append(tag); j = m.end()
        res.append(seg[j:]); return ''.join(res)
    for sk in H4_SKIP.finditer(c):
        out.append(walk(c[i:sk.start()])); out.append(sk.group(0)); i = sk.end()
    out.append(walk(c[i:]))
    return ''.join(out)

TABLE_RE = re.compile(r'<table\b.*?</table>', re.S | re.I)
def wrap_tables(c):
    """A table wider than the column scrolls inside its own box rather than running under the right sidebar."""
    return TABLE_RE.sub(lambda m: '<div class="tscroll">' + m.group(0) + '</div>', c)

SVG_RE = re.compile(r'<svg\b[^>]*role="img"[^>]*>.*?</svg>', re.S)
def describe_svgs(c):
    """role="img" hides a diagram's own labels from screen readers; repeat them, in source order, in its <desc>."""
    def one(m):
        svg = m.group(0)
        labels = [strip_tags(t) for t in re.findall(r'<text\b[^>]*>(.*?)</text>', svg, re.S)]
        labels = [l for l in labels if l]
        if not labels or '<desc>' not in svg: return svg
        return re.sub(r'</desc>', lambda _: ' Labels: ' + '; '.join(labels) + '.</desc>', svg, count=1)
    return SVG_RE.sub(one, c)

# Left-margin label. Advanced Track sections have the same label and title, so print it once.
def navwk_text(section):
    label, title = section["label"], section["title"]
    if label.strip() == title.strip():
        return html.escape(title)
    return f'{html.escape(label)} &middot; {html.escape(title)}'

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
           'if(s)d.style.fontSize=(["85%","95%","106%"][s]||"85%");'
           'if(localStorage.getItem("mam-hide-left")=="1")d.classList.add("hl");'
           'if(localStorage.getItem("mam-hide-right")=="1")d.classList.add("hr");}catch(e){}</script>')

# reshow tabs + collapse/expand wiring for the side margins (shell pages only)
NAV_TOG_L = '<button class="navtoggle" type="button" data-m="l" aria-expanded="true"><span class="lh">&laquo; Hide left sidebar</span><span class="ls">&raquo; Show left sidebar</span></button>'
NAV_TOG_R = '<button class="navtoggle" type="button" data-m="r" aria-expanded="true"><span class="lh">Hide key terms &raquo;</span><span class="ls">&laquo; Show key terms</span></button>'
MARGIN_BODY = ('<script>document.addEventListener("click",function(e){'
               'var t=e.target.closest?e.target.closest("[data-m]"):null;if(!t)return;'
               'var m=t.getAttribute("data-m"),k=m=="l"?"mam-hide-left":"mam-hide-right",c=m=="l"?"hl":"hr";'
               'var on=localStorage.getItem(k)=="1";try{localStorage.setItem(k,on?"0":"1");}catch(e){}'
               'document.documentElement.classList.toggle(c,!on);t.setAttribute("aria-expanded",on?"true":"false");});'
               'document.addEventListener("DOMContentLoaded",function(){document.querySelectorAll(".navtoggle").forEach(function(b){var c=b.getAttribute("data-m")=="l"?"hl":"hr";'
               'b.setAttribute("aria-expanded",document.documentElement.classList.contains(c)?"false":"true");});});</script>')
# the text-size group: fixed bottom-right on every page, plus a copy at the top of the right
# rail on pages that have one (the fixed copy is hidden there, so it never covers rail text)
TS_GROUP = ('<div class="tsize" role="group" aria-label="Text size">'
            '<button type="button" data-ts="0" aria-label="Default text size">A</button>'
            '<button type="button" data-ts="1" aria-label="Larger text size">A</button>'
            '<button type="button" data-ts="2" aria-label="Largest text size">A</button></div>')
TS_BODY = (TS_GROUP +
           '<script>(function(){var S=["85%","95%","106%"],K="mam-textsize";'
           'function ap(i){document.documentElement.style.fontSize=S[i]||S[0];'
           'var b=document.querySelectorAll(".tsize button");'
           'for(var k=0;k<b.length;k++)b[k].setAttribute("aria-pressed",b[k].getAttribute("data-ts")==i?"true":"false");}'
           'var v=0;try{v=parseInt(localStorage.getItem(K))||0;}catch(e){}ap(v);'
           'document.addEventListener("click",function(e){var t=e.target.closest?e.target.closest(".tsize button"):null;'
           'if(!t)return;var i=parseInt(t.getAttribute("data-ts"))||0;ap(i);'
           'try{localStorage.setItem(K,i);}catch(e){}});})();</script>')

def page(title, body, script=""):
    return ('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
            f'<title>{html.escape(title)}</title>{FONTS}<style>{CSS}</style>{TS_HEAD}</head>'
            f'<body><a class="skip" href="#main">Skip to main content</a>{body}{script}{TS_BODY}{ANALYTICS}</body></html>')

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
    c = fix_dead_videos(c)                 # embedding-disabled YouTube -> link-card
    c = widen_long_grids(c)                # long-prose card grids -> two-across
    c = mark_long_h4(c)                    # sentence-length h4s -> ordinary type
    c = relevel_h4(c)                      # h4 straight under h2 -> h3.lbl
    c = describe_svgs(c)                   # diagram labels into <desc>
    c = wrap_tables(c)                     # wide tables scroll in their own box
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
    leftnav = ('<div class="leftnav">' + NAV_TOG_L +
               f'<a class="back" href="{back}">&larr; All lessons</a>'
               f'<div class="navwk">{navwk_text(section)}</div>'
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
            slug = re.sub(r'[^a-z0-9]+', '-', term.lower()).strip('-')
            gh = relhref('glossary.html', href)
            snotes += (f'<div class="snote"><div class="sk"><a href="{gh}#gt-{slug}">'
                       f'{html.escape(term)}</a></div>{d["definition"]}</div>')
    rail_terms = (f'<div class="rhd">Key terms</div>{snotes}') if snotes else ''
    rightrail = ('<div class="rightrail">' + (NAV_TOG_R if snotes else '') + TS_GROUP + f'<div class="rmeta">{meta}</div>{rail_terms}</div>')

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

    mobterms = (f'<details><summary>Key terms</summary><div class="mnbody">{snotes}</div></details>') if snotes else ''
    mobnav = ('<div class="mobnav">'
              f'<details><summary>Contents</summary><div class="mnbody"><a class="back" href="{back}">&larr; All lessons</a>'
              f'<div class="navwk">{navwk_text(section)}</div>'
              f'<nav class="toc">{items}</nav></div></details>' + mobterms + '</div>')
    # AI-authorship disclosure + licence. Lives in the page chrome, NOT in content/, because the
    # renderer only carries `.content` across: the old per-page .ai-notice sat outside it and was
    # silently dropped from 83 of 84 lessons by the Press redesign (71d15ee) for three weeks.
    # verify_content.py compares .content to .abody, so it could never have caught that.
    disc = relhref('course-introduction/AI Content Disclaimer.html', href)
    afoot = ('<div class="afoot">'
             f'<p class="aidisc">Drafted with Claude (Anthropic) and reviewed by Jonathan Shock '
             f'before publication. AI-generated errors are possible &mdash; if you spot one, please email '
             f'<a href="mailto:jonathan.shock@uct.ac.za">jonathan.shock@uct.ac.za</a>. '
             f'Full detail: <a href="{disc}">AI Content Disclaimer</a>.</p>'
             '<p class="alic">&copy; 2026 Jonathan Shock &middot; MAM5020F: Generative AI for Research '
             '&middot; <a href="https://creativecommons.org/licenses/by/4.0/" rel="license noopener" '
             'target="_blank">CC BY 4.0</a></p></div>')
    main = (MARGIN_BODY + '<div class="ahead"><div class="eyebrow">MAM5020F &mdash; Generative AI for Research</div>'
            f'<h1>{html.escape(h1)}</h1>' + (f'<div class="deck">{html.escape(deck)}</div>' if deck else '') + '</div>'
            + mobnav + f'<div class="abody">{c}</div>{pn}{afoot}')
    body = ('<div class="brandrule"></div><div class="shell">' + leftnav +
            '<main class="maincol" id="main">' + main + '</main>' + rightrail + '</div>')
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
    def part_of(s):
        n = s['num'].upper()
        if n in ('I', 'II'): return 0
        if n.isdigit():
            w = int(n)
            return 1 if w <= 2 else 2 if w <= 4 else 3 if w <= 8 else 4
        return 5
    PARTS = [("", "Orientation &amp; Introduction"), ("Part 1", "Foundations"),
             ("Part 2", "Impacts &amp; Ethics"), ("Part 3", "AI in the Research Workflow"),
             ("Part 4", "Frontiers &amp; Critique"), ("", "Advanced Track")]
    groups = {i: [] for i in range(6)}
    for s in sections:
        groups[part_of(s)].append(s)
    parts = []
    for i, (label, ptitle) in enumerate(PARTS):
        if not groups[i]: continue
        cells = []
        for s in groups[i]:
            num = s['num']
            lite = ' lite' if i == 0 else ''
            numeral = num.upper() if num else 'A'
            time = f'<span class="wtime">{html.escape(s["time"])}</span>' if s['time'] else ''
            li = ''.join(f'<li><a href="{relhref(x["href"], "index.html")}">{html.escape(x["title"])}</a></li>' for x in s['lessons'])
            cells.append(f'<div class="wcell{lite}"><div class="wnum">{numeral}</div><div class="wbody">'
                         f'<div class="wrow"><h3>{html.escape(s["title"])}</h3>{time}</div>'
                         f'<ul class="lessons">{li}</ul></div></div>')
        head = (f'<span>{label}</span>{ptitle}') if label else ptitle
        parts.append(f'<section class="part"><h2 class="phead">{head}</h2><div class="pgrid">{"".join(cells)}</div></section>')
    body = ('<div class="brandrule"></div>'
            '<main class="iwrap" id="main">'
            '<div class="icover">'
            '<div><div class="eyebrow">University of Cape Town &middot; MAM5020F &middot; 2026</div>'
            '<h1>Generative AI for Research</h1>'
            '<div class="sub">A postgraduate course on how generative AI is changing research practice.</div></div>'
            '<div class="iintro"><p>From literature reviews to data analysis, writing to ethics. No prior programming, '
            'machine learning, or computer science background required.</p>'
            '<div class="links"><a href="glossary.html">Glossary &rarr;</a>'
            '<a href="papers/index.html">Papers to read &rarr;</a>'
            '<a href="about.html">About &rarr;</a></div></div>'
            '</div>' + ''.join(parts) + '</main>'
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
    leftnav = ('<div class="leftnav">' + NAV_TOG_L +
               '<a class="back" href="index.html">&larr; All lessons</a>'
               f'<div class="navwk">Reference</div><nav class="toc">{nav}</nav></div>')
    blocks = ''
    for L in letters:
        blocks += f'<h2 class="ga" id="L{L}">{html.escape(L)}</h2>'
        for t in groups[L]:
            slug = re.sub(r'[^a-z0-9]+', '-', t["term"].lower()).strip('-')
            blocks += (f'<div class="gentry" id="gt-{slug}"><div class="gt">{html.escape(t["term"])}</div>'
                       f'<div class="gd">{t["definition"]}</div></div>')
    rightrail = ('<div class="rightrail">' + TS_GROUP + f'<div class="rmeta">Glossary<br>{len(terms)} terms<br>MAM5020F</div></div>')
    main = (MARGIN_BODY + '<div class="ahead"><div class="eyebrow">MAM5020F &mdash; Generative AI for Research</div>'
            '<h1>Glossary</h1><div class="deck">Key terms used across the course, in plain language.</div></div>'
            f'<div class="abody gloss">{blocks}</div>')
    body = ('<div class="brandrule"></div><div class="shell">' + leftnav +
            '<main class="maincol" id="main">' + main + '</main>' + rightrail + '</div>')
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
