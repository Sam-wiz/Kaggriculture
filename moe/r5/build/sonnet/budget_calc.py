"""
r5 sonnet — planning-budget calculator for Architecture B (runtime forward simulation).

Kaggriculture's actual per-agent time budget (confirmed against the installed
kaggle_environments package, envs/kaggriculture/kaggriculture.json, and agent.py/core.py's
overage-accounting code):
  - actTimeout = 1s: free per step, does not accumulate/bank.
  - remainingOverageTime = 60s TOTAL, shared across the entire 720-step (30-day) episode.
    Only time spent beyond the 1s/step free allowance is drawn from this pool, and it never
    refills. Exceed it and the agent is timed out (an automatic loss, worse than any economic gap).

This script takes measured ms/frame numbers (from bench_realengine.py) and answers the concrete
question opusb/architecture-B need answered: how many candidate-plan rollouts, of what horizon,
fit in the 60s pool if concentrated at the natural decision points (town-shop unlocks, which land
on day 3, 6, 9, ... i.e. steps 72, 144, 216, ... -- up to 8 instances per BRIEF/README).

Run: .venv/bin/python moe/r5/build/sonnet/budget_calc.py
"""

TOTAL_POOL_S = 60.0
FREE_PER_STEP_S = 1.0  # not banked; irrelevant to a rollout that itself takes >1s

# ms/frame at three fidelity levels (from bench_realengine.log, 09-26):
MS_PER_FRAME = {
    "trivial surrogate policies (near pass/pass)": 2.30,
    "realistic policy cost (actual chassis complexity, e.g. hyb2965/C1)": 12.85,
}

HORIZONS_DAYS = [1, 3, 7, 14, 30]
DECISION_POINTS = [1, 5, 8, 10, 15]  # 8 = one per town-shop unlock (the natural count)


def rollout_cost_s(ms_per_frame, horizon_days):
    steps = horizon_days * 24
    return steps * ms_per_frame / 1000.0


def main():
    for label, mspf in MS_PER_FRAME.items():
        print(f"\n=== {label}: {mspf} ms/frame ===")
        print(f"{'horizon(days)':>14} | {'cost/rollout(s)':>16} | " +
              " | ".join(f"branches @ k={k:>2}" for k in DECISION_POINTS))
        for h in HORIZONS_DAYS:
            c = rollout_cost_s(mspf, h)
            row = []
            for k in DECISION_POINTS:
                budget_per_decision = TOTAL_POOL_S / k
                branches = budget_per_decision / c if c > 0 else float("inf")
                row.append(f"{branches:7.2f}")
            print(f"{h:>14} | {c:>16.2f} | " + " | ".join(f"{r:>14}" for r in row))

    print("""
Reading this table:
  - "branches @ k=N" = how many full-fidelity candidate rollouts of that horizon you can afford
    PER decision point if you spend the 60s pool evenly across N decision points during the game.
  - k=8 is the natural count (one decision per town-shop unlock, README default townShopUnlockInterval=3
    up to 8 instances). k=1 is "spend it all on a single planning event" (e.g. only the day-0 land/
    animal opening).

Headline numbers (realistic policy cost, 12.85 ms/frame):
  - A single FULL 30-day rollout costs ~9.25s. Only ~6 fit in the whole 60s pool, whole-game total,
    not per decision -- there is no version of "simulate to game end at every shop unlock" that fits.
  - A 3-day lookahead (72 steps) costs ~0.93s/rollout: ~6.5 branches per decision at k=8, i.e. enough
    for a coarse 2-3-way A/B/C compare at every shop unlock, nothing deeper (no tree search, no
    opponent-response modelling loop).
  - A 7-day lookahead costs ~2.16s/rollout: ~3.5 branches per decision at k=8 -- still only a shallow
    compare, and this already assumes the rollout's OWN plan-generation/scoring code costs ~0, which
    it will not.

Bottom line: architecture B, as scoped in the BRIEF ("simulate candidate plans forward with the
engine and pick the best"), is not affordable as a general search procedure under the real budget.
The only versions that fit are: (a) a handful (<=8-10) of decision points, (b) short horizons
(<=3-7 days), (c) 2-3 candidate branches, (d) cheap surrogate policies for the simulated future, not
the full chassis. That is a narrow, purpose-built heuristic check bolted onto a scripted plan
(closer to architecture C with a look-ahead sanity check at shop unlocks), not a standalone planner,
and it still has to be built, debugged and proven not to time out -- from zero, in the days remaining.
""")


if __name__ == "__main__":
    main()
