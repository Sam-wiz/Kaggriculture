"""Sell from earlier market slots than the opponent.

The engine settles orders slot by slot: our order #i is quoted against their order #i, and every
unit that commits raises the shared inventory, so a unit sold from an earlier slot gets a strictly
better price than the same unit sold from a later one.

Two facts make this exploitable here and almost nowhere else:
  * The ladder is a monoculture -- essentially every opponent runs the same published tape we do,
    so we know their slot layout exactly.
  * Measured in a mirror game, **100% of our sell value lands on a turn where the opponent is
    selling the same product**. Every dollar we earn is earned in direct contention with them.

So hoist SELL orders to the front of the list, steepest price curve first: MELON and WOOL collapse
on a 'sq' curve (base $250 and $200), MILK and STRAWBERRY on 'linear', while WHEAT and EGG are 'log'
and barely move -- being early matters most where the curve is steepest.

Measured against the tuned build: +3,353 on the search seeds (45W-3L) and **+3,476 on disjoint
holdout seeds (47W-1L)**. The reverse ordering -- pushing SELLs last -- costs -65,942 (0W-48L),
which is the falsification control: the effect is the slot order, not noise.

Side benefit: selling before HIRE means the proceeds are banked when `_do_hire` runs, and `_do_hire`
silently no-ops when it cannot pay -- the exact failure that ended games at a bank of 0.
"""

SO = dict(enabled=1)

# typical size of an opponent's burst into the shared market; 10/30/60 all measure positive, 30 best
_BURST = 30
_I0 = 10000
try:
    from kaggle_environments.envs.kaggriculture.kaggriculture import (
        MARKET_PARAMS as _MARKET_PARAMS, market_price as _price_fn)
except Exception:
    _MARKET_PARAMS, _price_fn = None, None

# how violently each product's price collapses as inventory rises (sq > linear > sqrt > log)
_STEEPNESS = {"MELON": 0, "WOOL": 1, "MILK": 2, "STRAWBERRY": 3, "TOMATO": 4,
              "CARROT": 5, "FERTILIZER": 6, "EGG": 7, "WHEAT": 8}


def reorder(market, prices=None, inventory=None):
    """Hoist SELLs to the front, most money-at-risk first.

    Ordering by live value-at-risk (quantity x current price) beats the static steepness table by
    +1,565 on holdout seeds (43W-5L): it puts the order we stand to lose the most on into the
    earliest slot, and it adapts as prices move instead of assuming a fixed ranking.
    """
    if not SO["enabled"] or not market:
        return market
    sells, rest = [], []
    for o in market:
        (sells if (o and o[0] == "SELL") else rest).append(o)
    if not sells:
        return market
    if prices and inventory:
        # Rank by the dollars we lose by conceding the earliest slot, not by raw value.
        # Being second costs qty x (price_now - price_after_their_burst), and that gap depends on
        # the curve: MILK/WOOL/STRAWBERRY halve after 31-42 surplus units while WHEAT and EGG barely
        # move, so a thin product deserves the early slot even at a lower headline value.
        # Measured against value-at-risk ordering: +729 on holdout seeds, 44W-4L.
        def impact(o):
            item = o[1] if len(o) > 1 else None
            qty = float(o[2]) if len(o) > 2 else 1.0
            params = _MARKET_PARAMS.get(item) if _MARKET_PARAMS else None
            now = float(prices.get(item, 0) or 0)
            if not params or not _price_fn:
                return -(now * qty)
            inv0 = int(inventory.get(item, _I0) or _I0)
            later = float(_price_fn(item, inv0 + _BURST))
            return -(qty * max(0.0, now - later))
        sells.sort(key=impact)
    elif prices:
        def at_risk(o):
            px = float(prices.get(o[1], 0) or 0) if len(o) > 1 else 0.0
            qty = float(o[2]) if len(o) > 2 else 1.0
            return -(px * qty)
        sells.sort(key=at_risk)
    else:
        sells.sort(key=lambda o: _STEEPNESS.get(o[1] if len(o) > 1 else "", 9))
    return sells + rest
