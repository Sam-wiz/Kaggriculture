"""Fit per-route margin models over shop-count features on decoupled-draw labels.

margin_r(seed) = a_r + sum_s b_{r,s} * count_s(full draw)   [ridge, per route]
At decision time with k shops seen: predict with count_seen_s + (8-k)/8 for unseen.
Router picks argmax predicted margin among prefix-feasible routes, gated by
_RMAP_MIN_GAIN over the current route's predicted margin.
"""
import ast, json, zlib, base64, collections, math, statistics

src = open('subV_sirxL96.py').read()
tree = ast.parse(src)
blob = None
for node in ast.walk(tree):
    if isinstance(node, ast.Assign):
        for t in node.targets:
            if isinstance(t, ast.Name) and t.id == '_R108_DATA':
                for n in ast.walk(node.value):
                    if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) > 10000:
                        blob = n.value
b = json.loads(zlib.decompress(base64.b85decode(blob)))
routes = {int(k): [b["actions"][i] for i in ids] for k, ids in b["routes"].items()}
RIDS = sorted(r for r in routes if r != 1)
SHOPS = sorted({s for r in b['shops'] for s in r['shops']})
NSHOP = len(SHOPS)

# shipped tables (from source, for comparison)
r108 = {tuple(r['shops']): r['route'] for r in b['shops']}
V92 = 9  # yarn override route

rows = [json.loads(l) for l in open('route_labels.jsonl')]
seeds = sorted({r['seed'] for r in rows})
print(f"{len(rows)} labels, {len(seeds)} seeds, {len({r['route'] for r in rows})} routes")

# --- ridge fit per route: margin ~ 1 + counts ---
def ridge(X, y, lam=1.0):
    n, p = len(X), len(X[0])
    A = [[0.0]*p for _ in range(p)]; v = [0.0]*p
    for xi, yi in zip(X, y):
        for i in range(p):
            v[i] += xi[i]*yi
            for j in range(p):
                A[i][j] += xi[i]*xi[j]
    for i in range(p): A[i][i] += lam
    # gauss elim
    M = [row[:] + [vv] for row, vv in zip(A, v)]
    for c in range(p):
        piv = max(range(c, n if n < p else p), key=lambda r: abs(M[r][c]))
        M[c], M[piv] = M[piv], M[c]
        if abs(M[c][c]) < 1e-9: continue
        for r in range(p):
            if r != c and abs(M[r][c]) > 1e-9:
                f = M[r][c]/M[c][c]
                for j in range(c, p+1): M[r][j] -= f*M[c][j]
    coef = [0.0]*p
    for i in range(p):
        if abs(M[i][i]) > 1e-9: coef[i] = M[i][p]/M[i][i]
    return coef

# per-seed normalization: use margin vs seed-mean to cancel seed difficulty
by_seed = collections.defaultdict(dict)
draw_of = {}
for r in rows:
    by_seed[r['seed']][r['route']] = r['bank']
    draw_of[r['seed']] = r['shops']

models = {}
for r in RIDS:
    X, y = [], []
    for seed, banks in by_seed.items():
        if r not in banks: continue
        counts = collections.Counter(draw_of[seed])
        X.append([1.0] + [counts.get(s, 0) for s in SHOPS])
        y.append(banks[r] - statistics.mean(banks.values()))
    if len(X) >= 8:
        coef = ridge(X, y, lam=2.0)
        models[r] = coef

# evaluate: predicted argmax vs oracle argmax, per seed
def predict(r, counts_seen, total_shops=8):
    c = models.get(r)
    if c is None: return None
    k = sum(counts_seen.values())
    feats = [counts_seen.get(s, 0) + (total_shops - k)/NSHOP for s in SHOPS]
    return c[0] + sum(ci*f for ci, f in zip(c[1:], feats))

hit = 0; tot = 0; gaps = []
for seed, banks in by_seed.items():
    draw = draw_of[seed]
    seen2 = collections.Counter(draw[:2])
    best_pred = max((r for r in RIDS if r in models), key=lambda r: predict(r, seen2))
    oracle = max(banks, key=banks.get)
    if best_pred == oracle: hit += 1
    gaps.append(banks[oracle] - banks.get(best_pred, oracle and banks[oracle]))
    tot += 1
print(f"day-6 model: oracle-hit {hit}/{tot}, mean regret {statistics.mean(gaps):.0f} (vs shipped-map regret TBD)")

# vs shipped router pick
ship_gap = []
for seed, banks in by_seed.items():
    pair = tuple(draw_of[seed][:2])
    shipped = V92 if 'YARN_STORE' in pair else r108.get(pair, 100)
    oracle = max(banks, key=banks.get)
    ship_gap.append(banks[oracle] - banks.get(shipped, banks[oracle]))
print(f"shipped router mean regret: {statistics.mean(ship_gap):.0f}")
json.dump({'models': {str(k): v for k, v in models.items()}}, open('route_models.json','w'))
