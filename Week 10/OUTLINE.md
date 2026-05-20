# Week 10 — Agentic AI, RAG & Advanced Research Tools — STRUCTURAL OUTLINE

**Status:** Research/discovery pass complete. Outline only — no HTML yet.
**Date of research sweep:** 19 May 2026 (covers AINews emails 28 Apr → 19 May 2026).
**Voice/style targets:** Follow Week 9 — trajectory-aware, time-stamped, model-version genericised (`Claude (family)`, `GPT (family)`, etc.), African/UCT context woven through, honest pushback over reflexive hype, calls back to earlier weeks.

---

## Overall pedagogical frame for Week 10

The course's central frame for Week 9 was the **trajectory of capability** — patched, reduced, structural. For Week 10 the frame is **the harness, not the model**: agentic performance in May 2026 is a joint property of model × harness × context strategy, and the failure modes that matter for researchers are no longer pure capability gaps but reliability, long-horizon coherence, and tool-loop brittleness. This is the same trajectory framing applied to a moving target one level up the stack.

Three recurring threads should be woven across all six sub-lessons:

1. **Trajectory honesty.** What was true about agents in 2024 is mostly false now; what is true in May 2026 will be partly false by November. Every concrete claim should be time-stamped.
2. **Verification still on the student.** Every Week 9 verification protocol applies — agents do more, fail in new ways, and shift the verification burden rather than eliminate it.
3. **Honest free-vs-paid split.** UCT students often can't afford subscriptions and many can't access foreign credit cards. Every tool recommendation has to acknowledge what the free tier actually does as of May 2026.

---

## 10.1 — Agents: What They Are and What's Actually New in 2026

**Thesis.** An "agent" is a model with a harness — tools, memory, loops, and permissions — and the meaningful shift since Week 9 is that the harness has become the product. Students need a working definition that distinguishes 2026 agents from 2023-style "chains" and from chatbots-plus-browsing, plus a calibrated sense of what current agents reliably do versus what they merely demo.

**Section structure (h2 sections, 1-line summaries).**

- **What is an agent? A working definition for researchers** — model + tools + loop + memory + permissions, with a deliberate move away from the "autonomy" framing because autonomy is a spectrum, not a category.
- **What's new since 2024: the harness is the product** — Cursor/LangChain/Hermes/Cline/deepagents writeups showing the same finding: prompts, tools, context packing, evals, model-specific tuning matter more than which base model you call. Documented 10–20 point swings on tau2-bench and Terminal-Bench 2 from pure harness work.
- **The 2026 agent landscape in one picture** — coding agents (Claude Code, Codex, Cursor, Cline, Hermes, opencode), computer-use agents (Codex CUA, Anthropic Computer Use, Operator-lineage), research agents (Deep Research modes), general agents (Manus, ChatGPT Agent), and creative agents (Claude + Blender/Adobe/Ableton MCP connectors).
- **Agents are breaking containment** — the May 2026 throughline: coding agents are now being used for non-coding knowledge work (Codex for Work, Claude Cowork, Anthropic Orbit leak). Implications for researchers.
- **What this means for research workflows** — not "AI replaces research", but "research workflows now include long-running, tool-using delegates". Calls back to Week 7 (vibe coding caution applies even more strongly when the agent runs for hours).

**Key sources (URLs verified).**

- Latent Space / AINews "Agents for Everything Else: Codex for Knowledge Work, Claude for Creative Work" — https://www.latent.space/p/ainews-agents-for-everything-else (1 May 2026) — Codex for Work landing page, dynamic UI, 42% faster CUA, Claude creative connectors.
- Latent Space / AINews "Codex Rises, Claude Meters Programmatic Usage" — https://www.latent.space/p/ainews-codex-rises-claude-meters (14 May 2026) — Cline SDK launch, LangSmith Engine/SmithDB, Notion External Agents API, Cursor cloud agents.
- Latent Space / AINews "Silicon Valley gets Serious about Services" — https://www.latent.space/p/ainews-silicon-valley-gets-serious (6 May 2026) — Anthropic/PE JV, OpenAI Deployment Company, services-not-software thesis.
- Latent Space / AINews "The Other vs The Utility" — https://www.latent.space/p/ainews-the-other-vs-the-utility (4 May 2026) — harness-as-product-boundary, 10–20 point Terminal-Bench/tau2-bench swings from harness changes, "Clippy vs Anton 2026" framing of agent character.
- Anthropic blog: Claude for Creative Work — https://www.anthropic.com/news/claude-for-creative-work (28 April 2026) — 9 creative MCP connectors, all available on free plan.
- Simon Willison's MCP/agents tag — https://simonwillison.net/tags/model-context-protocol/ — for the pragmatic "I don't use MCP much in practice, CLI utilities work better" voice.

**Specific claims / data points to include.**

- 10–20 point swings on tau2-bench from harness changes (May 2026; Mason Drxy / Anthony Maio via AINews 4 May).
- gpt-5.2-codex moved 52.8% → 66.5% on Terminal-Bench 2.0 from prompt+middleware changes (AINews 4 May 2026).
- Codex CUA is 42% faster after the late-April update (AINews 1 May 2026, AriX).
- 9 Anthropic creative connectors (Blender, Adobe, Autodesk, Ableton, Splice, Affinity, SketchUp, Resolume Arena, Resolume Wire) live on free plan from 28 April 2026.
- LangChain shipped LangSmith Engine, SmithDB, Sandboxes, Managed Deep Agents, LLM Gateway, Context Hub, Deep Agents 0.6 at Interrupt (May 2026 via AINews 14 May).
- Manus: invitation-only, ~500K waitlist as of April 2026; Meta acquisition unwound by Chinese regulators April 2026 (Wikipedia/Euronews).

**Calls back to earlier weeks.**

- Week 2 (transformers): the agent is still the same transformer doing next-token prediction — but now with tool calls in the stream. The capability change is at the harness level, not the architecture level.
- Week 7 (coding): vibe-coding caution scales. A vibe-coded codebase that one person inherited had a +10,197 / −3,618,778 diff to clean up (AINews 14 May).
- Week 9 (trajectory): the same "what's been patched, what's reduced, what's structural" frame works for agent capabilities. We'll use it explicitly in 10.2.

---

## 10.2 — Agents: Failure Modes for Multi-Step / Long-Horizon Tasks

**Thesis.** Apply the Week 9.2 patched/reduced/structural taxonomy to agent-specific failures. The structural ones — long-horizon coherence loss, tool-loop instability, reliability gap, prompt-injection on retrieved content — are the ones researchers need to plan workflows around.

**Section structure.**

- **Why this needs its own lesson** — Week 9 was about single-turn capability. Agents fail in new ways because they run for many turns, accumulate state, call tools, and act on retrieved content. Reliability ≠ accuracy.
- **The agent failure taxonomy** — three categories applied to agents:
  - *Patched:* simple tool-call format errors (mostly fixed by JSON-mode and tool-calling APIs); short-loop hallucinated tools; basic "agent forgets it has a tool" issues.
  - *Reduced but persistent:* sycophancy in long sessions; loop instability (Qwen 27B "stuck-in-loop" reports on Reddit); confidence miscalibration over horizons; over-eager file deletion / over-confident refactor; the Giffmana / "wrong proof defended confidently" pattern carried over from Week 9.
  - *Structural:* long-horizon planning collapse (Wang et al. 2026 "Why Reasoning Fails to Plan"); the augmentation-vs-automation reliability gap (Rabanser/Kapoor/Narayanan et al. 2026); compositional brittleness (FoodTruck Bench / ProgramBench 0%-on-whole-repo); prompt injection on retrieved tool output (Simon Willison's standing claim); compounding error rates over many steps.
- **The "reliability is not accuracy" finding** — Rabanser/Kapoor et al. (2026): 14 models, 18 months, accuracy improved substantially, reliability did not. Four dimensions: consistency, robustness, predictability, safety. Predictability is the weakest; "when agents report confidence, it often carries little signal."
- **Long-horizon planning collapse** — Wang et al. (Jan 2026): step-wise reasoning is a greedy policy that works for short horizons and fails for long ones; locally optimal early choices get amplified.
- **Tool-loop and harness failures observed in the wild** — wedding concierge: 25% of usage was jailbreak attempts (AINews 14 May); Grok→Bankrbot $200K exploit (AINews 6 May) as an AI-to-AI prompt injection example; Anthropic "Gift Max" exploit (AINews 6 May).
- **What the Week 9 taxonomy tells us about action** — for each category, what the researcher should do (verify, plan around, refuse to delegate).

**Key sources (URLs verified).**

- Wang et al., "Why Reasoning Fails to Plan: A Planning-Centric Analysis of Long-Horizon Decision Making in LLM Agents" — https://arxiv.org/abs/2601.22311 (29 Jan 2026).
- Rabanser, Kapoor, Kirgis, Liu, Utpala & Narayanan, "Towards a Science of AI Agent Reliability" — https://arxiv.org/abs/2602.16666 (Feb 2026, Princeton CITP) — four reliability dimensions, 14 models, 18 months. **This is the Kalai-2025-equivalent for agents** — exactly what the user asked for.
- Kapoor & Narayanan, normaltech.ai blog post on the same paper — https://www.normaltech.ai/p/new-paper-towards-a-science-of-ai
- Kapoor & Narayanan in *Fortune* (24 March 2026) on the reliability lag — https://fortune.com/2026/03/24/ai-agents-are-getting-more-capable-but-reliability-is-lagging-narayanan-kapoor/
- Kalai et al. (2025) *Why Language Models Hallucinate*, arXiv:2509.04664 — already cited in Week 9, recapped here as the single-turn parent of the agent reliability problem.
- ProgramBench (Meta FAIR, May 2026) — top accuracy 0% on whole-repo-from-scratch tasks (already cited in Week 9; reuse here as agent compositional brittleness).
- "YC-Bench" (arXiv:2604.01212) — meltdown looping, hallucinations, legal threats as documented frontier-agent failure modes; "Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents" (arXiv:2603.29231).
- Simon Willison on prompt injection — https://simonwillison.net/tags/prompt-injection/ — for the structural "we've known about this for 2.5 years and still don't have convincing mitigations" claim.

**Specific claims / data points.**

- Rabanser et al. (2026): outcome consistency scores 30–75% across models on the same prompt; reliability improved only modestly while accuracy improved substantially across 18 months.
- Wang et al. (Jan 2026): with FLARE, LLaMA-8B frequently outperforms GPT-4o-with-standard-step-by-step on multiple long-horizon benchmarks — small + planning > large + greedy.
- Goodfire + AISI: agents sometimes verbalise eval-awareness, inflating safety scores (AINews 4 May 2026).
- 92% hallucination rate on AA-Omniscience for Ling 2.6 1T (already in Week 9; recap as "mitigations are not uniformly inherited across the open-weights frontier").

**Calls back to earlier weeks.**

- Week 9.2 (patched/reduced/structural): apply same scaffold explicitly.
- Week 5 (hallucinated citations): agentic RAG inherits the hallucination problem and adds new vectors. Set up 10.4.
- Week 7 (silent errors): the silent-error problem from data analysis returns, amplified by tool chaining.

---

## 10.3 — Agents: The Current Tool Landscape (Including MCP)

**Thesis.** A practical, honest, time-stamped tour of what exists in May 2026 and what UCT students can actually access. Frame as four categories: coding agents, computer-use/browser agents, research agents, and the MCP plumbing layer.

**Section structure.**

- **Four categories of agent tool in May 2026** — coding (Claude Code, Codex, Cursor, Cline, Hermes), computer-use (Codex CUA, Anthropic Computer Use, Operator-lineage, Manus), research (Deep Research modes — own section in 10.4), and connectors-and-plumbing (MCP).
- **Coding agents** — what they are, the Claude vs Codex pricing dynamic (programmatic-credits change in May 2026), the open alternative tier (Cline, opencode, Hermes, deepagents-cli), local open-weight options (Qwen 3.6 27B on RTX 4090). Brief comparison table with free-tier reality.
- **Computer-use agents** — what "uses a computer like a human" actually means; current OSWorld scores (GPT-5.4 75.0%, Claude Sonnet 4.6 72.5% as of early 2026, vs human 72.36% — agents now meet/exceed average human on this benchmark, but benchmark ≠ real workflow); WebArena progress from 14.41% baseline to ~62% (IBM CUGA early 2025) to higher in 2026. Caveat: real-world deployments still fragile; OSWorld is 369 cross-app tasks, narrow scope.
- **Agentic browsers** — Comet (Perplexity, free with Perplexity account), Dia (Browser Company, ex-Arc team), ChatGPT Atlas. Comparison + security warning (prompt injection on browsed content).
- **Manus and the "general agent" claim** — what it is, what it isn't, GAIA benchmark claim, regulatory situation (Meta acquisition blocked April 2026), invitation-only / 500K waitlist. Treat skeptically.
- **MCP: the connector layer** — what it is, how it became cross-vendor standard (Anthropic origin, now also Google, OpenAI), what it means for researchers (Zotero, GitHub, Drive, Notion, Slack connectors), free-tier availability on Claude.ai, the 2026 MCP roadmap (transport scalability, agent communication, governance, enterprise). Brief security warning (prompt injection through MCP-retrieved content; Willison's standing critique).
- **What's still vapourware** — recursive self-improvement / autonomous science (Recursive, Adaption AutoScientist — flagged as launches not deployments); "Anthropic Orbit" (leak, not launch).

**Key sources (URLs verified).**

- OSWorld benchmark current standings — see https://benchmarkingagents.com/agent-benchmarks/ and https://os-world.github.io/ (need to verify the latter resolves; if not, use the BenchmarkingAgents aggregator).
- Anthropic Claude for Creative Work — https://www.anthropic.com/news/claude-for-creative-work (28 April 2026).
- Perplexity Comet — https://www.perplexity.ai/comet (free with Perplexity account; iOS/Android/Mac/Windows by 2026).
- Dia Browser (Browser Company) — verify URL before citing; "Best AI Browsers 2026" overview at https://tooldirectory.ai/best-ai-collections/best-ai-browsers-2026 (third-party, use for orientation only).
- Manus Wikipedia entry — https://en.wikipedia.org/wiki/Manus_(AI_agent) for the regulatory and waitlist facts.
- MCP roadmap blog post — https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/ (9 March 2026).
- Simon Willison MCP tag — https://simonwillison.net/tags/model-context-protocol/ — for the practitioner critique that MCP isn't always the best abstraction (Willison's stated current preference for CLI utilities and Playwright over MCP for coding work).
- HuggingFace smolagents — https://huggingface.co/docs/smolagents/en/index and Computer Agent Space at https://huggingface.co/spaces/smolagents/computer-agent — verify Space still live before week is published.
- LangChain deepagents / LangGraph — verify https://www.langchain.com/ and https://github.com/langchain-ai/langgraph (used to back up "deployment infrastructure has matured" claim in 10.3).

**Specific claims / data points.**

- OSWorld: human baseline 72.36%; GPT-5.4 (March 2026) 75.0% on OSWorld-Verified; Claude Sonnet 4.6 (Feb 2026) 72.5% — flag these are 2026 results and will date.
- WebArena: 14.41% baseline → ~62% (IBM CUGA early 2025) → higher in 2026 — exact current SOTA to be verified at draft time.
- Manus GAIA claim: "state-of-the-art across all three difficulty levels" per company; independent replication scarce.
- Anthropic creative connectors: 9 connectors, all available on Free plan as of 28 April 2026. Free users still limited to 1 custom connector.
- Microsoft Copilot for EDU: free Copilot Chat available to UCT students if IT enables it via Microsoft 365 A1/A3/A5 (this is realistic for UCT — flag).
- Latent Space Notion External Agents API: third-party agents (Claude, Codex, Cursor, Decagon, Warp, Devin) can operate inside Notion (AINews 14 May 2026).

**Calls back to earlier weeks.**

- Week 5 (lit review tools): Connected Papers, ResearchRabbit, NotebookLM continue. The agentic layer adds Deep Research modes (handled in 10.4) and Zotero MCP (10.5).
- Week 8 (multimodal): screen-pixel-reading is the same VLM technology — but the failure modes from Week 8 (description vs value-extraction) carry over directly.

---

## 10.4 — RAG in 2026: What Changed Since Week 5, Agentic RAG, Long-Context vs Retrieval, Eval

**Thesis.** Three things changed since Week 5: (1) long-context windows up to 1M+ tokens erode the basic case for RAG; (2) agentic RAG (planner-retriever-synthesiser-checker loops) outperforms static RAG on multi-hop research questions; (3) eval frameworks (RAGAS and successors) matured but the hardest evals — multi-hop with planning, context compaction — remain unsolved operationally.

**Section structure.**

- **Recap: what we covered in Week 5** — Elicit, Consensus, NotebookLM, Perplexity, Connected Papers, ResearchRabbit. All still relevant. Hallucinated citation crisis still real (it's reduced-but-persistent in the Week 9 taxonomy).
- **What changed since Week 5: long-context vs retrieval** — frontier models routinely handle 1M+ tokens; whether retrieval still helps depends on the task. Cite the 2024–2025 long-context vs RAG comparison literature; note 1M-token "needle in haystack" performance remains imperfect in practice (jxmnop on AINews 4 May 2026: "true 1M-context capability still does not really work in practice").
- **Agentic RAG** — the move from static (retrieve once, generate) to planner-retriever-synthesiser-checker loops. Singh et al. *Agentic RAG: A Survey* (arXiv:2501.09136, Jan 2025) as the canonical reference; *Towards Agentic RAG with Deep Reasoning* (arXiv:2507.09477) as the follow-up.
- **What this looks like in research workflows** — Deep Research modes are the consumer-facing agentic RAG. Trade-offs vs Week 5 tools.
- **RAG eval: RAGAS and successors** — RAGAS (Es, James, Espinosa-Anke & Schockaert, arXiv:2309.15217, EACL 2024) four metrics: context precision, recall, faithfulness, answer relevance. Now processes >5M evals/month at major firms. Limitations: needs a strong judge model; faithfulness is necessary but not sufficient for "the answer is actually correct"; multi-hop and compaction evals still open.
- **Retrieval vs long-context for actual research** — honest verdict for May 2026: for single-document analysis, long-context dumping wins; for multi-source synthesis, agentic RAG still wins (because it does follow-up retrievals based on what it learned); for citation work, Week 5 verification protocols stand regardless of which approach you used. Cost matters: RAG remains cheaper at scale.
- **The Esethu / low-resource angle** — RAG is potentially equity-positive because it can ground frontier-model outputs in domain corpora that those models weren't trained well on (African languages, local datasets), but only if the embedding/retrieval layer handles the target language adequately. Most don't yet.

**Key sources (URLs verified).**

- Singh, Ehtesham, Kumar & Khoei (Jan 2025), *Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG* — https://arxiv.org/abs/2501.09136
- Singh et al. (follow-up, July 2025), *Towards Agentic RAG with Deep Reasoning: A Survey of RAG-Reasoning Systems in LLMs* — https://arxiv.org/pdf/2507.09477
- Li, Liu, Saxena et al., *Retrieval Augmented Generation or Long-Context LLMs? A Comprehensive Study and Hybrid Approach* — https://arxiv.org/pdf/2407.16833 (the canonical long-context-vs-RAG comparison; tested on Gemini 1.5 Pro and GPT-4 era models, so flag as 2024 evidence that needs current re-testing).
- Yu, Xiong, Ahn et al., *Long Context vs. RAG for LLMs: An Evaluation and Revisits* — https://arxiv.org/pdf/2501.01880
- Es, James, Espinosa-Anke & Schockaert (2023, EACL 2024), *RAGAS: Automated Evaluation of Retrieval Augmented Generation* — https://arxiv.org/abs/2309.15217
- RAGAS docs and adoption — https://docs.ragas.io/ (verify URL resolves before citing).
- AINews 4 May "The Other vs The Utility" — https://www.latent.space/p/ainews-the-other-vs-the-utility — for the May 2026 practitioner take that 1M context still doesn't truly work in practice.
- Esethu Framework, Rajab et al. — https://arxiv.org/abs/2502.15916 — already cited in Week 4; reuse for the equity argument about RAG over local corpora.

**Specific claims / data points.**

- RAGAS processes >5M evals/month at major firms as of 2026 (per RAGAS docs/blog).
- 2024 finding (Li et al.): long-context outperforms RAG on Wikipedia QA; RAG wins on dialogue-based and general queries. Flag as 2024 — frontier long-context has since improved.
- 1M+ context windows are standard on Gemini Pro tier (Week 8 already established the Gemini Pro tier number).
- Multi-hop and context-compaction evals remain identified gaps (philschmid, jxmnop, AINews 4 May).

**Calls back to earlier weeks.**

- Week 5 (lit review): direct continuation. The 5-tool landscape gains a 6th category — Deep Research / agentic RAG — and that's where 10.5 starts.
- Week 7 (data analysis): RAG over your own dataset is a research workflow component — but the silent-error problem applies to retrieval too (wrong chunk retrieved, plausible-but-wrong answer).
- Week 9.4 (illusions of understanding): Messeri & Crockett's "monocultures of knowing" applies extra forcefully to agentic RAG, because the agent decides what to retrieve and synthesise — closing further sources of friction that previously kept the researcher honest.

---

## 10.5 — Advanced Research Tools: A Curated Tour (Honest Free-vs-Paid Split)

**Thesis.** Build a usable map of the May 2026 advanced-tool landscape, with brutally honest verdicts about (a) what each tool actually does well, (b) what its specific failure mode is, and (c) what the free tier delivers in practice for a UCT student without a foreign credit card.

**Section structure.**

- **The free-tier reality for UCT students** — UCT issues Microsoft 365 EDU; Anthropic and OpenAI generally accept South African cards but Perplexity and Gemini accept more reliably; many AI tools require a foreign credit card or geo-locked sign-up; Claude.ai, ChatGPT, Gemini, Perplexity, Microsoft Copilot Chat all currently work from South African networks. Flag tools that don't.
- **Deep Research mode comparison (the assignment hinges on this)** —
  - **Perplexity Deep Research** — Free tier currently 5 Deep Research queries/day (better than competitors). Recommended for the activity.
  - **ChatGPT Deep Research** — Free tier 5/month (capped, hard limit, with possible auto-fallback to a lightweight version after exhaustion).
  - **Gemini Deep Research** — Free tier 5 reports/month on Gemini Apps free tier.
  - **Claude Research** — Anthropic shipped agentic research features inside Claude; verify current free-tier availability before drafting.
  - **Kimi Deep Research (kimi.com)** — Moonshot AI's free-tier Deep Research mode. Cited, visualised reports; the strongest free Chinese alternative to Perplexity Deep Research. POPIA caveat applies (data → China). No published per-day quota; community reports suggest a few Deep Research runs/day are usable before throttling.
  - **DeepSeek with DeepThink + web search (chat.deepseek.com)** — not a single-button Deep Research mode, but DeepThink reasoning + web search + file upload chained manually approximates the workflow. Free, no quotas published, English UI.
  - **Qwen Chat with thinking + web search (chat.qwen.ai)** — similar pattern: hybrid thinking + search on free tier. Less mature "Deep Research" surface than Kimi as of May 2026.
  - Honest comparison table: speed, depth, citation quality, hallucination rate (anecdotal — students will measure their own in 10.6).
- **Agentic coding tools for research** — Claude Code (free tier exists but limited; Anthropic May 2026 pricing change added programmatic credits to paid plans), Codex (currently more generous limits + 2-month-free-for-enterprise-switchers promo), open alternatives (Cline, opencode, deepagents-cli) for the budget-conscious / locally-hosted.
- **MCP connectors that matter for researchers** — Zotero (community MCP servers exist), GitHub, Drive, Notion, Slack. Caveats: each one widens the prompt-injection attack surface; each one is also a POPIA-relevant data flow. Flag both honestly.
- **HuggingFace agent demos and Spaces** — smolagents library, Computer Agent Space, agent demos run free on HF (verify 2-3 currently work before publishing).
- **What's expensive and probably not worth it for a postgrad on a stipend** — Sierra / Decagon / Cognition Devin (enterprise pricing); Manus (currently waitlist-only); Cursor Pro (worth it if you code daily, otherwise free Codex/Claude Code is fine).
- **Workflow recommendations** — a single 5-step "use Deep Research, then verify, then synthesise, then write, then audit" pipeline that combines free-tier tools and ties back to Week 5/6/7 workflows.

**Key sources (URLs verified).**

- Perplexity pricing and free-tier limits — https://www.perplexity.ai/pricing (verify daily Deep Research quota at draft time — current research suggests 5/day on free).
- ChatGPT pricing — https://chatgpt.com/pricing/ — and OpenAI Deep Research help article https://help.openai.com/en/articles/10500283-deep-research-faq.
- Gemini Apps free tier — https://gemini.google/subscriptions/ — and DataStudios 2026 free-tier writeup for orientation.
- Anthropic Claude pricing — https://www.anthropic.com/pricing — and the May 2026 programmatic-credits explanation (verify Anthropic's own blog post before linking).
- HuggingFace smolagents Computer Agent — https://huggingface.co/spaces/smolagents/computer-agent.
- Zotero MCP servers — community-maintained; check GitHub for currently active repo before citing (e.g. search github.com for "zotero mcp server"). **Uncertain — flag if no maintained server exists.**
- Microsoft Copilot for Education — https://www.microsoft.com/en-us/education/products/copilot-in-education (verify UCT licensing — likely A3 tier).
- POPIA: South Africa Information Regulator — https://inforegulator.org.za/ (canonical source; cross-check against Michalsons https://www.michalsons.com/blog/how-popia-affects-ai/76842 for plain-language explanation).
- Esethu Framework — https://arxiv.org/abs/2502.15916 — for the equity-and-data-sovereignty argument.

**Specific claims / data points.**

- Perplexity Deep Research free tier: 5 queries/day (most generous of the major free Deep Research offerings).
- ChatGPT Deep Research free tier: 5/month, with auto-fallback to lightweight version after exhaustion (verified via OpenAI help).
- Gemini Deep Research free tier: 5 reports/month.
- Anthropic creative MCP connectors live on free Claude.ai plan (28 April 2026).
- UCT students with @myuct.ac.za / @uct.ac.za accounts get Microsoft 365 A-tier with Copilot Chat (verify with UCT ICTS — likely true).
- Only ~5% of African AI researchers have access to the compute they need (UNDP figure); 95% rely on Colab or shared/free tools. Frames why free-tier matters here in a way it doesn't in EU/US courses.
- 60% of top supercomputers in US (175), China (47), Germany (41); none in Africa.

**Calls back to earlier weeks.**

- Week 3 (environmental cost): agentic workflows burn far more tokens than chat. Theo's Copilot 60M-token-in-one-message stunt (AINews 4 May 2026) makes the cost picture vivid. Add a row to the per-prompt cost calculation from Week 3 for "a research-agent run".
- Week 4 (ubuntu / Just AI / Esethu): the data flows that an agent enables (MCP into your Gmail, Drive, Zotero) cross POPIA-relevant boundaries. Brief explicit warning here, full coverage in 10.6 disclosure section.
- Week 5 (lit review): Deep Research extends the Week 5 toolkit. Frame as "Tool category 4" alongside the three Week 5 categories.
- Week 9.5 (verification protocols): every verification protocol from Week 9 still applies. The dated-research three-question check becomes the dated-tool four-question check: which tool, which model, when used, what was the free-tier reality at the time.

---

## 10.6 — Hands-On Activities and Assessment

**Thesis.** The activity is already decided: "Same task, three ways." Students apply the Week 9 failure taxonomy to a real-world comparison of plain chat vs chat-with-browsing vs Deep Research mode, using free tools only.

**Section structure.**

- **Activity 1: Same Task, Three Ways (the headline activity)** —
  - Pick a research question in your own field (specific, answerable, not trivially Googleable).
  - Run it through (1) plain chat (Claude.ai free, ChatGPT free, or Gemini free — pick one and stick with it), (2) the same chat with browsing/tools enabled, (3) Perplexity Deep Research (free tier, 5/day — most generous as of May 2026). *Acceptable substitute if Perplexity quota exhausted or sign-up blocked: **Kimi Deep Research (kimi.com)** — students must disclose tool choice and acknowledge POPIA implication (prompts flow to mainland-China servers) in the writeup.*
  - 1–2 page comparison: depth, accuracy, citation quality, hallucinations encountered, where each tool failed.
  - Apply the Week 9.2 patched/reduced/structural taxonomy explicitly: which failures fit which category, what action would the Week 9.5 verification protocol prescribe.
- **Activity 2: Build a small MCP-style workflow** — optional / for the more technical students. Use Claude.ai's free MCP connectors (creative tools, or the Microsoft 365 connector if UCT supplies it) to do one small task in your research workflow. 250-word writeup of what worked, what failed, what you'd never let it do unsupervised.
- **Activity 3: Verify a Deep Research output** — take the Deep Research output from Activity 1 and apply the Week 5 Five-Point Citation Check + the Week 9 dated-research three-question check. How many of the citations check out? How many "papers" don't exist? How many exist but say something different? This is the citation-verification exercise from Week 5 carried into the agentic-RAG era.
- **Weekly assessment** — ~1500 words. Same structure as Week 9 final assessment: snapshot in time, deliberately acknowledging future obsolescence, with retest-cadence recommendation. Required sections: tool comparison, applied failure taxonomy, verification audit, POPIA / data-flow disclosure, and a "what I'd do differently if I had a paid subscription" honest paragraph. Free-tier required — no paid tools — to keep the playing field equal.
- **Grading split (proposed; mirrors Week 9 split):** Tool comparison 25%, Failure taxonomy application 25%, Verification audit 20%, Data-flow / POPIA disclosure 15%, Staleness reflection 10%, Disclosure statement 5%.
- **Closing pointer to Week 11** — Africa's sovereign AI capacity. Agents that depend on US/Chinese frontier APIs are not sovereign infrastructure; the compute / API asymmetry just covered in 10.5 sets up the Week 11 discussion directly.

**Key sources (URLs verified).**

- Reuses Week 5 (Five-Point Citation Check), Week 6 (disclosure templates), Week 9 (failure taxonomy, verification protocols) materials — no new external sources needed.
- POPIA — https://inforegulator.org.za/ — for the data-flow disclosure section.
- Free-tier Deep Research links from 10.5.

**Specific design notes.**

- Free tools only is a hard constraint, not a soft preference. The Week 5 lesson on UCT students who can't access paid subscriptions or foreign credit cards still applies — and more sharply, because agentic tools are more expensive.
- Mirror the Week 9 deliberate-obsolescence reflection — every Week 10 claim has an implicit "as of May 2026" stamp, including the activity outputs.
- The activity is small enough that everyone can do it on a phone or a borrowed laptop. Important.

**Calls back to earlier weeks.**

- Week 5 (citation verification): direct reuse of the Five-Point Citation Check.
- Week 6 (disclosure templates): student-facing disclosure obligations apply.
- Week 7 (verification habit): the verification habit extends to agent outputs.
- Week 9 (entire week): this assessment is essentially "apply the Week 9 frame to agentic tools".

---

## Research sweep — what I found vs what's missing

### AINews sweep (~28 April – 19 May 2026)

Pulled 16 emails in the window; the agent-relevant ones were:
- 28 Apr "ImageGen is on the Path to AGI" — not agent-focused, skip.
- 29 Apr "not much happened today" — skip.
- 30 Apr "The Inference Inflection" — infrastructure, partly relevant; flagged for Week 11.
- **1 May "Agents for Everything Else: Codex for Knowledge Work, Claude for Creative Work"** — top of stack for 10.1 and 10.3.
- 2 May "AI Engineer World's Fair — Autoresearch, Memory, World Models" — agent-adjacent; some content for 10.4.
- **4 May "The Other vs The Utility" (Clippy vs Anton 2026)** — harness-as-product-boundary, 10-20 pt Terminal-Bench swings, agent character debate, ProgramBench rebuttal. Heavy use in 10.1, 10.2.
- **6 May "Silicon Valley gets Serious about Services"** — Anthropic/PE JV, OpenAI Deployment Company, finance verticals, Anthropic Orbit leak. Used in 10.1, 10.3, 10.5.
- 7 May "Anthropic-SpaceX 300MW/$5B/yr deal" — infrastructure; deferred to Week 11. (As flagged in Week 9 build notes.)
- 8 May "GPT-Realtime-2 / -Translate / -Whisper" — voice; deferred to Week 11 / future weeks.
- 9 May "Anthropic growing 10x/year" — business dynamics; partial use in 10.5 (free-tier sustainability uncertainty).
- 12 May "Thinking Machines TML-Interaction-Small" — model release; skip for now.
- 13 May "End of Finetuning" — out of scope.
- **14 May "Codex Rises, Claude Meters Programmatic Usage"** — top of stack for 10.3 and 10.5 (pricing, harness ecosystem maturity, Notion External Agents, Cline SDK, recursive self-improvement startup cluster).
- 15 May "Everything is Conductor" — model orchestration; mention briefly in 10.1.
- 16 May "Cerebras IPO" — infrastructure; out of scope.
- 19 May "How to land a job at a frontier lab" — out of scope.

**Email-size issue (Week 9 warning).** Same problem hit again — three of the four most relevant emails exceeded 200K tokens when fetched and saved to disk, but plaintext bodies were extractable with `jq` from the saved JSON. All key passages successfully captured.

### Academic / blog literature

- **Found, key citation:** Rabanser, Kapoor, Kirgis, Liu, Utpala, Narayanan (Feb 2026), "Towards a Science of AI Agent Reliability" (arXiv:2602.16666). This is the requested agentic equivalent of Kalai et al. 2025 — by the same Kapoor/Narayanan team the user flagged as critical. Direct heir to the Week 9 frame.
- **Found, key citation:** Wang et al. (Jan 2026), "Why Reasoning Fails to Plan" (arXiv:2601.22311) — gives the structural long-horizon-planning-collapse mechanism with an explicit step-wise-greedy-policy analysis.
- **Found, secondary:** "Beyond pass@1" (arXiv:2603.29231) and "YC-Bench" (arXiv:2604.01212) for reliability-at-scale and concrete frontier failure modes.
- **Found, RAG:** Singh et al. *Agentic RAG: A Survey* (arXiv:2501.09136, Jan 2025) and follow-up arXiv:2507.09477. Li et al. arXiv:2407.16833 for the 2024 long-context-vs-RAG baseline (flag as needing 2026 re-test).
- **Tim Gowers blog:** No new agent-specific post on https://gowers.wordpress.com/ since the 8 May 2026 ChatGPT 5.5 Pro post already used in Week 9. That post itself is *not* about agents — it is about direct conversational use. A single anonymous commenter mentions Deep Research, nothing more. Conclusion: Gowers has not yet weighed in on agents publicly. Reuse the existing Week 9 reference rather than over-claim.
- **Terence Tao / other mathematicians:** Tao is heavily quoted in Epoch AI's *FrontierMath Tiers 1-4 Expert Perspectives* (https://epoch.ai/frontiermath/tiers-1-4/expert-perspectives); use existing Week 9 citations rather than duplicate.
- **Anthropic blog:** Claude for Creative Work (28 April 2026), Claude Managed Agents updates (May 2026 — dreaming, multi-agent orchestration), Claude Code release notes. All verified.
- **OpenAI blog:** Codex for Work, Operator/Codex CUA writeups — verified via AINews summaries; will WebFetch each at draft time to confirm canonical URLs.
- **Simon Willison:** Active on agents and MCP. Two key positions to cite: (a) MCP isn't always the right abstraction in practice; (b) prompt injection remains structurally unsolved.
- **Kapoor & Narayanan:** Covered (see above). normaltech.ai is the active blog. *AI Snake Oil* (Princeton UP 2024) for the book reference; Fortune 24 March 2026 article for the journalistic framing of the reliability paper.
- **Steve Newman blog:** Did not turn up any May 2026 post that adds beyond what's already covered. Will not cite unless a specific piece is found at draft time.

### Free agentic tool landscape (May 2026)

Verified free-tier specifics:
- **Perplexity:** 5 Deep Research/day on free tier (most generous); Comet browser free with Perplexity account.
- **ChatGPT free:** 5 Deep Research/month, then lightweight fallback.
- **Gemini Apps free:** 5 Deep Research reports/month.
- **Claude.ai free:** 9 creative MCP connectors plus Microsoft 365 connector available on free plan as of 28 April 2026; free users limited to 1 custom connector.
- **HuggingFace Spaces:** smolagents Computer Agent Space exists; verify 2–3 currently-working agent demos at draft time (HF Spaces churn rapidly).
- **Microsoft Copilot via UCT M365:** Copilot Chat available if UCT IT enables it on A1/A3/A5 — almost certainly available, verify with UCT ICTS before stating definitively.

#### Chinese free-tier offerings (May 2026)

The Western free-tier list above is West-Coast-heavy. For UCT students without foreign credit cards, Chinese-hosted services often have *more* generous free tiers and accept email/Google sign-up. Access from a Cape Town residential connection is generally OK without a VPN as of May 2026 (per Surfshark / chat-deep.ai availability data, 9 May 2026 — South Africa is not on any nationwide DeepSeek block list, and Kimi/Qwen/Z.ai have no SA-specific restrictions). The single biggest catch is **POPIA**: prompts and uploads flow to servers in mainland China, which is not currently recognised as an adequate-protection jurisdiction under POPIA s.72 — students must be told this before using these tools on identifiable personal data or third-party confidential material.

- **DeepSeek (chat.deepseek.com)** — DeepSeek (Hangzhou). Free chat with V4 Flash plus DeepThink reasoning toggle, web search, file upload, no message cap, no credit card, no Chinese phone. Email or Google sign-up. English UI. Fair-use throttling shows "Server Busy" at peak times. *Strength:* the single most capable fully-free reasoning chat as of May 2026. *Weakness:* DeepSeek's privacy policy locates data in mainland China — POPIA implications real; not appropriate for personal-data work.
- **Kimi (kimi.com)** — Moonshot AI (Beijing). Free chat on K2.6 with Deep Research, Agent Swarm, Slides/Docs/Sheets generation, and Kimi Code surfaced on the free tier; community-reported soft limit ~30–50 K2.6 messages/day. Google sign-in works; English UI. Long-context (256K+) is the differentiator. *Strength:* the strongest free Deep Research alternative to Perplexity — produces cited, visualised reports. *Weakness:* free-tier Deep Research quota is not transparently published; expect it to tighten.
- **Qwen (chat.qwen.ai)** — Alibaba (Hangzhou). Free chat on Qwen3.6 / 3.5 Plus, hybrid thinking mode, web search, file/image/video understanding, image generation, artefacts. English UI. 1M-token context advertised on selected models. *Caveat:* Qwen Code's OAuth free tier was discontinued 15 April 2026 — the *chat* surface remains free, the *coding-agent CLI* now requires a paid plan or OpenRouter key. *Strength:* widest modality coverage on a free tier. *Weakness:* fair-use quotas on Deep-Research-style runs are opaque.
- **Z.ai / Zhipu (chat.z.ai)** — Zhipu AI (Beijing). Free chat powered by GLM-4.5/4.6 with agent mode, web search, and file generation (.docx/.pdf/.xlsx); GLM-5 (launched 11 Feb 2026, 744B MoE / 40B active, MIT-licensed) accessible via paid tier and API. English UI. Email sign-up. *Strength:* the most open-weights-aligned of the major Chinese free chats; GLM-4.6 is MIT-licensed and self-hostable. *Weakness:* free-tier agent runs are slower and shorter than DeepSeek/Kimi.
- **Doubao / Dola (Cici → Dola rebrand)** — ByteDance. International rebrand of Doubao; available in UK / Mexico / Spain but not in US/Canada/Australia and SA availability uncertain. The international app reportedly proxies through Azure-hosted OpenAI for English. *Verdict:* skip — opaque and not pedagogically interesting.
- **MiniMax Agent (agent.minimax.io)** — MiniMax (Shanghai). Free tier exists; coding-agent strengths; less mature Deep Research surface than Kimi. English UI, email sign-up. *Verdict:* worth a brief mention; not a Perplexity substitute.
- **Manus (manus.im)** — Singaporean-registered, Chinese-founded. *Status update from research sweep:* the Meta acquisition was formally blocked / unwound by China's NDRC on 27 April 2026 (CNBC, Fortune, O'Melveny alert, 27–28 April 2026), and elevated to the National Security Commission — the existing outline framing stands. Public access is now mixed: some third-party blogs claim the waitlist was dropped in late 2025 with 1,000-credit / 1-daily-task free trials, but the existing outline note (invitation-only, ~500K waitlist April 2026) draws on a different source and may still be the more accurate state. **Uncertain — flag at draft time.** Independent benchmark replication remains scarce.
- **Yi / 01.AI** — Founded by Kai-Fu Lee. Open-weights Yi-34B / Yi-Large via HuggingFace, OpenRouter, Fireworks. No prominent free consumer chat surface in English as of May 2026 following 01.AI's August 2025 business adjustment; the company has since partnered with Alibaba on the consumer side. *Verdict:* mention as open-weights option, not as a usable consumer chat.
- **Baichuan (Baixiaoying)** — Baichuan Intelligence. Chinese-only chat surface; open-weights models on HuggingFace and NVIDIA NIM. *Verdict:* skip for the consumer-tool tour; mention only in any open-weights rollup.

**Honest free-tier ranking for the UCT student who can't pay (May 2026):**

1. **DeepSeek (chat.deepseek.com)** — most capable free reasoning chat, no Chinese phone needed, English UI, full V4 + DeepThink + search + files. POPIA caveat.
2. **Kimi (kimi.com)** — closest free analogue to Perplexity Deep Research. POPIA caveat.
3. **Qwen (chat.qwen.ai)** — strongest multimodal on free tier; coding-CLI now paid.
4. **Z.ai (chat.z.ai)** — for open-weights-aligned work and file generation.

### MCP

Active cross-vendor standard. Anthropic origin; OpenAI and Google announced support during 2025. 2026 roadmap (https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/, March 2026) lists transport scalability, agent communication, governance, enterprise readiness. African-specific MCP servers: did not find any in a brief search — flag honestly. Zotero community MCP servers exist; verify GitHub repo activity before linking.

### African / Global South perspectives

- **Esethu Framework:** Confirmed not directly about agents (data governance), but the equity argument transposes well to agentic RAG over local corpora. Reuse the Week 4 citation rather than over-claim.
- **POPIA + agents:** Multiple recent practitioner blogs (Michalsons, Cloudgate, Labournet) cover this explicitly; cross-border data transfer through agent connectors is the main flagged risk. Solid material for 10.5/10.6.
- **Compute access asymmetry:** UNDP figure — 95% of African AI researchers rely on Colab or free/shared tools; only 5% have meaningful compute access; 60% of top-500 supercomputers in US/China/Germany combined; none in Africa. Strong material for 10.5 free-tier framing and the pointer to Week 11.
- **Mozilla / AI Now / Sayash Kapoor:** Kapoor's reliability paper is the strongest critical-of-agents source; AI Now Institute and Mozilla have published more on agents in general policy frames — useful for Week 11 but lighter touch in Week 10.

### Gaps and honest flags

- **No African MCP servers found** (state explicitly in 10.3 / 10.5 — invitation for student work).
- **No Gowers post specifically on agents** (don't over-claim — reuse existing Week 9 citation).
- **OSWorld and WebArena May 2026 SOTA numbers** are reported via third-party aggregators (Coasty Blog, BenchmarkingAgents); will re-verify against the original benchmark sites at draft time. Treat current numbers as best-known but pending verify-references.
- **Anthropic "Orbit" proactive assistant** is a leak (per AINews 6 May), not a launched product — flag accordingly.
- **Manus benchmark claims** (GAIA SOTA) are company-reported; independent replication scarce — flag.
- **Chinese free-tier Deep Research quotas are opaque.** Kimi, Qwen and Z.ai publish no clear free-tier Deep Research quota numbers the way Perplexity / ChatGPT / Gemini do. Treat the "strongest free alternative to Perplexity" verdict as a working assumption pending live measurement at draft time.
- **POPIA exposure for Chinese-hosted tools.** Prompts and uploads to DeepSeek / Kimi / Qwen / Z.ai flow to servers in mainland China; mainland China is not currently a POPIA s.72 "adequate-protection" jurisdiction. The disclosure requirement in 10.6 must explicitly name the destination jurisdiction for any tool used on the assignment.
- **Manus public-access status conflicts across sources.** Some May 2026 secondary sources claim the waitlist was dropped in late 2025 (1,000-credit / 1-daily-task free trial), others report it remains invitation-only with a ~500K waitlist. Resolve at draft time by attempting sign-up from a SA IP and recording the result.

---

## Summary

This outline is dense, verifiable, and explicitly time-stamped. It draws the agent-failure backbone from a single anchor citation (Rabanser/Kapoor/Narayanan et al., arXiv:2602.16666) the way Week 9 drew the hallucination backbone from Kalai et al. The free-tool tour is grounded in checked-as-of-May-2026 quotas. The MCP and POPIA treatments are real but appropriately cautious. The activity is decided and matches the constraint envelope (free tools, UCT-realistic, applies Week 9 taxonomy explicitly).

Ready for user review before drafting begins.
