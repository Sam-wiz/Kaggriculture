"""Arm R bisection instrument. For each candidate (name=path) and each of the 18 WLV tapes:
  hybrid mode: candidate MARKET computed closed-loop from its own observation, UNIT ops forced to WLV's recorded
               unit ops (farm state = WLV's) -> market-channel first divergence + differing steps by phase + samples.
  full mode:   candidate drives its whole seat vs our recorded tape -> first unit / market / any divergence.
usage: rdiv.py OUTTAG [--full] name=path ..."""
import sys, json, gzip
ARGS = list(sys.argv); sys.argv = [sys.argv[0]]
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/run.py").read().split("if __name__")[0])
def norm(a):
    if isinstance(a, dict): return tuple((k, norm(v)) for k, v in sorted(a.items()))
    if isinstance(a, (list, tuple)): return tuple(norm(x) for x in a)
    if isinstance(a, float) and a == int(a): return int(a)
    return a
def units(a): return norm((a.get("farmer"), a.get("hands")))
def mkt(a): return norm(a.get("market") or [])
def phase(t):
    d = t // 24
    return "d0-5" if d <= 5 else "d6-12" if d <= 12 else "d13-24" if d <= 24 else "d25-29"
def tapes():
    rows = json.load(open("moe/r3/fable_scratch/live_rows2.json"))
    sel = [r for r in rows if tuple(r["open_they"]) == (5, 0) and (r["R"] or 0) >= 2000 and r["same_u"] >= 0.85 and "Acidic" not in r["opp"]]
    return sel
def work(job):
    name, path, ep, seed, opp, mode = job
    acts = json.load(gzip.open(f"mine/opp/{ep}.json.gz", "rt"))["actions"]
    ag, m = load(path, "r"); g = kagsim.Game(seed=int(seed)); me = 1 - opp
    per = {"d0-5": 0, "d6-12": 0, "d13-24": 0, "d25-29": 0}; samples = []; first = {"unit": None, "mkt": None}
    nm = 0
    for t in range(719):
        ours = acts[t + 1][me] if isinstance(acts[t + 1][me], dict) else PASS
        rec = acts[t + 1][opp] if isinstance(acts[t + 1][opp], dict) else PASS
        a = act(ag, g.observe(opp))
        if mode == "hyb":
            a = {"farmer": rec.get("farmer", ["PASS"]), "hands": rec.get("hands", []), "market": a.get("market") or []}
        if units(a) != units(rec) and first["unit"] is None: first["unit"] = t
        if mkt(a) != mkt(rec):
            if first["mkt"] is None: first["mkt"] = t
            per[phase(t)] += 1
            if len(samples) < 12: samples.append((t, a.get("market") or [], rec.get("market") or []))
        else: nm += 1
        if mode == "full" and first["unit"] is not None and first["mkt"] is not None: break
        g.step(*((ours, a) if opp == 1 else (a, ours)))
    return dict(name=name, ep=ep, mode=mode, first=first, per=per, match=nm, samples=samples, tele=tele(m))
if __name__ == "__main__":
    tag = ARGS[1]; full = "--full" in ARGS
    cands = [a.split("=", 1) for a in ARGS[2:] if "=" in a]
    jobs = []
    for n, p in cands:
        for r in tapes():
            d = json.load(gzip.open(f"mine/opp/{r['ep']}.json.gz", "rt"))
            jobs.append((n, p, int(r["ep"]), d["seed"], 1 - r["seat"], "hyb"))
            if full: jobs.append((n, p, int(r["ep"]), d["seed"], 1 - r["seat"], "full"))
    out = f"moe/r3/build/opus/rdiv_{tag}.jsonl"; open(out, "w").close()
    pool(work, jobs, out)
    res = [json.loads(l) for l in open(out)]
    for n, _ in cands:
        for mode in ("hyb", "full"):
            R = [r for r in res if r["name"] == n and r["mode"] == mode]
            if not R: continue
            fm = sorted((r["first"]["mkt"] if r["first"]["mkt"] is not None else 719) for r in R)
            fu = sorted((r["first"]["unit"] if r["first"]["unit"] is not None else 719) for r in R)
            print(f"{n:14s} {mode:4s} n={len(R)} mkt_first med={fm[len(fm)//2]} >=600:{sum(x>=600 for x in fm)} list={fm} | unit_first med={fu[len(fu)//2]} | match_mean={sum(r['match'] for r in R)/len(R):.0f}/719 | per={ {k: sum(r['per'][k] for r in R) for k in R[0]['per']} }")
