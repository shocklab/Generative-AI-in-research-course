---
name: course-freshness-check
description: >
  Run a deep freshness + accuracy re-verification of the MAM5020F course content
  and produce a dated findings report (and optionally a GitHub issue). Use this
  when the user asks to "check the course for updates", "what's gone stale",
  "run the freshness check", "monthly course review", or when invoked by the
  scheduled monthly routine. Read-only on content: it REPORTS, it does not edit
  lesson pages or push fixes.
---

# Course freshness check (MAM5020F)

Purpose: this course makes many fast-decaying claims — model versions, benchmark
SOTA numbers, the "Current Landscape" snapshot, the AI-policy landscape, dated
statistics, and live URLs. This skill re-verifies them against current reality
and produces a prioritised, source-cited findings report for the course owner to
review. **It never edits content or opens PRs that change `docs/` — the human
decides what to apply, via the normal review→PR flow.**

It is the scheduled-routine counterpart to a manual run: same procedure either way.

## Operating rules (read first)

1. **Report, don't edit.** Do not modify any lesson HTML, `Week N/` source, or
   `build_weekN.py`. The only file you may write is the report (see Output).
   Reasoning: live student content is governed by "docs/ is canonical, changes
   go through review" (see CLAUDE.md). A freshness bot proposes; the human disposes.
2. **`docs/` is the source of truth.** Audit the published `docs/week-*/*.html`
   (plus `docs/course-*` and `docs/index.html`). Amathuba is not reachable from a
   headless run and is downstream of `docs/` anyway.
3. **It is `2026` and beyond — always anchor "current" to today's real date** (use
   web search; do not assume the training cutoff). The course is explicitly written
   as dated snapshots, so the job is "what has changed since this was written?",
   not "rewrite to a fixed target".
4. **Respect deliberate historical/dated content.** Many citations are *meant* to
   be dated (e.g. "AlphaFold 3 (Nature, May 2024)" as a historical exemplar; the
   "Current Landscape (Month Year)" snapshot framing). Flag these as
   "intentionally dated — confirm, don't "correct"" rather than as errors. The
   course's own model-version genericisation rule (family names like "Claude
   (family)") is intentional; don't flag it.
5. **Verify before asserting — never hallucinate a citation or a "newer" fact.**
   Every claimed staleness or replacement must cite a real, fetched source. If you
   can't verify, mark it ⚠️ unverifiable, don't guess. (This is the same discipline
   as the `verify-references` skill; reuse it for any citation existence/metadata
   checks.)
6. **Calibrate (Real / Overclaimed / Aspirational).** When proposing a model/
   capability update, apply the course's own calibration frame — don't replace a
   carefully-bounded claim with a hypier one from a press release.

## Scope of a DEEP run

Cover all of these across Weeks 1–12 (+ course intro/orientation):

A. **Model & version currency.** Flagship model names/versions and their dated
   claims (e.g. Week 1 "Current Generative AI Landscape", Week 2 frontier box,
   Week 9 model cards/benchmark table). Are the named flagships still current?
   Have new ones shipped? Are "GA on <date>" / "preview" statuses still true?

B. **Benchmark SOTA & numbers.** SWE-bench Verified, FrontierMath, GPQA Diamond,
   MCP-Atlas, AIME, HLE, Codeforces, etc. — are the cited SOTA holders and scores
   still accurate? Has any benchmark saturated or been superseded?

C. **Dated statistics & studies.** E-waste tonnage/year, energy/water figures,
   foundry market share, disclosure-rate stats (He & Bu ~0.1%), policy-coverage
   percentages (Wang & Gong), etc. Check for newer editions/figures.

D. **Policy & institutional landscape (Weeks 3, 4, 11.3, 11.6).** Journal/funder/
   conference AI rules (NIH, NSF, UKRI, NeurIPS, Elsevier/Springer/Wiley/ACM/OUP),
   the South African NRF gap, the SA national AI policy saga, AU Continental AI
   Strategy phasing, the Africa Declaration / African AI Scientific Panel. These
   move fast — check for new editions, withdrawals, enactments.

E. **Citation re-verification (deep).** Re-confirm the higher-risk citations still
   resolve and are correctly attributed — especially recent (2025–2026) DOIs/arXiv
   IDs and any added since the last run. Watch for: retracted/updated papers, a
   preprint now formally published (update venue), broken/redirected DOIs.

F. **Link rot.** Scan every external `href` for dead/redirected links (HTTP
   status). Report 4xx/5xx and cross-host redirects. (CDN/licence links are fine.)

G. **Regressions / new content.** If new pages or claims were added since the last
   report, include them. Cross-check that prior reports' accepted fixes actually
   landed.

## Procedure

1. **Establish "now".** Web-search the current date and a couple of "latest
   frontier model / latest benchmark leaderboard" queries to ground the run.
2. **Inventory.** List `docs/week-*/*.html` + `docs/course-*`. Extract every
   verifiable claim (model/version, benchmark+score, dated stat, policy fact,
   citation, external URL). A scripted pass (grep for years, "%", "SWE-bench",
   model names, `href=`, DOIs/arXiv) plus reading the high-churn pages
   (Week 1 Landscape, Week 9 trajectory, Week 11.3/11.6) is the fast path.
3. **Verify each** against current primary sources (web search + fetch). For a
   big run, fan out: one worker per week/dimension, then an adversarial pass that
   tries to *refute* each "this is stale" finding before it's reported (kills
   false positives — e.g. don't flag a deliberately-dated historical citation).
4. **Bucket & rate every finding:**
   - 🔴 **Wrong now** (factually incorrect as of today) ·
     🕰️ **Stale** (was right, now outdated) ·
     🔗 **Broken link** ·
     ⚠️ **Unverifiable** (couldn't confirm — needs human eyes) ·
     ✅ **Checked, still correct** (note the high-churn ones you confirmed) ·
     🟰 **Intentionally dated** (confirm it's still an apt historical example).
   - For each actionable item: exact page + quoted current text → proposed
     replacement + the source URL backing it.
5. **Do NOT apply.** Leave application to the human via PR.

## Output

1. **Report file:** write `freshness-reports/YYYY-MM.md` (create the dir if
   needed) with: a one-paragraph executive summary (how much drifted), counts by
   bucket, then the per-finding list (page · current text · proposed fix · source ·
   confidence). End with an explicit "examined and still correct" section so the
   reader knows coverage was real, and a "needs human judgement / unverifiable"
   section. Keep this file committed on a branch + PR (report only — no `docs/`
   edits in that PR).
2. **GitHub issue** (if `gh` is available and the run is the scheduled one, or the
   user asks): open an issue titled `Course freshness check — YYYY-MM` in
   `shocklab/Generative-AI-in-research-course`, body = the executive summary +
   the actionable findings (link to the report file/PR for full detail). Label it
   `freshness` if the label exists. This is the thing the course owner actually
   sees each month.
3. **Conversational summary** if run interactively: lead with the headline (e.g.
   "3 wrong-now, 5 stale, 2 dead links, rest holding"), then the must-fix items.

## Notes
- This is intentionally **advisory**. Expect occasional false positives on
  deliberately-dated content; that's why every finding carries a source and a
  confidence flag, and why nothing auto-applies.
- A headless/scheduled run cannot reach Amathuba (no browser session). It audits
  the repo only; the human mirrors accepted fixes to the LMS per the usual flow.
- Related: `.claude/skills/verify-references/SKILL.md` (citation existence checks),
  `RECONCILE-NOTES.md`, `AMATHUBA-EDIT-CHECKLIST.md`, and the CLAUDE.md
  "docs/ is canonical" rule.
