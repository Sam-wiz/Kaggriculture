"""Across many seeds, what does the market look like at the end of an h_over
mirror? A product left far BELOW I0 with a high price is demand the tape never
serves -- that is exactly the money an adaptive agent can take without a fight.
"""
import argparse
import os
import statistics
import sys
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import harness  # noqa: E402
from kaggle_environments.envs.kaggriculture import kaggriculture as K  # noqa: E402

PRODUCTS = K.PRODUCTS


def _job(a):
    agent, opp, seed = a
    out = {}

    def on_step(step, state, env):
        if step == 719 or step % 24 == 23:
            m = state[0].observation.market
            out["inv"] = dict(m["inventory"])
            out["price"] = dict(m["prices"])
            out["shops"] = list(state[0].observation.town["unlocked_shops"])

    r = harness.run_episode(agent, opp, seed=seed, on_step=on_step, catch_errors=True)
    assert r["errors"] == [None, None], (seed, r["errors"])
    out["reward"] = r["reward"]
    out["seed"] = seed
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent", default="port2/h_over.py")
    ap.add_argument("--opp", default="port2/h_over.py")
    ap.add_argument("-n", type=int, default=24)
    ap.add_argument("--seed0", type=int, default=3000)
    ap.add_argument("-w", type=int, default=8)
    args = ap.parse_args()
    seeds = list(range(args.seed0, args.seed0 + args.n))
    with ProcessPoolExecutor(max_workers=args.w) as ex:
        res = list(ex.map(_job, [(args.agent, args.opp, s) for s in seeds]))

    print("%s vs %s, %d seeds\n" % (args.agent, args.opp, len(seeds)))
    print("%-12s %9s %9s %9s %9s   %s" %
          ("product", "medPrice", "meanPrice", "minPrice", "maxPrice", "med inv-I0"))
    for p in PRODUCTS:
        pr = sorted(r["price"][p] for r in res)
        inv = sorted(r["inv"][p] - 10000 for r in res)
        print("%-12s %9d %9.0f %9d %9d   %+9d" %
              (p, statistics.median(pr), statistics.mean(pr), pr[0], pr[-1],
               statistics.median(inv)))

    # how often is each product left scarce (price well above base)?
    print("\nseasons where the end price is >= 1.5x base (demand left unserved):")
    for p in PRODUCTS:
        base = K.MARKET_PARAMS[p]["base"]
        n = sum(1 for r in res if r["price"][p] >= 1.5 * base)
        hi = sum(1 for r in res if r["price"][p] >= 3.0 * base)
        print("  %-12s  >=1.5x: %2d/%d   >=3x: %2d/%d" % (p, n, len(res), hi, len(res)))

    c = Counter()
    for r in res:
        c.update(r["shops"])
    print("\nshop draw frequency over %d seasons: %s" % (len(res), dict(c.most_common())))

    # correlate: which shop drives which unserved product
    print("\nmean end price by number of shop instances serving that product:")
    for p in PRODUCTS:
        if p == "FERTILIZER":
            continue
        by = defaultdict(list)
        for r in res:
            k = sum(1 for s in r["shops"] if p in K.SHOPS[s])
            by[k].append(r["price"][p])
        row = "  ".join("%d:%.0f(n%d)" % (k, statistics.mean(v), len(v))
                        for k, v in sorted(by.items()))
        print("  %-12s %s" % (p, row))


if __name__ == "__main__":
    main()
