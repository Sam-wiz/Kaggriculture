"""Move land off wheat and onto carrot.

Measured on the tuned build over 6 games, revenue per tile-turn by crop:

    WHEAT       14,091 tile-turns -> $14,850   $1.1/tile-turn
    STRAWBERRY  12,930            -> $45,483   $3.5
    MELON        2,846            -> $15,102   $5.3
    CARROT         343            -> $ 1,228   $3.6

Wheat occupies more land than anything else and pays 3-5x less for it. This is the same edge the
one genuinely adaptive agent on the ladder runs on: it plants ~131 wheat to our ~195 and buys its
feed instead, freeing the tiles for better crops.

**Carrot specifically, and nothing slower.** Carrot matures in 3 days against wheat's 4, so a tile
substituted wheat->carrot is ready *before* the tape's scheduled HARVEST and the schedule still
lands. Substituting a slower crop (melon 12d, strawberry 10d) leaves the tile unready when the tape
harvests and still occupied when it tries to replant, which is why earlier attempts at this lost
$21k-$49k.

Two engine rules drive the design:
  * `_apply_unit_action` runs BEFORE `_process_market`, so a seed bought this turn is not available
    to a PLANT this turn. Carrot seeds must be bought ahead.
  * Planting is atomic per crop: if a turn demands more seed of a crop than is held, EVERY planting
    of that crop that turn is dropped. So a substitution is only ever made when the carrot seed
    already in hand covers the tape's own carrot plantings plus ours.
"""

CS = dict(enabled=1, max_sub_per_turn=2, buffer=6, cap_frac=0.35, stop_day=24, feed_floor=40)

_state = {"subbed": 0, "wheat_seen": 0}


def reset():
    _state["subbed"] = 0
    _state["wheat_seen"] = 0


def apply(obs, farmer_act, hand_acts, market):
    """Rewrite some PLANT WHEAT into PLANT CARROT, and keep carrot seed stocked ahead."""
    if not CS["enabled"]:
        return farmer_act, hand_acts, market
    priv = obs.get("private") or {}
    seeds = priv.get("seeds") or {}
    shed = priv.get("shed") or {}
    day = int(obs.get("day", 0) or 0)

    acts = [farmer_act] + list(hand_acts)
    wheat_idx = [i for i, a in enumerate(acts)
                 if a and a[0] == "PLANT" and len(a) > 1 and a[1] == "WHEAT"]
    tape_carrot = sum(1 for a in acts if a and a[0] == "PLANT" and len(a) > 1 and a[1] == "CARROT")
    _state["wheat_seen"] += len(wheat_idx)

    out = list(acts)
    if wheat_idx and day < CS["stop_day"]:
        # never exceed the seed actually held, or the whole crop's plantings are voided
        room = int(seeds.get("CARROT", 0)) - tape_carrot
        budget = int(CS["cap_frac"] * max(1, _state["wheat_seen"])) - _state["subbed"]
        n = min(len(wheat_idx), CS["max_sub_per_turn"], max(0, room), max(0, budget))
        # keep enough wheat coming for the animals
        if int(shed.get("WHEAT", 0)) < CS["feed_floor"]:
            n = 0
        for i in wheat_idx[:n]:
            out[i] = ["PLANT", "CARROT"]
        _state["subbed"] += n

    # keep a small carrot-seed buffer so a substitution is possible when the chance comes
    m = [list(o) for o in (market or [])]
    if (day < CS["stop_day"] and len(m) < 10
            and int(seeds.get("CARROT", 0)) < CS["buffer"]
            and not any(o and o[0] == "BUY_SEED" and len(o) > 1 and o[1] == "CARROT" for o in m)):
        m.append(["BUY_SEED", "CARROT", CS["buffer"]])
    return out[0], out[1:], m
