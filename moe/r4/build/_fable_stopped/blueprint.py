"""Per-day tile blueprint of one recorded seat, from exact replay. usage: blueprint.py FILE SEAT [days,comma]"""
import sys, os, json
from common import *
SYM = {"WHEAT": "w", "CARROT": "k", "TOMATO": "t", "STRAWBERRY": "s", "MELON": "m"}
def cell(t):
    if t is None: return "."
    if t == "LOCKED": return "#"
    k = t.get("kind")
    if k == "PLANT": return SYM.get(t.get("crop"), "?")
    if k == "WEED": return "W"
    if k in ("COOP", "PASTURE"):
        a = t.get("animal")
        return {"COW": "C", "SHEEP": "S", "GOOSE": "G"}.get(a, "P" if k == "PASTURE" else "c")
    return "?"
if __name__ == "__main__":
    d = load_ep(sys.argv[1]); s = int(sys.argv[2])
    days = [int(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3 else [0, 1, 2, 3, 4, 6, 7, 9, 10, 12, 15, 20, 25, 29]
    acts = d["actions"]; g = kagsim.Game(seed=int(d["seed"]))
    print(d["episode_id"], d["teams"][s], "seed", d["seed"], "shops", d["shops"])
    for t in range(720):
        o = g.observe(s)
        if t % 24 == 0 and t // 24 in days:
            f = o["farms"][s]; day = t // 24
            grid = ["".join(cell(f["tiles"][y][x]) for x in range(10)) for y in range(10)]
            shed = {k: v for k, v in o["private"]["shed"].items() if v}
            print(f"day {day:2d} money {f['money']:7.0f} hands {len(f['hands'])} shops {o['town']['unlocked_shops']} shed {shed} seeds {o['private']['seeds']}")
            for row in grid: print("      " + row)
        g.step(rec_action(acts, t, 0), rec_action(acts, t, 1))
    print("final", g.reward(s))
