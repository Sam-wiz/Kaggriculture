"""Kaggriculture agent v2.

Design:
  * Every unit-action is scored by the marginal dollars it creates, divided by
    the turns spent walking to it. Units keep a sticky target so they sweep a
    zone instead of oscillating.
  * Planting is a saturation-aware greedy allocation: each free tile goes to
    whichever crop has the best discounted $/tile-day *given the supply we have
    already committed*, so the mix self-diversifies and pours tiles into
    whatever the town actually demands (the hinge curves on carrot/tomato/egg
    can push those to 10x base).
  * Land is bought as early as cash allows -- 75 extra tiles for $7k pays back
    many times over.
  * Animals are bought in batches, and every unit tops up on wheat at the shed
    each morning so nothing starves.
"""

import math

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

# days = age at final harvest, u/uf = units without / with fertilizer,
# a = unit-actions, f = fertilizer consumed, touch = actions per tile-day
RECIPES = {
    "WHEAT":      {"days": 4,  "u": 4, "uf": 6, "a": 6,  "f": 1},
    "CARROT":     {"days": 3,  "u": 3, "uf": 4, "a": 5,  "f": 1},
    "TOMATO":     {"days": 11, "u": 4, "uf": 8, "a": 13, "f": 2},
    "STRAWBERRY": {"days": 16, "u": 4, "uf": 8, "a": 14, "f": 2},
    "MELON":      {"days": 10, "u": 6, "uf": 6, "a": 10, "f": 0},
}

P = dict(
    action_value=6.0,
    max_hands=13,
    hire_budget_frac=0.35,
    hire_budget_min=150.0,
    land_reserve=350.0,
    land_last_day=22,
    animal_hurdle=1.30,
    animal_batch=3,
    animal_last_buy=22,
    disc_early=0.12,       # per-day discount while land is still unbought
    disc_late=0.025,
    plant_min_score=4.0,
    plan_lookahead=8,      # tiles expected to free up soon
    seed_budget_frac=0.60,
    wheat_per_unit=2,      # spare wheat each unit carries beyond its feed needs
    fert_keep=8,
    sell_hold_gain=0.055,  # hold stock if a day of town drain lifts price this much
    shed_pressure=70,
    drop_hour=17,          # last day: be back at the shed by here
)


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


class Farmer:
    def __init__(self):
        self.reset()

    def reset(self):
        self.targets = {}
        self.day = -1
        self.sold_today = {}
        self.plan = []

    # ------------------------------------------------------------- entry point
    def __call__(self, obs):
        if obs.get("step", 0) == 0:
            self.reset()
        me = obs["player"]
        farm = obs["farms"][me]
        priv = obs["private"]
        self.farm = farm
        self.tiles = farm["tiles"]
        self.n = len(self.tiles)
        self.half = self.n // 2
        self.day = day = obs["day"]
        self.hour = hour = obs["hour"]
        self.day_left = LAST_DAY - day
        self.money = farm["money"]
        self.shed = priv["shed"]
        self.seeds = priv["seeds"]
        self.invs = priv["inventories"]
        self.market = obs["market"]
        self.inv = self.market["inventory"]
        self.price = self.market["prices"]
        self.drain = self.drain_rates(obs["town"].get("unlocked_shops", []))
        self.n_quads = len(farm["unlocked_quadrants"])
        if hour == 0:
            self.sold_today = {}

        self.scan()
        self.plan = self.plan_crops(day)
        units = [list(farm["farmer"])] + [list(h) for h in farm["hands"]]

        orders = self.market_orders(hour, day)
        acts = self.unit_actions(units, day, hour)
        return {"farmer": acts[0], "hands": acts[1:], "market": orders[:10]}

    # ------------------------------------------------------------------ market
    def drain_rates(self, shops):
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

    def forecast(self, item, days_ahead, extra=0.0):
        return market_price(item, self.inv[item] - self.drain[item] * days_ahead + extra)

    def discount(self, days):
        r = P["disc_early"] if (self.n_quads < 4 and self.day <= 14) else P["disc_late"]
        return 1.0 / (1.0 + r) ** days

    # -------------------------------------------------------------------- scan
    def scan(self):
        tiles = self.tiles
        n = self.n
        self.empty = []
        self.weeds = []
        self.plants = []
        self.animals = []
        self.free_struct = []
        self.pipeline = {p: 0.0 for p in PRODUCTS}
        self.n_animals = 0
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
                    self.pipeline[t["crop"]] += self.plant_future(t)
                elif "animal" in t:
                    self.animals.append((x, y, t))
                    self.n_animals += 1
                    a = ANIMALS[t["animal"]]
                    rem = max(0, self.day_left - 1)
                    self.pipeline[a["product"]] += t["yield_units"] + rem * min(1 + a["interval"], a["held"]) / a["interval"]
                    self.pipeline["FERTILIZER"] += rem
                else:
                    self.free_struct.append((x, y, t["kind"]))
        for p in PRODUCTS:
            self.pipeline[p] += self.shed.get(p, 0)
            for iv in self.invs:
                self.pipeline[p] += iv.get(p, 0)

    def plant_future(self, t):
        cd = CROPS[t["crop"]]
        age = self.day - t["planted_day"]
        if not cd["ongoing"]:
            room = cd["maxy"] - t["yield_units"]
            last = min(cd["myd"], age + self.day_left)
            days = max(0, last - max(age, (cd["myd"] + 1) // 2) + 1)
            return t["yield_units"] + min(room, days)
        k = age - cd["first"]
        done = (k // cd["interval"] + 1) if k >= 0 else 0
        left = max(0, cd["maxy"] - done)
        left = min(left, self.day_left // max(1, cd["interval"]) + 1)
        return t["yield_units"] + left * 1.5

    # ------------------------------------------------------------ crop planner
    def crop_value(self, crop, day, extra):
        """Discounted $ per tile-day for planting `crop` today given committed supply."""
        r = RECIPES[crop]
        if day + r["days"] > LAST_DAY:
            return None
        fert = self.fert_supply() > 0 and r["uf"] > r["u"]
        units = r["uf"] if fert else r["u"]
        acts = r["a"] + (r["f"] if fert else 0)
        pr = self.forecast(crop, r["days"] * 0.6, extra=extra)
        gross = units * pr * self.discount(r["days"])
        cost = CROPS[crop]["seed"] + acts * P["action_value"]
        if fert:
            cost += r["f"] * self.price["FERTILIZER"] * 0.6
        return (gross - cost) / r["days"], units

    def fert_supply(self):
        return (self.shed.get("FERTILIZER", 0)
                + sum(iv.get("FERTILIZER", 0) for iv in self.invs)
                + self.n_animals)

    def plan_crops(self, day):
        """Greedy per-slot allocation; returns a list of crops, best first."""
        slots = len(self.empty) - len(self.reserved) + P["plan_lookahead"]
        slots = max(0, min(slots, 40))
        if slots == 0:
            return []
        extra = {c: self.pipeline[c] * 0.7 for c in CROPS}
        out = []
        for _ in range(slots):
            best, bs, bu = None, P["plant_min_score"], 0
            for c in CROPS:
                res = self.crop_value(c, day, extra[c])
                if res is None:
                    continue
                s, u = res
                if s > bs:
                    best, bs, bu = c, s, u
            if best is None:
                break
            out.append(best)
            extra[best] += bu
        return out

    # ---------------------------------------------------------- market orders
    def market_orders(self, hour, day):
        orders = []
        money = self.money
        if hour <= 1:
            want = self.target_hands()
            have = self.farm["hires_today"]
            todo = max(0, want - have)
            k = min(todo, 10)
            for _ in range(k):
                orders.append(["HIRE"])
            money -= self.hire_cost(have, k)
            if len(orders) >= 10:
                return orders

        sells = self.sell_orders(day)
        buys, money = self.buy_orders(day, money)
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
        work = len(self.plants) * 1.35 + self.n_animals * 3.6
        work += min(len(self.empty), 30) * 1.15 + len(self.weeds) * 1.0
        work *= 1.45
        want = int(math.ceil(work / 21.0)) - 1
        want = max(0, min(P["max_hands"], want))
        budget = max(P["hire_budget_min"], self.money * P["hire_budget_frac"])
        while want > 0 and self.hire_cost(0, want) > budget:
            want -= 1
        return want

    def carried(self, p):
        return sum(iv.get(p, 0) for iv in self.invs)

    def sell_orders(self, day):
        out = []
        shed_total = sum(self.shed.values())
        horizon = max(1, self.day_left + 1)
        for p in PRODUCTS:
            stock = self.shed.get(p, 0)
            if stock <= 0:
                continue
            if day >= LAST_DAY - 1:
                out.append(["SELL", p, int(stock + self.carried(p) + 5)])
                continue
            if p == "WHEAT":
                stock -= self.wheat_reserve()
            elif p == "FERTILIZER":
                stock -= P["fert_keep"]
            if stock <= 0:
                continue
            already = self.sold_today.get(p, 0)
            total = max(stock, self.pipeline[p])
            q = total / horizon
            # holding pays when a day of town drain lifts the price materially
            cur = self.price[p]
            nxt = market_price(p, self.inv[p] - self.drain[p])
            if cur > 0 and (nxt - cur) / cur > P["sell_hold_gain"] and shed_total < P["shed_pressure"]:
                q = min(q, stock / horizon)
            q = int(math.ceil(q)) - already
            if shed_total > P["shed_pressure"]:
                q = max(q, stock // 2)
            q = min(q, stock)
            if q > 0:
                out.append(["SELL", p, int(q)])
                self.sold_today[p] = already + int(q)
        return out

    def wheat_reserve(self):
        return int(self.n_animals * 1.6) + 4

    def buy_orders(self, day, money):
        out = []
        # land: earliest possible, it is the cheapest capacity in the game
        n_extra = self.n_quads - 1
        if n_extra < 3 and day <= P["land_last_day"]:
            cost = LAND_PRICES[n_extra]
            if money >= cost + P["land_reserve"] and self.land_pays(cost, day):
                out.append(["BUY_LAND"])
                money -= cost

        # wheat for feed
        if self.n_animals or self.pending_animals():
            need = self.wheat_reserve() + 6
            have = self.shed.get("WHEAT", 0) + self.carried("WHEAT")
            if have < need and self.day_left >= 0:
                wp = market_price("WHEAT", self.inv["WHEAT"] - 1)
                want = min(need - have, 25)
                if money > wp * want + 150:
                    out.append(["BUY_PRODUCT", "WHEAT", int(want)])
                    money -= wp * want

        # animals, in small batches
        if self.pending_animals() < P["animal_batch"] and day <= P["animal_last_buy"]:
            pick = self.best_animal(money)
            if pick:
                k = 1
                while (k < P["animal_batch"]
                       and money >= ANIMALS[pick]["cost"] * (k + 1) + 600):
                    k += 1
                out.append(["BUY_ANIMAL", pick, k])
                money -= ANIMALS[pick]["cost"] * k

        # seeds for the plan
        want = {}
        for c in self.plan:
            want[c] = want.get(c, 0) + 1
        budget = money * P["seed_budget_frac"]
        for c in sorted(want, key=lambda c: -CROPS[c]["seed"]):
            need = want[c] - self.seeds.get(c, 0)
            if need <= 0:
                continue
            sc = CROPS[c]["seed"]
            k = min(need, int(budget // sc))
            if k > 0:
                out.append(["BUY_SEED", c, k])
                budget -= sc * k
                money -= sc * k
        return out, money

    def land_pays(self, cost, day):
        left = self.day_left
        if left < 4:
            return False
        best = 0.0
        for c in CROPS:
            res = self.crop_value(c, day, self.pipeline[c])
            if res and res[0] > best:
                best = res[0]
        return 25 * best * min(left, 20) > cost * 1.2

    def pending_animals(self):
        return sum(self.shed.get(a, 0) + self.carried(a) for a in ANIMALS)

    def best_animal(self, money):
        best, bv = None, 0.0
        for name, a in ANIMALS.items():
            prod_days = self.day_left - a["first"]
            if prod_days < 3 or money < a["cost"] + 500:
                continue
            per_day = min(1 + a["interval"], a["held"]) / a["interval"]
            units = per_day * prod_days
            pr = self.forecast(a["product"], prod_days * 0.5,
                               extra=self.pipeline[a["product"]] * 0.7 + units * 0.5)
            wheat = market_price("WHEAT", self.inv["WHEAT"]) * (prod_days + a["first"])
            fert = prod_days * self.price["FERTILIZER"] * 0.5
            net = units * pr + fert - wheat
            if net > a["cost"] * P["animal_hurdle"] and net > bv:
                best, bv = name, net
        return best

    # ----------------------------------------------------------- unit actions
    def unit_actions(self, units, day, hour):
        tasks = self.build_tasks(day)
        shed_tiles = {(self.half - 1, self.half - 1), (self.half, self.half - 1),
                      (self.half - 1, self.half), (self.half, self.half)}
        acts = []
        claimed = set()
        plant_left = {}
        for c in set(self.plan):
            plant_left[c] = self.seeds.get(c, 0)
        unfed = [1 for _x, _y, t in self.animals if not t["fed_today"]]
        n_unfed = len(unfed)
        n_units = max(1, len(units))
        per_unit_wheat = int(math.ceil(n_unfed / n_units)) + P["wheat_per_unit"]

        for i, (ux, uy) in enumerate(units):
            inv = self.invs[i] if i < len(self.invs) else {}
            at_shed = (ux, uy) in shed_tiles

            if day >= LAST_DAY and inv:
                d = self.shed_dist(ux, uy)
                if hour >= P["drop_hour"] - d or hour >= 21 - d:
                    if at_shed:
                        acts.append(["DROP"])
                    else:
                        acts.append(self.step_toward(ux, uy, self.shed_goal(ux, uy)))
                    continue

            if at_shed:
                sup = self.shed_supply(inv, per_unit_wheat, n_unfed, day)
                if sup is not None:
                    acts.append(sup)
                    continue

            tgt = self.pick_task(i, ux, uy, inv, tasks, claimed, plant_left)
            if tgt is None:
                acts.append(self.idle(ux, uy, inv, day, at_shed))
                continue
            x, y, op, arg, _v = tgt
            claimed.add((x, y, op))
            if op == "PLANT":
                plant_left[arg] = plant_left.get(arg, 0) - 1
            if (ux, uy) == (x, y):
                acts.append([op] if arg is None else [op, arg])
            else:
                acts.append(self.step_toward(ux, uy, (x, y)))
        return acts

    def idle(self, ux, uy, inv, day, at_shed):
        if inv and (day >= LAST_DAY or sum(inv.values()) >= 12):
            if at_shed:
                return ["DROP"]
            return self.step_toward(ux, uy, self.shed_goal(ux, uy))
        return ["PASS"]

    def shed_dist(self, x, y):
        h = self.half
        return abs(x - min(max(x, h - 1), h)) + abs(y - min(max(y, h - 1), h))

    def shed_goal(self, x, y):
        h = self.half
        return (min(max(x, h - 1), h), min(max(y, h - 1), h))

    def shed_supply(self, inv, per_unit_wheat, n_unfed, day):
        """Standing at the shed: grab an animal that needs placing, or feed."""
        for a in ANIMALS:
            if self.shed.get(a, 0) > 0 and inv.get(a, 0) == 0:
                for _x, _y, kind in self.free_struct:
                    if kind == ANIMALS[a]["struct"]:
                        return ["PICKUP", a, 1]
        if n_unfed > 0 and inv.get("WHEAT", 0) < min(2, per_unit_wheat):
            have = self.shed.get("WHEAT", 0)
            if have > 0:
                return ["PICKUP", "WHEAT", int(min(have, per_unit_wheat))]
        if day < LAST_DAY and sum(inv.values()) >= 8:
            return ["DROP"]
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

    def pick_task(self, i, ux, uy, inv, tasks, claimed, plant_left):
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
            if op == "PLANT" and plant_left.get(arg, 0) <= 0:
                continue
            d = abs(x - ux) + abs(y - uy)
            s = v / (1.0 + d)
            if prev is not None and prev[0] == x and prev[1] == y and prev[2] == op:
                s *= 1.3
            if s > bs:
                best, bs = t, s
        self.targets[i] = (best[0], best[1], best[2]) if best else None
        return best

    # -------------------------------------------------------------- task list
    def build_tasks(self, day):
        tasks = []
        av = P["action_value"]
        left = self.day_left
        endgame = day >= LAST_DAY - 1

        for x, y, t in self.animals:
            a = ANIMALS[t["animal"]]
            pr = self.price[a["product"]]
            per_prod = min(1 + a["interval"], a["held"])
            if not t["fed_today"] and left >= 0:
                v = pr * 1.1
                if t["consecutive_unfed"] >= 1:
                    v += 500.0 + per_prod * pr * max(0, left) / a["interval"]
                tasks.append((x, y, "FEED", None, v))
            if not t["cared_today"] and left >= 1:
                tasks.append((x, y, "CARE", None, pr * 0.95))
            if t["fertilizer_available"]:
                tasks.append((x, y, "COLLECT_FERTILIZER", None, self.price["FERTILIZER"] * 0.9))
            yu = t["yield_units"]
            if yu > 0:
                waste = max(0, yu + per_prod - a["held"])
                v = waste * pr + yu * pr * 0.12
                if endgame:
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
                if t["consecutive_unwatered"] >= 1 and left >= 1:
                    v += self.plant_future(t) * pr * 0.75 + 25.0
                if v > 0:
                    tasks.append((x, y, "WATER", None, v))
            if t["yield_units"] > 0 and age >= cd["first"]:
                v = 0.0
                if not cd["ongoing"]:
                    if t["yield_units"] >= cd["maxy"] or age >= cd["myd"]:
                        v = t["yield_units"] * pr * 0.4 + 30.0
                    if age > cd["myd"]:
                        v = t["yield_units"] * pr
                else:
                    k = (day + 1) - t["planted_day"] - cd["first"]
                    waste = 0
                    if k >= 0 and k % cd["interval"] == 0:
                        waste = max(0, t["yield_units"] + (2 if fert else 1) - cd["maxy"])
                    v = waste * pr + t["yield_units"] * pr * 0.14
                if endgame:
                    v = t["yield_units"] * pr
                if v > 0:
                    tasks.append((x, y, "HARVEST", None, v))
            if (not fert) and left >= 2 and RECIPES[crop]["f"] > 0:
                gain = 0.0
                if cd["ongoing"]:
                    k = (day + 1) - t["planted_day"] - cd["first"]
                    if k >= -1:
                        gain = pr * min(2, cd["maxy"])
                elif age <= cd["myd"] - 1 and t["yield_units"] < cd["maxy"]:
                    gain = pr * min(2, cd["maxy"] - t["yield_units"])
                net = gain - self.price["FERTILIZER"] - av
                if net > 0:
                    tasks.append((x, y, "FERTILIZE", None, net))

        reserved = self.reserved
        plan = list(self.plan)
        for (x, y) in sorted(self.empty, key=lambda c: self.shed_dist(c[0], c[1])):
            if (x, y) in reserved:
                a = reserved[(x, y)]
                op = "BUILD_COOP" if ANIMALS[a]["struct"] == "COOP" else "BUILD_PASTURE"
                tasks.append((x, y, op, None, 300.0))
                continue
            if plan:
                c = plan.pop(0)
                if self.seeds.get(c, 0) > 0:
                    r = RECIPES[c]
                    res = self.crop_value(c, day, self.pipeline[c])
                    val = (res[0] if res else 5.0) * r["days"] * 0.6
                    tasks.append((x, y, "PLANT", c, max(val, 20.0)))

        for (x, y, kind) in self.free_struct:
            for a in ANIMALS:
                if ANIMALS[a]["struct"] == kind and (self.shed.get(a, 0) > 0 or self.carried(a) > 0):
                    tasks.append((x, y, "PLACE", a, 500.0))
                    break

        if left >= 2 and self.weeds:
            best = 6.0
            for c in CROPS:
                res = self.crop_value(c, day, self.pipeline[c])
                if res and res[0] > best:
                    best = res[0]
            dv = best * min(left, 8) * 0.8
            for (x, y) in self.weeds:
                tasks.append((x, y, "DIG", None, dv))
        return tasks

    # ------------------------------------------------------- animal reservations
    @property
    def reserved(self):
        if getattr(self, "_res_key", None) == (self.day, self.hour):
            return self._res
        pend = {}
        for a in ANIMALS:
            k = self.shed.get(a, 0) + self.carried(a)
            if k:
                pend[a] = k
        res = {}
        if pend:
            free = {}
            for _x, _y, kind in self.free_struct:
                free[kind] = free.get(kind, 0) + 1
            need = []
            for a, k in pend.items():
                st = ANIMALS[a]["struct"]
                use = min(k, free.get(st, 0))
                free[st] = free.get(st, 0) - use
                need.extend([a] * (k - use))
            if need:
                cand = sorted(self.empty, key=lambda c: self.shed_dist(c[0], c[1]))
                res = {cand[i]: need[i] for i in range(min(len(need), len(cand)))}
        self._res_key = (self.day, self.hour)
        self._res = res
        return res


_AGENT = Farmer()


def agent(obs):
    return _AGENT(obs)
