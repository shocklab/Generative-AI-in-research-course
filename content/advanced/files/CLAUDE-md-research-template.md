# CLAUDE.md - <project name>

<!--
  Research-habits template for Claude Code.
  Adapted, with thanks, from the AGENTS.md conventions in Dominik Lukes'
  "Using AI Agents for Reproducible Research" workshop (Oxford), and extended
  with habits working researchers tend to add. Part of the MAM5020F Advanced
  Track. CC BY 4.0. Fill in the two lines below and adjust the rules to fit.
-->

## What this project is
- One line on the project, the data, and the question.
- Status: e.g. "fictional teaching project" / "real, unpublished - do not share".

## Working rules
- Read files before proposing changes.
- Never modify anything in data/raw/. It is the only copy.
- Use plan mode and show me the plan before any consequential change.
- When you summarise or analyse, name which files you used.
- If something is uncertain, say so - never fill a gap with a plausible guess.
- Save reusable code in scripts/; save generated outputs in outputs/.
- Log every consequential decision in notes/decision-log.md, dated, with the reason.
- Run analysis scripts to a committed log (... 2>&1 | tee outputs/<name>_run.log);
  the log, not the figure, is the record of what happened.
- Work from logs and printed tables, not screenshots, unless I ask otherwise.
- Before you tell me a task is done, show me the diff.

## Pre-registration
- If the pre-registrations/ folder has an entry for the current question, it is
  binding. Do not tune on the headline metric; do not reframe a result after the
  fact. If reality contradicts the prediction, apply the decision rule and say so.

## Boundaries
- Don't add claims about real people, studies, or institutions that aren't in the sources.
- Don't commit or push unless I ask; don't send anything on my behalf.
- British spelling.
