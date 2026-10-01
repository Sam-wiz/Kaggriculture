"""Route analysis for the causal-shop-router tape.

1. `draw`  -- what shop prefix each seed produces, and whether the tape's own
   route-switch condition (ICE_CREAM, FM, FM  +  rival geese > 1) can fire.
2. `duel`  -- force route 0 vs route 1 and compare, per seed, against the pool.
"""
import argparse
import os
import statistics
import sys
from collections import Counter
from concurrent.futures import ProcessPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import evalpool  # noqa: E402
import harness  # noqa: E402
import tune  # noqa: E402

CAND = os.path.join(ROOT, "port2/h_guard.py")


def draw(seeds):
    hits = 0
    pref = Counter()
    for seed in seeds:
        info = {}

        def probe(obs, _i=info):
            if obs["step"] == 216:
                town = obs["town"]
                _i["shops"] = list(town["unlocked_shops"])
                geese = 0
                for row in obs["farms"][1]["tiles"]:
                    for t in row or []:
                        if isinstance(t, dict) and t.get("animal") == "GOOSE":
                            geese += 1
                _i["geese"] = geese
            return {"farmer": ["PASS"], "hands": [], "market": []}

        harness.run_episode(probe, os.path.join(ROOT, "port/main.py"),
                            seed=seed, catch_errors=False)
        s = info.get("shops", [])
        p = tuple(s[:3])
        pref[p] += 1
        fires = (p == ("ICE_CREAM_SHOP", "FARMERS_MARKET", "FARMERS_MARKET")
                 and info.get("geese", 0) > 1)
        hits += fires
        print(f"seed {seed:>3}: shops[:3]={p}  oppGeese={info.get('geese')}  fires={fires}")
    print(f"\nrule fires on {hits}/{len(seeds)} seeds")
    for p, c in pref.most_common():
        print(f"   {c:>3}  {p}")


def _job(args):
    route, opp, seed, swap = args
    mod = tune.load_module(CAND, {"route": route, "route_step": 216}, tag="rt%d" % route)
    a, b = (opp, mod.agent) if swap else (mod.agent, opp)
    r = harness.run_episode(a, b, seed=seed, catch_errors=True)
    x, y = r["reward"]
    e = list(r["errors"])
    if swap:
        x, y = y, x
        e = [e[1], e[0]]
    return dict(route=route, opp=opp, seed=seed, me=x, them=y, err=e)


def duel(seeds, workers):
    pool = evalpool.available()
    jobs = [(rt, opp, s, sw) for rt in (0, 1) for opp in pool
            for s in seeds for sw in (False, True)]
    with ProcessPoolExecutor(max_workers=workers) as ex:
        res = list(ex.map(_job, jobs))
    bad = [r for r in res if r["err"] != [None, None]]
    if bad:
        print("ERRORS:", len(bad), bad[0]["err"])
    print(f"{'':<10}{'wr':>8}{'bank':>10}{'margin':>10}")
    for rt in (0, 1):
        rs = [r for r in res if r["route"] == rt]
        w = sum(1 for r in rs if r["me"] > r["them"])
        t = sum(1 for r in rs if r["me"] == r["them"])
        print(f"route {rt:<4}{(w + 0.5 * t) / len(rs):>8.3f}"
              f"{statistics.mean(r['me'] for r in rs):>10.0f}"
              f"{statistics.mean(r['me'] - r['them'] for r in rs):>10.0f}"
              f"   {w}W {t}T /{len(rs)}")
    print("\nper-seed mean margin (route0 -> route1):")
    for s in seeds:
        m0 = statistics.mean(r["me"] - r["them"] for r in res if r["route"] == 0 and r["seed"] == s)
        m1 = statistics.mean(r["me"] - r["them"] for r in res if r["route"] == 1 and r["seed"] == s)
        print(f"  seed {s:>3}: {m0:>9.0f} -> {m1:>9.0f}   d={m1 - m0:+.0f}"
              + ("   ROUTE1" if m1 > m0 else ""))
    print("\nper-opponent mean margin (route0 -> route1):")
    for opp in pool:
        m0 = statistics.mean(r["me"] - r["them"] for r in res if r["route"] == 0 and r["opp"] == opp)
        m1 = statistics.mean(r["me"] - r["them"] for r in res if r["route"] == 1 and r["opp"] == opp)
        print(f"  {os.path.basename(os.path.dirname(opp))[:38]:<40}{m0:>9.0f} -> {m1:>9.0f}"
              f"   d={m1 - m0:+.0f}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["draw", "duel"])
    ap.add_argument("-n", type=int, default=8)
    ap.add_argument("--seed0", type=int, default=1)
    ap.add_argument("-w", type=int, default=8)
    a = ap.parse_args()
    seeds = list(range(a.seed0, a.seed0 + a.n))
    if a.cmd == "draw":
        draw(seeds)
    else:
        duel(seeds, a.w)
