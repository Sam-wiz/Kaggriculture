"""Kaggriculture agent -- marginal-value task scheduler.

Every farmer/hand action is scored by the marginal dollars it creates (extra
yield, avoided spoilage, freed tile), divided by the turns it costs to walk
there. Macro decisions (hire / land / animals / seeds / sell rate) are driven by
forecast market prices that account for town drain and our own pipeline.
"""

import math

# ------------------------------------------------------------------ constants
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
PRODUCTS = ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL", "FERTILIZER"]
MARKET_PARAMS = {
    "WHEAT":      {"base":  25, "T": 400, "bf": "sqrt",   "bt": 0.80, "af": "log",    "at": 0.20},
    "CARROT":     {"base":  35, "T": 450, "bf": "hinge",  "bt": 1.00, "af": "sqrt",   "at": 0.70},
    "TOMATO":     {"base":  60, "T": 200, "bf": "hinge",  "bt": 0.40, "af": "sqrt",   "at": 0.60},
    "STRAWBERRY": {"base": 120, "T": 100, "bf": "sqrt",   "bt": 0.70, "af": "linear", "at": 1.60},
    "MELON":      {"base": 250, "T": 300, "bf": "log",    "bt": 0.20, "af": "sq",     "at": 3.60},
    "EGG":        {"base":  50, "T": 332, "bf": "hinge",  "bt": 0.40, "af": "log",    "at": 0.20},
    "MILK":       {"base": 160, "T": 122, "bf": "sqrt",   "bt": 0.60, "af": "linear", "at": 1.60},
    "WOOL":       {"base": 200, "T": 105, "bf": "log",    "bt": 0.20, "af": "sq",     "at": 3.20},
    "FERTILIZER": {"base": 100, "T": 200, "bf": "linear", "bt": 0.40, "af": "linear", "at": 0.40},
}
SHOPS = {
    "BAKERY":         ["EGG", "WHEAT"],
    "PIZZA_SHOP":     ["MILK", "TOMATO", "WHEAT"],
    "BRUNCH_SPOT":    ["EGG", "WHEAT", "STRAWBERRY"],
    "YARN_STORE":     ["WOOL"],
    "ICE_CREAM_SHOP": ["STRAWBERRY", "MILK", "WHEAT"],
    "PET_CAFE":       ["CARROT"],
    "SMOOTHIE_SHOP":  ["STRAWBERRY", "MILK"],
    "FARMERS_MARKET": ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY"],
}
I0 = 10000
HINGE_GAIN = 8.0
LAND_PRICES = [1000, 2000, 4000]
LAST_DAY = 29

# Per-tile production recipes: days = age at final harvest, u = units without
# fertilizer, uf = units with, a = farmer actions, f = fertilizer units used.
RECIPES = {
    "WHEAT":      {"days": 4,  "u": 4, "uf": 6, "a": 6,  "f": 1},
    "CARROT":     {"days": 3,  "u": 3, "uf": 4, "a": 5,  "f": 1},
    "TOMATO":     {"days": 11, "u": 4, "uf": 8, "a": 13, "f": 2},
    "STRAWBERRY": {"days": 16, "u": 4, "uf": 8, "a": 14, "f": 2},
    "MELON":      {"days": 10, "u": 6, "uf": 6, "a": 10, "f": 0},
}

P = dict(
    action_value=9.0,        # $ opportunity cost of one unit-action
    max_hands=13,
    hire_money_frac=0.30,
    seed_budget_frac=0.55,
    land_reserve=250,
    animal_hurdle=1.35,      # required revenue / cost before buying an animal
    sell_bias_glut=1.40,     # front-load selling when we are oversupplying
    sell_bias_tight=0.80,    # defer selling when the town can absorb it
    shed_pressure=72,
    wheat_buffer=2.0,        # days of animal feed to keep in the shed
    fert_keep=6,             # fertilizer units to hold back for crop boosting
    plant_min_score=6.0,     # $ per tile-day floor to bother planting
)


# ------------------------------------------------------------------ pricing --
def _shape(func, x, T):
    if x < 0.0:
        x = 0.0
    if func == "linear":
        return x
    if func == "sq":
        return x * x
    if func == "sqrt":
        return math.sqrt(x)
    if func == "log":
        return math.log(1.0 + x)
    if func == "log10":
        return math.log10(1.0 + x)
    if func == "hinge":
        if not T or T <= 0:
            return x
        u = x / T
        d = u - 1.0
        return u + HINGE_GAIN * (d * d if d > 0 else 0.0)
    return x


def market_price(item, inv):
    p = MARKET_PARAMS[item]
    base, T = p["base"], p["T"]
    if inv < I0:
        amp = p["bt"] * base / _shape(p["bf"], T, T)
        price = base + amp * _shape(p["bf"], I0 - inv, T)
    else:
        amp = p["at"] * base / _shape(p["af"], T, T)
        price = base - amp * _shape(p["af"], inv - I0, T)
    v = int(round(price))
    return 1 if v < 1 else v


def sale_revenue(item, inv, n):
    """Exact revenue for dumping n units starting from market inventory `inv`."""
    total = 0
    for _ in range(n):
        v = market_price(item, inv)
        total += v
        if v > 1:
            inv += 1
    return total


# -------------------------------------------------------------------- agent --
class Farmer:
    def __init__(self):
        self.reset()

    def reset(self):
        self.targets = {}        # unit index -> (x, y, op, arg)
        self.sold_today = {}
        self.day = -1
        self.hires_wanted = 0
        self.animal_plan = {}    # (x,y) -> animal name reserved for that structure

    # ---------------------------------------------------------------- helpers
    def drain_rates(self, shops):
        """Units of each product the town removes from the market per day."""
        d = {p: 0.0 for p in PRODUCTS}
        for shop in shops:
            prods = SHOPS.get(shop)
            if not prods:
                continue
            mult = 2.0 if len(prods) == 1 else 1.0
            for p in prods:
                d[p] += mult * 6.0
        for p in PRODUCTS:
            if p != "FERTILIZER":
                d[p] += 1.0
        return d

    def forecast(self, item, days_ahead, extra_supply=0.0):
        inv = self.inv[item] - self.drain[item] * days_ahead + extra_supply
        return market_price(item, inv)

    # -------------------------------------------------------------- main call
    def __call__(self, obs):
        step = obs.get("step", 0)
        if step == 0:
            self.reset()
        me = obs["player"]
        farm = obs["farms"][me]
        priv = obs["private"]
        day = obs["day"]
        hour = obs["hour"]
        tiles = farm["tiles"]
        n = len(tiles)
        self.n = n
        self.half = n // 2
        self.day_left = LAST_DAY - day          # 0 on the final day
        self.money = farm["money"]
        self.shed = priv["shed"]
        self.seeds = priv["seeds"]
        self.invs = priv["inventories"]
        self.market = obs["market"]
        self.inv = self.market["inventory"]
        self.price = self.market["prices"]
        self.drain = self.drain_rates(obs["town"].get("unlocked_shops", []))
        self.tiles = tiles
        self.farm = farm

        if day != self.day:
            self.day = day
            self.sold_today = {}
            self.day_budget = {}

        self.scan()
        units = [list(farm["farmer"])] + [list(h) for h in farm["hands"]]
        self.units = units

        orders = self.market_orders(obs, hour, day)
        acts = self.unit_actions(units, day, hour)
        return {"farmer": acts[0], "hands": acts[1:], "market": orders[:10]}

    # ------------------------------------------------------------------ scan
    def scan(self):
        """One pass over the board: inventory of what exists and what it owes us."""
        tiles = self.tiles
        n = self.n
        self.empty = []
        self.weeds = []
        self.plants = []
        self.animals = []
        self.free_struct = []
        self.n_animals = 0
        self.pipeline = {p: 0.0 for p in PRODUCTS}
        for y in range(n):
            row = tiles[y]
            for x in range(n):
                t = row[x]
                if t is None:
                    self.empty.append((x, y))
                elif t == "LOCKED":
                    continue
                elif t["kind"] == "WEED":
                    self.weeds.append((x, y))
                elif t["kind"] == "PLANT":
                    self.plants.append((x, y, t))
                    self.pipeline[t["crop"]] += self.plant_future_units(t)
                elif "animal" in t:
                    self.animals.append((x, y, t))
                    self.n_animals += 1
                    a = ANIMALS[t["animal"]]
                    rem = max(0, self.day_left - 1)
                    self.pipeline[a["product"]] += t["yield_units"] + rem * (1 + a["interval"]) / a["interval"]
                    self.pipeline["FERTILIZER"] += rem
                else:
                    self.free_struct.append((x, y, t["kind"]))
        for p in PRODUCTS:
            self.pipeline[p] += self.shed.get(p, 0)
            for iv in self.invs:
                self.pipeline[p] += iv.get(p, 0)

    def plant_future_units(self, t):
        """Units this plant will still hand us if tended to the end."""
        cd = CROPS[t["crop"]]
        age = self.day - t["planted_day"]
        if not cd["ongoing"]:
            room = cd["maxy"] - t["yield_units"]
            days = max(0, min(cd["myd"], self.day + self.day_left) - max(age, (cd["myd"] + 1) // 2) + 1)
            return t["yield_units"] + min(room, days)
        done = 0
        k = age - cd["first"]
        if k >= 0:
            done = k // cd["interval"] + 1
        left = max(0, cd["maxy"] - done)
        left = min(left, self.day_left // max(1, cd["interval"]) + 1)
        return t["yield_units"] + left * 1.5

    # ------------------------------------------------------------ crop choice
    def crop_score(self, crop, day):
        """Expected $ per tile-day for planting `crop` today, net of inputs."""
        r = RECIPES[crop]
        if day + r["days"] > LAST_DAY:
            return -1.0, 0
        fert_ok = self.fert_available() and r["f"] > 0 and r["uf"] > r["u"]
        units = r["uf"] if fert_ok else r["u"]
        acts = r["a"] + (r["f"] if fert_ok else 0)
        pr = self.forecast(crop, r["days"], extra_supply=self.pipeline[crop] * 0.5)
        gross = units * pr
        cost = CROPS[crop]["seed"] + acts * P["action_value"]
        if fert_ok:
            cost += r["f"] * self.price["FERTILIZER"] * 0.5
        return (gross - cost) / r["days"], units

    def fert_available(self):
        held = self.shed.get("FERTILIZER", 0) + sum(iv.get("FERTILIZER", 0) for iv in self.invs)
        return held > 0 or self.n_animals >= 3

    def best_crop(self, day):
        best, bs = None, P["plant_min_score"]
        for crop in CROPS:
            s, _ = self.crop_score(crop, day)
            if s > bs:
                best, bs = crop, s
        return best, bs

    # --------------------------------------------------------- market orders
    def market_orders(self, obs, hour, day):
        orders = []
        farm = self.farm
        money = self.money

        # --- hiring: all up front so hands get a full day of turns
        if hour <= 1:
            want = self.target_hands()
            have = farm["hires_today"]
            todo = max(0, want - have)
            if hour == 0:
                todo = min(todo, 10)
            for _ in range(min(todo, 10)):
                orders.append(["HIRE"])
            money -= self.hire_cost(have, min(todo, 10))
            if len(orders) >= 10:
                return orders

        # --- selling
        sells = self.sell_orders(day)
        # --- buying
        buys, money = self.buy_orders(day, money)

        # sells first: they fund the buys inside the same turn
        orders.extend(sells)
        orders.extend(buys)
        return orders

    def hire_cost(self, already, k):
        a, b = 1, 1
        for _ in range(already):
            a, b = b, a + b
        tot = 0
        for _ in range(k):
            tot += a
            a, b = b, a + b
        return tot

    def target_hands(self):
        """Enough hands to service the board, capped by what hiring costs."""
        work = 0.0
        for _x, _y, t in self.plants:
            work += 1.35
        work += self.n_animals * 3.6
        work += min(len(self.empty), 30) * 1.2
        work += len(self.weeds) * 1.0
        work *= 1.45                      # travel overhead
        want = int(math.ceil(work / 21.0)) - 1
        want = max(0, min(P["max_hands"], want))
        budget = max(60.0, self.money * P["hire_money_frac"])
        while want > 0 and self.hire_cost(0, want) > budget:
            want -= 1
        return want

    def sell_orders(self, day):
        out = []
        shed_total = sum(self.shed.values())
        horizon = max(1, self.day_left + 1)
        for p in PRODUCTS:
            stock = self.shed.get(p, 0)
            if stock <= 0:
                continue
            if p == "WHEAT":
                keep = int(self.n_animals * P["wheat_buffer"]) + 2
                stock = max(0, stock - keep)
                if stock <= 0:
                    continue
            if p == "FERTILIZER":
                stock = max(0, stock - P["fert_keep"])
                if stock <= 0:
                    continue
            already = self.sold_today.get(p, 0)
            if day >= LAST_DAY - 1:
                q = stock
            else:
                total = max(stock, self.pipeline[p])
                q = total / horizon
                bias = P["sell_bias_glut"] if total > self.drain[p] * horizon else P["sell_bias_tight"]
                q = q * bias
                q = max(q, min(stock, self.drain[p] * 0.5))
                q = int(math.ceil(q)) - already
                if shed_total > P["shed_pressure"]:
                    q = max(q, stock // 2)
                q = min(q, stock)
            if q <= 0:
                continue
            # spread the daily quota across the turns that remain today
            out.append(["SELL", p, int(q)])
            self.sold_today[p] = already + int(q)
        return out

    def buy_orders(self, day, money):
        out = []
        farm = self.farm

        # --- land: cheap, permanent, and the tiles pay for themselves fast
        n_extra = len(farm["unlocked_quadrants"]) - 1
        if n_extra < 3 and day <= 21:
            cost = LAND_PRICES[n_extra]
            if money >= cost + P["land_reserve"] and len(self.empty) <= 14 + 8 * n_extra:
                out.append(["BUY_LAND"])
                money -= cost

        # --- wheat for feed
        need = int(self.n_animals * P["wheat_buffer"]) + 3
        have = self.shed.get("WHEAT", 0)
        if self.n_animals and have < need and self.day_left > 0:
            grow = self.pipeline["WHEAT"]
            want = need - have
            if grow < need:
                wp = market_price("WHEAT", self.inv["WHEAT"] - 1)
                if money > wp * want + 200:
                    out.append(["BUY_PRODUCT", "WHEAT", int(want)])
                    money -= wp * want

        # --- animals
        pend = sum(self.shed.get(a, 0) for a in ANIMALS)
        if pend == 0 and self.day_left >= 5:
            pick = self.best_animal(money)
            if pick:
                out.append(["BUY_ANIMAL", pick, 1])
                money -= ANIMALS[pick]["cost"]

        # --- seeds
        crop, score = self.best_crop(day)
        if crop:
            slots = len(self.empty) - len(self.animal_plan)
            slots = max(0, min(slots, 24))
            have = self.seeds.get(crop, 0)
            want = slots - have
            if want > 0:
                sc = CROPS[crop]["seed"]
                budget = money * P["seed_budget_frac"]
                want = min(want, int(budget // sc))
                if want > 0:
                    out.append(["BUY_SEED", crop, want])
                    money -= sc * want
        return out, money

    def best_animal(self, money):
        best, bv = None, 0.0
        for name, a in ANIMALS.items():
            prod_days = self.day_left - a["first"]
            if prod_days < 3:
                continue
            if money < a["cost"] + 250:
                continue
            per_day = min(1 + a["interval"], a["held"]) / a["interval"]
            units = per_day * prod_days
            pr = self.forecast(a["product"], prod_days * 0.6,
                               extra_supply=self.pipeline[a["product"]] * 0.6)
            wheat = market_price("WHEAT", self.inv["WHEAT"]) * (prod_days + a["first"])
            fert = prod_days * self.price["FERTILIZER"] * 0.5
            net = units * pr + fert - wheat
            if net > a["cost"] * P["animal_hurdle"] and net > bv:
                best, bv = name, net
        return best

    # ----------------------------------------------------------- unit actions
    def unit_actions(self, units, day, hour):
        tasks = self.build_tasks(day)
        acts = []
        claimed = set()
        shed_tiles = {(self.half - 1, self.half - 1), (self.half, self.half - 1),
                      (self.half - 1, self.half), (self.half, self.half)}
        n_units = len(units)
        wheat_need = sum(1 for _x, _y, t in self.animals if not t["fed_today"])
        wheat_have = sum(iv.get("WHEAT", 0) for iv in self.invs[:n_units])

        for i, (ux, uy) in enumerate(units):
            inv = self.invs[i] if i < len(self.invs) else {}
            at_shed = (ux, uy) in shed_tiles

            # supply run: grab feed / animals / fertilizer while standing at the shed
            if at_shed:
                sup = self.shed_pickup(i, inv, wheat_need, wheat_have)
                if sup is not None:
                    acts.append(sup)
                    if sup[0] == "PICKUP" and sup[1] == "WHEAT":
                        wheat_have += sup[2]
                    continue

            # last day: make sure carried goods reach the shed in time to be sold
            if day >= LAST_DAY and inv:
                d = self.shed_dist(ux, uy)
                if hour >= 21 - d:
                    if at_shed:
                        acts.append(["DROP"])
                        continue
                    acts.append(self.step_toward(ux, uy, self.shed_goal(ux, uy)))
                    continue

            tgt = self.pick_task(i, ux, uy, inv, tasks, claimed)
            if tgt is None:
                if inv and day >= LAST_DAY:
                    acts.append(self.step_toward(ux, uy, self.shed_goal(ux, uy)))
                else:
                    acts.append(["PASS"])
                continue
            x, y, op, arg, _v = tgt
            claimed.add((x, y, op))
            if (ux, uy) == (x, y):
                acts.append([op] if arg is None else [op, arg])
            else:
                acts.append(self.step_toward(ux, uy, (x, y)))
        return acts

    def shed_dist(self, x, y):
        h = self.half
        return abs(x - min(max(x, h - 1), h)) + abs(y - min(max(y, h - 1), h))

    def shed_goal(self, x, y):
        h = self.half
        return (min(max(x, h - 1), h), min(max(y, h - 1), h))

    def shed_pickup(self, i, inv, wheat_need, wheat_have):
        # animals waiting in the shed for a structure to stand on
        for a in ANIMALS:
            if self.shed.get(a, 0) > 0 and inv.get(a, 0) == 0:
                for _x, _y, kind in self.free_struct:
                    if kind == ANIMALS[a]["struct"]:
                        return ["PICKUP", a, 1]
        if wheat_need > wheat_have and self.shed.get("WHEAT", 0) > 0:
            take = min(self.shed["WHEAT"], max(1, wheat_need - wheat_have), 12)
            if inv.get("WHEAT", 0) < 3:
                return ["PICKUP", "WHEAT", int(take)]
        return None

    def step_toward(self, ux, uy, goal):
        gx, gy = goal
        dx, dy = gx - ux, gy - uy
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

    def pick_task(self, i, ux, uy, inv, tasks, claimed):
        best, bs = None, 0.0
        prev = self.targets.get(i)
        for t in tasks:
            x, y, op, arg, v = t
            if (x, y, op) in claimed:
                continue
            if op == "FEED" and inv.get("WHEAT", 0) <= 0:
                continue
            if op == "FERTILIZE" and inv.get("FERTILIZER", 0) <= 0:
                continue
            if op == "PLACE" and inv.get(arg, 0) <= 0:
                continue
            d = abs(x - ux) + abs(y - uy)
            s = v / (1.0 + d)
            if prev is not None and prev[0] == x and prev[1] == y and prev[2] == op:
                s *= 1.25          # stickiness: finish what we walked toward
            if s > bs:
                best, bs = t, s
        self.targets[i] = (best[0], best[1], best[2]) if best else None
        return best

    # ------------------------------------------------------------ task table
    def build_tasks(self, day):
        tasks = []
        av = P["action_value"]
        left = self.day_left

        for x, y, t in self.animals:
            a = ANIMALS[t["animal"]]
            pr = self.price[a["product"]]
            per_prod = min(1 + a["interval"], a["held"])
            if not t["fed_today"]:
                v = pr * 1.0
                if t["consecutive_unfed"] >= 1:
                    v += 400.0 + per_prod * pr * max(0, left) / a["interval"]
                tasks.append((x, y, "FEED", None, v))
            if not t["cared_today"] and left >= 1:
                tasks.append((x, y, "CARE", None, pr * 0.9))
            if t["fertilizer_available"]:
                tasks.append((x, y, "COLLECT_FERTILIZER", None, self.price["FERTILIZER"] * 0.85))
            yu = t["yield_units"]
            if yu > 0:
                waste = max(0, yu + per_prod - a["held"])
                v = waste * pr + yu * pr * 0.10
                if day >= LAST_DAY - 1:
                    v = yu * pr
                tasks.append((x, y, "HARVEST", None, v))

        for x, y, t in self.plants:
            crop = t["crop"]
            cd = CROPS[crop]
            pr = self.price[crop]
            age = day - t["planted_day"]
            fert = t["fertilized_until_day"] >= day
            if not t["watered_today"]:
                v = 0.0
                if not cd["ongoing"]:
                    ws = (cd["myd"] + 1) // 2
                    if ws <= age <= cd["myd"] and t["yield_units"] < cd["maxy"]:
                        v = pr * (2.0 if fert else 1.0)
                else:
                    k = (day + 1) - t["planted_day"] - cd["first"]
                    if k >= 0 and k % cd["interval"] == 0 and fert:
                        v = pr
                if t["consecutive_unwatered"] >= 1:
                    v += self.plant_future_units(t) * pr * 0.8 + 30.0
                if v > 0:
                    tasks.append((x, y, "WATER", None, v))
            if t["yield_units"] > 0 and age >= cd["first"]:
                v = 0.0
                if not cd["ongoing"]:
                    ripe = t["yield_units"] >= cd["maxy"] or age >= cd["myd"]
                    if ripe:
                        v = t["yield_units"] * pr * 0.35 + 25.0
                    if age > cd["myd"]:
                        v = t["yield_units"] * pr
                else:
                    k = (day + 1) - t["planted_day"] - cd["first"]
                    prod_tonight = k >= 0 and k % cd["interval"] == 0
                    waste = 0
                    if prod_tonight:
                        waste = max(0, t["yield_units"] + (2 if fert else 1) - cd["maxy"])
                    v = waste * pr + t["yield_units"] * pr * 0.12
                if day >= LAST_DAY - 1:
                    v = t["yield_units"] * pr
                if v > 0:
                    tasks.append((x, y, "HARVEST", None, v))
            if (not fert) and left >= 2:
                r = RECIPES[crop]
                gain = 0.0
                if cd["ongoing"]:
                    k = (day + 1) - t["planted_day"] - cd["first"]
                    if k >= -1:
                        gain = pr * min(2, cd["maxy"])
                elif age <= cd["myd"] - 1 and t["yield_units"] < cd["maxy"]:
                    gain = pr * min(2, cd["maxy"] - t["yield_units"])
                net = gain - self.price["FERTILIZER"] - av
                if net > 0 and r["f"] > 0:
                    tasks.append((x, y, "FERTILIZE", None, net))

        # planting / building / clearing
        crop, score = self.best_crop(day)
        reserve = self.animal_reserve()
        for (x, y) in self.empty:
            if (x, y) in reserve:
                a = reserve[(x, y)]
                op = "BUILD_COOP" if ANIMALS[a]["struct"] == "COOP" else "BUILD_PASTURE"
                tasks.append((x, y, op, None, 250.0))
                continue
            if crop and self.seeds.get(crop, 0) > 0:
                tasks.append((x, y, "PLANT", crop, score * RECIPES[crop]["days"] * 0.5))
        for (x, y, kind) in self.free_struct:
            for a in ANIMALS:
                if ANIMALS[a]["struct"] == kind and (self.shed.get(a, 0) > 0 or
                                                     any(iv.get(a, 0) for iv in self.invs)):
                    tasks.append((x, y, "PLACE", a, 400.0))
                    break
        if left >= 2:
            _c, s = self.best_crop(day)
            dv = max(8.0, s) * min(left, 6)
            for (x, y) in self.weeds:
                tasks.append((x, y, "DIG", None, dv))
        return tasks

    def animal_reserve(self):
        """Empty tiles nearest the shed, held for coops/pastures we still owe."""
        pend = {}
        for a in ANIMALS:
            k = self.shed.get(a, 0) + sum(iv.get(a, 0) for iv in self.invs)
            if k:
                pend[a] = k
        if not pend:
            return {}
        free = {}
        for _x, _y, kind in self.free_struct:
            free[kind] = free.get(kind, 0) + 1
        need = []
        for a, k in pend.items():
            st = ANIMALS[a]["struct"]
            avail = free.get(st, 0)
            use = min(k, avail)
            free[st] = avail - use
            for _ in range(k - use):
                need.append(a)
        if not need:
            return {}
        cand = sorted(self.empty, key=lambda c: self.shed_dist(c[0], c[1]))
        return {cand[i]: need[i] for i in range(min(len(need), len(cand)))}


_AGENT = Farmer()


def agent(obs):
    return _AGENT(obs)
