"""What do the side hands actually spend their turns on?"""
import argparse
import collections
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--set", default=None)
    a = ap.parse_args()
    params = json.loads(a.set) if a.set else {}
    C = load(os.path.join(REPO, "side", "farm.py"), "cand", params)
    R = load(os.path.join(REPO, "port2", "h_over.py"), "ref")

    per_day = collections.defaultdict(collections.Counter)
    myorders = collections.defaultdict(collections.Counter)
    raw = C.agent

    def wrapped(obs):
        act = raw(obs)
        if obs["player"] != 0:
            return act
        s = C._SIDES[0]
        d = obs["step"] // 24
        lo = s.tape_hires
        for h in list(act.get("hands") or [])[lo:]:
            per_day[d][h[0]] += 1
        return act

    r = harness.run_episode(wrapped, R.agent, seed=a.seed)
    assert r["errors"] == [None, None], r["errors"]
    print("reward", r["reward"], "margin", r["reward"][0] - r["reward"][1])
    for d in sorted(per_day):
        c = per_day[d]
        tot = sum(c.values())
        move = sum(v for k, v in c.items() if k in ("NORTH", "SOUTH", "EAST", "WEST"))
        work = tot - move - c.get("PASS", 0)
        print(f"day {d:>2} turns {tot:>3} work {work:>3} move {move:>3} "
              f"pass {c.get('PASS', 0):>3}  " +
              " ".join(f"{k}:{v}" for k, v in sorted(c.items())
                       if k not in ("NORTH", "SOUTH", "EAST", "WEST", "PASS")))


if __name__ == "__main__":
    main()
