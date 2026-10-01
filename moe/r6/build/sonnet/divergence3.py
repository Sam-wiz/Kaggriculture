"""sonnet r6 round2 pt3: redo with market-order padding normalized (drop trailing [] entries,
which are no-ops per AGENTS.md 'invalid actions are silent no-ops'). Find TRUE first divergence
harvest vs c1r2, and characterize c1 vs c1r2 diffs across the full game (macro vs market-only?)."""
import sys, os, json
sys.path.insert(0, "moe/r3/build/opus"); sys.path.insert(0, "kaggriculture-cppsim")
from run import load, act
import kagsim

def norm_market(m):
    return [o for o in (m or []) if o]

def F(a):
    if not isinstance(a, dict): return "x"
    return json.dumps([a.get("farmer"), list(a.get("hands") or []), norm_market(a.get("market"))])

def Ftile(a):  # tile-ops only (farmer+hands), no market
    if not isinstance(a, dict): return "x"
    return json.dumps([a.get("farmer"), list(a.get("hands") or [])])

seed = 9100001
a, _ = load("subAA_harvest.py", "pa"); b, _ = load("subZ_C1R2.py", "pb")
g = kagsim.Game(seed=seed)
diffs = tile_diffs = market_diffs = 0
first = None
for t in range(720):
    o0, o1 = g.observe(0), g.observe(1)
    xa, xb = act(a, o0), act(b, o1)
    d = F(xa) != F(xb)
    if d:
        diffs += 1
        if first is None: first = (t, t // 24, xa, xb)
    if Ftile(xa) != Ftile(xb): tile_diffs += 1
    if norm_market(xa.get("market")) != norm_market(xb.get("market")): market_diffs += 1
    g.step(xa, xb)
print("harvest vs c1r2 (normalized), seed", seed)
print("  total diffs:", diffs, "tile-op diffs:", tile_diffs, "market diffs:", market_diffs)
print("  first real diff:", first)
