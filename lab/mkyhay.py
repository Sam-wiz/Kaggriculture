"""Package yhay81's Shop Router 0908 for submission, plain and with our slot-ordering edge.

The kernel ships a tar.gz of main.py + observation.py + model.json + actions.json, and recovers its
own directory through `agent.__code__.co_filename` because Kaggle's loader omits `__file__`. That
detail matters here: the overlay rebinds the module-level name `agent`, and the original function
reads that same global to find its folder, so the folder is captured from the ORIGINAL function
object before the rebind rather than left to resolve later.

Variant B adds price-impact slot ordering. Orders settle slot-by-slot against the opponent's order
of the same index and every unit moves the shared price, so conceding the first slot on a thin
product costs qty x (price_now - price_after_burst). It is worth little against the field (+68) but
wins 93% of MIRROR matches, and a notebook with 61 votes on its first day will be widely cloned --
which is exactly the matchup it is for.
"""
import os
import shutil
import subprocess
import sys

SRC = "rivals/yhay81_shop-router-0908/pkg"
FILES = ("main.py", "observation.py", "model.json", "actions.json")

OVERLAY = '''

# ---------------------------------------------------------------------------
# OVERLAY: price-impact slot ordering  (Sam-wiz)
# ---------------------------------------------------------------------------
_SO_BURST = 30
_SO_I0 = 10000
try:
    from kaggle_environments.envs.kaggriculture.kaggriculture import (
        MARKET_PARAMS as _SO_PARAMS, market_price as _so_price)
except Exception:
    _SO_PARAMS, _so_price = None, None

_so_base = agent
# Capture the package folder from the ORIGINAL function: the router resolves its own directory by
# reading the global name `agent`, which the rebind below would otherwise repoint at the wrapper.
_SO_DIR = Path(_so_base.__code__.co_filename).resolve().parent


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
        return -(qty * max(0.0, now - float(_so_price(item, inv0 + _SO_BURST))))

    sells.sort(key=impact)
    return sells + rest


def _so_agent(observation, configuration=None):
    global _ROUTER
    if _ROUTER is None:
        _ROUTER = Router(_SO_DIR)
    a = _so_base(observation, configuration)
    try:
        mkt = observation.get("market") or {}
        m = list(a.get("market") or [])
        if len(m) > 1:
            a = dict(a)
            a["market"] = _so_reorder(m, mkt.get("prices") or {},
                                      mkt.get("inventory") or {})[:10]
    except Exception:
        pass
    return a


# Kaggle takes the LAST callable by insertion order; rebinding an existing name keeps its original
# slot, so the wrapper has to be re-inserted or the bare router would run.
del agent
agent = _so_agent
'''


def build(outdir, overlay=False):
    if os.path.isdir(outdir):
        shutil.rmtree(outdir)
    os.makedirs(outdir)
    for f in FILES:
        shutil.copy(os.path.join(SRC, f), os.path.join(outdir, f))
    if overlay:
        with open(os.path.join(outdir, "main.py"), "a") as fh:
            fh.write(OVERLAY)
    tar = outdir + ".tar.gz"
    if os.path.exists(tar):
        os.remove(tar)
    subprocess.run(["tar", "-czf", os.path.basename(tar)] + list(FILES),
                   cwd=outdir, check=True)
    shutil.move(os.path.join(outdir, os.path.basename(tar)), tar)
    print("built %s  (%d bytes)%s" % (tar, os.path.getsize(tar),
                                      "  [+slot ordering]" if overlay else ""))
    return tar


if __name__ == "__main__":
    build("subA_router0908", overlay=False)
    build("subB_router0908_slot", overlay=True)
