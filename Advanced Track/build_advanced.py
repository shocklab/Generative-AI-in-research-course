#!/usr/bin/env python3
"""
Generate the Advanced Track lesson HTML files
(Beyond the Free Tier: Agentic Research with Claude Code).

Outputs to both:
  Course materials/Advanced Track/            (source / Amathuba upload copies)
  Course materials/docs/advanced/             (GitHub Pages serving copies)

Mirrors the Week 9-12 generators exactly (same CSS, same PAGE_SHELL, pretty-printed
CSS, <style> in <head> for Brightspace). Adds a dark terminal-style code block for
shell commands and CLAUDE.md snippets.

Lesson A (3 pages) is built first for review. Lesson B is added after sign-off.

Re-run after any content change.
"""

import os
import re

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SRC_DIR = os.path.join(ROOT, "Advanced Track")
DOCS_DIR = os.path.join(ROOT, "docs", "advanced")


def pretty_print_css(css: str) -> str:
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
.instructor-box { background: #f3effa; border-left: 5px solid #6a5da8; border-radius: 12px; padding: 22px 26px; margin: 25px 0; }
.instructor-box h4 { color: #4f4391; font-size: 1.15em; margin-bottom: 12px; display: flex; align-items: center; gap: 10px; }
.instructor-box p { color: #463f5e; line-height: 1.75; margin-bottom: 12px; font-style: italic; }
.instructor-box p:last-child { margin-bottom: 0; }
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
pre.code-block { background: #11243d; color: #e6edf3; border-radius: 10px; padding: 18px 22px; margin: 20px 0; overflow-x: auto; font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; font-size: 0.85em; line-height: 1.65; white-space: pre; }
pre.code-block .cm { color: #8aa0b6; }
pre.code-block .pr { color: #7fd1b9; }
code { background: #eef2f6; color: #11407c; padding: 2px 6px; border-radius: 5px; font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; font-size: 0.86em; }
pre.code-block code { background: none; color: inherit; padding: 0; }
.gate-banner { background: #003A70; color: white; padding: 22px 28px; border-radius: 12px; margin-bottom: 30px; font-size: 1.0em; line-height: 1.7; }
.gate-banner strong { color: #ffffff; }
@media (max-width: 768px) { header h1 { font-size: 1.8em; } .content { padding: 30px 20px; } .card-grid { grid-template-columns: 1fr; } .comparison-table { font-size: 0.85em; } pre.code-block { font-size: 0.78em; } }
/* Force white text on dark-blue backgrounds (overrides Brightspace stylesheet defaults). */
header, header h1, header h2, header h3, header h4, header p, header span, header strong, header em, .week-badge,
.highlight-box, .highlight-box h1, .highlight-box h2, .highlight-box h3, .highlight-box h4, .highlight-box h5,
.highlight-box p, .highlight-box ul, .highlight-box ol, .highlight-box li,
.highlight-box strong, .highlight-box em, .highlight-box span,
.gate-banner, .gate-banner p, .gate-banner strong, .gate-banner em {
    color: #ffffff !important;
}
.highlight-box a, header a, .gate-banner a { color: #ffffff !important; text-decoration: underline; }"""

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


GATE_BANNER = """
  <div class="gate-banner">
    <strong>&#9888;&#65039; This is the Advanced Track &mdash; it goes beyond the free tier.</strong> Everything in Weeks 1&ndash;12 was chosen so that you could do it on free tools, because access is not a detail (Week&nbsp;10) and most of the world&#39;s researchers do not have a paid AI budget (Week&nbsp;11.4). This track is the one deliberate exception. It uses <strong>Claude Code</strong>, which needs a paid Claude subscription and comfort with a terminal. It is genuinely optional, it sits <em>after</em> the Week&nbsp;12 capstone on purpose, and the next page makes the honest case for whether it is worth it to you &mdash; including what you can and cannot approximate without paying.
  </div>
"""


# ===========================================================================
# Lesson A.1 — What Claude Code Actually Is
# ===========================================================================

SL_A1_BODY = GATE_BANNER + """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>For most of this course, &ldquo;using AI&rdquo; has meant a chat window: you type, the model answers, you copy what is useful back into your own work. Claude Code is a different kind of thing, and the difference is the whole point of this track. It is an <em>agent</em> that works inside your real project folder &mdash; it reads your files, runs your code, edits your documents, uses version control, and can work on its own for long stretches.</p>
    <p>This first lesson does three things: it says precisely what Claude Code is (and is not), using the model-versus-harness distinction from Week&nbsp;10; it draws the sharp line between chatting and working with an agent, around a single principle &mdash; <strong>the chat is not the archive</strong>; and it sets up the question the rest of Lesson A answers: what does it actually take to drive one of these well?</p>
    <p>Lesson&nbsp;B then turns to the payoff this track exists for: using Claude Code to make your research genuinely <em>reproducible</em> &mdash; inspectable and repeatable by someone who is not you.</p>
  </div>

  <h2 class="section-title">&#129518; The Model Is the Smallest Part</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Week&nbsp;10.1 made an argument that is easy to nod along to and hard to feel until you see it: <strong>the harness is the product</strong>. The language model &mdash; Claude itself &mdash; is one component. What turns it into something useful is everything wrapped around it: the tools it can call, the files it can see, the commands it can run, the permissions it operates under, and the loop that lets it act, observe the result, and act again. In a chat window that harness is thin and invisible. In Claude Code it is thick, and it is the part you are actually driving.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Put concretely: when you ask Claude in a browser tab to help with an analysis, the model is essentially all you get. It can reason about what you paste in and write text back. When you ask Claude Code the same thing, the model is the <em>smallest</em> part of what goes to work. The harness gives it your actual data files, a shell to run a script, the ability to read the error message that script produced, version control to record what changed, and standing instructions about how your project works. The intelligence is similar; the leverage is not.</p>

  <div class="info-box">
    <h4>&#128161; The one-sentence version</h4>
    <p>You are not talking to a smarter chatbot. You are driving a different kind of machine &mdash; a model with hands, working in your project folder. Almost everything that follows in this track is about driving it well, and about the discipline that makes its work trustworthy afterwards.</p>
  </div>

  <h2 class="section-title">&#128295; What Claude Code Can Actually Do</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Claude Code runs in your terminal and operates on a folder you point it at. Within that folder &mdash; and only within it, unless you say otherwise &mdash; it has a set of capabilities that are worth naming explicitly, because each one is a piece of the harness you will learn to use deliberately.</p>

  <div class="card-grid">
    <div class="card">
      <h3>Reads and writes your files</h3>
      <p>It can open, read, and edit the actual documents, data files, and scripts in your project &mdash; not a copy you pasted, the real thing. This is powerful and is exactly why permission and raw-data rules matter (Lesson&nbsp;B).</p>
    </div>
    <div class="card">
      <h3>Runs commands and code</h3>
      <p>It can execute shell commands and run your analysis scripts, then read the output or the error and respond to it. The act&ndash;observe&ndash;act loop is what makes it an agent rather than a text generator.</p>
    </div>
    <div class="card">
      <h3>Uses version control</h3>
      <p>It can initialise Git, commit changes, show you diffs, and read the history. Used well, this turns into a reproducibility trace (Lesson&nbsp;B.5), not just a software habit.</p>
    </div>
    <div class="card">
      <h3>Reads standing instructions</h3>
      <p>A <code>CLAUDE.md</code> file in the project is loaded at the start of every session. It is how you tell the agent the rules of <em>your</em> project once, instead of re-explaining every time. We meet it properly in A.3.</p>
    </div>
    <div class="card">
      <h3>Runs reusable Skills</h3>
      <p>A Skill is a packaged, reusable workflow (a folder with a <code>SKILL.md</code>) the agent can invoke when it is relevant &mdash; a tested research procedure that travels across projects rather than being re-improvised each time (Lesson&nbsp;B.4).</p>
    </div>
    <div class="card">
      <h3>Spawns subagents</h3>
      <p>For a bounded job it can launch a separate, focused agent &mdash; for example, an independent check of an analysis it just produced. This connects directly to the adversarial-verification idea from Week&nbsp;9.</p>
    </div>
    <div class="card">
      <h3>Connects to external tools (MCP)</h3>
      <p>Through the Model Context Protocol it can reach approved external services and data sources &mdash; a reference database, a paper repository &mdash; the same MCP idea introduced in Week&nbsp;10.</p>
    </div>
    <div class="card">
      <h3>Plans before it acts</h3>
      <p>It has a read-only <em>plan mode</em>: it inspects and proposes a plan without changing anything, so you can approve the approach before a single file moves. This is your most important safety control, and we use it in A.3.</p>
    </div>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">None of these capabilities is exotic on its own &mdash; researchers have used shells, version control, and scripts for decades. What is new is that one system can use all of them <em>in a loop, on your behalf, from a plain-language request</em>. That is the capability Week&nbsp;11.1 called &ldquo;AI as a substantive collaborator,&rdquo; made operational. And as Week&nbsp;11.1 also insisted: the more the system can do unsupervised, the more the verification habit matters, not less.</p>

  <h2 class="section-title">&#128202; Why This Is Categorically Different From Chat</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">It is tempting to file Claude Code under &ldquo;a more capable chatbot.&rdquo; That framing will mislead you. The difference is not capability; it is <em>where the work lives</em>.</p>

  <div class="card-grid">
    <div class="card" style="border-left-color: #888;">
      <h3>In a chat window</h3>
      <p>You paste context in. The model answers. The useful output, the reasoning, the decisions you made along the way &mdash; all of it lives in a conversation thread. Next week the thread is buried; next month you cannot reconstruct what you actually did, or why. The work is real but the <em>record</em> evaporates.</p>
    </div>
    <div class="card">
      <h3>In Claude Code</h3>
      <p>The work lives in your files. The script it wrote is in <code>scripts/</code>. The output is in <code>outputs/</code>. The decision it made is in a log you told it to keep. The change is in the Git history. Six months later, you &mdash; or a stranger &mdash; can open the folder and see what happened.</p>
    </div>
  </div>

  <div class="highlight-box">
    <h3>&#128193; The chat is not the archive</h3>
    <p>This is the organising principle of the whole track, so it is worth stating once, plainly: <strong>save your sources, notes, instructions, scripts, outputs, and decisions into files &mdash; not into a chat thread.</strong> The conversation is where the work is <em>commissioned</em>; the project folder is where the work <em>lives</em>. A chatbot session is a conversation you will lose. A project folder is the unit of reproducible research.</p>
    <p>Everything Lesson&nbsp;B builds &mdash; the folder discipline, the decision log, the reproducible analysis &mdash; is a consequence of taking this one sentence seriously.</p>
  </div>

  <div class="info-box">
    <h4>&#9878;&#65039; This is not &ldquo;abandon chat&rdquo;</h4>
    <p>Chat is still the right tool for a great deal: a quick question, a brainstorm, a one-off paragraph, thinking out loud. The honest distinction is about <em>durability</em>. Reach for chat when the value is in the answer you read right now. Reach for an agent in a project folder when the value is in work that has to survive, be repeated, or be defended later. Most researchers will use both, for different things, and knowing which is which is itself a skill.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 25px; margin-bottom: 15px;"><strong>Coming up in A.2:</strong> the honest case. Before you invest time learning to drive this, you deserve a straight account of what it costs, who it excludes, what you can approximate for free, and the genuine shift in how you work that it demands &mdash; the move from <em>chatting</em> to <em>managing an agent</em>.</p>
"""


# ===========================================================================
# Lesson A.2 — The Honest Case: Cost, Access, and the Disposition
# ===========================================================================

SL_A2_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>This is the one place in the entire course where we recommend a paid tool, so it gets the same calibrated treatment the course gives every other claim: an honest reckoning, not a sales pitch. This lesson covers what Claude Code costs, the equity problem that cost creates, what you can genuinely approximate on free tools, and &mdash; the part that changes how you work &mdash; the disposition shift from chatting to <em>managing an agent</em>.</p>
    <p>The aim is that by the end you can decide, for yourself and honestly, whether this track is worth it for your situation. For some readers it clearly will be; for others it clearly will not be, and saying so plainly is part of keeping faith with the rest of the course.</p>
  </div>

  <h2 class="section-title">&#128176; The Cost Picture, Honestly</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Claude Code is not free. As of mid-2026 it is available through Anthropic&#39;s paid subscription tiers and via metered API usage; the entry subscription sits at roughly the price of a couple of streaming services per month, and the heavier tiers cost substantially more. Because these numbers change, this lesson deliberately does not pin an exact figure &mdash; check the current Anthropic pricing page rather than trusting a number a course page wrote months ago. (That habit &mdash; trust the live source, not the cached claim &mdash; is the Week&nbsp;9 disposition applied to pricing.)</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">There are two cost shapes worth distinguishing. A flat <strong>subscription</strong> gives you a generous but bounded amount of use for a predictable monthly fee &mdash; the right model for most individual researchers. <strong>Metered API</strong> use is pay-as-you-go and can run up quickly when an agent works autonomously for an hour across a large codebase: that is real money per run, and worth watching. Either way, the honest framing from Week&nbsp;3 applies &mdash; the cost is not only the invoice. It is also tokens, time, attention, and the review effort every piece of agent output demands.</p>

  <h2 class="section-title">&#127757; The Equity Tension, Named</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">This course has been militantly free-tier-first, and that was a deliberate choice with an argument behind it. Week&nbsp;10 made the case that &ldquo;just pay for the Pro plan&rdquo; is not advice but an assumption that excludes most of the people the course is for. Week&nbsp;11.4 put numbers on the African compute gap. A paid-tool track sits in direct tension with all of that, and the worst thing we could do is pretend otherwise.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">So, plainly: for a researcher in a well-funded lab, the subscription cost is a rounding error and this track is a straightforward yes. For a postgraduate paying out of pocket, in a department without an AI budget, on a currency that makes dollar-denominated subscriptions painful, it is a genuine barrier &mdash; the same barrier this course spent eleven weeks taking seriously. This track is the signposted exception, not a quiet reversal. It comes after the assessed core precisely so that nothing required of you depends on being able to afford it.</p>

  <div class="info-box">
    <h4>&#127909; What you can approximate for free</h4>
    <p>You can get <em>part</em> of the way without paying. The free Claude.ai web app, combined with manual file discipline &mdash; you keep a real project folder, you paste files in, you save the outputs and decisions back into that folder yourself &mdash; gives you the most important idea of this whole track: <strong>the chat is not the archive</strong>. You can keep a decision log, a data inventory, and separated outputs entirely by hand.</p>
    <p>What you lose without the paid agent is the automation: it will not read and write your files for you, run your code, drive Git, or use Skills and subagents. You become the harness &mdash; doing by hand the file operations the agent would otherwise do. That is slower and more error-prone, but it is not nothing, and the <em>reproducibility discipline</em> in Lesson&nbsp;B is valuable whether a paid agent enforces it or you do.</p>
  </div>

  <h2 class="section-title">&#129520; The Disposition Shift: You Are Managing an Agent Now</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The hardest part of using Claude Code well is not technical. It is a shift in posture. In a chat you prompt and read, prompt and read &mdash; you are in the loop on every step. With an agent you <em>delegate</em>: you hand over a multi-step task and the agent goes away and does it. The skill is no longer prompt-craft. It is judgement &mdash; about what to delegate, where to put checkpoints, and how to verify what comes back.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Week&nbsp;11.1 borrowed Ethan Mollick&#39;s framing for exactly this moment: we are moving from working <em>with</em> a co-intelligence to managing what he calls a <em>wizard</em> &mdash; a system that produces sophisticated work through a process you did not watch and cannot fully see. His paradox holds here with force: <em>competence and opacity rise together</em>. The better the agent gets, the more it can do unsupervised, and the harder it becomes to verify. And Week&nbsp;10&#39;s Princeton reliability finding is the warning underneath: an agent that runs for an hour can do an hour of confident, plausible, wrong work. The verification burden does not shrink as the tool improves. It grows.</p>

  <div class="instructor-box">
    <h4>&#128100; From the instructor&#39;s own practice</h4>
    <p>&ldquo;There&rsquo;s a careful balance needed between micromanaging and making sure that there are clear boundaries and checkpoints. You don&rsquo;t want to let it loose in an unstructured way, and inherently there are dangers in anything agentic, but there needs to be some balance if it is going to be useful. It took a while to figure out the right oversight to give it, but now I treat it like a very capable, overenthusiastic graduate student who I have to keep a careful eye on at each checkpoint that I set.&rdquo;</p>
    <p>&ldquo;Setting checkpoints is key, but it&rsquo;s not enough. Because the volume of output is now so large, we are going to have to figure out how to both be effective and careful.&rdquo;</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">There is one more thing Week&nbsp;11.1 said that lands hardest here: two researchers using the identical tool can have wildly different experiences. The agent does not make you a good researcher. It amplifies whatever practice you bring to it. A careful researcher with strong verification habits gets a powerful collaborator; a careless one gets a faster way to produce confident nonsense. The rest of this track is, in effect, about being the first kind.</p>

  <h2 class="section-title">&#9878;&#65039; Discipline Proportionate to Stakes</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Before Lesson&nbsp;B lays out a fair amount of structure &mdash; immutable raw data, decision logs, reproducible folders &mdash; it is worth heading off a misreading. None of this is a ritual you must perform on every interaction. The honest practice is to <strong>match the discipline to the stakes and the lifespan of the work</strong>.</p>

  <div class="instructor-box">
    <h4>&#128100; From the instructor&#39;s own practice</h4>
    <p>&ldquo;I&rsquo;ve got many different projects. Some need serious scaffolding &mdash; to make sure everything is reproducible and auditable, and that I understand all of the underlying processes. Others need much less, but still have agentic aspects. An example of the latter is a project for my fitness goals, which reads in my smartwatch data and adjusts the training plan accordingly: the stakes there are low, and I&rsquo;ll question it if it feels really off.&rdquo;</p>
    <p>&ldquo;But something that&rsquo;s going to be published has much higher stakes &mdash; and so it needs much more scaffolding.&rdquo;</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Read Lesson&nbsp;B in that spirit. It shows you the full apparatus so you know what good looks like when the stakes are high. You then apply as much of it as the task in front of you deserves &mdash; which for an exploratory afternoon might be almost none, and for the analysis behind a paper figure should be most of it.</p>

  <div class="highlight-box">
    <h3>&#128221; The disposition, in three lines</h3>
    <p>Delegate, then verify &mdash; the burden of checking is yours and it grows with the agent&#39;s competence.</p>
    <p>The tool amplifies your practice; it does not replace your judgement.</p>
    <p>Scaffold in proportion to the stakes &mdash; heavy where the work must last, light where it need not.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 25px; margin-bottom: 15px;"><strong>Coming up in A.3:</strong> your first real session. We open a deliberately messy research archive, use plan mode to inspect it without changing anything, watch how permissions work, and meet the single most important file in any Claude Code project &mdash; <code>CLAUDE.md</code>, the control surface.</p>
"""


# ===========================================================================
# Lesson A.3 — First Contact and the Control Surface
# ===========================================================================

SL_A3_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>Enough framing &mdash; this lesson gets your hands on the tool. We do a first real session against a deliberately messy research archive, the kind every researcher actually has. You will inspect it <em>without changing anything</em>, see exactly how Claude Code asks permission before it touches a file, run the debrief that turns the exercise into a lesson, and meet <code>CLAUDE.md</code> &mdash; the file that steers every session and becomes, in Lesson&nbsp;B, the device that enforces reproducible habits.</p>
    <p>Setup is deliberately out of scope here: installation changes too often to print. Install Claude Code from the official documentation at <a href="https://docs.claude.com/en/docs/claude-code" target="_blank" rel="noopener">docs.claude.com</a>, confirm it runs, and come back.</p>
  </div>

  <h2 class="section-title">&#128193; The Sample Project: A Messy Research Archive</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Throughout this track we use one fictional running example: <strong>the Berg River microplastics study</strong>. A postgraduate has collected water samples at three sites &mdash; upstream of a town, in the town, and downstream &mdash; and counted microplastic particles across a sampling season. Wherever you see &ldquo;microplastic counts,&rdquo; read your own measurements; the structure is what matters, not the subject.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The starting archive is realistically messy, because real ones are. Inconsistent column names across files, two obvious data-entry errors, a confusingly named &ldquo;final-v2&rdquo; file with no v1 in sight, free-text field notes that contradict the spreadsheets in places, and a stale README referring to files that no longer exist:</p>

  <pre class="code-block">berg-river-microplastics/
  data/raw/
    site-upstream.csv          <span class="cm"># columns differ from the others</span>
    site_town.csv              <span class="cm"># mixed date formats; two data-entry errors</span>
    downstream-final-v2.csv    <span class="cm"># where is v1?</span>
    sampling-metadata.xlsx     <span class="cm"># site coordinates, dates, methods</span>
    field-notes.md             <span class="cm"># free text; contradicts the CSVs in places</span>
  literature-notes.md          <span class="cm"># half-organised reading notes</span>
  README-old.txt               <span class="cm"># stale; refers to files that are gone</span></pre>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">This is the perfect first task because the danger is obvious: you do <em>not</em> want an over-eager agent &ldquo;tidying&rdquo; your only copy of the raw data before you have understood it. So the first thing we do is the opposite of letting it loose.</p>

  <div class="resource-placeholder">
    <h4>&#128229; Download: the Berg River sample archive</h4>
    <p>Grab the deliberately-messy starting files and open the folder in Claude Code to follow along: <a href="files/berg-river-microplastics.zip">berg-river-microplastics.zip</a>. The same archive drives the full reproducible analysis in Lesson&nbsp;B.3. Equally good for this first inspect-only exercise &mdash; and arguably better &mdash; is to point Claude Code at <em>a real messy folder of your own</em>, provided you have a backup and you keep the agent in inspect-only mode throughout.</p>
  </div>

  <h2 class="section-title">&#128064; Your First Task: Inspect, Don&#39;t Change</h2>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Open a terminal in the project folder and start Claude Code:</p>

  <pre class="code-block">cd berg-river-microplastics
claude</pre>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Then give it an inspection-only task. The wording matters &mdash; it explicitly forbids changes:</p>

  <pre class="code-block"><span class="pr">&gt;</span> Inspect this folder before changing anything. Tell me what files
  are here, what each appears to contain, what you should not edit,
  and what you would recommend doing first. Do not move, rename, or
  edit anything yet.</pre>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Better still, put Claude Code into <strong>plan mode</strong> first (Claude Code lets you toggle a read-only planning mode in which it can look but cannot act). In plan mode the agent physically cannot edit a file &mdash; it can only inspect and propose. For a first encounter with a folder you care about, that guarantee is worth having rather than relying on the wording of your prompt alone.</p>

  <div class="info-box">
    <h4>&#128065; What to watch while it works</h4>
    <ul class="styled-list" style="margin-top: 0;">
      <li>Does it actually <em>read</em> the files before making claims about them, or does it guess from the names?</li>
      <li>Does it separate what it observed from what it inferred &mdash; &ldquo;this column is labelled pH&rdquo; versus &ldquo;this is probably pH&rdquo;?</li>
      <li>Does it flag the contradictions (the field notes versus the CSVs) rather than silently picking one?</li>
      <li>When it wants to do something, does it propose it and wait, or just do it?</li>
      <li>Which permissions does it ask you for, and which did you grant?</li>
    </ul>
  </div>

  <h2 class="section-title">&#128272; Permissions and Plan Mode</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">This is the moment to understand Claude Code&#39;s safety model, because it is what makes handing an agent your files defensible rather than reckless.</p>

  <div class="card-grid">
    <div class="card">
      <h3>Permission prompts</h3>
      <p>By default, Claude Code asks before it does anything consequential &mdash; editing a file, running a command. You see what it intends and approve or decline. The default posture is &ldquo;ask first,&rdquo; and for research work you should keep it that way until you have reason not to.</p>
    </div>
    <div class="card">
      <h3>Plan mode</h3>
      <p>A read-only mode: the agent inspects and produces a plan but cannot change anything. Use it for any first contact with real data, and for any step whose consequences you cannot easily reverse. It is the cheapest insurance in the tool.</p>
    </div>
    <div class="card">
      <h3>Allowlists</h3>
      <p>Once you trust a category of action &mdash; say, running your read-only inspection script &mdash; you can allow it without re-approving each time. The skill is allowlisting the genuinely safe and routine, never the destructive. (Your own projects, the survey showed, allowlist exact commands, not blanket access.)</p>
    </div>
    <div class="card">
      <h3>The sandbox boundary</h3>
      <p>Claude Code works in the folder you point it at. It does not roam your whole machine by default. Keep raw, sensitive, or irreplaceable material outside the working folder, or explicitly marked read-only, and the blast radius of any mistake stays small.</p>
    </div>
  </div>

  <h2 class="section-title">&#128172; The Debrief</h2>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">When the inspection is done, ask the question that converts the exercise into a transferable habit:</p>

  <pre class="code-block"><span class="pr">&gt;</span> What did you inspect, what did you infer, and what would you
  change only after my approval?</pre>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">A good answer cleanly separates the three. <em>Inspected</em>: the files it actually opened and what they contained. <em>Inferred</em>: the educated guesses &mdash; that &ldquo;final-v2&rdquo; supersedes a missing v1, that two values are data-entry errors. <em>Would change only with approval</em>: every rename, merge, and correction it is recommending but has not done. If the agent blurs these together, that is itself the finding: it is exactly the &ldquo;evidence versus guess&rdquo; line that Week&nbsp;9 spent a whole sub-lesson on, now showing up in a tool instead of a chat.</p>

  <h2 class="section-title">&#128221; <code>CLAUDE.md</code>: The Control Surface</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">You will not want to retype &ldquo;don&#39;t touch the raw data, separate evidence from inference, ask before editing&rdquo; at the start of every session. You should not have to. That is what <code>CLAUDE.md</code> is for: a plain-Markdown file at the root of your project that Claude Code reads automatically at the start of every session. It is the standing instruction set &mdash; the single most important file for steering the agent, and the thing that makes the next session behave like the last one.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">You can generate a starter with the <code>/init</code> command, which inspects the project and drafts a <code>CLAUDE.md</code> for you to edit. A minimal one for the Berg River project might begin:</p>

  <pre class="code-block"><span class="cm"># CLAUDE.md &mdash; Berg River microplastics study</span>

<span class="cm">## Working rules</span>
- Read files before proposing changes.
- Never modify anything in data/raw/. It is the only copy.
- Use plan mode and show me the plan before any consequential change.
- When you summarise or analyse, name which files you used.
- If something is uncertain, say so &mdash; do not fill the gap with a guess.
- Save scripts in scripts/ and generated outputs in outputs/.
- Before you tell me a task is done, show me the diff.</pre>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">One piece of vocabulary, since it recurs: a <strong>diff</strong> (short for &ldquo;difference&rdquo;) is the set of exact lines that changed between the old and new version of a file &mdash; what was removed and what was added &mdash; rather than the whole file. So &ldquo;show me the diff&rdquo; means <em>show me precisely what you changed</em>, not a description of it. It is the cheapest way to see what an agent actually did, and how to use it well at scale is a question we return to in Lesson&nbsp;B.3.</p>

  <div class="info-box">
    <h4>&#128161; This is the hinge of the whole track</h4>
    <p>Notice what just happened. Every one of those lines is a research-integrity habit this course already taught &mdash; &ldquo;do not fill the gap with a guess&rdquo; is the Week&nbsp;9 hallucination lesson; &ldquo;name which files you used&rdquo; is the Week&nbsp;5 citation lesson; &ldquo;show me the diff&rdquo; is verification. Written into <code>CLAUDE.md</code>, they stop being good intentions and become rules the agent follows every time. Lesson&nbsp;B turns this short file into the full <em>reproducibility-enforcement</em> template &mdash; the headline artefact of the track.</p>
  </div>

  <div class="highlight-box">
    <h3>&#9989; What to take from Lesson A</h3>
    <p>Claude Code is a model with hands in your project folder &mdash; the harness, not the model, is what you are driving. The work lives in files, not in the chat. It costs money and excludes some researchers, and we said so. Using it well is a shift from prompting to <em>managing</em>: delegate, checkpoint, verify, and scaffold in proportion to the stakes. And <code>CLAUDE.md</code> is where your standing rules live.</p>
    <p>Lesson&nbsp;B is the reason the track exists: turning all of this into research that someone else can inspect and repeat &mdash; reproducibility, made concrete.</p>
  </div>
"""


# ===========================================================================
# Lesson B.1 — Reproducibility, and the Reproducible Project Folder
# ===========================================================================

SL_B1_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>Lesson&nbsp;A was about driving the tool. Lesson&nbsp;B is the reason the whole track exists: using Claude Code to make your research genuinely <em>reproducible</em> &mdash; the kind of work a stranger, or you in two years, can open up, inspect, and repeat.</p>
    <p>This first page draws the distinction that the rest of the lesson hangs on: reproducibility is not the same as verification, and the two demand different things. Then it lays out the structure that makes reproducibility possible &mdash; the project folder as the unit of trustworthy research &mdash; and gives you a scaffold you can copy for your own work.</p>
    <p>The two pages that follow turn that structure into practice: a <code>CLAUDE.md</code> that enforces good habits, pre-registration, and reusable Skills (B.2); then a full worked analysis from messy data to a reproducible result, how to verify it, and how the folder itself becomes your disclosure (B.3).</p>
  </div>

  <h2 class="section-title">&#9878;&#65039; Reproducibility Is Not Verification</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The course has taught <strong>verification</strong> thoroughly &mdash; Week&nbsp;9 was largely about it. Verification asks a question about an output: <em>is this correct?</em> Did the model hallucinate the citation, get the analysis right, reason soundly? Reproducibility asks a different question, about a process: <em>could someone else inspect what I did and repeat it?</em> They are siblings, and they are not the same. A result can be correct but irreproducible (you got the right answer but cannot say how), and a process can be perfectly reproducible but wrong (anyone can repeat your flawed analysis exactly). Good research needs both.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Agentic work cuts both ways here, and it is worth being honest about both edges. It makes reproducibility <em>harder</em>, because the agent does a great deal autonomously and the steps can be opaque &mdash; this is Mollick&#39;s &ldquo;wizard&rdquo; problem from Week&nbsp;11.1, where competence and opacity rise together: the more the agent does for you, the less you watched it do. But it also makes reproducibility <em>easier</em> in a way manual work never managed, because the agent can be instructed to document as it goes &mdash; to log every decision, name every source, and save every script, tirelessly, without the human tendency to think &ldquo;I&#39;ll write that up later.&rdquo;</p>

  <div class="highlight-box">
    <h3>&#128161; The claim this lesson makes good on</h3>
    <p>Used with discipline, Claude Code can produce research that is <em>more</em> reproducible than typical manual work &mdash; not less. The reason is simple: a human researcher documents their decisions when they remember to and have time; an agent told to log every consequential choice does it every time, by default. The opacity is real, but it is a problem you solve by <em>instructing the agent to leave a trail</em>, and the rest of this lesson is how.</p>
  </div>

  <h2 class="section-title">&#128193; The Project Folder as the Unit of Reproducible Work</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Lesson&nbsp;A&#39;s organising principle was <em>the chat is not the archive</em>. Its positive form is this: the <strong>project folder</strong> is the unit of reproducible work. Everything that matters &mdash; the raw data, the code, the outputs, the decisions, the standing instructions, the version history &mdash; lives in one inspectable place. Here is what a reproducible version of the Berg River project looks like once it is set up properly:</p>

  <pre class="code-block">berg-river-microplastics/
  CLAUDE.md                  <span class="cm"># the standing instructions (B.2)</span>
  data/
    raw/                     <span class="cm"># the original data &mdash; never edited</span>
    processed/               <span class="cm"># cleaned data, regenerable from raw + scripts</span>
  scripts/                   <span class="cm"># the code, preserved and re-runnable</span>
  outputs/                   <span class="cm"># figures, tables, reports</span>
  notes/
    decision-log.md          <span class="cm"># every consequential choice, dated, with reasons</span>
  docs/
    data-inventory.md        <span class="cm"># what the data actually is</span>
  pre-registrations/         <span class="cm"># predictions + decision rules, before the compute (B.2)</span></pre>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Each part earns its place by answering a question a replicator would ask:</p>

  <div class="card-grid">
    <div class="card">
      <h3>data/raw/ &mdash; never edited</h3>
      <p>The original data, treated as immutable. Cleaning produces <em>new</em> files in <code>data/processed/</code>; the raw stays untouched so the whole chain can always be rebuilt from the source. The <code>CLAUDE.md</code> will forbid the agent from editing anything in here.</p>
    </div>
    <div class="card">
      <h3>scripts/ &mdash; the method, preserved</h3>
      <p>Every cleaning and analysis step is a saved script, not a one-off action in a chat. &ldquo;Re-run the analysis&rdquo; becomes a command, not a memory. This is the difference between a result you can regenerate and one you merely once obtained.</p>
    </div>
    <div class="card">
      <h3>outputs/ &mdash; derived, separate</h3>
      <p>Figures, tables, and reports live apart from the data and the code that made them, so it is always clear what is source, what is method, and what is product. Nothing in <code>outputs/</code> is hand-edited &mdash; if it&#39;s wrong, you fix the script and regenerate.</p>
    </div>
    <div class="card">
      <h3>notes/decision-log.md &mdash; the reasons</h3>
      <p>The single most valuable file for reproducibility. Which outliers were excluded and why; how missing values were handled; which test was chosen. The decisions a reader most needs and most often cannot find. The agent appends to it as it works.</p>
    </div>
    <div class="card">
      <h3>docs/data-inventory.md &mdash; what the data is</h3>
      <p>A plain description of each file, its variables, units, and known problems. The thing you wish every dataset you inherited had come with. Usually the first thing the agent writes, after inspecting the raw data.</p>
    </div>
    <div class="card">
      <h3>pre-registrations/ &mdash; the commitments</h3>
      <p>Where you write down what you expect to find, and the rule for deciding, <em>before</em> you run anything. This is the strongest single guard against fooling yourself, and it gets its own section in B.2.</p>
    </div>
  </div>

  <div class="info-box">
    <h4>&#9878;&#65039; Remember: discipline proportionate to stakes</h4>
    <p>This is the full apparatus, for work whose results have to survive, be repeated, or be defended &mdash; the analysis behind a paper figure, say. It is deliberately heavy. As Lesson&nbsp;A.2 argued, you apply as much of it as the task in front of you deserves: an exploratory afternoon might need only a <code>data-inventory.md</code> and a saved script; the headline analysis of your thesis should have all of it. The structure here is what &ldquo;good&rdquo; looks like at the high-stakes end, not a ritual for every interaction.</p>
  </div>

  <div class="resource-placeholder">
    <h4>&#128229; Download: the reproducible-project scaffold</h4>
    <p>An empty version of the structure above &mdash; the folders, a starter <code>CLAUDE.md</code>, and empty <code>decision-log.md</code> and <code>data-inventory.md</code> templates &mdash; ready to copy into your own project and adapt. <a href="files/reproducible-project-scaffold.zip">reproducible-project-scaffold.zip</a></p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 25px; margin-bottom: 15px;"><strong>Coming up in B.2:</strong> the structure is the skeleton; the habits are what bring it to life. Next we write the <code>CLAUDE.md</code> that makes the agent keep the raw data sacred and the decision log current &mdash; the headline artefact of this track &mdash; then add pre-registration and reusable Skills.</p>
"""


# ===========================================================================
# Lesson B.2 — Encoding Good Habits: CLAUDE.md, Pre-registration, and Skills
# ===========================================================================

SL_B2_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>A folder structure is a skeleton. This page adds the muscle: the standing instructions that make the agent keep the structure honest, the discipline of deciding what counts <em>before</em> you spend the compute, and the reusable Skills that turn a good workflow into one you can repeat across projects.</p>
    <p>The centrepiece is the <code>CLAUDE.md</code> research-habits template &mdash; the single most useful thing this track produces. It is where the integrity habits the whole course has taught stop being good intentions and become rules the agent follows every time.</p>
  </div>

  <h2 class="section-title">&#128203; The CLAUDE.md Research-Habits Template</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Lesson&nbsp;A.3 introduced <code>CLAUDE.md</code> as the control surface &mdash; the file Claude Code reads at the start of every session. Here it does its real job: encoding research integrity as machine-readable rules. This template is adapted, with thanks, from the <code>AGENTS.md</code> conventions in Dominik Luke&#353;&#39;s <em>Using AI Agents for Reproducible Research</em> workshop (Oxford), and extended with the harder-edged habits that working researchers tend to add once they have been burned a few times.</p>

  <pre class="code-block"><span class="cm"># CLAUDE.md &mdash; &lt;project name&gt;</span>

<span class="cm">## What this project is</span>
- One line on the project, the data, and the question.
- Status: e.g. &ldquo;fictional teaching project&rdquo; / &ldquo;real, unpublished &mdash; do not share&rdquo;.

<span class="cm">## Working rules</span>
- Read files before proposing changes.
- Never modify anything in data/raw/. It is the only copy.
- Use plan mode and show me the plan before any consequential change.
- When you summarise or analyse, name which files you used.
- If something is uncertain, say so &mdash; never fill a gap with a plausible guess.
- Save reusable code in scripts/; save generated outputs in outputs/.
- Log every consequential decision in notes/decision-log.md, dated, with the reason.
- Run analysis scripts to a committed log (... 2&gt;&amp;1 | tee outputs/&lt;name&gt;_run.log);
  the log, not the figure, is the record of what happened.
- Work from logs and printed tables, not screenshots, unless I ask otherwise.
- Before you tell me a task is done, show me the diff.

<span class="cm">## Pre-registration</span>
- If the pre-registrations/ folder has an entry for the current question,
  it is binding. Do not tune on the headline metric; do not reframe a
  result after the fact. If reality contradicts the prediction, apply the
  decision rule and say so plainly.

<span class="cm">## Boundaries</span>
- Don&#39;t add claims about real people, studies, or institutions that aren&#39;t in the sources.
- Don&#39;t commit or push unless I ask; don&#39;t send anything on my behalf.
- British spelling.</pre>

  <div class="info-box">
    <h4>&#128161; Why this is the hinge of the whole track</h4>
    <p>Read those rules again and notice what they are. Almost every line is a research-integrity habit this course already taught &mdash; now written somewhere the agent obeys it every time:</p>
    <ul class="styled-list" style="margin-top: 0;">
      <li>&ldquo;Never fill a gap with a plausible guess&rdquo; is the <strong>Week&nbsp;9 hallucination lesson</strong>.</li>
      <li>&ldquo;Name which files you used&rdquo; is the <strong>Week&nbsp;5 citation-integrity lesson</strong>.</li>
      <li>&ldquo;Log every consequential decision&rdquo; is <strong>reproducibility</strong> itself.</li>
      <li>&ldquo;Show me the diff before done&rdquo; is <strong>verification</strong> (Weeks&nbsp;9&ndash;10).</li>
      <li>&ldquo;Don&#39;t reframe a result after the fact&rdquo; is the <strong>calibrated-reading disposition</strong> the whole course is built on.</li>
    </ul>
    <p>The disposition the course spent eleven weeks building collapses, here, into one file you can drop into any project.</p>
  </div>

  <div class="resource-placeholder">
    <h4>&#128229; Download: the CLAUDE.md research-habits template</h4>
    <p>The template above as a ready-to-edit file. Drop it into the root of a project, fill in the top two lines, and adjust the rules to fit. <a href="files/CLAUDE-md-research-template.md">CLAUDE-md-research-template.md</a></p>
  </div>

  <h2 class="section-title">&#128221; Pre-registration: Decide What Counts Before You Spend the Compute</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">This is the habit that most separates careful computational research from the other kind, and it goes beyond anything in the source workshop. The idea is simple and old &mdash; it comes from clinical trials &mdash; and it transfers directly to any experiment where you can run a cheap pilot: <strong>write down what you expect to find, and the rule for deciding, before you run the thing.</strong></p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Concretely, a pre-registration is a short file, committed to <code>pre-registrations/</code> before any serious compute, that states: the question; what an <em>interesting</em>, a <em>boring-but-worth-knowing</em>, and a <em>dead</em> result would each look like, in advance; the analysis you will run; and the decision rule you will follow. The point is to bind your future self. When the result comes back and it is disappointing, the temptation is to quietly re-frame &mdash; to tune the metric, move the threshold, tell a flattering story. A committed pre-registration is what stops you, because the standard was set when you had nothing to defend.</p>

  <pre class="code-block"><span class="cm"># pre-registration: do microplastic counts differ across the three sites?</span>
<span class="cm"># committed 2026-03-20, before running the analysis</span>

Question: Is the median microplastic count higher at the town site than
  at the upstream site?

Prediction: Town &gt; upstream, by a margin large enough to matter ecologically
  (we set &ldquo;matters&rdquo; at a difference of &ge; 20 particles/L in advance).

Decision rule:
  - Interesting: town median exceeds upstream by &ge; 20 particles/L AND the
    difference survives a Mann-Whitney U test at p &lt; 0.05.
  - Boring-but-worth-knowing: a real but smaller difference, or no difference.
    Either way we report it straight.
  - Dead: the data are too sparse or too messy after cleaning to test at all.

Fixed in advance: outlier rule (exclude only samples the field notes mark
  unreliable); missing-value handling (listwise); the test (Mann-Whitney U,
  because counts are not normally distributed). No tuning of these on results.</pre>

  <div class="instructor-box">
    <h4>&#128100; From the instructor&#39;s own practice</h4>
    <p>&ldquo;It&rsquo;s very easy now to come up with ideas and to explore them. The important point is to figure out in advance what are going to be the markers for success as you go along, so writing them down before you start is vital.&rdquo;</p>
    <p>&ldquo;Of course sometimes you get a completely surprising result, but mostly you define a question and come up with what would correspond to an interesting outcome at each stage (starting off small) &mdash; and if it fails the test as you go along, that&rsquo;s generally the time to stop.&rdquo;</p>
    <p>&ldquo;This means you have to define interesting/important carefully upfront, but once you&rsquo;ve defined it, unless there&rsquo;s something really strange that happens, stick to it and save the compute. This is the pre-registration process: you register the gates at the start, and if the gates are closed as you go along, you stop.&rdquo;</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">That staged framing is what makes pre-registration practical rather than bureaucratic. You rarely commit one giant analysis up front and judge it only at the end; instead you set <em>gates at each stage</em> and run the cheapest stage first. A small pilot either clears its pre-registered gate or it does not. If it clears, you have earned the right to spend more compute on the next stage; if it does not, you stop &mdash; and you have spent almost nothing finding out. Pre-registration and cheap pilots belong together: the gates tell you, in advance and honestly, how far a question deserves to be taken before the next increment of effort. The discipline is not &ldquo;decide everything before you start&rdquo;; it is &ldquo;decide the gate before each step, and let a closed gate stop you.&rdquo;</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Pre-registration is the operational form of the course&#39;s deepest theme: ask &ldquo;is this interesting?&rdquo; not just &ldquo;is this publishable?&rdquo;, and be honest when the data say no. It is also where the agent earns its keep without being given a chance to flatter you: the <code>CLAUDE.md</code> rule above tells Claude Code that an existing pre-registration is <em>binding</em>, so the agent that runs your analysis is the same one holding you to the standard you set before you saw the answer.</p>

  <h2 class="section-title">&#129513; Skills and Subagents: Packaging Reproducible Practice</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">A <code>CLAUDE.md</code> encodes the rules of <em>one</em> project. A <strong>Skill</strong> packages a reusable <em>workflow</em> that travels across projects. Where a rule says &ldquo;always log decisions,&rdquo; a Skill says &ldquo;here is exactly how to build a data inventory, every time&rdquo; &mdash; a tested procedure rather than a re-improvised prompt.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">A Skill is a folder under <code>.claude/skills/</code> with a <code>SKILL.md</code> file: a little YAML header naming it and saying when to use it, then concise instructions. For example, a reproducible-research skill for creating a data inventory:</p>

  <pre class="code-block"><span class="cm"># .claude/skills/data-inventory/SKILL.md</span>
---
name: data-inventory
description: >
  Create docs/data-inventory.md describing each raw data file, its
  variables, units, row counts, and visible problems. Use when a project
  has data in data/raw/ and no inventory yet.
---

Inspect every file in data/raw/ (read-only). For each file, record:
the filename, what it appears to contain, the columns and their units,
the number of rows, missing-value counts, and any obvious anomalies
(impossible values, inconsistent column names, mixed date formats).
Do not edit the raw files. Where something is ambiguous, say so &mdash;
do not guess. Cross-check against any field notes and flag contradictions.
Write the result to docs/data-inventory.md.</pre>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Written once and inspected, that Skill produces the same disciplined inventory on every project you use it in. That repeatability is the reproducibility win: a Skill is a procedure you have tested and can trust, the opposite of ad-hoc prompting that varies every time.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;"><strong>Subagents</strong> add a second move. For a bounded job, Claude Code can spawn a separate, focused agent &mdash; and the most useful research application is verification. After the main agent has produced an analysis, you can have an independent subagent check it: re-derive the result from the raw data, look for the errors the first agent might have made, and report disagreements. This is the Week&nbsp;9 adversarial-verification idea made operational &mdash; a second pair of eyes that does not share the first agent&#39;s assumptions.</p>

  <div class="info-box">
    <h4>&#128270; A note on trust</h4>
    <p>A verification subagent is genuinely useful, but it is not magic: it is another instance of the same kind of system, and it can share the same blind spots. Treat it as one more screen, not as a guarantee &mdash; exactly as Week&nbsp;9 said of any single check. The human who reads the disagreements and decides what they mean is still you.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 25px; margin-bottom: 15px;"><strong>Coming up in B.3:</strong> we put all of it together &mdash; a full analysis of the Berg River data from messy files to a result a stranger could reproduce, then how to verify agentic work honestly, and why the reproducible folder turns out to be the best research-disclosure you can offer.</p>
"""


# ===========================================================================
# Lesson B.3 — The Reproducible Workflow, End to End
# ===========================================================================

SL_B3_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>Everything so far has been apparatus. This page runs it for real: a complete analysis of the messy Berg River data, from the first inspection to a result and a folder that someone else could open and reproduce. Then the two things that keep it honest &mdash; verifying work an agent did largely on its own, and disclosing what the AI actually did &mdash; where we find that the reproducible folder is itself the best disclosure you can give.</p>
  </div>

  <h2 class="section-title">&#128257; Git as a Reproducibility Trace</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">One piece of the structure deserves a word before the worked example, because it is the part most researchers skip. <strong>Git</strong> &mdash; the version-control system &mdash; records the state of your project over time. Each commit is a labelled snapshot; the history is a record of how the work actually evolved. You do not need to become a software engineer to benefit: even committing at a few milestones (&ldquo;raw data inventoried,&rdquo; &ldquo;cleaning done,&rdquo; &ldquo;analysis complete&rdquo;) gives you a trace that says what the project looked like at each stage, and lets you see exactly what changed between them.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Claude Code can do the Git work for you &mdash; initialise the repository, show you what changed, commit with a message &mdash; so the mechanics are not a barrier. What matters is the habit of using the history as a <em>research record</em>, not just a backup: a commit message like &ldquo;excluded D-03 per field note; corrected town-site pH for the calibration error&rdquo; turns the version history into a narrated account of your decisions. Used this way, Git is reproducibility infrastructure, not a developer&#39;s indulgence.</p>

  <h2 class="section-title">&#128300; A Worked Reproducible Analysis</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Here is the Berg River study, start to finish, with the discipline of the previous pages applied. The dataset is the same deliberately-messy archive from Lesson&nbsp;A.3 &mdash; downloadable below &mdash; and it has real problems planted in it: inconsistent column names, two data-entry errors, missing values, a field note that contradicts a value in the data, and a stale README. Watch how the structure turns that mess into something inspectable.</p>

  <ol class="step-list">
    <li><strong>Put the <code>CLAUDE.md</code> in place.</strong> The research-habits template from B.2 goes in the project root before anything else, so every rule &mdash; don&#39;t touch <code>data/raw/</code>, log decisions, don&#39;t guess &mdash; is active from the first action.</li>
    <li><strong>Inspect and inventory.</strong> In plan mode, the agent reads every raw file and writes <code>docs/data-inventory.md</code>: the columns (and the fact that the three site files name them differently), the units, the row counts, the missing values, and the anomalies &mdash; including a town-site pH of 72 that cannot be real, and a note that <code>field-notes.md</code> says sample D-03 was discarded though a value for it sits in the CSV.</li>
    <li><strong>Pre-register the question.</strong> Before running the comparison, the prediction and decision rule from B.2 go into <code>pre-registrations/</code> and are committed. The standard is set while there is nothing to defend.</li>
    <li><strong>Plan the analysis; you review it.</strong> Still in plan mode, the agent proposes the cleaning and analysis steps. You read the plan &mdash; this is the checkpoint &mdash; and approve it before a single file is written.</li>
    <li><strong>Clean, and log every decision.</strong> The agent writes a cleaning script to <code>scripts/</code> that harmonises the column names, corrects the town-site pH using the calibration note in the field notes (&divide;10), excludes D-03 because the field notes mark it discarded, and handles the missing values by the pre-registered rule. <em>Each of these choices is appended to <code>notes/decision-log.md</code>, dated, with its reason and its source.</em> The raw files are never touched; the cleaned data lands in <code>data/processed/</code>.</li>
    <li><strong>Run the analysis to a committed log.</strong> The analysis script runs the pre-registered Mann-Whitney test, prints its result to <code>outputs/analysis_run.log</code> (committed), and saves the figure and summary table to <code>outputs/</code>.</li>
    <li><strong>Record assumptions and uncertainty.</strong> The agent notes what it assumed and what remains uncertain &mdash; the small sample after exclusions, the reliance on the field note for the pH correction &mdash; rather than presenting a clean result as if nothing were in doubt.</li>
    <li><strong>Commit.</strong> A Git commit snapshots the whole state, with a message that narrates the decisions.</li>
  </ol>

  <div class="case-study">
    <h4>&#129510; The test that matters: hand it to a stranger</h4>
    <p>Now the question reproducibility actually asks. Give the finished folder to someone who was not there. Can they reconstruct what happened? Yes &mdash; and not because they trust you, but because the evidence is all present: the untouched raw data, the script that transforms it, the decision log explaining every judgement call (why D-03 went, why the pH was divided by ten), the pre-registration showing the standard was set in advance, the outputs, and the run log proving what was executed. They can re-run the script and get the same result, and they can <em>disagree</em> with a decision because they can see it.</p>
    <p>Contrast the same analysis done in a chat window. The model gives you the same answer, perhaps in the same minute. But the cleaning decisions are buried in a conversation you will lose; the pH correction is a thing the model did somewhere in the middle that nobody recorded; and next month there is no folder to hand anyone &mdash; only a number you once obtained and can no longer account for. Same model, same answer, utterly different research.</p>
  </div>

  <div class="resource-placeholder">
    <h4>&#128229; Download: the Berg River sample archive</h4>
    <p>The deliberately-messy starting files &mdash; the three inconsistent CSVs with their planted errors, the contradicting field notes, the stale README, and the metadata &mdash; so you can run this whole workflow yourself. <a href="files/berg-river-microplastics.zip">berg-river-microplastics.zip</a></p>
  </div>

  <h2 class="section-title">&#128270; Verifying Agentic Work</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">When the agent runs for an hour and makes a hundred changes you did not watch, the instinct is to inspect each one &mdash; to read every diff as it happens. That does not scale, and pretending it does is the fastest route to a false sense of safety. The volume <em>is</em> the problem: when so much is changing all the time, there often isn&#39;t a chance to check each change, and any carefulness that depends on watching every one will quietly fail. So the move is to take verification <em>off</em> the per-change axis. Don&#39;t try to catch every mistake as it happens; instead make mistakes survivable, encode what must stay true so a machine checks it, and verify the few things that actually matter. Week&nbsp;9&#39;s protocols and Week&nbsp;10&#39;s Princeton reliability finding still bite &mdash; the burden is real and it grows &mdash; but the response is to automate and target verification, not to watch harder.</p>

  <div class="card-grid">
    <div class="card">
      <h3>1. Make mistakes recoverable</h3>
      <p>The quiet hero. With <code>data/raw/</code> read-only, everything regenerable from raw plus scripts, and all of it under Git, any bad change can be rolled back and any output rebuilt. You are no longer reviewing to prevent disaster &mdash; disaster is structurally off the table &mdash; so you can safely <em>not</em> watch every step, and find errors later, in batch.</p>
    </div>
    <div class="card">
      <h3>2. Automate the checks</h3>
      <p>Write down what must stay true &mdash; row counts didn&#39;t drop, values stay in physical range, a known sub-result still holds &mdash; and have the agent assert it after changes. A Claude Code <em>hook</em> can run your check script automatically after every edit, so a silently-dropped column trips an assertion with no diff-reading at all. You read a one-line pass or fail, not the change.</p>
    </div>
    <div class="card">
      <h3>3. Verify the result, not every step</h3>
      <p>You cannot check every edit, but you can check the end against ground truth: re-derive the one number that matters, trace a few output values back to the raw data by hand, sanity-check against what you know of the domain. A hundred edits collapse into a handful of checks on the thing you actually care about.</p>
    </div>
    <div class="card">
      <h3>4. Let the decision log choose your diffs</h3>
      <p>You don&#39;t read every diff &mdash; you read the consequential ones. The &ldquo;log every consequential decision&rdquo; rule means the agent surfaces the handful that mattered (excluded D-03; divided the town pH by ten); those are the few worth your eyes, and the boilerplate you let go. The log is a high-signal substitute for the full diff.</p>
    </div>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">These layers catch different failures, and it helps to see which catches which. A <em>wrong-direction</em> failure &mdash; the agent confidently pursuing the wrong goal because it inferred the wrong intent, and taking you on a tangent for days &mdash; is invisible to any amount of diff-reading, because no single change is wrong; the <em>question</em> is wrong. That is what the pre-registration <em>gates</em> from B.2 are for: a closed gate stops the tangent early. A <em>quiet-correctness</em> failure &mdash; a dropped column, a plausible default you didn&#39;t notice &mdash; is what the automated assertions catch. And reviewing at the <em>checkpoint</em> (the commit boundary) rather than at every keystroke is how human review stays in the loop without becoming a full-time job. Verification scales when it is layered, not when it is heroic.</p>

  <div class="warning-box">
    <h4>&#9888;&#65039; What stays human, honestly</h4>
    <p>The structure verifies the <em>process</em>; it does not verify the <em>judgement</em>. Is this the right analysis for the question? Does the result make physical sense for a river? Is the effect real or an artefact of the small sample after exclusions? Those are research judgements, and no amount of logging makes them the agent&#39;s job. The Week&nbsp;7 silent-error problem and the Week&nbsp;9 plausible-but-wrong problem do not disappear because the work is well-documented &mdash; a beautifully reproducible analysis can still be reproducibly wrong. And there is a cost to all of this: tokens, time, and the genuine review effort every agentic result demands. Budget for it.</p>
  </div>

  <div class="instructor-box">
    <h4>&#128100; From the instructor&#39;s own practice</h4>
    <p>&ldquo;The errors that have mattered were never the dramatic ones &mdash; the agent rarely does something obviously absurd. They were quiet: a plausible default I didn&#39;t notice, a column silently dropped, a result that looked right and wasn&#39;t. What catches them is boring and reliable: reading the diff every time, keeping the decision log honest enough that a wrong choice stands out in it, and re-running the thing myself before I believe the number. The discipline isn&#39;t there to slow me down; it&#39;s there because the failures are invisible by design.&rdquo;</p>
    <p style="font-style: normal; font-size: 0.9em; color: #6a5da8;">[Instructor voice &mdash; adjust or replace with your own account.]</p>
  </div>

  <h2 class="section-title">&#128196; Disclosure: The Reproducible Folder Is the Disclosure</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Week&nbsp;4 and Week&nbsp;11.3 asked you to disclose your AI use. Week&nbsp;11.3 also delivered the bracing finding that, against roughly 70% of journals having an AI policy, only about 0.1% of papers actually disclose. Most disclosure, where it happens at all, is a vague sentence: &ldquo;AI tools were used in the preparation of this work.&rdquo; That sentence tells a reader almost nothing.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">A reproducible project folder flips the problem. You do not need a sentence that gestures at what the AI did, because the folder <em>shows</em> it: the <code>CLAUDE.md</code> states the rules the agent worked under; the decision log records every judgement and who made it; the scripts are the method; the Git history is the sequence of events; the pre-registration proves the standard predated the result. The honest answer to &ldquo;what did the AI do, and what did you decide?&rdquo; is not a paragraph &mdash; it is &ldquo;here is the folder.&rdquo; That is what good disclosure actually looks like, and it is a higher standard than almost any journal currently asks for.</p>

  <div class="info-box">
    <h4>&#127891; The capstone connection</h4>
    <p>If you took this track alongside the course, the Week&nbsp;12 capstone is where it can land: a reproducible project folder is the natural form for the concrete piece of work the capstone asks you to commit to. You do not just argue that you would use AI responsibly in your research &mdash; you show the structure in which you would.</p>
  </div>

  <div class="highlight-box">
    <h3>&#9989; What to take from the Advanced Track</h3>
    <p>Claude Code is a model with hands in your project folder, and the work lives in files, not in the chat. Reproducibility is a different goal from verification, and the agent can be instructed to serve it &mdash; logging decisions, keeping raw data sacred, holding you to a pre-registration &mdash; better than unaided human discipline usually manages.</p>
    <p>The <code>CLAUDE.md</code> research-habits template is where the course&#39;s integrity becomes a rule the agent follows. Pre-registration is where you refuse to fool yourself. The reproducible folder is where verification, disclosure, and trust all meet &mdash; the same folder answers all three.</p>
    <p>And the disposition underneath has not changed since Lesson&nbsp;A: delegate, then verify; the tool amplifies your practice rather than replacing your judgement; and you scaffold in proportion to what the work has to bear. Use the heavy machinery where the stakes are real, lightly where they are not, and honestly everywhere.</p>
  </div>
"""


# ---------------------------------------------------------------------------
# SUBLESSONS
# ---------------------------------------------------------------------------

SUBLESSONS = [
    {
        "filename": "Claude Code as a Research Environment.html",
        "title": "Advanced A.1 - What Claude Code Actually Is",
        "badge": "Advanced Track &bull; Lesson A &bull; 1 of 3",
        "header_emoji": "&#128421;&#65039;",  # desktop computer
        "header_title": "What Claude Code Actually Is",
        "header_subtitle": "An agent that lives in your project folder &mdash; where the model is the smallest part of what works for you",
        "body": SL_A1_BODY,
    },
    {
        "filename": "The Honest Case - Cost Access and Disposition.html",
        "title": "Advanced A.2 - The Honest Case: Cost, Access, and the Disposition",
        "badge": "Advanced Track &bull; Lesson A &bull; 2 of 3",
        "header_emoji": "&#9878;&#65039;",  # balance scale
        "header_title": "The Honest Case: Cost, Access, and the Shift in How You Work",
        "header_subtitle": "What it costs, who it excludes, what you can approximate for free, and the disposition it demands",
        "body": SL_A2_BODY,
    },
    {
        "filename": "First Contact and the Control Surface.html",
        "title": "Advanced A.3 - First Contact and the Control Surface",
        "badge": "Advanced Track &bull; Lesson A &bull; 3 of 3",
        "header_emoji": "&#129517;",  # compass
        "header_title": "First Contact and the Control Surface",
        "header_subtitle": "Your first real session, plan mode, permissions, and the CLAUDE.md file that steers everything",
        "body": SL_A3_BODY,
    },
    {
        "filename": "Reproducibility and the Project Folder.html",
        "title": "Advanced B.1 - Reproducibility, and the Reproducible Project Folder",
        "badge": "Advanced Track &bull; Lesson B &bull; 1 of 3",
        "header_emoji": "&#128257;",  # repeat
        "header_title": "Reproducibility, and the Reproducible Project Folder",
        "header_subtitle": "Why reproducibility is not the same as verification, and how a project folder becomes the unit of trustworthy research",
        "body": SL_B1_BODY,
    },
    {
        "filename": "Encoding Good Habits - CLAUDE.md Pre-registration and Skills.html",
        "title": "Advanced B.2 - Encoding Good Habits: CLAUDE.md, Pre-registration, and Skills",
        "badge": "Advanced Track &bull; Lesson B &bull; 2 of 3",
        "header_emoji": "&#128203;",  # clipboard
        "header_title": "Encoding Good Habits: CLAUDE.md, Pre-registration, and Skills",
        "header_subtitle": "Turning research integrity into rules the agent follows every time",
        "body": SL_B2_BODY,
    },
    {
        "filename": "The Reproducible Workflow End to End.html",
        "title": "Advanced B.3 - The Reproducible Workflow, End to End",
        "badge": "Advanced Track &bull; Lesson B &bull; 3 of 3",
        "header_emoji": "&#128300;",  # microscope
        "header_title": "The Reproducible Workflow, End to End",
        "header_subtitle": "A full analysis from messy data to a result a stranger could reproduce &mdash; then verifying it, and disclosing it",
        "body": SL_B3_BODY,
    },
]


TOC_HTML = """<html><head><meta http-equiv="'Content-Type'" content="'text/html;charset=utf-8'" /><title>MAM5020F 2026 | Gen AI for Research - Advanced Track: Agentic Research with Claude Code</title></head><body>
<div style="background: #003A70; padding: 8px 20px; text-align: center;"><a href="../index.html" style="color: white; text-decoration: none; font-size: 0.85em;">&#8592; Back to Contents</a></div><table cellpadding=0 cellspacing=0 border=0 width=100%><tr><td colspan=3>&nbsp;</td></tr><tr><td valign="top" width="100%"><font class="title"><strong>Advanced Track &mdash; Beyond the Free Tier: Agentic Research with Claude Code</strong></font><br><p style='margin-left: 25px; margin-top: 20px; color: #003A70; font-weight: bold; font-size: 1.1em;'>Lesson A &mdash; Claude Code as a Research Environment</p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Claude Code as a Research Environment.html" />A.1 What Claude Code Actually Is</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="The Honest Case - Cost Access and Disposition.html" />A.2 The Honest Case: Cost, Access, and the Disposition</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="First Contact and the Control Surface.html" />A.3 First Contact and the Control Surface</a></p><p style='margin-left: 25px; margin-top: 24px; color: #003A70; font-weight: bold; font-size: 1.1em;'>Lesson B &mdash; Reproducible Research Workflows</p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Reproducibility and the Project Folder.html" />B.1 Reproducibility, and the Reproducible Project Folder</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Encoding Good Habits - CLAUDE.md Pre-registration and Skills.html" />B.2 Encoding Good Habits: CLAUDE.md, Pre-registration, and Skills</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="The Reproducible Workflow End to End.html" />B.3 The Reproducible Workflow, End to End</a></p></td></tr></table><footer style="background: #f9f9f9; margin-top: 40px; padding: 22px 30px; text-align: center; color: #888; font-size: 0.85em; border-top: 1px solid #eee; font-family: 'Lato', 'Lucida Sans Unicode', 'Lucida Grande', sans-serif;">
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


def write_to(directory, filename, content):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  wrote {path}")


def main():
    print("Generating Advanced Track (Lesson A)...")
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
