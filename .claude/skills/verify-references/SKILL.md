# Verify References

## Description
Post-creation quality check that verifies every external link, academic citation, and factual claim in lesson HTML files. Run this after building any new week's content.

## Usage
```
/verify-references Week 5
/verify-references "Week 5/The Hallucinated Citation Crisis.html"
```

If no argument is given, prompt the user for which week or file to verify.

## Process

### Phase 1: Extract All References
Scan the target HTML file(s) for:
1. **All `<a href="...">` links** — extract every URL
2. **Named academic citations** — anything matching patterns like "Author et al. (YYYY)", "Author (YYYY)", or "(Author, YYYY)"
3. **Specific statistical claims** — any sentence containing a percentage, fraction, or specific number attributed to a study (e.g., "39.6% hallucination rate", "over 100 hallucinated citations")
4. **Tool/platform URLs** — links to tools, services, or platforms mentioned in the content

### Phase 2: Verify URLs
For each extracted URL:
- Use WebFetch to check the URL is accessible (not 404, not redirecting to an error page)
- Confirm the page content is relevant to how it's being cited
- Flag any URLs that fail, redirect unexpectedly, or whose content doesn't match the context

### Phase 3: Verify Academic Citations
For each named citation (e.g., "Linardon et al., 2025"):
- Use WebSearch to find the actual paper
- Confirm: correct author names, correct year, correct journal/venue, paper actually exists
- If a DOI is mentioned, verify it resolves correctly
- If the citation makes a specific claim about the paper's findings, verify that claim against the actual paper

### Phase 4: Verify Statistical Claims
For each specific statistic or factual claim attributed to a source:
- Locate the original source (via the linked URL or via search)
- Confirm the exact number/percentage matches what the source actually says
- Flag any statistics that cannot be traced to a primary source
- Flag any statistics where the number doesn't match the source (even if close)

### Phase 5: Report
Produce a verification report in this format:

```
## Reference Verification Report: [Week/File]
Date: [date]

### Summary
- Total URLs checked: X
- Total citations checked: X
- Total statistics checked: X
- Issues found: X

### URL Verification
| # | URL | Status | Notes |
|---|-----|--------|-------|
| 1 | https://... | OK / BROKEN / MISMATCH | ... |

### Citation Verification
| # | Citation | Exists? | Details Correct? | Notes |
|---|----------|---------|------------------|-------|
| 1 | Author et al. (YYYY) | YES/NO | YES/PARTIAL/NO | ... |

### Statistical Claims Verification
| # | Claim in HTML | Source | Verified? | Actual Value | Notes |
|---|--------------|--------|-----------|-------------|-------|
| 1 | "39.6% for GPT-3.5" | Chelli et al., 2024 | YES/NO | ... | ... |

### Issues Requiring Attention
1. [Description of issue + suggested fix]
2. ...
```

## Important Rules
- NEVER assume a citation is correct just because it looks plausible — that's the whole point of this skill
- Every percentage or specific number must be traced to a primary source
- If a URL works but the content doesn't support how it's being used, flag it
- If you cannot verify a claim after reasonable searching, flag it as UNVERIFIED rather than assuming it's correct
- Check press coverage / secondary sources against primary sources — secondary sources often get numbers wrong
- Be especially sceptical of statistics from web search summaries — these are frequently inaccurate (as we learned the hard way with the "28.6% ChatGPT legal citation" claim)
- For academic papers: always try to find the actual paper (journal site, PubMed, arXiv) rather than relying on news articles about the paper

## After Verification
- Present the report to the user
- For any issues found, suggest specific corrections with the correct information and source
- Only make edits after user approval
