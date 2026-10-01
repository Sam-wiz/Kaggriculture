"""Read-only controller probes on expert states, not closed-loop performance tests."""
import collections, copy, gzip, hashlib, json, os, pathlib, runpy, sys
try:
    os.nice(10)
except PermissionError:
    pass  # Sandbox prohibits changing process niceness.
ROOT = pathlib.Path(__file__).resolve().parents[4]
p = ROOT/'moe/r7/build/devin/clone_bc.py'
src = p.read_text()
lines = src.splitlines()
coverage_line = next(i+1 for i,s in enumerate(lines) if s.strip() == 'i=best[1]; po=units[i]')
plant_line = next(i+1 for i,s in enumerate(lines) if s.strip().startswith('want_crops='))
ns = runpy.run_path(str(p))
raw = json.load(gzip.open(ROOT/'mine/rawkeep/109709272.json.gz', 'rt'))
pi = raw['info']['TeamNames'].index('DSM')
counts = collections.Counter()
examples = collections.defaultdict(list)
for t in range(144):
    ob = copy.deepcopy(raw['steps'][t][pi]['observation'])
    ob['player'] = pi
    ob['step'] = t
    # Independent snapshot probes: do not carry intentions between expert states.
    ns['_ST']['assign'] = {}
    ns['_ST']['step'] = -1
    selected = []
    before = {}
    def trace(frame, event, arg):
        if frame.f_code is not ns['agent'].__code__: return None
        if event == 'line':
            loc = frame.f_locals
            if frame.f_lineno == coverage_line:
                selected.append((loc['best'][1],loc['cl'],loc['x'],loc['y']))
            elif frame.f_lineno == plant_line:
                before['assign'] = copy.deepcopy(loc['assign'])
                before['ops'] = copy.deepcopy(loc['ops_out'])
                before['claimed'] = sorted(loc['claimed_tiles'])
        return trace
    sys.settrace(trace)
    try:
        result = ns['agent'](ob)
    except Exception as exc:
        counts['exceptions'] += 1
        examples['exceptions'].append([t,repr(exc)])
        continue
    finally:
        sys.settrace(None)
    counts['states'] += 1
    counts['coverage_assignments'] += len(selected)
    if len({r[0] for r in selected}) < len(selected):
        counts['states_reusing_unit_in_coverage'] += 1
        if len(examples['coverage_reuse']) < 3:
            examples['coverage_reuse'].append({'t':t,'selected':selected,'surviving_assign':before['assign']})
    after_ops = [result['farmer']]+result['hands']
    changed = []
    for ui, intent in before.get('assign',{}).items():
        if intent[0] not in ('WATER','FEED'): continue
        if before['ops'][ui] == after_ops[ui]: continue
        if ns['_ST']['assign'].get(ui) == intent: continue
        changed.append({'ui':ui,'intent_before':intent,'op_before':before['ops'][ui],
                        'intent_after':ns['_ST']['assign'].get(ui),'op_after':after_ops[ui]})
    if changed:
        counts['states_planting_overrides_survival'] += 1
        counts['survival_overrides'] += len(changed)
        if len(examples['planting_override']) < 3:
            examples['planting_override'].append({'t':t,'changes':changed})
report = {'scope':'144 independent expert-state probes; no games, no held-out performance claim',
          'episode':raw['info'],'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
          'lines':{'coverage_selection':coverage_line,'planting_floor':plant_line},
          'counts':dict(counts),'examples':dict(examples)}
out = ROOT/'moe/r7/build/astra/bc_arbitration_audit.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
