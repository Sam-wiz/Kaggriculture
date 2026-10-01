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
    reach_override=50.0,   # task value that justifies leaving the wedge
    animal_price_floor=0.55,  # skip livestock whose product is already near the floor
    weed_mult=1.0,
    load_hour=3,         # morning window for loading feed at the shed
    refill_reach=3,      # only walk back for wheat from within this many steps
    herd_anchor=2.356,   # ~135 deg: pack the livestock into one quadrant
    herd_tight=0.0,
    fert_value=1.4,
    tight_sell_frac=0.0,   # fraction of stock to liquidate while capital-starved       # [(day, min_hands)] floor under the workload estimate
    open_herd={},
    feed_tiles_per_animal=0.9,   # wheat tiles grown per animal instead of buying feed

    # ---- adaptive rebuild knobs (adaptive/a1.py) -------------------------
    # Stage 1: feed logistics. v22 spent 722 unit-actions on PICKUP for only
    # 207 FEEDs because the shed was chronically empty of wheat, so every hand
    # shuttled 1 unit at a time.
    a_feed=1,              # 0 = keep v22 behaviour
    feed_days=1.5,         # days of feed held in the shed per animal
    feed_buy_max=70,       # per-turn market wheat purchase cap
    feed_carry=1.5,        # wheat carried per unfed animal in the unit's zone
    feed_carry_min=3,      # minimum useful pickup -- avoid 1-unit shuttle runs
    feed_val=0.55,          # FEED value as a multiple of the animal's daily value
    feed_panic=0.3,        # extra weight when the animal is one day from escaping
    care_val=0.3,          # CARE value as a multiple of one product unit
    collect_val=0.3,       # COLLECT_FERTILIZER value multiplier on fert unit value

    # Stage 2: fertilizer as an input, not a by-product. One unit on a
    # strawberry buys 2 extra units at ~$180; v22 sold it at $55.
    a_fert=1,
    fert_use_disc=0.55,    # haircut on the theoretical bonus (watering may be missed)
    fert_keep_mult=1.0,    # keep this many units per plant that can still use one
    fert_keep_max=40,
    fert_carry=4,          # units a hand loads per trip

    # Stage 3: route by TILE, not by task. An animal tile is FEED + CARE +
    # COLLECT_FERTILIZER + HARVEST for a single walk, so scoring those four
    # separately makes the trip look four times more expensive than it is.
    # Measured: v22 burns 1.77 moves per productive action, the tape 1.00.
    a_bundle=1,
    bundle_act_cost=1.0,   # turns charged per action once the unit has arrived
    bundle_decay=1.0,      # weight on the 2nd..nth task in a bundle

    # Stage 4: price a unit-action at its SHADOW value, not the hand's wage.
    # Tile-days are free once the land is bought; unit-actions are not, and the
    # crop planner was charging ~$5 per action against a wage of fib(n)/24.
    # A carrot is 5 actions for 3 units (~$150); a strawberry is 14 for 8
    # (~$1200). At the wage both look fine, so v22 planted 159 carrots and
    # starved the herd of the care actions that are worth $200 each.
    act_shadow=0.0,
    water_prod_val=0.35,  # parity nudge: water ongoing crops on their production day

    # Stage 5: a LABOUR budget on the standing crop. Tile-days are free once the
    # land is bought but unit-actions are not, and an over-planted farm services
    # everything at 60% instead of servicing less at 100%. Measured: h_over gets
    # the fertilizer bonus on 98% of its strawberry production events off 33
    # plants; a1 got 51% off 47.
    a_labour=1,
    labour_travel=2.3,     # turns spent per productive action, including the walk
    labour_animal=3.4,     # actions per animal per day (feed+care+collect+harvest)
    labour_slack=1.0,      # scale on the budget; <1 keeps a reserve

    # ---- Crop Dusta blueprint directives (measured one at a time) ---------
    land_days=[],          # e.g. [5,8]: force BUY_LAND on these days
    buy_feed=0.0,          # >0: buy this many days of feed and stop growing wheat
    wheat_tile_cap=0,      # 0 = no cap on standing wheat tiles

    # Stage 6: rank crops by dollars per ACTION as well as per tile-day.
    # Ranking purely per tile-day favours 3-day carrot over 11-day tomato even
    # when tomato is $300 and carrot is $50, because tiles are not the scarce
    # resource once the land is bought -- hands are.
    score_act_pow=0.0,     # 0 = pure $/tile-day (v22); 1 = fully per-action
    score_act_ref=8.0,

    # Stage 7: FERTILIZER has no town demand at all -- no shop buys it and it is
    # excluded from TOWN_CENTER_PRODUCTS -- so its inventory only ever rises and
    # its price only ever falls (median $1 by day 29 in an h_over mirror). The
    # whole pot is ~$25k and it goes to whoever sells first. Keep what the crop
    # bonus needs, dump the rest immediately.
    fert_dump=0,

    # Stage 8: book shed stock out as it is assigned within a turn.
    a_shedalloc=0,

    # Stage 9: prize-collecting routing (linear move toll) instead of a rate.
    a_route=1,
    move_cost=60.0,
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
        self.tile_owner = {}
        self.by_tile = {}
        self.shed_left = {}
        self.zone_by_tile = {}
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
        self.action_value = max(1.2, _fib(max(0, self.hands_target - 1)) / 24.0,
                                P["act_shadow"])
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
        self._fuv = None
        self.n_fert_need = None
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
        score = (gross - cost) / r["days"]
        if P["score_act_pow"] and score > 0:
            score *= (P["score_act_ref"] / max(1.0, acts)) ** P["score_act_pow"]
        return score, units

    def feed_shortfall(self):
        """Wheat we will have to buy from the market if we grow no more of it."""
        need = (self.n_animals + self.pending_animals()) * max(0, self.day_left)
        return max(0.0, need - self.pipeline["WHEAT"])

    def fert_supply(self):
        return self.shed.get("FERTILIZER", 0) + self.carried("FERTILIZER") + self.n_animals

    def crop_daily_actions(self, crop):
        r = RECIPES[crop]
        return (r["a"] + r["f"]) / float(r["days"])

    def labour_room(self):
        """How many more plant-days per day the crew can actually service.

        A tile costs nothing to hold, but every plant on it demands watering,
        fertilizing and harvesting out of a fixed pool of unit-actions. Planting
        past this line does not add output, it just dilutes coverage across the
        whole farm -- which is how a strawberry that should yield 8 units yields
        3.5."""
        units = max(1, self.hands_target + 1)
        slots = units * 24.0 / max(1.0, P["labour_travel"])
        load = (self.n_animals + self.pending_animals()) * P["labour_animal"]
        for _x, _y, t in self.plants:
            load += self.crop_daily_actions(t["crop"])
        return slots * P["labour_slack"] - load

    def plan_crops(self, day):
        """Budget-aware greedy: fill every tile, best crop each can still afford."""
        look = 0 if self.cash_tight else P["plan_lookahead"]
        slots = len(self.empty) - len(self.reserved) + look
        slots = max(0, min(slots, P["plan_cap"]))
        room = self.labour_room() if P["a_labour"] else 1e9
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
                if self.crop_daily_actions(c) > room:
                    continue
                if force_fast and RECIPES[c]["days"] > 4:
                    continue
                cap = P["tile_cap"].get(c)
                if c == "WHEAT" and P["wheat_tile_cap"]:
                    cap = P["wheat_tile_cap"]
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
            room -= self.crop_daily_actions(best)
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
        if P["buy_feed"] > 0:
            herd = self.n_animals + self.pending_animals()
            days = min(P["buy_feed"], max(0, self.day_left) + 1)
            return int(herd * days) + 4
        if P["a_feed"]:
            # hold enough feed that a hand can load a full round instead of
            # shuttling single units, but never more than the herd can eat
            herd = self.n_animals + self.pending_animals()
            days = min(P["feed_days"], max(0, self.day_left) + 1)
            return int(herd * days) + 4
        return int(self.n_animals * P["wheat_days"]) + 4

    def animal_day_value(self, t):
        """What one more day of this animal alive is worth: its share of a
        production plus the fertilizer it drops every single day. Pricing FEED
        off the raw product price alone makes a cow worthless the moment milk
        gluts -- but it is still a $60/day fertilizer machine."""
        a = ANIMALS[t["animal"]]
        pr = max(self.price[a["product"]], self.forecast(a["product"], 3.0))
        per_day = min(1 + a["interval"], a["held"]) / a["interval"]
        return pr * per_day + self.price["FERTILIZER"] * P["fert_value"]

    def fert_prod_gain(self, t):
        """Extra units one FERTILIZE buys on this plant. Fertilizer is active for
        day..day+2 inclusive, so it covers three watering days on a one-time crop
        and 3//interval production days on an ongoing one."""
        crop = t["crop"]
        cd = CROPS[crop]
        if RECIPES[crop]["f"] <= 0:
            return 0.0
        day = self.day
        age = day - t["planted_day"]
        if cd["ongoing"]:
            # FERTILIZE sets fertilized_until_day = day+2, and the engine checks
            # `fertilized_until_day >= current_day` at end of day, so the window is
            # exactly {day, day+1, day+2}. Count the production days that actually
            # fall inside it: 3 for tomato (interval 1) and 2 for strawberry when
            # applied on a production day -- not 3//interval == 1.
            covered = 0
            end = day + max(0, self.day_left)
            for dd in (day, day + 1, day + 2):
                if dd > end:
                    break
                kk = (dd + 1) - t["planted_day"] - cd["first"]
                if kk < 0 or kk % cd["interval"]:
                    continue
                if kk // cd["interval"] + 1 > cd["maxy"]:
                    continue
                covered += 1
            return float(covered)
        # one-time: each watering inside the window yields +2 instead of +1
        ws = (cd["myd"] + 1) // 2
        days_in = len([d for d in (age, age + 1, age + 2) if ws <= d <= cd["myd"]])
        days_in = min(days_in, max(0, self.day_left + 1))
        head = cd["maxy"] - t["yield_units"] - days_in   # units it gets unfertilized
        return float(max(0, min(days_in, head)))

    def fert_unit_value(self):
        """Marginal worth of one fertilizer unit: the better of selling it and
        the best crop bonus it can still buy. v22 priced it at the market quote,
        which is why it sold 101 units of the thing that doubles strawberry."""
        v = self._fuv
        if v is not None:
            return v
        best = float(self.price["FERTILIZER"])
        for _x, _y, t in self.plants:
            if t["fertilized_until_day"] >= self.day:
                continue
            g = self.fert_prod_gain(t)
            if g > 0:
                cand = g * self.price[t["crop"]] * P["fert_use_disc"]
                if cand > best:
                    best = cand
        self._fuv = best
        return best

    def fert_need(self):
        """How many fertilizer units the standing crop can still profitably use."""
        n = self.n_fert_need
        if n is not None:
            return n
        n = 0
        for _x, _y, t in self.plants:
            if t["fertilized_until_day"] >= self.day:
                continue
            g = self.fert_prod_gain(t)
            if g > 0 and g * self.price[t["crop"]] * P["fert_use_disc"] > self.price["FERTILIZER"]:
                n += 1
        self.n_fert_need = n
        return n

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
                if P["a_fert"]:
                    keep = min(P["fert_keep_max"],
                               int(math.ceil(self.fert_need() * P["fert_keep_mult"])))
                    stock -= max(P["fert_keep"], keep)
                else:
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
            if p == "FERTILIZER" and P["fert_dump"]:
                # No shop and no town-centre demand consumes fertilizer, so its
                # inventory is monotonically rising and its price monotonically
                # falling. Pacing sales over the season just hands the early,
                # expensive part of the curve to the opponent.
                q = stock
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
                cap = P["feed_buy_max"] if P["a_feed"] else P["wheat_buy_max"]
                want = min(need - have, cap, room)
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
            if P["land_days"]:
                # Crop Dusta buys on days 5 and 8 rather than 6 and 11, which is
                # ~75 extra tile-days on the binding resource.
                if day >= P["land_days"][min(n_extra, len(P["land_days"]) - 1)] \
                        and money >= cost:
                    out.append(["BUY_LAND"])
                    money -= cost
            elif money >= cost + 25 * MIN_SEED and self.land_pays(cost, day):
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
            self.tile_owner = {}

        self.shed_left = dict(self.shed)
        tasks = self.build_tasks(day)
        self.task_zone = [self.zone_of(t[0], t[1]) for t in tasks]
        if P["a_bundle"]:
            self.by_tile = {}
            for t in tasks:
                self.by_tile.setdefault((t[0], t[1]), []).append(t)
            self.zone_by_tile = {tl: self.zone_of(tl[0], tl[1]) for tl in self.by_tile}
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
            if t["fertilized_until_day"] >= day or RECIPES[t["crop"]]["f"] <= 0:
                continue
            if P["a_fert"]:
                g = self.fert_prod_gain(t)
                if g * self.price[t["crop"]] * P["fert_use_disc"] <= self.price["FERTILIZER"]:
                    continue
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
            if haul >= P["drop_load"] or (overflow > 0 and haul >= 5):
                if at_shed:
                    acts.append(["DROP"])
                    continue
                if self.shed_dist(ux, uy) <= P["drop_reach"]:
                    acts.append(self.step_toward(ux, uy, self.shed_goal(ux, uy)))
                    continue

            if at_shed:
                sup = self.shed_supply(i, inv, zone_feed, zone_fert, day)
                if sup is not None:
                    if P["a_shedalloc"] and sup[0] == "PICKUP":
                        # Every unit sees the same start-of-turn shed, so without
                        # this they all request the same stock and the engine
                        # silently trims the losers to nothing -- a wasted action
                        # AND a wasted turn standing at the shed. Book the stock
                        # out as we assign it.
                        item, n = sup[1], int(sup[2])
                        n = min(n, self.shed_left.get(item, 0))
                        if n <= 0:
                            sup = None
                        else:
                            self.shed_left[item] -= n
                            sup = ["PICKUP", item, n]
                    if sup is not None:
                        acts.append(sup)
                        continue
            elif (inv.get("WHEAT", 0) <= 0 and self.shed.get("WHEAT", 0) > 0
                  and zone_feed.get(i, 0) > 0 and day < LAST_DAY
                  and self.shed_dist(ux, uy) <= P["refill_reach"]):
                acts.append(self.step_toward(ux, uy, self.shed_goal(ux, uy)))
                continue

            if P["a_bundle"]:
                tgt = self.pick_bundle(i, ux, uy, inv, claimed, plant_left, day, hour)
            else:
                tgt = self.pick_task(i, ux, uy, inv, tasks, claimed, plant_left, day, hour)
            if tgt is None:
                acts.append(self.idle(ux, uy, inv, day, at_shed))
                continue
            x, y, op, arg, _v = tgt
            if op is None:                      # travelling to a bundle
                acts.append(self.step_toward(ux, uy, (x, y)))
                continue
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
            # Hands hired this turn only appear NEXT turn, so at hour 0 there is
            # exactly one unit on the board. Dividing the day's feed by that gives
            # the farmer a mandate to empty the entire shed into its own pockets,
            # after which no other hand can ever pick up wheat and the herd
            # starves. Share against the crew we will actually have today.
            share = max(1, self.n_units, self.hands_target + 1)
            want = max(want, int(math.ceil(self.n_unfed / share)))
        if P["a_feed"] and want:
            # load a whole round's worth in one action; a 1-unit pickup costs the
            # same turn as a 20-unit one, and the walk back costs several more
            carry = inv.get("WHEAT", 0)
            target = max(int(math.ceil(want * P["feed_carry"])), P["feed_carry_min"])
            # never take more than a fair share of the shed: a hand that hoards
            # the reserve blocks every other hand from feeding
            share = max(1, self.n_units, self.hands_target + 1)
            fair = int(math.ceil(self.shed.get("WHEAT", 0) / share)) + P["wheat_spare"]
            target = min(target, max(P["feed_carry_min"], fair))
            take = min(self.shed.get("WHEAT", 0), target - carry)
            if take > 0 and carry < want:
                return ["PICKUP", "WHEAT", int(take)]
        elif want and inv.get("WHEAT", 0) < want:
            have = self.shed.get("WHEAT", 0)
            if have > 0:
                return ["PICKUP", "WHEAT", int(min(have, want + P["wheat_spare"]))]
        if P["a_fert"]:
            if zone_fert.get(i, 0) and inv.get("FERTILIZER", 0) == 0:
                take = min(self.shed.get("FERTILIZER", 0), zone_fert[i], P["fert_carry"])
                if take > 0:
                    return ["PICKUP", "FERTILIZER", int(take)]
        elif (zone_fert.get(i, 0) and inv.get("FERTILIZER", 0) == 0
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

    def _doable(self, group, inv, claimed, plant_left, ux, uy, day, hour):
        out = []
        for t in group:
            x, y, op, arg, _v = t
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
            if day >= LAST_DAY and op == "HARVEST":
                d = abs(x - ux) + abs(y - uy)
                if hour + d + 1 + self.shed_dist(x, y) > 21 - P["last_day_slack"]:
                    continue
            out.append(t)
        return out

    def pick_bundle(self, i, ux, uy, inv, claimed, plant_left, day, hour):
        """Best tile by value per turn, counting every task the unit can do once
        it gets there. Only one task is executed and claimed per turn, but the
        walk is justified by the whole bundle -- which is what stops a hand from
        crossing the farm, feeding one cow and leaving its fertilizer behind."""
        held = self.holds.get(i)
        best = bestg = None
        # With a linear move toll every score can be negative; starting the
        # search at 0 would make the hand idle rather than walk to the least-bad
        # job, which is never right while any work remains.
        bs = bsg = -1e18 if P["a_route"] else 0.0
        for tile, group in self.by_tile.items():
            owner = self.tile_owner.get(tile)
            if owner is not None and owner != i:
                continue
            doable = self._doable(group, inv, claimed, plant_left, ux, uy, day, hour)
            if not doable:
                continue
            x, y = tile
            d = abs(x - ux) + abs(y - uy)
            zone_ok = self.zone_by_tile.get(tile, 0) == i
            vals = sorted((t[4] for t in doable), reverse=True)
            vmax = vals[0]
            if d > P["zone_reach"] and not zone_ok and vmax < P["reach_override"]:
                continue
            tot = vals[0] + P["bundle_decay"] * sum(vals[1:])
            if P["a_route"]:
                # Prize-collecting objective: subtract a fixed toll per step
                # instead of dividing by turns. A value RATE is scale-free, so a
                # distant jackpot always outranks adjacent work and the crew
                # criss-crosses the farm -- measured at 1.8 moves per productive
                # action against the tape's 1.0. A linear toll makes a hand
                # finish its neighbourhood before it walks anywhere.
                s = tot - P["move_cost"] * d
            else:
                turns = d + len(doable) * P["bundle_act_cost"]
                s = tot / max(1.0, turns) ** P["dist_pow"]
            if held == tile:
                s *= P["stick"]
            if s > bsg:
                bestg, bsg = (tile, doable), s
            if zone_ok and s > bs:
                best, bs = (tile, doable), s
        pick = best if best is not None else bestg
        if held is not None and self.tile_owner.get(held) == i:
            del self.tile_owner[held]
        if pick is None:
            self.holds.pop(i, None)
            return None
        tile, doable = pick
        self.holds[i] = tile
        self.tile_owner[tile] = i
        if tile == (ux, uy):
            return max(doable, key=lambda t: t[4])
        return (tile[0], tile[1], None, None, 0.0)   # travel marker

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
            if P["a_feed"]:
                dayv = self.animal_day_value(t)
                if not t["fed_today"] and left >= 0:
                    v = dayv * P["feed_val"]
                    if t["consecutive_unfed"] >= 1:
                        # two missed days and the animal is gone, taking its cost
                        # and every remaining day of product and fertilizer
                        v += P["feed_panic"] * (a["cost"] * 0.5
                                                + dayv * max(0, min(left, 12)))
                    tasks.append((x, y, "FEED", None, v))
                # CARE banks +1 unit, collected at the next production day only if
                # the animal is fed then and is not already at max_held.
                if (not t["cared_today"] and left >= 1
                        and t["yield_units"] + t.get("pending_care_bonus", 0) < a["held"]):
                    cpr = max(pr, self.forecast(a["product"], a["interval"]))
                    tasks.append((x, y, "CARE", None, cpr * P["care_val"]))
            else:
                if not t["fed_today"] and left >= 0:
                    v = pr * 1.1
                    if t["consecutive_unfed"] >= 1:
                        v += 600.0 + per_prod * pr * max(0, left) / a["interval"]
                    tasks.append((x, y, "FEED", None, v))
                if not t["cared_today"] and left >= 1:
                    tasks.append((x, y, "CARE", None, pr * 0.95))
            if t["fertilizer_available"]:
                tasks.append((x, y, "COLLECT_FERTILIZER", None,
                              self.fert_unit_value() * P["collect_val"]
                              if P["a_feed"] else
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
                    if k >= 0 and k % cd["interval"] == 0:
                        # Production lands tonight. Watering is worth a full extra
                        # unit if the plant is fertilized. If it is not, watering
                        # still matters: it resets consecutive_unwatered, which is
                        # what sets the PARITY of every later forced watering.
                        # Strawberry produces on odd day-offsets while the
                        # survival pattern (forced water on the planting day, then
                        # every second day) waters on even ones -- so without this
                        # nudge the fertilizer bonus can never once apply and the
                        # crop is permanently capped at 4 units instead of 8.
                        v = pr if fert else pr * P["water_prod_val"]
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
                if P["a_fert"]:
                    # value the actual number of production days the 3-day window
                    # covers, so the scarce fertilizer lands on strawberry
                    # (2 units x $180) instead of wheat (2 units x $45)
                    gain = self.fert_prod_gain(t) * pr * P["fert_use_disc"]
                    net = gain - self.price["FERTILIZER"] - av
                else:
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
