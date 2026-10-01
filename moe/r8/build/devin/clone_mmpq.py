# clone_mmpq.py — direct implementation of the decoded MMPQ spec (MoE r8).
# Program/market: emit the full aspirational order list every turn in fixed
# priority; engine affordability + 10-order cap IS the bookkeeping (their
# "implicit priority queue"). Dispatch: pure greedy walker — stay-finish ->
# step-to-nearest-pending-job -> scan-order ties; no territories, no momentum.
# Decoded in moe/r8/build/mmpq/FINDINGS.md + HANDOFF 09-30d.

DAYS = 30
CENTER = [(4, 4), (5, 4), (4, 5), (5, 5)]
CENTER_SET = set(CENTER)
PRODUCTS = ["STRAWBERRY", "MELON", "MILK", "WOOL", "TOMATO", "EGG", "CARROT", "WHEAT", "FERTILIZER"]
CROPS = {
    "WHEAT": {"seed": 10, "first": 2, "maxd": 4, "harv": 2, "ongoing": False},
    "CARROT": {"seed": 20, "first": 2, "maxd": 3, "harv": 2, "ongoing": False},
    "TOMATO": {"seed": 50, "first": 8, "maxd": 8, "harv": 8, "ongoing": True},
    "STRAWBERRY": {"seed": 100, "first": 10, "maxd": 10, "harv": 10, "ongoing": True},
    "MELON": {"seed": 80, "first": 10, "maxd": 12, "harv": 10, "ongoing": False},
}
ANIMALS = {
    "GOOSE": {"cost": 300, "struct": "COOP"},
    "COW": {"cost": 400, "struct": "PASTURE"},
    "SHEEP": {"cost": 500, "struct": "PASTURE"},
}
ANIMAL_STRUCT = {"COW": "PASTURE", "SHEEP": "PASTURE", "GOOSE": "COOP"}

# --- executed program (450-ep consensus, moe/r8/build/devin/mmpq_program.py) ---
HIRES = [5, 3, 4, 5, 6, 5, 6, 8, 9, 10, 11, 10, 10, 10, 10,
         11, 11, 11, 12, 11, 11, 11, 11, 11, 11, 11, 10, 10, 10, 9]
LAND_DAYS = {5: "NE", 9: "SW"}                 # SE only when rich (d15+, $12k)
HERD_WIN = {"COW": (0, 12), "SHEEP": (0, 17), "GOOSE": (2, 12)}
HERD_TGT = {"COW": 9, "SHEEP": 14, "GOOSE": 7}  # incl. escape losses (re-buys)
# crop windows + tile floors driving seed buys / plant picks
CROP_WIN = {"MELON": (0, 2), "STRAWBERRY": (1, 16), "TOMATO": (13, 20),
            "CARROT": (0, 27), "WHEAT": (0, 27)}
CROP_TGT = {"MELON": 12, "STRAWBERRY": 34, "TOMATO": 10, "CARROT": 30, "WHEAT": 60}
FEED_RESERVE = 40        # shed wheat kept for feed runs
FERT_SELL_RESERVE = 20   # MMPQ sells surplus fert but keeps a working floor
SEED_BUF = 8             # keep >= this many seeds of in-window crops on hand


def mh(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def step_to(pos, tgt):
    dx, dy = tgt[0] - pos[0], tgt[1] - pos[1]
    if dx == 0 and dy == 0:
        return "PASS"
    if abs(dx) >= abs(dy):
        return "EAST" if dx > 0 else "WEST"
    return "SOUTH" if dy > 0 else "NORTH"


def animal_of(t):
    a = t.get("animal")
    return a if isinstance(a, str) else (a or {}).get("kind")


def agent(obs, config=None):
    p = int(obs.get("player") or 0)
    day = int(obs.get("day") or 0)
    me = obs["farms"][p]
    tiles = me["tiles"]
    money = me["money"]
    priv = obs.get("private") or {}
    shed = priv.get("shed") or {}
    seeds = priv.get("seeds") or {}
    invs = priv.get("inventories") or []
    quads = me.get("unlocked_quadrants") or []

    # ---- board scan: jobs + counts -----------------------------------------
    jobs = []           # (x, y, op)
    empties = []
    free_struct = {"PASTURE": [], "COOP": []}
    have = {"COW": 0, "SHEEP": 0, "GOOSE": 0}
    structs = {"PASTURE": 0, "COOP": 0}
    crops = {c: 0 for c in CROPS}
    for y, row in enumerate(tiles):
        for x, t in enumerate(row):
            if t == "LOCKED":
                continue
            if t is None:
                empties.append((x, y))
                continue
            if not isinstance(t, dict):
                continue
            k = t.get("kind")
            if k == "WEED":
                jobs.append((x, y, "DIG"))
            elif k == "PLANT":
                c = t.get("crop")
                if c in crops:
                    crops[c] += 1
                cd = CROPS.get(c)
                age = day - t.get("planted_day", 0)
                ripe = cd and (t.get("yield_units") or 0) > 0 and (
                    age >= cd["harv"] or (cd["ongoing"] and age >= cd["first"]))
                if ripe:
                    jobs.append((x, y, "HARVEST"))
                elif not t.get("watered_today"):
                    jobs.append((x, y, "WATER"))
            elif k in ("COOP", "PASTURE"):
                structs[k] += 1
                a = animal_of(t)
                if a:
                    have[a] = have.get(a, 0) + 1
                    if not t.get("fed_today"):
                        jobs.append((x, y, "FEED"))
                    if not t.get("cared_today"):
                        jobs.append((x, y, "CARE"))
                    if (t.get("yield_units") or 0) > 0:
                        jobs.append((x, y, "HARVEST"))
                    if t.get("fertilizer_available"):
                        jobs.append((x, y, "COLLECT_FERTILIZER"))
                else:
                    free_struct[k].append((x, y))
    herd_n = sum(have.values()) + sum(shed.get(a, 0) for a in ANIMALS)
    feed_jobs = sum(1 for j in jobs if j[2] == "FEED")

    # struct demand: unhoused shed animals + planned herd ahead of the build crew
    want_past = min(17, 4 + sum(HERD_TGT[s] for s in ("COW", "SHEEP") if day >= HERD_WIN[s][0]))
    want_coop = min(4, 2 * (day >= HERD_WIN["GOOSE"][0]) + (1 if day >= 8 else 0))
    unhoused_past = shed.get("COW", 0) + shed.get("SHEEP", 0)
    unhoused_coop = shed.get("GOOSE", 0)
    build_jobs = []
    b = 0
    for (x, y) in empties:
        if (x, y) in CENTER_SET:
            continue
        if unhoused_past + have["COW"] + have["SHEEP"] + b >= want_past and structs["PASTURE"] + b >= want_past:
            break
        if structs["PASTURE"] + b < want_past and (unhoused_past > 0 or structs["PASTURE"] + b < herd_n):
            build_jobs.append((x, y, "BUILD_PASTURE")); b += 1
            if b >= 2:
                break
    for (x, y) in empties:
        if (x, y) in CENTER_SET:
            continue
        if structs["COOP"] + sum(1 for j in build_jobs if j[2] == "BUILD_COOP") >= want_coop:
            break
        if structs["COOP"] < want_coop and (unhoused_coop > 0 or structs["COOP"] < shed.get("GOOSE", 0) + have["GOOSE"]):
            build_jobs.append((x, y, "BUILD_COOP"))
            break
    jobs = jobs + build_jobs
    # plant jobs on empty tiles when the day's program wants more of some crop
    plant_jobs = []
    if empties and day < 28:
        want_any = any(lo <= day <= hi and crops[c] < CROP_TGT[c] and seeds.get(c, 0) > 0
                       for c, (lo, hi) in CROP_WIN.items())
        if want_any or seeds.get("WHEAT", 0) > 0:
            plant_jobs = [(x, y, "PLANT") for (x, y) in empties if (x, y) not in CENTER_SET]

    # ---- market: aspirational priority queue, emitted whole every turn -----
    market = []

    def emit(o):
        if len(market) < 10:
            market.append(o)
            return True
        return False

    if day >= DAYS - 1:
        for prod in PRODUCTS:
            if shed.get(prod, 0) > 0:
                emit(["SELL", prod, 200])
        while len(market) < 10 and me["hires_today"] + sum(1 for o in market if o[0] == "HIRE") < 7:
            emit(["HIRE"])
    else:
        # 1) labor spam — every free slot until the day's target is met
        issued = 0
        while me["hires_today"] + issued < HIRES[min(day, 29)] and issued < 4:
            if emit(["HIRE"]):
                issued += 1
        # 2) land — spam the scheduled buys until they clear
        for d, q in sorted(LAND_DAYS.items()):
            if day >= d and q not in quads and money > {"NE": 1000, "SW": 2000}[q] + 300:
                emit(["BUY_LAND"])
        if day >= 15 and "SE" not in quads and money > 12000:
            emit(["BUY_LAND"])
        # 3) feed buyback — wheat is the herd's lifeline
        feed_need = herd_n * 2 + 8 - shed.get("WHEAT", 0)
        if feed_need > 0 and money > 100:
            emit(["BUY_PRODUCT", "WHEAT", min(feed_need, 10)])
        if feed_jobs and shed.get("WHEAT", 0) < herd_n + 2 and money > 50:
            emit(["BUY_PRODUCT", "WHEAT", 10])
        if shed.get("FERTILIZER", 0) < 12 and money > 400:
            emit(["BUY_PRODUCT", "FERTILIZER", 6])
        # 4) animals — aspirational spam inside species windows
        for sp in ("COW", "SHEEP", "GOOSE"):
            lo, hi = HERD_WIN[sp]
            deficit = HERD_TGT[sp] - have.get(sp, 0) - shed.get(sp, 0)
            if lo <= day <= hi and deficit > 0 and money > ANIMALS[sp]["cost"] + 200:
                emit(["BUY_ANIMAL", sp, min(deficit, 5)])
        # 5) structures demand is implicit — builds come from jobs; buy seeds
        for c, (lo, hi) in CROP_WIN.items():
            if lo <= day <= hi and crops[c] < CROP_TGT[c] and seeds.get(c, 0) < SEED_BUF and money > CROPS[c]["seed"] * 4 + 40:
                emit(["BUY_SEED", c, 4])
        if seeds.get("WHEAT", 0) < 10 and money > 120:
            emit(["BUY_SEED", "WHEAT", 6])
        # 6) standing sells — small batches, everything incl surplus fert
        for prod in PRODUCTS:
            have_q = shed.get(prod, 0)
            keep = FERT_SELL_RESERVE if prod == "FERTILIZER" else (FEED_RESERVE if prod == "WHEAT" else 0)
            if have_q - keep >= 3:
                emit(["SELL", prod, min(have_q - keep, 6)])

    # ---- dispatch: stay-finish -> nearest pending job -> scan-order --------
    units = [me["farmer"]] + list(me.get("hands") or [])
    claimed = set()

    # jobs needing seed/feed items are filtered per-unit below
    def visible_jobs(inv):
        out = []
        for j in jobs:
            x, y, op = j
            if (x, y, op) in claimed:
                continue
            if op == "FEED" and not inv.get("WHEAT", 0):
                continue
            out.append(j)
        return out

    def pick_plant_crop(pos, inv):
        # choose in-window crop the farm wants more of, seeds permitting
        pref = None
        best = -1
        for c, (lo, hi) in CROP_WIN.items():
            if not (lo <= day <= hi):
                continue
            if seeds.get(c, 0) <= 0:
                continue
            gap = CROP_TGT[c] - crops[c]
            if gap <= 0:
                continue
            # urgency: tighter window first, then bigger gap
            score = gap * 2 - (hi - day)
            if score > best:
                best, pref = score, c
        return pref

    def work(pos, ui):
        px, py = pos
        tile = tiles[py][px] if (0 <= py < len(tiles) and 0 <= px < len(tiles[py])) else None
        inv = invs[ui] if ui < len(invs) and isinstance(invs[ui], dict) else {}
        animals_carried = [a for a in ANIMALS if inv.get(a, 0) > 0]
        goods = sum(v or 0 for k, v in inv.items() if k not in ANIMALS and k not in ("WHEAT", "FERTILIZER"))

        # 1) carrying an animal -> nearest free structure
        if animals_carried:
            sp = animals_carried[0]
            k = ANIMAL_STRUCT[sp]
            if free_struct[k]:
                tgt = min(free_struct[k], key=lambda s: mh(pos, s))
                if (px, py) == tgt:
                    return ["PLACE", sp, 1]
                return [step_to(pos, tgt)]
            return ["PASS"]
        # 2) carrying wheat -> feed route if animals are hungry
        if inv.get("WHEAT", 0) > 0 and feed_jobs:
            fj = [j for j in jobs if j[2] == "FEED" and (j[0], j[1], "FEED") not in claimed]
            if fj:
                bx, by, _ = min(fj, key=lambda j: mh(pos, j))
                claimed.add((bx, by, "FEED"))
                if (bx, by) == (px, py):
                    return ["FEED"]
                return [step_to(pos, (bx, by))]
        # 3) carrying goods -> shed
        if goods > 0:
            if (px, py) in CENTER_SET:
                return ["DROP"]
            return [step_to(pos, min(CENTER, key=lambda c: mh(pos, c)))]
        # 4) stay-finish: pending op on our own tile
        if isinstance(tile, dict):
            k = tile.get("kind")
            if k == "PLANT":
                c = tile.get("crop")
                cd = CROPS.get(c)
                age = day - tile.get("planted_day", 0)
                ripe = cd and (tile.get("yield_units") or 0) > 0 and (
                    age >= cd["harv"] or (cd["ongoing"] and age >= cd["first"]))
                if ripe:
                    return ["HARVEST"]
                if not tile.get("watered_today"):
                    return ["WATER"]
                if cd and not cd["ongoing"] and age > cd["maxd"]:
                    return ["DIG"]
                if inv.get("FERTILIZER", 0) > 0 and (tile.get("fertilized_until_day", -1) < day):
                    return ["FERTILIZE"]
            elif k == "WEED":
                return ["DIG"]
            elif k in ("COOP", "PASTURE") and animal_of(tile):
                if not tile.get("fed_today") and inv.get("WHEAT", 0) > 0:
                    return ["FEED"]
                if (tile.get("yield_units") or 0) > 0:
                    return ["HARVEST"]
                if not tile.get("cared_today"):
                    return ["CARE"]
                if tile.get("fertilizer_available"):
                    return ["COLLECT_FERTILIZER"]
        elif tile is None:
            c = pick_plant_crop(pos, inv)
            if c:
                claimed.add((px, py, "PLANT"))
                return ["PLANT", c]
        # 5) at shed: load wheat for feed runs / grab a homeless animal
        if (px, py) in CENTER_SET:
            if feed_jobs and inv.get("WHEAT", 0) == 0 and shed.get("WHEAT", 0) > 0:
                return ["PICKUP", "WHEAT", min(6, shed["WHEAT"])]
            for sp in ("GOOSE", "COW", "SHEEP"):
                if shed.get(sp, 0) > 0 and free_struct[ANIMAL_STRUCT[sp]]:
                    return ["PICKUP", sp, 1]
            if inv.get("FERTILIZER", 0) == 0 and shed.get("FERTILIZER", 0) > 0:
                return ["PICKUP", "FERTILIZER", min(3, shed["FERTILIZER"])]
        # 6) nearest pending job (FEED filtered by carrying wheat)
        pool = visible_jobs(inv)
        if pool:
            bx, by, op = min(pool, key=lambda j: mh(pos, j))
            claimed.add((bx, by, op))
            if (bx, by) == (px, py):
                return [op]
            return [step_to(pos, (bx, by))]
        # 7) nearest plantable empty tile
        pj = [j for j in plant_jobs if (j[0], j[1], "PLANT") not in claimed]
        if pj:
            bx, by, _ = min(pj, key=lambda j: mh(pos, j))
            claimed.add((bx, by, "PLANT"))
            if (bx, by) == (px, py):
                c = pick_plant_crop(pos, inv) or "WHEAT"
                return ["PLANT", c]
            return [step_to(pos, (bx, by))]
        # 7) hungry animals & no wheat carried -> head to shed
        if feed_jobs and shed.get("WHEAT", 0) > 0 and inv.get("WHEAT", 0) == 0:
            return [step_to(pos, min(CENTER, key=lambda c: mh(pos, c)))]
        # 8) shed has animals + free structs -> run the delivery
        if any(shed.get(sp, 0) > 0 and free_struct[ANIMAL_STRUCT[sp]] for sp in ANIMALS):
            return [step_to(pos, min(CENTER, key=lambda c: mh(pos, c)))]
        return ["PASS"]

    farmer_op = work(units[0], 0)
    hand_ops = [work(units[i], i) for i in range(1, len(units))]
    return {"farmer": farmer_op, "hands": hand_ops, "market": market}
