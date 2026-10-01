"""Opus r3: Fable's mkcand.py verbatim except output names/dir (Fable's session exited before building).
Reads fable/streams_all.json read-only; writes the two *_rebuilt candidates into build/opus/."""
"""Build cand_C1.py (= subW_shepherd.py) and cand_C2.py (= subX_hyb2965.py) with the dormant PREDICT2 library
(`path = None`) replaced by an embedded, zlib+base85 blob of every >=2200 post-lock rival premium-sale stream.
Only the `_v92_q_streams()` body changes; `_V92_EP` (parity holdout) and everything else is untouched."""
import base64, hashlib, json, os, sys, zlib
sys.path.insert(0, "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/fable")
import common
common.setup()

streams = json.load(open(os.path.join(common.HERE, "streams_all.json")))
payload = [{"ep": s["ep"], "ev": s["ev"]} for s in streams if s["ev"]]
raw = json.dumps(payload, separators=(",", ":")).encode("ascii")
blob = base64.b85encode(zlib.compress(raw, 9)).decode("ascii")
assert "'" not in blob and "\\" not in blob
# round trip
back = json.loads(zlib.decompress(base64.b85decode(blob)).decode("ascii"))
assert back == payload
n_ev = sum(len(p["ev"]) for p in payload)
print(f"library: {len(payload)} streams, {n_ev} events, json {len(raw)} B, blob {len(blob)} B, "
      f"sources {dict((k, sum(1 for s in streams if s['src'] == k and s['ev'])) for k in ('idx', 'live', 'wlv'))}")

BUILDS = [("cand_C1_rebuilt.py", "subW_shepherd.py", "        path = None  # Frozen offline build: no environment-dependent external library.\n"),
          ("cand_C2_rebuilt.py", "subX_hyb2965.py", "        path = None  # Offline, self-contained submission.\n")]
OLD_TAIL = ("        out = []\n"
            "        if path:\n"
            "            for x in _v92_json.load(open(path)):\n"
            "                ev = {(t, i): q for t, i, q in x[\"ev\"] if i <= 2}\n"
            "                if ev:\n"
            "                    out.append((x[\"ep\"], ev))\n"
            "        _V92_Q_CACHE[\"streams\"] = out\n")
NEW_BODY = ("        out = []\n"
            "        for x in _v92_json.loads(_v92_zlib.decompress(_v92_b64.b85decode(_V92_Q_BLOB)).decode(\"ascii\")):\n"
            "            ev = {(t, i): q for t, i, q in x[\"ev\"] if i <= 2}\n"
            "            if ev:\n"
            "                out.append((x[\"ep\"], ev))\n"
            "        _V92_Q_CACHE[\"streams\"] = out\n")
IMPORT_LINE = "import json as _v92_json, os as _v92_os\n"
for out_name, base, old_head in BUILDS:
    src = open(os.path.join(common.ROOT, base)).read()
    old = old_head + OLD_TAIL
    assert src.count(old) == 1, (base, src.count(old))
    assert src.count(IMPORT_LINE) == 1, (base, src.count(IMPORT_LINE))
    new = src.replace(old, NEW_BODY)
    ins = (IMPORT_LINE + "import zlib as _v92_zlib, base64 as _v92_b64\n"
           "# Sam-wiz r3 FABLE C-build 2026-09-26: PREDICT2 library = premium-sale (MILK/WOOL/STRAWBERRY) streams of every\n"
           f"# >=2200 post-lock rival tape ({len(payload)} streams / {n_ev} fill events; exact-replay engine fills, price>1, >=2 units).\n"
           "# Format: zlib+base85 of JSON [{\"ep\", \"ev\": [[tick, item_index, qty]]}]; _V92_EP parity holdout mechanism unchanged.\n"
           f"_V92_Q_BLOB = '{blob}'\n")
    new = new.replace(IMPORT_LINE, ins)
    path = os.path.join("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus", out_name)
    open(path, "w").write(new)
    # sanity: only the intended lines differ
    a, b = src.splitlines(), new.splitlines()
    import difflib
    d = [l for l in difflib.unified_diff(a, b, lineterm="", n=0) if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))]
    print(out_name, "from", base, ":", len(d), "changed lines;", "md5", hashlib.md5(new.encode()).hexdigest(), "size", len(new))
    for l in d:
        print("   ", l[:110])
