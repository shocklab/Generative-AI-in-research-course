# docs ↔ Amathuba reconciliation — working notes

Goal: end with **one source of truth (`docs/`)** and Amathuba matching it, with no editorial work lost from either side.

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

## Phase 3 — Fresh Brightspace export ⏳ NEEDS USER
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
