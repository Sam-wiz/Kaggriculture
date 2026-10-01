"""Which plants does the family leave unwatered?  Replay DSM/Vadim games; at the last step of each day (hour 23,
pre-EOD obs) classify every plant by (crop, age, watered_today, yield_units, ongoing production due today)."""
import glob, gzip, json, os, sys, collections
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT); sys.path.insert(0, ROOT)
import harness
CR = {"WHEAT": (2, 4, 0), "CARROT": (2, 3, 0), "TOMATO": (8, 8, 1), "STRAWBERRY": (10, 10, 2), "MELON": (10, 12, 0)}
PASS = {"farmer": ["PASS"], "hands": [], "market": []}
agg = collections.Counter(); tot = collections.Counter()
n = 0
for p in sorted(glob.glob("mine/top10/*.json.gz"))[::15]:
    d = json.load(gzip.open(p, "rt"))
    seats = [s for s in range(2) if d["teams"][s] in ("DSM", "Vadim Vasilenko", "DECEM")]
    if not seats: continue
    n += 1; acts = d["actions"]
    def mk(seat):
        def ag(obs):
            if seat in seats and obs["hour"] == 23 and obs["day"] >= 3:
                # obs at hour 23 is the state BEFORE hour-23 actions; approximate end-of-day watering state
                day = obs["day"]
                for row in obs["farms"][seat]["tiles"]:
                    for t in row:
                        if isinstance(t, dict) and t.get("kind") == "PLANT":
                            c = t["crop"]; fy, my, iv = CR[c]; age = day - t["planted_day"]
                            if iv == 0:
                                ph = "grow<bonus" if age < (my + 1) // 2 else ("bonus" if age <= my else "ripe/over")
                            else:
                                ph = "pre-prod" if age < fy else ("prod-day" if (age - fy) % iv == 0 else "off-day")
                            key = (c, ph, "unw1" if t.get("consecutive_unwatered", 0) >= 1 else "ok")
                            tot[(c, ph)] += 1
                            if not t.get("watered_today"): agg[(c, ph, key[2])] += 1
            a = acts[obs["step"] + 1][seat] if obs["step"] + 1 < len(acts) else PASS
            return a if isinstance(a, dict) else PASS
        return ag
    harness.run_episode(mk(0), mk(1), seed=d["seed"], copy_obs=False)
print("games", n)
print(f"{'crop':11s} {'phase':11s} {'n':>6s} {'unwatered@h23':>14s} {'of which prev-day missed':>24s}")
for (c, ph), v in sorted(tot.items()):
    u = agg[(c, ph, "ok")] + agg[(c, ph, "unw1")]
    print(f"{c:11s} {ph:11s} {v:6d} {u/v:14.2f} {agg[(c, ph, 'unw1')]/v:24.2f}")
