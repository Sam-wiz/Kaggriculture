"""Per-day trace of what the side farm actually does on the SE quadrant."""
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--set", default=None)
    a = ap.parse_args()
    params = json.loads(a.set) if a.set else {}
    C = load(os.path.join(REPO, "side", "farm.py"), "cand", params)
    R = load(os.path.join(REPO, "port2", "h_over.py"), "ref")

    rows = []

    def on_step(step, state, env):
        if (step + 1) % 24:
            return
        obs = state[0].observation
        f = obs.farms[0]
        pr = state[0].observation.private
        t = f["tiles"]
        se = dict(empty=0, plant=0, weed=0, locked=0, animal=0, coop=0)
        crops = {}
        for y in range(5, 10):
            for x in range(5, 10):
                tt = t[y][x]
                if tt is None:
                    se["empty"] += 1
                elif tt == "LOCKED":
                    se["locked"] += 1
                elif tt["kind"] == "WEED":
                    se["weed"] += 1
                elif tt["kind"] == "PLANT":
                    se["plant"] += 1
                    crops[tt["crop"]] = crops.get(tt["crop"], 0) + 1
                elif "animal" in tt:
                    se["animal"] += 1
                else:
                    se["coop"] += 1
        rows.append((step // 24, int(f["money"]), len(f["hands"]),
                     len(f["unlocked_quadrants"]), sum(pr["shed"].values()),
                     dict(se), crops, dict(pr["seeds"])))

    r = harness.run_episode(C.agent, R.agent, seed=a.seed, on_step=on_step)
    assert r["errors"] == [None, None], r["errors"]
    print("reward", r["reward"], "margin", r["reward"][0] - r["reward"][1])
    for d, m, h, q, shed, se, crops, seeds in rows:
        print(f"day {d:>2} $ {m:>7} hands {h:>2} quads {q} shed {shed:>3} "
              f"SE {se} {crops} seeds {seeds}")


if __name__ == "__main__":
    main()
