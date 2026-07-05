#!/usr/bin/env python3
import diagrams as D
from genlib import main

CAP = "content/week-12/Synthesis and the Integrative Capstone.html"

FIGS = [
    dict(fid="fig-w12-disposition", page=CAP, loc=r'Course in One Disposition', mode="after_p",
         cap="The whole course in one disposition — four moves that repeat on any claim: go to the source, read for its limits, calibrate, and decide where you stand before you reach for tools.",
         svg=D.cycle([
             dict(title="Pull the primary source", sub="go to the original"),
             dict(title="Read for limitations", sub="not just the claim"),
             dict(title="Calibrate before you cite", sub="weigh it honestly"),
             dict(title="Choose where you stand", sub="before choosing tools"),
         ], "The course in one disposition",
            "A four-move habit of mind that repeats on any claim, arranged as a loop.",
            center=dict(title="The disposition", sub="a habit, not steps"),
            center_kind='accent', arrow='#2a5298')),

    dict(fid="fig-w12-pitch", page=CAP, loc=r'The Structured Pitch', mode="after_p",
         cap="The 600-word capstone pitch in six prompts — and how each one pulls a specific thread from across the twelve weeks.",
         svg=D.matrix(["What it asks for", "Draws on"], [
             ("1 · Research question", ["one plain-language question", "the whole project"]),
             ("2 · AI tools & stages", ["which tools, which stages, why", "Weeks 5–8, 10"]),
             ("3 · What you won't delegate", ["the boundary you hold", "Weeks 6, 9"]),
             ("4 · Local-context choice", ["one concrete African-context call", "Week 11"]),
             ("5 · Verification protocol", ["a real procedure, not 'be careful'", "Weeks 5, 7, 9"]),
             ("6 · Ethical commitment", ["one principle put into practice", "Week 4"]),
         ], "The six-prompt capstone pitch",
            "Six numbered prompts of the capstone pitch, each mapped to what it asks for and the weeks it draws on.",
            label_w=172)),
]

if __name__ == '__main__':
    main(FIGS, "wk12")
