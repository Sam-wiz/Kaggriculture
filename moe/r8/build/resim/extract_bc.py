"""Bulk BC extraction via resim: emits rows in the EXACT schema of
mine/rawkeep/bc_extract2.py / bc_extract_team.py:

    {ep, t, ui, xy, d, dshed, inv, on, G, y, y2}

Causal pairing (bc_extract_team convention): row t (1..719) = features of the
observation the agent saw when it chose actions[t] -- i.e. resim pre-state at
game-step t-1, labels from tape action index t.

Usage:
    python extract_bc.py "M & M & P & Q" out.jsonl [workers]
"""
import gzip, json, glob, os, sys
from collections import deque
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from resim import resim, PASS  # noqa: E402

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
T10 = ROOT + "/mine/top10"

CROPS = ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON"]
ANIMALS = ["GOOSE", "COW", "SHEEP"]
CENTERS = [(4, 4), (5, 4), (4, 5), (5, 5)]
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
MOVES = {"NORTH", "SOUTH", "EAST", "WEST"}
MASKKEYS = ["water", "harvest", "feed", "care", "cfert", "dig", "empty", "struct_free"]


def cls(op):
    k = op[0]
    if k in ("PLANT", "PICKUP", "PLACE"):
        return f"{k}:{op[1]}"
    return k


def bfs_nearest(tiles, masks, sx, sy):
    H = len(tiles); W = len(tiles[0])
    found = {}
    shed_dir = None
    seen = [[False] * W for _ in range(H)]
    q = deque([(sx, sy, 0, 0, 0)]); seen[sy][sx] = True
    while q and (len(found) < len(MASKKEYS) or shed_dir is None):
        x, y, d, fdx, fdy = q.popleft()
        for k in MASKKEYS:
            if k not in found and masks[k][y][x]:
                found[k] = (d, fdx, fdy)
        if (x, y) in CENTERS and shed_dir is None:
            shed_dir = (d, fdx, fdy)
        if len(found) == len(MASKKEYS) and shed_dir is not None:
            break
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H and not seen[ny][nx]:
                seen[ny][nx] = True
                q.append((nx, ny, d + 1, dx if d == 0 else fdx, dy if d == 0 else fdy))
    out = {k: found.get(k, (99, 0, 0)) for k in MASKKEYS}
    return out, (shed_dir or (99, 0, 0))


def board_scan(me):
    tiles = me["tiles"]; H = len(tiles); W = len(tiles[0])
    masks = {k: [[False] * W for _ in range(H)] for k in
             ["water", "harvest", "feed", "care", "cfert", "dig", "empty",
              "plantable", "struct_free", "fertok"]}
    for y in range(H):
        for x in range(W):
            t = tiles[y][x]
            if t is None:
                masks["empty"][y][x] = masks["plantable"][y][x] = True
            elif isinstance(t, dict):
                k = t.get("kind")
                if k == "WEED":
                    masks["dig"][y][x] = True
                elif k == "PLANT":
                    if not t.get("watered_today"):
                        masks["water"][y][x] = True
                    if (t.get("yield_units") or 0) > 0:
                        masks["harvest"][y][x] = True
                    if not t.get("fertilized_until_day") or t.get("fertilized_until_day", 0) <= 30:
                        masks["fertok"][y][x] = True
                elif k in ("COOP", "PASTURE"):
                    if t.get("animal"):
                        if not t.get("fed_today"):
                            masks["feed"][y][x] = True
                        if not t.get("cared_today"):
                            masks["care"][y][x] = True
                        if t.get("fertilizer_available"):
                            masks["cfert"][y][x] = True
                        if (t.get("yield_units") or 0) > 0:
                            masks["harvest"][y][x] = True
                    else:
                        masks["struct_free"][y][x] = True
    return masks


def next_work(uop, t):
    for tt in range(t, min(t + 12, len(uop))):
        c = uop[tt]
        if c not in MOVES and c != "PASS" and c != "ABSENT":
            return c
    return None


def impossible_in_state(state):
    """First recorded unit op that cannot execute under current resim state.
    Returns (step, player, ui, op, reason) or None."""
    obs0 = state[0].observation
    step = obs0.step
    for pi, s in enumerate(state):
        a = s.action if isinstance(s.action, dict) else {}
        farm = obs0.farms[pi]
        priv = s.observation.private
        ops = [a.get("farmer")] + list(a.get("hands") or [])
        for ui, op in enumerate(ops):
            if not isinstance(op, list) or not op:
                continue
            name = op[0]
            if name in ("NORTH", "SOUTH", "EAST", "WEST", "PASS"):
                continue
            pos = farm["farmer"] if ui == 0 else (
                farm["hands"][ui - 1] if ui - 1 < len(farm["hands"]) else None)
            if pos is None:
                return (step, pi, ui, op, "no such unit")
            x, y = pos
            tile = farm["tiles"][y][x]
            if name == "PLANT":
                crop = op[1] if len(op) > 1 else None
                if tile is not None:
                    return (step, pi, ui, op, "tile occupied/locked")
                if (priv["seeds"].get(crop, 0) or 0) <= 0:
                    return (step, pi, ui, op, "no seeds")
            elif name == "WATER":
                if not (isinstance(tile, dict) and tile.get("kind") == "PLANT"
                        and not tile.get("watered_today")):
                    return (step, pi, ui, op, "no unwatered plant here")
            elif name == "HARVEST":
                if not (isinstance(tile, dict) and (tile.get("yield_units") or 0) > 0):
                    return (step, pi, ui, op, "nothing to harvest")
            elif name == "FEED":
                if not (isinstance(tile, dict) and "animal" in tile
                        and not tile.get("fed_today")):
                    return (step, pi, ui, op, "no unfed animal here")
                inv = priv["inventories"][ui] if ui < len(priv["inventories"]) else {}
                if (inv.get("WHEAT", 0) or 0) <= 0:
                    return (step, pi, ui, op, "no WHEAT in inventory")
            elif name == "PICKUP":
                item = op[1] if len(op) > 1 else None
                if (priv["shed"].get(item, 0) or 0) <= 0:
                    return (step, pi, ui, op, "item not in shed")
            elif name == "CARE":
                if not (isinstance(tile, dict) and "animal" in tile
                        and not tile.get("cared_today")):
                    return (step, pi, ui, op, "no uncared animal here")
            elif name == "COLLECT_FERTILIZER":
                if not (isinstance(tile, dict) and "animal" in tile
                        and tile.get("fertilizer_available")):
                    return (step, pi, ui, op, "no fertilizer available")
    return None


def extract_file(args):
    """Worker: resim one tape, return (rows_text, meta)."""
    path, team = args
    try:
        x = json.load(gzip.open(path, "rt"))
    except Exception as e:
        return "", {"ep": os.path.basename(path), "error": str(e)}
    teams = x.get("teams") or []
    if team not in teams:
        return "", None
    pi = teams.index(team)
    ep = x.get("episode_id"); seed = x.get("seed")
    acts = x.get("actions") or []
    rec = x.get("rewards")

    # per-unit op-class timeline for y2 labels (tape-indexed, like steps[t].action)
    max_units = 0
    for a in acts:
        p = a[pi] if pi < len(a) else None
        act = p if isinstance(p, dict) else {}
        ops = [act.get("farmer")] + list(act.get("hands") or [])
        max_units = max(max_units, len(ops))
    unit_ops = [[] for _ in range(max_units)]
    for a in acts:
        p = a[pi] if pi < len(a) else None
        act = p if isinstance(p, dict) else {}
        ops = [act.get("farmer")] + list(act.get("hands") or [])
        for ui in range(max_units):
            op = ops[ui] if ui < len(ops) else None
            unit_ops[ui].append(cls(list(op)) if isinstance(op, (list, tuple)) and op else "ABSENT")

    rows = []
    first_bad = [None]
    diverge_t = [None]

    def pre_step(s, state, env):
        if first_bad[0] is None:
            first_bad[0] = impossible_in_state(state)
            if first_bad[0] is not None:
                diverge_t[0] = s + 1  # row index whose label/op first failed
        t = s + 1  # bc_extract_team row index
        obs0 = state[0].observation
        me = obs0.farms[pi]
        priv = state[pi].observation.private
        tiles = me["tiles"]
        masks = board_scan(me)
        counts = {k: sum(row.count(True) for row in m) for k, m in masks.items()}
        a = acts[t] if t < len(acts) else None
        act = a[pi] if (a and pi < len(a) and isinstance(a[pi], dict)) else {}
        if not act:
            return  # mirrors bc_extract_team `if not obs or not act: continue`
        units = [me["farmer"]] + list(me.get("hands") or [])
        ops = [act.get("farmer")] + list(act.get("hands") or [])
        shed = priv.get("shed") or {}
        invs = priv.get("inventories") or []
        G = {"day": obs0.day, "hour": obs0.hour, "money": me["money"],
             "hires": me["hires_today"], "quads": len(me["unlocked_quadrants"]),
             "shed_wheat": shed.get("WHEAT", 0), "shed_fert": shed.get("FERTILIZER", 0),
             "shed_animals": sum(shed.get(an, 0) for an in ANIMALS), "cnts": counts}
        for ui, (pos, op) in enumerate(zip(units, ops)):
            if not isinstance(pos, (list, tuple)) or len(pos) < 2:
                continue
            if not isinstance(op, (list, tuple)) or not op:
                op = ["PASS"]
            ux, uy = int(pos[0]), int(pos[1])
            dists, shed_dir = bfs_nearest(tiles, masks, ux, uy)
            inv = invs[ui] if ui < len(invs) else {}
            inv = inv if isinstance(inv, dict) else {}
            t0 = tiles[uy][ux]
            on = {"empty": t0 is None}
            if isinstance(t0, dict):
                k = t0.get("kind")
                on = {"weed": k == "WEED", "plant": k == "PLANT",
                      "animal": bool(t0.get("animal")),
                      "watered": t0.get("watered_today"),
                      "yield": t0.get("yield_units") or 0,
                      "fed": t0.get("fed_today"), "cared": t0.get("cared_today"),
                      "fert_av": t0.get("fertilizer_available")}
            y_raw = cls(list(op))
            y_job = y_raw if y_raw not in MOVES else (next_work(unit_ops[ui], t) or "MOVE_IDLE")
            rows.append({"ep": ep, "t": t, "ui": ui, "xy": [ux, uy],
                         "d": dists, "dshed": shed_dir,
                         "inv": {"WHEAT": inv.get("WHEAT", 0),
                                 "FERTILIZER": inv.get("FERTILIZER", 0),
                                 "goods": sum(v for kk, v in inv.items()
                                              if kk not in ANIMALS and kk not in ("WHEAT", "FERTILIZER")),
                                 "animals": sum(inv.get(an, 0) for an in ANIMALS)},
                         "on": on, "G": G, "y": y_raw, "y2": y_job})

    r = resim(acts, seed, pre_step=pre_step)
    errs = [abs(r["money"][i] - rec[i]) for i in range(2)] if rec else [0, 0]
    rel = [errs[i] / max(1.0, abs(rec[i])) for i in range(2)] if rec else [0, 0]
    exact = max(errs) < 1.0
    within1 = max(rel) <= 0.01

    # truncation policy: if not exact, keep only rows whose feature-state (game
    # step s=t-1) precedes the first impossible recorded op (state may already
    # have drifted there); exact eps keep everything.
    keep = rows if exact else [row for row in rows
                               if diverge_t[0] is None or row["t"] < diverge_t[0]]
    text = "".join(json.dumps(row) + "\n" for row in keep)
    meta = {"ep": ep, "seed": seed, "teams": teams, "pi": pi,
            "rec": rec, "got": r["money"], "exact": exact, "within1": within1,
            "maxrel": max(rel), "rows": len(keep), "rows_total": len(rows),
            "diverge_t": diverge_t[0], "first_bad": first_bad[0],
            "status": r["status"]}
    return text, meta


def main():
    team = sys.argv[1] if len(sys.argv) > 1 else "M & M & P & Q"
    out_path = sys.argv[2] if len(sys.argv) > 2 else "bc2r_MMPQ.jsonl"
    workers = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    only = sys.argv[4] if len(sys.argv) > 4 else None

    files = sorted(glob.glob(T10 + "/*.json.gz"))
    if only:  # comma-separated episode ids for quick tests
        keep = set(only.split(","))
        files = [f for f in files if os.path.basename(f).split(".")[0] in keep]

    # pre-scan team membership cheaply (full parse; caches nothing -- fine)
    todo = []
    for f in files:
        try:
            with gzip.open(f, "rt") as fh:
                head = json.load(fh)
            if team in (head.get("teams") or []):
                todo.append((f, team))
        except Exception:
            continue
    print(f"{team}: {len(todo)} tapes", flush=True)

    metas = []
    done = 0
    with open(out_path, "w") as out, ProcessPoolExecutor(max_workers=workers) as pool:
        for text, meta in pool.map(extract_file, todo, chunksize=4):
            if meta:
                metas.append(meta)
                if not meta.get("within1"):
                    print("MISS", meta["ep"], "rec", meta["rec"], "got", meta["got"],
                          "diverge_t", meta["diverge_t"], "first_bad", meta["first_bad"],
                          flush=True)
            out.write(text)
            done += 1
            if done % 25 == 0:
                print(f"  {done}/{len(todo)}", flush=True)
    n = len(metas)
    ex = sum(1 for m in metas if m["exact"])
    w1 = sum(1 for m in metas if m["within1"])
    rows = sum(m["rows"] for m in metas)
    with open(out_path + ".manifest.json", "w") as f:
        json.dump(metas, f, indent=1, default=str)
    print(f"{team}: {n} eps, exact {ex} ({ex/max(1,n):.0%}), within1% {w1} ({w1/max(1,n):.0%}), {rows} rows -> {out_path}")


if __name__ == "__main__":
    main()
