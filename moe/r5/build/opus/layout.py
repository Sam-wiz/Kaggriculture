"""r5 opus: family canonical layout. Per tile, share of family seats with animal (c/s/g/P/O) vs crop by crop, at d3/d6/d10/d12/d15/d21."""
import pickle, collections, json
F = pickle.load(open("moe/r5/build/opus/fam.pkl", "rb"))["fam"]
out = {}
for d in (3, 6, 10, 12, 15, 21):
    grid = [[collections.Counter() for _ in range(10)] for _ in range(10)]
    for r in F:
        m = r["maps"][d]
        for i, ch in enumerate(m): grid[i // 10][i % 10][ch] += 1
    print(f"--- day {d}: animal share (A=cow-heavy a=sheep g=goose) / modal crop")
    rows = []
    for y in range(10):
        line = ""
        for x in range(10):
            c = grid[y][x]; n = sum(c.values())
            an = c["c"] + c["s"] + c["g"] + c["P"] + c["O"]
            if an / n >= 0.5:
                k = max("csg", key=lambda z: c[z]); line += {"c": "C", "s": "S", "g": "G"}[k] + f"{int(9.99*an/n)}"
            else:
                k, v = max(((z, c[z]) for z in "WCTSM.#w"), key=lambda t: t[1])
                line += k.lower() + f"{int(9.99*v/n)}"
            line += " "
        print("  " + line); rows.append(line)
    out[d] = {f"{x},{y}": dict(grid[y][x]) for y in range(10) for x in range(10)}
json.dump(out, open("moe/r5/build/opus/layout.json", "w"))
