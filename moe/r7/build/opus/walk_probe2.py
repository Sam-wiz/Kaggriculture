# Per-type: when job k is on current tile (d==0), P(unit moves away) and by hour band.
import json,sys,collections
MV={"NORTH","SOUTH","EAST","WEST"}
S=collections.Counter()
for l in open(sys.argv[1]):
    r=json.loads(l); d=r["d"]; mv=r["y"] in MV; h=r["G"]["hour"]
    for k in ["water","harvest","feed","care","cfert","dig"]:
        if k in d and d[k][0]==0 and (k!="feed" or r["inv"]["WHEAT"]>0):
            b="early" if h<12 else "late"
            S[(k,b,"n")]+=1; S[(k,b,"mv")]+=mv
    on=r.get("on",{})
    if on.get("plant") and on.get("watered") is False:
        S[("unwatered_plant","all","n")]+=1; S[("unwatered_plant","all","mv")]+=mv
for k in ["water","harvest","feed","care","cfert","dig","unwatered_plant"]:
    print(k, "  ".join("%s leave %.0f%% (n=%d)"%(b,100*S[(k,b,"mv")]/max(1,S[(k,b,"n")]),S[(k,b,"n")]) for b in ["early","late","all"] if S[(k,b,"n")]))
