# clonefix — why `clone_dsm_bc.py` loses, what we fixed, where it landed

**devin (clonefix lane), r8.** Source: `moe/r7/build/devin/clone_dsm_bc.py`
(DSM BC clone: hardcoded season tables + 56→128→64→31 MLP job scorer).
Repaired agent: `moe/r8/build/clonefix/clone_dsm_bc2.py`.
Probe tooling: `probe.py` (per-day economy/labor/plant/animal/shed dump via
`harness.run_episode(..., on_step=cb)`), `probe2.py` (action histograms),
`gate.py` (paired-seat gate runner). Ablation kept for reference:
`clone_nomlp.py` (MLP stripped, nearest-urgent dispatch).

---

## 1. Scorecard

| pairing | seeds | seats | W-L-T (clone) | avg margin | clone avg |
|---|---|---|---|---|---|
| original clone vs v8x | 7000-7007 | both | 0-16-0 | −54,761 | ~37k |
| repaired MLP variant vs v8x | 7000-7007 | both | 0-16-0 | −38,328 | ~50k |
| repaired no-MLP (7000-7007 subset) | 7000-7007 | both | 0-16-0 | −37,805 | ~52k |
| **repaired final vs v8x (the gate)** | **7000-7015** | **both** | **0-32-0** | **−36,766** | **~52k** |
| repaired vs subAB_m30b (context only) | 8000-8003 | both | 0-8-0 | −129,630 | ~36k |
| MLP vs no-MLP head-to-head | 7000-7007 | both | 3-13-0 | −5,588 | — |
| v8x vs v8x (sanity) | 7000-7005 | both | 3-3-6 | +20 | — |

Net repair lift: ~37k → ~52k (**+40% absolute**) with zero wins. v8x sits at
~90k on these seeds; subAB_m30b ~164k. The conditional m30b gate (≥50% vs
v8x) was **not earned** — the 4-seed row above is context, not a gate.
Per the timebox rule (gates far below v8x after the top repairs → stop and
write the diagnosis), this document is the deliverable.

Every game DONE, zero errors, ~2 s/episode after the MLP was removed (the MLP
+BFS scoring cost ~90 s/episode).

## 2. When the clone falls behind (instrumented)

`probe.py` on seed 8001, per-day dump of money / hands / plants-by-crop /
animals / shed for both players:

- **d0-d2**: comparable money (~0-3k both, both spend down), but v8x buys
  land+animals+seeds; the clone buys hires+seeds and *some* structures.
- **d2-d9 (divergence window)**: clone is cashless (< $500) with idle hands —
  80-170 `PASS` actions/day logged in `probe2.py` histograms, movement
  dominating the rest. v8x already has animals producing and a 2-3× crop
  footprint. The clone's plant count stays in single digits.
- **d10-d20**: clone's first sell wave lands (melon opener + strawberry) but
  ~4-6 days behind v8x's compounding; shed periodically hits the 100 cap in
  the original (forced discard) — fixed in the repair via 12-unit sell chunks.
- **d20-30**: both saturated; gap is already baked. Clone finishes ~50-60k vs
  v8x ~85-118k.

Falling-behind order of subsystems: **economy first (d0-9 cash starvation),
then planting throughput, then animals.** Selling is a real bug but only the
4th-largest lever — fixing the drain alone did not close the gap.

## 3. Ranked root causes

### 3.1 Planting starvation — dispatcher early-return (largest single bug)
`clone_dsm_bc.py` builds `plant_jobs` *after* the main `if jobs:` dispatch
block that always returns when any WATER/FEED/HARVEST/DIG exists. With weeds
spawning at 0.005/tile/day and watering queued daily, `jobs` is ~never empty
→ planting code was effectively dead. Probe confirmed `plant_days` counters
barely moved; the agent sat on seeds it had paid for. **This is the "half the
score" headline bug.** Fix: plant jobs merged into the central queue as
`(x,y,"PLANT",crop)` tuples; dispatch emits `["PLANT",crop]` on arrival.

### 3.2 Sell drain too weak (SELL ×3)
Original sold ≤4 orders × ~3 units ≈ 12 units/day while producing far more;
shed filled to the 100 cap (end-of-day discard burned goods) and the season
ended in a glut-price dump (premium goods → $1 floor at high market
inventory). Fix: sell up to 12/order, drain each product every turn, large
end-of-season dump, wheat gated by feed reserve (`herd_n*2+8`), fertilizer
never sold.

### 3.3 Hire cost accounting `money -= 12`
Engine charges Fibonacci per hire: n-th hire costs fib(n+1) → 1,1,2,3,5,8,13,
21,34,55,89. 11 hires = 232, not 132. Systematic under-budgeting meant later
market orders silently failed. Fix: `_FIB` table, exact cost subtracted at
plan time.

### 3.4 Herd/structure desync + structure-kind starvation
HERD_PLAN bought animals on calendar windows regardless of free structures →
probes found 5-6 cows/geese parked in the shed earning $0 (and at 100-cap
risk). Worse, the structure chooser was `next(k for k in STRUCT ...)` over
dict insertion order → COOP always first → coops built to plan while pastures
starved → cows permanently parked. Fix: demand-driven builds (build only
when `herd_in_shed + inbound > free capacity`), animals only bought when a
free matching structure exists, shed-parked animals fetched by idle units,
BUILD jobs in the URGENT set.

### 3.5 MLP dispatch actively harmful
Head-to-head: MLP scorer 3-13 vs nearest-urgent dispatcher (−5.6k avg), and
~45× slower per episode. The learned 31-way scorer ranks jobs by
`z[class] − 0.6·manhattan`, but the class priors learned from BC tapes reward
the wrong thing locally (e.g. deprioritizing builds). Fix: deleted — pure
nearest-urgent dispatch over a dedup'd job list; urgent set =
{WATER,FEED,HARVEST,DIG,CARE,BUILD_*}.

### 3.6 Land timing / planting area
Original land buys gated by `money < 500+600` + a large barn reservation →
too few crop tiles early; probes showed large PASS+move counts days 2-9.
Fix: buy land whenever `money > land_cost + small reserve`, tightened BARN
footprint, planted earlier.

### 3.7 Structure overbuilding
STRUCT_PLAN targeted up to 23-24 pastures on a ~16-animal practical herd —
burning prime NW crop tiles and build labor. Fix: demand-driven builds only,
compact barn region, ≤3 build jobs/day.

### 3.8 Crop schedule
Melon opener (d0-2) restored as bridge capital — worth ~+3-5k alone on
seed 8001. Strawberry double-share d2-16, carrot filler, tomato d6-26,
wheat = herd feed + residual. Window tuning moved ±3-5k, never decisive.

### 3.9 Harvest batching
Ongoing crops now dispatch HARVEST at `yield>=3` (cap 4) instead of `>0`, and
decaying tiles (`max_lifespan_step` passed, yield draining) harvest at any
yield. Animal HARVEST likewise ≥3. ~0 measured score change; kept — halves
harvest trips in principle.

### 3.10 Remaining gap = scheduler density + adaptive economy
Even fully repaired, the clone averages ~5 useful ops/unit-hour vs v8x ~10:
one global job queue, manhattan dispatch, no zone partition, no
carry-batching, no momentum/commitment (mmpq decode showed the same family
weakness in real agents). And the plan is a **fixed table** — it cannot
react to seed-to-seed price/shop variance the way v8x's adaptive market does.
This is the irreducible ~40%: closing it needs a scheduler/economy rewrite,
not clone repair. Stopped here per the timebox.

## 4. Changes in clone_dsm_bc2.py (vs clone_dsm_bc.py)

1. MLP + BFS feature machinery deleted; nearest-urgent job dispatcher.
2. Plant jobs merged into the central queue (the §3.1 fix).
3. `_FIB` hire accounting.
4. Sell drain: 12-unit chunks, per-product every turn, wheat feed reserve,
   fertilizer held, big end-of-season dump.
5. Animals: buy only with free matching structure; shed-parked fetch errands;
   demand-driven builds; BUILD in URGENT.
6. Land: buy when `money > land_cost + reserve`; tighter barn.
7. CROP_PLAN: melon opener d0-2, strawberry d2-16 ×2 share, carrot/tomato
   filler, wheat-to-herd feed target.
8. Harvest thresholds ≥3 for ongoing yields (any yield if decaying).

## 5. Verdict

The clone was losing on **two stacked causes**: (a) a dispatcher bug that
starved planting outright — the single biggest defect — plus a cluster of
accounting/scheduling bugs (sell drain, hire costs, herd/structure desync,
MLP harm) worth another ~10-15k together; (b) an architectural deficit —
plan-table economy + zone-less transit-bound dispatch — that caps it around
~55% of v8x no matter how the tables are tuned. Repair took it 37k→52k;
matching v8x needs the mmpq/prog-class scheduler, which is a different lane.
