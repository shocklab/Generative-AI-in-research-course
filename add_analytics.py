#!/usr/bin/env python3
"""
add_analytics.py — inject a privacy-friendly GoatCounter analytics snippet
into every page of the docs/ live site (GitHub Pages).

Marker-wrapped (<!-- ANALYTICS-START/END -->) so re-runs are idempotent,
mirroring add_page_nav.py and scorm/add_scorm_hooks.py. Re-run after any
rebuild that regenerates pages.

The snippet is injected into docs/ ONLY. It is deliberately NOT added to
the Amathuba 'Week N/' copies, and build_scorm.py strips it from the SCORM
packages — pages served inside the LMS must not phone home to an external
analytics service. GoatCounter is cookieless and collects no personal
data, so no cookie-consent banner is required.

Usage:
    python3 add_analytics.py --code YOURCODE          # inject (YOURCODE.goatcounter.com)
    python3 add_analytics.py --code YOURCODE --strip  # remove the snippet
"""
import os, re, sys, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(HERE, "docs")

START = "<!-- ANALYTICS-START -->"
END = "<!-- ANALYTICS-END -->"
BLOCK_RE = re.compile(r"\n*" + re.escape(START) + r".*?" + re.escape(END) + r"\n*", re.DOTALL)


def snippet(code):
    return (
        f"{START}\n"
        f'<script data-goatcounter="https://{code}.goatcounter.com/count" '
        f'async src="//gc.zgo.at/count.js"></script>\n'
        f"{END}"
    )


def inject(content, block):
    # strip any prior block first (byte-idempotent across re-runs)
    content = BLOCK_RE.sub("\n", content)
    idx = content.rfind("</body>")
    if idx == -1:
        return None
    return content[:idx].rstrip("\n") + "\n" + block + "\n" + content[idx:]


def strip(content):
    return BLOCK_RE.sub("\n", content)


def gather():
    """Every .html under docs/ — the whole live site."""
    out = []
    for dirpath, _dirs, files in os.walk(DOCS):
        for f in sorted(files):
            if f.endswith(".html"):
                out.append(os.path.join(dirpath, f))
    return sorted(out)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--code", default="", help="GoatCounter site code (the X in X.goatcounter.com)")
    p.add_argument("--strip", action="store_true", help="remove the snippet instead of injecting")
    args = p.parse_args()

    if not args.strip and not args.code:
        print("Provide --code YOURCODE — the subdomain of your GoatCounter dashboard "
              "(X in X.goatcounter.com).", file=sys.stderr)
        sys.exit(2)

    block = None if args.strip else snippet(args.code)
    files = gather()
    n = 0
    for path in files:
        with open(path, encoding="utf-8") as f:
            c = f.read()
        new = strip(c) if args.strip else inject(c, block)
        if new is None:
            print(f"  no </body> in {os.path.relpath(path, HERE)}, skipped")
            continue
        if new != c:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new)
            n += 1
    action = "Stripped" if args.strip else "Injected"
    print(f"{action} analytics in {n}/{len(files)} docs pages.")


if __name__ == "__main__":
    main()
