"""Does C1's V219 route-level disqualifier (all chassis routes, steps 432-718: no BUY_LAND, no PLANT TOMATO) ever pass?"""
import sys; sys.path.insert(0, "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus")
from run import load
a, m = load("subY_C1_predict2.py", "s")
R = m._IMPL.chassis.routes
land = [k for k, t in R.items() if any(any(o and o[0] == 'BUY_LAND' for o in a.get('market', [])) for a in t[432:719])]
tom = [k for k, t in R.items() if any(any(c == ['PLANT', 'TOMATO'] for c in [a.get('farmer')] + a.get('hands', [])) for a in t[432:719])]
se = [k for k, t in R.items() if sum(any(o and o[0] == 'BUY_LAND' for o in a.get('market', [])) for a in t) >= 3]
print("routes", len(R), "late_land", len(land), "late_tomato", len(tom), "buys3lands", len(se))
print("sample late_land", land[:5], "late_tomato", tom[:5])
