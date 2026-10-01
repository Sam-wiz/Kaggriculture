"""Benchmark remapped V48 vs stock V48 (and pool opps) on held-out seeds.

Usage: bench_remap.py SEED_START N_SEEDS [OPP1,OPP2,...]
"""
import collections
import importlib.util
import json
import os
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness
import route_remap

V48 = "rivals/ahmedberatozer_kaggriculture-v48-clear-the-queue/_entry.py"

OPPS = {
    "v45": "rivals/ahmedberatozer_kaggriculture-v45-first-turn-wheat-round-trip/_entry.py",
    "aurax7": "rivals/aurax7_kaggriculture-shop-router-reactive-v7/_entry.py",
    "pipe7": "rivals/nathanjacob_kaggriculture-pipe-7-wheat-microstructure/_entry.py",
    "v48": "rivals/ahmedberatozer_kaggriculture-v48-clear-the-queue/_entry.py",
}


def load_module():
    spec = importlib.util.spec_from_file_location("v48m", V48)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def full_agent(m):
    return [v for v in vars(m).values() if callable(v)][-1]


def kload(path):
    env = {}
    exec(compile(open(path).read(), path, "exec"), env)  # noqa: S102
    return [v for v in env.values() if callable(v)][-1]


SHOPS = ["BAKERY", "BRUNCH_SPOT", "YARN_STORE", "PET_CAFE", "PIZZA_SHOP",
         "ICE_CREAM_SHOP", "SMOOTHIE_SHOP", "FARMERS_MARKET"]


def build_remap():
    rows = route_remap.load()
    pmap = route_remap.pair_means(rows)
    smap = route_remap.single_means(rows)
    pc = collections.Counter(tuple(r["shops2"]) for r in rows)
    out = {}
    for a in SHOPS:
        for b in SHOPS:
            t = (a, b)
            out[t] = route_remap.remap_pick(t, pmap, smap, pair_counts=dict(pc))
    return out


def job(arg):
    seed, oppname, sw = arg
    stock = load_module()
    rem = load_module()
    for t, rid in build_remap().items():
        rem._R108_SHOP_ROUTES[t] = rid
        rem._R110_OLD_SHOPS[t] = rid
    a_stock = full_agent(stock)
    a_rem = full_agent(rem)
    a_opp = a_stock if oppname == "v48" else kload(OPPS[oppname])
    res = {}
    for name, agent in (("rem", a_rem), ("stock", a_stock)):
        x, y = (a_opp, agent) if sw else (agent, a_opp)
        r = harness.run_episode(x, y, seed=seed, catch_errors=True)
        p, q = r["reward"][::-1] if sw else r["reward"]
        res[name] = p - q
    return seed, oppname, sw, res


if __name__ == "__main__":
    start = int(sys.argv[1])
    n = int(sys.argv[2])
    oppnames = sys.argv[3].split(",") if len(sys.argv) > 3 else list(OPPS)
    args = [(s, o, sw) for s in range(start, start + n)
            for o in oppnames for sw in (0, 1)]
    byopp = collections.defaultdict(lambda: {"w": 0, "l": 0, "m": []})
    with ProcessPoolExecutor(7) as ex:
        for seed, oppname, sw, res in ex.map(job, args):
            d = res["rem"] - res["stock"]
            st = byopp[oppname]
            st["m"].append(d)
            if d > 0:
                st["w"] += 1
            elif d < 0:
                st["l"] += 1
    for o, st in byopp.items():
        print("%-8s rem-vs-stock W%d-L%d mean %+6.0f" % (
            o, st["w"], st["l"], statistics.mean(st["m"])))
