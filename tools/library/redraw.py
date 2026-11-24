"""Redraw single symbols after changing their drawing in glyphs.py / glyphs_extra.py.
Usage: python3 tools/library/redraw.py <pack folder> <symbol id> [<symbol id> ...]
Renders -off and -on (with and without background, all 15 themes) for the symbol and its badge
variants, palette-optimises them like optimize_png.py, and refreshes the plain <id>.png files
from the Off drawing. File names and icons.json stay unchanged."""
import sys, os, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import *
from sheet import pal_from
from PIL import Image
from playwright.sync_api import sync_playwright

P = sys.argv[1].rstrip('/') + '/'
ids = sys.argv[2:]
want = {}
for i in ids:
    assert i in G, f'unknown symbol {i}'
    for cid, g in items():
        if cid == i or cid in [f'{i}-{v}' for v in VARIANTS.get(i, [])]:
            want[cid] = (i, g)

def save(png_bytes, path):
    im = Image.open(io.BytesIO(png_bytes)).convert('RGBA')
    im.quantize(colors=64, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE).save(path, 'PNG', optimize=True)

n = 0
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 144, 'height': 144})
    for s, sn, sd in SEAS:
        for m, mn, md in MODES:
            c = pal_from(P, s, m)
            for cid, (base_id, g) in want.items():
                for st, stn, sty in STATES:
                    for clear in (False, True):
                        suffix = '-clear' if clear else ''
                        pg.set_content(f'<body style="margin:0;background:transparent">{svg(g, st, c, clear)}</body>')
                        data = pg.screenshot(omit_background=True)
                        save(data, f'{P}icons/{s}-{m}-{cid}-{st}{suffix}.png'); n += 1
                        if st == 'off' and cid == base_id:
                            save(data, f'{P}icons/{s}-{m}-{cid}{suffix}.png'); n += 1
    b.close()
print('written', n, 'files for', ', '.join(want))
