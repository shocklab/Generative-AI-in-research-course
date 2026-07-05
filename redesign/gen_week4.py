#!/usr/bin/env python3
import diagrams as D
from genlib import main

FL = "content/week-4/Ethical Frameworks and Four Lenses.html"
UB = "content/week-4/Ubuntu Relational Ethics and the Just AI Framework.html"
TR = "content/week-4/Transparency Authorship and Integrity.html"
AP = "content/week-4/Applying Ethics Case Studies and Your Framework.html"

FIGS = [
    dict(fid="fig-w4-four-lenses", page=FL, loc=r'Applying the Lenses', mode="after_p",
         cap="One scenario — a thesis discussion rewritten by AI and submitted undisclosed — judged through each of the four lenses. They diverge, which is the point.",
         svg=D.hubspoke(
             dict(title="Rewritten discussion", sub="undisclosed AI, no policy"),
             [dict(title="Consequentialism", sub="trust erodes if hidden"),
              dict(title="Deontology", sub="breaks a duty of honesty"),
              dict(title="Virtue ethics", sub="is this who I want to be?"),
              dict(title="Ubuntu ethics", sub="harms the supervisor bond")],
             "One scenario through four lenses",
             "A central scenario judged by consequentialist, deontological, virtue, and Ubuntu lenses, each reaching a different emphasis.")),

    dict(fid="fig-w4-rationality", page=UB, loc=r'From Rationality to Relationality', mode="after_p",
         cap="Mhlambi's argument: Western AI ethics starts from the individual; Ubuntu starts from relationship — and that changes what counts as ethical.",
         svg=D.columns([
             dict(title="Cartesian / individual", kind='alt', lines=["'I think, therefore I am'", "Personhood = rational capacity", "Prizes autonomy and rights"]),
             dict(title="Ubuntu / relational", kind='accent', lines=["'I am because we are'", "Personhood through community", "Prizes relationships, the collective"]),
         ], "From rationality to relationality",
            "Two foundations for ethics: the individual rational self versus personhood constituted through community.")),

    dict(fid="fig-w4-integrity-spectrum", page=TR, loc=r'Academic Integrity Spectrum', mode="after_p",
         cap="AI use runs on a spectrum, not a binary: grammar help and search at one end, fabrication and undisclosed authorship at the other, with a large grey zone that needs disclosure and judgment.",
         svg=D.spectrum([
             ("Generally accepted: grammar, search, brainstorming", 'good'),
             ("Grey zone: drafting, analysis — disclose and verify", 'warn'),
             ("Problematic: passing off, fabricating, abdicating", 'bad'),
         ], "The academic integrity spectrum",
            "A three-band spectrum from generally accepted AI uses, through a grey zone, to generally problematic ones.",
            lo="lower risk", hi="misconduct")),

    dict(fid="fig-w4-six-steps", page=AP, loc=r'Decision Framework for AI Ethics', mode="after_p",
         cap="Six steps for reasoning through an AI ethics dilemma — it won't hand you an answer, but it makes sure you've weighed the perspectives before deciding.",
         svg=D.vflow([
             ("1 · Identify the dilemma", 'accent'),
             ("2 · Identify the stakeholders", 'accent'),
             ("3 · Apply the four lenses", 'accent'),
             ("4 · Consider context", 'accent'),
             ("5 · Make a judgment", 'accent'),
             ("6 · Document and disclose", 'good'),
         ], "Six steps for ethical reasoning",
            "A six-step sequence from naming the dilemma to documenting and disclosing the decision.")),
]

if __name__ == '__main__':
    main(FIGS, "wk4")
