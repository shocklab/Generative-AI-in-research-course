# Course glossary — review draft

**Status:** DRAFT, de-Claudified (em-dashes and contrastive phrasing removed), pending your verification. 171 canonical terms.

Verify like references: check each definition is accurate and current, fix wording, and **strike any term not worth a glossary entry**. The rail on each lesson shows only that lesson's 2–4 terms (listed at the bottom).

## ⚠︎ Possible near-duplicates to merge or split (18)

- `Agent (AI)`  ⟷  `Computer-use agent`  (subset)
- `Agent (AI)`  ⟷  `Multi-agent system`  (subset)
- `Agent (AI)`  ⟷  `Permissions (agent)`  (subset)
- `Agentic AI`  ⟷  `Agentic coding tool`  (subset)
- `Agentic AI`  ⟷  `Agentic RAG (agentic retrieval-augmented generation)`  (subset)
- `Agentic AI`  ⟷  `Agentic scaffolding`  (subset)
- `Agentic RAG (agentic retrieval-augmented generation)`  ⟷  `RAG (retrieval-augmented generation)`  (subset)
- `Benchmark`  ⟷  `Benchmark contamination`  (subset)
- `CLAUDE.md`  ⟷  `Claude Projects`  (subset)
- `CLAUDE.md`  ⟷  `Skill (Claude Code)`  (subset)
- `Data sovereignty`  ⟷  `Epistemic sovereignty`  (subset)
- `Epistemic`  ⟷  `Epistemic injustice`  (subset)
- `Epistemic`  ⟷  `Epistemic sovereignty`  (subset)
- `GAN (generative adversarial network)`  ⟷  `Generative AI`  (subset)
- `Hallucination`  ⟷  `Transcription hallucination`  (subset)
- `Multimodal`  ⟷  `Native multimodal architecture`  (subset)
- `Next-token prediction`  ⟷  `Token`  (subset)
- `Pre-training`  ⟷  `Training data`  (subset)

## Glossary A–Z (171)

- **50% time horizon** — A capability metric from the AI-evaluation group METR: the length of the longest software task an AI system can finish with at least a 50% success rate, used to track progress over time.
- **Ablation study** — An experiment in which parts of a system are removed one at a time to measure how much each contributes to overall performance, common in machine-learning research.
- **Adversarial prompting** — Deliberately probing an AI with trick questions, pushback, or reworded versions of the same query to find where its answers become unreliable or inconsistent.
- **Agent (AI)** — A language model placed in a loop so it can act repeatedly (calling tools, running code, reading results, deciding next steps) until a task is done, rather than answering once.  _(merged: agent (AI agent), AI agent (agentic AI))_
- **Agentic AI** — AI that plans and carries out multi-step tasks on its own, reading files, running code, checking results, and correcting errors, rather than answering a single prompt at a time.  _(merged: agentic tools)_
- **Agentic coding tool** — An AI coding assistant that works across multiple steps autonomously, writing code, running it, reading the output or error, and fixing it, without the user copying results back and forth.  _(merged: agentic coding tools)_
- **Agentic RAG (agentic retrieval-augmented generation)** — A method where an AI retrieves sources, reads them, decides what is still missing, and retrieves again in a loop, rather than fetching once and answering. This drives Deep Research tools.
- **Agentic scaffolding** — A software framework wrapped around an AI model that has it plan, use tools, check its own outputs, or consult copies of itself, letting it tackle tasks too complex for a single prompt-and-reply.
- **AGI (artificial general intelligence)** — A hypothetical AI able to perform any intellectual task a human can, at human level or above, across many domains, unlike today's systems that excel only at specific tasks.
- **AI factory** — A large, GPU-dense data centre built specifically to train and run AI models at national or commercial scale. The term, popularised by NVIDIA, now appears in African policy documents on sovereign compute.
- **AI use disclosure** — A formal statement, now required by most major journals, describing how and where AI tools contributed to a piece of research or writing; the human authors remain accountable for the result.  _(merged: AI use disclosure statement)_
- **AI winter** — A period of collapsed funding and interest in AI research after expectations outran what the technology could deliver; notable winters occurred in the 1970s and the late 1980s.  _(merged: AI winters)_
- **Algorithmic injustice** — The view, associated with Abeba Birhane, that bias in AI is a structural and relational problem: algorithms encode and amplify existing power relations, so it cannot be fixed by adjusting a dataset alone.
- **Alignment** — The challenge of reliably making an AI's behaviour match human values and intentions (helpful, honest, avoiding harm), and of keeping that true in novel situations it was not trained on.
- **Anchoring** — A cognitive bias in which the first information encountered, such as an AI's initial suggestion, becomes a reference point that shapes later thinking and makes genuinely different alternatives harder to consider.
- **Artisanal and small-scale mining (ASM)** — Informal, often hand-tool-based mineral extraction by individuals or small groups outside regulated industrial operations, common in cobalt mining in the Democratic Republic of Congo.
- **ASR (automatic speech recognition)** — Technology that converts spoken audio into written text automatically. Modern systems use neural networks trained on large speech collections, so accuracy varies sharply by language and accent.
- **Attention mechanism** — A component of transformer models that lets the system weigh, for each word it processes, which other words in the text are most relevant, rather than treating all context as equally important.  _(merged: self-attention)_
- **Backpropagation** — The training algorithm that makes multi-layer neural networks learnable: after each prediction, the error is traced backwards through the layers so every connection can be nudged to reduce future mistakes.
- **Benchmark** — A standardised test used to measure and compare AI models, made of problems with known answers. A high benchmark score can overstate real-world ability if the test is easier than actual tasks.
- **Benchmark contamination** — Inflated benchmark scores caused by a model having seen the test questions and answers during training. The test is no longer unseen, so high scores may reflect memorisation rather than genuine reasoning.
- **Brain drain** — The emigration of skilled or highly educated people to higher-income regions. In African AI contexts, some argue the pattern is better seen as a connected continent-and-diaspora community than a one-way loss of talent.
- **Burstiness (in AI detection)** — The natural variation in sentence length and complexity within writing. Human prose mixes short and long sentences; AI text tends to be more uniform, a feature detection tools use to flag machine-generated content.
- **Calibration** — The match between how confident an AI (or a person) is and how often it is actually right. A poorly calibrated model may claim 90% certainty while being correct only 70% of the time.
- **Carbon intensity** — The amount of carbon dioxide emitted per unit of electricity generated. It varies widely by location, so the same AI workload produces very different emissions on a coal grid versus a renewable one.  _(merged: grid carbon intensity)_
- **CARE Principles** — A 2018 framework for Indigenous data governance (Collective Benefit, Authority to Control, Responsibility, Ethics) asserting that communities must control data about them and that its use serve their interests.
- **Chain-of-thought prompting** — A technique that asks an AI to reason through a problem step by step before giving its final answer, which typically produces more considered and better-structured outputs than a direct question.
- **Chartjunk** — Visual elements in a chart (heavy gridlines, decorative backgrounds, 3D effects, redundant legends) that take up space without conveying information. The concept was coined by Edward Tufte.
- **Citation network** — The web of references connecting academic papers, where a link exists when one paper cites another. Tools can map this web to surface related work beyond what keyword search finds.
- **CLAUDE.md** — A plain-text file placed in a project folder that Claude Code reads automatically at the start of every session, holding standing instructions and context so the researcher need not repeat them each time.
- **Claude Projects** — A persistent workspace inside Claude (paid subscription) where you can upload documents and set custom instructions that stay active across conversations, so you need not re-explain your research context each time.
- **Co-citation analysis** — A bibliometric method that treats two papers as related when later work frequently cites them together, capturing conceptual kinship that the research community has signalled through its own citation behaviour.  _(merged: co-citation and bibliographic coupling)_
- **CO₂ equivalent (CO₂e)** — A standardised unit that converts all greenhouse gases into the amount of carbon dioxide that would cause the same warming, letting different emission sources be compared on a single scale.
- **Cognitive dissonance** — The psychological discomfort of holding two conflicting beliefs. In AI writing, it describes the tension when AI-generated text sounds more polished than your own yet does not represent your actual thinking.
- **Colourblind-safe palette** — A set of colours chosen so the distinctions stay visible under common colour-vision deficiencies, which affect roughly 8% of men. Examples include the Okabe-Ito palette and the viridis colour map.
- **Compositional brittleness** — The way small per-step error rates multiply across a multi-step AI task: each step may look plausible, but combined mistakes can make the final result substantially wrong.
- **Computer-use agent** — An AI agent that controls a computer graphically, reading the screen as an image and then clicking and typing, rather than calling software directly, so it can operate any application, even ones with no API.
- **Confabulation** — When an AI gives a fluent, confident explanation that sounds plausible but does not match what is actually in the image or source — fabricating a justification rather than reasoning from the evidence.
- **Confirmation bias** — The tendency to favour information that supports what you already believe. In AI-assisted analysis it arises when a prompt framed around an expected result steers the model toward confirming it.
- **Consensus Meter** — A visual indicator in the Consensus search engine that aggregates how peer-reviewed papers answer a specific research question, showing whether the literature broadly agrees, disagrees, or is divided.
- **Consequentialism** — An ethical framework that judges an action by its outcomes alone: an action is right if it produces the best overall results, such as the most benefit and least harm, for everyone affected.
- **Context window** — The maximum amount of text an AI model can hold in view at once, measured in tokens. Once a long session fills the window, the model starts losing track of earlier exchanges.
- **Critical minerals** — Raw materials deemed critical because they are economically essential to modern technologies such as chips and clean energy yet sourced from few countries, leaving supplies vulnerable to disruption.
- **Cross-model triangulation** — Running the same task on two or more AI models and comparing their outputs. Agreement raises confidence; disagreement flags a claim worth checking independently and is often more informative than either answer alone.
- **Data cleaning** — Identifying and correcting errors in a dataset before analysis (removing duplicates, standardising formats, handling missing values, fixing impossible entries) so the data accurately reflects what was measured.
- **Data leakage** — In predictive modelling, the accidental inclusion of information the model should not have, such as data from the future or the outcome itself, making it look far more accurate than it really is.
- **Data sovereignty** — The principle that a community has the right to govern how data about its members or culture is collected, used, and shared, including refusing harmful uses, and to benefit from it.
- **Decision log** — A dated running record, usually a plain-text file, of every consequential analytical choice in a project (which outliers were dropped, how missing data was handled), along with the reasons.
- **Deep learning** — A branch of machine learning using neural networks with many layers, whose depth lets the system learn increasingly abstract features from raw data, powering most modern AI including language and image models.
- **Deep Research mode** — A feature of tools such as Perplexity and Gemini that takes a question, autonomously plans and runs multiple web searches, reads the results, and produces a cited report over several minutes.
- **Deontology** — An ethical framework holding that some actions are inherently right or wrong regardless of consequences, because they involve fundamental duties or rights — a duty of honesty holds even when lying would help.
- **Devil's advocate (review role)** — A designated AI reviewer tasked solely with constructing the strongest possible objection to a paper's main claim, forcing authors to face weaknesses they may be too close to their work to see.
- **Diff** — A display of the exact lines removed and added between two versions of a file — what changed, not a description of it. Asking an AI to show the diff is a standard way to verify its work.
- **Diffusion model** — A generative AI that learns to create images by reversing a process of gradually adding noise: starting from random static, it progressively refines an image guided by a text prompt. Stable Diffusion works this way.
- **Digital forgery** — Synthetic image, video, or audio fabricated with AI to make a real person appear to say or do something they never did, often indistinguishable from genuine media without specialist tools. Commonly called a “deepfake”, a term that originated in 2017 with non-consensual pornography.  _(merged: Deepfake, deepfake)_
- **Disposition shift** — The change in how a researcher must work with capable AI: moving from interactive back-and-forth chat to acting as a manager who delegates tasks, sets checkpoints, and verifies outputs rather than watching every step.  _(merged: disposition (disposition shift))_
- **DOI (Digital Object Identifier)** — A persistent, unique code assigned to a published paper or dataset (e.g. 10.1000/xyz123) that you can enter at doi.org to confirm the item exists and reach the publisher's record.
- **Domain-trained model** — An AI model trained on data from one field, such as medical scans or satellite imagery, rather than general internet data. Such models typically outperform general-purpose AI on precise tasks within that field.
- **E-waste** — Discarded electronic equipment such as servers, GPUs, laptops, and phones, containing both recoverable valuable metals and hazardous substances that require careful handling to avoid environmental and health harm.
- **Effect size** — A number measuring how large or practically meaningful a difference or relationship is, independent of sample size. A result can be statistically significant yet have a tiny, practically unimportant effect size.
- **Embeddings** — Numerical representations of text produced by a neural network, where passages with similar meanings get similar numbers, letting a system measure conceptual closeness between a query and millions of documents almost instantly.
- **Embodied carbon** — The greenhouse-gas emissions released when manufacturing a physical object; for AI, the carbon cost of making chips, servers, and data centres, as distinct from emissions from the electricity used during operation.
- **English hegemony (in academic publishing)** — The structural dominance of English as the required language for high-status academic publishing, which disadvantages researchers whose first language is not English regardless of the quality of their ideas.
- **Epistemic** — Relating to knowledge and how we come to know things. An epistemic concern is a worry about whether a belief is genuinely well-founded, beyond how convincing it feels.
- **Epistemic injustice** — A wrong done to someone specifically as a knower or knowledge-producer — for example, when a researcher imposes external interpretive categories onto a community's experience, distorting what participants actually meant.
- **Epistemic sovereignty** — The capacity of a community or region to generate, govern, and apply knowledge on its own terms — in AI, to shape research from its own intellectual traditions rather than only adopting frameworks made elsewhere.
- **Exploratory data analysis (EDA)** — An early-stage examination of a dataset using summary statistics, plots, and correlation checks to understand its structure, spot problems like missing values, and form hypotheses before formal modelling.
- **Faithfulness (in RAG evaluation)** — A metric checking whether a generated answer is actually supported by the retrieved passages rather than adding unsupported claims. A faithful answer can still be wrong if those passages were themselves incorrect.
- **Falsifiable forecast** — A prediction specific enough that it could be proven wrong, naming a date, number, or milestone someone could check, as opposed to vague speculation that cannot be tested against evidence.
- **Fine-tuning** — Continuing to train a pre-trained model on a smaller, focused dataset so it learns new behaviour or domain knowledge without starting over. It is far cheaper than original training but can meaningfully change what the model does.
- **Formal verification (Lean)** — Checking a mathematical proof with software that enforces every logical step, making errors impossible to hide. Lean is a widely used tool; a Lean formalisation is a machine-checked certificate that a proof is correct.
- **Foundation model** — A large AI model trained on a broad body of data that can be adapted to many specific tasks. African-language examples include InkubaLM, built specifically for under-represented languages.
- **Frontier model** — A large AI model at the current leading edge of measured capability — the best publicly available models from well-resourced labs. Which models qualify changes every few months as new releases arrive.
- **GAN (generative adversarial network)** — An architecture that trains two neural networks in competition, a generator producing fake outputs and a discriminator trying to detect them, until the generator's outputs are statistically indistinguishable from real data.
- **Generative AI** — AI systems that produce new content (text, images, code, audio) in response to a prompt, rather than only classifying or retrieving existing data. ChatGPT, Claude, and Midjourney are widely used examples.
- **Ghost work** — The hidden human labour behind AI systems (data labelling, content tagging, quality checking) done by contractors kept invisible so AI appears fully automated. The term was coined by Mary Gray and Siddharth Suri (2019).
- **Git** — A version-control system that records snapshots, called commits, of a project's files over time, so you can see what changed between steps, roll back mistakes, and share a verifiable history of your work.
- **Goodhart's Law** — The principle that when a measure becomes the target of optimisation, it stops being a reliable measure. Models trained to score well on benchmarks may inflate scores without improving at the real tasks those tests proxy.
- **Hallucinated citation** — A bibliographic reference generated by an AI that does not correspond to any real published work, or that misattributes authors, venue, or DOI — plausible-sounding but unverifiable in any database.
- **Hallucination** — When an AI confidently produces false or fabricated information (a nonexistent citation, a wrong formula, an invented fact) presented with no sign it is incorrect, because the model predicts plausible text rather than retrieving verified facts.
- **Harness** — The software wrapped around a language model to make it an agent: the tools it can call, the files it can see, the loop that runs it repeatedly, the memory across steps, and the permissions that limit it.
- **ICMJE criteria** — The International Committee of Medical Journal Editors' four requirements for authorship: substantial contribution, drafting or revising the work, approving the final version, and accountability for it. Widely adopted beyond medicine.
- **Idea monoculture** — The convergence of research ideas across many researchers toward the same topics and approaches, driven by everyone drawing on AI tools trained on the same underlying data and producing similar outputs.
- **Immutable raw data** — The principle that original data files are never edited or overwritten; all cleaning and processing produces new files elsewhere, so the full analysis chain can always be rebuilt from the unchanged source.
- **Inference** — Running an already-trained AI model to generate a response. Distinct from training, inference is the repeated ongoing cost; across billions of queries, cumulative inference energy quickly exceeds the one-time training cost.
- **Integrity spectrum** — A scale for weighing the ethical risk of AI writing assistance, from low-risk surface corrections like grammar to high-risk substantive generation like arguments or data descriptions, with risk rising as AI shifts from form to content.
- **IRB (Institutional Review Board)** — An ethics committee that reviews research involving human participants, called an IRB in the US and a Research Ethics Committee elsewhere. Using AI with participant data may require amended approval.
- **Jevons paradox** — The observation that making a resource cheaper or more efficient tends to increase total consumption rather than reduce it, because lower costs open new uses. Named after economist William Stanley Jevons.
- **Knowledge-transforming writing** — Writing that forces you to reorganise, clarify, and test ideas rather than record already-formed thoughts. Turning ideas into linear prose is itself a form of reasoning, in contrast to mere transcription.
- **Large language model (LLM)** — An AI system trained on vast amounts of text that can generate, summarise, translate, and reason about language. LLMs such as Claude, ChatGPT, and Gemini are the core of most modern AI assistants.  _(merged: general-purpose LLM (large language model))_
- **Long context** — A model's ability to take in very large amounts of text in a single prompt — up to a million words or more on 2026 frontier models. A long input does not guarantee the model attends carefully to all of it.
- **Long-horizon planning collapse** — A failure in AI agents where picking the locally best next step each time leads the whole task into a dead end, because early choices that look fine commit the agent to a path whose costs surface only later.
- **Long-tail problem** — The observation that AI performance degrades on rare or niche topics because they appear infrequently in training data; the rarer the topic, the more likely the model is to hallucinate or answer wrongly.
- **LoRA (Low-Rank Adaptation)** — A parameter-efficient fine-tuning method that inserts small trainable matrices into a frozen model, updating only a tiny fraction of parameters, so a large model can be adapted on modest hardware near full-fine-tuning quality.
- **Lost in the middle** — The documented tendency of AI models to attend more reliably to content at the start and end of a long input than to the middle, making them less dependable at finding details buried in the interior.
- **Low-resource language** — A language for which very little digitised text, audio, or labelled data exists, making AI models harder to train. Most African languages are low-resource because they are under-represented in current training datasets.
- **MCP (Model Context Protocol)** — An open standard, introduced by Anthropic in 2024, that lets an AI agent connect to external tools and data sources (databases, file storage, reference managers) through one consistent interface rather than custom wiring for each.  _(merged: Model Context Protocol (MCP), MCP connector (Model Context Protocol))_
- **Metered API use** — A pay-as-you-go pricing model where you are charged per unit of AI processing (tokens) used, rather than a flat monthly fee; costs can mount quickly during long autonomous runs.
- **Mixture of experts (MoE)** — An architecture where a large model is split into many specialised sub-networks (experts), but each input is routed through only a small subset, keeping computation per query low despite a very large total parameter count.
- **Modality** — A category of input type — image, audio, video, or document text. Different AI models support different combinations of modalities, each with its own reliability profile for research use.
- **Multi-agent system** — An AI setup in which several specialised components work together, each handling a different sub-task, rather than one model doing everything alone.  _(merged: multi-agent review)_
- **Multimodal** — Describes an AI model that can process or generate more than one type of data, for example text and images together, or text, audio, and video, rather than working with text alone. Most large models since 2023 are multimodal.  _(merged: multimodal AI)_
- **Multiple comparisons problem** — The inflation of false positives when many statistical tests run on the same data: at a 5% threshold, about one in twenty tests looks significant by chance even when nothing real is happening.
- **Native multimodal architecture** — A model design that processes audio, visual, and text content together in a single pass, letting it reason across modalities — such as noticing when a speaker's words contradict what is shown on screen.
- **Neural network** — A computational system loosely inspired by the brain, made of layers of simple mathematical units (neurons) connected together. By adjusting connection strengths through training, it learns to recognise patterns in data.
- **Next-token prediction** — The main learning objective in pre-training: given a sequence of words or word-pieces, the model is trained to predict the most probable next item, using each prediction's error to update its parameters.
- **OCR (optical character recognition)** — Software that converts a scanned image of text into machine-readable characters. When a PDF is a photograph of a page rather than embedded text, OCR must run before AI can read or search its content.
- **Open-weight model** — An AI model whose trained parameters are publicly released so anyone can download, run, or modify it, in contrast to closed, proprietary models whose weights stay private and are reachable only through an API.
- **Overplotting** — A problem in dense charts where many data points are drawn over each other at full opacity, creating an opaque mass that hides the underlying distribution rather than revealing it.
- **P-hacking (outcome-driven analysis)** — Selecting or adjusting an analytical method after seeing the data to produce statistically favourable results, rather than choosing the method on principled grounds before analysis begins.
- **Peer review** — The process by which submitted manuscripts are evaluated by independent expert researchers before publication. Manuscript confidentiality during review is the main reason most journals bar reviewers from uploading papers to AI services.
- **Permissions (agent)** — The defined boundary of actions an agent may take without checking with a human (read files only, write files, spend money, and so on), setting how much autonomy it has regardless of model capability.
- **Perplexity (in AI detection)** — A statistical measure of how predictable each word choice is in a text. AI writing tends to have low perplexity because models favour highly probable next words; human writing is more variable and harder to predict.
- **Plan mode** — A read-only setting in Claude Code where the AI can inspect files and propose actions but is prevented from making any changes — the safest way to let an agent examine data you cannot afford to have altered.
- **Pollution loop** — The self-reinforcing cycle in which hallucinated citations published in real papers get indexed by databases, absorbed into future AI training data, and then reproduced with even greater false confidence.
- **POPIA (Protection of Personal Information Act)** — South Africa's data-protection law. Section 72 restricts sending personal information to servers in other countries unless the recipient meets equivalent privacy standards, making cross-border AI tool use a compliance issue.
- **Positional encoding** — Information added to each token before processing to tell the model where in the sequence that token sits, since transformers otherwise treat all positions as equivalent.
- **Power Usage Effectiveness (PUE)** — A ratio of how efficiently a data centre uses electricity: a PUE of 1.0 means all power reaches the computers, while higher values like 1.5 mean cooling and other overhead consume extra energy on top of the compute.
- **Pre-registration** — Writing down your research question, predicted outcome, and decision rules before analysing data, then committing that record, so the standard cannot be quietly shifted after the results are known.
- **Pre-training** — The initial phase of building a large language model, in which it learns from vast quantities of text by repeatedly predicting the next word or token, before any task-specific tuning takes place.
- **Premature convergence** — The tendency for AI to narrow quickly toward a single answer or approach instead of keeping many possibilities open, closing off exploration before the full space of ideas has been considered.
- **Preprint** — A research paper shared publicly before completing peer review, typically posted on a repository such as arXiv. Preprints are citable but have not yet been checked by independent referees.
- **Prompt engineering** — Deliberately crafting the wording, structure, and context of instructions given to an AI model to obtain more useful, accurate, or targeted responses.
- **Prompt injection** — An attack in which hostile instructions hidden inside content an agent reads (a web page, email, or document) hijack its behaviour, because the model cannot reliably tell data from instructions.
- **Publication bias** — The tendency of scientific literature to over-represent studies with positive or significant results, because null findings are less likely to be submitted or accepted. AI models trained on published work inherit this skew.
- **Radiative forcing** — A warming effect on the atmosphere beyond direct carbon emissions. Aviation's contrails and nitrogen oxides at altitude trap heat independently of CO₂, roughly doubling aviation's total climate impact over its carbon footprint alone.
- **RAG (retrieval-augmented generation)** — A technique where an AI searches a specific set of documents at query time and draws its answer from what it finds, grounding responses in real sources rather than the model's general training memory alone.
- **RAGAS (Retrieval-Augmented Generation Assessment)** — An open framework for measuring RAG quality without hand-written answers. It separately scores whether the right passages were retrieved and whether the generated answer stays within what those passages say.
- **Redundant encoding** — Using two or more visual channels, such as colour and shape, to convey the same information, so readers who cannot distinguish one channel can still read the chart using another.
- **Relational ethics** — An ethical approach that begins from relationships and communities rather than individual rights, asking how an action affects the social bonds through which people live and flourish.
- **Reliability (vs accuracy)** — In agentic AI, accuracy measures whether individual actions are correct, while reliability measures whether the agent consistently completes whole multi-step tasks and recovers from its own errors. One can improve while the other stays flat.
- **Reproducibility** — A property of research where another person, or you later, can inspect exactly what was done and repeat it from the same starting point. Distinct from verification, which asks whether a result is correct.
- **Retrieval-based tool** — A search tool such as Semantic Scholar, Elicit, or Consensus that looks up records in a real database of published papers, so every result it returns actually exists — unlike a generative AI producing text from patterns.
- **Reversal curse** — A failure in early language models where knowing "A is B" did not help infer "B is A." Documented in GPT-3.5/4-era systems but largely absent in 2025–2026 frontier models, it is a superseded finding still cited as current.
- **Reverse outline** — An editing technique where you take a finished draft and work backwards to extract the structure actually present, then compare it with your intended structure to reveal missing claims, stray paragraphs, or broken logic.
- **RIA Just AI Framework** — A framework from the Research ICT Africa think-tank that extends beyond conventional responsible AI to demand restorative and redistributive justice, structured around nine inquiries spanning human rights, epistemic justice, data justice, and sustainability.
- **RLHF (Reinforcement Learning from Human Feedback)** — A training technique where human raters compare or score model responses, and those preferences train the model toward outputs humans prefer — embedding the raters' values, assumptions, and blind spots into its behaviour.
- **Scaling laws** — Empirical relationships showing that a model's performance improves predictably as model size, training data, and compute increase, letting labs forecast the payoff of an expensive training run before committing to it.
- **Self-supervised learning** — A training approach where the data itself supplies the learning signal; for language models the next word acts as the label, so no human annotation is needed to train on billions of documents.
- **Semantic search** — A search method that finds documents by meaning rather than exact word matches, so a query about exercise and mood can surface papers using completely different phrasing such as physical activity and depression.
- **Semiconductor foundry node** — A measure of how small a chip's transistors are, given in nanometres (e.g. 5 nm). Smaller nodes pack more computing power into less space and need the most advanced, scarce fabrication facilities to make.
- **Silent error** — An error in AI-generated code that produces no crash or warning but yields wrong results — for example using the wrong variable. Because the output looks clean, the mistake can go undetected.
- **Simpson's paradox** — A statistical phenomenon where a trend in an overall dataset reverses or vanishes when the data is split into subgroups, usually because an unaccounted-for variable is distributed unevenly across those groups.
- **Skill (Claude Code)** — A reusable, packaged workflow stored in a project's .claude/skills/ folder and triggered on demand, giving an AI agent a tested, step-by-step procedure to follow instead of ad-hoc prompting.  _(merged: skills (slash commands))_
- **Smart citations** — A feature of Scite.ai that classifies each citation as supporting, contrasting, or merely mentioning the original paper, letting you see at a glance whether later research agreed with or challenged a finding.
- **Sovereign AI** — A nation's or community's capacity to develop, govern, and control AI on its own terms — who owns the infrastructure, whose data is used, whose rights the systems protect. Definitions vary from hardware ownership to community rights.
- **Speaker diarisation** — The automated process of labelling who said which words in a multi-speaker recording. AI diarisation remains imperfect, and incorrect speaker attribution can corrupt qualitative analysis, so it requires manual verification.  _(merged: speaker diarization)_
- **Stationarity** — A property of a time series whose mean, variance, and other statistics stay roughly constant over time. Many standard time-series models require it; a series with a rising trend or changing volatility must be transformed first.
- **Strategy as governance** — Publishing national AI policy documents as a substitute for actual governance, without the binding legislation, enforcement bodies, or institutions needed to make policy effective. Some scholars argue this describes most African AI governance so far.
- **Subagent** — A second AI agent spawned by a primary agent to handle a specific, bounded task, such as independently verifying an analysis, without sharing the first agent's assumptions or context.
- **Surveillance capitalism** — A term coined by Shoshana Zuboff for a business model that harvests behavioural data from users, analyses it to predict behaviour, and sells those predictions — treating human experience itself as raw material for profit.
- **Sycophancy** — A tendency in AI models to agree with the user or say what they seem to want to hear, even when the user is wrong, arising from training that rewards responses humans rate favourably.
- **Synthetic data** — Data generated computationally to mimic real experimental results (plausible distributions, correlations, effect sizes) without any underlying observation. In misconduct, AI can produce synthetic datasets hard to distinguish from genuine ones.
- **Systematic review** — A structured survey of all available research on a question, using documented, reproducible search criteria and explicit rules for selecting and comparing studies, as opposed to a narrative review based on the author's judgment.
- **Temporal reasoning** — The ability to understand events in time order within a recording — when something was first mentioned, what happened between two timestamps, how an argument developed. Current AI does this unreliably and should be checked against timestamps.
- **Text layer** — The embedded, selectable text stored inside a PDF as actual characters rather than a picture. PDFs with a text layer can be searched and copied; scanned PDFs lack one and need OCR before extraction.
- **Token** — The basic unit of text a language model reads and produces — roughly a word or word-fragment (e.g. "unbelievable" may split into "un", "believe", "able"). Models process text one token at a time.
- **Training data** — The large collection of text and other content an AI model learns from during development. Biases, gaps, or errors in that data are absorbed by the model and can shape its outputs in ways not always visible to the user.
- **Transcription hallucination** — A failure in AI transcription where the model generates text that was never spoken, inventing sentences, fabricating names, or silently dropping content, rather than faithfully converting the audio.
- **Transformer** — A neural network architecture introduced in 2017 that processes whole sequences of text at once and uses attention to weigh how relevant each word is to every other. It underpins virtually all modern large language models.
- **Turing Test** — A benchmark proposed by Alan Turing in 1950: if a machine can hold a text conversation a human judge cannot distinguish from talking to another person, it is taken to have demonstrated intelligence.
- **Ubuntu** — A southern African philosophical tradition captured in the phrase "a person is a person through other people," treating personhood and ethical action as constituted through relationships and community rather than individual reason alone.  _(merged: ubuntu (relational ethics))_
- **Unit test** — A short, focused check that verifies one specific function does what it claims: given a known input, you assert the expected output and automatically flag any mismatch.
- **Version control** — A system for saving successive named snapshots of a document so you can trace what changed, when, and why — from manually dated file copies to tools such as Google Docs version history or Git.
- **Vibe coding** — A style of AI-assisted programming where the user describes what they want in natural language and accepts or adjusts the output based on whether the result looks right, rather than verifying every line in detail.
- **Virtue ethics** — An ethical framework concerned with the character of the person acting rather than rules or outcomes, asking what habits and qualities to cultivate — applied to AI, the long-term effect of repeated choices on a researcher's intellectual character.
- **VLM (vision-language model)** — An AI model that processes images and text together, so it can answer questions about a picture or describe what it sees. General assistants such as Claude, ChatGPT, and Gemini act as VLMs when given an image.
- **WER (word error rate)** — The standard measure of transcription accuracy: the percentage of words that are wrong (substituted, deleted, or inserted) against the correct reference text. A 10% WER means about one word in ten is incorrect.
- **Wet-lab validation** — Physical laboratory experiments using cells, chemicals, or living organisms that test whether a prediction holds in the real world, as distinct from a purely computational result.
- **Whisper** — An open-source automatic speech recognition model from OpenAI that converts spoken audio into written text. Trained on a large multilingual dataset, it is widely used for transcription in research.
- **Writing homogenisation** — The tendency of AI writing tools to push authors toward a single dominant style, typically Western native-English prose, reducing the stylistic and cultural diversity that naturally exists across writers and linguistic communities.

## Per-lesson terms (what each rail shows)


### week-1
- *A lightning tour of AI* — _(none)_
- *An introduction to Transformers* — Transformer, Attention mechanism, Diffusion model
- *But what is a neural network* — Neural network, Deep learning, Transformer
- *Current Generative AI Landscape* — Large language model (LLM), Multimodal, Open-weight model, Mixture of experts (MoE)
- *Foundations of Generative AI* — Generative AI, AI winter
- *Hands-On Exploration* — Generative AI, AI winter
- *History of AI From Neurons to Neural Networks* — Neural network, Turing Test, Backpropagation, Transformer
- *Understanding How Generative AI Works* — Token, Attention mechanism, Diffusion model, GAN (generative adversarial network)

### week-2
- *Fine-Tuning RLHF and Alignment* — Fine-tuning, RLHF (Reinforcement Learning from Human Feedback), Alignment, LoRA (Low-Rank Adaptation)
- *How AI Image Generation Works* — Diffusion model
- *LLM Architecture Deep Dive* — Token, Attention mechanism, Positional encoding, Mixture of experts (MoE)
- *Training Large Language Models* — Pre-training, Next-token prediction, Self-supervised learning, Scaling laws

### week-3
- *Critical Minerals and AI* — Critical minerals, Artisanal and small-scale mining (ASM), E-waste, Semiconductor foundry node
- *Infrastructure Scale and the Rebound Problem* — Jevons paradox, Power Usage Effectiveness (PUE), Embodied carbon, Carbon intensity
- *Sustainable AI What Can Be Done* — Carbon intensity, CO₂ equivalent (CO₂e), Embodied carbon, LoRA (Low-Rank Adaptation)
- *What Does AI Actually Consume* — Inference, Agentic AI, Carbon intensity, Radiative forcing

### week-4
- *Applying Ethics Case Studies and Your Framework* — Epistemic injustice, P-hacking (outcome-driven analysis), RIA Just AI Framework
- *Ethical Frameworks and Four Lenses* — Consequentialism, Deontology, Ubuntu, Virtue ethics
- *The Broader Landscape of AI Ethics* — Ghost work, Surveillance capitalism, Digital forgery, CARE Principles
- *Transparency Authorship and Integrity* — ICMJE criteria, Training data, Publication bias, IRB (Institutional Review Board)
- *Ubuntu Relational Ethics and the Just AI Framework* — Ubuntu, Relational ethics, Algorithmic injustice, Data sovereignty

### week-5
- *Building Your Research Workflow with Claude* — Claude Projects, CLAUDE.md, Skill (Claude Code)
- *Free Tools Deep Dive* — RAG (retrieval-augmented generation), Citation network, Co-citation analysis, Hallucination
- *Hands-On Activities and Assessment* — Hallucinated citation, RAG (retrieval-augmented generation)
- *Paid Tools and When They Are Worth It* — Systematic review, Smart citations, Consensus Meter
- *The AI Literature Review Landscape* — Semantic search, RAG (retrieval-augmented generation), Embeddings, Co-citation analysis
- *The Hallucinated Citation Crisis* — Hallucination, Retrieval-based tool, Pollution loop, DOI (Digital Object Identifier)

### week-6
- *AI Writing Tools Landscape and Honest Assessment* — Large language model (LLM), Writing homogenisation, English hegemony (in academic publishing)
- *Building Your AI Writing Workflow* — Reverse outline, Version control
- *Hands-On Activities and Assessment* — Prompt engineering, Chain-of-thought prompting, AI use disclosure
- *Research Ideation with AI* — Anchoring, Idea monoculture, Premature convergence, Chain-of-thought prompting
- *Scientific Integrity and the Writing Pipeline* — Integrity spectrum, Perplexity (in AI detection), Burstiness (in AI detection), Synthetic data
- *Using AI to Review Your Own Work* — Multi-agent system, Context window, Devil's advocate (review role), Ablation study
- *Writing as Thinking* — Knowledge-transforming writing, Cognitive dissonance, Virtue ethics

### week-7
- *AI-Assisted Data Analysis in Practice* — Silent error, Exploratory data analysis (EDA), Data leakage, Simpson's paradox, Multiple comparisons problem
- *Agentic Data Analysis* — Agentic AI, MCP (Model Context Protocol), CLAUDE.md
- *Building Your Data Analysis Workflow* — Exploratory data analysis (EDA), Effect size, Stationarity, CLAUDE.md
- *Hands-On Activities and Assessment* — Data cleaning, Confirmation bias
- *Natural Language to Code* — Agentic coding tool, Context window, Vibe coding
- *Verification of AI-Generated Code* — Agentic AI, Unit test, Data leakage
- *Visualization with AI* — Chartjunk, Overplotting, Redundant encoding, Colourblind-safe palette

### week-8
- *AI and Scientific Images* — VLM (vision-language model), Benchmark, Domain-trained model, Confabulation
- *Document Intelligence* — OCR (optical character recognition), Text layer, Lost in the middle
- *Hands-On Activities and Assessment* — Whisper, WER (word error rate)
- *Transcription and Audio Analysis* — WER (word error rate), Transcription hallucination, ASR (automatic speech recognition), Speaker diarisation
- *Video and Multimodal Workflows* — Native multimodal architecture, Temporal reasoning, Speaker diarisation, Lost in the middle
- *What Multimodal AI Can See Hear and Read* — Multimodal, Modality, Context window, Speaker diarisation

### week-9
- *Hands-On Activities and Assessment* — Hallucination, Frontier model, Cross-model triangulation
- *Illusions of Understanding* — Epistemic, RLHF (Reinforcement Learning from Human Feedback), Calibration
- *The Trajectory of LLM Capabilities* — Frontier model, Benchmark, Goodhart's Law, Benchmark contamination
- *Three Categories of Failure* — Sycophancy, Calibration, Long-tail problem, Compositional brittleness
- *Verification Protocols for a Moving Target* — Adversarial prompting, Cross-model triangulation, Reversal curse
- *Where AI Is Now Genuinely Strong* — Formal verification (Lean), Agentic scaffolding, Hallucination

### week-10
- *Advanced Research Tools - A Curated Tour* — Deep Research mode, MCP (Model Context Protocol), Prompt injection
- *Failure Modes for Long-Horizon Tasks* — Reliability (vs accuracy), Long-horizon planning collapse, Prompt injection, Compositional brittleness
- *Hands-On Activities and Assessment* — Deep Research mode, POPIA (Protection of Personal Information Act)
- *RAG in 2026* — Agentic RAG (agentic retrieval-augmented generation), Long context, RAGAS (Retrieval-Augmented Generation Assessment), Faithfulness (in RAG evaluation)
- *The Current Tool Landscape and MCP* — MCP (Model Context Protocol), Computer-use agent, Prompt injection
- *What Agents Are and Whats New in 2026* — Agent (AI), Harness, Permissions (agent)

### week-11
- *Data Languages and African Model-Building* — Data sovereignty, Foundation model, Benchmark, Low-resource language
- *Policy Institutions and Talent* — Strategy as governance, Hallucinated citation, Brain drain
- *Sovereign AI Capacity and Why Compute Is the Floor* — Sovereign AI, Epistemic sovereignty, CARE Principles, AI factory
- *Speculative Futures - A Reading Guide* — AGI (artificial general intelligence), 50% time horizon, Epistemic sovereignty, Falsifiable forecast
- *The Shifting Research Landscape* — AI use disclosure, Prompt injection, Peer review
- *What the Future of AI in Research Might Look Like* — Agentic coding tool, Wet-lab validation, Preprint, Multi-agent system

### week-12
- *Synthesis and the Integrative Capstone* — RAG (retrieval-augmented generation)

### advanced
- *Claude Code as a Research Environment* — Agent (AI), Harness, MCP (Model Context Protocol)
- *Encoding Good Habits - CLAUDE.md Pre-registration and Skills* — CLAUDE.md, Pre-registration, Skill (Claude Code), Subagent
- *First Contact and the Control Surface* — Plan mode, CLAUDE.md, Context window, Diff
- *Reproducibility and the Project Folder* — Reproducibility, Pre-registration, Decision log, Immutable raw data
- *The Honest Case - Cost Access and Disposition* — Agent (AI), Metered API use, Disposition shift
- *The Reproducible Workflow End to End* — Git, Decision log, Pre-registration
