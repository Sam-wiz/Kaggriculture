# Tape-match: run agents_v8.py on the same seed as a 吃白饭 episode and compare the
# team's recorded actions vs our agent's output, step by step (unit ops + market).
import gzip, json, sys, os
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from run import load, act
import kagsim

EP = "mine/top10/112239186.json.gz"   # fish seat 1, seed 1856189715
d = json.load(gzip.open(EP))
seat = 1
rec = [a[seat] for a in d["actions"]]
opp = [a[1 - seat] for a in d["actions"]]

a, _ = load("rivalsGH/r34l-rudr44_kaggriculture/agents_v8.py", "a")
g = kagsim.Game(seed=int(d["seed"]))
N = min(96, len(rec))
match_u = match_m = 0
first_diff = None
for t in range(N):
    mine = act(a, g.observe(seat))
    theirs = rec[t]
    mu = (mine.get("farmer"), tuple(tuple(x) for x in (mine.get("hands") or []))) == \
         (theirs.get("farmer"), tuple(tuple(x) for x in (theirs.get("hands") or [])))
    mm = [tuple(o) for o in (mine.get("market") or [])] == [tuple(o) for o in (theirs.get("market") or [])]
    match_u += mu; match_m += mm
    if not (mu and mm) and first_diff is None:
        first_diff = (t, mine, theirs)
    if seat == 1:
        g.step(opp[t], mine)
    else:
        g.step(mine, opp[t])

print(f"steps: {N}; unit-op match {match_u}/{N} = {match_u/N:.0%}; market match {match_m}/{N} = {match_m/N:.0%}")
if first_diff:
    t, m, th = first_diff
    print("first diff at step", t)
    print("  mine:   ", json.dumps(m)[:220])
    print("  theirs: ", json.dumps(th)[:220])
