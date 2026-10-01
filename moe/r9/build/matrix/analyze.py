"""Analyze results.jsonl: pairwise W-L, margins, per-seed outcomes."""
import json, statistics, sys, collections

path = sys.argv[1] if len(sys.argv) > 1 else "moe/r9/build/matrix/results.jsonl"
recs = [json.loads(l) for l in open(path)]

def short(p):
    return p.split("/")[-1].replace("subAB_m30b.py", "M30B").replace(".py", "")

pairs = collections.defaultdict(list)
for r in recs:
    pairs[(r["a"], r["b"])].append(r)

rows = []
for (a, b), rs in sorted(pairs.items()):
    ok = [r for r in rs if r["ra"] is not None and r["rb"] is not None]
    errs = [r for r in rs if r["ra"] is None or r["rb"] is None]
    wa = sum(1 for r in ok if r["ra"] > r["rb"])
    wb = sum(1 for r in ok if r["rb"] > r["ra"])
    ti = len(ok) - wa - wb
    ma = statistics.mean(r["ra"] - r["rb"] for r in ok) if ok else float("nan")
    seed_won_a = sorted(set(r["seed"] for r in ok if r["ra"] > r["rb"]))
    seed_won_b = sorted(set(r["seed"] for r in ok if r["rb"] > r["ra"]))
    rows.append((a, b, wa, wb, ti, ma, len(ok), len(errs),
                 seed_won_a, seed_won_b,
                 [r.get("err") or str(r.get("errors")) for r in errs][:3]))

for a, b, wa, wb, ti, ma, n, ne, swa, swb, err in rows:
    print(f"{short(a):>16} vs {short(b):<16}  W{wa:>2}-L{wb:>2}-T{ti:<2} "
          f"margin {ma:+8.0f}  n={n} err={ne}")
    if ne:
        print(f"    errors: {err}")
    print(f"    seeds {short(a)} won: {swa}")
    print(f"    seeds {short(b)} won: {swb}")
