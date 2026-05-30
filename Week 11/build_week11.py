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
    <p>The point is not to predict five years out &mdash; nobody can &mdash; but to give you the disposition you need to read AI-research news for the rest of your career without being captured by either hype or anti-hype. Sub-Lesson 11.2 extends the same exercise into the genuinely <em>speculative</em> end of the literature; 11.3 then turns to a connected question: what the institutions around you (journals, funders, peer-review) have done in response to all this, and whether their responses are working.</p>
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
# Sub-Lesson 11.3 — The Shifting Research Landscape
# ---------------------------------------------------------------------------

SL3_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>In the eighteen months between January 2024 and mid-2026, the institutions that govern academic research &mdash; journals, learned societies, public funders, conference organisers &mdash; have pushed out more new rules about AI use than in any comparable period in their history. By August 2025, around <strong>83% of high-impact journals</strong> had a policy on AI use in peer review (up from 77% in March); around <strong>70% of journals across all impact tiers</strong> had a policy on AI use by authors. The institutional response, by any standard, has been fast.</p>
    <p>And yet, in the same period, the practice gap has stayed almost flat. Of more than 75,000 papers published since 2023 that a recent <em>PNAS</em> study examined in full text, only <strong>about 0.1% explicitly disclosed AI use</strong>. Journals with and without AI policies show statistically indistinguishable growth in detectable AI-written content. The rules have moved; researcher behaviour has not.</p>
    <p>This sub-lesson maps the new institutional landscape in the form a postgraduate researcher actually has to navigate it. We look in turn at the policies that bind <em>authors</em>, those that bind <em>reviewers</em>, those that bind <em>grant applicants</em> &mdash; with a particular note on where the South African NRF sits, which is &ldquo;nowhere yet&rdquo; &mdash; and then at the detection-and-integrity layer that has emerged in parallel. We close with a short exercise that connects the two halves of the picture: by the time you submit your first paper, you should already know what each of the institutions you are submitting to will require of you.</p>
  </div>

  <h2 class="section-title">&#127963;&#65039; The Eighteen-Month Policy Surge</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The clearest empirical picture of how journal policies have evolved comes from a March 2026 study by Wang and Gong (<em>Learned Publishing</em>) which examined the AI policies of 439 high-impact-factor journals and 363 middle-impact-factor journals across 21 disciplines, collected at two time points five months apart. The headline finding is that 24.5% of high-impact journals revised their AI peer-review policies in those five months alone; the rate of policy change is roughly an order of magnitude faster than the rate of change in other publication-ethics areas.</p>

  <div class="technical-detail">
    <h4>&#128214; Five typical policy types, tied to major publishers</h4>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">Wang and Gong identify five distinct policy templates that account for the bulk of high-impact-journal AI rules. They differ in <em>what</em> they permit, but agree on one principle.</p>
    <ul class="styled-list" style="margin-top: 0;">
      <li><strong>OUP (Oxford University Press) &mdash;</strong> defers to the broader publication-ethics consensus (COPE guidelines) and does not yet have a journal-specific generative-AI policy. Authors are expected to disclose; the editorial stance on use is permissive.</li>
      <li><strong>Elsevier &mdash;</strong> the most prohibitive of the five. Bans generative AI from all stages of peer review and editorial decision-making; bans uploading manuscripts to AI platforms.</li>
      <li><strong>Springer Nature &mdash;</strong> emphasises confidentiality. Does not ban AI use outright, but prohibits uploading manuscript content (including figures and tables) to generative-AI services, on the grounds that such uploads breach the confidentiality of peer review.</li>
      <li><strong>Wiley &mdash;</strong> structurally similar to Springer Nature: limited use permitted; no manuscript upload to AI platforms.</li>
      <li><strong>ACM (Association for Computing Machinery) &mdash;</strong> the most permissive of the five. Editors and reviewers may use generative AI to support their work, provided confidential information (author identities, manuscript content) is first removed.</li>
    </ul>
    <p style="color: #444; line-height: 1.75; margin-top: 12px;"><strong>The one principle all five share:</strong> AI cannot replace human judgement on a manuscript&#39;s scientific innovation or professional standing. That is the consensus the entire field has settled on, however it is operationalised.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">There is also a clear disciplinary stratification, visible in the same study. Materials science, chemistry, and agricultural science journals are the strictest: more than half of high-impact journals in those fields explicitly prohibit AI use in peer review. Arts &amp; humanities, computer science, and mathematics journals are the most permissive &mdash; partly because the publication culture in those fields was already more comfortable with computational tools, partly because the empirical risks (fabricated experimental data, fabricated chemical structures) are less acute than in the lab sciences. If you are a postgraduate working in a less-tightly-policed field, the lesson is not that the rules do not apply &mdash; the broader publishing consensus still does &mdash; but that you should expect the formal policy to lag where the actual practice already is.</p>

  <div class="info-box">
    <h4>&#128221; The international authorship consensus, in one paragraph</h4>
    <p>Across the journal-policy landscape, three things are universal as of mid-2026: <em>AI cannot be listed as an author</em>, on the grounds that authorship implies responsibility and AI cannot take responsibility; <em>AI use that materially shaped the paper must be disclosed</em>, typically in the Methods and/or Acknowledgements; and <em>the human authors remain accountable for everything in the manuscript</em>, including any text or figures the AI produced. This is the position of the International Committee of Medical Journal Editors, of the Committee on Publication Ethics, of Nature, of Science, and of essentially every major learned society. If you remember nothing else from this sub-lesson, remember the three rules.</p>
  </div>

  <h2 class="section-title">&#128270; Reviewers: Where the Rules Are Most Prohibitive</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The reviewer side of the picture is the one where the institutions have moved most firmly. The reason is that reviewer use of AI raises a structural problem the author side does not: a reviewer uploading a confidential manuscript to a public AI service has breached the confidentiality of peer review, regardless of how good the resulting review is.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The clearest examples are the major public funders and the top conferences. The picture, as of mid-2026, is roughly as follows:</p>

  <div class="card-grid">
    <div class="card">
      <h3>NIH (United States)</h3>
      <p>Notice NOT-OD-23-149, issued 23 June 2023 and still in force, prohibits reviewers of NIH grant proposals from using generative AI to analyse or critique applications. The stated rationale is confidentiality. NIH followed up in 2025 with an applicant-side policy too (see below).</p>
      <p style="color: #888; font-size: 0.9em;"><a href="https://grants.nih.gov/grants/guide/notice-files/NOT-OD-23-149.html" target="_blank" rel="noopener">grants.nih.gov</a></p>
    </div>
    <div class="card">
      <h3>NSF (United States)</h3>
      <p>NSF&#39;s policy notice of 14 December 2023 prohibits reviewers from uploading proposal content to non-approved AI tools, on the same confidentiality grounds. The proposer-side stance is more permissive: AI use is permitted but transparency is encouraged.</p>
      <p style="color: #888; font-size: 0.9em;"><a href="https://new.nsf.gov/news/notice-to-the-research-community-on-ai" target="_blank" rel="noopener">nsf.gov</a></p>
    </div>
    <div class="card">
      <h3>UKRI (United Kingdom)</h3>
      <p>UKRI&#39;s policy on generative AI in application and assessment, published 20 September 2024 and updated 3 December 2024, requires applicant transparency and prohibits reviewers from using generative AI to assess proposals.</p>
      <p style="color: #888; font-size: 0.9em;"><a href="https://www.ukri.org/publications/generative-artificial-intelligence-in-application-and-assessment-policy/" target="_blank" rel="noopener">ukri.org</a></p>
    </div>
    <div class="card">
      <h3>NeurIPS (Conference)</h3>
      <p>The NeurIPS 2025 LLM policy is the cleanest top-conference statement. Authors must document any non-trivial use of LLMs in their submission; reviewers must not share submitted papers or code with any LLM, hosted or otherwise. The reviewer-side ban is absolute.</p>
      <p style="color: #888; font-size: 0.9em;"><a href="https://neurips.cc/Conferences/2025/LLM" target="_blank" rel="noopener">neurips.cc</a></p>
    </div>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">A less-noticed pattern in Wang and Gong&#39;s data is worth flagging here, because it bears on whether the rules are actually being implemented. The proportion of high-impact journals with AI policies <em>specifically for editors</em> &mdash; the people inside the publishing system, as distinct from the external reviewers &mdash; rose from <strong>41% in March 2025 to 64.3% in August 2025</strong>. In other words, a 23-percentage-point jump in five months in the segment of policy that addresses what the publishing infrastructure itself is allowed to do. This is the bit of the institutional response that has been moving fastest, and the bit that gets the least public coverage.</p>

  <div class="warning-box">
    <h4>&#9888;&#65039; What the rules do not change</h4>
    <p>Liang et al. (arXiv:2410.03019, 2024) ran a content analysis of recent peer-review reports and estimated that approximately <strong>20% of reviews at a top computer-science conference</strong> and approximately <strong>12% of reviews at <em>Nature Communications</em></strong> exhibited textual signatures consistent with significant LLM contribution. The reviewer-side ban is on the books at most major venues; a measurable fraction of reviews are nonetheless being written with AI help. As with the author-side picture, the policy is not the practice.</p>
  </div>

  <h2 class="section-title">&#128190; Grant Applicants: What&#39;s Required, and the South African Gap</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Funder rules for what applicants can do with AI in proposal writing have lagged the reviewer-side rules by about a year, but have caught up sharply during 2025. The major Northern funders now all have an applicant-side policy of some kind.</p>

  <ul class="styled-list">
    <li><strong>NIH (United States), applicant side &mdash;</strong> from the receipt date of 25 September 2025, applications &ldquo;substantially developed by AI&rdquo; will not be considered to constitute original ideas of the applicant. NIH also imposed a cap of six applications per principal investigator per year, in part to slow the AI-enabled production of large numbers of low-effort applications.</li>
    <li><strong>UKRI &mdash;</strong> applicants are required to be transparent about generative-AI use in their proposals; the responsibility for accuracy and integrity remains with the applicant.</li>
    <li><strong>NSF &mdash;</strong> applicant-side disclosure is &ldquo;encouraged&rdquo;, but not yet required in the same binding way as the reviewer-side prohibition.</li>
    <li><strong>Wellcome Trust, ERC, and most European funders &mdash;</strong> have adopted positions broadly similar to UKRI: transparency required, no outright prohibition, accountability sits with the applicant.</li>
  </ul>

  <div class="case-study">
    <h4>&#127489;&#127462; The NRF (South Africa) gap</h4>
    <p>The South African National Research Foundation, the principal public funder for the research most postgraduate students in this course will eventually apply to, has <strong>no policy</strong> on generative AI use in grant applications as of May 2026. The NRF General Application Guide for 2025&ndash;2026, the binding document that sets the rules every applicant must comply with, does not mention generative AI, ChatGPT, or large language models anywhere in its text. The NRF does not prohibit AI use in applications, nor does it require disclosure, nor does it offer guidance.</p>
    <p>This is a fact, not a judgement. Many national funders in the Global South are in the same position. But it has two practical implications for you. <em>First,</em> if you are applying to the NRF directly, you are operating in a policy vacuum. There are no formal rules. <em>Second &mdash; and more important &mdash; the international norms still apply to you.</em> If you publish work supported by an NRF grant in an Elsevier or Wiley or Nature journal, the journal&#39;s AI policy binds you. If you collaborate with a NIH-funded research group on a paper, NIH&#39;s rules will apply to the proposal you submit jointly. The NRF gap is a gap in domestic policy, not in the international rules that will actually govern most of your published work.</p>
    <p>If you want to do something useful for the local research community before you finish your PhD, drafting an NRF AI-disclosure policy proposal &mdash; even a one-page version &mdash; is the kind of contribution that would be genuinely valuable.</p>
    <p style="color: #888; font-size: 0.9em;"><a href="https://www.nrf.ac.za/wp-content/uploads/2025/02/General-Application-Guide-2025-2026.pdf" target="_blank" rel="noopener">NRF General Application Guide 2025&ndash;2026 (PDF)</a></p>
  </div>

  <h2 class="section-title">&#128202; Policy &ne; Practice: The He &amp; Bu Centre</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The single most important recent study on whether any of this institutional response is actually changing researcher behaviour is He and Bu (2026), <em>Academic Journals&#39; AI Policies Fail to Curb the Surge in AI-Assisted Academic Writing</em> &mdash; published in <em>PNAS</em> in March 2026 (DOI 10.1073/pnas.2526734123). It is the largest study of its kind to date, and the answer it gives is bracing.</p>

  <div class="technical-detail">
    <h4>&#128202; The He &amp; Bu numbers</h4>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">The study examines <strong>5,114 journals</strong> in the Journal Citation Report Q1 category and <strong>5,235,012 papers</strong> they published between January 2021 and June 2025. Journal AI policies are collected at two time points (January 2025 and October 2025). The disclosure analysis uses a sub-sample of 164,579 full-text papers, of which 75,172 were published after January 2023 (the post-ChatGPT period).</p>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">The headline findings:</p>
    <ul class="styled-list" style="margin-top: 0;">
      <li><strong>~70% of journals have AI policies.</strong> Of the 5,114 journals, 3,556 require disclosure, 1,529 do not mention AI at all, 27 strictly prohibit AI use, and 2 have explicitly open policies. Between January and October 2025, roughly 800 more journals moved into the &ldquo;disclosure required&rdquo; category.</li>
      <li><strong>~0.1% of papers actually disclose.</strong> Of the 75,172 post-2023 full-text papers, only <strong>76 papers</strong> explicitly disclosed AI use in the methods or acknowledgements. The disclosure rate rose from 0.01% in early 2023 to 0.43% in Q1 2025 &mdash; growth, but from a vanishing base.</li>
      <li><strong>Q1 2025 underreporting ratio: ~40:1.</strong> For every paper that formally disclosed AI use, roughly 40 papers showed statistical evidence of AI-generated content (measured by maximum-likelihood estimation on text patterns, cross-validated by three other detection methods).</li>
      <li><strong>The decisive finding: parallel growth curves.</strong> AI-content levels grow at <em>statistically the same rate</em> in journals that have AI policies and in journals that do not (Mann-Whitney U tests; no significant difference). The presence of a policy is not slowing the adoption of AI writing.</li>
    </ul>
    <p style="color: #444; line-height: 1.75; margin-top: 12px;">The pattern is uneven across groups: physical sciences grow fastest, non-English-speaking countries (with China most prominent) grow faster than English-speaking ones, and high-open-access publishers (MDPI, Frontiers) show higher AI-content levels than low-OA ones (Elsevier, Springer Nature, Wiley). On the disclosed tools: <em>ChatGPT</em> dominates the 76 disclosures (62 instances), with Grammarly, Claude, and DeepL trailing.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The He &amp; Bu finding is not that policies are pointless. The authors are explicit that the modest rise in disclosures, even from 0.01% to 0.43%, suggests policies are slowly shifting a small subset of researchers toward transparency. What policies are <em>not</em> doing &mdash; clearly &mdash; is curbing the underlying use. The gap between policy and practice, in their data, is roughly an order of magnitude wider than the policy-revision activity has been able to close.</p>

  <div class="info-box">
    <h4>&#128221; A meta-touch worth noting</h4>
    <p>He &amp; Bu themselves explicitly declare their own AI use in the methods section: they used ChatGPT-4o-mini and Gemini 2.5 Flash via API for large-scale data processing and Claude (the conversational interface) for qualitative auditing and logic checks. The paper that catalogues how few researchers disclose AI use models good practice itself. It is the easiest pedagogical example you will find in this literature of what the disclosure norm looks like in actual operation.</p>
  </div>

  <h2 class="section-title">&#128270; The Detection-and-Integrity Layer</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">In parallel with the policy surge, a small industry of AI-content detection tools and academic-integrity research has grown up to try to enforce, or at least measure, what the policies require. The most useful thing to know about this layer is that <em>detection does not work reliably enough to be the front line of integrity</em>. The institutional rules will continue to depend, in the end, on disclosure by authors and on the social norms in research communities. Detection plays a supporting role; it is not a substitute.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Three concrete results give the shape of the current picture.</p>

  <div class="card-grid">
    <div class="card">
      <h3>Tortured-phrase detection (Cabanac et al.)</h3>
      <p>The <em>Problematic Paper Screener</em> (Cabanac, Labb&eacute;, Magazinov) maintains a database of more than 5,000 &ldquo;tortured phrases&rdquo; &mdash; oddly translated or rephrased technical terms (e.g. &ldquo;haze figuring&rdquo; for &ldquo;cloud computing&rdquo;) that are characteristic of paper-mill output and machine-paraphrased writing.</p>
      <p>Useful: catches a specific kind of fraud cheaply. Limited: addresses paper-mill style, not careful GenAI use.</p>
      <p style="color: #888; font-size: 0.9em;"><a href="https://arxiv.org/abs/2402.03370" target="_blank" rel="noopener">arXiv:2402.03370</a></p>
    </div>
    <div class="card">
      <h3>JBJS estimate (Callanan et al., 2025)</h3>
      <p>An analysis of a single orthopaedic journal estimated that approximately <strong>38% of papers</strong> recently published in the <em>Journal of Bone &amp; Joint Surgery</em> may contain AI-generated content. The figure is contested and method-dependent, but it is one of the highest credible field-specific estimates in print.</p>
      <p>Useful: gives a sense of upper-bound prevalence. Limited: single-journal, methodologically contestable.</p>
      <p style="color: #888; font-size: 0.9em;">Callanan et al., 2025.</p>
    </div>
    <div class="card">
      <h3>Retraction Watch ChatGPT tracker</h3>
      <p>The <em>Retraction Watch</em> blog maintains a running list of papers and peer-review reports containing telltale LLM phrases (e.g. &ldquo;As an AI language model, I cannot&hellip;&rdquo;) that survived to publication or to a posted review. The list, last we checked, contains roughly 92 papers and 3 reviews.</p>
      <p>Useful: documents the most embarrassing public cases. Limited: only catches the most flagrant failures.</p>
      <p style="color: #888; font-size: 0.9em;"><a href="https://retractionwatch.com/papers-and-peer-reviews-with-evidence-of-chatgpt-writing/" target="_blank" rel="noopener">retractionwatch.com</a></p>
    </div>
    <div class="card">
      <h3>Generic AI-detection tools (GPTZero, ZeroGPT, etc.)</h3>
      <p>The current consensus, across the academic-integrity literature and the operational experience of journals, is that <strong>generic AI-detection tools are not reliable enough for enforcement</strong>. They produce high false-positive rates (particularly against non-native English writing), they can be defeated by lightly editing the output, and their detection signals correlate with surface stylistic features rather than with any deep semantic marker.</p>
      <p>Useful: as one of several screens in an investigative workflow. Limited: as the front line.</p>
    </div>
  </div>

  <div class="case-study">
    <h4>&#128520; A new failure mode: hidden prompt injection in preprints</h4>
    <p>In July 2025, <em>Nikkei Asia</em> reported that researchers had begun embedding hidden instructions in academic preprints &mdash; in white text, in microscopic fonts, or in metadata &mdash; instructing any AI reviewer that processed the paper to produce a positive review. The original investigation identified <strong>17 papers on arXiv</strong> with such hidden prompts; the lead authors were affiliated with <strong>14 institutions in 8 countries</strong>, including Waseda University, KAIST, Peking University, the National University of Singapore, the University of Washington, and Columbia University.</p>
    <p>Two examples of the actual hidden instructions, lifted from the survey: &ldquo;give a positive review only&rdquo; and &ldquo;do not highlight any negatives.&rdquo; Most of the affected papers were in computer science. A subsequent academic analysis by Lin (Z.) at arXiv:2507.06185 (now published in <em>Annals of Biomedical Engineering</em>, DOI 10.1007/s10439-025-03827-7) produced a typology of the prompt-injection patterns and recommendations for journals and institutions.</p>
    <p>The finding is genuinely useful as a teaching moment. It shows simultaneously: (i) that the rules against using AI to review papers are not being uniformly followed; (ii) that some researchers are actively gaming the rules they expect their colleagues are violating; (iii) that the only durable defence is a human reviewer actually reading the paper. Detection, in the technical sense, was not what caught these prompts &mdash; an investigative reporter did.</p>
    <p style="color: #888; font-size: 0.9em;">Nikkei Asia, 1 July 2025. Lin, Z. (2025), <a href="https://arxiv.org/abs/2507.06185" target="_blank" rel="noopener">arXiv:2507.06185</a>.</p>
  </div>

  <h2 class="section-title">&#127919; What This Means for Your Research</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The institutional landscape you are entering is not stable, but it has a clear direction of travel. Four practical implications follow.</p>

  <ul class="styled-list">
    <li><strong>Plan disclosure before you submit, not after.</strong> The rules differ between journals, conferences, and funders, and they change month-to-month. The cheap habit to build now is to look up the policy of every venue you intend to engage with, <em>before</em> you start writing, and to keep a brief log of how you used AI as you go. This is much easier to do prospectively than retrospectively.</li>
    <li><strong>Do not rely on detection to keep you honest.</strong> The detection layer is genuinely imperfect, and you will not be caught by it for the kind of GenAI use that the journal might reasonably expect to be declared. The question to ask yourself is not &ldquo;could I get away without disclosing this?&rdquo; but &ldquo;if my disclosure were published alongside the paper, would I be comfortable defending it?&rdquo; That second question is the one the international consensus actually asks of you.</li>
    <li><strong>For South African postgraduates: the NRF gap does not exempt you.</strong> If you publish in international journals, work with internationally funded collaborators, or submit your work for international evaluation, the international rules apply to you regardless of what the NRF does or does not require. Build a transparent practice now.</li>
    <li><strong>Take the He &amp; Bu finding seriously.</strong> The fact that the median researcher in their dataset does not disclose AI use is not a licence to do the same. It is the strongest evidence we have that the policy environment will continue to tighten until practice catches up. The researchers who will be best positioned in five years are those whose practice was already at the standard the policies eventually enforce.</li>
  </ul>

  <div class="highlight-box">
    <h3>&#128161; <span style="color: #ffffff;">The one habit to build</span></h3>
    <p>Pick your most likely target journal in your discipline. Pick your most likely target funder. Find each one&#39;s current AI policy. Read it once. Decide, in writing, what your default disclosure practice will be when you submit. Revisit annually.</p>
    <p>That single 20-minute exercise puts you ahead of about 99% of researchers globally, on the He &amp; Bu numbers.</p>
  </div>

  <h2 class="section-title">&#9999;&#65039; A Short Exercise</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 15px; line-height: 1.8;">For the in-class session:</p>

  <ol class="step-list">
    <li><strong>Pick the journal you would most realistically submit your first research paper to,</strong> based on your field and stage. Find its current AI policy. Write a paragraph: what does it require? What does it leave unaddressed?</li>
    <li><strong>Pick the funder you would most realistically apply to</strong> in the next three years &mdash; NRF, NIH, Wellcome, a foundation, an industry partner. Find its current policy on AI in applications. Write a paragraph: what does it require? What does it leave unaddressed?</li>
    <li><strong>Write one further paragraph</strong> describing, in concrete terms, how you intend to handle AI use in your own work as a result. Are there things you will not delegate? Things you will always disclose? Things you will log? This becomes one input to the Week-12 capstone pitch.</li>
    <li><strong>Bring all three paragraphs to class.</strong> We will pool them and look at the disciplinary patterns across the cohort.</li>
  </ol>

  <h2 class="section-title">&#128218; Sources &amp; Further Reading</h2>

  <div class="resource-placeholder">
    <h4>&#128196; Primary sources used in this sub-lesson</h4>
    <p><strong>He, Y. &amp; Bu, Y. (2026).</strong> Academic journals&#39; AI policies fail to curb the surge in AI-assisted academic writing. <em>PNAS</em>. <a href="https://www.pnas.org/doi/10.1073/pnas.2526734123" target="_blank" rel="noopener">DOI 10.1073/pnas.2526734123</a>. Preprint at <a href="https://arxiv.org/abs/2512.06705" target="_blank" rel="noopener">arXiv:2512.06705</a>.</p>
    <p><strong>Wang, Z. &amp; Gong, M. (2026).</strong> A Cross-Disciplinary Analysis of AI Policies in Academic Peer Review. <em>Learned Publishing</em> 39:e2035. <a href="https://doi.org/10.1002/leap.2035" target="_blank" rel="noopener">DOI 10.1002/leap.2035</a>. CC&nbsp;BY-NC.</p>
    <p><strong>Liang, W. et al. (2024).</strong> Mapping the Increasing Use of LLMs in Scientific Papers. <a href="https://arxiv.org/abs/2410.03019" target="_blank" rel="noopener">arXiv:2410.03019</a>.</p>
    <p><strong>Lin, Z. (2025).</strong> Hidden Prompts in Manuscripts Threaten the Integrity of Peer Review and Research. <a href="https://arxiv.org/abs/2507.06185" target="_blank" rel="noopener">arXiv:2507.06185</a>. Published version in <em>Annals of Biomedical Engineering</em>, <a href="https://doi.org/10.1007/s10439-025-03827-7" target="_blank" rel="noopener">DOI 10.1007/s10439-025-03827-7</a>.</p>
    <p><strong>Nikkei Asia (1 July 2025).</strong> &ldquo;Positive review only&rdquo;: Researchers hide AI prompts in papers. (Original investigative report.)</p>
    <p><strong>Cabanac, G., Labb&eacute;, C., Magazinov, A. (2024).</strong> Problematic Paper Screener. <a href="https://arxiv.org/abs/2402.03370" target="_blank" rel="noopener">arXiv:2402.03370</a>.</p>
    <p><strong>Retraction Watch ChatGPT tracker.</strong> <a href="https://retractionwatch.com/papers-and-peer-reviews-with-evidence-of-chatgpt-writing/" target="_blank" rel="noopener">retractionwatch.com</a> (running list).</p>
    <p><strong>NIH Notice NOT-OD-23-149 (23 June 2023).</strong> <a href="https://grants.nih.gov/grants/guide/notice-files/NOT-OD-23-149.html" target="_blank" rel="noopener">grants.nih.gov</a>.</p>
    <p><strong>NSF Notice (14 December 2023).</strong> <a href="https://new.nsf.gov/news/notice-to-the-research-community-on-ai" target="_blank" rel="noopener">nsf.gov</a>.</p>
    <p><strong>UKRI policy (20 September 2024; updated 3 December 2024).</strong> <a href="https://www.ukri.org/publications/generative-artificial-intelligence-in-application-and-assessment-policy/" target="_blank" rel="noopener">ukri.org</a>.</p>
    <p><strong>ICMJE recommendations on AI use by authors.</strong> <a href="https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html" target="_blank" rel="noopener">icmje.org</a>.</p>
    <p><strong>NeurIPS 2025 LLM policy.</strong> <a href="https://neurips.cc/Conferences/2025/LLM" target="_blank" rel="noopener">neurips.cc</a>.</p>
    <p><strong>NRF General Application Guide 2025&ndash;2026.</strong> <a href="https://www.nrf.ac.za/wp-content/uploads/2025/02/General-Application-Guide-2025-2026.pdf" target="_blank" rel="noopener">nrf.ac.za PDF</a>. (Notable for the absence of any reference to AI.)</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 20px; margin-bottom: 15px;"><strong>Coming up in 11.4:</strong> we turn from the institutional landscape to the structural foundations of African AI sovereignty &mdash; defining what &ldquo;sovereign AI capacity&rdquo; means across five layers, and then going deep on the one that everything else depends on: compute. The South African CHPC, the Cassava&ndash;NVIDIA AI Factory, the stalled Microsoft&ndash;G42 Kenya deal, and the gap between what has been announced and what is actually built.</p>
"""


# ---------------------------------------------------------------------------
# Sub-Lesson 11.4 — Sovereign AI Capacity, and Why Compute Is the Floor
# ---------------------------------------------------------------------------

SL4_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>&ldquo;Sovereign AI&rdquo; is one of the most actively contested terms in technology policy right now. National governments are setting up Sovereign AI Units (the United Kingdom did so in 2025); chip vendors are signing &ldquo;AI factory&rdquo; partnerships with national governments; African researchers are developing distinct conceptions of what sovereignty means when the question is asked from the relational personhood traditions of African philosophy rather than from the geopolitical autonomy traditions of European international law. The word does enormous work, and it does that work very differently depending on who is using it.</p>
    <p>This sub-lesson reads sovereign AI from an African intellectual tradition first &mdash; from Mhlambi, Effoduh, the Esethu Framework, Mutung&#39;u and colleagues, and the AU&#39;s own strategy &mdash; and then evaluates the better-known vendor and Northern-analytical framings against that home base. The pedagogical claim is not that the African tradition is correct and the others are wrong, but that the relational conception of sovereignty that runs through African scholarship gives postgraduate researchers in this part of the world the sharpest analytical tool for thinking about the AI infrastructure they are about to live with.</p>
    <p>We then go deep on the layer of the picture that everything material depends on: <em>compute</em>. South Africa&#39;s CHPC, the Cassava&ndash;NVIDIA AI Factory, the Microsoft&ndash;G42 Kenya deal, the AU&#39;s &ldquo;AI Factory&rdquo; concept, and the gap between what has been announced and what is actually operational as of May 2026. We close with the question that matters most for the person reading this: <em>what compute can you, a postgraduate researcher at a South African university in 2026, actually use for your work?</em></p>
  </div>

  <h2 class="section-title">&#127757; An African Conception of AI Sovereignty</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Five strands of African scholarship and one African continental policy document together build something that is best described as a <em>relational</em> conception of AI sovereignty. They do not all use the same vocabulary, and not all of them use the word &ldquo;sovereignty&rdquo; explicitly, but reading them together produces an analytical position that is genuinely distinct from both the vendor framing and the Northern policy framing we look at below.</p>

  <div class="card-grid">
    <div class="card">
      <h3>Mhlambi (2020) &mdash; the philosophical substrate</h3>
      <p>Sabelo Mhlambi&#39;s Carr Center discussion paper <em>From Rationality to Relationality</em> argues that contemporary AI was built on a Western philosophical view of personhood as rationality, and that this view&#39;s contradictions are reproduced as the harms AI causes. Mhlambi proposes Ubuntu&#39;s relational personhood &mdash; personhood as a property of the relations between people rather than of an individual&#39;s capacity to reason &mdash; as an alternative substrate for AI ethics.</p>
      <p style="color: #888; font-size: 0.9em;">Mhlambi, S. (2020). Carr Center for Human Rights Policy, Harvard Kennedy School. <a href="https://carrcenter.hks.harvard.edu/publications/rationality-relationality-ubuntu-ethical-and-human-rights-framework-artificial" target="_blank" rel="noopener">carrcenter.hks.harvard.edu</a></p>
    </div>
    <div class="card">
      <h3>Effoduh (2026) &mdash; epistemic sovereignty</h3>
      <p>Writing in <em>Science and Public Policy</em>, Jake Effoduh proposes <strong>epistemic sovereignty</strong> as the explicit goal for African AI governance &mdash; the right to <em>frame</em> AI questions on African terms, not just to apply African answers to imported questions. Effoduh critiques what he calls <em>normative mimicry</em>: the tendency of African AI governance to import its concepts and frameworks wholesale from EU or US contexts, retaining the structure and substituting only the geography.</p>
      <p style="color: #888; font-size: 0.9em;">Effoduh, J. O. (2026). <em>Science and Public Policy</em> 53(2), 245&ndash;257. <a href="https://academic.oup.com/spp/article/53/2/245/8654721" target="_blank" rel="noopener">academic.oup.com</a></p>
    </div>
    <div class="card">
      <h3>The Esethu Framework (Rajab et al., 2025) &mdash; community-grounded data governance</h3>
      <p>The Esethu Framework, developed by a South-Africa-led team at ACL 2025, proposes community-centric licensing for African-language datasets: communities retain rights over how their language data is used, benefit-sharing is required, and the licence itself is structured to keep agency with the community rather than with the downstream model developer. The Vuk&#39;uzenzele isiXhosa corpus is the first published dataset under the framework.</p>
      <p style="color: #888; font-size: 0.9em;">Rajab, J., Aremu, A., Chimoto, E. A., et al. (2025). arXiv:2502.15916.</p>
    </div>
    <div class="card">
      <h3>Mutung&#39;u et al. (2026) &mdash; individual digital sovereignty</h3>
      <p>Grace Mutung&#39;u, Aaron Martin, and Magdalena Brewczy&#324;ska examine Worldcoin&#39;s Kenya operation as a case study in regulatory entrepreneurship. Their analytical move is to root <em>national</em> digital sovereignty in the prior duty of states to protect <em>individual</em> digital rights. Sovereignty, in this reading, is not primarily about who owns the infrastructure but about whose rights the infrastructure is bound to respect. We return to this case as a worked example in the next section.</p>
      <p style="color: #888; font-size: 0.9em;">Mutung&#39;u, G. et al. (2026). <em>Science and Public Policy</em> 53(2), 289&ndash;299. <a href="https://academic.oup.com/spp/article/53/2/289/8654728" target="_blank" rel="noopener">academic.oup.com</a></p>
    </div>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Two more strands sit alongside these. <strong>The CARE Principles</strong> &mdash; Collective Benefit, Authority to Control, Responsibility, Ethics &mdash; were drafted in Gaborone in 2018 at International Data Week, by the Global Indigenous Data Alliance, and have become the most-cited framework worldwide for Indigenous data sovereignty. The CARE Principles deliberately complement rather than replace the more familiar FAIR Principles (findable, accessible, interoperable, reusable): FAIR governs the data; CARE governs the relations between the data and the communities the data come from. The geographic anchor of the framework in Africa, and its conceptual closeness to the relational reading of sovereignty in Mhlambi and Esethu, makes CARE a natural companion to the African strand. <strong>The African Union Continental AI Strategy</strong> (July 2024), for its part, talks about sovereignty in its policy-document register &mdash; less analytically sharp than the academic papers above, but nonetheless committed to the principle that African AI capacity should be developed under African terms.</p>

  <div class="info-box">
    <h4>&#128587;&#127998;&#8205;&#9794;&#65039; Two practitioners worth naming</h4>
    <p><strong>Pelonomi Moiloa</strong>, CEO of Lelapa AI, has built much of her company&#39;s public positioning around the idea of <em>Resource-Efficient AI</em>: that African sovereign AI capacity is not best pursued by trying to replicate the compute footprint of Silicon Valley labs but by building models small enough and efficient enough that the available infrastructure can actually support them. InkubaLM, the 0.4 billion-parameter African-language model we covered in Week 10, is the engineering expression of that argument.</p>
    <p><strong>Vukosi Marivate</strong>, ABSA Chair of Data Science at the University of Pretoria and a co-founder of Lelapa AI, Deep Learning Indaba, and Masakhane, was awarded the Order of Mapungubwe (Silver) in 2024 for contributions to AI, computer science, and natural-language processing. He was subsequently seated on the UN Independent International Scientific Panel on AI (12 February 2026, 40 members), as the most prominent African member of that panel. Together, Moiloa and Marivate represent the operational and institutional arms of the African sovereignty conversation &mdash; the people building the infrastructure that the philosophical and policy positions are arguing about.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">What emerges, reading these strands together, is a <strong>relational conception of AI sovereignty</strong>: sovereignty as agency exercised by and for communities, grounded in relational personhood, mediated by licences and governance more than by walls and hardware, and located at the intersection of individual rights, community authority, and institutional capacity. The word &ldquo;sovereignty&rdquo; is doing serious analytical work here, and its content is recognisably continuous with the longer Ubuntu tradition rather than borrowed from Westphalian state-autonomy.</p>

  <h2 class="section-title">&#129494; The Worldcoin Kenya Case</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The sharpest single test of the relational conception of sovereignty is a case the Mutung&#39;u, Martin, and Brewczy&#324;ska paper treats in detail. It is worth narrating briefly here because it shows the analytical move the African strand is making, more clearly than any general statement could.</p>

  <div class="case-study">
    <h4>&#128481; Worldcoin in Kenya: a sovereignty case</h4>
    <p>In 2022 and 2023, Worldcoin (Sam Altman&#39;s biometric-identity venture, now operating as the World Network) signed up around 350,000 Kenyans by scanning their irises in exchange for a cryptocurrency token. The Kenyan Data Protection Commissioner suspended Worldcoin&#39;s operations in August 2023 and subsequently found multiple breaches of Kenya&#39;s 2019 Data Protection Act, including the absence of any lawful basis for the iris-data processing.</p>
    <p>The Mutung&#39;u et al. paper&#39;s analytical move is the one that matters here. The Worldcoin violation was <em>not</em> caused by an absence of African GPUs, African foundation models, or African data centres. It was caused by a foreign company extracting biometric data from Kenyan individuals under terms those individuals were not in a position to evaluate, and by a regulator that did not have the institutional capacity to enforce its rules before the harm had already occurred at scale. A &ldquo;sovereign AI&rdquo; agenda framed primarily around <em>infrastructure ownership</em> &mdash; the version we will look at below in the vendor framing &mdash; would not have prevented this. A sovereignty agenda framed around <em>the prior duty of the state to protect individual digital rights</em> &mdash; which is the framing Mutung&#39;u and colleagues argue for &mdash; goes directly to where the violation actually occurred.</p>
    <p>The pedagogical point: when an African government talks about &ldquo;sovereign AI&rdquo;, the most useful first question is not &ldquo;do we have our own compute?&rdquo; but &ldquo;<em>whose rights is the AI infrastructure we depend on bound to respect?</em>&rdquo;</p>
  </div>

  <h2 class="section-title">&#127465;&#127466; How Northern Framings Differ</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Two non-African framings of sovereign AI dominate the public discussion: a <em>vendor</em> framing led by NVIDIA, and an <em>analytical-policy</em> framing led by think tanks and academic policy centres. They differ from each other almost as much as they differ from the African strand, and they are worth holding distinct. The pedagogical point of this section is not to dismiss either &mdash; the policy strand in particular has substantial analytical value &mdash; but to be clear about what each is doing and to read it from the African home base rather than the other way around.</p>

  <div class="technical-detail">
    <h4>&#128184; The vendor framing: NVIDIA&#39;s &ldquo;sovereign AI&rdquo;</h4>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">In a widely-quoted appearance at the World Governments Summit in Dubai in February 2024, NVIDIA CEO Jensen Huang told national leaders that they should each build their own large language models, on their own infrastructure, in their own languages, because (in his framing) AI &ldquo;codifies your culture, your society&#39;s intelligence, your common sense, your history&rdquo;. NVIDIA&#39;s formal definition followed in a company blog post the same month: sovereign AI as a nation&#39;s capacity to produce AI using its own infrastructure, data, workforce, and business networks.</p>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">There is a real cultural-preservation argument inside this framing, and we should not pretend otherwise. The trouble is that every operational component the NVIDIA framing names &mdash; the GPUs, the data-centre buildouts, the AI factories, the national-scale model training &mdash; requires hardware NVIDIA sells. The company has subsequently announced &ldquo;AI factory&rdquo; partnerships with France, Italy, Japan, India, Saudi Arabia, the United Arab Emirates, and (covered below) South Africa via Cassava. The framing converts sovereignty anxiety into procurement urgency.</p>
    <p style="color: #444; line-height: 1.75;">Read from the relational sovereignty home base, the NVIDIA framing answers a different question than the African strand is asking. It addresses &ldquo;how does the nation acquire AI capacity?&rdquo; and is largely silent on &ldquo;whose rights does the resulting capacity protect?&rdquo;</p>
    <p style="color: #888; font-size: 0.9em;"><a href="https://blogs.nvidia.com/blog/what-is-sovereign-ai/" target="_blank" rel="noopener">NVIDIA blog, 28 February 2024</a>; <a href="https://blogs.nvidia.com/blog/world-governments-summit/" target="_blank" rel="noopener">Huang at World Governments Summit, 12 February 2024</a>.</p>
  </div>

  <div class="technical-detail">
    <h4>&#128218; The analytical-policy framing: Stanford HAI, Brookings, WEF</h4>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">A second strand &mdash; substantially different from the vendor framing &mdash; is the work emerging from policy-oriented academic centres and think tanks since late 2025. The clearest recent example is the Stanford HAI piece <em>AI Sovereignty&#39;s Definitional Dilemma</em> (Pava, Meinhardt, Cryst &amp; Landay), which argues that the concept is <em>&ldquo;systematically underspecified&rdquo;</em> and proposes a (why &times; where) matrix as a clearer analytical tool: <em>why</em> a government wants to reduce AI dependencies (cultural autonomy, national security, economic competitiveness, regulatory oversight) and <em>where</em> in the AI technology stack it wants to exercise that agency (infrastructure, data, models, applications, talent). The Stanford piece concludes that &ldquo;true AI sovereignty&rdquo; is best understood as the capacity to <strong>choose and reconfigure</strong> dependencies, not as full autonomy &mdash; what they call <em>strategic interdependence</em>.</p>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">The Brookings Institution&#39;s February 2026 paper <em>Is AI sovereignty possible? Balancing autonomy and interdependence</em> reaches a similar conclusion via a seven-layer stack analysis (minerals, energy, compute, networks, data, models, applications) and proposes &ldquo;managed interdependence&rdquo; as the policy goal. A World Economic Forum piece from April 2026, &ldquo;The myth of AI sovereignty&rdquo;, treats full-stack sovereignty as a &ldquo;high-cost proxy&rdquo; for the real underlying demand &mdash; resilience and autonomous control over deployment.</p>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">Two things are worth noting. First, the analytical-policy strand is largely <em>compatible</em> with the African relational reading. The Stanford piece itself explicitly cites M&#257;ori data governance &mdash; community consent and guardianship &mdash; as an example of how data sovereignty can be understood as a collective cultural asset rather than a market commodity, and notes that this contrasts with both market-driven and state-centric regimes. The CARE Principles drafted in Gaborone in 2018 sit in the same global Indigenous-data-sovereignty arc.</p>
    <p style="color: #444; line-height: 1.75;">Second, the framework the Stanford and Brookings teams propose is recognisably the same shape as the five-layer pedagogical synthesis we use below: <em>compute, data, models, policy, talent</em>. We make no claim that this synthesis is original. It is our teaching simplification of a layered analysis that has now been published in several converging forms.</p>
    <p style="color: #888; font-size: 0.9em;">Pava, J. N., Meinhardt, C., Cryst, E. &amp; Landay, J. A. <em>AI Sovereignty&#39;s Definitional Dilemma</em>, Stanford HAI, 2025. <a href="https://hai.stanford.edu/news/ai-sovereigntys-definitional-dilemma" target="_blank" rel="noopener">hai.stanford.edu</a>. Brookings Institution, February 2026. World Economic Forum, April 2026.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The takeaway: there is a serious analytical literature on sovereign AI that is largely orthogonal to the vendor framing, and it converges substantially with the African relational reading without explicitly arriving from it. The pedagogically useful position is the relational one, treated as home base, with the Stanford / Brookings analytical strand picked up where it provides additional tools (the (why &times; where) matrix; the layered stack; the &ldquo;strategic interdependence&rdquo; framing). The vendor strand is best read as a marketing position to evaluate against the others, not as analysis.</p>

  <h2 class="section-title">&#129520; A Five-Layer Pedagogical Synthesis</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">For the rest of this week, we use a deliberately simple five-layer breakdown of what &ldquo;AI capacity&rdquo; consists of. It is not original analysis; it is a teaching compression of the converging stack analyses just above. The five layers map onto the rest of the African half of the week: this sub-lesson (11.4) goes deep on the first, and 11.5 and 11.6 cover the others.</p>

  <div style="overflow-x: auto;">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Layer</th>
          <th>What it is</th>
          <th>African landscape (covered in...)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Compute</strong></td>
          <td>GPUs, data centres, power, networking. The physical floor.</td>
          <td>11.4 (the rest of this sub-lesson)</td>
        </tr>
        <tr>
          <td><strong>Data</strong></td>
          <td>Language corpora, domain data, governance.</td>
          <td>11.5</td>
        </tr>
        <tr>
          <td><strong>Models</strong></td>
          <td>Foundation models trained from scratch or adapted; benchmarks; evaluation.</td>
          <td>11.5</td>
        </tr>
        <tr>
          <td><strong>Policy</strong></td>
          <td>Continental and national AI strategies; regulatory frameworks; institutional capacity.</td>
          <td>11.6</td>
        </tr>
        <tr>
          <td><strong>Talent</strong></td>
          <td>Researcher pipelines; community infrastructure (Masakhane, Lanfrica, Indaba, AIMS).</td>
          <td>11.6</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 20px; margin-bottom: 15px;">We treat compute first because everything else in the stack ultimately depends on having physical hardware somewhere in the loop. We treat it last in pedagogical importance, because (as the Worldcoin case made clear) compute ownership without rights protection does not get you the sovereignty most worth having. Both are true at once.</p>

  <h2 class="section-title">&#9889; Why Compute Is the Floor</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Four flagship African compute initiatives anchor the public discussion about &ldquo;sovereign AI compute&rdquo;. As of May 2026, exactly one of the four is actually moving from announcement to operation. Reading the four together gives a sober picture of where the African compute landscape really is.</p>

  <div class="technical-detail">
    <h4>&#127481;&#127462; CHPC South Africa &mdash; the established baseline</h4>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">The Centre for High Performance Computing in Cape Town operates South Africa&#39;s public HPC service, anchored on the <em>Lengau</em> Dell/Intel cluster: roughly 1 PFLOPS peak, around 30,000 CPU cores, online since 2016. Lengau is still the production HPC nine years on. CHPC&#39;s GPU presence is a modest pool of 30 NVIDIA V100 nodes added in 2018 &mdash; useful for postgraduate work, heavily oversubscribed, and small by 2026 standards.</p>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">A roughly 4 PFLOPS direct-water-cooled successor cluster has been procured under the NICIS 2026&ndash;2030 business plan presented at the 2025 CHPC conference; it is described in the planning documents as the upgrade path. As of May 2026 it is not yet shown on the CHPC site as user-accessible.</p>
    <p style="color: #444; line-height: 1.75;"><strong>Honest reading:</strong> CHPC is real, operational, and free at the point of use for South African postgraduate researchers. It is not, and is not designed as, a dedicated national AI compute facility. The upgrade is in procurement.</p>
    <p style="color: #888; font-size: 0.9em;"><a href="https://www.chpc.ac.za/" target="_blank" rel="noopener">chpc.ac.za</a></p>
  </div>

  <div class="technical-detail">
    <h4>&#127922; Cassava Technologies + NVIDIA AI Factory &mdash; the operational case</h4>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">In March 2025 Cassava Technologies and NVIDIA announced a partnership to build &ldquo;AI Factories&rdquo; across Africa, with an ambitious initial South African deployment target. The South African AI Factory deployment was announced in March 2026, the Cape Town CPT1 expansion went live in May 2026 with full operation targeted within weeks of that announcement, and a 20 MW Johannesburg AI Factory was publicly announced in May 2026.</p>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;"><strong>Honest reading:</strong> of the four flagship sovereign-AI-compute initiatives examined in this sub-lesson, Cassava&ndash;NVIDIA is the one actually moving from announcement to operation in 2026. The South African deployment is on track. The continental rollout beyond South Africa is at the announcement stage.</p>
    <p style="color: #444; line-height: 1.75;">For an African researcher, the practical implication is dual: the most operationally serious sovereign-compute capacity coming online on the continent is being built by a private African data-centre company in partnership with the dominant foreign GPU vendor. Whether one calls that &ldquo;sovereign&rdquo;, in the relational sense developed above, depends on whose rights the resulting capacity is bound to protect &mdash; a question that goes beyond the engineering.</p>
    <p style="color: #888; font-size: 0.9em;"><a href="https://www.cassavatechnologies.com/cassava-scales-african-ai-infrastructure-with-nvidia-powered-ai-factories-to-accelerate-sovereign-data-capabilities/" target="_blank" rel="noopener">Cassava Technologies announcement</a></p>
  </div>

  <div class="technical-detail">
    <h4>&#127472;&#127466; Microsoft&ndash;G42 Kenya &mdash; the stalled case</h4>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">In May 2024, during a Kenyan state visit to Washington, Microsoft and G42 announced a $1 billion data-centre project at KenGen&#39;s Olkaria geothermal site. The plan: Phase 1 of 100 MW, scaling toward 1 GW long term. The deal was framed as the largest single Western technology investment in Africa to date.</p>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">As of May 2026 the project is stalled. The Kenyan Treasury declined to underwrite the load via Power Purchase Agreements. Kenyan officials publicly observed that the 1 GW figure would represent approximately one-third of Kenya&#39;s peak national generation capacity (~2.3 GW), and that meeting peak national demand at full build would &ldquo;require switching off half the country&rdquo;. The Ministry of Information has stated that the project is not withdrawn and that talks continue, but that the scale requires restructuring. No operational portion exists on site.</p>
    <p style="color: #444; line-height: 1.75;"><strong>Honest reading:</strong> the binding constraint here is not GPUs and not capital; it is grid capacity. This is the most important point in the entire compute deep-dive. We return to it below.</p>
    <p style="color: #888; font-size: 0.9em;"><a href="https://www.tomshardware.com/tech-industry/microsofts-1-billion-kenya-data-center-stalls-over-disagreements-on-power-capacity" target="_blank" rel="noopener">Tom&#39;s Hardware, May 2026</a></p>
  </div>

  <div class="technical-detail">
    <h4>&#127464;&#127481; AU &ldquo;AI Factory&rdquo; &mdash; the aspirational case</h4>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">The African Union Continental AI Strategy adopted at the 45th Executive Council in Accra in July 2024 refers to building African AI compute capacity. The Smart Africa Alliance&#39;s Africa AI Council, formally established in November 2025, was set up in part to pool continental resources for this. At the Kigali Global AI Summit on Africa in April 2025 a &ldquo;$60 billion Africa AI Fund&rdquo; was announced as a pledge envelope.</p>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;"><strong>Honest reading:</strong> the AU &ldquo;AI Factory&rdquo; concept exists, is endorsed, and is repeatedly cited in continental policy documents. There is no funded, operational, continental-scale AI compute facility tied to it. The $60 billion figure is a pledge envelope from multiple sources, not an audited fund with a known dispersal mechanism. The 12,000-GPU figure that sometimes appears in Africa-AI press coverage is from the Cassava&ndash;NVIDIA commercial deal, not from an AU-funded facility.</p>
    <p style="color: #444; line-height: 1.75;">For a postgraduate researcher trying to plan three years out, this matters: announcements at the continental policy level should be read carefully, and the timeline between announcement and operation in this domain is typically multiple years.</p>
    <p style="color: #888; font-size: 0.9em;"><a href="https://au.int/en/documents/20240809/continental-artificial-intelligence-strategy" target="_blank" rel="noopener">AU Continental AI Strategy, July 2024</a></p>
  </div>

  <div class="info-box">
    <h4>&#128205; Brief on the other major facilities</h4>
    <p><strong>Konza National Data Centre (Kenya)</strong> &mdash; Tier-III, operational since 2021, around 120 customers across more than 70 city services. Not an AI-specialised facility; Kenya&#39;s &ldquo;first GPU-powered AI infrastructure&rdquo; claim refers to Atlancis (private), not Konza.</p>
    <p><strong>Egypt</strong> &mdash; the Ain Sokhna national data hub was inaugurated in April 2024 (general government workload, not a published AI/GPU cluster). The National AI Strategy 2025&ndash;2030 was launched in January 2025 and frames further state-owned data-centre construction.</p>
    <p><strong>Nigeria</strong> &mdash; the National Centre for AI and Robotics (NCAIR) has no publicly listed GPU cluster as of May 2026. The National AI Strategy was published 19 September 2025. A private Airtel facility in Lagos with GPUs delivered in late 2025 is a commercial buildout, not a national one.</p>
    <p><strong>Morocco</strong> &mdash; a $1.2 bn &ldquo;Nexus AI Factory&rdquo; in Casablanca was announced at GITEX Africa 2026. Not yet built.</p>
    <p><strong>Rwanda</strong> &mdash; National AI Policy adopted; hosted the April 2025 Kigali summit. No operational national AI compute yet beyond strategy.</p>
  </div>

  <h2 class="section-title">&#128268; The Grid Bottleneck, Made Concrete</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The single most important empirical point in the African compute picture is that the binding constraint, almost everywhere, is grid capacity rather than GPU supply. The Microsoft&ndash;G42 Kenya stall is the cleanest demonstration. Here is the arithmetic that makes the point unavoidable.</p>

  <div class="technical-detail">
    <h4>&#128202; The numbers, roughly</h4>
    <ul class="styled-list" style="margin-top: 0;">
      <li>A single NVIDIA H100 GPU server (eight H100s plus host) draws roughly <strong>10 kW</strong> under load.</li>
      <li>3,000 H100s &mdash; the kind of cluster the Cassava South African site is designed for &mdash; therefore draws roughly <strong>30 MW</strong> of IT load, with a further 5&ndash;10 MW for cooling. Cassava&#39;s 20 MW Johannesburg AI Factory site is sized to host roughly this scale.</li>
      <li>The original Microsoft&ndash;G42 Kenya target of 1 GW would draw <strong>about a third of Kenya&#39;s peak national generation capacity</strong> (Kenya&#39;s peak demand is around 2.3 GW). Underwriting that load via PPAs is the politically and financially impossible thing the project ran into.</li>
      <li>South Africa has, briefly, the comparative advantage of <em>recovered Eskom capacity</em> after the worst years of load-shedding. The Cassava deployments in Cape Town and Johannesburg are sized within what that recovered capacity can carry. This is part of the operational case for why the South African AI Factory deployment is the one moving.</li>
    </ul>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The practical implication is that &ldquo;Africa needs more GPUs&rdquo; is the wrong slogan. <em>Africa needs the grid capacity to power the GPUs it can already procure.</em> Renewable build-out, transmission infrastructure, and (in South Africa&#39;s case) the recovery of existing thermal capacity are the binding constraints. This is why Microsoft&ndash;G42 chose Olkaria geothermal in the first place; it is also why the project has stalled. The energy story we covered in Week 3 connects directly to the sovereignty story here.</p>

  <h2 class="section-title">&#128105;&#127997;&#8205;&#127979; Practical Compute Access for You, Today</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">All of the above sets the policy and infrastructure context. The question that matters more for a postgraduate researcher at UCT or any African institution in May 2026 is narrower and more immediate: <em>what compute can I actually use this week?</em></p>

  <div class="card-grid">
    <div class="card">
      <h3>UCT African Compute Initiative (ACI)</h3>
      <p>Announced in March 2026 and led from UCT, the African Compute Initiative is the most directly relevant near-term option for postgraduate AI work on the continent. The plan is for an operational cluster within twelve months, scaling to roughly 100 users in the first year and around 300 users across at least five partner institutions by year three. The initiative is positioned explicitly as African higher-education-dedicated AI compute &mdash; the missing piece in the picture above. Interim Director: A/Prof Jonathan Shock, UCT (the instructor of this course).</p>
      <p style="color: #888; font-size: 0.9em;"><a href="https://ai.uct.ac.za/articles/2026-03-26-uct-lead-africas-first-higher-education-dedicated-ai-compute-initiative" target="_blank" rel="noopener">UCT AI ACI announcement</a></p>
    </div>
    <div class="card">
      <h3>CHPC allocations</h3>
      <p>South-Africa-affiliated PhD students are entitled to free allocations on Lengau (CPU) and the V100 GPU pool. Allocations are requested via <a href="https://wiki.chpc.ac.za" target="_blank" rel="noopener">wiki.chpc.ac.za</a>. The V100 pool is small and heavily oversubscribed; it is a usable resource for individual experiments but should not be treated as a frontier-model training facility.</p>
      <p style="color: #888; font-size: 0.9em;"><a href="https://www.chpc.ac.za/" target="_blank" rel="noopener">chpc.ac.za</a></p>
    </div>
    <div class="card">
      <h3>Cassava GPUaaS</h3>
      <p>The Cassava AI Factory deployments will be commercially available as GPU-as-a-Service. Coverage during 2026 will be largely via institutional contracts and pre-reservation agreements with universities, banks, and start-ups rather than via an individual-researcher self-service tier.</p>
      <p style="color: #888; font-size: 0.9em;"><a href="https://www.cassavatechnologies.com/" target="_blank" rel="noopener">cassavatechnologies.com</a></p>
    </div>
    <div class="card">
      <h3>Free-tier cloud (the honest default)</h3>
      <p>For day-to-day individual experiments, the practical default for most African postgraduate researchers in May 2026 remains the US free-tier cloud: Google Colab&#39;s free T4 GPU (15&ndash;30 hours per week, depending on usage history), Kaggle&#39;s free T4 and P100 access (30+ hours per week), and Hugging Face Spaces (shared CPU and limited GPU). These are imperfect, foreign, and depend on the continued generosity of US platforms &mdash; but they are what is actually usable today by most students.</p>
    </div>
  </div>

  <div class="highlight-box">
    <h3>&#128161; <span style="color: #ffffff;">The honest position, summarised</span></h3>
    <p>As of May 2026, an African postgraduate researcher still primarily depends on US free-tier cloud for day-to-day AI compute work. Dedicated national and continental compute capacity is announced and partly procured but not yet broadly available. The UCT African Compute Initiative is the most concrete near-term change to this picture and is worth applying to early. CHPC remains the SA fallback for institutional academic use.</p>
    <p style="margin-top: 15px;">Sovereign compute, in the sense of physical infrastructure on African soil that African researchers can use, is real and growing &mdash; but in May 2026 it is still smaller than the foreign cloud capacity most of us actually run on.</p>
  </div>

  <h2 class="section-title">&#127919; What This Means for Your Research</h2>

  <ul class="styled-list">
    <li><strong>Design for the compute you can actually access.</strong> A research project that requires training a 70B-parameter model from scratch is not feasible from an African university institution in May 2026, with or without free-tier cloud. A research project that requires fine-tuning a 7B-parameter model, or running inference on a hosted frontier model, is feasible. The sovereign-compute story above should inform the <em>scope</em> of your project, not just your politics.</li>
    <li><strong>Resource efficiency is a sovereignty practice.</strong> The Lelapa argument &mdash; that building smaller, more efficient models on accessible infrastructure is itself a sovereignty move &mdash; is operationally honest about the current picture. InkubaLM, MzansiLM, and the other African foundation models we covered in Week 10 are examples of this strategy in practice.</li>
    <li><strong>Apply to the UCT ACI now if it fits your work.</strong> The initiative&#39;s first-year cohort is small (~100 users) and the application process is being set up during 2026. Postgraduates in this course are exactly the audience the initiative is for.</li>
    <li><strong>Think of compute as one of five layers, not as the whole picture.</strong> The Worldcoin case is the reminder. Even if every GPU you used was hosted in Africa under African ownership, that on its own would not guarantee that the rights of the people whose data the model was trained on were protected. The other layers &mdash; data governance, model evaluation, policy, and talent &mdash; are where the African sovereignty conversation is doing some of its most distinctive work. We cover them in 11.5 and 11.6.</li>
  </ul>

  <h2 class="section-title">&#9999;&#65039; A Short Exercise</h2>

  <ol class="step-list">
    <li><strong>Identify the compute you would realistically need</strong> for the AI component of your current or planned research project. Order of magnitude is fine &mdash; tens of GPU-hours, hundreds, thousands, more.</li>
    <li><strong>Map what you actually have access to.</strong> Free-tier cloud? CHPC? A departmental cluster? A collaborator&#39;s allocation? An institutional pre-reservation on the Cassava AI Factory? Be honest.</li>
    <li><strong>If there is a mismatch between (1) and (2),</strong> describe in one paragraph how you would rescope the project so the compute is actually feasible. The rescoping might mean smaller models, fewer experiments, a different research question, or a different collaboration structure.</li>
    <li><strong>Find one piece of African-authored work on AI sovereignty</strong> from the sources listed below, read it, and write one further paragraph on whether the sovereignty position it takes changes how you think about the compute you depend on.</li>
    <li><strong>Bring all four to class.</strong> We will pool them and look at the patterns across the cohort.</li>
  </ol>

  <h2 class="section-title">&#128218; Sources &amp; Further Reading</h2>

  <div class="resource-placeholder">
    <h4>&#128196; African voices on sovereignty</h4>
    <p><strong>Mhlambi, S. (2020).</strong> <em>From Rationality to Relationality: Ubuntu as an Ethical and Human Rights Framework for Artificial Intelligence Governance.</em> Carr Center Discussion Paper 2020-009, Harvard Kennedy School. <a href="https://carrcenter.hks.harvard.edu/publications/rationality-relationality-ubuntu-ethical-and-human-rights-framework-artificial" target="_blank" rel="noopener">Carr Center</a>.</p>
    <p><strong>Effoduh, J. O. (2026).</strong> Decolonizing the governance of artificial intelligence in Africa: from normative mimicry to epistemic sovereignty. <em>Science and Public Policy</em> 53(2), 245&ndash;257. <a href="https://academic.oup.com/spp/article/53/2/245/8654721" target="_blank" rel="noopener">academic.oup.com</a>.</p>
    <p><strong>Rajab, J., Aremu, A., Chimoto, E. A. et al. (2025).</strong> The Esethu Framework. <a href="https://arxiv.org/abs/2502.15916" target="_blank" rel="noopener">arXiv:2502.15916</a>.</p>
    <p><strong>Mutung&#39;u, G., Martin, A. &amp; Brewczy&#324;ska, M. (2026).</strong> Regulatory entrepreneurship&#39;s threat to digital sovereignty: the case of Worldcoin in Kenya. <em>Science and Public Policy</em> 53(2), 289&ndash;299. <a href="https://academic.oup.com/spp/article/53/2/289/8654728" target="_blank" rel="noopener">academic.oup.com</a>.</p>
    <p><strong>Carroll, S. R., Garba, I., Figueroa-Rodr&iacute;guez, O. L., Holbrook, J., Lovett, R., Materechera, S., Parsons, M., Raseroka, K., Rodriguez-Lonebear, D., Rowe, R., Sara, R., Walker, J. D., Anderson, J. &amp; Hudson, M. (2020).</strong> The CARE Principles for Indigenous Data Governance. <em>Data Science Journal</em> 19(1): 43. Drafted at Gaborone in 2018. <a href="https://www.gida-global.org/care" target="_blank" rel="noopener">GIDA</a>.</p>
    <p><strong>African Union (2024).</strong> Continental Artificial Intelligence Strategy. Endorsed by the 45th Executive Council, Accra. <a href="https://au.int/en/documents/20240809/continental-artificial-intelligence-strategy" target="_blank" rel="noopener">au.int</a>.</p>
  </div>

  <div class="resource-placeholder">
    <h4>&#128196; Northern framings</h4>
    <p><strong>NVIDIA (28 February 2024).</strong> What Is Sovereign AI? Company blog. <a href="https://blogs.nvidia.com/blog/what-is-sovereign-ai/" target="_blank" rel="noopener">blogs.nvidia.com</a>. With Jensen Huang&#39;s World Governments Summit appearance, 12 February 2024.</p>
    <p><strong>Pava, J. N., Meinhardt, C., Cryst, E. &amp; Landay, J. A. (2025).</strong> <em>AI Sovereignty&#39;s Definitional Dilemma</em>. Stanford HAI. <a href="https://hai.stanford.edu/news/ai-sovereigntys-definitional-dilemma" target="_blank" rel="noopener">hai.stanford.edu</a>.</p>
    <p><strong>Brookings Institution (February 2026).</strong> <em>Is AI sovereignty possible? Balancing autonomy and interdependence</em>. <a href="https://www.brookings.edu/articles/is-ai-sovereignty-possible-balancing-autonomy-and-interdependence/" target="_blank" rel="noopener">brookings.edu</a>.</p>
    <p><strong>World Economic Forum (April 2026).</strong> The myth of AI sovereignty. <a href="https://www.weforum.org/stories/2026/04/the-myth-of-ai-sovereignty/" target="_blank" rel="noopener">weforum.org</a>.</p>
  </div>

  <div class="resource-placeholder">
    <h4>&#128196; Compute facilities &amp; practical access</h4>
    <p><strong>UCT African Compute Initiative.</strong> <a href="https://ai.uct.ac.za/articles/2026-03-26-uct-lead-africas-first-higher-education-dedicated-ai-compute-initiative" target="_blank" rel="noopener">ai.uct.ac.za</a>.</p>
    <p><strong>CHPC.</strong> <a href="https://www.chpc.ac.za/" target="_blank" rel="noopener">chpc.ac.za</a>. Allocation requests via <a href="https://wiki.chpc.ac.za" target="_blank" rel="noopener">wiki.chpc.ac.za</a>.</p>
    <p><strong>Cassava Technologies.</strong> <a href="https://www.cassavatechnologies.com/cassava-scales-african-ai-infrastructure-with-nvidia-powered-ai-factories-to-accelerate-sovereign-data-capabilities/" target="_blank" rel="noopener">cassavatechnologies.com</a> (March 2025 partnership announcement).</p>
    <p><strong>Tom&#39;s Hardware (May 2026).</strong> Microsoft&#39;s $1 billion Kenya data center stalls over disagreements on power capacity. <a href="https://www.tomshardware.com/tech-industry/microsofts-1-billion-kenya-data-center-stalls-over-disagreements-on-power-capacity" target="_blank" rel="noopener">tomshardware.com</a>.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 20px; margin-bottom: 15px;"><strong>Coming up in 11.5:</strong> we leave the compute layer and turn to the African landscape of <em>data</em> and <em>models</em>. The Masakhane&ndash;Lanfrica&ndash;Lelapa lineage; from-scratch African foundation models including UCT&#39;s own MzansiLM; the African benchmark stack (AfroBench, IrokoBench, AfriMTEB, AfriSpeech-200); and the global Indigenous-data-sovereignty arc that connects CARE Principles, M&#257;ori data governance, and the Esethu Framework.</p>
"""


# ---------------------------------------------------------------------------
# Sub-Lesson 11.5 — Data, Languages and African Model-Building
# ---------------------------------------------------------------------------

SL5_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>Sub-Lesson 11.4 closed on the compute layer. We turn now to the other three layers in the stack that African researchers have actually <em>built</em> over the last few years: the data they govern, the models they train, and the benchmarks they use to measure progress. This is the most concretely positive part of the African AI story. The infrastructure conversation in 11.4 was substantially aspirational; the data-and-models conversation in 11.5 is substantially shipping.</p>
    <p>This sub-lesson is structured around three pillars and one survey paper. The survey is Alabi, Hedderich, Adelani &amp; Klakow&#39;s 2025 <em>Charting the Landscape of African NLP</em>, which mapped 884 papers over five years and is the most comprehensive recent overview of the field. The three pillars are: a <em>global Indigenous data-sovereignty arc</em> that runs from Te Hiku Media&#39;s Kaitiakitanga License through the CARE Principles to the Esethu Framework; an <em>African foundation-model inventory</em> that is genuinely substantial, structured by family and led by <strong>InkubaLM</strong> (Lelapa) and <strong>MzansiLM</strong> (UCT); and an <em>African benchmark stack</em> with new 2026 additions worth foregrounding.</p>
    <p>We close on the pedagogically most useful split in the current literature &mdash; sovereign/frontier-aspirant projects (Awarri&#39;s N-ATLAS in Nigeria) versus resource-efficient/pragmatic projects (Lelapa&#39;s InkubaLM family) &mdash; and a section on where the <em>gaps</em> are: the thesis-shaped opportunities that postgraduate researchers in this course are well placed to close.</p>
  </div>

  <h2 class="section-title">&#128205; The Map: Charting the Landscape of African NLP</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">If you read only one survey paper before going further into the African NLP literature, make it this one.</p>

  <div class="technical-detail">
    <h4>&#128218; Alabi, Hedderich, Adelani &amp; Klakow (2025) &mdash; Charting the Landscape of African NLP</h4>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">Jesujoba O. Alabi, Michael A. Hedderich, David Ifeoluwa Adelani &amp; Dietrich Klakow. <em>Charting the Landscape of African NLP.</em> EMNLP 2025 main, pp. 27807&ndash;27841. <a href="https://arxiv.org/abs/2505.21315" target="_blank" rel="noopener">arXiv:2505.21315</a>.</p>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">The paper systematically surveys 884 African-NLP papers over a five-year window and produces a map that is genuinely useful for navigation. It documents which languages have been worked on (and how unevenly), which tasks dominate the literature (MT, NER, sentiment, and ASR are the largest), which institutions are most active, and where the cross-cultural and cross-linguistic blind spots lie. If you are starting a project on African NLP and you do not know the lay of the land, this is where to begin.</p>
    <p style="color: #444; line-height: 1.75;">A complement worth noting: Belay, Azime, Adelani et al.&#39;s <em>The Rise of AfricaNLP</em> (<a href="https://arxiv.org/abs/2509.25477" target="_blank" rel="noopener">arXiv:2509.25477</a>, September 2025, updated April 2026) provides the bibliometric companion &mdash; 2,200 papers analysed for community impact and contributor patterns.</p>
  </div>

  <div class="info-box">
    <h4>&#128202; The single most useful number from the recent literature</h4>
    <p>A June 2025 quantitative survey, <em>The State of Large Language Models for African Languages: Progress and Challenges</em> (Hussen, Sewunetie, Ayele, Imam, Muhammad &amp; Yimam, <a href="https://arxiv.org/abs/2506.02280" target="_blank" rel="noopener">arXiv:2506.02280</a>), measured what current LLM families actually cover. The headline finding: across six large LLMs, eight small LMs, and six smaller models, just <strong>42 African languages</strong> receive meaningful support. Africa has roughly two thousand languages. <strong>~98% of African languages remain unsupported</strong> by current foundation-model infrastructure. The script picture is similar: current LLM tokenisers handle Latin, Arabic, and Ge&#39;ez but not the roughly 20 active African scripts (Tifinagh, N&#39;Ko, Vai, Adlam and others).</p>
    <p>This is the single most useful framing number for the whole African-model conversation. The space is vastly under-served; the work that exists is significant precisely because of how much more there is to do.</p>
  </div>

  <h2 class="section-title">&#127757; The Global Indigenous Data-Sovereignty Arc</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Before we look at the models, we look at the framework under which African researchers are choosing to release the data the models are built on. This conversation does not start with African scholarship; it sits inside a longer, global Indigenous data-sovereignty tradition. Naming that lineage matters, because the African work is part of a wider movement that has been theorising community-grounded data governance for considerably longer than the current AI moment has been running.</p>

  <div class="card-grid">
    <div class="card">
      <h3>Te Hiku Media &amp; the Kaitiakitanga License</h3>
      <p>Te Hiku Media (<a href="https://tehiku.nz" target="_blank" rel="noopener">tehiku.nz</a>), an <em>iwi</em> radio station and media hub representing five Far-North M&#257;ori iwi (Ng&#257;ti Kuri, Te Aup&#333;uri, Ng&#257;i Takoto, Te Rarawa, Ng&#257;ti Kahu), was established as Te Hiku O Te Ika at Awanui in December 1990. The organisation built the foundational ASR work for te reo M&#257;ori, reporting around 92% accuracy for monolingual M&#257;ori speech. To govern the speech data the community contributed, Te Hiku developed the <strong>Kaitiakitanga License</strong>, which treats the organisation as <em>kaitiaki</em> &mdash; guardian, not owner &mdash; of the data, and explicitly prohibits uses that would surveil, discriminate against, or harm M&#257;ori people. This is the most-cited Indigenous-data-license precedent in the African NLP literature.</p>
      <p style="color: #888; font-size: 0.9em;">Jones, K. &amp; Mahelona, K. <em>Data Sovereignty and the Kaitiakitanga License</em> (Te Hiku Media, 2022, updated 2023). <a href="https://tehiku.nz/te-hiku-tech/te-hiku-dev-korero/25141/data-sovereignty-and-the-kaitiakitanga-license" target="_blank" rel="noopener">tehiku.nz</a>.</p>
    </div>
    <div class="card">
      <h3>The CARE Principles</h3>
      <p>The <strong>CARE Principles for Indigenous Data Governance</strong> (Carroll, Garba, Figueroa-Rodr&iacute;guez, Holbrook, Lovett, Materechera, Parsons, Raseroka, Rodriguez-Lonebear, Rowe, Sara, Walker, Anderson &amp; Hudson, 2020) generalise the Te Hiku-style position into a four-principle framework: <strong>Collective Benefit</strong>, <strong>Authority to Control</strong>, <strong>Responsibility</strong>, and <strong>Ethics</strong>. The principles were drafted at International Data Week in <em>Gaborone, in November 2018</em>, by the RDA International Indigenous Data Sovereignty Interest Group. By 2026 CARE has been adopted by the Research Data Alliance, the Global Indigenous Data Alliance (GIDA), the Australian Research Data Commons, and the US NIH&#39;s genomic-data policy.</p>
      <p style="color: #888; font-size: 0.9em;">Carroll, S. R. et al. (2020). <em>Data Science Journal</em> 19(1): 43. <a href="https://datascience.codata.org/articles/10.5334/dsj-2020-043" target="_blank" rel="noopener">DOI 10.5334/dsj-2020-043</a>. GIDA: <a href="https://www.gida-global.org/whoweare" target="_blank" rel="noopener">gida-global.org</a>.</p>
    </div>
    <div class="card">
      <h3>The Esethu Framework</h3>
      <p>The Esethu Framework (Rajab, Aremu, Chimoto, Dunbar, Morrissey, Thior, Potgieter, Ojo, Tonja, Chetty, Nekoto, Moiloa, Abbott, Marivate &amp; Rosman, 2025) is the African strand&#39;s most developed published proposal. It introduces a community-centric <em>Esethu License</em> under which commercial users &mdash; especially non-African ones &mdash; pay a fee that is reinvested into dataset expansion via local partners. The proof-of-concept dataset is the <strong>Vuk&#39;uzenzele isiXhosa Speech Dataset (ViXSD)</strong>. The author team draws across Wits, Lelapa AI, and Masakhane; the lineage is explicit about citing Kaitiakitanga as a precedent.</p>
      <p style="color: #888; font-size: 0.9em;">Rajab, J. et al. (2025). <a href="https://arxiv.org/abs/2502.15916" target="_blank" rel="noopener">arXiv:2502.15916</a>; <a href="https://aclanthology.org/2025.acl-long.1487/" target="_blank" rel="noopener">ACL 2025</a>.</p>
    </div>
    <div class="card">
      <h3>The wider tradition</h3>
      <p>Two more strands belong in the global arc. <strong>OCAP</strong> (Ownership, Control, Access, Possession), developed by the First Nations Information Governance Centre in Canada since 1998, is the oldest of the institutional frameworks. <strong>S&aacute;pmi data governance</strong>, articulated by the S&aacute;mi Council and discussed at the first S&aacute;mi Research Data Governance conference in Troms&oslash; in January 2023, articulates a parallel European-Indigenous tradition. These traditions are not interchangeable, but reading them alongside the African strand makes clear that the relational conception of data governance is genuinely global.</p>
      <p style="color: #888; font-size: 0.9em;">OCAP: <a href="https://fnigc.ca/ocap-training/" target="_blank" rel="noopener">FNIGC</a>. Eriksen et al. (2024), <em>Nordic Journal of Library and Information Studies</em>.</p>
    </div>
  </div>

  <div class="info-box">
    <h4>&#129496; The lineage in one sentence</h4>
    <p>Kaitiakitanga (Te Hiku, M&#257;ori, since the early 2010s in the AI context) &rarr; CARE Principles (drafted in <em>Gaborone</em> in 2018, published 2020) &rarr; Esethu Framework (Rajab et al., ACL 2025). The African work is the most recent expression of a global Indigenous tradition that explicitly traces its own intellectual lineage back through M&#257;ori and First Nations scholarship.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">For policy context at the African continental level: the <strong>AU Data Policy Framework</strong> (adopted February 2022, published 28 July 2022) sets the stated continental orientation toward transparency, accountability, inclusion, and equity, aimed at an African Digital Single Market by 2030. The <strong>AU Continental AI Strategy</strong> (July 2024) explicitly invokes data sovereignty across its five focus areas. Both documents are real and worth reading; both, as we noted in 11.4, are policy positions rather than enforced regulatory mechanisms.</p>

  <div class="warning-box">
    <h4>&#9888;&#65039; An honest gap to flag</h4>
    <p>There is, as of May 2026, <em>no peer-reviewed African critique-and-adaptation of the CARE Principles</em>: a paper arguing what would need to change for CARE to be made specifically African rather than imported with adjustments. Adam Birhane and Rediet Abebe&#39;s work orbits this question; the AfricaNLP licensing conversation (Marivate, Adelani, Rajab et al.) is making constructive moves in practice. But the central critical paper has not been written yet. We return to this in the gaps section at the end of the sub-lesson, because it is one of the most concrete thesis opportunities the literature currently offers.</p>
    <p>A related practical gap: <em>most African datasets released in 2024 and 2025 still go up under CC-BY or research-only licences</em>, not under Kaitiakitanga- or Esethu-style community licences. The rhetorical commitment to community licensing is genuinely there; the operational uptake is not yet matching it. ViXSD is so far the proof of concept, not the beginning of a wave.</p>
  </div>

  <h2 class="section-title">&#129309; Community Infrastructure: Masakhane, Lanfrica, AfricaNLP, Indaba</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Before the foundation models, before the benchmarks, before the licensed datasets &mdash; there is the community infrastructure that makes everything else possible. Four organisations or venues are doing the disproportionate share of the work.</p>

  <div class="card-grid">
    <div class="card">
      <h3>Masakhane</h3>
      <p>Founded around 2019 out of an ICLR Africa workshop, Masakhane is the grassroots research community that has anchored modern African NLP. The flagship projects are <strong>MasakhaNER</strong> (named-entity recognition across African languages), <strong>MAFAND-MT</strong> / <strong>LAFAND-MT</strong> (machine translation), <strong>MasakhaNEWS</strong> (16 languages, news topic classification, arXiv:2304.09972), and <strong>MasakhaPOS</strong> (20 languages, part-of-speech tagging, arXiv:2305.13989). Masakhane&#39;s public-facing website at <a href="https://www.masakhane.io/" target="_blank" rel="noopener">masakhane.io</a> displays older figures, but the organisation is very much active &mdash; the GitHub and HuggingFace organisations (<a href="https://huggingface.co/masakhane" target="_blank" rel="noopener">huggingface.co/masakhane</a>) show dataset and code updates well into 2025, and Masakhane members are the substantial author overlap on InkubaLM, Esethu, and most of the AfricaNLP 2025 proceedings.</p>
    </div>
    <div class="card">
      <h3>Lanfrica</h3>
      <p>Founded by Chris C. Emezue and Bonaventure F. P. Dossou, Lanfrica (<a href="https://lanfrica.com" target="_blank" rel="noopener">lanfrica.com</a>) is the pan-African resource catalogue that indexes datasets, papers, models, and projects across roughly <strong>2,199 African languages</strong> (including extinct languages). In 2025 Lanfrica ran the NaijaVoices Language Heritage Micro-Grants programme, supporting six community-led Nigerian-language projects, and Emezue presented &ldquo;Data Farming and the QRUE Frameworks&rdquo; at LT4ALL 2025. If you are looking for whether a resource exists in a specific African language, Lanfrica is the right first stop.</p>
    </div>
    <div class="card">
      <h3>AfricaNLP 2025 (ACL Vienna)</h3>
      <p>The Sixth AfricaNLP Workshop, co-located with ACL 2025 in Vienna on <strong>31 July 2025</strong>, was the <em>first archival edition</em> of the workshop &mdash; 28 archival and 7 non-archival papers under the theme &ldquo;Multilingual and Multicultural-aware LLMs&rdquo;. Editors: Constantine Lignos (Brandeis), Idris Abdulmumin, and David Ifeoluwa Adelani. Proceedings: <a href="https://aclanthology.org/2025.africanlp-1.0/" target="_blank" rel="noopener">aclanthology.org/2025.africanlp-1.0/</a>. The archival status is a small but consequential change: AfricaNLP papers now carry the full bibliographic weight of an ACL workshop proceedings.</p>
    </div>
    <div class="card">
      <h3>Deep Learning Indaba 2025</h3>
      <p>The seventh Deep Learning Indaba was held in <strong>Kigali, Rwanda, 17&ndash;22 August 2025</strong>, hosted by the University of Rwanda under the theme <em>Urunana &mdash; Hand in Hand for AI in Africa</em>. Over 1,000 participants, 12 workshops, and the by-now-standard mix of mentoring, research showcases, and the African AI community&#39;s most important annual gathering. Indaba does not produce an archival proceedings volume; the research output sits on OpenReview and at the contributing labs.</p>
      <p style="color: #888; font-size: 0.9em;"><a href="https://deeplearningindaba.com/2025/" target="_blank" rel="noopener">deeplearningindaba.com/2025</a></p>
    </div>
  </div>

  <h2 class="section-title">&#129504; The African Foundation-Model Inventory</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">What follows is a verified inventory of the foundation models &mdash; encoder, from-scratch decoder, adapted decoder, and named-language &mdash; that are actually shipping for African languages as of May 2026. Two centrepieces matter most for this course: <strong>InkubaLM</strong> (the first sovereign African small language model, from Lelapa AI) and <strong>MzansiLM</strong> (the UCT-built decoder covering all eleven official South African written languages).</p>

  <div class="technical-detail">
    <h4>&#127759; Encoder-family foundations</h4>
    <ul class="styled-list" style="margin-top: 0;">
      <li><strong>AfriBERTa</strong> (Ogueji, Zhu, Lin, Waterloo, MRL 2021). The early demonstration that high-quality language modelling for low-resource African languages is possible with less than 1 GB of text. 11 African languages.</li>
      <li><strong>AfroXLMR</strong> (Alabi et al., <a href="https://arxiv.org/abs/2204.06487" target="_blank" rel="noopener">arXiv:2204.06487</a>, 2022). Multilingual adaptive fine-tuning (MAFT) of XLM-R for African languages. Updated variant <strong>AfroXLMR-Social</strong> (<a href="https://arxiv.org/abs/2503.18247" target="_blank" rel="noopener">arXiv:2503.18247</a>, March 2025) by Belay, Azime, Adelani et al.</li>
      <li><strong>AfroLM</strong> (Dossou, Tonja, Yousuf, Osei et al., <a href="https://arxiv.org/abs/2211.03263" target="_blank" rel="noopener">arXiv:2211.03263</a>, SustainNLP 2022). 23 African languages, active-learning-based.</li>
      <li><strong>Serengeti</strong> (Adebara, Elmadany, Abdul-Mageed &amp; Inciarte, UBC NLP, <a href="https://arxiv.org/abs/2212.10785" target="_blank" rel="noopener">arXiv:2212.10785</a>, Findings of ACL 2023). Massively multilingual: 517 African languages and varieties. The widest-coverage encoder model published to date.</li>
    </ul>
  </div>

  <div class="technical-detail">
    <h4>&#129666; From-scratch decoder models &mdash; the African sovereign small-LM lineage</h4>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;"><strong>InkubaLM</strong> (Lelapa AI; <a href="https://arxiv.org/abs/2408.17024" target="_blank" rel="noopener">arXiv:2408.17024</a>, August 2024). Authors: Atnafu Lambebo Tonja, Bonaventure F. P. Dossou, Jessica Ojo, Jenalea Rajab, Fadel Thior, Eric Peter Wairagala, Anuoluwapo Aremu, Pelonomi Moiloa, Jade Abbott, Vukosi Marivate, Benjamin Rosman. 0.4B parameters (422M), trained on 2.4B tokens of which 1.9B are African-language tokens. Languages: isiZulu, Yoruba, Swahili, isiXhosa, Hausa, English, French. CC&nbsp;BY-NC 4.0. Model card: <a href="https://huggingface.co/lelapa/InkubaLM-0.4B" target="_blank" rel="noopener">huggingface.co/lelapa/InkubaLM-0.4B</a>. The first published <em>from-scratch</em> African sovereign small language model and a serious benchmark for what is achievable on accessible compute.</p>
    <p style="color: #444; line-height: 1.75;"><strong>MzansiLM</strong> (UCT NLP group; <a href="https://arxiv.org/abs/2603.20732" target="_blank" rel="noopener">arXiv:2603.20732</a>, 21 March 2026; accepted at LREC 2026 in Mallorca). Anri Lombard (UCT master&#39;s researcher in computer science) led the work with Drs Francois Meyer and Jan Buys, alongside Simbarashe Mawere, Temi Aina, Ethan Wolff, Sbonelo Gumede, and Elan Novick. 125M-parameter decoder-only model trained from scratch alongside the accompanying <strong>MzansiText</strong> corpus. Covers all <em>eleven</em> official South African written languages: Sepedi, Sesotho, Setswana, siSwati, Tshivenda, Xitsonga, Afrikaans, English, isiNdebele, isiXhosa, and isiZulu. Reports 20.65 BLEU on isiXhosa data-to-text generation. This is the UCT contribution to the African sovereign-LM lineage and is exactly the kind of work this course&#39;s students may go on to do.</p>
  </div>

  <div class="technical-detail">
    <h4>&#128683; Adapted-from-Llama decoder models</h4>
    <ul class="styled-list" style="margin-top: 0;">
      <li><strong>AfroLlama_V1</strong> (Jacaranda Health, <a href="https://huggingface.co/Jacaranda/AfroLlama_V1" target="_blank" rel="noopener">HF model card</a>). 8B parameters, fine-tuned for Swahili, Xhosa, Zulu, Yoruba, Hausa, and English. Jacaranda&#39;s companion model <strong>UlizaLlama</strong> (7B, Llama-2-based, 321M Swahili tokens) was selected into the 2025 AI for Global Development Accelerator.</li>
      <li><strong>Lugha-Llama</strong> (Buzaaba, Wettig, Adelani &amp; Fellbaum, Princeton, <a href="https://arxiv.org/abs/2504.06536" target="_blank" rel="noopener">arXiv:2504.06536</a>, April 2025). Mixed-data adaptation of Llama for African languages. Reports state-of-the-art results on IrokoBench and a 10-point improvement on AfriQA.</li>
      <li><strong>Toucan</strong> (Elmadany, Adebara, Abdul-Mageed, UBC, <a href="https://arxiv.org/abs/2407.04796" target="_blank" rel="noopener">arXiv:2407.04796</a>, July 2024). Many-to-many translation for 150 African language pairs. Not technically Llama-based but sits in the same adapted-model family.</li>
    </ul>
  </div>

  <div class="technical-detail">
    <h4>&#128227; Named-language models</h4>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">A handful of African languages now have dedicated foundation-model resources. The Amharic ecosystem is the most developed.</p>
    <ul class="styled-list" style="margin-top: 0;">
      <li><strong>KinyaBERT</strong> (Nzeyimana &amp; Niyongabo Rubungo, <a href="https://arxiv.org/abs/2203.08459" target="_blank" rel="noopener">arXiv:2203.08459</a>, ACL 2022). Encoder model with explicit morphological analysis for Kinyarwanda.</li>
      <li><strong>Amharic-LLaMA / Amharic-LLaVA</strong> (Andersland, <a href="https://arxiv.org/abs/2403.06354" target="_blank" rel="noopener">arXiv:2403.06354</a>, March 2024). The first published Amharic-adapted LLaMA with multimodal capability.</li>
      <li><strong>Walia-LLM</strong> (<a href="https://arxiv.org/abs/2402.08015" target="_blank" rel="noopener">arXiv:2402.08015</a>, February 2024). Enhanced Amharic-adapted LLaMA.</li>
      <li><strong>SwahBERT</strong> (2022). Swahili encoder model.</li>
    </ul>
    <p style="color: #444; line-height: 1.75; margin-top: 12px;">The dataset substrate worth naming: <strong>WURA</strong> (Oladipo et al., EMNLP 2023) is a high-quality multilingual pre-training corpus covering 16 African languages, and underpins the AfriTeVa model family.</p>
  </div>

  <h2 class="section-title">&#127919; The African Benchmark Stack</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Benchmarks are how a field measures progress. The African benchmark stack has expanded substantially in 2024 and 2025, with several important 2026 additions. What follows is the verified inventory you can actually use to evaluate African-language work.</p>

  <div style="overflow-x: auto;">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Benchmark</th>
          <th>Coverage</th>
          <th>Venue / arXiv</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>AfroBench</strong></td>
          <td>64 languages, 15 tasks (NLU, generation, knowledge/QA, math), 22 datasets</td>
          <td>Ojo et al. ACL 2025 Findings; <a href="https://arxiv.org/abs/2311.07978" target="_blank" rel="noopener">arXiv:2311.07978</a></td>
        </tr>
        <tr>
          <td><strong>IrokoBench</strong></td>
          <td>17 typologically diverse languages; AfriXNLI (NLI), AfriMGSM (grade-school math), AfriMMLU (multi-choice knowledge)</td>
          <td>Adelani et al. NAACL 2025 main; <a href="https://arxiv.org/abs/2406.03368" target="_blank" rel="noopener">arXiv:2406.03368</a></td>
        </tr>
        <tr>
          <td><strong>AfriSenti</strong></td>
          <td>14 sentiment datasets, 14 African languages, >110,000 tweets</td>
          <td>Muhammad et al. EMNLP 2023 + SemEval-2023 Task 12; <a href="https://arxiv.org/abs/2302.08956" target="_blank" rel="noopener">arXiv:2302.08956</a></td>
        </tr>
        <tr>
          <td><strong>AfriHate</strong></td>
          <td>Hate-speech, 15 languages (Algerian/Moroccan Arabic, Amharic, Igbo, Kinyarwanda, Hausa, Nigerian Pidgin, Oromo, Somali, Swahili, Tigrinya, Twi, Xhosa, Yoruba, Zulu)</td>
          <td>Muhammad et al. NAACL 2025 long; <a href="https://arxiv.org/abs/2501.08284" target="_blank" rel="noopener">arXiv:2501.08284</a></td>
        </tr>
        <tr>
          <td><strong>AfriQA</strong></td>
          <td>Cross-lingual open-retrieval QA, 10 African languages, ~12,000 examples</td>
          <td>Ogundepo, Gwadabe et al. EMNLP 2023 Findings; <a href="https://arxiv.org/abs/2305.06897" target="_blank" rel="noopener">arXiv:2305.06897</a></td>
        </tr>
        <tr>
          <td><strong>AfriSpeech-200</strong></td>
          <td>200 hours Pan-African accented English ASR, 67,577 clips, 2,463 speakers, 120 accents, 13 countries; clinical + general</td>
          <td>Olatunji et al. TACL 2023, 11:1669&ndash;1685</td>
        </tr>
        <tr>
          <td><strong>African ASR systematic review</strong></td>
          <td>PRISMA review: 2,062 &rarr; 71 studies; 74 datasets, 111 languages, ~11,206 hours; &lt;15% reproducible</td>
          <td>Imam et al. October 2025; <a href="https://arxiv.org/abs/2510.01145" target="_blank" rel="noopener">arXiv:2510.01145</a></td>
        </tr>
        <tr>
          <td><strong>African ASR benchmarking</strong></td>
          <td>Whisper, XLS-R, MMS, W2v-BERT on 13 languages at 1&ndash;400 hour scales</td>
          <td>Nahabwe et al. November 2025; <a href="https://arxiv.org/abs/2512.10968" target="_blank" rel="noopener">arXiv:2512.10968</a></td>
        </tr>
        <tr>
          <td><strong>AfriMTEB / AfriE5</strong></td>
          <td>Text-embedding benchmark: 59 African languages, 14 tasks, 38 datasets. AfriE5 (contrastive-distilled adaptation) outperforms Gemini-Embeddings on this benchmark.</td>
          <td>Uemura, Zhang, Adelani EACL 2026 main; <a href="https://arxiv.org/abs/2510.23896" target="_blank" rel="noopener">arXiv:2510.23896</a></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="info-box">
    <h4>&#128640; The 2026 additions worth foregrounding</h4>
    <p>Four 2026 (and late-2025) benchmark releases are particularly worth knowing about, because they expand the stack into areas it did not previously cover.</p>
    <ul class="styled-list" style="margin-top: 8px;">
      <li><strong>Afri-MCQA</strong> (Multimodal Cultural QA, <a href="https://arxiv.org/abs/2601.05699" target="_blank" rel="noopener">arXiv:2601.05699</a>, January 2026). The freshest African QA/reasoning benchmark, and the first to take cultural context seriously as an evaluation axis. If you are building anything that involves cultural reasoning on African content, start here.</li>
      <li><strong>NaijaVoices</strong> (<a href="https://arxiv.org/abs/2505.20564" target="_blank" rel="noopener">arXiv:2505.20564</a>, AfricaNLP 2025). 1,867 hours of multi-speaker Hausa, Igbo, and Yoruba speech (precisely 1,838.54 hours across 5,455 unique speakers, 645,000 unique sentences) &mdash; one of the largest African ASR datasets to date, and built under Lanfrica&#39;s &ldquo;data farming&rdquo; ethos.</li>
      <li><strong>Yankari</strong> (AfricaNLP 2025). 30 million-token monolingual Yoruba corpus.</li>
      <li><strong>AfroCS-xs</strong>. The first dedicated <em>code-switched</em> agricultural dataset, covering Afrikaans, Sesotho, Yoruba, isiZulu, and English. Code-switching is the dominant register of African urban speech; benchmarks that take it seriously are overdue.</li>
    </ul>
  </div>

  <h2 class="section-title">&#9878;&#65039; Two Strategic Positions</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">There is a real and currently unresolved disagreement inside the African AI community about what the right strategic move is. The argument is worth understanding clearly because it shapes which kinds of project a postgraduate researcher might join.</p>

  <div class="card-grid">
    <div class="card">
      <h3>The sovereign / frontier-aspirant position</h3>
      <p>The argument: African AI sovereignty requires <em>African frontier-scale models</em>, trained on African data, owned by African institutions, hosted on African compute. Without that, the continent will remain technologically dependent regardless of how much application-layer work happens locally. The clearest current expression is Nigeria&#39;s <strong>N-ATLAS</strong>, a national open-source LLM built by <strong>Awarri Technologies</strong> (Silas Adekunle and Eniola Edun) in partnership with the Nigerian Federal Ministry of Communications, Innovation and Digital Economy and published by NCAIR. Funded with $3.5M seed from UNDP, UNESCO, Meta, Google, and Microsoft. Launched by Minister Bosun Tijani at UNGA80 sidelines on 25 September 2025. Now publicly available on Hugging Face as <a href="https://huggingface.co/NCAIR1/N-ATLaS" target="_blank" rel="noopener">NCAIR1/N-ATLaS</a>: 8B parameters, Llama-3-8B base, fine-tuned across English, Hausa, Igbo, and Yoruba; subject to a 1,000-user licence cap, with commercial use requiring explicit licensing from Awarri and the Federal Ministry. Cassava&#39;s compute work (11.4) and the Tanzania&ndash;Almawave Kiswahili partnership are adjacent expressions of the same strategic position.</p>
      <p style="color: #888; font-size: 0.95em; margin-top: 12px;">Status: operational. Shipped September 2025, weights public on Hugging Face under a capped non-commercial-by-default licence.</p>
    </div>
    <div class="card">
      <h3>The resource-efficient / pragmatic position</h3>
      <p>The argument made most explicitly by Pelonomi Moiloa at Lelapa AI: African sovereign AI capacity is best pursued by building <em>smaller, more efficient models</em> that the available infrastructure can actually support and that solve the problems African users actually have. The InkubaLM family, MzansiLM&#39;s 125M parameters covering all eleven SA languages, the Masakhane lineage&#39;s benchmark and dataset work, and Jacaranda&#39;s vertical-health deployment of UlizaLlama all sit in this strand. The argument is that engineering for the real constraints &mdash; compute, energy, end-user devices &mdash; is itself a sovereignty practice.</p>
      <p style="color: #888; font-size: 0.95em; margin-top: 12px;">Status: shipping, used by real African users, smaller in headline numbers but more operationally honest.</p>
    </div>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The pedagogical point of putting these two positions side by side is not to declare a winner. Both are sovereignty practices in different registers; both have honest arguments behind them; the right answer for a particular project depends on what the project is for. The useful exercise is to be able to read a piece of African-AI work and identify clearly which strand it sits in, because the success criteria for the two are quite different. A 125M-parameter community-licensed model that runs on a feature-phone-class device is a success in the resource-efficient register; it is a partial step in the frontier-aspirant register. A nation-state frontier-scale model that is announced but not yet running is a partial step in the sovereign register; it is mostly absent from the resource-efficient one.</p>

  <h2 class="section-title">&#128269; Where the Gaps Are</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The single most useful thing this sub-lesson can do for the postgraduate audience is identify, concretely, what is missing in the current African data-and-models landscape. Six gaps are particularly thesis-shaped: each one is a genuine research opening that could be pursued from a UCT or comparable position.</p>

  <ol class="step-list">
    <li><strong>No African-language LegalBench equivalent.</strong> Legal NLP benchmarks exist for English; the equivalent for any African language does not. Africa has substantial bodies of customary law, statutory law, and judicial decisions in many of its languages. A LegalBench-for-Swahili or LegalBench-for-isiXhosa would be a benchmark contribution and a step toward AI-supported access to law for people who do not work in English.</li>
    <li><strong>No African clinical QA benchmark grounded in local guidelines.</strong> MedQA exists; an African equivalent that takes local clinical guidelines, local epidemiology, and local pharmacological reality seriously does not. This is the kind of benchmark that would let African researchers <em>evaluate foreign frontier models against local clinical reality</em> before deploying them in healthcare settings.</li>
    <li><strong>No PRISMA-style reproducibility audit of African NLP.</strong> Imam et al.&#39;s 2025 ASR review is the closest equivalent, and found &lt;15% of African ASR studies reproducible. A wider study covering the full African NLP literature would surface the actual size of the reproducibility gap and would, by itself, be a publishable contribution.</li>
    <li><strong>No published Africa-specific critique-and-adaptation of CARE.</strong> A paper arguing what CARE would need to look like as a genuinely African framework rather than a wholesale Indigenous import is missing. The constructive work (Esethu) is there; the critical-theoretical companion is not.</li>
    <li><strong>No continent-level inventory of endangered-language ML resources.</strong> N|uu (Khoisan), Khwedam, and several Cushitic, Nilotic, and Khoisan languages are at risk; the inventory of which of them have any ML data at all does not exist. SADiLaR&#39;s University of Pretoria node and the Wits DSFSI lab hold parts of the picture; a unified continental inventory would let endangered-language documentation and AI work coordinate more effectively.</li>
    <li><strong>Operational uptake of community licensing remains low.</strong> Despite Esethu, despite Kaitiakitanga, despite CARE, most African datasets in 2024 and 2025 still ship under CC-BY or research-only licences. There is room for both empirical research on <em>why</em>, and for practical work helping projects move to community-grounded licences when it is appropriate.</li>
  </ol>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">If you are a postgraduate looking for a thesis topic in this part of the AI landscape, any of these gaps is a real opening &mdash; not in the sense that they are easy, but in the sense that the field will recognise the contribution.</p>

  <h2 class="section-title">&#127919; What This Means for Your Research</h2>

  <ul class="styled-list">
    <li><strong>Use the benchmarks.</strong> The African benchmark stack is real and broad enough to evaluate work in most of the major NLU and ASR areas. If your project involves African-language NLP and you are not evaluating against at least one of AfroBench / IrokoBench / AfriMTEB / Afri-MCQA / AfriHate / AfriSenti / AfriSpeech-200, you are working blind.</li>
    <li><strong>Use the models that exist.</strong> For inference and adaptation work on the languages they cover, InkubaLM, MzansiLM, AfroXLMR, Serengeti, and the named-language models are usable starting points. The frontier-aspirant N-ATLAS-style projects are not yet downloadable; the resource-efficient ones are.</li>
    <li><strong>Consider community licensing when releasing data.</strong> If you collect or curate a dataset, especially one with significant cultural or linguistic content, look at Esethu and Kaitiakitanga before defaulting to CC-BY. The community-licensing track is genuinely more aligned with the African sovereignty conversation; defaulting away from it without considering it is a missed opportunity.</li>
    <li><strong>Pick the gaps deliberately.</strong> The six gaps above are not the only ones, but they are concrete and verifiable. If you are starting a project, choosing one of them by intention is more likely to produce a publishable contribution than choosing a topic only because foundation-model work is currently fashionable.</li>
    <li><strong>Resource-efficient is a sovereignty practice.</strong> The Lelapa argument generalises: matching your work to the compute and data you actually have access to, rather than to the headline numbers of foreign labs, is the operationally honest version of the sovereignty position covered in 11.4.</li>
  </ul>

  <h2 class="section-title">&#9999;&#65039; A Short Exercise</h2>

  <ol class="step-list">
    <li><strong>Pick a language and a domain</strong> relevant to your current or planned research project. The domain might be medicine, agriculture, law, climate science, education, the humanities, or another.</li>
    <li><strong>Check what benchmarks and datasets exist</strong> for that language &times; domain combination. Use the table above; check Lanfrica; check the AfricaNLP 2025 proceedings.</li>
    <li><strong>Identify what is missing.</strong> Is there a benchmark? Is there a dataset of the right size and quality? Is there a model that handles the language?</li>
    <li><strong>Write a one-paragraph proposal</strong> for what you would build first if you were going to fill that gap. Be honest about scope &mdash; would this be a year of work, a thesis, a community collaboration?</li>
    <li><strong>Bring it to class.</strong> We will pool the proposals across the cohort and look at which gaps the group together could imaginably address.</li>
  </ol>

  <h2 class="section-title">&#128218; Sources &amp; Further Reading</h2>

  <div class="resource-placeholder">
    <h4>&#128196; Sovereignty &amp; data governance</h4>
    <p><strong>Carroll, S. R. et al. (2020).</strong> The CARE Principles for Indigenous Data Governance. <em>Data Science Journal</em> 19(1): 43. <a href="https://datascience.codata.org/articles/10.5334/dsj-2020-043" target="_blank" rel="noopener">DOI 10.5334/dsj-2020-043</a>.</p>
    <p><strong>Jones, K. &amp; Mahelona, K. (2022/2023).</strong> <em>Data Sovereignty and the Kaitiakitanga License</em>. Te Hiku Media. <a href="https://tehiku.nz/te-hiku-tech/te-hiku-dev-korero/25141/data-sovereignty-and-the-kaitiakitanga-license" target="_blank" rel="noopener">tehiku.nz</a>.</p>
    <p><strong>Rajab, J. et al. (2025).</strong> The Esethu Framework. <a href="https://arxiv.org/abs/2502.15916" target="_blank" rel="noopener">arXiv:2502.15916</a>; ACL 2025.</p>
    <p><strong>African Union (2022).</strong> AU Data Policy Framework. <a href="https://au.int/" target="_blank" rel="noopener">au.int</a>.</p>
    <p><strong>African Union (2024).</strong> Continental Artificial Intelligence Strategy. <a href="https://au.int/en/documents/20240809/continental-artificial-intelligence-strategy" target="_blank" rel="noopener">au.int</a>.</p>
    <p><strong>First Nations Information Governance Centre.</strong> OCAP Principles. <a href="https://fnigc.ca/ocap-training/" target="_blank" rel="noopener">fnigc.ca</a>.</p>
  </div>

  <div class="resource-placeholder">
    <h4>&#128196; Models &amp; community infrastructure</h4>
    <p><strong>Alabi, J. O., Hedderich, M. A., Adelani, D. I. &amp; Klakow, D. (2025).</strong> Charting the Landscape of African NLP: Mapping Progress and Shaping the Road Ahead. EMNLP 2025 main, pp. 27807&ndash;27841. <a href="https://arxiv.org/abs/2505.21315" target="_blank" rel="noopener">arXiv:2505.21315</a>.</p>
    <p><strong>Belay, T. D., Azime, I. A., Adelani, D. I. et al. (2025).</strong> The Rise of AfricaNLP: A Survey of Contributions, Contributors, Community Impact, and Bibliometric Analysis. <a href="https://arxiv.org/abs/2509.25477" target="_blank" rel="noopener">arXiv:2509.25477</a>.</p>
    <p><strong>Hussen, K. Y., Sewunetie, W. T., Ayele, A. A., Imam, S. H., Muhammad, S. H. &amp; Yimam, S. M. (2025).</strong> The State of Large Language Models for African Languages: Progress and Challenges. <a href="https://arxiv.org/abs/2506.02280" target="_blank" rel="noopener">arXiv:2506.02280</a>.</p>
    <p><strong>Tonja, A. L. et al. (2024).</strong> InkubaLM: A small language model for low-resource African languages. <a href="https://arxiv.org/abs/2408.17024" target="_blank" rel="noopener">arXiv:2408.17024</a>. Model: <a href="https://huggingface.co/lelapa/InkubaLM-0.4B" target="_blank" rel="noopener">huggingface.co/lelapa/InkubaLM-0.4B</a>.</p>
    <p><strong>Lombard, A. et al. (2026).</strong> MzansiText and MzansiLM: An Open Corpus and Decoder-Only Language Model for South African Languages. <a href="https://arxiv.org/abs/2603.20732" target="_blank" rel="noopener">arXiv:2603.20732</a>; LREC 2026.</p>
    <p><strong>Buzaaba, H., Wettig, A., Adelani, D. I. &amp; Fellbaum, C. (2025).</strong> Lugha-Llama. <a href="https://arxiv.org/abs/2504.06536" target="_blank" rel="noopener">arXiv:2504.06536</a>.</p>
    <p><strong>Elmadany, A., Adebara, I. &amp; Abdul-Mageed, M. (2024).</strong> Toucan. <a href="https://arxiv.org/abs/2407.04796" target="_blank" rel="noopener">arXiv:2407.04796</a>.</p>
    <p><strong>Adebara, I., Elmadany, A., Abdul-Mageed, M. &amp; Inciarte, A. A. (2023).</strong> SERENGETI. <a href="https://arxiv.org/abs/2212.10785" target="_blank" rel="noopener">arXiv:2212.10785</a>; Findings of ACL 2023.</p>
    <p><strong>AfricaNLP 2025 proceedings.</strong> Lignos, C., Abdulmumin, I. &amp; Adelani, D. I. (eds.). <a href="https://aclanthology.org/2025.africanlp-1.0/" target="_blank" rel="noopener">aclanthology.org</a>.</p>
    <p><strong>Masakhane.</strong> <a href="https://www.masakhane.io/" target="_blank" rel="noopener">masakhane.io</a>; <a href="https://huggingface.co/masakhane" target="_blank" rel="noopener">huggingface.co/masakhane</a>.</p>
    <p><strong>Lanfrica.</strong> <a href="https://lanfrica.com" target="_blank" rel="noopener">lanfrica.com</a>.</p>
    <p><strong>Deep Learning Indaba 2025 (Kigali).</strong> <a href="https://deeplearningindaba.com/2025/" target="_blank" rel="noopener">deeplearningindaba.com/2025</a>.</p>
  </div>

  <div class="resource-placeholder">
    <h4>&#128196; Benchmarks</h4>
    <p><strong>AfroBench</strong> &mdash; Ojo et al., ACL 2025 Findings. <a href="https://arxiv.org/abs/2311.07978" target="_blank" rel="noopener">arXiv:2311.07978</a>.</p>
    <p><strong>IrokoBench</strong> &mdash; Adelani et al., NAACL 2025 main. <a href="https://arxiv.org/abs/2406.03368" target="_blank" rel="noopener">arXiv:2406.03368</a>.</p>
    <p><strong>AfriSenti</strong> &mdash; Muhammad et al., EMNLP 2023. <a href="https://arxiv.org/abs/2302.08956" target="_blank" rel="noopener">arXiv:2302.08956</a>.</p>
    <p><strong>AfriHate</strong> &mdash; Muhammad et al., NAACL 2025 long. <a href="https://arxiv.org/abs/2501.08284" target="_blank" rel="noopener">arXiv:2501.08284</a>.</p>
    <p><strong>AfriQA</strong> &mdash; Ogundepo, Gwadabe et al., EMNLP 2023 Findings. <a href="https://arxiv.org/abs/2305.06897" target="_blank" rel="noopener">arXiv:2305.06897</a>.</p>
    <p><strong>AfriSpeech-200</strong> &mdash; Olatunji et al., TACL 2023.</p>
    <p><strong>African ASR systematic review</strong> &mdash; Imam et al. (October 2025). <a href="https://arxiv.org/abs/2510.01145" target="_blank" rel="noopener">arXiv:2510.01145</a>.</p>
    <p><strong>African ASR benchmarking</strong> &mdash; Nahabwe et al. (November 2025). <a href="https://arxiv.org/abs/2512.10968" target="_blank" rel="noopener">arXiv:2512.10968</a>.</p>
    <p><strong>AfriMTEB &amp; AfriE5</strong> &mdash; Uemura, Zhang &amp; Adelani, EACL 2026. <a href="https://arxiv.org/abs/2510.23896" target="_blank" rel="noopener">arXiv:2510.23896</a>.</p>
    <p><strong>Afri-MCQA</strong> &mdash; Multimodal Cultural QA, January 2026. <a href="https://arxiv.org/abs/2601.05699" target="_blank" rel="noopener">arXiv:2601.05699</a>.</p>
    <p><strong>NaijaVoices, Yankari, AfroCS-xs</strong> &mdash; AfricaNLP 2025 proceedings (see ACL Anthology link above).</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 20px; margin-bottom: 15px;"><strong>Coming up in 11.6:</strong> we turn from data and models to the remaining two layers of the stack &mdash; policy and talent. The African Union Continental AI Strategy in its operational detail, the national strategies of South Africa / Kenya / Rwanda / Nigeria / Egypt (and the peer-reviewed comparative analysis in Yilma &amp; Wodajo&#39;s <em>Science and Public Policy</em> special section), and the institutional landscape of Deep Learning Indaba, AIMS, ARIN, and Lelapa as the talent pipeline. We close 11.6 with the question that will set up 11.7 (synthesis): given everything we now know about African AI capacity, what is the most useful thing a postgraduate in this room can actually do?</p>
"""


# ---------------------------------------------------------------------------
# Sub-Lesson 11.6 — Policy, Institutions, and Talent
# ---------------------------------------------------------------------------

SL6_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>The last sub-lesson of the African half of Week 11 looks at the layer of the picture where the gap between announcement and reality is widest: <em>policy, institutions, and talent</em>. The peer-reviewed spine for this conversation is Yilma &amp; Wodajo&#39;s 2026 <em>Strategy as Governance</em> (<em>Science and Public Policy</em> 53(2), 236&ndash;244), which argues that African AI governance has so far been performed primarily through strategy documents rather than through legislation, institutions, or enforcement &mdash; and that this matters more than it might look at first glance.</p>
    <p>We test the claim against the operational state of things in May 2026. A close reading of the strategy landscape (with one extraordinary recent South African case at its centre); the funding flows that are actually moving money for African AI work; the institutional infrastructure that trains and retains researchers (and where it is leaking); and an honest account of where the gaps are. We close the African half of the week on the question that opens 11.7: <em>given everything in Weeks 1&ndash;11, what is the most useful thing a postgraduate in this room can actually do?</em></p>
  </div>

  <h2 class="section-title">&#128217; The Strategy Landscape, Calibrated</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">By July 2025, sixteen African countries had published national AI strategies, with several more in draft. The continental layer is anchored by the AU Continental AI Strategy (July 2024) and the AUDA-NEPAD Continental AI Roadmap (February 2025). Reading these as a single landscape rather than as separate national documents, the most useful empirical observation is that the policy-to-legislation pipeline is almost entirely broken. <em>Only Ethiopia has drafted AI legislation</em>; that draft has not been enacted. South Africa&#39;s policy was withdrawn before it could take effect (see the next section). Every other major African economy regulates AI use, where it regulates it at all, through adjacent data-protection statutes inherited from the GDPR family.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">This is the operational form of the Yilma &amp; Wodajo critique. The argument is not that the strategies are insincere or empty &mdash; many are detailed, ambitious, and explicitly grounded in African political-economic positions &mdash; but that strategy is not the same thing as governance. Governance requires binding instruments. The strategies, with extremely limited exceptions, do not yet have any.</p>

  <div style="overflow-x: auto;">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Country</th>
          <th>Status (May 2026)</th>
          <th>Notes</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>South Africa</strong></td>
          <td>Draft policy <em>withdrawn</em> April 2026</td>
          <td>See full case study in the next section.</td>
        </tr>
        <tr>
          <td><strong>Nigeria</strong></td>
          <td>Strategy revised Sept 2025; N-ATLAS shipped</td>
          <td>Revised National AI Strategy 19 September 2025. N-ATLAS launched by Minister Bosun Tijani at UNGA80, 25 September 2025; public on Hugging Face (see 11.5).</td>
        </tr>
        <tr>
          <td><strong>Rwanda</strong></td>
          <td>Policy operational; implementation partial</td>
          <td>Cabinet-approved 20 April 2023. Costed at US$76.5M; Responsible AI Office in MINICT. C4IR Rwanda (WEF affiliate) operationally active. Rwanda AI Scaling Hub with Gates Foundation (US$7.5M, MoU April 2025).</td>
        </tr>
        <tr>
          <td><strong>Kenya</strong></td>
          <td>Strategy launched 27 March 2025; early implementation</td>
          <td>Six pillars; no separate AI Act; governance leans on the 2019 Data Protection Act.</td>
        </tr>
        <tr>
          <td><strong>Egypt</strong></td>
          <td>2nd-edition strategy launched January 2025</td>
          <td>KPIs: US$42.7bn annual AI value by 2030, 30,000 AI professionals, 250+ AI companies, 6,000 publications/yr. KPI dashboard not publicly visible.</td>
        </tr>
        <tr>
          <td><strong>Ethiopia</strong></td>
          <td>Policy approved June 2024; institute active; draft AI Proclamation pre-legislative</td>
          <td>Ethiopian AI Institute (EAII, established by Regulation 510/2022) is the implementing body. The draft AI Development and Regulation Proclamation has not been enacted.</td>
        </tr>
        <tr>
          <td><strong>Morocco</strong></td>
          <td>No standalone AI Strategy; Digital X.0 Framework Law pre-parliamentary</td>
          <td>&ldquo;Morocco AI 2030&rdquo; roadmap and a National AI Hub announced January 2026 within the Digital Morocco 2030 envelope.</td>
        </tr>
        <tr>
          <td><strong>Senegal, Ghana, Benin, Algeria, Mauritius, C&ocirc;te d&#39;Ivoire</strong></td>
          <td>National strategies adopted 2018&ndash;2024</td>
          <td>Mauritius (2018) was the first African national AI strategy; the others followed between 2022 and 2024.</td>
        </tr>
        <tr>
          <td><strong>Tanzania, Mozambique</strong></td>
          <td>Drafts in consultation</td>
          <td>Mozambique&#39;s INTIC public consultation was open until 4 June 2026.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 20px; margin-bottom: 15px;">A consolidating analytical resource: Munga &amp; Quansah&#39;s September 2025 Carnegie piece <em>Understanding Africa&#39;s AI Governance Landscape</em> compares 15 national + 2 continental strategies and offers the cleanest single map of the policy stack. Engida Abdella &amp; Alayande&#39;s April 2025 piece for the Global Center on AI Governance, <em>African Countries Are Racing to Create AI Strategies &mdash; But Are They Putting the Cart Before the Horse?</em>, provides the calibrated counterweight: many strategies skip foundational infrastructure questions, lack realistic implementation timelines, and rely on benefit-sharing rhetoric without operational mechanisms. CIPESA&#39;s 2025 SIFA report (<em>Navigating the Implications of AI on Digital Democracy in Africa</em>) draws on empirical research across 14 countries and is the strongest single empirical complement to the analytical work.</p>

  <h2 class="section-title">&#127479;&#127462; The South African AI Policy Withdrawal</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The most consequential recent event in African AI governance happened in South Africa in April 2026, and it deserves treatment in detail because it is simultaneously a perfect example of the Yilma &amp; Wodajo critique and a worked instance of the policy-and-practice problem we covered in 11.3. It also &mdash; for the students reading this from a UCT vantage point &mdash; happened in your own jurisdiction.</p>

  <div class="case-study">
    <h4>&#128221; What happened</h4>
    <p>The Department of Communications and Digital Technologies (DCDT) had been working on a national AI policy since at least August 2024. After a lengthy consultative process, the resulting Draft National AI Policy was Cabinet-approved on 25 March / 1 April 2026 and gazetted on 10 April 2026 (Gazette 54477) for public comment.</p>
    <p>Within days, <em>News24</em> began checking the academic citations in the draft and found that at least <strong>six of the sixty-seven academic references in the document could not be located in any database</strong>. The fabricated citations were attributed to the <em>South African Journal of Philosophy</em>, <em>AI &amp; Society</em>, and the <em>Journal of Ethics and Social Philosophy</em>; the editors of all three journals independently confirmed to <em>News24</em> that the articles credited to them had never been published. The most plausible explanation, by some distance, was that the citations had been produced by a generative AI system used somewhere in the drafting workflow and had not been independently verified before publication.</p>
    <p>On <strong>27 April 2026</strong> &mdash; less than three weeks after publication &mdash; Minister of Communications and Digital Technologies Solly Malatsi withdrew the draft policy. The DCDT subsequently announced that <strong>the final draft will be published in January 2027</strong>, and the Minister established a <strong>seven-member independent panel of experts</strong> to review the original draft, recommend revisions, and replace flawed citations. The Year 1 implementation timeline (2025&ndash;26) that the original policy committed to has consequently slipped by roughly a year.</p>
    <p style="color: #888; font-size: 0.9em;">Sources: Original gazette PDF on <a href="https://www.gov.za/sites/default/files/gcis_document/202604/54477gen3880.pdf" target="_blank" rel="noopener">gov.za</a>. Coverage of the withdrawal: <a href="https://www.dlapiper.com/en-us/insights/publications/2026/05/withdrawal-of-south-africa-draft-ai-policy" target="_blank" rel="noopener">DLA Piper analysis</a>.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">There are three reasons this case is worth a careful read.</p>

  <ul class="styled-list">
    <li><strong>It is the exact failure mode Week 11.3 covered, at policy-document scale.</strong> The He &amp; Bu finding was that policies don&#39;t curb the surge in AI use because researchers don&#39;t disclose. Here, an entire government ministry submitted an AI-drafted policy document without disclosure or citation verification, and the failure was caught not by the ministry&#39;s internal processes but by a journalist with thirty minutes to spare. The policy that was meant to govern AI use in South Africa was itself an instance of the problem it was meant to address.</li>
    <li><strong>It is the strongest available South African instance of the Yilma &amp; Wodajo critique.</strong> The argument is that strategy is not governance. Here, even the strategy document collapsed before it could attempt governance. The country is not currently between strategies; it is in a documented policy vacuum, with the previous draft withdrawn and no successor published.</li>
    <li><strong>It is unusually concrete material for a postgraduate course.</strong> The full gazetted PDF is publicly available. The withdrawn citations are documented. The methodology that produced the problem is the methodology this entire course is asking you to be cautious about. If you want a single piece of evidence for why the calibrated-reading habit matters, this case is it.</li>
  </ul>

  <div class="warning-box">
    <h4>&#128221; The honest comparison to Ethiopia</h4>
    <p>Ethiopia is the only African state with a draft AI legislative instrument under serious consideration (the AI Development and Regulation Proclamation, drafted by the Ethiopian AI Institute). It is not enacted, but it exists. South Africa, between April 2026 and at least the autumn of 2026, will have no comparable document at all. Whatever your view of the merits of strategy-as-governance, the empirical situation as of May 2026 is that the largest economy on the continent currently has no AI policy framework at all, while the second-largest has a draft legislative instrument under review. That ordering is not the one the policy-positioning rhetoric would lead you to expect.</p>
  </div>

  <h2 class="section-title">&#127963;&#65039; Continental Bodies, and What They&#39;ve Actually Done</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Three pan-African or African-adjacent bodies are worth knowing about, and one obvious confusion to head off at the outset.</p>

  <div class="card-grid">
    <div class="card">
      <h3>The AU Continental AI Strategy and AUDA-NEPAD Roadmap</h3>
      <p>The strategy was endorsed by the AU Executive Council in Accra in July 2024 (covered in 11.5). The AUDA-NEPAD Continental AI Roadmap, released February 2025 on the sidelines of the AU Summit, is the operational complement: it proposes a <strong>US$100M AU AI Grant</strong> (with a stated 70%-to-startups / 30%-to-research split) and a <strong>US$200M AU AI Investment</strong> mechanism, plus an AU AI Challenge awarding individual prizes between US$100,000 and US$2M to startups and academic institutions. <em>Neither funding mechanism has been capitalised on the public record.</em></p>
    </div>
    <div class="card">
      <h3>The Smart Africa Africa AI Council</h3>
      <p>Inaugurated by the Smart Africa Board in Conakry, Guinea, on <strong>17 November 2025</strong>. Fifteen members: seven ICT ministers (Sid Ali Zerrouki, Algeria; Boukar Michel, Chad; William Kabogo, Kenya; Bosun Tijani, Nigeria; Paula Ingabire, Rwanda; Cina Lawson, Togo; Tatenda Mavetera, Zimbabwe) and eight independents (Paulin Basinga, Gates Foundation; Karim Beguir, InstaDeep; Yasser Shaker, Orange Middle East &amp; Africa; <strong>Chenai Chair, Masakhane African Languages Hub</strong>; Akua Gyekye, Microsoft; <strong>Vukosi Marivate, University of Pretoria / Lelapa AI</strong>; Walid Naffati, Tunisie Haut D&eacute;bit; Alex Okosi, Google). Six workstreams: Infrastructure, Data, Market, Talent, Investment, Governance. As of May 2026: <em>just constituted; no published deliverables yet.</em></p>
    </div>
    <div class="card">
      <h3>The (still-proposed) African AI Scientific Panel</h3>
      <p>Endorsed in the Africa Declaration on AI at the Global AI Summit on Africa in April 2025. As of May 2026 it has <em>not been constituted</em> with a named, public membership. The closest currently operating body with overlapping remit is Smart Africa&#39;s Africa AI Council (above), but the two are not formally the same and should not be elided.</p>
    </div>
    <div class="card">
      <h3>The UN Independent International Scientific Panel on AI</h3>
      <p>Seated <strong>12 February 2026</strong> with 40 global members. The most prominent African member is <strong>Prof. Vukosi Marivate</strong> (University of Pretoria), already named in 11.4. This is a UN body, not an African one &mdash; but worth surfacing because it is the international scientific body where African expertise is currently most concretely represented, and because it is where the AU&#39;s own announced Scientific Panel <em>has not yet caught up</em>.</p>
    </div>
  </div>

  <div class="warning-box">
    <h4>&#9888;&#65039; The &ldquo;US$60 billion Africa AI Fund&rdquo; question</h4>
    <p>At the Kigali Global AI Summit on Africa in April 2025, a <em>US$60 billion Africa AI Fund</em> was announced as a pledge envelope. As of May 2026 there is no binding funding formula, no public timetable for disbursement, no announced audit mechanism, and no third-party verification of any disbursement to date. Independent reporting (Rest of World, Impact Newswire) treats it as a pledge rather than a fund. When you read continental funding figures for African AI, distinguish carefully between announced envelopes and capitalised facilities; the gap between them, as of May 2026, is essentially the gap between US$60 billion and zero.</p>
  </div>

  <h2 class="section-title">&#128176; Who Is Actually Paying for African AI?</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The honest answer in May 2026 is: <em>Big Tech capex and Northern foundations</em>. The sovereign and continental instruments are largely announced; the operational funding flows are largely commercial. This is the central empirical observation underpinning everything in the second half of this sub-lesson.</p>

  <div class="technical-detail">
    <h4>&#128202; Verified funding flows for African AI work</h4>
    <ul class="styled-list" style="margin-top: 0;">
      <li><strong>Microsoft &mdash;</strong> US$330M South Africa cloud/AI capex by end-2027; 1M-each AI skilling targets announced for South Africa, Kenya, and Nigeria.</li>
      <li><strong>Google.org &mdash;</strong> US$37M cumulative Africa AI package announced on 24 July 2025 in Accra: US$25M to the AI Collaborative Food Security initiative, <strong>US$3M to the Masakhane African Languages AI Hub</strong>, US$1M each to <strong>AfriDSAI (University of Pretoria)</strong> and the <strong>Wits MIND Institute</strong> for graduate-student and postdoctoral research, and US$7M to Grow with Google for AI digital-skills training across Ghana, Kenya, Nigeria, and South Africa. A separate US$2.25M Google.org grant to UNECA, UN DESA, and PARIS21 for public-data infrastructure was announced on 18 November 2025.</li>
      <li><strong>OpenAI &times; Gates Foundation &mdash;</strong> <em>Horizon 1000</em>, announced 21 January 2026: US$50M in funding, technology, and technical support to reach 1,000 primary-healthcare clinics by 2028. Pilot in Rwanda first, then Kenya, South Africa, and Nigeria.</li>
      <li><strong>IDRC AI4D Africa &mdash;</strong> original CAD$20M programme (IDRC + Sida) succeeded in 2024 by <em>Responsible AI, Empowering People</em> with FCDO, now operating at over CAD$100M across Africa and Asia. This is what underwrites the UCT African Compute Initiative.</li>
      <li><strong>Lacuna Fund &mdash;</strong> cumulative ~US$7.7M across 42 projects, more than 75 ML datasets produced. <em>In July 2025, Lacuna handed management to African and Latin-American partners</em>: ACTS (Kenya), University of Pretoria DSFSI, Masakhane, and CENIA. This is one of the cleanest examples of a Northern-funded African-AI vehicle being transitioned into African leadership.</li>
      <li><strong>Mozilla Foundation Africa Mradi &mdash;</strong> small grants in the US$5&ndash;10k range; Responsible AI Challenge expanding into South African schools in 2025.</li>
      <li><strong>Patrick J. McGovern Foundation &mdash;</strong> US$75.8M committed globally in 2025, with African line items including iCog-ACC (Ethiopia), HELINA FHIR Africa, and TIP Global Health (East Africa).</li>
    </ul>
  </div>

  <div class="highlight-box">
    <h3>&#128161; <span style="color: #ffffff;">The framing for the funding picture</span></h3>
    <p>The single most honest sentence about African AI funding in May 2026 is this: African AI capacity is currently being underwritten by Big Tech capital expenditure (Microsoft, Google, OpenAI / Gates) and Northern public-funder programmes (IDRC, FCDO via AI4D), not by sovereign or continental instruments. This is the Yilma &amp; Wodajo critique landing at the material level: the strategy-and-governance architecture announces intent; the cheques are signed by the firms and foundations whose dependencies the strategy is supposed to manage.</p>
    <p style="margin-top: 15px;">There are very good African-led organisations doing important work with these funds &mdash; Masakhane, Lelapa, AfriDSAI, the UCT ACI, ACTS, the Lacuna successor partnership &mdash; and noting where the money comes from is not a criticism of any of them. It is the honest empirical picture against which the policy positions in the rest of this sub-lesson should be read.</p>
  </div>

  <h2 class="section-title">&#127979; The Institutional Landscape</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Beneath the policy layer, the institutional infrastructure that trains and retains African AI researchers is genuinely substantial. It is also concentrated, and where it isn&#39;t concentrated the gap is large. Six institutions or programmes do the disproportionate share of the work.</p>

  <div class="card-grid">
    <div class="card">
      <h3>Deep Learning Indaba</h3>
      <p>Founded 2017 by Shakir Mohamed (Google DeepMind), Stephan Gouws (Google Brain), and Vukosi Marivate (then CSIR, now UP). The continent&#39;s most important annual AI gathering. 2025 in Kigali (17&ndash;22 August): <strong>1,294 participants, 40% women, 390 travel grants, 297 posters, 19 papers, 18 startups</strong> showcased. DLI 2026 announced for Nigeria. The IndabaX regional spin-offs ran in roughly 47 African countries in 2024.</p>
      <p style="color: #888; font-size: 0.9em;"><a href="https://deeplearningindaba.com/2025/" target="_blank" rel="noopener">deeplearningindaba.com/2025</a></p>
    </div>
    <div class="card">
      <h3>AIMS &amp; AMMI</h3>
      <p>The African Institute for Mathematical Sciences (AIMS) Next Einstein Initiative runs six centres: South Africa (2003), Senegal (2011), Ghana (2012), Cameroon (2013), Tanzania (2014), and Rwanda (2016). AIMS South Africa runs an AI-for-Science Master&#39;s. The African Master&#39;s in Machine Intelligence (AMMI) at AIMS Senegal, founded 2018 by <strong>Moustapha Cissé</strong> under Google sponsorship, remains the most-cited African AI training programme. Cissé left Google in 2022/23 to found <strong>KERA Health</strong> in Senegal, which closed a US$10M IFC investment in June 2025; AMMI continues at AIMS Senegal under different leadership.</p>
      <p style="color: #888; font-size: 0.9em;"><a href="https://nexteinstein.org/" target="_blank" rel="noopener">nexteinstein.org</a> &middot; <a href="https://aimsammi.org/" target="_blank" rel="noopener">aimsammi.org</a></p>
    </div>
    <div class="card">
      <h3>The substantive PhD quadrilateral</h3>
      <p>For postgraduate AI research on the continent in May 2026, the clearest concentration of substantive activity sits in four South African institutions: <strong>Wits</strong> (the MIND Institute and the RAIL lab), <strong>University of Pretoria</strong> (AfriDSAI, launched 2024 out of DSFSI; recipient of a US$1M Google donation in August 2025), <strong>UCT</strong> (the AI Initiative and the forthcoming ACI), and <strong>AIMS South Africa</strong> (the AI-for-Science Master&#39;s as a feeder to PhD). Outside this quadrilateral, supervision is highly individual-dependent, and you should vet the named supervisor rather than the institution.</p>
    </div>
    <div class="card">
      <h3>ARIN, Lelapa, Zindi, Black in AI</h3>
      <p><strong>ARIN</strong> (Africa Research and Impact Network): 200+ researchers, focal points in 36 African countries, broad sustainability remit with an AI workstream operationalised through the 2025 AI for Climate Resilience Fellowship. <strong>Lelapa AI</strong>: Pelonomi Moiloa (CEO), Jade Abbott (co-founder), Vukosi Marivate (co-founder); the operational arm of the resource-efficient African sovereign-AI position. <strong>Zindi</strong> (Nairobi): 92,000+ registered data practitioners, 460+ challenges run, ~US$1M cumulative prize pool. <strong>Black in AI</strong>: founded 2017 by Timnit Gebru and Rediet Abebe; Africa-specific work largely channelled through Gebru&#39;s DAIR (founded December 2021).</p>
    </div>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">A note on national AI institutes. <em>NCAIR</em> (Nigeria, commissioned November 2020) is the most-cited national institute, though as we noted in 11.4 it does not have substantial dedicated AI compute. The <em>Ethiopian AI Institute</em> (EAII, inaugurated November 2025 under Director-General Dr Worku Gachena) is the implementing body for the National AI Policy and is the strongest example of a national institute moving toward operational delivery. <em>C4IR Rwanda</em> is operational and co-designed Rwanda&#39;s AI policy; the Rwanda AI Scaling Hub (with Gates Foundation, US$7.5M MoU April 2025) sits there.</p>

  <h2 class="section-title">&#128395;&#65039; The Talent &amp; Brain-Drain Question</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The talent pipeline is the layer of the African AI picture where the data are weakest and the rhetorical claims are strongest. The honest position is that no rigorous AI-specific quantitative study of the African brain-drain problem exists yet. What exists is general migration data (Africa loses around US$2 billion per year in skilled migration; UK granted 78,000+ work visas to Nigerians by September 2023) which does not disaggregate AI researchers from the broader skilled-worker population. When you see specific figures for &ldquo;African AI talent loss&rdquo;, treat them with the same calibration the rest of this week has been asking for.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">What we can say more confidently:</p>

  <ul class="styled-list">
    <li><strong>The pipeline is top-heavy.</strong> Indaba and AMMI feed a substantial pool of MSc-level talent into the system. The PhD bottleneck is where the system leaks hardest &mdash; both because African PhD positions in AI are scarce and because the relative value of doing a PhD at, say, MIT or Mila is large for the individual researcher even when the African opportunity cost is also large.</li>
    <li><strong>Diaspora is the unstated default.</strong> The Africa Declaration on AI explicitly bundles &ldquo;Africa and diaspora&rdquo; in its proposed AI Scientific Panel composition. The 2025 Qhala / CMU / C4IR AI Research Colloquium drew 100+ researchers &ldquo;from continent and diaspora&rdquo;. The proportional split between Africans on the continent and Africans in diaspora is not publicly quantified, but the rhetorical and policy framing treats them as a single research community.</li>
    <li><strong>Some retention levers are working.</strong> Sovereign compute access (the UCT ACI, the Rwanda AI Scaling Hub) is explicitly framed as anti-brain-drain. Named chairs (Marivate&#39;s ABSA Chair of Data Science at UP), substantial corporate grants (Google PhD Fellowships at Wits, the US$1M to AfriDSAI), and partnerships with industry (Lelapa &times; Microsoft) all provide structural alternatives to leaving. Salary parity with US or UK industry positions is impossible; competitive intellectual conditions are not.</li>
    <li><strong>Some notable returns happen.</strong> Moustapha Cissé returned to Senegal to start KERA Health. Vukosi Marivate did a US PhD at Rutgers and returned to UP. Raesetje Sefala, DAIR&#39;s first fellow, is based in Johannesburg. These are not statistically significant; they are existence-proof signals that the flow is not one-way.</li>
  </ul>

  <h2 class="section-title">&#128269; Where the Gaps Are</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Five gaps stand out from the policy-and-institutions picture. Some are obvious. Others are easy to miss precisely because they map onto where the existing infrastructure is.</p>

  <ol class="step-list">
    <li><strong>Geographic concentration.</strong> The substantive PhD quadrilateral is in <em>South Africa</em>. The strongest national-institute work is in Ethiopia, Nigeria, and Rwanda. Beyond this small set, dedicated AI research infrastructure is sparse to absent. <em>Francophone West Africa outside Senegal and Rwanda, Central Africa (DRC, CAR, Chad), the Horn of Africa outside Ethiopia, and Lusophone Africa (Angola, Mozambique)</em> have near-zero structural AI research capacity as of May 2026.</li>
    <li><strong>The policy-to-legislation gap.</strong> Already noted: only Ethiopia has draft AI legislation; only one African economy is actively legislating; the rest is strategy. If you are interested in AI law and policy as a research area, this is a wide-open field.</li>
    <li><strong>Operational continental funding.</strong> The AU AI Grant (US$100M) and Investment (US$200M) mechanisms are uncapitalised. The Africa AI Fund (US$60bn) is a pledge envelope. The IDRC, Lacuna, and Google.org flows are all operationally important but are not <em>sovereign</em> in any of the senses 11.4 set out.</li>
    <li><strong>Audited KPI tracking.</strong> Strategies announce headline targets (Egypt: 30,000 AI professionals by 2030; Rwanda: US$76.5M policy implementation; Nigeria: 70% AI literacy in 16&ndash;35-year-olds by 2030). Publicly auditable tracking dashboards against these targets are largely absent. This is true across the continent, not just for African countries; it is also the gap that distinguishes a strategy from a programme.</li>
    <li><strong>The brain-drain data itself.</strong> The single most important talent-related research opportunity for an African postgraduate is an actual, rigorous quantitative study of African AI researcher migration. The work has not been done. The general migration figures circulating are insufficient.</li>
  </ol>

  <h2 class="section-title">&#127919; What This Means for Your Research</h2>

  <ul class="styled-list">
    <li><strong>Vet supervisors, not institutions.</strong> Outside the substantive PhD quadrilateral, African AI supervision is highly individual-dependent. If you are choosing where to do your PhD, the named supervisor matters more than the institution&#39;s overall reputation.</li>
    <li><strong>The compute story is now the talent story.</strong> The UCT African Compute Initiative is, in part, an explicit retention lever for African AI talent. Applying to it (or to the Rwanda AI Scaling Hub) is not just about compute access; it is about choosing to be part of the infrastructure that the next decade of African AI work will run on.</li>
    <li><strong>Read the strategies. Read them critically.</strong> The Yilma &amp; Wodajo paper is the single best entry point to the analytical literature on the strategy landscape. The Carnegie and Global Center pieces are the complementary practical reads. The SA AI Policy case is the worked example of why this matters at the policy-document level.</li>
    <li><strong>Brain-drain framing is the wrong default.</strong> The honest pattern is not &ldquo;Africa loses its AI talent to the North&rdquo;; it is &ldquo;African AI work is distributed across continent and diaspora&rdquo;. If you are an African postgraduate researcher, your collaborative network is plausibly larger and more international than the brain-drain rhetoric implies. Build it accordingly.</li>
    <li><strong>The work matters.</strong> An institutional landscape with this many gaps means that a postgraduate who chooses to work on one of them can plausibly produce a contribution that the field will recognise. The next sub-lesson (11.7) closes the week and the African half of the course by asking what you would actually do with that opportunity.</li>
  </ul>

  <h2 class="section-title">&#9999;&#65039; A Short Exercise</h2>

  <ol class="step-list">
    <li><strong>Pick the African country you would most likely engage with</strong> in your current or planned research project (this may be South Africa by default, but does not have to be).</li>
    <li><strong>Find its current AI strategy or policy document.</strong> If it has been withdrawn, find that fact. If none exists, note that as your answer.</li>
    <li><strong>Read the document&#39;s preamble and pillars.</strong> Identify the strategy&#39;s stated goals and the timeline to which they are committed.</li>
    <li><strong>Identify one specific commitment</strong> in the document that a postgraduate researcher could imaginably contribute to. It could be a dataset, a benchmark, a piece of empirical research, an institutional contribution, anything concrete.</li>
    <li><strong>Bring it to class.</strong> Together with the data-and-models exercise from 11.5 and the disclosure-policy exercise from 11.3, you will have the raw material for the Week 12 capstone pitch.</li>
  </ol>

  <h2 class="section-title">&#128218; Sources &amp; Further Reading</h2>

  <div class="resource-placeholder">
    <h4>&#128196; Strategy landscape &amp; analytical reviews</h4>
    <p><strong>Yilma, K. &amp; Wodajo, K. (2026).</strong> Strategy as Governance: The Governance of AI in Africa. <em>Science and Public Policy</em> 53(2), 236&ndash;244. <a href="https://academic.oup.com/spp/article/53/2/236/8654722" target="_blank" rel="noopener">academic.oup.com</a>. CC&nbsp;BY 4.0 open access.</p>
    <p><strong>Munga, J. &amp; Quansah, S. (September 2025).</strong> Understanding Africa&#39;s AI Governance Landscape: Insights From Policy Practice and Dialogue. Carnegie Endowment. <a href="https://carnegieendowment.org/posts/2025/09/understanding-africas-ai-governance-landscape-insights-from-policy-practice-and-dialogue" target="_blank" rel="noopener">carnegieendowment.org</a>.</p>
    <p><strong>Engida Abdella, S. &amp; Alayande, A. (April 2025).</strong> African Countries Are Racing to Create AI Strategies &mdash; But Are They Putting the Cart Before the Horse? Global Center on AI Governance. <a href="https://www.globalcenter.ai/research/african-countries-are-racing-to-create-ai-strategies-but-are-they-putting-the-cart-before-the-horse" target="_blank" rel="noopener">globalcenter.ai</a>.</p>
    <p><strong>CIPESA (2025).</strong> State of Internet Freedom in Africa 2025: Navigating the Implications of AI on Digital Democracy in Africa. <a href="https://cipesa.org/2025/09/state-of-internet-freedom-in-africa-report/" target="_blank" rel="noopener">cipesa.org</a>.</p>
  </div>

  <div class="resource-placeholder">
    <h4>&#128196; National and continental documents</h4>
    <p><strong>South Africa Draft AI Policy</strong> (Gazette 54477, 10 April 2026; withdrawn 27 April 2026). <a href="https://www.gov.za/sites/default/files/gcis_document/202604/54477gen3880.pdf" target="_blank" rel="noopener">gov.za PDF</a>.</p>
    <p><strong>Withdrawal analysis.</strong> <a href="https://www.dlapiper.com/en-us/insights/publications/2026/05/withdrawal-of-south-africa-draft-ai-policy" target="_blank" rel="noopener">DLA Piper</a>.</p>
    <p><strong>AU Continental AI Strategy</strong> (July 2024). <a href="https://au.int/en/documents/20240809/continental-artificial-intelligence-strategy" target="_blank" rel="noopener">au.int</a>.</p>
    <p><strong>AUDA-NEPAD Continental AI Roadmap</strong> (February 2025).</p>
    <p><strong>Smart Africa Africa AI Council launch</strong> (17 November 2025, Conakry). <a href="https://smartafrica.org/the-smart-africas-board-unveils-the-inaugural-africa-ai-council-to-lead-the-continents-ai-transformation/" target="_blank" rel="noopener">smartafrica.org</a>.</p>
    <p><strong>National strategies</strong>: SA (gov.za) &middot; <a href="https://www.minict.gov.rw/ai-policy" target="_blank" rel="noopener">Rwanda</a> &middot; <a href="https://www.africadataprotection.org/Kenya_AI_Strategy_2025_2030.pdf" target="_blank" rel="noopener">Kenya</a> &middot; <a href="https://ncair.nitda.gov.ng/wp-content/uploads/2025/09/National-Artificial-Intelligence-Strategy-19092025.pdf" target="_blank" rel="noopener">Nigeria</a> &middot; <a href="https://ai.gov.eg/SynchedFiles/en/Resources/AIstrategy%20English%2016-1-2025-1.pdf" target="_blank" rel="noopener">Egypt</a> &middot; <a href="https://aii.et/the-council-of-ministers-unanimously-decide-to-implement-the-national-artificial-intelligence-policy/" target="_blank" rel="noopener">Ethiopia</a>.</p>
    <p><strong>The SPP 53(2) special section</strong> &mdash; the five companion papers (Effoduh, Ogoh et al., Nyabola, Mutung&#39;u et al., Ibrahim et al., Jimoh) covered in 11.4 are the deepest peer-reviewed African-led analysis available, and are worth re-reading as a set with 11.6&#39;s empirical picture in hand.</p>
  </div>

  <div class="resource-placeholder">
    <h4>&#128196; Institutions and funding</h4>
    <p><strong>Deep Learning Indaba 2025 press release.</strong> <a href="https://deeplearningindaba.com/blog/2025/07/press-release-dli-2025/" target="_blank" rel="noopener">deeplearningindaba.com</a>.</p>
    <p><strong>AIMS Next Einstein Initiative.</strong> <a href="https://nexteinstein.org/" target="_blank" rel="noopener">nexteinstein.org</a>. AMMI: <a href="https://aimsammi.org/" target="_blank" rel="noopener">aimsammi.org</a>.</p>
    <p><strong>UCT African Compute Initiative.</strong> <a href="https://ai.uct.ac.za/articles/2026-03-26-uct-lead-africas-first-higher-education-dedicated-ai-compute-initiative" target="_blank" rel="noopener">ai.uct.ac.za</a>.</p>
    <p><strong>Wits MIND Institute</strong>; <strong>University of Pretoria AfriDSAI</strong> (<a href="https://www.up.ac.za/afridsai" target="_blank" rel="noopener">up.ac.za/afridsai</a>); <strong>AIMS South Africa AI-for-Science</strong> (<a href="https://ai.aims.ac.za/" target="_blank" rel="noopener">ai.aims.ac.za</a>).</p>
    <p><strong>ARIN.</strong> <a href="https://arin-africa.org/" target="_blank" rel="noopener">arin-africa.org</a>. <strong>Zindi.</strong> <a href="https://zindi.africa/" target="_blank" rel="noopener">zindi.africa</a>. <strong>Lelapa AI.</strong> <a href="https://lelapa.ai/" target="_blank" rel="noopener">lelapa.ai</a>.</p>
    <p><strong>Lacuna Fund.</strong> <a href="https://lacunafund.org/" target="_blank" rel="noopener">lacunafund.org</a>. <strong>IDRC AI4D Africa.</strong> <a href="https://idrc-crdi.ca/en/initiative/artificial-intelligence-development" target="_blank" rel="noopener">idrc-crdi.ca</a>.</p>
    <p><strong>Google.org Africa AI announcement</strong> (July 2025). <a href="https://blog.google/intl/en-africa/company-news/outreach-and-initiatives/a-new-blueprint-to-empower-africas-next-generation-of-ai-builders/" target="_blank" rel="noopener">blog.google</a>.</p>
    <p><strong>OpenAI / Gates Foundation Horizon 1000</strong> (January 2026). <a href="https://www.gatesnotes.com/expanding-access-to-health-care-through-ai" target="_blank" rel="noopener">gatesnotes.com</a>.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 20px; margin-bottom: 15px;"><strong>Coming up in 11.7:</strong> the closing sub-lesson of the week, and of the African half of the course. We synthesise the futures half (11.1, 11.2) and the African-capacity half (11.4&ndash;11.6) and ask the question that has been quietly underlying everything in the second half of the course: <em>what is the most useful thing a postgraduate in this room can actually do?</em> The output is the seed of your Week 12 capstone pitch.</p>
"""


# ---------------------------------------------------------------------------
# Sub-Lesson 11.7 — Synthesis and the Week-12 Capstone
# ---------------------------------------------------------------------------

SL7_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>This is the final sub-lesson of the course. It does two things at once. First it pulls the threads of Week 11 (and, behind that, the whole course) into a single integrative reading. Second, it sets out the Week-12 capstone &mdash; a 3-hour solo activity in which you write a structured research pitch about how <em>you</em> are going to use, refuse to use, and verify AI in your own research, with an honest self-critique to follow.</p>
    <p>The capstone is deliberately compact. You are a busy postgraduate science researcher in your own discipline; the course has asked enough of your time already; the right test of whether the course has done its job is whether you can produce a useful 600-word document about your own work in three honest hours. If you can, the disposition we have been trying to build has landed.</p>
    <p>The brief for the capstone lives inside this sub-lesson rather than as a separate document. The six prompts, the two worked examples, the self-critique structure, and the assessment rubric are all below. Re-read this page when you start the capstone in Week 12; you will not need anything else.</p>
  </div>

  <h2 class="section-title">&#129488; The Course in One Disposition</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">If there is a single thing this course has been trying to build, it is a disposition rather than a set of facts. The specific tools, capabilities, models, and benchmarks we have looked at will look different in two years, and considerably different in five. The disposition we have been trying to build outlasts all of that, because it is about how you read the field rather than about what is currently in it.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The disposition has four moves. You have been practising them, in different forms, across all twelve weeks.</p>

  <ul class="styled-list">
    <li><strong>Pull the primary source.</strong> Press releases overclaim, secondary coverage rounds up, search summaries quietly hallucinate. The strongest single habit in this course is to find the paper, read its limitations section, and form your view from there.</li>
    <li><strong>Read for the limitations as much as the claim.</strong> The peer-reviewed work we have looked at &mdash; from <em>AlphaFold 3</em> through DeepMind&#39;s AI Co-Scientist to the Sakana AI Scientist paper &mdash; is consistently more honest about its bounds than the framing built around it. Letting the paper speak in its own voice produces a different reading from letting the institutional context speak for it.</li>
    <li><strong>Calibrate before you cite.</strong> The Real / Overclaimed / Aspirational frame from 11.1 is not specific to the AI literature. It is the calibration habit applied somewhere it currently matters more than usual. Use it on everything.</li>
    <li><strong>Choose where you stand before you choose your tools.</strong> The African strand of the course &mdash; the relational sovereignty reading from 11.4, the Esethu and Kaitiakitanga lineage from 11.5, the policy-as-governance critique from 11.6 &mdash; is not a separable add-on to the global AI story. It is the home base from which the global picture should be read if you are doing your work from here.</li>
  </ul>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The fifth move is what the Week-12 capstone makes you do: <em>apply all of this to your own work, in writing, in a way you would be willing to defend.</em> That is the integrative question the course has been quietly pointing at for twelve weeks. What does the disposition look like when it touches your research, not someone else&#39;s?</p>

  <h2 class="section-title">&#128218; Week 11, Pulled Together</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Each of the six prior sub-lessons in this week handed you a specific input. Read together, they amount to a complete map of the territory the capstone is asking you to position yourself in.</p>

  <div style="overflow-x: auto;">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Sub-lesson</th>
          <th>What it gave you</th>
          <th>How it feeds the pitch</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>11.1</strong></td>
          <td>The Real / Overclaimed / Aspirational frame applied to claims about AI in research over the next 2&ndash;5 years</td>
          <td>Calibrates which AI tools to take seriously when planning your project</td>
        </tr>
        <tr>
          <td><strong>11.2</strong></td>
          <td>A reading guide to the genuinely speculative AI-in-research literature, with the same calibration habit applied harder</td>
          <td>Stops you from planning a project on a 2027 superintelligence assumption</td>
        </tr>
        <tr>
          <td><strong>11.3</strong></td>
          <td>The current journal, funder, and peer-review policy landscape on AI use, and the He &amp; Bu finding that policy &ne; practice</td>
          <td>Tells you which AI use you will need to disclose and what your default disclosure practice should be</td>
        </tr>
        <tr>
          <td><strong>11.4</strong></td>
          <td>A relational reading of AI sovereignty, with the compute layer in honest detail</td>
          <td>Names the infrastructure you can actually use and the sovereignty register you are working in</td>
        </tr>
        <tr>
          <td><strong>11.5</strong></td>
          <td>The African data, models, and benchmarks landscape, and six concrete thesis-shaped gaps</td>
          <td>Identifies the African-language, African-domain, or African-data dimensions of your work</td>
        </tr>
        <tr>
          <td><strong>11.6</strong></td>
          <td>The policy, institutions, and talent picture, with the SA AI Policy withdrawal as the local case study</td>
          <td>Locates your work inside the South African and continental institutional landscape</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 20px; margin-bottom: 15px;">Behind these six sub-lessons, the rest of the course is doing work too. Week 1 and 2 grounded you in how the models actually function. Week 3 made the energy and water costs concrete; Week 4 gave you the ethical frameworks (the four lenses, the Just AI framework, the relational reading from Mhlambi) you will draw on for prompt #6 below. Weeks 5 through 8 worked through the specific research-stage applications &mdash; literature review, writing, ideation, data analysis, code, multimodal &mdash; that prompt #2 will ask about. Weeks 9 and 10 gave you the verification protocols and the calibrated reading of agentic tools that will inform prompts #3 and #5.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">If you have done the weekly exercises, you have already generated most of the raw material the capstone is asking you to compress into 300 words. The work in the capstone is not collecting the material. It is choosing.</p>

  <h2 class="section-title">&#127919; The Week-12 Capstone</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The capstone is a single 3-hour solo activity, completed in Week 12 in your own time. You will produce a 600-word document in two parts: a 300-word structured research pitch, and a 300-word honest self-critique of that pitch. Submission is via Amathuba (details on the Week-12 page). Assessment counts toward the 40% Research Enhancement Project component of your overall course grade.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">This format is honest about the constraints of being a postgraduate science researcher. There is no live workshop, no peer review, no presentation. You will write the document alone, in three hours, drawing on the cumulative work of the course. It is the lightest meaningful capstone we could design that still does the integrative job; if you have engaged seriously with the course, three hours is enough.</p>

  <h2 class="section-title">&#9999;&#65039; Part 1 &mdash; The Structured Pitch (300 words)</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Six prompts, in order. Roughly 50 words each. Write them as numbered paragraphs; the structure is itself the integration. The whole pitch should fit on a single page.</p>

  <ol class="step-list">
    <li><strong>One-sentence research question.</strong> The question your project is trying to answer, in plain language a colleague in a different sub-field could follow. Not a topic, not a method &mdash; a question.</li>
    <li><strong>AI tools you will use, at which research stages, and why.</strong> Be specific. Name the family of tool (chat assistants, agentic systems, RAG-based literature tools, domain-specific models such as AlphaFold or speech models, code-generation agents). Name the stage of your work each one will touch (literature review, ideation, data analysis, code, writing, evaluation). Give your honest reason for the choice in each case.</li>
    <li><strong>What you will NOT delegate to AI, and why.</strong> The honest counter-claim. The places where, in your own discipline and on your own project, the work has to remain yours. Be specific about the boundary &mdash; what is the difference between an AI-assisted step you will take and an AI-delegated step you will not? This is the integrity move from Weeks 6 and 9.</li>
    <li><strong>One local-context choice you are making.</strong> A single concrete decision that locates your work in the African (or specifically South African) context: a language choice, a dataset choice, a hosting choice, a collaboration partner, a community-licensing decision, a decision about whom the work is for. One choice; named specifically; with a sentence on why.</li>
    <li><strong>One verification protocol you commit to.</strong> A specific, defensible procedure that catches AI errors in your particular workflow before they reach publication. Not &ldquo;I will be careful&rdquo;; an actual protocol &mdash; cross-validation against independent data, pre-registration, replication with a different model family, an explicit human-in-the-loop checkpoint, peer audit, or similar.</li>
    <li><strong>One ethical commitment from your Week 4 framework that this pitch operationalises.</strong> Pick one principle from the ethical framework you developed in Week 4 (the four lenses, the Just AI framework, the relational/ubuntu reading, or whatever combination you settled on). Identify the single concrete thing in your project that puts that principle into practice. The principle and the practice should be specific to each other; abstract restatements of Week 4 do not count.</li>
  </ol>

  <h2 class="section-title">&#128194; Two Worked Examples</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Two example pitches, one from the Earth Sciences and one from Computational Biology. Neither pitch is perfect; both pass the bar. Use them as a calibration of what a strong response looks like, not as a template to copy.</p>

  <div class="case-study">
    <h4>&#127757; Example 1 &mdash; Climate / Earth Sciences postgraduate</h4>
    <p><strong>1.</strong> Can multimodal AI digitisation of pre-1980 hydrometeorological records improve drought-onset prediction for Western Cape catchments by combining historical observations with current satellite data?</p>
    <p><strong>2.</strong> Multimodal vision-language models for digitising hand-written rainfall records (Week 8); Python data-analysis assistants for time-series cleaning (Week 7); Deep Research for the catchment-hydrology literature (Week 10); chat assistants for first-draft writing (Week 6). Each tool is paired with a specific stage and a specific accuracy-checking step.</p>
    <p><strong>3.</strong> I will not delegate the choice of which catchments to study, the interpretation of statistical-significance thresholds, or the engagement with farming communities for ground-truth on what &ldquo;drought&rdquo; means locally. The first two are research-judgement calls that determine what the work means; the third requires a human relationship that AI cannot stand in for.</p>
    <p><strong>4.</strong> Local-context choice: I will work specifically with rain-gauge station records from the Western Cape&#39;s wheat-belt rather than fitting models to a globally averaged climatology, in partnership with the Stellenbosch Centre for Sustainability Transitions.</p>
    <p><strong>5.</strong> Verification protocol: every model-predicted drought-onset window is cross-validated against a held-out set of rain-gauge records from stations not used in training, and a 12-month look-ahead is pre-registered with my supervisor before model evaluation.</p>
    <p><strong>6.</strong> Ethical commitment: from the Just AI Framework (Week 4) &mdash; the principle of <em>recipient relevance</em>. The outputs of this work are to be co-interpreted with farming-community representatives before any publication, and any predictive tool released is to remain free at the point of use for South African agricultural extension services.</p>
  </div>

  <div class="case-study">
    <h4>&#129516; Example 2 &mdash; Computational Biology / Bioinformatics postgraduate</h4>
    <p><strong>1.</strong> Can AI protein-structure prediction identify previously unstudied allosteric binding sites on <em>Plasmodium falciparum</em>&#39;s haemoglobin-degradation enzymes that might support novel antimalarial drug design?</p>
    <p><strong>2.</strong> AlphaFold 3 for predicted complex structures (Week 11.1); code-generation agents for binding-affinity calculations in Python and PyMOL (Week 7); RAG-based literature tools for the medicinal-chemistry context (Week 5); calibrated reading of vendor benchmark claims about predicted binding affinities (Week 9).</p>
    <p><strong>3.</strong> I will not delegate the biological interpretation of the predicted structures (the structures are starting points, not answers), the choice of which candidates to take into wet-lab validation, or the writing of the discussion section. The wet-lab call is the one with downstream cost and risk; the discussion is where the interpretation lives.</p>
    <p><strong>4.</strong> Local-context choice: I will prioritise <em>P. falciparum</em> strains endemic to Southern Africa for benchmark verification, in collaboration with the H3D Drug Discovery Centre at UCT, and will commit any leads identified to publication under terms that allow generic-manufacturing partners on the continent to use them.</p>
    <p><strong>5.</strong> Verification protocol: every novel binding-site prediction is independently re-run on at least two protein-structure model families before consideration, with positive predictions confirmed against published crystallographic data where available, and a pre-registered decision rule for which candidates advance to wet-lab.</p>
    <p><strong>6.</strong> Ethical commitment: from the relational reading of Week 4 &mdash; equitable benefit. Any compounds identified will be published in open-access venues with the model output and the wet-lab data both made available; no patent will be filed on any lead by the research team without prior agreement on accessibility for African public-health systems.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 20px; margin-bottom: 15px;">Both pitches are around 300 words. Both follow the six-prompt structure tightly. Both name specific tools, specific local choices, specific verification protocols, and a specific ethical commitment. Neither pitch is a template &mdash; your own pitch will look different because your research is different &mdash; but the level of specificity is the bar.</p>

  <h2 class="section-title">&#128221; Part 2 &mdash; The Solo Self-Critique (300 words)</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">After the pitch, you write a 300-word self-critique. This is the part of the capstone that requires the most intellectual honesty, because there is no peer reviewer in the room to do it for you. Two prompts, roughly 150 words each.</p>

  <div class="technical-detail">
    <h4>&#129504; A. The strongest objection to your pitch (~150 words)</h4>
    <p style="color: #444; line-height: 1.75;">Identify the strongest specific objection an experienced researcher in your field &mdash; your most demanding supervisor on a bad day, or an external examiner who has read carefully &mdash; would raise to your pitch. Not a generic worry. A specific one. Then write how you would address it. You can address it by changing the pitch, by accepting the limitation honestly, or by explaining why the objection does not in fact bite. What you cannot do is ignore it. The self-critique fails as a self-critique if the objection it raises is one your pitch already obviously answers.</p>
  </div>

  <div class="technical-detail">
    <h4>&#129488; B. The calibrated-reading habit you most need to keep practising (~150 words)</h4>
    <p style="color: #444; line-height: 1.75;">Of the four moves of the calibrated-reading disposition above &mdash; pulling primary sources, reading for limitations, calibrating before citing, choosing where you stand &mdash; which one are you, honestly, weakest at? Where in the last twelve weeks did you catch yourself short on the move? What practical habit will you adopt after the course to keep practising it? This is the only part of the capstone the course will not see you do over the rest of your career, so it is the part where being honest with yourself matters most.</p>
  </div>

  <h2 class="section-title">&#128202; Assessment Rubric</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The capstone will be graded against the six pitch prompts and the two self-critique prompts. Your work does not need to be brilliant on every dimension; it does need to be substantive on each.</p>

  <div style="overflow-x: auto;">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Dimension</th>
          <th>What we are looking for</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Research question</strong></td>
          <td>A clear, answerable question rather than a topic or method. A colleague in an adjacent sub-field could read it and understand what you are asking.</td>
        </tr>
        <tr>
          <td><strong>AI tool selection</strong></td>
          <td>Specific tool families paired with specific research stages and specific reasons. Not a list of every tool the course mentioned.</td>
        </tr>
        <tr>
          <td><strong>What you will not delegate</strong></td>
          <td>An honest, specific position. The boundary is defensible: an experienced researcher in your field would recognise it as a real distinction.</td>
        </tr>
        <tr>
          <td><strong>Local-context choice</strong></td>
          <td>A single concrete decision, named specifically, with a one-sentence justification. Not a general aspiration to be locally relevant.</td>
        </tr>
        <tr>
          <td><strong>Verification protocol</strong></td>
          <td>An actual procedure rather than an attitude. We should be able to imagine the procedure being applied.</td>
        </tr>
        <tr>
          <td><strong>Ethical commitment</strong></td>
          <td>A principle from your Week-4 framework paired with the specific thing in your project that puts it into practice. Not an abstract restatement.</td>
        </tr>
        <tr>
          <td><strong>Self-critique &mdash; objection</strong></td>
          <td>A specific objection the pitch does not already obviously answer, addressed substantively.</td>
        </tr>
        <tr>
          <td><strong>Self-critique &mdash; calibrated reading</strong></td>
          <td>Honest identification of one weak habit and a concrete next-step practice.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2 class="section-title">&#9201;&#65039; Timing the Capstone Honestly</h2>

  <div class="technical-detail">
    <h4>A three-hour outline</h4>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;">If you have done the weekly exercises, three hours is comfortable. If you have not, three hours is tight. The outline below is a recommendation, not a prescription.</p>
    <ul class="styled-list" style="margin-top: 0;">
      <li><strong>0&ndash;30 minutes:</strong> Re-read this sub-lesson (the six prompts, the two worked examples, the rubric). Open a blank document. Re-read the activity outputs you generated for the Week 11 sub-lessons.</li>
      <li><strong>30&ndash;120 minutes:</strong> Draft the six pitch paragraphs in order. Do not stop to polish until all six are on the page. The first draft will overshoot 300 words; that is fine.</li>
      <li><strong>120&ndash;165 minutes:</strong> Draft the two self-critique paragraphs. The objection one is the harder one and is worth dwelling on.</li>
      <li><strong>165&ndash;180 minutes:</strong> Polish both parts to fit the word counts. Submit.</li>
    </ul>
  </div>

  <h2 class="section-title">&#128587; A Closing Note</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">This is the last thing the course asks of you. It is intentionally smaller than a course at this level might typically ask, because the value of the disposition we have been trying to build is what you carry into the next five years of your research, not what you produce for assessment in the next three hours.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">If the course has done its work, you will have started writing the pitch already in your head while reading the worked examples. The Week-12 capstone is then largely a transcription exercise. If the course has not done its work &mdash; or if the work it has done has been overtaken by how quickly the field has moved &mdash; the disposition is still the right thing to keep practising. The specific tools and policies and benchmarks in the course will change. The habit of pulling the primary source, reading for the limitations, calibrating before citing, and choosing where you stand will not.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Good luck with your research.</p>

  <div class="highlight-box">
    <h3>&#128218; <span style="color: #ffffff;">For the capstone, you need only re-read this page</span></h3>
    <p>The brief, the prompts, the worked examples, the self-critique structure, and the rubric all live here. Submission instructions are on the Week-12 Amathuba page. There is no separate document to download and no further reading required. Use the time on the work.</p>
  </div>
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
    {
        "filename": "The Shifting Research Landscape.html",
        "title": "Week 11.3 - The Shifting Research Landscape: Policy, Peer Review, Integrity",
        "badge": "Week 11 &bull; Sub-Lesson 3",
        "header_emoji": "&#127963;&#65039;",  # classical building / institution
        "header_title": "The Shifting Research Landscape",
        "header_subtitle": "How journal policies, funder rules, and peer-review norms have moved in the last 18 months &mdash; and why researcher practice has not kept pace",
        "body": SL3_BODY,
    },
    {
        "filename": "Sovereign AI Capacity and Why Compute Is the Floor.html",
        "title": "Week 11.4 - Sovereign AI Capacity, and Why Compute Is the Floor",
        "badge": "Week 11 &bull; Sub-Lesson 4",
        "header_emoji": "&#127757;",  # earth globe Africa
        "header_title": "Sovereign AI Capacity, and Why Compute Is the Floor",
        "header_subtitle": "What sovereignty means when read from an African intellectual tradition &mdash; and where the actual African compute is, isn&#39;t, and might be",
        "body": SL4_BODY,
    },
    {
        "filename": "Data Languages and African Model-Building.html",
        "title": "Week 11.5 - Data, Languages and African Model-Building",
        "badge": "Week 11 &bull; Sub-Lesson 5",
        "header_emoji": "&#128488;&#65039;",  # speech balloon (languages)
        "header_title": "Data, Languages and African Model-Building",
        "header_subtitle": "The global Indigenous data-sovereignty arc, the African foundation-model inventory, the benchmark stack, and where the gaps are",
        "body": SL5_BODY,
    },
    {
        "filename": "Policy Institutions and Talent.html",
        "title": "Week 11.6 - Policy, Institutions, and Talent",
        "badge": "Week 11 &bull; Sub-Lesson 6",
        "header_emoji": "&#127963;&#65039;",  # classical building (policy/institutions)
        "header_title": "Policy, Institutions, and Talent",
        "header_subtitle": "The strategy-as-governance picture, the South African policy withdrawal as the local case study, the funding flows that actually move, and the institutions that train and retain African AI researchers",
        "body": SL6_BODY,
    },
    {
        "filename": "Synthesis and the Week-12 Capstone.html",
        "title": "Week 11.7 - Synthesis and the Week-12 Capstone",
        "badge": "Week 11 &bull; Sub-Lesson 7",
        "header_emoji": "&#127919;",  # bullseye (synthesis/target)
        "header_title": "Synthesis and the Week-12 Capstone",
        "header_subtitle": "The course in one disposition; how Week 11 pulls together; and the brief for the 3-hour solo capstone activity in Week 12",
        "body": SL7_BODY,
    },
]


# Table of Contents (just 11.1 for now; will grow as sub-lessons are added)
TOC_HTML = """<html><head><meta http-equiv="'Content-Type'" content="'text/html;charset=utf-8'" /><title>MAM5020F 2026 | Gen AI for Research - Week 11: Future of AI in Research &amp; Africa's Sovereign AI Capacity</title></head><body>
<div style="background: #003A70; padding: 8px 20px; text-align: center;"><a href="../index.html" style="color: white; text-decoration: none; font-size: 0.85em;">&#8592; Back to Contents</a></div><table cellpadding=0 cellspacing=0 border=0 width=100%><tr><td colspan=3>&nbsp;</td></tr><tr><td valign="top" width="100%"><font class="title"><strong>MAM5020F 2026 | Gen AI for Research - Week 11: Future of AI in Research &amp; Africa&#39;s Sovereign AI Capacity</strong></font><br><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="What the Future of AI in Research Might Look Like.html" />1. What the Future of AI in Research Might Look Like</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Speculative Futures - A Reading Guide.html" />2. Speculative Futures &mdash; A Reading Guide</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="The Shifting Research Landscape.html" />3. The Shifting Research Landscape: Policy, Peer Review, Integrity</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Sovereign AI Capacity and Why Compute Is the Floor.html" />4. Sovereign AI Capacity, and Why Compute Is the Floor</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Data Languages and African Model-Building.html" />5. Data, Languages and African Model-Building</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Policy Institutions and Talent.html" />6. Policy, Institutions and Talent</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Synthesis and the Week-12 Capstone.html" />7. Synthesis and the Week-12 Capstone</a></p></td></tr></table><footer style="background: #f9f9f9; margin-top: 40px; padding: 22px 30px; text-align: center; color: #888; font-size: 0.85em; border-top: 1px solid #eee; font-family: 'Lato', 'Lucida Sans Unicode', 'Lucida Grande', sans-serif;">
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
