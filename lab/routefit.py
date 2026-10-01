"""Panel for re-fitting the router's three decisions against LIVE opponents.

The published thresholds were fitted on recorded tape panels (opponent plays a fixed recorded
route). Against agents that react to us, the market features move differently, so the same rule
can select the wrong tail. This collects, for every (seed, opponent) cell:

  * the margin under each of the four tails, run to completion
  * the public-state feature the router would read at each decision turn

The tails are byte-identical before the turn that selects them, so f226 is the same in all of
them; f360 must be read on a YARN game and f433 on a MAIN game, because that is the tail the
router is standing on when it evaluates them.
"""
import json, os, statistics, sys
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

TAILS = ["MAIN", "YARN", "YARN_CARROT", "MILK_GLUT"]
PATH = {t: "bench_frozen/T_%s.py" % t for t in TAILS}
POOL = [
 ("wheat-remembers", "rivals/prvsiyan_where-the-wheat-remembers-tomorrow-kaggriculture/main.py"),
 ("lynn-math", "rivals/lynnsakurai_farming-score-a-mathematical-approach/main.py"),
 ("apex-v7", "rivals/avioon_kaggriculture-apex-v7-god-emperor/main.py"),
 ("tetsutani-new", "rivals/tetsutani_shape-the-shop-work-the-pasture-kaggriculture/main.py"),
 ("v65", "rivals/leoprovorov_kaggriculture-v65/main.py"),
 ("moon-melons", "rivals/prvsiyan_kaggriculture-frontier-the-moon-counts-melons/main.py"),
 ("yhay-2929", "rivals/yhay81_public-match-history-router-rating-2929-aug-30/main.py"),
 ("x578", "rivals/stevenleehans_kaggriculture-x578-i-m-the-strongest/main.py"),
]
TURNS = (226, 360, 433)


def _job(a):
    tail, opp, seed, swap = a
    feats = {}

    def on_step(step, state, env):
        if step in TURNS:
            o = state[0].observation
            feats[step] = dict(
                yarn=(o.get("town", {}).get("unlocked_shops") or []).count("YARN_STORE"),
                px_carrot=o["market"]["prices"].get("CARROT", 0),
                inv_milk=o["market"]["inventory"].get("MILK", 0))
    me, them = (opp, PATH[tail]) if swap else (PATH[tail], opp)
    r = harness.run_episode(me, them, seed=seed, copy_obs=True, on_step=on_step,
                            catch_errors=True)
    p, q = r["reward"][::-1] if swap else r["reward"]
    return dict(tail=tail, opp=opp, seed=seed, swap=swap, me=p, them=q, feats=feats)


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    seed0 = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
    seeds = list(range(seed0, seed0 + n))
    jobs = [(t, p, s, sw) for t in TAILS for _, p in POOL for s in seeds for sw in (0, 1)]
    print(f"{len(jobs)} games", flush=True)
    with ProcessPoolExecutor(max_workers=7) as ex:
        res = list(ex.map(_job, jobs, chunksize=4))
    out = "data/routepanel_%d_%d.json" % (seed0, n)
    json.dump(res, open(out, "w"))
    print("wrote", out)
    for t in TAILS:
        m = [r["me"] - r["them"] for r in res if r["tail"] == t]
        print(f"  {t:<12} margin {statistics.mean(m):>+9,.0f}  wr {sum(1 for x in m if x>0)/len(m):.3f}")
