"""Baut die Novaroma-Bibliothek (An/Aus-Paare) ins Icon-Paket.
Aufruf: python3 build_lib.py <Paketordner> [Teil Anzahl]   (Teile = Jahreszeiten, parallel startbar)
Danach: python3 merge_lib.py <Paketordner>  (schreibt icons.json)"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import *
from sheet import pal_from
from playwright.sync_api import sync_playwright
P = sys.argv[1].rstrip('/') + '/'
part, parts = (int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) > 3 else (0, 1)
out = P + 'icons/'
its = items(); entries = []
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 144, "height": 144})
    for s, sn, sd in SEAS[part::parts]:
        for m, mn, md in MODES:
            c = pal_from(P, s, m)
            for cid, g in its:
                for st, stn, sty in STATES:
                    for clear in (False, True):
                        f = f'{s}-{m}-{cid}-{st}' + ('-clear' if clear else '') + '.png'
                        pg.set_content(f'<body style="margin:0;background:transparent">{svg(g, st, c, clear)}</body>')
                        pg.screenshot(path=out + f, omit_background=True)
                        nm = f'{g["name"]} {stn} ({sn} {mn}' + (', no background)' if clear else ')')
                        de = 'Aus' if st == 'off' else 'An'
                        tg = [g['name'], cid, sn, sd, mn, md, 'Season', 'Library', 'Toggle', stn, de, sty, g['grp']] + g['tags'] + (['No background', 'Transparent', 'Ohne Hintergrund'] if clear else [])
                        entries.append({"path": f, "name": nm, "tags": list(dict.fromkeys(tg))})
    b.close()
json.dump(entries, open(P + f'../.lib-entries-{part}.json', 'w'), ensure_ascii=False)
print(part, len(entries))
