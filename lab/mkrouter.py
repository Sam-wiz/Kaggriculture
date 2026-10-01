"""Build sub_router_slot.py = thomastschinkel's public-state router + our price-impact slot ordering.

Orders settle slot-by-slot against the opponent's slot of the same index, and every unit moves the
shared price, so the cost of conceding the earliest slot is qty x (price_now - price_after_burst).
That is our one independently measured market edge, and the router does not do it: it has
clamp_sells (drop unfillable SELLs) and dead_stock (dump doomed produce) but never reorders.
"""
import io, os

BASE = "sub_router.py"
OUT = "sub_router_slot.py"

OVERLAY = '''

# ---------------------------------------------------------------------------
# OVERLAY: price-impact slot ordering  (Sam-wiz)
# ---------------------------------------------------------------------------
# The market settles order slot 0 against the opponent's slot 0, slot 1 against theirs, and so on,
# and each unit sold moves the shared price. So conceding the first slot on a thin product costs
# qty x (price_now - price_after_their_burst). MILK/WOOL/STRAWBERRY halve after 31-42 surplus
# units while WHEAT and EGG barely move, which is why ranking by price impact beats ranking by
# raw order value. Measured on the previous base: +729 on holdout seeds (44W-4L).
_SO_BURST = 30
_SO_I0 = 10000
try:
    from kaggle_environments.envs.kaggriculture.kaggriculture import (
        MARKET_PARAMS as _SO_PARAMS, market_price as _so_price)
except Exception:
    _SO_PARAMS, _so_price = None, None


def _so_reorder(market, prices, inventory):
    if not market or len(market) < 2:
        return market
    sells, rest = [], []
    for o in market:
        (sells if (o and o[0] == "SELL") else rest).append(o)
    if len(sells) < 2:
        return market

    def impact(o):
        item = o[1] if len(o) > 1 else None
        qty = float(o[2]) if len(o) > 2 else 1.0
        now = float((prices or {}).get(item, 0) or 0)
        if not _SO_PARAMS or not _so_price or item not in (_SO_PARAMS or {}):
            return -(now * qty)
        inv0 = int((inventory or {}).get(item, _SO_I0) or _SO_I0)
        later = float(_so_price(item, inv0 + _SO_BURST))
        return -(qty * max(0.0, now - later))

    sells.sort(key=impact)
    return sells + rest


_so_base_agent = agent


def _so_agent(obs):
    a = _so_base_agent(obs)
    try:
        mkt = obs.get("market") or {}
        m = list(a.get("market") or [])
        if len(m) > 1:
            a = dict(a)
            a["market"] = _so_reorder(m, mkt.get("prices") or {},
                                      mkt.get("inventory") or {})[:MAX_ORDERS]
    except Exception:
        pass
    return a


# Kaggle's loader takes the LAST callable by insertion order, and rebinding an existing name keeps
# its original position -- so the wrapper has to be re-inserted, or the bare router would run.
del agent
agent = _so_agent
'''

src = open(BASE).read()
open(OUT, "w").write(src + OVERLAY)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
