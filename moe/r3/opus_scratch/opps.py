import json, gzip
rows=json.load(open('/tmp/opus_r3/rows.json'))
def unitops(a):
    if not isinstance(a,dict): return None
    return json.dumps([a.get('farmer'), a.get('hands')])
out=[]
for r in sorted(rows,key=lambda r:-(r['R'] or 0)):
    if (r['R'] or 0)<2100: continue
    d=json.load(gzip.open(r['path'],'rt')); A=d['actions']; me=r['seat']; op=1-me
    n=len(A); same=sum(1 for t in range(1,n) if unitops(A[t][me])==unitops(A[t][op]))
    mk=sum(1 for t in range(1,n) if isinstance(A[t][op],dict) and json.dumps(A[t][op].get('market'))==json.dumps(A[t][me].get('market') if isinstance(A[t][me],dict) else None))
    o1=json.dumps(A[1][op].get('market') if isinstance(A[1][op],dict) else None)[:70]
    r2=dict(r); r2.update(uid=round(same/(n-1),2), mid=round(mk/(n-1),2), open=o1); out.append(r2)
    print(f"{r['build'][:4]} R={r['R']:.0f} {r['opp'][:22]:22} m={r['m']:+7.0f} seat={me} unit_id={same/(n-1):.2f} mkt_id={mk/(n-1):.2f} {o1}")
json.dump(out,open('/tmp/opus_r3/opps.json','w'))
