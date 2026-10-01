# Compare the embedded V92 PREDICT2 stream libraries of Harvest vs C1R2 (and C1).
import re, ast, zlib, base64, sys, hashlib
def load(fn):
    src = open(fn).read()
    blob = re.search(r"^_V92_P_BLOB = '([^']*)'", src, re.M).group(1)
    idx = ast.literal_eval(re.search(r"^_V92_P_INDEX = (\[.*?\])\s*$", src, re.M).group(1))
    params = {k: re.search(rf"^{k} = (.*)$", src, re.M).group(1) for k in
              ("_V92_P_USE", "_V92_P_H", "_V92_P_K", "_V92_P_TOP", "_V92_P_EVERY")}
    raw = zlib.decompress(base64.b85decode(blob))
    lib = {}
    for pi, (start, length) in enumerate(idx):
        pos = start; n = raw[pos] | raw[pos+1] << 8; pos += 2; streams = []
        for _ in range(n):
            m = raw[pos] | raw[pos+1] << 8; pos += 2; ev = {}; last = 0
            for _ in range(m):
                d = raw[pos]; pos += 1
                if d == 255: t = raw[pos] | raw[pos+1] << 8; pos += 2
                else: t = last + d
                ev[(t, raw[pos])] = raw[pos+1]; pos += 2; last = t
            streams.append(hashlib.md5(repr(sorted(ev.items())).encode()).hexdigest())
        lib[pi] = streams
    return params, lib
L = {fn: load(fn) for fn in sys.argv[1:]}
for fn, (p, lib) in L.items():
    print(fn, p, "streams", sum(len(v) for v in lib.values()), "pairs", len(lib))
fns = list(L)
a, b = L[fns[0]][1], L[fns[1]][1]
sa = {(k, s) for k, v in a.items() for s in v}; sb = {(k, s) for k, v in b.items() for s in v}
print(f"{fns[0]} ∩ {fns[1]}: {len(sa & sb)}; only {fns[0]}: {len(sa - sb)}; only {fns[1]}: {len(sb - sa)}")
