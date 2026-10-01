"""Bank/margin AND action mix for a set of parameter overrides.

The point is to see whether a change that improves the bank does it by doing
MORE work or by doing better-paid work -- moves per productive action is the
number that separates the two.
"""
import argparse
import json
import os
import statistics
import sys
from collections import Counter
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import harness  # noqa: E402
import tune  # noqa: E402

MOVES = ("NORTH", "SOUTH", "EAST", "WEST")
SHED = ("PICKUP", "DROP")


def _job(job):
    path, params, opp, seed, swap = job
    mod = tune.load_module(path, params)
    ops = Counter()
    inner = mod.agent

    def wrapped(obs):
        a = inner(obs)
        for u in [a.get("farmer") or ["PASS"]] + list(a.get("hands") or []):
            if u:
                ops["MOVE" if u[0] in MOVES else u[0]] += 1
        return a

    a, b = (opp, wrapped) if swap else (wrapped, opp)
    r = harness.run_episode(a, b, seed=seed, catch_errors=True)
    x, y = r["reward"]
    if swap:
        x, y = y, x
    assert r["errors"] == [None, None], r["errors"]
    tot = sum(ops.values())
    shed = sum(ops[k] for k in SHED)
    work = tot - ops["MOVE"] - ops["PASS"] - shed
    return dict(me=x, opp=y, work=work, move=ops["MOVE"], pass_=ops["PASS"],
                shed=shed, plant=ops["PLANT"], water=ops["WATER"],
                harv=ops["HARVEST"], tot=tot)


def run(path, cfgs, opp, seeds, workers):
    print("%-40s %8s %9s %7s %7s %7s %6s %6s %6s" %
          ("config", "bank", "margin", "work", "move", "mv/wk", "plant", "water", "pass"))
    for label, params in cfgs:
        jobs = []
        for s in seeds:
            jobs.append((path, params, opp, s, False))
            jobs.append((path, params, opp, s, True))
        with ProcessPoolExecutor(max_workers=workers) as ex:
            res = list(ex.map(_job, jobs))
        m = lambda k: statistics.mean(r[k] for r in res)  # noqa: E731
        print("%-40s %8.0f %9.0f %7.0f %7.0f %7.2f %6.0f %6.0f %6.0f" %
              (label[:40], m("me"), m("me") - m("opp"), m("work"), m("move"),
               m("move") / max(1, m("work")), m("plant"), m("water"), m("pass_")))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("agent")
    ap.add_argument("--opp", default="port2/h_over.py")
    ap.add_argument("-n", type=int, default=12)
    ap.add_argument("--seed0", type=int, default=3000)
    ap.add_argument("-w", type=int, default=4)
    ap.add_argument("--cfgs", required=True,
                    help='JSON list of [label, params] pairs')
    a = ap.parse_args()
    run(a.agent, json.loads(a.cfgs), a.opp,
        list(range(a.seed0, a.seed0 + a.n)), a.w)
