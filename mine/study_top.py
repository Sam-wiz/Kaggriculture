"""Study a top team from their own episodes: are they a fixed tape, and what is the plan?"""
import gzip, glob, json, sys, hashlib, collections, statistics
sys.path.insert(0, ".")
from mine.decode import schedule

TEAM = sys.argv[1] if len(sys.argv) > 1 else "Crop Dusta"


def load():
    out = []
    for p in sorted(glob.glob("mine/top/*.json.gz")):
        with gzip.open(p, "rt") as f:
            d = json.load(f)
        if TEAM not in d["teams"]:
            continue
        seat = d["teams"].index(TEAM)
        acts = [a[seat] for a in d["actions"]]
        out.append(dict(seed=d["seed"], seat=seat, acts=acts,
                        mine=d["rewards"][seat], theirs=d["rewards"][1 - seat],
                        opp=d["teams"][1 - seat], ep=d["episode_id"]))
    return out


if __name__ == "__main__":
    recs = load()
    print(f"episodes with {TEAM}: {len(recs)}")
    if not recs:
        sys.exit()
    w = sum(1 for r in recs if r["mine"] > r["theirs"])
    l = sum(1 for r in recs if r["mine"] < r["theirs"])
    print(f"their record here: {w}W-{l}L-{len(recs)-w-l}T   "
          f"mean bank {statistics.mean(r['mine'] for r in recs):,.0f} "
          f"vs {statistics.mean(r['theirs'] for r in recs):,.0f}")
    zero = sum(1 for r in recs if r["mine"] == 0)
    print(f"their bank-0 games: {zero}")

    # fixed tape?  identical actions across DIFFERENT seeds is the tell
    by_hash = collections.defaultdict(list)
    for r in recs:
        h = hashlib.sha256(json.dumps(r["acts"], sort_keys=True).encode()).hexdigest()[:10]
        by_hash[h].append(r)
    seeds = {r["seed"] for r in recs}
    print(f"distinct action sequences: {len(by_hash)} across {len(seeds)} distinct seeds")
    for h, g in sorted(by_hash.items(), key=lambda kv: -len(kv[1]))[:4]:
        sd = {r['seed'] for r in g}
        print(f"   tape {h}: {len(g)} episodes, {len(sd)} seeds"
              + ("   <-- FIXED TAPE" if len(sd) > 1 else ""))

    # how far into the game are they identical? (prefix agreement across episodes)
    if len(recs) > 1:
        a, b = recs[0]["acts"], recs[1]["acts"]
        n = min(len(a), len(b))
        div = next((i for i in range(n) if json.dumps(a[i], sort_keys=True)
                    != json.dumps(b[i], sort_keys=True)), n)
        print(f"first divergence between two episodes: step {div} (day {div//24})")

    best = max(recs, key=lambda r: r["mine"])
    s = schedule(best["acts"])
    print(f"\nbest game: bank {best['mine']:,.0f} vs {best['opp']} (seed {best['seed']})")
    print("  land days:", s["land"], " max units/day:", s["maxunits"])
    print("  hires:", s["hires"][:150])
    print("  animals:", s["animals"], " plantings:", s["plants"])
    print("  bought:", s["buys"])
    print("  sells:", s["sells"])
    print("  first sell day:", s["first_sell"])
    print("  action mix:", s["ops"])
