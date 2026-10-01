"""h_over + an emergency cash floor.

Measured failure mode, from 19 ladder replays: the tape spends ~$2,830 of its $3,000
on day 0 and then runs the entire season on a minimum balance of $0-9. `_do_hire`
silently no-ops when `money < cost`, so if the balance touches zero at the moment the
day's HIRE orders are processed, we get NO hands. One farmer cannot water 19 crops,
every plant becomes a weed within two days, the livestock starves, and the game ends
with a bank of exactly 0. That happened in 18 of 117 games (15%).

The tape's own six-day budget guard cannot save it: it protects the static feed
reserve so strictly that it never fires.

Fix: before the market list is processed, if cash cannot cover the HIRE orders in it,
raise exactly the shortfall by selling the cheapest thing we can spare, hoisted to
slot 0 so it settles before the hires. Market orders execute in list order, so
position is what makes this work. Only fires in the failure mode -- selling early is
otherwise measurably bad.
"""
import importlib.util, os, sys

P = dict(enabled=1, max_units=4, buffer=5.0, last_day=3, min_fails=1)

_HERE = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


_H = _load(os.path.join(_HERE, "port2", "h_over.py"), "_hov_safe")


def _fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


SEED_COST = {"WHEAT": 10, "CARROT": 20, "TOMATO": 50, "STRAWBERRY": 100, "MELON": 80}
ANIMAL_COST = {"GOOSE": 300, "COW": 400, "SHEEP": 500}
LAND = [1000, 2000, 4000]


def agent(obs):
    a = _H.agent(obs)
    if not P["enabled"]:
        return a
    try:
        farm = obs["farms"][obs["player"]]
        market = list(a.get("market") or [])
        if not any(o and o[0] == "HIRE" for o in market):
            return a                       # only hire turns can fail this way
        if int(obs.get("day", 0) or 0) > P["last_day"]:
            return a                       # every observed death spiral began on day 1
        prices = obs["market"]["prices"]
        shed = obs["private"]["shed"]
        # Walk the list exactly as the engine will, so we fire only when the hires
        # genuinely cannot be paid. Orders settle in list order, so everything ahead
        # of the first HIRE moves our balance first -- buys included.
        money = float(farm["money"])
        already = int(farm.get("hires_today", 0) or 0)
        n_quad = len(farm.get("unlocked_quadrants", []) or ["NW"])
        short = 0.0
        n_fail = 0
        for o in market:
            if not o:
                continue
            k = o[0]
            if k == "HIRE":
                cost = _fib(already)
                already += 1
                if money < cost:
                    short += cost - money
                    n_fail += 1
                    money = 0.0
                else:
                    money -= cost
            elif k == "SELL" and len(o) > 2:
                money += min(int(o[2]), shed.get(o[1], 0)) * prices.get(o[1], 0)
            elif k == "BUY_SEED" and len(o) > 2:
                money -= SEED_COST.get(o[1], 0) * int(o[2])
            elif k == "BUY_ANIMAL" and len(o) > 2:
                money -= ANIMAL_COST.get(o[1], 0) * int(o[2])
            elif k == "BUY_PRODUCT" and len(o) > 2:
                money -= prices.get(o[1], 0) * int(o[2])
            elif k == "BUY_LAND":
                money -= LAND[min(2, max(0, n_quad - 1))]
                n_quad += 1
            money = max(0.0, money)
        if short <= 0 or n_fail < P["min_fails"]:
            return a                       # the hires are already funded
        extra = []
        need = short + P["buffer"]
        for p in sorted((p for p in shed if shed.get(p, 0) > 0 and p in prices),
                        key=lambda p: prices[p]):
            if need <= 0 or len(extra) >= 2:
                break
            px = max(1, int(prices[p]))
            k = min(int(shed[p]), int(need // px) + 1, P["max_units"])
            if k > 0:
                extra.append(["SELL", p, k])
                need -= k * px
        if not extra:
            return a
        return {"farmer": a.get("farmer", ["PASS"]), "hands": a.get("hands", []),
                "market": (extra + market)[:10]}
    except Exception:
        return a
