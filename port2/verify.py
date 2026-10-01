"""Prove a port2 variant is action-for-action identical to port/main.py at its
defaults (or under a given P override).

Runs one agent for real and shadows the other on the SAME observation each turn.
"""
import argparse
import importlib.util
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import harness  # noqa: E402


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cand")
    ap.add_argument("--opp", default="starter")
    ap.add_argument("-n", type=int, default=3)
    ap.add_argument("--set", default=None)
    a = ap.parse_args()

    ref = load(os.path.join(ROOT, "port/main.py"), "vref")
    cand = load(os.path.join(ROOT, a.cand), "vcand")
    if a.set:
        cand.P.update(json.loads(a.set))

    bad = 0
    for seed in range(1, a.n + 1):
        diffs = []

        def wrapper(obs, _d=diffs):
            import copy
            r = ref.agent(copy.deepcopy(obs))
            c = cand.agent(copy.deepcopy(obs))
            if r != c:
                _d.append((obs["step"], r, c))
            return r

        res = harness.run_episode(wrapper, a.opp, seed=seed, catch_errors=False)
        ok = res["errors"] == [None, None]
        print(f"seed {seed}: diffs={len(diffs)} bank={res['reward']} err_ok={ok}")
        if diffs:
            bad += 1
            for s, r, c in diffs[:3]:
                print("   step", s)
                print("     ref ", r["market"])
                print("     cand", c["market"])
    print("IDENTICAL" if bad == 0 else "DIFFERENT")


if __name__ == "__main__":
    main()
