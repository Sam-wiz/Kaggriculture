"""Prove the market-model overlay runs, and see what it changes.

Both the wrapper and the overlay swallow exceptions so a crash degrades to the bare route instead
of forfeiting the game. That is right for a submission and dangerous for a benchmark: a layer that
throws on every turn is indistinguishable from a layer that decided to do nothing. This counts
turns, modifications, added units and exceptions explicitly.
"""
import collections
import importlib.util
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


def instrument(m):
    stats = collections.Counter()
    orig_call = m._Overlay.__call__

    def spy(self, action, obs, step, route, protect):
        stats["turns"] += 1
        before = [tuple(o) for o in (action.get("market") or [])]
        try:
            out = orig_call(self, action, obs, step, route, protect)
        except Exception as e:
            stats["exceptions"] += 1
            stats["exc_" + type(e).__name__] += 1
            raise
        after = [tuple(o) for o in ((out or {}).get("market") or [])]
        if after != before:
            stats["modified"] += 1
            b = sum(o[2] for o in before if o and o[0] == "SELL" and len(o) > 2)
            a = sum(o[2] for o in after if o and o[0] == "SELL" and len(o) > 2)
            stats["units_added"] += max(0, a - b)
        return out

    m._Overlay.__call__ = spy
    return stats


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "bench_frozen/M_model.py"
    opp = "rivals/leoprovorov_kaggriculture-v65/main.py"
    m = load(path, "mmcheck")
    stats = instrument(m)
    print(f"{'seed':>8}{'baseBank':>10}{'modelBank':>11}{'delta':>9}"
          f"{'turns':>7}{'modified':>10}{'unitsAdd':>10}{'exc':>6}")
    for seed in (700009, 700010, 700034, 700043, 700107):
        stats.clear()
        rb = harness.run_episode("bench_frozen/A_router.py", opp, seed=seed, catch_errors=True)
        rm = harness.run_episode(m.agent, opp, seed=seed, catch_errors=True)
        print(f"{seed:>8}{rb['reward'][0]:>10,.0f}{rm['reward'][0]:>11,.0f}"
              f"{rm['reward'][0]-rb['reward'][0]:>+9,.0f}"
              f"{stats['turns']:>7}{stats['modified']:>10}{stats['units_added']:>10}"
              f"{stats['exceptions']:>6}")
    if stats["exceptions"]:
        print("\nEXCEPTION TYPES:", {k: v for k, v in stats.items() if k.startswith("exc_")})
