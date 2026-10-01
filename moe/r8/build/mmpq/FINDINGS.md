# MMPQ deep decode — diff vs DSM (mmpq lane, 09-30)

## Data
- **rawkeep episodes with MMPQ: only 4** (not ~38 as briefed): `109508082` (vs
  SpaTaro, W +225), `109763722` (vs SpaTaro, W +7547), `111099760` (vs **DSM**, W +7082 —
  a same-seed head-to-head!), `111414755` (vs THIRD FARM CLUB, L −1310).
  MMPQ is seat 0 in all four; both seats' `private` is populated every step.
- `bc2s_MMPQ.jsonl` = 26.8k unit-turn rows = exactly these 4 eps.
- `mine/top10/`: 450 MMPQ tapes (issued actions only), 09-23..09-26.
- **Replay semantics: `steps[t].observation` is POST-action[t]** — verified:
  act[3] PICKUPs already absent from obs[3].shed. (bc_extract-style pairing
  obs[t]→act[t] therefore leaks; obs[t-1]→act[t] is causal — consistent with the
  09-30b leak finding.)
- Evidence caveat: n=4 obs eps, and they contain **two behavioural variants** —
  early eps (109508082/109763722) issue modest-qty orders in an h1 burst and run
  coops/geese; late eps (111099760/111414755) issue aspirational qty-25 spam at
  all hours and never build coops. Numbers below are pooled; variant splits noted.

## 1. EXECUTED program (obs deltas; `exec_MMPQ.json`, `prog_mmpq.py`)

| dim | MMPQ executed (4 eps) | DSM executed (programs.json) |
|---|---|---|
| hires/day | 4.2→peak 11.5 d18-22 →9-10 tail | 4→10.5 d1 spike →11 flat |
| land | **NE@d5 ×4/4, SW@d8-9 ×4/4, SE d15-18 in only 2/4** | d5,d6,d9 (all three, fixed) |
| pastures built | 16.8/ep | (n/a — herd C10.9) |
| coops built | 3.8/ep (11,4,0,0 — variant-dependent) | ~ |
| animals placed | COW 8.0, SHEEP 8.8, GOOSE 3.8 | COW 10.9, SHEEP 5.7, GOOSE 1.9 |
| placed-day window | COW d0-10, SHEEP d0-17, GOOSE d2-10 | COW d0-18, SHEEP d0-21, GOOSE d6-11 |
| animal fills=bought | COW 7.5, SHEEP 8.5, GOOSE 4.8 (≈placed 1:1) | — |
| plants/ep | WHEAT 155.8, CARROT 71.8, STRAWBERRY 33.8, MELON 13.2, TOMATO 10.2 | W165.7, C51.1, S30.4, M13.2, T11.2 |
| plant windows | wheat d0-27, **carrot d0-27 (starts d0!)**, straw d1-16, melon d0-1, **tomato d15-19 only (late wave)** | wheat d0-28, carrot d6-27, straw d2-18, melon d0-2, tomato d6-27 |
| sells (executed units/ep) | WHEAT 449, STRAW 231, CARROT 207, FERT 181, EGG 181, MILK 159, WOOL 157, TOM 131, MELON 80 | W583, M355, STRAW360, T268, C301, WO246, E226, F278 |
| BUY_PRODUCT fills | WHEAT ~66-115/ep (feed buyback), FERT ~20-60 | — |

Issued-vs-executed: HIRE issued ~267/ep vs ~265 hired total (≈fills); seeds issued
≈ seeds planted 1:1 (e.g. ep109508082 issued W124/C66/M18/S33/T13 → planted
exactly that). The HANDOFF "seeds/ep W188/S40/M12/C41/T2" was an issued-order
estimate from the 450 tapes; executed planting is W156/S34/M13/C72/T10.

Other executed facts:
- Money curve (means): d0 ≈ $90-180 left, **d5 ~$63-490** (near-zero bank —
  everything reinvested), d10 ~$3-13k, d15 ~$11-44k, end $91-135k.
- Animal escapes (unfed 2d → gone): COW 3.5, SHEEP 8.0, GOOSE 1.0 per ep —
  MMPQ lets ~12 animals/ep die from neglect. Sloppy mid-game coverage.
- Shed hits the 100-cap (3/4 eps) → EOD discards do occur.
- Dismissed hands auto-deposit inventory into shed at day rollover (observed:
  hand carrying MILK×3 at h23 → shed MILK+3 at h0). Also the farmer's
  inventory persists.

## 2. Dispatch (`dispatch_mmpq.py` on the 4 eps; DSM numbers = HANDOFF 09-29g..j)

| probe | MMPQ | DSM |
|---|---|---|
| same-tile consec work pairs | **48.0%** (13,954 pairs; gap hist: d0=48%, d1=33%, d2=9%) | 51.7% |
| move→nearest-pending-job | **94-95%** (11,001 move rows) | 91.9% |
| momentum tie-break on equidistant dirs | **22.9%** ≈ chance | 60.6% |
| fixed dir priority (NWES/NESW/x-first/scan) | all ~26-35%, none explains | — |
| territory | homes all near shed (3,3)-(5,5); R4 52-87%, weak partition | strong partition (ui5 N-band, ui2 S, ui6 W, ui1 E), 80% R4 |
| mission persistence | run len: 68% len1, 19% len2; for len≥3 only **1%** arrive at the move-1 nearest tile; consecutive nearest-set overlap within runs 53:3670 — **retargets every step** | "committed missions" per 09-29e/j interpretation |
| op mix (/ep) | WATER 1222, HARVEST 479, CFERT 374, PLANT 293, FEED 303, CARE 285, FERT 214, DIG 31, PASS 157; moves 2757 | (ep111099760 same-seed) WATER 1389, HARVEST 517, CFERT 366, PLANT 284, FEED 286, CARE 298, FERT 190, DIG 39, PASS 49; moves 3441 |
| hand spawn | hands appear at shed ring: (4,4),(5,4),(4,5),(4,3),(3,4)... | — |

Reading: **MMPQ dispatch ≈ same greedy walker family as DSM** (stay-finish +
step-to-nearest), but pure per-turn re-evaluation — no momentum, weak/no fixed
territories (hands spawn at the shed each day and re-diffuse). MMPQ is *slightly
tighter* (95% vs 92% nearest-agreement, −14% moves for the same work count) but
Pass's more (157 vs 49/ep idle) — it tolerates idle units.

## 3. Market template

| feature | MMPQ | DSM (09-29c) |
|---|---|---|
| HIRE | ~267 orders/ep, qty 1, spammed h0 (749/1069) & h1 (310/1069) — issue-every-slot until cap reached | HIRE×k(day)@h0 single stack, ramp 4→11 |
| BUY_ANIMAL | early variant: h1 burst, qty 1-5; late variant: qty-25 aspirational spam h0-h10 + h21-23, COW order days {0-3,6-9} | COW n=1 every ~2h d6-18 affordability-only, GOOSE d6 |
| BUY_SEED | continuous trickle small qty (med 1-6); WHEAT seeds bought all game | trickle |
| BUY_PRODUCT | WHEAT 66-115 + FERT 20-60 per ep — deliberate feed/fert buyback | — |
| BUY_LAND | issued ~3-14/ep, executed NE d5 + SW d8-9 always, SE only when rich (d15-18, 2/4) | LAND d6+d9 fixed |
| SELL | 50-90 orders/ep, small batches (med qty 3-9), hours peak h0-1 & h21-23 (morning+evening dump); price-percentile-at-sale ≈ 33-55% → **sells through dips too, NOT price-gated** (earlier sell-vs-hold contrast was reverse-causality noise) | standing SELL ~3×7 products every turn, through dips (milk@97 vs 169) |
| orders/turn | mean 1.03, mode 0-2, bursts to 10 at h0 | standing ~4-10 |

## 4. Same-seed head-to-head (ep111099760, MMPQ 111980 vs DSM 104898)

| | MMPQ | DSM |
|---|---|---|
| hires | 4→11 peak, 9-10 tail | 4→11 flat |
| land | NE d5, SW d8 (SE never) | NE d6, SW d9 (SE never) |
| herd placed | C7 S10 (d0-9) | C8 S9 (d0-9) |
| crops | W167 C84 S31 M9 (carrot d10+, straw d1-15) | W176 C48 S24 M12 T20 |
| money | 2 / 63 / 13011 / 43568 / 85808 @d0/5/10/15/25 | 7 / 624 / 5364 / 33316 / 77343 |
| unit work ops | 4014 | 4144 (−3%) |
| unit moves | 2945 | 3441 (**−14%**) |
| PASS | 128 | 49 |

MMPQ wins by compounding: poorer through d5 (spends everything), ~2.4× richer at
d10, out-sells DSM on milk (137 vs 122), wool (214 vs 173), carrot (258 vs 140),
strawberry (236 vs ~178), and does it with 14% less walking. Difference is
tempo and volume, not a different mechanism.

## 5. What likely makes MMPQ #1 (hypotheses, ranked by evidence)

1. **Same mechanism, denser/economic tuning** — dispatch family is identical
   (greedy nearest + stay-finish). MMPQ's edge is throughput: more crops planted
   (carrot 72 vs 51, strawberry 34 vs 30), earlier strawberry window (d1 vs d2),
   wheat feed-buyback loop (~100/ep), higher fertilizer throughput (CFERT 374 +
   FERTILIZE 214/ep), more hands at peak (11.5 vs 11). Evidence: strong (4 obs
   eps + h2h).
2. **Aggressive day-0 capex** — bank to ~$2-5 by d1 (animals + melon + hires
   immediately), land NE@d5 reliably 1d before DSM. Compounds into the ~2×
   mid-game money lead seen in the h2h. Evidence: strong (all 4 eps + h2h).
3. **Order-spam = implicit priority queue** — aspirational qty-25 BUY_ANIMAL and
   per-slot HIRE spam let the engine's affordability cap implement "buy whenever
   possible" without internal bookkeeping; executed program is then purely
   liquidity-driven. Simpler to tune than DSM's fixed windows. Evidence: strong
   for late variant.
4. **No price-gated selling** — sells in small batches when stocked, dumps
   through dips just like DSM; not the edge. Falsified my earlier sell-vs-hold
   reading once percentiled within-episode.
5. **Variable goose/coop + tomato-late-wave modules** that switch per variant —
   probably shop-demand-conditioned (ep1 heavy EGG demand → 11 geese; eps 3-4
   no brunch-heavy demand → 0 coops, though they still issued goose orders that
   never filled on money). Evidence: suggestive (n=4, confounded by version).
6. **Animal churn tolerance** — ~12 escapes/ep and shed-cap discards; MMPQ runs
   hot (over-buys relative to service capacity). Not an edge per se — shows the
   strategy is robust to execution slack. Evidence: direct.

## 6. Clone implications
- The dispatch spec to copy: stay-finish (~48%) → step-to-nearest-pending-job
  (~95%) → **no momentum; tie-break near-uniform** (use rng or scan order) →
  territories are just spawn-at-shed diffusion (don't hardcode zones).
- Program table: hires 4,2-3,3-5,5,5.5,5.2,6.2,8.2,8.8,9.2,10.5,9,9.8,9.5,9.5,11,
  10.2,10.8,11.5,10.8,10.5,11,11.2,10.2,11,10.5,10.5,10,9,9.2; land NE@5 SW@8
  (SE only if cash); herd C8/S9/G0-11 (goose module optional); crops W156 C72
  S34 M13 T10 with carrot@d0 & tomato wave d15-19.
- Market: spam-style; HIRE every free slot at h0-1; BUY_ANIMAL aspirational;
  small-batch SELLs when stocked (no price gate needed to match MMPQ).
- Gap to close vs m30b-family: MMPQ's remaining unexplained dispatch residual is
  ~5%, smaller than DSM's ~8%.
