"""Summarise gate_bc.jsonl / gate_d.jsonl into the pre-registered gate numbers (prints markdown, writes summary.json)."""
import json, os, statistics as S, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common

HERE = common.HERE


def rows(fn):
    p = os.path.join(HERE, fn)
    return [json.loads(l) for l in open(p)] if os.path.exists(p) else []


def se(xs):
    return S.stdev(xs) / len(xs) ** 0.5 if len(xs) > 1 else float("nan")


def bc():
    R = rows("gate_bc.jsonl")
    m28 = {int(r["ep"]): r for r in common.mirror28()}
    w18 = {int(r["ep"]): r for r in common.wlv18()}
    out = {}
    key = lambda r: (r["ep"], r["base"], r["arm"], r["rmode"])
    G = {}
    for r in R:
        G[key(r)] = r          # last wins (re-runs)
    print(f"gate_bc: {len(R)} games, {len(G)} distinct cells")
    for base in ("C1", "C2"):
        for tapeset, name in ((m28, "mirror28"), (w18, "wlv18")):
            eps = sorted(tapeset)
            for rmode in ("open", "react"):
                van = {ep: G.get((ep, base, "vanilla", rmode)) for ep in eps}
                if not any(van.values()):
                    continue
                # exactness (C1 base, open-loop, mirror tapes were recorded with shepherd in our seat)
                if base == "C1" and rmode == "open":
                    ex = sum(1 for ep in eps if van[ep] and abs(van[ep]["margin"] - tapeset[ep]["margin"]) < 1)
                    print(f"\n[{base} {name} {rmode}] vanilla reproduces recorded margin: {ex}/{sum(1 for ep in eps if van[ep])}")
                vrec = [van[ep]["margin"] for ep in eps if van[ep]]
                vW = sum(1 for m in vrec if m > 0); vL = sum(1 for m in vrec if m < 0)
                print(f"[{base} {name} {rmode}] vanilla record {vW}-{vL} (n={len(vrec)}), mean margin {S.mean(vrec):+.0f}")
                for arm in ("parity", "loo"):
                    cells = [(ep, van[ep], G.get((ep, base, arm, rmode))) for ep in eps]
                    cells = [(ep, v, c) for ep, v, c in cells if v and c]
                    if not cells:
                        continue
                    d = [c["margin"] - v["margin"] for _, v, c in cells]
                    do = [c["ours"] - v["ours"] for _, v, c in cells]
                    dt = [c["theirs"] - v["theirs"] for _, v, c in cells]
                    lw = sum(1 for _, v, c in cells if v["margin"] < 0 and c["margin"] > 0)
                    wl = sum(1 for _, v, c in cells if v["margin"] > 0 and c["margin"] <= 0)
                    nl = sum(1 for _, v, c in cells if v["margin"] < 0); nw = sum(1 for _, v, c in cells if v["margin"] > 0)
                    cW = sum(1 for _, v, c in cells if c["margin"] > 0); cL = sum(1 for _, v, c in cells if c["margin"] < 0)
                    fires = [c["q"].get("pred_fires", 0) for _, v, c in cells]
                    units = [c["q"].get("pred_units", 0) for _, v, c in cells]
                    errs = sum(c["q"].get("pred_errors", 0) for _, v, c in cells)
                    perr = sum(c["p"].get("pred_errors", 0) for _, v, c in cells)
                    pf = [c["p"].get("pred_fires", 0) for _, v, c in cells]
                    shop_ok = sum(1 for _, v, c in cells if c["shops"] == v["shops"])
                    nlib = sorted({c["nlib"] for _, v, c in cells})
                    rr = [c["rival"] for _, v, c in cells if c.get("rival")]
                    rivs = ""
                    if rr:
                        rivs = (f" rival: lots {S.mean([x['lots'] for x in rr]):.0f}/g held {S.mean([x['held'] for x in rr]):.1f}/g "
                                f"rel_price {S.mean([x['released_price'] for x in rr]):.1f} rel_deadline {S.mean([x['released_deadline'] for x in rr]):.1f} "
                                f"hold_ticks {S.mean([x['hold_ticks'] for x in rr]):.0f}")
                    line = (f"  {arm:6s} n={len(cells)} record {cW}-{cL} | mean d {S.mean(d):+.0f} (se {se(d):.0f}, median {S.median(d):+.0f}) | "
                            f"ours {S.mean(do):+.0f} theirs {S.mean(dt):+.0f} | L->W {lw}/{nl} W->L {wl}/{nw} | "
                            f"Q fires {S.mean(fires):.1f}/g units {S.mean(units):.0f}/g err {errs} | P fires {S.mean(pf):.1f}/g err {perr} | "
                            f"shops== {shop_ok}/{len(cells)} nlib {nlib[0]}..{nlib[-1]}{rivs}")
                    print(line)
                    out[f"{base}/{name}/{rmode}/{arm}"] = dict(n=len(cells), W=cW, L=cL, mean_d=S.mean(d), se_d=se(d), median_d=S.median(d),
                                                             d_ours=S.mean(do), d_theirs=S.mean(dt), LtoW=lw, nL=nl, WtoL=wl, nW=nw,
                                                             q_fires=S.mean(fires), q_units=S.mean(units), q_err=errs, p_fires=S.mean(pf), p_err=perr,
                                                             shops_ok=shop_ok, vanilla_W=vW, vanilla_L=vL,
                                                             per_game=[(ep, v["margin"], c["margin"]) for ep, v, c in cells])
        # gate (c): our-bank component retained under the reactive rival
        for name in ("mirror28", "wlv18"):
            for arm in ("parity", "loo"):
                o = out.get(f"{base}/{name}/open/{arm}"); r = out.get(f"{base}/{name}/react/{arm}")
                if o and r:
                    ratio = r["d_ours"] / o["d_ours"] if o["d_ours"] else float("nan")
                    print(f"  (c) {base} {name} {arm}: our-bank d open {o['d_ours']:+.0f} -> react {r['d_ours']:+.0f} = {ratio*100:.0f}% retained; "
                          f"margin d open {o['mean_d']:+.0f} -> react {r['mean_d']:+.0f}; record open {o['W']}-{o['L']} -> react {r['W']}-{r['L']}")
                    out[f"{base}/{name}/c/{arm}"] = dict(open_ours=o["d_ours"], react_ours=r["d_ours"], ratio=ratio)
    return out


def d():
    R = rows("gate_d.jsonl")
    out = {}
    print(f"\ngate_d: {len(R)} games")
    G = {}
    for r in R:
        G[(r["a"], r["b"], r["seed"], r["swap"])] = r
    for (a, b) in sorted({(r["a"], r["b"]) for r in R}):
        cells = [r for r in G.values() if r["a"] == a and r["b"] == b]
        W = sum(1 for r in cells if r["margin"] > 0); L = sum(1 for r in cells if r["margin"] < 0); T = len(cells) - W - L
        wr = (W + 0.5 * T) / len(cells)
        ms = [r["margin"] for r in cells]
        s0 = [r for r in cells if not r["swap"]]; s1 = [r for r in cells if r["swap"]]
        w0 = sum(1 for r in s0 if r["margin"] > 0); w1 = sum(1 for r in s1 if r["margin"] > 0)
        qa = [r["tel"][a]["q"].get("pred_fires", 0) for r in cells]; qb = [r["tel"][b]["q"].get("pred_fires", 0) for r in cells]
        ea = sum(r["tel"][a]["q"].get("pred_errors", 0) for r in cells); eb = sum(r["tel"][b]["q"].get("pred_errors", 0) for r in cells)
        pa = [r["tel"][a]["p"].get("pred_fires", 0) for r in cells]; pb = [r["tel"][b]["p"].get("pred_fires", 0) for r in cells]
        errs = sum(1 for r in cells if r["errors"] != [None, None] or r["status"] != ["DONE", "DONE"])
        print(f"  {a} vs {b}: {W}-{L}-{T} WR {wr:.3f} (seat0 {w0}/{len(s0)}, seat1 {w1}/{len(s1)}) mean margin {S.mean(ms):+.0f} se {se(ms):.0f} median {S.median(ms):+.0f} | "
              f"Q fires {a} {S.mean(qa):.1f}/g (err {ea}) {b} {S.mean(qb):.1f}/g (err {eb}) | P fires {S.mean(pa):.1f} / {S.mean(pb):.1f} | game errors {errs}")
        out[f"{a}-{b}"] = dict(W=W, L=L, T=T, WR=wr, n=len(cells), mean=S.mean(ms), se=se(ms), median=S.median(ms), seat0=(w0, len(s0)), seat1=(w1, len(s1)),
                              q_fires_a=S.mean(qa), q_fires_b=S.mean(qb), q_err_a=ea, q_err_b=eb, errors=errs)
    return out


if __name__ == "__main__":
    res = {"bc": bc(), "d": d()}
    json.dump(res, open(os.path.join(HERE, "summary.json"), "w"), indent=1, default=str)
