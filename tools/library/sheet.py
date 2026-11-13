import sys; sys.path.insert(0,'/tmp/sdp/lib')
from render import *
from PIL import Image
from collections import Counter
from playwright.sync_api import sync_playwright
P='/home/claude/stream-deck-icon-pack/uk.novaroma-homelab.season-icons.sdIconPack/'
def pal_from(P,s,m):
    im=Image.open(f'{P}icons/{s}-{m}-gear.png').convert('RGBA')
    bg=im.getpixel((20,72)); bd=im.getpixel((4,72)); ac=im.getpixel((72,125))
    c=Counter(p for p in im.getdata() if p[3]==255 and p not in (bg,bd,ac)); tx=c.most_common(1)[0][0]
    h=lambda t:'#%02x%02x%02x'%t[:3]
    return dict(bg=h(bg),bd=h(bd),ac=h(ac),tx=h(tx))
pal=lambda s,m:pal_from(P,s,m)
if __name__=='__main__':
    s,m=sys.argv[1],sys.argv[2]; c=pal(s,m); its=items()
    lo,hi=int(sys.argv[3]),int(sys.argv[4]); its=its[lo:hi]
    cells=''.join(f'<div title="{i}">{svg(g,st,c,False)}</div>' for i,g in its for st in ('off','on'))
    html=f'<body style="margin:0;background:#222"><div style="display:grid;grid-template-columns:repeat(12,72px);gap:4px;padding:4px">{cells}</div></body>'
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':12*76+8,'height':900}); pg.set_content(html.replace('<svg xmlns="http://www.w3.org/2000/svg" width="144" height="144"','<svg style="width:72px;height:72px" xmlns="http://www.w3.org/2000/svg" width="144" height="144"'))
        pg.screenshot(path=f'sheet-{lo}.png',full_page=True); b.close()
