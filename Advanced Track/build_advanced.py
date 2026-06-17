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
    <p>&ldquo;The mental adjustment that took me longest was learning to stop watching every step and start designing checkpoints instead. Early on I either micromanaged &mdash; which wastes the whole point &mdash; or I let it run and then could not tell whether the result was trustworthy. What works is treating it like supervising a capable but over-confident research assistant: be clear about the goal, insist on seeing the plan before the work, and verify the output as if a stranger had handed it to me, because in a real sense one has.&rdquo;</p>
    <p style="font-style: normal; font-size: 0.9em; color: #6a5da8;">[Instructor voice &mdash; adjust or replace with your own account.]</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">There is one more thing Week&nbsp;11.1 said that lands hardest here: two researchers using the identical tool can have wildly different experiences. The agent does not make you a good researcher. It amplifies whatever practice you bring to it. A careful researcher with strong verification habits gets a powerful collaborator; a careless one gets a faster way to produce confident nonsense. The rest of this track is, in effect, about being the first kind.</p>

  <h2 class="section-title">&#9878;&#65039; Discipline Proportionate to Stakes</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Before Lesson&nbsp;B lays out a fair amount of structure &mdash; immutable raw data, decision logs, reproducible folders &mdash; it is worth heading off a misreading. None of this is a ritual you must perform on every interaction. The honest practice is to <strong>match the discipline to the stakes and the lifespan of the work</strong>.</p>

  <div class="instructor-box">
    <h4>&#128100; From the instructor&#39;s own practice</h4>
    <p>&ldquo;My scaffolding scales with stakes and longevity, not prestige. A serious computational experiment and my personal training log get the same discipline &mdash; one source of truth, append-only logs, a protocol the agent cannot skip &mdash; because both are records I will need to trust months from now. A one-off read of a colleague&#39;s draft gets a structured output file and nothing else. The heavy machinery earns its place only where the work has to survive, be repeated, or be defended.&rdquo;</p>
    <p style="font-style: normal; font-size: 0.9em; color: #6a5da8;">[Instructor voice &mdash; adjust or replace with your own account.]</p>
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
]


TOC_HTML = """<html><head><meta http-equiv="'Content-Type'" content="'text/html;charset=utf-8'" /><title>MAM5020F 2026 | Gen AI for Research - Advanced Track: Agentic Research with Claude Code</title></head><body>
<div style="background: #003A70; padding: 8px 20px; text-align: center;"><a href="../index.html" style="color: white; text-decoration: none; font-size: 0.85em;">&#8592; Back to Contents</a></div><table cellpadding=0 cellspacing=0 border=0 width=100%><tr><td colspan=3>&nbsp;</td></tr><tr><td valign="top" width="100%"><font class="title"><strong>Advanced Track &mdash; Beyond the Free Tier: Agentic Research with Claude Code</strong></font><br><p style='margin-left: 25px; margin-top: 20px; color: #003A70; font-weight: bold; font-size: 1.1em;'>Lesson A &mdash; Claude Code as a Research Environment</p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Claude Code as a Research Environment.html" />A.1 What Claude Code Actually Is</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="The Honest Case - Cost Access and Disposition.html" />A.2 The Honest Case: Cost, Access, and the Disposition</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="First Contact and the Control Surface.html" />A.3 First Contact and the Control Surface</a></p><p style='margin-left: 25px; margin-top: 24px; color: #888; font-size: 0.95em;'>Lesson B &mdash; Reproducible Research Workflows <em>(in preparation)</em></p></td></tr></table><footer style="background: #f9f9f9; margin-top: 40px; padding: 22px 30px; text-align: center; color: #888; font-size: 0.85em; border-top: 1px solid #eee; font-family: 'Lato', 'Lucida Sans Unicode', 'Lucida Grande', sans-serif;">
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
