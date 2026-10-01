"""Buy land as early as we can afford it, instead of on the tape's fixed schedule.

The tape buys its two extra quadrants at step 150 (day 6) and step 265 (day 11). Crop Dusta --
the one agent on the top ladder that is not running our tape, and which takes 50-20 off the rest
of it -- buys on days 5 and 8. That is worth roughly 75 extra tile-days.

This does not move the purchase to a fixed earlier step, which would just fail when the cash is
not there. It buys at the first turn from `day1`/`day2` onward where the money is actually
present, and never later than the tape would have. Land is bought out of the same thin cash the
morning HIRE orders come from, and an unpaid hire is what starts the death spiral, so every
purchase keeps `reserve` behind for the crew.
"""

LH = dict(enabled=1, day1=5, day2=8, reserve=150.0, max_extra=2)

_LAND_PRICES = (1000, 2000, 4000)


def _extra_owned(farm):
    q = farm.get("unlocked_quadrants") or []
    return max(0, len(q) - 1)


def adjust_market(obs, market):
    """Return a possibly-modified market order list, or None to leave it alone."""
    if not LH["enabled"]:
        return None
    farm = obs["farms"][obs["player"]]
    bought = _extra_owned(farm)
    out = list(market)
    changed = False

    # the tape's own land buys are now redundant once we already hold our quota
    if bought >= LH["max_extra"]:
        trimmed = [o for o in out if not (o and o[0] == "BUY_LAND")]
        if len(trimmed) != len(out):
            return trimmed
        return None

    if any(o and o[0] == "BUY_LAND" for o in out):
        return None                       # tape is already buying this turn

    day = int(obs.get("day", 0) or 0)
    want = day >= LH["day1"] if bought == 0 else day >= LH["day2"]
    if not want or bought >= len(_LAND_PRICES):
        return None

    price = _LAND_PRICES[bought]
    if float(farm["money"]) < price + LH["reserve"]:
        return None                       # leave the hires their money
    if len(out) >= 10:
        return None
    out.append(["BUY_LAND"])
    changed = True
    return out if changed else None
