# Opus lane B — where we lose to the 2400-2900 band, and one fix

## 1. Decomposition (exact fills, 197 live band games, 197/197 replays reproduce the recorded rewards)

Source: every cached own episode whose opponent is rated 2400-2900 on `live_eps/lb_now.json`
(736 full replays + 171 reduced archives indexed → 197 band games, 118 losses; all 8 builds).
Each game was re-run through the pinned engine with hooks on `_commit_unit`, `_do_hire`,
`_do_buy_land`, `_apply_unit_action` and `_drop_inventories_to_shed` (`ledger_eps.py`). Money identity
3000 + Σfills == final bank checked for every game and both seats.

**Band opponents are production clones.** Harvested wheat 559.6 vs 559.6 per game; herd placed
7.6/7.5/2.3 (cow/sheep/goose) vs 7.7/7.5/2.3; hires 274.8 vs 274.7; the same land; strawberry plants
4.0 vs 4.2 at day 6 and 32.9 vs 32.8 at day 12. Unit-op identity with us is 80-97% in most games.
So the brief's structural candidates (strawberry from day 2, ~10 cows) describe the **top-10**, not
this band. Nothing separates us from the band on production scale.

Loss gap by phase × channel (118 losses, mean −1,916/game, ours minus theirs, $):

| channel | d0-9 | d10-20 | d21-29 | total |
|---|---|---|---|---|
| SELL STRAWBERRY | 0 | −385 | −246 | −631 |
| SELL MILK | −22 | −411 | −158 | −591 |
| SELL TOMATO | 0 | −91 | −280 | −372 |
| SELL CARROT | −6 | −92 | −186 | −285 |
| SELL WOOL | −30 | −161 | −26 | −218 |
| wheat churn (SELL −2,914, BUY +2,979) | | | | +65 |
| fert churn (SELL −522, BUY +460) | | | | −62 |
| seeds+animals+hire+land | | | | +103 |

The same table for the 79 wins flips sign on strawberry/milk/wool (+468/+442/+767), so those are the
race itself, not a structural deficit. **Tomato is the only channel with the same sign in wins
(−368) and losses (−372)**, and it comes from 10 games where the opponent ran a 70-170-unit tomato
annex and we ran none. We went 5-5 in those 10, and excluding them the band WR is unchanged
(0.395 vs 0.40). So the annex is a $ channel but carries no WR.

How the losses are distributed:
- **Blowouts**: 8 of 118 losses are below −5k, yet they hold 51% of the $ deficit. All are MILK-led:
  we end with 4-5 cows against their 6-8, and 4 of the 7 also lose a cow to an escape. This is the
  known cash-trough / animal-buy-failure class (HANDOFF §5.23, three rescue variants measured
  negative), so I did not reopen it.
- **Whisker games**: 74 of 118 losses are within $1,000 (median loss −708). In the 169 games with
  identical wheat behaviour, WR is 0.41 and the median gap is −$199 on ~$100k banks.
- Heavy wheat round-trippers (opponent buys 150+ more wheat): 7 games, WR 0.00. This is an opponent
  class, not something we can fix.

What decides whisker games (`timing.py`, `idxrace*.py`, `orderagree.py`):
- It is the same-turn market race: per game about 250 turns where both sides sell the same item.
- Our SIR builds lose the index race 24.0 vs 17.5 turns per game. On a price-only metric that nets
  −29/g for SIR builds and −70/g for f55 (−147/g in f55 losses). WOOL loses every time (−34/g).
- 18.3 of those lost turns per game are pure SELL-vs-SELL ordering. Buys, hires and empty slots
  in front of our sells are rare.
- **Band opponents keep our native (pre-SIR) sell order on 88% of multi-item contested turns**
  (only 73% vs our SIR lists). SIR sorts by self-impact and never uses that prediction.

**Largest recoverable channel:** the per-turn sell-order race against a predictable, mostly
native-ordered clone field. It happens every game, unlike the annex (5% of games, no WR effect) or
the blowouts (closed thread).

## 2. The change — `cand_brx.py` (subV_sir2.py + BRX, ~150 lines appended)

BRX = best-response SELL permutation:
1. Take the pre-SIR list (`_sir_parent`) as the predicted rival list: native order, clone
   quantities. Hedge with a SIR-ordered rival (weights 0.6 / 0.4).
2. Items never interact in the price function, so for each SELL row × each existing SELL slot, run
   the exact per-index, per-unit lockstep for that one item against the predicted rival rows,
   including BUY_PRODUCT rows for WHEAT/FERT. Objective = our $ − rival $.
3. Assign rows to slots by brute force (k ≤ 7). Deviate from SIR only if the gain is > $1.
   Duplicate items, or k > 7, fall back to SIR. Non-SELL rows never move, same as SIR.

Why it differs from the falsified CF / lockstep selectors (−46 each): those modelled the rival as
+1 inventory pressure per unit, so they could not see the same-index race. BRX models the rival's
**list** directly, and the band data says that list is predictable.

Fire proof (seed 424242 vs sir2): 719 turns entered, 47 multi-sell turns, 6-7 reorders, 5-8
fallbacks, 0 exceptions, 3.8 s/game (same as the parent). The final assignment is
`agent = _brx_agent`, and the chain is traced: _brx_agent → _rec_agent → … . SIR's sort is
re-implemented inside BRX, so it is not applied twice.
Bug found and fixed before gating: v0 took stock from the pre-action shed. On a same-turn DROP turn
it believed we had 0 melons and moved MELON 24 behind FERT 5 (−$282 on that turn). Stock is now
max(shed, order qty).

**`cand_brx2.py` (recommended) = cand_brx + online rival-order inference.** After each multi-sell
turn, BRX2 compares our realised cashflow (money delta across the market step) with what our final
list would have earned against a native-ordered rival and against a SIR-ordered rival. It predicts
with the same per-item sims plus the known HIRE fib / seed / animal costs, and skips cash- or
shed-constrained turns. Each discriminating turn (predictions ≥ $4 apart) moves the log-odds by
±0.5 (prior P(native) = 0.70, clipped at ±3), and that sets the blend weight for the permutation
choice. Fire proof: vs sir2 it moved to lo −0.15 (2 native / 4 SIR votes); vs f55rec_V1 and
f55rec_V2 it moved to lo +2.85…3.0 (all votes native). 0 exceptions, 2.3 s/game (parent 2.4 s).

Preflight: `kaggle_load_check.py` passes on both files: they load with no `__file__`, the last
callable is `_brx2_agent` / `_brx_agent`, and the real kaggle_environments run finishes DONE for
both seats. Each file's final line binds `agent`.

## 3. Gate evidence (seed slice [1000:1100], fresh; real engine; 0 failed games)

**Measurement caveat found on the way:** clone pairings are seat-symmetric. In 47 of 50 seeds,
swapping seats swaps the rewards to the dollar, so a gate cell of "n=100" holds about **50
independent games**. The significance figures below are computed on seat-0-only W/L.

### 3a. `moe/gate.py --only-candidates --workers 2 --seeds 1000 50`
(both seats, n=100/cell; `ctrl` = byte copy of subV_sir2.py run in the same job, so every delta
is paired on the identical seed and seat)

| opponent | brx2 WR | brx WR | ctrl (=sir_V1) WR | brx2−ctrl $/g (d+/d−) | brx−ctrl $/g (d+/d−) |
|---|---|---|---|---|---|
| LIVE_f55rec_V2 | 0.99 | 0.99 | 0.99 | +112 (93/4) | +44 (84/12) |
| **LIVE_sir_V1** | **0.77** | 0.62 | 0.50 | +42 (76/20) | +28 (62/36) |
| f55rec_V1 | 0.99 | 0.99 | 0.99 | +107 (98/2) | +41 (90/10) |
| sir_V2 | 0.95 | 0.93 | 0.95 | +37 (70/24) | +25 (56/40) |
| koshinm | 0.65 | 0.63 | 0.59 | +62 (90/8) | +62 (88/10) |
| melon | 0.63 | 0.63 | 0.63 | −23 (33/59) | −24 (41/49) |
| 2802 | 0.92 | 0.92 | 0.92 | −10 (40/54) | +0 (40/56) |
| metav4 | 0.85 | 0.83 | 0.81 | +77 (89/7) | +20 (80/12) |
| **mean vs 8-pool** | **0.844** | 0.818 | 0.797 | | |

brx2 vs LIVE_sir_V1 on independent seeds (seat 0): **37-2-11, z = 3.75**. brx vs sir_V1: 30-1-19.
The gate's own ranking: brx2 > melon > koshinm > LIVE_sir_V1 > …

### 3b. Confirmation, seeds [1050:1100], seat 0 only (50 independent games per cell)

| opponent | brx2 WR | brx WR | ctrl WR | brx2−ctrl | brx−ctrl |
|---|---|---|---|---|---|
| LIVE_sir_V1 | **0.79** | 0.70 | 0.50 | +75 (39+/10−) | +59 (33/13) |
| LIVE_f55rec_V2 | 1.00 | 1.00 | 1.00 | +110 (48/2) | +69 (47/3) |
| koshinm | 0.50 | 0.50 | 0.50 | +46 (42/8) | +22 (37/11) |
| metav4 | 0.76 | 0.80 | 0.76 | +86 (44/4) | +73 (45/2) |

### 3c. Against the brief's target
- Beat both live builds ≥ 0.60 over ≥ 48 games each: brx2 vs f55rec_V2 is 0.99 (n=100) and 1.00
  (n=50). brx2 vs sir_V1 is 0.77 (n=100 gate) and 0.79 (n=50 fresh), about 76-21 over 100
  independent seeds. **Pass.**
- Mean vs the rest of the pool (excluding the two live builds), same seeds: brx2 0.832; sir_V1
  (ctrl) 0.815 (the baseline log on [1330:1354] gives sir_V1 0.805). **Pass.**

### 3d. What it is worth, and what it is not
- The per-game gain is a whisker: +40 to +110 against clone-lineage opponents, positive in 70-98% of
  paired games. That is exactly the class the band decomposition says decides our 2400-2900 losses
  (median loss −$708; clone-band median gap −$199). By the whisker model (~$300 of relative margin
  ≈ 100 Elo in this band), +$60-110 is roughly **+20-35 Elo**. It is not +200.
- Against non-clone lineages (melon −23, 2802 −10) the native-order prediction is wrong. The cost
  is small and WR does not move (0.63 / 0.92 unchanged).
- The big band-$ channels are untouched: blowouts (51% of loss $, closed thread) and the
  opponent's tomato annex (5% of games, WR-neutral).
- Whether the live band really plays native order is measured from 197 real games (88%
  agreement). How it behaves live cannot be proven offline. The inference layer falls back toward
  SIR ordering when the rival is SIR-like, which is the mechanism behind the 0.77 vs sir_V1.
- Known weakness, not fixed so the deliverable stays byte-identical to what was gated: if
  `obs['step']` were ever None, BRX2 degrades to v1 with a fixed 0.70 weight (no crash).
  Per HANDOFF V5 that bug is replay-only.

## 4. Files
`cand_brx2.py` (recommended), `cand_brx.py` (v1, no inference). Analysis: `index_eps.py`,
`ledger_eps.py` → `ledger_band.json`, `decompose.py`, `pergame.py`, `timing.py`, `mktdiff.py`,
`idxrace.py`, `idxrace2.py`, `orderagree.py`. Measurement: `firetest.py`, `paired.py`,
`confirm.py`, `gate_brx_v1_1000_50.{log,json}`, `gate_brx2_1000_50.{log,json}`,
`confirm_1050_50.{log,json}`. Frozen gated copies: `frozen_brx_v1.py`, `frozen_brx2_v1.py`
(md5-identical to the cand files), `frozen_ctrl_sir2.py` (= subV_sir2.py).

VERDICT: SUBMIT-WORTHY — cand_brx2.py beats LIVE_sir_V1 0.77/0.79 (≈76-21 over 100 independent seeds, z≈3.75 on the gate half) and LIVE_f55rec_V2 0.99-1.00, raises the pool mean 0.797→0.844 on paired seeds, and is paired-positive against every clone lineage; it is a whisker-scale edge (~+20-35 Elo), so the orchestrator's held-out confirmation should decide which slot it replaces (it is a strict extension of sir-V1, so it would naturally take sir-V1's slot).
