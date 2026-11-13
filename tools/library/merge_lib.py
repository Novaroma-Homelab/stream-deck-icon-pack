"""Fügt die Teil-Ergebnisse von build_lib.py in icons.json ein. Aufruf: python3 merge_lib.py <Paketordner>"""
import sys, os, json, glob
P = sys.argv[1].rstrip('/') + '/'
entries = []
for f in sorted(glob.glob(P + '../.lib-entries-*.json')): entries += json.load(open(f))
js = json.load(open(P + 'icons.json'))
js = [e for e in js if 'Library' not in e.get('tags', [])] + entries
names = {e['path'] for e in js}
missing = [e['path'] for e in js if not os.path.exists(P + 'icons/' + e['path'])]
json.dump(js, open(P + 'icons.json', 'w'), indent=1, ensure_ascii=False)
print(len(entries), 'Bibliothek,', len(js), 'gesamt, fehlende Dateien:', len(missing))
