#!/usr/bin/env python3
"""
Generate Week 10 lesson HTML files (Agentic AI, RAG & Advanced Research Tools).

Outputs to both:
  Course materials/Week 10/                  (source / Amathuba upload copies)
  Course materials/docs/week-10/             (GitHub Pages serving copies)

Mirrors the Week 9 generator. CSS is pretty-printed (one property per line) and the
<style> block lives in <head> so Brightspace's TinyMCE source editor preserves it.

Re-run after any content change.
"""

import os
import re

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SRC_DIR = os.path.join(ROOT, "Week 10")
DOCS_DIR = os.path.join(ROOT, "docs", "week-10")


def pretty_print_css(css: str) -> str:
    """Convert single-line CSS rules to multi-line format (each property on its own line).
    Brightspace's TinyMCE strips compact <style> blocks but preserves pretty-printed ones
    that match the format of Weeks 1-8."""
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
&copy; 2026 Jonathan Shock, University of Cape Town &middot; MAM5020F: Generative AI for Research &middot; Licensed under <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener" style="color: #003A70; text-decoration: underline;">CC&nbsp;BY&nbsp;4.0</a>
</footer>
</body></html>
"""


# ---------------------------------------------------------------------------
# Sub-Lesson 10.1 — Agents: What They Are and What's Actually New in 2026
# ---------------------------------------------------------------------------

SL1_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>For the last two years, &ldquo;AI agent&rdquo; has been one of the most over-used and under-defined phrases in the field. Vendors apply it to everything from a chatbot that can call a weather API to a system that runs unsupervised for hours rewriting a codebase. If we are going to think clearly about what agents mean for research, we need a working definition that survives the marketing.</p>
    <p>This sub-lesson gives you that definition &mdash; an agent is a model wrapped in a <em>harness</em> of tools, memory, loops, and permissions &mdash; and then makes one central observation that frames the whole week: <strong>since 2024, the harness has become the product</strong>. The base model matters less than it used to; how it is scaffolded matters more. We will look at the May 2026 agent landscape, the surprising trend of coding agents being repurposed for general knowledge work, and what all of this actually means for a working researcher.</p>
    <p>A word of calibration, carried over from Week 9: every concrete claim in this sub-lesson is time-stamped. The agent landscape moves faster than almost anything else in AI right now. What is true in May 2026 will be partly false by November. Treat the specifics as a snapshot and the framing as the durable part.</p>
  </div>

  <h2 class="section-title">&#129302; What Is an Agent? A Working Definition</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Strip away the marketing and an agent is a language model placed inside a loop that lets it <em>act</em>, not just respond. Five components turn a model into an agent. The first is the model itself; the other four, taken together, are what this week calls the <strong>harness</strong>.</p>

  <ul class="styled-list">
    <li><strong>A model</strong> &mdash; the same kind of transformer doing next-token prediction we met in Week 2. Nothing about the underlying architecture has changed; the model is still predicting tokens. What is new is what those tokens are allowed to <em>do</em>.</li>
  </ul>

  <div class="technical-detail">
    <h4>&#129520; The Harness &mdash; everything built around the model</h4>
    <p style="color: #555; line-height: 1.7; margin-bottom: 15px;">The model is the engine; the harness is the chassis, wheels, steering, and brakes built around it. A model on its own answers questions. A model in a harness gets things done. These four components &mdash; plus the prompts and context-management that coordinate them &mdash; are the harness:</p>
    <ul class="styled-list" style="margin-top: 0;">
      <li><strong>Tools</strong> &mdash; functions the model can call by emitting a structured request in its output stream: run code, search the web, read a file, query a database, send an email. The model does not execute these; the harness does, and feeds the result back in.</li>
      <li><strong>A loop</strong> &mdash; the harness runs the model, executes any tool call it requests, appends the result to the context, and runs the model again. This repeats until the model decides the task is done. A chatbot answers once; an agent iterates.</li>
      <li><strong>Memory</strong> &mdash; some way of carrying state across many loop iterations (and sometimes across sessions), because a useful task can span dozens or hundreds of steps that overflow a single context window.</li>
      <li><strong>Permissions</strong> &mdash; the boundary of what the agent is allowed to do without asking. Read-only? Allowed to write files? Allowed to spend money? This is the single most important safety dial, and the one researchers most often leave on the wrong setting.</li>
    </ul>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 20px; margin-bottom: 15px;">Keep that word &mdash; <em>harness</em> &mdash; in mind. The central claim of the next section is that in 2026 the harness, not the engine, increasingly decides how well the whole thing drives.</p>

  <div class="info-box">
    <h4>&#128161; Drop the word &ldquo;autonomy&rdquo;</h4>
    <p>Popular coverage frames agents as a binary: either a tool &ldquo;is autonomous&rdquo; or it is not. This is unhelpful. Autonomy is a <em>spectrum</em> set by the permissions dial, not a property of the model. The same model is a cautious assistant when it must confirm every action, and an unsupervised delegate when it can act freely for an hour. When you read that a system &ldquo;is an autonomous agent&rdquo;, the useful question is never &ldquo;is it autonomous?&rdquo; but &ldquo;<em>how much</em> is it allowed to do, over <em>how long</em>, before a human looks?&rdquo;</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">This definition lets us draw two clean distinctions. A <strong>chatbot with browsing</strong> is not yet an agent in the full sense &mdash; it makes one tool call and answers. A <strong>2023-style &ldquo;chain&rdquo;</strong> (a fixed, pre-scripted sequence of model calls) is not an agent either, because the model does not decide what to do next; the developer hard-coded the steps. An agent chooses its own next action inside the loop. That difference &mdash; the model, not the developer, steering the loop &mdash; is what changed between 2023 and 2026, and it is where both the new capability and the new failure modes come from.</p>

  <h2 class="section-title">&#128295; What&#39;s New Since 2024: The Harness Is the Product</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Here is the single most important shift to internalise. In 2023, agent performance was dominated by the base model: a better model gave you a better agent, full stop. By May 2026, that is no longer true. Agent performance is a <em>joint</em> property of the model, the harness around it, and the strategy for packing the right context into the model at each step. The harness &mdash; the prompts, the tool definitions, the context management, the evaluation loop, the model-specific tuning &mdash; has become the thing that companies actually build and sell.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">This is not just a claim from practitioners. It is now the subject of formal research. The clearest statement comes from a March 2026 Stanford preprint, <em>Meta-Harness: End-to-End Optimization of Model Harnesses</em> (Lee et al.), whose opening line is almost a thesis statement for this whole week:</p>

  <div class="technical-detail">
    <h4>&#128209; From the Meta-Harness paper (Lee et al., Stanford, March 2026)</h4>
    <p style="color: #444; line-height: 1.75; margin-bottom: 12px;"><em>&ldquo;The performance of large language model systems depends not only on model weights, but also on their harness: the code that determines what information to store, retrieve, and present to the model.&rdquo;</em></p>
    <p style="color: #555; line-height: 1.7;">The paper builds a system that automatically searches over harness code &mdash; keeping the model fixed &mdash; and improves on a state-of-the-art context-management baseline by <strong>7.7 points while using four times fewer context tokens</strong>. The point for us is not the system itself but the demonstration: a measurable chunk of an agent&#39;s performance lives in the harness, independent of the model, and is large enough to optimise on its own.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The companies building these systems show the same effect in detail. In a February 2026 engineering write-up, the LangChain team took a single coding model (GPT-5.2-Codex) and, <em>without changing the model</em>, improved their agent&#39;s score on <em>Terminal-Bench 2.0</em> by 13.7 points &mdash; from 52.8% to 66.5%, moving it from outside the top 30 to the top 5. Every point of that gain came from the harness:</p>

  <div class="case-study">
    <h4>&#128295; A worked example: 13.7 points from the harness alone</h4>
    <p>LangChain&#39;s recipe for the jump from 52.8% to 66.5% on Terminal-Bench 2.0 (same model throughout) was entirely harness engineering:</p>
    <ul class="styled-list">
      <li><strong>A better system prompt</strong> &mdash; explicit planning, build, verify, and fix phases, with emphasis on edge-case testing and checking output against the task specification.</li>
      <li><strong>Middleware in the loop</strong> &mdash; a pre-exit checklist that forces verification before the agent declares itself done, an onboarding step that maps the working environment, and a loop-detector that interrupts the agent when it gets stuck repeating an edit.</li>
      <li><strong>Context management</strong> &mdash; mapping the directory structure and available tools up front, and warning the agent about its remaining time budget.</li>
      <li><strong>A &ldquo;reasoning sandwich&rdquo;</strong> &mdash; allocating more reasoning effort to the planning and verification phases than to the execution in between.</li>
    </ul>
    <p style="margin-top: 12px;">None of this touched the model&#39;s weights. It is a concrete demonstration of the thesis: a large slice of agent performance is engineering of the scaffolding, and it is exactly the kind of thing a tool vendor can do that you, choosing between tools, cannot see from the model name alone.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">And it generalises across models. In a May 2026 follow-up the same team reported that, on a different agentic benchmark (tau2-bench), prompts and middleware alone moved scores by <strong>10 to 20 points</strong> &mdash; a roughly 20% lift on one coding model and 10% on another &mdash; and that the same harness techniques apply when driving open-weight models such as Kimi, Qwen, and DeepSeek (which we return to in 10.5). The lesson holds regardless of whose model you use: the harness is doing a large and measurable share of the work.</p>

  <div class="warning-box">
    <h4>&#9888;&#65039; What this means when you read a benchmark</h4>
    <p>If the harness can swing a score by ten points or more, then a leaderboard number attached to a bare model name is close to meaningless without knowing the scaffolding that produced it. This is not hypothetical: <em>Terminal-Bench 2.0</em> (the benchmark itself, arXiv:2601.11868) is explicitly run through a named harness, and different harnesses on the same model produce different scores. When a tool claims &ldquo;state-of-the-art on benchmark X&rdquo;, the honest question is: <em>which harness?</em> A strong model, badly scaffolded, will underperform a weaker model in a better harness. This is the agentic version of the Week 9 lesson that benchmark numbers need their context to mean anything.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">There is a research-tooling consequence too. The agent-infrastructure companies are now shipping harnesses as products: at LangChain&#39;s <em>Interrupt</em> conference (13&ndash;14 May 2026), the company released a cluster of harness-building tools &mdash; a hosted runtime for &ldquo;deep agents&rdquo;, a faster trace database, sandboxes, a context-management hub, and a gateway that enforces spend limits and redacts personal data before requests leave your environment. The takeaway for a researcher is not that you need any of these, but that the centre of gravity in the field has moved from &ldquo;which model&rdquo; to &ldquo;which harness&rdquo;. When you choose an agent tool, you are choosing a harness as much as a model.</p>

  <h2 class="section-title">&#128506;&#65039; The 2026 Agent Landscape in One Picture</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">As of May 2026, the agent ecosystem sorts into roughly five families. The boundaries are blurring fast (see the next section), but this map is a useful starting orientation. We will return to specific tools, and to the honest free-versus-paid picture, in Sub-Lessons 10.3 and 10.5.</p>

  <div style="overflow-x: auto;">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Family</th>
          <th>What it does</th>
          <th>Representative tools (May 2026)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Coding agents</strong></td>
          <td>Read, write, run, and debug code across a whole project, often unsupervised for long stretches.</td>
          <td>Claude Code, OpenAI Codex, Cursor, Cline, opencode</td>
        </tr>
        <tr>
          <td><strong>Computer-use agents</strong></td>
          <td>Drive a graphical interface &mdash; click, type, scroll &mdash; the way a person would, for tasks with no API.</td>
          <td>Anthropic Computer Use, Codex computer-use mode, the Operator lineage</td>
        </tr>
        <tr>
          <td><strong>Research agents</strong></td>
          <td>Plan a multi-step search, gather and cross-check sources, and synthesise a cited report. &ldquo;Deep Research&rdquo; modes.</td>
          <td>Deep Research modes across the major chat assistants (covered in 10.5)</td>
        </tr>
        <tr>
          <td><strong>General agents</strong></td>
          <td>Attempt arbitrary multi-step tasks across tools and the web from a single instruction.</td>
          <td>Manus, ChatGPT Agent</td>
        </tr>
        <tr>
          <td><strong>Creative agents</strong></td>
          <td>Drive creative software (3D, audio, design) through tool connectors.</td>
          <td>Claude with creative connectors (Blender, Ableton, and others)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 20px; margin-bottom: 15px;">A concrete, datable example of how fast the creative corner is moving: on 28 April 2026 Anthropic shipped nine creative tool connectors for Claude &mdash; including Blender, Ableton, Adobe and Autodesk integrations &mdash; and, notably, made them available on the <em>free</em> plan. We will treat &ldquo;what is actually free&rdquo; as a first-class question throughout this week, because for many students at UCT it is the question that decides whether a tool is usable at all.</p>

  <div class="case-study">
    <h4>&#128421;&#65039; A threshold moment: computer-use at human speed</h4>
    <p>The computer-use family crossed a noticeable threshold in April 2026. Ari Weinstein of OpenAI, posting about the Codex computer-use mode, wrote on 16 April: <em>&ldquo;This is the first time I&#39;ve ever seen an LLM operate a GUI as fast as a person, and it&#39;s surreal.&rdquo;</em> Two weeks later he reported that a Codex app update had made one computer-use task run <strong>42% faster</strong> again.</p>
    <p>Two honest caveats. First, these are <em>first-party</em> claims &mdash; the person shipping the product describing his own product &mdash; not independent measurements, so treat the 42% as a vendor figure. Second, &ldquo;as fast as a person&rdquo; is about <em>speed</em>, not <em>reliability</em>; a fast agent that takes a wrong action quickly is not obviously progress (we develop exactly this distinction in 10.2). But the qualitative marker is real and worth recording: as of mid-2026, an AI driving a graphical interface by clicking and typing is no longer visibly slow. The bottleneck has moved from speed to judgement.</p>
  </div>

  <div class="info-box">
    <h4>&#128221; A note on naming</h4>
    <p>Throughout this course we refer to model <em>families</em> &mdash; &ldquo;Claude (family)&rdquo;, &ldquo;GPT (family)&rdquo;, &ldquo;Gemini (family)&rdquo; &mdash; rather than chasing version numbers, because the versions change monthly. Agent <em>products</em> are different: &ldquo;Claude Code&rdquo;, &ldquo;Codex&rdquo;, &ldquo;Cursor&rdquo;, &ldquo;Manus&rdquo; are tool names, and we keep them, the same way we kept &ldquo;Whisper large-v3&rdquo; in Week 8. When you see a specific version number attached to a benchmark figure, treat it as a dated citation, not a recommendation.</p>
  </div>

  <h2 class="section-title">&#128640; Agents Are Breaking Containment</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The most interesting throughline of April&ndash;May 2026 is that the families above are bleeding into one another. Tools built as <em>coding</em> agents are being pointed at general knowledge work, because the thing that makes a good coding agent &mdash; a robust loop, file access, the ability to run for a long time without losing the thread &mdash; turns out to be exactly what a good general agent needs too.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">In the space of a few weeks, the major coding-agent products launched explicit &ldquo;for work&rdquo; or &ldquo;for non-code tasks&rdquo; surfaces. OpenAI&#39;s 16 April 2026 Codex update &mdash; which the company itself titled <a href="https://openai.com/index/codex-for-almost-everything/" target="_blank" rel="noopener">&ldquo;Codex for (almost) everything&rdquo;</a> &mdash; explicitly repositioned a coding tool for knowledge work: operating your computer, working across apps like Slack, Gmail and Notion, remembering preferences, and scheduling its own future work. Anthropic pushed Claude into knowledge-work and creative settings over the same period. (A reported general-work product circulating under the name &ldquo;Orbit&rdquo; had not, as of mid-May 2026, been officially launched &mdash; treat it as a rumour until it ships.) The pattern, though, is real and on the record: the coding harness has become a general-purpose work harness.</p>

  <div class="case-study">
    <h4>&#127869;&#65039; Why this matters for a researcher</h4>
    <p>You do not need to write code to be affected by this. A coding agent that can read a folder of files, run a script, and edit a document is, functionally, a general research assistant that happens to have been built by people optimising for software tasks. Increasingly, the most capable &ldquo;do this multi-step thing for me&rdquo; tool available to a researcher is a coding agent wearing a different label.</p>
    <p>The flip side is that the caution travels with the capability. Everything Week 7 said about verifying AI-generated code &mdash; that plausible output can be silently wrong &mdash; now applies to a delegate that runs for an hour and touches many files before you see the result.</p>
  </div>

  <h2 class="section-title">&#129518; What This Means for Research Workflows</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">It is tempting to read all of this as &ldquo;AI is about to do research for us&rdquo;. That is the wrong framing, and the rest of this week is largely about why. The accurate framing is narrower and more useful: <strong>research workflows now routinely include long-running, tool-using delegates</strong>. The question is no longer &ldquo;can the model answer my question?&rdquo; but &ldquo;should I hand this multi-step task to an agent, and if so, how do I stay in control of what it does?&rdquo;</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">That shift raises the stakes on the Week 7 lesson about &ldquo;vibe coding&rdquo; &mdash; accepting AI-generated work without understanding it. When a chatbot writes a function, you can read the function. When an agent runs unsupervised for an hour, you inherit whatever it produced, and the surface area for silent error is far larger. The genre of &ldquo;developer inherits a vibe-coded codebase and finds the cleanup involves deleting millions of lines of accumulated machine-generated cruft&rdquo; became a recurring story on developer social media through 2025&ndash;26. The figures in any single anecdote are unverifiable, but the structural point is not: an unsupervised agent can accumulate a great deal of plausible-looking output, and a great deal of it can be wrong, before any human reviews it.</p>

  <div class="highlight-box">
    <h3>The frame for the week: the harness, not the model</h3>
    <p>Week 9 gave you a frame for capability claims: ask <em>which model, which date, has anyone retested</em>. Week 10 adds the layer above it. For an agent, the model is only one of five components, and often not the one that determines whether the thing works. So the agent-era version of the question is: <em>which model, in which harness, with which permissions, verified how?</em></p>
    <p>Hold onto that. In 10.2 we apply the Week 9 patched / reduced / structural failure taxonomy to agents specifically &mdash; because agents fail in genuinely new ways that single-turn chatbots did not.</p>
  </div>

  <div class="resource-placeholder">
    <h4>&#128214; Sources &amp; Further Reading</h4>
    <p><strong>Primary sources for the claims above:</strong></p>
    <ul class="styled-list">
      <li><a href="https://arxiv.org/abs/2603.28052" target="_blank" rel="noopener">Lee, Y., et al. (2026). <em>Meta-Harness: End-to-End Optimization of Model Harnesses.</em> arXiv:2603.28052</a> &mdash; the &ldquo;harness is the product&rdquo; thesis, with measured results.</li>
      <li><a href="https://arxiv.org/abs/2601.11868" target="_blank" rel="noopener">Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command-Line Interfaces. arXiv:2601.11868</a> &middot; <a href="https://www.tbench.ai/" target="_blank" rel="noopener">tbench.ai leaderboard</a> &mdash; the harness-run benchmark referenced above.</li>
      <li><a href="https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering" target="_blank" rel="noopener">LangChain, &ldquo;Improving Deep Agents with Harness Engineering&rdquo;</a> (17 February 2026) &mdash; the worked 52.8% &rarr; 66.5% example and exactly which harness changes produced it.</li>
      <li><a href="https://www.langchain.com/blog/deep-agents-0-6" target="_blank" rel="noopener">LangChain, &ldquo;Deep Agents 0.6&rdquo;</a> (13 May 2026) &mdash; the tau2-bench 10&ndash;20 point swings across models, and harness profiles for open-weight models (Kimi, Qwen, DeepSeek).</li>
      <li><a href="https://openai.com/index/codex-for-almost-everything/" target="_blank" rel="noopener">OpenAI, &ldquo;Codex for (almost) everything&rdquo;</a> (16 April 2026) &mdash; coding agent repositioned for knowledge work.</li>
      <li><a href="https://www.langchain.com/blog/interrupt-2026-overview" target="_blank" rel="noopener">LangChain, &ldquo;Everything we shipped at Interrupt&rdquo;</a> (13&ndash;14 May 2026) &mdash; harnesses sold as products.</li>
      <li><a href="https://www.anthropic.com/news/claude-for-creative-work" target="_blank" rel="noopener">Anthropic, &ldquo;Claude for Creative Work&rdquo;</a> (28 April 2026) &mdash; the nine free creative connectors.</li>
      <li><a href="https://x.com/AriX/status/2049932746567598472" target="_blank" rel="noopener">Ari Weinstein (OpenAI) on X</a> (30 April 2026; quoting his 16 April post) &mdash; the computer-use &ldquo;as fast as a person&rdquo; observation and the 42% speed-up. A first-party claim, cited as such.</li>
    </ul>
    <p style="margin-top: 12px;"><strong>For day-by-day tracking</strong> of these fast-moving developments, the <a href="https://www.latent.space/" target="_blank" rel="noopener">AINews / Latent Space</a> daily briefings are a useful aggregator &mdash; but note that they themselves aggregate company announcements and social-media posts, so trace any specific number back to its origin (as we have done here) before citing it. For a pragmatic practitioner&#39;s voice &mdash; including healthy scepticism about how much of this you actually need &mdash; <a href="https://simonwillison.net/tags/model-context-protocol/" target="_blank" rel="noopener">Simon Willison&#39;s ongoing writing</a> is consistently worth reading.</p>
  </div>

  <div class="intro-text" style="margin-top: 50px;">
    <h2>&#128073; What Comes Next</h2>
    <p><strong>Sub-Lesson 10.2 &mdash; Failure Modes for Multi-Step / Long-Horizon Tasks.</strong> Now that we have a working definition and the &ldquo;harness is the product&rdquo; frame, we turn to where agents break. We take the patched / reduced-but-persistent / structural taxonomy from Week 9.2 and apply it directly to agents &mdash; because running a model in a loop for many steps introduces failure modes that no single-turn chatbot ever had. The headline finding, from a February 2026 Princeton study: across 18 months and 14 models, agent <em>accuracy</em> improved substantially while agent <em>reliability</em> barely moved. Accuracy is not reliability, and for a researcher the gap between them is where the danger lives.</p>
  </div>
"""


# ---------------------------------------------------------------------------
# Sub-Lesson 10.2 — Agents: Failure Modes for Multi-Step / Long-Horizon Tasks
# ---------------------------------------------------------------------------

SL2_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>Week 9 gave us a taxonomy for how AI fails: some failures have been <em>patched</em>, some are <em>reduced but persistent</em>, and some are <em>structural</em> &mdash; baked into how the systems work and unlikely to be fixed by the next release. That taxonomy was built for single-turn chatbots. This sub-lesson applies it to agents, which fail in genuinely new ways because they do not answer once and stop. They run for many steps, accumulate state, call tools, and act on whatever those tools return.</p>
    <p>The single most important idea in this sub-lesson is a distinction: <strong>reliability is not accuracy</strong>. An agent can be more accurate than ever &mdash; better at any individual step &mdash; and still be unreliable, because reliability is about doing the whole multi-step task consistently, recovering from its own mistakes, and knowing when it is wrong. A February 2026 Princeton study put numbers on this: across 14 models and 18 months, accuracy improved substantially while reliability barely moved. For a researcher deciding whether to hand a task to an agent, the gap between those two things is exactly where the danger lives.</p>
    <p>As always, the framing is the durable part and the examples are the snapshot. The specific failure stories below will date; the three-category question &mdash; <em>is this patched, reduced, or structural?</em> &mdash; will not.</p>
  </div>

  <h2 class="section-title">&#9201;&#65039; Why Agents Need Their Own Failure Lesson</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">A chatbot makes one prediction and stops. If it is right 90% of the time, that is roughly your experience of it. An agent runs the model in a loop &mdash; dozens or hundreds of times for a single task &mdash; and three things change.</p>

  <ul class="styled-list">
    <li><strong>Errors compound.</strong> If each step is 95% reliable and the task takes twenty independent steps, the probability that <em>every</em> step is correct is roughly 0.95<sup>20</sup> &mdash; about 36%. High per-step accuracy can still produce a task that usually fails. This is the agentic version of the Week 7 silent-error problem: each step looks plausible, the end result is wrong.</li>
    <li><strong>State accumulates.</strong> The agent carries its own earlier outputs forward as context. An early mistake does not just cost one step &mdash; it poisons every step that depends on it, and the agent rarely notices.</li>
    <li><strong>The agent acts.</strong> A chatbot that hallucinates wastes your time. An agent that hallucinates can delete a file, send an email, or spend money &mdash; because it has tools and permissions (the harness components from 10.1). The cost of a failure is no longer just a wrong answer.</li>
  </ul>

  <div class="info-box">
    <h4>&#128202; Reliability &ne; accuracy &mdash; the definition that anchors this week</h4>
    <p><strong>Accuracy</strong> asks: when the agent acts, is the action correct? <strong>Reliability</strong> asks: across many runs and many steps, does the agent <em>consistently</em> complete the task, recover from its own errors, behave predictably, and avoid unsafe actions? You can improve the first without improving the second. A model that is more accurate per step but no better at the other things is a more capable component inside a system that is no more trustworthy.</p>
  </div>

  <h2 class="section-title">&#128451;&#65039; The Agent Failure Taxonomy</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Here is the Week 9.2 taxonomy, applied to agents. As before, the value is in placing a failure you encounter into the right category, because the category tells you what to do about it.</p>

  <!-- CATEGORY A -->
  <h3 style="color: #2a5298; font-size: 1.4em; margin: 30px 0 15px;">&#9989; (a) Patched / Largely Solved</h3>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Early agent demos (2023&ndash;24) failed in ways that have since been largely engineered away by the harness layer:</p>

  <ul class="styled-list">
    <li><strong>Malformed tool calls.</strong> Early agents frequently emitted tool requests that did not parse. Structured tool-calling APIs and constrained decoding have largely fixed this.</li>
    <li><strong>&ldquo;Forgetting&rdquo; available tools.</strong> Better system prompts and tool-discovery steps (exactly the harness changes in the LangChain worked example from 10.1) have substantially reduced this.</li>
    <li><strong>Trivially hallucinated tools.</strong> Calling a function that was never provided is now rare on short tasks, though it returns on long ones.</li>
  </ul>

  <p style="color: #555; line-height: 1.75; margin-top: 15px;">The lesson here mirrors 9.2: if you see one of these, you are probably using an old model or a thin harness. Switch to a current frontier tool and the problem usually disappears.</p>

  <!-- CATEGORY B -->
  <h3 style="color: #2a5298; font-size: 1.4em; margin: 30px 0 15px;">&#128737;&#65039; (b) Reduced but Persistent</h3>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">These are mitigated but resurface, especially on longer tasks. They are the failure modes most relevant to real research workflows in 2026:</p>

  <div class="card-grid">
    <div class="card">
      <h3>Loop instability</h3>
      <p>Agents get stuck repeating an edit, re-running a failing command, or oscillating between two states. Harnesses now ship explicit loop-detectors (again, see the LangChain recipe in 10.1) &mdash; which tells you the problem is real enough to need a dedicated mitigation.</p>
    </div>
    <div class="card">
      <h3>Over-eager action</h3>
      <p>Given write permissions, agents delete more than asked, refactor confidently in the wrong direction, or &ldquo;fix&rdquo; things that were not broken. The Week 9 pattern of confidently-defended wrong reasoning becomes confidently-executed wrong action.</p>
    </div>
    <div class="card">
      <h3>Sycophancy over long sessions</h3>
      <p>The Week 9 sycophancy finding (Sharma et al., 2023) intensifies in long agentic conversations: the longer the session and the more you push back, the more the agent drifts toward agreeing with you rather than the task.</p>
    </div>
    <div class="card">
      <h3>Confidence miscalibration over horizons</h3>
      <p>An agent&#39;s sense of &ldquo;I&#39;ve got this&rdquo; does not decay as a task gets longer and riskier, even though its actual success rate does. The confidence signal you might want to threshold on is least trustworthy exactly when you need it most.</p>
    </div>
  </div>

  <!-- CATEGORY C -->
  <h3 style="color: #2a5298; font-size: 1.4em; margin: 30px 0 15px;">&#129512; (c) Structural and Likely Persistent</h3>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">These follow from how agents work, not from fixable engineering gaps. They are the ones to design your workflow <em>around</em>, because the next model release will not remove them. Each gets its own section below: the reliability gap, long-horizon planning collapse, and prompt injection. Compositional brittleness &mdash; the compounding-error problem from the top of this lesson, and the same effect behind ProgramBench scoring 0% on whole-repository tasks in Week 9 &mdash; sits here too.</p>

  <h2 class="section-title">&#128201; Reliability Is Not Accuracy: The Princeton Finding</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The structural case is made most rigorously by a February 2026 paper from Princeton&#39;s Center for Information Technology Policy: <em>Towards a Science of AI Agent Reliability</em> (Rabanser, Kapoor, Kirgis, Liu, Utpala &amp; Narayanan). It is the agent-era counterpart to the Kalai et al. hallucination paper we met in Week 9 &mdash; a careful argument that a whole class of failure is structural, not a passing engineering problem.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The authors evaluated 14 models from OpenAI, Google, and Anthropic spanning 18 months of releases, across roughly 500 benchmark runs. Their headline finding is the one in this section&#39;s title:</p>

  <div class="highlight-box">
    <h3>Accuracy went up. Reliability did not.</h3>
    <p><em>&ldquo;Reliability has improved only modestly over 18 months, while accuracy improved substantially.&rdquo;</em> Compressing an agent&#39;s behaviour into a single success score, the authors argue, hides the operational flaws that actually determine whether you can depend on it.</p>
    <p>They decompose reliability into four dimensions &mdash; <strong>consistency, robustness, predictability, and safety</strong> &mdash; measured by twelve concrete metrics. The weakest, across the board, is <strong>predictability</strong>: <em>&ldquo;agents are not good at knowing when they&#39;re wrong.&rdquo;</em> On one benchmark, most models could not distinguish their own correct answers from their incorrect ones better than chance.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Two numbers make this concrete. Outcome <strong>consistency</strong> scores ranged from <strong>30% to 75%</strong> across the models tested &mdash; meaning that running the same agent on the same task under identical conditions often produced different outcomes. And because predictability is so weak, you cannot use the agent&#39;s own confidence as a filter: the &ldquo;ask it only when it&#39;s sure&rdquo; strategy fails, because it is not reliably sure when it should be.</p>

  <div class="warning-box">
    <h4>&#9888;&#65039; What this means for delegating a task</h4>
    <p>If you run an agent once and it succeeds, that is weak evidence it will succeed next time &mdash; outcome consistency can be as low as a coin flip. And you cannot lean on the agent to tell you when it has failed, because knowing-when-it&#39;s-wrong is its weakest skill. Both facts push in the same direction: <strong>the verification burden stays with you</strong>, and it is heavier for agents than for chatbots, not lighter. This is the Week 9 verification lesson, scaled up.</p>
  </div>

  <h2 class="section-title">&#129517; Long-Horizon Planning Collapse</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Why do long tasks fail so distinctively? A January 2026 paper, <em>Why Reasoning Fails to Plan</em> (Wang et al.), gives a structural answer that is worth understanding because it explains a failure you will see repeatedly.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The argument: the step-by-step reasoning that makes models good at short tasks is, formally, a <em>greedy</em> strategy &mdash; it picks the locally best next step. Greedy strategies are fine over short horizons. Over long ones they fail, because an early choice that looks locally optimal commits the agent to a path whose costs only show up much later, and those early commitments get <em>amplified over time and are difficult to recover from</em>. The authors prove the gap is <strong>structural, not a matter of model capability</strong>: a more powerful reasoner making step-wise decisions is still fundamentally limited on long-horizon tasks.</p>

  <div class="case-study">
    <h4>&#128161; The counter-intuitive result: small + planning beats large + greedy</h4>
    <p>The paper&#39;s most striking demonstration: with their lookahead method (FLARE), <em>&ldquo;LLaMA-8B with FLARE frequently outperforms GPT-4o with standard step-by-step reasoning&rdquo;</em> on long-horizon benchmarks. A small model that genuinely plans can beat a much larger model that merely reasons step by step.</p>
    <p>The research lesson is not &ldquo;use LLaMA-8B&rdquo;. It is that <em>reasoning is not planning</em>. When you see an agent handle each individual step competently and still walk the task into a wall, you are watching greedy step-wise reasoning fail at planning &mdash; a structural limitation, not a bug that more model scale will fix.</p>
  </div>

  <h2 class="section-title">&#128200; Watching Agents Run Long: Two 2026 Benchmarks</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">A new class of benchmark in 2026 stopped measuring single answers and started measuring whether an agent can hold a task together over a long horizon. Two are worth knowing, both because of what they measure and because they make the structural failures visible.</p>

  <div class="card-grid">
    <div class="card">
      <h3>YC-Bench &mdash; run a startup for a (simulated) year</h3>
      <p>YC-Bench (arXiv:2604.01212) tasks an agent with running a simulated startup over a one-year horizon spanning hundreds of turns &mdash; managing employees, choosing contracts, and staying profitable while adversarial clients and rising payroll create compounding consequences. It is long-horizon planning made measurable.</p>
      <p style="font-size: 0.95em; color: #003A70;">Top result: Claude Opus 4.6 at $1.27M average final funds &mdash; with the much cheaper GLM-5 (from China&#39;s Zhipu AI) close behind at $1.21M for roughly 11&times; lower inference cost. A preview of the lower-cost and Chinese-model story we develop in 10.5.</p>
    </div>
    <div class="card">
      <h3>The &ldquo;Meltdown Onset Point&rdquo;</h3>
      <p><em>Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents</em> (arXiv:2603.29231) evaluated 10 models across 23,392 episodes and introduced metrics for how agents fall apart over time &mdash; including a <strong>Meltdown Onset Point</strong> that detects behavioural collapse by watching the agent&#39;s tool-call patterns become erratic.</p>
      <p style="font-size: 0.95em; color: #003A70;">That a benchmark needs a dedicated &ldquo;meltdown&rdquo; metric tells you the phenomenon is common enough to formalise: past some task length, agents do not just get things wrong, they come apart.</p>
    </div>
  </div>

  <h2 class="section-title">&#128137; Prompt Injection: The Structural Security Hole</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">One structural failure deserves singling out because it is a security problem, not just a reliability one. An agent reads tool output &mdash; web pages, file contents, emails, search results &mdash; and acts on it. If an attacker can place text in that content, they can try to issue instructions to your agent. This is <strong>prompt injection</strong>, and the practitioner who has tracked it most closely, Simon Willison, has made the uncomfortable point repeatedly: we have known about it since 2022 and still have no robust, general defence.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">For a researcher this is concrete. If you point an agent at the open web, or at a shared document, or at your inbox, you are trusting every piece of content it reads not to contain hostile instructions &mdash; and the agent has no reliable way to tell data from commands, because to a language model they are both just text. The mitigation is not technical cleverness on your side; it is the <em>permissions</em> dial from 10.1. An agent that can only read is far harder to weaponise than one that can also send, delete, or pay.</p>

  <div class="info-box">
    <h4>&#127765; An African-context note: where the agent acts matters</h4>
    <p>Prompt injection and the permissions dial are not abstractions when an agent touches real systems. An agent with access to a university inbox, a grant portal, or institutional data is acting inside systems governed by South Africa&#39;s Protection of Personal Information Act (POPIA). The structural insecurity of agents is one more reason the verification and permissioning burden cannot be delegated &mdash; a theme we return to concretely in the Week 10 activity, where you will be asked to state where your tools send data before you use them.</p>
  </div>

  <h2 class="section-title">&#129519; Putting the Taxonomy to Work</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">As in Week 9, the point of the taxonomy is action. When you observe an agent failure, locate it &mdash; the category tells you what to do.</p>

  <div style="overflow-x: auto;">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Observed failure</th>
          <th>Category</th>
          <th>What to do</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Agent emits a broken tool call or forgets it has a tool</td>
          <td>Patched</td>
          <td>You&#39;re on an old model or thin harness. Switch to a current frontier tool.</td>
        </tr>
        <tr>
          <td>Agent gets stuck in a loop or re-runs a failing step</td>
          <td>Reduced but persistent</td>
          <td>Use a harness with loop-detection; cap the number of steps; watch it rather than walking away.</td>
        </tr>
        <tr>
          <td>Agent deletes or changes more than you asked</td>
          <td>Reduced but persistent</td>
          <td>Turn down the permissions dial. Run read-only or in a sandbox until you trust the task.</td>
        </tr>
        <tr>
          <td>Agent succeeds once; you assume it always will</td>
          <td>Structural (consistency)</td>
          <td>Don&#39;t. Outcome consistency can be 30&ndash;75%. Re-run, or verify the output directly.</td>
        </tr>
        <tr>
          <td>Agent handles each step well but walks the whole task into a wall</td>
          <td>Structural (planning)</td>
          <td>Long-horizon planning collapse. Break the task into shorter, checkpointed pieces you verify between.</td>
        </tr>
        <tr>
          <td>Agent acts on a web page / email / document that contained instructions</td>
          <td>Structural (prompt injection)</td>
          <td>Assume any content the agent reads may be hostile. Restrict permissions; never give a web-reading agent send/pay/delete rights you wouldn&#39;t give a stranger.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="highlight-box">
    <h3>The skill is the taxonomy, not the examples</h3>
    <p>The specific tools and figures in this sub-lesson will date within months. What persists is the move: when an agent fails, ask whether the failure is patched (you&#39;re using the wrong tool), reduced-but-persistent (manage it with harness settings and supervision), or structural (design your workflow around it, because the next release will not save you).</p>
    <p>And the one structural fact to carry forward: <em>accuracy is not reliability</em>. More capable agents are not automatically more trustworthy ones. The trust has to be earned per task, by you, through verification.</p>
  </div>

  <div class="resource-placeholder">
    <h4>&#128214; Sources &amp; Further Reading</h4>
    <ul class="styled-list">
      <li><a href="https://arxiv.org/abs/2602.16666" target="_blank" rel="noopener">Rabanser, S., Kapoor, S., Kirgis, P., Liu, K., Utpala, S., &amp; Narayanan, A. (2026). <em>Towards a Science of AI Agent Reliability.</em> arXiv:2602.16666</a> (Princeton CITP) &mdash; reliability vs accuracy; four dimensions; the predictability finding.</li>
      <li><a href="https://arxiv.org/abs/2601.22311" target="_blank" rel="noopener">Wang, Z., et al. (2026). <em>Why Reasoning Fails to Plan: A Planning-Centric Analysis of Long-Horizon Decision Making in LLM Agents.</em> arXiv:2601.22311</a> &mdash; planning collapse is structural; FLARE; small-plus-planning beats large-plus-greedy.</li>
      <li><a href="https://arxiv.org/abs/2604.01212" target="_blank" rel="noopener">YC-Bench: Benchmarking AI Agents for Long-Term Planning and Consistent Execution. arXiv:2604.01212</a> &mdash; the simulated-startup long-horizon benchmark.</li>
      <li><a href="https://arxiv.org/abs/2603.29231" target="_blank" rel="noopener">Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents. arXiv:2603.29231</a> &mdash; reliability-decay and the Meltdown Onset Point.</li>
      <li><a href="https://arxiv.org/abs/2509.04664" target="_blank" rel="noopener">Kalai, A. T., Nachum, O., Vempala, S. S., &amp; Zhang, E. (2025). <em>Why Language Models Hallucinate.</em> arXiv:2509.04664</a> &mdash; the single-turn parent of the agent reliability problem (from Week 9).</li>
      <li><a href="https://simonwillison.net/tags/prompt-injection/" target="_blank" rel="noopener">Simon Willison on prompt injection</a> &mdash; the standing argument that we still lack a robust general defence.</li>
    </ul>
  </div>

  <div class="intro-text" style="margin-top: 50px;">
    <h2>&#128073; What Comes Next</h2>
    <p><strong>Sub-Lesson 10.3 &mdash; The Current Tool Landscape (Including MCP).</strong> Having defined agents (10.1) and mapped how they fail (10.2), we get concrete about the tools themselves: the coding, computer-use, research, and general agents available in May 2026, and the Model Context Protocol (MCP) that increasingly connects them to your data. We carry the permissions-dial and reliability lessons straight into that tour &mdash; because choosing an agent tool is, in large part, choosing how much you are willing to let it do on your behalf.</p>
  </div>
"""


# ---------------------------------------------------------------------------
# Sub-Lesson 10.3 — The Current Tool Landscape (Including MCP)
# ---------------------------------------------------------------------------

SL3_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>This is the practical sub-lesson: a tour of the agent tools that actually exist in May 2026, organised by what they do. We cover three families here &mdash; coding agents, computer-use and browser agents, and the connector layer (MCP) that links agents to your data. The fourth family, research agents (&ldquo;Deep Research&rdquo; modes), gets its own treatment in 10.4, and the full honest free-versus-paid tool comparison &mdash; including Chinese options &mdash; lands in 10.5.</p>
    <p>Two commitments carry through. First, every capability number is time-stamped and will date; treat the trajectory as the lesson and the figures as a snapshot. Second, we keep asking the question that matters most for a UCT student: <strong>what can you actually use without a credit card?</strong> The answer is more encouraging than you might expect, but it requires knowing where to look.</p>
    <p>And we carry forward the two ideas from 10.1 and 10.2: an agent is a model plus a harness, and an agent&#39;s reliability is not the same as its accuracy. Both shape how you should read every claim a tool vendor makes.</p>
  </div>

  <h2 class="section-title">&#128187; Coding Agents</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Coding agents are the most mature family, and &mdash; as we saw in 10.1 &mdash; increasingly the most capable <em>general</em> agents too, because a tool that can read a folder, run a command, and edit a document is a research assistant whether or not the documents are code. The leaders as of May 2026 are Claude Code (Anthropic), Codex (OpenAI), and Cursor, with Cline and opencode as prominent open alternatives.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The honest access picture: <strong>the most capable coding agents are paid.</strong> Claude Code, Codex, and Cursor all sit behind subscriptions, and through 2026 the pricing models shifted repeatedly as the companies worked out how to charge for long-running, compute-hungry agents. For a student without a subscription, the realistic free routes are (a) the open-source agent frameworks &mdash; Cline, opencode, and LangChain&#39;s open <em>deepagents</em> &mdash; which you can point at a free or low-cost model, and (b) running a smaller open-weight coding model locally if you have a capable GPU. Both require setup and neither matches the polished paid tools, so we do not build the Week 10 activity around coding agents (see 10.6). They are best treated, for now, as a powerful option you should know exists rather than a baseline everyone can reach.</p>

  <div class="info-box">
    <h4>&#128218; The connection to Week 7</h4>
    <p>Everything Week 7 said about verifying AI-generated code applies with more force here. A chatbot writes a function you can read; a coding agent runs for an hour and hands you a result built from many steps, any of which could be silently wrong (10.2&#39;s compounding-error problem). The more autonomous the coding agent, the more the verification burden grows &mdash; not shrinks.</p>
  </div>

  <h2 class="section-title">&#128433;&#65039; Computer-Use Agents</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">A computer-use agent drives a graphical interface the way a person does &mdash; it looks at the screen, then clicks and types. The &ldquo;looks at the screen&rdquo; part is the same vision-language technology from Week 8: the agent reads screen pixels exactly as it reads a scientific figure, and it inherits Week 8&#39;s failure modes (it can describe what it sees far more reliably than it can extract precise values from it). The point of computer-use agents is that they work with any software, including the many tools that have no API.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The standard benchmark is <strong>OSWorld</strong> &mdash; 369 real tasks across desktop applications. Its trajectory is one of the steepest in AI:</p>

  <div style="overflow-x: auto;">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>When</th>
          <th>System</th>
          <th>OSWorld score</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>January 2025</td>
          <td>OpenAI&#39;s first computer-use agent, at launch</td>
          <td>38.1%</td>
        </tr>
        <tr>
          <td>&mdash;</td>
          <td><strong>Human baseline (estimated)</strong></td>
          <td><strong>~72%</strong></td>
        </tr>
        <tr>
          <td>Late 2025</td>
          <td>Simular Agent S2 &mdash; first agent to cross the human baseline</td>
          <td>72.6%</td>
        </tr>
        <tr>
          <td>March 2026</td>
          <td>GPT-5.4 (OSWorld-Verified)</td>
          <td>75.0%</td>
        </tr>
        <tr>
          <td>May 2026<br>(leaderboard top, clustered)</td>
          <td>Claude Mythos Preview<br>GPT-5.5<br>Gemini 3.5 Flash<br>Claude Opus 4.7</td>
          <td>79.6%<br>78.7%<br>78.4%<br>78.0%</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 18px; margin-bottom: 15px;">By the time you read this, those May 2026 figures will already be wrong &mdash; the public OSWorld-Verified leaderboard was reshuffling week to week as this was written, with newer preview models displacing the ones named here. That is not a flaw in the table; it <em>is</em> the lesson. Check <a href="https://llm-stats.com/benchmarks/osworld-verified" target="_blank" rel="noopener">the live leaderboard</a> for today&#39;s standings, and read whatever you find there through the caveat below.</p>

  <div class="warning-box">
    <h4>&#9888;&#65039; &ldquo;Beats the human baseline&rdquo; does not mean &ldquo;does your work&rdquo;</h4>
    <p>It is true and striking that computer-use agents now match or exceed the average human score on OSWorld. But read that claim through 10.2. OSWorld is 369 specific, well-defined tasks &mdash; a narrow slice of what &ldquo;using a computer&rdquo; means. A benchmark score is a single-number summary of exactly the kind that the Princeton reliability work warns hides operational flaws. In real, open-ended workflows, computer-use agents remain fragile: they misclick, they lose the thread on long tasks, and &mdash; per 10.2 &mdash; their outcome consistency is far below 100%. The honest summary is the one from 10.1: the bottleneck has moved from speed to judgement, not disappeared.</p>
  </div>

  <h2 class="section-title">&#127760; Agentic Browsers</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">A growing category wraps a computer-use agent inside a web browser, so it can browse, fill forms, and carry out multi-step web tasks on your behalf. For UCT students, one of these is genuinely accessible:</p>

  <div class="card-grid">
    <div class="card">
      <h3>Comet (Perplexity) &mdash; free, worldwide</h3>
      <p>Perplexity&#39;s agentic browser. After a paywalled 2025 launch, Comet became <strong>free for all Perplexity account holders in 2026</strong>, across iOS, Android, Mac and Windows, with no regional restriction &mdash; which means it works from South Africa without a subscription or a foreign card. The free tier includes the assistant that answers questions and summarises pages; paid plans add a background assistant for longer multi-step tasks.</p>
    </div>
    <div class="card">
      <h3>Dia &amp; ChatGPT Atlas</h3>
      <p>Dia (from the team behind the Arc browser) and OpenAI&#39;s ChatGPT-integrated browsing are two other entrants. Availability and free tiers shift constantly; verify current access before relying on either. The category as a whole is young and the products are not yet stable.</p>
    </div>
  </div>

  <div class="warning-box">
    <h4>&#9888;&#65039; Agentic browsers are a prompt-injection magnet</h4>
    <p>This is 10.2&#39;s structural security hole at its most exposed. An agentic browser reads whatever web page you send it to &mdash; and any page can contain hidden instructions aimed at your agent. Never give a browsing agent the ability to act on accounts that matter (email, banking, institutional systems) while it roams the open web. Keep the permissions dial low: let it read and summarise, not send, buy, or delete.</p>
  </div>

  <h2 class="section-title">&#129300; Manus and the &ldquo;General Agent&rdquo; Claim</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Manus is worth discussing precisely because it is a good case study in reading agent hype critically. Launched in invitation-only beta in March 2025 by Butterfly Effect (a Chinese-founded company that relocated to Singapore), it was marketed as a <em>general</em> autonomous agent &mdash; give it a goal, walk away, come back to a finished task. The launch demos generated enormous attention and a thriving secondary market in invitation codes.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Apply the week&#39;s discipline. Manus&#39;s headline capability claims are <strong>company-reported</strong>, and independent replication has been scarce &mdash; exactly the situation 10.1 and 10.2 tell you to treat cautiously, because a polished demo is a best case, not a reliability measurement. What is independently documented is the regulatory drama: in April 2026, China&#39;s National Development and Reform Commission <strong>blocked Meta&#39;s reported $2&nbsp;billion acquisition of Manus</strong>, following a Ministry of Commerce investigation earlier in the year. That is a verifiable fact about the company; the &ldquo;it can do anything&rdquo; framing is not. Useful tool, genuine engineering &mdash; but a textbook example of why you separate what a vendor claims from what has been measured.</p>

  <h2 class="section-title">&#128268; MCP: The Connector Layer</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The Model Context Protocol (MCP) is the plumbing that lets an agent connect to your tools and data through a single standard interface &mdash; often described as &ldquo;USB-C for AI&rdquo;. Instead of every tool needing a bespoke integration with every model, a tool exposes an MCP server once and any MCP-speaking agent can use it.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">MCP matters in 2026 because it stopped being one vendor&#39;s idea and became a cross-industry standard with remarkable speed. Anthropic introduced it in November 2024; OpenAI adopted it in March 2025; Google followed in April 2025. In December 2025 Anthropic donated the protocol to a Linux Foundation body (the Agentic AI Foundation, co-founded with Block and OpenAI), so it is now governed in the open rather than controlled by one company. In barely a year it went from a single company&#39;s proposal to a standard that all the major model providers speak &mdash; which is why it is worth a researcher&#39;s attention rather than just a developer&#39;s.</p>

  <div class="info-box">
    <h4>&#128300; Why a researcher should care</h4>
    <p>MCP is what will connect agents to the tools you already use. MCP servers exist (or are emerging) for reference managers like <strong>Zotero</strong>, for <strong>GitHub</strong>, <strong>Google Drive</strong>, <strong>Notion</strong>, and more &mdash; meaning an agent can search your library, read your repository, or draft in your notes through one standard. On Claude.ai, a set of connectors is available even on the <em>free</em> plan (the nine creative connectors from 10.1 are MCP under the hood). We return to the specific research-relevant connectors, and how to use them safely, in 10.5.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The protocol&#39;s own March 2026 roadmap signals where it is heading: scaling the transport layer for production, refining agent-to-agent communication, maturing open governance, and enterprise features like audit trails and authentication &mdash; an evolution &ldquo;from releases to working groups&rdquo; that marks MCP&#39;s shift from experiment to infrastructure.</p>

  <div class="warning-box">
    <h4>&#9888;&#65039; The pragmatic and the security caveats</h4>
    <p>Two cautions. First, practically: MCP is not always the right tool. Simon Willison &mdash; among the most careful practitioner voices &mdash; has argued that for a lot of agent work, plain command-line utilities are simpler and more reliable than wiring up an MCP server. MCP is a standard, not a magic wand. Second, and more seriously: anything an agent reads through MCP is untrusted content, so MCP is another channel for the prompt injection from 10.2. A connector that can both read your email and browse the web is exactly the kind of capability combination that turns a hidden instruction on a web page into an action on your inbox. Connect deliberately; keep the permissions dial low.</p>
  </div>

  <h2 class="section-title">&#129517; Reading the Frontier: Real, Overclaimed, and Vapour</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">A closing honesty note &mdash; but in the spirit of Week 9, the honest move is calibration in <em>both</em> directions, not blanket scepticism. Some frontier agent claims are genuine and shipping; some are real but overclaimed; some are still vapour. The skill is telling them apart. Three examples that are easy to get wrong in either direction.</p>

  <div class="case-study">
    <h4>&#129516; Autonomous science: real milestones, overclaimed framing</h4>
    <p>It would be wrong to dismiss autonomous-science agents as vapour. The milestones are real and documented. Sakana AI&#39;s <em>AI Scientist-v2</em> produced a fully AI-generated manuscript that cleared peer review at an ICLR 2025 workshop &mdash; the first time a start-to-finish AI-written paper passed human review. DeepMind&#39;s <em>AlphaEvolve</em> discovered a way to multiply two 4&times;4 complex matrices using 48 scalar multiplications, improving on a record that had stood since 1969. Hypothesis-generation agents like DeepMind&#39;s <em>Co-Scientist</em> and FutureHouse&#39;s <em>Robin</em> are being used in real labs. These sit alongside the Week 9 results &mdash; Erd&#337;s problems, gluon amplitudes &mdash; as genuine AI contributions to research.</p>
    <p>What is overclaimed is the framing &ldquo;the AI did the science&rdquo;. The workshop paper passed a deliberately lower bar than a main conference and was withdrawn by agreement; the system still makes errors a reviewer must catch. Most of these tools <em>generate hypotheses or optimise within a well-defined space</em> &mdash; the human still frames the problem, validates the result, and supplies the novel data the agent cannot gather itself. As one assessment put it, we are likely years from autonomous &ldquo;true innovation&rdquo;. So: real and accelerating, genuinely useful &mdash; and not the end-to-end autonomous discovery the headlines imply. Both halves are true.</p>
  </div>

  <div class="case-study">
    <h4>&#128260; Self-improving agents: bootstrapping is real; recursive self-improvement is not (yet)</h4>
    <p>Here too the honest answer is &ldquo;partly real&rdquo;. AI coding tools are now substantially used to build themselves: Anthropic engineers write much of Claude Code <em>using</em> Claude Code, and the Meta-Harness research from 10.1 automates the search for better harnesses. That is genuine bootstrapping &mdash; the tools are accelerating their own development, and it is not hype to say so.</p>
    <p>But it is human-directed bootstrapping, not the autonomous recursive self-improvement the term usually invokes. An engineer wields Claude Code to write Claude Code faster, including reviewing and deciding what ships; the agent is not, on its own, rewriting itself in a closed loop and getting recursively more capable without people. &ldquo;AI-accelerated development of AI tools&rdquo; (real, shipping, important) is a different claim from &ldquo;agents autonomously improving themselves&rdquo; (not what is happening). Keep the two apart and you will read this corner of the hype accurately.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 20px; margin-bottom: 15px;">And some things genuinely are just vapour or rumour as of mid-May 2026 &mdash; for example the Anthropic general-work product circulating under the codename &ldquo;Orbit&rdquo; (from 10.1), which had not officially launched. A codename is not a product, and a demo is not a deployment. The pattern across all three examples is the same: find the verified core, name the overclaim around it, and do not let either the hype or the backlash do your thinking for you.</p>

  <div class="highlight-box">
    <h3>How to read this whole landscape</h3>
    <p>Three questions cut through almost any agent-tool announcement. <strong>Which harness?</strong> (10.1 &mdash; the model name alone tells you little.) <strong>How reliable, not just how accurate?</strong> (10.2 &mdash; a demo is a best case.) <strong>What can I actually access for free, from here?</strong> (this week&#39;s throughline.) Hold those three up against every tool below and in 10.5, and you will not be badly misled.</p>
  </div>

  <div class="resource-placeholder">
    <h4>&#128214; Sources &amp; Further Reading</h4>
    <ul class="styled-list">
      <li><a href="https://llm-stats.com/benchmarks/osworld-verified" target="_blank" rel="noopener">OSWorld-Verified leaderboard</a> and <a href="https://xlang.ai/blog/osworld-verified" target="_blank" rel="noopener">XLANG Lab, &ldquo;Introducing OSWorld-Verified&rdquo;</a> &mdash; the computer-use benchmark, human baseline, and current standings.</li>
      <li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol" target="_blank" rel="noopener">Model Context Protocol (Wikipedia)</a> &mdash; the cross-vendor adoption timeline and Linux Foundation governance.</li>
      <li><a href="https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/" target="_blank" rel="noopener">MCP 2026 Roadmap</a> (9 March 2026) &mdash; the protocol&#39;s own stated priorities.</li>
      <li><a href="https://simonwillison.net/tags/model-context-protocol/" target="_blank" rel="noopener">Simon Willison on MCP</a> &mdash; the pragmatic critique that MCP is not always the best abstraction.</li>
      <li><a href="https://www.perplexity.ai/comet" target="_blank" rel="noopener">Perplexity Comet</a> &middot; <a href="https://www.cnbc.com/2025/10/02/perplexity-ai-comet-browser-free-.html" target="_blank" rel="noopener">CNBC on Comet going free</a> &mdash; the free agentic browser accessible from South Africa.</li>
      <li><a href="https://en.wikipedia.org/wiki/Manus_(AI_agent)" target="_blank" rel="noopener">Manus (Wikipedia)</a> &mdash; origin and the blocked Meta acquisition; note its capability claims are company-reported.</li>
      <li><a href="https://arxiv.org/abs/2504.08066" target="_blank" rel="noopener">Sakana AI, <em>The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search</em>. arXiv:2504.08066</a> &mdash; the autonomous-paper-through-peer-review milestone, with its own caveats.</li>
      <li><a href="https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/" target="_blank" rel="noopener">Google DeepMind, &ldquo;AlphaEvolve&rdquo;</a> &mdash; the 4&times;4 complex-matrix algorithm (48 multiplications) that improved on Strassen&#39;s 1969 record after 56 years.</li>
      <li><a href="https://cen.acs.org/articles/104/web/2026/05/ai-companies-introduce-agent-based-research-tools.html" target="_blank" rel="noopener">C&amp;EN (May 2026), &ldquo;AI companies introduce new agent-based tools for scientific discovery&rdquo;</a> &mdash; overview of Co-Scientist, Robin, and the realistic limits.</li>
    </ul>
  </div>

  <div class="intro-text" style="margin-top: 50px;">
    <h2>&#128073; What Comes Next</h2>
    <p><strong>Sub-Lesson 10.4 &mdash; RAG in 2026.</strong> We deferred the research-agent family to its own lesson, and here it is. Retrieval-augmented generation was the backbone of the literature tools in Week 5; we look at what has changed since &mdash; how much longer context windows have eroded the need for naive retrieval, where &ldquo;agentic RAG&rdquo; wins it back, and why evaluating any of this remains genuinely hard. Deep Research modes &mdash; the research agents &mdash; sit right at the centre of that story.</p>
  </div>
"""


# ---------------------------------------------------------------------------
# Sub-Lesson 10.4 — RAG in 2026
# ---------------------------------------------------------------------------

SL4_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>Week 5 introduced retrieval-augmented generation (RAG) as the engine behind the AI literature tools &mdash; the technique of fetching relevant documents and feeding them to a model so its answer is grounded in real sources rather than its training data alone. Those tools and that technique are still central. But three things have shifted since Week 5, and this sub-lesson is about all three.</p>
    <p>First, <strong>long context</strong>: frontier models now routinely accept a million tokens or more, which changes when you need retrieval at all. Second, <strong>agentic RAG</strong>: retrieval has moved from a single fetch-then-answer step to a loop in which the model plans, retrieves, reads, and retrieves again &mdash; and the Deep Research modes you have heard about are exactly this. Third, <strong>evaluation</strong>: we now have frameworks for measuring whether a RAG system is any good, though the hardest cases remain open.</p>
    <p>The honest verdict, which we build to: for reading one long document, just use long context; for synthesising across many sources, agentic RAG still wins; and for anything you will cite, the Week 5 verification protocols apply regardless of which method produced the answer. None of this removes the researcher from the loop.</p>
  </div>

  <h2 class="section-title">&#128214; Recap: What Week 5 Established</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Week 5 mapped a landscape of AI literature tools &mdash; Elicit, Consensus, NotebookLM, Perplexity, Connected Papers, ResearchRabbit &mdash; and a hard warning: the hallucinated-citation crisis is real. Both still hold in 2026. The tools have improved; the warning has not expired.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">In the Week 9 taxonomy, hallucinated citations are a <em>reduced-but-persistent</em> failure: far less common on well-covered topics than in 2023, but still present, and concentrated exactly where research lives &mdash; the niche, the recent, the long-tail. RAG was always partly a response to this: ground the model in retrieved sources and it has less need to invent them. That logic is intact. What has changed is how the grounding is done.</p>

  <h2 class="section-title">&#128220; Change One: Long Context vs Retrieval</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">In Week 5, a model&#39;s context window was small enough that you <em>had</em> to retrieve: you could not simply paste a stack of papers in. By 2026, frontier models accept a million tokens or more (the Gemini Pro tier from Week 8 being the standard example) &mdash; enough for hundreds of pages at once. So a fair question is whether retrieval is still needed at all, or whether you should just dump everything into the context window and ask.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The most-cited study on this is Li et al. (2024), <em>Retrieval Augmented Generation or Long-Context LLMs?</em> (Google; EMNLP 2024). Their finding, in their words: <em>&ldquo;when resourced sufficiently, [long context] consistently outperforms RAG in terms of average performance. However, RAG&#39;s significantly lower cost remains a distinct advantage.&rdquo;</em> They proposed a hybrid, &ldquo;Self-Route&rdquo;, that routes each query to whichever approach suits it &mdash; cutting cost while keeping long-context quality.</p>

  <div class="warning-box">
    <h4>&#9888;&#65039; Two caveats on the long-context win</h4>
    <p>First, that study is from 2024, tested on the long-context models of the time. Treat it as evidence of the <em>shape</em> of the trade-off, not the current margins &mdash; the Week 9 &ldquo;which model, which date&rdquo; discipline applies.</p>
    <p>Second, and more important: an advertised context length is not the same as reliable recall across the whole of it. A model that <em>accepts</em> a million tokens does not necessarily <em>use</em> all of them well; recall tends to sag in the middle of very long inputs, and practitioners in 2026 still report that a model&#39;s true working-memory across a giant context is well short of the advertised number. &ldquo;It fits&rdquo; is not &ldquo;it was read carefully.&rdquo;</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The practical upshot: for analysing a <em>single</em> long document where everything relevant is in front of the model, long context is simpler and usually better. For drawing on a large or open-ended body of sources &mdash; where you cannot fit it all, and where the model needs to decide what to look at next &mdash; you still want retrieval. And that is where the second change comes in.</p>

  <h2 class="section-title">&#128257; Change Two: Agentic RAG</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Classic RAG is a single shot: retrieve a set of passages once, then generate an answer from them. Its weakness is obvious for real research questions &mdash; if the first retrieval misses, the answer is built on the wrong sources, and the system never reconsiders. <strong>Agentic RAG</strong> turns the single shot into a loop.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The canonical reference is Singh et al. (2025), <em>Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG</em>, which describes how agentic RAG <em>&ldquo;transcends these limitations by embedding autonomous AI agents into the RAG pipeline.&rdquo;</em> In plain terms, the agent does what a careful researcher does:</p>

  <ul class="step-list">
    <li><strong>Plan</strong> &mdash; break the question into sub-questions.</li>
    <li><strong>Retrieve</strong> &mdash; search for sources on the first sub-question.</li>
    <li><strong>Read and reflect</strong> &mdash; work out what was learned and what is still missing.</li>
    <li><strong>Retrieve again</strong> &mdash; run follow-up searches based on what the first round turned up (this is the step classic RAG cannot do).</li>
    <li><strong>Synthesise and check</strong> &mdash; assemble an answer and, in better systems, verify claims against the retrieved sources.</li>
  </ul>

  <p style="color: #555; line-height: 1.75; margin-top: 15px; margin-bottom: 15px;">This loop is just the agent definition from 10.1 (model + tools + loop + memory) pointed at a retrieval tool. And it is not a research curiosity: <strong>the &ldquo;Deep Research&rdquo; modes</strong> in the major assistants &mdash; which take a question, spend several minutes searching and reading, and return a cited report &mdash; are agentic RAG in consumer form. When you use one, you are running a planner-retriever-synthesiser loop, with all the strengths and the 10.2 reliability caveats that implies. We compare the specific Deep Research tools, free tiers included, in 10.5.</p>

  <h2 class="section-title">&#128207; Change Three: Can You Tell If It&#39;s Any Good?</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">If a RAG system can retrieve the wrong sources and still produce a fluent answer, how do you measure quality? The most widely-adopted answer is <strong>RAGAS</strong> (Es, James, Espinosa-Anke &amp; Schockaert, 2023) &mdash; a framework that scores a RAG system without needing hand-written gold answers for every question. Its widely-used metrics separate the two places RAG can fail:</p>

  <ul class="styled-list">
    <li><strong>Context precision &amp; context recall</strong> &mdash; did the <em>retrieval</em> step fetch the relevant passages, and only those?</li>
    <li><strong>Faithfulness</strong> &mdash; is the <em>generated answer</em> actually supported by the retrieved passages, or did the model add unsupported claims?</li>
    <li><strong>Answer relevancy</strong> &mdash; does the answer actually address the question asked?</li>
  </ul>

  <div class="warning-box">
    <h4>&#9888;&#65039; What these metrics do and do not tell you</h4>
    <p>The crucial limitation: <strong>faithfulness is not correctness</strong>. An answer can be perfectly faithful to its retrieved passages &mdash; inventing nothing beyond them &mdash; and still be wrong, because the passages themselves were wrong, outdated, or cherry-picked. RAGAS checks that the model did not hallucinate <em>beyond its sources</em>; it cannot check that the sources were right. That second check is yours.</p>
    <p>Two further caveats: RAGAS uses a strong &ldquo;judge&rdquo; model to score, so it inherits that model&#39;s blind spots; and the hardest cases &mdash; multi-hop questions that require chaining several retrievals, and judging how well an agent compacted a huge context &mdash; remain operationally hard to evaluate even in 2026.</p>
  </div>

  <h2 class="section-title">&#9878;&#65039; The Honest Verdict for May 2026</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Pulling the three changes together, here is how to choose, as a researcher, for a given task:</p>

  <div style="overflow-x: auto;">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Your task</th>
          <th>Best approach (May 2026)</th>
          <th>Why</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Analyse one long document (a thesis, a report, a contract)</td>
          <td>Long context &mdash; paste it in</td>
          <td>Everything relevant fits; retrieval adds complexity for no gain.</td>
        </tr>
        <tr>
          <td>Synthesise across many sources or the open literature</td>
          <td>Agentic RAG / Deep Research</td>
          <td>The model needs to decide what to read next; follow-up retrieval is the whole point.</td>
        </tr>
        <tr>
          <td>Anything you will cite in your own work</td>
          <td>Either &mdash; then verify by hand</td>
          <td>The Week 5 citation checks apply regardless of method. Faithful &ne; correct.</td>
        </tr>
        <tr>
          <td>High-volume / repeated querying on a budget</td>
          <td>RAG</td>
          <td>RAG&#39;s lower cost is its standing advantage (Li et al.); stuffing a million tokens in per query is expensive.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="info-box">
    <h4>&#129504; A Week 9.4 warning that sharpens here</h4>
    <p>Messeri &amp; Crockett warned (Week 9.4) that AI can create &ldquo;monocultures of knowing&rdquo; &mdash; everyone funnelled toward the same sources and framings. Agentic RAG intensifies the risk, because now the <em>agent</em> decides what to retrieve, what counts as relevant, and what to leave out &mdash; and it does so invisibly, in a loop you do not see. A Deep Research report that reads as comprehensive may rest on a narrow, agent-chosen slice of the literature. The friction that retrieval used to add &mdash; you, deciding what to read &mdash; was doing useful epistemic work. Automating it away is convenient and quietly costly.</p>
  </div>

  <h2 class="section-title">&#127757; RAG, Local Corpora, and the Equity Angle</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">There is a genuinely hopeful version of RAG for African and other under-represented research contexts. Frontier models are trained predominantly on high-resource languages and well-digitised corpora; they know comparatively little about, say, isiXhosa scholarship or region-specific datasets. RAG offers a route around this: ground the model in a <em>local</em> corpus it was never trained well on, and it can work with material outside its training distribution.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The catch is in the retrieval layer. RAG works by converting text into embeddings (numerical representations) and matching on them &mdash; and the embedding models are themselves trained mostly on high-resource languages. If the embedding layer cannot represent isiXhosa or Setswana well, retrieval over an isiXhosa corpus will be poor no matter how good the generating model is. So the equity promise is real but conditional: <strong>RAG can ground frontier models in local knowledge only as well as the retrieval layer handles the local language</strong>, and as of 2026 most embedding models handle African languages poorly. This connects directly to the sovereign-capacity questions of Week 11 &mdash; the Esethu Framework (Rajab et al., 2025) argues for exactly this kind of locally-grounded infrastructure as a precondition for equitable AI, not an afterthought.</p>

  <div class="resource-placeholder">
    <h4>&#128214; Sources &amp; Further Reading</h4>
    <ul class="styled-list">
      <li><a href="https://arxiv.org/abs/2501.09136" target="_blank" rel="noopener">Singh, A., Ehtesham, A., Kumar, S., Talaei Khoei, T., &amp; Vasilakos, A. V. (2025). <em>Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG.</em> arXiv:2501.09136</a> &mdash; the canonical agentic-RAG reference.</li>
      <li><a href="https://arxiv.org/abs/2407.16833" target="_blank" rel="noopener">Li, Z., Li, C., Zhang, M., Mei, Q., &amp; Bendersky, M. (2024). <em>Retrieval Augmented Generation or Long-Context LLMs? A Comprehensive Study and Hybrid Approach.</em> arXiv:2407.16833</a> (Google; EMNLP 2024) &mdash; the long-context-vs-RAG trade-off and the Self-Route hybrid. (2024 evidence &mdash; read for shape, not current margins.)</li>
      <li><a href="https://arxiv.org/abs/2309.15217" target="_blank" rel="noopener">Es, S., James, J., Espinosa-Anke, L., &amp; Schockaert, S. (2023). <em>RAGAS: Automated Evaluation of Retrieval Augmented Generation.</em> arXiv:2309.15217</a> &mdash; the RAG evaluation framework; metric definitions at <a href="https://docs.ragas.io/" target="_blank" rel="noopener">docs.ragas.io</a>.</li>
      <li><a href="https://arxiv.org/abs/2502.15916" target="_blank" rel="noopener">Esethu Framework (Rajab et al., 2025). arXiv:2502.15916</a> &mdash; locally-grounded infrastructure for equitable AI (introduced in Week 4; expanded in Week 11).</li>
    </ul>
  </div>

  <div class="intro-text" style="margin-top: 50px;">
    <h2>&#128073; What Comes Next</h2>
    <p><strong>Sub-Lesson 10.5 &mdash; Advanced Research Tools: A Curated Tour.</strong> We have now built up the concepts (10.1&ndash;10.2) and the categories (10.3&ndash;10.4). The next sub-lesson is the practical pay-off: a tool-by-tool tour with an honest free-versus-paid split, including the Deep Research modes that implement the agentic RAG from this lesson, the Chinese free-tier options, and the MCP connectors that plug agents into your research tools &mdash; all framed by the question that runs through this week: what can you actually use, from here, for free?</p>
  </div>
"""


# ---------------------------------------------------------------------------
# Sub-Lesson 10.5 — Advanced Research Tools: A Curated Tour
# ---------------------------------------------------------------------------

SL5_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>This is the practical pay-off of the week: a tool-by-tool tour with honest verdicts. For each category we ask three questions &mdash; what does it actually do well, what is its specific failure mode, and <strong>what does the free tier deliver for a student who cannot put a foreign credit card into a sign-up form?</strong> That last question is not a footnote in this course; for many UCT students it decides whether a tool exists at all.</p>
    <p>The centrepiece is a comparison of <strong>Deep Research modes</strong> &mdash; the agentic-RAG tools from 10.4 &mdash; because the Week 10 activity (10.6) hinges on them. We then cover the Chinese free-tier options (often <em>more</em> generous than the Western ones, with one serious catch), the MCP connectors worth wiring into a research workflow, what is expensive and skippable, and a free-tier research pipeline you can actually run.</p>
    <p>A hard warning before any number appears: <strong>every quota in this sub-lesson is a May 2026 snapshot and several will be wrong by the time you read this.</strong> Free tiers are the most volatile thing in the entire field &mdash; they change monthly, sometimes weekly. Treat the specific figures as &ldquo;go and check&rdquo;, not gospel. The framework for choosing is the durable part.</p>
  </div>

  <h2 class="section-title">&#127757; Why &ldquo;Free&rdquo; Is the Whole Game Here</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">A course written in California would treat the free-versus-paid question as a budgeting detail. From Cape Town it is structural. The UNDP&#39;s 2025 analysis of African AI talent (drawing on Zindi&#39;s network of some 11,000 data scientists) found that <strong>only about 5% have access to the computing power their work needs</strong> &mdash; roughly 1% with on-premise GPUs and 4% paying for cloud access. The continent holds an estimated <strong>0.1% of the world&#39;s computing capacity</strong>, while 60% of the top supercomputers sit in just three countries. The lived effect is stark: a well-resourced researcher in a G7 country can retrain a model every thirty minutes, while an African peer may wait up to six days between iterations.</p>

  <div class="highlight-box">
    <h3>The compute gap is why this week is free-tier-first</h3>
    <p>When 95% of a continent&#39;s AI researchers depend on free or shared tools, &ldquo;just pay for the Pro plan&rdquo; is not advice &mdash; it is an assumption that excludes most of the people this course is for. So everything below is filtered through what is genuinely reachable on a free tier from a South African connection. This is the same equity argument the Esethu Framework (Week 4, expanded in Week 11) makes about infrastructure: access is not a detail, it is the precondition.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The practical access picture as of May 2026: Claude.ai, ChatGPT, Gemini, Perplexity, and Microsoft Copilot all work from South African networks without a VPN, and UCT&#39;s Microsoft 365 subscription means Copilot Chat is very likely already available to you through your university account. The Chinese services below also work from a Cape Town connection without a VPN. One thing unites all of them, Western and Chinese alike: they process your data on servers outside South Africa &mdash; a data-protection point we treat seriously below.</p>

  <h2 class="section-title">&#128270; Deep Research Modes: The Comparison That Matters</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Deep Research modes take a question, spend several minutes planning, searching, and reading, and return a cited report &mdash; the consumer face of the agentic RAG from 10.4. They are also what the 10.6 activity asks you to test. Here is the free-tier landscape, with the staleness warning in force.</p>

  <div class="warning-box">
    <h4>&#9888;&#65039; Quotas below are a May 2026 snapshot &mdash; verify before relying</h4>
    <p>These numbers move constantly. While this was being written, sources already disagreed about Perplexity&#39;s free Deep Research allowance (some said five a day, one said none) &mdash; which tells you exactly how much weight to put on any single figure. Check the current limit yourself before building the activity around a tool.</p>
  </div>

  <div style="overflow-x: auto;">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Tool</th>
          <th>Free-tier Deep Research (May 2026)</th>
          <th>Notes</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Perplexity</strong></td>
          <td>~5 / day</td>
          <td>The most generous Western free tier; the recommended default for the activity. Comet browser also free.</td>
        </tr>
        <tr>
          <td><strong>Kimi</strong> (kimi.com)</td>
          <td>Usable, quota not published</td>
          <td>Moonshot AI. The strongest free <em>alternative</em> to Perplexity &mdash; cited, visualised reports.</td>
        </tr>
        <tr>
          <td><strong>ChatGPT</strong></td>
          <td>~5 / month, then a lightweight fallback</td>
          <td>Hard monthly cap on the full version; the fallback is shallower.</td>
        </tr>
        <tr>
          <td><strong>Gemini</strong></td>
          <td>~5 reports / month</td>
          <td>On the Gemini Apps free tier; 1M-token context on the Pro models.</td>
        </tr>
        <tr>
          <td><strong>DeepSeek</strong> (chat.deepseek.com)</td>
          <td>No one-button mode; approximate it manually</td>
          <td>DeepThink reasoning + web search + file upload, chained by hand, gets close. Fully free, English UI.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 18px; margin-bottom: 15px;">For the 10.6 activity, the recommended free Deep Research tool is <strong>Perplexity</strong>; if its quota is exhausted or sign-up is blocked, <strong>Kimi</strong> is the strongest substitute &mdash; provided you read the data-protection note next, and disclose your choice as the activity requires.</p>

  <h2 class="section-title">&#127760; Chinese Free Tiers: Often More Generous</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The Western free-tier list is West-Coast-heavy, and for a student who cannot pay, that matters &mdash; the major Chinese services are often <em>more</em> generous, accept email or Google sign-up, and (as of May 2026) work from a Cape Town connection without a VPN. They belong in any honest free-tier map. The honest ranking for the UCT student who cannot pay:</p>

  <div class="card-grid">
    <div class="card">
      <h3>1. DeepSeek &mdash; chat.deepseek.com</h3>
      <p>The most capable fully-free reasoning chat in May 2026: V4 plus a DeepThink toggle, web search, and file upload, with no message cap and no Chinese phone number required. English UI, email or Google sign-up. Throttles to &ldquo;Server Busy&rdquo; at peak times.</p>
    </div>
    <div class="card">
      <h3>2. Kimi &mdash; kimi.com</h3>
      <p>Moonshot AI. The closest free analogue to Perplexity Deep Research, plus document and slide generation and a very long (256K+) context window. Google sign-in, English UI. Free Deep Research quota is not published &mdash; expect it to tighten.</p>
    </div>
    <div class="card">
      <h3>3. Qwen &mdash; chat.qwen.ai</h3>
      <p>Alibaba. The widest <em>modality</em> coverage on a free tier: hybrid thinking, web search, image/video understanding, image generation. Note: Qwen&#39;s free coding-agent CLI was discontinued on 15 April 2026 &mdash; the chat surface stays free, the coding CLI now needs payment.</p>
    </div>
    <div class="card">
      <h3>4. Z.ai / Zhipu &mdash; chat.z.ai</h3>
      <p>Zhipu AI. The most open-weights-aligned option: free chat on GLM-4.5/4.6 (MIT-licensed and self-hostable) with an agent mode and document generation. Free agent runs are slower and shorter than DeepSeek&#39;s or Kimi&#39;s.</p>
    </div>
  </div>

  <div class="warning-box">
    <h4>&#9888;&#65039; Sending data abroad: a rule for <em>all</em> these tools, not just the Chinese ones</h4>
    <p>It is tempting to attach the data-protection worry only to the Chinese services, but that would be both unfair and wrong. <strong>Almost every free AI tool in this sub-lesson processes your data outside South Africa</strong> &mdash; the US-based services (ChatGPT, Claude, Gemini, Perplexity) on infrastructure outside South Africa, typically in the United States; the Chinese services (DeepSeek, Kimi, Qwen, Z.ai) on servers in mainland China. Under South Africa&#39;s Protection of Personal Information Act (POPIA, section 72), the relevant question is not <em>which</em> country, but whether sending personal information there is permitted at all: a transfer abroad is restricted unless the recipient is bound by data-protection rules substantially similar to POPIA&#39;s, or the data subject has consented (among a few narrow conditions). POPIA has no &ldquo;approved-country&rdquo; whitelist &mdash; the test is the recipient&#39;s actual protection, which for any consumer AI service hosting your prompts abroad you have no basis to assume is met, wherever its servers sit.</p>
    <p>In plain terms, applied equally to the US-hosted and the China-hosted tools: <strong>do not put identifiable personal data, participant information, unpublished results, or third-party confidential material into any of them.</strong> For public, non-personal research questions they are all excellent and free. For anything involving real people&#39;s data, the obligation is the same regardless of vendor &mdash; and you must record which tool you used and where its data went. The 10.6 activity makes this disclosure a required, graded section, for every tool, not an afterthought.</p>
  </div>

  <h2 class="section-title">&#128268; MCP Connectors Worth Wiring In</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">From 10.3: MCP lets an agent reach your tools through one standard. A handful of connectors are genuinely useful for research &mdash; reference managers (community-maintained <strong>Zotero</strong> MCP servers exist; search for the current one), <strong>GitHub</strong>, <strong>Google Drive</strong>, and <strong>Notion</strong>. On Claude.ai a set of connectors is available even on the free plan (free users get one custom connector). Used well, an agent can search your own library or read your repository through a single interface.</p>

  <div class="warning-box">
    <h4>&#9888;&#65039; Every connector is two risks at once</h4>
    <p>Each connector you add does two things beyond its convenience. First, it <strong>widens the prompt-injection surface</strong> (10.2): an agent that can read your Drive and browse the web can be steered by hostile text in a document or page. Second, it <strong>opens a POPIA-relevant data flow</strong>: connecting your inbox or institutional Drive sends that content to the model provider. Connect deliberately, one at a time, with the lowest permissions that do the job &mdash; and never connect a personal-data source to a tool whose servers you would not trust with that data.</p>
  </div>

  <h2 class="section-title">&#128176; What&#39;s Expensive &mdash; and Probably Skippable</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">For a postgraduate on a stipend, most of the heavily-marketed paid agents are not worth it:</p>

  <ul class="styled-list">
    <li><strong>Enterprise agents</strong> (Sierra, Decagon, Cognition&#39;s Devin) &mdash; priced for companies; not aimed at, or affordable for, an individual researcher.</li>
    <li><strong>Manus</strong> &mdash; the &ldquo;general agent&rdquo; from 10.3. Access is mixed and its capability claims are company-reported; not something to build a workflow on now.</li>
    <li><strong>Cursor Pro</strong> &mdash; genuinely good if you code every day; if you do not, the free coding tools cover it.</li>
    <li><strong>Paid Deep Research tiers</strong> &mdash; faster and higher-quota, but the free tiers are enough to do real work and to complete this course. The activity is deliberately built to be done entirely free.</li>
  </ul>

  <div class="info-box">
    <h4>&#127757; A Week 3 reminder: agents are expensive in tokens, not just money</h4>
    <p>An agentic run &mdash; planning, many tool calls, reading long results, retrying &mdash; burns far more tokens than a single chat message, sometimes by orders of magnitude. That is why free Deep Research is rationed, and it is also a Week 3 environmental point: a Deep Research report has a much larger compute (and therefore energy and water) footprint than a one-shot answer. Use the heavy tools when the task warrants them, not reflexively.</p>
  </div>

  <h2 class="section-title">&#129534; A Free-Tier Research Pipeline</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Putting the week together, here is a five-step pipeline a UCT student can run entirely on free tools &mdash; and which deliberately keeps you in the loop at every verification point:</p>

  <ul class="step-list">
    <li><strong>Explore</strong> &mdash; run your question through a free Deep Research mode (Perplexity, or Kimi for non-personal topics) to map the landscape and surface sources. (Week 10.4)</li>
    <li><strong>Verify</strong> &mdash; do not trust the report. Run every citation through the Week 5 Five-Point Citation Check and the Week 9 &ldquo;which model, which date, retested?&rdquo; check. Expect some sources to be wrong or invented.</li>
    <li><strong>Synthesise</strong> &mdash; organise what survived verification into your own structure, in your own words. The work of deciding what matters and how it fits together is yours; a chat tool can react to your structure, not replace it. (Week 6)</li>
    <li><strong>Write</strong> &mdash; write your own first draft. Then use AI to refine it &mdash; tightening, questioning, suggesting &mdash; checking each change as you go. This is the Week 6 order, and it matters: the thinking and the first words should be yours, with AI sharpening what you wrote, not generating it for you. Drafting by prompt is how you end up with fluent text you do not actually understand or stand behind.</li>
    <li><strong>Audit</strong> &mdash; before anything leaves your hands, check it as you would AI-generated code: claims against sources, numbers against primaries, and a record of which tool did what. (Weeks 7 and 9)</li>
  </ul>

  <p style="color: #555; line-height: 1.75; margin-top: 15px;">Every step here has a free tool behind it, and every verification step is yours, not the agent&#39;s. That is the whole argument of the week in one workflow: agents change what the tools can do; they do not change who is responsible for the result.</p>

  <div class="resource-placeholder">
    <h4>&#128214; Sources &amp; Further Reading</h4>
    <ul class="styled-list">
      <li><a href="https://www.undp.org/digital/blog/only-five-percent-africas-ai-talent-has-compute-power-it-needs" target="_blank" rel="noopener">UNDP, &ldquo;Only five percent of Africa&#39;s AI talent has the compute power it needs&rdquo;</a> &mdash; the compute-equity figures.</li>
      <li><a href="https://inforegulator.org.za/" target="_blank" rel="noopener">South Africa Information Regulator (POPIA)</a> &middot; <a href="https://www.michalsons.com/blog/how-popia-affects-ai/76842" target="_blank" rel="noopener">Michalsons, &ldquo;How POPIA affects AI&rdquo;</a> &mdash; for the cross-border data-flow rules behind the Chinese-tools caveat.</li>
      <li>Deep Research free tiers (verify current): <a href="https://www.perplexity.ai/" target="_blank" rel="noopener">Perplexity</a> &middot; <a href="https://help.openai.com/en/articles/10500283-deep-research-faq" target="_blank" rel="noopener">OpenAI Deep Research FAQ</a> &middot; <a href="https://gemini.google/" target="_blank" rel="noopener">Gemini</a>.</li>
      <li>Chinese free tiers: <a href="https://chat.deepseek.com/" target="_blank" rel="noopener">DeepSeek</a> &middot; <a href="https://kimi.com/" target="_blank" rel="noopener">Kimi</a> &middot; <a href="https://chat.qwen.ai/" target="_blank" rel="noopener">Qwen</a> &middot; <a href="https://chat.z.ai/" target="_blank" rel="noopener">Z.ai</a>.</li>
      <li><a href="https://arxiv.org/abs/2502.15916" target="_blank" rel="noopener">Esethu Framework (Rajab et al., 2025). arXiv:2502.15916</a> &mdash; the equity-and-sovereignty argument, expanded in Week 11.</li>
    </ul>
  </div>

  <div class="intro-text" style="margin-top: 50px;">
    <h2>&#128073; What Comes Next</h2>
    <p><strong>Sub-Lesson 10.6 &mdash; Hands-On Activities and Assessment.</strong> Now you put it to work. The headline activity, &ldquo;Same Task, Three Ways&rdquo;, has you run a research question from your own field through plain chat, chat-with-tools, and a Deep Research mode, then judge the results with the Week 9 failure taxonomy and verify them with the Week 5 citation checks &mdash; using free tools only, and disclosing where your data went. It is the whole week, made concrete on a question you actually care about.</p>
  </div>
"""


# ---------------------------------------------------------------------------
# Sub-Lesson 10.6 — Hands-On Activities and Assessment
# ---------------------------------------------------------------------------

SL6_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>This is where the week becomes concrete. You have a working definition of agents (10.1), a taxonomy of how they fail (10.2), a map of the tools (10.3), an understanding of agentic RAG (10.4), and an honest free-tier guide (10.5). Now you apply all of it to a research question you actually care about.</p>
    <p>The headline activity is <strong>&ldquo;Same Task, Three Ways&rdquo;</strong>: run one question through plain chat, chat-with-tools, and a Deep Research mode, then judge the results with the Week 9 failure taxonomy and verify them with the Week 5 citation checks. Two shorter activities follow, and the week&#39;s assessment pulls them together. Everything here is designed to be done <strong>entirely on free tools</strong> &mdash; on a phone or a borrowed laptop if that is what you have &mdash; because, as 10.5 argued, a course for this continent cannot assume a subscription.</p>
    <p>One last echo of Week 9: every output you produce this week is a snapshot dated May 2026. Part of the assessment is acknowledging that &mdash; recording what was true when you did the work, and how soon you would expect it to change.</p>
  </div>

  <h2 class="section-title">&#129514; Activity 1: Same Task, Three Ways</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The core activity. Choose a research question <strong>in your own field</strong> &mdash; specific, genuinely answerable, and not trivially Googleable. Something a knowledgeable colleague would have to think about. You will be the expert judge of the answers, which is the point: you can tell when an AI is wrong in your own area in a way you cannot in someone else&#39;s.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Run that one question through three modes, keeping everything else the same:</p>

  <ul class="step-list">
    <li><strong>Plain chat</strong> &mdash; a free assistant with no tools (Claude.ai, ChatGPT, or Gemini free; pick one and stay with it). The model answers from training alone.</li>
    <li><strong>Chat with tools</strong> &mdash; the same kind of assistant, but with web search / browsing switched on, so it can retrieve before answering.</li>
    <li><strong>Deep Research mode</strong> &mdash; a full agentic-RAG run. Perplexity&#39;s free Deep Research is the recommended default. <em>If its quota is exhausted or sign-up is blocked, Kimi (kimi.com) is an acceptable substitute</em> &mdash; but see the data-disclosure rule below, which applies whichever tool you choose.</li>
  </ul>

  <p style="color: #555; line-height: 1.75; margin-top: 15px; margin-bottom: 15px;">Then write a <strong>one-to-two-page comparison</strong>. Do not just say which was &ldquo;best&rdquo;. For each mode, record: how deep and specific the answer was; how good the citations were (and whether they exist &mdash; you will check in Activity 2); what it got wrong in your expert judgement; and where each mode failed. Then do the analytical core of the exercise:</p>

  <div class="info-box">
    <h4>&#128202; Apply the Week 9.2 taxonomy explicitly</h4>
    <p>For every failure you observed, classify it: was it <strong>patched</strong> (you were using a weak tool &mdash; a current one would not fail this way), <strong>reduced-but-persistent</strong> (a known weakness you can manage with better prompting or tool choice), or <strong>structural</strong> (something the next model release will not fix &mdash; long-tail gaps, compositional error, the reliability-not-accuracy problem from 10.2)? Then, for the structural ones, state what the Week 9.5 verification protocol would have you do about it. This is the muscle the whole activity exists to build.</p>
  </div>

  <h2 class="section-title">&#128269; Activity 2: Verify a Deep Research Output</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">This follows directly from Activity 1. Take the Deep Research report you generated and put its citations on trial, using the tools you already have:</p>

  <ul class="styled-list">
    <li>Run every citation through the <strong>Week 5 Five-Point Citation Check</strong> (does the paper exist; are the authors and year right; does it say what the report claims; is the venue real; does the link resolve to the right thing).</li>
    <li>Apply the <strong>Week 9 dated-research check</strong>: which model produced this, when, and would the claim survive a retest on a current model?</li>
  </ul>

  <p style="color: #555; line-height: 1.75; margin-top: 15px; margin-bottom: 15px;">Then report the numbers: of the citations the Deep Research tool gave you, how many checked out completely? How many pointed to real sources that said something <em>different</em> from the report&#39;s claim? How many were to &ldquo;papers&rdquo; that do not appear to exist at all? This is the Week 5 hallucinated-citation exercise carried into the agentic-RAG era &mdash; and the results are usually sobering, which is exactly the lesson. A fluent, well-formatted, confident research report is not a verified one.</p>

  <h2 class="section-title">&#128268; Activity 3 (Optional): A Small MCP Workflow</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">For students who want to go further. Using one of Claude.ai&#39;s free connectors &mdash; the creative connectors, or (since April 2026) the read-only Microsoft 365 connector &mdash; wire up <em>one</em> small step of your research workflow, involving nothing personal or confidential. Write 250 words on what worked, what failed, and &mdash; most importantly &mdash; <strong>what you would never let it do unsupervised</strong>, and why. The point is not the connector; it is articulating your own permissions dial (10.1) for a real task.</p>

  <div class="info-box">
    <h4>&#128274; A note on the Microsoft 365 connector</h4>
    <p>It needs a <em>business or education</em> Microsoft account (not a personal @outlook.com one), and your institution&#39;s IT must allow the connection. There is a simple way to find out whether yours does: just try adding it. If Microsoft shows an &ldquo;administrator approval required&rdquo; screen, self-service connection is not enabled for your institution and you would need IT to approve it. Reading that consent screen &mdash; and deciding whether you would even want to grant the access it asks for &mdash; is itself a useful exercise in the permissions thinking this week is about.</p>
  </div>

  <h2 class="section-title">&#127760; The Data-Disclosure Rule (Required, Graded)</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Every tool in this activity processes your data outside South Africa &mdash; the US-based assistants and the Chinese ones alike (10.5). So a disclosure statement is part of the deliverable, not an optional extra. Two firm rules and a template:</p>

  <ul class="styled-list">
    <li><strong>No personal or confidential data.</strong> Use a research question that involves no identifiable personal information, no participant data, no unpublished third-party material. POPIA (section 72) restricts sending personal information abroad regardless of the destination country, and a free consumer AI tool gives you no basis to assume the recipient meets the bar. Keep the activity to public, non-personal questions.</li>
    <li><strong>Disclose what you used and where it went.</strong> Naming your tools and their data destinations is a habit worth building now &mdash; it is exactly what a research-ethics committee or a journal will increasingly expect.</li>
  </ul>

  <div class="technical-detail">
    <h4>&#128196; Disclosure statement template (copy, complete, submit)</h4>
    <p style="color: #444; line-height: 1.8;">
      <em>&ldquo;For this exercise I used: [tool 1], [tool 2], [tool 3].<br>
      Each processes data outside South Africa, in: [country/region per tool, e.g. United States / China / unknown].<br>
      The research question involved no identifiable personal information or third-party confidential material.<br>
      I verified the outputs as follows: [Five-Point Citation Check / dated-research check / other].<br>
      Outputs are accurate as of [date]; I would expect the tool capabilities and free-tier limits described to change within [estimate].&rdquo;</em>
    </p>
  </div>

  <h2 class="section-title">&#128221; The Week 10 Assessment</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The assessment is a single piece of roughly <strong>1,500 words</strong>, in the same spirit as the Week 9 assessment: an explicitly dated snapshot that acknowledges its own coming obsolescence. <strong>Free tools only</strong> &mdash; a hard rule, so that everyone is judged on the same playing field regardless of what they can afford. Required sections:</p>

  <div style="overflow-x: auto;">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Section</th>
          <th>What it contains</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Tool comparison</td>
          <td>The Activity 1 three-way comparison, with concrete observations per mode.</td>
        </tr>
        <tr>
          <td>Applied failure taxonomy</td>
          <td>Each observed failure classified patched / reduced / structural, with the Week 9.5 action for the structural ones.</td>
        </tr>
        <tr>
          <td>Verification audit</td>
          <td>The Activity 2 citation check, with the numbers: how many citations held up, how many didn&#39;t.</td>
        </tr>
        <tr>
          <td>Data-flow disclosure</td>
          <td>The completed disclosure statement and a sentence on the POPIA reasoning behind it.</td>
        </tr>
        <tr>
          <td>Staleness reflection</td>
          <td>What is dated about your findings, and your recommended retest cadence.</td>
        </tr>
        <tr>
          <td>&ldquo;If I had a paid subscription&rdquo;</td>
          <td>One honest paragraph on what you could not do for free, and whether it would have changed your conclusions.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2 class="section-title">&#128506;&#65039; Week 10 in One Page</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Pulling the week together:</p>

  <ul class="styled-list">
    <li><strong>An agent is a model plus a harness</strong> &mdash; tools, a loop, memory, and permissions &mdash; and since 2024 the harness, not the model, increasingly decides how well the whole thing works (10.1).</li>
    <li><strong>Reliability is not accuracy.</strong> Agents fail in new ways over long horizons; the failures that matter are structural, and the verification burden grows rather than shrinks (10.2).</li>
    <li><strong>The tool landscape is real but volatile</strong> &mdash; coding, computer-use, browser, and research agents, connected increasingly through MCP &mdash; and best read with three questions: which harness, how reliable, free from here? (10.3)</li>
    <li><strong>RAG has split</strong> into long-context, agentic RAG, and Deep Research; the right choice is task-dependent, and the researcher still decides what to trust (10.4).</li>
    <li><strong>A great deal is genuinely free</strong> from South Africa &mdash; Western and Chinese alike &mdash; if you know where to look and you treat cross-border data flow seriously for every tool (10.5).</li>
  </ul>

  <div class="highlight-box">
    <h3>The one idea to keep</h3>
    <p>Agents change what the tools can do. They do not change who is responsible for the result. Every capability in this week shifts work onto the machine and verification onto you &mdash; and the researcher who understands that trade, and keeps the verification, is the one who benefits from agents instead of being misled by them.</p>
  </div>
"""


# ---------------------------------------------------------------------------
# Sub-lesson registry  (ToC added once all sub-lessons approved)
# ---------------------------------------------------------------------------

SUBLESSONS = [
    {
        "filename": "What Agents Are and Whats New in 2026.html",
        "title": "Week 10.1 - Agents: What They Are and What's Actually New in 2026",
        "badge": "Week 10 &bull; Sub-Lesson 1",
        "header_emoji": "&#129302;",  # robot face
        "header_title": "Agents: What They Are and What&#39;s New in 2026",
        "header_subtitle": "A working definition of agents for researchers &mdash; and the central shift since 2024: the harness, not the model, has become the product",
        "body": SL1_BODY,
    },
    {
        "filename": "Failure Modes for Long-Horizon Tasks.html",
        "title": "Week 10.2 - Agents: Failure Modes for Multi-Step / Long-Horizon Tasks",
        "badge": "Week 10 &bull; Sub-Lesson 2",
        "header_emoji": "&#129512;",  # dynamite / structural-failure motif (matches Week 9.2)
        "header_title": "Failure Modes for Long-Horizon Tasks",
        "header_subtitle": "Applying the Week 9 patched / reduced / structural taxonomy to agents &mdash; and the central finding that reliability is not accuracy",
        "body": SL2_BODY,
    },
    {
        "filename": "The Current Tool Landscape and MCP.html",
        "title": "Week 10.3 - Agents: The Current Tool Landscape (Including MCP)",
        "badge": "Week 10 &bull; Sub-Lesson 3",
        "header_emoji": "&#129520;",  # toolbox
        "header_title": "The Current Tool Landscape (Including MCP)",
        "header_subtitle": "A time-stamped, free-tier-honest tour of coding agents, computer-use and browser agents, and the MCP connector layer &mdash; as of May 2026",
        "body": SL3_BODY,
    },
    {
        "filename": "RAG in 2026.html",
        "title": "Week 10.4 - RAG in 2026",
        "badge": "Week 10 &bull; Sub-Lesson 4",
        "header_emoji": "&#128218;",  # books
        "header_title": "RAG in 2026",
        "header_subtitle": "What changed since Week 5: long context vs retrieval, agentic RAG and Deep Research, evaluating it all &mdash; and why the researcher stays in the loop",
        "body": SL4_BODY,
    },
    {
        "filename": "Advanced Research Tools - A Curated Tour.html",
        "title": "Week 10.5 - Advanced Research Tools: A Curated Tour",
        "badge": "Week 10 &bull; Sub-Lesson 5",
        "header_emoji": "&#129520;",  # toolbox
        "header_title": "Advanced Research Tools: A Curated Tour",
        "header_subtitle": "An honest free-versus-paid map of Deep Research modes, Chinese free tiers, MCP connectors and a free research pipeline &mdash; built for a student without a foreign credit card",
        "body": SL5_BODY,
    },
    {
        "filename": "Hands-On Activities and Assessment.html",
        "title": "Week 10.6 - Hands-On Activities and Assessment",
        "badge": "Week 10 &bull; Sub-Lesson 6",
        "header_emoji": "&#127919;",  # bullseye (matches Week 9.6)
        "header_title": "Hands-On Activities and Assessment",
        "header_subtitle": "Same Task, Three Ways: test plain chat, chat-with-tools, and Deep Research on your own research question &mdash; then judge and verify the results, on free tools only",
        "body": SL6_BODY,
    },
]


TOC_HTML = """<html><head><meta http-equiv="'Content-Type'" content="'text/html;charset=utf-8'" /><title>MAM5020F 2026 | Gen AI for Research - Week 10: Agentic AI, RAG &amp; Advanced Research Tools</title></head><body>
<div style="background: #003A70; padding: 8px 20px; text-align: center;"><a href="../index.html" style="color: white; text-decoration: none; font-size: 0.85em;">&#8592; Back to Contents</a></div><table cellpadding=0 cellspacing=0 border=0 width=100%><tr><td colspan=3>&nbsp;</td></tr><tr><td valign="top" width="100%"><font class="title"><strong>MAM5020F 2026 | Gen AI for Research - Week 10: Agentic AI, RAG &amp; Advanced Research Tools</strong></font><br><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="What Agents Are and Whats New in 2026.html" />1. Agents: What They Are and What&#39;s New in 2026</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Failure Modes for Long-Horizon Tasks.html" />2. Failure Modes for Multi-Step / Long-Horizon Tasks</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="The Current Tool Landscape and MCP.html" />3. The Current Tool Landscape (Including MCP)</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="RAG in 2026.html" />4. RAG in 2026</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Advanced Research Tools - A Curated Tour.html" />5. Advanced Research Tools: A Curated Tour</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Hands-On Activities and Assessment.html" />6. Hands-On: Activities &amp; Assessment</a></p></td></tr></table><footer style="background: #f9f9f9; margin-top: 40px; padding: 22px 30px; text-align: center; color: #888; font-size: 0.85em; border-top: 1px solid #eee; font-family: 'Lato', 'Lucida Sans Unicode', 'Lucida Grande', sans-serif;">
&copy; 2026 Jonathan Shock, University of Cape Town &middot; MAM5020F: Generative AI for Research &middot; Licensed under <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener" style="color: #003A70; text-decoration: underline;">CC&nbsp;BY&nbsp;4.0</a>
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
    print("Generating Week 10...")
    print("Table of Contents:")
    write_to(SRC_DIR, "Table of Contents.html", TOC_HTML)
    write_to(DOCS_DIR, "Table of Contents.html", TOC_HTML)
    for sl in SUBLESSONS:
        print(f"{sl['title']}:")
        rendered = render_sublesson(sl)
        write_to(SRC_DIR, sl["filename"], rendered)
        write_to(DOCS_DIR, sl["filename"], rendered)
    print(f"\nDone. {len(SUBLESSONS)} file(s) written to each of:")
    print(f"  {SRC_DIR}")
    print(f"  {DOCS_DIR}")


if __name__ == "__main__":
    main()
