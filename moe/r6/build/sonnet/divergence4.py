"""sonnet r6 round2 pt4: bucket the 89 harvest-vs-c1r2 diffs by day and by op-type on 3 seeds,
to see if they cluster late-game (Yujin Cha's d17-25 mirror-dump claim) or are spread out,
and whether market diffs are SELL-quantity/timing vs different items entirely."""
import sys, os, json, collections
sys.path.insert(0, "moe/r3/build/opus"); sys.path.insert(0, "kaggriculture-cppsim")
from run import load, act
import kagsim

def norm_market(m):
    return [o for o in (m or []) if o]

def market_ops(m):
    return sorted(o[0] for o in norm_market(m))

for seed in (9100001, 9100002, 9100003):
    a, _ = load("subAA_harvest.py", "pa"); b, _ = load("subZ_C1R2.py", "pb")
    g = kagsim.Game(seed=seed)
    day_bucket = collections.Counter()
    op_bucket = collections.Counter()
    tile_days = []
    for t in range(720):
        o0, o1 = g.observe(0), g.observe(1)
        xa, xb = act(a, o0), act(b, o1)
        ma, mb = norm_market(xa.get("market")), norm_market(xb.get("market"))
        tile_a = (xa.get("farmer"), list(xa.get("hands") or []))
        tile_b = (xb.get("farmer"), list(xb.get("hands") or []))
        if ma != mb:
            day_bucket[t // 24] += 1
            opa, opb = market_ops(ma), market_ops(mb)
            op_bucket[(tuple(opa), tuple(opb))] += 1
        if tile_a != tile_b:
            tile_days.append(t // 24)
        g.step(xa, xb)
    print(f"seed {seed}: market-diff days (count>=2): {[(d,c) for d,c in sorted(day_bucket.items()) if c>=1]}")
    print(f"  tile-op diff days: {sorted(set(tile_days))}")
    print(f"  top op-type swaps: {op_bucket.most_common(6)}")
