"""Hybrid #2: the yhay81 fieldbook tape + the same selling overlay as h1.

yhay81 already ships a one-step lead-sale overlay (`sell_lead`), vetoed on any
turn where the town consumes. This variant switches that off and substitutes the
window shape h1 measured as best -- pull the tape's next few scheduled sales
into this turn, sized by how far the current turn sits from a consumption tick.

The tape branches: it picks one of six routes at step 144 / 216, so the schedule
is not a single static array. The route the runtime committed to is readable off
`runtime.route_state`, which is what the lookahead indexes.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _base  # noqa: E402

_M = _base.load("yhay81", "h2")

PRODUCTS = list(_M.PRODUCTS)

P = dict(
    mode="lookahead",       # 'off' | 'lookahead'
    native_lead=0,          # 1 -> keep yhay81's own one-step lead sale as well
    items=["STRAWBERRY", "MILK", "WOOL", "FERTILIZER", "MELON", "CARROT", "TOMATO", "EGG"],
    win4=[0, 4, 3, 2],      # pull window by step %% 4
    lookahead=40,
    wheat=1,
    wheat_days=1.0,
    wheat_start=300,
    min_price=2.0,
)

_RUNTIME = _M.FieldbookRuntime(sell_lead=False)
_AGENT_STATE = {0: {"last": -1}, 1: {"last": -1}}


def _route(player):
    st = _RUNTIME.route_state.get(player)
    return st["route"] if st else 0


def _sched(route, step, item):
    if not 0 <= step < 719:
        return 0
    total = 0
    for o in (_M.ROUTES[route][step].get("market") or []):
        if o and o[0] == "SELL" and len(o) >= 3 and o[1] == item:
            try:
                total += max(0, int(o[2]))
            except (TypeError, ValueError):
                pass
    return total


def _n_animals(own):
    n = 0
    for row in (_M._get(own, "tiles", []) or []):
        for t in row or []:
            if isinstance(t, dict) and "animal" in t:
                n += 1
    return n


def overlay(obs, action, step, player, own):
    market = [list(o) for o in (action.get("market") or [])]
    projected = _M._projected_shed(obs, action, None)
    prices = _M._get(_M._get(obs, "market", {}) or {}, "prices", {}) or {}
    route = _route(player)
    window = min(int(P["lookahead"]), int(P["win4"][step % 4]))
    if window <= 0:
        return action

    items = [i for i in P["items"] if i in PRODUCTS]
    if P["wheat"] and step >= int(P["wheat_start"]):
        items = items + ["WHEAT"]
    animals = _n_animals(own)

    for item in items:
        stock = max(0, int(projected.get(item, 0) or 0))
        if item == "WHEAT":
            stock -= int(animals * P["wheat_days"])
        already = sum(max(0, int(o[2])) for o in market
                      if len(o) >= 3 and o[0] == "SELL" and o[1] == item)
        surplus = stock - already
        if surplus <= 0:
            continue
        if float(_M._get(prices, item, 0) or 0) < P["min_price"]:
            continue
        want = sum(_sched(route, step + d, item) for d in range(1, window + 1))
        want = min(surplus, want)
        if want <= 0:
            continue
        hit = next((o for o in market
                    if len(o) >= 3 and o[0] == "SELL" and o[1] == item), None)
        if hit is not None:
            hit[2] = max(0, int(hit[2])) + want
        elif len(market) < 10:
            market.append(["SELL", item, int(want)])
    action["market"] = market[:10]
    return action


def agent(obs, configuration=None):
    _RUNTIME.settings["sell_lead"] = bool(P["native_lead"])
    action = _RUNTIME.act(obs, configuration)
    if P["mode"] == "off":
        return action
    try:
        step = min(max(_M._step(obs), 0), 718)
        player, own, _ = _M._farm_pair(obs)
        return overlay(obs, action, step, player, own)
    except Exception:
        return action
