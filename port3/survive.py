"""Survival override: when the hires fail, stop following the tape and save the herd.

The tape's unit actions assume ~12 hands. When a cash shortfall voids the morning
hires we are left with one farmer executing a 12-hand script, so nothing gets watered
or fed: crops become weeds within two days, livestock starves, and the game ends at a
bank of 0 (observed repeatedly on the ladder).

One farmer cannot save 19 crops, but it can easily save the animals -- 4 animals need
4 FEED + 4 CARE out of 24 turns, and livestock is worth ~$300/tile-day against a crop's
$60-110. So when we are far below the hand count the tape expects, redirect every unit
we do have to: feed, then care, then water whatever is one day from dying.

Fires only in the failure state, so normal play is untouched.
"""

PS = dict(enabled=1, max_hands=0, from_day=1, from_hour=3)


def _dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def _step_toward(pos, goal):
    dx, dy = goal[0] - pos[0], goal[1] - pos[1]
    if abs(dx) >= abs(dy):
        if dx > 0:
            return ["EAST"]
        if dx < 0:
            return ["WEST"]
    if dy > 0:
        return ["SOUTH"]
    if dy < 0:
        return ["NORTH"]
    return ["PASS"]


def survival_actions(obs):
    """Return unit actions that keep the farm alive, or None if not needed."""
    if not PS["enabled"]:
        return None
    day = int(obs.get("day", 0) or 0)
    if day < PS["from_day"]:
        return None
    # hour 0 of every day legitimately shows 0 hands: the hires have not landed yet.
    # Only treat an empty crew as a failure once the morning hire window has passed.
    if int(obs.get("hour", 0) or 0) < PS["from_hour"]:
        return None
    me = obs["player"]
    farm = obs["farms"][me]
    hands = farm.get("hands", []) or []
    if len(hands) > PS["max_hands"]:
        return None                      # the tape has the crew it expects

    tiles = farm["tiles"]
    n = len(tiles)
    half = n // 2
    shed_tiles = {(half - 1, half - 1), (half, half - 1),
                  (half - 1, half), (half, half)}
    invs = obs["private"]["inventories"]
    shed = obs["private"]["shed"]

    jobs = []                            # (priority, x, y, op)
    for y in range(n):
        for x in range(n):
            t = tiles[y][x]
            if not isinstance(t, dict):
                continue
            if "animal" in t:
                if not t["fed_today"]:
                    jobs.append((0, x, y, "FEED"))
                if not t["cared_today"]:
                    jobs.append((2, x, y, "CARE"))
                if t["yield_units"] > 0:
                    jobs.append((3, x, y, "HARVEST"))
                if t["fertilizer_available"]:
                    jobs.append((4, x, y, "COLLECT_FERTILIZER"))
            elif t.get("kind") == "PLANT":
                # one unwatered day already banked: water today or it becomes a weed
                if not t["watered_today"] and t["consecutive_unwatered"] >= 1:
                    jobs.append((1, x, y, "WATER"))

    units = [list(farm["farmer"])] + [list(h) for h in hands]
    acts = []
    taken = set()
    for i, pos in enumerate(units):
        inv = invs[i] if i < len(invs) else {}
        best = None
        for j in jobs:
            pr, x, y, op = j
            if (x, y, op) in taken:
                continue
            if op == "FEED" and inv.get("WHEAT", 0) <= 0:
                continue
            d = _dist(pos, (x, y))
            score = (pr, d)
            if best is None or score < best[0]:
                best = (score, j)
        # no feed on hand but animals are hungry: fetch wheat from the shed
        if best is None or (best[1][3] == "FEED" and inv.get("WHEAT", 0) <= 0):
            if (any(j[3] == "FEED" for j in jobs) and inv.get("WHEAT", 0) <= 0
                    and shed.get("WHEAT", 0) > 0):
                if tuple(pos) in shed_tiles:
                    acts.append(["PICKUP", "WHEAT", min(8, shed["WHEAT"])])
                else:
                    goal = (min(max(pos[0], half - 1), half),
                            min(max(pos[1], half - 1), half))
                    acts.append(_step_toward(pos, goal))
                continue
        if best is None:
            acts.append(["PASS"])
            continue
        _, (pr, x, y, op) = best
        taken.add((x, y, op))
        acts.append([op] if tuple(pos) == (x, y) else _step_toward(pos, (x, y)))
    return acts
