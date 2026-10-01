"""Make the tape's sell quantities follow actual stock instead of being hard-coded.

The tape issues fixed quantities ("SELL 40 WOOL on turn 500") sized for the herd it was recorded
with. Measured consequence: the cow->sheep swap produced ~50% more wool and sold 21 FEWER thin
units than the unmodified route, because nothing in the schedule ever ordered the surplus. That is
not a result about herds -- it means every production-side change we have ever tested was measured
through a sell schedule that could not absorb extra output.

This rebinds each scheduled SELL to what is actually in the shed, on the same turns, in the same
slots, in the same order. Nothing else moves: no new sell turns, no reordering, no extra slots.

`cap` bounds how far a quantity may grow (as a multiple of what the tape asked for) so the change
stays a rescale rather than a dump; `cap=0` means unbounded (sell the whole stock).

Sanity check before it is used for anything: on the UNMODIFIED herd this should be roughly neutral.
If it is strongly positive or negative on its own, it is doing something other than what it says.

Usage:  python mkstock.py <out.py> <cap> [src.py]
"""
import os
import sys

TEMPLATE = '''

# ---------------------------------------------------------------------------
# OVERLAY: stock-following sell quantities  (Sam-wiz)
# ---------------------------------------------------------------------------
# Each scheduled SELL is resized to the stock actually held, capped at @CAP@x the tape's own
# quantity (0 = uncapped). Same turns, same slots, same order -- only the number changes. Without
# this the schedule silently truncates any production the recorded route did not anticipate.
_SF = dict(enabled=1, cap=@CAP@, min_day=@MINDAY@, items=@ITEMS@, min_yarn=@YARN@)


def _sf_apply(obs, action):
    if not _SF["enabled"]:
        return action
    try:
        step = obs.get("step")
        step = int(step) if step is not None else int(obs.get("day", 0)) * 24 + int(obs.get("hour", 0))
        if step // 24 < _SF["min_day"]:
            return action
        if _SF["min_yarn"]:
            yarn = list((obs.get("town") or {}).get("unlocked_shops") or []).count("YARN_STORE")
            if yarn < _SF["min_yarn"]:
                return action
        # Stock is shed PLUS what the units are still carrying: production lands in
        # private["inventories"] and only drops into the shed at end of day, so a shed-only
        # reading shows zero surplus at exactly the turns the tape sells on.
        priv = obs.get("private") or {}
        shed = dict(priv.get("shed") or {})
        for _inv in (priv.get("inventories") or []):
            for _k, _v in (_inv or {}).items():
                shed[_k] = shed.get(_k, 0) + int(_v or 0)
        market = action.get("market") or []
        if not shed or not market:
            return action
        # Reserve stock for SELLs already earlier in the list: orders settle slot by slot and
        # two orders for the same item must not both claim it.
        claimed = {}
        out, changed = [], False
        for o in market:
            if o and len(o) > 2 and o[0] == "SELL" and (not _SF["items"] or o[1] in _SF["items"]):
                item = o[1]
                want = int(o[2])
                have = int(shed.get(item, 0) or 0) - claimed.get(item, 0)
                if have > want:
                    lim = have if not _SF["cap"] else min(have, want * _SF["cap"])
                    if lim > want:
                        o = [o[0], item, int(lim)]
                        changed = True
                claimed[item] = claimed.get(item, 0) + int(o[2])
            out.append(o)
        if changed:
            action = dict(action)
            action["market"] = out[:MAX_ORDERS]
    except Exception:
        pass
    return action


_sf_base = agent


def _sf_agent(obs):
    return _sf_apply(obs, _sf_base(obs))


# Kaggle takes the LAST callable by insertion order; rebinding an existing name keeps its original
# slot, so the wrapper has to be re-inserted or the bare route would run.
del agent
agent = _sf_agent
'''

if __name__ == "__main__":
    out = sys.argv[1]
    cap = int(sys.argv[2])
    min_day = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    items = tuple(x for x in (sys.argv[4] or "").split(",") if x) if len(sys.argv) > 4 else ()
    yarn = int(sys.argv[5]) if len(sys.argv) > 5 else 0
    src = sys.argv[6] if len(sys.argv) > 6 else "sub_router_slot.py"
    body = (TEMPLATE.replace("@CAP@", str(cap)).replace("@MINDAY@", str(min_day))
            .replace("@ITEMS@", repr(items)).replace("@YARN@", str(yarn)))
    open(out, "w").write(open(src).read() + body)
    print("wrote %s (cap=%s min_day=%d items=%s min_yarn=%d base=%s) %d bytes"
          % (out, cap or "uncapped", min_day, items or "ALL", yarn, src, os.path.getsize(out)))
