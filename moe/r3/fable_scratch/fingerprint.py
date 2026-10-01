import json, gzip
from collections import Counter, defaultdict
rows=json.load(open("/tmp/fable/live_rows.json"))
def norm(m):
    return [tuple(o) for o in (m or []) if isinstance(o,(list,tuple)) and o]
def sells(m):
    c=Counter()
    for o in m:
        if o[0]=="SELL" and len(o)>=3 and isinstance(o[2],(int,float)): c[o[1]]+=o[2]
    return c
PREM=("MILK","WOOL","STRAWBERRY","MELON")
out=[]
for r in rows:
    d=json.load(gzip.open(f"mine/opp/{r['ep']}.json.gz","rt")); me=r["seat"]; op=1-me; A=d["actions"]
    # step-1 opening
    def opening(x):
        m=norm((x or {}).get("market")); b=sum(o[2] for o in m if o[0]=="BUY_PRODUCT" and o[1]=="WHEAT"); s=sum(o[2] for o in m if o[0]=="SELL" and o[1]=="WHEAT" and len(o)>=3); return (b,s)
    oo=opening(A[1][me]); ot=opening(A[1][op])
    ndiff=0; prem_they=0; prem_us=0; nonsell=0; first_prem_diff=None
    tot_they=Counter(); tot_us=Counter()
    for s,x in enumerate(A):
        ma=norm((x[me] or {}).get("market")); mb=norm((x[op] or {}).get("market"))
        sa=sells(ma); sb=sells(mb); tot_us.update(sa); tot_they.update(sb)
        if ma!=mb:
            ndiff+=1
            if [o for o in ma if o[0]!="SELL"]!=[o for o in mb if o[0]!="SELL"]: nonsell+=1
            for p in PREM:
                if sb[p]>sa[p]: prem_they+=sb[p]-sa[p]
                if sa[p]>sb[p]: prem_us+=sa[p]-sb[p]
                if sa[p]!=sb[p] and first_prem_diff is None: first_prem_diff=s
    r2=dict(r); r2.pop("opening",None)
    r2.update(open_us=oo, open_they=ot, ndiff=ndiff, nonsell=nonsell, prem_they=prem_they, prem_us=prem_us, first_prem_diff=first_prem_diff,
              tot_prem_us=sum(tot_us[p] for p in PREM), tot_prem_they=sum(tot_they[p] for p in PREM), tot_us=dict(tot_us), tot_they=dict(tot_they))
    out.append(r2)
json.dump(out,open("/tmp/fable/live_rows2.json","w"))
for b in ["shepherd","hyb2965"]:
    print(f"\n=== {b}: mirror games (same_u>=0.95), R>=2000")
    print(" ep        opp                  R   seat  m     opn_us  opn_they ndiff nonsell prem_they prem_us 1stPremDiff totprem us/they")
    for r in sorted([r for r in out if r["build"]==b and r["same_u"]>=0.95 and (r["R"] or 0)>=2000], key=lambda r:-r["R"]):
        print(f" {r['ep']} {r['opp'][:20]:20s} {r['R']:.0f} {r['seat']} {r['margin']:+6.0f} {str(r['open_us']):8s} {str(r['open_they']):8s} {r['ndiff']:4d} {r['nonsell']:4d} {r['prem_they']:5d} {r['prem_us']:5d} {str(r['first_prem_diff']):5s} {r['tot_prem_us']}/{r['tot_prem_they']}")
# opening distribution by result among mirrors
print("\nopening(they) vs W/L among shepherd mirrors >=2000:")
c=defaultdict(lambda:[0,0])
for r in out:
    if r["build"]=="shepherd" and r["same_u"]>=0.95 and (r["R"] or 0)>=2000:
        c[str(r["open_they"])][0 if r["margin"]>0 else 1]+=1
for k,v in sorted(c.items()): print("  ",k,"W/L",v)
