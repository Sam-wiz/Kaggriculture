"""Parallel fingerprinting: which known agent runs each pipe16-loss opponent?

Per episode: pipe16 replays in our recorded seat, candidate in opponent's
seat, same seed. Deterministic candidates that ARE the opponent reproduce
the recorded stream ~exactly. Multiprocess over candidates.
"""
import gzip, json, glob, os, sys
sys.path.insert(0, ".")
import inco, kagsim
from concurrent.futures import ProcessPoolExecutor

PASS = {"farmer": ["PASS"], "hands": [], "market": []}
P16_PATH = "subAB_m30b.py"


def norm(a):
    if isinstance(a, dict):
        return tuple((k, norm(v)) for k, v in sorted(a.items()))
    if isinstance(a, (list, tuple)):
        return tuple(norm(x) for x in a)
    if isinstance(a, float) and a == int(a):
        return int(a)
    return a


def work(job):
    """Run one candidate vs pipe16 on seed, return match fracs."""
    name, path, seed, opp_seat, rec_theirs, rec_ours, n = job
    try:
        cand = inco.load_agent(path)
        p16 = inco.load_agent(P16_PATH)
    except Exception:
        return name, 0.0, 0.0
    g = kagsim.Game(seed=int(seed))
    mt = mo = 0
    for i in range(n):
        try:
            a0 = p16(g.observe(0)) if opp_seat == 1 else cand(g.observe(0))
        except Exception:
            a0 = dict(PASS)
        try:
            a1 = cand(g.observe(1)) if opp_seat == 1 else p16(g.observe(1))
        except Exception:
            a1 = dict(PASS)
        # recorded actions are offset by one step: rec[i+1] is the reply to obs[i]
        rt, ro = rec_theirs[i + 1], rec_ours[i + 1]
        at, ao = (a1, a0) if opp_seat == 1 else (a0, a1)
        if norm(rt) == norm(at):
            mt += 1
        if norm(ro) == norm(ao):
            mo += 1
        g.step(a0, a1)
    return name, mt / n, mo / n


def main():
    cands = {}
    for p in sorted(glob.glob("data/donors/agents/*.py")):
        cands["donor/" + os.path.basename(p)[:-3]] = p
    for p in sorted(glob.glob("rivals/*/_entry.py")) + \
             sorted(glob.glob("rivals5/*/_entry.py")) + \
             sorted(glob.glob("rivals6/*/_entry.py")):
        cands[os.path.basename(os.path.dirname(p))] = p
    for name, p in [("pipe16", "subK_pipe16.py"),
                    ("pipe16clamp", "subM_pipe16clamp.py"),
                    ("metav4", "subL_metav4.py")]:
        if os.path.exists(p):
            cands[name] = p
    print(f"{len(cands)} candidates", flush=True)

    for ep in sys.argv[1:]:
        for pat in (f"mine/opp/{ep}.json.gz", f"mine/loss/{ep}.json.gz"):
            if os.path.exists(pat):
                break
        d = json.load(gzip.open(pat, "rt"))
        t = d["teams"]
        me, opp = t.index("Sam-wiz"), 1 - t.index("Sam-wiz")
        rec_theirs = [a[opp] for a in d["actions"]]
        rec_ours = [a[me] for a in d["actions"]]
        seed = d["seed"]
        jobs = [(n_, p, seed, opp, rec_theirs, rec_ours, 72)
                for n_, p in cands.items()]
        best = []
        with ProcessPoolExecutor(max_workers=8) as ex:
            for name, mt, mo in ex.map(work, jobs, chunksize=4):
                if mt > 0.55:
                    best.append((mt, mo, name))
        best.sort(reverse=True)
        m = d["rewards"][me] - d["rewards"][opp]
        print(f"\nep{ep} vs {t[opp]} margin {m:+.0f} seed {seed} our-seat{me}")
        for mt, mo, name in best[:6]:
            print(f"   {mt:6.1%} opp-match (ours {mo:5.1%})  {name}")
        if not best:
            print("   no candidate >55% — private/unknown agent")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
