#!/usr/bin/env python3
"""Reusable SVG diagram library for MAM5020F lessons (the Press house style).

Every function returns a complete, self-contained <svg> string:
  - light-blue panel (#ebf1f8) + soft border, UCT palette
  - Fraunces titles, Newsreader body
  - presentation attributes only (no style="" — build_site.py strips those)
Wrap each result in <figure class="diagram"><svg/><figcaption/></figure>.
"""
import re

FT = "'Fraunces',Georgia,serif"
FB = "'Newsreader',Georgia,serif"
PANEL, PANEL_BD = "#ebf1f8", "#c4d3e6"

# tint fill, stroke, text  — for soft cells
TINT = {
    'accent':  ('#d6e3f2', '#9fb8d6', '#003A70'),
    'good':    ('#e7efe8', '#8fb09a', '#2c6e3f'),
    'bad':     ('#f3e3df', '#c08a82', '#9a2f2f'),
    'warn':    ('#f7efe0', '#cdab6a', '#7c5c12'),
    'neutral': ('#fffdf8', '#d8cfbd', '#3f3a32'),
}
# strong solid header fills (white text)
HEAD = {'accent': '#003A70', 'good': '#2c6e3f', 'bad': '#9a2f2f',
        'warn': '#7c5c12', 'neutral': '#5b5446', 'alt': '#2a5298'}


ARROW = ('<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" '
         'orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" '
         'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>')


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def wrap(text, max_chars):
    words, lines, cur = str(text).split(), [], ''
    for w in words:
        if cur and len(cur) + 1 + len(w) > max_chars:
            lines.append(cur); cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        lines.append(cur)
    return lines or ['']


def _svg(w, h, title, desc, body):
    return (f'<svg width="100%" viewBox="0 0 {w} {h}" role="img" xmlns="http://www.w3.org/2000/svg">'
            f'<title>{esc(title)}</title><desc>{esc(desc)}</desc>'
            f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="3" fill="{PANEL}" stroke="{PANEL_BD}"/>'
            f'{body}</svg>')


_SIZE_SNAP = {11.5: 12, 12.5: 12, 13.5: 13, 14.5: 14, 15: 15.5, 16: 15.5}

def _txt(x, y, s, size, fill, fam=FB, anchor='start', weight=None, italic=False):
    size = _SIZE_SNAP.get(size, size)
    w = f' font-weight="{weight}"' if weight else ''
    it = ' font-style="italic"' if italic else ''
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{fam}" '
            f'font-size="{size}" fill="{fill}"{w}{it}>{esc(s)}</text>')


# ---------------------------------------------------------------- vtimeline
def vtimeline(rows, title, desc, legend=None):
    """rows: list of (label, [(text, kind), ...]). Label sits above its cell(s);
    a spine of dots runs down the left. Robust to long labels."""
    W = 680
    top = 58 if legend else 32
    y = top
    seg = []
    if legend:
        lx = 66
        for txt, kind in legend:
            f, s, t = TINT[kind]
            seg.append(f'<rect x="{lx:.0f}" y="20" width="15" height="15" rx="3" fill="{f}" stroke="{s}"/>')
            seg.append(_txt(lx + 22, 32, txt, 13, t))
            lx += 30 + 8.6 * len(txt)
    spine_top = top - 6
    for label, cells in rows:
        seg.append(f'<circle cx="44" cy="{y+11:.0f}" r="6" fill="#003A70"/>')
        seg.append(_txt(66, y + 15, label, 14, '#003A70', FT, 'start', 500))
        cy = y + 24
        for text, kind in cells:
            f, s, t = TINT[kind]
            seg.append(f'<rect x="66" y="{cy:.0f}" width="570" height="30" rx="8" fill="{f}" stroke="{s}"/>')
            seg.append(_txt(80, cy + 20, text, 13.5, t))
            cy += 34
        y = cy + 10
    spine = f'<line x1="44" y1="{spine_top}" x2="44" y2="{int(y-10)}" stroke="#a9bcd4" stroke-width="2"/>'
    return _svg(W, int(y + 6), title, desc, spine + ''.join(seg))


# ---------------------------------------------------------------- vflow
def vflow(steps, title, desc):
    """steps: list of (text, kind). Vertical sequence of boxes with down-arrows."""
    W, bx, bw, gap = 680, 130, 420, 22
    y = 30
    boxes, ys = [], []
    for text, kind in steps:
        f, s, t = TINT[kind]
        lines = wrap(text, int((bw - 28) / 6.6))
        bh = 12 + len(lines) * 17 + 4
        b = f'<rect x="{bx}" y="{y}" width="{bw}" height="{bh}" rx="9" fill="{f}" stroke="{s}"/>'
        for i, ln in enumerate(lines):
            b += _txt(bx + bw / 2, y + 20 + i * 17, ln, 13.5, t, FB, 'middle')
        boxes.append(b); ys.append((y, y + bh))
        y += bh + gap
    arrows = ''
    for i in range(len(ys) - 1):
        arrows += (f'<line x1="340" y1="{ys[i][1]}" x2="340" y2="{ys[i+1][0]}" '
                   f'stroke="#6a6256" stroke-width="2" marker-end="url(#arrow)"/>')
    return _svg(W, int(ys[-1][1] + 10), title, desc, ARROW + arrows + ''.join(boxes))


# ---------------------------------------------------------------- tree
def tree(top, branches, title, desc):
    """top: str root label. branches: list of dict(title, sub, kind, action)."""
    W = 680
    n = len(branches)
    cxs = [120 + i * (440 / (n - 1)) for i in range(n)] if n > 1 else [340]
    rw = max(180, len(top) * 7.8 + 30)
    seg = [ARROW, f'<rect x="{340 - rw/2:.0f}" y="46" width="{rw:.0f}" height="44" rx="8" fill="#003A70"/>',
           _txt(340, 73, top, 14.5, '#ffffff', FT, 'middle', 500)]
    for cx, b in zip(cxs, branches):
        f, s, t = TINT[b['kind']]
        x = cx - 100
        seg.append(f'<line x1="340" y1="90" x2="{cx:.0f}" y2="148" stroke="#6a6256" stroke-width="2" marker-end="url(#arrow)"/>')
        seg.append(f'<rect x="{x:.0f}" y="150" width="200" height="56" rx="8" fill="{f}" stroke="{s}"/>')
        seg.append(_txt(cx, 174, b['title'], 15, t, FT, 'middle', 500))
        seg.append(_txt(cx, 192, b['sub'], 12.5, '#6a6256', FB, 'middle'))
        seg.append(f'<line x1="{cx:.0f}" y1="206" x2="{cx:.0f}" y2="250" stroke="#6a6256" stroke-width="2" marker-end="url(#arrow)"/>')
        seg.append(f'<rect x="{x:.0f}" y="250" width="200" height="46" rx="8" fill="#d6e3f2" stroke="#9fb8d6"/>')
        seg.append(_txt(cx, 278, b['action'], 13.5, '#003A70', FT, 'middle', 500))
    return _svg(W, 322, title, desc, ''.join(seg))


# ---------------------------------------------------------------- barchart
def barchart(bars, title, desc, unit='', threshold=None, thresh_label=''):
    """bars: list of (label, value, kind). Horizontal bars, value labelled at the end."""
    W, lx, bx, barmax, rh = 680, 184, 200, 356, 30
    vmax = max(v for _, v, _ in bars) * 1.18
    y = 44
    seg = []
    for label, value, kind in bars:
        f, s, t = TINT[kind]
        seg.append(_txt(lx, y + 19, label, 13, '#3f3a32', FB, 'end'))
        bw = (value / vmax) * barmax
        seg.append(f'<rect x="{bx}" y="{y+5}" width="{bw:.0f}" height="19" rx="4" fill="{f}" stroke="{s}"/>')
        seg.append(_txt(bx + bw + 8, y + 19, f"{value}{unit}", 12.5, t, FB, 'start', 500))
        y += rh
    if threshold is not None:
        tx = bx + (threshold / vmax) * barmax
        seg.insert(0, f'<line x1="{tx:.0f}" y1="38" x2="{tx:.0f}" y2="{y}" stroke="#9a2f2f" stroke-width="1.5" stroke-dasharray="4 4"/>')
        seg.append(_txt(tx, y + 16, thresh_label, 11.5, '#9a2f2f', FB, 'middle', None, True))
        y += 22
    return _svg(W, int(y + 14), title, desc, ''.join(seg))


# ---------------------------------------------------------------- linechart
def linechart(series, xlabels, title, desc, ylabel='', note='', yticks=None):
    """series: list of dict(label, color, pts=[(t,v)...], above=bool,
    marks=[(t,v,text,pos)]) with t,v in [0,1]; pos in above/right/left/ar.
    yticks: [(v, label), ...] draws dashed gridlines with left labels.
    Single-series charts get no on-curve label (the caption names it);
    use marks to annotate the values that carry the message."""
    W, x0, x1, y0, y1 = 680, 90, 604, 70, 300
    def X(t): return x0 + t * (x1 - x0)
    def Y(v): return y1 - v * (y1 - y0)
    seg = []
    for v, lab in (yticks or []):
        yy = Y(v)
        if v > 0.01:
            seg.append(f'<line x1="{x0}" y1="{yy:.0f}" x2="{x1}" y2="{yy:.0f}" stroke="#d3deec" stroke-width="1" stroke-dasharray="3 5"/>')
        seg.append(_txt(x0 - 10, yy + 4, lab, 12, '#6a6256', FB, 'end'))
    seg.append(f'<line x1="{x0}" y1="58" x2="{x0}" y2="{y1}" stroke="#c4d3e6" stroke-width="1.5"/>')
    seg.append(f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="#c4d3e6" stroke-width="1.5"/>')
    if ylabel:
        seg.append(_txt(x0 + 8, 64, ylabel, 11.5, '#6a6256'))
    multi = len(series) > 1
    for sr in series:
        pts = ' '.join(f"{X(t):.0f},{Y(v):.0f}" for t, v in sr['pts'])
        c = sr['color']
        seg.append(f'<polyline points="{pts}" fill="none" stroke="{c}" stroke-width="2.5"/>')
        if multi and sr.get('label'):
            lt, lv = sr['pts'][-1]
            seg.append(f'<circle cx="{X(lt):.0f}" cy="{Y(lv):.0f}" r="4" fill="{c}"/>')
            ly = Y(lv) - 10 if sr.get('above', True) else Y(lv) + 20
            seg.append(_txt(X(lt), ly, sr['label'], 14, c, FT, 'end', 500))
        for t, v, lab, pos in sr.get('marks', []):
            mx, my = X(t), Y(v)
            seg.append(f'<circle cx="{mx:.0f}" cy="{my:.0f}" r="4.5" fill="{c}"/>')
            if pos == 'right':
                seg.append(_txt(mx + 10, my + 5, lab, 13, c, FT, 'start', 500))
            elif pos == 'left':
                seg.append(_txt(mx - 10, my + 5, lab, 13, c, FT, 'end', 500))
            elif pos == 'ar':
                seg.append(_txt(mx + 8, my - 6, lab, 13, c, FT, 'start', 500))
            else:
                seg.append(_txt(mx, my - 12, lab, 13, c, FT, 'middle', 500))
    for t, lab in xlabels:
        anchor = 'start' if t < 0.1 else ('end' if t > 0.9 else 'middle')
        seg.append(_txt(X(t), y1 + 18, lab, 12, '#6a6256', FB, anchor))
    if note:
        seg.append(_txt((x0 + x1) / 2, y1 + 44, note, 11.5, '#736a5c', FB, 'middle', None, True))
    return _svg(W, 380 if note else 352, title, desc, ''.join(seg))


# ---------------------------------------------------------------- filetree
def filetree(rows, title, desc, note_x=302):
    """rows: list of (name, note, depth). A folder/file listing with a note per row."""
    W, mx, rowh = 680, 24, 32
    y = 34
    seg = []
    for i, (name, note, depth) in enumerate(rows):
        fill = '#ffffff' if i % 2 == 0 else '#f3f6fb'
        seg.append(f'<rect x="{mx}" y="{y}" width="{W-2*mx}" height="{rowh}" fill="{fill}" stroke="#e2e8f2"/>')
        x = mx + 14 + depth * 22
        seg.append(f'<rect x="{x}" y="{y+11}" width="11" height="9" rx="1.5" fill="#003A70"/>')
        seg.append(_txt(x + 18, y + 21, name, 13, '#003A70', FT, 'start', 500))
        seg.append(_txt(mx + note_x, y + 21, note, 12.5, '#6a6256', FB, 'start'))
        y += rowh
    return _svg(W, int(y + 14), title, desc, ''.join(seg))


# ---------------------------------------------------------------- cycle
def cycle(nodes, title, desc, center=None, node_kind='accent', center_kind='warn', arrow='#6a6256'):
    """nodes: 4 dict(title, sub) clockwise from top-left. center: optional dict(title, sub)."""
    pos = [(70, 70), (400, 70), (400, 300), (70, 300)]
    seg = [ARROW,
           f'<line x1="286" y1="103" x2="394" y2="103" stroke="{arrow}" stroke-width="2" marker-end="url(#arrow)"/>',
           f'<line x1="505" y1="142" x2="505" y2="294" stroke="{arrow}" stroke-width="2" marker-end="url(#arrow)"/>',
           f'<line x1="394" y1="333" x2="286" y2="333" stroke="{arrow}" stroke-width="2" marker-end="url(#arrow)"/>',
           f'<line x1="175" y1="294" x2="175" y2="142" stroke="{arrow}" stroke-width="2" marker-end="url(#arrow)"/>']
    for (x, y), nd in zip(pos, nodes):
        f, s, t = TINT[node_kind]
        seg.append(f'<rect x="{x}" y="{y}" width="210" height="66" rx="10" fill="{f}" stroke="{s}" stroke-width="1.5"/>')
        seg.append(_txt(x + 105, y + 28, nd['title'], 15.5, t, FT, 'middle', 500))
        seg.append(_txt(x + 105, y + 48, nd['sub'], 13, '#6a6256', FB, 'middle'))
    if center:
        f, s, t = TINT[center_kind]
        seg.append(f'<rect x="235" y="185" width="210" height="66" rx="10" fill="{f}" stroke="{s}" stroke-width="1.5"/>')
        seg.append(_txt(340, 213, center['title'], 15.5, t, FT, 'middle', 500))
        seg.append(_txt(340, 233, center['sub'], 13, '#6a6256', FB, 'middle'))
    return _svg(680, 406, title, desc, ''.join(seg))


# ---------------------------------------------------------------- hubspoke
def hubspoke(center, spokes, title, desc):
    """center: dict(title, sub). spokes: list of dict(title, sub) placed top, right, bottom, left."""
    place = [(255, 50), (470, 181), (255, 312), (40, 181)]
    conn = ['<line x1="340" y1="178" x2="340" y2="108" stroke="#6a6256" stroke-width="1.8" marker-end="url(#arrow)"/>',
            '<line x1="415" y1="210" x2="470" y2="210" stroke="#6a6256" stroke-width="1.8" marker-end="url(#arrow)"/>',
            '<line x1="340" y1="242" x2="340" y2="312" stroke="#6a6256" stroke-width="1.8" marker-end="url(#arrow)"/>',
            '<line x1="265" y1="210" x2="210" y2="210" stroke="#6a6256" stroke-width="1.8" marker-end="url(#arrow)"/>']
    seg = [ARROW]
    for i, sp in enumerate(spokes[:4]):
        seg.append(conn[i])
    for i, sp in enumerate(spokes[:4]):
        x, y = place[i]
        f, s, t = TINT['accent']
        seg.append(f'<rect x="{x}" y="{y}" width="170" height="58" rx="10" fill="{f}" stroke="{s}"/>')
        seg.append(_txt(x + 85, y + 24, sp['title'], 14.5, t, FT, 'middle', 500))
        seg.append(_txt(x + 85, y + 42, sp['sub'], 12, '#45556b', FB, 'middle'))
    seg.append('<rect x="265" y="178" width="150" height="64" rx="10" fill="#003A70"/>')
    seg.append(_txt(340, 205, center['title'], 15.5, '#ffffff', FT, 'middle', 500))
    seg.append(_txt(340, 225, center['sub'], 12, '#c9d9ec', FB, 'middle'))
    return _svg(680, 398, title, desc, ''.join(seg))


# ---------------------------------------------------------------- spectrum
def spectrum(stops, title, desc, lo='lower', hi='higher'):
    """stops: list of (label, kind) left-to-right. A coloured band with labels below."""
    W = 680
    x0, x1 = 40, 640
    n = len(stops)
    sw = (x1 - x0) / n
    seg = [ARROW,
           _txt(x0, 40, lo, 12.5, '#6a6256', FB, 'start', None, True),
           _txt(x1, 40, hi, 12.5, '#6a6256', FB, 'end', None, True),
           f'<line x1="{x0}" y1="46" x2="{x1}" y2="46" stroke="#9fb8d6" stroke-width="2" marker-end="url(#arrow)"/>']
    maxlines = 1
    for i, (label, kind) in enumerate(stops):
        f, s, t = TINT[kind]
        x = x0 + i * sw
        seg.append(f'<rect x="{x+3:.0f}" y="54" width="{sw-6:.0f}" height="30" rx="6" fill="{f}" stroke="{s}"/>')
        lines = wrap(label, int((sw - 10) / 6.4))
        maxlines = max(maxlines, len(lines))
        for k, ln in enumerate(lines):
            seg.append(_txt(x + sw / 2, 104 + k * 15, ln, 12, t, FB, 'middle'))
    return _svg(W, int(104 + maxlines * 15 + 14), title, desc, ''.join(seg))


# ---------------------------------------------------------------- columns
def columns(cols, title, desc, intro_h=0):
    """cols: list of dict(title, kind, lines=[str,...]). Header box + dash lines."""
    W = 680
    n = len(cols)
    mx, gap = 26, 22
    cw = (W - 2 * mx - (n - 1) * gap) / n
    chars = int((cw - 26) / 6.2)
    top = 30
    headh = 40
    # measure tallest column
    maxlines = 0
    wrapped = []
    for c in cols:
        ws = [wrap(ln, chars) for ln in c['lines']]
        wrapped.append(ws)
        maxlines = max(maxlines, sum(len(w) + 0.7 for w in ws))
    body = []
    for i, c in enumerate(cols):
        x = mx + i * (cw + gap)
        hc = HEAD.get(c['kind'], '#003A70')
        body.append(f'<rect x="{x:.0f}" y="{top}" width="{cw:.0f}" height="{headh}" rx="9" fill="{hc}"/>')
        for tl in wrap(c['title'], int((cw - 16) / 7.4))[:2]:
            body.append(_txt(x + cw / 2, top + 26, c['title'], 14.5, '#ffffff', FT, 'middle', 500))
            break
        yy = top + headh + 24
        for ws in wrapped[i]:
            body.append(f'<circle cx="{x+12:.0f}" cy="{yy-4:.0f}" r="2.5" fill="#6a6256"/>')
            for k, ln in enumerate(ws):
                body.append(_txt(x + 22, yy + k * 17, ln, 13, '#3f3a32'))
            yy += len(ws) * 17 + 12
    h = int(top + headh + 24 + maxlines * 17 + 24)
    return _svg(W, h, title, desc, ''.join(body))


# ---------------------------------------------------------------- matrix
def matrix(col_headers, rows, title, desc, label_w=120):
    """col_headers: [str,...]; rows: [(rowlabel, [cell,...]), ...]."""
    W = 680
    mx = 24
    nc = len(col_headers)
    cw = (W - 2 * mx - label_w) / nc
    chars = int((cw - 20) / 6.0)
    top = 30
    headh = 36
    # row heights from wrapped cells
    rowys = []
    y = top + headh
    body = []
    # header row
    body.append(f'<rect x="{mx}" y="{top}" width="{W-2*mx}" height="{headh}" rx="8" fill="#003A70"/>')
    for j, ch in enumerate(col_headers):
        cx = mx + label_w + j * cw + 12
        body.append(_txt(cx, top + 23, ch, 13.5, '#ffffff', FT, 'start', 500))
    for ri, (rlabel, cells) in enumerate(rows):
        wrapped = [wrap(c, chars) for c in cells]
        lines = max(len(w) for w in wrapped)
        rh = 12 + lines * 17 + 8
        fill = '#ffffff' if ri % 2 == 0 else '#f3f6fb'
        body.append(f'<rect x="{mx}" y="{y:.0f}" width="{W-2*mx}" height="{rh:.0f}" fill="{fill}" stroke="#d7e0ec"/>')
        body.append(_txt(mx + 14, y + 22, rlabel, 13.5, '#003A70', FT, 'start', 500))
        for j, ws in enumerate(wrapped):
            cx = mx + label_w + j * cw + 12
            for k, ln in enumerate(ws):
                body.append(_txt(cx, y + 22 + k * 17, ln, 12.5, '#3f3a32'))
        y += rh
    h = int(y + 20)
    return _svg(W, h, title, desc, ''.join(body))
