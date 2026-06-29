#!/usr/bin/env python3
"""
check_links.py — internal link integrity for the rendered Press site.

Walks redesign/site/, extracts every href/src, resolves relative paths, and
reports any internal target that does not exist on disk. External URLs, mailto,
and pure #anchors are skipped.
"""
import os, re
from urllib.parse import unquote, urldefrag

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(os.path.dirname(HERE), "docs")

def main():
    pages = []
    for dp, _, fns in os.walk(SITE):
        for fn in fns:
            if fn.endswith(".html"):
                pages.append(os.path.join(dp, fn))
    broken = {}; total = 0
    for p in pages:
        src = open(p, encoding="utf-8").read()
        for m in re.finditer(r'(?:href|src)="([^"]+)"', src):
            url = m.group(1)
            if url.startswith(("http://", "https://", "//", "mailto:", "#", "data:")):
                continue
            target = urldefrag(url)[0]
            if not target:
                continue
            total += 1
            fs = os.path.normpath(os.path.join(os.path.dirname(p), unquote(target)))
            if not os.path.exists(fs):
                broken.setdefault(os.path.relpath(p, SITE), []).append(url)
    print(f"checked {total} internal links across {len(pages)} pages")
    if not broken:
        print("all internal links resolve.")
    else:
        nb = sum(len(v) for v in broken.values())
        print(f"{nb} BROKEN links in {len(broken)} pages:")
        for pg, links in sorted(broken.items()):
            print(f"\n@@ {pg}")
            for l in sorted(set(links)): print("   ->", l)

if __name__ == "__main__":
    main()
