import json, gzip, sys
from collections import Counter
def norm(m):
    out=[]
    for o in m or []:
        if isinstance(o,(list,tuple)) and o: out.append(tuple(o))
    return out
def sells(m):
    c=Counter()
    for o in m:
        if o[0]=="SELL" and len(o)>=3: c[o[1]]+=o[2]
    return c
for e in sys.argv[1:]:
    d = json.load(gzip.open(f"mine/opp/{e}.json.gz","rt"))
    t=d["teams"]; me=t.index("Sam-wiz"); op=1-me
    A=d["actions"]
    print(f"\n#### {e} {t[op]} seat={me} rewards ours={d['rewards'][me]} theirs={d['rewards'][op]}")
    ndiff=0; cat=Counter(); sellmore=Counter(); firstdiff=None; nonsell_kinds=Counter()
    for s,x in enumerate(A):
        a=x[me] or {}; b=x[op] or {}
        ma=norm(a.get("market")); mb=norm(b.get("market"))
        if ma!=mb:
            ndiff+=1
            if firstdiff is None: firstdiff=s
            sa=sells(ma); sb=sells(mb)
            for p in set(sa)|set(sb):
                if sb[p]>sa[p]: sellmore[p+"_they"]+=sb[p]-sa[p]
                elif sa[p]>sb[p]: sellmore[p+"_us"]+=sa[p]-sb[p]
            na=[o for o in ma if o[0]!="SELL"]; nb=[o for o in mb if o[0]!="SELL"]
            if na!=nb:
                cat["nonsell"]+=1
                for o in set(na)^set(nb): nonsell_kinds[o[0]]+=1
            if sa!=sb: cat["sellqty"]+=1
            elif [o for o in ma if o[0]=="SELL"]!=[o for o in mb if o[0]=="SELL"]: cat["sellorder_only"]+=1
            if s<30 or (s%48==0):
                print(f"  s={s} d={s//24} h={s%24}\n     OURS={ma}\n     THEY={mb}")
    print("  market-diff turns", ndiff, "first", firstdiff, dict(cat), dict(nonsell_kinds))
    print("  sell-more units:", dict(sellmore))
