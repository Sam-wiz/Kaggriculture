"""Executor v2 for island-ga blueprints: sticky per-unit task queues.

vs islandga.ReferenceExecutor:
- units commit to a task sequence until done (no per-turn thrash)
- FEED/PLACE auto-prefetch their item at the shed, then continue
- late-day DROP appended when carrying goods
- same market channel (blueprint replay + animal ledger + seed makeup)

A unit's queue is a list of steps:
  ("GOTO", x, y)              walk toward (x,y); pops on arrival
  ("DO", verb, ...)           emit verb at current tile; pops after one emit
  ("GOSHED",)                 walk to nearest shed tile
  ("SHEDOP", verb, ...)       emit verb once on a shed tile
"""
from islandga.engine_facts import ANIMALS, CROPS, SHED_TILES


def _g(v, k, d=None):
    return v.get(k, d) if isinstance(v, dict) else getattr(v, k, d)


def _dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def _toward(pos, tgt):
    x, y = pos
    tx, ty = tgt
    if x < tx:
        return ["EAST"]
    if x > tx:
        return ["WEST"]
    if y < ty:
        return ["SOUTH"]
    if y > ty:
        return ["NORTH"]
    return None


def _shed_gate(pos):
    return min(SHED_TILES, key=lambda s: _dist(pos, s))


P_DEAD, P_FEED, P_HARVEST, P_WATER = 0, 1, 2, 2
P_PLANT, P_BUILD, P_PLACE, P_COLLECT, P_CARE, P_DIG = 3, 4, 4, 5, 6, 8


QUADS = {"NW": (0, 0), "NE": (5, 0), "SW": (0, 5), "SE": (5, 5)}


def _quad(pos):
    return ("N" if pos[1] < 5 else "S") + ("W" if pos[0] < 5 else "E")


class Executor2:
    def __init__(self, bp):
        self.bp = bp
        self.goal = dict((bp.get("meta") or {}).get("herd_goal") or {})
        self.q = {}          # unit index -> list of steps
        self.zone = {}       # unit index -> quadrant name, assigned at hour 0

    # ---------------------------------------------------------- market
    def _market_orders(self, turn, grid, shed, carried):
        owned = {}
        for row in grid:
            for tl in row:
                if isinstance(tl, dict) and tl.get("animal"):
                    k = tl["animal"]
                    k = k.get("kind") if isinstance(k, dict) else k
                    owned[k] = owned.get(k, 0) + 1
        out = []
        for o in (self.bp["market"].get(str(turn)) or []):
            if o and o[0] == "BUY_ANIMAL" and len(o) > 2:
                kind = o[1]
                have = (owned.get(kind, 0) + int(shed.get(kind, 0) or 0)
                        + carried.get(kind, 0))
                room = self.goal.get(kind, 0) - have
                if room <= 0:
                    continue
                out.append(["BUY_ANIMAL", kind, min(int(o[2]), room)])
            else:
                out.append(list(o))
        return out[:10]

    # ---------------------------------------------------------- jobs
    def _jobs(self, day, grid, target, seeds):
        want_plant = {(x, y): c for x, y, c in (target.get("plants") or [])}
        want_animal = {(x, y): (k, s) for x, y, k, s
                       in (target.get("animals") or [])}
        for x, y, s in (target.get("buildings") or []):
            want_animal.setdefault((x, y), (None, s))
        jobs = []
        budget = dict(seeds)
        for y, row in enumerate(grid):
            for x, tl in enumerate(row):
                pos = (x, y)
                if tl is None:
                    crop = want_plant.get(pos)
                    if crop and budget.get(crop, 0) > 0:
                        budget[crop] -= 1
                        jobs.append((P_PLANT, x, y, ("PLANT", crop)))
                    elif pos in want_animal:
                        struct = want_animal[pos][1]
                        v = "BUILD_COOP" if struct == "COOP" else "BUILD_PASTURE"
                        jobs.append((P_BUILD, x, y, (v,)))
                    continue
                if not isinstance(tl, dict):
                    continue
                kind = tl.get("kind")
                if kind == "PLANT":
                    crop = tl.get("crop")
                    c = CROPS.get(crop) or {}
                    age = day - int(tl.get("planted_day") or day)
                    if not tl.get("watered_today"):
                        urg = int(tl.get("consecutive_unwatered", 0) or 0) >= 1
                        jobs.append((P_DEAD if urg else P_WATER, x, y, ("WATER",)))
                    yu = int(tl.get("yield_units", 0) or 0)
                    myd = c.get("max_yield_day", 99)
                    ripe = (yu >= c.get("max_yield", 99) or age > myd
                            or (age == myd and tl.get("watered_today")))
                    can = age >= c.get("first_yield_day", 0)
                    if yu > 0 and can and (c.get("ongoing") or ripe):
                        jobs.append((P_HARVEST, x, y, ("HARVEST",)))
                    if yu == 0 and not c.get("ongoing") and age > myd:
                        jobs.append((P_DIG, x, y, ("DIG",)))
                elif tl.get("animal"):
                    if not tl.get("fed_today"):
                        jobs.append((P_FEED, x, y, ("FEED",)))
                    if int(tl.get("yield_units", 0) or 0) > 0:
                        jobs.append((P_HARVEST, x, y, ("HARVEST",)))
                    if not tl.get("cared_today"):
                        jobs.append((P_CARE, x, y, ("CARE",)))
                    if tl.get("fertilizer_available"):
                        jobs.append((P_COLLECT, x, y, ("COLLECT_FERTILIZER",)))
                elif kind in ("PASTURE", "COOP"):
                    w = want_animal.get((x, y))
                    if w and w[0]:
                        jobs.append((P_PLACE, x, y, ("PLACE", w[0])))
                elif kind == "WEED":
                    jobs.append((P_DIG, x, y, ("DIG",)))
        return jobs

    # ---------------------------------------------------------- task plan
    def _plan(self, pos, job, inv, shed, n_feed):
        """Job -> step list, inserting shed prefetches as needed."""
        p, x, y, v = job
        steps = []
        if v[0] == "FEED" and int(inv.get("WHEAT", 0) or 0) <= 0:
            n = min(max(n_feed, 2), int(shed.get("WHEAT", 0) or 0), 6)
            if n <= 0:
                return None
            steps += [("GOSHED",), ("SHEDOP", "PICKUP", "WHEAT", n)]
        elif v[0] == "PLACE" and int(inv.get(v[1], 0) or 0) <= 0:
            if int(shed.get(v[1], 0) or 0) <= 0:
                return None
            steps += [("GOSHED",), ("SHEDOP", "PICKUP", v[1], 1)]
        steps += [("GOTO", x, y), ("DO",) + tuple(v)]
        return steps

    # ---------------------------------------------------------- turn
    def act(self, obs):
        seat = int(_g(obs, "player", 0) or 0)
        day = int(_g(obs, "day", 0) or 0)
        hour = int(_g(obs, "hour", 0) or 0)
        turn = day * 24 + hour
        farms = list(_g(obs, "farms", []) or [])
        farm = farms[seat] if len(farms) > seat else {}
        grid = list(_g(farm, "tiles", []) or [])
        private = _g(obs, "private", {}) or {}
        seeds = dict(_g(private, "seeds", {}) or {})
        shed = dict(_g(private, "shed", {}) or {})
        invs = list(_g(private, "inventories", []) or [])
        units = [_g(farm, "farmer", None)] + list(_g(farm, "hands", []) or [])
        carried = {}
        for iv in invs:
            if isinstance(iv, dict):
                for g, n in iv.items():
                    carried[g] = carried.get(g, 0) + int(n or 0)

        market = self._market_orders(turn, grid, shed, carried)
        target = self.bp["days"].get(str(min(day, 29))) or {}
        jobs = self._jobs(day, grid, target, seeds)

        # seed makeup valve at hour 3
        if hour == 3 and day < 26 and len(market) < 10:
            money = float(_g(farm, "money", 0) or 0)
            want = {}
            for x, y, crop in (target.get("plants") or []):
                if y < len(grid) and x < len(grid[y] or []) \
                        and grid[y][x] is None:
                    want[crop] = want.get(crop, 0) + 1
            for crop, n in sorted(want.items()):
                miss = n - int(seeds.get(crop, 0) or 0)
                cost = CROPS[crop]["seed"]
                if miss > 0 and money >= miss * cost + 300:
                    market.append(["BUY_SEED", crop, min(miss, 6)])
                    money -= min(miss, 6) * cost
            market = market[:10]

        n_feed = sum(1 for _p, _x, _y, v in jobs if v == ("FEED",))

        # zone assignment at day start: hands partitioned across quadrants
        # in proportion to each quadrant's open job count
        if hour == 0:
            qcount = {q: 0 for q in QUADS}
            for _p, x, y, v in jobs:
                qcount[_quad((x, y))] += 1
            n_units = sum(1 for u in units if u)
            busy = sum(qcount.values())
            want = {}
            for qn, c in qcount.items():
                want[qn] = int(round(c * n_units / busy)) if busy else 0
                if c > 0:
                    want[qn] = max(want[qn], 1)
            self.zone = {}
            order = sorted(QUADS, key=lambda qn: -want[qn])
            for i, u in enumerate(units):
                if not u:
                    continue
                pos = (int(u[0]), int(u[1]))
                # stay in current quadrant if it still wants hands
                cq = _quad(pos)
                if want.get(cq, 0) > 0:
                    self.zone[i] = cq
                    want[cq] -= 1
                    continue
                for qn in order:
                    if want[qn] > 0:
                        self.zone[i] = qn
                        want[qn] -= 1
                        break

        claimed = set()
        verbs = []
        for i, u in enumerate(units):
            if not u:
                verbs.append(["PASS"])
                continue
            pos = (int(u[0]), int(u[1]))
            inv = dict(invs[i]) if i < len(invs) and \
                isinstance(invs[i], dict) else {}
            load = sum(int(n or 0) for n in inv.values())

            q = self.q.setdefault(i, [])
            # discard a queue whose destination job vanished (done by other)
            if q:
                tail = [s for s in q if s[0] == "DO"]
                if tail:
                    dv = tail[-1][1]
                    dx, dy = q[-2][1], q[-2][2] if len(q) >= 2 \
                        and q[-2][0] == "GOTO" else (pos[0], pos[1])
                    if not any((v[0], x, y) == (dv, dx, dy)
                               for _p, x, y, v in jobs):
                        q.clear()
            if not q:
                # prefer a job underfoot, else nearest by (priority, dist),
                # restricted to the unit's zone while it has open work
                zn = self.zone.get(i)
                pool = jobs
                if zn:
                    zj = [j for j in jobs if _quad((j[1], j[2])) == zn]
                    if zj:
                        pool = zj
                best = None
                for p, x, y, v in pool:
                    if (v[0], x, y) in claimed:
                        continue
                    plan = self._plan(pos, (p, x, y, v), inv, shed, n_feed)
                    if plan is None:
                        continue
                    if pos == (x, y) and len(plan) == 2:
                        rank = (p - 1, 0)          # underfoot bonus
                    else:
                        rank = (p, _dist(pos, (x, y)))
                    if best is None or rank < best[0]:
                        best = (rank, plan, (v[0], x, y))
                if best is None:
                    if load >= 6 or (load > 0 and hour >= 20):
                        q.extend([("GOSHED",), ("SHEDOP", "DROP")])
                    else:
                        verbs.append(["PASS"])
                        continue
                else:
                    claimed.add(best[2])
                    q.extend(best[1])
            # execute head of queue
            s = q[0]
            if s[0] == "GOTO":
                mv = _toward(pos, (s[1], s[2]))
                if mv is None:
                    q.pop(0)
                    s = q[0] if q else None
                    if s is None or s[0] != "DO":
                        verbs.append(["PASS"])
                        continue
                else:
                    verbs.append(mv)
                    continue
            if s[0] == "GOSHED":
                if pos in SHED_TILES:
                    q.pop(0)
                    s = q[0] if q else None
                    if s is None or s[0] != "SHEDOP":
                        verbs.append(["PASS"])
                        continue
                else:
                    verbs.append(_toward(pos, _shed_gate(pos)) or ["PASS"])
                    continue
            verbs.append(list(s[1:]))
            q.pop(0)
        self.q = {i: t for i, t in self.q.items() if i < len(units)}
        return {"farmer": verbs[0] if verbs else ["PASS"],
                "hands": verbs[1:], "market": market}


def make_agent(bp):
    ex = Executor2(bp)
    return ex.act
