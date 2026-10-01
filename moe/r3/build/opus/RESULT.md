# r3 build — Opus arms W1 + R — RESULT

Machine clock (`date -u`): started 2026-09-25 19:47 UTC. ≤2 worker processes, nice 10, kagsim.
No submissions. Every file is in `moe/r3/build/opus/`. Nothing was written outside it.

## Verdicts (top line)

- **C1/C2 gate reading (Opus; Fable's session died at ~19:59 UTC with no candidates and no RESULT.md, so this is not a Fable VERDICT):**
  - I rebuilt `cand_C1_rebuilt.py` and `cand_C2_rebuilt.py` with Fable's own `mkcand.py`.
  - **C1 passes Fable's gates** b (+914, L→W 11/22, W→L 0), c (310%) and d (0.90/0.80), plus the load check → **upload-eligible**.
  - **C2 fails gate b** (L→W 5 < 8).
  - C1 beats my WLV proxy 10–4, C2 25–15 and shepR 28–12.
- **W1, pre-registered row:** **"Neither"** (formal). Row 1 (Fable) fails on magnitude: WL+S leaves shepherd at 9–5, +$686. Row 2 (Opus) fails because WL+S moves shepherd by −$840/g, more than $500 and more than WL+R.
- **Substantively, W1 favours Fable.** The asymmetry is real, specific to shepherd's streams, and **dose-dependent and unsaturated**:

  | library | share of the public-WL → live-WLV gap closed (WLV seeds) |
  |---|---|
  | ~2.7 shepherd streams in the game's bucket | 41% |
  | ~5.3 per bucket | 71% (7–7, +$64) |
  | oracle (same-seed stream) | 89% |

  A fork that records shepherd offline reproduces most of WLV's edge.
- **Mirror (§1b): the lever works for us too.** Shepherd armed with ~5 streams per bucket of the WLV proxy R2 goes:

  | opponent | seeds | shepherd | armed shepherd (shepR) | paired |
  |---|---|---|---|---|
  | R2S | WLV seeds, closed-loop | 4–10 | 12–2 | +$1,642/g |
  | hyb2965 | fresh | — | 39–1 | — |
  | shepherd | fresh | — | 26–14 | — |
  | real WLV tapes | open-loop, 18 | 5–13 | 10–8 | +$598/g (our-bank +$159) |

  `shepR.py` is a candidate lead for Claude Code; its gate is in §1b.
- **R gate:** fails the market-match leg (0/18 tapes reach a ≥600-step market prefix; the best build reaches a median of 215). The retrodiction leg passes, but it passes for unmodified hyb2965 too, so it does not discriminate.
- **`VERDICT R: NO`.** `cand_R.py` is delivered as an **instrument** (closest aggregate WLV proxy), not as an upload.
- **C1 vs best WLV reproduction (§4).** Fable's session died before building C1, so I rebuilt C1 and C2 with Fable's own `mkcand.py` into this directory.
  - **C1 beats my WLV proxy R2S 10–4** (+$955/g paired over shepherd, 13/14), and C2 beats it 14–0.
  - On the rebuilt files, **C1 passes all of Fable's pre-registered gates** (b: +914, L→W 11/22, W→L 0; c: 310%; d: 0.90/0.80) and loads cleanly.
  - **C2 fails (b)** on the L→W count (5 < 8).
- **Opus recommendation to Claude Code** (my reading of Fable's gates; Fable issued no verdict):
  1. **Upload `cand_C1_rebuilt.py`** (md5 `f5ce2562e7214251ae36c0a1895f6da3`).
  2. **No clear second candidate.**
     - C2 fails gate (b) and loses 12–28 to a hyb-family-armed library (shepR).
     - shepR is only marginal vs shepherd (WR 0.47 / 0.65) and loses 12–28 to C1.
     - Keeping hyb2965 as the control beside C1 stays defensible.
- **Leads for later:**
  - Pull the current `haideptry/the-2965-master-hybrid-engine` and its forks. WLV is an EarlyCycle build of that stack, run by 18 teams, so probably public (§2).
  - Grow C1's library with offline-recorded band streams (§1b dose curve).

---

## 1. W1 — asymmetry test (my r2 §5)

### Setup

**Library streams (one per seed).** Each stream is x's premium-sale stream as public WL (yummers) itself recovers it, via its own `_v92_p_update`, while x plays public WL. There are 162 library seeds, disjoint from all test seeds. Each stream is keyed by the game's **real** first-two-shop pair, read at t=150.
- **Correction, found mid-run.** I chose library seeds by a pass-agent pair predictor, intending 6 streams per test pair. The pass-agent pair is **wrong on 14/14 WLV seeds**: empty-tile weed draws shift the shop RNG.
  - The 162 streams actually spread over 60 of 64 real pairs (1–6 each).
  - The WLV-game buckets hold **~2.7 appended streams** for S, R and O (matched, same seeds). S+S2 holds ~5.3.
  - Results are unaffected (keys are the real pairs, seeds are disjoint). The effects below come from *fewer* streams than designed.
  - **Every "per pair" count below means these real bucket counts.**
- **Deviation from the r2 text:** streams were recorded **vs WL**, not in self-play. Self-play is exactly seat-symmetric in kagsim (both seats produce an identical stream), so it yields no extra information.

**Opponent arms** (all public yummers plus 162 appended streams, same buckets and count):

| arm | appended streams | note |
|---|---|---|
| WL+S | shepherd | the hypothesis |
| WL+R | hyb2965 | pre-registered control; see caveat below |
| WL+O | jaxa623 `2802` | **added clean control**: non-band agent, no `_R108` tape, no library |
| WL+S+oracle | WL+S plus each test seed's own shepherd-vs-WL stream | ceiling |

**Caveat on WL+R.** hyb2965's streams overlap shepherd's: 81% exact-tick, 83% of ≥4-unit lots, same seed. It shares the tape, so WL+R is nearly a copy of S. That is why WL+O was added.

**Test.** Shepherd in our seat, closed-loop, on:
- the 14 WLV seeds at the recorded seat;
- 20 fresh seeds (seedindex `[1356:1376]`) × both seats.

The baseline reproduces r2 E-A exactly (+1,525, 13–1).

### Results (shepherd's margin; paired Δ vs the yummers baseline)

| opponent | WLV14 W–L | WLV14 mean | paired Δ (SE, #worse) | fresh40 W–L | fresh40 mean | paired Δ (SE) | forecasts picking an appended stream |
|---|---|---|---|---|---|---|---|
| yummers (public WL) | 13–1 | +1,525 | — | 39–1 | +1,411 | — | — |
| **WL+S** | **9–5** | **+686** | **−840** (344, 10/14) | 31–9 | +974 | −437 (149) | 62% |
| WL+R (hyb2965 streams) | 13–1 | +1,331 | −195 (294, 7/14) | 37–3 | +1,046 | −365 (125) | 41% |
| **WL+O (non-band streams)** | 14–0 | +1,990 | **+464** (143, 1/14) | 39–1 | +1,866 | **+456** (136) | 31% |
| **WL+S+oracle** | **7–7** | **−320** | **−1,846** (423, 13/14) | — | — | — | 79% |
| **WL+S2** (S + 162 more; ~5.3 in bucket) | **7–7** | **+64** | **−1,462** (320, 13/14) | 26–14 | +583 | −827 (133) | 75% |
| *live record vs WLV, same 14 games* | *3–11* | *−546* | | | | | |

**Contrasts** (shepherd margin, WLV14 / fresh40):

| contrast | WLV14 | fresh40 |
|---|---|---|
| S − O | −1,304 (SE 359, 12/14) | −892 (SE 161, 36/40) |
| S − R | −645 (SE 277) | −72 (SE 104) |
| R − O | −659 | −820 |

### Pre-registered reading

| row | condition | observed | holds? |
|---|---|---|---|
| Fable (asymmetry) | shepherd vs WL+S ≤6/14 wins **and** mean ≤ −$200, **and** WL+R ≥11/14 for shepherd | 9/14 wins, +$686; WL+R 13/14 | **no** (magnitude) |
| Opus (non-library) | WL+S moves <$500/g, **or** WL+R moves as much as WL+S | WL+S −$840. WL+R −$195 on WLV14; −365 vs −437 on fresh | **no** on WLV14 (true only on fresh, where R ≈ S by construction) |
| Opus-regardless | R median divergence ≥600 **and** shepherd vs R ≤5/14 | median 215 (§2) | **no** |
| Both | — | — | **no** |
| **Neither** | → no upload from this arm; the hyb2965 read decides | | **holds (formal)** |

### What it means

1. **The mechanism is real and specific.** Which streams the forecaster holds swings shepherd's result by $1.3k/g (S vs O), closed-loop, with both sides reacting.
   - Tape-family streams (shepherd, or hyb2965 on fresh seeds) arm the forecaster against us.
   - Unrelated streams disarm it: WL+O gets *worse* by $460/g.
   - This is the mirror image of C1's premise, measured closed-loop. It is direct support for Fable's lever, and it answers my r2 dispute #3 ("C1 can only be validated live or vs a reproduced WLV") in C1's favour on mechanism, though not on size.
2. **Size.**
   - A realistic S library (~2.7 streams in the game's bucket, which any fork could record offline) closes 840 of the 2,071 public-WL → live-WLV gap on these seeds (**~41%**).
   - The oracle closes 1,846 (**~89%**) and lands at 7–7 / −$320, near the live 3–11 / −$546.
   - **Dose-response:** doubling the library (~5.3 per bucket) closes 1,462 (**~71%**), with 75% of WL's forecasts picking an appended stream. The curve has not flattened.
   - So "WLV forecasts us from a library of tape-family streams" explains most of the gap with an ordinary offline recording effort (a few hundred games).
   - A *simulated* forecast, running our shared public tape forward, would be the oracle limit.
   - Not tested: whether WLV actually holds such a library. Its market is private beyond t≈150 (§2).

## 1b. Mirror: arm *shepherd* with the WLV proxy's streams (C1-prime direction check; not in the r3 brief)

**Build: `shepR.py`** = `subW_shepherd.py` + 324 R2 streams appended to its PREDICT (P) library.
- R2 is the §2 rebuild: hyb2965 + EarlyCycle + no step-91 guard.
- Streams were recovered by shepherd's own `_v92_p_update` in shepherd-vs-R2 games on the W1 library seeds (disjoint from every test slice).
- They land on all 64 real pairs (1–10 each, ~5.3 in the WLV-game buckets).
- Nothing else changed. PREDICT2 stays dormant.

| test | shepherd | shepR | paired Δ | shepR forecasts on an appended stream |
|---|---|---|---|---|
| vs R2S, WLV14 (closed-loop) | 4–10, −443 | **12–2, +1,200** | **+1,642** (SE 302, 13/14) | 76% |
| vs R2S, fresh40 | 16–24, −84 | **39–1, +1,035** | **+1,118** (SE 177, 36/40) | 87% |
| vs R2, WLV14 | 5–9, −94 | 14–0, +1,241 | +1,335 (SE 240, 14/14) | 78% |
| vs R2, fresh40 | 20–20, +88 | 39–1, +1,185 | +1,096 (SE 175) | 88% |
| **vs shepherd, fresh40** | — | **26–14 (0.65), +408** (SE 286) | — | — |
| **vs hyb2965, fresh40** | — | **39–1 (0.97), +1,198** (SE 302) | — | — |
| **vs real WLV tapes, open-loop, 18** | 5–13, −454 | **10–8, +143** | **+598** (our-bank +159, their-bank −439), L→W 5, W→L 0 | — |

**Reading.**
- The forecaster's side gains $1.1–1.6k/g closed-loop when its library holds the opponent family's streams. This is symmetric with W1 (WL+S2 took −$1,462 off shepherd).
- The R2 streams are hyb2965-family, so shepR also crushes unmodified hyb2965 (39–1) and still beats shepherd (26–14).
- **Transfer to the real WLV is smaller:**
  - Open-loop vs the 18 real tapes: +$598/g, 5 losses→wins, 0 wins→losses. That is comparable to Fable's E4 holdout (+$628) with **zero** WLV data in the library.
  - The conservative our-bank half is +$159. R2's premium-sale timing still differs from WLV's on ~54 steps/game (§2), which bounds the transfer.
- **Offline check.** The best same-pair stream F1 vs the live WLV streams does not separate libraries: R2 0.59, S 0.55, 2802 0.57, our shipped library 0.64. Stream "closeness" by that metric is not what the forecaster exploits.

**shepR gate.** Closed-loop on Fable's gate-(d) slice. Note: `[1380:1404]` holds only **20** seeds because the index ends at 1400, so n=40 per matchup; this applies to Fable's gate (d) too. The non-band check uses `[1380:1392]` × both seats.

| matchup | W–L | WR | mean (SE) | note |
|---|---|---|---|---|
| shepR vs shepherd | 19–21 | 0.47 | **+215** (85) | first fresh slice: 26–14, +408. Pooled: 45–35, ~+310 |
| shepR vs hyb2965 | 34–6 | 0.85 | **+918** (192) | first fresh slice: 39–1 |
| shepR vs 2802 (non-band) | 24–0 | — | +3,617 | shepherd: 24–0, +3,652. Paired **−35** (SE 17): negligible mis-pick cost |
| shepR vs koshinm (non-band) | 22–2 | — | +688 | shepherd: 15–9, +436. Paired **+252** (SE 83) |

- PREDICT fires 13–14 per game; 0 errors. Load check: see §3.
- **Reading:** shepR passes a Fable-style (d) threshold (WR ≥0.45 vs each live build) and is mean-positive against both. Its edge is concentrated on hyb2965-family opponents, which include WLV's family. It does not hurt against non-band opponents.
- **Unvalidated:** live transfer (open-loop our-bank +$159/g vs real WLV is the only direct evidence); the ~(8,3)/four-turn families; and whether band libraries already forecast *us* (which shepR does not change).
- **Not a DECISION arm and not gated by the r3 brief.** It is offered as a C1-prime lead for Claude Code to gate.

## 2. R — WLV rebuild from the hyb2965 side (Fable E2 recipe), bisected on the 18 WLV tapes

### Instrument

`rdiv.py` runs two modes on each tape:
- **hyb:** candidate market on WLV's exact farm; WLV's recorded unit ops are forced. This is Fable's deconfounded test.
- **full:** the candidate drives its whole seat against our recorded tape.

It reports per-channel first divergence and a matching-step count. `rclass.py` classifies every differing market step.

### Identification (new)

**WLV's farm is hyb2965's farm, not WL's.**
- Full mode: hyb2965's **unit channel matches WLV to a median of step 598** (range 318–719).
- The step-53 "herd idle" that public WL fails is hyb2965's Gluzdov `_CL_` layer: "mature the temporary wheat one extra day" (hand 0 PASS 53–57, commands 84–91). Public WL (5,764 lines) lacks it.
- hyb2965 ships the WLV opening dormant: `_ALT_MODE='EarlyCycle'` installs `BUY_PRODUCT WHEAT 5, BUY_SEED WHEAT 1`, strips day-1 wheat trades and clears `CT_TABLE`.
- WLV is therefore a **2965-Master-Hybrid-lineage build (6.4k-line stack) in EarlyCycle mode**.
- Eighteen different teams at 2036–2562 run it, so it is very likely a **public notebook we do not hold** (a later version or fork of haideptry's 2965 engine or its EarlyCycle siblings), not a private agent. **Action for Claude Code:** pull the current versions and forks of `haideptry/the-2965-master-hybrid-engine`, and any EarlyCycle 6.4k-line notebooks, into `exact2.py`. I cannot fetch.
- The only local EarlyCycle build with `_CL_`, `rivals4/kaggriculture-more-wheat-smarter-sales`, tracks **worse** than R2: market median 156, units 383.

### Bisection (market first divergence on WLV's farm, 18 tapes)

| build | change | market first divergence | tapes ≥600 | matching steps (of 719) |
|---|---|---|---|---|
| hyb2965 | — | 0 ×18 (opening) | 0 | mean 614; ≥600 on 15/18 |
| R0 | (5,0) opening via `V9_OPENING_STEP0` | 91 ×16, 121 ×2 | 0 | 615 |
| R0L | R0 + WL's library | 91 ×16, 121 ×2 | 0 | 614 |
| R1 | `_ALT_MODE='EarlyCycle'` (identical play to R0) | 91 ×16, 121 ×2 | 0 | 615 |
| **R2** | R1 + remove the step-91 wheat price guard (`price<31`) | **median 215** (91, 91, 121, 150, 150, 151×3, 156, 215, 241, 249×3, 268, 299, 343, 365) | **0** | 616 |
| R3 / R3b | R2 + strip trailing `[]` (± carrot margin −15) | median 121 (worse) | 0 | 595 |

Notes on the table:
- **Matching-step count.** Unmodified hyb2965 already has ≥600 matching steps on 15/18 tapes, so the count reading of "≥600-step market match" discriminates nothing. I bind to the **prefix** (first-divergence) reading, as in my r2 §5 row 3 and Fable's "per-channel first divergence".
- **t=91.** WLV sells the 3 temporary wheat at t=91 on 16/18 tapes. The 2 exceptions have identical price (29), inventory, cash and shop state to 4 games that do sell, so WLV's guard keys on something unobserved.
- **Trailing `[]`.** WLV keeps the trailing `[]` at t=121 on 16/18, so "strip empty orders" is not a global rule. Its hole handling is state-dependent.

**Where R2 stalls** (every differing step, 18 tapes, R2 on WLV's farm):

| phase | differing steps/game | classes |
|---|---|---|
| d0-5 | 0.3 | — |
| d6-12 | 6.8 | qty 34, other 31, slot order 28, premium-sell 24 |
| d13-24 | **49.8** | **premium-sell 534 (60%)**, qty 149, other 129, empty-slot 43, order 41 |
| d25-29 | **45.7** | **premium-sell 439 (53%)**, other 132, qty 119, empty-slot 104, order 29 |

- The d13-29 block is premium-sale presence/absence: the PREDICT/RACE channel, conditioned on a library we do not have. It cannot be reverse-engineered from 18 tapes in a 3-hour bisection.
- The remaining classes are real WLV rules that I could see but not pin down:
  - `BUY_PRODUCT WHEAT` placed ahead of SELLs/HIREs, state-dependently;
  - halved or split wheat buys (14→7, 48→24 + 8s, 9→5);
  - wash fertiliser orders zeroed (`SELL FERTILIZER 0`/`BUY_PRODUCT FERTILIZER 0`);
  - WOOL sold at 156 rather than 150/151.

### Retrodiction (shepherd in our recorded seat vs candidate, closed-loop, 18 WLV seeds)

| opponent | 18: shepherd W–L | 18 mean | 14 mean | sim − live mean | per-game Spearman vs live | same sign |
|---|---|---|---|---|---|---|
| *live WLV* | *4–14* | *−448* | *−546* | — | — | — |
| hyb2965 (unmodified) | 7–11 | −81 | −110 | +367 | −0.11 | 9/18 |
| R0 = R1 | 7–11 | −89 | −118 | +359 | −0.11 | 9/18 |
| R2 | 7–11 | −67 | −94 | +381 | −0.11 | 9/18 |
| R0LS (R0 + WL lib + S) | 8–10 | −296 | −383 | +152 | −0.12 | 6/18 |
| R0S (R0 + our lib + S) | 6–12 | −378 | −467 | +70 | −0.01 | 10/18 |
| **R2S = `cand_R.py`** | **6–12** | **−356** | **−443** | **+92** | −0.02 | 10/18 |

- **The retrodiction leg ("shepherd loses ≥10/18") passes for every hyb2965-family build, including unmodified hyb2965.** These seeds are outcome-selected (games shepherd lost live), and hyb2965 beats shepherd on them anyway.
- Adding S streams moves the aggregate to within ~$90/g of live (again the W1 mechanism). **Per-game agreement is chance**: Spearman ≈ 0, mean |sim − live| ≈ $1,000/g.
- R2S matches WLV's *average* strength against shepherd, not WLV itself.
- **Fresh seeds (20 × 2, `[1356:1376]`).** R2S is at parity with both live builds, far milder than live WLV:
  - shepherd vs R2S: 16–24, −$84 ± 293;
  - shepherd vs R2: 20–20, +$88;
  - hyb2965 vs R2S: 22–18, −$10.
- **Use as an instrument:** it is a biased band proxy. It is adequate for a *direction* check on a PREDICT layer (it carries S-streams, so it forecasts us), not for sizing.

### Gate (DECISION r3)

| leg | pass | result | outcome |
|---|---|---|---|
| market match | ≥10/18 tapes with a ≥600-step market match | **0/18** (best median prefix 215) | FAIL |
| retrodiction | shepherd-vs-R loses ≥10/18 | 12/18 (R2S), 11/18 (R2) | PASS, non-discriminating: unmodified hyb2965 also gives 11/18 |

**`VERDICT R: NO`**

## 3. Files

- **W1:**
  - `w1_prep.py`, `w1_seeds.json`: test and library seeds.
  - `w1_record.py`, `w1_record_o.py`: streams (`w1_streams.jsonl`, `w1_streams_o.jsonl`).
  - `w1_build.py`: builds `wl_S.py`, `wl_R.py`, `wl_O.py`.
  - `w1_test.py`, `w1_tele.py`, `w1_sum.py`: results in `w1_test.jsonl`; telemetry rerun in `w1_tele.jsonl`.
  - `w1_oracle.py`: builds `wl_Sorc.py`; results in `w1_oracle.jsonl`.
  - `w1_dose.py`: builds `wl_S2.py`.
- **W1 mirror / shepR:**
  - `w1_mirror.py`: `w1_mirror_streams.jsonl` → **`shepR.py`**; results in `w1_mirror.jsonl`.
  - `rfresh_b.jsonl`: shepR vs the live builds on `[1356:1376]`.
  - `gate_w1p.py` → `gate_w1p.jsonl`.
  - `openwlv.py` → `openwlv_a.json`: open-loop vs the 18 real WLV tapes.
  - `transfer.py`: offline stream-F1 check.
  - `w1p_record.py`: unused. It was written for full pair coverage, which proved unnecessary once real pairs were known.
- **C1/C2 (rebuilt):**
  - `mkc1.py` (Fable's `mkcand.py` with outputs redirected) → `cand_C1_rebuilt.py` (md5 `f5ce2562…`), `cand_C2_rebuilt.py` (md5 `b23aa81f…`).
  - `c1test.py` → `c1test.jsonl`: vs WLV proxies, plus C1 gate (d).
  - `c2gate.py` → `c2gate.jsonl`.
  - `gate_bc_opus.py` (Fable's `gate_bc.py`, output redirected) → `gate_bc.jsonl`; summary script `gate_bc_sum.py`.
- **Load checks** (`kaggle_load_check.py`: 3 harness seeds + a real `kaggle_environments` run vs starter): **`cand_R.py`, `shepR.py`, `cand_C1_rebuilt.py` and `cand_C2_rebuilt.py` all OK**, DONE/DONE with no errors. Logs are `loadcheck_*.log`.
- **md5:** `cand_R.py` `d0449487…`, `shepR.py` `bee77734…`.
- **Codec:** `lib.py` decodes and encodes `_V92_P_BLOB`/`_INDEX` (round-trip verified on both libraries).
- **R:**
  - `mkR.py` (named patches), `R0/R0L/R1/R2/R3/R3b.py`, `addlib.py`, `R0S/R0LS/R2S.py`.
  - `rdiv.py` → `rdiv_*.jsonl`; `rclass.py` → `rclass_R2.jsonl`.
  - `rretro.py` → `rretro_a/b.jsonl`; `rsum.py` (summary); `rfresh.py` → `rfresh_a.jsonl`.
  - **`cand_R.py`** = R2S + a one-line header.
- **Runner:** `run.py`.
- **Bug noted and fixed mid-run:** the first `w1_test` pick counter compared against `(ep, ev)` tuples, so it read 0 appended picks for S and R. Margins are unaffected (deterministic reruns match to the dollar), and `w1_tele.jsonl` has the corrected counts.

## 4. C1 vs best WLV reproduction (and Fable's gates, since Fable's session died)

### Provenance
- **Fable's session (PID 39814) exited at ~19:59 UTC**, right after stream extraction, while "waiting for the completion notification". It never built `cand_C1.py`/`cand_C2.py` and wrote no RESULT.md.
- I built them from **Fable's own `mkcand.py`**, verbatim except the output names and directory (`mkc1.py`). Fable's `streams_all.json` was read-only input: 456 streams (409 idx + 29 live + 18 WLV) and 39,339 events.
- Outputs:
  - `cand_C1_rebuilt.py` = `subW_shepherd.py` + embedded PREDICT2 blob (15 changed lines, md5 `f5ce2562…`);
  - `cand_C2_rebuilt.py` = `subX_hyb2965.py` + the same blob (md5 `b23aa81f…`).
- Nothing was written into `build/fable/`.

### C1/C2 vs my WLV proxies
Closed-loop, 14 WLV seeds at the recorded seat, with Fable's `_V92_EP` parity holdout set to each game's episode id, so the game's own WLV stream is excluded.

| candidate vs proxy | W–L | mean | shepherd vs the same proxy | paired over shepherd | PREDICT2 fires/g |
|---|---|---|---|---|---|
| **C1 vs R2S (`cand_R`)** | **10–4** | **+512** (SE 195) | 4–10, −443 | **+955** (SE 214, 13/14 better) | 9.6 |
| C1 vs WL+S2 | 11–3 | +824 | 7–7, +64 | +760 (SE 191, 14/14) | 9.9 |
| **C2 vs R2S** | **14–0** | **+703** (SE 113) | 4–10, −443 | **+1,146** (SE 241, 14/14) | 8.4 |
| C2 vs WL+S2 | 14–0 | +1,279 | 7–7, +64 | +1,216 (SE 269, 12/14) | 7.8 |

### Closed-loop gate (d), seedindex `[1380:1404]` (20 seeds × both seats; no holdout needed on fresh seeds)

| matchup | W–L | WR | mean (SE) |
|---|---|---|---|
| **C1 vs shepherd** | **36–4** | 0.90 | **+813** (154) |
| **C1 vs hyb2965** | **32–8** | 0.80 | **+593** (128) |
| C1 vs shepR (§1b) | 28–12 | 0.70 | +500 (167) |
| **C2 vs shepherd** | **30–10** | 0.75 | **+581** (146) |
| **C2 vs hyb2965** | **38–2** | 0.95 | **+793** (98) |
| C1 vs C2 | 25–15 | 0.62 | +80 (127) |
| **C2 vs shepR** | **12–28** | **0.30** | **−273** (191) |

- PREDICT2 fires 6–7 per game on fresh seeds, with 0 errors.
- **The matchups are non-transitive: C1 > shepR > C2, and C1 ≳ C2.** shepR's library holds hyb2965-family (R2) streams, so it forecasts C2's hyb2965 chassis and beats it 28–12. C1 runs on the shepherd chassis and is not exposed to that library.
- **Whoever's chassis-family streams sit in the rival's library loses.** That is the W1 asymmetry again, and it is the main live risk for C2 if band forks record hyb2965 (and for C1 if they record shepherd, as WL+S does, though C1 still beat WL+S2 11–3).

### Fable's pre-registered gates (b)/(c) on the rebuilt candidates
Fable's `gate_bc.py`, run as `gate_bc_opus.py` with output redirected to this directory:

Setup: 444 games, all `[None, None]` errors. Our seat is the live candidate; their seat is the recorded tape, either open-loop or price-reactive (W=12, δ=0.10).

**Parity holdout (primary, as in Fable E4), 28 mirror tapes:**

| candidate | mode | vanilla → cand W–L | mean Δ (SE) | our-bank Δ | L→W | W→L |
|---|---|---|---|---|---|---|
| **C1** | open | 6–22 → **17–11** | **+914** (165) | +279 | **11/22** | **0** |
| **C1** | react | 6–22 → 19–9 | +2,571 (1,114) | **+866 (310% of open)** | 13/22 | 0 |
| C2 | open | 13–15 → 16–12 | +403 (110) | +143 | **5/15** | 2 |
| C2 | react | 21–7 → 21–7 | +1,345 (952) | +405 (284%) | 1/7 | 1 |

**Reference: 18 WLV tapes, parity holdout:**

| candidate | mode | vanilla → cand W–L | mean Δ | our-bank Δ | L→W | W→L |
|---|---|---|---|---|---|---|
| C1 | open | 5–13 → 10–8 | +664 | +258 | 5 | 0 |
| C1 | react | — | +2,229 | +726 | — | — |
| C2 | open | 3–15 → 8–10 | +559 | +192 | 6 | 1 |

**LOO holdout** (production library size) gives the same picture:
- C1 open: 16–12, +928, L→W 10/22, W→L 0.
- C2 open: 17–11, +425, L→W 6/15, W→L 2.

**Against Fable's pre-registered thresholds:**

| gate | threshold | C1 | C2 |
|---|---|---|---|
| (b) | mean ≥ +$400, L→W ≥ 8/22, W→L ≤ 2 | **PASS** (+914, 11, 0) | **FAIL**: L→W 5 < 8. Its hyb2965 baseline has only 15 losses on these shepherd tapes. Mean +403 is on the line. |
| (c) | reactive our-bank ≥ 60% of open | **PASS** (310%) | PASS (284%) |
| (d) | WR ≥ 0.45 vs each live build | **PASS** (0.90 / 0.80) | PASS (0.75 / 0.95) |
| load check | loads and runs cleanly | **OK** | OK |

Note on (c): the reactive rival makes *vanilla* do better too (rival lots held → it sells into a worse book later). The react deltas are large and noisy (SE ~1k), but the threshold is met by a wide margin.

### Reading
- On every closed-loop test available, **C1 and C2 dominate shepherd, hyb2965 and my WLV proxies.** That includes R2S, which is itself armed with shepherd streams and is the proxy closest to live WLV's average strength.
- This is the W1 mechanism working for us: a library of tape-family (band) streams arms the forecaster. W1 and §1b show the effect is $0.8–1.6k/g closed-loop and symmetric.
- C1 also beats shepR (my single-proxy-family library) 28–12. The broad live-tape library generalises better than a single-proxy-family library.
- **Caveat (the one that sank yesterday's layer):** all opponents here are ours or rebuilt proxies. None of them is a live band agent with its *own* private library. The only live-behaviour evidence remains open-loop (gate b, and the WLV open-loop numbers).
