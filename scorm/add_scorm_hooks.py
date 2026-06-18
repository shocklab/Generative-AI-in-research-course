#!/usr/bin/env python3
"""
add_scorm_hooks.py — inject a SCORM 1.2 page-completion script tag into
selected lesson pages in docs/.

The script tag points at scorm-api.js (which lives alongside this file).
It is wrapped in <!-- SCORM-HOOK-START / END --> markers so re-runs are
idempotent.

Designed to mirror add_page_nav.py: same source-of-truth, same injection
pattern, same idempotency guarantee. Re-run safely after any rebuild.

Usage:
    python3 scorm/add_scorm_hooks.py                  # inject across docs/week-1/ (default prototype)
    python3 scorm/add_scorm_hooks.py --week 1         # explicit
    python3 scorm/add_scorm_hooks.py --all            # all weeks + index
    python3 scorm/add_scorm_hooks.py --strip          # remove hooks (revert)
"""
import os, re, sys, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOCS = os.path.join(ROOT, "docs")

START = "<!-- SCORM-HOOK-START -->"
END = "<!-- SCORM-HOOK-END -->"
BLOCK_RE = re.compile(r"\n*" + re.escape(START) + r".*?" + re.escape(END) + r"\n*", re.DOTALL)


def hook_block(rel_depth):
    """Return the inject-able script block.

    `rel_depth` is how many '../' steps to walk from the lesson page back to
    the package root (where scorm-api.js will sit). Lessons under docs/week-N/
    are one level deep, so they use '../scorm-api.js'.
    """
    rel = "../" * rel_depth + "scorm-api.js"
    return (
        f"{START}\n"
        f'<script src="{rel}"></script>\n'
        f"{END}"
    )


def inject(content, block):
    # strip any prior block first (byte-idempotent across re-runs)
    content = BLOCK_RE.sub("\n", content)
    # inject just before </body>
    idx = content.rfind("</body>")
    if idx == -1:
        return None
    return content[:idx].rstrip("\n") + "\n" + block + "\n" + content[idx:]


def strip(content):
    return BLOCK_RE.sub("\n", content)


def gather_targets(week):
    """Return [(path, rel_depth)] for all lesson pages we want to hook."""
    targets = []
    if week is None or week == "all":
        weeks_dir_pattern = re.compile(r"^week-\d+$")
        for entry in sorted(os.listdir(DOCS)):
            sub = os.path.join(DOCS, entry)
            if weeks_dir_pattern.match(entry) and os.path.isdir(sub):
                for f in sorted(os.listdir(sub)):
                    if f.endswith(".html"):
                        targets.append((os.path.join(sub, f), 1))
        # course-orientation, course-introduction, and the advanced track sit alongside week-N
        for extra in ("course-orientation", "course-introduction", "advanced"):
            sub = os.path.join(DOCS, extra)
            if os.path.isdir(sub):
                for f in sorted(os.listdir(sub)):
                    if f.endswith(".html"):
                        targets.append((os.path.join(sub, f), 1))
        # the docs/index.html landing page itself
        idx = os.path.join(DOCS, "index.html")
        if os.path.exists(idx):
            targets.append((idx, 0))
    else:
        sub = os.path.join(DOCS, "advanced" if week == "advanced" else f"week-{week}")
        if not os.path.isdir(sub):
            print(f"  no such directory: {sub}", file=sys.stderr)
            sys.exit(2)
        for f in sorted(os.listdir(sub)):
            if f.endswith(".html"):
                targets.append((os.path.join(sub, f), 1))
    return targets


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--week", default="1", help="week number to hook (or 'all'); default = '1' for prototype")
    p.add_argument("--all", action="store_true", help="shortcut for --week all")
    p.add_argument("--strip", action="store_true", help="remove hooks instead of injecting")
    args = p.parse_args()

    week = "all" if args.all else args.week
    targets = gather_targets(week)
    if not targets:
        print("No target files found.", file=sys.stderr)
        sys.exit(2)

    action = "stripped" if args.strip else "injected"
    n = 0
    for path, depth in targets:
        with open(path, encoding="utf-8") as f:
            c = f.read()
        if args.strip:
            new = strip(c)
        else:
            new = inject(c, hook_block(depth))
        if new is None:
            print(f"  no </body> in {path}, skipped")
            continue
        if new != c:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new)
            n += 1
    print(f"{action.title()} hooks in {n}/{len(targets)} files (target: week {week}).")


if __name__ == "__main__":
    main()
