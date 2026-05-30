#!/usr/bin/env python3
"""
Generate Week 9 lesson HTML files (Table of Contents + 6 sub-lessons).

Outputs to both:
  Course materials/Week 9/                  (source / Amathuba upload copies)
  Course materials/docs/week-9/             (GitHub Pages serving copies)

Re-run after any content change.
"""

import os
import re

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SRC_DIR = os.path.join(ROOT, "Week 9")
DOCS_DIR = os.path.join(ROOT, "docs", "week-9")


def pretty_print_css(css: str) -> str:
    """Convert single-line CSS rules to multi-line format (each property on its own line).
    Brightspace's TinyMCE strips compact <style> blocks but preserves pretty-printed ones
    that match the format of Weeks 1-8."""
    out_lines = []
    for line in css.splitlines():
        # Match a CSS rule like `selector { prop: val; prop: val; }` on a single line.
        m = re.match(r"^(\s*)(.+?)\s*\{\s*(.+?)\s*\}\s*$", line)
        if m and ";" in m.group(3):
            indent, selector, props = m.group(1), m.group(2), m.group(3)
            # Split by `;` but keep declarations intact
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
/* Force white text on dark-blue backgrounds (overrides Brightspace stylesheet defaults).
   !important is required because Brightspace's body:not(.template-fallback) h1..h6 selector
   has specificity (0,2,2), beating .highlight-box h3 (0,1,1). */
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
# Sub-Lesson 9.1 — The Trajectory of LLM Capabilities
# ---------------------------------------------------------------------------

SL1_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>The way researchers talk about &ldquo;what AI can&#39;t do&rdquo; goes stale faster than almost any other technical claim in the literature. A paper from 2023 documenting that ChatGPT failed at undergraduate mathematics is, by 2026, a historical artefact rather than a current diagnosis. A claim from 2024 that AI can&#39;t do scientific writing well no longer matches what frontier models produce today. The artefact under study has changed. The literature about it has not always kept up.</p>
    <p>This sub-lesson does two things. First, it lays out the trajectory of LLM capabilities from 2019 to May 2026, so you have a calibrated sense of where the frontier sits right now. Second, it makes the central pedagogical move of the whole week explicit: every claim about AI limitations carries an implicit &ldquo;as of [date]&rdquo;. Reading the AI literature critically means asking which model, which date, and whether anyone has retested.</p>
    <p>The week&#39;s centrepiece reading lives at the end of this sub-lesson: a May 2026 blog post by the Fields-medallist Tim Gowers reporting on his experience using ChatGPT 5.5 Pro to extend bounds on an open problem in additive number theory. Read it before moving on to the next sub-lesson.</p>
  </div>

  <h2 class="section-title">&#128200; A Seven-Year Sweep</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The pace of capability change over the last seven years is worth pausing on. Below is a deliberately compressed history. Each row marks a moment when the answer to &ldquo;what can these systems do?&rdquo; shifted enough that the previous answer became wrong.</p>

  <div style="overflow-x: auto;">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Year</th>
          <th>Frontier model(s)</th>
          <th>What was new</th>
          <th>What still failed</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>2019</strong></td>
          <td>GPT-2 (1.5B)</td>
          <td>OpenAI initially declined to release weights citing misuse risk; sparked first wave of policy debate.</td>
          <td>Output became incoherent past a few paragraphs; no real reasoning; minimal factual reliability.</td>
        </tr>
        <tr>
          <td><strong>2020</strong></td>
          <td>GPT-3 (175B)</td>
          <td>Few-shot in-context learning &mdash; the system could do tasks it had never been trained on if given examples in the prompt.</td>
          <td>Confidently fabricated facts; couldn&#39;t reliably do basic arithmetic; no instruction-following beyond pattern matching.</td>
        </tr>
        <tr>
          <td><strong>2022&ndash;23</strong></td>
          <td>ChatGPT, GPT-4, Claude 2</td>
          <td>Instruction-following via RLHF; emergent reasoning on graduate-level tasks; mass adoption.</td>
          <td>Hallucinated citations at high rates (Week 5); the &ldquo;reversal curse&rdquo;; failed graduate-level mathematics; limited tool use.</td>
        </tr>
        <tr>
          <td><strong>2024</strong></td>
          <td>GPT-4o, Claude 3.5 Sonnet, Gemini 1.5</td>
          <td>First generation with measurable drops in basic-failure rates; multimodal inputs (Week 8); early agentic capability.</td>
          <td>Still unreliable on niche-topic citations; sycophancy persisted; long-context performance degraded mid-document.</td>
        </tr>
        <tr>
          <td><strong>2025</strong></td>
          <td>Claude 4 / Opus 4.6, GPT-5, Gemini 2.5 / Deep Think</td>
          <td>IMO 2025 gold-medal performance (35/42, end-to-end natural language, within the 4.5-hour competition window). FrontierMath at ~50%. Frontier coding capability.</td>
          <td>Domain-specific brittleness remained; cross-disciplinary verification still required human expertise; calibration still imperfect.</td>
        </tr>
        <tr>
          <td><strong>May 2026</strong></td>
          <td>Claude Mythos, Opus 4.7, GPT-5.5 Pro, Gemini 3.1 Pro, DeepSeek V4 Pro&hellip;</td>
          <td>Research-grade contributions in mathematics (Erd&#337;s problems) and theoretical physics (gluon and graviton amplitudes). Open-weights frontier (DeepSeek) competitive with closed.</td>
          <td>The structural failures &mdash; long-tail brittleness, compositional errors, illusions of understanding &mdash; persist (see 9.2 and 9.4).</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="info-box">
    <h4>&#128161; Why This Matters Now</h4>
    <p>If you arrived in this course with a calibration of AI based on news coverage from 2023, you are in roughly the position of someone reading 2010 reviews of smartphone cameras. Some core observations still apply &mdash; cameras have lenses, smartphones have batteries &mdash; but the specifics are out of date.</p>
    <p>The recalibration matters in two directions. Some things you might think AI can&#39;t do, it now can. Some things you might think AI can do reliably, it cannot. Both errors are common in published research right now. This sub-lesson and the next two address them in turn.</p>
  </div>

  <!-- SECTION: MAY 2026 LANDSCAPE -->
  <h2 class="section-title">&#128300; The May 2026 Frontier &mdash; Closed-Weights Models</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">As of mid-May 2026, the closed-weights frontier comprises six families of models, all from large well-resourced labs. Each has slightly different strengths, and the leaderboards shuffle every few weeks. The numbers below are accurate at time of writing and will be wrong within months &mdash; that itself is a teaching point.</p>

  <div class="card-grid">

    <div class="card">
      <h3>Anthropic &mdash; Claude Mythos (Preview)</h3>
      <p>Released as a limited preview in May 2026. Currently leads the GPQA Diamond reasoning benchmark at <strong>94.6%</strong> and HLE at <strong>64.7</strong>. Notable in security: autonomously identified and exploited a 17-year-old remote-code-execution vulnerability in FreeBSD with no human guidance after the initial request. As of early May 2026, the UK AI Security Institute reported GPT-5.5 reaching rough parity with Mythos on offensive-cyber evaluations (GPT-5.5 71.4% vs Mythos 68.6% on multi-step attack simulations) &mdash; so Anthropic&#39;s earlier unique lead in this domain has narrowed. Available to limited partners via Project Glasswing.</p>
    </div>

    <div class="card">
      <h3>Anthropic &mdash; Claude Opus 4.7</h3>
      <p>Generally available since 16 April 2026. SWE-bench Verified <strong>87.6%</strong> (up from 80.8% on Opus 4.6). MCP-Atlas (multi-tool agentic) <strong>77.3%</strong>. Coding lift of 13% over Opus 4.6. Vision resolution roughly tripled. The current default for production-grade research workflows.</p>
    </div>

    <div class="card">
      <h3>OpenAI &mdash; GPT-5.5 Pro &amp; GPT-5.5</h3>
      <p>Top of the FrontierMath leaderboard. GPT-5.5 Pro at <strong>52.4%</strong>; GPT-5.5 at 51.7%. The GPT-5.4 Pro variant (50%) is the model behind the Erd&#337;s problem solutions discussed in 9.3. The GPT-5.2 Pro variant produced the gluon-amplitude result with the Strominger group.</p>
    </div>

    <div class="card">
      <h3>Google DeepMind &mdash; Gemini 3.1 Pro / Deep Think</h3>
      <p>Achieved IMO 2025 gold medal: 5/6 problems solved, 35/42 points, end-to-end natural language within the competition&#39;s 4.5-hour window &mdash; up from a silver in 2024. Long context, multimodal, and the Deep Think variant powers the cosmic-string radiation result discussed in 9.3.</p>
    </div>

    <div class="card">
      <h3>Meta &mdash; Muse Spark</h3>
      <p>Released 8 April 2026. Meta&#39;s first frontier model since Llama 4, and notably their first <em>not</em> released as open weights. Scores 52 on the Artificial Analysis Intelligence Index. Natively multimodal with text, image and voice input. Includes a parallel-reasoning &ldquo;Contemplating mode&rdquo;. Powers Meta AI inside WhatsApp, Instagram, Facebook, Messenger and Ray-Ban smart glasses.</p>
    </div>

    <div class="card">
      <h3>Other major closed labs</h3>
      <p>xAI&#39;s Grok 4, Mistral&#39;s Large 3, Cohere&#39;s Command R+ generation, and Inflection-acquired models from Microsoft also sit in the broad frontier band. A new OpenAI model (codename &ldquo;Spud&rdquo;) is reportedly imminent at time of writing. Track <a href="https://llm-stats.com/" target="_blank" rel="noopener">llm-stats.com</a> or <a href="https://benchlm.ai/" target="_blank" rel="noopener">benchlm.ai</a> for current state.</p>
    </div>

  </div>

  <h2 class="section-title">&#128274; The May 2026 Frontier &mdash; Open-Weights Models</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">A meaningful part of the 2026 story is that open-weights models have closed most of the gap. This wasn&#39;t true in 2023&ndash;24, where closed labs had a clear lead on every important capability. As of May 2026, an open-weights model leads the world on competitive programming, and matches the closed frontier on most agentic and coding benchmarks at substantially lower cost.</p>

  <div class="card-grid">

    <div class="card">
      <h3>DeepSeek V4 Pro</h3>
      <p>Released 24 April 2026 under the MIT licence. Mixture-of-experts architecture: <strong>1.6 trillion total parameters with 49 billion active</strong> per token. <strong>1 million token context window</strong>. Codeforces rating <strong>3206</strong> &mdash; the highest competitive-programming score of any model, surpassing GPT-5.4&#39;s 3168. SWE-bench Verified 80.6%. Roughly 10&ndash;13&times; cheaper per output token than the closed frontier on most agentic benchmarks.</p>
    </div>

    <div class="card">
      <h3>Kimi K2.6 (Moonshot AI)</h3>
      <p>Released 20 April 2026 by the Beijing-based startup Moonshot. Mixture-of-experts: <strong>1 trillion total parameters with 32 billion active</strong>. 256K context window. <strong>SWE-Bench Verified 85.4 %</strong> &mdash; effectively ties GPT-5.5 (85.1%) at roughly 80% lower cost per token. Modified MIT license (display requirement only kicks in above 100M monthly active users or $20M monthly revenue). A second open-weights model now matching closed-frontier coding capability is a notable trajectory data point.</p>
    </div>

    <div class="card">
      <h3>DeepSeek V4 Flash</h3>
      <p>The efficiency variant: 284B total parameters, 13B active. Designed for high-throughput deployment where Pro&#39;s scale is unnecessary.</p>
    </div>

    <div class="card">
      <h3>Qwen 3.6 (Alibaba) &amp; Gemma 4 (Google DeepMind)</h3>
      <p>Qwen 3.6 27B (April 2026): Apache 2.0, 262K context window, native multimodal input, BF16 weights small enough to fit on a single H100. Top of Artificial Analysis&#39;s Intelligence Index for open-weights models under 150B parameters at 46. Hybrid thinking model (toggle chain-of-thought on/off). Reaches frontier on AIME 2026 (~91%). Both Qwen 3.6 and Gemma 4 implement <strong>Multi-Token Prediction (MTP)</strong> &mdash; predicting several future tokens per forward pass for substantial inference speed-ups, an emerging cross-model technique.</p>
    </div>

    <div class="card">
      <h3>Other open-weights players</h3>
      <p>Tencent&#39;s <strong>Hy3-preview</strong> (295B/21B MoE, restricted commercial license) and xAI&#39;s <strong>Grok 4.3</strong> (~40&ndash;60% cheaper than Grok 4.20 v2) sit just below the frontier. Ant Group&#39;s <strong>Ling 2.6 1T</strong> targets cost-efficiency at $95-per-benchmark-run but reports a 92% hallucination rate on AA-Omniscience &mdash; a useful warning that not all open-weights releases inherit the leading labs&#39; mitigations (see 9.2). The Mistral and Falcon families remain strong on European-deployment grounds. <strong>Zyphra ZAYA1-74B</strong> (May 2026) is a non-standard transformer architecture with hybrid attention &mdash; an architectural-innovation data point.</p>
    </div>

  </div>

  <div class="warning-box">
    <h4>&#9888;&#65039; The Pace of Change</h4>
    <p>Every model and number above will be wrong within months. By the time you sit this course, several of these systems will have been replaced or substantially upgraded; new entrants will have appeared; some leaderboards will have saturated. Treat the table as a snapshot and use the <a href="https://llm-stats.com/" target="_blank" rel="noopener">llm-stats.com</a> and <a href="https://benchlm.ai/" target="_blank" rel="noopener">benchlm.ai</a> leaderboards as living references.</p>
  </div>

  <!-- SECTION: BENCHMARKS -->
  <h2 class="section-title">&#129518; What These Benchmarks Actually Measure</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Benchmark scores are now the standard currency of AI capability claims. They are useful, but only if you know what each one tests. A 90% on AIME and a 50% on FrontierMath sound very different but might describe the same model on tasks of very different difficulty.</p>

  <div style="overflow-x: auto;">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Benchmark</th>
          <th>What it measures</th>
          <th>Current SOTA (May 2026)</th>
          <th>Created by / source</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>FrontierMath</strong></td>
          <td>350 expert-level mathematics problems (300 Tier 1&ndash;3 + 50 Tier 4 unpublished). Evaluated with Python tools.</td>
          <td>GPT-5.5 Pro 52.4%</td>
          <td><a href="https://epoch.ai/frontiermath" target="_blank" rel="noopener">Epoch AI</a>; problems set by IMO gold medallists and Fields Medal recipients.</td>
        </tr>
        <tr>
          <td><strong>GPQA Diamond</strong></td>
          <td>Graduate-level physics, biology and chemistry reasoning. Designed to be Google-proof.</td>
          <td>Claude Mythos 94.6%</td>
          <td>Frontier reasoning benchmark; widely used to discriminate among frontier models.</td>
        </tr>
        <tr>
          <td><strong>SWE-bench Verified</strong></td>
          <td>Real-world software engineering: GitHub issues with verified human-validated solutions.</td>
          <td>Opus 4.7 87.6%</td>
          <td>Princeton/Anthropic-validated subset of the original SWE-bench.</td>
        </tr>
        <tr>
          <td><strong>AIME 2026</strong></td>
          <td>American Invitational Mathematics Examination &mdash; high-school olympiad level.</td>
          <td>Qwen3.5-plus 91.3%</td>
          <td>Closing in on saturation; useful but no longer discriminating at the top.</td>
        </tr>
        <tr>
          <td><strong>MCP-Atlas</strong></td>
          <td>Multi-tool agentic workflows using the Model Context Protocol.</td>
          <td>Opus 4.7 77.3%</td>
          <td>Anthropic; tracks performance on real agentic deployments.</td>
        </tr>
        <tr>
          <td><strong>HLE</strong></td>
          <td>Human Language Evaluation &mdash; broad reasoning across domains.</td>
          <td>Claude Mythos 64.7</td>
          <td>Composite reasoning measure.</td>
        </tr>
        <tr>
          <td><strong>Codeforces (Elo)</strong></td>
          <td>Competitive programming rating against human contestants.</td>
          <td>DeepSeek V4 Pro 3206</td>
          <td>Notable: an open-weights model leads here, ahead of GPT-5.4&#39;s 3168.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="info-box">
    <h4>&#128270; Reading Benchmark Scores Critically</h4>
    <p>Three pitfalls to watch for in announcements:</p>
    <p>(1) <strong>Benchmark mismatch.</strong> A 90% on AIME 2024 does not predict a 90% on FrontierMath. The benchmarks measure different things at different levels of difficulty.</p>
    <p>(2) <strong>Saturation.</strong> When the SOTA on a benchmark exceeds about 90%, the benchmark has stopped discriminating and the remaining gap is largely noise.</p>
    <p>(3) <strong>Selection.</strong> Labs cherry-pick benchmarks favourable to their model. Always check whether the announcement reports performance on benchmarks where competitors lead.</p>
  </div>

  <!-- SECTION: WHAT BENCHMARKS DON'T TELL YOU -->
  <h2 class="section-title">&#128683; What Benchmarks Don&#39;t Tell You</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Benchmark scores are easy to read and easy to compare. They give the illusion of an objective measure of capability. They are, in fact, a partial and contested measure &mdash; and three specific failures of benchmarks are worth knowing before you read any model announcement uncritically.</p>

  <h3 style="color: #2a5298; font-size: 1.4em; margin: 30px 0 15px;">1. Goodhart&#39;s Law: Benchmarks Are Not Real-World Use</h3>

  <div class="info-box">
    <h4>&#128221; Goodhart&#39;s Law (Strathern&#39;s formulation, 1997)</h4>
    <p><em>&ldquo;When a measure becomes a target, it ceases to be a good measure.&rdquo;</em></p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 15px; margin-bottom: 15px;">Charles Goodhart, a British economist, originally articulated the principle in 1975 in the context of monetary policy: any observed statistical regularity tends to collapse once pressure is placed upon it for control purposes. The popular formulation above is from anthropologist Marilyn Strathern in 1997.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The application to AI benchmarks is direct. The benchmarks were originally proxies for capability &mdash; if a model scores well on FrontierMath, that&#39;s evidence the model can do research-level mathematics. But once benchmarks become the public yardstick for model quality, labs train and tune <em>specifically to perform well on them</em>. The benchmark stops being a proxy for capability and becomes a target the model is optimised to hit. The resulting score is no longer a good measure of the underlying capability the benchmark was meant to track.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">A concrete consequence: a model that scores 87.6% on SWE-bench Verified is genuinely good at GitHub-issue-style coding tasks. It may or may not be good at the coding work <em>you</em> need to do. A model that scores 52.4% on FrontierMath is genuinely capable on Fields-medal-curated mathematics problems. It may or may not be useful for the specific mathematical questions in <em>your</em> field. The benchmark measures performance on the benchmark; that&#39;s all it can measure.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">This is why Sub-Lesson 9.6 asks you to test current frontier models on tasks from your own field, rather than rely on published benchmark scores. The benchmarks tell you what the labs have optimised for. They tell you very little about whether the model will work for what <em>you</em> need.</p>

  <div class="case-study">
    <h4>&#128221; A Concrete Goodhart Illustration: SWE-Bench &rarr; ProgramBench</h4>
    <p>Frontier models score above 87% on SWE-bench Verified (Opus 4.7) and 85% on it (Kimi K2.6, GPT-5.5). The benchmark is approaching saturation. If you read those scores as a measure of &ldquo;the model is now good at software engineering,&rdquo; you would be making the Goodhart error.</p>
    <p>ProgramBench (May 2026) tests something different: given <em>only</em> a program and its documentation, can the model architect and implement a codebase from scratch that matches the reference behaviour? No method signatures to fill in, no class skeletons, no natural-language descriptions of file layout. 200 tasks sourced from real-world open-source GitHub repositories, with more than 248,000 behavioural tests.</p>
    <p>The result on the same frontier models that nearly saturate SWE-bench: <strong>0% pass rate on fully resolving any task</strong>. Across all nine frontier models tested &mdash; including Opus 4.7, GPT-5.4, Gemini 3.1 Pro &mdash; not one fully resolved task. Even partial credit was sparse (Opus 4.7 reaches 95% test-pass rate on only 3% of tasks).</p>
    <p>The same models, the same general task family (software engineering), wildly different scores. SWE-bench measures &ldquo;can the model solve well-scoped patches to existing code given the issue description.&rdquo; It does not measure &ldquo;can the model architect and build a real piece of software.&rdquo; The benchmark you cite determines the capability claim you can make.</p>
    <p style="font-size: 0.9em; color: #003A70; font-weight: 600;">Source: <a href="https://arxiv.org/abs/2605.03546" target="_blank" rel="noopener">ProgramBench: Can Language Models Rebuild Programs From Scratch? (arXiv:2605.03546, May 2026)</a></p>
  </div>

  <div class="case-study">
    <h4>&#128221; The Hidden Variable: Harness Engineering</h4>
    <p>A second Goodhart-adjacent finding has been hardening across 2026: a model&#39;s benchmark score conflates two things &mdash; the model&#39;s underlying capability, and the engineering work done around the model (system prompt, tools, middleware, decomposition strategy, retrieval scaffolding). The community has started calling this latter component the <em>harness</em>, and the harness now often dominates.</p>
    <p>The Agentic Harness Engineering paper documents the effect: the same model on Terminal-Bench 2 went from <strong>69.7% to 77.0%</strong> over ten iterations of pure harness improvement &mdash; beating a human-designed Codex-CLI baseline of 71.9% &mdash; while reducing token use on SWE-bench Verified by 12%. Other reports converge on the same observation: 10&ndash;20 point swings on tau2-bench depending on prompts and middleware, while the underlying model is identical. <em>Source: Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses</em>, <a href="https://arxiv.org/abs/2604.25850" target="_blank" rel="noopener">arXiv:2604.25850</a> (April 2026).</p>
    <p>The implication for reading announcements: a 90% score on a benchmark may reflect a 75% model with a great harness, or an 85% model with a mediocre harness. When a lab announces SOTA on benchmark X, you cannot disentangle the harness contribution from the model contribution. For your own work, the corollary is that switching to the latest frontier model is often less impactful than improving the harness around the model you already use.</p>
  </div>

  <h3 style="color: #2a5298; font-size: 1.4em; margin: 40px 0 15px;">2. Benchmark Contamination &mdash; Training-Data Leakage</h3>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">A benchmark only measures capability if the model hasn&#39;t already seen the answers. The internet contains most published benchmarks. Models trained on web-scale data have, in many cases, seen the benchmark questions and answers during training &mdash; producing inflated scores that don&#39;t reflect generalised capability.</p>

  <div class="case-study">
    <h4>&#128221; The MMLU Contamination Evidence</h4>
    <p>Deng, C., Zhao, Y., Tang, X., Gerstein, M., &amp; Cohan, A. (2023). <em>Investigating Data Contamination in Modern Benchmarks for Large Language Models.</em> <a href="https://arxiv.org/abs/2311.09783" target="_blank" rel="noopener">arXiv:2311.09783</a>.</p>
    <p>Used a &ldquo;Testset Slot Guessing&rdquo; methodology: mask one wrong answer in an MMLU multiple-choice question and ask the model to fill it in. A model that has never seen the question should perform near chance. ChatGPT achieved <strong>52%</strong> exact-match on the masked options; GPT-4 achieved <strong>57%</strong>. Far above chance, and consistent with having seen the test set.</p>
    <p>A subject-level scan of MMLU found contamination rates as high as <strong>66.7%</strong> in some subjects. Variations of the contamination methodology have been documented in dozens of papers since &mdash; benchmark contamination is now a recognised systematic problem, not a one-off finding. The <a href="https://github.com/lyy1994/awesome-data-contamination" target="_blank" rel="noopener">Awesome Data Contamination</a> repository tracks the literature.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 20px; margin-bottom: 15px;">The implication: a model&#39;s reported MMLU score may overstate its general reasoning ability, possibly substantially. Comparable concerns apply to AIME, GSM8K, HumanEval, and most popular benchmarks &mdash; all of which have appeared in training corpora.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Three responses have emerged:</p>

  <ul class="styled-list">
    <li><strong>Held-out / private benchmarks.</strong> FrontierMath was deliberately constructed as 350 entirely new and unpublished problems. The Tier 4 set has <strong>20 problems explicitly held out</strong> from OpenAI (the funder) so a private set remains for honest evaluation; the leaderboard scores reported in this lesson are evaluated on the private sets. CharXiv (Week 8) used a similar design.</li>
    <li><strong>Cleaned and refreshed benchmarks.</strong> MMLU-Pro (Wang et al. 2024) increased question difficulty and expanded answer choices to make memorisation less helpful. MMLU-Redux (2025) cleaned ambiguous questions and incorrect answers from the original.</li>
    <li><strong>Dynamic benchmarks.</strong> Benchmarks regenerated continuously based on training cutoffs, so contamination is structurally impossible. <a href="https://arxiv.org/abs/2312.12343" target="_blank" rel="noopener">LatestEval (AAAI 2024)</a> is one example.</li>
  </ul>

  <p style="color: #555; line-height: 1.75; margin-top: 15px;">When you read a benchmark score in a model announcement, ask: was this evaluation done on a private/held-out set, or on a public benchmark that was probably in the training data?</p>

  <h3 style="color: #2a5298; font-size: 1.4em; margin: 40px 0 15px;">3. What Benchmarks Don&#39;t Test &mdash; Low-Resource Languages and African Contexts</h3>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Almost every major benchmark in the table above &mdash; FrontierMath, GPQA Diamond, SWE-bench Verified, AIME, MCP-Atlas, HLE &mdash; is administered <strong>in English</strong>. A model that excels on these benchmarks is genuinely good at English-language reasoning on topics well-represented in English-language training data. The leaderboard scores tell you very little about how the model performs on questions in Setswana, on legal reasoning grounded in South African law, on medical questions framed for a Nigerian or Kenyan clinical context, or on mathematics problems written by African educators for African students.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">For UCT students, this matters directly: the benchmark scores you see in news coverage may not predict how the same model performs on your research questions, your students&#39; questions, or your local context.</p>

  <div class="case-study">
    <h4>&#128221; The Measured Gap</h4>
    <p>The <em>Bridging the Gap</em> project (Alhanai, Kasumovic, Ghassemi, Zitzelberger, Lundin &amp; Chabot-Couture, AAAI 2025; <a href="https://arxiv.org/abs/2412.12417" target="_blank" rel="noopener">arXiv:2412.12417</a>) translated portions of MMLU and Winogrande into eight low-resource African languages (Amharic, Bambara, Igbo, Sepedi, Shona, Sesotho, Setswana, Tsonga) covering more than 160 million speakers. The paper reports &ldquo;previously unknown performance gaps&rdquo; between state-of-the-art LLMs in English and these African languages, and explores fine-tuning, cross-lingual transfer, and cultural-appropriateness adjustments as mitigations &mdash; achieving incremental improvements (5.6% from fine-tuning, 2.9% from cross-lingual transfer) that are notable precisely because the underlying gap is so substantial.</p>
    <p>Even the &ldquo;multilingual&rdquo; benchmarks tend to under-cover Africa. <a href="https://mmluprox.github.io/" target="_blank" rel="noopener">MMLU-ProX</a> covers 29 languages including Wolof, Yoruba, and Zulu, but documents consistent performance degradation from high-resource to low-resource languages. Most African languages aren&#39;t covered at all.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 20px; margin-bottom: 15px;">Africa-specific benchmarks have begun to emerge in response to the gap. They are useful but not yet widely cited in model announcements:</p>

  <ul class="styled-list">
    <li><strong><a href="https://aclanthology.org/2025.findings-acl.976.pdf" target="_blank" rel="noopener">AfroBench (ACL 2025)</a></strong> &mdash; comprehensive evaluation of LLMs on African languages across multiple NLP tasks.</li>
    <li><strong><a href="https://arxiv.org/abs/2406.03368" target="_blank" rel="noopener">IrokoBench</a></strong> &mdash; benchmark designed specifically for African languages in the LLM era.</li>
    <li><strong>AfriSpeech-Dialog (NAACL 2025)</strong> and <strong>Intron Sahara v2 (2026, 57 languages)</strong> &mdash; African-language ASR benchmarks (covered in Week 8).</li>
    <li><strong>Nahabwe et al. (2025), <em>Benchmarking Automatic Speech Recognition Models for African Languages</em></strong>, arXiv:2512.10968 &mdash; covered in Week 8.</li>
  </ul>

  <p style="color: #555; line-height: 1.75; margin-top: 15px; margin-bottom: 15px;">The pattern: for well-represented African languages (Swahili, Hausa, Yoruba, Afrikaans), frontier models perform reasonably. For under-represented languages (Setswana, Sepedi, isiXhosa, isiZulu in many tasks), performance falls off substantially. <strong>Performance differences between languages are larger than performance differences between frontier models.</strong></p>

  <div class="warning-box">
    <h4>&#9888;&#65039; A Practical Implication</h4>
    <p>If your research touches African languages, African legal systems, African clinical contexts, or African educational systems, do not rely on benchmark scores to predict model usefulness. The benchmarks don&#39;t test what you need to know.</p>
    <p>Instead, build your own small evaluation: a set of representative questions from your domain, in the languages and contexts you actually work with. The hands-on activities in 9.6 explicitly ask you to do this for your own field. The capability and limitation maps that emerge will be far more informative than any benchmark leaderboard for your purposes.</p>
  </div>

  <div class="highlight-box">
    <h3>The three failures together</h3>
    <p><strong>Goodhart&#39;s law</strong> means benchmarks measure benchmark performance, not real-world capability. <strong>Contamination</strong> means even that benchmark performance is often inflated by training-data overlap. <strong>The African / low-resource gap</strong> means the benchmarks are answering questions that are mostly not yours.</p>
    <p>None of this means benchmarks are useless. They are useful as a coarse comparison between current frontier models on the specific tasks they measure. They are not useful as a substitute for testing the model on your own work.</p>
  </div>

  <!-- SECTION: GOWERS -->
  <h2 class="section-title">&#128218; Centrepiece Reading: Gowers on ChatGPT 5.5 Pro</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Tim Gowers is a Fields medallist and a long-time chronicler of mathematical practice. In May 2026 he posted an account of an experiment in which he used ChatGPT 5.5 Pro to attack open problems from a paper by Mel Nathanson on additive number theory.</p>

  <div class="case-study">
    <h4>&#128221; What Gowers reports</h4>
    <p>Over roughly two hours of interaction, ChatGPT 5.5 Pro produced an original construction using <em>h&sup2;-dissociated sets</em> that improved the bounds on a function <em>N(h, k)</em> from exponential to polynomial in <em>k</em>. The construction was novel &mdash; not retrieved from training data &mdash; and Gowers describes it as &ldquo;quite impressive&rdquo;. Isaac Rajagopal, the original researcher who had been working on the problem, confirmed that the improvement was &ldquo;almost certainly correct&rdquo; at the level of ideas, not merely line-by-line.</p>
    <p>Gowers&#39; broader claim is striking: <em>&ldquo;The lower bound for contributing to mathematics will now be to prove something that LLMs can&#39;t prove.&rdquo;</em></p>
    <p>He pairs this with a defence of human work: <em>&ldquo;by solving hard problems you get an insight&hellip;that you simply don&#39;t if all you do is read other people&#39;s solutions.&rdquo;</em></p>
  </div>

  <div class="resource-placeholder">
    <h4>&#128214; Required Reading</h4>
    <p><strong><a href="https://gowers.wordpress.com/2026/05/08/a-recent-experience-with-chatgpt-5-5-pro/" target="_blank" rel="noopener">Gowers, T. (8 May 2026). <em>A recent experience with ChatGPT 5.5 Pro.</em></a></strong></p>
    <p>Read this before moving to the next sub-lesson. The full post is short, accessible without specialist additive-number-theory background, and lays the groundwork for the trajectory frame that runs through the rest of the week.</p>
  </div>

  <!-- SECTION: WHAT TO TAKE FROM 9.1 -->
  <h2 class="section-title">&#127919; The Move This Sub-Lesson Makes</h2>

  <div class="highlight-box">
    <h3>Date-stamp every claim about AI capability</h3>
    <p>From here on, when you encounter a claim about what AI can or cannot do &mdash; in this course, in published papers, in news articles, anywhere &mdash; reflexively check three things. <strong>Which model</strong> was tested? <strong>When</strong> was it tested? <strong>Has anyone retested</strong> with current frontier models?</p>
    <p>Without these three pieces of information, an AI capability claim has the same evidentiary status as a 2010 review of smartphone cameras. The category is right; the specifics are stale.</p>
    <p>Sub-lesson 9.2 takes this trajectory framing and applies it to specific failure modes. Some have been patched. Some have been reduced. Some are structural and likely permanent. Distinguishing them is the skill we are building.</p>
  </div>

  <div class="intro-text" style="margin-top: 50px;">
    <h2>&#128073; What Comes Next</h2>
    <p><strong>Sub-Lesson 9.2 &mdash; Three Categories of Failure: Patched, Reduced, Structural.</strong> A taxonomy of AI failures that survives the next model release. We use the trajectory frame from this sub-lesson to separate failures that have been fixed from failures that are inherent to how language models work.</p>
  </div>
"""


# ---------------------------------------------------------------------------
# Sub-Lesson 9.2 — Three Categories of Failure
# ---------------------------------------------------------------------------

SL2_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>If &ldquo;what AI can&#39;t do&rdquo; is a moving target, you need a way of organising failures that doesn&#39;t go stale every time a new model drops. This sub-lesson offers one: three categories that classify failures by how durable they are, not by which specific model exhibited them.</p>
    <p>The pay-off: when you encounter an AI failure in your own work, you can place it in the taxonomy. Failures in category (a) are diagnostic of model age &mdash; switch to a current frontier model and try again. Failures in category (b) require workflow design to manage. Failures in category (c) are structural and won&#39;t be fixed by the next release; they need verification protocols (Sub-Lesson 9.5).</p>
  </div>

  <!-- CATEGORY A -->
  <h2 class="section-title">&#9989; (a) Patched / Largely Solved</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">These were widely-cited failure modes in 2023&ndash;24 that have been substantially mitigated by current training pipelines. The original papers documenting them remain valuable as historical landmarks &mdash; but they no longer describe current frontier behaviour. Citing them as if they did is a common error in the recent AI literature.</p>

  <div class="card-grid">

    <div class="card">
      <h3>The Reversal Curse</h3>
      <p>In 2023, Berglund et al. showed that LLMs trained on facts of the form &ldquo;A is B&rdquo; failed to generalise to &ldquo;B is A&rdquo; &mdash; even when the inverse relationship was common in their training data. A model that knew &ldquo;Tom Cruise&#39;s mother is Mary Lee Pfeiffer&rdquo; would not reliably answer &ldquo;Who is Mary Lee Pfeiffer&#39;s son?&rdquo;</p>
      <p>By 2026, this failure mode is no longer prominent in benchmark discussions. Training-data interventions and inference-time techniques have substantially mitigated it in frontier models. Still cited in the literature, but largely as a historical landmark.</p>
      <p style="font-size: 0.9em; color: #003A70; font-weight: 600;">Original: <a href="https://arxiv.org/abs/2309.12288" target="_blank" rel="noopener">Berglund, L., Tong, M., Kaufmann, M., et al. (2023). The Reversal Curse. arXiv:2309.12288</a></p>
    </div>

    <div class="card">
      <h3>Basic Arithmetic and Short-Form Reasoning</h3>
      <p>In 2023, Frieder et al. tested ChatGPT and GPT-4 on graduate-level mathematics and found them mostly inadequate. The paper became a touchstone for &ldquo;LLMs can&#39;t do real maths&rdquo; arguments. By May 2026 this is thoroughly superseded: GPT-5.5 Pro scores 52.4% on FrontierMath (research-level problems set by Fields medallists), Gemini Deep Think scored 35/42 at IMO 2025, and several Erd&#337;s problems have been solved with frontier-model assistance (see 9.3).</p>
      <p style="font-size: 0.9em; color: #003A70; font-weight: 600;">Original: <a href="https://arxiv.org/abs/2301.13867" target="_blank" rel="noopener">Frieder, S., Pinchetti, L., et al. (2023). Mathematical Capabilities of ChatGPT. NeurIPS 2023</a></p>
    </div>

    <div class="card">
      <h3>Hallucinated Code on Common Tasks</h3>
      <p>In 2023, asking a model for code in a popular library would frequently produce calls to functions that didn&#39;t exist. By 2026, frontier models pass SWE-bench Verified above 87% &mdash; meaning they correctly resolve real GitHub issues. The hallucination of function signatures has been largely mitigated for well-documented libraries; it persists for niche or proprietary APIs (which moves it into category b).</p>
    </div>

  </div>

  <div class="info-box">
    <h4>&#128218; The Skill Being Taught</h4>
    <p>When reading a 2023&ndash;24 paper that says &ldquo;AI cannot do X&rdquo;, ask: has the same X been retested with current frontier models? If yes, what did the retest find? If no, the claim is unproven on current systems and should be cited cautiously, with the model and date explicit.</p>
  </div>

  <!-- CATEGORY B -->
  <h2 class="section-title">&#128737;&#65039; (b) Reduced but Persistent</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">These failures have been mitigated but still surface, especially under specific conditions. Frontier models behave better than 2023&ndash;era models, but not so well that you can stop checking. These are the failure modes most relevant to research workflows in 2026.</p>

  <h3 style="color: #2a5298; font-size: 1.4em; margin: 30px 0 15px;">Hallucinated Citations</h3>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Even frontier models in 2026 hallucinate citations on niche topics. The Week 5 evidence remains directly relevant:</p>

  <ul class="styled-list">
    <li><strong>Magesh et al. (2024).</strong> <em>Hallucination-Free?</em> arXiv:2405.20362. Stanford HAI. Lexis+ AI, Westlaw, and Ask Practical Law: <strong>17&ndash;33%</strong> hallucination on benchmarking queries &mdash; despite vendor marketing as &ldquo;hallucination-free&rdquo;.</li>
    <li><strong>Chelli et al. (2024).</strong> <em>JMIR</em> 26: e53164. GPT-3.5 39.6%, GPT-4 28.6%, Bard 91.4%.</li>
    <li><strong>Linardon et al. (2025).</strong> <em>JMIR Mental Health</em> 12: e80371. GPT-4o: 19.9% overall; <strong>28&ndash;29% on niche topics</strong>; 6% on well-studied. Citation hallucination correlates with how rare the topic is in training data.</li>
  </ul>

  <p style="color: #555; line-height: 1.75; margin-top: 15px; margin-bottom: 15px;">In 2026 these rates have dropped further on common topics but the long-tail problem persists: the rarer a topic is in training data, the more likely AI is to hallucinate when asked about it. For research that touches the long tail by definition, citation verification is non-negotiable.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">A vivid current data point: Ant Group&#39;s <strong>Ling 2.6 1T</strong> (April 2026), a 1-trillion-parameter open-weights model targeted at cost-efficient inference, scores around 34 on Artificial Analysis&#39;s Intelligence Index but reports a <strong>92% hallucination rate on the AA-Omniscience benchmark</strong> (<a href="https://artificialanalysis.ai/articles/aa-omniscience-knowledge-hallucination-benchmark" target="_blank" rel="noopener">Artificial Analysis</a>; methodology paper <a href="https://arxiv.org/abs/2511.13029" target="_blank" rel="noopener">arXiv:2511.13029</a>). The hallucination problem is unevenly addressed across the open-weights frontier; not every recent release inherits the mitigations from the leading labs.</p>

  <h3 style="color: #2a5298; font-size: 1.4em; margin: 30px 0 15px;">Sycophancy</h3>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Sharma et al. (2023) documented that RLHF-trained models tend to agree with users even when the user is wrong &mdash; a behaviour driven in part by human preference judgements favouring agreement. Anthropic and other labs have invested heavily in mitigations:</p>

  <ul class="styled-list">
    <li><strong>Constitutional AI</strong> trains the model to evaluate its own outputs against principles including honesty and calibrated confidence (Week 2).</li>
    <li><strong>DPO with sycophancy-labelled preference pairs</strong> directly penalises sycophantic responses while preserving instruction-following.</li>
    <li><strong>Persona-vector interpretability methods</strong> extract activation patterns associated with traits like sycophancy and intervene at inference time.</li>
  </ul>

  <p style="color: #555; line-height: 1.75; margin-top: 15px; margin-bottom: 15px;">Sycophancy is reduced in frontier 2026 models &mdash; but it reappears under specific conditions: long conversations, emotional framing, expert-claimed user identities, and pushback against initial AI outputs. If you want a frontier model to tell you it&#39;s wrong, you need to ask in a way that doesn&#39;t signal what answer you want.</p>

  <div class="case-study" style="margin-top: 20px;">
    <h4>&#128221; A May 2026 anecdote: model overconfidence on a maths disagreement</h4>
    <p>An informal but instructive comparison from researcher @giffmana: presented with a pair of mathematical formulas that appeared to disagree, three frontier models behaved very differently. Claude Opus 4.6 confidently defended a wrong proof and resisted correction even with pushback. ChatGPT Pro reconciled the two formulas correctly but offered the result without much interpretation. Muse Spark did both &mdash; reconciled the formulas and explained why the apparent disagreement dissolved.</p>
    <p>Anecdotal, single-case, not a benchmark. But it&#39;s a useful illustration that overconfident defence of wrong reasoning &mdash; the sycophancy/calibration failure mode &mdash; is still surfacing in mid-2026 frontier models, and that the failure mode is not uniformly distributed across the frontier. If you want to detect it in your own work, ask the same question of multiple frontier models and notice where they disagree (cross-model triangulation, Sub-Lesson 9.5).</p>
  </div>

  <p style="font-size: 0.9em; color: #003A70; font-weight: 600; margin-top: 15px;">Original sycophancy paper: <a href="https://arxiv.org/abs/2310.13548" target="_blank" rel="noopener">Sharma, M., Tong, M., Korbak, T., et al. (2023). Towards Understanding Sycophancy in Language Models. ICLR 2024 / arXiv:2310.13548</a></p>

  <h3 style="color: #2a5298; font-size: 1.4em; margin: 30px 0 15px;">Calibration</h3>

  <p style="color: #555; line-height: 1.75;">Frontier models are still over-confident. The probability they assign to an answer being correct does not reliably match the actual accuracy. Calibration has improved over time, but a 90%-confident answer may be right 75% of the time, and a 60%-confident answer may be right 80%. This makes confidence-thresholded workflows less useful than you might hope &mdash; you can&#39;t simply &ldquo;ask the model only when it&#39;s sure&rdquo;.</p>

  <!-- CATEGORY C -->
  <h2 class="section-title">&#129518; (c) Structural and Likely Persistent</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">These failures follow from how LLMs work, not from training-data quirks. They are unlikely to be solved by the next model release because they are properties of the architecture or the training paradigm. Verification protocols (Sub-Lesson 9.5) target these specifically.</p>

  <div class="card-grid">

    <div class="card">
      <h3>Hallucination as Statistical Pressure</h3>
      <p>OpenAI&#39;s own analysis: hallucinations originate as binary-classification errors and persist because evaluations reward confident guessing over acknowledging uncertainty. The proposed fix is socio-technical &mdash; change how benchmarks score uncertainty &mdash; not architectural.</p>
      <p>The argument: <em>&ldquo;Hallucinations need not be mysterious &mdash; they originate simply as errors in binary classification.&rdquo;</em></p>
      <p style="font-size: 0.9em; color: #003A70; font-weight: 600;">Source: <a href="https://arxiv.org/abs/2509.04664" target="_blank" rel="noopener">Kalai, A. T., Nachum, O., Vempala, S. S., &amp; Zhang, E. (Sept 2025). Why Language Models Hallucinate. arXiv:2509.04664</a></p>
    </div>

    <div class="card">
      <h3>Pattern Completion vs Understanding</h3>
      <p>LLMs predict next tokens. Whether this constitutes &ldquo;understanding&rdquo; in any deeper sense is a philosophical question, but the practical implication is concrete: a model can produce correct output via shortcuts that don&#39;t generalise. This is the foundation for the <em>illusions of understanding</em> argument we develop in Sub-Lesson 9.4 (Messeri &amp; Crockett, Nature 2024).</p>
    </div>

    <div class="card">
      <h3>The Long-Tail Problem</h3>
      <p>Performance degrades on rare topics regardless of model scale. Frontier models in 2026 are excellent on widely-discussed topics and worse on niche ones &mdash; exactly where novel research happens. Niimi (2025), cited in Week 5, demonstrated that bibliographic hallucination rates correlate strongly with how often a paper appears in training data. This effect compounds at the frontier of any field.</p>
    </div>

    <div class="card">
      <h3>Compositional Brittleness</h3>
      <p>The &ldquo;silent error&rdquo; theme from Week 7. Each step of an AI-generated analysis can be plausible while the end result is wrong. This is not solved by making each step more accurate, because compositional errors compound multiplicatively. Long agentic chains amplify the problem.</p>
      <p style="margin-top: 10px;">Concrete current example: <strong>FoodTruck Bench (2026)</strong> tests real-world multi-step agentic tasks. Even DeepSeek V4 Pro &mdash; competitive with the closed frontier on most single-step benchmarks &mdash; struggles substantially. Individual capabilities (writing code, calling tools, parsing documents) keep improving; chaining them reliably remains hard. This is the failure mode that scales worst as agentic systems get longer.</p>
    </div>

    <div class="card">
      <h3>Domain-Specific Failure Modes</h3>
      <p>Even frontier models fail differently in different fields, regardless of overall benchmark score. A model excellent at theoretical physics may be brittle on Renaissance history. Aggregate benchmarks don&#39;t predict performance in your specific domain. This is why the hands-on activities (9.6) ask you to test capability in your own field rather than rely on published numbers.</p>
    </div>

    <div class="card">
      <h3>Training Data Dependence</h3>
      <p>Models can only know what was in their training data. They will confidently answer questions about events after their training cutoff using outdated information. They may have been trained on a biased sample of the literature in your field. This dependence is structural &mdash; it doesn&#39;t go away with more parameters or better RLHF.</p>
    </div>

  </div>

  <div class="resource-placeholder">
    <h4>&#128214; Background Reading</h4>
    <p><strong><a href="https://normaltech.ai/" target="_blank" rel="noopener">Kapoor, S., &amp; Narayanan, A. (ongoing). normaltech.ai</a></strong> &mdash; the blog formerly known as <em>AI Snake Oil</em>. The structural-failures position; argues that many AI capability claims are overstated and many failures are structural rather than version-specific. The 2024 Princeton UP book <em>AI Snake Oil</em> is a longer version of the argument.</p>
    <p style="margin-top: 10px;"><strong><a href="https://arxiv.org/abs/2509.04664" target="_blank" rel="noopener">Kalai, A. T., Nachum, O., Vempala, S. S., &amp; Zhang, E. (Sept 2025). <em>Why Language Models Hallucinate.</em> arXiv:2509.04664</a></strong> &mdash; OpenAI&#39;s technical paper on the structural origins of hallucination. Reading both Kapoor &amp; Narayanan and Kalai et al. gives you views from outside and inside the labs respectively.</p>
  </div>

  <!-- DIAGNOSTIC TABLE -->
  <h2 class="section-title">&#129534; Putting the Taxonomy to Work</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Here&#39;s how the taxonomy plays out for failures you might actually encounter in research workflows. When you observe a failure, locate it in this table:</p>

  <div style="overflow-x: auto;">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Observed Failure</th>
          <th>Category</th>
          <th>Diagnosis &amp; Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Model fails on simple arithmetic in your prompt</td>
          <td>Patched</td>
          <td>You&#39;re using an old model. Switch to a current frontier (Opus 4.7, GPT-5.5, etc.) and try again.</td>
        </tr>
        <tr>
          <td>Model produces a confident citation that doesn&#39;t exist on a niche topic</td>
          <td>Reduced but persistent</td>
          <td>Run the Five-Point Citation Check from Week 5. Don&#39;t skip verification because the model sounded confident.</td>
        </tr>
        <tr>
          <td>Model agrees with your hypothesis after you express attachment to it</td>
          <td>Reduced but persistent</td>
          <td>Sycophancy. Re-prompt without signalling your preferred answer; cross-check with a different model.</td>
        </tr>
        <tr>
          <td>Model produces code that runs perfectly but gives wrong numerical results</td>
          <td>Structural (compositional)</td>
          <td>The Week 7 silent-error problem. Verification with known-answer testing is mandatory.</td>
        </tr>
        <tr>
          <td>Model gives you summary statistics on a topic that look reasonable but on inspection are wrong</td>
          <td>Structural (long tail)</td>
          <td>You&#39;ve hit the long-tail problem. Verify against primary sources; consider whether the model&#39;s training data covers your topic adequately.</td>
        </tr>
        <tr>
          <td>Model is excellent in one of your domains and brittle in another</td>
          <td>Structural (domain-specific)</td>
          <td>Test capability in each domain you use AI in. Don&#39;t generalise from one domain&#39;s reliability to another&#39;s.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="highlight-box">
    <h3>The skill is the taxonomy, not the specific examples</h3>
    <p>The specific examples in this sub-lesson will date. The reversal curse will eventually be a footnote that no one cites. New patched failures will replace it. The structural-failures list may grow or shrink as research clarifies what is fundamental and what is not.</p>
    <p>What persists is the question you ask when you encounter a failure: <em>is this patched, reduced-but-persistent, or structural?</em> The answer determines what you do about it.</p>
  </div>

  <div class="intro-text" style="margin-top: 50px;">
    <h2>&#128073; What Comes Next</h2>
    <p><strong>Sub-Lesson 9.3 &mdash; Where AI Is Now Genuinely Strong.</strong> Having looked at the trajectory and the failure taxonomy, we now look at the other side: what current frontier models are genuinely good at, with concrete examples from mathematics and theoretical physics in 2026. Many students underestimate AI in some directions; recalibration is the work.</p>
  </div>
"""


# ---------------------------------------------------------------------------
# Sub-Lesson 9.3 — Where AI Is Now Genuinely Strong
# ---------------------------------------------------------------------------

SL3_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>The trajectory frame from 9.1 cuts both ways. If you arrive thinking AI is more capable than it is, you over-rely on it. If you arrive thinking AI is less capable than it is, you miss things you could be doing. Both errors are common. This sub-lesson focuses on the second.</p>
    <p>We look at concrete cases from 2025&ndash;26 where AI played a pivotal role in research-grade work in mathematics, theoretical physics, and beyond. The examples are deliberately drawn from fields where, two years ago, the consensus was that AI couldn&#39;t contribute meaningfully. The point is not that AI replaces researchers in these fields &mdash; in every case, human collaboration was essential and human verification was mandatory &mdash; but that the ceiling has moved.</p>
    <p>A pedagogical caveat to flag now: these are <strong>selection-biased examples</strong>. They are the cases where AI worked. The ratio of attempts-to-successes is unknown. We close the sub-lesson with the caveats; read them.</p>
  </div>

  <!-- MATHEMATICS -->
  <h2 class="section-title">&#10135; Mathematics</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">If there is one field where 2026 has decisively shifted, it is mathematics. The combination of frontier reasoning models (GPT-5.4 Pro, GPT-5.5 Pro, Gemini Deep Think) and tools that connect them to formal verification (AlphaProof, AlphaEvolve) has produced a stream of contributions to research-level problems.</p>

  <div class="case-study">
    <h4>&#128221; Erd&#337;s Problems Solved with Frontier Models</h4>
    <p>Since January 2026, <strong>15 Erd&#337;s problems have moved from &ldquo;open&rdquo; to &ldquo;solved&rdquo;</strong> on the canonical Erd&#337;s problem database, with <strong>11 of those crediting AI models</strong> as part of the process. The contributions are tracked at <a href="https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems" target="_blank" rel="noopener">github.com/teorth/erdosproblems</a>.</p>
    <p><strong>Erd&#337;s Problem #1196.</strong> A 1968 conjecture from Erd&#337;s, S&aacute;rk&ouml;zy and Szemer&eacute;di on primitive sets. Solved by GPT-5.4 Pro on 13 April 2026, with a solution that includes a Lean formalisation. A peer-reviewed-track follow-up paper extends the result substantially: <strong><a href="https://arxiv.org/abs/2605.00301" target="_blank" rel="noopener">Alexeev, B., Barreto, K., Li, Y., Lichtman, J. D., Price, L., Shah, J. I., Tang, Q., &amp; Tao, T. (3 May 2026). <em>Primitive sets and von Mangoldt chains: Erd&#337;s Problem #1196 and beyond.</em> arXiv:2605.00301</a></strong>.</p>
    <p><strong>Erd&#337;s Problem #728.</strong> Solved by GPT-5.4 Pro in approximately 80 minutes from a single prompt. Tao&#39;s commentary: <em>&ldquo;the proof reveals a previously undescribed connection between the anatomy of integers and Markov process theory.&rdquo;</em> A meaningful contribution to the field that goes well beyond the specific problem.</p>
  </div>

  <div class="case-study">
    <h4>&#128221; Mathematical Exploration at Scale</h4>
    <p><strong><a href="https://arxiv.org/abs/2511.02864" target="_blank" rel="noopener">Georgiev, B., G&oacute;mez-Serrano, J., Tao, T., &amp; Wagner, A. Z. (3 November 2025). <em>Mathematical exploration and discovery at scale.</em> arXiv:2511.02864</a></strong></p>
    <p>Tao and collaborators tested Google&#39;s AlphaEvolve &mdash; an evolutionary coding agent that combines an LLM with automated evaluation &mdash; on 67 mathematical problems across analysis, combinatorics, geometry, and number theory. The system rediscovered established solutions in most cases and identified <strong>improved solutions on several</strong>. The authors integrated AlphaEvolve with Deep Think and AlphaProof for proof generation. Tao&#39;s blog post on the paper at <a href="https://terrytao.wordpress.com/2025/11/05/mathematical-exploration-and-discovery-at-scale/" target="_blank" rel="noopener">terrytao.wordpress.com</a> is a useful accessible summary.</p>
  </div>

  <div class="case-study">
    <h4>&#128221; DeepMind&#39;s AI Co-Mathematician (May 2026)</h4>
    <p>Announced on 8 May 2026 by Pushmeet Kohli&#39;s team at Google DeepMind, the AI Co-Mathematician is a multi-agent system built on Gemini 3.1 Pro that actively collaborates with human mathematicians on open research problems.</p>
    <p>On <strong>FrontierMath Tier 4</strong> &mdash; the hardest 50 problems in the benchmark, designed to take expert mathematicians hours or days &mdash; the system <strong>solved 23 of 48 non-public problems, a 48% accuracy rate</strong>. The base model alone (Gemini 3.1 Pro) scored 19% on the same benchmark; the entire jump came from agentic scaffolding with parallel agents reviewing each other&#39;s work.</p>
    <p>And it has already been used to close a real open problem: topologist Marc Lackenby used the system to close <strong>problem 21.10 from the Kourovka Notebook</strong>, an open compendium of group theory problems maintained continuously since 1965 in Novosibirsk.</p>
    <p style="font-size: 0.9em; color: #003A70; font-weight: 600;">Source: <a href="https://arxiv.org/abs/2605.06651" target="_blank" rel="noopener">AI Co-Mathematician: Accelerating Mathematicians with Agentic AI (arXiv:2605.06651, 7 May 2026)</a></p>
  </div>

  <div class="case-study">
    <h4>&#128221; IMO 2025 &mdash; Gold Medal in Natural Language</h4>
    <p>An advanced version of <strong>Gemini with Deep Think</strong> achieved gold-medal performance at the 2025 International Mathematical Olympiad: <strong>5 out of 6 problems perfect, 35/42 points</strong>, end-to-end natural-language proofs (not formal Lean), within the official 4.5-hour competition window. This is up from 2024, when AlphaProof + AlphaGeometry 2 took silver requiring expert formalisation into Lean and 2&ndash;3 days of computation. One year, formalisation overhead removed, time pressure met.</p>
  </div>

  <h3 style="color: #2a5298; font-size: 1.4em; margin: 30px 0 15px;">Centrepiece reading (revisited)</h3>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">If you have not yet read it, return to <strong><a href="https://gowers.wordpress.com/2026/05/08/a-recent-experience-with-chatgpt-5-5-pro/" target="_blank" rel="noopener">Gowers (May 2026), <em>A recent experience with ChatGPT 5.5 Pro</em></a></strong>. The Gowers post is the single most useful piece of writing I know on the current state of frontier-model mathematics, partly because Gowers is one of the few people who can credibly assess the quality of the work himself.</p>

  <!-- THEORETICAL PHYSICS -->
  <h2 class="section-title">&#9883; Theoretical Physics</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The theoretical physics cases are particularly notable because they involve named senior physicists collaborating directly with AI on amplitude calculations. The work has appeared as preprints with credentialed authors, not as AI-lab demonstrations.</p>

  <div class="case-study">
    <h4>&#128221; Single-Minus Gluon Amplitudes &mdash; OpenAI &times; Strominger Group</h4>
    <p><strong><a href="https://arxiv.org/abs/2602.12176" target="_blank" rel="noopener">Guevara, A., Lupsasca, A., Skinner, D., Strominger, A., &amp; Weil, K. (12 February 2026). <em>Single-minus gluon tree amplitudes are nonzero.</em> arXiv:2602.12176</a></strong></p>
    <p>The paper&#39;s own abstract is explicit about the AI contribution:</p>
    <p style="font-style: italic; color: #444; margin: 15px 0; padding: 12px 18px; border-left: 3px solid #003A70; background: #f9f9f9;">&ldquo;The key formula was first conjectured by GPT-5.2 Pro and then proved by a new internal OpenAI model.&rdquo;</p>
    <p>Human verification was mandatory: the proof was checked by hand using the Berends&ndash;Giele recursion and tested against multiple consistency conditions including Weinberg&#39;s soft theorem. The author list includes Andrew Strominger (Harvard) &mdash; among the most distinguished living theoretical physicists &mdash; and Kevin Weil on behalf of OpenAI. This is not an AI-lab demonstration; it is a real preprint with a real result.</p>
  </div>

  <div class="case-study">
    <h4>&#128221; Graviton Extension</h4>
    <p>The same group extended the gluon result to <em>gravitons</em> in March 2026. Currently hosted at <a href="https://openai.com/index/extending-single-minus-amplitudes-to-gravitons/" target="_blank" rel="noopener">openai.com/index/extending-single-minus-amplitudes-to-gravitons/</a> (PDF at <a href="https://cdn.openai.com/pdf/graviton.pdf" target="_blank" rel="noopener">cdn.openai.com/pdf/graviton.pdf</a>); arXiv version not yet posted at time of writing. The extension used the gluon results as context plus some guidance from the human physicists; GPT-5.2 Pro constructed the analogous single-minus scattering amplitudes for gravitons.</p>
  </div>

  <div class="case-study">
    <h4>&#128221; Cosmic-String Gravitational Radiation</h4>
    <p><strong><a href="https://arxiv.org/abs/2603.04735" target="_blank" rel="noopener">Brenner, M. P., Cohen-Addad, V., &amp; Woodruff, D. (5 March 2026). <em>Solving an Open Problem in Theoretical Physics using AI-Assisted Discovery.</em> arXiv:2603.04735</a></strong></p>
    <p>A neuro-symbolic system &mdash; Gemini Deep Think combined with a tree-search framework and automated numerical feedback &mdash; computed the power spectrum of gravitational radiation emitted by cosmic strings. The system discovered <strong>six different analytical methods</strong>; the most elegant uses Gegenbauer-polynomial expansions and is exact and efficient. Of growing relevance given recent Pulsar Timing Array observations of the stochastic gravitational background.</p>
  </div>

  <div class="case-study">
    <h4>&#128221; Quantum Many-Body Calculations</h4>
    <p><strong><a href="https://www.nature.com/articles/s42005-025-01956-y" target="_blank" rel="noopener">Pan, H., Mudur, N., Taranto, W., Tikhanovskaya, M., Venugopalan, S., Bahri, Y., Brenner, M. P., &amp; Kim, E.-A. (2025). <em>Quantum many-body physics calculations with large language models.</em> Communications Physics. DOI:10.1038/s42005-025-01956-y</a></strong></p>
    <p>Tested GPT-4 on 15 quantum many-body papers from the past decade. With multi-step prompt templates, the model correctly derived the final Hartree&ndash;Fock Hamiltonian in <strong>13 of 15</strong> cases. The first systematic evaluation of LLMs on research-level physics calculations &mdash; and a result obtained even before the GPT-5 generation. Pre-registered prompt templates and step-by-step verification matter as much as model capability.</p>
  </div>

  <!-- OTHER PARADIGMS -->
  <h2 class="section-title">&#129504; Adjacent Paradigms (Not LLM-based)</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Not all of the AI-in-science story is LLMs. Two notable 2025 results use different machine-learning paradigms entirely. They are worth knowing because the limits of LLMs are not the limits of AI.</p>

  <div class="card-grid">

    <div class="card">
      <h3>AI-Newton (Symbolic Discovery)</h3>
      <p>Fang, Y.-L., Jian, D.-S., Li, X., &amp; Ma, Y.-Q. (April 2025). <em>AI-Newton: A Concept-Driven Physical Law Discovery System without Prior Physical Knowledge</em>. <a href="https://arxiv.org/abs/2504.01538" target="_blank" rel="noopener">arXiv:2504.01538</a>. From Peking University. Symbolic regression that, given experimental data, autonomously rediscovers Newton&#39;s second law, energy conservation, and the law of gravitation &mdash; without prior physics knowledge built in.</p>
    </div>

    <div class="card">
      <h3>Physics-Tailored ML in Dusty Plasmas</h3>
      <p>Yu, W., Abdelaleem, E., Nemenman, I., &amp; Burton, J. C. (2025). <em>Physics-tailored machine learning reveals unexpected physics in dusty plasmas.</em> <em>PNAS</em> 122(31), e2505725122. <a href="https://www.pnas.org/doi/10.1073/pnas.2505725122" target="_blank" rel="noopener">DOI:10.1073/pnas.2505725122</a>. Custom neural network trained on dusty-plasma trajectory data infers non-reciprocal forces with R&sup2; &asymp; 0.99. From Emory University. Demonstrates that physics-aware ML can rediscover laws and even reveal new ones from carefully-designed experiments.</p>
    </div>

  </div>

  <!-- AGENTIC RESEARCH -->
  <h2 class="section-title">&#129302; Autonomous Research Pipelines</h2>

  <div class="case-study">
    <h4>&#128221; The AI Scientist v2 &mdash; First AI-Authored Peer-Reviewed Paper</h4>
    <p><strong><a href="https://www.nature.com/articles/s41586-026-10265-5" target="_blank" rel="noopener">Lu, C., Lu, C., Lange, R. T., et al. (26 March 2026). <em>Towards end-to-end automation of AI research.</em> Nature 651, 914&ndash;919. DOI:10.1038/s41586-026-10265-5</a></strong></p>
    <p>Sakana AI&#39;s second-generation AI Scientist &mdash; agentic tree search, no human-authored code templates &mdash; produced three manuscripts that were submitted to a peer-reviewed workshop at ICLR 2025. <strong>One manuscript passed peer review with an average reviewer score of 6.33</strong>, placing it in roughly the top 45% of submissions. Sakana withdrew the paper before final publication, but the milestone &mdash; first fully AI-generated paper to pass rigorous human peer review &mdash; is real. Includes important caveats about generality and replicability.</p>
  </div>

  <!-- CODE AND OTHER DOMAINS -->
  <h2 class="section-title">&#128187; Code, Writing, and Other Domains</h2>

  <div class="card-grid">

    <div class="card">
      <h3>Code at the Frontier</h3>
      <p><strong>Claude Opus 4.7</strong> at SWE-bench Verified 87.6%; <strong>DeepSeek V4 Pro</strong> at Codeforces 3206 (top of any model); <strong>GPT-5.5 Pro</strong> at MCP-Atlas 77.3%. Frontier models in 2026 are research-grade for many programming tasks. The Week 7 caveat applies: code that runs is not code that&#39;s correct. Verification and known-answer testing are still mandatory.</p>
    </div>

    <div class="card">
      <h3>Scientific Writing</h3>
      <p>Capability has improved substantially. Frontier models produce drafts that read like academic prose without obvious AI tells. The Week 6 caveats apply: AI suggestions homogenise writing toward Western styles (Agarwal, Naaman &amp; Vashistha, CHI 2025); citation hallucination rates remain non-zero; the &ldquo;writing as thinking&rdquo; concern is more important now, not less.</p>
    </div>

    <div class="card">
      <h3>Multimodal</h3>
      <p>Pointer to Week 8. Frontier models in 2026 can describe scientific figures, transcribe audio (with hallucination caveats), parse complex documents, and process video. The capability is real; the verification overhead remains substantial.</p>
    </div>

  </div>

  <!-- THE CAVEATS -->
  <h2 class="section-title">&#9888;&#65039; Essential Caveats</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Read these. Without them, the cases above can be miscalibrated as &ldquo;AI now does mathematics and physics autonomously&rdquo;. That is not the claim being made.</p>

  <div class="warning-box">
    <h4>1. Selection Bias</h4>
    <p>Every case above is one where AI worked. The ratio of attempts-to-successes is unknown. For every Erd&#337;s problem solved, dozens may have been attempted with no result. For every gluon-amplitude formula correctly conjectured, an unknown number of incorrect ones were rejected. The Gowers post itself is honest about this: ChatGPT&#39;s initial outputs were &ldquo;rambling&rdquo; and required multiple iterations.</p>
  </div>

  <div class="warning-box">
    <h4>2. Human Collaboration Was Essential in Every Single Case</h4>
    <p>The gluon-amplitude paper required Strominger and colleagues to feed GPT-5.2 specific human-computed cases as a starting point. The Erd&#337;s solutions required follow-up work to formalise and extend. The IMO gold required problem-statements to be presented in their canonical form. The Gowers experiment required Gowers&#39; expertise to evaluate what the model had produced. These are all <em>collaborations</em>, not autonomous discovery. Reading them as &ldquo;AI did mathematics&rdquo; misses the structure.</p>
  </div>

  <div class="warning-box">
    <h4>3. Human Verification Was Always Required</h4>
    <p>Even when the AI&#39;s contribution was substantial, the proof was checked by humans. The Lean formalisations of the Erd&#337;s solutions provided machine-checkable verification. The Berends&ndash;Giele recursion check on the gluon formula was done by hand. The cosmic-string-radiation result was tested numerically against existing partial solutions. <em>Hallucination remains a real risk in any AI mathematical or physical output.</em> The verification step is not optional.</p>
  </div>

  <div class="warning-box">
    <h4>4. Several of These Are Preprints, Not Yet Peer-Reviewed</h4>
    <p>The gluon and graviton papers are arXiv (and OpenAI-hosted) preprints. Several of the Erd&#337;s solutions are documented in forum posts and follow-up arXiv papers but have not all completed formal peer review. Some may not survive review unchanged. The status as of May 2026 is provisional, not consensus.</p>
  </div>

  <!-- CLOSING -->
  <div class="highlight-box">
    <h3>What this sub-lesson asks of you</h3>
    <p>Update your calibration. If your prior on &ldquo;AI in mathematics&rdquo; was based on Frieder et al. (2023), look at Gowers (2026), Erd&#337;s #1196, and the IMO 2025 gold. If your prior on &ldquo;AI in theoretical physics&rdquo; was &ldquo;not really&rdquo;, look at the gluon paper.</p>
    <p>And: hold the calibration loosely. The structural failures from 9.2 are still operative in every case above. The ceiling has moved; the floor of verification has not.</p>
    <p>In your own field: test current frontier models on tasks you assumed they couldn&#39;t do. The activities in 9.6 ask you to do exactly this.</p>
  </div>

  <div class="intro-text" style="margin-top: 50px;">
    <h2>&#128073; What Comes Next</h2>
    <p><strong>Sub-Lesson 9.4 &mdash; Illusions of Understanding.</strong> Having now seen both what AI fails at (9.2) and what it&#39;s now genuinely good at (9.3), we turn to a deeper question: when AI is right, do <em>you</em> understand the result? The Messeri &amp; Crockett (2024, <em>Nature</em>) framework is the centrepiece.</p>
  </div>
"""


# ---------------------------------------------------------------------------
# Sub-Lesson 9.4 — Illusions of Understanding
# ---------------------------------------------------------------------------

SL4_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>Versions of AI come and go. The capabilities listed in 9.1 will date within months. The patched failures in 9.2(a) will be replaced by new patched failures. The strong cases in 9.3 will be joined by new strong cases.</p>
    <p>What does <em>not</em> date as fast is the deeper question of what happens to <em>your own understanding</em> when AI is doing more of the cognitive work in your research. That question is the subject of this sub-lesson, and its centrepiece is Messeri &amp; Crockett&#39;s 2024 <em>Nature</em> paper, which lays out four distinct illusions of understanding that AI use can produce.</p>
    <p>The argument is durable because it is about epistemics, not about specific model behaviour. A frontier 2030 model that&#39;s right 99% of the time will produce these illusions <em>more</em> easily, not less.</p>
  </div>

  <!-- THE PAPER -->
  <h2 class="section-title">&#128218; Messeri &amp; Crockett: The Four Illusions</h2>

  <div class="resource-placeholder">
    <h4>&#128214; Required Reading (Centrepiece)</h4>
    <p><strong><a href="https://www.nature.com/articles/s41586-024-07146-0" target="_blank" rel="noopener">Messeri, L. &amp; Crockett, M. J. (2024). <em>Artificial intelligence and illusions of understanding in scientific research.</em> Nature 627, 49&ndash;58.</a></strong> DOI:10.1038/s41586-024-07146-0.</p>
    <p>A 10-page <em>Nature</em> Perspective. Read in full before working through the sub-lesson; the four illusions below summarise but do not replace the original argument.</p>
  </div>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Messeri (Yale, anthropology) and Crockett (Princeton, neuroscience) argue that AI use in research generates four specific illusions of understanding. Each looks like progress; each can mask a real loss of epistemic ground.</p>

  <div class="card-grid">

    <div class="card">
      <h3>1. Illusion of Explanatory Breadth</h3>
      <p>Researchers using AI to summarise a literature feel they&#39;ve covered the field comprehensively. They haven&#39;t. The AI summary reflects which sources are well-represented in training data, which papers attracted attention, which arguments propagate easily. Marginal voices, dissenting views, and recent work all systematically under-appear. The feeling of breadth is real; the breadth is not.</p>
    </div>

    <div class="card">
      <h3>2. Illusion of Exploratory Objectivity</h3>
      <p>AI outputs feel neutral &mdash; they don&#39;t come with a visible agenda. But they inherit the biases of training data, the values encoded by RLHF, the framings the model finds most natural. The neutrality is performative, not actual. A researcher using AI to generate hypotheses thinks they are exploring without prejudice; they are exploring the priors of the model.</p>
    </div>

    <div class="card">
      <h3>3. Monocultures of Knowing</h3>
      <p>If everyone in a field uses the same frontier models, ideas and framings homogenise. Different researchers asking similar questions of the same model get convergent answers. The field becomes <em>narrower</em> in its diversity of approaches, even as it produces more output. Connect to the &ldquo;scientific monoculture&rdquo; finding in Week 6 (Traberg, Roozenbeek &amp; van der Linden, <em>Communications Psychology</em>, 2026): AI use by researchers is measurably narrowing the diversity of ideas in circulation.</p>
    </div>

    <div class="card">
      <h3>4. Doing More But Understanding Less</h3>
      <p>AI accelerates output. More papers can be written, more analyses run, more literature reviewed. But the cognitive work that produces deep understanding &mdash; the slow grappling with a problem, the dead-ends that turn out to matter, the synthesis that emerges from struggle &mdash; can be skipped. Output rises; depth falls. Connect to Week 6&#39;s &ldquo;writing as thinking&rdquo; argument and Kosmyna et al. (2025)&#39;s MIT Media Lab study showing reduced neural engagement in AI-assisted essay writing.</p>
    </div>

  </div>

  <div class="case-study">
    <h4>&#128221; A 2026 Concrete Example: &ldquo;Vibe Coding&rdquo;</h4>
    <p>The term &ldquo;vibe coding&rdquo; has emerged in 2025&ndash;26 to describe a development style in which programmers describe what they want to an AI assistant in plain English and accept the output without deeply reading the resulting code. The AI handles the syntax; the human handles the intent.</p>
    <p>For straightforward tasks &mdash; quick scripts, well-trodden patterns &mdash; this is genuinely productive. For research code, it produces exactly the illusion Messeri &amp; Crockett describe: <em>output rises (more analyses run, more pipelines built), depth falls (the developer&#39;s actual understanding of what the code is doing in detail is shallower than it would have been if they had written it themselves)</em>.</p>
    <p>This connects directly to the &ldquo;silent error&rdquo; problem from Week 7: code that runs without errors but produces wrong results is precisely the failure mode that vibe coding amplifies. If you don&#39;t read the code closely, you don&#39;t catch the silent errors. The illusion of doing analysis is real; the analysis itself may not be.</p>
    <p>The pedagogical point: vibe coding is not <em>wrong</em>. It is a real productivity gain for many tasks. But applying it without verification (Sub-Lesson 9.5) to research-grade work is the contemporary face of doing-more-understanding-less.</p>
  </div>

  <!-- WHY THIS MATTERS NOW -->
  <h2 class="section-title">&#128302; Why This Argument is More Important in 2026, Not Less</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">A natural response to the 2024 paper is: well, that was when AI was unreliable. Now that frontier models are good at maths and physics (9.3), surely the illusions are less of a problem &mdash; the AI is more often right.</p>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The argument is precisely backwards. The illusions are <em>more</em> dangerous when the AI is more often right, because the surface fluency of AI outputs masks the remaining gaps more effectively. A model that&#39;s right 60% of the time is obviously to-be-checked. A model that&#39;s right 95% of the time looks trustworthy &mdash; and the 5% wrong is harder to spot because it doesn&#39;t come surrounded by other obvious errors.</p>

  <div class="info-box">
    <h4>&#9889; The Calibration Trap</h4>
    <p>If your overall experience with a model is that it&#39;s usually right, you start trusting it more. Trust calibrated to overall accuracy is then mis-calibrated for the specific cases where the model fails &mdash; which by structural argument (9.2c) cluster in the long tail, exactly where novel research happens.</p>
    <p>This is the AI version of the Dunning&ndash;Kruger trap: the less you know about a topic, the harder it is to spot the AI&#39;s errors in that topic, but the more useful the AI feels precisely <em>because</em> you couldn&#39;t do the work yourself. Both cuts of the knife point the same way.</p>
  </div>

  <!-- CONNECTING WEEKS -->
  <h2 class="section-title">&#128279; How This Connects to Earlier Weeks</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Several earlier weeks have touched on pieces of the illusions argument. The Messeri &amp; Crockett framework gives you a way of seeing them together.</p>

  <div style="overflow-x: auto;">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Earlier week</th>
          <th>Concrete instance of an illusion</th>
          <th>Which Messeri &amp; Crockett illusion</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Week 5 (Literature reviews)</td>
          <td>AI literature summaries miss niche work; over-represent canonical papers</td>
          <td>Explanatory breadth</td>
        </tr>
        <tr>
          <td>Week 6 (Writing &amp; ideation)</td>
          <td>Si et al. (2024): LLM-generated research ideas more novel-seeming but less diverse than human-generated</td>
          <td>Monoculture; exploratory objectivity</td>
        </tr>
        <tr>
          <td>Week 6 (Writing as thinking)</td>
          <td>Kosmyna et al. (2025): EEG study showing reduced neural engagement during AI-assisted writing</td>
          <td>Doing more but understanding less</td>
        </tr>
        <tr>
          <td>Week 6 (Homogenisation)</td>
          <td>Agarwal, Naaman &amp; Vashistha (CHI 2025): AI writing tools homogenise text toward Western norms</td>
          <td>Monoculture</td>
        </tr>
        <tr>
          <td>Week 6 (Scientific monoculture)</td>
          <td>Traberg, Roozenbeek &amp; van der Linden (<em>Comms Psych</em>, 2026): heavy AI use narrows scientific diversity</td>
          <td>Monoculture</td>
        </tr>
        <tr>
          <td>Week 7 (Silent errors)</td>
          <td>AI-generated code that runs but produces wrong results &mdash; researcher feels they&#39;ve done analysis but hasn&#39;t verified meaning</td>
          <td>Doing more but understanding less</td>
        </tr>
        <tr>
          <td>Week 8 (Multimodal)</td>
          <td>Jin et al. (2024): GPT-4V medical image accuracy 81.6% but 35.5% of correct answers via flawed reasoning</td>
          <td>Exploratory objectivity (apparent precision masking flawed process)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p style="color: #555; font-size: 1.05em; margin-top: 20px; line-height: 1.8;">Each week of this course has been giving you fragments. Messeri &amp; Crockett is the unifying frame &mdash; and the reason the previous fragments matter even as the specific models change.</p>

  <!-- WHAT TO DO -->
  <h2 class="section-title">&#129534; What to Do About It</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The Messeri &amp; Crockett argument is not a counsel of despair. They explicitly argue that AI can be a useful tool in research <em>provided</em> researchers maintain practices that resist the four illusions. Their suggested practices, paraphrased and operationalised:</p>

  <ul class="styled-list">
    <li><strong>For explanatory breadth:</strong> deliberately seek out sources that AI summaries miss. Use AI for first-pass familiarisation; then read primary sources, dissenting views, recent work that may post-date training cutoffs.</li>
    <li><strong>For exploratory objectivity:</strong> ask the same question of multiple models with different training. When they agree, ask: is this a property of the world or a property of overlapping training data? When they disagree, that disagreement is evidence.</li>
    <li><strong>For monoculture:</strong> consciously vary your prompts and your problem framings. Talk to colleagues who don&#39;t use the same tools. Read literature outside your immediate field. Treat AI ideas as one input among several, not the privileged starting point.</li>
    <li><strong>For doing-more-but-understanding-less:</strong> impose deliberate slowness on parts of the work. Read papers manually before asking AI to summarise them. Write paragraphs without AI before refining with it. Run analyses by hand on small datasets to check intuitions before scaling.</li>
  </ul>

  <div class="highlight-box">
    <h3>The argument that doesn&#39;t go stale</h3>
    <p>Note what the Messeri &amp; Crockett argument is <em>not</em>. It is not &ldquo;current AI is unreliable, so don&#39;t use it.&rdquo; It is not &ldquo;AI is overhyped.&rdquo; It is not anti-AI. The argument is strictly about <em>what happens to human understanding when AI does more of the cognitive work</em>, regardless of how good the AI is.</p>
    <p>That is why the argument doesn&#39;t go stale when the next model releases. A better model produces more output; the question of whether the researcher understands that output more or less than they would have without AI assistance is unchanged.</p>
    <p>This is the durable epistemic concern. Sub-Lesson 9.5 takes it into practical verification protocols.</p>
  </div>

  <div class="intro-text" style="margin-top: 50px;">
    <h2>&#128073; What Comes Next</h2>
    <p><strong>Sub-Lesson 9.5 &mdash; Verification Protocols for a Moving Target.</strong> Practical techniques for verifying AI output in your own research, including the meta-skill of how to read AI capability claims critically when the artefact under study changes every six months.</p>
  </div>
"""


# ---------------------------------------------------------------------------
# Sub-Lesson 9.5 — Verification Protocols for a Moving Target
# ---------------------------------------------------------------------------

SL5_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>The previous sub-lessons established the trajectory (9.1), the failure taxonomy (9.2), the genuine capability cases (9.3), and the durable epistemic concerns (9.4). This sub-lesson is the practical pay-off: how do you actually verify AI output in your own research workflow, and how do you read claims about AI capability critically when the literature is always six to twelve months behind the artefact?</p>
    <p>Two layers. First, verification of specific AI outputs &mdash; techniques you apply to a particular analysis, citation, or proof. Second, verification of <em>capability claims</em> &mdash; the meta-skill of reading the AI literature without being fooled by dated examples or selection bias. Both are required.</p>
  </div>

  <!-- LAYER 1: VERIFYING OUTPUTS -->
  <h2 class="section-title">&#128270; Layer 1: Verifying Specific AI Outputs</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">These techniques are the operational consequence of the failure taxonomy. Each targets a specific failure mode from 9.2.</p>

  <div class="card-grid">

    <div class="card">
      <h3>Known-Answer Testing</h3>
      <p>Run AI through tasks where you know the correct answer in advance &mdash; synthetic data with planted truths, problems from your field where the answer is published, edge cases you&#39;ve constructed. Check whether the output matches. The Week 7 silent-error problem &mdash; code that runs but is wrong &mdash; is detected here, nowhere else. Build small known-answer sets in your own domain and re-run them whenever you change models.</p>
    </div>

    <div class="card">
      <h3>Adversarial Prompting</h3>
      <p>Deliberately try to break outputs. Ask trick questions, push back on initial answers, change framings to see whether responses are stable. The Hallucination Hunting activity in 9.6 is exactly this. The point is not to catch the AI being wrong once &mdash; it is to map where the AI is fragile in your domain.</p>
    </div>

    <div class="card">
      <h3>Cross-Model Triangulation</h3>
      <p>Ask the same question of Claude Opus 4.7, GPT-5.5, Gemini 3.1 Pro, and an open-weights model like DeepSeek V4 Pro. When they agree: that&#39;s some evidence the answer is correct (provided their training data overlaps don&#39;t produce a shared error). When they disagree: that&#39;s a stronger signal that the question is one you should investigate yourself rather than trust any single output.</p>
    </div>

    <div class="card">
      <h3>The &ldquo;Teach It Back&rdquo; Test</h3>
      <p>If you cannot explain the AI&#39;s reasoning in your own words, you don&#39;t understand it &mdash; and you should not trust it. This applies whether the AI is doing your statistics, your code review, or your conceptual synthesis. The Messeri &amp; Crockett illusions (9.4) are specifically about the gap between feeling you understand and actually understanding. The teach-it-back test closes the gap.</p>
    </div>

    <div class="card">
      <h3>Manual Spot-Checks</h3>
      <p>Even when overall reliability is high, manually verify a sample of outputs. Every Nth citation. Every Nth analytical step. Random samples of generated text. The discipline is not catching every error; it is keeping your own intuitions calibrated as the work scales.</p>
    </div>

    <div class="card">
      <h3>Citation Verification</h3>
      <p>Direct re-use of the Week 5 framework. The Five-Point Citation Check (existence, authors, year, venue, claim verification) applies to every AI-generated citation. Frontier models still hallucinate citations on niche topics. The fix is mechanical, not mysterious; treat citation verification as a pipeline step, not an afterthought.</p>
    </div>

    <div class="card">
      <h3>Reproducibility Testing</h3>
      <p>Does the same prompt produce the same answer on different runs? Different sessions? Different models in the same family? Variable outputs are a signal &mdash; either of model uncertainty (informative) or of stochasticity that may matter for your downstream conclusions. Test before relying on a single run.</p>
    </div>

    <div class="card">
      <h3>Domain-Expert Spot-Checks</h3>
      <p>For cross-disciplinary work, recruit a domain expert to check AI output in their field. The Dunning&ndash;Kruger trap from 9.4 means you cannot reliably assess AI output in fields you don&#39;t know well. The fix is not to try harder; it is to ask someone who can.</p>
    </div>

  </div>

  <!-- LAYER 2: VERIFYING CAPABILITY CLAIMS -->
  <h2 class="section-title">&#128202; Layer 2: Verifying Capability Claims (the Dated-Research Trap)</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">This is the meta-skill the rest of the week has been building towards. When you encounter a published claim about what AI can or cannot do &mdash; in a journal article, a conference paper, a news story, a textbook &mdash; treat it as a hypothesis about a system that has since been replaced.</p>

  <div class="info-box">
    <h4>&#128221; The Three-Question Check</h4>
    <p><strong>1. Which model and version?</strong> A 2023 paper that says &ldquo;LLMs cannot do X&rdquo; tested GPT-3.5, GPT-4, or Claude 1. None of those is current. Without knowing which specific system was tested, the claim has no clear referent.</p>
    <p><strong>2. When was it tested?</strong> Anything pre-2024 is now historical. The artefact under study has been replaced two or three times since. Useful as a historical landmark; not useful as a current diagnosis.</p>
    <p><strong>3. Has anyone retested with current frontier models?</strong> If yes, what did the retest find? If no, the claim is unproven on present systems &mdash; not falsified, just unproven. Treat with the same caution you would treat a 2010 claim about smartphone battery life applied to 2026 phones.</p>
  </div>

  <p style="color: #555; font-size: 1.05em; margin-top: 25px; margin-bottom: 20px; line-height: 1.8;">A specific case to keep in mind: the Frieder et al. (2023) paper on &ldquo;Mathematical Capabilities of ChatGPT&rdquo; found that GPT-4 was inadequate for graduate-level mathematics. This was a careful, well-cited study at the time. By May 2026, the same questions answered by GPT-5.5 Pro, Gemini Deep Think, or AlphaEvolve give very different answers (see 9.3). Citing Frieder et al. as if it described current AI is now an error &mdash; but the citation persists in the literature precisely because it was a good paper when published.</p>

  <div class="case-study">
    <h4>&#128221; A Concrete Example: The Reversal Curse</h4>
    <p>Berglund et al. (2023) showed the reversal curse on the GPT-3.5/GPT-4 generation. The paper has been cited several thousand times. It was an important contribution at the time.</p>
    <p>By 2026, the reversal curse is no longer a prominent failure in benchmark discussions. Frontier models handle it largely correctly. A 2026 paper that opens with &ldquo;LLMs famously suffer from the reversal curse (Berglund et al., 2023)&rdquo; has not retested the claim and is treating a historical finding as a current diagnosis.</p>
    <p>The fix: cite Berglund et al. as the originating documentation of a failure mode that has since been mitigated, not as evidence about current model behaviour. The same disciplinary move applies to most pre-2025 capability claims.</p>
  </div>

  <!-- BUILDING HABITS -->
  <h2 class="section-title">&#129336; Building Verification Habits</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Verification is not a one-time audit. It is a habit that survives model releases. Three commitments that make verification durable:</p>

  <ul class="styled-list">
    <li><strong>Verification as workflow component, not afterthought.</strong> Every AI-assisted analysis pipeline should have a verification step before any output leaves your workspace. Bake it into the workflow; don&#39;t leave it to memory or virtue.</li>
    <li><strong>Retest cadence.</strong> When a new frontier model drops, your previous calibration may be wrong &mdash; in either direction. Re-run your known-answer test set. Re-test the failure cases that worried you. Re-test the capability cases that worked. The model that&#39;s frontier today is not the one you calibrated against six months ago.</li>
    <li><strong>Write down what you found.</strong> Document the model, the date, the prompts, the outputs, the verification steps. This is partly for reproducibility, partly for your own future self when you wonder &ldquo;was that working back then or am I misremembering?&rdquo;, and partly so the field can learn from your domain-specific findings.</li>
  </ul>

  <!-- VERIFY-REFERENCES SKILL -->
  <h2 class="section-title">&#128221; The Course&#39;s Own Verification Practice</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">This course practises what it teaches. The materials are AI-assisted (see the AI Content Disclaimer on the home page) and have been verified using a custom <code>/verify-references</code> skill that does exactly the kind of checking described above: every URL fetched, every named citation cross-checked against primary sources, every statistical claim traced back to source.</p>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">In building these materials we have caught and fixed errors of exactly the patterns documented this week:</p>

  <ul class="styled-list">
    <li>Wrong arXiv IDs (a Gupta &ldquo;Chasing Carbon&rdquo; reference linked to a maths paper on Fourier&ndash;Stieltjes algebras)</li>
    <li>Hallucinated authors (&ldquo;Tamburrino et al.&rdquo; for what was actually Wright et al.; &ldquo;Anthony et al.&rdquo; for what was actually Luccioni et al.; &ldquo;Humbel et al.&rdquo; for what was actually Crosilla et al.)</li>
    <li>Wrong DOIs (a Lund et al. citation pointed at a paper about academic promotions, not ChatGPT)</li>
    <li>Hallucinated post titles (a Mollick blog post on AI ethics that doesn&#39;t exist)</li>
    <li>Wrong article titles (Nature article cited with a hallucinated subtitle; MIT Tech Review article cited with the URL slug as &ldquo;title&rdquo;)</li>
    <li>Wrong link slugs (Okolo Brookings article URL had &ldquo;equitable&rdquo; where it should have been &ldquo;inclusive&rdquo;; ICRC autonomous-weapons URL had the words in the wrong order)</li>
  </ul>

  <p style="color: #555; font-size: 1.05em; margin-top: 20px; margin-bottom: 20px; line-height: 1.8;">All caught by the verification process. Some had been in place across multiple weeks. The lesson: even careful AI-assisted writing produces these errors at non-trivial rates. Verification catches them; without verification, they persist.</p>

  <div class="info-box">
    <h4>&#129504; A 2026 Open Question: &ldquo;Teaching Claude Why&rdquo;</h4>
    <p>In May 2026 Anthropic published research on training models not just to follow safety rules but to understand the <em>reasons</em> behind those rules. The thinking: a model that understands why a rule exists can navigate novel situations the rule-makers didn&#39;t anticipate, and can articulate trade-offs when rules conflict.</p>
    <p>This raises a verification question that doesn&#39;t have a settled answer yet. <strong>If a model is being trained to understand <em>why</em> it should behave certain ways, does that change how we verify its outputs?</strong> Does understanding motivation make verification easier (the model can explain its reasoning) or harder (the model can construct plausible justifications for almost anything)? It is too early to say definitively. Worth tracking as the research develops &mdash; and worth thinking about for your own discipline: when AI systems can articulate <em>why</em> they reached a conclusion, what new verification opportunities and pitfalls emerge?</p>
  </div>

  <div class="highlight-box">
    <h3>The verification stance</h3>
    <p>Verification is not a sign of distrust in AI. It is a sign of taking AI seriously as a research tool. Tools you take seriously, you check. Microscopes get calibrated. Statistical packages get validated against worked examples. AI outputs get verified against primary sources.</p>
    <p>The researcher who never verifies their AI outputs is making a methodological mistake. The researcher who verifies systematically is doing their job.</p>
  </div>

  <div class="intro-text" style="margin-top: 50px;">
    <h2>&#128073; What Comes Next</h2>
    <p><strong>Sub-Lesson 9.6 &mdash; Hands-On Activities and Assessment.</strong> Three activities that put the trajectory and verification frames into practice in your own field, and a final assessment that asks you to write your own dated capability/limitation snapshot. The deliverable explicitly acknowledges that it will go stale &mdash; that is the teaching move.</p>
  </div>
"""


# ---------------------------------------------------------------------------
# Sub-Lesson 9.6 — Hands-On Activities and Assessment
# ---------------------------------------------------------------------------

SL6_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>Three activities that operationalise the trajectory frame in your own research domain, and a final assessment that asks you to produce a dated snapshot of AI capability and limitation in your field. The deliverable is explicitly time-stamped and is expected to go stale within months &mdash; that <em>is</em> the teaching move. Continuous re-calibration is the skill being taught, not the ability to write a static report.</p>
  </div>

  <!-- ACTIVITY 1: HALLUCINATION HUNTING -->
  <h2 class="section-title">&#127919; Activity 1: Hallucination Hunting</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Familiar from earlier weeks (Week 5&#39;s citation hunt; Week 8&#39;s self-recorded transcription test). Here, applied to your own domain in 2026.</p>

  <div class="technical-detail">
    <h4>&#128221; Brief</h4>
    <p>Choose a current frontier model: Claude Opus 4.7, GPT-5.5 (or Pro), Gemini 3.1 Pro, or DeepSeek V4 Pro. Try, deliberately, to induce failures in your own discipline.</p>
    <p style="margin-top: 12px;">Prompts to consider:</p>
    <ul class="styled-list">
      <li>Ask for a citation to a recent paper on a niche sub-topic in your field. Verify the paper exists and that the cited claim matches.</li>
      <li>Ask for the proof of a result you know well. Check whether the proof is correct or contains plausible-but-wrong steps.</li>
      <li>Ask for the contemporary consensus on a debated question in your field. Check whether the model represents the debate accurately or flattens it into a single position.</li>
      <li>Ask for a summary of a specific paper&#39;s findings. Compare to the actual paper.</li>
      <li>Ask the model to apply a method from your field to a problem outside its usual domain. See whether it transfers correctly.</li>
    </ul>
    <p style="margin-top: 12px;"><strong>Document each failure.</strong> What was the prompt? What did the model produce? What was wrong about it? Categorise per the 9.2 taxonomy: patched (you&#39;re using an old model), reduced-but-persistent (frontier behaviour but mitigatable), or structural (won&#39;t go away with the next release).</p>
    <p style="margin-top: 12px;"><strong>Deliverable:</strong> a structured table of at least <strong>five distinct failures</strong> in your domain, with prompt, output, what was wrong, and category.</p>
  </div>

  <!-- ACTIVITY 2: CAPABILITY HUNTING -->
  <h2 class="section-title">&#128640; Activity 2: Capability Hunting</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The new activity. Hallucination hunting documents what AI fails at; capability hunting documents what it can do that you didn&#39;t expect. The pairing is the point &mdash; both halves of the calibration in one assessment.</p>

  <div class="technical-detail">
    <h4>&#128221; Brief</h4>
    <p>Choose a task in your own field that &ldquo;common knowledge&rdquo; (or your own intuition) says AI can&#39;t handle. Test current frontier models on it. Document what actually happened.</p>
    <p style="margin-top: 12px;">Some prompts for thinking about what to test:</p>
    <ul class="styled-list">
      <li>A type of analysis you assumed required hand-tuning</li>
      <li>A class of problem your field considers &ldquo;AI-resistant&rdquo;</li>
      <li>A skill that the literature claims AI can&#39;t do (date-check the claim)</li>
      <li>A task where you have ground truth (your own published work; a benchmark question with known answer)</li>
      <li>A task that requires combining knowledge from two sub-fields</li>
    </ul>
    <p style="margin-top: 12px;"><strong>Cross-model triangulation is required.</strong> Test the same task on at least two different frontier models. Document agreement and disagreement. The disagreements are particularly informative.</p>
    <p style="margin-top: 12px;"><strong>Deliverable:</strong> a write-up of at least <strong>three capability tests</strong>, with the assumption you held going in, the prompts you used, what each model produced, your verification of the outputs, and your updated calibration.</p>
  </div>

  <!-- ACTIVITY 3: TRAJECTORY TRACKING -->
  <h2 class="section-title">&#128202; Activity 3: Trajectory Tracking</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The meta-activity. Test the dated-research trap in practice. Pick a 2023&ndash;24 published claim &ldquo;AI cannot reliably do X&rdquo; and check whether it still holds against current frontier models.</p>

  <div class="technical-detail">
    <h4>&#128221; Brief</h4>
    <p>Find a 2023 or 2024 paper, blog post, or news article that makes a specific empirical claim about an AI limitation. Quote the claim and the model(s) the claim was tested on. Examples to start from (you should find your own):</p>
    <ul class="styled-list">
      <li>Frieder et al. (2023): GPT-4 cannot do graduate-level mathematics &mdash; retest on GPT-5.5 Pro and Gemini Deep Think</li>
      <li>Berglund et al. (2023): the reversal curse on GPT-3.5 / GPT-4 &mdash; retest on Opus 4.7 and DeepSeek V4 Pro</li>
      <li>Magesh et al. (2024): purpose-built legal AI tools hallucinate 17&ndash;33% &mdash; check whether updated versions still do</li>
      <li>A claim from your own field, ideally one you&#39;ve cited in your own work</li>
    </ul>
    <p style="margin-top: 12px;">Run the test yourself with current frontier models. Document the results. Reflect on:</p>
    <ul class="styled-list">
      <li>Does the claim still hold? Partially? Has it been entirely superseded?</li>
      <li>If superseded, what changed &mdash; better training, more parameters, different architecture, different prompting?</li>
      <li>What did the original paper get right structurally, even if the specific empirical claim is now dated?</li>
      <li>Should the original citation still appear in your literature review? With what framing?</li>
    </ul>
    <p style="margin-top: 12px;"><strong>Deliverable:</strong> a 400&ndash;600 word write-up of one trajectory test, with original claim, retest methodology, retest results, and a paragraph on how the original paper should now be cited.</p>
  </div>

  <!-- ASSESSMENT -->
  <h2 class="section-title">&#128221; Weekly Assessment</h2>

  <div class="resource-placeholder">
    <h4>&#128218; <em>AI in [your field] &mdash; May 2026 Snapshot</em></h4>
    <p><strong>Length:</strong> approximately 1,500 words</p>
    <p><strong>Due:</strong> end of Week 9 (specific date in Amathuba)</p>
    <p><strong>Format:</strong> structured report with sections for capability, limitation, methodology, and reflection</p>

    <p style="margin-top: 18px;"><strong>What the snapshot should contain:</strong></p>
    <ul class="styled-list">
      <li><strong>Capability findings.</strong> Drawing on Activity 2, document what current frontier models can do in your field. Be specific: which model, which version, when tested, what prompts, what outputs, what verification you did. At least three documented capabilities.</li>
      <li><strong>Limitation findings.</strong> Drawing on Activity 1, document where current frontier models still fail in your field. Categorise by the 9.2 taxonomy. At least five documented failures.</li>
      <li><strong>Methodology.</strong> Document the verification protocols you used. Which models did you test? Which prompts? How did you verify the outputs? What did you learn about your own verification practice along the way?</li>
      <li><strong>Reflection: when this snapshot will go stale.</strong> Identify which of your findings are most likely to be superseded soonest. What kinds of evidence would prompt you to update the snapshot? What is your recommended retest cadence for your domain?</li>
      <li><strong>Disclosure statement</strong> (per Lesson 6 Sub-Lesson 5 format): which AI tools you used in producing the report itself, what for, and how you verified.</li>
    </ul>

    <p style="margin-top: 18px;"><strong>Grading split (100 points):</strong></p>
    <ul class="styled-list">
      <li>Capability findings &mdash; 25 points (specificity, dated evidence, verification quality)</li>
      <li>Limitation findings &mdash; 25 points (specificity, taxonomy use, dated evidence)</li>
      <li>Methodology &mdash; 25 points (rigour of verification, cross-model triangulation, manual spot-checks)</li>
      <li>Reflection on staleness and retest cadence &mdash; 15 points</li>
      <li>Disclosure statement &mdash; 10 points</li>
    </ul>
  </div>

  <div class="info-box">
    <h4>&#127919; Why the Deliverable Acknowledges Its Own Future Obsolescence</h4>
    <p>The point of the snapshot is not the snapshot itself. The point is the practice of producing it: knowing which models you tested, when, with what prompts, with what verification, and being able to reproduce the exercise in six months and notice what has changed.</p>
    <p>A static body of knowledge about &ldquo;what AI can do in my field&rdquo; is not what we&#39;re asking for. We are asking for a calibrated, dated, retestable starting point that you can update as the field changes &mdash; and the meta-skill of knowing how to update it.</p>
  </div>

  <!-- WEEK SUMMARY -->
  <h2 class="section-title">&#128218; Week 9 in Summary</h2>

  <div class="highlight-box">
    <h3>What you should leave the week with</h3>
    <p><strong>A trajectory frame.</strong> Every claim about AI capability has an implicit &ldquo;as of [date]&rdquo;. From Sub-Lesson 9.1, you have a calibrated picture of where the May 2026 frontier sits.</p>
    <p><strong>A failure taxonomy.</strong> When you encounter an AI failure, you can locate it in patched / reduced-but-persistent / structural. From Sub-Lesson 9.2, you have the categories.</p>
    <p><strong>A capability map.</strong> From Sub-Lesson 9.3, you have concrete evidence of where AI is now genuinely strong &mdash; including in fields where two years ago the consensus said it couldn&#39;t contribute.</p>
    <p><strong>An epistemic frame that doesn&#39;t go stale.</strong> From Sub-Lesson 9.4, you have the Messeri &amp; Crockett four-illusion framework as a durable lens on what happens to your own understanding when AI does more of the cognitive work.</p>
    <p><strong>Verification protocols.</strong> From Sub-Lesson 9.5, you have practical techniques for checking specific outputs and for reading capability claims critically.</p>
    <p><strong>Practice in your own field.</strong> From Sub-Lesson 9.6&#39;s activities and assessment, you have a documented snapshot of AI in your discipline as of May 2026, and the meta-skill to update it.</p>
  </div>

  <div class="intro-text" style="margin-top: 50px;">
    <h2>&#128073; What Comes Next</h2>
    <p><strong>Week 10 &mdash; Agentic AI, RAG &amp; Advanced Research Tools.</strong> Now that you have a calibrated picture of current capability and a verification habit in place, the next week introduces the more powerful agentic tools. The order matters: agentic AI amplifies both capability and risk. The verification literacy you built this week is what makes the next week safe to teach.</p>
  </div>
"""


# ---------------------------------------------------------------------------
# Table of Contents
# ---------------------------------------------------------------------------

TOC_HTML = """<html><head><meta http-equiv="'Content-Type'" content="'text/html;charset=utf-8'" /><title>MAM5020F 2026 | Gen AI for Research - Week 9: Critical Evaluation &amp; Limitations of AI</title></head><body>
<div style="background: #003A70; padding: 8px 20px; text-align: center;"><a href="../index.html" style="color: white; text-decoration: none; font-size: 0.85em;">&#8592; Back to Contents</a></div><table cellpadding=0 cellspacing=0 border=0 width=100%><tr><td colspan=3>&nbsp;</td></tr><tr><td valign="top" width="100%"><font class="title"><strong>MAM5020F 2026 | Gen AI for Research - Week 9: Critical Evaluation &amp; Limitations of AI</strong></font><br><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="The Trajectory of LLM Capabilities.html" />1. The Trajectory of LLM Capabilities</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Three Categories of Failure.html" />2. Three Categories of Failure: Patched, Reduced, Structural</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Where AI Is Now Genuinely Strong.html" />3. Where AI Is Now Genuinely Strong</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Illusions of Understanding.html" />4. Illusions of Understanding</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Verification Protocols for a Moving Target.html" />5. Verification Protocols for a Moving Target</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Hands-On Activities and Assessment.html" />6. Hands-On: Activities &amp; Assessment</a></p></td></tr></table><footer style="background: #f9f9f9; margin-top: 40px; padding: 22px 30px; text-align: center; color: #888; font-size: 0.85em; border-top: 1px solid #eee; font-family: 'Lato', 'Lucida Sans Unicode', 'Lucida Grande', sans-serif;">
&copy; 2026 Jonathan Shock &middot; MAM5020F: Generative AI for Research &middot; Licensed under <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener" style="color: #003A70; text-decoration: underline;">CC&nbsp;BY&nbsp;4.0</a>
</footer></body></html>
"""


# ---------------------------------------------------------------------------
# Sub-lesson registry
# ---------------------------------------------------------------------------

SUBLESSONS = [
    {
        "filename": "The Trajectory of LLM Capabilities.html",
        "title": "Week 9.1 - The Trajectory of LLM Capabilities",
        "badge": "Week 9 &bull; Sub-Lesson 1",
        "header_emoji": "&#128200;",  # chart with upwards trend
        "header_title": "The Trajectory of LLM Capabilities",
        "header_subtitle": "From GPT-2 to the May 2026 frontier &mdash; why every claim about &ldquo;what AI can do&rdquo; carries a hidden date stamp",
        "body": SL1_BODY,
    },
    {
        "filename": "Three Categories of Failure.html",
        "title": "Week 9.2 - Three Categories of Failure",
        "badge": "Week 9 &bull; Sub-Lesson 2",
        "header_emoji": "&#129518;",  # compass
        "header_title": "Three Categories of Failure",
        "header_subtitle": "A taxonomy that survives the next model release: what&#39;s been patched, what&#39;s reduced but persistent, and what&#39;s structural",
        "body": SL2_BODY,
    },
    {
        "filename": "Where AI Is Now Genuinely Strong.html",
        "title": "Week 9.3 - Where AI Is Now Genuinely Strong",
        "badge": "Week 9 &bull; Sub-Lesson 3",
        "header_emoji": "&#128640;",  # rocket
        "header_title": "Where AI Is Now Genuinely Strong",
        "header_subtitle": "Concrete cases from 2026 in mathematics and theoretical physics &mdash; with the caveats that prevent miscalibration",
        "body": SL3_BODY,
    },
    {
        "filename": "Illusions of Understanding.html",
        "title": "Week 9.4 - Illusions of Understanding",
        "badge": "Week 9 &bull; Sub-Lesson 4",
        "header_emoji": "&#128302;",  # crystal ball
        "header_title": "Illusions of Understanding",
        "header_subtitle": "Messeri &amp; Crockett&#39;s four illusions: durable epistemic concerns that get worse, not better, as AI gets more capable",
        "body": SL4_BODY,
    },
    {
        "filename": "Verification Protocols for a Moving Target.html",
        "title": "Week 9.5 - Verification Protocols for a Moving Target",
        "badge": "Week 9 &bull; Sub-Lesson 5",
        "header_emoji": "&#128270;",  # magnifying glass
        "header_title": "Verification Protocols for a Moving Target",
        "header_subtitle": "Practical techniques for verifying AI outputs, plus the meta-skill of reading AI capability claims critically",
        "body": SL5_BODY,
    },
    {
        "filename": "Hands-On Activities and Assessment.html",
        "title": "Week 9.6 - Hands-On Activities and Assessment",
        "badge": "Week 9 &bull; Sub-Lesson 6",
        "header_emoji": "&#127919;",  # bullseye
        "header_title": "Hands-On Activities and Assessment",
        "header_subtitle": "Hallucination hunting, capability hunting, trajectory tracking &mdash; and a dated capability snapshot that explicitly acknowledges its own future obsolescence",
        "body": SL6_BODY,
    },
]


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
    print("Generating Week 9...")
    # Table of contents
    print("Table of Contents:")
    write_to(SRC_DIR, "Table of Contents.html", TOC_HTML)
    write_to(DOCS_DIR, "Table of Contents.html", TOC_HTML)
    # Sub-lessons
    for sl in SUBLESSONS:
        print(f"{sl['title']}:")
        rendered = render_sublesson(sl)
        write_to(SRC_DIR, sl["filename"], rendered)
        write_to(DOCS_DIR, sl["filename"], rendered)
    print("\nDone. 7 files written to each of:")
    print(f"  {SRC_DIR}")
    print(f"  {DOCS_DIR}")


if __name__ == "__main__":
    main()
