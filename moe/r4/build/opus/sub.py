"""TOP-SUB: substitute a candidate into one seat of a recorded top-dump game; the other seat replays its
recorded (contemporaneous, top-rated) tape open-loop. kagsim, recorded seed.

Per cell (ep, seat=candidate's seat): candidate bank, opponent replayed bank, recorded banks of both seats
(the replaced seat's recorded bank = what a top team made in exactly this spot), shops aligned?
usage: sub.py OUT.jsonl NAME=PATH[,NAME=PATH] WORKERS LIMIT_GAMES [GLOB] [OFFSET]
"""
import glob, gzip, json, os, sys, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from run import load, act, PASS
import kagsim


def job(arg):
    name, path, p, seat = arg
    d = json.load(gzip.open(p, "rt")); acts = d["actions"]; t0 = time.time()
    if not d.get("shops"):  # live files: recover the recorded shop sequence by exact replay
        g0 = kagsim.Game(seed=int(d["seed"]))
        for t in range(719):
            g0.step(*[acts[t + 1][i] if isinstance(acts[t + 1][i], dict) else PASS for i in (0, 1)])
        d["shops"] = list(g0.observe(0)["town"]["unlocked_shops"])
        d["rec_ok"] = [abs(g0.reward(i) - d["rewards"][i]) < .5 for i in (0, 1)]
    try:
        fn, m = load(path, "sub")
        PIN = os.environ.get("PIN", "1") == "1"
        g = kagsim.Game(seed=int(d["seed"]), shops=(list(d["shops"]) if PIN else None)); nerr = 0
        for t in range(719):
            o = g.observe(seat)
            a = act(fn, o)
            b = acts[t + 1][1 - seat] if isinstance(acts[t + 1][1 - seat], dict) else PASS
            g.step(*((a, b) if seat == 0 else (b, a)))
        o = g.observe(0)
        shops = list(o["town"]["unlocked_shops"])
        r = [float(g.reward(0)), float(g.reward(1))]
    except Exception as e:
        return dict(name=name, ep=d["episode_id"], seat=seat, err=repr(e)[:120])
    return dict(name=name, ep=d["episode_id"], seat=seat, date=d.get("date"), me=r[seat], opp=r[1 - seat],
                rec_me=d["rewards"][seat], rec_opp=d["rewards"][1 - seat], replaced=d["teams"][seat],
                opp_team=d["teams"][1 - seat], rec_ok=d.get("rec_ok"), shops_ok=shops == list(d.get("shops") or []),
                s=round(time.time() - t0, 1))


if __name__ == "__main__":
    out = sys.argv[1]; arms = [a.split("=", 1) for a in sys.argv[2].split(",")]
    W, LIM = int(sys.argv[3]), int(sys.argv[4]); g = sys.argv[5] if len(sys.argv) > 5 else "mine/top10/*.json.gz"
    OFF = int(sys.argv[6]) if len(sys.argv) > 6 else 0
    paths = sorted(glob.glob(g))[OFF:OFF + LIM]
    LB = json.load(open("moe/r3/lb_0926_0500.json"))
    done = set()
    if os.path.exists(out):
        for line in open(out):
            try: r = json.loads(line); done.add((r["name"], r["ep"], r["seat"]))
            except Exception: pass
    jobs = []
    for p in paths:
        ep = int(os.path.basename(p).split(".")[0])
        seats = (0, 1)
        if os.environ.get("ONLY_TEAM"):
            dd = json.load(gzip.open(p, "rt")); seats = [i for i in (0, 1) if dd["teams"][i] == os.environ["ONLY_TEAM"]]
            if os.environ.get("RMIN") and (LB.get(dd["teams"][1 - seats[0]]) or 0) < float(os.environ["RMIN"]): seats = []
        for s in seats:
            for n, a in arms:
                if (n, ep, s) not in done: jobs.append((n, a, p, s))
    print(len(jobs), "jobs", flush=True)
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=W) as ex, open(out, "a") as f:
        for i, r in enumerate(ex.map(job, jobs, chunksize=1), 1):
            f.write(json.dumps(r, ensure_ascii=False) + "\n"); f.flush()
            if i % 20 == 0: print(i, flush=True)
