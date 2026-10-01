# MoE r8 THREAD — top-2 clone build

**devin (orchestrator), 08:00 UTC** — Round seeded. Lanes: resim / clonefix / prog / mmpq.
Live pair [v8x, m30b] untouched; 3 upload slots held; deadline 18:00 UTC.
Resim verified deterministic in-process (all 8 shop draws reproduce); only the
action-application detail diverges. If resim cracks, MMPQ training data goes
38 eps → 450 eps.

## resim — CRACKED: replay re-simulation is EXACT; 7.29M bc rows extracted

Root cause of the orchestrator's divergence (ep 112219779 [101218,46823] vs
[107468,104194]): the driver applied `actions[s]` at game-step s. Replays store
`steps[t].action` = action that produced `steps[t].obs` (submitted at t-1);
`actions[0]` = PASS placeholder. Correct replay = `actions[s+1]` at step s
(tapefidelity's shift=1 / replayaudit's `obs.step+1`). With shift=1 the stock
pip interpreter (kaggle_environments 1.32.7) reproduces everything — no version
skew, no action normalization. 719 calls (steps 0-718; DONE at >= episodeSteps-2).

Match rate (final money, to the dollar): rawkeep MMPQ 4/4, top10 random 120/120,
MMPQ full run 450/450, DSM full run 554/554 = **1128/1128 exact (100%)**.

Deliverables in `moe/r8/build/resim/`:
- `resim.py` (driver w/ pre_step+on_step hooks, impossible-op checker),
  `bisect_ep.py` (field diff vs full replay), `validate.py`, `extract_bc.py`.
- `bc2r_MMPQ.jsonl` 3,213,581 rows / 450 eps; `bc2r_DSM.jsonl` 4,075,068 rows /
  554 eps — exact bc_extract_team schema {ep,t,ui,xy,d,dshed,inv,on,G,y,y2},
  causal pairing S_{t-1}->action[t]. Per-ep fidelity in `*.manifest.json`.
- Caveat: recorded per-step `observation` in replay JSONs is the shared mutable
  dict (all steps show terminal state) — only actions/rewards are per-step;
  money+shop cross-check is the fidelity signal.
- `find_impossible` fires in ~96% of exact eps (agents emit no-op PLANT/PICKUP/
  WATER ops) — benign; meaningful only on non-exact eps (none seen).

## devin (orchestrator) — prog result verified + staged

Independently re-gated v8prog hh on fresh seeds 9100-9109 x2 seats:
**20-0 vs v8x, +19.7k, zero errors.** Baked config into `agents/v8hh.py`
(no env vars on Kaggle) — staged as family-slot candidate once live pair
converges and a slot frees. m30b remains the local ceiling (hh 0-24 vs it).
MMPQ dispatcher train running on bc2r_MMPQ (3.2M rows) for clone_mmpq.

## mmpq — MMPQ deep decode done (4 obs eps only, not ~38)

Deliverables: `build/mmpq/FINDINGS.md`, `programs_MMPQ.json`, `exec_MMPQ.json`,
`prog_mmpq.py`, `dispatch_mmpq.py`, `walkrows_MMPQ.jsonl`.

- **Corpus correction**: only 4 rawkeep eps contain MMPQ (109508082/109763722/
  111099760/111414755), all seat0 w/ full private obs every step — incl. a
  same-seed MMPQ-vs-DSM game (111099760, +7082). bc2s_MMPQ = exactly these 4.
- **Replay semantics verified**: `steps[t].observation` is POST-action[t]
  (act[t] pickups absent from obs[t].shed). Causal pairing = obs[t-1]→act[t].
  Also: dismissed hands auto-deposit inventory to shed at day rollover; farmers
  keep inv; shed 100-cap discard real (3/4 eps hit it).
- **EXECUTED program** (tile/obs deltas, all 4 eps): hires 4.2→11.5 peak→9-10
  (vs issued 4.7→11.7); land NE@d5 ×4, SW@d8-9 ×4, SE only 2/4 (d15-18) — cash-
  gated, not scheduled; herd C8.0/S8.8/G3.8 placed d0-10 (G=0 in the 2 late
  eps); crops W156/C72/S34/M13/T10, windows: wheat d0-27, carrot d0-27, straw
  d1-16, melon d0-1, tomato ONLY d15-19 late wave; sells executed W449/S231/
  C207/F181/E181/MILK159/WO157/T131/M80 per ep; BUY_PRODUCT wheat ~66-115/ep.
- **Dispatch** (26.8k unit-turns): same family as DSM — stay-finish 48.0%
  (DSM 51.7%), step-to-nearest-job 94-95% (DSM 91.9%) — but NO momentum
  (22.9% vs DSM 60.6%), weak territories (homes all near shed; hands spawn on
  shed ring and re-diffuse daily), and mission-commitment probe says pure
  per-turn retargeting (len≥3 runs arrive at move-1 nearest tile only 1%;
  nearest-set overlap within runs 53:3670). Residual ~5%.
- **Market**: order-SPAM confirmed — HIRE qty1 every free slot h0-1 (~267/ep),
  late-variant BUY_ANIMAL qty-25 aspirational (engine affordability = the cap;
  COW order days 0-3+6-9), SELL small batches med 3-9 at h0-1 & h21-23. Sell
  price-percentile ~33-55% → sells THROUGH dips like DSM (earlier sell-vs-hold
  price contrast = reverse causality; corrected).
- **h2h vs DSM (same seed)**: money 2/63/13k/43.6k/85.8k vs 7/624/5.4k/33.3k/
  77.3k @d0/5/10/15/25 — MMPQ spends to ~$0 d0-1 then compounds ~2.4× mid-game;
  −14% moves for −3% work-ops; PASS ×2.6 (128 vs 49) — tolerates idle.
- **Two MMPQ variants in obs data**: early (eps 1-2: h1-burst small-qty orders,
  coops+geese live) vs late (eps 3-4: qty-25 spam all-hours, zero coops, goose
  orders unfilled on money). Both beat their opponent; late variant = the
  ~3115-rated one most likely.
- **Ranked edge hypotheses** in FINDINGS.md §5: (1) denser economic program
  (carrot+strawberry volume, feed-buyback, fert loop, 11.5-hand peak), (2)
  all-in d0 capex + NE@d5 one day earlier, (3) spam-order = free priority
  queue. Center-tile pastures are NOT MMPQ-unique (DSM/TFC/SpaTaro all do it).

## clonefix — clone_dsm_bc diagnosed + repaired; still 0-32 vs v8x; diagnosis is the deliverable

Deliverables: `build/clonefix/clone_dsm_bc2.py` (repaired agent),
`build/clonefix/FINDINGS.md` (full writeup), `probe.py`/`probe2.py`/`gate.py`
(instrumentation), `clone_nomlp.py` (ablation reference).

- **Gates** (paired seats, W-L-T from clone's side): original vs v8x
  7000-7007 = 0-16, −54.8k avg margin (~37k). Repaired vs v8x **7000-7015 =
  0-32, −36.8k (~52k)**. Repaired vs subAB_m30b 8000-8003 = 0-8, −129.6k
  (~36k vs ~164k). Conditional m30b gate not earned (needed >=50% vs v8x).
  Net lift +40% absolute, zero wins; ~2s/ep, zero errors.
- **Root causes ranked** (details in FINDINGS.md): (1) dispatcher early-return
  made the plant-job path dead code — planting starved, the headline bug;
  (2) SELL x3 drain vs production → shed 100-cap discard + glut-price dumps;
  (3) `money -= 12` hire accounting vs real Fibonacci (11 hires = 232);
  (4) herd/structure desync — animals bought with no free structure parked in
  shed, and `next(k for k in STRUCT)` dict-order always built COOP first so
  pastures starved; (5) MLP job scorer harmful — 3-13 vs nearest-urgent h2h
  (−5.6k) and 45x slower; (6) land-timing/barn over-reservation starved crop
  tiles d2-9; (7) structure overbuild (24 pastures for ~16 animals); (8) crop
  window tuning +/-3-5k, not decisive.
- **Divergence window** (probe.py, seed 8001): clone cashless with 80-170
  PASS/day d2-9 while v8x already compounds animals+crops; first sell wave
  lands d10+ but ~4-6 days late; gap baked by d20.
- **Residual ~40% gap = architecture**: fixed plan-table economy + zone-less
  global-queue transit-bound dispatch (~5 vs ~10 useful ops/unit-hr). Not
  closable by table repair — needs the prog/mmpq-class scheduler. Stopped per
  timebox.

## prog

**devin (prog lane), ~12:30 UTC** — `build/prog/v8prog.py` shipped: v8x + PROG
config layer (per-subsystem scheduled/reactive flags, `V8PROG` env override).
Tables: HIRE_TABLE 4,4,6,6,6,6,8,9,9,10,11x18,10,10 | LAND d5 NE/d7 SW/(d9 SE) |
HERD_PLAN cumulative windows (C2+9+3, S3+5+3, G4) | CROP_PLAN tile floors.

Ablation vs v8x, seeds 6200-6207 x2 seats: hire-only 16-0 **+22.2k**;
herd-only 12-4 **+11.5k**; crop-only 4-12 −6.7k; land4-only 4-12 −8.2k;
all-sched 8-8 −2.1k. Combos: hh (hire+herd) 14-2 **+27.7k**; hhc 16-0 +23.9k;
+sched-land collapses to +6.5k/+1.3k; wheat_fill −6.5k margin; herd-first neutral.

**Gate vs v8x (fresh 7100-7119 x2): hh 40-0, +27.5k** (hhc 35-5 +17.2k).
**Gate vs subAB_m30b (8000-8023 x2): hh 0-48, −84.7k** vs v8x baseline 0-24
−110.1k — closes ~25k of the family gap, zero wins. Family cap stands;
promotion bar not met.

Verdict: the decoded program is REAL for labor+livestock (reactive v8x
under-hires and under-herds vs the tuned schedule) but FALSE for land+crops
(ROI-checked buys beat calendar days; value-scored planting beats committed
floors). Full tables in `build/prog/FINDINGS.md`. Default config = hh.
