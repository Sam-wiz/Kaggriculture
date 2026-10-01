"""Hybrid: boatlee_v29's action tape + our v22 market model as the selling overlay.

The tape supplies every physical action (farmer / hands) and every macro buy
(HIRE, BUY_SEED, BUY_ANIMAL, BUY_PRODUCT, BUY_LAND). Only the SELL side is ours.

Two measured facts drive the design:

1. boatlee_v29's own `_adaptive_market` overlay never fires -- the tape empties
   the shed every turn, so there is never an "unscheduled" surplus for it to
   sell. Disabling it reproduces v29 bit-for-bit on every seed. Its 0.97 pool
   score is the tape, not the overlay.
2. The market is a per-slot lockstep auction: at slot i both players quote off
   the same inventory. So the only way to out-earn an identical tape is to move
   the same units to an EARLIER turn -- the opponent then sells into inventory
   we already raised. Selling a turn early is worth ~+$1.7k in the mirror.

So the overlay's job is to decide, per item per turn, how much of the shed to
release now instead of on the tape's schedule. That decision uses v22's market
model: `market_price`, `mean_drain` (which prices in shops that have NOT
unlocked yet), `forecast`, opponent-aware `supply`, glut/tight bias, and hinge
metering -- plus a hard carve-out for WHEAT, which is animal feed and must never
be sold out from under the tape's PICKUP schedule.
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _base  # noqa: E402

_M = _base.load("boatlee29", "h1")
_M._adaptive_market = lambda action, obs, step: action
_M._FR_ITEMS = ()

# ---------------------------------------------------------------- market model
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
EXP_PULL = {p: 0.0 for p in PRODUCTS}
for _shop, _prods in SHOPS.items():
    _m = 2.0 if len(_prods) == 1 else 1.0
    for _p in _prods:
        EXP_PULL[_p] += _m / len(SHOPS)
SHOP_INTERVAL = 3
MAX_SHOPS = 8
TICKS_PER_DAY = 6
I0 = 10000
HINGE_GAIN = 8.0
LAST_DAY = 29

P = dict(
    mode="lookahead",       # 'off' | 'greedy' | 'lookahead' | 'model'
    items=["STRAWBERRY", "MILK", "WOOL", "FERTILIZER", "MELON", "CARROT", "TOMATO", "EGG"],
    lookahead=40,           # how many turns of scheduled sales to pull forward
    wheat=1,                # 1 -> also manage WHEAT (it is animal feed: keep a reserve)
    wheat_days=1.0,         # days of feed to leave in the shed before selling any
    wheat_start=300,        # step before which WHEAT is never touched
    fert_keep=0,            # fertilizer units to hold back
    start_step=0,           # overlay stays silent before this step
    price_gate=0.0,         # skip a pull-forward if price/base is below this
    hold_gain=0.0,          # >0: hold when the 1-turn forecast beats spot by this much
    sell_bias_glut=2.2,     # v22 pacing multipliers, used by mode='model'
    sell_bias_tight=2.0,
    hinge_meter=0.5,
    shed_target=88,
    unlock_trust=1.0,
    opp_weight=0.85,
    opp_mirror=0.7,
    mine_w=0.7,
    horizon_days=0.6,
    sells_first=0,          # 1 always reorder | 2 reorder only when nothing is truncated
    sell_sort=0,            # 1 -> order our SELLs by gross value, high first
    tranche=99,             # cap on units pulled forward per item per turn
    drain_gate=4,           # 0 fixed | 1 boatlee's veto | 2 tick-free block | 3 per-item
    window_cap=24,          # ceiling on the per-item tick-free window
    win4=[0, 4, 3, 2],      # drain_gate=4: window by step %% 4
    hold_horizon=0.2,       # days ahead the hold test forecasts
    opp_press=0.0,          # weight on the opponent's pipeline inside that forecast
    endgame_day=30,         # from this day on, liquidate everything (30 = never; the tape does it)
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


# --------------------------------------------------------------- tape lookahead
# CUM[item][t] = units of `item` the tape schedules over steps 0..t-1.
_NSTEP = len(_M._ACTIONS)
CUM = {p: [0] * (_NSTEP + 1) for p in PRODUCTS}
SCHED = {p: [0] * _NSTEP for p in PRODUCTS}
for _s, _a in enumerate(_M._ACTIONS):
    for _o in (_a.get("market") or []):
        if len(_o) >= 3 and _o[0] == "SELL" and _o[1] in SCHED:
            try:
                SCHED[_o[1]][_s] += max(0, int(_o[2]))
            except (TypeError, ValueError):
                pass
for _p in PRODUCTS:
    _run = 0
    for _s in range(_NSTEP):
        CUM[_p][_s] = _run
        _run += SCHED[_p][_s]
    CUM[_p][_NSTEP] = _run


def _sched_window(item, lo, hi):
    """Units of `item` scheduled over steps lo..hi inclusive."""
    lo = max(0, lo)
    hi = min(_NSTEP - 1, hi)
    if hi < lo:
        return 0
    return CUM[item][hi + 1] - CUM[item][lo]


class Overlay:
    """v22's market model, re-pointed at a tape's shed instead of v22's own farm."""

    def __init__(self):
        self.reset(0)

    def reset(self, step):
        self.last_step = step
        self.debt = {}      # units pulled forward, repaid from the tape's later orders
        self.sold_today = {}
        self.day = -1
        self.opp_pipe = {p: 0.0 for p in PRODUCTS}

    # ------------------------------------------------------------- observation
    def observe(self, obs, step):
        me = int(_M._get(obs, "player", 0) or 0)
        farms = list(_M._get(obs, "farms", []) or [])
        self.me = me
        self.farm = farms[me] if me < len(farms) else {}
        priv = _M._get(obs, "private", {}) or {}
        self.shed = dict(_M._get(priv, "shed", {}) or {})
        self.invs = list(_M._get(priv, "inventories", []) or [])
        market = _M._get(obs, "market", {}) or {}
        self.inv = dict(_M._get(market, "inventory", {}) or {})
        self.price = dict(_M._get(market, "prices", {}) or {})
        town = _M._get(obs, "town", {}) or {}
        self.shops = list(_M._get(town, "unlocked_shops", []) or [])
        self.day = step // 24
        self.hour = step % 24
        self.day_left = LAST_DAY - self.day
        self.drain = self.drain_rates(self.shops)
        self.n_animals = 0
        self.pipeline = {p: 0.0 for p in PRODUCTS}
        for row in (_M._get(self.farm, "tiles", []) or []):
            for t in row or []:
                if not isinstance(t, dict):
                    continue
                if t.get("kind") == "PLANT":
                    self.pipeline[t["crop"]] += self.plant_future(t)
                elif "animal" in t:
                    self.n_animals += 1
                    a = ANIMALS[t["animal"]]
                    rem = max(0, self.day_left - 1)
                    per = min(1 + a["interval"], a["held"]) / a["interval"]
                    self.pipeline[a["product"]] += t["yield_units"] + rem * per
                    self.pipeline["FERTILIZER"] += rem
        for p in PRODUCTS:
            self.pipeline[p] += self.shed.get(p, 0) + self.carried(p)
        if step % 6 == 0 or self.opp_pipe is None:
            self.opp_pipe = self.scan_opponent(farms[1 - me] if len(farms) > 1 else {})

    def carried(self, p):
        return sum(iv.get(p, 0) for iv in self.invs)

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

    def scan_opponent(self, farm):
        pipe = {p: 0.0 for p in PRODUCTS}
        for row in (_M._get(farm, "tiles", []) or []):
            for t in row or []:
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

    # ------------------------------------------------------------ market model
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
        """Average daily town pull over the next `days_ahead` days, counting shops
        that have not unlocked yet -- today's shop list badly under-prices the
        whole first half of the game."""
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

    def supply(self, item, horizon=None):
        """Committed supply reaching the shared pool inside `horizon` days, scaled
        so a season-long pipeline is not charged against a few days of drain."""
        if horizon is None or self.day_left <= 0:
            scale = 1.0
        else:
            scale = min(1.0, float(horizon) / max(1.0, self.day_left))
        mine = self.pipeline[item] * scale * P["mine_w"]
        theirs = max(self.opp_pipe[item] * scale, mine * P["opp_mirror"])
        return mine + theirs * P["opp_weight"]

    # ------------------------------------------------------------------ policy
    def model_q(self, item, avail):
        """v22's pacing: clear stock+pipeline by day 29, front-loaded under glut,
        held back while the town is still short, metered on a hinge curve."""
        horizon = max(1, self.day_left + 1)
        total = max(avail, self.pipeline[item])
        q = total / horizon
        q *= P["sell_bias_glut"] if total > self.drain[item] * horizon else P["sell_bias_tight"]
        if MARKET_PARAMS[item]["bf"] == "hinge" and self.inv[item] < I0:
            q *= P["hinge_meter"]
        q = int(math.ceil(q)) - self.sold_today.get(item, 0)
        shed_total = sum(max(0, v) for k, v in self.shed.items() if k in PRODUCTS)
        carried_total = sum(sum(v for k, v in iv.items() if k in PRODUCTS) for iv in self.invs)
        overflow = shed_total + carried_total - P["shed_target"]
        if overflow > 0:
            q = max(q, min(avail, int(math.ceil(overflow * avail / max(1, shed_total)))))
        return max(0, q)

    def window(self, item, step):
        """How many turns of the tape's schedule it is safe to pull into `step`.

        The town consumes on steps divisible by 4 (24 for the town centre) and it
        does so AFTER the market resolves. So a unit moved from step s back to
        step t skips every consumption tick in [t, s-1] and prints against a
        fuller market. Inside one 4-step block there is no tick to skip, and
        moving a unit earlier inside the block is pure profit in a mirror: the
        opponent then sells into inventory we already raised."""
        g = int(P["drain_gate"])
        k = int(P["lookahead"])
        if g == 0:
            return k
        if g == 1:  # boatlee's rule: never pull across a tick, at any depth
            return 0 if _M._town_demand_now({"town": {"unlocked_shops": self.shops}},
                                            item, step) > 0 else k
        if g == 4:  # explicit per-phase window, swept to find the shape
            return min(k, int(P["win4"][step % 4]))
        if g == 2:  # pull only as far as the end of the current tick-free block
            free = (4 - (step % 4)) % 4
            return min(k, free)
        # g == 3: per-item. Shops pull every 4 steps but only for what they sell,
        # and the town centre pulls every 24 -- except FERTILIZER, which no shop
        # and no town centre ever consumes. Fertiliser therefore has no tick to
        # respect at all: its inventory only ratchets up, so releasing it before
        # the opponent does is free money.
        shop = 0.0
        for s in self.shops:
            prods = SHOPS.get(s)
            if prods and item in prods:
                shop += 2.0 if len(prods) == 1 else 1.0
        cap = int(P["window_cap"])
        for d in range(0, cap + 1):
            s = step + d
            pull = shop if s % 4 == 0 else 0.0
            if item != "FERTILIZER" and s % 24 == 0:
                pull += 1.0
            if pull > 0:
                return min(k, d)
        return min(k, cap)

    def hold(self, item):
        """True when the market model says this unit is worth more next turn.

        The town consumes every 4 steps, so an item can be a third cheaper on a
        pre-drain turn than on the turn after it. `forecast` prices the drain in
        (including shops that have not unlocked yet); `supply` prices in what the
        opponent's visible tiles are about to dump on top of us."""
        spot = float(self.price.get(item, 0) or 0)
        if spot <= 0:
            return False
        base = MARKET_PARAMS[item]["base"]
        if P["price_gate"] > 0 and spot < base * P["price_gate"]:
            return True
        if P["hold_gain"] > 0:
            h = float(P["hold_horizon"])
            nxt = self.forecast(item, h, extra=self.supply(item, h) * P["opp_press"])
            if (nxt - spot) / spot > P["hold_gain"]:
                return True
        return False

    def __call__(self, action, obs, step):
        if step == 0 or step < self.last_step:
            self.reset(step)
        self.last_step = step
        if P["mode"] == "off" or step < int(P["start_step"]):
            return action
        self.observe(obs, step)
        if self.hour == 0:
            self.sold_today = {}

        action = _M._copy_action(action)
        market = [list(o) for o in (action.get("market") or [])]

        # 1. Repay what we pulled forward, out of the tape's own later orders.
        #    Anything still owed after this turn is forgiven -- the tape's sell
        #    quantities are aspirational (it orders far more than the shed holds),
        #    so carrying a ledger forward would silently choke real sales.
        if self.debt:
            kept = []
            for o in market:
                if len(o) >= 3 and o[0] == "SELL" and self.debt.get(o[1], 0) > 0:
                    try:
                        n = max(0, int(o[2]))
                    except (TypeError, ValueError):
                        n = 0
                    cut = min(n, self.debt[o[1]])
                    self.debt[o[1]] -= cut
                    n -= cut
                    if n <= 0:
                        continue
                    o = [o[0], o[1], n]
                kept.append(o)
            market = kept
            self.debt = {}

        items = [i for i in P["items"] if i in PRODUCTS]
        if P["wheat"] and step >= int(P["wheat_start"]):
            items = items + ["WHEAT"]
        endgame = self.day >= int(P["endgame_day"])

        extra = {}
        for item in items:
            stock = max(0, int(self.shed.get(item, 0) or 0))
            reserve = _M._pickup_reserve(action, item)
            if item == "WHEAT":
                reserve += int(self.n_animals * P["wheat_days"])
            elif item == "FERTILIZER":
                reserve += int(P["fert_keep"])
            already = sum(max(0, int(o[2])) for o in market
                          if len(o) >= 3 and o[0] == "SELL" and o[1] == item)
            surplus = stock - reserve - already
            if surplus <= 0:
                continue
            if endgame:
                extra[item] = surplus
                continue
            if P["mode"] == "greedy":
                want = surplus
            else:
                # Pull the next `lookahead` turns of the tape's own schedule
                # forward into this turn.
                k = self.window(item, step)
                if k <= 0:
                    continue
                want = _sched_window(item, step + 1, step + k)
                if P["mode"] == "model":
                    want = max(want, self.model_q(item, surplus))
            want = min(surplus, want, int(P["tranche"]))
            if want <= 0:
                continue
            if self.hold(item):
                continue
            extra[item] = want
            self.debt[item] = self.debt.get(item, 0) + want

        # 2. Merge our extra units into the existing order for that item, or add
        #    a new order. Slot order is preserved for everything we do not touch.
        for item, q in extra.items():
            hit = next((o for o in market
                        if len(o) >= 3 and o[0] == "SELL" and o[1] == item), None)
            if hit is not None:
                hit[2] = max(0, int(hit[2])) + q
            else:
                market.append(["SELL", item, int(q)])

        # Reordering is only safe while nothing falls off the 10-order cliff: the
        # tape fills all ten slots in the opening and dropping one of its buys
        # costs far more than an earlier print is worth.
        if P["sells_first"] and (P["sells_first"] == 1 or len(market) <= 10):
            sells = [o for o in market if len(o) >= 1 and o[0] == "SELL"]
            rest = [o for o in market if not (len(o) >= 1 and o[0] == "SELL")]
            if P["sell_sort"]:
                sells.sort(key=lambda o: -float(self.price.get(o[1], 0) or 0) * o[2])
            market = sells + rest
        action["market"] = market[:10]
        return action


_OVER = {0: Overlay(), 1: Overlay()}


def agent(obs):
    # The tape runs exactly once per turn: `_weed_repair_action` keeps state
    # keyed to what it emitted, so a retry inside an except: block would
    # desynchronise it. Only the overlay is guarded.
    action = _M.agent(obs)
    try:
        fallback = int(_M._get(obs, "day", 0) or 0) * 24 + int(_M._get(obs, "hour", 0) or 0)
        raw = _M._get(obs, "step", None)
        step = int(raw) if raw is not None else fallback
        step = min(max(0, step), _NSTEP - 1)
        seat = _M._seat(obs)
        return _M._align_hands(_OVER[seat](action, obs, step), obs)
    except Exception:
        return action
