"""Diagnostic: where does the money come from in a contested game?

Wraps both agents, logs every market order they issue, and samples the shared
market (inventory + price) once per day. Reports per-product realised revenue,
units sold, and the end-of-season price -- which is what tells us which markets
were left scarce (= free money) and which were glutted.

Usage: python adaptive/probe.py <agentA> [agentB] [--seed S]
"""
import argparse
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import harness  # noqa: E402
from kaggle_environments.envs.kaggriculture import kaggriculture as K  # noqa: E402

PRODUCTS = K.PRODUCTS


class Logger:
    """Wrap an agent, record its market orders and its observed state."""

    def __init__(self, spec, name):
        self.fn = harness.load_agent(spec, name)
        self.name = name
        self.orders = []          # (step, order)
        self.money = []           # (step, money)
        self.tiles_day = defaultdict(lambda: defaultdict(int))
        self.ops = defaultdict(int)

    def __call__(self, obs):
        act = self.fn(obs)
        me = obs["player"]
        step = obs["step"]
        farm = obs["farms"][me]
        self.money.append((step, farm["money"]))
        if isinstance(act, dict):
            for u in [act.get("farmer") or ["PASS"]] + list(act.get("hands") or []):
                if u:
                    o = u[0]
                    self.ops["MOVE" if o in ("NORTH", "SOUTH", "EAST", "WEST") else o] += 1
        if isinstance(act, dict):
            for o in (act.get("market") or [])[:10]:
                self.orders.append((step, list(o)))
        if step % 24 == 0:
            d = obs["day"]
            comp = self.tiles_day[d]
            for row in farm["tiles"]:
                for t in row:
                    if t is None:
                        comp["EMPTY"] += 1
                    elif t == "LOCKED":
                        comp["LOCKED"] += 1
                    elif t.get("kind") == "PLANT":
                        comp["p:" + t["crop"]] += 1
                    elif t.get("kind") == "WEED":
                        comp["WEED"] += 1
                    elif "animal" in t:
                        comp["a:" + t["animal"]] += 1
                    else:
                        comp["s:" + t["kind"]] += 1
        return act


FILLS = {}          # (farm_id, op, item) -> [count, value]
_FARM_IDS = {}      # id(farm dict) -> player index


def _install_fill_tracker():
    """Record every ACTUAL market fill. Order quantities are requests; the engine
    stops an order when the shed runs dry or money runs out, so only the commit
    path tells the truth about revenue."""
    orig = K._commit_unit
    orig_pm = K._process_market

    def pm(state, env):
        # farms live in state[0]; register their identities before any commit
        for i, f in enumerate(state[0].observation.farms):
            _FARM_IDS[id(f)] = i
        return orig_pm(state, env)

    K._process_market = pm

    def wrapped(op, item, price, farm, private, market, shed_capacity=100):
        ok = orig(op, item, price, farm, private, market, shed_capacity)
        if ok:
            pid = _FARM_IDS.get(id(farm), -1)
            k = (pid, op, item)
            e = FILLS.setdefault(k, [0, 0.0])
            e[0] += 1
            e[1] += price
        return ok

    K._commit_unit = wrapped
    return orig, orig_pm


def run(a, b, seed):
    la, lb = Logger(a, "A"), Logger(b, "B")
    inv_trace = []
    shops_trace = []
    FILLS.clear()
    _FARM_IDS.clear()
    orig, orig_pm = _install_fill_tracker()

    def on_step(step, state, env):
        if step % 24 == 23:
            m = state[0].observation.market
            inv_trace.append((step // 24, dict(m["inventory"]), dict(m["prices"])))
            shops_trace.append(sorted(state[0].observation.town["unlocked_shops"]))

    try:
        r = harness.run_episode(la, lb, seed=seed, on_step=on_step, catch_errors=True)
    finally:
        K._commit_unit = orig
        K._process_market = orig_pm
    assert r["errors"] == [None, None], r["errors"]
    return r, la, lb, inv_trace, shops_trace


def fill_report():
    """Per-player, per-item realised sales and purchases."""
    out = {0: {}, 1: {}}
    for (pid, op, item), (n, v) in FILLS.items():
        if pid not in out:
            continue
        out[pid].setdefault(item, {})[op] = (n, v)
    return out


def revenue(logger, inv_trace):
    """Approximate realised revenue by replaying SELL order quantities against the
    daily price sample. Order quantities are requests, not fills, so this is an
    upper bound -- use `units` from market inventory deltas for the truth."""
    by = defaultdict(lambda: [0, 0.0])   # product -> [ordered_units, est_value]
    price_at = {}
    for d, inv, pr in inv_trace:
        price_at[d] = pr
    for step, o in logger.orders:
        if not o or o[0] != "SELL":
            continue
        d = step // 24
        p = o[1]
        q = int(o[2]) if len(o) > 2 else 0
        by[p][0] += q
        by[p][1] += q * price_at.get(d, price_at.get(0, {})).get(p, 0)
    return by


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("a")
    ap.add_argument("b", nargs="?", default="port2/h_over.py")
    ap.add_argument("--seed", type=int, default=1000)
    args = ap.parse_args()

    r, la, lb, inv_trace, shops_trace = run(args.a, args.b, args.seed)
    print("seed", args.seed, " banks", r["reward"])
    print("\nfinal shops:", shops_trace[-1])
    from collections import Counter
    print("shop counts:", dict(Counter(shops_trace[-1])))

    fr = fill_report()
    _, endinv, endpr = inv_trace[-1]
    print("\nREALISED FILLS (units / $ / $ per unit)")
    print("%-12s %9s %8s   %-22s %-22s" % ("product", "endInv", "endPr", "A sold", "B sold"))
    tot = [0.0, 0.0]
    for p in PRODUCTS:
        cells = []
        for pid in (0, 1):
            n, v = fr[pid].get(p, {}).get("SELL", (0, 0.0))
            tot[pid] += v
            cells.append("%5d %9.0f %6.1f" % (n, v, v / n if n else 0))
        print("%-12s %9d %8d   %-22s %-22s" % (p, endinv[p], endpr[p], cells[0], cells[1]))
    print("%-12s %9s %8s   %5s %9.0f %6s   %5s %9.0f" %
          ("TOTAL SALES", "", "", "", tot[0], "", "", tot[1]))
    print("\nBUYS (units / $)")
    for pid in (0, 1):
        row = []
        for item, ops in sorted(fr[pid].items()):
            for op, (n, v) in ops.items():
                if op != "SELL":
                    row.append("%s %s x%d $%.0f" % (op[4:], item, n, v))
        print("  %s: %s" % ("AB"[pid], ", ".join(row)))

    print("\nACTION MIX")
    keys = sorted(set(la.ops) | set(lb.ops))
    print("  %-22s %8s %8s" % ("op", "A", "B"))
    for k in keys:
        print("  %-22s %8d %8d" % (k, la.ops.get(k, 0), lb.ops.get(k, 0)))
    for nm, lg in (("A", la), ("B", lb)):
        tot = sum(lg.ops.values())
        prod = tot - lg.ops.get("MOVE", 0) - lg.ops.get("PASS", 0)
        print("  %s: total %d, productive %d (%.1f%%), move %d, pass %d"
              % (nm, tot, prod, 100.0 * prod / max(1, tot),
                 lg.ops.get("MOVE", 0), lg.ops.get("PASS", 0)))

    print("\nprice trajectory (day: " + " ".join("%-6s" % p[:6] for p in PRODUCTS) + ")")
    for d, inv, pr in inv_trace:
        if d % 3 == 0 or d >= 28:
            print("  d%-3d " % d + " ".join("%-6d" % pr[p] for p in PRODUCTS))

    print("\ntile composition (A):")
    keys = sorted({k for d in la.tiles_day.values() for k in d})
    print("  day  " + " ".join("%-7s" % k[:7] for k in keys))
    for d in sorted(la.tiles_day):
        if d % 4 == 0 or d == 29:
            print("  %-4d " % d + " ".join("%-7d" % la.tiles_day[d].get(k, 0) for k in keys))
    print("\ntile composition (B):")
    keys = sorted({k for d in lb.tiles_day.values() for k in d})
    print("  day  " + " ".join("%-7s" % k[:7] for k in keys))
    for d in sorted(lb.tiles_day):
        if d % 4 == 0 or d == 29:
            print("  %-4d " % d + " ".join("%-7d" % lb.tiles_day[d].get(k, 0) for k in keys))


if __name__ == "__main__":
    main()
