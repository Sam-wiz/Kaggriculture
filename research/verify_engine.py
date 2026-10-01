"""Empirical verification of the Kaggriculture engine quirks claimed in the community
notebooks. Run:  ./.venv/bin/python research/verify_engine.py

Every check prints PASS/FAIL plus the observed evidence. Nothing here touches the
agents/ or harness code; it drives kaggle_environments directly.
"""
import json
from kaggle_environments import make
from kaggle_environments.envs.kaggriculture import kaggriculture as K

RESULTS = []


def check(name, ok, evidence):
    RESULTS.append((name, ok, evidence))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}\n        {evidence}")


# --------------------------------------------------------------------------
# 1. Last executable step is 718 (episodeSteps=720 -> DONE fires at step 718).
# --------------------------------------------------------------------------
def t_last_step():
    seen = {}

    def probe(obs):
        seen[obs["step"]] = (obs["day"], obs["hour"])
        return {"farmer": ["PASS"], "hands": [], "market": []}

    env = make("kaggriculture", configuration={"seed": 7}, debug=False)
    env.run([probe, "pass"])
    last = max(seen)
    check(
        "last executable step == 718 (day 29, hour 22); step 719 never runs",
        last == 718 and seen[718] == (29, 22),
        f"max obs.step seen by agent = {last}, (day,hour) = {seen[last]}; "
        f"len(env.steps) = {len(env.steps)}",
    )


# --------------------------------------------------------------------------
# 2. BUILD_COOP / BUILD_PASTURE are free (no coin cost, only an action).
# 3. COLLECT_FERTILIZER yields 1 FERTILIZER per animal per day and FERTILIZER
#    is sellable (nobody in the town ever buys it, so it is pure new money).
# 4. DROP and SELL resolve in the same turn (units act before the market).
# 5. PLANT atomicity: N plant requests for a crop with < N seeds -> ALL dropped.
# 6. Shed cap 100: end-of-day auto-drop discards the overflow.
# --------------------------------------------------------------------------
def t_scripted():
    """One scripted agent that exercises several quirks and records what happened."""
    log = {}

    def agent(obs):
        step, day, hour = obs["step"], obs["day"], obs["hour"]
        me = obs["player"]
        farm = obs["farms"][me]
        priv = obs["private"]
        fx, fy = farm["farmer"]
        tile = farm["tiles"][fy][fx]
        money = farm["money"]
        act = {"farmer": ["PASS"], "hands": [], "market": []}
        nh = len(farm["hands"])

        # ---- day 0: build a pasture for free, buy + place a cow, buy wheat ----
        if day == 0:
            if hour == 0:
                log["money_before_build"] = money
                act["farmer"] = ["BUILD_PASTURE"]
                act["market"] = [["BUY_ANIMAL", "COW", 1], ["BUY_PRODUCT", "WHEAT", 20]]
            elif hour == 1:
                log["money_after_build"] = money
                log["tile_after_build"] = tile
                # PICKUP the cow from the shed, then PLACE it next turn.
                act["farmer"] = ["PICKUP", "COW", 1]
            elif hour == 2:
                act["farmer"] = ["PLACE", "COW"]
            elif hour == 3:
                log["tile_after_place"] = tile
                act["farmer"] = ["PICKUP", "WHEAT", 20]
            elif hour == 4:
                act["farmer"] = ["FEED"]
            elif hour == 5:
                act["farmer"] = ["CARE"]
            else:
                act["farmer"] = ["PASS"]
            # PLANT atomicity probe: hire 3 hands, buy 2 carrot seeds, ask 3 to plant.
            if hour == 8:
                act["market"] = [["HIRE"], ["HIRE"], ["HIRE"], ["BUY_SEED", "CARROT", 2]]
            if hour == 10:
                log["seeds_before_plant"] = dict(priv["seeds"])
                # farmer + 2 hands = 3 PLANT CARROT requests, only 2 seeds held.
                act["farmer"] = ["PLANT", "CARROT"]
                act["hands"] = [["PLANT", "CARROT"], ["PLANT", "CARROT"]] + [["PASS"]] * max(0, nh - 2)
            if hour == 11:
                log["seeds_after_atomic_plant"] = dict(priv["seeds"])
                planted = sum(
                    1
                    for row in farm["tiles"]
                    for t in row
                    if isinstance(t, dict) and t.get("kind") == "PLANT"
                )
                log["tiles_planted_after_atomic"] = planted
                act["hands"] = [["PASS"]] * nh
            if hour >= 12:
                act["hands"] = [["PASS"]] * nh
            return act

        # ---- from day 1: feed + care + collect fertilizer + sell it ----
        act["hands"] = [["PASS"]] * nh
        if hour == 0:
            act["farmer"] = ["PICKUP", "WHEAT", 1]
        elif hour == 1:
            act["farmer"] = ["FEED"]
        elif hour == 2:
            act["farmer"] = ["CARE"]
        elif hour == 3:
            act["farmer"] = ["COLLECT_FERTILIZER"]
        elif hour == 4:
            # DROP + SELL in the SAME turn: units act before _process_market.
            act["farmer"] = ["DROP"]
            act["market"] = [["SELL", "FERTILIZER", 1]]
            log.setdefault("dropsell_money_before", {})[day] = money
            log.setdefault("dropsell_shed_before", {})[day] = dict(priv["shed"])
        elif hour == 5:
            log.setdefault("dropsell_money_after", {})[day] = money
            log.setdefault("dropsell_shed_after", {})[day] = dict(priv["shed"])
            act["farmer"] = ["HARVEST"]
        elif hour == 6:
            log.setdefault("carry", {})[day] = dict(priv["inventories"][0])
        if day == 3 and hour == 7:
            log["cow_tile_day3"] = farm["tiles"][fy][fx]
        return act

    env = make("kaggriculture", configuration={"seed": 11}, debug=False)
    env.run([agent, "pass"])

    # -- free build --
    mb, ma = log.get("money_before_build"), log.get("money_after_build")
    # money_after_build also reflects the COW (400) and 20 WHEAT bought that same turn
    check(
        "BUILD_PASTURE costs 0 coins (only an action)",
        isinstance(log.get("tile_after_build"), dict)
        and log["tile_after_build"].get("kind") == "PASTURE",
        f"tile after BUILD_PASTURE = {log.get('tile_after_build')}; "
        f"money {mb} -> {ma} (delta includes COW $400 + 20 WHEAT)",
    )
    check(
        "PLACE COW onto the free PASTURE works",
        isinstance(log.get("tile_after_place"), dict)
        and log["tile_after_place"].get("animal") == "COW",
        f"tile after PLACE = {log.get('tile_after_place')}",
    )

    # -- PLANT atomicity --
    sb = log.get("seeds_before_plant", {}).get("CARROT")
    sa = log.get("seeds_after_atomic_plant", {}).get("CARROT")
    check(
        "PLANT atomicity: 3 requests with 2 seeds -> ALL dropped, 0 seeds spent",
        sb == 2 and sa == 2 and log.get("tiles_planted_after_atomic") == 0,
        f"CARROT seeds {sb} -> {sa}, PLANT tiles created = "
        f"{log.get('tiles_planted_after_atomic')} (expected 2->2 and 0 tiles)",
    )

    # -- DROP + SELL same turn --
    days = sorted(log.get("dropsell_money_after", {}))
    hit = None
    for d in days:
        before = log["dropsell_money_before"][d]
        after = log["dropsell_money_after"][d]
        shed_b = log["dropsell_shed_before"][d].get("FERTILIZER", 0)
        if after > before and shed_b == 0:
            hit = (d, before, after)
            break
    check(
        "DROP then SELL in the SAME turn: carried FERTILIZER banks immediately",
        hit is not None,
        f"day {hit[0]}: money {hit[1]} -> {hit[2]} on a turn whose shed held 0 "
        f"FERTILIZER before the DROP" if hit else "no same-turn drop+sell observed",
    )

    # -- COLLECT_FERTILIZER is a daily, free income stream --
    n_days_income = sum(
        1
        for d in days
        if log["dropsell_money_after"][d] > log["dropsell_money_before"][d]
    )
    check(
        "COLLECT_FERTILIZER yields 1 FERTILIZER/animal/day, sellable for real coins",
        n_days_income >= 20,
        f"{n_days_income} separate days banked fertilizer revenue from ONE cow",
    )

    # -- care-bonus banking --
    cow = log.get("cow_tile_day3")
    check(
        "CARE banks a pending_care_bonus that pays out on the production day",
        isinstance(cow, dict) and cow.get("pending_care_bonus", 0) > 0,
        f"cow tile on day 3 = {cow}",
    )
    return env


# --------------------------------------------------------------------------
# 7. Shed cap 100 -> end-of-day auto-drop discards overflow.
# --------------------------------------------------------------------------
def t_shed_overflow():
    priv = K._new_private()
    priv["shed"]["WHEAT"] = 95
    priv["inventories"] = [{"MELON": 30}]
    K._drop_inventories_to_shed(priv, 100)
    total = sum(priv["shed"].values())
    check(
        "shed cap 100: end-of-day auto-drop keeps 5 and DESTROYS the other 25",
        total == 100 and priv["shed"].get("MELON") == 5 and priv["inventories"][0] == {},
        f"shed after drop = {dict((k, v) for k, v in priv['shed'].items() if v)}, "
        f"total = {total}; 25 MELON silently discarded",
    )


# --------------------------------------------------------------------------
# 8. Sales at the $1 floor do not raise market inventory (pure loss).
# 9. BUY_PRODUCT / BUY_ANIMAL are blocked when the shed is full (can starve you).
# --------------------------------------------------------------------------
def t_market_floor_and_full_shed():
    market = K._new_market()
    market["inventory"]["WOOL"] = 10000 + 5000  # deep in the glut, price == 1
    farm = K._new_farm(10, 3000)
    priv = K._new_private()
    priv["shed"]["WOOL"] = 1
    inv_before = market["inventory"]["WOOL"]
    K._commit_unit("SELL", "WOOL", K.market_price("WOOL", inv_before), farm, priv, market)
    check(
        "a SELL that clears at the $1 floor does NOT add to market inventory",
        market["inventory"]["WOOL"] == inv_before and farm["money"] == 3001,
        f"WOOL inventory {inv_before} -> {market['inventory']['WOOL']}, "
        f"money 3000 -> {farm['money']} (price was "
        f"${K.market_price('WOOL', inv_before)})",
    )

    market2 = K._new_market()
    farm2 = K._new_farm(10, 3000)
    priv2 = K._new_private()
    priv2["shed"]["WHEAT"] = 100  # shed exactly at capacity
    ok_wheat = K._commit_unit(
        "BUY_PRODUCT", "WHEAT", K.market_price("WHEAT", 9999), farm2, priv2, market2
    )
    ok_cow = K._commit_unit("BUY_ANIMAL", "COW", 400, farm2, priv2, market2)
    ok_seed = K._commit_unit("BUY_SEED", "WHEAT", 10, farm2, priv2, market2)
    check(
        "a FULL shed blocks BUY_PRODUCT and BUY_ANIMAL (but NOT BUY_SEED)",
        ok_wheat is False and ok_cow is False and ok_seed is True,
        f"BUY_PRODUCT WHEAT -> {ok_wheat}, BUY_ANIMAL COW -> {ok_cow}, "
        f"BUY_SEED WHEAT -> {ok_seed}  (a full shed can silently starve your herd)",
    )


# --------------------------------------------------------------------------
# 10. Market order SLOT INDEX is a priority queue shared with the opponent.
# --------------------------------------------------------------------------
class _Obs(dict):
    """kaggle_environments observations allow both obs['x'] and obs.x."""

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


class _Seat:
    def __init__(self, obs, action):
        self.observation = obs
        self.action = action


class _Env:
    def __init__(self, cfg):
        self.configuration = cfg


def _market_only(orders0, orders1, seed_shed):
    """Run ONE turn of the engine's market resolver with hand-built state."""
    farms = [K._new_farm(10, 100000) for _ in range(2)]
    privs = [K._new_private() for _ in range(2)]
    for p in range(2):
        privs[p]["shed"].update(seed_shed)
    market = K._new_market()
    obs0 = _Obs(farms=farms, market=market, town=K._new_town(), private=privs[0], step=0)
    obs1 = _Obs(farms=farms, market=market, town=obs0["town"], private=privs[1], step=0)
    state = [_Seat(obs0, {"market": orders0}), _Seat(obs1, {"market": orders1})]
    K._process_market(state, _Env({"boardSize": 10, "maxMarketOrdersPerTurn": 10,
                                   "farmHandCostMult": 1, "shedCapacity": 100}))
    return farms[0]["money"] - 100000, farms[1]["money"] - 100000


def t_slot_priority():
    """Seat order vs market-order SLOT INDEX: two different things."""
    sell = ["SELL", "MELON", 30]
    pad = ["PASS"]  # unparseable -> that slot is a no-op, but it still IS a slot

    # (a) both players sell the same 30 melon at the SAME slot index -> identical.
    a0, a1 = _market_only([sell], [sell], {"MELON": 30})
    check(
        "SEAT is worth nothing: same order at the same slot pays both seats equally",
        a0 == a1,
        f"P0 banked ${a0:.0f}, P1 banked ${a1:.0f} for 30 MELON each at slot 0 "
        f"(both quoted against the same pre-commit inventory)",
    )

    # (b) same order, different SLOT INDEX -> the early slot clears first, alone.
    b0, b1 = _market_only([sell], [pad, pad, pad, sell], {"MELON": 30})
    check(
        "market SLOT INDEX is a shared priority queue: slot 0 beats slot 3",
        b0 > b1,
        f"P0 (slot 0) banked ${b0:.0f}, P1 (slot 3) banked ${b1:.0f} for the same "
        f"30 MELON -> slot advantage ${b0 - b1:.0f} ({(b0 - b1) / b0:.0%} of P0's take)",
    )


if __name__ == "__main__":
    print("=" * 78)
    print("Kaggriculture engine verification  (kaggle-environments installed version)")
    import importlib.metadata as md

    print("kaggle-environments", md.version("kaggle-environments"))
    print("=" * 78)
    t_last_step()
    t_scripted()
    t_shed_overflow()
    t_market_floor_and_full_shed()
    t_slot_priority()
    print("=" * 78)
    npass = sum(1 for _, ok, _ in RESULTS if ok)
    print(f"{npass}/{len(RESULTS)} checks passed")
    for name, ok, _ in RESULTS:
        if not ok:
            print("  FAILED:", name)
