"""Did our hires actually happen? Compare HIRE orders issued to hands held."""
import json, glob, sys

f = glob.glob('mine/raw/*.json')
if not f:
    sys.exit()
d = json.load(open(f[0]))
steps = d['steps']
t = d['info']['TeamNames']
me = 0 if t[0] == 'Sam-wiz' else 1
hires = [0] * 31
held = [0] * 31
for i, s in enumerate(steps[:719]):
    day = i // 24
    a = s[me].get('action')
    if isinstance(a, dict):
        hires[day] += sum(1 for o in (a.get('market') or []) if o and o[0] == 'HIRE')
    if i % 24 == 12:
        held[day] = len(s[0]['observation']['farms'][me].get('hands', []))
short = [(dd, hires[dd], held[dd]) for dd in range(1, 30) if held[dd] < hires[dd]]
lost = sum(h - k for _, h, k in short)
print("ep %s vs %-18s bank %9.0f  short-days %2d  hands lost %3d  %s"
      % (sys.argv[1], t[1 - me][:18], d['rewards'][me], len(short), lost, short[:4]))
