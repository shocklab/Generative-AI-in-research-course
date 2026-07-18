# Course prose style — the de-slop avoid-list

The canonical avoid-list for MAM5020F lesson prose. Goal: read like a person wrote
it, not a model. Fix the tells below while preserving meaning, facts, citations,
numbers, and the calibrated-reading voice. It is a prior, not a straitjacket — a
flagged word is fine when it is genuinely the right one.

**All budgets are per 1,000 words, measured across the whole corpus on the BUILT
site (`docs/`, the `.abody` container), never per paragraph.** A per-paragraph rule
reported zero violations on a sibling course carrying 13 dashes per 1,000 words;
the reader drowned anyway. Census first, edit in `content/`, rebuild, re-census.

## 1. The dominant tell: don't label your own points

The course's most grating habit is prose that tells the reader which of its *own*
points are clever, important, honest, or significant — instead of just making the
point and trusting the reader to see it. Cut it.

Delete or rewrite self-labels like:
- "the **load-bearing** assumption / claim / decision" → just state the thing
- "the cleanest X in the block", "the honest framing", "the real finding here",
  "the part that changes how you work", "the single most important file"
- "this is **the hinge** of the whole track", "the headline artefact"
- "**notice what just happened**", "here's what makes that earn its place",
  "that sentence is **doing a lot of work**"
- "**precisely because**", "exactly the …" used to flag your own cleverness or
  foreshadow your own payoff

> Before: "Watch the upstream halving in particular — it is the load-bearing
> decision that decides the answer."
> After: "The upstream halving is what changes the answer."

Make the point. If it is good, the reader will notice without being told.

## 2. Emphasis bold — THIS course's biggest measured problem

**Budget: zero emphasis bold in prose.** Measured 2026-07-18 at 13.1 `<strong>`
per 1,000 words corpus-wide; the Week 5 pilot cut one page from 25.5 to 3.0
without losing a fact.

Exempt (these are not emphasis):
- **First use of a technical term** being defined at that point.
- Table headers and row-labels, rubric criterion names, glossary term markup.
- Bold that is part of a quoted source.

NOT exempt: `<li><strong>Label:</strong>` list-opener bolds in tool listings and
card lists. The approved Week 5 pilot unbolded 52 of them (the colon structure
carries the label); that is the precedent.

The distinction that matters (learned on a Week 3 near-miss): a bolded **verified
number, citation title, or table label is content, not emphasis** — a naive
unbolding sweep mangles fact-dense pages. Inspect context before every edit on
listing/table-heavy pages.

## 3. Em-dashes

**Budget: zero in running prose.** A comma, colon, full stop, or parentheses
serves. Do **not** evade by swapping em-dash (`—` / `&mdash;`) for en-dash
(`–` / `&ndash;`) or a spaced hyphen doing the same job.

Exempt: dash-*labels* where the dash separates a label from content ("Step 3 —
Scale by √d", "Anthropic — Claude Opus", "Mhlambi (2020) — the philosophical
substrate", folder listings); en-dashes in ranges and compound names (2012–2017,
Mori–Zwanzig). Those are correct typography.

## 4. "X, not Y" — the delete-test, not a number

Delete ", not Y": **if the claim dies, the contrast was the content — keep it.**
If the claim survives, the contrast was decoration — state the claim directly.

Expect a high keep-rate: on this course's headings, 34 of 44 flagged survived
review (the negation IS the claim: "Reliability Is Not Accuracy" is a finding's
name; "the harness, not the model" is Week 10's thesis; scope labels like
"Linked but not redistributed" are facts). A course that teaches by distinctions
keeps its distinctions. Triage each hit; never bulk-rewrite this family.

## 5. The course narrating itself

Course-as-agent with intent or virtue — "the course moved deliberately", "this
course refuses", "we have tried to be honest here", "this section is deliberately
a taster" — delete the meta-commentary or state the content directly. Plain
navigation ("this week covers X", "10.4 takes this up") is fine in moderation.

Framing arrows in prose ("Idealised → empirical") get written as words. Pipeline
and technical arrows (data flows, step chains, `chat.deepseek.com → R1`) stay.

## 6. The honesty boundary — protect-list (censused 2026-07-18, 127 hits read)

This course *teaches* intellectual honesty. The word is subject matter here, not
a tell. **Protected — do not touch:**
- Honesty as the topic: "intellectual honesty", "duty of honesty", "honest
  disclosure/reporting/uncertainty", "be honest with yourself", the integrity
  spectrum, virtue-ethics discussion of honesty.
- **"Honest" in the HHH alignment framework** (Helpful, Harmless, Honest — Week 2).
- Assessment and rubric vocabulary: "Honest reporting of AI tool successes AND
  failures", "honest self-critique", capstone prompts ("The honest counter-claim",
  "three honest hours"), every Discussion Question asking students to answer
  honestly.
- Honesty OF a source or practice: "the Gowers post is honest about this", "the
  Sakana team behaved very honestly", "operationally honest".
- The course's named "one disposition" formulation ("… and an honest sense of
  where the present ends") — a named course device, mirrored across pages.

**The tell (kill on sight): "honest" as a badge on the course's own analysis** —
"honest verdicts", "the honest ranking", "the honest access picture", "the honest
answer is…", "Two honest caveats", "a closing honesty note". Delete the word; the
verdict/ranking/caveat stands. Concentrated on Week 10 tool pages.

Also protected: `deliberately` when factual or instructional ("deliberately messy
archive" describes the dataset; "labs are deliberately secretive" is a claim;
"connect deliberately" is an instruction). The tell is only course-self-narration.
`harness` (model-vs-harness) is a core course concept, never a banned word here.

## 7. Banned vocabulary — the plainer word wins

delve / dive into → look at, examine · leverage → use · underscore → show ·
bolster → strengthen · foster → support · comprehensive → full, thorough ·
robust → solid, reliable · nuanced → subtle · seamless → smooth · intricate →
complex · multifaceted / holistic → (drop) · transformative / groundbreaking →
major, big · pivotal → key · realm / figurative *landscape* → field, area ·
testament → (drop) · the spine / through-line (essayist tics) → anchor, runs
through.

Also cut: significance-labels (*crucially, importantly, notably, it's important
to*); connective stacking (*Moreover, Furthermore, Additionally*) where you'd just
continue; pseudo-depth openers (*At its core, In essence, Fundamentally, Simply
put*); padding adverbs (*simply, basically, essentially, just*).

## 8. Structure

Avoid the forced rule of three; both-sidesing (take a position); dramatic
noun-phrase headings; and paragraphs you could swap without breaking the argument.

**Mirrored phrases:** if a sentence is deliberately echoed on a sibling page
(Next-boxes, intro boxes, a body line quoted in that page's own Discussion
Questions), edit both identically or neither.

## Keep — do NOT "fix" these

- Code blocks, citations, DOIs, links, names, numbers, dates, every factual claim.
- Glossary terms (`glossary.json` is the term store) and their in-page markup.
- British spelling, and the course's actual arguments and worked examples.
- Quoted text from sources — match the source, not this guide.

**Headings ARE editable** (the old "wired to nav/SCORM" exemption was disproven
2026-07-16: 30+ headings edited safely; the renderer syncs h1/title/nav from one
build). But a *page rename* is a procedure, not an edit: filename + `<title>` +
h1 + every inbound href + all link-text variants + generators + `content/index.html`,
in `content/` AND the Amathuba source folders. Heading-list adjudications go to
Jonathan **as an .xlsx**, not markdown.

## Verification (every pass)

1. Edit `content/`, never `docs/`. `python3 redesign/build_site.py`, then census
   the BUILT `docs/`.
2. Tag-balance check on every edited file — count openers vs closers for **every**
   tag the corpus uses: div, p, span, h1–h6, strong, em, li, ul, ol, a, details,
   figure, table. (A checker that counts only the tags you thought of will pass
   the ones you didn't — 12 unclosed spans got through the sibling sweep that way.)
3. `verify_content.py` + `check_links.py` clean; `git diff --stat` roughly
   line-balanced — large insertions mean an agent rewrote beyond its brief.
4. Baseline (2026-07-18, 87 pages, 192,664 prose words): strong 13.08/1k ·
   em-dash 2.29/1k · X-not-Y 1.66/1k · virtue lexicon 0.73/1k · arrows 0.28/1k ·
   course-as-agent 0.05/1k. Re-census against these; the numbers must fall.
