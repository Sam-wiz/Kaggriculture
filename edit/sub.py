"""Rewrite a fraction of the tape's WHEAT plantings into CARROT.

Loss analysis says the agents that beat us plant ~126 wheat to our 195, and more
carrot/melon/strawberry. Wheat is the lowest-value tile on the board (~$60/tile-day
vs carrot ~$80 and far more when a pet cafe unlocks the hinge). Wheat is also feed,
so anything we stop growing has to be bought instead.

Carrot substitutes into a wheat slot better than anything else: wheat waters on ages
0/2/3/4 and harvests at 4; carrot waters the same days and merely starts decaying at
age 4, so the tape's existing WATER/HARVEST schedule still fits.
"""
import importlib.util, os, sys

P = dict(sub_frac=0.0, sub_from=0, sub_to=719, buy_wheat_back=1, seed_swap=1)


def _load_port():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(os.path.dirname(here), "port", "main.py")
    spec = importlib.util.spec_from_file_location("_portmod", path)
    m = importlib.util.module_from_spec(spec)
    sys.modules["_portmod"] = m
    spec.loader.exec_module(m)
    return m


_M = _load_port()
_STATE = {"n": 0}


def agent(obs):
    a = _M.agent(obs)
    f = P["sub_frac"]
    if f <= 0:
        return a
    step = obs.get("step") or 0
    if not (P["sub_from"] <= step < P["sub_to"]):
        return a
    if step == 0:
        _STATE["n"] = 0
    market = list(a.get("market") or [])
    units = [a.get("farmer") or ["PASS"]] + list(a.get("hands") or [])
    swapped = 0
    for i, op in enumerate(units):
        if op and len(op) > 1 and op[0] == "PLANT" and op[1] == "WHEAT":
            _STATE["n"] += 1
            # deterministic every-k-th substitution
            if (_STATE["n"] * f) % 1.0 < f:
                units[i] = ["PLANT", "CARROT"]
                swapped += 1
    if swapped and P["seed_swap"]:
        # make sure the carrot seeds exist: convert wheat seed buys, else add one
        conv = 0
        for j, o in enumerate(market):
            if conv >= swapped:
                break
            if o and o[0] == "BUY_SEED" and len(o) > 2 and o[1] == "WHEAT":
                take = min(int(o[2]), swapped - conv)
                rest = int(o[2]) - take
                market[j] = ["BUY_SEED", "CARROT", take] if rest == 0 else ["BUY_SEED", "WHEAT", rest]
                if rest:
                    market.insert(j + 1, ["BUY_SEED", "CARROT", take])
                conv += take
        if conv < swapped and len(market) < 10:
            market.append(["BUY_SEED", "CARROT", swapped - conv])
    if swapped and P["buy_wheat_back"] and len(market) < 10:
        market.append(["BUY_PRODUCT", "WHEAT", swapped * 2])
    return {"farmer": units[0], "hands": units[1:], "market": market[:10]}
