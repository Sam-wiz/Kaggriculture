"""Fit pair->route overrides from REAL-engine route labels.
For each first-2-shops pair cell: rank routes by mean margin, emit an override
only where measured-best beats the shipped pick by >= MIN_GAP with >= MIN_N seeds.
Also reports per-seed shipped regret (real-engine oracle gap)."""
import json, collections, sys

MIN_N = int(sys.argv[2]) if len(sys.argv) > 2 else 2
MIN_GAP = float(sys.argv[3]) if len(sys.argv) > 3 else 800.0

env = {}
exec(compile(open('subV_sirxL96.py').read(), 'x', 'exec'), env)
R108, V92 = env['_R108_SHOP_ROUTES'], env['_V92_TABLE']

def shipped_pick(pair):
    if 'YARN_STORE' in pair:
        return V92.get(pair, 9)
    return R108.get(pair, 100)

rows = [json.loads(l) for l in open(sys.argv[1] if len(sys.argv) > 1 else 'route_labels_real.jsonl')]
by_seed = collections.defaultdict(dict)
pairs = {}
for r in rows:
    by_seed[r['seed']][r['route']] = r['bank']
    pairs[r['seed']] = tuple(r['shops'][:2])

# per-seed shipped regret
regs = []
for s, banks in by_seed.items():
    sp = shipped_pick(pairs[s])
    regs.append(max(banks.values()) - banks.get(sp, -10**9))
print(f"seeds={len(by_seed)} shipped mean regret={sum(regs)/len(regs):.0f} median={sorted(regs)[len(regs)//2]:.0f}")

# per-pair cell: mean margin per route, count seeds
cells = collections.defaultdict(lambda: collections.defaultdict(list))
for s, banks in by_seed.items():
    p = pairs[s]
    for rt, b in banks.items():
        cells[p][rt].append(b)

overrides = {}
print(f"\n{'pair':<38} {'n':>3} {'ship':>4} {'best':>4} {'gap':>6}")
for p, rtab in sorted(cells.items()):
    n = max(len(v) for v in rtab.values())
    sp = shipped_pick(p)
    means = {rt: sum(v) / len(v) for rt, v in rtab.items() if len(v) >= 1}
    if sp not in means:
        continue
    best = max(means, key=means.get)
    gap = means[best] - means[sp]
    flag = ''
    if best != sp and n >= MIN_N and gap >= MIN_GAP:
        overrides[p] = best
        flag = ' <== OVERRIDE'
    if gap > 300 or flag:
        print(f"{str(p):<38} {n:>3} {sp:>4} {best:>4} {gap:>6.0f}{flag}")

print(f"\noverrides ({len(overrides)}): {overrides}")
with open('rmap2_overrides.json', 'w') as f:
    json.dump({str(k): v for k, v in overrides.items()}, f)
