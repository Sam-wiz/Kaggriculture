"""r5 opus an3: shop conditioning of the family macro.  For each macro quantity, fit
   M0 = team-pooled mean, M1 = linear in revealed-shop demand counts (per product), M2 = + dawn cash/empty
and report R^2 (5-fold by episode).  Demand count D_p = number of revealed shops demanding product p."""
import pickle, collections, numpy as np, json
D = pickle.load(open("moe/r5/build/opus/fam.pkl", "rb")); F = D["fam"]
DEM = {"BAKERY": ["EGG", "WHEAT"], "PIZZA_SHOP": ["MILK", "TOMATO", "WHEAT"], "BRUNCH_SPOT": ["EGG", "WHEAT", "STRAWBERRY"],
       "YARN_STORE": ["WOOL", "WOOL"], "ICE_CREAM_SHOP": ["STRAWBERRY", "MILK", "WHEAT"], "PET_CAFE": ["CARROT", "CARROT"],
       "SMOOTHIE_SHOP": ["STRAWBERRY", "MILK"], "FARMERS_MARKET": ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY"]}
PR = ["EGG", "MILK", "WOOL", "WHEAT", "TOMATO", "STRAWBERRY", "CARROT"]
def dem(shops):
    c = collections.Counter()
    for s in shops:
        for p in DEM.get(s, []): c[p] += 1
    return [c[p] for p in PR]
def r2(X, y, groups, k=5):
    X = np.c_[np.ones(len(y)), X]; pred = np.zeros(len(y)); g = np.array(groups) % k
    for f in range(k):
        tr, te = g != f, g == f
        b, *_ = np.linalg.lstsq(X[tr], y[tr], rcond=None); pred[te] = X[te] @ b
    return 1 - ((y - pred) ** 2).sum() / ((y - y.mean()) ** 2).sum(), np.linalg.lstsq(X, y, rcond=None)[0]
targets = {
  "cows_d12": lambda r: r["dawn"][12]["herd"].get("COW", 0), "sheep_d12": lambda r: r["dawn"][12]["herd"].get("SHEEP", 0),
  "geese_d12": lambda r: r["dawn"][12]["herd"].get("GOOSE", 0),
  "cows_d7": lambda r: r["dawn"][7]["herd"].get("COW", 0), "sheep_d7": lambda r: r["dawn"][7]["herd"].get("SHEEP", 0),
  "geese_d7": lambda r: r["dawn"][7]["herd"].get("GOOSE", 0),
  "tom_seed_d9_20": lambda r: sum(r["dec"][d]["seed"].get("TOMATO", 0) for d in range(9, 21)),
  "car_seed_d9_27": lambda r: sum(r["dec"][d]["seed"].get("CARROT", 0) for d in range(9, 28)),
  "str_seed_d6_15": lambda r: sum(r["dec"][d]["seed"].get("STRAWBERRY", 0) for d in range(6, 16)),
  "whe_seed_d6_27": lambda r: sum(r["dec"][d]["seed"].get("WHEAT", 0) for d in range(6, 28)),
  "str_plants_d18": lambda r: r["dawn"][18]["plants"].get("STRAWBERRY", 0), "tom_plants_d18": lambda r: r["dawn"][18]["plants"].get("TOMATO", 0),
  "car_plants_d24": lambda r: r["dawn"][24]["plants"].get("CARROT", 0), "whe_plants_d18": lambda r: r["dawn"][18]["plants"].get("WHEAT", 0),
}
# shops revealed by the decision time: herd d7 -> shops at dawn d6 (2); herd d12 -> dawn d11 (3); crops -> dawn d15 (5)
kshop = {"cows_d7": 6, "sheep_d7": 6, "geese_d7": 6, "cows_d12": 11, "sheep_d12": 11, "geese_d12": 11,
         "tom_seed_d9_20": 15, "car_seed_d9_27": 21, "str_seed_d6_15": 12, "whe_seed_d6_27": 18,
         "str_plants_d18": 12, "tom_plants_d18": 15, "car_plants_d24": 21, "whe_plants_d18": 15}
grp = [r["ep"] for r in F]
teams = sorted({r["team"] for r in F}); T = np.array([[r["team"] == t for t in teams[1:]] for r in F], float)
out = {}
print(f"{'target':16s} {'mean':>6s} {'sd':>5s}  R2(team) R2(team+shops) R2(+cash,empty)  coefs(shops: {PR})")
for name, fn in targets.items():
    y = np.array([fn(r) for r in F], float); dd = kshop[name]
    S = np.array([dem(r["dawn"][dd]["shops"]) for r in F], float)
    C = np.array([[r["dawn"][dd]["money"] / 1e4, r["dawn"][dd]["empty"]] for r in F], float)
    a, _ = r2(T, y, grp); b, cb = r2(np.c_[T, S], y, grp); c, _ = r2(np.c_[T, S, C], y, grp)
    co = cb[1 + T.shape[1]:]
    out[name] = dict(mean=y.mean(), r2_team=a, r2_shop=b, r2_cash=c, coef=dict(zip(PR, co.round(2).tolist())))
    print(f"{name:16s} {y.mean():6.1f} {y.std():5.1f}  {a:7.2f}  {b:7.2f}  {c:7.2f}   " + " ".join(f"{p[:3]}{v:+.2f}" for p, v in zip(PR, co)))
json.dump(out, open("moe/r5/build/opus/an3.json", "w"), indent=1)
