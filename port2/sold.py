"""Uncontested accounting: agent vs `pass`, tracking market inventory drift.

The town drains inventory as well as our selling adding to it, so the absolute
number here is net drift, NOT a unit count.  What it is good for is the
DIFFERENCE between two agents on the same seed: town drain is near-identical,
so the gap in final drift is the gap in units sold.  That separates "sells
more" from "sells the same units earlier".
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import harness  # noqa: E402

PRODUCTS = ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG",
            "MILK", "WOOL", "FERTILIZER"]


def measure(path, seed):
    start = {}
    trace = []

    def on_step(step, state, env):
        inv = state[0].observation.market["inventory"]
        if not start:
            start.update({p: inv[p] for p in PRODUCTS})
        trace.append((step, {p: inv[p] - start[p] for p in PRODUCTS}))

    r = harness.run_episode(os.path.join(ROOT, path), "pass", seed=seed,
                            catch_errors=True, on_step=on_step)
    assert r["errors"] == [None, None], r["errors"]
    final = trace[-1][1]
    # mid-season cumulative sales, to show timing rather than volume
    mid = trace[len(trace) // 2][1]
    return r["reward"][0], final, sum(final.values()), sum(mid.values())


for seed in (1, 7, 42):
    print(f"seed {seed}")
    for path in ("port/main.py", "port2/h_over.py"):
        bank, final, tot, mid = measure(path, seed)
        print(f"  {path:<20} bank={bank:>9.0f}  unitsSold={tot:>5}  "
              f"soldByHalfway={mid:>5}  {final}")
