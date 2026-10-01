"""Fingerprint metav4's 13 live losses: which known agent runs each opponent?

Same machinery as fingerprint_loss2.py but metav4 is our seat's agent.
Replays each episode's seed locally, candidate in opponent's seat, compares
recorded action streams (offset +1).
"""
import gzip, json, glob, os, sys
sys.path.insert(0, ".")
import inco, kagsim
from concurrent.futures import ProcessPoolExecutor

PASS = {"farmer": ["PASS"], "hands": [], "market": []}
OURS = "subL_metav4.py"

# (ep, opponent_name) — all 13 corrected losses
LOSS_EPS = {
    111287656: "Satuker", 111235089: "cununn", 111273086: "Dmitry Bardonov",
    111351018: "RS Turley", 111345304: "csly666", 111292110: "Munal Singh",
    111317876: "lumen", 111277533: "Aurora wy", 111226181: "Sam-wiz(p16)",
    111285496: "Dzmitry Pihulski", 111288189: "eliasruntime",
    111359390: "Duck Typing", 111275323: "c_fxy",
}


def norm(a):
    if isinstance(a, dict):
        return tuple((k, norm(v)) for k, v in sorted(a.items()))
    if isinstance(a, (list, tuple)):
        return tuple(norm(x) for x in a)
    if isinstance(a, float) and a == int(a):
        return int(a)
    return a


def load_ep(ep):
    for d in ("mine/loss", "mine/opp"):
        p = f"{d}/{ep}.json.gz"
        if os.path.exists(p):
            with gzip.open(p) as f:
                return json.load(f)
    return None


def work(job):
    name, path, seed, opp_seat, rec_theirs, rec_ours, n = job
    try:
        cand = inco.load_agent(path)
        ours = inco.load_agent(OURS)
    except Exception:
        return name, 0.0, 0.0
    g = kagsim.Game(seed=int(seed))
    mt = mo = 0
    for i in range(n):
        try:
            a0 = ours(g.observe(0)) if opp_seat == 1 else cand(g.observe(0))
        except Exception:
            a0 = dict(PASS)
        try:
            a1 = cand(g.observe(1)) if opp_seat == 1 else ours(g.observe(1))
        except Exception:
            a1 = dict(PASS)
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
             sorted(glob.glob("rivals6/*/_entry.py")) + \
             sorted(glob.glob("donors/*/_entry.py")):
        cands[os.path.basename(os.path.dirname(p))] = p
    print(f"{len(cands)} candidates", flush=True)

    for ep, opp in LOSS_EPS.items():
        d = load_ep(ep)
        if d is None:
            print(f"ep{ep} {opp}: NO REPLAY", flush=True)
            continue
        acts = d["actions"]
        seed = d.get("seed")
        teams = d.get("teams") or []
        our_seat = 0 if teams[0] == "Sam-wiz" else 1
        opp_seat = 1 - our_seat
        n = min(72, len(acts) - 1)
        rec_theirs = [a[opp_seat] for a in acts]
        rec_ours = [a[our_seat] for a in acts]
        jobs = [(name, path, seed, opp_seat, rec_theirs, rec_ours, n)
                for name, path in cands.items()]
        res = []
        with ProcessPoolExecutor(max_workers=8) as ex:
            for name, mt, mo in ex.map(work, jobs):
                if mt > 0.3:
                    res.append((mt, mo, name))
        res.sort(reverse=True)
        print(f"ep{ep} {opp} seed={seed} opp_seat={opp_seat}: "
              + ", ".join(f"{nm} {mt:.2f}/{mo:.2f}" for mt, mo, nm in res[:6])
              + (" (no match)" if not res else ""), flush=True)


if __name__ == "__main__":
    main()
