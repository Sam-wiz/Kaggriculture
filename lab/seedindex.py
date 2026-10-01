"""Index seeds by their shop draw, by simulation.

The draw cannot be precomputed from the seed: `_end_of_day` shares one RNG between `_spawn_weeds`
and the shop choice, and weed spawning draws once per EMPTY tile on both farms, so how much land
each player has unlocked and planted shifts the stream. The draw is therefore a function of play.

Running router self-play makes it deterministic again (both seats fixed), which is all we need to
build a seed set where a given product's demand is extreme.
"""
import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

AGENT = "bench_frozen/A_router.py"


def _job(seed):
    shops = {}

    def on_step(step, state, env):
        if step % 24 == 23:
            shops[step] = list((state[0].observation.town or {}).get("unlocked_shops") or [])

    try:
        harness.run_episode(AGENT, AGENT, seed=seed, copy_obs=False, on_step=on_step,
                            catch_errors=True)
    except Exception:
        return None
    final = shops.get(max(shops)) if shops else []
    at9 = shops.get(9 * 24 + 23, [])
    return dict(seed=seed, shops=sorted(final), yarn=final.count("YARN_STORE"),
                yarn_d9=at9.count("YARN_STORE"))


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 600
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 700000
    with ProcessPoolExecutor(max_workers=7) as ex:
        res = [r for r in ex.map(_job, range(start, start + n), chunksize=8) if r]
    out = "data/seedindex_%d_%d.json" % (start, n)
    json.dump(res, open(out, "w"))
    import collections
    c = collections.Counter(r["yarn"] for r in res)
    print(f"{len(res)} seeds -> {out}")
    print("YARN_STORE count distribution (router self-play):")
    for k in sorted(c):
        print(f"   {k}: {c[k]:>5}  ({c[k]/len(res):>5.1%})")
    hi = [r for r in res if r["yarn"] >= 3]
    print(f"\n3+: {len(hi)} seeds")
    print("  first 24:", [r["seed"] for r in hi[:24]])
    print("\nis the day-9 count predictive?  final mean by day-9 count:")
    b = collections.defaultdict(list)
    for r in res:
        b[r["yarn_d9"]].append(r["yarn"])
    for k in sorted(b):
        print(f"   day9={k}: n={len(b[k]):>4}  mean final {sum(b[k])/len(b[k]):.2f}")
