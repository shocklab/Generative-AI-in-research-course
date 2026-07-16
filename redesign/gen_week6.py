#!/usr/bin/env python3
import diagrams as D
from genlib import main

WT = "content/week-6/Writing as Thinking.html"
RI = "content/week-6/Research Ideation with AI.html"
TL = "content/week-6/AI Writing Tools - Landscape and Assessment.html"
SI = "content/week-6/Scientific Integrity and the Writing Pipeline.html"
BW = "content/week-6/Building Your AI Writing Workflow.html"
UR = "content/week-6/Using AI to Review Your Own Work.html"

FIGS = [
    dict(fid="fig-w6-assistance-spectrum", page=WT, loc=r'Spectrum of AI Assistance', mode="after_p",
         cap="Five levels of AI writing help, from fixing typos to generating whole sections — the risk rises as AI moves from polishing your words to producing your ideas.",
         svg=D.spectrum([
             ("Proofreading & grammar", 'good'),
             ("Language enhancement", 'good'),
             ("Restructuring", 'warn'),
             ("Generating arguments", 'bad'),
             ("Generating whole sections", 'bad'),
         ], "A spectrum of AI writing assistance",
            "Five levels of assistance from proofreading to generating whole sections, low risk to high.",
            lo="you do the thinking", hi="AI does the thinking")),

    dict(fid="fig-w6-monoculture", page=RI, loc=r'Idea Monoculture Problem', mode="after_p",
         cap="The monoculture risk: when everyone brainstorms with the same models, ideas converge and the field's diversity quietly narrows.",
         svg=D.cycle([
             dict(title="Same tools for everyone", sub="the same frontier models"),
             dict(title="Convergent ideas", sub="similar prompts, similar output"),
             dict(title="Directions narrow", sub="the field homogenises"),
             dict(title="Pressure to adopt AI", sub="to keep pace with peers"),
         ], "The idea monoculture loop",
            "A reinforcing loop where shared tools produce convergent ideas and a narrowing field.",
            center=dict(title="Idea monoculture", sub="less diversity of thought"),
            center_kind='warn', arrow='#b07a1e')),

    dict(fid="fig-w6-multilingual", page=TL, loc=r'Multilingual Equity', mode="after_p",
         cap="Amano et al.: AI translation could lift the burden on non-native English writers — or entrench English further. Which future depends on how we use it.",
         svg=D.tree("AI translation goes mainstream", [
             dict(title="Write in English", sub="AI polishes to native level", kind='warn', action="English hegemony deepens"),
             dict(title="Write in your language", sub="read and publish in yours", kind='good', action="More language diversity"),
         ], "Two futures for multilingual publishing",
            "A fork from widespread AI translation into deepening English dominance or growing linguistic diversity.")),

    dict(fid="fig-w6-publishers", page=SI, loc=r'Updated Journal Policies', mode="after_p",
         cap="Major publishers converge on two rules — AI cannot be an author, and substantive AI use must be disclosed — while differing in strictness.",
         svg=D.matrix(["AI as author?", "Disclosure?", "Stance"], [
             ("Science (AAAS)", ["No", "Yes — full prompts", "Strictest"]),
             ("Nature", ["No", "For substantive use", "Middle ground"]),
             ("Elsevier", ["No", "Yes — on submission", "Disclosure-focused"]),
             ("IEEE", ["No", "Yes", "Disclosure-focused"]),
             ("ACM", ["No", "Yes", "Responsibility-centred"]),
         ], "Major publisher AI policies",
            "Five publishers compared on AI authorship, disclosure requirements, and overall stance.")),

    dict(fid="fig-w6-workflow", page=BW, loc=r'The Principled Workflow', mode="after_p",
         cap="A principled writing workflow — AI earns its place in the middle (drafting and auditing); the thinking and the final voice stay yours.",
         svg=D.vflow([
             ("1 · Think first, before any AI", 'accent'),
             ("2 · Outline it yourself", 'accent'),
             ("3 · Draft with AI assistance", 'good'),
             ("4 · Audit thoroughly", 'good'),
             ("5 · Revise in your own voice", 'accent'),
         ], "The principled writing workflow",
            "Five stages where AI assists with drafting and auditing while the thinking and voice stay the researcher's.")),

    dict(fid="fig-w6-peer-review", page=UR, loc=r'What AI Can Usefully', mode="after_p",
         cap="Use AI to catch the checkable — consistency, clarity, stats, gaps — but novelty, significance, and ethics still need human judgment.",
         svg=D.columns([
             dict(title="AI can usefully check", kind='good', lines=["Logical consistency", "Writing quality", "Positioning & related work", "Methodology gaps", "Statistical reporting", "Figures and tables"]),
             dict(title="Human judgment only", kind='warn', lines=["True novelty", "Domain conventions", "Significance", "Ethical concerns", "Reviewer taste & politics"]),
         ], "What AI can and cannot judge in review",
            "Two columns splitting review dimensions AI checks reliably from those that need human judgment.")),
]

if __name__ == '__main__':
    main(FIGS, "wk6")
