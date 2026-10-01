"""Build router specs from a team index (tfc_index.json format). usage: mkspec.py INDEX OUTPREFIX"""
import json, collections, sys
recs = json.load(open(sys.argv[1])); outp = sys.argv[2]
modal = collections.Counter(r['hfull'] for r in recs).most_common(1)[0][0]
modu = collections.Counter(r['hunit'] for r in recs).most_common(1)[0][0]
pre = max((r for r in recs if r['hfull'] == modal), key=lambda r: r['bank'])
bp = collections.defaultdict(list)
for r in recs: bp["|".join(r['pair'])].append(r)
def pick(c, key):
    for f in (lambda x: x['hfull'] == modal, lambda x: x['hunit'] == modu, lambda x: True):
        cc = [x for x in c if f(x)]
        if cc: return max(cc, key=lambda x: x[key])
for key in ('bank', 'margin'):
    spec = dict(prefix=[pre['p'], pre['s']], default=[pre['p'], pre['s']], switch=144,
                routes={k: [pick(v, key)['p'], pick(v, key)['s']] for k, v in bp.items()})
    json.dump(spec, open(f"{outp}_{key}.json", "w"))
json.dump(dict(prefix=[pre['p'], pre['s']], default=[pre['p'], pre['s']], switch=144, routes={}), open(f"{outp}_single.json", "w"))
print("prefix", pre['p'], pre['s'], "bank", pre['bank'], "pairs", len(bp))
