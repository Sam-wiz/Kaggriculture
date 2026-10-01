"""fam0 — r5 opus PROTOTYPE of architecture A: the top family's macro policy (extracted from the 1,773-game
dump, moe/r5/build/opus/an1..an3, layout.log) driving the r2 row-walker executor (exec3.Executor3).

Macro (all measured on 2,176 family seats):
  hires/day   family modal schedule (an1.log)
  land        steps 149 / 219 / 253 (an1.log), cash reserved ahead of each
  herd        linear in revealed-shop demand (an3.log, R^2 0.82-0.95): cows ~ milk shops, sheep ~ wool,
              geese fill to ~20 animals; bursts after each land buy (d0: 2 cows + 3 sheep)
  crops       tile-level canonical layout (layout.log); crop per empty tile by deficit vs demand-driven
              targets (strawberry ~ strawberry demand, tomato ~ tomato demand, carrot ~ carrot demand, wheat fill)
  cash        spend-down (family dawn cash ~$0-800 until d10), keep feed wheat for the herd
Sell: simple trickle (<=SELL_CHUNK units/product/step above a reserve); NOT the family's sell layer.
This is a feasibility probe for the executor, not a candidate.
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", "..", "..", ".."))
for p in (_ROOT, os.path.join(_ROOT, "kaggriculture-island-ga")):
    if p not in sys.path: sys.path.insert(0, p)
import exec3
from islandga.engine_facts import CROPS, ANIMALS, SHED_TILES

HIRES = [4, 4, 6, 6, 6, 6, 8, 9, 9, 10, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 11, 11, 11, 10]
LAND = [(149, 1000), (219, 2000), (253, 4000)]
# animal tiles in family fill order (layout.log d3/d10/d12): (x, y, preferred kind)
ANIMAL_TILES = [(4, 2, "COW"), (4, 4, "COW"), (4, 3, "SHEEP"), (3, 4, "SHEEP"), (2, 4, "SHEEP"),      # NW, d0
                (5, 2, "COW"), (5, 3, "COW"), (5, 4, "COW"), (6, 2, "COW"), (6, 3, "COW"),             # NE, d6
                (6, 4, "GOOSE"), (7, 4, "GOOSE"), (8, 4, "COW"),
                (3, 5, "COW"), (4, 5, "COW"), (2, 5, "GOOSE"), (4, 6, "GOOSE"), (4, 7, "GOOSE"),       # SW, d9
                (1, 3, "GOOSE"), (2, 3, "GOOSE"), (7, 3, "COW"), (7, 2, "COW"), (3, 6, "GOOSE"), (2, 6, "GOOSE")]
DEM = {"BAKERY": ["EGG", "WHEAT"], "PIZZA_SHOP": ["MILK", "TOMATO", "WHEAT"], "BRUNCH_SPOT": ["EGG", "WHEAT", "STRAWBERRY"],
       "YARN_STORE": ["WOOL", "WOOL"], "ICE_CREAM_SHOP": ["STRAWBERRY", "MILK", "WHEAT"], "PET_CAFE": ["CARROT", "CARROT"],
       "SMOOTHIE_SHOP": ["STRAWBERRY", "MILK"], "FARMERS_MARKET": ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY"]}
BASE = dict(WHEAT=25, CARROT=35, TOMATO=60, STRAWBERRY=120, MELON=250, EGG=50, MILK=160, WOOL=200, FERTILIZER=100)
SELL_CHUNK = 3
import json as _json
OPEN = _json.load(open(os.path.join(_HERE, "open_mtmr.json")))
OPEN_STEPS = 24
QUAD_OF = lambda x, y: ("N" if y < 5 else "S") + ("W" if x < 5 else "E")


def _g(v, k, d=None):
    return v.get(k, d) if isinstance(v, dict) else getattr(v, k, d)


def demand(shops):
    c = {}
    for s in shops:
        for p in DEM.get(s, []): c[p] = c.get(p, 0) + 1
    return c


class Fam0:
    def __init__(self):
        self.bp = {"market": {}, "days": {}, "meta": {"herd_goal": {}}}
        self.ex = exec3.Executor3(self.bp)
        self.day = -1
        self.hired = 0
        self.plan_tiles = {}

    # ------------------------------------------------------------ macro targets
    def herd_goal(self, day, D):
        if day < 6:
            return {"COW": 2, "SHEEP": 3, "GOOSE": 0}
        milk, wool = D.get("MILK", 0), D.get("WOOL", 0)
        if day < 9:   # d7 family means: 6.2 / 4.2 / 1.7  (an3: cows +2.8/milk, sheep +1.7/wool)
            cows = min(8, 4 + round(2.8 * milk)); sheep = min(6, 3 + round(0.9 * wool)); tot = 12
        else:         # d12 family means 8.6 / 5.9 / 6.1 (cows +3.3/milk, sheep +1.6/wool, geese fill ~20)
            cows = min(13, 5 + round(3.3 * milk)); sheep = min(10, 3 + round(1.6 * wool)); tot = 20
        geese = max(0, min(8, tot - cows - sheep))
        return {"COW": cows, "SHEEP": sheep, "GOOSE": geese}

    def crop_targets(self, day, D):
        s, t, c = D.get("STRAWBERRY", 0), D.get("TOMATO", 0), D.get("CARROT", 0)
        tgt = {}
        tgt["MELON"] = 10 if day <= 1 else 0
        tgt["STRAWBERRY"] = (0 if day < 2 else 10 if day < 6 else min(36, 18 + round(7.8 * s))) if day <= 13 else 0
        tgt["TOMATO"] = min(22, 3 + round(6.0 * t)) if 8 <= day <= 18 else 0
        tgt["CARROT"] = (min(24, 2 + round(3.7 * c) + (day - 9) // 3)) if day >= 9 else 0
        return tgt

    def day_plan(self, obs, farm, day):
        grid = farm["tiles"]
        unlocked = set(farm.get("unlocked_quadrants") or [])
        D = demand(list(obs["town"]["unlocked_shops"]))
        goal = self.herd_goal(day, D)
        self.ex.goal = dict(goal)
        # animal placements: first N animal tiles in unlocked quadrants, kinds by goal
        need = dict(goal)
        for x, y, k in ANIMAL_TILES:
            t = grid[y][x]
            if isinstance(t, dict) and t.get("animal"): need[t["animal"]] = need.get(t["animal"], 0) - 1
        animals = []
        for x, y, k in ANIMAL_TILES:
            if QUAD_OF(x, y) not in unlocked: continue
            t = grid[y][x]
            if isinstance(t, dict) and (t.get("animal") or t.get("kind") in ("PASTURE", "COOP")):
                if t.get("animal"): continue
                kind = k if need.get(k, 0) > 0 else next((a for a in ("COW", "SHEEP", "GOOSE") if need.get(a, 0) > 0 and
                                                          ANIMALS[a]["structure"] == t.get("kind")), None)
                if kind and ANIMALS[kind]["structure"] == t.get("kind"):
                    animals.append((x, y, kind, None)); need[kind] -= 1
                continue
            if t is not None: continue
            kind = k if need.get(k, 0) > 0 else next((a for a in ("COW", "SHEEP", "GOOSE") if need.get(a, 0) > 0), None)
            if kind:
                animals.append((x, y, kind, ANIMALS[kind]["structure"])); need[kind] -= 1
        atiles = {(x, y) for x, y, _, _ in animals} | {(x, y) for x, y, _ in ANIMAL_TILES
                                                       if isinstance(grid[y][x], dict) and grid[y][x].get("kind") in ("PASTURE", "COOP")}
        # crops: count current plants, assign empty (or freeing) crop tiles by deficit
        have = {}
        free = []
        for y in range(10):
            for x in range(10):
                if (x, y) in atiles or QUAD_OF(x, y) not in unlocked: continue
                t = grid[y][x]
                if t is None: free.append((x, y))
                elif isinstance(t, dict) and t.get("kind") == "PLANT":
                    have[t["crop"]] = have.get(t["crop"], 0) + 1
                    c = CROPS[t["crop"]]
                    if not c["ongoing"] and day - int(t.get("planted_day") or 0) >= c["max_yield_day"] - 1:
                        free.append((x, y))   # will be harvested today: pre-plan its successor
        tgt = self.crop_targets(day, D)
        plants = []
        # far tiles first for long crops (strawberry/tomato), near shed for wheat (feed)
        free.sort(key=lambda p: -(abs(p[0] - 4.5) + abs(p[1] - 4.5)))
        for p in free:
            crop = "WHEAT"
            for c in ("MELON", "STRAWBERRY", "TOMATO", "CARROT"):
                if have.get(c, 0) < tgt.get(c, 0):
                    crop = c; break
            if day >= 27: crop = "CARROT" if day <= 27 else None
            if crop:
                have[crop] = have.get(crop, 0) + 1
                plants.append((p[0], p[1], crop))
        self.bp["days"][str(day)] = {"plants": plants, "animals": animals, "buildings": []}
        self.plan_tiles = {(x, y): c for x, y, c in plants}
        self.goal = goal

    # ------------------------------------------------------------ market
    def market(self, obs, farm, day, hour, step, units_n):
        pv = obs["private"]; shed = dict(pv.get("shed") or {}); seeds = dict(pv.get("seeds") or {})
        prices = obs["market"]["prices"]
        money = float(farm["money"])
        grid = farm["tiles"]
        if step == 0:
            return [["BUY_ANIMAL", "COW", 1], ["BUY_PRODUCT", "WHEAT", 5]]
        if step == 1:
            return [["HIRE"]] * 4 + [["BUY_ANIMAL", "COW", 1], ["BUY_ANIMAL", "SHEEP", 3]]
        out = []
        n_an = sum(1 for row in grid for t in row if isinstance(t, dict) and t.get("animal"))
        carried = {}
        for iv in (pv.get("inventories") or []):
            if isinstance(iv, dict):
                for k, v in iv.items(): carried[k] = carried.get(k, 0) + int(v or 0)
        # sells first (cash for this turn's buys)
        wres = n_an * 2 + 4
        for p in ("STRAWBERRY", "MELON", "MILK", "WOOL", "TOMATO", "EGG", "CARROT", "WHEAT", "FERTILIZER"):
            q = int(shed.get(p, 0))
            if p == "WHEAT": q -= wres
            if p == "FERTILIZER": q -= (0 if day < 12 else 6)
            if day >= 29: q = int(shed.get(p, 0))
            if q <= 0: continue
            chunk = q if (day >= 29 and hour >= 16) else min(q, SELL_CHUNK)
            if prices.get(p, 0) >= 0.45 * BASE[p] or sum(shed.values()) > 80 or day >= 29:
                out.append(["SELL", p, chunk]); money += chunk * prices.get(p, 0) * 0.9
        # land (reserve ahead of the family's land steps)
        nq = len(farm.get("unlocked_quadrants") or [])
        reserve = 0
        for i, (st, cost) in enumerate(LAND):
            if nq == i + 1:
                if step >= st and money >= cost:
                    out.append(["BUY_LAND"]); money -= cost
                elif step >= st - 36:
                    reserve = cost
                break
        # feed wheat: always first claim on cash
        wheat = int(shed.get("WHEAT", 0)) + carried.get("WHEAT", 0)
        feed_need = n_an + 1 if day < 29 else 0
        wp = prices.get("WHEAT", 30) + 3
        if wheat < feed_need and money > wp:
            k = min(feed_need - wheat, int(money // wp))
            if k > 0: out.append(["BUY_PRODUCT", "WHEAT", k]); money -= k * wp
        feed_res = max(0, n_an - wheat) * wp
        # hires (engine rejects unaffordable ones; keep feed money)
        want_h = HIRES[min(day, 29)]
        hires_today = int(farm.get("hires_today") or 0)
        if hour <= 2 and hires_today < want_h:
            n = min(want_h - hires_today, 10 - len(out))
            a, b, spend = 1, 1, 0
            for _ in range(hires_today): a, b = b, a + b
            k = 0
            while k < n and money - a >= feed_res:
                money -= a; spend += a; k += 1; a, b = b, a + b
            out += [["HIRE"]] * k
        # seeds for planned plantings (priority long crops)
        if day <= 27:
            need = {}
            for (x, y), c in self.plan_tiles.items():
                t = grid[y][x]
                if t is None or (isinstance(t, dict) and t.get("kind") == "PLANT" and not CROPS[t["crop"]]["ongoing"]):
                    need[c] = need.get(c, 0) + 1
            for c in ("WHEAT", "MELON", "STRAWBERRY", "TOMATO", "CARROT"):
                miss = need.get(c, 0) - int(seeds.get(c, 0))
                cost = CROPS[c]["seed"]
                avail = money - reserve - feed_res
                n = min(miss, int(avail // cost)) if avail > 0 else 0
                if n > 0: out.append(["BUY_SEED", c, n]); money -= n * cost
        # animals toward goal (after the opening), keep reserves
        if day >= 1:
            goal = getattr(self, "goal", {})
            owned = {}
            for row in grid:
                for t in row:
                    if isinstance(t, dict) and t.get("animal"): owned[t["animal"]] = owned.get(t["animal"], 0) + 1
            for k in ("COW", "SHEEP", "GOOSE"):
                have = owned.get(k, 0) + int(shed.get(k, 0)) + carried.get(k, 0)
                miss = goal.get(k, 0) - have
                cost = ANIMALS[k]["cost"]
                while miss > 0 and money - cost >= reserve + feed_res + 30 and len(out) < 10:
                    out.append(["BUY_ANIMAL", k, 1]); money -= cost; miss -= 1
        return out[:10]

    def act(self, obs):
        seat = int(obs["player"]); day = int(obs["day"]); hour = int(obs["hour"]); step = int(obs["step"])
        farm = obs["farms"][seat]
        if step < OPEN_STEPS:      # family day-0 tape (identical in 214/214 mtmr_s1 games)
            return OPEN[step]
        if day != self.day or hour in (8, 16):
            self.day_plan(obs, farm, day)
            if hour in (8, 16):
                self.ex.day = -1        # rebuild tours with the refreshed targets
            self.day = day
        a = self.ex.act(obs)
        a["market"] = self.market(obs, farm, day, hour, step, 1 + len(farm.get("hands") or []))
        return a


_A = None


def agent(obs, config=None):
    global _A
    if _A is None or int(obs["step"]) == 0:
        _A = Fam0()
    return _A.act(obs)
