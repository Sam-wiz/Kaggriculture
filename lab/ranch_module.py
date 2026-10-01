"""Ranch module: demand-gated animal additions on the exclusive SE quadrant.

Composes with V48: appends a daily ranch hand (hired after the tape's hour-1
burst), buys SE land once after the tape's SW purchase, builds pastures on SE
tiles near the shed, places demand-matched animals, and services them daily
(feed/care/harvest/drop). The tape's own sell machinery sells the products.

Design constraints baked in:
- BUY_LAND only after day 11 (tape buys NE d6 + SW d11; ours is always SE).
- Ranch hand hired at hour >= 3 so it is the LAST hand index -> tape's ops
  for indices 0..k-1 are untouched; we append our op at the end.
- Products DROP to shared shed; tape's sells handle them. Shed overflow risk
  is real late-game -> we keep the herd small.
"""
import sys
sys.path.insert(0, ".")
import harness

SHED_TILES = [(4, 4), (5, 4), (4, 5), (5, 5)]

# SE-quadrant tiles nearest the shed (all in SE: x>=5,y>=5), ordered by
# distance from shed corner (5,5). (5,5) itself is a spawn tile -> skip it.
RANCH_TILES = [(6, 5), (5, 6), (6, 6), (7, 5), (5, 7), (6, 7), (7, 6),
               (8, 5), (5, 8), (7, 7), (8, 6), (6, 8)]

HIRE_HOUR = 6          # after tape's last hire (max observed hour 5): our
                       # hands must be the day's LAST spawns so the tape's
                       # positional hand ops never land on them
HIRE_UNTIL = 12        # retry window if the market list was full at hour 6
LAND_DAY = 11          # buy SE right after tape's day-11 SW purchase (hour>1)
MIN_MONEY = 9000       # keep a buffer so tape purchases never starve
MAX_RANCH_ANIMALS = 8  # two hands service ~8 on a compact grid
MIN_ANIMALS = 4        # engage only when the herd justifies fixed costs


def _demand_mix(shops):
    """Choose animal counts from the revealed shop demand."""
    n_yarn = shops.count("YARN_STORE")
    n_milk = sum(shops.count(s) for s in
                 ("PIZZA_SHOP", "ICE_CREAM_SHOP", "SMOOTHIE_SHOP"))
    n_egg = sum(shops.count(s) for s in ("BAKERY", "BRUNCH_SPOT"))
    want = {}
    if n_yarn:
        want["SHEEP"] = min(5, 2 + 2 * n_yarn)
    if n_milk >= 2:
        want["COW"] = min(4, n_milk)
    if n_egg >= 2:
        want["GOOSE"] = min(3, n_egg)
    if not want:
        want = {"SHEEP": 0, "COW": 0, "GOOSE": 0}
    total = sum(want.values())
    while total > MAX_RANCH_ANIMALS:
        for a in sorted(want, key=lambda k: -want[k]):
            if want[a] > 0 and total > MAX_RANCH_ANIMALS:
                want[a] -= 1
                total -= 1
    return want


STRUCT = {"SHEEP": "PASTURE", "COW": "PASTURE", "GOOSE": "COOP"}
BUY_UNTIL_DAY = 18       # sheep first-yield ~d+6; later buys never pay back
PICKUP_UNTIL = 17      # hand inv vanishes at day end; leave travel margin
HOME_HOUR = 20         # must be shed-adjacent and empty-handed by day end


class Ranch:
    def __init__(self):
        self.reset()

    def reset(self):
        self.want = None          # demand-chosen animal counts
        self.our_hands = []       # indices of our hired hands in farm.hands
        self.hires_emitted = 0    # HIRE ops we appended today
        self.expect_hand = None   # hand count at emit; ours spawn next obs
        self.struct_plan = {}     # tile -> animal type assigned to structure
        self.unusable = set()     # SE tiles blocked by something we can't use
        self.bought = {}          # animal -> count bought (our market buys only)
        self.lost = {}            # animal -> count escaped/died after placement
        self._prev_placed = {}    # animal -> count seen on our tiles last step
        self.harvested = {}       # product -> total units our hands harvested
        self.sold = {}            # product -> units we emitted SELL for
        self.land_done = False
        self.day = -1
        self._svc_seen = None

    def step(self, obs, action):
        player = obs["player"]
        me = obs["farms"][player]
        tiles = me["tiles"]
        day = obs["day"]
        hour = obs["hour"]
        money = me["money"]
        shops = obs["town"]["unlocked_shops"]
        shed = obs["private"]["shed"]
        invs = obs["private"]["inventories"]
        hands = me["hands"]
        market = action.setdefault("market", [])
        if market is None:
            market = []
            action["market"] = market
        hacts = action.setdefault("hands", [])

        if day != self.day:
            self.day = day
            self.our_hands = []
            self.hires_emitted = 0
            self.expect_hand = None

        if self.want is None and day >= 9:
            self.want = _demand_mix(shops)

        want_total = sum(self.want.values()) if self.want else 0
        active = want_total >= MIN_ANIMALS  # below this the fixed land+hand
                                            # costs can't amortize: stay stock

        # --- market: land purchase (once, after day-11 hour-1 SW buy) ------
        if (not self.land_done and active
                and (day > LAND_DAY or (day == LAND_DAY and hour >= 2))
                and "SE" not in me["unlocked_quadrants"] and money >= MIN_MONEY):
            market.append(["BUY_LAND"])
            self.land_done = True

        # --- market: daily hires (after tape's last hire; retry if full) ---
        n_hires = 2 if want_total > 4 else 1
        if (self.land_done and active
                and HIRE_HOUR <= hour <= HIRE_UNTIL
                and self.expect_hand is None and not self.our_hands
                and money >= MIN_MONEY and len(market) < 10 - n_hires):
            for _ in range(n_hires):
                market.append(["HIRE"])
            self.hires_emitted = n_hires
            self.expect_hand = len(hands)

        # --- market: animal buys (setup window only) ------------------------
        if active and self.land_done and day <= BUY_UNTIL_DAY:
            for a, n in self.want.items():
                have = self.bought.get(a, 0)
                cost = {"SHEEP": 500, "COW": 400, "GOOSE": 300}[a]
                if have < n and money >= MIN_MONEY + cost \
                        and len(market) < 10:
                    market.append(["BUY_ANIMAL", a, 1])
                    self.bought[a] = self.bought.get(a, 0) + 1
                    money -= cost

        # --- market: emergency wheat for feed (shed empty) ------------------
        if (self.struct_plan and shed.get("WHEAT", 0) == 0
                and money >= MIN_MONEY and len(market) < 10):
            market.append(["BUY_PRODUCT", "WHEAT", 10])

        # --- market: drain our own products promptly -----------------------
        # The tape accumulates shed stock for its scheduled sells; our goods
        # sitting in the shed steal its headroom and trigger cap discards of
        # ITS premiums on peak days. Sell our output ourselves, bounded to
        # our net production so we never dump the tape's stock early.
        if active and self.struct_plan:
            shed_total = sum(shed.values())
            if shed_total > 70 or obs["day"] >= 22:
                prods = {"SHEEP": "WOOL", "COW": "MILK", "GOOSE": "EGG"}
                for a in self.want:
                    p = prods[a]
                    unsold = self.harvested.get(p, 0) - self.sold.get(p, 0)
                    n = min(shed.get(p, 0), unsold, 8)
                    if n > 0 and len(market) < 10:
                        market.append(["SELL", p, n])
                        self.sold[p] = self.sold.get(p, 0) + n

        # --- our hand indices (last spawns are ours: our ops processed last) -
        if self.expect_hand is not None:
            if len(hands) > self.expect_hand:
                n_spawned = min(self.hires_emitted, len(hands) - self.expect_hand)
                self.our_hands = list(range(len(hands) - n_spawned, len(hands)))
                self.expect_hand = None
            elif hour > HIRE_HOUR:
                # our hires were dropped (shouldn't happen: market gated) ->
                # allow a retry next hour
                self.expect_hand = None

        # --- drive our hands --------------------------------------------------
        for rank, idx in enumerate(self.our_hands):
            if idx >= len(hands):
                continue
            while len(hacts) <= idx:
                hacts.append(["PASS"])
            if hacts[idx] == ["PASS"]:
                hacts[idx] = self._hand_op(obs, idx, rank, len(self.our_hands))

    def _needed_struct(self):
        for a, n in (self.want or {}).items():
            if sum(1 for x in self.struct_plan.values() if x == a) < n:
                return a
        return None

    def _needed_for_kind(self, kind):
        for a, n in (self.want or {}).items():
            if STRUCT[a] == kind and \
                    sum(1 for x in self.struct_plan.values() if x == a) < n:
                return a
        return None

    def _hand_op(self, obs, idx, rank=0, nparts=1):
        me = obs["farms"][obs["player"]]
        tiles = me["tiles"]
        hx, hy = me["hands"][idx]
        hour = obs["hour"]
        inv = obs["private"]["inventories"][idx + 1] \
            if idx + 1 < len(obs["private"]["inventories"]) else {}
        shed = obs["private"]["shed"]

        def toward(p):
            x, y = p
            if hx < x: return ["EAST"]
            if hx > x: return ["WEST"]
            if hy < y: return ["SOUTH"]
            if hy > y: return ["NORTH"]
            return None

        at_shed = (hx, hy) in SHED_TILES

        # live view of our ranch tiles + escape tracking (once per step)
        placed, empty_struct = {}, []
        for t, a in self.struct_plan.items():
            tile = tiles[t[1]][t[0]]
            if isinstance(tile, dict) and tile.get("kind") == STRUCT[a]:
                if "animal" in tile:
                    placed[t] = a
                else:
                    empty_struct.append(t)
        if self._svc_seen != (obs["day"], hour):
            self._svc_seen = (obs["day"], hour)
            for a in STRUCT:
                prev = self._prev_placed.get(a, 0)
                cur = sum(1 for x in placed.values() if x == a)
                if cur < prev:
                    self.lost[a] = self.lost.get(a, 0) + prev - cur
                self._prev_placed[a] = cur

            # adopt structures we built into the plan
            for t in RANCH_TILES:
                if t in self.struct_plan or t in self.unusable:
                    continue
                tile = tiles[t[1]][t[0]]
                if isinstance(tile, dict) and "animal" not in tile \
                        and tile.get("kind") in ("PASTURE", "COOP"):
                    need = self._needed_for_kind(tile["kind"])
                    if need:
                        self.struct_plan[t] = need
                        if "animal" in tile:
                            placed[t] = need
                        else:
                            empty_struct.append(t)

        # partition this hand's share of the tiles (round-robin)
        my_placed = {t: a for i, (t, a) in enumerate(sorted(placed.items()))
                     if i % nparts == rank}
        my_empty = [t for i, t in enumerate(sorted(empty_struct))
                    if i % nparts == rank]

        carried_kinds = [k for k in inv if k in STRUCT]

        # carried animals are perishable cargo (inv vanishes overnight):
        # place before anything else
        for a in carried_kinds:
            for t in empty_struct:
                if self.struct_plan[t] == a:
                    if (hx, hy) != t:
                        return toward(t)
                    return ["PLACE", a]

        # day-end rescue: hand inventory vanishes overnight -- drop only if
        # the shared shed has room; better our goods vanish than the tape's
        # premium drops get discarded at cap
        if hour >= HOME_HOUR:
            if not at_shed:
                return toward(self._nearest_shed(hx, hy))
            if inv and sum(shed.values()) + sum(inv.values()) <= 95:
                return ["DROP"]
            return ["PASS"]

        # phase 1: FEED first -- placed animals escape after 2 unfed days
        unfed = [t for t in my_placed
                 if not tiles[t[1]][t[0]]["fed_today"]]
        if unfed:
            if inv.get("WHEAT", 0) == 0:
                if not at_shed:
                    return toward(self._nearest_shed(hx, hy))
                if shed.get("WHEAT", 0) > 0:
                    need_w = len(unfed) + 2
                    return ["PICKUP", "WHEAT", min(need_w, shed["WHEAT"])]
                # no wheat anywhere: fall through to care/harvest
            else:
                t = unfed[0]
                if (hx, hy) != t:
                    return toward(t)
                return ["FEED"]

        # phase 2: build structures the demand mix still needs
        need = self._needed_struct()
        if need:
            candidates = [t for i, t in enumerate(RANCH_TILES)
                          if i % nparts == rank]
            for t in candidates:
                if t in self.struct_plan or t in self.unusable:
                    continue
                tile = tiles[t[1]][t[0]]
                if tile is None:
                    if (hx, hy) != t:
                        return toward(t)
                    return ["BUILD_" + STRUCT[need]]
                if isinstance(tile, dict) and tile.get("kind") == "WEED":
                    if (hx, hy) != t:
                        return toward(t)
                    return ["DIG"]
                if not (isinstance(tile, dict)
                        and tile.get("kind") in ("PASTURE", "COOP")
                        and "animal" not in tile):
                    self.unusable.add(t)
                # adoptable empty structures get claimed above next pass

        # phase 3: fetch + place bought animals on this hand's empties
        for t in my_empty:
            a = self.struct_plan[t]
            # entitlement guards against draining the tape's shed stock:
            # ours still in shed = bought - on tiles - carried - escaped
            carried = sum(
                obs["private"]["inventories"][i + 1].get(a, 0)
                for i in self.our_hands
                if i + 1 < len(obs["private"]["inventories"]))
            in_shed_owed = self.bought.get(a, 0) \
                - sum(1 for x in placed.values() if x == a) \
                - carried - self.lost.get(a, 0)
            if in_shed_owed > 0 and shed.get(a, 0) > 0 and hour <= PICKUP_UNTIL:
                if not at_shed:
                    return toward(self._nearest_shed(hx, hy))
                return ["PICKUP", a, 1]

        # phase 4: care / harvest on this hand's placed tiles
        # (no COLLECT_FERTILIZER: it fills the shared shed for little value)
        for t, a in my_placed.items():
            tile = tiles[t[1]][t[0]]
            needs = not tile["cared_today"] \
                or tile.get("yield_units", 0) > 0
            if not needs:
                continue
            if (hx, hy) != t:
                return toward(t)
            if not tile["cared_today"]:
                return ["CARE"]
            if tile.get("yield_units", 0) > 0:
                prod = {"SHEEP": "WOOL", "COW": "MILK", "GOOSE": "EGG"}[a]
                self.harvested[prod] = self.harvested.get(prod, 0) \
                    + tile["yield_units"]
                return ["HARVEST"]

        # phase 5: patrol SE weeds -- unlocked SE spawns weeds that the tape's
        # weed_repair sends its units to dig; we dig them first so the tape
        # never wastes trips on our quadrant (split by hand rank)
        for y in range(5, 10):
            for x in range(5, 10):
                if (x + y) % nparts != rank:
                    continue
                t = tiles[y][x]
                if isinstance(t, dict) and t.get("kind") == "WEED":
                    if (hx, hy) != (x, y):
                        return toward((x, y))
                    return ["DIG"]

        # done for now: dump products so nothing rides overnight in inv --
        # but never push the shared shed over ~95: at 100 the tape's own
        # harvest drops get discarded, which costs far more than our goods
        shed_total = sum(shed.values())
        if shed_total + sum(inv.values()) <= 95:
            if not at_shed:
                return toward(self._nearest_shed(hx, hy))
            if any(k != "WHEAT" for k in inv):
                return ["DROP"]
        return ["PASS"]

    @staticmethod
    def _nearest_shed(hx, hy):
        return min(SHED_TILES, key=lambda p: abs(p[0] - hx) + abs(p[1] - hy))


_RANCHES = {}


def make_wrapped(base_agent):
    def agent(observation, configuration=None):
        action = base_agent(observation, configuration)
        if not isinstance(action, dict):
            return action
        player = observation.get("player", 0)
        step = observation.get("step", 0)
        key = player
        if key not in _RANCHES or step == 0:
            _RANCHES[key] = Ranch()
        _RANCHES[key].step(observation, action)
        return action
    return agent


if __name__ == "__main__":
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "v48", "rivals/ahmedberatozer_kaggriculture-v48-clear-the-queue/_entry.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    base = [v for v in vars(m).values() if callable(v)][-1]
    wrapped = make_wrapped(base)
    r = harness.run_episode(wrapped, "pass", seed=6000, catch_errors=True)
    print("reward", r["reward"])
