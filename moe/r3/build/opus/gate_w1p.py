"""Gate for shepR (shepherd + 324 R2 streams): closed-loop on seedindex [1380:1404] x both seats vs shepherd and hyb2965
(Fable gate-(d) slice), plus non-band mis-pick check vs 2802 / koshinm on [1380:1392] for shepR and vanilla shepherd."""
import sys, json
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/run.py").read().split('\nif __name__ == "__main__":')[0])
if __name__ == "__main__":
    idx = [r["seed"] for r in json.load(open(ROOT + "/data/seedindex_900000_1400.json"))]
    G = idx[1380:1404]; N = idx[1380:1392]; SR = "moe/r3/build/opus/shepR.py"
    jobs = [("shepR", SR, on, op, s, us) for on, op in (("shep", "subW_shepherd.py"), ("hyb2965", "subX_hyb2965.py")) for s in G for us in (0, 1)]
    for xn, xp in (("shepR", SR), ("shep", "subW_shepherd.py")):
        for on, op in (("2802", "rivals/jaxa623_2802/_entry.py"), ("koshinm", "rivals/koshinm_kaggriculture-local-best-2026-09-21/_entry.py")):
            jobs += [(xn, xp, on, op, s, us) for s in N for us in (0, 1)]
    out = ROOT + "/moe/r3/build/opus/gate_w1p.jsonl"; open(out, "w").close(); pool(closed, jobs, out)
