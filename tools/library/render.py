import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from glyphs import G, BADGE, VARIANTS
SEAS=[("standard","Standard","Standard"),("fruehling","Spring","Frühling"),("sommer","Summer","Sommer"),("herbst","Autumn","Herbst"),("winter","Winter","Winter")]
MODES=[("light","Light","Hell"),("dark","Dark","Dunkel"),("burgundy","Burgundy","Burgund")]
STATES=[('off','Off','Outline'),('on','On','Filled')]
def items():
    """alle Konzepte inkl. Abzeichen-Varianten: (id, dict)"""
    out=[]
    for i,g in G.items():
        out.append((i,g))
        for v in VARIANTS.get(i,[]):
            lab,mark=BADGE[v]
            h=dict(g); h['name']=f"{g['name']} {lab}"; h['badge']=mark; h['tags']=g['tags']+[lab]
            out.append((f'{i}-{v}',h))
    return out
def svg(g,state,c,clear):
    on=state=='on'; tx,bg,ac=c['tx'],c['bg'],c['ac']
    base='' if clear else f'<rect width="144" height="144" rx="24" fill="{bg}"/><rect x="5" y="5" width="134" height="134" rx="19" fill="none" stroke="{c["bd"]}" stroke-width="2"/>'
    under=f'<rect x="58" y="124" width="28" height="4" rx="2" fill="{ac}"/>'
    sw=3.4 if (on and g['kind']=='l') else 2
    body=f'<g fill="{tx if on else "none"}" stroke="{tx}" style="color:{tx}">{g["body"]}</g>' if g['body'] else ''
    kc=bg if on else tx
    knock=f'<g fill="none" stroke="{kc}" style="color:{kc}">{g["knock"]}</g>' if g['knock'] else ''
    line=f'<g fill="none" stroke="{tx}" style="color:{tx}" stroke-width="{sw}">{g["line"]}</g>' if g['line'] else ''
    acc=f'<g fill="none" stroke="{ac}" style="color:{ac}">{g["acc"]}</g>' if (on and g['acc']) else ''
    det=g.get('det','')
    detsvg=''
    if det:
        dt=f'<g fill="none" stroke="{tx}" style="color:{tx}">{det}</g>'
        if on and g['body']:
            dt+=f'<clipPath id="kb">{g["body"]}</clipPath><g clip-path="url(#kb)" fill="none" stroke="{bg}" style="color:{bg}">{det}</g>'
        detsvg=dt
    cuts=''
    if g.get('slash'): cuts+=f'<path d="{g["slash"]}" stroke="#000" stroke-width="5.6" fill="none"/>'
    if g.get('badge'): cuts+='<circle cx="18.5" cy="18.5" r="6.6" fill="#000" stroke="none"/>'
    mask=f'<mask id="m" maskUnits="userSpaceOnUse" x="-8" y="-8" width="40" height="40"><rect x="-8" y="-8" width="40" height="40" fill="#fff" stroke="none"/>{cuts}</mask>' if cuts else ''
    slash=f'<path d="{g["slash"]}" fill="none" stroke="{tx}" stroke-width="2"/>' if g.get('slash') else ''
    badge=f'<circle cx="18.5" cy="18.5" r="5" fill="{tx}" stroke="none"/><path d="{g["badge"]}" fill="none" stroke="{bg}" stroke-width="1.8"/>' if g.get('badge') else ''
    inner=f'<g{" mask=\"url(#m)\"" if cuts else ""}>{body}{knock}{line}{detsvg}{acc}</g>{slash}{badge}'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="144" height="144" viewBox="0 0 144 144">{base}<g transform="translate(30 22) scale(3.5)" stroke-width="{sw if g["kind"]=="l" else 2}" stroke-linecap="round" stroke-linejoin="round" fill="none"><defs>{mask}</defs>{inner}</g>{under}</svg>'
