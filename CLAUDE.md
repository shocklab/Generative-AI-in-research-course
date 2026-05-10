# Generative AI in Research — Course Materials

## Project Overview

Course materials for **MAM5020F 2026: Generative AI for Research** at the University of Cape Town. A 12-week, NQF Level 9 (postgraduate) course requiring no prior ML, CS, or programming background. Taught by Assoc. Prof. Jonathan Shock.

**Repository:** https://github.com/shocklab/Generative-AI-in-research-course
**GitHub Pages site:** https://shocklab.github.io/Generative-AI-in-research-course/ (served from `/docs` on `main`)
**Licence:** [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). Authorised under clauses 8.2 and 9.2.1 of the UCT Intellectual Property Policy (2011), which assigns course-material copyright to the academic author and explicitly permits Creative Commons distribution. UCT retains a perpetual royalty-free non-exclusive internal-use licence (clause 8.2). Suggested citation: `Shock, J. (2026). MAM5020F: Generative AI for Research [Course materials]. University of Cape Town.`

## Course Structure

Each week follows a three-phase structure: **Pre-Class** (readings/videos), **In-Class** (discussions/activities), **Post-Class** (deeper reading and assignments). All readings are freely accessible.

**Assessment:** Weekly practical exercises (40%), research enhancement project with presentation (40%), ethical framework development (20%).

## 12-Week Topic Map

| Week | Topic | Status |
|------|-------|--------|
| 1 | Foundations of Generative AI | Built |
| 2 | LLM Deep Dive | Built |
| 3 | Environmental Implications of AI | Built |
| 4 | Ethical Frameworks for AI in Research | Built |
| 5 | AI-Assisted Literature Review | Built |
| 6 | AI for Writing, Communication & Research Ideation | Built |
| 7 | AI for Data, Code & Computation | Built |
| 8 | Multimodal AI for Research | Built; uploaded to Amathuba; Assignment 4 live |
| 9 | Critical Evaluation & Limitations of AI | Built |
| 10 | Agentic AI, RAG & Advanced Research Tools | Not started |
| 11 | Future of AI in Research & Africa's Sovereign AI Capacity | Not started |
| 12 | Integrative Workshop & Student Presentations | Not started |

**Note on restructured schedule (Weeks 7-12):** The original Weeks 7 (Data Analysis) and 8 (Coding/Computational Research) were merged into Week 7 because they overlap heavily — data analysis IS coding for most researchers. Original Week 9 (Domain-Specific Applications) content is woven into other weeks as case studies. Original Week 10 (Critical Evaluation/Limitations) was moved to Week 9. This freed a slot for a Multimodal AI week (Week 8) and a Flexible/TBD week. See the plan file at `.claude/plans/goofy-whistling-journal.md` for full rationale.

## File Structure

```
Course introduction/
  Introduction to the course.html
  Table of Contents.html

Week 1/          (Foundations of Generative AI)
  Table of Contents.html
  Course Caveats.html
  Class introductions.html
  A lightning tour of AI - video.html
  But what is a neural network.html
  An introduction to Transformers - from 3Brown1Blue.html
  Import - 1770828860589/    (additional imported content)

Week 2/          (LLM Deep Dive)
  Table of Contents.html
  LLM Architecture Deep Dive.html
  Fine-Tuning, RLHF and Alignment.html
  Untitled.html

week 3/          (Environmental Implications of AI)
  Table of Contents.html
  The Cost of Every Prompt.html
  Infrastructure, Scale and the Rebound Problem.html
  Critical Minerals and AI.html
  Sustainable AI - Practices and Possibilities.html
  Environmental Impacts of AI.docx    (supplementary reference doc)

Week 4/          (Ethical Frameworks for AI in Research)
  Table of Contents.html
  Ethical Frameworks and Four Lenses.html
  Ubuntu Relational Ethics and the Just AI Framework.html
  Transparency Authorship and Integrity.html
  Applying Ethics Case Studies and Your Framework.html
  The Broader Landscape of AI Ethics.html    (supplementary — topics not fully covered)

Week 5/          (AI-Assisted Literature Reviews)
  Table of Contents.html
  The AI Literature Review Landscape.html
  Free Tools Deep Dive.html
  Paid Tools and When They Are Worth It.html
  The Hallucinated Citation Crisis.html
  Building Your Research Workflow with Claude.html
  Hands-On Activities and Assessment.html

Week 6/          (AI for Writing, Communication & Research Ideation)
  Table of Contents.html
  Writing as Thinking.html
  Research Ideation with AI.html
  AI Writing Tools Landscape and Honest Assessment.html
  Scientific Integrity and the Writing Pipeline.html
  Building Your AI Writing Workflow.html
  Hands-On Activities and Assessment.html
  Using AI to Review Your Own Work.html    (supplementary — based on paper-review skill)

Week 7/          (AI for Data, Code & Computation)
  Table of Contents.html
  Natural Language to Code.html
  AI-Assisted Data Analysis in Practice.html
  Visualization with AI.html
  Verification of AI-Generated Code.html
  Building Your Data Analysis Workflow.html
  Hands-On Activities and Assessment.html

Week 8/          (Multimodal AI for Research)
  Table of Contents.html
  What Multimodal AI Can See Hear and Read.html
  AI and Scientific Images.html
  Document Intelligence.html
  Transcription and Audio Analysis.html
  Video and Multimodal Workflows.html
  Hands-On Activities and Assessment.html

From Amathuba/           (Amathuba/Brightspace export — the live/edited versions of all lessons)

docs/                    (GitHub Pages site — served at shocklab.github.io)
  index.html             (Landing page with full course navigation)
  course-orientation/    (Overview, Meet the Course Team)
  course-introduction/   (Introduction, Course Caveats, AI Content Disclaimer)
  week-1/ through week-8/  (All lesson pages from Amathuba export, organised by week)
```

Lesson plans.docx        (full 12-week lesson plans with readings/activities)
Style guide.rtf          (HTML/CSS design system for Brightspace pages)
RIA_JustAI_Framework_Summary.md   (summary of RIA Just AI Framework, used in Week 4)

## Design System

All sub-lesson pages use **inline CSS** following UCT branding (no external stylesheets beyond Brightspace CDN). Key design tokens:

- **Primary colour:** `#003A70` (UCT blue)
- **Secondary colour:** `#2a5298` (lighter blue for headings)
- **Font:** Lato via Brightspace CDN (`https://s.brightspace.com/lib/fonts/0.6.1/fonts.css`)
- **Brightspace CSS:** `https://templates.lcs.brightspace.com/lib/assets/css/styles.min.css`
- **Responsive breakpoint:** 768px

### CSS Components

| Class | Purpose |
|-------|---------|
| `.ai-notice` | Blue banner noting Claude enhancement |
| `header` + `.week-badge` | Dark blue header with "Week X • Sub-Lesson Y" badge |
| `.content` | Main content wrapper (padding: 50px 40px) |
| `.intro-text` | Gray box with left blue border — always first section ("What We'll Cover") |
| `.section-title` | Large blue h2 with bottom border and emoji prefix |
| `.card-grid` + `.card` | Responsive grid of hoverable cards (min 300px, border-left) |
| `.styled-list` | Custom triangle (▸) bullet points |
| `.highlight-box` | Dark blue (#003A70) background call-out for key insights |
| `.warning-box` | Yellow (#fff8e1) box with orange border for cautions |
| `.info-box` | Light gray box with blue left border for notes/tips |
| `.resource-placeholder` | Dashed border box for readings/resources |
| `.technical-detail` | White box with blue border for detailed content |
| `.comparison-table` | Styled table with dark blue header row |
| `.case-study` | Gradient background with blue border for scenarios |
| `.decision-framework` | Gradient background with solid border for frameworks |
| `.tool-card` | Top-bordered card for tool listings |
| `.step-list` | Numbered steps with blue circle counters. **Important:** uses `> li` direct child selectors so nested lists inside step items are not affected by the counter or blue circle styling |

### Page Template Structure

Every sub-lesson follows this skeleton:
1. `<!DOCTYPE html>` with charset, viewport, title (`Week X.Y - Title`)
2. Brightspace fonts CDN link
3. Full inline `<style>` block (duplicated per page)
4. Brightspace CSS link at end of `<head>`
5. `.container` > `.ai-notice` > `<header>` > `.content`
6. `.intro-text` ("What We'll Cover") — always first
7. Multiple `h2.section-title` sections with content components
8. Final `.intro-text` summary with forward pointer to next session

### Table of Contents Template

ToC pages use a simpler Brightspace/D2L format: a `<table>` with `<font class="title">` for the week title and `<p class='d2l'>` entries linking to sub-lesson files.

## Conventions

- All links use `target="_blank" rel="noopener"`
- Emojis appear inside h2 section titles (before text) and in h1 headers
- Header h1 text wrapped in `<span style="color: #ffffff;">`
- Sub-lesson intro paragraphs are conversational, not bullet-point
- Each page has an AI transparency notice at the top: "This page's design, presentation and content have been created and enhanced using Claude (Anthropic's AI assistant) to improve visual quality and educational experience."
- Summary sections use `.intro-text` with `margin-top: 50px`
- The final sub-lesson of each week provides a full-week summary and "Next week" pointer
- Supplementary pages use `Week X • Supplementary` in the week-badge (not a numbered sub-lesson)

## Build Process for New Weeks

When building a new week's content, follow these steps in order:

1. **Research & plan** — Read the lesson plan, research the topic with web searches, propose structure to user for approval
2. **Build sub-lesson HTML pages** — Follow the design system, CSS conventions, and page template structure documented above
3. **Build Table of Contents page** — Link to all sub-lesson files
4. **🔴 MANDATORY: Run `/verify-references`** — Before considering a week complete, run the reference verification skill against all new HTML files. This checks every URL, academic citation, and statistical claim against primary sources. Do NOT skip this step. Experience from Week 5 showed that web search summaries and AI-generated content frequently contain incorrect statistics, hallucinated citation details, and broken URLs.
5. **Fix any issues** — Present the verification report to the user, get approval, then correct any problems found
6. **Update docs/ site** — Copy the Amathuba-exported versions of new lesson pages into the appropriate `docs/week-N/` folder, add back-nav links, and update `docs/index.html` with new lesson links
7. **Push to GitHub** — Commit and push all changes (source files, docs/, CLAUDE.md). GitHub Pages auto-deploys from `/docs` on `main`
8. **Upload to Amathuba** — Use Claude in Chrome to automate page creation (Create Module → Create Page → paste HTML via source code editor). **🔴 IMPORTANT: Before pasting into Amathuba's source code editor, sanitise the HTML** to convert emojis to the correct format: CSS `content` properties need unicode escapes (`\1F3AF`), HTML body content needs HTML entities (`&#127919;`). Use this script to prepare the clipboard:
   ```bash
   python3 -c "
   import sys, re
   with open(sys.argv[1], 'r') as f: content = f.read()
   def css_fix(m):
       r = []
       for ch in m.group(0):
           r.append('\\\\\\\\' + format(ord(ch), 'X') if ord(ch) > 127 else ch)
       return ''.join(r)
   content = re.sub(r\"content:\s*'[^']*'\", css_fix, content)
   sys.stdout.write(''.join(f'&#{ord(c)};' if ord(c) > 127 else c for c in content))
   " FILENAME.html | pbcopy
   ```
   Without this step, Brightspace's editor corrupts UTF-8 emojis into garbled characters (lesson learned from Week 6).
9. **Update CLAUDE.md** — Mark the week as Built, add file structure, content details, and any new CSS components or notes

## Key References for Building New Weeks

- **CSS template source:** `week 3/Sustainable AI - Practices and Possibilities.html` (widest component set)
- **Week 4 CSS template:** `Week 4/The Broader Landscape of AI Ethics.html` (full component set including case-study, comparison-table)
- **Case study styling:** `week 3/Critical Minerals and AI.html`
- **Full page structure:** `week 3/The Cost of Every Prompt.html`
- **Lesson plans for all 12 weeks:** `Lesson plans.docx`
- **Design system details:** `Style guide.rtf`
- **Reference verification skill:** `.claude/skills/verify-references/SKILL.md`

## Week 4 Content Details

Week 4 has 4 core sub-lessons plus 1 supplementary page:

1. **Ethical Frameworks and Four Lenses** — The ethics gap, four philosophical lenses (consequentialism, deontology, virtue ethics, ubuntu), worked example scenario, all week readings. Includes forward reference to RIA Just AI Framework (info-box after "Why Four Lenses, Not One?") and pointer to the broader landscape page.
2. **Ubuntu, Relational Ethics and the Just AI Framework** — Ubuntu philosophy, Mhlambi's "From Rationality to Relationality" (linked to perma.cc/Q5ZL-TTD8), Birhane's algorithmic injustice (linked to abebabirhane.com), RIA Just AI Framework (9 core inquiries as card grid, 4 structural challenges), Esethu Framework case study (Rajab et al., 2025 — community-driven data governance for low-resource languages), comparison table (individualist vs ubuntu/Just AI), Global South perspectives.
3. **Transparency, Authorship and Integrity** — Disclosure norms, journal policy comparison table (Nature, Science, IEEE, ACM, Elsevier, PLOS), AI authorship debate, bias in AI-assisted research, privacy/data handling, academic integrity spectrum, intellectual property.
4. **Applying Ethics: Case Studies and Your Framework** — 6-step decision framework (step-list), 4 case studies (Dr. Amara, Thabo, Dr. Nkosi, Fatima), personal ethical framework guide, journal policy audit, weekly assessment. Full week summary with forward pointer to Week 5 and to the broader landscape page.
5. **The Broader Landscape of AI Ethics** (Supplementary) — 12 dimensions not fully covered: labour exploitation, surveillance/carceral AI, autonomous weapons, corporate power, deepfakes/democracy, gender, disability, emotional/psychological impacts, accountability/liability, indigenous data sovereignty (CARE Principles), feminist ethics of care, AI and labour market. Institutions section linking to UCT Ethics Lab, Global Center on AI Governance, Research ICT Africa, AI Now Institute, Algorithmic Justice League, GovAI, Data & Society.

## Week 5 Content Details

Week 5 has 6 core sub-lessons:

1. **The AI Literature Review Landscape** — Why AI changes literature review (6 pain point/solution cards), three categories of tools (citation-based, semantic search, grounded chat/RAG), how tools work under the hood (graph analysis, embeddings, RAG), building a combined workflow (6-step strategy), all week readings (3 core + 5 supplementary).
2. **Free Tools Deep Dive** — Detailed coverage of Semantic Scholar, ResearchRabbit (post-2025 merger with Litmaps), Connected Papers, NotebookLM, Google Scholar. Each tool has strengths/limitations cards and best-use-case guidance. Comparison table including Perplexity and Gemini Deep Research. Combined free workflow recommendation.
3. **Paid Tools and When They Are Worth It** — Honest assessments of Elicit (~$12/mo, killer data extraction), Consensus (~$9/mo, Consensus Meter), Scite.ai (~$12/mo, smart citations supporting/contrasting), SciSpace (~$12/mo, all-in-one), Litmaps Premium (best visualisations). Each has pricing, worth-it/not-worth-it verdicts. Comparison table. Institutional access note for UCT.
4. **The Hallucinated Citation Crisis** — All statistics properly sourced and cited. Scale of the problem: Stanford HAI legal AI study (Magesh et al., 2024 — 17-34% for purpose-built tools, 58-82% for general chatbots), JMIR comparative analysis (Chelli et al., 2024 — GPT-3.5 39.6%, GPT-4 28.6%, Bard 91.4%), JMIR Mental Health (Linardon et al., 2025 — GPT-4o 19.9% overall, 28-29% for niche topics vs 6% for well-studied). NeurIPS 2025 scandal sourced from GPTZero analysis, Fortune, TechCrunch (4,841 papers scanned, 100+ hallucinated citations across 51 papers, "vibe citing" term). Partial hallucinations sourced from GPTZero's "uncanny valley" findings. Citation frequency correlation from Niimi (2025, arxiv). Also covers: why it happens (pattern completion vs knowledge), the pollution loop, Five-Point Citation Check verification toolkit, red flags, Retraction Watch.
5. **Building Your Research Workflow with Claude** — Three levels: Level 1 (better prompts — structured literature, synthesis, critical reading, anti-hallucination templates), Level 2 (Claude Projects for persistent research context), Level 3 (Claude Code skills and CLAUDE.md for power users, Teresa Torres approach). Privacy and data warning. Includes prompt-example and code-block custom CSS components.
6. **Hands-On Activities and Assessment** — Activity 1: Comparative Search Challenge (same question through 4 tools). Activity 2: Citation Verification Exercise (10 AI-generated references, verify all). Activity 3: Literature Map Construction (Connected Papers or ResearchRabbit). Weekly assessment: 1000-word AI-assisted mini literature review with reliability audit (3+ verified/corrected claims) and ethical reflection. Submit via Amathuba. Full week summary with forward pointer to Week 6.

## Week 6 Content Details

Week 6 has 6 core sub-lessons plus 1 supplementary page. It folds in the research ideation content from the original lesson plan's Week 5.

1. **Writing as Thinking — Why the Process Matters** — Cognitive science of writing-as-thinking, Harvard Gazette (2025) "Is AI dulling our minds?", MIT Media Lab "Your Brain on ChatGPT" study (now published in PMC), Frontiers in AI (2025) cognitive dissonance study, the "first draft trap", a spectrum of AI assistance (5 levels from proofreading to generating sections), connection to Week 4 virtue ethics. Readings: Harvard Gazette, Frontiers in AI, Frontiers in Education, Psychology Today, Holmner et al. (ASIS&T).
2. **Research Ideation with AI** — Folded in from original Week 5. Five prompting strategies (chain-of-thought, role-playing, constraint-based, adversarial, cross-disciplinary) with practical examples. Si et al. (2024) study (LLM ideas rated more novel but less feasible/diverse). Idea monoculture: Nature Comms Psychology (2026) "scientific monoculture" paper, ScienceDirect (2025) homogenisation study. Five ideation risks (anchoring, confirmation bias, premature convergence, novelty illusion, loss of serendipity). When NOT to use AI. Girotra, Meincke, Terwiesch & Ulrich (2023) with caveat that AI has improved since. Sakana AI "AI Scientist" (Nature 2026) as supplementary reading.
3. **AI Writing Tools — Landscape and Honest Assessment** — Four tool categories (general LLMs, specialist academic, grammar/style, translation). Multilingual equity: Amano, Bowker & Burton-Jones (2025, PLOS Biology) two futures for multilingual publishing, writing time ~50% longer for non-native speakers. Homogenisation: Agarwal, Naaman & Vashistha (2025, CHI) Indian writing becoming more American. African context. Usdan, Connell Pensky & Chang (2024, CMU/SSRN) — 64.5% time reduction, B+ to A grades. Comparison table (8 tools). Daryani et al. (2026) homogenising engine.
4. **Scientific Integrity and the Writing Pipeline** — Integrity spectrum (6 levels, colour-coded risk cards). Nuanced data description section distinguishing with/without data access, modern models pushing back rather than fabricating, subtler risks (instructed fabrication, over-claiming, silent gap-filling). "When AI knows more than you" warning box. Journal policy comparison table with hyperlinked policies: Science/AAAS (updated Nov 2023, now disclosure-based), Nature, Elsevier (Sept 2025), IEEE, ACM, COPE. AI detection unreliability (Pangram Labs 2025). Practical auditing techniques (5 cards). Data integrity and fabrication detection tools. Disclosure templates (3 levels). "Practice what we preach" note that these course materials themselves are Template 3. Frontiers in AI (2025) scientific integrity paper. AMEE Guide No.192.
5. **Building Your AI Writing Workflow** — 5-stage principled workflow (think → outline → draft with AI → audit → revise in your voice). Prompt examples for: blank page paralysis, structuring arguments, translation/polishing, clarity feedback, audience summarisation. Warning about subtle argument changes even with explicit preservation instructions. Reverse outline technique. Version control for AI-assisted writing. Disclosure templates (3 levels with guidance).
6. **Hands-On Activities and Assessment** — Activity 1: Writing Process Experiment (300 words human vs AI, compare). Activity 2: Prompt Engineering for Ideation (4 rounds: naive, chain-of-thought, persona, constraint). Activity 3: Audit Exercise (systematic audit of AI-assisted writing). Weekly assessment: 800-word AI-assisted writing sample with process log, self-audit (3+ corrections), and disclosure statement. Criteria: Writing Quality 30%, Process Log 25%, Self-Audit 25%, Disclosure 20%. Full week summary with forward pointer to Week 7.
7. **Using AI to Review Your Own Work** (Supplementary) — Based on the paper-review skill. What AI can check (6 dimensions: logical consistency, writing quality, positioning, methodology, statistics, figures). What AI cannot reliably judge (novelty, domain conventions, significance, ethics, reviewer taste) — with caveat that AI's outsider perspective can catch author blind spots. Multi-agent review approach. Practical prompting guide (5 steps). Limitations warning. Venue-specific review standards.

## Week 7 Content Details

Week 7 has 6 core sub-lessons. It merges the original Weeks 7 (Data Analysis) and 8 (Coding/Computational Research) into one richer week.

1. **Natural Language to Code — The New Interface** — The paradigm shift: describing analysis in plain English. Tools landscape: Claude Code, ChatGPT Code Interpreter, GitHub Copilot, Cursor, Google Colab AI, Gemini Code Assist. Comparison table (6 tools, free vs paid tiers). Free vs paid quality gap (context window, model quality, rate limits, file access) with honest assessment and strategies for maximising free tier value. "Vibe coding" — when useful (prototyping, exploration), when dangerous (publication, consequences). Minimum code literacy for AI-assisted researchers (variables, functions, loops, error messages). "Runs vs correct" case study (t-test vs Mann-Whitney on Likert data). Readings: Mineault (2026) Claude Code for Scientists, Dataquest (2025) Claude Code for Data Scientists, Cheng, Li & Bing (2023) "Is GPT-4 a Good Data Analyst?", Wickham, Çetinkaya-Rundel & Grolemund (2023) R4DS 2e, Hong et al. (2024) Data Interpreter.
2. **AI-Assisted Data Analysis in Practice** — Data cleaning with AI (strengths, blind spots, silent fixes danger, transformation logs, before-and-after checks). Exploratory data analysis (promise vs reality, 4-step EDA walkthrough with South African survey example). The silent error problem (6 types: wrong variable, off-by-one time series, incorrect missing data, wrong statistical test, grouping/aggregation errors, data leakage). Domain expertise as essential complement (spurious correlations via tylervigen.com, Simpson's paradox, overfitting, confounding variables). Statistical pitfalls AI introduces (correlation≠causation, multiple comparisons, cherry-picking, p-hacking, garden of forking paths). Kapoor & Narayanan (2023) "Leakage and the Reproducibility Crisis" as key reading. Supplementary: Narayanan & Kapoor normaltech.ai (formerly AI Snake Oil), Mollick's One Useful Thing.
3. **Visualization with AI** — What AI can generate (Claude Code/matplotlib, ChatGPT Code Interpreter, LIDA/Dibia 2023, Google Colab AI). Six good visualisation principles AI often violates (misleading axes, poor colours, overplotting, wrong chart type, missing context, chartjunk/Tufte). Help vs mislead (default settings trap, publication quality as different standard). Accessibility (colourblind-safe palettes: ColorBrewer, viridis, Okabe-Ito; redundant encoding; alt text for figures; 8% colour vision deficiency stat). Five-step practical workflow (explore → audit → fix accessibility → polish → verify). Readings: Dibia (2023) LIDA, Wilke (2019) Fundamentals of Data Visualization (free online), ColorBrewer 2.0, Coblis simulator.
4. **Verification of AI-Generated Code** — Why verification matters more than generation. Reading code you didn't write as essential skill. Practical verification techniques (test with known data, edge cases, sanity checks, comparison with established tools, "change one thing" test). Six common failure patterns (wrong library/function, incorrect statistical assumptions, off-by-one errors, silent data type conversions, scope/variable shadowing, incorrect aggregation). Building a verification habit (5-step checklist). Version control for reproducibility. Readings: Cheng, Li & Bing (2023), Wickham et al. R4DS 2e, software testing resources.
5. **Building Your Data Analysis Workflow** — Five-stage workflow (question → data preparation → analysis → verification → interpretation). Prompt templates for common tasks (loading data, summary statistics, group comparisons, regression, visualisation). Claude Code + Jupyter notebook side-by-side workflow adapted from Mineault (2026). CLAUDE.md for project context. When to use AI vs established statistical packages. Reproducibility and documentation. Privacy considerations (what data can you paste into AI tools? UCT data classification, anonymisation, institutional agreements). Readings: Mineault (2026), Dataquest (2025).
6. **Hands-On Activities and Assessment** — Activity 1: Data Cleaning Challenge (messy dataset with planted errors, use AI to clean, document every change). Activity 2: Code Generation and Verification (describe analysis in plain English, AI generates code, critically verify outputs against known answers). Activity 3: Interpretation Challenge (AI-generated analyses, some correct, some with classic statistical errors — identify which). Weekly assessment: Use AI to analyse a dataset relevant to your research, submit code, outputs, and critical commentary (1000 words). Full week summary with forward pointer to Week 8.

## Week 8 Content Details

Week 8 has 6 core sub-lessons covering multimodal AI (vision, documents, audio/transcription, video).

**Naming convention for model references throughout Week 8 (the "version-lock-in fix"):** capability discussions use family names — `Claude (family)`, `GPT (family)`, `Gemini (family)` (with the parenthetical literal). Where a tier matters for a capability claim, use `Gemini's Pro tier currently…`. Specific model names (e.g. GPT-4o, Claude 3.5 Sonnet, GPT-4V) are kept ONLY in historical citations of papers that tested those specific models. Open-source models named for their version (Whisper large-v3, olmOCR-2-7B) keep the version because the version IS the name. This rule was established to prevent the materials from going stale every time a new model release ships.

1. **What Multimodal AI Can See, Hear, and Read** — The four modalities (images, documents, audio, video) with capability overview. Tool landscape table uses family names (Claude, GPT, Gemini, plus Whisper large-v3). Gemini Pro tier context limits: ~1 hr video at standard resolution / ~8.5 hrs audio-only (durations depend on FPS and resolution). Whisper large-v3: ~2.0% WER on clean audio. Reading vs. understanding distinction as week's central frame. "The Real-World Chart Gap" case study (renamed from "The 47% Problem" — frontier scores have moved since 2024 so the historical framing no longer matches what students will reproduce): CharXiv published 2024 baseline of GPT-4o 47.1% vs human 80.5%, scores have improved substantially since but the underlying pattern (real-world performance lags simplified benchmarks) is durable. VLMs Are Blind (ACCV 2024, arXiv:2407.06581): 4 state-of-the-art VLMs, 7 geometric task categories, 58.07% average accuracy. Readings: CharXiv (arXiv:2406.18521), VLMs Are Blind (arXiv:2407.06581).
2. **AI and Scientific Images** — What VLMs can and cannot do with scientific figures. The "description vs. value-extraction" heuristic: AI is reliable on description tasks (what does this image show, qualitatively?), unreliable on value-extraction tasks (what is the exact value at this point?). CharXiv table presents 2024 baselines explicitly as historical benchmarks (GPT-4o 47.1%, Claude 3.5 Sonnet ~60%, AI2D 94.7%) with caveat that frontier scores have improved. Jin et al. (npj Digital Medicine, July 2024): GPT-4V 81.6% vs 77.8% physicians, 35.5% flawed reasoning, ~27% image comprehension errors — the correct-answer-wrong-reasoning problem. Domain-specific image AI section restructured to give a fair landscape view: foundation models (Prithvi/Prithvi-EO-2.0, Clay, SatMAE, Scale-MAE, SatCLIP), frameworks (TerraTorch, torchgeo, geoai-py), cloud APIs (Google Geospatial Reasoning with Gemini). "Where to start" recommendation: TerraTorch + Prithvi-EO-2.0 for research-grade Earth observation. Mujahid et al. (2024, *Sci Rep*): 97–99% on the NIH thin-blood-smear malaria dataset (curated benchmark, not field deployment, no formal pathologist comparison). Bias section uses NIST FRVT figures (10–100× false-positive factor, ~3× false-negative factor for African/East Asian subjects in 1:1 verification) rather than the previously-unverified "25–35%" gap. Readings: CharXiv, VLMs Are Blind, Jin et al. npj Digital Medicine.
3. **Document Intelligence** — PDF parsing landscape: Docling (IBM, strong table and formula extraction), LlamaParse, Marker, Unstructured, Azure Document Intelligence. OmniDocBench (CVPR 2025) noted as saturated: top tools now exceed 94% on the original benchmark; v1.6 hard subset released. Three PDF types (native, scanned, mixed). Complex table problem: merged cells, multi-level headers, footnote associations, reading order. Lost in the Middle framed as a foundational 2024 finding that frontier long-context models have partially addressed but not eliminated. Handwriting OCR: ~96–98% character-level accuracy on IAM/RIMES benchmarks with frontier VLMs (GPT-4o ~1.69% CER on RIMES; Crosilla et al., 2025, arXiv:2503.15195); 80–95% on noisy/historical/cursive content; olmOCR-2-7B (arXiv:2510.19817) noted as a specialised open option. Multi-language OCR limitations for African scripts.
4. **Transcription and Audio Analysis** — Whisper large-v3: ~2.0% WER on LibriSpeech clean (with explanatory note that the commonly-quoted 2.7% figure is from large-v2). WER benchmarks for African languages from Nahabwe et al. (2025, Deep Learning Indaba 2025, arXiv:2512.10968) — explicitly labelled as W2v-BERT model with 1 hour vs 50 hours of fine-tuning (not generic baseline). Other models in the same study reach comparable or better WER (e.g. Whisper Afrikaans 50h ≈ 2.11%). Koenecke et al. (FAccT 2024, "Careless Whisper"): 38% of hallucinations in clinical transcripts involved explicit harms. Investigative reporting (AP, TechCrunch 2024): Whisper hallucinated in ~80% of public meeting transcriptions tested. AfriSpeech-Dialog (NAACL 2025): African-accented English conversation benchmark (not indigenous languages). Intron Sahara v2 (2026): 57 languages total (24 newly added in v2), 500+ accents. PazaBench (Microsoft): 39 languages, 52 models. CAAI (Conversational Analysis with AI) framework (Friese, 2025, SSRN 5232579) used for the qualitative analysis workflow section. Privacy/data governance three-point check (institutional policy, ethics approval, consent forms).
5. **Video and Multimodal Workflows** — Gemini's current Pro tier video capabilities (~1 hr at standard settings, longer at low FPS, ~8.5 hrs audio-only). Native multimodal vs. text-centric architecture distinction (Gemini and GPT family natively multimodal; current Claude versions text-centric, requires transcription bridge for audio/video). Liu et al. "Lost in the Middle" (TACL 2024, correct authors: Liu, N.F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P.) framed as a foundational finding partially addressed by frontier models. Compounded failure modes specific to video (image errors × audio errors × language errors). Temporal hallucination warning. Practical workflow: structured modality first, transcription as text bridge, explicit context, cross-check across modalities, verify temporal claims directly.
6. **Hands-On Activities and Assessment** — **Activity 1: Figure Analysis Challenge.** Students choose 3 scientific figures of increasing complexity from their own field, run them through Claude or GPT, evaluate description vs. value-extraction accuracy, check the AI's reasoning against the actual image. **Activity 2: Self-Recorded Transcription Test ("The Hallucination Hunt").** Students write their own ~3-minute script with deliberate challenge features (10+ specific categories: technical jargon, homophones, proper nouns, acronyms, numbers, second-language sentences), record themselves, transcribe with Whisper (Hugging Face Space or Colab), compare to their own script (their ground truth), categorise errors, calculate their personal WER. Pedagogical rationale: students must measure Whisper's accent performance on their own voice rather than read a published number. **Activity 3: COPCOV Document Extraction.** Two tables from the same open-access PLOS Medicine paper (COPCOV trial, 10.1371/journal.pmed.1004428): Table 1 (long, section headers, mid-table page break, embedded italics) and Table 2 (multi-line cell content, section dividers, footnote markers, mixed CI delimiters). Same tool used for both, isolating effect of structural complexity. Weekly assessment: Multimodal Analysis Report (~1000 words) — see "Week 8 Assessment" section below.

### Week 8 Assessment — Assignment 4 in Amathuba

Created in the Amathuba dropbox as **"Assignment 4 - Multimodal Analysis Report"** (continues the existing numbering from Assignments 1–3). 100 points, In Grade Book. Due 11 May 2026, 11:59 PM. Available 27 April 2026 → 27 October 2026 (six-month submission window matching Assignment 2/3 pattern). File submission, Visible. No rubric attached (matches Assignment 3 convention). Instructions structured exactly like Assignment 3: H4 heading with word count, opening rationale paragraph, "Requirements" H4 with numbered list, sub-bullets where needed, then Submission and Grading sections. Six requirements: choose materials (≥2 modalities), apply tools, document ≥3 specific errors with concrete examples (most heavily weighted at 30%), document verification approach, reflect on workflow implications, include Disclosure Statement (referencing Lesson 6 Sub-Lesson 5). Grading split: tool use 25%, error documentation 30%, verification practice 25%, workflow integration + disclosure 20%.

## Week 9 Content Details

Week 9 has 6 core sub-lessons. The week's central pedagogical move is the **trajectory frame**: every claim about AI capability has an implicit "as of [date]", and reading the AI literature critically means making that explicit. The frame deliberately replaces the static "AI limitations" framing because that framing goes stale every six months.

1. **The Trajectory of LLM Capabilities** — Seven-year sweep from GPT-2 (2019, incoherent past a paragraph) through GPT-3 (2020), ChatGPT/GPT-4 (2022–23), GPT-4o/Claude 3.5/Gemini 1.5 (2024), Claude 4/GPT-5/Gemini 2.5 (2025), to the May 2026 frontier. Detailed table of current frontier closed-weights models (Mythos preview, Opus 4.7, GPT-5.5/Pro, Gemini 3.1 Pro, Muse Spark) and open-weights models (DeepSeek V4 Pro/Flash). Benchmark literacy section covering FrontierMath, GPQA Diamond, SWE-bench Verified, AIME 2026, MCP-Atlas, HLE, Codeforces. Centrepiece reading: Gowers (8 May 2026) blog post on ChatGPT 5.5 Pro extending bounds in additive number theory.
2. **Three Categories of Failure: Patched, Reduced, Structural** — A taxonomy that survives the next model release. (a) Patched: reversal curse (Berglund et al. 2023), basic arithmetic and short-form reasoning (Frieder et al. 2023), hallucinated code on common tasks. (b) Reduced but persistent: hallucinated citations (Magesh, Chelli, Linardon — Week 5 evidence still applies), sycophancy (Sharma et al. 2023, plus Anthropic's persona-vector interpretability work), calibration. (c) Structural and likely persistent: hallucination as statistical pressure (Kalai et al. 2025, *Why Language Models Hallucinate*, OpenAI), pattern completion vs understanding, long-tail problem, compositional brittleness, domain-specific failure modes, training data dependence. Closes with a diagnostic table mapping observed failures to categories with action.
3. **Where AI Is Now Genuinely Strong** — Counterbalances the limitations narrative with current capability evidence. Mathematics: Gowers (revisited), Erdős Problem #1196 (GPT-5.4 Pro April 2026, with peer-reviewed-track follow-up Alexeev/Barreto/Li/Lichtman/Price/Shah/Tang/Tao May 2026 arXiv:2605.00301), Erdős #728 with Tao's "anatomy of integers and Markov process theory" quote, 15 problems open→solved since Jan 2026, AlphaEvolve paper (Georgiev/Gómez-Serrano/Tao/Wagner Nov 2025 arXiv:2511.02864), IMO 2025 gold (Gemini Deep Think, 5/6, 35/42, end-to-end natural language). Theoretical physics: gluon amplitudes paper (Guevara/Lupsasca/Skinner/Strominger/Weil Feb 2026 arXiv:2602.12176, with paper's own GPT-5.2-Pro credit), graviton extension (March 2026, OpenAI CDN), cosmic-string radiation (Brenner/Cohen-Addad/Woodruff March 2026 arXiv:2603.04735, neuro-symbolic Gemini Deep Think + tree search), quantum many-body (Pan et al. 2025, *Comm. Phys.*, GPT-4 13/15 Hartree-Fock derivations). Adjacent paradigms: AI-Newton symbolic regression (Fang et al. April 2025), physics-tailored ML in dusty plasmas (Yu/Abdelaleem/Nemenman/Burton 2025, *PNAS*, R²≈0.99). Autonomous research: AI Scientist v2 *Nature* paper (Lu et al. March 2026, score 6.33 at ICLR ICBINB). Code/writing/multimodal pointers to Weeks 7/6/8. **Mandatory caveats** at end: selection bias, human collaboration was essential in every case, human verification was always required, several papers are still preprints.
4. **Illusions of Understanding** — Centrepiece is Messeri & Crockett (2024, *Nature* 627, 49–58). Four illusions: explanatory breadth, exploratory objectivity, monocultures of knowing, doing more but understanding less. Argues the illusions argument is **more** important now, not less, because surface fluency of frontier models masks remaining gaps more effectively. Calibration trap explained. Connecting-weeks table maps Week 5/6/7/8 evidence to specific illusions. Suggested practices for resisting each illusion.
5. **Verification Protocols for a Moving Target** — Two layers. Layer 1 (verifying outputs): known-answer testing, adversarial prompting, cross-model triangulation, "teach it back" test, manual spot-checks, citation verification (Week 5 framework), reproducibility testing, domain-expert spot-checks. Layer 2 (verifying capability claims): the dated-research three-question check (which model/version, when tested, has anyone retested?). Concrete worked example with Berglund et al. reversal curse. Section on verification habits (workflow component, retest cadence on new model release, document what you find). Closes with the course's own verification practice — examples of errors caught by verify-references in earlier weeks (Gupta arXiv ID, Tamburrino→Wright, Anthony→Luccioni, Humbel→Crosilla, Lund DOI, Mollick post, Nature title, Okolo URL, ICRC URL).
6. **Hands-On Activities and Assessment** — Three activities. **Activity 1 (Hallucination Hunting):** test current frontier in your domain, document ≥5 distinct failures, categorise per 9.2 taxonomy. **Activity 2 (Capability Hunting):** test tasks you assumed AI couldn't do, with cross-model triangulation, document ≥3 capability tests. **Activity 3 (Trajectory Tracking):** pick a 2023–24 published claim "AI cannot do X", retest with current frontier, 400–600 word write-up. **Final assessment:** *AI in [your field] — May 2026 Snapshot*, ~1500 words, structured report explicitly acknowledging its own future obsolescence with retest-cadence recommendation. Grading split: capability 25%, limitations 25%, methodology 25%, staleness reflection 15%, disclosure 10%.

### Week 9 Key Sources

- Gowers, T. (8 May 2026). *A recent experience with ChatGPT 5.5 Pro.* Blog. (Centrepiece)
- Messeri, L. & Crockett, M. J. (2024). *Artificial intelligence and illusions of understanding in scientific research.* *Nature* 627, 49–58. DOI:10.1038/s41586-024-07146-0. (9.4 centrepiece)
- Kalai, A. T., Nachum, O., Vempala, S. S., & Zhang, E. (Sept 2025). *Why Language Models Hallucinate.* arXiv:2509.04664 (OpenAI)
- Guevara, A., Lupsasca, A., Skinner, D., Strominger, A., & Weil, K. (12 Feb 2026). *Single-minus gluon tree amplitudes are nonzero.* arXiv:2602.12176
- Alexeev, B., Barreto, K., Li, Y., Lichtman, J. D., Price, L., Shah, J. I., Tang, Q., & Tao, T. (3 May 2026). *Primitive sets and von Mangoldt chains: Erdős Problem #1196 and beyond.* arXiv:2605.00301
- Georgiev, B., Gómez-Serrano, J., Tao, T., & Wagner, A. Z. (3 Nov 2025). *Mathematical exploration and discovery at scale.* arXiv:2511.02864
- Brenner, M. P., Cohen-Addad, V., & Woodruff, D. (5 March 2026). *Solving an Open Problem in Theoretical Physics using AI-Assisted Discovery.* arXiv:2603.04735
- Pan, H., Mudur, N., Taranto, W., Tikhanovskaya, M., Venugopalan, S., Bahri, Y., Brenner, M. P., & Kim, E.-A. (2025). *Quantum many-body physics calculations with large language models.* *Communications Physics*. DOI:10.1038/s42005-025-01956-y
- Yu, W., Abdelaleem, E., Nemenman, I., & Burton, J. C. (2025). *Physics-tailored machine learning reveals unexpected physics in dusty plasmas.* *PNAS* 122(31), e2505725122
- Fang, Y.-L., Jian, D.-S., Li, X., & Ma, Y.-Q. (April 2025). *AI-Newton.* arXiv:2504.01538
- Lu, C., Lu, C., Lange, R. T., et al. (26 March 2026). *Towards end-to-end automation of AI research.* *Nature* 651, 914–919
- Berglund, L., Tong, M., Kaufmann, M., et al. (Sept 2023). *The Reversal Curse.* arXiv:2309.12288 (cited as historical landmark)
- Sharma, M., Tong, M., Korbak, T., et al. (Oct 2023). *Towards Understanding Sycophancy in Language Models.* arXiv:2310.13548 / ICLR 2024 (cited as historical, with note on 2024–25 mitigations)
- Frieder, S., Pinchetti, L., Chevalier, A., Griffiths, R.-R., Salvatori, T., Lukasiewicz, T., Petersen, P. C., & Berner, J. (Jan 2023). *Mathematical Capabilities of ChatGPT.* arXiv:2301.13867 / NeurIPS 2023 D&B (cited as historical baseline, thoroughly superseded)
- Kapoor, S. & Narayanan, A. *AI Snake Oil* (Princeton UP, 2024); blog at *normaltech.ai*

### Week 9 Build Notes

- Built using a Python generator script at `Week 9/build_week9.py` containing all sub-lesson content as data; re-run after content edits. This pattern lets the inline CSS template stay consistent across pages and makes systematic edits trivial.
- Frontier-model snapshot (Mythos, Opus 4.7, GPT-5.5/Pro, DeepSeek V4 Pro etc.) is explicitly time-stamped May 2026 — the table will date and that's part of the lesson.
- verify-references caught 2 issues during build: "Kosmyna et al. (2026)" (was 2025; arXiv:2506.08872 is June 2025) and "Jin et al. ~27% via flawed reasoning" (was 35.5% flawed reasoning; 27% was the image-comprehension errors figure). Both fixed.
- **Pattern note for future weeks**: this is the first week to use a Python generator rather than per-page hand-written HTML. The pattern is much faster for content-heavy weeks and worth replicating for Weeks 10–12.

## GitHub Pages Site

The public course website is served from the `docs/` folder on the `main` branch via GitHub Pages.

- **URL:** https://shocklab.github.io/Generative-AI-in-research-course/
- **Source:** `docs/` folder — contains Amathuba-exported (live/edited) versions of all lesson pages, organised into week subfolders
- **index.html** — Landing page with UCT styling, links to all built weeks, "coming soon" placeholders for future weeks
- **AI Content Disclaimer** — `docs/course-introduction/AI Content Disclaimer.html` — explains AI-assisted creation, known risks, contact for corrections
- **Back navigation** — Every lesson page has a "Back to Contents" bar at the top linking to `index.html`
- **Course Orientation pages** use Brightspace/Bootstrap templates (different from Week 1-5 inline CSS pages). Their `/shared/HTML-Template-Library/` CSS references won't resolve on GitHub Pages — the content is still readable but styling is limited
- **When adding new weeks:** copy Amathuba-exported files to `docs/week-N/`, add back-nav, update `docs/index.html` links, and change the "coming soon" placeholder to active links

## Notes

- Week 3 folder is lowercase (`week 3`); other weeks use title case (`Week 1`, `Week 2`, `Week 4`)
- **Week 3 key stat to include:** 1 month of heavy Claude Code usage ≈ 30–40 kWh ≈ driving ~150 km in a car
- The course has a strong emphasis on African context (ubuntu ethics, AU AI strategy, South African grid, RIA Just AI Framework, Esethu Framework)
- Week 4 Sub-Lesson 2 integrates the RIA Just AI Framework of Inquiry (Chetty & Sey, 2025) alongside ubuntu philosophy
- Week 4 Sub-Lesson 2 includes the Esethu Framework (Rajab et al., 2025) as a case study on data sovereignty for low-resource languages
- Key external links in Week 4: Mhlambi paper (perma.cc/Q5ZL-TTD8), Birhane website (abebabirhane.com), RIA Just AI Framework (researchictafrica.net), Esethu Framework (arxiv.org/abs/2502.15916), UCT Ethics Lab (health.uct.ac.za/ethics-lab), Global Center on AI Governance (globalcenter.ai)
- Week 5 introduces new CSS components: `.prompt-example` (monospace prompt boxes), `.prompt-label` (blue label badges), `.code-block` (dark terminal-style block), `.level-card` + `.level-tag` (level summary cards), `.tool-card` with pricing badges and verdict boxes
- Week 5 Sub-Lesson 5 (Claude workflow) is NEW content not in the original lesson plan — added to cover Claude skills, CLAUDE.md, and personalised research workflows
- Week 5 CSS template source: `Week 5/Building Your Research Workflow with Claude.html` (widest Week 5 component set)
- Key external tool links in Week 5: Semantic Scholar (semanticscholar.org), ResearchRabbit (researchrabbit.ai), Connected Papers (connectedpapers.com), NotebookLM (notebooklm.google.com), Elicit (elicit.com), Consensus (consensus.app), Scite.ai (scite.ai), SciSpace (scispace.com), Litmaps (litmaps.com), Retraction Watch (retractionwatch.com)
- **CSS lesson learned (Week 5):** `.step-list` must use `> li` direct child selectors to prevent nested lists from inheriting the counter and blue circle styling. Fixed in Sub-Lesson 6; apply same pattern in future weeks when nesting lists inside step-list items.
- Week 5 Sub-Lesson 4 hallucination statistics were all verified against primary sources and corrected. Key sources: Stanford HAI (hai.stanford.edu), Chelli et al. 2024 (jmir.org/2024/1/e53164), Linardon et al. 2025 (mental.jmir.org/2025/1/e80371), GPTZero NeurIPS analysis (gptzero.me/news/neurips/), Niimi 2025 (arxiv.org/html/2510.25378)
- Week 5 assessment is 1000 words (not 2000) — changed from original lesson plan to better suit scope
- Week 6 folds in research ideation content from original lesson plan's Week 5 (prompt engineering, brainstorming, idea generation)
- Week 6 verification caught 5 hallucinated author names (Girotra co-authors, PLOS Biology authors, CHI paper authors), 1 wrong arXiv URL, 1 wrong statistic (2.5-3x → 1.5x writing time), 1 outdated policy (Science/AAAS), and 1 outdated fact (SA languages 11→12)
- Week 6 Sub-Lesson 4 includes nuanced discussion of AI and data: modern models push back rather than fabricate, risks shift to over-claiming and silent gap-filling. Also covers "when AI knows more than you" (both positive and dangerous sides)
- Week 6 Sub-Lesson 5 includes warning about AI subtly changing arguments even when instructed to preserve meaning
- Week 6 Supplementary page (AI review) is based on the paper-review skill at `.claude/skills/paper-review/SKILL.md`
- Week 6 Sub-Lesson 4 notes that course materials themselves are a "Template 3" (substantial AI use) example
- Key journal policy links in Week 6: Science (science.org/content/page/science-journals-editorial-policies), Nature (nature.com/nature-portfolio/editorial-policies/ai), Elsevier (elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals), IEEE (journals.ieeeauthorcenter.ieee.org), ACM (acm.org/publications/policies/new-acm-policy-on-authorship), COPE (publicationethics.org/guidance/cope-position/authorship-and-ai-tools)
- Week 6 assessment is 800 words (not 2000 from original plan)
- Week 7 merges original Weeks 7 (Data Analysis) and 8 (Coding/Computational Research) — they overlap too heavily to justify separate weeks
- Week 7 introduces `.code-block` CSS component (dark terminal-style) in Sub-Lesson 5 for project structure examples
- Week 7 verification caught: wrong Cheng et al. authors (fixed to Cheng, L., Li, X., & Bing, L.), missing R4DS co-author (added Çetinkaya-Rundel), Mineault year wrong (2025→2026), aisnakeoil.com redirect to normaltech.ai, hallucinated Mollick post title
- Week 7 key external links: Mineault (neuroai.science/p/claude-code-for-scientists), Dataquest Claude Code guide, Cheng et al. (arxiv.org/abs/2305.15038), R4DS (r4ds.hadley.nz), Hong et al. (arxiv.org/abs/2402.18679), Kapoor & Narayanan (doi.org/10.1016/j.patter.2023.100804), Tyler Vigen (tylervigen.com/spurious-correlations), Dibia LIDA (arxiv.org/abs/2303.02927), Wilke (clauswilke.com/dataviz), ColorBrewer (colorbrewer2.org), Narayanan & Kapoor blog (normaltech.ai, formerly aisnakeoil.com), Mollick (oneusefulthing.org)
- Week 7 assessment is 1000 words (critical commentary on AI-assisted data analysis)
- Week 7 Sub-Lesson 2 has the most important pedagogical content: the "silent error problem" — code that runs without errors but produces wrong results. This is the central risk message of the entire week
- Week 7 Sub-Lesson 3 covers accessibility as non-optional (colourblind-safe palettes, redundant encoding, alt text) — 8% of men have colour vision deficiency
- Week 7 Sub-Lesson 5 covers privacy/data classification for AI tools — important for researchers handling sensitive data
- Week 8 verification (multiple passes) caught and fixed: "Jiang et al." → "Jin et al." (4 occurrences in Sub-Lesson 2), wrong paper title for Jin et al., image comprehension error rate "exceeded 20%" → "~27%", Claude 3.5 Sonnet CharXiv score "~40-45%" → "~60%", "7 major models" → "4 state-of-the-art VLMs", Docling/Unstructured specific accuracy % not in OmniDocBench paper (replaced with qualitative ratings), Whisper large-v3 WER "2.7%" → "~2.0%" (2.7% is large-v2), African WER table headers clarified (W2v-BERT baseline, not Whisper), AfriSpeech-Dialog described as African-accented English (not indigenous languages), Liu et al. fabricated co-author removed, Gemini 2.5 Pro video/audio limits corrected (~1hr video / ~8.5hrs audio, not 2hr/19hr), VLMs Are Blind arXiv ID corrected (2407.06581 not 2407.06217), Nahabwe et al. year corrected 2024 → 2025 with W2v-BERT specificity, "CAAI" framework expansion corrected to "Conversational Analysis with AI" (Friese 2025) not "Computer-Assisted AI Interview analysis", Intron Sahara language count 24 → 57, malaria 97.5% pathologist comparison removed (no such study), 25–35% facial-recognition gap replaced with NIST FRVT figures, handwriting OCR 90–95% tightened to 96–98% on IAM/RIMES with Crosilla et al. citation, GeoAI restructured to fair landscape (Prithvi/Clay/SatMAE/Scale-MAE/SatCLIP foundation models + TerraTorch/torchgeo/geoai-py frameworks + Google Geospatial Reasoning APIs)
- **Week 8 model-version genericisation rule:** capability discussions use family names — `Claude (family)`, `GPT (family)`, `Gemini (family)` (with parenthetical literal). Tier-specific claims use `Gemini's Pro tier currently…`. Specific model names kept ONLY in historical citations of papers that tested those specific models. Open-source models named for their version (Whisper large-v3, olmOCR-2-7B) keep the version. Apply this same rule to future weeks.
- Week 8 "47% Problem" branding replaced with "The Real-World Chart Gap" — frontier scores have moved since 2024 so the original framing no longer matches what students will reproduce. The 2024 numbers (GPT-4o 47.1%, Claude 3.5 Sonnet ~60%, human 80.5%) are presented explicitly as historical baselines.
- Week 8 Sub-Lesson 1 ToC summary list was originally inconsistent with the actual sub-lesson titles (said "Documents and Tables", "Audio and Transcription", "Video Analysis"). Fixed to match actual titles ("Document Intelligence", "Transcription and Audio Analysis", "Video and Multimodal Workflows") and Sub-Lesson 6 added.
- Week 8 key external links: CharXiv (arxiv.org/abs/2406.18521), VLMs Are Blind (arxiv.org/abs/2407.06581), Jin et al. npj Digital Medicine (nature.com/articles/s41746-024-01185-7), OmniDocBench (arxiv.org/abs/2412.07626), Koenecke et al. FAccT 2024 (dl.acm.org/doi/10.1145/3630106.3658975), Liu et al. TACL 2024 (doi.org/10.1162/tacl_a_00638), Nahabwe et al. (arxiv.org/abs/2512.10968), Crosilla et al. (arxiv.org/abs/2503.15195), olmOCR-2 (arxiv.org/abs/2510.19817), Mujahid et al. (nature.com/articles/s41598-024-63831-0), Friese CAAI (papers.ssrn.com/sol3/papers.cfm?abstract_id=5232579), Intron Sahara v2, PazaBench, NIST FRVT (pages.nist.gov/frvt/html/frvt_demographics.html), TerraTorch (IBM), torchgeo (Microsoft), geoai-py (opengeos/geoai)
- Week 8 assessment: Assignment 4 - Multimodal Analysis Report. 1000 words, 100 points, due 11 May 2026, available until 27 October 2026. Created in Amathuba dropbox following Assignment 3's H4-headings + numbered-Requirements pattern. Includes Disclosure Statement requirement that ties back to Lesson 6 Sub-Lesson 5 (Building Your AI Writing Workflow).
- Week 8 Amathuba upload: all 6 sub-lesson pages (3985954–3985966) live in unit 3985951, all set Visible. Assignment 4 dropbox live and Visible. The standalone Table of Contents page from the source folder is NOT uploaded to Amathuba — Amathuba's left sidebar serves that role inside the unit. The ToC stays in the GitHub source for the docs/ site only.
- Week 8 Activity 2 redesign worth carrying forward: instead of providing audio + transcript, students record themselves reading a script with deliberate challenge features (jargon, homophones, code-switching) and compare Whisper output against their own script. Lets students measure Whisper accent performance on their own voice rather than read a published number — directly addresses the South African research context the lesson is anchored in.
