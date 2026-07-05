# NotebookLM image plan — MAM5020F: Generative AI for Research

A per-lesson list of images worth creating in Google NotebookLM, organised by week and lesson. The brief is sized to NotebookLM's strengths — explanatory infographics, concept and architecture diagrams, process and data-flow diagrams, comparison charts, decision frameworks, and timelines built from the lesson's own content — not decorative stock art.

**How to read each entry.** Under each lesson H1 are the suggested images, each with:
- **Title** — what to call the figure.
- *Shows:* the exact concept from that lesson the image makes visible.
- *NotebookLM:* a brief you can hand to NotebookLM to generate it. Pull the actual figures, names, and wording from the lesson page itself when you prompt.

**Scope and density.** Core teaching lessons only — hands-on/assessment, discussion, and Table-of-Contents pages are excluded by design. Density is 2–3 images where they genuinely help, fewer for lighter pages. "— (no image needed)" is a deliberate call: video-wrapper pages, pure orientation pages, and pages where a static image would only restate a heading get nothing rather than padding.

Roughly 100 images are suggested in total across the course. You almost certainly won't make all of them — treat this as a ranked menu per lesson and pick the ones that earn their place.

---

## Week 1 — Foundations of Generative AI

**Foundations of Generative AI**

— (no image needed)

Orientation/overview page: learning objectives, a topic list, and a preview timeline already rendered as styled HTML. Nothing here is dense enough to warrant a separate infographic — the page's job is to point forward to the substantive lessons.

**The Evolution of Artificial Intelligence**

1. **AI's Historical Timeline** — *Shows:* The six distinct eras of AI development from the 1950s through the Generative AI era, including the two AI winters and the key turning points (Perceptron, backpropagation, ImageNet, Transformers, ChatGPT). *NotebookLM:* Generate a horizontal timeline with labelled eras as bands (Symbolic AI, First Winter, Expert Systems & Second Winter, Statistical Turn, Deep Learning Revolution, Generative AI Era), with 2–3 named milestone events per era and brief annotations on what broke the preceding deadlock. Aim for a "big-picture arc" a newcomer can read in 60 seconds.
2. **Rules vs Statistics vs Learning — Three Paradigms of AI** — *Shows:* The conceptual shift from symbolic rule-based AI, to statistical machine learning, to neural/deep learning, with a concrete example of the same task handled by each paradigm. *NotebookLM:* Create a three-column comparison diagram — one column per paradigm — showing the core idea, how knowledge is encoded, what fails, and a real example from the lesson (ALPAC report for rules, IBM statistical translation for statistics, AlexNet for deep learning).

**AI History and Mathematical Foundations**

— (no image needed)

Video-only page embedding a recorded seminar. The video itself is the content.

**But What Is a Neural Network?**

— (no image needed)

Wrapper for the 3Blue1Brown video. The animated video already performs the visualisation job better than any static infographic could.

**Understanding How Generative AI Works**

1. **Discriminative vs Generative AI** — *Shows:* The core distinction between a system that draws a boundary between categories ("Is this spam?") and a system that learns the underlying structure to create new examples ("Write me a convincing email"). *NotebookLM:* Generate a side-by-side diagram with a concrete research scenario on each side — left, a microscopy image classified as "tumour/not tumour"; right, a model generating a synthetic microscopy image from a text prompt — with labels naming the task type, the question the system answers, and a representative tool.
2. **Three Architectures: Transformers, Diffusion Models, GANs** — *Shows:* How each of the three major generative architectures produces its output, using the lesson's own descriptions and analogies. *NotebookLM:* Create a three-row process-flow diagram — one row per architecture — with 4–5 labelled steps drawn from the lesson (e.g. for diffusion: clean image → add noise → learn to denoise → start from noise → guided refinement → output). Include the lesson's analogy for each (attention as selective reading, crystallisation for diffusion, forger-vs-expert for GANs) as a caption.

**Transformers and Diffusion Models**

— (no image needed)

Video-collection page (five embedded YouTube videos with a single framing paragraph). The videos are the lesson.

**Current Generative AI Landscape**

1. **The Generative AI Modality Map** — *Shows:* How the current landscape divides by output modality (text, image, video, code/agents) and by access type (closed-frontier, open-weight, specialist tool), with representative model families placed in each region. *NotebookLM:* Generate a structured matrix with modalities as rows (LLMs, image, video, code/agents) and columns for key attributes (representative families, distinguishing strength, research use case), drawn from the page's model cards. The goal is to help a researcher find which category of tool fits which task without memorising 30 model names.

---

## Week 2 — LLM Deep Dive

**LLM Architecture Deep Dive**

1. **Transformer Forward Pass — Anatomy of One Token** — *Shows:* The seven-step journey from raw text to a predicted next token (tokenisation → embedding → positional encoding → N× transformer layers → layer norm → output projection → sampling). *NotebookLM:* Generate a vertical pipeline diagram with labelled boxes for each step, annotated with concrete details from the lesson (e.g. "token IDs: [464, 3797]", "4096-dim vector", "vocab size ~50K"). Use arrows for data flow; sidebar annotations call out where attention and feed-forward happen inside the repeated block.
2. **Dense vs Sparse (MoE) Architectures — Side-by-Side** — *Shows:* The contrast between a dense model (all parameters active per token) and a Mixture-of-Experts model (router selects 2-of-8 experts), with the Mixtral 8x7B and DeepSeek-V3 examples from the lesson. *NotebookLM:* Two-column comparison: left, a single FFN layer lighting up fully; right, 8 expert FFNs with only 2 highlighted as active and a router node above them. Annotate with the lesson's numbers (47B total / 13B active; 671B total / 37B active).
3. **Attention Variants Comparison Made Visual** — *Shows:* How MHA, MQA, and GQA differ in how Q, K, V heads are shared, and why GQA became dominant. *NotebookLM:* Three side-by-side attention head schemas — MHA (every head has its own Q, K, V), MQA (single shared K, V; unique Q per head), GQA (grouped: subsets share K, V) — with labels matching the lesson's table.

**Training Large Language Models**

1. **The Pre-Training Data Pipeline** — *Shows:* How raw web text becomes training tokens, from Common Crawl through quality filtering, deduplication, tokenisation (BPE), and final batching. *NotebookLM:* Left-to-right pipeline diagram with labelled stages and examples from the lesson (e.g. "GPT-3: 300B tokens from Filtered Common Crawl + WebText2 + Books + Wikipedia"), with a callout on why data composition — not just volume — shapes model behaviour.
2. **Kaplan vs Chinchilla Scaling — The Key Shift** — *Shows:* The lesson's core insight that compute-optimal training balances model size and token count together, not just parameters. *NotebookLM:* Two-panel diagram: left, the Kaplan-era intuition (scale model size for fixed tokens); right, the Chinchilla correction (scale tokens with parameters, ~20 tokens/param). Annotate with the lesson's example: GPT-3 (175B params / 300B tokens = undertrained) vs the Chinchilla-optimal equivalent.
3. **3D Parallelism — How 1024 GPUs Train One Model** — *Shows:* How data, tensor, and pipeline parallelism combine in the 175B-model example (16 × 8 × 8 = 1024 GPUs). *NotebookLM:* A 3D grid or layered block diagram decomposing the GPU arrangement into its three parallel dimensions, with a brief note on what each does (batch splits / layer splits / pipeline stages).

**Fine-Tuning, RLHF & Alignment**

1. **The Three-Step RLHF Pipeline** — *Shows:* The full SFT → Reward Model → RL optimisation (PPO) pipeline, including the KL-divergence penalty that keeps the policy from drifting. *NotebookLM:* Left-to-right three-stage flowchart: Stage 1 (SFT model on curated prompt/response pairs); Stage 2 (human annotators compare outputs → reward model trained on (prompt, chosen, rejected) triples); Stage 3 (RL loop where SFT policy generates, RM scores, PPO updates). Include the chef-and-diner analogy from the lesson as a caption.
2. **Fine-Tuning Decision Framework — Prompt vs LoRA vs Full Fine-Tune** — *Shows:* The practical decision researchers face between prompt engineering, LoRA, and full fine-tuning, based on the lesson's comparison table. *NotebookLM:* Decision-tree starting "Do you have a specialised task?" and branching on data volume, structured output, sensitivity/privacy, and compute budget. Terminal nodes map to the lesson's recommendations (few-shot prompting / LoRA on 7B / full fine-tune / closed-API).

**How AI Image Generation Works**

— (no image needed)

---

## Week 3 — Environmental Implications of AI

**The Cost of Every Prompt**

1. **The Energy Scale Ladder** — *Shows:* The relative energy cost of different AI operations (a single text query vs an image generation vs a frontier training run), placed against everyday reference points so the orders of magnitude are felt, not just read. *NotebookLM:* Generate a vertical (log-scale) ladder ordering operations from cheapest to most expensive, each rung carrying the lesson's figure and an everyday equivalent (phone charge, household-day, car-lifetime), making the spread across many orders of magnitude legible at a glance.
2. **The Transparency Gap** — *Shows:* How little of AI's true energy and water footprint major providers actually disclose — what can be measured versus what stays hidden. *NotebookLM:* Generate an iceberg or two-column "disclosed / withheld" diagram, with the measurable per-query estimates above the waterline and the undisclosed training, cooling, and embodied-hardware costs below, each annotated with why it is hard to obtain.

**Infrastructure, Scale and the Rebound Problem**

1. **Anatomy of a Data Centre** — *Shows:* The physical components of an AI data centre and where energy and water actually go (compute, cooling, power delivery, networking). *NotebookLM:* Generate a labelled cutaway/anatomy diagram with each subsystem annotated by its share of energy or water use, and a callout on the cooling-water draw that connects to local resource stress.
2. **The Jevons Paradox Loop** — *Shows:* How efficiency gains in AI drive more total consumption rather than less (cheaper inference → more usage → larger aggregate footprint). *NotebookLM:* Generate a closed-loop cycle diagram — efficiency improves → cost per query drops → usage expands → total demand rises → more infrastructure built → back to the start — annotating the rebound mechanism at each node.

**Critical Minerals and AI**

1. **Mine-to-Data-Centre Supply Chain** — *Shows:* The path of critical minerals from extraction through refining and component manufacture to the chips inside a data centre, with the human and environmental burden concentrated at the extraction end. *NotebookLM:* Generate a left-to-right supply-chain flow with labelled stages (mining → refining → component fabrication → hardware → data centre), annotating which minerals (cobalt, lithium, rare earths) enter where, and where the environmental and labour costs fall.
2. **Environmental Cost Distribution** — *Shows:* How the environmental burden of AI is distributed unevenly across the lifecycle and across geographies — extraction costs concentrated in the global South, benefits accruing in the global North. *NotebookLM:* Generate a stacked-bar or map-linked breakdown showing where in the lifecycle the costs land versus where the benefits accrue, making the distributional injustice visible.

**Sustainable AI — Practices and Possibilities**

1. **The Researcher's Decision Framework** — *Shows:* The practical choices a researcher can make to reduce the footprint of their own AI use (model size, local vs cloud, batching, when not to use a generative model at all). *NotebookLM:* Generate a decision-tree starting "Do you need a generative model for this task?" and branching through model-size choice, local vs cloud, batching, and reuse, each terminal node carrying a one-line footprint-reduction action drawn from the lesson.

---

## Week 4 — Ethical Frameworks for AI in Research

**Ethical Frameworks and Four Lenses**

1. **The Ethics Gap** — *Shows:* The gap between what is technically possible with AI and what is ethically defensible, and why ethical reasoning is needed where rules run out. *NotebookLM:* Generate a two-zone diagram (the larger "can" space with the smaller "should" space inside it), annotated with a research example that is permitted but ethically fraught, establishing why the four lenses are needed.
2. **The Four Lenses Toolkit** — *Shows:* The four ethical frameworks the course uses (consequentialism, deontology, virtue ethics, and the relational/Ubuntu lens) side by side, with the core question each one asks. *NotebookLM:* Generate a four-panel toolkit diagram, one panel per lens, each naming the framework, its central question ("What are the consequences?" / "What are my duties?" / "What kind of researcher am I?" / "What do my relationships and community require?"), and a one-line example application.
3. **The Same Scenario Through Four Lenses** — *Shows:* How a single research dilemma yields different judgments depending on which lens is applied. *NotebookLM:* Generate a hub-and-spoke diagram with one research scenario at the centre and four spokes, each showing the verdict and reasoning that lens produces — so the reader sees the lenses as complementary, not interchangeable.

**Ubuntu Relational Ethics and the Just AI Framework**

1. **Rationality vs Relationality** — *Shows:* The contrast between the individualist, rationality-first assumptions of Northern AI ethics and the relational, community-first starting point of Ubuntu. *NotebookLM:* Generate a side-by-side comparison — left, "the individual as the unit of moral concern"; right, "a person is a person through other persons" — each annotated with how it frames a data-consent or authorship question differently.
2. **The Nine Core Inquiries** — *Shows:* The nine inquiries of the Just AI framework as a structured set a researcher can work through. *NotebookLM:* Generate a 3×3 grid or radial diagram naming each of the nine inquiries with a one-line prompt for each, designed as a working checklist a researcher can return to.
3. **Reframing Questions: Individualist vs Ubuntu** — *Shows:* How the same ethical question is re-asked when you move from an individualist to an Ubuntu frame. *NotebookLM:* Generate a two-column table pairing an individualist phrasing ("Did the individual consent?") with its Ubuntu reframing ("Whose relationships and community are affected, and were they part of the decision?") across several research situations.

**Transparency, Authorship and Integrity**

1. **The Academic Integrity Spectrum** — *Shows:* The spectrum of AI involvement in scholarly work from clearly acceptable (grammar/formatting) to clearly unacceptable (fabricated data, ghost-authored arguments), with the grey zone in the middle. *NotebookLM:* Generate a horizontal green-to-red spectrum with labelled points along it, and the principle that concern rises as AI moves from form to substance stated as a caption.
2. **What and Where to Disclose** — *Shows:* Which AI uses require disclosure and where in a paper that disclosure belongs. *NotebookLM:* Generate a placement diagram mapping types of AI use to the disclosure action and location (methods section / acknowledgements / no disclosure needed), drawn from the lesson's guidance.

**Applying Ethics: Case Studies and Your Framework**

1. **The Six-Step Decision Framework** — *Shows:* The six-step process for working through an AI ethics decision, from identifying the dilemma to committing to a course of action. *NotebookLM:* Generate a numbered six-stage flow (identify stakeholders → apply the four lenses → check disclosure/integrity obligations → weigh community/relational impact → decide → document the reasoning), each step with a one-line prompt, designed as a reusable procedure.

**The Broader Landscape of AI Ethics**

— (no image needed)

---

## Week 5 — AI-Assisted Literature Review

**The AI Literature Review Landscape**

1. **Three Categories of AI Literature Tools** — *Shows:* The structural distinction between citation-based discovery (graph analysis), semantic search/synthesis (embeddings), and grounded chat/RAG (retrieval + generation), and what each does under the hood. *NotebookLM:* Three-column diagram, one per category, showing the core mechanism (graph nodes and edges / vector similarity space / chunking-retrieval-generation pipeline), representative tools, and the key strength and key failure mode for each.
2. **The Seven-Step Combined Workflow** — *Shows:* How the three tool categories combine into a sequential research workflow, from landscape scan to synthesis and note-taking. *NotebookLM:* Numbered pipeline diagram (steps 1–7), labelling each step with its action, the tool category used, and example tool names; use visual grouping to mark where human judgment is required (steps 2 and 7).

**Free Tools Deep Dive**

1. **Tool Role Map: What Each Free Tool Is Actually For** — *Shows:* That the five free tools (Semantic Scholar, ResearchRabbit, Connected Papers, NotebookLM, Google Scholar) occupy distinct, non-overlapping roles rather than being interchangeable. *NotebookLM:* A lane diagram mapping each tool to its stage in the research lifecycle (discovery / citation mapping / reading & synthesis / verification), with a one-line "use it for this, not that" note per tool and its current pricing status.

**Paid Tools and When They Are Worth It**

1. **Decision Framework: When to Pay** — *Shows:* The specific situations that justify each paid tool (Elicit → systematic review; Scite → contested claims; Consensus → empirical consensus check) versus the free alternatives that cover general use. *NotebookLM:* Decision-tree starting "What kind of literature task are you doing?" branching to either a specific paid tool with its killer feature or the free alternative that suffices; include a "check institutional access first" node before any paid recommendation.

**The Hallucinated Citation Crisis**

1. **Retrieval vs Generation: Why One Hallucinates and the Other Doesn't** — *Shows:* The architectural difference between tools that search a real database (retrieval) and tools that predict the next token (generation), explaining why general-purpose LLMs fabricate citations while Semantic Scholar or Elicit cannot. *NotebookLM:* Side-by-side diagram: left, the retrieval path (query → database lookup → real record returned); right, the generation path (query → token prediction → statistically plausible text, no database step); annotate each step where hallucination can and cannot occur.
2. **The Pollution Loop** — *Shows:* How a hallucinated citation, once published, gets indexed, absorbed into training data, and cited with growing confidence by future AI — a self-reinforcing degradation of the scholarly record. *NotebookLM:* Closed-loop cycle diagram with four nodes: (1) AI generates fake citation → (2) enters a published paper → (3) indexed by databases → (4) absorbed into the next model's training data → back to (1), with an annotation at each node showing what makes detection harder there.

**Building Your Research Workflow with Claude**

— (no image needed)

---

## Week 6 — AI for Writing, Communication & Research Ideation

**Writing as Thinking**

1. **The AI Assistance Spectrum** — *Shows:* The five-level continuum from proofreading (low risk) to generating entire sections (very high risk), with the cognitive cost at each level. *NotebookLM:* Horizontal spectrum diagram with five labelled zones (Proofreading → Language Enhancement → Restructuring → Generating Arguments → Generating Entire Sections), colour-coded green to red, each with a one-line description of the cognitive work the researcher retains versus cedes. Source the exact zone labels from this lesson.
2. **Writing as Knowledge-Transforming vs Transcription** — *Shows:* The distinction between writing as a thinking process (ideas start messy and interconnected; writing forces linearisation, revealing gaps) and writing as transcription (ideas → words, no cognitive transformation). *NotebookLM:* Two-panel "with/without" diagram: left shows the messy-web-to-linear-argument process of genuine writing; right shows the shortcut where AI produces polished prose and the thinking loop is bypassed. Draw on the cognitive-science box in the lesson.

**Research Ideation with AI**

1. **Five Prompting Strategies for Ideation** — *Shows:* The five strategies (chain-of-thought, role-playing, constraint-based, adversarial, cross-disciplinary) mapped against their cognitive purpose and the kind of output each produces. *NotebookLM:* Five-cell comparison infographic — one row per strategy — with columns for strategy name, what it forces the model to do, and the type of research gap or idea it surfaces. Use the exact names, purposes, and example prompts from the lesson's card grid.
2. **The Idea Monoculture Risk** — *Shows:* The self-reinforcing cycle by which widespread AI brainstorming narrows rather than expands the research space, and the mitigations that break it. *NotebookLM:* Circular-flow diagram showing researchers use same tools → convergent outputs → similar directions → narrower field → more pressure to adopt AI → repeat; with annotations pointing to the break-out interventions in the lesson (brainstorm alone first, adversarial prompting, separate conversations, unstructured time).

**AI Writing Tools — Landscape and Honest Assessment**

1. **The Four Tool Categories** — *Shows:* How the four categories (general-purpose LLMs, specialist academic tools, grammar/style tools, translation tools) differ in scope, best use, and what they do and do not touch. *NotebookLM:* Quadrant diagram positioning the four categories by two axes (breadth of task vs academic-specificity), each cell annotated with representative tools, key strengths, and the one thing each category cannot do. Draw from the card-grid descriptions in this lesson.
2. **Two Futures for Multilingual Publishing** — *Shows:* The divergent paths the Amano et al. 2025 PLOS Biology paper identifies: AI used to write in English (reinforcing hegemony) versus AI enabling write-in-your-own-language / read-in-yours (promoting diversity). *NotebookLM:* Forked-path diagram with a shared start ("AI translation becomes widespread"), two clearly labelled branches, and the consequence for African/non-Anglophone researchers at the end of each. Source the framing from the case-study box.

**Scientific Integrity and the Writing Pipeline**

1. **The Integrity Spectrum: Form to Substance** — *Shows:* The six-level risk spectrum from grammar fixes through generating arguments and data descriptions, with the principle that integrity concern scales as AI shifts from form to substance. *NotebookLM:* Vertical or diagonal spectrum with six labelled steps, each showing what AI does at that level, what the researcher retains, and the risk colour (green → red). Include the lesson's heuristic ("if you removed the AI contribution, would the intellectual content change?") as an annotated test at the top.
2. **Major Publisher AI Policies at a Glance** — *Shows:* The convergence and variation across Science, Nature, Elsevier, IEEE, ACM, and COPE on three dimensions: whether AI authorship is permitted, whether disclosure is required, and who bears accountability. *NotebookLM:* Compact comparison table or icon-matrix with publishers as rows and policy dimensions as columns, using the data from the lesson's table. Highlight the converging baseline (four shared principles) so both consensus and variation are visible.

**Building Your AI Writing Workflow**

1. **The Five-Stage Principled Workflow** — *Shows:* The ordered sequence from "Think first" through "Revise in your own voice," with the rule that AI is most valuable in stages 3–4 and most dangerous if used to replace stages 1–2. *NotebookLM:* Numbered five-stage pipeline, each stage annotated with what the researcher does, what AI does (if anything), and the guard rail ("AI enters here," "this stage is yours alone"). Include the core principle from the highlight box as a caption.

**Using AI to Review Your Own Work**

1. **What AI Can and Cannot Usefully Check in Peer Review** — *Shows:* The six review dimensions AI handles with varying reliability (logical consistency, writing quality, positioning, experimental methodology, statistical reporting, figures/tables) contrasted with the five that remain beyond it (novelty, domain conventions, significance, ethics, reviewer politics). *NotebookLM:* Split diagram: left zone "AI reliable" listing the six checkable dimensions in rough order of reliability; right zone "Human judgment required" listing the five unreachable ones. Source the items from Sections 2 and 3.

---

## Week 7 — AI for Data, Code & Computation

**Natural Language to Code — The New Interface**

1. **The Spectrum from Conversational to Agentic Tools** — *Shows:* How the six tools (ChatGPT Code Interpreter, Google Colab AI, GitHub Copilot, Cursor, Gemini Code Assist, Claude Code) sit on two axes: ease of entry for non-programmers vs autonomous capability. *NotebookLM:* Labelled quadrant placing all six tools by beginner-friendliness (y-axis) and agentic autonomy (x-axis), each annotated by pricing tier and best use case.
2. **Vibe Coding: When It Works vs When It Fails** — *Shows:* The contrast between safe and dangerous uses of the vibe-coding approach — prototyping vs publication; exploratory code vs analysis you will report. *NotebookLM:* Two-column comparison contrasting safe contexts (prototyping, exploration, learning, utility scripts) against dangerous ones (publication analysis, policy-informing results, complex pipelines, reproducibility-critical work), with a clear divider and the core principle — scientific errors survive autonomous iteration, programming errors do not — as a caption.

**AI-Assisted Data Analysis in Practice**

1. **The Silent Error Taxonomy** — *Shows:* The six named categories of silent error (wrong variable, off-by-one in time series, incorrect missing-data handling, wrong statistical test, aggregation errors, data leakage) as a labelled anatomy. *NotebookLM:* Hexagonal or grid taxonomy in which each of the six error types is a labelled cell showing what it is, an example column/scenario, and how to catch it. Emphasise visually that these errors produce clean output with no warning.
2. **Simpson's Paradox: Aggregate vs Subgroup** — *Shows:* The reversal where an aggregate trend vanishes or flips when the data is broken into subgroups. *NotebookLM:* Split diagram: left, a single aggregated bar/slope showing the misleading result; right, the same data separated into subgroups showing the true (reversed) pattern, annotated to explain that domain expertise — not AI — is what prompts you to look for confounders.

**Visualisation with AI**

1. **Six Visualisation Failures in AI Defaults** — *Shows:* The six ways AI-generated charts go wrong (misleading axes, poor colour, overplotting, wrong chart type, missing context, chartjunk) as a single annotated "bad chart anatomy." *NotebookLM:* One deliberately flawed chart with six numbered callout arrows, each pointing to a failure mode, labelled with the failure name and a one-line fix.
2. **Colourblind-Safe Palette Comparison** — *Shows:* How the same categorical data looks under a default matplotlib palette vs Okabe-Ito or viridis, with a deuteranopia simulation column. *NotebookLM:* Three-column grid: default matplotlib swatch; the same under a colourblind-safe palette; both under a red-green colourblindness simulation, with a caption noting the 8% prevalence figure from the lesson.

**Verification of AI-Generated Code**

1. **Common AI Code Failure Patterns Checklist** — *Shows:* The six failure patterns from the lesson's table (variable confusion, off-by-one, wrong test, missing data, aggregation errors, library version) as a structured pre-submission checklist. *NotebookLM:* Visual checklist card — one row per pattern — with columns for "what happens," "how to catch it," and a checkbox; styled as a reference card a student consults before submitting any AI-generated analysis.

**Building Your Data Analysis Workflow**

1. **The Five-Stage Principled Workflow** — *Shows:* The cycle Define → Prepare → Analyse → Verify → Interpret, marking where AI is most valuable (stages 2–4) versus where researcher judgment is non-negotiable (stages 1 and 5). *NotebookLM:* Circular or linear five-stage pipeline; stages 2–4 highlighted "AI assist here"; stages 1 and 5 marked "researcher judgment only," with a brief label for what AI cannot do at each.
2. **AI vs Established Packages Decision Matrix** — *Shows:* The ten task types from the lesson's table (EDA, data cleaning, hypothesis tests, basic regression, complex regression, visualisation, time series, ML, Bayesian, clinical trials) mapped against AI-assisted vs established-package suitability. *NotebookLM:* Colour-coded matrix — green "use AI," amber "hybrid," red "established package only" — so the overall pattern (AI strong for exploration, packages required for complex/validated work) is immediately visible.

**Agentic Data Analysis: Giving AI Tools, Not Just Questions**

1. **Conversational vs Agentic AI: What Changes** — *Shows:* The structural difference between a human-in-the-loop conversational loop and an agentic pipeline (agent reads files, runs code, fixes errors, iterates, returns results). *NotebookLM:* Side-by-side flow diagram: left, the conversational back-and-forth between a human icon and a chat bubble; right, the agentic autonomous loop (read files, run code, check output, fix error, iterate) with a single human input at the start and a review checkpoint at the end.
2. **Reliability Degradation in Sequential Pipelines** — *Shows:* How 90% per-step reliability compounds to 59% over 5 steps, 35% over 10, and 12% over 20 — the mathematical case for human checkpoints. *NotebookLM:* Bar or curve chart with pipeline length (1–20 steps) on the x-axis and end-to-end reliability on the y-axis, the 5-, 10-, and 20-step values annotated, plus a horizontal "acceptable reliability threshold" line and a caption framing this as the structural argument for mid-pipeline review.

---

## Week 8 — Multimodal AI for Research

**What Multimodal AI Can See, Hear, and Read**

1. **Four Modalities Map** — *Shows:* The four research-relevant modalities (images, audio, documents, video) mapped against the major tools and the research domains that rely on each. *NotebookLM:* Landscape diagram with the four modalities as labelled zones/columns, the leading tools placed in each, and a row of example domains (qualitative research, archival, earth science, education) cross-referenced to the relevant modality columns.
2. **Reading vs Understanding Gap** — *Shows:* The distinction between pattern-matching fluency and genuine reasoning, anchored by the CharXiv benchmark result (47.1% AI vs 80.5% human). *NotebookLM:* A "what the model does vs what you might assume it does" comparison using the chart-reading scenario: one side shows confident fluent output, the other what actually went wrong (reading axis labels, not geometry), with the benchmark numbers labelled.

**AI and Scientific Images**

1. **The Description Zone vs Value-Extraction Zone** — *Shows:* The boundary between tasks where AI image analysis is reliable (description, alt text, qualitative trends, visual comparison) and tasks where it fails (specific numbers from axes, reasoning about chart geometry). *NotebookLM:* Two-zone diagram with specific example tasks placed inside each, clearly labelled "Reliable" and "Unreliable." This operationalises the lesson's central heuristic.
2. **Benchmark Paradox — Real vs Simplified Charts** — *Shows:* The performance drop from simplified benchmarks (AI2D, ChartQA ~90%) to real scientific charts (CharXiv ~47%), and the mechanism (models read text labels rather than processing geometry). *NotebookLM:* Before/after comparison showing a simplified benchmark chart vs a complex real scientific chart, with score bars for each and an annotation explaining what the model is actually attending to.
3. **Five-Step Workflow for Scientific Images** — *Shows:* The sequential workflow (description only, verify numbers, check reasoning, use domain tools, test on labelled subsample) as a pipeline. *NotebookLM:* Numbered flow diagram where each step is labelled with both the action and the failure mode it catches (Step 2 "verify numbers" catches the CharXiv reading error; Step 3 "check reasoning" catches the Jin et al. confabulation problem).

**Document Intelligence — PDFs, Tables, and Forms**

1. **Three PDF Types and Their Extraction Characteristics** — *Shows:* The distinction between native, scanned, and mixed PDFs and which tools handle each reliably. *NotebookLM:* Decision-tree or three-column anatomy showing the structural difference (text stored as glyphs vs page as image vs mixed), the expected accuracy, and the recommended tool for each.
2. **Complex Table Failure Modes** — *Shows:* The four ways complex tables break during extraction (row merging, multi-level headers, footnote associations, reading order). *NotebookLM:* "Anatomy of a broken complex table" showing a schematic research table with merged cells and multi-level headers on the left, then the corrupted extracted output on the right, with each failure mode labelled.

**Transcription and Audio Analysis**

1. **WER Across Audio Conditions** — *Shows:* The gap between the headline 2% WER on clean read speech and the 11–26% WER on realistic research audio (meetings, telephony, spontaneous speech, African languages). *NotebookLM:* Bar or step chart of WER for each condition from the lesson's table, with a horizontal line marking where human review becomes mandatory and each condition linked to the type of research audio it represents.
2. **Audio-to-Analysis Pipeline with Privacy Checkpoints** — *Shows:* The workflow from raw interview audio through transcription, verification, QDA import, and AI-assisted coding, with explicit data-governance decision gates (local vs cloud, ethics-approval check, consent scope). *NotebookLM:* Flow diagram of the CAAI-informed workflow with branching decision points for privacy governance (does ethics approval cover cloud processing? does consent cover commercial AI?), mapping to local-tool vs cloud-tool branches.

**Video and Multimodal Workflows**

1. **Native Multimodal vs Text-Centric Architecture** — *Shows:* The architectural difference between natively multimodal models (Gemini, GPT family jointly processing all modalities) and text-centric sequential pipelines (Claude: transcribe audio first, then analyse), and what cross-modal reasoning the joint architecture enables that the sequential one cannot. *NotebookLM:* Side-by-side architecture diagram: one path where audio, visual, and text enter a single model together; one where each modality is converted to text first, then fed to the language model, annotated with what information is lost at each conversion.
2. **Video-Specific Failure Modes** — *Shows:* The four compounding failure modes unique to video (compounding errors across layers, temporal hallucination, middle-of-video attention drop, speaker diarization errors) as a risk map. *NotebookLM:* Labelled risk diagram of a video timeline, each failure mode placed where it occurs (temporal hallucination at timestamp markers, attention drop in the middle segment, compounding errors as a stack at the output layer), so readers see where in a video workflow each risk materialises.

---

## Week 9 — Critical Evaluation & Limitations of AI

**The Trajectory of LLM Capabilities**

1. **Capability Timeline: 2019–2026** — *Shows:* The seven-year sweep of what changed and what still failed at each milestone, from GPT-2 through the May 2026 frontier. *NotebookLM:* Horizontal timeline with six labelled stops (2019 GPT-2 through May 2026), each with two cells beneath it — "What was new" and "What still failed" — from the lesson's table. Use contrasting colours so the pattern of receding failures is visible at a glance.
2. **Benchmark Pitfalls: Three Failure Modes** — *Shows:* Why benchmark scores mislead — Goodhart's law, contamination, and the African/low-resource gap. *NotebookLM:* Three-panel comparison, one per pitfall, each with a short caption and a concrete example from the lesson (SWE-bench vs ProgramBench for Goodhart; MMLU contamination rates; the English-vs-African-language performance gap).

**Three Categories of Failure: Patched, Reduced, Structural**

1. **Failure Taxonomy Decision Tree** — *Shows:* How to classify an observed AI failure into one of the three categories and what to do about it. *NotebookLM:* Decision-tree/flowchart: "When you observe a failure → Is it known to be fixed in current frontier models? → Is it reduced but still surfacing under specific conditions? → Is it structural/architectural?" Each branch leads to a labelled action (switch model / add workflow mitigations / use verification protocols). Source the leaf examples from the lesson's diagnostic table.
2. **Anatomy of a Structural Failure** — *Shows:* The five structural failures (hallucination as statistical pressure, pattern completion vs understanding, the long-tail problem, compositional brittleness, training-data dependence) as a labelled cluster. *NotebookLM:* Hub-and-spoke with "Structural — unlikely to be fixed by the next release" at the centre and one spoke per failure, each with a one-sentence explanation and a real example (FoodTruck Bench for compositional brittleness, Ling 2.6's 92% hallucination rate for training-data dependence).

**Where AI Is Now Genuinely Strong**

1. **The Human-AI Collaboration Structure** — *Shows:* That every 2025–26 research breakthrough in the lesson shares a pattern: human provides context/framing → AI contributes conjecture or exploration → human verifies → result. *NotebookLM:* Process-flow diagram of this collaboration loop, with four concrete cases from the lesson (Gowers/GPT-5.5, gluon amplitudes/Strominger group, IMO 2025, AI Co-Mathematician/Lackenby) placed at the "AI contributes" node, emphasising that verification is never skipped.

**Illusions of Understanding**

1. **The Four Illusions Map** — *Shows:* Messeri & Crockett's four illusions as distinct concepts with the mechanism and research-practice consequence for each. *NotebookLM:* Four-quadrant diagram, one per illusion (Explanatory Breadth, Exploratory Objectivity, Monocultures of Knowing, Doing More Understanding Less), each with the name, what the researcher feels is happening, and what is actually happening. Source the wording from the lesson's card descriptions.
2. **Illusions Mapped Back to Earlier Weeks** — *Shows:* That each illusion already appeared as a concrete finding in a prior week, making the framework a unifying lens. *NotebookLM:* Mapping diagram with four illusion labels on one side and earlier-week examples on the other, connected by lines, using the lesson's table (Week 5 / explanatory breadth; Week 6 writing-as-thinking / doing more understanding less; Week 7 silent errors / doing more understanding less; Week 6 homogenisation / monoculture; Week 8 medical imaging / exploratory objectivity).

**Verification Protocols for a Moving Target**

1. **Verification Protocol Cards** — *Shows:* The eight Layer 1 verification techniques as a named, actionable set, each linked to the failure mode it targets. *NotebookLM:* Card grid of the eight techniques (Known-Answer Testing, Adversarial Prompting, Cross-Model Triangulation, Teach-It-Back, Manual Spot-Checks, Citation Verification, Reproducibility Testing, Domain-Expert Spot-Checks), each with a one-line description of what it catches and one example from the lesson. Designed as a quick-reference checklist.

---

## Week 10 — Agentic AI, RAG & Advanced Research Tools

**Agents: What They Are and What's New in 2026**

1. **Anatomy of an Agent** — *Shows:* The five-component definition (model + tools + loop + memory + permissions), with the harness visually distinguished from the model at its centre. *NotebookLM:* Labelled architecture diagram with a central model node surrounded by four harness components (Tools, Loop, Memory, Permissions), arrows showing the flow (model emits a request → tools execute → result feeds back → loop repeats), and a clear visual separation between "model" and "harness."
2. **The Harness Is the Product** — *Shows:* The benchmark evidence that harness engineering, not model swapping, moves agent scores (the LangChain 52.8% → 66.5% example; the Meta-Harness 7.7-point gain). *NotebookLM:* Before/after comparison: left, a fixed model with a thin harness and its score; right, the same model with specific harness changes listed (better system prompt, loop-detector, context management, reasoning sandwich) and the resulting jump. Keep the model icon identical on both sides to stress that only the harness changed.

**Failure Modes for Long-Horizon Tasks**

1. **Accuracy vs Reliability** — *Shows:* The Princeton finding that accuracy improved substantially across 18 months while reliability barely moved, and the four reliability dimensions (consistency, robustness, predictability, safety). *NotebookLM:* Dual-axis timeline (early 2024 to early 2026) with two trend lines — accuracy rising steeply, reliability nearly flat — and four labelled callouts naming the reliability dimensions, "predictability" highlighted as the weakest.
2. **The Agent Failure Taxonomy** — *Shows:* The three-category framework (patched / reduced-but-persistent / structural) applied to agent-specific failures, with the "what to do" column making each actionable. *NotebookLM:* Three-column framework, one per category with distinct visual weight (patched = light, reduced = medium, structural = heavy border), listing the key failures under each and a short action phrase. Scannable enough to work as a reference card.

**The Current Tool Landscape (Including MCP)**

1. **MCP: The Connector Layer** — *Shows:* How MCP works as a standard interface between agents and tools, the "USB-C for AI" framing, and its cross-vendor adoption timeline (Anthropic Nov 2024 → OpenAI Mar 2025 → Google Apr 2025 → Linux Foundation Dec 2025). *NotebookLM:* Layered architecture diagram: top, several agent products (Claude Code, ChatGPT, Gemini); middle, a single MCP protocol bar as the standard connector; bottom, the tools/data sources (Zotero, GitHub, Google Drive, email). A compact timeline strip below shows the adoption milestones, making clear why one standard replacing many bespoke integrations matters.

**RAG in 2026**

1. **Classic RAG vs Agentic RAG** — *Shows:* The structural difference between a single fetch-then-answer step and the multi-turn plan → retrieve → reflect → retrieve-again loop that defines agentic RAG and underlies Deep Research modes. *NotebookLM:* Side-by-side process diagram. Left, classic RAG as a linear three-step flow (query → retrieve once → generate). Right, agentic RAG as a loop (plan → retrieve → read & reflect → retrieve again → synthesise), with "retrieve again" visually emphasised and the loop labelled as what Deep Research modes do under the hood.
2. **Long Context vs RAG: When to Use Which** — *Shows:* The decision logic from the lesson's verdict table — paste it in vs retrieve, depending on task type, with cost and recall caveats. *NotebookLM:* Decision-tree or 2×2 mapping task type (single long document vs many sources) against approach (long context vs RAG), with a cost-sensitivity dimension and brief annotations for the "middle-of-window recall sag" caveat and the "faithful ≠ correct" reminder.

**Advanced Research Tools: A Curated Tour**

1. **A Free-Tier Research Pipeline** — *Shows:* The five-step workflow (Explore → Verify → Synthesise → Write → Audit) and which free tools sit at each step, with verification checkpoints marked as the researcher's responsibility. *NotebookLM:* Horizontal five-stage pipeline, each stage labelled with its action verb and the supporting free tool(s) (Perplexity/Kimi at Explore, Week 5 citation checks at Verify), the two verification stages marked with a "human in the loop" indicator to reinforce that agents change the tools, not the responsibility.

---

## Week 11 — Future of AI in Research & Africa's Sovereign AI Capacity

**What the Future of AI in Research Might Look Like**

1. **The Real / Overclaimed / Aspirational Framework** — *Shows:* The three-bucket classification for sorting AI-in-science claims, with decision tests for each bucket. *NotebookLM:* Decision-tree showing the three buckets (Real, Overclaimed, Aspirational) with the specific test questions for each, plus two or three examples from the lesson placed in their correct bucket.
2. **From Paper to Press Release: Where Rounding Happens** — *Shows:* The Sakana AI Scientist case — what the paper actually claimed versus what public coverage said, step by step. *NotebookLM:* Side-by-side chart tracing the result from its actual primary-source claim (one acceptance out of three, workshop level, paper withdrawn) through the three overclaimed formulations named in the lesson, illustrating where each rounding step happens.

**Speculative Futures: A Reading Guide**

1. **Map of the Speculative Literature by Calibration Level** — *Shows:* Where each major work sits on a spectrum from serious-and-falsifiable to structured-fiction, using the lesson's four-bucket taxonomy (Frameworks, Falsifiable Forecasts, Institutional Visioning, Wild Speculation). *NotebookLM:* Landscape diagram placing the named works (Krenn et al., METR, Royal Society, AI 2027, Narayanan & Kapoor, etc.) on two axes — degree of falsifiability and time horizon — so the reader sees the shape of the literature at a glance.

**The Shifting Research Landscape**

1. **The Policy vs Practice Gap in AI Disclosure** — *Shows:* The He & Bu finding: ~70% of journals have AI policies, yet only ~0.1% of papers disclose, a ~40:1 underreporting ratio in Q1 2025. *NotebookLM:* Annotated chart showing the diverging curves — rapid policy adoption across journals versus nearly flat actual disclosure — with the key numbers labelled (disclosure growth from 0.01% to 0.43%, 76 disclosing papers out of 75,172 examined).
2. **Publisher Policy Comparison: The Five Templates** — *Shows:* How OUP, Elsevier, Springer Nature, Wiley, and ACM differ in what they permit for AI use by authors and reviewers. *NotebookLM:* Comparison grid mapping the five publishers against key dimensions (AI use by authors: permitted/restricted/banned; manuscript upload to AI tools; AI use in peer review; stance on AI authorship), so a researcher can instantly identify which rules apply to their target venue.

**Sovereign AI Capacity, and Why Compute Is the Floor**

1. **The Five-Layer Sovereign AI Stack** — *Shows:* The breakdown of AI capacity into Compute / Data / Models / Policy / Talent, with the African status for each layer and which sub-lesson covers it. *NotebookLM:* Labelled stack or pyramid with the five layers, each annotated with its African status in May 2026 (Compute: partly operational; Policy: largely strategy-only) and a pointer to where the lesson goes deeper.
2. **African Compute Initiatives: Announced vs Operational** — *Shows:* The four flagship cases (CHPC, Cassava–NVIDIA, Microsoft–G42 Kenya, AU AI Factory) mapped against their actual operational status and the binding constraint that explains each outcome. *NotebookLM:* Status matrix placing each initiative on a timeline and annotating the key constraint per case (grid capacity, procurement stage, capitalisation status), making the gap between announcement and operation visually concrete.

**Data, Languages and African Model-Building**

1. **The Global Indigenous Data-Sovereignty Lineage** — *Shows:* The arc from Kaitiakitanga (Te Hiku, Māori) through the CARE Principles (drafted in Gaborone, 2018) to the Esethu Framework (ACL 2025), as traced in the lesson. *NotebookLM:* Timeline/lineage diagram tracing the three frameworks in sequence — dates, geographic anchors, the key principle each contributed — showing that Esethu is the most recent African expression of a global Indigenous tradition, not an isolated local invention.
2. **African Foundation-Model Families at a Glance** — *Shows:* The verified inventory of encoder, from-scratch decoder, adapted decoder, and named-language models, anchored on InkubaLM and MzansiLM. *NotebookLM:* Structured landscape diagram or table mapping each model family (encoders AfriBERTa/AfroXLMR/Serengeti; from-scratch decoders InkubaLM/MzansiLM; adapted Llama models AfroLlama/Lugha-Llama; named-language models) with parameter count, language coverage, and whether it is actually downloadable as of 2026.

**Policy, Institutions, and Talent**

1. **Strategy vs Governance: African AI Policy Status Matrix** — *Shows:* The Yilma & Wodajo critique made concrete — which countries have adopted strategies, which have binding legislation, and where the South African policy withdrawal sits. *NotebookLM:* Status matrix covering the countries in the lesson's table (South Africa, Nigeria, Rwanda, Kenya, Egypt, Ethiopia, Morocco) with columns for strategy status, legislation status, and key institution, making the pattern of strategy-without-governance visible alongside the SA withdrawal as the standout case.

---

## Week 12 — Integrative Capstone

**Synthesis and the Integrative Capstone**

1. **The Four-Move Disposition** — *Shows:* The four habits of mind the course has been building (pull the primary source; read for limitations; calibrate before citing; choose where you stand), arranged as a cycle rather than a list. *NotebookLM:* Infographic presenting the four moves as a recursive loop or compass — each move named, briefly defined, visually connected to the others — so a reader sees these are not sequential steps but a repeating orientation toward any claim.
2. **The Six-Prompt Pitch Structure** — *Shows:* The anatomy of the 600-word structured research pitch: what each of the six prompts asks for, its word budget, and which course week feeds it. *NotebookLM:* Structured overview mapping each prompt (Research question → AI tools → Hard limits → Local context choice → Verification protocol → Ethical commitment) to its approximate word weight and the course week(s) it draws on — a single-glance map of how the capstone assembles all twelve weeks.

---

## Advanced Track — Agentic Research with Claude Code

**What Claude Code Actually Is**

1. **Chat vs Agent: Where the Work Lives** — *Shows:* The core distinction between a chat window (work evaporates in the conversation) and Claude Code (work lands in durable files). *NotebookLM:* Side-by-side comparison: left, a chat interaction (prompt in, answer out, value lost); right, a Claude Code session where the same work ends up in named files (`scripts/`, `outputs/`, Git history, decision log). Label the principle "the chat is not the archive" at the bottom.
2. **Anatomy of the Claude Code Harness** — *Shows:* The eight capabilities (read/write files, run commands, version control, CLAUDE.md, Skills, subagents, MCP, plan mode) and how they compose around the model. *NotebookLM:* Labelled architecture diagram with the language model at the centre, surrounded by eight capability layers, each with a one-phrase note on what it contributes ("plan mode — inspect without changing").

**The Honest Case: Cost, Access, and the Shift in How You Work**

1. **The Disposition Shift: Chatting vs Managing an Agent** — *Shows:* The difference between prompt-and-read (chat) and the delegate-checkpoint-verify cycle of agentic work. *NotebookLM:* Two-column process diagram: "Chatting" as a simple back-and-forth loop; "Managing an Agent" as delegate → agent works autonomously → checkpoint → verify → researcher decides, with a callout on the growing verification burden as agent competence rises.
2. **What to Automate and What to Keep** — *Shows:* The boundary between work it is legitimate to delegate (mechanical, repetitive, adversarial) and work that must remain the researcher's own (ideas, reading, writing, judgement). *NotebookLM:* Two-zone diagram: "The Agent's Domain" (fetch, extract, format, check claims, catch inconsistencies) vs "Yours Alone" (research question, reading, drafting, interpreting results, defending claims), with a clear boundary line.

**First Contact and the Control Surface**

1. **The Permission and Safety Model** — *Shows:* How Claude Code's four-layer safety model (permission prompts, plan mode, allowlists, sandbox boundary) keeps a researcher in control of their data. *NotebookLM:* Layered diagram with the four controls arranged "most permissive" to "most protective," each noted with when to use it and what it prevents — aimed at someone who has never used a terminal.
2. **Anatomy of a CLAUDE.md File** — *Shows:* The six-to-eight working rules in the starter template and what each one protects against (a hallucination rule, a citation rule, a raw-data rule, a verification rule). *NotebookLM:* Annotated breakdown of the sample CLAUDE.md with each line linked by an arrow to the course week and integrity concept it encodes ("never fill a gap with a guess" → Week 9 hallucination; "name which files you used" → Week 5 citation).

**Reproducibility and the Reproducible Project Folder**

1. **Reproducibility vs Verification: Two Different Questions** — *Shows:* The distinction between "is this output correct?" (verification) and "could someone else inspect and repeat what I did?" (reproducibility), and why both are necessary. *NotebookLM:* 2×2 matrix with axes "Correct / Incorrect" and "Reproducible / Irreproducible," a brief example in each of the four cells to anchor the concept for a non-technical reader.
2. **The Reproducible Project Folder: Anatomy** — *Shows:* The seven-folder structure (CLAUDE.md, data/raw, data/processed, scripts, outputs, notes/decision-log.md, pre-registrations) and the question each component answers for a future replicator. *NotebookLM:* Labelled folder-tree where each directory and key file has a callout stating the question it answers ("data/raw/ — never edited: what did you actually measure?"; "notes/decision-log.md — why did you make that choice?").

**Encoding Good Habits: CLAUDE.md, Pre-registration, and Skills**

1. **How Pre-registration Works as a Gate System** — *Shows:* The staged process: write the prediction and decision rule before running anything; define what "interesting," "boring-but-worth-knowing," and "dead" each look like; then let the pre-registered gate decide whether to proceed. *NotebookLM:* Flowchart with three stages (define question → run cheapest pilot → apply gate), two branches at each gate ("clears → spend more compute on next stage" and "closed → stop and report"), with a note that the standard was set before any results were seen.
2. **Skills vs CLAUDE.md: What Each Governs** — *Shows:* The distinction between CLAUDE.md (project-level standing rules, session by session) and a Skill (a portable, reusable workflow that travels across projects). *NotebookLM:* Comparison diagram showing a single project folder with its CLAUDE.md at the root on one side, and a library of Skills shared across three different projects on the other — illustrating that CLAUDE.md is local and a Skill is universal.

**The Reproducible Workflow, End to End**

1. **Layered Verification: Which Layer Catches Which Failure** — *Shows:* The four verification layers (immutable raw data + Git make mistakes recoverable; automated assertions; verify the result not every step; the decision log chooses which diffs to read) and the distinct failure each catches. *NotebookLM:* Four stacked layers, each labelled with its mechanism and an example failure it catches (wrong-direction tangent caught by pre-registration gates; dropped column caught by automated assertions; plausible-but-wrong result caught by result-level spot check; consequential decision hidden in diffs caught by the decision log).
2. **The Reproducible Folder as Disclosure** — *Shows:* How the folder's components collectively answer "what did the AI do and what did you decide?" — making vague sentences like "AI tools were used" obsolete. *NotebookLM:* Diagram mapping the disclosure question to the folder component that answers it: "What rules did the AI work under?" → CLAUDE.md; "What judgements did you make?" → decision log; "What was the method?" → scripts; "Was the standard set in advance?" → pre-registration; "What changed, and when?" → Git history.
