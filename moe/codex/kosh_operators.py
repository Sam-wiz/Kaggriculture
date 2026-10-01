"""Reusable market operators for replay-backed routes.

The operators in this module are deliberately independent of a particular
public agent's private chassis.  A route supplies its future action tape as the
fourth argument, and the operator only changes market orders that are justified
by the live observation and that tape.  This makes the strong idea reusable
without copying Thomas's internal ``_IMPL`` or sell-debt objects.
"""

from __future__ import annotations

import copy
import itertools
import math
from typing import Any


BASE_PRICES = {
    "WHEAT": 25,
    "CARROT": 35,
    "TOMATO": 60,
    "STRAWBERRY": 120,
    "MELON": 250,
    "EGG": 50,
    "MILK": 160,
    "WOOL": 200,
    "FERTILIZER": 100,
}
RACE_ITEMS = tuple(BASE_PRICES)
SALE_ADVANCE_ITEMS = (
    "STRAWBERRY", "WOOL", "EGG", "MILK", "MELON", "CARROT", "TOMATO",
)
_SALE_ADVANCE_SHOP_PRODUCTS = {
    "BAKERY": {"EGG", "WHEAT"},
    "PIZZA_SHOP": {"MILK", "TOMATO", "WHEAT"},
    "BRUNCH_SPOT": {"EGG", "WHEAT", "STRAWBERRY"},
    "YARN_STORE": {"WOOL"},
    "ICE_CREAM_SHOP": {"STRAWBERRY", "MILK", "WHEAT"},
    "PET_CAFE": {"CARROT"},
    "SMOOTHIE_SHOP": {"STRAWBERRY", "MILK"},
    "FARMERS_MARKET": {"WHEAT", "CARROT", "TOMATO", "STRAWBERRY"},
}
_NO_MILK_SALE_ITEMS = tuple(item for item in SALE_ADVANCE_ITEMS
                            if item != "MILK")
_STATE: dict[tuple[int, str], dict[str, Any]] = {}
_OPPONENT_FRONT_RUN_STATE: dict[tuple[int, str], dict[str, Any]] = {}
TELEMETRY = {
    "calls": 0,
    "reservations": 0,
    "reserved_units": 0,
    "suppressed_units": 0,
    "quote_abstains": 0,
}
OPPONENT_FRONT_RUN_TELEMETRY = {
    "calls": 0,
    "evidence": 0,
    "changed_turns": 0,
    "advanced_units": 0,
    "abstains": 0,
}
ADVANCE_TELEMETRY = {
    "calls": 0,
    "changed_turns": 0,
    "advanced_units": 0,
    "abstains": 0,
    # Bounded research trace.  It is diagnostic only and does not affect the
    # returned action; callers may clear/read it between official-engine games.
    "events": [],
}
PRESSURE_SALE_STATE: dict[tuple[int, str], dict[str, Any]] = {}

# A portable version of the public ``budget_guard`` layer.  Unlike
# ``sale_advance``, which only monetises stock already present in a future
# SELL, this layer reacts to a concrete shortfall in the next tape block.  It
# is kept as a separate operator so that it can be evaluated on top of the
# current local-best without changing the incumbent by default.
_BUDGET_SEED_PRICE = {
    "WHEAT": 10, "CARROT": 20, "TOMATO": 50,
    "STRAWBERRY": 100, "MELON": 80,
}
_BUDGET_ANIMAL_COST = {"GOOSE": 300, "COW": 400, "SHEEP": 500}
_BUDGET_LAND_PRICES = (1000, 2000, 4000)
_BUDGET_PRODUCTS = (
    "WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON",
    "EGG", "MILK", "WOOL", "FERTILIZER",
)
BUDGET_GUARD_TELEMETRY = {
    "calls": 0,
    "changed_turns": 0,
    "added_units": 0,
    "abstains": 0,
    "events": [],
}
ROOM_GUARD_TELEMETRY = {
    "calls": 0,
    "changed_turns": 0,
    "added_units": 0,
    "abstains": 0,
    "events": [],
}

# Thomas EXP231's R97 layer protects the next tape pickup from a same-turn
# WHEAT sell/queue shortfall.  This is kept separate from the broader budget
# and room guards because its decision boundary is much narrower: it only
# repairs an immediately observable tape-input deficit.
SUPPLY_PREFETCH_TELEMETRY = {
    "calls": 0,
    "changed_turns": 0,
    "protected_units": 0,
    "abstains": 0,
    "events": [],
}
SELL_IMPACT_TELEMETRY = {
    "calls": 0,
    "changed_turns": 0,
    "reordered_sales": 0,
    "abstains": 0,
    "events": [],
}

# Public research provenance: Jaxa V2780's ``frontload`` component.  The
# complete public agent is not imported here; only its order-reordering idea
# is exposed as a standalone, testable operator.  The operator is deliberately
# conservative: it returns the original order unless both the original and
# reordered lists are executable under two inventory-pressure assumptions.
_FRONTLOAD_PRICE_FLOOR = 1
_FRONTLOAD_HINGE_GAIN = 8.0
_FRONTLOAD_MARKET_PARAMS = {
    "WHEAT": {"base": 25, "I0": 10000, "T": 400,
              "below_func": "sqrt", "below_target": 0.80,
              "above_func": "log", "above_target": 0.20},
    "CARROT": {"base": 35, "I0": 10000, "T": 450,
               "below_func": "hinge", "below_target": 1.00,
               "above_func": "sqrt", "above_target": 0.70},
    "TOMATO": {"base": 60, "I0": 10000, "T": 200,
               "below_func": "hinge", "below_target": 0.40,
               "above_func": "sqrt", "above_target": 0.60},
    "STRAWBERRY": {"base": 120, "I0": 10000, "T": 100,
                   "below_func": "sqrt", "below_target": 0.70,
                   "above_func": "linear", "above_target": 1.60},
    "MELON": {"base": 250, "I0": 10000, "T": 300,
              "below_func": "log", "below_target": 0.20,
              "above_func": "sq", "above_target": 3.60},
    "EGG": {"base": 50, "I0": 10000, "T": 332,
            "below_func": "hinge", "below_target": 0.40,
            "above_func": "log", "above_target": 0.20},
    "MILK": {"base": 160, "I0": 10000, "T": 122,
             "below_func": "sqrt", "below_target": 0.60,
             "above_func": "linear", "above_target": 1.60},
    "WOOL": {"base": 200, "I0": 10000, "T": 105,
             "below_func": "log", "below_target": 0.20,
             "above_func": "sq", "above_target": 3.20},
    "FERTILIZER": {"base": 100, "I0": 10000, "T": 200,
                   "below_func": "linear", "below_target": 0.40,
                   "above_func": "linear", "above_target": 0.40},
}
_FRONTLOAD_SEED_COST = {
    "WHEAT": 10, "CARROT": 20, "TOMATO": 50,
    "STRAWBERRY": 100, "MELON": 80,
}
_FRONTLOAD_ANIMAL_COST = {
    "CHICKEN": 150, "GOOSE": 300, "COW": 400, "SHEEP": 500,
}
_FRONTLOAD_LAND_PRICES = (1000, 2000, 4000)
FRONTLOAD_TELEMETRY = {
    "calls": 0, "changed_turns": 0, "declined": 0,
    "events": [],
}

COUNTERFACTUAL_TELEMETRY = {
    "calls": 0, "changed_turns": 0, "declined": 0,
    "evaluated": 0, "events": [],
}

LOCKSTEP_TELEMETRY = {
    "calls": 0,
    "changed_turns": 0,
    "declined": 0,
    "evaluated": 0,
    "events": [],
}

# Boatlee V29's public adaptive-market idea, made portable.  This layer is
# intentionally separate from the OR2 rival-stock tracker: it only adds a
# small tranche of currently available stock when the quote and observable
# market pressure justify it.  It never changes worker actions or future
# tape orders.
_ADAPTIVE_ITEMS = ("STRAWBERRY", "MILK", "WOOL")
_ADAPTIVE_BASE_PRICE = {"STRAWBERRY": 120.0, "MILK": 160.0, "WOOL": 200.0}
_ADAPTIVE_SHOPS = {
    "PIZZA_SHOP": ("MILK",), "ICE_CREAM_SHOP": ("STRAWBERRY", "MILK"),
    "SMOOTHIE_SHOP": ("STRAWBERRY", "MILK"), "YARN_STORE": ("WOOL",),
}
_ADAPTIVE_STATE: dict[int, dict[str, Any]] = {}
ADAPTIVE_TELEMETRY = {"calls": 0, "changed_turns": 0, "added_units": 0,
                      "abstains": 0}


def _adaptive_demand(observation: dict, item: str, step: int) -> int:
    demand = 1 if step % 24 == 0 else 0
    if step % 4:
        return demand
    shops = (observation.get("town") or {}).get("unlocked_shops") or []
    for shop in shops:
        products = _ADAPTIVE_SHOPS.get(shop, ())
        if item in products:
            demand += 2 if len(products) == 1 else 1
    return demand


def _adaptive_counterfactual_revenue(item: str, market_inventory: int,
                                     quantity: int) -> float:
    """Value a unit tranche with the official piecewise market curve."""
    if item not in _FRONTLOAD_MARKET_PARAMS or quantity <= 0:
        return 0.0
    return sum(_frontload_price(item, market_inventory + offset)
               for offset in range(max(0, int(quantity))))


def _adaptive_wait_revenue(observation: dict, item: str, step: int,
                           market_inventory: int, quantity: int,
                           pressure: float, horizon: int) -> float:
    """Approximate the same tranche after one short observable wait."""
    demand = 0
    for future_step in range(step + 1, step + max(1, int(horizon)) + 1):
        demand += _adaptive_demand(observation, item, future_step)
    rival_supply = max(0, int(round(max(0.0, pressure)
                                   * max(1, int(horizon)) / 4.0)))
    future_inventory = max(0, int(market_inventory) - demand + rival_supply)
    return _adaptive_counterfactual_revenue(item, future_inventory, quantity)


def _adaptive_public_capacity(observation: dict, item: str) -> int:
    """Compare publicly visible production capacity for an adaptive item."""
    farms = observation.get("farms") or []
    player = int(observation.get("player", 0))
    if len(farms) < 2 or player not in (0, 1):
        return 0
    kind = {"STRAWBERRY": "STRAWBERRY", "MILK": "COW",
            "WOOL": "SHEEP"}.get(item)
    if kind is None:
        return 0

    def count(farm: dict) -> int:
        total = 0
        for row in farm.get("tiles") or []:
            for tile in row or []:
                if not isinstance(tile, dict):
                    continue
                if (kind == "STRAWBERRY" and tile.get("kind") == "PLANT"
                        and tile.get("crop") == kind):
                    total += 1
                elif kind in {"COW", "SHEEP"} and tile.get("animal") == kind:
                    total += 1
        return total
    return count(farms[1 - player]) - count(farms[player])


def _adaptive_near_mirror(observation: dict, composition_distance: int,
                          money_distance: float) -> bool:
    """Detect the public near-symmetric regime where extra supply is risky."""
    farms = observation.get("farms") or []
    player = int(observation.get("player", 0))
    if len(farms) < 2 or player not in (0, 1):
        return False

    # Count directly; public capacity is deliberately based only on visible
    # board state, never the opponent's private shed.
    def direct(farm: dict, kind: str) -> int:
        total = 0
        for row in farm.get("tiles") or []:
            for tile in row or []:
                if not isinstance(tile, dict):
                    continue
                if kind == "STRAWBERRY" and tile.get("kind") == "PLANT" \
                        and tile.get("crop") == kind:
                    total += 1
                elif kind in {"COW", "SHEEP"} and tile.get("animal") == kind:
                    total += 1
        return total

    own, rival = farms[player], farms[1 - player]
    distance = sum(abs(direct(own, kind) - direct(rival, kind))
                   for kind in ("STRAWBERRY", "COW", "SHEEP"))
    same_workers = len(own.get("hands") or []) == len(rival.get("hands") or [])
    same_land = len(own.get("unlocked_quadrants") or []) == len(
        rival.get("unlocked_quadrants") or [])
    try:
        money_gap = abs(float(own.get("money", 0))
                        - float(rival.get("money", 0)))
    except (TypeError, ValueError):
        money_gap = float("inf")
    return (distance <= max(0, int(composition_distance))
            and same_workers and same_land and money_gap <= max(0.0, float(money_distance)))


def _adaptive_rank_sell_orders(observation: dict, action: dict,
                               step: int, configuration: dict) -> dict:
    """Rank existing SELL slots by exact market-impact value.

    Non-SELL slots stay at their original indices.  This is deliberately
    separate from adding inventory: it can improve the order of a producer's
    existing sale portfolio without inventing a new sale or disturbing HIRE,
    BUY, or land orders.
    """
    market = action.get("market") or []
    sell_rows = []
    positions = []
    inventory = ((observation.get("market") or {}).get("inventory") or {})
    shops = tuple((observation.get("town") or {}).get(
        "unlocked_shops") or [])
    for index, raw in enumerate(market):
        if (not isinstance(raw, (list, tuple)) or len(raw) < 3
                or str(raw[0]).upper() != "SELL"):
            continue
        item = str(raw[1]).upper()
        if item not in _FRONTLOAD_MARKET_PARAMS:
            continue
        try:
            quantity = max(0, int(raw[2]))
        except (TypeError, ValueError):
            continue
        if quantity <= 0:
            continue
        current_inventory = int(inventory.get(item, 10000))
        current_price = float(_frontload_price(item, current_inventory))
        after_price = float(_frontload_price(
            item, current_inventory + quantity))
        demand = max(0.25, float(sum(
            _adaptive_demand(observation, item, future_step)
            for future_step in range(step + 1, step + 25))))
        excess = max(0.0, current_inventory + quantity - 10000)
        urgency = min(1.0, (excess / demand) / 10.0)
        shop_bonus = sum(
            2 if len(_ADAPTIVE_SHOPS.get(shop, ())) == 1 else 1
            for shop in shops if item in _ADAPTIVE_SHOPS.get(shop, ()))
        score = float(quantity) * max(0.0, current_price - after_price)
        score *= 1.0 + float(configuration.get(
            "adaptive_rank_demand_weight", 0.20)) * urgency
        score += float(configuration.get(
            "adaptive_rank_shop_weight", 0.5)) * shop_bonus
        positions.append(index)
        sell_rows.append((score, -index, list(raw)))
    if len(sell_rows) < 2:
        return action
    if configuration.get("adaptive_rank_require_sell_only") and any(
            not isinstance(order, (list, tuple)) or not order
            or str(order[0]).upper() != "SELL" for order in market):
        return action
    sell_rows.sort(reverse=True)
    ranked = [row[2] for row in sell_rows]
    if ranked == [list(market[index]) for index in positions]:
        return action
    result = _normalise_action(action)
    iterator = iter(ranked)
    for index in positions:
        result["market"][index] = next(iterator)
    return result


def _adaptive_terminal_liquidation(observation: dict, action: dict,
                                   step: int, configuration: dict) -> dict:
    """Sell uncommitted terminal stock when no future production remains."""
    if step < int(configuration.get("adaptive_terminal_start", 716)):
        return action
    result = _normalise_action(action)
    shed = ((observation.get("private") or {}).get("shed") or {})
    sale_items = tuple(configuration.get(
        "adaptive_terminal_items",
        ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON",
         "EGG", "MILK", "WOOL"),
    ))
    existing = {}
    for order in result["market"]:
        if (isinstance(order, (list, tuple)) and len(order) >= 3
                and str(order[0]).upper() == "SELL"):
            item = str(order[1]).upper()
            try:
                existing[item] = existing.get(item, 0) + max(0, int(order[2]))
            except (TypeError, ValueError):
                continue
    for raw_item in sale_items:
        item = str(raw_item).upper()
        try:
            available = max(0, int(shed.get(item, 0)) - existing.get(item, 0))
        except (TypeError, ValueError):
            continue
        if available <= 0:
            continue
        updated = _adaptive_add_sell(result, item, available)
        if updated is result:
            continue
        result = updated
        existing[item] = existing.get(item, 0) + available
    return result


def _adaptive_pickup_reserve(action: dict, item: str) -> int:
    commands = [action.get("farmer") or ["PASS"],
                *(action.get("hands") or [])]
    total = 0
    for command in commands:
        if (isinstance(command, (list, tuple)) and len(command) >= 2
                and command[0] == "PICKUP" and str(command[1]).upper() == item):
            try:
                total += max(0, int(command[2])) if len(command) >= 3 else 1
            except (TypeError, ValueError):
                total += 1
    return total


def _adaptive_existing_sell(action: dict, item: str) -> int:
    total = 0
    for order in action.get("market") or []:
        if (isinstance(order, (list, tuple)) and len(order) >= 3
                and order[0] == "SELL" and str(order[1]).upper() == item):
            try:
                total += max(0, int(order[2]))
            except (TypeError, ValueError):
                pass
    return total


def _adaptive_add_sell(action: dict, item: str, quantity: int) -> dict:
    result = _normalise_action(action)
    existing = next((order for order in result["market"]
                     if len(order) >= 3 and order[0] == "SELL"
                     and str(order[1]).upper() == item), None)
    if existing is not None:
        existing[2] = max(0, int(existing[2])) + quantity
    elif len(result["market"]) < 10:
        # Append, instead of inserting at position zero, to avoid changing
        # the order of purchases that finance the rest of the tape.
        result["market"].append(["SELL", item, quantity])
    else:
        return action
    return result


def adaptive_market(observation: dict, action: dict,
                    configuration=None, tape=None) -> dict:
    """Add bounded, pressure-aware sales from Boatlee's public V29 idea."""
    ADAPTIVE_TELEMETRY["calls"] += 1
    cfg = configuration if isinstance(configuration, dict) else {}
    try:
        step = int(observation.get("step", 0))
        seat = int(observation.get("player", 0))
        start = int(cfg.get("adaptive_start_step", 456))
        tail = int(cfg.get("adaptive_tail_step", 704))
        if step == 0 or step < int(_ADAPTIVE_STATE.get(seat, {}).get("last_step", -1)):
            _ADAPTIVE_STATE[seat] = {
                "last_step": -1, "last_inventory": {}, "last_sold": {},
                "last_shops": (), "pressure": {}, "added": {},
            }
        state = _ADAPTIVE_STATE.setdefault(seat, {
            "last_step": -1, "last_inventory": {}, "last_sold": {},
            "last_shops": (), "pressure": {}, "added": {},
        })
        if (cfg.get("adaptive_disable_on_any_weed")
                and _visible_any_weed(observation)):
            state["last_inventory"] = {
                item: int((observation.get("market") or {}).get(
                    "inventory", {}).get(item, 0))
                for item in _ADAPTIVE_ITEMS}
            state["last_shops"] = tuple((observation.get("town") or {}).get(
                "unlocked_shops") or [])
            return action
        market = observation.get("market") or {}
        inventory = market.get("inventory") or {}
        shops = tuple((observation.get("town") or {}).get(
            "unlocked_shops") or [])
        # Adding a SELL to a turn that also contains HIRE/BUY/land orders can
        # change the shared market's unit-by-unit execution order.  The
        # adaptive layer is optional, so provide a fail-closed mode for
        # experiments and production profiles that want to touch only pure
        # selling turns.
        if cfg.get("adaptive_require_sell_only_market") and any(
                not isinstance(order, (list, tuple)) or not order
                or str(order[0]).upper() != "SELL"
                for order in (action.get("market") or [])):
            state["last_inventory"] = {
                item: int(inventory.get(item, 0)) for item in _ADAPTIVE_ITEMS}
            state["last_shops"] = shops
            return action
        existing_sell_total = 0
        for order in action.get("market") or []:
            if (isinstance(order, (list, tuple)) and len(order) >= 3
                    and str(order[0]).upper() == "SELL"):
                try:
                    existing_sell_total += max(0, int(order[2]))
                except (TypeError, ValueError):
                    pass
        max_existing_sell = cfg.get("adaptive_max_existing_sell")
        if max_existing_sell is not None:
            try:
                if existing_sell_total > max(0, int(max_existing_sell)):
                    state["last_inventory"] = {
                        item: int(inventory.get(item, 0))
                        for item in _ADAPTIVE_ITEMS}
                    state["last_shops"] = shops
                    return action
            except (TypeError, ValueError):
                pass
        if int(state.get("last_step", -1)) == step - 1:
            for item in _ADAPTIVE_ITEMS:
                delta = (int(inventory.get(item, 0))
                         - int(state.get("last_inventory", {}).get(item, 0)))
                external = (delta
                            + _adaptive_demand(
                                {"town": {"unlocked_shops": state.get("last_shops", ())}},
                                item, step - 1)
                            - int(state.get("last_sold", {}).get(item, 0)))
                old = float(state.setdefault("pressure", {}).get(item, 0.0))
                state["pressure"][item] = max(
                    0.0, old * float(cfg.get("adaptive_decay", 0.72))
                    + min(24.0, max(0.0, float(external))))
        state["last_step"] = step
        if step >= tail and cfg.get("adaptive_terminal_liquidation"):
            return _adaptive_terminal_liquidation(
                observation, action, step, cfg)
        if step < start or step >= tail:
            state["last_inventory"] = {
                item: int(inventory.get(item, 0)) for item in _ADAPTIVE_ITEMS}
            state["last_shops"] = shops
            return action
        private = observation.get("private") or {}
        shed = private.get("shed") or {}
        total_shed = sum(max(0, int(value)) for value in shed.values())
        result = action
        changed = False
        near_mirror = bool(cfg.get("adaptive_disable_near_mirror")) and step >= int(
            cfg.get("adaptive_mirror_latch_step", 289)) and _adaptive_near_mirror(
                observation,
                int(cfg.get("adaptive_mirror_composition_distance", 2)),
                float(cfg.get("adaptive_mirror_money_distance", 250)),
            )
        for item in _ADAPTIVE_ITEMS:
            if near_mirror:
                continue
            stock = max(0, int(shed.get(item, 0)))
            pickup = _adaptive_pickup_reserve(result, item)
            scheduled = min(max(0, stock - pickup),
                            _adaptive_existing_sell(result, item))
            excess = max(0, stock - pickup - scheduled)
            if excess <= 0:
                continue
            if step < 528:
                reserve = 12
            elif step < 600:
                reserve = 8
            elif step < 648:
                reserve = 6
            elif step < 684:
                reserve = 3
            else:
                reserve = 0
            if total_shed >= int(cfg.get("adaptive_shed_soft", 72)):
                reserve = max(0, reserve - 7)
            if total_shed >= int(cfg.get("adaptive_shed_hard", 88)):
                reserve = 0
            if cfg.get("adaptive_reserve_shop_demand") and step < 684:
                shop_demand = _adaptive_demand(observation, item, step)
                reserve += min(
                    int(cfg.get("adaptive_demand_reserve_cap", 14)),
                    shop_demand * int(cfg.get("adaptive_demand_reserve", 2)),
                )
            excess = max(0, excess - reserve)
            if excess <= 0:
                continue
            price = float((market.get("prices") or {}).get(item, 0))
            ratio = price / _ADAPTIVE_BASE_PRICE[item]
            pressure = float(state.get("pressure", {}).get(item, 0.0))
            gate = float(cfg.get("adaptive_price_gate", 0.66))
            if step < 684:
                gate += min(0.24, _adaptive_demand(observation, item, step)
                            * float(cfg.get("adaptive_demand_gate", 0.045)))
            if step >= 648:
                gate -= 0.12
            if step >= 684:
                gate -= 0.18
            if pressure >= float(cfg.get("adaptive_pressure_trigger", 2.0)):
                gate -= 0.18
            if cfg.get("adaptive_use_public_capacity"):
                capacity_delta = _adaptive_public_capacity(observation, item)
                if capacity_delta >= int(cfg.get(
                        "adaptive_capacity_trigger", 0)):
                    gate -= float(cfg.get(
                        "adaptive_capacity_gate_cut", 0.08))
            urgent = (total_shed >= int(cfg.get("adaptive_shed_hard", 88))
                      or step >= 704)
            if not urgent and ratio < max(0.20, gate):
                continue
            already = int(state.setdefault("added", {}).get(item, 0))
            budget = max(0, int(cfg.get("adaptive_max_extra", 18)) - already)
            if budget <= 0:
                continue
            tranche = int(cfg.get("adaptive_tranche", 4))
            if pressure >= float(cfg.get("adaptive_pressure_trigger", 2.0)):
                tranche += int(cfg.get("adaptive_pressure_tranche", 4))
            if total_shed >= int(cfg.get("adaptive_shed_soft", 72)):
                tranche += int(cfg.get("adaptive_shed_tranche", 4))
            if step >= 684:
                tranche += int(cfg.get("adaptive_tail_tranche", 5))
            quantity = min(excess, max(1, tranche), budget)
            if (cfg.get("adaptive_use_exact_curve") and not urgent
                    and quantity > 0):
                try:
                    market_inventory = int(inventory.get(item, 10000))
                    now_value = _adaptive_counterfactual_revenue(
                        item, market_inventory, quantity)
                    wait_value = _adaptive_wait_revenue(
                        observation, item, step, market_inventory, quantity,
                        pressure,
                        int(cfg.get("adaptive_value_horizon", 8)),
                    )
                    margin = float(cfg.get("adaptive_value_margin", 0.0))
                    if wait_value > now_value * (1.0 + max(0.0, margin)):
                        continue
                except (TypeError, ValueError, KeyError):
                    continue
            updated = _adaptive_add_sell(result, item, quantity)
            if updated is result:
                continue
            result = updated
            state["added"][item] = already + quantity
            ADAPTIVE_TELEMETRY["added_units"] += quantity
            changed = True
        rank_start = max(
            start,
            int(cfg.get("adaptive_rank_start_step", start)),
        )
        if cfg.get("adaptive_rank_sell_orders") and step >= rank_start:
            result = _adaptive_rank_sell_orders(
                observation, result, step, cfg)
        if cfg.get("adaptive_terminal_liquidation"):
            result = _adaptive_terminal_liquidation(
                observation, result, step, cfg)
        state["last_inventory"] = {
            item: int(inventory.get(item, 0)) for item in _ADAPTIVE_ITEMS}
        state["last_sold"] = {
            item: min(max(0, int(shed.get(item, 0))),
                      _adaptive_existing_sell(result, item))
            for item in _ADAPTIVE_ITEMS}
        state["last_shops"] = shops
        if changed:
            ADAPTIVE_TELEMETRY["changed_turns"] += 1
        return result
    except (AttributeError, IndexError, KeyError, TypeError, ValueError):
        ADAPTIVE_TELEMETRY["abstains"] += 1
        return action


def adaptive_market_tape_guard(observation: dict, action: dict,
                               configuration=None, tape=None) -> dict:
    """Accept adaptive sales only when a short Tape suffix stays executable."""
    cfg = dict(configuration) if isinstance(configuration, dict) else {}
    proposed = adaptive_market(observation, action, cfg, tape)
    if proposed == action or tape is None:
        return action
    try:
        step = int(observation.get("step", 0))
        if cfg.get("adaptive_tape_reserve_future_sales"):
            reserve_horizon = max(1, int(cfg.get(
                "adaptive_tape_reserve_horizon", 24)))
            future_required = {}
            raw_actions = getattr(tape, "actions", ())
            for index in range(
                    step + 1,
                    min(len(raw_actions), step + reserve_horizon + 1)):
                frame = raw_actions[index]
                for order in ((frame.get("market") or [])
                              if isinstance(frame, dict) else []):
                    if (not isinstance(order, (list, tuple))
                            or len(order) < 3
                            or str(order[0]).upper() != "SELL"):
                        continue
                    item = str(order[1]).upper()
                    try:
                        amount = max(0, int(order[2]))
                    except (TypeError, ValueError):
                        continue
                    future_required[item] = future_required.get(item, 0) + amount
            if future_required:
                original_by_item = {}
                for order in action.get("market") or []:
                    if (isinstance(order, (list, tuple)) and len(order) >= 3
                            and str(order[0]).upper() == "SELL"):
                        try:
                            original_by_item[str(order[1]).upper()] = (
                                original_by_item.get(str(order[1]).upper(), 0)
                                + max(0, int(order[2])))
                        except (TypeError, ValueError):
                            continue
                proposed_queue = [list(order)
                                  for order in (proposed.get("market") or [])]
                for item, required in future_required.items():
                    proposed_total = sum(
                        max(0, int(order[2]))
                        for order in proposed_queue
                        if (isinstance(order, list) and len(order) >= 3
                            and str(order[0]).upper() == "SELL"
                            and str(order[1]).upper() == item)
                    )
                    original_total = original_by_item.get(item, 0)
                    extra = max(0, proposed_total - original_total)
                    remove = min(extra, required)
                    for order in reversed(proposed_queue):
                        if remove <= 0:
                            break
                        if (len(order) >= 3
                                and str(order[0]).upper() == "SELL"
                                and str(order[1]).upper() == item):
                            cut = min(remove, max(0, int(order[2])))
                            order[2] = int(order[2]) - cut
                            remove -= cut
                proposed = dict(proposed, market=[
                    order for order in proposed_queue
                    if not (len(order) >= 3
                            and str(order[0]).upper() == "SELL"
                            and int(order[2]) <= 0)
                ])
                if proposed == action:
                    return action
        horizon = max(1, int(cfg.get("adaptive_tape_horizon", 8)))
        suffix = _tape_market_suffix(tape, step, horizon)
        if not suffix:
            return action
        player = int(observation["player"])
        farm = (observation.get("farms") or [])[player]
        private = observation["private"]
        money = float(farm["money"])
        shed_total = sum(int(value) for value in private["shed"].values())
        inventory = {
            key: int(value)
            for key, value in observation["market"]["inventory"].items()
        }
        hires_today = int(farm.get("hires_today", 0))
        extra_land = max(
            0, len(farm.get("unlocked_quadrants", ["NW"])) - 1)
        baseline_queue = [list(order) for order in (action.get("market") or [])]
        proposed_queue = [list(order)
                          for order in (proposed.get("market") or [])]
        if baseline_queue == proposed_queue:
            return action
        raw_pressures = cfg.get("adaptive_tape_pressures", (0, 1))
        pressures = tuple(int(value) for value in raw_pressures) or (0,)
        minimum_gain = float(cfg.get("adaptive_tape_min_cash_gain", 0.0))
        baseline_values = []
        proposed_values = []
        for pressure in pressures:
            baseline = _frontload_sequence_outcome(
                [baseline_queue, *suffix], money, shed_total,
                inventory, hires_today, extra_land, pressure)
            candidate = _frontload_sequence_outcome(
                [proposed_queue, *suffix], money, shed_total,
                inventory, hires_today, extra_land, pressure)
            if baseline is None or candidate is None:
                return action
            baseline_values.append(float(baseline[0]))
            proposed_values.append(float(candidate[0]))
        if min(proposed_values) + 1e-9 < min(baseline_values) + minimum_gain:
            return action
        events = ADAPTIVE_TELEMETRY.setdefault("events", [])
        events.append({
            "step": step,
            "horizon": horizon,
            "baseline_min_cash": min(baseline_values),
            "proposed_min_cash": min(proposed_values),
        })
        del events[:-512]
        return proposed
    except (AttributeError, IndexError, KeyError, TypeError, ValueError):
        return action


def _frontload_shape(function: str, value: float, threshold: float) -> float:
    value = max(0.0, value)
    if function == "linear":
        return value
    if function == "sq":
        return value * value
    if function == "sqrt":
        return math.sqrt(value)
    if function == "log":
        return math.log(1.0 + value)
    if function == "hinge":
        if threshold <= 0:
            return value
        ratio = value / threshold
        return ratio + _FRONTLOAD_HINGE_GAIN * max(0.0, ratio - 1.0) ** 2
    return value


def _frontload_price(item: str, inventory: int) -> int:
    params = _FRONTLOAD_MARKET_PARAMS[item]
    base = params["base"]
    initial = params["I0"]
    threshold = params["T"]
    if inventory < initial:
        shape = params["below_func"]
        amplitude = params["below_target"] * base / _frontload_shape(
            shape, threshold, threshold)
        value = base + amplitude * _frontload_shape(
            shape, initial - inventory, threshold)
    else:
        shape = params["above_func"]
        amplitude = params["above_target"] * base / _frontload_shape(
            shape, threshold, threshold)
        value = base - amplitude * _frontload_shape(
            shape, inventory - initial, threshold)
    return max(_FRONTLOAD_PRICE_FLOOR, int(round(value)))


def _frontload_outcome(orders: list[list], money: float, shed_total: int,
                       inventory: dict[str, int], hires_today: int,
                       extra_land: int, pressure: int):
    """Return the simulated terminal state, or ``None`` if invalid."""
    inv = dict(inventory)
    money = float(money)
    shed = int(shed_total)
    for order in orders:
        if not isinstance(order, (list, tuple)) or not order:
            return False
        operation = order[0]
        if operation == "HIRE":
            a, b = 1, 1
            for _ in range(max(0, int(hires_today))):
                a, b = b, a + b
            if money < a:
                return None
            money -= a
            hires_today += 1
            continue
        if operation == "BUY_LAND":
            if extra_land >= len(_FRONTLOAD_LAND_PRICES):
                return None
            cost = _FRONTLOAD_LAND_PRICES[extra_land]
            if money < cost:
                return None
            money -= cost
            extra_land += 1
            continue
        if len(order) < 3:
            return None
        try:
            quantity = int(order[2])
        except (TypeError, ValueError):
            return None
        if quantity <= 0:
            return None
        item = order[1]
        if operation == "SELL":
            if item not in _FRONTLOAD_MARKET_PARAMS or item not in inv:
                return None
            for _ in range(quantity):
                price = _frontload_price(item, inv[item])
                money += price
                if price > 1:
                    inv[item] += 1 + pressure
                shed -= 1
        elif operation == "BUY_PRODUCT":
            if item not in ("WHEAT", "FERTILIZER") or item not in inv:
                return None
            for _ in range(quantity):
                price = _frontload_price(item, inv[item] - 1)
                if money < price or shed >= 100:
                    return None
                money -= price
                inv[item] -= 1 + pressure
                shed += 1
        elif operation == "BUY_SEED":
            if item not in _FRONTLOAD_SEED_COST:
                return None
            if money < _FRONTLOAD_SEED_COST[item] * quantity:
                return None
            money -= _FRONTLOAD_SEED_COST[item] * quantity
        elif operation == "BUY_ANIMAL":
            if item not in _FRONTLOAD_ANIMAL_COST:
                return None
            for _ in range(quantity):
                cost = _FRONTLOAD_ANIMAL_COST[item]
                if money < cost or shed >= 100:
                    return None
                money -= cost
                shed += 1
        else:
            return None
    return money, shed, inv


def _frontload_simulate(orders: list[list], money: float, shed_total: int,
                        inventory: dict[str, int], hires_today: int,
                        extra_land: int, pressure: int) -> bool:
    """Check whether an order list completes under the official market ABI."""
    return _frontload_outcome(
        orders, money, shed_total, inventory, hires_today, extra_land,
        pressure) is not None


def _frontload_order_variants(orders: list[list]) -> list[list[list]]:
    """Return stable order-class permutations for counterfactual selection."""
    ordinary_sells: list[list] = []
    product_buys: list[list] = []
    other: list[list] = []
    for index, order in enumerate(orders):
        operation = order[0]
        if operation == "SELL":
            wash = any(
                prior[0] == "BUY_PRODUCT" and len(prior) > 1
                and len(order) > 1 and prior[1] == order[1]
                for prior in orders[:index]
            )
            (product_buys if wash else ordinary_sells).append(order)
        elif operation == "BUY_PRODUCT":
            product_buys.append(order)
        else:
            other.append(order)
    groups = (ordinary_sells, product_buys, other)
    variants = []
    for order_groups in (
            (0, 1, 2), (1, 0, 2), (0, 2, 1),
            (1, 2, 0), (2, 0, 1), (2, 1, 0)):
        variant = [order for group in order_groups for order in groups[group]]
        if variant not in variants:
            variants.append(variant)
    return variants


def _sell_slot_variants(orders: list[list], max_permutations: int = 240
                        ) -> list[list[list]]:
    """Enumerate SELL-only queue variants without moving other order slots.

    A market queue is not a bag of independent orders: a SELL can finance a
    later BUY, and each unit changes the shared quote.  This helper therefore
    keeps every non-SELL order at its original index and only permutes the
    existing SELL rows.  The bound is a safety limit for malformed or very
    large queues.
    """
    positions = [index for index, order in enumerate(orders)
                 if isinstance(order, (list, tuple)) and order
                 and str(order[0]).upper() == "SELL"]
    if len(positions) < 2:
        return [orders]
    sell_rows = [list(orders[index]) for index in positions]
    variants: list[list[list]] = []
    for permutation in itertools.islice(
            itertools.permutations(sell_rows), max(1, int(max_permutations))):
        candidate = [list(order) for order in orders]
        for index, order in zip(positions, permutation):
            candidate[index] = list(order)
        if candidate not in variants:
            variants.append(candidate)
    return variants or [orders]


def market_counterfactual_selector(observation: dict, action: dict,
                                   configuration=None, tape=None) -> dict:
    """Select a market queue by exact, robust counterfactual simulation.

    This is an algorithmic selector, not a fixed price rule.  It generates
    alternatives from the current queue, simulates every alternative under a
    small set of inventory-pressure scenarios, and accepts a change only when
    its worst-case same-turn cash is at least as good as the incumbent by the
    configured margin.  By default only existing SELL rows are permuted, so
    financing, hiring, and land orders remain in their original slots.

    The operator intentionally does not invent production or market orders.
    It is a reusable portfolio-order optimizer that can be applied to any
    Tape, including newly registered Tapes, without hand-written conditions.
    """
    COUNTERFACTUAL_TELEMETRY["calls"] += 1
    cfg = configuration if isinstance(configuration, dict) else {}
    try:
        step = int(observation.get("step", 0))
        if step < max(0, int(cfg.get("counterfactual_first_step", 0))):
            return action
    except (TypeError, ValueError):
        return action
    if cfg.get("counterfactual_disable_on_any_weed") and _visible_any_weed(
            observation):
        return action
    if not isinstance(action, dict):
        return action
    market = action.get("market") or []
    if not isinstance(market, list) or len(market) < 2:
        return action
    orders = [list(order) for order in market
              if isinstance(order, (list, tuple)) and order]
    if len(orders) != len(market):
        return action
    try:
        player = int(observation["player"])
        farm = observation["farms"][player]
        private = observation["private"]
        money = float(farm["money"])
        shed_total = sum(int(value) for value in private["shed"].values())
        inventory = {key: int(value) for key, value in
                     observation["market"]["inventory"].items()}
        hires_today = int(farm.get("hires_today", 0))
        extra_land = max(0, len(farm.get("unlocked_quadrants", ["NW"])) - 1)
    except (KeyError, TypeError, ValueError, IndexError, AttributeError):
        COUNTERFACTUAL_TELEMETRY["declined"] += 1
        return action

    max_permutations = max(1, int(cfg.get(
        "counterfactual_max_permutations", 240)))
    if cfg.get("counterfactual_preserve_non_sell", True):
        candidates = _sell_slot_variants(orders, max_permutations)
    else:
        candidates = [orders, *_frontload_order_variants(orders)]
        candidates.extend(_sell_slot_variants(orders, max_permutations))

    pressures = tuple(int(value) for value in (
        cfg.get("counterfactual_pressures", (0, 1))))
    if not pressures:
        pressures = (0,)
    baseline = []
    for pressure in pressures:
        outcome = _frontload_outcome(
            orders, money, shed_total, inventory, hires_today,
            extra_land, pressure)
        if outcome is None:
            COUNTERFACTUAL_TELEMETRY["declined"] += 1
            return action
        baseline.append(float(outcome[0]))

    best = orders
    best_score = (min(baseline), sum(baseline), 0)
    min_gain = float(cfg.get("counterfactual_min_cash_gain", 0.0))
    seen = set()
    for candidate in candidates:
        key = repr(candidate)
        if key in seen:
            continue
        seen.add(key)
        values = []
        valid = True
        for pressure in pressures:
            outcome = _frontload_outcome(
                candidate, money, shed_total, inventory, hires_today,
                extra_land, pressure)
            if outcome is None:
                valid = False
                break
            values.append(float(outcome[0]))
        COUNTERFACTUAL_TELEMETRY["evaluated"] += 1
        if not valid:
            continue
        gain = min(values) - min(baseline)
        if gain + 1e-9 < min_gain:
            continue
        score = (min(values), sum(values), -int(candidate == orders))
        if score > best_score:
            best, best_score = candidate, score
    if best == orders:
        COUNTERFACTUAL_TELEMETRY["declined"] += 1
        return action

    COUNTERFACTUAL_TELEMETRY["changed_turns"] += 1
    events = COUNTERFACTUAL_TELEMETRY.setdefault("events", [])
    events.append({
        "step": step,
        "candidate_count": len(seen),
        "baseline_min_cash": min(baseline),
        "selected_min_cash": best_score[0],
    })
    del events[:-512]
    return dict(action, market=best)


def _frontload_sequence_outcome(sequence: list[list[list]], money: float,
                                shed_total: int, inventory: dict[str, int],
                                hires_today: int, extra_land: int,
                                pressure: int):
    """Simulate a short sequence of market queues with carried state.

    ``_frontload_outcome`` intentionally models one queue only.  This helper
    carries the two state variables that matter when a queue is evaluated
    against a future Tape: the Fibonacci hire index and the land-price index.
    It is still only a market suffix model; worker movement and production
    are deliberately not fabricated here.
    """
    current_money = float(money)
    current_shed = int(shed_total)
    current_inventory = dict(inventory)
    current_hires = int(hires_today)
    current_land = int(extra_land)
    for orders in sequence:
        outcome = _frontload_outcome(
            orders, current_money, current_shed, current_inventory,
            current_hires, current_land, pressure)
        if outcome is None:
            return None
        current_money, current_shed, current_inventory = outcome
        current_hires += sum(
            1 for order in orders
            if isinstance(order, (list, tuple)) and order
            and str(order[0]).upper() == "HIRE"
        )
        current_land += sum(
            1 for order in orders
            if isinstance(order, (list, tuple)) and order
            and str(order[0]).upper() == "BUY_LAND"
        )
    return current_money, current_shed, current_inventory


def _tape_market_suffix(tape: Any, step: int, horizon: int) -> list[list[list]]:
    """Extract future market queues without importing the replay chassis."""
    raw = getattr(tape, "actions", ()) if tape is not None else ()
    if not isinstance(raw, (list, tuple)):
        return []
    suffix = []
    for index in range(int(step) + 1,
                      min(len(raw), int(step) + max(1, int(horizon)) + 1)):
        frame = raw[index]
        if not isinstance(frame, dict):
            suffix.append([])
            continue
        queue = frame.get("market") or []
        if not isinstance(queue, list):
            return []
        if any(not isinstance(order, (list, tuple)) or not order
               for order in queue):
            return []
        suffix.append([list(order) for order in queue])
    return suffix


def market_queue_lockstep(observation: dict, action: dict,
                          configuration=None, tape=None) -> dict:
    """Choose a SELL ordering using a short carried-state Tape suffix.

    The live market is shared, so a same-turn cash improvement is not enough:
    moving one item first changes the quote seen by later orders and by the
    next Tape queues.  This operator enumerates only SELL permutations at the
    current turn, then runs each candidate and the unchanged future Tape
    queues through the official piecewise market approximation under multiple
    rival-pressure scenarios.  It fails closed when no Tape or an invalid
    future queue is available.

    It does not add production or invent future sales.  The operator is
    therefore suitable as a bounded market-only experiment and can be
    attached to a newly registered Tape without hand-written item rules.
    """
    LOCKSTEP_TELEMETRY["calls"] += 1
    cfg = configuration if isinstance(configuration, dict) else {}
    try:
        step = int(observation.get("step", 0))
        if step < max(0, int(cfg.get("lockstep_first_step", 0))):
            return action
        horizon = max(1, int(cfg.get("lockstep_horizon", 12)))
    except (TypeError, ValueError):
        LOCKSTEP_TELEMETRY["declined"] += 1
        return action
    if cfg.get("lockstep_disable_on_any_weed") and _visible_any_weed(observation):
        return action
    if not isinstance(action, dict):
        return action
    market = action.get("market") or []
    if not isinstance(market, list) or len(market) < 2:
        return action
    orders = [list(order) for order in market
              if isinstance(order, (list, tuple)) and order]
    if len(orders) != len(market):
        LOCKSTEP_TELEMETRY["declined"] += 1
        return action
    suffix = _tape_market_suffix(tape, step, horizon)
    if not suffix:
        LOCKSTEP_TELEMETRY["declined"] += 1
        return action
    try:
        player = int(observation["player"])
        farm = observation["farms"][player]
        private = observation["private"]
        money = float(farm["money"])
        shed_total = sum(int(value) for value in private["shed"].values())
        inventory = {key: int(value) for key, value in
                     observation["market"]["inventory"].items()}
        hires_today = int(farm.get("hires_today", 0))
        extra_land = max(0, len(farm.get("unlocked_quadrants", ["NW"])) - 1)
    except (KeyError, TypeError, ValueError, IndexError, AttributeError):
        LOCKSTEP_TELEMETRY["declined"] += 1
        return action

    candidates = _sell_slot_variants(
        orders, max(1, int(cfg.get("lockstep_max_permutations", 120))))
    raw_pressures = cfg.get("lockstep_pressures", (0, 1))
    try:
        pressures = tuple(int(value) for value in raw_pressures)
    except (TypeError, ValueError):
        pressures = (0, 1)
    if not pressures:
        pressures = (0,)
    sequences = lambda candidate: [candidate, *suffix]
    baseline_values = []
    for pressure in pressures:
        outcome = _frontload_sequence_outcome(
            sequences(orders), money, shed_total, inventory,
            hires_today, extra_land, pressure)
        if outcome is None:
            # The Tape is not a valid suffix from this live state; changing
            # the current queue based on a fictitious continuation is unsafe.
            LOCKSTEP_TELEMETRY["declined"] += 1
            return action
        baseline_values.append(float(outcome[0]))

    best = orders
    best_score = (min(baseline_values), sum(baseline_values), 0)
    min_gain = float(cfg.get("lockstep_min_cash_gain", 0.0))
    seen = set()
    for candidate in candidates:
        key = repr(candidate)
        if key in seen:
            continue
        seen.add(key)
        values = []
        valid = True
        for pressure in pressures:
            outcome = _frontload_sequence_outcome(
                sequences(candidate), money, shed_total, inventory,
                hires_today, extra_land, pressure)
            if outcome is None:
                valid = False
                break
            values.append(float(outcome[0]))
        LOCKSTEP_TELEMETRY["evaluated"] += 1
        if not valid:
            continue
        gain = min(values) - min(baseline_values)
        if gain + 1e-9 < min_gain:
            continue
        score = (min(values), sum(values), -int(candidate == orders))
        if score > best_score:
            best, best_score = candidate, score
    if best == orders:
        LOCKSTEP_TELEMETRY["declined"] += 1
        return action
    LOCKSTEP_TELEMETRY["changed_turns"] += 1
    events = LOCKSTEP_TELEMETRY.setdefault("events", [])
    events.append({
        "step": step,
        "horizon": len(suffix),
        "candidate_count": len(seen),
        "baseline_min_cash": min(baseline_values),
        "selected_min_cash": best_score[0],
    })
    del events[:-512]
    return dict(action, market=best)


def jaxa_frontload(observation: dict, action: dict,
                   configuration=None, tape=None) -> dict:
    """Safely front-load market orders, ported from public Jaxa V2780.

    Orders are partitioned as: ordinary SELLs, BUY_PRODUCT plus same-item
    wash-sale SELLs, and all other orders.  The reorder is accepted only when
    both versions execute completely under pressure 0 and pressure 1.  The
    ``tape`` argument is accepted for the common overlay ABI but is unused.
    """
    FRONTLOAD_TELEMETRY["calls"] += 1
    cfg = configuration if isinstance(configuration, dict) else {}
    try:
        if int(observation.get("step", 0)) < max(
                0, int(cfg.get("frontload_first_step", 0))):
            return action
    except (TypeError, ValueError):
        return action
    if cfg.get("frontload_disable_on_weed") and _visible_weed(observation):
        return action
    if (cfg.get("frontload_disable_on_any_weed")
            and _visible_any_weed(observation)):
        return action
    if "frontload_player" in cfg:
        try:
            if int(observation.get("player", 0)) != int(cfg["frontload_player"]):
                return action
        except (TypeError, ValueError):
            return action
    if cfg.get("frontload_require_money_lead"):
        try:
            player = int(observation.get("player", 0))
            farms = observation.get("farms") or []
            if len(farms) == 2:
                own_money = float(farms[player].get("money", 0))
                rival_money = float(farms[1 - player].get("money", 0))
                if own_money < rival_money:
                    return action
        except (AttributeError, IndexError, TypeError, ValueError):
            return action
    if not isinstance(action, dict):
        return action
    market = action.get("market") or []
    if not isinstance(market, list) or len(market) < 2:
        return action
    orders = [list(order) for order in market
              if isinstance(order, (list, tuple)) and order]
    if len(orders) != len(market):
        return action

    variants = _frontload_order_variants(orders)
    reordered = variants[0] if variants else orders
    if reordered == orders:
        return action

    # The public front-loader also moves BUY_PRODUCT, HIRE, BUY_LAND, and
    # other non-SELL actions.  That is strategically dangerous in a
    # two-player market: the same order change can help one seat and hurt the
    # other by changing who reaches the shared market first.  This optional
    # guard keeps every non-SELL slot and order fixed, allowing only SELLs to
    # exchange places with other SELLs.  It is intentionally opt-in so the
    # broad public port remains available for ablation, while the safer
    # variant can be evaluated independently.
    if cfg.get("frontload_preserve_non_sell"):
        for before, after in zip(orders, reordered):
            before_non_sell = before[0] != "SELL"
            after_non_sell = after[0] != "SELL"
            if before_non_sell or after_non_sell:
                if before != after:
                    return action

    try:
        player = int(observation["player"])
        farm = observation["farms"][player]
        private = observation["private"]
        money = float(farm["money"])
        shed_total = sum(int(value) for value in private["shed"].values())
        inventory = {key: int(value)
                     for key, value in observation["market"]["inventory"].items()}
        hires_today = int(farm.get("hires_today", 0))
        extra_land = max(
            0, len(farm.get("unlocked_quadrants", ["NW"])) - 1)
        if cfg.get("frontload_counterfactual_select"):
            best_orders = orders
            best_score = None
            for candidate in [orders, *variants]:
                candidate_outcomes = []
                for candidate_pressure in (0, 1):
                    candidate_outcome = _frontload_outcome(
                        candidate, money, shed_total, inventory, hires_today,
                        extra_land, candidate_pressure)
                    if candidate_outcome is None:
                        candidate_outcomes = []
                        break
                    candidate_outcomes.append(float(candidate_outcome[0]))
                if len(candidate_outcomes) != 2:
                    continue
                score = (
                    min(candidate_outcomes),
                    sum(candidate_outcomes),
                    -int(candidate == orders),
                )
                if best_score is None or score > best_score:
                    best_score = score
                    best_orders = candidate
            if best_orders == orders:
                FRONTLOAD_TELEMETRY["declined"] += 1
                return action
            reordered = best_orders

        for pressure in (0, 1):
            before = _frontload_outcome(
                orders, money, shed_total, inventory, hires_today,
                extra_land, pressure)
            after = _frontload_outcome(
                reordered, money, shed_total, inventory, hires_today,
                extra_land, pressure)
            if before is None:
                FRONTLOAD_TELEMETRY["declined"] += 1
                return action
            if after is None:
                FRONTLOAD_TELEMETRY["declined"] += 1
                return action
            if cfg.get("frontload_require_money_non_decrease"):
                if float(after[0]) + 1e-9 < float(before[0]):
                    FRONTLOAD_TELEMETRY["declined"] += 1
                    return action
    except (KeyError, TypeError, ValueError, IndexError):
        FRONTLOAD_TELEMETRY["declined"] += 1
        return action

    FRONTLOAD_TELEMETRY["changed_turns"] += 1
    events = FRONTLOAD_TELEMETRY.setdefault("events", [])
    player = int(observation.get("player", 0))
    farms = observation.get("farms") or []
    opponent_money = None
    if len(farms) == 2 and 0 <= player < 2:
        try:
            opponent_money = float(farms[1 - player].get("money", 0))
        except (AttributeError, TypeError, ValueError):
            opponent_money = None
    events.append({
        "step": int(observation.get("step", 0)),
        "player": player,
        "weed": _visible_weed(observation),
        "money": float(farms[player].get("money", 0))
        if 0 <= player < len(farms) else None,
        "opponent_money": opponent_money,
        "before": [tuple(order[:2]) for order in orders],
        "after": [tuple(order[:2]) for order in reordered],
    })
    del events[:-512]
    return dict(action, market=reordered)


def _actions(tape: Any) -> tuple[dict, ...]:
    raw = getattr(tape, "actions", ()) if tape is not None else ()
    return tuple(item for item in raw if isinstance(item, dict))


def _visible_weed(observation: dict) -> bool:
    player = int(observation.get("player", 0))
    farms = observation.get("farms") or []
    if not 0 <= player < len(farms):
        return False
    for row in farms[player].get("tiles") or []:
        for tile in row:
            if isinstance(tile, dict) and tile.get("kind") == "WEED":
                return True
    return False


def _visible_any_weed(observation: dict) -> bool:
    """Return whether either publicly visible farm currently has a weed."""
    for farm in observation.get("farms") or []:
        for row in farm.get("tiles") or []:
            for tile in row:
                if isinstance(tile, dict) and tile.get("kind") == "WEED":
                    return True
    return False


def _visible_milk_shop(observation: dict) -> bool:
    shops = list((observation.get("town") or {}).get("unlocked_shops") or [])
    return any(shop in {"PIZZA_SHOP", "ICE_CREAM_SHOP", "SMOOTHIE_SHOP"}
               for shop in shops)


def _visible_rival_yield(observation: dict, item: str) -> int:
    """Estimate immediately saleable rival stock from public board tiles.

    Rival sheds are private, so this is deliberately only a lower-bound signal:
    currently accumulated ``yield_units`` on visible crops/animals.  It is
    useful as an optional pressure gate, not as a reconstruction of hidden
    inventory.
    """
    player = int(observation.get("player", 0))
    farms = observation.get("farms") or []
    if len(farms) < 2 or player not in (0, 1):
        return 0
    product_to_crop = {
        "WHEAT": "WHEAT", "CARROT": "CARROT", "TOMATO": "TOMATO",
        "STRAWBERRY": "STRAWBERRY", "MELON": "MELON",
    }
    product_to_animal = {"EGG": "GOOSE", "MILK": "COW", "WOOL": "SHEEP"}
    crop = product_to_crop.get(str(item).upper())
    animal = product_to_animal.get(str(item).upper())
    total = 0
    for row in (farms[1 - player].get("tiles") or []):
        for tile in row or []:
            if not isinstance(tile, dict):
                continue
            if crop is not None and tile.get("crop") != crop:
                continue
            if animal is not None and tile.get("animal") != animal:
                continue
            if crop is None and animal is None:
                continue
            try:
                total += max(0, int(tile.get("yield_units", 0)))
            except (TypeError, ValueError):
                continue
    return total


def _normalise_action(action: Any) -> dict[str, list]:
    if not isinstance(action, dict):
        return {"farmer": ["PASS"], "hands": [], "market": []}
    return {
        "farmer": list(action.get("farmer") or ["PASS"]),
        "hands": [list(item or ["PASS"])
                  for item in (action.get("hands") or [])],
        "market": [list(order) for order in (action.get("market") or [])],
    }


def _sell_amount(order: list, item: str) -> int:
    if len(order) < 3 or order[0] != "SELL" or order[1] != item:
        return 0
    try:
        return max(0, int(order[2]))
    except (TypeError, ValueError):
        return 0


def _suppress_due(action: dict, due: dict[str, int]) -> None:
    if not due:
        return
    kept = []
    for raw in action["market"]:
        order = list(raw)
        if len(order) >= 3 and order[0] == "SELL":
            item = str(order[1]).upper()
            remove = min(_sell_amount(order, item), due.get(item, 0))
            if remove:
                order[2] = max(0, int(order[2]) - remove)
                due[item] -= remove
        try:
            empty_sell = (len(order) >= 3 and order[0] == "SELL"
                          and int(order[2]) <= 0)
        except (TypeError, ValueError):
            empty_sell = False
        if not empty_sell:
            kept.append(order)
    action["market"] = kept


def _future_sale_plan(frame: dict, item: str) -> int:
    total = 0
    for raw in frame.get("market") or []:
        if len(raw) >= 3 and raw[0] == "SELL" and str(raw[1]).upper() == item:
            try:
                total += max(0, int(raw[2]))
            except (TypeError, ValueError):
                continue
    return total


def _has_future_pickup(frame: dict, item: str) -> bool:
    commands = [frame.get("farmer") or ["PASS"], *(frame.get("hands") or [])]
    return any(len(command) > 1 and command[0] == "PICKUP"
               and str(command[1]).upper() == item for command in commands)


def _racegate_sell_totals(action: dict) -> dict[str, int]:
    totals: dict[str, int] = {}
    for order in action.get("market") or []:
        if (isinstance(order, (list, tuple)) and len(order) >= 3
                and str(order[0]).upper() == "SELL"):
            item = str(order[1]).upper()
            totals[item] = totals.get(item, 0) + _sell_amount(list(order), item)
    return totals


def _opfr_sell_totals(action: dict) -> dict[str, int]:
    totals: dict[str, int] = {}
    for order in action.get("market") or []:
        if (isinstance(order, (list, tuple)) and len(order) >= 3
                and str(order[0]).upper() == "SELL"):
            item = str(order[1]).upper()
            totals[item] = totals.get(item, 0) + _sell_amount(
                list(order), item)
    return totals


def opponent_front_run(observation: dict, action: dict,
                       configuration=None, tape=None) -> dict:
    """Advance one future tape sale after observing a rival's supply.

    This is a deliberately narrow adaptation of the public H4/H5 idea.  It
    does not assume that the opponent follows a replay.  It first estimates
    rival supply from the public market-inventory delta, subtracting our
    executed/requested supply and known town demand.  Only after the signal
    is observed does it add a sale for a future tape sale, and only on a
    pure-SELL (or empty) market queue.  The operator never changes worker
    actions or removes the future tape order.

    It is intentionally opt-in: the default configuration requires no
    evidence and therefore returns the input action unchanged when no tape is
    supplied.  Callers should evaluate it as a separate market arm before
    promotion.
    """
    OPPONENT_FRONT_RUN_TELEMETRY["calls"] += 1
    if int(observation.get("step", 0)) == 0:
        _OPPONENT_FRONT_RUN_STATE.clear()
        OPPONENT_FRONT_RUN_TELEMETRY.update(
            evidence=0, changed_turns=0, advanced_units=0, abstains=0)

    actions = _actions(tape)
    if not actions:
        OPPONENT_FRONT_RUN_TELEMETRY["abstains"] += 1
        return action

    step = int(observation.get("step", 0))
    player = int(observation.get("player", 0))
    route_id = str(getattr(tape, "route_id", "tape"))
    key = (player, route_id)
    state = _OPPONENT_FRONT_RUN_STATE.get(key)
    if state is None or step <= int(state.get("step", -1)):
        state = {
            "step": -1,
            "last_inventory": {},
            "last_prices": {},
            "last_shops": (),
            "last_shed": {},
            "last_sold": {},
            "evidence": 0,
            "active": False,
            "done_targets": set(),
        }
        _OPPONENT_FRONT_RUN_STATE[key] = state

    cfg = configuration if isinstance(configuration, dict) else {}
    configured_items = cfg.get("opponent_front_run_items")
    if isinstance(configured_items, str):
        configured_items = configured_items.split(",")
    items = tuple(str(item).upper() for item in (
        configured_items or ("MELON", "STRAWBERRY", "MILK", "WOOL")
    ) if str(item).upper() in BASE_PRICES)
    min_own = max(1, int(cfg.get("opponent_front_run_min_own", 2)))
    min_rival = max(1, int(cfg.get("opponent_front_run_min_rival", 2)))
    min_evidence = max(1, int(cfg.get("opponent_front_run_min_evidence", 1)))
    min_price = max(0.0, float(cfg.get("opponent_front_run_min_price", 1.0)))
    ratio_low = max(0.0, float(cfg.get("opponent_front_run_ratio_low", 0.40)))
    ratio_high = max(ratio_low, float(
        cfg.get("opponent_front_run_ratio_high", 2.50)))
    target_offset = max(1, int(cfg.get("opponent_front_run_offset", 5)))
    result = _normalise_action(action)
    market = result.get("market") or []

    market_data = observation.get("market") or {}
    inventory = market_data.get("inventory") or {}
    prices = market_data.get("prices") or {}
    shops = tuple((observation.get("town") or {}).get(
        "unlocked_shops") or ())

    # Infer rival supply from the previous public market transition.  This is
    # only used as a gate; it never directly determines the quantity sold.
    if int(state.get("step", -1)) == step - 1:
        previous_inventory = state.get("last_inventory") or {}
        previous_prices = state.get("last_prices") or {}
        previous_shed = state.get("last_shed") or {}
        previous_sold = state.get("last_sold") or {}
        previous_shops = state.get("last_shops") or ()
        for item in items:
            if (float(previous_prices.get(item, 0.0) or 0.0) <= min_price
                    or float(prices.get(item, 0.0) or 0.0) <= min_price):
                continue
            own_supply = min(
                max(0, int(previous_shed.get(item, 0) or 0)),
                max(0, int(previous_sold.get(item, 0) or 0)),
            )
            if own_supply < min_own:
                continue
            demand = _adaptive_demand(
                {"town": {"unlocked_shops": previous_shops}},
                item, step - 1)
            observed_delta = (int(inventory.get(item, 0) or 0)
                              - int(previous_inventory.get(item, 0) or 0))
            rival_supply = observed_delta + demand - own_supply
            if (rival_supply >= min_rival
                    and ratio_low <= rival_supply / max(1, own_supply)
                    <= ratio_high):
                state["evidence"] = int(state.get("evidence", 0)) + 1
                OPPONENT_FRONT_RUN_TELEMETRY["evidence"] += 1
        if int(state.get("evidence", 0)) >= min_evidence:
            state["active"] = True

    state["last_inventory"] = {
        str(item).upper(): int(value) for item, value in inventory.items()
    }
    state["last_prices"] = {
        str(item).upper(): float(value) for item, value in prices.items()
    }
    state["last_shops"] = shops
    state["last_shed"] = {
        str(item).upper(): int(value)
        for item, value in (((observation.get("private") or {}).get(
            "shed") or {}).items())
    }
    state["last_sold"] = _opfr_sell_totals(result)
    state["step"] = step

    if not state.get("active") or step + target_offset >= len(actions):
        return result
    if any(not isinstance(order, (list, tuple)) or not order
           or str(order[0]).upper() != "SELL" for order in market):
        return result
    if len(market) >= 10:
        return result

    target = step + target_offset
    if target in state["done_targets"]:
        return result
    future = actions[target]
    planned: dict[str, int] = {}
    for order in future.get("market") or []:
        if (isinstance(order, (list, tuple)) and len(order) >= 3
                and str(order[0]).upper() == "SELL"):
            item = str(order[1]).upper()
            if item in items:
                planned[item] = planned.get(item, 0) + _sell_amount(
                    list(order), item)
    if not planned:
        return result

    # Do not pre-sell an item that the tape must pick up before the target.
    for offset in range(1, target_offset):
        frame = actions[step + offset]
        if any(_has_future_pickup(frame, item) for item in planned):
            return result

    shed = ((observation.get("private") or {}).get("shed") or {})
    current_sells = _opfr_sell_totals(result)
    shops_now = tuple((observation.get("town") or {}).get(
        "unlocked_shops") or ())
    choices = []
    for item, quantity in planned.items():
        if _adaptive_demand({"town": {"unlocked_shops": shops_now}},
                            item, step) > 0:
            continue
        available = max(0, int(shed.get(item, 0) or 0)
                        - current_sells.get(item, 0))
        quantity = min(available, quantity)
        if quantity <= 0:
            continue
        price = float(prices.get(item, 0.0) or 0.0)
        choices.append((price * quantity, item, quantity))
    if not choices:
        return result
    _, item, quantity = max(choices)
    result["market"].append(["SELL", item, quantity])
    state["done_targets"].add(target)
    OPPONENT_FRONT_RUN_TELEMETRY["changed_turns"] += 1
    OPPONENT_FRONT_RUN_TELEMETRY["advanced_units"] += quantity
    return result


def racegate_reservation(observation: dict, action: dict,
                         configuration=None, tape=None) -> dict:
    """Reserve future tape sales when the current quote is not glutted.

    This is a portable approximation of Thomas's RACEGATE layer.  It reserves
    physically available shed stock for a future ``SELL`` in the selected tape,
    then removes the corresponding future order when that due turn arrives.
    It intentionally abstains when the quote is at/below base, when a current
    task picks up the item, or when the market queue is full.
    """
    if int(observation.get("step", 0)) == 0:
        TELEMETRY.update(calls=0, reservations=0, reserved_units=0,
                         suppressed_units=0, quote_abstains=0)
    TELEMETRY["calls"] += 1
    actions = _actions(tape)
    if not actions:
        return _normalise_action(action)
    step = int(observation.get("step", 0))
    player = int(observation.get("player", 0))
    route_id = str(getattr(tape, "route_id", "tape"))
    key = (player, route_id)
    state = _STATE.get(key)
    if state is None or step <= int(state.get("step", -1)):
        state = {
            "step": -1,
            "debts": {},
            "last_inventory": {},
            "last_sold": {},
            "dynamic_horizon": None,
        }
        _STATE[key] = state

    result = _normalise_action(action)
    due = state["debts"].pop(step, {})
    before_due = sum(max(0, int(value)) for value in due.values())
    _suppress_due(result, due)
    TELEMETRY["suppressed_units"] += max(
        0, before_due - sum(max(0, int(value)) for value in due.values()))

    try:
        cfg = configuration if isinstance(configuration, dict) else {}
        inventory = (observation.get("market") or {}).get("inventory") or {}
        if cfg.get("race_dynamic_horizon") and int(state.get("step", -1)) == step - 1:
            trigger = max(1, int(cfg.get("race_trigger_sales", 2)))
            rival_supply = 0
            for item in RACE_ITEMS:
                delta = (int(inventory.get(item, 0))
                         - int(state.get("last_inventory", {}).get(item, 0)))
                own_sold = int(state.get("last_sold", {}).get(item, 0))
                rival_supply = max(rival_supply, delta - own_sold)
            if rival_supply >= trigger:
                state["dynamic_horizon"] = max(
                    1, int(cfg.get("race_trigger_horizon", 40)))
        state["last_inventory"] = {
            str(item).upper(): int(amount)
            for item, amount in inventory.items()
        }
        state["last_sold"] = _racegate_sell_totals(result)
        state["step"] = step
    except (AttributeError, TypeError, ValueError):
        state["step"] = step

    if not 192 <= step < 696 or step >= len(actions):
        return result
    prices = (observation.get("market") or {}).get("prices") or {}
    shed = ((observation.get("private") or {}).get("shed") or {})
    commands = [result.get("farmer") or ["PASS"], *(result.get("hands") or [])]
    blocked = {str(order[1]).upper() for order in result["market"]
               if len(order) > 1 and order[0] in ("SELL", "BUY_PRODUCT")}
    blocked.update(str(command[1]).upper() for command in commands
                   if len(command) > 1 and command[0] == "PICKUP")
    if any(len(command) > 1 and command[0] == "PLACE"
           and str(command[1]).upper() in {"COW", "SHEEP", "GOOSE"}
           for command in commands):
        return result

    horizon = 40
    max_horizon = 48
    min_offset = 1
    try:
        horizon = max(1, int((configuration or {}).get("race_default", horizon)))
        max_horizon = max(horizon, int((configuration or {}).get("race_max", max_horizon)))
        min_offset = max(1, int((configuration or {}).get("race_min_offset", min_offset)))
        if ((configuration or {}).get("race_dynamic_horizon")
                and state.get("dynamic_horizon") is not None):
            horizon = max(horizon, int(state["dynamic_horizon"]))
    except (AttributeError, TypeError, ValueError):
        pass
    end = min(len(actions) - 1, 695, step + max_horizon)
    for item in RACE_ITEMS:
        if item in blocked:
            continue
        try:
            price = int(prices.get(item, 0))
            available = max(0, int(shed.get(item, 0)))
        except (TypeError, ValueError):
            continue
        if price <= BASE_PRICES[item] or available <= 0:
            if available > 0 and price <= BASE_PRICES[item]:
                TELEMETRY["quote_abstains"] += 1
            continue
        reservations = []
        item_end = min(end, step + horizon)
        for due_step in range(step + min_offset, item_end + 1):
            future = actions[due_step]
            if _has_future_pickup(future, item):
                break
            planned = _future_sale_plan(future, item)
            amount = min(available, max(0, planned - state["debts"].get(
                due_step, {}).get(item, 0)))
            if amount:
                reservations.append((due_step, amount))
                available -= amount
            if not available:
                break
        quantity = sum(amount for _, amount in reservations)
        if not quantity or len(result["market"]) >= 10:
            continue
        result["market"].append(["SELL", item, quantity])
        TELEMETRY["reservations"] += 1
        TELEMETRY["reserved_units"] += quantity
        for due_step, amount in reservations:
            state["debts"].setdefault(due_step, {})[item] = (
                state["debts"].setdefault(due_step, {}).get(item, 0) + amount
            )
    return result


def sale_advance(observation: dict, action: dict,
                 configuration=None, tape=None) -> dict:
    """Sell available stock ahead of a selected Tape's planned sale.

    This is the portable version of the public EXP293 idea.  It deliberately
    uses only the live shed, current market orders, and the selected Tape's
    future market schedule.  It never treats a future sale as cash and never
    invents stock.  The later Tape SELL is left in place: after the advance,
    the engine naturally sells only whatever stock remains.

    The operator is intentionally conservative at day-end and shop-opening
    boundaries.  The first future SELL item is protected because public
    routes often use that sale to fund an immediately following purchase.
    """
    if int(observation.get("step", 0)) == 0:
        ADVANCE_TELEMETRY.update(
            calls=0, changed_turns=0, advanced_units=0, abstains=0,
            events=[])
    ADVANCE_TELEMETRY["calls"] += 1
    result = _normalise_action(action)
    actions = _actions(tape)
    if not actions:
        ADVANCE_TELEMETRY["abstains"] += 1
        return result

    step = int(observation.get("step", 0))
    turns_per_day = 24
    first_day = 6
    last_step = min(718, len(actions) - 1)
    lookahead = 14
    min_sell_price = 2
    require_base_price = False
    shop_cycle_guard = False
    max_items = None
    abstain_on_weed = False
    sale_items = SALE_ADVANCE_ITEMS
    base_price_items = ()
    require_empty_market = False
    dynamic_weed = False
    dynamic_context = False
    exact_curve = False
    value_horizon = 8
    value_margin = 0.0
    robust_curve = False
    robust_rival_floor = 8
    robust_rival_cap = 24
    protect_first_sale = True
    require_cash_non_decrease = False
    disable_near_mirror = False
    mirror_latch_step = 289
    mirror_composition_distance = 2
    mirror_money_distance = 250.0
    rival_yield_gate = None
    min_future_quantity = 0
    expand_cash_threshold = None
    expand_shed_threshold = None
    day_tail_guard = 1
    shop_demand_lookahead = None
    min_market_excess = None
    try:
        cfg = configuration or {}
        turns_per_day = max(1, int(cfg.get("turnsPerDay", turns_per_day)))
        first_day = max(0, int(cfg.get("sale_advance_first_day", first_day)))
        lookahead = max(1, int(cfg.get("sale_advance_lookahead", lookahead)))
        min_sell_price = max(0, int(cfg.get(
            "sale_advance_min_sell_price", min_sell_price)))
        require_base_price = bool(cfg.get(
            "sale_advance_require_base_price", require_base_price))
        configured_base_items = cfg.get("sale_advance_base_price_items")
        if configured_base_items:
            if isinstance(configured_base_items, str):
                configured_base_items = configured_base_items.split(",")
            base_price_items = tuple(
                str(item).upper() for item in configured_base_items
                if str(item).upper() in SALE_ADVANCE_ITEMS)
        require_empty_market = bool(cfg.get(
            "sale_advance_require_empty_market", require_empty_market))
        shop_cycle_guard = bool(cfg.get(
            "sale_advance_shop_cycle_guard", shop_cycle_guard))
        configured_max_items = cfg.get("sale_advance_max_items")
        if configured_max_items is not None:
            max_items = max(1, int(configured_max_items))
        abstain_on_weed = bool(cfg.get(
            "sale_advance_abstain_on_weed", abstain_on_weed))
        configured_items = cfg.get("sale_advance_items")
        if configured_items:
            if isinstance(configured_items, str):
                configured_items = configured_items.split(",")
            sale_items = tuple(
                str(item).upper() for item in configured_items
                if str(item).upper() in SALE_ADVANCE_ITEMS)
        dynamic_weed = bool(cfg.get("sale_advance_dynamic_weed", False))
        dynamic_context = bool(cfg.get("sale_advance_dynamic_context", False))
        exact_curve = bool(cfg.get("sale_advance_use_exact_curve", False))
        value_horizon = max(1, int(cfg.get(
            "sale_advance_value_horizon", value_horizon)))
        value_margin = max(0.0, float(cfg.get(
            "sale_advance_value_margin", value_margin)))
        robust_curve = bool(cfg.get(
            "sale_advance_use_robust_curve", robust_curve))
        robust_rival_floor = max(0, int(cfg.get(
            "sale_advance_robust_rival_floor", robust_rival_floor)))
        robust_rival_cap = max(robust_rival_floor, int(cfg.get(
            "sale_advance_robust_rival_cap", robust_rival_cap)))
        protect_first_sale = bool(cfg.get(
            "sale_advance_protect_first_sale", protect_first_sale))
        require_cash_non_decrease = bool(cfg.get(
            "sale_advance_require_cash_non_decrease",
            require_cash_non_decrease))
        disable_near_mirror = bool(cfg.get(
            "sale_advance_disable_near_mirror", disable_near_mirror))
        mirror_latch_step = max(0, int(cfg.get(
            "sale_advance_mirror_latch_step", mirror_latch_step)))
        mirror_composition_distance = max(0, int(cfg.get(
            "sale_advance_mirror_composition_distance",
            mirror_composition_distance)))
        mirror_money_distance = max(0.0, float(cfg.get(
            "sale_advance_mirror_money_distance", mirror_money_distance)))
        if cfg.get("sale_advance_min_rival_yield") is not None:
            rival_yield_gate = max(0, int(
                cfg.get("sale_advance_min_rival_yield")))
        min_future_quantity = max(0, int(cfg.get(
            "sale_advance_min_future_quantity", min_future_quantity)))
        if cfg.get("sale_advance_expand_all_below_cash") is not None:
            expand_cash_threshold = float(
                cfg.get("sale_advance_expand_all_below_cash"))
        if cfg.get("sale_advance_expand_all_above_shed") is not None:
            expand_shed_threshold = max(0, int(
                cfg.get("sale_advance_expand_all_above_shed")))
        day_tail_guard = max(1, int(cfg.get(
            "sale_advance_day_tail_guard", day_tail_guard)))
        if cfg.get("sale_advance_shop_demand_lookahead") is not None:
            shop_demand_lookahead = max(1, int(
                cfg.get("sale_advance_shop_demand_lookahead")))
        if cfg.get("sale_advance_min_market_excess") is not None:
            min_market_excess = int(
                cfg.get("sale_advance_min_market_excess"))
        if configured_items and (
                (expand_cash_threshold is not None and
                 float((observation.get("farms") or [])[int(
                     observation.get("player", 0))].get("money", 0))
                 <= expand_cash_threshold)
                or (expand_shed_threshold is not None and
                    sum(max(0, int(value)) for value in
                        ((observation.get("private") or {}).get(
                            "shed", {}) or {}).values())
                    >= expand_shed_threshold)):
            sale_items = SALE_ADVANCE_ITEMS
        if dynamic_context and not configured_items:
            # Use the conservative arm until the public shop regime or the
            # board state justifies exposing the milk arm.
            sale_items = (SALE_ADVANCE_ITEMS if
                          (_visible_weed(observation) or
                           _visible_milk_shop(observation)) else
                          _NO_MILK_SALE_ITEMS)
        if dynamic_weed and not configured_items:
            sale_items = _NO_MILK_SALE_ITEMS
            if _visible_weed(observation):
                sale_items = SALE_ADVANCE_ITEMS
        last_step = min(last_step, int(cfg.get("episodeSteps", 720)) - 2)
    except (AttributeError, TypeError, ValueError):
        pass
    if (step < first_day * turns_per_day
            or step >= last_step
            or step % turns_per_day >= turns_per_day - day_tail_guard):
        ADVANCE_TELEMETRY["abstains"] += 1
        return result

    if abstain_on_weed and _visible_weed(observation):
        ADVANCE_TELEMETRY["abstains"] += 1
        return result

    # In a near-symmetric public board state, advancing a sale can mainly
    # move both players' supply into the same market regime.  The public
    # adaptive strategy uses a similar mirror latch.  Keep this opt-in: it is
    # a risk control for experiments, not an assumption that symmetry is
    # always bad.
    if (disable_near_mirror and step >= mirror_latch_step
            and _adaptive_near_mirror(
                observation, mirror_composition_distance,
                mirror_money_distance)):
        ADVANCE_TELEMETRY["abstains"] += 1
        return result

    shops = list((observation.get("town") or {}).get("unlocked_shops") or [])
    # Demand-preserving public variant: once two bakeries are open, the
    # short shop cycle makes a long speculative lookahead less reliable.
    active_lookahead = (
        3 if shop_cycle_guard and shops.count("BAKERY") >= 2 else lookahead)

    market = result["market"]
    baseline_market = [list(order) for order in market]
    if require_empty_market and market:
        ADVANCE_TELEMETRY["abstains"] += 1
        return result
    # Do not move stock in front of a product purchase.  The purchase may be
    # deliberately indexed against the original queue, and the public
    # evidence did not establish that reordering such a turn is safe.
    if any(len(order) > 0 and order[0] == "BUY_PRODUCT" for order in market):
        ADVANCE_TELEMETRY["abstains"] += 1
        return result

    prices = (observation.get("market") or {}).get("prices") or {}
    market_inventory = ((observation.get("market") or {}).get(
        "inventory") or {})
    shed = ((observation.get("private") or {}).get("shed") or {})
    current_sells: dict[str, int] = {}
    for order in market:
        if len(order) < 3 or order[0] != "SELL":
            continue
        item = str(order[1]).upper()
        current_sells[item] = current_sells.get(item, 0) + _sell_amount(order, item)

    # Preserve the first future sale's item.  This is a narrow guard against
    # breaking a same-turn financing pattern while allowing later sales to be
    # advanced.
    first_market_order = None
    for offset in range(1, active_lookahead + 1):
        future_step = step + offset
        if future_step > last_step:
            break
        future = actions[future_step]
        if future.get("market"):
            first_market_order = future["market"][0]
            break
    protected = None
    if (isinstance(first_market_order, list)
            and len(first_market_order) > 1
            and first_market_order[0] == "SELL"):
        protected = str(first_market_order[1]).upper()

    planned: dict[str, int] = {}
    first_due: dict[str, int] = {}
    for offset in range(1, active_lookahead + 1):
        future_step = step + offset
        if future_step > last_step:
            break
        future = actions[future_step]
        for order in future.get("market") or []:
            if len(order) < 3 or order[0] != "SELL":
                continue
            item = str(order[1]).upper()
            if (shop_demand_lookahead is not None
                    and offset > shop_demand_lookahead
                    and any(item in _SALE_ADVANCE_SHOP_PRODUCTS.get(shop, ())
                            for shop in shops)):
                continue
            if (item not in sale_items
                    or (protect_first_sale and item == protected)):
                continue
            if (shop_cycle_guard and offset >= 5 and item == "WOOL"
                    and "YARN_STORE" in shops):
                continue
            try:
                quantity = max(0, int(order[2]))
            except (TypeError, ValueError):
                quantity = 0
            planned[item] = planned.get(item, 0) + quantity
            first_due[item] = min(first_due.get(item, offset), offset)
    if not planned:
        ADVANCE_TELEMETRY["abstains"] += 1
        return result

    # Choose expensive products first, matching the public operator's bounded
    # market-slot policy and keeping lower-value inventory available for later
    # demand if the queue is full.
    additions: list[list] = []
    event_items: list[dict[str, int | str]] = []
    advanced = 0
    selected_items = 0
    for item in sorted(planned, key=lambda name: -int(prices.get(name, 0))):
        if max_items is not None and selected_items >= max_items:
            break
        if planned[item] < min_future_quantity:
            continue
        try:
            price = int(prices.get(item, 0))
            available = max(0, int(shed.get(item, 0)))
        except (TypeError, ValueError):
            continue
        available = max(0, available - current_sells.get(item, 0))
        threshold = max(min_sell_price,
                        BASE_PRICES[item]
                        if (require_base_price or item in base_price_items)
                        else 0)
        if price < threshold or available <= 0:
            continue
        if (rival_yield_gate is not None
                and _visible_rival_yield(observation, item)
                < rival_yield_gate):
            continue
        if min_market_excess is not None:
            try:
                market_excess = int(market_inventory.get(item, 10000)) - 10000
            except (TypeError, ValueError):
                continue
            if market_excess < min_market_excess:
                continue
        quantity = min(available, planned[item])
        if quantity <= 0:
            continue
        if exact_curve:
            # Compare each possible prefix, rather than accepting the full
            # future-sale quantity as one indivisible tranche.  This keeps a
            # profitable part of an advance while retaining units whose
            # future quote is expected to improve through town demand.
            try:
                inventory_now = int(market_inventory.get(item, 10000))
                current_value = 0.0
                future_value = 0.0
                demand = 0
                item_horizon = min(
                    value_horizon, max(1, int(first_due.get(item,
                                                          value_horizon))))
                for future_step in range(
                        step + 1, step + item_horizon + 1):
                    demand += _adaptive_demand(
                        observation, item, future_step)
                future_inventory = max(0, inventory_now - demand)
                accepted = 0
                for offset in range(quantity):
                    current_value += _frontload_price(
                        item, inventory_now + offset)
                    future_value += _frontload_price(
                        item, future_inventory + offset)
                    if current_value + 1e-9 >= future_value * (
                            1.0 + value_margin):
                        accepted = offset + 1
                quantity = min(quantity, accepted)
            except (TypeError, ValueError, KeyError):
                quantity = 0
        if robust_curve and quantity > 0:
            # Compare the current sale with the same prefix at its first
            # planned Tape sale.  The rival batch is intentionally a bounded
            # scenario, not an attempt to observe private rival inventory.
            # A floor makes the test conservative when the rival shed is
            # hidden; the visible yield is only allowed to increase pressure.
            try:
                inventory_now = int(market_inventory.get(item, 10000))
                due_offset = max(1, int(first_due.get(item, value_horizon)))
                demand = sum(
                    _adaptive_demand(observation, item, future_step)
                    for future_step in range(
                        step + 1,
                        step + min(value_horizon, due_offset) + 1)
                )
                rival_batch = min(
                    robust_rival_cap,
                    max(robust_rival_floor,
                        _visible_rival_yield(observation, item)),
                )
                future_inventory = max(
                    0, inventory_now - demand + rival_batch)
                now_value = future_value = 0.0
                accepted = 0
                for offset in range(quantity):
                    now_value += _frontload_price(
                        item, inventory_now + offset)
                    future_value += _frontload_price(
                        item, future_inventory + offset)
                    if now_value + 1e-9 >= future_value * (
                            1.0 + value_margin):
                        accepted = offset + 1
                quantity = min(quantity, accepted)
            except (TypeError, ValueError, KeyError):
                quantity = 0
        if quantity <= 0:
            continue
        existing = next(
            (order for order in market
             if len(order) >= 2 and order[0] == "SELL"
             and str(order[1]).upper() == item),
            None,
        )
        if existing is not None:
            try:
                existing[2] = int(existing[2]) + quantity
            except (TypeError, ValueError):
                continue
        elif len(market) + len(additions) < 10:
            additions.append(["SELL", item, quantity])
        else:
            continue
        advanced += quantity
        selected_items += 1
        event_items.append({
            "step": step,
            "item": item,
            "price": price,
            "planned": int(planned[item]),
            "available": int(available + quantity),
            "quantity": int(quantity),
            "bakery_count": int(shops.count("BAKERY")),
            "yarn_open": int("YARN_STORE" in shops),
        })

    if not advanced:
        ADVANCE_TELEMETRY["abstains"] += 1
        return result
    if require_cash_non_decrease:
        try:
            player = int(observation.get("player", 0))
            farms = observation.get("farms") or []
            farm = farms[player]
            money = float(farm.get("money", 0))
            shed_total = sum(
                max(0, int(value))
                for value in (observation.get("private") or {})
                .get("shed", {}).values())
            inventory = {
                key: int(value)
                for key, value in (observation.get("market") or {})
                .get("inventory", {}).items()
            }
            hires_today = int(farm.get("hires_today", 0))
            extra_land = max(
                0, len(farm.get("unlocked_quadrants", ["NW"])) - 1)
            candidate_market = additions + market
            for pressure in (0, 1):
                before = _frontload_outcome(
                    baseline_market, money, shed_total, inventory,
                    hires_today, extra_land, pressure)
                after = _frontload_outcome(
                    candidate_market, money, shed_total, inventory,
                    hires_today, extra_land, pressure)
                if (after is None or not isinstance(after, tuple)
                        or (before is not None
                            and (not isinstance(before, tuple)
                                 or float(after[0]) + 1e-9
                                 < float(before[0])))):
                    ADVANCE_TELEMETRY["abstains"] += 1
                    return dict(result, market=baseline_market)
        except (AttributeError, TypeError, ValueError, IndexError):
            ADVANCE_TELEMETRY["abstains"] += 1
            return dict(result, market=baseline_market)
    ADVANCE_TELEMETRY["changed_turns"] += 1
    ADVANCE_TELEMETRY["advanced_units"] += advanced
    # Keep the trace bounded for long matches and avoid retaining mutable
    # action/observation objects.
    events = ADVANCE_TELEMETRY.setdefault("events", [])
    events.extend(event_items)
    del events[:-256]
    return dict(result, market=additions + market)


def _sale_advance_policy_context(observation: dict) -> tuple[str, str]:
    shops = tuple(
        str(shop).upper()
        for shop in ((observation.get("town") or {}).get(
            "unlocked_shops") or [])[:2]
    )
    day_bucket = max(0, int(observation.get("step", 0))) // 24 // 2
    shop_key = "|".join(shops) if shops else "global"
    return shop_key, f"{shop_key}|day{day_bucket}"


def _sale_advance_policy_stats(candidate: dict, keys: tuple[str, ...]
                               ) -> dict[str, float]:
    evidence = candidate.get("evidence") or {}
    if not isinstance(evidence, dict):
        return {}
    contexts = evidence.get("contexts") or {}
    raw = None
    if isinstance(contexts, dict):
        for key in keys:
            if isinstance(contexts.get(key), dict):
                raw = contexts[key]
                break
    if raw is None and isinstance(evidence.get("global"), dict):
        raw = evidence["global"]
    if not isinstance(raw, dict):
        return {}
    try:
        count = max(0, int(raw.get("count", 0)))
        mean = float(raw.get("mean", 0.0))
        variance = max(0.0, float(raw.get("variance", 0.0)))
        failures = max(0, int(raw.get("hard_failures", 0)))
    except (TypeError, ValueError):
        return {}
    standard_error = math.sqrt(variance / count) if count else float("inf")
    return {
        "count": float(count),
        "mean": mean,
        "lcb90": mean - 1.645 * standard_error if count else float("-inf"),
        "ucb90": mean + 1.645 * standard_error if count else float("inf"),
        "hard_failures": float(failures),
    }


def sale_advance_policy(observation: dict, action: dict,
                        configuration=None, tape=None) -> dict:
    """Select an evidence-qualified sale-advance configuration by context.

    Candidates are evaluated offline against a paired incumbent and supplied
    as ``sale_advance_policy_candidates``.  A candidate needs enough samples,
    no hard failures, and a strictly positive 90% lower confidence bound in
    the current shop/day context.  With no qualified candidate this is exactly
    the ordinary configured ``sale_advance`` path.
    """
    cfg = dict(configuration) if isinstance(configuration, dict) else {}
    candidates = cfg.pop("sale_advance_policy_candidates", None)
    if isinstance(candidates, (list, tuple)):
        shop_key, exact_key = _sale_advance_policy_context(observation)
        try:
            min_count = max(1, int(
                cfg.get("sale_advance_policy_min_count", 20)))
        except (TypeError, ValueError):
            min_count = 20
        eligible: list[tuple[tuple[float, float, float, str], dict]] = []
        for candidate in candidates:
            if not isinstance(candidate, dict):
                continue
            candidate_config = candidate.get("config")
            if not isinstance(candidate_config, dict):
                continue
            stats = _sale_advance_policy_stats(
                candidate, (exact_key, shop_key, "global"))
            if (stats.get("count", 0.0) < min_count
                    or stats.get("hard_failures", 1.0) > 0.0
                    or stats.get("lcb90", float("-inf")) <= 0.0):
                continue
            eligible.append((
                (stats["lcb90"], stats["mean"], stats["ucb90"],
                 str(candidate.get("id", ""))),
                candidate_config,
            ))
        if eligible:
            _, selected = max(eligible, key=lambda item: item[0])
            cfg.update(selected)
    return sale_advance(observation, action, cfg, tape)


def _budget_fibonacci(index: int) -> int:
    """Return the engine's 1, 1, 2, 3, ... Farm Hand cost sequence."""
    a, b = 1, 1
    for _ in range(max(0, int(index))):
        a, b = b, a + b
    return a


def _budget_order_quantity(order: Any) -> int:
    if not isinstance(order, (list, tuple)) or len(order) < 3:
        return 1
    try:
        return max(1, int(order[2]))
    except (TypeError, ValueError):
        return 1


def _budget_future_sell_total(actions: tuple[dict, ...], item: str,
                              start: int, end: int) -> int:
    total = 0
    for frame in actions[max(0, int(start)):max(0, int(end))]:
        if not isinstance(frame, dict):
            continue
        for raw in frame.get("market") or []:
            if (isinstance(raw, (list, tuple)) and len(raw) >= 3
                    and str(raw[0]).upper() == "SELL"
                    and str(raw[1]).upper() == item):
                try:
                    total += max(0, int(raw[2]))
                except (TypeError, ValueError):
                    continue
    return total


def _budget_block_requirements(actions: tuple[dict, ...],
                               observation: dict, start: int, end: int,
                               turns_per_day: int) -> tuple[float, dict[str, int]]:
    """Estimate purchases and peak input reserves in ``[start, end)``.

    The calculation intentionally follows the public guard's conservative
    accounting: inputs are consumed by the tape and replenished only by
    explicit BUY orders.  Existing shed/carried stock is applied later as a
    protection amount, so this helper itself remains independent of hidden
    route state.
    """
    budget = 0.0
    seed_balance: dict[str, int] = {}
    item_balance: dict[str, int] = {}
    seed_need: dict[str, int] = {}
    item_need: dict[str, int] = {}
    hires_by_day: dict[int, int] = {}
    player = int(observation.get("player", 0))
    farms = observation.get("farms") or []
    farm = farms[player] if 0 <= player < len(farms) else {}
    current_hires = max(0, int(farm.get("hires_today", 0) or 0))
    quadrants = max(1, len(farm.get("unlocked_quadrants") or ["NW"]))

    begin = max(0, int(start))
    finish = min(max(begin, int(end)), len(actions))
    for step in range(begin, finish):
        frame = actions[step]
        if not isinstance(frame, dict):
            continue
        commands = [frame.get("farmer") or ["PASS"]]
        commands.extend(frame.get("hands") or [])
        for raw in commands:
            if not isinstance(raw, (list, tuple)) or not raw:
                continue
            operation = str(raw[0]).upper()
            item = (str(raw[1]).upper() if len(raw) > 1
                    and raw[1] is not None else None)
            quantity = _budget_order_quantity(raw)
            if operation == "PLANT" and item in _BUDGET_SEED_PRICE:
                seed_balance[item] = seed_balance.get(item, 0) - 1
                seed_need[item] = max(
                    seed_need.get(item, 0), -seed_balance[item])
            elif operation == "FEED":
                item_balance["WHEAT"] = item_balance.get("WHEAT", 0) - 1
                item_need["WHEAT"] = max(
                    item_need.get("WHEAT", 0), -item_balance["WHEAT"])
            elif operation == "FERTILIZE":
                item_balance["FERTILIZER"] = (
                    item_balance.get("FERTILIZER", 0) - 1)
                item_need["FERTILIZER"] = max(
                    item_need.get("FERTILIZER", 0),
                    -item_balance["FERTILIZER"])
            elif operation == "PLACE" and item is not None:
                item_balance[item] = item_balance.get(item, 0) - quantity
                item_need[item] = max(
                    item_need.get(item, 0), -item_balance[item])

        for raw in frame.get("market") or []:
            if not isinstance(raw, (list, tuple)) or not raw:
                continue
            operation = str(raw[0]).upper()
            item = (str(raw[1]).upper() if len(raw) > 1
                    and raw[1] is not None else None)
            quantity = _budget_order_quantity(raw)
            if operation == "HIRE":
                day = (step - begin) // max(1, int(turns_per_day))
                hires_by_day[day] = hires_by_day.get(day, 0) + quantity
            elif operation == "BUY_LAND":
                extra = quadrants - 1
                if 0 <= extra < len(_BUDGET_LAND_PRICES):
                    budget += _BUDGET_LAND_PRICES[extra] * quantity
                    quadrants += quantity
            elif operation == "BUY_SEED" and item in _BUDGET_SEED_PRICE:
                budget += _BUDGET_SEED_PRICE[item] * quantity
                seed_balance[item] = seed_balance.get(item, 0) + quantity
            elif operation == "BUY_PRODUCT" and item in (
                    "WHEAT", "FERTILIZER"):
                prices = ((observation.get("market") or {}).get(
                    "prices") or {})
                try:
                    budget += float(prices.get(item, BASE_PRICES[item])) * quantity
                except (TypeError, ValueError):
                    budget += float(BASE_PRICES[item]) * quantity
                item_balance[item] = item_balance.get(item, 0) + quantity
            elif operation == "BUY_ANIMAL" and item in _BUDGET_ANIMAL_COST:
                budget += _BUDGET_ANIMAL_COST[item] * quantity
                item_balance[item] = item_balance.get(item, 0) + quantity

    for day, quantity in hires_by_day.items():
        first = current_hires if day == 0 else 0
        for offset in range(quantity):
            budget += _budget_fibonacci(first + offset)
    return budget, {**seed_need, **item_need}


def _budget_in_hands(observation: dict, item: str) -> int:
    inventories = ((observation.get("private") or {}).get(
        "inventories") or [])
    total = 0
    for inventory in inventories:
        if not isinstance(inventory, dict):
            continue
        try:
            total += max(0, int(inventory.get(item, 0)))
        except (TypeError, ValueError):
            continue
    return total


def _budget_existing_sells(action: dict) -> dict[str, int]:
    totals: dict[str, int] = {}
    for raw in action.get("market") or []:
        if (not isinstance(raw, (list, tuple)) or len(raw) < 3
                or str(raw[0]).upper() != "SELL"):
            continue
        item = str(raw[1]).upper()
        try:
            totals[item] = totals.get(item, 0) + max(0, int(raw[2]))
        except (TypeError, ValueError):
            continue
    return totals


def _budget_add_sell(action: dict, item: str, quantity: int,
                     max_orders: int) -> bool:
    quantity = max(0, int(quantity))
    if quantity <= 0:
        return False
    market = action.setdefault("market", [])
    for raw in market:
        if (isinstance(raw, list) and len(raw) >= 3
                and str(raw[0]).upper() == "SELL"
                and str(raw[1]).upper() == item):
            try:
                raw[2] = max(0, int(raw[2])) + quantity
            except (TypeError, ValueError):
                return False
            return True
    if len(market) >= max(1, int(max_orders)):
        return False
    market.append(["SELL", item, quantity])
    return True


def budget_guard(observation: dict, action: dict,
                 configuration=None, tape=None) -> dict:
    """Fund the next tape block only when its planned purchases are short.

    This is a research-only overlay.  It is deliberately inert when there is
    no tape, outside a block boundary, when cash is sufficient, or when the
    required input/inventory data is malformed.  Added sales are selected by
    current quote and never consume stock reserved for the tape's near-term
    unit actions.
    """
    if int(observation.get("step", 0)) == 0:
        BUDGET_GUARD_TELEMETRY.update(
            calls=0, changed_turns=0, added_units=0, abstains=0, events=[])
    BUDGET_GUARD_TELEMETRY["calls"] += 1
    result = _normalise_action(action)
    unchanged = action if isinstance(action, dict) else result
    actions = _actions(tape)
    if not actions:
        BUDGET_GUARD_TELEMETRY["abstains"] += 1
        return unchanged

    try:
        step = int(observation.get("step", 0))
        block = max(1, int((configuration or {}).get(
            "budget_guard_block_turns", 72)))
        first_step = max(0, int((configuration or {}).get(
            "budget_guard_first_step", 0)))
        max_orders = max(1, int((configuration or {}).get(
            "budget_guard_max_orders", 10)))
        turns_per_day = max(1, int((configuration or {}).get(
            "budget_guard_turns_per_day", 24)))
        min_price = max(0, int((configuration or {}).get(
            "budget_guard_min_sell_price", 2)))
        reserve_blocks = max(1, int((configuration or {}).get(
            "budget_guard_reserve_blocks", 1)))
        move_sells_first = bool((configuration or {}).get(
            "budget_guard_move_sells_first", True))
        configured_items = (configuration or {}).get(
            "budget_guard_sale_items")
        if configured_items is None:
            sale_items = _BUDGET_PRODUCTS
        elif isinstance(configured_items, str):
            sale_items = tuple(
                item.strip().upper() for item in configured_items.split(",")
                if item.strip().upper() in _BUDGET_PRODUCTS)
        else:
            sale_items = tuple(
                str(item).upper() for item in configured_items
                if str(item).upper() in _BUDGET_PRODUCTS)
    except (AttributeError, TypeError, ValueError):
        BUDGET_GUARD_TELEMETRY["abstains"] += 1
        return unchanged

    if (step < first_step or step % block != 0
            or step >= min(718, len(actions))):
        BUDGET_GUARD_TELEMETRY["abstains"] += 1
        return unchanged
    farms = observation.get("farms") or []
    player = int(observation.get("player", 0))
    if not 0 <= player < len(farms):
        BUDGET_GUARD_TELEMETRY["abstains"] += 1
        return unchanged

    try:
        farm = farms[player]
        money = float(farm.get("money", 0))
        shed = ((observation.get("private") or {}).get("shed") or {})
        prices = ((observation.get("market") or {}).get("prices") or {})
        budget, item_need = _budget_block_requirements(
            actions, observation, step, step + block, turns_per_day)
        if reserve_blocks > 1:
            _, protected_need = _budget_block_requirements(
                actions, observation, step, step + block * reserve_blocks,
                turns_per_day)
            item_need = protected_need
        existing = _budget_existing_sells(result)
        cash = money
        block_end = min(len(actions), step + block)
        for item in _BUDGET_PRODUCTS:
            planned = max(
                existing.get(item, 0),
                _budget_future_sell_total(actions, item, step, block_end),
            )
            available = max(0, int(shed.get(item, 0)))
            quote = float(prices.get(item, BASE_PRICES[item]))
            cash += min(available, planned) * quote
        cash_before_sales = cash
        shortfall = budget - cash
    except (AttributeError, KeyError, TypeError, ValueError, IndexError):
        BUDGET_GUARD_TELEMETRY["abstains"] += 1
        return unchanged

    if shortfall <= 0:
        BUDGET_GUARD_TELEMETRY["abstains"] += 1
        return unchanged

    candidates: list[tuple[float, str, int, float]] = []
    for item in sale_items:
        try:
            quote = float(prices.get(item, BASE_PRICES[item]))
            stock = max(0, int(shed.get(item, 0)))
        except (KeyError, TypeError, ValueError):
            continue
        if quote < min_price:
            continue
        protected = max(0, int(item_need.get(item, 0))
                        - _budget_in_hands(observation, item))
        available = stock - protected - existing.get(item, 0)
        if available > 0:
            candidates.append((-quote, item, available, quote))
    candidates.sort(key=lambda row: (row[0], row[1]))

    added_units = 0
    added_items: list[str] = []
    for _, item, available, quote in candidates:
        if shortfall <= 0:
            break
        quantity = min(available, max(1, int(math.ceil(shortfall / quote))))
        if not _budget_add_sell(result, item, quantity, max_orders):
            continue
        shortfall -= quantity * quote
        added_units += quantity
        added_items.append(item)

    if added_units <= 0:
        BUDGET_GUARD_TELEMETRY["abstains"] += 1
        return unchanged

    if move_sells_first:
        sells = [raw for raw in result["market"]
                 if isinstance(raw, list) and raw
                 and str(raw[0]).upper() == "SELL"]
        others = [raw for raw in result["market"]
                  if not (isinstance(raw, list) and raw
                          and str(raw[0]).upper() == "SELL")]
        result["market"] = sells + others
    BUDGET_GUARD_TELEMETRY["changed_turns"] += 1
    BUDGET_GUARD_TELEMETRY["added_units"] += added_units
    events = BUDGET_GUARD_TELEMETRY.setdefault("events", [])
    events.append({
        "step": step,
        "budget": float(budget),
        "cash_before": float(cash_before_sales),
        "shortfall_after": float(shortfall),
        "items": tuple(added_items),
        "added_units": int(added_units),
    })
    del events[:-256]
    return result


def _room_tile_at(farm: dict, position: Any) -> Any:
    if not isinstance(position, (list, tuple)) or len(position) < 2:
        return None
    try:
        x, y = int(position[0]), int(position[1])
        rows = farm.get("tiles") or []
        return rows[y][x]
    except (AttributeError, IndexError, TypeError, ValueError):
        return None


def _room_unit_flow(observation: dict, action: dict) -> tuple[int, int]:
    """Return (newly produced, consumed/carried-away) units this turn."""
    player = int(observation.get("player", 0))
    farms = observation.get("farms") or []
    if not 0 <= player < len(farms):
        return 0, 0
    farm = farms[player]
    commands = [action.get("farmer") or ["PASS"]]
    commands.extend(action.get("hands") or [])
    positions = [farm.get("farmer")]
    positions.extend(farm.get("hands") or [])
    produced = 0
    consumed = 0
    for index, command in enumerate(commands):
        if not isinstance(command, (list, tuple)) or not command:
            continue
        operation = str(command[0]).upper()
        tile = _room_tile_at(
            farm, positions[index] if index < len(positions) else None)
        if operation == "HARVEST" and isinstance(tile, dict):
            try:
                produced += max(0, int(tile.get("yield_units", 0)))
            except (TypeError, ValueError):
                pass
        elif (operation == "COLLECT_FERTILIZER"
              and isinstance(tile, dict)
              and tile.get("fertilizer_available")):
            produced += 1
        elif operation in {"FEED", "FERTILIZE"}:
            consumed += 1
        elif operation == "PLACE":
            try:
                consumed += max(1, int(command[2])) if len(command) >= 3 else 1
            except (TypeError, ValueError):
                consumed += 1
    return produced, consumed


def room_guard(observation: dict, action: dict,
               configuration=None, tape=None) -> dict:
    """Recover inventory that would overflow the shed at a day boundary.

    The guard is intentionally narrower than a general liquidation policy:
    it runs only on the final turn of a day, estimates only observable unit
    flow, and protects the next tape block's required inputs before choosing
    extra SELLs.  It never changes the order of existing market commands.
    """
    if int(observation.get("step", 0)) == 0:
        ROOM_GUARD_TELEMETRY.update(
            calls=0, changed_turns=0, added_units=0, abstains=0, events=[])
    ROOM_GUARD_TELEMETRY["calls"] += 1
    result = _normalise_action(action)
    unchanged = action if isinstance(action, dict) else result
    actions = _actions(tape)
    if not actions:
        ROOM_GUARD_TELEMETRY["abstains"] += 1
        return unchanged
    try:
        step = int(observation.get("step", 0))
        cfg = configuration or {}
        turns_per_day = max(1, int(cfg.get("room_guard_turns_per_day", 24)))
        capacity = max(1, int(cfg.get("room_guard_capacity", 100)))
        target = max(0, min(capacity, int(cfg.get(
            "room_guard_target_capacity", capacity - 1))))
        min_price = max(0, float(cfg.get("room_guard_min_sell_price", 1)))
        protect_blocks = max(1, int(cfg.get(
            "room_guard_protect_blocks", 1)))
        max_orders = max(1, int(cfg.get("room_guard_max_orders", 10)))
    except (AttributeError, TypeError, ValueError):
        ROOM_GUARD_TELEMETRY["abstains"] += 1
        return unchanged
    if (step % turns_per_day != turns_per_day - 1
            or step >= min(718, len(actions))):
        ROOM_GUARD_TELEMETRY["abstains"] += 1
        return unchanged

    try:
        private = observation.get("private") or {}
        shed = private.get("shed") or {}
        inventories = private.get("inventories") or []
        shed_total = sum(max(0, int(value)) for value in shed.values())
        carried = sum(
            max(0, int(value))
            for inventory in inventories if isinstance(inventory, dict)
            for value in inventory.values()
        )
        produced, consumed = _room_unit_flow(observation, result)
        current_sells = _budget_existing_sells(result)
        planned_buys = 0
        for raw in result.get("market") or []:
            if (isinstance(raw, (list, tuple)) and len(raw) >= 3
                    and str(raw[0]).upper() in {"BUY_PRODUCT", "BUY_ANIMAL"}):
                planned_buys += max(0, int(raw[2]))
        fillable = sum(
            min(max(0, int(shed.get(item, 0))), quantity)
            for item, quantity in current_sells.items()
        )
        overflow = (shed_total + carried + produced - consumed
                    + planned_buys - fillable - target)
        if overflow <= 0:
            ROOM_GUARD_TELEMETRY["abstains"] += 1
            return unchanged

        player = int(observation.get("player", 0))
        farms = observation.get("farms") or []
        farm = farms[player] if 0 <= player < len(farms) else {}
        prices = ((observation.get("market") or {}).get("prices") or {})
        _, future_need = _budget_block_requirements(
            actions, observation, step + 1,
            step + 1 + 72 * protect_blocks, 24)
        future = tuple(actions[step + 1:min(len(actions), step + 1 + 72)])
        candidates = []
        for item in _BUDGET_PRODUCTS:
            quote = float(prices.get(item, BASE_PRICES[item]))
            stock = max(0, int(shed.get(item, 0)))
            protected = max(0, int(future_need.get(item, 0))
                            - _budget_in_hands(observation, item))
            available = stock - protected - current_sells.get(item, 0)
            if available <= 0 or quote < min_price:
                continue
            future_sales = _budget_future_sell_total(
                actions, item, step + 1, step + 1 + 72)
            candidates.append((future_sales > 0, -quote, item, available))
        # Prefer stock with no immediate tape sale, then the highest quote.
        candidates.sort(key=lambda row: (row[0], row[1], row[2]))
        added_units = 0
        added_items = []
        remaining = overflow
        for _, _, item, available in candidates:
            if remaining <= 0:
                break
            quantity = min(available, remaining)
            if not _budget_add_sell(result, item, quantity, max_orders):
                continue
            remaining -= quantity
            added_units += quantity
            added_items.append(item)
    except (AttributeError, KeyError, TypeError, ValueError, IndexError):
        ROOM_GUARD_TELEMETRY["abstains"] += 1
        return unchanged

    if added_units <= 0:
        ROOM_GUARD_TELEMETRY["abstains"] += 1
        return unchanged
    ROOM_GUARD_TELEMETRY["changed_turns"] += 1
    ROOM_GUARD_TELEMETRY["added_units"] += added_units
    events = ROOM_GUARD_TELEMETRY.setdefault("events", [])
    events.append({
        "step": step,
        "overflow": int(overflow),
        "remaining": int(max(0, remaining)),
        "items": tuple(added_items),
        "added_units": int(added_units),
    })
    del events[:-256]
    return result


def _supply_quantity(raw: Any) -> int:
    if not isinstance(raw, (list, tuple)) or len(raw) < 3:
        return 0
    try:
        return max(0, int(raw[2]))
    except (TypeError, ValueError):
        return 0


def _supply_pickup_need(frames: tuple[dict, ...], start: int,
                        horizon: int) -> int:
    """Count near-future WHEAT pickups in a short tape window."""
    need = 0
    begin = max(0, int(start))
    end = min(len(frames), begin + max(1, int(horizon)))
    for frame in frames[begin:end]:
        commands = [frame.get("farmer") or ["PASS"]]
        commands.extend(frame.get("hands") or [])
        for command in commands:
            if (isinstance(command, (list, tuple)) and len(command) >= 2
                    and str(command[0]).upper() == "PICKUP"
                    and str(command[1]).upper() == "WHEAT"):
                need += _supply_quantity(command) or 1
    return need


def _supply_project(action: dict, shed: dict, inventories: list,
                    capacity: int = 100, include_hands: bool = False):
    """Project only the WHEAT shed stock and current market queue."""
    stock = max(0, int(shed.get("WHEAT", 0)))
    buys: dict[int, int] = {}
    sales: dict[int, int] = {}
    total = sum(max(0, int(value)) for value in shed.values())
    for index, raw in enumerate(action.get("market") or []):
        if not isinstance(raw, (list, tuple)) or len(raw) < 3:
            continue
        operation = str(raw[0]).upper()
        item = str(raw[1]).upper()
        quantity = _supply_quantity(raw)
        if item != "WHEAT" or quantity <= 0:
            continue
        if operation == "SELL":
            actual = min(quantity, stock)
            stock -= actual
            total = max(0, total - actual)
            sales[index] = actual
        elif operation == "BUY_PRODUCT":
            actual = min(quantity, max(0, int(capacity) - total))
            stock += actual
            total += actual
            buys[index] = actual
    if include_hands:
        for inventory in inventories:
            if not isinstance(inventory, dict):
                continue
            carried = max(0, int(inventory.get("WHEAT", 0)))
            actual = min(carried, max(0, int(capacity) - total))
            stock += actual
            total += actual
    return stock, total, buys, sales


def _supply_budget_ok(observation: dict, orders: list[list]) -> bool:
    farms = observation.get("farms") or []
    player = int(observation.get("player", 0))
    if not 0 <= player < len(farms):
        return False
    try:
        money = float(farms[player].get("money", 0))
        prices = ((observation.get("market") or {}).get("prices") or {})
        cost = 0.0
        for raw in orders:
            if (isinstance(raw, (list, tuple)) and len(raw) >= 3
                    and str(raw[0]).upper() == "BUY_PRODUCT"):
                item = str(raw[1]).upper()
                if item in {"WHEAT", "FERTILIZER"}:
                    cost += _supply_quantity(raw) * float(
                        prices.get(item, BASE_PRICES[item]))
        return cost <= money + 1e-9
    except (AttributeError, KeyError, TypeError, ValueError):
        return False


def supply_prefetch(observation: dict, action: dict,
                    configuration=None, tape=None) -> dict:
    """Protect the next tape WHEAT pickup with a funded current order.

    This is the portable form of Thomas EXP231/R97.  It does not generate a
    buy unless the next few tape frames explicitly require a WHEAT pickup.  A
    current WHEAT SELL is reduced first; otherwise an existing WHEAT buy is
    enlarged or a new order is appended when a queue slot and shed capacity
    remain.  The cash check intentionally ignores same-turn sale proceeds.
    """
    if int(observation.get("step", 0)) == 0:
        SUPPLY_PREFETCH_TELEMETRY.update(
            calls=0, changed_turns=0, protected_units=0, abstains=0,
            events=[])
    SUPPLY_PREFETCH_TELEMETRY["calls"] += 1
    actions = _actions(tape)
    unchanged = action
    if not actions:
        SUPPLY_PREFETCH_TELEMETRY["abstains"] += 1
        return unchanged
    try:
        cfg = configuration or {}
        step = int(observation.get("step", 0))
        first_step = max(0, int(cfg.get("supply_prefetch_first_step", 144)))
        last_step = min(695, len(actions) - 1)
        horizon = max(1, int(cfg.get("supply_prefetch_horizon", 2)))
        capacity = max(1, int(cfg.get("supply_prefetch_capacity", 100)))
        max_orders = max(1, int(cfg.get("supply_prefetch_max_orders", 10)))
    except (AttributeError, TypeError, ValueError):
        SUPPLY_PREFETCH_TELEMETRY["abstains"] += 1
        return unchanged
    if step < first_step or step >= last_step:
        SUPPLY_PREFETCH_TELEMETRY["abstains"] += 1
        return unchanged

    need = _supply_pickup_need(actions, step + 1, horizon)
    # Thomas's special pre-fund condition covers a full next-turn queue where
    # a later turn needs grain but the immediate frame itself has no pickup.
    if not need:
        next_orders = actions[step + 1].get("market") or []
        no_wheat_order = not any(
            isinstance(raw, (list, tuple)) and len(raw) >= 2
            and str(raw[1]).upper() == "WHEAT"
            and str(raw[0]).upper() in {"BUY_PRODUCT", "SELL"}
            for raw in next_orders)
        if len(next_orders) == max_orders and no_wheat_order:
            need = _supply_pickup_need(actions, step + 1, horizon + 1)
    if need <= 0:
        SUPPLY_PREFETCH_TELEMETRY["abstains"] += 1
        return unchanged

    try:
        private = observation.get("private") or {}
        shed = private.get("shed") or {}
        inventories = private.get("inventories") or []
        current = _normalise_action(action)
        stock, total, buys, sales = _supply_project(
            current, shed, inventories, capacity, include_hands=False)
        # A current tape pickup consumes from the same projected shed before
        # the next frame is reached.
        current_pickup = _supply_pickup_need((current,), 0, 1)
        shortage = max(0, need - max(0, stock - current_pickup))
        if shortage <= 0:
            SUPPLY_PREFETCH_TELEMETRY["abstains"] += 1
            return unchanged

        proposed = copy.deepcopy(current)
        # Reduce a current WHEAT sell from the end, matching R97's safe
        # direction while preserving all non-WHEAT queue slots.
        remaining = shortage
        for index in range(len(proposed["market"]) - 1, -1, -1):
            raw = proposed["market"][index]
            if (isinstance(raw, list) and len(raw) >= 3
                    and str(raw[0]).upper() == "SELL"
                    and str(raw[1]).upper() == "WHEAT"):
                reducible = min(_supply_quantity(raw), remaining)
                raw[2] = max(0, _supply_quantity(raw) - reducible)
                remaining -= reducible
                if remaining <= 0:
                    break
        proposed["market"] = [
            raw for raw in proposed["market"]
            if not (isinstance(raw, list) and len(raw) >= 3
                    and str(raw[0]).upper() == "SELL"
                    and str(raw[1]).upper() == "WHEAT"
                    and _supply_quantity(raw) <= 0)
        ]
        if remaining > 0:
            for raw in proposed["market"]:
                if (isinstance(raw, list) and len(raw) >= 3
                        and str(raw[0]).upper() == "BUY_PRODUCT"
                        and str(raw[1]).upper() == "WHEAT"):
                    raw[2] = _supply_quantity(raw) + remaining
                    remaining = 0
                    break
        if remaining > 0:
            if len(proposed["market"]) >= max_orders:
                SUPPLY_PREFETCH_TELEMETRY["abstains"] += 1
                return unchanged
            proposed["market"].append(["BUY_PRODUCT", "WHEAT", remaining])
        if not _supply_budget_ok(observation, proposed["market"]):
            SUPPLY_PREFETCH_TELEMETRY["abstains"] += 1
            return unchanged
        projected_stock, projected_total, _, _ = _supply_project(
            proposed, shed, inventories, capacity, include_hands=False)
        if projected_stock < need or projected_total > capacity:
            SUPPLY_PREFETCH_TELEMETRY["abstains"] += 1
            return unchanged
    except (AttributeError, KeyError, TypeError, ValueError, IndexError):
        SUPPLY_PREFETCH_TELEMETRY["abstains"] += 1
        return unchanged

    SUPPLY_PREFETCH_TELEMETRY["changed_turns"] += 1
    SUPPLY_PREFETCH_TELEMETRY["protected_units"] += shortage
    events = SUPPLY_PREFETCH_TELEMETRY.setdefault("events", [])
    events.append({"step": step, "need": need, "added": shortage})
    del events[:-256]
    return proposed


def _sell_impact_demand(observation: dict, item: str,
                        configuration: dict) -> float:
    shops = list((observation.get("town") or {}).get(
        "unlocked_shops") or [])
    products = _SALE_ADVANCE_SHOP_PRODUCTS
    turns_per_day = max(1, int(configuration.get(
        "sell_impact_turns_per_day", 24)))
    shop_interval = max(1, int(configuration.get(
        "sell_impact_shop_interval", 4)))
    demand = 0.0
    for shop in shops:
        offered = products.get(shop, set())
        if item in offered:
            demand += (turns_per_day / shop_interval) * (
                2 if len(offered) == 1 else 1)
    center_interval = max(1, int(configuration.get(
        "sell_impact_center_interval", 24)))
    if item != "FERTILIZER":
        demand += turns_per_day / center_interval
    return max(0.25, demand)


def _sell_impact_score(observation: dict, order: list,
                       configuration: dict) -> float:
    if (not isinstance(order, (list, tuple)) or len(order) < 3
            or str(order[0]).upper() != "SELL"):
        return float("-inf")
    item = str(order[1]).upper()
    if item not in _FRONTLOAD_MARKET_PARAMS:
        return float("-inf")
    try:
        quantity = max(0, int(order[2]))
        market = observation.get("market") or {}
        inventory = market.get("inventory") or {}
        prices = market.get("prices") or {}
        current_inventory = int(inventory.get(item, 10000))
        current_quote = float(prices.get(
            item, _frontload_price(item, current_inventory)))
        later_quote = float(_frontload_price(
            item, current_inventory + quantity))
        score = quantity * max(0.0, current_quote - later_quote)
        alpha = float(configuration.get("sell_impact_demand_alpha", 0.25))
        if alpha > 0.0 and score > 0.0:
            excess = max(0.0, current_inventory + quantity - 10000)
            urgency = min(1.0, excess / (
                _sell_impact_demand(observation, item, configuration) * 10.0))
            score *= 1.0 + alpha * urgency
        return score
    except (AttributeError, KeyError, TypeError, ValueError):
        return float("-inf")


def sell_impact_reorder(observation: dict, action: dict,
                        configuration=None, tape=None) -> dict:
    """Rank existing SELL slots by their market-impact loss.

    This is the portable part of Kaito v27's order-ranking layer.  It never
    creates or deletes an order and keeps every non-SELL row at its original
    queue index, so it cannot change a BUY/SELL dependency by moving a BUY.
    The operator is therefore useful as an isolated ablation of queue order.
    """
    if int(observation.get("step", 0)) == 0:
        SELL_IMPACT_TELEMETRY.update(
            calls=0, changed_turns=0, reordered_sales=0, abstains=0,
            events=[])
    SELL_IMPACT_TELEMETRY["calls"] += 1
    cfg = dict(configuration) if isinstance(configuration, dict) else {}
    step = int(observation.get("step", 0))
    try:
        first_step = max(0, int(cfg.get("sell_impact_first_step", 0)))
        last_step = min(718, int(cfg.get("sell_impact_last_step", 718)))
    except (TypeError, ValueError):
        SELL_IMPACT_TELEMETRY["abstains"] += 1
        return action if isinstance(action, dict) else _normalise_action(action)
    if step < first_step or step > last_step:
        SELL_IMPACT_TELEMETRY["abstains"] += 1
        return action if isinstance(action, dict) else _normalise_action(action)
    result = _normalise_action(action)
    orders = result.get("market") or []
    configured_items = cfg.get("sell_impact_items")
    if configured_items is None:
        eligible_items = set(_FRONTLOAD_MARKET_PARAMS)
    elif isinstance(configured_items, str):
        eligible_items = {item.strip().upper() for item in
                          configured_items.split(",") if item.strip()}
    else:
        eligible_items = {str(item).upper() for item in configured_items}
    positions = [index for index, raw in enumerate(orders)
                 if isinstance(raw, (list, tuple)) and len(raw) >= 3
                 and str(raw[0]).upper() == "SELL"
                 and str(raw[1]).upper() in eligible_items]
    if len(positions) < 2:
        SELL_IMPACT_TELEMETRY["abstains"] += 1
        return action if isinstance(action, dict) else result
    ranked = sorted(
        (list(orders[index]) for index in positions),
        key=lambda raw: (-_sell_impact_score(observation, raw, cfg),
                         str(raw[1]), -_supply_quantity(raw)),
    )
    reordered = list(orders)
    for index, raw in zip(positions, ranked):
        reordered[index] = raw
    if reordered == orders:
        SELL_IMPACT_TELEMETRY["abstains"] += 1
        return action if isinstance(action, dict) else result
    result["market"] = reordered
    SELL_IMPACT_TELEMETRY["changed_turns"] += 1
    SELL_IMPACT_TELEMETRY["reordered_sales"] += len(positions)
    events = SELL_IMPACT_TELEMETRY.setdefault("events", [])
    events.append({
        "step": int(observation.get("step", 0)),
        "before": [tuple(orders[index][:2]) for index in positions],
        "after": [tuple(raw[:2]) for raw in ranked],
    })
    del events[:-256]
    return result


def sale_advance_pressure(observation: dict, action: dict,
                          configuration=None, tape=None) -> dict:
    """Add lower-value sale arms only after observing rival supply pressure.

    ``sale_advance`` is intentionally conservative in its default premium
    configuration.  This wrapper keeps that configuration while estimating
    rival supply from consecutive public market inventories:

        observed inventory increase + town demand - our previous SELL

    The estimate is accumulated with decay, so a single noisy transition does
    not permanently change the policy.  Once pressure reaches the configured
    trigger, all sale-advance items become eligible for the current decision.
    The tape, worker actions, and future orders are otherwise handled by the
    existing operator.  This is an experimental arm; it does not affect the
    ordinary ``sale_advance`` path.
    """
    step = int(observation.get("step", 0))
    player = int(observation.get("player", 0))
    route_id = str(getattr(tape, "route_id", "tape"))
    if step == 0:
        # A new episode may reuse a route id.  Do not retain pressure from a
        # previous official-engine match.
        PRESSURE_SALE_STATE.clear()

    key = (player, route_id)
    state = PRESSURE_SALE_STATE.get(key)
    if state is None or step <= int(state.get("step", -1)):
        state = {
            "step": -1,
            "last_inventory": {},
            "last_shops": (),
            "last_sold": {},
            "pressure": {},
        }
        PRESSURE_SALE_STATE[key] = state

    cfg = dict(configuration) if isinstance(configuration, dict) else {}
    try:
        decay = min(0.99, max(0.0, float(
            cfg.get("sale_advance_pressure_decay", 0.72))))
        trigger = max(0.0, float(
            cfg.get("sale_advance_pressure_trigger", 2.0)))
        expand_all = bool(cfg.get(
            "sale_advance_pressure_expand_all", True))
        targeted = bool(cfg.get(
            "sale_advance_pressure_targeted", False))
    except (TypeError, ValueError):
        decay, trigger, expand_all, targeted = 0.72, 2.0, True, False

    market_data = observation.get("market") or {}
    inventory = market_data.get("inventory") or {}
    items = tuple(SALE_ADVANCE_ITEMS)
    if int(state.get("step", -1)) == step - 1:
        previous_inventory = state.get("last_inventory") or {}
        previous_shops = state.get("last_shops") or ()
        previous_sold = state.get("last_sold") or {}
        pressure = state.setdefault("pressure", {})
        for item in items:
            try:
                delta = (int(inventory.get(item, 10000))
                         - int(previous_inventory.get(item, 10000)))
                demand = _adaptive_demand(
                    {"town": {"unlocked_shops": previous_shops}},
                    item, step - 1)
                rival_supply = max(
                    0, delta + demand - int(previous_sold.get(item, 0)))
            except (TypeError, ValueError):
                rival_supply = 0
            pressure[item] = (decay * float(pressure.get(item, 0.0))
                              + float(rival_supply))
        state["pressure"] = pressure

    state["last_inventory"] = {
        str(item).upper(): int(value)
        for item, value in inventory.items()
    }
    state["last_shops"] = tuple(
        (observation.get("town") or {}).get("unlocked_shops") or ())

    # Evaluate the incumbent action after updating the signal.  The recorded
    # SELLs represent the supply this turn and are subtracted on the next
    # observation's inventory transition.
    pressure = state.get("pressure") or {}
    pressured_items = tuple(
        item for item in SALE_ADVANCE_ITEMS
        if float(pressure.get(item, 0.0)) >= trigger)
    if pressured_items and expand_all:
        cfg["sale_advance_items"] = ",".join(SALE_ADVANCE_ITEMS)
    elif pressured_items and targeted:
        configured = cfg.get(
            "sale_advance_items", "STRAWBERRY,MELON,MILK,WOOL")
        if isinstance(configured, str):
            configured = configured.split(",")
        premium = tuple(
            str(item).upper() for item in configured
            if str(item).upper() in SALE_ADVANCE_ITEMS)
        cfg["sale_advance_items"] = ",".join(
            dict.fromkeys((*premium, *pressured_items)))
    elif "sale_advance_items" not in cfg:
        cfg["sale_advance_items"] = "STRAWBERRY,MELON,MILK,WOOL"

    result = sale_advance(observation, action, cfg, tape)
    state["last_sold"] = _opfr_sell_totals(result)
    state["step"] = step
    return result
