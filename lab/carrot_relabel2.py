"""Bounded carrot-boost relabel: relabel up to n mid-season wheat plants to
carrot inside routes chosen for pet/FM first-2-shop pairs. Mutates tapes inside
the already-built chassis so the full outer wrapper stack (terminal
liquidation + E182 planner) stays intact. Seed buy injected >=1 day before the
first relabeled plant (market settles after unit ops).
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


def demand_routes(m):
    """Route ids whose first-2-shop pair contains carrot-draining shops."""
    return {r for p, r in m._R108_SHOP_ROUTES.items()
            if "PET_CAFE" in p or "FARMERS_MARKET" in p}


def build_agent(n_relabel=14, lo=10, hi=17, routes_filter=None):
    m = load_module()
    want = demand_routes(m) if routes_filter is None else routes_filter
    routes = m._IMPL.chassis.routes
    totals = {}
    for rid in list(routes):
        if rid not in want:
            continue
        tape = copy.deepcopy(routes[rid])
        wheat_ops = []
        for i, a in enumerate(tape):
            day = i // 24
            if not (lo <= day <= hi):
                continue
            for unit, op in enumerate([a.get("farmer")] + list(a.get("hands") or [])):
                if op and op[0] == "PLANT" and len(op) > 1 and op[1] == "WHEAT":
                    wheat_ops.append((i, unit))
        take = wheat_ops[:n_relabel]
        for i, unit in take:
            if unit == 0:
                tape[i]["farmer"][1] = "CARROT"
            else:
                tape[i]["hands"][unit - 1][1] = "CARROT"
        totals[rid] = len(take)
        if take:
            buy_day = take[0][0] // 24 - 1
            tape[buy_day * 24].setdefault("market", []).append(
                ["BUY_SEED", "CARROT", len(take)])
        routes[rid] = tape
    agent = [v for v in vars(m).values() if callable(v)][-1]
    return agent, totals


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import harness
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    agent, totals = build_agent(n)
    print("relabeled per-route counts:", sorted(set(totals.values())),
          "on", len(totals), "routes")
    r = harness.run_episode(agent, "pass", seed=3, catch_errors=True)
    print("vs pass:", r["reward"], r.get("errors"))
