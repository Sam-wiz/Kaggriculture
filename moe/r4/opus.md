# MoE r4 — Opus 5.5 (decoding lane), round 1

Written 2026-09-26 05:05–06:30 UTC (machine `date -u`). No submissions. Code and data: `moe/r4/build/opus/`.
Data used: 94 of the 09-25 top-dump episodes (`mine/top10`, still streaming), plus the 1,725-episode pre-lock
archive (`mine/top`), plus our 166 post-lock live games (`mine/opp` ≥112.9M). Every replay reproduces the
recorded banks to the dollar: dump 94/94, archive 1,725/1,725, live 166/166.

## 0. Top line (all checked)

1. **Most of the top-10 is one private agent family, and it is not a tape.**
   - **Shared opening.** 6 of the top 8 on the 09-26 05:00 LB open with `BUY_ANIMAL COW 1` at step 1.
     - **Exact two-step opening** (`COW 1, WHEAT 5` then `SELL WHEAT 1, HIRE×4, COW 1, SHEEP 3`): DSM #2, Vadim #3, DECEM #5 and Mother-Goose #7. Also mtmr_s1 #14, Densike #16, Smackaveli and tetsuya.
     - **Variants:** M&M&P&Q #4 and Majkel1337 #8.
   - **History.** The opening has been in the archive since ep ~107.4M (Majkel1337).
   - **Private.** No agent file we hold emits it (605 files checked by source grep and exact-prefix fingerprint).
   - **Reactive.** Within one team, per-step unit-op identity across games is only **0.10–0.25**; our band's shared tape runs at 0.97. Each team executes a shop-conditioned macro plan reactively.
   - **Other lineages.** Boey (#1) and THIRD FARM CLUB (#11) share a `WHEAT 3 + HIRE×5` start. Fourth Quadrant (#6, five single-melon buys) and 吃白饭的大肥鱼 (#12) are separate again.
2. **No replay-built proxy of a top team can rank anything.**
   - **Their tapes break.** A recorded top tape loses **$18–56k** when anything in its world changes. The family spends to the dollar: dawn cash is $1–10 on days 1–4, so a $5 wheat-price change at step 1 cascades.
   - **Open-loop substitution fails retrodiction.** With the recorded shops pinned, substituting our builds against these tapes rates them at **~3,120**. Live they sit at 1,800–2,100, so it fails by more than 1,000 Elo.
   - **Band tapes are the opposite.** They move only **~$400–700** under substitution (robust).
3. **Where the money gap is (descriptive, same worlds).** Our builds in closed-loop self-play, on the dump's seeds with the recorded shops pinned, bank **−$6.3k per seat** against the top pair (30 worlds). The revenue gap is **−$13.5k**:

   | product | gap | why |
   |---|---|---|
   | eggs | −$4.5k | 2.4 geese vs 5.8 |
   | tomatoes | −$4.0k | ~2 plants vs ~15 |
   | wheat | −$4.6k | |
   | strawberries | −$1.6k | we plant **more** (33 vs 21) and glut our own price ($118 vs $142) |

   Lower capex (+$4.3k) and fewer wheat buys (+$2.6k) offset part of it. The top family owns **all 4 quadrants by step 253**; we stop at 3. By first shop:
   - ICE_CREAM_SHOP first: we **beat** the top pair in 3/3 worlds (+$19–29k).
   - Every other first shop: we lose 15/15 (−$12.6k mean).
4. **The instrument behind (3), ENGINE, fails its pre-registered retrodiction.**
   - **Result.** Spearman **0.03** against the pre-lock converged ratings of 6 builds; the bar was ≥ 0.7. pipe16 (2787) and metav4 (2307) bank within $41 (SE 29) of each other.
   - **Consequence.** "Close the engine gap" is a hypothesis about what the top teams do, not a measured lever for us.
5. **Our games are mirror markets, and collision is a property of mirrors, not of skill.**
   - **Ours.** In our live games, **61–90%** of our premium sell-steps collide with the rival selling the same product that turn.
   - **The family against itself is also a mirror:** it collides 35–80% vs its own clones and only 9–30% vs other teams. Its strawberry price is $130 against clones and $142 against others.
   - **Cost.** Replace us with an idle agent and the band opponent's bank rises by **+$68k**.
6. **Boey's giant wheat/fertiliser churn is worth ≈ $0.**
   - **Size.** About 2,000–2,800 same-turn round-tripped units per game.
   - **Value.** Its direct P&L is +$20–73 per game, and −$10 in the one counterfactual that left shops and herd untouched. It is not Boey's edge.
7. **One instrument passes retrodiction, but only for the band: LINEAGE RR.** This is a closed-loop round-robin among our own builds.
   - **Result.** It reproduces the post-lock live order of 5 builds: Spearman 0.70 with 2/10 flips, exactly at the pre-registered bars.
   - **Scale.** The spread matches: 302 Elo in the RR against ~300 live.
   - **Scope.** It may rank candidates aimed at the 2200–2600 band (our medal race). It says nothing about the top-10.

---

## 1. Answers to Q1–Q3 from the decoding lane

### Q1 — How do we reach 3k+?
We cannot by 09-30, and the decode says why. The top-10 are a different class of agent, not a better-tuned copy of ours:
- **Different farm.** Reactive, cash-exact, shop-conditioned planners that fill all four quadrants and diversify into tomato, egg and carrot as the shop draw dictates (plan table in §1 Q2).
- **Measured gap.** In matched worlds their economy out-earns ours by ~$6k/seat. Excluding ICE_CREAM-first worlds it is ~$12.6k.
- **Our levers are too small.** Every lever we have measured (PREDICT, SIR, BRX, capture, reclaim) moves $0.2–1.5k/g against lineage opponents and does not change the farm.
- **Wrong lever class.** Closing ~900 Elo would take a new planner, which is the "reactive replanner" in AGENTS.md. That is not a 4-day job, and we have no instrument that could validate one against the top (Q3).
- **Realistic targets.** Bronze (2211) and silver (2409). The medal race is fought against the 2200–2600 band, which is **our own lineage**. The top-10 is not the relevant opponent for any medal we can reach.

What the decode offers the medal race:
- **Mirror markets are the band's defining feature.** Up to 90% of our premium sells collide, and the mirror costs each side ~$68k against solo play.
- **The top family's diversification is a candidate anti-mirror lever.** It has the 4th quadrant by step 253, ~15–20 tomatoes, ~6 geese, ~9 carrots, and fewer strawberries.
- **Untested.** Its value against the band has not been measured yet. LINEAGE RR (§3) is the one instrument that can measure it, and it retrodicts only marginally. It is a hypothesis for the build lane (opusb), not a result.

### Q2 — Decode the top-10 and build from them

**How the top teams play** (09-25 dump, 94 episodes; family = 115 seats)

| | DSM / Vadim / DECEM / Mother-Goose (+mtmr_s1, Densike, Smackaveli, tetsuya) | Boey (#1) |
|---|---|---|
| step-1 market | `BUY_ANIMAL COW 1, BUY_PRODUCT WHEAT 5` | `BUY_PRODUCT WHEAT 3, HIRE×5, BUY_SEED WHEAT 3, NOOP, BUY_SEED WHEAT 4, BUY_ANIMAL SHEEP 1` |
| step-2 market | `SELL WHEAT 1, HIRE×4, BUY_ANIMAL COW 1, BUY_ANIMAL SHEEP 3` | 10-slot lists with NOOP spacers from then on |
| land | **149 / 219 / 253–254** (all 4 quadrants by day 10.5) | 145 / ~200 (3 quadrants) |
| hires/day | 4,4,6,6,5,6,8,9,9,10,12,12,12… (~300/game) | 5,2,5,5,6,5,9,6,10,9,11… (~280) |
| dawn d11 | 9 cows, 5 sheep, 5.6 geese, 22 strawberries, 26 wheat, 4 tomatoes | 8 cows, 4.5 sheep, 7 geese, 23 strawberries, 26 wheat |
| dawn d21 | 8.4 cows, 5.9 sheep, 6.5 geese, 21 strawberries, **17 tomatoes, 9 carrots**, 24 wheat | similar herd, no tomatoes |
| wheat buy-back | 134–180 units at ~$36 | ~3,300 bought and ~3,600 sold per game (same-turn round trips; ≈ $0 P&L) |
| captured price | milk 106, wool 137, strawberry 135, melon 214 | milk 114, wool 111, **strawberry 153**, melon 202 |
| sell collisions | 35–80% vs its own clones; 9–30% vs other teams | 15–41% |
| record in dump | DSM 17–1, Vadim 14–12, Mother-Goose 14–9, DECEM 12–18 | 12–3 |

**Shop conditioning** (family, 09-25 dump): mean count on the farm at dawn of day 21, grouped by whether that shop is among the first two drawn.

| first-two shop | n | cows | sheep | geese | strawberry | tomato | carrot | wheat | bank |
|---|---|---|---|---|---|---|---|---|---|
| YARN_STORE | 16 | 6.8 | **12.1** | 4.4 | 17.6 | 17.9 | 9.0 | 22.4 | 112.5k |
| ICE_CREAM | 24 | **10.8** | 5.6 | 4.4 | 24.0 | 15.2 | 8.6 | 24.0 | 106.2k |
| SMOOTHIE | 34 | 9.5 | 5.0 | 5.8 | 26.8 | 16.6 | 8.1 | 20.8 | 101.8k |
| PIZZA | 26 | 10.7 | 6.0 | 5.3 | 16.6 | **22.8** | 7.1 | 23.6 | 107.0k |
| PET_CAFE | 26 | 6.8 | 5.9 | 7.4 | 14.7 | 12.5 | **20.2** | 24.0 | 86.6k |
| BAKERY | 33 | 7.7 | 5.8 | **8.1** | 16.5 | 16.9 | 6.6 | 29.0 | 91.5k |
| BRUNCH | 25 | 8.6 | 4.8 | 6.8 | 26.6 | 16.8 | 5.5 | 23.7 | 106.4k |
| FARMERS_MKT | 24 | 7.2 | 4.8 | 7.5 | 24.2 | 21.4 | 9.0 | 19.1 | 109.7k |

The family's plan changed over time. In the pre-lock archive (681 seats) it averaged **2.3 geese and 7.5 tomatoes** at d21; the 09-25 dump shows **6.5 geese and 17.1 tomatoes**. The diversification is recent, so these teams are still iterating.

**Tape vs reactive:**
- **The macro plan is fixed per shop draw.** Land steps are identical in 100% of family games; the herd follows the table above.
- **Execution is reactive.** Per-step unit identity is only 0.10–0.25, the openings are cash-exact, and the tapes break under perturbation.
- **Opponent-conditioning is not identifiable from the dump.** There is no same-seed counterfactual; it would need closed-loop code we do not have.

**Build advice to the build lane (opusb this round; the brief's roster named Fable):**
- **(a) Do not build a router over top-team tapes.**
  - They are cash-exact and collapse under any perturbation: −$56k in the traced case (ep 113067521, DSM's tape against our hyb2965 in DECEM's seat).
  - A PASS opponent alone moves them ±$53k.
  - A "tape + repair executor" would have to re-plan purchases every turn, which makes it a planner, not a tape.
- **(b) The portable content is the macro plan.**
  - Buy the 4th quadrant by ~step 253.
  - Tomatoes: ~15–20 by d16–21 (~23 with PIZZA).
  - Geese: ~6 (8 with BAKERY).
  - Carrots: ~9 (20 with PET_CAFE).
  - Strawberries: ~21, not 33.
  - Sheep: 12 when YARN_STORE is among the first two shops.

  This targets the measured revenue gap (eggs/tomato/wheat) and the mirror collisions. It does not touch the market layer, so C1's PREDICT carries over.
- **(c) Gate for (b): LINEAGE RR**, the only instrument that passed retrodiction.
  - **Setup.** Add the candidate to the round-robin (`rr.py`, same seeds 9100001–20, both seats) against shep, hyb, f55V2, sirV1, pipe16 and C1.
  - **Promote only if** its BT beats C1's by ≥ 50, which maps to ≥ ~30 live Elo.
  - **Also require** that it is not below 0.45 head-to-head against either live build.
  - **Known blind spot.** The RR cannot see how the *top* teams react. It is a band gate only.

### Q3 — Decode the private field; an instrument that retrodicts

What a replay does and does not give:

| recoverable exactly | not recoverable |
|---|---|
| both action streams; seed; every fill (step, seat, op, item, price) | their code, libraries and thresholds |
| price, stock, cash, herd and shed at every tick | their response to any state not in the recording |
| shop sequence; weeds; which orders silently failed | how a reactive agent would re-plan after our change |
| same-seed counterfactuals of *their* edits (open-loop, with invariance checks) | whether the recorded version is still the one playing |

Instruments tried against that constraint, each with its retrodiction verdict:

| instrument | what it is | retrodiction | verdict |
|---|---|---|---|
| tape proxy on its own seed | recorded X vs recorded Y | 94/94 + 1,725/1,725 banks exact | **vacuous**: it reproduces only itself |
| TOP-SUB (open-loop vs top tapes, shops pinned) | our build in one seat vs a recorded top tape | our builds rated ~3,120 (WR 0.71, +$44k); live 1,800–2,100 | **FAIL by >1,000 Elo**; tape breakage $18–56k |
| ENGINE (closed-loop self-play in the dump's worlds) | our pair vs the recorded top pair, same seed and shops | Spearman 0.03 vs pre-lock ratings (bar ≥ 0.7) | **FAIL**; descriptive only |
| BAND-SUB (open-loop vs band tapes, shops pinned) | our seat swapped in 42 live games vs ≥2200 | tapes robust (median \|Δ\| $380); on the recorded build it reproduces shep 2,155 (trivial) | **not validated**; the same method predicted hyb2965 > shepherd on 09-25i, live was the reverse |
| **LINEAGE RR (closed-loop round-robin of our builds)** | 5 builds with known post-lock live ratings, 400 games | Spearman 0.70, 2/10 flips, spread 302 vs ~300 live (pre-registered bar: ≥ 0.7 and ≤ 2) | **PASS (marginal)**: may rank band-targeted candidates only (§3) |

Conclusions:
- **Against the top-10: no offline instrument we can build before 09-30 retrodicts.**
  - Tape proxies cannot survive our presence in their world.
  - Generative proxies are out of reach. A reactive, cash-exact, shop-conditioned planner cannot be cloned from ~20–30 games per team per day in 4 days; the WLV rebuild, which was easier, stalled at a median prefix of 215.
  - The only instrument that measures us against the top-10 is the live ladder.
- **Against the band (our medal race), LINEAGE RR is the one instrument that passed retrodiction**, marginally (§3). It works because the band *is* our lineage: closed-loop, both sides react, and the opponents are the band's own ancestors.
- **BAND-SUB stays a direction check.** It is physically sound (band tapes are robust) but blind to reactive market layers, which is C18.
- **C1's live read is the next retrodiction test for both.** I pre-register three predictions for it below; Sonnet's protocol reads them.

---

## 2. Method: how to reverse-engineer a game (tested on the dump, archive and live games)

1. **Exact replay.** Feed seed + both action streams to the pinned Python engine with fill hooks (`decode.py`, reusing `moe/opus/ledger_eps.py`), or to kagsim.
   - Alignment: `actions[t+1]` answers observation t.
   - Check that both banks match to the dollar; they did on 1,985/1,985 episodes.
2. **Ledger → plan.** From the replay, per seat, extract:
   - land steps; hires per day; seeds and animals bought by day;
   - herd, plants and weeds at every dawn; bank at every dawn;
   - per-product sell units, revenue, price/base and phase split; buy-backs; discards; the opening signature.
   - Tools: `decode.py`, `teams.py`.
3. **Family identification.**
   - (a) Opening signature (first 3 market lists): cheap and decisive.
   - (b) Pairwise per-step unit and market identity within and across teams (`ident.py`): tape vs reactive.
   - (c) Exact-prefix fingerprint against every agent file (`fp.py`: candidate in the seat, recorded opponent open-loop; exact up to the first divergence).
   - (d) Source grep for the opening literal.
   - For the family, (c) and (d) found nothing; the literal exists only in replays back to ep 107.47M.
4. **Conditioning.** Group plan features by shop draw (the table in Q2) and by period (archive vs dump) to separate router branches from version changes.
5. **Mechanism tests by counterfactual replay** (`cfx2.py`).
   - Method: edit one seat's orders on *filled* quantities (never requested ones: my first attempt did that and produced a spurious −$40–100k), replay both seats, and **check shops and herd are unchanged** before attributing money.
   - Example: Boey's churn nets to ≈ $0.
   - Pitfall: any change to the tile plan re-rolls the shops (weed-RNG coupling), so pin them (`kagsim.Game(seed, shops=...)`; `engdec.py` monkeypatches `_end_of_day` for the Python engine and matches kagsim 6/6).
6. **Tape stress test before using any recording as an opponent** (`sub.py`, `brk.py`).
   - Swap the other seat for the candidate and for a PASS control, shops pinned, and measure the tape's own bank drift.
   - Top tapes drift $18–56k; band tapes drift $0.4–0.7k.
   - A tape whose drift exceeds the effect you want to measure cannot be used as an opponent. This single check would have flagged TOP-SUB before any number was read.
7. **Market-skill decode** (`mskill.py`): captured price vs holding-weighted price, same-step collision rate with the rival, and slot order in collisions, per product.
8. **Retrodiction before ranking.** Every instrument gets a pre-registered pass bar against a *known live result*, written before it runs (`PREREG_*.txt`). Two of mine failed it (TOP-SUB, ENGINE); one passed marginally (LINEAGE RR).

## 3. What I built, gates and retrodiction

**Tools, all in `moe/r4/build/opus/`:**
- `decode.py` and `teams.py`: per-seat plan and market ledger, per-team summaries.
- `ident.py` and `fp.py`: family identification.
- `cfx2.py`: fill-accurate counterfactual replay.
- `sub.py` (TOP-SUB / BAND-SUB) and `brk.py`: substitution and tape-breakage diagnosis.
- `engine.py`, `engdec.py`, `engcmp.py`: ENGINE and its product decomposition.
- `mskill.py`: market skill.
- `rr.py`: closed-loop round-robin with a BT fit.

**Data:**
- Decodes: `dec_top10.jsonl`, `dec_top.jsonl`.
- Market skill: `msk_*.jsonl`.
- Substitution: `sub1.jsonl` (TOP-SUB), `sub_band.jsonl`.
- ENGINE: `eng1.jsonl`, `eng_retro.jsonl`, `engdec_shep.jsonl`.
- Round-robin: `rr_retro.jsonl`.

**ENGINE retrodiction** (pre-registered 05:26 UTC). The bank column is ENGINE's per-seat bank on the same 20 worlds; Δ vs K is paired against pipe16.

| build | pre-lock rating | bank/seat | Δ vs K (SE) |
|---|---|---|---|
| K pipe16 | 2787 | 100,740 | — |
| Ob pipe16prem | 2686 | 99,848 | −892 (184) |
| D v43 | 2612 | 102,703 | +1,963 (905) |
| P2 metav4prem | 2602 | 99,814 | −925 (185) |
| H v48 | 2339 | 101,930 | +1,190 (919) |
| L metav4 | 2307 | 100,699 | −41 (29) |

Spearman is 0.03, so ENGINE **FAILS**. Rating differences among our lineage come from head-to-head market interaction, not from solo economy.

**LINEAGE RR retrodiction** (pre-registered 05:31 UTC; raw seeds 9100001–20 × both seats; n = 40 per pair; 400 games, 0 errors):

| build | BT elo (RR) | live post-lock | pairwise WR in RR |
|---|---|---|---|
| shep | **+113** | ~2100 | beats f55V2 0.75, sirV1 0.75, pipe16 0.90; **loses to hyb 0.30** |
| sirV1 | +88 | 1897 | beats f55V2 1.00, hyb 0.65, pipe16 0.65 |
| hyb | +80 | 1974 | beats shep 0.70, pipe16 1.00; loses to f55V2 0.45, sirV1 0.35 |
| f55V2 | −92 | 1930 | beats hyb 0.55, pipe16 0.60 |
| pipe16 | **−189** | ~1800 | loses to all |

**Verdict: PASS, but only just.**
- Spearman is **0.70** (bar ≥ 0.7) and **2 of 10** pairwise orders disagree (bar ≤ 2). The flips are hyb–sirV1 and f55V2–sirV1.
- **Scale matches.** The BT spread shep−pipe16 is 302 against ~300 live.
- **The ends are right** (shep on top, pipe16 at the bottom).
- **The flips sit inside the live noise.** hyb, f55V2 and sirV1 are within 77 Elo live, each ±40–50.
- **Matchups are non-transitive**: hyb beats shep 28–12 head-to-head, yet shep has the best BT.
- **Usage limit.** This is the only instrument of the five that retrodicts. Under the pre-registered rule it may rank **band-targeted** candidates (lineage opponents), never top-10 claims.
- **Mapping to live.** A least-squares fit on the 5 anchors gives live ≈ 1940 + 0.62 × BT.
- **Reading RR results.** Always read the full BT fit, not a single head-to-head. A single pair can mislead: hyb beats shep 0.70 head-to-head, the reverse of their live order.
- **C1 added.** C1 is in the same round-robin (200 more games, same seeds); its mapped value is registered below as the third C1 prediction.

**Pre-registered live predictions for C1** (56560349), to be read at ≥24 games vs ≥2200 on one LB snapshot:
- **BAND-SUB:** C1 gains +$1,429/g paired over the recorded builds (SE 285, L→W 20, W→L 1, n = 42). That implies ~**2,510** vs ≥2200 opponents, WR 0.67.
- **r3 prior (Opus RESULT.md):** 2,230–2,320.
- **LINEAGE RR: still running when this was written.**
  - Job: C1 × 5 builds, 200 games on the same seeds, started 06:26 UTC, ETA ~07:25 UTC at the current load. Parent PID **72377**, workers 72388–72390, nohup. Reap by PID if it hangs; the pool has hung at shutdown twice today.
  - Output: appends to `moe/r4/build/opus/rr_retro.jsonl` (resumable).
  - **To read the prediction:** `.venv/bin/python moe/r4/build/opus/c1map.py`. It refits BT, maps live ≈ a + b × BT on the 5 anchors (currently 1941 + 0.62 × BT) and prints C1's predicted live rating.
  - The value counts as registered only once the run shows all 200 C1 games. I will post it to THREAD.md.
- **Reading rule:**
  - Live ≥ 2,420 → BAND-SUB is calibrated for PREDICT-class changes and may rank the next candidate.
  - Live ≤ 2,330 → BAND-SUB over-predicts by ≥ 180 (C18 again) and is demoted to a direction check.
  - LINEAGE RR keeps its gate status only if C1's live rating lands within ±100 of its RR mapping.

## 4. Next 12 h (2 workers, nice 10)

1. **Decode the full 09-23..25 dump** as it streams (~1,750 episodes): per-team tables, and whether each family changed version across the 3 days (plan drift = moving target). Deliver `moe/r4/build/opus/TOP10.md` with a per-team one-pager.
2. **Hand opusb the plan table and diversification targets** (Q2 b). claude-code's C1-T2/T2E, which loosens the V219 tomato gate, is the cheapest version. For any such candidate:
   - run it through the LINEAGE RR gate (§1 Q2 c) and report BT with SE;
   - measure its collision rate (`mskill.py` on its RR games).
   - I will also run any opusb candidate through RR on request. PREDICT-class candidates take ~1.5 h per 200 games at the current machine load.
3. **Opponent-conditioning in the family.**
   - **First cut, done:** sell volumes are similar whatever the opponent (milk 156–195, strawberry 206–227 per game). Collisions and prices track the opponent's family.
   - **Next:** the same-shop-draw comparison (DSM against Boey vs against family mirrors) to test for a PREDICT-like layer.
4. **With Sonnet: C1 live read at ~13:00 UTC** against the three registered predictions above, on a fixed snapshot, with a per-family WR table and Sonnet's per-band SPRT.
5. **Stop list:**
   - top-tape routers or substitution against the top;
   - ENGINE as a ranking gate;
   - any claim about 3k from offline numbers.

## 5. Probabilities (final standing, as of 05:35 UTC)

P(3k+): **0.2%**   P(top-10): **0.5%**   P(silver): **7%**   P(bronze): **38%**

Basis:
- **Top-10 and 3k+:** the gap is an agent-class gap: ~$6–13k/seat of economy, reactive planning, and no instrument to validate against.
- **Bronze:** rests on C1 converging in its r3 prior band (2,230–2,320) or better. hyb2965's 1,974 alone is 237 short.
- **Silver:** needs BAND-SUB's optimistic reading to hold live. That method has over-predicted once already (C18).

## Answer to claude-code's thread question (06:55 post; I can only write this file)

- **Clement Lau / tamref's `WHEAT 5 / seed 1` opening is the r3 "(5,0)" WLV opening.** That is the EarlyCycle build of the 2965-hybrid stack (r3 RESULT §2), i.e. a band-lineage mirror.
- **None of C1's 8 opponents at ≥2000 is a top-dump team.** None opens `BUY_ANIMAL COW 1`, and none of the 8 names appears in either the 09-25 dump or the 1,725-episode archive (checked by team name).
- **So C1's ≥2400 slice is pure band.** It is exactly the population LINEAGE RR claims to model, which makes C1's live read a fair retrodiction test for it.

## Reconciliation with prior decodes (for round 2)

- **`TOP10_DECODE.md` (09-23) decoded public kernels that *claimed* top-10 scores, not the teams at the top.**
  - Its conclusion was "rivals do not win on a mechanism we lack".
  - That does not hold for the 09-25 top-10: they run a different, reactive farm, own all 4 quadrants by step 253, and diversify per shop draw.
  - They are private.
- **Sonnet r4 §1.2 ("top tier: carrot → 0", from pre-lock `meta/` features) does not describe the current top.** Sonnet has since reproduced this and retracted it (THREAD.md 05:42).
  - All 12 of the current top-12 teams sell carrots in the 09-25 dump: **112–248 units/game**, 35–84 carrot seeds bought.
  - Only 4 of 168 top-12 seats sold zero carrots. DSM (#2) sells 242/game and DECEM 248; the family plants 20 carrots when PET_CAFE is drawn.
  - The family's plan also changed between the archive and 09-25 (geese 2.3 → 6.5, tomatoes 7.5 → 17.1).
  - Correlates from pre-lock data are therefore stale for the current top. Any "carrot reallocation" test built on them should be re-derived from the dump first.

## Failures and corrections this round

- **fp.py stalled.** Exact-prefix fingerprinting of 605 files × 9 seats was too slow (~5 s/job, 7+ h). I stopped it at 60 jobs; none matched beyond step 3. Source grep covered the rest.
- **cfx.py measured an artefact.** Netting *requested* orders produced −$40–100k; the correct version is `cfx2.py` (filled quantities plus invariance checks).
- **The first TOP-SUB run re-rolled the shops in every cell.** I rewrote it with the shops pinned; it still failed on tape breakage.
- **The ENGINE gap shrank with more data.** At 10 worlds it read −$13k/seat; at 17–30 worlds it is −$6k (the ICE_CREAM worlds). Quote −$6.3k (30 worlds, SE ≈ $3.6k).
- **ENGINE confounds economy with self-collision.** Self-play mirrors collide by construction; top pairs collide less. Part of the −$6.3k is mirror penalty, not farm.
