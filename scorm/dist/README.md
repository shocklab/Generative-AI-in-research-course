# MAM5020F: Generative AI for Research — SCORM 1.2 Packages

This folder contains SCORM 1.2 packages for the course **MAM5020F (2026): Generative AI for Research**, taught at the University of Cape Town by Assoc. Prof. Jonathan Shock. The materials are licensed **CC BY 4.0** — share and adapt freely with attribution.

## What's in this folder

13 SCORM 1.2 ZIPs:

| File | Contents | Approx. size |
|---|---|---|
| `mam5020f_course_scorm12.zip` | **Full course** — every lesson, all 12 weeks plus course orientation and introduction. One unified SCORM package. | ~810 KB |
| `mam5020f_week1_scorm12.zip` | Week 1 — Foundations of Generative AI | ~65 KB |
| `mam5020f_week2_scorm12.zip` | Week 2 — LLM Deep Dive | ~55 KB |
| `mam5020f_week3_scorm12.zip` | Week 3 — Environmental Implications of AI | ~70 KB |
| `mam5020f_week4_scorm12.zip` | Week 4 — Ethical Frameworks for AI in Research | ~75 KB |
| `mam5020f_week5_scorm12.zip` | Week 5 — AI-Assisted Literature Reviews | ~80 KB |
| `mam5020f_week6_scorm12.zip` | Week 6 — AI for Writing, Communication & Research Ideation | ~105 KB |
| `mam5020f_week7_scorm12.zip` | Week 7 — AI for Data, Code & Computation | ~115 KB |
| `mam5020f_week8_scorm12.zip` | Week 8 — Multimodal AI for Research | ~80 KB |
| `mam5020f_week9_scorm12.zip` | Week 9 — Critical Evaluation & Limitations of AI | ~75 KB |
| `mam5020f_week10_scorm12.zip` | Week 10 — Agentic AI, RAG & Advanced Research Tools | ~75 KB |
| `mam5020f_week11_scorm12.zip` | Week 11 — Future of AI in Research & Africa's Sovereign AI Capacity | ~110 KB |
| `mam5020f_week12_scorm12.zip` | Week 12 — Integrative Capstone | ~27 KB |

Each per-week package is self-contained — it includes its own lesson pages, the SCORM API binding, and the course landing page so navigation works inside the LMS.

## How to deploy

These are standard **SCORM 1.2** packages. They can be imported into any SCORM-compliant Learning Management System: Brightspace (incl. UCT's Amathuba), Moodle, Canvas, Blackboard, Cornerstone, Open edX with the SCORM XBlock, and most others.

**Typical import flow (Brightspace example):**
1. In your course, go to **Content**
2. Inside a module, click **Existing Activities → SCORM/xAPI**
3. Upload the ZIP
4. The LMS imports the manifest and surfaces the lesson titles

For Moodle, Canvas, etc., the path differs slightly but the same ZIP works.

**Quick validation:** if you want to verify a package before deploying it, [SCORM Cloud](https://cloud.scorm.com/) has a free testing tier — sign in, upload the ZIP, and you'll see exactly how an LMS will render it.

## Completion logic

These packages mark each page as **completed** when the learner opens it. No quiz or scroll-threshold requirement. If you want richer completion logic for your deployment, the SCORM API binding (`scorm-api.js`) inside each ZIP is small and easy to modify — search for `cmi.core.lesson_status` in that file.

## What you get inside each ZIP

```
imsmanifest.xml              ← SCORM 1.2 manifest (the lesson order and structure)
imscp_rootv1p1p2.xsd         ← IMS Content Packaging schema
imsmd_rootv1p2p1.xsd         ← IMS Metadata schema
adlcp_rootv1p2.xsd           ← ADL SCORM extension schema
scorm-api.js                 ← The runtime JavaScript binding to the LMS
index.html                   ← Course landing page (for in-package navigation)
week-N/                      ← The actual lesson HTML files
```

> **Note on `adlcp_rootv1p2.xsd`**: the canonical copy of this file is served by ADLnet.gov and was occasionally unavailable when these packages were built; in some cases this XSD may be a small placeholder pointing at the canonical URL rather than the real ~14 KB schema. Most LMSes do not strictly validate the bundled XSDs at import time — these packages have been tested successfully on SCORM Cloud. If your LMS rejects the package for an XSD reason, ask the package maintainer to rebuild after fetching the schema cleanly, or substitute the file from <https://adlnet.gov/projects/scorm-1-2/>.

## External dependencies (browser-loaded at runtime)

The lessons embed YouTube videos via `youtube-nocookie.com` and load the Lato font from Brightspace's CDN. Both work fine inside any modern LMS as long as the learner is online. There are no external assets required at import time.

## Source, updates, and full live version

- **GitHub source**: <https://github.com/shocklab/Generative-AI-in-research-course>
- **Live web version** (publicly browseable, always current): <https://shocklab.github.io/Generative-AI-in-research-course/>
- **Contact**: Jonathan Shock, jonathan.shock@uct.ac.za

## Attribution

If you deploy these materials in your own institution, please retain the existing footer attribution on each lesson page, and cite as:

> Shock, J. (2026). *MAM5020F: Generative AI for Research* [Course materials]. University of Cape Town. <https://shocklab.github.io/Generative-AI-in-research-course/>

Materials are licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
