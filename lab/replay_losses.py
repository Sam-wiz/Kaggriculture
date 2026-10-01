"""Replay our real ladder games from the recorded tapes and track the bank margin over time.

Both players' full action lists and the seed are in the replay, so feeding both tapes back into
the engine reproduces the episode exactly. That gives us the per-turn bank curve the replay
viewer shows, for every game at once.
"""
import gzip, glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

PASS = {"farmer": ["PASS"], "hands": [], "market": []}


def tape(actions, idx):
    n = len(actions)
    def agent(obs):
        s = obs.get("step")
        if s is None:
            s = int(obs.get("day", 0)) * 24 + int(obs.get("hour", 0))
        if s < 0 or s >= n:
            return dict(PASS)
        a = actions[s][idx]
        if not isinstance(a, dict):
            return dict(PASS)
        hands = a.get("hands") or []
        have = len(obs["farms"][obs["player"]].get("hands", []))
        hands = list(hands[:have]) + [["PASS"]] * max(0, have - len(hands))
        return {"farmer": a.get("farmer", ["PASS"]), "hands": hands,
                "market": (a.get("market") or [])[:10]}
    return agent


def curve(path):
    d = json.load(gzip.open(path, "rt"))
    t = d["teams"]
    if "Sam-wiz" not in t:
        return None
    me = t.index("Sam-wiz")
    acts = d["actions"]
    banks = []
    def on_step(step, state, env):
        f = state[0].observation.farms
        banks.append((f[me]["money"], f[1 - me]["money"]))
    r = harness.run_episode(tape(acts, 0), tape(acts, 1), seed=d["seed"],
                            copy_obs=False, on_step=on_step, catch_errors=True)
    got = r["reward"]
    return dict(ep=d["episode_id"], opp=t[1 - me], seat=me, seed=d["seed"],
                actual=d["rewards"][me], actual_opp=d["rewards"][1 - me],
                repro=got[me], repro_opp=got[1 - me], banks=banks)


if __name__ == "__main__":
    fs = sorted(glob.glob("mine/opp/*.json.gz"))[:int(sys.argv[1]) if len(sys.argv) > 1 else 3]
    for f in fs:
        c = curve(f)
        if not c:
            continue
        ok = abs(c["repro"] - c["actual"]) < 1 and abs(c["repro_opp"] - c["actual_opp"]) < 1
        print(f"{c['ep']}  {c['opp'][:20]:<20} actual {c['actual']:>9,.0f}/{c['actual_opp']:>9,.0f}"
              f"   repro {c['repro']:>9,.0f}/{c['repro_opp']:>9,.0f}   {'EXACT' if ok else 'MISMATCH'}"
              f"  steps={len(c['banks'])}")
