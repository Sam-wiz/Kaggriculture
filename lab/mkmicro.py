"""Build a router variant with a self-contained SHEEP MICRO-FARM.

Every previous production change failed because the tape is a positional program: its unit actions
are bound to specific tiles, turns and unit indices, so altering what the farm owns breaks the
schedule that tends it. The micro-farm avoids that entirely by sharing nothing with the base except
cash and the market order list.

  land     the SE quadrant, $4,000, the last entry in LAND_ORDER and the only one the tape never
           buys. Its corner (5,5) is also a shed-access tile, so the plot is 0-2 steps from the
           shed and harvested product auto-drops into the shed at end of day.
  hand     one extra HIRE appended AFTER the tape's own hires each day, so the tape pays the same
           Fibonacci rungs it always did and we pay only the marginal one ($34-233/day, $3,584 for
           days 6-29 if hired daily). The new hand lands at the END of farm["hands"], and the tape
           only ever indexes the hands it hired itself.
  tiles    BUILD_PASTURE is free -- it needs nothing but an empty tile.
  feed     BUY_PRODUCT WHEAT, one of only two items the engine lets you buy back, and its price
           barely moves.
  sales    appended AFTER the tape's orders so its rate-matched schedule and slot order are intact.

On a seed where the trigger never fires the agent is byte-identical to its base; that is the
acceptance test, not a nicety.

Usage:  python mkmicro.py <out.py> <n_sheep> <min_yarn> [from_day] [min_money] [src.py]
"""
import os
import sys

TEMPLATE = '''

# ---------------------------------------------------------------------------
# OVERLAY: sheep micro-farm  (Sam-wiz)
# ---------------------------------------------------------------------------
_MF = dict(enabled=1, n_sheep=@NSHEEP@, min_yarn=@MINYARN@, from_day=@FROMDAY@,
           min_money=@MINMONEY@)
# SE-quadrant tiles nearest the shed. (5,5) is left clear: it is a shed-access tile and the
# micro-farm's pickup point.
_MF_PLOT = [(6, 5), (5, 6), (6, 6), (7, 5), (5, 7), (7, 6), (6, 7), (7, 7)]
_MF_PICK = (5, 5)
_MF_MOVES = {"NORTH": (0, -1), "SOUTH": (0, 1), "EAST": (1, 0), "WEST": (-1, 0)}
_mf_state = [dict(on=None, last=-1, land=False, fed_day=-1), dict(on=None, last=-1, land=False, fed_day=-1)]


def _mf_step_toward(pos, goal):
    x, y = pos
    gx, gy = goal
    if x != gx:
        return "EAST" if gx > x else "WEST"
    if y != gy:
        return "SOUTH" if gy > y else "NORTH"
    return None


def _mf_tile(farm, x, y):
    try:
        return farm["tiles"][y][x]
    except Exception:
        return "LOCKED"


def _mf_plot(n):
    return _MF_PLOT[:max(0, min(n, len(_MF_PLOT)))]


def _mf_apply(obs, action):
    if not _MF["enabled"] or _MF["n_sheep"] <= 0:
        return action
    try:
        seat = int(obs.get("player", 0) or 0)
        s = _mf_state[seat]
        step = obs.get("step")
        step = int(step) if step is not None else int(obs.get("day", 0)) * 24 + int(obs.get("hour", 0))
        if step == 0 or step < s["last"]:
            s.update(on=None, land=False, fed_day=-1)
        s["last"] = step
        day = int(obs.get("day", step // 24))
        farm = obs["farms"][seat]
        priv = obs.get("private") or {}

        # ---- activation: decided once, and only on public state ----
        if s["on"] is None:
            if day < _MF["from_day"]:
                return action
            yarn = list((obs.get("town") or {}).get("unlocked_shops") or []).count("YARN_STORE")
            s["on"] = bool(yarn >= _MF["min_yarn"] and farm.get("money", 0) >= _MF["min_money"])
        if not s["on"]:
            return action

        plot = _mf_plot(_MF["n_sheep"])
        market = list(action.get("market") or [])
        tape_hands = list(action.get("hands") or [])
        hands = farm.get("hands") or []
        me = len(tape_hands)              # our hand is the one the tape does not index
        shed = dict(priv.get("shed") or {})
        invs = priv.get("inventories") or []
        inv = dict(invs[me + 1]) if len(invs) > me + 1 else {}

        # ---- land: the SE quadrant, once ----
        if not s["land"]:
            if _mf_tile(farm, *_MF_PICK) == "LOCKED":
                if len(market) < MAX_ORDERS:
                    market.append(["BUY_LAND"])
            else:
                s["land"] = True

        # ---- one extra hand per day, appended after the tape's own hires ----
        if len(hands) <= me and len(market) < MAX_ORDERS:
            market.append(["HIRE"])

        # ---- livestock and feed ----
        placed = sum(1 for (x, y) in plot
                     if isinstance(_mf_tile(farm, x, y), dict)
                     and "animal" in _mf_tile(farm, x, y))
        want = len(plot) - placed - int(shed.get("SHEEP", 0)) - int(inv.get("SHEEP", 0))
        if s["land"] and want > 0 and len(market) < MAX_ORDERS and farm.get("money", 0) > 1200:
            market.append(["BUY_ANIMAL", "SHEEP", min(want, 2)])
        # Feed: buy ONCE a day, and only the shortfall. Re-checking every turn bought 198 wheat
        # for four sheep over eighteen days -- nearly three times what they eat, at ~$35 a unit,
        # while crowding the same 100-item shed the base is already running near.
        if s["land"] and s["fed_day"] != day and len(market) < MAX_ORDERS:
            # Buy our own feed unconditionally, one day's worth. Buying only the shortfall looks
            # thriftier but takes wheat out of the shared shed, which is the base's animals' feed --
            # a coupling the whole design exists to avoid. Adding and consuming the same amount each
            # day leaves the base's feed chain exactly as it was.
            market.append(["BUY_PRODUCT", "WHEAT", len(plot)])
            s["fed_day"] = day

        # ---- sell only what the micro-farm produced, after the tape's own orders ----
        tape_wool = sum(int(o[2]) for o in market
                        if o and len(o) > 2 and o[0] == "SELL" and o[1] == "WOOL")
        spare = int(shed.get("WOOL", 0)) - tape_wool
        if spare > 0 and len(market) < MAX_ORDERS:
            market.append(["SELL", "WOOL", spare])
        action = dict(action)
        action["market"] = market[:MAX_ORDERS]

        # ---- drive our hand ----
        if len(hands) <= me:
            return action
        pos = tuple(hands[me])
        act = ["PASS"]
        tile = _mf_tile(farm, *pos)
        carry_wheat = int(inv.get("WHEAT", 0))

        if isinstance(tile, dict) and "animal" in tile:
            if tile.get("yield_units", 0) > 0:
                act = ["HARVEST"]
            elif not tile.get("fed_today") and carry_wheat > 0:
                act = ["FEED"]
            else:
                act = None
        elif tile is None and pos in plot:
            act = ["BUILD_PASTURE"]
        elif isinstance(tile, dict) and tile.get("kind") == "PASTURE" and int(inv.get("SHEEP", 0)) > 0:
            act = ["PLACE", "SHEEP"]
        else:
            act = None

        if act is None:
            # Priorities, in order: carry feed if empty, then serve the nearest animal that needs
            # something, then idle at the pickup tile. The earlier version restocked whenever it
            # held less than a full load, which sent it back to the shed mid-round and left half
            # the flock unfed -- and an animal misses two days running, it escapes.
            unfed = [p for p in plot
                     if isinstance(_mf_tile(farm, *p), dict) and "animal" in _mf_tile(farm, *p)
                     and not _mf_tile(farm, *p).get("fed_today")]
            ripe = [p for p in plot
                    if isinstance(_mf_tile(farm, *p), dict) and "animal" in _mf_tile(farm, *p)
                    and _mf_tile(farm, *p).get("yield_units", 0) > 0]
            build = [p for p in plot if _mf_tile(farm, *p) is None]
            empty_pasture = [p for p in plot
                             if isinstance(_mf_tile(farm, *p), dict)
                             and _mf_tile(farm, *p).get("kind") == "PASTURE"
                             and "animal" not in _mf_tile(farm, *p)]
            need_pickup = (carry_wheat == 0 and unfed and int(shed.get("WHEAT", 0)) > 0) or \
                          (empty_pasture and int(shed.get("SHEEP", 0)) > 0
                           and int(inv.get("SHEEP", 0)) == 0)
            if need_pickup:
                goal = _MF_PICK
            elif ripe:
                goal = min(ripe, key=lambda p: abs(p[0]-pos[0]) + abs(p[1]-pos[1]))
            elif unfed and carry_wheat > 0:
                goal = min(unfed, key=lambda p: abs(p[0]-pos[0]) + abs(p[1]-pos[1]))
            elif empty_pasture and int(inv.get("SHEEP", 0)) > 0:
                goal = empty_pasture[0]
            elif build:
                goal = build[0]
            else:
                goal = _MF_PICK
            if pos == goal:
                if goal == _MF_PICK:
                    if empty_pasture and int(shed.get("SHEEP", 0)) > 0 and int(inv.get("SHEEP", 0)) == 0:
                        act = ["PICKUP", "SHEEP", 1]
                    elif int(shed.get("WHEAT", 0)) > 0 and carry_wheat < len(plot):
                        act = ["PICKUP", "WHEAT", min(len(plot), int(shed.get("WHEAT", 0)))]
                    else:
                        act = ["PASS"]
                else:
                    act = ["PASS"]
            else:
                mv = _mf_step_toward(pos, goal)
                act = [mv] if mv else ["PASS"]

        hands_out = list(tape_hands)
        while len(hands_out) < me:
            hands_out.append(["PASS"])
        hands_out.append(act)
        action["hands"] = hands_out
    except Exception:
        pass
    return action


_mf_base = agent


def _mf_agent(obs):
    return _mf_apply(obs, _mf_base(obs))


# Kaggle takes the LAST callable by insertion order; rebinding an existing name keeps its original
# slot, so the wrapper has to be re-inserted or the bare route would run.
del agent
agent = _mf_agent
'''

if __name__ == "__main__":
    out = sys.argv[1]
    n = int(sys.argv[2])
    my = int(sys.argv[3])
    fd = int(sys.argv[4]) if len(sys.argv) > 4 else 11
    mm = int(sys.argv[5]) if len(sys.argv) > 5 else 7000
    src = sys.argv[6] if len(sys.argv) > 6 else "sub_herd.py"
    body = (TEMPLATE.replace("@NSHEEP@", str(n)).replace("@MINYARN@", str(my))
            .replace("@FROMDAY@", str(fd)).replace("@MINMONEY@", str(mm)))
    open(out, "w").write(open(src).read() + body)
    print("wrote %s  (%d sheep, yarn>=%d, from day %d, money>=%d, base=%s) %d bytes"
          % (out, n, my, fd, mm, src, os.path.getsize(out)))
