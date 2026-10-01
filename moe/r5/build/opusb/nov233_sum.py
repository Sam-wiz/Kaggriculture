"""Summarise nov233 paired runs. usage: nov233_sum.py FILE.jsonl [FILE ...]"""
import json, math, sys
rows = [json.loads(l) for f in sys.argv[1:] for l in open(f)]
by = {}
for r in rows:
    if "bank" in r:
        by.setdefault(r["seed"], {})[r["arm"]] = r
screened_quiet = sorted({r["seed"] for r in rows if "quiet_at" in r})
pairs = {s: d for s, d in by.items() if "C1" in d and "C1noV233" in d}


def first_diff(a, b):
    for i in range(0, min(len(a), len(b)), 10):
        if a[i:i + 10] != b[i:i + 10]:
            return i // 10
    return None if len(a) == len(b) else min(len(a), len(b)) // 10


def se(xs):
    n = len(xs); m = sum(xs) / n
    return m, (math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1) / n) if n > 1 else float("nan"))


nat, quiet = [], []
for s, d in sorted(pairs.items()):
    o, a = d["C1"], d["C1noV233"]
    rec = dict(seed=s, me=o["me"], req=o["v233_me"]["req"], com=o["v233_me"]["committed"],
               opp_req=o["v233_opp"]["req"], ab_req=a["v233_me"]["req"],
               db=a["bank"] - o["bank"], do=a["opp"] - o["opp"],
               dm=(a["bank"] - a["opp"]) - (o["bank"] - o["opp"]),
               m_off=o["bank"] - o["opp"], m_ab=a["bank"] - a["opp"],
               fd_me=first_diff(o["h_me"], a["h_me"]), fd_opp=first_diff(o["h_opp"], a["h_opp"]),
               first_req=o["first_req"], shops=o["shops"][:4], err=[o["errors"], a["errors"]],
               bank_off=o["bank"])
    (nat if rec["req"] else quiet).append(rec)

print(f"paired seeds {len(pairs)}; native-V233 (off arm made a commit request for our seat) {len(nat)}; quiet {len(quiet)}"
      + (f"; screened-quiet (prefix only) {len(screened_quiet)}" if screened_quiet else ""))
print(f"errors: {sum(bool(any(x for x in e)) for r in nat + quiet for e in r['err'])}")
print(f"ablation fires: ab-arm commit requests for our seat = {sum(r['ab_req'] for r in nat + quiet)} (must be 0); "
      f"native worlds committed {sum(r['com'] > 0 for r in nat)}/{len(nat)}")
ident = [r for r in quiet if r["fd_me"] is None and r["fd_opp"] is None and r["db"] == 0 and r["do"] == 0]
print(f"IDENTITY in quiet worlds: {len(ident)}/{len(quiet)} bit-identical (both seats' 720 action hashes + both banks)")
bad = [r["seed"] for r in quiet if r not in ident]
if bad: print("  NON-IDENTICAL quiet worlds:", bad)
print(f"native worlds: first divergence step (ours) {[r['fd_me'] for r in nat]} vs first request step {[r['first_req'] for r in nat]}")
print(f"native worlds where opponent C1 also requested V233: {sum(r['opp_req'] > 0 for r in nat)}/{len(nat)}")

for lab, grp in (("native", nat), ("all paired", nat + quiet)):
    if not grp: continue
    for k, nm in (("db", "bank"), ("do", "opp bank"), ("dm", "margin")):
        m, e = se([r[k] for r in grp])
        print(f"  {lab:10} d{nm:8} {m:+8.0f} (SE {e:.0f})  >0 {sum(r[k] > 0 for r in grp)}/{len(grp)}")
    wl = lambda key: (sum(r[key] > 0 for r in grp), sum(r[key] < 0 for r in grp), sum(r[key] == 0 for r in grp))
    print(f"  {lab:10} W/L/T vs C1: off {wl('m_off')}  ab {wl('m_ab')}")
for grp_name, pred in (("opp also V233", lambda r: r["opp_req"] > 0), ("opp no V233", lambda r: r["opp_req"] == 0)):
    g = [r for r in nat if pred(r)]
    if g:
        print(f"  native/{grp_name:13} n={len(g):2}  dbank {sum(r['db'] for r in g)/len(g):+8.0f}  dopp {sum(r['do'] for r in g)/len(g):+8.0f}"
              f"  dmargin {sum(r['dm'] for r in g)/len(g):+8.0f}  margin>0 {sum(r['dm'] > 0 for r in g)}/{len(g)}")
print("\nseed     me req oppreq  first_req fd_me  dbank    dopp   dmargin  m_off   m_ab  shops")
for r in nat:
    print(f"{r['seed']} {r['me']}  {r['req']}   {r['opp_req']}      {r['first_req']}   {r['fd_me']}  {r['db']:+7.0f} {r['do']:+7.0f} {r['dm']:+8.0f} {r['m_off']:+7.0f} {r['m_ab']:+7.0f}  {','.join(x[:5] for x in r['shops'])}")
