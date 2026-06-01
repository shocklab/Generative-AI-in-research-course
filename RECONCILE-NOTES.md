# docs ↔ Amathuba reconciliation — working notes

Goal: end with **one source of truth (`docs/`)** and Amathuba matching it, with no editorial work lost from either side.

## Phase 5 — Merge (docs-side) ✅ IN PROGRESS

**LMS-only pages — decisions made:**
- **Hands-On Exploration: Testing Generative AI Tools (Week 1)** → **ADOPTED into docs** as `docs/week-1/Hands-On Exploration.html` (converted bare LMS import file to house template; added to `index.html` + prev/next nav). It's self-contained lesson content that renders fine statically.
- **Class introductions (Week 1)** → **left intentionally LMS-only.** It is only a wrapper around an embedded Brightspace discussion board, which cannot function on the static GitHub site; adopting it would create a dead page. Recorded here so future audits don't re-flag it.
- **Meet the course team (orientation)** → **left intentionally LMS-only** (teaching-team/personal info; per user decision).

**Still to do (Amathuba-side — user applies by hand, since direct-LMS editing is the user's domain):**
1. Apply `AMATHUBA-EDIT-CHECKLIST.md` (the bucket-(c) fact-fixes) to Lessons 1–9.
2. Rename the four collision-named "Hands-On Activities and Assessment" pages on Amathuba to disambiguate by week (currently Weeks 5/6/8/9; two carry literal "- Copy" suffixes).
3. Settle the per-page H1/title wordings (see list below) — decide which wording is canonical and align both sides.
4. Optionally upload the new `docs/week-1/Hands-On Exploration.html` to Amathuba if a tidied version is wanted there too (the LMS already has the original).

**H1/title conflicts to settle (user decides per page):** the main known one is Week-1 history — Amathuba H1 "The Evolution of Artificial Intelligence" vs docs "History of AI: From Neurons to Neural Networks". (A complete H1 list can be generated on request by diffing H1s export-vs-docs.)

## Phase 1 — Governance ✅ DONE
- `docs/` declared canonical; "never edit Amathuba directly" rule added to CLAUDE.md.

## Phase 2 — Fork characterisation ✅ DONE (against the March 2026 export)

Method: strip CSS/scripts/tags → word-level `difflib` similarity between each March-export page and its `docs/` counterpart. The March export is **stale** (predates Weeks 9–12 and this session's fixes) and uses cryptic `m3816909_*` filenames for Week 1, so it is a *method-validation + shape-reading* basis only — **not** the reconcile basis.

**Headline finding: there is no large hidden fork.** Across all 13 matchable pages, similarity is 90–99% on 11 of them, and every content-level difference inspected falls into one of three buckets:

- **(a) Cosmetic / chrome** — docs-only "Back to Contents" bar, prev/next nav, footer. *Ignore* (these are docs-site furniture, deliberately not on Amathuba).
- **(b) Amathuba-only editorial** — the only genuine "fork" content. So far the clearest example is the **History page H1**: Amathuba shows *"The Evolution of Artificial Intelligence"*; docs uses *"History of AI: From Neurons to Neural Networks"*. These are LMS-side wording choices docs lacks — must be **harvested into docs**, not discarded.
- **(c) docs-only fixes** — our session fact-checks not yet on Amathuba. These are exactly the `AMATHUBA-EDIT-CHECKLIST.md` items.

Per-page similarity (March export vs current docs; lower = more session-fixes + more to look at):

| docs page | sim | note |
|---|---|---|
| Training Large Language Models | 0.994 | trivial |
| The Broader Landscape of AI Ethics | 0.994 | trivial |
| Paid Tools and When They Are Worth It | 0.993 | trivial |
| Critical Minerals and AI | 0.991 | fact-fixes only |
| Infrastructure Scale and the Rebound Problem | 0.984 | TMI fix etc. |
| The Hallucinated Citation Crisis | 0.985 | Linardon fix |
| History of AI From Neurons to Neural Networks | 0.983 | all fixes = checklist items; H1 = bucket (b) |
| Understanding How Generative AI Works | 0.968 | context-window + Nano Banana |
| Foundations of Generative AI | 0.956 | minor |
| LLM Architecture Deep Dive | 0.901 | Current-Frontier rewrite + link fix |
| Current Generative AI Landscape | 0.904 | currency refresh (lots of model names) |
| How AI Image Generation Works | 0.798 | title/notice rewrite — **inspect** |
| What Does AI Actually Consume | 0.731 | **lowest — inspect closely** |

**Implication:** the reconcile is mostly "apply the checklist fixes to Amathuba" (already documented) **plus** a small harvest of bucket-(b) LMS-only wording (H1s, possibly a few headings) back into docs. Not a big merge.

## Phase 3 — Fresh Brightspace export ✅ DONE
Current export (01 June 2026) copied into `From Amathuba/MAM5020F 2026  Gen AI for Research_01 June 2026 207 PM/` — 69 HTML files, includes Weeks 9–12. Confirmed it captures the session's Amathuba work (W11/W12 pages, W8 Intron fix, W9 HLE fix, W11.6 8-founder Indaba) and still shows the un-applied checklist items (e.g. W3 TMI "restarted" error present).

## Phase 4 — Categorised reconciliation report ✅ DONE (against 01 June export)

Auto-mapped all 69 export pages to their best `docs/` match by content similarity. **The fork is small and well-behaved.**

**Bucket summary:**
- **57 pages ≥ 0.97 similar** → identical modulo docs-only chrome. **Nothing to do.**
- **5 pages 0.85–0.97** (LLM Architecture, Current Landscape, Foundations, Course Caveats, "But what is a neural network") → differences are the **session fact-fixes** = bucket (c), already in `AMATHUBA-EDIT-CHECKLIST.md`.
- **Low-similarity matches** that are actually heavily-edited real pairs (How AI Image Generation 0.80, Intro to Transformers 0.81, Lightning Tour 0.84) → also bucket (c) / cosmetic; short/video pages where small edits move the ratio.

**Bucket (b) — genuine Amathuba-only content the repo is MISSING (the real reconciliation payload):**
| LMS page | Status | Action |
|---|---|---|
| **Class introductions** (Week 1) | live activity page, not in docs | decide: add to docs, or intentionally LMS-only |
| **Meet the course team** (orientation) | live, not in docs | likely intentionally LMS-only (personal/teaching-team info) |
| **Course Orientation / Overview** | live, not in docs | check vs `docs/course-orientation/Overview.html` (may be a near-empty template stub on the site) |
| **Hands-On Exploration: Testing GenAI Tools** (`m…slln2nvba`, Week 1) | live activity page, not in docs | decide: add to docs, or intentionally LMS-only |

**Bucket (b) — LMS housekeeping (not a content fork, but worth fixing on Amathuba):**
- **Four "Hands-On Activities and Assessment" pages share collision-prone names** (two carry literal "- Copy"/"- Copy (1)/(2)" suffixes from duplication). They are actually **different weeks**: `- Copy (1)`=Week 8, `- Copy (2)`=Week 9, `- Copy`=Week 6, plain=Week 5. Recommend renaming each on Amathuba to "Week N — Hands-On Activities and Assessment" to remove ambiguity. (docs already keeps them cleanly separated by week folder.)

**H1/title differences** (bucket b, decide per page — user chose case-by-case): the clearest is the Week-1 history page — Amathuba H1 "The Evolution of Artificial Intelligence" vs docs "History of AI: From Neurons to Neural Networks". A full H1-conflict list will be produced at merge time.

**Net:** reconciliation = (c) apply the existing checklist to Amathuba  +  (b) decide on 4 LMS-only pages (adopt into docs or mark intentionally-LMS-only) + tidy the 4 duplicate Hands-On names + settle a short list of H1 wordings. No large content merge.

## ~~Phase 3~~ (superseded — see above)
<!-- original Phase 3 instructions retained below for reference -->
### Original Phase 3 instructions ⏳ NEEDS USER
The March export can't be the reconcile basis (stale + missing Weeks 9–12). Need a **current** export:
1. Amathuba → **Manage Course → Import / Export / Copy Components**
2. **Export** as a component package (include all Content/HTML topics).
3. Download the zip, unzip it into the repo (e.g. `From Amathuba/<dated folder>/`), and tell me the path.

That gives current live HTML for **all** lessons (1–12), including the pages just built, so the diff reflects reality.

## Phase 4 — Categorised reconciliation report (from fresh export)
Re-run the Phase-2 harness on the fresh export → per-page decision list, each difference bucketed (a)/(b)/(c). Output: exactly what to harvest into docs (b) and what to push to Amathuba (c).

## Phase 5 — Merge & republish
- Harvest bucket-(b) Amathuba-only wording into `docs/` + `Week N/` source + `build_weekN.py`; commit (→ live GitHub site updates).
- Apply bucket-(c) fixes to Amathuba (the checklist) — or, cleaner, re-upload the now-unified pages.
- End state: docs == Amathuba (modulo intentional chrome). One source of truth.

## Decision still open for Phase 5
For bucket-(b) H1/title differences (e.g. "The Evolution of AI" vs "History of AI…"): decide per page which wording wins. Default proposal: **keep the Amathuba H1 wording** (it was a deliberate later edit) and bring it into docs — unless you prefer the docs wording, in which case docs wins and Amathuba gets updated.
