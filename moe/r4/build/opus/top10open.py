"""Scan mine/top10 dumps: do C1's 8 band opponents appear, and how often does any top seat open WLV (5,0)?"""
import gzip, json, os, collections
os.chdir("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture")
names = {"Clement Lau","Fanch","kazuhiro3381","tamref","Juste Me","我的AI是豆包","hinemos","SatoGo"}
WLV = [["BUY_PRODUCT","WHEAT",5],["BUY_SEED","WHEAT",1]]
hit = collections.Counter(); opens = collections.Counter(); wlv_teams = collections.Counter(); n = 0
for f in os.listdir("mine/top10"):
    if not f.endswith(".gz"): continue
    try: d = json.load(gzip.open("mine/top10/" + f, "rt"))
    except Exception: continue
    n += 1
    for s, t in enumerate(d["teams"]):
        if t in names: hit[t] += 1
        a = d["actions"][1][s]; m = a.get("market") if isinstance(a, dict) else None
        k = json.dumps(m)[:60]; opens[k] += 1
        if m == WLV: wlv_teams[t] += 1
print("files", n, "hits", dict(hit))
print("WLV-opening seats by team", wlv_teams.most_common(10))
for k, v in opens.most_common(8): print(v, k)
