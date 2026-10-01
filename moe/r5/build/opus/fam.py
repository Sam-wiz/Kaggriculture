"""r5 opus: compact family-seat table from macro.jsonl -> fam.pkl (list of dicts), used by the analyses."""
import json, pickle, sys
FAM = {"Vadim Vasilenko", "DECEM", "Unknown Mother-Goose", "DSM", "mtmr_s1", "M & M & P & Q"}
OPEN = [["BUY_ANIMAL", "COW", 1], ["BUY_PRODUCT", "WHEAT", 5]]
rows, other = [], []
for l in open("moe/r5/build/opus/macro.jsonl"):
    d = json.loads(l)
    for s, se in enumerate(d["seats"]):
        r = dict(ep=d["ep"], date=d["date"], seed=d["seed"], seat=s, team=se["team"], opp=d["teams"][1 - s],
                 bank=se["bank"], obank=d["rewards"][1 - s], shops=d["shops"], op1=d["op1"][s],
                 dawn=[{k: v for k, v in w.items() if k not in ("map", "inv")} for w in se["dawn"]],
                 maps={k: se["dawn"][k]["map"] for k in (3, 6, 10, 12, 15, 18, 21, 24, 27)},
                 dec=se["dec"], prod=se["prod"], discard=se["discard"])
        r["fam"] = se["team"] in FAM and (d["op1"][s] or [])[:2] == OPEN
        (rows if r["fam"] else other).append(r)
pickle.dump(dict(fam=rows, other=other), open("moe/r5/build/opus/fam.pkl", "wb"))
print(len(rows), "family seats;", len(other), "other seats")
