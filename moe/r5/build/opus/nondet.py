"""r5 opus: is the family agent deterministic?  On day 0 (steps < 24) there is no RNG in the engine
(weeds/shops roll at end of day), so the state at step t is a pure function of both seats' action
histories.  For every pair of games of team T where BOTH seats' full action histories are identical
up to step t-1, T's action at step t must match if T is deterministic.  Count first divergences."""
import gzip, json, glob, collections
FAM = {"Vadim Vasilenko", "DECEM", "Unknown Mother-Goose", "DSM", "mtmr_s1", "M & M & P & Q"}
G = collections.defaultdict(list)
for f in sorted(glob.glob("mine/top10/*.json.gz")):
    d = json.load(gzip.open(f, "rt"))
    for s in range(2):
        t = d["teams"][s]
        if t not in FAM: continue
        acts = d["actions"]
        own = [json.dumps(acts[k][s], sort_keys=True) for k in range(1, 25)]
        opp = [json.dumps(acts[k][1 - s], sort_keys=True) for k in range(1, 25)]
        G[t].append((own, opp, d["episode_id"], d["teams"][1 - s]))
for t, L in G.items():
    # walk steps; keep partitions of games with identical joint history
    div = collections.Counter(); ex = {}
    parts = [list(range(len(L)))]
    for st in range(24):
        newp = []
        for p in parts:
            if len(p) < 2: continue
            # split by opp action at st (state at st depends on history < st; our action at st is decision)
            byown = collections.defaultdict(list)
            for i in p: byown[L[i][0][st]].append(i)
            if len(byown) > 1:
                div[st] += 1
                if st not in ex:
                    ks = list(byown)[:2]; ex[st] = (L[byown[ks[0]][0]][2], L[byown[ks[1]][0]][2], ks[0][:200], ks[1][:200])
            # continue with joint history identical: group by (own, opp) at st
            j = collections.defaultdict(list)
            for i in p: j[(L[i][0][st], L[i][1][st])].append(i)
            newp += [q for q in j.values() if len(q) >= 2]
        parts = newp
    print(t, "n", len(L), "divergence events by step (identical joint history):", dict(sorted(div.items())), "surviving groups at 24:", len(parts), sum(len(p) for p in parts))
    for st in sorted(ex)[:2]: print("   ex", st, ex[st])
