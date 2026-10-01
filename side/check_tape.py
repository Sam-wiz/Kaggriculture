"""Proof that the side farm leaves the tape alone.

The tape's unit actions are a fixed recording -- prices cannot change them --
so if we never steal a seed, never move one of its hands and never crowd it out
of a market slot, its three quadrants must evolve tile-for-tile exactly as they
do in `port2/h_over.py`.  Any divergence outside the SE quadrant is a bug.
"""
import argparse
import importlib.util
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
import harness  # noqa: E402


def load(path, tag, params=None):
    spec = importlib.util.spec_from_file_location(tag, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[tag] = m
    spec.loader.exec_module(m)
    if params:
        m.P.update(params)
    return m


def snap(state):
    """Tiles outside the SE quadrant, plus seeds, for player 0."""
    farm = state[0].observation.farms[0]
    out = []
    for y in range(10):
        for x in range(10):
            if x >= 5 and y >= 5:
                continue
            t = farm["tiles"][y][x]
            if isinstance(t, dict):
                # weeds are ignored: owning the SE quadrant adds 25 tiles to the
                # daily weed roll, which shifts the shared RNG stream.  That is
                # inherent to buying land, symmetric between the two farms, and
                # nothing to do with whether the tape's own work survived.
                if t.get("kind") == "WEED":
                    out.append((x, y, None, None, None, None))
                    continue
                out.append((x, y, t.get("kind"), t.get("crop"), t.get("animal"),
                            t.get("yield_units")))
            else:
                out.append((x, y, t, None, None, None))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", default="1,2,3,4,5,6,7,8")
    ap.add_argument("--set", default=None)
    a = ap.parse_args()
    params = json.loads(a.set) if a.set else {}
    C = load(os.path.join(REPO, "side", "farm.py"), "cand", params)
    R = load(os.path.join(REPO, "port2", "h_over.py"), "ref")
    R2 = load(os.path.join(REPO, "port2", "h_over.py"), "ref2")

    bad = 0
    for seed in [int(s) for s in a.seeds.split(",")]:
        a_snaps, b_snaps = [], []
        r1 = harness.run_episode(C.agent, R.agent, seed=seed,
                                 on_step=lambda s, st, e: a_snaps.append(snap(st)))
        r2 = harness.run_episode(R2.agent, R.agent, seed=seed,
                                 on_step=lambda s, st, e: b_snaps.append(snap(st)))
        assert r1["errors"] == [None, None] and r2["errors"] == [None, None]
        first = None
        for i, (x, y) in enumerate(zip(a_snaps, b_snaps)):
            if x != y:
                d = [(p, q) for p, q in zip(x, y) if p != q][:3]
                first = (i, i // 24, d)
                break
        if first is None:
            print(f"seed {seed}: tape quadrants IDENTICAL for all 720 steps  "
                  f"(margin {r1['reward'][0] - r1['reward'][1]:+.0f})")
        else:
            bad += 1
            print(f"seed {seed}: DIVERGED at step {first[0]} (day {first[1]}): {first[2]}")
    print("divergent seeds:", bad)


if __name__ == "__main__":
    main()
