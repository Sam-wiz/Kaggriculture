"""Build three pipe16 overlay variants to separate 'slot ordering is wrong' from 'the overlay is broken'.

The original mirror overlay (mkmirror.py) measured 0.225 vs bare pipe16 and was logged as a
falsified hypothesis. But it returns `sells + rest`, which moves every non-SELL order -- including
HIRE -- behind every sell, and then truncates the list to 10 slots. pipe16 is a hiring-sensitive
agent ("Pipe-16 Idle Workers"), so that is a plausible mechanism for the loss that has nothing to
do with whether price-impact ordering helps.

  passthru  same wrapper machinery, market returned unchanged  -> MUST be 0.500 / all ties
  broken    the original overlay, kept verbatim as the control  -> reproduces 0.225 if diagnosis holds
  posfix    reorder SELLs only among the slots SELLs already occupy; non-SELLs never move; no truncation
"""
import os

HEAD = '''

# --- OVERLAY (%s) -----------------------------------------------------------
_MIR_BURST = 30
_MIR_I0 = 10000
try:
    from kaggle_environments.envs.kaggriculture.kaggriculture import (
        MARKET_PARAMS as _MIR_PARAMS, market_price as _mir_price)
except Exception:
    _MIR_PARAMS, _mir_price = None, None

_mir_base = agent


def _mir_impact(o, prices, inventory):
    item = o[1] if len(o) > 1 else None
    qty = float(o[2]) if len(o) > 2 else 1.0
    now = float((prices or {}).get(item, 0) or 0)
    if not _MIR_PARAMS or not _mir_price or item not in (_MIR_PARAMS or {}):
        return -(now * qty)
    inv0 = int((inventory or {}).get(item, _MIR_I0) or _MIR_I0)
    return -(qty * max(0.0, now - float(_mir_price(item, inv0 + _MIR_BURST))))
'''

PASSTHRU = '''

def _mir_reorder(market, prices, inventory):
    return market


def _mir_agent(observation, configuration=None):
    a = _mir_base(observation, configuration)
    try:
        mkt = observation.get("market") or {}
        m = list((a or {}).get("market") or [])
        if len(m) > 1:
            a = dict(a)
            a["market"] = _mir_reorder(m, mkt.get("prices") or {}, mkt.get("inventory") or {})
    except Exception:
        pass
    return a
'''

BROKEN = '''

def _mir_reorder(market, prices, inventory):
    if not market or len(market) < 2:
        return market
    sells, rest = [], []
    for o in market:
        (sells if (o and o[0] == "SELL") else rest).append(o)
    if len(sells) < 2:
        return market
    sells.sort(key=lambda o: _mir_impact(o, prices, inventory))
    return sells + rest


def _mir_agent(observation, configuration=None):
    a = _mir_base(observation, configuration)
    try:
        mkt = observation.get("market") or {}
        m = list((a or {}).get("market") or [])
        if len(m) > 1:
            a = dict(a)
            a["market"] = _mir_reorder(m, mkt.get("prices") or {},
                                       mkt.get("inventory") or {})[:10]
    except Exception:
        pass
    return a
'''

POSFIX = '''

def _mir_reorder(market, prices, inventory):
    """Sort SELL orders by price impact, but only within the slots SELLs already hold.

    Every non-SELL order (HIRE, BUY_*) keeps its exact index, and the list length is unchanged,
    so the overlay cannot starve hiring or drop orders off the end of a slot cap.
    """
    if not market or len(market) < 2:
        return market
    idx = [i for i, o in enumerate(market) if o and o[0] == "SELL"]
    if len(idx) < 2:
        return market
    ranked = sorted((market[i] for i in idx),
                    key=lambda o: _mir_impact(o, prices, inventory))
    out = list(market)
    for slot, order in zip(idx, ranked):
        out[slot] = order
    return out


def _mir_agent(observation, configuration=None):
    a = _mir_base(observation, configuration)
    try:
        mkt = observation.get("market") or {}
        m = list((a or {}).get("market") or [])
        if len(m) > 1:
            a = dict(a)
            a["market"] = _mir_reorder(m, mkt.get("prices") or {}, mkt.get("inventory") or {})
    except Exception:
        pass
    return a
'''

TAIL = '''

globals().pop("agent", None)
agent = _mir_agent
'''

if __name__ == "__main__":
    src = open("subK_pipe16.py").read()
    for name, body in (("passthru", PASSTHRU), ("broken", BROKEN), ("posfix", POSFIX)):
        out = "bench_frozen/pipe16_%s.py" % name
        open(out, "w").write(src + (HEAD % name) + body + TAIL)
        print("wrote %s (%d bytes)" % (out, os.path.getsize(out)))
