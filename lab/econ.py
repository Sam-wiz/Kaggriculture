"""Economic analysis of the Kaggriculture market.

Answers: how much money is actually extractable per product, what the town drain
schedule looks like, and what each crop/animal recipe is worth per farmer-action.
"""

import math
from collections import defaultdict

from kaggle_environments.envs.kaggriculture import kaggriculture as K

PRODUCTS = K.PRODUCTS
SHOPS = K.SHOPS
I0 = K.MARKET_I0


def price(item, inv):
    return K.market_price(item, inv)


def shop_demand_per_tick(shop):
    """{product: units consumed per tick} for one instance of `shop`."""
    prods = SHOPS[shop]
    mult = 2 if len(prods) == 1 else 1
    return {p: mult for p in prods}


def expected_demand_per_instance():
    """Expected units/tick per product for a uniformly random shop instance."""
    out = defaultdict(float)
    for shop in SHOPS:
        for p, m in shop_demand_per_tick(shop).items():
            out[p] += m / len(SHOPS)
    return dict(out)


def drain_schedule(shops_by_day=None, days=30, turns_per_day=24,
                   shop_interval=4, center_interval=24):
    """Cumulative town drain per product at the END of each day.

    shops_by_day: list (len=days) of lists of shop names active that day.
    Defaults to the *expected* mix (fractional) using the standard unlock ramp.
    """
    cum = defaultdict(float)
    per_day = []
    exp = expected_demand_per_instance()
    for d in range(days):
        n_ticks_shop = sum(1 for h in range(turns_per_day)
                           if (d * turns_per_day + h) % shop_interval == 0)
        n_ticks_center = sum(1 for h in range(turns_per_day)
                             if (d * turns_per_day + h) % center_interval == 0)
        if shops_by_day is None:
            n_shops = min(K.MAX_SHOP_INSTANCES, d // 3)
            for p, v in exp.items():
                cum[p] += v * n_shops * n_ticks_shop
        else:
            for shop in shops_by_day[d]:
                for p, m in shop_demand_per_tick(shop).items():
                    cum[p] += m * n_ticks_shop
        for p in PRODUCTS:
            if p != "FERTILIZER":
                cum[p] += n_ticks_center
        per_day.append(dict(cum))
    return per_day


def revenue_curve(item, start_inv, n):
    """Total revenue and marginal price for selling n units starting at start_inv.
    Mirrors the engine: price quoted at pre-sell inventory; $1 sales do not add supply."""
    inv = start_inv
    total = 0
    marg = []
    for _ in range(n):
        p = price(item, inv)
        total += p
        marg.append(p)
        if p > 1:
            inv += 1
    return total, marg


# ---------------------------------------------------------------- recipes ----
# (name, actions_per_cycle, units_per_cycle, tile_days, seed_cost, product,
#  fertilizer_used)
def crop_recipes():
    """Action counts derived from the engine rules:
      - must WATER on the planting day (consecutive_unwatered starts at 1)
      - thereafter watering every other day keeps a plant alive
      - one-time crops: watering inside [ceil(max_yield_day/2), max_yield_day]
        adds +1 (or +2 if fertilized that day) to yield, capped at max_yield
      - harvest legal from first_yield_day; one-time crops vacate the tile
    """
    out = []

    # WHEAT: window ages 2..4, start yield 1, cap 6 (4 without fertilizer)
    out.append(dict(name="WHEAT_full", crop="WHEAT", actions=6, units=4, tile_days=4,
                    seed=10, fert=0))              # plant,W0,W2,W3,W4,harvest
    out.append(dict(name="WHEAT_fast", crop="WHEAT", actions=5, units=3, tile_days=3,
                    seed=10, fert=0))              # plant,W0,W2,W3,harvest
    out.append(dict(name="WHEAT_fert", crop="WHEAT", actions=7, units=6, tile_days=4,
                    seed=10, fert=1))              # + FERTILIZE at age 2

    # CARROT: window ages 2..3, start 1, cap 4
    out.append(dict(name="CARROT_full", crop="CARROT", actions=5, units=3, tile_days=3,
                    seed=20, fert=0))              # plant,W0,W2,W3,harvest
    out.append(dict(name="CARROT_fert", crop="CARROT", actions=6, units=4, tile_days=3,
                    seed=20, fert=1))

    # MELON: window ages 6..12, start 1, cap 6; first harvest age 10
    out.append(dict(name="MELON_full", crop="MELON", actions=10, units=6, tile_days=10,
                    seed=80, fert=0))              # plant,W0,2,4,6,7,8,9,10,harvest
    out.append(dict(name="MELON_fert", crop="MELON", actions=10, units=6, tile_days=10,
                    seed=80, fert=1))              # plant,W0,2,4,6,7,8,+fert,W10?,harvest

    # TOMATO: productions at ages 8..11 (4 of them), 2/ea if watered+fertilized
    out.append(dict(name="TOMATO_plain", crop="TOMATO", actions=11, units=4, tile_days=11,
                    seed=50, fert=0))              # plant,W0,2,4,6,7,8,9,10 + 2 harvest
    out.append(dict(name="TOMATO_fert", crop="TOMATO", actions=13, units=8, tile_days=11,
                    seed=50, fert=2))

    # STRAWBERRY: productions at ages 10,12,14,16; 2/ea if watered+fertilized
    out.append(dict(name="STRAW_plain", crop="STRAWBERRY", actions=15, units=4, tile_days=16,
                    seed=100, fert=0))
    out.append(dict(name="STRAW_fert", crop="STRAWBERRY", actions=21, units=8, tile_days=16,
                    seed=100, fert=4))
    return out


def animal_recipes():
    """Steady-state per-day figures with daily FEED + CARE.

    care banking: bonus resets on each production and re-accrues +1 per fed&cared
    day, so a production yields 1 + interval units.
    """
    out = []
    for a, d in K.ANIMALS.items():
        iv = d["interval"]
        per_prod = 1 + iv                       # base 1 + banked care bonus
        per_prod = min(per_prod, d["max_held"])
        per_day = per_prod / iv
        # FEED + CARE every day, HARVEST every `iv` days, COLLECT_FERTILIZER daily
        acts = 2 + 1.0 / iv + 1
        out.append(dict(name=a, animal=a, product=d["product"], cost=d["cost"],
                        per_day=per_day, actions_per_day=acts,
                        wheat_per_day=1, first=d["first_yield_day"],
                        max_held=d["max_held"]))
    return out


def report():
    print("=" * 78)
    print("EXPECTED TOWN DRAIN PER PRODUCT (units removed from market)")
    print("=" * 78)
    sched = drain_schedule()
    end = defaultdict(float, sched[-1])
    exp = expected_demand_per_instance()
    print(f"{'product':<12}{'/tick/shop':>11}{'late /day':>11}{'total 30d':>11}"
          f"{'P(end,unsold)':>15}{'base':>7}")
    for p in PRODUCTS:
        late = exp.get(p, 0.0) * 8 * 6 + (1 if p != "FERTILIZER" else 0)
        print(f"{p:<12}{exp.get(p,0.0):>11.3f}{late:>11.1f}{end[p]:>11.0f}"
              f"{price(p, I0-int(end[p])):>15}{K.MARKET_PARAMS[p]['base']:>7}")

    print()
    print("=" * 78)
    print("SELL REVENUE: total $ for selling N units all at once at end of season")
    print("(start inventory = I0 - expected drain; marginal price shown)")
    print("=" * 78)
    print(f"{'product':<12}" + "".join(f"{'N='+str(n):>12}" for n in (25, 50, 100, 200, 400)))
    for p in PRODUCTS:
        start = I0 - int(end[p])
        row = ""
        for n in (25, 50, 100, 200, 400):
            tot, marg = revenue_curve(p, start, n)
            row += f"{tot:>7}/{marg[-1]:<4}"
        print(f"{p:<12}{row}")

    print()
    print("=" * 78)
    print("CROP RECIPES  ($ uses price at I0-drain, i.e. a lightly-sold market)")
    print("=" * 78)
    print(f"{'recipe':<14}{'acts':>5}{'units':>6}{'tiledays':>9}{'$/unit':>8}"
          f"{'$/action':>10}{'$/tile/day':>11}{'u/tile/day':>11}")
    for r in crop_recipes():
        pr = price(r["crop"], I0 - int(end[r["crop"]]))
        gross = r["units"] * pr - r["seed"]
        print(f"{r['name']:<14}{r['actions']:>5}{r['units']:>6}{r['tile_days']:>9}"
              f"{pr:>8}{gross/r['actions']:>10.1f}{gross/r['tile_days']:>11.1f}"
              f"{r['units']/r['tile_days']:>11.2f}")

    print()
    print("=" * 78)
    print("ANIMAL RECIPES (steady state, daily FEED+CARE, wheat feed cost at $45)")
    print("=" * 78)
    print(f"{'animal':<8}{'prod':<6}{'/day':>6}{'acts/day':>9}{'$/unit':>8}"
          f"{'$/day net':>11}{'$/action':>10}{'first':>7}")
    for r in animal_recipes():
        pr = price(r["product"], I0 - int(end[r["product"]]))
        net = r["per_day"] * pr - 45  # wheat feed
        # collecting a fertilizer each day is one of those actions; count its value
        print(f"{r['name']:<8}{r['product']:<6}{r['per_day']:>6.2f}{r['actions_per_day']:>9.2f}"
              f"{pr:>8}{net:>11.1f}{net/r['actions_per_day']:>10.1f}{r['first']:>7}")

    print()
    print("FERTILIZER: 1 action (COLLECT_FERTILIZER) per animal per day.")
    for n in (50, 100, 200, 300, 500):
        tot, marg = revenue_curve("FERTILIZER", I0, n)
        print(f"  sell {n:>3}: ${tot:>6}  avg ${tot/n:>6.1f}/unit  marginal ${marg[-1]}")

    print()
    print("=" * 78)
    print("HIRING: marginal cost of the k-th hand of a day (24 actions each)")
    print("=" * 78)
    tot = 0
    for k in range(1, 21):
        c = K._fib(k - 1)
        tot += c
        print(f"  hand {k:>2}: cost ${c:<7} cumulative ${tot:<7} $/action {c/24:>7.2f}")


if __name__ == "__main__":
    report()
