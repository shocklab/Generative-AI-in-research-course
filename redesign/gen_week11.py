#!/usr/bin/env python3
import diagrams as D
from genlib import main

FUT = "content/week-11/What the Future of AI in Research Might Look Like.html"
SOV = "content/week-11/Sovereign AI Capacity and Why Compute Is the Floor.html"
DAT = "content/week-11/Data Languages and African Model-Building.html"
POL = "content/week-11/Policy Institutions and Talent.html"

FIGS = [
    dict(fid="fig-w11-real-overclaimed", page=FUT, loc=r'Real / Overclaimed / Aspirational', mode="after_p",
         cap="A working filter for AI-in-science claims: what's real and shipping, what's overclaimed in the retelling, and what's still aspirational.",
         svg=D.columns([
             dict(title="Real", kind='good', lines=["Already shipping now", "Verifiable, in use", "lit search, coding, ASR"]),
             dict(title="Overclaimed", kind='warn', lines=["Rounded up in the retelling", "Real core, inflated claim", "e.g. 'AI scientist' hype"]),
             dict(title="Aspirational", kind='alt', lines=["Not happening yet", "Plausible but unproven", "e.g. autonomous discovery"]),
         ], "Real, overclaimed, or aspirational",
            "Three buckets for sorting AI-in-science claims by how well the evidence supports them.")),

    dict(fid="fig-w11-five-layers", page=SOV, loc=r'Five-Layer', mode="after_p",
         cap="The five layers of AI capacity, from the compute floor up — the course's map for the African half of the week. Compute comes first because everything rests on it.",
         svg=D.vflow([
             ("Compute — GPUs, data centres, power (the floor)", 'accent'),
             ("Data — corpora, domain data, governance", 'accent'),
             ("Models — trained or adapted; benchmarks", 'accent'),
             ("Policy — strategies and regulation", 'accent'),
             ("Talent — researchers and communities", 'good'),
         ], "The five layers of sovereign AI capacity",
            "A stack of five capacity layers from compute at the floor up through data, models, policy, and talent.")),

    dict(fid="fig-w11-lineage", page=DAT, loc=r'Global Indigenous', mode="after_p",
         cap="African data-sovereignty work sits inside a longer Indigenous lineage — from the Māori Kaitiakitanga licence, through the CARE Principles drafted in Gaborone, to the Esethu Framework.",
         svg=D.vtimeline([
             ("Kaitiakitanga licence — Te Hiku, Aotearoa", [("Māori guardianship of language data", 'accent')]),
             ("CARE Principles — Gaborone, 2018", [("Indigenous data governance, globally", 'accent')]),
             ("Esethu Framework — ACL 2025", [("the African expression of the arc", 'good')]),
         ], "The global Indigenous data-sovereignty lineage",
            "A three-step lineage from the Kaitiakitanga licence through the CARE Principles to the Esethu Framework.")),

    dict(fid="fig-w11-models", page=DAT, loc=r'African Foundation-Model Inventory', mode="after_p",
         cap="A snapshot of the African foundation-model inventory — encoders, from-scratch decoders, adapted Llama models, and named-language models.",
         svg=D.matrix(["Examples", "What they do"], [
             ("Encoders", ["AfriBERTa, AfroXLMR, Serengeti", "understand and classify text"]),
             ("From-scratch decoders", ["InkubaLM, MzansiLM", "generate text, built ground-up"]),
             ("Adapted decoders", ["AfroLlama, UlizaLlama, Lugha-Llama", "Llama tuned for African languages"]),
             ("Named-language", ["KinyaBERT, SwahBERT, Walia-LLM", "one language each"]),
         ], "The African foundation-model inventory",
            "Four families of African language model with representative examples and what each does.",
            label_w=158)),

    dict(fid="fig-w11-strategy", page=POL, loc=r'Strategy Landscape', mode="after_p",
         cap="African AI policy, calibrated: most countries have strategies but few have binding law — and South Africa stands out for withdrawing its draft.",
         svg=D.matrix(["Where they stand (2026)", "Key point"], [
             ("South Africa", ["Draft policy withdrawn", "the standout reversal, April 2026"]),
             ("Nigeria", ["Revised strategy, Sept 2025", "N-ATLAS model shipped"]),
             ("Rwanda", ["Operational, partial", "costed; Responsible AI Office"]),
             ("Kenya", ["Launched March 2025", "leans on 2019 Data Protection Act"]),
             ("Egypt", ["2nd-edition, Jan 2025", "big KPIs, dashboard not visible"]),
             ("Ethiopia", ["Approved June 2024", "institute active; law pre-legislative"]),
             ("Morocco", ["No standalone strategy", "framework law pre-parliament"]),
         ], "African AI strategy versus governance",
            "Seven countries compared on the status of their AI strategy and a key point for each.",
            label_w=112)),
]

if __name__ == '__main__':
    main(FIGS, "wk11")
