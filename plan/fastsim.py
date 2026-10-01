"""Forward model of OUR OWN farm, exact against the engine.

The point: our farm evolves deterministically from our own actions (the only external
inputs are seeded weed spawns and the shared market price). So an agent can simulate
its own future exactly and PLAN, instead of guessing with heuristics. We have ~719 s
of unused compute per episode and every rival uses none of it.

Mirrors kaggriculture.py exactly for the subset an owner needs: plant growth/decay,
animal production with the care bonus, watering/feeding deadlines, shed, seeds, money.
Validated in plan/validate.py by replaying real episodes and diffing every field.
"""

CROPS = {
    "WHEAT":      {"seed": 10,  "first": 2,  "myd": 4,  "interval": 0, "maxy": 6, "ongoing": False},
    "CARROT":     {"seed": 20,  "first": 2,  "myd": 3,  "interval": 0, "maxy": 4, "ongoing": False},
    "TOMATO":     {"seed": 50,  "first": 8,  "myd": 8,  "interval": 1, "maxy": 4, "ongoing": True},
    "STRAWBERRY": {"seed": 100, "first": 10, "myd": 10, "interval": 2, "maxy": 4, "ongoing": True},
    "MELON":      {"seed": 80,  "first": 10, "myd": 12, "interval": 0, "maxy": 6, "ongoing": False},
}
ANIMALS = {
    "GOOSE": {"cost": 300, "struct": "COOP",    "first": 4, "interval": 1, "held": 4, "product": "EGG"},
    "COW":   {"cost": 400, "struct": "PASTURE", "first": 8, "interval": 2, "held": 6, "product": "MILK"},
    "SHEEP": {"cost": 500, "struct": "PASTURE", "first": 6, "interval": 3, "held": 6, "product": "WOOL"},
}
MOVES = {"NORTH": (0, -1), "SOUTH": (0, 1), "EAST": (1, 0), "WEST": (-1, 0)}
LAND_ORDER = ["NE", "SW", "SE"]
LAND_PRICES = [1000, 2000, 4000]


def quadrant_of(x, y, n):
    h = n // 2
    return ("N" if y < h else "S") + ("W" if x < h else "E")


def shed_tiles(n):
    h = n // 2
    return [(h - 1, h - 1), (h, h - 1), (h - 1, h), (h, h)]


def fib(k):
    a, b = 1, 1
    for _ in range(k):
        a, b = b, a + b
    return a


class Farm:
    """Our own farm. `tiles[y][x]` is None | 'LOCKED' | dict, exactly as the engine."""

    def __init__(self, obs, player):
        f = obs["farms"][player]
        self.n = len(f["tiles"])
        self.tiles = [[_copy_tile(t) for t in row] for row in f["tiles"]]
        self.money = float(f["money"])
        self.units = [list(f["farmer"])] + [list(h) for h in f["hands"]]
        self.quads = list(f["unlocked_quadrants"])
        self.hires_today = int(f.get("hires_today", 0) or 0)
        priv = obs["private"]
        self.shed = dict(priv["shed"])
        self.seeds = dict(priv["seeds"])
        self.invs = [dict(i) for i in priv["inventories"]]
        self.day = int(obs["day"])
        self.hour = int(obs["hour"])
        self.turns_per_day = 24
        self.shed_cap = 100

    # ---------------------------------------------------------------- unit ops
    def apply_unit(self, idx, act):
        if not act:
            return
        op = act[0]
        if idx >= len(self.units):
            return
        x, y = self.units[idx]
        inv = self.invs[idx] if idx < len(self.invs) else {}
        if op in MOVES:
            dx, dy = MOVES[op]
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                self.units[idx] = [nx, ny]
            return
        if op == "PASS":
            return
        tile = self.tiles[y][x]
        adj = (x, y) in shed_tiles(self.n)
        if op == "DROP":
            if not adj:
                return
            for item, k in list(inv.items()):
                if k <= 0:
                    del inv[item]
                    continue
                room = max(0, self.shed_cap - sum(self.shed.values()))
                take = min(k, room)
                if take:
                    self.shed[item] = self.shed.get(item, 0) + take
                del inv[item]
            return
        if op == "PICKUP":
            if not adj or len(act) < 2:
                return
            item = act[1]
            k = int(act[2]) if len(act) >= 3 else 1
            k = min(k, self.shed.get(item, 0))
            if k <= 0:
                return
            self.shed[item] -= k
            inv[item] = inv.get(item, 0) + k
            return
        if op == "PLACE":
            if len(act) < 2:
                return
            item = act[1]
            if (item in ANIMALS and isinstance(tile, dict)
                    and tile.get("kind") == ANIMALS[item]["struct"] and "animal" not in tile):
                if inv.get(item, 0) >= 1:
                    inv[item] -= 1
                    if inv[item] == 0:
                        del inv[item]
                    self.tiles[y][x] = _new_animal(item, self.day)
                return
            if adj:
                k = int(act[2]) if len(act) >= 3 else 1
                k = min(k, inv.get(item, 0),
                        max(0, self.shed_cap - sum(self.shed.values())))
                if k <= 0:
                    return
                inv[item] -= k
                if inv[item] == 0:
                    del inv[item]
                self.shed[item] = self.shed.get(item, 0) + k
            return
        if tile == "LOCKED":
            return
        if op == "PLANT":
            if len(act) < 2 or act[1] not in CROPS or tile is not None:
                return
            if self.seeds.get(act[1], 0) <= 0:
                return
            self.seeds[act[1]] -= 1
            self.tiles[y][x] = _new_plant(act[1], self.day, self.turns_per_day)
            return
        if op == "WATER":
            if not (isinstance(tile, dict) and tile.get("kind") == "PLANT"):
                return
            if tile["watered_today"]:
                return
            tile["watered_today"] = True
            cd = CROPS[tile["crop"]]
            if not cd["ongoing"]:
                age = self.day - tile["planted_day"]
                if (cd["myd"] + 1) // 2 <= age <= cd["myd"]:
                    bonus = 2 if tile["fertilized_until_day"] >= self.day else 1
                    tile["yield_units"] = min(cd["maxy"], tile["yield_units"] + bonus)
            return
        if op == "HARVEST":
            if not isinstance(tile, dict) or tile.get("yield_units", 0) <= 0:
                return
            if tile.get("kind") == "PLANT":
                cd = CROPS[tile["crop"]]
                if self.day - tile["planted_day"] < cd["first"]:
                    return
                inv[tile["crop"]] = inv.get(tile["crop"], 0) + tile["yield_units"]
                tile["yield_units"] = 0
                if not cd["ongoing"]:
                    self.tiles[y][x] = None
            elif "animal" in tile:
                p = ANIMALS[tile["animal"]]["product"]
                inv[p] = inv.get(p, 0) + tile["yield_units"]
                tile["yield_units"] = 0
            return
        if op == "FERTILIZE":
            if not (isinstance(tile, dict) and tile.get("kind") == "PLANT"):
                return
            if inv.get("FERTILIZER", 0) < 1:
                return
            inv["FERTILIZER"] -= 1
            if inv["FERTILIZER"] == 0:
                del inv["FERTILIZER"]
            tile["fertilized_until_day"] = max(tile.get("fertilized_until_day", -1), self.day + 2)
            return
        if op == "DIG":
            if tile is None or (isinstance(tile, dict) and "animal" in tile):
                return
            self.tiles[y][x] = None
            return
        if op == "BUILD_COOP" and tile is None:
            self.tiles[y][x] = {"kind": "COOP"}
            return
        if op == "BUILD_PASTURE" and tile is None:
            self.tiles[y][x] = {"kind": "PASTURE"}
            return
        if op == "FEED":
            if not (isinstance(tile, dict) and "animal" in tile) or tile["fed_today"]:
                return
            if inv.get("WHEAT", 0) < 1:
                return
            inv["WHEAT"] -= 1
            if inv["WHEAT"] == 0:
                del inv["WHEAT"]
            tile["fed_today"] = True
            return
        if op == "COLLECT_FERTILIZER":
            if not (isinstance(tile, dict) and "animal" in tile):
                return
            if not tile["fertilizer_available"]:
                return
            tile["fertilizer_available"] = False
            inv["FERTILIZER"] = inv.get("FERTILIZER", 0) + 1
            return
        if op == "CARE":
            if isinstance(tile, dict) and "animal" in tile and not tile["cared_today"]:
                tile["cared_today"] = True
            return

    # ------------------------------------------------------------- day rollover
    def end_of_day(self):
        for y in range(self.n):
            for x in range(self.n):
                t = self.tiles[y][x]
                if not isinstance(t, dict):
                    continue
                if t.get("kind") == "PLANT":
                    self._refresh_plant(x, y, t)
                elif "animal" in t:
                    self._refresh_animal(t)
        for inv in self.invs:
            for item, k in list(inv.items()):
                if k <= 0:
                    del inv[item]
                    continue
                room = max(0, self.shed_cap - sum(self.shed.values()))
                take = min(k, room)
                if take:
                    self.shed[item] = self.shed.get(item, 0) + take
                del inv[item]
        self.units = [list(shed_tiles(self.n)[0])]
        self.invs = [{}]
        self.hires_today = 0

    def _refresh_plant(self, x, y, t):
        nxt = self.day + 1
        was = t["watered_today"]
        t["consecutive_unwatered"] = 0 if was else t["consecutive_unwatered"] + 1
        t["watered_today"] = False
        if t["consecutive_unwatered"] >= 2:
            self.tiles[y][x] = {"kind": "WEED"}
            return
        cd = CROPS[t["crop"]]
        if not cd["ongoing"]:
            return
        k = nxt - t["planted_day"] - cd["first"]
        if k < 0 or k % cd["interval"] != 0:
            return
        count = k // cd["interval"] + 1
        if count > cd["maxy"]:
            return
        fert = was and t.get("fertilized_until_day", -1) >= self.day
        t["yield_units"] = min(cd["maxy"], t["yield_units"] + (2 if fert else 1))
        if count == cd["maxy"]:
            t["max_lifespan_step"] = (nxt + 1) * self.turns_per_day

    def _refresh_animal(self, t):
        nxt = self.day + 1
        t["consecutive_unfed"] = 0 if t["fed_today"] else t["consecutive_unfed"] + 1
        if t["consecutive_unfed"] >= 2:
            t.clear()
            t["kind"] = "PASTURE"
            return
        a = ANIMALS[t["animal"]]
        k = nxt - t["placed_day"] - a["first"]
        if k >= 0 and k % a["interval"] == 0:
            bonus = t.pop("pending_care_bonus", 0) if t["fed_today"] else 0
            t["yield_units"] = min(a["held"], t["yield_units"] + 1 + bonus)
            t["pending_care_bonus"] = 0
        if t["cared_today"] and t["fed_today"]:
            t["pending_care_bonus"] = t.get("pending_care_bonus", 0) + 1
        t["fertilizer_available"] = True
        t["fed_today"] = False
        t["cared_today"] = False

    def decay(self, step):
        for y in range(self.n):
            for x in range(self.n):
                t = self.tiles[y][x]
                if not isinstance(t, dict) or t.get("kind") != "PLANT":
                    continue
                mls = t["max_lifespan_step"]
                if mls < 0 or step < mls or (step - mls) % 2 != 0:
                    continue
                t["yield_units"] -= 1
                if t["yield_units"] <= 0:
                    self.tiles[y][x] = {"kind": "WEED"}


def _copy_tile(t):
    if isinstance(t, dict):
        return dict(t)
    return t


def _new_plant(crop, day, tpd):
    cd = CROPS[crop]
    return {"kind": "PLANT", "crop": crop, "planted_day": day, "watered_today": False,
            "consecutive_unwatered": 1, "yield_units": 0 if cd["ongoing"] else 1,
            "max_lifespan_step": -1 if cd["ongoing"] else (day + cd["myd"] + 1) * tpd,
            "fertilized_until_day": -1}


def _new_animal(animal, day):
    return {"kind": ANIMALS[animal]["struct"], "animal": animal, "placed_day": day,
            "yield_units": 0, "consecutive_unfed": 0, "fed_today": False,
            "cared_today": False, "fertilizer_available": False, "pending_care_bonus": 0}


# ---------------------------------------------------------------- market ----
# The engine walks orders one unit at a time: SELL is quoted at the pre-sell
# inventory, BUY_PRODUCT at the post-buy inventory (so an immediate round trip is
# exactly zero). Both players interleave, so against a live opponent this is a
# forecast, not a certainty -- but for our own planning it is exact enough, and it
# is exact when the opponent is idle.

def apply_market(farm, orders, prices, inventory, price_fn, max_orders=10):
    """Apply our market orders to `farm`, walking prices as the engine does."""
    inv = dict(inventory)
    for o in (orders or [])[:max_orders]:
        if not o:
            continue
        op = o[0]
        if op == "HIRE":
            cost = fib(farm.hires_today)
            if farm.money < cost:
                continue
            farm.money -= cost
            farm.hires_today += 1
            farm.units.append(list(shed_tiles(farm.n)[0]))
            farm.invs.append({})
            continue
        if op == "BUY_LAND":
            extra = len(farm.quads) - 1
            if extra >= len(LAND_ORDER):
                continue
            cost = LAND_PRICES[extra]
            if farm.money < cost:
                continue
            farm.money -= cost
            q = LAND_ORDER[extra]
            farm.quads.append(q)
            for y in range(farm.n):
                for x in range(farm.n):
                    if quadrant_of(x, y, farm.n) == q and farm.tiles[y][x] == "LOCKED":
                        farm.tiles[y][x] = None
            continue
        if len(o) < 3:
            continue
        item, n = o[1], int(o[2])
        for _ in range(max(0, n)):
            if op == "SELL":
                if farm.shed.get(item, 0) <= 0:
                    break
                px = price_fn(item, inv[item])
                farm.shed[item] -= 1
                farm.money += px
                if px > 1:
                    inv[item] += 1
            elif op == "BUY_PRODUCT" and item in ("WHEAT", "FERTILIZER"):
                px = price_fn(item, inv[item] - 1)
                if farm.money < px or sum(farm.shed.values()) >= farm.shed_cap:
                    break
                farm.money -= px
                farm.shed[item] = farm.shed.get(item, 0) + 1
                inv[item] -= 1
            elif op == "BUY_SEED" and item in CROPS:
                px = CROPS[item]["seed"]
                if farm.money < px:
                    break
                farm.money -= px
                farm.seeds[item] = farm.seeds.get(item, 0) + 1
            elif op == "BUY_ANIMAL" and item in ANIMALS:
                px = ANIMALS[item]["cost"]
                if farm.money < px or sum(farm.shed.values()) >= farm.shed_cap:
                    break
                farm.money -= px
                farm.shed[item] = farm.shed.get(item, 0) + 1
            else:
                break
    return inv
