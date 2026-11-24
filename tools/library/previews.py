"""Five season icon previews (1920x960) for the Marketplace, built from the pack's own PNGs.
Writes marketplace/icon-preview-N-<season>.png and the identical copies in <pack>/previews/N-preview.png.
Usage: python3 tools/library/previews.py   (run from the repository root)"""
import base64, os, shutil
from playwright.sync_api import sync_playwright

PACK = 'uk.novaroma-homelab.season-icons.sdIconPack'
ICONS = ['home', 'bulb-on', 'monitor', 'headset', 'soundboard', 'mixer', 'gradcap', 'terminal']
MODES = [('light', 'Light'), ('dark', 'Dark'), ('burgundy', 'Burgundy')]
# file id, label, subtitle, gradient start, title colour
SEASONS = [
    ('standard', 'Standard', 'Home, studio and desk', '#1b0e0f', '#f6ecde'),
    ('fruehling', 'Spring', 'Fresh greens and blossom pink', '#162f1f', '#e8f5e1'),
    ('sommer', 'Summer', 'Warm gold and long days', '#593a0a', '#fff0c8'),
    ('herbst', 'Autumn', 'Amber, rust and burgundy', '#3a1a0c', '#f7e3c8'),
    ('winter', 'Winter', 'Cool blues and quiet nights', '#0b1a2c', '#eaf3fb'),
]
FILE_NAMES = ['standard', 'spring', 'summer', 'autumn', 'winter']

def uri(season, mode, icon):
    path = f'{PACK}/icons/{season}-{mode}-{icon}.png'
    assert os.path.exists(path), path
    return 'data:image/png;base64,' + base64.b64encode(open(path, 'rb').read()).decode()

def page(season, label, sub, grad, fg):
    rows = ''
    for r, (mode, mlabel) in enumerate(MODES):
        top = 207 + r * 196
        rows += f'<div style="position:absolute;left:80px;top:{top + 58}px;font-size:28px;opacity:.8">{mlabel}</div>'
        for c, icon in enumerate(ICONS):
            rows += f'<img src="{uri(season, mode, icon)}" style="position:absolute;left:{256 + c * 196}px;top:{top}px;width:170px;height:170px">'
    return f'''<html><body style="margin:0;width:1920px;height:960px;position:relative;color:{fg};
background:linear-gradient(135deg,{grad} 0%,#120a0b 100%);font-family:'Liberation Serif','DejaVu Serif',serif">
<div style="position:absolute;left:80px;top:40px;font-size:84px;font-weight:bold">{label}</div>
<div style="position:absolute;left:80px;top:140px;font-size:30px;opacity:.8">{sub} · light, dark and burgundy</div>{rows}</body></html>'''

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1920, 'height': 960})
    for n, ((season, label, sub, grad, fg), fname) in enumerate(zip(SEASONS, FILE_NAMES), 1):
        pg.set_content(page(season, label, sub, grad, fg))
        out = f'marketplace/icon-preview-{n}-{fname}.png'
        pg.screenshot(path=out)
        shutil.copyfile(out, f'{PACK}/previews/{n}-preview.png')
    b.close()
print('5 previews written')
