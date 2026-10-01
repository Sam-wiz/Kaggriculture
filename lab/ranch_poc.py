"""Standalone ranch proof-of-concept vs pass: farmer builds one pasture,
buys a sheep, places it, runs feed/care/harvest/drop daily. Measures the
yield curve + revenue of a single well-cared sheep.
"""
import sys
sys.path.insert(0, ".")
import harness

PASTURE = (4, 3)      # empty NW tile north of shed spawn
SHED = (4, 4)         # shed-adjacent tile


def ranch_agent(obs, cfg=None):
    me = obs["farms"][obs["player"]]
    tiles = me["tiles"]
    fx, fy = me["farmer"]
    shed = obs["private"]["shed"]
    inv = obs["private"]["inventories"][0]
    money = me["money"]
    market = []

    def at(p):
        return (fx, fy) == p

    def toward(p):
        x, y = p
        if fx < x: return ["EAST"]
        if fx > x: return ["WEST"]
        if fy < y: return ["SOUTH"]
        if fy > y: return ["NORTH"]
        return None

    tile_p = tiles[PASTURE[1]][PASTURE[0]]
    has_pasture = isinstance(tile_p, dict) and tile_p.get("kind") == "PASTURE"
    has_animal = has_pasture and "animal" in tile_p

    # market: buy sheep once we can afford and have none in shed/inventory
    if not has_animal and shed.get("SHEEP", 0) == 0 and inv.get("SHEEP", 0) == 0 and money >= 500:
        market.append(["BUY_ANIMAL", "SHEEP", 1])
    # keep a little wheat for feed
    if inv.get("WHEAT", 0) == 0 and shed.get("WHEAT", 0) == 0 and money >= 50:
        market.append(["BUY_PRODUCT", "WHEAT", 5])
    # sell wool whenever it's in the shed
    if shed.get("WOOL", 0) > 0:
        market.append(["SELL", "WOOL", shed["WOOL"]])

    farmer = ["PASS"]
    if not has_pasture:
        if not at(PASTURE):
            farmer = toward(PASTURE)
        else:
            farmer = ["BUILD_PASTURE"]
    elif not has_animal:
        if shed.get("SHEEP", 0) > 0 and inv.get("SHEEP", 0) == 0:
            if not at(SHED): farmer = toward(SHED)
            else: farmer = ["PICKUP", "SHEEP", 1]
        elif inv.get("SHEEP", 0) > 0:
            if not at(PASTURE): farmer = toward(PASTURE)
            else: farmer = ["PLACE", "SHEEP"]
        elif not at(SHED):
            farmer = toward(SHED)
    else:
        # animal loop: carry wheat, service animal, drop products
        if inv.get("WHEAT", 0) == 0:
            if not at(SHED): farmer = toward(SHED)
            elif shed.get("WHEAT", 0) > 0: farmer = ["PICKUP", "WHEAT", 5]
            else: farmer = ["PASS"]
        elif not at(PASTURE):
            farmer = toward(PASTURE)
        elif not tile_p["fed_today"]:
            farmer = ["FEED"]
        elif not tile_p["cared_today"]:
            farmer = ["CARE"]
        elif tile_p.get("fertilizer_available"):
            farmer = ["COLLECT_FERTILIZER"]
        elif tile_p.get("yield_units", 0) > 0:
            farmer = ["HARVEST"]
        else:
            # done for the day: return to shed and drop
            if not at(SHED): farmer = toward(SHED)
            elif inv: farmer = ["DROP"]
            else: farmer = ["PASS"]

    return {"farmer": farmer, "hands": [], "market": market}


if __name__ == "__main__":
    wool = [0]
    money = [0]

    def spy(step, state, env):
        o = state[0].observation
        wool[0] = o["private"]["shed"].get("WOOL", 0)
        money[0] = o["farms"][0]["money"]

    r = harness.run_episode(ranch_agent, "pass", seed=6000,
                          catch_errors=True, on_step=spy)
    print("reward", r["reward"], "final shed wool", wool[0])
