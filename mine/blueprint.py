"""Aggregate a top team's plan across many games, and find what they VARY."""
import gzip, glob, json, sys, statistics, collections
sys.path.insert(0, ".")
from mine.decode import schedule

TEAM = sys.argv[1] if len(sys.argv) > 1 else "Crop Dusta"
rows = []
for p in sorted(glob.glob("mine/top/*.json.gz")):
    with gzip.open(p, "rt") as f:
        d = json.load(f)
    if TEAM not in d["teams"]:
        continue
    seat = d["teams"].index(TEAM)
    s = schedule([a[seat] for a in d["actions"]])
    a, pl, b, se = s["animals"], s["plants"], s["buys"], s["sells"]
    rows.append(dict(
        bank=d["rewards"][seat], opp_bank=d["rewards"][1 - seat],
        land1=s["land"][0] if s["land"] else None,
        land2=s["land"][1] if len(s["land"]) > 1 else None,
        n_land=len(s["land"]), maxunits=s["maxunits"],
        COW=a.get("COW", 0), SHEEP=a.get("SHEEP", 0), GOOSE=a.get("GOOSE", 0),
        WHEAT=pl.get("WHEAT", 0), STRAW=pl.get("STRAWBERRY", 0),
        MELON=pl.get("MELON", 0), CARROT=pl.get("CARROT", 0), TOMATO=pl.get("TOMATO", 0),
        buyWheat=b.get("buy:WHEAT", 0), buyFert=b.get("buy:FERTILIZER", 0),
        WATER=s["ops"].get("WATER", 0), PASS=s["ops"].get("PASS", 0),
        FEED=s["ops"].get("FEED", 0), CARE=s["ops"].get("CARE", 0),
        COLLECT=s["ops"].get("COLLECT_FERTILIZER", 0),
        FERTILIZE=s["ops"].get("FERTILIZE", 0), HARVEST=s["ops"].get("HARVEST", 0),
    ))
print(f"{TEAM}: {len(rows)} games   mean bank {statistics.mean(r['bank'] for r in rows):,.0f}")
keys = [k for k in rows[0] if k not in ("bank", "opp_bank")]
print(f"\n{'metric':<12}{'mean':>9}{'median':>9}{'min':>8}{'max':>8}{'stdev':>9}  varies?")
for k in keys:
    v = [r[k] for r in rows if r[k] is not None]
    if not v:
        continue
    sd = statistics.pstdev(v)
    mu = statistics.mean(v)
    flag = "  <-- ADAPTS" if sd > max(0.15 * abs(mu), 1.5) else ""
    print(f"{k:<12}{mu:>9.1f}{statistics.median(v):>9.1f}{min(v):>8}{max(v):>8}{sd:>9.1f}{flag}")
# does the crop mix track the shop draw?
print("\nwins vs losses — does the plan differ?")
w = [r for r in rows if r["bank"] > r["opp_bank"]]
l = [r for r in rows if r["bank"] < r["opp_bank"]]
print(f"{'metric':<12}{'won':>9}{'lost':>9}")
for k in ("COW", "SHEEP", "WHEAT", "STRAW", "MELON", "CARROT", "buyWheat", "land1", "land2"):
    wv = [r[k] for r in w if r[k] is not None]
    lv = [r[k] for r in l if r[k] is not None]
    if wv and lv:
        print(f"{k:<12}{statistics.mean(wv):>9.1f}{statistics.mean(lv):>9.1f}")
