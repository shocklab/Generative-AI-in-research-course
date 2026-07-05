#!/usr/bin/env python3
"""Shared insert/dump helper for the per-week diagram generators."""
import os, re, sys

ROOT = "/Users/jonathanshock/Cursor folders/Gen AI in research course/Course materials"


def _insert(FIGS):
    for f in FIGS:
        path = os.path.join(ROOT, f['page'])
        src = open(path, encoding='utf-8').read()
        if f'id="{f["fid"]}"' in src:
            print("SKIP (present):", f['fid']); continue
        # only match inside the .content body — avoids hitting the page title/h1/nav
        cstart = src.find('class="content"')
        base = (src.find('>', cstart) + 1) if cstart != -1 else 0
        m = re.search(f['loc'], src[base:])
        if not m:
            print("!! LOCATOR NOT FOUND:", f['fid'], "in", f['page']); continue
        ms, me = base + m.start(), base + m.end()
        if f['mode'] == 'before':
            idx = ms
        elif f['mode'] == 'after_p':
            c = src.find('</p>', me); idx = c + 4 if c != -1 else me
        else:
            idx = me
        fig = f'\n<figure id="{f["fid"]}" class="diagram">{f["svg"]}<figcaption>{f["cap"]}</figcaption></figure>\n'
        open(path, 'w', encoding='utf-8').write(src[:idx] + fig + src[idx:])
        print("OK inserted:", f['fid'])


def _dump(FIGS, tag):
    out = os.path.join(ROOT, "redesign", "_%s_preview" % tag)
    os.makedirs(out, exist_ok=True)
    for f in FIGS:
        open(os.path.join(out, f['fid'] + ".svg"), "w", encoding="utf-8").write(f['svg'])
    print("dumped", len(FIGS), "to", out)


def main(FIGS, tag):
    _insert(FIGS) if '--insert' in sys.argv else _dump(FIGS, tag)


def check(FIGS):
    for f in FIGS:
        src = open(os.path.join(ROOT, f['page']), encoding='utf-8').read()
        print(("FOUND " if re.search(f['loc'], src) else "MISSING"), f['fid'])
