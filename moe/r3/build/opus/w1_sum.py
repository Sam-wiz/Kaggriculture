import json, statistics as st
R = [json.loads(l) for l in open("w1_test.jsonl")]
S = json.load(open("w1_seeds.json")); wlv = {(g["seed"], g["seat"]) for g in S["wlv"]}
arms = sorted({r["o"] for r in R}, key=lambda a: (["yummers", "WL+S", "WL+S2", "WL+R", "WL+O"] + [a]).index(a))
base = {(r["seed"], r["us"]): r["m"] for r in R if r["o"] == "yummers"}
for grp, f in (("WLV14", lambda r: (r["seed"], r["us"]) in wlv), ("fresh40", lambda r: (r["seed"], r["us"]) not in wlv)):
    print("==", grp)
    for a in arms:
        X = [r for r in R if r["o"] == a and f(r)]
        if not X: continue
        ms = [r["m"] for r in X]; w = sum(m > 0 for m in ms)
        d = [r["m"] - base[(r["seed"], r["us"])] for r in X if (r["seed"], r["us"]) in base]
        fires = st.mean(r["to"]["P"].get("pred_fires", 0) for r in X); units = st.mean(r["to"]["P"].get("pred_units", 0) for r in X)
        app = sum(r["picks"]["app"] for r in X); calls = sum(r["picks"]["calls"] for r in X)
        sfire = st.mean(r["tx"]["P"].get("pred_fires", 0) for r in X)
        print(f"  shep vs {a:8s} n={len(X):2d} W-L {w}-{len(X)-w}  mean {st.mean(ms):+7.0f}  median {st.median(ms):+7.0f}  | paired vs yummers {st.mean(d):+6.0f} (se {st.stdev(d)/len(d)**.5 if len(d)>1 else 0:4.0f}, {sum(x<0 for x in d)}/{len(d)} worse for shep) | WL PREDICT fires/g {fires:5.1f} units/g {units:5.0f} | forecasts picking appended stream {app}/{calls} | shep fires/g {sfire:4.1f}")
