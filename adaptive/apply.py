"""Bake a params JSON into an agent's module-level P dict.

The tuned values must live in the file itself: Kaggle execs the source with no
way to pass overrides, so a params file that only tune.py knows about would ship
a differently-behaved agent than the one that was measured.
"""
import json
import re
import sys


def bake(path, params, out=None):
    src = open(path).read()
    for k, v in params.items():
        lit = json.dumps(v).replace('"', '"')
        # match `    key=<anything up to a comma at end of the entry>,`
        pat = re.compile(r"(\n    %s=)(?:\{[^}]*\}|\[[^\]]*\]|[^,\n]*)(,)" % re.escape(k))
        new, n = pat.subn(lambda m: m.group(1) + lit + m.group(2), src, count=1)
        if n != 1:
            raise SystemExit("could not bake %r (matched %d times)" % (k, n))
        src = new
    open(out or path, "w").write(src)
    print("baked %d params into %s" % (len(params), out or path))


if __name__ == "__main__":
    bake(sys.argv[1], json.load(open(sys.argv[2])),
         sys.argv[3] if len(sys.argv) > 3 else None)
