"""Executor v3: row-walker. Pre-partitioned daily tours, not dispatch.

At hour 0 every serviceable tile is sorted into a serpentine route per
quadrant and chunked across the day's hands. A unit then walks its route
once, doing whatever each stop needs (water, harvest, plant, feed...).
One dedicated unit runs the animal circuit with a wheat prefetch.
Idle units fall back to a global job list (weeds, builds, shed runs).

Tile needs are re-evaluated at each stop, so the tour survives partial
execution and day-boundary drift.
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


def _quad(pos):
    return ("N" if pos[1] < 5 else "S") + ("W" if pos[0] < 5 else "E")


QUADS = {"NW": (0, 0), "NE": (5, 0), "SW": (0, 5), "SE": (5, 5)}


class Executor3:
    def __init__(self, bp):
        self.bp = bp
        self.goal = dict((bp.get("meta") or {}).get("herd_goal") or {})
        self.tour = {}       # unit index -> [(x,y)]
        self.tpos = {}       # unit index -> int
        self.fbt = {}        # unit index -> sticky fallback target
        self.day = -1

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

    # ---------------------------------------------------------- tile needs
    def _tile_need(self, tl, pos, day, want_plant, want_animal):
        """Ordered list of ops this tile needs now."""
        x, y = pos
        ops = []
        if tl is None:
            if pos in want_plant:
                ops.append(("PLANT", want_plant[pos]))
            elif pos in want_animal and want_animal[pos][1]:
                s = want_animal[pos][1]
                ops.append(("BUILD_COOP",) if s == "COOP"
                           else ("BUILD_PASTURE",))
            return ops
        if not isinstance(tl, dict):
            return ops
        kind = tl.get("kind")
        if kind == "PLANT":
            crop = tl.get("crop")
            c = CROPS.get(crop) or {}
            age = day - int(tl.get("planted_day") or day)
            yu = int(tl.get("yield_units", 0) or 0)
            myd = c.get("max_yield_day", 99)
            ripe = (yu >= c.get("max_yield", 99) or age > myd
                    or (age == myd and tl.get("watered_today")))
            can = age >= c.get("first_yield_day", 0)
            if not tl.get("watered_today"):
                ops.append(("WATER",))
            if yu > 0 and can and (c.get("ongoing") or ripe):
                ops.append(("HARVEST",))
            # FERTILIZE: ongoing crops while producing, one-time crops in
            # their bonus window; cheapest last so real work goes first
            fertilized = int(tl.get("fertilized_until_day") or 0) > day
            if not fertilized:
                if c.get("ongoing") and can:
                    ops.append(("FERTILIZE",))
                elif not c.get("ongoing") and not ripe \
                        and age >= (myd + 1) // 2:
                    ops.append(("FERTILIZE",))
            if yu == 0 and not c.get("ongoing") and age > myd:
                ops = [("DIG",)]
        elif tl.get("animal"):
            if not tl.get("fed_today"):
                ops.append(("FEED",))
            if int(tl.get("yield_units", 0) or 0) > 0:
                ops.append(("HARVEST",))
            if not tl.get("cared_today"):
                ops.append(("CARE",))
            if tl.get("fertilizer_available"):
                ops.append(("COLLECT_FERTILIZER",))
        elif kind in ("PASTURE", "COOP"):
            w = want_animal.get(pos)
            if w and w[0]:
                ops.append(("PLACE", w[0]))
        elif kind == "WEED":
            ops.append(("DIG",))
        return ops

    # ---------------------------------------------------------- day plan
    def _build_tours(self, day, grid, target, n_units):
        want_plant = {(x, y): c for x, y, c in (target.get("plants") or [])}
        want_animal = {(x, y): (k, s) for x, y, k, s
                       in (target.get("animals") or [])}
        for x, y, s in (target.get("buildings") or []):
            want_animal.setdefault((x, y), (None, s))

        animal_tiles = []
        crop_tiles = []
        misc = []
        for y, row in enumerate(grid):
            for x, tl in enumerate(row):
                if tl == "LOCKED":
                    continue
                pos = (x, y)
                if isinstance(tl, dict) and (tl.get("animal")
                                           or tl.get("kind") in
                                           ("PASTURE", "COOP")):
                    animal_tiles.append(pos)
                elif pos in want_plant or pos in want_animal \
                        or (isinstance(tl, dict) and tl.get("kind")
                            in ("PLANT", "WEED")):
                    crop_tiles.append(pos)
        # serpentine per quadrant, oriented to END at the shed corner so
        # the post-route DROP is free (walk far edge -> shed corner)
        shed_corner = {"NW": (4, 4), "NE": (5, 4), "SW": (4, 5),
                       "SE": (5, 5)}

        def skey(pos):
            x, y = pos
            q = _quad(pos)
            scx, scy = shed_corner[q]
            x0, y0 = QUADS[q]
            # row order: farthest row from the shed row first
            r = -abs(y - scy)
            # within row r (0=farthest): snake; last row must travel
            # toward the shed column
            ridx = 4 - abs(y - scy)
            flip = 1 if scx == x0 else 0      # shed on min-x side
            col = x if (ridx + flip) % 2 == 0 else -x
            return (q, r, col)
        crop_tiles.sort(key=skey)
        animal_tiles.sort(key=lambda p: (skey(p),
                                         -_dist(p, shed_corner[_quad(p)])))

        # routes: animal circuits chunked to ~5 stops (each stop costs
        # ~4 ops: feed+care+harvest+collect), then crop chunks of ~8;
        # units claim chunks as they spawn
        routes = []
        for h in range(0, len(animal_tiles), 5):
            routes.append(animal_tiles[h:h + 5])
        per = 8
        for h in range(0, len(crop_tiles), per):
            routes.append(crop_tiles[h:h + per])
        return routes, want_plant, want_animal

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

        if day != self.day:
            self.routes, self._wp, self._wa = self._build_tours(
                day, grid, target, len(units))
            self.claimed = set()
            self.route_of = {}
            self.tpos = {}
            self.fbt = {}
            self.day = day
        want_plant, want_animal = self._wp, self._wa

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

        verbs = []
        for i, u in enumerate(units):
            if not u:
                verbs.append(["PASS"])
                continue
            pos = (int(u[0]), int(u[1]))
            inv = dict(invs[i]) if i < len(invs) and \
                isinstance(invs[i], dict) else {}
            wheat = int(inv.get("WHEAT", 0) or 0)
            load = sum(int(n or 0) for n in inv.values())
            # claim a route if we don't hold one
            ri = self.route_of.get(i)
            if ri is None:
                for k in range(len(self.routes)):
                    if k not in self.claimed:
                        ri = k
                        self.route_of[i] = k
                        self.claimed.add(k)
                        self.tpos[i] = 0
                        break
            tour = self.routes[ri] if ri is not None else []
            tp = self.tpos.get(i, 0)

            # prefetch: scan the remaining tour for inventory-gated ops
            # (FEED needs wheat, PLACE needs the animal) and detour to the
            # shed once, grabbing everything the rest of the route needs.
            # A heavy load also sends the unit home to DROP first.
            if tour and tp < len(tour):
                need = {}
                for t2 in tour[tp:]:
                    tl = grid[t2[1]][t2[0]] if t2[1] < len(grid) else None
                    for op in self._tile_need(tl, t2, day,
                                              want_plant, want_animal):
                        if op[0] == "FEED":
                            need["WHEAT"] = need.get("WHEAT", 0) + 1
                        elif op[0] == "PLACE":
                            need[op[1]] = need.get(op[1], 0) + 1
                        elif op[0] == "FERTILIZE":
                            need["FERTILIZER"] = need.get("FERTILIZER", 0) + 1
                want_fetch = {}
                for item, n in need.items():
                    have = int(inv.get(item, 0) or 0)
                    if n > have and int(shed.get(item, 0) or 0) > have:
                        want_fetch[item] = min(n, int(shed.get(item, 0) or 0)) - have
                # junk = carried goods the route doesn't need (harvests);
                # needed items already carried are cargo, keep them
                cargo = sum(min(int(inv.get(it, 0) or 0), n)
                            for it, n in need.items())
                junk = load - cargo
                if want_fetch or junk >= 5 or (junk > 0 and hour >= 21):
                    if pos in SHED_TILES:
                        if junk > 0:
                            verbs.append(["DROP"])
                        elif want_fetch:
                            item = next(iter(want_fetch))
                            verbs.append(["PICKUP", item, want_fetch[item]])
                        else:
                            verbs.append(["PASS"])
                    else:
                        verbs.append(_toward(pos, _shed_gate(pos)) or ["PASS"])
                    continue

            # advance past satisfied stops
            while tp < len(tour):
                x, y = tour[tp]
                tl = grid[y][x] if y < len(grid) and x < len(grid[y]) else None
                needs = self._tile_need(tl, (x, y), day,
                                        want_plant, want_animal)
                # filter needs by feasibility
                feas = []
                for op in needs:
                    if op[0] == "PLANT" and \
                            int(seeds.get(op[1], 0) or 0) <= 0:
                        continue
                    if op[0] == "FEED" and wheat <= 0:
                        continue
                    if op[0] == "PLACE" and \
                            int(inv.get(op[1], 0) or 0) <= 0:
                        continue
                    if op[0] == "FERTILIZE" and \
                            int(inv.get("FERTILIZER", 0) or 0) <= 0:
                        continue
                    feas.append(op)
                if feas:
                    break
                tp += 1
            self.tpos[i] = tp

            if tp >= len(tour):
                # route done: release it; then opportunistic work — nearest
                # outstanding need anywhere (weeds, ripened crops, strays)
                if ri is not None:
                    self.claimed.discard(ri)
                    self.route_of.pop(i, None)
                if load >= 6 or (load > 0 and hour >= 20):
                    if pos in SHED_TILES:
                        verbs.append(["DROP"])
                    else:
                        verbs.append(_toward(pos, _shed_gate(pos)) or ["PASS"])
                    continue
                # fallback dispatch over the whole board — sticky: keep the
                # unit's last fallback target while it still needs work
                ft = self.fbt.get(i)
                def need_at(xx, yy):
                    tl = grid[yy][xx] if yy < len(grid) \
                        and xx < len(grid[yy]) else None
                    return [op for op in self._tile_need(
                                tl, (xx, yy), day, want_plant, want_animal)
                            if not (op[0] == "PLANT" and
                                    int(seeds.get(op[1], 0) or 0) <= 0)
                            and not (op[0] == "FEED" and wheat <= 0)
                            and not (op[0] == "PLACE" and
                                     int(inv.get(op[1], 0) or 0) <= 0)
                            and not (op[0] == "FERTILIZE" and
                                     int(inv.get("FERTILIZER", 0) or 0) <= 0)]
                if ft is not None:
                    fx, fy, fop = ft
                    if fop in need_at(fx, fy):
                        if pos == (fx, fy):
                            verbs.append(list(fop))
                        else:
                            verbs.append(_toward(pos, (fx, fy)) or ["PASS"])
                        continue
                    self.fbt.pop(i, None)
                best = None
                for yy, row in enumerate(grid):
                    for xx, tl in enumerate(row):
                        if tl == "LOCKED":
                            continue
                        feas = need_at(xx, yy)
                        if not feas:
                            continue
                        rank = (0 if feas[0][0] in ("WATER", "FEED")
                                else 1, _dist(pos, (xx, yy)))
                        if best is None or rank < best[0]:
                            best = (rank, (xx, yy), feas[0])
                if best is None:
                    if load > 0:
                        if pos in SHED_TILES:
                            verbs.append(["DROP"])
                        else:
                            verbs.append(_toward(pos, _shed_gate(pos))
                                         or ["PASS"])
                    else:
                        verbs.append(["PASS"])
                    continue
                _, (xx, yy), op = best
                if pos == (xx, yy):
                    verbs.append(list(op))
                else:
                    self.fbt[i] = (xx, yy, op)
                    verbs.append(_toward(pos, (xx, yy)) or ["PASS"])
                continue

            x, y = tour[tp]
            if pos == (x, y):
                tl = grid[y][x]
                needs = self._tile_need(tl, (x, y), day,
                                        want_plant, want_animal)
                feas = [op for op in needs
                        if not (op[0] == "PLANT"
                                and int(seeds.get(op[1], 0) or 0) <= 0)
                        and not (op[0] == "FEED" and wheat <= 0)
                        and not (op[0] == "PLACE"
                                 and int(inv.get(op[1], 0) or 0) <= 0)
                        and not (op[0] == "FERTILIZE"
                                 and int(inv.get("FERTILIZER", 0) or 0) <= 0)]
                if feas:
                    verbs.append(list(feas[0]))
                else:
                    self.tpos[i] = tp + 1
                    verbs.append(["PASS"])
            else:
                verbs.append(_toward(pos, (x, y)) or ["PASS"])
        return {"farmer": verbs[0] if verbs else ["PASS"],
                "hands": verbs[1:], "market": market}


def make_agent(bp):
    ex = Executor3(bp)
    return ex.act
