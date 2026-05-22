#!/usr/bin/env python3
"""
Generate the styled HTML 'Papers' section of the GitHub Pages site
from a single embedded data structure.

Outputs:
  docs/papers/index.html             - landing page listing the weeks
  docs/papers/week-N.html            - one page per week, link-only

Each reference links to its canonical source (arXiv abstract, journal DOI,
or publisher page). PDFs are NOT redistributed from this repo.

Re-run this script whenever the data below changes.
"""

import os
import textwrap
from html import escape

REPO = os.path.dirname(os.path.abspath(__file__))
DOCS_PAPERS = os.path.normpath(os.path.join(REPO, "..", "docs", "papers"))

# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

# Each week has:
#   topic       - title shown in headers
#   tagline     - one-liner shown under header
#   summary     - short paragraph for the index card and intro on the week page
#   sublessons  - list of dicts with id, title, papers (list of paper dicts)
#   paywalled   - list of paywalled / link-only references (citation, sublesson, note)
#   notes       - optional extra paragraph (e.g. citation corrections)

WEEKS = {
    1: {
        "topic": "Foundations of Generative AI",
        "tagline": "Video-led introductory week",
        "summary": (
            "Week 1 is built around video lectures rather than primary literature, "
            "so there are no PDFs to host here. Resources used in the week are "
            "listed for reference."
        ),
        "sublessons": [],
        "paywalled": [],
        "extra_html": """
            <p>The week's resources are all video material:</p>
            <ul class="styled-list">
                <li>3Blue1Brown &mdash; <em>But what is a neural network?</em> (Sub-Lesson 1.4)</li>
                <li>3Blue1Brown &mdash; <em>Gradient descent</em> (Sub-Lesson 1.4)</li>
                <li>3Blue1Brown &mdash; <em>What is a transformer?</em> (Sub-Lesson 1.6)</li>
                <li>3Blue1Brown &mdash; <em>Attention in transformers</em> (Sub-Lesson 1.6)</li>
                <li>Jonathan Shock &mdash; <em>A lightning tour of AI</em> (UCT seminar, Sub-Lesson 1.3)</li>
            </ul>
            <p>Primary academic literature begins in Week 2.</p>
        """,
        "paper_count": 0,
    },
    2: {
        "topic": "LLM Deep Dive",
        "tagline": "Architecture, training, and alignment of large language models",
        "summary": "11 arXiv papers covering transformers, scaling laws, instruction tuning, RLHF, and the major open and closed model families.",
        "paper_count": 11,
        "sublessons": [
            {
                "id": "2.1", "title": "LLM Architecture Deep Dive",
                "papers": [
                    {
                        "file": "Vaswani_2017_Attention-Is-All-You-Need.pdf",
                        "authors": "Vaswani, A., et al.",
                        "year": "2017",
                        "title": "Attention Is All You Need",
                        "venue": "NeurIPS 2017",
                        "src_label": "arXiv:1706.03762",
                        "src_url": "https://arxiv.org/abs/1706.03762",
                    },
                ],
            },
            {
                "id": "2.2", "title": "Training Large Language Models",
                "papers": [
                    {"file": "Kaplan_2020_Scaling-Laws.pdf",
                     "authors": "Kaplan, J., et al.", "year": "2020",
                     "title": "Scaling Laws for Neural Language Models",
                     "src_label": "arXiv:2001.08361", "src_url": "https://arxiv.org/abs/2001.08361"},
                    {"file": "Brown_2020_GPT-3-Few-Shot-Learners.pdf",
                     "authors": "Brown, T., et al.", "year": "2020",
                     "title": "Language Models are Few-Shot Learners (GPT-3)",
                     "venue": "NeurIPS 2020",
                     "src_label": "arXiv:2005.14165", "src_url": "https://arxiv.org/abs/2005.14165"},
                    {"file": "Hoffmann_2022_Chinchilla.pdf",
                     "authors": "Hoffmann, J., et al.", "year": "2022",
                     "title": "Training Compute-Optimal Large Language Models (Chinchilla)",
                     "src_label": "arXiv:2203.15556", "src_url": "https://arxiv.org/abs/2203.15556"},
                    {"file": "OpenAI_2023_GPT-4-Technical-Report.pdf",
                     "authors": "OpenAI", "year": "2023",
                     "title": "GPT-4 Technical Report",
                     "src_label": "arXiv:2303.08774", "src_url": "https://arxiv.org/abs/2303.08774"},
                    {"file": "Touvron_2023_Llama-2.pdf",
                     "authors": "Touvron, H., et al.", "year": "2023",
                     "title": "Llama 2: Open Foundation and Fine-Tuned Chat Models",
                     "src_label": "arXiv:2307.09288", "src_url": "https://arxiv.org/abs/2307.09288"},
                    {"file": "Dubey_2024_Llama-3-Herd.pdf",
                     "authors": "Dubey, A., et al.", "year": "2024",
                     "title": "The Llama 3 Herd of Models",
                     "src_label": "arXiv:2407.21783", "src_url": "https://arxiv.org/abs/2407.21783"},
                ],
            },
            {
                "id": "2.3", "title": "Fine-Tuning, RLHF and Alignment",
                "papers": [
                    {"file": "Hu_2021_LoRA.pdf",
                     "authors": "Hu, E. J., et al.", "year": "2021",
                     "title": "LoRA: Low-Rank Adaptation of Large Language Models",
                     "src_label": "arXiv:2106.09685", "src_url": "https://arxiv.org/abs/2106.09685"},
                    {"file": "Ouyang_2022_InstructGPT.pdf",
                     "authors": "Ouyang, L., et al.", "year": "2022",
                     "title": "Training language models to follow instructions with human feedback (InstructGPT)",
                     "src_label": "arXiv:2203.02155", "src_url": "https://arxiv.org/abs/2203.02155"},
                    {"file": "Bai_2022_Constitutional-AI.pdf",
                     "authors": "Bai, Y., et al.", "year": "2022",
                     "title": "Constitutional AI: Harmlessness from AI Feedback",
                     "src_label": "arXiv:2212.08073", "src_url": "https://arxiv.org/abs/2212.08073"},
                    {"file": "Rafailov_2023_DPO.pdf",
                     "authors": "Rafailov, R., et al.", "year": "2023",
                     "title": "Direct Preference Optimization: Your Language Model is Secretly a Reward Model",
                     "venue": "NeurIPS 2023",
                     "src_label": "arXiv:2305.18290", "src_url": "https://arxiv.org/abs/2305.18290"},
                ],
            },
            {
                "id": "2.4", "title": "How AI Image Generation Works",
                "papers": [],
                "note": "Explanatory content only &mdash; no primary papers in this sub-lesson.",
            },
        ],
        "paywalled": [],
    },
    3: {
        "topic": "Environmental Implications of AI",
        "tagline": "Energy, water, hardware lifecycle, and the rebound problem",
        "summary": "9 papers covering AI energy and water consumption, embodied carbon, the Jevons rebound, sustainable AI practice, and the token cost of agentic coding. The OECD policy report and several agentic-energy references are link-only.",
        "paper_count": 9,
        "sublessons": [
            {
                "id": "3.1", "title": "What Does AI Actually Consume?",
                "papers": [
                    {"file": "Li_2023_Making-AI-Less-Thirsty.pdf",
                     "authors": "Li, P., Yang, J., Islam, M. A., & Ren, S.", "year": "2023",
                     "title": "Making AI Less &lsquo;Thirsty&rsquo;: Uncovering and Addressing the Secret Water Footprint of AI Models",
                     "src_label": "arXiv:2304.03271", "src_url": "https://arxiv.org/abs/2304.03271"},
                    {"file": "Luccioni_2024_Power-Hungry-Processing.pdf",
                     "authors": "Luccioni, S., Jernite, Y., & Strubell, E.", "year": "2024",
                     "title": "Power Hungry Processing: Watts Driving the Cost of AI Deployment?",
                     "venue": "FAccT &rsquo;24",
                     "src_label": "arXiv:2311.16863", "src_url": "https://arxiv.org/abs/2311.16863"},
                    {"authors": "Stanford Digital Economy Lab &amp; Microsoft Research", "year": "2026",
                     "title": "How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks",
                     "venue": "supports the agentic-multiplier estimate in 3.1",
                     "src_label": "arXiv:2604.22750", "src_url": "https://arxiv.org/abs/2604.22750"},
                ],
            },
            {
                "id": "3.2", "title": "Infrastructure, Scale and the Rebound Problem",
                "papers": [
                    {"file": "Gupta_2021_Chasing-Carbon.pdf",
                     "authors": "Gupta, U., et al.", "year": "2021",
                     "title": "Chasing Carbon: The Elusive Environmental Footprint of Computing",
                     "venue": "IEEE HPCA 2021",
                     "src_label": "arXiv:2011.02839", "src_url": "https://arxiv.org/abs/2011.02839"},
                    {"file": "Wright_2023_Efficiency-Is-Not-Enough.pdf",
                     "authors": "Wright, D., Igel, C., Samuel, G., & Selvan, R.", "year": "2023",
                     "title": "Efficiency is Not Enough: A Critical Perspective of Environmentally Sustainable AI",
                     "src_label": "arXiv:2309.02065", "src_url": "https://arxiv.org/abs/2309.02065"},
                    {"file": "Patterson_2022_Carbon-Footprint-Plateau.pdf",
                     "authors": "Patterson, D., et al.", "year": "2022",
                     "title": "The Carbon Footprint of Machine Learning Training Will Plateau, Then Shrink",
                     "src_label": "arXiv:2204.05149", "src_url": "https://arxiv.org/abs/2204.05149"},
                ],
            },
            {
                "id": "3.3", "title": "Critical Minerals and AI",
                "papers": [],
                "note": "Sub-lesson uses news reporting and policy documents (CHIPS Act, EU CRMA, US Geological Survey) which aren&rsquo;t redistributable PDFs.",
            },
            {
                "id": "3.4", "title": "Sustainable AI: What Can Be Done?",
                "papers": [
                    {"file": "Schwartz_2019_Green-AI.pdf",
                     "authors": "Schwartz, R., Dodge, J., Smith, N. A., & Etzioni, O.", "year": "2019",
                     "title": "Green AI",
                     "src_label": "arXiv:1907.10597", "src_url": "https://arxiv.org/abs/1907.10597"},
                    {"file": "Rolnick_2019_Tackling-Climate-Change-with-ML.pdf",
                     "authors": "Rolnick, D., et al.", "year": "2019",
                     "title": "Tackling Climate Change with Machine Learning",
                     "src_label": "arXiv:1906.05433", "src_url": "https://arxiv.org/abs/1906.05433"},
                    {"file": "Dodge_2022_Carbon-Intensity-Cloud.pdf",
                     "authors": "Dodge, J., et al.", "year": "2022",
                     "title": "Measuring the Carbon Intensity of AI in Cloud Instances",
                     "venue": "FAccT &rsquo;22",
                     "src_label": "arXiv:2206.05229", "src_url": "https://arxiv.org/abs/2206.05229"},
                ],
            },
        ],
        "paywalled": [
            {"citation": "OECD (2022). <em>Measuring the environmental impacts of artificial intelligence compute and applications.</em>",
             "url": "https://doi.org/10.1787/7babf571-en", "url_label": "DOI:10.1787/7babf571-en",
             "sublesson": "3.4",
             "note": "Open-access on the OECD library &mdash; included as a link rather than a downloaded copy because the OECD URL changes occasionally."},
        ],
        "extra_html": """
            <p>The agentic-energy estimate in Sub-Lesson 3.1 also draws on these non-paper sources (reports and documentation rather than academic papers):</p>
            <ul class="styled-list">
                <li>Stanford Digital Economy Lab (2026). <em>How are AI agents spending your tokens?</em> &mdash; <a href="https://digitaleconomy.stanford.edu/news/how-are-ai-agents-spending-your-tokens/" target="_blank" rel="noopener">analysis</a> of the token-consumption study above.</li>
                <li>Anthropic (2026). <em>Effort</em> documentation (Claude effort levels: low / medium / high / xhigh / max) &mdash; <a href="https://platform.claude.com/docs/en/build-with-claude/effort" target="_blank" rel="noopener">platform.claude.com</a></li>
                <li>US EPA. <em>Greenhouse Gas Emissions from a Typical Passenger Vehicle</em> (~0.25&nbsp;kg&nbsp;CO&#8322;/km) &mdash; <a href="https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle" target="_blank" rel="noopener">epa.gov</a></li>
                <li>Republic of South Africa (2024). <em>2022 Grid Emission Factors Report</em> (~0.9&nbsp;kg&nbsp;CO&#8322;/kWh) &mdash; <a href="https://www.gov.za/sites/default/files/gcis_document/202411/51495gon5498.pdf" target="_blank" rel="noopener">gov.za PDF</a></li>
            </ul>
        """,
    },
    4: {
        "topic": "Ethical Frameworks for AI in Research",
        "tagline": "Ethics, ubuntu, transparency, and the just-AI framework",
        "summary": "2 arXiv papers downloaded; 4 journal items (Birhane Patterns, two Nature comments, Lund JASIST) listed as DOI links because the publishers don't expose direct PDF endpoints.",
        "paper_count": 2,
        "sublessons": [
            {
                "id": "4.1", "title": "Ethical Frameworks and Four Lenses",
                "papers": [
                    {"file": "Jobin_2019_AI-Ethics-Guidelines-Landscape.pdf",
                     "authors": "Jobin, A., Ienca, M., & Vayena, E.", "year": "2019",
                     "title": "The Global Landscape of AI Ethics Guidelines",
                     "venue": "Nature Machine Intelligence",
                     "src_label": "arXiv:1906.11668", "src_url": "https://arxiv.org/abs/1906.11668"},
                ],
            },
            {
                "id": "4.2", "title": "Ubuntu, Relational Ethics and the Just AI Framework",
                "papers": [
                    {"file": "Rajab_2025_Esethu-Framework.pdf",
                     "authors": "Rajab, J., Aremu, A., Chimoto, E. A., et al.", "year": "2025",
                     "title": "The Esethu Framework: Reimagining Sustainable Dataset Governance and Curation for Low-Resource Languages",
                     "src_label": "arXiv:2502.15916", "src_url": "https://arxiv.org/abs/2502.15916"},
                ],
            },
            {"id": "4.3", "title": "Transparency, Authorship and Integrity", "papers": [],
             "note": "Built around journal policy comparisons (Nature, Science, IEEE, ACM, Elsevier, PLOS) which are policies, not papers."},
            {"id": "4.4", "title": "Applying Ethics: Case Studies and Your Framework", "papers": [], "note": "Case-study material only."},
            {"id": "4.5", "title": "The Broader Landscape of AI Ethics (supplementary)", "papers": [], "note": "Links to organisations and frameworks rather than primary papers."},
        ],
        "paywalled": [
            {"citation": "Birhane, A. (2021). Algorithmic Injustice: A Relational Ethics Approach. <em>Patterns</em> 2(2).",
             "url": "https://doi.org/10.1016/j.patter.2021.100205", "url_label": "DOI:10.1016/j.patter.2021.100205",
             "sublesson": "4.1, 4.2",
             "note": "Open access at Cell Press but no direct PDF endpoint without their auth flow. Click through the DOI."},
            {"citation": "Nature Editorial (2023). Tools Such as ChatGPT Threaten Transparent Science; Here Are Our Ground Rules. <em>Nature</em> 613.",
             "url": "https://doi.org/10.1038/d41586-023-00191-1", "url_label": "DOI:10.1038/d41586-023-00191-1",
             "sublesson": "4.1, 4.3",
             "note": "Free to read on Nature.com; comments don&rsquo;t have a redistributable PDF."},
            {"citation": "van Dis, E. A. M., et al. (2023). ChatGPT: Five Priorities for Research. <em>Nature</em> 614.",
             "url": "https://doi.org/10.1038/d41586-023-00288-7", "url_label": "DOI:10.1038/d41586-023-00288-7",
             "sublesson": "4.1, 4.3",
             "note": "Free to read; same constraint as above."},
            {"citation": "Lund, B. D., et al. (2023). ChatGPT and a New Academic Reality. <em>JASIST</em>.",
             "url": "https://doi.org/10.1002/asi.24750", "url_label": "DOI:10.1002/asi.24750",
             "sublesson": "4.1, 4.3",
             "note": "Wiley paywalled; UCT library has a Wiley subscription."},
        ],
        "extra_html": """
            <p>Other references in Week 4 are not academic papers in the strict sense:</p>
            <ul class="styled-list">
                <li>Mhlambi, S. <em>From Rationality to Relationality</em> (2020) &mdash; archived at <a href="https://perma.cc/Q5ZL-TTD8" target="_blank" rel="noopener">perma.cc/Q5ZL-TTD8</a></li>
                <li>RIA Just AI Framework (Chetty &amp; Sey, 2025) &mdash; <a href="https://researchictafrica.net" target="_blank" rel="noopener">Research ICT Africa</a> report</li>
            </ul>
        """,
    },
    5: {
        "topic": "AI-Assisted Literature Reviews",
        "tagline": "Tools, the hallucinated-citation crisis, and AI-augmented research workflows",
        "summary": "5 papers covering hallucination rates across legal, medical and scientific contexts plus systematic-review screening. Most other Week 5 references are tool documentation rather than primary papers.",
        "paper_count": 5,
        "sublessons": [
            {
                "id": "5.1", "title": "The AI Literature Review Landscape",
                "papers": [
                    {"file": "Syriani_2023_ChatGPT-Systematic-Reviews.pdf",
                     "authors": "Syriani, E., David, I., & Kumar, G.", "year": "2023",
                     "title": "Assessing the Ability of ChatGPT to Screen Articles for Systematic Reviews",
                     "src_label": "arXiv:2307.06464", "src_url": "https://arxiv.org/abs/2307.06464"},
                ],
            },
            {"id": "5.2", "title": "Free Tools Deep Dive", "papers": [],
             "note": "Covers Semantic Scholar, ResearchRabbit, Connected Papers, NotebookLM, Google Scholar &mdash; tools, not papers."},
            {"id": "5.3", "title": "Paid Tools and When They Are Worth It", "papers": [],
             "note": "Covers Elicit, Consensus, Scite.ai, SciSpace, Litmaps Premium &mdash; tools, not papers."},
            {
                "id": "5.4", "title": "The Hallucinated Citation Crisis",
                "papers": [
                    {"file": "Magesh_2024_Hallucination-Free-Legal-AI.pdf",
                     "authors": "Magesh, V., Surani, F., Dahl, M., Suzgun, M., Manning, C. D., & Ho, D. E.", "year": "2024",
                     "title": "Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools",
                     "venue": "Stanford HAI",
                     "src_label": "arXiv:2405.20362", "src_url": "https://arxiv.org/abs/2405.20362"},
                    {"file": "Chelli_2024_Hallucinations-Systematic-Reviews.pdf",
                     "authors": "Chelli, M., Descamps, J., Lavou&eacute;, V., et al.", "year": "2024",
                     "title": "Hallucination Rates and Reference Accuracy of ChatGPT and Bard for Systematic Reviews",
                     "venue": "JMIR 26: e53164",
                     "src_label": "DOI:10.2196/53164", "src_url": "https://doi.org/10.2196/53164"},
                    {"file": "Linardon_2025_Mental-Health-Hallucinations.pdf",
                     "authors": "Linardon, J., et al.", "year": "2025",
                     "title": "Hallucinations in AI-Generated References for Mental Health Literature Reviews",
                     "venue": "JMIR Mental Health 12: e80371",
                     "src_label": "DOI:10.2196/80371", "src_url": "https://doi.org/10.2196/80371"},
                    {"file": "Niimi_2025_Citation-Frequency-Hallucination.pdf",
                     "authors": "Niimi, J.", "year": "2025",
                     "title": "Hallucinations in Bibliographic Recommendation: Citation Frequency as a Proxy for Training Data Redundancy",
                     "src_label": "arXiv:2510.25378", "src_url": "https://arxiv.org/abs/2510.25378"},
                ],
            },
            {"id": "5.5", "title": "Building Your Research Workflow with Claude", "papers": [], "note": "Original workflow content."},
            {"id": "5.6", "title": "Hands-On Activities and Assessment", "papers": [], "note": "Assessment design."},
        ],
        "paywalled": [],
    },
    6: {
        "topic": "AI for Writing, Communication & Research Ideation",
        "tagline": "How AI changes the way we write, think, and generate research ideas",
        "summary": "12 papers across writing cognition, ideation, homogenisation, and scientific integrity. SSRN, SAGE and ScienceDirect items are link-only.",
        "paper_count": 12,
        "sublessons": [
            {
                "id": "6.1", "title": "Writing as Thinking",
                "papers": [
                    {"file": "Kosmyna_2025_Your-Brain-on-ChatGPT.pdf",
                     "authors": "Kosmyna, N., et al.", "year": "2025",
                     "title": "Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task",
                     "venue": "MIT Media Lab",
                     "src_label": "arXiv:2506.08872", "src_url": "https://arxiv.org/abs/2506.08872"},
                    {"file": "Seran_2025_AI-Cognitive-Dissonance.pdf",
                     "authors": "Seran, C. E., Tan, M. J. T., Abdul Karim, H., et al.", "year": "2025",
                     "title": "A conceptual exploration of generative AI-induced cognitive dissonance and its emergence in university-level academic writing",
                     "venue": "Frontiers in AI",
                     "src_label": "DOI:10.3389/frai.2025.1573368", "src_url": "https://doi.org/10.3389/frai.2025.1573368"},
                    {"file": "SanzTejeda_2025_GenAI-Academic-Reading-Writing.pdf",
                     "authors": "Sanz-Tejeda, A., Dom&iacute;nguez-Oller, J. C., Baldaqu&iacute;-Escandell, J. M., & G&oacute;mez-D&iacute;az, R.", "year": "2025",
                     "title": "The impact of generative AI on academic reading and writing: a synthesis of recent evidence (2023&ndash;2025)",
                     "venue": "Frontiers in Education",
                     "src_label": "DOI:10.3389/feduc.2025.1711718", "src_url": "https://doi.org/10.3389/feduc.2025.1711718"},
                ],
            },
            {
                "id": "6.2", "title": "Research Ideation with AI",
                "papers": [
                    {"file": "White_2023_Prompt-Pattern-Catalog.pdf",
                     "authors": "White, J., et al.", "year": "2023",
                     "title": "A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT",
                     "src_label": "arXiv:2302.11382", "src_url": "https://arxiv.org/abs/2302.11382"},
                    {"file": "Sourati_2023_Human-Aware-AI-Science.pdf",
                     "authors": "Sourati, J., & Evans, J. A.", "year": "2023",
                     "title": "Accelerating science with human-aware artificial intelligence",
                     "src_label": "arXiv:2306.01495", "src_url": "https://arxiv.org/abs/2306.01495"},
                    {"file": "Meincke_2024_Prompting-Diverse-Ideas.pdf",
                     "authors": "Meincke, L., Mollick, E., & Terwiesch, C.", "year": "2024",
                     "title": "Prompting Diverse Ideas: Increasing AI Idea Variance",
                     "src_label": "arXiv:2402.01727", "src_url": "https://arxiv.org/abs/2402.01727"},
                    {"file": "Si_2024_LLM-Novel-Ideas.pdf",
                     "authors": "Si, C., Yang, D., & Hashimoto, T.", "year": "2024",
                     "title": "Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers",
                     "src_label": "arXiv:2409.04109", "src_url": "https://arxiv.org/abs/2409.04109"},
                    {"file": "Lu_2024_AI-Scientist.pdf",
                     "authors": "Lu, C., Lu, C., Lange, R. T., et al.", "year": "2024",
                     "title": "The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery",
                     "venue": "Sakana AI; Nature 2026",
                     "src_label": "arXiv:2408.06292", "src_url": "https://arxiv.org/abs/2408.06292"},
                    {"file": "Traberg_2026_AI-Scientific-Monoculture.pdf",
                     "authors": "Traberg, C. S., Roozenbeek, J., & van der Linden, S.", "year": "2026",
                     "title": "AI is turning research into a scientific monoculture",
                     "venue": "Communications Psychology",
                     "src_label": "DOI:10.1038/s44271-026-00428-5", "src_url": "https://doi.org/10.1038/s44271-026-00428-5"},
                ],
            },
            {
                "id": "6.3", "title": "AI Writing Tools &mdash; Landscape and Honest Assessment",
                "papers": [
                    {"file": "Amano_2025_Multilingual-Publishing-PLOS.pdf",
                     "authors": "Amano, T., Bowker, M., & Burton-Jones, A.", "year": "2025",
                     "title": "Two futures for multilingual scientific publishing in the age of AI",
                     "venue": "PLOS Biology",
                     "src_label": "DOI:10.1371/journal.pbio.3003215", "src_url": "https://doi.org/10.1371/journal.pbio.3003215"},
                    {"file": "Agarwal_2024_AI-Homogenize-Writing.pdf",
                     "authors": "Agarwal, D., Naaman, M., & Vashistha, A.", "year": "2024",
                     "title": "AI Suggestions Homogenize Writing Toward Western Styles and Diminish Cultural Nuances",
                     "venue": "CHI 2025",
                     "src_label": "arXiv:2409.11360", "src_url": "https://arxiv.org/abs/2409.11360"},
                ],
            },
            {
                "id": "6.4", "title": "Scientific Integrity and the Writing Pipeline",
                "papers": [
                    {"file": "Pellegrina_2025_AI-Scientific-Integrity.pdf",
                     "authors": "Pellegrina, D., Helmy, M., et al.", "year": "2025",
                     "title": "AI for scientific integrity: detecting ethical breaches, errors, and misconduct in manuscripts",
                     "venue": "Frontiers in AI",
                     "src_label": "DOI:10.3389/frai.2025.1644098", "src_url": "https://doi.org/10.3389/frai.2025.1644098"},
                ],
            },
            {"id": "6.5", "title": "Building Your AI Writing Workflow", "papers": [], "note": "Original workflow content."},
            {"id": "6.6", "title": "Hands-On Activities and Assessment", "papers": [], "note": "Assessment design."},
            {"id": "6.7", "title": "Using AI to Review Your Own Work (supplementary)", "papers": [], "note": "Based on the paper-review skill."},
        ],
        "paywalled": [
            {"citation": "Girotra, K., Meincke, L., Terwiesch, C., & Ulrich, K. (2023). Quantity vs. Quality: Comparing the Idea Generation Capabilities of LLMs and Humans.",
             "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4526071", "url_label": "SSRN:4526071",
             "sublesson": "6.2",
             "note": "SSRN protects downloads with Cloudflare; sign in to SSRN to download."},
            {"citation": "Usdan, S., Connell Pensky, A., & Chang, R. (2024). Effects of structured AI writing instruction at Carnegie Mellon.",
             "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4941022", "url_label": "SSRN:4941022",
             "sublesson": "6.3", "note": "Same SSRN bot-protection."},
            {"citation": "Daryani, S., et al. (2026). The Homogenizing Engine: AI&rsquo;s Role in Standardizing Culture. <em>SAGE Journals</em>.",
             "url": "https://journals.sagepub.com/doi/10.1177/23727322251406591", "url_label": "DOI:10.1177/23727322251406591",
             "sublesson": "6.2, 6.3",
             "note": "SAGE paywalled; UCT library has SAGE access."},
            {"citation": "Holmner, M., et al. (2025). The Future of Academic Writing in the Age of Generative AI. <em>JASIST</em>.",
             "url": "", "url_label": "Wiley/ASIS&T",
             "sublesson": "6.1", "note": "Wiley paywalled; UCT library access."},
        ],
    },
    7: {
        "topic": "AI for Data, Code & Computation",
        "tagline": "Code generation, data analysis, visualization, verification, and agentic workflows",
        "summary": "6 papers downloaded across the literature on LLMs as data analysts, the data-leakage crisis, visualization, and the safety profile of agentic AI for science.",
        "paper_count": 6,
        "sublessons": [
            {
                "id": "7.1", "title": "Natural Language to Code",
                "papers": [
                    {"file": "Cheng_2023_GPT-4-Data-Analyst.pdf",
                     "authors": "Cheng, L., Li, X., & Bing, L.", "year": "2023",
                     "title": "Is GPT-4 a Good Data Analyst?",
                     "src_label": "arXiv:2305.15038", "src_url": "https://arxiv.org/abs/2305.15038"},
                    {"file": "Hong_2024_Data-Interpreter.pdf",
                     "authors": "Hong, S., Lin, Y., Liu, B., et al.", "year": "2024",
                     "title": "Data Interpreter: An LLM Agent for Data Science",
                     "src_label": "arXiv:2402.18679", "src_url": "https://arxiv.org/abs/2402.18679"},
                ],
            },
            {
                "id": "7.2", "title": "AI-Assisted Data Analysis in Practice",
                "papers": [
                    {"file": "Kapoor_2023_Leakage-Reproducibility-Crisis.pdf",
                     "authors": "Kapoor, S., & Narayanan, A.", "year": "2023",
                     "title": "Leakage and the Reproducibility Crisis in ML-based Science",
                     "venue": "Patterns 4(9): 100804",
                     "src_label": "arXiv:2207.07048", "src_url": "https://arxiv.org/abs/2207.07048"},
                ],
            },
            {
                "id": "7.3", "title": "Visualization with AI",
                "papers": [
                    {"file": "Dibia_2023_LIDA.pdf",
                     "authors": "Dibia, V.", "year": "2023",
                     "title": "LIDA: A Tool for Automatic Generation of Grammar-Agnostic Visualizations and Infographics using Large Language Models",
                     "venue": "ACL System Demos",
                     "src_label": "arXiv:2303.02927", "src_url": "https://arxiv.org/abs/2303.02927"},
                ],
            },
            {"id": "7.4", "title": "Verification of AI-Generated Code", "papers": [],
             "note": "Re-uses Kapoor &amp; Narayanan (above) as the central reading."},
            {"id": "7.5", "title": "Building Your Data Analysis Workflow", "papers": [],
             "note": "References Mineault (2026) <em>Claude Code for Scientists</em> &mdash; a Substack post, linked in the lesson."},
            {
                "id": "7.6", "title": "Agentic Data Analysis",
                "papers": [
                    {"file": "Gridach_2025_Agentic-AI-Scientific-Discovery.pdf",
                     "authors": "Gridach, M., Nanavati, J., Abidine, K. Z. E., et al.", "year": "2025",
                     "title": "Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions",
                     "src_label": "arXiv:2503.08979", "src_url": "https://arxiv.org/abs/2503.08979"},
                    {"file": "Zardiashvili_2025_Risks-AI-Scientists.pdf",
                     "authors": "Zardiashvili, L., et al.", "year": "2025",
                     "title": "Risks of AI scientists: prioritizing safeguarding over autonomy",
                     "venue": "Nature Communications",
                     "src_label": "DOI:10.1038/s41467-025-63913-1", "src_url": "https://doi.org/10.1038/s41467-025-63913-1"},
                ],
            },
            {"id": "7.7", "title": "Hands-On Activities and Assessment", "papers": [], "note": "Assessment design."},
        ],
        "paywalled": [
            {"citation": "<em>Nature</em> (2026). AI scientists are changing research &mdash; institutions must respond.",
             "url": "https://doi.org/10.1038/d41586-026-00934-w", "url_label": "DOI:10.1038/d41586-026-00934-w",
             "sublesson": "7.6",
             "note": "Nature editorial &mdash; free to read on Nature.com but no redistributable PDF endpoint."},
        ],
        "extra_html": """
            <p>Other Week 7 references are practitioner resources rather than papers:</p>
            <ul class="styled-list">
                <li>Mineault, P. (2026). <em>Claude Code for Scientists.</em> <a href="https://www.neuroai.science/p/claude-code-for-scientists" target="_blank" rel="noopener">neuroai.science</a></li>
                <li>Wickham, H., &Ccedil;etinkaya-Rundel, M., &amp; Grolemund, G. (2023). <em>R for Data Science (2e).</em> <a href="https://r4ds.hadley.nz" target="_blank" rel="noopener">r4ds.hadley.nz</a></li>
                <li>Wilke, C. (2019). <em>Fundamentals of Data Visualization.</em> <a href="https://clauswilke.com/dataviz" target="_blank" rel="noopener">clauswilke.com/dataviz</a></li>
            </ul>
        """,
    },
    8: {
        "topic": "Multimodal AI for Research",
        "tagline": "Vision, documents, audio, and video &mdash; what AI can really do across modalities",
        "summary": "10 papers covering chart understanding, VLM blind spots, scientific images, document OCR, transcription benchmarks, and long-context behaviour. Two references (ACM FAccT, SSRN) are link-only.",
        "paper_count": 10,
        "sublessons": [
            {
                "id": "8.1", "title": "What Multimodal AI Can See, Hear, and Read",
                "papers": [
                    {"file": "Wang_2024_CharXiv.pdf",
                     "authors": "Wang, Z., et al.", "year": "2024",
                     "title": "CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs",
                     "src_label": "arXiv:2406.18521", "src_url": "https://arxiv.org/abs/2406.18521"},
                    {"file": "Rahmanzadehgervi_2024_VLMs-Are-Blind.pdf",
                     "authors": "Rahmanzadehgervi, P., et al.", "year": "2024",
                     "title": "Vision Language Models Are Blind: Failing to Translate Detailed Visual Features into Words",
                     "venue": "ACCV 2024",
                     "src_label": "arXiv:2407.06581", "src_url": "https://arxiv.org/abs/2407.06581"},
                ],
            },
            {
                "id": "8.2", "title": "AI and Scientific Images",
                "papers": [
                    {"file": "Jin_2024_GPT-4V-Medical.pdf",
                     "authors": "Jin, Q., et al.", "year": "2024",
                     "title": "Hidden flaws behind expert-level accuracy of multimodal GPT-4 vision in medicine",
                     "venue": "npj Digital Medicine",
                     "src_label": "DOI:10.1038/s41746-024-01185-7", "src_url": "https://doi.org/10.1038/s41746-024-01185-7"},
                    {"file": "Mujahid_2024_Malaria-Detection.pdf",
                     "authors": "Mujahid, M., et al.", "year": "2024",
                     "title": "Efficient deep learning-based approach for malaria detection",
                     "venue": "Scientific Reports",
                     "src_label": "DOI:10.1038/s41598-024-63831-0", "src_url": "https://doi.org/10.1038/s41598-024-63831-0"},
                ],
            },
            {
                "id": "8.3", "title": "Document Intelligence",
                "papers": [
                    {"file": "Crosilla_2025_Handwritten-Text-Recognition.pdf",
                     "authors": "Crosilla, G., Klic, L., & Colavizza, G.", "year": "2025",
                     "title": "Benchmarking Large Language Models for Handwritten Text Recognition",
                     "src_label": "arXiv:2503.15195", "src_url": "https://arxiv.org/abs/2503.15195"},
                    {"file": "Poznanski_2025_olmOCR-2.pdf",
                     "authors": "Poznanski, J., Soldaini, L., et al.", "year": "2025",
                     "title": "olmOCR 2: Unit Test Rewards for Document OCR",
                     "src_label": "arXiv:2510.19817", "src_url": "https://arxiv.org/abs/2510.19817"},
                ],
            },
            {
                "id": "8.4", "title": "Transcription and Audio Analysis",
                "papers": [
                    {"file": "Imam_2025_African-ASR-Survey.pdf",
                     "authors": "Imam, S. H., Belay, T. D., et al.", "year": "2025",
                     "title": "Automatic Speech Recognition (ASR) for African Low-Resource Languages: A Systematic Literature Review",
                     "src_label": "arXiv:2510.01145", "src_url": "https://arxiv.org/abs/2510.01145"},
                    {"file": "Nahabwe_2025_African-ASR-Benchmark.pdf",
                     "authors": "Nahabwe, A., Kagumire, S., et al.", "year": "2025",
                     "title": "Benchmarking Automatic Speech Recognition Models for African Languages",
                     "venue": "Deep Learning Indaba 2025",
                     "src_label": "arXiv:2512.10968", "src_url": "https://arxiv.org/abs/2512.10968"},
                ],
            },
            {
                "id": "8.5", "title": "Video and Multimodal Workflows",
                "papers": [
                    {"file": "Liu_2024_Lost-in-the-Middle.pdf",
                     "authors": "Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P.", "year": "2024",
                     "title": "Lost in the Middle: How Language Models Use Long Contexts",
                     "venue": "TACL 2024",
                     "src_label": "arXiv:2307.03172", "src_url": "https://arxiv.org/abs/2307.03172"},
                ],
            },
            {
                "id": "8.6", "title": "Hands-On Activities and Assessment",
                "papers": [
                    {"file": "COPCOV_2024_PLOS-Medicine.pdf",
                     "authors": "COPCOV Investigators", "year": "2024",
                     "title": "Hydroxychloroquine and chloroquine prophylaxis for COVID-19",
                     "venue": "PLOS Medicine &mdash; activity 3 source paper",
                     "src_label": "DOI:10.1371/journal.pmed.1004428", "src_url": "https://doi.org/10.1371/journal.pmed.1004428"},
                ],
            },
        ],
        "paywalled": [
            {"citation": "Koenecke, A., et al. (2024). Careless Whisper: Speech-to-Text Hallucination Harms. <em>FAccT &rsquo;24</em>.",
             "url": "https://doi.org/10.1145/3630106.3658975", "url_label": "DOI:10.1145/3630106.3658975",
             "sublesson": "8.4",
             "note": "ACM Digital Library doesn&rsquo;t expose a public PDF endpoint; click through or use ACM Open Access."},
            {"citation": "Friese, S. (2025). From Coding to Conversation: A New Methodological Framework for AI-Assisted Qualitative Analysis.",
             "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5232579", "url_label": "SSRN:5232579",
             "sublesson": "8.4", "note": "SSRN bot-protected."},
        ],
    },
    9: {
        "topic": "Critical Evaluation & Limitations of AI",
        "tagline": "Benchmarks, failure categories, and where AI is now genuinely strong",
        "summary": "15 papers spanning benchmark contamination, structural failure modes (the reversal curse, sycophancy, hallucination), and recent cases of AI contributing to genuine mathematical and physical discovery.",
        "paper_count": 15,
        "sublessons": [
            {
                "id": "9.1", "title": "The Trajectory of LLM Capabilities",
                "papers": [
                    {"authors": "Deng, C., Zhao, Y., Tang, X., Gerstein, M., & Cohan, A.", "year": "2023",
                     "title": "Investigating Data Contamination in Modern Benchmarks for Large Language Models",
                     "venue": "NAACL 2024",
                     "src_label": "arXiv:2311.09783", "src_url": "https://arxiv.org/abs/2311.09783"},
                    {"authors": "", "year": "2023",
                     "title": "LatestEval &mdash; dynamic test construction to avoid data contamination",
                     "venue": "AAAI 2024",
                     "src_label": "arXiv:2312.12343", "src_url": "https://arxiv.org/abs/2312.12343"},
                    {"authors": "Alhanai, T., Kasumovic, M., Ghassemi, M., Zitzelberger, R., Lundin, E., &amp; Chabot-Couture, G.", "year": "2024",
                     "title": "Bridging the Gap &mdash; measuring the real-world capability gap",
                     "venue": "AAAI 2025",
                     "src_label": "arXiv:2412.12417", "src_url": "https://arxiv.org/abs/2412.12417"},
                    {"authors": "", "year": "2024",
                     "title": "IrokoBench: a benchmark for African languages",
                     "src_label": "arXiv:2406.03368", "src_url": "https://arxiv.org/abs/2406.03368"},
                    {"authors": "", "year": "2026",
                     "title": "ProgramBench: Can Language Models Rebuild Programs From Scratch?",
                     "venue": "arXiv, May 2026",
                     "src_label": "arXiv:2605.03546", "src_url": "https://arxiv.org/abs/2605.03546"},
                ],
            },
            {
                "id": "9.2", "title": "Three Categories of Failure",
                "papers": [
                    {"authors": "Berglund, L., Tong, M., Kaufmann, M., et al.", "year": "2023",
                     "title": "The Reversal Curse: LLMs Trained on &ldquo;A is B&rdquo; Fail to Learn &ldquo;B is A&rdquo;",
                     "src_label": "arXiv:2309.12288", "src_url": "https://arxiv.org/abs/2309.12288"},
                    {"authors": "Frieder, S., Pinchetti, L., et al.", "year": "2023",
                     "title": "Mathematical Capabilities of ChatGPT",
                     "venue": "NeurIPS 2023",
                     "src_label": "arXiv:2301.13867", "src_url": "https://arxiv.org/abs/2301.13867"},
                    {"authors": "Sharma, M., Tong, M., Korbak, T., et al.", "year": "2023",
                     "title": "Towards Understanding Sycophancy in Language Models",
                     "venue": "ICLR 2024",
                     "src_label": "arXiv:2310.13548", "src_url": "https://arxiv.org/abs/2310.13548"},
                    {"authors": "Kalai, A. T., Nachum, O., Vempala, S. S., &amp; Zhang, E.", "year": "2025",
                     "title": "Why Language Models Hallucinate",
                     "src_label": "arXiv:2509.04664", "src_url": "https://arxiv.org/abs/2509.04664"},
                ],
            },
            {
                "id": "9.3", "title": "Where AI Is Now Genuinely Strong",
                "papers": [
                    {"authors": "Fang, Y.-L., Jian, D.-S., Li, X., &amp; Ma, Y.-Q.", "year": "2025",
                     "title": "AI-Newton: A Concept-Driven Physical Law Discovery System without Prior Physical Knowledge",
                     "src_label": "arXiv:2504.01538", "src_url": "https://arxiv.org/abs/2504.01538"},
                    {"authors": "Georgiev, B., G&oacute;mez-Serrano, J., Tao, T., &amp; Wagner, A. Z.", "year": "2025",
                     "title": "Mathematical exploration and discovery at scale",
                     "src_label": "arXiv:2511.02864", "src_url": "https://arxiv.org/abs/2511.02864"},
                    {"authors": "Guevara, A., Lupsasca, A., Skinner, D., Strominger, A., &amp; Weil, K.", "year": "2026",
                     "title": "Single-minus gluon tree amplitudes",
                     "venue": "AI-assisted amplitude calculation",
                     "src_label": "arXiv:2602.12176", "src_url": "https://arxiv.org/abs/2602.12176"},
                    {"authors": "Brenner, M. P., Cohen-Addad, V., &amp; Woodruff, D.", "year": "2026",
                     "title": "Solving an Open Problem in Theoretical Physics using AI",
                     "src_label": "arXiv:2603.04735", "src_url": "https://arxiv.org/abs/2603.04735"},
                    {"authors": "Alexeev, B., Barreto, K., Li, Y., Lichtman, J. D., Price, L., Shah, J. I., Tang, Q., &amp; Tao, T.", "year": "2026",
                     "title": "Primitive sets &mdash; a number-theory problem solved with AI assistance",
                     "src_label": "arXiv:2605.00301", "src_url": "https://arxiv.org/abs/2605.00301"},
                    {"authors": "", "year": "2026",
                     "title": "AI Co-Mathematician: Accelerating Mathematicians with Agentic AI",
                     "venue": "arXiv, May 2026",
                     "src_label": "arXiv:2605.06651", "src_url": "https://arxiv.org/abs/2605.06651"},
                ],
            },
            {"id": "9.4", "title": "Illusions of Understanding", "papers": [],
             "note": "Conceptual sub-lesson &mdash; draws on the failure-mode papers above rather than introducing new primary literature."},
            {"id": "9.5", "title": "Verification Protocols for a Moving Target", "papers": [],
             "note": "Original protocol/workflow content."},
            {"id": "9.6", "title": "Hands-On Activities and Assessment", "papers": [], "note": "Assessment design."},
        ],
        "paywalled": [],
    },
    10: {
        "topic": "Agentic AI, RAG & Advanced Research Tools",
        "tagline": "Harnesses, long-horizon reliability, MCP, agentic RAG, and the 2026 tool landscape",
        "summary": "12 papers covering harness optimisation, agent benchmarks, the reliability-vs-accuracy distinction, long-horizon planning collapse, agentic RAG, and RAG evaluation.",
        "paper_count": 12,
        "sublessons": [
            {
                "id": "10.1", "title": "What Agents Are and What's New in 2026",
                "papers": [
                    {"authors": "Lee, Y., et al.", "year": "2026",
                     "title": "Meta-Harness: End-to-End Optimization of Model Harnesses",
                     "src_label": "arXiv:2603.28052", "src_url": "https://arxiv.org/abs/2603.28052"},
                    {"authors": "", "year": "2026",
                     "title": "Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command-Line Interfaces",
                     "src_label": "arXiv:2601.11868", "src_url": "https://arxiv.org/abs/2601.11868"},
                ],
            },
            {
                "id": "10.2", "title": "Failure Modes for Long-Horizon Tasks",
                "papers": [
                    {"authors": "Rabanser, S., Kapoor, S., Kirgis, P., Liu, K., Utpala, S., &amp; Narayanan, A.", "year": "2026",
                     "title": "Towards a Science of AI Agent Reliability",
                     "venue": "Princeton CITP",
                     "src_label": "arXiv:2602.16666", "src_url": "https://arxiv.org/abs/2602.16666"},
                    {"authors": "Wang, Z., et al.", "year": "2026",
                     "title": "Why Reasoning Fails to Plan: A Planning-Centric Analysis of Long-Horizon Decision Making in LLM Agents",
                     "src_label": "arXiv:2601.22311", "src_url": "https://arxiv.org/abs/2601.22311"},
                    {"authors": "", "year": "2026",
                     "title": "YC-Bench: Benchmarking AI Agents for Long-Term Planning and Consistent Execution",
                     "src_label": "arXiv:2604.01212", "src_url": "https://arxiv.org/abs/2604.01212"},
                    {"authors": "", "year": "2026",
                     "title": "Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents",
                     "src_label": "arXiv:2603.29231", "src_url": "https://arxiv.org/abs/2603.29231"},
                    {"authors": "Kalai, A. T., Nachum, O., Vempala, S. S., &amp; Zhang, E.", "year": "2025",
                     "title": "Why Language Models Hallucinate",
                     "venue": "also cited in Week 9",
                     "src_label": "arXiv:2509.04664", "src_url": "https://arxiv.org/abs/2509.04664"},
                ],
            },
            {
                "id": "10.3", "title": "The Current Tool Landscape and MCP",
                "papers": [
                    {"authors": "Sakana AI", "year": "2025",
                     "title": "The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search",
                     "src_label": "arXiv:2504.08066", "src_url": "https://arxiv.org/abs/2504.08066"},
                ],
            },
            {
                "id": "10.4", "title": "RAG in 2026",
                "papers": [
                    {"authors": "Singh, A., Ehtesham, A., Kumar, S., Talaei Khoei, T., &amp; Vasilakos, A. V.", "year": "2025",
                     "title": "Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG",
                     "src_label": "arXiv:2501.09136", "src_url": "https://arxiv.org/abs/2501.09136"},
                    {"authors": "Li, Z., Li, C., Zhang, M., Mei, Q., &amp; Bendersky, M.", "year": "2024",
                     "title": "Retrieval Augmented Generation or Long-Context LLMs? A Comprehensive Study and Hybrid Approach",
                     "venue": "Google; EMNLP 2024",
                     "src_label": "arXiv:2407.16833", "src_url": "https://arxiv.org/abs/2407.16833"},
                    {"authors": "Es, S., James, J., Espinosa-Anke, L., &amp; Schockaert, S.", "year": "2023",
                     "title": "RAGAS: Automated Evaluation of Retrieval Augmented Generation",
                     "src_label": "arXiv:2309.15217", "src_url": "https://arxiv.org/abs/2309.15217"},
                ],
            },
            {
                "id": "10.5", "title": "Advanced Research Tools &mdash; A Curated Tour",
                "papers": [
                    {"authors": "Rajab, J., Aremu, A., Chimoto, E. A., et al.", "year": "2025",
                     "title": "The Esethu Framework: Reimagining Sustainable Dataset Governance and Curation for Low-Resource Languages",
                     "venue": "also cited in Week 4",
                     "src_label": "arXiv:2502.15916", "src_url": "https://arxiv.org/abs/2502.15916"},
                ],
            },
            {"id": "10.6", "title": "Hands-On Activities and Assessment", "papers": [], "note": "Assessment design (the &ldquo;Same Task, Three Ways&rdquo; activity)."},
        ],
        "paywalled": [],
    },
}

# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------

CSS = """
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
        font-family: 'Lato', sans-serif;
        line-height: 1.6;
        color: #2c3e50;
        background: #f5f5f5;
        padding: 20px;
    }
    .container {
        max-width: 1000px;
        margin: 0 auto;
        background: white;
        border-radius: 20px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        overflow: hidden;
    }
    .back-bar {
        background: #f0f4f8;
        padding: 12px 30px;
        border-bottom: 1px solid #e0e0e0;
    }
    .back-bar a {
        color: #003A70;
        text-decoration: none;
        font-size: 0.9em;
        font-weight: 600;
    }
    .back-bar a:hover { text-decoration: underline; }
    header {
        background: #003A70;
        color: white;
        padding: 50px 40px;
        text-align: center;
    }
    header h1 {
        font-size: 2.3em;
        margin-bottom: 10px;
        font-weight: 300;
        letter-spacing: 1px;
    }
    header p {
        font-size: 1.1em;
        opacity: 0.9;
        max-width: 700px;
        margin: 10px auto 0;
    }
    .week-pill {
        display: inline-block;
        background: rgba(255,255,255,0.2);
        padding: 6px 18px;
        border-radius: 20px;
        font-size: 0.9em;
        margin-bottom: 15px;
        backdrop-filter: blur(10px);
    }
    .content { padding: 50px 40px; }
    .intro-text {
        background: #f9f9f9;
        padding: 25px 30px;
        border-radius: 12px;
        border-left: 5px solid #003A70;
        margin-bottom: 40px;
    }
    .intro-text p { color: #444; line-height: 1.8; margin-bottom: 10px; }
    .intro-text p:last-child { margin-bottom: 0; }
    .section { margin-bottom: 45px; }
    .section-title {
        color: #2a5298;
        font-size: 1.4em;
        font-weight: 600;
        margin-bottom: 6px;
        padding-bottom: 8px;
        border-bottom: 2px solid #003A70;
    }
    .section-subtitle { color: #888; font-size: 0.9em; margin-bottom: 18px; font-style: italic; }
    .section p { color: #444; line-height: 1.8; margin-bottom: 14px; }
    .section a { color: #003A70; font-weight: 600; }
    .paper-card {
        background: white;
        border: 1px solid #e0e6ed;
        border-left: 5px solid #003A70;
        border-radius: 10px;
        padding: 18px 22px;
        margin-bottom: 16px;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .paper-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(0, 58, 112, 0.08);
    }
    .paper-title { color: #2a5298; font-weight: 600; font-size: 1.05em; margin-bottom: 4px; line-height: 1.4; }
    .paper-meta { color: #666; font-size: 0.9em; margin-bottom: 10px; }
    .paper-meta em { color: #555; }
    .paper-actions { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; margin-top: 8px; }
    .download-btn {
        display: inline-block;
        background: #003A70;
        color: white !important;
        padding: 7px 16px;
        border-radius: 6px;
        text-decoration: none !important;
        font-size: 0.88em;
        font-weight: 600;
        transition: background 0.15s ease;
    }
    .download-btn:hover { background: #002550; }
    .source-link {
        color: #003A70 !important;
        font-size: 0.88em;
        text-decoration: none !important;
        font-weight: 600;
        padding: 7px 14px;
        border: 1px solid #003A70;
        border-radius: 6px;
    }
    .source-link:hover { background: #f0f4f8; }
    .empty-note {
        color: #888;
        font-style: italic;
        margin: 8px 0 4px;
    }
    .styled-list { list-style: none; padding-left: 0; margin: 12px 0 14px; }
    .styled-list li {
        position: relative;
        padding-left: 22px;
        margin-bottom: 8px;
        color: #444;
        line-height: 1.7;
    }
    .styled-list li::before {
        content: '\\25B8';
        position: absolute;
        left: 0;
        color: #003A70;
        font-weight: 700;
    }
    .paywalled-section {
        background: #fff8e1;
        border-left: 5px solid #f9a825;
        padding: 20px 25px;
        border-radius: 10px;
        margin-top: 30px;
    }
    .paywalled-section h3 {
        color: #b86400;
        font-size: 1.1em;
        margin-bottom: 12px;
    }
    .paywalled-item {
        margin-bottom: 14px;
        padding-bottom: 14px;
        border-bottom: 1px solid #f0e0b0;
    }
    .paywalled-item:last-child {
        margin-bottom: 0;
        padding-bottom: 0;
        border-bottom: none;
    }
    .paywalled-item .citation { color: #444; font-size: 0.95em; line-height: 1.6; }
    .paywalled-item .access { color: #777; font-size: 0.85em; line-height: 1.6; margin-top: 6px; }
    .paywalled-item .access a { color: #003A70; }
    .paywalled-item .sublesson-tag {
        display: inline-block;
        background: rgba(0, 58, 112, 0.08);
        color: #003A70;
        padding: 2px 10px;
        border-radius: 12px;
        font-size: 0.78em;
        margin-left: 6px;
        font-weight: 600;
    }
    /* Index page */
    .week-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 18px;
    }
    .week-card {
        background: white;
        border: 1px solid #e0e6ed;
        border-radius: 12px;
        padding: 22px;
        text-decoration: none;
        color: inherit;
        transition: transform 0.15s ease, box-shadow 0.15s ease, border-color 0.15s ease;
        display: block;
    }
    .week-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 22px rgba(0, 58, 112, 0.12);
        border-color: #003A70;
    }
    .week-card.empty { opacity: 0.7; }
    .week-card .num {
        display: inline-block;
        background: #003A70;
        color: white;
        width: 36px;
        height: 36px;
        line-height: 36px;
        text-align: center;
        border-radius: 50%;
        font-weight: 700;
        margin-right: 12px;
    }
    .week-card .topic {
        color: #2a5298;
        font-weight: 600;
        font-size: 1.05em;
        margin-bottom: 8px;
        line-height: 1.3;
    }
    .week-card .count {
        background: #003A70;
        color: white;
        font-size: 0.78em;
        padding: 2px 10px;
        border-radius: 10px;
        font-weight: 600;
    }
    .week-card.empty .count { background: #aaa; }
    .week-card p { color: #555; font-size: 0.9em; line-height: 1.55; margin-top: 10px; }
    footer {
        background: #f9f9f9;
        padding: 22px 30px;
        text-align: center;
        color: #888;
        font-size: 0.85em;
        border-top: 1px solid #eee;
        font-family: 'Lato', sans-serif;
    }
    footer a { color: #003A70; }
    @media (max-width: 768px) {
        header h1 { font-size: 1.6em; }
        .content { padding: 30px 20px; }
    }
"""

PAGE_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="https://s.brightspace.com/lib/fonts/0.6.1/fonts.css">
    <style>{css}</style>
</head>
<body>
<div class="container">
    <div class="back-bar">{back_links}</div>
"""

PAGE_FOOT = """    <footer>
        &copy; 2026 Jonathan Shock &middot; MAM5020F: Generative AI for Research &middot; Licensed under <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">CC&nbsp;BY&nbsp;4.0</a>
        <p style="margin-top: 8px;">Each reference links to its canonical source. The papers themselves remain under their original licences and copyright holders.</p>
    </footer>
</div>
</body>
</html>
"""


def render_paper_card(p, week_num=None):
    """Render a single paper card (link-only — points to the canonical source)."""
    venue = f" &mdash; <em>{p['venue']}</em>" if p.get("venue") else ""
    meta = f"{p['authors']} ({p['year']})" if p.get("authors") else f"({p['year']})"
    return f"""
    <div class="paper-card">
        <div class="paper-title">{p['title']}</div>
        <div class="paper-meta">{meta}{venue}</div>
        <div class="paper-actions">
            <a class="source-link" href="{p['src_url']}" target="_blank" rel="noopener">View source &middot; {p['src_label']}</a>
        </div>
    </div>"""


def render_paywalled(items):
    if not items:
        return ""
    rows = []
    for it in items:
        url_html = (
            f'<a href="{it["url"]}" target="_blank" rel="noopener">{it["url_label"]}</a>'
            if it.get("url") else f'<em>{it["url_label"]}</em>'
        )
        rows.append(f"""
        <div class="paywalled-item">
            <div class="citation">{it['citation']} {url_html} <span class="sublesson-tag">{it['sublesson']}</span></div>
            <div class="access">{it['note']}</div>
        </div>""")
    return f"""
    <div class="paywalled-section">
        <h3>Linked but not redistributed</h3>
        {''.join(rows)}
    </div>"""


def render_week_page(num, w):
    title = f"Week {num} Papers &mdash; {w['topic']}"
    back_links = (
        '<a href="../index.html">&larr; Back to Course Contents</a>'
        ' &middot; '
        '<a href="index.html">&larr; All Papers</a>'
    )
    sublessons_html = []
    for sl in w["sublessons"]:
        if sl["papers"]:
            cards = "\n".join(render_paper_card(p, num) for p in sl["papers"])
            sublessons_html.append(f"""
        <div class="section">
            <h2 class="section-title">{sl['id']} &middot; {sl['title']}</h2>
            {cards}
        </div>""")
        else:
            note = sl.get("note", "")
            sublessons_html.append(f"""
        <div class="section">
            <h2 class="section-title">{sl['id']} &middot; {sl['title']}</h2>
            <p class="empty-note">{note}</p>
        </div>""")

    paywalled_html = render_paywalled(w.get("paywalled", []))
    extra_html = w.get("extra_html", "")

    body = f"""
    <header>
        <div class="week-pill">Week {num}</div>
        <h1><span style="color:#fff;">{w['topic']}</span></h1>
        <p>{w['tagline']}</p>
    </header>
    <div class="content">
        <div class="intro-text">
            <p>{w['summary']}</p>
            <p style="margin-top:8px; color:#666; font-size:0.92em;">Each entry links to the canonical version of the paper &mdash; on arXiv, the journal, or the publisher. Where a paper is paywalled, the DOI is given for UCT-library access.</p>
        </div>
        {''.join(sublessons_html)}
        {extra_html}
        {paywalled_html}
    </div>
"""

    return (
        PAGE_HEAD.format(title=title, css=CSS, back_links=back_links)
        + body
        + PAGE_FOOT
    )


def render_index_page():
    title = "Course Papers &mdash; MAM5020F 2026"
    back_links = '<a href="../index.html">&larr; Back to Course Contents</a>'
    cards = []
    for num in sorted(WEEKS.keys()):
        w = WEEKS[num]
        count = w["paper_count"]
        empty_class = " empty" if count == 0 else ""
        count_html = (
            f'<span class="count">{count} paper{"s" if count != 1 else ""}</span>'
            if count else '<span class="count">no papers</span>'
        )
        cards.append(f"""
        <a class="week-card{empty_class}" href="week-{num}.html">
            <div style="display:flex; align-items:center; justify-content:space-between; gap:10px;">
                <div style="display:flex; align-items:center;"><span class="num">{num}</span></div>
                {count_html}
            </div>
            <div class="topic" style="margin-top:12px;">{w['topic']}</div>
            <p>{w['tagline']}</p>
        </a>""")

    body = f"""
    <header>
        <h1><span style="color:#fff;">Course Papers</span></h1>
        <p>Every academic paper cited across the 12-week course, grouped by week. Each entry links to the canonical source &mdash; arXiv, journal DOI, or publisher.</p>
    </header>
    <div class="content">
        <div class="intro-text">
            <p>One card per paper, each linking to the canonical source (arXiv, journal DOI, or publisher). Where a paper is paywalled, the DOI is given so you can reach it through the UCT library.</p>
            <p style="margin-top:8px; color:#666; font-size:0.92em;">We link to papers rather than hosting copies, so each one stays at its authoritative version. The course materials themselves (lesson HTML and the rest of this site) are <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">CC&nbsp;BY&nbsp;4.0</a>; that licence does not extend to the linked third-party papers.</p>
        </div>
        <div class="week-grid">
            {''.join(cards)}
        </div>
    </div>
"""

    return (
        PAGE_HEAD.format(title=title, css=CSS, back_links=back_links)
        + body
        + PAGE_FOOT
    )


def main():
    os.makedirs(DOCS_PAPERS, exist_ok=True)

    # Index
    idx_path = os.path.join(DOCS_PAPERS, "index.html")
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(render_index_page())
    print(f"wrote {idx_path}")

    # Weeks
    for num in sorted(WEEKS.keys()):
        path = os.path.join(DOCS_PAPERS, f"week-{num}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(render_week_page(num, WEEKS[num]))
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
