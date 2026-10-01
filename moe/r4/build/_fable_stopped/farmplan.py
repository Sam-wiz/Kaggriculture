"""Farm-plan summary of a reduced episode file (mine/top10/*.json.gz or mine/opp/*.json.gz).
usage: farmplan.py FILE [FILE ...]        (env OURS=<team name> marks our seat)
Importable: summarize(d, seat) -> dict.
"""
import gzip, json, sys, collections

def summarize(d, seat):
    acts = d["actions"]
    land = []; animals = collections.Counter(); hires = collections.Counter(); seeds = collections.Counter()
    builds = collections.Counter(); buyprod = collections.Counter(); sells = collections.Counter()
    sell_steps = 0; nsteps = 0; maxhands = 0; unitops = collections.Counter(); first_day = {}
    for t, step in enumerate(acts):
        a = step[seat]
        if not isinstance(a, dict): continue
        nsteps += 1; day = t // 24
        mk = a.get("market") or []
        if any(m and m[0] == "SELL" for m in mk): sell_steps += 1
        for m in mk:
            if not m: continue
            op = m[0]
            if op == "BUY_LAND": land.append(day)
            elif op == "BUY_ANIMAL": animals[m[1]] += int(m[2]); first_day.setdefault("A_" + m[1], day)
            elif op == "HIRE": hires[day] += 1
            elif op == "BUY_SEED": seeds[m[1]] += int(m[2]); first_day.setdefault("S_" + m[1], day)
            elif op == "BUY_PRODUCT": buyprod[m[1]] += int(m[2])
            elif op == "SELL": sells[m[1]] += int(m[2])
        for u in [a.get("farmer") or []] + list(a.get("hands") or []):
            if u: unitops[u[0]] += 1
            if u and u[0] in ("BUILD_COOP", "BUILD_PASTURE"): builds[u[0]] += 1; first_day.setdefault(u[0], day)
        maxhands = max(maxhands, len(a.get("hands") or []))
    return dict(team=d["teams"][seat], bank=d["rewards"][seat], land=land, animals=dict(animals),
                seeds=dict(seeds), builds=dict(builds), buyprod=dict(buyprod), sells=dict(sells),
                hires=sum(hires.values()), hires_by_day=[hires.get(x, 0) for x in range(30)], maxhands=maxhands,
                sell_steps=sell_steps, unitops=dict(unitops), first_day=first_day)

if __name__ == "__main__":
    ours = None
    import os; ours = os.environ.get("OURS")
    for p in sys.argv[1:]:
        d = json.load(gzip.open(p, "rt"))
        print("\n==", d.get("episode_id"), "seed", d.get("seed"), "shops150", d.get("shops150"), "shops", d.get("shops"))
        for s in (0, 1):
            o = summarize(d, s)
            tag = " <OURS>" if ours and o["team"] == ours else ""
            print(" ", o["team"] + tag, "bank", o["bank"], "land", o["land"], "animals", o["animals"], "builds", o["builds"],
                  "hires", o["hires"], "maxhands", o["maxhands"], "sell_steps", o["sell_steps"])
            print("     seeds", o["seeds"], "buyprod", o["buyprod"])
            print("     sells", o["sells"])
            print("     hires/day", o["hires_by_day"])
            print("     first", o["first_day"])
            print("     unitops", o["unitops"])
