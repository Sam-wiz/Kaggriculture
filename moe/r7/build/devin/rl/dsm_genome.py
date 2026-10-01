"""DSM-seeded genome, derived from mine/rawkeep/ds_DSM.jsonl
(50 raw episodes, 36k obs->action rows) + the r7 thread's day-indexed
program decode.

Measured aggregates (per-episode means over n=50):
  hires/day: ~4 d0-1 -> ~6 d2-5 -> ~10.4 plateau from d9
  quads:     1 -> 2 at day 6 (75%), 2 -> 3 at day 9-10; NEVER 4
  animals:   d0 COW~2+SHEEP~3 | d6 COW~4.2 GOOSE~1.8 | d9 COW~2.9
             -> season totals C~11, S~8, G~2-6 (team_specs: C11.1 S7.6 G6.4)
  seeds:     d0 MELON~6+WHEAT~13 | d1-2 MELON~+9 | d2-7 STRAWBERRY~29
             d6+ TOMATO lanes | CARROT grows to ~8/day d23-26
             WHEAT seeds ongoing ~200-860/day (grown feed program)
  feed:      BUY_PRODUCT:WHEAT ~176/ep, clustered d6-27

islandga-spec encoding notes:
* herd waves are cumulative "reach N by day d" targets (the compiler's
  ladder re-emits buys and the executor's ledger valve stops at goal).
* prog counts are tiles per quadrant; structures are placed first, crops
  fill the rest, over-spec is clipped at the tile count.
* sellpol "sweep" is the closest of the three policies to DSM's standing
  sell-stream (top-up toward cumulative production).
"""
import copy

DSM_GENOME = {
    "ne": 6, "sw": 9, "se": None,          # quads 1->2 @d6, 2->3 @d9-10, no SE
    "plateau": 10, "ramp_full": 7,          # ~10.4 hands by d9
    "tomato_day": 11, "melon2": 0,          # tomato lane d11-22; single melon pass
    "sellpol": "sweep",                     # standing-sell approximation
    "herd": [[0, "COW", 2], [0, "SHEEP", 3],
             [6, "COW", 5], [6, "GOOSE", 4],
             [9, "COW", 4], [12, "SHEEP", 5],
             [15, "GOOSE", 2]],             # -> C11 / S8 / G6
    "prog": {
        "NW": {"MELON": 15, "WHEAT": 10},                     # d0-2 melon rush
        "NE": {"STRAWBERRY": 14, "WHEAT": 8, "TOMATO": 3},    # strawberry d6+
        "SW": {"TOMATO": 10, "CARROT": 8, "WHEAT": 5, "STRAWBERRY": 2},
        "SE": {},
    },
}


def dsm_genome():
    return copy.deepcopy(DSM_GENOME)


if __name__ == "__main__":
    import json
    print(json.dumps(DSM_GENOME, indent=1))
