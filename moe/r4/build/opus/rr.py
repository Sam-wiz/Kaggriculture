"""Closed-loop round-robin (kagsim, raw seeds, both seats) + Bradley-Terry fit.
usage: rr.py OUT.jsonl SEED0 NSEEDS WORKERS NAME=PATH [NAME=PATH ...]     (resumes)
       rr.py --fit OUT.jsonl
"""
import itertools, json, math, os, sys
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r3/build/opus")


def job(arg):
    from run import load, act
    import kagsim
    (na, pa), (nb, pb), seed, sw = arg
    try:
        a, _ = load(pa, "ra"); b, _ = load(pb, "rb")
        g = kagsim.Game(seed=int(seed))
        for t in range(719):
            o0, o1 = g.observe(0), g.observe(1)
            if sw == 0: g.step(act(a, o0), act(b, o1))
            else: g.step(act(b, o0), act(a, o1))
        r = [float(g.reward(0)), float(g.reward(1))]
        ra, rb = (r[0], r[1]) if sw == 0 else (r[1], r[0])
        return dict(a=na, b=nb, seed=seed, sw=sw, ra=ra, rb=rb)
    except Exception as e:
        return dict(a=na, b=nb, seed=seed, sw=sw, err=repr(e)[:120])


def fit(path):
    rows = [json.loads(l) for l in open(path)]
    rows = [r for r in rows if "err" not in r]
    names = sorted({r["a"] for r in rows} | {r["b"] for r in rows})
    W = {(x, y): 0.0 for x in names for y in names}
    for r in rows:
        if r["ra"] > r["rb"]: W[(r["a"], r["b"])] += 1
        elif r["ra"] < r["rb"]: W[(r["b"], r["a"])] += 1
        else: W[(r["a"], r["b"])] += .5; W[(r["b"], r["a"])] += .5
    s = {n: 0.0 for n in names}
    for _ in range(2000):  # MM iterations for BT strengths (log scale), small prior
        new = {}
        for i in names:
            num = sum(W[(i, j)] for j in names if j != i) + 0.5
            den = sum((W[(i, j)] + W[(j, i)] + 1) / (math.exp(s[i]) + math.exp(s[j])) for j in names if j != i)
            new[i] = math.log(num / den)
        m = sum(new.values()) / len(new); s = {k: v - m for k, v in new.items()}
    elo = {k: 400 * v / math.log(10) for k, v in s.items()}
    for n in sorted(names, key=lambda k: -elo[k]):
        wr = {m: W[(n, m)] / max(1, W[(n, m)] + W[(m, n)]) for m in names if m != n}
        print(f"{n:8} elo {elo[n]:+6.0f}  " + " ".join(f"{m}:{v:.2f}" for m, v in wr.items()))
    return elo


if __name__ == "__main__":
    if sys.argv[1] == "--fit":
        fit(sys.argv[2]); sys.exit()
    out, s0, ns, Wk = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    arms = [a.split("=", 1) for a in sys.argv[5:]]
    done = set()
    if os.path.exists(out):
        for l in open(out):
            try: r = json.loads(l); done.add((r["a"], r["b"], r["seed"], r["sw"]))
            except Exception: pass
    jobs = [(x, y, s, sw) for x, y in itertools.combinations(arms, 2) for s in range(s0, s0 + ns) for sw in (0, 1)
            if (x[0], y[0], s, sw) not in done]
    print(len(jobs), "games", flush=True)
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=Wk) as ex, open(out, "a") as f:
        for i, r in enumerate(ex.map(job, jobs, chunksize=1), 1):
            f.write(json.dumps(r) + "\n"); f.flush()
            if i % 50 == 0: print(i, flush=True)
