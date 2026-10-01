"""Upper bound on what a *perfect* executor could bank with our farm design.

Two resources bind: tile-days and unit-actions. Revenue is concave in units sold
(the market curve), so the optimum is found by allocating each marginal unit of
production to whichever recipe has the best marginal revenue per shadow-priced
resource, then tightening the shadow prices until both constraints bind.

The point of this is to separate "our planner picks the wrong crops" from "no
plan could do better with this action budget".
"""

import argparse
import math

from kaggle_environments.envs.kaggriculture import kaggriculture as K

I0 = 10000

# tile_days = days the tile is occupied per cycle
# actions   = unit-actions per cycle (plant, waters, fertilise, harvest)
# units     = units produced per cycle
CROP_RECIPES = {
    "WHEAT_f":  dict(product="WHEAT",      tile_days=4,  actions=7,  units=6, seed=10, fert=1),
    "WHEAT":    dict(product="WHEAT",      tile_days=4,  actions=6,  units=4, seed=10, fert=0),
    "CARROT_f": dict(product="CARROT",     tile_days=3,  actions=6,  units=4, seed=20, fert=1),
    "CARROT":   dict(product="CARROT",     tile_days=3,  actions=5,  units=3, seed=20, fert=0),
    "TOMATO_f": dict(product="TOMATO",     tile_days=12, actions=13, units=8, seed=50, fert=2),
    "STRAW_f":  dict(product="STRAWBERRY", tile_days=17, actions=14, units=8, seed=100, fert=2),
    "MELON":    dict(product="MELON",      tile_days=11, actions=10, units=6, seed=80, fert=0),
}

# per animal-day: 1 tile, `actions` unit-actions, `rate` product units, 1 wheat eaten,
# plus 1 fertilizer collected
ANIMAL_RECIPES = {
    "COW":   dict(product="MILK", rate=1.5,  actions=3.5, cost=400, first=8),
    "SHEEP": dict(product="WOOL", rate=4/3., actions=3.4, cost=500, first=6),
    "GOOSE": dict(product="EGG",  rate=2.0,  actions=4.0, cost=300, first=4),
}


def drain_total(item, days=30):
    """Units the town removes over `days`, using the expected shop mix."""
    exp = 0.0
    for shop, prods in K.SHOPS.items():
        m = 2.0 if len(prods) == 1 else 1.0
        if item in prods:
            exp += m / len(K.SHOPS)
    shop_days = 0
    for d in range(days):
        shop_days += min(K.MAX_SHOP_INSTANCES, d // 3)
    total = exp * shop_days * 6
    if item != "FERTILIZER":
        total += days
    return total


class Market:
    """Tracks how much of each product we have already sold and prices the next unit."""

    def __init__(self, opp_share=0.0):
        self.sold = {p: 0.0 for p in K.PRODUCTS}
        self.opp = {p: opp_share * drain_total(p) for p in K.PRODUCTS}

    def inv(self, p):
        return I0 - drain_total(p) + self.sold[p] + self.opp[p]

    def marginal(self, p, n=1.0):
        return K.market_price(p, int(self.inv(p)))

    def sell(self, p, n):
        rev = 0.0
        for _ in range(int(n)):
            rev += K.market_price(p, int(self.inv(p)))
            self.sold[p] += 1
        return rev


def solve(tile_days, actions, opp_share=0.0, wheat_price=45.0, verbose=True):
    """Greedy marginal allocation under shadow prices on both resources."""
    mkt = Market(opp_share)
    used_t = used_a = 0.0
    chosen = {}
    wheat_needed = 0.0

    def crop_step(name):
        r = CROP_RECIPES[name]
        rev = mkt.marginal(r["product"]) * r["units"]
        rev -= r["seed"]
        rev += r["fert"] * 0  # fertilizer from animals is free at the margin
        return rev, r["tile_days"], r["actions"], r["units"]

    def animal_step(name):
        a = ANIMAL_RECIPES[name]
        # one animal for the rest of a 22-day productive window
        days = 22 - a["first"]
        if days <= 0:
            return -1, 1, 1, 0
        units = a["rate"] * days
        rev = mkt.marginal(a["product"]) * units
        rev += mkt.marginal("FERTILIZER") * days   # 1 fertilizer per animal-day
        rev -= wheat_price * days                  # feed
        rev -= a["cost"]
        return rev, days, a["actions"] * days + 2, units

    while True:
        best = None
        for name in CROP_RECIPES:
            rev, td, ac, u = crop_step(name)
            if rev <= 0:
                continue
            score = rev / (td / max(tile_days, 1) + ac / max(actions, 1))
            if best is None or score > best[0]:
                best = (score, "crop", name, rev, td, ac, u)
        for name in ANIMAL_RECIPES:
            rev, td, ac, u = animal_step(name)
            if rev <= 0:
                continue
            score = rev / (td / max(tile_days, 1) + ac / max(actions, 1))
            if best is None or score > best[0]:
                best = (score, "animal", name, rev, td, ac, u)
        if best is None:
            break
        _s, kind, name, rev, td, ac, u = best
        if used_t + td > tile_days or used_a + ac > actions:
            break
        used_t += td
        used_a += ac
        chosen[name] = chosen.get(name, 0) + 1
        prod = (CROP_RECIPES if kind == "crop" else ANIMAL_RECIPES)[name]["product"]
        mkt.sell(prod, u)
        if kind == "animal":
            mkt.sell("FERTILIZER", td)
            wheat_needed += td

    revenue = 0.0
    for p in K.PRODUCTS:
        inv = I0 - drain_total(p) + mkt.opp[p]
        for _ in range(int(mkt.sold[p])):
            revenue += K.market_price(p, int(inv))
            inv += 1
    cost = wheat_needed * wheat_price
    for name, n in chosen.items():
        if name in CROP_RECIPES:
            cost += CROP_RECIPES[name]["seed"] * n
        else:
            cost += ANIMAL_RECIPES[name]["cost"] * n
    if verbose:
        print(f"  tile-days {used_t:.0f}/{tile_days}   actions {used_a:.0f}/{actions}"
              f"   opp_share={opp_share}")
        print(f"  portfolio: {chosen}")
        print(f"  units sold: { {p: int(v) for p, v in mkt.sold.items() if v} }")
        print(f"  gross ${revenue:,.0f}   inputs ${cost:,.0f}   NET ${revenue-cost:,.0f}")
    return revenue - cost


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tiles", type=int, default=75)
    ap.add_argument("--days", type=int, default=24, help="usable days once land is bought")
    ap.add_argument("--units", type=float, default=12.5, help="farmer + hands per turn")
    args = ap.parse_args()

    turns = 24 * args.days
    for eff in (0.40, 0.55, 0.70, 1.00):
        actions = args.units * turns * eff
        print(f"\n=== movement efficiency {eff:.0%}  "
              f"({actions:,.0f} productive actions, {args.tiles * args.days:,} tile-days)")
        for opp in (0.0, 0.5):
            solve(args.tiles * args.days, actions, opp_share=opp)


if __name__ == "__main__":
    main()
