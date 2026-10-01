# MoE brief — Kaggriculture, 2026-09-25 (deadline 2026-09-30 23:59 UTC)

You are one expert in a two-expert mixture (Codex gpt-6-astra xhigh + Claude Opus 5.5 xhigh).
Claude Code (the orchestrating session) is the gate: it runs the final tests and decides what,
if anything, gets submitted. **You cannot submit to Kaggle and must not try.**

## Objective
Flat $5k prizes for ranks 1-10. Top-10 cutoff on the live board today: **~2922**.
Final standings = Bradley-Terry refit over post-deadline games between the two active agents of
each team; team score = better of its two agents (Kaggle Staff, verbatim, discussions.md V4).
Our best builds converge around **2600-2750**. Your job: find the change that raises our win rate
against the **2400-2900 opponent band** — that is where the ~200-300 points are lost.

## Read first (fast)
- `HANDOFF.md` §5 (falsified approaches) and the timeline from `## 09-22n` to the end (09-23 SIR,
  09-23 r3 forensics, 09-25 band analysis, 09-25b, 09-25c). Do NOT re-propose anything in §5 or
  anything the timeline marks dead (rescue overlays, BUY reorder, alpha sweeps, noprem, etc.).
- `AGENTS.md` below the banner = game rules. Engine: `.venv/.../kaggle_environments/envs/kaggriculture/kaggriculture.py`.
- `MISTAKES.md` — our recurring instrument failures. The top one: an overlay that silently never
  runs (`except Exception: pass`, or a wrapper chain whose final `agent=` is not your wrapper).
  **After appending any wrapper, grep the final `agent=` assignment and prove your layer fires.**

## Current live pair (do not modify these files)
- `subV2_f55rec.py` (metav4 chassis + clamp + premium layer f55 + rec/reclaim) — live 56531508
- `subV_sir2.py` (pipe16 chassis + reclaim + SIR sell-impact reorder) — live 56532595
Other builds on disk: subV_f55rec.py, subV2_sir.py, subV_sirx*.py, subV2_sirx*.py, subM_pipe16clamp.py.

## Known facts you can build on
- Market: orders resolve index-by-index in per-unit lockstep; unit actions run BEFORE the market
  each step; drains at step%4==0 after market; day 29 has no end-of-day refresh (last payable
  production day 28); 10 market orders/turn cap; only WHEAT/FERTILIZER can be bought back.
- vs koshinm (the one agent that beats our builds): identical production/buy schedule; we lead
  through step ~480 then bleed ~$1k in days 24-29 on price capture (their WOOL sells capture
  +$11/unit); their chassis switches to a dedicated route at step 648.
- Live loss classes (09-23 r3): production mix (opponent tomato annex, our V219 gate declines at
  2 tomato-demand shops), reclaim deadlock (fixed in sirx), empty-slot defeat, same-turn shed
  blindspot (premium overlay reads pre-action shed).
- Blowouts (-20k..-28k) come from opponent-induced cash troughs on days 6-9 making animal buys fail;
  three rescue grafts all measured net-negative — thread closed.
- Weed/shop RNG: one draw per EMPTY tile, shared stream; seed is NOT observable. Not exploitable.

## Measurement rules (non-negotiable)
- Use `moe/gate.py` (round-robin, real engine, both seats). `fieldtest.py` is a SATURATED gate —
  do not use it to rank candidates.
- Seed slices already used: [1150:1270], [1300:1354]. Use your own fresh slice:
  **Codex: [900:1000]; Opus: [1000:1100]**. Confirmation runs by the gate use a held-out slice.
- **Max 2 worker processes** (`--workers 2`). The machine has 8 cores / 8.6 GB shared by 3 agents.
  Reap your own background jobs by explicit PID. Never kill processes you did not start.
- n matters: a 16-game panel cannot resolve effects < 0.1. Report n, and paired margins.
- Report failures honestly. A clean negative result is useful; a dressed-up marginal one is not.

## Deliverable
Work only under `moe/<you>/` (codex -> `moe/codex/`, opus -> `moe/opus/`). Keep `NOTES.md` there
updated as you go (so progress survives if you are cut off). At the end:
1. `moe/<you>/cand_<name>.py` — a single self-contained agent file (copy a live file, add your
   layer; the final line must bind `agent` to your wrapper). Up to 2 candidates.
2. `moe/<you>/RESULT.md` — what the change is, the mechanism, and gate evidence:
   `python moe/gate.py --only-candidates --workers 2 --seeds <your slice> cand=moe/<you>/cand_x.py`
   Target: beats BOTH live builds >= 0.60 over >= 48 games each, and its mean vs the rest of
   the pool is not below the stronger live build's.
3. An explicit verdict line: `VERDICT: SUBMIT-WORTHY` or `VERDICT: NOT READY` with one sentence why.

Do not edit HANDOFF.md, AGENTS.md, sub*.py, or anything outside moe/<you>/.
Time budget: aim to finish within ~3 hours; write NOTES.md checkpoints every major step.

## Your lane
