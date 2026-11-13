# Glyph-Bibliothek (24er Raster). Jede Form: (Name, Gruppe, Tags, Art, Körper, Aussparung, Linien, Akzent[, Schrägstrich])
#  Art 'f' = füllbar: Aus = Umriss, An = gefüllt (Aussparungen werden Hintergrundfarbe)
#  Art 'l' = nur Linie: An = fett
#  Körper: geschlossene Formen | Aussparung: Details, im An-Zustand in Hintergrundfarbe | Linien: immer Textfarbe
#  Akzent: nur im An-Zustand, Akzentfarbe (Licht, Strahlen)
G = {}
def f(i, name, grp, tags, body='', knock='', line='', acc='', slash=''):
    G[i] = dict(name=name, grp=grp, tags=tags.split(',') if tags else [], kind='f', body=body, knock=knock, line=line, acc=acc, slash=slash)
def l(i, name, grp, tags, line):
    G[i] = dict(name=name, grp=grp, tags=tags.split(',') if tags else [], kind='l', body='', knock='', line=line, acc='', slash='')
C = lambda x, y, r: f'<circle cx="{x}" cy="{y}" r="{r}"/>'
D = lambda x, y: f'<circle cx="{x}" cy="{y}" r="1.1" fill="currentColor" stroke="none"/>'
R = lambda x, y, w, h, r=1.5: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/>'
GL = 'Light'
RAYS = '<path d="M12 .8V-1M4.4 3.6 3 2.2M19.6 3.6 21 2.2M2.2 9H.2M21.8 9h2"/>'
# ---------- Licht ----------
f('light-bulb','Light bulb',GL,'lamp,bulb,toggle,smart home,Glühbirne,Lampe','<path d="M9 18v-1.6c0-1-.6-1.8-1.4-2.5A6.5 6.5 0 1 1 16.4 13.9c-.8.7-1.4 1.5-1.4 2.5V18z"/>','','<path d="M9.5 21h5"/>','<path d="M12 .8V-1M4.6 3.8 3.2 2.4M19.4 3.8l1.4-1.4M1.8 9.5H-.2M22.2 9.5h2"/>')
f('spot-light','Spot light',GL,'spotlight,beam,cone,Strahler,Spot,toggle','<path d="M8.5 3h7l1.6 5H6.9z"/>','','<path d="M6.5 11 3.5 21M17.5 11l3 10" stroke-dasharray="1.6 3"/>','<path d="M6.9 8 3 21h18l-3.9-13z" fill="currentColor" fill-opacity=".22" stroke="none"/><path d="M6.5 11 3.5 21M17.5 11l3 10M12 11v10"/>')
f('downlight','Built-in light (downlight)',GL,'built-in,recessed,downlight,ceiling,Einbauleuchte,Einbauspot,Deckenlicht,toggle','<path d="M7 4.5h10l2 4H5z"/>','','<path d="M2 4.5h20M2 4.5h3M19 4.5h3"/>','<path d="M5 8.5 5.5 9l-3 11h19L18.5 9l.5-.5z" fill="currentColor" fill-opacity=".2" stroke="none"/><path d="M6.5 11.5 4.5 19M12 11.5V20M17.5 11.5l2 7.5"/>')
f('cabinet-light','Under-cabinet light',GL,'cupboard,cabinet,under cabinet,kitchen,Schrank,Unterbauleuchte,Küche,toggle','<rect x="6" y="10" width="12" height="2.6" rx="1.3"/>','','<rect x="3" y="3" width="18" height="7" rx="1.5"/><path d="M3 21h18"/>','<path d="M6.5 13 3.2 21h17.6L17.5 13z" fill="currentColor" fill-opacity=".2" stroke="none"/><path d="M8 15l-1.4 4M12 14.5V19M16 15l1.4 4"/>')
f('cupboard-light','Cupboard light (inside)',GL,'wardrobe,closet,cupboard,Schrank,Kleiderschrank,Innenlicht,built-in,toggle','<rect x="5" y="3" width="14" height="18" rx="2"/>','<path d="M12 3v18M9.5 11v2.5M14.5 11v2.5"/>','','<path d="M3.5 3.5 2 2M20.5 3.5 22 2M12 1V-1"/>')
f('light-strip','Light strip (LED strip)',GL,'LED strip,light strip,Lichtband,LED-Streifen,Elgato,RGB,toggle','<rect x="2.5" y="9.5" width="19" height="5.5" rx="2.75"/>','<path d="M6.5 12.2h.01M10.5 12.2h.01M14.5 12.2h.01M18.5 12.2h.01" stroke-width="2.4"/>','','<path d="M6 6.5V4.5M12 6.5V3M18 6.5V4.5M6 18v2M12 18v3M18 18v2"/>')
f('led-strip-wave','LED strip (wave)',GL,'LED strip,wave,ribbon,Lichtband,RGB,toggle','<path d="M2.5 15.5c2.2-5 5-5 7-1.5s5 2.5 7-1.5c1.2-2.4 3.2-3 5-2v5c-1.8-1-3.8-.4-5 2-2 4-5 5-7 1.5s-4.8-3.5-7 1.5z"/>','<path d="M7.5 13.2h.01M12.5 15h.01M17 12.5h.01" stroke-width="2.2"/>','','<path d="M7 7V5M13 8V5.5M19 7V5"/>')
f('key-light','Key light (panel on stand)',GL,'Elgato,Key Light,panel,studio,streaming,Panel,toggle','<rect x="4" y="3" width="16" height="11" rx="2.2"/>','<path d="M8 6.8h8M8 10.2h8"/>','<path d="M12 14v6M7.5 21h9"/>','<path d="M2 5.5H.2M2 9.5H.2M22 5.5h1.8M22 9.5h1.8"/>')
f('panel-light','LED panel',GL,'LED panel,panel,studio,Flächenlicht,toggle','<rect x="3" y="4" width="18" height="16" rx="2.5"/>','<path d="M8 9h.01M12 9h.01M16 9h.01M8 12.5h.01M12 12.5h.01M16 12.5h.01M8 16h.01M12 16h.01M16 16h.01" stroke-width="2.2"/>','','<path d="M3 1.5 1.8 .3M21 1.5l1.2-1.2"/>')
f('ring-light','Ring light',GL,'ring,Ringlicht,Elgato,Ring Light,streaming,toggle','<path fill-rule="evenodd" d="M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zm0 4.2a4.8 4.8 0 1 1 0 9.6 4.8 4.8 0 0 1 0-9.6z"/>','','','<path d="M12 .6V-1M3.4 3.4 2 2M20.6 3.4 22 2"/>')
f('desk-lamp','Desk lamp',GL,'desk,lamp,Schreibtischlampe,Tischlampe,toggle','<path d="M5.5 6.5 11 3l4.5 6.5-5.5 3.4z"/>','','<path d="M10 12.9 7 18.5M4 21h9M7 18.5h5"/>','<path d="M14 11.5l5.5 8h-8.5z" fill="currentColor" fill-opacity=".2" stroke="none"/><path d="M16 14.5l2.5 4M13 13l1.5 5"/>')
f('floor-lamp','Floor lamp',GL,'floor,lamp,Stehlampe,toggle','<path d="M8 3h8l2 6.5H6z"/>','','<path d="M12 9.5V21M8 21.5h8"/>','<path d="M3.5 6.5H1.7M20.5 6.5h1.8M5 2.2 3.8 1M19 2.2 20.2 1"/>')
f('pendant-light','Pendant light',GL,'pendant,ceiling,hanging,Pendelleuchte,Hängelampe,toggle','<path d="M4.5 14a7.5 7.5 0 0 1 15 0z"/>','','<path d="M12 2v4.5M9 2h6"/>','<path d="M4.5 14 3 21h18l-1.5-7z" fill="currentColor" fill-opacity=".2" stroke="none"/><path d="M7 17.5l-.6 2.5M12 17v3.5M17 17.5l.6 2.5"/>')
f('lantern','Lantern',GL,'lantern,Laterne,camping,toggle','<path d="M7.5 7h9v11a2.5 2.5 0 0 1-2.5 2.5h-4A2.5 2.5 0 0 1 7.5 18z"/>','<path d="M7.5 11h9M7.5 15.5h9"/>','<path d="M9.5 7V4.5h5V7M12 2.5v2M8.5 22.5h7"/>','<path d="M4.5 12H2.5M21.5 12h-2M5 6 3.5 4.5M19 6l1.5-1.5"/>')
f('string-lights','String lights',GL,'fairy lights,string,Lichterkette,party,toggle','<circle cx="5" cy="12.5" r="2.2"/><circle cx="12" cy="14" r="2.2"/><circle cx="19" cy="12.5" r="2.2"/>','','<path d="M2 6c3.5 3.5 6 3.5 10 0s6.5-3.5 10 0M5 10.3V9M12 11.8V10.4M19 10.3V9"/>','<path d="M5 17.5v2M12 19v2.5M19 17.5v2"/>')
f('monitor-light','Monitor light bar',GL,'monitor light,screenbar,light bar,Monitorleuchte,Bildschirmlampe,toggle','<rect x="6" y="3" width="12" height="3.2" rx="1.6"/>','','<path d="M5 11h14a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-7a1 1 0 0 1 1-1zM12 20v2"/>','<path d="M7 7.6l-1.2 2.2M12 7.4v2.6M17 7.6l1.2 2.2"/>')
f('smart-plug','Smart plug',GL,'plug,socket,outlet,Steckdose,Zwischenstecker,toggle','<rect x="5" y="3" width="14" height="18" rx="4.5"/>','<path d="M10 7.5v2.5M14 7.5v2.5"/><circle cx="12" cy="15.2" r="2.1"/>','','')
f('light-switch','Light switch',GL,'switch,wall,Lichtschalter,toggle','<rect x="6" y="2.5" width="12" height="19" rx="3.2"/>','<rect x="9.7" y="6" width="4.6" height="6" rx="1.4"/>','','')
f('color-temperature','Color temperature',GL,'white balance,temperature,warm,cool,Farbtemperatur,Thermometer,toggle','<path d="M10 14.5V5a2 2 0 0 1 4 0v9.5a4.2 4.2 0 1 1-4 0z"/>','<path d="M12 9v8"/><circle cx="12" cy="17.6" r="1.1" fill="currentColor"/>','','<path d="M17 6h3M17 9.5h2M17 13h3"/>')
f('light-scene','Light scene',GL,'scene,mood,ambience,Lichtstimmung,Szene,toggle','<path d="M10 3l1.9 5.1L17 10l-5.1 1.9L10 17l-1.9-5.1L3 10l5.1-1.9z"/>','','<path d="M18 14l.8 2.2 2.2.8-2.2.8L18 20l-.8-2.2L15 17l2.2-.8z"/>','')
f('sun','Sun / brightness',GL,'sun,brightness,Helligkeit,Sonne,day,toggle','<circle cx="12" cy="12" r="4.6"/>','','<path d="M12 2.5v2.4M12 19.1v2.4M2.5 12h2.4M19.1 12h2.4M5.3 5.3 7 7M17 17l1.7 1.7M5.3 18.7 7 17M17 7l1.7-1.7"/>','')
f('moon-night','Moon / night light',GL,'moon,night,night light,sleep,dark,Mond,Nachtlicht,toggle','<path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a7 7 0 0 0 10.5 10.5z"/>')
f('lightning','Lightning bolt',GL,'bolt,flash,power,Blitz,Strom,toggle','<path d="M13.5 2 4.5 14H11l-1 8 9-12h-6.5z"/>')
f('flame','Flame',GL,'fire,hot,Feuer,Flamme,toggle','<path d="M12 22c4 0 7-2.8 7-7 0-3-2-5-3-7-1 1.5-2 2-3 2 0-3-1-5-3-7-.5 3-4 5.5-4 10.5C6 19 8 22 12 22z"/>','<path d="M12 19a2.5 2.5 0 0 0 2.5-2.5c0-1.5-1.5-2-2.5-3.5-1 1.5-2.5 2-2.5 3.5A2.5 2.5 0 0 0 12 19z"/>')
# ---------- Pfeile & Zeichen (Linie) ----------
for i, n, t, d in [
 ('arrow-up','Arrow up','arrow,up,Pfeil,hoch','M12 20V5M6 11l6-6 6 6'),('arrow-down','Arrow down','arrow,down,Pfeil,runter','M12 4v15M6 13l6 6 6-6'),
 ('arrow-left','Arrow left','arrow,left,Pfeil,links','M20 12H5M11 6l-6 6 6 6'),('arrow-right','Arrow right','arrow,right,Pfeil,rechts','M4 12h15M13 6l6 6-6 6'),
 ('arrow-left-right','Arrow left-right','arrow,horizontal,Pfeil','M4 12h16M8 8l-4 4 4 4M16 8l4 4-4 4'),('arrow-up-down','Arrow up-down','arrow,vertical,Pfeil','M12 4v16M8 8l4-4 4 4M8 16l4 4 4-4'),
 ('arrow-return','Arrow return','arrow,return,enter,Pfeil','M6 4v7a3 3 0 0 0 3 3h10M15 10l4 4-4 4'),
 ('chevron-up','Chevron up','chevron,up','M6 15l6-6 6 6'),('chevron-down','Chevron down','chevron,down','M6 9l6 6 6-6'),
 ('chevron-left','Chevron left','chevron,left,back','M15 6l-6 6 6 6'),('chevron-right','Chevron right','chevron,right,next','M9 6l6 6-6 6'),
 ('chevrons-up','Chevrons up','chevron,double,up','M6 12l6-6 6 6M6 19l6-6 6 6'),('chevrons-down','Chevrons down','chevron,double,down','M6 5l6 6 6-6M6 12l6 6 6-6'),
 ('chevrons-left','Chevrons left','chevron,double,rewind','M12 6l-6 6 6 6M19 6l-6 6 6 6'),('chevrons-right','Chevrons right','chevron,double,forward','M5 6l6 6-6 6M12 6l6 6-6 6'),
 ('chevrons-up-down','Chevrons up-down','chevron,select,expand','M8 9l4-4 4 4M8 15l4 4 4-4'),
 ('plus','Plus','plus,add,hinzufügen','M12 5v14M5 12h14'),('minus','Minus','minus,remove,entfernen','M5 12h14'),
 ('close','Close','close,x,cross,schliessen','M6 6l12 12M18 6L6 18'),('check','Check','check,tick,ok,Haken','M5 12.5l4.5 4.5L19 7'),
 ('code','Code','code,brackets,Entwicklung','M8 8l-4 4 4 4M16 8l4 4-4 4M13.5 5l-3 14'),('code-brackets','Code chevrons','code,chevrons,html','M8 8l-4 4 4 4M16 8l4 4-4 4'),
 ('more-horizontal','More (horizontal)','more,dots,menu,mehr','M6 12h.01M12 12h.01M18 12h.01'),('more-vertical','More (vertical)','more,dots,menu,mehr','M12 6h.01M12 12h.01M12 18h.01'),
 ('menu','Menu','menu,hamburger,Menü','M3 6h18M3 12h18M3 18h18'),('list','List','list,bullets,Liste','M9 6h12M9 12h12M9 18h12M4 6h.01M4 12h.01M4 18h.01'),
 ('checklist','Checklist','checklist,todo,tasks,Aufgaben','M10 6h11M10 12h11M10 18h11M3.5 6l1.5 1.5L7.5 5M3.5 12l1.5 1.5 2.5-2.5M3.5 18l1.5 1.5 2.5-2.5'),
 ('expand','Expand','expand,fullscreen,Vollbild','M14 4h6v6M20 4l-7 7M10 20H4v-6M4 20l7-7'),('collapse','Collapse','collapse,shrink,verkleinern','M20 10h-6V4M14 10l7-7M4 14h6v6M10 14l-7 7'),
 ('refresh','Refresh','refresh,reload,sync,Aktualisieren','M20 12a8 8 0 1 1-2.5-5.8M20 4v5h-5'),('undo','Undo','undo,back,Rückgängig','M4 10h10a5 5 0 0 1 0 10H8M4 10l4-4M4 10l4 4'),
 ('redo','Redo','redo,forward,Wiederholen','M20 10H10a5 5 0 0 0 0 10h6M20 10l-4-4M20 10l-4 4'),('shuffle','Shuffle','shuffle,random,Zufall','M3 7h3c4 0 5 10 9 10h3M3 17h3c1.5 0 2.5-1.5 3.5-3M15 7h3M18 7l-2.5-2.5M18 7l-2.5 2.5M18 17l-2.5-2.5M18 17l-2.5 2.5'),
 ('upload','Upload','upload,export,Hochladen','M12 15V3M7 8l5-5 5 5M4 14v5a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-5'),('download-tray','Download','download,import,Herunterladen','M12 3v12M7 10l5 5 5-5M4 14v5a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-5'),
 ('power','Power','power,on off,Ein Aus','M12 3v9M6.5 6.5a8 8 0 1 0 11 0'),('crop','Crop','crop,trim,Zuschneiden','M6 2v14a2 2 0 0 0 2 2h14M2 6h14a2 2 0 0 1 2 2v14'),
 ('scan-frame','Scan frame','viewfinder,scan,frame,capture','M3 8V5a2 2 0 0 1 2-2h3M16 3h3a2 2 0 0 1 2 2v3M21 16v3a2 2 0 0 1-2 2h-3M8 21H5a2 2 0 0 1-2-2v-3'),
 ('face-scan','Face scan','face id,face,scan,Gesicht','M3 8V5a2 2 0 0 1 2-2h3M16 3h3a2 2 0 0 1 2 2v3M21 16v3a2 2 0 0 1-2 2h-3M8 21H5a2 2 0 0 1-2-2v-3M9 10v1.5M15 10v1.5M9.5 15a3.5 3.5 0 0 0 5 0'),
 ('bold','Bold','text,bold,fett','M7 4h6a3.5 3.5 0 0 1 0 7H7zM7 11h7a3.5 3.5 0 0 1 0 7H7z'),('italic','Italic','text,italic,kursiv','M10 4h8M6 20h8M15 4l-6 16'),
 ('underline','Underline','text,underline,unterstrichen','M6 4v7a6 6 0 0 0 12 0V4M5 21h14'),('quote','Quote','quote,citation,Zitat','M7 17c-2 0-3-1.2-3-3 0-3 2-5 4-6M17 17c-2 0-3-1.2-3-3 0-3 2-5 4-6'),
 ('paperclip','Paperclip','attachment,clip,Anhang,Büroklammer','M20 11.5l-8 8a5 5 0 0 1-7-7l8.5-8.5a3.3 3.3 0 0 1 4.7 4.7L9.5 17a1.7 1.7 0 0 1-2.4-2.4l7.4-7.4'),
 ('scissors','Scissors','cut,scissors,Schere','M6 9a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM6 21a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM8.1 7.9 20 18M8.1 16.1 20 6'),
 ('dollar','Dollar','money,dollar,currency,Geld','M12 2v20M17 6.5C16 5 14.5 4.5 12 4.5c-3 0-4.5 1.5-4.5 3.5S9 11 12 11.5s5 1.3 5 3.5-1.5 3.5-5 3.5c-2.5 0-4.5-.7-5.5-2.5'),
 ('euro','Euro','money,euro,currency,Geld','M18 6.5A7 7 0 1 0 18 17.5M3 10h10M3 14h10'),
 ('pound','Pound','money,pound,currency,Geld','M17 6a4.5 4.5 0 0 0-8.5 2v4M6 12h8M6 20h12M8.5 12v6c0 1.5-1 2-2.5 2'),
 ('yen','Yen','money,yen,currency,Geld','M6 3l6 9 6-9M12 12v9M7 14h10M7 18h10'),
 ('swap','Swap','swap,exchange,transfer,Tauschen','M4 8h14M14 4l4 4-4 4M20 16H6M10 12l-4 4 4 4'),
]: l(i, n, 'Arrows & signs', t, f'<path d="{d}"/>')
# ---------- Formen ----------
S = 'Shapes'
f('circle','Circle',S,'circle,dot,Kreis','<circle cx="12" cy="12" r="9"/>')
f('record','Record',S,'record,rec,Aufnahme','<circle cx="12" cy="12" r="9"/>','<circle cx="12" cy="12" r="3.4" fill="currentColor"/>')
f('square','Square',S,'square,Quadrat','<rect x="4" y="4" width="16" height="16" rx="3"/>')
f('stop','Stop',S,'stop,Stopp','<rect x="5" y="5" width="14" height="14" rx="2.6"/>')
f('diamond','Diamond',S,'diamond,rhombus,Raute','<path d="M12 2.5l9.5 9.5-9.5 9.5L2.5 12z"/>')
f('hexagon','Hexagon',S,'hexagon,Sechseck','<path d="M12 2.5l8.2 4.7v9.6L12 21.5l-8.2-4.7V7.2z"/>')
f('octagon','Octagon',S,'octagon,stop sign,Achteck','<path d="M8 3h8l5 5v8l-5 5H8l-5-5V8z"/>')
f('pentagon','Pentagon',S,'pentagon,Fünfeck','<path d="M12 3l9 6.6-3.5 10.9h-11L3 9.6z"/>')
f('triangle','Triangle',S,'triangle,Dreieck','<path d="M12 4l9 16H3z"/>')
f('heart','Heart',S,'heart,like,favorite,Herz','<path d="M12 20.5C4 14.5 3 11 3 8.5A4.5 4.5 0 0 1 12 6.5a4.5 4.5 0 0 1 9 2c0 2.5-1 6-9 12z"/>')
f('star','Star',S,'star,favorite,rating,Stern','<path d="M12 3l2.7 5.8 6.3.7-4.7 4.3 1.3 6.2L12 16.8 6.4 20l1.3-6.2L3 9.5l6.3-.7z"/>')
f('badge-star','Star badge',S,'badge,star,award,Abzeichen','<path d="M12 2.5l8.2 4.7v9.6L12 21.5l-8.2-4.7V7.2z"/>','<path d="M12 7.5l1.4 3 3.2.3-2.4 2.2.7 3.2L12 14.5 9.1 16.2l.7-3.2-2.4-2.2 3.2-.3z"/>')
f('percent-badge','Percent badge',S,'discount,percent,sale,Rabatt','<path d="M12 2l2.5 2 3.2-.3 1.2 3 3 1.2-.3 3.2L22 12l-2 2.5.3 3.2-3 1.2-1.2 3-3.2-.3L12 22l-2.5-2-3.2.3-1.2-3-3-1.2.3-3.2L2 12l2-2.5-.3-3.2 3-1.2 1.2-3 3.2.3z"/>','<path d="M9 15l6-6M9.5 9.5h.01M14.5 14.5h.01" stroke-width="2.2"/>')
f('check-circle','Check circle',S,'check,done,success,erledigt','<circle cx="12" cy="12" r="9"/>','<path d="M7.8 12.3l3 3 5.4-6"/>')
f('x-circle','Close circle',S,'close,cancel,error,Abbrechen','<circle cx="12" cy="12" r="9"/>','<path d="M8.8 8.8l6.4 6.4M15.2 8.8l-6.4 6.4"/>')
f('plus-circle','Plus circle',S,'add,plus,hinzufügen','<circle cx="12" cy="12" r="9"/>','<path d="M12 7.5v9M7.5 12h9"/>')
f('minus-circle','Minus circle',S,'remove,minus,entfernen','<circle cx="12" cy="12" r="9"/>','<path d="M7.5 12h9"/>')
f('x-square','Close square',S,'close,cancel,Abbrechen','<rect x="3.5" y="3.5" width="17" height="17" rx="3"/>','<path d="M8.5 8.5l7 7M15.5 8.5l-7 7"/>')
f('info-circle','Info',S,'info,information,Information','<circle cx="12" cy="12" r="9"/>','<path d="M12 11v5.5"/><circle cx="12" cy="7.7" r="1.1" fill="currentColor"/>')
f('help-circle','Help',S,'help,question,Hilfe,Frage','<circle cx="12" cy="12" r="9"/>','<path d="M9.4 9.6a2.6 2.6 0 1 1 3.6 2.3c-.7.4-1 .9-1 1.7"/><circle cx="12" cy="16.6" r="1.1" fill="currentColor"/>')
f('warning','Warning',S,'warning,alert,Warnung','<path d="M12 3l10 18H2z"/>','<path d="M12 10v5"/><circle cx="12" cy="17.9" r="1.1" fill="currentColor"/>')
f('ban','No entry',S,'ban,forbidden,blocked,verboten','<circle cx="12" cy="12" r="9"/>','<path d="M5.7 5.7l12.6 12.6"/>')
f('pause','Pause',S,'pause,Pause','<rect x="6" y="4" width="4" height="16" rx="1.5"/><rect x="14" y="4" width="4" height="16" rx="1.5"/>')
f('play','Play',S,'play,start,Wiedergabe','<path d="M7 4.5l13 7.5-13 7.5z"/>')
f('play-circle','Play circle',S,'play,start,Wiedergabe','<circle cx="12" cy="12" r="9"/>','<path d="M10 8.2l6 3.8-6 3.8z"/>')
f('play-pause','Play / pause',S,'play pause,next,Wiedergabe','<path d="M3 5l9 7-9 7z"/><rect x="15" y="5" width="2.8" height="14" rx="1"/><rect x="19.6" y="5" width="2.8" height="14" rx="1"/>')
f('cloud','Cloud',S,'cloud,Wolke','<path d="M7 18.5a4.5 4.5 0 0 1-.6-8.96A6 6 0 0 1 18 10.5a4 4 0 0 1 0 8z"/>')
f('drop','Drop',S,'drop,water,humidity,Tropfen','<path d="M12 3c3.5 4.2 6 7.2 6 10.5a6 6 0 0 1-12 0C6 10.2 8.5 7.2 12 3z"/>','<path d="M9 14.5a3 3 0 0 0 3 3"/>')
f('crown','Crown',S,'crown,king,premium,Krone','<path d="M3 8l4.5 4L12 5l4.5 7L21 8l-2 11H5z"/>')
f('mountain','Mountain',S,'mountain,landscape,hike,Berg','<path d="M2 20l7-12 4 6 2.5-4L22 20z"/>')
f('pine','Pine tree',S,'tree,pine,forest,Baum,Wald','<path d="M12 3l5 7h-2.5l4 6H5.5l4-6H7z"/>','','<path d="M12 16v5"/>')
f('smiley','Smiley',S,'smile,emoji,happy,Smiley','<circle cx="12" cy="12" r="9"/>','<path d="M9 10h.01M15 10h.01M8.5 14.5a4.5 4 0 0 0 7 0" stroke-width="2"/>')
f('sparkles','Sparkles',S,'sparkles,magic,ai,Funken,Magie','<path d="M10 3l1.8 5.2L17 10l-5.2 1.8L10 17l-1.8-5.2L3 10l5.2-1.8z"/><path d="M18 14l.8 2.2 2.2.8-2.2.8L18 20l-.8-2.2L15 17l2.2-.8z"/>')
# ---------- Objekte ----------
O = 'Objects'
f('person','Person',O,'person,user,profile,Benutzer,Person','<circle cx="12" cy="7.5" r="4"/><path d="M4.5 21a7.5 7.5 0 0 1 15 0z"/>')
f('people','People',O,'people,group,team,Gruppe,Personen','<circle cx="9" cy="8" r="3.4"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0z"/><circle cx="17" cy="9" r="2.6"/><path d="M17 14.5a5.5 5.5 0 0 1 4.5 5.5h-4"/>')
f('user-circle','User circle',O,'user,account,profile,Konto','<circle cx="12" cy="12" r="9"/>','<circle cx="12" cy="10" r="3"/><path d="M6.4 18.3a6 6 0 0 1 11.2 0"/>')
f('accessibility','Accessibility',O,'accessibility,a11y,Barrierefreiheit','<circle cx="12" cy="12" r="9"/>','<circle cx="12" cy="7.8" r="1.1" fill="currentColor"/><path d="M7.5 10.5l4.5 1 4.5-1M12 11.5v3M12 14.5l-2.5 3.5M12 14.5l2.5 3.5"/>')
f('home','Home',O,'home,house,Haus,Startseite','<path d="M4 11l8-7 8 7v9a1 1 0 0 1-1 1h-4v-6h-6v6H5a1 1 0 0 1-1-1z"/>')
f('briefcase','Briefcase',O,'briefcase,work,job,Aktentasche,Arbeit','<rect x="3" y="7" width="18" height="13" rx="2.2"/>','<path d="M3 13h18"/>','<path d="M9 7V5a1.5 1.5 0 0 1 1.5-1.5h3A1.5 1.5 0 0 1 15 5v2"/>')
f('book-open','Open book',O,'book,read,open,Buch,Lesen','<path d="M12 6c-2-1.5-5-2-9-2v14c4 0 7 .5 9 2 2-1.5 5-2 9-2V4c-4 0-7 .5-9 2z"/>','<path d="M12 6v14"/>')
f('books','Books',O,'books,library,Bücher,Bibliothek','<rect x="3" y="4" width="4" height="16" rx="1"/><rect x="9" y="4" width="4" height="16" rx="1"/><path d="M15 5.5l3.8-1 3.2 14.5-3.8 1z"/>')
f('calendar-day','Calendar',O,'calendar,date,Kalender,Datum','<rect x="3" y="5" width="18" height="16" rx="2.5"/>','<path d="M3 10h18"/>','<path d="M8 3v4M16 3v4"/>')
f('clock','Clock',O,'clock,time,Uhr,Zeit','<circle cx="12" cy="12" r="9"/>','<path d="M12 7v5l3 2"/>')
f('alarm','Alarm clock',O,'alarm,clock,Wecker','<circle cx="12" cy="13" r="8"/>','<path d="M12 8.5V13l3 2"/>','<path d="M3.5 5.5l3-2.5M20.5 5.5l-3-2.5"/>')
f('timer','Timer',O,'timer,stopwatch,Stoppuhr','<circle cx="12" cy="14" r="8"/>','<path d="M12 14l3-3.5"/>','<path d="M10 2.5h4M12 2.5V6"/>')
f('bell','Bell',O,'bell,notification,Glocke,Benachrichtigung','<path d="M6 17.5V11a6 6 0 0 1 12 0v6.5l2 2H4z"/>','','<path d="M10 22a2 2 0 0 0 4 0"/>')
f('bell-slash','Bell off',O,'bell,mute,silent,Stumm','<path d="M6 17.5V11a6 6 0 0 1 12 0v6.5l2 2H4z"/>','','<path d="M10 22a2 2 0 0 0 4 0"/>','','M3.5 3.5l17 17')
f('eye-open','Eye',O,'eye,view,visible,Auge,sichtbar','<path d="M2 12s3.5-7 10 -7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/>','<circle cx="12" cy="12" r="3" fill="currentColor"/>')
f('eye-closed','Eye off',O,'eye,hidden,invisible,Auge,versteckt','<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/>','<circle cx="12" cy="12" r="3" fill="currentColor"/>','','','M3.5 3.5l17 17')
f('lock','Lock',O,'lock,secure,locked,Schloss,gesperrt','<rect x="5" y="10.5" width="14" height="10.5" rx="2.6"/>','<circle cx="12" cy="15.6" r="1.4" fill="currentColor"/>','<path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/>')
f('unlock','Unlock',O,'unlock,open,unlocked,Schloss,offen','<rect x="5" y="10.5" width="14" height="10.5" rx="2.6"/>','<circle cx="12" cy="15.6" r="1.4" fill="currentColor"/>','<path d="M8 10.5V7.5a4 4 0 0 1 7.6-1.7"/>')
f('key','Key',O,'key,password,Schlüssel,Passwort','<circle cx="8" cy="15" r="4.8"/>','<circle cx="8" cy="15" r="1.3" fill="currentColor"/>','<path d="M11.4 11.6L20.5 2.5M17 6l3 3M14.3 8.7l2.2 2.2"/>')
f('pin','Location pin',O,'location,pin,map,Standort,Karte','<path d="M12 22s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/>','<circle cx="12" cy="10" r="2.6"/>')
f('globe','Globe',O,'globe,web,world,internet,Welt','<circle cx="12" cy="12" r="9"/>','<path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>')
f('mail','Mail',O,'mail,email,letter,Post,E-Mail','<rect x="2.5" y="5" width="19" height="14" rx="2.6"/>','<path d="M3 7l9 6.5L21 7"/>')
f('chat','Chat',O,'chat,message,comment,Nachricht','<path d="M5 4h14a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-7l-5 4v-4H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/>')
f('chat-text','Chat with text',O,'chat,message,text,Nachricht','<path d="M5 4h14a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-7l-5 4v-4H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/>','<path d="M7.5 9h9M7.5 12.5h5.5"/>')
f('phone','Phone',O,'phone,call,Telefon,Anruf','<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2z"/>')
f('microphone','Microphone',O,'microphone,mic,audio,Mikrofon','<rect x="9" y="2.5" width="6" height="11" rx="3"/>','','<path d="M5 11a7 7 0 0 0 14 0M12 18v3.5M8.5 21.5h7"/>')
f('microphone-slash','Microphone off',O,'microphone,mute,Mikrofon,stumm','<rect x="9" y="2.5" width="6" height="11" rx="3"/>','','<path d="M5 11a7 7 0 0 0 14 0M12 18v3.5M8.5 21.5h7"/>','','M3.5 3.5l17 17')
f('speaker-volume','Speaker',O,'speaker,volume,sound,Lautsprecher,Lautstärke','<path d="M3 9.5h4l5-4.5v14l-5-4.5H3z"/>','','<path d="M16 9a4 4 0 0 1 0 6M18.5 6.5a8 8 0 0 1 0 11"/>')
f('speaker-low','Speaker low',O,'speaker,volume,low,leise','<path d="M3 9.5h4l5-4.5v14l-5-4.5H3z"/>','','<path d="M16 9a4 4 0 0 1 0 6"/>')
f('speaker-mute','Speaker muted',O,'speaker,mute,silent,stumm','<path d="M3 9.5h4l5-4.5v14l-5-4.5H3z"/>','','<path d="M16.5 9.5l5 5M21.5 9.5l-5 5"/>')
f('headphones','Headphones',O,'headphones,audio,music,Kopfhörer','<rect x="3" y="13" width="5" height="8" rx="2.2"/><rect x="16" y="13" width="5" height="8" rx="2.2"/>','','<path d="M4 15v-3a8 8 0 0 1 16 0v3"/>')
f('music-note','Music',O,'music,note,song,Musik,Note','<circle cx="7.5" cy="18" r="3"/><circle cx="17.5" cy="16" r="3"/>','','<path d="M10.5 18V6l10-2v12"/>')
f('camera-photo','Camera',O,'camera,photo,Kamera,Foto','<path d="M4 8h3l2-3h6l2 3h3a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z"/>','<circle cx="12" cy="13.5" r="3.4"/>')
f('video','Video',O,'video,camera,film,Video','<rect x="2.5" y="6" width="13" height="12" rx="2.6"/><path d="M15.5 10.5l6-3.5v10l-6-3.5z"/>')
f('webcam','Webcam',O,'webcam,camera,Webcam','<circle cx="12" cy="10" r="7.5"/>','<circle cx="12" cy="10" r="3"/>','<path d="M12 17.5v3M8 21h8"/>')
f('webcam-slash','Webcam off',O,'webcam,camera,off,Webcam,aus','<circle cx="12" cy="10" r="7.5"/>','<circle cx="12" cy="10" r="3"/>','<path d="M12 17.5v3M8 21h8"/>','','M3.5 3.5l17 17')
f('cart','Shopping cart',O,'cart,shop,basket,Warenkorb,Einkaufen','<path d="M5.8 7H21l-2 8H7.8z"/><circle cx="9.5" cy="19.8" r="1.4"/><circle cx="17" cy="19.8" r="1.4"/>','','<path d="M2 3h3l1 4M7.8 15L6.4 7"/>')
f('church','Church',O,'church,cathedral,Kirche','<path d="M12 2.5l3 4.5v5h6V21H3v-9h6V7z"/>','<path d="M10 21v-3.5a2 2 0 0 1 4 0V21"/>')
f('tag','Tag',O,'tag,label,price,Etikett,Preis','<path d="M3 12V4a1 1 0 0 1 1-1h8l9 9-9 9z"/>','<circle cx="7.6" cy="7.6" r="1.3" fill="currentColor"/>')
f('trophy','Trophy',O,'trophy,award,win,Pokal','<path d="M7 3h10v6a5 5 0 0 1-10 0z"/>','','<path d="M7 5H4v2a3 3 0 0 0 3 3M17 5h3v2a3 3 0 0 1-3 3M12 14v4M8 21h8M9 18h6"/>')
f('rocket','Rocket',O,'rocket,launch,deploy,Rakete','<path d="M12.5 15.5l-4-4C10 7 13 4 20 4c0 7-3 10-7.5 11.5z"/>','<circle cx="15.5" cy="8.5" r="1.6" fill="currentColor"/>','<path d="M8.5 11.5L4 12l3-3.5M12.5 15.5L12 20l3.5-3M6 18l-2 2"/>')
f('puzzle','Puzzle',O,'puzzle,plugin,extension,Erweiterung','<path d="M9 4a2 2 0 1 1 4 0v1h4a1 1 0 0 1 1 1v4h1a2 2 0 1 1 0 4h-1v4a1 1 0 0 1-1 1h-4v-1a2 2 0 1 0-4 0v1H5a1 1 0 0 1-1-1v-4h1a2 2 0 1 0 0-4H4V6a1 1 0 0 1 1-1h4z"/>')
f('shield','Shield',O,'shield,security,protect,Schild,Sicherheit','<path d="M12 2.5l8 3v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10v-6z"/>','<path d="M8.5 12l2.5 2.5 4.5-5"/>')
f('shield-slash','Shield off',O,'shield,security,off,Schild,aus','<path d="M12 2.5l8 3v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10v-6z"/>','','','','M3.5 3.5l17 17')
f('compass','Compass',O,'compass,navigate,Kompass','<circle cx="12" cy="12" r="9"/>','<path d="M15.8 8.2l-2 5.6-5.6 2 2-5.6z"/>')
f('receipt','Receipt',O,'receipt,invoice,bill,Beleg,Rechnung','<path d="M6 2.5h12v19l-3-2-3 2-3-2-3 2z"/>','<path d="M9 8h6M9 12h6"/>')
f('credit-card','Credit card',O,'card,payment,credit,Karte,Zahlung','<rect x="2.5" y="5" width="19" height="14" rx="2.6"/>','<path d="M2.5 10h19M6.5 15h4"/>')
f('truck','Truck',O,'truck,delivery,shipping,Lieferwagen,Versand','<rect x="2.5" y="5.5" width="11" height="11" rx="1.6"/><path d="M13.5 9h4.5l3.5 4v3.5h-8z"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>')
f('train','Train',O,'train,tram,transport,Zug,Tram','<rect x="5" y="3" width="14" height="14" rx="3.2"/>','<path d="M5 11h14M9 14h.01M15 14h.01" stroke-width="2.2"/>','<path d="M8 21l2-4M16 21l-2-4"/>')
f('weather','Sun and cloud',O,'weather,sun,cloud,Wetter','<path d="M8.5 20.5a4 4 0 0 1-.5-8A5.5 5.5 0 0 1 18.6 13.7a3.4 3.4 0 0 1-.6 6.8z"/>','','<path d="M7.5 3.5v2M2.2 8.5h2M3.7 4.7l1.4 1.4M12 5l-.8 1.7"/>')
f('wifi-signal','Wi-Fi',O,'wifi,wlan,network,Netzwerk','<circle cx="12" cy="19.2" r="1.3" fill="currentColor"/>','','<path d="M2.5 9a14 14 0 0 1 19 0M5.5 12.5a10 10 0 0 1 13 0M8.5 16a5.5 5.5 0 0 1 7 0"/>')
f('wifi-signal-slash','Wi-Fi off',O,'wifi,off,offline,Netzwerk,aus','<circle cx="12" cy="19.2" r="1.3" fill="currentColor"/>','','<path d="M2.5 9a14 14 0 0 1 19 0M5.5 12.5a10 10 0 0 1 13 0M8.5 16a5.5 5.5 0 0 1 7 0"/>','','M3.5 3.5l17 17')
f('signal','Signal',O,'signal,bars,reception,Empfang','<rect x="3" y="16" width="3.2" height="5" rx="1"/><rect x="8" y="12" width="3.2" height="9" rx="1"/><rect x="13" y="8" width="3.2" height="13" rx="1"/><rect x="18" y="4" width="3.2" height="17" rx="1"/>')
f('palette','Palette',O,'palette,color,paint,Farbpalette','<path d="M12 3a9 9 0 1 0 0 18c1.5 0 2-1 1.4-2-.6-1 0-2.2 1.3-2.2H17a4 4 0 0 0 4-4A9 9 0 0 0 12 3z"/>','<path d="M7.5 11h.01M10 7.5h.01M14.5 7.5h.01" stroke-width="2.2"/>')
f('pen','Pen',O,'pen,edit,write,Stift,Bearbeiten','<path d="M4 20l1-5L16 4a2.1 2.1 0 0 1 3 3L8 18z"/>','','<path d="M14 6l3 3"/>')
f('paint-roller','Paint roller',O,'roller,paint,Farbroller','<rect x="4" y="3" width="14" height="6" rx="1.6"/>','','<path d="M18 6h2v5h-8v3M12 14v7"/>')
# ---------- Dateien ----------
F = 'Files & folders'
f('file','File',F,'file,document,Datei,Dokument','<path d="M6.5 2.5H14l5 5v13a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 5 20.5v-17A1.5 1.5 0 0 1 6.5 2.5z"/>','<path d="M14 2.5V8h5"/>')
f('file-text','File with text',F,'file,document,text,Datei,Text','<path d="M6.5 2.5H14l5 5v13a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 5 20.5v-17A1.5 1.5 0 0 1 6.5 2.5z"/>','<path d="M14 2.5V8h5M8.5 13h7M8.5 17h5"/>')
f('folder','Folder',F,'folder,directory,Ordner','<path d="M3 6a1.5 1.5 0 0 1 1.5-1.5H9l2 2.5h8.5A1.5 1.5 0 0 1 21 8.5V18a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 18z"/>')
f('save','Save',F,'save,disk,floppy,Speichern','<path d="M4.5 3h12.5l3.5 3.5V19a2 2 0 0 1-2 2H5.5a2 2 0 0 1-2-2V4a1 1 0 0 1 1-1z"/>','<path d="M7 3v5h8V3M7 21v-7h10v7"/>')
f('copy','Copy',F,'copy,duplicate,Kopieren','<rect x="8" y="8" width="13" height="13" rx="2.6"/>','','<path d="M16 8V5.5A1.5 1.5 0 0 0 14.5 4h-9A1.5 1.5 0 0 0 4 5.5v9A1.5 1.5 0 0 0 5.5 16H8"/>')
f('clipboard','Clipboard',F,'clipboard,paste,Zwischenablage','<rect x="5" y="4" width="14" height="17" rx="2.4"/>','','<rect x="9" y="2" width="6" height="4" rx="1.4"/>')
f('layers','Layers',F,'layers,stack,Ebenen','<path d="M12 3l9 5-9 5-9-5z"/>','','<path d="M3 12.5l9 5 9-5M3 16.5l9 5 9-5"/>')
f('trash','Trash',F,'trash,delete,bin,Papierkorb,Löschen','<path d="M5.5 7h13L17.3 20a1.5 1.5 0 0 1-1.5 1.5H8.2A1.5 1.5 0 0 1 6.7 20z"/>','<path d="M10 11v6M14 11v6"/>','<path d="M3.5 7h17M9 7V4h6v3"/>')
f('database','Database',F,'database,storage,Datenbank','<path d="M4 6c0-1.7 3.6-3 8-3s8 1.3 8 3v12c0 1.7-3.6 3-8 3s-8-1.3-8-3z"/>','<path d="M4 6c0 1.7 3.6 3 8 3s8-1.3 8-3M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>')
# ---------- Geräte & Layout ----------
V = 'Devices & layout'
f('display','Display',V,'display,monitor,screen,Bildschirm,Monitor','<rect x="2.5" y="4" width="19" height="13" rx="2.2"/>','','<path d="M8 21h8M12 17v4"/>')
f('laptop','Laptop',V,'laptop,notebook,Laptop','<rect x="4.5" y="5" width="15" height="11" rx="1.8"/>','','<path d="M2.5 19.5h19"/>')
f('smartphone','Smartphone',V,'phone,mobile,smartphone,Handy','<rect x="6.5" y="2.5" width="11" height="19" rx="2.8"/>','<path d="M10.5 18.5h3"/>')
f('chip','Chip',V,'chip,cpu,processor,Prozessor','<rect x="6" y="6" width="12" height="12" rx="2.2"/>','<rect x="9.5" y="9.5" width="5" height="5" rx="1"/>','<path d="M9 2.5v3M15 2.5v3M9 18.5v3M15 18.5v3M2.5 9h3M2.5 15h3M18.5 9h3M18.5 15h3"/>')
f('cube','Cube',V,'cube,3d,box,Würfel','<path d="M12 2.5l8.5 4.8v9.4L12 21.5l-8.5-4.8V7.3z"/>','<path d="M3.5 7.3L12 12l8.5-4.7M12 12v9.5"/>')
f('cube-scan','3D scan',V,'cube,3d,scan,ar,Scan','<path d="M12 7l4 2.2v4.6L12 16l-4-2.2V9.2z"/>','<path d="M8 9.2l4 2.3 4-2.3M12 11.5V16"/>','<path d="M3 8V5a2 2 0 0 1 2-2h3M16 3h3a2 2 0 0 1 2 2v3M21 16v3a2 2 0 0 1-2 2h-3M8 21H5a2 2 0 0 1-2-2v-3"/>')
f('grid-4','Grid',V,'grid,tiles,apps,Raster,Kacheln','<rect x="3.5" y="3.5" width="7.5" height="7.5" rx="2"/><rect x="13" y="3.5" width="7.5" height="7.5" rx="2"/><rect x="3.5" y="13" width="7.5" height="7.5" rx="2"/><rect x="13" y="13" width="7.5" height="7.5" rx="2"/>')
f('apps-add','Widgets',V,'widgets,apps,add,Widgets','<rect x="3.5" y="3.5" width="7.5" height="7.5" rx="2"/><rect x="13" y="3.5" width="7.5" height="7.5" rx="2"/><rect x="3.5" y="13" width="7.5" height="7.5" rx="2"/>','','<path d="M16.8 13.5v7M13.3 17h7"/>')
f('window','Window',V,'window,app,Fenster','<rect x="3" y="4" width="18" height="16" rx="2.5"/>','<path d="M3 9h18"/>')
f('sidebar','Sidebar',V,'sidebar,layout,panel,Seitenleiste','<rect x="3" y="4" width="18" height="16" rx="2.5"/>','<path d="M9.5 4v16"/>')
f('columns','Columns',V,'columns,layout,Spalten','<rect x="3" y="4" width="18" height="16" rx="2.5"/>','<path d="M9 4v16M15 4v16"/>')
f('windows-overlap','Windows',V,'windows,overlap,copy,Fenster','<rect x="3" y="9" width="12" height="12" rx="2.4"/>','','<path d="M8 6.5V6a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-.5"/>')
f('sliders','Sliders',V,'sliders,settings,mixer,Regler','<circle cx="14" cy="7" r="2.4"/><circle cx="9" cy="17" r="2.4"/>','','<path d="M3 7h8.6M16.4 7H21M3 17h3.6M11.4 17H21"/>')
f('sliders-vertical','Sliders vertical',V,'sliders,vertical,mixer,Regler','<circle cx="7" cy="14" r="2.4"/><circle cx="17" cy="9" r="2.4"/>','','<path d="M7 3v8.6M7 16.4V21M17 3v3.6M17 11.4V21"/>')
f('filter','Filter',V,'filter,funnel,Filter','<path d="M3 4h18l-7 9v6l-4 2v-8z"/>')
f('bar-chart','Bar chart',V,'chart,bars,stats,Diagramm,Statistik','<rect x="4" y="12" width="4.5" height="8" rx="1.3"/><rect x="9.8" y="4" width="4.5" height="16" rx="1.3"/><rect x="15.5" y="8" width="4.5" height="12" rx="1.3"/>')
f('pie-chart','Pie chart',V,'chart,pie,stats,Kreisdiagramm','<path d="M11 3.2A9 9 0 1 0 20.8 13H11z"/><path d="M14 2.7a9 9 0 0 1 7.3 7.3H14z"/>')
f('search','Search',V,'search,find,magnifier,Suche,Lupe','<circle cx="11" cy="11" r="7"/>','','<path d="M16.2 16.2L21 21"/>')
f('cursor','Cursor',V,'cursor,pointer,mouse,Zeiger','<path d="M5 3l15 7.5-6.3 2.2-2.2 6.3z"/>')
f('align-left','Align left',V,'align,left,Ausrichten,links','<rect x="6" y="5" width="13" height="5" rx="1.5"/><rect x="6" y="14" width="8" height="5" rx="1.5"/>','','<path d="M3 3v18"/>')
f('align-right','Align right',V,'align,right,Ausrichten,rechts','<rect x="5" y="5" width="13" height="5" rx="1.5"/><rect x="10" y="14" width="8" height="5" rx="1.5"/>','','<path d="M21 3v18"/>')
f('align-top','Align top',V,'align,top,Ausrichten,oben','<rect x="5" y="6" width="5" height="13" rx="1.5"/><rect x="14" y="6" width="5" height="8" rx="1.5"/>','','<path d="M3 3h18"/>')
f('align-bottom','Align bottom',V,'align,bottom,Ausrichten,unten','<rect x="5" y="5" width="5" height="13" rx="1.5"/><rect x="14" y="10" width="5" height="8" rx="1.5"/>','','<path d="M3 21h18"/>')
f('align-center-h','Align center horizontal',V,'align,center,Ausrichten,Mitte','<rect x="5" y="5" width="14" height="5" rx="1.5"/><rect x="8" y="14" width="8" height="5" rx="1.5"/>','','<path d="M12 3v18"/>')
f('align-center-v','Align center vertical',V,'align,center,Ausrichten,Mitte','<rect x="5" y="5" width="5" height="14" rx="1.5"/><rect x="14" y="8" width="5" height="8" rx="1.5"/>','','<path d="M3 12h18"/>')
# ---------- Streaming/Audio (bestehende Formen als An/Aus) ----------
f('soundboard','Soundboard',O,'soundboard,pads,audio,Soundboard,streaming','<rect x="3" y="3" width="8" height="8" rx="2"/><rect x="13" y="3" width="8" height="8" rx="2"/><rect x="3" y="13" width="8" height="8" rx="2"/><rect x="13" y="13" width="8" height="8" rx="2"/>')
l('waveform','Waveform',O,'waveform,audio,sound,Wellenform','<path d="M3 10v4M6.5 7v10M10 4v16M14 8v8M17.5 7v10M21 10v4"/>')
f('equalizer','Equalizer',O,'equalizer,bars,audio,Equalizer','<rect x="3.5" y="11" width="3.4" height="9" rx="1.2"/><rect x="10.3" y="4" width="3.4" height="16" rx="1.2"/><rect x="17.1" y="8" width="3.4" height="12" rx="1.2"/>')
f('broadcast','Broadcast',O,'broadcast,live,streaming,Übertragung','<circle cx="12" cy="12" r="2.4"/>','','<path d="M7.8 7.8a5.9 5.9 0 0 0 0 8.4M16.2 7.8a5.9 5.9 0 0 1 0 8.4M4.8 4.8a10.2 10.2 0 0 0 0 14.4M19.2 4.8a10.2 10.2 0 0 1 0 14.4"/>')
# ---------- Abzeichen-Varianten ----------
BADGE = {
 'plus':('with plus','M18.5 16.1v4.8M16.1 18.5h4.8'),'minus':('with minus','M16.1 18.5h4.8'),
 'check':('with check','M16.3 18.7l1.7 1.7 3-3.6'),'up':('with arrow up','M18.5 21v-4.8M16.4 18.2l2.1-2.1 2.1 2.1'),
 'down':('with arrow down','M18.5 16v4.8M16.4 18.8l2.1 2.1 2.1-2.1'),'out':('with arrow out','M16.8 20.2l3.4-3.4M17.4 16.8h2.8v2.8'),
}
VARIANTS = {'camera-photo':['check','plus','out'],'video':['plus','check','out'],'display':['plus','check','out'],'person':['plus','minus','check'],
 'chat':['plus','check','up','down','out'],'globe':['plus','check'],'headphones':['plus','out'],'folder':['plus','up','down'],
 'file':['plus','up','down'],'calendar-day':['plus','check'],'cube':['check'],'sun':['plus','minus','out'],'bell':['plus'],'mail':['plus','check']}

import glyphs_extra  # zusätzliche Formen
