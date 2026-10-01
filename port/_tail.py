

# --------------------------------------------------------------------------
# Tape decoding (policy.cpp::decode_action)
# --------------------------------------------------------------------------
def _i16(value):
    """static_cast<std::int16_t>."""
    value &= 0xFFFF
    return value - 0x10000 if value >= 0x8000 else value


def _u8(value):
    """static_cast<std::uint8_t>."""
    return value & 0xFF


def _decode_action(encoded):
    values = [int(token) for token in encoded.split()]
    if len(values) < 2:
        raise RuntimeError("invalid encoded tape action counts")
    n_units, n_orders = values[0], values[1]
    if not (0 <= n_units <= MAX_UNITS) or not (0 <= n_orders <= 16):
        raise RuntimeError("invalid encoded tape action counts")
    cursor = 2
    units = []
    for _ in range(n_units):
        op, arg, quantity = values[cursor], values[cursor + 1], values[cursor + 2]
        cursor += 3
        units.append((_u8(op), _u8(arg), _i16(quantity)))
    orders = []
    for _ in range(n_orders):
        op, item, quantity = values[cursor], values[cursor + 1], values[cursor + 2]
        cursor += 3
        orders.append((_u8(op), _u8(item), quantity))
    if cursor != len(values):
        raise RuntimeError("trailing encoded tape value")
    return (n_units, units, n_orders, orders)


# kag::Action{} -- the value-initialised default: one unit, {OP_PASS, 0, 1}.
_DEFAULT_ACTION = (1, [(0, 0, 1)], 0, [])


def _load_tapes():
    text = zlib.decompress(base64.b85decode(_TAPE_B85)).decode("ascii")
    routes = text.split("\x00")
    if len(routes) != K_ROUTES:
        raise RuntimeError("tape blob route count mismatch")
    tapes = []
    for route in routes:
        lines = route.split("\n")
        if len(lines) != K_TURNS:
            raise RuntimeError("tape blob turn count mismatch")
        tapes.append([_decode_action(line) for line in lines])
    return tapes


_TAPES = _load_tapes()


# --------------------------------------------------------------------------
# sim.hpp helpers
# --------------------------------------------------------------------------
def _fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def _is_animal(item):
    return GOOSE <= item < N_ITEMS


# --------------------------------------------------------------------------
# _entry.py observation reader.  The native build packed the whole observation
# into a C struct; the policy only ever reads the fields extracted here.
# --------------------------------------------------------------------------
def _read(value, key, default=None):
    if isinstance(value, Mapping):
        return value.get(key, default)
    getter = getattr(value, "get", None)
    if callable(getter):
        return getter(key, default)
    return getattr(value, key, default)


def _count(mapping, name):
    """_fill_counts, one entry."""
    if not mapping:
        return 0
    return int(_read(mapping, name, 0) or 0)


def _packed_tile_kind_and_animal(tile):
    """_entry.py::_fill_tile -> (kind, has_animal, what)."""
    if tile is None:
        return 0, False, 0
    if isinstance(tile, str):
        return _KIND_ID.get(tile, 0), False, 0
    kind = _read(tile, "kind")
    crop = _read(tile, "crop")
    animal = _read(tile, "animal")
    if kind == "PLANT" or crop:
        return _KIND_ID["PLANT"], False, (_ITEM_ID[str(crop)] if crop else 0)
    if animal is not None:
        return _KIND_ID.get(kind, _KIND_ID["PASTURE"]), True, _ITEM_ID[str(animal)]
    return _KIND_ID.get(kind, 0), False, 0


class _StateView(object):
    """The subset of kag::State that this policy actually consults."""

    __slots__ = ("step", "n_shops", "shops", "prices", "money", "n_quadrants",
                 "hires_today", "shed", "n_units", "inv", "rival_tiles")

    def __init__(self, observation, seat):
        step = int(_read(observation, "step", 0) or 0)
        self.step = step

        market = _read(observation, "market", {}) or {}
        price_map = _read(market, "prices", {}) or {}
        self.prices = [_count(price_map, name) for name in _PRODUCTS]

        town = _read(observation, "town", {}) or {}
        shops = list(_read(town, "unlocked_shops", []) or [])
        n_shops = min(len(shops), MAX_SHOP_INSTANCES)
        self.n_shops = max(0, min(n_shops, MAX_SHOP_INSTANCES))
        self.shops = [_SHOP_ID[str(shop)] for shop in shops[:MAX_SHOP_INSTANCES]]

        farms = list(_read(observation, "farms", []) or [])
        if len(farms) != 2:
            raise ValueError("ShopForge needs exactly two public farms")

        own = farms[seat]
        self.money = float(_read(own, "money", 0) or 0)
        positions = [_read(own, "farmer", [0, 0]), *list(_read(own, "hands", []) or [])]
        self.n_units = max(1, min(len(positions), MAX_UNITS))
        self.n_quadrants = max(0, min(
            len(list(_read(own, "unlocked_quadrants", []) or [])), 4))
        self.hires_today = int(_read(own, "hires_today", 0) or 0)

        private = _read(observation, "private", {}) or {}
        shed_map = _read(private, "shed", {}) or {}
        self.shed = [_i16(_count(shed_map, name)) for name in _ITEMS]
        inventories = list(_read(private, "inventories", []) or [])
        self.inv = [
            [_i16(_count(carried or {}, name)) for name in _ITEMS]
            for carried in inventories[:MAX_UNITS]
        ]

        self.rival_tiles = farms[1 - seat]

    # policy.cpp::animal_tiles
    def rival_animal_tiles(self, animal):
        result = 0
        rows = list(_read(self.rival_tiles, "tiles", []) or [])
        for row in rows[:BOARD]:
            for tile in list(row or [])[:BOARD]:
                kind, has_animal, what = _packed_tile_kind_and_animal(tile)
                if (kind == T_COOP or kind == T_PASTURE) and has_animal and what == animal:
                    result += 1
        return result

    # six_day_budget_guard.hpp::owned_in_hands
    def owned_in_hands(self, item):
        result = 0
        for unit in range(min(self.n_units, MAX_UNITS)):
            if unit < len(self.inv):
                result += max(0, self.inv[unit][item])
        return result


# --------------------------------------------------------------------------
# policy.cpp::choose_observed_tail
# --------------------------------------------------------------------------
def _choose_observed_tail(state):
    if (state.n_shops < 3 or
            state.shops[0] != SHOP_ICE_CREAM_SHOP or
            state.shops[1] != SHOP_FARMERS_MARKET or
            state.shops[2] != SHOP_FARMERS_MARKET):
        return False
    return float(state.rival_animal_tiles(GOOSE)) > 1


# --------------------------------------------------------------------------
# six_day_budget_guard.hpp::calculate_six_day_requirements
# --------------------------------------------------------------------------
def _planned_quantity(quantity):
    return max(1, quantity)


def _calculate_six_day_requirements(state, tape, start, end):
    purchase_budget = 0.0
    starting_seeds = [0] * N_CROPS
    starting_items = [0] * N_ITEMS
    seed_balance = [0] * N_CROPS
    item_balance = [0] * N_ITEMS
    hires_by_day = [0] * 6
    quadrants = state.n_quadrants

    for step in range(start, end):
        n_units, units, n_orders, orders = (
            tape[step] if 0 <= step < K_TURNS else _DEFAULT_ACTION)
        for index in range(n_units):
            op, arg, n = units[index]
            quantity = _planned_quantity(n)
            if op == OP_PLANT and arg < N_CROPS:
                seed_balance[arg] -= 1
                if -seed_balance[arg] > starting_seeds[arg]:
                    starting_seeds[arg] = -seed_balance[arg]
            elif op == OP_FEED:
                item_balance[WHEAT] -= 1
                if -item_balance[WHEAT] > starting_items[WHEAT]:
                    starting_items[WHEAT] = -item_balance[WHEAT]
            elif op == OP_FERTILIZE:
                item_balance[FERTILIZER] -= 1
                if -item_balance[FERTILIZER] > starting_items[FERTILIZER]:
                    starting_items[FERTILIZER] = -item_balance[FERTILIZER]
            elif op == OP_PLACE and arg < N_ITEMS:
                item_balance[arg] -= quantity
                if -item_balance[arg] > starting_items[arg]:
                    starting_items[arg] = -item_balance[arg]
        for index in range(n_orders):
            op, item, n = orders[index]
            quantity = _planned_quantity(n)
            if op == M_HIRE:
                day = min(5, max(0, (step - start) // 24))
                hires_by_day[day] += 1
            elif op == M_BUY_LAND:
                extra = quadrants - 1
                if 0 <= extra < 3:
                    purchase_budget += LAND_PRICES[extra]
                    quadrants += 1
            elif op == M_BUY_SEED and item < N_CROPS:
                purchase_budget += CROP_SEED_COST[item] * quantity
                seed_balance[item] += quantity
            elif op == M_BUY_PRODUCT and (item == WHEAT or item == FERTILIZER):
                purchase_budget += state.prices[item] * quantity
                item_balance[item] += quantity
            elif op == M_BUY_ANIMAL and _is_animal(item):
                purchase_budget += ANIMAL_COST[item - GOOSE] * quantity
                item_balance[item] += quantity

    for day in range(len(hires_by_day)):
        first_hire = state.hires_today if day == 0 else 0
        for index in range(hires_by_day[day]):
            purchase_budget += CFG_HIRE_MULT * _fib(first_hire + index)

    return purchase_budget, starting_seeds, starting_items


# --------------------------------------------------------------------------
# six_day_budget_guard.hpp::apply_six_day_budget_guard
# --------------------------------------------------------------------------
def _existing_sale(orders, n_orders, item):
    result = 0
    for index in range(n_orders):
        op, order_item, n = orders[index]
        if op == M_SELL and order_item == item and n > 0:
            result += n
    return result


def _add_budget_sale(orders, item, quantity):
    """Returns (ok, new_n_orders); mutates ``orders`` in place."""
    if quantity <= 0:
        return True
    for index in range(len(orders)):
        op, order_item, n = orders[index]
        if op == M_SELL and order_item == item:
            orders[index] = (op, order_item, n + quantity)
            return True
    limit = max(0, min(16, CFG_MAX_ORDERS))
    if len(orders) >= limit:
        return False
    orders.append((M_SELL, _u8(item), quantity))
    return True


def _budget_sales_first(orders):
    sells = [o for o in orders if o[0] == M_SELL]
    rest = [o for o in orders if o[0] != M_SELL]
    orders[:] = sells + rest


def _apply_six_day_budget_guard(state, action, requirements):
    n_units, units, n_orders, orders = action
    if (state.step < 0 or GUARD_INTERVAL_TURNS <= 0 or
            state.step % GUARD_INTERVAL_TURNS != 0):
        return action
    purchase_budget, _starting_seeds, starting_items = requirements

    orders = list(orders)  # kag::Action result = input;

    available_cash = state.money
    for item in range(N_PRODUCTS):
        sold = min(max(0, state.shed[item]),
                   _existing_sale(orders, len(orders), item))
        available_cash += sold * state.prices[item]
    shortfall = purchase_budget - available_cash
    if shortfall <= 0.0:
        return action

    candidates = []
    for item in range(N_PRODUCTS):
        price = state.prices[item]
        if price < GUARD_MIN_UNIT_PRICE:
            continue
        protected_total = starting_items[item] if GUARD_PROTECT_STATIC_CONSUMPTION else 0
        protected_shed = max(0, protected_total - state.owned_in_hands(item))
        available = max(0, state.shed[item] - protected_shed -
                        _existing_sale(orders, len(orders), item))
        if available > 0:
            candidates.append((item, available, price))
    # std::stable_sort by (price desc, item asc); candidates were appended in
    # ascending item order, so the item key is already satisfied.
    candidates.sort(key=lambda c: -c[2])

    added = 0
    for item, quantity_available, price in candidates:
        if shortfall <= 0.0:
            break
        # static_cast<int>(std::ceil(shortfall / price)); shortfall > 0 and
        # price >= 2, so ceil() >= 1 and the truncating cast is a no-op.
        needed = int(math.ceil(shortfall / price))
        quantity = min(quantity_available, needed)
        if not _add_budget_sale(orders, item, quantity):
            continue
        shortfall -= float(quantity * price)
        added += 1
    if added > 0 and GUARD_SALES_FIRST:
        _budget_sales_first(orders)
    return (n_units, units, len(orders), orders)


# --------------------------------------------------------------------------
# policy.cpp::Context  +  submission_bridge.cpp::Session
# --------------------------------------------------------------------------
class _Context(object):
    __slots__ = ("selected_route",)

    def __init__(self):
        self.selected_route = 0

    def action_for(self, step):
        if step < 0 or step >= K_TURNS:
            return _DEFAULT_ACTION
        return _TAPES[self.selected_route][step]

    def act(self, state, seat):
        if state.step < 0 or state.step >= K_TURNS:
            return _DEFAULT_ACTION
        if state.step == 0:
            self.selected_route = 0
        if state.step == K_DECISION_STEP:
            self.selected_route = 1 if _choose_observed_tail(state) else 0

        action = self.action_for(state.step)
        if state.step % K_SEGMENT_TURNS != 0:
            return action
        end = min(K_TURNS, state.step + K_SEGMENT_TURNS)
        requirements = _calculate_six_day_requirements(
            state, _TAPES[self.selected_route], state.step, end)
        return _apply_six_day_budget_guard(state, action, requirements)


_SESSION_CONTEXT = [None, None]
_SESSION_LAST_STEP = [-1, -1]


# --------------------------------------------------------------------------
# _entry.py action unpacking
# --------------------------------------------------------------------------
def _unit_order(op, arg, quantity):
    name = _UNIT_OPS[op] if 0 <= op < len(_UNIT_OPS) else "PASS"
    if name in ("PLANT", "PICKUP", "PLACE"):
        item = _ITEMS[arg] if 0 <= arg < len(_ITEMS) else _ITEMS[0]
        return [name, item] if quantity == 1 else [name, item, int(quantity)]
    return [name]


def _market_order(op, item, quantity):
    name = _MARKET_OPS[op] if 0 <= op < len(_MARKET_OPS) else "PASS"
    if name == "PASS":
        return None
    if name in ("HIRE", "BUY_LAND"):
        return [name]
    item_name = _ITEMS[item] if 0 <= item < len(_ITEMS) else _ITEMS[0]
    return [name, item_name, int(quantity)]


def _unpack_action(action):
    """submission_bridge.cpp::pack_action followed by _entry.py::_unpack_action."""
    raw_units, units, raw_orders, orders = action
    n_units = max(1, min(raw_units, MAX_UNITS))
    # pack_action zeroes the struct first, so slots the tape did not fill read
    # back as kag::UnitAction defaults ({OP_PASS, 0, 1}) for units[0] when the
    # tape declared n_units == 0, and as zeros beyond that.
    packed = []
    for unit in range(n_units):
        if unit < len(units):
            packed.append(units[unit])
        elif unit == 0:
            packed.append((0, 0, 1))
        else:
            packed.append((0, 0, 0))
    farmer = _unit_order(*packed[0])
    hands = [_unit_order(*packed[index]) for index in range(1, n_units)]
    market = []
    for index in range(max(0, min(raw_orders, 16))):
        order = _market_order(*orders[index])
        if order is not None:
            market.append(order)
    return {"farmer": farmer, "hands": hands, "market": market}


# --------------------------------------------------------------------------
# entry point
# --------------------------------------------------------------------------
def agent(observation, configuration=None):
    seat = int(_read(observation, "player", 0) or 0)
    if seat < 0 or seat > 1:
        raise RuntimeError("ShopForge native policy failed")
    state = _StateView(observation, seat)

    # submission_bridge.cpp::kag_submission_act session-reset rule.
    if (_SESSION_CONTEXT[seat] is None or state.step == 0 or
            state.step < _SESSION_LAST_STEP[seat]):
        _SESSION_CONTEXT[seat] = _Context()
        _SESSION_LAST_STEP[seat] = -1

    action = _SESSION_CONTEXT[seat].act(state, seat)
    _SESSION_LAST_STEP[seat] = state.step
    return _unpack_action(action)
