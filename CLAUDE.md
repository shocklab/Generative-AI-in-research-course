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
| 8 | Multimodal AI for Research | Built |
| 9 | Critical Evaluation & Limitations of AI | Built |
| 10 | Agentic AI, RAG & Advanced Research Tools | Built |
| 11 | Future of AI in Research & Africa's Sovereign AI Capacity | Built (6 sub-lessons) |
| 12 | Integrative Capstone (3-hour solo activity, brief inside the Week 12 page) | Built |

**Note on restructured schedule (Weeks 7-12):** The original Weeks 7 (Data Analysis) and 8 (Coding/Computational Research) were merged into Week 7 because they overlap heavily — data analysis IS coding for most researchers. Original Week 9 (Domain-Specific Applications) content is woven into other weeks as case studies. Original Week 10 (Critical Evaluation/Limitations) was moved to Week 9. This freed a slot for a Multimodal AI week (Week 8) and a Flexible/TBD week. See the plan file at `.claude/plans/goofy-whistling-journal.md` for full rationale.

## Source and build

The repository is where the course is written and published. The public site is GitHub Pages,
served from `docs/` on `main`. The course is not published on Amathuba.

- **`content/` is the source.** One HTML file per page, in `week-1/` to `week-12/`,
  `course-introduction/`, `course-orientation/`, `advanced/` (the Claude Code track) and
  `papers/`, plus `about.html`. `content/index.html` is the sitemap: the order of weeks and
  lessons, the left-hand navigation and the previous/next links all come from it.
- **`redesign/build_site.py` builds `docs/`** from `content/` and `glossary.json`, including the
  glossary page, the papers pages and the About page. From each lesson it takes the `<h1>`, the
  paragraph after it and the `.content` body; nothing outside `.content` reaches the site. The
  builder adds the navigation, the AI-authorship footer and the GoatCounter analytics snippet.
- **Edit `content/` or `build_site.py`, never `docs/`**: the next build overwrites it.
- **Checks after every build:** `redesign/verify_content.py` (every rendered page carries the same
  words as its source; one expected flag on Week 2 "LLM Architecture Deep Dive") and
  `redesign/check_links.py` (internal links).
- **Diagrams** are inline SVG inside `content/` pages, drawn by `redesign/gen_week*.py`,
  `gen_extras.py` and `gen_advanced.py` with `genlib.py`. When a diagram's text changes in
  `content/`, change its script too, or a rerun restores the old text.
- **Publishing:** commit the `content/` change and the rebuilt `docs/` (as separate commits) on a
  branch and open a PR. GitHub Pages deploys when it merges to `main`.
- `add_page_nav.py` and `add_analytics.py` at the root, and `Papers/build_papers_site.py`, write
  into `docs/` from before the builder existed. The builder now does their jobs; do not run them.

## Files

```
content/                         source pages
docs/                            generated site, served by GitHub Pages
redesign/                        site builder, checks and diagram scripts
glossary.json                    glossary terms and definitions, read by the builder
STYLE.md                         course-specific writing rules
WEEK-BUILD-NOTES.md              per-week content notes, key sources and build history
Papers/                          per-week manifests of the papers the course cites
Lesson plans.docx                the original 12-week lesson plans
RIA_JustAI_Framework_Summary.md  summary of the RIA Just AI framework, used in Week 4
.claude/skills/                  verify-references, course-freshness-check
```

## Page structure

Lesson pages in `content/` keep the skeleton they were first written in (an inline `<style>`
block, a header with the week badge and `<h1>`, then the `.content` body). Only the `<h1>`, the
paragraph after it and `.content` reach the site, and the styling comes from the CSS in
`build_site.py`, so the inline `<style>` has no effect. Write new pages in the same shape. Inside
`.content`, use these component classes; the builder styles them:

| Class | Purpose |
|-------|---------|
| `.intro-text` | Box with left border, always the first section ("What We'll Cover") |
| `.section-title` | `h2` section heading; the builder lists these in the page's contents |
| `.card-grid` + `.card` | Grid of cards |
| `.styled-list` | List with custom bullets |
| `.highlight-box` | Call-out for a key point |
| `.warning-box` | Call-out for a caution |
| `.info-box` | Note or tip |
| `.resource-placeholder` | Box for readings and resources |
| `.technical-detail` | Box for detailed content |
| `.comparison-table` | Table with a header row |
| `.case-study` | Scenario box |
| `.decision-framework` | Framework box |
| `.tool-card` | Card for a tool listing |
| `.step-list` | Numbered steps. Uses `> li` direct-child selectors so nested lists inside a step are not numbered |

## Conventions

- All links use `target="_blank" rel="noopener"`
- The builder removes emoji from headings and body text, so pages need none
- Sub-lesson intro paragraphs are conversational, not bullet-point
- The AI-authorship notice is a footer the builder adds to every lesson; a page carries none of its own
- Summary sections use `.intro-text`
- The final sub-lesson of each week provides a full-week summary and "Next week" pointer
- Supplementary pages use `Week X • Supplementary` in the week-badge (not a numbered sub-lesson)

## Build Process for New Weeks

When building a new week's content, follow these steps in order:

1. **Research & plan**: read the lesson plan, research the topic with web searches, propose the structure to the user for approval.
2. **Write the sub-lesson pages** in `content/week-N/`, following "Page structure" above.
3. **Add the week and its lessons to `content/index.html`**, the sitemap the builder reads.
4. **🔴 MANDATORY: run `/verify-references`** on every new page before considering the week complete. It checks every URL, academic citation and statistical claim against primary sources. Experience from Week 5 showed that web search summaries and AI-generated content frequently contain incorrect statistics, hallucinated citation details and broken URLs.
5. **Fix any issues**: present the verification report to the user, get approval, then correct the problems found.
6. **Build and check**: run `redesign/build_site.py`, then `redesign/verify_content.py` and `redesign/check_links.py`.
7. **Open a PR** with the `content/` changes and the rebuilt `docs/`; the site deploys when it merges to `main`.
8. **Update CLAUDE.md and WEEK-BUILD-NOTES.md**: mark the week as Built and add its content notes.

## Key References for Building New Weeks

- **Full page structure:** `content/week-3/What Does AI Actually Consume.html`
- **Case study styling:** `content/week-3/Critical Minerals and AI.html`
- **Wide component set (case studies, comparison tables):** `content/week-4/The Broader Landscape of AI Ethics.html`
- **Lesson plans for all 12 weeks:** `Lesson plans.docx`
- **Reference verification skill:** `.claude/skills/verify-references/SKILL.md`

## Per-Week Content Details

Detailed content descriptions, key sources, build notes, verification logs, and lessons learned for each built week are in **[WEEK-BUILD-NOTES.md](WEEK-BUILD-NOTES.md)**. Read it when working on a specific week's content.

Key conventions that apply across weeks:
- **Model-version genericisation (from Week 8 onward):** capability discussions use family names — `Claude (family)`, `GPT (family)`, `Gemini (family)`. Specific model names kept ONLY in historical citations. Open-source models named for their version (Whisper large-v3) keep it.
- **Weeks 9 to 12** were first generated by `build_weekN.py` scripts, which are no longer in the repository. Edit those weeks in `content/` like the others.
- **Week 11 strong African emphasis:** the four sub-lessons 11.4–11.7 treat the African intellectual tradition as the analytical home base, with Northern voices treated as foils. African voices include Mhlambi, Effoduh, Esethu Framework, Mutung'u et al., CARE Principles (Gaborone 2018), Pelonomi Moiloa (Lelapa), Vukosi Marivate (UP/Lelapa/Indaba/Masakhane), Anri Lombard (UCT, MzansiLM lead).
- **Week 12 is a 3-hour solo capstone** with the brief living entirely inside the Week 12 page (six-prompt structured pitch + solo self-critique = 600 words). No separate document, no live session.

## Notes

- The course has a strong emphasis on African context (ubuntu ethics, AU AI strategy, South African grid, RIA Just AI Framework, Esethu Framework)
- **CSS lesson (Week 5+):** `.step-list` must use `> li` direct child selectors to prevent nested lists from inheriting counter/circle styling
