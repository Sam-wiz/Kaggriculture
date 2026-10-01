"""Tape surgery v2: relabel last-week wheat plants -> carrot inside V48 routes.

The tape runs a late carrot program already (BUY_SEED CARROT ~day 25, terminal
SELL CARROT ~day 29). We relabel only wheat plant ops in the final ~6 days so
early cashflow is untouched, inject carrot seed buys next to the tape's own,
and rely on the existing terminal liquidation for sales.
"""
import copy
import importlib.util
import os
import sys

V48 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "rivals/ahmedberatozer_kaggriculture-v48-clear-the-queue/_entry.py")


def load_module():
    spec = importlib.util.spec_from_file_location("v48mod", V48)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def build_agent(n_relabel, relabel_from_day=23, seed_day=24, relabel_routes=None):
    """V48 with up to n_relabel wheat plant ops (from relabel_from_day onward)
    swapped to carrot, per route. Seed buy injected at seed_day."""
    m = load_module()
    routes = copy.deepcopy(m._ROUTES)
    totals = {}
    for rid, tape in routes.items():
        if relabel_routes is not None and rid not in relabel_routes:
            continue
        wheat_ops = []
        for i, a in enumerate(tape):
            if i // 24 < relabel_from_day:
                continue
            for unit, op in enumerate([a.get("farmer")] + list(a.get("hands") or [])):
                if op and op[0] == "PLANT" and len(op) > 1 and op[1] == "WHEAT":
                    wheat_ops.append((i, unit))
        take = wheat_ops[:n_relabel] if n_relabel else wheat_ops
        for i, unit in take:
            if unit == 0:
                tape[i]["farmer"][1] = "CARROT"
            else:
                tape[i]["hands"][unit - 1][1] = "CARROT"
        totals[rid] = len(take)
        if take:
            mk = tape[seed_day * 24].setdefault("market", [])
            mk.append(["BUY_SEED", "CARROT", len(take)])
    agent = m.make_agent(routes, router=m._router, **m._SETTINGS)
    return agent, totals


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import harness
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    agent, totals = build_agent(n)
    print("relabeled per-route counts:", sorted(set(totals.values())))
    r = harness.run_episode(agent, "pass", seed=3, catch_errors=True)
    print("vs pass:", r["reward"], r.get("errors"))
