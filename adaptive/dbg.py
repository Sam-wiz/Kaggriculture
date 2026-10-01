"""Dump one day of unit decisions: positions, carried wheat, chosen action, and
the FEED tasks that were available but not taken."""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import harness  # noqa: E402


def load(path):
    spec = importlib.util.spec_from_file_location("dbgmod", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["dbgmod"] = mod
    spec.loader.exec_module(mod)
    return mod


def run(path, opp, seed, target_day, hours=(0, 1, 2, 3, 8, 14)):
    mod = load(path)
    fn = mod.agent

    def wrapped(obs):
        act = fn(obs)
        d, h = obs["day"], obs["hour"]
        if d != target_day or h not in hours:
            return act
        f = mod._AGENT
        me = obs["player"]
        farm = obs["farms"][me]
        units = [list(farm["farmer"])] + [list(x) for x in farm["hands"]]
        acts = [act["farmer"]] + list(act["hands"])
        print("--- day %d hour %d  money=%d shedW=%d nAnimals=%d unfed=%d"
              % (d, h, farm["money"], f.shed.get("WHEAT", 0), f.n_animals, f.n_unfed))
        tasks = f.build_tasks(d)
        feeds = sorted([t for t in tasks if t[2] == "FEED"], key=lambda t: -t[4])
        tops = sorted(tasks, key=lambda t: -t[4])[:8]
        print("    top tasks:", [(t[2], t[3], round(t[4])) for t in tops])
        print("    FEED tasks: n=%d  values=%s"
              % (len(feeds), [round(t[4]) for t in feeds[:6]]))
        for i, (ux, uy) in enumerate(units):
            inv = f.invs[i] if i < len(f.invs) else {}
            print("      u%-2d @(%d,%d) zone=%d wheat=%d fert=%d inv=%s -> %s"
                  % (i, ux, uy, f.zone_of(ux, uy), inv.get("WHEAT", 0),
                     inv.get("FERTILIZER", 0),
                     {k: v for k, v in inv.items() if k not in ("WHEAT", "FERTILIZER")},
                     acts[i] if i < len(acts) else None))
        return act

    r = harness.run_episode(wrapped, opp, seed=seed, catch_errors=False)
    print("bank", r["reward"])


if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
