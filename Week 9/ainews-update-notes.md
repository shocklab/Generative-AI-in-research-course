# Week 9 Update Notes — AINews Digest (Late April – 9 May 2026)

These notes are for the session writing/updating Lesson 9 (Critical Evaluation & Limitations of AI). They summarise models and developments that are either missing from or should be updated in the current lesson content, drawn from AINews emails (swyx+ainews@substack.com) from approximately 30 April – 9 May 2026.

---

## Models Missing from Sub-lesson 9.1 (The Trajectory of LLM Capabilities)

### Priority 1 — Should definitely be added

**Kimi K2.6** (Moonshot AI, China)
- Open-weights, 1T total parameters, 32B active (MoE architecture)
- Apache 2.0 licence
- Performance: matches or beats DeepSeek V3 on coding and math benchmarks; competitive with some closed-weight frontier models
- Significance for lesson 9: a Chinese open-weight model reaching near-frontier performance at 32B active params is a major trajectory data point; demonstrates the speed of open-weight catch-up
- Fits in the **Open-Weights Frontier** model cards section alongside DeepSeek V4

**Qwen 3.6** (Alibaba, China)
- The current lesson mentions Qwen but hasn't been updated to 3.6
- Key new feature: **Multi-Token Prediction (MTP)** — predicts multiple future tokens per forward pass, significant inference speed-up
- MTP is emerging as a cross-model technique (also in Gemma 4) and could warrant a brief mention in the trajectory narrative
- Hybrid thinking model (can toggle chain-of-thought on/off)

**Gemma 4** (Google DeepMind)
- Open-weights
- Also implements MTP
- Notable because it pairs with DeepMind's broader push on reasoning (see co-mathematician below)

### Priority 2 — Worth mentioning

**GPT-5.5 Instant** (OpenAI)
- Launched ~6 May 2026
- Positioned as a faster, cheaper variant of GPT-5.5
- Relevant to the lesson's point about the rapid pace of model releases and the "trajectory" framing

**Zyphra ZAYA1-74B**
- Novel architecture (not standard transformer)
- Hybrid model combining different attention mechanisms
- Interesting as a data point that architectural innovation hasn't stopped — relates to the lesson's point about whether current limitations are structural or just engineering problems not yet solved

---

## Developments Relevant to Specific Sub-lessons

### For 9.1 — The Trajectory of LLM Capabilities

**ProgramBench** (new benchmark, ~May 2026)
- Tests whole-repository code generation (not just single-file or function-level)
- Result: **0% success rate** across all frontier models tested
- This is an excellent addition to the **Benchmark Literacy** section — it's a concrete, current example of a task where models completely fail, and it illustrates the gap between impressive demo performance and real software engineering
- Connects well to the existing Goodhart's Law / benchmark gaming discussion

**Multi-Token Prediction (MTP)** as a cross-cutting trend
- Both Qwen 3.6 and Gemma 4 implement this
- Worth a brief mention as an inference-time optimisation that's becoming standard in open-weight models
- Doesn't change capability per se, but changes the speed/cost trajectory

### For 9.3 — Where AI Is Now Genuinely Strong

**DeepMind co-mathematician system**
- Achieved **48% on FrontierMath Tier 4** problems
- This is a significant jump — the lesson currently discusses frontier math performance but this specific result should be added
- Reinforces the lesson's existing narrative about AI in mathematics being genuinely strong and rapidly improving
- Source: AINews 9 May 2026

### For 9.4 — Illusions of Understanding

**"Vibe coding" culture**
- AINews coverage of developers increasingly writing code by describing what they want to AI and accepting the output without deep review
- Perfect real-world example of Messeri & Crockett's "illusion of exploratory breadth" — the AI makes coding feel more productive, but the developer's actual understanding of the codebase may be shallower
- Could be used as a discussion prompt or example in the illusions section

### For 9.5 — Verification Protocols for a Moving Target

**Anthropic's "Teaching Claude Why" alignment work**
- Anthropic published research on training models to understand the reasons behind safety rules, not just the rules themselves
- Relevant to the verification discussion: if models are being trained to understand *why* they should behave certain ways, does that change how we verify their outputs? Does understanding motivation make verification easier or harder?
- Could be a brief mention or discussion prompt

### For 9.2 — Three Categories of Failure

**DeepSeek V4 Pro on FoodTruck Bench**
- FoodTruck Bench tests real-world agentic tasks (multi-step, tool-using scenarios)
- Models still struggle significantly with these compound tasks
- Supports the lesson's "reduced but persistent" failure category — individual capabilities improve but chaining them reliably remains hard

---

## Suggested Update Priorities

1. **Add Kimi K2.6 model card** to the Open-Weights Frontier section in 9.1 — this is the biggest gap
2. **Update Qwen entry** to 3.6 with MTP mention in 9.1
3. **Add Gemma 4** to open-weights section in 9.1
4. **Add ProgramBench** (0% whole-repo) to Benchmark Literacy section in 9.1 — powerful pedagogical example
5. **Add DeepMind co-mathematician** (48% FrontierMath Tier 4) to the mathematics section in 9.3
6. **Consider adding vibe coding** as an example in 9.4's illusions discussion
7. **Lower priority**: GPT-5.5 Instant, ZAYA1, FoodTruck Bench, "Teaching Claude Why"

---

## Source Emails

All sourced from swyx+ainews@substack.com:
- 9 May 2026: "Anthropic growing 10x/year" — Kimi K2.6, DeepMind co-mathematician, ZAYA1, Teaching Claude Why
- 8 May 2026: "GPT-Realtime-2" — voice models, Anthropic Natural Language Autoencoders
- 7 May 2026: "Anthropic-SpaceX deal" — partially reviewed
- 6 May 2026: "Silicon Valley gets Serious about Services" — GPT-5.5 Instant, Qwen 3.6, Gemma 4, ProgramBench, FoodTruck Bench
- 1 May 2026: "Agents for Everything Else" — partially reviewed
- 30 Apr 2026: "The Inference Inflection" — partially reviewed

Note: three of the six emails were too large to fully load in the retrieval pass (7 May, 1 May, 30 Apr). The above captures the key items but there may be additional relevant details in those issues.
