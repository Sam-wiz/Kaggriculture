"""Trace the feed pipeline: shed occupancy, wheat on hand, cash, market slots.

A full shed silently blocks BUY_PRODUCT (the engine refuses the commit), and the
10-order cap silently drops whatever the agent appended last -- both of which
starve the herd without any error.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import harness  # noqa: E402


def run(path, opp, seed, day_from=0, day_to=30):
    inner = harness.load_agent(path)
    rows = {}

    def wrapped(obs):
        act = inner(obs)
        d, h = obs["day"], obs["hour"]
        me = obs["player"]
        priv, farm = obs["private"], obs["farms"][me]
        shed = priv["shed"]
        carried = sum(v for iv in priv["inventories"] for k, v in iv.items() if k == "WHEAT")
        n_an = fed = 0
        for row in farm["tiles"]:
            for t in row:
                if isinstance(t, dict) and "animal" in t:
                    n_an += 1
                    fed += 1 if t["fed_today"] else 0
        m = (act or {}).get("market") or []
        r = rows.setdefault(d, dict(shed0=None, wheat0=None, money0=None, an=n_an,
                                    fed=0, buys=0, sells=0, hires=0, trunc=0,
                                    shedmax=0, carry=0))
        if h == 0:
            r["shed0"] = sum(shed.values())
            r["wheat0"] = shed.get("WHEAT", 0)
            r["money0"] = farm["money"]
        r["shedmax"] = max(r["shedmax"], sum(shed.values()))
        r["fed"] = max(r["fed"], fed)
        r["an"] = max(r["an"], n_an)
        r["carry"] = max(r["carry"], carried)
        for o in m[:10]:
            if o and o[0] == "BUY_PRODUCT" and o[1] == "WHEAT":
                r["buys"] += int(o[2])
            elif o and o[0] == "SELL":
                r["sells"] += 1
            elif o and o[0] == "HIRE":
                r["hires"] += 1
        if len(m) > 10:
            r["trunc"] += len(m) - 10
        return act

    r = harness.run_episode(wrapped, opp, seed=seed, catch_errors=False)
    print("%s vs %s seed=%d  bank=%.0f" % (path, opp, seed, r["reward"][0]))
    print(" day  anim  fed  shed@0 wheat@0 shedMAX carryW  money@0  wheatBuy sells hires DROPPED")
    for d in sorted(rows):
        if not (day_from <= d <= day_to):
            continue
        x = rows[d]
        print(" %3d  %4d %4d  %6s %7s %7d %6d %8s %9d %5d %5d %7d"
              % (d, x["an"], x["fed"], x["shed0"], x["wheat0"], x["shedmax"],
                 x["carry"], x["money0"], x["buys"], x["sells"], x["hires"], x["trunc"]))


if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "pass",
        int(sys.argv[3]) if len(sys.argv) > 3 else 1)
