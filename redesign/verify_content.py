#!/usr/bin/env python3
"""
verify_content.py — content-parity safety check for the re-skin.

For every rendered lesson, compare the visible words of the ORIGINAL page's
.content body against the rendered .abody. They must match (the re-skin moves
presentation only). Emoji and whitespace are normalised out; word multisets are
compared so reordering-free text loss/addition is caught.
"""
import os, re, json, sys
from collections import Counter
from urllib.parse import unquote

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOCS = os.path.join(ROOT, "content")
OUT  = os.path.join(ROOT, "docs")
INDEX_SRC = os.path.join(DOCS, "index.html")

def strip_tags(s): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s or '')).strip()
def strip_emoji(s):
    s = re.sub(r'&#(\d+);', lambda m: '' if int(m.group(1)) >= 8500 else m.group(0), s or '')
    return re.sub(r'&#x[0-9a-fA-F]+;', '', s)  # hex emoji entities (e.g. &#x1F4C4;) aren't words
def inner_div(src, cls):
    s = re.search(r'<div class="' + re.escape(cls) + r'"[^>]*>', src)
    if not s: return ""
    i = s.end(); depth = 1
    for m in re.finditer(r'<div\b[^>]*>|</div>', src[i:]):
        depth += -1 if m.group().startswith('</div') else 1
        if depth == 0: return src[i:i + m.start()]
    return src[i:]
def words(t): return Counter(re.findall(r'[a-z0-9]+', strip_emoji(t or '').lower()))

def lessons_from_index():
    src = open(INDEX_SRC, encoding="utf-8").read()
    out = []
    for b in src.split('<div class="week-section">')[1:]:
        for u in re.findall(r'<ul class="lesson-list"[^>]*>(.*?)</ul>', b, re.S):
            for am in re.finditer(r'<a [^>]*href="([^"]+)"[^>]*>', u, re.S):
                out.append(am.group(1).replace('&amp;', '&'))
    return out

def main():
    bad = []; ok = 0; missing = 0
    for href in lessons_from_index():
        rel = unquote(href)
        srcf = os.path.join(DOCS, rel); outf = os.path.join(OUT, rel)
        if not (os.path.exists(srcf) and os.path.exists(outf)):
            missing += 1; continue
        src = open(srcf, encoding="utf-8").read()
        out = open(outf, encoding="utf-8").read()
        sc = inner_div(src, "content") or inner_div(src, "container")
        sc = re.sub(r'\n*<!-- (PAGE-NAV|SCORM-HOOK|ANALYTICS)-START -->.*?-END -->', '', sc, flags=re.S)
        ab = inner_div(out, "abody")
        ws, wo = words(strip_tags(sc)), words(strip_tags(ab))
        lost = ws - wo            # words in source missing from output
        added = wo - ws           # words in output not in source
        # ignore tiny noise (<=2 total token-instances drift)
        if sum(lost.values()) > 2 or sum(added.values()) > 2:
            bad.append((rel, sum(ws.values()), sum(wo.values()),
                        dict(lost.most_common(6)), dict(added.most_common(6))))
        else:
            ok += 1
    print(f"content parity: {ok} clean, {len(bad)} flagged, {missing} missing files")
    for rel, ns, no, lost, added in bad:
        print(f"\n@@ {rel}  (src {ns}w -> out {no}w)")
        if lost:  print(f"   LOST  : {lost}")
        if added: print(f"   ADDED : {added}")

if __name__ == "__main__":
    main()
