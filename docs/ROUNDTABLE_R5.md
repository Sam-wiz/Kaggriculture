# Round table r5 — the build session: closing ~700 Elo to 3k+ before freeze

You are one of three senior engineers (Devin, Claude, Codex-Astra). This is a BUILD
session, not more analysis. Read `HANDOFF.md`, `MEMORY.md`, `ROUNDTABLE.md`,
`TOP10_DECODE.md` first — the falsified list is long, do not re-propose dead ideas.
Engine: `.venv/lib/python3.14/site-packages/kaggle_environments/envs/kaggriculture/kaggriculture.py`.

## Position right now (09-24 ~16:00 UTC, freeze 09-30)

- Live: `subV_sirxL96` (ref 56495194) @2225 after ~26h/173eps; `subV2_sirxP` @2072
  still converging as fallback. `subV2_sirxL96.py` goes out at next quota window.
- Best-ever frozen score: 2552 (subV2_f55rec). Top-10 cutoff ~2977, leaders ~3100.
- **Gap to 3k+: ~500-700 Elo. Every market-layer lever is now exhausted or falsified.**
- A new submission needs ~2-3 days to converge → **anything new must ship by ~09-27**.
- Quota: 5 subs/day, resets ~00:00 UTC. Currently free.

## What the decode proved (the ONLY remaining edge)

Replaying tetsuya (lb~2953) action-for-action, rewards reproduced to the dollar:

| | us | tetsuya |
|---|---|---|
| revenue | $114.2k | $113.7k — equal |
| spend | $28.3k | **$19.6k** |
| feed-wheat buys | $8.65k / 239u | $3.25k / 96u (grows feed) |
| fert buys | $2.4k | **$0** |
| animals placed | 23 | 19 (0 geese despite 437 orders) |
| carrot sold | 162 @ $45 | **324 @ $49** |
| strawberry sold | 251 @ $40 glutted | 200 @ $87 |

The edge is **demand-matched production mix + lean inputs**: plant carrots ∝
carrot-shop draw, grow feed wheat instead of buying, cap strawberry below glut,
fertilize from collection only. It is decided by ~day 6-15. Same revenue on $8.7k
less spend. Top-10 agents emit a different buy signature every game — they replan
against the shop draw; we commit at day 6.

## Our architecture (the constraint + the opportunity)

`subV_sirxL96.py`: `_IMPL = make_agent(_ROUTES, router=_router)` where
`routes = {route_id: [720 action dicts]}` — 144 embedded tapes (base85 blob
`_R108_DATA`), router called every step (commits ~day 6 from first-2-shop
signature), then the overlay stack (SIRX market reorder, f55 floors, reclaim,
projected-shed prem overlay, L96 endgame lead, E182 terminal planner) executes
on top. ~1MB single file, stdlib only.

Infrastructure that exists:
- `mine/tapes/` — **223 mined full tapes from top-10 teams' real episodes**
- `mkshoprouter.py` — packages {library + day-6 router} into a submission
- `route_remap.py`, `route_data*.py`, `routefit.py` — route-margin analysis
- `harness.run_episode`, `bench_vs.py` — paired seeded eval both seats
- Full engine source locally; replay offsets decoded (+1 step)

## Falsified this session (measured — do NOT re-propose)

- market_counterfactual_selector: −46 (12-16). market_queue_lockstep: −46 (10-16).
  Root cause: sim can't see the same-index lockstep race.
- Sell phase-shift to step%4==1: counterfactual −$1,185.
- CXO confidence-gated herd swap (shiiin9 port): NULL — 0 fires, our day-6
  router already demand-matches the herd.
- Fertilizer-buy trim: bought units get consumed/resold at a gain, not waste.
- Tomato 2-shop annex gate: −1809 tail when it fires. E1 prem-off: −171.
- Blind aspiration-order spam: no effect (engine caps at cash).
- koshinm route-2 sell schedule: byte-identical to ours — no gap.
- Prior attempt: naive mined-tape replay −0.586 WR (draw-dependence; fixed by
  the day-6 switch + shared prefix).

## The question on the table

**ONE buildable plan to capture the production-mix edge within ~48-72h of work
that can ship by 09-27.** Candidates, in rough order of prior plausibility:

A. **Demand-keyed route expansion** — mine/record top-10 tapes whose plans are
   demand-specialized (carrot-heavy, wheat-feed, lean-animal), register them in
   the router keyed on a richer shop-draw signature. Approximates replanning
   with zero live-planning risk. Feasibility Q: can we extract per-draw
   specialized tapes from mine/tapes or generate fresh ones?
B. **Bounded live replanner** — replace only the *plant/hire/animal* decisions
   days ~6-15 with a draw-conditioned planner, keep tape execution skeleton +
   all overlays. Narrow scope vs full replan.
C. **Parametric plan generator** — write the offline planner once (plant counts
   by crop ∝ shop signature, feed-wheat self-sufficiency, fert-collect-only),
   synthesize N routes, feed the existing router. A = C with a generator.
D. Accept plateau, polish convergence, select best pair at freeze.

## Private-leaderboard lens (the user explicitly asked)

- Final scoring = unseen seeds/opponents → prefer mechanisms that read the live
  draw (generalize) over rival-specific counters (overfit).
- The freeze snapshot = whatever submissions are selected then; convergence
  runway is the hard constraint, not exploration breadth.
- Demand-matched production is the most generalizable decoded edge — it wins
  on ANY draw distribution because it reacts to the actual shops.

## Deliverable from each of you

1. Pick ONE plan (A-D or a variant) with the honest EV estimate in Elo.
2. Concrete file-level spec: what gets built, where it plugs in, what machinery
   already exists, what the failure modes are.
3. The kill criteria: what measurement in the first 4 hours tells us it's dead.
4. Time-to-submittable estimate and what we sacrifice if it slips past 09-27.
Do not propose anything on the falsified list. Do not propose a full reactive
replanner — already ruled unreachable. Be concrete, not exhaustive.
