"""Build a router variant that converts whole cow CHAINS to sheep, not just the purchase.

The first attempt at this rewrote only `BUY_ANIMAL COW` -> `SHEEP`. The tape then ran `PICKUP COW`
against a shed holding SHEEP, found nothing, and had nothing to `PLACE`. Result: four cows lost,
zero sheep gained, -7,758. Counting the animals alive at the end (8 sheep in both the base and the
"swap") is what finally exposed it.

Livestock reaches a pasture through three species-bound actions -- BUY_ANIMAL, PICKUP and PLACE --
and all three must be renamed together. FEED and CARE take no argument and act on whatever animal
occupies the tile, so the husbandry schedule itself needs no changes. COW and SHEEP share the
PASTURE structure, so the placement tile accepts either.

The chains are identical across all four tails (every animal is bought inside the shared prefix):

    buy  pickup  place  unit  day        buy  pickup  place  unit  day
      1       2    4,5   5,1    0        169     175    177     3    7
     65      66     69     0    2        176     180    183     3    7
     88      92     95     3    3        195     196    199     2    8
    150 152,153    156   0,3    6

Only chains bought from `min_day` on are eligible: the day-0 purchases run on a $0-9 cash floor
where a $100 difference (SHEEP costs 500, COW 400) has been measured to kill the farm outright,
and they are decided before any shop has unlocked.

Usage:  python mkherd.py <out.py> <max_convert> <min_yarn> [min_day] [src.py]
"""
import os
import sys

import chains

TEMPLATE = '''

# ---------------------------------------------------------------------------
# OVERLAY: cow->sheep chain conversion  (Sam-wiz)
# ---------------------------------------------------------------------------
# Converts whole BUY/PICKUP/PLACE chains, which is what makes the animal actually arrive. Renaming
# the purchase alone leaves PICKUP looking for a species the shed no longer holds; that failure
# cost four cows and produced no sheep.
_HD = dict(enabled=1, max_convert=@MAXC@, min_yarn=@MINYARN@, min_day=@MINDAY@)
# (buy_turn, pickup_turn, place_turn, unit) for every COW chain, latest first: later chains are
# decided with more of the shop draw visible and with the opening cash crunch already past.
_HD_CHAINS = @CHAINS@
_hd_state = [dict(picked=None, last=-1), dict(picked=None, last=-1)]


def _hd_yarn(obs):
    try:
        return list((obs.get("town") or {}).get("unlocked_shops") or []).count("YARN_STORE")
    except Exception:
        return 0


def _hd_choose(obs, step, s):
    """Decide once, at the first eligible buy turn, how many chains to convert."""
    if s["picked"] is not None:
        return s["picked"]
    n = _HD["max_convert"] if _hd_yarn(obs) >= _HD["min_yarn"] else 0
    s["picked"] = set(c[:4] for c in _HD_CHAINS[:n])
    return s["picked"]


def _hd_apply(obs, action):
    if not _HD["enabled"] or not _HD_CHAINS:
        return action
    try:
        seat = int(obs.get("player", 0) or 0)
        s = _hd_state[seat]
        step = obs.get("step")
        step = int(step) if step is not None else int(obs.get("day", 0)) * 24 + int(obs.get("hour", 0))
        if step == 0 or step < s["last"]:
            s["picked"] = None
        s["last"] = step
        first_buy = min(c[0] for c in _HD_CHAINS)
        if step < first_buy:
            return action
        picked = _hd_choose(obs, step, s)
        if not picked:
            return action

        buys = sum(1 for c in picked if c[0] == step)
        pick_units = set(c[3] for c in picked if c[1] == step)
        place_units = set(c[3] for c in picked if c[2] == step)
        if not buys and not pick_units and not place_units:
            return action

        action = dict(action)
        if buys:
            out = []
            for o in (action.get("market") or []):
                if o and len(o) > 1 and o[0] == "BUY_ANIMAL" and o[1] == "COW":
                    n = int(o[2]) if len(o) > 2 else 1
                    take = min(n, buys)
                    buys -= take
                    if n - take > 0:
                        out.append(["BUY_ANIMAL", "COW", n - take])
                    out.append(["BUY_ANIMAL", "SHEEP", take])
                else:
                    out.append(o)
            action["market"] = out[:MAX_ORDERS]

        if pick_units or place_units:
            units = [action.get("farmer") or ["PASS"]] + [list(h) for h in (action.get("hands") or [])]
            for i, u in enumerate(units):
                if not u or len(u) < 2 or u[1] != "COW":
                    continue
                if (u[0] == "PICKUP" and i in pick_units) or (u[0] == "PLACE" and i in place_units):
                    units[i] = [u[0], "SHEEP"] + list(u[2:])
            action["farmer"] = units[0]
            action["hands"] = units[1:]
    except Exception:
        pass
    return action


_hd_base = agent


def _hd_agent(obs):
    return _hd_apply(obs, _hd_base(obs))


# Kaggle takes the LAST callable by insertion order; rebinding an existing name keeps its original
# slot, so the wrapper has to be re-inserted or the bare route would run.
del agent
agent = _hd_agent
'''


def cow_chains(min_day):
    m = chains.load_router()
    route = m.routes()[m.MAIN]
    cs = [c for c in chains.chains(route)
          if c["species"] == "COW" and c["pickup"] is not None and c["buy"] is not None]
    cs = [c for c in cs if c["buy"] // 24 >= min_day]
    cs.sort(key=lambda c: -c["buy"])          # latest first
    return [(c["buy"], c["pickup"], c["place"], c["unit"]) for c in cs]


if __name__ == "__main__":
    out = sys.argv[1]
    maxc = int(sys.argv[2])
    minyarn = int(sys.argv[3])
    min_day = int(sys.argv[4]) if len(sys.argv) > 4 else 6
    src = sys.argv[5] if len(sys.argv) > 5 else "sub_router_slot.py"
    cs = cow_chains(min_day)
    body = (TEMPLATE.replace("@MAXC@", str(maxc)).replace("@MINYARN@", str(minyarn))
            .replace("@MINDAY@", str(min_day)).replace("@CHAINS@", repr(cs)))
    open(out, "w").write(open(src).read() + body)
    print("wrote %s  convert<=%d when yarn>=%d, from day %d; %d eligible chains: %s"
          % (out, maxc, minyarn, min_day, len(cs), cs))
