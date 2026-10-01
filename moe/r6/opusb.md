# MoE r6 — opusb round 1: decoding ranks 11-20 (2026-09-27)

Lane: ranks 11-20 of `moe/r6/top20.json`. All numbers below come from exact engine replays: 116/116 lane
episodes reproduce both banks to the dollar. Replays use opus's `macro.py` job, over `moe/r5/build/opus/macro.jsonl`
plus my 09-26 decode `build/opusb/macro26.jsonl`. Scripts and logs are in `moe/r6/build/opusb/`.

## TL;DR
1. **Most of this lane has no usable tape, because it is made of late risers.** Six of the ten teams put up a
   new private submission on 09-25/26 and climbed fast. atsushi11o7 went from 1488 to 2840 in about 39 h.
   Russell Kirk went from 2143 to 2886 and then **renamed itself 有辣条有权**. kigasudayooo went from 2543 to 2850,
   My second life from 2673 to 2834, and Yizhou from 2663 to 2835. The 09-23..26 dumps hold ≥4 games for
   only 6 teams: Azat 52, TheEggman 31, "nah id win" 24, Arda 7, 有辣条有权 5 and Kawatta 4. kigasudayooo
   has 1. atsushi11o7, Yizhou and My second life have 0.
2. **Every decoded lane agent is private.** Step-1 action matches none of 328 md5-unique library agents.
   That includes every rivals9 agent file and our own subs (`fp1step.jsonl`). Day-0..1 full-action identity
   against Harvest/C1/rivals9 self-play is 0.00–0.02 (`pubtape.log`).
3. **Shared-code finding: 有辣条有权 (#13) runs the DSM/Vadim chassis.** Full-action identity over steps 1–48 is
   0.54 with DSM and 0.50 with Vadim, against its own within-team figure of 0.51. At steps 1–216 it is still
   0.25 with DSM against 0.22 within. The same cluster holds Smackaveli (#28; 0.48 with DSM) and, more
   loosely, Arda (#16; 0.38) and Unknown Mother-Goose (#7; 0.24). Azat, TheEggman, KawattaTaido and "nah id
   win" are separate lineages, each with cross-team identity ≤0.17. Details in `xident48.log`,
   `xident96.log` and `xident216.log`.
4. **The COW1+WHEAT5 opening is not one codebase.** 32 teams open with it (`cowwheat.log`). It starts with
   Majkel1337 around ep 108.7M, reaches the whole top family, and turns up in #1182–#4888 teams around
   ep 111.2M. Across teams the day-0..2 unit tapes agree only 0.06–0.61, so it looks like a converged
   opening rather than a copied executor. No public source exists in our library.
5. **Against the top 8, the lane loses almost everything.** Records: Azat 9-43, TheEggman 3-28, Arda 0-7,
   有辣条有权 0-5, Kawatta 1-3, kigasudayooo 0-1. Mean margins run −$5.5k to −$15.2k per game. The one
   exception is **"nah id win" on 09-23: 18-6, +$5.8k/g**. My best guess is that this is #20's old name
   (medium confidence).
6. **What we can take for 09-30 is almost nothing.** Macro gaps against C1 are real but not cheap knobs:
   - Quad-3 comes about 2 days earlier in every lane team, but C1's timing is baked into its tape.
   - Lane/family teams apply roughly 1.5–2× as much fertilizer (~170–240 per game against C1's ~123, and
     C1 also buys 91 back). That comes down to executor labour.
   - The mid-game carrot/tomato programme is O3-class, and O3's measured ceiling is +$109/g.

   The only cheap item worth a kill test is **fertilizer churn on the Harvest chassis** (W3 below).
7. **Two cross-lane flags.**
   - Boey (#2) and Fourth Quadrant (#8) trade the market at scale. Boey buys 2,693 wheat and 619 fertilizer
     per game; Fourth Quadrant buys 1,386 wheat and 938 fertilizer. Every other top team buys 113–192
     wheat and no fertilizer.
   - The LB medal lines are deflating. Bronze (rank ~1008) went 2239 → 2209 → **2129**, and silver (rank ~504)
     went 2437 → 2408 → **2350**, across 09-25 16:12, 09-26 05:00 and 09-27 (`lb_*.json`).

## 0. Data coverage and aliases
LB columns are snapshots: `data/lb.json` (09-23), `live_eps/lb_now.json` (09-25a), `moe/r3/lb_0925_1612`,
`lb_0926_0500` and `moe/r6/lb_0927`.

| # | team (members) | LB 09-23 → 09-25a → 09-25b → 09-26 → 09-27 | games decoded | alias / note |
|---|---|---|---|---|
| 11 | KawattaTaido | 2977 → 2830 → 2815 → 2790 → 2873 | 4 (09-23) + 95 pre-09-21 (`mine/top`) | recent sub; old games are older versions |
| 12 | Azat Akhtyamov | 777 → 2925 → 2862 → 2899 → 2861 | **52** (09-23/24/26) | 3 step-1 variants, so ≥2 active subs |
| 13 | 有辣条有权 (russcore) | 1927 → 1296 → 2143 → 2886 → 2851 | 5 (09-26, as "Russell Kirk") | renamed between 09-26 05:00 and 09-27; username match. Forum: "I'm trying a math heavy approach" (discussions.md:2506) |
| 14 | kigasudayooo | 2491 → 2456 → 2543 → 2810 → 2850 | 1 (09-26) | riser |
| 15 | TheEggman (ethanl67) | 2967 → 2860 → 2909 → 2889 → 2848 | **31** | stable |
| 16 | Arda Ceylan | 2548 → 2901 → 2858 → 2859 → 2843 | 7 (+26 old) | stable |
| 17 | atsushi11o7 | 724 → 1198 → 1485 → 1488 → 2840 | **0** | new sub on 09-26/27 |
| 18 | Yizhou | 2781 → 2730 → 2663 → 2793 → 2835 | 0 (2 old vs us) | riser |
| 19 | My second life (4 members) | 1658 → 1462 → 2673 → 2832 → 2834 | 0 (1 old) | riser |
| 20 | We wanna be tomatos (5 members) | — → 2818 → 2881 → 2802 → 2820 | 24 as "nah id win" (09-23), **probable** | see note |

**Why "nah id win" is probably #20.** Of the 09-23 names, 'midnq' (2884) vanished before 09-25, and
midnqly is a member of #20. "nah id win" played only on 09-23 and was never on any LB snapshot. It
coexisted with 'tetsuya…guoqi', Fourth Quadrant and 'Roxy', so it cannot be any of them. Evidence is by
elimination only: no shared tapes exist.

The 09-26 dump was still landing while I worked: 175/596 files. To refresh:
`.venv/bin/python moe/r6/build/opusb/macro26.py && .venv/bin/python moe/r6/build/opusb/extract.py && .venv/bin/python moe/r6/build/opusb/dossier.py`.

## 1. Lineage map
Method (`xident.py N`): mean pairwise step-identity of the full action (farmer + hands + market) over steps
1..N, between seats of team A and team B. The diagonal is within-team. When cross ≈ within, the codes can't
be told apart.

destbreso's caveat (rivals9 georgymamarin §10) is that nothing observable varies before turn 48. That
inflates *within*-team agreement, not *cross*-team agreement, and the RK≈DSM result holds to N=216.

| N=48 | self | DSM | Vadim | UMG | DECEM | mtmr | Arda | Smack | TheEgg | Azat |
|---|---|---|---|---|---|---|---|---|---|---|
| 有辣条有权 (RK) | 0.51 | **0.54** | **0.50** | 0.30 | 0.17 | 0.09 | 0.27 | 0.40 | 0.11 | 0.02 |
| Arda Ceylan | 0.51 | 0.38 | 0.31 | 0.13 | 0.06 | 0.07 | — | 0.23 | 0.16 | 0.02 |
| TheEggman | 0.47 | 0.12 | 0.11 | 0.10 | 0.06 | 0.15 | 0.16 | 0.08 | — | 0.01 |
| Azat | 0.25 | 0.02 | 0.02 | 0.02 | 0.01 | 0.01 | 0.02 | 0.01 | 0.01 | — |
| KawattaTaido | 0.89 | 0 | 0 | 0 | 0 | 0.03 | 0 | 0 | 0.01 | 0 |
| nah id win | 0.71 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| kigasudayooo (n=1) | — | 0.10 | 0.10 | 0.08 | 0.19 | 0.27 | 0.05 | 0.06 | 0.13 | 0.01 |

At N=216: DSM self 0.34, Vadim self 0.29, RK self 0.22, RK–DSM 0.25, RK–Vadim 0.20, Smack–DSM 0.26,
Arda–DSM 0.14.

**Openings.**
- Top family and five lane teams: `[BUY_ANIMAL COW 1, BUY_PRODUCT WHEAT 5]` at step 1.
  - Azat adds either `SHEEP 2` or seven no-op `SELL x 3` orders.
  - TheEggman and Arda reverse the order: `WHEAT 5, COW 1`.
- Kawatta: `BUY_PRODUCT WHEAT 14` at step 1, then `SELL WHEAT 9 + HIRE×5 + COW 2 + SHEEP 2 + SEED WHEAT 7
  + MELON 12` at step 2. The step-2 bundle is the public pipe/v48 chassis bundle, which C1 and Harvest
  also play at step 2. Kawatta's unit tape nonetheless matches Harvest's at only 0.06.
- "nah id win": `HIRE×5, COW 1, SHEEP 1, WHEAT 6` at step 1.

**Answer to claude-code's thread question.** The Harvest/guru/tetsutani/lynn family is C1's own opening:
48-step identity Harvest≡C1 is 1.00, and haideptry is 0.98 (`pubtape.log`). It opens like **no** decoded
top-20 team (0.00, or 0.02 for one generic step). It sits far from the top-20 executors, much as C1 does.

## 2. Per-team dossiers
Common schema: land = BUY_LAND steps. Herd and crops are dawn means. The "sells" line is product units,
revenue and price index (captured/base); late = share sold on d25+. H2H is margin per game.

### #11 KawattaTaido (n=4, 09-23; plus 95 old games)
- **Lineage.** Pipe/v48 chassis bundle behind a step-1 wheat round-trip (buy 14, sell 9). Unit ops are
  identical across all 4 games through d5. The market diverges at median step 53, which fits a
  price-reactive sell layer over a fixed opening. The 09-21d fingerprint said "v65/router ~75-79%".
- **Macro.**
  - Land 150 then 197 (3 of 4 games) or 221.
  - Hires/day go 5,4,4,5,4,5, then 8–13 from d6. Total 289, costing $6.1k.
  - Herd at d15 is C7.2 G2.8 S8.0. Seeds: melon 12, strawberry 23 on d0-9; carrots 18/44 on d10-19/d20-29.
- **Market.**
  - Wool is the biggest earner: 199u, $28.6k, pi 0.72.
  - Other lines: strawberry 161u pi 1.11; melon 76u pi 0.87; milk 178u pi 0.53. Fertilizer: 254 sold of
    414 made.
  - Buys back 168 wheat and 10 fertilizer. **Discards 46 per game**, the highest in the lane.
- **H2H.** 1-3: beat Vadim +$4.9k, lost to UMG ×2 (−$10.3k) and Kaggledew (−$11.8k).
- **Adopt/exploit.** Nothing. It is the old public chassis with a private overlay, and n=4.

### #12 Azat Akhtyamov (n=52; the largest sample)
- **Lineage.** COW1+WHEAT5 family opening, but the executor is its own. Cross-team identity is ≤0.06, and
  within-team is only 0.25 because it plays 3 step-1 variants (21/16/15 games).
- **Macro.** Two land schedules, i.e. two submissions:
  - (149, 219/221) in 20 games.
  - An **early 2nd quadrant at step 129–134 (d5) plus 3rd at 198** in 14 games.

  Herd at d15 is C8.0 G1.5 S6.8. Wheat seeds 40/80/63 by phase; carrots 24 on d10-19 and 39 on d20-29;
  tomatoes 6.
- **Market.**
  - Strawberry 217u pi 1.17 ($30.4k); milk 199u pi 0.68; wool 149u pi 0.61.
  - Eggs are thin: 55u, geese 1.5. Buys back 144 wheat, no fertilizer.
- **Same-world gap vs top-8 opponents (n=36).** Margin −$6.5k/g. Revenue shortfall: wheat −$4.9k, eggs
  −$4.5k, fertilizer −$5.7k, tomatoes −$2.3k, wool −$1.8k.
- **H2H.** 9-43: DECEM 0-8, Majkel 0-6, UMG 1-6, mtmr 0-6, Vadim 1-4, Fourth Quadrant 2-1, Kaggledew 2-2.
- **Reactivity.** The full tape diverges from the team mode at step 0–1. Correlation of shops with herd:
  sheep↔yarn 0.96, cow↔milk shops 0.79, goose↔egg shops 0.18 (it barely keeps geese).
- **Adopt/exploit.** The early-2nd-quad variant is not measurably better. Mean margins by schedule are too
  noisy at n=14 against 20, so I'm not proposing it.

### #13 有辣条有权, formerly Russell Kirk (n=5, all 09-26)
- **Lineage.** The DSM/Vadim chassis (§1), with differences later in the game.
- **Macro.** Land (149, 219) plus 4th quadrant at 254 in 2 of 5 games. It keeps **the lane's biggest cow
  herd**: 11.6 cows bought, C11.2 G3.4 S6.4 at d15.
- **Market.** Milk 269u pi 0.90, **$38.6k**, the best milk line in the lane. Wool 129u pi 0.55; strawberry
  192u pi 1.27.
- **Result.** **0-5, −$15.2k/g**: DECEM −$10.6k, MMPQ ×2 −$12.1k, Vadim −$7.0k, and **Fourth Quadrant
  −$34.3k**. Against the same top-8 worlds it is short on fertilizer (−$10.7k), wheat (−$9.8k),
  strawberries (−$6.4k) and wool (−$3.9k).
- **Adopt/exploit.** This is a "math heavy" DSM derivative that is weaker than DSM head-to-head.

### #14 kigasudayooo (n=1)
- A single game against Vadim, lost −$10.6k.
- It is a **goose-heavy farm**: 11 geese bought, 337 eggs for $16.6k. It has 4 quads (149, 219, 253), 956
  wheat, and only 90 milk.
- Nearest code is mtmr_s1 at 0.27, which is weak evidence. It is too thin to act on.

### #15 TheEggman (n=31)
- **Lineage.** WHEAT5+COW1 order. Distinct code, with cross-team identity ≤0.17.
- **Macro.**
  - **4th quadrant at step 253–254 (d10) in ~94% of games** (quads 3.94 at d15). That is the most
    land-aggressive in the lane.
  - Herd C7.3 **G5.5** S6.8.
  - **Tomato programme**: 16 seeds on d10-19, 116 tomatoes. 7–9 empty tiles from d15 on, so the extra land
    is not filled.
- **Market.** Eggs 171u pi 0.92; tomatoes 115u pi 1.05; strawberry 207u pi 1.01. Buys back 174 wheat.
- **Same-world gap vs top 8 (n=24).** −$7.7k/g, spread across melon −$2.6k, wool −$2.1k, fertilizer
  −$2.9k, milk −$1.5k and eggs −$1.5k. It **pays about +$0.25 quads for land it does not use.**
- **H2H.** 3-28. It is 0-8 against Vadim and beat Azat once (+$8.6k).
- **Adopt/exploit.** Of all the teams, this one is the live evidence that the 4th quadrant does not pay by
  itself. That is the same verdict as O1 on C1.

### #16 Arda Ceylan (n=7)
- **Lineage.** WHEAT5+COW1 order, same as TheEggman. Its tapes, though, sit closest to DSM/Vadim (0.38/0.31;
  0.61 on units with the old Majkel1337).
- **Macro.** 4th quadrant at 253 in 4 of 7 games. Cows 9.7, geese 4.1.
- **Market.** Strawberry 221u pi 1.23; milk 217u pi 0.78. **Discards 31 per game.**
- **Result.** 0-7, −$7.4k.

### #17 atsushi11o7, #18 Yizhou, #19 My second life: no games in any archive under any known name
All three are risers or brand-new submissions. The only source for them is a pull by submission or team.
See W1.

### #20 We wanna be tomatos, probably "nah id win" (n=24, 09-23 only)
- **Lineage.** Unique, with 0.00 identity to every other team. Opens with `HIRE×5, COW 1, SHEEP 1, WHEAT 6`.
- **Macro.** Only 3 quads (148, 222–223). Herd C7.2 G3.1 S8.1. Strawberry 25 plus melon 12 early; carrots
  and tomatoes late. **Discards 5.8 per game**, the lowest.
- **Market.**
  - Strawberry 208u **pi 1.33**: it captures $159 against the opponent's $153.
  - Wool 184u pi 0.79 ($29.1k; $158 against $147).
  - Buys back 205 wheat.
- **Result.** **18-6, +$5.8k/g against the top 8:**
  - DECEM 5-4, Vadim 3-0, UMG 2-0, MMPQ 1-2, Kaggledew 5-0.
  - Boey 1-0 at +$64.7k (one blow-up).

  Against the same worlds its edge is **wool +$3.1k and −0.61 quads (less land spend)**; revenue elsewhere
  is roughly equal.
- **Puzzle.** A 75% win rate against the top 8 should rate at about 3000, yet the team sits at 2820. Most
  likely that agent was deactivated around the merge.
- **Adopt/exploit.** "Skip the 4th quadrant and sell wool and strawberries into better prices" is
  consistent with O1 being dead on C1. It is not a separate lever.

## 3. Cross-cutting measurements
**(a) Macro: lane against C1.**
- C1 live: 40 exact-replayed games from `mine/opp` with our C1 opening (`c1live.log`).
- C1 self-play: 80 seats (`c1cmp.log`).

| | C1 live | C1 self | lane (COW1+WHEAT5 teams) | top-8 family |
|---|---|---|---|---|
| land steps | 150, 265 (+433 in 25%) | 150, 265 | 149, 219–223 (+253 for TheEggman/Arda/RK) | see opus.md |
| dawn cash d9 / d10 | — | $1.36k / $2.55k | $1.89k / $0.48k | |
| hires/game | 273 | 268 | 285–296 | |
| fertilizer made / sold / bought | 365 / 333 / **91** | 369 / 335 / ? | 360–470 / ~50% / 0 | 411–476 / 49–60% / 0 |
| fertilizer applied (≈ made + bought − sold) | **~123** | | ~170–220 | ~190–240 |
| wheat made / bought | 560 / 587 (round trips) | 558 / ? | 697–729 / 144–174 | / 113–192 |
| carrot + tomato seeds d10-19 | — | 1.7 + 1.5 | 22–25 + 6–16 | |

**(b) Shop reactivity is universal, so it is not a differentiator.** Correlations between demand from shops
at d9 and herd at d12 or seeds on d10-19 (`contrast_final.log`):

| | sheep↔yarn | cow↔milk shops | tomato |
|---|---|---|---|
| everyone, including C1 | 0.84–1.00 | 0.73–0.96 | |
| C1 self | 0.98 | 0.77 | 0.69 |
| TheEggman | | | 0.78 |
| Azat | | | 0.34 |

The goose↔egg correlation varies most: 0.16 (MMPQ) to 0.81 ("nah id win").

**(c) Tape identity and reactivity.** Every lane agent diverges from its own modal tape within days 0–2:

| team | median first-divergence step |
|---|---|
| Azat | 0 |
| "nah id win" | 21 |
| TheEggman | 28 |
| Arda | 38 |
| RK | 39 |
| Kawatta | 53 (market) / 155 (units) |

That is before any shop is drawn, so the triggers are market price and opponent. **None is a fixed
tape.**

**(d) Compute signature: not observable from our data.** The reduced dumps drop `remainingOverageTime`, and
none of the lane teams appear in `moe/r5/build/opusb/overage_*.jsonl`.

## 4. "Ways" from this lane, ranked, with kill tests
Promotion rule (claude-code, THREAD 15:45): a candidate needs RR-map point > the incumbent's and a
lower bound > the other slot's.

- **W1. Fill the six empty dossiers. This is information, not a lever. About 1 h, owner claude-code.**
  - Pull lane-team episodes from the public `georgymamarin/kaggriculture-episodes` dataset (the rivals9
    notebook says it holds every finished game, with `episodes.csv` and `stream_hashes.csv`), or from the
    09-27 daily dump.
  - Add per-seat `remainingOverageTime` to `mine/fetch_epindex.py:reduce()` so compute signatures survive.
  - Kill: none. It changes what we believe about #14, #17–#20, not the agent.
- **W3. Fertilizer churn on the Harvest chassis. The only cheap lever I found. About 3–4 h.**
  - What I measured: C1 sells 333 and buys 91 back, applying ~123. Lane/family teams buy none back and
    apply ~170–240.
  - Hypothesis: a sell clamp that keeps a reserve for the next 72 steps of scheduled FERTILIZE ops removes
    the buy-back and the price hit.
  - Kill 1: exact-replay 40 Harvest games with fill prices. Kill if buy-back cost minus lost sale revenue
    is < $150/g.
  - Kill 2: 40 paired seeds against Harvest. Kill if Δmargin ≤ 0.
  - Kill 3: RR map. Kill unless point > 2329 and lower bound > 2152.
  - Prior: weak. If the application gap is labour-bound, as r5 found C1 saturated at 9–12 hires/day, the
    clamp only shifts cash.
- **Killed without a run (named so nobody re-proposes them).**
  - Earlier quad-3: tape-baked in C1 (`subY_C1_predict2.py:4317`, "Day 11 waits until the tape's own land
    purchase"), and Harvest shares the opening.
  - 4th quadrant: TheEggman and Arda pay for it and underperform; O1 measured −$9–17k on C1.
  - Mid-game carrot/tomato: O3 ceiling +$109/g; the carrot premise was retracted in r4.
  - Any exploit of lane teams: they are ~500–700 Elo above our band, and the final Bradley-Terry fit
    scores win/loss against the opponents we actually meet.
- **Not started in this session: Harvest+PREDICT2.** The thread assigns it to opusb (claude-code, 15:20).
  This session was scoped to round 1 (this file). It is my next action; bar: point > 2329 and lower bound
  > 2152.

## 5. Probabilities (final pair under the best plan)
Best plan: [Harvest (2329 [2160, 2514]), plus C1R2 or whatever beats it by the gate].

- Today's LB puts bronze at 2129 and silver at 2350, but the lines have fallen about 110 points since 09-25.
  That is probably deadline resubmissions resetting to 600, which is transient. The final Bradley-Terry
  fit over active agents should put the lines back near 09-25/26 levels on the RR scale: about 2200–2240
  and 2400–2440.
- Harvest is public, so expect clones. They crowd its band, and mirror games are coin-flips.
- On an RR σ of about 105, Harvest clears ~2220 about 85% of the time. After calibration and clone risk I
  put it at 0.7.

**P(bronze) ≈ 0.70, P(silver) ≈ 0.20, P(top-10) < 0.01.**
