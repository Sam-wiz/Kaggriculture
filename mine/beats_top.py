"""What beats a top-5 team? Profile the opponents who defeated Crop Dusta."""
import gzip, glob, json, sys, statistics, collections
sys.path.insert(0, ".")
from mine.decode import schedule

TEAM = "Crop Dusta"
rows = []
for p in sorted(glob.glob("mine/top/*.json.gz")):
    with gzip.open(p, "rt") as f:
        d = json.load(f)
    if TEAM not in d["teams"]:
        continue
    seat = d["teams"].index(TEAM)
    opp = 1 - seat
    s = schedule([a[opp] for a in d["actions"]])
    a, pl = s["animals"], s["plants"]
    rows.append(dict(
        name=d["teams"][opp], their=d["rewards"][opp], cd=d["rewards"][seat],
        beat_cd=d["rewards"][opp] > d["rewards"][seat],
        land1=s["land"][0] if s["land"] else None,
        land2=s["land"][1] if len(s["land"]) > 1 else None,
        nland=len(s["land"]),
        COW=a.get("COW", 0), SHEEP=a.get("SHEEP", 0), GOOSE=a.get("GOOSE", 0),
        WHEAT=pl.get("WHEAT", 0), STRAW=pl.get("STRAWBERRY", 0),
        MELON=pl.get("MELON", 0), CARROT=pl.get("CARROT", 0), TOMATO=pl.get("TOMATO", 0),
        buyWheat=s["buys"].get("buy:WHEAT", 0),
        FERT=s["ops"].get("FERTILIZE", 0), CARE=s["ops"].get("CARE", 0),
        units=s["maxunits"]))
won = [r for r in rows if r["beat_cd"]]
lost = [r for r in rows if not r["beat_cd"]]
print(f"opponents of {TEAM}: {len(rows)}   they beat CD in {len(won)}")
print(f"\n{'metric':<10}{'beat CD':>10}{'lost to CD':>12}{'CD itself':>11}")
CD = dict(COW=7.1, SHEEP=8.0, GOOSE=2.5, WHEAT=130.8, STRAW=28.6, MELON=11.8,
          CARROT=33.9, TOMATO=2.9, buyWheat=1800.8, land1=5.2, land2=8.1,
          nland=2.0, units=13.0, FERT=0.0, CARE=114.4)
for k in ("COW", "SHEEP", "GOOSE", "WHEAT", "STRAW", "MELON", "CARROT", "TOMATO",
          "buyWheat", "land1", "land2", "nland", "units", "FERT", "CARE"):
    wv = [r[k] for r in won if r[k] is not None]
    lv = [r[k] for r in lost if r[k] is not None]
    if not wv or not lv:
        continue
    print(f"{k:<10}{statistics.mean(wv):>10.1f}{statistics.mean(lv):>12.1f}{CD.get(k,0):>11.1f}")
print(f"\ntop banks against CD:")
for r in sorted(rows, key=lambda r: -r["their"])[:8]:
    print(f"  {r['name'][:22]:<24} {r['their']:>9,.0f} vs CD {r['cd']:>9,.0f}"
          f"   cows {r['COW']:>2} sheep {r['SHEEP']:>2} wheat {r['WHEAT']:>3}"
          f" straw {r['STRAW']:>2} carrot {r['CARROT']:>2} tom {r['TOMATO']:>2}")
