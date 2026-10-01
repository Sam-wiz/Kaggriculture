"""Reclaim the tape's idle turns.

Measured over 24 episodes: the tape issues ~7,186 unit-actions per game and ~699 of them are
PASS -- roughly 10% of the farm's entire labour budget spent standing still. Its *productive*
actions are tight (WATER 0.0% wasted, HARVEST 0.6%, CARE 1.0%), so the idle turns are the only
large pool of free labour left in it.

The constraint is that the tape is a fixed script: a unit that moves is out of position for the
next scripted action, and anything touching inventory can void a later PICKUP or FEED. So a PASS
is only ever replaced by an op that is **stationary and inventory-neutral** -- WATER on the tile
the unit already occupies, or CARE on the animal already under it. Both are pure gain, neither
changes where the unit is standing or what it is carrying, and the tape's next turn is unaffected.

Deliberately NOT filled: HARVEST and COLLECT_FERTILIZER (add to the unit's inventory), FEED
(consumes wheat the tape has earmarked), and anything requiring a step.
"""

PF = dict(enabled=1, water=1, care=1)


def fill(obs, farmer_act, hand_acts):
    """Replace idle PASS turns with a free stationary action. Returns (farmer, hands)."""
    if not PF["enabled"]:
        return farmer_act, hand_acts
    farm = obs["farms"][obs["player"]]
    tiles = farm["tiles"]
    n = len(tiles)
    units = [list(farm["farmer"])] + [list(h) for h in (farm.get("hands") or [])]
    acts = [farmer_act] + list(hand_acts)
    claimed = set()

    # tiles another unit is already treating this turn: a second WATER/CARE there is a no-op
    for i, a in enumerate(acts):
        if i < len(units) and a and a[0] in ("WATER", "CARE"):
            claimed.add((tuple(units[i]), a[0]))

    out = []
    for i, a in enumerate(acts):
        if i >= len(units) or not a or a[0] != "PASS":
            out.append(a)
            continue
        x, y = units[i]
        t = tiles[y][x] if 0 <= y < n and 0 <= x < len(tiles[0]) else None
        pick = None
        if isinstance(t, dict):
            if "animal" in t:
                if (PF["care"] and not t.get("cared_today")
                        and ((x, y), "CARE") not in claimed):
                    pick = "CARE"
            elif t.get("kind") == "PLANT":
                if (PF["water"] and not t.get("watered_today")
                        and ((x, y), "WATER") not in claimed):
                    pick = "WATER"
        if pick:
            claimed.add(((x, y), pick))
            out.append([pick])
        else:
            out.append(a)
    return out[0], out[1:]
