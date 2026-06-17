# Advanced Track — Beyond the Free Tier: Agentic Research with Claude Code

**Status:** Design document for sign-off. No HTML built yet.
**Decided with instructor:** fictional core worked example + instructor's real practice as framing; *fully Claude-Code-specific*; design both lessons fully on paper before building.

---

## 1. Positioning and the honest gate

These are **not** Weeks 13–14. They are a clearly-marked **Advanced Track**, **folded in after Week 12** in the site sequence and the Prev/Next chain, but kept distinct from the numbered weeks because adding paid-tool weeks to the core sequence would quietly break the course's deliberate free-tier-first equity stance (the Week 10 "why free is the whole game" argument; the African-context thread in 11.4). It comes *after* the capstone deliberately: a student finishes the assessed core, then optionally continues into the advanced material.

Every page in the track opens with the same honest gate:

> *This track goes beyond the free tier. It requires a paid Claude subscription and comfort with a terminal. It is genuinely optional and deliberately outside the free-tier core of this course. What follows is the honest case for whether it is worth it for you — including what you can and cannot approximate without paying, and who this is and is not for.*

The equity tension is **named, not hidden**, throughout — consistent with the calibrated voice. This is the one place in the whole course where we recommend a paid tool, and we say so plainly.

### Framing decision: fully Claude-Code-specific

Per the instructor's choice, the track leans all the way into Claude Code specifics — the `claude` CLI, `CLAUDE.md`, `/init`, plan mode, permission modes, slash commands, Skills (`.claude/skills/`), subagents, MCP, Git integration. We accept that this dates faster than a tool-general treatment and reads slightly more like a single-product guide. We mitigate the rot risk only by dating the snapshot ("as of mid-2026…") and pointing to the official docs for anything that changes (pricing, install, exact command syntax), rather than reproducing it.

### Worked-example decision: hybrid

The **hands-on spine** runs on a fictional dataset (below). The **framing sections** — "what this is actually like," "the disposition shift," "what still needs human review" — draw on the instructor's real Claude Code research practice, the way 11.1 draws on Mineault and Mollick. Those slots are marked **[INSTRUCTOR INPUT]** in the design; they stay generic until the instructor supplies 3–5 real observations.

---

## 2. The running fictional example

**The Berg River microplastics study** — a fictional postgraduate project, legible across the science faculty and grounded in a South African setting (consistent with the course's local vantage).

A student has collected water samples and counted microplastic particles at three sites on the Berg River — upstream of a town, in the town, and downstream — across a sampling season. The starting archive is deliberately *messy*:

```
berg-river-microplastics/
  data/raw/
    site-upstream.csv          # inconsistent column names vs the others
    site_town.csv              # mixed date formats, two obvious data-entry errors
    downstream-final-v2.csv    # a confusing name; is there a v1?
    sampling-metadata.xlsx     # site coordinates, sampling dates, methods
    field-notes.md             # free-text notes, some contradicting the CSVs
  literature-notes.md          # half-organised reading notes
  README-old.txt               # stale, refers to files that no longer exist
```

The reproducibility stakes are real and concrete: which readings to exclude as errors, how to handle missing values, which unit convention, which statistical test, how to treat the contradiction between the field notes and the CSVs. **Every one of those is a decision a replicator must be able to inspect.** That is the whole point.

The example threads through both lessons: Lesson A *inspects* the messy archive; Lesson B *builds the reproducible analysis* from it. Students are told to read "microplastic counts" as "your own measurements, whatever they are."

This fictional dataset becomes a **downloadable artifact** (like Dominik's `workshop-sample-files.zip`), so the hands-on activities are real.

---

## 3. Lesson A — Claude Code as a Research Environment

*The "what / why / how to drive it" lesson. Proposed as 3 sub-lesson pages.*

### A.1 — What Claude Code actually is (and isn't)

- **Definition.** A terminal-based agentic tool that operates inside your real project folder. Not a chat window — a process that reads your files, runs commands and code, edits files, uses Git, and can run autonomously for extended stretches.
- **The model-vs-harness distinction made physical** (direct callback to Week 10.1, "the harness is the product"). In chat, the model is all you get. In Claude Code, the model is the *smallest* part of what's working for you: the CLI, your file system, the shell, Git, Skills, subagents, and MCP servers are the harness. *"You are not talking to a smarter chatbot. You are driving a different kind of machine."*
- **The research-relevant capabilities, named:** reads/writes files in the project; runs shell commands and code; uses Git; loads standing instructions (`CLAUDE.md`) every session; runs reusable Skills; spawns subagents; connects to external data/tools via MCP; plans before acting (plan mode); asks permission before changing things (permission modes).
- **Calibration.** This is "AI as a substantive collaborator" (11.1) made operational — but every capability comes with a verification cost we pay down across the lesson. Not an advertisement.

### A.2 — Why it's categorically different from chat: "the chat is not the archive"

- **The contrast.** Chat: you paste context in, it answers, the work lives in a conversation that you will lose. Claude Code: the work lives in your files — durable, inspectable, repeatable.
- **The organising principle, stated once and carried through both lessons:** *the chat is not the archive.* Save sources, notes, instructions, scripts, outputs, and decisions into **files**, not the thread. The local project folder is the unit of reproducible work.
- **Honest scope.** Chat is still the right tool for many things — quick questions, brainstorming, one-off drafts. Claude Code is for *project* work where durability and repeatability matter. We are not telling you to abandon chat.
- This section is the bridge to Lesson B (reproducibility).

### A.3 — The honest cost and access picture (the equity gate, in depth)

- **Cost.** Subscription tiers and rough monthly cost, framed in ranges and dated ("as of mid-2026, expect roughly …; check the current pricing page"), never hard-coded to a number that rots. Token costs for heavy use noted honestly.
- **The terminal learning curve.** You need to be comfortable with — or willing to learn — a command line. This is a real barrier for some researchers and we say so.
- **The equity tension, named.** This is exactly the free-vs-paid divide that Weeks 10 and 11.4 are built around. For a well-funded lab the cost is trivial; for many African postgraduates it is a genuine barrier. The course's free-tier-first stance is deliberate; this track is the explicit, signposted exception, not a reversal.
- **What's approximable for free.** Claude.ai Projects plus manual file discipline gets you *part* of the reproducibility benefit — you can keep a project folder and paste files in. You lose the autonomous file operations, the running of code, the Git integration, the Skills/subagents. We are honest about the size of that gap.

### A.4 — First contact: the messy research archive

- **Setup.** Light-touch only — install from the official Claude Code docs (linked), don't reproduce steps that go stale.
- **The adapted messy-folder first task**, fully Claude-Code-specific. Open the Berg River archive, run `claude`, and use **plan mode** so the first interaction is read-only:
  > *Inspect this folder before changing anything. Tell me what's here, what each file appears to contain, what you should not edit, and what you'd recommend doing first. Do not move, rename, or edit anything yet.*
- **What to watch:** which files it actually reads; whether it separates evidence from inference; whether it proposes changes before making them; the **permission prompts** (Claude Code asks before edits by default); what an allowlist would change.
- **The debrief prompt:** *"What did you inspect, what did you infer, and what would you change only after my approval?"*
- **Claude-Code specifics introduced here:** permission modes, plan mode (read-only planning), the allowlist concept, the sandbox boundary.

### A.5 — The disposition shift: you are managing an agent now

- **The shift.** You are no longer prompting-and-reading; you are delegating multi-step work and verifying it. The skill is judgement: what to delegate, where to put checkpoints, how to verify.
- **Callbacks.** Mollick's "wizards" and "managing AIs" (11.1); the Week 10 Princeton reliability finding (accuracy rose, reliability didn't); the Week 9 verification disposition. *An agent that runs for an hour can do an hour of wrong work.*
- **[INSTRUCTOR INPUT] — "what it's actually like."** The honest, first-person account of using Claude Code for real research: where it saved weeks, where it went confidently wrong, the moment you learned to checkpoint, the habits you now refuse to skip. This is the practitioner-authenticity slot (the Mineault/Mollick role, but it's *you*).
- **The two-researchers point** (from 11.1): the tool's value depends almost entirely on the practice you bring to it. Same tool, two researchers, wildly different results.

### A.6 — `CLAUDE.md`: the control surface

- **What it is.** The project's standing instructions, loaded into every session. The single most important file for steering the agent — the thing that makes the next session behave like the last one.
- **`/init`** generates a starter `CLAUDE.md` from your project.
- This section is deliberately a *bridge*: a light example here, because in Lesson B the `CLAUDE.md` becomes the **reproducibility-enforcement device** — the place where good research habits become machine-readable rules.

---

## 4. Lesson B — Reproducible Research Workflows with Claude Code

*The payoff lesson. Proposed as 3 sub-lesson pages.*

### B.1 — Reproducibility is not verification

- **The distinction, sharply drawn.** Verification (Week 9) asks: *is this output correct?* Reproducibility asks: *can someone else inspect and repeat what I did?* Siblings, not the same thing. The course has taught the first thoroughly; this lesson adds the second.
- **Why agentic work cuts both ways.** Harder: the agent does a lot autonomously and the steps can be opaque (Mollick's "wizard" opacity — competence and opacity rise together). Easier: everything can be captured in files automatically — the agent can be instructed to document its own decisions as it goes.
- **The lesson's claim.** Used with discipline, Claude Code can produce research that is *more* reproducible than typical manual work — because the agent can be told to log as it works, and never tires of doing so.

### B.2 — The project folder as the unit of reproducible work

- **The scaffolding, Claude-Code-idiomatic:**
  - `data/raw/` — immutable raw data (the `CLAUDE.md` forbids editing it)
  - `data/processed/` — derived data, regenerable from raw + scripts
  - `scripts/` — the code, preserved
  - `outputs/` — figures, tables, reports
  - `notes/decision-log.md` — every consequential choice, dated, with rationale
  - `docs/data-inventory.md` — what the data actually is
  - `CLAUDE.md` — the standing instructions
  - Git — the version trace
- **Why each exists:** a stranger, or future-you, can open the folder and reconstruct what happened. Shown concretely on the Berg River example.

### B.3 — The `CLAUDE.md` research-habits template (the headline artifact)

The single most valuable thing the track produces: a downloadable `CLAUDE.md` that turns good research practice into machine-readable rules. Adapted from Dominik Lukeš's `AGENTS.md` into Claude-Code idiom (with attribution, CC BY):

- Read files before proposing changes.
- Never modify anything in `data/raw/`.
- Use plan mode and explain intended changes before making anything consequential.
- When summarising or analysing, name which files you used.
- Record uncertainty instead of inventing — never fill a gap with a plausible guess.
- Save reusable code in `scripts/`, generated outputs in `outputs/`.
- Log every consequential decision in `notes/decision-log.md`, dated, with the reason.
- Before reporting a task done, show me the diff.

**The pedagogical move:** walk through *why each rule operationalises a theme the course already taught.* "Never invent" = the Week 9 hallucination lesson. "Name your sources" = the Week 5 citation-integrity lesson. "Log decisions" = reproducibility. "Show me the diff" = verification. The course's entire integrity-and-verification thread collapses into one copy-pasteable file.

### B.4 — Skills and subagents: packaging reproducible practice

- **Skills** (`.claude/skills/<name>/SKILL.md`): a reusable workflow that travels across projects. Real examples shown: a `data-inventory` skill, a `reproducible-analysis` skill, a `source-grounded-summary` skill. Show an actual `SKILL.md` (YAML frontmatter `name` + `description`, concise instructions, optional `scripts/`/`references/`/`assets/`).
- **Subagents** (the Task/Agent tool): spawning a specialised agent for a bounded job — e.g., an independent "verify this analysis" subagent that checks the main agent's work. Connects to the course's adversarial-verification ideas.
- **The reproducibility payoff:** a Skill is a *tested, repeatable* research procedure — the opposite of ad-hoc prompting. You write it once, inspect it, and reuse it across projects with the same behaviour every time.

### B.5 — Git as a reproducibility trace

- **The concept only**, not a Git tutorial. Each commit is a snapshot of project state; the history is a record of how the research evolved. Versioned state *is* a reproducibility record.
- Claude Code can do the Git work (commit, diff, log) — you direct it.
- **Honest note:** Git has a learning curve; even minimal use (a commit at each milestone) gives you a usable trace. We are not asking you to become a software engineer.

### B.6 — A worked reproducible analysis, end to end

The Berg River analysis, start to finish, on the page:

1. `CLAUDE.md` in place (the research-habits template).
2. Inspect raw data; agent drafts `docs/data-inventory.md`.
3. Agent proposes an analysis plan in **plan mode** — you review *before* it runs anything.
4. It writes the cleaning + analysis script to `scripts/`, and logs the cleaning decisions (which outliers excluded, how missing values handled, the field-notes-vs-CSV contradiction resolved) to `notes/decision-log.md`.
5. It runs the analysis and saves outputs (a figure, a table) to `outputs/`.
6. It records assumptions and uncertainties explicitly.
7. Git commit.
8. **The test:** hand the folder to a stranger — can they reconstruct what happened? Yes, because raw data + script + decision log + outputs are all present and inspectable.

**The contrast that makes the point:** the same analysis done in chat lives in a conversation that's gone next week, with the cleaning decisions invisible and unrecoverable. Same model, same answer — utterly different reproducibility.

### B.7 — Verifying agentic work

- **Why it's harder and more important here.** The agent runs autonomously; the Week 9 protocols and the Week 10 Princeton reliability finding apply with more force, not less.
- **Concrete tactics:** plan mode before consequential steps; checkpoint reviews; reading the diff before accepting; treating the decision log as a verification surface; an independent verification subagent; re-running the script yourself; spot-checking outputs against the raw data.
- **The honest limits.** What still needs human review: the *research judgement* — is this the right analysis? does the result make physical sense? The failure modes: the Week 7 silent-error problem, the Week 9 plausible-but-wrong problem. The cost: tokens, time, attention, review effort.
- **[INSTRUCTOR INPUT]** — a real "this is where it went wrong and how I caught it" story.

### B.8 — Disclosure: the reproducible folder *is* the disclosure

- **The flip.** Instead of a vague "AI was used in this research" statement (Week 4 transparency; Week 11.3 disclosure norms), you have an inspectable record: the decision log, the scripts, the `CLAUDE.md`, the Git history show exactly what the agent did and what you decided.
- **Connection to 11.3's "0.1% disclose" finding:** this is what good disclosure actually looks like — not a sentence, but a folder.
- **The capstone hook:** the Week 12 capstone could *optionally* ask for a reproducible project structure, so the track isn't theory — it lands in the assessed work for students who take it.

---

## 5. Downloadable artifacts

1. **The `CLAUDE.md` research-habits template** (the headline; attributed adaptation of Lukeš's `AGENTS.md`, CC BY).
2. **A starter folder scaffold** (`data/raw/`, `data/processed/`, `scripts/`, `outputs/`, `notes/decision-log.md`, `docs/data-inventory.md`, `CLAUDE.md`).
3. **Example `SKILL.md` files** (`data-inventory`, `reproducible-analysis`, `source-grounded-summary`).
4. **The fictional Berg River sample dataset** (deliberately messy, zipped, for the hands-on).

---

## 6. How it connects to the existing course

- **Week 7** (data, code, computation) — the prerequisite; this is its advanced continuation.
- **Week 9** (verification) and **Week 10** (agents, harness, Princeton reliability) — the conceptual backbone.
- **Week 11.1** (AI as substantive collaborator; Mollick's wizards / managing AIs) — the framing.
- **Week 4** and **Week 11.3** (integrity, disclosure) — the reproducible folder as the disclosure mechanism.
- **Week 12** (capstone) — the optional reproducible-structure hook.

This track is a *synthesis* of the agentic + verification + integrity threads, made concrete with one real tool. It assumes those weeks are done; it does not re-teach them.

---

## 7. On-voice guardrails (the things that keep it from becoming an advert)

- **Calibration first.** Every capability claim bounded; honest about cost, failure modes, and the two-researchers-different-results point.
- **Reproducibility is the point; agentic capability is just the means.** "Here's how to make agentic research inspectable and repeatable," never "look what Claude Code can do."
- **Builds on, doesn't repeat.** Synthesis, not introduction.
- **Equity tension named, not hidden.** The gate up front; free-tier approximations flagged throughout.

---

## 8. Deliberately out of scope

Cloudflare/Wrangler publishing; a full Git tutorial; install walkthroughs that rot; anything Codex-specific. The workshop's tooling-maximalism doesn't fit the course; the reproducibility discipline underneath it does.

---

## 9. Open questions for the instructor (needed before / during build)

1. **[INSTRUCTOR INPUT] slots.** Sections A.5 and B.7 (and lighter touches elsewhere) need 3–5 real observations from your Claude Code research practice — the "what it's actually like," the "where it went wrong and how I caught it." Without these the framing stays generic. Can be supplied as rough notes; I'll shape them.
2. **Page structure.** Proposed: each Lesson = 3 sub-lesson pages (6 pages total), matching the course's multi-page-week pattern and keeping each page to a readable chapter length. Alternative: one long deep page per lesson. Recommend the 3+3 split.
3. **Site placement — DECIDED.** A new **Advanced Track** block in `docs/index.html`, placed after Week 12, with the honest gate as its intro. **Folded into the Prev/Next chain after the Week 12 capstone** (a student finishes the core, then optionally continues). Still visually marked as a distinct, optional advanced track, not as numbered weeks.
4. **Build approach.** A new `build_advanced.py` generator mirroring `build_week11.py` (recommended, for consistency and rebuildability), versus hand-built pages.
5. **Discussion Questions.** Should the Advanced Track get its own Discussion Questions page in the established format? (Recommend: yes, one page covering both lessons.)
6. **SCORM — DEFERRED.** Not building the SCORM package for the Advanced Track for now (instructor's call). Revisit later if the track should travel to other institutions.

---

## 10. Proposed build sequence (once design is signed off)

1. Build **Lesson A** (3 pages) to the course's depth → instructor reviews tone/pitch.
2. Incorporate the **[INSTRUCTOR INPUT]** framing.
3. Build **Lesson B** (3 pages) + the downloadable artifacts.
4. Add the **Advanced Track block** to `docs/index.html`; wire nav.
5. Add the **Discussion Questions** page.
6. Verify-references pass; HTML-balance validation; commit + push.

---

## 11. Real-practice patterns to fold in (anonymised from the instructor's own projects)

A read-only survey of ~13 of the instructor's real Claude Code research projects (RL experiments, ML emulation, materials ML, physics simulation, interpretability pipelines) surfaced a consistent, distinctive workflow. **These patterns are used as generic teaching material only** — every real name, number, finding, dataset, cluster detail, and collaborator attribution is treated as embargoed and invented from scratch for the fictional Berg River example. What's reusable is the *shape* of the practice, and it is noticeably more rigorous than the source workshop. It is the lesson's real differentiator.

### The distinctive spine: pre-registration of computational experiments

The single most teachable habit, and one that goes well beyond Dominik's workshop: **the prediction and the numeric decision rule are written and committed to a `pre-registrations/` file *before* any compute is spent**, amendments are themselves committed with reasons before new runs, and when a result contradicts the prediction the decision rule is applied and the refutation is recorded *straight* — not reframed into a flattering story. This directly operationalises the course's deepest themes (calibration; "is this interesting, not just publishable"; honesty over reflexive iteration) and connects to the instructor's existing `pre-register` and `convergence-check` skills. **Recommendation: make pre-registration a named section of Lesson B**, not just a passing mention — it is the strongest "your experience as framing" hook in the whole track.

### Recurring CLAUDE.md rules to seed the research-habits template (B.3)

Generic, non-sensitive rule-lines that recurred across projects — these enrich the headline template beyond the workshop's set:

- Treat upstream / vendored code as **read-only**; copy out before editing, never silently fork its semantics.
- Don't touch the heavy artifacts — no retraining; derived caches/results are regenerable and read-only to downstream steps.
- **The pre-registration is binding.** Don't tune on the headline metrics; don't reframe outcomes post hoc. If reality contradicts the prediction, apply the decision rule and say so.
- Document deviations; don't silently rescope. From→to changes are recorded with justification.
- Run scripts to a **committed log** (`… 2>&1 | tee <name>_run.log`); the log, not the figure, is the gold record.
- **Work from logs and printed tables, not screenshots** unless a visual is genuinely needed.
- Fix seeds and tolerances before running; new choices must be data-independent and recorded first.
- Don't bluff — state estimated confidence and explain uncertainty explicitly.
- Name canonical sources / cite prior art before claiming novelty.
- Optimise for clarity and reproducibility, not packaging; delete dead code rather than leaving shims.

### Framing observations for the [INSTRUCTOR INPUT] slots (A.5, B.7)

Honest, habit-level observations the instructor can speak to in first person (no findings, just practice):

1. **Pre-registration is a committed file, not an intention** — the prediction and decision rule precede the compute.
2. **Engineering state and research results live in separate documents** — a living `STATUS.md` / `SESSION_STATE.md` ("what's running, what's known, what's next") kept apart from a results doc.
3. **Commit messages are used as a research log** — they narrate the decision and record *refuted* hypotheses ("this was wrong", "gate failed"), not the diff.
4. **Raw / derived / vendored boundaries are enforced in writing**, not just intended.
5. **The committed run-log is the source of truth; figures are derived** — reason from tables, not images.
6. **Negative results are recorded straight, not reframed** — a clean documented STOP when a pre-registered gate fails.
7. **Per-project permission allowlists** (`.claude/settings.local.json`) tailored to the project's real needs, not blanket access.
8. **The discipline is a choice applied where it pays off** — the same researcher runs both heavily-scaffolded projects and bare results-dump folders. Honest, and worth saying in the lesson: scaffolding is proportionate to stakes, not a ritual.

### Worked-example structures to mirror (for B.2 and B.6)

Three real structures are the cleanest models for the fictional Berg River scaffold (mirror the shape, invent all content):

- **The "discipline as a system" model:** immutable pre-registration → living STATUS journal → distinct results doc → audit/review logs, with upstream code vendored read-only. Best overall.
- **The "directed data-flow" model:** `extract/` writes `cache/`; downstream steps only ever *read* `cache/` and write `results/`; one master `PLAN.md` as source of truth. Best for teaching raw-vs-derived separation.
- **The "production hygiene" model:** clean `src/`/`scripts/`/`tests/`/`docs/` split with an explicit maintained-vs-legacy distinction so new work never lands in historical code.

### Breadth of current use (second survey — the ten most-recent folders)

A second read-only survey of the ten most-recently-used folders broadened the picture beyond the heavily-scaffolded experiments, and produced the lesson's most important honest framing. Recent use spans: pre-registered computational experiments; a large document-analysis pipeline with evidence-integrity gating; teaching-material authoring with a deployed site; research-governance/admin; peer-review of others' manuscripts; and personal longitudinal tracking.

**The key teaching point — discipline is proportionate to stakes and longevity, not prestige.** The two experiment folders, the corpus-analysis folder, *and a personal fitness tracker* all carry heavy scaffolding (single-source-of-truth, append-only logs, a protocol the agent cannot skip) — because each is a record the researcher will need to trust months later. A one-off manuscript review gets a structured output file and nothing else. This defuses the lesson's biggest risk: it must NOT preach "always do all this heavy process." The honest message is **match the discipline to the stakes** — which is exactly the calibrated voice the course already uses.

Additional everyday patterns (present even when full reproducibility scaffolding is absent):

- **`CLAUDE.md` as institutional memory, not configuration** — mostly "a list of mistakes I refuse to make twice" (wrong interpreter, a stale-cache deployment trap, a data stream that lies). The instruction file stops the *next* session repeating errors.
- **An explicit "single source of truth" declaration** in almost every project (the `.tex`, the JSONL, the corpus DB) — derived views regenerated, never hand-edited.
- **A human-approval gate for anything externally consequential** — "present the draft, don't send", "commit/push only when asked", "all pending your approval" — written into nearly every project.
- **Not everything is a git repo.** When the canonical artefact lives elsewhere (a synced corpus, a separate code repo, a LaTeX source), the working folder is deliberately disposable and *said to be* so the agent doesn't treat scratch as precious.

**Five first-person framing seeds** (anonymisable; the instructor can adopt/adapt these near-verbatim for the A.5 / B.7 slots):

1. *"My scaffolding scales with stakes and longevity, not prestige. A computational experiment and my personal training log get the same discipline — single source of truth, append-only logs, a protocol the agent can't skip — because both are records I'll trust months later. A one-off review of a colleague's paper gets a structured output file and nothing else."*
2. *"For anything that runs more than once, my `CLAUDE.md` is mostly a list of mistakes I refuse to make twice. The instruction file is institutional memory, not configuration."*
3. *"I gate consequential actions behind a human. The agent drafts the review, the email, the commit — but 'pending your approval', 'present for copy-paste', 'push only when asked' is written into nearly every project."*
4. *"Not everything is a git repo. When the canonical artefact lives elsewhere, the working folder is deliberately disposable, and I say so explicitly."*
5. *"Before spending real compute I pre-register: I write down what 'interesting', 'boring-but-worth-knowing', and 'dead' each look like, and a decision rule — then I hold myself to it even when the result disappoints. The pre-reg is binding; outcomes don't get reframed after the fact."*

### Privacy guardrail for the build

When building: all worked-example content is fictional (the Berg River study). Real `CLAUDE.md` content, pre-registration thresholds, collaborator names, paper/venue references, dataset names, and HPC/cluster specifics from the instructor's projects are **never** quoted — only the generic rule-shapes above are reused. The second survey flagged specific folders as sensitive/identifiable — a research-ethics submission, a politically-sensitive treaty-corpus analysis with named external collaborators, a personal health/fitness tracker, an ops-runbook website folder with infrastructure secrets, and two folders concerning collaborators' unpublished manuscripts. **None of these is quoted or named in the course;** they inform only the abstract workflow patterns above.
