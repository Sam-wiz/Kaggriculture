# Opus lane B — notes (append as I go)

## 2026-09-25 checkpoint 0 — setup
- Read BRIEF, HANDOFF §5 + 09-22n..09-25c, MISTAKES top, gate.py, gate_baseline.log.
- Baseline gate (seeds [1330:1354], n=48/cell): LIVE_sir_V1 beats LIVE_f55rec_V2 0.98, koshinm beats
  sir_V1 0.56. => a candidate on subV_sir2 must beat its own parent >= 0.60 (near-mirror cell).
- Tools on disk: `ledger.py` / `replayaudit.py` hook `_commit_unit` for exact FILLS; full replays in
  live_eps/replays (742, info.seed present, actions in steps[t][seat].action, answer obs t-1).
- Plan: index own eps -> filter opp rating 2400-2900 -> replay through engine with hooks -> per phase
  x channel ledger (fills, hires, land, harvest units, animals alive) -> losses vs wins.

## checkpoint 1 — ledger of 197 band games (opp 2400-2900), 197/197 replays reproduce exactly
- `ledger_eps.py` -> `ledger_band.json`; `decompose.py` prints phase x channel.
- Band opponents are production-clones: harvested wheat 559.6 vs 559.6, same herd (7.6/7.5/2.3 vs
  7.7/7.5/2.3), same hires 275, same land. The loss gap (-1,916 mean, n=118) is NOT production scale.
- Loss gap by channel: STRAWBERRY -631, MILK -591, TOMATO -372, CARROT -285, WOOL -218; wheat churn
  (they buy+sell ~70 more) nets +65; fert churn -62; seeds/animals/hire/land +103.
- In WINS the same channels flip sign (straw +468, milk +442, wool +767) EXCEPT TOMATO: -368 in wins
  too. Tomato is the only channel with a consistent (non-symmetric) opponent edge.

## checkpoint 2 — where the WR is lost
- 118 band losses: 8 blowouts (< -5k) carry 51% of the $ deficit (MILK-dominated, cash-trough class —
  rescue thread CLOSED per HANDOFF §5.23). 74/118 losses are within $1,000 (median loss -708).
- Tomato-annex games: 12/197; opponent ran annex & we did not in 10 -> we went 5-5 in those.
  Excluding them WR stays 0.395 => tomato annex is a $ channel (-370/game) but ~0 WR channel.
- 169/197 games have identical wheat buy behaviour (|dbw|<20): WR 0.41, median gap -199.
  7 games vs heavy wheat round-trippers (opp buys 150+ more wheat): WR 0.00, median -486.
- Carrot: opp harvests/sells ~identically (sell step 682 vs 689 driven by 28/164 games where opp has
  a few extra early carrots). Not a lever.
- => WR is lost in a near-mirror whisker class (median -$199 on ~$100k banks). Next: diff market
  order streams vs opponent on those games to find what the opponent overlay does.

## checkpoint 3 — the market race, and the lever chosen
- Blowouts (7 games): we end with 4-5 cows vs their 6-8, plus 1 escaped cow in 4/7 = the known
  cash-trough class (closed, §5.23). Not re-proposed.
- Index race on contested same-turn sells (`idxrace.py`, price-only metric, whisker games):
  SIR builds net -29/g (we_earlier +252, they_earlier -281; WOOL -34 consistently, FERT +32, STRAW +14);
  f55 builds net -70/g (loss games -147, WOOL -94 MILK -64).
- Lost index races are 18.3/g pure SELL-vs-SELL ordering differences (not buys/hires/empties).
- `orderagree.py`: on multi-item contested turns (~38/g) band opponents keep the SAME relative sell
  order as our NATIVE (f55, un-reordered) lists 88% of the time; only 73% vs our SIR lists.
  => the band mostly plays native tape order. SIR's self-impact sort ignores that it can predict
  the rival's order exactly. Prior CF selector (-46) modelled the rival as +1 inv pressure, not as a
  same-index list; that is the gap.
- LEVER: best-response SELL permutation. Predict the rival list = our pre-SIR native list (clone
  quantities), exact per-index lockstep sim of the turn, choose the SELL-slot permutation maximising
  (our revenue - rival revenue), hedged with a SIR-ordered rival model; tie-break to SIR order.

## checkpoint 4 — cand_brx built, fires, first gate launched
- `cand_brx.py` = subV_sir2.py + BRX layer (final line `agent = _brx_agent`; chain: _brx_agent ->
  _sir_parent(_rec_agent) -> ...; BRX re-implements SIR's sort itself so SIR is not applied twice).
- Fire proof (`firetest.py`, seed 424242 vs sir2): 719 turns, 47 multi-sell turns, 6-7 reorders,
  5-8 fallbacks (duplicate items / k>7), 0 exceptions, runtime unchanged (~3.8 s/game).
- BUG found + fixed: v0 used pre-action shed as stock -> believed 0 melons on a same-turn DROP turn
  -> rotated MELON 24 behind FERT 5 -> -$282 on one turn. Now stock = max(shed, order qty)
  (chassis already clamps SELL qty to projected stock).
- Measurement fact: clone pairings are EXACTLY seat-symmetric (swap seats -> rewards swap to the
  dollar), so gate n per clone cell = seeds, not 2*seeds.
- Screen after fix (seat 0, paired vs sir2 control, 4 seeds): vs f55rec_V1 +68/+349/+48/+61,
  vs f55rec_V2 +74/+329/+51/+65, vs sir2 mirror +48/-258/+84/+28.
- Gate launched: PID 24325, seeds [1000:1050], brx + ctrl(sir2 copy), log gate_brx_v1_1000_50.log.

## checkpoint 5 — gate result v1 (seeds [1000:1050], n=100/cell, 0 failures)
- brx row: f55rec_V2 0.99 | sir_V1 0.62 | f55rec_V1 0.99 | sir_V2 0.93 | koshinm 0.63 | melon 0.63 |
  2802 0.92 | metav4 0.83 | vs ctrl 0.62 ; MEAN 0.796 (ctrl 0.751). Ranking: brx > ctrl > LIVE_sir_V1.
- Paired vs ctrl (sir2 copy), $/game (d>0/d<0 of 100): f55rec_V2 +44 (84/12), sir_V1 +28 (62/36),
  f55rec_V1 +41 (90/10), sir_V2 +25 (56/40), koshinm +62 (88/10), melon -24 (41/49), 2802 +0 (40/56),
  metav4 +20 (80/12). Mean WR vs 8-pool: 0.818 vs 0.797.
- CAVEAT: 47/50 seeds seat-identical in clone cells -> ~50 independent games per cell.
  brx vs sir_V1 on seat 0 only: 30-1-19, z=1.57 (not significant alone).
- v2 (`cand_brx2.py`): online native-vs-SIR rival inference from own realized cashflow.
  Fire test seed 777: vs sir2 lo->-0.15 (2 nat/4 sir votes) margin +29 (v1 was -258);
  vs f55rec_V1 lo->3.0 (6/0) margin +3587 (= v1).
- Confirmation launched: PID 29535, seat 0, seeds [1050:1100], brx/brx2/ctrl x {sir_V1, f55rec_V2,
  koshinm, metav4} -> confirm_1050_50.log.

## checkpoint 6 — confirmation [1050:1100] seat 0 (independent n=50/cell), paired vs ctrl
| opp | brx WR | brx2 WR | ctrl WR | brx-ctrl | brx2-ctrl |
|---|---|---|---|---|---|
| LIVE_sir_V1 | 0.70 | **0.79** | 0.50 | +59 (33+/13-) | +75 (39+/10-) |
| LIVE_f55rec_V2 | 1.00 | 1.00 | 1.00 | +69 (47/3) | +110 (48/2) |
| koshinm | 0.50 | 0.50 | 0.50 | +22 (37/11) | +46 (42/8) |
| metav4 | 0.80 | 0.76 | 0.76 | +73 (45/2) | +86 (44/4) |
- brx2 >= brx on paired $ in every cell. brx2 vs sir_V1 39-1-10 -> z~4.1.
- brx combined over both slices vs sir_V1: 65-1-34 of 100 independent seeds (z~3.1).
- Launched gate for brx2 on [1000:1050] full pool both seats -> gate_brx2_1000_50.log.

## checkpoint 7 — FINAL
- brx2 gate [1000:1050] both seats (n=100/cell, 0 failures): f55rec_V2 0.99 | sir_V1 0.77 |
  f55rec_V1 0.99 | sir_V2 0.95 | koshinm 0.65 | melon 0.63 | 2802 0.92 | metav4 0.85 ; MEAN 0.844.
  Paired vs ctrl (same seeds, from the v1 run): +112, +42, +107, +37, +62, -23, -10, +77 $/g.
  vs sir_V1 seat0: 37-2-11, z=3.75.
- Rest-of-pool mean (excluding live pair): brx2 0.832 vs sir_V1 0.815 -> criterion met.
- kaggle_load_check OK for both candidates; runtime 2.3 s/game (parent 2.4 s); err=0.
- VERDICT in RESULT.md: SUBMIT-WORTHY (cand_brx2.py), whisker-scale (~+20-35 Elo), held-out
  confirmation by the gate decides. All my background jobs reaped (24325, 29535, 30104 exited).
- Not done / next if time: handle duplicate-item SELL rows (5-8 fallbacks/game); obs['step']=None
  fallback (day*24+hour) — left out so the deliverable matches the gated bytes.
