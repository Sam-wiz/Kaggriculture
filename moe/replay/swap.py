"""Swap/bias probe: pipe16's own 09-20 live episodes (pipe16 = home, reproduces exactly); run other
arms in our seat against the recorded opponent tape. usage: swap.py OUT.jsonl LIMIT ARM=file ..."""
import gzip, json, os, sys, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT)
import harness

out, limit = os.path.abspath(os.path.join("/tmp/opus_r2", sys.argv[1])), int(sys.argv[2])
arms = [a.split("=", 1) for a in sys.argv[3:]]
lb = json.load(open("data/lb.json"))
eps = [json.loads(l) for l in open("data/ep_pipe16.jsonl")]
eps = list({e["ep"]: e for e in eps if os.path.exists("mine/opp/%d.json.gz" % e["ep"])}.values())
eps.sort(key=lambda e: e["ep"])
PASS = {"farmer": ["PASS"], "hands": [], "market": []}


def tape(acts, seat):
    def ag(obs):
        t = obs["step"] + 1
        a = acts[t][seat] if t < len(acts) else None
        return a if isinstance(a, dict) else PASS
    return ag


n = 0
with open(out, "a") as f:
    for e in eps:
        d = json.load(gzip.open("mine/opp/%d.json.gz" % e["ep"], "rt"))
        if "Sam-wiz" not in d["teams"]:
            continue
        us = d["teams"].index("Sam-wiz"); them = 1 - us
        if d["teams"][them] == "Sam-wiz" or (lb.get(d["teams"][them]) or 0) < float(os.environ.get("RMIN", "0")):
            continue
        rew = d["rewards"]
        rec = dict(ep=e["ep"], seat=us, opp=d["teams"][them], R=lb.get(d["teams"][them]),
                   recorded=rew[us] - rew[them])
        for name, path in arms:
            me = harness.load_agent(path, name="swap_%s_%d" % (name, e["ep"]))
            pair = (me, tape(d["actions"], them)) if us == 0 else (tape(d["actions"], them), me)
            r = harness.run_episode(pair[0], pair[1], seed=d["seed"], copy_obs=True)
            rec[name] = r["reward"][us] - r["reward"][them]
            rec[name + "_opp"] = r["reward"][them] - rew[them]
        f.write(json.dumps(rec) + "\n"); f.flush(); print(rec, flush=True)
        n += 1
        if n >= limit:
            break
