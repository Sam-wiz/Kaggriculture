

# ==========================================================================
# SIDE FARM
#
# The tape above is fixed: it buys two land quadrants (days 6 and 11), hires
# up to 12 hands a day, and never touches the SE quadrant -- 25 tiles idle all
# season.  This bolts a small independent farm onto those tiles.
#
# Three invariants keep the tape bit-identical to `port2/h_over.py`:
#
#   1. HANDS.  The tape drives hand slots 0..H-1 where H is the number of HIRE
#      orders it has issued today (hands are dismissed every night, so H resets
#      daily).  We count those orders as they go by and only ever write slots
#      >= H.  We never use the tape's own `n_units`: on many days it declares
#      only 10 units while holding 12 hands, and driving the two it meant to
#      leave standing would move them off the squares its later actions assume.
#
#   2. MARKET.  Orders are executed in list order and a HIRE costs fib(hires
#      today), so every order of ours is APPENDED after the tape's -- never
#      inserted, never reordered, never truncated.  The tape fills all ten
#      slots at hour 0 of days 6..29; on those steps we simply add nothing.
#
#   3. SEEDS.  PLANT validation is atomic per crop: if the turn's total PLANT
#      requests for a crop exceed the seeds on hand, the engine drops ALL of
#      them, the tape's included.  So we count the tape's PLANT requests for
#      this turn first and only plant out of what is left, and we keep a ledger
#      of the seeds we bought ourselves so we never spend the tape's.
# ==========================================================================

P.update(dict(
    side_on=1,
    side_land_day=11,       # earliest day to buy the SE quadrant ($4000)
    side_land_cash=11000,   # ... and the cash we want in hand first
    side_hands=1,           # extra hands hired per day, on top of the tape's
    side_day=11,            # first day we hire them
    side_stop_day=99,       # last day we hire them (wages run to the final bell)
    side_hire_hour=1,       # after the tape's own hour-0/1 hires
    side_crop="AUTO",       # 'AUTO' or a crop name
    side_fert=0,            # 1 -> fertilize (doubles the watering bonus)
    side_fert_price=30,     # ... only while fertilizer is at most this dear
    side_geese=0,           # geese to run in the SE quadrant
    side_goose_day=12,
    side_wheat_buy=1,       # buy feed rather than raid the tape's wheat
    side_sell_every=2,      # append our SELL orders every N hours
    side_tranche=12,
    side_drop_load=8,       # carried produce that justifies a walk to the shed
    side_seed_ahead=6,      # seeds to keep banked ahead of the planter
    side_last_plant=27,
    side_acts=9.0,          # useful actions a hand really gets through in a day
    side_radius=4,          # only farm SE tiles this close to the shed corner
    side_dist_pow=1.6,      # >1 keeps a hand working its own corner
))

# `w` counts every watering the tile needs, not just the ones that pay: a plant
# left dry two days running turns into a weed, so the survival waterings between
# planting and the yield window are part of the price of the crop.  With one or
# two hands the action budget -- not the 25 tiles -- is what binds, so `cyc` and
# the action count are what the planner actually reasons about.
_SIDE_CROPS = {
    "WHEAT":      dict(seed=10,  first=2,  myd=4,  interval=0, maxy=6, ongoing=False,
                       cyc=4,  w=4, u=3, uf=6, fa=2),
    "CARROT":     dict(seed=20,  first=2,  myd=3,  interval=0, maxy=4, ongoing=False,
                       cyc=3,  w=3, u=2, uf=4, fa=1),
    "TOMATO":     dict(seed=50,  first=8,  myd=8,  interval=1, maxy=4, ongoing=True,
                       cyc=11, w=6, u=4, uf=8, fa=4),
    "STRAWBERRY": dict(seed=100, first=10, myd=10, interval=2, maxy=4, ongoing=True,
                       cyc=16, w=9, u=4, uf=8, fa=6),
    "MELON":      dict(seed=80,  first=10, myd=12, interval=0, maxy=6, ongoing=False,
                       cyc=12, w=9, u=6, uf=6, fa=0),
}


def _side_load(crop, fert):
    """Hand-actions per tile per day for one tile of `crop`."""
    cd = _SIDE_CROPS[crop]
    return (2.0 + cd["w"] + (cd["fa"] if fert else 0)) / cd["cyc"]


class _Side(object):
    """An independent little farm on the SE quadrant, driven by the hands the
    tape does not know it has."""

    def __init__(self):
        self.reset(0)

    def reset(self, step):
        self.last_step = step
        self.day = -1
        self.tape_hires = 0
        self.my_hires = 0
        self.bank = {}          # seeds we paid for and have not planted yet
        self.fert_bank = 0      # fertilizer we paid for and have not collected yet
        self.drain = {}
        self.inv = {}
        self.price = {}
        self.shops = []
        self.plan_today = []
        self.n_geese = 0
        self.n_tape_animals = 0
        self.planted = {}
        self.pipeline = {}
        self.shed = {}
        self.invs = []
        self.me = 0
        self.owed = {}
        self.yield_at = {}

    # ---------------------------------------------------------- market model
    def _drain_rates(self, shops):
        d = {p: 0.0 for p in _OV_PRODUCTS}
        for shop in shops:
            prods = _OV_SHOPS.get(shop)
            if not prods:
                continue
            mult = 2.0 if len(prods) == 1 else 1.0
            for p in prods:
                d[p] += mult * 6.0
        for p in _OV_PRODUCTS:
            if p != "FERTILIZER":
                d[p] += 1.0
        return d

    def forecast(self, item, days_ahead, extra=0.0):
        """Price `days_ahead` days out, counting the shops the town has not
        opened yet -- pricing off today's two shops makes everything look
        worthless exactly when the season still has 20 days to run."""
        n = int(days_ahead)
        if n <= 0:
            d = self.drain[item]
        else:
            base = 1.0 if item != "FERTILIZER" else 0.0
            known = self.drain[item] - base
            n_now = len(self.shops)
            tot = 0.0
            for t in range(self.day, self.day + n + 1):
                future = max(0, min(_OV_MAX_SHOPS, (t + 1) // _OV_SHOP_INTERVAL) - n_now)
                tot += known + base + future * _OV_TICKS_PER_DAY * _OV_PULL[item]
            d = tot / (n + 1)
        return _ov_price(item, self.inv.get(item, _OV_I0) - d * days_ahead + extra)

    def committed(self, item, horizon):
        """Everything already heading for the shared market inside `horizon`.

        The overlay above already tracks this for the whole board -- both farms'
        standing crops and herds plus our shed -- and getting it wrong is what
        makes a side farm plant 14 strawberries a fortnight before the tape
        dumps 33 of its own on the same day."""
        try:
            return _OVERLAYS[self.me].supply(item, horizon)
        except Exception:
            return self.pipeline.get(item, 0.0)

    # --------------------------------------------------------- crop planning
    def crop_score(self, crop, day, extra):
        """Net dollars per unit of hand-time.  With one or two extra hands and
        25 tiles, ACTIONS are the scarce resource, not land -- so the planner
        ranks by $/action, not $/tile-day."""
        cd = _SIDE_CROPS[crop]
        if day + cd["cyc"] > _OV_LAST_DAY:
            return None
        fert = bool(P["side_fert"]) and cd["uf"] > cd["u"] and \
            float(self.price.get("FERTILIZER", 999) or 999) <= P["side_fert_price"]
        units = cd["uf"] if fert else cd["u"]
        acts = 2 + cd["w"] + (cd["fa"] if fert else 0)
        pr = self.forecast(crop, cd["cyc"] * 0.7, extra=extra)
        cost = cd["seed"]
        if fert:
            cost += cd["fa"] * float(self.price.get("FERTILIZER", 0) or 0)
        return (units * pr - cost) / acts, units, fert

    def plan(self, day, n_slots, load=0.0):
        """Greedy fill: each free tile takes the best crop *given what the
        earlier tiles already committed to the market*, so the mix diversifies
        on its own instead of dumping 25 melons on one day.  Stops as soon as
        the standing crop needs more daily watering than our hands can do --
        an over-planted quadrant is not a bigger farm, it is a weed patch."""
        want = str(P["side_crop"])
        budget = float(P["side_hands"]) * float(P["side_acts"])
        out = []
        extra = {}
        for c in _SIDE_CROPS:
            extra[c] = self.committed(c, _SIDE_CROPS[c]["cyc"] * 0.7)
        for _ in range(max(0, n_slots)):
            if load >= budget:
                break
            best, bs, bu, bf = None, 0.0, 0, False
            for c in _SIDE_CROPS:
                if want != "AUTO" and c != want:
                    continue
                res = self.crop_score(c, day, extra[c])
                if res is None:
                    continue
                if res[0] > bs:
                    best, bs, bu, bf = c, res[0], res[1], res[2]
            if best is None:
                break
            out.append(best)
            extra[best] += bu
            load += _side_load(best, bf)
        return out

    # ---------------------------------------------------------------- geometry
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

    # ------------------------------------------------------------------ tasks
    def build_tasks(self, day, tiles, half, n):
        """Every task is scored in marginal dollars unlocked by that single
        action, so a rescue watering (the whole plant) always outranks planting
        another tile (one action's worth of a future cycle)."""
        tasks = []
        left = _OV_LAST_DAY - day
        endgame = day >= _OV_LAST_DAY - 1
        price = self.price
        empty = []
        n_coop_free = 0
        load = 0.0
        pend_goose = self.shed.get("GOOSE", 0) + self.carried("GOOSE")

        self.yield_at = {}
        reach = int(P["side_radius"])
        for y in range(half, n):
            for x in range(half, n):
                if (x - half) + (y - half) > reach:
                    continue
                t = tiles[y][x]
                if t is None:
                    empty.append((x, y))
                    continue
                if t == "LOCKED" or not isinstance(t, dict):
                    continue
                kind = t.get("kind")
                if kind == "WEED":
                    tasks.append((x, y, "DIG", None, 0.0))
                    continue
                if kind == "PLANT":
                    crop = t["crop"]
                    cd = _SIDE_CROPS[crop]
                    pr = float(price.get(crop, 0) or 0)
                    age = day - t["planted_day"]
                    fert = t.get("fertilized_until_day", -1) >= day
                    yu = t["yield_units"]
                    load += _side_load(crop, fert)
                    if not t["watered_today"]:
                        v = 0.0
                        if not cd["ongoing"]:
                            ws = (cd["myd"] + 1) // 2
                            if ws <= age <= cd["myd"] and yu < cd["maxy"]:
                                v = pr * (2.0 if fert else 1.0)
                        else:
                            k = (day + 1) - t["planted_day"] - cd["first"]
                            if k >= 0 and k % cd["interval"] == 0 and fert:
                                v = pr
                        # dry two days running and the tile is a weed patch: the
                        # rescue is worth everything the plant still has to give
                        if t["consecutive_unwatered"] >= 1 and left >= 1:
                            rest = 0
                            if not cd["ongoing"]:
                                ws = (cd["myd"] + 1) // 2
                                rest = max(0, min(cd["maxy"] - yu,
                                                  min(cd["myd"], age + left) - max(age, ws) + 1))
                            elif day + cd["interval"] <= _OV_LAST_DAY:
                                rest = max(0, min(cd["maxy"] - yu, left // cd["interval"]))
                            v += (yu + rest) * pr + 15.0
                        if v > 0:
                            tasks.append((x, y, "WATER", None, v))
                    if yu > 0 and age >= cd["first"]:
                        if endgame:
                            v = yu * pr
                        elif not cd["ongoing"]:
                            v = yu * pr if (age >= cd["myd"] or yu >= cd["maxy"]) \
                                else yu * pr * 0.08
                        else:
                            v = yu * pr if yu >= cd["maxy"] else yu * pr * 0.10
                        if v > 0:
                            tasks.append((x, y, "HARVEST", None, v))
                            self.yield_at[(x, y)] = (crop, yu)
                    if (bool(P["side_fert"]) and not fert and cd["fa"] > 0
                            and left >= 2 and self.carried("FERTILIZER") > 0):
                        room = cd["maxy"] - yu
                        if not cd["ongoing"]:
                            ok = age <= cd["myd"] - 1 and room > 0
                        else:
                            ok = day + cd["interval"] <= _OV_LAST_DAY
                        if ok:
                            tasks.append((x, y, "FERTILIZE", None, pr * min(2, max(1, room)) * 0.9))
                    continue
                if "animal" in t:
                    a = _OV_ANIMALS[t["animal"]]
                    pr = float(price.get(a["product"], 0) or 0)
                    if not t["fed_today"] and left >= 0:
                        v = pr * 1.4
                        if t["consecutive_unfed"] >= 1:
                            v += 900.0
                        tasks.append((x, y, "FEED", None, v))
                    if not t["cared_today"] and left >= 1:
                        tasks.append((x, y, "CARE", None, pr * 1.1))
                    if t["fertilizer_available"] and bool(P["side_fert"]):
                        tasks.append((x, y, "COLLECT_FERTILIZER", None,
                                      float(price.get("FERTILIZER", 0) or 0)))
                    yu = t["yield_units"]
                    if yu > 0:
                        per = min(1 + a["interval"], a["held"])
                        waste = max(0, yu + per - a["held"])
                        v = yu * pr if endgame else waste * pr + yu * pr * 0.06
                        if v > 0:
                            tasks.append((x, y, "HARVEST", None, v))
                            self.yield_at[(x, y)] = (a["product"], yu)
                    continue
                if kind == "COOP":
                    n_coop_free += 1
                    if pend_goose > 0:
                        tasks.append((x, y, "PLACE", "GOOSE", 900.0))

        # coops first, then crops, on the tiles nearest the shed
        empty.sort(key=lambda c: abs(c[0] - half) + abs(c[1] - half))
        need_coop = max(0, pend_goose + self.goose_backlog() - n_coop_free)
        load += self.n_geese * 2.5
        i = 0
        while i < len(empty) and need_coop > 0:
            x, y = empty[i]
            tasks.append((x, y, "BUILD_COOP", None, 700.0))
            need_coop -= 1
            i += 1
        rest = empty[i:]
        n_weed = sum(1 for t in tasks if t[2] == "DIG")
        self.plan_today = []
        if day <= P["side_last_plant"]:
            self.plan_today = self.plan(day, len(rest) + n_weed, load)
        for j, (x, y) in enumerate(rest):
            if j >= len(self.plan_today):
                break
            c = self.plan_today[j]
            if self.bank.get(c, 0) - self.planted.get(c, 0) <= 0:
                continue
            res = self.crop_score(c, day, self.committed(c, _SIDE_CROPS[c]["cyc"] * 0.7))
            tasks.append((x, y, "PLANT", c, max(8.0, res[0] if res else 8.0)))
        # a weed tile is a dead tile, but clearing one only pays if the action
        # budget has room to farm it afterwards
        dig = 0.0
        if len(self.plan_today) > len(rest):
            c = self.plan_today[-1]
            res = self.crop_score(c, day, self.committed(c, _SIDE_CROPS[c]["cyc"] * 0.7))
            dig = max(6.0, (res[0] if res else 6.0) * 0.9)
        if dig <= 0.0:
            tasks = [t for t in tasks if t[2] != "DIG"]
        else:
            tasks = [(x, y, op, a, dig if op == "DIG" else v)
                     for (x, y, op, a, v) in tasks]
        return tasks

    def wheat_reserve(self):
        return int(self.n_tape_animals * 2) + 4

    def goose_backlog(self):
        pend = self.shed.get("GOOSE", 0) + self.carried("GOOSE")
        return max(0, int(P["side_geese"]) - self.n_geese - pend)

    def carried(self, item):
        return sum(iv.get(item, 0) for iv in self.invs)

    # ------------------------------------------------------------------ entry
    def __call__(self, act, obs, step):
        self.last_step = step
        day = step // 24
        hour = step % 24
        me = int(_read(obs, "player", 0) or 0)
        self.me = me
        farm = list(_read(obs, "farms", []) or [])[me]
        priv = _read(obs, "private", {}) or {}
        tiles = farm["tiles"]
        n = len(tiles)
        half = n // 2

        market = [list(o) for o in (act.get("market") or [])]
        base_hands = [list(h) for h in (act.get("hands") or [])]
        farmer = list(act.get("farmer", ["PASS"]))

        if day != self.day:
            self.day = day
            self.tape_hires = 0
            self.my_hires = 0
        # every HIRE the tape issues shifts the boundary between its hands and
        # ours; count them before we append any of our own
        self.tape_hires += sum(1 for o in market if o and o[0] == "HIRE")

        quads = len(farm.get("unlocked_quadrants", []) or [])
        money = float(farm.get("money", 0) or 0)

        # ------------------------------------------------------------ land
        if (quads == 3 and day >= P["side_land_day"] and hour >= 1
                and money >= P["side_land_cash"] and len(market) < CFG_MAX_ORDERS
                and not any(o and o[0] == "BUY_LAND" for o in market)):
            market.append(["BUY_LAND"])
        have_se = quads >= 4

        # ------------------------------------------------------------ hire
        if (have_se and P["side_day"] <= day <= P["side_stop_day"]
                and hour == int(P["side_hire_hour"]) and int(P["side_hands"]) > 0):
            for _ in range(int(P["side_hands"]) - self.my_hires):
                if len(market) >= CFG_MAX_ORDERS:
                    break
                market.append(["HIRE"])
                self.my_hires += 1

        if not have_se:
            act["market"] = market
            return act

        # -------------------------------------------------------- observation
        self.shed = dict(_read(priv, "shed", {}) or {})
        self.invs = list(_read(priv, "inventories", []) or [])
        seeds = dict(_read(priv, "seeds", {}) or {})
        mkt = _read(obs, "market", {}) or {}
        self.inv = dict(_read(mkt, "inventory", {}) or {})
        self.price = dict(_read(mkt, "prices", {}) or {})
        self.shops = list(_read(_read(obs, "town", {}) or {}, "unlocked_shops", []) or [])
        self.drain = self._drain_rates(self.shops)
        day_left = _OV_LAST_DAY - day

        # what the SE quadrant will add to the market, for its own price forecast
        self.pipeline = {}
        self.n_geese = 0
        self.n_tape_animals = 0
        for row_y in range(n):
            for col_x in range(n):
                if col_x >= half and row_y >= half:
                    continue
                t = tiles[row_y][col_x]
                if isinstance(t, dict) and "animal" in t:
                    self.n_tape_animals += 1
        for y in range(half, n):
            for x in range(half, n):
                t = tiles[y][x]
                if not isinstance(t, dict):
                    continue
                if t.get("kind") == "PLANT":
                    cd = _SIDE_CROPS[t["crop"]]
                    age = day - t["planted_day"]
                    if not cd["ongoing"]:
                        room = cd["maxy"] - t["yield_units"]
                        last = min(cd["myd"], age + day_left)
                        days = max(0, last - max(age, (cd["myd"] + 1) // 2) + 1)
                        self.pipeline[t["crop"]] = self.pipeline.get(t["crop"], 0.0) + \
                            t["yield_units"] + min(room, days)
                    else:
                        self.pipeline[t["crop"]] = self.pipeline.get(t["crop"], 0.0) + \
                            t["yield_units"] + max(0, day_left // max(1, cd["interval"]))
                elif "animal" in t:
                    if t["animal"] == "GOOSE":
                        self.n_geese += 1
                    a = _OV_ANIMALS[t["animal"]]
                    self.pipeline[a["product"]] = self.pipeline.get(a["product"], 0.0) + \
                        t["yield_units"] + max(0, day_left - 1) * 2.0
        for c in _SIDE_CROPS:
            self.pipeline.setdefault(c, 0.0)

        # -------------------------------------------------------- seed ledger
        # the tape's PLANT requests for this turn come first: if the two of us
        # together ask for more of a crop than there are seeds, the engine drops
        # every one of them, the tape's included
        tape_plant = {}
        for a in [farmer] + base_hands:
            if len(a) >= 2 and a[0] == "PLANT":
                tape_plant[a[1]] = tape_plant.get(a[1], 0) + 1
        for c in list(self.bank):
            self.bank[c] = max(0, min(self.bank[c],
                                      seeds.get(c, 0) - tape_plant.get(c, 0)))
        self.fert_bank = max(0, min(self.fert_bank, self.shed.get("FERTILIZER", 0)))
        self.planted = {}

        # ------------------------------------------------------- unit actions
        lo = self.tape_hires
        hands = list(farm.get("hands", []) or [])
        while len(base_hands) < len(hands):
            base_hands.append(["PASS"])
        mine = list(range(lo, len(hands)))
        tasks = self.build_tasks(day, tiles, half, n)
        if mine:
            claimed = set()
            shed_goal = (half, half)
            for i in mine:
                ux, uy = hands[i][0], hands[i][1]
                inv = self.invs[i + 1] if i + 1 < len(self.invs) else {}
                at_shed = (ux, uy) == shed_goal
                base_hands[i] = self.unit_action(
                    i, ux, uy, inv, tasks, claimed, day, hour, at_shed, shed_goal)

        # -------------------------------------------------------- our orders
        room = CFG_MAX_ORDERS - len(market)
        if room > 0:
            self.buy_orders(market, day, hour, seeds, money)
        self.sell_orders(market, day, hour)

        act["farmer"] = farmer
        act["hands"] = base_hands
        act["market"] = market
        return act

    # ------------------------------------------------------------------ units
    def unit_action(self, i, ux, uy, inv, tasks, claimed, day, hour, at_shed, shed_goal):
        haul = sum(v for k, v in inv.items() if k in _OV_PRODUCTS and k != "WHEAT")
        # last-day sweep: anything not in the shed by nightfall is worth nothing
        if day >= _OV_LAST_DAY and haul and hour >= 18:
            return ["DROP"] if at_shed else self.step_toward(ux, uy, shed_goal)
        if haul >= int(P["side_drop_load"]):
            if at_shed:
                return ["DROP"]
            return self.step_toward(ux, uy, shed_goal)
        if at_shed:
            sup = self.shed_supply(inv, day)
            if sup is not None:
                return sup

        best, bs = None, 0.0
        for t in tasks:
            x, y, op, arg, v = t
            key = (x, y, op)
            if key in claimed:
                continue
            if op == "FEED" and inv.get("WHEAT", 0) <= 0:
                continue
            if op == "FERTILIZE" and inv.get("FERTILIZER", 0) <= 0:
                continue
            if op == "PLACE" and inv.get(arg, 0) <= 0:
                continue
            if op == "PLANT" and self.bank.get(arg, 0) - self.planted.get(arg, 0) <= 0:
                continue
            d = abs(x - ux) + abs(y - uy)
            # a step is a whole turn: with ~9 useful actions a day, a jackpot
            # four tiles away is worth less than two chores underfoot
            s = v / (1.0 + d) ** P["side_dist_pow"]
            if s > bs:
                best, bs = t, s
        if best is None:
            if inv and (day >= _OV_LAST_DAY or haul):
                return ["DROP"] if at_shed else self.step_toward(ux, uy, shed_goal)
            need = self.shed_need(inv, day)
            if need is not None and not at_shed:
                return self.step_toward(ux, uy, shed_goal)
            return ["PASS"]
        x, y, op, arg, _v = best
        claimed.add((x, y, op))
        if op == "PLANT":
            self.planted[arg] = self.planted.get(arg, 0) + 1
        if (ux, uy) != (x, y):
            return self.step_toward(ux, uy, (x, y))
        if op == "PLANT":
            self.bank[arg] = self.bank.get(arg, 0) - 1
            return ["PLANT", arg]
        if op == "PLACE":
            return ["PLACE", arg, 1]
        if op == "HARVEST":
            item, units = self.yield_at.get((x, y), (None, 0))
            if item:
                self.owed[item] = self.owed.get(item, 0) + units
        return [op]

    def shed_need(self, inv, day):
        if self.n_geese and inv.get("WHEAT", 0) <= 0 and day < _OV_LAST_DAY \
                and self.shed.get("WHEAT", 0) > self.wheat_reserve():
            return "WHEAT"
        if self.shed.get("GOOSE", 0) > 0 and inv.get("GOOSE", 0) == 0:
            return "GOOSE"
        return None

    def shed_supply(self, inv, day):
        """Top up at the shed.  Never DROP here -- the evening drop is free."""
        if self.shed.get("GOOSE", 0) > 0 and inv.get("GOOSE", 0) == 0:
            return ["PICKUP", "GOOSE", 1]
        if self.n_geese and day < _OV_LAST_DAY:
            # the shed is shared: the tape feeds 17 head out of it, and a hand
            # that arrives to find the bin empty loses the animal two days later
            spare = self.shed.get("WHEAT", 0) - self.wheat_reserve()
            want = self.n_geese * 2 + 1
            if inv.get("WHEAT", 0) < self.n_geese + 1 and spare > 0:
                return ["PICKUP", "WHEAT", int(min(spare, want))]
        if bool(P["side_fert"]) and inv.get("FERTILIZER", 0) == 0:
            # only ever the fertilizer we bought ourselves: the tape doubles its
            # strawberry yield with the shed's, and a bag taken from under it is
            # a unit of fruit that never grows
            k = min(self.fert_bank, self.shed.get("FERTILIZER", 0), 4)
            if k > 0:
                self.fert_bank -= k
                return ["PICKUP", "FERTILIZER", int(k)]
        return None

    # ----------------------------------------------------------------- orders
    def buy_orders(self, market, day, hour, seeds, money):
        if hour == 0:
            return                      # the tape owns all ten slots at hour 0
        room = CFG_MAX_ORDERS - len(market)
        if room <= 0:
            return
        # geese, spread one per day so a single failed order is cheap
        if (int(P["side_geese"]) > 0 and day >= P["side_goose_day"]
                and _OV_LAST_DAY - day >= 6 and hour == 2):
            k = self.goose_backlog()
            if k > 0 and money > 400 + ANIMAL_COST[0]:
                k = min(k, 2, int((money - 400) // ANIMAL_COST[0]))
                if k > 0 and len(market) < CFG_MAX_ORDERS:
                    market.append(["BUY_ANIMAL", "GOOSE", int(k)])
        # feed
        if self.n_geese and hour in (3, 13) and day < _OV_LAST_DAY and P["side_wheat_buy"]:
            have = self.shed.get("WHEAT", 0) + self.carried("WHEAT")
            want = int(self.n_geese * 2) - have
            shed_room = 100 - sum(self.shed.values())
            want = min(want, max(0, shed_room - 4))
            if want > 0 and len(market) < CFG_MAX_ORDERS:
                market.append(["BUY_PRODUCT", "WHEAT", int(want)])
        # fertilizer
        if (bool(P["side_fert"]) and hour == 5 and _OV_LAST_DAY - day >= 3
                and float(self.price.get("FERTILIZER", 999) or 999) <= P["side_fert_price"]):
            have = self.fert_bank + self.carried("FERTILIZER")
            shed_room = 100 - sum(self.shed.values())
            want = min(12 - have, max(0, shed_room - 4))
            if want > 0 and len(market) < CFG_MAX_ORDERS:
                market.append(["BUY_PRODUCT", "FERTILIZER", int(want)])
                self.fert_bank += want
        # seeds -- our own, always, so a PLANT of ours never starves the tape
        if day > P["side_last_plant"]:
            return
        need = {}
        for c in self.plan_today[:int(P["side_seed_ahead"])]:
            need[c] = need.get(c, 0) + 1
        budget = money - 1500.0
        for c in sorted(need, key=lambda c: -_SIDE_CROPS[c]["seed"]):
            k = need[c] - self.bank.get(c, 0)
            if k <= 0:
                continue
            sc = _SIDE_CROPS[c]["seed"]
            k = min(k, int(max(0.0, budget) // sc))
            if k <= 0 or len(market) >= CFG_MAX_ORDERS:
                continue
            market.append(["BUY_SEED", c, int(k)])
            self.bank[c] = self.bank.get(c, 0) + k
            budget -= sc * k

    def sell_orders(self, market, day, hour):
        """Sell what the SE quadrant made.  The tape's own overlay only pulls
        forward sales the tape had scheduled, so a crop the tape never grows
        would otherwise sit in the shed until the shed cap starts binning the
        tape's produce instead."""
        every = max(1, int(P["side_sell_every"]))
        endgame = day >= _OV_LAST_DAY
        if hour == 0 or (hour % every and not endgame):
            return
        for item in sorted(self.owed):
            owed = int(self.owed.get(item, 0))
            if owed <= 0 or item not in _OV_PRODUCTS:
                continue
            # never more than we grew ourselves: the shed is shared, and the
            # tape's overlay paces its own produce far better than we would
            stock = int(self.shed.get(item, 0) or 0)
            if item == "WHEAT":
                stock -= self.wheat_reserve() + int(self.n_geese * 2)
            already = sum(max(0, int(o[2])) for o in market
                          if len(o) >= 3 and o[0] == "SELL" and o[1] == item)
            q = min(owed, stock - already, int(P["side_tranche"]))
            if endgame:
                q = min(owed, stock - already)
            if q <= 0:
                continue
            self.owed[item] = owed - q
            hit = None
            for o in market:
                if len(o) >= 3 and o[0] == "SELL" and o[1] == item:
                    hit = o
                    break
            if hit is not None:
                hit[2] = max(0, int(hit[2])) + int(q)
            elif len(market) < CFG_MAX_ORDERS:
                market.append(["SELL", item, int(q)])


_SIDES = [_Side(), _Side()]


def agent(observation, configuration=None):
    action = _base_agent(observation, configuration)
    if not P["side_on"]:
        return action
    seat = int(_read(observation, "player", 0) or 0)
    step = int(_read(observation, "step", 0) or 0)
    side = _SIDES[seat]
    if step == 0 or step < side.last_step:
        side.reset(step)
    try:
        return side(action, observation, step)
    except Exception:
        side.last_step = step
        return action
