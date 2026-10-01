"""C1-D: append an outermost stream-decorrelation layer to a C1-family file.
Native premium SELLs (MILK/WOOL/STRAWBERRY) are deferred by D ticks (or a per-order jitter in [1, D]) on steps
[LO, HI), except on steps where PREDICT/PREDICT2 fired (their pre-emptive dumps are left untouched). Deferred slots
become [] holes so the other orders keep their slot priority; released sells go to slot 0.
usage: mkdc.py BASE.py OUT.py D MODE(delay|jitter)
"""
import hashlib, sys

LAYER = r'''

# ---------------------------------------------------------------------------
# Sam-wiz opusb r4 2026-09-26: C1-D stream decorrelation (outermost layer).
# Band forecasters match our premium-sale ticks (+-1) against library streams of the public shepherd family;
# shifting our NATIVE premium sells by a few ticks breaks the match. PREDICT/PREDICT2 dumps are never shifted.
# ---------------------------------------------------------------------------
import random as _dc_random
_DC_PARENT = kaggle_submission_agent
_DC_ITEMS = ("MILK", "WOOL", "STRAWBERRY")
_DC_D = __D__
_DC_MODE = "__MODE__"
_DC_LO, _DC_HI = 150, 690
_DC = {}
_DC_REPORT = dict(entered=0, deferred_orders=0, deferred_units=0, released_orders=0, skipped_pred=0, held_full=0, errors=0)


def _dc_fires():
    return (_V92_P_REPORT.get("pred_fires", 0), _V92_Q_REPORT.get("pred_fires", 0))


def _dc_apply(obs, action, st, fired):
    step = int(obs["step"])
    market = [list(o) if isinstance(o, (list, tuple)) else o for o in (action.get("market") or [])]
    changed = False
    if _DC_LO <= step < _DC_HI:
        if fired:
            _DC_REPORT["skipped_pred"] += 1
        else:
            for k, o in enumerate(market):
                if isinstance(o, list) and len(o) >= 3 and o[0] == "SELL" and o[1] in _DC_ITEMS and int(o[2]) > 0:
                    d = _DC_D if _DC_MODE == "delay" else st["rng"].randint(1, _DC_D)
                    st["q"].append([step + d, o[1], int(o[2])])
                    market[k] = []
                    _DC_REPORT["deferred_orders"] += 1; _DC_REPORT["deferred_units"] += int(o[2])
                    changed = True
    due = [x for x in st["q"] if x[0] <= step or step >= _DC_HI]
    if due:
        merged = {}
        for x in due:
            merged[x[1]] = merged.get(x[1], 0) + x[2]
        keep = [x for x in st["q"] if x not in due]
        for item, qty in merged.items():
            while len(market) >= 10 and market and market[-1] == []:
                market.pop()
            if len(market) >= 10:
                keep.append([step + 1, item, qty]); _DC_REPORT["held_full"] += 1
                continue
            market.insert(0, ["SELL", item, qty]); _DC_REPORT["released_orders"] += 1
            changed = True
        st["q"] = keep
    if not changed:
        return action
    return dict(action, market=market[:10])


def dc_agent(observation, configuration=None):
    player, step = int(observation["player"]), int(observation["step"])
    st = _DC.get(player)
    if st is None or step <= st["step"]:
        st = _DC[player] = {"step": -1, "q": [], "rng": _dc_random.Random(1000003 * (player + 1))}
    st["step"] = step
    f0 = _dc_fires()
    action = _DC_PARENT(observation, configuration)
    try:
        _DC_REPORT["entered"] += 1
        return _dc_apply(observation, action, st, _dc_fires() != f0)
    except Exception:
        _DC_REPORT["errors"] += 1
        return action


globals().pop("agent", None)
agent = dc_agent
'''

if __name__ == "__main__":
    base, out, D, mode = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
    src = open(base).read()
    assert "kaggle_submission_agent" in src and "_V92_Q_REPORT" in src and "_V92_P_REPORT" in src
    new = src + LAYER.replace("__D__", str(D)).replace("__MODE__", mode)
    open(out, "w").write(new)
    print(out, "md5", hashlib.md5(new.encode()).hexdigest(), "size", len(new))
