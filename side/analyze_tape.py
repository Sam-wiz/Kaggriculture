"""Static analysis of the two 719-turn tapes + a live probe of h_over."""
import importlib.util, os, sys, collections
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); sys.modules[name] = m
    spec.loader.exec_module(m); return m

H = _load(os.path.join(REPO, "port2", "h_over.py"), "_hov")

for r, tape in enumerate(H._TAPES):
    plants = collections.Counter(); seedbuy = collections.Counter()
    hires_by_day = collections.Counter(); land = []
    orders_hist = collections.Counter()
    animals = collections.Counter()
    units_by_day = {}
    for s in range(H.K_TURNS):
        nu, units, no, orders = tape[s]
        d = s // 24
        units_by_day.setdefault(d, set()).add(nu)
        for i in range(nu):
            op, arg, n = units[i]
            if op == H.OP_PLANT: plants[H._ITEMS[arg]] += 1
        for i in range(no):
            op, it, n = orders[i]
            if op == H.M_HIRE: hires_by_day[d] += 1
            elif op == H.M_BUY_LAND: land.append(s)
            elif op == H.M_BUY_SEED: seedbuy[H._ITEMS[it]] += max(1, n)
            elif op == H.M_BUY_ANIMAL: animals[H._ITEMS[it]] += max(1, n)
        orders_hist[no] += 1
    print(f"=== route {r} ===")
    print(" plants:", dict(plants))
    print(" seedbuy:", dict(seedbuy))
    print(" animals:", dict(animals))
    print(" land buys at steps:", land, "days", [s//24 for s in land])
    print(" hires/day:", dict(sorted(hires_by_day.items())))
    print(" n_orders histogram:", dict(sorted(orders_hist.items())))
    print(" steps with n_orders>=10:", sum(v for k,v in orders_hist.items() if k>=10))
    print(" n_units per day:", {d: sorted(v) for d,v in sorted(units_by_day.items())})

# --- when may we append?  hire hours and full market-order steps ---
for r,tape in enumerate(H._TAPES):
    hire_hours=collections.Counter(); full=[]
    per_day_hire_hours={}
    for s in range(H.K_TURNS):
        nu,units,no,orders=tape[s]
        d,h=s//24,s%24
        nh=sum(1 for i in range(no) if orders[i][0]==H.M_HIRE)
        if nh: per_day_hire_hours.setdefault(d,[]).append((h,nh)); hire_hours[h]+=nh
        if no>=10: full.append((d,h,no))
    print(f"--- route {r} ---")
    print(" hires by hour:", dict(sorted(hire_hours.items())))
    print(" per-day hire schedule:", {d:v for d,v in sorted(per_day_hire_hours.items())})
    print(" full-slot steps (day,hour,n):", full)
