"""Behavioural gap analysis: where does OUR agent differ from the top of the ladder?

Every previous improvement was measured against our own past builds, which flatters us (the slot
"exploit" looked like +3,474 until we checked that the whole field already sells from slot 0). The
honest question is where our behaviour differs from the players ABOVE us.

Replays record both seats' actions, so we can compare our agent to any team on every observable
dimension without needing to play them. Run:  python mine/gap.py [n_games]
"""
import gzip, glob, json, os, sys, collections, statistics

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

UNIT_OPS = ("WATER", "HARVEST", "CARE", "FEED", "COLLECT_FERTILIZER", "FERTILIZE",
            "PLANT", "PICKUP", "PLACE", "DROP", "DIG", "BUILD_COOP", "BUILD_PASTURE", "PASS")
MOVES = {"NORTH", "SOUTH", "EAST", "WEST"}


def profile(actions, seat):
    """Everything observable about one player's season, from their action list alone."""
    p = collections.Counter()
    plant = collections.Counter()
    sells = collections.Counter()
    sell_units = collections.Counter()
    animals = collections.Counter()
    hires_by_day = collections.Counter()
    land_days = []
    sell_slot0 = [0, 0]
    for step, a in enumerate(actions):
        act = a[seat]
        if not isinstance(act, dict):
            continue
        day = step // 24
        for u in [act.get("farmer", ["PASS"])] + list(act.get("hands") or []):
            if not u:
                continue
            op = u[0]
            if op in MOVES:
                p["MOVE"] += 1
            else:
                p[op] += 1
            if op == "PLANT" and len(u) > 1:
                plant[u[1]] += 1
        mk = act.get("market") or []
        idx = [i for i, o in enumerate(mk) if o and o[0] == "SELL"]
        if idx:
            sell_slot0[1] += 1
            if idx[0] == 0:
                sell_slot0[0] += 1
        for o in mk:
            if not o:
                continue
            if o[0] == "SELL" and len(o) > 2:
                sells[o[1]] += 1
                sell_units[o[1]] += int(o[2])
            elif o[0] == "BUY_ANIMAL" and len(o) > 1:
                animals[o[1]] += int(o[2]) if len(o) > 2 else 1
            elif o[0] == "HIRE":
                hires_by_day[day] += 1
            elif o[0] == "BUY_LAND":
                land_days.append(day)
    return dict(units=p, plant=plant, sells=sells, sell_units=sell_units, animals=animals,
                hires=sum(hires_by_day.values()), land_days=land_days,
                slot0=(100.0 * sell_slot0[0] / sell_slot0[1]) if sell_slot0[1] else 0.0)


def our_profile(n_games, agent_path="port3/newtape_slot.py"):
    from harness import load_agent, run_episode
    acc = []
    for s in range(20000, 20000 + n_games):
        rec = []
        base = load_agent(agent_path)
        def probe(obs, cfg=None):
            a = base(obs)
            rec.append([a, {}])
            return a
        run_episode(probe, load_agent(agent_path), seed=s)
        acc.append(profile(rec, 0))
    return acc


def mean_of(profiles, key, sub=None):
    if sub is None:
        return statistics.mean(p[key] for p in profiles)
    return statistics.mean(p[key].get(sub, 0) for p in profiles)


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    by_team = collections.defaultdict(list)
    for f in sorted(glob.glob(os.path.join(ROOT, "mine/top/*.json.gz"))):
        with gzip.open(f, "rt") as fh:
            d = json.load(fh)
        for seat, team in enumerate(d["teams"]):
            by_team[team].append(profile(d["actions"], seat))
    ours = our_profile(n)
    by_team["** US **"] = ours

    teams = [t for t, v in sorted(by_team.items(), key=lambda kv: -len(kv[1])) if len(v) >= 3][:7]
    if "** US **" not in teams:
        teams = ["** US **"] + teams[:6]

    def row(label, fn):
        cells = "".join(f"{fn(by_team[t]):>13}" for t in teams)
        print(f"{label:<22}{cells}")

    print(f"comparing {n} of our games against {len(by_team)-1} teams "
          f"({', '.join(t[:14] for t in teams)})\n")
    hdr = "".join(f"{t[:12]:>13}" for t in teams)
    print(f"{'metric':<22}{hdr}")
    print("-" * (22 + 13 * len(teams)))
    for op in ("WATER", "HARVEST", "CARE", "FEED", "COLLECT_FERTILIZER", "PLANT", "MOVE", "PASS"):
        row(op, lambda v, op=op: f"{mean_of(v,'units',op):,.0f}")
    print()
    for c in ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON"):
        row("plant " + c, lambda v, c=c: f"{mean_of(v,'plant',c):,.0f}")
    print()
    for c in ("GOOSE", "COW", "SHEEP"):
        row("buy " + c, lambda v, c=c: f"{mean_of(v,'animals',c):,.0f}")
    print()
    for c in ("STRAWBERRY", "MILK", "WOOL", "MELON", "FERTILIZER", "WHEAT"):
        row("sell units " + c[:6], lambda v, c=c: f"{mean_of(v,'sell_units',c):,.0f}")
    print()
    row("total hires", lambda v: f"{mean_of(v,'hires'):,.0f}")
    row("SELL in slot 0 %", lambda v: f"{mean_of(v,'slot0'):,.1f}")
    row("land buy days", lambda v: "/".join(str(int(x)) for x in
        (statistics.median([p["land_days"][i] for p in v if len(p["land_days"]) > i])
         for i in range(2) if any(len(p["land_days"]) > i for p in v))) or "-")


if __name__ == "__main__":
    main()
