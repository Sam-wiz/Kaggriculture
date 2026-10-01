"""Does bolting extra hands onto the tape disturb it?

The tape drives hands 0..N-1. Extra hands land at higher indices, so its own actions
keep their slots. But hire COST is fib(hires_today), so our HIRE orders must come
AFTER the tape's in the market list or every one of its hires gets dearer.
"""
import importlib.util, os, sys

P = dict(extra_hands=0, from_day=12, buy_se=0)


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


_H = _load(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "port2", "h_over.py"), "_hov")


def agent(obs):
    a = _H.agent(obs)
    n = P["extra_hands"]
    day = obs.get("day", 0)
    if n <= 0 or day < P["from_day"]:
        return a
    farm = obs["farms"][obs["player"]]
    market = list(a.get("market") or [])
    hands = list(a.get("hands") or [])
    have = len(farm.get("hands", []))
    # our extra hands sit past the tape's, and just idle in this probe
    while len(hands) < have:
        hands.append(["PASS"])
    if obs.get("hour", 0) <= 1:
        room = 10 - len(market)
        for _ in range(min(n, max(0, room))):
            market.append(["HIRE"])          # appended: the tape hires first, cheaply
    if P["buy_se"] and len(farm.get("unlocked_quadrants", [])) < 4 and len(market) < 10:
        market.append(["BUY_LAND"])
    return {"farmer": a.get("farmer", ["PASS"]), "hands": hands, "market": market[:10]}
