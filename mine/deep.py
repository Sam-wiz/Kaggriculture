"""Full-spectrum comparison of the plans that beat us: not just crops but livestock
timing, structures, land, hiring, feed logistics and sale timing."""
import gzip, glob, json, sys, collections, statistics

OUR_TAPE = dict(COW=8, SHEEP=9, WHEAT=195, STRAW=33, MELON=12, CARROT=9)


def profile(actions):
    """Everything we can read off a recorded action sequence."""
    p = dict(
        plants=collections.Counter(), sells=collections.Counter(),
        buys=collections.Counter(), animals=collections.Counter(),
        ops=collections.Counter(), land_days=[], hires=collections.Counter(),
        build_day={}, place_day={}, first_sell={}, sell_by_day=collections.defaultdict(int),
        animal_buy_day=collections.defaultdict(list), plant_day=collections.defaultdict(list),
        units_day=collections.defaultdict(int), feed_day=collections.Counter(),
        care_day=collections.Counter(), collect_day=collections.Counter(),
        buy_wheat_day=collections.Counter(), n_steps=len(actions),
    )
    for step, a in enumerate(actions):
        if not isinstance(a, dict):
            continue
        day = step // 24
        acts = [a.get("farmer") or ["PASS"]] + list(a.get("hands") or [])
        p["units_day"][day] = max(p["units_day"][day], len(acts))
        for op in acts:
            if not op:
                continue
            k = op[0]
            p["ops"][k] += 1
            if k == "PLANT" and len(op) > 1:
                p["plants"][op[1]] += 1
                p["plant_day"][op[1]].append(day)
            elif k in ("BUILD_COOP", "BUILD_PASTURE"):
                p["build_day"].setdefault(k, []).append(day)
            elif k == "PLACE" and len(op) > 1 and op[1] in ("COW", "SHEEP", "GOOSE"):
                p["place_day"].setdefault(op[1], []).append(day)
            elif k == "FEED":
                p["feed_day"][day] += 1
            elif k == "CARE":
                p["care_day"][day] += 1
            elif k == "COLLECT_FERTILIZER":
                p["collect_day"][day] += 1
        for o in (a.get("market") or []):
            if not o:
                continue
            k = o[0]
            if k == "HIRE":
                p["hires"][day] += 1
            elif k == "BUY_LAND":
                p["land_days"].append(day)
            elif k == "SELL" and len(o) > 2:
                p["sells"][o[1]] += int(o[2]); p["first_sell"].setdefault(o[1], day)
                p["sell_by_day"][day] += int(o[2])
            elif k == "BUY_ANIMAL" and len(o) > 2:
                p["animals"][o[1]] += int(o[2]); p["animal_buy_day"][o[1]].append(day)
            elif k == "BUY_SEED" and len(o) > 2:
                p["buys"]["seed:" + str(o[1])] += int(o[2])
            elif k == "BUY_PRODUCT" and len(o) > 2:
                p["buys"]["buy:" + str(o[1])] += int(o[2])
                if o[1] == "WHEAT":
                    p["buy_wheat_day"][day] += int(o[2])
    return p


def flat(p):
    """One comparable row of scalars."""
    a, pl, s, b = p["animals"], p["plants"], p["sells"], p["buys"]
    def med(xs):
        return statistics.median(xs) if xs else None
    return {
        "COW": a.get("COW", 0), "SHEEP": a.get("SHEEP", 0), "GOOSE": a.get("GOOSE", 0),
        "animals_total": sum(a.values()),
        "cow_day": med(p["animal_buy_day"].get("COW", [])),
        "sheep_day": med(p["animal_buy_day"].get("SHEEP", [])),
        "pastures": len(p["build_day"].get("BUILD_PASTURE", [])),
        "coops": len(p["build_day"].get("BUILD_COOP", [])),
        "first_build": min([d for v in p["build_day"].values() for d in v], default=None),
        "land1": p["land_days"][0] if p["land_days"] else None,
        "land2": p["land_days"][1] if len(p["land_days"]) > 1 else None,
        "n_land": len(p["land_days"]),
        "hires_total": sum(p["hires"].values()),
        "max_units": max(p["units_day"].values()) if p["units_day"] else 0,
        "WHEAT": pl.get("WHEAT", 0), "STRAW": pl.get("STRAWBERRY", 0),
        "MELON": pl.get("MELON", 0), "CARROT": pl.get("CARROT", 0),
        "TOMATO": pl.get("TOMATO", 0),
        "straw_med_day": med(p["plant_day"].get("STRAWBERRY", [])),
        "melon_med_day": med(p["plant_day"].get("MELON", [])),
        "buy_wheat": b.get("buy:WHEAT", 0), "buy_fert": b.get("buy:FERTILIZER", 0),
        "FEED": p["ops"].get("FEED", 0), "CARE": p["ops"].get("CARE", 0),
        "COLLECT": p["ops"].get("COLLECT_FERTILIZER", 0),
        "WATER": p["ops"].get("WATER", 0), "HARVEST": p["ops"].get("HARVEST", 0),
        "PASS": p["ops"].get("PASS", 0), "FERTILIZE": p["ops"].get("FERTILIZE", 0),
        "DIG": p["ops"].get("DIG", 0),
        "sell_milk": s.get("MILK", 0), "sell_wool": s.get("WOOL", 0),
        "sell_straw": s.get("STRAWBERRY", 0), "sell_melon": s.get("MELON", 0),
        "sell_wheat": s.get("WHEAT", 0), "sell_fert": s.get("FERTILIZER", 0),
        "sell_carrot": s.get("CARROT", 0), "sell_tomato": s.get("TOMATO", 0),
        "sell_egg": s.get("EGG", 0),
        "first_sell_milk": p["first_sell"].get("MILK"),
        "first_sell_straw": p["first_sell"].get("STRAWBERRY"),
    }


def load():
    out = []
    for path in sorted(glob.glob("mine/tapes/*.json.gz")):
        with gzip.open(path, "rt") as f:
            r = json.load(f)
        if not r.get("our_bank") or not r.get("opp_actions"):
            continue
        out.append(r)
    return out


if __name__ == "__main__":
    recs = load()
    rows = []
    for r in recs:
        fr = flat(profile(r["opp_actions"]))
        fr["_margin"] = r["our_bank"] - r["opp_bank"]
        fr["_opp"] = r["opponent"]
        fr["_ourbank"] = r["our_bank"]
        fr["_oppbank"] = r["opp_bank"]
        rows.append(fr)
    losses = [r for r in rows if r["_margin"] < 0]
    wins = [r for r in rows if r["_margin"] > 0]
    mirror = [r for r in rows if all(r[k] == v for k, v in OUR_TAPE.items())]
    print(f"games {len(rows)}   losses {len(losses)}   wins {len(wins)}   mirrors {len(mirror)}")
    nonmirror_loss = [r for r in losses if not all(r[k] == v for k, v in OUR_TAPE.items())]
    print(f"non-mirror losses (the real problem): {len(nonmirror_loss)}")
    keys = [k for k in rows[0] if not k.startswith("_")]
    print(f"\n{'metric':<18}{'OURS':>9}{'beat us':>10}{'we beat':>10}{'delta':>10}")
    for k in keys:
        lv = [r[k] for r in nonmirror_loss if r[k] is not None]
        wv = [r[k] for r in wins if r[k] is not None]
        if not lv or not wv:
            continue
        ours = OUR_TAPE.get(k)
        om = mirror[0][k] if mirror else None
        base = ours if ours is not None else om
        lm, wm = statistics.mean(lv), statistics.mean(wv)
        flag = "  <<<" if base is not None and abs(lm - base) > 0.25 * max(1, abs(base)) else ""
        print(f"{k:<18}{(f'{base:.0f}' if base is not None else '-'):>9}"
              f"{lm:>10.1f}{wm:>10.1f}{lm-wm:>10.1f}{flag}")
