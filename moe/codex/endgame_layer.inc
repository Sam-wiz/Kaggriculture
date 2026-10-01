
# Lane A: same-turn endgame cash capture, isolated from sirx/L96 changes.
_EC_REPORT = dict(calls=0, active=0, changed_turns=0, premium_changed=0,
                  premium_orders=0, compact_changed=0, worker_calls=0,
                  worker_changed=0, care_targets_skipped=0, errors=0)
_EC_CHANGED_STEP = -1
_EC_STRICT = False
_ec_parent = agent
_ec_premium_parent = _rec_base
_ec_worker_parent = _v233_worker


def _ec_premium(observation, configuration=None):
    global _EC_CHANGED_STEP
    step = int(observation.get('step', 0))
    if step < 504:
        return _ec_premium_parent(observation, configuration)
    # Replace only the stock source used by the existing premium layer.
    # Reconciliation still runs afterwards, using the final emitted quantities.
    action = _prm_base(observation, configuration)
    try:
        orders = list(action.get('market') or [])
        if len(orders) >= _PRM_MAX:
            return action
        selling = {o[1] for o in orders if len(o) > 1 and o[0] == 'SELL'}
        prices = observation['market']['prices']
        projected = projected_shed(action, FarmView(observation))
        before = observation['private']['shed']
        additions = []
        old_additions = []
        for stock, target in ((projected, additions), (before, old_additions)):
            for item in _PRM_ORDER:
                if len(orders) + len(target) >= _PRM_MAX:
                    break
                if item in selling or prices.get(item, 0) < _PRM[item]:
                    continue
                qty = min(max(0, int(stock.get(item, 0))), _PRM_BATCH)
                if qty:
                    target.append(['SELL', item, qty])
        if additions != old_additions:
            _EC_REPORT['premium_changed'] += 1
            _EC_CHANGED_STEP = step
        if additions:
            _EC_REPORT['premium_orders'] += len(additions)
            _PRM_REPORT['orders_added'] += len(additions)
            _PRM_REPORT['units_added'] += sum(o[2] for o in additions)
            _PRM_REPORT['turns_active'] += 1
            action = dict(action, market=orders + additions)
    except Exception:
        _EC_REPORT['errors'] += 1
        if _EC_STRICT:
            raise
    return action


def _ec_worker_impl(observation, actor, targets):
    global _EC_CHANGED_STEP
    step = int(observation['step'])
    if step < 504:
        return _ec_worker_parent(observation, actor, targets)
    _EC_REPORT['worker_calls'] += 1
    day = step // 24
    player = int(observation['player'])
    farm = observation['farms'][player]
    tiles = farm['tiles']
    skip = []
    for x, y in targets:
        tile = tiles[y][x]
        if not isinstance(tile, dict) or tile.get('animal') != 'SHEEP' or tile.get('cared_today'):
            continue
        first = int(tile['placed_day']) + 6
        last_payout = first + ((29 - first) // 3) * 3
        # Refresh pays production before adding today's care to the bank.
        # Care on day last_payout-1 therefore cannot reach the last payout.
        if day + 1 >= last_payout:
            skip.append((x, y))
    if not skip:
        return _ec_worker_parent(observation, actor, targets)
    _EC_REPORT['care_targets_skipped'] += len(skip)
    # A private planning view marks unpayable CARE complete, so the existing
    # controller can fall through to HARVEST/COLLECT or move to its next target.
    # No engine observation, production, tile occupancy, or route is modified.
    rows = list(tiles)
    for y in {p[1] for p in skip}:
        rows[y] = list(rows[y])
    for x, y in skip:
        rows[y][x] = dict(rows[y][x], cared_today=True)
    farms = list(observation['farms'])
    farms[player] = dict(farm, tiles=rows)
    projected = dict(observation, farms=farms)
    # Both worker functions are decision-only, apart from diagnostic counters.
    # Preserve those counters while measuring the old decision on the same obs.
    reports = [(r, dict(r)) for r in (_SL_REPORT, _VT_REPORT)]
    original = _ec_worker_parent(observation, actor, targets)
    for report, snapshot in reports:
        report.clear()
        report.update(snapshot)
    result = _ec_worker_parent(projected, actor, targets)
    if result != original:
        _EC_REPORT['worker_changed'] += 1
        _EC_CHANGED_STEP = step
    return result


def _ec_worker(observation, actor, targets):
    try:
        return _ec_worker_impl(observation, actor, targets)
    except Exception:
        _EC_REPORT['errors'] += 1
        if _EC_STRICT:
            raise
        return _ec_worker_parent(observation, actor, targets)


def _ec_agent(observation, configuration=None):
    global _EC_CHANGED_STEP
    step = int(observation.get('step', 0))
    if step == 0:
        for key in _EC_REPORT:
            _EC_REPORT[key] = 0
        _EC_CHANGED_STEP = -1
    _EC_REPORT['calls'] += 1
    action = _ec_parent(observation, configuration)
    if step < 504:
        return action
    _EC_REPORT['active'] += 1
    try:
        orders = action.get('market') or []
        sells = [i for i, o in enumerate(orders)
                 if isinstance(o, (list, tuple)) and len(o) >= 3
                 and o[0] == 'SELL' and o[1] in _SIR_PARAMS]
        if sells:
            eligible = [i for i, o in enumerate(orders)
                        if i <= sells[-1] and (i in sells or o is None or o == [])]
            out = list(orders)
            for i in eligible:
                out[i] = []
            for i, old_index in zip(eligible, sells):
                out[i] = orders[old_index]
            if out != orders:
                _EC_REPORT['compact_changed'] += 1
                _EC_CHANGED_STEP = step
                action = dict(action, market=out)
    except Exception:
        _EC_REPORT['errors'] += 1
        if _EC_STRICT:
            raise
    if _EC_CHANGED_STEP == step:
        _EC_REPORT['changed_turns'] += 1
    return action


# Rebind the entry used by reconciliation, not the already-captured public name.
_rec_base = _ec_premium
if _EC_FIX_WORKERS:
    _v233_worker = _ec_worker
_ec_agent.telemetry = _EC_REPORT
del agent
agent = _ec_agent
