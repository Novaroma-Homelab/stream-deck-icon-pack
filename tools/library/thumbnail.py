"""Marketplace thumbnail (1920x960): title, icon count from icons.json, two rows of pack icons.
Usage: python3 tools/library/thumbnail.py   (run from the repository root)"""
import base64, json, os
from playwright.sync_api import sync_playwright

PACK = 'uk.novaroma-homelab.season-icons.sdIconPack'
TITLE = 'Roman Season Icons'
ROW = ['home', 'bulb-on', 'monitor', 'headset', 'graduation-on', 'calendar', 'terminal-on', 'wrench']

count = len(json.load(open(f'{PACK}/icons.json')))

def uri(name):
    path = f'{PACK}/icons/{name}.png'
    assert os.path.exists(path), path
    return 'data:image/png;base64,' + base64.b64encode(open(path, 'rb').read()).decode()

def row(mode):
    return ''.join(f'<img src="{uri(f"standard-{mode}-{n}")}">' for n in ROW)

html = f'''<html><body style="margin:0;width:1920px;height:960px;background:#1a0f0f;color:#f6efe3;
font-family:'Liberation Serif','DejaVu Serif',serif;position:relative">
<div style="position:absolute;left:90px;top:190px;font-size:88px;font-weight:bold">{TITLE}</div>
<div style="position:absolute;left:90px;top:312px;font-size:34px;color:#d9ccbd">{count:,} icons · with and without background · 5 seasons · light, dark and burgundy</div>
<div style="position:absolute;left:90px;top:395px;display:flex;gap:28px">{row("dark")}</div>
<div style="position:absolute;left:90px;top:593px;display:flex;gap:28px">{row("light")}</div>
<style>img{{width:170px;height:170px}}</style></body></html>'''

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 1920, 'height': 960})
    pg.set_content(html)
    pg.screenshot(path='marketplace/thumbnail.png')
    b.close()
print('thumbnail written,', count, 'icons')
