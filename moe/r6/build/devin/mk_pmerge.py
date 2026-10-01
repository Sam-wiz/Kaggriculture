# Merge C1R2's PREDICT-P streams into M30B's P library (same V92 blob format).
# Blob: 64 shop-pair sections; each: u16 n, then n streams of u16 m events.
# Event: d byte (255=>u16 absolute t, else t=last+d) + item_idx byte + qty byte.
import sys, os, zlib, base64, re, json
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)

def get_var(path, name):
    src = open(path).read()
    m = re.search(r"^" + name + r" = (.*)$", src, re.M)
    return eval(m.group(1))

def decode(blob, index):
    raw = zlib.decompress(base64.b85decode(blob))
    out = []
    for start, length in index:
        pos = start
        n = raw[pos] | raw[pos + 1] << 8; pos += 2
        streams = []
        for _ in range(n):
            m = raw[pos] | raw[pos + 1] << 8; pos += 2
            ev = {}; last = 0
            for _ in range(m):
                d = raw[pos]; pos += 1
                if d == 255:
                    t = raw[pos] | raw[pos + 1] << 8; pos += 2
                else:
                    t = last + d
                ev[(t, raw[pos])] = raw[pos + 1]; pos += 2; last = t
            streams.append(ev)
        out.append(streams)
    return out

def encode(sections):
    blob = bytearray(); index = []
    for streams in sections:
        start = len(blob)
        blob += bytes([len(streams) & 0xFF, len(streams) >> 8])
        for ev in streams:
            items = sorted(ev.items())
            blob += bytes([len(items) & 0xFF, len(items) >> 8])
            last = 0
            for (t, i), q in items:
                d = t - last
                if 0 <= d <= 254:
                    blob.append(d)
                else:
                    blob.append(255); blob += bytes([t & 0xFF, t >> 8])
                blob += bytes([i & 0xFF, q & 0xFF]); last = t
        index.append((start, len(blob) - start))
    return bytes(blob), index

h = decode(get_var("subAA_harvest.py", "_V92_P_BLOB"), get_var("subAA_harvest.py", "_V92_P_INDEX"))
c = decode(get_var("subZ_C1R2.py", "_V92_P_BLOB"), get_var("subZ_C1R2.py", "_V92_P_INDEX"))
print("H streams:", sum(len(s) for s in h), " C1R2:", sum(len(s) for s in c))

merged = []; added = 0
for i, (hs, cs) in enumerate(zip(h, c)):
    have = {frozenset(ev.items()) for ev in hs}
    keep = [ev for ev in cs if frozenset(ev.items()) not in have]
    added += len(keep)
    merged.append(hs + keep)
print("added streams:", added, " new total:", sum(len(s) for s in merged))

blob, index = encode(merged)
enc = base64.b85encode(zlib.compress(blob, 9)).decode("ascii")

src = open("moe/r6/build/devin/harvest_m30_brx2.py").read()
src = re.sub(r"^_V92_P_BLOB = '.*'$", "_V92_P_BLOB = " + repr(enc), src, count=1, flags=re.M)
src = re.sub(r"^_V92_P_INDEX = \[.*\]$", "_V92_P_INDEX = " + repr(index), src, count=1, flags=re.M)
out = "moe/r6/build/devin/harvest_m30b_p324.py"
open(out, "w").write(src)

# verify roundtrip: decode the new file's blob, compare merged sections
chk = decode(get_var(out, "_V92_P_BLOB"), get_var(out, "_V92_P_INDEX"))
assert all(sorted(frozenset(e.items()) for e in a) == sorted(frozenset(e.items()) for e in b) for a, b in zip(chk, merged))
print("wrote", out, "roundtrip OK; size:", os.path.getsize(out))
