# Ledger probe (r7 09-30k): is the dispatch "ledger" = hindsight mission targets, and does it explain choices?
# Mission = run of a unit's ops ending in an on-tile work op; target T = tile where the work op fires.
# M1 persistence: mid-mission moves that reduce Manhattan distance to T.
# M2 causal identifiability: # job tiles (of T's type, present at mission start) consistent with the move prefix.
# M3 decision rule at travel-mission start: T == nearest same-type job tile, with/without excluding tiles
#    claimed by other units' active missions (hindsight ledger). Collision rate T in claimed vs nearest in claimed.
import gzip, json, glob, sys
from collections import Counter, defaultdict
from multiprocessing import Pool

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
TEAM = sys.argv[1] if len(sys.argv) > 1 else "DSM"
MV = {"NORTH": (0, -1), "SOUTH": (0, 1), "EAST": (1, 0), "WEST": (-1, 0)}
WORK = {"WATER": "water", "HARVEST": "harvest", "FEED": "feed", "CARE": "care",
        "COLLECT_FERTILIZER": "cfert", "DIG": "dig", "PLANT": "empty"}

def jobs(tiles):
    J = defaultdict(set)
    for y, row in enumerate(tiles):
        for x, t in enumerate(row):
            if t is None: J["empty"].add((x, y))
            elif isinstance(t, dict):
                k = t.get("kind")
                if k == "WEED": J["dig"].add((x, y))
                elif k == "PLANT":
                    if not t.get("watered_today"): J["water"].add((x, y))
                    if (t.get("yield_units") or 0) > 0: J["harvest"].add((x, y))
                elif k in ("COOP", "PASTURE") and t.get("animal"):
                    if not t.get("fed_today"): J["feed"].add((x, y))
                    if not t.get("cared_today"): J["care"].add((x, y))
                    if t.get("fertilizer_available"): J["cfert"].add((x, y))
                    if (t.get("yield_units") or 0) > 0: J["harvest"].add((x, y))
    return J

man = lambda a, b: abs(a[0]-b[0]) + abs(a[1]-b[1])

def one(f):
    x = json.load(gzip.open(f, "rt"))
    teams = x["info"]["TeamNames"]
    if TEAM not in teams: return None
    pi = teams.index(TEAM); S = x["steps"]
    C = Counter()
    # per (day, ui): list of (t, pos, opname); unit identity valid within a day
    seq = defaultdict(list); J_at = {}
    for t in range(1, len(S)):
        if pi >= len(S[t]): break
        act = S[t][pi].get("action") or {}; obs = S[t-1][pi].get("observation") or {}
        if not obs or not act: continue
        me = obs["farms"][pi]
        units = [me["farmer"]] + list(me.get("hands") or [])
        ops = [act.get("farmer")] + list(act.get("hands") or [])
        J_at[t] = jobs(me["tiles"])
        for ui, (p, op) in enumerate(zip(units, ops)):
            if not isinstance(op, (list, tuple)) or not op: op = ["PASS"]
            seq[(obs["day"], ui)].append((t, tuple(p), op[0]))
    # segment missions
    missions = []  # (ui, day, start_t, end_t, T, type, moves[(t,pos,op)])
    for (day, ui), s in seq.items():
        cur = []
        for (t, p, op) in s:
            cur.append((t, p, op))
            if op in WORK:
                mv = [c for c in cur if c[2] in MV]
                missions.append((ui, day, cur[0][0], t, p, WORK[op], mv, cur[0][1]))
                cur = []
            elif op not in MV and op != "PASS":
                cur = []  # shed/other op: resets
    active = defaultdict(list)  # t -> [(ui, T)]
    for m in missions:
        for tt in range(m[2], m[3]+1): active[tt].append((m[0], m[4], m[2]))
    for (ui, day, st, en, T, typ, mv, p0) in missions:
        # M1
        for (t, p, op) in mv:
            dx, dy = MV[op]; C["mv"] += 1
            if man((p[0]+dx, p[1]+dy), T) < man(p, T): C["mv_toward"] += 1
        if not mv: continue
        C["travel"] += 1
        J = J_at.get(st, {}).get(typ, set())
        if T not in J: C["T_not_job_at_start"] += 1; continue
        # M2: candidates consistent with first k moves
        for k in (1, 2, 3):
            if len(mv) < k: continue
            cand = [c for c in J if all(man((p[0]+MV[o][0], p[1]+MV[o][1]), c) < man(p, c) for (_, p, o) in mv[:k])]
            C[f"id{k}_n"] += 1; C[f"id{k}_uniq"] += (len(cand) == 1); C[f"id{k}_cand"] += len(cand)
        # M3
        claimed_prior = {Tq for (uq, Tq, sq) in active[st] if uq != ui and sq < st}
        claimed_all = {Tq for (uq, Tq, sq) in active[st] if uq != ui}
        def near(Jset):
            if not Jset: return 0.0, None
            d = min(man(p0, c) for c in Jset); ties = [c for c in Jset if man(p0, c) == d]
            return (1.0/len(ties) if T in ties else 0.0), ties
        for name, cl in (("raw", set()), ("prior", claimed_prior), ("all", claimed_all)):
            sc, ties = near(J - cl)
            C[f"near_{name}"] += sc
        C["T_in_claimed_prior"] += T in claimed_prior
        dmin = min(man(p0, c) for c in J); gap = man(p0, T) - dmin
        C["gap_%s" % (gap if gap < 4 else "4+")] += 1
        # 2-step lookahead over same-type jobs: min d(p0,c)+d(c, nearest other)
        def la(c):
            rest = [man(c, e) for e in J if e != c]
            return man(p0, c) + (min(rest) if rest else 0)
        m2 = min(la(c) for c in J); t2 = [c for c in J if la(c) == m2]
        C["la2_tie"] += T in t2
        # any-type nearest (type choice not conditioned): nearest of all work jobs excluding empty
        AJ = set().union(*[J_at[st].get(k, set()) for k in ("water","harvest","feed","care","cfert","dig")])
        if AJ:
            da = min(man(p0, c) for c in AJ); C["any_tie"] += man(p0, T) == da
        _, t0 = near(J); C["T_in_ties"] += bool(t0) and T in t0; C["ntie"] += len(t0 or [])
        if t0 and T in t0 and len(t0) > 1:
            C["tied"] += 1
            d = (T[0]-p0[0], T[1]-p0[1]); C["tb_" + ("N" if d[1]<0 else "S" if d[1]>0 else "") + ("W" if d[0]<0 else "E" if d[0]>0 else "")] += 1
            # scan-order tie-breaks
            C["tb_rowmajor"] += T == min(t0, key=lambda c: (c[1], c[0]))
            C["tb_colmajor"] += T == min(t0, key=lambda c: (c[0], c[1]))
            C["tb_rowmajor_rev"] += T == max(t0, key=lambda c: (c[1], c[0]))
            C["tb_colmajor_rev"] += T == max(t0, key=lambda c: (c[0], c[1]))
        _, ties = near(J)
        C["nearest_in_claimed_prior"] += bool(ties) and all(c in claimed_prior for c in ties)
        C["njobs"] += len(J)
    # static ownership: tiles a unit worked yesterday (any type) = zone ledger
    zone = defaultdict(set)
    for (ui, day, st, en, T, typ, mv, p0) in missions: zone[(day, ui)].add(T)
    nunits = defaultdict(int)
    for (day, ui) in zone: nunits[day] += 1
    for (ui, day, st, en, T, typ, mv, p0) in missions:
        if not mv or day == 0: continue
        J = J_at.get(st, {}).get(typ, set())
        if T not in J: continue
        Z = zone.get((day-1, ui), set())
        C["z_n"] += 1; C["z_Tin"] += T in Z
        C["z_base"] += sum(len(zone.get((day-1, u), set()) & J) for u in range(nunits[day-1])) and len(Z & J) / max(1, len(J))
        JZ = J & Z
        if JZ:
            d = min(man(p0, c) for c in JZ); ties = [c for c in JZ if man(p0, c) == d]
            C["z_near"] += (1.0/len(ties)) if T in ties else 0.0
            C["z_neartie"] += T in ties
        # combined: nearest in zone if any else nearest overall
    # region partition: per (day,type) tiles worked by >1 unit
    wk = defaultdict(set)
    for (ui, day, st, en, T, typ, mv, p0) in missions: wk[(day, typ, T)].add(ui)
    C["wk_tiles"] += len(wk); C["wk_shared"] += sum(len(v) > 1 for v in wk.values())
    return dict(C)

if __name__ == "__main__":
    files = sorted(glob.glob(ROOT + "/mine/rawkeep/*.json.gz"))
    tot = Counter(); n = 0
    with Pool(2) as P:
        for r in P.imap_unordered(one, files):
            if r: tot.update(r); n += 1
    tr = tot["travel"]
    print(TEAM, "eps", n)
    print(" M1 moves toward hindsight target: %d/%d = %.3f" % (tot["mv_toward"], tot["mv"], tot["mv_toward"]/max(1, tot["mv"])))
    print(" travel missions", tr, "target not a job at start:", tot["T_not_job_at_start"])
    v = tr - tot["T_not_job_at_start"]
    for k in (1, 2, 3):
        nn = tot[f"id{k}_n"]
        if nn: print(f" M2 after {k} moves: unique {tot[f'id{k}_uniq']/nn:.3f}, mean cand {tot[f'id{k}_cand']/nn:.2f} (n={nn})")
    print(" mean same-type jobs at start %.1f" % (tot["njobs"]/max(1, v)))
    for name in ("raw", "prior", "all"):
        print(f" M3 T==nearest same-type ({name} claims excluded): {tot['near_'+name]/max(1,v):.3f}")
    print(f" T in nearest-tie set: {tot['T_in_ties']/max(1,v):.3f}, mean tie size {tot['ntie']/max(1,v):.2f}; tied&hit {tot['tied']}")
    print("  tiebreak:", {k[3:]: round(c/max(1,tot['tied']),3) for k,c in tot.items() if k.startswith('tb_')})
    print(f" (day,type,tile) worked by >1 unit: {tot['wk_shared']/max(1,tot['wk_tiles']):.3f} of {tot['wk_tiles']}")
    zn = max(1, tot['z_n'])
    print(f" ZONE: T in unit's yesterday-tiles {tot['z_Tin']/zn:.3f} (expected if random over J: {tot['z_base']/zn:.3f}); T==nearest-in-zone {tot['z_near']/zn:.3f}, in zone-tie {tot['z_neartie']/zn:.3f} (n={tot['z_n']})")
    print("  gap d(T)-d(nearest):", {k[4:]: round(c/max(1,v),3) for k,c in sorted(tot.items()) if k.startswith('gap_')})
    print(f" 2-step lookahead tie contains T: {tot['la2_tie']/max(1,v):.3f}; T at any-type nearest distance: {tot['any_tie']/max(1,v):.3f}")
    print(f" T in claimed_prior: {tot['T_in_claimed_prior']/max(1,v):.3f}; raw-nearest all claimed_prior: {tot['nearest_in_claimed_prior']/max(1,v):.3f}")
