#!/usr/bin/env python3
"""
Generate Week 11 lesson HTML files (Future of AI in Research & Africa's Sovereign AI Capacity).

Outputs to both:
  Course materials/Week 11/                  (source / Amathuba upload copies)
  Course materials/docs/week-11/             (GitHub Pages serving copies)

Mirrors the Week 9 / Week 10 generators. CSS is pretty-printed (one property per line) and the
<style> block lives in <head> so Brightspace's TinyMCE source editor preserves it.

Re-run after any content change.
"""

import os
import re

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SRC_DIR = os.path.join(ROOT, "Week 11")
DOCS_DIR = os.path.join(ROOT, "docs", "week-11")


def pretty_print_css(css: str) -> str:
    """Convert single-line CSS rules to multi-line format (each property on its own line)."""
    out_lines = []
    for line in css.splitlines():
        m = re.match(r"^(\s*)(.+?)\s*\{\s*(.+?)\s*\}\s*$", line)
        if m and ";" in m.group(3):
            indent, selector, props = m.group(1), m.group(2), m.group(3)
            decls = [d.strip() for d in props.split(";") if d.strip()]
            out_lines.append(f"{indent}{selector} {{")
            for d in decls:
                out_lines.append(f"{indent}    {d};")
            out_lines.append(f"{indent}}}")
        else:
            out_lines.append(line)
    return "\n".join(out_lines)


CSS = """* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Lato', sans-serif; line-height: 1.6; color: #2c3e50; background: #f5f5f5; padding: 20px; }
.container { max-width: 1200px; margin: 0 auto; background: white; border-radius: 20px; box-shadow: 0 20px 60px rgba(0,0,0,0.3); overflow: hidden; }
.ai-notice { background: #e8f4f8; color: #003A70; padding: 15px 30px; text-align: center; font-size: 0.9em; border-bottom: 1px solid #d0e8f2; }
header { background: #003A70; color: white; padding: 50px 40px; text-align: center; }
.week-badge { display: inline-block; background: rgba(255,255,255,0.2); padding: 8px 20px; border-radius: 20px; font-size: 0.9em; margin-bottom: 15px; backdrop-filter: blur(10px); }
header h1 { font-size: 2.3em; margin-bottom: 15px; font-weight: 300; letter-spacing: 1px; }
header p { font-size: 1.1em; opacity: 0.95; max-width: 800px; margin: 10px auto 0; }
.content { padding: 50px 40px; }
.intro-text { background: #f9f9f9; padding: 35px; border-radius: 15px; border-left: 5px solid #003A70; margin-bottom: 40px; }
.intro-text h2 { color: #2a5298; font-size: 1.8em; margin-bottom: 15px; display: flex; align-items: center; gap: 10px; }
.intro-text p { font-size: 1.1em; color: #495057; line-height: 1.8; margin-bottom: 15px; }
.intro-text p:last-child { margin-bottom: 0; }
.section-title { font-size: 2em; color: #2a5298; margin: 50px 0 30px; padding-bottom: 15px; border-bottom: 3px solid #003A70; display: flex; align-items: center; gap: 15px; }
.card-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin: 30px 0; }
.card { background: white; border-radius: 15px; padding: 25px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); border-left: 5px solid #003A70; transition: all 0.3s ease; }
.card:hover { transform: translateY(-5px); box-shadow: 0 10px 25px rgba(0,0,0,0.15); }
.card h3 { color: #2a5298; font-size: 1.4em; margin-bottom: 15px; font-weight: 600; }
.card p { color: #555; line-height: 1.7; margin-bottom: 15px; }
.styled-list { list-style: none; margin-top: 15px; }
.styled-list li { padding: 8px 0 8px 25px; color: #555; position: relative; line-height: 1.6; }
.styled-list li::before { content: '\\25B8'; position: absolute; left: 0; color: #003A70; font-weight: bold; }
.highlight-box { background: #003A70; color: white; padding: 30px; border-radius: 15px; margin: 40px 0; }
.highlight-box h3 { font-size: 1.8em; margin-bottom: 15px; }
.highlight-box p { font-size: 1.05em; line-height: 1.8; opacity: 0.95; margin-bottom: 12px; }
.highlight-box p:last-child { margin-bottom: 0; }
.warning-box { background: #fff8e1; border-left: 5px solid #f9a825; padding: 20px 25px; border-radius: 12px; margin: 20px 0; }
.warning-box h4 { color: #e65100; font-size: 1.1em; margin-bottom: 10px; }
.warning-box p { color: #555; line-height: 1.7; }
.info-box { background: #f8f9fa; padding: 20px 25px; border-radius: 12px; margin: 20px 0; border-left: 4px solid #003A70; }
.info-box h4 { color: #2a5298; font-size: 1.2em; margin-bottom: 12px; display: flex; align-items: center; gap: 10px; }
.info-box p { color: #555; line-height: 1.7; margin-bottom: 8px; }
.info-box p:last-child { margin-bottom: 0; }
.technical-detail { background: white; border: 2px solid #d0e8f2; border-radius: 12px; padding: 25px; margin: 20px 0; }
.technical-detail h4 { color: #2a5298; font-size: 1.3em; margin-bottom: 15px; }
.case-study { background: linear-gradient(135deg, rgba(0,58,112,0.03) 0%, rgba(42,82,152,0.03) 100%); border: 2px solid #003A70; border-radius: 15px; padding: 25px; margin: 25px 0; }
.case-study h4 { color: #003A70; font-size: 1.3em; margin-bottom: 15px; }
.case-study p { color: #444; line-height: 1.75; margin-bottom: 12px; }
.case-study p:last-child { margin-bottom: 0; }
.comparison-table { width: 100%; border-collapse: collapse; margin: 20px 0; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
.comparison-table th { background: #003A70; color: white; padding: 15px; text-align: left; font-weight: 600; font-size: 0.95em; }
.comparison-table td { padding: 12px 15px; border-bottom: 1px solid #e9ecef; color: #555; font-size: 0.95em; line-height: 1.5; }
.comparison-table tr:last-child td { border-bottom: none; }
.comparison-table tr:hover { background: #f9f9f9; }
.step-list { counter-reset: step-counter; list-style: none; margin: 20px 0; }
.step-list > li { counter-increment: step-counter; padding: 15px 15px 15px 60px; position: relative; margin-bottom: 12px; background: #f9f9f9; border-radius: 10px; color: #444; line-height: 1.7; }
.step-list > li::before { content: counter(step-counter); position: absolute; left: 15px; top: 50%; transform: translateY(-50%); background: #003A70; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.9em; }
.resource-placeholder { background: linear-gradient(135deg, rgba(0,58,112,0.05) 0%, rgba(42,82,152,0.05) 100%); border: 2px dashed #003A70; border-radius: 15px; padding: 30px; margin: 25px 0; }
.resource-placeholder h4 { color: #2a5298; font-size: 1.3em; margin-bottom: 10px; }
.resource-placeholder p { color: #555; line-height: 1.7; margin-bottom: 8px; }
.resource-placeholder p:last-child { margin-bottom: 0; }
@media (max-width: 768px) { header h1 { font-size: 1.8em; } .content { padding: 30px 20px; } .card-grid { grid-template-columns: 1fr; } .comparison-table { font-size: 0.85em; } }
/* Force white text on dark-blue backgrounds (overrides Brightspace stylesheet defaults). */
header, header h1, header h2, header h3, header h4, header p, header span, header strong, header em, .week-badge,
.highlight-box, .highlight-box h1, .highlight-box h2, .highlight-box h3, .highlight-box h4, .highlight-box h5,
.highlight-box p, .highlight-box ul, .highlight-box ol, .highlight-box li,
.highlight-box strong, .highlight-box em, .highlight-box span {
    color: #ffffff !important;
}
.highlight-box a, header a { color: #ffffff !important; text-decoration: underline; }"""

PAGE_SHELL = """<!DOCTYPE html>
<html lang="en"><head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="https://s.brightspace.com/lib/fonts/0.6.1/fonts.css">
  <style>
{css}
  </style>
  <link rel="stylesheet" href="https://templates.lcs.brightspace.com/lib/assets/css/styles.min.css">
</head><body>
<div style="background: #003A70; padding: 8px 20px; text-align: center;"><a href="../index.html" style="color: white; text-decoration: none; font-size: 0.85em;">&#8592; Back to Contents</a></div>
<div class="container">

<div class="ai-notice"><strong>Note:</strong> This page&#39;s design, presentation and content have been created and enhanced using Claude (Anthropic&#39;s AI assistant) to improve visual quality and educational experience.</div>

<header>
  <div class="week-badge">{badge}</div>
  <h1>{header_emoji} <span style="color: #ffffff;">{header_title}</span></h1>
  <p>{header_subtitle}</p>
</header>

<div class="content">
{body}
</div>
</div>
<footer style="background: #f9f9f9; padding: 22px 30px; text-align: center; color: #888; font-size: 0.85em; border-top: 1px solid #eee; font-family: 'Lato', 'Lucida Sans Unicode', 'Lucida Grande', sans-serif;">
&copy; 2026 Jonathan Shock &middot; MAM5020F: Generative AI for Research &middot; Licensed under <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener" style="color: #003A70; text-decoration: underline;">CC&nbsp;BY&nbsp;4.0</a>
</footer>
</body></html>
"""


# ---------------------------------------------------------------------------
# Sub-Lesson 11.1 — What the Future of AI in Research Actually Looks Like
# ---------------------------------------------------------------------------

SL1_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>Most public commentary about &ldquo;the future of AI in research&rdquo; is a mixture of three very different claims: things that are demonstrably happening; things that are technically real but loudly oversold; and things that are not happening at all but are presented as imminent. The most useful thing a postgraduate researcher can take away from a futures discussion is not a list of predictions but a habit: <strong>before you accept a claim about what AI is doing for science, ask which of those three buckets it falls into.</strong></p>
    <p>This sub-lesson does that exercise on the most prominent recent claims from the period running up to May 2026. We will look in turn at the genuinely shipping work (AlphaFold-family structure prediction; autonomous materials discovery; biomedical hypothesis systems with wet-lab validation), at one carefully-bounded case study of how a real result gets repackaged into an overclaimed one (the Sakana AI Scientist <em>Nature</em> paper), and at the things that are genuinely not happening yet despite confident pronouncements (end-to-end autonomous science, recursive self-improving research systems, AI as the primary author of high-impact papers).</p>
    <p>The point is not to predict five years out &mdash; nobody can &mdash; but to give you the disposition you need to read AI-research news for the rest of your career without being captured by either hype or anti-hype. Sub-Lesson 11.2 then turns to a connected question: what the institutions around you (journals, funders, peer-review) have done in response to all this, and whether their responses are working.</p>
  </div>

  <h2 class="section-title">&#129518; A Working Framework: Real / Overclaimed / Aspirational</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">We have been using a version of this three-bucket frame throughout Weeks 9 and 10. Week 9.3 distinguished what AI is now genuinely strong at from what it merely performs convincingly. Week 10.3 separated agentic capabilities that ship from those that exist mainly in vendor demos. The frame is the same here. The three buckets are not graded by quality &mdash; an aspirational claim is not necessarily a dishonest one &mdash; but by their relationship to evidence.</p>

  <div class="card-grid">
    <div class="card">
      <h3>&#9989; Real</h3>
      <p>A capability that is documented in peer-reviewed literature or independently replicated, with the scope of the claim carefully bounded by the people who made it. Almost always narrower than the headline.</p>
      <p style="color: #888; font-size: 0.95em;">Test: would a working researcher in the field describe the result the same way the press does? If yes, it is real.</p>
    </div>
    <div class="card">
      <h3>&#9888;&#65039; Overclaimed</h3>
      <p>A real underlying result that has been rounded up. The paper exists, the experiment worked &mdash; but the framing, the headline, or the press release strips away the caveats that the authors themselves wrote into the discussion section.</p>
      <p style="color: #888; font-size: 0.95em;">Test: does the abstract say something importantly more careful than the press release? If yes, the press release is overclaimed.</p>
    </div>
    <div class="card">
      <h3>&#128640; Aspirational</h3>
      <p>A claim about the future presented as if it were the present. Often grounded in real trend lines but extrapolated past where the evidence ends. Includes timelines for AGI, &ldquo;by 2027&rdquo; predictions, and the recurring claim that AI scientists will replace PhDs.</p>
      <p style="color: #888; font-size: 0.95em;">Test: is the claim supported by anything other than a graph of past trends and a confident sentence? If not, treat as aspirational.</p>
    </div>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The rest of this sub-lesson is a worked example of the frame in action. We will take three concrete cases &mdash; one in each bucket &mdash; and trace each one from its primary source to its public reception.</p>

  <h2 class="section-title">&#9989; Real: What Is Actually Shipping in Research-AI</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Four lines of work, all peer-reviewed, all with humans verifying outputs in a laboratory, give the clearest picture of what AI is currently contributing to active scientific research. None of them is &ldquo;an AI doing science&rdquo;; all of them are <em>AI as a serious collaborator in narrow, well-defined parts of the scientific process</em>.</p>

  <div class="card-grid">
    <div class="card">
      <h3>Protein structure prediction</h3>
      <p>The AlphaFold lineage is the cleanest example of an AI capability that is now infrastructure. AlphaFold 3 (Abramson et al., <em>Nature</em>, May 2024) extended the protein-only prediction of AlphaFold 2 to complexes including nucleic acids, small molecules and ions; code and weights were opened to academic users in November 2024. Structural biologists no longer treat predicted structures as exotic.</p>
      <p style="color: #888; font-size: 0.95em;">Real-bucket marker: a working scientist in the field uses it without thinking about it.</p>
    </div>
    <div class="card">
      <h3>Autonomous materials synthesis</h3>
      <p>The GNoME / A-Lab work (Merchant et al., Szymanski et al., <em>Nature</em> 2023) generated 2.2 million candidate crystal structures, filtered them to 381,000 predicted to be stable, and then ran an autonomous laboratory at Lawrence Berkeley that synthesised dozens of novel materials with minimal human intervention. The synthesis success rate (about 71%) is the genuine number; the &ldquo;381,000 stable materials&rdquo; figure is a prediction.</p>
      <p style="color: #888; font-size: 0.95em;">Real-bucket marker: a closed loop from AI prediction to physical experiment, peer-reviewed.</p>
    </div>
    <div class="card">
      <h3>Biomedical hypothesis-and-validation</h3>
      <p>DeepMind&#39;s AI Co-Scientist (Gottweis et al., <em>Nature</em>, May 2026) is the most carefully validated recent example. It paired computational hypothesis generation with three wet-lab biomedical validations carried out by named academic collaborators. We treat this case in detail below.</p>
      <p style="color: #888; font-size: 0.95em;">Real-bucket marker: AI-generated hypotheses tested in physical experiments by humans, with the negatives reported alongside the positives.</p>
    </div>
    <div class="card">
      <h3>End-to-end candidate-to-lab pipelines</h3>
      <p>FutureHouse&#39;s <em>Robin</em> (arXiv:2505.13400, May 2025) identified ripasudil as a candidate for dry age-related macular degeneration and ran phagocytosis assays showing a 7.5&times; increase <em>in vitro</em>. FutureHouse spun out Edison Scientific in November 2025; its successor system <em>Kosmos</em> reportedly processes 1,500 papers plus tens of thousands of lines of analysis code per run.</p>
      <p style="color: #888; font-size: 0.95em;">Real-bucket marker: published preprint with replicable wet-lab numbers, not just a chat transcript.</p>
    </div>
  </div>

  <div class="technical-detail">
    <h4>&#129516; A worked example: DeepMind&#39;s AI Co-Scientist, primary-source version</h4>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">The peer-reviewed <em>Nature</em> paper (Gottweis et al., DOI 10.1038/s41586-026-10644-y) describes a multi-agent system built on Gemini, evaluated against OpenAI o1, o3-mini-high, DeepSeek R1, and Gemini 2.0 Pro Experimental on 203 research goals. On an 11-goal expert-evaluated subset, Co-Scientist outputs received a mean preference rank of 2.36 and ratings of 3.64/5 for novelty and 3.09/5 for impact. So far, so benchmark.</p>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">The interesting part is the three wet-lab biomedical validations published alongside:</p>
    <ul class="styled-list" style="margin-top: 0;">
      <li><strong>Drug repurposing for acute myeloid leukaemia.</strong> Binimetinib (already approved for melanoma) showed a half-maximal inhibitory concentration as low as 2&nbsp;nM in AML cell lines, against around 180&nbsp;nM in a non-AML control. The genuinely novel candidate KIRA6, an IRE1&alpha; inhibitor for which no prior preclinical AML evidence existed, showed an 18-fold selectivity window between leukaemic and control cells.</li>
      <li><strong>Liver fibrosis epigenetic targets.</strong> Two of three Co-Scientist-predicted compounds, including the already-FDA-approved drug Vorinostat, showed significant anti-fibrotic activity in human hepatic organoids with no observed cellular toxicity (published as Guan et al., <em>Advanced Science</em>, 2025).</li>
      <li><strong>A bacterial-evolution mechanism.</strong> Co-Scientist proposed, in two days and with only minimal background information, that capsid-forming phage-inducible chromosomal islands interact with diverse phage tails to expand bacterial host range &mdash; matching the primary discovery of an independent, co-timed experimental study from the Pen&aacute;d&eacute;s group at the Fleming Initiative / Imperial College London (Pen&aacute;d&eacute;s et al., <em>Cell</em> 188(23), 6654&ndash;6665, 2025) before peer review of either was complete.</li>
    </ul>
    <p style="color: #444; line-height: 1.75; margin-top: 12px;">Note what made this work: AI-generated hypotheses, prioritised by oncologists and microbiologists, validated in physical experiments by named human collaborators, with the failures (drugs that didn&#39;t work, hypotheses that were rejected) reported alongside the successes.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The Co-Scientist paper&#39;s own limitations section is worth reading as a model of the calibrated voice this sub-lesson is asking you to adopt. The authors explicitly flag that the system&#39;s knowledge is constrained by open-access literature, that there is a systemic lack of access to negative experimental results, and that the validation reported is preliminary. The closing warning &mdash; that improper use of such systems without rigorous peer review and guardrails could worsen the scientific reproducibility crisis through low-quality scientific artefacts &mdash; is from the authors themselves, in <em>Nature</em>. That is how a major lab paper is supposed to sound. Most press coverage of the same work does not sound like that.</p>

  <div class="info-box">
    <h4>&#128270; What &ldquo;real&rdquo; looks like up close</h4>
    <p>If you take only one habit from this section, take this one: when a paper makes a striking AI-in-science claim, read the <em>limitations</em> section before reading the abstract. Authors usually mark the boundary of their own claim honestly. Press coverage strips that boundary out. The gap between what the discussion section says and what the headline says is one of the most useful signals you have for separating real from overclaimed.</p>
  </div>

  <h2 class="section-title">&#9888;&#65039; Overclaimed: A Detailed Case Study</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Now we take a single, recent, high-profile result &mdash; the Sakana AI &ldquo;AI Scientist&rdquo; paper in <em>Nature</em> in March 2026 &mdash; and trace what it actually says, what the public coverage said it said, and what the gap between those two looks like. This is a worked exercise, not a takedown. The underlying paper is interesting and the authors are careful. The point is that even careful, peer-reviewed work gets routinely rounded up in transit.</p>

  <div class="case-study">
    <h4>&#128209; What the Sakana paper actually claims</h4>
    <p>Lu, C., Lu, C., Lange, R. T., Yamada, Y. et al. (2026). <em>Towards end-to-end automation of AI research.</em> <em>Nature</em> 651, 914&ndash;919, DOI 10.1038/s41586-026-10265-5. CC&nbsp;BY 4.0 open access. Note the actual title: not &ldquo;<em>The AI Scientist: Towards Fully Automated AI Research</em>&rdquo; (the lab blog framing) but the more modest <em>Towards end-to-end automation of AI research</em>.</p>
    <p>The headline result, as written in the paper itself, is this: <strong>one of three</strong> AI-generated manuscripts that the team submitted to the <em>ICLR 2025 ICBINB workshop</em> received average reviewer scores of 6.33 on the ICLR 1&ndash;10 scale (individual scores 6, 7, 6) and was ranked in the top 45% of submissions. The workshop&#39;s acceptance rate was <strong>70%</strong>. The acceptance rate of the main ICLR 2025 conference was 32%. The paper that &ldquo;passed&rdquo; reported a negative result, aligned with the workshop&#39;s focus on interesting negative findings.</p>
    <p>Crucially: <strong>all three submissions were withdrawn per the pre-arranged ethics protocol</strong> with the workshop organisers and the University of British Columbia&#39;s Research Ethics Board. Nothing was actually published. The team also conducted their own internal review and concluded, in their own words, that one of the papers met the bar for workshop publication but <em>none</em> met the higher bar for a main ICLR conference paper.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">That is the real claim, and it is a perfectly interesting one. A fully AI-generated machine-learning paper now reaches the lower bar of a top-venue workshop with measurable consistency. The team&#39;s separate &ldquo;Automated Reviewer&rdquo; (an LLM judging machine-learning papers) shows balanced accuracy of 66&ndash;69% against historical accept/reject decisions, comparable to or modestly above human inter-reviewer consistency. The paper also documents a real correlation (R&sup2; = 0.517, P &lt; 0.00001) between underlying model release date and generated-paper quality &mdash; sometimes loosely called a &ldquo;scaling law of science&rdquo;, though it is a correlation across a handful of models, not a physics-style law.</p>

  <div class="warning-box">
    <h4>&#128221; Where the rounding happens</h4>
    <p>Compare what the paper says with three things you will see in coverage of it:</p>
    <ul class="styled-list" style="margin-top: 8px;">
      <li>&ldquo;<em>An AI wrote a paper that passed peer review.</em>&rdquo; True only at workshop level (70% acceptance), at a venue specifically designed for negative results, and the paper was withdrawn.</li>
      <li>&ldquo;<em>The first fully AI-generated paper to pass a rigorous human peer-review process.</em>&rdquo; Strips out &ldquo;workshop&rdquo;, strips out &ldquo;one of three&rdquo;, and strips out &ldquo;withdrawn per protocol&rdquo;.</li>
      <li>&ldquo;<em>AI Scientists are here.</em>&rdquo; The paper&#39;s own limitations section states that the system &ldquo;cannot yet meet the standards of top-tier publications nor even do so consistently for workshops.&rdquo; Common failure modes named by the authors include hallucinated citations, naive ideas, and lack of methodological rigour.</li>
    </ul>
    <p style="margin-top: 12px;">There is also an independent critical evaluation (arXiv:2502.14297, &ldquo;Bold Claims, Mixed Results&rdquo;) of the system, which is worth reading as a counterweight before forming your own opinion.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The discipline this case is meant to teach is not cynicism. It is the habit of pulling a primary source and reading its own discussion section before forming an opinion about what it means. The Sakana team behaved very honestly: they obtained ethics approval, they pre-committed to withdraw any accepted paper, they reported one acceptance and two rejections out of three submissions, and they wrote a careful limitations section. The rounding happened later, in transit, in summaries written by people who had not read the paper. As a postgraduate researcher in 2026, that &ldquo;in transit&rdquo; layer is where most of the AI-in-research claims you will encounter will live. Read past it.</p>

  <h2 class="section-title">&#128640; Aspirational: What Is Not Happening Yet</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The aspirational bucket is the one most worth being explicit about, because confident claims about the near future are usually presented as if they were claims about the present. Three of the most prominent are worth naming and bounding.</p>

  <div class="card-grid">
    <div class="card">
      <h3>End-to-end autonomous science</h3>
      <p>The picture in which an AI system formulates an original research question, designs experiments to answer it, runs them, interprets results, writes the paper, and submits it &mdash; with no human in the loop &mdash; is not happening, and is not on a credible near-term trajectory. Every system we have looked at above &mdash; Co-Scientist, Robin, GNoME/A-Lab, the AI Scientist &mdash; was steered by named human collaborators at every critical step. The Co-Scientist paper&#39;s own framing is &ldquo;scientist-in-the-loop&rdquo;.</p>
      <p style="color: #888; font-size: 0.95em;">Aspirational marker: every demonstration of &ldquo;autonomy&rdquo; turns out, on inspection, to have humans selecting research goals, prioritising hypotheses, and verifying outputs.</p>
    </div>
    <div class="card">
      <h3>Recursive self-improvement</h3>
      <p>The idea that an AI research system substantially improves <em>itself</em> &mdash; designing better versions of its own architecture, then using those better versions to design better-still versions &mdash; remains a hypothetical capability. Real systems improve when humans deploy better models, write better harnesses, or curate better training data (the Week 10.1 lesson that the harness is the product). A coding agent helping its developers ship faster (as Claude Code reportedly does at Anthropic) is real and useful; it is not the same thing as recursive self-improvement of capability.</p>
      <p style="color: #888; font-size: 0.95em;">Aspirational marker: claims rely on extrapolating compute curves, not on any system that has demonstrably bootstrapped itself.</p>
    </div>
    <div class="card">
      <h3>AI as primary author of high-impact papers</h3>
      <p>The journals you would want to publish in (<em>Nature</em>, <em>Science</em>, the medical journals, the African Journal of Marine Science) do not permit AI to be listed as an author, and have ethics policies under the International Committee of Medical Journal Editors and the Committee on Publication Ethics that make AI authorship a misconduct matter (we look at these in 11.2). Even the Sakana paper&#39;s headline AI-generated workshop manuscript was withdrawn rather than published. The notion of AI as first author is not a near-term operational reality.</p>
      <p style="color: #888; font-size: 0.95em;">Aspirational marker: the institutional rules have, if anything, moved in the opposite direction.</p>
    </div>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Listing the aspirational claims is not the same as dismissing them. Some of them may turn out to be true on a five-or-ten-year horizon. The point is the same as in Weeks 9 and 10: when you read a confident sentence about what AI &ldquo;will&rdquo; do for science, the useful question is not whether it is plausible but whether you would be willing to plan a research project on the assumption. If not, it belongs in the aspirational bucket, and you should make decisions about your own work as if the present, not the projected future, is what you have to work with.</p>

  <h2 class="section-title">&#127757; What This Means for Your Research Trajectory</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">If you are starting a research project in 2026, you are scoping work that you will be defending at a viva in 2027 or 2028, and publishing from for some years after. The 2&ndash;5 year horizon for AI in research matters because it is the horizon you are actually living in. Three honest implications follow from the picture above.</p>

  <ul class="styled-list">
    <li><strong>AI as a collaborator in narrow tasks is here.</strong> Literature search (Week 5), code (Week 7), document and image analysis (Week 8), agentic multi-step assistance (Week 10) are real and worth integrating into your workflow. The decision is not <em>whether</em> to use them but <em>where</em> the verification has to happen, and you make that decision per task, not per tool.</li>
    <li><strong>AI as the author of your project is not here, and the rules are tightening against it.</strong> If you are tempted to outsource the framing, the analysis or the writing of your work to AI in a way that you would not declare openly, the institutional direction of travel is against you. The next sub-lesson (11.2) shows how funders, journals, and peer-review systems have moved on this in the last 18 months. The norms are real, they are evolving, and they will apply to your work.</li>
    <li><strong>The questions worth scoping around are about leverage, not capability.</strong> &ldquo;Can I use AI to do this?&rdquo; is now usually a yes. The more useful question is: <em>where in my research is my own context, data, language, or relationships giving me a distinctive angle that an AI scaling up generic literature does not have?</em> For the African-led second half of this week, that question has a particular sharp answer.</li>
  </ul>

  <div class="highlight-box">
    <h3>&#128161; <span style="color: #ffffff;">The disposition this sub-lesson is asking for</span></h3>
    <p>You do not need a confident prediction about whether AI will replace researchers in 2030. You need a habit: when you read a claim about what AI is doing for science, ask which bucket it belongs in &mdash; real, overclaimed, or aspirational &mdash; and pull the primary source if you cannot tell.</p>
    <p>If you carry only that into the rest of your research career, you will read AI-research news the way an experienced scientist reads any other field&#39;s news: looking for the limitations section, suspicious of press releases, willing to be impressed by carefully bounded results, and not willing to be hurried by aspirational ones.</p>
  </div>

  <h2 class="section-title">&#9999;&#65039; A Short Exercise</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 15px; line-height: 1.8;">Before the in-class session, do this exercise. It should take 30&ndash;45 minutes.</p>

  <ol class="step-list">
    <li><strong>Pick one of the four real-bucket cases above</strong> (AlphaFold 3, GNoME/A-Lab, AI Co-Scientist, or Robin/Kosmos) <strong>or one from your own field</strong> if you know it better.</li>
    <li><strong>Find the primary source.</strong> Not a press release, not a blog post, not a news article &mdash; the peer-reviewed paper or the verified preprint. Look at the abstract, the limitations section, and the figure captions.</li>
    <li><strong>Write two short paragraphs.</strong> In the first, describe what the paper <em>actually</em> claims, in terms a careful reader of your discipline would accept. In the second, describe what the AI specifically contributed and what humans still did. Be precise about the boundary.</li>
    <li><strong>Find one piece of public coverage</strong> of the same work (newspaper, vendor blog, X/Twitter thread, anywhere). Note one specific thing it says that goes beyond what the paper itself supports. This is your &ldquo;in transit&rdquo; rounding.</li>
    <li><strong>Bring all three to class.</strong> We will pool them across the cohort.</li>
  </ol>

  <h2 class="section-title">&#128218; Sources &amp; Further Reading</h2>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Primary sources used in this sub-lesson:</p>

  <div class="resource-placeholder">
    <h4>&#128196; The peer-reviewed papers</h4>
    <p><strong>DeepMind AI Co-Scientist</strong> &mdash; Gottweis, J. et al. (2026). <em>Accelerating scientific discovery with Co-Scientist.</em> <em>Nature</em>. <a href="https://doi.org/10.1038/s41586-026-10644-y" target="_blank" rel="noopener">DOI 10.1038/s41586-026-10644-y</a>. Accepted 11 May 2026; published online 19 May 2026.</p>
    <p><strong>Liver fibrosis follow-up</strong> &mdash; Guan, Y. et al. (2025). <em>AI-assisted drug re-purposing for human liver fibrosis.</em> <em>Advanced Science</em>, e08751.</p>
    <p><strong>cf-PICI mechanism</strong> &mdash; Pen&aacute;d&eacute;s, J. R. et al. (2025). <em>AI mirrors experimental science to uncover a novel mechanism of gene transfer crucial to bacterial evolution.</em> <em>Cell</em> 188(23), 6654&ndash;6665.</p>
    <p><strong>Sakana AI Scientist</strong> &mdash; Lu, C., Lu, C., Lange, R. T., Yamada, Y. et al. (2026). <em>Towards end-to-end automation of AI research.</em> <em>Nature</em> 651, 914&ndash;919. <a href="https://doi.org/10.1038/s41586-026-10265-5" target="_blank" rel="noopener">DOI 10.1038/s41586-026-10265-5</a>. CC&nbsp;BY 4.0.</p>
    <p><strong>Independent Sakana critique</strong> &mdash; &ldquo;Bold Claims, Mixed Results&rdquo;, <a href="https://arxiv.org/abs/2502.14297" target="_blank" rel="noopener">arXiv:2502.14297</a> (February 2025).</p>
    <p><strong>AlphaFold 3</strong> &mdash; Abramson, J. et al. (2024). <em>Accurate structure prediction of biomolecular interactions with AlphaFold 3.</em> <em>Nature</em> 630, 493&ndash;500. <a href="https://doi.org/10.1038/s41586-024-07487-w" target="_blank" rel="noopener">DOI 10.1038/s41586-024-07487-w</a>.</p>
    <p><strong>GNoME &amp; A-Lab</strong> &mdash; Merchant, A. et al. (2023). <em>Scaling deep learning for materials discovery.</em> <em>Nature</em> 624, 80&ndash;85. Szymanski, N. J. et al. (2023). <em>An autonomous laboratory for the accelerated synthesis of novel materials.</em> <em>Nature</em> 624, 86&ndash;91.</p>
    <p><strong>FutureHouse Robin</strong> &mdash; <a href="https://arxiv.org/abs/2505.13400" target="_blank" rel="noopener">arXiv:2505.13400</a> (May 2025); see also FutureHouse&#39;s research announcement at <a href="https://www.futurehouse.org/research-announcements/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system" target="_blank" rel="noopener">futurehouse.org</a>.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 20px; margin-bottom: 15px;"><strong>Coming up in 11.2:</strong> a reading guide for the genuinely <em>speculative</em> end of the AI-in-research literature &mdash; frameworks (Krenn, Wang, Morris), falsifiable forecasts (METR), institutional visioning (Royal Society, Africa Declaration), and wild speculation (Clune, <em>AI 2027</em>, Russell) &mdash; with the same calibration habit applied throughout. 11.3 then turns from speculation to the institutional present: what journals and funders have actually <em>done</em> in response to AI in research, and the surprising gap between policy and practice.</p>
"""


# ---------------------------------------------------------------------------
# Supplementary — Speculative Futures: A Reading Guide
# ---------------------------------------------------------------------------

SL_SUPP_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>Sub-Lesson 11.1 deliberately stayed inside the next 2&ndash;5 years and inside well-documented results. This sub-lesson takes the same calibrated reading habit and applies it to the genuinely <em>speculative</em> end of the AI-in-research literature &mdash; the work that asks not &ldquo;what does AI do for science now?&rdquo; but &ldquo;what could AI do for science, eventually, and what would that change?&rdquo;</p>
    <p>The calibration habit from 11.1 still applies here &mdash; only more strongly. Confident sentences about 2030 are rarely better-grounded than confident sentences about 2026. Several of the works in this guide are serious academic frameworks; a couple are essentially structured science fiction with a confident tone. The lesson is organised so you can tell them apart.</p>
    <p>The goal is not to make you a forecaster. It is to give you a working reading guide for the question &ldquo;what kind of researcher do I want to be in a world where this stuff keeps moving?&rdquo; &mdash; which is the question that quietly underlies everything else in this week.</p>
  </div>

  <h2 class="section-title">&#129516; A. Frameworks for Thinking About AI in Science</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">If you only read one piece of speculative-futures work, make it one of these three. They are the conceptual scaffolding most subsequent debates are arguing inside.</p>

  <div class="card-grid">
    <div class="card">
      <h3>The three dimensions of AI in understanding (Krenn et al., 2022)</h3>
      <p>Krenn and colleagues, writing in <em>Nature Reviews Physics</em>, set out a three-part framework for how AI can contribute to scientific understanding: as a <strong>computational microscope</strong> (observing things humans cannot), as a <strong>resource of inspiration</strong> (a muse for hypotheses), and as an <strong>agent of understanding</strong> &mdash; an AI that itself <em>understands</em> what it has found.</p>
      <p>The paper itself classifies the third dimension as &ldquo;the ultimate, not yet existent&rdquo; capability. Read it for the calibrated framing as much as for the framework: this is what a serious speculative paper sounds like.</p>
      <p style="color: #888; font-size: 0.9em;">Krenn, M. et al. (2022). On scientific understanding with artificial intelligence. <em>Nature Reviews Physics</em> 4, 761&ndash;769. arXiv:2204.01467.</p>
    </div>
    <div class="card">
      <h3>The AI-in-discovery landscape (Wang et al., 2023)</h3>
      <p>Wang and colleagues, in <em>Nature</em>, map AI&#39;s emerging role across every stage of the scientific process: hypothesis generation, experiment design, data collection, analysis, interpretation. The paper is a landscape, not a manifesto &mdash; useful for orienting yourself before reading any of the more polemical speculative work.</p>
      <p>Notable for being honest that &ldquo;AI in science&rdquo; is not one thing: protein structure prediction, materials discovery, automated chemistry, and LLM-assisted writing all sit at different levels of maturity and need to be evaluated separately.</p>
      <p style="color: #888; font-size: 0.9em;">Wang, H., Fu, T., Du, Y. et al. (2023). Scientific discovery in the age of artificial intelligence. <em>Nature</em> 620, 47&ndash;60. DOI 10.1038/s41586-023-06221-2.</p>
    </div>
    <div class="card">
      <h3>Levels of AGI (Morris et al., 2023)</h3>
      <p>A DeepMind team led by Meredith Ringel Morris &mdash; with Shane Legg among the authors &mdash; proposes a six-level framework for AGI capability, indexed jointly by performance (depth) and generality (breadth), explicitly analogous to the SAE levels of autonomous driving. The framework deliberately avoids putting a date on any level.</p>
      <p>Useful precisely because it refuses to commit to a timeline. When you read confident claims about &ldquo;AGI by 2027&rdquo;, this paper is what such claims are pretending to be.</p>
      <p style="color: #888; font-size: 0.9em;">Morris, M. R. et al. (2023). Levels of AGI: Operationalizing Progress on the Path to AGI. arXiv:2311.02462.</p>
    </div>
  </div>

  <h2 class="section-title">&#128202; B. Concrete, Falsifiable Forecasts</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">A useful filter for speculative work: does the author commit to a number, on a defined timescale, that someone could check? Most speculative writing about AI does not. The few works that do are worth reading carefully, because they are the parts of the discourse that can actually be wrong in the ordinary scientific sense.</p>

  <div class="technical-detail">
    <h4>&#9201;&#65039; The METR &ldquo;doubling-every-seven-months&rdquo; study</h4>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">In March 2025, the AI-evaluation lab METR published a paper introducing a deceptively simple metric: the <em>50% time horizon</em>, defined as the length of a software task an AI system can complete with at least 50% success. Over the six years from 2019 to 2025, the 50% horizon has doubled approximately every seven months.</p>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">The endpoints of the curve in the March 2025 paper are striking: from GPT-2 in 2019 (a 50% horizon of seconds) up to Claude 3.7 Sonnet in early 2025 (approximately one hour). METR maintains an updated &ldquo;Time Horizon 1.1&rdquo; dataset with newer models and a larger task suite, but the specific later-2025 figures circulating in secondary coverage (including ones I had originally cited here for o3 and Opus 4.6) need to be checked directly against METR&#39;s own tracker, not against synthesised news summaries.</p>
    <p style="color: #444; line-height: 1.75; margin-top: 12px;">Extrapolated naively, the curve says that within a decade AI systems will be able to autonomously complete the kind of software work that today takes a person days or weeks. The honest caveat the METR team itself flags is that exponential curves bend &mdash; nothing in nature stays exponential forever &mdash; and they are deliberately not predicting <em>when</em> the bend will happen.</p>
    <p style="color: #444; line-height: 1.75;">Why read it: this is the cleanest example of a falsifiable forecast in the speculative-futures literature. By 2028 we will know whether the 7-month doubling held; that is more than can be said for most predictions in this area. <em>METR (March 2025). Measuring AI Ability to Complete Long Software Tasks. arXiv:2503.14499.</em></p>
  </div>

  <div class="warning-box">
    <h4>&#9888;&#65039; What an extrapolation can&#39;t tell you</h4>
    <p>A doubling time is not the same thing as a model of <em>why</em> the doubling happens. The METR paper documents the curve; it does not explain it. The curve could continue. It could also bend tomorrow if, say, the reliability ceiling on long-horizon agents (Week 10.2) turns out to be the real bottleneck. Treat extrapolation curves the way you would treat any time-series forecast in your own field: useful as a starting estimate, dangerous as a basis for confident predictions about specific dates.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Adjacent to METR is the body of work from <strong>Epoch AI</strong> &mdash; an organisation focused on training-compute scaling, dataset-size trends, and the economics of frontier model training. Their forecasts share METR&#39;s strength (quantitative and refutable) and weakness (extrapolation without a mechanism). Worth reading if you want the technical version of &ldquo;how big might AI training get?&rdquo;</p>

  <h2 class="section-title">&#127960;&#65039; C. Institutional Visioning</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">This category contains some of the most quietly important speculative-futures work, because it is what the bodies that <em>set rules</em> &mdash; learned societies, national academies, intergovernmental panels &mdash; think research is going to look like. These documents move slowly and read carefully, but they are the speculative pieces that translate most directly into actual policy.</p>

  <div class="technical-detail">
    <h4>&#128218; <em>Science in the age of AI</em> (Royal Society, October 2024)</h4>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">The Royal Society&#39;s 2024 working-group report (ISBN 978-1-78252-712-1) draws on interviews with more than 100 scientists across disciplines plus a working group of experts. It frames AI as transforming the nature, method, and integrity of scientific research, and is unusually careful in its scepticism: a central recommendation is that overdependence on &ldquo;opaque&rdquo; AI systems could undermine the reliability of scientific findings and the public&#39;s trust in them.</p>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">Read it for its tone. This is what speculative-futures discourse sounds like when written by a body that takes responsibility for science as an institution rather than as a market.</p>
    <p style="color: #444; line-height: 1.75;"><a href="https://royalsociety.org/news-resources/projects/science-in-the-age-of-ai/" target="_blank" rel="noopener">royalsociety.org/.../science-in-the-age-of-ai</a></p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">In a similar register is the <strong>Africa Declaration on AI</strong> (April 2025), signed at the conclusion of the Global AI Summit on Africa by almost every AU member state. Its institutional speculation is the proposal for an <strong>African AI Scientific Panel</strong> &mdash; a regional body of researchers from Africa and the diaspora to provide evidence-based research on AI risks and opportunities. Whether the panel materialises in the form proposed will be a useful early test of how much of the continental-strategy rhetoric (covered in 11.5) translates into operational reality.</p>

  <h2 class="section-title">&#128640; D. Wild Speculation</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">This bucket contains the most ambitious and least-grounded work in the field. The works listed below range from serious academic research that is openly speculative to documents that are essentially structured science fiction with a confident tone. They are listed not because we endorse them but because they are influential enough that you will encounter them, and being able to read them critically is part of the disposition this week is asking you to build.</p>

  <div class="card-grid">
    <div class="card">
      <h3>Open-endedness and AI-Generating Algorithms (Clune, 2019)</h3>
      <p>Jeff Clune &mdash; one of the co-authors of the Sakana <em>AI Scientist</em> paper covered in 11.1 &mdash; proposes that the most plausible route to general-purpose AI is to build systems that <em>invent</em> better AI systems, in an open-ended evolutionary process. The 2019 paper (arXiv:1905.10985) is the foundational reference for the lineage of automated-science work, of which the Sakana AI Scientist is a recent product.</p>
      <p>This is serious academic research that is honest about its speculative character. Useful to read for the intellectual history alone.</p>
      <p style="color: #888; font-size: 0.9em;">Clune, J. (2019). AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence. arXiv:1905.10985.</p>
    </div>
    <div class="card">
      <h3><em>AI 2027</em> scenario (Kokotajlo et al., April 2025)</h3>
      <p>A 71-page month-by-month scenario, written by Daniel Kokotajlo&#39;s AI Futures Project, of how the period 2025&ndash;2027 might play out in capabilities and geopolitics. The scenario predicts &ldquo;superhuman coders&rdquo; by March 2027 and &ldquo;superhuman AI researchers&rdquo; by June 2027.</p>
      <p>Two honest notes. The authors themselves estimate roughly 50% probability that the superhuman-coder milestone is missed on the 2027 timeline, and Kokotajlo&#39;s own median forecast has since shifted to &ldquo;around 2030, lots of uncertainty though&rdquo;. Critics describe parts of the scenario as closer to science fiction than forecasting. Worth reading as the cleanest specimen of confident-tone speculation in the field &mdash; the kind of document the reading habit from 11.1 is most useful against.</p>
      <p style="color: #888; font-size: 0.9em;">AI Futures Project, <em>AI 2027</em>, April 2025.</p>
    </div>
    <div class="card">
      <h3><em>Human Compatible</em> and the alignment literature (Russell, 2019)</h3>
      <p>Stuart Russell&#39;s book lays out the speculative-but-serious case that controlling capable AI systems &mdash; getting them to do what humans actually want, rather than what we literally asked &mdash; is a research problem in its own right. The book has become foundational reading for the AI safety / alignment literature, which now has its own academic conferences and a growing presence in policy discussions.</p>
      <p>Worth reading because the alignment conversation is one of the few places where speculative AI futures translate directly into institutional and regulatory action.</p>
      <p style="color: #888; font-size: 0.9em;">Russell, S. (2019). <em>Human Compatible: Artificial Intelligence and the Problem of Control</em>. Viking.</p>
    </div>
    <div class="card">
      <h3>The frontier-vendor speculation lane</h3>
      <p>Senior figures at the major AI labs publish their own speculative-futures pieces with some regularity: Sam Altman&#39;s essays, Dario Amodei&#39;s &ldquo;Machines of Loving Grace&rdquo; (October 2024), Demis Hassabis&#39;s interviews. These are not academic work; they are speculative essays by people with strong commercial interests in particular futures coming true. They are also genuinely influential on policy and public understanding.</p>
      <p>Read them as primary sources for &ldquo;what frontier labs publicly believe (or wish to be seen believing) about the future&rdquo;, not as predictions.</p>
      <p style="color: #888; font-size: 0.9em;">Various vendor essays, 2024&ndash;2026.</p>
    </div>
  </div>

  <h2 class="section-title">&#127757; A Note on the African Gap</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The serious speculative-futures literature is, by and large, written from a small number of institutions in the Global North. Of the works in this guide, none are authored from an African research institution; the institutional visioning that comes closest is the Africa Declaration on AI, which is a political document rather than a research one.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">This is itself a research opportunity. The closest existing African work in this register sits in the literature we covered in Weeks 4 and 11.5:</p>

  <ul class="styled-list">
    <li><strong>Mhlambi (2020), <em>From Rationality to Relationality</em></strong> &mdash; argues for ubuntu as a foundation for AI ethics, with implications for what a non-Western AI research culture would look like.</li>
    <li><strong>Effoduh (2026), &ldquo;Decolonizing the governance of artificial intelligence in Africa&rdquo;</strong> (<em>Science and Public Policy</em> 53(2), 245&ndash;257) &mdash; develops the concept of <em>epistemic sovereignty</em> as a speculative-normative goal for African AI work.</li>
    <li><strong>Nyabola (2026), &ldquo;Foundations for African feminism as an ethics for artificial intelligence&rdquo;</strong> (<em>Science and Public Policy</em> 53(2), 277&ndash;288) &mdash; makes the case that a genuinely African AI research tradition would need to start from different onto-epistemological commitments, not just import Northern AI tools and add an &ldquo;African values&rdquo; layer on top.</li>
  </ul>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">If you find the speculative-futures conversation interesting, one of the most useful contributions you could make as an African postgraduate researcher is to add to this side of the literature. The frame the Effoduh and Nyabola papers develop is genuinely under-applied to questions about AI <em>research</em> as opposed to AI <em>governance</em>, and there is room for serious work that explores what an African vision of AI in science would look like, beyond importing the Northern speculative literature wholesale.</p>

  <div class="highlight-box">
    <h3>&#128161; <span style="color: #ffffff;">The reading habit, restated for speculative work</span></h3>
    <p>When you read a speculative-futures piece &mdash; in this guide or elsewhere &mdash; the questions worth asking are not so different from the ones 11.1 set out. <em>Is there a number the author commits to that someone could check?</em> Is the speculation grounded in a mechanism or in a graph of past trends? Does the author take responsibility for being wrong, or do they reserve the right to retrofit their predictions?</p>
    <p>If a piece of futures work would not change anything its author does if it turned out to be wrong, it is closer to fiction than forecasting. That is not a reason to ignore it &mdash; serious fiction can be useful &mdash; but it is a reason to read it differently from a piece of work the author would defend on the same terms as their other research.</p>
  </div>

  <h2 class="section-title">&#9999;&#65039; An Optional Exercise</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 15px; line-height: 1.8;">If you want to put the calibration habit through its paces:</p>

  <ol class="step-list">
    <li><strong>Pick one work from buckets A, B, C, or D above</strong> that you have not previously read.</li>
    <li><strong>Read it,</strong> with particular attention to where in the text the author signals the limits of their own claim. (Look for words like &ldquo;might&rdquo;, &ldquo;could&rdquo;, &ldquo;under the assumption that&rdquo;, and for hedged probability language.)</li>
    <li><strong>Locate one specific claim in the work that you could imagine checking in 2030</strong> &mdash; a date, a number, a milestone, a behaviour. Write it down in a sentence.</li>
    <li><strong>Write a second sentence describing what evidence would persuade you the claim was wrong.</strong></li>
  </ol>

  <p style="color: #555; line-height: 1.75; margin-top: 20px; margin-bottom: 15px;">That second sentence &mdash; what would change your mind &mdash; is the centre of the calibrated reading habit. A speculative work that gives you no way to check it later is a work you should hold loosely. One that does is a work you can engage with on the same terms as any other piece of research.</p>

  <h2 class="section-title">&#128218; Full Reference List</h2>

  <div class="resource-placeholder">
    <h4>&#128196; Primary sources used in this guide</h4>
    <p><strong>Krenn, M. et al. (2022).</strong> On scientific understanding with artificial intelligence. <em>Nature Reviews Physics</em> 4, 761&ndash;769. <a href="https://arxiv.org/abs/2204.01467" target="_blank" rel="noopener">arXiv:2204.01467</a> &middot; <a href="https://www.nature.com/articles/s42254-022-00518-3" target="_blank" rel="noopener">Nature page</a>.</p>
    <p><strong>Wang, H. et al. (2023).</strong> Scientific discovery in the age of artificial intelligence. <em>Nature</em> 620, 47&ndash;60. <a href="https://www.nature.com/articles/s41586-023-06221-2" target="_blank" rel="noopener">DOI 10.1038/s41586-023-06221-2</a>.</p>
    <p><strong>Morris, M. R. et al. (2023).</strong> Levels of AGI: Operationalizing Progress on the Path to AGI. <a href="https://arxiv.org/abs/2311.02462" target="_blank" rel="noopener">arXiv:2311.02462</a>.</p>
    <p><strong>METR (March 2025).</strong> Measuring AI Ability to Complete Long Software Tasks. <a href="https://arxiv.org/abs/2503.14499" target="_blank" rel="noopener">arXiv:2503.14499</a>. Blog post: <a href="https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/" target="_blank" rel="noopener">metr.org</a>.</p>
    <p><strong>Royal Society (October 2024).</strong> <em>Science in the age of AI</em>. ISBN 978-1-78252-712-1. <a href="https://royalsociety.org/news-resources/projects/science-in-the-age-of-ai/" target="_blank" rel="noopener">Project page</a>.</p>
    <p><strong>Africa Declaration on AI (April 2025).</strong> Adopted at the Global AI Summit on Africa. (Covered in detail in 11.5.)</p>
    <p><strong>Clune, J. (2019).</strong> AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence. <a href="https://arxiv.org/abs/1905.10985" target="_blank" rel="noopener">arXiv:1905.10985</a>.</p>
    <p><strong>Kokotajlo, D. et al. (April 2025).</strong> <em>AI 2027</em> scenario. AI Futures Project. (Available via the project&#39;s website; treat as the prominent specimen of structured speculative-futures scenario planning, not as forecast.)</p>
    <p><strong>Russell, S. (2019).</strong> <em>Human Compatible: Artificial Intelligence and the Problem of Control</em>. Viking.</p>
    <p><strong>Effoduh, J. O. (2026).</strong> Decolonizing the governance of artificial intelligence in Africa. <em>Science and Public Policy</em> 53(2), 245&ndash;257. <a href="https://academic.oup.com/spp/article/53/2/245/8654721" target="_blank" rel="noopener">DOI 10.1093/scipol/scag005</a>.</p>
    <p><strong>Nyabola, N. (2026).</strong> Foundations for African feminism as an ethics for artificial intelligence. <em>Science and Public Policy</em> 53(2), 277&ndash;288. <a href="https://academic.oup.com/spp/article/53/2/277/8654723" target="_blank" rel="noopener">DOI 10.1093/scipol/scag009</a>.</p>
    <p><strong>Mhlambi, S. (2020).</strong> <em>From Rationality to Relationality: Ubuntu as an Ethical and Human Rights Framework for Artificial Intelligence Governance</em>. Carr Center for Human Rights Policy, Harvard Kennedy School.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 20px; margin-bottom: 15px;"><strong>Coming up in 11.3:</strong> we turn from speculative futures to the institutional present &mdash; what journals, funders, and peer-review systems have actually <em>done</em> in response to AI in research over the last 18 months, and one large recent study showing that, despite ~70% of journals now having AI-disclosure policies, only about 0.1% of post-2023 papers actually disclose AI use. The gap between policy and practice is the central feature of the landscape we will look at next.</p>
"""


# ---------------------------------------------------------------------------
# SUBLESSONS list — grows as sub-lessons are drafted
# ---------------------------------------------------------------------------

SUBLESSONS = [
    {
        "filename": "What the Future of AI in Research Might Look Like.html",
        "title": "Week 11.1 - What the Future of AI in Research Might Look Like",
        "badge": "Week 11 &bull; Sub-Lesson 1",
        "header_emoji": "&#128302;",  # crystal ball
        "header_title": "What the Future of AI in Research Might Look Like",
        "header_subtitle": "A calibrated reading of what is shipping, what is overclaimed, and what is purely aspirational &mdash; with three worked cases",
        "body": SL1_BODY,
    },
    {
        "filename": "Speculative Futures - A Reading Guide.html",
        "title": "Week 11.2 - Speculative Futures: A Reading Guide",
        "badge": "Week 11 &bull; Sub-Lesson 2",
        "header_emoji": "&#128302;",  # crystal ball
        "header_title": "Speculative Futures: A Reading Guide",
        "header_subtitle": "Reading further into the genuinely speculative end of the AI-in-research literature &mdash; frameworks, forecasts, institutional visioning, and wild speculation, with calibration",
        "body": SL_SUPP_BODY,
    },
]


# Table of Contents (just 11.1 for now; will grow as sub-lessons are added)
TOC_HTML = """<html><head><meta http-equiv="'Content-Type'" content="'text/html;charset=utf-8'" /><title>MAM5020F 2026 | Gen AI for Research - Week 11: Future of AI in Research &amp; Africa's Sovereign AI Capacity</title></head><body>
<div style="background: #003A70; padding: 8px 20px; text-align: center;"><a href="../index.html" style="color: white; text-decoration: none; font-size: 0.85em;">&#8592; Back to Contents</a></div><table cellpadding=0 cellspacing=0 border=0 width=100%><tr><td colspan=3>&nbsp;</td></tr><tr><td valign="top" width="100%"><font class="title"><strong>MAM5020F 2026 | Gen AI for Research - Week 11: Future of AI in Research &amp; Africa&#39;s Sovereign AI Capacity</strong></font><br><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="What the Future of AI in Research Might Look Like.html" />1. What the Future of AI in Research Might Look Like</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Speculative Futures - A Reading Guide.html" />2. Speculative Futures &mdash; A Reading Guide</a></p><p class='d2l' style=' margin-left: 40px; color: #888;'><em>3. The Shifting Research Landscape (to be drafted)</em></p><p class='d2l' style=' margin-left: 40px; color: #888;'><em>4. Sovereign AI Capacity, and Why Compute Is the Floor (to be drafted)</em></p><p class='d2l' style=' margin-left: 40px; color: #888;'><em>5. Data, Languages and African Model-Building (to be drafted)</em></p><p class='d2l' style=' margin-left: 40px; color: #888;'><em>6. Policy, Institutions and Talent (to be drafted)</em></p><p class='d2l' style=' margin-left: 40px; color: #888;'><em>7. Where This Leaves Your Research + Hands-On Activity (to be drafted)</em></p></td></tr></table><footer style="background: #f9f9f9; margin-top: 40px; padding: 22px 30px; text-align: center; color: #888; font-size: 0.85em; border-top: 1px solid #eee; font-family: 'Lato', 'Lucida Sans Unicode', 'Lucida Grande', sans-serif;">
&copy; 2026 Jonathan Shock &middot; MAM5020F: Generative AI for Research &middot; Licensed under <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener" style="color: #003A70; text-decoration: underline;">CC&nbsp;BY&nbsp;4.0</a>
</footer></body></html>"""


def render_sublesson(sl):
    return PAGE_SHELL.format(
        title=sl["title"],
        css=pretty_print_css(CSS),
        badge=sl["badge"],
        header_emoji=sl["header_emoji"],
        header_title=sl["header_title"],
        header_subtitle=sl["header_subtitle"],
        body=sl["body"],
    )


def write_to(directory, name, content):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  wrote {path}")


def main():
    print("Generating Week 11...")
    print("Table of Contents:")
    write_to(SRC_DIR, "Table of Contents.html", TOC_HTML)
    write_to(DOCS_DIR, "Table of Contents.html", TOC_HTML)
    for sl in SUBLESSONS:
        print(f"{sl['title']}:")
        rendered = render_sublesson(sl)
        write_to(SRC_DIR, sl["filename"], rendered)
        write_to(DOCS_DIR, sl["filename"], rendered)
    print(f"\nDone. {len(SUBLESSONS)} sub-lesson(s) + ToC written to each of:")
    print(f"  {SRC_DIR}")
    print(f"  {DOCS_DIR}")


if __name__ == "__main__":
    main()
