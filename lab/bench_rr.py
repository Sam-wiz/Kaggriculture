"""Round-robin among candidate agents, paired seeds x both seats."""
import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

AGENTS = {
    "v45": "subF_v45.py",
    "v44": "subG_v44.py",
    "v48": "rivals/ahmedberatozer_kaggriculture-v48-clear-the-queue/_entry.py",
    "v47": "rivals/ahmedberatozer_kaggriculture-v47-reactive-market-coordination/v47_main.py",
    "v46": "rivals/ahmedberatozer_kaggriculture-v46-first-turn-microstructure-and-s/_entry.py",
    "pipe7": "rivals/nathanjacob_kaggriculture-pipe-7-wheat-microstructure/_entry.py",
    "aurax7": "rivals/aurax7_kaggriculture-shop-router-reactive-v7/_entry.py",
    "alperen": "rivals/alperen5252525_kaggriculture-ready-stock-earlier-sales/_entry.py",
}


def kload(path):
    src = open(path).read()
    env = {}
    exec(compile(src, path, "exec"), env)  # noqa: S102
    return [v for v in env.values() if callable(v)][-1]


def _job(a):
    pa, pb, s, sw = a
    fa = kload(pa)
    fb = kload(pb)
    x, y = (fb, fa) if sw else (fa, fb)
    r = harness.run_episode(x, y, seed=s, catch_errors=True)
    p, q = r["reward"][::-1] if sw else r["reward"]
    return (pa, pb, s, sw, p, q, r["errors"])


def main():
    seeds = list(range(2000, 2040))
    names = sys.argv[1].split(",") if len(sys.argv) > 1 else list(AGENTS)
    pairs = [(AGENTS[a], AGENTS[b]) for i, a in enumerate(names) for b in names[i + 1:]]
    jobs = [(pa, pb, s, sw) for (pa, pb) in pairs for s in seeds for sw in (0, 1)]
    with ProcessPoolExecutor(max_workers=7) as ex:
        res = list(ex.map(_job, jobs, chunksize=2))
    rec = {}
    for (pa, pb, s, sw, p, q, errs) in res:
        d = rec.setdefault((pa, pb), {"w": 0, "l": 0, "t": 0, "m": []})
        d["w" if p > q else "l" if p < q else "t"] += 1
        d["m"].append(p - q)
    inv = {v: k for k, v in AGENTS.items()}
    for (pa, pb), d in sorted(rec.items(), key=lambda kv: -sum(kv[1]["m"])):
        n = len(d["m"])
        print(f"{inv[pa]:8s} vs {inv[pb]:8s}  W{d['w']}-L{d['l']}-T{d['t']}  margin={sum(d['m'])/n:+8,.0f}")


if __name__ == "__main__":
    main()
