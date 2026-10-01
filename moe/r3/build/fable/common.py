"""Shared helpers for the r3 FABLE build (arm C1/C2).

Tape formats:
  compact  mine/opp/<ep>.json.gz : {episode_id, seed, teams, rewards, actions}
  full     live_eps/replays/episode-<ep>-replay.json : kaggle replay JSON (seed in info.seed)
Convention (HANDOFF 09-10 / BRIEF addendum): actions[t] PRODUCED step t, so the reply to obs t is actions[t+1].
"""
import gzip, json, os, sys

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
HERE = os.path.join(ROOT, "moe/r3/build/fable")
PASS = {"farmer": ["PASS"], "hands": [], "market": []}
PREM = ("MILK", "WOOL", "STRAWBERRY", "EGG", "MELON")      # premium products (reactive rival scope)
Q_ITEMS = ("MILK", "WOOL", "STRAWBERRY")                   # PREDICT2 stream items (index 0..2)
MAX_ORDERS = 10


def setup():
    os.chdir(ROOT)
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)
    try:
        os.nice(10)
    except Exception:
        pass


def load_tape(path, kind):
    """-> (actions, seed, rewards). actions[t][seat] is the action that produced step t."""
    if kind == "full":
        d = json.load(open(path))
        acts = [[s[0].get("action"), s[1].get("action")] for s in d["steps"]]
        return acts, d["info"]["seed"], d["rewards"]
    d = json.load(gzip.open(path, "rt"))
    return d["actions"], d["seed"], d["rewards"]


def tape_agent(acts, seat):
    """Open-loop replay of one seat."""
    def ag(obs):
        t = obs["step"] + 1
        a = acts[t][seat] if t < len(acts) else None
        return a if isinstance(a, dict) else PASS
    return ag


class RecordingTape:
    """Open-loop replay of one seat that also records what that seat observed (prices, shed) each step."""
    def __init__(self, acts, seat):
        self.acts, self.seat = acts, seat
        self.prices, self.shed = {}, {}

    def __call__(self, obs):
        t = obs["step"]
        self.prices[t] = {k: obs["market"]["prices"].get(k, 0) for k in PREM}
        self.shed[t] = {k: obs["private"]["shed"].get(k, 0) for k in PREM}
        a = self.acts[t + 1][self.seat] if t + 1 < len(self.acts) else None
        return a if isinstance(a, dict) else PASS


def rival_lots(acts, seat, prices, shed):
    """Recorded premium SELL lots of `seat`: [[t, item, qty_order, qty_fill, price_at_t]] in issue order.
    qty_fill clamps the order to the shed at obs t (in-shed sellers; cumulative per item per tick)."""
    out = []
    for t in range(len(acts) - 1):
        a = acts[t + 1][seat]
        if not isinstance(a, dict):
            continue
        used = {}
        for o in (a.get("market") or []):
            if isinstance(o, (list, tuple)) and len(o) >= 3 and o[0] == "SELL" and o[1] in PREM \
                    and isinstance(o[2], (int, float)) and o[2] > 0:
                item, q = o[1], int(o[2])
                have = shed.get(t, {}).get(item, 0) - used.get(item, 0)
                fill = max(0, min(q, have))
                used[item] = used.get(item, 0) + fill
                out.append([t, item, q, fill, prices.get(t, {}).get(item, 0)])
    return out


def stream_from_lots(lots):
    """PREDICT2 stream events [[t, i, q]] over MILK/WOOL/STRAWBERRY from fills (>=2 units, as the layer sees them)."""
    ev = {}
    for t, item, q, fill, p in lots:
        if item in Q_ITEMS and fill > 0:
            k = (t, Q_ITEMS.index(item))
            ev[k] = ev.get(k, 0) + min(100, fill)
    return [[t, i, q] for (t, i), q in sorted(ev.items()) if q >= 2]


class ReactiveTape:
    """Price-reactive rival (SCL tier 1, fable_r2 s4): unit ops and non-premium orders replay open-loop;
    each recorded premium SELL lot waits up to W ticks while the product's current price is below
    (1-delta) x the price the rival saw when it issued the lot. W=0 -> exact open-loop."""
    def __init__(self, acts, seat, lots, W=12, delta=0.10):
        self.acts, self.seat, self.W, self.delta = acts, seat, W, delta
        self.prec = {}
        for t, item, q, fill, p in lots:
            self.prec.setdefault((t, item), []).append(p)
        self.hold = []          # [item, qty, prec, deadline]
        self.report = dict(lots=0, held=0, released_price=0, released_deadline=0, hold_ticks=0, dropped_cap=0)

    def __call__(self, obs):
        t = obs["step"]
        a = self.acts[t + 1][self.seat] if t + 1 < len(self.acts) else None
        if not isinstance(a, dict):
            a = PASS
        if self.W <= 0:
            return a
        prices = obs["market"]["prices"]
        out, keep = [], []
        for lot in self.hold:
            item, q, prec, dl = lot
            if prices.get(item, 0) >= (1 - self.delta) * prec:
                out.append(["SELL", item, q]); self.report["released_price"] += 1
            elif t >= dl:
                out.append(["SELL", item, q]); self.report["released_deadline"] += 1
            else:
                keep.append(lot)
        self.hold = keep
        seen = {}
        for o in (a.get("market") or []):
            if isinstance(o, (list, tuple)) and len(o) >= 3 and o[0] == "SELL" and o[1] in PREM \
                    and isinstance(o[2], (int, float)) and o[2] > 0:
                item = o[1]
                k = seen.get(item, 0); seen[item] = k + 1
                lst = self.prec.get((t, item), [])
                prec = lst[k] if k < len(lst) else (lst[-1] if lst else 0)
                self.report["lots"] += 1
                if prices.get(item, 0) >= (1 - self.delta) * prec:
                    out.append(list(o))
                else:
                    self.hold.append([item, int(o[2]), prec, t + self.W]); self.report["held"] += 1
            else:
                out.append(o)
        self.report["hold_ticks"] += len(self.hold)
        if len(out) > MAX_ORDERS:
            # keep recorded orders; released lots that overflow the cap go back on hold (deadline now)
            extra = out[MAX_ORDERS:]
            out = out[:MAX_ORDERS]
            for o in extra:
                if o[0] == "SELL" and o[1] in PREM:
                    self.hold.append([o[1], int(o[2]), 0, t]); self.report["dropped_cap"] += 1
        return {"farmer": a.get("farmer", ["PASS"]), "hands": a.get("hands", []), "market": out}


def mirror28():
    """The 28 shepherd-seat live games vs >=2200 opponents with unit identity >=0.95 (claude.md s1: 6-22)."""
    rows = json.load(open(os.path.join(ROOT, "moe/r3/fable_scratch/live_rows2.json")))
    sel = [r for r in rows if (r["R"] or 0) >= 2200 and r["same_u"] >= 0.95 and r["build"] == "shepherd"]
    assert len(sel) == 28, len(sel)
    return sel


def wlv18():
    rows = json.load(open(os.path.join(ROOT, "moe/r3/fable_scratch/live_rows2.json")))
    sel = [r for r in rows if tuple(r["open_they"]) == (5, 0) and (r["R"] or 0) >= 2000
           and r["same_u"] >= 0.85 and "Acidic" not in r["opp"]]
    assert len(sel) == 18, len(sel)
    return sel


def tape_universe():
    """Every >=2200 post-lock rival tape: eps_index >=2200 (409) + live 166 at >=2200 (41) + the 18 WLV.
    -> list of dict(ep, src, opp, R, seat(ours), path, kind)."""
    out, seen = [], set()
    for x in json.load(open(os.path.join(ROOT, "moe/opus/eps_index.json"))):
        if (x["R"] or 0) >= 2200 and x["ours"] is not None:
            out.append(dict(ep=int(x["ep"]), src="idx", opp=x["opp"], R=x["R"], seat=x["seat"], path=x["path"], kind=x["kind"], build=x["build"]))
            seen.add(int(x["ep"]))
    rows = json.load(open(os.path.join(ROOT, "moe/r3/fable_scratch/live_rows2.json")))
    wl = {int(r["ep"]) for r in wlv18()}
    for r in rows:
        ep = int(r["ep"])
        if ep in seen:
            continue
        if (r["R"] or 0) >= 2200 or ep in wl:
            out.append(dict(ep=ep, src="wlv" if ep in wl else "live", opp=r["opp"], R=r["R"], seat=r["seat"],
                            path=f"mine/opp/{ep}.json.gz", kind="reduced", build=r["build"]))
            seen.add(ep)
    return out


def load_module_agent(path, name):
    """Fresh module per game (telemetry counters and layer state are module-level)."""
    import harness
    fn = harness.load_agent(path, name=name)
    return fn, sys.modules[name]
