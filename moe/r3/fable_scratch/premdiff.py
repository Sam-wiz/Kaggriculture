import json, gzip, sys
PREM=("MILK","WOOL","STRAWBERRY")
def norm(m): return [tuple(o) for o in (m or []) if isinstance(o,(list,tuple)) and o]
for e in sys.argv[1:]:
    d=json.load(gzip.open(f"mine/opp/{e}.json.gz","rt")); t=d["teams"]; me=t.index("Sam-wiz"); op=1-me; A=d["actions"]
    print(f"\n#### {e} {t[op]} seat={me} m={d['rewards'][me]-d['rewards'][op]:+.0f}")
    shown=0
    for s,x in enumerate(A):
        ma=[o for o in norm((x[me] or {}).get("market")) if o[0]=="SELL" and o[1] in PREM]
        mb=[o for o in norm((x[op] or {}).get("market")) if o[0]=="SELL" and o[1] in PREM]
        if ma!=mb and 140<=s<=260:
            print(f"  s={s:3d} d{s//24}h{s%24:2d} OURS={ma}  THEY={mb}")
            shown+=1
            if shown>=14: break
