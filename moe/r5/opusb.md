# MoE r5 — opusb (Opus 5.5 #2, BUILD lane + Kaggle time budget), round 1

Clock: started 20:36 UTC 09-26 (`date -u`); experiments 20:40-21:15; written 21:15-21:40 UTC. Foreground only, ≤2
workers, nice 10, no background jobs left. Scripts, outputs and logs are all in `moe/r5/build/opusb/`. External calls:
5 raw episode downloads from `kaggle/kaggriculture-episodes-2026-09-25` (deleted after extraction; the extracts are
kept), plus 1 `competitions episodes` + 1 `competitions logs` call for our live C1. All read-only, no submissions.

## 0. Bottom line

1. **The top family plans at runtime on Kaggle, measured from their replays.** THIRD FARM CLUB spends
   **~2.9 s at every dawn from day 8 to day 29** (5.8 / 4.0 / 11.1 s on days 8-10) and ends the game with 6.5 s of its
   60 s bank left. 吃白饭的大肥鱼 re-plans in hour-level bursts on days 12-15 (up to 16.3 s). DSM, Boey, Majkel1337 and
   M&M&P&Q spend 13-38 s on their first call only. So Architecture B is what at least two of the four robust teams do.
2. **The budget is much larger than the 60 s bank.** Budget: `actTimeout` 1 s per step (free, not banked) plus a 60 s
   overage bank, with agents called in parallel. **The free 1 s/step adds up to ~720 s per game, 12× the bank.**
   Kaggle's CPU is **~3.5-4.5× slower than this M1** (our live C1: 6.62 ms/step mean, 5.13 median on Kaggle vs
   1.8-1.95 / 1.1-1.2 ms locally). Design rule: spread planning over the free per-step time and keep the bank for
   step-1 loading and emergencies.
3. **The official interpreter can serve as the planner's simulator, and it is exact and cheap.** It is pure Python and
   importable in Kaggle's agent runtime (kaggle_environments 1.32.7, Python 3.11), and it can be vendored.
   - Cost when called directly: **0.04 ms/step with PASS agents, 0.13 ms/step with C1-level action traffic.**
   - Full rest-of-season rollouts: **~60-95 ms on M1** with a tape policy (~0.3-0.4 s on Kaggle); 1.5-2.6 s with C1
     itself as the policy.
   - A state rebuilt from *our observation* reproduces the real game **to the dollar** (given the opponent's actions
     and private state).
   - Sonnet's §2 figures (2.30 ms/frame PASS, 9.25 s per full-game rollout) are 20-100× too slow. They price
     `env.run` framework overhead plus both agents' policy cost, and they ignore the free 720 s (§2).
4. **B with recorded top tapes as the candidate plans ("TS") is measured dead.** I built the dawn planner:
   - Exact rollouts from our observation.
   - An opponent model from exact shadow market deltas.
   - Tape candidates retrieved by shop prefix or by state similarity.

   Closed-loop vs C1 over 4 variants: **3/32 wins, mean margin −$15.5k to −$37.8k.** That equals the r4 TFC router
   (0.24, −$14.5k) and is better than raw tapes (8/125). It fails for the reason r4 found: no recorded plan fits our
   state and world after day 9. The plumbing is reusable and validated.
5. **C1 can be cloned exactly for rollouts with `os.fork`:** 3/3 continuations match the real game to the dollar.
   This makes a **C+B hybrid** buildable: C1 stays the executor, and a dawn planner picks, per world, among switchable
   macro options using fork-cloned C1 rollouts. But gating C1's *existing* knobs is capped: the tomato gate's
   per-world oracle is worth ~+$225/g, from r4 T2 data. The hybrid only has value if *new* options have large
   per-world variance, and that is the +12 h kill test (§5).
6. **P(3k+ | fielded in slot 2) 0.3%, P(top-10 | fielded) 0.4%, P(beats C1 closed-loop) ~20% for the C+B build**
   (~1% for TS). No construction measured this round is on a path to 3k.

## 1. Kaggle time budget — measured, not assumed

| fact | value | source |
|---|---|---|
| per-step free time | `actTimeout` = **1 s** (env spec); unused time does not bank | `kaggriculture.json`, `agent.py:207-221` |
| overage bank | **60 s** per agent per game; overshoot beyond 1 s is deducted; <0 → TIMEOUT loss | `kaggriculture.json`, `core.py:628-632` |
| episode cap | `runTimeout` 1200 s per episode. Agents are called via `Pool.map` when parallelizable, so per-agent wall ≤ 720 s + 60 s. *Inferred* from `core.py`, not observed in Kaggle's orchestrator; TFC-heavy episodes do complete DONE. Keep our per-step average ≤ 0.3 s so that even a sequential runner stays far from 1200 s | replay `configuration`, `core.py:326-332, 740-743` |
| Kaggle runtime | Python 3.11, `/usr/local/lib/python3.11/dist-packages/kaggle_environments` importable from the agent; replays report `module_version` 1.32.7 (= ours) | `logs/episode-105182622-agent-0-logs.json` traceback; replay header |
| **Kaggle CPU vs this M1** | our live C1: **6.62 ms/step mean, 5.13 median, p99 15.8 ms, first call 0.74 s** (ep 113848034) vs local 1.8-1.95 / 1.1-1.2 / 8.9-11.4 ms, first call 0.04-0.06 s → **×3.4-3.7 (mean), ×4.3-4.7 (median)** | `klogs/`, local re-run |
| Kaggle episode wall | 88-321 s for the last 4 C1 episodes | `competitions episodes 56560349` |

**How the field spends it** (`overage_scan.py`; `overage_rawtop.jsonl` = 42 older top seats;
`overage_top0925.jsonl` + `overage_bursts.txt` = 10 seats from 5 raw 09-25 top-vs-top episodes). The wall figures
below are ≥ 1 s + overage; sub-second compute is invisible in replays.

| team | overage used / 60 s | when |
|---|---|---|
| THIRD FARM CLUB | **53.5 s** | first call <1 s; **every dawn day 8-29**: 5.79, 3.99, 11.11 s on days 8-10, then 2.87-2.89 s each dawn; 6.47 s left at the end |
| 吃白饭的大肥鱼 | 42.5 s | 3.0 s first call; bursts through hours 0-15 of days 12-15 (1.1-1.9 s each, 16.3 s at d15 h3); dawns d16-24 |
| M & M & P & Q | 37-38 s | first call only |
| Majkel1337 | 11.6-24.1 s | first call only (6/6 seats) |
| DSM | 10.3-19.2 s | first call only (6/6) |
| Boey | 13.4-18.3 s | first call only |
| Vadim / UMG / Blurry / Roman K. | 11-16 s | first call only |
| older mid-table seats | 0 | — |

TFC's fixed 2.87 s at each dawn is a deadline-capped anytime planner that budgets to the bank. On Kaggle hardware,
2.9 s is ≈0.65 s of M1 compute, i.e. about 7 tape rollouts from our code.

**Budget design for any planner we field (the numbers above ×4.5):**
- Normal steps stay under ~0.3 s on Kaggle (≈65 ms on M1). Planning runs in slices of the free per-step time and is
  evaluated for the *next* dawn from the current state. A rollout that continues the current plan to dawn and then
  switches is exactly the "switch at next dawn" evaluation. That gives ~23 × 0.3 s ≈ 7 s of Kaggle compute per day
  (~1.5 s M1) at zero overage.
- Every call reads `obs.remainingOverageTime` and a `perf_counter` deadline. No single step may exceed
  `1 s + min(5 s, 0.25 × bank)`.
- Step-1 library decode stays ≤1 s on M1 (≤5 s on Kaggle). The top teams show 13-38 s at step 1 is tolerated, but the
  loss if we time out is total.
- Fork children are killed at the deadline (`os.kill`); the agent then falls back to its current plan.

## 2. Correction to sonnet §2 ("kill B: 1,000-5,000× short")

Sonnet's measured ms/frame are not the planner's cost. Same machine, `bench_engine.py`, `ts.py`, `forkclone.py`:

| quantity | sonnet §2 | measured here | why they differ |
|---|---|---|---|
| interpreter, PASS/PASS | 2.30 ms/frame | **0.043 ms/step** (480 steps from a day-10 state, 0.020 s) | a planner calls `K.interpreter(state, env)` directly (as `harness.py` does); `env.run` adds schema validation, structify and deepcopy every step |
| interpreter, realistic traffic | 12.85 ms/frame | **0.13 ms/step** engine + glue (C1 vs C1 game: 2.36 s wall, of which 2.26 s is the two agents) | the 12.85 ms is two chassis policies plus framework; a rollout's policy is whatever we choose (a tape costs ~0) |
| full-season rollout | 9.25 s | **60-95 ms on M1** (tape policy, with deepcopy and opponent injection); 1.5-2.6 s with C1 as the policy (fork-cloned) | same |
| budget | 60 s total | 60 s bank **+ ~720 s free** (1 s/step) | `actTimeout` is per step and unbanked, so 720 × up to 1 s is available without touching the bank |

What sonnet has right: kagsim (Mach-O arm64) cannot ship. A timeout loses the game, so budget accounting needs hard
deadlines. With C1 as the rollout policy, full-season lookahead is expensive: ~7-12 s per rollout on Kaggle, i.e.
1-2 per day inside the free budget unless horizons are truncated. So "deep search with the real chassis" is out, and
narrow option gating is in, as sonnet proposes. But B with a cheap policy fits comfortably, and the top family runs
it.

## 3. What I built and measured (prototype TS = Architecture B over recorded top plans)

**Exactness of the planner's simulator (`tsgame.py --validate`):**
- Rebuilt from the TS seat's observation at steps 144/240/360, plus the opponent's true private state, its recorded
  actions and the true seed, the rollout reproduces **both banks to the dollar in 6/6 snapshots** (2 seeds × 3).
- Separately, **40/40** recorded top-vs-top games reproduce exactly on the official Python engine (`oppprof.py`).

**The opponent is the dominant model error.** The opponent's private state is hidden, so rollouts drop it:
- PASS opponent: our rollout bank is **+$47k to +$55k** too high.
- Injecting the opponent's exact *future* per-step net market deltas: −16% … +19%. The residual comes from injecting
  before or after each step, versus the real lockstep order.
- Recent-pattern extrapolation (last 2 days by hour): +$40-55k, because opponents sell in late bursts.
- Data-driven profile scaled per item to this opponent's observed supply so far: **+10% … +26%**.

The per-step deltas come from a one-step shadow re-simulation: actual market minus our own step, since our fills do
not depend on the opponent. `shadow_err` = 0. The profile is the mean per-step net supply of robust top-family seats,
from 40 exactly replayed games. Season net per seat: WHEAT 253, FERTILIZER 217, EGG 192, STRAWBERRY 182, MILK 176,
WOOL 140, CARROT 139, MELON 80, TOMATO 79. C1's seat is similar in premium volume but has far fewer EGG/TOMATO
(76/16, `c1prof.py`).

**Closed-loop, TS vs C1** (official engine, `harness.run_episode`, fresh seeds 9510001-08, seats alternate by seed,
0 errors):

| variant | W | mean margin (SE) | our / C1 bank | plan time per game, M1 (max/dawn) | switches |
|---|---|---|---|---|---|
| A: 718 robust tapes (TFC, Boey, 吃白饭, Majkel), shop-prefix retrieval, M=8, R=1, top profile | 2/8 | −$15.6k (5.4k) | $101.8k / $117.5k | 16.7 s (3.0) | 5.6 |
| NN: same, state-similar retrieval (tile Hamming + cash + shop prefix, `libstate.py`), M=8, R=2 | 0/8 | −$15.5k (4.3k) | $90.1k / $105.6k | 31.9 s (5.6) | 10.2 |
| C1prof: A with the C1-class opponent profile (upper bound on opponent-class ID) | 1/8 | −$16.4k (4.3k) | $95.3k / $111.7k | 19.3 s (3.0) | 6.1 |
| ALL: ~3.5k tapes from 12 top teams, prefix, M=12, R=1 | 0/8 | −$37.8k (9.6k) | $88.7k / $126.4k | 22.8 s (2.6) | 6.9 |

**Why TS fails** (from per-dawn logs, `ts_*.jsonl` field `log`):
- **(a) No fit after day 9.** Past day 9 the best retrieved tape matches only 2 of our shops, and no candidate beats
  "stay" by the margin. The splice damage the rollouts price (plants of ours the new tape never waters, dead
  ops) outweighs any world-fit.
- **(b) Optimism bias from the max-of-noisy-candidates.** Prediction minus actual is +$36k at dawn 0, +$10-20k at
  dawns 6-15, and +$1.5k at dawn 24.
- **(c) A wider library hurts.** Cash-lean teams' tapes look fine in rollouts, then break against the real market
  (seed 9510005: $35k bank).

Opponent-class modelling does not move it (C1prof ≈ A). Kill criteria for TS are met: it is not a slot-2 candidate.
Budget-wise it would also need ~75 s of Kaggle compute per game, so it would have to be amortized.

**Fork-cloned C1 (`forkclone.py`)**, C1 vs C1, the parent forks at step T and the child continues the same game:
- **Banks match to the dollar 3/3** (T = 144, 240, 480).
- The true continuation takes 3.2-5.9 s. The C+B rollout shape (our C1 from our observation plus profile injection,
  opponent PASS) takes **1.5-2.6 s on M1 ≈ 7-12 s on Kaggle** per rest-of-season rollout, and its bank error vs the
  real game is −2% / +1.5% / +28% (T = 240 / 480 / 144).
- C1 carries dozens of stateful overlay layers (exec'd namespaces, a Chassis object, closures), so a module-state
  snapshot would be fragile. Fork is the clone to use. Fork is untested inside Kaggle's agent sandbox; that is item
  1 of the +12 h kill test.

## 4. Architecture pick (build lane) and why

- **A (macro imitation + our executor): not from me.** We have no executor near top efficiency (exec3 $35k vs V48
  $96k). The only top-efficiency "executor" we hold is the recorded tapes themselves, and §3 shows those cannot be
  re-targeted to our state. If opus extracts a clean macro table, its content should become C+B *options*.
- **B over tapes (TS): dead**, measured 4 ways (§3). Its plumbing is the asset: exact rollouts from an observation,
  shadow opponent deltas, opponent profiles, the budget rules.
- **C (chassis + fixed macro corrections):** sonnet's pick. The project's base rate for structural ports on the
  chassis is poor (09-21; T2 −$1,166/g), and the r4 E-shop2 data says the value is *world-conditional*. A fixed
  correction pays in some worlds and costs in others, and averages near zero.
- **My pick: C+B.** C1 is the executor. 2-3 decoded top-family gaps are built as switchable C1 overlays ("options"):
  - 4th quadrant by ~day 10 when cash allows;
  - geese to ~6;
  - an earlier tomato program with a replant cycle, or a strawberry cap in glut worlds.

  At 1-3 decision dawns, a planner turns each option on only in worlds where fork-cloned C1 rollouts (paired on the
  same sampled seeds, opponent profile injected, 3-5 day horizon plus terminal valuation of assets) say it pays.
  - What it fixes in C: a mixed-sign option becomes non-negative, provided the rollouts rank the options correctly.
  - What it fixes in B: the plan generator is our own efficient executor, not a foreign tape.
  - Ceiling: bounded by the options' per-world variance. That is tens to low hundreds of Elo, not 900. Existing knobs
    are too small: T2's per-world oracle ≈ +$225/g (+$6.3k in 1 of 28 seeds, r4 `t2/summary.log`). So new options
    must be built and must show large per-world variance first.

Budget fit on Kaggle at ×4.5: a 4-day-horizon C1 rollout is ~96 steps × 2.3 ms ≈ 0.22 s on M1 ≈ 1 s on Kaggle. The
free budget of ~7 s/day at 0.3 s/step affords ~6 rollouts/day, i.e. 1 option × 3 paired seeds per decision dawn with
no overage. Add the bank at ≤5 s per decision dawn for 3 dawns.

## 5. Build plan to a submittable file by 09-30 06:00 UTC (hours from 09-27 00:00 UTC)

| h | work | output |
|---|---|---|
| 0-3 | Fork harness inside the agent. Time-sliced child pool with deadline kill, pipe protocol, fallback to C1's action. Vendored interpreter (`_vendor_kagg.py`, 1,086 lines, no `kaggle_environments` import at runtime). Budget governor driven by `remainingOverageTime`. | `cb_core.py` + unit tests: exactness (fork = real continuation, 10 games × 3 T); deadline kill; no zombie processes |
| 3-9 | Options as C1 overlays, each off by default and switched on only by the planner: **O1** buy the 4th quadrant at the first dawn from day 9 when cash ≥ price + reserve; **O2** geese to 6 (coop builds on spare tiles); **O3** strawberry cap / tomato replant in glut worlds. Each fires-verified (count turns entered/changed/errors, rule 4). | `cand_CB_O{1,2,3}.py` |
| 9-12 | **Kill test 1** (below) | `oracle_O*.jsonl` |
| 12-20 | Planner: decision dawns 9/12/15; paired CRN rollouts (sampled seeds, profile opponent scaled to the observed opponent); horizon 4 days plus terminal value (money + shed at current price + yield-in-field + herd at purchase price). | `cand_CB.py` |
| 20-30 | Gates: vs C1 (fresh 32 unique seeds; the seat swap is an exact duplicate), vs hyb2965, RR anchors via opus's `rr.py`. Budget simulation: M1 time ×4.5 accounting, 50 games, 0 bank breaches. `kaggle_load_check` plus official `env.run` both seats. | gate log |
| 30-36 | **Kill test 2**; package; preflight | file to claude-code |
| 36-54 | Buffer: fixes, re-gate, second seed slice | — |

## 6. Kill tests (pre-registered here, before any result)

**+12 h (09-27 ~12:00 UTC)** — all three must hold, else stop C+B:
1. **Fork works in the real runner.** `kaggle_load_check.py` plus the official `env.run` with the fork harness, both
   seats, 10 games: 0 errors, 0 timeouts, no orphaned PIDs. If `os.fork` is unavailable or unsafe there, stop:
   module-state snapshot is the only fallback, and it is fragile.
2. **Oracle value.** For at least one option, the per-world oracle over 40 fresh seeds is ≥ +$1,000/g. The oracle is
   the mean of max(0, C1+O − C1) under paired games, vs C1 and hyb2965, with shops decoupled via `kag_dc.py` so
   re-rolls do not fake it. T2's is +$225/g; below +$1k there is nothing for a planner to select.
3. **Rollout ranking.** On the worlds where |Δ| > $1k, the 4-day rollout agrees in sign with the true Δ in ≥ 65% of
   worlds.

**+36 h (09-28 ~12:00 UTC)** — the upload bar for slot 2:
- Closed-loop vs C1 **≥ 0.55 over ≥ 32 unique seeds with paired ≥ +$300/g**, and vs hyb2965 not worse than C1's own
  cell.
- Opus's RR map lower bound ≥ C1's point estimate (2088).
- 0 errors and 0 bank breaches over 50 games at ×4.5 budget accounting; load check OK.

Miss any of these → slot 2 goes to the best C1-family variant (C1RS/C1R2 per r4) by claude-code/sonnet's call; no
moonshot exists.

## 7. Probabilities (final standing, if the C+B build is fielded in slot 2)

| | value | basis |
|---|---|---|
| **P(3k+ \| fielded)** | **0.3%** | Nothing measured this round reaches top-family play: TS −$15.5k vs C1; C+B's ceiling is the options' per-world variance |
| **P(top-10 \| fielded)** | **0.4%** | cutoff ~2900-2977; same reasoning |
| **P(beats C1 closed-loop)** | **~20%** (TS ~1%) | Kill test 2 needs options with ≥ $1k/g oracle value plus correct ranking. The project's base rate for chassis changes vs C1 is ~1 in 6, lifted a little because B turns mixed-sign options non-negative |

**What would change my mind upward:** kill test 1 showing any option with ≥ $3k/g per-world oracle value and ≥ 75%
rollout sign agreement. That would be the first evidence that world-fitting can be reached on our executor.

## 8. Files (`moe/r5/build/opusb/`)

| file | purpose |
|---|---|
| `overage_scan.py`, `overage_rawtop.jsonl`, `overage_top0925.jsonl`, `overage_bursts.txt` | top teams' overage use from replays |
| `klogs/episode-113848034-agent-0-logs.json` | C1's per-step durations on Kaggle hardware |
| `bench_engine.py` | engine and C1 cost; deepcopy cost (0.37 ms state+env at day 10) |
| `ts.py`, `tsgame.py`, `ts_{A,NN,C1prof,ALL}.jsonl` | TS planner; closed-loop runs; `--validate` exactness and opponent-model bias |
| `oppprof.py` / `oppprof.json`, `c1prof.py` / `c1prof.json` | opponent market-supply profiles (40 exact top-vs-top games; 10 C1 self-play) |
| `libstate.py` / `libstate.json` | per-dawn tile/cash signatures of 718 library tapes (exact replays) |
| `forkclone.py` | fork-cloned C1 continuation: exactness and cost |
