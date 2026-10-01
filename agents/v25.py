"""Kaggriculture agent v5.

Three ideas carry the agent:

1. Never leave a tile idle. Planting is a budget-aware greedy allocation -- each
   free tile goes to whichever crop has the best discounted $/tile-day *given
   the supply already committed*, while reserving enough cash that every
   remaining tile can still afford at least a wheat seed. Because the score uses
   a forecast price, the mix self-diversifies and pours tiles into whatever the
   town actually demands (the hinge curves on carrot/tomato/egg run to 10x base).

2. Units work a pie-slice zone. Rebalanced daily by workload, so a unit sweeps
   outward from the shed through its own wedge instead of crossing the board
   chasing whatever is momentarily most valuable.

3. Price forecasts include the OPPONENT's visible pipeline. Both farms sell into
   one shared pool, so a crop everyone is about to harvest is worth far less than
   its quoted price -- melon in particular collapses on the day both players cash
   out. Counting their tiles steers us into the markets they are ignoring.

4. Produce is carried to the shed and sold the same day when a load is worth it.
   The end-of-day drop is free but a day late, and in a contested market the
   player who sells first takes the high side of the curve.
"""

import math
from bisect import bisect_right

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
# Shops unlock every 3 days, drawn uniformly with replacement, capped at 8
# instances. Until one exists we still know its EXPECTED pull: this is the mean
# units-per-tick a random instance takes of each product.
EXP_PULL = {}
for _p in ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL", "FERTILIZER"]:
    EXP_PULL[_p] = 0.0
for _shop, _prods in SHOPS.items():
    _m = 2.0 if len(_prods) == 1 else 1.0
    for _p in _prods:
        EXP_PULL[_p] += _m / len(SHOPS)
SHOP_INTERVAL = 3
MAX_SHOPS = 8
TICKS_PER_DAY = 6

I0 = 10000
HINGE_GAIN = 8.0
LAND_PRICES = [1000, 2000, 4000]
LAST_DAY = 29
MIN_SEED = 10

RECIPES = {
    "WHEAT":      {"days": 4,  "u": 4, "uf": 6, "a": 6,  "f": 1},
    "CARROT":     {"days": 3,  "u": 3, "uf": 4, "a": 5,  "f": 1},
    "TOMATO":     {"days": 11, "u": 4, "uf": 8, "a": 13, "f": 2},
    "STRAWBERRY": {"days": 16, "u": 4, "uf": 8, "a": 14, "f": 2},
    "MELON":      {"days": 10, "u": 6, "uf": 6, "a": 10, "f": 0},
}

P = dict(
    max_hands=12,
    hire_budget_frac=0.30,
    hire_budget_min=200.0,
    work_per_unit=20.0,
    travel_mult=1.40,
    disc_rate=0.055,
    plant_min_score=3.0,
    plan_lookahead=10,
    plan_cap=64,
    cash_floor=60.0,
    land_last_day=23,
    animal_hurdle=1.25,
    animal_batch=4,
    animal_last_buy=22,
    animal_cash_guard=0.35,  # fraction of tile-fill cost to keep before buying animals
    animal_spend_frac=0.60,  # ceiling on cash committed to livestock in one turn
    wheat_spare=5,
    wheat_days=1.5,        # days of feed to hold in the shed per animal
    wheat_buy_max=45,
    feed_urgency=12.0,     # pushes the planner toward wheat when the herd is short
    fert_keep=6,
    sell_bias_glut=2.2,
    sell_bias_tight=2.0,
    sell_hold_gain=0.0,      # >0 restores the v3 "wait, the price is recovering" brake
    shed_target=88,          # raise past 100 to disable overflow-forced selling
    animals_before_seeds=0,
    feed_boost=0.0,
    drop_hour=12,
    stick=1.0,
    opp_weight=0.85,     # how much of the opponent's visible pipeline to price in
    opp_scan_every=6,
    drop_load=14,        # carried produce that justifies a trip to the shed
    drop_value=99999.0,  # $ of carried produce that justifies the same trip
    drop_reach=6,        # only detour to the shed from within this many steps
    last_day_slack=1,
    disc_hi=0.055,         # per-day discount while capital-constrained
    disc_window=8,         # days over which the high rate applies
    open_days=0,           # days treated as "the opening" (livestock before seeds)
    open_animal_budget=1400.0,
    fast_crop_frac=0.0,    # share of opening tiles reserved for <=4-day crops
    fast_until_day=6,
    tile_seed_est=45.0,
    unlock_trust=1.0,    # how much of the expected future shop demand to believe
    opp_mirror=0.7,      # assume a peer opponent commits at least this share of ours
    max_quads=3,         # NW+NE+SW; the SE quadrant loses in every published test
    hinge_meter=0.5,    # sell hinge goods below the drain rate while scarce
    tile_cap={"MELON": 12},
    mine_w=0.7,
    crop_horizon=0.6,
    animal_horizon=0.5,
    animal_cap={"GOOSE": 3},
    dist_pow=1.0,        # >1 makes units prefer nearby work over distant jackpots
    zone_reach=4,       # cap on how far outside its wedge a unit will wander
    hand_floor=[[3,4],[6,8],[10,11]],
    reach_override=600.0,   # task value that justifies leaving the wedge
    animal_price_floor=0.55,  # skip livestock whose product is already near the floor
    weed_mult=1.0,
    load_hour=3,         # morning window for loading feed at the shed
    refill_reach=3,      # only walk back for wheat from within this many steps
    herd_anchor=2.356,   # ~135 deg: pack the livestock into one quadrant
    herd_tight=3.0,
    fert_value=1.4,
    tight_sell_frac=0.0,   # fraction of stock to liquidate while capital-starved       # [(day, min_hands)] floor under the workload estimate
    open_herd={},
    feed_tiles_per_animal=0.9,   # wheat tiles grown per animal instead of buying feed
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


def _fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


class Farmer:
    def __init__(self):
        self.reset()

    def reset(self):
        self.targets = {}
        self.holds = {}
        self.hold_by = {}
        self.sold_today = {}
        self.zone_key = None
        self.zone_bounds = []
        self.day = -1

    # ------------------------------------------------------------ entry point
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
        self.c = (self.n - 1) / 2.0
        self.day = day = obs["day"]
        self.hour = hour = obs["hour"]
        self.day_left = LAST_DAY - day
        self.money = farm["money"]
        self.shed = priv["shed"]
        self.seeds = priv["seeds"]
        self.invs = priv["inventories"]
        self.inv = obs["market"]["inventory"]
        self.price = obs["market"]["prices"]
        self.shops = obs["town"].get("unlocked_shops", [])
        self.drain = self.drain_rates(self.shops)
        self.n_quads = len(farm["unlocked_quadrants"])
        if hour == 0:
            self.sold_today = {}

        self.scan()
        if hour % P["opp_scan_every"] == 0 or not hasattr(self, "opp_pipe"):
            self.opp_pipe = self.scan_opponent(obs["farms"][1 - me])
        self.cash_tight = self.money < self.cash_need()
        self.hands_target = self.target_hands()
        self.action_value = max(1.2, _fib(max(0, self.hands_target - 1)) / 24.0)
        self.plan = self.plan_crops(day)

        units = [list(farm["farmer"])] + [list(h) for h in farm["hands"]]
        orders = self.market_orders(hour, day)
        acts = self.unit_actions(units, day, hour)
        return {"farmer": acts[0], "hands": acts[1:], "market": orders[:10]}

    # ---------------------------------------------------------------- market
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

    def mean_drain(self, item, days_ahead):
        """Average daily town pull over the next `days_ahead` days.

        Using only today's shops badly under-prices everything early: on day 2 the
        town takes 1 unit a day, by day 24 it takes 13-30. Pricing a cow off the
        day-2 rate makes milk look worthless exactly when cows are the best buy on
        the board."""
        n = int(days_ahead)
        if n <= 0:
            return self.drain[item]
        base = 1.0 if item != "FERTILIZER" else 0.0
        known = self.drain[item] - base
        n_now = len(self.shops)
        tot = 0.0
        for t in range(self.day, self.day + n + 1):
            future = max(0, min(MAX_SHOPS, (t + 1) // SHOP_INTERVAL) - n_now)
            tot += known + base + future * TICKS_PER_DAY * EXP_PULL[item] * P["unlock_trust"]
        return tot / (n + 1)

    def forecast(self, item, days_ahead, extra=0.0):
        d = self.mean_drain(item, days_ahead)
        return market_price(item, self.inv[item] - d * days_ahead + extra)

    def discount(self, days):
        """Cash is worth far more while we are still buying land, hands and stock
        than it is once the farm is built, so discount hard over the opening window
        and gently after it."""
        lo = P["disc_rate"]
        hi = P["disc_hi"] if self.cash_tight else lo
        w = min(days, P["disc_window"])
        return 1.0 / ((1.0 + hi) ** w * (1.0 + lo) ** max(0, days - w))

    def carried(self, p):
        return sum(iv.get(p, 0) for iv in self.invs)

    # ------------------------------------------------------------------ scan
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
        self.n_unfed = 0
        self.critical_unfed = 0
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
                    if not t["fed_today"]:
                        self.n_unfed += 1
                        if t["consecutive_unfed"] >= 1:
                            self.critical_unfed += 1
                    a = ANIMALS[t["animal"]]
                    rem = max(0, self.day_left - 1)
                    per = min(1 + a["interval"], a["held"]) / a["interval"]
                    self.pipeline[a["product"]] += t["yield_units"] + rem * per
                    self.pipeline["FERTILIZER"] += rem
                else:
                    self.free_struct.append((x, y, t["kind"]))
        for p in PRODUCTS:
            self.pipeline[p] += self.shed.get(p, 0) + self.carried(p)
        self.reserved = self.reserve_tiles()

    def scan_opponent(self, farm):
        """What the other farm is about to dump into the shared market.

        Their shed is hidden, but their tiles are not -- and a crop we can both see
        maturing is worth far less than its quoted price."""
        pipe = {p: 0.0 for p in PRODUCTS}
        for row in farm["tiles"]:
            for t in row:
                if not isinstance(t, dict):
                    continue
                if t.get("kind") == "PLANT":
                    pipe[t["crop"]] += self.plant_future(t)
                elif "animal" in t:
                    a = ANIMALS[t["animal"]]
                    rem = max(0, self.day_left - 1)
                    per = min(1 + a["interval"], a["held"]) / a["interval"]
                    pipe[a["product"]] += t["yield_units"] + rem * per
                    pipe["FERTILIZER"] += rem
        return pipe

    def supply(self, item, horizon=None):
        """Committed supply that will reach the shared market within `horizon` days.

        Scaling matters: a pipeline is a season's worth of production, but a price
        forecast looks only a few days out. Charging the opponent's whole remaining
        herd against a 4-day drain window prices milk at the floor when the town
        will in fact absorb every drop of it."""
        if horizon is None or self.day_left <= 0:
            scale = 1.0
        else:
            scale = min(1.0, float(horizon) / max(1.0, self.day_left))
        mine = self.pipeline[item] * scale * P["mine_w"]
        theirs = max(self.opp_pipe[item] * scale, mine * P["opp_mirror"])
        return mine + theirs * P["opp_weight"]

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

    # ------------------------------------------------------------ crop plan
    def crop_value(self, crop, day, extra):
        r = RECIPES[crop]
        if day + r["days"] > LAST_DAY:
            return None
        fert = self.fert_supply() > 0 and r["uf"] > r["u"]
        units = r["uf"] if fert else r["u"]
        acts = r["a"] + (r["f"] if fert else 0)
        if crop == "WHEAT":
            # wheat we grow is wheat we do not have to buy, and buying walks the
            # steep scarcity side of the curve up against us
            extra -= self.feed_shortfall() * P["feed_boost"]
            if self.n_animals and self.pipeline["WHEAT"] < self.n_animals * 2:
                extra -= self.n_animals * P["feed_urgency"]
        h = r["days"] * P["crop_horizon"]
        pr = self.forecast(crop, h, extra=extra)
        gross = units * pr * self.discount(r["days"])
        cost = CROPS[crop]["seed"] + acts * self.action_value
        if fert:
            cost += r["f"] * self.price["FERTILIZER"] * 0.5
        return (gross - cost) / r["days"], units

    def feed_shortfall(self):
        """Wheat we will have to buy from the market if we grow no more of it."""
        need = (self.n_animals + self.pending_animals()) * max(0, self.day_left)
        return max(0.0, need - self.pipeline["WHEAT"])

    def fert_supply(self):
        return self.shed.get("FERTILIZER", 0) + self.carried("FERTILIZER") + self.n_animals

    def plan_crops(self, day):
        """Budget-aware greedy: fill every tile, best crop each can still afford."""
        look = 0 if self.cash_tight else P["plan_lookahead"]
        slots = len(self.empty) - len(self.reserved) + look
        slots = max(0, min(slots, P["plan_cap"]))
        if slots == 0:
            return []
        cash = self.money - P["cash_floor"]
        for c, k in self.seeds.items():
            cash += k * CROPS[c]["seed"]      # seeds on hand are already paid for
        extra = {c: self.supply(c, RECIPES[c]["days"] * P["crop_horizon"]) for c in CROPS}
        # In the opening, part of the field has to be crops that pay before the
        # long ones do -- otherwise there is no cash for land or livestock and the
        # whole compounding chain stalls out.
        fast_quota = 0
        if day <= P["fast_until_day"]:
            fast_quota = int(slots * P["fast_crop_frac"])
        planted = {}
        for _x, _y, t in self.plants:
            planted[t["crop"]] = planted.get(t["crop"], 0) + 1
        taken = {}
        out = []
        for i in range(slots):
            force_fast = (slots - i) <= fast_quota
            rem = slots - i - 1
            afford = cash - rem * MIN_SEED
            best, bs, bu, bc = None, P["plant_min_score"], 0, 0
            for c in CROPS:
                sc = CROPS[c]["seed"]
                if sc > afford:
                    continue
                if force_fast and RECIPES[c]["days"] > 4:
                    continue
                cap = P["tile_cap"].get(c)
                if cap is not None and taken.get(c, 0) + planted.get(c, 0) >= cap:
                    continue
                res = self.crop_value(c, day, extra[c])
                if res is None:
                    continue
                s, u = res
                if s > bs:
                    best, bs, bu, bc = c, s, u, sc
            if best is None:
                break
            out.append(best)
            taken[best] = taken.get(best, 0) + 1
            # every tile we commit to a crop also makes it likelier the opponent
            # piles into the same obvious pick, so charge the mirror here too
            extra[best] += bu * (1.0 + P["opp_mirror"] * P["opp_weight"])
            cash -= bc
        return out

    def cash_need(self):
        """What we would spend today if cash were no object: fill the tiles, take the
        next quadrant, and put livestock on the board."""
        # deliberately plan-free: the crop plan depends on the discount, which
        # depends on this
        need = min(len(self.empty), 40) * P["tile_seed_est"]
        n_extra = self.n_quads - 1
        if n_extra < P["max_quads"] - 1 and self.day <= P["land_last_day"]:
            need += LAND_PRICES[n_extra]
        if self.day <= P["animal_last_buy"]:
            need += 800.0
        return need

    def fill_cost(self):
        cost = 0
        need = {}
        for c in self.plan:
            need[c] = need.get(c, 0) + 1
        for c, k in need.items():
            cost += max(0, k - self.seeds.get(c, 0)) * CROPS[c]["seed"]
        return cost

    # ----------------------------------------------------------- market orders
    def market_orders(self, hour, day):
        orders = []
        money = self.money
        if hour <= 1:
            have = self.farm["hires_today"]
            todo = max(0, self.hands_target - have)
            k = min(todo, 10)
            for _ in range(k):
                orders.append(["HIRE"])
            money -= self.hire_cost(have, k)
            if len(orders) >= 10:
                return orders

        orders.extend(self.sell_orders(day))
        buys, money = self.buy_orders(day, money)
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
        work = len(self.plants) * 1.35 + self.n_animals * 3.7
        work += min(len(self.empty), 40) * 1.8 + len(self.weeds) * 1.0
        work *= P["travel_mult"]
        want = int(math.ceil(work / P["work_per_unit"])) - 1
        floor = 0
        for d, n in P["hand_floor"]:
            if self.day >= d:
                floor = n
        want = max(want, floor)
        want = max(0, min(P["max_hands"], want))
        budget = max(P["hire_budget_min"], self.money * P["hire_budget_frac"])
        while want > 0 and self.hire_cost(0, want) > budget:
            want -= 1
        return want

    def wheat_reserve(self):
        return int(self.n_animals * P["wheat_days"]) + 4

    def sell_orders(self, day):
        """Pace each product so stock+pipeline clears by day 29, front-loaded when we
        are outproducing town demand (price will fall) and held back when we are not
        (price will rise). Overselling is safe: the engine stops the order when the
        shed runs dry, which is exactly what we want for goods dropped this turn."""
        out = []
        shed_total = sum(self.shed.values())
        carried_total = sum(sum(iv.values()) for iv in self.invs)
        horizon = max(1, self.day_left + 1)
        # everything a unit is holding lands in the shed tonight; overflow is binned
        overflow = shed_total + carried_total - P["shed_target"]

        if day >= LAST_DAY - 1:
            return [["SELL", p, 100] for p in PRODUCTS]
        for p in PRODUCTS:
            stock = self.shed.get(p, 0)
            if stock <= 0:
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
            if self.cash_tight:
                # while we are still short of land and livestock, capital today is
                # worth far more than a better price later -- pacing sales at
                # stock/horizon starves the opening of the money that compounds
                q = max(q, stock * P["tight_sell_frac"])
            q *= P["sell_bias_glut"] if total > self.drain[p] * horizon else P["sell_bias_tight"]
            if MARKET_PARAMS[p]["bf"] == "hinge" and self.inv[p] < I0:
                # scarcity side of a hinge curve: every unit withheld is worth more
                # tomorrow than today, so meter these harder than the drain rate
                q *= P["hinge_meter"]
            if P["sell_hold_gain"] > 0:
                cur = self.price[p]
                nxt = market_price(p, self.inv[p] - self.drain[p])
                if cur > 0 and (nxt - cur) / cur > P["sell_hold_gain"] and shed_total < 68:
                    q = stock / horizon
            q = int(math.ceil(q)) - already
            if overflow > 0:
                q = max(q, min(stock, int(math.ceil(overflow * stock / max(1, shed_total)))))
            q = min(q, stock)
            if q > 0:
                out.append(["SELL", p, int(q)])
                self.sold_today[p] = already + int(q)
        return out

    def buy_orders(self, day, money):
        out = []
        fill = self.fill_cost()

        # 1. feed -- a starved animal is a $400-500 write-off
        if (self.n_animals or self.pending_animals()) and day < LAST_DAY - 1:
            need = self.wheat_reserve() + P["wheat_spare"] * 2
            have = self.shed.get("WHEAT", 0) + self.carried("WHEAT")
            room = 100 - sum(self.shed.values())
            if have < need and room > 0:
                wp = market_price("WHEAT", self.inv["WHEAT"] - 1)
                want = min(need - have, P["wheat_buy_max"], room)
                starving = have < self.n_animals
                if money > wp * want + (0 if starving else 100):
                    # slot 0: market orders are a contested priority queue and a
                    # starved animal costs far more than the price tick
                    out.insert(0, ["BUY_PRODUCT", "WHEAT", int(want)])
                    money -= wp * want

        def buy_animals(money):
            if day <= P["open_days"] and P["open_herd"]:
                for name in P["open_herd"]:
                    have = sum(1 for _x, _y, t in self.animals if t["animal"] == name)
                    have += self.shed.get(name, 0) + self.carried(name)
                    k = P["open_herd"][name] - have
                    c = ANIMALS[name]["cost"]
                    k = min(k, int(money // c))
                    if k > 0:
                        out.append(["BUY_ANIMAL", name, k])
                        money -= c * k
                return money
            if self.pending_animals() >= P["animal_batch"] or day > P["animal_last_buy"]:
                return money
            room = len(self.free_struct) + len(self.empty) - len(self.reserved)
            if room <= 0:
                return money
            cap = min(money * P["animal_spend_frac"], money - fill * P["animal_cash_guard"])
            if day <= P["open_days"]:
                cap = min(money, P["open_animal_budget"])
            pick = self.best_animal(cap)
            if pick:
                c = ANIMALS[pick]["cost"]
                k = 1
                while k < P["animal_batch"] and c * (k + 1) <= cap:
                    k += 1
                out.append(["BUY_ANIMAL", pick, k])
                money -= c * k
            return money

        def buy_seeds(money):
            need = {}
            for c in self.plan:
                need[c] = need.get(c, 0) + 1
            budget = money - P["cash_floor"]
            for c in sorted(need, key=lambda c: -CROPS[c]["seed"]):
                k = need[c] - self.seeds.get(c, 0)
                if k <= 0:
                    continue
                sc = CROPS[c]["seed"]
                k = min(k, int(max(0, budget) // sc))
                if k > 0:
                    out.append(["BUY_SEED", c, k])
                    budget -= sc * k
                    money -= sc * k
            return money

        # Livestock bought in the opening pays from day 6-8 and funds everything
        # after it; past the opening, idle tiles compound worse, so seeds go first.
        if P["animals_before_seeds"] or day <= P["open_days"]:
            money = buy_seeds(buy_animals(money))
        else:
            money = buy_animals(buy_seeds(money))

        # land
        n_extra = self.n_quads - 1
        if n_extra < P["max_quads"] - 1 and day <= P["land_last_day"]:
            cost = LAND_PRICES[n_extra]
            if money >= cost + 25 * MIN_SEED and self.land_pays(cost, day):
                out.append(["BUY_LAND"])
                money -= cost
        return out, money

    def land_pays(self, cost, day):
        if self.day_left < 4:
            return False
        best = 0.0
        for c in CROPS:
            res = self.crop_value(c, day, self.supply(c, RECIPES[c]["days"] * P["crop_horizon"]))
            if res and res[0] > best:
                best = res[0]
        return 25 * best * min(self.day_left, 18) > cost * 1.15

    def pending_animals(self):
        return sum(self.shed.get(a, 0) + self.carried(a) for a in ANIMALS)

    def best_animal(self, money):
        best, bv = None, 0.0
        for name, a in ANIMALS.items():
            prod_days = self.day_left - a["first"]
            if prod_days < 3 or money < a["cost"]:
                continue
            cap = P["animal_cap"].get(name)
            if cap is not None:
                have = sum(1 for _x, _y, t in self.animals if t["animal"] == name)
                if have + self.shed.get(name, 0) + self.carried(name) >= cap:
                    continue
            per_day = min(1 + a["interval"], a["held"]) / a["interval"]
            units = per_day * prod_days
            h = prod_days * P["animal_horizon"]
            pr = self.forecast(a["product"], h,
                               extra=self.supply(a["product"], h) + units * 0.5 * h / max(1, prod_days))
            wheat = market_price("WHEAT", self.inv["WHEAT"]) * (prod_days + a["first"])
            fert = prod_days * self.price["FERTILIZER"] * 0.5
            if pr < MARKET_PARAMS[a["product"]]["base"] * P["animal_price_floor"]:
                continue
            net = units * pr + fert - wheat
            if net > a["cost"] * P["animal_hurdle"] and net > bv:
                best, bv = name, net
        return best

    def reserve_tiles(self):
        pend = {}
        for a in ANIMALS:
            k = self.shed.get(a, 0) + self.carried(a)
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
            use = min(k, free.get(st, 0))
            free[st] = free.get(st, 0) - use
            need.extend([a] * (k - use))
        if not need:
            return {}
        cand = sorted(self.empty, key=self.herd_rank)
        return {cand[i]: need[i] for i in range(min(len(need), len(cand)))}

    # ------------------------------------------------------------------ zones
    def compute_zones(self, k):
        """Pie slices around the shed, balanced by today's workload."""
        items = []
        for x, y, t in self.plants:
            items.append((math.atan2(y - self.c, x - self.c), 1.4))
        for x, y, t in self.animals:
            items.append((math.atan2(y - self.c, x - self.c), 3.7))
        for (x, y) in self.empty:
            items.append((math.atan2(y - self.c, x - self.c), 1.6))
        for (x, y) in self.weeds:
            items.append((math.atan2(y - self.c, x - self.c), 1.0))
        if not items or k <= 1:
            self.zone_bounds = []
            return
        items.sort()
        total = sum(w for _a, w in items)
        per = total / k
        bounds = []
        acc = 0.0
        nxt = per
        for ang, w in items:
            acc += w
            while len(bounds) < k - 1 and acc >= nxt:
                bounds.append(ang)
                nxt += per
        while len(bounds) < k - 1:
            bounds.append(items[-1][0])
        self.zone_bounds = bounds

    def zone_of(self, x, y):
        if not self.zone_bounds:
            return 0
        return bisect_right(self.zone_bounds, math.atan2(y - self.c, x - self.c))

    # ------------------------------------------------------------ unit actions
    def unit_actions(self, units, day, hour):
        k = len(units)
        if self.zone_key != (day, k):
            self.compute_zones(k)
            self.zone_key = (day, k)
            self.holds = {}
            self.hold_by = {}

        tasks = self.build_tasks(day)
        self.task_zone = [self.zone_of(t[0], t[1]) for t in tasks]
        shed_tiles = {(self.half - 1, self.half - 1), (self.half, self.half - 1),
                      (self.half - 1, self.half), (self.half, self.half)}
        acts = []
        claimed = set()
        self.n_units = k
        plant_left = {c: self.seeds.get(c, 0) for c in set(self.plan)}
        overflow = (sum(self.shed.values())
                    + sum(sum(iv.values()) for iv in self.invs) - P["shed_target"])

        # how much feed each unit's own wedge will need today
        zone_feed = {}
        for x, y, t in self.animals:
            if not t["fed_today"]:
                z = self.zone_of(x, y)
                zone_feed[z] = zone_feed.get(z, 0) + 1
        zone_fert = {}
        for x, y, t in self.plants:
            if t["fertilized_until_day"] < day and RECIPES[t["crop"]]["f"] > 0:
                z = self.zone_of(x, y)
                zone_fert[z] = zone_fert.get(z, 0) + 1

        for i, (ux, uy) in enumerate(units):
            inv = self.invs[i] if i < len(self.invs) else {}
            at_shed = (ux, uy) in shed_tiles

            if day >= LAST_DAY and inv:
                d = self.shed_dist(ux, uy)
                if hour >= min(P["drop_hour"], 21 - d):
                    acts.append(["DROP"] if at_shed
                                else self.step_toward(ux, uy, self.shed_goal(ux, uy)))
                    continue

            # a full load is worth walking in for: it sells today instead of
            # tomorrow, and it keeps the evening drop under the 100-item shed cap
            haul = sum(v for k, v in inv.items()
                       if k in PRODUCTS and k not in ("WHEAT", "FERTILIZER"))
            # Value, not count, decides whether to walk in: a unit holding 12 melons
            # is carrying ~$3k and every turn it waits is a turn the opponent spends
            # selling the same melons into the same curve.
            haul_value = sum(self.price.get(k, 0) * v for k, v in inv.items()
                             if k in PRODUCTS and k not in ("WHEAT", "FERTILIZER"))
            if (haul >= P["drop_load"] or haul_value >= P["drop_value"]
                    or (overflow > 0 and haul >= 5)):
                if at_shed:
                    acts.append(["DROP"])
                    continue
                if self.shed_dist(ux, uy) <= P["drop_reach"]:
                    acts.append(self.step_toward(ux, uy, self.shed_goal(ux, uy)))
                    continue

            if at_shed:
                sup = self.shed_supply(i, inv, zone_feed, zone_fert, day)
                if sup is not None:
                    acts.append(sup)
                    continue
            elif (inv.get("WHEAT", 0) <= 0 and self.shed.get("WHEAT", 0) > 0
                  and zone_feed.get(i, 0) > 0 and day < LAST_DAY
                  and self.shed_dist(ux, uy) <= P["refill_reach"]):
                acts.append(self.step_toward(ux, uy, self.shed_goal(ux, uy)))
                continue

            tgt = self.pick_task(i, ux, uy, inv, tasks, claimed, plant_left, day, hour)
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
        if inv and day >= LAST_DAY:
            return ["DROP"] if at_shed else self.step_toward(ux, uy, self.shed_goal(ux, uy))
        return ["PASS"]

    def herd_rank(self, c):
        """Near the shed and bunched in one direction, so feed runs stay short and
        only a couple of wedges ever contain an animal."""
        x, y = c
        ang = math.atan2(y - self.c, x - self.c)
        d = ang - P["herd_anchor"]
        while d > math.pi:
            d -= 2 * math.pi
        while d < -math.pi:
            d += 2 * math.pi
        return self.shed_dist(x, y) + P["herd_tight"] * abs(d)

    def shed_dist(self, x, y):
        h = self.half
        return abs(x - min(max(x, h - 1), h)) + abs(y - min(max(y, h - 1), h))

    def shed_goal(self, x, y):
        h = self.half
        return (min(max(x, h - 1), h), min(max(y, h - 1), h))

    def shed_supply(self, i, inv, zone_feed, zone_fert, day):
        """Top up at the shed. Never DROP here: end-of-day deposits everything for
        free, and a DROP/PICKUP pair would just cycle the same wheat back and forth."""
        for a in ANIMALS:
            if self.day_left < ANIMALS[a]["first"] + 2:
                continue
            if self.shed.get(a, 0) > 0 and inv.get(a, 0) == 0:
                for _x, _y, kind in self.free_struct:
                    if kind == ANIMALS[a]["struct"]:
                        return ["PICKUP", a, 1]
        want = zone_feed.get(i, 0)
        if self.hour <= P["load_hour"] and self.n_unfed:
            want = max(want, int(math.ceil(self.n_unfed / max(1, self.n_units))))
        if want and inv.get("WHEAT", 0) < want:
            have = self.shed.get("WHEAT", 0)
            if have > 0:
                return ["PICKUP", "WHEAT", int(min(have, want + P["wheat_spare"]))]
        if (zone_fert.get(i, 0) and inv.get("FERTILIZER", 0) == 0
                and self.shed.get("FERTILIZER", 0) > 2):
            return ["PICKUP", "FERTILIZER",
                    int(min(self.shed["FERTILIZER"] - 2, zone_fert[i], 4))]
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

    def pick_task(self, i, ux, uy, inv, tasks, claimed, plant_left, day=0, hour=0):
        held = self.holds.get(i)
        """Best value-per-turn inside this unit's wedge; fall back to the board."""
        prev = self.targets.get(i)
        best = bestg = None
        bs = bsg = 0.0
        tz = self.task_zone
        for ti, t in enumerate(tasks):
            x, y, op, arg, v = t
            key = (x, y, op)
            if key in claimed:
                continue
            owner = self.hold_by.get(key)
            if owner is not None and owner != i:
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
            if d > P["zone_reach"] and tz[ti] != i and v < P["reach_override"]:
                continue
            if day >= LAST_DAY and op == "HARVEST":
                # anything harvested too late to carry back to the shed is binned
                if hour + d + 1 + self.shed_dist(x, y) > 21 - P["last_day_slack"]:
                    continue
            s = v / (1.0 + d) ** P["dist_pow"]
            if held is not None and held == key:
                s *= P["stick"]
            if s > bsg:
                bestg, bsg = t, s
            if tz[ti] == i and s > bs:
                best, bs = t, s
        pick = best if best is not None else bestg
        if held is not None and self.hold_by.get(held) == i:
            del self.hold_by[held]
        if pick is not None:
            key = (pick[0], pick[1], pick[2])
            self.holds[i] = key
            self.hold_by[key] = i
        else:
            self.holds.pop(i, None)
        return pick

    # --------------------------------------------------------------- task list
    def build_tasks(self, day):
        tasks = []
        av = self.action_value
        left = self.day_left
        endgame = day >= LAST_DAY - 1

        for x, y, t in self.animals:
            a = ANIMALS[t["animal"]]
            pr = self.price[a["product"]]
            per_prod = min(1 + a["interval"], a["held"])
            if not t["fed_today"] and left >= 0:
                v = pr * 1.1
                if t["consecutive_unfed"] >= 1:
                    v += 600.0 + per_prod * pr * max(0, left) / a["interval"]
                tasks.append((x, y, "FEED", None, v))
            if not t["cared_today"] and left >= 1:
                tasks.append((x, y, "CARE", None, pr * 0.95))
            if t["fertilizer_available"]:
                tasks.append((x, y, "COLLECT_FERTILIZER", None,
                              self.price["FERTILIZER"] * P["fert_value"]))
            yu = t["yield_units"]
            if yu > 0:
                waste = max(0, yu + per_prod - a["held"])
                v = yu * pr if endgame else waste * pr + yu * pr * 0.12
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
                        v = t["yield_units"] * pr * 0.45 + 30.0
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

        plan = list(self.plan)
        for (x, y) in sorted(self.empty, key=lambda c: self.shed_dist(c[0], c[1])):
            if (x, y) in self.reserved:
                a = self.reserved[(x, y)]
                op = "BUILD_COOP" if ANIMALS[a]["struct"] == "COOP" else "BUILD_PASTURE"
                tasks.append((x, y, op, None, 320.0))
                continue
            if plan:
                c = plan.pop(0)
                if self.seeds.get(c, 0) > 0:
                    res = self.crop_value(c, day, self.supply(c, RECIPES[c]["days"] * P["crop_horizon"]))
                    val = (res[0] if res else 5.0) * RECIPES[c]["days"] * 0.55
                    tasks.append((x, y, "PLANT", c, max(val, 25.0)))

        for (x, y, kind) in self.free_struct:
            for a in ANIMALS:
                if ANIMALS[a]["struct"] == kind and (self.shed.get(a, 0) > 0 or self.carried(a) > 0):
                    tasks.append((x, y, "PLACE", a, 520.0))
                    break

        if left >= 2 and self.weeds:
            best = 6.0
            for c in CROPS:
                res = self.crop_value(c, day, self.supply(c, RECIPES[c]["days"] * P["crop_horizon"]))
                if res and res[0] > best:
                    best = res[0]
            dv = best * min(left, 8) * 0.75 * P["weed_mult"]
            for (x, y) in self.weeds:
                tasks.append((x, y, "DIG", None, dv))
        return tasks


_AGENT = Farmer()


def agent(obs):
    return _AGENT(obs)
