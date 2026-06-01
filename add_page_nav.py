#!/usr/bin/env python3
"""
add_page_nav.py — inject prev/next lesson navigation into the GitHub Pages site.

Single source of truth for lesson ORDER is docs/index.html (the curated
landing page). This script reads that order, then injects a "← Previous /
Next →" nav bar at the bottom of every lesson page in docs/.

- docs/ ONLY. Source Week N/ pages (which feed Amathuba) are left untouched:
  the relative links here would not resolve in the LMS, and the LMS has its
  own next/prev controls.
- Idempotent: the injected block is wrapped in <!-- PAGE-NAV-START/END -->
  markers, so re-running replaces rather than duplicates.
- RE-RUN this after rebuilding any generated week (9-12) with its
  build_weekN.py, because those scripts overwrite the docs copies.

Usage:  python3 add_page_nav.py            (apply)
        python3 add_page_nav.py --check    (report only, no writes)
"""
import os, re, sys, html

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(HERE, "docs")
INDEX = os.path.join(DOCS, "index.html")
CHECK = "--check" in sys.argv

START = "<!-- PAGE-NAV-START -->"
END = "<!-- PAGE-NAV-END -->"
# remove any previously injected block (idempotent re-runs)
BLOCK_RE = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)

# Pull ordered (href, title) for lesson pages from index.html.
# Lesson pages live under course-orientation/, course-introduction/, or week-N/.
# IMPORTANT: only match links inside the structured lesson list (<li><a ...>),
# so banner/intro links (e.g. "full AI content disclaimer", about.html) are
# excluded and do not pollute the sequence or its ordering.
LINK_RE = re.compile(
    r'<li\b[^>]*>\s*<a\b[^>]*\bhref="((?:course-orientation|course-introduction|week-\d+)/[^"]+\.html)"[^>]*>(.*?)</a>',
    re.IGNORECASE | re.DOTALL,
)

def clean_title(raw):
    t = re.sub(r"<[^>]+>", "", raw)            # strip any inner tags
    t = html.unescape(t).strip()
    t = re.sub(r"\s+", " ", t)
    return t

def build_order():
    with open(INDEX, encoding="utf-8") as f:
        idx = f.read()
    seen, order = set(), []
    for m in LINK_RE.finditer(idx):
        href, title = m.group(1), clean_title(m.group(2))
        if href not in seen:
            seen.add(href)
            order.append((href, title))
    return order

def nav_html(prev_item, next_item):
    link_style = ("flex:1 1 240px;text-decoration:none;display:block;padding:14px 18px;"
                  "border:1px solid #d0e0ee;border-radius:12px;background:#f8fbff;"
                  "color:#003A70;transition:background .2s,color .2s;")
    def cell(item, direction):
        href, title = item
        align = "left" if direction == "prev" else "right"
        label = "&#8592; Previous" if direction == "prev" else "Next &#8594;"
        # every lesson page sits one directory deep under docs/, so the
        # index-relative href becomes page-relative with a single "../"
        return (
            f'<a class="page-nav-link" href="../{html.escape(href)}" '
            f'style="{link_style}text-align:{align};">'
            f'<div style="font-size:.78em;text-transform:uppercase;letter-spacing:.5px;'
            f'color:#8a99a8;margin-bottom:3px;">{label}</div>'
            f'<div style="font-weight:600;font-size:.97em;line-height:1.35;">'
            f'{html.escape(title)}</div></a>'
        )
    spacer = '<span style="flex:1 1 240px;"></span>'
    left = cell(prev_item, "prev") if prev_item else spacer
    right = cell(next_item, "next") if next_item else spacer
    return (
        f"{START}\n"
        '<style>.page-nav-link:hover{background:#003A70 !important;}'
        '.page-nav-link:hover *{color:#ffffff !important;}</style>\n'
        '<nav class="page-nav" aria-label="Lesson navigation" '
        "style=\"max-width:1200px;margin:28px auto 0;padding:0 40px;display:flex;"
        'flex-wrap:wrap;justify-content:space-between;gap:16px;'
        "font-family:'Lato',sans-serif;\">\n"
        f"  {left}\n  {right}\n</nav>\n{END}"
    )

def inject(content, block):
    content = BLOCK_RE.sub("", content)        # strip prior block if present
    # prefer to sit just above the page footer; else just before </body>
    idx = content.rfind("<footer")
    if idx == -1:
        idx = content.rfind("</body>")
    if idx == -1:
        return None
    return content[:idx] + block + "\n" + content[idx:]

def main():
    order = build_order()
    print(f"Lessons in sequence (from index.html): {len(order)}")
    injected = skipped = 0
    notes = []
    for i, (href, title) in enumerate(order):
        path = os.path.join(DOCS, href)
        if not os.path.exists(path):
            skipped += 1; notes.append(f"  MISSING file, skipped: {href}"); continue
        prev_item = order[i-1] if i > 0 else None
        next_item = order[i+1] if i < len(order)-1 else None
        block = nav_html(prev_item, next_item)
        with open(path, encoding="utf-8") as f:
            c = f.read()
        new = inject(c, block)
        if new is None:
            skipped += 1; notes.append(f"  NO footer/</body> anchor, skipped: {href}"); continue
        if not CHECK:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new)
        injected += 1
    print(f"{'Would inject' if CHECK else 'Injected'} nav into: {injected} pages")
    print(f"Skipped: {skipped}")
    for n in notes:
        print(n)
    # show first/last sequence entries as a sanity check
    if order:
        print("\nFirst in chain:", order[0][1], "->", order[0][0])
        print("Last in chain: ", order[-1][1], "->", order[-1][0])

if __name__ == "__main__":
    main()
