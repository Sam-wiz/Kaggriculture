"""sonnet r6 round2 pt2: characterize the harvest-vs-c1r2 divergence at/after step 121,
and check c1 vs c1r2 over the FULL game (720 steps) to close my r1 item #3 (stale-kill check)."""
import sys, os, json
sys.path.insert(0, "moe/r3/build/opus"); sys.path.insert(0, "kaggriculture-cppsim")
from run import load, act
import kagsim

def F(a):
    return json.dumps([a.get("farmer"), list(a.get("hands") or []), a.get("market") or []]) if isinstance(a, dict) else "x"

seed = 9100001
a, _ = load("subAA_harvest.py", "pa"); b, _ = load("subZ_C1R2.py", "pb")
g = kagsim.Game(seed=seed)
diffs = 0
first5 = []
for t in range(160):
    o0, o1 = g.observe(0), g.observe(1)
    xa, xb = act(a, o0), act(b, o1)
    if F(xa) != F(xb):
        diffs += 1
        if len(first5) < 6:
            first5.append((t, t//24, t%24, xa, xb))
    g.step(xa, xb)
print("harvest vs c1r2: diffs in steps 0-159:", diffs)
for row in first5:
    print(row)

# c1 vs c1r2 over full 720
a2, _ = load("subY_C1_predict2.py", "pa"); b2, _ = load("subZ_C1R2.py", "pb")
g2 = kagsim.Game(seed=seed)
diffs2 = 0
first_diff2 = None
for t in range(720):
    o0, o1 = g2.observe(0), g2.observe(1)
    xa, xb = act(a2, o0), act(b2, o1)
    if F(xa) != F(xb):
        diffs2 += 1
        if first_diff2 is None:
            first_diff2 = (t, t//24, xa, xb)
    g2.step(xa, xb)
print("c1 vs c1r2 full-720 diffs:", diffs2, "first:", first_diff2)
