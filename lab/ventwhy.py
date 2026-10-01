"""If the vent is not preventing discards, what is it doing?

Engine-level counting says the base route destroys ~2 thin units per player per game -- a $200-500
ceiling. The vent is worth +374. So the gain cannot be overflow rescue, and the explanation I wrote
into NOTES.md is wrong.

Three candidates, separated here:
  (a) it sells MORE units in total  -> the tape simply under-sells its production
  (b) it sells the SAME units EARLIER -> a timing/price effect, not a volume effect
  (c) it changes WHICH products are sold -> a mix effect

Also re-runs the discard count on the herd-swap variant, which pinned the shed at 100 for six days:
if the swap's extra wool really was destroyed, its discard count must be far above the base's.
"""
import collections
import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness
from kaggle_environments.envs.kaggriculture import kaggriculture as K

POOL = [
    "rivals/leoprovorov_kaggriculture-v65/main.py",
    "rivals/tetsutani_shape-the-shop-work-the-pasture-kaggriculture/main.py",
    "rivals/avioon_kaggriculture-apex-v7-god-emperor/main.py",
]
THIN = ("STRAWBERRY", "MILK", "WOOL", "MELON", "CARROT", "TOMATO")


def _job(a):
    agent, opp, seed, swap = a
    lost = collections.Counter()
    orig = K._drop_inventories_to_shed

    def patched(private, capacity):
        shed = private["shed"]
        for inv in private["inventories"]:
            for item, n in list(inv.items()):
                if n <= 0:
                    del inv[item]
                    continue
                room = max(0, capacity - sum(v for v in shed.values()))
                take = min(n, room)
                if take > 0:
                    shed[item] = shed.get(item, 0) + take
                if n - take > 0:
                    lost[item] += (n - take)
                del inv[item]

    sold = collections.Counter()
    revenue = [0.0]
    seat = [1 if swap else 0]

    def on_step(step, state, env):
        act = state[seat[0]].action or {}
        px = state[0].observation.market["prices"]
        for o in (act.get("market") or []):
            if o and o[0] == "SELL" and len(o) > 2:
                sold[o[1]] += int(o[2])
                sold["_turns"] += 0
                revenue[0] += int(o[2]) * float(px.get(o[1], 0) or 0)
        if act.get("market"):
            if any(o and o[0] == "SELL" for o in act["market"]):
                sold["_sellturns"] += 1

    K._drop_inventories_to_shed = patched
    try:
        x, y = (opp, agent) if swap else (agent, opp)
        r = harness.run_episode(x, y, seed=seed, copy_obs=False, on_step=on_step,
                                catch_errors=True)
    finally:
        K._drop_inventories_to_shed = orig
    rew = r["reward"][::-1] if swap else r["reward"]
    return dict(agent=agent, lost=dict(lost), sold=dict(sold), rev=revenue[0],
                bank=rew[0], margin=rew[0] - rew[1])


if __name__ == "__main__":
    idx = json.load(open("data/seedindex_700000_1200.json"))
    seeds = [r["seed"] for r in idx][200:230]
    cands = sys.argv[1:] or ["bench_frozen/A_router.py", "bench_frozen/V_80_10_12.py",
                             "bench_frozen/S_y1s4.py"]
    jobs = [(c, o, s, sw) for c in cands for o in POOL for s in seeds for sw in (0, 1)]
    with ProcessPoolExecutor(max_workers=7) as ex:
        res = list(ex.map(_job, jobs, chunksize=4))
    print(f"{len(seeds)} seeds x {len(POOL)} opponents x 2 seats = "
          f"{len(seeds)*len(POOL)*2} games per candidate\n")
    print(f"{'candidate':<24}{'margin':>9}{'unitsSold':>11}{'thinSold':>10}"
          f"{'sellTurns':>11}{'thinLost':>10}{'ordRev':>11}")
    for c in cands:
        g = [r for r in res if r["agent"] == c]
        n = len(g)
        us = sum(sum(v for k, v in r["sold"].items() if not k.startswith("_")) for r in g) / n
        th = sum(sum(v for k, v in r["sold"].items() if k in THIN) for r in g) / n
        st = sum(r["sold"].get("_sellturns", 0) for r in g) / n
        tl = sum(sum(v for k, v in r["lost"].items() if k in THIN) for r in g) / n
        rv = sum(r["rev"] for r in g) / n
        mg = sum(r["margin"] for r in g) / n
        print(f"{os.path.basename(c):<24}{mg:>+9,.0f}{us:>11.0f}{th:>10.0f}"
              f"{st:>11.0f}{tl:>10.1f}{rv:>11,.0f}")
    print("\n(thinLost counts BOTH farms; ordRev = sum of qty x price-at-order, an upper bound "
          "on revenue that ignores the impact of each unit)")
