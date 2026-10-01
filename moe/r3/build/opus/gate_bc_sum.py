"""Summarize gate_bc.jsonl against Fable's pre-registered (b)/(c) thresholds (DECISION_R3)."""
import json, sys, statistics as st
sys.path.insert(0, "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/fable")
import common
R = [json.loads(l) for l in open("gate_bc.jsonl")]
m28 = {int(r["ep"]) for r in common.mirror28()}; w18 = {int(r["ep"]) for r in common.wlv18()}
V = {(r["ep"], r["base"], r["rmode"]): r for r in R if r["arm"] == "vanilla"}
for base in ("C1", "C2"):
    for arm in ("parity", "loo"):
        ob = {}
        for rmode in ("open", "react"):
            for tag, S in (("mirror28", m28), ("wlv18", w18)):
                X = [r for r in R if r["base"] == base and r["arm"] == arm and r["rmode"] == rmode and r["ep"] in S and (r["ep"], base, rmode) in V]
                if not X: continue
                d = [r["margin"] - V[(r["ep"], base, rmode)]["margin"] for r in X]
                do = [r["ours"] - V[(r["ep"], base, rmode)]["ours"] for r in X]
                van = [V[(r["ep"], base, rmode)]["margin"] for r in X]
                lw = sum(1 for r, v in zip(X, van) if v <= 0 < r["margin"]); wl = sum(1 for r, v in zip(X, van) if r["margin"] <= 0 < v)
                nl = sum(1 for v in van if v <= 0)
                ob[(rmode, tag)] = st.mean(do)
                extra = ""
                if rmode == "react" and ("open", tag) in ob and ob[("open", tag)]:
                    extra = f" | our-bank kept {st.mean(do)/ob[('open', tag)]*100:.0f}% of open"
                print(f"{base} {arm:6s} {rmode:5s} {tag:8s} n={len(X)} vanilla W-L {len(X)-nl}-{nl} -> {sum(r['margin']>0 for r in X)}-{sum(r['margin']<=0 for r in X)} | mean d {st.mean(d):+6.0f} (se {st.stdev(d)/len(d)**.5:.0f}) our-bank {st.mean(do):+5.0f} | L->W {lw}/{nl} W->L {wl}{extra}")
