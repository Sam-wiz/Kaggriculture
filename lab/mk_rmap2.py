"""Emit rm2 variant: L96 + _RMAP2 pair->route overrides (real-engine fitted).
Minimal diff: one dict + one lookup line inside the existing day-6 block."""
import json, sys

BASE = sys.argv[1]                      # e.g. subV_sirxL96.py
OUT = sys.argv[2]                       # e.g. subV_sirxL96_rm2.py
overrides = json.load(open('rmap2_overrides.json'))
table = {tuple(eval(k)): v for k, v in overrides.items()}

src = open(BASE).read()
anchor = "        state['day6']=True"
assert src.count(anchor) == 1, src.count(anchor)
inject = "        state['route']=_RMAP2.get(shops,state['route'])\n" + anchor
src = src.replace(anchor, inject)

# emit dict just before the router def
rdef = "def _router(observation,step,state):"
assert src.count(rdef) == 1
src = src.replace(rdef, f"_RMAP2={table!r}\n" + rdef)
open(OUT, 'w').write(src)
print(f"{OUT}: {len(table)} overrides")
