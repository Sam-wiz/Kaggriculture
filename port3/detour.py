"""Send idle units to do a job and be back before the tape needs them.

Measured on the live tape: ~672 of its ~7,186 unit-actions per game are PASS, and 97.8% of those
idle stretches have a tile needing work close enough to walk to and return from within the stretch
(~637 reclaimable work-turns/game, about +9% labour). Simply filling a PASS in place recovers only
~21 of them, because the tape parks its idle units on tiles it has already finished -- the work is
always a few steps away.

What makes the detour safe is that the tape is a fixed script we carry with us: for any unit we can
read forward and find the exact turn the tape next gives it a real order. If the idle stretch is L
turns and the job is d steps away, a round trip costs 2d+1, so whenever 2d+1 <= L the unit is
provably standing back on its original tile, carrying exactly what it left with, before the script
resumes. The tape is never disturbed; we only spend turns it was throwing away.

Restricted to WATER and CARE: both are inventory-neutral, so nothing can void a later PICKUP or
FEED. HARVEST and COLLECT_FERTILIZER would fill the unit's hands and are deliberately excluded.
"""

DT = dict(enabled=1, max_dist=4, horizon=24, water=1, care=1)

_plans = [None] * 16          # per unit index: list of (expected_pos, action)


def reset():
    for i in range(len(_plans)):
        _plans[i] = None


def _tape_idle_run(tapes, route, step, unit, horizon, unpack):
    """Turns until the tape next gives `unit` a real order (capped at horizon)."""
    n = len(tapes[route])
    for k in range(1, horizon + 1):
        t = step + k
        if t >= n:
            return k                      # tape is over; treat as the end of the run
        a = unpack(tapes[route][t])
        if unit == 0:
            act = a["farmer"]
        else:
            hands = a["hands"]
            act = hands[unit - 1] if unit - 1 < len(hands) else ["PASS"]
        if act and act[0] != "PASS":
            return k
    return horizon + 1


def _path(a, b):
    """Explicit tile sequence from a to b: x first, then y."""
    out = []
    x, y = a
    while x != b[0]:
        x += 1 if b[0] > x else -1
        out.append(("EAST" if b[0] > a[0] else "WEST", (x, y)))
    while y != b[1]:
        y += 1 if b[1] > y else -1
        out.append(("SOUTH" if b[1] > a[1] else "NORTH", (x, y)))
    return out


def apply(obs, farmer_act, hand_acts, tapes, route, unpack):
    if not DT["enabled"]:
        return farmer_act, hand_acts
    farm = obs["farms"][obs["player"]]
    tiles = farm["tiles"]
    n = len(tiles)
    step = int(obs.get("step") or (int(obs.get("day", 0)) * 24 + int(obs.get("hour", 0))))
    units = [list(farm["farmer"])] + [list(h) for h in (farm.get("hands") or [])]
    acts = [farmer_act] + list(hand_acts)

    # tiles that want work, and are not already being handled by a scripted action
    busy = set()
    for i, a in enumerate(acts):
        if i < len(units) and a and a[0] in ("WATER", "CARE"):
            busy.add(tuple(units[i]))
    jobs = []
    for y in range(n):
        for x in range(n):
            if (x, y) in busy:
                continue
            t = tiles[y][x]
            if not isinstance(t, dict):
                continue
            if "animal" in t:
                if DT["care"] and not t.get("cared_today"):
                    jobs.append((x, y, "CARE"))
            elif t.get("kind") == "PLANT":
                if DT["water"] and not t.get("watered_today"):
                    jobs.append((x, y, "WATER"))

    out = []
    for i, a in enumerate(acts):
        if i >= len(units):
            out.append(a)
            continue
        pos = tuple(units[i])
        if a and a[0] != "PASS":
            _plans[i] = None              # the tape wants this unit; stand down
            out.append(a)
            continue

        plan = _plans[i] if i < len(_plans) else None
        if plan:
            want_pos, act = plan[0]
            if want_pos == pos:            # still on script
                _plans[i] = plan[1:] or None
                if act[0] in ("WATER", "CARE"):
                    busy.add(pos)
                out.append(act)
                continue
            _plans[i] = None               # drifted (crew reshuffle); abandon safely

        L = _tape_idle_run(tapes, route, step, i, DT["horizon"], unpack)
        best = None
        for (jx, jy, op) in jobs:
            d = abs(jx - pos[0]) + abs(jy - pos[1])
            if d == 0 or d > DT["max_dist"] or 2 * d + 1 > L:
                continue
            if best is None or d < best[0]:
                best = (d, jx, jy, op)
        if best is None:
            out.append(a)
            continue

        d, jx, jy, op = best
        goal = (jx, jy)
        seq = []
        for mv, p in _path(pos, goal):
            seq.append((None, [mv], p))
        seq.append((goal, [op], goal))
        back = _path(goal, pos)
        for mv, p in back:
            seq.append((None, [mv], p))

        # rebuild as (expected_position_before_acting, action)
        steps = []
        cur = pos
        for want, act, after in seq:
            steps.append((cur, act))
            cur = after
        jobs = [j for j in jobs if (j[0], j[1]) != goal]
        busy.add(goal)
        _plans[i] = steps[1:] or None
        out.append(steps[0][1])

    return out[0], out[1:]
