# Week 11 — Future of AI in Research & Africa's Sovereign AI Capacity

Status: outline / pending sign-off
Date: 30 May 2026
Build pattern: Python generator (`build_week11.py`, mirrors `build_week9.py`/`build_week10.py`)
Emphasis: **Africa-led (2 future + 4 sovereign capacity)**

This is the last content week before the Week 12 capstone. It pulls forward the course's African-context emphasis and lands students in a position to scope their final research project realistically.

---

## Pedagogical stance (across the week)

1. **Honest calibration over excitement.** Continue the Week 9/10 frame: distinguish *real* (peer-reviewed, shipping, lab-validated) from *overclaimed* (PR figures, single-venue results) from *aspirational* (announced, unfunded, speculative).
2. **Concrete African examples, not generic "Global South" framing.** Specific orgs, specific people, specific funded projects, specific gaps.
3. **Researcher-actionable.** Every sub-lesson asks "what does this mean for *your* research right now?"
4. **No model-version name-dropping.** Per the course convention from Week 8 on, capability discussions use family names (Claude family / GPT family / Gemini family); specific versions only in historical citations.
5. **No repeating Week 9/10.** Where the topic touches autonomous science / AlphaEvolve / Sakana / failure modes, reference rather than re-explain.

---

## Sub-lesson map

| # | Title | Half | Anchor question |
|---|-------|------|-----------------|
| 11.1 | What the Future of AI in Research Actually Looks Like | Futures | Which 2–5 year trajectories are real, overclaimed, or speculation? |
| 11.2 | The Shifting Research Landscape: Policy, Peer Review, Integrity | Futures | What rules have changed for authors, reviewers, and grant applicants? |
| 11.3 | Sovereign AI Capacity — and Why Compute Is the Floor | Africa | What does "sovereignty" mean, and what compute does Africa actually have? |
| 11.4 | Data, Languages and African Model-Building | Africa | What models, datasets, and benchmarks for African research exist now? |
| 11.5 | Policy, Institutions, and Talent | Africa | Where does the AU strategy meet country strategies meet research communities? |
| 11.6 | Where This Leaves Your Research + Hands-On Activity | Both | How does a researcher position their work given everything in Weeks 1–11? |

---

## 11.1 — What the Future of AI in Research Actually Looks Like

### Theme
A calibrated forward look. Frames the next 2–5 years as a mix of *shipping* (AlphaFold, GNoME/A-Lab autonomous synthesis, AI Co-Scientist's wet-lab-validated biomedical hits), *overclaimed* ("first AI-authored peer-reviewed paper" framings), and *aspirational* (end-to-end autonomous research). Builds on Week 10's harness/agentic framing without repeating it.

### Key citable facts
- **Sakana AI Scientist** in *Nature* (26 Mar 2026, DOI s41586-026-10265-5). ICLR ICBINB workshop manuscript scored 6.33/7 (above 55% of human authors). *Counterweight:* arXiv:2502.14297 "Bold Claims, Mixed Results" — independent critical eval, Feb 2025.
- **DeepMind AI Co-Scientist** (19 May 2026, *Nature* s41586-026-10644-y, rolled out via Gemini for Science). Six biomedical collaborations including 91% blockade of a fibrosis response (Peltz lab) and confirmed integrated-stress-response hypothesis (Calico).
- **FutureHouse Robin** (20 May 2025, arXiv:2505.13400) — identified ripasudil as dry-AMD candidate; phagocytosis ↑ 7.5× in vitro. FutureHouse spun out **Edison Scientific** (Nov 2025, $70M seed at ~$250M valuation); successor system **Kosmos** processes 1,500 papers + 42,000 lines of analysis code per run.
- **AlphaFold 3** (Abramson et al., *Nature* May 2024) — proteins + nucleic acids + small molecules + ions; code+weights opened to academia Nov 2024.
- **GNoME / LBNL A-Lab** — 2.2M predicted crystals, 381k stable, ~41 autonomously synthesised (Nov 2023, expanded through 2024).

### Honest assessment
- **Real:** AlphaFold lineage; GNoME/A-Lab; AI Co-Scientist's wet-lab-validated hits; Robin's ripasudil hypothesis-to-lab loop (though preclinical).
- **Overclaimed:** "First AI-authored peer-reviewed paper" — true only in a narrow workshop-track sense the authors negotiated; "55% of humans" is single-venue.
- **Aspirational:** End-to-end AI scientist replacing PhDs; Edison Scientific's commercial pitch; CEO timelines on "AGI-grade research."

### Source-card lineup
1. Sakana AI Scientist *Nature* paper — https://sakana.ai/ai-scientist-nature/
2. arXiv:2502.14297 — independent evaluation of Sakana
3. AI Co-Scientist (DeepMind) — https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/
4. Robin / FutureHouse — https://www.futurehouse.org/research-announcements/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system + arXiv:2505.13400
5. AlphaFold 3 — *Nature* 2024, DOI 10.1038/s41586-024-07487-w
6. GNoME / A-Lab — DeepMind blog + LBNL coverage

### Activity hook
"Pick a real result from the table; trace it to its primary source; explain *what specifically* the AI contributed vs the human researchers." Builds the verification habit we'll need in 11.6.

---

## 11.2 — The Shifting Research Landscape: Policy, Peer Review, Integrity

### Theme
The rules have changed, fast. Authorship policies, funder policies, peer-review confidentiality, and integrity tooling have all moved in the last 12–18 months — and the He & Bu PNAS 2026 paper shows that policies alone aren't changing behaviour. Frames the institutional moving target the researchers in this class are operating inside.

### Key citable facts
- **ICMJE recommendations** (medical journals) — AI chatbots cannot be authors; disclosure in cover letter and manuscript required; non-disclosure may be construed as misconduct.
- **NeurIPS 2025 LLM policy** — authors must document non-trivial LLM use; reviewers must not share submissions or code with any LLM.
- **NIH NOT-OD-23-149** (23 Jun 2023) — reviewers prohibited from using generative AI on grant proposals (confidentiality). Still in force.
- **NIH 2025 application policy** — from 25 Sep 2025 receipt date, applications "substantially developed by AI" not considered original ideas; six-application/PI/year cap.
- **NSF Notice** (14 Dec 2023) — reviewer-side prohibition; proposer-side disclosure encouraged.
- **UKRI policy** (20 Sept 2024, updated 3 Dec 2024) — applicant transparency required; reviewers prohibited from using genAI on applications.
- **NRF (South Africa)** — *no specific generative-AI-in-grants policy located as of 30 May 2026* (honest gap; the SA National AI Policy Framework is high-level and doesn't bind grant applicants).
- **He & Bu, PNAS 2026** (DOI 10.1073/pnas.2526734123) — 5,114 journals, 5.2M papers; ~70% have policies, but only ~0.1% of post-2023 papers disclose AI use.
- **Liang et al.**, arXiv:2410.03019 — ~20% of ICLR reviews and ~12% of *Nature Communications* reviews show LLM signatures.
- **Wang 2026**, *Learned Publishing* DOI 10.1002/leap.2035 — 24.5% of high-impact journals revised peer-review AI policies between Mar–Aug 2025; adoption rose 77% → 83%.
- **Retraction Watch** ChatGPT tracker — ~92 papers, 3 reviews with telltale LLM phrases.
- **Problematic Paper Screener** (Cabanac et al., arXiv:2402.03370) — >5,000 tortured-phrase fingerprints + 185 acronym fingerprints.
- **AI-detection tools** — converging consensus: unreliable for enforcement (high FP rates, easy evasion).

### Honest assessment
- **Real:** Funder policies are coherent and enforceable at the application stage; NeurIPS-style reviewer-confidentiality rules are clear; tortured-phrase detection catches mill output.
- **Overclaimed:** Industry pitches that AI-detection tools can reliably flag LLM writing or reviewing.
- **Aspirational:** Uniform disclosure — He & Bu shows the gulf between policy and practice.
- **Local gap:** NRF SA has no generative-AI grant policy; flag this for postgrads.

### Source-card lineup
1. He & Bu PNAS 2026 — https://www.pnas.org/doi/10.1073/pnas.2526734123
2. NIH NOT-OD-23-149 — https://grants.nih.gov/grants/guide/notice-files/NOT-OD-23-149.html
3. NIH 2025 Nexus notice — apply-responsibly policy (Jul 2025)
4. UKRI policy — https://www.ukri.org/publications/generative-artificial-intelligence-in-application-and-assessment-policy/
5. NSF Notice — https://www.nsf.gov/news/notice-to-the-research-community-on-ai
6. ICMJE — https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html
7. NeurIPS 2025 LLM Policy — https://neurips.cc/Conferences/2025/LLM
8. Wang 2026 *Learned Publishing* — DOI 10.1002/leap.2035
9. Liang et al., arXiv:2410.03019
10. Retraction Watch tracker — https://retractionwatch.com/papers-and-peer-reviews-with-evidence-of-chatgpt-writing/

### Activity hook
"Pick a journal in your field and a funder you'd realistically apply to. Find their current AI policies (or note their absence). One paragraph each."

---

## 11.3 — Sovereign AI Capacity, and Why Compute Is the Floor

### Theme
Defines AI sovereignty across five layers (compute, data, models, policy, talent) and rejects the binary "own it / depend on it" framing in favour of meaningful agency. The sub-lesson then zooms into the compute layer — the hard floor — because the rest depends on it. Continues the Week 3 grid/infrastructure story.

### Five-layer sovereignty frame (the spine of this sub-lesson)
1. **Compute** — GPUs, data centres, grid capacity.
2. **Data** — language corpora, domain datasets, governance.
3. **Models** — from-scratch pre-training, adaptation, evaluation.
4. **Policy** — strategy, legislation, regulator capacity.
5. **Talent** — pipelines, retention, communities.

Argument: sovereignty ≠ autarky. Most countries depend on global supply chains for all five. The question is *whether any layer has zero domestic agency* — and where the resulting dependency becomes a research-quality or ethical risk.

### Compute layer — facts
- **CHPC South Africa** — Lengau supercomputer (~1 PFLOPS, ~30,000 CPU cores, online 2016). Operational but pre-AI-era; increasingly outclassed for large-model training.
- **Konza National Data Centre** (Kenya) — Tier III, operational, 171 entities onboarded. Cloud/colo, not AI-supercompute.
- **Cassava Technologies + NVIDIA "AI Factory"** — 3,000 NVIDIA GPUs target SA by June 2025; planned 12,000 across Africa over 3–4 years; ~US$720M. *Genuine commercial deployment; not a sovereign public-good facility.*
- **Microsoft–G42 Kenya $1bn data centre** — announced May 2024; **stalled** as of 2026 over grid capacity (Ruto: cannot power at full scale). Honest example of compute-without-grid.
- **AU "AI Factory" / continental compute** — endorsed by Africa AI Council via Smart Africa (2025); *no operational facility or budget line traced to a primary AU document* as of May 2026.

### Honest assessment
- **Real:** CHPC, Konza, Cassava 3,000 GPU deployment in SA.
- **Overclaimed:** "Africa's first AI factory" branding for a commercial NVIDIA Cloud Partner; "continental compute" framing for an unfunded coordinating endorsement.
- **Aspirational:** Sovereign public-good AI compute facility at continental scale.
- **Bottleneck:** grid capacity, not GPU supply — Microsoft–G42 Kenya is the case study.

### Source-card lineup
1. CHPC — https://www.chpc.ac.za/
2. Konza Data Centre — https://dc.konza.go.ke/about
3. Cassava–NVIDIA — https://www.cassavatechnologies.com/cassava-to-upgrade-its-data-centres-with-nvidia-supercomputers-to-drive-africas-ai-future/
4. Microsoft–G42 Kenya — https://news.microsoft.com/source/2024/05/22/microsoft-and-g42-announce-1-billion-comprehensive-digital-ecosystem-initiative-for-kenya/

### Activity hook
"Find one operational and one announced-but-unbuilt AI-relevant compute facility in your country (or a country you work in). What's the public source for each? What does the difference tell you?"

---

## 11.4 — Data, Languages and African Model-Building

### Theme
The strongest layer of the sovereignty story. Peer-reviewed, reproducible, community-built. The sub-lesson is organised into three rings: (a) **community infrastructure** that makes the work possible (Masakhane, Lanfrica); (b) **models** trained from scratch or adapted (encoder, decoder, MT); (c) **benchmarks** that measure progress honestly across NLU, generation, sentiment, ASR, and retrieval. Lands with a UCT-built model — **MzansiLM** — as the local anchor.

### Community infrastructure
- **Masakhane** — grassroots NLP community since ~2019; >1,000 participants across 30+ African countries (self-reported). https://www.masakhane.io/
- **Lanfrica** — pan-African NLP-resource hub founded by Chris Emezue and Bonaventure Dossou. Catalogues and links African-language datasets, papers, models, benchmarks; emerged from a Masakhane survey of barriers to NMT work. Documents resources across ~2,199 African languages (including extinct ones). https://lanfrica.com
- **Charting the Landscape of African NLP** (EMNLP 2025) — meta-survey paper of African NLP progress; useful as a single citable landscape. https://aclanthology.org/2025.emnlp-main.1414.pdf
- **AfricaNLP 2025 workshop proceedings** — https://aclanthology.org/2025.africanlp-1.pdf

### Models — encoder, decoder, MT
- **MasakhaNER** (arXiv:2103.11811) — NER for 10 African languages; foundational dataset.
- **MAFAND-MT** (Masakhane) — many-to-many MT corpus for African languages.
- **AfroXLMR / AfriBERTa / AfriBERTa-V2 / AfroLM** — encoder-family foundations.
- **Serengeti** — multilingual encoder LM tuned for African languages.
- **Toucan** (arXiv:2407.04796, Elmadany et al., U Alberta / Adelani group) — many-to-many MT, 156 language pairs, 43 African languages + Ar/En/Fr; trained on **AfroLingu-MT** (the largest African MT benchmark to date).
- **InkubaLM-0.4B** (Lelapa AI; arXiv:2408.17024; https://huggingface.co/lelapa/InkubaLM-0.4B) — 422M params, 2.4B training tokens (1.9B from African languages); covers isiZulu, Yoruba, Swahili, isiXhosa, Hausa + EN/FR. CC BY-NC 4.0. **First sovereign African SLM trained from scratch.**
- **MzansiLM-125M + MzansiText corpus** (Lombard et al., arXiv:2603.20732, Mar 2026; HF: `anrilombard/mzansilm-125m`, `anrilombard/mzansi-text`) — **UCT-built**. First publicly available decoder-only LM trained from scratch across all 11 official SA written languages (Sepedi, Sesotho, Setswana, siSwati, Tshivenda, Xitsonga, Afrikaans, English, isiNdebele, isiXhosa, isiZulu). Monolingual fine-tuning hits 20.65 BLEU on isiXhosa data-to-text, competitive with encoder-decoder baselines 10× larger.
- **AfroLlama_V1** (Jacaranda Health; https://huggingface.co/Jacaranda/AfroLlama_V1) — Llama-3-8B continual-pretrained for SW/XH/ZU/YO/HA/EN.
- **Lugha-Llama** (arXiv:2504.06536, Apr 2025) — adapted LLM for African languages.
- **WURA** — large multilingual pre-training corpus including African-language documents.
- **Lelapa's productionised systems** — Vulavula (API), Africa Sondecho — commercial deployments of the InkubaLM lineage.
- **Esethu Framework** (arXiv:2502.15916; already in course Weeks 4 & 10) — sustainable dataset governance + Vuk'uzenzele isiXhosa speech dataset.

### Benchmarks
- **AfroBench** (arXiv:2311.07978, ACL 2025 Findings) — 64 languages, 15 tasks, 22 datasets.
- **IrokoBench** (arXiv:2406.03368, NAACL 2025) — 17 languages × AfriXNLI / AfriMGSM / AfriMMLU.
- **AfriSenti** (arXiv:2302.08956, EMNLP 2023; SemEval-2023 Task 12, 200+ participants) — 14 sentiment datasets, 110,000+ tweets, 14 African languages. https://huggingface.co/datasets/masakhane/afrisenti
- **AfriHate** — multilingual hate-speech / abusive-language datasets for African languages.
- **AfriSpeech-200** (TACL, MIT Press) — 200 hours Pan-African accented English ASR; 67,577 clips, 2,463 speakers, 120 accents, 13 countries; clinical + general domain.
- **African ASR systematic review** (arXiv:2510.01145) — PRISMA review of 74 datasets across 111 languages, ~11,206 hours; <15% of studies reproducible.
- **African ASR benchmarking** (arXiv:2512.10968, Nahabwe et al., Nov 2025) — Whisper / XLS-R / MMS / W2v-BERT on 13 languages.
- **AfriMTEB and AfriE5** (arXiv:2510.23896, Oct 2025) — text-embedding benchmark + adapted embedding model for African languages; extends MMTEB.

### Honest assessment
- **Real:** All of the above are peer-reviewed / community artefacts with code, data, or model weights. The Masakhane–Lanfrica–benchmarks–models stack is the most mature layer of the sovereignty story.
- **Overclaimed:** "First African LLM" framings in vendor PR. InkubaLM is small (a genuine sovereign SLM); MzansiLM is a 125M-parameter research model and not a SOTA chat system; AfroLlama and Lugha-Llama are *adaptations* of Llama, not from-scratch training.
- **Aspirational:** Parity with English-language SOTA on African languages. AfroBench and IrokoBench both document large persistent gaps as of 2025.
- **Reproducibility gap:** <15% of African ASR studies are reproducible (per the survey) — an honest problem and a real research opening.

### Activity hook
"Identify a language or domain in your work where African-language or African-context data is the rate-limiter. Find one Masakhane-tradition dataset that helps and one that doesn't yet exist. Bonus: search Lanfrica for both."

---

## 11.5 — Policy, Institutions, and Talent

### Theme
How the layered policy stack (continental → national → community) actually fits together, and who the institutions are that turn it into research. Calibrated honestly: strategies are real documents but largely aspirational in execution.

### Key citable facts — policy stack
- **AU Continental AI Strategy** — adopted by STC 11–13 June 2024; ratified by Executive Council July 2024 in Accra. Five focus areas: harnessing benefits, building capabilities, minimising risks, stimulating investment, fostering cooperation. Aligned to Agenda 2063.
- **South Africa** — National AI Policy Framework, DCDT, August 2024 (draft; 32 public submissions; not yet binding).
- **Rwanda** — National AI Policy, Cabinet-approved 20 Apr 2023 (first comprehensive African national AI policy).
- **Kenya** — Kenya AI Strategy 2025–2030, launched 27 Mar 2025. Three pillars: infrastructure, data/governance, R&I.
- **Nigeria** — National AI Strategy draft Aug 2024; revised Sept 2025 (the revision-within-13-months is itself a signal).
- **Egypt** — National AI Strategy 2nd edition, Jan 2025; targets ICT GDP share 7.7% by 2030; US$42.7bn annual AI value and 30,000 trained specialists by 2030 (policy aspiration, not forecast).
- **Smart Africa AI Blueprint** (2021) — pan-African policy recommendations.

### Key citable facts — institutions & talent
- **Deep Learning Indaba** — founded 2017; 2025 edition Kigali (17–22 Aug 2025; U Rwanda host).
- **AIMS / Next Einstein Initiative** — founded 2003; six centres (RSA, Senegal, Ghana, Cameroon, Tanzania, Rwanda); AMMI Master's programme. https://nexteinstein.org/
- **ARIN** (Africa Research & Impact Network) — broader sustainability/impact network with an AI workstream. https://arin-africa.org/
- **Masakhane** as institution-shaped community (not formally an org but functioning like one).
- **Lelapa AI** as the leading African commercial gen-AI lab (InkubaLM, Vulavula, Africa Sondecho).

### Honest assessment
- **Real documents:** All listed strategies exist. Most lack funded implementation, binding legislation, or KPI audit. Rwanda and Egypt have the most institutional follow-through; SA is still pre-policy; Nigeria's revision-within-13-months suggests instability.
- **AU strategy:** even more pointed than "aspirational." Per Yilma & Wodajo, the AU AI Strategy was conceived and ratified less as a governance instrument than as an advocacy position for the UN Global Digital Compact negotiations — produced in a few rushed months and now functioning as a coordinating signal rather than a budgeted programme.
- **Strategy-to-legislation pipeline is largely absent:** only Ethiopia (draft AI Development and Regulation Proclamation, EU-AI-Act-shaped) and Morocco (bill not even preceded by a strategy) have publicly announced AI legislative processes.
- **Borrowing is built in:** the AU Strategy itself directs members to "best practices" from the EU, Canada, UK. Ethiopia's draft bill emulates the EU AI Act's risk-based approach. The Effoduh and Ogoh-et-al. papers frame this as **normative mimicry / mimetic isomorphism**.
- **Institutional layer is strong** (Indaba, AIMS, ARIN, Lelapa, Masakhane), but talent retention is the open question (we don't have hard numbers; flag honestly).

### Source-card lineup

**Continent-wide reviews (lead with these):**
- **Yilma, K. & Wodajo, K. (2026). "Strategy as Governance: The Governance of AI in Africa."** *Science and Public Policy* 53(2), April 2026, 236–244. **CC-BY 4.0 open access** — DOI 10.1093/scipol/scag011. Editorial introduction to a special section titled "Beyond the Hype: Deconstructing Visions of AI Governance in Africa."
  - Open-access via Oxford Academic: https://academic.oup.com/spp/article/53/2/236/8654722
  - Preprint (White Rose): https://eprints.whiterose.ac.uk/id/eprint/236807/1/Ed%20Intro,%20final%20version%20Dec%202025.pdf
  - **Key arguments to lead 11.5 with:**
     1. *Strategy as governance is the defining African pattern.* Close to a dozen AU member states have introduced AI strategies — Mauritius (2018), Egypt (2019), Algeria (2021), Ghana (2022), Benin / Rwanda / Senegal (2023), Ethiopia (2024) — but **only Ethiopia and Morocco have publicly announced an AI legislative process** as of the paper's writing. The rest stop at strategy.
     2. *The AU Continental AI Strategy was conceived as an advocacy instrument, not a governance instrument.* The paper quotes the then–AU Commission Chairperson Moussa Faki Mahamat telling the 45th Executive Council (Accra, 18–19 July 2024) that the AU AI Strategy and the African Digital Compact would serve as advocacy instruments for the **African Common Position** in the UN Global Digital Compact negotiations. The strategy was produced largely between April and July 2024 — "a rushed and opaque process" (the paper's framing).
     3. *The AU Strategy is internally incoherent about its own role.* It sometimes positions itself as a framework for member states to "domesticate" (implying legislation), and sometimes proposes regional governance mechanisms (an AI ethics board, advisory board, ethics guidelines) — but never lays out a pathway from strategy to legislation. The result: a fragmented governance landscape with incoherent and ambiguous visions.
     4. *Borrowing from elsewhere is built in.* Section 32 of the AU Strategy itself directs member states to consider "best practices" from the EU AI Act, the Canadian AIDA, and the UK Artificial Intelligence Regulation. Ethiopia's draft AI Bill already emulates the EU AI Act's risk-based approach. The paper draws an analogy to the 2014 Malabo Convention, which took ~10 years to ratify and saw member states enact EU-/CoE-derived domestic law in the meantime.
     5. *Other recent continental moves.* AUDA-NEPAD released a Continental AI Roadmap in Feb 2025 (a "complementary resource" with only high-level governance recommendations). The Africa Declaration on AI (April 2025, Global AI Summit on Africa) — signed by nearly every AU member — endorses the creation of an **African AI Scientific Panel**, a regional parallel to the UN Global Digital Compact's international scientific panel.
- **Munga, J. & Quansah, S. (Sept 2025). "Understanding Africa's AI Governance Landscape."** Carnegie Endowment. https://carnegieendowment.org/posts/2025/09/understanding-africas-ai-governance-landscape-insights-from-policy-practice-and-dialogue — 15 national + 2 continental strategies; uses the AfTech tracker.
- **Engida Abdella, S. & Alayande, A. (Apr 2025). "African Countries Are Racing to Create AI Strategies — But Are They Putting the Cart Before the Horse?"** Global Center on AI Governance. https://www.globalcenter.ai/research/african-countries-are-racing-to-create-ai-strategies-but-are-they-putting-the-cart-before-the-horse — sceptical foil; focused on Kenya / Zambia with reference to SA, Nigeria, Ghana; argues strategies skip infrastructure/timelines/benefit-sharing.
- **CIPESA SIFA 2025 — "Navigating the Implications of AI on Digital Democracy in Africa"** — empirical research across 14 countries (Cameroon, Egypt, Ethiopia, Ghana, Kenya, Mozambique, Namibia, Nigeria, Rwanda, Senegal, SA, Tunisia, Uganda, Zimbabwe). https://cipesa.org/2025/09/state-of-internet-freedom-in-africa-report/

**Primary continental + national strategy documents:**
- AU PDF — https://au.int/sites/default/files/documents/44004-doc-EN-_Continental_AI_Strategy_July_2024.pdf
- AU adoption press release — https://au.int/en/pressreleases/20240617/african-ministers-adopt-landmark-continental-artificial-intelligence-strategy
- SA — https://www.dcdt.gov.za/sa-national-ai-policy-framework.html
- Rwanda — https://www.minict.gov.rw/ai-policy
- Kenya — https://ict.go.ke/sites/default/files/2025-03/Kenya%20AI%20Strategy%202025%20-%202030.pdf
- Nigeria — https://ncair.nitda.gov.ng/wp-content/uploads/2025/09/National-Artificial-Intelligence-Strategy-19092025.pdf
- Egypt — https://ai.gov.eg/SynchedFiles/en/Resources/AIstrategy%20English%2016-1-2025-1.pdf
- Smart Africa — https://smartafrica.org/wp-content/uploads/2023/11/70029-eng_ai-for-africa-blueprint-min.pdf

**Companion papers in the SPP 53(2), April 2026 special section "Beyond the Hype: Deconstructing Visions of AI Governance in Africa"** *(all elevated to source cards on the 11.5 lesson page)*:

- **Effoduh, J. O. (2026). "Decolonizing the governance of artificial intelligence in Africa: from normative mimicry to epistemic sovereignty."** *Science and Public Policy* 53(2), 245–257. DOI 10.1093/scipol/scag005. https://academic.oup.com/spp/article/53/2/245/8654721 — TWAIL + decolonial inquiry; introduces **"normative mimicry"** as the failure mode of African AI governance (epistemic subordination, institutional dependency, restricted policy autonomy).
- **Ogoh, G. et al. (2026). "AI governance in North Africa: an ecosystems approach."** *Science and Public Policy* 53(2), 258–276. DOI 10.1093/scipol/scag007. https://academic.oup.com/spp/article/53/2/258/8654720 — Empirical thematic + ecosystem analysis across Egypt, Morocco, Mauritania, Algeria, Libya, Tunisia. Reads the EU/US alignment as **mimetic isomorphism**.
- **Nyabola, N. (2026). "Foundations for African feminism as an ethics for artificial intelligence."** *Science and Public Policy* 53(2), 277–288. DOI 10.1093/scipol/scag009. https://academic.oup.com/spp/article/53/2/277/8654723 — Decolonial African feminist critique; pushes back on **reductive invocations of Ubuntu** in AI policy and argues for an epistemic shift grounded in African philosophies of personhood, relationality, environmental interdependence.
- **Mutung'u, G. et al. (2026). "Regulatory entrepreneurship's threat to digital sovereignty: the case of Worldcoin in Kenya."** *Science and Public Policy* 53(2), 289–299. DOI 10.1093/scipol/scag010. https://academic.oup.com/spp/article/53/2/289/8654728 — Concrete African enforcement case study: **Worldcoin / World Network in Kenya**, with documented breaches of Kenya's 2019 Data Protection Act. Frames national digital sovereignty as deriving authority from the duty to protect individual digital rights.
- **Ibrahim, N. et al. (2026). "AI models for detecting and generating hate speech: implications for Ethiopian policy."** *Science and Public Policy* 53(2), 300–315. DOI 10.1093/scipol/scag006. https://academic.oup.com/spp/article/53/2/300/8654735 — Trans-disciplinary empirical work on LLMs for hate speech in Ethiopia; critical reading of Ethiopia's AI Policy; proposes the **ASPIRE framework** (Adapting policy / Strengthening linguistic inclusivity / Preventing AI misuse / Improving infrastructure / Resourcing media literacy / Emphasizing hate-speech overlaps).
- **Jimoh, M. (2026). "Achieving fair AI in Africa? Ideas from the African charter on human and peoples' rights."** *Science and Public Policy* 53(2), 316–328. DOI 10.1093/scipol/scag008. https://academic.oup.com/spp/article/53/2/316/8654724 — Examines the **African Charter on Human and Peoples' Rights** as a foundation for "fair AI"; non-discrimination; the African Commission's Art. 45 mandate; centring Ubuntu in the governance structure.

**Institutions:**
- Indaba — https://deeplearningindaba.com/
- AIMS — https://nexteinstein.org/
- ARIN (Africa Research & Impact Network) — https://arin-africa.org/
- Lelapa AI — https://lelapa.ai/

### Activity hook
"Read the AU strategy's five pillars. For each, find one piece of evidence that your country is or isn't actually implementing it (could be a policy, a funded programme, or a notable gap). 5 short paragraphs."

---

## 11.6 — Where This Leaves *Your* Research + Hands-On Activity

### Theme
Synthesis. Folds the futures half (what's coming) and the sovereignty half (what we have) into a single question: *given everything in this course, how do you scope a research project in 2026 that is honest, useful, and grounded in your context?* Bridge to Week 12 capstone.

### Structure
1. **Recap as a frame, not a list.** Five 1-paragraph passes across the course: foundations → ethics → environment → critical evaluation → agentic tools → African capacity.
2. **The 2026 researcher's positioning question.** Four axes:
   - *Where in the research pipeline does AI genuinely help me?* (link to Weeks 5–8)
   - *Where does it create new risks or dependencies?* (link to Weeks 3, 4, 9)
   - *Where does African data/context/community give my work distinctive leverage?* (link to 11.4, 11.5)
   - *What can I verify, and how often?* (link to Week 9.5, Week 10 reliability)
3. **Hands-on activity — "Your Week-12 Pitch in 11.6":** A 300-word structured pitch:
   - one-sentence research question;
   - which AI tools you'll use in which stage;
   - what you will NOT delegate to AI;
   - one local-context choice you're making (data, language, collaboration, hosting);
   - one verification protocol you commit to.
   This becomes the seed for the Week 12 capstone.
4. **Closing.** Single page. No "Next week" pointer — Week 12 is the capstone, not a content week.

### Sources
Reuses sources from across the course; introduces no new primary references.

---

## What I'm NOT including (and why)

- **A separate "AI for African languages in education" sub-lesson.** Strong topic; out of scope for a research course; could be a guest-lecture pointer in 11.4.
- **A deep-dive on AU national-level law (POPIA / NDPR / DPA Kenya).** Covered substantially in Week 10.5; reference and move on.
- **A separate ethics sub-lesson.** Week 4 owns this; cross-reference.
- **Speculation on AGI timelines.** Out of scope by course pedagogy; note and move on.
- **Re-doing autonomous-science.** Week 10.3 owns this; 11.1 builds on it without repeating.

---

## Verification plan

Per CLAUDE.md, after building Week 11 the `/verify-references` skill runs against all six HTML files. Specific things to verify:
- Every arXiv ID and DOI resolves and the content matches the citation.
- The AU PDF link delivers (file is binary so WebFetch can't parse contents; corroborate via the AU press release page).
- The Nature paper URLs (Sakana, Robin, Co-Scientist) — these are auth-walled in WebFetch but verified-by-existence-metadata; flag at verification time.
- The PNAS He & Bu DOI resolves (10.1073/pnas.2526734123).
- All NIH / NSF / UKRI / NeurIPS / ICMJE policy pages still resolve.

---

## Build process from here

1. Outline sign-off (this document).
2. Draft 11.1 → audit → user review.
3. Draft 11.2 → audit → user review.
4. Continue 11.3 → 11.6 the same way.
5. Build `Table of Contents.html`.
6. `/verify-references Week 11`.
7. Copy to `docs/week-11/`, update `docs/index.html`, push to GitHub.
8. Add Week 11 references to the papers site (`build_papers_site.py`).
9. Upload to Amathuba (the user will trigger this).

---

## Open questions for sign-off

1. **Activity for 11.6.** The "Your Week-12 Pitch" structure above — does that match what you want as the capstone bridge, or do you want a different hands-on?
2. **Country focus.** I default to a stack of SA / Kenya / Rwanda / Nigeria / Egypt for national strategies. Add Ghana? Senegal? Morocco? Drop any?
3. **Should 11.5 include a section on POPIA-style cross-border data carry-over from Week 10?** Or just one-sentence cross-reference and move on?
4. **Are you comfortable citing the auth-walled Nature URLs** for Sakana / Co-Scientist / Robin given they're verifiable by other means, or should we lead with the lab-blog primary sources only?
