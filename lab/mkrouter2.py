"""sub_router2.py = public-state router, milk branch retired, plus price-impact slot ordering.

Two changes on top of thomastschinkel's agent, both measured on a 320-cell panel (20 seeds x 8
current-meta opponents x both seats), each tail run to completion so every cell has all four
outcomes:

 1. DROP THE MILK_GLUT DECISION. On this panel the branch fires 122/320 times but is the best of
    the four tails only 55 times, and the margin curve in its threshold is *monotone*: +12,894 at
    threshold 0, +14,949 at the published 10067, +15,148 once it can never fire. A monotone curve
    is evidence, where a grid-search peak would just be overfitting. Worth +199.
    The likely reason it was fitted the other way: the author's 968-game panel replays *recorded*
    routes, and a milk glut against a fixed tape means something different than against an agent
    that reacts to the same market.

 2. PRICE-IMPACT SLOT ORDERING. Orders settle slot-by-slot against the opponent's slot of the same
    index and every unit moves the shared price, so conceding the first slot on a thin product
    costs qty x (price_now - price_after_burst). The router clamps and dumps but never reorders.
    Worth +68/game, positive against 8 of 9 pool opponents.

Left alone deliberately: the px_CARROT threshold. Its best value on the panel is 38 (+142 over 42)
but the curve is not monotone and the plateau is flat from 38 to 45, so that is a fit to noise.
"""
import os

src = open("sub_router.py").read()

OLD = '''DECISIONS = (
    (226, "shop_YARN_STORE", 1, YARN),
    (360, "px_CARROT", 42, YARN_CARROT),
    (433, "inv_MILK", 10067, MILK_GLUT),
)'''
NEW = '''DECISIONS = (
    (226, "shop_YARN_STORE", 1, YARN),
    (360, "px_CARROT", 42, YARN_CARROT),
    # (433, "inv_MILK", 10067, MILK_GLUT) retired -- see module docstring: on a 320-cell panel of
    # live opponents this branch fires 122 times and is the best tail only 55, and the margin is
    # monotone increasing in its threshold, peaking where it never fires (+199).
)'''
assert OLD in src, "DECISIONS block not found"
src = src.replace(OLD, NEW)

OVERLAY = open("sub_router_slot.py").read()
tail = OVERLAY.split("# OVERLAY: price-impact slot ordering", 1)[1]
src = src + "\n\n# ---------------------------------------------------------------------------\n" \
            "# OVERLAY: price-impact slot ordering" + tail

open("sub_router2.py", "w").write(src)
print("wrote sub_router2.py", os.path.getsize("sub_router2.py"), "bytes")
