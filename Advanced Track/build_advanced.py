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
    <strong>&#9888;&#65039; This is the Advanced Track &mdash; it goes beyond the free tier.</strong> Everything in Weeks 1&ndash;12 was chosen so that you could do it on free tools, because access is not a detail (Week&nbsp;10) and most of the world&#39;s researchers do not have a paid AI budget (Week&nbsp;11.4). This track is the one deliberate exception. It uses <strong>Claude Code</strong>, which needs a paid Claude subscription and comfort with a terminal. It is genuinely optional, it sits <em>after</em> the Week&nbsp;12 capstone on purpose, and the next page makes the honest case for whether it is worth it to you, including what you can and cannot approximate without paying.
  </div>
"""


# ===========================================================================
# Lesson A.1 — What Claude Code Actually Is
# ===========================================================================

SL_A1_BODY = GATE_BANNER + """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>For most of this course, &ldquo;using AI&rdquo; has meant a chat window: you type, the model answers, you copy what is useful back into your own work. Claude Code is a different kind of thing, and the difference is the whole point of this track. It is an <em>agent</em> that works inside your real project folder. It reads your files, runs your code, edits your documents, uses version control, and can work on its own for long stretches.</p>
    <p>This first lesson does three things. It says what Claude Code is (and is not), using the model-versus-harness distinction from Week&nbsp;10. It draws the line between chatting and working with an agent, around a single principle: <strong>the chat is not the archive</strong>. And it sets up the question the rest of Lesson A answers: what does it actually take to drive one of these well?</p>
    <p>Lesson&nbsp;B then turns to the payoff this track exists for: using Claude Code to make your research genuinely <em>reproducible</em>, inspectable and repeatable by someone who is not you.</p>
  </div>

  <div class="info-box">
    <h4>&#128591; Sources and thanks</h4>
    <p>This track&rsquo;s reproducibility framework owes a large and explicit debt to <strong>Dominik Luke&#353;</strong>&rsquo;s workshop <em>Using AI Agents for Reproducible Research</em> (Oxford e-Research Centre). The organising principle that the chat is not the archive, the model-versus-harness framing, the research-habits instruction file, and the &ldquo;inspect a messy folder&rdquo; first task are all adapted, with thanks, from that workshop and its accompanying skills. His materials are openly available: <a href="https://techczech.github.io/agents-for-reproducibility/" target="_blank" rel="noopener">techczech.github.io/agents-for-reproducibility</a> (the workshop guide) and <a href="https://github.com/techczech/dominiks-agent-skills" target="_blank" rel="noopener">github.com/techczech/dominiks-agent-skills</a> (his agent-skills collection, MIT-licensed). The <code>grill-with-docs</code> glossary practice is from Matt Pocock (AI&nbsp;Hero). What this track adds on top (the pre-registration gates, the worked Berg River example, and the instructor&rsquo;s own practice in the boxes below) builds on that foundation.</p>
  </div>

  <h2 class="section-title">&#129518; The Model Is the Smallest Part</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Week&nbsp;10.1 argued that <strong>the harness is the product</strong>. The language model, Claude itself, is one component. What turns it into something useful is everything wrapped around it: the tools it can call, the files it can see, the commands it can run, the permissions it operates under, and the loop that lets it act, observe the result, and act again. In a chat window that harness is thin and invisible. In Claude Code it is thick, and it is the part you are actually driving.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">When you ask Claude in a browser tab to help with an analysis, the model is most of what you get. It can reason about what you paste in and write text back. When you ask Claude Code the same thing, the model is the <em>smallest</em> part of what goes to work. The harness gives it your actual data files, a shell to run a script, the ability to read the error message that script produced, version control to record what changed, and standing instructions about how your project works. The intelligence is similar; the leverage is not.</p>

  <div class="info-box">
    <h4>&#128161; The one-sentence version</h4>
    <p>This is a different kind of machine from a smarter chatbot: a model with hands, working in your project folder. Almost everything that follows in this track is about driving it well, and about the discipline that makes its work trustworthy afterwards.</p>
  </div>

  <h2 class="section-title">&#128295; What Claude Code Can Actually Do</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Claude Code runs in your terminal and operates on a folder you point it at. Within that folder, and only within it unless you say otherwise, it has a set of capabilities worth naming, because each one is a piece of the harness you will learn to use.</p>

  <div class="card-grid">
    <div class="card">
      <h3>Reads and writes your files</h3>
      <p>It can open, read, and edit the actual documents, data files, and scripts in your project: not a copy you pasted, the real thing. This is powerful, and it is why permission and raw-data rules matter (Lesson&nbsp;B).</p>
    </div>
    <div class="card">
      <h3>Runs commands and code</h3>
      <p>It can execute shell commands and run your analysis scripts, then read the output or the error and respond to it. The act&ndash;observe&ndash;act loop is what makes it an agent and not a text generator.</p>
    </div>
    <div class="card">
      <h3>Uses version control</h3>
      <p>It can initialise Git, commit changes, show you diffs, and read the history. Used well, this turns into a reproducibility trace (Lesson&nbsp;B.3), not just a software habit.</p>
    </div>
    <div class="card">
      <h3>Reads standing instructions</h3>
      <p>A <code>CLAUDE.md</code> file in the project is loaded at the start of every session. It is how you tell the agent the rules of <em>your</em> project once, instead of re-explaining every time. We meet it properly in A.3.</p>
    </div>
    <div class="card">
      <h3>Runs reusable Skills</h3>
      <p>A Skill is a packaged, reusable workflow (a folder with a <code>SKILL.md</code>) the agent can invoke when it is relevant: a tested research procedure that travels across projects instead of being re-improvised each time (Lesson&nbsp;B.2).</p>
    </div>
    <div class="card">
      <h3>Spawns subagents</h3>
      <p>For a bounded job it can launch a separate, focused agent, for example an independent check of an analysis it just produced. This connects directly to the adversarial-verification idea from Week&nbsp;9.</p>
    </div>
    <div class="card">
      <h3>Connects to external tools (MCP)</h3>
      <p>Through the Model Context Protocol it can reach approved external services and data sources (a reference database, a paper repository): the same MCP idea introduced in Week&nbsp;10.</p>
    </div>
    <div class="card">
      <h3>Plans before it acts</h3>
      <p>It has a read-only <em>plan mode</em>: it inspects and proposes a plan without changing anything, so you can approve the approach before a single file moves. It is a safety control we lean on, and we use it in A.3.</p>
    </div>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">None of these capabilities is exotic on its own; researchers have used shells, version control, and scripts for decades. What is new is that one system can use all of them <em>in a loop, on your behalf, from a plain-language request</em>. That is the capability Week&nbsp;11.1 called &ldquo;AI as a substantive collaborator,&rdquo; made operational. And as Week&nbsp;11.1 also insisted: the more the system can do unsupervised, the more the verification habit matters, not less.</p>

  <h2 class="section-title">&#128202; Why This Is Categorically Different From Chat</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">It is tempting to file Claude Code under &ldquo;a more capable chatbot.&rdquo; That framing will mislead you. What separates the two is <em>where the work lives</em>, not how capable each one is.</p>

  <div class="card-grid">
    <div class="card" style="border-left-color: #888;">
      <h3>In a chat window</h3>
      <p>You paste context in. The model answers. The useful output, the reasoning, the decisions you made along the way: all of it lives in a conversation thread. Next week the thread is buried; next month you cannot reconstruct what you actually did, or why. The work is real but the <em>record</em> evaporates.</p>
    </div>
    <div class="card">
      <h3>In Claude Code</h3>
      <p>The work lives in your files. The script it wrote is in <code>scripts/</code>. The output is in <code>outputs/</code>. The decision it made is in a log you told it to keep. The change is in the Git history. Six months later, you (or a stranger) can open the folder and see what happened.</p>
    </div>
  </div>

  <div class="highlight-box">
    <h3>&#128193; The chat is not the archive</h3>
    <p>The organising principle of the whole track, stated plainly: <strong>save your sources, notes, instructions, scripts, outputs, and decisions into files, not into a chat thread.</strong> The conversation is where the work is <em>commissioned</em>; the project folder is where the work <em>lives</em>. A chatbot session is a conversation you will lose. A project folder is the unit of reproducible research.</p>
    <p>Everything Lesson&nbsp;B builds (the folder discipline, the decision log, the reproducible analysis) follows from taking this one sentence seriously.</p>
  </div>

  <div class="info-box">
    <h4>&#9878;&#65039; This is not &ldquo;abandon chat&rdquo;</h4>
    <p>Chat is still the right tool for a great deal: a quick question, a brainstorm, a one-off paragraph, thinking out loud. The distinction is about <em>durability</em>. Reach for chat when the value is in the answer you read right now. Reach for an agent in a project folder when the value is in work that has to survive, be repeated, or be defended later. Most researchers will use both, for different things, and knowing which is which is itself a skill.</p>
  </div>

  <div class="resource-placeholder">
    <h4>&#128214; Download: the companion guide</h4>
    <p>The instructor has written a short guide, <em>Claude Code as a Co-Scientist</em>, that gathers this track&rsquo;s territory into a single document: the model-versus-harness mental model, the human work an agent must never touch, the reproducibility conventions of Lesson&nbsp;B, and a reference for the research <em>Skills</em> that build on them. It is the companion to these two lessons and goes further than we can here. Many of its ideas, the reproducibility framework above all, come from <strong>Dominik Luke&#353;</strong>&rsquo;s work, credited at the top of this lesson; the guide builds openly on that foundation and is shared in the same spirit. <a href="files/co-scientist-guide.pdf" target="_blank" rel="noopener">co-scientist-guide.pdf</a>. The seven research <em>Skills</em> it documents are available as a separate download in Lesson&nbsp;B.2.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 25px; margin-bottom: 15px;"><strong>Coming up in A.2:</strong> the honest case. Before you invest time learning to drive this, you deserve a straight account of what it costs, who it excludes, what you can approximate for free, and the genuine shift in how you work that it demands: the move from <em>chatting</em> to <em>managing an agent</em>.</p>
"""


# ===========================================================================
# Lesson A.2 — Cost, Access, and the Disposition Shift
# ===========================================================================

SL_A2_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>This is the one place in the entire course where we recommend a paid tool, so it gets the same calibrated treatment the course gives every other claim: an honest reckoning, not a sales pitch. This lesson covers what Claude Code costs, the equity problem that cost creates, what you can genuinely approximate on free tools, and the disposition shift from chatting to <em>managing an agent</em>.</p>
    <p>The aim is that by the end you can decide, for yourself and honestly, whether this track is worth it for your situation. For some readers it clearly will be; for others it clearly will not be, and saying so plainly is part of keeping faith with the rest of the course.</p>
  </div>

  <h2 class="section-title">&#128176; The Cost Picture</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Claude Code is not free. As of mid-2026 it is available through Anthropic&#39;s paid subscription tiers and via metered API usage; the entry subscription sits at roughly the price of a couple of streaming services per month, and the heavier tiers cost substantially more. Because these numbers change, this lesson does not pin an exact figure: check the current Anthropic pricing page rather than trusting a number a course page wrote months ago. (Trusting the live source over the cached claim is the Week&nbsp;9 disposition applied to pricing.)</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">There are two cost shapes worth distinguishing. A flat <strong>subscription</strong> gives you a generous but bounded amount of use for a predictable monthly fee, the right model for most individual researchers. <strong>Metered API</strong> use is pay-as-you-go and can run up quickly when an agent works autonomously for an hour across a large codebase: that is real money per run, and worth watching. Either way, the framing from Week&nbsp;3 applies: the cost is not only the invoice. It is also tokens, time, attention, and the review effort every piece of agent output demands.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The practical question this raises is how to <em>not</em> be surprised by it. Two cautions. On a subscription your usage is generous but not unlimited: sustained agentic work can reach the cap, at which point you wait for a reset, so budget for that if a deadline is near. On metered API use the spend concentrates in <em>long autonomous runs</em>: an agent working unattended for an hour across a large project is where a bill grows, far more than a quick exchange. Helpfully, the instincts that keep you safe also keep you cheap: a tightly-scoped task in plan mode costs less than &ldquo;go work out my whole project,&rdquo; and the pre-registration gates of Lesson&nbsp;B.2 stop you pouring compute into a question that has already failed its test.</p>

  <div class="info-box">
    <h4>&#128176; The bill is not only the tokens</h4>
    <p>Remember the burden named in the disposition shift below: every agentic result needs checking, and that review time is part of the true cost. A run that is cheap in tokens but produces an hour of plausible-but-wrong work you then have to untangle was not cheap. Scope tightly, checkpoint often, and the spend (of money <em>and</em> of attention) stays proportionate to the stakes.</p>
  </div>

  <h2 class="section-title">&#127757; The Equity Tension</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">This course has been militantly free-tier-first, and that was a deliberate choice with an argument behind it. Week&nbsp;10 made the case that &ldquo;just pay for the Pro plan&rdquo; is not advice but an assumption that excludes most of the people the course is for. Week&nbsp;11.4 put numbers on the African compute gap. A paid-tool track sits in direct tension with all of that, and the worst thing we could do is pretend otherwise.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">So, plainly: for a researcher in a well-funded lab, the subscription cost is a rounding error and this track is a straightforward yes. For a postgraduate paying out of pocket, in a department without an AI budget, on a currency that makes dollar-denominated subscriptions painful, it is a genuine barrier: the same barrier this course spent eleven weeks taking seriously. This track is the signposted exception, not a quiet reversal. It comes after the assessed core so that nothing required of you depends on being able to afford it.</p>

  <div class="info-box">
    <h4>&#127909; What you can approximate for free</h4>
    <p>You can get <em>part</em> of the way without paying. The free Claude.ai web app, combined with manual file discipline (you keep a real project folder, you paste files in, you save the outputs and decisions back into that folder yourself) gives you the central idea of this whole track: <strong>the chat is not the archive</strong>. You can keep a decision log, a data inventory, and separated outputs entirely by hand.</p>
    <p>What you lose without the paid agent is the automation: it will not read and write your files for you, run your code, drive Git, or use Skills and subagents. You become the harness, doing by hand the file operations the agent would otherwise do. That is slower and more error-prone, but it is not nothing, and the <em>reproducibility discipline</em> in Lesson&nbsp;B is valuable whether a paid agent enforces it or you do.</p>
  </div>

  <h2 class="section-title">&#129520; The Disposition Shift: You Are Managing an Agent Now</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The hardest part of using Claude Code well is not technical. It is a shift in posture. In a chat you prompt and read, prompt and read; you are in the loop on every step. With an agent you <em>delegate</em>: you hand over a multi-step task and the agent goes away and does it. The skill is no longer prompt-craft but judgement: what to delegate, where to put checkpoints, and how to verify what comes back.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Week&nbsp;11.1 borrowed Ethan Mollick&#39;s framing for exactly this moment: we are moving from working <em>with</em> a co-intelligence to managing what he calls a <em>wizard</em>, a system that produces sophisticated work through a process you did not watch and cannot fully see. His paradox holds here with force: <em>competence and opacity rise together</em> (Mollick, <a href="https://www.oneusefulthing.org/p/on-working-with-wizards" target="_blank" rel="noopener">&ldquo;On Working with Wizards,&rdquo;</a> 2025). The better the agent gets, the more it can do unsupervised, and the harder it becomes to verify. And Week&nbsp;10&#39;s Princeton reliability finding (<a href="https://arxiv.org/abs/2602.16666" target="_blank" rel="noopener">Rabanser et&nbsp;al., 2026</a>) is the warning underneath: an agent that runs for an hour can do an hour of confident, plausible, wrong work. The verification burden does not shrink as the tool improves. It grows.</p>

  <div class="instructor-box">
    <h4>&#128100; From the instructor&#39;s own practice</h4>
    <p>&ldquo;There&rsquo;s a careful balance needed between micromanaging and making sure that there are clear boundaries and checkpoints. You don&rsquo;t want to let it loose in an unstructured way, and inherently there are dangers in anything agentic, but there needs to be some balance if it is going to be useful. It took a while to figure out the right oversight to give it, but now I treat it like a very capable, overenthusiastic graduate student who I have to keep a careful eye on at each checkpoint that I set.&rdquo;</p>
    <p>&ldquo;Setting checkpoints is key, but it&rsquo;s not enough. Because the volume of output is now so large, we are going to have to figure out how to both be effective and careful.&rdquo;</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">There is one more thing Week&nbsp;11.1 said that bears on this directly: two researchers using the identical tool can have wildly different experiences. The agent does not make you a good researcher. It amplifies whatever practice you bring to it. A careful researcher with strong verification habits gets a powerful collaborator; a careless one gets a faster way to produce confident nonsense. The rest of this track is, in effect, about being the first kind.</p>

  <h2 class="section-title">&#129504; The Human Core: What Not to Automate</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">A workflow this automated has a failure mode that matters more than any bug: it can let you produce a paper without doing the research. Everything in Lesson&nbsp;B is worth using because it clears away drudgery, but the drudgery was never the research. The research is the thinking, and the thinking has to be yours. So before the structure arrives, here is the counterweight to the whole track: the work you must never hand over, however capable the agent becomes.</p>

  <div class="info-box">
    <h4>&#129302; A co-scientist, not a substitute scientist</h4>
    <p>The agent is for the work that is <strong>mechanical</strong> (fetching, extracting, formatting), <strong>repetitive</strong> (checking fifty claims or two hundred citations), and <strong>adversarial</strong> (an honest critic that will not flatter you). It is <em>not</em> for the work that is <strong>generative, interpretive, or authorial</strong>. The moment you let it do your thinking, reading, or writing, you have stopped doing research.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;"><strong>The idea is yours.</strong> Taste, noticing what is strange, what is beautiful, what is worth a year of your life, is the whole game, and it comes from immersion, conversation, teaching, and play, not from a prompt. Do not ask the agent for your research questions. Bring an idea you already care about and use the agent to <em>stress-test</em> it: surface the assumption it rests on, find the paper that already did it, ask the awkward question.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;"><strong>Reading is yours.</strong> Turning a PDF into Markdown is not reading it. The argument you have <em>with</em> a paper, the marginal note, the slow accretion of a mental map of a field, the connection that fires only in your own head: that is where research understanding is actually built. An agent can put a paper in front of you in a workable form; it cannot do the reading. Read deeply, and read more than the agent summarises.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;"><strong>Writing is thinking.</strong> Writing is not the transcription of finished thoughts; it is how the thoughts get finished. Putting an argument into sentences is what exposes the gap in the logic, forces the definition you were fudging, and tells you what you actually believe. If the agent writes your draft, you skip the thinking the writing was meant to do, and you end up defending prose you never reasoned your way to. So: <strong>you write the draft.</strong> The agent&rsquo;s job around your writing is to <em>critique</em> it, check its claims, and catch inconsistencies, not to produce it and not to supply your voice.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;"><strong>Judgement is yours.</strong> What a surprising result <em>means</em>, whether a finding is interesting or merely true, which thread to pull next: these are judgements, and judgement does not come off a shelf. The agent can lay out the options and the evidence; the choosing is yours.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;"><strong>The struggle is not a bug.</strong> Some of the friction in research, the stuck week, the fourth rewrite, the confusion that sits just before understanding, is not waste to be optimised away. It is often where the understanding is forged. Automate the drudgery, by all means; be wary of automating away the productive struggle along with it.</p>

  <div class="highlight-box">
    <h3>&#129514; The acid test</h3>
    <p>At the end, can you defend every idea, every claim, and every sentence as your own thinking? If yes, the agent helped you do research. If the agent did the thinking, you have a paper but you have not done research, and your examiners, your reviewers, and your future self will eventually find the hollow centre.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">This section is drawn from the instructor&rsquo;s companion guide, <em>Claude Code as a Co-Scientist</em>, available to download at the end of Lesson&nbsp;A.1. Keep it in view as you read Lesson&nbsp;B; the structure there exists to support this thinking, never to replace it.</p>

  <h2 class="section-title">&#9878;&#65039; Discipline Proportionate to Stakes</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Before Lesson&nbsp;B lays out a fair amount of structure (immutable raw data, decision logs, reproducible folders) it is worth heading off a misreading. None of this is a ritual you must perform on every interaction. The practice is to <strong>match the discipline to the stakes and the lifespan of the work</strong>.</p>

  <div class="instructor-box">
    <h4>&#128100; From the instructor&#39;s own practice</h4>
    <p>&ldquo;I&rsquo;ve got many different projects. Some need serious scaffolding &mdash; to make sure everything is reproducible and auditable, and that I understand all of the underlying processes. Others need much less, but still have agentic aspects. An example of the latter is a project for my fitness goals, which reads in my smartwatch data and adjusts the training plan accordingly: the stakes there are low, and I&rsquo;ll question it if it feels really off.&rdquo;</p>
    <p>&ldquo;But something that&rsquo;s going to be published has much higher stakes &mdash; and so it needs much more scaffolding.&rdquo;</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Read Lesson&nbsp;B in that spirit. It shows you the full apparatus so you know what good looks like when the stakes are high. You then apply as much of it as the task in front of you deserves, which for an exploratory afternoon might be almost none, and for the analysis behind a paper figure should be most of it.</p>

  <div class="highlight-box">
    <h3>&#128221; The disposition, in three lines</h3>
    <p>Delegate, then verify: the burden of checking is yours and it grows with the agent&#39;s competence.</p>
    <p>The tool amplifies your practice; it does not replace your judgement.</p>
    <p>Scaffold in proportion to the stakes: heavy where the work must last, light where it need not.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 25px; margin-bottom: 15px;"><strong>Coming up in A.3:</strong> your first real session. We open a deliberately messy research archive, use plan mode to inspect it without changing anything, watch how permissions work, and meet <code>CLAUDE.md</code>, the file that steers a Claude Code project.</p>
"""


# ===========================================================================
# Lesson A.3 — First Contact and the Control Surface
# ===========================================================================

SL_A3_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>Enough framing; this lesson gets your hands on the tool. We do a first real session against a deliberately messy research archive, the kind every researcher actually has. You will inspect it <em>without changing anything</em>, see how Claude Code asks permission before it touches a file, run the debrief that turns the exercise into a lesson, and meet <code>CLAUDE.md</code>, the file that steers every session and becomes, in Lesson&nbsp;B, the device that enforces reproducible habits.</p>
    <p>Setup is out of scope here: installation changes too often to print. Install Claude Code from the official documentation at <a href="https://docs.claude.com/en/docs/claude-code" target="_blank" rel="noopener">docs.claude.com</a>, confirm it runs, and come back.</p>
  </div>

  <h2 class="section-title">&#128193; The Sample Project: A Messy Research Archive</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Throughout this track we use one fictional running example: <strong>the Berg River microplastics study</strong>. A postgraduate has collected water samples at three sites (upstream of a town, in the town, and downstream) and counted microplastic particles across a sampling season. Wherever you see &ldquo;microplastic counts,&rdquo; read your own measurements; the structure is what matters, not the subject.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">The starting archive is realistically messy, because real ones are. Inconsistent column names across files, counts at one site that are quietly wrong in a way only the field notes explain, a confusingly named &ldquo;final-v2&rdquo; file with no v1 in sight, a contaminated outlier and some missing values, free-text field notes that explain anomalies the spreadsheets don&rsquo;t, and a stale README referring to files that no longer exist:</p>

  <pre class="code-block">berg-river-microplastics/
  data/raw/
    site-upstream.csv          <span class="cm"># one naming convention...</span>
    site_town.csv              <span class="cm"># ...different columns, DD/MM/YYYY dates</span>
    downstream-final-v2.csv    <span class="cm"># third naming; blank cells; one oddly high value; where is v1?</span>
    sampling-metadata.csv      <span class="cm"># site coordinates, dates, methods</span>
    field-notes.md             <span class="cm"># free text; explains anomalies the CSVs don't</span>
  literature-notes.md          <span class="cm"># half-organised reading notes</span>
  README-old.txt               <span class="cm"># stale; refers to files that are gone</span></pre>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">This is the perfect first task because the danger is obvious: you do <em>not</em> want an over-eager agent &ldquo;tidying&rdquo; your only copy of the raw data before you have understood it. So the first thing we do is the opposite of letting it loose.</p>

  <div class="resource-placeholder">
    <h4>&#128229; Download: the Berg River sample archive</h4>
    <p>Grab the deliberately-messy starting files and open the folder in Claude Code to follow along: <a href="files/berg-river-microplastics.zip">berg-river-microplastics.zip</a>. The same archive drives the full reproducible analysis in Lesson&nbsp;B.3. Equally good for this first inspect-only exercise, and arguably better, is to point Claude Code at <em>a real messy folder of your own</em>, provided you have a backup and you keep the agent in inspect-only mode throughout.</p>
  </div>

  <h2 class="section-title">&#128064; Your First Task: Inspect, Don&#39;t Change</h2>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Open a terminal in the project folder and start Claude Code:</p>

  <pre class="code-block">cd berg-river-microplastics
claude</pre>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Then give it an inspection-only task. The wording matters, because it explicitly forbids changes:</p>

  <pre class="code-block"><span class="pr">&gt;</span> Inspect this folder before changing anything. Tell me what files
  are here, what each appears to contain, what you should not edit,
  and what you would recommend doing first. Do not move, rename, or
  edit anything yet.</pre>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Better still, put Claude Code into <strong>plan mode</strong> first (Claude Code lets you toggle a read-only planning mode in which it can look but cannot act). In plan mode the agent physically cannot edit a file; it can only inspect and propose. For a first encounter with a folder you care about, that guarantee is worth having rather than relying on the wording of your prompt alone.</p>

  <div class="info-box">
    <h4>&#128065; What to watch while it works</h4>
    <ul class="styled-list" style="margin-top: 0;">
      <li>Does it actually <em>read</em> the files before making claims about them, or does it guess from the names?</li>
      <li>Does it separate what it observed from what it inferred: &ldquo;this column is labelled pH&rdquo; versus &ldquo;this is probably pH&rdquo;?</li>
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
      <p>By default, Claude Code asks before it does anything consequential, such as editing a file or running a command. You see what it intends and approve or decline. The default posture is &ldquo;ask first,&rdquo; and for research work you should keep it that way until you have reason not to.</p>
    </div>
    <div class="card">
      <h3>Plan mode</h3>
      <p>A read-only mode: the agent inspects and produces a plan but cannot change anything. Use it for any first contact with real data, and for any step whose consequences you cannot easily reverse. It is the cheapest insurance in the tool.</p>
    </div>
    <div class="card">
      <h3>Allowlists</h3>
      <p>Once you trust a category of action, say running your read-only inspection script, you can allow it without re-approving each time. The skill is allowlisting the genuinely safe and routine, never the destructive. (Your own projects, the survey showed, allowlist exact commands, not blanket access.)</p>
    </div>
    <div class="card">
      <h3>The sandbox boundary</h3>
      <p>Claude Code works in the folder you point it at. It does not roam your whole machine by default. Keep raw, sensitive, or irreplaceable material outside the working folder, or explicitly marked read-only, and the blast radius of any mistake stays small.</p>
    </div>
  </div>

  <h2 class="section-title">&#128274; What Leaves Your Machine</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The permissions model governs what the agent may <em>do</em> to your files. There is a second question it does not answer, and for research data it is the more important one: what <em>leaves your machine</em>? Claude Code runs in your terminal, but the model does not. When the agent reads a file, that file&#39;s contents are sent to Anthropic&#39;s API for the model to process; that is how it &ldquo;sees&rdquo; them at all. Pointing the agent at a folder is, in effect, sending that folder&#39;s contents to a third party. For a great deal of research that is completely fine. For some of it, it is the whole question.</p>

  <div class="warning-box">
    <h4>&#9888;&#65039; Before you point an agent at confidential data</h4>
    <p>If your data is human-subjects data under an ethics approval, personal data under POPIA or the GDPR, or covered by an NDA or a data-use agreement, you carry an obligation that is entirely separate from how good the tool is: <strong>establish whether sending it to a third-party service is permitted at all.</strong> Your ethics clearance or data agreement may forbid external processing, require de-identification first, or demand specific contractual terms. That is yours to confirm <em>before</em> the first <code>claude</code> in that folder, not the tool&#39;s, and not an afterthought.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Two things are worth keeping separate. First, the <strong>provider&#39;s data-usage terms</strong>: whether your inputs are retained or used to improve models. For Anthropic&#39;s commercial and API products the default is that they are <em>not</em> used for training; the consumer subscription plans are governed separately, and those settings have changed over time. So apply the Week&nbsp;9 habit and read the <a href="https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training" target="_blank" rel="noopener">current data-usage terms for your plan</a> rather than trusting a claim a course page wrote months ago. Second, and independent of that: <strong>your own obligations</strong>. Even a provider that never trains on your data is still a third party your ethics approval may not permit you to send participant data to. The training question and the permission-to-send question are different, and you have to clear both.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">In practice, a few habits keep you on the right side of this:</p>

  <div class="card-grid">
    <div class="card">
      <h3>State the data&#39;s status</h3>
      <p>Put it at the very top of <code>CLAUDE.md</code>: &ldquo;real, human-subjects; do not share externally&rdquo; versus &ldquo;public; fine to process.&rdquo; It reminds you each session, and it tells the agent the stakes it is working under.</p>
    </div>
    <div class="card">
      <h3>Work on extracts, not the originals</h3>
      <p>Where you can, point the agent at de-identified, sampled, or synthetic data and keep the identifiable originals out of the working folder entirely. The agent can only transmit what it can read.</p>
    </div>
    <div class="card">
      <h3>Keep secrets out of the folder</h3>
      <p>API keys, passwords, tokens: an agent that reads a config file reads those too. Keep them in environment variables, never in the working tree, and <code>.gitignore</code> anything sensitive so it is neither read nor committed.</p>
    </div>
    <div class="card">
      <h3>Mind what you commit</h3>
      <p>Never commit participant data or credentials to a repository, especially a public one. A <code>.gitignore</code> covering <code>data/raw/</code> and any secrets stops one careless commit from becoming a permanent, published mistake.</p>
    </div>
  </div>

  <h2 class="section-title">&#128172; The Debrief</h2>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">When the inspection is done, ask the question that converts the exercise into a transferable habit:</p>

  <pre class="code-block"><span class="pr">&gt;</span> What did you inspect, what did you infer, and what would you
  change only after my approval?</pre>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">A good answer cleanly separates the three. <em>Inspected</em>: the files it actually opened and what they contained. <em>Inferred</em>: the educated guesses, that &ldquo;final-v2&rdquo; supersedes a missing v1, that two values are data-entry errors. <em>Would change only with approval</em>: every rename, merge, and correction it is recommending but has not done. If the agent blurs these together, that is itself the finding: it is the &ldquo;evidence versus guess&rdquo; line that Week&nbsp;9 spent a whole sub-lesson on, now showing up in a tool instead of a chat.</p>

  <h2 class="section-title">&#128221; <code>CLAUDE.md</code>: The Control Surface</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">You will not want to retype &ldquo;don&#39;t touch the raw data, separate evidence from inference, ask before editing&rdquo; at the start of every session. You should not have to. That is what <code>CLAUDE.md</code> is for: a plain-Markdown file at the root of your project that Claude Code reads automatically at the start of every session. It is the standing instruction set for steering the agent, and the thing that makes the next session behave like the last one.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">You can generate a starter with the <code>/init</code> command, which inspects the project and drafts a <code>CLAUDE.md</code> for you to edit. A minimal one for the Berg River project might begin like this:</p>

  <pre class="code-block"><span class="cm"># CLAUDE.md &mdash; Berg River microplastics study</span>

<span class="cm">## Working rules</span>
- Read files before proposing changes.
- Never modify anything in data/raw/. It is the only copy.
- Use plan mode and show me the plan before any consequential change.
- When you summarise or analyse, name which files you used.
- If something is uncertain, say so &mdash; do not fill the gap with a guess.
- Save scripts in scripts/ and generated outputs in outputs/.
- Before you tell me a task is done, show me the diff.</pre>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">One piece of vocabulary, since it recurs: a <strong>diff</strong> (short for &ldquo;difference&rdquo;) is the set of exact lines that changed between the old and new version of a file, what was removed and what was added, rather than the whole file. So &ldquo;show me the diff&rdquo; means <em>show me what you changed</em>, not a description of it. It is the cheapest way to see what an agent actually did, and how to use it well at scale is a question we return to in Lesson&nbsp;B.3.</p>

  <div class="info-box">
    <h4>&#128161; Where the course&#39;s habits become rules</h4>
    <p>Every one of those lines is a research-integrity habit this course already taught. &ldquo;Do not fill the gap with a guess&rdquo; is the Week&nbsp;9 hallucination lesson; &ldquo;name which files you used&rdquo; is the Week&nbsp;5 citation lesson; &ldquo;show me the diff&rdquo; is verification. Written into <code>CLAUDE.md</code>, they stop being good intentions and become rules the agent follows every time. Lesson&nbsp;B turns this short file into the full <em>reproducibility-enforcement</em> template.</p>
  </div>

  <h2 class="section-title">&#129504; Sessions, Memory, and Starting Fresh</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">One practical thing about how Claude Code behaves over a long task. A session has a finite <strong>context window</strong>, the amount it can hold in working memory at once. A morning&#39;s analysis can fill it, and as it fills, the agent starts to lose track of what was said early on. This sounds like a limitation, and in part it is. It is also where this track&#39;s organising principle pays off.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Because <em>the chat is not the archive</em>, you are never dependent on the conversation surviving. The project state lives on disk: the <code>CLAUDE.md</code> (re-read automatically at the start of every session), the decision log, the scripts, the Git history. So you can end a bloated, drifting session and start a clean one whenever you like: quit, run <code>claude</code> again, and the new session picks the project up <em>from the files</em>, not from a transcript you have lost. A fresh session pointed at a well-kept folder is often sharper than a long one that has wandered.</p>

  <div class="info-box">
    <h4>&#128161; The corollary of &ldquo;the chat is not the archive&rdquo;</h4>
    <p>If losing the conversation would lose your work, your work is in the wrong place. In a well-kept project folder the conversation is disposable by design: you commission the work in the chat, it lands in the files, and the next session starts fresh from those files. This is also why committing at milestones matters: a brand-new session can read the Git history and the decision log and see exactly where things stand, with no memory of the chat required.</p>
  </div>

  <div class="highlight-box">
    <h3>&#9989; What to take from Lesson A</h3>
    <p>Claude Code is a model with hands in your project folder, and the harness, not the model, is what you are driving. The work lives in files, not in the chat. It costs money and excludes some researchers, and we said so. Using it well is a shift from prompting to <em>managing</em>: delegate, checkpoint, verify, and scaffold in proportion to the stakes. And <code>CLAUDE.md</code> is where your standing rules live.</p>
    <p>Lesson&nbsp;B is the reason the track exists: turning all of this into research that someone else can inspect and repeat, reproducibility made concrete.</p>
  </div>
"""


# ===========================================================================
# Lesson B.1 — Reproducibility, and the Reproducible Project Folder
# ===========================================================================

SL_B1_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>Lesson&nbsp;A was about driving the tool. Lesson&nbsp;B is the reason the whole track exists: using Claude Code to make your research genuinely <em>reproducible</em>, the kind of work a stranger, or you in two years, can open up, inspect, and repeat.</p>
    <p>This first page draws the distinction that the rest of the lesson hangs on: reproducibility is not the same as verification, and the two demand different things. Then it lays out the structure that makes reproducibility possible, the project folder as the unit of trustworthy research, and gives you a scaffold you can copy for your own work.</p>
    <p>The two pages that follow turn that structure into practice: a <code>CLAUDE.md</code> that enforces good habits, pre-registration, and reusable Skills (B.2); then a full worked analysis from messy data to a reproducible result, how to verify it, and how the folder itself becomes your disclosure (B.3).</p>
  </div>

  <h2 class="section-title">&#9878;&#65039; Reproducibility Is Not Verification</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">The course has taught <strong>verification</strong> thoroughly; Week&nbsp;9 was largely about it. Verification asks a question about an output: <em>is this correct?</em> Did the model hallucinate the citation, get the analysis right, reason soundly? Reproducibility asks a different question, about a process: <em>could someone else inspect what I did and repeat it?</em> They are siblings, and they are not the same. A result can be correct but irreproducible (you got the right answer but cannot say how), and a process can be perfectly reproducible but wrong (anyone can repeat your flawed analysis exactly). Good research needs both.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Agentic work cuts both ways here, on both edges at once. It makes reproducibility <em>harder</em>, because the agent does a great deal autonomously and the steps can be opaque: this is Mollick&#39;s &ldquo;wizard&rdquo; problem from Week&nbsp;11.1, where competence and opacity rise together, so the more the agent does for you, the less you watched it do. But it also makes reproducibility <em>easier</em> in a way manual work never managed, because the agent can be instructed to document as it goes, to log every decision, name every source, and save every script, tirelessly, without the human tendency to think &ldquo;I&#39;ll write that up later.&rdquo;</p>

  <div class="highlight-box">
    <h3>&#128161; The claim this lesson makes good on</h3>
    <p>Used with discipline, Claude Code can produce research that is <em>more</em> reproducible than typical manual work, not less. A human researcher documents their decisions when they remember to and have time; an agent told to log every consequential choice does it every time, by default. The opacity is real, but it is a problem you solve by <em>instructing the agent to leave a trail</em>, and the rest of this lesson is how.</p>
  </div>

  <h2 class="section-title">&#128193; The Project Folder as the Unit of Reproducible Work</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Lesson&nbsp;A&#39;s organising principle was <em>the chat is not the archive</em>. Its positive form is this: the <strong>project folder</strong> is the unit of reproducible work. Everything that matters lives in one inspectable place: the raw data, the code, the outputs, the decisions, the standing instructions, the version history. Here is what a reproducible version of the Berg River project looks like once it is set up properly:</p>

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

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Each part answers a question a replicator would ask:</p>

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
      <p>Figures, tables, and reports live apart from the data and the code that made them, so it is always clear what is source, what is method, and what is product. Nothing in <code>outputs/</code> is hand-edited; if it&#39;s wrong, you fix the script and regenerate.</p>
    </div>
    <div class="card">
      <h3>notes/decision-log.md &mdash; the reasons</h3>
      <p>Which outliers were excluded and why; how missing values were handled; which test was chosen. The decisions a reader most needs and most often cannot find. The agent appends to it as it works.</p>
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
    <p>This is the full apparatus, for work whose results have to survive, be repeated, or be defended: the analysis behind a paper figure, say. It is heavy by design. As Lesson&nbsp;A.2 argued, you apply as much of it as the task in front of you deserves: an exploratory afternoon might need only a <code>data-inventory.md</code> and a saved script; the main analysis of your thesis should have all of it. The structure here is what &ldquo;good&rdquo; looks like at the high-stakes end, not a ritual for every interaction.</p>
  </div>

  <div class="resource-placeholder">
    <h4>&#128229; Download: the reproducible-project scaffold</h4>
    <p>An empty version of the structure above (the folders, a starter <code>CLAUDE.md</code>, and empty <code>decision-log.md</code> and <code>data-inventory.md</code> templates) ready to copy into your own project and adapt. <a href="files/reproducible-project-scaffold.zip">reproducible-project-scaffold.zip</a></p>
  </div>

  <div class="info-box">
    <h4>&#128218; Foundations and further reading</h4>
    <p>None of this discipline is new with AI; agentic tools mainly make it easier to practise. It draws on two established literatures worth knowing in their own right:</p>
    <ul class="styled-list" style="margin-top: 0;">
      <li><strong>Why reproducibility matters.</strong> That a great deal of published research does not hold up is argued in Ioannidis, <em>Why Most Published Research Findings Are False</em> (<a href="https://doi.org/10.1371/journal.pmed.0020124" target="_blank" rel="noopener">2005, PLoS Medicine</a>); the Open Science Collaboration&#39;s mass replication of psychology studies (<a href="https://doi.org/10.1126/science.aac4716" target="_blank" rel="noopener">2015, Science</a>); and Baker&#39;s survey of 1,500 researchers (<a href="https://doi.org/10.1038/533452a" target="_blank" rel="noopener">2016, Nature</a>).</li>
      <li><strong>How to do it in practice.</strong> The project-folder structure above is essentially an implementation of Sandve et&nbsp;al., <em>Ten Simple Rules for Reproducible Computational Research</em> (<a href="https://doi.org/10.1371/journal.pcbi.1003285" target="_blank" rel="noopener">2013, PLoS Computational Biology</a>) and Wilson et&nbsp;al., <em>Good Enough Practices in Scientific Computing</em> (<a href="https://doi.org/10.1371/journal.pcbi.1005510" target="_blank" rel="noopener">2017, PLoS Computational Biology</a>), both short, practical, and worth reading in full.</li>
    </ul>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 25px; margin-bottom: 15px;"><strong>Coming up in B.2:</strong> the structure is the skeleton; the habits are what bring it to life. Next we write the <code>CLAUDE.md</code> that makes the agent keep the raw data sacred and the decision log current, then add pre-registration and reusable Skills.</p>
"""


# ===========================================================================
# Lesson B.2 — Encoding Good Habits: CLAUDE.md, Pre-registration, and Skills
# ===========================================================================

SL_B2_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>A folder structure is a skeleton. This page adds the muscle: the standing instructions that make the agent keep the structure honest, the discipline of deciding what counts <em>before</em> you spend the compute, and the reusable Skills that turn a good workflow into one you can repeat across projects.</p>
    <p>The centrepiece is the <code>CLAUDE.md</code> research-habits template. It is where the integrity habits the whole course has taught stop being good intentions and become rules the agent follows every time.</p>
  </div>

  <h2 class="section-title">&#128203; The CLAUDE.md Research-Habits Template</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Lesson&nbsp;A.3 introduced <code>CLAUDE.md</code> as the control surface, the file Claude Code reads at the start of every session. Here it does its real job: encoding research integrity as machine-readable rules. This template is adapted, with thanks, from the <code>AGENTS.md</code> conventions in Dominik Luke&#353;&#39;s <em>Using AI Agents for Reproducible Research</em> workshop (Oxford), and extended with the harder-edged habits that working researchers tend to add once they have been burned a few times.</p>

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
    <h4>&#128161; The course&#39;s habits, written as rules</h4>
    <p>Almost every line is a research-integrity habit this course already taught, now written somewhere the agent obeys it every time:</p>
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

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">This is the habit that most separates careful computational research from the other kind, and it goes beyond anything in the source workshop. The idea is simple and old. It comes from clinical trials, and the case for making it a routine research habit rather than a clinical-trials formality is laid out in Nosek et&nbsp;al.&#39;s <em><a href="https://doi.org/10.1073/pnas.1708274114" target="_blank" rel="noopener">The Preregistration Revolution</a></em> (2018, PNAS). It transfers directly to any experiment where you can run a cheap pilot: <strong>write down what you expect to find, and the rule for deciding, before you run the thing.</strong></p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Concretely, a pre-registration is a short file, committed to <code>pre-registrations/</code> before any serious compute, that states: the question; what an <em>interesting</em>, a <em>boring-but-worth-knowing</em>, and a <em>dead</em> result would each look like, in advance; the analysis you will run; and the decision rule you will follow. The point is to bind your future self. When the result comes back and it is disappointing, the temptation is to quietly re-frame: to tune the metric, move the threshold, tell a flattering story. A committed pre-registration is what stops you, because the standard was set when you had nothing to defend.</p>

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

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">That staged framing is what makes pre-registration practical rather than bureaucratic. You rarely commit one giant analysis up front and judge it only at the end; instead you set <em>gates at each stage</em> and run the cheapest stage first. A small pilot either clears its pre-registered gate or it does not. If it clears, you have earned the right to spend more compute on the next stage; if it does not, you stop, having spent almost nothing finding out. Pre-registration and cheap pilots belong together: the gates tell you, in advance and honestly, how far a question deserves to be taken before the next increment of effort. The discipline is to decide the gate before each step, and to let a closed gate stop you, rather than to decide everything before you start.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Pre-registration is the operational form of the course&#39;s deepest theme: ask &ldquo;is this interesting?&rdquo; not just &ldquo;is this publishable?&rdquo;, and be honest when the data say no. It is also where the agent earns its keep without being given a chance to flatter you: the <code>CLAUDE.md</code> rule above tells Claude Code that an existing pre-registration is <em>binding</em>, so the agent that runs your analysis is the same one holding you to the standard you set before you saw the answer.</p>

  <h2 class="section-title">&#129513; Skills and Subagents: Packaging Reproducible Practice</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">A <code>CLAUDE.md</code> encodes the rules of <em>one</em> project. A <strong>Skill</strong> packages a reusable <em>workflow</em> that travels across projects. Where a rule says &ldquo;always log decisions,&rdquo; a Skill says &ldquo;here is exactly how to build a data inventory, every time&rdquo;: a tested procedure rather than a re-improvised prompt.</p>

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

  <div class="resource-placeholder">
    <h4>&#128230; Download: seven research Skills</h4>
    <p>The <code>data-inventory</code> Skill above is deliberately small, to show the shape. To see the idea at full size, and to actually use it, here is a bundle of seven ready-to-install Skills for reproducible research: <code>pre-register</code> (idea triage before you spend compute), <code>arxiv-fetcher</code> and <code>academic-pdf-to-mkd</code> (getting papers into a workable form), <code>paper-review</code>, <code>claim-fact-checker</code> and <code>reference-verifier</code> (the Week&nbsp;9 verification habit, packaged as procedures), and <code>convergence-check</code> (an honest read on whether an iterative loop is converging or just spinning). Unzip, drop the folders into <code>~/.claude/skills/</code>, and Claude Code loads each one on demand. <a href="files/co-scientist-skills.zip">co-scientist-skills.zip</a></p>
    <p style="font-size: 0.92em; color: #777;">Three of the seven (<code>academic-pdf-to-mkd</code>, <code>claim-fact-checker</code>, and <code>paper-review</code>) are adapted, with thanks, from <strong>Dominik Luke&#353;</strong>&rsquo;s MIT-licensed agent-skills collection (<a href="https://github.com/techczech/dominiks-agent-skills" target="_blank" rel="noopener">github.com/techczech/dominiks-agent-skills</a>); the bundle ships with a <code>LICENSE</code> and full attribution. The other four are the instructor&rsquo;s own.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;"><strong>Subagents</strong> add a second move. For a bounded job, Claude Code can spawn a separate, focused agent, and the most useful research application is verification. After the main agent has produced an analysis, you can have an independent subagent check it: re-derive the result from the raw data, look for the errors the first agent might have made, and report disagreements. This is the Week&nbsp;9 adversarial-verification idea made operational: a second pair of eyes that does not share the first agent&#39;s assumptions.</p>

  <div class="info-box">
    <h4>&#128270; A note on trust</h4>
    <p>A verification subagent is genuinely useful, but it is not magic: it is another instance of the same kind of system, and it can share the same blind spots. Treat it as one more screen, not as a guarantee, just as Week&nbsp;9 said of any single check. The human who reads the disagreements and decides what they mean is still you.</p>
  </div>

  <p style="color: #555; line-height: 1.75; margin-top: 25px; margin-bottom: 15px;"><strong>Coming up in B.3:</strong> we put all of it together: a full analysis of the Berg River data from messy files to a result a stranger could reproduce, then how to verify agentic work honestly, and why the reproducible folder turns out to be the best research-disclosure you can offer.</p>
"""


# ===========================================================================
# Lesson B.3 — The Reproducible Workflow, End to End
# ===========================================================================

SL_B3_BODY = """
  <div class="intro-text">
    <h2>&#127919; What We&#39;ll Cover</h2>
    <p>Everything so far has been apparatus. This page runs it for real: a complete analysis of the messy Berg River data, from the first inspection to a result and a folder that someone else could open and reproduce. Then the two things that keep it honest, verifying work an agent did largely on its own, and disclosing what the AI actually did, where we find that the reproducible folder is itself the best disclosure you can give.</p>
  </div>

  <h2 class="section-title">&#128257; Git as a Reproducibility Trace</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">One piece of the structure deserves a word before the worked example, because it is the part most researchers skip. <strong>Git</strong>, the version-control system, records the state of your project over time. Each commit is a labelled snapshot; the history is a record of how the work actually evolved. You do not need to become a software engineer to benefit: even committing at a few milestones (&ldquo;raw data inventoried,&rdquo; &ldquo;cleaning done,&rdquo; &ldquo;analysis complete&rdquo;) gives you a trace that says what the project looked like at each stage, and lets you see exactly what changed between them.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">Claude Code can do the Git work for you, initialising the repository, showing you what changed, committing with a message, so the mechanics are not a barrier. What matters is the habit of using the history as a <em>research record</em>, not just a backup: a commit message like &ldquo;halved upstream counts (double-counting fault, per field note); excluded contaminated D-03&rdquo; turns the version history into a narrated account of your decisions. Used this way, Git is reproducibility infrastructure, not a developer&#39;s indulgence.</p>

  <h2 class="section-title">&#128300; A Worked Reproducible Analysis</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Here is the Berg River study, start to finish, with the discipline of the previous pages applied. The dataset is the same deliberately-messy archive from Lesson&nbsp;A.3, downloadable below, and it has real problems planted in it: inconsistent column names, a systematic counting fault at one site, a contaminated outlier, missing values, and field notes that explain anomalies the spreadsheets don&rsquo;t. The structure turns that mess into something inspectable, and one of the corrections along the way decides the answer.</p>

  <ol class="step-list">
    <li><strong>Put the <code>CLAUDE.md</code> in place.</strong> The research-habits template from B.2 goes in the project root before anything else, so every rule (don&#39;t touch <code>data/raw/</code>, log decisions, don&#39;t guess) is active from the first action.</li>
    <li><strong>Inspect and inventory.</strong> In plan mode, the agent reads every raw file and writes <code>docs/data-inventory.md</code>: the columns (and the fact that the three site files name them differently), the units, the row counts, the missing values, and the anomalies. Among them: upstream counts that sit suspiciously close to the town&rsquo;s (surprising for a site <em>above</em> the town), and one downstream value far higher than its neighbours. The <code>field-notes.md</code> file explains both: the upstream counter double-counted all season, and the high downstream sample (D-03) was contaminated and should be discarded.</li>
    <li><strong>Pre-register the question.</strong> Before running the comparison, the prediction and decision rule from B.2 go into <code>pre-registrations/</code> and are committed. The standard is set while there is nothing to defend.</li>
    <li><strong>Plan the analysis; you review it.</strong> Still in plan mode, the agent proposes the cleaning and analysis steps. You read the plan, the checkpoint, and approve it before a single file is written.</li>
    <li><strong>Clean, and log every decision.</strong> The agent writes a cleaning script to <code>scripts/</code> that harmonises the column names, <strong>halves the upstream counts</strong> because the field notes record that the upstream counter double-counted all season, excludes the contaminated D-03, and handles the missing values by the pre-registered rule. <em>Each of these choices is appended to <code>notes/decision-log.md</code>, dated, with its reason and its source.</em> The raw files are never touched; the cleaned data lands in <code>data/processed/</code>. The upstream halving is the decision that changes the answer.</li>
    <li><strong>Run the analysis to a committed log.</strong> The analysis script runs the pre-registered Mann-Whitney test, prints its result to <code>outputs/analysis_run.log</code> (committed), and saves the figure and summary table to <code>outputs/</code>.</li>
    <li><strong>Record assumptions and uncertainty.</strong> The agent notes what it assumed and what remains uncertain (the small sample after exclusions, the reliance on a single field note for the upstream correction that drives the result) rather than presenting a clean result as if nothing were in doubt.</li>
    <li><strong>Commit.</strong> A Git commit snapshots the whole state, with a message that narrates the decisions.</li>
  </ol>

  <div class="case-study">
    <h4>&#129510; The test that matters: hand it to a stranger</h4>
    <p>Now the question reproducibility actually asks. Give the finished folder to someone who was not there. Can they reconstruct what happened? Yes, and not because they trust you: because the evidence is all present. The untouched raw data, the script that transforms it, the decision log explaining every judgement call (why the upstream counts were halved, why D-03 was dropped), the pre-registration showing the standard was set in advance, the outputs, and the run log proving what was executed. They can re-run the script and get the same result, and they can <em>disagree</em> with a decision because they can see it.</p>
    <p>The decision log is what carries the weight here. Without the upstream correction, if a hurried researcher never opened the field notes, this same analysis concludes that the town has <em>no</em> measurable effect: town and upstream read almost identically (a median difference of 2 particles/L, not remotely significant). With the correction, the town is clearly and significantly higher (a difference of 36, p&nbsp;&asymp;&nbsp;0.00002). One logged decision, sourced to a single field note, is the entire difference between the right answer and the wrong one. A reader of the folder can see exactly where the result turns; a chat transcript would have buried it.</p>
    <p>Contrast the same analysis done in a chat window. The model gives you the same answer, perhaps in the same minute. But the cleaning decisions are scattered through a conversation you will lose; the upstream halving is a thing the model did somewhere in the middle that nobody recorded; and next month there is no folder to hand anyone, only a number you once obtained and can no longer account for. Same model, same answer, wholly different research.</p>
  </div>

  <div class="resource-placeholder">
    <h4>&#128229; Download: the Berg River sample archive</h4>
    <p>The deliberately-messy starting files (the three inconsistent CSVs with their planted errors, the contradicting field notes, the stale README, and the metadata) so you can run this whole workflow yourself. <a href="files/berg-river-microplastics.zip">berg-river-microplastics.zip</a></p>
  </div>

  <div class="resource-placeholder">
    <h4>&#9989; Download: the worked solution (model answer)</h4>
    <p>The completed, reproducible folder: a filled <code>CLAUDE.md</code>, the pre-registration, the data inventory, the cleaning-and-analysis script, the decision log, the processed data, and the outputs (summary table, run log, and a figure). Running <code>python3 scripts/analyse.py</code> regenerates every output from the raw data, so you can watch the whole chain work and confirm the result for yourself. Do the exercise first; reach for this when you want to check your structure against a model answer. <a href="files/berg-river-microplastics-worked-solution.zip">berg-river-microplastics-worked-solution.zip</a></p>
  </div>

  <h2 class="section-title">&#128270; Verifying Agentic Work</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">When the agent runs for an hour and makes a hundred changes you did not watch, the instinct is to inspect each one, to read every diff as it happens. That does not scale, and pretending it does is the fastest route to a false sense of safety. The volume <em>is</em> the problem: when so much is changing all the time, there often isn&#39;t a chance to check each change, and any carefulness that depends on watching every one will quietly fail. So the move is to take verification <em>off</em> the per-change axis. Don&#39;t try to catch every mistake as it happens; instead make mistakes survivable, encode what must stay true so a machine checks it, and verify the few things that actually matter. Week&nbsp;9&#39;s protocols and Week&nbsp;10&#39;s Princeton reliability finding (<a href="https://arxiv.org/abs/2602.16666" target="_blank" rel="noopener">Rabanser et&nbsp;al., 2026</a>) still bite, since the burden is real and it grows, but the response is to automate and target verification, not to watch harder.</p>

  <div class="card-grid">
    <div class="card">
      <h3>1. Make mistakes recoverable</h3>
      <p>With <code>data/raw/</code> read-only, everything regenerable from raw plus scripts, and all of it under Git, any bad change can be rolled back and any output rebuilt. You are no longer reviewing to prevent disaster, since disaster is structurally off the table, so you can safely <em>not</em> watch every step, and find errors later, in batch.</p>
    </div>
    <div class="card">
      <h3>2. Automate the checks</h3>
      <p>Write down what must stay true (row counts didn&#39;t drop, values stay in physical range, a known sub-result still holds) and have the agent assert it after changes. A Claude Code <em>hook</em> can run your check script automatically after every edit, so a silently-dropped column trips an assertion with no diff-reading at all. You read a one-line pass or fail, not the change.</p>
    </div>
    <div class="card">
      <h3>3. Verify the result, not every step</h3>
      <p>You cannot check every edit, but you can check the end against ground truth: re-derive the one number that matters, trace a few output values back to the raw data by hand, sanity-check against what you know of the domain. A hundred edits collapse into a handful of checks on the thing you actually care about.</p>
    </div>
    <div class="card">
      <h3>4. Let the decision log choose your diffs</h3>
      <p>You don&#39;t read every diff; you read the consequential ones. The &ldquo;log every consequential decision&rdquo; rule means the agent surfaces the handful that mattered (halved the double-counted upstream counts; excluded the contaminated D-03); those are the few worth your eyes, and the boilerplate you let go. The log is a high-signal substitute for the full diff.</p>
    </div>
  </div>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">These layers catch different failures, and it helps to see which catches which. A <em>wrong-direction</em> failure, the agent confidently pursuing the wrong goal because it inferred the wrong intent and taking you on a tangent for days, is invisible to any amount of diff-reading, because no single change is wrong; the <em>question</em> is wrong. That is what the pre-registration <em>gates</em> from B.2 are for: a closed gate stops the tangent early. A <em>quiet-correctness</em> failure, a dropped column or a plausible default you didn&#39;t notice, is what the automated assertions catch. And reviewing at the <em>checkpoint</em> (the commit boundary) rather than at every keystroke is how human review stays in the loop without becoming a full-time job. Verification scales when it is layered, not when it is heroic.</p>

  <div class="warning-box">
    <h4>&#9888;&#65039; What stays human</h4>
    <p>The structure verifies the <em>process</em>; it does not verify the <em>judgement</em>. Is this the right analysis for the question? Does the result make physical sense for a river? Is the effect real or an artefact of the small sample after exclusions? Those are research judgements, and no amount of logging makes them the agent&#39;s job. The Week&nbsp;7 silent-error problem and the Week&nbsp;9 plausible-but-wrong problem do not disappear because the work is well-documented: a beautifully reproducible analysis can still be reproducibly wrong. And there is a cost to all of this: tokens, time, and the genuine review effort every agentic result demands. Budget for it.</p>
  </div>

  <div class="instructor-box">
    <h4>&#128100; From the instructor&#39;s own practice</h4>
    <p>&ldquo;In my earlier workflows I could go off on tangents for days, sometimes weeks, thinking that something was interesting, when in fact we were just chasing a bug in another paper. In this case the agent thought that the bug-chasing was the interesting thing we were trying to do, and I didn&rsquo;t have the right checks in place to understand that that&rsquo;s what it thought. No amount of looking at individual changes would have caught that: nothing was wrong with any one line; the whole direction was wrong.&rdquo;</p>
    <p>&ldquo;I&rsquo;ve had lots of smaller errors too, and the genuine issue is that when so much is changing all the time, you often can&rsquo;t check each change as it happens (as you wouldn&rsquo;t if you were supervising a student). So I&rsquo;ve stopped trying to be careful by watching everything. The carefulness has to live somewhere else. It&rsquo;s in the gates I set at the start so a tangent gets stopped early, in keeping the structure so that any mistake can be undone, and in checking the things that actually matter rather than every step along the way. I&rsquo;m still trying to figure out how to do this well at the volume the tools now make possible.&rdquo;</p>
  </div>

  <h2 class="section-title">&#128196; Disclosure: The Reproducible Folder Is the Disclosure</h2>

  <p style="color: #555; font-size: 1.05em; margin-bottom: 20px; line-height: 1.8;">Week&nbsp;4 and Week&nbsp;11.3 asked you to disclose your AI use. Week&nbsp;11.3 also delivered the bracing finding that, against roughly 70% of journals having an AI policy, only about 0.1% of papers actually disclose (<a href="https://doi.org/10.1073/pnas.2526734123" target="_blank" rel="noopener">He &amp; Bu, 2026, PNAS</a>). Most disclosure, where it happens at all, is a vague sentence: &ldquo;AI tools were used in the preparation of this work.&rdquo; That sentence tells a reader almost nothing.</p>

  <p style="color: #555; line-height: 1.75; margin-bottom: 15px;">A reproducible project folder flips the problem. You do not need a sentence that gestures at what the AI did, because the folder <em>shows</em> it: the <code>CLAUDE.md</code> states the rules the agent worked under; the decision log records every judgement and who made it; the scripts are the method; the Git history is the sequence of events; the pre-registration proves the standard predated the result. The honest answer to &ldquo;what did the AI do, and what did you decide?&rdquo; is &ldquo;here is the folder.&rdquo; That is what good disclosure actually looks like, and it is a higher standard than almost any journal currently asks for.</p>

  <div class="info-box">
    <h4>&#127891; The capstone connection</h4>
    <p>If you took this track alongside the course, the Week&nbsp;12 capstone is where it can land: a reproducible project folder is the natural form for the concrete piece of work the capstone asks you to commit to. You do more than argue that you would use AI responsibly in your research; you show the structure in which you would.</p>
  </div>

  <div class="highlight-box">
    <h3>&#9989; What to take from the Advanced Track</h3>
    <p>Claude Code is a model with hands in your project folder, and the work lives in files, not in the chat. Reproducibility is a different goal from verification, and the agent can be instructed to serve it, logging decisions, keeping raw data sacred, holding you to a pre-registration, better than unaided human discipline usually manages.</p>
    <p>The <code>CLAUDE.md</code> research-habits template is where the course&#39;s integrity becomes a rule the agent follows. Pre-registration is where you refuse to fool yourself. The reproducible folder is where verification, disclosure, and trust all meet: the same folder answers all three.</p>
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
        "header_subtitle": "An agent that lives in your project folder, where the model is the smallest part of what works for you",
        "body": SL_A1_BODY,
    },
    {
        "filename": "Cost Access and the Disposition Shift.html",
        "title": "Advanced A.2 - Cost, Access, and the Disposition Shift",
        "badge": "Advanced Track &bull; Lesson A &bull; 2 of 3",
        "header_emoji": "&#9878;&#65039;",  # balance scale
        "header_title": "Cost, Access, and the Disposition Shift",
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
        "header_subtitle": "A full analysis from messy data to a result a stranger could reproduce, then verifying it, and disclosing it",
        "body": SL_B3_BODY,
    },
]


TOC_HTML = """<html><head><meta http-equiv="'Content-Type'" content="'text/html;charset=utf-8'" /><title>MAM5020F 2026 | Gen AI for Research - Advanced Track: Agentic Research with Claude Code</title></head><body>
<div style="background: #003A70; padding: 8px 20px; text-align: center;"><a href="../index.html" style="color: white; text-decoration: none; font-size: 0.85em;">&#8592; Back to Contents</a></div><table cellpadding=0 cellspacing=0 border=0 width=100%><tr><td colspan=3>&nbsp;</td></tr><tr><td valign="top" width="100%"><font class="title"><strong>Advanced Track &mdash; Beyond the Free Tier: Agentic Research with Claude Code</strong></font><br><p style='margin-left: 25px; margin-top: 20px; color: #003A70; font-weight: bold; font-size: 1.1em;'>Lesson A &mdash; Claude Code as a Research Environment</p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Claude Code as a Research Environment.html" />A.1 What Claude Code Actually Is</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Cost Access and the Disposition Shift.html" />A.2 Cost, Access, and the Disposition Shift</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="First Contact and the Control Surface.html" />A.3 First Contact and the Control Surface</a></p><p style='margin-left: 25px; margin-top: 24px; color: #003A70; font-weight: bold; font-size: 1.1em;'>Lesson B &mdash; Reproducible Research Workflows</p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Reproducibility and the Project Folder.html" />B.1 Reproducibility, and the Reproducible Project Folder</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="Encoding Good Habits - CLAUDE.md Pre-registration and Skills.html" />B.2 Encoding Good Habits: CLAUDE.md, Pre-registration, and Skills</a></p><p class='d2l' style=' margin-left: 40px'><a target="_blank" href="The Reproducible Workflow End to End.html" />B.3 The Reproducible Workflow, End to End</a></p></td></tr></table><footer style="background: #f9f9f9; margin-top: 40px; padding: 22px 30px; text-align: center; color: #888; font-size: 0.85em; border-top: 1px solid #eee; font-family: 'Lato', 'Lucida Sans Unicode', 'Lucida Grande', sans-serif;">
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
