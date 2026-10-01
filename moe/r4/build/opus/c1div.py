"""First full-action divergence of C1's band opponents vs WL-family / lineage candidates (exact.py work(), kagsim).
WLV signature (fable_r2 E1, wlv_pull): diverges from public WL (yummers) and wonderful/peak2950 at step 53."""
import json, gzip, sys
sys.argv = [sys.argv[0]]
exec(open('/tmp/opus_r3/exact.py').read().split('if __name__')[0])
C = {"WL": "rivals4/kaggriculture-yummers/_entry.py", "wonderful": "rivals8/hanifnoerrofiq_a-wonderful-life/_entry.py",
     "peak2950": "rivals8/haideptry_the-2950-peak-farm/_entry.py",
     "leo4turn": "rivals8/leoprovorov_four-turn-forecast-notebook-version-2/_entry.py",
     "shep": "subW_shepherd.py", "hyb": "subX_hyb2965.py"}
if __name__ == "__main__":
    opps = json.load(open("moe/r4/build/opus/c1opp.json"))
    jobs = []
    for o in opps:
        d = json.load(gzip.open(o["path"], "rt"))
        for c, p in C.items(): jobs.append((o["ep"], c, p, d["seed"], 1 - o["seat"], d["actions"]))
    res = {}
    with ProcessPoolExecutor(max_workers=2) as ex:
        for ep, name, t, rw in ex.map(work, jobs, chunksize=1): res.setdefault(ep, {})[name] = t
    for o in opps:
        print(f"{o['opp'][:12]:12} m={o['m']:+6.0f} " + " ".join(f"{c}@{res[o['ep']].get(c)}" for c in C), flush=True)
    json.dump({str(k): v for k, v in res.items()}, open("moe/r4/build/opus/c1div.json", "w"))
