#!/usr/bin/env python3
import diagrams as D
from genlib import main

CC = "content/advanced/Claude Code as a Research Environment.html"
HC = "content/advanced/Cost Access and the Disposition Shift.html"
FC = "content/advanced/First Contact and the Control Surface.html"
RP = "content/advanced/Reproducibility and the Project Folder.html"
EN = "content/advanced/Encoding Good Habits - CLAUDE.md Pre-registration and Skills.html"
E2E = "content/advanced/The Reproducible Workflow End to End.html"

FIGS = [
    dict(fid="fig-adv-chat-vs-agent", page=CC, loc=r'Categorically Different From Chat', mode="after_p",
         cap="The categorical difference: a chat's value evaporates in the conversation; Claude Code's work lands in durable files you can re-run, inspect, and cite. The chat is not the archive.",
         svg=D.columns([
             dict(title="Chat window", kind='alt', lines=["Work lives in the conversation", "Answers you copy out by hand", "Gone when you close the tab", "No trace of what happened"]),
             dict(title="Claude Code", kind='accent', lines=["Work lands in real files", "Scripts, outputs, a decision log", "Tracked in Git history", "The folder is the record"]),
         ], "Chat versus agent: where the work lives",
            "Two columns contrasting a chat, where work evaporates, with Claude Code, where work lands in durable files.")),

    dict(fid="fig-adv-automate", page=HC, loc=r'What Not to Automate', mode="after_p",
         cap="Delegate the mechanical, repetitive, and adversarial work; keep the idea, the reading, the writing, and the judgement. The struggle is not a bug.",
         svg=D.columns([
             dict(title="Fair to delegate", kind='good', lines=["Mechanical, repetitive tasks", "Fetching and formatting", "Checking claims", "Catching inconsistencies"]),
             dict(title="Yours alone", kind='warn', lines=["The idea", "Reading", "Writing — it is thinking", "Judgement, and the struggle"]),
         ], "What to automate and what to keep",
            "Two columns separating work fair to delegate to an agent from work that must remain the researcher's.")),

    dict(fid="fig-adv-permissions", page=FC, loc=r'Permissions and Plan Mode', mode="after_p",
         cap="Four controls keep you in charge of an agent working on your data — from the everyday permission prompt to the sandbox around what it can reach.",
         svg=D.vflow([
             ("Permission prompts — it asks before acting", 'neutral'),
             ("Plan mode — look without touching", 'accent'),
             ("Allowlists — pre-approve safe commands", 'accent'),
             ("Sandbox — limits what it can reach", 'good'),
         ], "The control surface, most permissive to most protective",
            "Four layered controls from permission prompts through plan mode and allowlists to the sandbox boundary.")),

    dict(fid="fig-adv-folder", page=RP, loc=r'Project Folder as the Unit', mode="after_p",
         cap="The reproducible project folder — each part answers a question a future replicator (or you) will ask: what did you measure, what did you do, and why.",
         svg=D.filetree([
             ("CLAUDE.md", "the standing instructions", 0),
             ("data/raw/", "original data — never edited", 0),
             ("data/processed/", "cleaned, regenerable from raw", 0),
             ("scripts/", "the code, preserved and re-runnable", 0),
             ("outputs/", "figures, tables, reports", 0),
             ("notes/decision-log.md", "every choice, dated, with reasons", 0),
             ("pre-registrations/", "predictions set in advance", 0),
         ], "Anatomy of a reproducible project folder",
            "A folder listing where each file or directory carries the question it answers for a future replicator.",
            note_x=250)),

    dict(fid="fig-adv-prereg", page=EN, loc=r'Pre-registration: Decide', mode="after_p",
         cap="Pre-registration in one gate: write the prediction and the decision rule before you run anything, then let the pre-set bar — not hope — decide whether to continue.",
         svg=D.tree("Pre-registration gate", [
             dict(title="Interesting", sub="clears the bar", kind='good', action="Spend more compute"),
             dict(title="Worth knowing", sub="boring but real", kind='neutral', action="Report it briefly"),
             dict(title="Dead", sub="doesn't clear", kind='bad', action="Stop, don't sink cost"),
         ], "The pre-registration gate",
            "A gate with three outcomes — interesting, worth-knowing, or dead — set before any results are seen.")),

    dict(fid="fig-adv-disclosure", page=E2E, loc=r'Reproducible Folder Is the Disclosure', mode="after_p",
         cap="The reproducible folder is the disclosure — each honest question about what the AI did and what you decided is answered by a specific part of the folder, making 'AI tools were used' obsolete.",
         svg=D.matrix(["Answered by"], [
             ("What rules did the AI follow?", ["CLAUDE.md"]),
             ("What did you decide, and why?", ["notes/decision-log.md"]),
             ("What was the method?", ["scripts/"]),
             ("Was the standard set in advance?", ["pre-registrations/"]),
             ("What changed, and when?", ["Git history"]),
         ], "The folder as disclosure",
            "Five disclosure questions, each mapped to the part of the reproducible folder that answers it.",
            label_w=290)),
]

if __name__ == '__main__':
    main(FIGS, "adv")
