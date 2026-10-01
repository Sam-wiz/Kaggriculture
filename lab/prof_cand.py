"""Profile candidate agents' macro farm plan vs `pass`: plants, animals, PASS count."""
import collections
import os
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

FILES = {
    "v48": "rivals/ahmedberatozer_kaggriculture-v48-clear-the-queue/_entry.py",
    "seyit2820": "rivals/seyitkaangunes_kaggriculture-2820-score/_entry.py",
    "yeshawang": "rivals/yeshawang_kaggriculture-agent-evolution-public-notebook/_entry.py",
    "xz_auto": "rivals/xuanzhang001_kaggriculture-auto-top1/_entry.py",
    "xt_capacity": "rivals/xuantianfengwu_kaggriculture-capacity-release/_entry.py",
    "tetsutani": "rivals/tetsutani_shop-aware-farming-kaggriculture/_entry.py",
    "mzcao7": "rivals/mzcao7_kaggriculture-2476-8-peak-lightgbm-xgboost/_entry.py",
    "xt_cow": "rivals/xuantianfengwu_kaggriculture-day-3-cow-challenger/_entry.py",
    "degnon": "rivals/degnonguidi_best-agent-ranking/_entry.py",
    "pipe7": "rivals/nathanjacob_kaggriculture-pipe-7-wheat-microstructure/_entry.py",
}


def kload(path):
    src = open(path).read()
    env = {}
    exec(compile(src, path, "exec"), env)  # noqa: S102
    return [v for v in env.values() if callable(v)][-1]


def _job(a):
    name, path, seed = a
    try:
        agent = kload(path)
        recs = []
        def on_step(step, state, env):
            recs.append(state[0].action)
        r = harness.run_episode(agent, "pass", seed=seed, catch_errors=True, on_step=on_step)
        plants = collections.Counter(); animals = collections.Counter()
        npass = nact = 0
        land = []
        for act in recs:
            units = [act.get("farmer") or ["PASS"]] + list(act.get("hands") or [])
            for u in units:
                if not u:
                    continue
                nact += 1
                if u[0] == "PASS":
                    npass += 1
                if u[0] == "PLANT" and len(u) > 1:
                    plants[u[1]] += 1
            for o in (act.get("market") or []):
                if o and o[0] == "BUY_ANIMAL" and len(o) > 2:
                    animals[o[1]] += int(o[2])
                if o and o[0] == "BUY_LAND":
                    land.append(len(land))
        return (name, seed, r["reward"][0], npass, nact, dict(plants), dict(animals),
                None if r["status"][0] != "ERROR" else r["errors"][0])
    except Exception as e:
        return (name, seed, -1, -1, -1, {}, {}, repr(e)[:200])


def main():
    seeds = [2001, 2002]
    names = sys.argv[1].split(",") if len(sys.argv) > 1 else list(FILES)
    jobs = [(n, FILES[n], s) for n in names for s in seeds]
    with ProcessPoolExecutor(max_workers=7) as ex:
        for (name, s, bank, npass, nact, plants, animals, err) in ex.map(_job, jobs):
            if err and bank < 0:
                print(f"{name:12s} seed={s} FAIL {err}")
                continue
            print(f"{name:12s} seed={s} bank={bank:<8.0f} PASS={npass}/{nact} "
                  f"wh={plants.get('WHEAT',0)} ca={plants.get('CARROT',0)} st={plants.get('STRAWBERRY',0)} "
                  f"to={plants.get('TOMATO',0)} me={plants.get('MELON',0)} "
                  f"cow={animals.get('COW',0)} sh={animals.get('SHEEP',0)} go={animals.get('GOOSE',0)}")


if __name__ == "__main__":
    main()
