"""Assemble port/main.py from port/_head.py + the embedded tape blob + port/_tail.py.

Run with:  ./.venv/bin/python port/build_main.py
The blob is zlib+base85 of the exact space-separated text of the 1438 C string
literals in rivals/.../source/tape.inc (route 0 lines, "\\x00", route 1 lines).
"""
import base64
import os
import re
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
TAPE_INC = os.path.join(
    REPO, "rivals", "yhay81_the-35-0-tape-a-causal-shop-router", "source", "tape.inc")


def build_blob():
    src = open(TAPE_INC).read()
    assert "\\" not in src, "tape.inc contains escapes; naive extraction unsafe"
    strings = re.findall(r'"([^"]*)"', src)
    assert len(strings) == 1438, len(strings)
    raw = "\n".join(strings[:719]) + "\x00" + "\n".join(strings[719:])
    blob = base64.b85encode(zlib.compress(raw.encode("ascii"), 9)).decode("ascii")
    assert not (set('"\'\\') & set(blob))
    return blob


def main():
    blob = build_blob()
    width = 96
    chunks = [blob[i:i + width] for i in range(0, len(blob), width)]
    literal = ("\n# ---------------------------------------------------------"
               "-----------------\n"
               "# source/tape.inc -- zlib + base85 of the two 719-turn tapes\n"
               "# ---------------------------------------------------------"
               "-----------------\n"
               "_TAPE_B85 = (\n"
               + "\n".join('    "%s"' % c for c in chunks) + "\n)\n")
    head = open(os.path.join(HERE, "_head.py")).read()
    tail = open(os.path.join(HERE, "_tail.py")).read()
    out = head + literal + tail
    with open(os.path.join(HERE, "main.py"), "w") as fh:
        fh.write(out)
    print("wrote port/main.py: %d bytes, %d blob chunks" % (len(out), len(chunks)))


if __name__ == "__main__":
    main()
