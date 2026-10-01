"""Build a tape-candidate submission file: embeds K recorded top-team seat streams (zlib+base85 JSON) and plays
one of them open-loop. Selection: fixed index (MODE="fixed") or uniform over the K tapes (MODE="random").
usage: mktape.py OUT.py MODE EP:SEAT[,EP:SEAT...]
The tape for (ep, seat) is actions[t][seat], t = 0..719; the reply to obs t is actions[t+1] (BRIEF convention).
"""
import base64, gzip, hashlib, json, os, sys, zlib
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"


def load_seat(ep, seat):
    for d in ("mine/top10", "mine/top"):
        p = os.path.join(ROOT, d, "%s.json.gz" % ep)
        if os.path.exists(p):
            g = json.load(gzip.open(p, "rt"))
            return [a[seat] if isinstance(a[seat], dict) else None for a in g["actions"]], g["teams"][seat]
    raise FileNotFoundError(ep)


TEMPLATE = '''"""Sam-wiz opusb tape candidate ({mode}). {k} recorded stream(s): {desc}.
Plays one recorded seat stream open-loop (reply to obs t = stream[t+1])."""
import base64 as _tb64, json as _tjson, zlib as _tzlib, random as _trandom

_T_BLOB = '{blob}'
_T_MODE = '{mode}'
_T_FIX = 0
_T_TAPES = None
_T_PICK = {{}}
_T_PASS = {{"farmer": ["PASS"], "hands": [], "market": []}}


def _t_get(o, k):
    try:
        return o[k]
    except Exception:
        return getattr(o, k)


def tape_agent(observation, configuration=None):
    global _T_TAPES
    try:
        if _T_TAPES is None:
            _T_TAPES = _tjson.loads(_tzlib.decompress(_tb64.b85decode(_T_BLOB)).decode("ascii"))
        step = int(_t_get(observation, "step")); player = int(_t_get(observation, "player"))
        if step == 0 or player not in _T_PICK:
            _T_PICK[player] = _T_FIX if _T_MODE == "fixed" else _trandom.randrange(len(_T_TAPES))
        tape = _T_TAPES[_T_PICK[player]]
        a = tape[step + 1] if step + 1 < len(tape) else None
        return a if isinstance(a, dict) else dict(_T_PASS)
    except Exception:
        return dict(_T_PASS)


agent = tape_agent
'''


def build(out, mode, specs):
    tapes, desc = [], []
    for s in specs:
        ep, seat = s.split(":"); seat = int(seat)
        t, team = load_seat(ep, seat); tapes.append(t); desc.append("%s:%d(%s)" % (ep, seat, team))
    raw = json.dumps(tapes, separators=(",", ":"), ensure_ascii=True).encode("ascii")
    blob = base64.b85encode(zlib.compress(raw, 9)).decode("ascii")
    assert "'" not in blob and "\\" not in blob
    src = TEMPLATE.format(mode=mode, k=len(tapes), desc=", ".join(desc), blob=blob)
    open(out, "w").write(src)
    print(out, "tapes", len(tapes), "raw", len(raw), "blob", len(blob), "md5", hashlib.md5(src.encode()).hexdigest())


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2], sys.argv[3].split(","))
