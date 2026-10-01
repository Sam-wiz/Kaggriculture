# resim lane — replay re-simulation: CRACKED + bulk extraction done

## Result

**Re-simulation is EXACT.** Every tape tested reproduces final bank to the dollar.

| corpus | eps | exact | within 1% |
|---|---|---|---|
| rawkeep MMPQ full replays (obs ground truth) | 4 | 4 (100%) | 4 |
| mine/top10 random sample | 120 | 120 (100%) | 120 |
| mine/top10 MMPQ (extraction run) | 450 | 450 (100%) | 450 |
| mine/top10 DSM (extraction run) | 554 | 554 (100%) | 554 |
| **total** | **1128** | **1128 (100%)** | **1128** |

Gate (≥90% within 1%): PASSED at 100% exact.

## The divergence — root cause

The orchestrator's reported mismatch (ep 112219779 → resim [101218, 46823] vs
tape [107468, 104194]) was an **action-alignment off-by-one in the driver**, not
an interpreter semantic.

Kaggle replays store `steps[t].action` = the action that *produced*
`steps[t].observation`, i.e. the action submitted at game-step t−1.
`steps[0].action` is the init placeholder (all-PASS dict). So the action that
must be applied at game-step `s` is `actions[s+1]` — `tapefidelity.check`'s
`shift=1` convention. The prior driver applied `actions[s]` at step `s`
(shift=0): every op ran one turn late, which desyncs money early and cascades
( hires fire an hour late → unit streams never line up). `replayaudit.py` had
the right alignment (`t = obs['step']+1`); whatever produced the orchestrator's
numbers didn't.

With shift=1 the official pip interpreter (`kaggle_environments 1.32.7`)
reproduces everything — **no version skew, no action-format munging, no
post-validation normalization** in the tapes. End-of-season: interpreter marks
DONE at `step >= episodeSteps-2` = step 718, so 719 interpreter calls total
(steps 0..718) and tape `actions[1..719]` cover them all.

## Driver

`resim.py`:
- `resim(actions, seed, pre_step=..., on_step=...)` — feeds `actions[s+1]` to
  `K.interpreter` at step `s` via the harness `_Env`/`_AgentState` shim;
  `pre_step` fires after actions are set, before the interpreter call (captures
  the exact observation the agents acted on).
- `resim_top10(path)` — tape wrapper. `bisect_ep.py` — per-step field diff vs a
  full replay (note: recorded per-step `observation` in replay JSONs is the
  mutable shared dict serialized at dump time → all steps show the terminal
  state; only `action`, `reward` fields are per-step. Money/shops still
  cross-check).
- `find_impossible(state)` — flags recorded unit ops that would silently no-op
  (PLANT w/o seeds, PICKUP empty shed, WATER non-plant...). On exact tapes these
  still fire in ~96% of eps (median t≈59): agents emit best-effort ops that
  no-op live too. Only meaningful on non-exact tapes — of which there are none.

## Extraction — `bc2r_*.jsonl`

`extract_bc.py TEAM out.jsonl [workers]`: resims every mine/top10 tape of TEAM,
emits rows in the EXACT `bc_extract_team.py` schema `{ep,t,ui,xy,d,dshed,inv,
on,G,y,y2}` — same `board_scan`/`bfs_nearest`/`cls`/`next_work` code, same
causal pairing `S_{t-1} → action[t]` (row `t` = 1..719; features from the
pre-interpreter state at game-step t−1; `y`/`y2` from tape action index `t`).
Per-episode fidelity + truncation policy recorded in `*.manifest.json` (had
divergences existed, rows would be truncated at the first impossible op —
unused, all eps exact).

- `bc2r_MMPQ.jsonl` — **450 eps, 3,213,581 rows** (~7.1k rows/ep, ~9.9 units).
- `bc2r_DSM.jsonl` — **554 eps, 4,075,068 rows** (~7.4k rows/ep).
  (Existing rawkeep-derived `bc2_DSM.jsonl`/`bc2s_MMPQ.jsonl` covered only the
  ~38/4 full-replay eps; this expands coverage ~12–110×.)

## Notes for consumers

- `G.money` etc. is the observation at decision time (post-step-t−1
  / pre-step-t state), matching bc_extract_team's `steps[t-1].observation`.
- Market orders are not in rows (per bc schema — unit ops only).
- `status` all DONE/DONE; no errored agents in these corpora.
- Divergence hunt on future corpora: check `*.manifest.json` `exact`/`within1`,
  then `first_bad`/`diverge_t` for the suspect step.
