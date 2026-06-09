#!/usr/bin/env python3
"""
build_scorm.py — package a portion of the course as a SCORM 1.2 ZIP.

Default: builds Week 1 only as the prototype. The ZIP is dropped into
scorm/dist/.

Behaviour:
  - Reads the curated lesson order from docs/index.html (the same source
    of truth used by add_page_nav.py and add_scorm_hooks.py).
  - Copies the relevant lesson HTML files, the docs/index.html landing
    page, and scorm/scorm-api.js into a staging directory.
  - Generates an imsmanifest.xml describing the lesson sequence as
    SCO items (SCORM 1.2, single organisation, flat structure).
  - Bundles in the three SCORM 1.2 XSD schema files (fetched on first
    run; cached locally in scorm/schemas/).
  - Zips everything as scorm/dist/mam5020f_<scope>_scorm12.zip.

Usage:
    python3 scorm/build_scorm.py            # prototype: Week 1 + index only
    python3 scorm/build_scorm.py --week 1   # explicit
    python3 scorm/build_scorm.py --all      # full course (when ready)
"""
import os, sys, re, html, shutil, zipfile, argparse, hashlib
import urllib.request, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOCS = os.path.join(ROOT, "docs")
DIST = os.path.join(HERE, "dist")
SCHEMAS = os.path.join(HERE, "schemas")
INDEX = os.path.join(DOCS, "index.html")
APIJS = os.path.join(HERE, "scorm-api.js")

# The three SCORM 1.2 XSD files referenced by the manifest. We embed
# placeholder content if the real schemas can't be downloaded so that
# the ZIP is still structurally valid for upload tests.
SCHEMA_URLS = {
    "imscp_rootv1p1p2.xsd": "https://www.imsglobal.org/xsd/imscp_rootv1p1p2.xsd",
    "imsmd_rootv1p2p1.xsd": "https://www.imsglobal.org/xsd/imsmd_rootv1p2p1.xsd",
    "adlcp_rootv1p2.xsd":   "https://www.adlnet.gov/xsd/adlcp_rootv1p2.xsd",
}


def clean_title(raw):
    t = re.sub(r"<[^>]+>", "", raw)
    t = html.unescape(t).strip()
    return re.sub(r"\s+", " ", t)


def read_index_chain(week):
    """Return ordered [(href, title)] for the requested scope, drawn from
    docs/index.html (the curated landing page)."""
    with open(INDEX, encoding="utf-8") as f:
        idx = f.read()
    link_re = re.compile(
        r'<li\b[^>]*>\s*<a\b[^>]*\bhref="((?:course-orientation|course-introduction|week-\d+)/[^"]+\.html)"[^>]*>(.*?)</a>',
        re.IGNORECASE | re.DOTALL,
    )
    seen, items = set(), []
    for m in link_re.finditer(idx):
        h, t = m.group(1), clean_title(m.group(2))
        if h in seen:
            continue
        seen.add(h)
        if week == "all":
            items.append((h, t))
        else:
            # restrict to the requested week-N/ prefix only (no orientation/intro)
            if h.startswith(f"week-{week}/"):
                items.append((h, t))
    return items


def ensure_schemas():
    os.makedirs(SCHEMAS, exist_ok=True)
    for name, url in SCHEMA_URLS.items():
        path = os.path.join(SCHEMAS, name)
        if os.path.exists(path) and os.path.getsize(path) > 0:
            continue
        try:
            print(f"  fetching schema: {name}")
            req = urllib.request.Request(url, headers={"User-Agent": "MAM5020F-scorm-build"})
            with urllib.request.urlopen(req, timeout=10) as r:
                data = r.read()
            with open(path, "wb") as f:
                f.write(data)
        except Exception as e:
            print(f"  WARN: could not fetch {name} ({e}); writing placeholder")
            with open(path, "w", encoding="utf-8") as f:
                f.write(f"<!-- placeholder; original schema at {url} -->\n")


def make_manifest(scope_label, items):
    """Render the SCORM 1.2 manifest XML."""
    pkg_id = "MAM5020F." + scope_label
    course_title = f"MAM5020F — {scope_label.replace('-', ' ').title()}"
    parts = []
    parts.append('<?xml version="1.0" encoding="UTF-8"?>')
    parts.append('<manifest identifier="' + pkg_id + '" version="1.0"')
    parts.append('  xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"')
    parts.append('  xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"')
    parts.append('  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
    parts.append('  xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd'
                 ' http://www.imsglobal.org/xsd/imsmd_rootv1p2p1 imsmd_rootv1p2p1.xsd'
                 ' http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd">')
    parts.append('  <metadata>')
    parts.append('    <schema>ADL SCORM</schema>')
    parts.append('    <schemaversion>1.2</schemaversion>')
    parts.append('  </metadata>')
    parts.append(f'  <organizations default="ORG-1">')
    parts.append(f'    <organization identifier="ORG-1">')
    parts.append(f'      <title>{html.escape(course_title)}</title>')
    for i, (href, title) in enumerate(items, start=1):
        ident = f"ITEM-{i:03d}"
        res_id = f"RES-{i:03d}"
        parts.append(f'      <item identifier="{ident}" identifierref="{res_id}" isvisible="true">')
        parts.append(f'        <title>{html.escape(title)}</title>')
        parts.append(f'      </item>')
    parts.append('    </organization>')
    parts.append('  </organizations>')
    parts.append('  <resources>')
    for i, (href, title) in enumerate(items, start=1):
        res_id = f"RES-{i:03d}"
        href_attr = html.escape(href, quote=True)
        parts.append(
            f'    <resource identifier="{res_id}" type="webcontent" '
            f'adlcp:scormtype="sco" href="{href_attr}">'
        )
        parts.append(f'      <file href="{href_attr}"/>')
        parts.append('    </resource>')
    parts.append('  </resources>')
    parts.append('</manifest>')
    return "\n".join(parts) + "\n"


def stage_files(stage, items):
    """Copy the lesson HTML files into the staging directory."""
    for href, _title in items:
        src = os.path.join(DOCS, href)
        if not os.path.exists(src):
            print(f"  WARN: missing source file {src}; skipped")
            continue
        dst = os.path.join(stage, href)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
    # include the landing page only when bundling more than a single week
    # (helps cross-page navigation inside the package without duplicating bytes)
    landing_src = os.path.join(DOCS, "index.html")
    if os.path.exists(landing_src):
        shutil.copy2(landing_src, os.path.join(stage, "index.html"))
    # SCORM API binding
    shutil.copy2(APIJS, os.path.join(stage, "scorm-api.js"))


def stage_schemas(stage):
    for name in SCHEMA_URLS:
        src = os.path.join(SCHEMAS, name)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(stage, name))


def zip_dir(stage, out_path):
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _dirs, files in os.walk(stage):
            for f in sorted(files):
                full = os.path.join(root, f)
                rel = os.path.relpath(full, stage)
                zf.write(full, rel)
    print(f"  wrote {out_path} ({os.path.getsize(out_path)/1024:.1f} KB)")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--week", default="1", help="week number to package (or 'all'); default = '1'")
    p.add_argument("--all", action="store_true", help="shortcut for --week all")
    args = p.parse_args()

    week = "all" if args.all else args.week
    scope = "course" if week == "all" else f"week{week}"
    items = read_index_chain(week)
    if not items:
        print(f"No lessons found for scope '{scope}'. Aborting.", file=sys.stderr)
        sys.exit(2)
    print(f"Scope: {scope} ({len(items)} lessons)")

    ensure_schemas()

    stage = os.path.join(DIST, f"_stage_{scope}")
    if os.path.exists(stage):
        shutil.rmtree(stage)
    os.makedirs(stage, exist_ok=True)

    stage_files(stage, items)
    stage_schemas(stage)

    # manifest
    manifest = make_manifest(scope, items)
    with open(os.path.join(stage, "imsmanifest.xml"), "w", encoding="utf-8") as f:
        f.write(manifest)

    # zip it
    out = os.path.join(DIST, f"mam5020f_{scope}_scorm12.zip")
    if os.path.exists(out):
        os.remove(out)
    zip_dir(stage, out)

    # clean up staging dir but keep the zip
    shutil.rmtree(stage)
    print("\nDone.")


if __name__ == "__main__":
    main()
