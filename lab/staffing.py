"""Can a micro-farm be staffed from idle unit-turns, or must it hire its own hand?

Two options, with different risks:
  HIRE   - append one HIRE after the tape's, every day. Costs fib(hires_today) per day and touches
           nothing positional, because the new hand lands at the END of farm["hands"] and the tape
           only indexes the ones it hired.
  RETASK - reuse unit-turns the tape wastes. Free, but the unit is then not where the next tape
           action expects it, which is exactly the coupling that has destroyed every previous
           production change.

This measures both: the marginal hire cost per day, and how much genuinely idle unit-time exists --
counting not just PASS but contiguous runs of it, since a micro-farm needs several turns together.
"""
import collections
import statistics
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness
from kaggle_environments.envs.kaggriculture.kaggriculture import _hire_cost

AGENT = "bench_frozen/A_router.py"
OPP = "rivals/leoprovorov_kaggriculture-v65/main.py"


def main(seed=900009):
    hires = collections.Counter()
    idle = collections.defaultdict(list)     # (day, unit) -> list of turns idle
    per_day_units = collections.Counter()

    def on_step(step, state, env):
        a = state[0].action or {}
        day = step // 24
        n = sum(1 for o in (a.get("market") or []) if o and o[0] == "HIRE")
        hires[day] += n
        units = [a.get("farmer")] + list(a.get("hands") or [])
        per_day_units[day] = max(per_day_units[day], len(units))
        for i, u in enumerate(units):
            if u and u[0] == "PASS":
                idle[(day, i)].append(step)

    harness.run_episode(AGENT, OPP, seed=seed, copy_obs=False, on_step=on_step,
                        catch_errors=True)

    print(f"seed {seed}\n")
    print("MARGINAL HIRE COST (one extra hand appended after the tape's own hires)")
    print(f"{'day':>5}{'tape hires':>12}{'next rung costs':>18}")
    tot = 0
    for d in sorted(hires):
        if d < 6:
            continue
        c = _hire_cost(hires[d])
        tot += c
        if d % 4 == 0 or d > 26:
            print(f"{d:>5}{hires[d]:>12}{c:>18,}")
    print(f"   total for days 6-29 if hired every day: ${tot:,}")

    print("\nIDLE UNIT-TIME (PASS actions), by day")
    print(f"{'day':>5}{'units':>7}{'idle turns':>12}{'longest run':>13}")
    for d in sorted(per_day_units):
        if d < 12 or d > 24:
            continue
        turns = sorted(t for (dd, _), ts in idle.items() if dd == d for t in ts)
        best = 0
        runs = collections.Counter()
        for (dd, u), ts in idle.items():
            if dd != d:
                continue
            ts = sorted(ts)
            run = 1
            for a, b in zip(ts, ts[1:]):
                run = run + 1 if b == a + 1 else 1
                best = max(best, run)
            runs[u] = len(ts)
        print(f"{d:>5}{per_day_units[d]:>7}{len(turns):>12}{best:>13}")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 900009)
