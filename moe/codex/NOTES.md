# Codex lane A — endgame money capture

2026-09-25. Working only under `moe/codex/`; no submissions. Read `moe/BRIEF.md`
in full, HANDOFF ground rules/falsifications/recent timeline, and MISTAKES.md.
Lane claim is recorded here because the brief explicitly prohibits editing HANDOFF.

## Plan and constraints

- Engine-hook successful `_commit_unit` calls; requests are never treated as fills.
- Fresh seed-index slice [900:1000], maximum two worker processes.
- Trace sir-V1 against koshinm and f55rec-V2 in both seats, reconcile cash ledger.
- Isolate an endgame-only same-turn-delivery/empty-slot patch from sirx's other
  changes. Do not import the broader L96 stack or repeat dead phase-shift work.
- Prove changed actions and zero layer exceptions, then use `moe/gate.py`.

## Initial source findings

The prompt's route-648 hypothesis is superseded by HANDOFF r4d: both chassis
already switch to route 2, and prior same-seed sell streams matched. Source
inspection agrees. Koshinm's actual entry wraps a compressed base with only
`sell_impact_reorder`; decode its base/operator before attributing new behavior.
The live sir file still reads the pre-action shed in `_prm_agent`, and preserves
empty slots in `_sir_agent`. Both defects can be isolated to days 21–29.
Engine package is 1.32.7. `projected_shed` accounts for unit-order PICKUP/DROP,
capacity, and non-animal PLACE, matching the intended same-turn stock source.

## Checkpoint 1 — baseline ledger and minimal market patch

24 games: sir-V1 vs koshinm and f55rec-V2, seed-index [900:906] (actual seeds
900900–900905), both seats, 12 games per matchup. Every step's money reconciles
exactly against successful engine commits, hire/land costs, and unit-action
costs. Projected stock equals actual pre-market shed on every checked step.
Raw per-unit fill prices, order indices, action requests, stock, bank, and route
are in `traces/*.json`; `trace_baseline.jsonl` indexes them.

- vs koshinm: mean margin -$110.58; days 21–29 sale-revenue gap -$140.42.
  Both sell exactly 1,431 wool in the pooled window. Prices $56.60 vs $59.28;
  days 27–29 alone $52.99 vs $60.79. This panel does not reproduce a universal
  $11/unit gap; the gap depends on draw and phase.
- vs f55rec-V2: +$1,868.17 margin, days 21–29 sale-revenue gap +$1,510.83.
- Decoded koshinm's nested wrappers; **entire route 2 is identical** to sir-V1,
  including its 648–718 tail (`decode_report.json`). Its layers are market
  portfolio, jaxa frontload, adaptive market, sale advance 7/10, and SIR.

`cand_delivery.py`: sir-V1 plus projected-shed premium selling and empty-slot
compaction only at step >=504. Same 24 games: paired margin gain +$178.17 vs
koshinm (8W/4L) and +$53.67 vs f55rec-V2 (12W/0L). Zero errors; 82 changed
turns overall, including 64 premium-stock changes and 18 compactions.
This is a development panel, not held-out confirmation.

## Checkpoint 2 — delivery stall identified; isolated worker correction

Seed 900902 seat 0, koshinm: sir-V1 loses $1,150 overall. During steps 648–718
each sells 62 wool, but receipts are $2,084 vs $3,992 (-$1,908). At steps
657–669 our two SE sheep workers repeat PASS because reclaim strips their
unpayable CARE; koshinm keeps moving, harvesting, and delivering. This is a
delivery-timing defect despite equal final filled sale volumes, not different route 2.

`cand_capture.py` adds a private planning view for V233 workers: mark CARE
complete only when no future payable production can consume today's bonus.
The engine pays production BEFORE banking today's care, so care on the day
before the animal's last production is also too late. Last harvest day is
29 (the refresh after day 28 produces it); day 29 itself has no refresh.
No farm state is mutated. The existing controller handles all moves/harvests.

Source audit also found a defect in the prior sirx generic worker edit:
HARVEST/COLLECT branches were nested inside `not cared_today`, eliminating
both when care was already complete. Our wrapper retains the original
branches. This is a source finding; no live-performance attribution is made.

## Checkpoint 3 — mechanism confirmed, fresh gate running

Capture development panel (same 24 games): +$944 paired margin vs koshinm,
10W/2L, and +$411.83 vs f55rec-V2, 12W/0L. Worker decisions changed 188
times across the panel, with 198 changed turns including market changes and
zero new-layer errors. The seed-900902 seat-0 loss becomes +$3,498: our bank
increases $2,210 and the rival's decreases $2,438, total margin gain $4,648.
Filled wool sales remain 363 units each; late wool receipts change from
$2,084/$3,992 to $4,166/$1,589. The wool-revenue gain is entirely price capture
on unchanged filled volumes. This ledger does not count total harvests.

Validation: trace hooks reproduce an unhooked game exactly; full trace prefixes
through step 503 match bit-for-bit in all 48 candidate games; shop sequences
also match in all 48. Both files pass `kaggle_load_check.py`, including its
official-engine run. `source_manifest.json` records hashes and a direct engine
check that sheep CARE on day 27 can pay on day 29, but CARE on day 28 cannot.

At 09:52 UTC launched `run_gate.py` (session 8734; initial gate PID 23272).
Sequential runs, each `--only-candidates --workers 2 --seeds 906 24`:
1. delivery and capture versus all eight pool members, plus each other (816 games).
2. unchanged sir-V1 and f55rec-V2 as controls on the identical cells (816 games).
Candidate files are frozen while running. No submission decision yet.

Further audits: `prior_worker_branch_audit.json` demonstrates the old generic
sirx worker returns PASS on a cared, fed sheep holding four wool where the
original worker returns HARVEST. The outer reclaim may recover some such
actions, so this is not a claim about the complete sirx agent's lost yield.
`compaction_audit.json` found four same-item BUY crossings among 18 development
compactions; all four sell one fertilizer while eight are already in stock,
so none relies on the intervening purchase to fund stock availability.

`endgame_mechanism.png` / `.pdf` plot the development margin curves and the
exact 900902 wool ledger. Paired margin gains include own revenue and opponent
price suppression: capture vs koshinm gains $443.92 bank and reduces the
opponent bank by $500.08 on average. Against V2 those components are $65.17
and $346.67. Worker correction changes decisions on only 1/6 development
seeds (the expansion is present on 2/6); fresh-seed replication is essential.

Gate analysis detail: in `--only-candidates` mode, the printed MEAN for an
original pool row covers only its candidate opponents. It is not comparable
to a candidate's broader opponent average (which also includes the other
candidate when two are supplied). The separate live-control run supplies
the fair comparison against the same six non-live pool members, and allows
paired margin differences keyed by opponent, seed, and candidate seat.
`analyze_gate.py` also restores the left-agent index omitted by gate.py's
raw `--out` format using its deterministic job order, checking every saved
right-agent/seed/seat tuple before writing named records. Confidence intervals
resample seeds as blocks, keeping both seats together.

## Checkpoint 4 — candidate gate complete, control gate running (10:19 UTC)

First 816 games finished in 1,579.7 seconds, zero failures, [906:930], 48
games per cell. Both candidates have identical W/L/T records against the pool:

| opponent | W/T/L | win score | capture margin |
|---|---:|---:|---:|
| LIVE f55rec-V2 | 46/0/2 | .9583 | +1206.29 |
| LIVE sir-V1 | 39/4/5 | .8542 | +117.42 |
| f55rec-V1 | 48/0/0 | 1.0000 | +987.25 |
| sir-V2 | 46/0/2 | .9583 | +362.38 |
| koshinm | 24/0/24 | .5000 | +27.83 |
| melon | 33/0/15 | .6875 | +1876.69 |
| 2802 | 44/0/4 | .9167 | +2672.83 |
| metav4 | 40/0/8 | .8333 | +438.48 |

Worker increment over delivery is zero on every pool cell except 2802:
seed 900906, both seats, +$1,227 each (+$51.13 across that 48-game cell).
Direct delivery vs capture is 4W/40T/4L, mean $0. The worker's large development
effect is therefore rare and not replicated vs koshinm in this fresh panel.
Do not advertise the +$944 development figure as the fresh expected gain.

Head-to-head targets pass, but the rest-of-pool criterion is pending. Controls
started automatically at ~10:18:55 UTC, PID 25131, same session 8734, same
24 seeds. Raw first-run output is `gate_candidates.json`; named recovered
records are `gate_candidates_records.jsonl`. The simpler delivery arm may be
the better recommendation if controls confirm the field gain.

## Emitted-action firing audit (10:34 UTC)

The internal `changed_turns` counter records proposal changes, including
worker decisions before the reclaim layer. Independent comparison of final
returned actions against the matching baseline traces shows actual divergence:
delivery 168 turns (164 market / 4 unit-action turns); capture 384 turns
(214 market / 224 unit-action turns), each across 24 development games.
These trajectory differences include downstream policy feedback, so they are
not direct intervention counts. Both analyses agree the layers are active;
new-layer exception counts remain zero. Prefixes through step 503 still match.

## FINAL — both gates complete; delivery passes (10:53 UTC)

Controls finished in 1,948.6 seconds, zero failures. Both gate runs together:
1,632 games, all DONE, maximum two workers; all owned benchmark jobs joined
and exited normally. Named records and seed-block bootstrap analysis are in
`gate_*_records.jsonl` and `gate_analysis.json`.

Common six-opponent win score: delivery/capture **81.597%**, unchanged sir-V1
**79.861%**, unchanged f55rec-V2 **49.653%**. Delivery paired margin gain over
the stronger sir control: **+$45.24/game**, 95% seed-block bootstrap
[$15.54,$88.85], n=288 cells / 24 seed blocks. Win-score increment +1.736
percentage points, interval [0,3.819]. Worst paired margin change -$278.
Capture adds only another $8.52/game without extra wins; the worker effect
does not generalize at the magnitude seen in the development panel.

**VERDICT: SUBMIT-WORTHY — cand_delivery.py meets the brief's local thresholds;
recommend the simpler market patch for the orchestrator's held-out confirmation.**
This is a small field edge, not evidence of +$1k/game or +200–300 rating.
`cand_capture.py` remains the second, rare-effect alternative. The final
RESULT.md contains the complete matchup table, mechanism, caveats, and commands.
Both files are frozen, rebuild byte-for-byte (`build.py --check`), and pass
Kaggle loader/official-engine checks. No live files changed; no submission made.
