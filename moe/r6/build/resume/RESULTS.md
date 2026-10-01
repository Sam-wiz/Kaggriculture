# Continuation results — 2026-09-27 16:58 UTC

**No submissions. The user requires BOTH Harvest and C1R2 to converge before any upload.**

V8 is a promising adaptive research base, but **fails the existing promotion gate**. It has not
established top-10 private strength. Both forecaster modifications are closed as promotion candidates.

## Completed experiments

| Candidate / opponent | Wins–losses–ties | Design | Mean margin |
|---|---:|---|---:|
| Harvest+456 streams / Harvest | 3–6–11 | 20 fresh seeds, one lineage seat | −$9.50 |
| Same + censor-aware scoring / Harvest | 3–9–8 | Same 20 seeds | −$17.85 |
| Public adaptive V8 / Harvest, screening | 13–7–0 | 20 seeds, seat 0; selected after 5-seed prescreen | +$3,394.30 |
| V8 / Harvest, untouched holdout | **68–12–0** | **40 independent seeds, both seats** | +$5,638.50 |
| V8 / C1R2, same holdout | **58–22–0** | **40 independent seeds, both seats** | +$4,423.25 |

Holdout 95% seed-cluster bootstrap win-rate intervals: Harvest 72.5–95.0%; C1R2 57.5–85.0%.
Both seats have the same win counts (34/40 and 29/40 respectively), but different banks;
seats are not independent trials. No tuning on this holdout.

Historical RR gate: **2149 [2043,2229]** (90% seed bootstrap). Required point >2329 and
lower bound >2152: **FAIL**. V8 vs reference agents: pipe16 27–13, f55V2 32–8,
sirV1 34–6, shepherd 32–8, hyb2965 32–8, C1 30–10 (20 seeds, both seats per opponent).
Harvest's archived reference results are stronger. Do not override this disagreement by
selecting only favorable matchups. The historical rating map was checked against the original
implementation and reproduced Harvest's 2329 [2160,2514] exactly, but has not been calibrated
for this adaptive architecture against the private field.

## Preflight and instrumentation

- Original V8 and strict diagnostic both pass Kaggle's no-`__file__`, last-callable loader.
- Strict diagnostic: three extra fresh closed-loop games, no exceptions. Max measured local
  action 0.0602 seconds under concurrent load; not a Kaggle hardware benchmark.
- Official environment, seed 9203001: both seats DONE; candidate banks 125029 and 130277,
  opponent banks 120849 and 118192. Kagsim reproduces each seat to the dollar.
- All 240 RR + 160 holdout games explicitly count internal V8 exceptions: **zero**.
- New runner uses file hashes + seed + seat identities, flushed resumable records, no silent
  runner fallback. Original borrowed agents may have their own catches; V8's is instrumented.
- Censor fix demonstrably executes: 172961 skipped hidden-observation penalties and 103 Q fire
  turns; plain Q fires 77 times. Neither improves Harvest on the tested seeds.

## Exact evidence and provenance

Source: https://github.com/r34l-rudr44/kaggriculture/blob/main/agents/v8.py
Local source: `rivalsGH/r34l-rudr44_kaggriculture/agents_v8.py`
SHA-256: `6f4a3205b5bd781b370bf03a08c237e28cc6c0bfe23634038309dd92e979dae9`
Public-source reuse/license review remains pending before any packaging or submission.

All records/manifests: `moe/r6/build/resume/`.
- `forecast.jsonl`: 80 games; seeds 9201001..9201020.
- `github.jsonl`: 105 path-correct prescreen games (21 paths), plus V8's 15 additional screen games;
  seeds 9202001..9202020. Only V8 advanced.
- `r34_rr.jsonl`: 240 games; seeds 9100001..9100020.
- `r34_holdout.jsonl`: 160 games; seeds 9204001..9204040.
- `r34_preflight.json`, `r34_swap.jsonl`: official environment / strict / simulator checks.
- `RESULTS.json`: full summaries and bootstrap intervals.

Legacy GH screen limitations: 244 paths were reported under only 169 labels; six names conflate
81 files. The positive ambiguous group was re-screened by path. 75 legacy load failures remain
unevaluated, with implicated paths in `unevaluated_github.json`; they are not proven weak.

## Live hold and next work

Snapshot 09-27 16:55 UTC: Harvest **1788.6**, 29 completed games, age 1.63h;
C1R2 **1672.8**, 35 completed games, age 2.27h. **Neither converged.**

1. Keep both current submissions. Refresh with `.venv/bin/python moe/r6/monitor_pair.py`;
   it saves immutable snapshots, updates notes, and cannot submit or automatically lift the hold.
2. Resolve V8's matchup-specific advantage with representative responsive opponents before changing
   promotion criteria. The older RR is evidence against promotion, not something to hide.
3. Use this new adaptive base for future separately pre-registered improvements; C1's failed macro
   grafts do not establish what works on V8. Keep current holdout sealed from parameter tuning.
4. Recover dependencies for the unevaluated public agents and inspect fresh published updates on
   the next daily sweep. Existing episode fetch PID 1939 was left running.

All experiments started in this continuation are complete. No model API credits or external messages
were used. No submission package was published.
