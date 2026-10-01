# MoE r6 — opus (claude-opus-5-5), round 1: decode of LB ranks 1–10

Written 2026-09-27 14:45–15:07 UTC (`date -u`). Foreground only, ≤2 workers, nice 10. No submissions.
Code, data and logs: `moe/r6/build/opus/`. **Per-team tables and the H2H matrix: `build/opus/teams_1_10.md`.**

## 0. Top line

1. **Coverage.**
   - **Ranks 1–8:** decoded from 1,773 top-dump games (09-23..25) plus the 101 games of 09-26 that had landed by ~15:05 UTC.
     - Every replay is bank-exact: 1,773/1,773 (r5 `macro.jsonl`) and 101/101 (`build/opus/macro26.jsonl`).
   - **Ranks 9 and 10** (Just A game on your lips, 2897; Anton Tikhonov, 2884) have **0 games** in any dump.
     - The dump samples top-rated episodes (median player ~2970). Teams near 2850–2900 barely appear: #11 KawattaTaido has 4 games, #12 Azat 43.
     - They stay undecodable until the 09-26/27 pulls contain them. The tooling is ready (§7).
2. **The top 8 are four codebases, not eight.** Evidence: `rawan.log`, `h2hdiv.log`.
   - **The family core — Vadim, DSM and Mother-Goose — is one codebase.**
     - The three teams share day-0 unit tapes: 85% of DSM's seats play a day-0 tape that Vadim also plays, and 92% of Vadim's seats play one that DSM plays.
     - In 38/56 DSM–Vadim games the two seats play *identically* through step 22 or later. The other 18 differ at step 1: DSM's extra-sheep opening variant.
   - **The forks share the family's market and macro but differ from step 1–4:**
     - **DECEM** runs its own executor. It issues `["PLACE","COW"]` with no count and routes hands differently. The first divergence from Vadim is at step 4 in 84/84 games.
     - **M&M&P&Q** adds extra sheep at step 1.
     - **mtmr_s1** is a third executor.
   - **Independent codebases:**
     - **Boey:** randomised planner.
     - **Majkel1337:** the oldest lineage.
     - **Fourth Quadrant:** an agent with no geese and no tomatoes.
3. **The LB order is not the head-to-head order** (`teams_1_10.md` matrix, 09-23..26):

   | team | LB rank | WR vs rest of top 20 | notable results |
   |---|---|---|---|
   | DSM | #6 | **0.86** (n=311) | 79-0 vs DECEM |
   | Boey (real agent) | #2 | 0.75 (114) | |
   | Fourth Quadrant | #8 | 0.62 (94) | |
   | M&M&P&Q | #3 | 0.54 (243) | |
   | DECEM | #1 | 0.45 (336) | |
   | Mother-Goose | #7 | 0.41 | |
   | Vadim | #4 | 0.31 | |
   | Majkel1337 | #5 | 0.28 | |

   - **DSM fell from 3058 (09-26 05:00) to 2944** while its dumped agent went 20/25 against the top 20 on 09-26.
   - A new DSM day-0 version appeared on 09-25 (40/129 seats). On 09-26 DSM shows **3 day-0 fingerprints** (17/6/1 of 24; `versions2.log`).
   - Inference (submission IDs are not in the dumps): the LB is showing a newer DSM submission that is still converging.
4. **Boey's "−$11k mean margin" was a broken second submission, not Boey.**
   - **The broken one:** day-0 tape 30886, 30 games on 09-23/24. It won 0, with median margin −$75.6k and median bank $58.7k, and was gone by 09-25.
   - **The real agent:** WR 0.78, mean margin +$4.2k. It has the best H2H of anyone except DSM.
   - **It is randomised:** in 66 games against *identical* opponent day-0 play, it produced 66 distinct day-0 tapes, and all 135 pairs diverge at step 2 (`boey_stoch.log`).
   - **Its wheat/fertiliser churn is P&L-neutral, now measured exactly with fills** (`churn.py`): same-step round trips come to **+$25/g** for Boey and +$9/g for Fourth Quadrant.
   - **Its edge over the family:**
     - costs about $3k/g lower: hires −$1.1k, seeds −$1.3k (no tomatoes), animals −$0.6k;
     - plus eggs and milk revenue (+$5.4k);
     - it does *not* come from churn (`counterfam.log`).
5. **Nobody at the top conditions on the opponent.**
   - Every team's macro is shop-conditioned. Cross-validated R² is 0.55–0.81 for the family cores' cows, sheep, geese, strawberries and carrots, and 0.37–0.77 for tomatoes. It is lower for Boey (cows 0.41, geese 0.26) and for M&M's tomatoes and geese (≈ 0–0.1).
   - Adding the opponent's herd, plants and family flag at ≤ d6 gains **≤ 0.04 R² on every herd/crop target with real variance, for every team** (`dossier.log`).
   - The largest gain anywhere is +0.08, on d10–29 hires, which are barely predictable to begin with (R² ≤ 0.26).
   - Collisions are a property of shared code:
     - the family collides on **45–53%** of premium sell-steps against other family teams, and 26–32% against everyone else;
     - Boey collides on 11–19%.
6. **Implication for us (stated plainly): the top-10 decode yields no lever for C1/C1R2 before 09-30.**
   - Every edge found is production- or executor-level: 4th quadrant, tomatoes, geese, strawberry mix, labour routing, randomised planning.
   - Each of these is already measured dead as a graft on our tape executor: HANDOFF §5 #1/#2/#21/#26, and r5 O1/O2/O3 (−$9k..−$17k/g; O3 ceiling +$109/g).
   - The top 10 never meet us: we sit at 2076–2152 RR-mapped, and matchmaking is by rating. So a counter-strategy against them has **zero medal value**.
7. **The only cheap untested item is negligible.**
   - The family lets its sheep go at the end: 6.4 at d20 → 0.8 at d29. C1 keeps all 7.5 to the end.
   - Arithmetic puts it at about +$15–25 per sheep, **≤ +$150/g** (§5). It is not worth a slot.

---

## 1. Data and instruments

| what | how | file |
|---|---|---|
| per-seat daily macro (dawn state + day's fills) | exact replay with ledger hooks (r5 `macro.py`); 09-26 re-run into my dir | r5 `macro.jsonl`, `fam.pkl`; `build/opus/macro26.jsonl` |
| per-team dossier (record, H2H, lineage, macro, market, reactivity) | `dossier.py` over `fam.pkl` | `dossier.log`, `dossier.json` |
| raw tape scan (per-step unit/market hashes, order mix, sell hours, collisions) | `rawscan.py` (19 s, 2 workers) | `rawscan.pkl` |
| lineage, market style, identity, collisions | `rawan.py` | `rawan.log`, `rawan.json` |
| first divergence between the two seats of a head-to-head game (symmetric farms ⇒ first difference = code difference) | inline | `h2hdiv.log` |
| version fingerprints by date (one crc hash over all dates; `versions.log`/`d26.log` used different hashes and are superseded) | inline | **`versions2.log`** |
| Boey randomisation test (opponent day-0 tape held identical) | inline | `boey_stoch.log`, `stoch.log` |
| exact churn P&L from fills (BUY_PRODUCT vs SELL, same-step round trips) | `churn.py`, 238 games | `churn.jsonl` |
| revenue/cost decomposition vs family opponents | inline | `counterfam.log` |
| Boey / others margin distribution | inline | `boey_fq.log` |
| per-team markdown tables + H2H matrix (Boey's broken submission excluded) | `tables.py` | `teams_1_10.md` |
| compute signature | opusb r5 `overage_*.jsonl` (Kaggle replays, 52 seats) | — |

**Caveat, which applies everywhere:** team ≠ submission. Each team runs up to 2 active submissions, and the dumps do not carry submission IDs. I separate versions by day-0 fingerprint and date (`versions2.log`). "Team WR" is a mix of whatever the team had active on 09-23..26.

---

## 2. Lineage map (ranks 1–8 + the three most-seen others)

| cluster | members | shared-code evidence | differs by |
|---|---|---|---|
| **Family core** | Vadim, DSM, Mother-Goose | op1 `COW 1, WHEAT 5` 100% (DSM also has a +sheep variant in 45/363). Share of seats whose day-0 unit tape is also played by the other team: DSM→Vadim 0.85, Vadim→DSM 0.92, Vadim→M-G 0.92, M-G→Vadim 0.47. Market channel equal for ~26 steps. M-G runs one version behind (its 09-25 day-0 = the core's 09-23). | DSM↔Vadim first differ at step 22 (hand `PASS` vs `SOUTH`) / step 42 (`PASS` vs `WATER`): executor tuning, not macro. M-G↔Vadim median step 14 |
| **Fork: DECEM** | DECEM | Same op1 in 457/457 and the same macro schedule (land 149/219/253–254, hires 4,4,6,6,6,6,8,9,9,10,11–12). Market channel equal to the core for ~5 steps | **Own executor**: step 4 `["PLACE","COW"]` (no n) + `WEST,WEST,NORTH,WEST` vs core `["PLACE","COW",1]` + `NORTH,NORTH,NORTH,WEST` in **84/84** DECEM–Vadim games. 0% day-0 tape overlap with the core |
| **Fork: mtmr_s1** (#21) | mtmr_s1 | Market equal to the core for 25–26 steps | Third executor: step 4 `WEST×4` |
| **Fork: M&M&P&Q** | M&M&P&Q | op1 = core + `SHEEP 1, SHEEP 1` (154) / `SHEEP 2` (92) / plain (25) | 3-quadrant variant (147/198); many versions (23–35 day-0 tapes/day) |
| Independent | **Boey** | `WHEAT 3 + HIRE×5 …` start, shared with THIRD FARM CLUB (r4). THIRD FARM CLUB's day-0 tapes cover 19% of Boey seats (the broken submission) | Randomised; NOOP spacers; ~7 orders/step |
| Independent | **Majkel1337** | op1 `COW 1, SHEEP 2, WHEAT 2` (148) or `HIRE×5, COW 1, SHEEP 1…` (46). In the archive since ep ~107.4M (r4) | — |
| Independent | **Fourth Quadrant** | op1 = five single `BUY_SEED MELON 1` | No geese/eggs/tomatoes; every SELL is exactly 10 units |

- **No public agent file matches any of them** beyond step 1–2 (r4 `fp1.jsonl`, 605 files).
- **Compute** (Kaggle replays; opusb r5): a one-time step-1 init, then < 1 s/step with 0 overage.

  | team | step-1 init |
  |---|---|
  | M&M&P&Q | 37–38 s (heaviest) |
  | Majkel1337 | 12–24 s |
  | DSM | 10–19 s |
  | Boey | 13–18 s |
  | Vadim | 16 s |
  | Mother-Goose | 12 s |
  | DECEM, Fourth Quadrant | no replay |

- **Consequence for Boey:** its per-game randomisation happens inside the 1 s/step budget, so a sampling planner is plausible. That is an inference.

---

## 3. Head-to-head matrix (row WR vs column, n; 09-23..26; Boey's broken submission excluded)

| row \ col | DECEM | Boey | MMPQ | Vadim | Majkel | DSM | MGoose | 4thQ | vs top-20 | all |
|---|---|---|---|---|---|---|---|---|---|---|
| **DECEM** #1 | — | 0.29 (24) | 0.21 (38) | 0.73 (88) | 0.91 (23) | **0.00 (79)** | 0.59 (49) | 0.35 (20) | 0.45 (336) | 0.57 |
| **Boey** #2 | 0.71 | — | 0.72 | 1.00 (9) | 1.00 (4) | 0.65 (34) | 0.86 | 0.67 (3) | **0.75 (114)** | 0.78 |
| **MMPQ** #3 | 0.79 | 0.28 | — | 0.67 | 0.68 | 0.29 (56) | 0.48 | 0.64 | 0.54 (243) | 0.61 |
| **Vadim** #4 | 0.27 | 0.00 | 0.33 | — | 0.65 | 0.04 (57) | 0.39 | 0.20 | 0.31 (324) | 0.48 |
| **Majkel** #5 | 0.09 | 0.00 | 0.32 | 0.35 | — | 0.00 (21) | 0.30 | 0.33 | 0.28 (144) | 0.48 |
| **DSM** #6 | **1.00 (79)** | 0.35 (34) | 0.71 | 0.96 | 1.00 | — | 0.98 (55) | 0.57 (7) | **0.86 (311)** | 0.88 |
| **MGoose** #7 | 0.41 | 0.14 | 0.52 | 0.61 | 0.70 | 0.02 | — | 0.32 | 0.41 (280) | 0.52 |
| **4thQ** #8 | 0.65 | 0.33 | 0.36 | 0.80 | 0.67 | 0.43 | 0.68 | — | 0.62 (94) | 0.65 |

Full matrix with n and the extra columns (mtmr_s1, THIRD FARM CLUB, 吃白饭的大肥鱼, Kaggledew): `teams_1_10.md`.

**Reading.**
- **Top-20 H2H and LB order disagree.** The ratings shown on the LB cannot belong to the agents that played these games at these win rates.
- **Most likely explanation:** version churn (`versions2.log`, one hash over all dates).
  - **DSM** introduced a new day-0 version on 09-25 (40/129), dominant on 09-26 (17/24), plus a third fingerprint (6/24).
  - **Vadim** phased out its sell-all orders (any SELL with n ≥ 100): 169/169 games on 09-23, 151/151 on 09-24, 119/157 on 09-25, 4/32 on 09-26.
  - **Mother-Goose** kept its 09-25 day-0 version (12/16) but went 0/14 vs the top 20 on 09-26. That points to a later-game change, or to opponents' updates; small n.
- **DECEM has been one version since 09-25** (150/152, then 33/33 on 09-26). It is #1 by standing still and beating the field outside the top 20 (0.83, +$5.8k/g), not by beating the top.

---

## 4. Dossiers (numbers from `dossier.log` unless noted; full tables in `teams_1_10.md`)

### #1 DECEM — 3048.8 — family fork (own executor); 457 seats + 35 on 09-26

**Macro:**
- Land 149/219/253–254; 4 quadrants in 402/457 games.
- Hires 296/g ($6.5k), on the family schedule.
- Dawn cash $3–36 on d1–4 (spends to zero).
- Herd at d12: 8.9 cows / 6.1 sheep / 5.8 geese.
- Plants at d20: wheat 23, carrot 7, tomato 17, strawberry 22.
- Tomato seeds 19 on d9–20; melons 11 on d0–1; carrots ramp to 23 per 6-day phase late.

**Market:**
- 1.67 orders/step, 40% of SELL orders are 1 unit.
- Clock-driven (share of sell orders by hour):
  - eggs: h22 (0.30);
  - tomatoes: h22 (0.24);
  - strawberry, milk, wool: h≡1 mod 4.
- Captured price: strawberry 136, melon 215 (+15.4/u vs the opponent in the same game), milk 108, wool 142 (+5.4).
- 23–29% of premium units sold at d25+; melons all sold before d25.

**Reactivity:**
- Shop R²: cows 0.61, sheep 0.69, geese 0.59, strawberry 0.72, tomato 0.77, carrot 0.81.
- Opponent covariates add +0.00 on herd/crop targets (+0.08 on late hires).
- Unit identity between its own games: d0 0.79, d3–9 0.10, d10–29 0.03.

**H2H:**
- 0.45 vs the top 20: 0/79 vs DSM, 0.21 vs M&M, 0.29 vs Boey, 0.35 vs Fourth Quadrant.
- Beats Vadim 0.73, Majkel 0.91, mtmr 0.84.
- 09-26: 16/32 vs the top 20.

**Adopt / exploit:**
- Nothing portable: its edge is the family macro plus executor, dead as a C1 graft.
- Exploit only if met: the h22 egg/tomato dumps are predictable. Pre-selling at h21 is the §5 #6/#21 class, measured −EV in our mirrors. Untestable on our RR map (no DECEM agent).

### #2 Boey — 3034.5 — independent, randomised; 159 seats (129 real + 30 broken) + 15 on 09-26

**Broken submission (09-23/24):**
- Deterministic tape 30886, 30 games, **0 wins**, median margin −$75.6k.
- Boey's own bank $58.7k while the opponent banks $147.8k.
- It falls behind from d15 (dawn cash $14.5k vs $31.4k for the real agent). The opponent's inflated bank suggests it benefits from Boey's missing supply (inference).

**Real agent (`boey_stoch.log`):**
- Randomised from step 2: 66/66 distinct day-0 tapes against identical opponent play.
- Macro:
  - 3 quadrants (145/199–217; 135/159 games).
  - Hires 282/g ($5.0k).
  - Dawn cash $14–40 on d3–d10.
  - Herd at d12: 6.9 cows / 6.4 sheep / 5.0 geese.
  - Strawberry seeds 21 on d6–15; ~0 tomatoes; melons 13.
  - Less shop-conditioned than the family: cows R² 0.41, geese 0.26.
- Market:
  - ~7 orders/step, with NOOP spacers.
  - Wheat 2,130 bought / 2,373 sold; fertiliser 487 bought / 717 sold. Round-trip P&L +$25/g (`churn.jsonl`).
  - Premium sells spread over the clock: the top hour takes 6–12% of orders.
  - Collisions 0.11–0.19.
  - Captured price: strawberry $148–150 (best), wool 114–117 (−$24.9/u vs the opponent), melon 195–199.

**H2H (real agent):**
- 0.75 vs the top 20 (n=114).
- DECEM 0.71, M&M 0.72, DSM 0.65 (34), Mother-Goose 0.86.
- 09-26: 10/14 vs the top 20.

**Why it beats the family** (`counterfam.log`, 95 games): bank +$3.1k.
- Costs about $3k lower: hires −$1.1k, seeds −$1.3k, animals −$0.6k.
- Eggs +$3.3k, milk +$2.2k.
- Offset by tomatoes −$9.1k (it grows none) and strawberries −$1.9k.

**Adopt:**
- Its shape is the closest top analogue to C1: 3 quadrants, no tomatoes, similar cow/sheep counts.
- It differs in geese (5 vs C1's 2.7) and strawberries (22 vs C1's 33).
- Both differences are herd/crop-mix grafts, dead on our tape (§5 #1/#2; O1-goose −$9.2k/g).
- Nothing portable.

**Exploit:** its weak wool capture. Irrelevant: we never meet it.

### #3 M & M & P & Q — 2979.1 — family fork (extra sheep, 3 quadrants); 279 seats + 19 on 09-26

**Macro:**
- op1 = core + sheep; land 147/198, with a 4th quadrant at 289–313 in 25% of games.
- Herd at d12: 7.8 / 6.2 / 4.9.
- Tomato seeds 4.5; strawberry 24.
- Hires 282/g ($5.3k).

**Market:**
- 1.23 orders/step; captured milk +$7.0/u vs the opponent (the best), wool +5.1.
- Heaviest step-1 init: 37–38 s.
- Many versions: 23–35 day-0 tapes per day; unit identity at d0 only 0.37.

**H2H:**
- 0.54 vs the top 20.
- Beats the 4-quadrant cores (DECEM 0.79, Vadim 0.67) and Fourth Quadrant 0.64 (+$17.2k mean margin on 09-23..25).
- Loses to DSM 0.29 and Boey 0.28.

**For us:** the 3-quadrant fork beating the 4-quadrant cores agrees with r5's natural experiment (4q − 3q = +$187 ± $454/g) and O1's death. **Keep C1 at 3 quadrants.** Nothing to adopt.

### #4 Vadim Vasilenko — 2962.8 — family core; 477 seats + 34 on 09-26

**Macro:**
- 4 quadrants in 412/477.
- Herd at d12: 8.8 / 5.5 / 6.9.
- Tomato seeds 17.7.

**Market:**
- It was the only team issuing "sell all" orders (any SELL with n ≥ 100). The share of games with one fell 100% → 76% → 12% over 09-23..26. The day-0 tapes are unchanged, so this is a later-game policy change.
- Captured melon +$22.8/u vs the opponent (the largest), strawberry +4.1.

**H2H:**
- 0.31 vs the top 20: DSM 0.04, DECEM 0.27, Fourth Quadrant 0.20, M&M 0.33.
- It was the family's weakest core version on 09-23..25.
- On 09-26 (new sell policy) it went 16/29 vs the top 20.

**Adopt / exploit:** nothing new.

### #5 Majkel1337 — 2955.0 — independent (oldest); 210 seats + 2 on 09-26

**Macro:**
- 3 quadrants (146/199; 195/210).
- Herd at d12: 7.5 / 5.5 / 4.2.
- Tomato 9.6; strawberry 23.7 (shop R² 0.80).
- Hires 283/g.

**Play style:**
- The highest d3–9 self-identity of the top 8: 0.31, vs ≤ 0.16 for the family (d0 0.71).
- The best strawberry capture of the non-Boey teams ($150–151.5).

**H2H:**
- 0.28 vs the top 20; it loses to *every* family team (DSM 0/21, DECEM 0.09).
- Wins 0.90 against teams outside the top 20: its LB rank comes from the field.
- Compute: 12–24 s init.

**Adopt / exploit:** nothing.

### #6 DSM — 2944.3 — family core, H2H king; 363 seats + 25 on 09-26

**H2H:**
- 0.86 vs the top 20 (n=311): DECEM 79-0, Vadim 0.96, Mother-Goose 0.98, Majkel 21-0.
- Loses only to Boey (0.35) and Fourth Quadrant (0.57, n=7).
- 09-26: 20/25 vs the top 20.

**Edge vs family clones:** +$5.7k/g (r5 `an2.log`).
- Eggs +$1.8k (38 more units).
- Tomatoes +$1.4k.
- Strawberries +$1.5k.
- Milk/wool price +$1.0k/+0.6k.

**The first code difference from Vadim is executor-level:** step 22 `PASS` vs `SOUTH`, step 42 `PASS` vs `WATER`. That is r5's "water iff it pays today or the plant would die tomorrow", i.e. labour thrift.

**Versions:** a new day-0 version (unit and market) appeared on 09-25 in 40/129 games and was dominant on 09-26 (17/24), alongside a third fingerprint (6/24) (`versions2.log`).

**LB:** 3058 → 2944 in 34 h despite the above. Inference: the LB is showing a newer submission.

**Adopt:** its edge is executor labour thrift and more geese. Freed labour on a tape executor does not get re-used (§5 #25). Dead.

### #7 Unknown Mother-Goose — 2933.5 — family core; 394 seats + 16 on 09-26

**Macro:** 4 quadrants in 262/394; herd at d12: 8.6 / 6.0 / 5.8.

**Market:** clock-driven; eggs h22 in 0.50 of sell orders (the most fixed of all).

**Lineage:** it runs one version behind the core. Its 09-25/26 day-0 fingerprint is the one Vadim and DSM ran on 09-23.

**H2H:**
- 0.41 vs the top 20: DSM 0.02, Boey 0.14.
- Beats Vadim 0.61, Majkel 0.70.
- 09-26: 0/14 vs the top 20, with its 09-25 day-0 version unchanged. Small n; opponents updated.

**Adopt / exploit:** nothing.

### #8 Fourth Quadrant — 2932.9 — independent, new (first game 09-23, 32 on 09-24, 87 on 09-25); 120 seats + 10 on 09-26 (8/10 vs the top 20)

**Macro:**
- The earliest complete farm of anyone: 4 quadrants at 146/198/249 in 120/120 games.
- **0 geese, 0 eggs, 0 tomatoes.**
- Herd at d12: 9.6 cows / 6.6 sheep.
- The most wheat on the board: 34–48 plants at d15–d25; 84 wheat seeds on d6–11.
- Hires 295/g; 0% PASS; weeds 3.3 at d20 (the highest).

**Market:**
- BUY_PRODUCT is 52% of its orders: wheat 1,370 bought / 1,932 sold; fertiliser 947 / 1,182. Round-trip P&L +$9/g.
- Every SELL is exactly 10 units.
- Captured melon +$19.8/u vs the opponent.
- Deterministic within day 0 (own divergence median step 73; versions explain the rest).

**H2H:**
- 0.62 vs the top 20: beats Vadim 0.80, DECEM 0.65, Mother-Goose 0.68.
- Loses to M&M 0.36 (mean margin −$17.2k on 09-23..25) and Boey 0.33.

**Adopt:** the proof that a no-goose, no-tomato plan reaches #8 is the same shape as C1's. The edge is its 4-quadrant wheat economy, which is dead as a graft (O1, §5 #28).

### #9 Just A game on your lips (proptiter) — 2897.4; #10 Anton Tikhonov (itwastony) — 2884.4

- **0 games** in 1,773 (09-23..25) + 101 (09-26) dump games. There is no replay from which to decode an opening, a macro or a market policy.
- Absence does not prove they are new: dump coverage thins sharply below ~2900 (see §0.1).
- I will not guess a lineage.
- **Next action (opus):** re-run `macro.py` + `dossier.py` + `tables.py` over the 09-26/27 files when claude-code's pull completes (§7).

---

## 5. What the top does that C1 doesn't — checked against what we already measured

C1 numbers are from its self-play decode (r5 `c1macro.jsonl`, 80 seats): bank median $99.7k; 3 quadrants in 64/80; herd 7.1 / 7.5 / 2.7; strawberries 33; tomatoes 1.5; hires 274/g.

| top-10 feature | who | C1 | status in our lineage |
|---|---|---|---|
| 4th quadrant by step ~254 | family cores, 4thQ | 3q | **dead**: O1 −$9.2k..−$16.9k/g; the 3q M&M fork beats the 4q cores 0.67–0.79 |
| tomatoes 16–19 seeds | family cores | 1.5 | **dead**: O3 ceiling +$109/g; Boey and 4thQ win with 0 tomatoes |
| geese 5–7 | family, Boey | 2.7 | **dead**: O1-goose −$9.2k/g; 4thQ wins with 0 geese |
| strawberries shop-conditioned (20–25) | all | 33 fixed | **dead** as a graft (§5 #1 crop-mix, tape desync) |
| sell clock at h≡1 mod 4 (post-drain) + fixed h22 egg/tomato dumps | family, Majkel, Boey partly | C1R2 has lockstep/impact ordering | **dead** (§5 #21 phase-shift −$1,185; §5 #6) |
| small premium lots (1–5 units) | family | — | covered by the SIR/lockstep layer; not new |
| wheat/fertiliser churn | Boey, 4thQ | none | **net-zero** (§5 #26; exact +$9..25/g here) |
| labour thrift (skip pre-bonus waters) | DSM | tape | freed turns aren't re-used on a tape (§5 #25) |
| randomised per-game planner | Boey | deterministic | not buildable by 09-30 (the "reactive replanner" lever) |
| **terminal herd release** | family: sheep 6.4→4.8→0.8 at d20/27/29; cows 8.3→6.4; geese 7.1→6.0 | keeps 7.1/7.5/2.7 to d29 | **untested.** Stopping feed after the last harvestable production saves ≤2 wheat (~$65) per sheep and loses ≤1 fertiliser (~$40–50). Net ≈ **+$15–25/sheep, ≤ +$150/g**. Not worth an RR run |
| opponent conditioning | nobody (≤0.04 R² on herd/crops) | V92 etc. | the top has no opponent model to exploit or copy |

---

## 6. Ways — my lane's contribution, ranked (each with its kill test)

The decode's main value is negative, and it narrows the search:

1. **W0 — Do not port any top-10 mechanism into C1/C1R2** (decision, no test).
   - Every mechanism is in §5's "dead" column, with a measured number.
   - This frees all remaining hours for the lanes that can still move the RR map: astra's censored-observation fix in C1R2's forecaster, and claude-code's `screen9` stage-2 candidates (18-2 vs C1, +$686..791 in stage 1).
2. **W1 — Pick the final pair on the RR map, not on live LB movement.**
   - Top-10 ratings are visibly version-lagged: DSM is #6 while winning 0.86 against the top 20.
   - C1's live 1672 vs its RR-mapped 2076 is the same phenomenon.
   - **Kill test:** none needed. It is the adopted gate (HANDOFF 09-26d).
3. **W2 — Terminal herd release for C1 (optional, lowest priority).**
   - Change: skip FEED/CARE for animals with no production due before step 718.
   - **Kill test:** 40 paired seeds vs C1, bar ≥ +$150/g paired and 0 lost wins; then `screen2.py`.
   - Expected ≤ +$150/g, below paired-test resolution (opusb's r5 40-seed paired SE was $219). **I recommend not running it** unless a lane is idle.
4. **W3 — Counters to top-10 habits** (h22 dumps, Boey's wool, 4thQ's 10-unit lots). **Untestable and medal-irrelevant.**
   - No top-10 agent file exists, and recorded tapes fail as proxies: r4 found open-loop substitution overrates by >1,000 Elo.
   - We never meet them. Do not build.

---

## 7. Reproduce / extend

```
.venv/bin/python moe/r6/build/opus/dossier.py > moe/r6/build/opus/dossier.log   # needs r5 fam.pkl
.venv/bin/python moe/r6/build/opus/rawscan.py 2 && .venv/bin/python moe/r6/build/opus/rawan.py > rawan.log
.venv/bin/python moe/r6/build/opus/churn.py OUT.jsonl "Boey,Fourth Quadrant,DSM" 2 80
# new dump files: symlink undecoded eps into build/opus/d26/, then
.venv/bin/python moe/r5/build/opus/macro.py moe/r6/build/opus/macro26.jsonl "moe/r6/build/opus/d26/*.json.gz" 2
.venv/bin/python moe/r6/build/opus/tables.py        # -> teams_1_10.md (H2H matrix includes macro26)
```

- The decode costs ~0.1 s/game with 2 workers, so the full 09-26 dump (~600 games) takes about 1 minute.
- If ranks 9–10 appear, `dossier.py` picks them up automatically (it iterates over `top20.json`). Note: it reads `fam.pkl`, so append their `macro26` rows, or point it at `macro26.jsonl`.

---

## 8. Probabilities (final pair under my best plan)

**Plan:** hold [C1, C1R2]. Replace one slot only with a candidate whose RR-map 90% CI lower bound clears the pre-registered gate (2148); `screen9` stage-2 is the live source. Port nothing from the top 10.

**Basis:**
- C1R2 maps to 2152 [2021, 2294], so sd ≈ 83.
- P(true rating ≥ bronze ~2210, allowing +10–20 of cutoff drift) ≈ 0.22–0.25. C1 adds ~0.01 (correlated).
- If a `screen9` candidate passes the gate at ≥ 2250 mapped, bronze is ~0.6 for that slot. I give it ~15% to happen.

| | P |
|---|---|
| **P(bronze)** | **0.30** |
| **P(silver)** (≥ ~2410) | **0.02** |
| **P(top-10)** (≥ ~2884) | **< 0.005** |

**Next action (claude-code):** finish the 09-26 pull and ping me. I will decode ranks 9–10 the same day (≈1 min of compute) and post only if either has a new lineage.
**Next action (opus):** available for `screen2.py` stage-2 runs on the `screen9` finalists.
