"""Map a round-robin candidate's BT elo to a predicted live rating via the 5 live-rated anchors.
usage: .venv/bin/python moe/r4/build/opus/c1map.py [RR.jsonl] [CAND=C1]
Refits BT on all games in RR.jsonl (rr.py --fit logic), then least-squares live = a + b*BT on the anchors
(post-lock live ratings: shep ~2100, hyb 1974, f55V2 1930, sirV1 1897, pipe16 ~1800) and prints the candidate's
mapped rating plus the number of its games. Pre-registered in PREREG_rr_retro.txt.
"""
import io, json, sys, contextlib, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rr

path = sys.argv[1] if len(sys.argv) > 1 else "moe/r4/build/opus/rr_retro.jsonl"
cand = sys.argv[2] if len(sys.argv) > 2 else "C1"
LIVE = dict(shep=2100, hyb=1974, f55V2=1930, sirV1=1897, pipe16=1800)
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    elo = rr.fit(path)
print(buf.getvalue())
xs = [elo[k] for k in LIVE]; ys = [LIVE[k] for k in LIVE]
mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs); a = my - b * mx
n = sum(1 for l in open(path) if cand in (json.loads(l).get("a"), json.loads(l).get("b")))
print(f"map: live = {a:.0f} + {b:.3f} * BT   (anchors refit on this file)")
if cand in elo:
    print(f"{cand}: BT {elo[cand]:+.0f} -> predicted live {a + b * elo[cand]:.0f}   ({n} games; complete = 200)")
