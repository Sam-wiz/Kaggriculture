"""Decode / encode the _V92_P_BLOB + _V92_P_INDEX PREDICT library (64 shop-pair buckets)."""
import re, zlib, base64
NAMES = ['BAKERY', 'BRUNCH_SPOT', 'FARMERS_MARKET', 'ICE_CREAM_SHOP', 'PET_CAFE', 'PIZZA_SHOP', 'SMOOTHIE_SHOP', 'YARN_STORE']
def read_src(path):
    src = open(path).read()
    blob = re.search(r"^_V92_P_BLOB = '([^']*)'$", src, re.M).group(1)
    index = eval(re.search(r"^_V92_P_INDEX = (\[.*\])$", src, re.M).group(1))
    return src, blob, index
def decode(blob, index):
    raw = zlib.decompress(base64.b85decode(blob)); lib = []
    for start, length in index:
        pos = start; n = raw[pos] | raw[pos+1] << 8; pos += 2; out = []
        for _ in range(n):
            m = raw[pos] | raw[pos+1] << 8; pos += 2; ev = {}; last = 0
            for _ in range(m):
                d = raw[pos]; pos += 1
                if d == 255: t = raw[pos] | raw[pos+1] << 8; pos += 2
                else: t = last + d
                ev[(t, raw[pos])] = raw[pos+1]; pos += 2; last = t
            out.append(ev)
        lib.append(out)
    return lib
def encode(lib):
    raw = bytearray(); index = []
    for streams in lib:
        start = len(raw); raw += bytes([len(streams) & 255, len(streams) >> 8])
        for ev in streams:
            items = sorted(ev.items()); raw += bytes([len(items) & 255, len(items) >> 8]); last = 0
            for (t, i), q in items:
                d = t - last
                if 0 <= d < 255: raw.append(d)
                else: raw += bytes([255, t & 255, t >> 8])
                raw += bytes([i, min(255, max(0, int(q)))]); last = t
        index.append((start, len(raw) - start))
    return base64.b85encode(zlib.compress(bytes(raw), 9)).decode(), index
def pair_index(shops):
    return NAMES.index(shops[0]) * 8 + NAMES.index(shops[1])
def write_src(src, blob, index, path, extra_subs=()):
    s = re.sub(r"^_V92_P_BLOB = '[^']*'$", lambda m: "_V92_P_BLOB = '%s'" % blob, src, count=1, flags=re.M)
    s = re.sub(r"^_V92_P_INDEX = \[.*\]$", lambda m: "_V92_P_INDEX = %r" % (index,), s, count=1, flags=re.M)
    for a, b in extra_subs:
        assert s.count(a) == 1, a; s = s.replace(a, b)
    open(path, "w").write(s)
if __name__ == "__main__":
    import sys, collections
    for p in sys.argv[1:]:
        src, blob, index = read_src(p); lib = decode(blob, index)
        b2, i2 = encode(lib); assert decode(b2, i2) == lib
        n = [len(x) for x in lib]; items = collections.Counter(i for x in lib for ev in x for (t, i) in ev)
        ts = [t for x in lib for ev in x for (t, i) in ev]; qs = collections.Counter(min(q,20)//5*5 for x in lib for ev in x for q in ev.values())
        evn = [len(ev) for x in lib for ev in x]
        print(p, "streams", sum(n), "per-pair min/med/max", min(n), sorted(n)[32], max(n), "items", dict(items), "t", min(ts), max(ts), "ev/stream med", sorted(evn)[len(evn)//2], "qty bins", dict(qs), "roundtrip ok")
