"""Marketplace gallery images 3 and 4 (1920x960), built from the pack's own PNGs.
Usage: python3 tools/library/gallery.py   (run from the repository root)"""
import base64, json, os
from playwright.sync_api import sync_playwright

PACK = 'uk.novaroma-homelab.season-icons.sdIconPack'
entries = json.load(open(f'{PACK}/icons.json'))
total = len(entries)
# toggle symbols = library concepts: one Off file per concept for a single theme, with background
toggle_symbols = sum(1 for e in entries if 'Library' in e['tags'] and e['path'].startswith('standard-dark-')
                     and e['path'].endswith('-off.png'))

def uri(theme, cid, state):
    path = f'{PACK}/icons/{theme}-{cid}-{state}.png'
    assert os.path.exists(path), path
    return 'data:image/png;base64,' + base64.b64encode(open(path, 'rb').read()).decode()

def grid(theme, symbols, size, gap, label_col):
    cells = lambda st: ''.join(f'<img src="{uri(theme, c, st)}" style="width:{size}px;height:{size}px">' for c, _ in symbols)
    labels = ''.join(f'<div style="width:{size}px;text-align:center">{n}</div>' for _, n in symbols)
    cap = lambda t: f'<div style="font-size:26px;color:{label_col};margin:26px 0 10px">{t}</div>'
    row = lambda inner, extra='': f'<div style="display:flex;gap:{gap}px;{extra}">{inner}</div>'
    return (cap('Off') + row(cells('off')) + cap('On') + row(cells('on')) +
            row(labels, f'margin-top:14px;font-size:22px;color:{label_col}'))

def page(bg, fg, sub, title, subtitle, body):
    return f'''<html><body style="margin:0;width:1920px;height:960px;background:{bg};color:{fg};
font-family:'Liberation Serif','DejaVu Serif',serif;position:relative">
<div style="position:absolute;left:90px;top:100px;font-size:78px;font-weight:bold">{title}</div>
<div style="position:absolute;left:90px;top:206px;font-size:34px;color:{sub}">{subtitle}</div>
<div style="position:absolute;left:90px;top:290px">{body}</div></body></html>'''

g3_syms = [('light-bulb', 'Light bulb'), ('spot-light', 'Spot light'), ('desk-lamp', 'Desk lamp'), ('key-light', 'Key light'),
           ('ring-light', 'Ring light'), ('light-strip', 'LED strip'), ('microphone', 'Microphone'), ('webcam', 'Webcam')]
g4_syms = [('light-bulb', 'Bulb'), ('spot-light', 'Spot'), ('downlight', 'Downlight'), ('cabinet-light', 'Cabinet'),
           ('light-strip', 'LED strip'), ('key-light', 'Key light'), ('ring-light', 'Ring'), ('desk-lamp', 'Desk'),
           ('floor-lamp', 'Floor'), ('pendant-light', 'Pendant'), ('lantern', 'Lantern'), ('candle', 'Candle')]

classic = ['arch','bell','book','bolt','calendar','camera','chat','clock','cloud','code','coffee','database','gamepad','gear','globe',
           'gradcap','headphones','heart','home','key','laptop','lock','mail','mic','monitor','moon','music','network','phone','play',
           'power','rocket','search','server','shield','star','sun','terminal','trash','tv','video','volume','wifi','wrench']
def classic_grid(theme):
    img = lambda c: f'<img src="{uri_plain(theme, c)}" style="width:96px;height:96px">'
    rows = [classic[i:i + 15] for i in range(0, len(classic), 15)]
    return ''.join(f'<div style="display:flex;gap:22px;margin-bottom:22px">{"".join(img(c) for c in r)}</div>' for r in rows)

def uri_plain(theme, cid):
    path = f'{PACK}/icons/{theme}-{cid}.png'
    assert os.path.exists(path), path
    return 'data:image/png;base64,' + base64.b64encode(open(path, 'rb').read()).decode()

pages = {
 'gallery-2-symbols.png': page('#1a0f0f', '#f6efe3', '#d9ccbd', '120 classic symbols',
     'System, development, media, audio, streaming and study, in every season and colour theme',
     classic_grid('sommer-dark')),
 'gallery-3-toggle-symbols.png': page('#1a0f0f', '#f6efe3', '#d9ccbd', f'{toggle_symbols} toggle symbols',
     'Every symbol as outline Off and filled On, in 15 colour themes, with and without background',
     grid('herbst-dark', g3_syms, 170, 40, '#d9ccbd')),
 'gallery-4-lights.png': page('#f6efe3', '#2a1414', '#5a4040', 'Lights that glow when on',
     'Spot light, downlight, cabinet light, LED strip, key light, ring light, lamps and more',
     grid('winter-light', g4_syms, 120, 32, '#5a4040')),
}
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1920, 'height': 960})
    for name, html in pages.items():
        pg.set_content(html); pg.screenshot(path=f'marketplace/{name}')
    b.close()
print('galleries written;', toggle_symbols, 'toggle symbols,', total, 'icons')
