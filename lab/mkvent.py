"""Build a router variant that sells surplus when the shed is about to overflow.

Measured: the router's shed sits at 76-100 of its 100-item cap through days 18-25, and
`_drop_inventories_to_shed` only takes `room = capacity - current` -- everything above the cap is
silently discarded. So late-season production is being destroyed, and any attempt to produce MORE
(the demand-matched herd) is destroyed first: swapping four cows for sheep pinned the shed at 100
for six days and *reduced* wool sold from 196 to 191.

The router places market orders on only 89 of 719 turns and never uses more than a few of the ten
slots, so the capacity to sell exists; the tape simply has no order scheduled. This adds SELL orders
for whatever is crowding the shed, into slots the tape left empty, and only:

  * when the shed is at or above `hi` of 100, so it never competes with a healthy schedule
  * for products whose price is still above `min_px`, so it does not dump into a floored market
  * appended AFTER the tape's own orders, so it can never displace a scheduled sale
    (orders settle slot-by-slot, and the tape's slot assignment is worth real money)

Usage:  python mkvent.py <out.py> <hi> <min_px> <max_qty> [src]
"""
import os
import sys

TEMPLATE = '''

# ---------------------------------------------------------------------------
# OVERLAY: shed vent  (Sam-wiz)
# ---------------------------------------------------------------------------
# The shed caps at 100 and overflow is discarded, not stored. Through days 18-25 the route runs at
# 76-100, so produce is being thrown away while 9 of the 10 market slots sit empty on the turns the
# tape does trade. This sells the surplus into those empty slots -- never displacing a tape order,
# never into a floored market.
_VENT = dict(enabled=1, hi=@HI@, min_px=@MINPX@, max_qty=@MAXQTY@)
_VENT_SKIP = ("FERTILIZER",)   # an input to FERTILIZE, not just a product; dumping it costs yield


def _vent_apply(obs, action):
    if not _VENT["enabled"]:
        return action
    try:
        priv = obs.get("private") or {}
        shed = {k: int(v) for k, v in (priv.get("shed") or {}).items() if v}
        if not shed:
            return action
        used = sum(shed.values())
        if used < _VENT["hi"]:
            return action
        market = list(action.get("market") or [])
        free = MAX_ORDERS - len(market)
        if free <= 0:
            return action
        prices = (obs.get("market") or {}).get("prices") or {}
        already = set(o[1] for o in market if o and len(o) > 1 and o[0] == "SELL")
        cand = []
        for item, qty in shed.items():
            if item in _VENT_SKIP or item in already or item not in PRODUCTS:
                continue
            px = float(prices.get(item, 0) or 0)
            if px < _VENT["min_px"]:
                continue
            cand.append((px * min(qty, _VENT["max_qty"]), item, min(qty, _VENT["max_qty"])))
        if not cand:
            return action
        cand.sort(reverse=True)
        action = dict(action)
        for _, item, qty in cand[:free]:
            market.append(["SELL", item, int(qty)])
        action["market"] = market[:MAX_ORDERS]
    except Exception:
        pass
    return action


_vent_base = agent


def _vent_agent(obs):
    return _vent_apply(obs, _vent_base(obs))


# Kaggle takes the LAST callable by insertion order; rebinding an existing name keeps its original
# slot, so the wrapper has to be re-inserted or the bare route would run.
del agent
agent = _vent_agent
'''

if __name__ == "__main__":
    out = sys.argv[1]
    hi, min_px, max_qty = int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
    src_path = sys.argv[5] if len(sys.argv) > 5 else "sub_router_slot.py"
    body = TEMPLATE
    for tok, val in (("@HI@", hi), ("@MINPX@", min_px), ("@MAXQTY@", max_qty)):
        body = body.replace(tok, str(val))
    open(out, "w").write(open(src_path).read() + body)
    print("wrote %s (hi=%d min_px=%g max_qty=%d, base=%s) %d bytes"
          % (out, hi, min_px, max_qty, src_path, os.path.getsize(out)))
