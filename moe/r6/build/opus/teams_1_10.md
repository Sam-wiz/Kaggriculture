# r6 opus — per-team tables, LB ranks 1-10 (build/opus/tables.py)

Data: 09-23..25 top dump (1,773 games, exact replay) + 101 games of 09-26 decoded so far. Ranks 9 (Just A game on your lips) and 10 (Anton Tikhonov) have **0 games** in either.

## H2H matrix (row team's WR vs column, n), 09-23..26, Boey's broken submission excluded

| row \ col | DECEM | Boey | MMPQ | Vadim | Majkel | DSM | MGoose | 4thQ | mtmr_s1 | TFC | chibai | Kdew | all top-20 | all |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **DECEM** (#1, 3048.8) | — | 0.29 (24) | 0.21 (38) | 0.73 (88) | 0.91 (23) | 0.00 (79) | 0.59 (49) | 0.35 (20) | 0.84 (32) | 0.65 (23) | 0.91 (23) | 0.86 (35) | 0.45 (336) | 0.57 (485) |
| **Boey** (#2, 3034.5) | 0.71 (24) | — | 0.72 (18) | 1.00 (9) | 1.00 (4) | 0.65 (34) | 0.86 (21) | 0.67 (3) | 1.00 (3) | 1.00 (2) | 0.56 (9) | 1.00 (12) | 0.75 (114) | 0.78 (144) |
| **MMPQ** (#3, 2979.1) | 0.79 (38) | 0.28 (18) | — | 0.67 (43) | 0.68 (22) | 0.29 (56) | 0.48 (46) | 0.64 (14) | 0.73 (11) | 0.78 (9) | 0.80 (10) | 0.88 (17) | 0.54 (243) | 0.61 (314) |
| **Vadim** (#4, 2962.8) | 0.27 (88) | 0.00 (9) | 0.33 (43) | — | 0.65 (34) | 0.04 (57) | 0.39 (57) | 0.20 (20) | 0.55 (33) | 0.64 (25) | 0.81 (32) | 0.90 (41) | 0.31 (324) | 0.48 (504) |
| **Majkel** (#5, 2955.0) | 0.09 (23) | 0.00 (4) | 0.32 (22) | 0.35 (34) | — | 0.00 (21) | 0.30 (20) | 0.33 (9) | 0.76 (17) | 1.00 (12) | 0.80 (15) | 1.00 (12) | 0.28 (144) | 0.48 (211) |
| **DSM** (#6, 2944.3) | 1.00 (79) | 0.35 (34) | 0.71 (56) | 0.96 (57) | 1.00 (21) | — | 0.98 (55) | 0.57 (7) | 0.86 (22) | 1.00 (13) | 0.91 (11) | 1.00 (19) | 0.86 (311) | 0.88 (386) |
| **MGoose** (#7, 2933.5) | 0.41 (49) | 0.14 (21) | 0.52 (46) | 0.61 (57) | 0.70 (20) | 0.02 (55) | — | 0.32 (19) | 0.62 (29) | 0.80 (20) | 0.85 (27) | 0.84 (31) | 0.41 (280) | 0.52 (404) |
| **4thQ** (#8, 2932.9) | 0.65 (20) | 0.33 (3) | 0.36 (14) | 0.80 (20) | 0.67 (9) | 0.43 (7) | 0.68 (19) | — | 1.00 (5) | 0.50 (6) | 0.50 (8) | 0.67 (9) | 0.62 (94) | 0.65 (130) |

## #1 DECEM (LB 3048.8) — seats 457 (09-23..25)

- record W-L 263-194, bank median $104,698, mean margin +2,331; dates {'2026-09-23': 146, '2026-09-24': 159, '2026-09-25': 152}
- step-1 market (top): x457 `[["BUY_ANIMAL", "COW", 1], ["BUY_PRODUCT", "WHEAT", 5]]`
- land-step tuples: [149, 219, 254] x104, [149, 219, 253] x101, [149, 221, 254] x62, [149, 221, 253] x46
- hires/day: 4.0 4.0 6.0 6.0 5.7 6.0 8.0 8.9 9.0 10.0 11.8 11.4 11.4 11.2 11.6 11.7 11.8 11.7 11.7 11.7 11.6 11.7 11.7 11.6 11.5 11.5 11.3 11.0 10.6 9.9 (total 296, $6,467)
- dawn cash (median) d1..d10: 6 3 25 36 421 844 38 205 2,274 294; d15 23,054; d29 98,308

| dawn | cows | sheep | geese | wheat | carrot | tomato | straw | melon |
|---|---|---|---|---|---|---|---|---|
| d3 | 2.0 | 3.0 | 0.0 | 5 | 0 | 0 | 3 | 11 |
| d6 | 2.0 | 3.0 | 0.0 | 0 | 0 | 0 | 9 | 11 |
| d10 | 8.7 | 5.6 | 3.5 | 20 | 0 | 2 | 19 | 11 |
| d15 | 9.1 | 6.8 | 5.8 | 25 | 5 | 10 | 29 | 0 |
| d20 | 8.5 | 7.1 | 5.8 | 23 | 7 | 17 | 22 | 0 |
| d25 | 7.7 | 6.3 | 5.5 | 31 | 16 | 8 | 13 | 0 |

Seeds bought per phase (d0-5 | 6-11 | 12-17 | 18-23 | 24-29): wheat 10|53|45|43|26; carrot 0|4|13|23|23; tomato 0|7|11|2|0; strawberry 10|15|6|0|0; melon 11|0|0|0|0

Animals bought/game: cow 9.2, sheep 7.4, goose 5.9. Buy-backs/game: wheat 143, fertilizer 1. Discards 15.5.

| product | units sold | revenue | captured $/u | share sold d25+ | share d29 | $/u edge vs opp same game (n) |
|---|---|---|---|---|---|---|
| wheat | 506 | $16,551 | 33 | 0.44 | 0.14 | — |
| carrot | 192 | $7,425 | 39 | 0.63 | 0.23 | — |
| tomato | 120 | $7,875 | 66 | 0.44 | 0.10 | -0.5 (386) |
| strawberry | 218 | $29,620 | 136 | 0.28 | 0.06 | -0.1 (457) |
| melon | 64 | $13,759 | 215 | 0.00 | 0.00 | +15.4 (457) |
| egg | 177 | $8,092 | 46 | 0.29 | 0.06 | -0.1 (411) |
| milk | 193 | $20,907 | 108 | 0.26 | 0.05 | -1.1 (457) |
| wool | 152 | $21,551 | 142 | 0.23 | 0.04 | +5.4 (457) |
| fertilizer | 227 | $11,973 | 53 | 0.13 | 0.06 | — |

| reactivity target | mean ± sd | CV R² shop demand | + opponent covariates (≤d6) |
|---|---|---|---|
| cows_d12 | 8.9 ± 3.0 | 0.61 | 0.61 |
| sheep_d12 | 6.1 ± 4.5 | 0.69 | 0.70 |
| geese_d12 | 5.8 ± 3.0 | 0.59 | 0.58 |
| straw_seed_d6_15 | 21.3 ± 9.3 | 0.72 | 0.72 |
| tomato_seed_d9_20 | 19.1 ± 9.0 | 0.77 | 0.78 |
| carrot_seed_d9_27 | 63.1 ± 43.7 | 0.81 | 0.80 |
| melon_seed_d0_29 | 10.7 ± 0.5 | -0.01 | 0.04 |
| hires_d10_29 | 228.1 ± 7.3 | 0.08 | 0.16 |

## #2 Boey (LB 3034.5) — seats 159 (09-23..25)

- record W-L 101-58, bank median $102,339, mean margin -11,107; dates {'2026-09-23': 53, '2026-09-24': 19, '2026-09-25': 87}
- step-1 market (top): x91 `[["BUY_PRODUCT", "WHEAT", 3], ["HIRE"], ["HIRE"], ["HIRE"], ["HIRE"], ["HIRE"], ["BUY_SEED", "WHEAT", 3], ["NOOP"], ["BU`; x36 `[["BUY_PRODUCT", "WHEAT", 3], ["HIRE"], ["HIRE"], ["HIRE"], ["HIRE"], ["HIRE"], ["BUY_SEED", "WHEAT", 3], ["BUY_SEED", "`
- land-step tuples: [145, 199] x54, [145, 217] x27, [149] x21, [145, 200] x20
- hires/day: 4.8 2.8 5.2 5.3 5.7 5.2 9.6 6.8 9.6 10.3 11.6 10.0 10.8 10.0 10.7 11.2 11.3 11.0 11.4 11.6 11.2 11.1 11.3 11.3 10.9 11.3 10.7 10.3 9.1 9.6 (total 282, $5,359)
- dawn cash (median) d1..d10: 22 291 14 17 16 27 15 33 416 40; d15 29,952; d29 94,695

| dawn | cows | sheep | geese | wheat | carrot | tomato | straw | melon |
|---|---|---|---|---|---|---|---|---|
| d3 | 2.8 | 2.2 | 1.6 | 8 | 0 | 0 | 0 | 10 |
| d6 | 4.4 | 2.8 | 1.9 | 0 | 0 | 0 | 5 | 11 |
| d10 | 6.7 | 6.0 | 4.9 | 18 | 1 | 0 | 22 | 12 |
| d15 | 7.2 | 6.8 | 5.2 | 22 | 2 | 0 | 25 | 2 |
| d20 | 7.0 | 7.5 | 5.2 | 21 | 6 | 1 | 22 | 1 |
| d25 | 6.8 | 7.1 | 5.2 | 31 | 12 | 0 | 6 | 0 |

Seeds bought per phase (d0-5 | 6-11 | 12-17 | 18-23 | 24-29): wheat 14|42|36|49|28; carrot 0|3|8|19|20; tomato 0|0|1|1|0; strawberry 6|19|3|0|0; melon 11|2|0|0|0

Animals bought/game: sheep 8.3, cow 8.3, goose 5.4. Buy-backs/game: wheat 2693, fertilizer 619. Discards 6.0.

| product | units sold | revenue | captured $/u | share sold d25+ | share d29 | $/u edge vs opp same game (n) |
|---|---|---|---|---|---|---|
| wheat | 3002 | $105,411 | 35 | 0.19 | 0.04 | — |
| carrot | 153 | $6,102 | 40 | 0.65 | 0.28 | — |
| tomato | 5 | $334 | 70 | 0.43 | 0.23 | -1.3 (27) |
| strawberry | 180 | $26,916 | 150 | 0.29 | 0.08 | +0.2 (159) |
| melon | 78 | $15,101 | 195 | 0.03 | 0.03 | -9.4 (159) |
| egg | 211 | $9,428 | 45 | 0.28 | 0.09 | +0.4 (143) |
| milk | 188 | $19,671 | 105 | 0.24 | 0.05 | -0.6 (159) |
| wool | 175 | $19,944 | 114 | 0.24 | 0.07 | -24.9 (159) |
| fertilizer | 858 | $36,579 | 43 | 0.22 | 0.04 | — |

| reactivity target | mean ± sd | CV R² shop demand | + opponent covariates (≤d6) |
|---|---|---|---|
| cows_d12 | 6.9 ± 2.8 | 0.41 | 0.40 |
| sheep_d12 | 6.4 ± 3.8 | 0.61 | 0.60 |
| geese_d12 | 5.0 ± 3.3 | 0.26 | 0.30 |
| straw_seed_d6_15 | 21.3 ± 7.3 | 0.70 | 0.69 |
| tomato_seed_d9_20 | 1.7 ± 3.5 | -0.08 | -0.05 |
| carrot_seed_d9_27 | 48.0 ± 29.5 | 0.50 | 0.49 |
| melon_seed_d0_29 | 13.3 ± 2.1 | -0.05 | -0.11 |
| hires_d10_29 | 216.4 ± 4.4 | 0.15 | 0.17 |

## #3 M & M & P & Q (LB 2979.1) — seats 279 (09-23..25)

- record W-L 173-106, bank median $106,021, mean margin +3,459; dates {'2026-09-23': 84, '2026-09-24': 78, '2026-09-25': 117}
- step-1 market (top): x154 `[["BUY_ANIMAL", "COW", 1], ["BUY_PRODUCT", "WHEAT", 5], ["BUY_ANIMAL", "SHEEP", 1], ["BUY_ANIMAL", "SHEEP", 1], ["BUY_AN`; x92 `[["BUY_ANIMAL", "COW", 1], ["BUY_PRODUCT", "WHEAT", 5], ["BUY_ANIMAL", "SHEEP", 2]]`
- land-step tuples: [147, 198] x95, [131, 198] x31, [147, 198, 313] x24, [129, 198] x19
- hires/day: 4.8 3.2 5.0 5.1 6.0 5.6 8.4 7.6 9.5 9.8 11.3 10.3 10.6 10.3 10.5 11.3 11.3 11.1 11.4 11.3 11.0 10.9 11.3 10.9 11.1 11.2 11.0 10.5 9.9 9.5 (total 282, $5,340)
- dawn cash (median) d1..d10: 7 89 58 53 77 215 92 298 251 425; d15 27,216; d29 96,295

| dawn | cows | sheep | geese | wheat | carrot | tomato | straw | melon |
|---|---|---|---|---|---|---|---|---|
| d3 | 3.4 | 2.6 | 0.0 | 8 | 0 | 0 | 2 | 9 |
| d6 | 5.1 | 3.1 | 0.0 | 3 | 0 | 0 | 7 | 9 |
| d10 | 7.7 | 5.9 | 4.5 | 20 | 1 | 0 | 24 | 11 |
| d15 | 8.0 | 6.6 | 5.7 | 22 | 5 | 2 | 28 | 3 |
| d20 | 7.5 | 6.7 | 5.7 | 23 | 7 | 4 | 24 | 1 |
| d25 | 6.9 | 5.9 | 5.6 | 34 | 15 | 3 | 8 | 0 |

Seeds bought per phase (d0-5 | 6-11 | 12-17 | 18-23 | 24-29): wheat 15|42|36|51|32; carrot 0|5|12|23|19; tomato 0|0|4|1|0; strawberry 8|17|7|0|0; melon 9|2|1|0|0

Animals bought/game: cow 8.2, sheep 7.4, goose 5.7. Buy-backs/game: wheat 113, fertilizer 10. Discards 8.1.

| product | units sold | revenue | captured $/u | share sold d25+ | share d29 | $/u edge vs opp same game (n) |
|---|---|---|---|---|---|---|
| wheat | 546 | $17,066 | 31 | 0.48 | 0.19 | — |
| carrot | 182 | $7,363 | 40 | 0.57 | 0.16 | — |
| tomato | 33 | $2,341 | 70 | 0.69 | 0.15 | -1.6 (76) |
| strawberry | 214 | $30,367 | 142 | 0.25 | 0.07 | +1.0 (279) |
| melon | 73 | $14,589 | 199 | 0.06 | 0.02 | +0.2 (279) |
| egg | 174 | $7,782 | 45 | 0.30 | 0.09 | -0.0 (170) |
| milk | 191 | $20,597 | 108 | 0.25 | 0.05 | +7.0 (279) |
| wool | 144 | $20,529 | 143 | 0.24 | 0.06 | +5.1 (279) |
| fertilizer | 226 | $12,442 | 55 | 0.12 | 0.05 | — |

| reactivity target | mean ± sd | CV R² shop demand | + opponent covariates (≤d6) |
|---|---|---|---|
| cows_d12 | 7.8 ± 2.7 | 0.60 | 0.61 |
| sheep_d12 | 6.2 ± 4.1 | 0.70 | 0.71 |
| geese_d12 | 4.9 ± 4.2 | 0.11 | 0.08 |
| straw_seed_d6_15 | 24.1 ± 7.4 | 0.60 | 0.59 |
| tomato_seed_d9_20 | 4.5 ± 7.9 | 0.01 | -0.00 |
| carrot_seed_d9_27 | 58.8 ± 37.2 | 0.61 | 0.61 |
| melon_seed_d0_29 | 12.3 ± 3.1 | -0.02 | -0.04 |
| hires_d10_29 | 216.7 ± 12.2 | 0.07 | 0.05 |

## #4 Vadim Vasilenko (LB 2962.8) — seats 477 (09-23..25)

- record W-L 230-247, bank median $101,908, mean margin +932; dates {'2026-09-23': 169, '2026-09-24': 151, '2026-09-25': 157}
- step-1 market (top): x477 `[["BUY_ANIMAL", "COW", 1], ["BUY_PRODUCT", "WHEAT", 5]]`
- land-step tuples: [149, 219, 254] x129, [149, 219, 253] x123, [149, 221, 254] x52, [149, 219] x44
- hires/day: 4.0 4.0 6.0 6.0 5.3 6.0 8.0 8.8 9.0 10.1 11.7 11.3 11.3 11.2 11.5 11.7 11.8 11.6 11.7 11.7 11.5 11.7 11.7 11.6 11.6 11.5 11.4 11.1 10.8 10.0 (total 296, $6,449)
- dawn cash (median) d1..d10: 6 1 6 12 427 835 40 88 2,298 218; d15 22,771; d29 95,534

| dawn | cows | sheep | geese | wheat | carrot | tomato | straw | melon |
|---|---|---|---|---|---|---|---|---|
| d3 | 2.0 | 3.0 | 0.0 | 4 | 0 | 0 | 4 | 10 |
| d6 | 2.0 | 3.0 | 0.0 | 0 | 0 | 0 | 10 | 10 |
| d10 | 8.7 | 5.1 | 4.5 | 21 | 0 | 3 | 19 | 10 |
| d15 | 8.9 | 6.0 | 6.9 | 26 | 5 | 9 | 28 | 0 |
| d20 | 8.9 | 6.5 | 6.9 | 23 | 7 | 16 | 21 | 0 |
| d25 | 7.8 | 5.6 | 6.6 | 33 | 14 | 8 | 12 | 0 |

Seeds bought per phase (d0-5 | 6-11 | 12-17 | 18-23 | 24-29): wheat 10|52|45|45|28; carrot 0|4|12|21|21; tomato 0|7|9|2|0; strawberry 11|13|6|0|0; melon 10|0|0|0|0

Animals bought/game: cow 9.0, sheep 6.6, goose 6.9. Buy-backs/game: wheat 168, fertilizer 0. Discards 6.9.

| product | units sold | revenue | captured $/u | share sold d25+ | share d29 | $/u edge vs opp same game (n) |
|---|---|---|---|---|---|---|
| wheat | 459 | $15,846 | 35 | 0.44 | 0.14 | — |
| carrot | 158 | $6,630 | 42 | 0.60 | 0.21 | — |
| tomato | 118 | $7,951 | 67 | 0.46 | 0.13 | -0.1 (406) |
| strawberry | 215 | $30,763 | 143 | 0.28 | 0.06 | +4.1 (477) |
| melon | 60 | $13,229 | 221 | 0.00 | 0.00 | +22.8 (477) |
| egg | 209 | $9,441 | 45 | 0.30 | 0.07 | -0.2 (424) |
| milk | 193 | $20,445 | 106 | 0.27 | 0.05 | -1.8 (477) |
| wool | 136 | $18,696 | 138 | 0.23 | 0.04 | +7.3 (477) |
| fertilizer | 280 | $13,270 | 47 | 0.15 | 0.06 | — |

| reactivity target | mean ± sd | CV R² shop demand | + opponent covariates (≤d6) |
|---|---|---|---|
| cows_d12 | 8.8 ± 2.6 | 0.55 | 0.54 |
| sheep_d12 | 5.5 ± 3.9 | 0.68 | 0.69 |
| geese_d12 | 6.9 ± 3.1 | 0.59 | 0.58 |
| straw_seed_d6_15 | 19.8 ± 8.6 | 0.67 | 0.67 |
| tomato_seed_d9_20 | 17.7 ± 7.8 | 0.73 | 0.74 |
| carrot_seed_d9_27 | 58.8 ± 41.0 | 0.81 | 0.81 |
| melon_seed_d0_29 | 10.0 ± 0.2 | -0.03 | -0.05 |
| hires_d10_29 | 228.6 ± 5.8 | 0.08 | 0.10 |

## #5 Majkel1337 (LB 2955.0) — seats 210 (09-23..25)

- record W-L 102-108, bank median $106,082, mean margin +1,712; dates {'2026-09-23': 62, '2026-09-24': 77, '2026-09-25': 71}
- step-1 market (top): x148 `[["BUY_ANIMAL", "COW", 1], ["BUY_ANIMAL", "SHEEP", 2], ["BUY_PRODUCT", "WHEAT", 2]]`; x46 `[["HIRE"], ["HIRE"], ["HIRE"], ["HIRE"], ["HIRE"], ["BUY_ANIMAL", "COW", 1], ["BUY_ANIMAL", "SHEEP", 1], ["BUY_PRODUCT",`
- land-step tuples: [146, 199] x129, [148, 223] x28, [149, 197] x15, [146, 199, 250] x15
- hires/day: 4.9 3.9 4.2 4.4 4.2 4.4 8.9 8.0 8.7 10.2 10.8 10.9 11.0 10.3 10.7 11.3 11.5 11.2 11.4 11.3 11.2 11.2 11.6 11.5 11.4 11.6 11.5 11.0 10.0 9.9 (total 283, $5,484)
- dawn cash (median) d1..d10: 7 41 209 118 42 368 63 198 292 141; d15 26,132; d29 96,478

| dawn | cows | sheep | geese | wheat | carrot | tomato | straw | melon |
|---|---|---|---|---|---|---|---|---|
| d3 | 2.3 | 3.0 | 0.0 | 7 | 0 | 0 | 1 | 11 |
| d6 | 3.8 | 3.1 | 0.1 | 2 | 0 | 0 | 5 | 11 |
| d10 | 7.3 | 4.7 | 4.2 | 21 | 1 | 0 | 23 | 12 |
| d15 | 7.8 | 6.0 | 4.2 | 21 | 4 | 4 | 28 | 1 |
| d20 | 7.7 | 6.3 | 4.2 | 18 | 4 | 10 | 25 | 0 |
| d25 | 7.3 | 5.9 | 4.2 | 28 | 13 | 7 | 8 | 0 |

Seeds bought per phase (d0-5 | 6-11 | 12-17 | 18-23 | 24-29): wheat 15|42|37|45|24; carrot 0|2|8|16|24; tomato 0|2|6|2|0; strawberry 5|21|3|1|0; melon 12|0|0|0|0

Animals bought/game: cow 8.0, sheep 6.6, goose 4.2. Buy-backs/game: wheat 192, fertilizer 0. Discards 9.9.

| product | units sold | revenue | captured $/u | share sold d25+ | share d29 | $/u edge vs opp same game (n) |
|---|---|---|---|---|---|---|
| wheat | 476 | $16,663 | 35 | 0.41 | 0.12 | — |
| carrot | 152 | $6,545 | 43 | 0.69 | 0.25 | — |
| tomato | 69 | $5,418 | 78 | 0.68 | 0.16 | -0.2 (167) |
| strawberry | 210 | $31,434 | 150 | 0.32 | 0.10 | +2.4 (210) |
| melon | 70 | $14,182 | 204 | 0.00 | 0.00 | +1.9 (210) |
| egg | 160 | $7,362 | 46 | 0.27 | 0.08 | +0.4 (190) |
| milk | 193 | $21,390 | 111 | 0.25 | 0.06 | +2.0 (210) |
| wool | 149 | $20,603 | 138 | 0.25 | 0.08 | -7.8 (210) |
| fertilizer | 215 | $11,952 | 56 | 0.12 | 0.05 | — |

| reactivity target | mean ± sd | CV R² shop demand | + opponent covariates (≤d6) |
|---|---|---|---|
| cows_d12 | 7.5 ± 3.0 | 0.60 | 0.59 |
| sheep_d12 | 5.5 ± 3.8 | 0.71 | 0.72 |
| geese_d12 | 4.2 ± 2.7 | 0.57 | 0.58 |
| straw_seed_d6_15 | 23.7 ± 7.9 | 0.80 | 0.80 |
| tomato_seed_d9_20 | 9.6 ± 6.6 | 0.68 | 0.69 |
| carrot_seed_d9_27 | 49.8 ± 30.3 | 0.65 | 0.64 |
| melon_seed_d0_29 | 11.7 ± 1.0 | -0.07 | -0.06 |
| hires_d10_29 | 221.2 ± 5.7 | 0.26 | 0.24 |

## #6 DSM (LB 2944.3) — seats 363 (09-23..25)

- record W-L 320-43, bank median $106,081, mean margin +6,757; dates {'2026-09-23': 103, '2026-09-24': 131, '2026-09-25': 129}
- step-1 market (top): x318 `[["BUY_ANIMAL", "COW", 1], ["BUY_PRODUCT", "WHEAT", 5]]`; x45 `[["BUY_ANIMAL", "COW", 1], ["BUY_PRODUCT", "WHEAT", 5], ["BUY_ANIMAL", "SHEEP", 1], ["BUY_ANIMAL", "SHEEP", 1], ["BUY_AN`
- land-step tuples: [149, 219, 254] x104, [149, 219, 253] x63, [149, 221, 254] x52, [147, 198] x40
- hires/day: 4.1 3.9 5.9 5.9 4.9 5.9 8.1 8.6 9.1 10.1 11.6 11.5 11.4 11.2 11.6 11.8 11.9 11.8 11.8 11.8 11.6 11.7 11.8 11.6 11.6 11.6 11.5 11.2 10.7 9.9 (total 296, $6,617)
- dawn cash (median) d1..d10: 6 1 6 11 464 841 40 83 2,178 183; d15 23,309; d29 98,874

| dawn | cows | sheep | geese | wheat | carrot | tomato | straw | melon |
|---|---|---|---|---|---|---|---|---|
| d3 | 2.1 | 3.0 | 0.0 | 5 | 0 | 0 | 4 | 10 |
| d6 | 2.4 | 3.1 | 0.0 | 0 | 0 | 0 | 10 | 10 |
| d10 | 8.8 | 5.3 | 4.7 | 20 | 0 | 3 | 19 | 10 |
| d15 | 9.0 | 6.2 | 7.1 | 26 | 5 | 10 | 29 | 0 |
| d20 | 8.3 | 6.4 | 7.1 | 23 | 6 | 17 | 22 | 0 |
| d25 | 7.6 | 5.7 | 6.9 | 31 | 14 | 8 | 13 | 0 |

Seeds bought per phase (d0-5 | 6-11 | 12-17 | 18-23 | 24-29): wheat 11|51|44|45|26; carrot 0|4|11|23|21; tomato 0|8|8|2|0; strawberry 10|14|7|0|0; melon 10|0|0|0|0

Animals bought/game: cow 9.1, sheep 6.7, goose 7.1. Buy-backs/game: wheat 146, fertilizer 0. Discards 7.1.

| product | units sold | revenue | captured $/u | share sold d25+ | share d29 | $/u edge vs opp same game (n) |
|---|---|---|---|---|---|---|
| wheat | 526 | $16,936 | 32 | 0.43 | 0.15 | — |
| carrot | 180 | $7,080 | 39 | 0.63 | 0.23 | — |
| tomato | 123 | $8,155 | 66 | 0.46 | 0.14 | +0.5 (257) |
| strawberry | 225 | $30,977 | 138 | 0.29 | 0.07 | +4.6 (363) |
| melon | 61 | $13,361 | 217 | 0.00 | 0.00 | +15.1 (363) |
| egg | 222 | $10,042 | 45 | 0.31 | 0.07 | -0.2 (335) |
| milk | 193 | $20,788 | 108 | 0.26 | 0.05 | +2.3 (363) |
| wool | 139 | $19,587 | 140 | 0.23 | 0.03 | +10.3 (363) |
| fertilizer | 238 | $12,403 | 52 | 0.13 | 0.06 | — |

| reactivity target | mean ± sd | CV R² shop demand | + opponent covariates (≤d6) |
|---|---|---|---|
| cows_d12 | 8.9 ± 2.9 | 0.64 | 0.63 |
| sheep_d12 | 5.7 ± 4.1 | 0.74 | 0.74 |
| geese_d12 | 7.1 ± 3.1 | 0.63 | 0.62 |
| straw_seed_d6_15 | 21.0 ± 8.4 | 0.69 | 0.68 |
| tomato_seed_d9_20 | 17.5 ± 8.9 | 0.37 | 0.36 |
| carrot_seed_d9_27 | 58.1 ± 36.8 | 0.78 | 0.78 |
| melon_seed_d0_29 | 10.2 ± 0.7 | -0.03 | -0.03 |
| hires_d10_29 | 229.6 ± 6.6 | 0.05 | 0.12 |

## #7 Unknown Mother-Goose (LB 2933.5) — seats 394 (09-23..25)

- record W-L 217-177, bank median $105,391, mean margin +2,069; dates {'2026-09-23': 130, '2026-09-24': 120, '2026-09-25': 144}
- step-1 market (top): x394 `[["BUY_ANIMAL", "COW", 1], ["BUY_PRODUCT", "WHEAT", 5]]`
- land-step tuples: [149, 219] x86, [149, 219, 253] x71, [149, 219, 254] x67, [149, 219, 252] x48
- hires/day: 4.0 3.9 6.0 5.9 5.3 6.0 8.0 8.8 9.0 10.0 11.5 11.3 11.3 11.2 11.5 11.6 11.7 11.6 11.7 11.6 11.6 11.6 11.6 11.5 11.6 11.5 11.4 11.3 10.6 9.9 (total 294, $6,331)
- dawn cash (median) d1..d10: 6 2 7 16 387 806 36 80 2,242 292; d15 23,809; d29 98,746

| dawn | cows | sheep | geese | wheat | carrot | tomato | straw | melon |
|---|---|---|---|---|---|---|---|---|
| d3 | 2.0 | 3.0 | 0.0 | 5 | 0 | 0 | 4 | 10 |
| d6 | 2.0 | 3.0 | 0.0 | 0 | 0 | 0 | 10 | 10 |
| d10 | 8.6 | 5.4 | 3.8 | 19 | 1 | 2 | 19 | 12 |
| d15 | 8.7 | 6.4 | 5.8 | 25 | 3 | 9 | 29 | 2 |
| d20 | 8.0 | 6.5 | 5.7 | 23 | 6 | 15 | 22 | 1 |
| d25 | 7.3 | 5.7 | 5.5 | 30 | 16 | 7 | 12 | 0 |

Seeds bought per phase (d0-5 | 6-11 | 12-17 | 18-23 | 24-29): wheat 10|49|43|46|27; carrot 0|3|8|23|21; tomato 0|6|8|2|0; strawberry 10|14|7|0|0; melon 10|2|0|0|0

Animals bought/game: cow 8.8, sheep 6.9, goose 5.8. Buy-backs/game: wheat 143, fertilizer 0. Discards 9.2.

| product | units sold | revenue | captured $/u | share sold d25+ | share d29 | $/u edge vs opp same game (n) |
|---|---|---|---|---|---|---|
| wheat | 503 | $16,696 | 33 | 0.44 | 0.15 | — |
| carrot | 164 | $6,734 | 41 | 0.68 | 0.22 | — |
| tomato | 104 | $7,285 | 70 | 0.44 | 0.11 | -0.3 (305) |
| strawberry | 219 | $30,812 | 141 | 0.27 | 0.05 | +0.4 (394) |
| melon | 72 | $14,594 | 202 | 0.00 | 0.00 | +4.0 (394) |
| egg | 179 | $8,177 | 46 | 0.30 | 0.06 | -0.1 (343) |
| milk | 189 | $20,808 | 110 | 0.25 | 0.05 | -1.8 (394) |
| wool | 142 | $20,070 | 141 | 0.22 | 0.04 | +8.1 (394) |
| fertilizer | 234 | $12,210 | 52 | 0.13 | 0.05 | — |

| reactivity target | mean ± sd | CV R² shop demand | + opponent covariates (≤d6) |
|---|---|---|---|
| cows_d12 | 8.6 ± 2.7 | 0.61 | 0.62 |
| sheep_d12 | 6.0 ± 4.4 | 0.76 | 0.77 |
| geese_d12 | 5.8 ± 3.1 | 0.62 | 0.61 |
| straw_seed_d6_15 | 20.4 ± 9.1 | 0.69 | 0.68 |
| tomato_seed_d9_20 | 15.6 ± 9.4 | 0.54 | 0.56 |
| carrot_seed_d9_27 | 55.4 ± 38.3 | 0.75 | 0.75 |
| melon_seed_d0_29 | 12.2 ± 2.2 | 0.05 | 0.07 |
| hires_d10_29 | 227.6 ± 7.1 | 0.01 | 0.03 |

## #8 Fourth Quadrant (LB 2932.9) — seats 120 (09-23..25)

- record W-L 76-44, bank median $95,978, mean margin +557; dates {'2026-09-23': 1, '2026-09-24': 32, '2026-09-25': 87}
- step-1 market (top): x100 `[["BUY_SEED", "MELON", 1], ["BUY_SEED", "MELON", 1], ["BUY_SEED", "MELON", 1], ["BUY_SEED", "MELON", 1], ["BUY_SEED", "M`; x20 `[["BUY_SEED", "MELON", 1], ["BUY_SEED", "MELON", 1], ["HIRE"], ["BUY_SEED", "MELON", 1], ["BUY_SEED", "MELON", 1], ["HIR`
- land-step tuples: [146, 198, 249] x34, [146, 198, 248] x27, [146, 197, 249] x15, [146, 198, 247] x9
- hires/day: 4.3 5.1 5.0 6.4 5.9 6.0 8.7 7.7 10.1 10.2 12.5 11.5 11.4 11.7 11.7 11.9 12.1 12.0 11.8 11.7 11.5 11.4 11.6 11.2 11.0 11.0 10.6 10.3 9.7 9.2 (total 295, $6,647)
- dawn cash (median) d1..d10: 6 16 7 7 6 7 5 7 8 339; d15 26,699; d29 91,588

| dawn | cows | sheep | geese | wheat | carrot | tomato | straw | melon |
|---|---|---|---|---|---|---|---|---|
| d3 | 3.0 | 3.0 | 0.0 | 7 | 0 | 0 | 4 | 8 |
| d6 | 4.8 | 3.6 | 0.0 | 0 | 0 | 0 | 7 | 10 |
| d10 | 9.2 | 6.3 | 0.0 | 19 | 3 | 0 | 25 | 12 |
| d15 | 9.8 | 7.3 | 0.0 | 34 | 12 | 0 | 32 | 2 |
| d20 | 9.3 | 7.4 | 0.0 | 35 | 9 | 0 | 27 | 0 |
| d25 | 8.6 | 6.6 | 0.0 | 48 | 9 | 0 | 11 | 0 |

Seeds bought per phase (d0-5 | 6-11 | 12-17 | 18-23 | 24-29): wheat 14|84|59|70|28; carrot 0|12|29|17|8; tomato 0|0|0|0|0; strawberry 9|19|5|0|0; melon 10|2|0|0|0

Animals bought/game: sheep 7.8, cow 9.9. Buy-backs/game: fertilizer 938, wheat 1386. Discards 1.5.

| product | units sold | revenue | captured $/u | share sold d25+ | share d29 | $/u edge vs opp same game (n) |
|---|---|---|---|---|---|---|
| wheat | 1955 | $60,437 | 31 | 0.27 | 0.06 | — |
| carrot | 176 | $6,730 | 38 | 0.29 | 0.05 | — |
| tomato | 0 | $0 | 0 | 0.00 | 0.00 | — |
| strawberry | 243 | $31,037 | 128 | 0.23 | 0.04 | +0.2 (120) |
| melon | 71 | $14,947 | 209 | 0.00 | 0.00 | +19.8 (120) |
| egg | 0 | $0 | 0 | 0.00 | 0.00 | — |
| milk | 220 | $20,945 | 95 | 0.25 | 0.06 | +1.3 (120) |
| wool | 161 | $20,728 | 129 | 0.22 | 0.06 | -2.3 (120) |
| fertilizer | 1176 | $45,390 | 39 | 0.22 | 0.05 | — |

| reactivity target | mean ± sd | CV R² shop demand | + opponent covariates (≤d6) |
|---|---|---|---|
| cows_d12 | 9.6 ± 3.0 | 0.57 | 0.55 |
| sheep_d12 | 6.6 ± 4.3 | 0.66 | 0.68 |
| geese_d12 | 0.0 ± 0.0 | nan | nan |
| straw_seed_d6_15 | 24.5 ± 7.2 | 0.65 | 0.63 |
| tomato_seed_d9_20 | 0.0 ± 0.0 | nan | nan |
| carrot_seed_d9_27 | 64.7 ± 50.4 | 0.69 | 0.67 |
| melon_seed_d0_29 | 12.1 ± 1.9 | 0.32 | 0.17 |
| hires_d10_29 | 226.0 ± 16.1 | -0.14 | -0.16 |

## #9 Just A game on your lips (LB 2897.4) — seats 0 (09-23..25)

No games in the top dump (09-23..25) nor in the 09-26 files decoded so far.

## #10 Anton Tikhonov (LB 2884.4) — seats 0 (09-23..25)

No games in the top dump (09-23..25) nor in the 09-26 files decoded so far.
