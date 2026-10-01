"""Port the h_over market-model sell overlay onto the public-state router.

Why this and not another parameter: the router's sell schedule is baked into its tape. Tracing 69
losses showed the shed sitting at 76-100 of its 100-item cap through days 18-25 -- and overflow is
DISCARDED, not stored -- while the tape places market orders on only 89 of 719 turns and rarely
uses more than a few of its ten slots. Late production is being destroyed for want of an order.

The h_over overlay is the one thing we ever built that models this properly: it estimates each
product's town drain rate from the unlocked shops, projects future shop unlocks, forecasts the price
after that drain, and meters sales against a shed target. It was worth +3,361 on the old tape and
has never been run on the router.

The only incompatible piece is `_sched_window`, which asks "how many units of X does the tape still
plan to sell between steps lo and hi" off a cumulative table keyed by h_over's tape encoding. The
router already answers exactly that question through `Agent.future_sells`, so the overlay is handed
the live Agent as its `route` handle and the window is a difference of two of its calls.

Usage:  python mkmodel.py <out.py> [src.py]
"""
import os
import re
import sys

SRC_OVERLAY = "port2/h_over.py"
START = "_OV_CROPS = {"
END = "_OVERLAYS = [_Overlay(), _Overlay()]"

PRELUDE = '''

# ---------------------------------------------------------------------------
# OVERLAY: market-model selling  (Sam-wiz, ported from our h_over build)
# ---------------------------------------------------------------------------
# Names below are lifted verbatim from port2/h_over.py so the model is not re-derived; only the
# tape-schedule lookup is rebound to the router. Checked for collisions against the router module:
# none of these names exist there.
_PRODUCTS = tuple(PRODUCTS)
K_TURNS = TURNS
CFG_MAX_ORDERS = MAX_ORDERS


def _read(value, key, default=None):
    try:
        if isinstance(value, dict):
            return value.get(key, default)
        return getattr(value, key, default)
    except Exception:
        return default


def _count(mapping, name):
    try:
        return int((mapping or {}).get(name, 0) or 0)
    except Exception:
        return 0


def _is_animal(item):
    return item in ANIMALS
'''

EPILOGUE = '''

def _sched_window(route, item, lo, hi):
    """Units of `item` the router's CURRENT tail still plans to sell over steps lo..hi.

    `route` is the live router Agent; `future_sells(item, s)` is the total it sells from step s to
    the end of the episode, so the window is the difference of the two endpoints.
    """
    lo = max(0, int(lo))
    hi = min(K_TURNS - 1, int(hi))
    if hi < lo:
        return 0
    try:
        return max(0, route.future_sells(item, lo) - route.future_sells(item, hi + 1))
    except Exception:
        return 0


_OVERLAYS = [_Overlay(), _Overlay()]
_mm_base = agent


def _mm_agent(obs):
    action = _mm_base(obs)
    try:
        step = obs.get("step")
        step = int(step) if step is not None else int(obs.get("day", 0)) * 24 + int(obs.get("hour", 0))
        seat = int(obs.get("player", 0) or 0)
        ov = _OVERLAYS[seat]
        if step == 0 or step < ov.last_step:
            ov.reset(step)
        # _A is the router's live Agent; it carries the selected tail and its future-sell table.
        return ov(action, obs, step, _A, {})
    except Exception:
        return action


# Kaggle takes the LAST callable by insertion order; rebinding an existing name keeps its original
# slot, so the wrapper has to be re-inserted or the bare route would run.
del agent
agent = _mm_agent
'''


def extract():
    src = open(SRC_OVERLAY).read()
    i = src.index(START)
    j = src.index(END)
    block = src[i:j]
    # _OV_CUM is built from h_over's tape encoding and is replaced by the router's future_sells.
    block = re.sub(r"# _OV_CUM.*?\n_OV_CUM = \[\].*?\n(?=\n\ndef |\n\nclass )", "",
                   block, flags=re.S)
    block = re.sub(r"def _sched_window\(route, item, lo, hi\):.*?\n(?=\n\ndef |\n\nclass )", "",
                   block, flags=re.S)
    return block


if __name__ == "__main__":
    out = sys.argv[1]
    base = sys.argv[2] if len(sys.argv) > 2 else "sub_router_slot.py"
    block = extract()
    for gone in ("_OV_CUM", "def _sched_window"):
        if gone in block:
            sys.exit("ERROR: %s survived extraction -- fix the regex before shipping" % gone)
    open(out, "w").write(open(base).read() + PRELUDE + "\n" + block + EPILOGUE)
    print("wrote %s (%d bytes, overlay block %d bytes)"
          % (out, os.path.getsize(out), len(block)))
