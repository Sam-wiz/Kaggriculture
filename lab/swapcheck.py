"""Verify the herd swap actually fires, and that it changes the farm the way it is supposed to.

A layer that loads cleanly and never triggers looks identical to its base and reads as "safe".
This counts the swaps, the animals actually standing in the pasture at the end, and the wool sold,
against the unmodified router on the same seeds.
"""
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

BASE = "bench_frozen/A_router.py"


def run(agent_path, seed, opp):
    orders = collections.Counter()
    animals = {}

    def on_step(step, state, env):
        a = state[0].action or {}
        for o in (a.get("market") or []):
            if o and o[0] in ("BUY_ANIMAL",):
                orders[o[1]] += int(o[2]) if len(o) > 2 else 1
            elif o and o[0] == "SELL":
                orders["SELL_" + o[1]] += int(o[2]) if len(o) > 2 else 1
        if step >= 700:
            farm = state[0].observation.farms[0]
            c = collections.Counter()
            for row in farm["tiles"]:
                for cell in row:
                    if isinstance(cell, dict) and cell.get("animal"):
                        c[cell["animal"]] += 1
                    elif isinstance(cell, dict) and cell.get("kind") in ("COW", "SHEEP", "GOOSE"):
                        c[cell["kind"]] += 1
            animals.clear()
            animals.update(c)

    r = harness.run_episode(agent_path, opp, seed=seed, copy_obs=False, on_step=on_step,
                            catch_errors=True)
    return r["reward"], orders, dict(animals)


if __name__ == "__main__":
    idx = json.load(open("data/seedindex_700000_1200.json"))
    hi = [r["seed"] for r in idx if r["yarn"] >= 3][:6]
    lo = [r["seed"] for r in idx if r["yarn"] == 0][:3]
    cand = sys.argv[1] if len(sys.argv) > 1 else "bench_frozen/S_y2s3.py"
    opp = "rivals/leoprovorov_kaggriculture-v65/main.py"
    print(f"candidate: {cand}\nopponent : {opp}\n")
    print(f"{'seed':>8}{'yarn':>5}  {'agent':<10}{'bank':>9}{'COWbuy':>8}{'SHPbuy':>8}"
          f"{'woolSold':>10}{'milkSold':>10}")
    for tag, seeds in (("HIGH", hi), ("ZERO", lo)):
        for s in seeds:
            y = next(r["yarn"] for r in idx if r["seed"] == s)
            for nm, p in (("base", BASE), ("swap", cand)):
                rew, o, an = run(p, s, opp)
                print(f"{s:>8}{y:>5}  {nm:<10}{rew[0]:>9,.0f}{o.get('COW',0):>8}"
                      f"{o.get('SHEEP',0):>8}{o.get('SELL_WOOL',0):>10}{o.get('SELL_MILK',0):>10}")
            print()
