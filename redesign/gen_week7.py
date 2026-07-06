#!/usr/bin/env python3
import diagrams as D
from genlib import main

NL = "content/week-7/Natural Language to Code.html"
DA = "content/week-7/AI-Assisted Data Analysis in Practice.html"
AG = "content/week-7/Agentic Data Analysis.html"
BW = "content/week-7/Building Your Data Analysis Workflow.html"

FIGS = [
    dict(fid="fig-w7-vibe-coding", page=NL, loc=r'Vibe Coding', mode="after_p",
         cap="Vibe coding is fine for prototypes and play, dangerous for anything you'll report — a scientific error survives autonomous iteration even when the code runs.",
         svg=D.columns([
             dict(title="Safe to vibe-code", kind='good', lines=["Prototypes and exploration", "Throwaway utility scripts", "Learning and play", "Nothing you will report"]),
             dict(title="Dangerous to vibe-code", kind='bad', lines=["Analysis you will publish", "Results that inform policy", "Complex pipelines", "Anything reproducibility-critical"]),
         ], "When vibe coding works and when it fails",
            "Two columns contrasting safe contexts for vibe coding with dangerous ones.")),

    dict(fid="fig-w7-silent-errors", page=DA, loc=r'Silent Error Problem', mode="after_p",
         cap="Six 'silent' errors that produce clean output with no warning — each needs a deliberate check, because the code runs fine either way.",
         svg=D.matrix(["What goes wrong", "How to catch it"], [
             ("Wrong variable", ["AI uses the wrong column", "Check it picked the right variable"]),
             ("Off-by-one (time series)", ["Shifted by one period", "Spot-check dates against rows"]),
             ("Missing-data handling", ["Drops or fills wrongly", "Check how NAs were handled"]),
             ("Wrong statistical test", ["Valid code, wrong test", "Confirm the test's assumptions"]),
             ("Aggregation errors", ["Sums the wrong groups", "Verify group counts and totals"]),
             ("Data leakage", ["Test info bleeds into training", "Trace what the model saw"]),
         ], "The silent error taxonomy",
            "Six categories of silent analysis error, each with what goes wrong and how to catch it.",
            label_w=168)),

    dict(fid="fig-w7-conv-vs-agentic", page=AG, loc=r'From Conversation to Agency', mode="after_p",
         cap="Conversational AI answers one prompt at a time; an agent reads files, runs code, and iterates on its own — which is why oversight moves to checkpoints.",
         svg=D.columns([
             dict(title="Conversational", kind='alt', lines=["You paste, it responds", "You run the code", "One step at a time", "You see every move"]),
             dict(title="Agentic", kind='accent', lines=["It reads files and runs code", "It fixes errors and iterates", "Many steps between check-ins", "You review at checkpoints"]),
         ], "Conversational versus agentic AI",
            "Two interaction styles compared: step-by-step conversation versus an autonomous agent loop.")),

    dict(fid="fig-w7-reliability", page=AG, loc=r'The Reliability Mathematics', mode="after_p",
         cap="Why agentic pipelines need human checkpoints: even at 90% reliability per step, end-to-end success collapses — about 35% over 10 steps, 12% over 20.",
         svg=D.linechart([
             dict(label="", color="#9a2f2f",
                  pts=[(0.0, 0.90), (0.053, 0.81), (0.105, 0.729), (0.211, 0.59), (0.316, 0.478),
                       (0.474, 0.349), (0.737, 0.206), (1.0, 0.122)],
                  marks=[(0.0, 0.90, "90%", 'right'), (0.211, 0.59, "59%", 'ar'),
                         (0.474, 0.349, "35%", 'ar'), (1.0, 0.122, "12%", 'above')]),
         ], [(0.0, "1 step"), (0.211, "5 steps"), (0.474, "10 steps"), (1.0, "20 steps")],
            "Reliability decays as pipelines get longer",
            "A declining curve of end-to-end reliability against the number of agent steps, annotated at 1, 5, 10 and 20 steps.",
            ylabel="chance the whole pipeline is right", yticks=[(1.0, "100%"), (0.5, "50%"), (0.0, "0%")],
            note="At 90% reliability per step, a 20-step pipeline finishes correctly about 12% of the time.")),

    dict(fid="fig-w7-workflow", page=BW, loc=r'Principled Data Analysis Workflow', mode="after_p",
         cap="A principled data-analysis workflow — AI assists with analysis and verification; defining the question and interpreting results stay yours.",
         svg=D.vflow([
             ("1 · Define the question clearly", 'accent'),
             ("2 · Prepare and understand your data", 'accent'),
             ("3 · Analyse with AI assistance", 'good'),
             ("4 · Verify everything", 'good'),
             ("5 · Interpret with your expertise", 'accent'),
         ], "The principled data-analysis workflow",
            "Five stages where AI assists with analysis and verification while framing and interpretation stay the researcher's.")),
]

if __name__ == '__main__':
    main(FIGS, "wk7")
