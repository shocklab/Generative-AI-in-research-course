#!/usr/bin/env python3
"""
Generate the Advanced Track downloadable artefacts into docs/advanced/files/:

  - berg-river-microplastics.zip        the deliberately-messy sample archive
  - CLAUDE-md-research-template.md       the research-habits CLAUDE.md template
  - reproducible-project-scaffold.zip    an empty good structure to copy

All content is fictional. The mess in the Berg River archive is planted on
purpose so the Lesson A.3 / B.3 exercises have real problems to find:
inconsistent column names across the three site files, a town-site pH meter
that reads x10 all season, sample D-03 marked discarded in the field notes
but still present in the data, missing values, mixed date formats, and a
stale README referring to files that no longer exist.

Re-run after any change. Deterministic (no randomness).
"""

import os, zipfile, io

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
FILES_DIR = os.path.join(ROOT, "docs", "advanced", "files")


# ---------------------------------------------------------------------------
# Berg River messy archive contents
# ---------------------------------------------------------------------------

# Upstream: the "reference" column naming. The automated counter double-counted
# all season, so the recorded values are ~2x the true per-litre figure. The field
# notes say to halve them. This is the systematic trap that decides the result:
# uncorrected, upstream looks the same as the town; halved, the town is clearly higher.
SITE_UPSTREAM = """date,sample_id,particles_per_litre,ph,water_temp_c,notes
2026-03-05,U-01,52,7.1,18.4,
2026-03-05,U-02,62,7.2,18.5,
2026-03-12,U-03,76,7.0,17.9,
2026-03-12,U-04,58,7.1,17.8,
2026-03-19,U-05,88,7.3,17.2,slightly turbid
2026-03-19,U-06,72,7.2,17.1,
2026-03-26,U-07,48,7.0,16.8,
2026-03-26,U-08,66,7.1,16.9,
2026-04-02,U-09,82,7.2,16.4,
2026-04-02,U-10,60,7.1,16.5,
2026-04-09,U-11,92,7.3,15.9,after light rain
2026-04-09,U-12,70,7.2,16.0,
"""

# Town site: DIFFERENT column names, DD/MM/YYYY dates. pH is normal here (the
# planted issues are the upstream double-count and the downstream contamination,
# not pH). T-07 is flagged post-storm in the field notes.
SITE_TOWN = """Date,SampleID,MP_count_per_L,pH,temp,comment
05/03/2026,T-01,48,7.1,18.9,
05/03/2026,T-02,71,7.2,19.0,
12/03/2026,T-03,55,7.0,18.3,
12/03/2026,T-04,66,7.3,18.4,
19/03/2026,T-05,84,7.2,17.7,heavy litter upstream of bridge
19/03/2026,T-06,77,7.1,17.6,
26/03/2026,T-07,90,7.2,17.1,sampled after storm - may be unreliable
26/03/2026,T-08,62,7.0,17.2,
02/04/2026,T-09,74,7.3,16.8,
02/04/2026,T-10,81,7.2,16.9,
09/04/2026,T-11,69,7.1,16.2,
09/04/2026,T-12,45,7.2,16.3,
"""

# Downstream: third naming convention, missing values, and D-03 a contaminated
# outlier (count far higher than any other downstream sample) that the field
# notes say to discard.
SITE_DOWNSTREAM = """sampling_date,id,particles_L,pH_value,temperature,remarks
2026-03-05,D-01,34,7.0,18.7,
2026-03-05,D-02,29,7.1,18.8,
2026-03-12,D-03,118,7.0,18.1,
2026-03-12,D-04,,7.1,18.2,bottle underfilled - count not taken
2026-03-19,D-05,46,,17.5,ph probe error
2026-03-19,D-06,38,7.2,17.4,
2026-03-26,D-07,33,7.1,,temp logger flat
2026-03-26,D-08,40,7.0,16.9,
2026-04-02,D-09,44,7.2,16.6,
2026-04-02,D-10,37,7.1,16.7,
2026-04-09,D-11,49,7.3,16.0,after light rain
2026-04-09,D-12,42,7.2,16.1,
"""

SAMPLING_METADATA = """site,latitude,longitude,distance_from_town_km,sampling_method,collector
upstream,-33.812,18.962,-4.2,grab sample 1L surface,field team A
town,-33.776,18.991,0.0,grab sample 1L surface,field team A
downstream,-33.741,19.018,5.1,grab sample 1L surface,field team B
"""

FIELD_NOTES = """# Berg River microplastics - field notes (season 2026)

Loose notes from the sampling team. Not all of this made it into the
spreadsheets, and some of it contradicts them - read before analysing.

## Equipment

- IMPORTANT: the automated particle counter used at the UPSTREAM site was later
  found to have been DOUBLE-COUNTING all season - it registered each particle
  twice. Every upstream count in the sheet is therefore about twice the true
  figure and must be HALVED to get the real particles/L. The town and downstream
  sites were counted manually and are not affected. (Without this correction the
  upstream counts look almost as high as the town's, which is the whole reason
  the fault was noticed - upstream of a town should not read like the town.)
- The downstream temperature logger failed on 26 March (sample D-07); the
  blank in the sheet is genuine, not a transcription slip.

## Samples to treat with care

- D-03 (downstream, 12 March): the sample bottle cracked in transit and was
  contaminated, which is why its count (118) is far higher than any other
  downstream sample. DISCARD this sample - the value in the sheet should not be
  used.
- D-04 (downstream, 12 March): bottle underfilled, particle count was not
  taken. The blank is intentional.
- D-05 (downstream, 19 March): pH probe error on the day; pH blank is genuine.
- T-07 (town, 26 March): sampled immediately after a storm; counts may be
  unusually high and should be flagged in any interpretation.

## General

- Sites were sampled fortnightly, two grab samples per site per visit.
- "distance_from_town_km" in the metadata is signed: negative is upstream of
  the town, positive is downstream.
"""

LITERATURE_NOTES = """# Reading notes (rough)

Half-organised notes from the literature - to be turned into a proper
review later. Citations are partial; check before using.

- Microplastics in freshwater rivers: concentrations vary enormously with
  proximity to urban runoff and wastewater outfalls. (review paper - find ref)
- Counting methods are not standardised; particles/L is common but size
  thresholds differ between studies, so cross-study comparison is fraught.
- Several studies report higher counts downstream of urban centres, but
  confounded by flow rate and sampling season.
- TODO: find the standard size-class definitions before claiming our counts
  are comparable to anyone else's.
- TODO: check whether "particles per litre" in our sheets means the same
  thing across all three field teams.
"""

README_OLD = """Berg River project - OLD readme (out of date, do not trust)

Files:
  site-A.csv        upstream
  site-B.csv        town
  site-C.csv        downstream
  analysis.xlsx     the analysis spreadsheet

Run analysis.xlsx and update the summary tab.

NOTE: the file names above are stale - the CSVs were renamed and the
old analysis spreadsheet was abandoned. This readme is kept only so you
can see what the project used to look like. Start from the actual files
in data/raw/ instead.
"""

BERG_FILES = {
    "berg-river-microplastics/data/raw/site-upstream.csv": SITE_UPSTREAM,
    "berg-river-microplastics/data/raw/site_town.csv": SITE_TOWN,
    "berg-river-microplastics/data/raw/downstream-final-v2.csv": SITE_DOWNSTREAM,
    "berg-river-microplastics/data/raw/sampling-metadata.csv": SAMPLING_METADATA,
    "berg-river-microplastics/data/raw/field-notes.md": FIELD_NOTES,
    "berg-river-microplastics/literature-notes.md": LITERATURE_NOTES,
    "berg-river-microplastics/README-old.txt": README_OLD,
}


# ---------------------------------------------------------------------------
# CLAUDE.md research-habits template (standalone)
# ---------------------------------------------------------------------------

CLAUDE_TEMPLATE = """# CLAUDE.md - <project name>

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
"""


# ---------------------------------------------------------------------------
# Reproducible-project scaffold contents
# ---------------------------------------------------------------------------

SCAFFOLD_README = """# Reproducible project scaffold

An empty version of the structure from the MAM5020F Advanced Track, Lesson B.1.
Copy it, rename it, and adapt. The point of each part:

  CLAUDE.md            standing instructions the agent reads every session
  data/raw/            the original data - never edited
  data/processed/      cleaned data, regenerable from raw + scripts
  scripts/             the code, preserved and re-runnable
  outputs/             figures, tables, reports (derived; never hand-edited)
  notes/decision-log.md   every consequential choice, dated, with reasons
  docs/data-inventory.md  what the data actually is
  pre-registrations/   predictions + decision rules, written before the compute

Apply as much of this as the work deserves - heavy where results must last,
light where they need not. CC BY 4.0.
"""

DECISION_LOG_TEMPLATE = """# Decision log

One entry per consequential choice, newest at the top. Each entry: the date,
the decision, the reason, and the source (which file or note it came from).

## YYYY-MM-DD - <short description of the decision>
- Decision:
- Reason:
- Source:
"""

DATA_INVENTORY_TEMPLATE = """# Data inventory

A plain description of each raw data file: what it contains, its columns and
their units, the number of rows, missing values, and any known problems.

## <filename>
- Contents:
- Columns (and units):
- Rows:
- Missing values:
- Known problems / anomalies:
"""

SCAFFOLD_FILES = {
    "reproducible-project-scaffold/README.md": SCAFFOLD_README,
    "reproducible-project-scaffold/CLAUDE.md": CLAUDE_TEMPLATE,
    "reproducible-project-scaffold/data/raw/.gitkeep": "",
    "reproducible-project-scaffold/data/processed/.gitkeep": "",
    "reproducible-project-scaffold/scripts/.gitkeep": "",
    "reproducible-project-scaffold/outputs/.gitkeep": "",
    "reproducible-project-scaffold/notes/decision-log.md": DECISION_LOG_TEMPLATE,
    "reproducible-project-scaffold/docs/data-inventory.md": DATA_INVENTORY_TEMPLATE,
    "reproducible-project-scaffold/pre-registrations/.gitkeep": "",
}


def write_zip(path, files: dict):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        for name, content in files.items():
            zf.writestr(name, content)
    print(f"  wrote {path} ({os.path.getsize(path)} bytes, {len(files)} entries)")


def main():
    os.makedirs(FILES_DIR, exist_ok=True)
    print("Generating Advanced Track downloadable artefacts...")

    write_zip(os.path.join(FILES_DIR, "berg-river-microplastics.zip"), BERG_FILES)
    write_zip(os.path.join(FILES_DIR, "reproducible-project-scaffold.zip"), SCAFFOLD_FILES)

    tmpl_path = os.path.join(FILES_DIR, "CLAUDE-md-research-template.md")
    with open(tmpl_path, "w", encoding="utf-8") as f:
        f.write(CLAUDE_TEMPLATE)
    print(f"  wrote {tmpl_path} ({os.path.getsize(tmpl_path)} bytes)")

    print("\nDone.")


if __name__ == "__main__":
    main()
