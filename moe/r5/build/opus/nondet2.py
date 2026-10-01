"""Versions vs nondeterminism: for each family team, signature = own actions at the divergence steps;
cross-tab against date. Consistent co-occurring signatures that split by date => versions."""
import gzip, json, glob, collections
FAM = {"Vadim Vasilenko", "DECEM", "Unknown Mother-Goose", "DSM"}
rows = collections.defaultdict(list)
for f in sorted(glob.glob("mine/top10/*.json.gz")):
    d = json.load(gzip.open(f, "rt"))
    for s in range(2):
        t = d["teams"][s]
        if t not in FAM: continue
        a = d["actions"]
        def g(k):
            x = a[k + 1][s]; return x if isinstance(x, dict) else {}
        sig10 = json.dumps((g(10).get("hands") or [None])[0])
        m13 = [m for m in (g(13).get("market") or []) if m[:2] == ["BUY_SEED", "WHEAT"]]
        sig13 = m13[0][2] if m13 else None
        sig21 = json.dumps(g(21).get("farmer"))
        opp0 = json.dumps(a[1][1 - s].get("market") if isinstance(a[1][1 - s], dict) else None)[:40]
        rows[t].append((d["date"], d["episode_id"], sig10, sig13, sig21, opp0))
for t, L in rows.items():
    c = collections.Counter((r[0], r[2], r[3]) for r in L)
    print("==", t)
    for k, v in sorted(c.items()): print("   ", k, v)
