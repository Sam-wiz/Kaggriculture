# MoE r8 — build the top-2 clone. 2026-09-30 ~08:00 UTC. Upload deadline 18:00 UTC, 3 slots left.

Orchestrator: **devin**. Lanes run as parallel subagents. Each lane writes ONLY under
`moe/r8/build/<lane>/` and may append to `moe/r8/THREAD.md`. Do not touch `agents/`,
`subAB_m30b.py`, `HANDOFF.md`, or each other's dirs. No submissions — orchestrator decides.

## Goal

Clone the private top-2 (MMPQ ~3115, DSM ~2943) closely enough to beat `subAB_m30b.py`
in local closed-loop gates (both seats, multi-seed, WR + margin). Everything decoded so
far is in HANDOFF.md 09-29c..k and 09-30a/b.

## Key facts (measured, do not re-derive)

- `mine/top10/*.json.gz`: ~450 MMPQ tapes, keys = episode_id, seed, teams, rewards,
  shops, actions[720][2] = {farmer, hands, market}. **No observations.**
- `mine/rawkeep/*.json.gz`: hundreds of full replays WITH per-step obs (all players'
  private state). MMPQ appears as opponent in ~38 → `bc2s_MMPQ.jsonl` (26.8k rows).
  `bc_DSM.jsonl` 347k rows; `bc2s_{mtmr,TFC,UMG,Vadim}.jsonl` 270-290k each.
- Interpreter RNG: `random.Random((seed*1_000_003)^day)` per day for weeds+shop draws —
  VERIFIED deterministic in-process; resim of a tape reproduces all 8 shop draws exactly.
  But resim money diverges from tape rewards (101218/46823 vs 107468/104194) → some
  action-application detail differs. Crack it = 450 MMPQ episodes of full obs+action data.
- `moe/r7/build/devin/clone_dsm_bc.py`: existing clone — hardcoded DSM program tables
  (HIRES/LAND_DAYS/HERD_PLAN/STRUCT_PLAN/CROP_PLAN) + rule dispatcher where a trained
  56→128→64→31 MLP only picks WHICH pending job to walk toward. Measured: loses
  ~45.6k vs 95.3k to agents/v8x.py. `clone_bc_pool.py` is dead (~1k).
- Decoded dispatch spec (DSM): stay-and-finish (~52% same-tile work chains) →
  step-toward-nearest-pending-job (~92% of moves) → momentum tie-break (60.6%) →
  static per-unit territories (80% of work within R4 of home).
- Decoded market template (DSM): HIRE×k(day)@h0 ramp 4→11; scheduled buys
  (COW every ~2h d6-18 affordability-only, GOOSE d6, MELON d0-2, LAND d6+d9);
  standing SELL ~3/product every turn.
- MMPQ program (fresh decode, per-episode): hires ~4.7→11.7/day, land sporadic d4-12,
  order-SPAM style (issues aspirational qty, engine caps), seeds/ep
  W188/S40/M12/C41/T2, sells/ep W584/MILK230/STRAW220/CARROT130/EGG124.
- Falsified (do not rebuild): hard mission commitment (v8m −46k), momentum graft on
  v8 (4-20), max_quads=4 (7-25), open-loop tape replay as gate, per-candidate Q−V
  argmax (caps ~15-25%).
- Harness: `harness.match(a, b, seeds, swap=True)` → (wa,wb,ties,records);
  `harness.run_episode(a,b,seed=s)` → reward/status/errors. Agent = .py path with
  `def agent(obs)->dict`. Anchors: `agents/v8x.py` (our best fixed agent),
  `subAB_m30b.py` (elite chassis, live anchor — THE gate).

## Lanes

- **resim** — make tape re-simulation exact. Feed recorded actions through
  `K.interpreter` (see harness.py lines 95-160 for the driver pattern), find where
  the trajectory diverges (first impossible/mismatched action), fix the driver until
  final money matches tape rewards on ≥5 episodes across ≥2 teams. Then bulk-extract
  (obs,action) rows for MMPQ into `build/resim/bc2r_MMPQ.jsonl` in the SAME schema as
  `mine/rawkeep/bc_extract2.py` produces (see bc2s_MMPQ.jsonl row shape).
- **clonefix** — diagnose `clone_dsm_bc.py`: run it vs v8x logging per-day
  money/hands/production, find WHERE it falls behind (which day, which subsystem).
  Repair the broken layer(s) → `build/clonefix/clone_dsm_bc2.py`. Gate vs v8x AND m30b.
- **prog** — `v8x` chassis + decoded top-team program as fixed schedule (program tape
  overlay). v8x already derives plans reactively; test whether hard-program targets
  (hire table, land days, herd plan, crop windows, standing sells) beat reactive.
  → `build/prog/v8prog.py`. Gate vs v8x AND m30b.
- **mmpq** — deepen the MMPQ decode using rawkeep obs files where MMPQ is a player:
  EXECUTED (not issued) hires/land/herd/plants per day, dispatch stats (stay-finish %,
  nearest-job %, territory map, tie-break), market template vs DSM's. Any structural
  difference from DSM is a finding. → `build/mmpq/FINDINGS.md` + `programs_MMPQ.json`.

## Gate protocol (every candidate)

1. DONE both seats, zero errors on ≥4 seeds first.
2. `harness.match` vs `agents/v8x.py` on ≥16 seeds ×2 seats.
3. If ≥ v8x: `harness.match` vs `subAB_m30b.py` ≥24 seeds ×2 seats.
4. Report W-L-T + avg margins in `moe/r8/THREAD.md`. Promotion bar: beat m30b.
