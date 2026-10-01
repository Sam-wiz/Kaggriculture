"""Buy the animal the town actually wants.

The tape buys a fixed 9 cows and 9 sheep every game, whatever shops unlocked. That is often badly
wrong, because MILK and WOOL demand come from completely different shops:

    MILK : PIZZA_SHOP, ICE_CREAM_SHOP, SMOOTHIE_SHOP   (up to 3 distinct shops, 1 unit each)
    WOOL : YARN_STORE only                             (but 2 units, being a single-product shop)

Observed on one seed: four milk shops unlocked (days 6, 9, 12, 15) and YARN_STORE not until day 24.
Season demand was roughly 498 units of milk against 138 of wool -- and the tape still sold ~300
wool into it. Wool traded at $94 against a $200 base (collapsed), while milk held $166 on a $160
base. Pasture was being spent on a product nobody was buying.

COW and SHEEP occupy the same PASTURE structure, so swapping one for the other is structurally free
-- unlike crops, whose per-crop watering/yield windows make substitution destructive.

Demand is counted from shops that have ALREADY unlocked (no guessing at future draws): each shop
instance fires every 4 turns for the rest of the season, doubled if it is a single-product shop,
plus the town centre's 1/day.
"""

AM = dict(enabled=1, min_edge=1.15, from_day=1)

_MILK_SHOPS = {"PIZZA_SHOP": 1, "ICE_CREAM_SHOP": 1, "SMOOTHIE_SHOP": 1}
_WOOL_SHOPS = {"YARN_STORE": 2}
_TURNS = 720
_SHOP_EVERY = 4
_CENTER_EVERY = 24


def _remaining_demand(shops, step, table):
    """Units of this product the town will still eat, from shops already open."""
    left = max(0, _TURNS - step)
    per_shop_fires = left // _SHOP_EVERY
    total = sum(per_shop_fires * mult
                for s in shops for name, mult in table.items() if s == name)
    return total + left // _CENTER_EVERY          # town centre: 1/day


def _count_animals(farm, kind):
    n = 0
    for row in farm.get("tiles") or []:
        for t in row:
            if isinstance(t, dict) and t.get("animal") == kind:
                n += 1
    return n


def adjust(obs, market):
    """Swap COW<->SHEEP purchases toward whichever product the town still wants."""
    if not AM["enabled"] or not market:
        return market
    day = int(obs.get("day", 0) or 0)
    if day < AM["from_day"]:
        return market
    if not any(o and o[0] == "BUY_ANIMAL" and len(o) > 1 and o[1] in ("COW", "SHEEP")
               for o in market):
        return market

    step = int(obs.get("step") or day * 24)
    shops = list((obs.get("town") or {}).get("unlocked_shops") or [])
    farm = obs["farms"][obs["player"]]

    milk_d = _remaining_demand(shops, step, _MILK_SHOPS)
    wool_d = _remaining_demand(shops, step, _WOOL_SHOPS)
    cows = _count_animals(farm, "COW")
    sheep = _count_animals(farm, "SHEEP")

    # demand still unclaimed per animal already producing it
    milk_score = milk_d / float(cows + 1)
    wool_score = wool_d / float(sheep + 1)

    out = []
    for o in market:
        if o and o[0] == "BUY_ANIMAL" and len(o) > 1 and o[1] in ("COW", "SHEEP"):
            want = o[1]
            if want == "SHEEP" and milk_score > wool_score * AM["min_edge"]:
                want = "COW"
            elif want == "COW" and wool_score > milk_score * AM["min_edge"]:
                want = "SHEEP"
            o = [o[0], want] + list(o[2:])
        out.append(o)
    return out
