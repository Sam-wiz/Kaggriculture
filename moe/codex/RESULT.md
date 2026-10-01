VERDICT: SUBMIT-WORTHY — `cand_delivery.py` passes both live head-to-head targets and improves the matched rest-of-pool win score; recommend it for the orchestrator's held-out confirmation.

Recommend **`cand_delivery.py`**, the smaller change. It copies `subV_sir2.py`
verbatim and adds two market corrections only from step 504 onward:

- The premium layer uses the shed projected after this turn's unit actions,
  so newly dropped produce can sell immediately. Existing floors, batch sizes,
  scheduled sells, and subsequent own-sale reconciliation are retained.
- After SIR ordering, SELLs fill earlier empty queue slots. Non-SELL rows
  retain their indices.

Fresh gate: seed-index **[906:930]**, actual seeds **900906–900929**, both seats,
**48 games per matchup**. Candidate and matched-control runs total **1,632
games, zero failures**, pinned real engine 1.32.7, at most two workers.
The candidates were frozen before these seeds were evaluated. This is separate
from development [900:906]; the orchestrator's independent confirmation remains.

| Opponent | Delivery W/T/L | Win score | Mean margin | Paired margin gain vs unchanged sir-V1 |
|---|---:|---:|---:|---:|
| **LIVE f55rec-V2** | 46/0/2 | **95.83%** | +$1,206.29 | +$33.42 |
| **LIVE sir-V1** | 39/4/5 | **85.42%** | +$117.42 | +$117.42 |
| f55rec-V1 | 48/0/0 | 100.00% | +$987.25 | +$94.42 |
| sir-V2 | 46/0/2 | 95.83% | +$362.38 | +$52.46 |
| koshinm | 24/0/24 | 50.00% | +$27.83 | +$31.60 |
| melon | 33/0/15 | 68.75% | +$1,876.69 | +$85.92 |
| 2802 | 44/0/4 | 91.67% | +$2,621.71 | +$16.69 |
| metav4 | 40/0/8 | 83.33% | +$438.48 | −$9.63 |

Win score counts ties as half wins. Paired gains match opponent, seed, and seat.
Against the **same six non-live opponents** (288 games per build), delivery
scores **81.60%**, versus **79.86%** for live sir-V1 and **49.65%** for live
f55rec-V2. Thus sir-V1 is the stronger live control on this pool.

Delivery adds **+$45.24 paired margin/game** across those six opponents;
95% seed-block bootstrap interval **[$15.54, $88.85]**. Win-score gain is
**1.74 percentage points**, interval **[0, 3.82]**. Resampling keeps both seats
and all opponents of a seed together. Worst paired margin change is **−$278**.
The field improvement is small; these results do **not** establish a
$1k/game improvement or a 200–300 rating increase. In particular, koshinm
improves from the live control's 45.83% to 50%, rather than becoming dominated.

The second file, **`cand_capture.py`**, adds a V233 worker planning correction:
mark CARE complete in a private planning view when today's care can no longer
contribute to a payable yield. The existing controller then advances to
harvesting, collection, and delivery instead of repeatedly emitting CARE that
reclaim converts to PASS. It preserves the original harvest/collection branches.

Capture has **identical pool W/T/L records** to delivery on the fresh slice.
Its only additional pool margin is +$1,227 in each seat of seed 900906 vs 2802:
an extra +$8.52 averaged across the six other opponents, with no additional wins.
Direct delivery/capture comparisons have zero paired margin on every seed.
The larger worker effect is real in the traced failure but rare in this gate;
keep this file as the alternative, rather than advertising the development gain
as its fresh expected effect.

The endgame diagnosis is now more precise:

- **There is no missing route-648 switch:** the entire decoded route-2 tape is
  identical in koshinm and sir-V1 (`decode_report.json`). Koshinm adds market
  portfolio/frontload/adaptive/sale-advance/SIR wrappers around that tape.
- Baseline development traces, six seeds × both seats vs koshinm: mean margin
  −$110.58, days 21–29 sale-revenue gap −$140.42. Both sides fill 1,431 pooled
  wool sales in that window, at $56.60 vs $59.28. During steps 648–718 the
  pooled prices are $52.99 vs $60.79; the quoted $11/unit gap is not universal.
- **Concrete delivery stall:** seed 900902 seat 0 loses $1,150. At steps
  657–669 two of our sheep workers repeatedly PASS while koshinm proceeds to
  other sheep and delivers. During steps 648–718 both fill 62 wool sales, but
  receipts are $2,084 vs $3,992. Capture changes them to $4,166 vs $1,589 and
  the game margin to +$3,498: **+$4,648 paired margin**. Both sides still fill
  363 wool sales across the game. These are filled sales, not inferred harvests.
- Development means were +$178/+944 for delivery/capture vs koshinm and
  +$54/+$412 vs V2, 12 games per matchup. The fresh gate above supersedes
  those larger estimates. A direct engine check also confirms that the refresh
  after day 28 can produce day-29 yield, while care banks *after* that refresh's
  production; care on the day immediately before the last payout is too late.

Instrumentation and validation:

- `trace.py` hooks **successful `_commit_unit` calls**, recording individual
  fill prices and queue indices. Every step's bank reconciles against those
  fills plus actual hire, land, and unit-action costs. Projected shed stock
  matches the engine's actual pre-market stock. A hooked/unhooked game matches.
- Across 24 development games per candidate, internal telemetry records 82
  changed decision turns for delivery and 198 for capture (including 188
  changed worker proposals). Independent final-action comparisons show 168
  and 384 changed turns respectively, including downstream feedback. **Zero
  new-layer exceptions.** Prefixes through step 503 and shop draws match base.
- Both final callables are `_ec_agent`; both files pass `kaggle_load_check.py`,
  including official-engine smoke runs. Source hashes remain unchanged and
  `build.py --check` reproduces both files byte-for-byte.

Reproduce the two gate runs with:

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python moe/gate.py --only-candidates --workers 2 --seeds 906 24 --out moe/codex/gate_candidates.json delivery=moe/codex/cand_delivery.py capture=moe/codex/cand_capture.py
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python moe/gate.py --only-candidates --workers 2 --seeds 906 24 --out moe/codex/gate_controls.json sir_control=subV_sir2.py f55_control=subV2_f55rec.py
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python moe/codex/analyze_gate.py
```

Evidence: `gate_analysis.json`, `gate_*_records.jsonl`, `gate_*.log`, and
`gate_manifest.json`; per-step filled-sale CSV `endgame_fills.csv`; full
ledgers `traces*/`; `trace_analysis.json`; development-only mechanism plot
`endgame_mechanism.png`/`.pdf`. `NOTES.md` records the work and source audits.
All edits are under `moe/codex/`. No Kaggle submission was attempted.
