"""Per-step net market injection profile of top-family seats (the opponent model for TS rollouts).
Replays recorded top-vs-top games exactly on the official Python engine (both seats' tapes, recorded seed) and, via
the one-step shadow re-simulation, recovers each seat's own net market effect per step.
usage: oppprof.py OUT.json NGAMES   -> {"n": games*2 seats, "mean": [ {item: mean delta} x 720 ], "check": [...]}
"""
import glob, gzip, json, os, sys, copy
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r5/build/opusb")
import harness as H
import ts

TEAMS = set(ts.LIB_TEAMS)


def game_deltas(d):
    acts = d["actions"]
    tapes = [lambda o, k=k: (acts[o["step"] + 1][k] if o["step"] + 1 < len(acts) and isinstance(acts[o["step"] + 1][k], dict) else ts.PASS) for k in (0, 1)]
    prev = [None, None]; pact = [None, None]; out = [dict(), dict()]   # out[k][step] = seat k's own net effect

    def wrap(k):
        def f(o):
            if prev[k] is not None and prev[k]["step"] + 1 == o["step"]:
                # shadow from seat k's view recovers the OTHER seat's effect
                out[1 - k][prev[k]["step"]] = ts.shadow_delta(prev[k], pact[k], o)
            a = tapes[k](o)
            prev[k] = copy.deepcopy(o); pact[k] = a
            return a
        return f
    r = H.run_episode(wrap(0), wrap(1), seed=d["seed"], copy_obs=True)
    return out, r["reward"]


if __name__ == "__main__":
    outp, n = sys.argv[1], int(sys.argv[2])
    files = sorted(glob.glob(ROOT + "/mine/top10/*.json.gz"))
    acc = [dict() for _ in range(720)]; cnt = 0; checks = []
    for f in files:
        if cnt >= 2 * n:
            break
        d = json.load(gzip.open(f, "rt"))
        if not (d["teams"][0] in TEAMS and d["teams"][1] in TEAMS):
            continue
        out, rew = game_deltas(d)
        checks.append(dict(ep=d["episode_id"], rec=d["rewards"], sim=rew, ok=[float(a) == float(b) for a, b in zip(d["rewards"], rew)]))
        for k in (0, 1):
            for s, dd in out[k].items():
                for it, v in dd.items():
                    acc[s][it] = acc[s].get(it, 0) + v
            cnt += 1
        print(checks[-1], flush=True)
    mean = [{it: v / cnt for it, v in a.items()} for a in acc]
    json.dump(dict(n=cnt, mean=mean, check=checks), open(outp, "w"))
    tot = {}
    for a in mean:
        for it, v in a.items():
            tot[it] = tot.get(it, 0) + v
    print("seats", cnt, "exact", sum(all(c["ok"]) for c in checks), "/", len(checks), "season net per seat", {k: round(v) for k, v in tot.items()})
