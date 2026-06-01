# Restructured Weeks 7-12 Plan

## Context

Weeks 1-6 are built. The original plan had Weeks 7 (Data Analysis) and 8 (Coding/Computational Research) as separate weeks, but they overlap heavily — in practice, data analysis IS coding for most researchers. Merging them into one richer week frees up a slot for flexibility later.

The original plan also had Week 9 (Domain-Specific Applications) and Week 10 (Critical Evaluation/Limitations) as separate weeks. Week 9's content (domain-specific examples) works better woven into other weeks as case studies rather than standing alone. Week 10's content (limitations, hallucinations, sycophancy, reasoning failures) is partially covered already in Weeks 5-6 (hallucinated citations, verification habits, integrity) — but deserves its own focused treatment.

## Proposed Restructured Schedule

| Week | Topic | Notes |
|------|-------|-------|
| 7 | **AI for Data, Code & Computation** | Merged from original Weeks 7+8. Natural-language-to-code, data analysis, visualization, verification of AI-generated code, coding tools landscape. |
| 8 | **Critical Evaluation & Limitations of AI** | Moved up from original Week 10. Hallucination taxonomy, sycophancy, reasoning failures, "illusions of understanding" (Messeri & Crockett), domain-specific failure modes, verification protocols. |
| 9 | **Agentic AI, RAG & Advanced Research Tools** | Merged from original Week 8 (Advanced Capabilities) + new agentic AI content. MCP, tool use, multi-step agents, RAG, deep research tools, NotebookLM, the AI Scientist. |
| 10 | **Future of AI in Research & Africa's Sovereign AI Capacity** | Original Week 11 content. Frontier capabilities, regulatory landscape, AU Continental AI Strategy, $60B Africa AI Fund, decolonial AI, open vs closed models, building sovereign capacity. |
| 11 | **Flexible / TBD** | Reserved. Could become: deeper project work, agentic AI practical session, domain-specific deep dives, guest lectures, or whatever the cohort needs most by this point. |
| 12 | **Integrative Workshop & Presentations** | Original Week 12. Final presentations, peer review, ethical framework submission, closing reflections. |

## Rationale for This Order

1. **Week 7 (Data/Code)** follows naturally from writing (Week 6) — students move from producing text to producing analysis
2. **Week 8 (Critical Evaluation)** comes right after data/code because that's when students most need to understand how AI can produce code that runs but gives wrong results — the "silent error" problem. Also builds on Weeks 5-6's verification lessons into a comprehensive framework
3. **Week 9 (Agentic/RAG/Advanced)** is placed after critical evaluation because students need to understand limitations BEFORE being given more powerful tools. Agentic AI amplifies both capabilities and risks
4. **Week 10 (Future/Africa)** provides the big-picture context before final projects — students need to situate their work in the broader landscape
5. **Week 11 (Flexible)** gives breathing room before final presentations and can adapt to cohort needs

---

## Week 7: AI for Data, Code & Computation

### Sub-Lessons (6 pages + ToC)

#### Sub-Lesson 1: Natural Language to Code — The New Interface
- The paradigm shift: describing analysis in plain English and getting working Python/R
- Tools landscape: Claude Code, GitHub Copilot, Cursor, ChatGPT Code Interpreter, Google Colab AI
- **Free vs paid: the quality gap** — free tiers (ChatGPT free, Claude free, Gemini free) vs paid (Claude Pro, ChatGPT Plus, Copilot Pro). The difference in code quality, context window, and reliability is substantial. Students need to know what they're getting with free tools and where the limitations bite hardest. Strategies for maximising free tier value.
- "Vibe coding" — what it means, when it's useful, when it's dangerous
- The key insight: you don't need to be a programmer, but you DO need to understand what code is doing
- For students with no coding background: this is genuinely democratising
- For students with coding background: this changes your workflow, not your need for expertise

#### Sub-Lesson 2: AI-Assisted Data Analysis in Practice
- Data cleaning: detecting missing values, fixing formatting, standardising entries
- Exploratory data analysis: AI generates summary statistics and plots
- The "silent error" problem: when AI code runs without errors but produces wrong results (from original Week 7)
- Case study: ask AI to analyse a dataset, then deliberately check every step
- Kapoor & Narayanan (2023): "Leakage and the Reproducibility Crisis in ML-Based Science"
- Domain expertise as the essential complement: AI finds correlations; you determine if they're meaningful
- Spurious correlations (tylervigen.com), Simpson's paradox, overfitting

#### Sub-Lesson 3: Visualization with AI
- AI-generated visualizations: what's possible now (LIDA, Claude artifacts, Code Interpreter)
- Good visualization principles that AI often violates (misleading axes, poor colour choices, overplotting)
- When AI visualizations help vs when they mislead
- Practical: generate visualizations from data, then critically evaluate them
- Accessibility in visualization (colourblind-safe palettes, alt text)

#### Sub-Lesson 4: Verification of AI-Generated Code
- Why verification matters more than generation — the code may run perfectly while being completely wrong
- Reading code you didn't write: a skill every AI-assisted researcher needs
- Practical verification techniques:
  - Test with known data (synthetic datasets with known answers)
  - Edge cases and boundary conditions
  - Sanity checks (do the numbers make sense?)
  - Comparison with established tools/packages
  - The "change one thing" test: modify an input and check if the output changes appropriately
- Version control for reproducibility: why you should save every piece of AI-generated code
- Cheng et al. (2023): "Is GPT-4 a Good Data Analyst?" — instructive failures

#### Sub-Lesson 5: Building Your Data Analysis Workflow
- Practical workflow: question → data preparation → analysis → verification → interpretation
- Prompt templates for common analysis tasks
- When to use AI vs when to use established statistical packages
- Reproducibility: documenting your AI-assisted analysis so others can verify it
- Claude Code / Jupyter notebook side-by-side workflow (from Dataquest/Mineault guides)
- Privacy considerations: what data can you paste into AI tools?

#### Sub-Lesson 6: Hands-On Activities & Assessment
- Activity 1: Data cleaning challenge — messy dataset with planted errors, use AI to clean it
- Activity 2: Code generation and verification — describe analysis in plain English, AI generates code, critically verify outputs
- Activity 3: Interpretation challenge — AI-generated analyses, some correct, some with classic statistical errors
- Assessment: Use AI to analyse a dataset relevant to your research. Submit code, outputs, and critical commentary (1000 words)

### Key Sources
- Kapoor & Narayanan (2023): "Leakage and the Reproducibility Crisis" (Patterns)
- Cheng et al. (2023): "Is GPT-4 a Good Data Analyst?" (arXiv:2305.15038)
- Dibia (2023): "LIDA" (ACL, arXiv:2303.02927)
- Vigen: Spurious Correlations (tylervigen.com)
- Hong et al. (2024): "Data Interpreter" (arXiv:2402.18679)
- Mineault: "Claude Code for Scientists" (neuroai.science)

---

## Week 8: Critical Evaluation & Limitations of AI

### Sub-Lessons (6 pages + ToC)

#### Sub-Lesson 1: A Taxonomy of AI Failures
- Hallucination: plausible but false information (building on Week 5's citation crisis)
- Confabulation: filling knowledge gaps with fabricated details
- Sycophancy: agreeing with you even when you're wrong (Sharma et al., 2024)
- The reversal curse: knowing A→B but not B→A (Berglund et al., 2023)
- Reasoning failures: solving problems in one framing but failing with trivial rephrasing
- Calibration: AI confidence doesn't correlate with accuracy
- The unified view: Schlereth (2025) argues these are all manifestations of one root cause

#### Sub-Lesson 2: Illusions of Understanding
- Messeri & Crockett (2024): "AI and Illusions of Understanding in Scientific Research" (Nature) — the centrepiece reading
- Four types of illusion: illusions of exploratory breadth, illusions of objectivity, monocultures of knowing, doing more but understanding less
- The overreliance problem: AI makes you feel like you understand when you don't
- Connection to Week 6: "writing as thinking" — if AI does the analysis, do you understand the results?
- The Dunning-Kruger risk with AI: the less you know, the harder it is to spot AI errors

#### Sub-Lesson 3: Domain-Specific Failure Modes
- Woven from original Week 9 (Domain-Specific Applications)
- Chemistry: invented molecules, impossible reactions
- Biology: fabricated species, wrong gene functions
- Physics/Maths: plausible but wrong equations, unit errors
- Social sciences: fabricated statistics, invented survey results
- Humanities: false attributions, anachronistic claims
- The pattern: AI fails worst in areas where it has least training data — exactly where novel research happens
- Students identify failure modes specific to their own field

#### Sub-Lesson 4: Building Verification Protocols
- From ad-hoc checking to systematic verification
- A verification protocol framework: what to always check, field-specific checks, red flags
- Cross-referencing strategies
- Adversarial testing: deliberately trying to break AI outputs
- The "teach it back" test: if you can't explain the AI's reasoning, you don't understand it
- Building verification into your workflow (not as an afterthought)

#### Sub-Lesson 5: Case Studies — When AI Failed in Published Science
- NeurIPS 2025 hallucinated citations (recap from Week 5, with updates)
- Retraction Watch cases of AI-generated content in published papers
- The Mata v Avianca legal case (lawyer cited fake cases)
- Domain-specific examples from student fields
- What went wrong systemically in each case
- How verification would have caught each failure

#### Sub-Lesson 6: Hands-On Activities & Assessment
- Activity 1: Hallucination hunting — deliberately induce failures in your domain
- Activity 2: Collaborative failure catalogue — class builds shared resource
- Activity 3: Verification protocol design — create a protocol for your field
- Assessment: Failure analysis report (1500 words) — document 5+ distinct failure modes in your domain

### Key Sources
- Messeri & Crockett (2024): "AI and Illusions of Understanding" (Nature)
- Berglund et al. (2023): "The Reversal Curse" (arXiv:2309.12288)
- Sharma et al. (2024): "Towards Understanding Sycophancy" (ICLR, arXiv:2310.13548)
- Narayanan & Kapoor: AI Snake Oil (aisnakeoil.com)
- Schlereth (2025): "Seven Persistent Failures, One Root Function" (PhilArchive)
- Frieder et al. (2023): "Mathematical Capabilities of ChatGPT" (NeurIPS)
- OpenAI (2025): "Why Language Models Hallucinate" (technical paper)

---

## Weeks 9-12: Summary (to be planned in detail when we get there)

### Week 9: Agentic AI, RAG & Advanced Research Tools
- RAG explained simply, practical RAG (NotebookLM, Claude Projects, uploading papers)
- Deep research tools (Perplexity, Claude Research, Google Deep Research)
- Agentic AI: planning, tool use, multi-step workflows, MCP
- The AI Scientist (Sakana AI, Nature 2026)
- Building custom research assistants
- "Lost in the middle" problem (Liu et al., 2024)
- Article Galaxy MCP for scientific literature access

### Week 10: Future of AI in Research & Africa's Sovereign AI Capacity
- Frontier capabilities: reasoning models, multimodal, real-time AI
- AI for scientific discovery: AlphaFold, GraphCast, GNoME, AlphaEvolve
- Regulatory landscape: EU AI Act, AU Continental AI Strategy, Africa AI Declaration (Kigali 2025)
- The $60B Africa AI Fund
- Open vs closed models, sovereign infrastructure
- Decolonial AI (Mohamed et al., 2020)
- How to stay current and navigate hype

### Week 11: Flexible / TBD
- Reserved for cohort needs
- Could be: deeper project work, guest lectures, agentic AI practical, domain deep dives

### Week 12: Integrative Workshop & Presentations
- Final project presentations (10 min + 5 min Q&A)
- Structured peer review
- Ethical framework submission
- Closing reflection

---

## Immediate Next Step: Build Week 7

Build "AI for Data, Code & Computation" following the established process:
1. Research & plan (done above)
2. Build 6 sub-lessons + ToC
3. Run `/verify-references`
4. Fix issues
5. Update CLAUDE.md
6. Copy to docs/, update index.html
7. Push to GitHub
8. Upload to Amathuba (with emoji sanitisation)
9. Update CLAUDE.md

### Files to Create
```
Week 7/
  Table of Contents.html
  Natural Language to Code.html
  AI-Assisted Data Analysis in Practice.html
  Visualization with AI.html
  Verification of AI-Generated Code.html
  Building Your Data Analysis Workflow.html
  Hands-On Activities and Assessment.html
```
