"""r5 opus turn 3: options.json, the O1-O3 targets for the C+B planner (THREAD 21:38 / opusb 21:48).
For each revealed-shop prefix at dawn d3 (1 shop), d6 (2), d9 (3): the family's targets
  O1  4th quadrant (SE, $4000): P(buy), buy step, dawn cash around the buy
  O2  herd: cows/sheep/geese at dawn d7 (after the d6 burst), d10 (after d9), d12 (final)
  O3  crops: strawberry seeds d6-15, tomato seeds d9-20, carrot seeds d9-27
plus each option's payback day, from family-realized production and prices, and C1's own values (c1macro.jsonl).
Estimator: order-invariant linear model in shop-demand counts (an3), conditioned on the prefix by replacing each
unrevealed-but-relevant shop by its expected demand (shops are uniform with replacement), so every prefix has a value;
the empirical cell (n eps, mean) is reported beside it.  Also an order test and per-future-shop increments.
"""
import collections, itertools, json, pickle, statistics as st
import numpy as np
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
B = ROOT + "/moe/r5/build/opus/"
D = pickle.load(open(B + "fam.pkl", "rb")); F = D["fam"]
C1 = [json.loads(l) for l in open(B + "c1macro.jsonl")]
DEM = {"BAKERY": ["EGG", "WHEAT"], "PIZZA_SHOP": ["MILK", "TOMATO", "WHEAT"], "BRUNCH_SPOT": ["EGG", "WHEAT", "STRAWBERRY"],
       "YARN_STORE": ["WOOL", "WOOL"], "ICE_CREAM_SHOP": ["STRAWBERRY", "MILK", "WHEAT"], "PET_CAFE": ["CARROT", "CARROT"],
       "SMOOTHIE_SHOP": ["STRAWBERRY", "MILK"], "FARMERS_MARKET": ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY"]}
SHOPS = sorted(DEM)
PR = ["EGG", "MILK", "WOOL", "WHEAT", "TOMATO", "STRAWBERRY", "CARROT"]
TEAMS = sorted({r["team"] for r in F})


def dem(shops):
    c = collections.Counter(p for s in shops for p in DEM[s])
    return np.array([c[p] for p in PR], float)


MU = np.mean([dem([s]) for s in SHOPS], axis=0)          # expected demand of one random shop
LS = lambda r: [s for d in r["dec"] for s in d.get("land_step", [])]
q4 = lambda r: len(LS(r)) >= 3 and LS(r)[2] <= 400       # 4th quadrant bought by d16
q4step = lambda r: LS(r)[2] if len(LS(r)) >= 3 else None
herd = lambda d, a: (lambda r: r["dawn"][d]["herd"].get(a, 0))
seeds = lambda c, lo, hi: (lambda r: sum(r["dec"][d]["seed"].get(c, 0) for d in range(lo, hi + 1)))
# target -> (fn, number of shops revealed when the family's decisions for it are complete)
T = {"cows_d7": (herd(7, "COW"), 2), "sheep_d7": (herd(7, "SHEEP"), 2), "geese_d7": (herd(7, "GOOSE"), 2),
     "cows_d10": (herd(10, "COW"), 3), "sheep_d10": (herd(10, "SHEEP"), 3), "geese_d10": (herd(10, "GOOSE"), 3),
     "cows_d12": (herd(12, "COW"), 3), "sheep_d12": (herd(12, "SHEEP"), 3), "geese_d12": (herd(12, "GOOSE"), 3),
     "str_seed_d2_5": (seeds("STRAWBERRY", 2, 5), 1), "str_seed_d6_15": (seeds("STRAWBERRY", 6, 15), 5),
     "tom_seed_d9_20": (seeds("TOMATO", 9, 20), 6), "car_seed_d9_27": (seeds("CARROT", 9, 27), 8),
     "whe_seed_d6_27": (seeds("WHEAT", 6, 27), 8), "q4_by_d16": (lambda r: float(q4(r)), 3)}


def posfeat(shops, h, fill=False):
    """demand of shop positions 1..min(h,3) separately, positions 4..h pooled; missing positions at expected demand."""
    k = min(h, 3); out = []
    for i in range(k): out.append(dem([shops[i]]) if i < len(shops) else MU)
    if h > 3: out.append(dem(shops[3:h]) + max(0, h - max(3, len(shops))) * MU if len(shops) > 3 else (h - 3) * MU)
    return np.concatenate(out)


def fit(X, y):
    X1 = np.c_[np.ones(len(y)), X]; return np.linalg.lstsq(X1, y, rcond=None)[0]


def cv_r2(X, y, g, k=5):
    X1 = np.c_[np.ones(len(y)), X]; pred = np.zeros(len(y)); g = np.array(g) % k
    for f in range(k):
        b = np.linalg.lstsq(X1[g != f], y[g != f], rcond=None)[0]; pred[g == f] = X1[g == f] @ b
    return 1 - ((y - pred) ** 2).sum() / ((y - y.mean()) ** 2).sum()


grp = [r["ep"] for r in F]
TD = np.array([[r["team"] == t for t in TEAMS] for r in F], float)   # team shares -> pooled / DSM variants
models, report = {}, {}
for name, (fn, h) in T.items():
    y = np.array([fn(r) for r in F], float)
    S = np.array([dem(r["shops"][:h]) for r in F])
    Sq = np.array([posfeat(r["shops"], h) for r in F])
    b = fit(np.c_[TD[:, 1:], Sq], y)
    # order test: position-specific demand for the first min(h,3) shops vs pooled counts
    k = min(h, 3)
    Sp = np.hstack([np.array([dem([r["shops"][i]]) for r in F]) for i in range(k)] + ([np.array([dem(r["shops"][k:h]) for r in F])] if h > k else []))
    r2p, r2o = cv_r2(np.c_[TD[:, 1:], S], y, grp), cv_r2(np.c_[TD[:, 1:], Sp], y, grp)
    tshare = TD.mean(0)[1:]
    models[name] = dict(h=h, b0=b[0], team=dict(zip(TEAMS[1:], b[1:len(TEAMS)])), shop=b[len(TEAMS):], tshare=tshare)
    bc = fit(np.c_[TD[:, 1:], S], y)[len(TEAMS):]
    W = b[len(TEAMS):].reshape(-1, len(PR))
    report[name] = dict(mean=round(y.mean(), 2), sd=round(y.std(), 2), shops_used=h, cv_r2_counts=round(r2p, 3),
                        cv_r2_ordered=round(r2o, 3),
                        coef_per_demanding_shop_pooled=dict(zip(PR, np.round(bc, 3).tolist())),
                        coef_by_position=[dict(zip(PR, np.round(w, 3).tolist())) for w in W],
                        increment_if_shop_at_position={f"pos{i + 1}" if i < 3 else "pos4+": {sh: round(float(W[i] @ (dem([sh]) - MU)), 2) for sh in SHOPS} for i in range(len(W))})


def predict(name, prefix, team=None):
    m = models[name]; h = m["h"]; known = list(prefix[:h]); miss = max(0, h - len(known))
    t = (m["team"].get(team, 0.0) if team and team != TEAMS[0] else 0.0) if team else float(np.dot(list(m["team"].values()), m["tshare"]))
    return float(m["b0"] + t + m["shop"] @ posfeat(known, h))


def cell(name, k, key):
    fn = T[name][0]; seen = {}
    for r in F:
        if tuple(r["shops"][:k]) == key: seen.setdefault(r["ep"], []).append(fn(r))
    v = [x for xs in seen.values() for x in xs]
    return (len(seen), round(st.mean(v), 2) if v else None)


# ---------------- C1 baseline (same quantities; C1 self-play is a mirror, seat 0 only) ----------------
def c1v(name, s):
    fn = T[name][0]
    return fn(dict(dawn=s["dawn"], dec=s["dec"]))


c1 = {}
C1S = [(g["shops"], g["seats"][0]) for g in C1]
for name in T:
    if name == "q4_by_d16":
        v = [float(len(L3) >= 3 and L3[2] <= 400) for L3 in ([x for d in s["dec"] for x in d["land_step"]] for _, s in C1S)]
    else:
        v = [c1v(name, s) for _, s in C1S]
    y = np.array(v, float)
    Sx = np.array([dem(sh[:T[name][1]]) for sh, _ in C1S])
    bb = np.linalg.lstsq(np.c_[np.ones(len(y)), Sx], y, rcond=None)[0] if y.std() > 0 else np.r_[y.mean(), np.zeros(len(PR))]
    c1[name] = dict(mean=round(y.mean(), 2), sd=round(y.std(), 2), min=float(y.min()), max=float(y.max()),
                    coef=dict(zip(PR, np.round(bb[1:], 2).tolist())))
c1_land = collections.Counter(tuple(x for d in s["dec"] for x in d["land_step"]) for _, s in C1S).most_common(3)
c1_cash = [round(st.median(s["dawn"][d]["money"] for _, s in C1S)) for d in range(30)]
fam_cash = [round(st.median(r["dawn"][d]["money"] for r in F)) for d in range(30)]


# ---------------- payback: family-realized production and prices ----------------
def realized_price():
    """units-weighted family sale price per item per day."""
    u = collections.defaultdict(lambda: np.zeros(30)); v = collections.defaultdict(lambda: np.zeros(30))
    for r in F:
        for d in range(30):
            for it, (n, rev) in r["dec"][d]["sell"].items(): u[it][d] += n; v[it][d] += rev
    out = {}
    for it in u:
        p = np.where(u[it] > 0, v[it] / np.maximum(u[it], 1), np.nan)
        # fill gaps forward/backward
        last = np.nanmean(p)
        for d in range(30):
            if np.isnan(p[d]): p[d] = last
            else: last = p[d]
        out[it] = p
    return out


PRICE = realized_price()
ANI = {"COW": ("MILK", 400, 8), "SHEEP": ("WOOL", 500, 6), "GOOSE": ("EGG", 300, 4)}


def animal_curve(a):
    """product units per animal by age (days since purchase day), from single-cohort windows:
       COW/SHEEP cohort = d0 buys (valid while no later cohort of that kind can yield: until d6+lag);
       GOOSE cohort = d6 buys (until d9+lag).  Plus fertilizer/animal-day from d1-d5 (herd = d0 buys only)."""
    prod, lag = ANI[a][0], ANI[a][2]
    if a == "GOOSE": d0, sel = 6, [r for r in F if r["dec"][6]["animal"].get("GOOSE", 0) > 0 and not any(r["dec"][d]["animal"].get("GOOSE", 0) for d in range(0, 6))]
    else: d0, sel = 0, [r for r in F if r["dec"][0]["animal"].get(a, 0) > 0]
    nxt = 9 if a == "GOOSE" else 6
    ages = {}
    for age in range(0, (nxt + lag) - d0):
        d = d0 + age
        if d >= 30: break
        n = sum(r["dec"][d0]["animal"][a] for r in sel)
        units = sum(r["prod"][d].get(prod, 0) for r in sel)
        ages[age] = units / n if n else 0.0
    return ages, len(sel)


def fert_rate():
    tot = n = 0
    for r in F:
        for d in range(1, 6):
            h = sum(r["dawn"][d]["herd"].values())
            if h: tot += r["prod"][d].get("FERTILIZER", 0); n += h
    return tot / n


FR = fert_rate()


def animal_payback(a, buy_day, curve, steady):
    prod, cost, lag = ANI[a]
    cum, pay, total = -cost, None, 0.0
    for d in range(buy_day, 30):
        age = d - buy_day
        u = curve.get(age, steady if age >= lag else 0.0)
        cash = u * PRICE[prod][d] + FR * PRICE["FERTILIZER"][d] - PRICE["WHEAT"][d]   # feed at wheat sale price
        cum += cash; total += cash
        if pay is None and cum >= 0: pay = d
    return pay, round(cum)


def steady_rate(a):
    """units/animal-day, d18-26, all family seats (whole herd, mature)."""
    prod = ANI[a][0]; u = n = 0
    for r in F:
        for d in range(18, 27): u += r["prod"][d].get(prod, 0); n += r["dawn"][d]["herd"].get(a, 0)
    return u / n


payback = {"animals": {}, "crops": {}, "O1_SE": {}}
for a in ANI:
    cur, ncoh = animal_curve(a); ss = steady_rate(a)
    rows = {d: animal_payback(a, d, cur, ss) for d in (0, 3, 6, 9, 10, 12, 15, 18)}
    last = max([d for d in range(30) if animal_payback(a, d, cur, ss)[0] is not None], default=None)
    payback["animals"][a] = dict(cost=ANI[a][1], first_yield_age=ANI[a][2], cohort_seats=ncoh,
                                 units_by_age={k: round(v, 2) for k, v in cur.items()}, steady_units_per_day=round(ss, 3),
                                 fert_per_day=round(FR, 3),
                                 payback_day_by_buy_day={d: v[0] for d, v in rows.items()},
                                 net_to_season_end_by_buy_day={d: v[1] for d, v in rows.items()},
                                 last_buy_day_that_pays_back=last)

# crops: units per plant from family production per tile-day of that crop (d12-26), seed cost per crop
CROP = {"WHEAT": (10, 4), "CARROT": (20, 3), "TOMATO": (50, 8), "STRAWBERRY": (100, 10), "MELON": (80, 10)}
CAP = {"WHEAT": 6, "CARROT": 4, "TOMATO": 8, "STRAWBERRY": 8, "MELON": 6}   # physical max units/plant (fertilized)
CYC = {"WHEAT": 5, "CARROT": 4, "TOMATO": 12, "STRAWBERRY": 17, "MELON": 11}   # tile occupancy days (table)
for c, (cost, first) in CROP.items():
    u = n = 0
    for r in F:
        for d in range(12, 27): u += r["prod"][d].get(c, 0); n += r["dawn"][d]["plants"].get(c, 0)
    per_tile_day = u / n if n else 0
    per_plant = min(per_tile_day * CYC[c], CAP[c])
    rows = {}
    for pd in (3, 6, 9, 12, 15, 18, 21, 24, 26):
        # revenue arrives from age `first` spread evenly over the productive span
        span = list(range(pd + first, min(30, pd + CYC[c])))
        cum, pay = -cost, None
        for d in span:
            cum += per_plant / max(1, CYC[c] - first) * PRICE.get(c, [0] * 30)[d]
            if pay is None and cum >= 0: pay = d
        rows[pd] = (pay, round(cum))
    payback["crops"][c] = dict(seed_cost=cost, first_yield_age=first, units_per_tile_day=round(per_tile_day, 3),
                               units_per_plant=round(per_plant, 2),
                               payback_day_by_plant_day={d: v[0] for d, v in rows.items()},
                               net_per_plant_by_plant_day={d: v[1] for d, v in rows.items()})

# O1: SE contents in family 4q seats (x 5-9, y 5-9 of the 100-char map), and value per SE tile-day
SE = [y * 10 + x for y in range(5, 10) for x in range(5, 10)]
se_mix = {}
for d in (12, 15, 18, 21, 24, 27):
    c = collections.Counter(); n = 0
    for r in F:
        if q4(r) and r["maps"].get(d): c.update(r["maps"][d][i] for i in SE); n += 1
    se_mix[d] = {k: round(v / n, 1) for k, v in c.most_common()}
CH = {"W": "WHEAT", "C": "CARROT", "T": "TOMATO", "S": "STRAWBERRY", "M": "MELON"}


def tile_day_value(c, d):
    pc = payback["crops"][c]; return pc["units_per_tile_day"] * PRICE[c][d] - pc["seed_cost"] / CYC[c]


def se_payback(buy_day):
    cum, pay = -4000.0, None
    for d in range(buy_day, 30):
        dd = min((12, 15, 18, 21, 24, 27), key=lambda x: abs(x - d)) if d >= 12 else 12
        mix = se_mix[dd]; ramp = min(1.0, (d - buy_day) / 3.0)   # first harvests ~3 days after planting
        v = sum(n * tile_day_value(CH[k], d) for k, n in mix.items() if k in CH) * ramp
        cum += v
        if pay is None and cum >= 0: pay = d
    return pay, round(cum)


# empirical O1: same-episode pairs, one 4q family seat vs one 3q family seat (confounded by version, reported only)
byep = collections.defaultdict(list)
for r in F: byep[r["ep"]].append(r)
pairs = [(a["bank"] - b["bank"]) for rs in byep.values() if len(rs) == 2 for a, b in [rs, rs[::-1]] if q4(a) and not q4(b)]
steps4 = [q4step(r) for r in F if q4(r)]
payback["O1_SE"] = dict(se_tile_mix_by_day=se_mix, gross_tile_day_value_note="units/tile-day x realized price - seed/cycle; no labour",
                        payback_day_by_buy_day={d: se_payback(d)[0] for d in (9, 10, 11, 12, 14, 16)},
                        net_to_season_end_by_buy_day={d: se_payback(d)[1] for d in (9, 10, 11, 12, 14, 16)},
                        same_episode_4q_minus_3q_bank=dict(n=len(pairs), mean=round(st.mean(pairs)) if pairs else None,
                                                          se=round(st.pstdev(pairs) / len(pairs) ** 0.5) if len(pairs) > 1 else None))

# O1 cash timing: dawn cash on the buy day and the next dawn, for the family 4q seats
o1_family = dict(p_buy_by_d16=round(np.mean([q4(r) for r in F]), 3),
                 buy_step_quartiles=[int(np.percentile(steps4, q)) for q in (10, 25, 50, 75, 90)],
                 buy_day_modal=collections.Counter(s // 24 for s in steps4).most_common(3),
                 buy_hour_modal=collections.Counter(s % 24 for s in steps4).most_common(3),
                 dawn_cash_on_buy_day_quartiles=[int(np.percentile([r["dawn"][q4step(r) // 24]["money"] for r in F if q4(r)], q)) for q in (10, 25, 50, 75, 90)],
                 dawn_cash_next_day_quartiles=[int(np.percentile([r["dawn"][q4step(r) // 24 + 1]["money"] for r in F if q4(r)], q)) for q in (10, 25, 50, 75, 90)],
                 sells_on_buy_day_before_rev_median=int(st.median(sum(v[1] for v in r["dec"][q4step(r) // 24]["sell"].values()) for r in F if q4(r))),
                 by_team_date={f"{t}|{dt}": round(np.mean([q4(r) for r in F if r["team"] == t and r["date"] == dt]), 2)
                               for t in TEAMS for dt in sorted({r["date"] for r in F}) if any(r["team"] == t and r["date"] == dt for r in F)},
                 third_quadrant_step_median=int(st.median(LS(r)[1] for r in F if len(LS(r)) >= 2)))


# ---------------- per-prefix tables ----------------
OUT_T = {"O1": ["q4_by_d16"], "O2": ["cows_d7", "sheep_d7", "geese_d7", "cows_d10", "sheep_d10", "geese_d10", "cows_d12", "sheep_d12", "geese_d12"],
         "O3": ["str_seed_d2_5", "str_seed_d6_15", "tom_seed_d9_20", "car_seed_d9_27", "whe_seed_d6_27"]}
by_prefix = {}
for day, k in ((3, 1), (6, 2), (9, 3)):
    tab = {}
    for key in itertools.product(SHOPS, repeat=k):
        row = {}
        for o, names in OUT_T.items():
            for nm in names:
                if T[nm][1] < k and nm != "q4_by_d16": continue      # already decided before this prefix: skip
                n, m = cell(nm, k, key)
                clip = (lambda v: min(1.0, max(0.0, v))) if nm == "q4_by_d16" else (lambda v: max(0.0, v))   # linear extrapolation guard
                row[nm] = dict(fam=round(clip(predict(nm, key)), 2), dsm=round(clip(predict(nm, key, "DSM")), 2), n_eps=n, cell_mean=m)
        tab[">".join(key)] = row
    by_prefix[f"d{day}"] = tab

opts = dict(
    meta=dict(written_by="opus, MoE r5 turn 3", source="fam.pkl (2,176 family seats, 1,535 eps, 09-23..25, bank-exact replays); c1macro.jsonl (C1 self-play, 40 fresh seeds 9530001-40)",
              key="ORDERED revealed shops joined by '>' (reveal order d3>d6>d9; order matters for timing: cv_r2_ordered vs cv_r2_counts in `fit`)",
              fam="linear model: shop positions 1-3 separate, 4..h pooled; team-share-weighted family; unrevealed shops within the target's horizon at their expected demand",
              dsm="same model with the DSM team effect (DSM wins 0.65-1.00 head-to-head in-family)",
              price_basis="family units-weighted realized sale price by day (top-vs-top worlds); feed at wheat sale price",
              clip="fam/dsm clipped at 0 (q4 to [0,1]); extreme triple-repeat prefixes are extrapolations (see n_eps)",
              caveat="payback uses family prices and family care/production; in C1 worlds prices differ; labour not charged except where noted"),
    fit=report,
    c1_baseline=dict(values=c1, land_steps_modal=[[list(k), v] for k, v in c1_land], dawn_cash_median=c1_cash, family_dawn_cash_median=fam_cash),
    realized_price_by_day={k: np.round(v, 1).tolist() for k, v in PRICE.items()},
    O1=dict(what="buy SE, the 4th quadrant ($4000); C1 never buys it", family=o1_family, payback=payback["O1_SE"]),
    O2=dict(what="herd to the family's shop-conditioned targets", payback=payback["animals"]),
    O3=dict(what="crop program: strawberry/tomato/carrot seed totals", payback=payback["crops"]),
    by_prefix=by_prefix,
)


def clean(o):
    if isinstance(o, dict): return {str(k): clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [clean(v) for v in o]
    if isinstance(o, (np.floating,)): return round(float(o), 3)
    if isinstance(o, (np.integer,)): return int(o)
    if isinstance(o, np.ndarray): return clean(o.tolist())
    return o


json.dump(clean(opts), open(B + "options.json", "w"), indent=1)
# ---------------- console summary ----------------
print("FIT (target mean sd | cv R2 counts / ordered | C1 mean sd)")
for nm, r in report.items():
    print(f" {nm:15s} {r['mean']:7.2f} {r['sd']:6.2f} | {r['cv_r2_counts']:.2f} / {r['cv_r2_ordered']:.2f} | C1 {c1[nm]['mean']:7.2f} {c1[nm]['sd']:5.2f}")
print("C1 land", c1_land, "\nC1 dawn cash", c1_cash[:16], "\nfam dawn cash", fam_cash[:16])
print("O1 family", json.dumps(clean({k: v for k, v in o1_family.items() if k != 'by_team_date'})))
print("O1 payback", json.dumps(clean(payback["O1_SE"])))
for a, v in payback["animals"].items(): print("O2", a, json.dumps(clean(v)))
for c, v in payback["crops"].items(): print("O3", c, json.dumps(clean(v)))
for pos in ("pos1", "pos2", "pos3"):
    print("increment vs expectation if shop at", pos, "(cows/sheep/geese d12, str d6-15, tom d9-20, car d9-27):")
    for sh in SHOPS: print("  ", f"{sh:15s}", [report[n]["increment_if_shop_at_position"].get(pos, {}).get(sh) for n in ("cows_d12", "sheep_d12", "geese_d12", "str_seed_d6_15", "tom_seed_d9_20", "car_seed_d9_27")])
for nm in ("cows_d12", "sheep_d12", "geese_d12", "str_seed_d6_15", "tom_seed_d9_20", "car_seed_d9_27"): print("C1 coef", nm, c1[nm]["coef"])
for it in ("FERTILIZER", "MILK", "WOOL", "EGG", "TOMATO", "STRAWBERRY", "CARROT", "WHEAT", "MELON"): print("price", it, np.round(PRICE[it]).astype(int).tolist())
