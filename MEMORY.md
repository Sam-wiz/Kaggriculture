# Memory — durable learnings for Kaggriculture

Consolidated from HANDOFF.md timeline. Append-only facts that survive context loss.

## Evaluation mechanics (staff-confirmed)

- Final ranking = **single Bradley-Terry tournament** over episodes between agents
  still active at the 09-30 deadline (María Cruz). Submissions keep playing ~2 weeks
  post-deadline before the fit.
- **Team score = better of the two active submissions**; a team can't occupy two ranks.
  The second slot is a hedge with literally no downside (Addison Howard).
- **Ties = half a win each** in the BT fit.
- Game parameters (MARKET_I0=10000, PRICE_FLOOR=1, etc.) are fixed for final eval.
- Unanswered publicly: whether the BT fit uses only post-deadline episodes or all
  history between deadline-active agents; whether ratings reset to 600 (community
  claims yes; Orbit Wars precedent says no — either way it doesn't change strategy).

## Public vs private leaderboard — the real difference

- Public = path-dependent Elo ladder: starts ~600, ~72h/100 games to converge,
  matchmaking is rating-local, position depends on trajectory and clone density.
- Private = one global pairwise fit. **Margin is invisible to BT** — a −46k loss
  costs exactly a −1 loss. Only P(win) per pairing matters.
- Optimize for private: maximize win probability vs the *post-deadline* field
  (stronger than today's ladder — documented hoarding), convert ties (each = +0.5),
  eliminate systematic loss classes, keep both slots on different lineages.

## Engine truths (verified in source)

- Market resolves **per-unit lockstep**, both players quoted at the same pre-commit
  inventory each iteration; a failed unit aborts that order only. Sells must precede
  the buys they fund in the same turn's order list.
- **Weeds + shop draws share one RNG stream** (one draw per empty tile, both farms,
  then shop draw). Any change to our actions reshuffles the world — measured deltas
  between variants are partly shop-draw luck; decide only on paired seeds, n≥16.
- obs['step'] is absent for seat 1 in *serialized* observations; live dispatch
  restores it. Derive via `day*24+hour` anyway (free insurance).
- Replay `actions[i]` answers obs at `steps[i+1]` — off-by-one otherwise.
- FERTILIZER drains nowhere (no shop/town demand); melon demand = 30/season
  (town center only) — the all-melon opening is a trap; hinge-curve products
  (tomato/carrot) run away when demand exists.

## Agent lessons

- **Tape+wrapper beats pure tape** (~88% score recovery for raw replay).
- **Dormant flags are the cheapest wins**: pipe16's `clamp_sells:False` was its only
  public counter hole (2802/melon/reactv7 −8k..−13k → wins). Metav4's embedded
  executor had the same flag off.
- **Oversell desync is the recurring bug class**: SELL qty > shed stock → failed
  units → funding desync → dead buys → escapes. Fix = clamp to projected shed.
  BUT hard-clamp on metav4 breaks melon-squeeze catastrophically (0-32) via the
  shop-RNG reshuffle — slack=50 (`projected+50`) threads it: trims only absurd
  overshoots (SELL FERTILIZER 997), keeps anticipatory pressure.
- **Premium-sell overlay (Ritwik Raha)**: append SELLs for MILK/WOOL/STRAWBERRY/
  MELON above floors 120/140/90/60 into free market slots from day 14, batch 15.
  Converts mirror ties → wins (live: 0 ties in 81 games vs pipe16's big tie cluster).
- **What wins live**: continuous staple conversion (sell wheat/fert as produced,
  don't hoard), shop-demand-matched herds, terminal liquidation.
- **What's uncounterable**: private runtime agents (Ebi, dauriel, tetsuya team) —
  outfarm by conversion efficiency, not exploits.

## Active pair (submitted 09-21 late, refs 56416380/56416374)

- `subOb_pipe16prem.py` (ref 56416380) = subO with prem floors -20% — pipe16 +
  clamp_sells + prem overlay. Beats pipe16 14-2, subM 25-5; sweeps all public
  counters. Live: 0 ties in first 81 games (prem converts mirror ties).
- `subP_metav4prem.py` (ref 56416179) — metav4 + slack-clamp(50) + step-guard +
  prem overlay. Strictly dominates subN on every paired cell: 25-7 vs subN
  mirror, flips koshinm 6-10→10-6, holds melon/v8/v48/pipe7/2802/reactv7
  (16-0..15-1 each), 14-2 vs 2945, 16-0 god/boatlee, 2-14 vs subO.
- `subP2_metav4prem.py` (ref 56416374) = subP with prem floors -20%:
  16-2 vs subP mirror, melon 16-0, v8 12-4 held.
  (subN 56407594 retired; prem overlay ports verbatim to mv4 chassis —
  the mirror-band was its biggest residual live loss class: 12/21 losses.)

**Submission mechanics**: only the latest 2 stay active — any new submission
retires the older one. To change one slot, the pair must be re-shipped together
or the surviving slot re-submitted after. 5/day limit.

## Process lesson (09-21)

- Burned 4 submissions in 2 rapid rotations ([subO',subP] then [subOb,subP2])
  when one rotation sufficed — submitted intermediate results before the local
  iteration was finished. Rule: complete the full improvement cycle locally,
  THEN do a single rotation with explicit per-file approval.
- Public rating churn is cosmetic for final BT (post-deadline refit over
  final-active agents), but only while runway >> 72h convergence. Near the
  deadline, an unconverged agent draws a weak eval pool — then it matters.

## Top-tier reverse engineering (09-21 deep dive)

Data: `mine/top/` ~550 reduced replays (actions+rewards), `mine/rawtop/` ~21
full-obs replays, `meta/` georgymamarin episodes dataset (202k episodes,
per-seat fingerprints). Fetch: `mine/fetch_any.py` (per-sub episodes).

**Top-11 (DSM 3115, Majkel 3104, Vadim, UMG, ymg_aq, 3RD FARM, mtmr_s1,
OtterVibe, KawattaTaido, SpaTaro, QQ) are ALL private reactive policies** —
~50% per-step action consistency across seeds (scripted day-0 opening ~90-100%
identical, then adaptive). Not tape-clonable.

**Shared skeleton (all of them)**: day-0 HIRE×4 + COW×2 + SHEEP×2-3 + melon
seeds ~6 + wheat ~7-10 + feed-buy wheat; BUY_LAND NE day5-6 ($1k) then SW
day9-11 ($2k), **SE ($4k) NEVER bought**; hires front-loaded hour 1-2 ramping
to ~11/day plateau, ~280-310 total; ~10 cows / 6-8 sheep / 2-3 geese avg;
~12 melons day0-2; strawberry planted day2 → shed day13; wheat 3-day replant
ramping to ~35-38 tiles; carrot day-11+/23+ filler; structures hug shed
(dist≤2). Hands ~1% PASS idle.

**Sell engine**: "ride the town drain" — shops consume at steps t≡1 mod4
(hours 1,5,9,13,17,21), town center t≡1 mod24. 60-70% of premium sell
*events* land post-drain (but only ~10% of volume — lots are 1-3 units).
Price-agnostic (sell local max, even into glut). Wheat = feed buffer:
sell surplus >~28, restock <~10. Endgame dump-all last ~6-24 turns.
DSM avg bank 110k/132g, Majkel 105k/142g, UMG 118k/15g — mid-field
"Planned Economy"/"Sida Zuo" avg HIGHER (126-127k). Dump-all clones
bank 115-158k single games — variance dominates single games.

**Our deltas vs spec**: cows 6-8 vs 10 (v231 sheep→cow converter is
guard-blocked: no_stock fails since tape keeps placement backlog),
strawberry seeds day5 vs day2, hand idle 7-10% vs 1%, sheep 9-11 vs 6-8.

**FAILED ports (all tested, all dead ends)**:
- Additive cow buys: never placed (tape placement is plan-bound), -400/game
- v231 window/cap/guard widening: converts ≤1-2 animals, ±$500 noise
- Early strawberry seed buys: tape plants on fixed schedule anyway
- Tick-gated prem overlay: 2-12 loss (shrinks already-small overlay)
- Replacement sell engine (drop premium sells off-tick): 0-16 catastrophe —
  tape's sells fund same-turn buys in list order, removal starves the plan
- The tape is plan-bound end-to-end; only additive market ops are safe.

**Working lever**: prem floor lowering is still paying — floors -40%
(subV_a) beat subOb 8-0-4 +609, floors -70% (subV_f) 10-2 +599 in mirror.
Field coverage check pending (must verify dumping premium cheap doesn't
lose vs clones).

**Honest ceiling assessment**: our economy ≈ top-tier avg (~104-112k
contested vs DSM's 110k); the 300pt rating gap is win-rate vs shared field
+ the fact top agents are unmeasurable private reactive policies. Any
further gain needs deep planner surgery (multi-day, unvalidatable) or is
whisker-scale tuning.

## Pending rotation (09-21 evening)

- Submitted `subV2_mvprem.py` ref **56439429** (17:15) — mv4 chassis, prem
  floors -40% (MILK72/WOOL84/STRAW54/MELON36). Active pair: [subOb 56416380,
  subV2 56439429].
- **TODO tomorrow (daily quota reset)**: submit `subV_a.py` (pipe16 chassis,
  same -40% floors) → retires subOb → final pair [subV2, subV_a].
- Evidence: subV_a 30-2/+733 vs subK clone, 8-0-4/+609 vs subOb, 32-0 melon,
  32-0 v8, 16-0 all public rivals; subV2 28-4/+655 vs subL, 20-10-2/+228
  vs subP2. Both DONE both seats official env.
- Counter-evidence logged: floors -70% (subV_f) LOSES vs subK clone
  (22-10 vs subOb's 26-6) — the mirror gain was divergence artifact.
  -40% is the sweet spot.
- User authorized this rotation explicitly ("submit them").

## Rotation complete (09-22 ~11:50 IST)

- `subV_a.py` submitted → final active pair **[subV2 56439429, subV_a 56455434]**
  — subOb retired. Both run prem floors -40%.
- Quota is rolling-24h (yesterday's 04:29 cluster freed ~04:30 IST today).

## Deeper floors rotation (09-22 afternoon)

- Live loss profile: 50% win rate, all whiskers vs clone band — the field at
  ~2700 IS our own public lineage. Coin flips decided days 21-28 by sell timing.
- subV_f55b30d10 (floors -55%, batch 30, minday 10) > subV_a on every cell:
  mirror +222/+456, clone band 33-7, metav4 34-6. Sweeps all rivals 16-0.
- subV2_f55 (same overlay on mv4) > subV2 mirror 23-2-7 +276.
- Submitted both (56458085, 56458087). Prem-overlay floor curve swept:
  -25% loses, -40% good, -55% best, -62% slight decline, -70% overshoots.
- Failed this session: phase deferral, absorb-scaled lots, self-plan front_run.

## 2026-09-22 late — bracket trades measured dead; reconcile fix submitted

### Same-turn bracket trades (order-index lockstep): DEAD
Mechanism is real (sell@index0 / buyback@index9 taxes intervening opp sells,
~slope·B·q per event — exact math verified against interpreter's per-index
lockstep + post-buy-inventory quoting). But measured net-negative:
- v1 (fert50+wheat120): −24-25k everywhere. Bleed = float occupies ~50 shed
  slots all season → end-of-day overflow discards premium produce.
- v2 (fert30, room+floor+cash guards): −4.6k everywhere. Residual costs:
  float depreciation (buy ~$55 day10, liquidates ~$10 day28) + crowding.
- Tax base is thin vs clones: opp real fert sells ~200-400u/game (SELL 9999
  requests fill only real stock — market inv only +440 all game). Ceiling
  +2-4k vs heavy dumpers, ~0 vs clones. Costs eat it. MEASURED DEAD.
- Wheat leg alone: never fires (post-pickup shed wheat <80).
- Sell-order reordering: already same-index as opp (dead).
Files: subV_bkt.py subV_bkt2.py subV_bktf.py subV_bktw.py (all rejected).

### Own-sale reconcile fix: WORKS, submitted
Bug: _V9_RACE and _OR2 estimators record prev["own"] sells BEFORE the
outermost prem overlay appends its sells → next-turn market-inv deltas
attribute our overlay units to the rival → phantom rival dumps corrupt the
lead-horizon fit and _v92_p forecasts.
Fix: outermost reconcile rebuilds prev["own"]/["left"] (and OR2's prev["own"])
from the FINAL emitted market list, capped by projected shed.
Files: subV_f55rec.py (pipe16 chassis), subV2_f55rec.py (metav4 chassis).
Fresh-seed results (97..131, both seats):
- f55rec vs pipe16 14-2 +840 (V9-only rec) / 12-4 +722 (dual rec)
- f55rec vs metav4 14-2 +887 / 12-4 +768
- f55rec vs subV_a 10-6 +346; vs f55 8-2-6 +29
- subV2_f55rec vs metav4 12-4 +758, vs pipe16 12-4 +708, vs f55 6-2-8 +27
- weak-pool regression: 8-0 +99k vs m_staged
Submitted both (quota exhausted for the day).

### Other measurements this session
- Shed pegged 100 days 15-27 when float held → overflow discards are the
  dominant cost of any held-float scheme.
- Herd saturated at 17 animals, 0 empty pastures day 15+; SE quadrant bought
  day 19 and used (10 tiles). No capacity slack for additive animals.
- Day-29 liquidation already continuous (prem stock oscillates 0-22).
- Opp day-29 pattern (QQ农场 win): continuous dump-all every turn hours 14-23
  capturing post-drain prices; ours equivalent. No exploitable gap found.
- Live: f55 pair climbing (2394/2208), subV_a 2055, subV2 2405, subOb 2685.

## 2026-09-23 — third estimator + dead-op reclaim; quota is 5/day (confirmed hard)

### Third estimator fix
`_RACE_STATE["prev_action"]` (feeds `_race_lost`) was also recorded pre-prem-overlay.
Fixed same way (points at final emitted action). No measurable delta on the standard
block but strictly more correct; kept.

### Dead-op reclaim overlay (subV_f55rec.py, subV2_f55rec.py — on disk, NOT yet submitted)
Outermost pass, step>=240, swaps provably-dead unit ops IN PLACE (never movement —
positions stay tape-synced):
- CARE on animal whose next production lands day 30+ -> HARVEST (yield>0) /
  COLLECT_FERTILIZER (fert avail) / PASS
- FEED on already-fed animal -> same fallback chain
- PASS on animal-structure tile -> HARVEST / COLLECT_FERTILIZER
- shed-room guard: collection swaps only if shed+carried < 90 (decremented per swap)
Scope note: ~15 dead CAREs + ~100 redundant FEEDs + ~50 idle-on-animal-tile PASSes
per game in days 20-29. Carried items auto-drop to shed at end-of-day (engine line ~878)
so in-place collections are safe.

Results (seeds 97..131, both seats): f55rec 14-2 +725 / +776 vs pipe16/metav4;
f55rec2 14-2 +712 / +763. Mirror bank +54 (seed7) / +736 (seed42) vs reconcile-only.
Approx +18-20 margin over the submitted reconcile-only pair; consistent but small.

### Rejected this session (measured)
- Plant-tile reclaim swaps (WATER-past-maxyield->HARVEST/PASS, PASS->WATER): ~-8 avg
  across all cells vs animal-only. Mechanism: any plant-tile change alters weed-spawn
  RNG draws -> re-rolls shared shop sequence both players' routes key off.
- Generalized reclaim incl. plants without shed guard: -70..-100 (overflow discards).
- Last-hire suppression: last hand is busy 16-22/24 every day; never suppressible.
- Staple spike-selling (tomato/carrot hinge): shed stock ~0 — tape already sells at
  slot 0 the moment produce lands; tomato sells went 6hi/0lo already. Nothing to time.
- Confirmed exhausted sell-side: gates, phase-deferral, own-schedule front-run,
  absorption-scaled dumps, index reordering, fert bracket, staple spikes.

### Submission mechanics correction
Daily cap is REAL: exactly 5/day, hit at 13:27 today (rec pair 56465704/56465708 live,
converging 2144/1977). User's "no limit" is wrong — plan around 5/day, resets daily.
Leaderboard: top ~3116, top-10 ~2980s, #20 ~2916.

### State of play
Tape+overlay ceiling ≈ clone-band win rate; 3k needs the reactive-executor class
(production mix changes per shop draw — astra's "bounded daily continuation" is the
cheapest credible version: per dawn choose baseline vs one alternative crop cycle vs
one alternative animal buy, gated on feasibility+payback).

### Validation + forensics (late session)
- Fresh-seed block 200-223 (alternating seats, never tuned on): f55rec 20-4 +549
  vs pipe16, 20-4 +594 vs metav4; f55rec2 20-4 +403, 20-4 +461. Ship-ready.
- BUY_PRODUCT is NOT fixed price (AGENTS.md is wrong): quotes market_price(inv-1)
  per unit — buy/sell round-trip nets zero by design. No arb exists.
- Route internals: 41 tapes share prefix to step ~143, diverge PHYSICALLY at day 6
  (farmer+hands differ massively) — mid-game re-route = position desync, dead.
  Router picks at step144 from first-2-shops (EXP240 table / V39 yarn fallback /
  rival-fingerprint override route128). Day-27 forces route 2 (terminal).
- Market structure: all products sit below I0=10000 all game; spikes come from
  shop drains (t%4==0 consume). Tomato med66/p90-161, milk med32/p90-181,
  strawberry med144/p90-188. Our tape already sells slot-0 continuously and
  shed is ~0 — nothing left to re-time.
- Top-agent adaptivity proof (mine/top/*.json.gz): Majkel1337/SpaTaro/CropDusta
  emit a DIFFERENT day0-10 buy signature every episode (6/6 distinct); tape-lineage
  rivals emit identical (1/6). The 3k gap = per-draw production replanning, not
  sell timing. This architecture ceiling is real.
- Tape economics reference (route0): hires 5→11/day (fib cost ~232/day late),
  buys: cows day0-7, sheep day0/8/9, geese day10/11, strawberry days5-11,
  wheat daily, carrot days24-27, fert buys daily, land day6+11. Tail is already
  trimmed (no day28+ plantings; day27 wheat/carrot yields land day29, marginal-alive).

## 2026-09-23 — Rescue overlay autopsy + restore

**Rescue overlay (_rsc_agent): DEAD, reverted.** Designed to retry failed BUY_ANIMALs and convert dead ops into pickup/place. Bisect on seed42 mirror (subV2 chassis): ops-leg −14k, market-retry-leg −22k vs base. Root cause: "free structure now" ≠ "uncommitted structure" — retried buys landed animals in pastures earmarked for the tape's next scheduled placements → planned animals stranded in shed → production cascade. Also chained hire/buy retries drained build-phase cash (day10 money 1454 vs 16012). The tape is a tight choreography; inserting resources it didn't budget for breaks it. The −28k outlier loss it targeted is 1-in-120 — the fix cost more on normal games than it saved.

**Append footgun found:** `_rec_agent` was defined but NEVER assigned to `agent` — the rescue block captured `_prm_agent`, silently dropping the reconcile+reclaim. Rule: after appending any wrapper, grep the final `agent=` line and trace the chain before testing. (Submitted pair at 13:27 ended with agent=_rec_agent correctly — disk bug was introduced later.)

**Restored:** both files now end `agent=_rec_agent` (prem overlay + 3-estimator reconcile + dead-op reclaim). Mirror s42: 90547/90523. Paired sanity vs pipe16: +310/+826 (subV both seats s200/s205), +174/+726 (subV2). Matches validated band.

**Resubmit decision:** disk = submitted pair + reclaim (~+50-100 margin). NOT worth resetting a climbing 2500+ pair to ~600 for that. Hold until live pair plateaus or a bigger upgrade exists.

**Live at check:** subV2_f55rec 2575.7, subV_f55rec 2510.7. subOb peak 2685.7.

## Shepherd rescue (v3): also dead — measured, removed

Design: rebuy missing animals when flush (day<=13, money>=cost+2500, empty struct exists, <=6/game) + dedicated shepherd hand (own hire, own steering, zero tape-op edits) to PICKUP shedded animal -> walk -> PLACE on the empty pasture. Theory was sound: ghost FEED/CARE ops on the empty tile service the rescued animal for free.

Measured vs metav4 seat0 seeds 300-305 (same-seed A/B vs base): uniform −255..−1516 regression on ALL six seeds; placed DID recover to 17 on 3 of them — recovery costs more than the animal is worth (hire + fib-shift on tape's later hires + rebuy cash + shepherd labor ≈ $600-1500/day while active). Mirror s42 drifted −104 (fires even uncontested — mirror contention does produce occasional underfill).

**Third failed rescue variant** (v1 blanket retry −17k, ops-leg −14k, mkt-leg −22k, shepherd −300..1500). The failure class (~5% of games, the −21k/−28k blowouts) is real but every graft pays more friction than it recovers. Correct fix is a replanner that owns the schedule — not an overlay. Thread closed; live files stay at agent=_rec_agent.

Also measured: seed-1764841126 mirror — tape's cash curve is healthy uncontested (1098-1814 at the buy steps vs 177-411 in the loss). The trough is opponent revenue compression; buy fails are the symptom.

## Buy-failure forensics — the full mechanism (Refrain −21k, ep 112112553)

Identical buy schedules both sides (COW6+SHEEP11, HIRE278, LAND2 — same tape lineage). Days 6-9 the tape burns cash to ~0 by design (7 pasture builds + 8 hires + seeds/day). Opponent revenue compression pushed our trough below the buy costs (s174 COW @411 ok, s179 COW @268 FAIL, s197 SHEEPx2 @177 FAIL, s217 SHEEP @325 FAIL) -> 14 placed vs their 17 -> −21k compounding. Same-seed mirror: we have 1098-1813 at those steps — trough is opponent-induced, not structural.

Buy->place coupling is TIGHT: PICKUP at buy+2, PLACE at buy+4..9, single-shot. Deferred buys strand in shed (cap pressure). Same-type later pickups can grab a stranded animal (partial self-heal) but the last of a type strands for good.

EV math on rescue: failure class ~5% of games x ~15-20k saved = +750-1000 expected; every graft implementation costs 300-1500 EVERY game it touches (hire/fib-shift/rebuy-cash/shepherd labor) -> net negative. Confirmed by 3 measured variants. CLOSED.

## SIR — sell-impact reorder (2026-09-23) — THE BIG WIN

Ported koshinm's sell_impact_reorder onto both live files (subV_sir.py, subV2_sir.py).
Permutes SELL slots by self-impact score qty*(p_now-p_at_inv+qty), alpha=0.25 demand
urgency. Mechanism: per-item inventories independent → reordering changes only WHERE
our dump lands vs opponent's same-item sell → we capture pre-dump prices.

Results (fresh seeds 224-261, both seats): 48-0 +1054-1456 vs own twin, 40-0
+868-1302 vs pipe16prem, 34-8 +218-1381 vs pipe16, 40-8 vs subJ2945, 48-0 +3123-3319
vs subH_v48, +633-3139 vs melon2749, koshinm −601→−263 (+338). Official env DONE
both seats. Never negative vs non-reordering opponents.

Rejected extensions: BUY_PRODUCT-last (−27k..−43k), rival-pressure boost (+1417<+1456),
alpha sweep flat. Buy-order already optimal (seeds before animals; seed-short cancels
all plantings of that crop).

Remaining koshinm gap ~1k: better endgame price capture (route switch at step 648),
not a structural hole.

## sirx stack (09-23) — three ablation-proven fixes, all measured on real loss replays
- **empty-slot sell defeat**: tape emits `[[],[],SELL]` late-game; per-index lockstep
  means opp's index-0 same-item sell dumps first. Fix = compact sells through empty
  slots (≤ last sell index), never past real orders. ~$1.1k/event on decisive turns.
- **reclaim↔controller deadlock**: post-hoc CARE→PASS conversion vs a controller
  waiting on cared_today = infinite stall. Fix at SOURCE (controller skips dead
  CARE, nxt≤28), not at the reclaim. Pattern: never post-hoc-convert an op a
  stateful controller is waiting to see land.
- **prem overlay blindspot**: sized sells off pre-action shed; hands DROP before
  market runs → use projected_shed(action,view) for same-turn deliveries. ~$644.
- **order-qty vs fills trap**: "FERTILIZER 2334@$9.9" was order requests; real
  fills ~1/7th at parity. Always decode losses from _commit_unit fills.
- market ordering: field ops run BEFORE market within a step (engine :935-941) —
  same-turn DROP→SELL works; last payable production is day 28 (no day-29 refresh).

## MoE r8 — replay resimulation + top-2 clone attempt (2026-09-30)

**Resim unlocked (the big tooling win).** Replay `actions[t]` is the action that
PRODUCED obs at step t — apply `actions[s+1]` at sim step s (off-by-one). With that,
the official interpreter reproduces every tape exactly: 1128/1128 (all 450 MMPQ +
554 DSM + spot checks). Action-only tapes → full (obs,action) streams:
`moe/r8/build/resim/resim.py`. Extracted `bc2r_MMPQ.jsonl` 3.2M rows / 450 eps,
`bc2r_DSM.jsonl` 4.1M rows / 554 eps. Weeds+shops share the per-day seed-keyed RNG,
so the world reproduces identically.

**MMPQ decoded (450-ep confidence, `moe/r8/build/mmpq/`):** hires 4.6→11.5 peak,
wind-down to ~9.4 by d29; 3 quads only (NE@d5-6, SW@d9, SE@d18 in ~16%); herd
sheep/goose-heavy 8.4C/9.0S/6.7G placed; crops W188/S40/M12/C41; fert economy
(collect 16-20/d mid-game AND sell ~181/ep); order-spam = implicit priority queue
(aspirational qty-25 orders, engine affordability cap does bookkeeping); pure greedy
walker dispatch — NO territories, NO momentum (14% fewer moves than DSM); tolerates
~12 escapes/ep. Solo bank ~$105k (m30b makes $150-190k — their edge is consistency,
not scale).

**Clone falsification — six architectures, all dead.** DSM-prog+MLP 45k, pooled-BC
1k, repaired skeleton 52-60k, rules-only 60k, clean-room MMPQ literal spec 1.7k,
MMPQ-prog+MLP 6k — vs v8x ~95-110k, m30b ~150-190k. Offline imitation accuracy
(67.8% top-1 / 94.9% top-3 MMPQ dispatcher) does NOT transfer: state diverges from
tape by ~t50, errors compound 670 turns. The private edge is the ~900-line executor
logistics layer (feed timing, shed chains, watering capacity) which observations
don't uniquely determine. **Program transfers; executor doesn't.**

**What DID transfer (v8prog ablation, `moe/r8/build/prog/`):** scheduled hires
alone +22k, scheduled herd alone +11.5k, both +27.5k (40-0 vs v8x). Scheduled land
and crop floors HURT (−2 to −8k) — keep those reactive. Standing sells (v8x) keep.

## MoE r9 — final-pair optimization + the two-v8s discovery (2026-09-30)

**Two agents share the name "v8"** — the day's critical correction:
- own-v8 = `agents/v8.py` (40KB, our pie-slice scheduler, v1-v31 lineage). Carries
  v8/v8s/v8w/v8x/v8hh. Weak base: banks ~56-65k, loses 0-16 to every pool member.
- r34-v8 = `rivalsGH/r34l-rudr44_kaggriculture/agents_v8.py` ≡ `subAC_v8.py`
  (83KB market-book). Carries subAC_v8/v8p/v8p2. Banks ~113k.
All "r34l-rudr44 credit" lines on own-v8 submissions were misattributed boilerplate;
the sell-meter bug fixed in v8x exists only in own-v8.

**Fresh-seed matrix (640 eps, seeds 9300+, both seats):** m30b .877 > ACv8 .742 >
harvest .625 > C1R2 .550 > shepherd .533 > f55rec .342 > metav4 .242 > v8hh .091.
subAC_v8 is the ONLY m30b-beater: 14-10, +936, banks MORE than m30b. v8hh 0-120 —
falsified as hedge. m30b live autopsy: ZERO crash/timeout mode; wins pure mirrors
28-9, loses 2-12 to same-skeleton market-overlay variants (out-traded: heavier
wheat sells, fert dumps, 2x BUY_PRODUCT arb).

**FINAL PAIR (subs 56709541/56709545): [m30b, subAC_v8]** — both identical-policy
resubmits. Under best-of-two BT, hedge value = P(hedge > anchor): ACv8 contributes
real upside where v8hh contributed ~none. Upload mechanics: newest evicts OLDEST
pair member — to swap only the hedge you must re-upload the anchor after it.
