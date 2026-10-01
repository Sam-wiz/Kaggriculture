# MoE r9 — INTEL lane: discussion mining for private-agent mechanics & exploits

Mined 2026-09-30 ~13:30 UTC. Sources:
- `discussions.md` (12,272 lines, ~531 KB; archive contains Versions 1–5; scraped ~Sep 27 but includes later comments).
- Live Kaggle discussion API via `.venv/bin/kaggle competitions topics …` — fetched Sep 28–30
  topics/comments absent from the archive (topics 743993, 736219, 744218, 744380, 743716,
  743384, 741743, 739273). The endpoint works: `kaggle competitions topics list
  kaggriculture --page-size 200 --format csv`, `topics show`, `topic-messages`.
- Engine source `.venv/.../kaggriculture.py` v1.32.7 read directly to confirm mechanics.
- Our agents: `subAB_m30b.py` (tape engine), `agents/v8hh.py` (reactive market-book).

Classification tags:
- **[m30b]** already implemented in `subAB_m30b.py`
- **[v8hh]** already implemented in `agents/v8hh.py`
- **[patch<2h]** plausibly patchable onto a live agent in under two hours (with the caveat
  that MISTAKES C18 killed our trusted gate — closed-loop validation needed)
- **[out-of-reach]** needs infrastructure/time we don't have today, or isn't real

Confidence grades: **A** = read in engine source / staff-confirmed; **B** = independently
reproduced measurement by credible author; **C** = single-author claim/anecdote;
**D** = speculation.

---

## 1. Market settlement mechanics (the core exploit surface) — CONFIRMED IN ENGINE SOURCE

`_process_market` (kaggriculture.py:544–628) settles both players' order lists
**per index, in lockstep**:

- Each player's market list is truncated to the first **10 orders** (`q[:max_orders]`);
  extras silently dropped. **[m30b]** (max_orders=10 constant, clamp_sells)
- `for i in range(max_len)`: at each index `i`, both players' `order[i]` are parsed.
  **HIRE and BUY_LAND execute atomically first, in player order** (lines 572–581), then
  SELL/BUY_* fill in a **per-unit interleaved loop**: both players quote their next unit
  off the **same pre-commit inventory snapshot**, both commit, repeat until neither can
  fill (lines 583–626).
- **Corollary 1 — index position is the same-turn race.** Your order at index `i`
  settles while the opponent's index-`i` order settles. To sell before an opponent dump
  *in the same turn*, put your sell at an **earlier index**, not just an earlier turn.
  Junk/malformed/empty entries in your list consume indices and delay your real orders
  (Debmalya: "Empty [] entries are positional… dropping an empty entry changes which
  orders settle together").
- **Corollary 2 — same-index pairing is symmetric.** Both players' units at index `i`
  see identical snapshots; there is no intra-index race. When a small order is paired
  with a big one, the small order's units ride the top of the price curve and the big
  order's tail eats the crash alone.
- **Corollary 3 — `$1` floor does not deepen the glut** (`_commit_unit` line 658–660):
  "Sales at $1 do not increase market supply." Dumping at the floor leaves no inventory
  damage for later turns, so a saturated market recovers faster than linear models
  assume. Conversely, an opponent's mega-dump into the floor is less damaging to you
  than raw unit count suggests — but it still took the good prices.
- **Corollary 4 — BUY_PRODUCT anti-arb** (line 599–601): buys quote at
  `inventory - 1` so a buy→sell round-trip against an unchanged market nets ~zero. No
  free market arbitrage exists. (Feed-buyback in MMPQ's program is buying WHEAT for
  feeding, not arbitrage.)
- **Corollary 5 — failed order dies at its index only**: a SELL on an empty shed sets
  that order to None; later queue positions still process. Farm actions resolve **before**
  market orders — same-turn sale proceeds cannot fund same-turn purchases.
- Community confirmation: 3정훈 (rank 1075) reconstructed fills for a full episode —
  "826 ledger entries… total absolute error $0.00; all 6,480 recorded quotes match the
  installed engine's price function" (discussions.md:4179–4234). Debmalya's byte-identical
  Rust port confirms the same semantics (line 9386–9430).
- **[m30b]** — **this whole exploit surface is already implemented, at index
  granularity, in the live agent.** The exported `agent` is `_brx2_agent`
  (subAB_m30b.py:10324–10447), wrapping the route-replay chassis:
  - `front_run` layer: reads an `opponent_plan` tape, sells our premium items one step
    before the opponent's scheduled SELL (turn-level pre-emption).
  - `sell_lead`: advances next-step sales when `step % 4 != 0` (no town consumption
    between); positional slot discipline is explicit ("A zero-quantity order keeps
    later market race slots intact", line 612).
  - **BRX2 sell-reorder** (line 10287+): extracts the SELL positions in the emitted
    queue, builds a `native` vs `sir`-ranked candidate, then **permutation-searches
    the SELL↔slot assignment** maximizing expected margin against a predicted rival
    order book, using `_brx2_revs` — a faithful per-index, per-unit lockstep
    simulation that replicates `_process_market` including the $1-floor inventory rule
    (`if pr > 1: inv += 1`, line ~10372). This IS the index-race exploit, live.
  - **BRX2 online rival-order inference** (line 10412+): each turn compares realized
    cashflow against predictions under a native-ordered rival hypothesis vs a
    SIR-ordered one, updating a log-odds (`_BRX_W_NATIVE`, prior 0.85) that weights the
    two rival books in the permutation choice — i.e. it learns which queue-ordering
    convention the current opponent uses mid-match.
- Implication: "sell at earlier index than the opponent's dump" is **[a] already in
  m30b** (BRX2 does strictly better — it optimizes slot assignment against an inferred
  rival book). A ~30-min audit could still check whether the BASE chassis pads the
  front of the queue with junk before BRX2 sees it, but there is no headroom claim to
  make without measurement.
- **[v8hh]** has no index-positioning layer — its market orders are emitted in fixed
  priority order. **[patch<2h]** a mini-BRX (reorder SELL slots by expected margin
  under a naive rival-book assumption) is technically small but unvalidated; flag as
  candidate-only per C18.

## 2. Sale timing / batching evidence — mixed, opponent-conditional

- **Georgy Mamarin** (rank ~576–871): paired test, same farm/seed/seat, only sell-order
  size varied (line ~11989): trickling 3 units/turn vs emptying the shed —
  vs passive opponent **+280±89** (8/8 seeds); vs sell-on-sight opponent **−547±6** and
  hands the opponent **+593±21** (head-to-head gap 1,154). "The impatient farm wins by
  selling early into a market that decays afterwards." Price support from holding back
  was only ~2% — the effect is a **transfer**, not price protection. **[B]**
  ⇒ "Always trickle" is false; batch size must be opponent-conditional.
- **Yujin Cha** (rank 1455): near-mirror farms stayed equal until late; matchup decided
  by when/how much each sold (wool crashed 226→31→1 when both dumped). Splitting
  1000-unit endgame sales into slices made things *worse* over 6 seeds (−4.9k → −6.2k
  gap vs V53). **[B]** Consistent with Georgy: slicing loses against dumpers.
- **VijaiKurianMathew** (rank ~3022): mined 3.26M actions / 214 episodes — #1 loss class
  was `premature_sale` ("$1M+ dumped into crashed markets"). Winners sell same-turn as
  harvest 41.6% of the time ("zero-latency sells"). Rule of thumb: never dump >20 units
  of premium goods in one order — convex curves crash to $1 at ~+63–77 units over
  baseline inventory (line 3617). **[B/C]** — note this *contradicts* Georgy in spirit;
  reconciliation: >20-unit premium orders vs an empty market crash *your own* tail units
  (Corollary 2 applies to your own order's units too — each unit re-quotes). Batch
  capping is self-protection; trickling across turns is what loses.
- **Ritwik Raha** (3368): screened premium-seller floors/batches — FLOOR =
  {MILK 120, WOOL 140, STRAWBERRY 90, MELON 60}, start-day screen [10..22], batch screen
  [1..60] → best pair **day 14 / batch 15**; premium window "roughly days 9–14… a melon
  sold on day 25 is worth about a fifth of one sold on day 12" (lines 6100–6330). **[C]**
- **Premium floor glut as weapon** — Shair Khan: "closed-loop policy adaptation
  consistently loses to static macro-schedules + concurrent market-queue floor
  manipulation… forcing opponent sell orders straight into the $1 price floor"
  (line 3225–3234). Asked whether top policies do this; no proof supplied. **[D]** —
  plausible via Corollary 3 but nobody demonstrated it; treat as hypothesis.
- **destbreso** (rank ~922–1229): mirror/draw detection — "a draw is a strong
  deterministic signal" of same-lineage; counter = advance sales by one turn; must not
  break the financing chain; cloning teams do this systematically. **[B/C]**
- **[m30b]** covers turn-level advancement (front_run + sell_lead), min_sell_price=2,
  clamp_sells to projected shed, dead_stock, terminal_liquidation.
- **[v8hh]** standing SELL every turn "sell through dips" (decoded top-team rule),
  sell_per_turn=5, hinge_meter sells hinge goods below drain rate while scarce,
  full liquidation day ≥ LAST_DAY−1. **Gap**: standing small sells ignore the
  Georgy result — vs a sell-on-sight opponent the trickle bleeds. **[patch<2h]** a
  contested-market detector (opponent sold >k units of item X yesterday → sell our X
  now, not across `horizon`) is a small, contained change to `sell_orders()`, but
  validation gate is weak — flag as candidate-only.

## 3. Seed determinism, RNG structure, shops

- Weeds and shop unlocks draw from the **same per-day RNG stream**; weeds consume one
  draw per empty tile → **the shop sequence depends on both players' actions**
  (Debmalya, line ~9412; also qihuaz in Picu's seed thread, line ~4874). First shop
  fixed by end of step 71, second by step 143. **[A]**
- ⇒ **Seed reverse-engineering is not a live exploit**: Picu asked about predicting
  shop unlocks from the seed; answer is no — action-dependent draws defeat any static
  lookup. **[A, out-of-reach]** Don't spend time on it.
- A *deliberate* RNG-steering exploit (keep tiles occupied/empty to shift weed draws and
  thus the next shop draw) exists in principle — one could in theory bias shop
  composition toward products one is stocked on. Needs a differentiable model of the
  per-day draw schedule and is worth single-digit EV at best. **[out-of-reach]**
- Local-tool caveat: Michael Timbs / Amedeo Biolatti noted weed+shop coupling makes
  fixed-replay comparisons noisy; Timbs locally forces shop evolution for controlled
  analysis. Doesn't transfer to the official env.

## 4. Private score / leaderboard mechanics (submission-strategy intel)

- **Final scoring** (María Cruz, Kaggle staff, line ~105): submissions keep running
  episodes for **two weeks** past the deadline, then a **single Bradley–Terry
  tournament** decides final ranks — "reduces hot streaks." Addison Howard: "plan is to
  write BT to private leaderboard if possible." Ties = half wins (staff-confirmed
  earlier). **[A]**
- **Team score = better of the two active submissions** (staff). **[A]**
- **Provisional rating is path-dependent** — Rayk Kretzschmar (1790): two byte-identical
  submissions 2h apart converged ~1700 vs >3000. Confirmed pattern by Victor Mercklé,
  Tien N. (resubmit −500), 守银摄金难铜 (resubmit −1000), Steve421471. **[B]** — but
  this is *provisional* Elo noise; BT final is computed fresh.
- **Convergence quantified** (Georgy Mamarin, 811 submissions / 224,523 games):
  median submission is 718 pts from settled after 5 games, 338 after 10, 222 after 20,
  **145 after 40**; ~15 games/hr for first ~5h, then <3/hr. Submissions that eventually
  played 400+ games were still 542 pts from settled at game 40 — "one curve over two
  populations." Ryo Hasegawa (ex-#1, topic 736219): ~90% converged by ~60 games; early
  losses disproportionately delay climbing; optimize **win probability vs nearby-rating
  opponents**, not raw money; re-submitting unchanged code is useless for final rank.
  VijaiKurianMathew: ~3 days / 100 games, 70% in first 6h. destbreso: measure drift in
  **episodes not hours** (leaderboard updates in batches; `n2 > n1` filter essential);
  one byte-identical agent fell **182 pts over 135 episodes** — field drift makes
  ratings non-comparable across windows. **[B]**
  ⇒ Relevance today: m30b at ~1750 mid-convergence tells us almost nothing about its
  lock value; its prior convergence (2220.6) is the better anchor.
- **Michael Timbs** (rank ~1317–1380, peaked #6): "submissions currently in the top 10
  are basically obsolete by the time they get there"; strategies cloned "within the
  first 24 hours"; "My 2500 ELO submission is stronger than my 2860 one"; undefeated
  runs can reach #1 in ~8h. **[B]** for reading the board; matches our decay evidence.
- **mikelou1** (rank 21): "There is no private tests… you cannot overfit for the
  leaderboard… public notebooks represent like 90% of the leaderboard — run a mini-ELO
  tournament." **[C]** — supports clone-pool representativeness but our C18 mistake
  stands: frozen replay ≠ live reactive opponents.
- Post-deadline play continues 2 weeks ⇒ a fresh upload submitted today has ample games
  before lock; converged *final BT* strength is what counts, not today's Elo.

## 5. Farm-economy mechanics

- **Daily reset toll** (Marcelo Correa): farmer+hands respawn at shed each day; walking
  back costs ~15 p.p. of turns; hands must be re-hired daily (Fibonacci, resets); gains
  saturate ~5 cells for a lone farmer; melon ≈ 3× wheat per tile-day (fewer visits).
  **[B]**
- **FERTILIZE gating** (Siva Kumar / Civitasmass dup post, ~1399): doubles tile yield
  only if applied **≤2 days before a production event**; yield-aware gating took
  fertilize actions 0→54. **CARE gating**: `pending_care_bonus` banks only when the
  animal is **fed the same day** — fixing care/feed alignment gave **+25% milk, +51%
  wool**; elite bots CARE on production hours {6,12,18} at ~25% alignment vs ~10%.
  Route-commitment for feeding cut animal deaths 10→1/game (PICKUP 1100+/game → meta
  135). Day-28+ liquidation: shed stock scores zero → bypass sell reserves, +$2.8k/game.
  **[B/C]**
  - **[m30b]**: terminal_liquidation + dead_stock already cover the endgame; care/fert
    timing is baked into the tape (the underlying route was cloned from top play which
    already does this).
  - **[v8hh]**: FEED tasks always enqueued when `!fed_today` (line 974–978); CARE tasks
    enqueued when `!cared_today` (line 979–980) — CARE is **not gated on the animal
    being fed today**, and feed/care dispatch to different units can desynchronize.
    **[patch<2h]**: gate CARE on `t["fed_today"] or fed-will-happen` — small, real EV
    if the claim holds, low risk.
  - **[v8hh]** FERTILIZE already recipe-gated (`RECIPES[crop]["f"] > 0`, line 834) but
    not explicitly production-window-gated; check `fertilized_until_day` bookkeeping —
    minor.
- **Fertilizer by-product > animal product** (Marcelo Correa): goose cycle, collecting
  fertilizer +$2,725 vs ~$1,250 of eggs. **[C]** — both agents already collect/sell
  fertilizer (v8hh sells FERTILIZER standing; m30b tape does).
- **Fertilizer SELL version mismatch** (Roy Lampe): buy→sell FERTILIZER worked on local
  1.32.7 but silently failed on notebook env 1.29.3. **[A]** We pin 1.32.7
  (requirements-lock) — fine; don't trust old-version results.
- **README lies** (Siva Kumar): town demand "escalates 2× after day 10" does NOT exist
  in engine ≥1.32.6 — flat shop consumption only. Melon max_yield_day: README 10, code
  12. **[A]** — v8hh's tables already use code values (MELON first=10/myd=12 ✓).
- **HIRE economy**: Fibonacci `1,1,2,3,5,8,13` resets daily; Georgy measured 6 hands =
  20 coins/day vs quadrant cost 1,000; "bare ground at nightfall tracks the bank far
  better than ground per worker" — 12 tiles / 3 hands slice-owning **+3,871±990** vs
  shared-list −601; 50 tiles +6 hands only +1,217 (uncovered land negative). Jack
  (rank 26): "#1 on LB is actively using SE quadrant" — the leader does use all 4
  quadrants (cost 7,000 total, NE→SW→SE fixed order). **[B]** — v8hh's scheduled
  HIRE_TABLE (4→11/day) + herd windows encode this; m30b tape likewise.
- **Engine gotchas** (starkhushi, +corroborated): shed = 4 center tiles (4,4)(5,4)(4,5)
  (5,5); SELL only spends from shed; FEED consumes WHEAT from the **unit's** inventory,
  not shed; animals bought into shed → PICKUP → walk → PLACE; two units PLANTing with 1
  seed = silent stall; BUILD no-ops on non-None tiles. **[A]** — all handled by both
  agents (m30b `_is_noop` models legality; v8hh dispatch carries feed).
- **719 actions, not 720** (Debmalya): runner asks for actions at steps 0..718; a
  driver applying a 720th changes the bank. **[A]** — m30b `LAST_ACT_STEP=718` ✓.

## 6. Tape/cloning meta (the field structure)

- **sobameshi** (rank ~588–1295): tracked submissions are mostly recorded 720-turn
  tapes replayed on fresh seeds; cloning a recent strong public strategy ≈ top 10%;
  14-implementation round-robin on 96 fresh seeds → near-chronological ladder (newer
  beats older in 86/91 pairs; adjacent ~60–80%; two-gen apart 90–100%); **main
  interaction surface is the shared market**; "a small reactive layer for tape-like or
  near-mirror opponents made those matchups noticeably easier… but the reactive layer
  alone has never been enough to get us into the top 100 — strong underlying economy
  first, thin adaptive layer second." **[B]**
- **destbreso's ecosystem analysis** (multiple threads): emergent interspecies
  interactions, lineage tracing, habitat-gradient path dependence; top agents are
  "highly specialized on top of a traceable baseline." Their x-ray notebook hunts the
  reigning #1 live (climbs the ladder via episode opponent links); **"today's king is
  the only genuinely live policy the instrument has read… its plan diverges from turn
  34, before the first shop draw, in all eight worlds"** — i.e. the current #1 is a
  true runtime agent, not a tape. **[B]** — implies the very top is non-clonable.
- **Michael Timbs**: fingerprinting traces lineages; most submissions are static
  policies with "very primitive" reaction (shop ordering only); "within a day of
  submitting a fixed policy it is copied."
- **Opponent-state information value** — Syed Asad Ali (rank 39, Sep 28, topic 743993):
  top agents likely hybrid (learned + deterministic guards + lookahead); apparent
  randomness comes from **shop order, opponent actions, prices**; "most top agents react
  more to market state than directly to opponent farm state"; bigger levers = build
  order, shop-aligned production, sale timing. **[C]** — matches our structure.
- **dzjiann** (rank ~1100–1800): PPO meta-agent selecting among public route
  trajectories plateaued — openings counter cyclically (rock-paper-scissors); opponent
  identity × opening branch predicted outcome at 67.5% (vs 54.2% baseline, opponent-only
  56.5%). "Pairwise payoff matrix more informative than average win rate." **[B]** —
  validates router/non-transitivity concerns; also their JAX/self-play ceiling ~20–22k
  gold and "rules > RL at this horizon" consensus (hengck23, Sahaj: need ≥10M games).
- **hengck23** (Kaggle GM, rank 3576 here): proposed architecture — copy a strong
  replay, train a market policy net on "deviate from forecast" + opponent-capacity
  features. Proposal only, no results. **[C]**
- **SpaTaro**: only top-10 agent noted to play a unique strategy every game (per
  sobameshi tracking, line 1983) — genuinely live policy at the top.

## 7. Environment bugs / runtime mechanics

- **obs["step"] missing for seat 1 — RESOLVED, tooling-only** (stpete_ishii + Yizuki +
  destbreso): `env.run()` agent calls DO get correct step for both seats; `env.step()`
  return values, recorded `env.steps`, and downloaded replays show `step: None` for
  seat 1 on all 719 turns. destbreso's house rule: **never read obs["step"]; derive
  `day*24+hour`** — reproduces recorded banks to the dollar (8/8). **[A]**
  - **[m30b]** `_step_of` already falls back to `day*24+hour` (line 308–312) ✓ —
    protected on both live and replay paths.
- **Timeout** (Zotar + Bovard Doerschuk-Tiberi, staff): `episodeSteps=720`,
  `actTimeout=1`, `remainingOverageTime=60`, inherited `runTimeout=1200`; sequential
  worst case would be 1560s > 1200, BUT staff: **"The two agents are run in parallel so
  1200s is a safe upper bound."** ⇒ per-turn budget ≈ 1s is real; no run-level risk.
  **[A]**
- **Less (rank 398) "winners deducted points" report**: staff (Addison Howard) —
  visual/display bug only; backend credited correctly (+105.8 / −4.5). **[A]**
- **Concurrent-episode rating overwrite** (line ~3215): two episodes finishing together
  appeared to both read the same base score and one update was lost. Unanswered —
  plausible provisional-Elo race, irrelevant to final BT. **[D]**
- **Matchmaking cadence** (4071–4150): ~fixed schedule early (~1–2 games / 4 min for
  first ~80 games); top-10 pool narrows — high-ranked players may never meet some
  counters. **[B]**
- **Episode data sources diverged** (Georgy Mamarin): Daily Top Episodes dumps vs
  API-crawled corpus share **zero** episode ids since Aug 9; ladder plays ~140k public
  episodes/day; dumps ≈ top-rated 0.5% slice. If anyone BCs: the dumps are the slice
  that matters. **[B]**
- **Engine version pinning** (Debmalya): 1.32.7 changed CARROT/TOMATO/EGG scarcity
  pricing (new hinge knees); "an older kaggle_environments left in a user site-packages
  silently prices on the old curves." Georgy measured the cutover: Aug 15, merge→PyPI
  →ladder in **17 minutes**; carrot planting 6.3%→44.2% of seat-games; frozen code
  never adapts (0/332 flipped crops); per-team bank delta a coin flip (+610, p=0.41);
  winner-loser gap compressed 6,810→4,454. **[A/B]** — (i) our pin is correct, (ii)
  balance patches mid-season are real and tapes can't adapt — a faint argument for the
  reactive hedge.
- **GPU trap** (VijaiKurianMathew): Kaggle P100 + torch 2.10 = silent CPU run. Infra
  trivia; irrelevant to our stdlib agents.

## 8. Opponent-information channels

- **Opponent inventory inference** (dzjiann, rank ~1100): bookkeeping identity
  `ΔS_i = H_i − C_i − (ΔM_i + D_i) − F_i − L_i` lets you bound the opponent's loose
  stock per commodity. **CARROT/TOMATO/EGG recoverable to MAE ≈ 0.000–0.008**; MILK/WOOL
  noisy because $1-floor sales leave no inventory trace (Corollary 3) and shed-vs-carried
  isn't observable. Suggested features: estimate + lower/upper bound + floor_risk per
  commodity. **[B]**
  - **[patch<2h]** borderline: a ~60-line estimator could feed v8hh's price forecast a
    "opponent is holding X units of tomato" signal (anticipate dumps before they hit
    `market.inventory`). Risk: no trusted gate, and v8hh already partially captures this
    via `scan_opponent` tile counting (their *pipeline*, not their *inventory*).
  - **[m30b]** gets most of this via `opponent_plan` when the opponent is a known tape.
- Same-turn omniscience impossible: both agents act simultaneously; you see the
  opponent's *prior* action only. Mirroring their crop plan floods the market and hurts
  both (v8hh's `opp_mirror=0.7` dampens this already).
- Private state is hidden: opponent shed/seeds/carried-inventory not observable — the
  estimator above is the best available channel.

## 9. Named-team coverage (who said what, who didn't)

| Requested name | Found? | Substance |
|---|---|---|
| MMPQ | No direct posts in archive; topic 743384 (Sep 28) asks about MMPQ/Boey — unanswered, only jokes | Nothing public. Our FINDINGS.md decode stands: edge = tempo/volume (all-in d0, land 1d earlier, carrot@d0, feed-buyback, 11.5-hand peak, spam-order priority queue), same greedy-walker dispatch family. |
| DSM | No hits | — |
| DECEM | 2 comments (8800, 9051) | Rank **1st** at scrape time; only said "Getting Better and Better" on an RL post. No mechanics. |
| Victor@Tufa / Victor Mercklé | 8152, 10738 | Rank 3521/35. Only rating-path-dependence commentary ("early losses make climbing extremely slow"; stale-agent pool). No mechanics. |
| Joseph Adamski | No hits in archive | (Known ~2700 opponent from our r3 games.) |
| lingxiaojun | No hits in archive | (Known ~2700 opponent from our r3 games.) |
| sobameshi | Multiple (1814–2143, 11913+) | Tape-meta quantification, round-robin, thin-reactive-layer finding — §6. |
| Erfan | No hits | (Known ~2700 opponent.) |

**Highest-value authors actually found:** destbreso (engine-faithful measurement:
step bug, shop knees, convergence), Georgy Mamarin (market A/B numbers, convergence
stats, patch-cutover field study, dataset forensics), Michael Timbs (meta/lineage),
3정훈 (order→fill reconstruction, exact), Debmalya (byte-identical Rust engine +
mechanics list), Syed Asad Ali rank 39 (top-tier architecture claims), mikelou1 rank
21 (LB composition), Jack rank 26 (#1 uses SE quadrant), Civitasmass rank 246
(convergence ~12h, post-deadline reset-to-600 claim), Snorlax rank 48 (RL silver),
dzjiann (meta-agent PPO + inventory inference), Ritwik Raha (premium-floor batch
screens), VijaiKurianMathew (loss taxonomy, CARE timing), Shair Khan (queue-floor
hypothesis), Ryo Hasegawa ex-#1 (submission strategy: optimize win% near your rating;
resubmitting is useless).

## 10. Actionable shortlist for the remaining window

1. **No code change is clearly justified today.** Every <2h patch below is bounded-EV
   and carries C18 risk (our only trusted gate was the RR map; these would need a
   matrix-lane screen before submission — and slots are the scarce resource anyway).
2. **m30b already owns the index-race** (BRX2 permutation optimizer + rival-book
   inference, §1) — the only residual audit is whether the base chassis emits junk
   orders that consume early indices before BRX2 reorders them (~30 min, read-only).
3. **v8hh contested-sell mode (<2h, unvalidated):** standing trickle-sells lose ~547
   coins/game vs dumpers per Georgy. A `contested` flag (opponent's yesterday's sell
   volume per item > threshold → sell all of that item today) is small. But v8hh's
   failure mode per the autopsy is getting *out-farmed* by off-meta agents, not market
   races — likely low EV for its pair role.
4. **v8hh CARE gating on fed_today (<1h, small EV):** only enqueue CARE for animals
   already fed today (or co-assign feed+care). Claimed +25% milk / +51% wool at
   low rank; our herd is scheduled so partial coverage likely exists.
5. **Out of reach:** seed/shop-RNG steering, RL/BC overlays, opponent-class mid-game
   route switching, queue-floor-forcing as a deliberate weapon, and any
   rebuild-the-executor work (6 falsified this round).
6. **Submission-strategy intel (free):** ratings are path-dependent noise; ~145 pts of
   drift remain at game 40 on median; final BT is fresh-computed over 2 post-deadline
   weeks → submit on intrinsic strength + decorrelation (v8hh fits), not on current
   Elo. Byte-identical resubmission cannot fix a bad trajectory *and* is pointless for
   the final anyway.

## 11. Limitations / caveats

- Archive is a snapshot; Sep 28–30 threads were supplemented via the CLI, but long-tail
  comments under 6h old and Discord content are not covered. Several top teams (MMPQ,
  DSM, DECEM, lingxiaojun, Joseph Adamski, Erfan) have **never posted substantive
  mechanics publicly** — silence is the finding; their edges are only in replays
  (which the decode lane already mined).
- Many "elite do X" claims are fingerprint-based (action-count histograms of public
  replays), not code access — directionally reliable, magnitude-uncertain.
- The $1-floor-dump exploit geometry (Corollary 3) is verified in source, but nobody
  has published a winning implementation of *deliberately* forcing opponent sells into
  the floor — keep it as hypothesis, not plan.
- All sale-timing results are opponent-conditional: effect signs flip between
  passive and sell-on-sight fields (Georgy). Any tuned constant is a bet on the field.
