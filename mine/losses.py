"""Why we lose: compare the opponent's schedule to ours, loss by loss."""
import gzip, glob, json, sys, collections, statistics
sys.path.insert(0, ".")
from mine.decode import schedule

OURS = {"COW": 8, "SHEEP": 9, "WHEAT": 195, "STRAWBERRY": 33, "MELON": 12, "CARROT": 9}


def load(subset=None):
    out = []
    for p in sorted(glob.glob("mine/tapes/*.json.gz")):
        with gzip.open(p, "rt") as f:
            r = json.load(f)
        if r.get("our_bank") is None or r.get("opp_bank") is None:
            continue
        out.append(r)
    return out


def sig(s):
    a = s["animals"]; p = s["plants"]
    return dict(COW=a.get("COW", 0), SHEEP=a.get("SHEEP", 0), GOOSE=a.get("GOOSE", 0),
                WHEAT=p.get("WHEAT", 0), STRAW=p.get("STRAWBERRY", 0),
                MELON=p.get("MELON", 0), CARROT=p.get("CARROT", 0),
                TOMATO=p.get("TOMATO", 0))


if __name__ == "__main__":
    recs = load()
    recs = [r for r in recs if r["our_bank"] != 0.0]      # drop our errored episodes
    w = [r for r in recs if r["our_bank"] > r["opp_bank"]]
    l = [r for r in recs if r["our_bank"] < r["opp_bank"]]
    t = [r for r in recs if r["our_bank"] == r["opp_bank"]]
    print(f"episodes {len(recs)}   W{len(w)} L{len(l)} T{len(t)}"
          f"   winrate {(len(w)+0.5*len(t))/len(recs):.3f}")
    print(f"mean bank ours {statistics.mean(r['our_bank'] for r in recs):,.0f}"
          f"  theirs {statistics.mean(r['opp_bank'] for r in recs):,.0f}")
    print()
    print("LOSSES, worst first — what the winner's plan looked like vs ours")
    print(f"{'opponent':<22}{'margin':>10}{'ourBank':>10}{'COW':>5}{'SHP':>5}{'GSE':>5}"
          f"{'WHEAT':>7}{'STRW':>6}{'MELN':>6}{'CARR':>6}{'TOM':>5}")
    print(f"{'(ours)':<22}{'':>10}{'':>10}{OURS['COW']:>5}{OURS['SHEEP']:>5}{0:>5}"
          f"{OURS['WHEAT']:>7}{OURS['STRAWBERRY']:>6}{OURS['MELON']:>6}{OURS['CARROT']:>6}{0:>5}")
    sigs = []
    for r in sorted(l, key=lambda r: r["our_bank"] - r["opp_bank"]):
        s = sig(schedule(r["opp_actions"]))
        sigs.append(s)
        print(f"{r['opponent'][:21]:<22}{r['our_bank']-r['opp_bank']:>10,.0f}"
              f"{r['our_bank']:>10,.0f}{s['COW']:>5}{s['SHEEP']:>5}{s['GOOSE']:>5}"
              f"{s['WHEAT']:>7}{s['STRAW']:>6}{s['MELON']:>6}{s['CARROT']:>6}{s['TOMATO']:>5}")
    if sigs:
        print("\nmean winner plan:", {k: round(statistics.mean(s[k] for s in sigs), 1) for k in sigs[0]})
    wsigs = [sig(schedule(r["opp_actions"])) for r in w]
    if wsigs:
        print("mean beaten plan: ", {k: round(statistics.mean(s[k] for s in wsigs), 1) for k in wsigs[0]})
