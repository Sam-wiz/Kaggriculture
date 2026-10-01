"""Replay-substitution: re-run cached live episodes with OUR seat played by agent file X and the
opponent's seat replaying its recorded actions (open-loop). Scratch pilot for moe/strat/opus_r2.md.
usage: python subst.py OUT.jsonl BUILDS(comma) LIMIT ARM=file.py [ARM=file.py ...]
"""
import gzip, json, os, sys, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
sys.argv[1] = os.path.abspath(sys.argv[1])
os.chdir(ROOT); sys.path.insert(0, ROOT)
import harness

out, builds, limit = os.path.abspath(sys.argv[1]), set(sys.argv[2].split(",")), int(sys.argv[3])
RMIN = float(os.environ.get("RMIN", "0"))
arms = [a.split("=", 1) for a in sys.argv[4:]]
idx = json.load(open("moe/opus/eps_index.json"))
rows = [r for r in idx if r["build"] in builds and r["ours"] is not None and (r["R"] or 0) >= RMIN]
rows.sort(key=lambda r: r["ep"])
OFF = int(os.environ.get("OFFSET", "0"))
rows = rows[OFF:OFF + limit] if limit else rows[OFF:]
PASS = {"farmer": ["PASS"], "hands": [], "market": []}


def load(row):
    if row["kind"] == "full":
        d = json.load(open(row["path"]))
        load.shops = d["steps"][-1][0]["observation"]["town"]["unlocked_shops"]
        return [[s[0].get("action"), s[1].get("action")] for s in d["steps"]], d["info"]["seed"], d["rewards"]
    d = json.load(gzip.open(row["path"], "rt"))
    load.shops = d.get("shops")
    return d["actions"], d["seed"], d["rewards"]


def tape(acts, seat):
    def ag(obs):
        t = obs["step"] + 1
        a = acts[t][seat] if t < len(acts) else None
        return a if isinstance(a, dict) else PASS
    return ag


with open(out, "a") as f:
    for row in rows:
        acts, seed, rew = load(row)
        us, them = row["seat"], 1 - row["seat"]
        rec = dict(ep=row["ep"], build=row["build"], seat=us, opp=row["opp"], R=row["R"],
                   recorded=rew[us] - rew[them])
        for name, path in arms:
            t0 = time.time()
            me = harness.load_agent(path, name="arm_%s_%d" % (name, row["ep"]))
            pair = (me, tape(acts, them)) if us == 0 else (tape(acts, them), me)
            r = harness.run_episode(pair[0], pair[1], seed=seed, copy_obs=True)
            rw = r["reward"]
            rec[name] = rw[us] - rw[them]
            rec[name + "_opp"] = rw[them] - rew[them]      # opponent bank drift vs recording
            rec[name + "_shopok"] = list(r["state"][0].observation.town["unlocked_shops"]) == list(load.shops or [])
            rec[name + "_s"] = round(time.time() - t0, 1)
        f.write(json.dumps(rec) + "\n"); f.flush()
        print({k: v for k, v in rec.items() if not k.endswith("_shops")}, flush=True)
