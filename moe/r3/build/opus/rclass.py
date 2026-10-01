"""Classify every differing market step of a candidate on WLV's exact farm (hybrid mode). usage: rclass.py name=path"""
import sys, json, gzip, collections
CARGS = list(sys.argv); sys.argv = [sys.argv[0]]
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/rdiv.py").read().split('\nif __name__ == "__main__":')[0])
PREM = ("MILK", "WOOL", "STRAWBERRY", "EGG", "MELON")
def cls(c, r):
    cn = [tuple(o) for o in c if o]; rn = [tuple(o) for o in r if o]
    if cn == rn: return "empty-slot"
    if sorted(cn) == sorted(rn): return "order"
    ck = sorted(o[:2] for o in cn); rk = sorted(o[:2] for o in rn)
    if ck == rk: return "qty"
    cs = {o[1] for o in cn if o[0] == "SELL" and len(o) > 1 and o[1] in PREM}; rs = {o[1] for o in rn if o[0] == "SELL" and len(o) > 1 and o[1] in PREM}
    if cs != rs: return "premium-sell"
    return "other"
def work2(job):
    name, path, ep, seed, opp = job
    acts = json.load(gzip.open(f"mine/opp/{ep}.json.gz", "rt"))["actions"]
    ag, m = load(path, "c"); g = kagsim.Game(seed=int(seed)); me = 1 - opp; cnt = collections.Counter()
    for t in range(719):
        ours = acts[t + 1][me] if isinstance(acts[t + 1][me], dict) else PASS
        rec = acts[t + 1][opp] if isinstance(acts[t + 1][opp], dict) else PASS
        a = act(ag, g.observe(opp))
        a = {"farmer": rec.get("farmer", ["PASS"]), "hands": rec.get("hands", []), "market": a.get("market") or []}
        if mkt(a) != mkt(rec): cnt[phase(t) + "|" + cls(a["market"], rec.get("market") or [])] += 1
        g.step(*((ours, a) if opp == 1 else (a, ours)))
    return dict(ep=ep, cnt=dict(cnt))
if __name__ == "__main__":
    n, p = CARGS[1].split("=", 1); jobs = []
    for r in tapes():
        d = json.load(gzip.open(f"mine/opp/{r['ep']}.json.gz", "rt")); jobs.append((n, p, int(r["ep"]), d["seed"], 1 - r["seat"]))
    out = f"moe/r3/build/opus/rclass_{n}.jsonl"; open(out, "w").close(); pool(work2, jobs, out)
    tot = collections.Counter()
    for l in open(out): tot.update(json.loads(l)["cnt"])
    for ph in ("d0-5", "d6-12", "d13-24", "d25-29"):
        row = {k.split("|")[1]: v for k, v in tot.items() if k.startswith(ph + "|")}
        print(f"{n} {ph:7s} total {sum(row.values()):5d} per-game {sum(row.values())/18:5.1f}  " + "  ".join(f"{k}={v}" for k, v in sorted(row.items(), key=lambda x: -x[1])))
