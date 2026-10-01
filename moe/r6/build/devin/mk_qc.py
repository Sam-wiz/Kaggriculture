"""Build harvest_qc.py = harvest_q.py + censor-aware _v92_q_update.

Defect (astra predict2_censor_probe.json): when prev price <= 3 the rival's sale is
unobservable, so `seen` records nothing; a library tick at that (tau,i) is scored as an
unmatched tick (-PF) even though the sale may have happened. Indistinguishable cases
(hidden floor sale vs no sale) score -1 vs 0 -> false negative evidence against streams
whose events sit in low-price windows.

Fix: mark (tick,item) as censored whenever price <=3 made the sale unobservable; in the
finalise loop skip BOTH the -PF penalty (no positive evidence either way) for ticks whose
+-1 observation window is censored.
"""
src = open("moe/r6/build/opus/hv/harvest_q.py").read()

OLD_STATE = '''    return {"step": -1, "obs": {}, "evs": evs, "index": index, "m": [0] * n, "f": [0] * n, "near": [0] * n,
            "score": [0.0] * n, "best": 0 if n else None, "done": 150}'''
NEW_STATE = '''    return {"step": -1, "obs": {}, "cens": set(), "evs": evs, "index": index, "m": [0] * n, "f": [0] * n, "near": [0] * n,
            "score": [0.0] * n, "best": 0 if n else None, "done": 150}'''
assert src.count(OLD_STATE) == 1
src = src.replace(OLD_STATE, NEW_STATE)

OLD_OBS = '''    seen = st["obs"]
    if prev and prev["step"] == step - 1:
        inv = obs["market"]["inventory"]
        draw = _v9_town_draw(prev["shops"], prev["step"])
        for i, item in enumerate(_V92_Q_ITEMS):
            if prev["prices"].get(item, 0) <= 3:
                continue'''
NEW_OBS = '''    seen = st["obs"]
    cens = st["cens"]
    if prev and prev["step"] == step - 1:
        inv = obs["market"]["inventory"]
        draw = _v9_town_draw(prev["shops"], prev["step"])
        for i, item in enumerate(_V92_Q_ITEMS):
            if prev["prices"].get(item, 0) <= 3:
                cens.add((step - 1, i))
                continue'''
assert src.count(OLD_OBS) == 1
src = src.replace(OLD_OBS, NEW_OBS)

OLD_LOOP = '''        for i in range(3):
            hit = (tau, i) in seen or (tau - 1, i) in seen or (tau + 1, i) in seen
            for c in index.get((tau, i), ()):
                if hit:
                    m[c] += 1
                    score[c] += 1.0
                else:
                    f[c] += 1
                    score[c] -= _V92_Q_PF
                    if c == best:
                        rescan = True'''
NEW_LOOP = '''        for i in range(3):
            hit = (tau, i) in seen or (tau - 1, i) in seen or (tau + 1, i) in seen
            unobs = (tau - 1, i) in cens or (tau, i) in cens or (tau + 1, i) in cens
            for c in index.get((tau, i), ()):
                if hit:
                    m[c] += 1
                    score[c] += 1.0
                elif not unobs:
                    f[c] += 1
                    score[c] -= _V92_Q_PF
                    if c == best:
                        rescan = True'''
assert src.count(OLD_LOOP) == 1
src = src.replace(OLD_LOOP, NEW_LOOP)

open("moe/r6/build/devin/harvest_qc.py", "w").write(src)
print("wrote harvest_qc.py", len(src))
