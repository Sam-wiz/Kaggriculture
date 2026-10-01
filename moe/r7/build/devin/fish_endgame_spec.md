# devin-f: fish endgame forensics — where the private +800 lives

## Labor engine: v8 ≈ fish (nearly identical)
Per-3-day unit ops/game, fish (37 games recorded) vs v8 (6 games sim):

| window | HIRE fish/v8 | FEED | CARE | COLL_FERT | WATER | HARVEST |
|---|---|---|---|---|---|---|
| d9-11 | 31.6/37.5 | 42/42 | 41.5/41 | 44/45 | 113/109 | 23.5/29 |
| d15-17 | 31.4/36 | 53/39 | 49/34 | 64/50 | 111/120 | 60/50 |
| d21-23 | 33.5/36 | 47/40 | 40/35 | 55/45 | 126/139 | 64/65 |
| d27-29 | 34.2/33 | 17/15 | 3.6/4.8 | 32/38 | 106/110 | 106/87 |

Same hires (~35/d), same builds (pastures d6-11 burst then 0, BUY_LAND ~2 quads d6-11),
same endgame taper (FEED/CARE lapse ~d26, harvest wave). The public r34 labor engine replicates
the fish's — **the private +800 is NOT in unit ops.**

## The actual divergence: herd sizing + market layer
- Herd bought by ~d12: fish ~10.2 COW + ~6.3 SHEEP + ~5.5 GOOSE; v8 ~5.5 + ~8.5 + ~4.3.
  Fish runs ~2x cows => ~2x MILK throughput, matching measured premium-sell volume.
- Sell volumes (units/game/3d, endgame): fish MILK 24-64 vs v8 22-32; STRAWBERRY ~45 vs ~10-45;
  fish sells TOMATO (~60/d27-29), v8 sells 0.
- => Fish's edge = **bigger cow herd + sustained ongoing-crop (strawberry/tomato) footprint +
  whatever its market-book policy does with the extra volume.** v8's seed-clustered fade is then
  a MARKET-layer failure on bad draws, not a labor failure — consistent with losses being
  seed-dependent across all opponents.

## Mechanism spec for a v8+fix (or an r34-chassis graft) — ranked by expected value
1. **Market/sell layer** — the contested axis. v8's books presumably mis-place vs responsive
   rivals on bad draws. Unknown exact rule (tapes show order lists but not intent); estimate
   via price-delta capture analysis of fish SELLs vs same-tick market state.
2. **Herd sizing** — cow count ~2x. Structural (pasture cap ~10 built by d11 vs v8's ~6).
   Cheap lever in a port, hard to graft as a constant.
3. **Ongoing-crop sustain** — TOMATO sells = dedicated ongoing patch v8 doesn't keep.
   ~60 units endgame ≈ few-hundred-per-game value; minor.
4. NOT labor, NOT builds, NOT hires — already replicated.

## Caveat
Tapes don't replay to banks (reduced dump ≠ sim-exact); sell volumes are reliable, op counts ±.
