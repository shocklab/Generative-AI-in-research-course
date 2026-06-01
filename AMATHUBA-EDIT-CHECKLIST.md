# Amathuba surgical-edit checklist — Lessons 1–9

These are the fact/consistency fixes already live on the GitHub Pages site that still need applying to the **Amathuba** copies. The live Amathuba pages have **diverged** from the GitHub `docs/` versions (different titles, H1s, section headings, AI-notice wording — they were edited directly on Amathuba), so **do NOT paste whole pages**. Instead, on each live page's HTML **source editor**, find the OLD text and change only that to NEW. If a diverged page no longer contains the OLD text, skip that item.

Workflow per page: open page → **⋯ → Edit → `</>` (source code)** → find OLD → replace with NEW → Save → Save and Close → reload to eyeball.

Status legend: ☐ to do · ☑ done · ⊘ skipped (text not present on the diverged page)

---

## Lesson 1 — Foundations of Generative AI

### Page: *History of AI* (live title may be "Historical Development of AI / The Evolution of Artificial Intelligence")
- ☐ **McCulloch & Pitts title** — OLD: `A Logical Calculus of Ideas Immanent in Nervous Activity` → NEW: `A Logical Calculus of the Ideas Immanent in Nervous Activity` *(insert "the")*
- ☐ **Amari romanisation** — OLD: `Shin-Ichi Amari` → NEW: `Shun-ichi Amari`
- ☐ **ALPAC/Lighthill misquote** — on the **1966 ALPAC** entry, the quoted line `"In no part of the field have the discoveries made so far produced the major impact that was then promised."` is Lighthill's, not ALPAC's. Replace it with ALPAC's actual finding: *"…concluded there was 'no immediate or predictable prospect of useful machine translation,' finding it slower, less accurate, and roughly twice as expensive as human translation."* (Leave the identical quote on the **1973 Lighthill** entry as-is.)
- ☐ **GPT-4 bar-exam hedge** — OLD: `passed the bar exam in the 90th percentile` → NEW: add a hedge, e.g. `reportedly passed the bar exam near the 90th percentile (a figure later disputed — Martínez (2024) found roughly the 48th percentile on essays and the 68th overall)`. Leave the SAT 1410 figure unchanged.
- ☐ **"fastest-growing" hedge** — OLD: `the fastest-growing consumer application in history.` → NEW: `at the time the fastest-growing consumer application in history (later overtaken, for example by Threads in 2023).`
- ☐ **Deep-learning era range** *(only if present)* — `2010–2017` → `2012–2017`. (May not exist as an explicit range on the live page; skip if absent.)

### Page: *Understanding How Generative AI Works*
- ☐ **Context-window range** — OLD: `typically thousands or tens of thousands of tokens` → NEW: `typically thousands to hundreds of thousands, or even over a million, tokens`
- ☐ **Nano Banana spelling** — OLD: `Nano-Banana` → NEW: `Nano Banana`

### Page: *Current Generative AI Landscape*
- ☐ **Date stamps (×3+)** — `Feb 2026` → `May 2026` (in the title, the "Updated:" banner, and the sub-header).
- ☐ **OpenAI flagship** — OLD: `GPT-5.2 — flagship family … GPT-4o — earlier multimodal model…` → NEW: `GPT-5.5 / GPT-5.5 Pro — flagship family for "work + agents" (May 2026)… GPT-5.2 / GPT-4o — earlier models…` (tops the FrontierMath leaderboard).
- ☐ **Anthropic flagship** — OLD: `Claude Opus 4.6 … Claude Opus 4.5 …` → NEW: `Claude Opus 4.7 — flagship (GA 16 April 2026)…` + `Claude Mythos (preview) — limited research preview (May 2026); leads GPQA Diamond and HLE`.
- ☐ **Google** — OLD: `Gemini 2.5 Pro / 2.5 Flash` → NEW: `Gemini 3.1 Pro / Deep Think` (IMO 2025 gold-level maths).
- ☐ **Kimi** — OLD: `Kimi K2.5 (Moonshot AI) … (Jan 2026)` → NEW: `Kimi K2.6 … (April 2026)` (open-weights MoE ~1T/32B active; near closed-frontier coding).
- ☐ **DeepSeek** — OLD: `DeepSeek (V3/R1; V4/R2 reported)` → NEW: `DeepSeek V4 Pro / V4 Flash` (open-weights MoE; Pro 1.6T/49B, 1M context, MIT licence, April 2026).

---

## Lesson 2 — LLM deep dive

### Page: *LLM Architecture Deep Dive*
- ☐ **Broken arXiv link** — OLD href: `chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://arxiv.org/pdf/1706.03762` → NEW: `https://arxiv.org/abs/1706.03762`
- ☐ **3Blue1Brown name (×2)** — OLD: `3brown1blue` → NEW: `3Blue1Brown`
- ☐ **GPT-4 1.76T hedge** — on the line `When we say "GPT-4 has 1.76 trillion parameters"…`, add that 1.76T is a widely-circulated but unconfirmed third-party estimate, never officially disclosed.
- ☐ **"Current Frontier" box** — OLD (line saying GPT-4o `seems to have been a dense model with around 1T parameters`) → NEW: reframe so it states proprietary frontier-model sizes/architectures are not disclosed and circulating figures are third-party estimates; **Claude → most likely dense** (no number); MoE examples = DeepSeek-V3 (671B/37B, arXiv:2412.19437) & Mixtral; GPT-4 ~1.8T reported MoE (SemiAnalysis); GPT-4o ~200B estimated; **drop the "GPT-5.2 may have over 10T parameters" figure**. *(This is the editorial rewrite — see the GitHub `docs/week-2/LLM Architecture Deep Dive.html` "Current Frontier" box for the exact replacement wording.)*

### Page: *How AI Image Generation Works*
- ☐ **`<title>`** — → `Week 2.4 - How AI Image Generation Works` (if a "Week 2.x" prefix is wanted; the live page title may differ).
- ☐ **AI-notice wording** — OLD: `to improve visual quality and user experience` → NEW: `to improve visual quality and educational experience`

---

## Lesson 3 — Environmental implications

### Page: *Critical Minerals and AI*
- ☐ **E-waste year** — OLD: `~62 million tonnes of e-waste was generated globally in 2023` → NEW: `…in 2022` (Global E-waste Monitor 2024).
- ☐ **Gallium/germanium** — the two are shown as separate July-2023 & August-2023 announcements; reword as a **single** measure: China's MOFCOM Announcement No. 23, **announced 3 July 2023, effective 1 August 2023** (covers both gallium and germanium). Align both table rows.
- ☐ **TSMC share** — OLD: `~54% of global semiconductor foundry revenue overall` → NEW: `~64% … (2024)`

### Page: *Infrastructure, Scale and the Rebound Problem*
- ☐ **Three Mile Island** — OLD: `The plant restarted in September 2024.` → NEW: *"September 2024 marked the announcement, not a restart: the unit — to be renamed the Crane Clean Energy Center — is scheduled to come back online around 2027, after an estimated $1.6 billion refurbishment and pending Nuclear Regulatory Commission approval."*

### Page: *Sustainable AI: What Can Be Done?*
- ☐ **Sub-lesson number** — `<title>` `Week 3.3 - Sustainable AI…` → `Week 3.4 - Sustainable AI…` (Critical Minerals keeps 3.3). *(Only if the live title carries a number.)*

### Page: *The Cost of Every Prompt / What Does AI Actually Consume*
- ☐ **944 Wh household claim** — OLD: `944 Wh is roughly what an average South African household uses in an entire day of electricity consumption.` → NEW: `944 Wh is roughly one-seventh of what an average South African household uses in a day (around 6–7 kWh) — a meaningful amount for a few seconds of video, but still a fraction of daily household use.`

---

## Lesson 4 — Ethical frameworks

### Page: *The Broader Landscape of AI Ethics*
- ☐ **Supplementary relabel** — `<title>` `Week 4.5 - …` → `Week 4 - Supplementary: The Broader Landscape of AI Ethics`; badge `Week 4 • L5` → `Week 4 • Supplementary`. *(Match whatever the live badge currently says.)*

---

## Lesson 5 — AI-assisted literature reviews

### Page: *The Hallucinated Citation Crisis*
- ☐ **Linardon per-topic figures** — OLD: `for binge eating disorder … fabrication rate jumped to 46%, compared to 17% for major depressive disorder` → NEW: `fabrication rates were 28% for binge eating disorder and 29% for body dysmorphic disorder (less familiar topics), compared to just 6% for major depressive disorder`
- ☐ **NeurIPS/ICML/AAAI overreach** — OLD: a clause saying the GPTZero finding extended to `ICML and AAAI` → NEW: remove that clause (the report was NeurIPS-2025-only).

### Page: *Paid Tools and When They Are Worth It*
- ☐ **Scite pricing** *(only if present in rand)* — reconcile `~ZAR 182/month` to `~$12/month` to match the table. *(NB: on the GitHub version this turned out already-USD; check the live page and skip if already $.)*

---

## Lesson 6 — AI for writing, communication & ideation

### Page: *AI Writing Tools — Landscape and Honest Assessment*
- ☐ **SAGE → real journal** — OLD: `SAGE Journals` (Daryani et al. 2026) → NEW: `Policy Insights from the Behavioral and Brain Sciences` (keep title + DOI 10.1177/23727322251406591).
- ☐ **Free-tier cell** — OLD: `Yes (GPT-4o limited)` → NEW: `Yes (usage limits)`
- ☐ **Amano mislink** — the ~50%-more-time stat hyperlink should point to **Amano 2023** `10.1371/journal.pbio.3002184` (not the 2025 `pbio.3003215` "two futures" paper).

### Page: *Research Ideation with AI*
- ☐ **"Nature Communications Psychology" (×3)** — OLD: `Nature Communications Psychology` → NEW: `Communications Psychology` (keep article title + DOI 10.1038/s44271-026-00428-5).
- ☐ **ScienceDirect cited as journal (×2)** — OLD: `ScienceDirect` (the 2025 LLM-homogenisation study) → NEW: `Computers in Human Behavior: Artificial Humans` (Moon, Green & Kushlev 2025; DOI 10.1016/j.chbah.2025.100207).

### Page: *Hands-On Activities and Assessment*
- ☐ **Next-week title** — OLD: `AI for Data Analysis and Visualisation` → NEW: `AI for Data, Code & Computation`

---

## Lesson 7 — AI for data, code & computation

### Page: *Agentic Data Analysis*
- ☐ **Gemini CLI date** — OLD: `released January 2026` → NEW: `released June 2025`
- ☐ **Author error** — OLD: `Zardiashvili et al. (2025)` → NEW: `Tang, X. et al. (2025)` (keep title, Nature Communications, DOI 10.1038/s41467-025-63913-1).
- ☐ **Nature editorial title (×2)** — OLD: `AI scientists are changing research — institutions must respond` → NEW: `…institutions, funders and publishers must respond`
- ☐ **p-hacking quote** — OLD: `overloads publishing peer-review systems without shifting the needle on discovery` → NEW: match the source verbatim (`…overload conference, publishing and funding peer-review systems, without shifting the needle on discovery`) or paraphrase without quote marks.
- ☐ **Sakana v1/v2** — attribute the **~$15/paper** figure to the **2024 v1** system; note the workshop manuscript was **withdrawn before publication**; clarify the Nature write-up describes v1.

### Page: *Verification of AI-Generated Code*
- ☐ **Cheng "out of date" flag** — remove the `Note that this is now pretty out of date!` flag on the Cheng et al. (2023) reading (it's cited as current elsewhere).
- ☐ **Forward-ref** — OLD "Up next: In Sub-Lesson 5 … hands-on activities and the weekly assessment" → NEW: "In Sub-Lesson 5, we bring everything together into a complete, reproducible data-analysis workflow."

### Page: *Building Your Data Analysis Workflow*
- ☐ **Forward-ref** — OLD: `In Sub-Lesson 6, we move to hands-on activities and assessment…` → NEW: "In Sub-Lesson 6, we turn to agentic data analysis … before the week's hands-on activities and assessment in Sub-Lesson 7."

### Page: *Visualization with AI*
- ☐ **matplotlib API** — OLD: `plt.cm.get_cmap('Set2')` → NEW: `plt.get_cmap('Set2')`

### Page: *Hands-On Activities and Assessment*
- ☐ **`<title>`** — `Week 7.6 - …` → `Week 7.7 - …` *(if the live title carries a number)*.
- ☐ **Next-week pointer** — OLD: `Next week, we turn to Critical Evaluation and Limitations of AI-Generated Content` → NEW: `Next week, we turn to Multimodal AI for Research` (Week 8; critical evaluation is Week 9).

---

## Lesson 8 — Multimodal AI  ✅ DONE (pilot)

### Page: *Transcription and Audio Analysis* — ☑ applied 2026-06-01
- Intron relabelled **Nigerian (Lagos-based)** (was "South African"); specs unchanged; Lelapa AI left as South African.

---

## Lesson 9 — Critical evaluation & limitations

### Page: *The Trajectory of LLM Capabilities*
- ☐ **HLE definition** — OLD: `Human Language Evaluation — broad reasoning across domains` / note `Composite reasoning measure.` → NEW: `Humanity's Last Exam — ~2,500 extremely difficult expert-authored questions spanning 100+ disciplines, designed to resist saturation.` / source `Single hard benchmark; CAIS + Scale AI, 2025 (arXiv:2501.14249).` (keep the 64.7 score).
- ☐ **GPT-5.5 naming** — standardise `ChatGPT 5.5 Pro` → `GPT-5.5 Pro`.
- ☐ **Ling 2.6 figures** — soften the unverified `$95-per-benchmark-run` / `92% hallucination` specifics (keep the real arXiv:2511.13029 citation + Intelligence-Index figure).

### Page: *Where AI Is Now Genuinely Strong*
- ☐ **MCP-Atlas attribution** — OLD: `GPT-5.5 Pro at MCP-Atlas 77.3%` → NEW: `Opus 4.7 at MCP-Atlas 77.3%`

---

*Reference copy of the corrected full pages: the GitHub `docs/week-N/…` files (and the live shocklab.github.io site) already contain all of the above, so you can copy exact NEW wording from there if needed.*
