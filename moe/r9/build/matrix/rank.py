"""Round-robin strength ranking from results.jsonl: mean winrate + margin vs field."""
import json, statistics, sys, collections

path = sys.argv[1] if len(sys.argv) > 1 else "moe/r9/build/matrix/results.jsonl"
recs = [json.loads(l) for l in open(path)]

def short(p):
    return (p.split("/")[-1].replace("subAB_m30b.py", "M30B").replace("subAA_harvest.py", "harvest")
            .replace("subV2_f55rec.py", "f55recV2").replace("subZ_C1R2.py", "C1R2")
            .replace("subAC_v8.py", "ACv8(pub)").replace("subW_shepherd.py", "shepherd")
            .replace("subN_metav4.py", "metav4N").replace("v8hh.py", "v8hh").replace(".py", ""))

agents = sorted(set([r["a"] for r in recs] + [r["b"] for r in recs]))
perf = collections.defaultdict(list)   # agent -> list of (won?, margin)
for r in recs:
    if r["ra"] is None or r["rb"] is None:
        continue
    for me, opp, rm, ro in ((r["a"], r["b"], r["ra"], r["rb"]), (r["b"], r["a"], r["rb"], r["ra"])):
        w = 1.0 if rm > ro else 0.5 if rm == ro else 0.0
        perf[me].append((w, rm - ro, opp))

print(f"{'agent':<14}{'games':>6}{'winrate':>9}{'meanMargin':>12}   (RR pool only)")
order = []
for a in agents:
    g = perf[a]
    wr = statistics.mean(w for w, m, o in g)
    mm = statistics.mean(m for w, m, o in g)
    order.append((wr, mm, a))
for wr, mm, a in sorted(order, reverse=True):
    print(f"{short(a):<14}{len(perf[a]):>6}{wr:>9.3f}{mm:>+12.0f}")

# per-agent margin matrix
print("\nmargin matrix (row earns vs col):")
cols = sorted(agents, key=lambda a: -statistics.mean(w for w, m, o in perf[a]))
print(f"{'':<12}" + "".join(f"{short(c):>12}" for c in cols))
for a in cols:
    row = f"{short(a):<12}"
    for c in cols:
        ms = [m for w, m, o in perf[a] if o == c]
        row += f"{statistics.mean(ms):>+12.0f}" if ms else f"{'--':>12}"
    print(row)
