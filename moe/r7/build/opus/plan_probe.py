# Per-episode plan parameters vs episode covariates (shops seen, seat, prices at buy time)
import gzip,json,glob,sys,collections,statistics as st
TEAM=sys.argv[1]; R=[]
for f in sorted(glob.glob("mine/rawkeep/*.json.gz")):
    x=json.load(gzip.open(f,"rt"))
    if TEAM not in x["info"]["TeamNames"]: continue
    pi=x["info"]["TeamNames"].index(TEAM); S=x["steps"]
    bought=collections.Counter(); bdays=collections.defaultdict(list); land=[]; hires=collections.Counter()
    for t in range(1,len(S)):
        o=S[t-1][pi].get("observation") or {}; a=S[t][pi].get("action") or {}
        m=[q for q in (a.get("market") or []) if q]
        for q in m:
            if q[0]=="BUY_ANIMAL": bought[q[1]]+=q[2]; bdays[q[1]].append(o.get("day"))
            if q[0]=="BUY_LAND": land.append(o.get("day"))
            if q[0]=="HIRE": hires[o.get("day")]+=1
    shops=lambda d: tuple(sorted(S[min(d*24+1,len(S)-1)][pi]["observation"]["town"]["unlocked_shops"]))
    fin=S[-1][pi]["observation"]["farms"][pi]["money"] if "farms" in S[-1][pi]["observation"] else None
    R.append(dict(seat=pi,ep=x["info"]["EpisodeId"],G=bought["GOOSE"],C=bought["COW"],Sh=bought["SHEEP"],
        land=tuple(sorted(set(land))),h=sum(hires[d] for d in range(9,29))/20,s6=shops(6),s12=shops(12),rew=S[-1][pi].get("reward")))
for r in R[:50]: print(r["seat"],r["G"],r["C"],r["Sh"],r["land"],round(r["h"],1),r["s6"],r["s12"][:4],r["rew"])
print("---- event test")
def cnt(s,k): return sum(1 for z in s if z==k)
for r in R: r["y12"]=cnt(r["s12"],"YARN_STORE")
by=collections.defaultdict(list)
for r in R: by[r["y12"]].append(r["Sh"])
print("sheep bought by #YARN_STORE unlocked by d12:",{k:(len(v),st.mean(v),min(v),max(v)) for k,v in sorted(by.items())})
for r in R:
    first=None
    for d in range(3,30,3):
        pass
