"""sonnet r6 round2: where does Harvest's (subAA) tape first diverge from C1R2's (subZ)?
Both share C1's opening per opusb (48-step identity 1.00). If the margin is post-opening
executor divergence (my r1 causal claim), the first differing action should land well past
step 48, and market SELL-order divergence should be visible near it."""
import sys, os, json
sys.path.insert(0, "moe/r3/build/opus"); sys.path.insert(0, "kaggriculture-cppsim")
from run import load, act
import kagsim

def F(a):
    return json.dumps([a.get("farmer"), list(a.get("hands") or []), a.get("market") or []]) if isinstance(a, dict) else "x"

CANDS = {"harvest": "subAA_harvest.py", "c1r2": "subZ_C1R2.py", "c1": "subY_C1_predict2.py"}
N = 300  # ~12.5 days; enough to see if divergence is early (macro) or late (executor)
SEEDS = list(range(9100001, 9100004))

for name_a, name_b in [("harvest", "c1r2"), ("harvest", "c1"), ("c1", "c1r2")]:
    path_a, path_b = CANDS[name_a], CANDS[name_b]
    first_diffs = []
    for seed in SEEDS:
        a, _ = load(path_a, "pa"); b, _ = load(path_b, "pb")
        g = kagsim.Game(seed=seed)
        first = None
        for t in range(N):
            o0, o1 = g.observe(0), g.observe(1)
            xa, xb = act(a, o0), act(b, o1)
            if F(xa) != F(xb) and first is None:
                first = t
            g.step(xa, xb)
        first_diffs.append(first)
    print(name_a, "vs", name_b, "first-diff steps:", first_diffs)
