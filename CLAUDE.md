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
| 10 | Agentic AI, RAG & Advanced Research Tools | Built |
| 11 | Future of AI in Research & Africa's Sovereign AI Capacity | Built (6 sub-lessons) |
| 12 | Integrative Capstone (3-hour solo activity, brief inside the Week 12 page) | Built |

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

Week 9/          (Critical Evaluation & Limitations of AI)
  Table of Contents.html
  The Trajectory of LLM Capabilities.html
  Three Categories of Failure.html
  Where AI Is Now Genuinely Strong.html
  Illusions of Understanding.html
  Verification Protocols for a Moving Target.html
  Hands-On Activities and Assessment.html
  build_week9.py    (Python generator — style in <head>, pretty-printed CSS)

Week 10/         (Agentic AI, RAG & Advanced Research Tools)
  Table of Contents.html
  What Agents Are and Whats New in 2026.html
  Failure Modes for Long-Horizon Tasks.html
  The Current Tool Landscape and MCP.html
  RAG in 2026.html
  Advanced Research Tools - A Curated Tour.html
  Hands-On Activities and Assessment.html
  build_week10.py    (Python generator, mirrors build_week9.py)
  OUTLINE.md         (research/discovery outline used to draft the week)

Week 11/         (Future of AI in Research & Africa's Sovereign AI Capacity)
  Table of Contents.html
  What the Future of AI in Research Might Look Like.html
  Speculative Futures - A Reading Guide.html
  The Shifting Research Landscape.html
  Sovereign AI Capacity and Why Compute Is the Floor.html
  Data Languages and African Model-Building.html
  Policy Institutions and Talent.html
  build_week11.py    (Python generator, mirrors build_week9/10.py)
  OUTLINE.md         (research/discovery outline used to draft the week)

Week 12/         (Integrative Capstone)
  Table of Contents.html
  Synthesis and the Integrative Capstone.html    (contains the full capstone brief)
  build_week12.py    (Python generator, mirrors build_week11.py)

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

## Per-Week Content Details

Detailed content descriptions, key sources, build notes, verification logs, and lessons learned for each built week are in **[WEEK-BUILD-NOTES.md](WEEK-BUILD-NOTES.md)**. Read it when working on a specific week's content.

Key conventions that apply across weeks:
- **Model-version genericisation (from Week 8 onward):** capability discussions use family names — `Claude (family)`, `GPT (family)`, `Gemini (family)`. Specific model names kept ONLY in historical citations. Open-source models named for their version (Whisper large-v3) keep it.
- **Week 9 build pattern:** Python generator script (`Week 9/build_week9.py`) — faster for content-heavy weeks. Replicated successfully for Week 10 and Week 11.
- **Week 11 strong African emphasis:** the four sub-lessons 11.4–11.7 treat the African intellectual tradition as the analytical home base, with Northern voices treated as foils. African voices include Mhlambi, Effoduh, Esethu Framework, Mutung'u et al., CARE Principles (Gaborone 2018), Pelonomi Moiloa (Lelapa), Vukosi Marivate (UP/Lelapa/Indaba/Masakhane), Anri Lombard (UCT, MzansiLM lead).
- **Week 12 is a 3-hour solo capstone** with the brief living entirely inside the Week 12 page (six-prompt structured pitch + solo self-critique = 600 words). No separate document, no live session.

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

- Week 3 folder is lowercase (`week 3`); other weeks use title case
- The course has a strong emphasis on African context (ubuntu ethics, AU AI strategy, South African grid, RIA Just AI Framework, Esethu Framework)
- **CSS lesson (Week 5+):** `.step-list` must use `> li` direct child selectors to prevent nested lists from inheriting counter/circle styling
