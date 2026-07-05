#!/usr/bin/env python3
import diagrams as D
from genlib import main

MIN = "content/week-3/Critical Minerals and AI.html"
INF = "content/week-3/Infrastructure Scale and the Rebound Problem.html"
SUS = "content/week-3/Sustainable AI What Can Be Done.html"

FIGS = [
    dict(fid="fig-w3-supply-chain", page=MIN, loc=r'From Mine to Data Centre', mode="after_p",
         cap="From mine to data centre — the material chain behind AI hardware, with the heaviest human and environmental costs at the extraction end.",
         svg=D.vflow([
             ("Mining — silicon, cobalt, copper, rare earths", 'neutral'),
             ("Refining — purify into usable materials", 'accent'),
             ("Chip and component fabrication", 'accent'),
             ("Servers, cooling and power systems", 'accent'),
             ("The data centre", 'good'),
         ], "From mine to data centre",
            "A five-stage supply chain from mining raw minerals to the finished data centre.")),

    dict(fid="fig-w3-datacentre", page=INF, loc=r"What.s Inside a Data Centre", mode="after_p",
         cap="Where a data centre's energy and water go: compute does the work, cooling keeps it alive, and power delivery loses some along the way.",
         svg=D.columns([
             dict(title="Compute", kind='accent', lines=["GPUs (H100 / H200)", "The energy-hungry core", "Most of the power draw"]),
             dict(title="Cooling", kind='alt', lines=["Stops chips overheating", "Large water footprint", "Air or liquid systems"]),
             dict(title="Power delivery", kind='neutral', lines=["Conversion and backup", "Losses along the way", "Grid plus generators"]),
         ], "What's inside a data centre",
            "Three subsystems of a data centre — compute, cooling, and power delivery — and what each costs.")),

    dict(fid="fig-w3-jevons", page=INF, loc=r'Rebound Problem', mode="after_p",
         cap="The rebound problem: efficiency gains lower the cost of AI, which drives more total use — so the overall footprint can grow rather than shrink.",
         svg=D.cycle([
             dict(title="AI gets more efficient", sub="cost per query falls"),
             dict(title="Using AI gets cheaper", sub="so we use much more"),
             dict(title="Total demand rises", sub="more queries and models"),
             dict(title="More data centres built", sub="net footprint grows"),
         ], "The Jevons paradox in AI",
            "A reinforcing loop where efficiency lowers cost, raising total use and the overall footprint.",
            center=dict(title="Jevons paradox", sub="efficiency is not less use"),
            center_kind='warn', arrow='#b07a1e')),

    dict(fid="fig-w3-decision", page=SUS, loc=r'Framework for Your Own', mode="after_p",
         cap="A few questions before reaching for a frontier model — most research compute can be made smaller, simpler, or skipped.",
         svg=D.vflow([
             ("Do I actually need AI for this task?", 'accent'),
             ("Would a simpler method or smaller model do?", 'accent'),
             ("Can I run locally, or batch and reuse results?", 'accent'),
             ("Only then: use a frontier model", 'good'),
         ], "Questions before running compute-heavy AI",
            "A short decision flow that pushes toward simpler, smaller, or no AI before a frontier model.")),
]

if __name__ == '__main__':
    main(FIGS, "wk3")
