"""Build a router variant that trades cows for sheep when the draw is wool-heavy.

Measured on 69 lost episodes: our herd is frozen at 8 SHEEP / 9 COW in every draw, while opponents
shift to 12/6 as YARN_STOREs accumulate. Median margin by yarn count: -1,412 (0), -2,053 (1),
-2,764 (2), -16,062 (3), -19,652 (4). Our wool output stays at 196 units; theirs reaches 301.

COW and SHEEP share PASTURE and both eat one wheat a day, so the swap needs no new building and no
extra feed -- only $100 more per head. Both sides already buy their animals on days 8-11, and by
day 9 the observed YARN_STORE count correlates 0.67 with the final count, so the information is in
hand before the purchase the tape is already making.

This rewrites BUY_ANIMAL COW orders to SHEEP in that window. It does not add orders, so the cash
schedule moves by at most $100 per swapped head.

Usage:  python mkswap.py <out.py> <min_yarn> <max_swap> [from_day] [to_day]
"""
import os
import sys

TEMPLATE = '''

# ---------------------------------------------------------------------------
# OVERLAY: demand-matched herd  (Sam-wiz)
# ---------------------------------------------------------------------------
# The tape buys a fixed 8 SHEEP / 9 COW whatever the town wants. When several YARN_STOREs have
# unlocked, wool demand is 2 units per shop per firing and the price does not fall (observed to
# RISE, 206 -> 245, across a whole episode) while MILK floors at $1. COW and SHEEP share PASTURE,
# so converting a purchase the tape is already making costs $100 and no structure.
_HS = dict(enabled=1, min_yarn=@MINYARN@, max_swap=@MAXSWAP@,
           from_day=@FROMDAY@, to_day=@TODAY@)
_hs_state = [dict(swapped=0, last=-1), dict(swapped=0, last=-1)]


def _hs_yarn(obs):
    try:
        return list((obs.get("town") or {}).get("unlocked_shops") or []).count("YARN_STORE")
    except Exception:
        return 0


def _hs_apply(obs, action):
    if not _HS["enabled"]:
        return action
    try:
        seat = int(obs.get("player", 0) or 0)
        s = _hs_state[seat]
        step = obs.get("step")
        step = int(step) if step is not None else int(obs.get("day", 0)) * 24 + int(obs.get("hour", 0))
        if step == 0 or step < s["last"]:
            s["swapped"] = 0
        s["last"] = step
        day = int(obs.get("day", step // 24))
        if not (_HS["from_day"] <= day <= _HS["to_day"]):
            return action
        if s["swapped"] >= _HS["max_swap"] or _hs_yarn(obs) < _HS["min_yarn"]:
            return action
        market = action.get("market") or []
        out, changed = [], False
        for o in market:
            if (o and len(o) > 1 and o[0] == "BUY_ANIMAL" and o[1] == "COW"
                    and s["swapped"] < _HS["max_swap"]):
                n = int(o[2]) if len(o) > 2 else 1
                take = min(n, _HS["max_swap"] - s["swapped"])
                s["swapped"] += take
                changed = True
                if take < n:
                    out.append(["BUY_ANIMAL", "COW", n - take])
                out.append(["BUY_ANIMAL", "SHEEP", take])
            else:
                out.append(o)
        if changed:
            action = dict(action)
            action["market"] = out[:MAX_ORDERS]
    except Exception:
        pass
    return action


_hs_base = agent


def _hs_agent(obs):
    return _hs_apply(obs, _hs_base(obs))


# Kaggle takes the LAST callable by insertion order, and rebinding an existing name keeps its
# original slot, so the wrapper has to be re-inserted.
del agent
agent = _hs_agent
'''

if __name__ == "__main__":
    out = sys.argv[1]
    min_yarn = int(sys.argv[2])
    max_swap = int(sys.argv[3])
    from_day = int(sys.argv[4]) if len(sys.argv) > 4 else 8
    to_day = int(sys.argv[5]) if len(sys.argv) > 5 else 11
    body = TEMPLATE
    for token, value in (("@MINYARN@", min_yarn), ("@MAXSWAP@", max_swap),
                         ("@FROMDAY@", from_day), ("@TODAY@", to_day)):
        body = body.replace(token, str(value))
    src = open("sub_router_slot.py").read() + body
    open(out, "w").write(src)
    print("wrote %s  (min_yarn=%d max_swap=%d days %d-%d)  %d bytes"
          % (out, min_yarn, max_swap, from_day, to_day, os.path.getsize(out)))
