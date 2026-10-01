"""Compute a seed's entire shop draw without running the game.

`_end_of_day` seeds its RNG as `random.Random((seed * 1_000_003) ^ day)` and, on every third day,
appends `rng.choice(sorted(SHOPS))`. Nothing about play enters it, so the eight shops a seed will
ever unlock -- and therefore the demand curve of the whole episode -- are known before turn 0.

That makes it cheap to build targeted seed sets: "give me 200 seeds that unlock 3+ YARN_STOREs" is
a loop, not a search. Since our losses scale with exactly that count, every experiment aimed at the
mismatch can be run on the draws where it actually bites.
"""
import random
import sys

from kaggle_environments.envs.kaggriculture.kaggriculture import SHOPS, MAX_SHOP_INSTANCES

NAMES = sorted(SHOPS)
SHOP_ITEMS = {s: tuple(SHOPS[s]) for s in NAMES}


def draw(seed, days=30, interval=3):
    """The unlock list as it stands at the end of the episode, in unlock order."""
    out = []
    for day in range(days):
        nxt = day + 1
        if nxt > 0 and nxt % interval == 0 and len(out) < MAX_SHOP_INSTANCES:
            rng = random.Random((seed * 1_000_003) ^ day)
            out.append(rng.choice(NAMES))
    return out


def demand(shops):
    """Units consumed per firing interval; a single-product shop counts double."""
    d = {}
    for s in shops:
        items = SHOP_ITEMS.get(s, ())
        mult = 2 if len(items) == 1 else 1
        for it in items:
            d[it] = d.get(it, 0) + mult
    return d


def seeds_with(pred, n, start=1, limit=4_000_000):
    out = []
    s = start
    while len(out) < n and s < limit:
        if pred(draw(s)):
            out.append(s)
        s += 1
    return out


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--verify":
        # episode 106242495, seed 20147307, observed unlock order from its replay
        got = draw(20147307)
        want = ["YARN_STORE", "PIZZA_SHOP", "ICE_CREAM_SHOP", "YARN_STORE", "YARN_STORE",
                "SMOOTHIE_SHOP", "FARMERS_MARKET", "YARN_STORE"]
        print("computed:", got)
        print("observed:", want)
        print("MATCH" if got == want else "MISMATCH")
        sys.exit(0)
    import collections
    c = collections.Counter()
    for s in range(1, 20001):
        c[draw(s).count("YARN_STORE")] += 1
    tot = sum(c.values())
    print("YARN_STORE count distribution over 20,000 seeds:")
    for k in sorted(c):
        print(f"   {k}: {c[k]:>6}  ({c[k]/tot:>5.1%})")
    print(f"\n3 or more: {sum(v for k,v in c.items() if k>=3)/tot:.1%} of all games")
