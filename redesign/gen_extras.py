#!/usr/bin/env python3
"""The extra diagrams in Weeks 5/9/10 that go beyond the original pilot."""
import diagrams as D
from genlib import main

W5L = "content/week-5/The AI Literature Review Landscape.html"
W5P = "content/week-5/Paid Tools and When They Are Worth It.html"
W9T = "content/week-9/The Trajectory of LLM Capabilities.html"
W9V = "content/week-9/Verification Protocols for a Moving Target.html"
W10R = "content/week-10/RAG in 2026.html"
W10A = "content/week-10/Advanced Research Tools - A Curated Tour.html"

FIGS = [
    dict(fid="fig-w5-three-categories", page=W5L, loc=r'Three Categories of AI Literature', mode="after_p",
         cap="Three kinds of AI literature tool — citation-graph mappers, meaning-based search, and grounded chat that answers from real retrieved papers.",
         svg=D.columns([
             dict(title="Citation-based", kind='alt', lines=["Maps the citation graph", "Who-cites-whom links", "e.g. ResearchRabbit"]),
             dict(title="Semantic search", kind='accent', lines=["Searches by meaning", "Embeddings, not keywords", "e.g. Semantic Scholar"]),
             dict(title="Grounded chat (RAG)", kind='good', lines=["Answers from real papers", "Cites what it retrieved", "e.g. Scite, NotebookLM"]),
         ], "Three categories of AI literature tools",
            "Three tool types compared: citation-graph discovery, semantic search, and grounded retrieval chat.")),

    dict(fid="fig-w5-when-to-pay", page=W5P, loc=r'The Honest Comparison', mode="after_p",
         cap="When a paid tool earns its keep: match the task to the tool. Otherwise the free tools cover general use.",
         svg=D.tree("What is the literature task?", [
             dict(title="Systematic review", sub="exhaustive, structured", kind='accent', action="Elicit"),
             dict(title="Contested claim", sub="does it hold up?", kind='neutral', action="Scite"),
             dict(title="Consensus check", sub="what does the field say?", kind='good', action="Consensus"),
         ], "When to pay for a literature tool",
            "A decision tree matching the literature task to the paid tool worth it, or a free alternative.")),

    dict(fid="fig-w9-benchmark-pitfalls", page=W9T, loc=r"What Benchmarks Don", mode="after_p",
         cap="Three reasons a high benchmark score can mislead: gaming the metric, test-set contamination, and benchmarks that ignore low-resource languages.",
         svg=D.columns([
             dict(title="Goodhart's law", kind='warn', lines=["The metric becomes the target", "Models train to the test", "Score up, skill flat"]),
             dict(title="Contamination", kind='warn', lines=["Test data leaks into training", "The model has seen it", "Inflated scores"]),
             dict(title="Coverage gap", kind='bad', lines=["Built on high-resource English", "African languages under-tested", "Scores don't transfer"]),
         ], "Three ways benchmarks mislead",
            "Three benchmark pitfalls: Goodhart's law, training-data contamination, and the low-resource coverage gap.")),

    dict(fid="fig-w9-verification-cards", page=W9V, loc=r'Layer 1: Verifying', mode="after_p",
         cap="Eight everyday checks for AI output — each aimed at a specific way it fails. Use them as a quick reference before you trust a result.",
         svg=D.matrix(["What it catches"], [
             ("Known-answer testing", ["wrong answers you can check"]),
             ("Adversarial prompting", ["confident but fragile claims"]),
             ("Cross-model triangulation", ["one model's blind spots"]),
             ("Teach-it-back", ["shallow, borrowed understanding"]),
             ("Manual spot-checks", ["errors hidden in bulk output"]),
             ("Citation verification", ["fabricated references"]),
             ("Reproducibility testing", ["results that don't replicate"]),
             ("Domain-expert spot-checks", ["plausible-but-wrong specifics"]),
         ], "Eight verification techniques",
            "Eight Layer-1 verification techniques, each matched to the failure mode it catches.",
            label_w=204)),

    dict(fid="fig-w10-rag-compare", page=W10R, loc=r'Change Two', mode="after_p",
         cap="Classic RAG fetches once and answers; agentic RAG loops — planning, retrieving, reflecting, and retrieving again. That loop is what Deep Research modes do under the hood.",
         svg=D.columns([
             dict(title="Classic RAG", kind='alt', lines=["Retrieve once, then answer", "One pass, linear", "Fast and cheap", "Misses what it didn't fetch"]),
             dict(title="Agentic RAG", kind='accent', lines=["Plan, retrieve, reflect, repeat", "A loop, not a pass", "What Deep Research does", "Finds what one query would miss"]),
         ], "Classic RAG versus agentic RAG",
            "Two columns contrasting single-pass classic RAG with the plan-retrieve-reflect loop of agentic RAG.")),

    dict(fid="fig-w10-free-pipeline", page=W10A, loc=r'Free-Tier Research Pipeline', mode="after_p",
         cap="A capable research pipeline on free tiers alone — but verification and the final audit stay yours. Agents change the tools, not the responsibility.",
         svg=D.vflow([
             ("Explore — Perplexity, Kimi, deep-research modes", 'accent'),
             ("Verify — check every citation (Week 5)", 'good'),
             ("Synthesise — cluster and compare findings", 'accent'),
             ("Write — draft in your own voice", 'accent'),
             ("Audit — you own the final check", 'good'),
         ], "A free-tier research pipeline",
            "A five-stage free-tier pipeline from exploring through verifying, synthesising, writing, and auditing.")),
]

if __name__ == '__main__':
    main(FIGS, "extras")
