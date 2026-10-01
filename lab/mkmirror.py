"""Add price-impact slot ordering to pipe16, to attack the measured mirror deficit.

Half our real opponents (50.8%, n=63) are >=90% action-identical to our own agent, and we win only
**0.349** of those games -- below the 0.50 a true mirror should produce by construction, so the
same-base-plus-someone's-overlay crowd is beating us there.

Slot ordering is the counter we already measured: orders settle slot-by-slot against the opponent's
order of the same index and every unit moves the shared price, so conceding the first slot on a thin
product costs qty x (price_now - price_after_burst). Against a varied field it is worth only ~+68,
but against an identical opponent it won 0.93 of 120 games with zero ties -- because in a mirror both
sides submit the same orders on the same turns, which is exactly the contested case.

If it works here, closing 0.349 -> 0.93 over 50.8% of games is ~+0.295 win rate.
If it does NOT, the likely reason is that the opponents beating us already run it, and the mirror
deficit needs a different explanation -- which is itself worth knowing.

pipe16 re-inserts `agent` last via `globals().pop('agent')` (Kaggle runs the last callable by
insertion order); the wrapper has to do the same or the bare agent runs.
"""
import os
import sys

OVERLAY = '''

# ---------------------------------------------------------------------------
# OVERLAY: price-impact slot ordering  (Sam-wiz)
# ---------------------------------------------------------------------------
# Targets the mirror matchup: 50.8% of measured opponents are >=90% action-identical to us and we
# win only 0.349 of those. Ranking sells by the dollars lost from conceding slot 0 decided 93% of
# mirror games in an earlier measurement.
_MIR_BURST = 30
_MIR_I0 = 10000
try:
    from kaggle_environments.envs.kaggriculture.kaggriculture import (
        MARKET_PARAMS as _MIR_PARAMS, market_price as _mir_price)
except Exception:
    _MIR_PARAMS, _mir_price = None, None

_mir_base = agent


def _mir_reorder(market, prices, inventory):
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
        if not _MIR_PARAMS or not _mir_price or item not in (_MIR_PARAMS or {}):
            return -(now * qty)
        inv0 = int((inventory or {}).get(item, _MIR_I0) or _MIR_I0)
        return -(qty * max(0.0, now - float(_mir_price(item, inv0 + _MIR_BURST))))

    sells.sort(key=impact)
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


# Kaggle runs the LAST callable by insertion order, and pipe16 itself relies on that
# (`agent = globals().pop('agent')`), so the wrapper must be re-inserted the same way.
globals().pop("agent", None)
agent = _mir_agent
'''

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "subK_pipe16.py"
    out = sys.argv[2] if len(sys.argv) > 2 else "bench_frozen/pipe16_mirror.py"
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    open(out, "w").write(open(src).read() + OVERLAY)
    print("wrote %s (%d bytes) from %s" % (out, os.path.getsize(out), src))
