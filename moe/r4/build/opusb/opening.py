"""Print each candidate's first 3 market lists + first land-buy step (kagsim, self-play vs PASS)."""
import sys, os, json
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT); sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from run import load, act, PASS
import kagsim
for path in sys.argv[1:]:
    fn, m = load(path, "op")
    g = kagsim.Game(seed=12345); ms = []; land = []
    for t in range(300):
        o = g.observe(0); a = act(fn, o)
        mk = a.get("market") or []
        if len(ms) < 3 and mk: ms.append(mk)
        if any(x and x[0] == "BUY_LAND" for x in mk): land.append(t + 1)
        g.step(a, PASS)
    print(path, "|", " || ".join(",".join(" ".join(map(str, x)) for x in mm) for mm in ms)[:260], "| land", land)
