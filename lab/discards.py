"""Count what the engine actually throws away, by product, per game.

This bounds the whole storage thesis before any controller is built. `_drop_inventories_to_shed`
moves each unit's carried inventory into the shed while room remains and silently deletes the rest:

    current = sum(shed.values()); room = max(0, capacity - current)
    take = min(n, room); ... del inv[item]

`del inv[item]` runs whether or not the unit was stored, so anything arriving after the shed fills
is destroyed. Which item loses is decided by iteration order over `private["inventories"]` (farmer
first, then each hand) and by insertion order within each -- i.e. by who picked what up first, not
by value.

If the discarded units are all WHEAT and FERTILIZER, the shed thesis is small: those are the two
items `BUY_PRODUCT` accepts back and their prices barely move. If thin products (WOOL, MILK,
STRAWBERRY, MELON) are being destroyed, the loss is priced at $100-250 a unit and the thesis is
large.
"""
import collections
import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness
from kaggle_environments.envs.kaggriculture import kaggriculture as K

DEEP = ("WHEAT", "FERTILIZER", "EGG")
POOL = [
    "rivals/leoprovorov_kaggriculture-v65/main.py",
    "rivals/tetsutani_shape-the-shop-work-the-pasture-kaggriculture/main.py",
    "rivals/avioon_kaggriculture-apex-v7-god-emperor/main.py",
]


def _job(a):
    agent, opp, seed, swap = a
    lost = collections.Counter()
    stored = collections.Counter()
    orig = K._drop_inventories_to_shed
    seat_of = {}

    def patched(private, capacity):
        shed = private["shed"]
        for inv in private["inventories"]:
            for item, n in list(inv.items()):
                if n <= 0:
                    del inv[item]
                    continue
                current = sum(v for k, v in shed.items())
                room = max(0, capacity - current)
                take = min(n, room)
                if take > 0:
                    shed[item] = shed.get(item, 0) + take
                key = (id(private), item)
                seat_of[key] = seat_of.get(key, 0)
                stored[item] += take
                if n - take > 0:
                    lost[item] += (n - take)
                del inv[item]

    K._drop_inventories_to_shed = patched
    try:
        x, y = (opp, agent) if swap else (agent, opp)
        r = harness.run_episode(x, y, seed=seed, catch_errors=True)
    finally:
        K._drop_inventories_to_shed = orig
    # Both farms share the patched routine, so halve to get a per-player figure.
    return dict(seed=seed, lost=dict(lost), stored=dict(stored),
                reward=(r["reward"][::-1] if swap else r["reward"]))


if __name__ == "__main__":
    idx = json.load(open("data/seedindex_700000_1200.json"))
    hi = [r["seed"] for r in idx if r["yarn"] >= 3][:20]
    rand = [r["seed"] for r in idx][:40]
    agent = sys.argv[1] if len(sys.argv) > 1 else "bench_frozen/A_router.py"
    for label, seeds in (("RANDOM", rand), ("HIGH-YARN (3+)", hi)):
        jobs = [(agent, o, s, sw) for o in POOL for s in seeds for sw in (0, 1)]
        with ProcessPoolExecutor(max_workers=7) as ex:
            res = list(ex.map(_job, jobs, chunksize=4))
        lost = collections.Counter()
        stored = collections.Counter()
        for r in res:
            lost.update(r["lost"])
            stored.update(r["stored"])
        n = len(res)
        print(f"\n{label}: {n} games (both farms counted)")
        print(f"{'item':<14}{'discarded/game':>16}{'stored/game':>14}{'discard rate':>14}")
        for it in sorted(set(lost) | set(stored), key=lambda k: -lost.get(k, 0)):
            L, S = lost.get(it, 0), stored.get(it, 0)
            if L + S == 0:
                continue
            print(f"{it:<14}{L/n:>16.1f}{S/n:>14.1f}{L/max(1,L+S):>13.1%}"
                  f"{'  deep' if it in DEEP else '  THIN'}")
        thin = sum(v for k, v in lost.items() if k not in DEEP)
        print(f"   -> thin-product units destroyed per game (both farms): {thin/n:.1f}")
