"""Identify which known agent each pipe16-loss opponent runs.

For a recorded episode we know the seed and both seats' action streams.
Re-run the game locally: pipe16 in our seat, candidate in the opponent's
seat, same seed. A deterministic candidate that IS the opponent reproduces
the recorded stream ~exactly. Report the best match per loss episode.
"""
import gzip, json, glob, os, sys
sys.path.insert(0, ".")
import inco, kagsim

PASS = {"farmer": ["PASS"], "hands": [], "market": []}


def norm(a):
    if isinstance(a, dict):
        return tuple((k, norm(v)) for k, v in sorted(a.items()))
    if isinstance(a, (list, tuple)):
        return tuple(norm(x) for x in a)
    if isinstance(a, float) and a == int(a):
        return int(a)
    return a


def opp_stream(agent, seed, opp_seat):
    """Run agent vs pipe16 on seed; return (opp_stream, our_stream)."""
    p16 = _P16
    g = kagsim.Game(seed=int(seed))
    ours, theirs = [], []
    for _ in range(720):
        try:
            a0 = p16(g.observe(0)) if opp_seat == 1 else agent(g.observe(0))
        except Exception:
            a0 = dict(PASS)
        try:
            a1 = agent(g.observe(1)) if opp_seat == 1 else p16(g.observe(1))
        except Exception:
            a1 = dict(PASS)
        ours.append(a0 if opp_seat == 1 else a1)
        theirs.append(a1 if opp_seat == 1 else a0)
        g.step(a0, a1)
    return theirs, ours


def load_ep(path):
    d = json.load(gzip.open(path, "rt"))
    t = d["teams"]
    me = t.index("Sam-wiz")
    return d, me, 1 - me


def match_frac(rec_theirs, rec_ours, cand, seed, opp_seat, n=None):
    st, so = opp_stream(cand, seed, opp_seat)
    n = n or len(rec_theirs)
    mt = sum(1 for i in range(n) if norm(rec_theirs[i]) == norm(st[i])) / n
    mo = sum(1 for i in range(n) if norm(rec_ours[i]) == norm(so[i])) / n
    return mt, mo


def main():
    global _P16
    _P16 = inco.load_agent("subK_pipe16.py")

    cands = {}
    for p in sorted(glob.glob("data/donors/agents/*.py")):
        cands["donor/" + os.path.basename(p)[:-3]] = p
    for p in sorted(glob.glob("rivals/*/_entry.py")) + \
             sorted(glob.glob("rivals5/*/_entry.py")) + \
             sorted(glob.glob("rivals6/*/_entry.py")):
        cands[os.path.basename(os.path.dirname(p))] = p
    # named extras
    for name, p in [("pipe16", "subK_pipe16.py"), ("pipe16clamp", "subM_pipe16clamp.py"),
                    ("metav4", "subL_metav4.py")]:
        if os.path.exists(p):
            cands[name] = p
    print(f"{len(cands)} candidate agents", flush=True)

    agents = {}
    def get(name):
        if name not in agents:
            try:
                agents[name] = inco.load_agent(cands[name])
            except Exception:
                agents[name] = None
        return agents[name]

    eps = sorted(sys.argv[1:], key=int)
    for ep in eps:
        path = f"mine/opp/{ep}.json.gz"
        if not os.path.exists(path):
            path = f"mine/loss/{ep}.json.gz"
        d, me, opp = load_ep(path)
        rec_theirs = [a[opp] for a in d["actions"]]
        rec_ours = [a[me] for a in d["actions"]]
        seed = d["seed"]
        best = []
        for name in cands:
            a = get(name)
            if a is None:
                continue
            try:
                mt, mo = match_frac(rec_theirs, rec_ours, a, seed, opp, n=240)
            except Exception:
                continue
            if mt > 0.55:
                best.append((mt, mo, name))
        best.sort(reverse=True)
        m = d["rewards"][me] - d["rewards"][opp]
        print(f"\nep{ep} vs {d['teams'][opp]} margin {m:+.0f} seed {seed} seat{me}")
        for mt, mo, name in best[:5]:
            print(f"   {mt:6.1%} opp-match (ours {mo:5.1%})  {name}")
        if not best:
            print("   no candidate >55% — private/unknown agent")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
