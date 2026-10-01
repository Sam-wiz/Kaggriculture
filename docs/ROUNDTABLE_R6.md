# Round-Table R6 — post-falsification hunt

Repo: /Users/samrudh/Documents/Projects/kaggle/Kaggriculture
READ FIRST: HANDOFF.md (append-only log incl. all falsifications), then this file.
Goal: lift the live Kaggriculture agent to 3000+/top-10. ~5.5 days left.
Constraint: single-file stdlib-only submission; every claim must survive a
real-engine holdout gate (paired seeds, both seats) — nothing ships without it.

## Live state
L96 pair submitted and converging: subV_sirxL96 ref 56495194 (~2210), 
subV2_sirxL96 ref 56526468 (~2246, climbing faster). Top-10 cutoff ~2910;
3k+ club = DSM 3071 / DECEM 3034 / Vadim 3005. Our realistic asymptote est.
2500-2700 — we are ~400-700 short. Quota: 4 slots/day, held in reserve.

## What just happened (r5-r6): the router refit died 3 ways — learn the mechanism

Architecture: 41 fixed action "tapes" (routes); shared prefix to step 144
(day 6); router picks route at step 144 keyed on first-2 unlocked shops
(_R108 map for non-yarn pairs, V92 yarn->9, V93 rival-fingerprint->128);
forced route 2 at step 648 (day 27). Overlays: SIRX sell-impact ordering,
f55 floors, prem, projected-shed, reclaim, L96 endgame lead.

### Falsified this session
1. **Decoupled-engine route refit (rmap)**: patched engine gave shop draw its
   own RNG stream; measured per-route margins under identical draws; fit ridge
   on shop-count features. In-sample regret 1131 vs shipped 5029, but real
   holdout W27-L53, -2481. 
2. **Real-engine pick-remap (rm2)**: re-measured on UNPATCHED engine keyed on
   first-2 shops (route-independent — shared prefix spans the day-3/6 draws).
   Pick-level dominators looked strong in-sample (9->103 +3695/88%, 105->116
   +3208/100%) but fresh-seed gate W18-L42, -1897. Winner's curse: single
   samples per cell don't transfer.
3. **Intra-family re-commit (rm3)**: prefix tree lets siblings share tape to
   day 9-26; re-pick via shipped map on last-2 shops. +48/seed screen —
   intra-family day-9 oracle ceiling measured at only +263/seed.
4. **Rival-conditional**: route 9's -11.4k vs koshinm was a pin artifact (route
   9 on NON-yarn draws). On real yarn draws route 9 is best vs koshinm (+210).
   And every runnable public-notebook rival already loses to L96; real top-10
   are unrunnable code submissions.

### The mechanism that matters — the shop draw is NOT exogenous
`_spawn_weeds` drains the day's RNG on every empty tile BEFORE rng.choice picks
the new shop. So: (a) first-2 shops ARE route-independent (shared prefix covers
days 0-6); (b) shops 3+ depend on our farm state/route; (c) any "best route for
draw D" measurement must use the real engine, where picking route R induces
draw D(R). The shipped map co-adapted to induced draws over its construction.

## The remaining hypothesis space — DIG HERE

### H1. Shop-draw SHAPING (the falsification inverted)
If our route/farm state perturbs the shop draw, maybe we can STEER it. The
labels already record each route's induced full shop sequence per seed
(route_labels_real.jsonl, ~3500 rows). Question: does any route systematically
induce better shop composition across seeds? If farm-state patterns bias the
draw (e.g., more premium shops), that's a new information-free edge — pick the
route that manufactures demand for its own products. NOTE: a top-10 notebook
is literally named "shape-the-shop-work-the-pasture" — this may be a known
technique. Check rivals/shape-the-shop-work-the-pasture-top-10/ source!

### H2. Mid-game weed-RNG steering
Empty-tile count controls how many RNG draws weeds consume per day -> changes
shop picks. Could deliberately leaving weeds/empty tiles bias draws? Wilder
version of H1. Needs the RNG mechanics read carefully (kag env source in
.venv site-packages: kaggle_environments/envs/kaggriculture/).

### H3. Feed-leanness overlay (tetsuya ledger: -$8.7k spend, -$5.4k feed-wheat)
Our tapes BUY_PRODUCT WHEAT as feed (route 103: 3401 units!; 105: 110). An
overlay suppressing redundant wheat buys when shed wheat covers animal needs
is market-only (can't desync worker positions). Risk: under-buy -> unfed
animals escape. Must be conservative (suppress only when shed >> need).

### H4. Your own dig
Anything the falsifications list MISSED. E.g.: terminal-day inventory flush
timing; HIRE cost timing; quadrant unlock timing; market-order cap
prioritization under pressure; the day-27 route-2 endgame tape itself.

## Rules
- Do NOT re-propose anything in HANDOFF.md falsified list — read it first.
- Every hypothesis needs: the mechanism, the measurement, expected magnitude,
  and a kill criterion. Cheap probes beat speculation.
- Budget-aware: machine is loaded; prefer analyses on existing data
  (route_labels_real.jsonl, mine/tapes 223 archives, rivals/ 303 agents).
- Output to your assigned answer file; keep it under ~150 lines.
