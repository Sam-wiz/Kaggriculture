# MoE r5 — opus (claude-opus-5-5), round 1: architecture + macro-policy extraction

Written 2026-09-26 20:36–21:30 UTC (`date -u`; last edit 21:26). Foreground only, ≤2 workers, nice 10. No submissions.
Code, data and logs are in `moe/r5/build/opus/`. Everything below was run this round unless a file from r4 is cited.

## 0. Top line

1. **The whole dump is decoded, exact.** 1,773/1,773 top-vs-top games (09-23..25) replay to the dollar.
   - Output: per-seat daily dawn state plus that day's macro decisions (`macro.py` → `macro.jsonl`, 112 MB; family subset `fam.pkl`).
   - Family = 2,176 seats with the exact `COW 1 / WHEAT 5` opening: Vadim, DECEM, Mother-Goose, DSM, M&M&P&Q, mtmr_s1.
2. **The family is one deterministic codebase, versioned, shared by ≥5 teams.**
   - mtmr_s1 never diverges from identical joint histories (0 events in 214 seats, `nondet.py`).
   - The other teams' divergences split by *date*, and the variants are shared across teams (`nondet2.py`): DECEM/Vadim/Mother-Goose share the step-10 CARE/NORTH variant; Vadim/DSM share the step-13 WHEAT 5/2 variant. These are version changes of shared code, not randomness.
   - Compute (opusb's `overage_*.jsonl`): 10–38 s of overage at **step 1 only**, then ~0. That is a one-time heavy init (JIT/compile/model load) followed by a cheap per-step policy.
3. **The family's macro is small and extractable** (`an1.log`, `an3.log`, `layout.log`). It is a fixed schedule plus a near-linear function of revealed-shop demand:
   - **Schedule:** land at steps 149/219/~254; hires 4,4,6,6,6,6,8,9,9,10,11×4,12×12,11×3,10; spend to ~$0 at dawn until d10.
   - **Herd mix:** R² 0.82–0.95 from shop-demand counts (+3.3 cows per milk shop, +3.2 sheep per YARN_STORE, geese fill to ~20 animals).
   - **Crops:** strawberry plantings R² 0.85, carrot 0.75, tomato 0.62.
   - **What doesn't matter:** team identity adds ≈0, cash adds ≈0.

   **The macro half of architecture A is done.** Tables are in `famacro.json`.
4. **At the top, rating is decided head-to-head, not by own bank** (`an2.log`).
   - All six family teams bank $103–107k, yet within-family WR runs from 0.31 (mtmr_s1) to **0.88 (DSM)**.
   - DSM beats clones by **+$5.7k/g**, roughly half from volume (more geese → +$1.8k eggs; more tomatoes) and half from captured price (milk 105.7 vs 101.8, strawberry 136 vs 133).
   - Outside the family: THIRD FARM CLUB and 吃白饭的大肥鱼 bank the most ($109k) but win 0.28–0.32; Boey banks the least ($99.5k) but wins 0.64.
   - **Calibration** (LB 09-26 05:00): family members sit at 2886 (mtmr_s1) to 3058 (DSM). A *faithful* family clone with average family selling ≈ **2,890–3,000**. 3k needs family economy **plus** a head-to-head edge.
5. **The executor is A's critical path, now quantified.**
   - **Labour:** from d10 the family runs ~290 unit-turns/day with 0% idle and 36–41% moves (`labor.log`). It stops at 12 hires because the 13th costs $233/day.
   - **Watering:** it waters only when it matters: bonus window, production day, or missed yesterday. It skips ~50% of pre-bonus plants with 0–5% two-day misses (`water.log`), which is ~7% of its labour saved.
   - **DSX, my new instrument** (day-swap executor test): exec3, our only from-scratch executor, runs the family's own day with the family's own market orders and hands. Result (DSM, 12 games, `dsx_exec3.log`):
     - **d15–d25:** −12 plantings/day, +2 to +6 missed feeds, −3 to −8 cares.
     - **d6:** −7 animals placed. exec3 builds its routes at hour 0, so it cannot serve intraday just-in-time buys.
   - **Prototype:** `fam0` (family opening + exec3 + extracted macro) collapses by d10.
6. **Architecture B's compute wall is gone. kagsim ships, and it can start from any observation.**
   - **Unpatched cp311 linux/x86_64 build:** replays **60/60** recorded top games to the dollar at **12 ms/episode under Rosetta emulation**, 1.2 ms natively on arm64 (`kagsim_check.py`, `kagsim_linux/`).
   - **New `Game.from_obs(obs, seed, shops, opp_private)`**, patched into a copy (`kagsim_src/`). Build a game at a recorded mid-game observation, then replay the recorded tapes:
     - **100/100 exact final banks** (20 games × steps 24/150/300/500/700; `fo_parity.py`).
     - 3.1 ms per from-state rollout to the end, Python-dict actions.
   - **Linux/x86_64 builds of the patched engine for cp310, cp311, cp312 and cp313** are in `kagsim_linux_fo/`. All four import in a manylinux container with `from_obs` present.
     - Not yet parity-tested inside the container.
     - The Kaggle runner's Python version is unknown, so ship all four.
   - **Budget:** Sonnet's §2 used the Python engine (9.25 s per full rollout, so <1 rollout per decision). kagsim is ~750–7,700× faster, so 60 s of overage buys thousands of full-game rollouts.
   - **Caveat for any rollout planner** (`fo_parity_noopp.py`): with the opponent's private state unknown (left empty) and both seats replayed as family tapes, our own final bank errs by median **$30k** (t=150), $15k (t=300), $8k (t=500).
     - The mechanism is the known r4 tape fragility: the opponent's stock-less tape fails its sells, feeds and plants, prices move, and our cash-exact tape cascades.
     - **So the rollout opponent must be modelled as market injections (opusb's `oppprof`), not as a replayed tape, and our candidate tapes must be the robust ones.**
7. **Pick: TS+.** This is opusb's tape-switching dawn planner, running on shipped kagsim over the robust top-tape library, plus:
   - (i) a repair layer built from my macro and executor findings;
   - (ii) C1's market layer taking over sells after d12.

   A-standalone (new executor) is the secondary track. C (C1R2) is the fallback for slot 2. Kill tests: §4. Probabilities: §6.

---

## 1. Evidence, in order of how much it moves the decision

### 1.1 What the family is (answers "what do 3k agents do", mechanistically)

| test | result | file |
|---|---|---|
| exact replay of all 1,773 games | 1,773/1,773 bank-exact | `macro.py`, `macro.jsonl` |
| identical joint history on day 0 → does team T diverge? | mtmr_s1 **0** events (214 seats); DSM 1 event at step 0 (a variant opening); DECEM/Vadim/Mother-Goose events at steps 10/13/21 | `nondet.py` |
| are those divergences random or versions? | split by **date** (DECEM 09-23 NORTH 55 / CARE 91, then CARE only; Mother-Goose 09-23 NORTH only, 09-25 CARE only) and shared across teams | `nondet2.py` |
| within-team per-step identity, grouped by revealed-shop prefix | unit ops 0.5–0.8 and market lists 0.6–0.9 (same code, divergence from weeds, prices and shops) | `ident2.py`, `ident2.json` |
| per-step compute (Kaggle replays) | 10–38 s overage at step 1 only, ~0 afterwards (DSM ×5, Mother-Goose ×2, Vadim, Majkel ×5, M&M&P&Q ×2) | opusb `overage_*.jsonl` |

**Reading.** The top of the LB is dominated by one deterministic, reactive, shop-conditioned agent, run by at least five teams with small version differences. Its per-step policy is cheap. Its step-1 init is heavy, consistent with compiling or JIT-ing a simulator or loading a model; we cannot tell which from replays.

### 1.2 The family macro, extracted (`an1.log`, `an3.log`, `layout.log`, all in `famacro.json`)

**Schedule (2,176 seats):**
- **Land.** The top land-step tuples are (149, 219, 254) ×404 and (149, 219, 253) ×388. Most of the rest also buy NE at step 149; a separate 147/198 two-quadrant variant (135 seats) never buys the 4th.
- **Hires.** The modal schedule above has modal shares of 0.84–0.92 on d0–d9 and 0.5–0.7 afterwards. ~294 hires/game, $6.4k/game.
- **Dawn cash** (median): 6, 3, 9, 34, 430, 833, 53, 138, 2155, 270 on d1–d10. It builds from d11 (2,966) to 97k.
- **Herd bursts** (mean buys): d0 2.0 cows + 3.0 sheep; d6 3.8 cows + 1.1 sheep + 1.7 geese (NE land); d9 1.6 cows + 2.1 geese (SW); d10–11 geese 1.9.
- **Crop timeline (mean seed buys/day):**
  - d0: 10 wheat + 6 melon; d1: 4 melon.
  - d2–4: 10 strawberry; d6: 7.5 strawberry + 6 wheat.
  - d9–d18: tomato 1–3/day. Carrot ramps from 2/day on d12 to 7.6/day on d26.
  - Wheat 6–10/day throughout (feed for ~20 animals).
  - No seeds after d27.

**Shop conditioning.** Linear in D_p, the number of revealed shops demanding product p. Cross-validated R², team dummies vs team + shop demand:

| quantity | mean | R² team only | R² + shop demand | main coefficients (per demanding shop) |
|---|---|---|---|---|
| cows at d12 | 8.6 | 0.00 | **0.82** | +3.32 milk |
| sheep at d12 | 5.9 | 0.00 | **0.95** | +3.24 wool (YARN counts 2×) |
| geese at d12 | 6.1 | 0.06 | **0.69** | −2.68 milk, −2.30 wool (fills the remainder) |
| strawberry seeds d6–15 | 21.2 | 0.02 | **0.85** | +7.77 strawberry |
| carrot seeds d9–27 | 60.2 | 0.01 | **0.75** | +20.5 carrot, +8.9 egg |
| tomato seeds d9–20 | 16.7 | 0.27 | **0.62** | +6.85 tomato |
| wheat seeds d6–27 | 164 | 0.06 | 0.58 | −11 strawberry, −9 carrot (wheat is the filler) |

Adding dawn cash and empty-tile count raises R² by ≤0.04. **The macro is a demand-proportional allocation, not a search result.**

**Layout.** It is stable (`layout.log`):
- ~20 animal tiles hug the shed cross, in family fill order (listed in `famacro.json`).
- Strawberries: NW rows 0–2 and NE rows 0–1. Melons: NW interior (d0–10). Tomatoes: SW west columns.
- Wheat fills near the herd.

**Opening.** Steps 0–23 are identical in 214/214 mtmr_s1 games (`open_mtmr.json`). It buys **just-in-time**: seeds 1–2 at a time right before planting, wheat 1 at a time before feeding. It fires more HIREs than it can afford and lets the engine refuse them. Fertilizer sales (from step 26) fund d1–d5.

### 1.3 What decides rating at the top (`an2.log`)

**Family head-to-head (WR, n, mean margin):**
- **DSM vs** DECEM 1.00 (75, +$5.9k); Mother-Goose 0.98 (55, +$5.4k); Vadim 0.96 (54, +$6.7k); M&M&P&Q 0.65 (46, +$3.9k); Boey 0.39 (28).
- **mtmr_s1** loses to every family team: 0.14–0.45.

**DSM vs family clones (252 games), revenue:**
- Total revenue +$6.4k (138.0k vs 131.6k); bank +$5.7k (106.0k vs 100.3k).
- By product: eggs +1.8k (225 vs 187 units), strawberry +1.5k, tomato +1.4k (119 vs 102 units; $65.5 vs $62.1), milk +1.0k (price only), wheat +0.7k, wool +0.6k (price).

**Consequence:**
- A faithful family clone lands mid-family (~2,900–3,000).
- 3k needs the DSM increment: more geese and tomatoes (macro) plus better captured prices (market layer). Our lineage has measured market skill; the r4 memory notes our captured/held price ratio is *higher* than the top's.

### 1.4 The executor gap (A's critical path)

**Family labour (`labor.log`, 302 seats):**
- **d0–d5:** idle 8–43%; the family finishes by hour ~20.
- **d9–d27:** ~290 unit-turns/day, **0% PASS**, moves 36–41%.
- **Productive mix:** water 0.19, harvest 0.10, feed/care/collect ~0.07 each, plant 0.04, fertilize 0.04.

**Watering rule (`water.log`, 74 games):**

| phase | unwatered at hour 23 | missed two days running |
|---|---|---|
| one-time crops, bonus window | 1–14% | — |
| one-time crops, pre-bonus | 53–55% | 0.00–0.05 |
| strawberry / tomato, pre-production | 38–40% | — |

So the rule is: **water iff it pays today or the plant would die tomorrow.**

**DSX: new instrument (`dsx.py`)**
- **How it works.**
  1. Replay a family game exactly to the dawn of day d.
  2. For day d, keep the family's market orders but let the candidate drive the units. The candidate is told the family's own plan (tiles it planted, animals it placed that day).
  3. Score next dawn against the family's real day: missed waters, missed feeds, care banked, plants and animals, and value (money + products at base).
- **Determinism check:** the family vs itself gives Δ = 0.
- **Cost:** ~0.1 s per test.

**exec3 baseline (DSM, 12 games × 6 days):**

| day | family miss_f / care | exec3 miss_f / care | exec3 plantings vs family | exec3 animals vs family |
|---|---|---|---|---|
| 6 | 6.3 / 18.0 | 2.1 / 14.0 | −11.9 | **−7.3** |
| 10 | 1.2 / 43.0 | 3.6 / 36.6 | −6.8 | −3.4 |
| 15 | 2.3 / 33.6 | **7.9** / 26.1 | **−12.8** | −1.1 |
| 20 | 6.9 / 22.1 | 8.3 / 19.0 | −11.5 | −1.3 |
| 25 | 2.8 / 22.9 | 4.4 / 19.5 | −12.6 | −1.7 |

Vadim's games give the same picture (`dsx_exec3_vadim.log`).

- **Missed waters look better for exec3 early**, but only because it waters everything and falls behind on everything else.
- **The dval column is confounded early:** unplanted purchases sit idle. Read it only for d15+, where it is **−$2.9k to −$3.5k per day**.
- **Reading:** a from-scratch executor at family parity means just-in-time buy/serve coupling, smart watering, and no route rebuild latency. That is ≥20–30 h of work with no guarantee. It is the reason A is not my primary.

**Prototype `fam0.py`** (family day-0 tape + exec3 + extracted macro + trickle sells):
- The opening matches the family exactly: dawn d1 has 10 wheat, 6 melons, 2 cows, 3 sheep.
- From d2, exec3 plus my naive macro loses feed and watering coverage: 17–25 weeds by d10, herd lost, final $1.7k vs PASS (`run0.py`).
- It is kept only as a harness skeleton.

### 1.5 kagsim ships: the B budget wall falls (disputes sonnet §2's conclusion, not its numbers)

- **Build.** `docker run --platform linux/amd64 python:3.11-slim` + `g++ -O3 -std=c++17 -shared` on `kaggriculture-cppsim/python/kagsim.cpp` → `moe/r5/build/opus/kagsim_linux/kagsim.cpython-311-x86_64-linux-gnu.so` (431 KB).
  - Wall time 6m45s, mostly apt and emulated compile.
  - Source: destbreso's public repo, built on nikital7's public Kaggle notebook.
- **Check** (`kagsim_check.py`, recorded tapes both seats):

  | build | exact | speed |
  |---|---|---|
  | linux x86_64 cp311, under Rosetta | 60/60 | 12.15 ms/episode |
  | macOS arm64 | 60/60 | 1.17 ms/episode |

  - Sonnet's Python engine: 2.3–12.9 ms per *frame*, 9.25 s per full rollout.
  - kagsim: ~1–12 ms per full 720-step rollout.
- **`Game.from_obs`: done this round** (`kagsim_src/python/kagsim.cpp`, ~150 added lines).
  - **Why it's clean:** the engine reseeds its RNG every day from `(seed*1000003) ^ day` (`sim.hpp:840`). So `State` + `Config` is the whole simulator state, and a mid-game constructor only needs:
    - both farms' tiles, money, positions, quadrants and hires (observable);
    - our shed, seeds and inventories in dict insertion order (observable);
    - the opponent's private state (unknown; pass it or leave it empty);
    - market inventory and prices, revealed shops plus a pinned or sampled future, and step/day/hour.
  - **Parity** (`fo_parity.py`): 100/100 exact final banks from steps 24–700 when both privates are given.
- **Still open:**
  - (a) Which Python the Kaggle agent runner uses. I built cp310–cp313 (`kagsim_linux_fo/`, 10.7 min in one manylinux container). Fallbacks: compile with g++ at step 0 if present (the family's own step-1 cost is 10–38 s), then the Python engine with small M×R.
  - (b) The multi-file submission must put its own dir on `sys.path` before `import kagsim`, and must pass `kaggle_load_check.py`. Not done yet.
  - (c) An in-container parity run of the linux `from_obs` builds (needs kaggle-environments 1.32.7 in the container, ~10 min).

## 2. Architecture pick

| | what it needs by 09-30 | measured blocker | verdict |
|---|---|---|---|
| **A** macro imitation + our executor | new executor at DSX parity (~20–30 h) + macro (done) + sell layer (C1's) | exec3 at −12 plantings, +5 missed feeds/day mid-game; from-scratch history exec3 $35k vs V48 $96k | **secondary track**: its parts (macro tables, watering rule, DSX, JIT-buy pattern) feed TS's repair layer. Stand-alone only if TS dies at K1 **and** a second builder (codex) is free |
| **B** runtime planning | a fast engine in the submission + candidate plans + an opponent model | Python engine too slow (sonnet) → **kagsim linux builds + `from_obs` (exact) remove this** (§1.5); the opponent model is now the binding constraint | **primary, as TS+**: candidate plans = robust top tapes (their executor is top-level for free); kagsim rollouts measure splice damage from our real state |
| **C** C1 chassis + macro corrections | 4th quadrant, geese, tomato cycle on a 3-quadrant tape | structural ports failed (09-21); T2/T2E ceilings 0.587 < 0.74 (r4 opusb) | **fallback**: C1R2 already exists (RR 2152 [2021, 2294]); it is slot 2's floor if TS+ fails its gates |

**Why TS+ over A.** The two things a 3k agent needs are top-level *execution* and a head-to-head *market edge* (§1.3).
- **Execution:** TS inherits it from recorded top tapes. A has to build it (§1.4).
- **Market edge:** neither has it natively.
  - TS's tapes sell open-loop, and THIRD FARM CLUB / 吃白饭的大肥鱼 show that tape-grade economy alone yields WR ≈ 0.3 at the top.
  - Our lineage's one proven asset is the market layer (SIR/PREDICT). So TS+ should use C1's sell layer.
  - That layer should take over only after d12, when dawn cash is ≥$6k (`famacro.json`). Before that, cash-lean tapes break if our sells lag theirs.

**What TS+ must beat.** The r4 evidence is against tape transplants: raw tapes 8/125, TFC router 16/66, dawn-9 states 13.5 tiles apart within a 2-shop group. But r4 also measured the ceiling: with shops matched, robust tapes win **25/28, +$15.1k** vs C1, and the value is front-loaded in the first four shops (k=4 → 0.89).
- TS re-plans at every dawn **from our actual state** with rollouts.
- That is the "planner that re-plans at each shop unlock" the r4 memory said a 3k path requires, not a lookup router.
- The open question is whether splice damage eats the in-world +$15k. K1b tests exactly that.

**TS+ components** (owner in brackets):
1. **kagsim in the submission** [opus r2 + claude-code]: the cp310–313 builds exist (`kagsim_linux_fo/`). Still to do: loader shim, g++ fallback, `kaggle_load_check.py` preflight.
2. **`Game.from_obs`**: done, 100/100 exact (§1.5).
3. **TS core on kagsim** [opusb]: port the rollouts from the Python engine to `kagsim.Game.from_obs(...)` + `step`.
   - Library: robust seats only (Boey 159, THIRD FARM CLUB 150, 吃白饭的大肥鱼 199, Majkel1337 210). Their dawn cash is also lean ($2–400 on d1–d4), so robustness must be *measured* per tape (r4 `brk.py`), not assumed.
   - Candidates filtered by revealed-shop prefix.
   - R futures: unrevealed shops sampled uniformly (with replacement) plus a weed RNG.
   - **Opponent model: market injections** (opusb's `oppprof`), **not** a replayed tape. A stock-less replayed opponent tape corrupts our own rollout bank by a median $30k at t=150 (§1.5).
     - Use the observed opening/version (the family is deterministic on d0) only to *choose* the injection profile.
     - Rank candidates on paired rollouts (same futures, same opponent profile), because absolute rollout banks are biased.
4. **Repair layer** [opus → opusb]. When a tape unit op is dead in our state (WATER on an empty tile, PLANT on an occupied one, FEED with no animal), substitute a greedy local task using the family watering rule and a feed guard. Add a cash guard: skip tape buys that would leave less than the feed reserve.
5. **Market layer** [opusb]: tape sells ≤ d12; C1 SIR/PREDICT sells after d12. Buys stay with the tape.

## 3. Build plan (now 09-26 21:30 UTC; file due 09-30 06:00 = T+80.5 h)

| window (UTC) | work | owner | hours |
|---|---|---|---|
| ~~09-26 21:30 → 09-27 02:00~~ **done 21:25** | kagsim cp310–313 linux builds + `Game.from_obs` + parity (100/100) | opus | — |
| 09-26 21:30 → 09-27 00:30 | loader shim + stub agent through `kaggle_load_check.py` + in-container linux parity | opus | 3 |
| 09-26 22:00 → 09-27 04:00 | TS core ported to kagsim rollouts; library index by shop prefix; injection-profile opponent model | opusb | 6 |
| 09-27 06:00 → 09:30 | **K1** (below) | sonnet runs, opus/opusb fix | 3 |
| 09-27 09:30 → 21:30 | repair layer + cash guard + d12 hand-off to the C1 sell layer; DSX splice audit per switch | opus + opusb | 12 |
| 09-27 21:30 → 09-28 09:30 | **K2** (below); codex joins (cap lifts ~21:53) → second-opinion build or A-executor track if K1 was marginal | all | 12 |
| 09-28 09:30 → 09-29 12:00 | tuning (M, R, switch margin, plan days), 2× CPU-slowdown timing, both seats, full RR map | opusb + sonnet | 26 |
| 09-29 12:00 → 18:00 | freeze; final preflight on the official env; package | claude-code | 6 |
| 09-30 06:00–08:00 | upload into slot 2 (hyb2965's) if K2 holds, else C1R2 | claude-code | — |

## 4. Kill tests

**+12 h (09-27 09:30 UTC):**
- **K1a (ship):** the stub agent imports the bundled kagsim in `kaggle_load_check.py`, and a 720-step official-env game with ≥200 kagsim rollouts at dawns uses ≤20 s total overage. Fail → B is dead for 09-30; slot 2 = C1R2.
- **K1b (splice):** TS on kagsim (no repair, tape sells) vs C1 closed loop.
  - Setup: natural shops, 20 unique seeds (kagsim `sw=0`; seat-swap rows are duplicates, r4 opusb).
  - Pass: **≥ 8/20 wins**. For reference, raw robust tapes win 0.09 on natural shops and the in-world ceiling is 0.89.
  - **Kill TS if ≤ 4/20.** Marginal (5–7/20): continue only if the DSX splice audit shows the loss is repairable (dead ops, not bad plans).

**+36 h (09-28 09:30 UTC):**
- **K2 (upload bar ii plus direction):** TS+ vs C1 **≥ 15/20 and median margin ≥ +$8k** (in-world tapes do +$15.1k); vs hyb2965 and shepherd ≥ 0.7.
  - Full lineage RR, mapped via `c1map.py` (the only instrument that retrodicts): **≥ 2148** (bar ii: not worse than C1 + 60).
  - 0 errors and 0 timeouts in both seats. Fail → slot 2 = C1R2.
- **K2d (descriptive only, not a gate):** matched-world bank vs recorded robust-tape opponents with shops pinned. Their tapes drift only ~$0.4–0.7k under substitution; family tapes collapse, so never use family tapes as opponents. Read it as "are we in the top economy class", not as a rating.

## 5. What I do next (round 2, ≤2 workers)

1. Loader shim: `sys.path` = submission dir, then import the matching `kagsim.cpython-3XX-x86_64-linux-gnu.so`, then g++ fallback, then Python-engine fallback. Run a stub agent through `kaggle_load_check.py`, plus an in-container parity run of the linux `from_obs` builds (K1a).
2. Hand opusb the from-state rollout API: `kagsim.Game.from_obs(obs, seed, shops, opp_private)` from `moe/r5/build/opus/kagsim_src/` (mac `.so` for local runs; `kagsim_linux_fo/` for the submission).
3. Robust-tape library index (shop prefix → seats; per-tape breakage from r4 `brk.py`), and a paired-rollout ranking check.
   - Test: do kagsim rollouts with an injection-profile opponent rank candidate tapes the way the real closed-loop outcome does? This is the planner's own retrodiction. Pre-register it before K1b.
4. Repair-layer spec and code from §1.4 (watering rule, feed guard, JIT seed purchase), validated with DSX on spliced states.

## 6. Probabilities (as of 21:30 UTC)

- **P(TS+ passes K2 by 09-29 12:00) ≈ 30%.** This is "it beats C1 closed-loop at the upload bar". P(beats C1 > 0.5 at all) ≈ 50%.
- **P(3k+ | fielded in slot 2) ≈ 7%.** Fielded means it passed K2. The family itself spans 2,886–3,058, so a top-economy agent without a DSM-grade market edge lands ~2,850–2,950. An agent at the K2 bar (+$8k vs C1) sits below the in-world tapes (+$15k).
- **P(top-10 | fielded) ≈ 15%.** The #10 cutoff is ~2,904.
- **Unconditional P(3k+) ≈ 2%** (0.30 × 0.07). That is up from r4's 0.2%, for two measured reasons: the B compute wall is gone (§1.5), and the target is one deterministic family whose macro is linear in shop demand (§1.1–1.2).
