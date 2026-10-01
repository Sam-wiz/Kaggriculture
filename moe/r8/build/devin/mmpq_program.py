# MMPQ executed program constants — consensus over 450 resim'd eps (bc2r_MMPQ
# label/G counts) + mmpq lane's 4-ep obs-exact cross-check. Same shapes as the
# DSM tables in gen_clone_bc.py / clone_dsm_bc.py for drop-in generation.

# hands hired per day (executed averages, rounded): ~11 sustained, wind-down d28-29
HIRES = [5, 3, 4, 5, 6, 5, 6, 8, 9, 10, 11, 10, 10, 10, 10,
         11, 11, 11, 12, 11, 11, 11, 11, 11, 11, 11, 10, 10, 10, 9]

# executed land buys: NE@5, SW@8-9; SE in ~16% of eps at d15-18 (money-gated)
LAND_DAYS = {5: "NE", 9: "SW"}
LAND_SE_DAY = 15          # opportunistic 4th quadrant when rich
LAND_SE_CASH = 12000      # only if bank >> cost (observed d15+ buys)

# herd: (lo_day, hi_day, species, target_incl_escape_losses) — MMPQ over-buys;
# ~8 sheep + ~3.5 cows + ~1 goose escape per ep and get re-bought (order-spam)
HERD_PLAN = [
    (0, 5, "COW", 4), (0, 5, "SHEEP", 4),
    (2, 10, "GOOSE", 6),
    (6, 12, "COW", 9), (6, 17, "SHEEP", 14),
    (10, 20, "GOOSE", 7),
]

# structures: 16.8 pastures + 3.8 coops built per ep
STRUCT_PLAN = [(0, "PASTURE", 6), (2, "COOP", 2), (5, "PASTURE", 10),
               (8, "COOP", 4), (10, "PASTURE", 14), (14, "PASTURE", 17)]

# crops: (lo, hi, crop, target_tiles, min_cash) — wheat mass all season,
# strawberry d1-16 (d6 spike), melon d0-2 burst, carrot ramping late, tomato d13-19
CROP_PLAN = [
    (0, 2, "MELON", 12, 250),
    (1, 8, "STRAWBERRY", 34, 300),
    (0, 27, "WHEAT", 60, 40),
    (8, 27, "CARROT", 30, 60),
    (13, 19, "TOMATO", 10, 200),
]

# market: standing sells INCLUDING fertilizer (MMPQ sells surplus fert ~181/ep)
SELL_QTY = 3
SELL_FERT_RESERVE = 30    # keep a fert floor for FERTILIZE runs
