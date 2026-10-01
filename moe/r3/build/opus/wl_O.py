# Kaggriculture submission v9/3: public V39 (Apache-2.0, notices below) plus the v9 layers
# RACEPX gate, RACE (reservation from step 192, horizon 40 / margin 12), COURIER, CARROT and HERD
# appended at the end of this file.
# EXP-173 isolate opening market sequence inspired by yhay81/shop-router-0911-simple (Apache-2.0).
# Kaggriculture EXP-167 candidate. Not submitted automatically.
# Attribution: thomastschinkel, yhay81, destbreso, aurax7, tetsutani,
# prvsiyan and Dmitrii Gluzdov. Apache-2.0 derivations; notices retained below.
# Kaggriculture v31 / EXP-157, Ahmed Berat Ozer, September 9 2026.
# Selected mechanism: crop_public_order. New independent confirmation is required.
# Public V221B/V224C production/timing lineage: prvsiyan, Apache-2.0.
# Original economics and integration; retained upstream licenses follow.
# Kaggriculture v28 / EXP-154, Ahmed Berat Ozer, September 9 2026.
# Changes: aurax7 day-end storage guard; Dmitrii Gluzdov physical terminal rescue
# adapted to v27, with 64 deterministic simulations. Apache-2.0.
# New action tapes and ordered shop-pair map: yhay81/shop-router-0909, Apache-2.0.
# Kaggriculture v25, EXP-149: Shop0908 production, sale lead, terminal cargo rescue.
# Runtime chassis: Apache-2.0; thomastschinkel, yhay81, tetsutani.
# Routing and public action data: yhay81/shop-router-0908, frozen September 8, 2026.
# 
#                                  Apache License
#                            Version 2.0, January 2004
#                         http://www.apache.org/licenses/
# 
#    TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
# 
#    1. Definitions.
# 
#       "License" shall mean the terms and conditions for use, reproduction,
#       and distribution as defined by Sections 1 through 9 of this document.
# 
#       "Licensor" shall mean the copyright owner or entity authorized by
#       the copyright owner that is granting the License.
# 
#       "Legal Entity" shall mean the union of the acting entity and all
#       other entities that control, are controlled by, or are under common
#       control with that entity. For the purposes of this definition,
#       "control" means (i) the power, direct or indirect, to cause the
#       direction or management of such entity, whether by contract or
#       otherwise, or (ii) ownership of fifty percent (50%) or more of the
#       outstanding shares, or (iii) beneficial ownership of such entity.
# 
#       "You" (or "Your") shall mean an individual or Legal Entity
#       exercising permissions granted by this License.
# 
#       "Source" form shall mean the preferred form for making modifications,
#       including but not limited to software source code, documentation
#       source, and configuration files.
# 
#       "Object" form shall mean any form resulting from mechanical
#       transformation or translation of a Source form, including but
#       not limited to compiled object code, generated documentation,
#       and conversions to other media types.
# 
#       "Work" shall mean the work of authorship, whether in Source or
#       Object form, made available under the License, as indicated by a
#       copyright notice that is included in or attached to the work
#       (an example is provided in the Appendix below).
# 
#       "Derivative Works" shall mean any work, whether in Source or Object
#       form, that is based on (or derived from) the Work and for which the
#       editorial revisions, annotations, elaborations, or other modifications
#       represent, as a whole, an original work of authorship. For the purposes
#       of this License, Derivative Works shall not include works that remain
#       separable from, or merely link (or bind by name) to the interfaces of,
#       the Work and Derivative Works thereof.
# 
#       "Contribution" shall mean any work of authorship, including
#       the original version of the Work and any modifications or additions
#       to that Work or Derivative Works thereof, that is intentionally
#       submitted to Licensor for inclusion in the Work by the copyright owner
#       or by an individual or Legal Entity authorized to submit on behalf of
#       the copyright owner. For the purposes of this definition, "submitted"
#       means any form of electronic, verbal, or written communication sent
#       to the Licensor or its representatives, including but not limited to
#       communication on electronic mailing lists, source code control systems,
#       and issue tracking systems that are managed by, or on behalf of, the
#       Licensor for the purpose of discussing and improving the Work, but
#       excluding communication that is conspicuously marked or otherwise
#       designated in writing by the copyright owner as "Not a Contribution."
# 
#       "Contributor" shall mean Licensor and any individual or Legal Entity
#       on behalf of whom a Contribution has been received by Licensor and
#       subsequently incorporated within the Work.
# 
#    2. Grant of Copyright License. Subject to the terms and conditions of
#       this License, each Contributor hereby grants to You a perpetual,
#       worldwide, non-exclusive, no-charge, royalty-free, irrevocable
#       copyright license to reproduce, prepare Derivative Works of,
#       publicly display, publicly perform, sublicense, and distribute the
#       Work and such Derivative Works in Source or Object form.
# 
#    3. Grant of Patent License. Subject to the terms and conditions of
#       this License, each Contributor hereby grants to You a perpetual,
#       worldwide, non-exclusive, no-charge, royalty-free, irrevocable
#       (except as stated in this section) patent license to make, have made,
#       use, offer to sell, sell, import, and otherwise transfer the Work,
#       where such license applies only to those patent claims licensable
#       by such Contributor that are necessarily infringed by their
#       Contribution(s) alone or by combination of their Contribution(s)
#       with the Work to which such Contribution(s) was submitted. If You
#       institute patent litigation against any entity (including a
#       cross-claim or counterclaim in a lawsuit) alleging that the Work
#       or a Contribution incorporated within the Work constitutes direct
#       or contributory patent infringement, then any patent licenses
#       granted to You under this License for that Work shall terminate
#       as of the date such litigation is filed.
# 
#    4. Redistribution. You may reproduce and distribute copies of the
#       Work or Derivative Works thereof in any medium, with or without
#       modifications, and in Source or Object form, provided that You
#       meet the following conditions:
# 
#       (a) You must give any other recipients of the Work or
#           Derivative Works a copy of this License; and
# 
#       (b) You must cause any modified files to carry prominent notices
#           stating that You changed the files; and
# 
#       (c) You must retain, in the Source form of any Derivative Works
#           that You distribute, all copyright, patent, trademark, and
#           attribution notices from the Source form of the Work,
#           excluding those notices that do not pertain to any part of
#           the Derivative Works; and
# 
#       (d) If the Work includes a "NOTICE" text file as part of its
#           distribution, then any Derivative Works that You distribute must
#           include a readable copy of the attribution notices contained
#           within such NOTICE file, excluding those notices that do not
#           pertain to any part of the Derivative Works, in at least one
#           of the following places: within a NOTICE text file distributed
#           as part of the Derivative Works; within the Source form or
#           documentation, if provided along with the Derivative Works; or,
#           within a display generated by the Derivative Works, if and
#           wherever such third-party notices normally appear. The contents
#           of the NOTICE file are for informational purposes only and
#           do not modify the License. You may add Your own attribution
#           notices within Derivative Works that You distribute, alongside
#           or as an addendum to the NOTICE text from the Work, provided
#           that such additional attribution notices cannot be construed
#           as modifying the License.
# 
#       You may add Your own copyright statement to Your modifications and
#       may provide additional or different license terms and conditions
#       for use, reproduction, or distribution of Your modifications, or
#       for any such Derivative Works as a whole, provided Your use,
#       reproduction, and distribution of the Work otherwise complies with
#       the conditions stated in this License.
# 
#    5. Submission of Contributions. Unless You explicitly state otherwise,
#       any Contribution intentionally submitted for inclusion in the Work
#       by You to the Licensor shall be under the terms and conditions of
#       this License, without any additional terms or conditions.
#       Notwithstanding the above, nothing herein shall supersede or modify
#       the terms of any separate license agreement you may have executed
#       with Licensor regarding such Contributions.
# 
#    6. Trademarks. This License does not grant permission to use the trade
#       names, trademarks, service marks, or product names of the Licensor,
#       except as required for reasonable and customary use in describing the
#       origin of the Work and reproducing the content of the NOTICE file.
# 
#    7. Disclaimer of Warranty. Unless required by applicable law or
#       agreed to in writing, Licensor provides the Work (and each
#       Contributor provides its Contributions) on an "AS IS" BASIS,
#       WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
#       implied, including, without limitation, any warranties or conditions
#       of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
#       PARTICULAR PURPOSE. You are solely responsible for determining the
#       appropriateness of using or redistributing the Work and assume any
#       risks associated with Your exercise of permissions under this License.
# 
#    8. Limitation of Liability. In no event and under no legal theory,
#       whether in tort (including negligence), contract, or otherwise,
#       unless required by applicable law (such as deliberate and grossly
#       negligent acts) or agreed to in writing, shall any Contributor be
#       liable to You for damages, including any direct, indirect, special,
#       incidental, or consequential damages of any character arising as a
#       result of this License or out of the use or inability to use the
#       Work (including but not limited to damages for loss of goodwill,
#       work stoppage, computer failure or malfunction, or any and all
#       other commercial damages or losses), even if such Contributor
#       has been advised of the possibility of such damages.
# 
#    9. Accepting Warranty or Additional Liability. While redistributing
#       the Work or Derivative Works thereof, You may choose to offer,
#       and charge a fee for, acceptance of support, warranty, indemnity,
#       or other liability obligations and/or rights consistent with this
#       License. However, in accepting such obligations, You may act only
#       on Your own behalf and on Your sole responsibility, not on behalf
#       of any other Contributor, and only if You agree to indemnify,
#       defend, and hold each Contributor harmless for any liability
#       incurred by, or claims asserted against, such Contributor by reason
#       of your accepting any such warranty or additional liability.
# 
#    END OF TERMS AND CONDITIONS
# 
#    APPENDIX: How to apply the Apache License to your work.
# 
#       To apply the Apache License to your work, attach the following
#       boilerplate notice, with the fields enclosed by brackets "[]"
#       replaced with your own identifying information. (Don't include
#       the brackets!)  The text should be enclosed in the appropriate
#       comment syntax for the file format. We also recommend that a
#       file or class name and description of purpose be included on the
#       same "printed page" as the copyright notice for easier
#       identification within third-party archives.
# 
#    Copyright [yyyy] [name of copyright owner]
# 
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
# 
#        http://www.apache.org/licenses/LICENSE-2.0
# 
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
"""Kaggriculture route-replay chassis (pure Python, stdlib only).

A *route* is a pre-computed tape of 719 Kaggle-format actions
``{"farmer": [op, ...], "hands": [[op, ...], ...], "market": [[order, item, qty], ...]}``.
The chassis replays the tape chosen by a caller-supplied ``router`` and wraps it
in small reactive layers (each independently switchable via ``settings``):

    hand_align            pad/truncate hands to the real hand count      (fieldbook_logic)
    weed_repair           DIG a weed that blocks PLANT/BUILD, replay      (tetsutani + task spec)
    sell_lead             sell next step's lots one step early            (fieldbook _lead_sale)
    front_run             sell before the opponent's scheduled SELL       (hook; opponent_plan)
    budget_guard          fund each 72-step block's purchases             (six_day_budget_guard.hpp)
    room_guard            keep shed <= 99 at hour 23                      (tetsutani)
    clamp_sells           trim SELL orders to the projected shed          (tetsutani)
    dead_stock            sell stock the route will never sell            (tetsutani)
    terminal_liquidation  step >= 718: sell the whole projected shed      (fieldbook _terminal_sale)

Engine facts (verified against kaggle_environments 1.32.7, env_1_32_7.py):
  observation["farms"][p] = {"money", "tiles"[y][x], "farmer"[x,y], "hands"[[x,y]..],
                             "unlocked_quadrants", "hires_today"}
  tiles: None (empty) | "LOCKED" | {"kind": WEED|COOP|PASTURE|PLANT, "crop"/"animal", ...}
  observation["private"] = {"shed": {item: n}, "seeds": {crop: n}, "inventories": [{}...]}
  observation["market"] = {"inventory": {...}, "prices": {...}}
  observation["town"] = {"unlocked_shops": [...]}
  Agents act on steps 0..718 (interpreter marks DONE once step >= episodeSteps-2).
"""
from __future__ import annotations

import copy

PRODUCTS = ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL", "FERTILIZER")
SEED_PRICE = {"WHEAT": 10, "CARROT": 20, "TOMATO": 50, "STRAWBERRY": 100, "MELON": 80}
ANIMAL_COST = {"GOOSE": 300, "COW": 400, "SHEEP": 500}
ANIMAL_STRUCTURE = {"GOOSE": "COOP", "COW": "PASTURE", "SHEEP": "PASTURE"}
LAND_PRICES = (1000, 2000, 4000)
MOVES = {"NORTH": (0, -1), "SOUTH": (0, 1), "EAST": (1, 0), "WEST": (-1, 0)}
FRONT_RUN_ITEMS = ("MILK", "WOOL", "STRAWBERRY", "MELON")
LAST_ACT_STEP = 718
PASS_ACTION = {"farmer": ["PASS"], "hands": [], "market": []}

DEFAULT_SETTINGS = {
    "hand_align": True,
    "weed_repair": True,
    "sell_lead": True,
    "front_run": True,
    "budget_guard": True,
    "room_guard": True,
    "clamp_sells": True,
    "dead_stock": True,
    "terminal_liquidation": True,
    # tunables
    "block_turns": 72,
    "shed_capacity": 100,
    "board_size": 10,
    "max_orders": 10,
    "turns_per_day": 24,
    "min_sell_price": 2,
}


# --------------------------------------------------------------------------- helpers
def _get(value, key, default=None):
    """Field access that works for dicts and Kaggle Struct/attribute objects."""
    if isinstance(value, dict):
        return value.get(key, default)
    getter = getattr(value, "get", None)
    if callable(getter):
        return getter(key, default)
    return getattr(value, key, default)


def _int(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def _step_of(observation):
    raw = _get(observation, "step")
    if raw is not None:
        return _int(raw)
    return _int(_get(observation, "day", 0)) * 24 + _int(_get(observation, "hour", 0))


def _shed_adjacent(pos, board):
    if not isinstance(pos, (list, tuple)) or len(pos) < 2:
        return False
    half = board // 2
    return pos[0] in (half - 1, half) and pos[1] in (half - 1, half)


def _tile_at(tiles, pos):
    try:
        x, y = int(pos[0]), int(pos[1])
        return tiles[y][x]
    except (TypeError, ValueError, IndexError):
        return "LOCKED"


def _is_noop(act, tile, inv, seeds, pos, board):
    """True when the engine will certainly ignore ``act`` (mirrors _apply_unit_action)."""
    if not act:
        return True
    op = act[0]
    x, y = pos[0], pos[1]
    if op in MOVES:
        dx, dy = MOVES[op]
        return not (0 <= x + dx < board and 0 <= y + dy < board)
    if op == "PASS":
        return True
    adjacent = _shed_adjacent(pos, board)
    if op == "DROP":
        return (not adjacent) or (not inv)
    if op == "PICKUP":
        return not adjacent
    if op == "PLACE":
        item = act[1] if len(act) > 1 else None
        if item in ANIMAL_STRUCTURE and isinstance(tile, dict) \
                and _get(tile, "kind") == ANIMAL_STRUCTURE[item] and _get(tile, "animal") is None:
            return _int(_get(inv, item, 0)) <= 0
        return (not adjacent) or _int(_get(inv, item, 0)) <= 0
    if tile == "LOCKED":
        return True
    is_dict = isinstance(tile, dict)
    kind = _get(tile, "kind") if is_dict else None
    animal = is_dict and _get(tile, "animal") is not None
    if op == "PLANT":
        return tile is not None or _int(_get(seeds, act[1] if len(act) > 1 else None, 0)) <= 0
    if op == "WATER":
        return kind != "PLANT" or bool(_get(tile, "watered_today"))
    if op == "HARVEST":
        return (not is_dict) or _int(_get(tile, "yield_units", 0)) <= 0
    if op == "FERTILIZE":
        return kind != "PLANT" or _int(_get(inv, "FERTILIZER", 0)) <= 0
    if op == "DIG":
        return tile is None or animal
    if op in ("BUILD_COOP", "BUILD_PASTURE"):
        return tile is not None
    if op == "FEED":
        return (not animal) or bool(_get(tile, "fed_today")) or _int(_get(inv, "WHEAT", 0)) <= 0
    if op == "COLLECT_FERTILIZER":
        return (not animal) or (not _get(tile, "fertilizer_available"))
    if op == "CARE":
        return (not animal) or bool(_get(tile, "cared_today"))
    return True


class _View:
    """Cheap per-step snapshot of everything the layers read from the observation."""

    def __init__(self, observation, player, cfg):
        farms = list(_get(observation, "farms", []) or [])
        self.farm = farms[player] if player < len(farms) else {}
        self.rival = farms[1 - player] if len(farms) >= 2 and 1 - player < len(farms) else {}
        private = _get(observation, "private", {}) or {}
        self.shed = {k: max(0, _int(v)) for k, v in dict(_get(private, "shed", {}) or {}).items()}
        self.seeds = dict(_get(private, "seeds", {}) or {})
        self.invs = [dict(i or {}) for i in (_get(private, "inventories", []) or [])]
        market = _get(observation, "market", {}) or {}
        self.prices = {k: _int(v) for k, v in dict(_get(market, "prices", {}) or {}).items()}
        self.money = float(_get(self.farm, "money", 0.0) or 0.0)
        self.tiles = _get(self.farm, "tiles", []) or []
        self.board = len(self.tiles) or cfg["board_size"]
        self.positions = [_get(self.farm, "farmer", None)] + [list(p) for p in (_get(self.farm, "hands", []) or [])]
        self.hires_today = _int(_get(self.farm, "hires_today", 0))
        self.quadrants = len(list(_get(self.farm, "unlocked_quadrants", []) or []))

    def inv(self, idx):
        return self.invs[idx] if idx < len(self.invs) else {}

    def in_hands(self, item):
        return sum(max(0, _int(_get(inv, item, 0))) for inv in self.invs)


# --------------------------------------------------------------------------- chassis
class Chassis:
    """Replays ``routes[router(...)]`` with reactive safety/market layers.

    routes         : {route_id: list of >= 719 Kaggle action dicts}
    router         : callable(observation, step, state_dict) -> route_id, called every
                     step; ``state_dict`` is per-player and persists across the game.
    settings       : overrides for DEFAULT_SETTINGS (layer switches + tunables)
    opponent_plan  : optional list of the opponent's expected actions (front_run hook)
    """

    def __init__(self, routes, router=None, settings=None, opponent_plan=None):
        self.routes = {rid: list(tape) for rid, tape in routes.items()}
        self.router = router or (lambda observation, step, state: next(iter(self.routes)))
        self.cfg = dict(DEFAULT_SETTINGS)
        self.cfg.update(settings or {})
        self.opponent_plan = opponent_plan
        self.players = {}
        self.diagnostics = {"layer_fallbacks": 0, "entry_fallbacks": 0}
        self._future_sells = {}   # route id -> {item: [remaining planned SELL qty from step t]}

    # ---- state -----------------------------------------------------------------
    def _state(self, player, step):
        st = self.players.get(player)
        if st is None or step == 0 or step <= st["last_step"]:
            st = {"last_step": -1, "route": None, "router_state": {},
                  "pending": {}, "sell_state": {"due_step": -1, "suppress": {}}}
            self.players[player] = st
        st["last_step"] = step
        return st

    def _route_action(self, route, step):
        tape = self.routes[route]
        if 0 <= step < len(tape) and isinstance(tape[step], dict):
            return copy.deepcopy(tape[step])
        return copy.deepcopy(PASS_ACTION)

    def future_sells(self, route, item, step):
        """Planned SELL quantity of ``item`` in route steps >= ``step`` (suffix sums)."""
        table = self._future_sells.get(route)
        if table is None:
            tape = self.routes[route]
            n = len(tape)
            table = {p: [0] * (n + 1) for p in PRODUCTS}
            for t in range(n - 1, -1, -1):
                for p in PRODUCTS:
                    table[p][t] = table[p][t + 1]
                for o in (tape[t].get("market") or []) if isinstance(tape[t], dict) else []:
                    if o and o[0] == "SELL" and len(o) >= 3 and o[1] in table:
                        table[o[1]][t] += max(0, _int(o[2]))
            self._future_sells[route] = table
        col = table.get(item)
        return col[step] if col and 0 <= step < len(col) else 0

    # ---- main entry -----------------------------------------------------------
    def act(self, observation, configuration=None):
        if len(_get(observation, "farms", []) or []) < 2:
            raise ValueError("incomplete observation")  # factory falls back to tape
        step = _step_of(observation)
        player = _int(_get(observation, "player", 0))
        st = self._state(player, step)
        cfg = self.cfg
        view = _View(observation, player, cfg)

        route = self.router(observation, step, st["router_state"])
        if route not in self.routes:
            route = st["route"] if st["route"] in self.routes else next(iter(self.routes))
        st["route"] = route
        action = self._route_action(route, step)
        raw = copy.deepcopy(action)
        try:
            if cfg["hand_align"]:
                self._hand_align(action, view)
            if cfg["weed_repair"]:
                self._weed_repair(action, view, st, route, step)
            if cfg["sell_lead"] or cfg["front_run"]:
                self._apply_suppression(action, st["sell_state"], step)
            projected = self._projected_shed(action, view)
            lead_available = dict(projected)
            next_sup = {"due_step": -1, "suppress": {}, "r36_debts": st["sell_state"].get("r36_debts", {})}
            if cfg["sell_lead"]:
                self._sell_lead(action, view, lead_available, route, step, next_sup)
            if cfg["front_run"] and self.opponent_plan:
                self._front_run(action, view, lead_available, route, step, next_sup)
            st["sell_state"] = next_sup
            if cfg["budget_guard"]:
                self._budget_guard(action, view, route, step)
            if cfg["room_guard"]:
                self._room_guard(action, view, route, step)
            if cfg["clamp_sells"]:
                self._clamp_sells(action, projected)
            if cfg["dead_stock"]:
                self._dead_stock(action, view, projected, route, step)
            if cfg["terminal_liquidation"]:
                self._terminal_liquidation(action, projected, step)
            action["market"] = action["market"][: cfg["max_orders"]]
            return action
        except Exception:
            self.diagnostics["layer_fallbacks"] += 1
            return raw

    # ---- layer: hand_align ----------------------------------------------------
    def _hand_align(self, action, view):
        """Pad with PASS / truncate the tape's hand list to the real number of hands
        (fieldbook_logic.act). Extra hands would be ignored by the engine anyway;
        missing ones just idle, so alignment only tidies the action."""
        expected = max(0, len(view.positions) - 1)
        hands = list(action.get("hands") or [])
        hands.extend([["PASS"] for _ in range(max(0, expected - len(hands)))])
        action["hands"] = hands[:expected]

    # ---- layer: weed_repair ---------------------------------------------------
    def _weed_repair(self, action, view, st, route, step):
        """If a PLANT/BUILD_* target tile is a WEED, DIG now and queue the intended
        action for that unit; the queue replays on a later step when the unit still
        stands there and its tape action would be a no-op (the displaced no-op is
        queued behind it, so PLANT -> WATER chains survive). A PLANT is only replayed
        when the unit's next tape action is not a move, so the mandatory same-day
        WATER can follow; otherwise the seed is kept. A no-op turn spent on a weed
        is also converted to DIG (tetsutani weed_dig)."""
        units = [action.get("farmer") or ["PASS"]] + list(action.get("hands") or [])
        pending = st["pending"]
        tape = self.routes[route]
        nxt = tape[step + 1] if step + 1 < len(tape) and isinstance(tape[step + 1], dict) else {}
        next_units = [nxt.get("farmer") or ["PASS"]] + list(nxt.get("hands") or [])
        for i in range(min(len(units), len(view.positions))):
            pos = view.positions[i]
            if not isinstance(pos, (list, tuple)):
                continue
            pos = (int(pos[0]), int(pos[1]))
            tile = _tile_at(view.tiles, pos)
            act = list(units[i])
            queue = pending.get(i)
            if queue and queue[0][0] != pos:
                pending.pop(i, None)
                queue = None
            is_weed = isinstance(tile, dict) and _get(tile, "kind") == "WEED"
            noop = _is_noop(act, tile, view.inv(i), view.seeds, pos, view.board)
            next_op = next_units[i][0] if i < len(next_units) and next_units[i] else "PASS"
            if act and act[0] in ("PLANT", "BUILD_COOP", "BUILD_PASTURE") and is_weed:
                pending.setdefault(i, []).append((pos, act))
                act = ["DIG"]
            elif queue and noop:
                _, replay = queue[0]
                if replay[0] == "PLANT" and next_op in MOVES:
                    pending.pop(i, None)          # WATER could never follow: keep the seed
                else:
                    queue.pop(0)
                    if act and act[0] != "PASS" and act[0] not in MOVES:
                        queue.append((pos, act))
                    act = replay
                    if not queue:
                        pending.pop(i, None)
            elif is_weed and noop:
                act = ["DIG"]
            units[i] = act
        action["farmer"] = units[0]
        action["hands"] = units[1:]

    # ---- projected shed -------------------------------------------------------
    def _projected_shed(self, action, view):
        """Shed contents after this step's unit actions but before the market runs:
        PICKUP removes, DROP/PLACE(non-animal) near the shed adds up to capacity
        (fieldbook _projected_shed / tetsutani projected shed)."""
        cap = self.cfg["shed_capacity"]
        proj = {p: view.shed.get(p, 0) for p in PRODUCTS}
        for k, v in view.shed.items():
            proj.setdefault(k, v)
        total = sum(proj.values())
        units = [action.get("farmer") or ["PASS"]] + list(action.get("hands") or [])
        for i in range(min(len(units), len(view.positions))):
            if not _shed_adjacent(view.positions[i], view.board):
                continue
            act = units[i]
            op = act[0] if act else "PASS"
            inv = view.inv(i)
            if op == "PICKUP" and len(act) >= 2 and act[1] in proj:
                qty = min(proj[act[1]], max(0, _int(act[2]) if len(act) >= 3 else 1))
                proj[act[1]] -= qty
                total -= qty
            elif op == "DROP":
                for item, held in inv.items():
                    take = min(max(0, _int(held)), max(0, cap - total))
                    if take > 0:
                        proj[item] = proj.get(item, 0) + take
                        total += take
            elif op == "PLACE" and len(act) >= 2 and act[1] not in ANIMAL_STRUCTURE:
                item = act[1]
                take = min(max(0, _int(act[2]) if len(act) >= 3 else 1),
                           max(0, _int(_get(inv, item, 0))), max(0, cap - total))
                if take > 0:
                    proj[item] = proj.get(item, 0) + take
                    total += take
        return proj

    # ---- layer: sell_lead / front_run suppression ------------------------------
    @staticmethod
    def _apply_suppression(action, sell_state, step):
        """Remove from this step's SELLs the quantities already sold a step early."""
        if sell_state.get("due_step") != step:
            return
        remaining = dict(sell_state.get("suppress", {}))
        kept = []
        for order in action.get("market") or []:
            order = list(order)
            if order and order[0] == "SELL" and len(order) >= 3 and remaining.get(order[1], 0) > 0:
                removed = min(max(0, _int(order[2])), remaining[order[1]])
                order[2] = _int(order[2]) - removed
                remaining[order[1]] -= removed
                # A zero-quantity order keeps later market race slots intact.
            kept.append(order)
        action["market"] = kept

    @staticmethod
    def _add_sell(action, item, qty, max_orders, merge=True):
        market = action.setdefault("market", [])
        if merge:
            for order in market:
                if order and order[0] == "SELL" and order[1] == item:
                    order[2] = _int(order[2]) + qty
                    return True
        if len(market) >= max_orders:
            return False
        market.append(["SELL", item, qty])
        return True

    def _sell_lead(self, action, view, projected, route, step, next_sup):
        """fieldbook _lead_sale: when step % 4 != 0 (no town consumption between the
        two steps) sell the lots the tape plans to SELL next step now, for products
        other than WHEAT/FERTILIZER we already hold, and suppress them next step.
        Skipped at the last step, at shop-unlock boundaries and if a SELL for that
        product is already queued this step."""
        cfg = self.cfg
        nxt = step + 1
        unlock_period = 3 * cfg["turns_per_day"]
        if nxt > LAST_ACT_STEP or nxt % unlock_period == 0 or step % 4 == 0:
            return
        tape = self.routes[route]
        future = tape[nxt] if nxt < len(tape) and isinstance(tape[nxt], dict) else {}
        planned = {}
        for o in future.get("market") or []:
            if o and o[0] == "SELL" and len(o) >= 3 and o[1] in PRODUCTS:
                planned[o[1]] = planned.get(o[1], 0) + max(0, _int(o[2]))
        already = {o[1] for o in action.get("market") or [] if o and o[0] == "SELL" and len(o) > 1}
        for item in PRODUCTS:
            if item in ("WHEAT", "FERTILIZER") or planned.get(item, 0) <= 0 or item in already:
                continue
            qty = min(projected.get(item, 0), planned[item])
            if qty <= 0 or view.prices.get(item, 0) < cfg["min_sell_price"]:
                continue
            if not self._add_sell(action, item, qty, cfg["max_orders"], merge=False):
                break
            projected[item] -= qty
            next_sup["suppress"][item] = next_sup["suppress"].get(item, 0) + qty
        if next_sup["suppress"]:
            next_sup["due_step"] = nxt

    def _front_run(self, action, view, projected, route, step, next_sup):
        """Hook: if ``opponent_plan`` (their expected tape) schedules a SELL of
        MILK/WOOL/STRAWBERRY/MELON next step, sell what we hold of it now (before
        their supply depresses the price) and suppress our own SELL of that quantity
        next step. Bounded by our own remaining planned sales so it never dumps."""
        cfg = self.cfg
        nxt = step + 1
        plan = self.opponent_plan
        if nxt > LAST_ACT_STEP or nxt >= len(plan) or not isinstance(plan[nxt], dict):
            return
        already = {o[1] for o in action.get("market") or [] if o and o[0] == "SELL" and len(o) > 1}
        for o in plan[nxt].get("market") or []:
            if not (o and o[0] == "SELL" and len(o) >= 3 and o[1] in FRONT_RUN_ITEMS):
                continue
            item = o[1]
            if item in already or view.prices.get(item, 0) < cfg["min_sell_price"]:
                continue
            own_next = sum(max(0, _int(x[2])) for x in self.routes[route][nxt].get("market", [])
                           if len(x) >= 3 and x[0] == "SELL" and x[1] == item)
            qty = min(projected.get(item, 0), max(0, _int(o[2])), own_next)
            if qty <= 0:
                continue
            if not self._add_sell(action, item, qty, cfg["max_orders"], merge=False):
                break
            projected[item] -= qty
            already.add(item)
            next_sup["suppress"][item] = next_sup["suppress"].get(item, 0) + qty
        if next_sup["suppress"]:
            next_sup["due_step"] = nxt

    # ---- layer: budget_guard --------------------------------------------------
    def _block_requirements(self, view, route, start, end):
        """Planned purchase cost and item reserves for tape steps [start, end)
        (six_day_budget_guard.hpp calculate_six_day_requirements)."""
        tape = self.routes[route]
        budget = 0.0
        seed_bal, item_bal = {}, {}
        seed_need, item_need = {}, {}
        hires_by_day = {}
        quadrants = view.quadrants
        for t in range(start, min(end, len(tape))):
            a = tape[t] if isinstance(tape[t], dict) else {}
            for u in [a.get("farmer") or ["PASS"]] + list(a.get("hands") or []):
                if not u:
                    continue
                op = u[0]
                arg = u[1] if len(u) > 1 else None
                qty = max(1, _int(u[2]) if len(u) > 2 else 1)
                if op == "PLANT" and arg in SEED_PRICE:
                    seed_bal[arg] = seed_bal.get(arg, 0) - 1
                    seed_need[arg] = max(seed_need.get(arg, 0), -seed_bal[arg])
                elif op == "FEED":
                    item_bal["WHEAT"] = item_bal.get("WHEAT", 0) - 1
                    item_need["WHEAT"] = max(item_need.get("WHEAT", 0), -item_bal["WHEAT"])
                elif op == "FERTILIZE":
                    item_bal["FERTILIZER"] = item_bal.get("FERTILIZER", 0) - 1
                    item_need["FERTILIZER"] = max(item_need.get("FERTILIZER", 0), -item_bal["FERTILIZER"])
                elif op == "PLACE" and arg is not None:
                    item_bal[arg] = item_bal.get(arg, 0) - qty
                    item_need[arg] = max(item_need.get(arg, 0), -item_bal[arg])
            for o in a.get("market") or []:
                if not o:
                    continue
                op = o[0]
                item = o[1] if len(o) > 1 else None
                qty = max(1, _int(o[2]) if len(o) > 2 else 1)
                if op == "HIRE":
                    day = (t - start) // self.cfg["turns_per_day"]
                    hires_by_day[day] = hires_by_day.get(day, 0) + 1
                elif op == "BUY_LAND":
                    extra = quadrants - 1
                    if 0 <= extra < len(LAND_PRICES):
                        budget += LAND_PRICES[extra]
                        quadrants += 1
                elif op == "BUY_SEED" and item in SEED_PRICE:
                    budget += SEED_PRICE[item] * qty
                    seed_bal[item] = seed_bal.get(item, 0) + qty
                elif op == "BUY_PRODUCT" and item in ("WHEAT", "FERTILIZER"):
                    budget += view.prices.get(item, 0) * qty
                    item_bal[item] = item_bal.get(item, 0) + qty
                elif op == "BUY_ANIMAL" and item in ANIMAL_COST:
                    budget += ANIMAL_COST[item] * qty
                    item_bal[item] = item_bal.get(item, 0) + qty
        for day, n in hires_by_day.items():
            first = view.hires_today if day == 0 else 0
            for k in range(n):
                budget += _fib(first + k)
        return budget, item_need

    def _budget_guard(self, action, view, route, step):
        """At every block boundary (step % 72 == 0) make sure cash + the value of
        stock the block already plans to sell covers the block's purchases (hires,
        land, seeds, animals, products). A shortfall is covered by extra SELLs of
        unprotected shed stock, highest price first; SELLs are moved in front of
        the buys so the money is there when they execute."""
        cfg = self.cfg
        block = cfg["block_turns"]
        if block <= 0 or step % block != 0:
            return
        budget, item_need = self._block_requirements(view, route, step, step + block)
        market = action.setdefault("market", [])
        existing = {}
        for o in market:
            if o and o[0] == "SELL" and len(o) >= 3:
                existing[o[1]] = existing.get(o[1], 0) + max(0, _int(o[2]))
        cash = view.money
        for item in PRODUCTS:
            planned = max(existing.get(item, 0), self.future_sells(route, item, step)
                          - self.future_sells(route, item, step + block))
            cash += min(view.shed.get(item, 0), planned) * view.prices.get(item, 0)
        shortfall = budget - cash
        if shortfall <= 0:
            return
        candidates = []
        for item in PRODUCTS:
            price = view.prices.get(item, 0)
            if price < cfg["min_sell_price"]:
                continue
            protected = max(0, item_need.get(item, 0) - view.in_hands(item))
            avail = view.shed.get(item, 0) - protected - existing.get(item, 0)
            if avail > 0:
                candidates.append((-price, item, avail, price))
        candidates.sort()
        added = False
        for _, item, avail, price in candidates:
            if shortfall <= 0:
                break
            qty = min(avail, -(-int(shortfall) // price))
            if self._add_sell(action, item, qty, cfg["max_orders"]):
                shortfall -= qty * price
                added = True
        if added:
            sells = [o for o in market if o and o[0] == "SELL"]
            others = [o for o in market if not (o and o[0] == "SELL")]
            action["market"] = sells + others

    # ---- layer: room_guard ----------------------------------------------------
    def _room_guard(self, action, view, route, step):
        """tetsutani room_guard: at hour 23 the end-of-day drop pushes every unit's
        inventory into the shed and overflow is destroyed. Estimate the shed after
        this step (stock + carried + harvest/collect - feed/fertilize/place + buys -
        sells) and, if it exceeds capacity-1, add SELLs preferring products with no
        future planned sale, then highest price."""
        cfg = self.cfg
        if step % cfg["turns_per_day"] != cfg["turns_per_day"] - 1:
            return
        cap = cfg["shed_capacity"]
        units = [action.get("farmer") or ["PASS"]] + list(action.get("hands") or [])
        carried = sum(max(0, _int(n)) for inv in view.invs for n in inv.values())
        produced = consumed = 0
        for i in range(min(len(units), len(view.positions))):
            tile = _tile_at(view.tiles, view.positions[i])
            a = units[i]
            if not a:
                continue
            op = a[0]
            if op == "HARVEST" and isinstance(tile, dict):
                produced += max(0, _int(_get(tile, "yield_units", 0)))
            elif op == "COLLECT_FERTILIZER" and isinstance(tile, dict) and _get(tile, "fertilizer_available"):
                produced += 1
            elif op in ("FEED", "FERTILIZE"):
                consumed += 1
            elif op == "PLACE" and len(a) > 1 and a[1] in ANIMAL_STRUCTURE:
                consumed += 1
        market = action.setdefault("market", [])
        planned_sells, planned_buys = {}, 0
        for o in market:
            if not o:
                continue
            if o[0] == "SELL" and len(o) >= 3:
                planned_sells[o[1]] = planned_sells.get(o[1], 0) + max(0, _int(o[2]))
            elif o[0] in ("BUY_PRODUCT", "BUY_ANIMAL") and len(o) >= 3:
                planned_buys += max(0, _int(o[2]))
        shed_total = sum(view.shed.values())
        fillable = sum(min(view.shed.get(it, 0), n) for it, n in planned_sells.items())
        needed = shed_total + carried + produced - consumed + planned_buys - fillable - (cap - 1)
        if needed <= 0:
            return
        priority = sorted(PRODUCTS, key=lambda it: (self.future_sells(route, it, step + 1) > 0,
                                                   -view.prices.get(it, 0), it))
        for item in priority:
            avail = max(0, view.shed.get(item, 0) - planned_sells.get(item, 0))
            qty = min(needed, avail)
            if qty <= 0 or view.prices.get(item, 0) < 1:
                continue
            if not self._add_sell(action, item, qty, cfg["max_orders"]):
                continue
            planned_sells[item] = planned_sells.get(item, 0) + qty
            needed -= qty
            if needed <= 0:
                break

    # ---- layer: clamp_sells ---------------------------------------------------
    @staticmethod
    def _clamp_sells(action, projected):
        """Clamp against a sequential stock upper bound, retaining market slots.

        Earlier BUY_PRODUCT orders can fund a wheat wash's sell leg. Their full
        quantity is an upper bound; the engine enforces actual cash/capacity.
        Removing empty orders would change the later lockstep market races.
        """
        avail = dict(projected)
        kept = []
        for o in action.get("market") or []:
            if o and o[0] == "SELL" and len(o) >= 3:
                have = avail.get(o[1], 0)
                n = min(_int(o[2]), have)
                n = max(0, n)
                avail[o[1]] = have - n
                kept.append(["SELL", o[1], n])
            else:
                kept.append(o)
                if o and o[0] in ("BUY_PRODUCT", "BUY_ANIMAL") and len(o) >= 3:
                    avail[o[1]] = avail.get(o[1], 0) + max(0, _int(o[2]))
        action["market"] = kept

    # ---- layer: dead_stock ----------------------------------------------------
    def _dead_stock(self, action, view, projected, route, step):
        """tetsutani dead_stock: stock beyond everything the rest of the route still
        plans to SELL is dead; sell it now when price > 1 (on day 29 everything not
        already in this step's orders is dead). Highest value lots first."""
        planned = {}
        for o in action.get("market") or []:
            if o and o[0] == "SELL" and len(o) >= 3:
                planned[o[1]] = planned.get(o[1], 0) + _int(o[2])
        day = step // self.cfg["turns_per_day"]
        extra = []
        for item in PRODUCTS:
            have = projected.get(item, 0) - planned.get(item, 0)
            if have <= 0:
                continue
            surplus = have if day >= 29 else have - self.future_sells(route, item, step + 1)
            if surplus > 0 and view.prices.get(item, 0) > 1:
                extra.append(["SELL", item, surplus])
        extra.sort(key=lambda o: -view.prices.get(o[1], 0) * o[2])
        action["market"] = (action.get("market") or []) + extra

    # ---- layer: terminal_liquidation -----------------------------------------
    def _terminal_liquidation(self, action, projected, step):
        """fieldbook _terminal_sale: on the final acting step (>= 718) replace the
        market orders with a SELL of the whole projected shed."""
        if step < LAST_ACT_STEP:
            return
        action["market"] = [["SELL", item, qty] for item, qty in projected.items()
                            if qty > 0 and item in PRODUCTS][: self.cfg["max_orders"]]


# --------------------------------------------------------------------------- factory
def make_agent(routes, router=None, opponent_plan=None, **settings):
    """Build a Kaggle ``agent(observation, configuration)`` closure that never raises:
    a failure inside a layer falls back to the raw tape action, and a failure even
    before that falls back to PASS (with hands padded when possible)."""
    chassis = Chassis(routes, router, settings, opponent_plan)

    def agent(observation, configuration=None):
        try:
            return chassis.act(observation, configuration)
        except Exception:
            chassis.diagnostics["entry_fallbacks"] += 1
            try:
                step = _step_of(observation)
                player = _int(_get(observation, "player", 0))
                tape = chassis.routes.get(chassis.players.get(player, {}).get("route"),
                                          next(iter(chassis.routes.values())))
                if 0 <= step < len(tape):
                    return copy.deepcopy(tape[step])
            except Exception:
                pass
            try:
                farms = _get(observation, "farms", []) or []
                hands = _get(farms[_int(_get(observation, "player", 0))], "hands", []) or []
                return {"farmer": ["PASS"], "hands": [["PASS"] for _ in hands], "market": []}
            except Exception:
                return copy.deepcopy(PASS_ACTION)

    agent.chassis = chassis
    return agent


import base64
import json
import zlib
# EXP239 native schedules: Yusuke Hayashi (yhay81), Shop Router 0913.
# https://www.kaggle.com/code/yhay81/shop-router-0913
# Ahmed Berat Ozer: V39 prefix/terminal, shared-action encoding and controllers.
_R108_DATA=json.loads(zlib.decompress(base64.b85decode('c-ri}-EL&p(j53My5<F0e<Xd^M=BpR+!6(;<$}j(9DMM2FoS_Tz-QkXes^~_Syg-QjEsoPwX0hP<10~YlC}2Q>nAfZGU9*y@Gt-AzyCk~-+%pYKm42j_&<L5zy9T4|I2^=*Uw-6@Y}mT{`le3-4Flwzx>z#^UJ?|{_?;4%fJ4=|M|av{`x=u@V7tz!#{re{pF`WfBg8v-4CaqkMBPJ_hI|#F8QbJ{g;3G<M`pj?0cX7=iT%(e|`D=<Inkr&VQYJ+WyPG{QUm+;}7l^U;fOyU*G@o?#l=K_;UK;ZWF%!$Ir*(Z(sglG3q~F{+y5c^W?q%@!$RV+uNV|@`v7L^ZJO>ujW5Jedfg{U4HO&D6@~8{5kenfBW<OhoAoO`A0tf`Q_1_4||=|*@rFuihRHi?|wWQ&lleR;#cwKoQ{8d{QAX@@5Cd${iHi<mp{Cm_qZ4SI39oc{O`XUKfL@3mdJ9x_y|5f^RFK-e=YgW;_av*JuHWGo>;Jyz^9#uc6#^m`1|s!uhT@P{oj5W$?OxZzkL16=gGF#s`ZGk>tXh}mp7Wv_4Q}wGgN-*akW_!8-M6^{yJ}X_J_>*zy4d?PqWWGpTps~-~Pbl^Ug;knE3PQG95u!P~PW;`HrtUPV@5f)iiGl)6Cv?obJU>uQBi7J+pa#{ps=tFGGdfO#DWFESYb;(b!cO9}r9|xIk_=q2z_W4M2TtVM4Ee+nG>sB@IpJ@}o+BnEbiL7p+)mKFL{xspA}Q{ejo0Z<ysk;kOz$_H|fq|7QG^c>i90_wApYKl1Y7!|}(D|M<7Z-#@<p@c#c;9&wky1b?s+@Par#`J3m+VDW9Z@7|J@$&Y^C?`fK}Tq(zQ%Qt+zN|%AElc8l%U^ct_Nt2HTkL;W^=iL~Si}V~d9x(r$Fq6G=<@#rCGfc35hsJw3X<paX%A>uW4kKrEvhN1gIr*%2`6_GNE<^8T<(n?P;r4auUygS>1>l6UP$D$)dZO@yekJjyVtFY$=d;*KU1RL?<Q<7{6ZZGy;vy5g$kK+V7Xb=#eD-X<-Jhk|1X0!4XszW+vfshk9F4H(VCBOjbQBEt{0D!2_xr!^rT=7>FRP%Ft60;08TLTdXTOIDn&RYsGNc?_-XKPt-2r**k-u+nQ|vHKe+i~lPCbX@`O(%`CiDyjaGRV~_6GrI{I)2J_e3Tjj#GvZWP5z01ilcOY|ELuj73;Y!TPEOoTt%<xRFEktN@l*KdX4It@SwwRf!i&_C@bCfFq-F^Ts)k1HR71?2_qSlImTAWL819=&oCoc|TR&Q+!5z&z8Z>c<oIKJ@~PfMNIQ5VD+x+S7fSt$88Ak7t;xDh;`!<^la9WDTIuCf$B@p``Zv?YXw4E|D)K!0VASq77>jHmMCxPJimy?m)Hxu(-Yjl-x!yVYeWz%3cLQ@l<pz_zWr{_lMCv0<kK40K8V_k59)+*8MUJv*6oMFI%jpUg2-Bs6ODsz9A>qmtIO`SPz(u?#W~Jv9lhvkQFU4uCdp&g9_R%A-V(<s#UKC#X~b3K%jGiXAQa(I)ye^Fj6||3LnlB%*ElUOxs?l&d|cirEkSjU2>=F=RRSL5Zr$}Wdy}XrNtcpy$j3dHtPntF8mRpd;1Yb0f%7=EO7{2Mf!9&^!c!2KGXA-N*(aa#)9)|8RU;FS0_^*676(Gd%F5l3m)pjUz??r0Ue6-<+o<yE^%FmdIC6u@Dhq;fvjPZCm-C;4kCdD}E1`x%)w|0t$0-_*Q!|c`b-R&CM)1gR(04hC;!Ly<{#s_N382@9=F2JB{*(LrkB`5<JN@nW`|tk&tZkGWsLvaFFaS`98eD-{6%o(L(|h539P#Bg$uZ;l+3QtTuc1GW@u%;&5~jFM<bIS@as@Ab6`UpKwN4j7FLGh%b`!MBR;Yi*y)Dea0yo4b8?3bCdB!Mjt-7}8Ml1D~S;3FfL4qO$cD<+U-z17z4&nOVVdX^9jTa-lT$2V-xwOSDe>g>o?qDo{&V|}eobHS?9=dBXyyM=C5dwJh_;2btui@*<%jf?bj5z!ZNWc989>AoV2nPhq{GJRdPkb)Tnx7AkpHxHV^|y<e$93wHM^Pcq<qss4gAQ}Nn?0RTcTn>Ifdk=#uvg-QFd%k}3~(^Yn5KiSRFIBu*1fo{AVGpk<=iK;Pv^nCE@1!8ti+Nt_@>{A^H}H_4r2hvlSA}iZNq8z#GRkA#DRj_VaaAU0+raTDL)u&JX)!c4Vt>I1P-3=Ky~<`ce*(5%w*us;&ZT^kjIcVxy4`g@tjSYSkkB(jjlo92Z=G=^@7%(yrr$nx)kdyc~gv$L$=~1maL_0v~`xIoIa6f2@pPi^4}#mArOP4v)?xEn@pQS<-4Pm$8YuS@TSXC!~*?bvvQ8ut5s!5+1+EJHZl#=#3^tA&~pm*EK=Wm>R{3#HjU{Ni=A}&-@my~)sf6w36YMN@#F+K@>|x<=QMbS!_{j$ZHPeBZ?FW8#;x&9N!YrZfyLl5Pl#Eb)!wD<P++EG)t@+`#7YF0#TD<J{I-d6CfJB<POcTPMdEVJvQnxY8jkgj!2Kb1A=n#6@1>7_gOpfsQ_thb=ShZ=^d3bYO0|>JC0>pHojIaA>h-)vonUEybph($l*CwgXudpe7s-3E1A?U&Xhhd7=+^@u+A$;=LE5vavhUtzBVsGM4hV)nRsb%ft~p1$f-MzZ5qw(kJ&WC^fpt{BWb-{FJ;3lV@GX857ZPJ2uID9C;pWM;O3YVKPNb}rQ3#D!t*;GcQ{X_P(v34R5-ouZb53UYE4#eFKVJ4oj><MU6CB;0ju}j7oUzg<E>REq=xfRG?LPhG{fB?|R<P0}m7K=@`ez<CX;JEc66TADXswVF>wvMu2hign7@8&<*I!0zgI0}%lIc_=t>EQYF}ps}a<6s(adZ{O?ZX-442zSc&{~+lYKmYtEC@iAI^MS5A`|mTR#{vMl5!k;giHjA(_pG%)~!?DQc0>#h4(3S@hQMDA#_FQSP86!Pkm2mx4(hSo(vhtQ_|2d>UJFxAXKSYTEc{#X^OjHTENb^j(CndPOXUo`u$bl&7?g62)tTr$;XZa{8lml@AA*DZ(ubV0EpvFQsW&}>dn@LjvFa|k?l9*ABTmKKu;P`kJ2r+n@>$XC@zkrcOn~;KLRPk41=`7XIt!2^cCV>40nm&x^&m$d4lSUrfsHuBkXMjJ)AlDGs#w}w6nPJjInGOZ*^Iv^h7a7Lt4941%!_=(~ifA<_ZZ#1=w7xQZ1#J+e)X}Knuu|j%F$tk-uVm=8Oj9n>eh!#8Hb4c-tH+(OjYRM4zW>VgZ!{0A#0gCh?A|Rwm1GMn8Bm*b+==$wjrQ%Z(LZ0YzTa+dauCm6*b_zR5r#IJw%?c}Z*y9|THHOyw24f{M)f3l&T+2CO{8@N!hQMOlz(0Fk3%B2q($vAw)<!K~o(p56HsvTl8qc<e}de8kDoO(K3;TC*pitW}A+76`MjpUJI_6A?kp)XfWiW>u4+MYMUwXHctr^s;y^w>XQ1WZd9&8D+&#zHTjxlxFiWPh2a|#&>H!T%C1FzF-@O-}b_&@9!@!e;j2oZCiMXqIN4yX!i~Icqs1&{0+a&6M?hG2mKhY&K&^3qEZ6a>%0#rF5#9})_=h757`1qI!ODisH(n@{VYDvfi8s_AL*Y=svt)~HeE(=Mn2oofS`m|v-yGnaE??#aa6b!B?1}3%jnHz?SP2snEx>O1-!9#{9N8=W<=M&oHTcZ0n-UWzd-*8Pz^U}?q{pI9k-?hhyDJO?}a)YG}xm2$-Q%)CwuJKA2t<g1xjkss43~0^}R3Wr?-^%)*a!Iv0j4~`A{|oJ@T8*Pa~go#$<9T>beGzoO`eBkUzdGC2(X6AE``l^Jm=bdlQJ^8W)S9^L3gNl>rA&X1LtsH(9)*Z<f7PLE*?-^$-#f7pQK0Z*Dx&t$fm*e$Jan4;G_%b0rFbv;2AhUWU9_aMaogASmhySo-lg)aN#xKfdbob6!t9R(gg#nxIXNdOg0*+zQNhkZZ(ZUeZ?@#byKUmdz12Q@C5rL3YvU;l3KxnYj33h4<jN&{F-b@Nb|N`mQW&VOiEXU(}izC2$l@coD88*w40xAQf7X5Q4|541M5>%L2W@N0Qx8Q5B&iXi%jI-(jNaRWYv)Csl@pu?9Uo_`t=hHNv)eD}`)_$_XPSW*BWTBCLSxy(Uk{g%Z%(f;P5PX(sCA6lcMX<<h%-a^+PoGoG_iBX*hv@fE|zJ6rn)V$^&$L>v|DCj1OYzK&7ZZG|F#kufVQAMm7n9a&SZv6A|20w7OA89Nk8Fb}O#!F8;60O00|3Qt{_g`A5N%<W!IMg-{_x${2OnCc_!226(}8L%XrJA}oPPZGJ8XLg^$vZ=~DVNo}}Iap(xI_2el>WhnU+Lga&NFl4=)xik%xISQ!8q5P=U5x;-q#{<`KF64^VV=mF9pB??iuB7`-Pkpmd|jH%o$BtCREX|e>bJ|Eq^S@-u2W~nj^$;KmS~wl%74w@K}mkjY@my21eIRSpTRhn$5a#8dZ0cFmD4~Q*$l`k7@KnRB={?^j2`O=(_RrjG&2YNAng<^RgIVuI90^0czJ;>8{<Pv=%A_=m1&4<1;rQ!RVM!@*-etvUoLG0m3+YKNuW|iOac_QDbPlL&`lo}Tl^=VpbFPBNH=KPR^+~%*73Wr7nKZNi6wY*)62!g4g+in;zrm+-+8WeLeD5#=rW4FoomrLyNnCa%*(pw*ThgtDwVi~ll(kcFWgiE1_?I{l2cWxQsM!Keen<hBWpQSgGsR$T}FW{c4Do*-ax_AlLAxv<7<rF_Rmy_Chd7ytxpUz;TetcRC1!F0tl|%_!)7Gxqo|YPuNS2m4nQDq#=tg+dcdpkr(9~()*ysBt6vGxL0E%beIbLoDrpXht+aOt??1-&H28-&=9OoOJVd_I&9kCSRFK|0FjM<S1ypNHaRNOK;M9o57(kbN(dG$2U#7t8Mm?~1;o@7$E@Te5mi9I!vu3-tM1wMVF_sj>?nPp`!d`Vd}hmQTxuG{$}!)&kQw5NYq&rqlT16N33r0k9B2i<Bz*>LH`M3YH7O=qqOXiP-H}Q1)^$m&WvEL0d>7DqLFTz!9-~*-rpnIt8tiUoPioqnIhR<_R0-r{b=orNcM<}FZ&L2Dix-RIWhKR9-<K)-njSSJ?1I&tkkdd5N@I#1&9q#+!ejAGYp{>e##q-UFHZ285osk`^!2X*K&5A;wCtVsdRpG`h2T98fWac>h~d`u8`Uf2Dh9`H+C{n%WfA!EuwNJ^mXB$|d8NT)g8Rnmv4V?{JwMeeAp#-i{FzoXw(`DID)cADiHZf|O0q*Vc2DR+iXagKY&30oTd_FFgI2IaLk=PH02#D0rbv{V0T3H$;Zdg6rq9w<+0Saze5)46S6JxtAy2Vw>s7G!5rAPpY+ge&uIP0v?jX~>*!<XRD`WS)!w)J@)fW%6?(R_Bd2d6ll8~~%l2yyNL<vo}Yh@Jla%4C{D&GLbYyctDE#g$HYkR74hUFr^Loc)C?FG}&a%5-N9?E7q(<KPVV2O#30mzWy`f{-q#RAj!%hn$H(Ng9`VM@{Z<C1@T%Z6dIagH6a#aE%(v9ngeBbT+M^`VU8?E3aI>&5ic#73V!0wV9z^|`k7U!tMgU6Q+rgm<Tkt;fIr{VneN&O}{80L&<aNnCH~0rJdt7iuQY!K%8a4w$RY&3l=Ho}X8vw1i)%#-S@v#Oa(&Y1nDvR<21M3n_zYO3USP6vQwp=EhO>g5q-FEF1`dY;)qMcA+eqsO+^bS0~TZn(_s&+{4R_1twSPJ`v(E+^-;=$XXmTy_j{vQAFIxWvS)?Ud36W5Jxc2cNE3NkMJ4aM>l+kOL;yQz(I1Xhr!Q)*Mdq-Q{8+Gfc!+@LtcbU7A<KxLk3{+B{8ID@}!kH_VZJa<I(0DUV-kgNeR*>PiQ;4X7Y*{l@_?AZ&P#1A;nJjNj&a-eUzWx{~hcfOWdasm(b135`U?r)@vrTC1~c;<GP89qeqy8u3jFWKLp_Zv3JoWuW(*f8F+xvli+K&z;=4@s`|bxzz~Ryhk{duf+sT^^pAe`E7LK+F5rWcHAf9LYoZ3QZq7x~1}Mb7`#MU<MO&lHxu2=zoN1LuxuxuiV_7epf@`kfpa7-&(dr@g@DtGp*5I;n*;Gy#u*-mj0TxI<peO*YnSx~wQR=HU126>zCISqG9rBf`V!p6K@H>HR>qNyav7H@JgD!RxK9WX)5{$xH${Q&%Rl+)%*a+<CRqv1{8*L9ZR)7O@FDMNHlF)@8FhW)D5xp*P=dyLSLWFvf{p~m=wTjM;(m^w3<+Vt>cI~4EEHjcqzt$=qc5R1Rag<QdI(D&K)XOK~^G-Yhr5q9!5#9Nl^)yUZ5Br_D*2kelAp--iKq@XN#-Re2F}FDOqBs^)SfYQydIFH5O$&N&Pjx6YRI+>?E$V|#-cZ|@dvxBxr#yV}ithP<iKD6Tc*y;B1@&|}2=fAFP58W_iQ?COY}W;1P^|!+wJsmyj2yDVnb<L(%iF$S8aZHrc~ph3k)nIY0UpO{{EXF_7z%71Wwvos_{CIHV}L?zY6vt7-O!Mb=)ZzcS-bop@HKWeU1eXn864TTjSP@z6{kb;V%myvml_TF`y>bN431SZ;2Fn$F7+i|NsWs&m^ymny<~0~tvr_SKXAo$s?2@?tp^3g%+hJY%*rR)esqlnewh2R=1c2B&#|zYf?}iBARY@4Q!#)+zhd%mkE6V8&0&rC!7OvLJHW}Ps;tQvrYY8hX%YqLc_*o`mJ~i1*>OkFZ>G`444k_QU5SBZJQcIiMYIk(b4d+g-HJm=-Z$BmJ-q{FDo?R0x=hGXy2hZ>2m#-eSr!s25thbx+hc+y<FrRMRvjv|Oi>fz3f;7|yi{zc2;mVtDup_zD1D5Om4UK<_Z>`tgWv?we<=lpx$JL>!x;sr<$Vqj0z=aegG{WHOGF!HgWB}{UE&N!^DAP(CKX<lQXarDOs+@#M@fP?|H>7m55rsbixh|&-xb1$n+Rm-^8!O=25xpO_!f0$$>TLv9;J&|-teqknU%|=|9Ocb!rm8+F9>lH0}0`)?x>gy4ORRlE!uiWg02s_kG}R4m{-xSaH~Qz&1XzWH-}cisVcl&m;zBnAt}-lTdaXn%`HFKVYN>l*A*?yIPIhG!l_rru%4rA*=FWgBBg`e6{3XJq$ty(I76rk5&fwwm?qIq#<ixvI)EGGk;eI0O)d-Fl5$FuHhTu(H{>kEKIAg+KGclc@z#}jz$0U;pOvvLk#Typx6A^K-D$MW2w2x`*=TAAuscFH2mv+th%^*4(L;i^xu~gbF$G{~nfZ2?kW?yy7rG4svw*;vf%KgiV&usTACkx1gwm|x7A&0XASoy7Q;h`TSero2IudcXk1V52MNX<FN1F3&pvQv^o7{)@Q*L6M<`2B)!cIKDdoCU+J=ZE1rZTv8Lo$|<((t;&?g7a`<Obgrjgg)U22%oJ47|=j@~Vsc$r4%t^S{#)AiQBIhHZx2ho$cXg#=rfd2IFx=onK2L`r<<g*mFHrB0$aw|1L9^)?<6!&Y&yS@&aE&2ZNcYk?N`63nA)+5gcR2y2a&>KN%WHN`U+PekT+;2NuydYejlU=!&ND@4i!F$RrWPP-QC(aS=PR`f(#+&q;;vFkD(g5@PF_n_OuoRMzIwk4kJA08r61U8WtNO6~K_w2l@xJQ!UB9X74nt(^c^@nV%rc!VLP$t+zfi#^V>vI^zF=3o-pQDh85IWxJYp8J#rkgmVmz$bQ3bTk}w9&afL9KY?S$BYI3!!5}6Nni?NM2g5LJ5QQc~Wdc1Nl3{7?L&n4XHWg01}YS<~eY5rg9O6r$V!d<Yz@X24v(1(RYKl&NM-pMWU(M(S~C~0_J4*4>!;5sl^^lCl9<cgt;kFDb0=hP1RU3AREe?QJzxdKuRE`TH<$VzLT6YO~H3feG@|&6*7d4rfsVBLyNx+mnOv~hBaHs9tG^oqm(y=F>a!YCCV?HG0M_+-bk3W)q-O*laS6O6Sryf)=96MSw8b1=kqJvM3Xw%DzUs^-$*SoN?1RQ@v5vUc{QDf=`pMRmjDMrg(f-LiOZDOOr<uqV8ft(546lXdnOaK?pdmUl7#?kqU+e3u-0@&+^3fek^e7r*gsWzTeAg3^w|A0E8D6D9l>h-&nPTXs=;XL^RI5+z-G}2l>&?Os<#tHcEJ@iK&LRTHo{5J88er3!VO>o=8<Ux>3~WXXCfrM^8<?A)!SfG`5mI~*6nJ_`w!LmMs}b#`-Uh4F9R7BEruWGlCC5{PgO+kyo20tZmDxJ@Ld__(4xn6^8>TprGP@Og}{6fN8lLDtT!XNi)_AK{|oo+;PMX!U7;o7@i^qA8qX_w%g~dum&e33L9}+~IvRqzTpE?K0U>R%;(Ro<k!k=;MU<o2G4Ca=wEA0@<>)r0!wF{w215$<?x)cl1qE3Bx(eA=sQMTfKrJ74*ZO+7680;Jfb+25y3tt?-YVp4j;O;K=->>TUBJ`_I$rWR_yaIla`ceH^t9IUuk$RZCrE``w4#Rt+q)P84r2T04!`K&sguW7@ZS`jM=*}d&wLORkixKYAkEnZ1sP^Wf8+~^<Zzu!Nm8nF2e-;Oe=2$p89OvC@}9^qLr#dKD-obw-=xBC4dd=2sgUKW$~B_t<Dk8NbEYhR`mfKWuT)nT#5Hmuo<?F<O*kHJuVhq|r)sW1hT?ahTIxKj><M_|s@e$CKt8d2L9}MgfQ4uf`wEyKU6CvX5`3%VK*-ceN+PsXS&>DIdTYi@)q}+%SZpQx-=t*3E<C^l@(C?(o<Aks1l!}*?FkX>Ck3>DUJ*1rBV1VW7i>$9ZDCBQIFi|2Vv5h8f2dtcJ(4xUAxfRXBv1q7)pCuW&g;NkBICu5dMlnn#3e4$hT*i$WjJ^FH9{D(od)%+*#H)_nOH|&Gvr+L{7|F~R%)f^IGkZSR!F?!B4-MoOfPRW^rN&hd}$kA;x<FZat9Dk8G2}?f*%~l6O(!%b$vl_gQVT87F_^cHx-H=Q_DyPgR0mWV?c(a`%e{$xu<4hX{mRjA&6ke+eI2!X*G2@joUttLU22dhTU$bd~9i5(}<MPo#kAgljrP=8El4#p)n|MlGB69r#Dk}Db<B~ZFA2-&y7W}JFq1M*KZ)LF}8rY$I`qrE5ht}*3U!NktX!kG=w{X9HppE=TG}@?#ZGAM_rxHU6O3`)&3PFc;Zi{Fb5ry91Q~#%CWF4ED{xv0`-kcERox02Bnc-ZFJ|96w|pwhl&9VImDItAfzG$LM1>5rNo-1R>jGkCtDCtnj(|_ocS6UsCP2u3_Rb01a+#ZZ#c5vHo4!Jaq+xuuP<(igF?2r%FjPl;6Sa;RzCjGFo;v{!q1Pb#ZP7SPIW6N`gTlbgjE~PEdx$9`?TMG87J4W$?Hr+o(2Kbg{+BH1KYZCoJd|GU5>n-yh~C>#%MR|l}quKyM8`I%B(SyGi@{NRlTWLPL@l(<u;luJ+0-$IrG164?){~JW3P9prTHvjAZyFR3Z9NJ#ylRkPMZbgho<W=*!K|#$^U<9ye46ofaS&bHH(;liHY~CF6WXod1irnEB4>8FyhW1z^Dlzn#gkF%;5sNt>kE+5JUuvxJW*(nU=*RxIQW^l^SSw<cZ?7K@M^*(UJTm9LVp6PUZJQF`lBE*zh7-qZuMIK!0qDl8ko)5Skxo0+g4<V+ysl#>L6sBGH4OqTSn(l(9XhSXgG(U<|YwAvq;N_;j@UtXhT55ptV2^5dtz93&~PtV-z>h;y%x6?&cxTiH8;+C*#z6kg)^Qm6`-?B6kzi{PMf>^pIRHyKoOi~jC;^d1On8T76)*W?nTYUOe5EIaJ^5NPCXF3u<+R`_gmRul8%FKP1Yo|s$KwIZ9qq7MNn<u!1EL>X_xN?zNqs4Ygq#1JhOrQVi?=R>8Jnzo8ACQy)Zl9)>EzFkn8%akm(y=+k?#Y#_5Cm48Bs$(w)DmXCHj-Wgyud6flS!@_1LvqQq4BN<;5$^kN>V-6UkTPjWwDl2D<19(s2}EO%{OvKMSro88-dEUxJBu;!>bDTiZFYM?gQBOOi3uTPV8)W6$v2lqy%Dt1+e@U!4ESw`(_22$_iiU7fLN)^6!iZ$fiifEom&9Jf{;DFc87v?k{*vcn`?ooK1lkE&v2_f9Gy1n-0gt@Z*Bq1xEkl0BZK=wJkxP0r;~J8^wY^RAxOqBF%!2(S<>GO(qurO|p*aM5hH)Q~=UyAbW*mw|Bb<UF7q#l-IgS31YJzw3;i>&@zbT&glLGES-u*=6Ts{Y6WS@R82O>TL4vnSOr*>F8f$-YK}P+u_vL8PddNdRwf)d#gIN}84@qSfaiXto=SEA^Imb21}+7J9wmv)#2bh(Wz;_bm#VnK>I;R=brB>CDfV>zbMZfr3lKE_Et|WqwJ-}rUYVo;>_S!?p3)_6-UUwcA<L++?MnQ)xa82Yl{WRAR9K^JGBnX<I~_b-<EbiHq-M>~9FzTH9PcoqEBpFb=d4N0d<^H~)?M))z>B;ztH)2IFWM2rozlCgqexJ4BWWXu&!@s{`Al1&WNM>ElYzKG(&41{5Fzp7ZqBf=&)>fedUVbr1cAnAds&&mlR{8RFwGKC*)b{)xqylFj}7?T<t-NuPQjQZCkJUc9UX&rIAb<GWJ1Q2B{R3`hP6$BYo+yAuK{NC3H*v6AX!kCGFzU-kaS=SpOT~k80YfJsSg;4T+%cwuaT1!Z(J)GwJ`?(DB&u3+>(*J-SkW8sAF{M^M&jl&<`G*>l7hu#$v{eXoPCj)~!bVfCS$Gp&fC$Hu^%IM=20Yb+^?HaPqK*O(;-4mevC^&Shm}+pOIOt_spBP*q#pC8kz#i<l%ehmPe=GM32%5rHNM<w2-SMp|S{CGS{}&Q@?VYSfpBZRIH}d$Q85JPTUL&_iJcst1$>S|!OfBBV{Hte~Yv@fZLZyNg@}COlW-68%Re{qOXIFze=%b$k%%;{>NbL6SR}ys^zs(bd0G*Pqu6(&T-iUJr7{Io)6E_rXEaX%<@*)+j2r+$EN@n#1L?V%F_!@_lYV5)YF|nd^HXL8`XOWV+4~Tab-S((R}DZqSg*#bx%cn_s4FLVL}h=~H!ht)CND%051f;me)g#sqYYtcy9aUaR*hZ$a^Dn-U=rGKk+v63vj@uc}%f6GU48r{W*O=oITnua$g3Q2;ZchcjR3ith63pY(<FUF!oRf?8s(GfuQH_jarkUGo_0^>2zrEKggHDL-dz2BPYJ*WH7FJ`|5!tdAAlpt*McDtx<AH)7mirTxjTwX5}?*myy8M0$964nUntjA)6lEi?(IJ(4@kv{s-O(5}P!SG_BZb88AE2QK1A%$7<WOpNv8&Qv_$v_z5fYANTA8zF(VI|9H-tpx!`0h*0@X=$i34(7s%9#o-m-gARh9N!~jAxR4s+Ro?uojp9!#-L0`==CRe*ippcXr7Ele-J%^4xvyyb|^i%yX84@ke;8XQ*$|t@9*yi8m7H|Fs<QIuNZ$BcX)sEZ?b1x=DUZACC_(p<RK;FG>bnJOp)2?{tAa|?kTa2)Iw9-<Y8<omI_YsQDFx(<M_oXte=+HUNI-XFcFIYCV0fe4n2X#{(t-P{fD3a@#D+eHRZWGONqsJ5t4cGO0xz|;A$n1P$$-RH(K3^Uf3XL%Q68)-mYZ|IGV{{Cng;LveV+<`b1vd2u*LHLO6v8uw1s!tb3MBG)b=sm|1((Ua79tJY1kjw2hN8m5nfY29iCsRtJhXV|ID|q!}ZaOBTtZT%|kkWMm!SzNm@&usWyo{2f$)qKk47xLv@m7`O4#Cnfw#>uV|AV=H9CC-DMP=I%``&kXEYDYND0U;Q~4S;25vd)Q>jENK(qvL)?D;cJeOI%%g4$%RRyNqzVrfM)Z`4ZmSFpE{wh^aORqsi<nb_*C~f3f;mtT3-Mem>~*ZpAMzQ;0mPf=YyN3-xk1~>*A~YT8ck^CfHEmDV6wOCZw^-ZcFQJ(}lUqbX?;XvtLZ+puGR)@X^zf`SARFsLFYrhjK+WL$iMT;_}1rPYrHD0w7)2R7)@Tjf!))IWTmx+8vLD7}60{xkSZVikULgq)w;NsMRrre5jU_C4ap@vI=jC#SCt2ampG1Y8*FSAz~~7K{}qF#?{<k(iO}625^tcp$V`AN8u-ujo8c#UC*KwepC2SRib(My0*}0VG6z|7Qm!G)L&@&&05Rpj;jWhY+yk!VTXo1ssg{dP-Ut~(=y|B)qM{iDaDsoz&F-`W7xpL&AF=u{bJ1#ry*G;(nZxr&?K=0ySD|~IEHnzZFE_Xz~_!prGgwJ)yI1<l!M;};PcmT=7I3roOgM7aJsPe;nnPQj5abCqWOT$1#KUWxxk`DwUL<46Pb@Mzr6eS5`K8P_Me|-5$^HB%daF=5cTIbBunHVrTmyyE|CNpo8M)&IiC3&GrXL*e}XAyD);|;e(&###OZjf%UgI^ojDJP;0I*NjjF>x+mwT3Ac|}PoU=Z`3xw(acQZXNNxuFv>X&EN8Tb<^P|bkA`4^0r>CFFkICFY$AUDlo=fS+Zw4C($cgN;DTlMH+NvX5+oCg0jmJ0A62lkDQ<{yRb0OPFNmFP2@Y**}#uC6y~F%28xW@YKpWP!Tsw~Nf3#pl)#fI|7ayNUp+blKmY#i-2dz?uihfgv-dCTzW4+@2&oL&S|fTT7Wrr_n^)gn9*y@?PfW{z3A|Og$`SCV9_t?s;`&`kuc0%ZGQr{&Xp#y!-Y2FYmryGcTvf&*0jMV=sDs*<b!%f>MyXA@d#qPovL}SB~lDzy0ygoM;&D_V{b4F21SpQ1cK1%J4DjUb)=}jOHAmzrCc~Qf&III5CUwG;Z=RG(Z4GJ(0_f&Pf0%s`8Xi;E`+<9_O{lq?%Odb)ko}JfT>JDEhngIU6$P&H0qWVd0wBqZX|ybOGoa5Er~JXZ0UHACJFzUPPAc1=Y}~{=DYl5;;c0OOSRil$sW-;2_maT*cAEibWb~iM{%k`tan+s>vrLe}orfSWIG4#p2_t29V1#f8B2dzaCp}wVGAqxdUNMfQM2ky5g9(_Gv^dM<eO*I>~Z{cnpWG!%d_JX8Qr1^{ILcYlU0LFciB*DHDjP-Xw8_(If7eNP-QNdxw;CAc8%D<M&)Namhu(7W0+1<c`l^x8uIX^vMzY>x*NmNOp$OdTm~K37l&}<crrie{UljGbWjFsibQu-yhv&rTozxK}qfV;b)<7dPwpcvzG!_%S-D(F2WP4E__{?3C2UG<%8BMNx9#~@*#QzjThusP4GLcgU&b5Gqg0Z9l^b=?xtO}K4JOhQIBEocBt9k5ogNct;EZ)8!Iak8qbvRv53=Iv2~Lox(A66NIVzR6IGRI=VT;il4nsg3+s4Wvf7wOr%Uq;Cq9*9gzs%zFp{OQy)}1|mR_@fb+v(xWPy9L(zJt(p{wcmP8hqrfRHA@T(i6r#HNaAV5$rGCRv;^nmxHH(!4{)9jddEsiK1a7?sJs*}B#sIu)-eVS~sn_LxSkj6mL>xwsSo>mUmSMYmDom=v9%EKE%|dUN5s<O~I6#4#&@%x+QAiZI#BjOhk|L3PF)*Hlb+PSz_`<$alvfa8n(B{4tL<Gj&5q}CWXjcU{8r*2rEG?eJK_FT#QyB>L>0qt&(;rc_|jWi=aY|=W*w-c>{SuwHflPYyyS5vJBOInwJhs!Z_Aa=$kKRQ+~fvVZ%P>68-Dub}S-fjOR6YJ;}JZ1L!4Urfo1V!hAr;sJ(b+WFg3UnwO!#WU=*)e#c#QVKt8djSapSaqA+zrjPVkv-;RC1%9oKG}iJw8eA_HmO0Z?Ulop2#j!pggx8h$k$Ln6+1yWszlw>x$Esu*S$2z5s*2CumDIU4;H<m~;T7aKwTlBaN!8t)~Fb*SWut7LoXx%RY^_#WtWSe`Vv`ZADqUz8}0b*eba*N}yNX&T^LF(tmWIZmhV@SSax(&E}}m$Z#6RhpD^rrhk0jm^C=cy|L`ChF*<a@-J6NZ4hzE7fc9=^AJ~{1=of%khVfh^<j|8?0&`QyQkyIp{x59i1%Ib`mV|pkF*QuA+w7srEc0j0mIn^5$A%%JYnT3C0fRM1vcTfTV`j3rc`j8Ayz}^lt|bWFSMn&?2~{>-nz68VDd4!;r#O%6XWvtAWaH<DpjLGzkt4X{R9LxS`B({e{Qq$Tx-J+xbz_U4T2^rM9p{*LO^*K;eu0gFn_`1YG<9F#={;~cvgqyC3(`^&r4>5aT>ym4o<^>YbWh3LJuAr578!(-7AY(E_*m~BbLn3gzs@;O^Mo*M57AiFN+hGy(!8$P1^~PlrV9$YDQaeQLxeS*v#HV?G{`{FeGGq(2E>}>M1!(J(^*|w=ws8B=N?V4Z3~u1%+8d_T@&qlUvUN5{Q^*yN0+FV4P3W8qDq}e@z6m*-pljo!L`2S^1^nIFOU7wIn9=`EdI^wMyu-Knm6T>JD&lbbCVU+YB@j^Pt$lEY?7TR2$K&tVIcDSG+$-2c#$sh*v?NCo32v|KyMYplME{LGQ^5bj(eqbWNxb;9Nw7+EuB#^ZWUrIJ>fWOVk<`zo&Q+<f^CsVnbb}h0<m6SlmgAd2+Dr;jh1{X8y>|$w9`onhC+)QM*{JS8lj^Y&CUO))jzbYa2u^QE8o|Bdf|LBDi(Mh?$A#Co|;rP*>b#)a96<Q`#jyzrM;DIcx9XiuGVzks{~%eXcTYFvydUJgC8vU#0V3Q8^9=QXy|(eZ6o_>df=O9n8)v)=^;Rsdf)Q37Ap{fIL#b_?PzyT91RwLZ~C*083y@YWwCIF6D%qMCr8RuelYrwWQIU)BtUX+XCsUVOK(|eXZvK1CT$qjM(ioEO_9pZ7^bXH>q7sTn>zqOoXrylxi8NxsaC}CwTD|rG;Th#*aH(ihW%zb+1SV)IL7_LE77gL8o1%BTJD=p~pMtIk*G0(Pvu}8qLPzw__-ol%5jvr;fVGVaDs9+FGEyw58L>H6WNPI8}p485gTinNdtZI})m`F11l|*Ikt?)Aw9xtt4$D)D)1S5ji)y*ONpWAcPxu+Fia5AKa99<Uw#^&h53MtPw#nc4J{Tu{^PiiYm<$b`>%Rni|}v!KN)tbHGa&v-kkQ?sd)RIoxJfvN5%lCcMQ9S3w3i^v(5kn{?04Nbw6a=nUm?TS_zD_Cq&IEQaf*J|fzI7A)<_K&2YLO`|Ey!3eNKsz>$qkBM{?n8j9@UYkj8nNhQ1&}(&c-2%iWsL8}w;AYI-Z@=#7vPU?6PW&(oVGNmi&PXady4>0N7wW2#5@+O5*eT39f#Mg244oxYS;RV8?oQ`iGE=YkhAlqAwHPRcqQsdgq`5sH5IJ~eMl6<Jy#@@HL7=!9DL+KCag0XJCftG00vONY28H>IY#09+42nk22L_Im(kp5ea)gF{2TLWg`4|9?rMmWX-c!~D4HVuc$h-0KMh9TQ1fh>uHhq^m*PQ>B2BgVUO$G#VtwN^_O`6I09ZgKIoc-}w4UIC>%~k?B6b$bL0U05Gpq>`FoxLLNfz|Q7L=?MFAjK$8+$(;3O}3J1aHROy5lh6=H9N3EmDN#MbVU!zUys67o!6Vu9$b<7LNwmN{Ls33m1HuCUenCWw+U+|vT8*Zz<-#A<@NILmseS&AdR7sl0nU3<048!*rJS-0u-zxZ9k2zL&8v^y-!yyanuVpR|y?p!bHqufc7%w*k4U(MBQdSI|pRoYjYgHhjEqJ>gXLDz^$o&wdLM@hgy2jS>Y@RPObNxupUc2IyFCEK?e!CIC=KFuYI#SF<Guu^jrdOC^nYOmOphP)=DGR_<*1QV8#&rxfp$w#x%X>#kdqvM_&IaP~TTWnVjF#=P1M^ti)29TNZtSTOEh*#0kZXuC&x{mo$*gu|?7+Rx9xfqEjLUPU-I_hj39_-LQK&%Q}V&Zi_c?be9IyG;kOuB{n$49LS+7@gNsWo`K{K7C1GX&!67^JwIEWg-p0n<%pb7e9<<WJ_upQ_E$II;}P`u*+GxRvg&AB8LpW%hz9a@;BL(IhvDkKxVC5Vw+}m0Okv;TAJO#pWNZK)c(w8<8c#=ZS~n!g!KtC8&{?s(PU7ed7fui`sSw6v`ts?jSpl8p{k<g2Agc5o6DB3PGVS<!N}fR3oY)536m`CBhYn}VX|)?cwxCQ6cJeLezguZRh=@bU!C0Q|4k_%~91B^`9wP%q7)B$N8ckVEjvp)pbY;+Y-v&+|Dw=xN8ntMnArulWwDtOja;3Ri7R`%yj-NM3Q5mysu>bdz$&p%Oq3RsvD(yW);`qnMN=zhAOzO^EnO));Q%D<Cu`#B;Ab``66`xznrjo>~X^?ib6JUBt#u$m9bfx>gV=71cC3tk?m&8p2n444onKo^K<2q0HF)}&{HDUT^6}bvhCY-`dsq$vKBzrXrmS#IR-ld@fDKutBeMD;gex~KxULjerBnzmZbA?&aI=3QgUVgX`%LdOg-6L>oEQe0YJ+X&4QtMA-EMB`5?f9q=5u}45A)74Fo~Lxv6XcO3@3f|N*Tf=?=2syy)AX_`XTI|S$l=q98$)bQ1n4N|nu_quqO@~=f1mNi=l?WQskx7LY20X>6d#pErysBpFcR(l>L_a6Y+A$?C!o~1u%NhFQ52Yphq&0)4JU=Qm5|P1q(i0jRkN-;w`u1aJiAYi!RLU@vmx%XM!(fJnF6T%J3&vL%fh?g`+b}JCkz0iD3EV2n`459<WZkO5|uEi97`yl_7>ME>Ake0dLl$5-u~ym{QFD%_Q#iB-hF)03*s*5F3-RF^%X3C^0hWM|K=r+rAu>6t%x!SFGWZ7;x0dE`iJEYI?Df>92?)*_seCo!JiYjN`4U7M2F3Km^X-qnZg6v%&y6Z&!>xFDZ$&WpaLZE8Je_I$oG~V*Tl%FDx-58v%$ciuP@h6r`giK>6SDUa7`@BNq$4qw2n*xDysOcM{|%xpo5MMA`vgZ6G~R-iHMF6d5v$gu^Q`Et*8z~%_U<pCh<vm=!q`J`65C|sny^#st`l(4ZHKoZ<DKZc~~kk%tO%`j{zUm#Yjd)XQ<#DWBo#ijI@ig5dN_y1XgL9=UR3W#1_7a{_2NkHzSYJqqK?z)9TyCslJgN!izezIb0pSbpOk{ZuB-`6@R8|%%9I_c_gic@fvOdQR%Ial7Uya3|NILyWKqPuv}<rO{FK+QO*uaw1*8$9gydewg~`d?8<iqXgy4a2DWv~5Gg+4-4OAUXD8Lurxiq39Zxg5(lRG^cIRyj?1y)1DqN>&-Tn#(m6UuABdwM$%ECZbvqModojNE~#+d-$w^Vhiy_>L6k*QLJ5wYeRKdtFKMg(s>)n#xr8S)lZcV=YLFb-O+rad;=jGa_q#4t5bv)QLZV=4?Rr(-b&M>jn+o7+kqe}d@WkZ!2AwUGh~r@a)({D~4yw?hTc+5E;Cx}+<~KU@@vkWmB`p*xgV$H!_9?4S;gLc_QyPFT_@aKz%B?NI;miDF%-!MoiAxn748HRUQex@8xE$dp?wcaX$h>VtIem9&;dwFnFCdElm3On1Q1A^i50#;@Q*D$C@1kq>I$po3T~X$XBK)dou}ka0@OD}~?wKCO?4XUoKPlQ9yK?;k2>50MpjTSW67r8TJ4xeplYNOg25DvMpWdy;|1scpj53$C2e5V?4ax5F9|NWc?rYThn=k!?Zc`MP;G1@75`v~nk&^MHTUk-}P2;OdPjbaR4BL|%mq)S&{v<bPoWX4^WFSlm1uhf~y+s%B6nAAGPoK89EsoKL-4D#luLh<V>z(iv~Jm1mbisS1~a3<b!7&>n<l7ZHh0@xr8+A(kY##3f)&!N=!_$GSqjst&<bDzMgrCEF{xEbU||nN@(W@_?~a%aa>Hc^|N3Ki@K@4C3<Ok<0(^snyZ0GJbAqLlu<ydntjW<OGU=I@|z~{9}tZ8Sqj(LWR6tEP^Y!D&KJVsBeH~IXAV3aJVj_;g(z%lK7}j$P8*^&f=_m2J)=3UBH}4|EYTvX*ncya^=u$Q=5;uI-OK2`Ke**QODGsrgk<#iem&aYI*yBdUh^ePHPU4f^bi;8IEZ%JA?#l!5GY=$?OCx->haNYs-?k2MXxbJ1o9FYCzMWH#b0p&Q=Bsp7&gzavM3*cQ3i6B9EdehJhM|&_>y*tF7cIY4JzcJ?CLq5%y8Tnf^ONhKw)l3ojGDd@>+ULw35Tn{`|8Me8(J5`I)jU_>cnAeLer+_Y}GIFAu<j6s-ln>bjyUGclkNPcY_i&AzYH6|<ce-OMkWrw04P)CF%+SgIJEd#>wu>Qu4k6d-mB;vJCo=7O92ss0Qjkm*4@yXSO4rki$K@r*t#v0F63V7sjR;EBm(O|28Oq?y04^WCV1_a7X4M}LbS#6pWK39NF(Y6t(Bo+nnY&rdm*ir9@QK%6?Oc_IzDcmQub-DRi;x7su3CF<H;TqV0Vr|-07Jj-}DqnQAX~W~_;w8=Eo|nelqPMiBX`#?AUgYX>E5M%AfGp&|gSyZ#a4Q4St(uXPhjdsaxM8Qtwd3;le6Lx4i=MfeY(n8{8}uUu3*C^h@GCu>-)=L|zET=xMr)P{tP5(bbaKa5s*25l$bRAt>;U@RK6daD&Pgy>53=;7%QWh2+3GcqTD<bC*KJrOjJ1O1FVV;ZtK9BWrw)YO{z;{nNqXD3qyg&*m0MLdxIKq_bPKe#^a&3U*=?zrkGHRDJeEA=Mn6-zC2;^Y_6Pp3xd{|A%LDh{M{x?Ah!SndA>Ai;$V0?B))Os|B$@zQzhMYk%LhQr`h50nnf&rl4X(82xa64+BLJlQ<x*--1Jv`SPn;K>bYj%ihxGI(f}L*3jPMn3zWQ}Wj8(A?>Tk+*C`FF&K0$;*yTXh|fuLJMHkzSI7Ef@@go8@|(CtuwLY8aHkcGG#R&ugzK?@m+Qgw4Ny<I`IMhP`f@eiEXQmmWX9^X#ci6tQ5lH!b<P9Kd#%so6nAZ6-y;8oReIi$GT8H9S->>46tnGLK~RXT9Jo&P#ozVY25^Q<LbhUGhBIS8(BXmO}Sog8cq>CGMUsg8yNbLA?~p$n`7$bTzPC|i^RQ&>)#2+WhmCue)-TR`C`>RJ(o5(JN<*hKRfb9N1WB7xmme&GdIYJcYlvL6u?W|9X~#PE&wr9q>|8q=*M|0F76CexDLBXJ3OYprA?P!_o|Cr-6xmOJ-pGx|4k?_6|ZLXef>DVBoPCM6&me@vlOhhc1LT69l3KXcV7%G5|f9ZxeU9$u7)6BT2!rbV7Sy1>(Or8qAG7N!@|@*30}6ZqOGxLEY2q9rMU5f=INJW7BvYQmo05{j2)0GiK%*W7jf5<xfxzAZ=tE|eB2o=MXI-VKUXdk;a^4JBWfUP{(j*69~$YV?V;(^uY}yYD?0YT$1#!DU`23oIsXmd!1RoY{Mp6=b@CY+!{PLzH8|iSN3os!S#D_#^LL7L3iKv%f6J`>j{K5lU3|le?HFl}?>dT6p_2$tKQLOUw&h40sxzI!{wK%r@6FLx;fRI7K!d+az>PU(CX;FVr?JT`%cnsMGg}DqSEE*=yT_LB-hv7xuyoGH@s-@BZXahBRTa`c$}aFe`w;hzC84C#bNv<La>w5udf|A##VC;yG>$S19JD{JJt3hcUlSh9in|R9M8!X@#MVsW6ApqWzs<BE^NRwfP?CLuKDNSY5n}^{m&=!>#B@lPCj$H%wuiBSxO)dhkptJ!6g$ZA$I<RM5*((h#h!HTBi0b5G=jGYG5CS#n$qI&lf<$=9Y)N%LDz<B7W*s<=_5Q(TVybnHdz;fCfm^(uen%@ryCuPH9Un#7BW)uOEI^eIuLUXg4vMPXmE+T=7a&e(aOY@DZq_{lQhlRDcm|B17LNCfB4s4sf@rl{L`LBE(~xG=A+KZhjH#0}#46~K5s69ul18^~P553cW+mVZG-aQq=f4U7m5zAR3YLAwa(0CAabX$aMOV-!2GUEM%Hl`ck>PVBwe&R4!^ZWvLU4*9Tnb(}vc;ux(~kfGlAi<7zwpy@M;XXBGSfJs7}B}#wC<Y)w)b?3Q37)~E)hW;&U5GSwe{^W?>NJmY?VtrJXW!xAoQm@bNT4j^bO9UJVqU@UL=B*r}7_)?qSaHQvf*Xf4yHB=C*Y+YWd&x6`<B-f7&AEeu)?Zx>s6d4lIz^_DVma)&X%pRHWwH~g+VGU$HwdhB*B#bCr%V|dPqzugU8do=XF2G(osT}x>1gmVP3h@nJiFc#Sl+f>pEdr9Qe33oVMv<EMInx<CeWdpYT%o8GdVBhpbc>}?6`~SsUT1^wUq#PRk<>{1%9%gYmNzWNki1a!dT=}Z7M>QG*)1+KNz0@v8*Dh#uTY2#KoT4Ry@6?i4{{&Q*)QMh!8ZSzA9V+Cm+A^(_KMd@@Se99=@};)%r3E`g9r6MnY4Q2+QZvq{$0@OnA*i+Ryd*yY9(KKbz5~Rik!JHmX?WF(IW=H>ORjgL${#6PO?WDrPXqS-PFk$-c#@Ri+m_bm#>xz65EAa{%jMlbsTj<5PalXZ$l=xE@3~?6itO8C@q-)w<N#mp*{!|AcQ^St?;ii&sir;T8FNmTf%WZ6j&eJpS>q#PTX`-KOk6!k>dw92F6C)I1sKxK`Bn0IcioqP~o|I_9VyFXv&c+rgKiTM#T<VlX?EdM|(BkbaYR#IY;tEA*A2Bs<XYy8O<*fsIYa-4jk)OaUj{a0^;`-ZPS9Mg*mgGQW0rswq9oskv^k@Gm@htdr;d>mhUzy9O0V*C5vKQ)p7%iP$2md(^plhEYdl{Xd@8N_PTEBm$v^848j+iPgdNN#w}alR5%dBQTsk>LxC}vwQ&~&)=$8`77kZ>*y854PRRRSr^D;flca`Kyl63;ucLNzUOcrO{J2H3T({xKH+YRE%v6(`XWhusQC7nSXRCvs11!wgDl$P@*_&@B@n#(X$tj>GlTk;%nEIDgCPbNP)d>Ym6(zM^b4Yk5N2ciJiEkhY(S#90}gMS9;S*!glXO+YP0Sm<%nSEme=ZQ;20AWc1Feq%arZ;0xE}&0e+{S@+h7YuS%Wx>`l9p;U&Kg`E|Fx8Z=5-iJGQ?)(t#w<h#F*iR;(zR`fy{CTG3q4usWv4qL~>GGLRve2$z`??C`cB1E1hO^-K)hR|X^Y7aKz>dbolbVuYAnz>xgdkTF9wr$tk%_Hmdj^S`_g!6-ny_D3<4~}&CU9E|@Mwe#{Nhuyl)Snxyq~v+Fm3Ac&onA-vw?E&1_~{=%zP!1_#&-+#qCD0TUGgiwGS(W`Ft6cM?b1_Evh6};B%7-Wlb9AG0Vh04!U)abwvNB#0fYF{*KuWyn2Uci==DWd`t?;lC2<VR9b38td1^oKZ06ns{9_uFaoJIn6`_`--iDMz=Y~)XCkCY|uC;DhL_D&RCJFx6H9Korh%X7wE^2e2i^X%tkmVYxO6dw4*4(57-Iq4dSPm*oZ|zF0ntjLcUjp%*;M%Ef8q!#}q=<BVAp~ARHCzNgOtMbx#LYaF1gF{qRBA7kn^&ieTY`EiUnv+B`+F5ha7saU@43RgC75@Z3C1LOTvBn(X$&}A&npdYSw1kRjH4x5@_lg-VjS`o?!FCC``C~Ho43_`Qsz<jeNBG}QUE7p6c??T{c7^SWPuMq5ggU46QJo!cllxXr+gB9?MYatl(dFx+s9qPo$1BPJmuEtabvY7gDNj<tl5oL-S(=xfewwI`xaqzAstr}E)=1L7^tEO$vOjdLgq|s_=!~bRLErL6-X<9B5wk5QyLBRSD=2iaF}3lvoh)LGkC1zA?-%u<<|~=)1ye>J_j$1qlp6#-8ygE4%YZ8WNXhL*bs}{wAn(0a7yPRX~AM4CaXG<h2Z%Onz%m2b3}AaW|_mQk85>^FwZ9X*o*T4Ps!znoYN#WK~Ry%TRa}iRq3}H`1#j|3k8n1iGnq$^Bj8PWg?ZQ93u$Z{F&3Rhg4qKBayf@M&upwMf%i->QlddXV;qt1*=@1Gfqm}V$njKQ-|n0JUqmS*y{&Ujep<`vf|t2#}W0-NMcq~CC-;3%zn9<<?<fzMJmAX3!4pGu9q)xjBu%#<%>->`_1y*+0!Hh4MZ}SefQ(bFYi9SEWf)Te@x%~@x#ln%Wr-?hZjTeo9{qd30R|)VzeX%Y|~QXIoWm->UfzTtDYbx>BGHtkxB>NoW~ZcXO|V2QsT<IOiC%cEOf?xKDj-Y1iCwiK|LW0^Q&CFk#^Dv!qoQLb<jB`X0!qq`!tZ%9ScIx&traFQK3A(>KJVETZUFab^rOcpn9lmrl-m=RMHjw=rB~n0%Wc$Yw-J@OH4@qRlympElC7=Njbmqnt$DJ+de#L#2fe>M^h5k;JN6L7Kf8hMvTSjqUsqf@WRLdx^He(LYulfI4ne&RL}SByzF(bxFj@G@-;`AMsqRgWSxiL`FOk3Wpc=wyV+IH$ryyl14N1I5_U$Z<CR;+qA;0XskQ|zI}IG|!e@A7@v{IVV!NJVhbVIRe2cWAQ`#GlAI>197)OOO(_x`|nxa94GqQ)QyJuhOWkwIS$*LFp?7nUT=jW!esKy2ktE}TEJvB&5ixF+|(sUYxZ<~ABW8kvVIFSH4ss1HuiBa2zB+90FUBU8Lvc$Fh@-ok&MN>JTBxzu=JR^=Idg!WM9S0rkg|OohfNzWS1T)5EW4dmGu^pUw$Jmi}P%!V~lDYwfT;}V5yB~;3JUDoL8A-p9o?q-lxJo(v2BD1CZhxfE+T{AyIy9*pYAz?BxhxytqgULxQ}W^>Em_QU{ElzR1U7?%g=drrn`I=KN2*h|;g?fI!Cwy~S}cbby&$&dXZ!`ISVlZnn!YQmN4-9v*;Q#I?A3tSlAq_{TzrWwo``j(33h!`v?o3R?-sEf$yAJ#-v4^|k;Bns;X?Xp%T;1Yu3`AZr%DaS*zvpc7@+cnW-<^xSSN+wI?gxCEs&&LDc!Jfy+Wk|MK~o919~FPA+N1`>mbVY(D|@&tGr0Ty$Wi2+0J1+6e(f7)!{co8fhpc)!nqv2MIKYoE1~k%SEWM#2e8Rg>m675(G9Cv12Cfn-0=)ifEg|`7V#(3iIq;V)G6;E5Gpi3ra<{t-5U#%4EEPMiW{%<L26rE9-V>Ty?8U&(^Q(k~@IEdDhU;ErvZ8ie3!T0f}(V`u49jM^Xai;N*H0;!W&Vc{JnOUs0M#ssyV#?9q`fj95zf?PVlT`7s0z4Wmp~(dNn2P9&via$%~s!{s3Hg)e(l!BATQoK}xF&(fWVCE{aDPS$3qt;(dJ9{1o%R#jTo+*YylJ0vv7%=UC&lZl91vLMpI={CAV$(u`-f=$fGR}KbE^rwz4uL1p_7$?aD%g%feChBFpk3iMkV2Dx73{*<PB;}=K__r5uFaDAF&0f!hnQB;uJQHO$ft;r7rfOP@G6y_FK^QUN@TSfrs3*<Gx%|In8Wg{1UPvVMq1v0a_?A;JrgP2e3s0tay)6O4MC0Pxf~T+csZS;Lm%_ZZ6Bz9#bzV$(5MI?W9l^w9HV3JmWEGLonk@s=q=!TRYzfrn*$II$>jg6N5gOaX7zj%BpLuD)wR`FX!Xg|;U!h1IZ)~85j}$+VF;|1V;>(@0pr51xhBYUba%~@w1Kk*v;%h(?3h>t9TcKK;Jbn;`Ul{w2lhX@ML%3W@OcNmWgrZjz$0|g6O~;Mcb18#5G<Ier<elKFz~q4BUlH0H4!!(J55{amUzxjNcx+Ni3M4eo4VUIYIn@Ug(KuQj=fZ6_IB|$cO0ceLRzg*3vs^{!7&U^8nt=x6`9<R$s*6yI|I3F1o!+iJxoL(>e?jw6i<ALRbt#>D05C@R{6@{1#a(cq;OF8(BFg@m*->Q&B7sQOhjGejz|aNOG$t6y7ArEzN5=vlu50-k9*gIREv00Nt;iyXha6DZV)HnNV&e8yH=F@hP6FXbZwrLH-OBr95oa>VkABvu&3tLrHxZsx8KJqg3zS%$i|tpY8svE)RpWMvc{^5^AP0rRRIMgwk1cx?mYSW8PR9V8lU9oZp_@f8HSa0gP?3xk$0X7NhqrBk8^E32)lIHgTm-_tvB5>EP475Voq#P)W<p-SQ@C3eQ;U%ES_`u|Zw@?4zf*#_H-bwv#<Z5n_%$FMELtFO7OM6kwb;F6%c%+RGD<kH8aKGbr@ZKH^kaXvDA*fF^{~wcO@v{3rZx-%Ld^;=&SB3{Uo@;2u2e{7Q|}@(si0&omARgh%Q}iLbeY7-rs5}+pvH@al&FIaf1f~9w`lC&yoQE_=rHOuR`teR{czY#Lo2fd=fx*bYty{0C_tHcA0=zPX)*|06IU@DytJC&ml+icHb^jVgBk~9GR0|dRKNOMyI%+#-Y2CBYGLH=rcL5+3H1{lA4GKDC#Bi14|~>7yia@`m>jz>ve1tc^n#0Ii(HEI_FfQZmCz@@&h$TnO+?;$S2d0(3T^QX?8>+MlT+{qj?&$R)XK?eP-6m~QMt9;6!?%FrI}cFqC`Oyu5qBK6yjqd0;6K0wSI2mWPzfuMINW-yh{w>War39oR7F4lKg_pKs#sC<dbRp=)=ZgDfmKhtcI&)i8t{Onnp6SbL!o%?|*ssbw~evJpMK*;bf{xrH-_3<Q(nylbKOm=`0M}hEDK9ae`S4Yd94v#-DEho2@BFS~XQP7S!<9IV+4^UON&6Z1BU));(|bz>x9hgRorDn#)7(1twOQ1`H@kg1XL3(jMa|zk2SXzAVC1W_;3If{b;qDil-^qc)x<tAsH*a>uA{4;rT{a~@Ra-oH>H^VsQ$9C+!`UUELCG6`U9c&@W!9CF_8FevVv4L6_RI<s7z?@Y>v<R3%`OW%HlmO`eXk)jZt!;v9{G#~{f(l|>^r4vs<q_Fl_IdpWZAXsc`Y#ju#ff;mr|Gk|;Ib+fKrC^GjdAydi;=u6Yl*G}YSFj%$A63#Nst+fpsZ9TyN}d`C+cr&HU!7wP$)ty$GC|_$FVH^%bGGH-g0tM$KeySXH?+q@<?{M51u?WbjJPd`^jv0#J?z1$t6G#FaJc{N&-WjG`p4&O@$pZhS0kQlIbp`7v^Nhg9!AB{M>K!B0#9jCnM#&s@r2_&F#Y(hvPgVPU?2|acK!t#m#7O4>`Ula%&RU>5+4$Dz~tQm#<S`A+_T$>8IVrMAzwUdAaNr3UZ`y&x8h>*>akAryd#_<u+|X&V$vuX#IUky;_Zy)+xfOePUU{WU9y8KXe7azAnFK*%4Li|_6g`L;rz+((Ul-Ek{tu@C@L+g%|Vs|i#oOQMVF~t&hoA%aK+BYXCXfwL5UnVr2bPORvH!CXU2Ib#*d<y)**BK@i7cMYUu#Hlj-=9(yf#ukxjJm;|gdu)w1ma5<YH1SBKFKP&1ODmU{%ZarQF<CWh9SDHcsDLvm&s%S^^Fs_)06NkW9Ak22b_bA-|W!aafm+rlyr6(j|{2a2@8NG(^n^_DI5n6TU!9OuK5*gvyID|BI`{no2&qNCYpSQp$gmX%#K0`UwHg=9n@PA~0%pcV;<9+>>baU`ILAQVEAO^I2%7r~PL)|8$M`nE&}m4>CRsZuU`((#Ic;<R+psEk**P!yo9{bSdZI%2mIltLv0`3r0~y>C?VzW=t8*EyFnv&m%~2+Qru)|Ilg9*DmhJD4)P)zm*>Y2gHggxSibLIq4mq;J5q)#^yRU{>kZ<St)Qv(oLiI8zmk2Z3UO1#L&ceV5U(e28QXZj4S4ss$V)Kg_=+fl5IjjW{q8F_n2U%z(pRyz?awfg~wh|5&5ykA|TiU~~9jM8yA?J&UO^;;F1dQ3z@JHr@HWil-|#){aXBbcCEy--glV;K*Bzs)f;mxfG8?Kf)9kjC}gH!>c3&?{(T0nk{pqbXiqV4>n`Q&t}SK#Vg9zD9vWr92}#D@_ufzTY2S<bAPn*6c^nxg~bqUJ~mUc<mqgNqQD5_3gik*eW^4+++)uu8s9x#V(V@3yWv@Ewq#GKXuuTr;@Z-*^*#+(S$m4rz22G-(9?a(qOaMxM|>$oJ32AdQ3Z}0^mUNu04;c+0!MGQhLt$opPV_)Ln=xO_s>;sah_l-)H6(uwS|IO#&}sQm-AUH`M`O1?DyTz9Zd>XS%RTJk*nemI*ONpMd?sRT8rN>NE5QI;V2gu#iWQ*VTT>TO7W^fZ8?<Hd#;>80tPFNrK3tfzlsm!&On5i9DTk)xxWrU^2MC_<e{7bJvVM8vTi?x1C%=%%a_Yv>oy#y6$;r`Q4&<56xGt8w)|j=nxe|BYMVkqFRu-XiY$+wy2IsPH-_1_EL%b9n|GDppkZFoOwq%epU(NE)JZgYx*Pmg4H7s6QSy<R(}A4{gg6{fQW_cr+#>XdwMNiU4xoJ6MRP!bh-i&cJDXqSGCuGApGcpT-(Jot50v_#xyZ|)F7a)p$^a}x%qSy1knnb~Qs|CJJNqgroZ*Rxpl|2<WNdBv1gD&`rlbmkWBGS@LN~o+K`TwvGe`lHPNVGXkE3<TCWRO=m;@_#?Zp(OP-R3bNa;o^&K(_X1l<B4yBG_O&3rziJcHuFM=4&UxhsMqLeU^p{d*}1<w+;g%9vvAy3B@1b~!QQ#xL4xq0<MCPxwrm?Jatp^{VZrFZAlD7HSCn7jHfLc2pe8mq1U9+G7J26c-9KPNJ+v+VWj(&n=A<y3LoCEZq8Uvp0~zH#uOKc=JX_%3tvSbQpv5`Yam~(e1y`XeBZ=x&W7c5hnH89oXNE%u50fcbgi>he#(smL`z;$&W9mkshDsuxc7^oPJ%eqcO1`-)#%Y)tq<1ms#z)NhVJ#%LS)nE(3!jP<H|ywIp6?CThgz(UK|i(*v5KN)|tp84ZDFmNauTK<qm@en+^n+0#PZW3p8(aewPlSn1`O4Y?|t0cP1T{MrtdBv=<Dn9!_Ytk@BBOg0>UhX7w3O5kIF2+AZ39aKSU8?gxko1C~T`AD5N2LosD=LnqQ#?C`;>Zo&m2@?=Wx6YJ&i@dOv{t<n(kxyg~ccYK&DvZMtzb1@%W*F@h&Cx!4&B-ee`<FszryR(1%V3iY6aL_VoyS<2OI00Iq7;5ybR>B7vZ-)8oHmtFd0M>mA5*faLr2@_!;}q?dDf-OhSGLtB{?AdJTHtb`L+etDp3g&?!X1N0N?7ie;3kxKxGy5A5ogps4B-17c`1fA{Zvm3BEf#c}fLRCRM=JOh8YPx3z3PX`zjIX3jDaU)9Izmn>@2GqriJ9smqtTO#Rfj<nzjnN?K7wKIZZdDPEIKvNUs`CdkfY_i;eT8v02J@gLggwh<#rW4onc#e72*AZSWE=abq&GvjkjrP+X)?%k5Zs@5YUte7>hM4kBY6D9Zx={UM+S^T9YeBY*mK!?@Pjg6FYD?2s&|cvb9_7cgzvs^dtQ>+@KBQ7sm`akKI~IUixqa(vqWB7|fCRgyd`p8{{|(hzdA|SG5o`S}qNv1~z>!3~jqoWulc?^g7qfQdP&q<6ric1h78w1udY$W(+xx1VYbpwUGg;2>C$hQ7H2yjwo7~mJtf7ocX&PmPZ>OY5=Hz<_X%^?^d+KPWG4aqcAJ@yI<s83McvEdm)^1~K4BuWdldeWrC)KZtfm(1uL^DpMOAhUcXto%ZJ)+2MbVS-L%hDHR|4+A{&~m$?B07B+UJr+31d(#MPg-m%ks9|kaw(zIN!MU0Eh@P!49un_DSVSversKx)4!y`SN!jIEa-+&ML-rW+6X7q?xU^}ML5_ph65x}I51{r&+7b^e^$#)f(?!7kn8qwW^;!s9Kza-jU9a!8mep2$L;u*H52w2*EU+o4Zw^PX4U3C4oH9E5#3Ob2+tT+;KoK9!C?UUa6@$*KPLE1^b6o-02+zL79=z9FmAd?ADT5`AfI?e;AbW9A^SyQrx@d6Iv=g0M{m_bQS5|Ot7y2w#0@%HW}A}FU@Y(Ex*iFvo1550A3V}0|2DjSa~oJvPW{pALYK~-d9~h7d(j3ZF!lAviS4BVmPq;6CuzX|I)IAA(lXvZ?RtIA$-<#yto_As5gdooUA(+}*^YvUTO>58mmT+`;FkF1Ro1k?i~s4N6A_cR+ZwBub`OJZy>6}_UtWGIvH^;xc#IY9TQW(rAOzLYw(IzN><3E6X+*tuYshOLOhL}ZVN_X6@qNNvI;Ib1I%tRbN8WJOXHjPTvq`x|bWyRV7-~f!j;B6*ja5A8$dCP&HO8i|wZ;}A6<73^^A}0vcBt$k>KtRTq@g1dddE(GR_{%M$B3IpuEEFyrFHI>I*2p$xP52^i*w~V(o$oi@9rF1_){KmuHo0fQ_}U2t$)uf!!&gp6(z~LV#&QzwNU7tXEv)EnDCIj)3`J(H^tlWM^wF?8Q0TNE!rVg-Mu3CDoR!ArlhJ4nov`JD{(c&o#0t!*``6J&|Y^{y-T&r;s}`nFD=o*YWdj8>G}zpBW8UytH|~-4HMBmWBZ<^?JTaaXlqHq;zo`lINqtrdq{eg`_~#c{sGK@qA8yh76GEw7Ep{%Bl8S#_e8!$NMtL3X-a{JEFHk^X|~s=z)80&(_-)x20J$DA^+LKci;nIt^(tHaPX!=V*x%XGq(95><MI$Vl{q4Qb&oP3MXQYT5Jofg}g#d;Dl}4yT$VpVcJ*tX_qgo*2WrvCMtw5|FEr1N9*eN%0K`S^d+IKwCX&=Qd3fFoC{rFPi9ix)y8)g5RUEecTG*CO}`64Wm<%+&2k$02)!21Fs1Zj4Uxep{l9=gWu)N>iG9=VRie>8iKR}`KYES+l7d4n>ozfb;!7)z375rPeHjL>SDRU{p^;9lSCgsys)XkjaJ$)GXEo+loM<&#236z79ybkTQs7NzDc0+Rh7c1{C#Tk}<kiKNw_TGvb&Wo!j{i~KfMwW3)fW+3+WA=M)#Rpj00kHopVI(K<Ug#Oa&Es}rpfrUP7g|&=Zy!A;0p92qQX!bz6ex##t)Q+2FVMWgLU<auLN`BaD~HI7d%zw>ZG#ZMu80vOx3j;Ex1&Iql=}I2%`5o8B2iHby)c+Z6dB<DwK)Bd6R$|@1^amUlcP*{MK7-hqOlfzOAI|$Ks6nfz}F{>4K`Q43m5-)OaTNUB(5CBF|Q-r4YvAtWMSkNDN0-ii>pD_1MN_!J*5;!(}4Do9>I5TFU;@I!h61r;xowsKojzWSnhZosM$*)eh+>Rr6>BDI6Jfqt0ycUDqsNx$*-$(v_B_8H?ZlF1f~C*VX5>YJ=$Xu)2fFO+3~-YLn)>#kPO!bnoLx^2mBJPaFehN=3nz+)wsE&4`%?acV+E6MI{r<iH9YV6Q>IcKLXAZ!#Vx$}N%u5H3#<(s!U0fu@IB|Lrg9YoQ=7!El3`y+>Sh^Sa_bS(!|PBCY}*wy`9V)U_zki&TgG3T^V{ntaIi0+jGj?R`_KS$wHVNSPn@tqhGUHn>>R(jOY-?H8g*99Wg+CJRvZr>bgyrT{Wdv-FlHdZAVpZ@46t@<=K`7?&nS3sUvx^3Guk6={T~n)ZC}+-}8Iny5QTdIf;<bd5YWKP{QlB(yWmD>VQk<V&_)3OOZ-c|oIjSc+<|aC6)qgPylARsAPZc5wqK@_7sVvIF@tH62s#Pps%?X6}U)p4I=T)ZOyr*17oZ=D9co4EBW%VZlL#WJ*IIZbQ@agMKhi#ST9HRz#t~$Ew2d^33Zap6<RAI8;v&XhQB?e5Y{VLjWYoRcIRNPMj(gdFxs<;1>e~sWE%BP4$5`P5avEbJrBRtw#{1N&FE=R0|dY2qjR^hVC9r^OmUp&MfR@Yb&oYvE6_kfTWmGyc|Uv0w0j<A}m<2><>7z@ABYA9YTYG#@AH6v<b8as)4b{_d?6;q<~G8yI_Y^CDT-EnQ1^$k}ADOn^|XJX;0>Hx)#*>hHYP{L(XB|HrKOK6P+RBZcYG}4A`c9igvP&$b@ktOGZO2wttr@6U9`GXadkCIN#;m&&Me5foX&hML@%<1HN~aQ`b^lxGS;fSmDNL>PuUkNk)>84RBtYc-54YGNNc|tk9aC-W_Azfw8g~tz38=k5N@ep|=M;$~v}Z7M@Y3iB}vlFc`9Jfgx|gn){o>AS80M+iiKiM41bQo7}Yb{VCJOo6#0>yEXse(FoJWp$QBxgInS%8h2n4{spj~$gdZQ+Cp_Vmg-V`K0XUMC|exuj;55)8&k;2=%jMaD=vHyuBWLmBX^OwYb`GN<cn#p;>ujrw7W?hu2d;l`-M}2u0^>m-?>6(L>UolyMSbH1c-82Oqr|>hX_Qc7p%x>nf6u0aB?&4l<#_8aF(~;&RWC_l<=`G&{ciJUJ}FJD*jqq$8E8?R3U^<<gc?^EW@F1(bdlw7UcY82OwR+Nvc-0D@|}5cllCAdFF+(0_IH!uyw4IJMs8*3%%N@!8~n*7Gji?{oA+eL+9<n5&;dCsk$;h6}E>u-NICIj)w?D;)3e(=(rc-seJ@0R*n5l+hwbvO1C9JLUt*o&l76x8+x{5$I5f@9;c`@g{k;gQh?vntp5s8?EflF6O6ST+bBYp36XhE^y||W5@0Ofc0sfVBSKqD6O4N_GA6ao_YB2Q{IPj_%Xq-!^pt=N%<R+Z=x;Q_Q8mnJVBf_=e58X=yYEWH8KyFKJ!FkZj}TTCpijRRAv%pF)-X+msJTIA^fK2$uuQ>OsMDR6ywy5xRfV>nN<aiOL|mr&6FSCxg*4QgOQoX*2MwNcaxc=A<Ya?wnG+Q7pp$_ant)^TSOzIdVJ@5-e0Hc+UZKUSkTIn?%IvKqv9PB1IwSmWt!1XhMGnw4&*@W+5M^|m*o0qW(DXI+m^R7Dv02NN(j|!bu=!N;Ha7bQflNTNt*QseFB8G(GaqP$5A$Mp7c|G)!e{rSc%nE2#o|GG1CviL@FWoKbC367ISG!t&{AW;Yx}-0bQu-t$f5u{(xNnw1pc`tBv%!KC^9eDqNwW0y(JCze-)sj(?Eits}#y$C$b_<YzogC<#SHN<vlokPg(8cIcw;JQi5P2m$?VM653#xVVbI~ukmE!3C+oF_4J_N6T>fn6kt_G#)PG5BTh#<d>-nlJ}FD;e{?a}4zoP$#?K<vMAnj4n}amD*BCEKnDvu&B#(Vw235*u#n}YPEYz#06k~~B&j}|PjfYeZdpntz?J4VxR=6A58k@pO=LXVLiWxi!hYt%}!{O71IUi8VOb!cm8sJa$Vx?#$$`GFvm{?UETvXoq8sO=5ZlJKHh&{!v46zUtRxU{b@MZXE^urpy3;EcrZm~+&zVkqLAq8B1=c%vy#o!}0d}I+<&kk!U==FYprmNUWIqczk=CBK$1V52wm3d3oaL@4z%=`xl@22zoZUx>d*$1(O2mx2}8EdpLon=47dgE3aPz2oQfSPD-Q-UJtk*-#7q@euZKnEGIdBvM46m|1EShE5VA5ZaEJYeY;tx~GO>mzO-uKPWxWz=EDaDsp@W>hRJR!f<jCP4Fexsb>EODU1krUEed!lQ`#HI#%JGt0$E#KshOhxnrF?MWI!Rv0UIYl}>})wTtg47Ain<qcb%aO!Adbuwki3ZyW6IvRVwu#?!Nk*F@^!M-fee52MN#HsMQla!rfM`mUEzT>E2&ma>|yrbfW-99W*47J5^S7hvgvBm;!+%nobeweO@Foq{QP;^d)8y0GTy0lXhi+K7}=<5g1w{i9vRdz7F8~jJwd}>G)Kqo)UCW${vOxbUVMQm=4MKBv!m{A`pU_|~G+N}T)kcgU=bEINFq|}fx4~cLit@#r78$JVtk+K$9`8=$wT`_j20}PX=G;xn^w;mYl>$8^%U3u<q8|~2xTW~35^H9Y5Io%MgLtIsX_<$+kuzGdZ)pwOb$}wvsu-IU}(Q3Lc$Oo`;eF-*{QdwwEX6uG_@-5Gl8mdAzBQMIziXC7h`mQan!a<foU21$SC>6<?a#YMsOF6i5nk7e^7?8#qwEzw0IqR?#r%Z-!A@V|A-9{R!VO6P9v!wb$uM;YM6t_4cow^+8g07_1#grYO>gvtmowd#z06}}}SLn0p!<z^M`q+2I^-h&PE%tfbe;I%KuIupOcHA7z<B}P@^Cqs^J2Fk?3)Dwa@2?QjJiAcS3C%|1*1LQV1pzJYow|!k4OvA)cXwm#3UG#fxb(izQT;r(et7z{Ce)$3`fsGi$k_(GsXiwj+zRA)90GWXBz30ZlExjS)K&D-ddf1)1ZtdsN!%ZWFN3dmSOHfm3J9eR<*GwtWzZtj;y8)J`OoPTO{;32RhoQZ7Ay8!e91Oq`o>bHp|DIxJAUn5SJ_Wl^1ulGz2)N5HO*FFT7f<t>l(HU+|RW+n4$+b_EKxs6_zxnAZJh>ujQ9c$MN<t+6-Z>-K5xvpY!a1;;IIQKWgAuLLC?GQo8g#dkaHgppf0r9yHd=gbK!fw;|}`6m1WrsjyC4=xh1LO&QTiXFLGP%U?AEAy&U;l0=HO3UONAb+ui#<#AY`k@k?m<o8gxaX>#Voq(?orc+y2Ac0rls=}~z)1F_+aP$&32456pD7KvAdgecs%A3zg^!h2eeQS@ZEqk*d<*E#(7`_y5GyYuZdVn^jUYkc7W0>vJE$vsDfe(iW)I2<l5ltqz8p2^bD(@+eVD*w>o0;@)m~AK+sNkZ##r;ZihZ@LPr&{z1<|40v7l2EVXHCQvx_LoJ9nU7k{VU)}`-bFf1G=Vl5|jsrOd-+f^DP^Q4s0H=5^biBWyjtWxGtoTYE61wYmJl!&to}gqcPL1gd{}W(-(AP)kfB5)u5MKft2DK8!j5{MF6_OgYj-aA{c)yUY<<KmeQaZg^qew9*y#eThU$V(DH~T+FJld!SRFY<yzw5a2|R{hD1HZWgB@z-WG(nh(96bQLrO{v?wrM{McfqzSbg>UjE_LPhuug07D4&_O&FhKgp;s1>r8+k`RKM7vEf{VSw}CC?Q^R#ZksUtcA}%;_&VC8m759(@pi@*l`{MQ+<hD8Bj5?`tuE=D%4JxPnn3!VpQ4bP4JE9tg-=<-0S3eG;llLoV;G@$FjEC@YY0kP09!5>)YKPN(~Vp*N&)|TdU@<xv%+meyLKUq5LRbV@?36MZ0<-EA19?h#np6Pp`WMaA6VATEC8{o8^|oSOJDi#t2e}W*VG!387f_wv5Y1#O2L^n#<}o{NG7%39;<K0uzYdIxfS^>_*jd{FW$Ia_2y$G4u5HqofTF3V2-v!hT8S#)?6mYe^Db?B?DiXDnBz;!#nxdHBXirpoGL?N!a_a!mL_G`Mt(?`2hyC#XoM)9Z<^Xv+7R;B9%nY72Z)7rjyfuKzSk=rr-6m^6)~epv%Mb+d<Qk|n~oN%`c)ACp4u`>do3xc3hmr=)u=*kJc*>^3KQ<;kyUC%t&OfZznAaLNhY%B^(9^i*L5$lIP8oR<64oxBvjaMAHwlCL^ZoR@$D#pXGq7@POsu2y^IJ=x%`GUY(<QzN?C59W4n^;9thOi+O(6TU(%0u(5P(!CHapSy27<G)i*Y~=1EB`W9;l0|dmXC&B1_nJJ=v`Pu1$8zd(%^1r!<&4a0S#!vmv`Mu0Xlo6an^ZJiv1Hd(r)=*~x`uL~4Q$_R^?-$TBjH55BFx%^7^aglE$bIKhulpbj<aW)dzLN?(>_h~E1Y-plD<+tt;P8Q*XrB1LM5DSMur#mK{VW7oi*NINfpal0L;VUu3Cd^pw^=u!<gtNU2aX8hg6}XYdV^nzLu~N&p4sgIxoAJ&PyQDm$zzF(7(62RpEHDZ&3>G`nX5jKo`pQLytmPvP>t86n0Am=`MrUGOJH($akcq-Zv1wNy1D8QB)}Qd6s^EL5J!2WPJMpl|-w|$gSm<{1C{Y8MB0#?0Eu7qZYPq8WBT1rnVqy3pxZizj`NvIl)|azCe0{(C5eJn&9UTsjp-DO1N&o(Jxei$;g03kzu3{0<=rwhnCkETKWa*T>EJXEyZ-90k(Nnc5{taaWbJI%3ENpe6|sssb%CP(<xE3>WrR_=f4>fu@--Fn2b_ex<)57SjV_jF7zo-uI|<$W~9m2I`d`$Fs088qAmJJGo)e(i=MoWDUi{#0_o+E4Egp)bthOCGUMoo7qmj`pz8YK7_HoJzN*AyvY@uc)ttlCa@U~eqpYrz7i7$`%gv`gZORsfq*=7MdjTQZ>r$@Ex4mVck2lw7^IL39!@H8p`8F$_@7F;FSX+@-^<zG~CSY(rnf=jH&P~^DTvnM#b50?C^`%PaXr*|o)m-kGA-gJUYseyVWfN0%O=x1&6juEavo>S~Ia6VQ;%MFeSU-RBBT7-q9LI&!tDx5~7p`V+rRBp#Ln=l<Dl7IE=*#KMdS=w9O+6;_f`k~0h(=!N%PFx?(-R1zIlslC&CHjdD_A{Rui$oGgrSpM=e3|<T-s|a7rI-b7z2Atj5*&CRq;ip)zv&g318!U^A@YZ>~RXi+X@Db7L>XZBXk<2aC9QS-J0#HG%boGZ;@Ipk4lHQnWa#l696^Ms)W6}xy={MPnSu-R#C=y$uj-|IhSWC)B-7(O?>)DtUSRvqpYCPqH&%N``4@GfLlqz58)yMk+Js1wsfi4q$_tz=Kb<-?|yy%%e$}J;pgM=H$)XVrtQ6Udr@5*+rx0dBkR!%$`W`(ZUbTE@?^wt%X~(f>qxSjF?;dEhAh&r3t!XN&v(USAtoEZa;cf0G5)em<>-p`Tr}QWch=RSWh=(Ec<uDnpN_=vhkYxi5sOt}1bKQYJ*8lx07xlVj6|qIGo%9(*P}dRS+0HgdzZtVWFmStks>-fE#va!5-0^hM_-(sm3#!Rg;wiU+Sv%q4Q9x3Ip!8|i*0nNiG5uGO+gQkXcm}F{KQ;D6Qyy1t7j4AQcHM-R#*aL^Uv)}qgxGS@V91la&76Hut|9g2oAZfGGdNYpj4Ng;8;s=zDbrWuo6KQY|eO$H>|Tvr|m9rl31>zZMDY>BNg+K`(>~Dn}7QK<u^H2hi=?=^4=EG{DYV0erxfno$E%;WvA^xd^%(+!-U`kOX6h*F|Lii9Zu`Skt~t7>Y}`3FhL+*;pSaUG^D5k0{0tZ9$g02Ps(Ku>9C)1pvgu~Gf2zUm-aR$szviR87|Lt=GfC1GZcc|623by-;2$!^eYLjb%J*nN@5Lu#1w@kBddDbsbG#)5_LJ&7T=@R%DJmF*yGMTCAk7+_xcj~1c_la2%10u!Iw1Oq5SR=5n`2bg2?-#1AGqZNG!*##=w|%9Ril~1-*Bu#wQMas5Z`1#VVQgVzD18#eK$N$Zn*)*9%akJ>^uW<m^{=Dc;~kyKhAUQZd2M=>wAK_PE*ki4O}{ZliXTRh!{mM&<tH_~GT(Wz7vd0Us;#!+^iZg2wBRprNt%Uck;~qh*($jE>@5hSykp(9+|ekLQG|7%ju0!}_-6TmSawX2Mtj>=-!J(6CR8!O!RD<Y?mAd+z%1hW_~?cV0lyWX#|<(Jz2Q+-nlW@3MU;UY_c2f4=|l(?32(A|L-;#?2B#$v85FeW@4iVQ_8Ih{iL8X8qtrh;q)F`0^4n|HIU7jsgNi)gnch6w%O|{FnxTrKMF~;F2uJGDrHT<g@2>mg`=o4v6u`<0IHYu?y-<Y21{$4lOZZtqh*Lblfc1*=qT8p)yKZ*5W^*g15vQeI~x^qe@!#Q@7-$`m9{JFk>!Qvv>ziOk88hNiJ4PXoXi!UpLi{FK_v@Sua|%o}?-w`)@>Qq!c>SFLN6IZMv15LZHF&4u0Thc7#P(jCzKUx=0xwG%y?HC)UbH4aau6ZV)Z)n5G`3t<HwR_$sN!O$X18!?JWmOJ*H*Sjd)$Q>-Cn`K0DgI}GSQqGDBzF;L*i9CeUF!KZbqoffhfLrqETBj^Kv-OI#F*AhG0FNSo`N<2Dli^L#<NoF1cfPqC|l|RiFoQa9}ksTBL<GsQ0`pTGcdF<BTI0z09K|K}KBlrN_Fknj)DlXtHrKKlyJG${@5_}axWvWhi%&C>kE+Xf(2m)IisKv4~oeTBbSa)hkeJ<uZ9rr@2*tjA^3bn-n;(u<oiuESuKUN_|jW=(Bw!WOi)3F|o=|}uX`7>4ZD!`<S#<$=+w?EaUCV)R)@NHn%FC}(8+}Bu9Of%Mv24)1Khx;_(&a${me)swA_^Dg@eyH4}q$(CurgpQUInYq&puJLzEV$;7m+wYMDzk7pjt`V}6qc91yj5B};!VZ0avCHy*1;O?)Fsvp*Kh>H9f;g0gBWKGTd5HgVjzAY)$(bW0~AM<c-qa2q#TI;^mq%jV^JE*1h(e@scH`OE^a!!E5?;e%Z{bokV|_ci{s?@)VijRu-CdQY#$>mRzswE4n60-NUUNfYuZLtdU>i2m^Zq?x9WGCcHXUf!?Mo56Kms!WrEUcWxFFvwUda_zq%2VL{nE4F2hV%E3eW?jG0zR;%OacuKUXJaE!^JvdH}weMXcb!V+wnhMaXP;mA;C@lfuF%3AaoCQ$ovnTQgBLrSw@^}+SB-$3N>bm|1nN%#u+McH-=sj?K7*Z@*yC%Dy32@V24<<OJg85s69-+L^qEhwI_vW5!LJ<Y(bYDi3ovduz^x~?Fjkr+6#Unw{y#>s=Iu65TH6DAwXk{)Xc>VOaekU3Q?s}mnS^y9-Ez>|(pzH<ZJv8;I@lp-KEP<J;BuPJKEC6fa8oi^M?VbzA}A9<;GZ|BA6l*%sYM){o7LMm|<l9hRlD-g43U1k(s*O~{=7nfEDS2JmoY(P@<t&ha=qz6h|_D2d5;%(W6P-%WQgx+sDgJl&vnl^Cyp`YP1hGFCZ@%FvgDRku_S^@+f(@<oQF3k|UeQIKGy%z!Q!UB^NU|WfD1i)}47v@D#EnQ6l;M0#7ABZhh;9~Bib%2h$DSYYFp?nTMY1}YL=_DL=S)OiCYOQ3*Hlrem#5TCMf*T2jG?B5hv(?u(f7J{NGjmH%aonYNdn%72by`6{)zW|iyY5)2kWrU;cUuv<C$ke|QcP(zW1W>sodt47u{-61KHMAy0<h{>Rf)1wfuX`W4C!|CV4TPu9F~$v<s2+r=wu#hm9xsY?#g2MYt5hG$)YH_%m^7Q2FTSm_5HS$W+)nFTsh>DC|gNoHJumC=dM<&COSB|^KfIbcV+(`%Xp!nsn|OJ`ig1+f4sGz+CPaR$+-N;UtO;wdBQtWW%Qp*aG)Y<LE8`hN^RPl`EP2pJY=-0ht%nokT|z1lOwpPilfH5MmvP0WmnnGK1k}MFcc$WiQ5<lvy-+(bQK)spdmu`o@PmDjmJR{S0#Dv8AC1JVyoYnLB=IUNkRSug}1zlYOk&Hb5yj}&8A~Wf^gZ5YgmvJ>kEo*&3L4q=}RHK1s?_&(IPiDX~QecZF~9K221iFTFZHpSCs{<VY3>JYn(>2fXF-Rxw<L^>FfihK+C3(j(r<hfc{MtlU>R;2&%dAZR(B7OPkrs81X&E2n)roBspcw!3()E5fm4^1pj*O@YLfnC-e~jM5lI;==kp~h_>^%H#XKHKo&=*_W;XH$c3zHT9$!Qp=SYXZXy;ggt1N8lqEUcUm)N(23Q&jMttKh2@_3{-g8!6IVWPbKQqu$`3A(4jpoH%;76&P5mcDFQ`ZqrTkFR{R>8NTB~IVlW?xWpd%C%WZQS!1p<=>r13iTcU^o??denu}IU;=si+(Zejji<s701a#96og`mr>)vHbBT^<+c&5Ka>V<N=AST58rKF6HMl;0<IR8`;v5`<h#xyxq|mD^DSS)frLf{@sz%tbzoe6^y8=7Jc*(T8=1-|liKJoFi_mct);?4jV>%19RBqF?*%c{cB@Wj)j=&kHMCmx==U?{PL2w(qF`*#+KP`M#;#86&7`$_nh#%sd1z{O!*o{_fd5sfM`TLaRGqKS@r721af??HYnSej2#P%zc3_J(#~#-apTD1D<6e}@Ovgr3_;|v$uMV8~Q8?~OY1CV9*k|6<%%mI>gfn+yYct?L)yMLeA~uMLHyyUz_Z_yN2M#hA6a0mB+DdSE18hT(V!jDkuF*!%ITr}QKDxehm8j0;Aba3$!D`Vlz&q2hWPsw^Yc8IHFHK@J=esoc>x|ZG)AMR1Uh%WP`0>6EVqqTRa^wZrmZ^MN#~_PvUs!|$Wg`7_cSL)qxAM?tARd}tnUGFZ0)aQzAv!_WwgQnqlU6851eh*%@&M{wFoB7@tLRcdXf$@3F)ngNZS4(}5o*j`G`pkWaaYug&-mO51AqPw7&wgiQR}SJsJzi`2dSf}F9*e2?zpZoMrRAgMRryUz-hodM^P}?^kZs;ocImM9>-MkXYw>Id7SIv0P=~V0nZ@*eKMWQpf)}WMUwF44MtAu>KsKy@K~YI*-jZq0ft=bd~`Y_y9{C-azpL+@RrBhzY|^3#39Zu)$AMAFD6*7p~YsrcA6Ll+ueIdhREs^6MZktUY?HdQ%mcWz2JhnYZU~|@iEd%D_{*$CK%Ro?QU7dx5?lQ3T@vR-)Wci`03~g0xb~xCK7H2%9TbuT0l<%W2uxVn`9qu9tp!>eP2M$1x*BYej7$_8`({`DDrmPNzz8KSr}kGK0J>rd<S-q!C0R)yhV1%bn5b*YR<Z-dRD?5AN-OjKMrQ*6R@d1_NLIZ1m+rCksR0%E2;tV`pLz~W~Sl>s3jfiOi{@1#8QZf3R~BuR)X^x<z38;sW(>Y^<kAWPg$j_ft_vE$m$^H4%34m{n@L?h09kxUn6Qgi!O2v`ZghX{QivcqsOcPJJ6w=C94C8B~b@wF5KalJsiFHw|n~W(_pMl+LO5ENCDq}=!e_1wB(VpPIXNlV?m7PJ#Y_Bzj<XWj`?n|h?FucSdW8b5Buq?u&m~SJkDKLXl^m!RB+sYvGP`7uP~8Nmpc}~M-vyqVLd<2jGiY$*tKCe?`69hGRSh<!)R)I`#uK}K2o0tt~x@?KZZ-_>$E-v+~r~DfzSx-YSlj5l(?+L)cs7F>^<;!^&~JXH*APG#4f8=CpPr}@OuILD!9s;mlseaF@#ghPqY+lJ~~E#W9gr`4J{ht<cn!m;G4T3bu~n;@MSW(OCUd};2N09@H}}dL1o#ha;Nh3lh<TLb*4PSZGQ?|FVk#m{kjXix##Srh#O@4a+<kLr`|-sZ1+LNfg(GUC6AO7&<m`S#9B1CcGgBorry_eu<BK2bB#>29E;Pb)a^!gx-e}UaBNf<cJj=7aH#AUk69smRiVMD(?<p#fK^?I{w)=urKID9vG$I(;&~AW?anf(Z~QAFfmpJw`ln&CF-i8wZCeochI?Mp%F$Re3<JjbnnhFO82ttK?(tKLj1o^cp%O{1P<H-NEWOe`L;1tB6|kv9<UUo+q|HyeI9yeLWDR=IqxEJY3Z2D#)2~I;N3Y^_J>ywd2qt8<Z(S#X;TaDKUV?kaq|iB^=7xe((E-~cpcrzSr4R;6N8{x+s54pV&s8DBkyusmFuBy3<*YdlX;9I6s$3)}13t)46i=C}d{SzS>FQARv>-6SaC$J!ge+KbO#uT`MFVCLE*Yy*{7!DBO~pF^<$MQKa`N2keZigihZh(Y05GL8DQLq1Cog+z!HoIdE~xRZ7#hlDYEhzm-!Do>#RcGa54vv!0<&zT8dXRzlgLY%Sv~Edzp8@4kBEi+Wzx$I8<ctCgap)XtcjJiLm-PjVIH(OCB#xb?OsTzfn+Ll4^63&m6vK#uIol3h=ztHO`r|Q93@ZZ+ty@(3T=W}OPtFSk1+fn_yvHU#cfi{7^F@iHcLSTgCa{I7?SB82iw}}qPc=izf<mly>h4}i!jgpb5U&$QJbwW9v(ww`b$JdUOUa|xuod94yKAo0k74er=<ZNg96u3)Z%g}R0a$@0jGiv3A&x?RTM#oPS2V~2Q<@m6QwpjXFN{?VXC32QrGayDtx%ZFU0odS|>%(a_vsL)&)yAmKhk<@!b}|hIjm+$lGgzQeh>K$bZo)=7;~R3T0B&n1$EA(-vlhHk=8^ej#{7Ml7sE#dvCsKSuiOhZu{zts7^JGolxCoK0M;t<pg2?Jc@cUaDaY)f$R~pg0Igc)-Z+bE~hqJwhzt#sXA1dv&ha#;nWD0#86JM-x;KCa|jzoLgizZ!$g|Qr#|8{WOUXEV!dEZuIIw0R6pSb}oO4B~-46(xcN%D%O*h?*PE6rNpOT0Jb(@9!=Yjbic3FHM&?2&qe}DOK6pnC|<>q;-!e%4|}V!0c&lEI=Led!adr$oM<My=!yZgI0~$m6(dpBic4IOTAj@(w|c@E0yR2dh>}feB_#_=8ISsO!76&@{91MH8gF`%&$RjEcVjU_n5-}wf0P)#`@=rO_8AFReg9GtD|D#_VV+IGWb3d3Z*iM;zcC@5w=;Y*RAq`+ZAQ8|<#inja1o7FbCQa2BzT?q3j-&9^4N@!SaBkHuGI>X(a3n%Ya#X2%8U%=PPw7Px<b`)GXqs&ZfQ2lu~g<@q~+vIaR}S5W~Eb7!i?SG%ml&VOvAdK$ui6uz>%|b+|mbOXH=YQwQ6eAJIfQ2^PCAv(a^1=)~ZOo5+~Po+et<AuC(8@>bg+|OFKH7au0shJ)>=<(k+Zfu;daqs8|SsG#Rc(^8{gt2WR-!-iB#~G^FsKJHQPq=bPHWk^feZPwXsmxMFw8y&>}$ONCb4qLjPRZFM=4qp4%W$-eH&<++;~CT+j5VNzW8yza&Osqzxo8d;h7NaCvELAXN_%d0aUF8^3?C*-;ooUg%dUyI(B`^8yqPH8ypcT)LWYn$$XLF<fvheIq+f6ZJJ5juGL)_tD<VKza~lE<kfDt-T{VCkB7u(7^3W>iurb!>E648ja>jiwdzYG;wx#&MqMP1Prc($lORkbv0u(a%Dl;?NlpE8&R)-2|SzV@ZSX&D^>WSyE~<BWW^&vqrrP@Y@Be4n*69qdrq3EL}zsCn*{Com2r@WO)O35uRMm(c}$`lM?rN*Hs#0DPb2T7l*>#0(uVUqkeq^ojn|C;B8e=hi<m>EEnRFuzvX)B_C=7Je`h91~$mNN=bt9WUS)?!G$GFMq)cTxddu=A+~7r6rp7RvoV8}vW^q%?8zKsu;)*OWlva$CcP5Z$SJ;8LhAYX0Rlht6@9v46G{;n+qEg)VdP0Ky+#-N+PMrS$~~CrY1wfd1^bC$+3tniRj(k5I#~u&SS$rYT!$TFrAj9+`hS>~*3*B;*wK{yC6@Wo5&O=&^4zzVNbH%NY9Log6EjxMjR$6D&xov7X6U6BpLNg6lZyihX*~%%H>?%G+Ya$xf%nJi0FAb%6SQ1Oo0{B)F+#d47@bpkgJ-(oX1~kJYn3`W3mx2dDrI?=iU)N_2As1nRoo`cY^|10U5Q%5&B!wvv(p~G+;p?L(*8zuCEq8B$=+~*iR#arMl%N09dX%n4vTwPpN6etz1;CM15~71x*rD`2v}Y^!kfjePE)l<d?Ds|5}o9gnyY=mhVyG0ksM+aOmO$nl~E`Yc%(~uoe;4DRlcQiRZp_eRcN@Ey4}2&7@Q|bfFX9ElP@0h`Nm*?%hJ%<D+@m$sO394g>uU4u%MrsiK=rB5?CJ<pIX=M%T|1oDk4_#(4IsU1FNm5{#}O2%lGA<2f~(#z!E8*T66)n;S(&r!R9UP&t?T~;JIShC;99tWv{GU?0n$gu}m5eR%o~AoNMt~mhdmsjI-##pyom_z_xT7HYp*@_+u_mc<<C%pnDx_0(6>c$gi1}NY6&r2|@>uP$+{NEAB6~piRHOGiRI!>`l#Ze$+SmO|pvKgBG{IEhEH_h*mP1l2FOy+xZozI8%*m!fRo3ttS=~hJ>t{5Z0OtGd`E$TDigr><wiiWkBMfwsK-YcZ8qV>Fzv64x*pa*H`w%{UaMqLZn$Y5RC-f(~!LMI>zhjoNM5QuaO+_06Q~V9bh53!X^oQjkqLA^qY~SLG8CGPzgGQCs7jLwkm+B5Sl3%<m<W!IYp3tB!XjXwV9&bf&_Zr_k~K0ICJ1qfBRM_(Xn02Dq)t_8Egc~*var>_moVT=ethmL+VyCs;%`LHC^H~IQ)P+`zLwa=K=iwa(1}|-+#E3I(Kf~y03U4#r(}{HE%x&wPIt<<D>*rswmZ3>EC9h<|t?RK&6GDJ5oNY0Kc>m)4wT5$D@`^rtH0yWZ8HaG@NVF4%=R6l~ZwI&SMJ*SCC*T<0L}q7#@LL%h-}lYC0jGydAb(sj>5uaizNRhtyXsoo(J$c=XEzU@|g<s3+M7LkZZ0ktec~!D+Twso(-Wp}df}=jsYHwL(7=UE6>wWU9>c%&Sf&)<RoUnKZ4n$ub2jewv+MZcGW*bnZ5>uZj(z(bohP2`)T}MpYs*$)F}jHkS@@mRK*bIVu86rAl?<?Q;n1cO^T6oO!O!lamy?UHRUYWzzs|Ob_Y81?2a6K4e9O$K?Bt|5uK%%H08eP&VN?;X$89BATb*H!TaXZzf@JPJo}2?{9C;LG*iwOhtM#mjnVr-6Y!Qi?a@AT6tnNCM|HlAG61JV1jh1FJ^t5R?C`a-6Av5<vmg#E!C&zB1<kAjTPJK118M`HGM_jT}%0}ghXk8#!ro>*+%qwIXmd4ewSR>KOPJu#c20eMqFGcaDFf>iiQOkhelqED5AnI&q}D-_fn#n+VxORc4HN#1QwE>Tyk)pM_cwpSB)EHFF7T2acK~S<#QWoxTxlt)5FHR=xtS^x2Nx^$>QTi9pS4nUj2o}){C#GX^H~*nbI!gsn3I5OQ^1IrWMP)w#VEQ;?Ub<YOhtmB$_XWt!bS8x(gmtv4iXPkAMIB8$<3KxSz9~-+q7j>CYcOs^%l`@;qknJZO@j6yula$$7Bws#p(@PK~9``K3AAXwfBi6yp9u@e2~gU)t4SBVLWH#haL!6%2g+mOJJK4?OxQ<OF^Y2!lhGc6jltLEqim{`3oaC;IA)G~?*Y>ru-btqtDfh%Pv5?9RxD_<a^|F@MoJ2v-LQBS-(&BYq<+E-FabGed-`-~SfA?;FCXUHs^>=^I_u%-1nh0EsWeduDzeZwe&jzC&cr)Y)|CDGzQtJHMn=d0Z4vGb;#iM4GzL+mu1oDyPT0kF`Dau9dwzWcVt;g$;;9k(?leK>Xz5fL&DE50s*@#olOu)JTzsZKt1r-Cxx9dh&De{piNAM|Ya*@d!-eJYtI>rAf~2XoB>RR(|XdMknDk1ew@&sqjSn_#lP;+XgZ5g(N}DB1t#2Gw{{3W#7M@u~-2^Ti(1o{Y}_DYRb%fo$uXPXmZ!D1m%=jMzBq1E1j#gBNp~7m)%MDha%ESMOm7{sJ^$1(=1nOjVARpiNpHvYoy-mgOHXcY44-%+G!Rp3|aO2<g#+=+1!r7rlC4&B~*YjUci+*YMrn6J2doR?wFtT*K_sDaq`LGgHFmKhXf(>-;-ma98UBli1s<KczvB;{^#AV?|*ss<=6lI^76-V@>BRmcqj<F)HVtT*JDS;>mc=Ef6t%dzF<Z3_K|nOBQ5$aq0B9RG0mIlZ-2i3@Y6qjd<ov-aXc4qrPts2{QZxA{yz6sSlsbymbZpi(%WCY&LSnWT)q{@IDOJm%?CsqPB+C}7`*W+m+(Q+{Wq?B-je87Q#W*ACN6!{<hE&U$!cMmth|g+F9+3+FQ<7l_xgnQ6)sinXsVe8Eq4-KH{sBNhnWn!K&-4I>etu6Tx=t<8lUCzUjF#`c>HaWaGMthQNk7@=U`|o)rxlMd_%9H*vHzFB3zjMP>Fg4juY26_;OiLU&P*MK!WtTb_`16VzsXM2AL7f)r}qOZzJ`x-lt4k&k>%#gAm_g7Lx8{XFDq^<MFWM1Po}TbF#}s%-bIdXFUQQ;x&3-l3Hr}0T+)nW1OUohPUh|dnC@a@9v5Qyd5e*aancN`OR$JI(!7yo=uBHL_9kqNC+sO0wb3*FsZ`k(Bxe7EzZ%`)p915#q4I91%OKE?Dx0&jj9~GfOb4=irRbU-#&hL`E@~YjD0L6sCuCfQ2-E;*)jveaF}j=A<+jJJXX@H7!~qn(w-$y9&vkjdpVDMD0DRxz%gZj%>`>wl)#^C?3vFe>*R;rKK<FRaK;)TjV=C4=K|aGNVFBeGxuF##;V1+j<;1ZNiINJ^221Y&vL%aY8Jb;YvO2@SBYV5q#o@7^#Jq)uekgGZ4jy$V3|%yM3aO9iNem-K)b?~sgLu=o9pPF%2X=Epy#A2+Oc1rMlfP^zraoaw%=%4VkK!&V#^USit&12Z-Dd5+F+H^re2r_@OU>`p%IJ#krF_#q25IX@NLUc7LJphoR{;z<J||4vqc!GR2q$41y0X77n1sI`}&JeZ<Us?_a(m=shzeFuBn_REZ4>(^B65qc4dnfvHtR<`*BNUC-f|VpQ!F>H6twAgOU^h1Zjox!2p}Ul~O8c2+L)bFhv2ii68J+cGsda@7skQZmX`+<qMJgEN)R^uNe;bm}3xbU!3ENnENGf&Gtfo`KBB)HW5ah5D5CY6(O&=KuWUK`66BB6_f-URuDQLpl;EeU4NN21eF$vD23N*RSAI?^0S7~-t?fKBeDkzeWh`rFCbucvC-;!0F>d?0*W!2IDMjzS(Q7Z5u(G$jVZKGdbF*e2ooiVxnX$*sk~3;l&TP3LU5tcf$kl@amDSXjTup$&}fQP+g5!X8|QX96z6h&HMi%P3j)-2pPs8%{=<liIbeKK5$TdE`{LeZLK(YSUla}5QTsg7$y}D)+zph}r<ipeqX~*z6SgT0v=`mCw>(Es@qlG|LM|0~3?B>vol9xLk^rf|5so1P#U?0_kY~!&N@&tf#QHqAo?(*oFH~&1Qu~ffzViN4t9!(>G(G6c3ZY{r^ZsB*)tRwPGGM}?0imaKqID3x&T|nDYsJ%mKNvhgz*{Cnv?O8!=%WI$nC_YC#Lc@@`bH|eWW)|E6*G@HwhCRMO%`r&>>=-<+X~QCqwAaDn2Wa3W4*Vs5O!uFW>9^?{2TjNitI9i8K<UkQyncUVy7*INZ6=g3n=Mw`y&yDV>y=D`GP^{!Vtb5f-zX_=5j^Ddl%&reiF6(T#F7EuEmrf%9$aBRrz@Ll_XjNYRTC_Y)!o$cOl;9K^-mzpoN_3r45zq@W%n|URI-zEbTfC%AzQ;Ecki~0yUT<G=m#pe`>14CS_N<qf8S&6bix`GT0S$2Uj<_xk|u5%uSd7n8FSKL2{XbLb;(5J(CK^sqQUG;e-(@o5<%6J%c_x3|9T}ThvV!uZB&L=?@x<Bb*8%{ajeexX84Y*!27R;+2spV41wpNLFd}$iKCi`ZP+YPd=+5&C9<^s-n;!e_uJ|8TbD?ko`<{j8v)BiD3cD&oAOby#l|Q_yG0Yz}^~Ld6y?KOv+x`k)WU^USfn8iO#K6z+Xv}2JsipYmrb7z^8lcsJ7sLa@eqj4<?j1shaQ{C)2CCK)QZwCnyeDM2M_1-6vOcslgS5feUMKj;7G}(_D3Y2MgyAh{smAA4tG@SR)Ei^5CdRbGj7-(Y%UDGZf^Dba^lC)aG#_0lh2`LvExBI3D3SCFhTUg;{N6i7Yv{=U@@|tqzY9LHa>KA=$(fM?Sec5gFG}$I3!Ko^5`iOB2+$S)YB1s{>DB{-o92S*l(_Z(6(9n-{fu&Ed2ef)>`%LqEyhc9u0QFiyQp{N2R>8c48>#KP6OyDB{Vl=kKsJh@g{OeaDW$PDlv{$fTdt!_S1w&u=LU<EM=XH$+aa72t{LiXsDr$+ie=L`RWwn!!z=|y+<>JF#^MC&MHJ9oMy0Q@9%CTz{d^&LZ_WbwCYjT8QCpw0&F1CX?OKG4+LR>fB^-d4>7SzN&AQ>4TypXzZ9Ha@_v@#|s&H<HEKXA{S(r^g~>=NK{lA*b)-4X6h3X>~twPQc^EaKFRUHy%s<K+zA_R?JMZIUH}5o>!w{yGyZD8grUJa%6ZQ_+3EC!L$W($4e|~yV<MI=jy3AntJEYB`bMq^hoNH<S*2>P30W$9eB~BmHJ(D{&_OFUNR3lTJ~e|;N9p*Pm%(d_#(i<wTfAdtVtVuWc<8{yMeMr?FCEtFLfNUEzn~uXy!GEB^yayY;QK(QGjauC5h6yHYTf<GI|p7sqoHX<+M8(9`-AwCi4Pqx#YanDh<}J?2-$w*nc;DnkPejZoKmwAymg)n+WnpjR-m;i_l?Xvo*1ISv@w2KiWwq?=YS(cfT=5iPu${zB#qGqR-2<#^|$(J_U6Gt7o)3DvGSO?WYn7h;HDx0M9=q<1`Q7h^SWw0wj`K#EVqDuK25(uPhsNwgZdqI_H<3A;KqwPy_9s>a?_H)VYFvwP?)4jfSUMUxTUICocM;Nig@-j5ff;caS$RBp33)k;g!F0f&=v1_vaOQA-|<E@Ep(N)e>ZzPS|Oqoxp$=@^_vN|bC$9m@+n>lio`?wV#Puc~Q%-T>$S;&no+8A41l;<!9BgEmo8($G%YP;CvxqfE4COiWb4mbEq=x<Y*5RdiNvGq+^LrDY~1MZt;!ih0ns5R4F(RVX78b-hV>YfmQIk;#SU&w3~sGD2e*NskwvwKD94OXyI9G-4$ll_M66JvB0Tye$b>Riq0+S$Nrqju1Vu%stIxq__#N&rEPFrFlEClWVa1H+G{e$#{^ON4~IR4Bp22G!mDpELF3w2<KV_R~~)VVR~>a)k2^&=rguPh*TRwM)<S6XCYXYtX{e4pGzf7s&`a4n&NTIj@5SRngHEL1Ek}*ki`>T`p1lA=59ZpW@JVlRMUnR7AJw_Zdy;d_^}JETuyOQ`$baQ9j15sEFxu^TZBDH@*``B%Ee7f^;AbhDW~I~b3X#u;ce&L9ds8bMAkZ*q_n>>N4&5Y?wShtVmD*>&(!+?OGtu<y@#tes}dKO%V8iW5qvo;f0Z4{E<Px>IK31jdZ=rz=bx+r^2y6^_P>f$5cuJsDghsyykqdK6;22ri0TT5QYGVN+i~Io$K^aAh~mkc2N@>Ua4eJXcdHA>LXR=Dr=^0~{8vq`m&Nx<wZI`ROH0|bsBHp3OkE4Vvc2ZQGBab4#!1RAk!D$pEZ_T*NuAj7T=XzSdoO=M0uK`QIJ0|o!N2TFo&ii&1I68(+1x^veUG^;q0!ylIizw`<IFiwk0c_;wQu*#!lkpRRW2pdjGI>#0AJm-FE#?bHe!*d`DCH?ISD>|BOkmG{jj>53OLegB5#CEBlRIul}WN;n4HvTFuz{}^WFK5Sm;DqaUPh9e#9Y^K}#KF8Njymwu;zgNUf(kNFq-t4JZ~V9wW`;;l9>xASw?^43YNe+2G}!v_B@7X5^i)Bzgfy8OioCs90s+QDQpHq1mw!w<I6D*ldB0$oqY0E~>=_T;=e5r%fUyCwH!c$e4aY{X)S#B}=6qB8&tdt0xlGAipINEb8PSkVlx15yrc){MLtxCUYujSLBTMU?A^X(oXTO3mXZdjm)p4wA*T(4GA44^co0F<Q&u5)ui4wj%Mv)6(B3S38*|QrPl<B+gNNASe7ZA!*HR8o=fMUXM|xlJvl1H*dQ=x4SCoEk!q3>Kq^QEPk`{6CaMB-ylGmM*S|HL#X(UNI0xd42=pYZD4U_ufa8pn&23C==eK5^-Rf4oCPQ}~c0`HSzCCU#;lOEKC%>n`L%q-$K~Ns3thCIkxcm|)`O4g(N`e3bh4tNtwkR~rO_XX&h$)4$;;-5bT<^FMwi8L{f`DS~tb^a3MR@YlPQ}3Vy=g7AyU|GpV1S3of^rg0r|g9lOLnzNfuO?CRvMbKipTMH?H!RcD8@z#4p6;%Rhc?3w_}bbbc$tnq~vC&C{=w=sQ8IzR@94y3)@wvn;9H<W?&x7<<joG>5ZeVxWM@T4vI5f4m$`%*(u2=c~0dEoLUpe+2<5*qE66g%TxU;UBQrao>EUAuh_9PEOGyeQha0~U9)!I4iU5%av@w1+cWdW%9V;Eq2q^_U(XhKX$9=-YJ1GCx9ymPM1Reex@OF7J?{n&Cy4$NhZW#MK9k7v((UR!)y4R@G%wseyQdL35U<aHw<MSyyukP%jy-7oV(I-vlAcQ~INxC+W(hy~RA#kgz32{9l!u^}4vV>j{LUff7RDI3EyQT|G(PzNe93;2igny}{@wixI+m4xhSo8!DEd^E&?$%3NTUaMVHLAo5SW7VgJkcQ&(AwUYqdPJLWRt%<MCB$>W|&?YU>nSPh&NK5K!d6K$QZ675S$!&D515l1hbd&B%muy@X0f+!IK52p(St$0?jy0Wx=Xk0Hv|dmNrL5djAcZvu{|2DLG+Tn-0|B<G<$apY!=s&OO4aaT==&E%BUm(3~dxn6g@hzrbWHK(BQ#y_o|Zk|3d;dN6TIde6=Qw>V;@$Zx5`^)zg`J&ndVKvRtn)qvDNKPf$>Q2sxJzu&_PE?#6DWhd9fyxNCl>(Pz;#(4R&CuC!UhEy^fkOSw%2uK6QmO=)j?};Fl$r0Tq?*;g@b=H;-Noeo0K&mMxI1%9X&C&DvoWNGWapV<f7cZYVR0Fy)e=P3*lv%dy0=~97*g6yhn5JcGw6dhgOz%fN$@+pt{!iX57&Q*dNtpbE^I~m{KC>~dIMeik-v@AGwDA{rPdPup%RmS_8!w$s7rc!NDDG~NXx%it6;>#<+0FC9C0cj>VMRp7+!nI<0`&I6e`YHO%n(j94eLj`{}vZ#^%Vp)(woa(g0OEd)7OYxtanDe2VoaE{4gI^CEU;khA?%@av9fMadzBMv0Otwk@onxDkBiG29~@vxzh_8(lHtYE@RkU{R&<?wY%nTd9}hKTm+S0W>`g<UF;;7^l0^Hah{}h0<OD7e7d4oL^mhGdnv?Y1=o!<4m^YsS#J)SG>dFIYePZ8(x-7xfo#VM!-doqf%o?NoU0B+Y)JfG~78nvYd!bw3&O=p+b^w4yKkCb4Dk`L~!I;V!rWj3i_Zv(~Vuk;fX<SNw7kUEA^h~1TBx8;$FiB#g@l5xbd!HJ(;J3*<`;<GhW{#hd~aWpE>;t6(7*)quqnjP=zbNi*cr##mSTSUURF(Hzmxm1!Q&cXCaH#$Z+nNr2H8eC`-fbRmvV~JOM?}^_{(jx<dVZ4_bs-8}VG<Yw^eK9Y1+=i8*v<x)O5H2_qzl5wa~)<n?s%+uVpueEYZ1G?=psO(5b#d`zaW>_i*)kn6=1sC*LYCBe4S<ScB)byq44rgLGZ+pb7OZ_5;<z)Lmz%WC;QV+@~2>uDxL1ZJFocO$O=ja-DPj9Nll%<>k*+H9M*EZEwo+*<rZvav#f4`RYEr<ZLpK))gwp0$2wquTVB0yk-o41#**Ek#M<8W4^xn=HY0EKF^y(~XG#b3>peL}Ingu&%}|11-C}Qk-b>sqp@2Qc3h$sqkT`JL$2i%Ew!j3Tm#ha_!WVoJKvBkD$a0+1=SDMW)H>rY4qmqTQk?<-4jp>($&VyVC^D8*M}!9&}cJO`@?!#G+)K{9BD$!DESWMzJ4ocgqbMk=`{C2T~+!dEg|nHjDzq^SB(AY|(ES%*C*X3u=dSg30Kw=z+$UUDB1|cwkgnMS3oCzCzZpY1TW<8#;Em;C2OF!Fbw~XnI-FrG&MRBxwv78~ycnrpt3g#qaxS4GPm>tJAN@$Cqq|$(}cjn?hAI6<pd|iFE$@V(+zxVJzDS%{}eUu(araB}LL(6I^dI=i%V!F*_rtsgA?!i+5bSm+S^?>Ss}JD|s?x?`*{=+fL|+S@HB}G)kQ%L3zDT^2~D1i`wca!sj`;MobKn#SgrI;s&C)ok=K`gds*ktGLbShPtO6IK!Ii&1QruT4D`{=-lT^BCrv}@+c*S;T_{)Bb7j-^|w^4ugQl=BV=0NgBK9A$*U8Xbiw2)tl52Xc^z1Vv`v)0cXfGBw9^GbO2Q}-pIklrnK(M$B5U^_mo(a%V8+w7l``ktV;w;<7{g1Jw@uMkBcUOKgei_U?e^8TEzv+&S&8lnE)V5YowjM1+v2g{UQ19dItcx_v?Iu8=NxJ!atm2i)T*NHinFnIp9<$xK~s?^^?-duO<0N%Rkr5tjWu@xxT??*Cj(kK$RQ2vnU(?!B`fDM39FQsM`*Ey!s)Ied|@hcTl?L8DR{S7a!<Z(VnZ1!?`|L|-`;Tfy*%Na_rh#>V%inZYLBd7v5tOTEHF7HqnUgojN`XMJUxyXMIPdgsU^ONb&g0;NX#$qMYPpCD%#~TVtO|C+%dE6QMcKJN8|w2i?_D#^L@7$37k2iA{md}#5Ml5uZ_cfWRyarvA_^(ycUYN85neq3s9)jq?=?dk`Gj6JeK*cM@=}4+$QM~kAYKcBo)tX9Xt89!1%GAdfH@^>JpDyiimTI@h=IQyhiW21nIW$6e$DG2lh{6(nSxogR=(}pUAJ9SA&0z0ox^!Uq*(HH_-!}1bMB3x9=9^bINmEDn%4NyD=tA_g#K<l6qTVnop*Ac;;?EC{Hx|mF75?$4|Rj8z!hGkzP8aSfuHyml)YW%xo*J0|+r{2bK&Th^Iqo@A>>W4iS|(9Ge{a+*c_Yyf9fwNAUJX=aS_Jy-2+GEk!p1Xi8JpDIE-BJ*HZMXv_2|T%x(-+Pi^=ivXiz!%)hxtEUA>kMzj&GfWFL6VnAzB}{S+r=0U?W~aj-4Dl3NG8}j7gIT-MTZ0(x(GWW+fLLB*`nHr7<m%eah>+(nUK1-=@WyN<wMwfhy7h>HChQ<}6amf<6{9Gi4JpvxPT9|6t?N^;+&pvr&FLO?qo!>L%i8;ht{>P$`oS93&`wW7#q`AxHN~%6-JB+fGYe}&i}tXlak=+hHGjEHQ@aGG5i|h`sz)tDF+V-i>3bvUBX|xYB2bQ|iI!|CJ-YF5H#QI$cme;<e5|uISuyyr1Qjno1S-eS<htN!9pYOa^b|{6C-=o*uY&?FIP0(QusWj`qyW~iFg%NTmXUbTpx}S8_cpzeEIGE|e|hUzgwgzSSzRS`7f@BV(bWYl9xi(I)&mS?R`chFhpq@kxY0<OMJO|r*MaU^O36cVcbbv3L-L%+9tt-N1#I9vc(CI*a?XgQN!R<;GR<<6U9M`NTL`JF7tA`bBgDCZdDiMKa%>q#De5Z2?M)Y9u_XJrU^a|7@W~_aR!pg}-702lbzOqBYs)Ck;Pc&GnTw3+JT=&QP*uYTyn@cT+oZIOvDojdrGq=~ZDWl7h+_|im4kg*dY)0QMVH6nAU#*-R-%Sup9hN?+{4kvMi<WPYEd?Y>$L)28?T1fquJUYTb|c$7vmW1%d!=a%Xr&BUu93*hgF1YYLJFEZ=q1}yW}IIGkbI)n2MS+{$~B&q8E&ip!u)Af7@tmdYAu=u@j$SK&x|5R{~EisVxKTeO(Ht?oQE8Kc=v<rI~uw96bH+heaqNtO{}SMNz6!giw(|40KB>N}aWyp6V#MO{_C3Ope|t6Is-UojgRE6ujAq>U8nswz)D=CiwJAJUWrqwkK^e$1Fe?3PdM&#@o^ZY3YWlkOo)}qnoobdQ_j+jA3j0l1f|E#$v;$-Eo}2!0JMEGxM=6->zt3yxWMsTSHT%V=RtleX*EXk6AiZ{<W_&m0xJY+C9nvZOBiECdWKtTVFH~6Gswg>nLQh4!#A+6Z*?afdhP>URm31ROaY4!9kZPwWIOP?47RD{kCmsOQq-ug>a+W(~%ugJ!q8ME>KdSK<7@Bqrji8jjI*Aqf-8c;J@)-ziDvIWy^nD;P!{uM1|h!cZD0ACXwo6I48IJ{?sKptmw3qdlu;6?XoGa?iWyH=0snGVG2lxqo=bM>|x;2<n;8~UOt!20~n@Obg7&it+8{90Izv7yS1Eq(yw^9H`HdYo}!0%sMZMHk%+aTH)eRWt33KPQZ&MXO!U?Bwk>6udYAycL`FkynqW9(T`1qO@Sc*=%qBZ&Z)bYWS8ZLh7G+!HI~Vp*N2fH_3$<2WZUOcr`cW-VR6lh(v~wy17Np;-*{DggwU4#u+%Wv%pe7-C)5s)ux5yARD7LBv2(xX=Y~TtJIMvjI%x5rET`gTypY5PVIv#}&=juN5W<V<L|5JqOg5NZ7j63>_4#GXRpU>_Ro=9MHo0b&-%d0Uz1G@-PmbQ2by(9GUP|dr{vZxVXQj~edB0DiKJ5@{5-eH}pU6-|1AH*6PF<7@1ys|}A30e~vx7%`R5zyIa)u#@t@3_NsZ}n6%K55d}?h`>3!soz<!jS_eXaN0F?AN*-m7|{}7xNa=(rf7r83Rw%M<H55=%wVdl5sc`cMq*G(*lj)bb+MYZX}zPsQf@1b9y?r@l`mgt{$JOf^gl$yvUUHQr#j^4z<AOwslBWpIf=ET$j5htQbzTKUJP$!=C2&oe8N}E<$-s<?&R^pc4&t_mnM6Y+-xxCHQbH!5wV22n`}L2)Aot?&lYbRTY#5ux1xl_6axDdF!ENt>%C8`Z)4<x97_fh~p9hN0I2>Q6w<u)#N&ABqCOBKgyeVizr^(pF(J(b$PrMyawvDQfvMIbkYpXgTiLzG^_=o#6qW`Xta9bRAn9b^h7;F6k>zbU03P}dfZ>rS3rm<3N2cVSn+bL(uJc=_U$Mw1H>{l-<sC|=Zw{q)x`3mJi^`?TN^8{;X;kokFVLI=zZvLqqd}{RZlF;GM!r}S{ft_>yobR^Ip|^wbkb=#aWXcQO!)O$Q{F+?wsw?V3KmDc<G`ynrFF;!c1*8QKoXO9NW&$gQ-$wzTwfWV2_=|gTME4ll6EDDdFMHDb#>%z;The4D0jCW($Jj>EW4x_OBXfm#dkwK2cYoD5qH4Z)mck2x{dQ%Hj31Bvk1<Z9URjf1~M(HaN`HfG*;Kp7p-{?YDni3gfnjV=WWj7&W>R-(qX3_gS!A-`&CVXfhtB$hMm2Y|0a#C7gV6lY$PTa++%#P>DuYLt|Z;=Gmh&#t9=jfUBHq0t=_Qbmy;HI0l=5BF1OTtptJ5@(|m2C@U$XvhS5+iHk!_?zYYPB0E*bRdHn$Ty5nOt8E`)+OI2~XS^+As}uuk7jrkaCygHeP3hB$#nP>MP&`J>sofIp7Tc~iqIdg80@<w7&q1}Of(U_CnCOZ^Ge#7R$ZHoU)9|Xye&t#_P}LI@Uqw{d$HwBQ-P+&KALL4!2Tt+x_>J|x=@BvSpRI)b@dV#S2fNB4VaKt4VeFzw&?{E^v*t=W!YA?<L079i=HEsfx+VpEll+?E(9|gotvt7xk_M*swYsL82@D-m<#Wqac{w6pL~%>-Lp#N&A}o#CBK6kLS5fiq6QlTHqTSEXrFgHOUOnfg2KyMW+{}7r95%|*iRMbn=@`3*yOHlO1-79^!x*Lx=#yNDw+MU>h4%&)w+0QZ8q+{m^e!Ed*N{<55WTHi?I5*MV6%hTXVVJ`JLD$mFS`P04X4#QfA`(1K@%vlC!a6YE?8A2y!#}RO87n2**N-bvP#LsYS*hN1*<!^XNukML8Z?(2*A2DH4XSV%u23t$f$%XwWE^ixHVCbnsu69p)G(y5oQ>(jZghne0Xx{WnGBS+v&M%oyfKG#p><7+89eiYihu2JegJ2NUbf}zIS6STRM|oBJ0!_YqK&@O2;eeQ%`@}7q2m9Z%gxdWWq|}qu#OAOV^@QiaW%Pd-We$y3s2H^G!T(xyoA+5XjUI(e8qoT*AGw^0X8&etcq^VUu2!)}#~d@YRHZovE8B3U>aUdgV(SUg^SFW2~vS*5I9nuPXokLdxU1&Un(b$$NV~UP>jo?0N3fP1aSCrw3G$UsFZ+8>$7T2UuucPL1_DsjjZSj+E)Ip;!8X@|WLR<T4~_`F*t&zm<UEo?AXDmKf6E+w!2ZnI@FVe19MzzPqx0GEaGr3-JxVz9ihQApMs5^)_BxOYNH~rZsjD{Yt87^o?Z4eg$!{@2gDpee|bl<c2lHsfuLN>#7}nPfa6TzvxxveomeAN3SLe@yfjYef<32fX}|#vKyi{`VJ)WPB-%M9r)H;+4dgE5WfL&`Ez;8zXOAJD_?h&!8@g=Q+VG{b%%$Wn!%IrPc7Wd@%eqIg3~vm3by(2e?<!6Z^;w<YRtHyQ^mJr#oa&bFF=a>{M_oh@a0Cx2fiO!ZjBK1*CEl3v&{O>TGMR#nJl^wu~YwaCf&X=!Ve(Pee5Xly_j@6c&2N-8?VQd+p<5h(#`gr8E`FCt{QvU3$ovaD=!KYUK+j$&+H4Z$|}?cW}^FM3|3W>=*AiNu^Ye8T7!zia79476?Cs57Ngr=8;Q~;Ifq?EaJvWlG-<8rG?)6cnkAcMMLnzsfO}=i&V~it@~4`UXq1ZvL8cN4jbV5Dec!*=_0gJ1wYSCX*YL{LJ&Q$WVtWb3<wpdKe=5K7v#QG`fp6T0I4NQiudjbHi>XjqB*{)v`oI*Ya*%jYvg=l<wOv<g1L=}^i*9FF@Ibmdhj*<tFCnp$OOtOx^}qGx%p7L_iPYTA%8$I{pT)*q_d^CR_lt6HKW7%=Rj9Y~lc~3Z(#DoZuSK-=V4IG&mX$QrB=Fbi0G0HlHbOYtXJiWSTVBt(*h7E%$6x>cC*0bfe|z7Z=)=^7N?9YIaPYto$X;LPb7S5twH6kfY8Rn3c39j*6ql{dGPS>ldP}Rt=JH;w-Wun7_+==Y$l?mMzcR%z+yG@xOWdAEZiYsu5a!_WV5hpw?Nn^IfBwhY+kdLcxMoK}jK02r8-L8KIh;t1YDZ~>zAV3RcSh~)M!eL&{p+uP`^*3E-~8`?6*G3_EnQbp`LWB=*>OC0cc1+RUB#~z_oMuEy_Gvu4lmY8m-n?;0*&l-=d4}M{<D847I>h6Tf6IxKfW)ihlW}j*imDv|0{<0zB1P+U!j?O^o&J5;~hOlAW<$lB?i?-4<3<s3*^%GF1C6SbEveo=Xsh3`5`HHEKs~hT6xTAOP9jv-Qo$4-KDBeBw=9NSyL~=>3-fk$WIcD${#;rfB%=to_{#~siyH85uYSkM%*-e8zM)!Zd#AK2|w-D%;i@d95&-;J%njzi<<;FQE05$!Jth7l1M1NO|$Pq%lT}l-g?;S%)yJpgO&?9Q=?|BSHmP-va4*p70)BrQJA7UY;)?^yffY)TdwRUPdBMyPCv*6Rp-E}Q?`$7-+c5{HMp3d&B{XkUF2<!Zov%Hba2Yhr`2PtCpvGI-oR)g8_L+BPCBdHvD=OAK@LhOG0s!((0gj=bel+x^6bt$w0FzO=CqD<QLbvQWZu{wfAONxe77>as=sw>qS@F1<!dr_!ZWD%tq>mXjR{q6Ypu%#;bjw0sJCFKtZEHAA;vBjD+t+r?6H2}DslU%QGX!X-I!8HK1CawwL6B4HE)X~HIO*d?`>?~#s0i~EJGlpe>Z548k%#f&6y%eY+H9d6~@5HMgLYem2qV&D}PMMFg}@cE=W#E^8WGqhOh<hlJff#&Dhp>;>tNXNs`S8={r-C55{`c4<|&965w;zO3wnfr#mf`g|`O;2RwS`daLkzX!8FN{`;7qqeXON^flWpI=gyKPhqvtaabyk;<dJfo10@Yi+jvACjS<AX4B(DWny|X#cLe#<qv~TeC~&#jkaRV7%FTYQiHe5*f;L>W>S>)q_SrF))xU$mea8EKBJB6(J@wI7dCNXUExSq7t9SdHppR@JiU(MDCfYsPCir1wH@qS9hW(u&utvdHN?20zmv!bfFb#WxLjy`sXzQ$ni-!>0!X#-y=dImnsy`O5kKmsSZ!DaHKZn><8(un+!u9Sm+&ij^0UV!Vw^g#+Zt9BmiO`cr@sQ_i@UnbTDhqHMWemT6Zg{}Khz;{!=?0;-iUsF=+OfJY+>Nx2@)iOr4MwkIiWtea^)B~KA<C7Wv#8YGkCKT7GsKAxK1^;&O}{PF=01hkdKx{gcyOT`k2>|hWicm-@pC+PyhW}@oi&c{{8K5zx|{5?gtsWg5|7h$?UN%)8kv+IIWnANcrIv)$+`?qaU+jt(K=T4>grpwK(ya3+S69FUC`@e)6uCPL1k}nP7zoLz|9bYm^b)8Afc+6hiT|{KDuxyJ>#1`Gs5B8{Q3iyl5B;_5g%Y;zGCXCbbBKsG&N|)7KqgNrPAuQ87iuP-Dl`*H=)bNO*$$u7>;uR2jNE4&rnPL0v0Vd%?q}t>Nl8?4*0T`zN>bTkOu6-XeXu$y+Pa77%O^@IIqNUkQE|;X%W!Z)|9&sr|z&b(B4H4W*c<oLfT?OkFS)-i%V|TNSo+7JCydU?9X>-8NwyRgwG)RY5GE)$B&DG`}}B*}R)P<62)+cftOvifKJ;5PpVibAc&)x{tm^>6N=4HOx(G@wfCaS=DRu`S<?1v661+>&qhguL{>UmtI;beU-XinYXEZ%VFM>r*#{|7r%NQs|YhW%sTHqq^yfS0O&3;J0FP`c^nD%7&Gv>k*~DLsVPZ{A(Nq=j!h2k=Q`sO=L&UPL^?cU25N3#Fz&c~<DJk<Sz56I`~AJ{9_S-FsNk3Ktkj^YrUMZkn$f}jTVYfPP5oAD8HJ2?d8rNC?7lD-Rh)6B78l(%sLBj+v9+~Zd5QpAk8Vv3?yovz+kfplh?|(Ci{<c`u%p8oR(gsO-uE`rzWcH<O`E!>)?En$XDHSgPi-g>mh)_D6S`&MPBv!QT}>;sXN~sOhljR2*Yj?`(%K2n8nS30Idie;!4&$b95kAdcW-^hi`-pPmyU>7>0Y$cL_HvQC#R6ccYrRyV#W0zDa_t(Q1V;I`Fl{c$Ap&4YL(epZOa&jyFVj6&mkXP_Jyg(Yb(EYX)=Q+#4Er1b7hEKm8g10Q;UYhdnsO49F=OAPczEcB8+XBuG}~lKff|`6PxmD>0(!yGOR75(ocqG=A&n)sGhe`x{ggFHq><D@`Eji%HTT)C;IE`MB33gO!d2m?b^LupHiGvdQyUAjK8@7Qf*a&v+-+t&Le!V52}Y+DDbIsPSBduym|>AskHJ_b!@^KO0)|qF}JbZyX`fi4`9QPfwkHkj4T!KGEP`~D%j_vZ6(7)_(y@BTE8`l?4cVfO++8+T>~vDT|3suw)4_k=4hM9m)j3W;qB9+gQ@L^r~-XV++{UYmYlJku5G73pJJ2fLEfwox?L^do#%jMHN^|3JYKv3NB-Tj)$9XeE)M2ldXAuU98!-h(I6nPJ~lJZ+};>}jXvfQd%_`rAerP+o<L8uT_Os+ti8aCN!RBEMym&<Yd+Fs6>@->&)2KLm}-YW+Z>}QTW_OmZl*l+E0q~NHZEg>KRMFE9{X+{PZ~HBT`3GZXROw>n@^6FRTVzD+ch3jS6oY-9(^2hQCUfPo1q%%uY4(skk*6Y$eaU}mnW9Ql9$;9rwPV79WKE{ud)QolZe%IZ8RZ<fXZj;ZnPr|){?TINZSMZokEUCu_Jii(D-ZD?EBkM!|qFUqp^~nP0mstmg0KGO^a#|<KGC%D7(M5oXP`EAEvtJ>upyB^3tc^7O+s0R_WEojH}Xt5z~ZdLiF89hhA4@#bD=<deesc;SYiw`8DC<KEfIO++42r`|8`NRoKaln@@YbkS2<Hpt9UUP(7=RrQKPWG2Rm{MYwK3^UL9A8D|_Q&eMb5tP-O1R`#MrQg7vNJ^XorURDD-xO*?9*7#YI`D&ovXdF#;T3OUx;-V*$Y1{HU&QejpTxEbpIU6a_!Wiy(Mq>+g<11E2WIPxe4T3J7Q4{li0Bvz5wM=ZM6Lo1LNpDXtV=BYplcdeBq!r?teQ%5Vw3xmc=go|PmB4^Q%jAr6z_Lbt;sa+^S6p)!(x+r>;5k)zVV|A2^KxZgU%nql2sd)XY*8qV<xwruMb@d#o=9weAh*w=+)J?$W;N&ZhjE(9RH^^O8CQZfHelD>bI+Kel2mP&T=>lGkoh~yPe~e;Z#DF5b*@&co6bET8_j77g|oGwTN)S?in=joocbO!lSIWt4r4&HGq5q9UH)hZ33O5MG*s4tfK@s_w0i;*Y|7fvdr+eKvX#%o1}@8T@DhCiF){2)L+!qZVC$AEeA17#c`7?_j!>@6UYHLPj@j02>o$tc*7mUgYhkSXp_=XoNGhJ3Zv|eQ$6#v#e}P{gV$ukrC}l_6SlOKsYJqw&%=JY!YWU`JC*OR~1zFa>5O|x=MAx*PNq1*|<vt>rsFBf^(<IUL{uby8Gx3EwQCAEwdSF5-FkD~;jo#J@lbcMF{r2_0V&HE%X%H>7RF%BEhu9tD0yga(qO@UoOWN6@H#F;FZJJ<q-cfQWc*Gc15x%AH72gDHLR0QOP|x;JNFw-n6xain5|s(FT2U^BNVx0BTmI%r)S{lVm62kNh0Zajg>o-AvTt|L+n_)T1V{d^u-iC%geQJ@b9!Xn+ge($4aUJkSd_ruDfgNS)tu|<XUJNb5_=PvQK|{%vTKICZz{WeUfR41tBcs1!8N;Cg69w43wzP7Q@z=iT&lmbj=<t2Doss6fq~EJ5z@#sgKhhf?^Mr6?{5*&N<-yqmjc}C){#pvAD$R;m_MBFto>yHOFG92;#Px=nS)mgLyt->TD#bb=x&+9TFp&@nXyCgGeTi(pL#`7-4mK)eoY-F{Tuz%%jsLnCe%5Q-6-@PX`Xd?!Gbz!<+n-^3<ulM+CpQRa4E;<867?wgNn`unzVy+<T=bky&}qPtHIRaohM4cl#Y3KpF!e$^14CxAISHw@UqYT^pC&({ZDxMfB)^bf4<#Bm>`_>UT3f^C2O|7QOA8g)i*3e=l<?)hx9v}6RkG1OK#9Y+*-@-^qa0)A@Ve~{J7CdVi69Ov}|4P@ZbLR*T4PcfByWNt*Bx%9aPIJ%De1)H5UVau1)RCRZ~Q6LFay;(}@dFSq<@Rz^u0Fb!xl)YA4(0<etZgmI1V{REEF+TIU)#mk(NNocN+gGnhkLge{B?#ps>98)eqd&8b<!7qlo|Z)?*~b8~uA={D59+%^-^!f{snTI;o}bhS0nf+_yg0ZL-+OF``a(R<YblqsZPWn~Uh_t^dEN4YQw%vA((({-CFkfe$7+<a8uh(lxFeR)$AO^)K$%~z#;!2Bg;I&Jn+TW^O3BMbzE6!os9;`Ytq82bZO%y3gVTQTk;92k*ZQO*wK829ZH)RmgrTg@$132&vxS|OFgpOS}sKD+sJZn3m@W@8E1Pu<rRUp}njB6r7z_welLCumZ>H+5Uqw_vX-R_*L#FIk0ZIx^nxjR`3XsG+6o45M4Nb|Rhvp+#iD%Fu7O@jS2}cXlgJ$@fah*{?)~_hP6usX~l>e^-grz@VIPcaOVQs&<Fboo9<twB8g0y6EcF#`fJ4->O4|W}cPAr}DJBci2mAT0WO@9{P0LC9rC5G)s`6cv~Trv0ig2vhoGm9Ws|EyH<XovC?bLaPm_Xg(|I5ALv(lEeq<qH)ZMEG>srPebLx!5>`<u0*eor<%iHPuhga#N~=ktnRdiSgj+!4k5y|5xr86Flqd1LyjCd<jtf+Gpgk8`MC)t4K-C=Dm$YxQUfHQPf6Y;Q^=9dt4VC(p<MmU%bsTsPtGCs%Wc3M7oh%tWGbLd@4RiG92^1d<0>>ULtrgokbs#KYwminWg0y!3Tw7<dqTlvb??ZVva4a7;(<o}arjWP#1frt}Xdpf{qSdfWibwwu*ZJM~^`_L}=J;ABFf}Q=sN_>a2X9;Y)FI^7QL~%%_KB~k-j%IT%30qOiB&3^DzF*o?WO7VhJWvFDX-oLRltlo)rNAKZmXy$hdzr`BRnPPiSjv}E4hhmJ5DfR&am`SXEbzd*~6n{EV!n7Wh@D{p7!0RnO%l^4828Si2Plq?HV_kH`3Eq9<*5w8m8Q=dY{b>)X<`0?IHCYzy15aKht%``@hVYAI&EkT7~NMHu`(Fmj`RwaW{JduW#1!sC}r_=s2-dWA+_nLFzMmCa?&$pQp_?i!bIqT8H<2R=?Wgdt`{+2%pb)Mm<xm*Eg;tpgT;=XuqGD$mwnfKmW__T-$H9;R!RmEsqiIVX-<)m6XTi<mk-YBckPcxN0JQHd$cpue@MsAG#VM(cncQ+fk+T<C+5%b)=Gs)vRFOpAzeVH<5ayjbgZ=rn!1|S*{MkXKxt&=FGc$AJ3Se_bMH2?3qEF^Eu*s<$jMB4TCg7eGODTA9qukLrn$LkzzX?t1yl?bs-o8CQ3uW{lI;I`l&{x?({>K%Q{B!(Lp(A{@ila`{I6deoh?#_lK+6vcafSuEnLIjWE{7_V3@v^r)U<jeNLq5Z+ui4f&TD@tdLdct>%7b4MRMskfW#Y|+N}>k(6a>3P_i(s~FJjC^$WO}C%ybH}+s{dQh%%WzbAvi78>4Ok0_$wbG^O0uAvUWbl%^m{{uu-orVwxfrp`oqzp(wQ99o@~2Gi}cwz4|m9kz8kWI&hUUblkMdfPZx!Dl*Jm^c&?a$MyogkoA*w2b@B)@r4$eMQ~ULjvP(MYeCD1jVQNdh4XSMIj;+~i^EXsbFgxLP?_OU?Q8BwhnMHZaZVvq(3Ej`GLdNj|bzIBWCaj&hhZx8`TDZcwva9Mia41SglE049klks}+QVS?Z}zq%n8b2rmeIn@5jZB75h3s-En?BNqg=ent)WWgO!e7aI31Fx=EL{7axD-}F13)ws}?`Fx#Sj85JoYay$SY3l4=EEj~~~xw+o+UgS5f3W{Ck*e^*37s=K4n+ec+@YWd#7o3e+r#UWoYsa)JD(&Zzcsik*^mR5ioNU7QsW+LGA(_MCo(`}XJEtjOoiFy0pqeo_wpVJ}<)%#523Wq96th%$Ow0c;{wUw4#m!ig%?y-7Js+3$ec4?*lR$z%WmD)L4JLyo6GSMO$h)VmaaX}~2?eN~#7HR7nG8Im%15HhZ1l1G8gz4|-gUmK0x6fdx9PAg<vE44GStHrn_D-$Q(#B8AcpfNkTB2sv7dV*X9TmTv{gai|NnVe2R>y;TtWnoSus5qB!B_jq+}1-EPL$#gYjIyiaFpKKbybGd6%{c$ni?o<!tF{{p-gv#D*WS>@clus{v(W~F<%TtDI=r$V@9WZ`+9Db-|k}JO364<`g?1fb9=^?^;#R;Nv-M>?=AYLYq*5Qv2#mtMit!cO$m(l)(E?LEwhYIB-Frg188=)f6Y@wjq<dvdhL7BDLRX&yumaIS+TA_uL0z@FU)eyfqhp_RcqQ4ZAgLDr5x#j?5qcRJ0#u~WgVm%WFKRjxRNpkrWz|MA?ok;`Nk}(xl7!KN(-*Z`;qO4AWnIhRYsI*ZaAo{Mvcv7mZXi!gi=;HG#b@Mm$IY%;%NZr*Y?a}KVy2=NbRlas5NY30u8szCT0Mq@2OTqiNYe~%$I_;8ldC-LA;_Bet82n_d_N4n01(PTtS(RjlF2Iw_T$Ik9%w7_qd;q57icj@o@Y5mzJ+h-N?ps{NPQ}ntkUK9)I;3=xZgg8W-)O4flHMoXuBR;tcj{H;KP$NK{8V8hO)f@jeLUsqdXf1Eq>3+GhcqJD9p<Y{x5+tIb@s)T^v5c96<eP6(O~i{GGT<|biMDZiy?`n|2PSc^2y$zCJ3bdeHg1|xzG^wPhm*rP?Tq-SjY>DtCV+t^FoQ@b}x7fTl&!<yWj#m8e*AVb;A0eN5-KXN)<j8pQv-BwzoR(y&CVw*mtEtuv&<H1R(W+*JEj8OCFu~4oG3U<<h_0SzPYde_)8AfTaQJ~e+IW^`geMhJdq&E!AnQzqXk<c5#LN#s!9J3~)?*CX5MXyCa)lxQS5CN$6GBl-UHX*&+|5V(A*-~f<3$!gHWtu<Mz~Nv8F)5N-VZP7JD7&+k7Fdin)hPm9j<vQE-6tJ>Zy-N%rr!<7E;N4Nisd$tx%r(a-gZ!)TFK}Ff<(?5ayosBjNj$S*5hlnCaZc@KgkRqS%Te=4WN{Jsekv%JVIpZu}Zx#d=(Z|qSz`N6q$vH_4u?7Q+yJOyC9RmQH#>LNzR+ub%S=3^%{`3L46Q8Hak+cb?|7a&%a*gsY(dCspg<$;5y`g_t(NoSoaU}z(J~P;Z_`!Q@CreQ-iB>*{PZ;Lsmb7Ij!0<#1oN)>792`-@HW@(Bha4>>~Pi%_E$aVJa`8eb}@BF)V(_viq_zO9{<OKGJ#NlDcU4%DdasrsD>&PVV~QpzWaD1IXBSVKKb5b_rNCfbN0bQ~atXdfrHE*A8g!C^F^4JCELv_Ip~*43+*M?eMnLa*ONuZv|?N_v$afQ3|IpujA)-giz8AqxYcpqo!_-Sf{eRqKp%33#6fNnmX)p27g+M_m3Z)JGXGT_#?L$IsZG7k2c2lga8(m$BFX`Rp<F#GN(S2z?u1(+=Xp)vfJ<B@`O!;MA3=cD8-Wk)C4<<OZDpz{MxyN?CAyLrkt~m1*v^y=BLJMr=iY>1vZ4c@0V&4Cr~94x@qhx4#O25XiH9;X4C4;Mdo-+um$FB_m1l9raQn}AJ-ipXf9F{7+a9F)<4uby``++X0h*~SJm7M0%kI1baC6ip@JB8QYG4d%i=3&8wNAE5}V>p-vEIHPgor~O|;teWKC%)ZEmTk%R4@47(FP`U0W;Or!C2AbEd%QZLh`R8}6&29z=|;ZR<6A5V+l`=eDR==ZQc`_WpIA+HW>CN$Kq+69DW5U#u-s6&rDAY#u+`m>p9-f3e3FWxmOVxBHawJNqcohn0E|#~0As8;vdI-#vL_LPHc$ak&NK)Ejl-6-`6D_<LGIfl1R5KV}ZUw+u&Ev*St&aA+jHUCq=zK6$Oj5An&B_uJiJXZPh8Z}|PKeWWmU-?=G=Hk<3+JGva){nB6$)s(Wq%DAabK?GVxlug&UEZkbDHi}=g<(eHwYOAqwyA3m43dO;L9k^Dd#UN!3JchY6{NC+;@q)+p=I=d(rByw}J8Xgq-uUr{6PkLwXHlxOp@KHVv>|c<y*RBk&y!Kn3N1zxctD@{Q5=O@a1?9gOrr|28&a%~#@T_WF^eeuXiL?`njNd33tQV}Jilr6#9S{@`h~--ShXCui%91^`c8Ebm<9@_GWzw-cr@S}Rxa!`n^kv8^Zh#gv0g;>-nR4PK?cXxZE(FSEoUq@!{w@m=CXYz_zZ>fdfpPYLi{wZEcswtcst*=X@wxg@-wQu){u?WL*u>vAOWz}&e9fwZZr~$wicrX;g4)ug}@kps74i2U6giheW;vSt&*(yGv$#Uh*NsttrwchW27l$Wfel3&0-wNJUGvwL$$jTL+D)35#5{*Y2=~y2FW_OpzRpb(iUloYCS}#{oYWUZ<qr&9iVnv4f7H!PB7RYXSGLI5Y3xTe%?Q;bMXV0|J8R-(E3dvfHK_@coku^#-7qOhw%-Ud~;I&{ZW<KW_k6%Sk>dO%N_UE@a23vE@tSAo#YD6rk=>F33IS3=0^VR4su#5?J#R(0BU*wlTn(8>=7}yxuc28h?MqcQzEXF3Yxm8px@sdqMi48uZBY!ZVlo$vO`V1909t8U2Zic2@D`Z)mfyrkYlm!*KR$|?CUg%c20R|r3rl%Iqmbk#5)ZS@ZJoz*?bljwU)yM(>q1gkr3AQ_x@k|%2N47WtgM)S!~=VG$Cb6eHmZ4qwSI7y>&FR#_8Up<6!+|DZ8WT8Q4HeUrEhqL2?^c`Y&QEvz1tzbJ3{I!jhr^NzC5jc4!(zEgIXJ>QNHYXJF{&X|qBW>TO<cPlsg!_z(TpZ<@op?Dvlg+|~}8vejGst_G~n1|51TPqgc<b8~5?l5ygs=W^S7B_ou+_19P*cv04@HTu-_5WyC#hjCQJUV-!=u%;fsT{RC`Ini6g#>%=gn;4(=P(~J@xBT7vkRBNqO@=UJyS<QUH;I!|2U6*%l@gM^m9Bd*%#$4P0zu_hr;ud$1;w=5x8e`g-pBNuufCX{I!*CWsnHS!`w?wRWYpPgAv6_G3$jqFuvd4NQp<pW1E3gDzODjBJ-tf~r*ulbb<1G|wcW&O614&HccY!D5$GBlrNN5ol-Z5#6J6HjR37Gss5stIo}hu+TS4sfP1?+CxUV5s^X3LnK1{Cjj01nmIWs;ZI<z&$+55(^nS0+>d!hkbx#P}Cb5;a}YDtx;trx-VqOR<%l7GO1xl4}{Pn6xFW#?lQoeVd5RD2>LGU?ZL+UY&kn4@~usE?WZciYLV%p3d28qJK{Y5ate9&*N-MnUO`OEw9ocdZT{IE{pThG>*CD{z3@J!7Z+<p+Y8T5HiLS~&6KLQTTshMSBG+*-#x_2!l9%B9xA1NW456~w%)Ev`J6O<V9xXwuym8ef~`W6cAwYlnwnZ+EoSN@>e{rLAyf1KFCGb*pzNn_LwS9A6*Bk+8R5WtaJ{_OA@Dl+WJOB+!y<<gW4K4p(kMRgK7&<sf#QFm4xF`u!WgV(v{Vj=^s%OGOXWTEofc$sK2PV9z5u3{fx*R>ztDdTHMGjLlEQ$E?Pp_XuqC?xKa&xAGi#Z0c$S+o?jTMPvu&GbJ0I+Tj(iq$)H0twpCcN))SotBHuDNu8?!KvAe@&7<6#AxT_4Cbo=1#zmycDF6-nxoeS&w*T~GBz^i&JybKDZ4VChR|KLm2RZZvwuyk>Zkl_4d+e~O@eUerl9C#hXF&C$PDK{GH>B{tPV#AyF+T)ySsXqpp?tWtGBU*5*)`?TU%fSt1v<xw+B=Q{S;~<;27X!;>(1dNzFE!52@}OKl|xPXR`rDGJkdjld>PQaL%LTNv2qq|_4}>N7MHyF;u;77O^C$p+lnrDFY?=`4O_tC%@W2imB0eb2G)DBL8u^(V7Dwq->*I87(Y3CKUXRm#?q*c4@NR7%OOVQ0<F(0-l<{ajUJwNYyYZ?2dr!a3r!y0bb?Nmw-wI-OqHI`wx9~&_wf@p<+kkbk3aq6uYdm&KK|$5-c`8p4l^k}_3yv^_RqJ_7P_8fw~y5Hij^_y`xCa$=@f@N6?*RvgMHp)tfBtj{`J?t{pEl7_x<<3K1{XyPJ?b7H8EHz+^ApF=T+@<n!TaNFoVwa1ZNG0+Aq{+zC`+}Db&kyYEnE3)4&A>*&f(2xuFfN?1TB|f4sf@rxByC?M%D4@zfhGqlrZ(rW(xa*L{2VruS=ndvi^Z-R@m?pDRWX8h=Q?1AHTNfBV~S|B%S2c2pHtshtsbqzA<Z%wM85q=v%n$FHMWAMRK+_ZaHLC?iUlm0dSb*9=xjxqeqo$-kS-{E5_P`soO+&#*n-pMU#!0Hu6rw#9Ub)!#iyR63?OqFbxst|R$wU*w`Nm7iH{I+4Sm_#RR3eUESr`mgrvd%BO8en+|4(3EToRtM@vb!yFvKfSrNu;fV$x36m~Xq(rFub)Y(uLWQ5|5V67o6XiQom<QB+uEATR@IVc>q9Z-Tt~Kwg?L*j4N#UUp13Tw)RF1xV$&X~em32Cw#Mz(H|SAL{_GycB7C&e9CyFw^PSnGVCLF13XcsqL7Z&UEML_g<T0}uqOp!1b&(6kU7_i9f}5^aEVe{(clYb#K4xQE<(GOKb?vdQPqELhY@3sxCE#HKvBoY8ls2NWD#a9nZUb|+rQ0qZtKi*D#7H%(8>oy3#{BEvuZH(r@Bx*ha&S&HEGcS<qc#{UPyp2CRs#Is0jH+5_qO=Cwh`&tYExQ;dcB`D24Alcd<A)G0A}$<!&=Ggdijn#p?lNUsS3z#q^C_Y^%3z*lZW`3B(z_m0~7qIX%)Zdv;N+~R%|J>nZ)?b444nIE?CRKVur5gU?Cs!Eb*GI=+x8q?A~UXeJfyuNr$F+1P#0h!Z0<A_F7(XaHZT*N14Bz*0VgoS>!pkc1juXZ6*Wv@vRr$*iP+EN{7gU%nsEJvhZ*O69=(mS?wkiNBdGG7TFnRv~lX%3MzN#Cw8MXzgW!KrBJiODm%4d>qU7w(p9W1>w4So!%PKc)Uw1?t~XVaw=xREQ=l%U9S%PWj+L{MI$cnjyK%nMdz>8F{c1ciaC&Y0Ksyz+^qfcg{K`D1DiWv<Ks-;y)JjdlM0qioBG%8`v7=m3#?U6Tk)kJPxmeBEHlbWl5$6%+%7%t(1A{ToOS`7`PEBB~E2@z<%v+H$4c%fZ*&#hdvaIqu#)fnr*-{?;V61^xvr)qvZl}YsP#48%YRGN-+HCAGsV)F(sa7rxQe3P}BScO$#+zaYyQp3*GUa4zwL{wdh$f|Kx71ag#l+&RS8_cg6)LB7FUippG$!>aC%;Xg#^C02zvaqH*?af<cX54AYfLpx*=E?w(nNeW=FQp%QVk|Hjf_D*p+pHYzL0#aOl2&J952u`+;7=S?e$6YPC)94k{$)N*_8ef`Y4D|TKG=w?<?EVs<0_Er)Iz3<0QQib+P-1*wPMMXCG<Wl(uks`NtIB;v7yI&q?L7-|=AFflpJL@`dI?nhqppYv{)vHK1kMdv#N+N)5{1BVLYmgP%o`mk4!Fi3aFud3$qOM|WSNp?n@2ZHpfwl+?RE!S4+&wvIz9xvqh>xB()3AhNi@io!!1o)sTxFqlN%jcLW$n=NBcydP0#j|}zNHju7a=$7I)tYcftP;2*E4Yz`-q+usd_0aKo1|9Fi0GC-@u2G08?$0{mKLRb-?cuguyoqr|K3bQbw~maqI9?hoExg9_Ve%_2_G!bGQ`ZibMYZF3WYKE1N}Z0ehAdjNQQcd%DJ)HBsO;zV8oP7l<W(n*&y9NU@wxx-?4DN&^>qaH`I7dgqf*7a#Mw3WtClLKlF)dq8G6ocaL!ooA<i4tTzj&iN7YL4rKUJ%V|?;vvi7kwSk(itMx#x=nQKM1Dv2H(2|ZU-F9v<?>P|)?Fubl6PEEo?O`OG6WW#H1**E@t#^?ckHmWzonq)@9(N2}19hWm1dnVP*(KfpV{$9tw-rvHqnTk(S_l=u{+b2d1Vc%cY)}kNNi8uRn9D?dy#@n3PmYdT&wrbh8S&BAD=$o<nvFYaDjKOB5j&9W~AM8hJZ%uQKXTjQ;->lNxxbjevVQLV>)r76)mZtpKf;!5B#=EEg{>UtKEd*Co`;1bCZGt$UW$JtOHW=7EZCxEL>M&Mq+Vg3+K!XC0^&-uKn<sSlEHoyl+GsgNcWJzL==EBKu(<_fGBal-$5B%ZSGcFQ=w-mAU33(co)D|?p|$hQfKT<_-(rRJHLdA&)o8cq18`6b3$~63*8`fBi^OV5r1o~y3Qg@Z_!gFG6*MeD&<2>?KNSQ4<zRYR0%es_X0y;maS)#>s7Ca3(oAp{CY|(-{P%1C-SmmI&NX#xN3E?XZcJ<5wrjq|=Bhn(nUtNQ<6;FS?#$NJ**cYehZ4)Zo02^@`IqVgm(FDOR~jOO--uEP4o0BfAKTlW?!n=KIAv*5)H4wX7Y!;$*GhcolZLo3_40e`KwgEO(CzKBp$`KF{|IL~+%;5VWNl#2f|}GbKY4>A+Ng&11|suzU(w!JriS5OBwLZTz`i<~9izh?R!@xXY1HgKM)&jtkj*HrD2G*}$F8E!@n{R4vP@c}Ejzd@DxFKYr9JYJ7&mn1sqNgofvDU#4^51O6-jp8TaoE;cPr=%E6|)8sYp64yatVxes)xH0j(9ZV;g+FSo@q?=~Rj%oa*+C%y52CMK;YrShef=h*@WSyCvORS|Cp2=-JSPW#GUXR2z8DS~I0_)^SF*Evxmm{+3L(#mO$-)2IwgDc`bS@B5UzQ_(UCmzC*QgNTZL5N>$idJ)gAhr8KVgp#8ZCN{i?GPP4rSl*2lZXR$W3*0%Q)fx!vRo;6A(F<m`cjoTOn3|Y)G?}Q_9eR`W*8Sd$h1EbF2Xi+yek(b@*(6~Rv{;>ik?u*gPG0M=*xt?3H8NN0)Tniqx=p=RZY#GgT>;Fh=ggs@o%HtM0zEYz&zD;Dss+v_&Wl)PS81VkuwygMcxOtZRq5l^PmMi(uD{co3aqL{la69>*m64CjD)kqP}D5hc!SN}_$|WqW3F6#XgHb%Q32wOf!kMzVPd74AkSO$?gy)VurKX!5RU+gV;#!sQw6~(r~*~)d&)SAnvxnc9C~^Zg^xH8K=~cIP?JH~s>nayLN@jDA}cjadr7{B)p9M6JdBm9NpKV0rhA{U7*V~-?&R2~UE{uHO^so&g<qvo;jPbCI-<6b@MCm*L~q9oL|P0`@|P!&LMaRh<?W~s7wOfH@TUe=*chEVh<b#Uy<SaWLroUO_uOSS_Z4Mrywx1R4WkiXIRa^|M1Ao69)_$`x304X>W;F|@#5D9DgX|yVM=wnsjI=@&<@B1bJze>X4Vu-M`H@H+C)_C67}Wk>YFvP=+E?RV!?PNkn;pDXA2#BRT!(Sz8K$m0!(RD_<}3sa$E5pR;vf_k)l&eM`F1mU9i~L?)E9rXDS#2ilE*YLU=Yz{ZOa_sN}}_7+mwQPP3L7=yj>%n{_UuI2czF4PT0bMJoL;l9}rC%nd{>_FT9!-EA?r6+69~V*32Zo^<1YNt@F|F=8bg`>FmmaJJf9@a9!ZP4vl=S}uFF;)<ze>yPq7-N6(-FtCUk7mFQ5`;J6jE@+SOhi77SrlA@Su%6YZm7LnVvN_)v>q`yvx|`D3g_><~lgi?%f~{`WoGOnIVOdb~QrEY*GZcnsO!UYT#YD|wqN()Y-uxxQ>mlCL0VsF;OVgw;<`=cqQ!c*91|Ie9^n2zPO{Jnm%EUw0!<-!!q8i%v*Rau4X7_ut`&k~l0QNHNOsnUzeC6l@K3yug&ckZ$%|r^>7ZVA6WT>=W2PkXK_LDX8;VN;`LdxFiszm`!wHU!lBr#Wftu{~+>20sD?ie5K=r0JLI9f^}AqrnhdBZ76MR*_s4dXt*tn~24l~wC~eUDMa^n#pDTf1Tzr_{Jxvat$w@7-Vjs+Mw;3+{4NLnY3vcSu~EO%$N3TwN!Iv9v&(^%_46g;u87N^0uMmC(M?Y3z5(H|V;zGuj((&z=MvYCIP`iiGwQz^PvPP`*F*_e_|KkX{>BshVD=>S-D$tbIS;%%gE$UH(@uLIy=P{C3b3IyN+m2u3D7gAY{8pg-Zwf-*ghO*`$YxpI2>M4>B9n056vYU)T0k#{!cu-cfm7Ef(3u$-0D$3m+@7be?YD9uyO*ZMs>b<`kRV~`%O0YLDww%W9p=Jbp&lwaN=sun+EzXkH@pge*RO_$1`dS8Iu6+I=6-gJXUnj}y5DbOHdEJycuuDHb%6|}WWf4EKv7krKzV_c@rqYB>6F`?3eXEgwrg*$u6S?P1@gE^}&s8Ob!H1z!_S2m?G<?*5PZ{~Tt1CM*cSHZ(k4SO%C6C&TaLQ^(_cng%bmgGIBCg6vD6tGA2XzGwYs2P(3-#PXxFp9u~d$Pi(7^mZVfNU_Tjiu$8=11S#)s-tF#D)}>txg)|c&`D4!7_1FExLcsw6d7XgMxp^=^_PhFFqS<Psh&-HRGuD%2X|=p5BVlXfyr$bkXfAQjoxC23&X;CE8PWzGC($1e9Ys@d+J}{!Ct4C_4?i#KhD0m|IlR@TRjnwAxbiaUJVf0t96vq0_DrPc@UClyyIlH596+W%?6nVmaR7IKr@II*LdqP|>9F@qS!7?VIaLdm7K?P^Z=M&iP5}(wyvbT6OClsl%^CkWe#)Dhy#e9<6g#v88o#+QTOe$bHpZ?Poi+tF=;HEuYWJH%tN<{h4x{DfH$>T(rIXNI@QP`?I#odnmSTU-LQ#*h)w5poK*T@pj+Ou>UKQm1IA$hopX5_U2nc4cCJO(i`6W@zxP)JiSok_fre3{~kHPy}w16R@FD$)biVUmivnDpIhEuO{_@|OHMsxcRG1q<GN}8xN=oVnq(60cehTLkb^m#($sdZ5i9N@?DKoQHM*7J#9b*>#fmmvjYrjt#bj%?YfaA;&kprXUoiDD0iB}f^jM;)Exr;_u-kmX4E4@PU-eNm0U{*_ehUz_+v9(Jq8EjPnqUT#W=AbKnnwWZ$vocuh&h_uBig^}pz$ag8Opw$DtOYME+1htw#gUm;=;cFBanGL&pcfkzwUYL{>_`s8h;!;+A8_lHx^plU)#|AYY{YP(aPx$bV(ZD)y?MdlfAf>VvQ_cj(4NpZB-ulD(Z?21h&00vE|VB^}+xBx8MHxrudckz{36=&R*kMoR{h1p#SubzyAGCqCD{1yWUx7&GWatwHCRskF9Jv=%4u_HJD-lE+crc5(<?2`saVVz5Qo&C?#-oEXFAR{`R-u{!tZ8y#Cac*wu2z5NM&4KmP4sfBoBE{^!rXeR%h{a8VidKHgtR|L~cgG%^$257H;vXZl+px|;3!c-uqqvGc$GwXc@iGuvTUz(0Ua(PuO>oA<XW_pl|T@E#dRs_i({WcxE&QKbuZ(7bz8FL4b)<+xP_tvi>oEtSs$jh;B?>f<O_f#N+%2Ya`*E#DGQ{Vc<w>rE<q@H=`=Z|hw>>{oltTj%lwr&&A0KIA@iHm$d+le8D^dlhUj<+*BXz^zlP`vu)IrdB?((xz6bv2@8%`Wv`~nBwIlVMwTE?Us&H8yt2IZISV-7?@JEs61`?8hdqy%12Yh7%KX1E<0JtHDJ83khV>~=3#LMK{;kGr2C~vel35gM*n0-|70XO&5A{J_Eh^+TSSG(!LCLn*ObdeFn0e=%#nlYLbR~@HgRng`-<fzVa4WZysl-)u>+56=$p?*-h2^}?>^rI<Ti0*1_^Z|JjPWIs}>TkXyoqrsvsI&Iu6RH<i~FY>JZldD<5k29a~4&Tnf7<_u{q5Tdn0IZ7Vr2Y#N`Gt&704i6j32gzrAWY+$4^I7AI)f91wLKu)!Axj&(p5+M6Osv&?jby4LLd!>y4XNzB*Qo2RTm|2(hDA#joD0dNQ6TBa<;L|Ff#gWotyRI3Z$0*<|gF`0PZIyS^H)Cmq((*<5Yg8-g7kx)2b*QCh(N__*bgImmgf8x9Z^Y9Y+E*)&tz?as1ed}dQCEKn1{B{YngR4oN8=`_<V5%Hvxyd4Vc#{#5j5#`V_2XTP&LQvvGltzl%u0&3sTn)7oizhOJuyBQ#EUgG#}9)075@K-K&+5N`8<YwD6j4{!FN_3m$B577xOOmbdH&32j}Emo6do)Q?<K^a3fL8`3=kyPD@u$59;BsMkR$eCH7h+7_>_N}(Ma6$xmmwF{(KZ9|&!uGjoI1ysbWjy01*y?WHm{t5O`;!K5&%wn&P$wV6FH5<0eR&#9`z6I~ag&q|f7K_Epv8sznJ=FMsc~=qQ>w0qgGVJTo^*uJ)uB?F2s6(yXR=%LR3s#8q-kiyY2aadfBL{;)Zz-m)4x~!9#g>et9Aq5fto&D}_j1`Vtj<yesnTj1;UnjJPz1|FD|%=}U%h2qi&nFj4-ZW|;`5`Uol4K_$HZ!!U$)HEs|13TfwXXUl&^wQs_azukb#txE?bcUusYFAMd4OOL+3PB`frE#JE&LK#%&NeJl91%-BV873s}v`roOd7EbLY?Jr`MmsXLX!5+?N$FjGdR&relye@h`MqP=QbUWq&%DyZc5A-_k6Ijl35g(kNvF;?y}F8rrNaZ{7o)MSjPX~$s?7xlc5dfYFI5WwS>g37vKTm(@Y(FqCOJzYhx{a{lS*=sx9C~m$^wvf)xOg|!A6W@83uF3@+NpZ?D{q(5Jrd=T|-JJ^wxRR|6GJVR?MA?+ujR%B);<s!QbD8X~N?k-LhL#PyO48O=f^JHz-dc5`Vin(}1kDyUeNfF;+4@Fv!wrkHofMTBU051bz0edmxZf0yX#{?YS<n60W=V5YJ-uG0LPK@ZqUs&dJ-E+Wv=WE{`Sn$I%T?xxA5hh01|++}(q7ckB6MyKbxltA-53`ykHqhubxlXu-YI5NX4r^VL-&AEpth^DPUY;Q5wH-c3$x8R1oc*LQe5M^gR`Zg933j+Hq^>1R6&;BT)Dy?NS|Vg0hZgp7Bv*~J?71-T|u{H+{tY*v){i@U{sQ0h3n1A&M259>@>lw|J^SVwN$DC=~|DL()VCX!^a<!dOC#doK9<=iZtD5D`*Qa?@Dy`<cMQUMZxp8FYVA?ZV2T}e(vKI?<-y8ZmmATH|J4jS*88Ktx72Ss}wmZ5+qaka@QPQd-e#0Qd@g_k&K3cXtNE+ATM;+iFf2zJdr(ERaS`JW8~UP!vV|!5)ExWr)*MdDs@u$($E2bq9MK+e4*t*v#nFbF=eRxNPnswB=UrFku6qF5lJzVxO)FBcfnF)bg7*x?as7Mp6u)RM1<w@J_BnJc~_n4WWxhipVxh^+K$Qkk|ay(`LjlLR*+Gpp(>;4o|E(%Sb1Kp0}oaK$ndUh9O$+6so<6>b6c}uU%#W(+CSbR@)l~(Pl@arb4;f2oj<KvW+OciQ<dw^K)!ohR2}a70G?u1TI-Ury+@cx_7IS5I#uA)fDUOZGAa&cjy3F<-dy2u@bixbt!oQIs9x2C&A1IRCdq6Fps_NTP!{Ay*}3PKR_57#H4v*W(GUamxZ&;nxB0*M_m(^}aPX{W6y|v&Sfeew$8HoI8gqwBiM%NnsP)W*7|2x6tVx<xj5{{Bn=0W_Q~EUov`P|;7P;H~0yhC^FCv9Yp&FIe&D{0vpEbAA<8mhbN_IT}RYNbZUmhBt*SOl4g145sqSdjXi!$t^z+yjWgJQTrF=169Or62%kXKBrCh!<@%P@}(e;Y$vcZGKg3yih{;l7)>5;U@+!fCcdeoG%F#7P-aaCf|;l@DGox}p^}lfcue=I_xrr?w!qpsr;=i;9;-$!eUAA1{n~Pi29h4b|z^Wp%wRO)9%wT$igF4k`{wPD|M@J{n<+V|w<nu~chDCQt>teV$UFbM>1I-=mJf7C|?07Dt)0(>o~p=krgNa)ZVox}LXN?Z(X|a|?TM)B|)d=)J8&!1`IR(i&xD)T2$gJ}xFQ^hE7)g#vW+v@+BV98uakrO<678QLg9bnd`kR&~%VFng@bMg-dHn>^F)_j3#O+tLrL!y=BDu6@?-+vK-@^0MGB|EsSOvpS?f+$N!F(f{=!1QWnf%bD`Pcia?9OSbB4YH{zhJ}f*GX&H@Ms)uZ;tSA_)TXl$9qob;fK1A8P0<#Y-SlZ-+s21zJitH<G9>pt)mo`Z$mFbs6D0GxAnTDgYMRR=X?QNK`Y^TwChOCj_z>&Er8MqnL)o<RZ^t)#T(>&d&u<iv+FXl+U+q4n!BTYItMbxsT^4<{pf9(O_a?tt)_^7z;5Y^A}dpEs~m$vPeT9|v@oH%r+8O>^mIeyerd4D&n5WUn3Muo{y5m7UpuJrvBp)71t8r8mvuL|`H-11~~QTs?seqn`ro5>~X3=vC}neyYLt&bm6&8e`6!})yKr^mdiL!wZ@ITWg;7`biBBz^BQ2Ee1C;q<KON|Z9O?R}@^&g>bBxgZ*C2RPGD+xVEiwJuj$$>Xh&)_$7P@KNpE;slHw0Si#$#@@=eYWueGsPu#?>vO&`PI&u`^{Jd&HeZzE47+a)?G;d}r_4_Ozj{!t*Exr(m4X%D7A4`p=%9T>R6J{aIDmS}qhxv4p0i)sb*`4UN(|LTS7MB-y%kdG>5;N#>zvZB!_xN_)+*?va4LJY-BevOikd&ht6kMh((U?DP7og6-ruO=JW#Emy6fVK`v$$Mqd2%m_lsquPPw4+ixMD-FL%FB(p^E+R?>0%tSY-kB@fc3RF!US8=$Xlg%alOy!oOEbd%A%hx@SHhQU~tuLhjn6N}cGZk@nPKC151uQ_gSY?x|aymyKSmKpXcn74LleB~A;%kE&{*U%g4>3#3K5p65Z^SArMPOG&eLa-a+a@0FNv@4>Zt+uk95~InKSv?!n&gr$j^p7ApHbhBP>au!T*BEMVt}9osOLK3ywc0p=dGK@VkY-)`Jw*HC3aV10M^F}wUdT4xg7Vg*b^6o?rfT%Vtq!1U*l8*y)M3<SNXL;qa@Kxiup_nyavapT`TK5ThXTs%8<A|l#=1O^#8l3U-vQRSJwZ72s(mfLv9bE0_W7G~^KQ!3=45nvKk6vb;D6IqTnLeag@B`zdyF)JCad259zk4UD(~v+>cE+bXAHcfvE`W!J_g0}JM9I^ysL&Xjcu?%tCpeFix=k~GGneo+Y`BQL$A}L7IO1)<&NtVUhTK;A!!yrsit3{vT%8a^e13vChwEU7V27{?L?*IhHa3}NjW98bd&0tXwwX`dVYv-EH-gK+Nr0J_?2fMt>EX*J+F^;Bq(>JR)R~=BStOLwpfbO=%qT`vUn^>CaXRi<}C{M?)DxO%(;g6o^{S1-F`|FdJ7?wma36+)CuhUSl5xwt*LcFnf>+ViPL$ejvZ1t>z5U-;F;JRg$m*nQK9wfn(|_}eMC?~qSM*Z(^qE^NWF*lu0gX<Io9_g_3o{=P!Gm`uE6-6Y+YJUw&7%~PP0h)MA`4VWbtc6q`pvsPEDS(rW1Qo$FEf2_m^TSJ~+(!ILxLff5IP(x5aHE`iaaIdMR=4nH^Oz*k=!qs_Dv;r$?>BQb#TR$B$&1?pNzF(J-_S5N}L0$8NP{=uf$oW9si2qO)p0pRzhk1!hy##a3dj`_k$62Y5t&Bnw?={BF@o%3iQ|IVv~(h#K{+^#Rk`au18)s2>V(*p|}<Te&LG32iAF+H#&s!%%gyz~u?l%9k%g4yUx5U%%7SAYv*PdZ*F?GB5`+Jpdxktm0)39_xp)H;uJC22L@m`*0nlNBU#Q&1+2{k5GF26yCs3p5l-H`_7zu|67^=7`_YNoqgbGB)NMrcDTqO(kru-)$YGI2nI+^elE*blek~LS$H1F_={0}nQ`zZFkJ<rL}U`rcr!nc<0>FZa&mc#8gY!D$;?zFr@pB6k7q8b2Eq@5qQ=<%#b^84-F_S!1I-n`BB9M|k-b=r*)PQP@<^5BHMw5;C-A=;&r1wf{pn;ck5P7fA<s(#D^P^%<u#Z`!u=Je=Wp*9Wjgq!M)zN4B)=KKA1!)@-C^oGjl%c#_`T{Rd~k^d2H{_BQv1m*QZG2J-9*Urx})09Y(4$jQEl^N@_oj%AKDo&JF6X;j{QDk+QvitLPOa-9;`N%Z8q$gXCKQS*lkYj&+%%b<X*eWYs{1H)?@oP`3nwXM;S_T+k|gDCr_3}`ZEWBhgX^L>}WhXJ%8f!Ri^fOX0U3Q^3NQE>+R5cooTpexFB=3zBUeLNQA3G#m>RT&W#m}!NmYyXzHrR5|xnnz2`nAtF+XvO8+CpxC{*A{>G~)=y%k^*!;n4k|!7Q8HHsF%<iU*=9{TOEOy<^#-}O+|39Zh_!Bw4TU6hY0d)j7+RviB4p2XT?xtUm`nuMU`O>u4hS5rz>yI^;UX#K)&b0SQb{#l|>3;h~%0}V!^>U25LD_;1i1&*S^<YMn9>uDE1Q6O1k!Gd3*jg6;QP5|cpjLBi^Q!=I;YgZ8W_V#<L5s@L;}rbHe0Np?6p1xf|GRbQIoZVgWhgFp(x3kE*T4S>cm3zz-fz5J4IPd9h%zAIFVwfvwKrk+L~%v$&wH*Z$OMtcOUv`+hON=Yz0)ut9mRgyG12%N7FSDP4LLJAwU>Aw0L>DDGP4}${!y0d7(@?@U*JZ<;?O@^yS%Xj$0EVf+Ak`d_Dd}<D+deg(X3iS{mrySV2D8BJampVMngf%2w)f%zU|vn*Yh&G{1~xu96I}LiuLDomaGj3>r*pkKkoY;QYcMtxTHBa%i%qinnZhLh?4C=ajRNZ5+fGfp78t&vA@*7Q~5@IVEFK-%xbqQpDn&uY4RcQnx~;U-qb>N8=zIsIpuFP0v@k|PPw;r-I#B+a<#HnS~X5-g_oXR4|mH{au6k3$>ES!z8cexC5llk)V3nb&AZOXS6*Y@KWx~urlokczf*fsL%}p$HV89^@8qlW9_pIS9R&MHG-oXo{O%Xugvp>f9e?{WmPhywYPH^Tz|pG7Wv6@9W1O~`+muTRmol8cQ-8t@KoKWO(D;dJ4bA6QryppjxHL_jTIEykv9#Vft937);0*H%Ff4?_-DHsygytrPvOnegZO9u!qXez&l1jLbP7dAjK|YULvNl6ntle>bC8mi6zmX#x8#SiBF|dN4NxT_L!K1XBwR6_`0yG>^NKiQotqN<$w{77Yp4PBu<bh3I*8~A~ia1^x<jm6s=Q-xKq|R3&cDwP7FU&^{c%v6#L}+rKoh%7~j=1uvD(CVW_Y*=VqR(2k&Dz~r%d0mrRyZ9_3YbyHE$q_xtF-{e8nn)h-zi(HFWDW%8$4Y2W9{wsdl>Zi5uJ|D>T5J(TM*-T75<EBg(<=ca{g9)8ES?#Tkm7Ay2|_7uwTA^^xnQb=ZzBjE)xNla=T0bTXLP+)Rf+NLod%C^1y6*rkC#n4s@V5Fo~RBp4y`HF-?#CYji^o0iR=<^=EP{#7w(BWWt}=FddBrK}*GkofROenUtjjsdv@JCJ*YhY%b?-K<&^%u%pc4E@x%hxO;l$7ig)ESGQjEU|Qz-m!o7Oy+@6|;~59Y+DY<7rx(iNX>gvQ<1Cq?XUv}}`ToE>0j)2l0dE!EXpJ5QUx)L<K)QD^FF*qFq6*lpe6*1o<IiR@3HDhkb;A6;rLzC`gN4uULgX^mn}P!fqIW3pI%lllps&za+wb}JZ=qN1QAh-A@)OmpE0QIK7|h8x)C*}{dyB2VNc1E4kRn<{DMVBqAGvG@Ny^HyW~z1#_Q8z!GhyHl{NMlA|NH;^AHL83?|+^7Q|D7U(J7yX(|DRr^JzJ)r^Me(r$l@#Ii-Q$&M8f&G@sIPO6!TvC*sf0iSmht6OAXDPBfor;f(B*&!?PDnSW(I<>8daQ=U$FKIP?<*VAx54e2z{X~;MK9Zth|8m7}QpN8c$tf%pO8q;Z{)0j^q-`RK?CyuSBaXF1EZ<f=PP7|G`e42*S#5X>jruj52r)fRS=hK`{Go9vqnupUoo@Rco`7|%5dF4a(X-TJrPD?&5!)X~$%XC`!v6s`bp4RheO{bMkYd)>RX&q1NbXw=r%5Md)h2P7WU(A``%$Z-!ncvNsU(T7|&Y54&ncvTuuao!3*WnG~72+M@CE_jOHR3(;i%k3`6X8Ykb^J0Dzs<z2Gx7UO{6Z7I(ZsJb@jFfYQd5RS_&R>CiC=8uH=Fp?CVsbxUvA>JoA~u6ey3@G>G(Q+vx#4A;&+?)<tBc+iC=Hx_nY_yCw{|egpK(+e#wd7a^lyV_&q0n(TU%5;#ZycT_=9oX~JUQ>-c>qe&LDVc;Z){_?;(y>51QZ;@6(|y{8$ghOgsSpZMJ;e));te&W}k`28m~Kw=9dHbGjjy!bk{LSi!{wnJh=B(_9iQzW)UVq+w>Mq05Bu@HGBvOS3HL2M6Vdl1`$*dE08AhrjwJt$$t@^x$vVtWwVgV-L#_8_(gu{{V28!KCuHeZLujn$3ijrENMjup=KAhrjwJt$)j@O5ktVtWwVgV-L#_8_(gu|0_GL2M5iuvz#zwg<62i0wga4`O=|+k@C1#P%Sz2aVWOd>z|^*dE08AhrjwJ&5f=Y!7045Zi+$Y(Kt^?Lll0VtWwVgV-L#_8_(gu|0_GK{NI#U&r<!wg<62i0wga4`O=|+k@C1#P*;C8=9|Udl1`$*dE08AhrjwJ&5f=Y!704(2AXpt<QU(?UC6YneCC;9+~Zt*&dngk=Y)Z?U56F1YgJY$ZU_y_Q-6H%=XA^kIeSSY>&+L$OLD?*Ree^+at3*GTS4wJu=%P!{xx|!0CwB;p^ac;CSG9;CkSD*dCefk=Y)Z?U4t#C%%sDk=Y)Z?UC6YneCC;9+~Zt*&dngkw^G3zK-pY*&dngk=Y)Z?UC6YneCC;9+~ZtCpbL5j_r}z9+~Zt*&dngk=Y)Z?UC6YneCBhct*aC?UC6YneCC;9+~Zt*&dngk=Y)Z?U5I_P`-}sk=Y)Z?UC6YneCC;9+~Zt*&dngkyrRyI9v9%Y>$EMF|a)bw#UHs7}y>I+hbsR3~Y}f!7KB1Y>$EMF|a)bw#UHs7}y>I+hbsR3~Y~q;J*1fg6rn%*d7DhV_<s>Y>$EMF|a)bw#Sg+;rTkY$H4X&*d7DhV_<s>2nL7-2nP}a_&NjvL;{2Y!~z5Zw#UHs7}y>I+hbsR3?l*tU&r<s*d7DhV_<s>Y>$EMF|a)bw#UHs7$!s(zK-oNussI0$H4X&*d7DhV_<s>Y>$EMG0X@-d>z|kV0#Q~kAdwmussI0$H4X&*d7DhV^|QY_&T=7!1fr}9s}EBV0#Q~kAdwmussI0$FL%(A*yj$V|$EjkCE*$vOPw&$H?{=*&ZX?V`O`b3E_{gV|$EjkCE*$vOPw&$H?{=*&ZX?V`O`bggD99u{}n%$H?{=*&ZX?V`O`bY>$!cF|s|zjDX75u{}n%$H?{=*&ZX?V`O`bY>$!cF|s|z0g;!lV|$EjkCE*$vOPvbXM|_OX9Q?OXbI7L9fCBXG{Q97V`O`bY>$!cF|s{Iw#PUjmh*LNkCE*$vOPw&$H?{=*&ZX?V`O`bY>#n9(C6#e9wXahWP6NkkCE*$vOPw&$H?{=*&gG9?0~OhdyH(4k?k?EJw~?2$o3f79wXahWP6M&(g@@coJg=eCbq}K_L$fn6We2AdrWMPiS045J*I?&gRf(IOl*&d?J==ECbq}K_L$fn6We2AdrXAPgs)?JOl*&d?J==ECbq}K_L$fn6We2AdrTQA3}46gnAjc@+hbyTOl*&d?J==ECbq}K_Lv6bI(!}5V`6(uY>$cUF|j=+w#UTwnAjc@+hZD$6!CRzkBRLuu{|c_O-P)OIU#jI?u6t?vM0U{`4bW-w#UTwnAjc@+hbyTOl*&d?J><rv-mo;$HexS*d7zxV`6(uY>$cUF|j=+w#T#}ALHxT9uwPRVtY(%kBRLuu{|cX$HexS*dEi0#0{Anr*3SIne8#NJ!ZDY%=Vbs9y8lxW_!$Rk2xX5<LlTSGuvZkd(24T|5y5j651K7t2d*aQ<2in{IDxt)cW+Kc19x0zkZfvwoGbg`FcxgXZhZi)XqqFD@pB)MEE1Aoe6(qzDsIn!rxmZsh#n=*hq86JIa#O&bgk{&iFeMuI1m0zm@Sj_(kJyu{me9;XL4F^S$G5u_<S^<&3|@)|}a#Guv}!gU<L{Bdo&L@!y*HZ_WI-X8v0<{uWzy#@}Mw&TQOyg8BG5-f%P9cZPvsVVD>;hLK@qm|5)1*TK?k>X~glv$1Ek_RQv<+1@i7e1^prEC{}iZ9cQnXSVtbv-5_VVRzneGaG(p%g-xT4weqD9k%_#wqMxx3)_BS+b?YUg>ApE?H9KFlCZ}3I=217wqMxx3)_BS+b>vYZ2N`R)xx%42#b-gV>>Tw--YeCu>BUc-@-Oq*k%jcYe51%;%ls2zLxE^uw53m$-*{S*d`0xWMP{uY?Fm;vJ6<_d>z|lVVf*$lZ9=vuuT@W$-*{S*d`0xWErs+__}f0?jMPCAgNuDY&Ryg3!Z~*y|Aqpw)MicUf9;lgw4o*pKZOctrxcS!nR)6)(hKuVOuY3>xFH-%s7Ygb!_Ve+Zy{C8yh<tTN`^Dn;Yj<Ik56|{2U8E$HLFC@N+Eu91B0kg6CjcFZ>+K3O4{hz>a{QW98>q`8ig8j+LKd<>y%WIaYp-m2JHyI1IjyZN0LsSGM)awqDuRE8BX78-WjDTdxGq!q>5_SGM)awqDuRE8BWyTd!>Em2JJUt=EiGHDAYeUfIqo+j(U>uWaX)?Yy#`SGM!Yc3uY@zxg`0^U8K!+0N?#_r=$-omaN=%64Aa&g-}(wJQ?BCnvS*i2vum&1+&E;WznjvyE4_@ya${*~aSxkbtja8?S8Rm2JGTjaRnu$~Iov#w*)+WgD+E94}wTHeT7rE8BQo()Rn=&MVt_Wjn8I=auceF7VR$8D9%W4o?nr0`LUz2>=vu=J4j?&c&a@p^HZsmo7eCoVs{*aqHsO#j(S)pOb_Dd;-q>4DWu1dq2a!pAjn02$pAr%QJwBGo1XHBx>Lj@abnb^E15m8Ls{ee|<&<x&@atobqxM!f!{y>Lk5<k^BdL9q#@NzkWslIRh3s0~a|XhMa+noB@rTfsLF8iF5b_;E^-%kuw02GZ2z9Ad)jMk~2V(Gf<K<V3PAFp%I@zP&p&2oDo*eh%0BHC1=1TXW%7g048T3Cg(|_DLw(v<P6m04A|rh+~f@4<P7BG4Cv$x?Bopa<UC6N#wUQEoB^PmfuNiLp`3xCoB^VofufuNqnv@GoEM4N_ynMoGq991z?3u4lr!LzGw_r%0F^Tkl`|lf^D1Fp;yi*mj3z08<OGrwNLC<ef#d~}7;KrrmKxv_k{n2OAnAeR2ZDMD>?ODt){i6!k|ju*AbEnIUjlzgsvrQEAYhU$2nHq~m?R96F-XcFIfEn(0)+_{CV7LPVFHH<9wxbiBo6|K2_`0>n4n?;iwQ0!z?dLo0*whaCV7M;5|T+sDj~UqAY=lO2}UL$nV@6>lL<~HK$#$A0+k6?CSaMMWdfH8UM7H<AZ7xY31%jsnV@C@n+a|vz?mRt0-XtVCg7Q%X9AxIekK5#AZP-i35F&hnxJR`qX~`%AT0q&OMudlo+sdGm;5{dSW7_G5}>sNY%Kv?OF-8W;I#yNEs-SHus<NS1dJ^KWJ^HV5@5CjoGp<6pOPd};*^~Z4En&J4-ERipnog|o$!M9AaueT&*HCS8vtu=z@Zb2bOE9h$?n0AKA`ACf>pO;(Fw)|7@c783mTnB{tEUYjGsu{oQ+5)EDu1^32OwHbizW3fYJ%8sRflzSb8n6biz9QN?bZ&6C~_{Ju;oJEpDOdM1n)(u?38l$C(A4P9(52UMBn)iGkqBNGv4yG%o+<Aa%m-e=KEBa2~fgdm>4hW!)l-N}Pd{hgTUT(f}^LfvXez%qYtn0P+oBo#1&AT#p7>C-|cThXl|%!7C+_b&og!$8-U%6Fk%fxlV9Z3BD@9StWR@J$jwsz7qV`1;0*kWVZlzf>%o<y9QYG2Zo(UKx_HYASiYsfv-0hJJAP@ooM^daz(NeTwsC^OeFtAR3h1Ah)X2kwp=j@qMhIp6MSMK0lE>W1?@(p#s%<?2@W#BL#Di4fmps>f@lsmiCSHPpG-Mj{wCaI5`T%RT@r_hx?Muy4nTK;*GzDmlcWtKc?13+eWKkdZ|I+VHK~Aif_DYto#0}h33(^@>s!n_p@{e_&^u+xlmPFq@<rYfYZNA1fbW#$JxPiMn6iR>^A8u!r1OzU|7w}^uLgW4q(09?z7z7OghVPKlS)~<2HsQ_w}Dd!(y4@eDj}gtl2M_&pCqM1fj=RqN|IEe#-C8+zhL1B)&51CB2eBBG&~{G^78A1RP2&qC*))aNm)WxM)GInl}vIa{s404n>_n~#Sd8gfW;43{D8#|Sp2nM@gpY>=H$bXlOH+xAFCN93BHJ)*CYTVx?U3y#sr8l0b@)6852;(1eh@aXG{PZlOT=ge@%cI6R^gV<(I;V18z)NHZz<!5XY2dHzUhCnpBQ#{K&?SZ2ZW^k8J$N#*b{g%*Mwf8$Yt~=V#*y<?f?5{7AdCv^!xs@5sBqHt$a8Gx?E;cS2LkqnUR?SImz}y;J`B+&jy!f2G`ekZ1kna_>Q2Szqowh|!;yd!vOb4Z+-7`n&?U_aMLJKKCBvm)_^z!}&{d??LYV$i1JCdrwF1edOMMG$j1zG^ZTt_<@2SDENVbA1L^Nf*&aOk%{jz@%hNak4*dzmWdBCeu)<&GnnPfWkT|ikbPKFmkFuKe(W+KSHWQ2k$WGx_mO)ax%ZKKAG!CDdmp*Cl6x;l?tSFmf4JNml{8pkkP;wlF-Vb5@@^8c7`n2aq(O>()eIcp%<>uhT6yuX+90GTM-qM{;YSjFB;iLAek9>X5`HA%Y7)L4N%*fvIhf@?$P2SD55j~3&f*hLo=D*LN+9@3!tgc7$Aqd-xC*!Q9iI@oLTUdJ!a`vz#GZo=MS>7Tf)Yg%nlETkB=CGC5Pc;ueI-zRC2)NukbNbveI?L+CGdSE5Pl^vekD+TC2)QvkbWhwekIU;CGdVF5Pu~wf2BcM{@`ap{*}P~l|cWM!2gv%0G7Z2mOufPzyX#(0+t3zzNO`F5#mLB0)7@$U<q7c31naiY+wm=U<rI+34~w?j9>|rU<sUH38Y|2f+Msm5~5=og*R%Jf8r#A)i6pc$}C?kAH$spnF%p7A!sIvnozY!qwFy(5X8+SjA4kJ386C~b|xVWljsS3iv)p-B&=bOxJb~rNJ1M1m5T)4ums|;B+OyscGkitumr#zmOvhsggp#;7YTwF3G`tJ{9y?MVhIdlNhri1dy$}fk%U8R6xK?itrXr$A+8kW%8j}bpOE96oaf{~ha~_Jj06>o1R}8nCb0x6u_Rn#kitmN!bl(!OTs1wIgA84u{6rt#S(xdMuH|r8s+U`2?(VabTN`}ia{A838@&gF%nqClF*7l9wP~_7z8pB6fzQs#gZ_KK_nwVB_ly5BS9x)kz2+xfLca^Tt*UlF$iWP@QW?Nyosd%-HZg`44e}Zh{kYGNRZG-!ZrpGjRX~q1R0G49gPGbjRYl)1SyR)iKoRHfSN{voJNA4MuMP5f}%!(q(*|KMuMnDf~rP>tVR;LF$ilUC~G9)8-un+g1AP4x<&%wSQ5rD2y7%MY$Ql*Bv6heaE>LAjwP^;C7~UI&_<GQ3aO2Rc$yGU6C!FtNKJ^T2|+a>swRZhgt(dzSQ8>^LTF8soa%+dR9H-f##DGrg~)VcGQ}t4jS875)&L|p(j>1GYhaRhiZy^pn-FRfVr@dOO^CJ$;Wi=OCIsAsh?@{{6Jl;c&`pTCNy08vITB<!lEhsIb0i78kmg8;yh+G^5qlGYZ$k7<2)_yOHz5EgMBs!FoFoQArXxY8BSEMmAqXc#;e;@p5Qh^2ags<p<Cr$dzwjv>)+YI4xt>fCq$-kVONg+9s7Q!>gy=?yKm@>-B<Kqumn4`A0G9;BB>{3tg1HFbBFGA0l>}TR0a!^uRuZ6<1Z*V%TuDGz65y2td?m?<4-l3Fh$R7INdQ?AP?iLkB>`ti09q1|mISCJ0c%MBTN2Qg1h^#uZ%F`L(k#zDT@Efnjy200z(N4_l4f}a!fPwUw!&;H)V9KHE9ABtyDdH;{I*yKz+n=Am;@vy0g6e$Vv>L{7zaw22TB+SN|*>r7zs+42}&3WN|*{t7z;|63rZLaN|+2v7!6984N4deN{cK6JTGR15{85l8WWRrCSpz~Noyh|g%WxblQ3rioJotEo$z9T(IkL02`EhhOp_K#y5I(Y)FePP30O@6Sd)O(B)~NZcufLelYrPHKsE`OO#*0>fZA+l8Q?Z)k)zinKgDOU7#2ByUC%PWauUFt1T-fB&Pl*?5&)e9L?;2#Nx*c{B6p8v0azyi*GT|&5|Ev=$VqIKukf)^Xom4ItPKD>3Fu7%9FxT10+2~SWD+2m1WYCYlu3&`0+t1EnY73w2#vVBPOJ?8G)WxqBF}-fvCNmV44|3>tR^kOfGiZq!htL#$ijjwgyQlhg$!BPkT*JHd<?4u;7wZOiLgq5-=sxY#qZBDi;#@VTf@o$u9E=lq(x3_cx%9S5&)hAgeL*wNx*m#K%NAY=Qzs*&ob%I@H{FCFIG`Vz-SXd+60s~0j5pBX%m3j1f(_rs!hOZ6TsR8v^K4>Ht|vc*d`#h36O09W}5)oCZM(nux$cvn*iJ<Ah!w7Z31?i0Ny5`w+ZlV0)CqS;HEXt1@p`*X92lCy!=%f_V1Zz0Q9C+`uDNRf%hf=zG;<1!u4>nif5DKg4~~+8RY&D82|+*V8IDsZ~_{f00*aayc|w|;3h!02^ebvh?{`ord8f4B7<a1KynkH+@ln6lp>B&#8HYkN)bmX;wVLY&-6VV>HCqszgqeZr;EUx5Sf!;afr=HNGqhafDoM!qZ5L3LX=Lc6emPC3GR25{8}m$*V+OicUq-ZA^J)1#)#f&m2~?UmpxMSBSk+_^dm(-QuHH5KT`D9NYM|4(qFG#Xcc4^UImdTt%B@|?5E_fBK#@JpCbJ!+MklYiu$L>e{TApA^-{nP>}!?4NwsQ6%|mC0Tmrk5dsw@P)LCyDiNX*Au3(ccS3X`L?=RYB19)bbRtA2I?I~EszP)kL?=RYB19)bbRtA2LUbZTCqiT*L>xlIAw(2HL?J{JLPQ}%6hcHHL=-|qAw(2HL?J{JI?Js=)d&%V5K#ybg%D8)5rq&@2oZ%4Q3w%*B%*xc@t;iag2#{YR>twEc>Jze$j0MGc`tI>lJ~N~?m8Y%=L#NA=k0qRcswCc5&|Wi<)_d`MWCef_ES7GG*S^L34xLjC<%d*5GV<Ok`O2ffszm?34xLjC<%d*5GV<Ok`O2ffszm?34xL%P>%8oq~WJ*7NYak1SG!z|HNqlVU!R?31O5FMhRh*5Jm}Mln_P<VU)1J2|Jvy#R+?yWRol1LWG@9Y3l}(i!pYMosdKncT>g1uM%Bc5yll|T#?3=Ic*u#mPu{wfFypEL`WB(zz%>%ptQ9FeKZVF+M0tt8iojtg3{I|Bwwvt!w|u1P`We>QQH24Uy4lv|3Ppd1P?-RA(XbRA^eR&hRWqD+8Tx^ZT&;I7<(pd-@`B1zK36cJ%fl$h{%M9Oo+$?4P*ieK!5=VH~;|%ARqw*D1bI8WGo~g0t7{5f+R9+n#i*Zx64oGn}#8RN-{wvnV^$QB9x4XOOQ(@(Mv|qC8#D-l26PsBab_nKN^Mz`pJ~!V^}_rP$tn(M(`ylDU(PkUmJ!9s>%deWrD6UCHXB_aFA9eXe$%Ml?m#~l;pQy!9ie|ps-9Lu`KH3cMU@X$z_~PNOYG)cv+N}MWcKc4dt`^6q7^JjU@9#SaYIQKFdfE7M=()Z;H&Td=J-Q^$AOW=#~R`At4J8@$zfS5D9Sr{5O3JFUeQ97x`;4z9jQY^4Da732RQYn}tO{Xas~uK=hkMz?q~$X_V{mG3in&TZTx~=Sb3jxizdqQK1tVI?<sMAv#fd7O7{Eq7$)aQF|7-XA!McT82nOphX2*WS~U{T7;lQp-v>~L<?HPphXQ@<e)_lS_Gj*5n3dnMST@5LnO-3+k3`36oF`x-j%zSArcwZMXV+LEMh1uOOcNj{b&)876oaMkQNPT5s?-ZX_1i@9cdAg7I=iDl|_t#btr18%QjYq&tfr(ys7wU(N$f<GV8dt43TI}3xXobs@Ikw0-8dAQwVqp0Z<_zDg;P{fT<8b6#}Y4LJACQheTi%=ng?;l|*G#JTatJ2`a0UH@*oOdBZP&Gla@2L1C4kuu4!@B~e$swhR$;Rtfs5lx18Fix66>goK|&s~RW`Wl<3qK8uae0v{74agh=iEph3ITI4!>7OPHxI>0srw2pw*5zsmUT1P<Z2xuJvts_C}fZ>opc0h3`%R|d~M1CJ!Aiz5k@DAV(34*uCi^b9dj7M4Gu)N(-rv1)a%Md|m@i@?gTZWFFp<i$SLPlcmiVhovt+f811O|}ibxD$?=#a*G(P2w8q=g#!%xTLnr0p2l0OC7Zd{2@}NN1|_%p!6jNTC<?B$<PB97@|KyzNQyg+-bn;j7?>;7Wd4&(Ie6CGS#sfi6?Y7Aug%^BpOWgmUqp@LP+k6)OSyLn>CHGlDbRBD^A^FoG}~A^hNtMy!NiL|+77#9p|61TX|%WPOOZh_wi{aQQf4Aj?BEMKDDyMJPoig_lPhMHodCg@;EBMF<TP7$iP678no%5&aPS5cUxD5cCl95b_Z55bzN15bhA|5bO})5a1Bs5Z(~o;QZmQ;iBPLvv?!E4*m!Z2_6Y92|kJKfiQ*uhWLf>h3JLgh1iAAg~)}Ng=mFfg)oIEg&>9SgusNjgs_Bwgm{EV1f^dH{X*v#62DORg}^WLeIbqpZ8RK+aUO;+8g$Vhi-xl>j>0$zLlO;&Xb?n$9vTk8I0NGd3@tQBq2c@sAvEZqK?V&fXpo|S;s6No!BG#2c`(0&njK{5U=9ZZI9R(u+KmDO$hMzdV8CEL=JGL?kJ&7YW??c5gISo%!dMojvM`i|nJkQCVIm6yS%bs|z77Eb5dt9sF#<t??SVNgjA3C43qx3#!NLd@Ca^Goh50LtUt#(R!&jKS!srzyuP}IpxhsraVd@G)SD3lN$Q358FmQ!=D~wxV+6u!~n6<*F6(+4PXoWc|j9H-)iXkh^SYgBp6IK|oLJbt-RhX{Aa24vGD1TzI3WHUsePXN%Q&p%TV5TZsLcrt{2B*9N0w55KOJQ0H_y=aCfPP?73fKqcq=0;2N(w_#n2`eNfe9%LNMSw-<58H7!f+I3qc9qU$tVm)VJ-?|QJ9LtP!wjOFcO7{s8K>UUx(n0=#B8r_P{6<CZRA0g*hmUL179CLr|E3!Uz;5pfCW1`6rA&Vfu-%p=9_8o(XUUVS5qw*C?4OehGfWM#0<@#-0ef4pUDUdcw>TMxJEiNn9BABZ=TPb|hg-680oz$%_%q;Lb4YBy&!Z@x!T2l5ZmElRC2G`?GwDuTJtW{AOf<Y$h3Pl01J)@!@5&+%o(uHa1~rQ<h{}ZX3=PyBk2oB<VUo0Op#eEfqleBcI@Vkz@cd4sH-LO&DpyL=*4{%ri}rm9OU`JC0|^M@!BhCOf7q$89;BuCh~PBo$v^E6NC@og-705xLJKnX;f?_gONDGRia3WT{a|YK$ZnIV=Eepwqyh(Qt!8#wl%;36u>^0+C5o0;sM4(I)}Mq#z-H?n$69fnc$E@j)aCGzeyk%=9eZN4|>RfQ*3#L2Bgt$Xf-i*(Jt9`pArhb`$vo3B~3!lVhRetYybS&568)khrJ`GP0Q>Lq>W-$ZsS^Mv`+)l7*{ikmtrezvRinOY}gZOvsuDX%iuD(sE@Ij-w&hvt>e>rKQV++$)+d(;!K+pD+_Lxl6`ONa?(knUM1ll0HJ#M@aj!7z)4oBX6cb)&c&=N9Ih!wjzdW?o3DwYsoVWaz9An7rAt~%by8JBq58uWYC0k@-~Gg<d%fw@{&XovP>G}8IWhn_CT_ElSn_>sYA$INmAEJDov8pD!FvRe%anDypqrjkmSzrq>@16sgMPKWYi=?1hS=&6qB$K$gYyyShkkz4`j%}%$kr&(;)UiGL6(~ko_bn^_E@}a%<X>YuVelX|bAYFJwo9m<`zx@@yJpgNfy^!;otel5HBqcGzXew+RV14Prj*H00cbq?-mY;3^(OTnK!~ZTAjsIe3|SlO*QwUcz^vHt>*qaF>9S)Hvl=!873Z(e?`w2XSn_q~RpFJ@%dS2;n4un~5h9JK^n0^8b;Hlbiwu`L6s2e@$)%{tS0RayuV6IpMxYP6py9NxlWoDWO%8>sfvv|H1Ep6UT9Z<VLXz<<Kz6cf|SPci`+W%NL{M=!APG+&tm#2?q(nNrG^cAlyD}_YViZJpfiC4itnF1&!k6#m$SK7e_CTu;C#11QH+EbQFg#9v?0rCk(<7gK)+m95M)}3>xM2!R>Dkf`z?32^K648-&vaZI1$cWP28QC0L-SpOVy1<-~#d=_KzEixlS$!oh>&<N?A3!qJ0p_8=TS2&WIi@q<9PKp<Qo5H1i17YJkvv^~%&(M!S?&>grL96*lzJ)FPiBY!{g_djy}{v+Y+Ne%`#Df=Xcghv2vJmOa&+Tf)jAU9^J4$c|^XAOa~MzVE*cEDS6&DX(SL%?_lAP<4Rh9)^=;C+L?Msjwvq}&4BB<(5Sv#BQSB#~v3Y+b$>C2gn4$lFQ!S_Che<VUz0`MHt06Cfo*<I4r^Cc%~_adGk^{Mqey;n!!m0`Em^kKgx!dlS$m0^D>#zG;%>fHeIE`zA2zNCJ;Qh6J7v%`O={A*>PN+Lps3x=9X?5O>Mp39*h4>~2wTLgc&T@PrUZh=GJ4cunFF4JC<}Gwviejy(1zi6=zKS{6@}tV(&jZC!4eJRyo+QhAzWnIdogK*b4sJ|yiqh^*Iaev;>(<$_W2d79)cU=1VI5`rxu+Fk&1n&fpX8$?dhwlm2~k^ETh40!YhPELr%gm5ewJ^FYqP&t7Bh!C4^Q+fg!&?ToQ1Z)B+&>k-*MDSa{oF>^OfVbu5*H6rx5Zy1JIU&qTE{|A$fz1g)pAhvWkw@q!#C`&)5P?*PKq^EC{)Ff+dHlTP<@iAAhtLTb1kLiDEr%yG8xb0fZeer+OA*Zi7r>oLo6#)L06Z#~iAdUvX1Q3>2W(2rei4Sh2$Nrg(J#X67h(8|F!@Co@giw6!hjcH!i&&mMABx2AumFkk)*=XD~ee!!mt-%+KVvmMVR*@415tLz6c{<G|MMoc}#r~#=Z!1UxdLg!sHi8s}W|u2*Y1APamK=+KmY9Mg(#q0yz<ZoQP&gp5?~G6^kzxXDr@WJ}drM9P;Lo@iFnqSk7oSBD5P3+KousjlfVuvn&gEW-t`dEDHl$8w^D>%gVs!215~np@_gxL|`Z)Fcc9OiU<rvB<)6EC?b#(5y*)MV_<|%BSNPUNv9FWiAXw)FiHi-EB%7fafG3;3knaXdI903QxMZ)gmE$WNO6&v8zT&kT|juk1Q}t3j4(q+7$Q6J_;4OS9C`ea#~*q8_i9VQkSt+JmX<Ad{kqPSFyekq;w!x=b^?!4U#ml<in+&=cLCj(?J6U8CrlgnG^%W<`yyVD+Im%-eEqgvMNihXh84o7^uA-|9&Nu%)CFwEX!Tv5jyY=&Z8x&?edkIoM_&YKmmA1iioOK<R|r$zfZJ)wA9y>VUs%cym;%3TVj+x#(;{hu*c!WWk>7&-xX7=;j>Kp<N&oO7zX!V#<Kcw)a9ZS7jncS<Phf9u1LCqf@m4X<O&I8wL>*JzT62q@r{A`>NR}>W`y#30B}o^s9lgkx9v70HWQ>b{WtR&r(<ME}L^>_vUzGG5bLzBgUPmV9@!G`sT+?%muG1op=$f8mjGdPGE<MLcJ7K2%(*Ck#=h7~{NP;UC6R#z1OR`+CnDo_2s(a1Om(7tax7qn3+hx6E=a`4DX6J&p@3M1gyxwK!i=@wZI%&q1?0k_#T3oGU)8cF;rI!0%#l5auc0O)jT#|Fl-xCJ#Nm{cpf=}!DlAKF_Hb(IY9iD^^PeO+$t>Tpt?^c0T5b@CAN$Bt-ba>J#`SW)1a!t<RQsGSrZJ&g;PeR)#q3x5<_DN{_B(#0fD%Zixt0aI@&X7<5TVp<rFrP-4-zN<46Xw&7Bt4v@k4KXJD<<i*ZjAX)?<FT;VT8+)QO^gv$q7@UBvYdBr>opK0;f!c?s9bcU~N2_WsYW<qgm!?mN}Ybj%JyoS>|Y#`9tUL(~-abYWX{XT+U433EU_IZWQ{UMUfnyHf9t9WEU3m50IU}RY$^R{zWsPw6UZc89Z&2ElvuLOykJmj~xEU;g1~t$l;G1{>b5v9R63z;pZcVKQQ<v41Uw7d=3V0waCyWXLR82NA7;)?nmx^<nBlAe&p^)?tbL%*W7(Ma`z*5Kl*2m{Qbz^kNo|}-+$Ho{pf%{I^d5E_+K)EUyls_kD%ZxW2%rd{819F1i>MK;82f<E5`WYA>km!Kd$mkzK{(JzlgDYcttox_(Y8C!z0dOXub}nW?N%eAHEQy`tXDp)W@9uq1O7n)mjMxR<9`6N~;`mrNeAnxY!Gm`~a^)?i~pXbVvz8qy!~Wf)pu1i<BTnN>C#u$dMBCNC|?Z1VvI><=l&y4na~9MbdzZD~W8WA>&F=lA~4n*2J!2Sh1{_R%|QAU7xGxN~?r(Su60doszD!ZmaBUin?Yf-QiDUsNLZ;=CiCuS&p(EWkJe{6n=jY{6q0BL-8&{@h(H@E<@=qL&+#Z=`KU*E<?#EpJnnI=Se8tWhmX{O^5YSnb#~&xT(3`%Dm<ean}!-*L*MYD#`m->AViIt>sT4(BtoYvCeD8lZei1-fr_w=QZQ5GqeITv;y;XS4co`R~dJeaaS34m2p=Yca?Eh8F!U&R~dJeaaS34m2p=Yca?EhdAqASo!5+;%(%(C-6Y7Iwwr{)!dX@v=GM2H#N;|O_A)f~GBoxwH1;yIn=&-^GBoxwH1;wy_A)f~vWU^%>%3-2?qx_hWk~L2NbY4w?qx{sWk~Mjv#fgvG2ou_Sr)zAGiKW%xtF1~m!YheA*z=ls+S?<lp(5@MVt0s=QTrPFGFK5Lt`&PV=qHvFGFK5BTLFilQQz8j6^9TQ_4t{G9Dr05wbi&5)F-wq5z)|tVX~Z(9;~5d@z$whb+>s*$e-bx=7Lm|CPc>MHBopsb+E#ELU`Pgkk2MZ6=HE<_+CU77fl1zL}ha+K>btCYN$1!=^b2o67cS`5v4YpkY`xC)q9nD`x?m@d<1j*f%HnE!aFTafXdEjGR$%$*^*UnKSI1VdxA?XHnjq=o6LCFnosPbJ{5KOfs4*Ohg_VjY}%&ve97qWvsu91(>k{GnQb+8q8RP8LKd38D^}*4Va%U$UIgg$vc*3oCKwxY~>`Z+ABJb<$DLuV=ZSa=8V-W06ms;#+uGp)H%ufLCn0>P{JD5xM>pBN1>vG-H@>zGWJ8phPblRU}t1(jf}k^1U1+o89PKMYOqZ*_K7GAqrRi!^r&Ttq!M;g##YMMOBtI<kb3MWkzTnX_1IrI2_XLo)hCkmhG3mURY|_sQPpHRe^S+C+P-toDVec5Z<GEkTNSbOlJ;k8+<o4kv6C~la>icHB)=<(b(4VhnWQfRp`?b|U-)XSn7vd#NbUkjIov?nN?;e%KEo|!_yrU%5{c@PT#uWO6(&n;TVwcbvdUzcNfAh@K(f%J4kR~<#Xu4rrCx;14u_H9F|xP})a<et6;-<|FCTTgOmfGAtYmxwn;nIRjOty+z31(=VNF!<GKvkE<eo=a{KCtGPhfYUj+X%gWK{ApI$kn-Mn;267N>z)UPdu5lWZESKDdnxzmefMGCW6y>&WmOS)2!IdKum$!+m7<j|>Nr;XyK7NQMu|a3UFMYZ+c7!;NJ4k<F%9zVId)?j*yXWH^)zkCFiwWVn<JpOWEJvUnA7D*_q_Y9O$I;06L52y!6Mfe5jQ5}OcRiC>Y5pEwq&`AN}F1ldH9P0D`aS;V!7ZxQDr-bLJt_!p`EiGvXjvlRfv#fXpDYJm8JNVG{6P|AQ(2b4k}>@KB1sRfFg5kDi2M#_QWX~fltuMuY>B|)hPin|eiBMwJAjtIAja+^rE2_KfY9Pv3)85B+|A;l7>Beg-{#S*V0DsEC86dgAaaudHJjz>I?xE}F6!jC1+M+DtO(M=@Xq)aH@M@X`SB}-_s#Q%u0n@GEf0}>A;Tv>VR#E~E1V=%lpBGGx1Gp?K}#TB8bp5cqKI3pAeGYaa*u^@abIP{?YILCsFAT8;k^qI(3Tep9%&1ZuQWG^Gi|Fpxw;{&o;8fjn~X{$j5kggg80O^LgJswC0Oofgz51WE@{csTJ&dHL*SK4#(u-(<F_UGh{n;W-D(pDm0;Zq1#KvMG{1d9k)(iS7JS6X1C)kWG`q+MleMUfViER>A+1op19m`HocAgwF%1oX8Ms<hpvoP0VcDnpGr(hVbBFoPID5_{Pfh_;e5OIHgzS+Zn?=wQjniZl8-G8#HEIyy31I`Sa)K(rmiAc(d|HgBa>g|ITC(<5&m!LOO*Tlh5y!RP?V=m5#+_sD4Y$mssa==#WmoJ-^^f)I?3kBp9wjE;|tj*pCvk3w#Bkk%diD&ek_MkD;DMNTvLO?O>9gUGMq^6g(_uvli%1HI|u$s!K=aWcrF5?Uz-WRVZOsRv}y5^d05&1g!=XiCXwO37#{&*&x30Jbxb?F?u;1KZ93w=>Y~40t;O-_8KIGZ5~K{*;Ucl?;eG1LKw#GN!GaCj;#k^8@nE!m5t4SqAc*rRN-#vyA?gj0TpB4wj6L?u?G^JPJ`M*5N3JM%+I-xidPs^C&?R^qMd<y12#8=;Y350ueK#n>(Ws<RaFZ(bX-sL}&Mf&oZOKyCk&C((`>Gw9IJ!-d-KlPj6IPGn&COn!)oZ=UnMVlXoE}T{&`GPXgn%z;V-}9xR8CMJ~oKkQ2!DB!CX_j1KWElBx27&~X2u<(fr6^`kLAi;}9m8*CKOQ~hYn&*&h}=pfG`ttzq&&{q|EKx7pg8%;GC-Q;<ccPe))FBSV^lolUcA#Yah7>cW#{IPt0xC*@HQSKg%G9MDJS(I3BG+wjFvd(htdfNUr1X|@!ON$R*D}Q*UPm$M*R`gqy*NnFGi^^+8d%7gXXmH8WqAoc*`qc5WjJ}<WUiFM#^^9Ki3<Z;m%xi{vNrnPRhEmA({~*KN{sT%}-V4wI$$)V(zPiY~W~hT?sDfmCD}Q_sI0a5jAQjF+DlCd1PyxwM0Rh2$Mq^Kw&Ylm7`7A9y$Z+$<FrS4#SlH+*GOt-^>W{QOn%2{i)*tlphs^8IdEeA||I2De<w*pIzEnFZ<G22B?WimPwMRQD%j10{^I0Cx){e?}`X8hnbu{N6!?nk7?J-<?r1;eo|4@ScW2N|6a*k)E_!-H|KE=;SW)20ZKbV5lF-Cig(H>*8N2Y#c>PM!2Wa?j#sUKReM~}?|JvP%9@>u>_JvK=)x0WWGJW0MM(cretW|Glgy!0%dS!=YJB<cJvjW$O*f28wAI)9||M>>C`^G7=WNIHM0!XA^ff7D6ZuLRw<8CvO-XrG})PetB(Dv;w#4@KH?dr9Z<6%sP(n^0zG^EBQL(M~d{S{tIxaD;bLw9;ZBtrZ6(f8_8-4u9nEM-G4F@J9~+syY0j40|-s{Gpp?j{f+Anf}P%kNo|}-;ezL$ls6r{hQ_QhbrtJQ&}oclAj9%yWFAh8Joa@;qxTlz?GQdpXA$H`kt|2E=YWy1OUd?5oCAz%-}Qjk(R<|Y_3ZVpJkWbB=K2>+*$>uvP{LDB{?EV<TG}wp2>ee@)>)%hRJ7a@*mL&pC@st^5FB<R5OWd^%D3Dx3l5z%h~USmjqsHv}_!f8LsLMeZNcJm-g&EPr{`h<Ejyoxk(5YZ&LS3C>^)lUFhZDKP7jcga)sHtY#AGw0-hEf#ze{DAS7cJx{{hf|s<?J!d5x^<Dlxtsnd}@Z1@$J5Rz6vVL+_!jb1mm?l0bE8)^Je0qjc&+zIQZas@%|0J!%i@M9<@z%gh0~V4DkDuZ4uSq<7e}?nV@ctR@Us&UWkmfUs=O19Yb^IJ<73#|MGll0Xru#wG8F{&q!{=F&^>&u}eG1RNXjN1AJmWVYs6e_%PDYR~k~S|$7zxo4WQ;BuJpV&JC0}9Pg8yZdtCx+7W(En)C<i4N0_z0I9l}He`3@l>f_}#(iO&%1z)4_`Q`bihpJ(BjN!JuUL(2nc{FcSbOfvsTwwUnGK;c7JhGyZQ;a|_|9H~1p_bdAh^goccBWo9SAP@q<SP%sf>X}*iX%INi!aS296LQN%pP?CYo33XFh*(lme8F6j(S!E=A|}OGELWx(<iACpo}o)3`R+}cE;KWerX$b2Wa&t9g=7XYCV3X)U`x$nol%ai@>AIWxV=&4y4MeqNvN9SS*(P^@jP8fCTB60>@l2?A#jpK|7rUzqW>f>S<cI-OG58N=w{~aKluE7s~?r;ZTsQ#B5rljkIJ)bMX~JWP4Q>Noo)wip_0PyTjU4$EsOjBzZ5JtVoYq#8M|}F_MByZ!mG?;bL`N0yG~fCgq8|h9(G^gJr;NmXr$yt`bv}hV8VZph{01pD<v=DDdeZ{5YS7>i+Bil14yRiMW{Sixeg!0tA=(;#tc@*3|3w?H7Q(-_YD=5yvX5bmG9wC!Usc6B|}doFWa>Jk*hc4>W2#K!9{a$(HvO&fwdo4`>SE?fkb_g@BW}f{T6KR&eNgt_KW1{5Ucy@JbjVW;n6&OkwYE!*CKiLU7ntoe96-xwU?o_cOdEqqW(fz`l0lCWa&qieq`xKmVRXEM@P)j5p#6J933%7{{C(9cRKW4|Ck*yy;G?K{dY;-*C+7H(551fn}#n~<<8;sASS<0-<w-uj{N<|-;ezL$ls6r{Z5-{!CDh-rcHdRPn&5O21A=^0jOVSGeO;|)Mi>_>7ujdqRq6(rn=K+T96OiX)`Ty%d@O<`p{-tWcQ)va*>?jqRq6(16;J3mQgO9Ked^bQ9iPMYBMd<`Cgl8!65`4FUv$n5`QG|uav|eYOF^Re<blo5`QG|M-qP|@dpThfbdZeJ};6m-zD(;J?y&e6foT+@cd8g&q*#>)dW5-vfGtr_XXmz*Jk$x6Jv|q#U%d}?X~eHf#-kXlp>8;a-b14W;x8r@e93Ki?|5!5u(bxOqXVN(Q!-XErI8ME}sc}UL-p&6L@wjG7N-E;8>O|ZI`d|O#;vV9E=2h&2q_jB=GSB{?J`L68Iy5KN9#Ofj<)XBZ2>A6L{p5gq-rW0e+vqBipvx-;pivQ+FiCm*#gumP!~&CZwt)sp>551iKPb2sDcu!HZiq7X$|aM<gjJ1`P;<286tnBrnAzFk!NQkeAXTGIH2X7!;sIhC=yW0>2jc8h!t?$UMEwg~Iw<&brE1LVznj#jnIG#@s8RpPrV@pM7+~(<};jc<o3~39a;m1XU(h7rf@JlOFH-b7FN_FDU#r@p_q9rCA&<o>S6V8FZD5789$4#Fb>Ib%n(+)XHDUf3Qu@@-g`-zwPY{d|>muaJ}2LaJIM>myt}dt}=-_%XM(WNYg+5vu+cs{2%-YQOHJsS!F_f`vL9@vk|xiNj$`?p<@jRYyL5Q10u&t;`!nFw;5IZ8mx&`u7jCZ$qwa^Bq1S7$}YKzM2x&;@cf@6gKx;-4_VbCgKx{=alx}Pc&h`R|I++**}KRzv0KWTPSa}XH04$P(IV6oN!;&rnnL2Lm&9F?7~KDg`-p0*Uf5)+;;Ki=ex&S2%6?$(2j+hC%p5&4FO#qz>Z(V=en9RA<bFWzNB(}~@4s~Zo`IjXK<@m3<(j)^z^fVXYF;I47bk)Pzx<GHXlDd;736&uR6s5*k@qaP>@1lBHt4#2cG{5l|G&NS>22c%qWE|5*@xkdwY%(1H5Awg92v5ENPt480=*?j+Ed~0UjE+Ns#YRbELyZ^!9xT&;&5j<{PXz8nQ_I5jnfa~5%cb_whm$IB5Yya9oE*x+7fc-59*yTI~}2QM7_H%Wkglt{Y1Sx3z|n^6OR-1?yN|z)#yOIJL{51RXU^IqaM-g<26{MM?F!v`Hgx{|JR>V@9F=BSL%J3coS4%?uUBsh$s0<z2E3hB&4ziFxW`cyG{%g+*OJ7G_qF;>xwFR0a5RaH#qt9Exu9jy(Vqy><`p?uMf=zv_-Gzu!wQ*CjzlvsrU2;PgQ*80{NbPMIG+>#K9->J$*x#c`Odc<a_#4zoMAV9ste_%hzK0mRhx8`G(~imTy?TVflvT8yDZW_{POIF8;rR-&<PM{~dmZ-GJOU3nIy89Q+Q|!5u?l8571B{0`Mo!tXF3;CJE}6S|nohcF<-CngLr^asob#0R{`Fg*-NhjcO~qzB=9iQda)LkJH-_Y%1mwga+*u)PHAh3Oz%FVT9TIK*&7{bwqe3=FeDU|x6)Xbo5m5@*0^3^H^ohpCgTp)+7J$cq7&K|%~%gaYU+0M7#WECA5b2aT$^gWV3PcLEqK0MY^|EdbL3I4uCw0!S?Y)zSwN=~YODF=`;DcOnNyAR7-i2yqG`0S5UmNPj{03zA=u`-0RLB)uT#1t~AcctOGo@?DVWf<zbOxgf&@2`<QQL3)c(OCsOt&Z%rNBN3R1kW74IA{!IQm>9-{FeU&6p(h9-L7)i2LJ$Ok7!ZVhAl3uX9f<2dL<eFy5W#`C4Gpz7)ZS2gL+uT<H`Lxx`@f3XTQb##+8b(bsJ#NUOaIkS1=>fQ*3Lour4*`!ZX;qFLE4DVMpOr)IN)%Hza1`dIK#;oj$>Zj-f(!s-wh`>eB5ws!><izHXOC^Uc-3}w>2Uy;IxLj8s2K727M}*UIec+4#jaX!=(&oGTg}Ubi+Lj$25G#@DIa13{Ntg!|)BmdyJFm$tO%lQ!Jx#>bQ)BUO&(j(p^W+ETfz(chku-%P5D+-E^qTGRjeM7v*inG8(~oQD;?3Ov@4))2ndy%nbrA5O76+8v-1<aX!Y;*mSa$-j_oy&a^nv;slFxe$MrEjvq&T@I={FhLvSyTG>{{jeiZcpQcYu74p97E6lMg{-t(K9f3iQooP~9lm?|eX--;`#-uH$rkr{if2ESCA!$dNkyfM;X~R??=n?5ls+Vn!sW+-Ssz0hjsz)lTFaCNK)OqQ>Y$J_*q_L4Sc9O;o5+kLNv6nP9lg4h+I`wxXnAuIsgw_cy6j~`*DyTkCeW3b4^?~XG)d#8%R3BV#$O1w2f$GC+^^}`_Kq1x+V*#*kocvV}(7opJOdhxAJXXVvhP58WLeKNkHy-c$KmExoGTR!ntufo$jaE(+X0|nETVu90W?N&nHD+65wl!v3W45)Go}pi9bE(NXWh_)i3>LI@vPh*5tR$@fAZX=i<!I$-<!I$-<!I$-<!I$-<!I$-<!I$-<!I%TRyb@K9$PkQDx(5+z>|_(V40L8R;8)O5oU8zl4zC2{@u8zV%$@)UXvjb+*2{)(-`+tj6J+@4aGRl7SIsV2<o3~>Wy8!v8}g3(<v1U`jraQ@41JA&Ti`T(wT5GM$8x+H3K8TMI0l9jIqHtcK8Mk6#x+e32I$J$Qbu>j4i(r6UU;`V5bT|Ne)bMaFPR*9HitxCFd2KS8%-oaLK_-9z@iLsS#C^#y~^z)kwajT5U+aA^C>nYxwu^&(rVT3v|{&d1p>%ax8K04qnPo@6M&mzngidH;8x#LDLs55%11C-OzkP^9{{6G~dvCL-YSEnt!>z`u6kZFW(ZN|LySY>ihNk&F<sX_1l*O`oDhu^_QQnzDu@wxz3i{{qW)TZvXVSeV!HfeDQbd-NR=0w0~Id-f!j-H+hNs+s*!Vw^={zpYFDgGl^AR;&Jo5zg@rE%*ytKviF}pt<P&7@}-|1w%g~s`^~w)m>2lC-hJ3VJ#Tk&W#YW_Q4?mHezjD*uKi~+Wg`Sz5UaPuOe|}Tuq04rlbJ}_FiV<MS?8p&as~?Ff<)d%p<5QK9xG>(3ziy|C3D6KenBR0uhp_tt;x;=^HvM<COK(=ieYswQ5abl#1^b}L9%*$ok?bg*d>{~)y8G1TC1H27OXaxI=n~LUS2F)7+-x!U||9rN;1{fIg-harm<MMX5Kq0Uu%mak%ATGGv1LNIXiT=P`YZ&%tXqz=t5blY>lofOI3`MdHJkGIxkBUZPMM8h4NPE=8Da0u9(oy1oE~yY2{O?>gnuMuzI|l3RW2DOr&N7Iu$AppJ7q1V6FLNb5tmc7~(?df}Iu~urP*(ved#DT6k8@Jd5S?V`wZ(l*iD*V~S(w$Cuv$UEG@c')))
_ROUTES={int(k):[_R108_DATA['actions'][i] for i in ids] for k,ids in _R108_DATA['routes'].items()}
_R108_SHOP_ROUTES={tuple(r['shops']):r['route'] for r in _R108_DATA['shops']}
del _R108_DATA
_SETTINGS={'hand_align': True, 'weed_repair': True, 'sell_lead': True, 'budget_guard': False, 'room_guard': False, 'clamp_sells': False, 'dead_stock': False, 'terminal_liquidation': False, 'front_run': False}

# EXP241: fixed two-policy choice, learned with five whole-team held-out folds.
# The full-fit tree and all five fold trees use only first-two-shop YARN_STORE count.
# V39 handles yarn-specialized worlds; EXP240 handles the other shop combinations.
_R110_OLD_SHOPS={('BAKERY', 'BAKERY'): 0, ('BAKERY', 'BRUNCH_SPOT'): 0, ('BAKERY', 'FARMERS_MARKET'): 0, ('BAKERY', 'ICE_CREAM_SHOP'): 0, ('BAKERY', 'PET_CAFE'): 0, ('BAKERY', 'PIZZA_SHOP'): 0, ('BAKERY', 'SMOOTHIE_SHOP'): 0, ('BAKERY', 'YARN_STORE'): 3, ('BRUNCH_SPOT', 'BAKERY'): 0, ('BRUNCH_SPOT', 'BRUNCH_SPOT'): 0, ('BRUNCH_SPOT', 'FARMERS_MARKET'): 0, ('BRUNCH_SPOT', 'ICE_CREAM_SHOP'): 0, ('BRUNCH_SPOT', 'PET_CAFE'): 0, ('BRUNCH_SPOT', 'PIZZA_SHOP'): 0, ('BRUNCH_SPOT', 'SMOOTHIE_SHOP'): 0, ('BRUNCH_SPOT', 'YARN_STORE'): 3, ('FARMERS_MARKET', 'BAKERY'): 0, ('FARMERS_MARKET', 'BRUNCH_SPOT'): 0, ('FARMERS_MARKET', 'FARMERS_MARKET'): 0, ('FARMERS_MARKET', 'ICE_CREAM_SHOP'): 0, ('FARMERS_MARKET', 'PET_CAFE'): 0, ('FARMERS_MARKET', 'PIZZA_SHOP'): 0, ('FARMERS_MARKET', 'SMOOTHIE_SHOP'): 0, ('FARMERS_MARKET', 'YARN_STORE'): 5, ('ICE_CREAM_SHOP', 'BAKERY'): 0, ('ICE_CREAM_SHOP', 'BRUNCH_SPOT'): 0, ('ICE_CREAM_SHOP', 'FARMERS_MARKET'): 0, ('ICE_CREAM_SHOP', 'ICE_CREAM_SHOP'): 0, ('ICE_CREAM_SHOP', 'PET_CAFE'): 0, ('ICE_CREAM_SHOP', 'PIZZA_SHOP'): 0, ('ICE_CREAM_SHOP', 'SMOOTHIE_SHOP'): 0, ('ICE_CREAM_SHOP', 'YARN_STORE'): 6, ('PET_CAFE', 'BAKERY'): 0, ('PET_CAFE', 'BRUNCH_SPOT'): 0, ('PET_CAFE', 'FARMERS_MARKET'): 0, ('PET_CAFE', 'ICE_CREAM_SHOP'): 0, ('PET_CAFE', 'PET_CAFE'): 0, ('PET_CAFE', 'PIZZA_SHOP'): 0, ('PET_CAFE', 'SMOOTHIE_SHOP'): 0, ('PET_CAFE', 'YARN_STORE'): 11, ('PIZZA_SHOP', 'BAKERY'): 0, ('PIZZA_SHOP', 'BRUNCH_SPOT'): 0, ('PIZZA_SHOP', 'FARMERS_MARKET'): 0, ('PIZZA_SHOP', 'ICE_CREAM_SHOP'): 0, ('PIZZA_SHOP', 'PET_CAFE'): 0, ('PIZZA_SHOP', 'PIZZA_SHOP'): 0, ('PIZZA_SHOP', 'SMOOTHIE_SHOP'): 0, ('PIZZA_SHOP', 'YARN_STORE'): 7, ('SMOOTHIE_SHOP', 'BAKERY'): 0, ('SMOOTHIE_SHOP', 'BRUNCH_SPOT'): 0, ('SMOOTHIE_SHOP', 'FARMERS_MARKET'): 0, ('SMOOTHIE_SHOP', 'ICE_CREAM_SHOP'): 0, ('SMOOTHIE_SHOP', 'PET_CAFE'): 0, ('SMOOTHIE_SHOP', 'PIZZA_SHOP'): 0, ('SMOOTHIE_SHOP', 'SMOOTHIE_SHOP'): 0, ('SMOOTHIE_SHOP', 'YARN_STORE'): 8, ('YARN_STORE', 'BAKERY'): 9, ('YARN_STORE', 'BRUNCH_SPOT'): 9, ('YARN_STORE', 'FARMERS_MARKET'): 3, ('YARN_STORE', 'ICE_CREAM_SHOP'): 9, ('YARN_STORE', 'PET_CAFE'): 10, ('YARN_STORE', 'PIZZA_SHOP'): 6, ('YARN_STORE', 'SMOOTHIE_SHOP'): 11, ('YARN_STORE', 'YARN_STORE'): 12}

_V92_TABLE={('BAKERY', 'YARN_STORE'): 9, ('BRUNCH_SPOT', 'YARN_STORE'): 9, ('FARMERS_MARKET', 'YARN_STORE'): 9, ('ICE_CREAM_SHOP', 'YARN_STORE'): 9, ('PET_CAFE', 'YARN_STORE'): 9, ('PIZZA_SHOP', 'YARN_STORE'): 9, ('SMOOTHIE_SHOP', 'YARN_STORE'): 9, ('YARN_STORE', 'BAKERY'): 9, ('YARN_STORE', 'BRUNCH_SPOT'): 9, ('YARN_STORE', 'FARMERS_MARKET'): 9, ('YARN_STORE', 'ICE_CREAM_SHOP'): 9, ('YARN_STORE', 'PET_CAFE'): 9, ('YARN_STORE', 'PIZZA_SHOP'): 9, ('YARN_STORE', 'SMOOTHIE_SHOP'): 9, ('YARN_STORE', 'YARN_STORE'): 9}

_V93_ROUTE_BY_RIVAL = {(229.0, 9989): 128}
def _router(observation,step,state):
    if step==2:
        try:
            _rv=observation['farms'][1-int(observation['player'])]
            state['rkey']=(round(float(_rv['money']),3), int(observation['market']['inventory']['WHEAT']))
        except Exception:
            state['rkey']=None
    if step>=144 and not state.get('day6'):
        shops=tuple((_get(_get(observation,'town',{}),'unlocked_shops',[]) or [])[:2])
        use_new=shops.count('YARN_STORE')<=0
        state['expert']='EXP240' if use_new else 'V39'
        state['route']=_R108_SHOP_ROUTES.get(shops,100) if use_new else _R110_OLD_SHOPS.get(shops,0)
        state['route']=_V92_TABLE.get(shops,state['route'])
        if 'YARN_STORE' in shops and state.get('rkey') in _V93_ROUTE_BY_RIVAL:
            state['route']=_V93_ROUTE_BY_RIVAL[state['rkey']]
        state['day6']=True
    if step>=648 and not state.get('day27'):
        state['route']=2
        state['day27']=True
    return state.get('route',0)

_R42_OPENING=[['BUY_PRODUCT', 'WHEAT', 13], ['BUY_PRODUCT', 'WHEAT', 30], ['SELL', 'WHEAT', 30]]
for _r42_tape in _ROUTES.values():
    _r42_tape[0]=dict(_r42_tape[0],market=[list(o) for o in _R42_OPENING])
del _r42_tape
_IMPL=make_agent(_ROUTES,router=_router,**_SETTINGS)
_IMPL.chassis.diagnostics['terminal_rescue_errors']=0

def agent(observation,configuration=None):
    try:
        action=_IMPL(observation,configuration)
        pass
        return action
    except Exception:
        return {'farmer':['PASS'],'hands':[],'market':[]}

_SHOP_PARENT=agent
del agent

def agent(observation,configuration=None):
    action=_SHOP_PARENT(observation,configuration)
    try:
        if _step_of(observation)>=718:
            view=_View(observation,_int(_get(observation,'player',0)),_IMPL.chassis.cfg)
            units=[]
            for i,pos in enumerate(view.positions):
                units.append(['DROP'] if _shed_adjacent(pos,view.board) and view.inv(i) else ['PASS'])
            action={'farmer':units[0],'hands':units[1:],'market':[]}
            projected=_IMPL.chassis._projected_shed(action,view)
            action['market']=[['SELL',item,projected.get(item,0)] for item in PRODUCTS if projected.get(item,0)>0]
            action['market'].sort(key=lambda o:-view.prices.get(o[1],0)*o[2])
    except Exception:
        _IMPL.chassis.diagnostics['terminal_rescue_errors'] += 1
    return action

# EXP-154 modifications: Ahmed Berat Ozer; public capabilities credited below.
# Dmitrii Gluzdov Seven Turn Rescue and Kaggle engine contributors, Apache-2.0.

_UNIT_NS={"__name__":"v28_own_unit_model"}
exec('# SPDX-License-Identifier: Apache-2.0\n# Extracted Kaggle / kaggle-environments contributor code; see NOTICE.txt.\n"""Exact deterministic unit/decay semantics extracted from kaggle-environments 1.32.7.\nSource kaggriculture.py SHA256 bc8a54879ef02c7ea64b8b333d6a976f0ea65c4949149d01f463f23bccee653e.\nNo interpreter, market RNG, policy controls, or replay content is included.\n"""\n\nENGINE_VERSION = "1.32.7"\nSOURCE_SHA256 = "bc8a54879ef02c7ea64b8b333d6a976f0ea65c4949149d01f463f23bccee653e"\n\nCROPS = {\n    "WHEAT":      {"seed": 10, "first_yield_day": 2, "max_yield_day": 4, "interval": 0, "max_yield": 6, "ongoing": False},\n    "CARROT":     {"seed": 20, "first_yield_day": 2, "max_yield_day": 3, "interval": 0, "max_yield": 4, "ongoing": False},\n    "TOMATO":     {"seed": 50, "first_yield_day": 8, "max_yield_day": 8, "interval": 1, "max_yield": 4, "ongoing": True},\n    "STRAWBERRY": {"seed": 100, "first_yield_day": 10, "max_yield_day": 10, "interval": 2, "max_yield": 4, "ongoing": True},\n    "MELON":      {"seed": 80, "first_yield_day": 10, "max_yield_day": 12, "interval": 0, "max_yield": 6, "ongoing": False},\n}\n\nANIMALS = {\n    "GOOSE": {"cost": 300, "structure": "COOP",    "first_yield_day": 4, "interval": 1, "max_held": 4, "product": "EGG"},\n    "COW":   {"cost": 400, "structure": "PASTURE", "first_yield_day": 8, "interval": 2, "max_held": 6, "product": "MILK"},\n    "SHEEP": {"cost": 500, "structure": "PASTURE", "first_yield_day": 6, "interval": 3, "max_held": 6, "product": "WOOL"},\n}\n\nPRODUCTS = ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL", "FERTILIZER"]\n\nFARMER_MOVES = {\n    "NORTH": (0, -1),\n    "SOUTH": (0, 1),\n    "EAST":  (1, 0),\n    "WEST":  (-1, 0),\n}\n\ndef _shed_access_tiles(board_size):\n    """Four inner-corner tiles around the shed, in NWSE order."""\n    half = board_size // 2\n    return [(half - 1, half - 1), (half, half - 1), (half - 1, half), (half, half)]\n\ndef _is_shed_adjacent(pos, board_size):\n    return tuple(pos) in {(x, y) for (x, y) in _shed_access_tiles(board_size)}\n\ndef _new_plant(crop, day, turns_per_day):\n    cd = CROPS[crop]\n    return {\n        "kind": "PLANT",\n        "crop": crop,\n        "planted_day": day,\n        "watered_today": False,\n        "consecutive_unwatered": 1,  # planting day counts as unwatered\n        "yield_units": 0 if cd["ongoing"] else 1,\n        "max_lifespan_step": (-1 if cd["ongoing"] else (day + cd["max_yield_day"] + 1) * turns_per_day),\n        "fertilized_until_day": -1,\n    }\n\ndef _new_animal(animal, day):\n    a = ANIMALS[animal]\n    return {\n        "kind": a["structure"],\n        "animal": animal,\n        "placed_day": day,\n        "yield_units": 0,\n        "consecutive_unfed": 0,\n        "fed_today": False,\n        "cared_today": False,\n        "fertilizer_available": False,\n        "pending_care_bonus": 0,\n    }\n\ndef _farmer_position(farm, idx):\n    """idx 0 = main farmer, 1+ = hand index."""\n    if idx == 0:\n        return farm["farmer"]\n    return farm["hands"][idx - 1] if idx - 1 < len(farm["hands"]) else None\n\ndef _set_farmer_position(farm, idx, pos):\n    if idx == 0:\n        farm["farmer"] = list(pos)\n    else:\n        farm["hands"][idx - 1] = list(pos)\n\ndef _farmer_inventory(private, idx):\n    """Inventories list is [main_farmer, *hands]; grow it if idx is past the end."""\n    while len(private["inventories"]) <= idx:\n        private["inventories"].append({})\n    return private["inventories"][idx]\n\ndef _inv_add(inv, item, n=1):\n    inv[item] = inv.get(item, 0) + n\n\ndef _inv_take(inv, item, n=1):\n    if inv.get(item, 0) < n:\n        return False\n    inv[item] -= n\n    if inv[item] == 0:\n        del inv[item]\n    return True\n\ndef _apply_unit_action(farm, private, idx, action, board_size, day, turns_per_day, shed_capacity=100):\n    """Process one farmer/hand\'s action. Invalid / illegal actions are silent no-ops."""\n    if not isinstance(action, list) or not action:\n        return\n    op = action[0]\n    pos = _farmer_position(farm, idx)\n    if pos is None:\n        return\n    fx, fy = pos[0], pos[1]\n    inv = _farmer_inventory(private, idx)\n\n    if op in FARMER_MOVES:\n        dx, dy = FARMER_MOVES[op]\n        nx, ny = fx + dx, fy + dy\n        if not (0 <= nx < board_size and 0 <= ny < board_size):\n            return\n        # Movement onto LOCKED tiles is allowed: a hand can spawn on a locked\n        # shed-access tile, and blocking movement would strand it there forever.\n        # Tile operations (PLANT, WATER, etc.) still no-op on LOCKED tiles.\n        _set_farmer_position(farm, idx, (nx, ny))\n        return\n\n    if op == "PASS":\n        return\n\n    tile = farm["tiles"][fy][fx]\n\n    # Shed operations resolve before the LOCKED guard. They use the tile only as\n    # a standing position -- the shed itself is always owned -- and three of the\n    # four shed-access tiles start LOCKED, so guarding them first would make the\n    # shed unreachable from those tiles.\n    if op == "DROP":\n        if not _is_shed_adjacent((fx, fy), board_size):\n            return\n        shed = private["shed"]\n        for item, n in list(inv.items()):\n            if n <= 0:\n                del inv[item]\n                continue\n            room = max(0, shed_capacity - sum(shed.values()))\n            take = min(n, room)\n            if take > 0:\n                shed[item] = shed.get(item, 0) + take\n            del inv[item]\n        return\n\n    if op == "PICKUP":\n        if not _is_shed_adjacent((fx, fy), board_size):\n            return\n        if len(action) < 2:\n            return\n        item = action[1]\n        n = int(action[2]) if len(action) >= 3 else 1\n        if n <= 0:\n            return\n        # Seeds live in private["seeds"] and are consumed directly by PLANT;\n        # they never pass through farmer inventory or the shed.\n        available = private["shed"].get(item, 0)\n        n = min(n, available)\n        if n <= 0:\n            return\n        private["shed"][item] -= n\n        _inv_add(inv, item, n)\n        return\n\n    if op == "PLACE":\n        if len(action) < 2:\n            return\n        item = action[1]\n        # Animal placement: standing on a matching unoccupied structure. A LOCKED\n        # tile is the string "LOCKED", never a dict, so this branch cannot match\n        # there and PLACE falls through to the shed path below.\n        if (\n            item in ANIMALS\n            and isinstance(tile, dict)\n            and tile.get("kind") == ANIMALS[item]["structure"]\n            and "animal" not in tile\n        ):\n            if _inv_take(inv, item, 1):\n                farm["tiles"][fy][fx] = _new_animal(item, day)\n            return\n        # Shed drop: orthogonally adjacent to the shed; obeys shedCapacity.\n        if _is_shed_adjacent((fx, fy), board_size):\n            n = int(action[2]) if len(action) >= 3 else 1\n            if n <= 0:\n                return\n            n = min(n, inv.get(item, 0))\n            if n <= 0:\n                return\n            current = sum(private["shed"].values())\n            room = max(0, shed_capacity - current)\n            n = min(n, room)\n            if n <= 0:\n                return\n            inv[item] -= n\n            if inv[item] == 0:\n                del inv[item]\n            private["shed"][item] = private["shed"].get(item, 0) + n\n        return\n\n    # Everything below mutates the tile the unit stands on, so it requires that\n    # tile to be owned.\n    if tile == "LOCKED":\n        return\n\n    if op == "PLANT":\n        if len(action) < 2:\n            return\n        crop = action[1]\n        if crop not in CROPS:\n            return\n        if tile is not None:\n            return\n        if private["seeds"].get(crop, 0) <= 0:\n            return\n        private["seeds"][crop] -= 1\n        farm["tiles"][fy][fx] = _new_plant(crop, day, turns_per_day)\n        return\n\n    if op == "WATER":\n        if not (isinstance(tile, dict) and tile.get("kind") == "PLANT"):\n            return\n        if tile["watered_today"]:\n            return\n        tile["watered_today"] = True\n        crop_data = CROPS[tile["crop"]]\n        if not crop_data["ongoing"]:\n            age_days = day - tile["planted_day"]\n            window_start = (crop_data["max_yield_day"] + 1) // 2\n            if window_start <= age_days <= crop_data["max_yield_day"]:\n                bonus = 2 if tile["fertilized_until_day"] >= day else 1\n                tile["yield_units"] = min(crop_data["max_yield"], tile["yield_units"] + bonus)\n        return\n\n    if op == "HARVEST":\n        if not isinstance(tile, dict):\n            return\n        if tile.get("yield_units", 0) <= 0:\n            return\n        if tile.get("kind") == "PLANT":\n            crop_data = CROPS[tile["crop"]]\n            if day - tile["planted_day"] < crop_data["first_yield_day"]:\n                # Ongoing crops only accumulate yield_units after first_yield_day,\n                # so reaching here with yield_units > 0 indicates a bug.\n                if crop_data["ongoing"]:\n                    print(\n                        f"WARNING: HARVEST on immature ongoing {tile[\'crop\']} "\n                        f"(planted day {tile[\'planted_day\']}, current day {day}, "\n                        f"first_yield_day {crop_data[\'first_yield_day\']}, "\n                        f"yield_units {tile[\'yield_units\']}); should never happen"\n                    )\n                return\n            units = tile["yield_units"]\n            tile["yield_units"] = 0\n            _inv_add(inv, tile["crop"], units)\n            if not crop_data["ongoing"]:\n                farm["tiles"][fy][fx] = None\n        elif "animal" in tile:\n            units = tile["yield_units"]\n            tile["yield_units"] = 0\n            _inv_add(inv, ANIMALS[tile["animal"]]["product"], units)\n        return\n\n    if op == "FERTILIZE":\n        if not (isinstance(tile, dict) and tile.get("kind") == "PLANT"):\n            return\n        if not _inv_take(inv, "FERTILIZER", 1):\n            return\n        # Active for `day`, `day+1`, `day+2` (3 days inclusive).\n        tile["fertilized_until_day"] = max(tile.get("fertilized_until_day", -1), day + 2)\n        return\n\n    if op == "DIG":\n        if tile is None:\n            return\n        # Removes plants, weeds, empty coop/pasture. Does NOT remove a placed animal.\n        if isinstance(tile, dict) and "animal" in tile:\n            return\n        farm["tiles"][fy][fx] = None\n        return\n\n    if op == "BUILD_COOP":\n        if tile is not None:\n            return\n        farm["tiles"][fy][fx] = {"kind": "COOP"}\n        return\n\n    if op == "BUILD_PASTURE":\n        if tile is not None:\n            return\n        farm["tiles"][fy][fx] = {"kind": "PASTURE"}\n        return\n\n    if op == "FEED":\n        if not (isinstance(tile, dict) and "animal" in tile):\n            return\n        if tile["fed_today"]:\n            return\n        if not _inv_take(inv, "WHEAT", 1):\n            return\n        tile["fed_today"] = True\n        return\n\n    if op == "COLLECT_FERTILIZER":\n        if not (isinstance(tile, dict) and "animal" in tile):\n            return\n        if not tile["fertilizer_available"]:\n            return\n        tile["fertilizer_available"] = False\n        _inv_add(inv, "FERTILIZER", 1)\n        return\n\n    if op == "CARE":\n        if not (isinstance(tile, dict) and "animal" in tile):\n            return\n        if tile["cared_today"]:\n            return\n        tile["cared_today"] = True\n        return\n\ndef _decay_plants(farm, step):\n    board_size = len(farm["tiles"])\n    for y in range(board_size):\n        for x in range(board_size):\n            tile = farm["tiles"][y][x]\n            if not isinstance(tile, dict) or tile.get("kind") != "PLANT":\n                continue\n            mls = tile["max_lifespan_step"]\n            if mls < 0 or step < mls:\n                continue\n            if (step - mls) % 2 != 0:\n                continue\n            tile["yield_units"] -= 1\n            if tile["yield_units"] <= 0:\n                farm["tiles"][y][x] = {"kind": "WEED"}\n\n',_UNIT_NS)
_PLANNER_NS=dict(_UNIT_NS)
exec('"""E182 modification: Shop0909 last-seven-turn physical closure planner.\n\nNo engine imports, policy tapes, replay fixtures, RNG or remote calls.\nThe only supported market continuation is SELL; unknown execution abstains.\n"""\nfrom copy import deepcopy\nfrom time import perf_counter\nSTART, FINAL = (712, 718)\nOPS = set(FARMER_MOVES) | {\'PASS\', \'DROP\', \'PICKUP\', \'PLACE\', \'PLANT\', \'WATER\', \'HARVEST\', \'FERTILIZE\', \'DIG\', \'BUILD_COOP\', \'BUILD_PASTURE\', \'FEED\', \'CARE\', \'COLLECT_FERTILIZER\'}\nITEMS = tuple(PRODUCTS) + tuple(ANIMALS)\n\nclass Unsupported(ValueError):\n    pass\n\ndef _get(obj, key, default=None):\n    return obj.get(key, default) if isinstance(obj, dict) else getattr(obj, key, default)\n\ndef _settings(config):\n    size, turns, last = (_get(config, k, d) for k, d in [(\'boardSize\', 10), (\'turnsPerDay\', 24), (\'episodeSteps\', 720)])\n    if (size, turns, last) != (10, 24, 720):\n        raise Unsupported(\'requires pinned 10x10/24/720 terminal window\')\n    cap = int(_get(config, \'shedCapacity\', 100))\n    orders = min(10, int(_get(config, \'maxMarketOrdersPerTurn\', 10)))\n    if cap < 1 or orders < 1:\n        raise Unsupported(\'invalid capacity/order limit\')\n    return (size, turns, cap, orders)\n\ndef physical_state(obs):\n    """Comparable own physical state; market prices and bank are intentionally excluded."""\n    seat = int(_get(obs, \'player\', 0))\n    farm = _get(obs, \'farms\')[seat]\n    return ({k: v for k, v in farm.items() if k != \'money\'}, _get(obs, \'private\'))\n\ndef _commands(action, n):\n    return [action.get(\'farmer\', [\'PASS\']), *action.get(\'hands\', [])][:n] + [[\'PASS\'] for _ in range(max(0, n - 1 - len(action.get(\'hands\', []))))]\n\ndef _clone_state(farm, private):\n    f = dict(farm)\n    f[\'tiles\'] = [[dict(tile) if isinstance(tile, dict) else tile for tile in row] for row in farm[\'tiles\']]\n    f[\'farmer\'] = list(farm[\'farmer\'])\n    f[\'hands\'] = [list(pos) for pos in farm[\'hands\']]\n    f[\'unlocked_quadrants\'] = list(farm[\'unlocked_quadrants\'])\n    pr = dict(private)\n    pr[\'shed\'], pr[\'seeds\'] = (dict(private[\'shed\']), dict(private[\'seeds\']))\n    pr[\'inventories\'] = [dict(inv) for inv in private[\'inventories\']]\n    return (f, pr)\n\ndef _clone_schedule(schedule):\n    result = []\n    for action in schedule:\n        value = dict(action)\n        if \'farmer\' in action:\n            value[\'farmer\'] = list(action[\'farmer\'])\n        for key in [\'hands\', \'market\']:\n            if key in action:\n                value[key] = [list(command) for command in action[key]]\n        result.append(value)\n    return result\n\ndef _validate(schedule, n, orders):\n    for action in schedule:\n        if not isinstance(action, dict) or set(action) - {\'farmer\', \'hands\', \'market\'}:\n            raise Unsupported(\'unknown action shape\')\n        if not isinstance(action.get(\'hands\', []), list):\n            raise Unsupported(\'hands must be a list\')\n        for command in [action.get(\'farmer\', [\'PASS\']), *action.get(\'hands\', [])]:\n            if not isinstance(command, list) or not command or command[0] not in OPS:\n                raise Unsupported(\'unknown/malformed unit operation\')\n            if command[0] in {\'PICKUP\', \'PLACE\', \'PLANT\'}:\n                if len(command) < 2 or command[1] not in ITEMS:\n                    raise Unsupported(\'unknown unit item\')\n                if len(command) > 2 and (not isinstance(command[2], int)):\n                    raise Unsupported(\'noninteger unit quantity\')\n        market = action.get(\'market\', [])\n        if not isinstance(market, list) or len(market) > orders:\n            raise Unsupported(\'market order shape/cap\')\n        for order in market:\n            if not isinstance(order, list) or len(order) != 3 or order[0] != \'SELL\' or (order[1] not in PRODUCTS) or (not isinstance(order[2], int)) or (order[2] <= 0):\n                raise Unsupported(\'baseline market must contain positive integer SELL only\')\n\ndef liquidation(shed, inherited_market, max_orders=10):\n    """Use actual post-unit stock; retain first parent item ordering, then stable product order."""\n    items = []\n    for order in inherited_market:\n        if order[1] not in items:\n            items.append(order[1])\n    items += [item for item in PRODUCTS if item not in items]\n    orders = [[\'SELL\', item, int(shed.get(item, 0))] for item in items if shed.get(item, 0) > 0]\n    if len(orders) > min(10, max_orders):\n        raise Unsupported(\'actual final stock exceeds order slots\')\n    return orders\n\ndef shop_liquidation(farm, private, prices):\n    """Exact original final worker/drop and market rule, with current stock/prices."""\n    return liquidate(FarmView({\'player\': 0, \'farms\': [farm], \'private\': private, \'market\': {\'prices\': prices}}))\n\ndef simulate(obs, config, schedule, *, final_liquidate=False, detailed=False, preserve_final_commands=False):\n    """Exact own unit/decay and SELL-stock transitions. No claim to simulate shared prices."""\n    size, turns, cap, order_cap = _settings(config)\n    step = int(_get(obs, \'step\', -1))\n    if step < START or step + len(schedule) - 1 > FINAL or (not schedule):\n        raise Unsupported(\'outside 712..718; no day boundary or terminal auto-drop\')\n    if any(((t + 1) % turns == 0 for t in range(step, step + len(schedule)))):\n        raise Unsupported(\'day boundary\')\n    farm0, private0 = physical_state(obs)\n    farm, private = _clone_state(farm0, private0)\n    n = 1 + len(farm[\'hands\'])\n    if len(private[\'inventories\']) != n or n > 32:\n        raise Unsupported(\'invalid/unbounded worker inventory shape\')\n    _validate(schedule, n, order_cap)\n    deposited = [dict() for _ in range(n)]\n    sold = {}\n    snapshots, rows, events = ([], [], [])\n    executed = _clone_schedule(schedule)\n    overflow = 0\n    for offset, action in enumerate(executed):\n        t = step + offset\n        if detailed:\n            snapshots.append(_clone_state(farm, private))\n        if t == FINAL and (not preserve_final_commands):\n            action = shop_liquidation(farm, private, _get(obs, \'market\')[\'prices\'])\n            executed[offset] = action\n        all_commands = [action.get(\'farmer\', [\'PASS\']), *action.get(\'hands\', [])]\n        demand = {}\n        for command in all_commands:\n            if command[0] == \'PLANT\':\n                demand[command[1]] = demand.get(command[1], 0) + 1\n        blocked = {item for item, count in demand.items() if count > private[\'seeds\'].get(item, 0)}\n        for actor, command in enumerate(_commands(action, n)):\n            if command[0] == \'PLANT\' and command[1] in blocked:\n                command = [\'PASS\']\n            pos = farm[\'farmer\'] if actor == 0 else farm[\'hands\'][actor - 1]\n            xy = tuple(pos)\n            inv = private[\'inventories\'][actor]\n            before_inv = dict(inv) if command[0] in {\'DROP\', \'HARVEST\', \'COLLECT_FERTILIZER\'} else None\n            before_shed = dict(private[\'shed\']) if command[0] in {\'DROP\', \'PLACE\'} else None\n            _apply_unit_action(farm, private, actor, command, size, t // turns, turns, cap)\n            if before_shed is not None:\n                delta = {item: amount - before_shed.get(item, 0) for item, amount in private[\'shed\'].items() if amount > before_shed.get(item, 0)}\n                for item, amount in delta.items():\n                    deposited[actor][item] = deposited[actor].get(item, 0) + amount\n                if delta:\n                    events.append({\'offset\': offset, \'actor\': actor, \'op\': command[0], \'xy\': xy, \'deposited\': delta})\n                if command[0] == \'DROP\':\n                    overflow += sum((max(0, amount - inv.get(item, 0) - delta.get(item, 0)) for item, amount in before_inv.items()))\n            if command[0] in {\'HARVEST\', \'COLLECT_FERTILIZER\'}:\n                delta = {item: amount - before_inv.get(item, 0) for item, amount in inv.items() if amount > before_inv.get(item, 0)}\n                if delta:\n                    events.append({\'offset\': offset, \'actor\': actor, \'op\': command[0], \'xy\': xy, \'acquired\': delta})\n        pre_market = dict(private[\'shed\'])\n        if t == FINAL and preserve_final_commands and final_liquidate:\n            action[\'market\'] = liquidation(pre_market, [], order_cap)\n            prices = _get(obs, \'market\')[\'prices\']\n            action[\'market\'].sort(key=lambda order: -int(prices.get(order[1], 0)) * order[2])\n        for _, item, requested in action.get(\'market\', []):\n            quantity = min(requested, private[\'shed\'].get(item, 0), 99999)\n            if quantity > 0:\n                private[\'shed\'][item] -= quantity\n                sold[item] = sold.get(item, 0) + quantity\n        _decay_plants(farm, t)\n        rows.append({\'pre_market_shed\': pre_market, \'post_market_shed\': dict(private[\'shed\']), \'deposited_by_actor\': [dict(v) for v in deposited], \'sold\': dict(sold)})\n    if detailed:\n        snapshots.append(_clone_state(farm, private))\n    return {\'rows\': rows, \'states\': snapshots, \'events\': events, \'actions\': executed, \'overflow_units\': overflow, \'farm\': farm, \'private\': private, \'sold\': sold}\n\ndef _ge(left, right):\n    return all((left.get(item, 0) >= value for item, value in right.items()))\n\ndef dominates(candidate, baseline):\n    """Preserve every baseline worker\'s actual deposit prefixes and shed availability."""\n    if candidate[\'overflow_units\']:\n        return False\n    for new, old in zip(candidate[\'rows\'], baseline[\'rows\']):\n        if not _ge(new[\'pre_market_shed\'], old[\'pre_market_shed\']):\n            return False\n        if not _ge(new[\'sold\'], old[\'sold\']):\n            return False\n        if any((not _ge(a, b) for a, b in zip(new[\'deposited_by_actor\'], old[\'deposited_by_actor\']))):\n            return False\n    return True\n\ndef _value(run, prices):\n    shed = run[\'private\'][\'shed\']\n    return sum(((run[\'sold\'].get(item, 0) + shed.get(item, 0)) * prices[item] for item in PRODUCTS))\n\ndef _walk(start, end):\n    x, y = start\n    tx, ty = end\n    return [[\'EAST\']] * max(0, tx - x) + [[\'WEST\']] * max(0, x - tx) + [[\'SOUTH\']] * max(0, ty - y) + [[\'NORTH\']] * max(0, y - ty)\n\ndef _return(pos):\n    targets = _shed_access_tiles(10)\n    target = min(targets, key=lambda xy: (abs(pos[0] - xy[0]) + abs(pos[1] - xy[1]), targets.index(xy)))\n    return _walk(pos, target) + [[\'DROP\']]\n\ndef _proposals(run, actor, prices, max_per_actor):\n    """One/two resource bundles plus direct carry closure, replacing a baseline suffix."""\n    owners = {}\n    for event in run[\'events\']:\n        if \'acquired\' in event:\n            owners.setdefault((tuple(event[\'xy\']), event[\'op\']), set()).add(event[\'actor\'])\n    proposals = []\n    seen = set()\n    horizon = len(run[\'rows\'])\n    for offset in range(horizon):\n        farm, private = run[\'states\'][offset]\n        pos = tuple(farm[\'farmer\'] if actor == 0 else farm[\'hands\'][actor - 1])\n        inventory = private[\'inventories\'][actor]\n        carried = sum((prices.get(item, 0) * count for item, count in inventory.items()))\n        prefix_deposits = run[\'rows\'][offset - 1][\'deposited_by_actor\'][actor] if offset else {}\n        future_deposits = run[\'rows\'][-1][\'deposited_by_actor\'][actor]\n        obligation = sum((prices.get(item, 0) * (count - prefix_deposits.get(item, 0)) for item, count in future_deposits.items()))\n        bundles = []\n        for y, row in enumerate(farm[\'tiles\']):\n            for x, tile in enumerate(row):\n                if not isinstance(tile, dict):\n                    continue\n                xy, operations, value = ((x, y), [], 0)\n                if tile.get(\'yield_units\', 0) > 0:\n                    item = tile.get(\'crop\') if tile.get(\'kind\') == \'PLANT\' else ANIMALS.get(tile.get(\'animal\'), {}).get(\'product\')\n                    mature = item and (\'animal\' in tile or (START + offset) // 24 - tile[\'planted_day\'] >= CROPS[item][\'first_yield_day\'])\n                    if mature and (not owners.get((xy, \'HARVEST\'), set()) - {actor}):\n                        operations.append([\'HARVEST\'])\n                        value += prices[item] * tile[\'yield_units\']\n                if tile.get(\'fertilizer_available\') and \'animal\' in tile and (not owners.get((xy, \'COLLECT_FERTILIZER\'), set()) - {actor}):\n                    operations.append([\'COLLECT_FERTILIZER\'])\n                    value += prices[\'FERTILIZER\']\n                if operations:\n                    distance = len(_walk(pos, xy)) + len(operations) + len(_return(xy))\n                    if distance <= horizon - offset:\n                        bundles.append((xy, operations, value, distance))\n        bundles.sort(key=lambda b: (-b[2] / b[3], -b[2], b[0]))\n        variants = [([], carried)] if carried else []\n        for xy, ops, value, _ in bundles[:6]:\n            variants.append(([(xy, ops)], carried + value))\n        for first in bundles[:3]:\n            for second in bundles[:3]:\n                if first[0] != second[0]:\n                    variants.append(([(first[0], first[1]), (second[0], second[1])], carried + first[2] + second[2]))\n        for stops, value in variants:\n            route, cursor = ([], pos)\n            for xy, ops in stops:\n                route += _walk(cursor, xy) + ops\n                cursor = xy\n            route += _return(cursor)\n            if len(route) > horizon - offset:\n                continue\n            route += [[\'PASS\']] * (horizon - offset - len(route))\n            key = (offset, tuple((tuple(c) for c in route)))\n            if key not in seen:\n                seen.add(key)\n                proposals.append((value - obligation, offset, route, len(stops)))\n    proposals.sort(key=lambda p: (-p[0], p[1], p[2]))\n    direct = [p for p in proposals if p[3] == 0 and p[0] > 0][:2]\n    chosen = direct + [p for p in proposals if p not in direct]\n    return chosen[:max_per_actor]\n\ndef plan_terminal(obs, config, baseline_remaining, *, max_simulations=64, passes=1, proposals_per_actor=4):\n    """At 712 accept seven actions; positive physical delivery is mandatory."""\n    begun = perf_counter()\n    fallback = {\'accepted\': False, \'reason\': \'\', \'actions\': None, \'simulations\': 0}\n    try:\n        if int(_get(obs, \'step\', -1)) != START or len(baseline_remaining) != FINAL - START + 1:\n            raise Unsupported(\'planning requires step 712 and exactly seven actions through 718\')\n        max_simulations = min(256, max(1, int(max_simulations)))\n        passes = min(2, max(1, int(passes)))\n        proposals_per_actor = min(16, max(1, int(proposals_per_actor)))\n        baseline = simulate(obs, config, baseline_remaining, detailed=True)\n        prices = {item: max(1, float(_get(obs, \'market\', {}).get(\'prices\', {}).get(item, 1))) for item in PRODUCTS}\n        current, best = (_clone_schedule(baseline_remaining), baseline)\n        baseline_value = best_value = _value(baseline, prices)\n        changes, simulations = ([], 0)\n        n = len(baseline[\'private\'][\'inventories\'])\n        for sweep in range(passes):\n            improved = False\n            for actor in range(n):\n                winner = None\n                for _, offset, route, bundle_count in _proposals(best, actor, prices, proposals_per_actor):\n                    if simulations >= max_simulations:\n                        break\n                    trial = _clone_schedule(current)\n                    for i, command in enumerate(route, offset):\n                        if actor == 0:\n                            trial[i][\'farmer\'] = command\n                        else:\n                            trial[i].setdefault(\'hands\', [])\n                            while len(trial[i][\'hands\']) < n - 1:\n                                trial[i][\'hands\'].append([\'PASS\'])\n                            trial[i][\'hands\'][actor - 1] = command\n                    evaluated = simulate(obs, config, trial)\n                    simulations += 1\n                    score = _value(evaluated, prices)\n                    if score > best_value and dominates(evaluated, baseline):\n                        required = {(tuple(e[\'xy\']), e[\'op\'], e[\'actor\']): e[\'acquired\'] for e in best[\'events\'] if \'acquired\' in e and e[\'actor\'] != actor}\n                        acquired = {}\n                        for e in evaluated[\'events\']:\n                            if \'acquired\' in e:\n                                key = (tuple(e[\'xy\']), e[\'op\'], e[\'actor\'])\n                                dst = acquired.setdefault(key, {})\n                                for item, amount in e[\'acquired\'].items():\n                                    dst[item] = dst.get(item, 0) + amount\n                        if all((_ge(acquired.get(k, {}), v) for k, v in required.items())):\n                            winner, best_value = ((trial, offset, bundle_count), score)\n                if winner:\n                    current, offset, bundle_count = winner\n                    best = simulate(obs, config, current, detailed=True)\n                    changes.append({\'pass\': sweep, \'actor\': actor, \'from_step\': START + offset, \'resource_bundles\': bundle_count, \'estimated_stock_value\': best_value})\n                    improved = True\n                if simulations >= max_simulations:\n                    break\n            if not improved or simulations >= max_simulations:\n                break\n        if not changes or best_value <= baseline_value:\n            return {**fallback, \'reason\': \'no positive physical delivery gain\', \'simulations\': simulations, \'changed_workers\': [], \'changes\': [], \'certificate\': {\'stock_value_gain_at_initial_prices\': 0, \'sold_unit_delta\': dict.fromkeys(PRODUCTS, 0)}, \'planning_ms\': (perf_counter() - begun) * 1000}\n        final = simulate(obs, config, current, final_liquidate=True, detailed=True)\n        physical = simulate(obs, config, current)\n        if not dominates(physical, baseline):\n            raise Unsupported(\'no zero-overflow dominating continuation\')\n        delta = {item: final[\'sold\'].get(item, 0) - baseline[\'sold\'].get(item, 0) for item in PRODUCTS}\n        deposited_gain = any((final[\'rows\'][-1][\'deposited_by_actor\'][actor].get(item, 0) > baseline[\'rows\'][-1][\'deposited_by_actor\'][actor].get(item, 0) for actor in range(n) for item in PRODUCTS))\n        worker_change = any((_commands(new, n) != _commands(old, n) for new, old in zip(final[\'actions\'], baseline[\'actions\'])))\n        accepted = worker_change and deposited_gain and any((v > 0 for v in delta.values())) and all((v >= 0 for v in delta.values()))\n        plan = {\'accepted\': accepted, \'reason\': \'joint physical dominance\' if accepted else \'no improvement\', \'baseline\': _clone_schedule(baseline_remaining), \'actions\': final[\'actions\'], \'expected_states\': final[\'states\'][:-1], \'simulations\': simulations, \'changes\': changes, \'abandoned\': False, \'changed_workers\': sorted({c[\'actor\'] for c in changes}), \'certificate\': {\'baseline_rows\': baseline[\'rows\'], \'physical_rows\': physical[\'rows\'], \'baseline_overflow\': baseline[\'overflow_units\'], \'candidate_overflow\': final[\'overflow_units\'], \'sold_unit_delta\': delta, \'stock_value_gain_at_initial_prices\': best_value - baseline_value, \'baseline_final_shed\': baseline[\'private\'][\'shed\'], \'final_shed\': final[\'private\'][\'shed\'], \'positive_physical_deposit_gain\': deposited_gain, \'markets_712_717_unchanged\': all((final[\'actions\'][i].get(\'market\', []) == baseline_remaining[i].get(\'market\', []) for i in range(FINAL - START)))}}\n    except (Unsupported, KeyError, TypeError, ValueError, IndexError) as exc:\n        plan = {**fallback, \'reason\': str(exc)}\n    plan[\'planning_ms\'] = (perf_counter() - begun) * 1000\n    return plan\n\ndef _effective_action(action, n):\n    return (_commands(action, n), action.get(\'market\', []))\n\ndef _recover_observed(obs, config, parent_action, plan):\n    """Bounded cargo salvage after deviation; never resume old positional commands."""\n    farm, private = physical_state(obs)\n    positions = [farm[\'farmer\'], *farm[\'hands\']]\n    remaining = FINAL - int(_get(obs, \'step\')) + 1\n    room = max(0, int(_get(config, \'shedCapacity\', 100)) - sum(private[\'shed\'].values()))\n    commands = []\n    problems = []\n    prices = _get(obs, \'market\', {}).get(\'prices\', {})\n    for actor, (pos, inv) in enumerate(zip(positions, private[\'inventories\'])):\n        command = [\'PASS\']\n        if any((v > 0 for v in inv.values())):\n            route = _return(pos)\n            if len(route) > remaining:\n                problems.append({\'actor\': actor, \'reason\': \'unreachable cargo\'})\n            elif len(route) > 1:\n                command = route[0]\n            elif sum((max(0, q) for q in inv.values())) <= room:\n                command = [\'DROP\']\n                room -= sum((max(0, q) for q in inv.values()))\n            else:\n                items = [item for item in PRODUCTS if inv.get(item, 0) > 0]\n                if room and items:\n                    item = max(items, key=lambda i: (prices.get(i, 1) * min(inv[i], room), -PRODUCTS.index(i)))\n                    quantity = min(inv[item], room)\n                    command = [\'PLACE\', item, quantity]\n                    room -= quantity\n                else:\n                    problems.append({\'actor\': actor, \'reason\': \'no shed capacity\'})\n        commands.append(command)\n    action = {\'farmer\': commands[0], \'hands\': commands[1:], \'market\': deepcopy(parent_action.get(\'market\', []))}\n    if int(_get(obs, \'step\')) == FINAL:\n        action[\'market\'] = []\n        action = simulate(obs, config, [action], final_liquidate=True, preserve_final_commands=True)[\'actions\'][0]\n    plan[\'recovery_steps\'] = plan.get(\'recovery_steps\', 0) + 1\n    if problems:\n        plan.setdefault(\'recovery_failures\', []).append({\'step\': int(_get(obs, \'step\')), \'problems\': problems})\n    return action\n\ndef terminal_action(obs, config, parent_action, plan):\n    """Canonical guard, pre-deviation abstention, observed recovery after deviation."""\n    step = int(_get(obs, \'step\', -1))\n    if not plan or not plan.get(\'accepted\') or (not START <= step <= FINAL):\n        return parent_action\n    if plan.get(\'abandoned\'):\n        return _recover_observed(obs, config, parent_action, plan) if plan.get(\'deviated\') else parent_action\n    index = step - START\n    n = 1 + len(physical_state(obs)[0][\'hands\'])\n    mismatch = physical_state(obs) != plan[\'expected_states\'][index] or _effective_action(parent_action, n) != _effective_action(plan[\'baseline\'][index], n)\n    if mismatch:\n        plan[\'abandoned\'] = True\n        plan[\'abandon_step\'] = step\n        plan[\'reason\'] = \'physical observation or effective baseline action diverged\'\n        plan[\'safety_failure\'] = True\n        return _recover_observed(obs, config, parent_action, plan) if plan.get(\'deviated\') else parent_action\n    result = deepcopy(plan[\'actions\'][index])\n    if step == FINAL:\n        farm, private = physical_state(obs)\n        result = shop_liquidation(farm, private, _get(obs, \'market\')[\'prices\'])\n    if _commands(result, n) != _commands(parent_action, n):\n        plan[\'deviated\'] = True\n    return result',_PLANNER_NS)
# EXP-154 integration by Ahmed Berat Ozer, derived from Dmitrii Gluzdov E182.
# The preserved v27 parent is simulated on a private shadow only at step 712.
_PRE_TERMINAL_AGENT=agent
del agent
_TERMINAL_PLANS={}
_TERMINAL_PREVIOUS={}
_UPGRADE_STATS={'planning_calls':0,'accepted':0,'changed_steps':0,'aborted':0,'shadow_declines':0,'errors':0,'max_planning_ms':0.0}

def _parent_liquidate(farm, private, prices):
    # Exactly v27's final projected DROP ordering, in the planner's private state.
    view=_View({'player':0,'farms':[farm],'private':private,'market':{'prices':prices}},0,_IMPL.chassis.cfg)
    commands=[['DROP'] if _shed_adjacent(pos,view.board) and view.inv(i) else ['PASS'] for i,pos in enumerate(view.positions)]
    action={'farmer':commands[0],'hands':commands[1:],'market':[]}
    stock=_IMPL.chassis._projected_shed(action,view)
    action['market']=[['SELL',item,stock.get(item,0)] for item in PRODUCTS if stock.get(item,0)>0]
    action['market'].sort(key=lambda o:-view.prices.get(o[1],0)*o[2])
    return action

_PLANNER_NS['shop_liquidation']=_parent_liquidate

def _shadow_terminal(obs,config):
    seat=int(obs['player']);chassis=_IMPL.chassis
    state=chassis.players.get(seat)
    if not state or state.get('last_step')!=711 or state.get('route')!=2:
        return None
    # No delayed weed/structure intervention may depend on an unmodeled future.
    if state.get('pending'):
        return None
    shadow=copy.copy(chassis);shadow.players=copy.deepcopy(chassis.players)
    shadow.diagnostics={k:0 for k in chassis.diagnostics}
    projected=copy.deepcopy(obs);baseline=[];states=[]
    for step in range(712,719):
        projected['step']=step;projected['day']=step//24;projected['hour']=step%24
        states.append(copy.deepcopy(shadow.players[seat]))
        action=shadow.act(projected,config)
        if step==718:
            action=_parent_liquidate(projected['farms'][seat],projected['private'],projected['market']['prices'])
        else:
            market=action.get('market',[])
            if len(market)!=9 or {o[1] for o in market}!=set(PRODUCTS) or any(o[0]!='SELL' or len(o)!=3 or type(o[2]) is not int or o[2]<100 for o in market):
                return None
        if any(shadow.diagnostics.values()):return None
        run=_PLANNER_NS['simulate'](projected,config,[action])
        if run['actions'][0]!=action:return None
        baseline.append(action)
        run['farm']['money']=projected['farms'][seat]['money']
        projected['farms'][seat]=run['farm'];projected['private']=run['private']
    return baseline,states

def agent(observation,configuration=None):
    try:
        step=int(observation['step']);seat=int(observation['player'])
    except Exception:
        return _PRE_TERMINAL_AGENT(observation,configuration)
    previous=_TERMINAL_PREVIOUS.get(seat)
    if step==0 or (previous is not None and step<=previous):_TERMINAL_PLANS.pop(seat,None)
    _TERMINAL_PREVIOUS[seat]=step
    plan=_TERMINAL_PLANS.get(seat)
    if plan and plan.get('accepted') and 712<=step<=718:
        if previous!=step-1:plan.update(abandoned=True,reason='nonconsecutive callback')
        try:
            result=_PLANNER_NS['terminal_action'](observation,configuration,plan['baseline'][step-712],plan)
            if plan.get('abandoned'):
                if not plan.get('abort_counted'):
                    plan['abort_counted']=True;_UPGRADE_STATS['aborted']+=1
                if not plan.get('deviated'):
                    _IMPL.chassis.players[seat]=copy.deepcopy(plan['parent_states_before'][step-712])
                    _TERMINAL_PLANS.pop(seat,None)
                    return _PRE_TERMINAL_AGENT(observation,configuration)
            _UPGRADE_STATS['changed_steps']+=int(result!=plan['baseline'][step-712])
            return result
        except Exception:
            _UPGRADE_STATS['errors']+=1
            if plan.get('deviated'):
                try:return _PLANNER_NS['_recover_observed'](observation,configuration,plan['baseline'][step-712],plan)
                except Exception:return _parent_liquidate(observation['farms'][seat],observation['private'],observation['market']['prices'])
    if step!=712:return _PRE_TERMINAL_AGENT(observation,configuration)
    _UPGRADE_STATS['planning_calls']+=1
    try:shadow=_shadow_terminal(observation,configuration)
    except (ValueError,KeyError,TypeError,IndexError):shadow=None
    if shadow is None:
        _UPGRADE_STATS['shadow_declines']+=1
        return _PRE_TERMINAL_AGENT(observation,configuration)
    baseline,states=shadow
    actual=_PRE_TERMINAL_AGENT(observation,configuration)
    if actual!=baseline[0]:
        _UPGRADE_STATS['shadow_declines']+=1;return actual
    try:
        plan=_PLANNER_NS['plan_terminal'](observation,configuration,baseline,max_simulations=64,passes=1,proposals_per_actor=4)
        _UPGRADE_STATS['max_planning_ms']=max(_UPGRADE_STATS['max_planning_ms'],plan.get('planning_ms',0.0))
        if not plan.get('accepted'):return actual
        plan['parent_states_before']=states;_TERMINAL_PLANS[seat]=plan
        _UPGRADE_STATS['accepted']+=1
        result=_PLANNER_NS['terminal_action'](observation,configuration,actual,plan)
        _UPGRADE_STATS['changed_steps']+=int(result!=actual)
        return result
    except Exception:
        _UPGRADE_STATS['errors']+=1;return actual

agent.telemetry=_UPGRADE_STATS

# EXP-154: aurax7 Reactive v2 day-end storage guard, adapted to our v27 view.
_PRE_ROOM_AGENT=agent
del agent
_ROOM_STATS={'changed_turns':0,'added_units':0,'errors':0}
def agent(observation,configuration=None):
    action=_PRE_ROOM_AGENT(observation,configuration)
    try:
        step=_step_of(observation)
        if step%24!=23:return action
        view=_View(observation,_int(_get(observation,'player',0)),_IMPL.chassis.cfg)
        carried=sum(max(0,int(n)) for inv in view.invs for n in inv.values())
        needed=sum(view.shed.values())+carried-99
        if needed<=0:return action
        planned={}
        for o in action.get('market',[]):
            if o and o[0]=='SELL' and len(o)>=3:planned[o[1]]=planned.get(o[1],0)+max(0,int(o[2]))
        result=copy.deepcopy(action);added=0
        for item in sorted(PRODUCTS,key=lambda it:-int(view.prices.get(it,0))):
            qty=min(needed,max(0,view.shed.get(item,0)-planned.get(item,0)))
            if qty<=0:continue
            if len(result['market'])>=10:break
            result['market'].append(['SELL',item,qty]);needed-=qty;added+=qty
            if needed<=0:break
        if added:_ROOM_STATS['changed_turns']+=1;_ROOM_STATS['added_units']+=added
        return result
    except Exception:
        _ROOM_STATS['errors']+=1;return action

agent.telemetry=_ROOM_STATS

# Incorporated upstream attribution and change notice:
# E182 Shop0909 + terminal physical closure (modified 2026-09-09)
# 
# The active public parent is Yusuke Hayashi's yhay81/shop-router-0909 v3.
# router_parent.py and actions.json are exact original bytes, not newly authored
# routes. The parent credits aurax7's Reactive Router for sale timing and shed
# projection; that attribution remains in router_parent.py. Original payload
# LICENSE.txt is preserved unchanged (Apache License 2.0 text); it contains no
# named copyright grantor and no separate NOTICE was supplied. No additional
# ownership, endorsement, or upstream replay-data rights claim is made.
# 
# Local changes: separate main.py/policy.py adapter; bounded start712 planner
# copied from frozen E180/S78 and modified for seven callbacks, exact Shop final
# liquidation, strict positive physical delivery/sale gain, and observation guards.
# unit_model.py is an unchanged frozen E180 copy of Kaggle's extracted semantics.
# The following original E180 notice is retained verbatim for attribution history.
# Its references to Thomas files describe E180, not files supplied in this Shop
# package: no Thomas tapes, trees or policy are included here.
# 
# ----- Original E180 notice -----
# Kaggriculture: Last-Mile Harvest Planner
# Attribution and change notice
# 
# Thomas Tschinkel is the author of the parent public state-router policy and its
# published decision trees and action-route data. Source: Kaggriculture: 93.8% Win
# Rate Public State Router, notebook version 3, scriptVersionId 347936183:
# https://www.kaggle.com/code/thomastschinkel/kaggriculture-93-8-win-rate-public-state-router?scriptVersionId=347936183
# The public notebook identifies its license as Apache License, Version 2.0.
# Original published main.py SHA-256:
# b87a27ed614a33329be85f1b662e51cf4078a019fee937afcebbbbf2f51f8522
# 
# Changes to that source for this distribution: compressed route/tree literals
# were decoded into readable tapes.json and trees.json; a read-only planned_action
# helper was added; descriptive headers and local data loading were adapted.
# The original parent feature extraction, tree traversal and agent behavior are
# retained. These public routes are not claimed as newly authored or trained by
# the notebook distributor.
# 
# unit_model.py contains deterministic unit-action and crop-decay definitions
# extracted from Kaggle's kaggle-environments 1.32.7 Kaggriculture engine, licensed
# under Apache License, Version 2.0. Credit: Kaggle and the kaggle-environments
# contributors. Project: https://github.com/Kaggle/kaggle-environments
# Source file: kaggle_environments/envs/kaggriculture/kaggriculture.py
# Source SHA-256:
# bc8a54879ef02c7ea64b8b333d6a976f0ea65c4949149d01f463f23bccee653e
# The extracted unit/decay definitions are not a newly authored game engine;
# market price dynamics and the full interpreter are not part of this module.
# 
# Additional work in this distribution: a bounded last-nine-action collection
# and delivery planner, observation guards and recovery, a settings-consuming
# factory and entry point, standalone examples, and deterministic packaging.
# The full Apache License, Version 2.0 is included as LICENSE.txt.
# No endorsement by Thomas Tschinkel or Kaggle is implied.
# 
# Data provenance limitation: Thomas's source refers to public replay data and
# an upstream provenance.json. That original episode-level manifest, replay IDs
# and individual replay-author identities were not supplied with the public
# notebook/output used here. No names or episode lineage have been invented.
# Notebook-level licensing does not independently establish the missing underlying
# replay-data rights chain. The package supplies usable readable routes, not a
# reproducible reconstruction of their original collection or training process.
# 
# Packaging note: source inputs described as byte-exact above are
# normalized to UTF-8/LF text with a final newline in this standalone
# notebook package. Route JSON values and parent policy behavior are unchanged.

# Final public-entry guard; measured separately and compared on captured observations.
_V28_CORE=agent
del agent
_IMPL.chassis.diagnostics['v28_entry_errors']=0
def agent(observation,configuration=None):
    try:
        return _V28_CORE(observation,configuration)
    except Exception:
        _IMPL.chassis.diagnostics['v28_entry_errors']+=1
        return {'farmer':['PASS'],'hands':[],'market':[]}
agent.telemetry=_ROOM_STATS

# EXP-155: prvsiyan V221B finite tomato investment, adapted by Ahmed Berat Ozer.
# Original public source is retained under research24/public; Apache-2.0.
MAX_ORDERS=10
class FarmView(_View):
    def __init__(self,obs):super().__init__(obs,int(obs['player']),_IMPL.chassis.cfg)
    def inventory(self,actor):return self.inv(actor)
def projected_shed(action,view):return _IMPL.chassis._projected_shed(action,view)

CROP_MIN_PRICE=70

# V219: a finite late tomato investment with dedicated, observed workers.
_V219_PARENT = agent
del agent
_V219_FERTILIZE = True  # Builder changes only this flag for the ablation.
_V219_STATES = {}
_V219_REPORT = {'commitments': 0, 'hire_requests': 0, 'confirmed_workers': 0,
                'hire_shortfalls': 0, 'plant_requests': 0, 'confirmed_plants': 0,
                'water_requests': 0, 'fertilize_requests': 0, 'harvest_requests': 0,
                'confirmed_harvest_units': 0, 'drop_requests': 0,
                'tomato_sale_requests': 0, 'budget_declines': 0, 'lost_plants': 0}


def _v219_fib(n):
    a, b = 1, 1
    for _ in range(n): a, b = b, a+b
    return a


def _v219_native_day(native, day):
    tape = _IMPL.chassis.routes[native['route']]
    return tape[day*24:min((day+1)*24,719)]


def _v219_qualifies(obs, native):
    farm=obs['farms'][obs['player']]
    if len(farm['tiles']) != 10 or set(farm['unlocked_quadrants']) != {'NW','NE','SW'}:
        return False
    if farm['money'] < 12000 or obs['market']['prices']['TOMATO'] < CROP_MIN_PRICE:
        return False
    if sum(s in ('PIZZA_SHOP','FARMERS_MARKET') for s in obs['town']['unlocked_shops']) < 3:
        return False
    if any(farm['tiles'][y][x] != 'LOCKED' for y in (5,6) for x in range(5,10)):
        return False
    if obs['private']['seeds'].get('TOMATO',0) or obs['private']['shed'].get('TOMATO',0):
        return False
    if any(isinstance(t,dict) and t.get('crop')=='TOMATO' for row in farm['tiles'] for t in row):
        return False
    # The investment uses spare land and new worker indices. Avoid taking over
    # any native tomato or land purchase obligation on the known own schedule.
    for tape in _IMPL.chassis.routes.values():
        for a in tape[432:719]:
            if any(o and o[0]=='BUY_LAND' for o in a.get('market',[])):return False
            if any(c==['PLANT','TOMATO'] for c in [a.get('farmer')]+a.get('hands',[])):return False
    return True


def _v219_walk(pos, target):
    x,y=pos;tx,ty=target
    if x != tx:return ['EAST' if x < tx else 'WEST']
    if y != ty:return ['SOUTH' if y < ty else 'NORTH']
    return None


def _v219_home(pos):
    return min(((4,4),(5,4),(4,5),(5,5)),key=lambda p:abs(pos[0]-p[0])+abs(pos[1]-p[1]))


def _v219_request(obs, action, state, native):
    step=int(obs['step']);day=step//24;offset=step%24
    farm=obs['farms'][obs['player']];private=obs['private']
    # If the planting-day transaction could not complete, abandon investment.
    # Later purchases would miss the finite day26..29 production window.
    if not state.get('committed') and day!=18:return action
    if state.get('requested_day')==day:return action
    planned=_v219_native_day(native,day)
    # EXP240: committed crops must wait for the native worker indices.
    # New schedules finish native hiring at hour4 or6. The existing two/three
    # crop-worker groups can still water/harvest their ten cells by midnight.
    # Initial investment stays within hour3; ordinary schedules are unchanged.
    latest_hire=max((i for i,a in enumerate(planned) if any(o and o[0]=='HIRE' for o in a.get('market',[]))),default=-1)
    deadline=6 if state.get('committed') and 3<latest_hire<=6 else 3
    if offset>deadline:return action
    remaining=planned[offset+1:]
    if any(o and o[0]=='HIRE' for a in remaining for o in a.get('market',[])):
        return action
    parent_hires=sum(bool(o) and o[0]=='HIRE' for o in action['market'])
    expected=max(len(a.get('hands',[])) for a in planned)
    if len(farm['hands'])+parent_hires != expected:return action
    fertilizer=bool(_V219_FERTILIZE and day in (24,27) and _r79_tomato_fertilizer_worthwhile(obs,action))
    # One watering tour: at most 2 entry moves + 9 between tiles + 10 waters.
    # A hire request by hour2 leaves at least21 callbacks after confirmation.
    crop_workers=1 if day in (19,20,21,22,23,25) and offset<=2 else (3 if 26<=day<=28 else 2)
    labor=_r53_labor_assignment(obs,action,fertilizer)
    if labor is not None:crop_workers=labor['workers']
    count=crop_workers+int(fertilizer and day==27 and labor is None)
    extra=[]
    if not state.get('committed'):
        extra += [['BUY_LAND'],['BUY_SEED','TOMATO',10]]
    fertilizer_quantity=_r70_parent_fert_qty(obs,action,planned,offset) if fertilizer else 0
    if fertilizer:extra.append(['BUY_PRODUCT','FERTILIZER',fertilizer_quantity])
    extra += [['HIRE'] for _ in range(count)]
    if len(action['market'])+len(extra)>MAX_ORDERS:return action
    # No assumed sale proceeds. Reserve 3,000 for parent obligations and price
    # movement; the qualification separately requires 12,000 initial liquidity.
    budget=sum(_v219_fib(n) for n in range(farm['hires_today'],farm['hires_today']+parent_hires+count))
    if not state.get('committed'):budget+=4500
    if fertilizer:budget+=fertilizer_quantity*(obs['market']['prices']['FERTILIZER']+5)
    for order in action['market']:
        if not order:continue
        if order[0]=='BUY_PRODUCT':budget+=int(order[2])*(int(obs['market']['prices'][order[1]])+10)
        elif order[0]=='BUY_ANIMAL':budget+=int(order[2])*{'COW':400,'SHEEP':500,'GOOSE':300}[order[1]]
        elif order[0]=='BUY_SEED':budget+=int(order[2])*{'WHEAT':10,'CARROT':20,'TOMATO':50,'STRAWBERRY':100,'MELON':80}[order[1]]
    if farm['money']<budget+3000:
        _V219_REPORT['budget_declines']+=1;return action
    state['pending']={'step':step,'first_actor':expected+1,'count':count,'crop_workers':crop_workers,'fertilizer':fertilizer,'labor':labor}
    if labor is not None:
        _R53_LABOR_REPORT['labor_requests']+=1;_R53_LABOR_REPORT['labor_hires_avoided']+=1;_R53_LABOR_REPORT['labor_day'+str(day)]+=1
    state['requested_day']=day
    _V219_REPORT['hire_requests']+=count
    if not state.get('committed'):
        state['committed']=True;_V219_REPORT['commitments']+=1
    changed=copy.deepcopy(action);changed['market']+=extra
    return changed


def _v219_worker(obs, state, actor, role):
    day=int(obs['step'])//24;step=int(obs['step']);view=FarmView(obs)
    pos=tuple(view.positions[actor]);inv=view.inventory(actor)
    targets=role['targets']
    # Actual cargo differences, observed on the next callback, verify harvests.
    previous=state['last_work'].get(actor)
    if previous and previous['step']==step-1 and previous['command']==['HARVEST']:
        _V219_REPORT['confirmed_harvest_units']+=max(0,int(inv.get('TOMATO',0))-previous['tomatoes'])
    if role.get('needs_fertilizer') and not role.get('loaded'):
        home=_v219_home(pos)
        walk=_v219_walk(pos,home)
        if walk:return walk
        desired=role.get('fertilizer_quantity',10 if role['kind']=='fertilizer' else 5)
        if inv.get('FERTILIZER',0)>=desired:role['loaded']=True
        elif role.get('pickup_requested'):
            # Never spend repeated turns waiting for stock that was not bought.
            role['loaded']=True;role['fertilizer_available']=int(inv.get('FERTILIZER',0))
        elif view.shed.get('FERTILIZER',0)>=desired:
            role['pickup_requested']=True;return ['PICKUP','FERTILIZER',desired]
        else:role['loaded']=True
    todo=[]
    for target in targets:
        x,y=target;tile=view.tiles[y][x]
        tomato=isinstance(tile,dict) and tile.get('crop')=='TOMATO'
        if tomato and target not in state['seen_plants']:
            state['seen_plants'].add(target);_V219_REPORT['confirmed_plants']+=1
        if target in state['seen_plants'] and not tomato and target not in state['lost']:
            state['lost'].add(target);_V219_REPORT['lost_plants']+=1
        command=None
        if role['kind']=='fertilizer':
            if tomato and tile.get('fertilized_until_day',-1)<day+2 and inv.get('FERTILIZER',0)>0:
                command=['FERTILIZE']
        elif day==18 and not tomato:
            if tile is None and obs['private']['seeds'].get('TOMATO',0)>0:command=['PLANT','TOMATO']
            elif isinstance(tile,dict) and tile.get('kind')=='WEED':command=['DIG']
        elif tomato:
            # No later production follows the final day, so watering then would
            # consume time needed to harvest and deliver the final cargo.
            if day<29 and not tile.get('watered_today'):command=['WATER']
            elif role.get('needs_fertilizer') and tile.get('fertilized_until_day',-1)<day+2 and inv.get('FERTILIZER',0)>0:
                command=['FERTILIZE']
            elif tile.get('yield_units',0)>0:command=['HARVEST']
        if command:todo.append((target,command))
    # Final return has priority once only the exact distance plus DROP remains.
    home=_v219_home(pos);distance=abs(pos[0]-home[0])+abs(pos[1]-home[1])
    if step>=718-distance and inv.get('TOMATO',0):
        return _v219_walk(pos,home) or ['PLACE','TOMATO',int(inv.get('TOMATO',0))]
    if todo:
        target,command=min(todo,key=lambda v:(abs(pos[0]-v[0][0])+abs(pos[1]-v[0][1]),targets.index(v[0])))
        return _v219_walk(pos,target) or command
    if inv.get('TOMATO',0):return _v219_walk(pos,home) or ['PLACE','TOMATO',int(inv['TOMATO'])]
    if any(inv.values()):return _v219_walk(pos,home) or ['DROP']
    return ['PASS']


def agent(observation, configuration=None):
    action=_V219_PARENT(observation,configuration)
    step=int(observation['step']);player=int(observation['player']);day=step//24
    state=_V219_STATES.get(player)
    if state is None or step<=state['last_step']:
        state={'last_step':step,'day':-1,'workers':{},'last_work':{},'seen_plants':set(),'lost':set(),
               'targets':[(x,y) for y in (5,6) for x in range(5,10)]}
        _V219_STATES[player]=state
    state['last_step']=step
    native=_IMPL.chassis.players[player]
    if step==432:state['eligible']=_v219_qualifies(observation,native)
    if not state.get('eligible') or day<18:return action
    if state['day']!=day:
        state['day']=day;state['workers']={};state['last_work']={}
    farm=observation['farms'][player]
    pending=state.pop('pending',None)
    if pending:
        if len(farm['hands'])+1 >= pending['first_actor']+pending['count'] and 'SE' in farm['unlocked_quadrants']:
            for index in range(pending['count']):
                fertilizer_worker=index==pending['crop_workers']
                if fertilizer_worker:targets=state['targets']
                elif pending['crop_workers']==1:targets=state['targets']
                elif pending['crop_workers']==2:targets=state['targets'][index*5:index*5+5]
                else:targets=[[(5,5),(6,5),(7,5)],[(8,5),(9,5),(9,6),(8,6)],[(5,6),(6,6),(7,6)]][index]
                state['workers'][pending['first_actor']+index]={'kind':'fertilizer' if fertilizer_worker else 'crop','targets':targets,
                    'needs_fertilizer':pending['fertilizer'] and (day==24 or fertilizer_worker)}
                if pending.get('labor') is not None:
                    role=state['workers'][pending['first_actor']+index]
                    role['targets']=[tuple(p) for p in pending['labor']['paths'][index]]
                    role['needs_fertilizer']=pending['labor']['fertilizer'];role['fertilizer_quantity']=len(role['targets'])
                    if tuple(farm['hands'][pending['first_actor']+index-1])!=tuple(pending['labor']['spawns'][index]):_R53_LABOR_REPORT['labor_spawn_errors']+=1
                    if index==0:_R53_LABOR_REPORT['labor_confirmed']+=1
            _V219_REPORT['confirmed_workers']+=pending['count']
        else:_V219_REPORT['hire_shortfalls']+=pending['count']
    action=_v219_request(observation,action,state,native)
    if state['workers']:
        commands=[action.get('farmer') or ['PASS']]+list(action.get('hands') or [])
        commands += [['PASS'] for _ in range(len(farm['hands'])+1-len(commands))]
        for actor,role in state['workers'].items():
            if actor>=len(commands):continue
            command=_v219_worker(observation,state,actor,role)
            commands[actor]=command
            name={'PLANT':'plant_requests','WATER':'water_requests','FERTILIZE':'fertilize_requests',
                  'HARVEST':'harvest_requests','DROP':'drop_requests'}.get(command[0])
            if name:_V219_REPORT[name]+=1
            state['last_work'][actor]={'step':step,'command':command,'tomatoes':observation['private']['inventories'][actor].get('TOMATO',0)}
        action=copy.deepcopy(action);action['farmer'],action['hands']=commands[0],commands[1:]
    if state.get('committed') and len(action['market'])<MAX_ORDERS and not any(o[:2]==['SELL','TOMATO'] for o in action['market']):
        quantity=projected_shed(action,FarmView(observation)).get('TOMATO',0)
        if quantity>0:
            action=copy.deepcopy(action);action['market'].append(['SELL','TOMATO',quantity])
            _V219_REPORT['tomato_sale_requests']+=quantity
    return action


agent.telemetry=_V219_REPORT

# V221B: labor-only ablation of frozen V219G; not yet publicly scored.


# Crop workers own their final routes after commitment. A private parent shadow
# does not contain these obligations, so terminal rescue must abstain there.
_ORIGINAL_SHADOW_TERMINAL=_shadow_terminal
def _shadow_terminal(obs,config):
    if _V219_STATES.get(int(obs['player']),{}).get('committed'):return None
    return _ORIGINAL_SHADOW_TERMINAL(obs,config)

APPLY_TIMING=False

_EXPERIMENT_PARENT=agent
del agent
_V219_REPORT['extra_fertilizer_days']=0
_V219_REPORT['reordered_market_turns']=0
_V219_REPORT['errors']=0
def agent(observation,configuration=None):
    try:
        action=_EXPERIMENT_PARENT(observation,configuration)
        if APPLY_TIMING and int(observation['step'])>=144:action=_v224_sales_first(action)
        return action
    except Exception:
        _V219_REPORT['errors']+=1
        return {'farmer':['PASS'],'hands':[],'market':[]}
agent.telemetry=_V219_REPORT

def _v224_sales_first(action):
    original=action.get('market',[])[:MAX_ORDERS]
    orders=[list(o) for o in original if o and (o[0] in ('HIRE','BUY_LAND') or (len(o)>=3 and int(o[2])>0))]
    for index in range(len(orders)):
        order=orders[index]
        if order[0]!='SELL':continue
        cursor=index
        while cursor>0:
            previous=orders[cursor-1]
            if previous[0]=='SELL':break
            if previous[0] in ('BUY_PRODUCT','BUY_ANIMAL') and previous[1]==order[1]:break
            orders[cursor-1],orders[cursor]=orders[cursor],orders[cursor-1]
            cursor-=1
    if orders==original:return action
    _V219_REPORT['reordered_market_turns']+=1
    changed=copy.deepcopy(action);changed['market']=orders
    return changed
_ORDER_PARENT=agent
del agent

def agent(observation,configuration=None):
    try:
        action=_ORDER_PARENT(observation,configuration)
        if int(observation["step"])>=144:action=_v224_sales_first(action)
        return action
    except Exception:
        _V219_REPORT["errors"]+=1
        return {"farmer":["PASS"],"hands":[],"market":[]}
agent.telemetry=_V219_REPORT

_V31_CORE=agent
del agent
_IMPL.chassis.diagnostics['production_errors']=0
_IMPL.chassis.diagnostics['v31_entry_errors']=0
def agent(observation,configuration=None):
    before=_V219_REPORT['errors']
    try:
        action=_V31_CORE(observation,configuration)
        _IMPL.chassis.diagnostics['production_errors']+=_V219_REPORT['errors']-before
        return action
    except Exception:
        _IMPL.chassis.diagnostics['v31_entry_errors']+=1
        return {'farmer':['PASS'],'hands':[],'market':[]}
agent.telemetry=_V219_REPORT

# Apache-2.0; later cattle transfer from prvsiyan, Moon (2026-09-10).
# Bounded livestock substitution; confirm owned animals before redirecting workers.
_V231_PARENT=agent
_V231_CAP=4
_V231_STATES={}
_V231_REPORT={}

def _v231_new_state():
    return {'last':-1,'confirmed':0,'reserved':0,'pending_buy':None,
            'carrying':{},'pending_places':[],'sites':{},'milk_credit':0,
            'requested':0,'failed_purchase_units':0,'picked':0,'placed':0,
            'failed_placements':0,'extra_milk_harvested':0,'extra_milk_sale_requests':0}

def _v231_controller(obs,action,state,cap):
    step=int(obs['step']);seat=int(obs['player']);farm=obs['farms'][seat]
    private=obs['private'];shed=private['shed'];inventories=private['inventories']
    positions=[farm['farmer'],*farm['hands']]
    pending=state['pending_buy']
    if pending is not None:
        gained=max(0,int(shed.get('COW',0))-pending['before'])
        confirmed=min(pending['quantity'],gained)
        state['confirmed']+=confirmed;state['reserved']+=confirmed
        state['failed_purchase_units']+=pending['quantity']-confirmed
        state['pending_buy']=None
    for pending in state['pending_places']:
        x,y=pending['site'];tile=farm['tiles'][y][x]
        if (isinstance(tile,dict) and tile.get('animal')=='COW'
                and tile.get('placed_day')==pending['day']):
            state['sites'][(x,y)]=pending['day'];state['placed']+=1
            actor=pending['actor'];state['carrying'][actor]=max(0,state['carrying'].get(actor,0)-1)
        else:state['failed_placements']+=1
    state['pending_places']=[]
    state['last']=step
    result=copy.deepcopy(action)
    workers=[result.get('farmer') or ['PASS'],*(result.get('hands') or [])]
    seen_harvest=set();cow_available=int(shed.get('COW',0));occupied=set()
    for actor,work in enumerate(workers[:len(positions)]):
        inventory=inventories[actor] if actor<len(inventories) else {}
        x,y=positions[actor];tile=farm['tiles'][y][x];site=(x,y)
        if (work==['HARVEST'] and site in state['sites'] and site not in seen_harvest
                and isinstance(tile,dict) and tile.get('animal')=='COW'
                and tile.get('placed_day')==state['sites'][site]):
            units=max(0,int(tile.get('yield_units',0)))
            state['milk_credit']+=units;state['extra_milk_harvested']+=units
            seen_harvest.add(site)
        if len(work)>=2 and work[:2]==['PICKUP','SHEEP']:
            quantity=max(0,int(work[2]) if len(work)>2 else 1)
            center=len(farm['tiles'])//2
            if (quantity and state['reserved']>=quantity and cow_available>=quantity
                    and x in (center-1,center) and y in (center-1,center)
                    and not any(inventory.get(a,0) for a in ('COW','SHEEP','GOOSE'))):
                work[1]='COW';state['reserved']-=quantity;cow_available-=quantity
                state['carrying'][actor]=state['carrying'].get(actor,0)+quantity
                state['picked']+=quantity
        if (len(work)>=2 and work[:2]==['PLACE','SHEEP']
                and state['carrying'].get(actor,0)>0 and inventory.get('COW',0)>0
                and isinstance(tile,dict) and tile.get('kind')=='PASTURE'
                and 'animal' not in tile and site not in occupied):
            work[1]='COW'
            state['pending_places'].append({'actor':actor,'site':site,'day':step//24})
        if (len(work)>=2 and work[0]=='PLACE' and work[1] in ('COW','SHEEP','GOOSE')
                and inventory.get(work[1],0)>0):occupied.add(site)
    result['farmer'],result['hands']=workers[0],workers[1:]
    market=result.get('market',[])
    animal_orders=[o for o in market if len(o)>=3 and o[0]=='BUY_ANIMAL']
    shops=obs['town']['unlocked_shops'];prices=obs['market']['prices']
    counts={'COW':0,'SHEEP':0}
    for line in farm['tiles']:
        for tile in line:
            if isinstance(tile,dict) and tile.get('animal') in counts:counts[tile['animal']]+=1
    cargo=sum(int(inv.get(a,0)) for inv in inventories for a in ('COW','SHEEP','GOOSE'))
    stock_animals=sum(int(shed.get(a,0)) for a in ('COW','SHEEP','GOOSE'))
    milk_shops=sum(shop in ('PIZZA_SHOP','ICE_CREAM_SHOP','SMOOTHIE_SHOP') for shop in shops)
    if (216<=step<=227 and len(shops)>=3 and state['confirmed']<cap and not state['reserved']
            and not any(state['carrying'].values()) and not state['pending_places']
            and not cargo and not stock_animals and len(animal_orders)==1
            and animal_orders[0][1]=='SHEEP' and milk_shops>=2 and 'YARN_STORE' not in shops
            and int(prices.get('MILK',0))>=int(prices.get('WOOL',0))
            and counts['COW']>=4 and counts['SHEEP']>=2):
        order=animal_orders[0];quantity=int(order[2])
        if 1<=quantity<=2 and quantity<=cap-state['confirmed']:
            order[1]='COW';state['requested']+=quantity
            state['pending_buy']={'before':int(shed.get('COW',0)),'quantity':quantity}
    # Sell only additional physically harvested production at an existing sale slot.
    if state['milk_credit']>0:
        stock=projected_shed(result,FarmView(obs))
        total_planned=sum(max(0,int(o[2])) for o in market if len(o)>=3 and o[:2]==['SELL','MILK'])
        extra=min(state['milk_credit'],max(0,int(stock.get('MILK',0))-total_planned))
        if extra:
            for order in market:
                if len(order)>=3 and order[:2]==['SELL','MILK'] and int(order[2])>0:
                    order[2]=int(order[2])+extra
                    state['milk_credit']-=extra;state['extra_milk_sale_requests']+=extra
                    break
    result['market']=market
    return result

def agent(observation,configuration=None):
    step=int(observation['step']);seat=int(observation['player'])
    state=_V231_STATES.get(seat)
    if state is None or step<=state['last']:
        state=_V231_STATES[seat]=_v231_new_state()
    action=_V231_PARENT(observation,configuration)
    action=_v231_controller(observation,action,state,_V231_CAP)
    _V231_REPORT.clear();_V231_REPORT.update(_V231_PARENT.telemetry)
    for name in ('confirmed','reserved','requested','failed_purchase_units','picked','placed',
                 'failed_placements','extra_milk_harvested','extra_milk_sale_requests','milk_credit'):
        _V231_REPORT['cattle_'+name]=state[name]
    _V231_REPORT['cattle_carried_pending']=sum(state['carrying'].values())
    return action

agent.telemetry=_V231_REPORT


# EXP-167, adapted from Dmitrii Gluzdov's Two Coins, One Sheep (Apache-2.0).
# Reserve only physically available stock after the final parent worker actions.
_R36_SALE_PARENT=agent
_R36_NATIVE_LEAD=Chassis._sell_lead
_R36_NATIVE_SUPPRESS=Chassis._apply_suppression
_R36_SALE_REPORT={}

def _r36_native_lead(self,action,view,projected,route,step,next_sup):
    if step<288 or step>=696:
        return _R36_NATIVE_LEAD(self,action,view,projected,route,step,next_sup)

def _r36_suppress(action,state,step):
    _R36_NATIVE_SUPPRESS(action,state,step)
    due=state.get('r36_debts',{}).pop(step,{})
    for order in action.get('market',[]):
        if len(order)>=3 and order[0]=='SELL':
            removed=min(max(0,int(order[2])),due.get(order[1],0))
            order[2]-=removed
            due[order[1]]=due.get(order[1],0)-removed

Chassis._sell_lead=_r36_native_lead
Chassis._apply_suppression=staticmethod(_r36_suppress)

def _r36_reserve(obs,action):
    step=int(obs['step'])
    # The final planner forecasts its own parent, so keep its full window native.
    if not 192<=step<696:return action
    native=_IMPL.chassis.players[int(obs['player'])]
    tape=_IMPL.chassis.routes[native['route']]
    _v9_hz=_V9_ITEM_HZ.get(int(obs['player']))
    end=min(695,step+(max(_v9_hz.values()) if _v9_hz else _R37_HORIZONS.get(int(obs['player']),2)))
    if end<=step:return action
    commands=[action.get('farmer') or ['PASS'],*(action.get('hands') or [])]
    view=FarmView(obs)
    # This projection intentionally abstains on ambiguous animal depot returns.
    if any(len(c)>1 and c[0]=='PLACE' and c[1] in ANIMAL_STRUCTURE
           and view.inv(i).get(c[1],0)>0 for i,c in enumerate(commands[:len(view.positions)])):
        return action
    stock=projected_shed(action,view)
    market=action.get('market',[])
    blocked={o[1] for o in market if len(o)>1 and o[0] in ('SELL','BUY_PRODUCT')}
    blocked.update(c[1] for c in commands if len(c)>1 and c[0]=='PICKUP')
    blocked.update(c[1] for queue in native['pending'].values() for pos,c in queue
                   if len(c)>1 and c[0]=='PICKUP')
    debts=native['sell_state'].setdefault('r36_debts',{})
    for item in PRODUCTS:
        if item in blocked or view.prices.get(item,0)<2:continue
        available=max(0,int(stock.get(item,0)))
        if not available or len(market)>=10:continue
        reservations=[]
        item_end=min(end,step+_v9_hz[item]) if _v9_hz and item in _v9_hz else end
        for due_step in range(step+1,item_end+1):
            future=tape[due_step]
            work=[future.get('farmer') or ['PASS'],*(future.get('hands') or [])]
            if any(len(c)>1 and c[:2]==['PICKUP',item] for c in work):break
            if any(len(o)>1 and o[:2]==['BUY_PRODUCT',item] for o in future.get('market',[])):break
            planned=sum(max(0,int(o[2])) for o in future.get('market',[]) if len(o)>=3 and o[:2]==['SELL',item])
            amount=min(available,max(0,planned-debts.get(due_step,{}).get(item,0)))
            if amount:
                reservations.append((due_step,amount));available-=amount
            if not available:break
        qty=sum(q for _,q in reservations)
        if qty:
            market.append(['SELL',item,qty])
            for due,q in reservations:
                debt=debts.setdefault(due,{})
                debt[item]=debt.get(item,0)+q
            _R36_SALE_REPORT['sale_reserved_units']+=qty
            _R36_SALE_REPORT['sale_reservations']+=1
    return action

def agent(observation,configuration=None):
    if int(observation.get('step',0))==0:
        _R36_SALE_REPORT.update(sale_reserved_units=0,sale_reservations=0,sale_errors=0)
    action=_R36_SALE_PARENT(observation,configuration)
    try:
        if configuration is None or all(configuration.get(k,v)==v for k,v in
            [('boardSize',10),('turnsPerDay',24),('shedCapacity',100),('maxMarketOrdersPerTurn',10)]):
            action=_r36_reserve(observation,action)
            if int(observation['step'])>=288:action=_v224_sales_first(action)
    except Exception:
        _R36_SALE_REPORT['sale_errors']=_R36_SALE_REPORT.get('sale_errors',0)+1
    _R36_SALE_REPORT.update(_R36_SALE_PARENT.telemetry)
    return action

agent.telemetry=_R36_SALE_REPORT

# Ensure the Kaggle-selected final callable is the exported policy.
agent = globals().pop("agent")


# Public capability transfer: lucifer19; Flexon is the same Two Coins asset set.
# Apache-2.0; exact functions from Kaggle kaggle-environments 1.32.7.
# https://github.com/Kaggle/kaggle-environments/tree/master/kaggle_environments/envs/kaggriculture
import math
_R37_MARKET_PARAMS = {'WHEAT': {'base': 25, 'I0': 10000, 'T': 400, 'below_func': 'sqrt', 'below_target': 0.8, 'above_func': 'log', 'above_target': 0.2}, 'CARROT': {'base': 35, 'I0': 10000, 'T': 450, 'below_func': 'hinge', 'below_target': 1.0, 'above_func': 'sqrt', 'above_target': 0.7}, 'TOMATO': {'base': 60, 'I0': 10000, 'T': 200, 'below_func': 'hinge', 'below_target': 0.4, 'above_func': 'sqrt', 'above_target': 0.6}, 'STRAWBERRY': {'base': 120, 'I0': 10000, 'T': 100, 'below_func': 'sqrt', 'below_target': 0.7, 'above_func': 'linear', 'above_target': 1.6}, 'MELON': {'base': 250, 'I0': 10000, 'T': 300, 'below_func': 'log', 'below_target': 0.2, 'above_func': 'sq', 'above_target': 3.6}, 'EGG': {'base': 50, 'I0': 10000, 'T': 332, 'below_func': 'hinge', 'below_target': 0.4, 'above_func': 'log', 'above_target': 0.2}, 'MILK': {'base': 160, 'I0': 10000, 'T': 122, 'below_func': 'sqrt', 'below_target': 0.6, 'above_func': 'linear', 'above_target': 1.6}, 'WOOL': {'base': 200, 'I0': 10000, 'T': 105, 'below_func': 'log', 'below_target': 0.2, 'above_func': 'sq', 'above_target': 3.2}, 'FERTILIZER': {'base': 100, 'I0': 10000, 'T': 200, 'below_func': 'linear', 'below_target': 0.4, 'above_func': 'linear', 'above_target': 0.4}}
_R37_PRICE_FLOOR = 1
_R37_HINGE_GAIN = 8.0
def _r37_shape(func, x, T=None):
    x = max(0.0, x)
    if func == "linear": return x
    if func == "sq":     return x * x
    if func == "sqrt":   return math.sqrt(x)
    if func == "log":    return math.log(1.0 + x)
    if func == "log10":  return math.log10(1.0 + x)
    if func == "hinge":
        # Degenerates to linear if T is missing or non-positive.
        if not T or T <= 0:
            return x
        u = x / T
        return u + _R37_HINGE_GAIN * max(0.0, u - 1.0) ** 2
    return x

def _r37_market_price(item, inventory, params=None):
    """Floor at _R37_PRICE_FLOOR."""
    p = (params or _R37_MARKET_PARAMS)[item]
    base = p["base"]
    I0 = p["I0"]
    T = p["T"]
    if inventory < I0:
        f = p["below_func"]
        amp = p["below_target"] * base / _r37_shape(f, T, T)
        price = base + amp * _r37_shape(f, I0 - inventory, T)
    else:
        f = p["above_func"]
        amp = p["above_target"] * base / _r37_shape(f, T, T)
        price = base - amp * _r37_shape(f, inventory - I0, T)
    return max(_R37_PRICE_FLOOR, int(round(price)))

def _r37_similarity(observation):
    """Empty tiles cannot make two unrelated production layouts look alike."""
    farms = observation['farms']
    own, rival = farms[observation['player']], farms[1-observation['player']]
    if own['unlocked_quadrants'] != rival['unlocked_quadrants']:
        return 0.0
    matches = total = 0
    for a, b in zip([t for row in own['tiles'] for t in row],
                    [t for row in rival['tiles'] for t in row]):
        sa = (a.get('crop'), a.get('animal')) if isinstance(a, dict) else (None, None)
        sb = (b.get('crop'), b.get('animal')) if isinstance(b, dict) else (None, None)
        if sa != (None, None) or sb != (None, None):
            total += 1
            matches += sa == sb
    return matches / total if total >= 8 else 0.0


def _r37_quote_priority(observation, order, stock):
    """Revenue exposed to a small rival batch, not nominal headline revenue."""
    item = order[1]
    quantity = min(max(0, int(order[2])), stock.get(item, 0))
    if not quantity or item not in _R37_MARKET_PARAMS:
        return 0.0
    inventory = observation['market']['inventory'][item]
    params = {k: dict(v) for k, v in _R37_MARKET_PARAMS.items()}
    for k, patch in observation['market'].get('params', {}).items():
        if k in params:
            params[k].update(patch)
    rival = observation['farms'][1-observation['player']]
    crop_item = item if item in ('WHEAT','CARROT','TOMATO','STRAWBERRY','MELON') else None
    animal = {'EGG':'GOOSE','MILK':'COW','WOOL':'SHEEP'}.get(item)
    standing = sum(max(0, int(t.get('yield_units', 0))) for row in rival['tiles'] for t in row
                   if isinstance(t, dict) and
                   ((crop_item is not None and t.get('crop') == crop_item) or
                    (animal is not None and t.get('animal') == animal)))
    # Public fields do not reveal the rival shed. Eight units are a scenario,
    # not a recovered hidden quantity; visible ripe yield increases the stress.
    batch = min(24, max(8, standing))
    now = sum(_r37_market_price(item, inventory+j, params) for j in range(quantity))
    later = sum(_r37_market_price(item, inventory+batch+j, params) for j in range(quantity))
    return now-later


def _r37_reorder_sales(observation, action):
    """Keep quantities and purchase barriers; rank distinct contiguous sales."""
    stock = projected_shed(action, FarmView(observation))
    orders = [list(o) for o in action['market']]
    start = 0
    while start < len(orders):
        if orders[start][0] != 'SELL':
            start += 1
            continue
        end = start
        while end < len(orders) and orders[end][0] == 'SELL':
            end += 1
        block = orders[start:end]
        if len({o[1] for o in block}) == len(block):
            orders[start:end] = sorted(block, key=lambda o: _r37_quote_priority(observation, o, stock), reverse=True)
        start = end
    if orders != action['market']:
        _R37_STATS['quote_reordered_turns'] += 1
        action = dict(action, market=orders)
    return action



# EXP175: bounded public cash-response probe inspired by leoprovorov,
# Two Coins Mirror Counter v1 (Apache-2.0). No hidden rival inventory.
_R44_PROBES={}
_R44_REPORT=dict(probe_matches=0,probe_four_turn_calls=0,probe_errors=0)

def _r44_before(obs):
    player=int(obs['player']);step=int(obs['step'])
    st=_R44_PROBES.get(player)
    if st is None or step<=st['step']:
        st=_R44_PROBES[player]={'step':-1,'money':None,'probe':0,'matched':False}
    if step==0:_R44_REPORT.update(probe_matches=0,probe_four_turn_calls=0,probe_errors=0)
    money=tuple(float(obs['farms'][i]['money']) for i in (player,1-player))
    if st['money'] is not None and st['probe']>=100 and _r37_similarity(obs)>=.90:
        own=money[0]-st['money'][0];rival=money[1]-st['money'][1]
        if own>0 and rival>0 and abs(own-rival)<=max(5.0,.05*st['probe']):
            if not st['matched']:_R44_REPORT['probe_matches']+=1
            st['matched']=True
    st.update(step=step,money=money,probe=0)
    return st

def _r44_after(obs,action,st):
    step=int(obs['step']);player=int(obs['player'])
    if not 336<=step<648 or st['matched']:return
    # Positive all-sale probes avoid mistaking equal spending for preemption.
    if not action['market'] or any(o and o[0]!='SELL' for o in action['market']):return
    debts=_IMPL.chassis.players[player]['sell_state'].get('r36_debts',{})
    own=debts.get(step+3,{})
    if own:st['probe']=sum(max(0,int(n))*int(obs['market']['prices'].get(item,0)) for item,n in own.items())

_R37_ADAPTIVE = True
_R37_QUOTE = True
# EXP-168: adapted from lucifer19 / Harvest Nocturne, Apache-2.0.
# All rivalry features use public occupied tiles; no private rival inventory.
_R37_PARENT = agent
_R37_PLAYERS = {}
_R37_HORIZONS = {}
_V9_ITEM_HZ = {}
_R37_REPORT = {}
_R37_STATS = dict(quote_reordered_turns=0, three_turn_calls=0, nocturne_errors=0)
del agent

def agent(observation, configuration=None):
    player, step = int(observation['player']), int(observation['step'])
    state = _R37_PLAYERS.get(player)
    if state is None or step <= state['step']:
        state = _R37_PLAYERS[player] = {'step': -1, 'streak': 0}
    if step == 0:
        _R37_STATS.update(quote_reordered_turns=0, three_turn_calls=0, nocturne_errors=0)
    state['step'] = step
    _R37_HORIZONS[player] = 2
    probe_state=_r44_before(observation)
    try:
        if _R37_ADAPTIVE and step < 648:
            state['streak'] = state['streak'] + 1 if _r37_similarity(observation) >= .90 else 0
            if 336 <= step < 648 and state['streak'] >= 6:
                _R37_HORIZONS[player] = 3
                _R37_STATS['three_turn_calls'] += 1
    except Exception:
        _R37_STATS['nocturne_errors'] += 1
    if _R37_HORIZONS[player]==3 and probe_state['matched']:
        _R37_HORIZONS[player]=4
        _R44_REPORT['probe_four_turn_calls']+=1
    # EXP179: four-turn reservation; retain stock, debt and purchase barriers.
    if 288 <= step < 696:_R37_HORIZONS[player] = 4
    action = _R37_PARENT(observation, configuration)
    _r44_after(observation,action,probe_state)
    if _R37_QUOTE and step >= 288:
        try:
            action = _r37_reorder_sales(observation, action)
        except Exception:
            _R37_STATS['nocturne_errors'] += 1
    _R37_REPORT.update(getattr(_R37_PARENT, 'telemetry', {}))
    _R37_REPORT.update(_R37_STATS)
    _R37_REPORT.update(_R44_REPORT)
    return action

agent.telemetry = _R37_REPORT

# Export guard: normal decisions stay identical to the frozen screened policy.
_RELEASE_PARENT=agent
_RELEASE_REPORT={}
_RELEASE_ERRORS=0
del agent

def agent(observation,configuration=None):
    global _RELEASE_ERRORS
    try:
        result=_RELEASE_PARENT(observation,configuration)
    except Exception:
        _RELEASE_ERRORS+=1
        count=0
        try:
            count=min(64,len(observation['farms'][int(observation['player'])]['hands']))
        except Exception:
            pass
        result={'farmer':['PASS'],'hands':[['PASS'] for _ in range(count)],'market':[]}
    _RELEASE_REPORT.update(getattr(_RELEASE_PARENT,'telemetry',{}))
    _RELEASE_REPORT['release_errors']=_RELEASE_ERRORS
    return result

agent.telemetry=_RELEASE_REPORT
agent=globals().pop('agent')

# Adapted from prvsiyan / The Soil Remembers Rain, Apache-2.0.
# V233: bounded, financed six-sheep SE discovery investment.
_V233_PARENT=agent
del agent
_V233_STATES={}
_V233_REPORT=dict(sheep_commit_requests=0,sheep_committed=0,sheep_hire_requests=0,
    sheep_workers_confirmed=0,sheep_hire_shortfalls=0,sheep_budget_declines=0,
    sheep_capacity_declines=0,sheep_purchase_shortfalls=0,sheep_feed_buy_requests=0,
    sheep_wool_harvested=0,sheep_fert_collected=0,sheep_extra_wool_sales=0,
    sheep_extra_fert_sales=0,sheep_rescue_feed_requests=0)

def _v233_eligible(obs,native):
    farm=obs['farms'][obs['player']];prices=obs['market']['prices']
    if len(farm['tiles'])!=10 or set(farm['unlocked_quadrants'])!={'NW','NE','SW'}:return False
    if obs['town']['unlocked_shops'].count('YARN_STORE')<2 or prices['WOOL']<220 or prices['WHEAT']>45:return False
    if any(farm['tiles'][y][x]!='LOCKED' for y in (5,6) for x in range(5,8)):return False
    if obs['private']['shed'].get('SHEEP',0) or any(i.get('SHEEP',0) for i in obs['private']['inventories']):return False
    for day in range(12,30):
        for a in _v219_native_day(native,day):
            if any(o and (o[0]=='BUY_LAND' or o[:2]==['BUY_ANIMAL','SHEEP']) for o in a.get('market',[])):return False
            if any(c and c[0] in ('PICKUP','PLACE') and len(c)>1 and c[1]=='SHEEP' for c in [a.get('farmer')]+a.get('hands',[])):return False
    return True

def _v233_request(obs,action,state,native):
    step=int(obs['step']);day=step//24;hour=step%24
    # EXP242: preserve native indices while servicing already committed sheep.
    if state.get('requested_day')==day:return action
    committed=state.get('committed')
    if not committed and (hour>(3 if day==11 else 1) or day not in (11,12) or not _v233_eligible(obs,native)):return action
    planned=_v219_native_day(native,day)
    deadline=2 if committed else (3 if day==11 else 1)
    if committed:
        last_native_hire=max((h for h,a in enumerate(planned) if any(o and o[0]=='HIRE' for o in a.get('market',[]))),default=0)
        if 2<last_native_hire<=6:deadline=6
    if hour>deadline:return action
    if any(o and o[0]=='HIRE' for a in planned[hour+1:] for o in a.get('market',[])):return action
    farm=obs['farms'][obs['player']];market=action.get('market',[])
    parent_hires=sum(bool(o) and o[0]=='HIRE' for o in market)
    expected=max(len(a.get('hands',[])) for a in planned)
    if len(farm['hands'])+parent_hires!=expected:return action
    initial=not state.get('committed')
    extra=([['BUY_LAND'],['BUY_ANIMAL','SHEEP',6]] if initial else [])+[['BUY_PRODUCT','WHEAT',6],['HIRE'],['HIRE']]
    if len(market)+len(extra)>MAX_ORDERS:return action
    stock=projected_shed(action,FarmView(obs))
    incoming=6+6*initial
    budget=7000*initial+6*(int(obs['market']['prices']['WHEAT'])+10)
    budget+=sum(_v219_fib(n) for n in range(farm['hires_today'],farm['hires_today']+parent_hires+2))
    for o in market:
        if not o:continue
        if o[0]=='BUY_LAND':return action
        if o[0]=='BUY_PRODUCT':
            incoming+=int(o[2]);budget+=int(o[2])*(int(obs['market']['prices'][o[1]])+10)
        elif o[0]=='BUY_ANIMAL':
            incoming+=int(o[2]);budget+=int(o[2])*{'SHEEP':500,'COW':400,'GOOSE':300}[o[1]]
        elif o[0]=='BUY_SEED':budget+=int(o[2])*{'WHEAT':10,'CARROT':20,'TOMATO':50,'STRAWBERRY':100,'MELON':80}[o[1]]
    if sum(stock.values())+incoming>100:
        _V233_REPORT['sheep_capacity_declines']+=1;return action
    if farm['money']<budget+(3000 if initial else 1000):
        _V233_REPORT['sheep_budget_declines']+=1;return action
    state['requested_day']=day
    state['pending']={'first':expected+1,'initial':initial}
    _V233_REPORT['sheep_hire_requests']+=2;_V233_REPORT['sheep_feed_buy_requests']+=6
    if initial:_V233_REPORT['sheep_commit_requests']+=1
    result=copy.deepcopy(action);result['market']=market+extra
    return result

def _v233_worker(obs,actor,targets):
    farm=obs['farms'][obs['player']];private=obs['private'];step=int(obs['step'])
    pos=tuple(farm['hands'][actor-1]);inv=private['inventories'][actor]
    access=((4,4),(5,4),(4,5),(5,5))
    home=min(access,key=lambda p:(abs(pos[0]-p[0])+abs(pos[1]-p[1]),p))
    distance=abs(pos[0]-home[0])+abs(pos[1]-home[1])
    cargo=[item for item in ('WOOL','FERTILIZER') if inv.get(item,0)]
    if cargo and step%24 >= (22 if step//24==29 else 23)-distance:
        return _v219_walk(pos,home) or ['PLACE',cargo[0],inv[cargo[0]]]
    missing=sum(not(isinstance(farm['tiles'][y][x],dict) and farm['tiles'][y][x].get('animal')=='SHEEP') for x,y in targets)
    if missing and not inv.get('SHEEP',0) and private['shed'].get('SHEEP',0):
        return _v219_walk(pos,home) or ['PICKUP','SHEEP',min(missing,private['shed']['SHEEP'])]
    hungry=sum(not(isinstance(farm['tiles'][y][x],dict) and farm['tiles'][y][x].get('fed_today')) for x,y in targets)
    if hungry and not inv.get('WHEAT',0) and private['shed'].get('WHEAT',0):
        return _v219_walk(pos,home) or ['PICKUP','WHEAT',min(hungry,private['shed']['WHEAT'])]
    tasks=[]
    for target in targets:
        x,y=target;tile=farm['tiles'][y][x];command=None
        if tile is None:command=['BUILD_PASTURE']
        elif isinstance(tile,dict) and tile.get('kind')=='WEED':command=['DIG']
        elif isinstance(tile,dict) and tile.get('kind')=='PASTURE' and not tile.get('animal'):
            if inv.get('SHEEP',0):command=['PLACE','SHEEP']
        elif isinstance(tile,dict) and tile.get('animal')=='SHEEP':
            if not tile['fed_today'] and inv.get('WHEAT',0):command=['FEED']
            elif not tile['cared_today']:command=['CARE']
            elif tile['yield_units']:command=['HARVEST']
            elif tile['fertilizer_available']:command=['COLLECT_FERTILIZER']
        if command:tasks.append((abs(pos[0]-x)+abs(pos[1]-y),targets.index(target),target,command))
    if tasks:
        _,_,target,command=min(tasks);return _v219_walk(pos,target) or command
    if cargo:return _v219_walk(pos,home) or ['PLACE',cargo[0],inv[cargo[0]]]
    return ['PASS']

def _v234_rescue(obs,action,state):
    if not state['workers'] or int(obs['step'])%24>14:return action
    orders=action.get('market',[])
    if len(orders)>=MAX_ORDERS:return action
    if any(o and (o[0] in ('HIRE','BUY_LAND','BUY_ANIMAL','BUY_PRODUCT','BUY_SEED') or (len(o)>1 and o[1]=='WHEAT')) for o in orders):return action
    farm=obs['farms'][obs['player']];private=obs['private'];hungry=carried=0
    commands=[action.get('farmer') or ['PASS']]+list(action.get('hands') or [])
    for actor,targets in state['workers'].items():
        command=commands[actor]
        if command==['FEED'] or command[:2]==['PICKUP','WHEAT']:return action
        carried+=private['inventories'][actor].get('WHEAT',0)
        hungry+=sum(isinstance(farm['tiles'][y][x],dict) and farm['tiles'][y][x].get('animal')=='SHEEP' and not farm['tiles'][y][x].get('fed_today') for x,y in targets)
    stock=projected_shed(action,FarmView(obs))
    shortage=hungry-carried-stock.get('WHEAT',0)
    if not 0<shortage<=6 or state.get('rescue_today',0)+shortage>6:return action
    quote=int(obs['market']['prices']['WHEAT'])
    if quote<1 or farm['money']<1000+shortage*(quote+10) or sum(stock.values())+shortage>100:return action
    result=copy.deepcopy(action);result['market'].append(['BUY_PRODUCT','WHEAT',shortage])
    state['rescue_today']=state.get('rescue_today',0)+shortage
    _V233_REPORT['sheep_rescue_feed_requests']+=shortage
    return result

def agent(observation,configuration=None):
    action=_V233_PARENT(observation,configuration)
    step=int(observation['step']);player=int(observation['player']);day=step//24
    state=_V233_STATES.get(player)
    if state is None or step<=state['last_step']:
        state={'last_step':step,'day':-1,'workers':{},'work':{},'credit':{'WOOL':0,'FERTILIZER':0}}
        _V233_STATES[player]=state
    state['last_step']=step
    if configuration is not None and any(configuration.get(k,v)!=v for k,v in
        (('boardSize',10),('turnsPerDay',24),('shedCapacity',100),('maxMarketOrdersPerTurn',10))):return action
    if day<11:return action
    farm=observation['farms'][player];private=observation['private']
    if state['day']!=day:state['day']=day;state['workers']={};state['work']={};state['rescue_today']=0
    for actor,previous in state['work'].items():
        if previous['step']!=step-1 or actor>=len(private['inventories']):continue
        item={'HARVEST':'WOOL','COLLECT_FERTILIZER':'FERTILIZER'}.get(previous['command'][0])
        if item:
            gained=max(0,private['inventories'][actor].get(item,0)-previous['inventory'].get(item,0))
            state['credit'][item]+=gained
            _V233_REPORT['sheep_wool_harvested' if item=='WOOL' else 'sheep_fert_collected']+=gained
    pending=state.pop('pending',None)
    if pending:
        funded='SE' in farm['unlocked_quadrants'] and (not pending['initial'] or private['shed'].get('SHEEP',0)>=6)
        if not funded:_V233_REPORT['sheep_purchase_shortfalls']+=1
        elif len(farm['hands'])<pending['first']+pending.get('count',2)-1:_V233_REPORT['sheep_hire_shortfalls']+=1
        else:
            if pending.get('count',2)==1:
                state['workers'][pending['first']]=list(pending['targets'])
                _SL_REPORT['confirmed']+=1
            else:
                for i in range(2):state['workers'][pending['first']+i]=[(x,5+i) for x in range(5,8)]
            _V233_REPORT['sheep_workers_confirmed']+=pending.get('count',2)
            if pending['initial']:state['committed']=True;_V233_REPORT['sheep_committed']+=1
    action=_v233_request(observation,action,state,_IMPL.chassis.players[player])
    if not state.get('committed'):return action
    result=copy.deepcopy(action)
    commands=[result.get('farmer') or ['PASS']]+list(result.get('hands') or [])
    commands += [['PASS'] for _ in range(len(farm['hands'])+1-len(commands))]
    state['work']={}
    for actor,targets in state['workers'].items():
        command=_v233_worker(observation,actor,targets);commands[actor]=command
        state['work'][actor]={'step':step,'command':command,'inventory':dict(private['inventories'][actor])}
    result['farmer'],result['hands']=commands[0],commands[1:]
    result=_v234_rescue(observation,result,state)
    stock=projected_shed(result,FarmView(observation))
    for item in ('WOOL','FERTILIZER'):
        scheduled=sum(int(o[2]) for o in result['market'] if o[:2]==['SELL',item])
        count=min(state['credit'][item],max(0,stock.get(item,0)-scheduled))
        if count and len(result['market'])<MAX_ORDERS:
            result['market'].append(['SELL',item,count]);state['credit'][item]-=count
            _V233_REPORT['sheep_extra_wool_sales' if item=='WOOL' else 'sheep_extra_fert_sales']+=count
    return result

_R46_SHEEP_AGENT=agent
_R46_SHADOW_PARENT=_shadow_terminal
_R46_REPORT={}
def _shadow_terminal(obs,config):
    if _V233_STATES.get(int(obs['player']),{}).get('committed'):return None
    return _R46_SHADOW_PARENT(obs,config)
del agent
def agent(observation,configuration=None):
    try:
        if int(observation.get('step',-1))==0:
            for k in _V233_REPORT:_V233_REPORT[k]=0
        result=_R46_SHEEP_AGENT(observation,configuration)
    except Exception:
        _R46_REPORT['sheep_overlay_errors']=_R46_REPORT.get('sheep_overlay_errors',0)+1
        result={'farmer':['PASS'],'hands':[],'market':[]}
    _R46_REPORT.update(getattr(_V233_PARENT,'telemetry',{}))
    _R46_REPORT.update(_V233_REPORT)
    return result
agent.telemetry=_R46_REPORT
agent=globals().pop('agent')

# EXP182: finite-harvest wheat/carrot input planner; original adaptation.
_R51_INPUT_PARENT=agent
_R51_INPUT_STATES={}
_R51_INPUT_REPORT={}
_R51_INPUT_MAX_WORKERS=2
_R51_INPUT_CROPS={'WHEAT':(2,4,6),'CARROT':(2,3,4)}

def _r51_input_forecast(obs,route,expected):
    step=int(obs['step']);day=step//24;farm=obs['farms'][obs['player']]
    pos=[list(farm['farmer'])]+[list(p) for p in farm['hands'][:expected]];targets={}
    for y,line in enumerate(farm['tiles']):
        for x,tile in enumerate(line):
            if not isinstance(tile,dict) or tile.get('crop') not in _R51_INPUT_CROPS:continue
            item=tile['crop'];first,last,cap=_R51_INPUT_CROPS[item]
            if 1<=day-tile['planted_day']<last:
                targets[(x,y)]={'crop':item,'birth':tile['planted_day'],'yield':tile['yield_units'],
                    'until':tile.get('fertilized_until_day',-1),'watered':tile.get('watered_today',False),'water':[],'harvest':None,'first':first,'last':last,'cap':cap}
    access=((4,4),(5,4),(4,5),(5,5));seen=set()
    # Native continuation ends before the reactive terminal closure planner.
    for t in range(step,min(712,(day+4)*24)):
        tape=_IMPL.chassis.routes[2 if t>=648 else route];a=tape[t]
        for actor,c in enumerate([a.get('farmer') or ['PASS'],*(a.get('hands') or [])][:len(pos)]):
            if not c:continue
            xy=tuple(pos[actor]);target=targets.get(xy)
            if target is not None and target['harvest'] is None:
                if c[0]=='WATER' and (t//24,xy) not in seen:
                    seen.add((t//24,xy))
                    if not(t//24==day and target['watered']) and target['first']<=t//24-target['birth']<=target['last']:target['water'].append(t)
                if c[0]=='HARVEST':target['harvest']=t
            if c[0] in MOVES:
                dx,dy=MOVES[c[0]];pos[actor]=[max(0,min(9,pos[actor][0]+dx)),max(0,min(9,pos[actor][1]+dy))]
        for o in a.get('market',[]):
            if o and o[0]=='HIRE':
                counts={p:sum(tuple(q)==p for q in pos) for p in access}
                pos.append(list(min(access,key=lambda p:(counts[p],access.index(p)))))
        if (t+1)%24==0:pos=[[4,4]]
    return targets

def _r51_input_gain(target,arrival,day):
    if target['harvest'] is None or target['harvest']<=arrival:return 0
    extra=sum(arrival<t<=target['harvest'] and day<=t//24<=day+2 and t//24>target['until'] for t in target['water'])
    baseline=target['yield']+sum(2 if t//24<=target['until'] else 1 for t in target['water'])
    return max(0,min(extra,target['cap']-baseline))

def _r51_input_path(obs,targets,action,index):
    step=int(obs['step']);day=step//24
    ready,start=_r62_input_start(obs,action,index)
    prices={p:max(1,int(obs['market']['prices'][p])-2) for p in ('WHEAT','CARROT')}
    fertilizer=max(1,_r37_market_price('FERTILIZER',obs['market']['inventory']['FERTILIZER']-16)+2)
    # Tuple: penalized value, gross value, next free turn, position, path, used,
    # wheat units, carrot units. No state reads from the rival's private farm.
    beam=[(0,0,ready,start,(),frozenset(),0,0)]
    best=None
    for depth in range(8):
        expanded=[]
        for score,gross,now,pos,path,used,wheat,carrot in beam:
            for xy,target in targets.items():
                if xy in used:continue
                arrival=now+abs(pos[0]-xy[0])+abs(pos[1]-xy[1])
                if arrival>=day*24+23:continue
                gain=_r51_input_gain(target,arrival,day)
                if not gain:continue
                item=target['crop'];new_gross=gross+gain*prices[item]
                new_path=path+((xy[0],xy[1],item,target['birth']),)
                expanded.append((new_gross-1.5*fertilizer*len(new_path),new_gross,arrival+1,xy,new_path,
                                 used|{xy},wheat+(gain if item=='WHEAT' else 0),carrot+(gain if item=='CARROT' else 0)))
        if not expanded:break
        expanded.sort(key=lambda s:(-s[0],-s[1],s[2],s[4]))
        beam=expanded[:8]
        if depth>=2:
            candidate=beam[0]
            if best is None or (-candidate[0],-candidate[1],candidate[2],candidate[4])<(-best[0],-best[1],best[2],best[4]):best=candidate
    if best is None:return [],{'WHEAT':0,'CARROT':0}
    return list(best[4]),{'WHEAT':best[6],'CARROT':best[7]}

def _r51_input_control(obs,action,state):
    step=int(obs['step']);day=step//24;hour=step%24;player=int(obs['player']);farm=obs['farms'][player];private=obs['private']
    native=_IMPL.chassis.players[player]
    if state.get('day')!=day:state.update(day=day,workers={},pending=None,placed=[])
    for x,y in state['placed']:
        tile=farm['tiles'][y][x]
        if isinstance(tile,dict) and tile.get('fertilized_until_day',-1)>=day+2:_R51_INPUT_REPORT['input_confirmed_applications']+=1
        else:_R51_INPUT_REPORT['input_application_errors']+=1
    state['placed']=[]
    if state.get('pending'):
        pending=state.pop('pending')
        for actor,plan in pending.items():
            if len(farm['hands'])>=actor:state['workers'][actor]=plan;_R51_INPUT_REPORT['input_confirmed_hires']+=1
            else:_R51_INPUT_REPORT['input_hire_errors']+=1
    if state['workers']:
        changed=copy.deepcopy(action)
        for actor,plan in state['workers'].items():
            inv=private['inventories'][actor];pos=tuple(farm['hands'][actor-1]);cmd=['PASS']
            if not plan['loaded']:
                stock=projected_shed(changed,FarmView(obs));q=min(plan['quantity'],max(0,stock.get('FERTILIZER',0)))
                if q and _shed_adjacent(pos,10):
                    cmd=['PICKUP','FERTILIZER',q];plan['loaded']=True;_R51_INPUT_REPORT['input_loaded_units']+=q
                    if q<plan['quantity']:_R51_INPUT_REPORT['input_stock_shortfalls']+=plan['quantity']-q
            elif inv.get('FERTILIZER',0):
                while plan['path']:
                    x,y,crop,birth=plan['path'][0];tile=farm['tiles'][y][x]
                    if not isinstance(tile,dict) or tile.get('crop')!=crop or tile.get('planted_day')!=birth or tile.get('fertilized_until_day',-1)>=day+2:
                        plan['path'].pop(0);continue
                    cmd=_v219_walk(pos,(x,y)) or ['FERTILIZE']
                    if cmd==['FERTILIZE']:state['placed'].append((x,y));plan['path'].pop(0);_R51_INPUT_REPORT['input_application_requests']+=1
                    break
            changed['hands'][actor-1]=cmd
        return changed
    if hour not in (1,2,3) or not 12<=day<=28:return action
    planned=_v219_native_day(native,day);expected=max(len(a.get('hands',[])) for a in planned)
    if any(o and o[0]=='HIRE' for a in planned[hour:] for o in a.get('market',[])) or native['pending']:return action
    parents=[_V219_STATES.get(player,{}),_V233_STATES.get(player,{})]
    # A parent may retry after a full market queue; its headcount must remain native.
    if day in (12,18) or any(p.get('committed') and p.get('requested_day')!=day for p in parents):return action
    if any(p.get('pending') for p in parents) or any(o and o[0]=='HIRE' for o in action.get('market',[])):return action
    owned=set(range(1,expected+1))
    for p in parents:
        actors=set(p.get('workers',{}))
        if owned&actors:return action
        owned|=actors
    if owned!=set(range(1,len(farm['hands'])+1)):return action
    targets=_r51_input_forecast(obs,native['route'],expected);plans=[];total_q=0;total_cost=0;all_units={'WHEAT':0,'CARROT':0}
    stock=projected_shed(action,FarmView(obs));purchases=sum(max(0,int(o[2])) for o in action.get('market',[]) if len(o)>2 and o[0] in ('BUY_PRODUCT','BUY_ANIMAL'))
    # Units act before market orders. Preserve the native next-turn pickup,
    # after the current parent's actual sales/purchases, before buying tour inputs.
    available=max(0,stock.get('FERTILIZER',0))
    for o in action.get('market',[]):
        if len(o)>=3 and o[:2]==['SELL','FERTILIZER']:available=max(0,available-max(0,int(o[2])))
        elif len(o)>=3 and o[:2]==['BUY_PRODUCT','FERTILIZER']:available+=max(0,int(o[2]))
    next_native=planned[hour+1];native_pickups=sum(max(0,int(c[2]) if len(c)>2 else 1) for c in [next_native.get('farmer') or ['PASS'],*(next_native.get('hands') or [])] if len(c)>1 and c[:2]==['PICKUP','FERTILIZER'])
    topup=max(0,native_pickups-available)
    plans,total_q,total_cost,all_units=_r68_joint_plans(obs,action,targets,stock,purchases,topup)
    if not plans:return action
    state['pending']={len(farm['hands'])+1+i:plan for i,plan in enumerate(plans)}
    _R51_INPUT_REPORT['input_hire_requests']+=len(plans);_R51_INPUT_REPORT['input_purchase_requests']+=total_q+topup
    _R51_INPUT_REPORT['input_forecast_wheat']+=all_units['WHEAT'];_R51_INPUT_REPORT['input_forecast_carrot']+=all_units['CARROT']
    changed=copy.deepcopy(action);changed['market'] += [['BUY_PRODUCT','FERTILIZER',total_q+topup]]+[['HIRE'] for _ in plans];return changed

def agent(observation,configuration=None):
    try:
        step=int(observation['step']);player=int(observation['player']);state=_R51_INPUT_STATES.get(player)
        if state is None or step<=state['step']:
            state=_R51_INPUT_STATES[player]={'step':-1}
            _R51_INPUT_REPORT.update(input_hire_requests=0,input_confirmed_hires=0,input_hire_errors=0,input_purchase_requests=0,
                input_loaded_units=0,input_stock_shortfalls=0,input_application_requests=0,input_confirmed_applications=0,
                input_application_errors=0,input_errors=0,input_forecast_wheat=0,input_forecast_carrot=0)
        state['step']=step;action=_R51_INPUT_PARENT(observation,configuration)
        if configuration is None or all(configuration.get(k,v)==v for k,v in [('boardSize',10),('turnsPerDay',24),('shedCapacity',100),('maxMarketOrdersPerTurn',10)]):
            action=_r51_input_control(observation,action,state)
        _R51_INPUT_REPORT.update(getattr(_R51_INPUT_PARENT,'telemetry',{}));return action
    except Exception:
        _R51_INPUT_REPORT['input_errors']=_R51_INPUT_REPORT.get('input_errors',0)+1
        return {'farmer':['PASS'],'hands':[],'market':[]}
agent.telemetry=_R51_INPUT_REPORT
agent=globals().pop('agent')

# EXP182: project the final hour's actual worker actions before automatic deposit.
_R51_WAREHOUSE_PARENT=agent
_R51_WAREHOUSE_REPORT={}

def _r51_close_warehouse(obs,action):
    step=int(obs['step']);day=step//24
    if step%24!=23 or not 12<=day<=28:return action
    # No speculative product purchase/worker count model: these hours abstain.
    if any(o and o[0] not in ('SELL',) for o in action.get('market',[])):return action
    farm,private=_PLANNER_NS['_clone_state'](obs['farms'][obs['player']],obs['private'])
    commands=[action.get('farmer') or ['PASS'],*(action.get('hands') or [])]
    demand={}
    for c in commands:
        if len(c)>1 and c[0]=='PLANT':demand[c[1]]=demand.get(c[1],0)+1
    blocked={k for k,q in demand.items() if q>private['seeds'].get(k,0)}
    for actor,c in enumerate(commands[:len(private['inventories'])]):
        if len(c)>1 and c[0]=='PLANT' and c[1] in blocked:c=['PASS']
        _PLANNER_NS['_apply_unit_action'](farm,private,actor,c,10,day,24,100)
    post=dict(private['shed'])
    for o in action.get('market',[]):
        if len(o)>=3 and o[0]=='SELL':post[o[1]]=max(0,post.get(o[1],0)-max(0,int(o[2])))
    needed=sum(post.values())+sum(max(0,q) for inv in private['inventories'] for q in inv.values())-100
    if needed<=0:return action
    result=copy.deepcopy(action);orders=result['market']
    # Grain and fertilizer have native input obligations; other products do not.
    # Additional commodity sales are bounded by actual post-action physical stock.
    for item in sorted((p for p in PRODUCTS if p not in ('WHEAT','FERTILIZER')),key=lambda p:-obs['market']['prices'].get(p,0)):
        qty=min(needed,post.get(item,0))
        if not qty:continue
        existing=next((o for o in orders if len(o)>=3 and o[:2]==['SELL',item]),None)
        if existing is not None:existing[2]=max(0,int(existing[2]))+qty
        elif len(orders)<10:orders.append(['SELL',item,qty])
        else:continue
        needed-=qty;post[item]-=qty;_R51_WAREHOUSE_REPORT['warehouse_extra_sales']+=qty
        if needed<=0:break
    if needed>0:
        native=_IMPL.chassis.players[int(obs['player'])];reserve=0
        for t in range(step+1,719):
            future=_IMPL.chassis.routes[2 if t>=648 else native['route']][t]
            for c in [future.get('farmer') or ['PASS'],*(future.get('hands') or [])]:
                if len(c)>1 and c[:2]==['PICKUP','WHEAT']:reserve+=max(0,int(c[2]) if len(c)>2 else 1)
            if any(len(o)>1 and o[:2]==['BUY_PRODUCT','WHEAT'] for o in future.get('market',[])):break
        incoming=sum(max(0,inv.get('WHEAT',0)) for inv in private['inventories'])
        others=sum(q for p,q in post.items() if p!='WHEAT')+sum(max(0,q) for inv in private['inventories'] for p,q in inv.items() if p!='WHEAT')
        # Even if every other carried item deposits first, this grain reserve fits.
        qty=min(needed,post.get('WHEAT',0),max(0,post.get('WHEAT',0)+incoming-reserve)) if 100-others>=reserve else 0
        existing=next((o for o in orders if len(o)>=3 and o[:2]==['SELL','WHEAT']),None)
        if qty and (existing is not None or len(orders)<10):
            if existing is not None:existing[2]=max(0,int(existing[2]))+qty
            else:orders.append(['SELL','WHEAT',qty])
            needed-=qty;_R51_WAREHOUSE_REPORT['warehouse_extra_sales']+=qty
    _R51_WAREHOUSE_REPORT['warehouse_projected_unresolved']+=max(0,needed)
    if result!=action:_R51_WAREHOUSE_REPORT['warehouse_changed_turns']+=1
    return result

def agent(observation,configuration=None):
    result=_R51_WAREHOUSE_PARENT(observation,configuration)
    try:
        if int(observation['step'])==0:_R51_WAREHOUSE_REPORT.update(warehouse_changed_turns=0,warehouse_extra_sales=0,warehouse_projected_unresolved=0,warehouse_errors=0)
        if configuration is None or all(configuration.get(k,v)==v for k,v in [('boardSize',10),('turnsPerDay',24),('shedCapacity',100),('maxMarketOrdersPerTurn',10)]):result=_r51_close_warehouse(observation,result)
    except Exception:_R51_WAREHOUSE_REPORT['warehouse_errors']=_R51_WAREHOUSE_REPORT.get('warehouse_errors',0)+1
    _R51_WAREHOUSE_REPORT.update(getattr(_R51_WAREHOUSE_PARENT,'telemetry',{}));return result
agent.telemetry=_R51_WAREHOUSE_REPORT
agent=globals().pop('agent')

from itertools import permutations as _r53_permutations
_R53_LABOR_REPORT=dict(labor_requests=0,labor_hires_avoided=0,labor_spawn_errors=0,labor_confirmed=0,labor_day26=0,labor_day27=0,labor_day28=0)

def _r53_labor_assignment(obs,action,fertilizer):
    step=int(obs['step']);day=step//24;farm=obs['farms'][obs['player']]
    if day not in (26,27,28) or step%24>2:return None
    # Do not preempt a later price-gated fertilizer request with a smaller unfertilized team.
    if day==27 and not fertilizer:return None
    count=3 if fertilizer else 2
    positions=[list(farm['farmer'])]+[list(p) for p in farm['hands']]
    for i,c in enumerate([action.get('farmer') or ['PASS'],*(action.get('hands') or [])][:len(positions)]):
        if c and c[0] in MOVES:
            dx,dy=MOVES[c[0]];positions[i]=[max(0,min(9,positions[i][0]+dx)),max(0,min(9,positions[i][1]+dy))]
    access=((4,4),(5,4),(4,5),(5,5));spawns=[]
    native_hires=sum(bool(o) and o[0]=='HIRE' for o in action.get('market',[]))
    for i in range(native_hires+count):
        chosen=min(access,key=lambda p:(sum(tuple(q)==p for q in positions),access.index(p)));positions.append(list(chosen))
        if i>=native_hires:spawns.append(chosen)
    groups=(((5,5),(6,5),(7,5),(8,5)),((9,5),(9,6),(8,6)),((5,6),(6,6),(7,6))) if fertilizer else (tuple((x,5) for x in range(5,10)),tuple((x,6) for x in range(5,10)))
    choices=[];remaining=23-step%24
    for assignment in _r53_permutations(groups):
        costs=[]
        for start,path in zip(spawns,assignment):
            distance=abs(start[0]-path[0][0])+abs(start[1]-path[0][1])
            distance+=sum(abs(a[0]-b[0])+abs(a[1]-b[1]) for a,b in zip(path,path[1:]))
            distance+=min(abs(path[-1][0]-x)+abs(path[-1][1]-y) for x,y in access)
            costs.append(distance+(3 if fertilizer else 2)*len(path)+1+int(fertilizer))
        if max(costs)<=remaining:choices.append((max(costs),sum(costs),assignment))
    if not choices:return None
    _,_,assignment=min(choices)
    return dict(paths=assignment,spawns=spawns,remaining=remaining,workers=count,fertilizer=fertilizer)

_R53_LABOR_PARENT=agent
def agent(observation,configuration=None):
    if isinstance(observation,dict) and observation.get('step')==0:
        for k in _R53_LABOR_REPORT:_R53_LABOR_REPORT[k]=0
    result=_R53_LABOR_PARENT(observation,configuration)
    _R53_LABOR_COMBINED.update(getattr(_R53_LABOR_PARENT,'telemetry',{}));_R53_LABOR_COMBINED.update(_R53_LABOR_REPORT)
    return result
_R53_LABOR_COMBINED={}
agent.telemetry=_R53_LABOR_COMBINED
agent=globals().pop('agent')

# EXP193: deterministic HIRE spawn after native unit actions, then next-turn pickup.
def _r62_input_start(obs,action,index):
    farm=obs['farms'][obs['player']]
    positions=[list(farm['farmer'])]+[list(p) for p in farm['hands']]
    for actor,c in enumerate([action.get('farmer') or ['PASS'],*(action.get('hands') or [])][:len(positions)]):
        if c and c[0] in MOVES:
            dx,dy=MOVES[c[0]]
            positions[actor]=[max(0,min(9,positions[actor][0]+dx)),max(0,min(9,positions[actor][1]+dy))]
    access=((4,4),(5,4),(4,5),(5,5))
    native_hires=sum(bool(o) and o[0]=='HIRE' for o in action.get('market',[]))
    for _ in range(native_hires+index+1):
        chosen=min(access,key=lambda p:(sum(tuple(q)==p for q in positions),access.index(p)))
        positions.append(list(chosen))
    return int(obs['step'])+2,chosen

agent=globals().pop('agent')

def _r68_joint_plans(obs,action,targets,stock,purchases,topup):
    farm=obs['farms'][obs['player']];choices=[]
    for mode,first_crop in enumerate((None,'WHEAT','CARROT')):
        remaining=dict(targets);plans=[];total_q=0;total_cost=0;total_value=0
        all_units={'WHEAT':0,'CARROT':0}
        for i in range(_R51_INPUT_MAX_WORKERS):
            subset={xy:t for xy,t in remaining.items() if t['crop']==first_crop} if i==0 and first_crop else remaining
            path,units=_r51_input_path(obs,subset,action,i);q=len(path)
            if q<3 or len(action.get('market',[]))+2+i>10 or sum(stock.values())+purchases+total_q+q+topup>95:break
            quote=_r37_market_price('FERTILIZER',obs['market']['inventory']['FERTILIZER']-total_q-q-topup)
            cost=(q+(topup if i==0 else 0))*(quote+2)+_v219_fib(int(farm['hires_today'])+i)
            value=sum(n*max(1,_r37_market_price(item,obs['market']['inventory'][item]+all_units[item]+n)-2) for item,n in units.items())
            if value<1.5*cost+50 or farm['money']<total_cost+cost+3000:break
            plans.append({'path':path,'quantity':q,'loaded':False});total_q+=q;total_cost+=cost;total_value+=value
            for item,n in units.items():all_units[item]+=n
            for x,y,_,_ in path:remaining.pop((x,y),None)
        score=(total_value-total_cost,total_value,-total_cost,-len(plans),-mode)
        choices.append((score,plans,total_q,total_cost,all_units))
    _,plans,total_q,total_cost,all_units=max(choices,key=lambda v:v[0])
    return plans,total_q,total_cost,all_units

agent=globals().pop('agent')

_R70_STATES={}
_R70_REPORT={}

def _r70_parent_fert_qty(obs,action,planned,offset):
    stock=dict(projected_shed(action,FarmView(obs)))
    for order in action.get('market',[]):
        if len(order)<3:continue
        op,item,quantity=order[:3];quantity=max(0,int(quantity))
        if op=='SELL':stock[item]=max(0,stock.get(item,0)-quantity)
        elif op in ('BUY_PRODUCT','BUY_ANIMAL'):
            stock[item]=stock.get(item,0)+min(quantity,max(0,100-sum(stock.values())))
    next_action=planned[offset+1] if offset+1<len(planned) else {}
    commands=[next_action.get('farmer') or ['PASS'],*(next_action.get('hands') or [])]
    native_need=sum(max(0,int(c[2]) if len(c)>2 else 1) for c in commands if len(c)>1 and c[:2]==['PICKUP','FERTILIZER'])
    quantity=max(10,10+native_need-max(0,stock.get('FERTILIZER',0)))
    if quantity>max(0,100-sum(stock.values())):
        _R70_REPORT['parent_input_capacity_declines']+=1
        return 10
    if quantity>10:
        _R70_REPORT['parent_input_guard_turns']+=1
        _R70_REPORT['parent_input_guard_extra_units']+=quantity-10
    return quantity

def _r70_before(obs):
    player=int(obs['player']);step=int(obs['step']);state=_R70_STATES.get(player)
    if state is None or step<=state['step']:
        state=_R70_STATES[player]={'step':-1,'pending':[],'roles':set()}
        _R70_REPORT.update(parent_input_guard_turns=0,parent_input_guard_extra_units=0,
            parent_input_requests=0,parent_input_confirmed=0,parent_input_shortfalls=0,
            parent_input_errors=0,parent_input_capacity_declines=0)
    state['step']=step
    for request in state['pending']:
        actor,quantity,old=request
        actual=max(0,int(obs['private']['inventories'][actor].get('FERTILIZER',0))-old)
        _R70_REPORT['parent_input_confirmed']+=min(quantity,actual)
        _R70_REPORT['parent_input_shortfalls']+=max(0,quantity-actual)
    state['pending']=[]
    return state

def _r70_after(obs,action,state):
    player=int(obs['player']);day=int(obs['step'])//24
    for actor,role in _V219_STATES.get(player,{}).get('workers',{}).items():
        if not role.get('needs_fertilizer'):continue
        key=(day,actor);inv=obs['private']['inventories'][actor].get('FERTILIZER',0)
        if key not in state['roles']:
            state['roles'].add(key)
            desired=role.get('fertilizer_quantity',10 if role['kind']=='fertilizer' else 5)
            if role.get('loaded') and not role.get('pickup_requested') and inv<desired:
                _R70_REPORT['parent_input_shortfalls']+=desired-inv
        command=action.get('hands',[])[actor-1] if actor<=len(action.get('hands',[])) else ['PASS']
        if len(command)>1 and command[:2]==['PICKUP','FERTILIZER']:
            quantity=max(0,int(command[2]) if len(command)>2 else 1)
            _R70_REPORT['parent_input_requests']+=quantity
            state['pending'].append((actor,quantity,int(inv)))

_R70_PARENT=agent

def agent(observation,configuration=None):
    state=None
    try:state=_r70_before(observation)
    except Exception:_R70_REPORT['parent_input_errors']=_R70_REPORT.get('parent_input_errors',0)+1
    result=_R70_PARENT(observation,configuration)
    try:
        if state is not None:_r70_after(observation,result,state)
    except Exception:_R70_REPORT['parent_input_errors']=_R70_REPORT.get('parent_input_errors',0)+1
    _R70_REPORT.update(getattr(_R70_PARENT,'telemetry',{}))
    return result

agent.telemetry=_R70_REPORT
agent=globals().pop('agent')

def _r79_tomato_fertilizer_worthwhile(obs,action):
    if obs['market']['prices']['FERTILIZER']<=30:return True
    farm=obs['farms'][obs['player']];day=int(obs['step'])//24;bonus=0
    for y in (5,6):
        for x in range(5,10):
            tile=farm['tiles'][y][x]
            if not isinstance(tile,dict) or tile.get('crop')!='TOMATO':continue
            birth=tile['planted_day'];until=tile.get('fertilized_until_day',-1)
            bonus+=sum(until<d and 8<=d+1-birth<=11 for d in range(day,day+3))
    if not bonus:return False
    inventory=obs['market']['inventory']
    price=max(1,_r37_market_price('TOMATO',inventory['TOMATO']+bonus+10)-2)
    fertilizer=max(1,_r37_market_price('FERTILIZER',inventory['FERTILIZER']-10)+2)
    native_hires=sum(bool(o) and o[0]=='HIRE' for o in action.get('market',[]))
    extra_labor=_v219_fib(int(farm['hires_today'])+native_hires+3)
    return bonus*price>=2*(10*fertilizer+extra_labor)+100

agent=globals().pop('agent')

# EXP216: original adaptation of economic feed and fertilizer-sale concepts.
# Conceptual credit: Steven Lee Hans, "Lord Momo Returns", September12 snapshot.
_R85_FEED = True
_R85_FERT = True
_R85_PARENT = agent
_R85_STATES = {}
_R85_REPORT = {}

def _r85_feed(obs, action):
    step=int(obs['step']);day=step//24
    if not 10<=day<=28 or step%24>21:return action
    player=int(obs['player']);native=_IMPL.chassis.players[player]
    tape=_v219_native_day(native,day)
    expected=max(len(a.get('hands',[])) for a in tape)
    farm=obs['farms'][player];positions=[farm['farmer'],*farm['hands']]
    commands=[action.get('farmer') or ['PASS'],*(action.get('hands') or [])]
    prices=obs['market']['prices'];changed=False
    for actor,command in enumerate(commands[:expected+1]):
        if command!=['FEED'] or actor>=len(positions):continue
        tile=_tile_at(farm['tiles'],positions[actor])
        if not isinstance(tile,dict) or tile.get('animal') not in ('GOOSE','COW','SHEEP'):continue
        if tile.get('fed_today') or int(tile.get('consecutive_unfed',0))!=0:continue
        if int(obs['private']['inventories'][actor].get('WHEAT',0))<=0:continue
        item={'GOOSE':'EGG','COW':'MILK','SHEEP':'WOOL'}[tile['animal']]
        bonus=_r88_feed_bonus_cost(tile,day)
        if bonus*(float(prices[item])+5)*1.25>=float(prices['WHEAT']):continue
        if not _r86_next_feed(obs,positions[actor]):continue
        commands[actor]=['PASS'];changed=True
        _R85_REPORT['feed_skips']+=1
    if not changed:return action
    result=copy.deepcopy(action);result['farmer'],result['hands']=commands[0],commands[1:]
    return result

def _r85_reserve(obs, state):
    step=int(obs['step']);player=int(obs['player']);native=_IMPL.chassis.players[player]
    route=native['route'];key=(route,step)
    cache=state.setdefault('native_reserves',{})
    if route not in cache:
        # Backward recurrence preserves field-before-market order within a turn.
        reserve=[0]*720
        for t in range(718,-1,-1):
            a=_IMPL.chassis.routes[2 if t>=648 else route][t]
            pickup=sum(max(0,int(c[2]) if len(c)>2 else 1) for c in [a.get('farmer') or ['PASS'],*(a.get('hands') or [])] if len(c)>1 and c[:2]==['PICKUP','FERTILIZER'])
            purchase=sum(max(0,int(o[2])) for o in a.get('market',[]) if len(o)>2 and o[:2]==['BUY_PRODUCT','FERTILIZER'])
            reserve[t]=pickup+max(0,reserve[t+1]-purchase)
        cache[route]=reserve
    dedicated=0
    for parent in (_V219_STATES.get(player,{}),_V233_STATES.get(player,{})):
        for actor,role in parent.get('workers',{}).items():
            if not isinstance(role,dict) or not role.get('needs_fertilizer') or role.get('loaded'):continue
            desired=role.get('fertilizer_quantity',10 if role.get('kind')=='fertilizer' else 5)
            carried=obs['private']['inventories'][actor].get('FERTILIZER',0)
            dedicated+=max(0,desired-carried)
        pending=parent.get('pending') or {}
        if pending.get('fertilizer'):dedicated+=10
    inputs=_R51_INPUT_STATES.get(player,{})
    for actor,plan in {**inputs.get('workers',{}),**(inputs.get('pending') or {})}.items():
        if not plan.get('loaded'):dedicated+=max(0,int(plan['quantity']))
    return max(14,cache[route][min(719,step+1)]+dedicated)

def _r85_fertilizer(obs, action, state):
    step=int(obs['step']);day=step//24
    if not 6<=day<=28:return action
    market=action.get('market',[])
    if len(market)>=MAX_ORDERS or any(o and o[0]!='SELL' for o in market):return action
    stock=projected_shed(action,FarmView(obs))
    held=max(0,int(stock.get('FERTILIZER',0)))
    sold=sum(max(0,int(o[2])) for o in market if len(o)>2 and o[:2]==['SELL','FERTILIZER'])
    extra=held-sold-_r85_reserve(obs,state)
    if extra<=0:return action
    result=copy.deepcopy(action);result['market'].append(['SELL','FERTILIZER',extra])
    _R85_REPORT['fert_sale_turns']+=1;_R85_REPORT['fert_sale_units']+=extra
    return result

def agent(observation, configuration=None):
    result=_R85_PARENT(observation,configuration)
    try:
        step=int(observation['step']);player=int(observation['player'])
        state=_R85_STATES.get(player)
        if state is None or step<=state['step']:
            state=_R85_STATES[player]={'step':-1}
            _R85_REPORT.update(feed_skips=0,fert_sale_turns=0,fert_sale_units=0,economic_overlay_errors=0)
        state['step']=step
        if configuration is not None and any(configuration.get(k,v)!=v for k,v in [('boardSize',10),('turnsPerDay',24),('shedCapacity',100),('maxMarketOrdersPerTurn',10)]):return result
        if _R85_FEED:result=_r85_feed(observation,result)
        if _R85_FERT:result=_r85_fertilizer(observation,result,state)
        if step%24==23:result=_r51_close_warehouse(observation,result)
    except Exception:
        _R85_REPORT['economic_overlay_errors']=_R85_REPORT.get('economic_overlay_errors',0)+1
    _R85_REPORT.update(getattr(_R85_PARENT,'telemetry',{}))
    return result

agent.telemetry=_R85_REPORT
agent=globals().pop('agent')

# EXP217: planned next-day service is required before discretionary feed cuts.
_R86_FEED_CACHE = {}

def _r86_next_feed(obs, target):
    step=int(obs['step']);day=step//24
    if day==28:return True  # No second dawn follows before game termination.
    player=int(obs['player']);native=_IMPL.chassis.players[player]
    tomorrow=day+1;route=2 if tomorrow>=27 else native['route'];key=(route,tomorrow)
    if key not in _R86_FEED_CACHE:
        positions=[(4,4)];wheat=[0];access=((4,4),(5,4),(4,5),(5,5));feeds=set()
        for hour in range(24):
            a=_IMPL.chassis.routes[route][tomorrow*24+hour]
            commands=[a.get('farmer') or ['PASS'],*(a.get('hands') or [])]
            for actor,command in enumerate(commands[:len(positions)]):
                if not command:continue
                pos=positions[actor];op=command[0]
                if op in MOVES:
                    dx,dy=MOVES[op];positions[actor]=(max(0,min(9,pos[0]+dx)),max(0,min(9,pos[1]+dy)))
                elif command[:2]==['PICKUP','WHEAT'] and pos in access:
                    wheat[actor]+=max(0,int(command[2]) if len(command)>2 else 1)
                elif op=='FEED' and wheat[actor]>0:
                    wheat[actor]-=1
                    if hour<=21:feeds.add(pos)
                elif op=='DROP' and pos in access:wheat[actor]=0
                elif command[:2]==['PLACE','WHEAT'] and pos in access:
                    wheat[actor]=max(0,wheat[actor]-max(0,int(command[2]) if len(command)>2 else 1))
            for order in a.get('market',[]):
                if order and order[0]=='HIRE':
                    chosen=min(access,key=lambda p:(positions.count(p),access.index(p)))
                    positions.append(chosen);wheat.append(0)
        _R86_FEED_CACHE[key]=frozenset(feeds)
    return tuple(target) in _R86_FEED_CACHE[key]

agent=globals().pop('agent')

# EXP219: charge care credits only when this feeding decision can affect them.
_R88_PHASE = True
_R88_HORIZON = True
_R88_ANIMAL_DAYS = {'GOOSE': (4, 1), 'COW': (8, 2), 'SHEEP': (6, 3)}


def _r88_feed_bonus_cost(tile, day):
    first, interval = _R88_ANIMAL_DAYS[tile['animal']]
    first += int(tile['placed_day'])
    tomorrow = day + 1
    produces = tomorrow >= first and (tomorrow - first) % interval == 0
    pending = max(0, int(tile.get('pending_care_bonus', 0)))
    if _R88_PHASE and not produces:
        pending = 0  # It remains banked on non-production dawns.
    care = 1  # Conservative: charge one possible CARE even if not yet observed.
    if _R88_HORIZON:
        # Today's care is added AFTER tomorrow's production; its first possible
        # payout is a later production dawn, which must occur before game end.
        next_use = first
        if next_use <= tomorrow:
            next_use += ((tomorrow - next_use) // interval + 1) * interval
        if next_use > 29:
            care = 0
    return pending + care


agent = globals().pop('agent')

# EXP226: retain physical grain for two complete days before trimming a buy.
_R95_PARENT = agent
_R95_REPORT = {}
_R95_RESERVES = {}

def _r95_reserve(obs):
    step=int(obs['step']);player=int(obs['player'])
    native=_IMPL.chassis.players[player];route=native['route']
    key=(route,step)
    if key not in _R95_RESERVES:
        demand=6  # Physical buffer beyond every scheduled pickup and sale.
        for t in range(step+1,min(719,step+49)):
            a=_IMPL.chassis.routes[2 if t>=648 else route][t]
            for c in [a.get('farmer') or ['PASS'],*(a.get('hands') or [])]:
                if c[:2]==['PICKUP','WHEAT']:
                    demand+=max(0,int(c[2]) if len(c)>2 else 1)
            for o in a.get('market',[]):
                if len(o)>2 and o[:2]==['SELL','WHEAT']:
                    demand+=max(0,int(o[2]))
        _R95_RESERVES[key]=demand
    demand=_R95_RESERVES[key]
    # Reserve full feed for a possible southeast sheep commitment. Do not
    # rely on its future discretionary buy, eligibility, or existing cargo.
    if obs['town']['unlocked_shops'].count('YARN_STORE')>=2:
        demand+=6*len({t//24 for t in range(step+1,step+49) if t//24>=12})
    return demand

def _r95_replenish(obs,action):
    step=int(obs['step'])
    if not 10<=step//24<=11:return action
    orders=action.get('market') or []
    if not any(len(o)>2 and o[:2]==['BUY_PRODUCT','WHEAT'] and int(o[2])>0 for o in orders):return action
    # Preserve all same-turn grain trading/arbitrage sequences unchanged.
    if any(o[:2]==['SELL','WHEAT'] for o in orders):return action
    farm,private=_PLANNER_NS['_clone_state'](obs['farms'][obs['player']],obs['private'])
    commands=[action.get('farmer') or ['PASS'],*(action.get('hands') or [])]
    for actor,c in enumerate(commands[:len(private['inventories'])]):
        _PLANNER_NS['_apply_unit_action'](farm,private,actor,c,10,step//24,24,100)
    held=max(0,int(private['shed'].get('WHEAT',0)))
    reserve=_r95_reserve(obs);result=None;removed=0
    for i,o in enumerate(orders):
        if len(o)<3 or o[:2]!=['BUY_PRODUCT','WHEAT']:continue
        quantity=max(0,int(o[2]));retained=min(quantity,max(0,reserve-held))
        held+=retained
        if retained<quantity:
            if result is None:result=copy.deepcopy(action)
            result['market'][i][2]=retained  # Zero keeps every later order slot.
            removed+=quantity-retained
    if result is None:return action
    _R95_REPORT['replenishment_trim_turns']+=1
    _R95_REPORT['replenishment_trim_units']+=removed
    return result

def agent(observation,configuration=None):
    result=_R95_PARENT(observation,configuration)
    try:
        if int(observation['step'])==0:
            _R95_REPORT.update(replenishment_trim_turns=0,replenishment_trim_units=0,replenishment_errors=0)
        if configuration is not None and any(configuration.get(k,v)!=v for k,v in [('boardSize',10),('turnsPerDay',24),('shedCapacity',100),('maxMarketOrdersPerTurn',10)]):return result
        result=_r95_replenish(observation,result)
    except Exception:
        _R95_REPORT['replenishment_errors']=_R95_REPORT.get('replenishment_errors',0)+1
    _R95_REPORT.update(getattr(_R95_PARENT,'telemetry',{}))
    return result

agent.telemetry=_R95_REPORT
agent=globals().pop('agent')

# EXP231: protect inputs using funded current orders without unassigned cash padding from observed physical resources.
_R97_PARENT=agent
_R97_REPORT={}
_R97_LAST={}

def _r97_market_stock(shed,orders):
    stock=dict(shed);buys={};sales={}
    for index,order in enumerate(orders):
        if len(order)<3:continue
        op,item,n=order[:3];n=max(0,int(n))
        if op=='SELL':
            q=min(n,max(0,stock.get(item,0)));stock[item]=stock.get(item,0)-q;sales[index]=q
        elif op in ('BUY_PRODUCT','BUY_ANIMAL'):
            q=min(n,max(0,100-sum(stock.values())));stock[item]=stock.get(item,0)+q;buys[index]=q
    return stock,buys,sales

def _r97_delivery(stock,private,night):
    stock=dict(stock);lost={}
    if night:
        for inv in private['inventories']:
            for item,q in inv.items():
                q=max(0,int(q));take=min(q,max(0,100-sum(stock.values())))
                stock[item]=stock.get(item,0)+take
                if q>take:lost[item]=lost.get(item,0)+q-take
    return stock,lost

def _r97_budget(obs,orders):
    farm=obs['farms'][obs['player']];cost=0;hires=int(farm['hires_today'])
    # At most ten 100-unit purchases per opponent turn. The additional 1000
    # own units give an intentionally conservative upper bound on buy quotes.
    prices={p:_r37_market_price(p,obs['market']['inventory'][p]-2000) for p in ('WHEAT','FERTILIZER')}
    for order in orders:
        if not order:continue
        op=order[0]
        if op=='HIRE':cost+=_v219_fib(hires);hires+=1
        elif op=='BUY_LAND':cost+=4000
        elif len(order)>2:
            item=order[1];q=max(0,int(order[2]))
            if op=='BUY_PRODUCT':cost+=q*prices[item]
            elif op=='BUY_ANIMAL':cost+=q*{'GOOSE':300,'COW':400,'SHEEP':500}[item]
            elif op=='BUY_SEED':cost+=q*{'WHEAT':10,'CARROT':20,'TOMATO':50,'STRAWBERRY':100,'MELON':80}[item]
    return cost<=farm['money']  # No current sale proceeds are assumed.

def _r97_supply(obs,action):
    step=int(obs['step']);player=int(obs['player']);day=step//24
    if not 144<=step<695:return action
    native=_IMPL.chassis.players[player]
    future=_IMPL.chassis.routes[2 if step+1>=648 else native['route']][step+1]
    commands=[future.get('farmer') or ['PASS'],*(future.get('hands') or [])]
    following=_IMPL.chassis.routes[2 if step+2>=648 else native['route']][step+2]
    next_orders=future.get('market') or []
    prefund=0
    if len(next_orders)==10 and not any(o[:2] in (['BUY_PRODUCT','WHEAT'],['SELL','WHEAT']) for o in next_orders):
        later=[following.get('farmer') or ['PASS'],*(following.get('hands') or [])]
        demand=lambda cs:sum(max(0,int(c[2]) if len(c)>2 else 1) for c in cs if c[:2]==['PICKUP','WHEAT'])
        if demand(later):prefund=demand(commands)+demand(later)
    if not prefund and not any(c[:2]==['PICKUP','WHEAT'] for c in commands):return action
    orders=action.get('market') or []
    if len(orders)>10 or not _r97_budget(obs,orders):
        _R97_REPORT['supply_budget_declines']+=1;return action
    farm,private=_PLANNER_NS['_clone_state'](obs['farms'][player],obs['private'])
    for actor,c in enumerate([action.get('farmer') or ['PASS'],*(action.get('hands') or [])][:len(private['inventories'])]):
        _PLANNER_NS['_apply_unit_action'](farm,private,actor,c,10,day,24,100)
    positions=[tuple(farm['farmer']),*map(tuple,farm['hands'])];night=step%24==23
    access=((4,4),(5,4),(4,5),(5,5))
    if night:positions=[(4,4)]
    else:
        for order in orders:
            if order and order[0]=='HIRE':positions.append(min(access,key=lambda p:(positions.count(p),access.index(p))))
    need=sum(max(0,int(c[2]) if len(c)>2 else 1) for pos,c in zip(positions,commands) if pos in access and c[:2]==['PICKUP','WHEAT'])
    need=max(need,prefund)
    if not need:return action
    original_stock,original_buys,_=_r97_market_stock(private['shed'],orders)
    original_final,original_loss=_r97_delivery(original_stock,private,night)
    if original_final.get('WHEAT',0)>=need:return action
    result=copy.deepcopy(action);proposed=result['market'];blocked=False
    def project(candidate):
        stock,buys,sales=_r97_market_stock(private['shed'],candidate)
        final,loss=_r97_delivery(stock,private,night)
        safe=all(buys.get(i,0)>=q for i,q in original_buys.items()) and all(q<=original_loss.get(item,0) for item,q in loss.items())
        return final,sales,safe
    # Hold an existing grain sale first. Preserve all order indices and every
    # originally funded buy; no extra overnight overflow may be introduced.
    for index in range(len(proposed)-1,-1,-1):
        if proposed[index][:2]!=['SELL','WHEAT']:continue
        final,sales,safe=project(proposed);shortage=max(0,need-final.get('WHEAT',0))
        if not shortage:break
        sold=sales.get(index,0)
        if not sold:continue
        old=proposed[index][2];proposed[index][2]=max(0,sold-shortage)
        after,_,safe=project(proposed)
        if not safe or after.get('WHEAT',0)<=final.get('WHEAT',0):proposed[index][2]=old
    final,_,safe=project(proposed);shortage=max(0,need-final.get('WHEAT',0))
    if shortage:
        last_sale=max((i for i,o in enumerate(proposed) if o[:2]==['SELL','WHEAT']),default=-1)
        index=next((i for i in range(len(proposed)-1,last_sale,-1) if proposed[i][:2]==['BUY_PRODUCT','WHEAT']),None)
        if index is not None:proposed[index][2]=max(0,int(proposed[index][2]))+shortage
        elif len(proposed)<10:proposed.append(['BUY_PRODUCT','WHEAT',shortage])
        else:_R97_REPORT['supply_slot_declines']+=1;return action
    final,_,safe=project(proposed)
    if not safe or final.get('WHEAT',0)<need:
        _R97_REPORT['supply_capacity_declines']+=1;return action
    if not _r97_budget(obs,proposed):
        _R97_REPORT['supply_budget_declines']+=1;return action
    if prefund:
        _R97_REPORT['supply_prefund_changes']+=1
        _R97_REPORT['supply_prefund_units']+=max(0,final.get('WHEAT',0)-original_final.get('WHEAT',0))
    if step<288:
        _R97_REPORT['supply_early_changes']+=1
        _R97_REPORT['supply_early_units']+=max(0,final.get('WHEAT',0)-original_final.get('WHEAT',0))
    _R97_REPORT['supply_guard_changes']+=1
    _R97_REPORT['supply_grain_protected']+=final.get('WHEAT',0)-original_final.get('WHEAT',0)
    _R97_REPORT['supply_buy_units']+=sum(max(0,int(o[2])) for o in proposed if o[:2]==['BUY_PRODUCT','WHEAT'])-sum(max(0,int(o[2])) for o in orders if o[:2]==['BUY_PRODUCT','WHEAT'])
    return result

def agent(observation,configuration=None):
    result=_R97_PARENT(observation,configuration)
    try:
        player=int(observation['player']);step=int(observation['step'])
        if player not in _R97_LAST or step<=_R97_LAST[player]:
            _R97_REPORT.update(supply_guard_changes=0,supply_grain_protected=0,supply_buy_units=0,supply_early_changes=0,supply_early_units=0,supply_prefund_changes=0,supply_prefund_units=0,supply_slot_declines=0,supply_capacity_declines=0,supply_budget_declines=0,supply_errors=0)
        _R97_LAST[player]=step
        if configuration is None or all(configuration.get(k,v)==v for k,v in [('boardSize',10),('turnsPerDay',24),('shedCapacity',100),('maxMarketOrdersPerTurn',10),('farmHandCostMult',1)]):result=_r97_supply(observation,result)
    except Exception:_R97_REPORT['supply_errors']=_R97_REPORT.get('supply_errors',0)+1
    _R97_REPORT.update(getattr(_R97_PARENT,'telemetry',{}))
    return result

agent.telemetry=_R97_REPORT
agent=globals().pop('agent')


# ---------------------------------------------------------------------------
# v9 COURIER: deliver premium cargo before midnight and sell it the same day.
#
# Roughly 40% of the tape's strawberries and milk are still in workers' hands
# when the day ends; the engine drops them into the shed *after* the market,
# so every sibling of this policy sells them the next morning.  No town draw
# happens between hour 20 and the next dawn's market, so an evening sale gets
# the morning's quote a day earlier than a rival who waits for the auto-drop.
#
# From hour V9_COURIER_FROM_HOUR, a tape worker carrying premium goods whose
# every remaining command today is a PASS or a move (moves are free: workers
# respawn at the shed at dawn) walks to the nearest shed-access tile, drops,
# and the delivered units are offered in the first market slot.
# ---------------------------------------------------------------------------
V9_COURIER_ITEMS = ("STRAWBERRY", "MILK", "WOOL", "MELON")
V9_COURIER_FROM_HOUR = 12
_V9_COURIER_ACCESS = ((4, 4), (5, 4), (4, 5), (5, 5))
_V9_COURIER_IDLE = frozenset({"PASS", "NORTH", "SOUTH", "EAST", "WEST", "DROP"})
_V9_COURIER = {}
_V9_COURIER_REPORT = dict(courier_trips=0, courier_units=0, courier_errors=0)


def _v9_courier_walk(pos, target):
    x, y = pos
    tx, ty = target
    return ([["EAST"]] * max(0, tx - x) + [["WEST"]] * max(0, x - tx)
            + [["SOUTH"]] * max(0, ty - y) + [["NORTH"]] * max(0, y - ty))


def _v9_courier_plan(tape, unit, pos, commands, step, end):
    """Walk-and-drop route for an idle tape worker, or None if it has work left today."""
    if commands[unit] and commands[unit][0] not in _V9_COURIER_IDLE:
        return None
    for t in range(step + 1, end + 1):
        a = tape[t] if t < len(tape) else {}
        units = [a.get("farmer") or ["PASS"]] + list(a.get("hands") or [])
        command = units[unit] if unit < len(units) else ["PASS"]
        if command and command[0] not in _V9_COURIER_IDLE:
            return None
    target = min(_V9_COURIER_ACCESS, key=lambda a: abs(a[0] - pos[0]) + abs(a[1] - pos[1]))
    walk = _v9_courier_walk(pos, target)
    return walk + [["DROP"]] if len(walk) <= end - step else None


def _v9_courier(obs, action, st):
    step = int(obs["step"])
    player = int(obs["player"])
    if step >= 718 or step % 24 < V9_COURIER_FROM_HOUR:
        return action
    day = step // 24
    if st.get("day") != day:
        st["day"] = day
        st["plans"] = {}
    native = _IMPL.chassis.players.get(player)
    if not native or native.get("route") not in _IMPL.chassis.routes:
        return action
    tape = _IMPL.chassis.routes[native["route"]]
    farm = obs["farms"][player]
    positions = [tuple(farm["farmer"])] + [tuple(p) for p in farm["hands"]]
    inventories = obs["private"]["inventories"]
    commands = [list(action.get("farmer") or ["PASS"])] + [list(c) for c in (action.get("hands") or [])]
    commands += [["PASS"]] * (len(positions) - len(commands))
    end = day * 24 + 23
    plans = st["plans"]
    # Only tape workers: overlay-dedicated hands are appended after the tape's crew.
    crew = 1 + max(len(tape[t].get("hands") or []) for t in range(day * 24, min(len(tape), end + 1)))
    delivered = {}
    changed = False
    for unit, pos in enumerate(positions[:crew]):
        inventory = inventories[unit] if unit < len(inventories) else {}
        cargo = {k: int(v) for k, v in inventory.items() if k in V9_COURIER_ITEMS and int(v) > 0}
        plan = plans.get(unit)
        if plan is None:
            if not cargo or native.get("pending", {}).get(unit):
                continue
            route = _v9_courier_plan(tape, unit, pos, commands, step, end)
            if route is None:
                continue
            plan = plans[unit] = {"route": route, "start": step}
            _V9_COURIER_REPORT["courier_trips"] += 1
        index = step - plan["start"]
        if index >= len(plan["route"]):
            continue
        command = plan["route"][index]
        if command == ["DROP"]:
            if pos not in _V9_COURIER_ACCESS:
                plans[unit] = {"route": [], "start": step}
                continue
            for item, n in cargo.items():
                delivered[item] = delivered.get(item, 0) + n
        commands[unit] = command
        changed = True
    if not changed:
        return action
    result = dict(action)
    result["farmer"], result["hands"] = commands[0], commands[1:]
    if delivered:
        market = [list(o) for o in action.get("market") or []]
        prices = obs["market"]["prices"]
        for item, n in sorted(delivered.items(), key=lambda kv: -int(prices.get(kv[0], 0)) * kv[1]):
            if int(prices.get(item, 0)) < 2:
                continue
            existing = next((o for o in market if o and o[0] == "SELL" and len(o) >= 3 and o[1] == item), None)
            if existing is not None:
                existing[2] = int(existing[2]) + n
                market.remove(existing)
                market.insert(0, existing)
            elif len(market) < MAX_ORDERS:
                market.insert(0, ["SELL", item, n])
            _V9_COURIER_REPORT["courier_units"] += n
        result["market"] = market
    return result


_V9_COURIER_PARENT = agent


def agent(observation, configuration=None):
    player, step = int(observation["player"]), int(observation["step"])
    st = _V9_COURIER.get(player)
    if st is None or step <= st["step"]:
        st = _V9_COURIER[player] = {"step": -1}
        if step == 0:
            _V9_COURIER_REPORT.update(courier_trips=0, courier_units=0, courier_errors=0)
    st["step"] = step
    action = _V9_COURIER_PARENT(observation, configuration)
    try:
        return _v9_courier(observation, action, st)
    except Exception:
        _V9_COURIER_REPORT["courier_errors"] += 1
        return action


agent.telemetry = _V9_COURIER_REPORT
agent = globals().pop("agent")


# ---------------------------------------------------------------------------
# v9 CARROT: plant carrots instead of wheat when the carrot book pays for it.
#
# The tape replants wheat on the same short cycle a carrot needs (water daily,
# harvest at age 2-4), so the swap keeps every worker's schedule intact.  A
# watered wheat plant yields 4 and a carrot 3, for $10 more seed, so the swap
# only pays once the carrot quote clears V9_CARROT_RATIO x the wheat quote --
# which pet cafes and farmers markets make happen by draining the hinge book.
# Wheat is also feed, so the swap stops while the shed holds less than
# V9_CARROT_WHEAT_RESERVE wheat.
# ---------------------------------------------------------------------------
V9_CARROT_RATIO = 1.8
V9_CARROT_FIRST_DAY = 10
V9_CARROT_LAST_DAY = 23
V9_CARROT_WHEAT_RESERVE = 40
V9_CARROT_BOOM_RATIO = 3.5   # from this ratio the feed reserve is bought instead of grown
V9_CARROT_BOOM_RESERVE = 10
_V9_CARROT_REPORT = dict(carrot_swaps=0, carrot_seed_swaps=0, carrot_errors=0)


def _v9_carrot(obs, action, st):
    step = int(obs["step"])
    day = step // 24
    prices = obs["market"]["prices"]
    private = obs["private"]
    commands = [list(action.get("farmer") or ["PASS"])] + [list(c) for c in (action.get("hands") or [])]
    market = [list(o) for o in action.get("market") or []]
    changed = False
    if st.get("tiles"):
        # swapped carrots die at the start of age 4, but the wheat tape may harvest at age 4:
        # harvest them on the age-3 watering visit instead
        _farm = obs["farms"][int(obs["player"])]
        _pos = [_farm["farmer"]] + list(_farm["hands"])
        for _i, c in enumerate(commands[:len(_pos)]):
            if c != ["WATER"]:
                continue
            _p = tuple(_pos[_i])
            if st["tiles"].get(_p) != day - 3:
                continue
            _t = _farm["tiles"][_p[1]][_p[0]]
            if isinstance(_t, dict) and _t.get("crop") == "CARROT" and int(_t.get("planted_day", -9)) == day - 3 and int(_t.get("yield_units", 0)) > 0:
                commands[_i] = ["HARVEST"]
                changed = True
                _V9_CARROT_REPORT["carrot_rescues"] = _V9_CARROT_REPORT.get("carrot_rescues", 0) + 1
    wheat_held = int(private["shed"].get("WHEAT", 0)) + sum(int(i.get("WHEAT", 0)) for i in private["inventories"])
    ratio = int(prices.get("CARROT", 0)) / max(1, int(prices.get("WHEAT", 99)))
    boom = ratio >= V9_CARROT_BOOM_RATIO
    reserve = V9_CARROT_BOOM_RESERVE if boom else V9_CARROT_WHEAT_RESERVE
    if boom and V9_CARROT_FIRST_DAY <= day <= V9_CARROT_LAST_DAY and wheat_held < V9_CARROT_WHEAT_RESERVE:
        # Carrots are worth several wheat each: buy the feed the swap no longer grows.
        topup = V9_CARROT_WHEAT_RESERVE - wheat_held
        budget = float(obs["farms"][int(obs["player"])]["money"]) - 1500
        qty = min(topup, int(budget // max(1, int(prices.get("WHEAT", 99)) + 5)))
        if qty > 0 and len(market) < MAX_ORDERS and not any(o[:2] == ["BUY_PRODUCT", "WHEAT"] for o in market if len(o) >= 2):
            market.append(["BUY_PRODUCT", "WHEAT", qty])
            changed = True
    if (V9_CARROT_FIRST_DAY <= day <= V9_CARROT_LAST_DAY and wheat_held >= reserve
            and ratio >= V9_CARROT_RATIO):
        carrot_seeds = int(private["seeds"].get("CARROT", 0)) - sum(1 for c in commands if c[:2] == ["PLANT", "CARROT"])
        _farm = obs["farms"][int(obs["player"])]
        _pos = [_farm["farmer"]] + list(_farm["hands"])
        for _i, c in enumerate(commands):
            if c[:2] == ["PLANT", "WHEAT"] and carrot_seeds > 0:
                c[1] = "CARROT"
                carrot_seeds -= 1
                changed = st["swapped"] = True
                _V9_CARROT_REPORT["carrot_swaps"] += 1
                if _i < len(_pos):
                    st.setdefault("tiles", {})[tuple(_pos[_i])] = day
        for o in market:
            if len(o) >= 3 and o[:2] == ["BUY_SEED", "WHEAT"]:
                o[1] = "CARROT"
                changed = st["swapped"] = True
                _V9_CARROT_REPORT["carrot_seed_swaps"] += int(o[2])
    result = dict(action)
    result["farmer"], result["hands"], result["market"] = commands[0], commands[1:], market
    if st.get("swapped") and day < 24:
        # Swapped carrots have no planned sale on the tape before its own carrot days.
        stock = projected_shed(result, FarmView(obs)).get("CARROT", 0)
        selling = sum(int(o[2]) for o in market if len(o) >= 3 and o[:2] == ["SELL", "CARROT"])
        if stock > selling and len(market) < MAX_ORDERS and int(prices.get("CARROT", 0)) >= 2:
            market.insert(0, ["SELL", "CARROT", stock - selling])
            changed = True
    return result if changed else action


_V9_CARROT = {}


_V9_CARROT_PARENT = agent


def agent(observation, configuration=None):
    player, step = int(observation["player"]), int(observation["step"])
    st = _V9_CARROT.get(player)
    if st is None or step <= st["step"]:
        st = _V9_CARROT[player] = {"step": -1}
        if step == 0:
            _V9_CARROT_REPORT.update(carrot_swaps=0, carrot_seed_swaps=0, carrot_errors=0)
    st["step"] = step
    action = _V9_CARROT_PARENT(observation, configuration)
    try:
        return _v9_carrot(observation, action, st)
    except Exception:
        _V9_CARROT_REPORT["carrot_errors"] += 1
        return action


agent.telemetry = _V9_CARROT_REPORT
agent = globals().pop("agent")


# ---------------------------------------------------------------------------
# v9 HERD: raise the tape's day-10 geese as sheep or cows when the draw pays.
#
# A cared goose lays 2 eggs a day into a $50 book; a cared sheep grows 4 wool
# every 3 days into a $200 book, a cow 3 milk every 2 days into a $160 book.
# The tape handles its geese exactly like pasture animals (build, pick up,
# place, feed, care, collect fertilizer, harvest), so swapping the species at
# the first goose purchase keeps every worker's schedule.  Wool needs a yarn
# store to hold its price and milk needs pizza / ice cream / smoothie shops;
# egg shops keep the geese.  The swapped herd's extra product has no planned
# sale on the tape, so anything beyond the tape's remaining planned sales is
# sold as it reaches the shed.
# ---------------------------------------------------------------------------
V9_HERD_MIN_WOOL = 150         # wool quote needed to swap to sheep
V9_HERD_MIN_MILK = 150         # milk quote needed to swap to cows
V9_HERD_MAX_EGG_SHOPS = 1         # sheep swap: at most this many BAKERY + BRUNCH_SPOT
V9_HERD_MAX_EGG_SHOPS_COW = 0  # cow swap: at most this many
V9_HERD_MIN_MILK_SHOPS = 3      # cow swap: at least this many PIZZA / ICE_CREAM / SMOOTHIE
_V9_HERD_PRODUCT = {"SHEEP": "WOOL", "COW": "MILK"}
_V9_HERD = {}
_V9_HERD_REPORT = dict(herd_species="", herd_rewrites=0, herd_extra_sold=0, herd_errors=0)


def _v9_herd_choose(obs):
    shops = obs["town"]["unlocked_shops"]
    prices = obs["market"]["prices"]
    egg_shops = sum(s in ("BAKERY", "BRUNCH_SPOT") for s in shops)
    if (egg_shops <= V9_HERD_MAX_EGG_SHOPS and "YARN_STORE" in shops
            and int(prices.get("WOOL", 0)) >= V9_HERD_MIN_WOOL):
        return "SHEEP"
    milk_shops = sum(s in ("PIZZA_SHOP", "ICE_CREAM_SHOP", "SMOOTHIE_SHOP") for s in shops)
    if (egg_shops <= V9_HERD_MAX_EGG_SHOPS_COW and milk_shops >= V9_HERD_MIN_MILK_SHOPS
            and int(prices.get("MILK", 0)) >= V9_HERD_MIN_MILK):
        return "COW"
    return None


def _v9_herd(obs, action, st):
    step = int(obs["step"])
    orders = action.get("market") or []
    if st.get("species") is None and not st.get("decided"):
        if step >= 216 and any(len(o) >= 2 and o[:2] == ["BUY_ANIMAL", "GOOSE"] for o in orders):
            st["decided"] = True
            st["species"] = _v9_herd_choose(obs)
            _V9_HERD_REPORT["herd_species"] = st["species"] or ""
    species = st.get("species")
    if not species:
        return action
    product = _V9_HERD_PRODUCT[species]
    commands = [list(action.get("farmer") or ["PASS"])] + [list(c) for c in (action.get("hands") or [])]
    market = [list(o) for o in orders]
    for c in commands:
        if c and c[0] == "BUILD_COOP":
            c[0] = "BUILD_PASTURE"
            _V9_HERD_REPORT["herd_rewrites"] += 1
        elif len(c) >= 2 and c[0] in ("PICKUP", "PLACE") and c[1] == "GOOSE":
            c[1] = species
            _V9_HERD_REPORT["herd_rewrites"] += 1
    rewritten = []
    for o in market:
        if len(o) >= 3 and o[:2] == ["BUY_ANIMAL", "GOOSE"]:
            rewritten.append(["BUY_ANIMAL", species, o[2]])
        elif len(o) >= 2 and o[:2] == ["SELL", "EGG"] and not any(isinstance(t_, dict) and t_.get("animal") == "GOOSE" for r_ in obs["farms"][int(obs["player"])]["tiles"] for t_ in r_):
            continue
        else:
            rewritten.append(o)
    result = dict(action)
    result["farmer"], result["hands"], result["market"] = commands[0], commands[1:], rewritten
    player = int(obs["player"])
    native = _IMPL.chassis.players.get(player)
    if native and native.get("route") in _IMPL.chassis.routes and step < 718:
        stock = projected_shed(result, FarmView(obs)).get(product, 0)
        selling = sum(int(o[2]) for o in rewritten if len(o) >= 3 and o[:2] == ["SELL", product])
        planned = _IMPL.chassis.future_sells(native["route"], product, step + 1)
        extra = stock - selling - planned
        if extra > 0 and len(rewritten) < MAX_ORDERS and int(obs["market"]["prices"].get(product, 0)) >= 2:
            rewritten.insert(0, ["SELL", product, extra])
            _V9_HERD_REPORT["herd_extra_sold"] += extra
    return result


_V9_HERD_PARENT = agent


def agent(observation, configuration=None):
    player, step = int(observation["player"]), int(observation["step"])
    st = _V9_HERD.get(player)
    if st is None or step <= st["step"]:
        st = _V9_HERD[player] = {"step": -1}
        if step == 0:
            _V9_HERD_REPORT.update(herd_species="", herd_rewrites=0, herd_extra_sold=0, herd_errors=0)
    st["step"] = step
    action = _V9_HERD_PARENT(observation, configuration)
    try:
        return _v9_herd(observation, action, st)
    except Exception:
        _V9_HERD_REPORT["herd_errors"] += 1
        return action


agent.telemetry = _V9_HERD_REPORT
agent = globals().pop("agent")


# ---------------------------------------------------------------------------
# v9 FERT: spend carried fertilizer on young wheat and carrots.
#
# Workers that tend animals carry collected fertilizer back to the shed, where
# the tape sells it into a book that falls from $55 on day 14 to $10 by day 27.
# On a short crop the same unit is worth far more: a watered wheat plant ends at
# 4 units, but fertilized for its yield window it caps at 6.  A worker that
# carries fertilizer and is about to water a wheat or carrot plant one day
# after planting (watered on planting day, not yet fertilized) fertilizes it
# instead; the tape waters it again on the following days.  Fertilizer the
# worker's own tape commands still spend today is left alone, and the layer only
# acts from day 16, once the fertilizer book is worth less than two wheat.
# ---------------------------------------------------------------------------
V9_FERT_CROPS = ("WHEAT", "CARROT")
V9_FERT_AGES = (1,)
V9_FERT_FIRST_DAY = 16
_V9_FERT_REPORT = dict(fert_applied=0, fert_errors=0)


def _v9_fert(obs, action):
    step = int(obs["step"])
    day = step // 24
    if day < V9_FERT_FIRST_DAY or step >= 700:
        return action
    player = int(obs["player"])
    farm = obs["farms"][player]
    positions = [tuple(farm["farmer"])] + [tuple(p) for p in farm["hands"]]
    inventories = obs["private"]["inventories"]
    commands = [list(action.get("farmer") or ["PASS"])] + [list(c) for c in (action.get("hands") or [])]
    changed = False
    native = _IMPL.chassis.players.get(player)
    tape = _IMPL.chassis.routes.get(native.get("route")) if native else None
    planned = {}
    if tape is not None:
        # fertilizer this worker's own tape commands still spend today
        for t in range(step, min(len(tape), day * 24 + 24)):
            a = tape[t] or {}
            for u, c in enumerate([a.get("farmer") or ["PASS"]] + list(a.get("hands") or [])):
                if c and c[0] == "FERTILIZE":
                    planned[u] = planned.get(u, 0) + 1
    carried = {}
    targeted = set()
    for unit, command in enumerate(commands[:len(positions)]):
        if not command or command[0] != "WATER":
            continue
        x, y = positions[unit]
        tile = farm["tiles"][y][x]
        if not (isinstance(tile, dict) and tile.get("kind") == "PLANT" and tile.get("crop") in V9_FERT_CROPS):
            continue
        if (day - int(tile["planted_day"])) not in V9_FERT_AGES or tile.get("watered_today"):
            continue
        if int(tile.get("consecutive_unwatered", 1)) != 0 or int(tile.get("fertilized_until_day", -1)) >= day:
            continue
        have = carried.setdefault(unit, int((inventories[unit] if unit < len(inventories) else {}).get("FERTILIZER", 0))
                                  - planned.get(unit, 0))
        if have <= 0 or (x, y) in targeted:
            continue
        commands[unit] = ["FERTILIZE"]
        carried[unit] = have - 1
        targeted.add((x, y))
        changed = True
        _V9_FERT_REPORT["fert_applied"] += 1
    if not changed:
        return action
    result = dict(action)
    result["farmer"], result["hands"] = commands[0], commands[1:]
    return result


_V9_FERT_PARENT = agent


def agent(observation, configuration=None):
    if int(observation["step"]) == 0:
        _V9_FERT_REPORT.update(fert_applied=0, fert_errors=0)
    action = _V9_FERT_PARENT(observation, configuration)
    try:
        return _v9_fert(observation, action)
    except Exception:
        _V9_FERT_REPORT["fert_errors"] += 1
        return action


agent.telemetry = _V9_FERT_REPORT
agent = globals().pop("agent")


# ---------------------------------------------------------------------------
# v9 OPENING: a cash-safe step-0 wheat trade.
#
# Every route tape opens with a wheat round trip
#     step 0: BUY 13, BUY 30, SELL 30      step 1: SELL 13, BUY 5   (net +5)
# and then runs days 0-9 with only ~$6 of cash slack (minimum at step 32).
# The round trip wins cash from rivals whose own opening buys into it, but
# against openings that dump wheat in the same slots (e.g. BUY 43 / SELL 20 /
# SELL 22 or BUY 30 / SELL all) it ends step 1 up to $75 short; the day-1
# wheat and hire orders then fail, the herd goes unfed, and by days 5-8 the
# strawberry seed orders fail too (18-21 plants instead of 33, -20k..-65k).
#
# Replacing it with BUY 10, SELL 5 at step 0 (still net +5, nothing at
# step 1) leaves >= $1,050 after step 1 against all 6,648 recorded openings
# in the metav2 / M&M replays (exact market simulation, build/v9/opensim.py),
# and $2 more than the round trip against the V38/V39 tape lineage.
# ---------------------------------------------------------------------------
V9_OPENING_STEP0 = (("BUY_PRODUCT", "WHEAT", 20), ("SELL", "WHEAT", 15))
V9_OPENING_TAPE = ((("BUY_PRODUCT", "WHEAT", 13), ("BUY_PRODUCT", "WHEAT", 30), ("SELL", "WHEAT", 30)),
                   (("SELL", "WHEAT", 13), ("BUY_PRODUCT", "WHEAT", 5)))


def _v9_opening(obs, action):
    step = int(obs["step"])
    if step > 1:
        return action
    native = _IMPL.chassis.players.get(int(obs["player"]))
    if not native or native.get("route") not in _IMPL.chassis.routes:
        return action
    market = [list(o) for o in action.get("market") or []]
    wheat = [o for o in market if len(o) >= 3 and o[0] in ("BUY_PRODUCT", "SELL") and o[1] == "WHEAT"]
    if tuple((o[0], o[1], int(o[2])) for o in wheat) != V9_OPENING_TAPE[step]:
        return action  # the tape's opening was changed upstream; leave it alone
    rest = [o for o in market if o not in wheat]
    result = dict(action)
    result["market"] = ([list(o) for o in V9_OPENING_STEP0] if step == 0 else []) + rest
    return result


_V9_OPENING_PARENT = agent


def agent(observation, configuration=None):
    action = _V9_OPENING_PARENT(observation, configuration)
    try:
        return _v9_opening(observation, action)
    except Exception:
        return action


agent = globals().pop("agent")




# ---------------------------------------------------------------------------
# v9/2 PREDICT: forecast the rival's premium sales from a library of recorded
# streams and sell our planned lots just before theirs.
#
# Each turn the rival's executed sales are recovered exactly like RACE does
# (inventory delta + town draw - own sales).  Library streams with the same
# first two shops are scored against the rival's recovered sale ticks of the last
# 240 turns; when most of the best TOP streams sell >= K units of a product in the
# next two turns, our tape's planned sales of that product within H turns are
# sold now.
# ---------------------------------------------------------------------------
import json as _v92_json, os as _v92_os, zlib as _v92_zlib, base64 as _v92_b64
_V92_P_ITEMS = ("MILK", "WOOL", "STRAWBERRY", "EGG", "MELON")
_V92_P_USE = ('MILK', 'WOOL', 'STRAWBERRY')
_V92_P_H = 48
_V92_P_K = 4
_V92_P_TOP = 1
_V92_P_EVERY = 3
_V92_EP = None          # panel: current episode (library excludes same-parity episodes)
_V92_P_LIB = None
_V92_P = {}
_V92_P_REPORT = dict(pred_units=0, pred_fires=0, pred_errors=0)



_V92_P_BLOB = 'c-ri}TaPT;mL4>3F(V=~Dl021>#{F>&gs*qyN~<0+s3jH5Br5j_yb4?$(E3zL9{^_A*;dWB3qU%V`SXEAcW)x3;P9G2!SyYZ&)${o<KrEGD4un24RqZAHev&Z_J3utgKqK*4lfmqjs%b%AFY*88KsC#vGS#eB&qK*TbKSHO7)-`bn6+j>8wF#_|};6!E5}Qgaw<$e~O%)Q33iLmfj-A>Z0-9!egrbBSTxgc?JR_H7zcPBCu#kUKjk){u&w8B?{tE{rkPL#ioFi9d{X1^c1Bw-aJYX=8VcF^4=1A%!#y$$mfN5M#6h)|OgAw!a=1v0ve@gcR}BzJxNQp{9M8u43pzw3ZGfbR$l)tJ`gAw#I}SqW$Q~8dy@<*k2e!+TaRlySENW_B3c-u$JJ;gPnGptB%~KW3o4SGuRg?mh`2aY~5kM3Gry}_rcD;!NCv%pXDx0As_#O_qX-NFFe!V3B5Sh)Bd(A+;|70N3DBm%v(Ii(~jSDINy5O8eXD3u6Mlk@rE70QOA#QsG(TvG7m=ULhFAHNW?!I3hTLKXB3P;#Rw!laIK-Mb|l$z6zf(#xBb?xP&GtdC_N5fDC~){j|Lv3SmQZp_Cp()jBD;VAho1%z%W_2<sNOYR##33J9xK=b-+W}#IhFJr8<m;UCOQ-vrVFa@v-aR>#Njdd&LPAeP&HXdlF|^zQR==0~(GS#?-}R?X_iqsf~-<BgEXH4VamU^C7ak><Ru~AI2Sj_|?;q#DY0lJPEDq3x~7|_1c=5OUH$D;Cqd&z2WfIJsxS$Y@0_oVba?m+X=g#2TR;V4l-8)#yM(^+GIqx*)pj^+HCOXSY7M`UwGHHx+2FssoT&!xTMVm4CBTocGObD5KZ=`$8@kJ4qT9>El7K!goa@r)u>4k>?@t488Hp%s^BZ@WIJ=8LywDNUW{0ZSSoh!;#0$#Xjh0fX!iap_=+904hzq*^Z9Dmw~N#qN4qj-#GT#F8h;gsY)_%<+Z%gUeB0wb>=`?P1!GGzq2CK02c48T%g{XZ2!Dk>$4@rV2GPc1z-mV`b_LhBYucKyk&0MtVHa#tV9I=hzeO%!Jy}0nn+GhrYu-BH6(eF7_$KCW5=4gGWSG#0H@q+Ac))6~H{XQ#O-SF^$)SAnZGPlU|8n??vHMA=TRf$WcIq%tX>YG4DkJ9XHWYhgPIJuQDO+E4W6l$&aE&8}6q3r8&0X%gQj4|Sh8Am`(+u5iqS~%tBDa|6+@<12B4v*KwqR15=(xdLrrgsjCZi43A!n?SErh=f1&6X!erp%R&|B|eS>PbLu<++5>N78B59Qa4`r*AAyyMvv`w8vI*c>H9tety|NntbWxJ|u-+P^pP&Ie36Z!$I#PP)ljmC#K5cCc1y7Gun<5v9WqBm2R&$j(G>(r?o-s)bmQb~f&~qjV~m?>0D?!)g-OH6&Hfwnd09tTJ99QgY!juh<^0Z+11W{O^W8AG_Zks!g>`*x4yNNGTiqN(o|5pRRC!h@=VPDep6v1VjTRT1F>bm)hZaRegLjj};cAowh*_vD-`(a;$iT#6`$9USR|hrDT`1D$1b^rU|4>CBkGnHgR4V5>^Ad<G9(aA*#_Y)**P%%1wEj{3jS64CBV0sK<>sycCLPBz|H$W4g^06ebVYY|bNgc_|p4fJMT`Nff6PshB1cXTcVd5D#a&hs_8m5>w`cvbN;zU{e93gu5roUf#t-mo*9P4faDjy|7i(bOPtHHLOD7C(aa;9_iXT!K9YW*Qf{V{*LcTx9{ANI1Z5YO~n|vzuA#}=0f85uhoqXiyT^7;l9&$B{nDETT>Pw`zXe3drIhfZcNn7>@S7BZRQ1A5{AN>KiLtR%##EoHuJ(=ntKqXvh*-(16Q8ibC5p5t3fHOynDqhI?CihyDis%Jx(rKy{Ru$Nw^2G@ivNhOzIIPPN<|@QB$PQw!5L@6W&xR9i?wu4@L(1kt9XO4G2w2nt<F`Fh04A+Jn-jVAY{H7%*s6wgmFB<CuuV-qCSODilxlAaQVcgj+xyL*iH?Y~>X^2E>d_Iw)~?1hndKw(rcF&WQD)-R*|GnpQhb{v10F^soQbr|or2-+!kjg%#qO@f7Nn&sm$x%Y+RsurhV1Y1W~5PM&qBnx*RPI_@%@Zam_%wVo(YCk6{;7&{d+l+uuDXx7YyLEt9Lo(d~X7!EHdtR3H(Duit;X?^&d&2GhP2kb1X*@`pw)I@Sqnrt!cxoG;hOjw9~Q>mde<qgduYu}ah<4CE)U8QigLO<pMZYSHvF%vg9f)%#m?6#}+>_99P&epP;t%Z-%@neyq#QSVVj)HAR9p>^~rE)Z2E^TY_VKN=<iE=b8%8@l5oonhQc1fF|5fb~G<W`~G&D1V@`)QS<{x@DNVOQeS)cqsP<p_xxGdI(nX^^yfT_J*2u%k|4dwZfjO}jSPJf#keZOBZbM61`0xSdUE&O{DTg$R}c%58BE^+}h9csEmJ;0B#chTx;rbc}q?vPr22<FzYL!6U_%{kw|V(9`u4IpDYf2M0!6PwhE3ONuiQ^QGgyS@^toL`v<bA5#8ejEkFK6STKvy>VktGeqj0xg3+}BeA#!Zwtcq)M=nL1Q8F_2e#o6V(Z8iNejvz6RLu>(*(5XiP)v=I=^`$XugV2gDwtW3XmFWuZNAHb#`s`+InY%puzT0U>`|on$7XJtF*;o5c_VJ7e9#I5<8#^7m6F3`UN9J_k`^7obS2)(G>!%3cCPDr)G^UOm7S<R6r^UkO<HnOAa#4VYg97*mBFJ<dX7*xztNyCYLofJN8A&@$5rMRKPGz>_M`7QZRS8!D{faOBM<&S_-^-6N`nLPL#7ILR;-;tBuBhWaynNc+;RZY_7yXGuiNbkO$TSc89QmR-UA0LZVRvHSO7!$So&Gq+JG$+0ML@k=x`B_285JkrpTf^v0e``=iMnOemK-FmFEX&iL!5oo^15HQ$fJ!v)veWP-*f%a2S2i!_B}d7#|6LT}sTH3MYoIp(m(x#ZZ#vHd}%%A8FbsB-c2Tb!`Pbij$l)r94Q2}8QA=&+ieTzsH?T=`q5cGxSqHKge}>VgAIB>w7XQb`Vpz>Amy=+fluFE<km)7-`$E-mPcww+d6zK`u&lPtDj5BLh^JC2*eXfq400B&lz-ec#2Kk5hpQUA|xO+Y+x=ujDfn1JW%)MaPiZlRaqx3!|}!&6CdNez(@uM!rtbs#SaJ$R-0?w}FG7|!Gcx<}5m6L~>J6aAN56M@c3U7&|}b^%c&AQtI>F^4R+g-u($xmq!vk=D<KYj4mVk=^@8S@16D(3BKwu+4}q%nwc&*wpqI)J^1^!rVX~cHDiaXIZnc-QcnNSbSzd55nJ-d<M9}A#sPbiEKYdv(qiad7?`SGbl@HP$b>bm*A>Omu@3ns6`HA6B&W33g#E}X*A;#s?@pre?H1NSvis4%Q=}&Jd^bUJd^3vCz)U8kQ`3Dk?D2b$nq|4WZ(7z>RlJSkyDuC2k-Dk@+s(w%<x`!m%Nctngid!1tMSbD}0jml24L-j;@5xy<LR(nBL1X$sJI?^=bQ4;F<grFDl>Xv8wz)StjNCiPl#43OR+k!LEeCq`qcyDtEM|3p_x}<V`qODJmE&i3j+$sP*j8b2yFq4yGzJSgxDF=B5dYB<UlCYd5*kXIjjJGclp+1bJOC6R{g#wfSYEQ98*}Ts#jhpzT*3XG9qwQcZWa1vF6w8(_Yrt=+MQ7s~ECQD1~F6fQ^WuRvun4|k?LE0RSu3KxRAQ`-PUIzw8p5cW_<?fQsnZK!`2C~nrO393iPfBJQU^TaHAs!vn6D5BU=vP4Q2Tea}o&SE9|uyj~D)_?d=la>|-_A1J8Lq8Pla_${i*X$5T4fsui?=OQ%ejJoqG3c@b6l*9Kg<`^kinw>7(%E%wv+FSza!+>+1%Zi*t4bdq;$6_r>>`M2!FGcztLk;`6wv1pNQ9H%WVPoEeY<1e3=fs=xCpUZ^<g_<N#_=L9Ic`IOku}OM|;o}F2-OO++j9t^Y44DTKP*<No-0{r!+Imer@AD-G>c&4d$kt5~fIvoRouR`91XxcabDpYxN;La=*Y1eCP2-1oy6Z&ZziQ+PK)a^U>=!QVs82JJ?F-**v*(hsD4%sX<cbd%zW-?HzFl;#XII`-F}mde0dNg!OFd!&nfj%(>VMnxio3*Iv~_H)g5iQJy~=PMgP%SR=K=Jnp90cl?NnWhx%DP=1VEg}0Jk5lpXcw8;Z+Wsi;s){x9y3o9hUvuxAOmZV*zqdTByH`g7uxUS&0ht9v<42VJ43Am9>4s49}5q9awTgMGt_C2>^1Z8keuq#YA2#fSEu(-K#UoBS%`t<g|drW#>2gfTtseOkHhsRUjr=CH1>q^A;u^epm=EEQDgL_C3I|xM%%J$~$_}j-1`}o$M-}T409)9cL-x?p^y5g;qKhMYX?R-oh@bmgU-`4M>*&qAyQw&pjo28$qW9zqfqx#md@AKR8;>Y*;?cYBgo8m`(OyAPS`s$B_nJHT3AJ?rK_;LO=zQ@Ot_wiNl3!P4haWlSo&1)$2g@YHref~9FekJ%VG}s7_^Hrz{z0tSxd;TfT);^~5KSpHYjI8#%ASiP!By|wNb4&{A=Be}8Q=%gav7IjFfsRn%atP~*`a={U3gZ(M`t=A-Ztt0LfauWtm;6uIljX0p<8)r*%^340o}APEJj|4y`If=*`GO&>Pp0FxKJ(k$uKc96M3^q1*G$Z$Fk1>su|pV*0EQ&yOMgLNcE^OCH4NdQc=}NOAgwWB-LU?=L(W>&Zc1eDYRIyp2+y@JwicfD^9=Zn0>GZN^SO`1Y4<L-P9CU0NJ)`uyJpYGC>JRlv?qU9`04?^0q(3FggnVJICnY1MpAfcL7jg4n%Ae-^w;4Xzlz>(Pfm!d%bq^b{01!_eHZWtjOPz~;iez_jAuVA?{VdePq%)J^LVXZmkU09y5anY{`@DaBRZJUd?c-}`ShGvmgDjCoY<QBwDIXu`{$>)^lf@!WarU;=ao-R=%4M?=dQCpes;oo?65Q>g34*9rAuACI^yljeozh8>W*!VD_WVBSN@&E5q~d&R3%P74)qc4?^5D$2N2c`eEM+fBl?vY?|wis%Kb#WkMXe5r+JA_$HZ_TH_T(G#4R6`^YD;-V|xhqAw7h=e}us9AJO~`15n3@Ae2XZn77}2e^1Z{)sqe5c#xw#9QStkd$#2gUxnjCE|2*KcH|)yk6E;D=Rct*iBC;Lz<m7>w7UX9TM+b(#JvCTNVJW$@UMlx8mC`Y*o1$#jB?#$Do;_bL7Em~tg%d~eD8)a5e4uH8*&uLhmlIXeu2nOJu>imP^gcuU6=?buh;D-gmUbw&Ot=g%$t1-*EGwA!|Jr;AQICP>KJ!`oC^`iv1+flc+$bNXEvAr8-1&4$xjT_U3*lIvDZ>tlHfpf=lh{NvJ)QXHkj6Oc1^TOo2_@0qW#BEzIW?C8K_;|wk|4sIy>_7Hnqo6H}l0CQiHgL>sz6V{Z$Ry>rL{HKX@d%!4B?M9VKvj6#f|}{A>X>1Pd!Fai*bpsq~lYFlOLN%Rg<aWh$}GtK}Gn4(r5*9b;Zf?KzSq54V7C-ap0(a|`K@O5y;t>LJBl_!$D(sT<_)AA~APKUV@UIGYfs`~#bj*Mx?phC6%ETIN^ww<T_#oyk+Iv-s^nk``mA^DCi0j#(ZMOWg{lz+F%Q%deGW#J|WNcr3FWN6JafKjeLprHC{QHe&)bq=(ANBm2C+%|c@^lP&ju@IzyVSo<Te6cOO;YrsAcI~-z{b6=98ncc{!-k1*^L(@a*OP(?#f(73qa5$K<#_4Onnqrp}x?`Zu`mHeN*zwHDSY67K4sK#!3&VSWBOo50kPs`}*3|jIj)^dRWk7K-%{^~%5tEaMpBF&x7-dXzpb^nQ{1DB<!3hD&)K9qn#v~QL>ara~3Qk`EK<@AqVUP0zu|xUrmuyCM*RlS9^BMSm01ixG=MIx{LQ)t6p&2Msm(wlRHS^UZS&{iQ#C}UCU|~|t2DrqbXxnB&R%A|=rZ0f{Oe<0XnnW^XDt9tsEr9LKK#WY(*NJc5XmUsmJs@KP*+B#)+nJ?v%^tp+Bn+l<!6eI(2xULnRA#Fwkty+-_8^G4GS7zcq2teY+%&2hKQet)DNmgZKEBmgu-8U_%Qpm~OvJGblhAAc8)agwqJVmY6y-5HLXf$5Ca%ktIW9R9QG$!}BJ92D7s1baqS%L^1RALzJN3gr44*Q!3Q>G8+t8l$HylP{>*woN1MF{~L1tfLnobvCY6AgkKxhFPBP7ZAT*Ak}v1qVf(-{ygPg{qe5n!n#^}N{<Ns=1!jCntOj~n%ZonhlbN=KiTe2zM&9u@4IgQsz1<O1+gO6H&}hcsmt9YJ9GmSV)LI$VG`gK-9s(KPQpeS~5#Hr$xCa3oIpI>?~^Du!Ldhb6~{(L^nd&#gO6F<>2QSfvkbfH@gXVPPvQ*SC!c`zOM$BKfb3xqKh#X_!D?*+)XJ9;1?c%g@<lvOnbonR=GLz7-S%_^sU?PcAJ<*&gVSi(?(_NI5WNa5yp}NUPlr+I%`Dg3y_9nlR?Odrvgq&^q57bMaI~9I;#5MLhj7XHy_G@9fMy&)hI^0mE{KTicuI9^j9JMk;v`LYUYX2*b@I-tVEN=IIvVV><HWzx}DR95NXP5{2~ZvK$h#9O`M7!??<F$XtX^Qye<neSs`P0V8C}`ruI(LvVnn{ak4cGio`XqLyVO(07O>gp-xoU{~%OxV#VwoTN2eMlILVoQ86i(;)P$?aRZGgPw?En-d!P(}adW2@N+)yjf*42%nv=T&=xn2@S(@2@N1Jz^>GC8X7wJ>Qm!4|3d73$@CsdlMTo>;u!E`Kq*4J<dJi8OO)^tjY<coEm%K2w&iQv>2b8wO4<meA!A;Ls<d1r(#8_n%JjZurZBS13wHsSb`!q^`Y9mCnGivxZBkZp*<+?*6Dc(Cl=j5C*vM>|uC+=!NAmZ9?Wb5~j<DH;n5u+tVlfXprtw1iMKgMyLw*rcTm0ihlh$UXt^n_rpzc>uS-_+0MMn=Jk&#-AQc~HBo`1*-MFJmmlc@Y?>NTT8VWL*-$<*c7PL%y24ttutP1BzWMMfpa@v+=LU<(I~k_{h@?C*Qbzx(EnEe}jbEBO}=f$5O|9^;7Zo>%k}Q<wUkM?OlC!Y&IJI;SnKAKhXb?EG6y=*^<qH#?U}vbJ)68_Z!nP&phyQo^s|BeE#-542kXhldyW!=N*Loqxvx-)xnTZp(@$ApVB@rPyUAu20NP5E(Se8Nvm#K!dy&XZhh@Uey2Z!NE}Ou>a6Trh=*-Wnf|aGT0uBn;~1rBrxps?gs!@-XWbQ4SUMZ9v1xdjWXtAo|}+?=H5E*3TH1f>tHy0dOgx6ZIlj!1Gjs-9kX?I1JnX2Z&&EiEpsO#AgA)mQqF^<B;7FGu59@%M65q%W*d>^1`76oH<Mt=_I^}OJT6=H+mTb#DHq_&X({(ysEykJ$G5n94}>R0fX=y&NR{-IKS+x7U;7rfjp^s!r6tnMaFQ;3wzH9{!S*z%-mWNe?f`Y%#T{V1N_sz`)48lG5_JqJ8&7XZYeJ(kP*?1bb&x$97>O;m;~`za^J0{?N0X00%b_I!_uRo|bulr!WSrA&xHqEV9a9|=jV|sRqxL0g-7=6%cKU+I44RIqA~`kgjfgA5D?~GhxeAIVC|!YJ4FFEv=pIQOl;_+};pMf5>W&03v)jQSV)r@@QIF8cUuR=PZPOn1tFz<;k3WG2iP-j-&-O9fS37j(z}4^(dzyzN0CxWu&z&Fk_l!uKy@hvB%;3Ar2ZFo#^d=SUgfEpzag>5jiP4#Oft?G-#!dQ>%@c-WY-oNMk-ElRF%14R>5fAK6O>7yKaL_i2@%QLzyWtj<VF;>p6BhNRjGGa2~_C63gtn`xYzD3bwk%qzRh2<<0TH_L4h3;5cyF)MkWMB!n`}iTjOnt@}S`aT>lr2IRYXM$!t5~&)jMyGphH8-<xo3UbjyP$5s{{2*<DqpR$d)QFnoGOw>opF5(8-ILA1x)8I)(%GMX*n7GJ1Js`>Foew--PdUem@@dMPyW!~p^xl$ijDI7XC7>*;8<>;>Jyx5Xn+LMRQ2R7qyCPb^JO<xFWh0r>bH+RtnX5FDk7bz0As>JLvM+r>yYMUDksj&CHGwvDWiml`#~sPE)SrReLytn}h3OcF9d`6<TUS?MOaCiU_HUUXfb2Xbp&tTMEr3AZ+A|&GR>bQhBRWBDSL9ULIrvqU3NkUHAOp>B4{aKNsVzHZf~U@m%Fy%tky)zNUAxQ<%b_#j*&`o-W|$pM-AI(b$(bI>E`1-yj$hS;#2^sDz}6XWA-Hx}W?)~aC5gTWi8wWG{>u-^^`F`Co=a+Z;)+OIIkB75<-(kC)IH~rxJJ%LX)rM-OIi6O${ABib4zHN>K1zF)2*f@#33gZIdN;UiL~NHQR=t+6GJyMq9Bc<P|VMXo9IxOve-$g^Ga}Li~ELYhA}B$6CSF8DVrNAx7t8VXvB>z0a!9!pYD?H8+H|L#hB}N&k>$nc}8aCdib0?CtpR*rur+-PbDY*L-=jB$FV!!I?2g!iR7f-JegL=7sAX^UQ_N{mUoCd$Y4jJRHnrWtKsxKZMwztOyih$p;4W9ghlhN=XLTbFEc4oUg=fHv0G>xJBCg~y%n>RcjT~;tjg0gXVL=MID_l>OxDD<gH!tpTqquk9r&){575FaeI<ByaOBMG13M=<8;P8gS}{oomG+utx&>w?p<_f#=s!7n%BE&CJ2T03Oid!UH@(k#C4G8|y&{*~9aib>bK`-0K|66l^m#9g1ux#G_H%V3wg|khJq$~C6wKf1kEuG;tHCWMk3n4$Kw*b2IiQ^fQ)LW$NL8-yc*+>Wn?-Jd+fTTjz$x}0c{JerKJn{4I84el^B1W~OxSA5VG2_ZKZ+9W_Q7^#Ik2gY4mrE+%;s0P;VYx+n-0E3s0Z}T_!MJKmSiDRS=!N)T<-%VFVBPvy!qoD8dT6Fy+}2o{=v8?4F!a@RQC@mYPz2z5<bXKf-~1~heTiay%M?fY~!v~Bq!0aOcl!_ky1+dHz?q=o(eC;`||EtPU57cZzl1yPq{LsRSjrX*OV8Ny9`>pRE`o^I``t1!ur5$4bo`fT1|syb2cTl5{idKiTD6j6?g~1GmsJBGv$jmE&>J3ghjw4$P)_JjYup=Ttg8=M;cwXSOb6k!lXb9n;zZH?QkhRR7^?-;@8r(a8ZPE!wCX64-MVHrv`#3;0L6_uL+XqT-nm8(;`M2*+-&h=$oCznKE%s!P``pX|mB}drc6G_TXU^IPMa{e+r^F51@x>`CFU3Hqa9X%GnsHvsYv_a#K-!rSlW0IR&L;CdU|LU>@QEpA`GX#7s}9^qHWr1LuAenHw5#?QDNB&95Cs*sdowxzuyda3&e&lL5=&;=jnEa_Ebv>XNX*_Kyh1LGn~kY(kuVrHF5fjEZ*m5ehD5Gf{;l`TML3R`)ev5wM3#5>Ac3{V!gv++CtRelO+jQquDCp{7)3=7aZD>o9?w=iq`)cTRH96uJ{`18Q?cJRoMCkiY4&Hb<V3GgYo{LHAjeD@(u$o{nuJDwy@S{X$Fd3MDS)&#uS)z3@SLoTs|KUWsc)ZDH8i*)*iMy>k*lUn3jLYAOxX)Y3&w4Z9^?^GaD0&LwUW*|(+ZfuYA1b+=Z~h9{~S4S<ziW_Nj37aN}FV&tnK^Mwec@NePN7@RB05o=q{N5(q2zJ>X0GrBNbrx>Py2-LTd`}jec+LSCpi(>;2jkBsHJ&SSD#A&;Q&~F;nt+)BY<UP};s=LKZF~6WgO&{;MdVlTd&wgu!4aya`7MsTW)iQ;5%GD?GWGw_E3Gk{@lFJu^2w&ZCgIm!ybT0njn&Fl>i$4eTLkN!G#*`0rDDuv@aD<1o(w<GH{0($RxDaH}5%87H1AA8kgyzEE0GBB}+6il7lce!$DRV+?W~vrM+6U^FgTuKXH18UH3Q+1jVnE~~@+s31OjNkSZdOx6TjU9U!!NztmgLTbF;F5z*UZUlPOj%A(fMA+plV+hi*iqkGK*3eYvjzLT+GS(ygAuj#Wr-5Q;oP(aw=bzQw#(L=ZcFBrXmAVF<&koimjQuOmDg~Gt+HM>c=!;#MaUF%AC%fAH!_4RthplY0O@bnbtBU_u4hktqUD7aLHw;<8;_3Q69T=i!19gOS(lDwPnVXw?I$3CTCn~S5`2H+xI4kuG8&Jj|k7PL&wXiF>{~tuaH@rh_f<_!YKZ%m>SlWeak>uLVUUF)5tx&%o!jJckH7;H0$8NrzLEio)emy9}3euO}Dm(Q}6$j_McF6TKmU;%|+)`Oh0=OVbS0fJ+Z>G4shE@mTxE<vOr4WAEN4i!V8Cm2rey9P>B)?YCUX^TOlUM7bzYSab_i_xN$N(*cRk8lUjchL_<C_pv2%wN#JOo=wOiRdPg$1vg21~#BJdox8K6#jD9sZhIb5aRJC6~Wa`#;WV}*HphC@5Qi;e&m0gSVLi#mOUyHj2(UHu62efuE*g!0Auuux=ZYG(izyDKoe{OwWE_b{W$Sl2n*5yeK_!TfkhE+~SxHLE3-&~pZ_}JZLGKIqEtPjD<XfQlz4W9C8cLF-&9Vs3=$M79R|HGcUQlI7F5B^kl7&h6gS|gy5yk28_#LSGF-?d&W>cy?LbWE(9bzj=4N3jjkF1LRp8a#>w(x&W)_g;mhbuBvVmi>z03~P$meXB4wqQhFcHm|$(>+tWmLGTj@toj8z_sA$=SB?Ol0c-up*8}}i=&~O17Vre^y<5v|DA%D3M6&DyEWHs&w4)3i69Leb_SguY4nh<mXUEhk5_k4yI}^DwLRH_8jO;)sNe6w2R8{EIFcI8~2|2invp9n%;HlV;vB?E7!2-lt!-g?SY@D5H?L_C3l`<d6LY*C$4i5GnrxldLfJ^|sm-`2dbY)-F&~p<kBPrkYhsrJD)K4ORCt+x0R-f-q<aR_@yQffu-+)DZdI}jasAnpNWiQks&Ka4{2(JL5;_Rm1JXsX)Vjb_psUo~%JZ?pi*ueIAg_oP_2j%jlgbVcIz$MeYWZHEDodDxXeM0Ae!mPn390qpgE*Run;`(Z#OsXrCE1OQum`nIz{G}9?cFy>&f-R$H)8W`#JPA!B3gXKjSYl~Ws~bh)xOf#*KE+QPwoyf(lJKmnnk|z4rL-*5Ar8-!YAG`<A_C*?aM&k@&w($0>z(#288Ay<l*v60>depRcEGmx-@F%1{<kn;6H|0gXKP_n$NNp#S@wU-gq=j_8FKun37fK47*e?AV<v1jvws#=cA;BR2&sA6b`A@pBmMO=7x@p1t8Bl*egd1o$=k0cZ+)iH12fsgVU34c=5Np5>+;yBgPV4r<MEZYrBAWf`L|y3kj8jJ<xb!=&o!h;**`HU$LCGTGP#FR29CU6-KvtvI!L(}_HVW-*Cu6lyU1b0oOfL_jWqRopLz}&cORGnX3$p7d|<3tKoOZ+EDaeet)Nw=0l977FN7p!FeH&r1oLoP<gA}OX-HMtSOJ2$6P^PYWS=fqXbI4<C8uUq0C0-Wvyf!+kfeuQ=ki$CkUhYuM5M5kzKDxkV~$7WB_7#qLV-^qf1~1&nkO4gWO35Un-Imae8C#@YFUnUOsa2m%1_IY9Xuqt`^1*vANuafDQ<eNuJxhi6d96~zWt<}Vt1jOV$cfMPYbkZY~>X5*uWs&TuyOSOR<8ARCU<)dnC@jTubq8uBEtr3TNV0Tb>kB{Mq;$Oq`SE-8I;fiT4ApUzaW?l)BoSV2ZCDnN0bPtXjmJ3M5Ecry#>MT_L<XG)@D}d&x53t;8|X@{6HQ)>Xs<8VWrzaw#GM!sb3wA9C~z>J>tgp6f>I%Xm9GCMCjW8{@Aqf6er1l{HjY2r6|e(Uin8;Xh=nDz9GweNL3{1fmmPV;>)tN=c9+H%$7gVrapF<Y-SdfESnFATq6OP;12?0keQV)IWy|zzC5eN;DMc=im@8e=h#jAifB_HWWr~(e}AQUi6$ilbxy{HfB%QTwyo(O0#4JFU*`IV28-9sjMvO@8ij9JbCrWuu3h@Dr+%6<^qn$=eg$q8z?zFffW^_*GF}G^3M0y<<EPmy`hh0ZkrT|{i-nyrjb2eC3=dhqiiIRb-}bskdHoNHw}kU-3y3oK1OwW{_!7wYTE+yQrxyZ5)!+YT<fJF;Q8up>>bu;a*a3YOScallbI{a*2O!=IO52CWC91x{w))mQ#$nNhQ%5t64KP@nN;wuWII1;xx?oVIS3~|jn=rutfbvn1ucV?MW*K@bOu?oBcn;Nw8ZVbE~vlar3v~GwFnAvoIq6(oMvrc6eE_AIJz+o$z8Nq{73<g$7~mj{eU34jR3OW$s<&DQDj6}elHS_jI5G}D<CS5ba$`A0LU@#mHdQEEus8oc$e&Rj03!Akbvlkuo8bH%OPa1)RD<5NnioxHAG<(>={due>l6s%FM&qbO%z3V};c0?rs?Uq82Y=Q)l4EE^-A(&5&AdzVF{kJ@MaWS^km*Bt_pV%)*OXyEZIPBmuN<*^E+e2)3oWdn*q!hWY2|D**PjkJDb>a@a6l5+gOwd@GNU^6X>B>_19j)3>DwDZ185a-pM!rJ|aa(8!!c$-}NOo?dh6<5H8uQ!V_oG@r%`U|qnUn)lt}`Cqj##&#)66E$FoILrr|GMh`^(pH8xd<a8D;cTMXK(`Qtjs&ZY&;ES+j-%o}deRb4|EWX$wA8ff_@9P9yPB{M&|fc4SQVnM#nI>f3#i7Jq+OmSlw2#(v!yw_h5o1{_8!KJ$wN=Wwh}`<7UWwEiVBysyB4Z$Mj)zYQmVf9aa$=8?@`xrlp!;4Q5|%`tjidXH1>@npF*HxHDmg$nEV;jqxH{$sul_w(G(d{$0(1Tb|dc@uz?;jOiZ$+BfT`HCIVZcKO+%n)L1%b#v5%+tZs?qxt`?*wJM`r_l=&bFrhRvZLO?IbTJf$6iaO#$Pm^~K$s3!L01|hQ-Lj+fWJcKLeh?-S`{aozVMX{$zz$&84Q=W%w(imZdE@N$W~mGZXVE8{BPf_dt*Wg%Xhjra(oBW;*xuV0JN)*^~bf6B_V!{hl6Y%bH#{{^l+H^KI|C;|5#@ngBqK~rLj9rXHBbg*4vlsb6qVixo!B|l`H>x`15g+a-?+gJEn?xMIHG2r`Zk}ORaR11nLx;8doseGl_XJQYzu|Xle*}D==AFDUfLgLrf)7F_H&pJ!7jW1?6I-c?H1$_L711|2oYk%n^p@wyFeA-~*-Eq~C5@8Aq}W*sMRu>o}!Nm59YxS4{^ct|3aw%t|&R0Psw7@+D<Pq^ncbxLY?mtYi5h&L;|o*Hn1gzxDa0jVr4bb7{;r?g`N5OpAyhN%fvzIr-+m4ZkiVhEG`wx!=+Q1wN5Pt`z@^P&t)cC4vjq<e+ufwa2l(=%jdX+ZbFkLB>`8D=*us+}SWkHXVTmRMS`vh$@?n##Ux5Bj3?=x=4Y=lOd>T&w{(S!pdSLWTHUk=f^(fR%*lz9AQ(l>kFr4*76|wrRI2oG-375DnYMbH8oAPZO&;{Njjx6$`HneB3?jeKay>W@$-tHUgb+8%6Sh7>jfrR%xh^OEEK2XXx0tAZqzn<S(m}h+or$@AEEj@SO<Ha44qUHraOV*CrTF8XLjg>lqt{qZHNiC;LhGG+FYX*;@Fo(#Zv`zMLA+iK1hp_I9tJFd{_+F_GVT^xx~1atC8(^UNCZNyj)r%KKz1tNb|vb<+>-AV4r`W#%F|BQ*$grZOpR`yHY}DZFhCYOK%zkW@v_OGf|~(p<-cbRxsyA7u(MXr0?CoslaLT48*vy+y&Ah=2TXE@+<#CzaIVqY`5)iZ)tD{*J7O=WX4{RfAq?|b>O=x8L}JVoBR8bI8+ov%Dp(bD0VhS)q~E{5#^X$#WZ|79aPaL{g9I~u|7|_1?FNCRQLuDAub^(d$+^`gmho<p1^jM+VR5kTE`paeoAFOW>xTG4c&eEepAPo4a!1kC>0Efv838TDP1#6PC~1+JF>P@M&)QV3|qwm4+5E(#tcFq+pZ?w^LkEMP@Gl-10w}u7iOqA?7QE0Lb*54n8uE{DE*Le9XCfCr!UI=L!3y<I308OD*VVE<p|Mo-~bQzK5>6HxA#W?CAgR$(ys_+enx{wVubrk$A3|n^o41Ur!kH7Q3to_XL-#s6Yt@Nb{b9Hd$&?aQ4r%3`n|gluNt}2{=vEy)POd9j}Mu-JP9ci)^-2KcdPgg@RYrz_=0@|8O|;LFxU9HDD>!s!agFX=NVwChxXxGFQ!$Py{6x8T#xF*xdz<12E4@e+)92;P`cIXGwW)%%4QtB7AJb(_Jz1Kx_yc3O`kn3{m;Hfk=jb;sz)SY4NTD3g61kuw+cvJC{K%V*x}pZNo`u2iY$n{DoMLb`yODGL^7>MW+@>dW#by>K(tH^?k^`3SlaDFY2_DV(+JnqXX~{!lGIO;Q{WaGkU-)l)HY&4v90E&L4vuNBf6-fv#e!yg*Z*HXM`e4ynj-F?XMwYsgLy+1J_}w2YObs6V_$A<_=6|o3@C3fFI*PS`<=}bW#nOX@)+}<P7NfaafYp(iRCCz1PMSy%87cq)jQRKI^6gWg|hO-e5k#DGA&ew0$y~!4G;bJ<^lMq`P1b>cFiRzaX{926T|=YcK5XC@(RYQGJG}V$zQ($#C>)Oq{!?(7n|B_12n+QPY-d83#{JbH)mga?LpanfzzP%b%-C=q9Psp7MZjDb>kjZ^UUwh&Qst(XyUsF%%FM@xutSKwPTTcWFw!9lUBeED8HbId9k856On76gc=rOGKt29*UV{TSzf1(Yj<NfsyB5wdpX-KKCzaChXnkegFo(>{2-nWzPr{Ab1l^qDmatRfCu9%k*f=0lxK}sXIg3(pb!7!y1a0?z5#bJfQE(;)%xV4!);ohPu>sdowZG?Y3!+{gmbe6C6Phfd2H%tD!g~pjE1Dic#Vc(cBs#fnAkGY!I>kROq9}nNY=rDkclP4rUm#plP$~^n|Bo?z)VY**wLj3)3uiR56l6tfdD9M$9n0l+M9)lp<QFLPTC4x_{~d{ZYNZeME|(@&H@CO!q7>eGjekKq6le0v~C-egB|fI_Xidm!)4IsgynY51E=3Rjty-eh>B!4^=R|@<#=@I0eC+&kvr)^mWqAUT7%k$5dp}bCnmuRPz6cP9o9Lnxq%Q6^;dF>*q%U<^WCWR331<Ep>+<-eWh_IW}2rc~HsCKX|ms4JGEwm^Xj=wSxaK4qp@WG0aRlj5*09zIQQ;9w}H9-7Pqa7^X(rExDJH+!Q-RU2vL-4B|-ns}5_D6A{7gjIcj*Q?3F5E{)-_A`8=gJCf~h<47Is?snNtX#}}2dLwlp*0dxs#NHP2$ap$qP2gSywQSlA@a<OO=xniVY3FEF9IP2+J^G5&a7EXItOmOTKv4xH8h1z)b0e;jgq5d(vS&}7U`MYvuy)jwt~tM1@|6h`1<%N|CI16{HKqF;ZBvC_Sb5s-eP22oJ9vDAD{FJV2)2P-Hdkv!d!g>~H{)UzGRmw;N#u8QH+zfrIzc6Vg$1z5X1A0B>8h1eQa~;vcC8;hI$PhB90IKFj=3(<nFAK*By;<Kq-pSFKR~zm!gk09Y`VDbEp(@!LzVbEJm#Mq2^NWY``>;du8(nD7yETYAB6UoOUm_kOZ3qaax+7E-I5(DWVR=WdNB_w(cKfqkCAjuQm*DSQKq4%SY~GcF4B{w+V$n2&_(d#67ae;I&TDXPdGrf*=PUVbF5K6Rq3Pg!)QRtHEoVpW{@grs{w~R`y#6Z2o<jm@$=M@wvrP^txUdo8q(=LHlALX{Y)#<-d|c=a&)BLg0R~WYeX4=W|VY-I4YC0?{i>XZNR#C0<2pyOP#`Eom@H)?NMfU9kU{`7^=jBF~jSeB*gl8>t02ff+yIK!aY#ArX+VySHjjM*@5aq)zZe|7}trWWaD+c!{KR4`=r&kN-oXfpRzX_Zf8m^)w~{P_snTi^I!4gsdbQKd_Lo}o4GqYRcuY)!RfyZ0yzzzHf*x_JD)n#_Y`_xfLW;B=W%-E@X^qFdOUKRQFz~yyQ5r)_I+Evj{Qn%_xT*d{Gy`+V*2{CNBjQs_fQgM*2(9Tgk8+}S<VPMXII533}x;mzR4X4xf6-ZHA>8wUic=n^G$Y*o*ar*50ehuSwx8p9d&~Y)wYLL@C@JNwev)fmxMHvMKwRt73L{ZSUr#f_X`yODdm}43@z}Pl6*aP$dAq_6SjMwH5=yjz|7`GAJRi~zxp?n*WXBjQuf`hsEdI3=q@MOe^TGrf8bO!-=ige73vlyD5z*+E1|)hu(}PXnQ`=L1p{&1nGW?za#B?*fQRRru8ZW(b+0>s;_Q?xBq{=LP%BKZw{F;G$Ga%DKqkJV4O;v}RJf1iFv6Tn$lU|Zj!vG9*n(2?ehXZf{M)H992MuSg6!C+cnZ(i=yAa0M-EUP>_jtEnkz<sDIJpM_w9@OaN`nHYKHHs(wjh5UC=j>V%Z~qabUFtQr&QzNiq%}M5`x<w)DBusf2GS90AiDLhp!DCSUf%9pHkXYfY^HTM1su!A#m=Ljog36aKjuv&x=NpRn$6+I4MbZ7;h~s^vng(D2|0{&rQ)JXyE7b0!79LLq0{oEKb}aJkt#`a8#lI~m(f)X^ZZ&1Hr7uELaT=(8K>$7Dw46+IMX1Fd}^Qe^YcpdlUgp92I(cXVpmN{DxvQz{+e?OBziJXmE_{xhGl7wftgJI3r+9oe6EB>iXH-cv);yZQZMcY<${d*g`uPu!(<)_*!kZz=lkLppCb>%1R^FXAilp+bh{Q*1nGlLQW(MnTO>ttD<#aYUil1}Q@2kmeN&ktvA@X=H+Ty4zzzOK-DRwTe_52q01$@%R{U@5HU-hQrMa>(SH{1Nzwf@jDS4kP3^O#?bD+w*UrOq<)V3`zt|6^AVauHek*zE=Pr!vzK$+W#RY(p)AXS?v#&l1%Gso2mN?T3yi!ShfT3SO4q+y|2(fCpG>$}FrJZA=BtFI6rW%)SAbIp=Gq#(AXpdh`V3>Z05a7sGviyMo8-wkpH@E<JDhOxwSgs)@4jiqOUy_Ef+SZYh;)w4K!PMRhhV2Mwc$vsLGjE5!i$_HuFS>YFbN-18@o)0aI0O?1?S6%=hGuDx0^@Smg+z9YA+{pcu=hC0ZP$u1g3p+@S?Hg@Fs3ToarSV2&LMv3L8pjs5TfpUO4$^GU~3Sq4DSA3|u`Z+!6&0m>$v>^x{t>GLE>f9rUtcaEjlO%<VBw_dH@Y%olMwlHvZ}`w+j^6CNO!H6~^6Fk9>?P08O5VrF8E1XU2K&<y}m9mzEgEiKWj30Vu%Wv9N!kuiGmnIIAnLX(Qnz=;-Hu6bnG5F0TG&;}q)W5Y0m<q@b;M&#t^xQkAVh`!vobA1Ni<R&SkT@=?k@F3&h%E?e#ds+%d6iq^D@ky#H<nLC6BX^idgR-rzXFWrlKarHfPhbqY(6>Uh8eVIJ=Rp0Fn}cHOp|qf=(_no#Wg?Q{SIa9L?d24-bK|-^F|PX;jq7@mALtZEi~3IQ<SV<JBkaXqMKV~MWnET|B`1vlOZSU7+I;3xT8!)AUB>mWh7-`Zt}Eku!*#W7R<i`=3-<L9sZS|hL4`yQP^LP3HqF_s&7h`~&ga&&>cg;%a*;EXde_=x#FN2wwI)QqXjapsTn4wSyTvQ&W>Wt2mh~Tgm5hxbB4I!%_qQ1e6^12m51Dv>S_N0+EC=2&Pq!RQ&elp^(n5@uKvqP}n%0!2ai(0wS3Bh;IiWpm0M()x(-D;bQQ~FKVo1&X3Wt#OS~sTqZKSNhIoEd15yxw6^`v-<pNml2OknMy?cpxFAk;4<sp*F|Y1iY9hcS}n0SUjEg{cP;<V-=8TU6`?QTeimM&|ibf=N?PN3Bg<Jcvarv6S9P_y3tC*i5(c%wLkoUt-4Th9>Hf7OUOf#-XE_E5d;8*bQQau{VbTf-uDRC~NMyHJi=5rJ}Ap9YyPzI<O^Eyh;{;S(Vwlm44&GrBW4eD9F6HFSHQJ0$*-e<Byvvn!Vwg=Y#GNH2R(h4se9r0=tW9YA{MY9@24>(ynCR!pcVRL(#}2M?~N!6w3_16mshp&xFQW5#Oe?okVbLM=Wx|<5OMC9*0&&mDdm&9D#!T2RO8$$W~Ti&s+APqCK=85?Njp!GsIFqvrf?ApMKlb^T=mMt-3I8A*LwQ_FtcsC;Oic4d;<&lG{u(?IX!T7bMkfy6H<_HRP=GJT$YR^9K1=;6e)w@Ox?G5{Pm9Fv}=xRo3kqi2N#Q5my<l8$GF`?Wu_G=;Of6$V0!+*LgI6}Q>pxUl=l>B_nqKvme(_(Hz_y{hU$wSrgn2stkqyFaQsol6;axdx2GBUt=-9SD%qw<7|x?Sv>2pe<)mCXsS#-gn4_-+V70_WN$LS=9?qciN})G3j0OG0*R`o>C!nx39p9n=R{MJm<+y;iEU(9xU45(q@~@&?Yr4%#_Ly`{gZ{mRUc<;lgH12WeGG!Lrlt=bg5MZT|}Tm~Po)KYQ2_{rtW78_cz(;cWBmHlpb3relmZ%MXD?4wC}zfM84e_YAP>n4yN!ARWQNsFR%Hb&oxF=l}`3%J5I3d<Zv0?c25#etzD-nGGx>q7cDT_Ho#js-n^iHOCG^Bw_fw5&u$pp{VfFKiHFHTrtNez#GhqjFKMWuuk7VO~8ZnoW&^TV*-=x6NP++okFXg3{Q$RavfF`(IoXFAbx$C&_ju2Wtct_@oF$k22?Mz75t6Ym?n26Q;Ii5iKwi^*kcaLV1@&}#A7CdK}r(4J)=!K6xtN-4h4*RnQKbG<9z=iZCcfT+Gz1HT>lMuIIbg#=z`3nYt#+wNyeFxv0T}N4YP5TK@;7BUSv}!GpHhKwhRp4!;_rKHygNVCPg+gg;RmQ^mozs>dt$*$7oQJUo??%+^$f=S4*9*(6w||R%67S>=AyP03u<y-ZL;6^GvtAxb^4WR#NifQOu=^aE2H0d<0cq_y!g70J8h0F-u&b#*9dUA{V6>+-Yk|wMf5%751mXAIRm0IXx0vzemKvHs5Io{&6mYMiAVzlRGcg4WsuI+l6(CtH<g=Vpmwh8JzW7H$97rEuh39@#CUg83A`>_I8>J3)_ImO>ob>=SH5E4XX!Z>xYKgD)7a)WnwAURUzY>b?}$LD-1{GnSI$r6+JwG1^kq~l737T6Hvmf^UfSq60agx0F}AqcAF$jJzuKlgR*=fByLfi#HggSG>*CXuUKYK1wVUUXQ1}9VPynDU!xS?9%3!2Qe4MZJNYovvgYy~Z`p}Ky>}YNui(&n_paSc<njR~@|IZpkKVQ6TcfzY7=m6l?&x`Dj3B(YcSoeL#4WH!xozC*R8vNwE^pb2HnXC}Dcu_xO}E1<_Upnr!X9mY!kG10w(S4gC+v<E%WLWsD1UyQv)7D!tmbS>OM(tPdvk`<3A+@@wi9~fX|FJA$uVoQS$u+AV=~hUyq3gEJJZm!<4MPLT0%Qwo2G>G2`iR@ffY__rxX#~R})q>4isIPXjELBt$SjGlsC+J!(Lu-RqucxiI!mNFo<{pn7C^5RB+I{Kyurw*yk4CK23~v{n2OqGvV$Rp%Rl!RPLC#X@^?5bCrazM3i;HHGj&IMHhQz@M}t~UgN@#rL5l1F`fTzuqXU;9u+d>=OroZAh>T+5G(0ve=3MS&QYnD!fSn%`-_x@47AMi`a^t`-P1ZAry^KHEw3@3c3y{2?DiDF4*rpDP-m=f@+6G@qPw!v-fy_Jajx|dy&HE=t9*K?n4dbxCOY~5`|N^v$JzRRf>=?ku$sBlAIiHVvhZuu@KhpmN-k6t=Mvdd-+9{f{LB^0IJt<OjPs&UmhS$tP^RprMBc*Rw?)zBGr26G>>~b^a=D6?@l-Bv2rwO*Tvpb>`^x1)xxBq3mp{ww#!dgur`L<0!ZFjk;F$GAV%fD)oIgM*eg(bkd&uJRBAFkm5pU?tlBjJOaa_ByobMBVeYvO_ldr++hF`{FZu7ZzoS)&7jrpeuj`^=YODgr{8sY*<joRn_Yxo&$W=*!aTst}i7#7ASB4NFU2*Ri=#tJYDqL^&mn+Dp5o^bh@CrW@8#h{U^e+Qg77(d4ToEWN8-7*qGeQ_jgi1RJG2^WeOKTxMHsGIFB-~U0XmCeH#;0-p34m0S7dwAgE4CUY!kJ@Pid;zL3Y;qAd8to@=>vaT`vsHnFSea#A5K{gUi#l2-Y*IUidwlieIhfw4%>&;$L;*c3sr%#x^%Kgb&u>k?GT=-D_66BdNKGxEQ0^`}!-o%uJfpn$i6{I$4C>mV%}-gV6P#`DKyWJ%NvG#cW`&p~{eWTFtvgIp6B+3{*5k^5^+_je&rMBpHi3L?z+eEsSF;z^nP={W;(*8tUd`OOh(=;&aedw7)yxHs_sQgie)l>*kndTSW^Uig6(Nx&=gVOnI~l56R~n(y(`l<(kY_U&#J%T}cl@Bqd(G6&p1Y??rfBjWeV>x<c1dwNHAOZjEb6K6o$Coz#eY5gl{oza;c=JC2J<D~QZIibp#MOyf{nvH(o+Cd*aMU>sDuVws^yRv=(IP?Qq*cc=*S}++X&0vV(xS;_gz%x<(Qeenrm{TA0*=yfkIncVY)`wm1eO<UiNB3fZqTtf>>#fEa8}_*9tBm(iud@56t?i4!DM{&#LlU=0&+7VejwwL*kQq)r1UicVkX<A^8sIX;>&VbBGRE@ba8Iz7vTW83-D9A|2@L^%_=$$$wDJ<}TFjrF4u9mg|{@npYVakvZ{*jd1<UYqdO=xp~D#zMQ#9M$~wgxrx*aR%6MYxta4xc1CL187fA$rzm++rM<z|x|X1yS`dg;V}QNQO8SRhFeh&cQW7_<T)TJ<XfulWm|5!U%uSM9Q>}DTj=5-iWo1BC^eZek@?mM4Vxah(y5|3KnQr&)6iYo4Cw)hDY(Y-<9Jjt@N{d6SbMSQ9%<SG&NeiPX#glGrUHuY<tg(F&cTzcS9b<9h%u3YAuLnO3u;U!VoG#H7g->YB2T|CiZ8z6)PTNXO?F2FrU1!bZo1zST7M&5!J9<&gm`=&aihd=;qcFiS%|$f5ES-qhSi2y!P<(L$)<GO^#etoxE3e)-TQ9_)PL3x8;!i-#3q6^xPaz`YLu+$d7=YIwvofpBE<QKjnc!M?`I{9{aBR2s2NyMJ@Umy|$<t}(#0APMABljhYo55}8P!pl<(-Fr|6|!GkzjDbMw!=al+YYGbEy;WYzy6Z=BP<k5WT8=YIfqY(r76~eO?Dg;7a^;JCV8Ye1b?+B6`>|AdLE0jn#6?y(5T=k@lVa{3@_EH~cRXFuy4OiS3Vr>xHT83Iy>)*NK$qOwS|}fJ&bm5IhKUoSgA_rkq5UZycE>n?ig_8wu&j9g1X^l^2hlU!-S<9D!X@hm@AZD^f{MeP%6@LEP-hU}owS3u2{RBGcp_fA6Xi*4a0w+guc1=fX}<pH`Tt?MyE+!6c!RA`@~ay6heI5)hOTd9E|T!sU`9OQ{J*a#a~qPfAVHrg8QYS>9Uu(WFFM-f!`(4DKmKlB)_%j3=bEbtjJrv~J}<>>WstamF|ty!b@9x5x1xj;gf0<t)ayW4Rvp9t~_IC{TamAXLHM`V7{@>^gg5P}KOMH6bH7!fSA1O;qs|z0QYbub{nViTkGp#j8!>;RREeTiBHdLA!TZ6VLh3POOQQ8!a-nOhC(f8Wc`oytamQaro3bx4&L0$Rt87PfNuLzd0?)l$$AGZ?}Kw#hLX!rRlwfq_6fQDKw;kCtIiPE-dv}yq-+FLHH4zUYFK6T;bixBIgPpPziQf-VwA;+Ux5;5-g^>*xJ+zM=*e}&t-X!XxIj8n|R?3J!pe3_`7|a07xU!rx5D8<4{;*4p5g_qXxh2%lTry;$pTd-}I<2WXpK`L*cK+>6e**eT?P7;b@N2$>n=D3`Ju86;FDxR(#2V4#&o$eoc^R4O2nsM%K#=PV^HzJy6W<#AC;Mt~01-ySQ^TxWT`hD|Y|Tf{Mx+7Bdl9o(9Z`@~Gk();+hJvV`hLiXKDx-mROJ1w5me=)YsfpOe@XSBp#j3{ZDlMEXZk7iF52JC4~e-8p_1;?a)W&b+2X$hSLw|5kK$%1hy(>CF{dKI$ib?7cDm_X3;cThMMn?CdBfZ4MGUpGA?kyYUoha?K0(!#RILVh!s{eS|&^sh@ATPlpASUt9Gm>+gHAblNx_=w~ky-QL--JRc!3a1k4Psp5NNZK4eaM)^b^yj4waB9(t)A_oZqKogqu+apIItMj~aamsy1VFc(>dIVD(j_*<JE7`@jZjGBl!+eFz=cPG4(EOQtRS1EfXVX}Dz6c;1jL9nvbZ3^$pG12480*h-_M2fmn#M@->&Vhb1pXiB4XzV6D0_li2ZWD6kr8dxaqNfCDZthvNxcqA^$*?P1ObpkEU{9F2`_T7&?QlJ&RjBDGp?Z!j`9HM`pVogF|q}it&&6_A3-bVb*uI`uAH60w>}nP>7j*uspRhoNbhSpMv&+`h2pemsF{jH-vQAl<&c=lbts_XGnq38m!4edEil?dsTP6m9m0lOVx53$*}duo2~dJwHp26Uke7M{VnU^<Wyi=AIe(lGkuH~i(>DP-{g+<12|VZAxFITK!b-dzn)4i6D1&W<Do|$DOiO&mmOn;xs?=e510eX>OlJCKrKKkMF61YVJ=5?=&d1yg=7F-tm|cx}T>|+B1pk6uP@-KJSV$~OsROo{n>vwZ2)R~!*mTGI3eOt=IEhn(cG1Sx&LAB;j7Q;3>1wcF5wI;aU*c=a;%0FpPa7#CY+D$c2fldGCy?O($9-_^)eG*jjqT0Z@wbm3_AxE5>8)ozvK!y}<h%R$*28ZT__x5vx30MGF?~B9(+B*#zR$PyJ8AaEe*8r8;ccRRM<1W)UG>|$QGM&!_xWvk@#A~__P4mUaC#(t+{g4SeXOtk2n>W*efN*+Rt=$~)wl6IKAyafuX<mYh)3RSz4=tH>GG>rQayc5D)u_paXa~Q$NR<lZVj^_V2Z+T^ryya<u?F=2WKE$*Lf;luZvL0#12tLFbh=(cH8BJ1}o=QcU7JPK|@)%SOr9zXL4pC7Q~dl3<@CXFP;2(1uPY`o%~25t+BjLJb@3gJNco5a@I$p*N<8sIe(K@w_C9+E<aHofJ)s(uixum4X=Kv`GSJyt3bF4qZWUSng)HtOUG4|oS4+cHM;8X)qC&rxN5mBSi}5uOW*2EYpt_uo;H5fbzC^BN64+<FJo4O7_e$MoM%^D#nI{UPnzd{%d^aX-hlbr)@kbj)#I$2v>wO#(Y&VG<<nLlqd$~SPQP^$0!#->BZ(`OZ3MSx6+FO?D_V%)PE@Lc{xaX|9KA;{v>it?a$7rTIl@;`u$>=#$Lr;v3@`np_3e{ybNe>8mM^b~BYt+!U(cT9?4x(ZGmW|2lGP92aYAZaNp8YndBbvT>t8)>dA#sY%YC0d@6g)3I;g+-SM!mjh08$>@vxi|OE{Z97eCHdIB92kzMbzlA+=)9e%jfamtRk=Ih=o++GW$lzD<`KJb&enscz|nuz1p?7yJ42;L_Cfm{Mkj#^iYVsw(hd-r8{dB!u*<ujgqkr#!9wMV?l`Q*yZnu3;y9|J5n1zvenRAexkct7J?O*{~)|ZovJ)I_z5EX#ukc+273!t#N2sZIhF<>NK*_?4zzQSR1yG>n6*m2efBGIaPuJ7KYX+>IQ_)89o?e9G#(+FkLXTa;qd4#PE-Q%RP6aXe@}E>(;q#z4ID9@Gu8=(kZ2F$F5rVY#W*F+)uToNNxQt!2g12DQ_Nw6RDtYJT?dpTQFg!?vXHF$6G7E(@ARyI&jk3t*x1V^4snYO(S-LI89a*ziA!mN~=VWh2l3V;5Rs3vQMegUcsEu)Ir*ha_Km4`WX91m7id~#WiAIPC-=AH!5w#?(xu;_fQ6&XS<p==%h^$=*_3jAN>xe&H@NSL%Q%}4y{+;!ZN+?ypz?Jef5bCrgb4l!0xdkN{*s1A4ENk3T|Sb<`d7EqNWJ;jn+lUFmo>505au)+zkSOZP4qXZy7H@=iUaDGg}iYYXp`#N?_^eiL4w4@)F;O9dQ#n4Mp!*x8cX(fA;a%)A0BzOkYumJd@Tw#nYH=$IyGd6t*SHpi@$<(O)C^Vmkp$a_zjD&<TP^$s?Nu>s1GqsTUr+ae|MU=L4Bb3ELpVhX)zdtt?#T^ee<Ti5yKlvWZxTnTcKbwRY)VRcVp~)jO6ENG<o*NmB)RWGKCMUb+QSL6r#|kHO+|Gy#ZiOQiwog*S-}W5fdDOIk2_q=*ExBYldS=*a_Mrft#s2o48Sm?%_+RFt|G^&?;yiAy5&>GnMHDX3;|7cQXJot}6FU@xD&=+M9Q-oW5nGHen0XS32F!2}*wRJ_H)@AYj)^*wTK2CaHPcs30KT#*1-9cY8iag&u|3-~Va0kMoc0Z=Z~sK=SNiIs`L5##{lk+=(#?PDE4ET#lF%#gY*kbU;=%9=DLk=gY`(}Q`7r-8dyaNCLs&8RyxLP_?D+bT^jXgZ5-BYm<4`5Tm4nF-k~1F_6wD=@8!mYmA~02XYb0!T%&7^&(-B)+~YOR}fx9mS1M!K%m1(Be<dINGLDj<$(_*zJm=?Tg0IHZ_hmYxkBm-PT0-hjO%aB@8Cv$kApEyaT+OXt9pNOGwTyl6{!S-i4;^$Bm}#gc!Qfv^^4ZV;_Gdi;FV|c>cAR+7g8tFsv_=wZ&;o*49PJxP`B+%zSM^EQ+#?K<r4|T5POsk>$z6=YN5<EsIk7-NbFtiQ8}~VqNgDTXDCQ6?a={g|fum20Ba<AQaa1MusiLS5>Z@sPKa)@36zuH)L>|oWV_H1;OA}sn7PQe1lpS>H3txEk48G_KT!GU^OhSfl<5iyPo55qy2D~y@vR^*xb&k+{!tX8{lyjZ*bqsY;O6}Qn~$^7qiM<MTg$-+hN9U&sh7+TJ&DzCyRZCf^xQSx^o;>e+9{<YHQs7yuwdEr;&-9lVy3m;^>UEZ}lh&i7On2YsV)q^@RDDTIyK!Opk6Rlo>!>O*5$#N;9>rdU=D&s;*G-phgg4&3(TQnznSTWmSJXq1mX+paC6TL`92RrG<5vWwyN1mRK#Xae=y=aX**2;8M6E%W~(wG7v5QiC1AuZ-Bxcs3Sly*#fG0x(hWocIFQBw*578yiAK1DW*-z$|N^t>vbK_siSRb8#_XVmjsXU#Nw}&<t@63GY1~Q<3>F+2>Loe773C|g#Rc0kmZT7RaInSLdv5|BTCu!%Dyedt2Xj@PYC6}+9crm?~n@C0gP=|wkuHUDXg4rN1zRvFhzYPe1+6BT&j3G(fA&G8v$w{kM~SeLLt@!TMmfsf`w|A>X8itmH@T~@Nb(e=m*FhsIh!N7Lm$)K%4&m$#WdjnH<xqK)vUP0dTruW#c~9y~^owW6I<?7HPvED0+zxB(Y(o4=5&E^mb{>2`Amq^Fa>fOig4UMf#z|$+WG+o+QpYHx3H-7s}PJV^v`Y&JkZdA|I2Pve@mp2^H!i-0LR^E@_`VR^4a{WJS+SDlNdasz|0(jNEhlm2L-xlxY>*P&S#WFx7g@LBbk4)>0-d165(_-P$__QikCw@<S`up%gnzkmxvi6?=?|W;hWLGHwX<6gN(0HXf@bp&vShh8R64Dj1oSG!Q#xDxoJ)Rl+s<LT9;(FlTPksPH4h3q=teI?#}%G5x&{VONsut+bxHOVubYR$(p9Iw=gSepsDXsmb9LwNi<vG!h%i)fK^AIU~4x!ll#+H#~^sVJU@~n&YWHrBkBcUW`hc=CtacA)mQvbV})YI;E*`+`W@dNwoKOOad-f<Wgc|)--oh@Bq!sru<GiCAsj<=#=*23MeS>(JL!|!+k3>Mx`^`>LQmChxF<Rol^QNG<W}fnAz=q`4zLczNkLP7uu>=rgIGfl@EOWcCnr*5ye?fkoDE&jtmfVcepbkll`PFTwp$P;~DRXkk?4g%zavty?Q2l;Sf1&I_FG+vnn?RG0fSBvaMchxI4-8QeK}jTwy}i6^m$_v&9p_V0Kl?ySQYkuaf;DisuY;jPIq{M_5~h0v<FHovaAdGRPf^uVz(Jm0IMN5;Fu6V1p;&I5|X{gWVZP9TyOa3}hx)wW&v<mYlX^PB`T^`EGgY{#^KrvHNXEL8|bnk}6oB_nubmz<LubVdu2~IV;mW{d~|t_=;_u+o(;|WAO^Xfg1mY^R&8K&XynQhC%g<%z>ATz~fg298yt+4DPa}1VPmy6_i4eg>--kUus#%^^=ArwcUBkLKL-?4aW5J8{H>lal+0&BxP26U5r5ASC++56vzbaQY*utY^E;*Jx?-&_Fnr#`)4`IHuRiO3L470Yr6$%AFvc^f#>KbeFN=5m5qcVjuiDtk#abfx3J4>*6ef(MuHiaP)4${!^mmz55Kn3)K8G?Gd_g;7;ZwmdEiG|u{*FZAEa)eQoFymEz&k;FDmr_T2%XQx(~&bAegf_a>sOjdjGC5FK}jlFzY{E-HSMo@t^~WuE8Pm5bcEYK)y)pq=(So$FF~5@rHiyqARrdLHp-(mA#BQ?U>jSu*SB%_uRm9+{y#mor=DMT-bc8>B5wiN`q4yHRdWSTAKu5y%eVtpqeeNqPj~>oXX!R<!p9#ChcRM6Vwuw`&M}}uNdH9ixZO~X%ka(i;bM(Lo1gKa(B8OItcTISMk(kau0YdEV`kvr^TyCDM#lkI2qEh0}n^xP65{m8N#9CDI1K%rjByBCKml+Kq{^bDdYkEUmvcDjaaR(QpM&R=8x9K&gh2gyR@;~w6S!mjg{AFWA$Cy*q*MB)U>h7jKki%cc^0NR255ku3L1@Y&nS(=he)X9ZiHYRZJ!MR9?L?TV7Vh$}_51d|nm%JYMhr{kw|GU^=(B%sibL&@!pCDcU@P=i1V}JNtHAC&Qk&O2Z#9_uHo0LNhL*f_NdS*Lqw<XEH4Ftg@AJfQIoA)qE^0_mtY4t)$=RS(I;Jjfs?=gk}_%flD<g;38UK1!aojDJKyb#wec&%G66inOpiteeP6I7q)tQVi}I^@6x3@S{#{EF>kb|)1V;Cg`MS~xGA|;vf{bmi9l3<$%69HX3gSs$}>bO`<B*pbb>l`MfQ-5W^Vk{MbZA|n%pu!gz+M|rOlcNs#d-wxg}h}(7G`+8>LM$I*K6|_>qs9k*|DRP<6X*^G*o2l6KcoBP_0(${mf_xTFPR7m9r=IzfuEaWhqOeEY?a%9dd+VM{XEp;aNIVZ=Dzg~6pPN|ud?rC1qK_>=<-hoBOUVxCm3Sg3;>E}5Rn`M%{^gcZ=c$1zcSZaLpd@AJ`hJvM;FBf)!S_kX;C2P~0eD`j#+_|A)iw$ZV8dLsF0mSB~X<eE?sS^1;jD3Y;D8Yi!Q$=d{HsUYDdEgqU7ET$?1rSN>25vQEQEkx&4L@3hL(BK8Gy<R0Q$S{{`UD6sJG<=~PCq?*i4uV#H<lE$svCCdx=8zfWPU>I59%IjYea0#w&o!wsWnWVHlHIwH6uV}z#F?I_6)_`q%oE<2H90z6zq?b$m^vGg`xCktZL*@5FjG5k=^wpMcWypF;DL2vOTQdl)wW>{v?D|mlSve_XMw!(w->*_;XMnjs=i)#c^sZqtgvDkPpgb3#MNfB-ihqOXRLMP2(Lj*bxW*aR-M2nN$*3KR+JyC0F44{@(ASS4#*yE=uJO@n>Y@s`2xy9S=UXWaV<GfO!oKzYZ!7xk(7)@RHI+EWItJyFR|?}B5#CSmr3e{@rZ@ZZlMDgtAl_Cj6=hfPba8}EiNyWb7gH#<gXVJ+DVPFr?@3wR8NH)bzQsnLj_#mll=75_P_R8i}Ob`wQK+%VgKjba1DFgAwV|KYjYEd4|JeNFSiKs_9EVRfKK0$%dc|DMtVpFD$Qi~$@Lgy4}-Bo;rLrv^^e-{ZLn^s1XC9L4DsgWK5*7x*fAb=>3i&QwCw?kgH8EgAR8#y_~i8<$%o0o!!1mniRL%F7~~N-CNWQ9W<7#-67d~GgBi^M0RJF^U*|YVrT($k2cX6|0A<&{w<W{r$k0=FjqrLU7sb$L1)!<|Pz+vl#SZ2}$0$>e=uj<O09X&u=NZxg#-T^~be4ot#0kh1EU=!`fw(5f+pzWFWK=1N2=&;Ro5ZkH-g$Tm7a0adb)vJ`;D?G_?d{6>I+9nL#WdI?a7x%j7)bexAXNu98=HZ?@NgL-NTE}Z3gOJmzch6aq&=cc47D-P#DEo@>5RgGE-3-dhE^qns(XgoMwX%i;^Tk()|LO2Eqki`YZ3@E*G2J$)-Kn0N#qVxcQ&WWKcSIlxU4AhUe(7s)%<a_$#s5)GgFxhFC?eiDl;6b<P)`@=#M>-n7t&hdl1OC(X3S#b9eDOJcGiD??z!cf@@E8-K4)zUO+4~oqz8-KPDYw&ESQ06xN_Me{kh;H>0rZt8RAGzJ@?ljGCVng7u$$I%D*G=VLnMgtPgWvlC7|!3k!1UY>#kyA?=K#mr}fU{Mvcc}gm~sII1D=ku{^8bLXol8OuDW`m}Wo04h?sDut}8WNkb_qY}X`}s_yd-~32;$h}~tM5Gx&!}u`a3i_~cgokl`60B%&jgX`%_a6gO^qsV8%v8{oEm2kQfTwQ$*w%9PpHN<I~p4t<WXV$uyKL<k~WJ<VTa9#y0m-JB$!+;q{oaFS9ZZvqtrr28qyQNDp~ZW7L0IWt(*>qsaJtvVNT{SaEIulSHQ|q779IMuvhR@2xAPv<DD^giWh;ncmaTdkonS>BRW(X>HPxz{QUKc^1uCEA)3;vhD#Nq)U58cFP`jiXS7lz#?~ZS+ZRdYpL@=QA~M#+zNn+g{03xNO`<BB4>f8R6cbr%!?2*3XpKpUke{{8C?>i*;B6y{i3kkmiWGfRtJH+TE5n-l+HC|GthK?J>eXtpSQ`%XMz63;Y45TX^J2~kX)gFH``>T8_i!E0-R_H_-h#+JTx;|h1IL}toSp1X&}Z<fXQ4{mpKfyGTBSnCAU5<)-mB2?j60)kJP%js!-6|AvC_C7(Md2I$Jy8DMVE_X7E%#_%38>MC+Vp~H%8aV$O^Zq_^?D)QkheiL=xS3n63H2cTS;CU@FJWjJ6(uup%T{4qL*|GKX#(P?}O0w5w$$6SA`!y@P%H@7~D5J}Ft)ThF|aTfO!0+sC&aeq#`OV-R~|5PM?~dt(rLV-R~|5c{Bx{Vhfxmfq;Y9QyMDgIH*e+7cHYF=Pur!y^_{qbfQIrul>R^a0Re#MC$@qDIyCB1<_zm)Li`929{nOn2_Zo+G?6L3fOS&#YLE4JrOn4*s-aw$gid{4?jq-5V<gE6>1w%D|-vy`HNs=cMVJfXvA~Ry1BOd~`qk=?OCf8crCUe`@_8?SvJ<mVz4`oi!U*NX}&z&Ka*%u2uz^IJit2ow>BqPW5s-uY$Xx-#YE>aCYRp)0D!#dTJkq63*GgSOG_bXv?6iuGZe1(26aOkk*gD5?HDh+}egtn_0sa1~h-J6_r?ga@up`V(B7l*!gIl{N(JM_Ho55wxSiwP8gAz+$i+<7v6MW4uZaFKU_15g~r&W%<FgZC_TsUH8XI%laMQ<@Ot8~ker_B?6=FC_~gxV>|@V!Z_P|qGpAMVo@Kl`BM5sH@!31uyn6F8AK6Sswx)G^j)UykL44-hrMI7)5aRM?9_4eAtmKxgn8=7L^pEKh30Jsu@a#x<a`*YoOOMuQ(H8!=lYvgp{xH9E*|a7yE6;v=@e0p<t0RTGOrvH)tZm(UAun&9>!_0>a~HkDN49<iy6`mA^_RaT$ZYY#sC+HY;bq69P?4A@&VaM5gGf>#!enR2Y&wO^ZX7a;q>&zpkV<lMmdh17_7oa>%_MCCRX5h*g2@)%h&6Pltf((f-XVt<;53$6MBkGm;z*(vqEs_5P}&?)5s@jf$Fob^gw{c5gQTN(%oB?$Vjg^zS>2n}NC_Q+(loLGL(VL^LMl|d)}E9mJTr+2j9D;>!j+B{P^0prJf?=^Z&b<w9&wDR%g&PmVz}S@C_u%)WR=&W`&-VDqx+vpJ90q9#*>c_HD@L01xlghqcNy@TB~K+&=i8kjfntx#}bw~U%GguHm7hvTD3qF2(CGfg4K~yoHLTV;t~?kT2fL+MXO4(WLH2vr{0TurQG2BN_{F+l+tt1eotxFA^@G-sH=6%k@O<3iBwM%bL=!%f|<}XiF+x`0DqEEaqDo5f0>~dA67#60`%fjBY^&ZP1wms<Hw;sq8imee4a}s*0HNs_EouiEZh4yJ%)V@Up_!&d`Z@VJ(=T1((mj_`f(x+F^r4+wWr~venM||jcHZ+_y^*ve((@fl#xA+b#${A89-1UnDp5bv0i!)fN!~Z-Psy?5U?nr6xaiDGj2n^FQMBrQtI?9z`=J3MdB)XDX_Cz3wKWD>#7|&MCulclBsM6^InmbClSsmDjI9^ehfF_2qU>vaV{N<*!Xup%i;$M#(OP(2Egl+^?yBj9pqtn?fMs{syki(9oK(;as3lPqr~oKL;&mBzAOcDlL9I&?jKj+s{FDPXnD5`(nld)qwfkAr9j9pN`c#VNrCM;N9|M!d|oh4`NzUvK_YSYGeN5quU{hHva|_16;588!uJK0#+lD-v#A~cekccazdimP(~Rxkk(N2hqRIpD5|2*&w0{iOA^pw=Bz|7Qso{V5;J^J9O!i`{PA-p~XFim8&x~jwD+rutGsumKBa@Cq<-Zdv1my`DN1aOu+t7X?`On(D8ABGk;M&{&@CK83tEKc7YkvFq*28bn{I^bigG{_ZCf*<uf1fI8@eMWchMIUoP5k|in&@ATc?hMxaPZ={?+u@D%FoxrCsx>r`a0}H*GkbKbiQxV;Tb`}71c2^)Ma5O7@rGD_{)8XWn|8nmtNBqLW_XI3p#|k3|NXM(e|g1iF3Tfz+hH7FI~1EC6aqY*N}-&TKM~Nl>8m2i8DyXQ^*7(HQ_0QV=1~eo!2d!tG;=WoEX-1!seoDa{)7dB9e13c&9!uEktxu?QB65l<>3w-qY%Fsfq&s6i6_hLnfZB8z&Nq)^h(iLnBl@PA)6W*X;4cb!E6#%E*t*4W19ibn+}A`qM3sc3LV=5e|}ct~&M-Ucztj<lua@Rt0S?mUh<K>@Iy$C#6=KjqDg%V2Kl?L<~<~PlD0uGFakbKwqV~(o;OcX?)+~(a+aryZG%IP7t494C19XFF+>VftOIu-s|uZXK;vjS6_SPL0)+O?s9JFSp>z>`L732T<n~3x%V!BDAG#-eZEOE*kC#5H86mgNiKdYEaYX##A`2Ao+*R3>XWA*&*s}1BIT?Cod2qLS2WB?i_n#K_gFfux3@kxZ?z3IK>>0SkoX%P6-S#uH2VTeMpX%@Q;sP6c3Wmv0*@<}vgDoDGgczfW}@CwLKQ9Y5r};{4HJWCXF+tuRHDLLAj(idGZxSY2eD)*KEZlNNC7RU+(fKcbS05|)i^OaFg!&bFATTE9V&J7j0rj?9+OSW9jvZS6a#&>z7=WqmdFl_>V&R9f^}vXYjEcM+5%YiKqEQ#>?^zSHJCmX!}_eDtN-xBhza6t=#IgOlvuu{0@DJmuCkt7BE=VpmuzZ~FTkcb>6Ch}$Rmw`HF`3sLQTsV#p9MqyyzLeTZR_XRp=>)+8!x-H?s5!RjJ`Fj96t?Z97Joi%OU<h&qV!kOcQgj2=)@0k<w<Q2`}M7d%uOIb4w}IYjQ@$D~}0jdV)9zyw$l=2BR(28bbGd|11f6a!*-V_gGI>gcgkf+Ip?1+tE_o{e$+49jS6k`*cGtf&Fl1Bs2DfJ3iEq~c7cMj)4yRO-c11&l;0dO+KvSF*`0ua@&)dJEpY1@GQMOK%_Fdibq}-y(N!k-N9Z-CN}DEpqo3xqFM;y+!WcB6lxG?&76`rM>Ased4qK&A)w3<c@EygK*s^VLKxHNh8OU=jzT3@~A1N)uU4Id~{i{ji<@Z`6StSj)JXopZ(y|$lXZCX^hW>)y^}Wua+d@bsp<`h3%HS-HVYsCJVdUza{xzcouz|=UCWz*7I_^>LExz$dbbBnaf3Kw#m~Bc7+867^GU~JI8gt@JR-=0$%I%YTT=fb6#*rC;8oT{4Qi43(sF(r);-C<npAeD5OG=-k#F(A6b+*O(mSAFrPO2;v<}8uSb!8pX4>4Kj7)dRSNU!<DAaC<T7Uu;;`swD7`|7>iLj|UQhZoFsHw>ILn31<@m1r+4p@N-hEDZAs_jDLM`Xn$EUHv7b0ID_SG}N$8;eH`d#rLIzFFCI?ks_$4>%k@6HkS<LPOL=RCgi<j8v3yfU-+VstFzXMghY>%~;!ws<ecxt^YLF`;<f8{wJYS3K+CcsU}rip|aM&)&?h^mU&^JO0Q*=l=zl?N`jwQ?vtBi^J5FsSn7{LE2XszYd_8tu!~07Z$FMao9odUz^a|g##t<w8JK=dM33Z!KRK3pW)F^FK1H{5_VZgO%>)yCBpnqYsMDL`l6<th&MqH&7Nl)HYiOT#A%C)3kAWEU9TEoc8Rc|bKicoJ%ZPNr)*`^jBCZJSk!rwm}Qy~%ow@nZ&3b#lnfoO#;SX$yHZutjI^*B)p*L5mDbQ^RMWr(uL85)f@;VoUYUU&K6TJnDUPV7Qbjxer^2u1vdd-6<@-7HDCLkI88ox`@esZ6?9VCiM1f+DdQTaB$6_!!gAv!xVd7n7;V6XLwEaM#w5Fr{B%mb6FtN=1L`AcTq8#65RH{m<&Z9k5&=WGm9w-8GkUnw8c;L={@(`3~>UY_(dA;)oSHA9*EPjA`biGua%m^EjpO%GLa1lL4Vi7kbTj6T=2*Vy!=Th509t~xMQmgUHyOUP`7TLk02;qqhQtZs`m6ICJ>STAiQBbwH>6WSUbB*7leyG$i-6fa5^&!E)eemgimUTHPz<E-}Ca<}QZAmbXnI-kW_`9xQQ_pJHs16`1O*ew+R@nAhm2U^u{$st`>O|$Z$bgb;Op<ld;;i}_Jrl1*QJz%KWL3RJ5n`#VwjL@!*y?lAa&8q>Rcbi<k;a)@p5)G1%1dJ@M@1QFQ>tB4<|=+3w{`;Kpej~K{xyZ86fc#DgvlPuAbmuJ<Y%r)^RK*j0nz8^%CCKvL(@M2A;jHWJGs?GO095mQd+zyu(JaaR4h5I$|0!yKxNb)1omYizfRX)2*GI?@=~G-l4wiD@{$>`=8Ed^NXjuDl<0f~q1mm91l8+k_u4RkjYqQycI(x;(=8*=$%|QSR7(4bdxsL1?Se-oVfzU0X5#T4q}BPK|IWKSpZ0fouCv+GOE*95<C6~d?BuAd=un>Yu`12j76%~dhB%JFsl`z*x3F@+#&cIu?c~8kEBn~w>Cx*xbnM_g1!<WpK9nROm2RCFe2-3LkNyk4Rl76ICA(UWX7aM<RgdOXkKTV<J^D65PbMfC_ETxySytVdU(=nx9RAT0GKzv-$vT%x8+$YJwXj=z*6`kE`*{E0uv<9d>?gM*sX_j?DWE}Mtl<#0F<y1~%iE}fKX}AOW4-xsup@E9N-q(El#jPi&{2Btz<ZT^cN=X`4-fGX-$p1?4<t}v0j^T=;Sg1%W&emDPDhk>_|atBoNH%x+LwR8Cye#)FTSqY;d8o)?Y<ND@O8n99CthE$($!h%U{YHUQ>tb*0l}UU{tS~mg*=Nqq&%2Cb@;px`}U4<bJM^fI`tr8N<Q)FI^FngffP7E)6I-XVw9x^+cv2dQMsa!-zjK1u9SIO*7i3yUKDUs{)2OE{H+X$Zl=h{~CM8&;CsO4V+a8GBQ=nw6)1v+R+Qi5@n{rY>8It2lVSPmESYu2{1Z5o7qXWH*V?m+orhffk(2juPD@Mvns=u%Cc#Elzx65B^nA+BD)fXKJ<GtkKiW-BLO!(>#Hfcnl+IRg>$qx=-ad)JTiu~BhtT;+{tb~fkG#!ur#X_rRxlrWz|$;HSdTD7ph1NE~HL1V+52ZKSu?Z6iRrB|A}l+fO3sJD4;SSUX}D%Q_8CG)7cm%h^TLZXdkHJ${vE_%`6x69&4VlWFh+5n!z%uiA6e4XwNIR@5m}ipN{I4Lp5aKxAa2?Zb5n7WYJ9k-uMlk75M(1<ycWNgOdw@H1bq_Lk0C4cmJ|dHH{Q&%Qxhv=!r!~#c~_aRC=nkeJbB<lG(drpV;J_9ZQz2D^j0-S9aVb7e=N&!m>>;c1@(ABD(DdlRW-389Nm~E?(N#Zf1}0;}ot?UK;AG24YaPK*&K9-8{C`hhDrRBg_2qCwR?xB9n37L@yC^MH{eY(?rE(!`gzboAO5Ag|hoEy{c$n1ecjT{q9=UBqwIbH#SM3=;z%X4D{&^o0I5qlC~wy$0JL^M&I+wRoZQ^D#ojHKza-cId+Xpld3RtD5fwDW|P6yV|(u5*4@-BmO^@$3Dj0{=k6j!B&zJdFecL}&fgIBXuH<1u{PkN?H832trNQ@HY89RWh%6rTe4BXILpHrZl-KzsGVu&V7aoGpxjonL8IJyw|K31_S4?|wfF1YTeH|O>RU4_Z`iN5yp`=j=xHykJFshQ&#5XlO<6FgUq|;G_cykgv7}v)KHs7ZHz<}ffw?7)w{DXcMoMgG?WQ&X2mWevgB6d8n9cYfL`gKIn~gl>?Dc&vMX?}ZJwYx<RUh?O6-K~}xQC3}-w}+><J$*0t=%JTZ8+SxFTVo^*J(%oPjls9Y%bP}Z?SqE9-{Fros}rFJ+^Bl%DPw7CqqpjT<3&uX;r!|vCxx>GM`ni%d6^j9oheerF^=2h&tE63B4+%*tJrMa|LyGFUtLojV|_`6EBrk!!9>>O1@CT?o~z9?^KyqK7!3jHN|eOpl(+yoFL*~>t!#ZoOEK*+SHrCTnd{(1HF3R8n&OAPAT5R-&i;wG4gkf^YMVRsD<_sF~U65QU@uw2!d1=^)@B4if4@Ru`G?B6FGt;k>|i6N_`lUjxo~QlqGp%S`;iY?x{sv1;I{ATBMk0{v7>;yC&i79rk=}wlR7B9b<6V(6SsuOcf(dsYhM+kvMS{upQdnyXYQETqk+fSPaXVt#~_bpwk9ky<HaPY?Gg?LZlwg8hF0Ki&+s}KaD#@yDu>BnOa!BhS<*vVwO`1V)6lI(+$Nq8RMJ)=!LoF7^NM*$<hJ@U{~FA|5jqopHYdQ7{F}C6&0>L@}^r4GP2Ztd$r~r@fuWWE|R}Wee#%AoyL&3V!l@`h|u-SQROX$)2CBQGM|0RUyal|1|?%c6$<SEv)rG0a}@SJB8bQW+PrDjn;;rDF{q`%&je^7__yTr5{q(Tx=HeIFh}4APQI9b^e5l&`)~ODH|+D<$G0AS>)|*2{u_S(4Zr_Wir-Ifv-GV}*&A~I4Y~hY9JxRIG*>DkOzNkJc8gVOoS}Wqyam$zXYl(^Xt%_<1^-|WZfIm?!qj;Qj!rZOaBgIG&BQfYT+yJjT4akqX6B=c;Ubw6oFbEBs~1YA^KxDQfVYVGB_ghPPN#JFV_9)=#Z{3j^>BSs)ha&w2v5nn)@?`vzn7CrT#hvsl6_0`*>lkK27Z4^S_TK*34DIlS96`Q=yk@H-Y(DdRXlH`QZC2?RL;QlFJbNH2G6%hCk<ZbMud2&B3yjJVOAQsSIaD!$;s$~BeR<G>vXE1QX2i+8e;zxU%x<)%j=7SrI*Trz5c7$AnxN!i2LUmt&%p2XK~*z6y|yXV*lc!E#H=RU$#Bh^CiFD7rj1QKJ%<>*BOHT|7Y)AVr|*l>!6yCnl-Cdt;b$_?Z>(I_iz8s#rYG*#&JYM<Itc34O;Y|1wsM>0ZRl(oX9375Xs7eG>CaP2q6)ofCNY&1p!h-7YRXwhLr{uAR7}|1d!;_2y=|_&3df0_Uqhx&$$WbYU|v+*Q!;kYSx_J{2t>QW5I&vm&d!sw>(3wbT*x=Z@@jRyXCGwtR=BiaBnB>nogTujn-d$YX0~_&}?y=-bQ;3y+0q)HRygtWVJ%vuSx9Ov+7=}y3TKY-GbwX3cMIG)z=ny>EAB!(o*0hyi(wab(&e@B?9YwUEn1MoJYbcZ@Mn=Lft8@)t%ZaHODIIQby_tU8evf&Pvf`Xhe5}Nd<h=nW#%g4HCi%m%2`!;gwO?cuf^De{yN3f3f-VEJ2o^-_xWr<9Z;jfU?g-7<lTs07@77Z5#)*7jUAvybHNi9|J2jkGyJ1&4mNo$I4tLIjS{C;9nlu`4j4inERNU2UU_WdBaw?G-7QW0Ku6b3?tEc!QkjPat}1SbrE9p@pZs*u<|9kEI5c;e5#K))d=b-TwBk#fLy$xfRs0V*!+l(<K0KQsSyo|=x-TzY)W7~wB;-D!0HvhE7BtbK$B>8p`V4P?Ea)#guU}W`t{&^<rX^DX4kBAn2WScLo$`MFgF>XTVv5)K!fP9q#=z%yP&QD;tbYZ1p<Y36fe^1inhEvu!+$qqzUN<E;vK_$>Hw=JHbgXs3Y)|T9AP!9|(HeWZ)v%0HS6RZ(U7Tfv_npaW}|IJXXfJva~h}n5dT49y_|zvZ<Ci)m{`ayk^2h!oN^vyeF;@@x<@O6in~<h)(6!;*k#rIL`6{)r~OwNhOv9)oZ~Km}neXurE^zGtwVor2Y|%U$NnvV)K36!h9tHy^2B1Th84cbZ4Fxv%K54&@4mOR4OCdgw~VK4~<H|&jwae%c|(mkW>~AR)W~xI@r}>*Vyw!48{O^Nd3pgs^STNN=;L0Sh2_oe1&nn5k}_;C?M3NC95$=S=Ikcq{oJx(?qtF`)x<Hg7CutBM|8)P3Zs2ru&Ycc%i?Blb(=+u2Sx$z4brY0<iueVXG#7MuCiN8#HiNXB3TzO-qD5s_6#z$tMul#)NHU(S768s5Uj=I5kUf&Y8!<Hk?F}xahQI2&Kw0d;q^@M(663Km!gghW&5cz64^{F~Z}F*>9sY=9D830p_SDD6$hA$~N)J;TYAihJAHw*eplWD*4Qc)ux4<c0Ym5Mn{P47WXyx?C_as!KB8vTr|oB3hi-Y&CS%p<GZPUhpU|jhcvj3L3j>+FKkA1e7EV#6C9|Q=bBwpCIXiDYCjbBul7R|0W6LWoQ|zGb3oYRC*2;)m;UCrh#|Y`(!r#!T)GfV5m7y4d{zrES((Ma;4HvoeRb@psR|T#dA)@x_7#&VZ#gaTWaSK5`zL!F8yfsZcrrtRNZdPte32ZN6ZPnXC#zsG3!DWPDvoAsq*3oUmj(2YhnFS}(iNC&*6*8qyZ#!UY~XIPp^M>2$Zn9bScxFHc0sl2AU;Xf&1OQCktNfdJl|U?VDz@vpaqQxymA@0Pf2xRL76|-%{qOYutei_A9>FH#A`tB!!^)*_Y&xRd?V<+*y2dgI}Km4RDALTy+`i<KOhf*CZrJWUsc3=yg<AYcIAH>3k`P>mq2$$^nr=MORRgWSa)&jPC)me!yR1$-OF+4Z_Z3RUSQoFvF=9NUhbts1LTZ#M_gH~8&#AEdT*Zwy>|wB7g_6!d*=l+%(=w9H_kpn=zF|?zO(DvD`pb<JulGjiRgE3PC&nBq2J+&Tm`^~{Q~`-7wGrj$t?j2nMA+;Y&l74zEr+viGJtJ-c%vzSHR%$EoVshc#edxlDK&5yMc%QwND=Rx3a0zCgEO){?YAwE&5l&F4uj+TMpn#0zlz-v;=@vDV8~a#2f(4@nVy>rt`}1dX)xnmIlyPA%Hbz@ukiyJM-C!L81X&*tBPawc2y*uB8N|{_3V}gW<lPa|27Y*Am<f1aVrzonMbMk|Y0d)qDl<uu!R_4cIN4n(M|^uHoi`^q(<JqO-c1a@pd<_$Oc0I8g5Rp$VtrPV$#`pcW@y`1*h4wsMbAQJa{T!pX^tQaPPyFxbF5!Z(0xhn~5{6wlFu_JD)&JnyY|G0Jtmhq*0}bjt@aK3FharkG;~o@Y3omNlSTM_z0mbF?B384$|Z*wx|Hvy82xjAv$JRbcxejQ*agw0=Gk&-w3r?XdkMzPtyM1Madco^8NhHr|_4CbA^|;17&nahZ>9tAV-qsdg=}$r+3gp$dVtM;}{<7BF@gb`Q?qm#G#MY=nEv!V(@J(0mN>&dHpX!w&Sw+6R1lIbk}v18=VXKVHpp@N()wG1ts;;OBtL6XD|6MTdY(-KS+Q4QCVwPEEHsNsG)5p~_A+#A+m0;w*AkbaY!8WyZNEIOi$ggwou3wLxg}G&DP0TXeRRjl5+dkG`)(UZk2jurNEbB1G1plI1egG#ZG9&!R^V2^d=+z4B4Cx~_&`;YtD$u1#?_;2=1~WoGmSKQ**iMCK>$0~12<i}psr-K{O3Ne%3hof6obUxKXDnzGTSAx}!V{^U<#O|9T&;{MtGBq+RxmYcSjpidcsg|9xihqL>pdpP0F?%DNw&7)Nt=kda$y?x1}{Q~v{H`1*=+Q>nU*F4%(J=(bTXj4}r`0E}m_Iq}3y63w$&)nJQPT}S5&F+oen@T%<k1lL_+J%izyReZiYzIc8XBs$Rg73I$pYP$MeKJQDJ*6O1x%6dU?Zq;;_zFkXR@D<-o!C-8wj=vnwr$YTe4sCTO<X0IXSQ}{5oE(=P5JEN9hQA?r$(k$?ab!UhBb9g*?daqA1Zr}<A#wkJiI*lwZWJVz^oK&VQUgyDNl*p(t*8gu<Oj_6^p!q|2bE<ECmAR%%`+Udvw?b7nzUDl*!cc&YiMV#+7K1Zc1`ol(b$-b$~blKC5;D)1PtjL8Y?6tQk4FkmqP_DojZwt+AP!=|KE2xvHMMgm>IlOxNYG$lRUn5L3=BHE8R07LI+|X1X#dU)M~>c?7P8T>jnhl^b?RMo#B4JIjpj8}_Rb&$L6)hn@-+f9DKx<VF6ec1huZm<~^DltY6VXPJ>8*%Oo3fO)5Cc2L7}8^nfX4;E@FRXWXyP{aD;27Y9UGG<0ND|pNVaek^#lj}>ytLL;$UH!NPiOSHinGR)<+B-(n&V)3wydk~+gUXoHV{z)_LaVh}{H)n+IykF>&Z{d^ODO@Q1-->wb`mQw>0a1Y=Ig<(GTrem-1Js6b(YN?d=$(Hk7|B(VLLUo)%G+e;v#+{Z}#l&c(B4ZJmoSUINzrW@arStC)Tz#UW{k0-04QbBH79vRT~L!)9DF%x41`ppt#MG-ITRDYAdpbJ`d?U&c|}6L*q>e$4ynV+S4bWnMkY^e8CA8>AV#?zW={8uWU=*fJ-pkgq`S8vyB;+&I7J!g6BnHGXgrhF(iHLgAxWrl*!F7lD(J}{l_{h+3{OmY?&w^)djx2<7$`>D<`p0XG8SzEjFF9*hUhKMj)JqC={wLh500m1{t{1kB;<t>@9S`)=Aok#|4ki^33!<U7XU+I-!iO89@_Jvai!Z_lsL#nwke={v~^{p4LKdt!B1Mx;D+9Wo};6h|QX@Hh{Lv8<b%%i=>sKn4(x{9Gn+t;}o^!Yl#3`DD8ZtESx1sOz{u6%hjW?tFp_p3m|#N6!`_Q&G}}1*ZOR=HygYDkpH6+u#Z2<((NOs=Uv%Z@km)sMCo>%;`bia+a#tzE=D>VB`^kk0<7?ziCBdS$-@&U4$8nHY!fy+pR@dKG2fxkjq*67^(>#A7Ato?slI(^V&@Mmo8%20XIxB)@zHSW^$`^>HQnfta_@F+UyInSuSHtC1?)n`j7y0RA2BWb|H#<FYfdtho!X@71%Qyp(q4)TMQox6z_=;}8Atmf)K8;5BKGJ9ugeJadICcnx(d!h7H2?C)A?fR4d4k?UcI`CwP<h%id^`3arU}a;7z>+x0+=lmpLh>ZH-}ZFrt{>`WDlzV03&k-MVYP2F5CoGV@B7^$D02Ik^Toain%=*ZI|!`PFa@W0ltV)u1$j@~h0pa=M#GtU6rlY7uVsOwBD7(yCi$R{e`eE1QS<6v&$lpCJ~Qg=gA(DJ53t^cu`+yM$SxPCfHI9A3rufUnzsS}*mFHh;;DzqfgO<WetRcZ-RZ9z#FzgwZ>>J%xd^L7Q7LqRKUANGO`uvW0!0#w8U~*8))~?EMiCs5suwOf$Yd<V>O%qhuuwY&mSCMNQ;RRYe&5Fd>fI8hV~B-5Xb1BA|UN=C3F9D*b-g$ve_2`$qP0e_&G3S`RS%{arKh&(gex@hG6RP}7)!`3AtMXm|uWcsyeM4#C)ZNOu*|9`hoa^0R%*c;xKk+|RT;<2Mb(yg;H%k?eCyp)eM5;;+Q8=k%|ldY`KId{7H2n2<B!ROdV}I8Uw05NqNq4@@-{18DLLkQr++CR|kPQ)g9>Hu`0`zFnA!p%RF)Tu)}$rz`gDQw%VBSd*T(N;Q9&Lrf?MjDk{_Oe|dqS_!6_ko!jw8j(S&1i81J50)~4MZh{_fP72XpGB{&zr{rx0!GQ0&a8t>1EboHXB|TO*FF-^q*>EPTI<3>+BTi<ZWCh4=QV3lIbpvB5eE=#8gUVIM?*fFtu~v|I1?8UYoaPNo^3a=79q8*X*&trhU69?;u`9<j9%o`wliyyfrvX}fcBSsMNeXf*;L}{2k!+*-hs+iq@dASPv9emPDFIf#)FjFCgv^CRvl?=joQ*(!3AF}`RzXKR`rY1Wb{Az^<b+oKUO|UXSE|>Ryi3uL$11W<f?cnX&evm1+E}h&-t*8*YpCpI+I~_;}W?_n;QwrRPnhj6W`d+#z>~hB;(cSVqw2dTnz?W1sQsaBVFz*TJ?VM@TIRD46s_J|LH*FcMOCh(c;_+I~3x-^yYyd!Bu}9FPvT+c#At@c>BPYk?y&Mmjh3@wm%>HI`CM6UwiBiSiAA{V-MH$bz}dZ+t?qS|K6*a;cuTYxlhzgQSfy;Pg;2YRKc_k|Ix<@jOs7SqvH%fwR-4CGFBS5JXJptnEGysIQ1ZyJg0(3mZlNuDwzyxqPktdN*&q#;(^@0ZbFmNFNqWPyJINfl`^f^(U3M3GTP6X<}Xo9dLqp{T65hB2)Y4qB7aPKxOJQw>8GEb7pl;u&@~rK&Ijba%o{i12cGTbi3#FNI9~a>u`yMmH1Emtd<pY>u>cFqXFI0XxbaL|u1z2D09GI~-AYMoa~?G$B&%5FwkfySxJ{i?l<MegS~07`4Bmug?g;R4PJ$2<v0%uZWi&(+M`tfkKAf{a6*@P!wYJO5o+0792<loQIud3v_vHGi4dFt}MK#tYZ0UKW)$L!w;^Pd0wsiZdcfjkjQ<jvxcRWQ$tPQjHjd>y>x2x(>&agiOVU_vYfzGVcTUrFZX3CkI)LR|J%Q^4V3N45<`xj=Pb<XD6-Nl;YKU*KMCa^J99~CY={Ps8O#eP`WMVl4eHy3$DqJS?MI8l`&tK9^Nivr=XR6f-Ws}#$yfKJD!q0=dgcD#{qI)kRUTMo|V?;12ceeY|cFcj+VG645NlYocUS;Cd%oMgg{Zru=ft$Nrh5W_SlF0E`c%_f4mT2WZLj>1k?qOj#Gw!QdM24cVcZPviS8Y|e|t7_osH3e{U))1}q>jF4{owWv@utctu!PnE-%HZ5)hIp+8&YdK&YDsIjD26{<3HMVad}{0b&`NkqOw76%zNmzAYuc)XgnmeEX?e09-mYi#om&^feIp^L=j!3>@a+?m%l>Ddc``rqWPaut{QT$V5&q2L_<4{&Q)Pap%KS`~`I*u2Gganis?6_tOyNGWWqu;I%<mRerrtf{$pnb-37*U;=`DC6g+A0fNl}quYq)0BAbb=-3^MU!1zviAJeW2OOxieO(F9;@CN?zEMYfz8k!BMXOp-!ogcZl*#G)xml@-@zHod1M#iEeu;?Hc-%*W_2Xc#Y<Ew8*Auh2H4mv_qBpWTIf;V#a8n2Ix??>t1k1m}f-Gbrr*?p3nN1%>8(awBy-zepo)SzO*3i)P~ts&Iw1vci(jh%|*vB-53D6P>1CGiqMaX)Yh`8F}U<8|vzS<@sH0%QjL?<_PtaGXdl?siu2|WAl;*aAq&O;MjbEV6zg^KEqV$U*fU+AhONt6qn(GXmQ2g$k~34jq?hN<Ey{=jQR69?oIzJ_hvXh^EAlUuj<2?Cof1iFW<dNp{WaAvqu^q<~hBjzs})#^~`Ug5_OB)G-jI%e$E#j>+5++$NF%e;o)3ThWhL8>a7J^Dba_QES>(jKc`{8!oBIIf17ZXr8AtR#{Y2hZ@LuFJ5b)={D@hYxQDXZ2u;Gq^n)dt#$Uz`yamytus^Wte-lAnfK9Tzc!10wKpjvTrrs6%O;7=f{saUBisV_<1-8keq%SFAVqjBjwk*FNMH$Vut9|z428|Tr)ac8p%DWqoi;cv__&tzyqFEBf#up@GK#|mwei0hWZlpSUIy9N>CL0!A2C+y)w%!02j*4Cu1VGSTkh%amr)nmfdY#a<xOkx6Sek15DOlUN{aftNZ+uk3ECHQS{&kzyAh*2gaJ_Jr$wH9VY*|4hkSpm$tC1OJ7V4$v#j<P--WA8l8tg=gI&)^3N@*hUz(;}huh)J9@lfy(<(jlt%D*eZEWq-gL*V+S5V#ee&n6Lq(ZdXbkiQP%kMczWI=CtaDqOKL+9+bD1uQ>SSpMc|SpG$&Od<64(*hm;(^vCk%$TnZJcW3y%Nc4-b6+%qW$oEB0Vb(d?HiS{R!GGlUNXGif$+nt=UogLZrg}Z$Fn=WCms$B(NnW#q+lRgYVeeV4$DL&icVkcbsoiG2@-oVB?RB_00IzLuqO`3S|rPqcyOliz0KT(RYh&QkS&SFp!L3?N+YqCJ*)WYO(+ws<;P7@vRpPTi`+j))Eic5Wr6d?>!U6*-l+~A(S;O<ViO_39UHl|Es$&hZM%{GF7y@oo#IENQXv2kC!sn#yDD+jW$hE<z~xM42J#hz{G;C;^0eGFX-%GXrWpPMK#<NA!@qi3F?`9N7At?+`<H~m(@H4(7366i%xTZ6gg?ccRyLZ~QB6qF;es|TKTVtF7o2HN6HdIEFzpGpwDfkiw3SvknUKCwsx-jj-aEUsPtTL~*S`z==&q8adG~=7>8`f#`S=1$`V4D%hD<Zgbm=RqwAnET>H+8VOjzj|PLr<m?(sH*=#`8pJ-mr1y{*u&1yQ=hnU_TAT_s9yUm{9>LkHgzuEHngO8>t<KDTjLa~tnEzW63?W90;!nc<i%p)W8TC(#?TG5@U$$NpJ{<3oi6$7dLhX^+rs_AI@zsEdm;J9+@L;|ui0H1J`@^m_A0)OUY{=U5#`sV9qN<vG65;;THz2`##><~iPw!2T(E;||;2$DPz6|3l4x;0Dslxp(jx1_e|Og#McoVCJCZzsE?Fxw(DN0EgB9uAzTG091nC{Vg_>^6?#-Swrtb2}Z-6Wp32yC8CqEkDu<%5qo?H;{y!AsgbU^m4eX}axVh`_Pmy7AR}Pd-;^cRcng7IcP~<gaCm6cH^u23hR68*Q`ocBwSO1(Jgj?c#LEwsfV)OThQyCQ{tq7z2|U?+^Gx?g>o%hDh$NBYPGrltSkb52KsL@~yva`<Eq{P@>zDl?>dS#E?8Nx4?i@KvIg9<@aQqBcMd**cfbAhn(9mx`r^OqI0(FbsM@=GZ@!<wn!T=r+$lIjMu)cc0%9ITsC>*bj-gf4wAxZRl9d^iB3T}#fhD**xh<Vtezw2&6(+pah#@yAr*X<^s7NQyc%tveV!uVBfi1vDiortoT4%s(i|M3%ZxCM-0pg7Zs2v0SA1!HZ<weKsg`@W+3zQA5lCsfA9m*^sujRUF+oj8M-t|(8K0XBl%&J4SpZv+5UBqH9c+k#Clq6F`(4`Nn}KyR5<32zoOInk(+LOwR)q=ZBKbM};e`l_E=oz#vU=NC;s@mkXlWJ37*;MR?}0ZEy;|CTX2o|RhNT<DJKumw$^Cl5)ISK3xJ0zMfDZos+NTYGJ6Y!~&k+bW~MV3rHm;IZT=n-BdOUu<UieT(KhJ`hw9^8;*qhn*j0U2-Yu7F+1(E$+``HJwNL6x3|KFOPPMK9}^p=1({OmTP|scZlwoGE%qb7mnWt^H$jbPDmXDf6tg5(G=3M<v#Zq<*<3MjfVs@P1iTAaj7V`;Msmw9t{5+7*lrWTL9y0;Qqn9m+Ls7fl+_U79di8VUCsI-mp<nwG0oZg{zGF3Ii|Bs5nw*u=9v(wfjR@D0^iM9QzUnXnBA@Nfk^iOn7~WEkH6-4&9NOLp4(`Kd>AFs`-vIS9^Xc92yaEd9jL@aXT1w1JpP;b=%CpN8?})Qq+OpgMHPkrW6C|eJ74&s|xFABp>+Hzg+wQth65>35!OncaEJeJWb>^K8E8XzQ4RMJi=8R2ENrchUD^CAYZ{S#dJbCAKhB4gdD3X%kZe>8-{y~`naH}7`Dtm4%|Dj%E2(vTYhUkEbqy~!kxzB8axJ^$#bS7I2`5mTP9Uhp{Ne;p!r<8O7Y4~ljxF3SHn-5KzG_`Ev9N~_>3zrma>hU|5o_mZpFJk5L%nK(_kNLgl<Fm01w|#EuNQ`EPG`YT|A;+d=(+FxQog(Khgvv9}v3oO2Ac@e^0JCo^Svi_prsH^o%abybN3L9{F7eHyqs~+T^t@>*~n30mcx#`v}iF9I#6k*Sk?HR=&Bv!F<}Id(B9)4>!J8*spYR7Tbh)<A0)(eS|8#$rL@_+66W8V)nP#s>*5o7qPi1cXr2xWO02XLg4b%{V|ZNh%=O5fv(jXOb{H;1(2|QIM?trg0*WKAizwlKiil8*lU@fA1$E6=DV*(Tq9T3^DVw`RFSW&r5?#)*V-gTS9A7Yd@V!XgO`tOj0nEUB_Cx9TGwv8=s3#XyMWaKLwsbtTbnrUHRPLe7);#`e=5Re`T-e6PHt3;+=hvEWowZQXc5A;OqT9^Q+9&k#)F2V#Zv663m(~)nYWl2H;n8$MN&t*oqM*%c{KInm?J1;ae5>@p|FHyc28?O?m~Yus$+Ge!gl`BYbQEmitd(LVw}w|%y)s48}F8pxW83M&6(lFK1)M*8@l@7J7GyYEJN|a%gTvX`@sU(9j!kqHg!v37IY`t6G(i)`nEHi0jDh=Jf4E~^cI_)KXnFnNb`!q#JxuYAZ|U};v}PKnc|wuG8mYjf20{1SiFPnW_|5&$9(`ae~l&=wb1Yt;Ey;4F@2Tu45ITGLhR}?&iJn54HijRTD!9u|Bn_2XSk|`6&Urf916C~09v&pl%L`;##~+>un&b$d5e@{D*n-)=b;%!R$|X^NvY^#@g`$}ei)UkT2fIxQn!lUJ8G31qB=TKyxge25QPziHqx*vV_*%gsIM}&mIY}-JOlrr-1|N9QBid3OhX_cHo{ACn)t;p80farAxa=R!KMZ-_Ra)j;MV>Ha{;%`|KNEqu)2Wd-`gv-Av~OpmTXgBZ|Oatm(T6eHEJ<<ETKIzX+Fh*WpQn4R#NCA=gNvaqM;wpiv;IR{9Z=%2VN9<hsDe6P`XTFALo{1-l52L;cUAscb!?<k*S-+^dz1(T?JT=$h-}_TFXJQDYpT;W9yJfAG83_gE)3j4#SlvoU^UTnJt>jXKHi(TRhW9X3exUc-zGL?wKg<Xi_%RsvMc)8iN&mPDj>JS(qxWT)B(XF{*2sY(ZS;!r$|Jm1ksZv8?jEt5u${R(aAl#3`Q3j9`_gT+bKRsyri@4$iAQW3BR}Wt9gJG73H4<Axf55rD5vM-Mk^wH_9F@8fyJhbnngH>?#OJbY(k>?VrwR)UefTU38qtW)*<gNC#`-uO%nNVAps|1wWU6@$uMFx$6O(is^n?qQ;tEbuTHFL01McUy%4o@65TIP?2@UrSXTx2_OHrX*D%QeSC_h7T_Z>r_^9eEfQ;sKMCYJ8MdPft%b?>SY8F62}ES`Koy2UGHn<Xej4r@rY0G>qza`zu%Gi(LX)QmHrf?sf<a~G08e3cO+d}cKaRZKaXB=qAuRlBp%IN_lPq2o{FU<>f15R(N)n>K!LUdS^(O^g{V~iNsbY&p}1&*UX-zc0_g$tP>~UHJem0}@80ov=wBX87!=jk+n~UeseeDlrr4YIz|Eh>i*>i`uw9i)$&y&jC{)3btf$Q*3Y(d}ps(A0c@*8q^BB7)#ah5Fv=Oy$z*eQYL)q;i0olSc-O<pL{dnW>FX&Ut6fFM^gwklY$HXn30?r<{(R5rrcfB&e9WslM@@t(1Y-$|O9&`g-x)J_o8A}ME$C`A^Y%R##1lWL%JphL3p8M1Wg#q!mO2z}Am8i-sBRA;*Z+y$LL?TfLYhTO^z|ev4on>!q`!PuO4Y^RIR9T2?4B98!yXcI5F;I_FkHy0Z^x6<*I7SAX<;4O1He8d8crr3(7JF&@ci+IQd`Dw(pigrHXNXmccoVH6B=!+(5Zp~fZ(MfdxVK${)e>0dATnd}ptK|Mxp=&xX~p#2deOg=j6xjDj`xW%yA`K2*S09O+YzqVt#2gsTfTG<azsC^d+hYP6S*&mWRa`Y7YL}{S{NQphqbYw#4~Z!DHT8rb~&;Ql|G$g*^=8jDrj$}Z&}ce^Q&8tIMb$eVfmIcWDJSzDV8z=g-et}+X(Mw`6+Wf7H7zI{5?53zWmj)uEyW<3PR!`j_(ZLg*kD=g`|7_8OS;e*O0mHyBbd_na5ch7<!K*gN6h0Pc?A@_Kxx?6!2QQHXW*iNNJV1wS#v~{~Tk|SCDr*_%2$iqd4^CYMIh^xo2sh_6In_mBH(3TZS6q384ob3B$%L?gRT*CP$44&k(vqpd+uJ15O1-1q+w~p*8s&F+&^W$<)}O-}}mu+>eAt)t(2^$zl;@@&+TJ96^liE4{oZM=Oi42!_i6%!4-GxQE)xiM_=XgrLuFtZG5ueQM#aA>ZyM@<nUSxDHIX<QNVMj^PzBf!!tHIc&lLuJ{cB6HqBw0~7iROb9Ol6K>ZE?h`8E?$x})pP23APc(ng$jOjj{T@BB2f_iIC2S8hVG9o6mO0xEGrB6y0&#>%Ju-csnZq3KEoYl*gA2jW%u+7Wu*i1a&HThcN0yJDn!P4?Ra(<D95MsVGVof{ba#fkMhbQlUGWKuY0lRq9ZOOaaX(4nz+QB8%ko`q5fGiHa;^7`H7L}+UQ4HpAjP+?HRD<%Wbz)4%+w??Q5}nCN#l?o)B+_!wSdf3BLxUf^Z)Wg_ydoqUA|mF)?4J!m*{)>#+{$I8!_FVWVgC85}{dSZCNrN4B<hR$I2o&knxSH6v0zV7Quvbu2=+FGCF4w6l&8~7Qs$iyE!J?uwK{)fi?&|!HTW@S2K|yIeh#YoS|g$#&xtQdBX*~Gj+u~g`0l8dUf*vVHolBd-48CsdwO_4IdGB{Kvno`tO1eP4!<K$(-d(^y%rbU*r1J=DMo<=JT?zaea<ffHWD}2~99EY>J#9YogD5LG)?Cq_{qNBiy}8^m*WsiAp<oM7R9xy}w&>eQx;V*Ib`B(Nr^-3x?Pww$Wez@E!h{{)A3-t80SZ%J41em0b{i>M0%X;<qI!jriJ@Ku)qO>P5Qvf;B;(m4!EEduX>;+{z2t0EhHsH<5t?F}~_R!2aKIw~W9bs;4J8lV4?Zqfy1OlWE|_KJDJwUm;d@SBRCXc6X>8UO^2B^6L2!V8v@sf;Vojz_f#Qcz7m#74a5zS4O){C12*GVEuoSUm{<o6i{(R>#nXX9d<$f@ki}R_*ZQ|{~3mQ_l<!YbO{fvKOp6XjeS2=V()|W9?KM`jyY<rD&)9|!1BacjVEP^++A&}ODvt1FY2wu17TklAnQ&I0+?-jWz=ppI_3*;FbRSUx5W!UE>@U-)oGdOuD%9~^hZw2K_|S!87MHp<Kdjp#h^77*MJH#xojIF$Arrwp@QkYoIn=5)1DPiiOZnib6}_)=93^aQ!%G;kG04%KB9Q0sIq05YGAeuA_V{AYvXn>zajZ#iKw1`w$$s97aHn|cUrX8RwtD>d8$x6ZsCwiZIEn?LUO4_v(f^UNEgy108ZGcxC$C;4r@@#=qcoqh<ouANMdh*b^Fqbt};-rhQ*Cfb(spUKeC?al?b4|i}MzKOYw($K<zNKj&i{)WedWgtKqtChuTA`rB5%K!I%y(683szQ-9x7ZLV0Qz48+$pR~VJHw{&fOJxlHVnL9eQJfAir7|58tI*j{@4^n4<-6)(fI{0IX|aZK7F<Eb5ZjzJ>@OH=tK1R>?T@?_2OwqH63`+~z7Le=&;~@t)H@bo<amu}`q<MyuZ|}Cg<>WScL+%j0?)E_rf)23eM=K-Zxu^;3{>raunNM58$+WgKy=J?moK`{PH+Lt?h_2wNbFT@>z8TucSkWz6TU#RLat&X0Elq%@xhKtTu87XZ-=Fm)vyj<Huw#R-lY=|-Qx&ofSHeSo}-}<RwnmX-Yh3|OY5ZA^;m_Zl$qNwOG8({w4}B;+eBrOg^So=!lCA9Z34w?q8mndhMlrQ#Ir=I<8ZU39%?!5(f851!UCUURFh-FYvV`{0lA=ZF=hC66jo_>d;|QJA!nD8M5T<88TwaTZRLyNXtH{B14mW_QFpniR#F`z*eDa7Ski`hA2+?_6u3#)Dk^anB$7S}-tqY`>s4L_qOA?UaFTR@UZ(GRywA{MVj6&b6#ueAh`|NchRuI1XU@{v@AwQ)(q5+<*W&3NS;yXmI0odX1r;LkD)0<7xs4}=daGb#51a+O%v@8h0jUt>Pa;HtT{O1Xj@W4CrI;>;8wU(pxwp<p++9Tv#SZGzt#XSUBe2dg;W#){ijUwWc7m0|)J<sBGKWf7L=ff%$poq+%G2i))3vL*evQt9Jwlmq9A=<hlP<&ogbbtRAdV6x?Y)|oC7GxviF@}p{hcwws+~|Oboz47INvMf*Qgg#y9wut9a)owGQ~{sIVBD`nY7JF5R8U2DvXl~PB2+Bw$++~nYA5OJxLa7n2=}Fe%rCPy!*B?e9!hEm8adiZy?FH|2j#&g?`wRxxKT*-lQDHhtmc{1gu5Rv4B78KAKvQRhIEn9+?lds}Vt1MFi_SpTWdl$nzPEFS8_KrC;Uwm<eE>ZxIws3g{O>!EhZf{;4y3{}}2E<x%{w>`*Lv9!eNW(gL}j>Lw~1ehVb>!#&-{vVlMejLuS7PY-x3KL*JjdS)AdiHavzf`zcb#9^Z+fTTOg64HVDp0ARS)HT27Tylr92{&J=&{>|)BX;}mmBVhd31Bep%h0!CS12YbFoA=P5Qvj`^VMNtAMN+YyGGdLvbBzP#i7J5*$G*`gY8E)@g5JPcn56&M5H*=qnc3YbYOA(+$sb28m!I)*FIax6{Q`YM`^Di+I|huj=Lr<Alm5yqV2Ciw9^8john58KwuuS(*sdASuEPhw7^G*gMoR<HlHe7I})xf`L;~B_QBK7oAii;)yB#Q>ft(6xc2d%`^Lty{Om4<b6`ruVb>37VGJW(zB-VB>BusWVZqK|ELqGR3i2gwpKt@bvv;-AvW}kz5UJ^u-=GbOhuUqhg;i~9B7dMZ8R_@Esnwyqz*@}^A#fDc&0=8P3HMH8)e8cB3gj+lb0bDnFptLn^WWkG9fa=UaK`InsYw~;f#keA*rfF9Nf{QCvbRZT*yl7ZCMAvK#k|A=Y0*ZY(FOdp4y_V-BD?Tm8eI<U#!D0gwq+jL=%j-=oFu$O5an`ci%I;0-;uT7*I`aGn}{v{P?vvuInwHI6dl2&ezx&xK%z}QXt6ypYg%UQhFNni_M?@EF`Tik_gH6YFX+{4mi+H({?Mx;&Ko#2nfW|qMvj562<6%^x9i$HAZ!rgimn|b!NymRi2&@Ne6Vd10pZ26p`>Ec`FrF?S~wKBr=8DmKwIcHBdOgn_DPg#mfh&k9fqXl*rQ1az(l4eU0dElxg26(#Xs;kveT)`HEeW+<@S81{<6%s$_YdHDUmBs5*>0Mp#uPwQg1-I0LGhGG-;`K(SyMQdtApV2`->VsiI{k<&U`Vc=NnK{pdtj7)KFVEb~ZXlqW=q<XGmzfztG47*nTGy3#C?OvFPtI7^brA@h~ssdc8;gI%;^s0Lc2WkShxoMw%BQ)q6etq2IE0*b`Z&0d=h9Ph0c)}@h-qqK)i@LcB%UfMTFayf}hfLw_>tEimHi%0ruphb}c@vJmmQzeA6u;^hr-9f1MptzGE4=>wW@FN%!yNBc~npnAAEfwjhQ&)A}`zgVt!??aiubfm<#dm7-WNp+Y5kJY%qfvO$`k8g(#j=C`5FMj-<4LZ_l)HH)x}%!HYF4`L(>W(mddZR72!tOl5B5`945!UqJ*~6U*7BSt3qIXWoDZIU>{MI|Y8Vuiipg{OT1mAt3s3JZDZG@x%uJS;b~)2~<;Cy+;bPJASy+EZuw{%pR*W9u31gKM2dM8DwYAs*Qbopg&T=#f-NBKGPb!}Ug4fHNJ=n6al}G5&l%LG*$pg<|ST<IiT5sgH(%&hex6bBisuK6YDBu_?or(S2ZLl`F@<pAjyA^#X$tDF=ZrA|efQHME?j;yx-G}B(;3%@dApUNNYxl^2NzsZG6T)%0u+Y&~HM<f1cE}L+kBDwye{Y+ULpc%oiC=iO>-kz4^3<gE%C2c*W^6$1YxQx5eb0#=Cf3%|V0A}hI|ALn&N26W-f@atHh0ZQIn+8%TQr#aMC2Z45cf+6&<qr$DbC5>8-{-r#b>0nxJqa2exb#m8^!Xy@7+{@B;VJ@m1n#2UJV~xHFK2LkG`L}<jbezQq#E~BWFZ8&53wRUoJyJM&)FIpfZ?`-9P-=KBJ#Rny4?6{>~Mz<E}ivdj)E^Oa$$B-W&$Ne0_d|JGLYD4VK{z2Hp!D0IVJ2g2PFSAe<Rx$nP8Ayc_?B{T%H;gOc9t+54U&o7!!2KogkvCm7%Fu_>VZezZJyOc*={G7rsxXng4EAnn2LLKA+pJWRR5TRP}uHA1lSXJ0o37nq4l$BkJZ_--5ajb3&_tM)3{#fdh9D|#^<Ya4W#vZFVz)Gq}W*}pY%MiSy?Xo;@LE!>(UG;rn1k}h+Ol*OYwlHnvecqA=5*kJGi`f9bb4J5(h`IIul`Ju*yA0Sc*r^{-gh^qoZw=uOv?kYj76)=fo?UrX5eY@y~-js)OPy-R7L#b}H2JoAwEN1_|^Ja#G-_f+AEB<bGV-E@&@WG9z<_-#+;zO{M80Vbn+wtKj6N8&5Pc0I@Fmgjx%Rl#T;SXvw#t70^{B|qgzc|qdVihPfR>~3~rPG05L156{o7R;Qj`R}nl{8vzE|^7YARnn>SbyN7?0KXZ(9j_~qNS{u@B=?`P=%2QnXvd^R!Y>6+s4%Fm|9OX>Sd(vCN@G<p4bE?$TFkP#_kcd%bI6rqTwWA$bsVMQQy&cYqm#Q*DLFr2wLcuMl@vy?!#%Ivx+K5h~_|I7*IH!z{;wu5$a{N!p0av0sP2lm<V&f65^mCm`I{3n8|zzIGn0xc7lu(9h@X7M{!4GzjH0CF_CAY=H7~%wX&(|UhP_{B%(%`lZ+m_mNJ#Kj^_F*&umSA)HpQ<DVvJgM6gU(D(p#nR|}epI_9DjXmelQpdho%xemdyarSS0R}4=?XiUB(Np<pcuv`67kB{>OFi2{^<~Tc(VbZ~zOPlBCaVyUg)y`mIl+}0D?YPw|om|t2;M%GicC#*+_gg*T`N7o$q*bWBJ-bDzmws{<FQOjYVqocBde_uywWW9M2A98>bevy!s`|x95U00r&VS9UVVP_{@x-=elCW!u?6UH2*7=5;3(lv$?pXnC1Uv0+EWnI3MZ?m6+RH)3U1xSzMK%J`b21v!N?M8+Rs63a!Rn2Y^Ntin$7~B;oaj1oV=Nu&7y@}OE0iq4i0wle&22Y{OCrERXdTt?g|to}eT1MsFwKk+m(r{vBtU7fHO7JxMTZmGW}TUMF3^B1+>vx0qKOg~6fr_n9xt>vWaV`h`Ndy&Qz0FF#x0wSZxHM!@!g_h7dAJw2(U-%Ha1ueT^+XA-&J}HAz@YJMwSur>Uaa@N%7|AS`Q(QY!hz?(IDT_yK<YOzwaAmF<TB^+xz1NJm2Df->`^uH~{da_;W`fYS{WOn2K=~sGZAf!j=x%#N@3f6Hn}5ZOYj(+4P9}I&6?NW>C$c4I1E(w#+N3vtGfydi;UlD$`FVSr;z;XImi$mYCmKX6v{ab#JM(p~AOd0$zgcf>LS=uw7>&uc)*IG)(xZ(#8rL5_jsQ<?|vNskh?Ugtuz}lAFMGqOUOtSWD$q&a@>T8e0@5O0=yrQY|N#da?!{8qwe?aiCMz6>_m$=iJPdhpdMhLs~zB=M5W~J5Ztx+?O(o=g^PlmM66iN#3d$D}nBo-J7wJp=qc|=7hB^GBo%#Q$;N_8`U+OfpDKf+U3@o)s3D~PA9o)%YAJ=CerS!tBt_JwMO9ajg7$Dw>JW#f$(X%*PnFYX*g>H{;6dnaBVbSF}~tO|NBFe6D&@ro>MgfdpBF!XQ^K!*LG-LW`FI;{)(??g@!n1e^oA=4Zm1rYXVrM0D=@@&uC!T2YuP?OYTF_1TI>AuX4b4;(%=l8oMBXjn5Lm#!3L2o+E(eaJ+&5wj%-T?ivAX`&#zb^VZ#b-nu)7DDT5}qkH!knm-T#z}X?o<MA(=zx@{>ax*RW?oSRp`Uvg;4aFvLkIf~XDw_o-FN!NnxmZ!o8()cku<4e7+9GTb`9hScvzVcLIGl{zLvVx9)QtuET#&;M6YIr4bkCk#5P@jN!YdT5G3lD&&S*5V2_O}pMXE?hE3xMS=h>ZDj%!Rve!QDtDmck_5_yTmfIC9oV!c678+x!aj<*Q<fg-zex`s%KL|g_Ngm<@OKxFm_r+RyOrHt#%wLO;(<#nPt`n6yvbxT~!S$c)u>d`hz3Am6Eu$Ih5DiFjuw<2_#C058;h-N|7jFG`%ZY9iJ24zkutD<T#33GZI<Bb=66&HFS0L_ES)qFRCyw!sem{WBm4q+}2{0n|=&i7p_a~4XV9RpoVkr5smCKLha@$M|WqC}v<M_R@a%k&D^kbnJaxl3<CC0(i}AUPH)VR3zcA0U~KC%uGg`r=u*ttINgjCM4#ooh~$IEU6evXj%qPWT0nV5{K5e5Jvd-Qj5DIQvTe8DEK78`>s|hb2eJ&yJFJb`z#t-gZ|Ur9gz0V+y;KyVO-*i7A-P=B1W|?^KK7U;SEh^J^-4d=qoiYi=r?c&_C^ynAGM{$g%+S6z8dll<hYG=CB!)*5s!t|w-+eMf$LotW{dSxJ6e&B{E_%CvOft;7q&#gp?9ld-z*ozlHFCE-47pPiBnxR<lioz2RjiI(}IaqL(zD~A5BzM1#{rB>RJ%paw3CQo;wKVZqodFibfMUChj2h}2LkylmnA*&j06?4lnnd3;(T+|Wq3{h+kb2`hkgj99o4q+f$YMa%Pt4*A#<DksGjlOPiDo-S^Hz}C;i>$^SD7=WAb0hT?$vaIoWj9M*SZ3_<^;W4)DivC3IIgpE^<S&cvRv;f?SdVgn+f;lLUZ;N>ZV<u)~j2L{;buJ<6QW*JmI1;PV9kYO%)qNUr%0NFLU{4{=zp2%_qGAp!s^Y92VJb)Tu<vH94>#yAi8ah(Ij~JEgKO&5*}D5#mZk!4?9GOs*yw1w;_|I#n`yU;LF44EB^#j8^T(gn|PH7XqM6)te&6yH#5ag_+>3@R_2prTT}r%DlUx136*tr9%b&a;7fpyFn0X%ioqS@6eZoVucmzIbkP593vT)nP5a6xdq3aC`X)Vz?AaOY}^PzLVgAePfYh(eZo@9{x5&6t>j(P-=4?2<jv>zYZKX!E`LjBR3NPuj|f2h5^-iSWBBH=nG4YHv3szdalfD^Ke8uUy_H@K3vSOk%i|z=8qOM1Sm4$WD(Y~V>q(7N3_%BT(~!8X7+5g14#cwd{Olv!rQv<-@sS=?8}b6)p<$Km$~FIz$Z@ej1bi3FdKZ7aW#;8QgWAmmVQwkXm2C@H(anE+t)*Z4wwws~5p|>Mf=%D*L|EIc(#n?}L}IRQShU@O+whwEph%66cka1G7{Z?0?rP8N!fQaC6OKc-b{yiF<G_p`oBogwoO}nr@E!UO_8sV|(s#i5N9}88z5{l;Yk9x)r0>wucTj08K9l-`G8(zt={V4jV3X}AMDNF%hJW#!+*5X>SXMM?H48dG+*4Y$a%oTL)qGDzV(4*6=3>2}kYPdMaOJPv1_+-G{TCH<Xhca&>8z)os&d$F$^mXq08QkdnIH#xxF)(AStj)c;EHbU@9HYgj-x7oQ@@r+D$2RJ8!4zf$?mIi9mRy9pUGJZ*|htF1zBU+80i3We-wiszl+`zxrs-La`ZT?mBudveQT6t0Tv7!=&Gb1NbOKnsOZ=vo~m2NM5Qcpz3YFY7@hvIH;fdfCHz0}=jhoU2G+ueU5<66bi3*b>nezh$TCcN^vd0^VJz~TWfO(PL2|1+7UbNGxr7KTG-I>W)>}qn<S{4%<tFY$HwswUhQ90&CzzN40Q|(W&t|a5uB{xT!ommJl7LW{J@s^zpPoMMK&B>>BDNwcItClI=LDm;HbOeDM2VbZS~MLHtR`+aKT~dLME6w5y%aj*;(Kp0Gfq_sQol$xuVT}Dl>=qW<urLE^nqVG{r;z#e~N8;CwNQ#(E(KPh@>F-%!A+KRB%4-xnE#6v4i=<P;g0Xlt*gtPP+gj4rb1VyU0YpVK|SBKMr@5o`?*;Y@nyje1PLnPPjX=DoAYAsgYuJ$oJr!u3X;6Zo>pOa)hZ8d=vOo?gM$m@{M==3Ub$z5}jW?avt|~Htg6Vij&A?9z^wfU+Ybk<AyjjRvqs}b73jWzEOhE_}0V3Gp-~k5oMm2L0AVFIqxTZBC-oW++~t=wuFfI$`LmInK!2xZ%_!jvXk!=K`v5^6XgweqCDppjq>I^zi8F)Reo_#a0%J?=+#A=d6r`Axy(SS$t+`Av0G@k!HO;Ko~IZCixH7U_GWh7%O<&v;#sRH#z7O>=tG%A1Z_>v)ma>kAuFxei1V|f_#xZW1M1E6Vhp=QWa5TxZi(&t*xtbtXh8m9_U(MP&M$&(^<Vksu>EkS4!LP}%6q_rDOc1c=45^7nXx&v28KmtsS~yz*K62*gf)S+od_2ys}b0<I7*;Csp`-{0EG%y%s&n$BMiV@*>!;TmJK!nY0EIa1yLd<y*}P$foBnvmJ9C09gap!I69rRA)-%y6yFK4x8)0ZJR-VBL>f868{xTiNWXY64mkkvJDS=KjR57o&>hf$MAWOr093^&ue;yJMMX$-xGDSCufHKB@=nn6x+A`ehiI|~WM`Z~*E^=i4X*D&tQ^JsK+~?iS|SrzDJHi@GMAgZ<7y3MIwC~F=VavvM7dM>7Aa!1K<3o+g?he|U_6GiBZU}%*W?|HQ?6r$O=@FJi8S&y7DrkF!IVq|=T}XXvNmo@0MEpMJHzi6OcXw@FjOwiSsGVK8<s$QZ*2=s><vV*IPcA*69hgpPKG$=SoGDQ3Z<{oAknN+Anq(om@E4(W0o_XO_f@wbjmr$rTrTwfW5EJVorHAg46_SreMm&3s|tY$0*2NeZ~3T^-JFvF%>W=FA-C*msr|F;kq`_GsIM!p4|m86_7g%F`_7d_;n>BQ(P`9>_UmCTN6|16%tdSNa@3KGDJgdW7`NCzPX}7l$F?zRd?vlsC+(VA?Uh9=2|%W>*!-PZk24m=umgHLtQO!ZXuuTYS-a)49&G#5I7XliiR?+YC%^DLC=9^27zV>wPs<@&5^TFQW50NJ)%Kc-Y?_>InHV;djc`@Jl*6)8+!Z>6oMj9k8MIHdf--qplZ(;inQ3${^2s9vDlDbW&@Lv2Cwpq2@*9>G2k)|X%{T!kYp0vWd<+V9N@?{@sR|M`0N%E1MG2w?|qQb1Dp*JK#8mTQSG}((F~kEJE&Osd-QP86+`zt&REXy1%Q1qK_vx}2bq74Vz1(^6kCH5mM<wz@;l-S(ji1~A-Hl{47?Z<N}R%+C~icPg=!>zL#3$Lnj#2`h;EcniPy>fA=`r;%GhnmV-e}JM}+IesBN>UQcAdeLnGKDoIo_GY=W<x!Rf!~8e3XHtxIwQ?3c6GKmYk*e|{d%Z~M>BBm8-U|MvLv^H6*q<WKXb|7QO5AMo+?mUq*)a@k+^&yVCte4eP^(x3kP-So|UQTjZvZ~1I|_Rlwc_WwTv>)qG-(|<#MrdR(-5WF=Y=+EU<>Cfq1_l7@Lzq?ocUK6eqxD8YO^{Ic^>!r`8EAQ49ufF^AzyA8aF-hXJcA5tJ(;LN^(@*2(-|J^<6)~)f@Ab#JmWAj`l~BixOgs$8eDzAS?5re=>?jC=f)c`#+i`Paw0@AS>l%Z2PNdt?YzX#?H7JI~PnAHmf}s#m>mTF(iT0<zUA?P%<7@uBJbyF4>nrhI)o&F}z^y+b-H^q_+nLk)OUa6^A*yZY9HJW~F-^W=9=gRaT2*d(Wp$B&)!CKTd$Aj=m(-Yl;-ob`T_g!Vo7Ip;<J}Q3*OX17U9(;A7AoT88gHx*f4V|-mM-tYUpdAt51YPvaYtyZn=a%0q1c~p{fhpaUNqg{)pv!tB6I|!RWzh<Bat>zz8dwm{*A$S2WkPT(VwtL^)3Bg%SVm9wfOh!&*i_(6CZj0UFVvoemVR2l`}iLS~HbFPqrSf9%~SBEpE`A-|W@zaxdM>@_?r<_?4s47@BE$D)J$nJ(|^hUAdiR`AnDprumweulqVHY}y1j{V0&E<vun2Tis8uOh40Sr#W`@gv-OGUsf06pS-VYZ`Ep~fBR@$z8hE9Grd0jBCypn7k2hVv%@wIf@urd&b1sFe{BH$#S>Ys+=)fQUA*EKi`OlAAnKp)tg7*kpxhSSSjlzs-o=j9i=Yx4e@TEeWc1d>`v(Kupic0B;=~<`4N$~sAkxZ>lT}2H+@T5kdsy+`4RjIFfe$EMZutA-ga4rjl^+0Icyvv^H$Aqmh|z@KR4m#N+(ttSej6#4XNP{r)-~_QRKDRJdjkr{u#2G61e5%O6+#BOKbun^d4u=&tXl%~;|A_sn_HRxDm+dHXDoZmA4A1w@6wMEeNt}m$4K|UTF;TtxwL6UXr;z>6E<1+Z%PhP2UBGo5&e=dfEY>vhhj6HOh^oMO9InKmJeXr!Ilb`WYVpF<OJPO@gekhE+@V+o|+9nVd&iUs1p<Q#4SNOWEpLxwWgykA9VuqbsZyh#Nu;oN7qpvklF)+^*|dIcYL625;hp83H}hoqk)#AJrS0UL|;L8c_3!XcOAG;TXw{4*l96lR2?^Dd6Pii)G3|+hE;!egx9}7w8XmagsR#TOVVD^9#7Zg#K;*WzsQR6#&7DR4PD{V6JM6j5SB7yPT2l&0$&jxlBO0<>5VlPBwE?{LvmI8%4oN@LN6|(lbEt__MUDb^@i-*>90Of4?d8`+gE}lmnu>bEj6kKvxBRyz-%zbO2W!|@T5Q}m>cT;o+9vQTNVh8t>5ecGP-4}3bRj0r1i13frqt#ndEpK*c7^28y@L(cTvazvfmC;yTf?y8vo^@LL8SB;$ZZRR9PVNowPM8;=k2|{rJ`5Kk;TPi8yjDp$n|vKZPYpGnV8kkfct}@*wu0L!jWHfFwpC6GecmR;$)ndIwF$Jqz@cra&tt4oRKOSdy`doP`UKv%P>M;sy*eoWyj_cAO{+M9G2Oh=NAAzVSWEx|=c=M)ZJp#FbnMo^95GXOW1KTOmq*=}jz;fh>=GOH;g^HReU}I1c2ku(5}c-|beMdSkds@yJYBIG2_KxHDQ8W+Lrk9>q*#tG$vt`qY8JLF0WSb_bKAv*qoGfDC{xic6NXE!<N?OXOs*C?2v2AbZi=(K_+Q-$od4G^|vhI&PLu$vv9{S*h;{%~IriQ0z27GpiGCOl5o=7L1R_zw&i^U%JYL^J4o`eK_SUV0to4qAVL!fy>5R_MAx`(yx1;C><i4S{{u&YSqW>;Af~C3bEu^TcHRO-wLV2luf*Bg`$ZDV>otHszqkVZV_iqO`mcLC$OfYXN8E6Vh;KiPUF40p~mKzjNwp3T$JgW8(h^H)uS_tq?`dgS80K*iDVIt3(E;Mn${rIpSC~B{daHXSA51`j*_!`LO+zMPrC~A>fNFt>QX;cyE=91#X-pSgvA;*R5c!yfOzVX%BiBNgH|$npAx{dM$-a-7CBm+yQU&4=oe3iC+ta+>5L|`oUf182NeZ}okT@<ScJ0DgAkwO(CD<(gO++Fbg0^JY1*8nL+UxRIzxYwUJA_@D+v+O_Ni(5R#U8*sUI#|`GxrFKQ)3&EG&J9KMMN^VE-eQ7TmjsDl_<%>Gg5;g|eRD)84tPL|&N}ClIcU2J|h~o}F=+SjM~(Z>1>aM?#DD)b3)BgFtzK6s{sr(eO{*8IBYw*fvKeXC9hYq_@LT7n;jgE*5_)c5c$i;+f!V_h?}N5AA_|UU?ST8C?omdT*_1UNnIErDX=QT(+J=u8sA|Y^FOSPAup7F(zKIS09^Dwa2`*rSn^k9K*KCSKM-n86>cgTGXRQlSMGfPyTx{T-+!%wQ`<&_baCC{G>TJ;}~q4c5gj4uTd19Tqpo|`6<^L6A>u~ZShnjDA9b?|M#<*aLTFn;)~p}2i+Sz>tK{q=KLoq${M|?<=c(ck!!<Auc+q#qqD*fy5haH8;ifS@-)Isw3gwg50|Wu$de!c5GRmmnED#$*7nvLvm15DK!`7%a9)6t2C)LP>jzB{iJYKpY~UXx7B%UMD3G8rfQo;;Dk7SUYUPq-UNhDqa8<BLzF^l(()Bgn5vIhxt8A3gU^Nn8$Xh!%5z;Hs-Rj1V{%DPxN_scRc;hFkcn@EukvQZElL|pyvT|F*0T+|hr?s51<jXWMfz__+)#(PzWB(ED-GBcfyXrGiHiwH{bz(tsWlJS5d$Nty)pZlY6MHMmEom@)8)X3&+pERO>TvMqtxF6~#LM4HtsAYARARPBy2HAtV!y4t)x}mzKd220)O6brxzCJ@<mk9rvwM|#7R!B>&aPP52Uhstj<*dPjU~Nal{K9-hZ#FpMGD7jfbH8iv707lkd9`U2}$th@pUvgn@_s8hJSYU^1uJ7<$c<vw$IbTKK@+KC(2}OP0xpXjD8c*)fG1e&%Y;80eZ8{b&^h!#6+q5b0Rl{?HM(lu|@yZM!Z<2<l}D`f#jiSgNY;swq*Zlq#d2>%GUS&>)mQSDf0Wr5bl_hkKB3>n80iZrru%sy_cdq(@^^+Nct8l!u2fS^_{w!@pS{2)qA)6!Tf(uv4z2@Vv7ZWC0yR+b62}QozhT(^z3bvM-n%VAPE6UYL-~{pt=-T166#Z*lA$M%Ip*qR6o+hVgyoMxh=GOC;~y|!r&-$ov<GcbWm>tH7l}{)B>~mexFr$^>@YY-r@{*-i_?b>)To?4wYYGOLuxtx-_``c>PB_DEoV9z1_oy8!B^n_;c1sAIaN$|LR_PPLdX~a3n83u*?};GXDo{O9>SGjeJ6B_Et?#!?&03-$8n_*iQ8Jm2ucqj$mNy%Ul?k)L|2Tk_(buF*BrpliW08=ES$qPf4m5R~f!GzRO<X*vurdLo=fXF_JJ=$bzxO>n)~@9}!2BFSEAIO0~QlL3_a78a02SG)X>^27C+5HGpW4U(sf_X{DXZfMtMgYO;Df?iAhHE$J+n7i5aaMQ@tkD4RK}O9!%HW$kIje*DcBnht$!I_wq#M9A((^@3t-T4zhZS9zR3AVi)z$t3ORef=eRW8Lnk)l2D7H%oWY!KQ?1?d|oRkpgqRjgi$v<i30f|Dd6UT}Cm8Cu43!J8;w3IA_%Ml1Pwdy$R1sHE8lutX{nlv2|lC-}Ps10d%XD$0dJ~_iiE!cYc=lS@=T16m?uxw>G8ITBw@cShw_`?6X$n^48ODw>h1#ev#J&xJ4_Wlddlh&QqJFRqXBj%<a^BH$L_Ab6)%_T6$>oOkI+z?_D)eV&DfG(ox_KvBJ7Z$8}Z~k_)QYLb@Jz>MHfRp9tU=v{i25$v0$hkFe>Lv&z{y;gf~KA5{Bud{J}ddre@*qrb;OLK^Ypq*guNJ5>~nyPNH7Ovqsn4>VqB$1^r^^9|Dqox>Y8^8_ROIYPf4Lumy*^x>PV%RzE+Wp>|UB^)ZsCY`*b6q2Rc;DEW?GBKTw=~-s$8EK>BcCy@sNJJ5iM2M+9j{FvB+?21-Ww#O-^N+pNw-R~R#|8I6{0CkwTZ3=tA307B96S&maL$zHcaK&r3MMmlf_$jEDK~mYT1IC#9dAMSMjB4Pq4>AMmP_aEWb|clJRi9oKzbCN|4!Q@y_D|0kvIn1$DBVl{g?JYNY~)N|AI6Hn;qF}8~#`G;J$SJ_65(Qd^$f$-NL;uKlIk#ix|J*FVnxq^Ur)4(qN5JSMNc?TRsTS&bPLp-nVW?=85ujCl@4|Qv!d2yu=J7dQe=^5jpon!SuUv@(kWH&6m+j%N<f3`(*mnmj9l4U0tWB__L_vKw`$!9*x*RNFm&m&n7@bs)VzoUfZY_`Vj5l9mCl7639%{USgd~6==_YF%Fe}nZm(tA8}z@sS@b`JB;u0gJL;;Z-U|_kYLJ>FK)RhY=Tp4@Lp_R=={UGoGG|A2@Fe*pl7v3(1<er97bGKajH@@aS|{26}*cgqZpOzW!N*-NKRS8%yhIOneb8=1NoL^4AUVQev`F7a%D=<?3bV9Qa*tPKZ;2Cp%L2RD=1Y}Xce<gs1F?7$U>NqRwFr~Ef2-cM<y`f1C?0yR36I?C8`*!{ZTaUkbs-XnRTjaG?JJ{cv!lhbW=lDGhZb8QAe$hM*;LE2qF2c?%-^R!DROibV@2L$D@?)@#tG|qcCnk;!J#Ncb1jIf(N^@g@K_lADek=lnC3~%5LF<6q8f4L@b7U((g`+4|;UHGMG)x29O&Wcm1m$=oL>c@s1WGkZI$_1e|7ncyfk!LA_hWau2SeED{Ctz=7(;QJaj}ke*)|=?ynD(sk5ZtiG}HWTEoxNhPC>M=LqpZxUCfjYPz#6i?BgB(GS6fF10oGJVd{KbECJ3`?@ba?D0WS`kH2;7DF)d1;^P*&@G}{t06<c)-l@8w#>A6}llwh8#S2-Z*>7W>8(x#B^C`37X^zo-ZrG$qr1?%CEtFb=(MO<|4l;{KwxwltZf2*G4%9)pX~ly6gDZA&U+M!(Nk8QO>3jAsFW$2VmrW2z5dh)XFtwCHh2A#$t@K1YkKBR4gq6ofafx!+`#OKD35fV_+&w95e_qnK#Wxff-bu52Kb6(4?jY1=zVnSyV<4H|S?>$sm>}DUDKY2!ZN2GlnfN%v_?ly(TiD>=}3yQ;Xs1#4V-=7+eJ{8-2H_5(Y8pg^83>cxm36Ah4lNuF6k^8cJZ+NHr+vs*1V%Pi8qv<@(>zlAK7x)<Tg|6QQRl<)NpbOvi)w&XN+o8lUpw7qQz~IixJ44bV4^VtOtMyh<@+@q>ZTq9+<DxPe9!Ff$Q_h{u2=1F1$B6ci&bobl2+ai9P;md(HRl!nMo0U5T<FvTcRz2omuu;L(3+}HI3zSl@eMX6^+y-V0joB-tBTPm2bNHXR(9^+@pS@;~XCef|Vql+{x6ga5JNgB5s&rlDJrqLx_SKTDxolHp%3!&|T=!z#j-e5Fn#=pf2GXSGQS}JFWq>|A@Z|&S0IgL%BaE_uEQdZc)aBxl*woPwIBg|NFLKM&^cvHExkNZVLM=35+=2=i3ASB`Q-dOWMXjKV#BlQ!=rNvRF(WxT97N0wl$8f$%Yo#eTOoEb&p|YtYG%yw|AvP9#8sVQY2&n+lPaiRQA0r3Wol0+f5k^iQtW%?M2l+W<oqnd+Ra{2%1F!M3pHyz=U#8%e<)p!{Vs*vIK2G6!uwABE-$h&qiY>2jaRF1*?Wae-)>cy~(?Vza-ud5!=I_E%&L6k%z803IE2&uqXZ%Qh!H;w<)3#_J(aOo@Buig-aU*V?b&G%fJRya0`sFu>Z^3!BXe{3$AuDcC)>^RTjR*QKa$CxZJz$TxL3ufN+eZE2-Y^OyrLeJ#Pm3^^!HCv#1Z}3@-Km&?J+TCeL$P*yE9wGs;#f?U<9H*Xq(DVeY`CB^+gtwvYhhyG&<8<9@|ChHuF~%bGjUTqb~`7_rnnubRowVfSFYLh<T7caVTf_>H~b1=8YL3x?VPzcf!iI6j$Ssx+Y>I{<mQI^*QG$$FE)RPChSWP2;({2p}v>jq4t~}IR>Z3o<{keBX6s95C^%N+~YV}(OOjAAXU^aX>^F3DDutM;cFPt;XM`GwBK^@9>osyU_vSfQ$JydX*Kf7Y$9IIJHriltM9l|i8zlO9#^Rec_r<Eepc;_DO=WVTQ*S%>A=nbOi-M(Et7#Ad6`KoNm4yWLP@@I8|CkY+MBW)bRGslh~QCU?<AL2rZ(v*Yr4*A?C!)6EVx%@83@7%Un|joh;;w9ECW&u{om3l23AGR^9#b635lr*%M?RTioD|+^9viM36x*xUX@>P)MAFnR$4qY$ItqjW$-m^s{Q4CO?+I>G9cqUCmLwD3@+S>4*Xd{DWOY0Euqx#$JJhdg2)#Xa4Z*iyC9U}g4nn?lz$Tdkm->mv#88CDNJDf<)-f#F%ME_aX`h5q!QDXe}i&h&-A$`Z~@j~Xb9XiAyXu3JxfxwTsW%cPkUyn%ZptU+ncc@hWf9s_H4`ih<3>0rL!jlMWho?waL(8h6TJhLohx<03eB0Z6r*QSWevXW|4*(x$apc0gq^=E>m*CE|iDW6}K)?Pdx%1DC#lPlgrbV*0Q)S2d>or_qF*>nVUx<gR_~T@(u6X=WI}>4N5iHIh&!LuVB+MMecRUwP6vqQQ8?=oPliw{nM7H%%t55mI##o>+3wXM46#5t1hxc@!S#-agi}EA}xr)D$dLh+0vi0M8aDMi^gdM`^fH>{flOZasQ5y&RxIAZjxve-`kp*AWgj~NA`^1-WyfzY<B|f&ZafjFucOz+*B1K5aR8vofJfDXXZw#%*{CfQlR=zXK_OOubMv;;=AB~gbVhO9X(r0y_H9?V-_=q*c&)#+z~g{vC!-(Qb&O~t78FA9paufXlg;hb?Vqa7AzY&c^|P1>3*(XBa$j_ZEZuzL0a!He8tRAx)f7vRO#l?5NSL8$-qBCU6OeUrZXJb@W8g35#5$KCZl%bM+O3=u{w5w)&dOC0_(=277doFs)6vVAg{-|lk6A)<B2y@`p$=qqz#mC;Lg=p@sXsj4AGM$yaPKqYOELCx~<)Jfs!Wx6sgtNf{Ea4rRtp8Q_Fr)%-K{<p!On$B3jt0s%;R#sF$>k{?BH_mYkcBz63@xTkW<A?%@hgVk`I~Zz~Crjy`;kR=2OHYa>K;CC2GlV7u>p-e4P2=ftS2P-yb4VJ0nMw08pmilaA|M-f5ZA|01K8Bo#e<PHXUtP<s0K=(7zkHT6~ZotJVk*9i^SLaMH$jBJ|2nd%j5ztD>a&tJ5%$MQ#DH!iqq)xaG$e_m!9zBpH2{XOC_z=t-fFkpV?f6D3A0l{GfhU2#%YVRz`3qNO@vD5|SVy-w$NTk2-=LX{9UAUFfzmq+n7$H6<(k31P+WcODFZ%*U|_h_)9|&}f}N$+VDpxH&WsXrYOn=nBabYaA<{-1_~ok^p{q#Al4LP`?Z)epP`2!GdFl*Ix1820F&*Jzv>eg$T@brLgPkKv!hq;yd>{lmV!_1X;{W5{wUKMJ-JOpdhRwHD>=#}Snct0}OE1SP)iG14cf&Co*JI`vV^+TXSVsC*WV<$C?H$?zGdHfVfkJBh&J7q>D4HBD2W+SVCY)uc0~WuD0o!oEu1vB!&agUW;mhXVf3s)`b1p6I8p;M8Jy%JmJRqAh7d*6$ZoOK7hMpQ19W}J}@c7kYIv5=WY!h}U$Vno-y>*uUc1NyApzpC~wY^k(2{jEUZ)kT2zQVvF+`SCLrD7lg2LNVeRe?Mxem`>_omeF*2Ybs*m^9&&$q6boE}?MBc574e6@3(9O<|^*MN7*Zo+pymRJdwELdtOhO7T><x;EIL8MlqAJ^H9yxhmxX<QV1UkS-Q!2se8!K;-4yx|x!Joz%NZ<o{1^Ag3<_a1-{-JB3{sAK`uM#7|FMAY8sl$zdZ0wCv#3C#!DnIrSL4syxZc5Ny9u1)7dEYc(q&yOfRNe8DU4siD*O3cTh@iG#D<e&^O_7zH1~s%niZz|VSjN=Vlf=|GQ`sb~@ra7(pg+%nrbBdOw&uf2Rr5L^75$8~HFosZ!t<xtPC;@7w2v7b}IHNnjBY~8uUA5UHdPbb7$Ug!<RnINB<w4u@~Vcx`*GGP!4c1^k)FvmDw2Ft7qq3)+AHRsn!=v+DSQ%#~v1#!B;P`UZpf8xnk6gsw$!4m&7uZ15y5Kdi8?>#)+G85WeGgO>F@8x_G*>?lvbXHjRAgC3wSW%uj+SZgy-c^d4bZ^<k127fxV*I1gU8u7NHH;nG(1oQ|w!j}yYdI10j=6t>3*dT3)|pui65bmw%YP;4DvqR{sTM!tRoEvdfP}B`H;*$ro1xUMZl#`7E{Uo`*d2K>{{)t|{L7zW!sWh}F?&<bF(fD=pfK*@*mEOPb@|||VWJ}74)3_y+00co!TpIe4jDCFwxlwAC}Gx}icQSRQi5BfULyPNk4A%la^cC8h{{m?cscnE#u6g&BL#v23fo_ZKOtjvWx{Ll6?g0`W|XhDjA8;b-8c!-CSctF=|nn`5<~ch9ihKADeEtsAgR(A#lQBd9un)@eT9<tWgCeQC)P>gHi;6`>Yr((X*H{A&vg82?OWh}auDD)1XHoaED3_Au%!g5D^>$^nqJWh<D6XWDxq$Q_j5~0pb#mQQEOvKX75ih9rU@kM0pMQ#2vS(Xy{<axI=C~3+&3~)@IILP0H*r@hFs7lL_s9<XrEkJ`-+tT{kHa)o2mDE(jFcZY5#o*kn?!;Eu&)Q(@+6*=$T8<w^d1Cl|mUTBR^PX@^M}kRQ4~Pw=9N41-$>aa&9GFj&58!;NADh`TxY_;=;9`7|9%wPh2AMkGgVQ|4NSQdDkHxZQ>_Bf{9q^Yt>VWt#sTla1vh)f{glTGHd5@K@$6)Pxxss+MUsQhoAg;MmI9WA!}v-&>`8V`UbIlujM-teH*n{`Yes$|)wSCls$MSDiro8Ieg3_IRtdmf-hF*0cSuteBxI>mvxJlsJh-_S~UupH3uPpcW%Nk+6v8X`to^I|_>DLNg>rD9NrlchV;5sY8VVAQouZDRxA@W%3nuY_@T5@9@iyN6Ru`MzfsXvIAQB#e2H>L^cpDY;GT1`_>YG@jZJ_Tm?&Jrb>tjMKTC2V>kfnKe-iApDXU}`@!#{X_X90i(q}Ssj>?{OZ!t5?(y#LWN%*?7Rs=M)W)A>r2b`Nf~S%tHr*YTj^G~!)%)=E<-UICn=Lp<u(0%uSacJ&AC)FOLf}(nc#9H@?i=oyf%6^NtM`FCJ0ZR|texKyte65TOePUBtvr6?x3T{I+?CepFOk+;wNC#Itd;Mpe*7*R_6!r)@?2)*u)}zxIvNaanc+|%4&G6&-uNAeh|WyhjaBZmD#w)wCo&-N8Zb(;QCG6!79ES<u5M?!5py3t>rO_yrn>H-_Ftoha)NWTtIU$>m@XTrZ`CX&7`S9Hu$_ck6=16xX;s-#Yc^U=&@>I477q?J@F_l&HY8O{XpZl#9U@jeyH+3f>LZ-soRXdnUiI>Orz~Zpl&-H5e&RjMf3o?vQ4-1(8Iu0~VyA$<VRDz|tgGQn`Tb`IY^8IZcdi{g<Uu-TvavhjZz)KYrrX^(<ZHeB8lqi~UgL^bjn2+)2ilD+$QQ8hC~tXhW%Y8UryZ7SW*C+jj<rGydw(3jdeXABq2;^fdmqY-7@?Jzh`8i<VC4h7faW)r_296>jDB&TQS)BxoaN(f+1z_V?3vuadcPqt&6JMgm6WfLQNxif$&Oe=!=K)1r(QK**uU%lhUquvK>nz?QG4fq^o?{tcf|sPyr<K&S#++qZZ}9jiVo#<+8;D4dTWVZ5zyoeo=z5h*31=4{U}sYEUTR%Hp9F_vr>^7cq%_hNI4|4a}|cB%D3;UkdzpQ%6aZb$OgM5wn1c6$>nWOjwjyxJ8#gB;npW98P=@oEm+Acqe$AHkZ%oHar%3kzwFvaJOcl~PKS3KYW{SO%x>0y$3~qR+#eo6;{u&57vn>-!yVY~qb<)UF->e2`YbyvrdJLUtbVjk7YD-#s*LUdGwZRuxTDA13jC-hJ2%NdVPON+%2o8$YkZyIqxd?xYoPqKnZ2AOFUP6DP6bOD-PzZ9UwxhSs;^THz);MN&U-mJofz1j^K#NFy&RAEI(W1ipSd_}+lC)--M@*ib8bQ~2%tN6aq<%`j{KXJ{*5g&FUk#p4e8&INKfo~E$v*pba5<yMlUB!RJ0UmyYA~?^98N$^S%y42>Ci)@pY~^I?!BywTttjf8+I8Idh-hzxnNNOQ8L#@Ej-VEIbF=1d*OOYCV$kYhooT!EQoBuLZj(OIGbU79vfly*1%EdDzY(`AS~J)NRU*p&|XUAD(l(sa^4`^$QgU7l%3Mju|e}iU9n4;Cz<-pScE$MQCR(g;v^`jf4S>RDtO<&3ZM33gAn)az$6RoXgu;lg=FM1newlE@vwmiv<!6N*2o*QvS?N*m0S%K#hznR*e%HfmlU^-jv=1WQmHUWR{aI=BBg0rH-(t=ix-E=<Gi&yU}0%ta<iX^X#)C*XKV!kMQRa{yf5;)y_WrPybo!?7N~G_4&`wI%l7C&OYm${jH^QmOrY_*`!Ps-k?nO-4!{*jf}5RI5Yl+IO)DX=j;>+U@#yW6Ei4B3zFp}^B|fuVhKpL2C&Rh=_<HM=PXoclwbV$qE1*dNuxy*Hq$GU&Y1vYVR%y5jQOzZdTCb<UP_2{rnY4?uk}in$LQi;xCP%_RXZbFA$trRQ$874&v5PMOhB$OEX<N@IHWtj>y_GB<sd%4NIzfXd_r*?*Dob)p>kv-2PHh}OoPo`2(z6lw8fQ5*<#qebLUt7;w!5^-BOB-Al^KE3$kc7i&1l!(6aWCOOdlng|nr+(@NfKExvUoZ+2D9YpMJ7=67@Rfv0t|JlLdgb}nz`Y-hQuarMFX^5O?)ZL{{`0ADY7J;Kv3SI&QV+3wk!dP3yv^$KUQE&4@0G1CPvk6BKw<-IRobQjuY%WH7Y>X1G0u75`I&Fp-5VTk6_cF!r6T^BYxd$Hc{T9(X<!0@V=*;B79pGyVxHo;vIN1ne}U#T?T=Q3vh`)gs_sBZuXvg^q3Sza6o1_`Vp5N%gpL0=~6%{_6;&ICv7o7?F^2$M${lsI|;ibx@4@|RI!DKwQp`4XOOr57ozIMf6ygN4BE6%s7yIK(U(wtVr)Ux2+$phVSux(2MT=!DT#(73Bm=NTZ4TT@+caTr*SS0ta#8COGKHN`%z%bS@qM8SmGsv*pY_dz!sX^vtYE_4hm@ZJXOZz^!wEhs(IZGZtlkKGb_?d2<V;<{YYgjD1?9Glh65+yzZ!i^wA{OzO~_2(C6WT*TtUcaxmR&NK@(r$5nXXw*b-k&N`Yo-=a+Bmi|qv4^v|KEHFL;LL$rN%vO{7KytR#A6k)Qw)6X5eDH&dq+TTyw7Kn9Vu{Bp2=|Cg%(~BBV#kjiE=pB&8}^R!q(wz03#SbpD#+i3G}2XXI=u<JoVBnFeA=Vki|Dn+f3a6&Ndm7y1@aU*x$I#&hK{J~U%AbXC@5vz9d(s;tT8CBi~!nhc+|>i4Iv0P{`++VzbQklfGkJTabnbS)99_J9M9Cs7zqT!w)>C<bX8PeCYcGBA_H<W|@fg5|ut^fC-Etivh9i3G(W2pFH;r1WuTm}77Bfe=XnwB=qeBI-G~aM;@Qt495mp#eeAD3~?-$4pb1iYl05<AiLdhRFDUiB`VoV2umbuDvI|PR_PiQW1#&r5{pdI*gSN?I6MxFY1{_6xqYQeHM}0oh^RRC3>k}a=36i-_;fVZ7LgeZdM+d7dab2vx4AQHI1S{5E6(co)k1P!9fGS2UGosPm2tCl7@9vVQ^DrkQVFw#89|<X_2${@RP3aUw#sLtL1$sUazveHT5Y?`YxP~L2R;FAvX;{s%t~Wc{qvZ&wAZWb7)4>T8BYa4?lZrjM4OH%UkY-RyaBv(LJdSVz!-VZQqe-*r=h<TYfYH5y<{2JZ^38cau;#v4!`JItuv6;e-t$H<JV<@Ga$A@-0wdvC@6QB2bTkZN+AfhC8+N3y$J?GfWUS@+J)whKFX-IUi5WOobZ40K8zi04?ll4S(yK1P#g7naI=%I+WeHYLV&N8FWZCklbO<tC=}dyfgF=eNaOW@vR&u0MSDCE|4H3vgeS^ih>SN{i>ND&{2sgXE5f$zX%-)gd;gAo6Q|Ed~AcOJ^$>MGSHCt0EJq588n1zzKdcaaN6C9Q5Y-VT?$4VB=w0hk^`Mo^5gK@1Q7~s5#<uOmDWINiV?ge=YC}Z^TuxMFZe%Ne~Pu`=G>sjnh?SI5m`Xm|MNp+c8e!B=>zRKTiYjRt|WK!rQ~jBlNWl9rnGx5vzydN^{mpaKU3P3%=0y|-7#yPo6=^iJzN<y18bRGZ>pQIYV3|rYwQa5mf-!_1e{%1Y3$Yp$l+yy-4Z_{puQVOMe3L8x`vQWBEjd(Z37{r@i~EAFte!RaiOt$RL66~CWxVHrLkKDc4_R+SZwkYnO!W<{z7K=lL<$bFa0ZTi2m_7O5hs@MgKQWWf&&X$nw|Yarw@~HyE!s3d%j3$usDL)Uj!aiO9%)7G#JD!RMHD4*hBS21ZUJV(rGFOrz;ll<&<M6N_Qw>{c^BjiW4%kq0`8et;SwxXNv+6#)X>%%o~-Digu_=|gcK5LO41oA49OD0h1B7E{_tENo6MX7!-6t#+7?F=BYCkt)d02$)VqS6@LJ%>1qqo3ivUr*<b=*!chgHtpSzMa-%`I8(!z<io9l#Eq*;$&rMqpeXzmP^~4Gen_sz2a&9mN2jS_G!B>}Bb=kqGTk0UVMZWri?m#Z%LMZT$)IxeTTnln0csHzsb)cyQOGfgg9si<dG}x;PkH!{JRW<>zz@2ntoD05103$}gT0z!O*_eQvM+@jv?b3~;X#gE<sM8!&Jni6RED+bUs$J1=!NHbSiHmj744^3xZbKxgwvK656C@PH+yc3I~s)7jWu@LPq|df%V1befgSZ>m=C~bksFJKy2b5u+9DC<iM2B=XNNRMZ4$v5@c-?%C=l!Cy~*=&7k8p=OaSn|pkueEsSk!`zLGA<*6E+sacmirIhc~bHhPWM@s#=q$mxuxr$dnb?-j9FxlY`At}4Y^R3*=dH1yzopeBK7Xhq`=W#dDtT+yMn-+5B1)!ef9oZ_GcOI&u_L0)SLuexB!>AP1Tr~RiUVsyXo;acst@Kxsith3ov-1H98oXTRk=J`ggM)|8mcB)0A77blq&K+jk#-<I6UagvNJB~bl(W2!!sNS84v*Vd>ElMI?2bl%#N|-Z(moJ(oyNNC4Nheb+1AD#&LV@z+!!R=S=jQ$_IKc;hV~($VHt7l9qLuvg^KTyYiBsTm)Yp=(7<GC~uV{~ZV$>N5QO`~h(A<cc#7Vyz_(m?{VZ0c4Fle3)yoEL#`?8&4M}=-T1Kc|5)(m4^akupqw!|S+E!VKQ9B-~1H80hXF4q3^H=b=iJoENZGFqvD?#x}By!}wUeKV)og?`ooi5Ct(_<|$6<uu#X+Tv2~rrOmuFPJX%d_V;is*+QX&mS&qtkwgDB%7b_7-s2l4O$O$p(g!Y()yczt`6&;@b<Sg*U)FDH8xpYH(OoPpwE1&cw+6!;qPbji?emq6wC?@qOsNaIhSpsgQGJ}KDeZlvPVmCw+o-Yuepz<&)-HQ-219R2}NKM2PtIRUE1em<QhttE4fG6YQNxr0HENLc>D3^U#&CB?9-Xl=)n@TzD{Ak&>Z!`qufz#v^C{0HB`^CqbwqHRe3Zi%-S_mCM7wGJI!`POJ~I@K^m75q{abGHkpMGX{X4NDx|QrYN3kMq8%hdiF8@syEbE+MKz}N;g(twyzurGP81ujYZ?WCr_sap((y4NQsY-UlyBRb5GhvV_nSZa0Zvzx3^&Cytf8Md)kHZw_y!W0G4e(<f|fV|?;vlC_-5oX#IGH+h7#lVk&TC>S0tFlL+-UTAv~vz&?K<S_2&?cgvwKeilq#S`(U}TK*csXGI}<qdkNN3Vz1mtU{1910y<>90pDbW5QB7*%^?**`AO)M4rp+s9XK%o8YJ50`w@~<(xPlp%4#~&>6g<Dyd8f+{HDPFE;krV<f*LPGTq}A%4$8)k1o!~hEa_IPRNn|^^a}fi%~hV?vyxrn{}rU?AN#Mu3C5hb*y`bnft9+cL*uIWZhi_I^?%n_eD)3tm%B1p*i=vv7OEw=;2el-iVg}w{LgyE`z<Rlb0TyO<q+1!|Pm=h$77S<n^m8<O`FR8K7^%H6e+DCDJYG|KQ2nH>%9}++F%5Hf<-tq$<YJylUnKwX!2tI4s(2J8oiMJ~M4w;~xwpqKY<c;axj^_G8c4fA2%m5%NM#^M;rP>?kc|lT!|Y)giCbOYs=-RU08>;l(pd_DV7;ac5LfRumiDr&{WUZm9Hy!Pt`LgqtIV%IdECNEI+IGh~R!65zq$X&8V*Qd7ij*xu(!Lm~Q^5-7IvY$A6|qGDMlpo)>B<Q+xeHq$hrIsoq#i>Yf2D}`KE*T~%>**(Q8%Xi^oNNX)|A0%0*Tunmy$R_PU`HC&bN`1{^Y*_Kbl1gB>XO-R?^&EsVjE3=+n`s*H!Op}NgR2VP?qC0qCk+1roQ5hL5x`}^kVt{?%#U<=#^#p6M8^~#QA3R~Yt)A#ZJqYeq%>kkJ(y&f8*4~%jVBD32h2BC$DqJnAW#D1JyH!V^n!ws){a}V3{5X-!{{ipfM>pw4yF)fBo}ZLeAraTMX2~J5vxY>c$6c@*w9j7T-ymnRUYBC>4-rugMK##Zio$4+A*WD`aP&AK=o19`6&OUaJtR7pJE;M<;sVq9pwb6(1d(q8TPUK+leNGu26Y~zp6)<#M%3fk5N)}WT%Y`5snmo+)=YGMbf;q5s&c{$+G6+mbui8mv&&;BbbH*^9*cbi>aZMUnW6OUkP|ec6S_vP61tt@_J0eccdw&8#>T;OicXgc&<>ml2LFyY*MOPVuU)5fA;lL%&&E<Y#p2=FO5$al{v$#d&zi5NGD=xK}dr$WgzV&CE%=dD?V?r)_Q37fj}xUy9cM0WeLzuG98JuU4s552-Eo$J>7Z|Gc;wMcAG}zQ_`J?kb{6?V$@6og+tRyPf<E0gm^}7Tj4;@z6=XMMNRmH*Q#jUfHAcMY28V-lnPl6oR=hW3Hdf8Zxwx@hfbKiAT}DYlY@Mj&g-5#`R;B4KwzTpTEE*1JrI0lO)fV1@ia%0Wzdhk-))fV$VR}yV{Ty&Pw=GuA=38NI87XLWAA?->JH&{>-X6hDU->>YG;F3(2tehHu&=%%0hn3HQ1xXRg3-Ie?h3n5t|D(i{fI4ILULj|FYcdmIWo02-Vq80r+Pd-EX`NRGSxw+Lj^^SkfvdM0dmbQDsN=tlS8m8Hlm<upyiv6V+}ja1((DUJR|6vY;_x1&w6>ULfOCd8lFf@xj2_7w0#(sp4?t)(`{8(>Y^kO|234MshGq*pu8iCQ1{k#Dcjyr0^-9{ZVn023L81JwIzdY38<;6eAIeI+9U&4Kz&1%Id%r9rw*7K{x5r&465iPi2ZHRIhJlKWy>Ai+?AfJM6S5C@sJ1{Cng4d$IpN9_Dh6b!a$Y-AJUWrjfE@qX9tN^}E1_`dA6Oqm?Fw#^t6mU*W*=a!!>yIhvB{oP`$anh!rH;mogpt3gC!5RsowaTZ&*1EwL&aReMG=AY>Ur)be$%XG#?C`|P8wl><B*5o1-_BE6UH1CQgv_G@f773A1C=u47M6B8AIgTLUU>Qf?-9$)oC8Y{if(S+s9rGZqlrsoTs1by07IIMsWNpfs@AyHuBgqJMH{DBNLO|TndGJ6fQjltxGMI!cFn38Fs6@z3Il*R~xJ)DmI$5OqsRP{K{2btZ4shQR;Lg!)i=zEUpRhmwP1Zx#mAPUip*!whRhbj)cuic%R5qtut<2T39Ao9zROb3xnZv0k%Ca0x_~vS5Zbw0}ZZ6Kvl$9s``Eq4$Vya{zSe3b-gOgP(=TA4|JGxgtFfkGQfJmM?Bacx2D?j}m)Xz#pIPORd$@yIzCsW$%+zp5&!SV_~Bv!cLTPQI~Sb^X)TS}y}{9opB9!L=jU5e%%dCA)c4>6~N(*zOECi=ugU_S04M!j*(Eu#RTeYYU^MB)NzNJb?Il5YM;@#?ZpZWyPYa86HYYnUYXbS*YAPrsn7gz}tssp&hDYs1snBhUasB7i~@A^fAgHQd0R+>6`s*FN0Lb|tnX0tMZg@ONJ80+gG0e*f3zKbcwT$Y0y}tBAt&B)E2d`oz`Drlpx}W$mwQ{^_-5HuM|jc_J-XFkvEtlvv5SZ2ta+!DW(BmEa@$9(sy2yz^#4u}-k(ziPwZO+fwRyHEq4r+52!w%ZQ|Q#gGW;E4Z^Wgl+e4y`S_^!SOPwc%CJTGTf|mFi|_Z4zZRuAEEy8nm|M_l^MvT%C!>3Y&;eLTha@Dp^Ppc++Zl0bsj9-ehp5vwjA%%?7h&F;@_~x!2T7-0vB%ZMp#4?i2?8?FY8~2b;h7cQbRAXXNIG{`fZ@pNR&2jPBv-U+NF8@FC{%%ip=|NWT8#U;OzGCDoh0uYIdYCtlK{>GYZg*a(Lj4Wr~^E@mF79a0f{iGBs3LalX00MOzwZY<9PkSN%(;c}EowU5ro7Y0Y{CTiegRK6eRKTk<<d9NVQPZeWI80e1bvBsdGghQy9%hs7_Jmo4{X=j#e8`&ikg2b4|#{Yy2EitCZOCotuVlCiPhsf0L&Z#LqF)}zdkggd8T^*>X&eX(DKo%AXEn?+B8YlmM?7d5`EZdqLG+!|zA~W)_a^-sLbI(2Z{iu8EUQ9_v>-+%!0XHnUWe~0s6otSA22r+f31q-VpsI3}X&Bi8Y`Qc+G(aG?kY$x*Bxv9U0t##zKnKx4Ld-G7H{+3ywb$Nt_Sxr_^Jr_GwK5|kBWBFUH@|N@5Q%SLAxb755uZUQL;@xb!GA{94?J_rzn!w?yf0o-FnxS2!o2=q@LAzgN0)dEUo}M+sSoXsl^i4tE@B{?5aPOoUA%s#=vaaO<1m2x=@qv;NmP#(m<{}f;aJ)z+3#99(t$XI?Rh+M62;sGL{y30;;uY|j)38osa=Ox(4q%iS!v&IaR1x)C<|3yUxXPWofyjjpUUsIM7XHEAj5d5HJihR7=?u0bUESB#80ZZ&;8@5mSc|b;URwNp_||J4x1>rPseYvH$AS(lf`8AbAR6bu5W$}4oC_8hdZ=g;tG~~xIGM8k0-i9KaPg{Gc6GOe&CI=>;wpC<A>4Oj!B=qH?9nGKy;TE>ugZzik@hVd>Dw!X=qwck$>9P1tMB-Kznq)mduXGyCnFX7?mdtatNvtFCCs|__X|aU_y^yRPLZH$M0OLdPb0$efcapbaN#3c>|+_^3{*bzhjj>8X7vE2-O@7XH#O#oDeb*yn*C>X|eLB;<Pr9J1?({GGh0b6q?B$0?`!C`5mt?<EJl~GO=qi)U7xuU~?LSLUk9RP?_E^{*-2#I||>By}5C$`!JCnCLI|QV9L(+=)QtL+8T0%5jxE!z7NFNw-RzzVqWpD_ciL6A*ng`%e|1A<y&*(kRvaBKFn{yR}vb{JSZffpUJQyji1(c#V4WWB$T4$&d!eC5K^RArDd!lc4P%&GfSE3w=`x(my|c={N}5QxpKf;lO<B#-C3~V-PmZ{F9q5F5bK43AL&zV9l;!wYjV}s6men_8s!wWO4Wzb<G?}9_@&x1tK{QHM~fQmu=<P*I}?#o%ns_+rs?BM34<mf0qAdh1;vb5-%g?|gi4~EKq=j|n1?d?D*vX@kTA)*!q0*qL#cgv>5zZ$vkIU6f&f-u41D(E0IXPZ7Is!q{QIJ-PALs<LszvGFZhv@&%g2h#xpPH@;dcmzsm2O%VQ#MX+qO6a{_O}_7b;20L}?wk25qg@0mpJnP|o{V!qH(tYwk8i~G*3^wyeQ+G%sujkP5{XDbD=(iS(|JeL*yfPpfk@Nmv{IF2R+<77&+Ob3G|CHsCC(9-7TNfMElaJhsdDyIiMiVe4u2LuT8h9TX4Zyxi&C5V7un&*hTKawRoQj`N2>w!ZhIGwq?LX>Mc1{>h;6wB5d0nT%bD=vAULvIk8e3qO+eh%T27&QrpK^jOn;5#gsm(D$O;jTP^&aL=+IpCWeUmwD^J4^?1<f82=mqp<^+Cab&YrFUKjp25NMaH<gH=_@_sZ)xHwfbt6O+}J2A~%zSU;f8FQ23MY&H|sBx?b6xDcCW+8T+GJq=Xs)g;ASn9s!+%KQq#!olr82jns*yh{Q?Tb8EmgeGv+cpY>L?@LV!zLuwVb7viAgr}FF+2btrOu@^Nn^D3!x7?&|ob3#j_jgdYQO~NUTyjb$hqc`w-=^bei5Xt3rZl?A2$jD!gj3j{N?Ne1?)0<hQBXmyY)ZR|cNHSA-U{oFpbvg))?99d52?ZB*x|VT}!Xln3DoRT8z$$UkY9S!d&Z4Kl$4rtVi@tsem+tE-)4v!lwPPjRRfQ>6(ZrTF`a>Hxo!348P|}V*P}~$rJNlq;6KI~6^z44-Q0f1wb>58+-+DQ2S}ZW=wkGLfPNUXa@2dXP>ADh;vCp++!~hDynqnByq^tEHy9D!EGM-WLw(VVY6HSpqea0JHHDDeR0t>iCVtocZ&MKk4Dw~(x2c{6*5*Av=$qKtxD5_M>QDfK+6hl`#mMTa)LT3^9>VVl_@So<0iN29zGtUMX-$oIWU-_y^RQX4EyzE{h|44nX`{fV#5Y|)kH}mGtv$hXv_<5_JHhJ<F8++c;PN>0tB6YbWIE}TglTp<JC5U>pYh#UC=7M>1_KUWxr6FiOs})NVs{La3D_@-++_MMASwm(&O`gFDNVSwXYskE8$X=Do2z?<nWL`ET4|tD;3?~h_pEu+m`=T2%c8|5?HZSzN+FHzauJ)o6vXQp6h4Q?4%AyhbjnM`-em;2BB(wIoUo-~R-TSd6)C{#Vb+P;7AFu&hr1<7tC;00Fuvw12w=@Pmc%?m@?Al6`pqTjvjX@DQ^og)JX$c}s$Hw?)zszBEb!OrjF0{?wMpHPSmd=_-n~d5*v>BBsfZ7RlDXbZq@#P)Z)EPhBo7L~->E1e%UwcCHY@+ANUcPEYO<+fMMj5|fcmK~jV2#@n-KE?`7`Y}W`E)U+hqPZK9X}|f&`(MacNB1C7J)%>Qozg#GnX!6X^m9TCSPm5OasftHklJ(IbS2m=xE}(p>iEWH$9Hu!l1|0YJw&D4He4-ZEhI4N7nSpE-KFCf}C`KVM1-YyJXrwou9sRI+)+?ndit+TaUyZj&&Jqhk8!$>$V6{UlNkH!~uKmV@LH{0-t@fUkpGUqa{|F$bD0qT}fK*KI*+tPuaG0Npi+|oqQhKRL1E`^)Bjo&FtW5hg&y>LBH3JgeuXyycnk4={YISg=im%mSzZXJzX}dMuIl`wRskVnVd1<24TL#VqbQ`9k8uBeyP|ELX3OTyD8gme&7G@tB4GDC}%2k$Cx;Pr%-x2USUzOxx>x~REZ8zH*2X7jR7|*g)(DcyhAIb3>820u1TJfGQPx-FwqRee+n%ZFq5`qaJAIN8*n7LP@BzXwh!D#)RPSQNGPMQd}I0P%Zh@ttq8>^=V2ABg&Hf*#spmlk~fy0@+ltgp%<F{3Ua`F-J{l)b)DeE>5_18hXSTwcb=gEgnu`@({g0l!tm}&0EHb2&l9@dx7d;4e#`5WYeL$Pw`}^{l<+`S3O_UGHBF*ZIj$f2r9BJJxXr)vA`$F5&u=a}#3YeX(DsYTeo}Ac;!vLOTKa|~N|(V@t`omWx00eYstpO!6C^d%N`#dhgkZuYsJVk;R@M;KUroBzu#v1BBM~!ZRfBe3{iw|7$MK(PwHV^pJ!6S%LioMqUvNoEsc;mqcpGY-Ma~?WO0<<6IRZVCtt=ltcmqC_MGqC*EoZUh)`R7ARkqdLp+0pVInS23X4*BH5lCa~mP7gTzr1;*epw!=w^qHG9^P8`_UEmIKgyrCrubm)s5O6mGf4d)!NaYieu-^+vq`<#q~2^&Z#JnP^yd|K)X@(0b?&Gvd5#9DkU5#oaNQ%-KpWLBb*s}?s0K4)xk5Dn5D&~D)7$}mCeosoTmf`?;+WMKEi$WRs*?~>@ME3>DT=tT6MdEOsJ~zdO2JJYHVE-PGd9ic#18f4KV5Jy*{5!+Kcn}-pBS*RN1fgXUc7cM<EKVP)aa{UT}xn6`SVV2AZU9ex}K&ho}`ounXFXjmapS&>h&;lfSue_!xcBx#+}?<42uhn-dikGF7hZMluL33h@*jNy~ycLyO9dSzWmb;J9{*~S_h8L+68+q^Bywyx1Bv!JLjw`)^G84hI*a25wl*Eg(Ytma|P`M#I|vKop`j#ebp`fF-M2W$$j$NeKjooLzjM|;lxWczT`uC;yQY6x_Zrl^o3s*KV!X}OKzLtitp<DW-s1FeN0#HYkc?OVT+Ha7vEhv+n%<bfARXyAElo)te;)#?A?oYtGY-vqrDs5MOW7Ie-|7@>!;i$yH)q1-Rg;Vs;WO{PORZIEpy>#_g<g!Q%_T~*u~VyXYR7<qI)N!RZVy2UaR3PKWB$6a8ZBr?S&9QZetqy$>9n*esIc;C~ur-;oX5UKd=^3j_FYNMloyE$k<B4^ivgN)f-N4RSO=gE!pBT8>{3l151Vluml{qK`bql3PyMdKE9*Mj<1kWDMX|m;60d`RS?0mm!BO}m~mL^_JW}5n0o?Id~ElTTt|s3N+lmF_6UcIGw(T-Lro8)8!Zwp!QlkG`*L`{zxK`oY>(WfP!a9E^a47{ZSPTp>RsGFRNXax#C#%yN<ze86NVdyum=Vq9`C|789}h~X7twGh36J0DevynXcbAzn@u>bgchW2Tv_FgPQq{H?VmV$>QYSK=<Vg&XmXiUL=(tVE^iOvvxw_CJ^-Pmu%-(z&ZDvdu=FKh%7mm)lTu|eqb!w^KYNJiK<AO*(@<l?MH~Oex1seuL+eptJi(?3+J=PgTp{U<qsx$~c#@x2hQ`MnUElJ*MKu?WmI(E6+~v@4^ArVXgWX?%;vWXvF{EGYfI#U9T^L$Cs5M~~>)_WdBs01OJDUx-+~xVCfg?=4sdTIFjopfokE+)VW+(7TN)PSUQgTbg7(-xvpjKUJEm+uz_rO3h(#PrZ7UaT6RC}bhEigqn4A^OMM1}A<w#E|C#MJOPhz>LoCegjT)TobZi@+y?$}-Lt?S!7y<u(jdqJ=6a(aYl4qY~ZuRlwl*T#_*CgIY*elp0LsMq1E+f+Bi|jS;01I1a#P#F*GZas*jeuIlJexDGEyE8tkAUA~=6I=%zTPKbWsx5-t4uXmI1%cq>Vvf+$?-2R-9p3f<ef!Qj-46Nfu;k%x8m_(EiI$j=V>QKP;ZAhQ5!VaRY)UAk|p|}|?lglq~o0(iyFZAvQA_vgv5mQeC#ro3zU(?*jfzVWBkaXtDmz7)iVQ?FeEir)fAT-O|d$R&9cTtApQJWMbC73Gi9UYvYUR5UT&&5t4+B`?}dij}bs4$x;nDe<A>dK&0!-C)YA;#ISzLtA6#L_)PygD3+J&=F^egW}n*r5}ZO;MR)p>Vr5EdptYpwmAX<*H1Pk5M}-PQFk`!HM43izMd|ulFoh7-1&J!0HI(>MH5HOrt*miwchdg!llb9(dW2?v}Ogbm22hphSR$@O+1UpfAeF=Hfu^S|+<Hnc19hBfg;(WdoZDd$%+FQ7r@f{b;+;{6E=(mEd6i3Z0uJyJPRNy6=qLkx$qi)VaB?Y8M+|fBm+ZA!Wi+Yw6VdbOu4L)r}J|yLgq+0X53plB^i&N=Kk@n&D{PqOa6JsFi>kj-upFl@(9<8#t_=?2sqbv2_B=q9NF8retHRrJh&YjuZ|_*Q878H4?mG<K#?j-el@^{b(E0g*AGY>DHtd3}YJCS<LE1@0(Ut4>;+U&*Esm{?%DqOZQ3p#lo7jur{`;CZa{pm(+A|NsYFi_8)FNC8+d$mek~r@k6bu;nJ$=>#CZysxnJDUs!)~X<^MTEUajmSFEjESbw3M<l@5Wp?>$OwKcqIVQsOnURhG(m%E<+D__ozrQwdHOjR=4Of!-|*|CIvv|++_MK+9;U*f&H%+(ndTpiDqZn0O9(eAicK?lmVQAuYT6%)YYMy1S`+WCwdl{{@!xPXpEEpghJAWOR=D6?ksfsr4gWRi^%?A@;X^|#;OcH-OxbH2j1+!M_asnM^sRivh2JOia-k<Ijk*CJcK6a-ojD6&b)pBQ0+H6AHDH$$hA2AQ~R=uOD21R(3`B%UF`1MP*jF06?j;*$#|mEj=R)687<IJ<Qw)mauw>cRA+cwmx@BjFlGm`-abIgp`(RlRw+iXa@duu7Yxx=*(<??v~CEOmj}mMF#eFx!^G*K=dy<)?OQwX!wZVYVOL3-jw=t=;JUEnCs{`c^bw*@|XvMVs@jsQ4{VPMlWHR9DaRUb|7*rF^lwQ7>P!uvjs>x9&rm*KR_8k!$5}vI&h`5dDiQW}KGG?tHmSL3;`Rwng*qwTtH4SIq9Kvts^D_nR}0)03m!95+^<%m_}5DVip>Z;-}k9EVqi4H(jXjrJ#(H*sM|z9*3}QDkLHQ7%%&{hrPOXiJiOMs5#UwG5y#pYmYxSjv}{w;mH8(Tb128ySXj{c;dO`zF#38hT%N@LR$gl_$$FJF^VvCZ!3Pn^O@>f|1zV;oHBVa;Bsx?vN;u;drewIu;;VJ%Y0}?Q0{qCrNG%+`S|*vVxT`wdzFd75mnW(pY5-rTr-75JmKgw7;O6Qjq;J=BWsgRa8EctOe;eQ6UIsl(HhVE>M@j<_1|aL9Gu1O}dVIFs4eMI+Tv~H*VS8_s#B3`b(>5v+%{#t}Uazg;Ae-%i?~_yzb9#z08)XVPw|Qndl=td2)WXunL_;PegW{K6y{|(ziT$sZf6SC;uN@o$Al&tYy(`BJ9g(om%3fMpJu4nW+SnRA85uAT}!@ggQw=?XN*dvsePUaS8D7d_qQY4Q>?KlAN6QmcSN+r`BaO*(wI)B*SvKejGsY3nMtItOe~TkSP2a=F2A9ijaUz3UA7)a$jwC8Wml@8ALqgM%`Z=tc3up&{Jp!+!zwWff;G+0g!UW&6KTB3pv@2cCHEDtH^EjWrXyI)N+yoPi3pYKo89r+a%51TDG%Iyt%y6*}(t-S_sNg#hhH*>k1wEez~cZb5IF316K_z;UVh_kFfvq{RO`plv`dF{Kj|fPBp*7T=ScX9ou)%{GKI6x859Qkehys>^E$UJrYa=C0K$qRoU-wUH03y-5&l47Zap++{z_N>~IB^2hCje8{0hvYO7@a$rlB`yHW7lm;MWZn-i(;wn}{`Nqq<9NZ+FHeJ*pelZ@3LSmC>L&-EpR@AR>RZ~ogaGRIK)u2YU7j6K(H1zhyxrn*HUzlm284CS<m!W~@2(x}UnrW`|HJ7tBlvrGfsDj5ilnTGO3MA&V)!ge*^kj8w&sl1sK>o}GBdCI}fQw|MN4xLgC^k0%tStavFQh7}c*s=~S<9Zrgj)@1Fg~1^@Q5KgnP}U_Ib;*^-SGQPy!z|^Hbf;?yS1_ZrJL!yLPuz?kldpj6(tq_nUGIR*`h~8y^@_mfT7DDTn$y5GQM!_Y7NYCTm09wR)1v0q%DGNe!!oUGHl)3#Z>0Nx$wDmrpaf&bq-C3FRIbiddK|nPB@S5o*QWNVXmg*e(7U!ydCYulWVjHtA?G#kmor^3Y%49>uFq~fEcJC>>+v@(W6MOPgCm1dSMj6=iF{rzW37O}sy@xf?Lq&B`y~kHq!Lqq1A_`0lV8K1mRo(AEEU5yYo97ztn`#ejD+sdw5hnf$MlSl*HjQ6ta?~txO~*q!$EG6eGsQ7{uaMvigzZQ4S?YlK8{{9IANH}V~^?1=6TI2onmqGbce2ce#A5XL?i-g7UZMv>gs#|vw%t_4^YYv?3-+9{PI{{-;@c$>{8G-xlX~f6xXJ9(7l+dX!a8CEYB7(PI`kG>d13;4-&#-N7KgoUIl7%tb4X45<0Nq39YfG$C1o21Oy9z#J{NWGSsj*6T(XMjxt&)UAe8+lJFxfF<>Hu0DB`SrS?A5&jwx<6SPsbf|LaGw1+2+1KJjHK9*Za<s#tGDknZ-{7sQDNy*zwZhR7?gqTA1b_|tC;3gI)U6zoHe?VJGObdI)N3cSnf<gy<$BNBlT&`*`#|bQztX}L{L3Qz2r^B^Z7hamYHWcOXR?&B+O<5%v;G|o>WxO_>lNTV-*bqmvv+<ZTQ7FbS%+J~xhEVln8k4tK2#z~t&%-3&Vj$Cn^o#dZF;w}QR=S_`5BBky=^(3x=ylKA$<<~uF2vBQ@Txp4{iu#P3WCxnd6a(PTXA$O9*-QK;P@xeEOrJFM2N1SB&wm>L#ztvA&mW`DiSR;dlo9E`aM2JyE`~+BsU4W){8q#H&QJ;b!Icdbdy@@#DlTpWy#dlx(9D0?*Cs~aC>eSz9Pn%FW@=+dw6GE(CG|wozDESaptRaI>}hl*2U;R@2=C?Rh`a*bn;tCbwb<b%&4%cFTPr;v#GHS#k!~lO4Tku8EtauANx^-jfZ~P*o-+Ce-cXu!{x@b__#69Ox^P<pzHZ}ZVE78mIBPJO>Qz8w-&zrd28XD6wFNu<|YMmlY+TP!Q7-^Zc;E`Sf{<I!F<_jFjR*)e=*fxnlE1#X08cSe}7pGrtwqS@uDCMAr=4;GVd6N-myXl=2J{kg8|OVhcVrGss<BGIYeHOqmGI}&qisK3sNv9)3H=gS?IJ(QZQSSf|=w#(wVf2e`j%+>8+KY>%c5^X{wyaA5a9Qn?ztDvuiA~y_X2gY9<2HOwB$?po}^&{=IczFq~E84SS|g2UQNLBiMM4{!A98x`tiXfe~=WE$_<|U?vfmi`p-<r#zRwx%|`H4bJpussc<f1sIdpQ0E4h=7MRrNqJN?7%7&V{`BsGG{;O9X4HN;moD-3&-r1m|9L9vGSh@P`J$6QU3f_i#xJ!~MhOuEXQ$Hx+=(E`E3bBbdGS;b=KO-g3sO0w?8#DcXME-S_=V7of9cOE7_tz?xuy~`{&HC;raKjinajn@|M{ivP^j&^cyZPVUwRy8`Y>~G7|c<lK1?!w7^f=tvJqY@r!yY;3b~kR?2HZQ-F)nXrOXRnNxEx(Bu&Rm2cNa)$t&}xHWS8?gj)3zwuNkNV$6!yBHjMy-YOc>OEe^zaXOR-R<uv|mA)aX$gSHs-(@nBJ*|Hdz(hj=Ay~TbgpU*3?cFBHERkd*1`Lsp&rst+-2g61W&C8W^C{|pART$}$1<%bO%RSB??Dg8XIXb4$UXulST1jy-I_z~0ER9Bmp!U1I3BhIuGjGiUV@tpi$7Fl%AXtDUAf;4Ll_p{c~}czVCTZKtTfj!U46<{RR)rCQ(6Yz>_Y>C%<kxDGR<rIC#<x0fUWsk(8rOitr39S1AV+cK_3HM6Zi7Xig6{|o*CBoa4?{8OD>*ydCyF<wl5R$vgxbrCKeuwW!ueydAC_G@8a-;np6pf?q=}e4xkOx^<eJAMR7FBT2-e2^U7MsOf1mhPrO@eeZ4l-^VN0=YNtlRFy`N5jg;6zGuxiS($Z)GUT1@1?`x~1+A6WO%6i!<iLJ7t{k&Qw0fK^7=~V5UwaOT2<k~8`5c@TJFG{QI{^S?lhssy&A8Nw@{d~&m9J`TGI+uQ7hqv{i?!EfZde(=;*leBw##$}Rpcu>34@wlx0k~?k)B1bPkZZuTXz%cbK@u>LDd)8J`1c&ry8Md?JpyzVdh`f734auiF3f8UJu0`{YO?3Tvn9X-gfN6wRc=6%(RN43^s!hC@*>|N$g<2G&DySKMPw1?$u(F!Wq#ZTxGalZ))VT16^<y@0nJ2JNsXJ*>zZ)zc5)ejbPc|@yt4N2Z^;8dt@;*Z3tK1T0lpMWKgLBN9P}a;ECAdlGL9%sjDFbU5FwFUpX&t>WXpoQp+fL`l||$J%n<+{gDGLgijd$sl{3th%GJ`|D<t_ZC3+IIoVXdwHvCC&pLppop97mj-cQ0Hcya1*WXr7z8HTXN;Z70ZGPNj$w<Cq9S`L9x#A-kAtUOPrs||P^BjKMa%Vjweph`agl_P%*_nX%~fn}Ls81wA%r+zqcOzi~K;q^rK4Hvdaogxu(A#8hS2KNk+5j<z#hOZMA@K`o6TP*Jb;VJ`VO?IY-0k}8b0)m=CO1RYUhU*OnJQz)@efS3ZOYf@dWa*ddz}_nCw&4`*nE*Ny9%;Q@I^I)<ugel8*o94N`NAM5_X9iNGmaU+Sm1r_6S)fI+misjbn8vS9kJ6IC4cvQ;G?74`3Zb<KsX!;v&6WcBS>LMg9#(hCetKHg6qv%wnA0}A_X{<;N_kAYu#lTygsIpAl(_DsS|9O&=(M-J4|LA#)esjumyrp^!wJV!qD%jU<T%yBFCQlJ-|vgGf;|ylMW5G2nYd(WI~okU{Uxx8LOFA)J=t$`Yj-)d4iY{5j0vgo8ntlN{E)7EVEU|T@jjGK4z_#xo)J5Rhe8KkXZ38iC%528eS8IUZzOCpJ2<TiYHOH5j6jCP$j=phVJlVOn@dV^Z=k#Hm(Qcg@$p->=VZJJyDE&@}=L!C+k@N$76WIn@Xx502j9kUeMdX@)$UeHTah;sEO%-B{OnDZX`ih&amQa++*qn^=pk&d0^!+55u=FfrpYvvVk|c$6yPfT0mVH%ie%>N4!RzBy+y*T3udwG44BH%_Ap>j`Ja3Cu1eq4$2RJ%eUxi)>+zy7HpsdL<8lMFltVHHi?h}LPA<59JdjHl;0BMSf`IP!B|qt<00P)WK++R_$}=2qamSyRP+pfR=i+YpTh_7&$xdfc26<AAq=*RA{c<i@CjYw%b$;gy9xjdFf3*kf=<g@<&S8H;3xFjL56SlCOfDPg*{^=OVt2b+*L`z<D&@)%l&)L?z?>;ot*xKM}z3{fj=Rj+utKJ+S5KAWGbi`Vs88qm&RwFADfp4%t|Z!c$xeS>YMB>%s4b)$IP|Ws&&MUV@%+c!xDNHPr`)9_R%cd_2=dRO-L{@BJcepA<Xh0FMmGcyY>f$nIws&Kl55W$p<jP;?rm~8N(eAtZ3AGW0Umd0`ItBl8Lms!#Etg7~XO9K!HDUwImw30d3vFlo7gJe~B3&Z**%oV%{0jUh0%h&9#+nYPt*0jdh1|SP3S!!A7Z`Vb9g9<2U}Ok+@Y%T-mm!56R*##Ut`V=^41x4a5T+FDABKEP?F~`Vqi{c6TOq(Me~Fb7>hkm`U!Y)M0rXi`nUqy{e^42>N3H54$&*i+04T4+loN!7ej1L=I25gMGQ=CljXLIZK4XuC_-6_$(1k?#xQVXTJWxO)Q=v&+sEb5g*X5C7$@y!!cC;atD$j(6kQ}n_&7eKWe~)Ps$8XUoSnWdDP>@&lU6lu;@iD#eolV_)G8X-gh1ljP89aOk(EV7iLED)w*vRX52eQ52x0B2Zhh3J%(s|X5DA_)FALM<w>NB(gr!eR^L8=I5Rejh=c$|4V698xe_Zh1Y@QcyME@_mtlbmpKq#}chWw|t{-eUXD?@YBbhLAuUNNMPFfWgI5WVXuTz!=Oq<NFF88x;6)#(;fdzZ7oh3s=q522%XO_-<=^xmGT5~=w&+2O&@)tw6fB|lF%Gsu~`s<#{+?Z4S$OFnv<R%hACOoo|r$_8D4HGSj>)={x6g0AGb5mK=fTA1u%;SMDgfq-I-(`$WAvrQtSs!DlE0QGBibVWsLQPfpMl7+w{c+3P8Dl(Gp6wo70cW8dA63%6q(p#?(C*|5H{5iwII-db*8o$Q!j{-dp<~EbnF`zvwKGzsENE9WBJNf30_{xO5AOF&F$aN5C#fUTUMR62^U6FDfgctD3d%$9ib?;B4s|c=@rn^(W5l(_EfjMS!Nw+#yvF~;U27)p+D8)2`Lm`jIR=50rAfOpb;%t%ec(>&uy=}rlNZ^KI#S$>l^I=eQI>E83A~`{9JG$1XN4%ka;R(Y6_%yS)VD8FC^KHttxR;TP0+U>V~kA>!54(5-!4CoAX0ad!r=~Z@FqF=<F3r-WX^=JPLP}ot?60HcKYY2g1k~?Hi&r1iB}>q_=r&y62tla$audz`}?S}IQm5bb{==i#jOOT+ActE6S*G4;KSk}V$MpUHMUNk5$TVXiDM`m=O1!|oJbJgmo^_c_WY$Z|8shNLL@r;Bko6UxS*A=<S0*LtU^C|#@d`&1h{{4W&i!HCv^Iwck4$q@b{J5ASX=XV$WqhdcvuGSnl{y=GR!9f5H;MF@YwfP^zqZJLc*RPw3etNNX7=K0I=63Jw&mBjScJ7HR+FYZvcl?jjT;d2T1TyK4qgm$`>+sQJl#s~N&tWpR(D#GW2B+_H{<%JXcX1ds}IM#5r8J8C@Ir?OfzQbM4>t#CPh7ygJ|jGUs6SgIeji(ot!EzV`=#a-K{Xdeb?9;X^u)y9$KMQQ<Jnp5UQT)2B?#DcXAGHXnAm+&wAJ70i9uht60wx)_UIrL7Vqh+suX{|VS=-n`PW6G&j3@uf{s8)JqkmiKZ4z9-17sW=u5huAW_8BXE!`+iD_L&bnk0!mC#wT(K=WpM7#uJq!nlM5{$y+hklT;k%!c64>=6#Y_a#m+(Q!LZ1B@c%1K!JAgj>^SLb34qIe7{$cwA#IIm_ezF{lH*VPmDxJG|s!O_n8rYd$#1yjh1(p7XFrFfMtDK`zc(yc%JhNjsO7dERVwoplfD2D%?#P{am$v5dx9Qsi6Q<ZC%ajpl1&yEU-l`)grB|+ASIo#m*TgO6ZvKeOO|HGKdzm?I}R4GM!?AXpZroAPP+X(q)On8)fbCq6}?V4&zU6Py{m2nFb;&|3ZAwpT!5|&!ehW3Atg55=gzY@KI_>!2}qj#G)O!*v=SO!H;o6o+1XGIT`sqG>jXvmY}K+#3?PuiST}^wCA82c*1#S-0(3oNAb7kGkm@_!yh3F(@lo(ao8ZUuge@7kJopolwx@AP)KN1Z$!xvb4Md>4o_=_Add!+=o<aWBSpI#X#C!hqMjvFQhwRMRy{Laqi=!pJSnHhK+<%b#_!blFr#(fK#`wPf^er#G;GH;G&G-Y8RpY59$5$3!dFlGxUw&T#$qc&_&~#Urwc}mlIURX2U^Dm9nZ^#J_t^@ma#mJkMx`mUFUlWzro|3WaSPr%J>#mDR5@lzr!Cs<6?SrF>HNXsynpwhhH%wDGS{5-@mcRZfvp}6X*8lt%Ywbd}EW{*km_0*^NzhV?5ocWH&0=%~kwk@yNoBN9LHWeJ2u`N!m>RUP~gQ2^g6=qudy4!-;itpq*k{ZN!yRgN=Bch+|<%9BU@x7?W-lcQB)p>Gvo~#f-<qbmwFzz2JFeBNiz+X)oT*`9zgO7T%3A=11mHo~)?-sXaHJ_{yD7$?9P<Hkm$qMkpI)G3}hmozlu;rED;-s}h{SmJ;=(!(~EQ9CNmQYG?bF9?72hEr)QGQ|3>eg(xKHl#b`mm}Qn4PQG3|Q`jqE@%S~SQaoMl<fA=%@da|39bbuN^CvYC&CcAzEl!(1>luMDEN$XvKbJ3hvlO>05vNA*z+e-IlENCfktIT3iDsiI`N%T!OLEHmm#e<je&NS`(IZ<H9oJY?1pB<?KYp2k)xE^qdW#{rpEkCql&d%qsr*|BO)q+ppHsuGUE8&bKlgJ#Jz&;2brjET<Qm1#FG+&e?$Iwyy%#^_Jl?sPyZ7Ab`?|?^oKvDq(QmZj7Lm%QQ_@+OwfPCb%FkTO{T1W#m+$f74f?S&zt}jhI_;cR7A|l$FY@@#hg%2>hT5FaXN{>*f6_jeeBQl(>BWUg<0}l!&)m%a+WW~|%VoxYSD;i!)V0qmLOD>Lb-oI;H@s*9WBpnpuc9x|!>%P=4GVsTd6ed32$Ql>h8kBnhO(M#mXrfk1~UVj91LlTqAo=VNd|LkN&ymwBvu6PKE<5Ld#K`uS&>M&ih<}N)dWM>5n3V`FCbupIio;Km8cDwVO2GBe2^aHAX12cv#A8PAk0vzQj_Au5DN|`>=cFXz_h_CU}@`zJvAbem+1qw(%HqOCCSnuU`g=y3uRt~Q<g>XbfW<QiS)N5U@h&6e(zNe*~-ha=iI^F^(}JdDk(by+f!EBud@+Cq6|&XEz>$e1iBfV3;-P(G|c79=f-Ixu8jCAPy?bFr{OyDq-74Phq-ZDhxSf!W}LRrGUs~Va&nysnU^l!R4wza@&&*P=p|W6Qb3&9rvXXex>0mmI<`P&12huML9HSQPzQ%wy62OX#a3=5Z5|%F$@Bwgb!YJ8bJsMJza>koH0E7{a&G$A<=pfuuLbNp$r8?|mRP)J5lw`M0s4G+G<a>SHikxF1ooH^+|vIbC~cd9g8(Fi&+IA$w>!v1428-rT6Z4!ZbKDP7Cpmr44+u=Oi9@za6Kh%$z6CJWIu);bf}mhoNAx4&EzaWJL6*kKy(OOVg&|*+3F>wEZN!ejrVx>69W^uL;0?Q_9J$F#Mr-6#%)g+qW=*gbx&eTR7PD3gcp!qtF#t__*m(5vRb)!>5k(>?FwrkEJLUbql*XN#Cn1&T9<@42HzI^nVu*Zplv&%y4P~mF-RIbM^M9dg1?IH1PNsx41Ql}hgP5^jL|YU*Bt*X<>6PYZ3;wsi!GiZt>}UzR_RGc{<05iDBcnSN}6-zN2ol^o08VMlW4OuXBZa0!wB904T4X;!H#yTrf|UJWmm~<1J?y@Ogf_vid^DVh6i7ntT5s<Kw(I@7cmqA1<5m!%tWagxeZg+|97j7->T!c%Hr+MTMOS>_}0R=()g`3ek+aNO5?ZE_^mX4D~<m_O5@>YqclDiw&9!e6;)ZS*ZeL*tI5A>jeIX@hN`dX<@7BAaT<-5nB<ji4xRa2Ws)MT7~AX8tMSXIppPuJMFo9R-_7oY3i?}X>h4kzeL8qeVJ~YmcXBT$74!?W^Sr1-FN*GJv_<)u&sS8)=w*sURaW|r`BNd+c=qR1N}p+!%DsE4py%oL(^7i2C*md2IyPWh-0T8mP%q%5j;?k~)qL}UPHWXXt*_YK+3PP<(--oom!F#NO^CKixW3dq{NlxWq_1BTsvN4fv-weZ^TPGS@f9200eA>QLYM#rMz}sZFRq_dLoXDP&kO2Tir>^^c}LCG>ji0+8)ik#_bA4DQ)nHlo-<ib@0VqDQw6zRS%3K!-g1NQ{qZ!F&po+tFE#iz?a_-ut}h&rmRG(k$)6Nu=MQmFyIqulm1RGzsjJzi^F((|-F57xuG%QiOWppW=<qAb>Ps*|c<JfCx~A^W1#{n4Uw_NRD`sov<1~yh>IKPH)f<+wx$aVNeTh*xaZNmXeOYKftFQmQd(rGOSHsR>ow5|}ppJzKaBiSA0<%vacY9ns8P*1?6Id#!@<BSeTon_o6T4I?+XkJYCX5e5YxRshEgL(Xjqyb_Wn={?RU$6GF(z~RTybNbDJP{#w9BNw%BfU7l>FJ}kR-o=@W-k$fqY#F1_o2zK#`s>DbB~NtmsO{pE*e!)6{93x)ke+vh@B~Nn&XqlfP`CHN57hilZlV{dlsvC`kIjr1~NS44ug*2I)89vW@f$!$7YRl(gbxL@719@!FD8+!w{~)wk0Nkuh6PF?RM5A|XU7X5hzZVRqR%GMbcPh`yeglc54t>LFS9X@@033vg4USl1JF_7>F!DJ8$A0G9tX_g6iHCx6}z32gMPoO4ft`7;Q&k-FAd(1K?GHdZ^Gpu7cvl^xfod;|`lW9OotaeBU^9VTjm=vj~D#b;b#`LW(GjO(dlzzO}4icyqt2}4z<Dz865*$Qj+zz6beDTO>CNM2Q3=lA$^`N_#i_~_zrq!BT1y^OkH2TjmqhQRazW|u)9EGOKRUXKBjP_j00j-$?b2NBR{aT}By%kirR-&H4J0T<9RkDwFFmNKtnd8QISz@LB1z!-b(94<5dmv{_u{RhbXT>xY3u+E+G`+Le%WsgDCa>P=bQ59WNY8c(U**SW0)g|fUX&X#Urbu+m35nm7d{8n?5Ok38j8Wtn9^+eDYJmEsXwRhB6FF!3oFvIuwHtz{`5~HCPpEQuRo-&J!uN8?JyYocL}VrYJs)w_cgX&mQJ=XnJ5lYS*wt$FAN6^7Xo%(<isEk#?4zU~2546|5mauiL}m`oWoS@=x|h{3dXU)mkR>qvCzFE`HY1GKjPNqPVkQ>#+wQMntPXz^9U*MlYg!-6F9~wHTc7$B80gq2|FB$3+8@~x+QxWWjBH0Bcke?m&D0Rm<fGxelu4=yc;5I%iwhT{J=+PhF+8&a?OQP*+q*g^J95o=yI|*!nWUYmf<#kZFszWg)+uD*HKO9Z*FJm2ZCn#<9>H51X^oi?d61$=Lz!cu@xvXzg_V0;E%kX;GMVS(O;Wy1Rb}9|ooTMX&6#~<#Z$#~u>TZ+j?or*|K9d?K=foX?xlTY+Zr=Qu@%saQT~F>1-px`!*k2wItyIWX~hg*X3~XZ3uXcC_;MaKTTPs{BC$-bWeA300XAz#Wj3zKbruk)h`UOT3I^Tg3SHubl{&?aIv%5LWn(&hz+jmYHAd-B&E6r-HX^P%1S2~KcVS@&u^7@6Tu#6b<@{T$%K#v^K{73S2w;r%x_ltz=pLA}^{NcPa0vGC$mvEPmJD<ZH0qCgLZcGG3c%0qpiXixJNLipeshZ3;*;xRjoUt%1#M-v90+f`2X+g;qyKR0x{@4-#F-P@DxtSUXm#%rRPf8nu+_%C54#9~hGcj-%m~>ummz-d4Pq0M84m=hNHQux4=eZarVD9};JAVQgS?w9QdMq2#^z84BwAAn{SjfBYszQaNKsTru_~%og~@3K`nVj`U+eG@G(;IE4S+T+KPxro&+uTQr|2Z$Fg#mA5-XOgx@T&wGj|ZsA&}m<N3H_`tkkT47)OZ2D@V$lN-tN)&gl0R711c3Tc?mZo5WK2<UNs3a%>kBr+nMGwDva2vI3|5_oo&3vlo}&wvM`MK*&*4Z@m=OiGI~ABz62uQYYS<j1Gp@3U)gfZ*vVD>J@foFGDFADdzN8R7b5Gg+y|_R>Caf(g6v@U}Nt{T5QdHoys<&2o5z!7`8dB09taJs##;@T;&d_JeyV(@aXI6Dh)ittC<kD_l7jAYpiM63|d`RQrM|lHn9rXG#JD8{6yd+v5wPll@fDxEs&%VSJ4gg1TzUm|Ap#bZ-q#ftM?TNY)N0XG;Uu?V5jQZ9!^xSw~QeL`<<y^)3_YUqc&ernT6{`kc62R1EXqTccz7n-Vr3NNTrx6i-fba)WVh;r~)rP6T<EYHf}DdV4EX5z=2+~h8{k}aDjF;7j_GM<5K^662I=|7VO;jH1rXRsp@NEuS7Y`XyVuF>S6z2ChL>c`g*ilHwhz?!2X=q_7P#P{=azblF`*<gI0|lv%ZNlx&CnwLFPG4D@CW3qQOehti{sdGT}`d9_PS*fje04`4c7!gi41paOSH6H(8iO$|7wFTP$SAP+(jgK+ki;Dgy+HrJ<!p7p4MrpUH<T*h5c&{o-rdly=Cs0>6&{hMVC48KzHVA;1oz>IU`#<+58Y8Bx&;x^beorSiQ^JFOkQW(x32Yh@Qix=~76+TSwRDxIxS?1yU;JCT@Bv;Bw?o(oln(TS{JdvfWNCQ0tGiF~68RMLUWj)gEzpllhtNMt{71Ij8hm(6Wj`E|SJ83RJ6^rzk5@WVG8gzs8zxu4ze47<I!qZ~1J+6ZNLT2SDiaR}IEKR;6aU!gBY!ZQxWAnCLbJ-8w8vAXc}@~6asy~K7or$ALY9P4UwU*@qjcex#=>k=e4rSW!70<OW(&e(Y8mTj=DvmqOAFZsT$c{*r&pC8MqMx->aYT%RUEq|G7p8lR<#aRMpOzQ%#+?$3gyG&(nmfPDnE`0XfO4ByS33QvQD1P|2-S7J5M~I4tfuf}JTZwD2NK)AYA;8|!mIzvQFmb^~psW!G?o^~-NdJ#AbRqX;d=rd4RVgx8d*4NEKJbwsSb7j)4spTV)JS+mIW(mAEYvHX+Hz(448o4|cd#0g-Zk;_A#sbmVT2rzHrufA_NoCtC`*Kv`pkS9UEE_gbI>aXg1Xf<$({+cbR*9hlmo+RtPK_xzyog6Q;v3Px8sDz_N^9vqyVgPbBEP%Oqg=yIKM6-riws%VqiLkBj26%i}1g_A~$kf4Y7k9?mMU-*I2DdzJIF%;(YaH1LiaB!`(^TcA|IKGro<B0FGjZR63l;a6wwfjO6erCTYXGjOX&Dc#g}kg>=oBML7%Ultq#H@z}-YqK0vvPI*nh=Q#jsz*lZ_;H0X{^PTjT&%(ZBL}HUZo=1Lu!Ff4b`H@cPCeh=MxAOlp3+>&mM3ZO2yLaGbJUy1Dm4-)5r)B!^kM2hg9BYhSj%Yykkrn#IuytQc;aeftMh6PRanB&xRwqo1imR;<`hz1y@_oE(j6sEecLoF~o9*v;O0##IIk`1_;CMQucu@X%s|KT-axGzfvpoMJa%R0uxRQIgr}F$0I{xz=(y42X<X%GU5=8akumx>Au>=5>VL&zlw&>-%OGLABpE6-6Pa?20%HaG{@4Pv?reeF(Y{mdWV}1q8t-PsDTS+z+=Coz3>!l-E-cNR9VW*i>L>QYw`(P#cTvHqawO}#QJCfSO1gU0QS`;3!nEP@72;U{1xSu$z9hPWpZnWqGd2eBc^8Ha|4KyDFWmjduYjfe#Km7rlO_`(!DfmhDcWgp>I*hH@*H+BcvP?DxnQFgmOA?P}%^7CRsS*(<oCxc<(xM5I*dY6!>y4V#s5CLNMuiPv2yD(hGvsW`*_QHXW^a3l^TNhx|A(g)<CRv7uWQ9HYsEZk#iq7mShixGwPO0V`wbD-autG?$g#238e^>;0z~0u3zS=~?B(?LDkb^On=KIbQv=zZ9YW-^=dG?`>Xn=_{O|@y6f#}qu=9{~Z?G=_r;Uyso-{Q!_bMDWW#+{0IgoaSDU#DJ&GEukx$!<EU38@4cY_UTM;36$T|j53E9rq#r8-(dG)jnCTQE8%q(KE~to2C+IokMmJu_}im@C6QdajuC;iPP=l!N6-L2sXO(Kth=VxDJx1RKMaQ76RWxk*pRDuwX-ixl%0<tBlU>MWiD&5rcnW^|LNbtgs;3;J&=q4z}pO+B~5^LUD0%wz_Sh7uChuTd36(7iGuZj7zQv9K_dxKqVhZW2Ml&<L`cliCzLBCI@BYfL#Q-8>bkWN9bmXw?F0sY(`jFKI@fc}mEIj0x_YZ-bIdvURfThUfltg^HeADGbc?N+_QlRKSX|^t)%SRP15YuiEM%rZCFxg6!cjl4>I9>qwx4j~z*2Qu?#6bw#?9f^%%|V@DUF^``XSh>ZCNRXoIO(Ni2AT&)pd-M>FtP7i6W3c{;YcA9(~!0;}=?@{Enz0WGLaP*)}XOuoUy-x7%{hfBMbhC@t`>slGlrRm)3i895@67Kc*KbULC1yIgA&(H_=FVuX<=O-ilE)I<A$Wt@Kd@d{!Uf;A@o<Mn&Eg_*;ib>4cV>?SJ34;jz!+n=XDyy6!^IQ$OYV1k^YgB3d|Ph9w-2=CfZ}tq@gK2o@;l$Oj6JZE#-_OpO2|!bn8pbxL}kIl?$8)3wJutZX;Ef_<cEt{W5b~v;cW=-D*F2{TN7oj$ZaA5VOe-39iZJd(g!GHlt?Xc7JHsBr8xdb?Q4IKxk#efPf8$T`yCfKW_19v>C0)iwjWLOSPGh_0}asD3?WSAo!79%h*44V6M+br+RWySrXd--#FYb54Y=_JOB>UD+o%k!gzZu6SYdH(CR`}vQ=oMWgv~NB2g!f-2b$H}rDuRy9;hQSf647~mMp%!jst4GTgfz-Pc6cA&*`yDO<C4Jl-5V{!yBMlAJhJ}rNaxv&WRc@909i&*a`_UU}gY}Nm%(y60*nc5nsIuqx65>853sKd75LCw!FiRkY=5*sp=lgHsv8Opx_+aHC|ZY$Dm08$FF&V+KC(+sp`wf1kJAuzc~KmmQ;2HYhg&ar`biuJFBQv-$(XiEMNNfKFH!<p5tb@_^ZpJ-0ZjJ0v69fCl`f3y1`sBtg}R0_O+<yuCDynUwjfWR9#~@U-NCj-&&%{I!@ML&hr0}g#9@r#qz&G{g*~j=7LfQR0W~hNHl7{0>BVoT<!gQwMUoq-qMK-wCNhwH6}*@t7WDZ;g^M?7FYY$TNHrliYd}iJ7#sUPV+^6@_MKplfAM`PO-71i86klhmX`N|2beHDejhkLbHZP4o=uxFmAP4$yljF_O#!mVMSA@(qCGwepp0Se7xN!?1qGfMK07snQ`HO#NEpsHcj%c{+7ov`OaK+Q>rzZa^D-wKHn&3E1~t?n@3Ms)YcX3DBvT{bChc>z6IgE6|(sJ(J}8r&b|aO2Qz-e77n3Dhn-Jp<Mk1C6%U+GlT<_Y^dhC%1Op0eUYZT&(~j5N48)`no_Jr)6X|Pii^A&v{ve~hhYZTKP~S#-o(*+{=;LT_Z56<1k3_L)s9Ob`qdgNxBI}hX?I+89W6YCn0pssBD81SE(>Q-Q>}#A~hAVePA=V(Dvw-6KwZ^=(C>3w#F_S6`TBHP(ImD<Q*$L+x#~`2c%PU5{K@_Te+=|O&_9KBO&?}5p1j($0IXtam(^}35w5SsM!73n3rutk}8CxPd1X63u9EZg4z0j_~=C4?H1P$Yz`*Ef~Foanqu+7ETSgH!0BG<mWiR1tJFdaNnB$FajV+Usv@U?qc#J;tUm&exCy)07!TGUW;YYZ+$WP~#K<Bpb)$|fMe!O{smW3+Nr`17ort7MB{tvVxyaU;uES$%vzu4{%;W|5w%lD4$5n|D&0j8ko3vAPA=ykG3&hP>oOo_6yvs}>NaEb~WkhXCBnYzKd-n|I?jH%K`x`P$8U%WqL92>le2rVRO3t?+l#X1D$7Z+8Frt4m>zjy#M#8dQO@Z!0SxK`XMf+EZA{nLF0L9Qi5Bn0u^%`_3_YjgDVh3|_WcZen<oFg_5f?q!--CQhKsI^_)|Kc^5ZGN*8~60&0Vj+J_Bk;*ixs%etTUX^Z(L~w4<UrH<Pye*4mlpLS&%U-MV0P7;H*QLWonh*{$&+f_zfw|l#E`{amdOqG@TXtOYqiVgSo4a-w1V>0HhjQik-M38^*K@h_CATzJx%)jJ8>TijhPh?Gkn5xnC%8{M_-tdI{hnFeFpF;cYB6ciEuFpS!s;|~GM^EFUZ;88xD0B8N)Cu<$F!A&upKd);;~MFY%Af}5G9*88{{5&>5zKL6ne`?8RkjKgB^DKvUF}GeORWqojDOQRqCjvR`#`!P{iuNLU<n-vS~H1P%doZR|-j~U?@a3(Ol`oBd@&pD`qSD6RJ(hZoJ&q_RLlk=Fsq04=z0)NR}mXG0{zQ*uzq*dqynN9g%b|U2we@gM?<AT{x7<?m65?#EYz45l|eEnb;ACcdtM#F>)cSQs{$nV|hT`>}vqBFyA4>1he&};mb;~O>h%^WWCGa412Q@?P#8k{+%d4hNL?P87$Y~&%kU2x>$heqa+XL&yEA&<4Z98;Kj2EOSY{yv-RILD8vT)|8+V3*|W=HDge6Si4zfGZ1@*u=?b#_@(_^%3d+e4I50?yj?V<;FXCC6q-`G^OOe|_T0`Mjl;Wm2j+S!*U$l?RsM|Fjb@DYt-3IQc2eL_q2E~VwCtKR+6AA4Rvw*d_x|0h^u;sf0_|fHN`K6}p96l9Ff|k_&KFEu6uY8W@$hUk>2@4?d$50efmimaeKqm8-_)20jr8BX=MmG0bCwM?BRK1SeNUT&uUCTt`aW}Z-#<Kg)mVFF&rXIZ5Hn_R=KYyP9=<B}w3H!~I+hJmd9`8u(Y*h^M$7rZ~rh|wGEdQTqB7mnTy?2t{*<$KKCq7T_bb`K@kadDTSbAr}`H7QyT=AmEl+Iv)PiA$9R%G@I!klZKP0rcfj%WqKH!_nvSxKG&dktiVC9mz7>QO?8d$lq{41}<+B`;c@LAO9997k8hy&G!sCoGdcgtY)EG~Z@-(>D8K#}>co{xYqY_pWal?v{z`8!6vY$*}Rwn@FTJCeH)fgTBYe+fs%#FzuMQ^D7T}5Z)uIrj?jl?Kn07VG7!}b2#y>J-K{gi#VkZ2KFC-L@g7U7;jNHMLK5_6ICXQJ$l4SZz1|Y=Ry!i3cd$$l|f?=8Nn!BD<zT30NU~^IC!-Bj3`B)6f>JfMx!ym^@gDj+*e0$U$;-Asyv5c^oKG+k-AOZRw@+X_`x#MZD>fF)KDvQoF=hl85>8Q6Iram*wnO{EfGF?0js{4CVF0`h$-pU7GWV-quo7`Yb%a$(L}ql`o-ZXJvY_$xW%;9q2(+l>`Fj*SEeyeiOO}Xflv|FAdzLztb;PMd?4YQ<?Fx#a*s?$Bw0zrOqauevdWS1LHEFuP^TF>qbAQPomK`AN3TuEPRyTjyT>>Z@KfOJ-j%?@m_<#eya&sHE@)mSP0$d2*zNC#n9{fC#<y6>yHSAkh;PRPaj+zb-K>|1xW|6wPrQSt^p;<uuX>{?92VAiTA3=?<=P*Ro@Y$un#TEqKR}!opqJs12QZS@lLUlh+|C3>S;u6-hQn`5XX!Eu2GMDHWT6gx@r@sWpk*&_TGc=h^LxR%d_rTB&4{##M~cf6!^u}3Jq)FvaPTMPm(row>Cu(;KI!EDT3KE?mF=0c&u_TRzzzUq`|@<QY^UcEcXesSf_>(aN$|KJlIY6a6GjA9`e&xt$|u*T9+aojZNfm_uzXL~UX_0PhjPfyuYD++WkkN6Y)6S>R;D*0<+ozSq=nvi>GZTg4H)r3zcXZBW!&oudyo1REp4bfKcMi7$pIIp?n_U2jG0C?2T?0LE(KkmV$jM9F)%74gVi11Qja%l!-K4g-^oOF4a`A#0$W}HLnUmFON6@?P+F{K6wiE9MXUk=)KMD0<*ncQAPJ9iFyxrOk8?ZdW&Zv(U`R~cw$EuQ$hhky+0A;`SiEPS5q}#o@;r+lEx|t)?>7}RYI(g(^ypXwnicO4lcqP<2$Wut1?!sAT)q(R9nmB2Z1o&s@0Y+xsIs$PFi17Il4y&4;1+StgrUwiqL7w1oI~A2#U(b9`8&@IQczugMR+8<bBrNztl5ryp6zHOmWmlpa=%D;#GZAkEUAq$;{W3NnE_zed@m6rtkY=nt?Ons0HEhp8-P@80Gf`aU7>PtnM_yq6jow3&3xpEI2JvsSN2u>7NqThIQuQ}kL9gqP}3@*#{LpbreFKzOpD{KP|ilb!Rx(HKbgFNs_);`sigF@hSoVu@JB&@T54B&>4%e04?GE3`Q>AKtoLC}(oEc!9Wgo@qyt!qZ@4pSIxeYr(x_B4j?Mu%k8zEFf!Skakyg{7iu!-|T1g4)7-Ea$QCX^e`F$YNq)dxtUGNR|FlC)xZR3zkPrLOhw;{w%ttmQSj}}b<!s}iBjwmZ>)o0d5m}5U_Gw5eiPdG5)t#d}bm4kGzDDR!PmSU17d5;(;o~_}?96yC*38eGmHdGl7uAaO+E2vc82O^;z&&DE2)u>opA^1$uva%-^Z$DY4Fma+f!ae2W7e}hyIKky=+JoM-id~j<f$(8=0VhHiQgL7?#!PHjUIRdTlW;|->JIf@{QOGlIR!%}l*w|=_1!Y_FO)XyNKr=PD5~Mq#~oo)Ay?m+_Sat(Kiy#p>SvDaeGj@5B8vw7w;9Stq)gh_K9|_9$xuy5qMdb2f%lH=SfmJc%#JqzA0RQ@)94(btSr=XiF}chkncG;uvRE4Q-J1<veCto(Et!K^f+e4wVOuj=FG0ocEPu1{UBfUYN|efY($55eml~h*apd3y`!}{Du$rD%MKn#VmiaF7^$w7P{Z7p(dgQG@~E$-Q3XBLX<7kKcC4E{4s*Ja@XHIRd5I^EME0m^nvfo*2ml6U353g_dVFLE;L;kY<=8!8%xts|?I<r+LZKnvrLft$5*Zw|HCcxrGa(^omoolJ98>Pqb2<7hctcdSbMdos`~zMrf!FtaINV1?a#1V<7e7TNhAuAyVz{<uGW~rNwox(}M<ZQv<-GU4?qJG2mfaV&nIUct?Cu7li>0wmG7oiiPSIr{dc<^<SG<CbXsRj_*8W>Bu5XtXw`-ys9m_@~#939FyO!JG#&45+M8>QzT{<e!entLc2@aXKv&66@5LP16f!id&BX&ol%}HeTv|CL!CyW)CRqZ^J@_250a(o8?7zZzYs2ojT(5Gmo4Sf>s#u&Y5<`r=|j1pF?MtXXpsO1tv($0;fPV`iiP$@~6B>%DtN0l5|j!CU1VGBxnK5&ZAFc7Ka-8f74mc2mybMD{cvZlP^56Zfj#Cc=>jZem<L+kUm`68;eh;qvsXiFmImP9im%h4nzJg|S;<H@M*A9|N1{nFw^NmT4fAd2;w49x8HYfFCRgZTLMv`jYcOCWM@kys$fP0Tl8Iu9iRPf7KFhGH4WTdXZD1soNV1m)eY69!7V5ytRI)gRToVNZx#Xj5J({g@aY={ew+GEELGr-RHBw#K{dk7+!tH|YgP<CNn!doNRqq=Jh|fB((Rs^Vr<aTB4x{dsHQTMOS>_-0k{{(pv>PsLY7^8fbd&7|UHQgJh>_$Ve7`F%|)x-ZqFq8d|(mGNqaiu}Th?__py)uBS3p&?$dr>N35)uAGuIaK7U4i%$4MUr+zL!{Nrsy_LRSyfDi70H2|j&c}Db%FlP&MYaABx<6$FN}T&!DLfI%_YeOAufypoL5S4;X!d?1hFs*;CTQPBX$fDwkv;T>@Xed{o<ARpTSSo1k>eZH`)<QpAzU`VK=cjRUGx#uir%#wqMvaum(w`<BswUTZ3b$Anbyl`%BDC8^YXr;>0VXo$NKn*GCtH$z@`+T$o++c-Pi3X66i+uUu+NG@U?hw&$lL7#x@87=Dz`pI-ESVKFiJOPIpC8*k7+jecR`p^<X(e8Z(aaOypB^3X?9i^cVXsrKW8MEOY2NMypzg#Tyu5hqpv{#;x?TyUHpZ5%EdBlvXHFXAPu1b^LWp?ie~MY!%D5o+{%s?ASeQ*+rF;C-%Bt`7CBi^rUPJYBk-aPj=%wDo3Jd*WIUUwDr5pIyC9zxZWz81Uz|17Uj6of=An(I8^{=ihe15GD_V;N5Gld^{jrJRsB|fBAziHCLF7DXilyKlsx1gsT@kK3Uvma`nbXjDrS_J872lKi#sS#+hgSdt6vOy!>bVxqxN<kM9q!xD4WnB1y-U;k9CCg3nv<2qhUjNAMs3lOE|L{vJ&Bx!W2uk5bttLSvfG0Id)XAyv01+-{ICdZ^ewmAc3qV?m#I04xiDWO!*up{~gpBUCOOu%LwR^b>=DRYKOKBqfdKtJsGOJ_?hYeqo0ysU)exILfIG8A#*O0^{gvZb;EGO*bU@LbC;s&Ke3)6TKJEurZW=R3XxtOsf}Qhy+v={3T2xLCS%&xuEZYkXcd<oyGJwC*<6(q>x$q*R6+^4)f#J>5-o+BXcOsd+50y`D)T5M;_;rBsszV)l{M1^MNlU$yq67jkFVl%qTRrf5^tJq5O`@p0y5~E~%3DRh2xPsgetR4`K2FQn(9Aa>!8luB~NKNRo@g6Vg3#4&~3smt@ErlOgBBrxH1a@f`;AK!QN}`|pndd?!J~8Hax&J-(X8A9@d{)so4-<;>!V0VFns)%>|KqHIt+kR9=ofKOL3fIE({G-3d8gj5nOCZEFqM?Qa$I#eS%5?Lq}2AC?bSGuW_(L{U|05HsWQdxqC<X6zlVCoLyG<Vd~L+zP>ge=@&t{h%c@eJ;_p%fw+SCa7o+;2ToL%t^C1E-F!k|tvL(l?$xH~;kdV#hT-XGnF;mpmW`@7ZnlktQ+{NE6A2=e(<HUwN7RH;^1C7>1vD=Gp#LC{N-OH&yC~E0z2lY<<jieFO-$txKdjxXv~ZQ(on%1NuEq;>9E3TCwFe4iQS`id-kAQ0JYbE2$feGPt@(!7{rH8ei0?CyUG%owo6tWXj%cfa02Bs&VNYnSa4<mbWiyGkOnHWUaX4*g%Kbj;B17yBh6CDxR8U(jPN&W(Fe&+#m^A_>rSk;q@_?V!0r$got36Cj*vn8nA;++twT$f}YoCX-T_>M23(z7na#>o-cMl9+!Dwt>MD=8gCXAytvR-|H~06+fNc1K*V-)m5gZQ_%H@>jfV0Gp$EYAFLN-h{$*PRO7H#F%XC(z)kYBbJ?|b8Xi>X-suOCauIhwq>Jql3vsOhyOkVeAMAka9!|tIf658S$qVO&GM3Jy+Yu(RL+%sLmJW>cj_L$TOS5;U|1WII|s8QHTI%NyPsBC0ZGE48`A>v(x2%Eaq52O}p3dvAE%--a|>KsbK$WjM#C|i_&^TW1xS!8Jw)6ARvXzeXM4-tpMHR5p9fwXw%k`Cmq@`c-zRwwIeu!hHXwPea9(xFmo3A$B{mC7KDdIG(nsaJKCu}9$%Y)sT(XAfk@X|X$hCKeFQo=GeXB1#<}i1%aBWKXHnAgR;VT(!Di{vw|bz{JtC<{wD!Hr`=H@r@5BF(%tiF-{8gne2rPrlZ~TK&Gd$ttwXCtoN@O<903Eeg$4*_vB@4oTXOPS=2N3a<bJZ$vJ9-1q&|IJ=-!(t*9jlV`@{SV$0Y4`bTZN1s{HDKlN#A!m99esatQu#DQP5C6>WibK<URC*D9*Qti63b{%JrslUp9!vs%jXKif)Axp0uUsabv?X_XnYa4F}$KA5mN`0*Rsrx%$q&vxgoK@rmec77C<GU|flUyeAY|Yz_GSU^8s=d}2;VgVfYDbk9#ECBnsk*I%O$f-&)t4kddWYl!E*qT!n58dCm&m|qPaH|a=i=60+)PE{TRD={FoW?x7e_l1pC<4sexEs#P_Qu~=U`$&=14*YV;UVvsv<eV3GU@>#_Fvc1E_FkPH$K*KQaUOUwo~O<|d{d`-do?EH$QfvN|kN(lbWT?l`KEie=AHb2nM?k@87t<1XwWmI439U2+F!-gc69%w)lrzOZkUb^<MY)fs|V-f{>Qn{epd4&=Wm*{;XE>&YqO0i~bf;BWPqc5(ySOuweBh15OEw@c@F9akHIT|26ib5Bric1RQx=CySkOqjd&fMDl(n_0G|AgD&Vr5FP|oV4_xT2OU&z;;93=7Ex#f&W(Nz(Awjrrf7Pm2W|}+>|~lm6rfkCH-Co%CVpZRNj+<%f?(>&DA1=M{eHRW3cH;Zb3uY*wVMo!4`s|5OLs1wvd4lTi3QOD@Om2{yFlq&o~d<F(2jrP#%KMAh%;*0r8mUx}}X^7D{+jxvjvDM^Tn26fd~~sI%<EmNEN+Y7`Ok|6$YMmbm@5%!Ev7jFTZ<P^6+g&W8ejV+ClIc~N^;5ccZUR7S2uxOqq0>N==Y5yhQ&hDEZJ`NlC{x-;cv1yC~!C%9XUJ3;fyOPnxC*6CPl);3T(mySfYEOj|=UT$49SxTi$$4y^3cu$s=c6^;Ga*~D0w#%crD;ci=^z*J7S3z_k)wz^E^Gt_W!W>9upjT3F*h}tZ+PDoh+D>wMLI7&B>j^cWuluzu14i%*e9J+utuDM)(@e&2<zxkvAu<uZHcOV~d6FZV*<X3#E@E=#v$mNwe5{%FfBh(~B{QP#>s(7#4B?iRC4E1-ySlf!mdNum&0R}W-15dmX&I|-%zw=2Wexqun$dr(58Py1T80Zg{%lCIqfRF|l_a#9q9;@J4OwnV<myUlcAx7xJ2>Ygr$EvhuO9t$#Q=GtvrsmQ5_`IKY9uq3X#*wP=zASZYLuaOFuyV@H8+@Eci^eM#kB-!hABW8Gjtz2J@*@?sZ<sERl1Icg{D%Z3brj9E<Np$5H7dESQNI3%`sxlq&{(=)>EdqQtM5UCmr4B47{q^Ihc9(;lL~c`OHi+K{dm*P;`x{?tdh%zS_wpEbJne<)f51Ikk~tIq>2CP(0jKb*;_pxghj1-;{V*7rv?GiQ;A*gy>P4QaI2X=@Pqvpnn~Lg)PrNnys&JF|ngh=5u*;iRw`bC6gJBcjjH`2UF`~;?hBg1BYajc1P3xr#H^cm&LgWH~j34x^yEY+*<h74!0KmStZugu=2*O`5+72t)t%PH8*<Ajb8JIon8~Z`t+JF;^!4s%}Ap;XVokyHGV;<89#fGQe%GP`q$`}ovS<;!ChGMHzc!bvgJd1Z*J906L=Y*3wT2e&%}YK?&d<y7_y}@7|guPyYYAP9h-4Gm`|h^`8lhmCS8I-708O%jtAJMMp@~JNOAp7;Xm978)JSzXJ@v{UNCj)bqc7#jx^m!rMAq!;_N5SoY(?l%ya^GIeI>L)OiC53*MbGY|Pu<dpF~txH!A`Scy%+l2zmFpYUv=Y&XVdF<xYHCr#weNH#(#+9gThCprVUT_Xc|*4t*s=w4hnCDY6(Q}SqVr;WdSaI=Ry>ksy+*>lv3#H?5sC8Q%M&rkS}iM;g{)77~&lLB>7+1c5PVS?(Lb$kW#$JvY5NGB6vWlo)`jF5?=u%wkN{){ia8_xbri$7mrx45$lTTpFeIJu<SjC2b7{oM&SFT8d6VqU(~vv=#*oTxVLI@QL#NVPeq*NktCPu%$h&*qfs5ywAKDjJ{oNTzYk?6b8yop5x<bDq#su3mYxr0~fjV+BROhw<Hu#FrP^WTN$?3vG4&OFZGYjQk|;=4S}?%EPR88Ih>A$@tbtkqJwRlDg38E5_ftM3k8*cY;u#R4jh|wP1z^I2gr8&C{GT9)KJO2MYD8czd9eV-hkuHuvK~iq*0u1w?amFTlfH7@%)XWpPhBj+1eKr+uXS*9oFX;jyhp-pN1#-<}CMc<d$qt@HRe$OJl4A6s@4P5=p%TT=KA1`9D2J6#F%qkEz++D-V3rllx*Z78Cf$N_RDeg{v15RNQDY<V83mc;?Ka*}r!3|*Gb>E0k_r&XuldOyxm(?VxE+&dXWu$X4TuqZsQ?M3|PBK=296*kens%42Ra$yQfZP>C3tl$!W(YO|UV8costD4{=OOBd!1M-=y&f*DLA}KYBv;%=&D$UY}Q^wA!G(o$W_D%YhunEqB*C=ghcIht2L{Pe@gbevgl_EQ60OAjJ@X@N^fh3ZZL~Da|pK%MA-}j-RqGa3y&mxzMOt0Z`F>R7{Ds*Bazw5|qJD(UFYWk6-CY~J?0OS9>czPdBKUy8Pn{h{4XT%X%S-fce4DLu{aGW$6o|p5<D3P+VIV_9QG;zosEv_qTB+kU6N8(6-LL5O5R*55*EFcX~(fHg<+KF<3lN(nvxjh@2!oNl{x)!SMS=csXtX5D?E)x@Lgo4oqj0bT9*iJ^tjaVaI3^+7wpt%CjwLTnzp()DObiGQ^GuFtg8f`+G%YyX&;})d<dv(?P1$EWD^eOM=U6nL6$j{O^gx+pT1VwX|B`Is$JjYQaw-d*SV4up8oa>y+`Ut!PsK-tYD8vCV7?y8Sl{dH9A&nllP1x4m9y)A-uVDrIc&!*_wQ|}wL(<~B?3nGPj`?6VZm5*YuvvX%RZ+5#1dY}cGx=Ba|3y#1XCKTo*E?e_^|aMJ?}N=rA8f*%d9ux220v0a{I74t_*)hER)M?yd28WY3;)CM=dCGj8kn~_{q4_No&Hv*zt!n)b$UBh`z|t={?d!7{?hym73}xRYP~F`lsAH1=Tx(o^d-`F6oZMXYc_NOjEhpMx5CN1X8(m0>_?f(lY+hT?yWU@<T2m1Y(J}f<KulTBKoNYJU_<Xien*sQNN!T@8_zX*K78wAN#PAG)R-E@u3$lR_@&k@|aE4J&EpIS#+w|Q%7cAwqNRb+PzPWR<Ai$2P9p57^bgFW?<`rKh?&Zy>fa}%R8F-!{VmmiP&j<`u_AD!`U(O5<bBPv&VW~xeqc_t2(_?**;A5`!iKc=P%Xl=gNNJ?P8dVg1vVyOJBbBt^87@{AF3rg<#<23Vm?iok$~|RCZl(@BF=g@ORG&`L$U>c(G3ZvUKF>yWLCgUhEhrub4Jt^OnP27I<8gz^`Bb$y-(HGE8umSKjrNcPCKD>#pY-qU8($6X;^=PLx7VP%`JQ1V3tKj=G@Nf0<Y7N7$1PX^TAi@4Dad&5u}>Dd+EK0ZOMSXn*)ht-Me9o-TlIqFJGFhHOHD3m4hh@&|9|W|xJL+rckPlTs&}v%MK0CYAh9MMwi>;hH^^-o}f~v>->JeUCzGt|dacbA!!UR`|Ob7l`A0EGN0cYSRVxK#p}shw(Uo^L#g=IM9;e({hp{6^JOjO|8uEiHrGI_C2g%QAca-!Z-P%%2Xhe2Dpor>v`5XOxV`0ev8FW<Wn|`O%U+*Cgxc_@ojq`_Cbv4J4Gm**R}Fg-7RW^*uMsfUMLP79L1aN2v%VWh`pX0|Ao@@RX_%_G`@<aziq0-M5+=dUb3dIqv_+yNznHM5?m+iXBF=vo#19<eL+NW8*)RYK71H2ko5(iYh$1og%y@tcgok7LR;u75uY_XM28b)pOs1~mry_@G*w|^sxY5%_eD=mYnWZHDrG-hVDQ)SawS3A$f*D3(Xg&6nxw`>a(|>SJ-{v6*pK{vinoR#u@1PN&hI4!rP|&lu75M<`gi6mFGad~!An&YnD>3TCBpyE{bfIlq-ny7fOT;4*~6Haa7lfFM<*jl#6XbSaPi3mdVtp1QDlWh)JR;%xN~on-z$?8$A39pPI$JZnb*+|v5X=7DHUCgD$^!`mPyOjU7`Hj3y8w)5|mxG==gk{Pj$_rw8OJX)Hj!*F~BN426sxn&MO=%WlXg7Md|y%y4ts#*cx^)sTiV{W#1*0`kVsr(wQX-2(#a+#;BobJ2LyllTL2fRp4YA#+?m4!^3o>WC3;K_`T<7^3}Jpmb>u^tXFN!ao3>#h%X}iH<%e`l@45+z(@Cw`d7LwLl2F;AcNhF7YEIZp5jGmDAPF_3hnA8qS1IU!x1;rez&8PF@anbd!VD`P^B4I+E1L3y<a7`$x3ArYpY2=K>((7Nd$N7OVXaqv}W&lKxcbljx;_r$|v)uSvF%`N%lxNG4ZjOO)%}5>xvUhZr_^<atc~*s?ep>BCvdT$uf%{?+x5;2V`&10mylAvm@zKBh^cEPWT4cF8gYr?5iQNpF$E7nKT@Rc^{AN#=6?c?wJ#v6fQ$OQfF2;OabUr4U}g-%k`I_Y{7T|F{u$Gj~Qp5@@mylM%%onwI?<RchD`^qZ!+0`o?IzoBz4x#c*`Q*`HK?dzMyhoNldAYsgyL`*3n!^-t@Tqp-nbay=~=Vf<N@LAZW%_=Zt8Tm5{DA~p78qCE~o-j}UC24(B~{81tY@XSf!d%yqwxVA4%ZiSe%d`WR7n&OI=I>|M;mBto*8X;5ZT5~i)w+wgemizVARhUpPm8GO$gO6HLQxbEHRa`AFfYxForH<$;aEMJ_y<`+}2y5h9zW@=13m_su+g1&Lng(zanm3saax3QyFVP^oHD58eM8{(3qtc-h*eSH^>S+dWqt;5xCTh>oZD+#jW;pzDh1I{~e+#QBJ%?jy?ZKDWJ`9bLh3KT^uGSoHLx*VkO-R4k!Ipkti^JU)OFvq1UDoXuA}L*i{3O7oDGp6pV1O=G>`}(S_eO9uH}eAMHYL(*UAOmntw}XWvfDS11C_+y=M-k+Mj{z~B!<shx_bBpybe7zhXG@U;N=iLFC83@9WgHt@FiX=eHD?KpmrYekdWZlwpR8rq`{P{rJ`iCGy7;tWi9a6k&8#>K6jw-aUWp+j`_4fd#B1@ijr-^sbkqT4Q=^7m{Uwy&|8YEhrn^{Y0{3A>6RM;CM(dbM83+@+$_I;yY4W{5Lrd33?sBBa5U^ZOykQhpJEv{$@xepfQ|!$cFj^4f|ATY)>AqEGcn4UIb#Zem4}-;_+gi^l0IKSLT^y~9ywmiIB4T9FlA{`IdaYJ2aFhNlmMK2ZqhH5lVtZb6&kdW*34eEwbZ7@O1Z`o@WTK{cn%|{$I)?$y2nfeN&929)sgEply{SYaa{S4pT*t<j@Ib@6y^qMdH^=ne{PaXl>fBB!LR!eqwP<--$CD8|CH*sQZ_1=d0Z$PL9FTlVN>RFIvh>D4viOCkU>0Nwlr~l6k7mVoBp0Rgefzwj&k6}oLhqEbcoV7`V@mW4ucz#CO$l<ty|FRFwq^#6c!b>-zCgX<(y0shhx?G`|c62&Rq<j9Pw69xy{uOzT2s{>f@w(Nn`DZM-99tgEvG<$1;DQGnN6pI=T+i1J<G89=)a<xleIbc5LgYXFg!ua5KEYMwg^8{^R<MoW`%diilCBfM*x)TovC0FC&)qck7$1Jul|LVS}E^UBSpab8<V&gp$U4I-8TEka&N+4&y|LCsd9pyXh4_?xFCl17vYt)^osF?*T=B_6mGr-ce!M$pfGq!<KstE47D8J`XsRWb<?ehGW`**~zzDq!Lda^eL((YOAh5HB*M4n{lMip{2!*VpH>g`L`{QDUJR8D~21KCoy~HnG|e9>n?(q(ks{KF8!I?#<sZ>wqP=ks{;d*nFmaoq7^K^^4TD7LJ>Jcv5>Q4j4$Ed5>ho85cE#kf(-t;YQa$^PbyAhUN(Q1miTo+n2~wMNwz}mOXC%flyGB;B=*Q;gmu|YQq}cfq2Z|LYCoGD1}Yl!fnFaQn}u303y4^0lUxPX7{?h|Hp_OYL<r+5iHw%t6&E$yr-_R~Nwh59CVEqNnIH2mhCV7{?-q_Ju{s*)G2(WbdFbhIjpmqw4SJA5CwVq;bo2383>$MyF{Qu8o}^5CCdU*#N#vfA?dV#)C9f3Jl=T>K1&s<rB1#0h0#KDL3VPmw5Vc9ZQ!3PSmf;_$C4Myu^KqU@dYF)Qo~!jvDJPM~lk!cQGDx|I%`GybMS*~x@1^QaD-4!%O#!>HYTKcl>hJwbD>p{lM7%||u^E$x)ae{I5fm1sygMTv?I2Ec8oNoP5l2d)F;<1fW~R_s#%<G3n|ah`9JQI3@{GO7Grm=uaS~=sU!E}ISHL>ufB0y-+k_Fj^bEVwCFiWId9RcRxIMvTm*gauN0*;8ZE#!bm8N)`y9Gf@PAA&hwj)go>Wh`5MbX=aT|kBMJg!ZgM0z)}VNR(q%{3~_9^Fl;Mj1USr;(XcyJK>sZeD}$xo7R_p4Fqfj-~d4=BWX(<2`Is&0+*kJ}mdFO}Hmxu?_`v$#&wzs57#MetG>7<IMl{8!hHWi@8w>Zhzid_}0QVTFi|Wb5pRqF=K87jvF)P#*Dc!WB%b_#*Dm{cVoun7hb&h?mIJMQhsk{jEWGi;>X~yMuL{KPKN(mLq!@uc9BqRR!%rrIL;+rhLA=kVmXrmtelvxavI)K$MXF+G5(?=<tZB`y^DzDdiFtocCc{Yalw6=pMTVQG|-gF6xmoWko`)8<wSbbRDjb=5!AhhWaX$=IZ=P=6$%kD>Q#<r%I4p4)(FNpsffL52<Pqk*U4bXOUcRwyCqx@v|K1v#_0k1crI3X#^8DJc@aLK^T!&esX)k*`lF9sJJ+0iL2&XVwaIhxN+npl%r$w-&+Zj$mHNFGnH=^Um$%?1{z`a3&+rAs%h%9QF7i=cFDW?}lRTmFT%gpvQdTj&#J8B9emo;mq<VLan`s_~k>oKy*!$C0E)rSXJBmQgSw{qL&J-pq{RlJ3dninX%L<b(2yb3K^SQQUSZYfqlZBj%PcDQg&q*!uYU^E<mlXeUf{E6ji){D5<bK;X+2<d!f|3cp-T8C`NQc1`>MmA>S)sMpLuv+77|e+XZ+R-OnV^5vM1>zKge$J;Tpn!vb<eg{UD1d!-|<Ld`;X<7M-)YNlxI|3JnUg%l~6&$r||m|fDP0)3jy9;24=zuA4Ed|#QGDnYRAkmB$(SC>AZzkR*B>rRoug;o=#VH6uRSLgXMG&Rk^kF`2wyM#ntRq0l=1Yr=pH002^q4Ho0!F$**NehsXimU59F8ql^D1VVxO${;3<@aIXCp+SUHS%@Vl!;Tc$x@~_|dZI9a4u!Z0y+G9w05VgkNc>toz2OHp{17U9nC7+4u(j@M;<!zMp@!2(1_Bx#E4NIWS6Mp7~RqgURHQ}~|iaf8~{lIsj<v4;?ea|W@E$YL;)9kby^H^G!Cy7ABl{*G^gou@%tzP;ZOo<<)co;UjasXgsT`X6NSN0DyfE0}bGNS0FJ0aYDsdUgGp@X7TI+U)v2GFKKcbpQ46SQhhK0QA9(j;ryn%<+klz#WACa8T}t1REd=L1brg&zoR3)`~rz05fz$L}X}S;!<dZc{E{2tOyx1tdM=4+RNMpaPUA$oJuUz={f4kJ72)d4h`LcgxSM(QnG}$ABUx3%#-2@!C~ZZi=7koGX>x=)ugbL6UOZhTqOLpd9?|E=Xxk`~|-&p=mh-$YL3;%&}Zp`@g@x<7g(8?ULhY-Y<Df;R1;%zq{9{pOKh`9a&57<uw{!=QX<WHqx(ojqc~tm@6xtE{RKY*Rv~pi`S@MdX0jq<mAsgF_jbu@0_~itGq^=OJ1YmikCTav-BFh$Uj=tVmo4$dE_17o|DmN`Y6DFzy5woyom`9zX6zTgztKFUQi*aC|O>?R*iOwkd6domvnCrlSl1m2wN*pfD*eV%p1KyaN5SRL{F7n5`Co2tHy4O!X>D``XFB+jcBDon;d=tkeK|F@@$i^>bx=XePsKX=`R|oqpKLDeBCzKcEwi=P#Hd}vE1+I8LCi;)C8(0lQK$JN|^)`5r>is_K{d7c2dA2%A*dzyzLzZR2dqXP^t!?T<}q15)lR$xlaPKLxMO-1=CI9y*mFf7`iY4^%)x;xn<`~|H(Cm*}(YYP*+G}n3cKdzB0@_rl$qNY=h61Hfi;4IcziX%t$g@#UyxTMoVO&YVOf;G}3l?+If*%wj$vy8^)PyIZ>MpL2D@t5mE=H<-3uRDcUOg=_6>oawUU#e#2`x+N7pu2sqJ-^BuDgn6R2~s8>=>+m~<YoJ^{t0ssQ8qrsnjsBoY_{(~gWBa;$bPD7|92fE23ij0ENGHeC%F)WfH1Ok>OilMdU#W1o{8L>>s4hjqh5Ns*5YHSLSd@aq=>TH?YNN%1vD6tK11t-a_uU`?#^C?Z${Dt=!|DU>Hi4z4dkZQw;J|r5Mk&A7^VZCKY)H|DVBf!C!S91^SOIe=w0Uac84DYafgiesHfk`3R??yuB_jRq|+#bz(JeFvJ=pS$zpNR_X$wDd1Oy*~WgNBT8>D9oY83?h%!SuE0xXz-reNVu3n=}Ln+%LD73{G0EkoU!0S6LTZG9D|ls(k0}2`#YI>Okrv(L8uYN!K924Q3!qX`uJ+8LMgX|GoElGQ#m*hH0G=qw%j}G(lu4!CD5>>ivs~#XGHL@@=kx!xS}G$Urs{@t`B)xdYrYQ|2R){Z48m@_OZ=wdU{~IJ$tj+Dq!*S8V7;xU8B#rHOnaeshD>n4~^@Z%-HSreX%uNF>^pDbr%$m1VxXc@<Ptd7J_PoIwCk4JQ$lk<7|IiD|@c-n0--pRtI{bi8@3O!ilROZ1Ol-2#Y+x*>%433vYZ%;5h3QUKYbK0IRT`|N=^Fb2u@1ICgP$VAL>WhQz32Z0{QjIqC2I>JGiOC0=t#phfMODF#JLl9718HrEQNG4_E54U74@-BW80AleiB|%j7EWsrCAv{gQor^yw`(?}sDL==be?-S9ll@LJ?jAjbmI-+G`-jr%N#5bKWZ>?)yz;kRJu+t)%4;KYfUCmGBeMfH_q8K4+sIrD%UvCoF<l*#oyKId7?7b3NRqD@g`A8=%ea#VJ`P1iNP^wh^-%fVjzcjrN-x_%jz$LO!Jy@{p*W30ZTNc8gjp!at?^*Mk|}{s3*h$4(A?Dp9v?)`Kd)iaM*!vis{5swwlVcFeFG8)F#Y%%O+U(X{ZyBN?^uRZQ5x7SkL1sgU)0I0p=>2V<-x6FRVg01Du!^-lONm;OMW6NkVfY?0PiZJgT7ErOL|3b45S8*f&56)OfBsoa4cVXk0VE8lW2Y;;gd3E9<Z428J2Yqi2TS_V*JPMlkOv>0B~f+UXXWj9}zMIN{s+jZx#Zowcu$yBZC#V!R-za^Ai=~vnn)y{&mfXJASTd=i%9!s+<-I{&(~{X-^w+rG~sm8}BORsuR_Njgc)iW~CxEMrl`!`Ul4_n;tFFY{6;Er|=aAdoiYCn5@1+_{?K_iD!7M8UrFMX?u@G#q-~4c6G?U;e&9g@hhfJyCW$wm5ibyOLs5B7%CH3w8JNS<W+%Phw(O8&4_v*NA6-&e0jh))H5$zwe-ZsIa<eIYsBtvf041vD`v=T^Dfh4u<6v29$fz~1uk6vqqF&{&XY}zUE(r!=`>YBR1bkm^p~f~DE4L~b!ItRM$DGlTSA2>o7&qHxO8JGL!MXMb9(tBTuWjgQ_p3yJi2y@S~AHG`}v&d$W3w@jhr@}slQz!HDEk{#CRqCR2o7^^Iq#;lDast5GvPpe@Q*)u68kp5Wuo=Oj&gF!{8Ez5BgdQ^dMYw?-xuMMC_?tvu^wdwqPrqQ{B+B_KBWIvKvKFKzhJL;Ae@q<jlKKrC+ag5AiVuq_@lPT|H6^d%O;0f2cA%q2(iOq(D;5d|E}J7K>tI<fE<gq($I7b8Vrdj>nE4rTrug1~8pHW4SacA9^P0n3*+vfWF07g`R<3yHl0MnQ57(#ZeZ_w9)DnQr#z*u8Rq9SUOX+VL$u!G*bqeRcmS!O%fYkHHuKxI2GQ9TJf@^Fpq4Q<!SorLt<iHXVoA-`*Z%iwTEbL&mBE2e@=D>Oj1<VhMl1`jD<EP^IB9rt(%gF*7%)hFJIQ);eYw4!Wpll7F`$4;B>D7!CN?Qb4#X6hESu|4wyz=a5Z{9af6B!qA|OjGb^Y{FjC6My@wlA)yp83Mq+KuUYK5nAN4YrwlV|=rwYLZy_|SP$qchKBMGUhX3Y1yED+ML=WVJP`71z#OaBqb=AZf!cMYGNkj<Bo36W#UccFi+psTg$p?Ap8#x;WAod~r(=!@H6g_t2RR=OC99L=g}P(Fg$s<aU>M(HnadT1L&BP#?9%#t!T05|-ksxofPwn&t#hC)p#?2>DYG4CnR;Y&M46jenH>Ge$CT6UYxDG`ZPv)4>ihSyN*AT7JV9iHQc;in#cBL$e`e<8v#>~nwiZ$_L=rUmzbpZQ-w1-|q72Ttl<S=wLUEidAMADH7f@FADL7a0%+vTM+goy@7EV~bLJSwMGu)I6py4ZlU<y5~Z+dgLA_)Y-vN!J&L+&-j~3&=NYWo^A6r&^QitE$nxKh2|RG&Ng&jdx-(YY)R@-{OpRpUVLVDa#IFw?Nhej0AHS3ONo0uPIE`xD?W%UP7~<gC@G!rOr?nowLl)GvUo>NJXLvR8YeX=RRR<1CS6&-qO`gs1Pw#JG7q)F%mIgxnayoo<^HoEwkCrZp)`UG?`y5kM*;*8=wL&l3~u`uO+HfP^1F9mbh1SUi5%k7)u)z~vLcbOF29+rM{~Scdn%2vUZBw?R<^eqEt%3MyOiKh|BG|QNuH`(61EeCI;*>1)wa9%v&KHjqNFaJ`^in=VO}V+&d-1ne77`446}7mpVvp4@jQMe&t<hbtdDul#GP3sRvGE>Kc{L-y5gLuud^KE{IWF-2@5p-G%eFtE~X~WbEQod`n9XGV6*xE$$Pg@+qN}5sJBaR{WAKv%rVEj?9178_CDv-*{4pOlS4s@AnVBoeG&9g@{$)d!K4U9LQ)<>Bt*O*Dn_wHEXY$3f=Cb_^hpq+M9r%jVys9gEfER@-z>C!-}krPTOV`G+gf|AwF@_k$=qX((MP|u_FupM`@Eg7;#Q+>Th0NGG*+aU%hx?7WxM_vs^43FiMXqr`R=BAn&+SO)lau3=ycAnSv!~CSuL;B_}q$x^TNM&X^L+ih6l~r7rFXN)9S3Ay&-P()7KI4M@mqC`@^ZEDkz>+QZE{t$4Bnd0EUwDxVROi$K!Ev3!bdDvCw$gQqh3+QFz;mw8gXgzC^^uog}y7aPep3_h)f2qtt$xy}z)J-DBhTd$$pVT~N;Kl;9os**+*cLsI+1;Qhu3LVVYwREGTd()j)Lw}1TppSBfx1j+QJ6<U^OS1rtoEHiszk%Wvdt1@PH7(#-76$l{bQ7r9>R)z&IL<nddn?Gy$kQ1o4$@ZW!>%Q_gu}-&4=)p*2S`-#KA&ESYUp@I;{Dxf!5-d#;9c_I$S%BBG=X@Pl^97oSojXEA!bwywIp)f-Dk{R$ufNwDmUP3~N;`JGZEEG0J2#X&mzGF?cMe;`ZeIKF<_R?=n5_0Bcu{%tA~-N666_(evs=i97ejx9W8hB`6Ewi1`F0*n!xft$-_c%u0Mff1Jo(M?cWn6>bw@$|W;gXvZtC%S&2Qz~+KCA_KZs8qntE4+ceJ>tn-+!fDbZxMDCi}Txr^eMT&d{_EX2Te^ad`$)o!ziLa8OuiS#4LgC_BT@JS3}{!S=i9iktIGTP%sgr(Vdv`6q$GDC7U<<<Gy<agw*1(7yIbWtAMfKM2w+ZdyA7?6P<VNkQ774ZlH`jiN2lCcuwF!uuBY~rW|A|xM=m*&NP1<M4Y8s>$)e19M?fo;2}2#J83eD;ZVCa;VZS0uJr2JaCGe<ZJTGQDRIJEM2E(QP4Ide^kH^!mCaRP|UIZUWqp308U@@H6cG1(xI@sX$@C|KV4&9Cy($wq!ZhB!-BN@yZ~$j5pR<1$D8YlH~ol%z(ztzLHGHsU?FT)Q8Eqa#%Qx2~MtJO&yW6F&0Z)AUbB<jwm+kMDv5*xMvNX5c$2)bLnY0h`6YPR3fN0AsWD!gUWWT{Ps+=YjnG+EE@XR=(Byrl<N)S>V-rStu9%pRsI=`Yu8DYMd~rcLBXlJ!h}4ZUJ`p(Q-;1UbX86!6mn)?Q#4yuHI|SVrlWIHFGk@od3%GpQ3qXx0zP|?jcUg7l%9Pbc7K}XyQ~~mF-tqQU;s;K?F`Q<0_5P%6eo<ZwsG_0tEj50H<R+O3?I$MR9eS|I&z%*YI3k;`QLb+<NT3_Csu!jafm7mQk7xiVqu2?1;m9y*_{b!RP@wB&4?vXx)@=(Gu}9m?SE~K!_wPD$Dv<-8a18bm4E23EQDrXyqn+C-8#_q^#uuNsk7T9#;(K_pR)>fAzLWH{YDM4v0Szg3kFi`6^152NILS1M-yDYj^w)`yWp%KCLEHtV8ZG(-bm@-9vwr|wlUNe=OT^q7`QLCQWTCF%Q4}2Sb43n4Jz_%ZJ7{|w?Wx^Dgx+$if(atVwqM%6n_IW=PY^-iq%aOn&kf*0exU9?CC4diRb{I{*T`V^tt1SkWV_+pih$$2*F=a7EoJ1aAqY(34_{_*K~zp0dx}UNj}gHgn;=5?F)EdB22II@}BhCv};=(Y72_MmTe|+$p&CI#psFgjDFxehV$3d1lY<O2C_iHDY44m;be}4Iv^~BYeQs{A6nnK$S^CqA|k+90(eGLy!jlMV#G>cAV-o0`b@41hG*tMtT4ltoPlu!u9JLMFqh2)hz7tWTIYWSCmPj5j7~sO%}pkb9S40yRO=mUAy|VFUb3AF5QHxQIQmaKKjkrSXWnVbLjV8=%*dUwCda&WyXO7|`)X>!{vM++Kf42%HlN4guKCRQAKl@R9`gHdy=E%!8vo^;ir0CG#N%ByBLrF9xx0eDo$_Z<bE74^<E)VrM8U`Mwp)}}arX%`p|HoPAxmJ`QKblA6@i5LkmFx6!<B>EA3njO`2v{M&RV`TkLFzPOQ~QIfGIDXD3td^qDca7Rq_rJVc_aVAaAgLF=$F9g3k^AJ1R)u6G~{gEeK}&f=ua3=CdW!w}9rb*mJ3jSy0|%+sHr(9gQ5wI}WNMN4_DnfTjL`q8#t*L8ej-&U`nJLN_otlfUu$AotZ~3GFxeQ5;xeiKrgH`QKo22@m1FeP48#0ERr;AiT^^`*?S-A1<^8OSM#pLj#PYaG^D*`bU%x(ao!9^>Y-|#dSOI5n6r6@2P3^HK&|R2qCck7T61VTUz~vL37n9OjT(Thj0cZQKvB0okBv$1OUiOj6CQxQ8T|jZ7v5lY&`P#4#b&f$XLyW5G`2vwX=KrImZ56$u+K;#NofdfeFIq%bs@>Qt3l?Wa@z|vkBLL#nIN`(B0<^DAM<ygH@r6C2gT7SY9R*v%~yz1I}AiI6hTXj$IwK@re|tK993v#;154FNVR5Xr2*dHNk;wn6M&CBRZ2uz>bMZJqTy#8xVTt6W-DU;B7ZpfO~<pct4a7N!Tm@-uJvoH&|Sw$QklG_n7xiDoFLNmG6zsmZ3)58{cnW7_n8-aezybjubrYpMMc$H#xfVuIsKtcCq<Xy1Zi#U^>qsV%P<#2yh=F(#Kp~u!i9NhU~98U()pMwthF*sQvB=1m^}f6N@Y=3OLZQ3;Dbbr))|>w$CGI<^4UV@eK`$5<p~$)mD<>^?s7Sg7pct%JVySHw;HT_6c;@1}#kmJ;oUTM@PPH*t!rlxC(zOMtc{o1RDkwx=`slVc`umeG(u<&=nNpS*7kDyp!>KqL7^L$MC>-vJz*J_*{fS9Hdh#Evsxi6I@o3@$_h|29=OWxNJ44){JN9EpbhC!wL0cVzn8tRVBW)CJ8#-4Rw}Kd7%Boom+K`G@=>Mmu_7N&spB$%ta%PZiec<FNRT}IzM-T!8KhrnC!#)N{U3g!KQhdMG1|ZuIJV=@BC4wQe|&5m1u>5cD7O@A>eA$J!dB|+xSqBMC9s_NQ@sC&iv&|1WCpZB}g(nCrHx2gCI#v$`#gXBypufG87$>bXkYwT!dsOA|#F?Bzdj$MTEo^5fb-=2nmRg-(H8Le_V&eGfCQ4IwUHQy{UCbupLS2k0l?p@Zol?jKRs|T8bn`pBL3gBr*AfAW4fy07x#?Na7=EB%8NYBbm<CNKA?(d`qNA{t-931odP;!6{F7HZ$>3_i$s1%GfAvlV%)*CK1QAw+PL#hCj4)Ef#QF^1mn7KxiHk(IXL9Ce!N>oOSlTj9RByB61eea{R5oj=^-#B8%w^(8&>T7NeWEt5wA$*_n!3wtm5~9k2|OH{7QztR~r{s4W0U4em=dxQ`Wq&SRWJJ%HXyu=wJRd+xx0p@?T|1ayw_mFXu|^|&pN=xNf_Q#y6yAH@S!$OQ}Z;}Ym=W}_k>7kz!BWWWvHLVSz+gF>(3%rr5?6BDCOGHD8Unqk2y5RJsI2r71wd&erdipcp0TDd)S1<vHR2xT|Gyfft#B@AAr7GV2Pw6;<@7IsrGo=+kTq5sf~;vNZ00u#88eVs_?Z^+FaLIbeX;y2xLefYm_{@?%UedWl23_J&-?V5SK?CtsaCkaP9$Inmtgy>#D&hO92`J?h;#&0b8wrV+)FwcGSEdA7}c&`-wgTE%Gpc170c3=d4%NFKOo9X1Zjh`z0do9Mib+#91O&A-|vg8xroPk#eoNH~sqJ3DliJ?7+=79!C)wGr+=lq5Z3nBJ+xe`Mqh{!(LvLuO}WgCFKJgV5N3O0DEDAM%k^fD!v?Jm%kfgB~SnX7DzrDiT*`nSR@!bbO&7MwKRwPD`C*~QRRhBem6E`&O83>@8FOy{8U@mF0lDSJFv4IY7a>rV+8>_Myn0Tlq8+m;QT(i_<4>;2ciF^M6S6Xw#W4E345P^trfGkqbJawA7E-7>fuG$AECD@M`?Ky{^+BVH`RaT0Y~Sw1bVqw2GiM&VEjD4P3CYC<?k7=jLhHNn(`m~f&3MH-w&95Q9z%8BQr89GxjrQgIGx@1Gl?T}L*5`1{uqFC=BWRi$(krKif64B#$qPD|15VC6Gpi=R#0=m3+=@+OxmzU0#<9c`Tih96+E+^n3ru(MV^i306yu#36Dy$jzR%g#PC!7qc4D9)Y0+0mwbh-UCn4Ub#RsBrE1STeiNc08w1n2@YJeW!keT2ngm`J=uw*Cd`^6U!dMHxsW=B2~a2xg3FYP7Ztv7DE~Ejt90sruMI&l-%>f#UpP{)w!IxD!l&<F7mYmBbH`6am@jw<JsHdq4DqN&_Sl;vN~4_nbv#d8r);oFMT7V9bpEyF;_d3xZ`==8z#>8|`CGtNgF6pva;H`U8SSKI^caLy^0;fFEDNkrvtC7eJ05fKe;3aeOdz^9<Oy)eO#K7~@dD08dQfJOwS*Ps1aaaMas@iqDY4tNYMJ!*6hf8GhK$Mf$L)Th*u6zYapIQAT*f=@sDN=h4EiKn`o1Q4vmKXL1oOd^XAVO#p_!6=-4i4?ebL+`9{OvA-oX$HzzLtWRbWs!NJZ+=`QfNg8WuRw+T<GYgmXx;Q5(2vXU>si~8Jr!d2hCIi`nrjiI-K46J$-_^;0s%0hB?W;~$tCXPR13d_cu1S$5hTvBTccpJbR`8#{YgeMH3QiZe56K!)FIYOW#C{v3S))%0Tx#g+ky&b!in~%hVnDtYS~;p9c$?Tm`zSTnYLUhwMH$2_1+Bl?q^3}>%F3y<vu-87aVt;Y)d$Ic-xfL12dj@0lxOZCA|z~S?4?NyIn>7Aa`qhVc!Pe;hVXMovW9NXC{!}JX{bJ$7ZGEasnLZ~X!c`UH&et+S8o*{UFu?`wRL-Ru{djFJvDn(k7YVrKIuWI;|m)m*TY#PV~GdWMp;B*8QSFtgg21c*=kxDIGT{1W+4PPYHjW*R^t%j#B3WorD}0KIwss*vTnCBkyo>IgHPNT#XT1t<W_+^YOBD&P$PSW>rLg;LABTzV`}BTPmjz3$HkC+q*eKE87=b<iICgoJcOz5RW=;xTqiEf{MwXLvkAzvc0=|ALXFah&O=xyR~se2C*wys?1EIJlO9z5mV@y%M5A2BL+Eytm?gW2SKm2$kz~cK5SokXEQT}h@$*1nt?w->^SvFj6;6s{pFmX)fD$;SbI7cOD~pY-UL?WHZOO~~HT@l%Ed<XZzXA>AJ&RNNF3;cbU5PbtHb8Acb&o_YiZ_jkGsa){Y}qGW1<9NbWcgubO|z_?-<z*Gwn4dgzFp%~_??jcFx|?>{GH}im~xEwHqOnMa->kPi|m{>;RYFQ;LJlZS#l)nDL)GCxxi9Cf{Whyf*MEdhT#bttk&1<MY}0F&|rAKGwBOzScd~aSS&8iaN#0&8)m5npMB79gBp7QcJo=VX%UPR)M8~XE^~{9Z78N^Z<{=8mlZh1Xt|4edkg;18%v__3y}po-opB51z%nr&~VQ*Ky7d<Fn6@;CHvz{VG*W4<i`94w?24K{(u0poWT4=$|&qq?ZTaLk_gAUfa4z~02SEX+hlZOS<2a)efTa9o62p`$Bler&Y;+`HMQx+;th-tInc>{^}FvWxK9^@`&pq~#Ly3ed-}eOd>_XDjG0DDPa*!pOy8KGD>U4LbRKkD<UY4pKQ6KUED;Ta)iMoOW$0^)47xu}0|G`hm;9>`pA#^lMEQr8MfqpR_*6{>wxW1l0)00>Ocg7punPA>@rlFZ;r{U2a6h=wok#rsQn=rJuyFsse_sfse0AIP;uY!dP$7`of;&E|RQ0SI_XUCEz}yz6^EFGlq>z$^OA2<A4^v3Z9Q6CT!W3;hPO|`lej!YYk1bM|r$j!cP>%+*mV`bwAn>BWRYM(F4ohNl8a+;$1#)gI69h(4!Col=MkXEssyZ!39H*<N9ACpv>OM9<Y51M@v<zQlLmzfX-@%4H$~UywP{Mtxo@rSx?`B3DK<L6Uq+;pBH(^7AXmW2hXs3q?I50Jp8SUmV>!nyiUT?0`VmCKjs-uQV&|2`DC#+|^V0$P#oW%NiMv7IL&i+H0PXCX-2qT-9$&ZP7{e*eNHQIC2so8k#Ql|%-ckt-lk^6RgD&wAnYfKmiVG;Ej5BVOdBe<^+{kX$Q$**i~{efQi(|qC3cX1$|x$)o4zue&~(2B`-{{&9E5g*6u(*g5?=}w@HnXV9M_rLxORqzhPdGQ45nfp63?&W=W3ou}RhfwK@Pq4U75i_^A1hMip1{xXWSwI@?AF&vizxUpOoj-5EAM5$aNnT@Z9c}uM8XdvHR-`l8o?olJj!^B?Fe|Wb77D*tg*L7$nZ4VDTjMWkR{w~}iKYDLOf8LA|M?#pOZicR+xeAIT4xZ97zkL{UQ>0%`Sw11dYYN<LiihRLz#Ix*AKZ&_br`}zA#k9g`rCQ*tJebRSh|sHV9`m&$L0{Z$&5E&s@Tj$=1YR8XzFZJmabIP3IqSdRL+!E5fQXi4Tf<>^VB4ex);U2ji@YGiR01hegN3qp6R?J*UwF-QWSAe@dxi`|-O1@n6h~qMs+@KOx!q2|V;E=HLgtU;N`QJxxk%DVC9M+l}Vqkrodm0YD(?Z2T7dj$0VmR)wh>*y&DXt6?sD!kKJ(fYjkR;p|8Su)*A0&&Ijb6M7N)Fr8IBAQ|;9ZfZLagW6)yWF)pP@~xOxi=-#z9A+=m-q}oBYcN;1!6<mRSIEu08J9_KFlsWYi34%1JI>^hD@|ySsF6fJPt>7g3seR*OmINXUqFe9y+81WcTL<iI;QeCWXSpb-+SpeJ6XX{dI(G10Z$|H(S4~-T{z5>>)PS0=OlyIGTj}l`=_5V85?>KOK{s5R8LthF%<`ipx~I^G|lLk6;iYqNjGe=R3mx;tORC}A2q!WY%Cp3WgtzHn^_}-)?@nFxQB&;kj`PU+DB9L4+X5XbX^8h$M35qURuVQtx^Duldv@XQo-Eg#PmUxEcvKi8J)4+uMy!@GQXMyckV&&wA2pr@xErF>8UU3Vl_TK&v2*N=G!cOq2>&SV6>-+lO|3(%>4CSHz^-1pUUU<sR>lBzN<{VH{QkrE4eurN(U9Aa6fX^t+j8TU8<FDoG+%$&3yc>sTf6_ok>{Dsrzy$2AYkZ%Q`m7|KM6M5yRv7nFtl|7{_`qUJMJ9fp=>rEpODTf8;leukRO$=|54#VdLTsfF^0>C5p1aED{6)Ptnt=t8d-JHX2!<@<Q1BdlO<rG+r<;lFJj}H3aea`cZ>s6Mvyl+R$UKw;)Cmw+4<maQ3?2OHPL3wcKq#wbCYPi6Ho6T{g#IKcJpT*OwZw_n$N1k4@b4&6rq#?EF^_=R8h15Wr~+aB#pqstgR&VefYxO06A};F}JJq5S7lz7^Lh+&0-$PgE?)U$*UWb2?Q`y1Y&d@q!EaPhUMFeo|SMv>!X-#pg-!9S6rb$7n*QgdiEFT)o&WZOUNdz}b8Cz5w<XRUiV{2aX$1`~W_Utmeu1;Aww*)J#aPh^cN#9+FPSlR1W!NQ{Y>)s`30zz~zPDA@t-IQKzj4<vIuG<j0UbunkrIUKqU&Dg5+h;MJD#U|_T>sl|NgT%E9K%}~mfuvojGWzo7;QcJ|L-}GpWdY*LF-<Q+Q5dJrM9mP&F+0*QJ4?KTWhqFZCYd4D_`L;vEiiUe+`>VE1~xba;}uK=aw!4!^zUBa)V~R+DhzxM`F|H?{rE+p)yFK^6~;I~9<SV$iUp~_#rhk|X%o*Sl0|+}BI3xxDL`fZ-#e3TJ{FaNfi7&{n0n%^nCWlDh|lS8_DyqGJa{AN@};o;IhHmPgi|&MX!PtCTg1+*IH?O(VGl4rDJf5jXq6BV;7__W4aH%RQV8vJS#CC3$X|F}x^^U~g=t1IGZTT!sOwxe5|4^S26_Gn!E;5Gfw!W+5&j=23*r2LgChaxeVK#LAKCrQ56s8^YQ>Vg<SOi^dpFUNR76YsbD|}Q|8r5aM6ng75!W32i<}_)FzuRv-&f*6sTLCC#%?ch@DnTg%y9JPl5~j*a{b53P5#t3Mhf$8WN2L>L$gX-YfNaqzf2<+D;l{})5y(aXkwDvt~k)rngcBr4z%tfr5p*+9#YErlR&Zy`&kYN{=$ojL{|W9NfZJpNWOzNp$o-{M;m>QJJ*p$tjm8z*Pkmn+ZE0{0ny&$^?ZdO?7}R14i7_)BJx7*Jem0?NB}_6v&(T@PGT^SoA(q52NI5!eOtT1$McKXYv5mMT7D|u!H!Zg;HBVTd>ivgx+y!|K7SWaDWBf8;0XL)fa5&?y6|CP5K@67(*67qe1*>^1{xNYYV)V^EBp$SBB>ASb-f)c?zl#Ns*PS>+H!V18>rS(;O6f%ugc{<!<#WNbs#-Yu_4CY#Bhgb^?2B5_E!|Xrcp~CZ_Hrg9B6R%MNFaR0CX#EiNf+^314H(4M<qUKOaB~=L*upG!`}lE2&XDN9O_)fa}BfxViG9J`Uo#xs#~^PgKY%Iy&65uztgAHg%FgGpc1=YGJ!7zaWpQUcn@P$(QD1y6Db6$c73S=~i!ZMR<azArgBNAgx=nXD6Urp%F5_esiz@$%p#Ql;E)8Yz&>dip9$<m(NSn!TZw9mY7bOJKj7=qK{mG=`uBSi8OopDz5lld!WiWq4&=q4F3rwtMey6Evv7NzJ0UlSuMV0pxtBD>=TKZNE)^2g@bajfM8J`-e4kD8kitJ+&JlrOx($kUmOJEBonM+-n>kYsMAb@9Zw{y*Q8$3|6XD2c<1@MQPA-BZ0vSmv)eK|I^{o2ro(qUp}U~@i%s6_SNP?MMLHh@_``d0ijrtJFyGzy&&s$2Fm`*mx@=6Z^6I$3@6(Upz8=FEgPeeTa;Tz2la!u|1ZC!*2{yEvJom3Vx|u|cvmwF~G&9AUVD|lrl1_CB9}7vJvHz7>Rfz)G$}=v)HLKlZ!E#{#rGUUS?aSf~nsi|#5Y0)3X3yWdY%=VaMr&9yGrI~4X%!%g`;UdEnI^B^25U0AnJAE_3N2D_KFs(4U#_Al3KZOQ?m^z)WBD2}U+*j4L*1Y77_Iqya931joH!m`s%%H7em{F6_0Pf_z1;ateJ16d-m7g_ZmJY~3ag-uwR0;5^O=dy7#JDqr*cZ(tuACml<uUYK5QB@Izj?1ICp&TSTP&A!^}T8Po-4PYraOo?->2WR1`kEbCsmB?5s{wLYalttngSi;r>6d>Oo`+=k~=UbJV%WK6w-yr$|_GXme5#0M0D!9CAgoO8mDAZBojIIJfKgCr)z5j!dN-^QK84GsA(zOKLFE8jdt8eL&!!Y_znn;(%$kp-h26oqAU?C<H0&kuj9y{feo)q177@=5R{L$vwe`B6Zn1&MB2dUW1SgCzl3ew(p2f(;d~(0@@v*W3kBymhWl|m-x-R7p0(!y&h9=4?t(+f^y``qiiYB!5trFR6QNU8i2lZ9J<q*WX%`Af*5kLM@?a!r}63I|2v?fJgYQ#j~TEaz-nkeeKq-OS{KauBu8NNu&EPC35q*ah*WKCd375?Uu=wxz+2c=Oju(q;*q4V`K)#uyIZEc9E_<Fq9+HR0MzyU9%DwXGnd4cg+zYP42?<@G^Q!V5Vce0x@%=he9@kp>&b(e308Pod#6To=8+fkD3LbKRv&Bl#ZXwBQp)1Xe->Aw%+xEGnj@xSzWvG+u1!*~^LNzHjGbFb;+2W_vpb1Z98}q{Y7}VY8W&Bk@{6E;vC%M|FEdaj#0z$@1=#n%pzEgfGqBGz+f<Qe?OJ-;wA9Wx85G3%>TDk<au}Mh4OOIB+u6p~G^^#@W>Pn|02W>Ox0-5d*zsBhOZ%BMHb3#dZu$0S&R?UZ_2!<N`Ljn7#%&G^nR4G@rN0454eL4icj8hw$pHeFHzo8-lrzc^YJT%=Li(MT<r_|=@7N}L<JSLtspq&kid>Zl@*Boo{yG(_2#;X|^@e6qZvaw;1fhLX==Bg|LiH%enA_mq6hJ(XTyrbALrrc2p;EskYR@GyMzomFNA~VZ6L~@<?8wPlf=>fFqlh3;Ey3v54Gw<Y7|-jQ{4Ka|=-9(-Pi`EV8x2;B<Q0nUfWZo6n(Pi+`Ndtv<kiKKcdokpE3e>O`-B6vBm1__ZSS4Zz~os)h;9S1W0pjt0|9kgP&@>^1y|U-27k!Da)iw6j*X*i>GBOIvsIy3L;A`qf1ivQ4T`f@eiwy)(|lK{?dQW>`CEN^2;<<7Bg$h#!y>!^0n79?%1a!&HA$tQeT#bW4KtZS#D<}@>mVAXTNSpczFI!32wK%!Ju80d7&PKTLK(hzvNtEYA<|2ArsxXYTHM3clj+>6HfM`wOMj2&AQ;mdmcQ0JlRr&p%vkqwU^Va~dwhgjwABaQPH3QIm*SfE3+~4oZk};aror;-gNoi8cDcq*HUft2$T~AS`A+)FL!;fx_ZXR)ZDUt!mJO`f(sATOa!cmIH*|=@tY1b_b_8g_h;#@LVTT9#j+^X0*#3W0_PHqDI<ZD6e<QEh8}c(1nh!YTH-;U7(Vloq`8ND@&kw$FGm8}?MDQBnUnrVr*(7b0_3{2BUiHYi03c2p6lVCRB9z9fBY~myVMz}rW0xO+)4T!C8TafBU8)GB%E{=K+Krv-!XUlTbrqt@^c;I8OBx>&zcT#?&A+{h0o!Av`ox7WFrUoVB3#D}pJ;0iq~K;Tg(wlH%B`b}8Vl*!Hcg_}N1=X47NM3MO0d}WEU!$OkMO%*q|i|mj|avVhX~>}K70IgHX8$@nLl^fHY(qwICDD#n2?_@qW9it#f1gly3&wq)coVm$$cun)-$?9v}=Q~S~3_@Lj?lHCx843FVMEO7Wjy&YAy@*VjxY{L{vP7-&<Imj;N3jY!W1BWW#eXl6y2*O+~XLxKZ~K7~sycJY~YF+!L-D4wQ#Lx29nl>i7T4^H0^!Y^zQ9zQx&Sh968s!pMxB(YqnR!U>{lID*sHiNzyr!eBTeoc1m686-VePD&j>M26eTW+D()r1;81eK#0$ExEj<>l_wl`@xZE-I@DP$zs7V1d*NkBZny|Bw+#EAj~OAI(P)2l|o|^Q(zG&=m!CNtpi&E;wTJ9nd1leuOKI)YMmiJMp!7ktGB?{X$EkEj1|m)#Lv&4WjENeWKotY;*6^L6zN^h88C}<NtKq!^y~4AtwC=m=4lO?G|a#trn2gHg|=;+fou#o($3hFs5UjPnuF%#6AN7p`>;pvR0@cVfqxOBMVr4M!I)Q%x|4E+KuA?*95X~M6`M((yeolZ_H<+WHct6~7KoW&E|O=Qve1y5wNvKB&Y?347-!LQ<&;(a8y<Jc`SPa4DbJdrE05fI5&gb-%p*IRxokMdF1{uBd+m`m!-}3zrzO#pIp=6^K6k{#wJ%<n@xa9M58|DZ8ZnCx+4{X9v~2&3BUVze$dXEOs~emsvECSA27zEqgv)9`35uEl2#3fVn9p!|aE_nl8%d|s7vdIUva|@{vLhxEO+&5%C+;^kL(yGw#1CgE659)#kLr%o|I@t1hByJ@{qiWaX9I!U@aKW5>YvNDIL|0?N8hk{hYX=bY_-f*T-+Ji67HVa8U0kE)W>#)VgL;QKCv@6>^aR6b`Q4&nBJcYQL}}jkU(Nsy6qW6lV9vb+amcJG9$z~8g;l=oDG7hfB<jA^2hH4)Th<*$MvFjRMviY!P-BTwLk1_Ks8<9XQ{Nys|a-X$a>Eq{xNd{R}ks)2a=`cx7;m_kf(NlTQjBJsG7nXBmI;1VNIpl6QMcoO7a#-N)hb{doEkaGxQV>2}N+x(mB^0op3Z4k~%RM2WJJCa~{>lcFfT9q%Iwca_bv_C?5AKlep}vWN(%?VKA0de-yJS6Tie!J;~|>p8vMcs_GVrgnN|-MiQ#3qT1Aisui0mA~LPe*$=59qx?YERd$|Rs8pZM5;x2eIqgqY;W|-t3wP?}bWsedzR;M?+^Nh{#<G)o-n|>Td}rDvyqrQ;s1hV-giDVqlwmJ5iUg1L^Byg|FB(g#{voNTIaT2uN2^R)gYlVN?jPk{?F;j)vX-YN2A^VI{dQ5W4)g#1e)Eo{oAF5lAg3r&!Ty0$R6+J}j~KYi(>Lo8w`+H((bP*G(HD;xFM7m;qHq@<4-{YI5$O(T6roe|T94TK8&(%DdqkFK-Vi2ea`vbQqP+Q-Yi!90|7zFRH^b(2uCcq|7ajTfKa^h#?j55+_PL&~Sq799-#$H}f9>1Hmwe~O{<-vM5D@V3AdvL^s#ZR=<a-?7B0vq;M$X&5u1+aT;asQWN_3VXy`WUdg+G-Hi7pCt%C6o4#+%_xR>Hb#(23x^<tRy=B)K>GmN`VENiI?1EB1k-^uiO~;;cxSF6{#i>beh=7!CjLhe(Y6VEKTa<KQ1EE1DW}1MS)e9A4}Luy@<KMu6^Vmx>PvXAXcTsd?iEJ|Ol5AoZSofUWe8y!=D_Q?CObenuH)T8FlEokZuMg2Ym`TjLLby#qc73e_X)?;9u)w3uRoZJJurr+J3YDh2Oz9(#sAEZS-83dIqn--i%H!3Y6C9I=R4MhEL3@Q0BE-uDC_QZr&O`dHsl%VmiEI8iQ)PjZ^bT3zsmyHf$Z+E3GX2E_jgC2g$e-*4WpKMj(PeAJ(EMCy5eDrK_txcNwK9G>&1Xc#|TR6#w`RsOVn#-B>K@ipbf;!JzuZs<udu{_a@=BKoMksHPTZumUmL;JeR$CTU`AF3Hvy270tC_4nb#gg=)a}){a`y5C<*X2`zbM~J3hESXB^n~gYAX76v&}>9Fz(`7v58CDX{rBuW3mfPoWkr1U+nPZ=?mgB2rrYu>@7cXw21QuX-YOgHe80$n=ExU#`@l_bGpv&+D4UkDVt82w)nhKieTd>BaGM{wviL8p7XC|CeG6cYCS_M6P*+eK30ziyUO~(ieK2W-O_4*K1F0Z}*;nFOjMocJgCHlGQB9z39Z|8uRH1=*xRSb;@5_WZh=k-l;b-$oY$QjDgH(zMc|jdoPEC>BVedHQ<49ef7mhCy;vDJM%=-v<7Rqn=M6qhpB5X_uJL-iZdx0D_)?p*}+OgMqlXLc|f;tpO4A#OUGi5#Ysl-Y-6iK9H`XAr37cNv$mzsXATQ@i^IpS5_Ha_Wyd9;ykw8rBc&+$0qrQJT_j+>dBpm0WQA2Uf7%9|X|Y?8{-cwrB4TQ+>xkn(3*qWRr3#t1K7i|TBkP&mK3GD%MA!~kyr^o+;k8%tvsppDH_K=tH>{@1Vl@AZ<v;)ZxWo#{EHTFYcr79a#=EU>V9=Wlu4Upz?zbq@|G)`59m9a`g$uEf2gBn5<Ahp=9WNgsTO37b0z=a{hF6PU0ZugB-&!50F;Xif41ybK6yvCp~gI2P9$tmgIgm1>+fe_bd|haf4=7vR7SRsfek{f794r{G`SV#8ig5MI<^@({Kpov@`e;vuY5BwRU%^F=C1QB|VH%mS$Cz;CmmA~10=#3HRp(MqTYw>=Rr-!IZq3>60oOwm&-rI{;_<9iMm-~98i(a}x6jDcX}00-m7nQTLFXJq&Nop^hz@$xuDahTxWC!cZLgp3iMQ=nusBPT)uS7RIn!bEwkX#zsy+Q6v(q9_%Dn?h4=fA})`R^00BI~^fcfp6>BPerafFln(z9X=`aDH~8+0BjUnwDR(5b$d^2X-qME$EF6$Y$f|*T>&~9Wkb+Fhdm2{+XEQSNFu&(@^|$#<YW>7!(Tq~&5?Stjw3uwP5=NKV;VzFSHF&7yB9==;dA&v0M!kb@5A!eQvg-kBRRz3L!wg+nwnk;O<i!Q!z=Prwi_dr#iN~=Li6KWAyPF&?1)QUs$I_@QUyo#62Uz~#JGY>^{;`$xC)w@P2M#DnG^5%xvzW>xW|tRO8v)dE8H<`ynVrL0JlU5-*>R#Z*(Kar>ZqQhi}h!Llq=yQY^=b<HOMkZiv3ONIE~3dxk<{X@4Sh#T?Prwunt#m^jXQi!>MzISUwv5->W>jEjrb73I`r3?{h)`Op<brm_|0C{hoWgP~>q$CtSchLb+9CtfAFvFxEvlTPc1(iK#h7(|?#`^YoPjTgOdggxMCXpu&I#dG`2DnNG5jbG0zsU&H$Vfwzl3|!95{i`BMSBSL4-cq}GCz2E9(X&XCOS6(PkJ*=BbZ)(L!be?{Ifxgh)uzjk<VCz`xH&>ix`)Jv%)tv2wE^$iGL*HDk;O%{OT?~kct&MIlL4cNt<ya2GM?`%;??-Rw>W`}9}oQLJL@^TG!Jy&HvDHJ!t7`8pAQ4@83O8+I|*w8ny$W-Wv5r+KarXs^4Y9PQ(D>=@SoP&bY~FIy1PmKpooY2!q%p*ke~VHA2v&Ovwbo0bNr}2Z`{m24^Qp*;tjFP56a;^33W+`<%39R9&vtN@!Q<0@O3EY{5iO7kt9t0iz>F$(+TQBZ)arM;8yQ98aX_7X{iVstY~bb1%X%VJ<&g?hiuCFO5~Wcu|!dC@>cAhb5U1v11+Kb4M?`<%~8Y4Chm!r!_*JEp83o>tKnGHs4GYCs+LTTJDA4wu-+6wBgUK+ZY-b1eo^l`qt%Ud5Li;KoPH&;m4(HTV2h9-WZ5G92jjD9UNWzqpTV?={u9=1H9fu&F+<!O%djy><%sd1Y=|TEI<C0|iR?gZ9yn!#yA}F$yYj6aXHP)a6OAEWvAGyp3!xB3l#<{XQ9MCn)-~$twrJyVbjgXRngI!BQnF)Ek=MuxXP;it(sSxawv305Zl>9Bg~`R44!zB%B%NNMBw8$V7iIcAJp6^KL%tkp4lQE!%5sDtT&OXoi1Bvyw)y<4SE@giQSI`!TC&DoA%M2E<J---_!Zv9-B)KGnwiz{JXm__7tVbfBT7@|_#d47!bD;t@qEyJzM|@FI1)va=1)~0&*ygCxP@7OlrNlZi~hfROEM2Jd5}5*R_}^q>=l_u-Zd%lA6TlIRP%#g(V0T_#O9NtSUr09h8#9fSCRFgY{>QoMD1r<j;+Y}IQK#8FPCb3%a~!J{&H{ZAb#=^;!doarD!%ff7el@5&0T0OT?lIX$Vy_^W+yJHz)$z8R6hcJ!s-X+mZIe8>J>#BU-jpOukjwM$pqk3ESA0^RsD<A0Q}l8z}z9>QhH{|LBZ6SM;C3+R=rqgQ78!Ow~pn6e{*mtxJi4YpYt`Gs`B`%p%@orX0twqAqskg<0Mft)auk)CHp^<-yxRCJLnz{@&7(SV;MQyp()xvu15-L0#Jen+5@|98%<E8Oia`y27OmdS6qC3P$w>5j`JF%*&ALCK?rtc9xTy{D*N)w0JtQ4Kl#oaP8~(zS6V;USFi=q0lYk;M#5C>Y=5kdS2u(oEn_c3&fF~893K0;#RKlvvwd^lf_!7Ji3rx*!g=+r^do9-8(9O0S4aa4ur*qnmpOULLKT~%&2K&NtVmrFJ2S7rA{-=3KF>8H0B5CgZU~J_pqoeH@-fH^6eCJ5-%3X-^&}cNfy?dU?-sRI*zAgeJ0gjpJ5OUlrN_@AG4yVj@4nskV~Q_k62K`6l*o>?0xr5;cm(C*k3jIz^`rHf#UL>4DTf5hmxQJ{lYNCc9Mjm1Z3Q>MX=mUHE;xra<AfOx&3*uwIB+Wh4NE=PhP_VZq>cf=z;UcB~v_`8h=8;vdn)5&v9l0801gwO~k_brm;}i-L8%%NfG<V=ioRp4re3W^W?aTpwFL=OttoNsSN!!U(_!}jRtEW^Oq#<6@Lm$JNaS`wkNJ>5K@+no94$$XS@?dyU&q3AYx49tVgFQSDlZ=MA`C&B?ga_=F}>f$j)T9&WHp-Jl94v+M#k@J~jPn^FK7lpGHzj#5ecRjj`SFuFta7y!qiC|J&cWbl(j39M8_@M`G~<Imb7Aaht#Io?ywm3T_bw9`ccI@wTh%Ht(&3y1U1hgW~uWujEgCdT*V`@!kYEu1<w6@h>*NNm96jOP}K`AY~{b?^}~($u<)0)ELq>LUk9~EKUQO@Ka6v4mpnpF_z|yd~$6Jd^Xgp<n0*fnI=#;=aUUG6vmF7&*wVGMxFABM=&Le=kFF3NeV)Gd-1+8+N>gmif@b@=f1fMh1<(-$j_yZe32JD_-F9H>QL{!WG3<lp>0FRgA+HQ=cn>w-dRH{hcL^zQ7sW1&-t)-`K&q7Jn-_b$z@l#OIY4YP|loaBCbf(9gXS{=`G&*Ck$)wDO87EjsJ+Hkc9P*GXnAhb2}CCgH%@S=2_SW!=oDTk#87T8aWiku6~X42#^6XkOx)o*{?9(#%YsNVYj7(2i(^{>U~H#`R-`*Xod?pI^ZUmS>}7Txi-b32@~qH)3-R2?2tS5D}wAvjvD{?AFw;u*=-X@A|5O@XIsziS-weI`q6wMJ>d(%Ew?RPx^14fZK!VBWZE16K>#ogvf<^n4exf_&HzXG=dJ*ba+vnu<_%z6Tiw54_YbM2ZB>?E*7uKy#BvM8G1xIXvL)CW)l#SyUvO5mi5n;cTuDNBaQX30(xA9zF&b$KV-?=Q4R!5?YvvHq;6l22vfx(}l_P%G{QRZNNmtOr%_g$DCR#B2Z^$6!u#@c6%wNJ*)Xw3=_a^|H!XElk_@g`$TLDI8l&|L?s(cqtSEw9`QixyyvL<XXMso6DY{P`x;ZLAh$}u&jM2>wEw~aS0cSJ4M5Eda__D+mpjAnxWipK<oc^4w#p;Nxs2l3IlLezv80Rr9x=IcRLFY$XfR}@b3;Rv#7FIg_&Ykk-tFAi};6N3}Poat<EqXa)()l+`&Z3yRc;x#@ZXqD)&`g2*ULHD>L^L)tZm#7?BGnQy1D|^oiT@8%L*&GqGm15M<JrKP@iBE#dYI&~(usoD@q6oB^HF7@IQ@vSwSa`il$Qw~<teeZAGOw8GM}|<Gq;07fyeMROF{Tps43(h9w0xb^_YkSpvRSQUvl0_!q%%Pbl`A&;nMOoveWKx8#BHtStz5QWSnex|dsmi{%|%mhD~Cm$zwxF#34Z%z>C%%$LZqsslwEP%e>5GgfB&6CQap-;(4vt@${h?rsufZ|R$^h%Gyn}w;<=EnC}o180Lr~!JQF)8TnmaLk?iLA@9jnf0Y;@AU5li6rJ1^cC<S2%jpVVQU7=zP5^^Xf@ULFQX%;)Q*_c^&O<`l<KI1RS|2scZ89HA`87oyG)Gv^9ML;T0DYf>DzNLYY8k923Y^D6!27*ng4#wroW4Hoq!Y*v}df|2yAR*F!L)fP+q>&OpAyK`f5?MY#_eakZ3@4PT5bqs@KH9*Z_9q0#w|6twT^#Rm|KoLYYn4dsKx5`buRd&|-<|NwZS-GX+t4-y3L%4t&;H5@`~SOlR?z+Bd;Imgfb>uq#H$JHzi%Hbsg<Q`;lOcr?~O<2kl%18raI?tgCx{uxx@PtYCb!W?%bk47pYeevG>AvvgtXAJt)L~Q|3DT)NFOW+n=x9<B-tSHCz2<7)Mc5aSvWo{D{p=C9$xL+3k!LCu90D*nVhJFv4Fa6{JdtFuAGjg(_QSh$3P1iAx01HR6y`AuvD29?PYd*n>(d5##hJ&T@oOt)}b@%M=6R1L#j$hco2_#N@MDEP51+h)4s*Dv(j>C_NUnZ#p7fSz$l%#K!E=uE<x&nh!0i7d@is`*?D86&kJ%cxS)wLZ7eth#RpX`(R$upXI-N3Uqt6nY&waMqN>o$?4+er>`JB&+E9oq(z5a6v+mepASlFKv&FCZDL?zg=~^c9orf3e86{8x!u4Z1g*_d2sLf0uc=){YZ{`dC2&7@E4`p^*031>s;zKu0u)BMUl1M=>@b$wg#%X{ug$DsFBryr9)_<_$*uQ{BI8p0UyA25_QPA9+(gD*_=3gMV4o6&kli1<;DuJ$H0|uxg@RdZ`~^PQ`9+RS^fQqzbxwWNuqd<;bNi$E#?mYhiZO=rb<xN%oLfG)`fgS48sqf#Y3Tt~3V8^ij;UGEhu1vojYP1@Lx~mHc~kg1W(MR~8XQKEY*LTDsd&dzVKJUtE#<-s4Vp@!VVb87LTPoyGssQjW)O}G$HMDBbEO-NNt!A5Yfx_eN+Ch7v;%`A9`e@z>+c#GBqS7}=%=M2l&V`1Piq-_c|R*j<@_{}*N+n3IZU7)rix*zjT(=5Xa_uilq8-*e(^2Y+r;hQ?8pOb0NGrmP)Xsh4n;_SMkuqB?I~K<*=)h>tC$%`bB*AnnFY|e!Pzx1Re}1xo^z8||C%YlMTg<>_XO)0iVNBo9vWxczL1>+a}wF=W7v8DaVbJ6W<t6sj3)Xv7-pE!O3ROfOA-N>34Z$p4~7Qrz#`D7gzLX~MLXj*>^q_Z^DBF4W2$ZJMXsA;@;K!v5SND?GKH9|j320>(ublpS1SJsr)5dmu)r@nZLO;M-I<0YtP&MptjZm^7L=r@L=3nyy3c-S8#8&OXs?*xx(V6IclIaMsqxf%_MRKE7;2x0@po0CUw$Wrc|Ij|6TCm`P;{oo#<~k4kYdZkZdeunRj!<mzZ|o?hZa@@-gE208szzJ<NT$~+!P?H9v!0Ui&kgY@~>wvy7K#26gB&~r@I`)t3<7mg|4NgMx-H{g8EQiMmGLk%cu9w|H9MxG&_s4?)}uHE%WI^m{i|&MPWga+KAR&e<tSEP*Iavbq)-6j{n<Q$QH=&q<lI(mQPbKWo~n(BBv*or06Y~CS(ms2SEId$-Cv(cbp#1A-ssBdeXHjb?$pcLyO28a+yPr)U&0|`^gCUi)asm1Q|pubH$z@H<v`R&51;&%dV)sZ73W(@(rW4BxvxRNxivB>aAlQ+`>3ELQUj_gTeUXVM!GV)yPv+o4L#zwK*ZSu3&h2>`_y{9ufS(TUzWi^~?02`@lJIeinbZ`S)D=qbBF6+YS)7{7^bN+?>^6>VKr-;hh_=sC#$Q?8#ahq;g65=S2C4yqu!+P4jcv;_vi#2*M_3dXE0s94Vp51|(ib$i4;7D_hlOrGxDmwC~l=@cUrqlCAsXs27=^#Rh(ga+B65Kb0?{iNx#oC}%(yRC<m)Y!HDf$ms#5AfDIzAMvvo2OkS_DGznWb8gv8*TH2U6E#l)4=&Uq)jqO=4sxJW=;9m5!4|192zv@MVIM34ks<!QW+u7&&f^Ax)n$rj$B7z_un~Kd-K^%Oh4`e@Bc><V>fg1r3r2zGqhxK0X$X&*29$a=w2o^~O{o;QOOcHt?lioHLrA8v%pzM$ZE{6G!916gOIi>i@UeH2ma_6%K!Ocr<F>A_Md_NL2Fn-~NoLzfDT$6<v8#a8tshX2Ajzn}6|*iRu_S@6d1R>^;wV}dVMaU)KHdbQfs+my2TY<=eM<pN&!~gFAenLA?Ugzt5my4AUddR9PVUjMMDW^w%+gst{?8E~Nn+wB)PKEY74syfXs*p1<+KpB&kJt4i}&z8Av?Pb^;xyJrq3J9A#Nea4EeKYOxSA1B+OjlPv2ElI&YG^>-NlB(N=~eDdh%m8ZD(n^XmOFhcJ`d3|J%N3bBJ|&T8b(lj`-Lg;C^!A>={T(7YV38m<v1{nrBl5#eBOAQ(1#VXBxC2Mk$+{DzZNUU}w7OMS4*>>)A1Z)}~kmE}ZGcgdlpTpQ*uAc7voq6aVQK!=q6wI_pxI#MWM!edgeA}eJim&O9GQMEnC1*&azbnk>YN#_-qc8POx!-v7Oybk5fsxOY%NZRV0MyF~J%s$;Ei^wS10EJU(jfzu+Q3vT<T$)MrrA|Yi(spG~gCn57#wqJK%-a<nNY8N7GfZa|<BD3YmAv_HOF+BBI44>pcxXpJ%H_SM84VuGe0tu2*S6VWse^8%CJVV<AbnA^`mf*KT-Pe9XXg5_?vKoJ7bt1rp^+dPE1io*ttxg&&Wv`?M<>KJUjfuAs<dT-(JQ;nZ-ME4Xtycj>`kejG;R+~w+|%aDb^d_?}7D}>E;T5)Oxq5w#^2-eZ2wif`;s#x8ZXKL_7*k0+HbvOMY7E{H__&c%vRLy;vXbjpSx#Gu|;a?YSN$*}|VVh2MU~%EC>1+m-e1fdDA`pAH0A-zAVul57^?sk}{mQBvo!dl(BaE5(Asvu&9(ck#i3vel$Qmh8SuT2Sj)AhO`Ijb0S^&^XglDzGu(Rz^NXgi|fEWu~_P<6{OHS3NfKgdNMD9%I8{UP0}=d`#2=&{`=c@-k0ls!IW)-xvk?&BIvW0oz!*%r^Ex!vWZx|Lo-})SOhkLU)vdUN2HBzC2u{V_Bh*sAFohIq68ZlnNvt)|ASs^zvcN;Df127g4b2&3nf!hy<88V5Uj624N8al?c^JL?aVxa72bOa~rVV;EDgI{9wyt(!s%pj}&Me-MrkW;Fp(M$LfsATls;bZ6}f*I8&A3H4>#E&cwlgd^|Rzh$65|AcibR4jIF_l&*vN(`e%F5bumJsCT|%?foc=<uBV}$=mG5FN<a7lE+yrgI-b<%dAb<m<kLySvV6G*?NUDxT$8j4s4(@WE?}uS;Uwt(Q(5AC|Y5Bb{@!>y?}+PP%*^1U~h+^#4;@_uUgbv5u;)m#4lh<@#yn7$!=K`1J);2b{lEVx+4q<j&MuB3=0;4Axx;^mu!4a2R`Iz+@W~v*SK})Q2qV4k6AX@w{PQF=+!0YxA>Qj>s)*&(tYItYR<V)fBM|ZgjLv591Uk{Q?yq2Ykf^$`5GvuQHQ<uGP~ks;_PL5g4HVjq6LL-9WFQ*)ZDh`5z2)`6EUxG8Ed#d)c(Z<3OU<Y^arpP{%?J_I!Gr#M9zakF!K>q>0YhSCZsv49u4=8s5&UB<|3_E=!`CX7*fYMp4K{jG@ceBBhJ+jst#Q!i13|D92Bi3n5vMvpF`@fil@oB{bWeZ+I?V1?JcC1Y?0P!5kF;XSW$Ia<BHgez_MzcE!(1|S+d@+#MXTkTMy`)s5^!#?;|XVIPxY~c-=n;uZJ%1Oi-0$4?X}|{ipN#>NVi<OUQ<C>7TIOb3!(sQak|P8Sgzncw@)<MUFmhtn?6%P3I|W+@S;*soag0P0!XtOT)9tQ8|hcDfvzETd>PCaUeMYS^@wFZF=$|4WN3?_jV%C4PEomA15!fH39$&o7hLJIL}7`w=!}qZ17puL>RO0Z4KrRMlZcHukOa6A*7bpZsXMxLp^oE+gctLs}izZO$$XSzd<gixfT8-UbN*^_V%LJnAgjZ4A~8)OGt(es$uk3;ZTI!`4jKN;_4Kyfc?h_-sWr$wPhYGu#h6FNUj`5O$xUsvXYnE31ykEdvUM38BQP|x}W>0Z1|KhBQ*^<1MfMQOJy=b2-_e`f@v4C!GSUtN2pqMQGFCo5S!gW%C`jAs_UxGVWOY60Y;t`SF??N1(1p2lw$Y+8#2x<BT&Lc%wObuB}QxS)RdrHFe*-E$f>l^HEYFt!zz{%{V)}+T<e%L1X8B(wG%)>W=L9K@@n(@y`S4<4rO|#)DpHXEo6SGcP1-F#(uydHAR$H;z9n~hhOEN&~mU#kZMVg2lS<{7<ION-FqzOQ;Im$n6tna!v)R!h#PnIQ#AnNh^?B68n&H}=>X>{GkEhzo(X{5{?D&)WNaiXj;u#V=G>7r1)KHCRKERYqAm2|HQUy!(03kf5w2*R+ViqLkdGQlZde<Ng%0|1ZHQG#LPC}Zi`A<+$ilhNQ(tNLsgAI`$<svv14sv;4*E@%%1;F)OeBF<|83qqRCL!Wm^rxUxzdu#d(pY|BpmFyrwjY(ipy=)1N5S4aTaaKXRTPnKTvk|7cbZJ0e&epeL*P$%K9*2$Gk$R@|mCZwaWVHtB1WR`v;Wu$0!HDjCQX=d`=!naozeawUAldPn=E?0?;bv!saFa9pUaJVL&m&y!tv#W(cx@pb0T?Yu#VJiT;j92E>{be9bJ7!i2mQ8^kPM*kQ3n+Ra>@2gw-}l=EQ^$gS9@ZsLJTmc$9=PoWFSoU!E>wRy={qq;FEAoeW~73>J})u~=7*HbqgVaWKID>*SnM)K|Y>^TF$+qeMj;hgQ}$M$hcF(LC)`Evyiz~z{|a7D~<Mofif1*YOa2JG*K-VN(TFv0@K?;hF|&4lGI-5S;>lng@BxvdlC)e!ow%ITcch2+bk8DSshp?l*)2#w|Ftub7&Sj})uMv78Urr;Y2T}K}bw#&ho1(;W3Nyca@^?ezu&4)S=CSCU)(Ty@tiSr9k!C-Qn#U$yJyl@kSIAf=q8S)oh`8n&v)B5zmY?CZnSAufm%PLr=w)&+LfRooUdK;=2{g-!wJrq<PsRK%E!=ktZM=1rAN_;N*FVE5auJhX#VJ`!8M5EiFw4~Y58Pmo&#OzUx6O=1A+$iGDgGP$5#;TW{>CC_GcM`)_f5JZdYZlfE$ftn*Iy*lYue_yBC8p28{lM_Ejof6oc5)!d0DaG+k7nI`Y?pXV(&j?a0fx50N2sZ@nnyv}IO3KJ2_tE#uzUd_%d%t6N%JiloUz{~9t4=Mpg}B}8w{=T(IJ{MU^N~HHws7D`B_vH3})XsjgGLe6@`jtdoI|7b6^ITqRt%gfFt&AaN4^Bh(+lidxp|p`2=d127Bcka63Cx2{xC?*W}v)E`AV|j9>xcPhdt7R4tpBW+I|s&w~~Pu8>0tK<mL85X;kGR;>+o)q}IK`L0pvtqHTsQJnsJ&C7F-p(GyJq;7zgMr_iOg@AD?CZdl;D3>`vEU@W8RRRMH!90b+F9+Vz{DcpJggcIislV&T$&vD#<NTT$v~hl;b4X;~5)zjLG1eFsOSj@+KeLW9Y55sL`JS0qu(+t`^)93F^ALx3VYVrubLBt_)NN_!dbi+`D>4D4QiY_ZaVrF96YiZ`cn?@aGtl$QbutSV6;2jch*y+o-Rn)uSFDhDoGRkfz}Oi4&yeE5`I!QyoS_Vsv;1iJx`ps%<`$q=5bjym<#X_2R2=h1qMg7T);G&}2IEOw2zUC%K#aO-zcAexc|yMcRA;cQ;>|81rvKuPuVz{zELLBw;>6+v@W**^f1=427-WH^Hmqa0FPi(=fyyBO+2BPklq06^o|<DM=PZb?cosYSgt#H2((hi|>}Dd)!3I}YipV?bJDO%0nWH(IY1v`~8{04}WEkPgdF};BgNB=}WMREg8Hh*G6^@D@TpQpNAgx%a12i3weVGrxcps+x@AL5G6qu-Dg4q8?^H+1$<MzQ_{UKJVH|{va1F1!>_;dOmO~*C|sz9~nwUk{0=m&hWqmd6={C;16tzjn?FxZ)&^w{C-Rl}3!o0M<f=R24i3>W+6h$^n1djAFO+bQILh+pdAZYH2x1RzKBnnTJPJWPMgAtI39SR9g)J-KEqab$jgUmW#1&OC43dlCo_^b385>8K$PK0^zYPw)gl1<q$m{;IW^vmBbW0Wjo*({9?%9}=P%(D8LZ!6;mYPHAvAoQeUWlLar|u`Nm0u*q+jn&Y3eA*0&Is%X|C;O*&Sch0yovTsNoeQfqTN6;FCAk;h|>U%(e(FyEJRWeDb)O$Q71bM~^fk>XkwCwIUn|adPFnf!D58Q<2w7IK*9ztF7fN6P5OTumTjOPaSeK_eHX#!x|b0)WEQEQ7pipn^oFzz)c2MU}B#0cxAdv2;brnXm}2}=`4)@dn2B;iaHq<Vve%j9Yn#s70}HO4F+yRcctm>E%@h}1!>7^V~BL&L#_4LX8?T{a~t4ehm3gB+%X?TvZyqm3mgukz$P=GL10G}uhoVVl=CX|*);!C}^u7$9!p_VR%btTL1DL1_Yl<a`r9=l6QOIiRdOZv7Pm<qbBHA8a=UwNVo%<j~DXIF0ct$5mkrp}*p2Otb_c75-RMRe9#&8n5sCI>r6JtOB#+Jiuqq!mc&(!4yud>OGUH#}h0ytZVSKcMHM_Z@@&O=9&F!QqCGUh@h+FNp0U!li3?<+A`0~km|umGa+eW3yL<(982?3;@P4-KbvHZh4OYfBStJ^%pykQOp?v{v3IZ<W8T`ig;C?4%EliIFneAs7-BkqlNcYaMwclFp(L5BhP%dK+K<dC<A5zEV$xU!m4n|aI*#Pc-B_V+4AsOkSK=8)yFVj0jGB?c9nf%U;oaxYr8x$Qln>uh?|=L4D~lHqLa(YUwyP1PZ>+K?slxL<uBcuylHWd7RumuNE6R#4#o}=u))djT<<-5Qtf-3JO;^_xofVWxOiChmZM8K#sMHh()fCmfZ5gGhrpWP$36h{zQ;bj46x;0l0ivH5DGOg8ud<l0=GUA5&`m!j-t+{{+E}LPn2p6Rj$EF|BqJJYyr%XO7Ta$4X!eYR+6E*j2fpEohLt08u-A;?Fik7IguHI{82D1brGSd8{k^-B4Mh+fnfVp$212p#IKq{+s80y01~wmZi1xkHl5<}3OMkS-wXnTPc2FJ`6WSBzmC?CW3JCUD-1T3|e<~N)k^kIX3!Gww!-?PZ3)fCnOw|a*;)P$fnziBkf35jVawPpS!>@c(F>aT=8(E?bn5`N+gj}2xk^l$laN{-CU(CT~++a#Q$9MsN;iw@FfD7_HR(PJbL_e|1=Sd=cjha(_;ZCnd*4_+7>OD2?^DkczEJ`oUa3>VjIqtFiUHQe&CwEmc+Z+h=H>MXzaEw2l%Iny=_(-JAOzfdQgd`v^(aEd)z#?DZ+=R}A=dV<7V1R?oz_z<+<bsh^1<n8m|CRf9D00s(Ju90z)$tQG8feF`0!9|gCKL^tlaGJ6M@y_DBxCAeG&Zyc8}Bw9&Mn&nQi5RI1a)!-;0o-rW&Xh&;c?xFHKnD}ZVn>)4XI)QiRQSR#>%3xC?|naI6B8ttbfzNk_5FsgOwVQg%BFevW<VkaFnfE`B4so&O`e^I)K}9Mz<synS7EV6zK}yKA<5xgp7fWMpCK4wzH0j!c~q$vRip$Kvqf@aaoNd5smp;DD`PYsQ~a@5<JOk?3EL)q-)+eVf3Oh^caPJA@@Y|Uqu7)3NfdW)qx>kKGa^chG62PIhc9*X|rJqcnTZwXdo2ARlkum4ZF8JYiS#-IW!|xYX#2A$2TJg_$CD`fx#<$AI3j^g{#Yg6lA5%4~2cmmJ8E&@mHW?+k7USN0wvS(zrd@a2<IKHwaR{_RW?y{EbK^2^9h)ohQR46R=??jro&U6gQFrtu+3GhX!0@whC`%)EQ_e;3(giH!)gf+HHQ_`)~v${zeG!qOr%WS@k#|)!`~Wp(cc7yzv37Cx32^S>_=JAV-6kmP-g8(gQM~wy!iL6}ET~jK{+C<O|l@D1}P!LYmGnl3=OO2sLfNo{dxEZCOdQkD7Un(VoQew&9WZd+QV;hoR%s=Q^Jo4dRGq6mIgG`Dk15^|z}id?-=4+E5+K@}i3Y<`E-r@H<1H5gIfXU($mZOQnhvr~M<bxS&T%EKaA~G6LGn$R6IG-cp(;G0%glW~7m67NzmFj=wkX!no=WJT+-`ka$2l@iL@!4bM;K!M7#WzDUiaTU3}gkYh#w&CiKZCG_(oj^{RN3b2{-v?XzOVP8ULZ?6N`xMReeT<eV2E)bs*?wqh!Ohf@h=}V;@*6a@NZ+VZixy+We>+A+clm77SEhg*pdm;%fJG%S!1al@z+|9|tR`45ThdvVN!!aKm;h*}3ZecYDeZ`3ShTA@c#6<G)jZ}+&*DUw4<z4Iz{hORkb1k=!<teL*=KHsq5x=~P6Wz^V{5@NKDe7Mv?DiYo#arDE+&m0LUk7nNL;`wQo#E_%zE?NK0C1IW+ZO&Z{+ai6x6YD0-L?ulVmFT?VfFnR&hB3%5!z$75FoyC7u#jBV|^o=PAiiA%g1hKzrLNj_3a$W?L=uH3I57EDi*_nlDGTXahUm&1|>OAo9FxT1B@o5uieDDCAvl5Y0~GY#SbUOGpA-`R5l)ix(uY-V4!PN3Zvd;bC2(g9NO>wJys*M-Lj)l1N#;j79z?xVLVclSBQlic^|JCzs5kyYyTwyZIR!u+BeyP{k8?cX>1Gy0oc$Mh{S{-4Y89Syy4rJ*dXf1UlCkyHpVFke{`VOO*G^*D~W!(VXC2^>%cFKMr0dBrkedh;*x4DxSbe7;$i2Dy7q<R!HSIjdr!dyhtjW8Yj%g<voio~Rled;7{Wq)G?70#fI<t2UvEQ0xS*pI5-^@W_n^w`q9Z<#{ausMbz;e(?Xw1wch+bk9&ggJ54vhOU^;FpVL7!jf&nKyl{$iT(#kJZKCpjW>S|auMX!)uk^*8BO}HVzV+HDS#)EWVZ{C`RMf1&|fX>**P4Q}Gzjj4l0a&{kp;!7*q3W20g?r7-<CJ3B(9E2D=}c8r;2Cz+GZB-osD#Qdp<v`RQrRv&x9TAI0vE~+<MRpCFNHnDw^mzLcrq(ixTa!Wl7jAxPE^a3+qXr#zFs7ao7<k{{gI4Ro~R;Uz>{u9q*MsQy2Ggi_-9Nw4Zawb(+f?dF|knOSPADIeNiGLy>%=}!B@D)YD}Y{K|-u3a=7Heo8Nkj*T}NaW^o`O1noI~b4G2{k-tdPMi|SvM0uD%ZQiz=AZ}6NKv^(brTk4j&<N9<f)1pC>y&-zi&4Fbq7|pU>rvg+4GP5&UjS4C`-OQdi)f(vLqu7s*)VpvJM1V1%CSWi%4b-OZ7~iebM1-K%8P%!Vkp9lIPY>vl8v6IU~60`1a=Fry|~kQgU$Hz{$MR>^t}ijLh)Z(esB^kt0)@Q&_`O}iGzCe!Dw))w}Bv9${aBG^cyc{D?$|X0B_Bz#{on8VH!Z-LF_vB;S77wy340DERAeg@+p{Yu+%QtUiN65ApkVc7?X;!qr7WD4=8%L1Ar!kU3L}k8z)`jJXIhNHYZVwnoE(TSKfu#l6dyEnPJoVxnQp?b&&!Bf!Bp~&Jew`rQj%)%DZlj!)|BpOt<i|o!eG5-8tt~=+bK7K}|C^|66G0*5GVm+=GS`4bCw)%bW6~DvKFrSaT^L%0;Pcc0YTd;#6uxgf}<@j-SJlEqr=Nra98gu1g(LGpV4rGo*NR9DWU@P7B7v4kDK`h4P-lutN=lg+FYzp^ov47uLnkbZ>=(EL7xlD=#&_KL2TE*&{%((86O4{OOnWVQ)!lc1=?pP&Gj|eTzP3Ixw;eMwbhxd<Rp1)pCSU9f=UG@}DMu*nl~D%V1FC5Bn?sX<)qV!3Rf)zF_3^ELQHe{&oy>P$&oH?R7n}NgAvbt9E0y730?b;SDy{^-Z%WnRp@T_rH|id8?_UaJccU(hez-@#DkbzqjF8HRi4QO(5l5seaI7elKseE0JPjkY<$^|L&{UtzKQ`Ntp9lm3ce~+}1Uou<EqFtjq(dfN!A8<4T#wzgw9nwjZv>)0P^KuWLMwr+~(DH6HJ8ym3Rf)!Y`_fy~mLD(%di2oy#B*z7j_*Dv*_D547%R!uQQtVf$-5_Jj;2dGQHRvby_Sq&@&)1Ju=U*vl%I?sMY=o>DjATUWZ2!Q!S44<=n=H=bgHZeh`g1N-rn%^G^9c*w$TjdkKvzj<M&{S&Zh%6R4Olx#v-p%4_I9jqY_ab0a*cg{%nmUp*OiAlz<)brL;GAYu`AN_To7T^w))pFn#_>AKtr7S#Q-Atp2#0s3{>FvTvJ%%S$ZY8tl5T!Z2{4<~pEF-J?qSYT`Cn~bzrsKo-}C6Ice*opq+jIdH0hKI7?LeAjegCeTmaq815vYAjf)o5lAo;3bN%8XVy6Kx!~hFfqFd*I3UBIkPSDm^kc}%}?87oB<(71Xkd29J_5Oc<vB&@_B8$(+p0{U3fxL*~^;@VB<uh7V&PXsLOzvv@fiw@8ZcaqEppQp}1#=#SJb-5Rk?G$MH^%79l3I~&H0L3{23X867%s<`fdw8@ifbr;<!|ZBgaVx!n|$p&D@FH1J<9x^gSS#1^?X=2+peY$dZ*CK97g`0kP0p*+TdOc=DnOK6FKfXYjK0d+JjGaERFJ!)f05;#7|&A<-)ZTtY@7JRSU<a)s)Xh&Q+MgoF(2E{S&zpN!TMC%0hwSP(cn7EUJ8lkH&v;y_OsOn4aV98_7dyB&Tnvkqo5Sx{(~!NN%l*%yz+r7IM7ULJrnH9!m25#u=F~$Hp%-k5g$Lr*A>?7$o_@9AA1_{}_@sQ54FKDg@R-j<%(i7V@^VkfVX{s}{0mE7V19t$%!Vxqlq`s(&0W_KzD4Cs`NSJ<>(Kdqo#nScqr4$c1O<Thd7WTT3JPCoe#8ibh7#rVnXk4(A#)OSd?2=%;bJcI^h*huAhVG{e40!6Zq~l7^X}B&Z_--JKcIhP5W~7h}k6rLqJik5n6dinlL}mwi)_<RRCVl#E^s#vs;EF`=^WR@fln$f4jaXC7PWrV=CBalH+GZP``E;k37xBHL&-J+TP0D;WTCOU7xfdOsWzSYs_?TKF4)@^YrUiwY?XI(kTbR4w;IneyLV)H6O~2=xe{a&qe>c9y#)+=J8ztz#f<r^Mpw45dJFkP0ZgV~La0LCjz^Xc^8k*q{s+)hbJ3MKY4}zeMi3B&iLy<oFQ)2{mt=#6=J!nI@J-AS+4u?iIi=;SeUQ@f86Q<B&p15J2n<?h16`3|SeS^;e)$=&fLyv)PvY4S{8q3D47=%3Xb#=2HL4l?fu5P6H4#s>mO_A)im`5U61WHkjm5EFe8=qhMADrIk@MTBdf$3@kB@hPXUz_q8{+oc!T_a}G;L4|7-0VjCJEd<)pv5QO}nws^1K3&b7PWB(+|y~l&yy$0p(YLxqKDerdv8LT@iVF*GVVBIk!;i)&xI?O|?yBf}zow-<qIncb?z)56)^$_d6tm0Byc?9lGX+50k4aDJH|3IlLHNKn6DKCS&r-u+5!rdd2>aH<61QPF8VckK3i-2(Bt$a{N*70L4>OZ-#6Z~?Mj=%#M<M1YM6=NH6wg}V&!=4ye#-iuc1a}c!8WdpLfg=Z8gBadEcz+}_O9Y8<yb&p2p(Nh;UgFVwu%BQS&b7T0#RVFdIdmmxqzjT@Koo|qPBxB{lkf8k30umi#~s}I4dbr?76ijs>K&2Yn8=#Q;6&Jn`-bzn+y^JhAsH!w3tP^;>=8OdXGR~Z<BH?js)ywJ_P?%bvak1R{nItsT6f?<O}3{;W8{6woy|G*V>MYwPPx=7{WLatdbDa*VCnE89`!~DK*<nN1du<b__a{HOy$?cUaA^4>2FSL_GsV;qQY9Vf)3#r^l0Rf4HOrNWpc_f;EFGIY9%OxQ=`fyD3^lqlHf#oYxs7=hEO%ZX_5=VBdyoS@v%IA&kPJveteXR<a#|fa2>6-U+758k$ue3fycSVhxIIM&<sJC_L?&!HOWC5W~ji9-2a=;o8dslaibOI4nGv??rZ-8zMh{vB;*>u)BZ=@f-9)=-{Yo56i%7pQSTwqII9?>0%;&gAQBV(96^&{&^YpssA4ZjBi^tfvAd|m^Y<Q%3Vq?*(B{vtcVsh(sEAN>;7W6TChH#5FJ|{rbmOADh9%m$oIxLoHS~nWgq4R4@t=HACoFHpA2-82JX^SR3KMcV3pDjD2Wp*ZgdhyQgU860EdL@wZ2W#}AIW|R;D$SV3a{@1X`A4A?s;m{HOgN1%vsURy2aYRSAp*u@~u7Z1hgaW@e7bYC+nPfdUC|a*On-gzoP*W%55VUQsnm%tC*iTxp_TKroVP;4ZUYNSjAKtOZd^Mk^M!LmWz{B;H*a!3So1Zh6UPz@M~KX(^4~Y28i2a(QU~e9+NoU&4fB<gx};`wSJ;#L^)t`K0UaTj7zkG^o;XeAwVVJLsU-y_1%F$00}Hr^jQYr5aFDuazSot4z{{;eN;owSvn9Ijxprcd9o<m6y;LaF#_8asE-hHE>t@1vc1><W?=i^3M7Msxv5-2K?L}M+Y&WdG~(-voM3Z-Mg)#dmf4qvS?3J9NbX1mZH)k0gb%bN3so2gGwyGhcf<*k^(`-I2V95c9o@xnjiY11*;KJLE1H>E+?hon=Dho`6N%lQfAv`NZDG4;!gV$-*8$`3JGODzsRr~=eu-W8gOr+WOX)TT5pa#@bXtRb7fm=wlggr^>972KB#%yG^34ioI0hJotv?MI|2uK$`N+kechVnH`TWpyUAVfjrs@dL69=Fvxc1f7%KV2bYT@`sMmsNu&6Wxnl&VqBoSMrHj8UZAL|R0sL=GH}fJt%x*}`PyfJK7U&HiIAwbgexhq$9lxo^T9qWU9C>N&8~o=Or(zvi5F=MPs+VX6qs4E+7kI^nkl^T;;bw%HxW&cPnpLse5yakNyfkl*x-Rld@kHk8b0vyyq>bPGL{e4qA)%DC{aKbZGR_kcBIJFA9K{zZJK=?37XbO;i1ipubRZV_+3L!ZB!Y{nk(T@*mNE)cQ@zT@e~RdL1yGc1BVmOR$i4AYDi`1sEmruP-Mv=d8Jvv5npkXJexbGwInC_S5UX(pC#ss5%qhNQudPFtn5{xA!;093m;GHJ}eY|+k7q7J6&?GUQc$3#A9EKjUjP43}Z{@LcQx#?G$`+F=h6u0j~;4k?w?R|&@6LMG+4&(sigamx#0OdqAxZ{bW7LETj$9K2TR}cUi4t5}kcH}IM;;RGNW!VFP#BE?wH;9)Hm-`i`-KkB2yZ%$IWAOU!nj5|$ujlbbBZoZNjd5R)>Ls$*M?t{+J0D24)A_9We6%h2m{lILHyjbxK(O2!jMY;#0O(4tTu*hgiGhVLAK?@%(w$L*HUIZJW@t<0ai{j!g~}ru*ux_uQY{;h;mHxHs(2ITRE@0$D?W}qnYrx9lzAAe71~F!pp^_wwq>CDW#RXYrIZ$_A;%1jyMh|)9ozP?(6M2x+X~SlJQn-1Nk_tr&jK>Rs3J_~nW~G08OO$bB_mfdL)W=gw&vF*$jQyr$QT$Ibf^}DUIx00hF9!N@xdINH=b^*uIGOfSwfO&hB+IG2o&mOBR*$$*A=WrgY#omnrxqf)z~+F{L<tf!2-|A@Mlcqet;-0UsU>;>$2hf8L`M;Q6Ty&y627e_rC3AasmA9nv(B@*dcz)?h|jrFC7QNo7fF{5zisV7U7Hhr`WZw;}BVAlh?7k#n1c*J_jFvV~XGy-X_)3uWPm%C;Ll{P`jA0&X4bwr6rE7!%{}FNe*)pHs_v{Uj`$QBl~!4LCR=vz&7p>@G!gNlFWYVB=ySB-$5n5Kfxs5aHxe_g1KR7+rf~qDUu_H9iQvzPIVU!Wyhwc^7wb1rGy4^Az}Q$r~Z8?p+o2H`*#Y8{HLT>5I?3```D<5CZE^!9V!qL`a{kaKFw^q^Wxh(>Gbh-^v#}PhSCQ`u)l4lZni!Q2!6xtTh3#?ylCHwaq9^0s4bgkrkoFdEoH1yir(S-``blbAZ^#xr3A@bm6JxolyDKd**dvn{ui98Ht8Tt63i6b!d}%P>DCwD>`)rTkP^8%Cn`{C;IQv-0fCf3EC%I}%(Z3qF6|wZ!Nu@t<z56`IgBNk+vgpwk#s_kq$o)XmtQ%eHaM~3I|XLJ7^g!aB&fSF!uibObo~#Tf8$9g%^drzftRNj$ZYu4H0_4|2H?;&_s5xJ*uc~^v1ur%y!uhTG(-!E(!!z~g^>w=ZiQk+vDnI6kHPyA{v_cTN*|Q8a8U($R{l0(dgxqNw9Hk>10JI%i9OR_qsCMp*N{#PN^Yh0o=WXKD2y8DH5n+mDp1;$Kxsf-0f#!QZLUsW7Qx8tFZ}&iYr(G3vfa~_*?a-Ji{*w2Fx!ybzkRCLm>#Rl?u^D(d|NeOHm-Z$Y%aPsUc$__I+=yh<so3Ue-1F)bBI;F8jet`(6S@L>kUf`HdRFo))Sc76MOY;i~Br~@1rx2Ea#AkXJX0i5-K+NHaZat=OFj+aw!gjII`Ek>6?5Zl^{o{#%@2H?+!~_@qI1Q(pId27<2m|miB>vu6^*tBK7M<8sB1(&hz_ak*2p;q~tM=v$bNK_rfA&6G`p$$5$x6?uKiS%hLedNb8b_>%DjeROsrd86F;RW(5Y<ZeFcbS&XV4h;3UVBH}|y{`w&ik>cnxE+WpV?wl`_E3m3bL>I<R<lIN>FZ|0n%xizrqz&j0^V9G66Ft)wQ8-!*kn(NDPmqG<rxVHX6Fzn9%{1hX&+p-Y5kh~V$a02ATsB~F0CP?G9_&J)WF?jbJ?NZ@t4iuHZOe>B&Jl|@qMl+k0I%0&Se?jF5L=FcEQFDOH>n=uAhI>t17T%T3N1C%(I9w_quRlpbXffFP5$4Bf~q7q6)5*GN%|exHz<cSL4#c1|B#cB?G5Q;SeVj`Aq14^E76iA{5pqv`3y-c8gRxaBQT>AeJbMiGNu^B7|Z+fM_*dkx<|Iaz@2q15Xk2%X(&4D`?*eqF&G9TjhGd{7%88e|932+x=GC0#~co`Z84$Pfa`!zTmFcUcPMIko6NyA{7PP+cWO_t<aNNl{n~JOA&Fy=g=f{c0h;*~H|e|Vj2PqD9beH`>>KWOQ0<e_(Wjrk=zd&5!AK?odCL)VNu8JBrATg0i`tOa9O%>XDQ(zW)Ev3c`Z*2@;n-3H2I_OTl)>JEk<OmI35ZiA`z-PVRGBc<nK0&{K6yS`=t9UAcq&J05zi44g&_&_z*>cU91G|GX$1%lcykc*1INu{;_@bPStpVfPgfFu=V=gzLP9v-^?rU&_Bd@+Sc%KWI|--A)-v{Z11|wz*Xc}<%{SD12bn<k^OptB>-x*3;Ms6qBl5>?A<lzIF>cV=j}aMF$IN+Wq#eR<Q5r}SaIPBqs%j`GK+ay0LAkB#Vy{b%&ZBCuNS1YlzcCrrxt}MACRRN<>z16@j+SPOMlxEJB)r@y_G?Z>rzA&(DtddHqhhF;OFSzPlamb&4#n|>o+9s{e$m9jUozSG6AW-R58HcA_4lP3n{W9QGO0HI@1EYp(-Pkh5uUGMACv?bA4y>l_9QV7ud|t9QlJ8X1F$Uz{=F$uBL+Ts8`yHLNE0{ipiWz4m;zI9OWB}w<zpo^|2YUIReo-0#t5sHbZ8kn^x{_qc0@eek(gk9wr6LQkrTBCK){Pq5aIhRPvdiz69}qq;>NaX+_K%3M0GjK`LHQ<DysGQ4M!U}sU!zNUf@QKo!|dozIgcJ`J{2dH+B?USx80PCW$ByP>^t@S1epDC7BFYD_J$%ZO)SU2Z-99`Pi9AV<ZvU%rU|n<_mvO*J8?`6RV<=ldeFu=&u`omO+%oW(0GSaY)=F(W-!{sAQm}NI3gRWxvkRXL9gG^bWp+UMy-l7BRYL>XDryu@PYhNKwzz1;fwYRQN5ZJI0bItTkcd$1U~!%@3N;)=NyNTW9P^Va6P>4yGag^UStDXjk&sPp7pK>8#fvO4Z=JJx>~5lGbJ?);*InYyliANdq(6DrrFZ33KUXzWwQ(_J-e>Jxfc;q&clkFGy<zUt8r0%xsm5_*A8}w!{QDywtv4FW9tF>+_odfy`h;hqyZTn{Q{H+H3l|6Jv9h4bu)CH9T-8nVi~k8>LMo#nMcafr+E6Wl#yqQw0$;!yV{!TCj;TxAcXJglN;2-=!5N#6&ABMT4Okgu)uU(ZK@=c_i9E@57aDFf1u@M7r^odNwUGTY<?m2LryT4Nq8OdLk&0L`foVfJ4Pt$!aK3aW;9Vt>^XJiY_D@n%<=E_Ca$Y3hjl5#tQAo5YMqf){7=XT3}CX{dJ4oL;h3$nTehTeB)jr29Zg>^YLq4RAqje0PsDR5zdFh->QsInFE4A(mU0<P(mKPCi~`k!p!@}l4vX?1@8r$dte}78scmkP~^;KzO=2nP>Gw%Ks?&Es>IDdwq$kxkH0h>{UonSg1s?<)$}Jfp-UI08*BWrO@m?;WI?xx8h3m{$`^YDB-}xv8>bqTVdl%dC+-3GHsqOT10c`bX1{~KB8|M^qjSn;fsH_|@Qy>M@`oq>m9PmTRKLMzbDo@ldkguAh-D1b^#AJPRQlSYzS{=r6kY5-r`l-`)%>mPPi{_*m#0cm?1IP6OQ$z*+gR_<Y2~i_XLlwAo>!Z*t4h!mIT*Q`d-Zm?+c(^wUQYY5&FMu7w%(sXWDK~g^A;UmwM9M9tjiY7*1qa2cZ4!)m!6)Od!g2DG_74L+jVOnK8_l23>+45@o&F)F69OJ#WT$G#>M?mUK}NedigBoozdRTkPFtMDpoy}C<NRYkR9XzUl19K@3)qsYh;`2#TE;T5=gvjOCBoFV`M50D9MG`u4o$?)tHCU7|G-7sggv6sA9T9JqhJ)#jOTN+7^+CaH`(MzVH|gOxU@O6ID0WBviYR{FK_#>j9D)ju^zg3kag(xg;Mn>Ej<T0r|6P-*0|-p*!o@xIfBbZ)uor*{;p&?!cbEm>HXR57PIL&F;X80E-xTqq^yUd(1v2ilXu0zYzT*!PUou--TJ?%y8F6M8>%43yx9eMKy8S^AK#bN<wluFE~<!_EXpb$!p-&?ubNzv6%dhy2p8;eJwIomI)%q0w!`e_Hr4@?NJqT9FNE$53BY0$a@6jV?<#w@|{srC7wsy2Szj`T6cW@hlT|Nvw-Ss#lP1)3yiMmN1v>a1<`zV#pPepq}*{qr}k2@;Gw|8;B?o8x6|mhy3N%DF8k)jk1ONPYL8|k{feA)w*1)4vBn)S;V(N`(ytl_2{UI8%jTL?V~xUee}Dp}oK)+TZXh0&hOrYbFQ9^0Zo%d##Ri2Z79hROsM{NG*|e6ah+~YPbQ~IFXVQrwh@`n)lM6EB(y22w0t{!8+l^zz609eM56epV4t(~Q?mA}rZ6dIzQ&@VG5n|On{oM!J{6F~iP%wzgKRwCi-#yOdUow~1(D{RS^-((i^j38Kk<P-c85!I+N9TV=$Iw4c=Px>jQ)}Q@G4AFMeYK`z5HuJ|&j}pj({qdr6B!wXH6sJ!fOn(wAIVGfA|eL=A_|5RKdaG}OGFF;vwm1EhCj2K%xo{sXK6UA3};Sv@xB!-pUL9R>hG9p`W!=5s>L5TJel^$VvrAP4XYN#5ED=hhi>#0=|KW3vPCX>qRe4nxxZ&4$m)B+^rt~sD9?)z68+mZ)j$>lz+hv!;U4b<^!F5^TZokrLtnAvz(B0O0)!7cfYR6AYAGRJk^NcU8(Eg#*l-4((p3lx1D~5&3t_!}t@(4I$MjS1pE!vqgXj95af(OMhWh_q{Jtg|?!)PZ!J_AE!5!>8RMXg7q^?^yUYk;$WUTZ0xW6%;D+2q&;g<6%Tx!7J<&WH&F3!;=f2=HexFMx8+Xn|)nf*x|%cOKrh{OYW%Peu&`;uiI?nJ5_PM;vP9jSgHXs&6qcne_<Y-Hp+3-P`a<y`WMCoyZ`F}5H&Bo2{(+F|%gKwnrlY?VLv`f(IG+x$YlRhmV)#w8xF18rK^ULo8Epu!7hjjzp5eXB=}2@nmRh(S>k3C&S7j0gW|ve}jC3Q4#^&)_K}edX_yc}skebHl+OqxkygA(k23$wu*&|5ZXQukfX+<f{8ENOkD0{O9>>*;PK>NHG^kM&(d_PUbdv@w*&~${%b`40$Be>HSxRi4Wb;Tfd)fYh?%iqqnIVbkKuZss=fTy;_$HPT(TQujd@K6%?o^4ya{iBc9a-7z=v$X(7Yl2E<w)CUH3mc?hB}D9yK00tX9QHsMz}Vowi}|G3WiJH+ikd~O#)fXTTn3?TZaqpOfRfQ|a0r6mq5yzfe)Mp~Hz+Rm^xn`G2>_=XOS1<z;jH%P@0!nVXsc6%eo>Q{Lf@t`7^jsD7#Fx<vVl`{>@$t~0t{hI@M|K5A$pLkYcarYJyi^4iJ=Mr@>yg&X4`)ul-(prp-SmrPDPwZaHKLN^Ze;Y6JPxP<npJ>ncC!&R4L-+>xC$4-Acl<cTUwrBR_7QQ9$bCJ4WuzS_E1D(US2rw5P4v-*MRKiwjL=q8gztuXw6dtNgsxkdZ`H8qXJfkHb6t&rj9%?2WFm<R`7x~SxIiD<lw)Zo!J`#KLA}U==<x{>+YWH8iZkI`Fm3ZM*vifK@W<~q{y0}#AK?GTBo$3gy=hX*N;ASTRaW&NcC&f{lB#^-!bCP>@C|j(vb$e~AY%pJU@@&yiQ($*>jJ8yh9GJ>HUyb$;qYWR2Z=d7qY{xf+^7v5DIJs7W^&ymA~QinNNuJ%Xskye`Cygr>QUb`)U^uk^|v323U>QVI$(YKBXMMy8$Y}K)Ejlx3@QiAmM0)USt?J!@d>mxe!)nw=los$1g549m!CiqwC>3#;2%7JP{!}c_}O4U3Q(p;Z-01j`yD-E{RALUfB6Xn_uJoOk&;^WVXTUj>MyJ-l(HeOE>hZ<^LwmQrm9XE9;s9M$Lf?bTh4ndReAyk|9@7h{4ZV{Sum{NK7V0Yk<M@sI{<ZTkb(fWWst&hC@9INLD4N9LfiXfvr$x<BW^O)X;f<?b3L78AJH{{Cr?d#A&q*hdn!~a)8ft$4GeP;vq}%*v8;-f4nz<JYT6;FLG4iKmDj8ei#e(EL@Cso4|Ai=SW^HCm=-O>_18vLej&qxp~2ovaXpH|e(Fc?@P8$*pmy)lFVG(K<T2_=8We5$99=x->)(){dWcC#%0?50`8K+K&=g(p$5K<!pN`a2ZqNq{h3kS^FbK_=a~nDspWVQBOho&hG;*3O$b&`Lz?zWw0Y^ZSI*71<T0K0@=c++*uY=4*Z<7#>1Mo@n<KLf;Q2o;p?p2<e+0ON^Eu#{JO8uv$sagHQ>z}cqmniHcqX!JdshMcsVEqojl|p}xwfg+0k?htQ6~`+b$%yO(I0wm2aVxz#dMMO$^F{sH=1=6v9RE<cykl*T<G%R$3G@FGDJ~l_6Oa)2D7%n1_+9AlN<SLRN!XcFV`y)$xngfcJ3O?LDn*5ktdSseI2;$AOwZ{IY#xXWTC4X~#j9JThDNqC5N;yHrohS{s#v$IFE;TD==s3ek2i2<IdGZu=EkT@P#`^N{0Ehn{?>StCk?-bMl4-~zvI#po8YMoOZ%eg<L^v3eL6KWuG#am<KK82q~NJCr!Qm&p2<Jv62n<SRy+Ko)e#8$rkQn;@@5!3E#(7a1O{E0;rV;R^TV;98PCpFT)^99q|9mr0rqz0dQU5=IhF|z48>IlAgn|P|0VM`qIb_PVn|9i(b47hgY}5>M|Kar?m5)+qvk_@Auoz4y7V=MhS=?gd}d_uN7)Xl40=rG=S7O~>L%Wu7}b&D9Qvi~&HR7ty~(d_+j<`~syXJIYt2>cwbtHe-+S)6ukiDW3+#v&BGEW)8i*DxBt!#*LWqRZNMb|`sbpiMfKcQYD-i@FBti!yss;_xK#36IKY$n<oWhnx1Q87ybQr(i?;EpN#oqgzd(J)g+2`uK{q|nPTyu>%<~P3aeZQiAaCZW2L953E@^@Y66M;%JYdElxRj$!b((*6xc7%gr2j45-P<G5q&OW^6&$uJ}f*aRI#t^iTwwP0*GyH(v1G874tn(M;PVP`*^1Vq|l$U)+FW6dMjrKktFJJ4C;Sr+$JI9QQ&&mT}4_zhei?AgESV4=xRMLd)tGc81Y;GMe^?MFN%Ywp6Uh#X|Ac*sh^7~ECIhOq_rrCZ7tJBhOuB^HgmQFI9d*yPN8P079@A1an?>2-}_9}72fcQfefK;x%8M%S@?a+Y1j(-4d=g_daN)E??-uBpot*N>VJWN?5F&7%MtYfK6RRt1wR`jSV;}Lt|dBf29B>D_!b)lu~X9=op!`=bS?E?F$qClEn8JmoWi=eFR#jT-roNdBn<_N+<<Es^mwu$x{zSy<3$TRuaK?x0nERf*6Ggk|c7v+j&MOG<^HK>N8Fr{icGfO5@*Z>;qGyE^^sz*-wPIu>?b65cH;x0*hC$^7Jzgb}^v+Y+ym?H-dv^{E=BEcKI8CMyzJev}pmjvCm)#42;FSCCv5jy%q@~hFsB$<i3r?)42(nw}YiYQf1IbcY72Khl}%EN0Y!(xdO_*zHnlj&iXBhX8ghGf;}Q+A_tBhwu}dbgN+%jmL}<tM4+!^sL~?&Zc+jJ`F}y<@{%5oB_SjOpC6B_>INN?ki}&dH=r)+`rJGxZG1!JBHLhBdhz4KwHFnZ^+lrnH=rRQ)KWeEv#(Qx@{<BbsW7XU!>hZha~3hc5c+z&HOn+6a~DGaI)Kn2Mh*3)!Dq=!!g5Y2ij{rYq8BvqP2xL#$rN2+sHPgYk6X*6KR$mNK_W{b<A;(<T}e|H6wqS1;}^PDb32Xza$_JAy^4?U8ZyAR>`wq9WK5wGusNopdacmgRkI8=%$Bm(^af)`5i-1;^%u;cu9p1Stc{T3YfgC3rD@Nl`>+NJr$EoXB7N00Yb>_8hu7AM6%;$eZKMLvhG!ar>!J7cip^d_#ciH1;lCAA6G;?#A{DuYkcSE-%8$X}_vV(eGq~tR7B{o#mR`fdJWFTox&<rO~3AZb5RrSx;9+j0#?ymD6%v4lR6s_ov_UB|_@U+&}oO^g%9!b(Z(Q1^gN|>eJO|bTyKt2&?Th`%^{B+7)OPdOC@UE`u|$?Q-gyNj<jznEft|3LUrsMve6AgI&InC_S<S4;pM}#o}G9#85fd4XwB}-ttlG{>AryOPGq0jr3}q`iHYPQ>S|^z^H<L9#!($oMx3}!{MZ%=Ro(d<!~~Lyy6fx7(X>VmxEVF&ZenGj&pQ0sb3iotoxPsJxJ2&V%%68$8R1kx~IbPld+;TpZYFV!R4<WF0wh1-HI6MEzg3t;f-qieo>&nj>M}%GX)Bo3~{5inW6;#{J#6uMd<;s8CD-&$C6~@;(o@m0_qFt`vC-D)Vl7Slo?QucttaMlV2wJR?hFl5I=IOzd8|XNL+?$6CITn^2oEMOtcuS2Z5CCF=SPmI<5pXiMH*}6dlFR;)s{6JT)Wf9h?o4R8G<$Lyz15bSH^u0e2WAuNYAZ$yK#vgfop_B&gZJ`c<c0_;IR<^(wEpBuUzMG@U@1pdfD=3utkYUNe1mK#TYhZEWr<P|y5USr++oV8H(qZVSZ&fIG^NmknS(cp)LnNUTR?<M9_Oae*se1~uL@c(I{WwzK6pG^iEu3dJqhRBAiG4nSmyzsvH6i`)kXiD0E*=AipMQ`x9KQeqK4p*f>9Aez*3$$i&U;KrPiRf2{pgfI6qqeT^zB?leDc0d`UlWIwTUZ;OVX(*oDJvX?(9s!a|Wd=3~ezKhU8tF=zUynqwXVx9E{Fm=Mfi-0ca2LfA-9}$-B|msWF$9T^NP9)ymeu6?S+=F0y~s#=fb?DYUp3OEG#%>ApJC)lp0rLL`$YuCZ6O(-gH*n&oiq0UBj%UFl#GAusC2!Pn}Lj+X}-)oh}5IG<`D=MgaWd?gFss>UzapWs;cPr(NA7dGyJ%!iWjPL<mh8PdV*@t5`rR)uP14;Le)lE%{gw1s_8Nx>9|fbk^xMD=@C%Cuz~Vn7;Qe6PMK+LQ5hB%&b6NFWsFLTgCOYh+{+V~Q)~MM^?yzEoWh*iY7tVcopczzHu;N<xf9CJ`j^=pto<k_XW(b^mp2vg(YirRGjIB*v?d*k)ZU7h;@{Lw;;7>g?E1RVoOSfQ9{;QFqDoU1W6<_fdP99ZKjqG&a1+&Vtv=s9yO-=J`fAT9MIM`<Ws~*YAC<Md*LJ_$W1sQPII()hK|Tbm>m_45&<0n6mvmH6pVbS#g?M;?Y+kcA5J@ED2t8tUw6f;u*0dpjrEOTSpgc9b+QYixOl-A+hO|Q&wQ+XS&;`QOlDL1+#K-VUn;J2tr8*$dSp&<oooHG#;2aD<iFkm`k*Tt({*Rg=8c-~t0GufE`ViI>lAzg@ou_&4$~ikh4o;N@7VuPK^~mlB9z=Ib?a;&%vpN^41La`=!C5@cCY+SUT3B$j6qS>^SAn^WjMn9|zQs-YADd9xKTDA18gFe+$TMdRaYnZ`wntP$2U(ooNz;5nX`?>+=-^+txAh#&4R#q&W$xV287E3AM|u`A>*be?RS;Cf>lwz;_FE%|-LkaMRSRnR?eGE;+jB_fOHDma{M@F{?ge~v)SRMXA3hE#`)6Qqu{OvP7&`W^TDDPnD<WUwEJ!`_6l^N@a*c3Sm9AJxU(Iv&3{bD%Qk}Vj!dT9?`U_QEVcZS3Cd9m!M9L-iDcmrjrCw=%LVvkiI^?`We_7BHFJysN15Eg0s1r9xft#@n(Q~R0Sx~_Rj%_$B$O3^RHXj>bo#muiknCM$wbeP$38OmDGB557Pp_+29o`t}O~BJn{%^_fU$#c@m0pbu>Ow;UA}+nOg0+LCVN1i57<Sq6{c;Dkt=0F+Ky9FZJM}x#yx)<+U2j;hk1NFD|DS~d{`;D<gQ4Z}jcHr?dS~9rH|K2EUzxDBV8-g}9c2|Qc|64M%gO8O<R!7g`SJJaq9Dcrt<upzYb`ygZco8nW15+kc)Ac2W#0y^9`kt$)_GB%&AUlIyz|exJ&}JE$tz7Jwut#y&9hbFk5;|4S(7*rTA_XYh?YrkBs8;HL(!>G$*x!1-6@-wQ`COseRHfBTF#*5SNnJ-&9MKdQ#&rZyf2^HU%(m}|CUp`4Bqx&9@%-xC<my#b8SO1fXWLUT3#rzVD~)LzksJux88~jG`*+uQ}3$VW~!oW)^!M7nqqDiVqKFok2o&BCZrZ<7>b}mfl5Fb#d<R%oLP^pk-4-9$xFj+4yMDv42w!E=<mbS+pRO@=NsH8Ym~Vl+jmMVT{haz8WWt7dc3lXfNx521g^7T_m1fsfY<(i-<o?cCmuBCGvW$BTS$%mLRUtrW|Q${U9V^KgXEX+far6J3qFukFy|iRGwy*mz`&AwP(gy?9<X;$VWX;4K59>m^aGZoBsAAWJBR>-OI(4EGf9iVJonfJzwLwBKgUBD$V2D_01ed#Q_i<DD#G5h(T#GHUdBe~tAN$q4YOs~rFQ*HqH4wISv9@Sa0|^m-c>?E`3iR|Mx|z&<B}RI_u1gT_G$i~yI-5SukjT$@>HnscUWUs{jD|Da^JQwf6J?imB$+LVB2Y}GN^N|wB9(FBdviP*>S;&^q@<GS2m1oayVx{9qT6bqtwF;O&gBUJ(gd(P?BkSRAHUfFVH_A)j8N(WS56eIqXrKSgnoL+gKGrhK1M$P;4Z;?yxRHjkL85eP_0a-2PzsP9y`D9Vn`LsFVzj*(FvwfUvkLih&VU8jQTLcpLd)U5ha#rKNZ=g*Le-QT0~E1t;y3L=z{sPgVwrRa`4n#F`2uOlG}O&{TK%+Ok#lr8aXYCMN+#ybblb)1FSnBorqa$!h+$w`M{5d{(O}p=}@i9@VLa*B=3W%_)$mM&@|8vSHi?`LpmI!yutJRF1F%Wgf;nWnOGMRNyc#cB)^FQ-hgEbaopM9ig}>(t0&FkOF1+f}jgb6T0ps)<jy>=#5=cb0DG*y6751d2zm&?lAM3j&nzLH|Pi{27!w^KvxK{%<C=IJeJLPBm&Xj?fAxs4Z|J1(}~=eUgnj5vg8MlDqs*%B0S6ia7qJP?<Ey&%Kg_y0uRaTE%CIWK^qfcW05!9i<rGbtpTwMB?^4dS93g0%fXR{kJ?bMLq);s6h(4P>w(l3o|QybyTA92`O&kfe{*xY`abi1t9sRpKh|`=f!1#YY=}<eyD8mY*ab1gxBR}H<@cjkkT;`pB5|70D~P3MKY5k=F|jhQAoD7ZZ<p&6h!o&gRq}^q!B!Ple1=?tWSm%yUWL9R04YERlvtLU+3TNx99h<{laLcD^r*`JSY-3*Pb^$sH|5`p>r;fTU9V5k8CfN&s1g;4B(eS+FXNXgQIU;E^Ig=Zd9Q`f`PAnkqDC1)@CJ*4rZ)s0FDp}Bhj0MZ!=YwFE$vOmS9W|nRi#V{2B`1=W#{r57`}w9r+UGOk{pTe9lW4m^uRI=vGl-Zi>fT@#vUwQVEOya4-yDoTDN*xEMSB4O5JKR^9{RFw=&MqqI4BaO=$`QlwoYSIc~MxZ_Z4^d=$Taa(33@6$n_;IYh;RR%BUjzO`_+H_V;S?83%Mmias9>JrBB)D5;`6CpD109@!|H(xHt%;?!%o?8O*j)_Hlr)t#F<@rgA=lF3gp8w64YBSs;d1)!b&_%NfZ6E0zBkMcsH^<=+Wrk!7R~Lt)Br}{;>PqgmmPu$sqawEL*5(8{mXJ(q0X(|9aAG@O_CT9ED18M)SF{#~O?XITtntNr;Ml?u1IcYsh^tNbgKGqTs7D07i|&LQ*k(zosJwf7KYlv?gzZZMxpO7KkLu^^**gms$(cuPG&rwyueYpQ$Gb?FH|9$`8})zhxu7swaXm+k(*)YH7}zbvzT>FG7ca%TfTmir7ZV6V@5M}EYq=8P5~Ui0l}pSXilIAl>m1a|SB&-6!6Rm(qq;Z2M1wT%Yww(OXx`5wU6F=SZ8bo%dz;B|T1_hWjpvRqQQEt+eQFd|qdd41@S<EaHW%;0F&J1?65e5B4JnP-%ENwjVeXSET%&qJm8q0IVjA~#w;UR_9L{pMM9ar?Gjv;;*e=Z;8#8<KHG5a+zVv%EMIjb73~@UK@b-EDzwmpE0yi+3ixx8j$4#lYs<VS4IcOxa98NZmk?thP_5$-XZXK@(zb`0_n@NMyf9y2Q|H9}1i`;$(Q%8J_d$#+69AGKQ0`-cNj}X!1NMmpQ_)79@uyakju<B%-PFzWu)I0Tt#TYgx#PUkmu{3sA#L0UG*r0+dety@{KhNg7HS|A!Fjw~Si93<jP{xwEV5PC$+p5tMP|*trQC_o_5L(IZ-~oi9+yjoY6%CUmH7^5b+Q`N#AfjhinF%g-)fAamKa0zDHjXSwT0ahX8^sN;-27zjb+vrAxbvyfU2lHb8%u0*k+G$8<F@B*Y^?LvdP9wwY4Mg;M6e!BC5Lb#)Ql~RB3|RI-dx+RDN!rK(l!DQdDUt>!%6vQSahe+%asQlbG2@HZ@XE>*706t#uk1YGd7vo|Lu35o<MlMczOx|DC>}h)3e;?jX~$miS`|PF>@n_9%2xZUQDyh!kcXa=GtO;qSZMKlBO9ND}h-qT)|gKej<!oo2rHc#8geodCHElx{=LH=65zvD^NkwC2uiLg*!ECZ<bh5il7)TTGXvGP(Sch9lP375rN3Wa^CB)d{8aFQL`V_!>%kn0wK*;pXQrTMEDPFO8&eXPM-JSQ%P-5pe&(wbEWU&w_cQ01iSSzP|loBQH{M!lu~T=-bm0@eFGq?0fo}MmL0U^N8YLlhG*-%uXLdrF)3@td{@5LwSVDf5wj^X3-#}k@@`eLCbg=XVIy0KX_4=$fz6_{Yt%cZM`~IbX5NV0E6x<2Ue`@LK$9Au+Rv=o?-2VM<u!xZk=y|@&$8PFuq5eit($Pl1P3!`L#3NHO<rce5M%heA7mXwtoiWui+*B{y`+Retb$965{927Kb)!<R}c$htck5T*!#LBiYu08u_n8zPu#jO);w3jh&SsOZFRLxN^_y*uvi(>WfkLWP0X$fKmKdt|N46~Wox*6wX>9s3t~;#Dww^ynX<)kDeOc+3s!Ac%EmgIP1~rR$e6gH?9sb-O59NQv)<FzLaooU+FH1puc=N@i)_c5vaQS9Y;DgNmJ@TPfgesbF>O}1A9q&%)(3%q?M0Ef3IBR))Z&UM;g$LUgJybR{Q#3uQq9w{$SFyc`?(&H&B`>E5aigfEFnmHNYFmb%D9AlP2Hbs6SKbx_DWD6T{q$@aMoCbz^W432$=$dh;#{g9G7x61*@9ufHN;w?tY2l>MO7zyex6+z6pujpP9rNUO`@}+tFX0?G96qE<ej@e39-SfhZjgM56?5$&TD!XZO<sTE8bB*RR~?jaFXKufrFRwF?K7+Tw8FxHfUcvEO3{>O$3}xo;vH(&!u_2xI^uzTL@25?-<8(<$&BS9ebJ8f8yMeWLulI;u~b6_;AtaWAo&PQV64YV&H0wUwuT!R_i(B0%k}X&thW(Ir4&tx+U#`sg9j(Knh<hdx(bqRyJx`UuSwFV5gU>;95&PJZ`?aNC!xbwAYcj#VV>=lvkvtw-{@9$kM|a%dDp_9e}Gbcb?KVy(Zp$1BAW!Bh8cO#)W=hTntO3jRG3nKI}nc5RY?;H7Xhv5k^;l9DuVDjf<vDHB7Eg3bdD`@r5%A_48e8>DT2j~k%jNtRRn&VgE*@J~TOs)Q;e>jww=+AkRqu8-;4fC>%bwk3hPV4p;|6z{d~8OIC?H*C8j^hkpzqSrW(Ad?Ow`^&_&ZBuw)c`CYlqtB<o#Q0-A3KK(pooX`E-5WPdR%$~fs^Jzti5mjyW)^Jh0g9{Tu-}pH&dKy127XGamcvAL#&qvh6M5t(K9m!<SJ{<}Q`Wg99vH~+&(!!R2mId2`YD|dw8xUJgWUy3SLhEhNrjn|@5$*|ow(bKAQ8*99i#VmKNN`my_U1Dq7tSy<Rv8GS}j}B(HCHZr>fYA{E_(*6s?MFy6Ck5`Ail2rKsb13ES6XUf!h@j6fFzRk8hfA)9gr({688=^_wK;*D0t9%urrLiX+jh3t<npZYi6MMLTUT=A9Zx%J|h^;i9ESfkk{DyVW2_3pNA<ed~FCxfb)tr-k0B_jp+*r+76BIGz)-rkYX+|m`^z%k`z3Cmy`FT|wiDhZ$`o$R}IDJCVbX)tVlA{l)lEG;_wnWWSlz8U45NfLfvftx+vhI81m147!C=1x4DJGv7iU}?ma!Fj6txD)43U0GIM1Fluq6rKyXu9{6+N@Ci_(Aa_!*qczz63YY@8U*}<Gr}u5)kd+kr9?ycz^;e()w=j6Er6D(e!(@OyO*pcvKf;{dW8cXoO%#yf0Ru_j1Qq&KCla;?(+j?&7({!Oe4V5*MJW_XkrGgP@s8-YFU7Zeow2kisKU|ih5||>^zj$*V-!IUOonwanCv>8QR@1zc*E55z&cI%oiSVSZHJ*NAz)gQrI{zgpI57X(x7xQz971A6#iQ-f^+0x=yK~)TOZ4lLm$xoS}AOf39u3ld>)`AAr2{ri*<`-gr;ms!_)|9ngL5vAC>PC3PHKd?{Br_PE%sUY9#<KdI~j8F6$+Darh;cZrkF%1mF4lNg*))E|-RDSh1?<7B)MC%YOa(=1L>(zqO1#7&Eni8^2-I3BS0nOFEcPD1})fcWYj9;LF2Wme+EVzo7K<`_OGV4CkLMU{BPq6JJp1x#uokC1ov3E&K$NygH_!IOhy-Mh7qKl(n<|Ic6RY$}%m{Ft|yP=QR{$}wLd1#-LdIVE`m$HZ%zR@s|BWQg;bWrkOXv;NE+axu9AO(65d{E{?2vGty{W1C-zQD7CUL9{X<M+DoJQ!LmNo90(H&M)psd=Qh{sy(1Rx3g+PiDk9a;FqO_?l#KwBWHDgb|C`UmAM0ggaPHH1Gy<rrB{z>{oq&hZ^T&LW7qX_pW&w6bzxI>_3M~g_bs~k{UDf2cv;McCX@hPBBRuGe$X=B?hMt7t@pwB{Rzs7xTRrxb`&EPDAq$6u7e<^C^dbjyzxOU@qW!Fi-74gena185b~=E1;$Z{LD~}KiI&_}3ClVEr4aU8t=p<#(1Sx#-J?VtM3K!F9_mM=qbE{lI;u4X8IcnGugwcG4nX78O)?n*Uv<ebAOHAs<;WL<&URv3G4q%&-7$*9h1J_tzMe$pJyMe_teFS!B2Vq$YS`V09f>kHHnh80|99%QxvJelsgtr+r?{pVM@u`$GK`X}N)>kiPE-$tgBAaLV7_%=bGB_lJQ?9#CU9Jb8J^~NG1Ql$q_kl;yuq&F@F#w64rfp<Z!xf`gNi(?B_m}vuJOjWrZTQ~k$abS8rtu=|NSf3zML^kue%r-+caLVO|5_)$kvo{VyqcxM%vY|7_(TPeC3}u(W(yAU$ZvKV4RB9EsN<|t9Z2_un|QRbYbE)kRoWM!zlY(VRO1LV^$=qWRS0j=8K7rk|@|v6ooSGuGT<VM$h$As#wIW>UpU8TKUfCs}1O@PGW~xXjM5QZ=Y<|ux90z#8t3aXC(>)W6|D^IdYas5&J~6!Xmj<9=c9Ez`U~3{PCOMNB>)2&64P=LvNOy#+O5HVu_R$eN*;Pt;+7pDM^n_Z=ieFv5#FxiLWXV7N!3%gZv6aE$Ml~<BV<cv}{7MY{!QE6=HukPSOeEZ&ahp26?lDh)SPG85hFQp_bLEmE_7BGBh^I!7yQ0)`X<_`VKveBVmU#FpkNVwU<2|P12FCy1K;Ue7t%3ue-kja&sfepx3N$mVes|Bkm(C>)=*^t+a6ZKH5*Oy8G}L*9jIjA(^}ztES}_sxXK8b01ET*@{%@$knKlQGjc9)^>w_UwP4Y6TP*L;XBKVKh$X@xd}v%!4NuI1O=u*&>n`RHat;yz|XM*u<kf5T4AGcB7qe2oLBT6apGYI=!JJAr8-0?@rm;>j#e&--!#*gTkB+*BtsXwwQcH^C5Hd&gM@>=WVnn7^A(EV{6#p(H5OROW)==IHGC8fD5+<t11c3y;h?E}zcCi*P&FKgn}>YDnNpnA#C$CxtR?b6!FAzf#&wFN9E$~`8&04kM)@+CD$**wCz9vKzHeu^t6*s~tK`W)7Zemdm-N4+?r$rZy(v0)siq2|5ZwY&nrSo6^{9-tuhL25isl8S5qKgicKDVBrFCoaSNGMqEMM{f(eNBMX&-rq<|qHi55Brxo6e>+_OclbtCfoxy?Of?9fJfur5ZQF>P&noAjcV%YuKBsQ@gn~wetuCt5drfnXR1H^OY{nm$~4Z1*%~&sneB}u5wz(NxhuW$*XDPo7s$JRhL9Jo6+pC`U|vl4+T^DJ6QuMw1#Rp*16n0IhVzU`1sTLUtTPNk6Z!EYQMQy1WzTcPmjkjWAb1alzDxkJ@B1f=X4Sh0Kb&4{Vj9(rKB2Z7ARltyw*E$ovbz=(VqEIYI5-R35^LKvRWUA8;w}bGWF~7J@L(~A+P8Y=ZRjCYgfYs4#fdf(SR+@CBDD1u63C_nd@>Z#e*Z`P7>oK2G~!KFrQdM-iESWTdRXnTf}G}K6(Gk+Ws;GWZeJPH(v()ET3Q3wJw^E8`Ipq6v!K@w|LUgZe_aYwJ{KQbH?g>>QgsoIP=hTw99knFs8lX%wv#gwO5XdyRNC*t`(GL#^r3e=W=m7+jg~t)pcj-EPeQrpWoqUxTV{Bt`JxC4o4!p<>d7f<da=uDStrn2sOiT|D}67t7gR5CtRnmVpNfUbIA(r01h4<V#5;-o3l#dH{!;A?SCY>CbI3LU;8+uFi`V6Mp2pkig1CU!-91R=?`~th$QTWG|-G}%}`o0x^;`&v25SV+}T86$cH8ktk|lUQ|^GD9IHB9tyBhwsz>Y69_bZ?f2kO04t@>R4poWY&~ire5RHQv-e3t~&yTHs)|MfQGT=6W9K{=OZ}CN1=F@MmmcZ>8&?_|mL!-Npb0Hh1CGk+vjz<3Jsx2#Kl+tV_7;gx&Jweo11>84p*ufBaim5+tAl!xJE3}9^%8#Hcp8P4YLlVd%g+K=Go-MZT0^THPV5cbA6->Y~BHv3^mxRxi9Bx^1mx#g+x+?hP3u<UexJkVFH@p)vm6QOVPk`KX<OlpbaaB2zI7-0(8b~!kDAJo%fDC~u@R9tl1P$mPMnfu^9Ef*+fVFqe_<<8{(hu>G?zNYF0d}oTwZkAQ4WCrb|EGf6peBL)Mpr=#A1hvNk0v?8ns>r*QAiZ4bJ;?c&EuQsq}o(gqc^5-RkoXk*a(>Q)%0MxrQ-W@3}62Fk1YCcsdxUi?%|o)-&?we$EACCrl{=OxrfhsM9h7jF%5^{G32)?S6f}bay1Q)w@t%kw>?C>;Hua1p_VsN6(740>#`j#HmA|nh8%DDhKJENe2pYwAdl#lb$F0<c&sv<b-(nqhj`W-N7b&938d;C?vPi$F9Y%Pv22+C;g4^%F8Qy<l_P@ej4qeX=yJkjbL+Am(QxS;jU6f!PFfrg8n}XkyGdj@%Wc|QRPIps|HdrwqayYhn>$EPR>ix-iO+_ftat-;CZs<es6&=!ebY9YpZNU~*-lTnmv2t%w0!8l54X{+&)=b%Jq#181o|G|n=_7`R9`nXYl2SO$dX@`;Gl~cy~kYKakoIiS2&t8uzoi!i;Qet=m}9I!;aSqfM#qVz@N^(#Nv{)FkA{(ZQxs!Ro4X8Nb8BDw)9XkG0OzNG^fQ8MFzczG7&9Zj@39B*5DeJ`$nkijSHW#s}LJZ!b}rW4^e+8{!k187|hg24+O$ZCIhkec2h{e%+3Mlv#yw1tm=to1rp|OxHT@XL|Y0GT+k`>osYJ~UMELC1eBfp%7?0**#3(9HP2I7Xtqa8MuT@BLOOZ#;oFw$mN6EvFCg}buw`QcBC~vCwcwErp>oWV8qoeg90WoMm!#ZcBvzDe?p208meiPbp{&GiO=A+T>4;*c(~Sp&i59+)U7&Gvrb-~4S4<jJkeH7Dq;sBh<<J`h^jwN@^p^Ivx5B(IVk~mjRz|>pORQmshc8UjE%CZ7lZ50|V+(8kxsptvm&6m3U>Sax^gkRpm@_uaEsz}#zU<G^R6}Om{0HxCA-KqE#^vCdexh7*E|-H#yi4sTTFsV;>&TvFZ5tIXM)tE6L8e_JUu=|Vn<Safh+``r<Vw$G-mnpIj78ef<#Z%9u4Y94ydY3N*Rxqt#(Mdqz_|g}OjZqzTW}dyFJO&r#2SO-zbkvfZELoPXN<;0^X3|<@gvj6d~AOAgCs8vq<<E@g?CO~Sd-{iSCW^_EP3%Njb5}Gy|)x55MP?-t;RZA$6RJL<}$K(yhvo4vqVPi1t>w{^t6{ao4MV&oY->CnupLWLK(&5q(DR9zFD(Jn?zO5244Y!s(~5+NW_@7%$f;#Y$HSh!&<OT&_+lG!Om;zB<!B(B)|&in*=8;ANqfOxR{%-wiGIUcq<X;wgNaVX7O4v*PBt<P(jej#k*@^w;MslqcP@rIu5+KEL5sYX6;~)bD5EMSdz-S8<7_aLuHhA6Kj{K4pD03s67V8SEcMe(>6bw%Y%_4-69>2U>($cf*<b{Oy?PicMQiXZ6|kgfjo@iN-gv(YPkjC{B$6Wum@ho;ww?O`?{iV`ltLjiv#N-!40pN4aFDF=zCKb?pjDuOcnB$lX|rb(9s?G8K<h@d^B2>;+@-hv!nvQO4HoCgHz{hG(?}VtSoV>TmMu^SMp7#h#l?{4_v7MewZYZhQ&mm)eC4UREb#G7ZLwxE={V(NZZ2lKA9xpCiC2ZR%@U!&=b68;9v{)C7)U{x5`9gy4sn}w7^BEJns1~a>mIEv7eK=WP>F`>?CZtWFBRXi?6?CZHf02nk}ZyQEA5BUEE9yj+aCOXEZO439F)x<TT@H&+I1Tl0-W~<k?~#>83MymCzHT94*rMPzn3y6Gq2nS|y4CE8z#aNXN_&m`F=y`KqFv`RPFoDCCWGUkpq(@u#9eNJhZo<#Rjbgf|KRBI8t5nk1yS0Bh+9T+qv<2zOh0-<lAYe<uFfl|O&y-B+fsOP~3=uwP4UT*uq_Ix*ih=BaI_+dfSI4Zn0@8Rh-1GW3tLJ4v;mq-!X*^JYPhWI9I^y{idTu>Qg=?AD^+wQ;%HtC1Bc{W{7-r|0WH-HkfXZdL^9E8DNZOuU^_(MTvnEkfS_s($&<Uw$#g4b%4fpCcTsPQI%IGBlY!Lsvw^wUx{_6Y34!(KP>p{39*8(eAUn>p>fZ>fIUGeLPMbO-s^H7Qz-h-@CzE-db7IfRLKkXPiHd-wz^$-HShMCqM}w8uXD`-A#NuE*s^XKO=LB=iHnK*<vulNj{i$MppD;Pu#9mwU|vORJ;_>!<~>oEbT-aF+B3h9+xLZN7fxBpkw#v-WwkdhKEij*Wkm2nY&3zS2Ndx){B4mG#`%Jbky#M4rerGxnT6z^`l7%b-01;2$c+%1PZ^xhih;1;Z!39C2nP8xIB{K2HKcUOgIiaZm&RK0((IZ;S{Pz2$Ab*RtO{BED3OS@7*)oDaZVa@NWHSxay&$XkyX)^cJPLKG36;!UKV^eYNsU>l--b`f?XF9O-;twuo#d_Hxgo{(!c$a%yL<3qGz*V$&Jw2zy*1wPK=qAYkeTa$0y7W!LSj0tIa`zKbnCu>O*!SCmqQ#Srr_mhfgw+#5zR7$e;>SVVPfY%{e-4nUP&?x&M<tRR^F%2NxuObo0aq99?JI7mf}3RAi#D-Lp_Ed}E)6gGD(0w;9%fTrxgI%!CEvB(U~0e-HRl^<rVzErnolUuSXzv+H7S!F!q?D`Og7AsxaKyBJ2_W6zXC;_@=uLsS#cfd^NB(CZl<=$Ac5SHYO8jP@4jXIgq$w!W>lVBCe%y*MIlB`%GN7{xeP6D=|ljdbpB|%d4T$P_hrcW3N*GXxpni+Ot{JBE^4{)G;&_2jSNW6q+>Wif(kVz*<&PZ<(5RCQHqrDz;XNcxgYR54@%JHYq=97w%jJ)#F!}URC#wz35(b$&fCz@!@>{))J2BlV+&gesZJ^z_=?DS{-#RJvKS58027q6VWHK8wVZ@F^h>6cKC+0DND`G?AAfbo84omR&rk5wi^`x5;BWB2QR7y)7)?$6j#S$`Yl`C*LbJ<9W-@v!2b1VDkT4J=>~%wIY4S+swYwOu1wX<%qh?=S)x$W?Sk9fuUJDsjQQlmu{;lY9fM)j-q}q;c5Qz+%{hL;3cdW0N_w)C8fybYx;j@E53qyrIh-ov~`P^b#)5(z}z02p%vgs|usRZ5V|PaMT9gWHc&r<5TjgN%nn#!f3b$N#I1g)N)#BevL;%Nu2V6G`%UQ9}V#gMu%OF%qt^<3SExnTpg=<jo5o~l$J9){;gHO;10-JkBV7f%zt)n)B}a1D@Hxo6TqvdjqMk*m5s2kAd-*bp^33Kc{BzcMtw`)i*o#uSjw_!Fi#7pU(-4}VnaY@Bjyu{%kHkExC2^ago%Zo_e19CG*rQExYcHZBYf7mX0Y41v#E^O-DJFg3Nzu`1JWpXT4V#S8p+%V@E<$mH{lCdTUY^$h|pxifQB)Wxvs-p5N@Esb`l%q9@f?M1dtHLZq3s}8wU45ryf-kS8Z9J0cxZ$iOXAyT>U@z;0^fpT=#zJxIp^;S`8cGm$l<!>U%iUV!su~P7J>~3x*d&8Sb~R89DF4=ep(E_$i~BoCR6m9Xl>#4}Lo}U8*$=L8O_2`G${gCaJ!*=3WbY{EgO2UT(SK+!DjrGWN=9*nO3+HO36_2a$CFm97OG?qpJUXAV!1;iIjp`*CxQfIqJw5G^yO!G~``-TJRjt{9&&6u-94`lFc2jRQKct%*$M`Y#yg+3hR?c_{m>EjBAV5RKh|+4XSb{+~!u6xMcVPOTDB3~Z$CoN94QkF8~z*5o621F4o52>XuBf33RgS^VjE`B4xHVsM77h=0V!k!Rs33xdfw@K9^wh#JD_gd|!Ab1tX63}}6QgLR>gwN3?`A0`O;k4z|g>X=9>D<-QhHqq+SRGum^L&8gN@a=+`!OO)=;H<6Jx<#irD7>LYBwyiLk0K&BV3PKLWR4$df-G=&v)!RLQFzG+GJWif;GrQR4buXKigmO}{;TDhH;r$83dtW<<5!T%!dlwcGI5v(tQAq?8S-KVqHu^}fF-c9&}Fx7umy{~AuCEU7q*cNDWEd2R;~RA)ylCZE_!A8jJ31XnECurvh=+rJ+Ile_2a)B`e0A3%PZ$kF>{Rw=AN$s=we7L%9j%c5uI-Vc2xy;{lcG}^?SQ|@NybkAOZx>h(eRndW3q#gVCZ?KI*8^MZ2xY8jiGOslA~SYalyB(4EAGIV_2Z5*(fF#rAbpQJe*0kL;;_{EjMKW|B3^0sreK7oCe0CmVthoBBI0H%D&1{8ZHwKRcaO^=R9e*ch^fhUh32_6X{WL|O<}i^i$1-F@szdr5~xIoGSgmnvY3YqjStqw1bfl$xzk&bYGXSBlYycBr~%ek67yZ((X+^zNuSbxc=v&)CT<2RYY)tw=BJusp3n=+A;%Ju&!W`5UUWn)i~3oENfnWXW1-VZ!!)rR1oj4@(+K!+bvA_*S>$l7P7zZ5=7+Uv84k+QAw$DdUiZ3CvvLOv;)dme~E`LV}`fX-|~ckoZJ`tr@09CWv(h9Pq;<Cx{V2SZ}{W`1+FY4BW*7Dsaa>9DDn+tk}mA^akm4r||8d;ZOkulkQP`w`g(^h;AsPgnx{UJZ}`~cvnXBWNG#zuftIns)Yu|qo>4WxlTKgCe?6B!@Vap8+_`9niu70dx%UCS%G^y_#>8g2|xNhfbw0iCdCPunxMNZZLJKuQL*3w)t-%A&jbyR!7Kd5>Yvg5dAs*EK79AZ_ui<Du;*<PC5#|Y!8KuomS~zPiGXzHXnF{?RobeA%Lh@Y!ihJ&mdd+Y3=7eit}}&%P(6*t>@A26HtHm-z<th^dy&puh8;9fBiXm>^0LS(x8-NR)NXM{p?zRgNYkW^ck#gDHiG3bOh%nm6AA+b*#vcL?1a~>T_&UH#%>kVrVRwtb-(i7E&`;wZd`}pzbFazW~S>%w?18ms21&3LB_5Fwl%?`O5U3VEKz>T;rG$hqkw;|CX-9mj}1~~Lb6-#Uno#PRVBL!oir*Ks8KB!VXl(1AI1xkk&~NML%kqtUXZl7AS}o+!eA(l@{~rrEb+Y8)sWePq%2l)Fsv8k-~REwAoYH@yKyzP)slH*^-D^RKrtjrlC9${A>gU5z^Yz>HcP0`So-rDV;|&{vA7OGvUa)-S(}XUQn2efT@7;;(;d?3g0xO%)!iTYO4sC$ci$ALcs1@VI;DAZs#hS4p{edLSK&MyCG7wfV~_8B3^k3!r*Ok&79vnkS*a+phL2JnqfO5WBd3Xm^Ny)8>Xe&lIOW`wMy&&8A?9Ss2-8(zmXZi{|Hj9T?z8bDplVGb(Y2s{eFi^RL|@Ke)-6b~;Go7TBt*@dWFduGLW(CV+krgHM!KDi^e&!-bBi9m{%q>3jln=o7Rx6U98_+;<^H5udOdKX`QV1vv4i3<Z{?Dk+@YS{D{m*;3rx;?f8e_F=)wp*%3Pmu&$)EiQIMC(R?q!5ik%Iz$&$d?tyvy<z>RV;Coceuw%D5>?X?z`Uisj<nuBIyydf8vtpJ~aC)C!1TRo}BG=}&PeMKV}c?ZMGu-wNuF~FpPud6flh17t|l(Os*a;%?%sdn#&YDB@b%!;Xjz^E<1Q9jhl2&9cd_%Ci%ez^~?8~(BK`)HfSl60-8_ZIG4QrY(aykrcsvhPmiKr@OIAf{xTjLwJ^hpN4lV)fqLYMafzli1-(!UJwM)UR^rt377f+N?=3^P~?GdMFiIuRdwVdJy1k+HM4-Yr!h2_#1JbY_?`)8G8~*Q9**MLYwqj1kMzzCAfLl6G$QjTO&0__|Y>pX93H~zN#S0>Ap|e76EslzL;uEErYe-FK8U~=719QarAc2>}sZDpB^cYAu=WX+G9O20S8bQ_EZ^6b+?}hs0*W)V4}WU**pBJFS0=`VeDs6e(7HE+Gd}3)`jG)QUR}wA90J~Ne_6Ev9WWq-N{NlYLMv>Bpy9(A@z}%#>aebiX%c~b>>~H1~nqz7Yz5ABD~+DN;q0iwJ)s&`g85@4o<rwDa_^v+%S)NyQcX)uHL{s3u=>lLnY~E*6tQkK|8z2@v?((v8-j4Px<R*Ntp8-5Zq7PRKYqnl`Yl@R0mYf`j#aW-AJ(V<eV!v&kj>IwXUg!%W`*vn8yu2cipU0LvKw86Bf9!#}ZUH^qJdQY>6<m&47&}FrZt*t8^{ylM+}B{TpOuihb<1gScX3Pi&R3VaMcKsRPGCdHKYiQHB-%avwDf3U3Wjo{7%$s&6FnC8!-C${)s=yekr2r2`m2(jcvoV%>Zy2E)pQYN1EnQ#P6yR!ERxN-7ZnDVT7#pNx5GMPAHU$@MB{@RF>?PFFIOkwr3A3eeTy{pD6sk~cnz+QB-qFmBqe!#u54mcuV94KQ5=q9M@_tC#)2%f79bJ?pZ=r#F>*2HKwrl6S1|d)A1?k~NX2VP7x!+VP@^u!%VfzN|N~ka9_pUk)y>ncH{jP6zw1XK6yve?C>FSh>`DqhSVYo6!0St1fIeF0Jtt1QvQk&VkcpPgDfTctmGyr8EC341{k|iGVZC>#(662s=ugZfmPYWEx9t*UnVJRV^(Sft^5lp@hzwYHX;K*Z-(>w)jQvuZ?GCznne(>Cboj^V4{K=s!P=@TU>}G{T?${4~Pv@@IH2e}=byZ+@F+^M^R+ul(oNls|l$r61_eaQ<w5e;<@T4eZ;zH$D01TfO)9&%g%%mHrIx>CgP)KV@j-XMfJmN`H>e`nULV@w<P~?<spbRI6WJ^3&CKU48KCv$ubS>pxTW6&Y<1X>WEeY%q>S5Ptf-zL(YNXhqnwe@5%$zm(0{l7iH}Vq&c_BLe`mDFkg`jVz)eOgs~P4am<;L7yz%m#?pH%{3(Y+H{izn8f{cd_BT%5edeP0=pV~-d;BUXY8La7U;ckblSy>tIEvmjko{Q2f1*5gxT+`xb({-_}QP)pPzrYcK+Uv?4|K{jP{P0ce?~CM!Pusa~xQ?ZJeE+^>*e%Iv;_0V$SjwlWfwdUY_T4WW%mkg)?twYjB~vbar~00Ml0p=U+i*esOgw%Ie18+hlm+YK|vK__pw#R$IIi(6Y6DNicPC7US%90?Fm<?Z!XtXRxPudebBI&v5zF{HF`IpE`S2cl~A0AI;CsaCYY7pP^rTBe#6n)1P?xGt_ek*G|SJ*zNNlpIv^JaQTg{o^4qEX;81T7j&~fm)BJP-0XKdtH#YAH<Ub&reFN*Ey26XgN)PZsiD>>B{x1hUZe4q^pMl<!G`N{PToGaI5$tfF@(1}rtO-?BR4j?#;@#>aeb!Ih}Q>a95h$oUTHVpUHuv6KW%ZrQwt>Zf3u)nbkxt>PQ0%$=Y0)Ob3$(b)-fqVof$ICVk_m1`ECOON4mj7a(xP`H2`sxhoWNC&e-rd5q2#m0{E0+AjRl$A5s@uPL-cXzB0J@Ziy@tf?HMY!l4uO3q6Biw{lp?lzgYg3IlLJYwkcFXsrgQ{%d$bUDA_?`+nsOVT~74vdD|vAMnjzu}Q2RkZ)_V6(*%zOwhferfV=ItXL)UMQ3V_8B5)~L6&xe@^MWT#@as26Nt%PL(HampwuFYjuq_FP4l1GSwjXIFSYaoLKGzocxJ9wVl(MmtdM9>Esa1(nNg7ky8YL{2lRDn+&hY#a1ogC0f(4!%M6t^+_6u2MT{mF$?j;b)d>QmG2SDY9g-XNhDvCKyGcNEmn$~3M1Ul8QakWqc;x|egr<%JgByWq<p@p2Y&6?|SUxo;8^1Nhz&nzcN#7twWsi{<2A2t-c+jVu*wsX<&9(5mbh<=%iYHvAH`G&Ca)%>SCkeX5XVnmI%nnlUl63S+*>PgO<I0Oh$?kpCCwVJl=V7VWy&&0``P`+-4sgU$>K<*9o{=>(X}o@QO{Tj%HQbizhCnIXnem!TcbF*}%w@V6o7zgOX+~E+iFIop$I;=hYU+#vAaf}lUx(#of;y)4(Oj53J6&hquK^M+LO)1l_NLYIT<gq-dm#sWRqB_H_kO0*dM432DR@&3l0pU_U%~rtz8^F4Bj=;(2*0hh*UVLo6BbaIxei~brd|-p(QGvoX?65kN^sDF&Qp9_-bv=@MQp%UC@kJv3nth&VH>Jphp>_O-#sWBo=me&aK#-b8cZ{>X}b?Mjk$JJa^{vX7kO6Y%Ps)-C&?=>T)8lM>zOOpXvtO1`Pj*o>tkDT{ZBs@zV_GETt;jAn`$oS*7gngAki({?MEG#bA$Ua@Cj6s=sr3V_H9hqmzyPG$>OMgblc-TETvr9mw4O@xyOJevo{ju&xL(0<T;SKDLPN}h3g*oq#V9Kw_Qp`k{IS}H1Z#J|EVATkb8Xe9pS6_b3!#Ap%{xx^cYLR((`<%hC-OuiBL=2)llvm1h{;lsDN->{BsEA`Q7$}ia9?PrORuYHBv6A{^@T2k_wrTP{+RHvh<ftoy8r!<_lsm=fKLeuWME#w;Ow^B${o;=aLC*(mW7wcrZ^{ss-TZYX=<{ibYz&)d@NFV5rbgU%8@|u1Uh*aX%G=Q6`MByyf3{7k^=@M>b#ZCqum#Tyo{QR$iw@%EFhUox_?W!l*rwEWjD(<qQ!R=ONF~mS9K^1rQ%uyAs5UkTXyMyk=@SKer_hdL1pci*y!~5=axn79iG3vbcjXmINBsQjt)#Cdz#llbs}Z;B`S&cU&xta|OU)mhTv|hJi+FnJmx7YZ)htaZgv6$dvmImTWx?((D8_fX|XWNsrT$>2eYDymu>3{8mh`zh+mae2X940Ck(=OAVVFCc2j~6XFM;z;)ML-M4c)(=ldZV;xtAk&sZLBK+UU<kW+-;PO%HtqIO2)2zrQ6sn938nvMhR4pDOm4Q)Hl|0G=ZyT`TaH%&62t22lYlusTjU5=-IFoWQduqZZ6{PuKBkDA%d47%XF3Z!lI@uX1U_%jGZmDJIixcg!nK}vK$`?q*(N|*likT=vZYJ`Q+E#?rVu%{j;_!(L^Z||E%6u@J(KP$Azx!jcHev{`t&QG|R$k96kI~SxqDzW{Zg~H&lsw}m+Djv965YJET4Kdsu9k9F7@g^+ZNe=X{HImVZY`Bf)!m#el}zRqOJ!fR&!QOlTq<)~3ZEq@aZZb5C!rda&7WN-+mFu0{}<eU<a6t@7GbTT-$L5oa|P}mvBWWg_-s02bsc_10vJ15T6jD1II-B~>5<1r+j5ovZ#S6lscH~(o6xN>TA!8QAKWS!1G+nM9yzIN<Co8=N3~+jWCh}LD5EqfV&V~sqNxPV2NBXAn8Q_S1GD`STTJ_GIDvZ}tU(u>N1(jhlUFr8{=;|iY8h2E#Q&Jx)w9hLBk-9&OEM0N!gyxwsv5OOB6H!@f+M_@QOgyVmSA$bTxKaQhz3c=-e4y~KPs0kyjs|kkX=iz4CuDIZr8G}+n{jMu4VF6?r5?$8nwhLMlF)jU>9)X<=Pe&UM<jkNl0<Ms&RGC|Fk~~byWN6&l1B!=FRMJ1+_)fOg!89r}@r*?##lAc^6_OjDO_aTl!;T{R;o>-l>F@>-WQqxLB}E5XWa<6;t)!W>(socf{KBv}L{MmwEYR=VqMv+=rc2y~HtT=aT+>dv{s>@_w{CnOeZ}e{K}D>aJ)`*IGSATxNy(QSidb5F!tp>8k6UIznSd5PybWpt)%^-qsJbxAPwAt~omAdVCoK%sLCE@9Aqz@5SXc6RI7*^6EyP0{2|1W%N;EmuDN}IPBx=@hSf1p%y>m_&clcc~Pu$*Di<s4DRCMx@UgpGB1@tyY>D2A47%jrbsYcv8g_r6}E1Tf9AzmJv##R4q93~eVq95+g~Ze%_xgr&u~i?+FoS1P<N>r?&VH~2CtUkb|&h947Vhbd6waN+LD!9zg2y2>BEjaNWHmRQ2x|n^KNz%Kat_GtJ8{ZIhU2EB-51P2Gw6oB0D!#EQf6-A1{+!oANQtb$xw$nZJi@YM~?+(d?ND;nk@YvC?0w1VK`v=C)y32FkPCcEtiv^U?y)$4_j3ago^WKriZNiETPYs`$k$?<Sf$N-i+*V#X6LHGP(hhMY<=+ks9MDN5ScV$<Um1(GqzZ4S~3g)*p|)|K$$s~<q84}4iiDP6kFdP#eAkyI%1RfDtC^&oN}gzRD)O$jOU<W<L0&l?osN=*z3j<4d%a$B~&l#$jHK9AA4JhG=Io=%cl?P``obrA+uk$Yig<q|*{5Ax50-TQM339m&-12cvyUPtbgy;0-x7akR*jx9J&)9#_(|9h%$i`UyCq6}qd!Cf?)tD#4dOmcA8?$M>DnWa4&*SMMchC*I<l<h(h0=lNB-mQB)-tti8TeK@QB)1XIZU?uP-w`@rA-5o4L&t_s^&R!NHmE>#jaR)yDxqB$x*gPF$`B4AJpB20mn%MvLdBd+`(=Hngv9NoII&NYIC07C@JO>|42+PaDM|k!Fx^kSQKHX+ni5v2M0C5EII)*X4HK?h(hYhVAXGw)kR4FCR(OWEl4lQ_vA>7MSp)_3azlL!Xcg0LjJI3~8rV&hmz8lHB*_(At=ceMDxbJTFkc^_B_4H2od?)p4R(APoFSTGah$L6gMIGZ=Wgfx;h$TG5Or9)x>1BkmjWONhy=$Y7^<g7Wo&8vNXhFms~+8>gQA?dER@Uhpo)XLN1Z=>|7g}HrwB6c=P2x<a@|8uE0oJZq4e@%B)H|&e&UtND7-5lgl1zL(Bk>ZZ|JL2ZZ6b_QFBV=ihT*?3EW8cR5$1V(ZFsv-=p+^cz^KH0RL%6Z<LdkAir0@`48S&dG$zD71dP^Rddx>OT4mV>#6dZ&B(teb9BY<3H3z$vr54c%dp9=sx!B$IKUo{G_E?9AU+w{RDj76u`to4l1|hB7sANxd$|W816nRruWejM<3+<og|=rPXFXqfXG!YCedWs2;+INV%+D#+NrMN&j<!;19Gf#C8k&R4w`>!mbiydLF1al7`<?95WHn@gq8=94$Z9A6uar+|I<FzcN^GhPGM>i5t9@#eCaq9pf5##WP3PV^AA3UalZDi;l8?1vlKbqoQ!>{0x(~aoFEby5;sq6@%Okn*^j(=87LrLtBXQ~GzCP(9`|?(6PVBkhfksz@eF=!ab3Y_^O=^yG22x=BkzDmf#^s;LxFoWm77aH&9mHu3<JQuoUYca|4`D@%kfgHb5|}s7Gp^1cpL??nVbT>sta;aAmUlt5Ju&I(XrP?VQZGuNLmz~Xe2uAB{GE3%oyp_)tx9K7@aK%qj))mqQ=Jvff>q3hdBsethg-T+O*8jq^{hLqo+YcBne9|_Q8x=y(QJ6KXlC=b7R}O?qM0gVet%IkJ99T4WG#bT3o2&axwWw}A$;r2%gSXm1X|h|$8euL(cuu|h(a`6E0;Cb%4IyyaA%~Bn|s~nYn!?M!zV$2uS*ahyc<vI)1RMo6+SVhKaKFGKR=D|$7lW50_Z2=|0m-Ak6H5IKXLy*asNMY|9`)8|KEzR|J8rqp!|;<|F@$2Pye1I`-f%(e(c5ZH*S6=j#=RM#+wrYdn|lAYnLrchk+WXzNvOuaU`mbtp7k@lu^_#`Tn7LU9uMPG-ZClaL-o!Ft)x}|7)pHzgO0OoV}nYCD~vY?(A86YW|Hh+r6KY>*wEV{H*$mOMb?(?_^sfmc5&pc952hdSra@f_h*7oWud<--6zk^Y1>wX@Xzs1L$j3e(w3VNN3+-`uYp40Fl4Ez)moQqZyENWuMXqaBA3&GphbsS>Dql3mE}FlM!gnWdv@|4G!kng$R`az0ebYR53ve&giLf2Qg44OO@=E$zf3Mol6b4Yf=N@Ikkb2Uq4qE7=KA7_;7=0-?=BG2F_#zT(xREdv^N8-~8o@5P_e#=Vx?sJ7#l(dmf(D4S3nJPn@drPaee2qzRVa?#j8%PrJFzroXt#(@<Z$pfcRu8DD;`Q(-&V`iS&o&#3n<o{JltYaN71zQA3|DTJrKj=%UuK2))SeDjUZ3K5(Q%jMvNt3nDl#0q93MsP}))CtDH375m-uRpSc5uW4gjBP&tTh!72$9G{N-7;+k4Pw^y3Corb`jQ3_?QasJ4HBIRiI(5yO17fDx;J;$#i?``0-!s9M>2JXWzhu&OUVclSP?DTi|XHiE98OP>_-mtgo}VIL$uCK6n@hrnE7@hhJ$(`IhwM1hTkmR*qqr4M^_!5qcv&#)TBXovKjj{=E6%I_9Posd|cBmxqQw%qRzUCOG5KV=L2)=W1_kK!URJ6@@mJsw!7O4M~t%xwNs<;nkmM-#a*p2c(=uHFn5f;8jR%8`zTclOZKIs3^I~|YtWY5&1@^xr>ktKraFk3M@Dr4m+xd_cq}TH!x|b`5g8Vt@z=v0OoltXT#|Oa15?!<<WB-U@(_<R<0CMC!eKN5hqH@Zz)dy-qVGqubrIh6jy_-VbUBm*{z3N_UTpmKoFDr@q*JVZ>~lzX%a=8NEAy0dGxo`eogG$nxpjGJE3qRi1>z3lO^tqixiBk=P?*0i;VNjyCfbyx`DIw##b}F0Lur<SlxxtN6T9s8h;wma&1Q8HUW8e#FyQ)EE<<y~JZlelUM>Fe;9*VM0h+OwYjZj|!%Z{j?!1Nb?gS1?wsph5(DEA>GUf6J9MkyV0Dn!G%C#wjC08yTfK?rJ_@yM}N6?SRw^eWmR2%SUV%JiegjDDWi50bLvNehp4#>&=N#)QTZVp`{kbh~eK_Zs%W__@oTa~}DRfi<8DDPrBvUy&ZR{(A#xr8$o0ShS0KS6mYV&Z8LnDhlhnAUZs=~)m$oTMpYbTmH>+WsZsO$gKAvnLq}C`l!224D?=(t_4V4WnS(dKnC|P1S};Kp)PxtmY?f#+lyI@o1Li7TuQ{-I-dD_^<Vm`3t(yB4l=iPyy>9=5g4~(X*as%Xbl^%o8%1yv%ojCRyFvJdG|VRh#-njJ>du@3~!5ZO&znC>&~;jb&bu3}P8Z{TWX*xDui{R6+%!$$#d4A*S!e@JL6OM^bk7h$BOeVGkP<sNwWA=kS>InLfj*Eo*I*n>-#Nq!$YwG=@szqF+eyY>4=3U`N_lhvBk29b`>T6m_67k!tla&c?(SAG|)Eg|y9FyZ5-CkMh*ndgDbqzZ1%MT?Q3OIx=mL_v0fX8XdZ6CJ9zFWqX=nw!ncfUL-KM;c!2EOF*uQ>qOnBv#;<PKt;glU<cB0brL_PH4Pbg%Qg)%k|60DksWO-jmy{&t5jA?-gdk-O)V+NUB=sON+ML2xQaltU|C~e9h@`GXCv|=N`}Gw4h?<h<xtU?O=bGG-g*HVz(KgO0NujbX2U$ff96TR?Uo5-R&FUbplDeFmkD5Q%`uCyz!0raR9a$g6;{f!(p9u=oU(y(pTI9}r2h1{j8B1VH@HnofG$^H?_}`n=(yrM;qPU!YYrtJsOkcV=-9PV0R!s{d(0z1YRehi)AQ{=dF#CXXTcW7*qod|oaNxnnr4qokO;P32n_hOSJ5O?jRD!J1WT5Ik_VtyD;>`_Ge?Ndl7h71k<GTz6J<<%YINlYJ*{*-u1xUNE~rl|+3<)x4@kBz(0EB`e6QIVVPeC@zu^Hzy4)z}Nlb%F`ihp%z{n=K!P7L%+cq*&T||OhFfkSIzTyh+v9>ZjjV4qU>8VUjg-Yd6U4{pT<=-8hPy#1Q{W|3|)>!qt`Q4Q_-BEF&>eE19i@<(36y9N*vZdHe`mL`-_;~_gS|V6~0WhTmLAfN`yabqrnCEw0+0Mb4ssc;{1riWTBJuxB!y7}FO6N+tX_@zAN0T4HMu8#?mXhbm&X<{Z00J@1prs`GFGzW;7*qMJaicsO3+bGYm6X?db5V*_1q&A2Ga}w~bZLmyI!h*2OL;5lr1A>3EV)js#+k5H8Q66jrj@*1AWh{t4cIg3J;yoHw7o&^xw0YT=HR353FB{nDCvd$HA%KAy<iGg??Zhdj+E16nJ5jt-%gpRrQCwQR3@4UEu33WdlyWW$XTi%r2`$F)>`QNOJ?qc+=5b3qn`OTRK<l0J+_V$IlYbCLSIRl@tWL%1<KjX%^#bX7XR`)l*if=&M<2kO|mk?SI>T0I>Xw_bv01PhfAmFdURTxRwz)Ex0e-on~_7V#}$+9$KZunR`<&|4p_nla)7yd$?cUoJwb{=nvmRP2O1-4XW<FqM-`%_R8NVsD`tut3A{#ab{QHYI~!1d!3XtZ8nt8)m!A!h&m>9HFO19R2KrTW_)039NqtM(1f%i+qC6m#K0ZptE!-zXE@~7GUJN^cx`%LTP!AIiY0JXf_v^}7MqowtDD#E<Yj0hPDg$u$q{hqoEd*ZR)XLzp;;Pg2GrM6%mad<X*=M%)7FJrj!qO+`&Q`#T6)-NX?4JuF*TYAsKK32mp`VKm3Ju;0A6G-ea1j(DIk*j0vCN$pCUUEfW(S!ES)+&&7!G366duc3)xQ2v{_h{@!sg>!k`{U{CD%v`agB}6g0~PZ^gf=YE?m+3m=(dc-UP2GsPQ7nkEoh3-H^RMsD4q&HQjag0uEJPwt9i;M|+#VFfi(OjKf<I?QRno(xm!9*{&-b22wn$qjd^T(irgR#$-q;k1m-EYcF{^6na**Li&UP$RaZeIQW?e$Zkg8mlR0Xdns6beJjpyeyD8zk}f9Ilzx`YH!=HjEiy}y0ybh3U2G7~`dqf7lN_k%V)8v66MBz?p2X8pxOU|3FX>`<lsUbM7h;Spb9&{<o)(}!GN{$$J~b0rzozv@0hHhGlp?(>v%e=rD2sfkJSbwQnXQ;)hM-*puTWUD+_VRUziOY&u?usNMiP?O>z8u$<28}SuUlQ>U1RQTq8I}D?gcVSSHmu+^CfBQR@hbDrwebx6=U7J$}HWWi!Ef97;QZYI=5w(<YIk`F%~xL9m!4jX{Du(pF3AtVx0o1h2$tF_L$VNRb#Rn=y?uVFUcjao2STo#Mzqk$~)1>qS~l;vw)j4qbVHlbx-R5{;S5^_KIZqP5I^3OnbR!=Q4u<jw)t}u$N-XoircahWaE~H0axs%bVMh%ZDntoSu|i&NIp7_4AU;yxSl;C$VJ`6s6C%zEoO9aBrKDLW^^j%yPGsSuWpnxF)mQuB5Sydi+P0S^n+!zEaPp%&nDr-HeLeFI}w5B)X!sTqZ?#TS!aW4;Hzbu1+G{y3;;{Oz}&tc~@~3D8-FBl3Kg_^n@x_)s76Kvi!}J`ceSPWWVQomEM-@GvUZfjpb*ABe}Hu_fgDfzX2<_|Bb~8{+_bSvR{7B6E<E+FflQ)HjjDbsQJcL4J=ir)G}0AsHSF@P0cPLJ;B6cOfcgz!HjAP({BATyKH9JWh;D#wUegoGF;5raFJb>cUfxLT1FXfXOx(W1Gdleq!OtQ#CT_wVJ4MX00j}sUsh%N$i?Bm@s7dtGZe@cOYnPfK**E*L0&C13n4df?$m+kna6@KYi*gbWsIAMFI;~aG$ZHZ)s>eMa7%<+kO2&U9&SgOYicMj*58)vuhwM<#%#^<psTC!9fec5_+l#kG;ss1JPssbGT9thHrG@QP0vK4T%zx5{dImd%i}Wf8b|lh<?h1p;ksWOa5eJg69;goWn3G3V00o{#I*)4MpqVMZ(?{Wb}+j}pJ7?sBD5vOH9Z~$KMP4shEx^rJYX=bpUozg0%i0v2DP9HAPTV9Pz#v~uw>(Xbvp2xt)qyuA{uuTmz}Vi%65KfbHM#FK?7rS<0>4M;&##-H*q_sNgWuxL%-ZOvtUJNi1k~ZZGe6BHiG}vw-y?^tU?oKR6AbRaCja%@f8elhJ+9lPe_Ov8ZS;zJZ-^b^b|xSXbc^>($cx(cu!C~W$oPX4igk_kcw~uVyY&3SkODhvJGm8l#+`A<YAZUwTIoFq4C__O`>C7kg@XW9*gF>+($#$89I{Xfo_3{C~M$p&+D9!@M8CJtTJleY0sMe=G>GmzH%&MvUdLY43k&p@jil$glEy=$ZCkJS)VAcZdE+u+OL}hjSMtY%6oUX$;+A?HzE-AVJA#mtDMzL+$f#~=wlMKB^z+6so<~*E{)1Wzvyt=)6@-Nq7^>Qga{=iD@0eM$U6%FGIVosWN+NFPFDsp(Nb+C@(|tDtT1Py{Rm-|JcP)P*K|g`N@i#&ww7N5o`|oMY%EDMF{8EE_vT+BB)dmtL2)XTk)<Rs$x;qrBk^*Oyvx3>^_^T@ohcKCI8nzG)JCLepj>#{qb1hR|3DC7YG>m@V0o2`Y{}_#G|ERZ^9$M1J^a$98aT>3*Xn<XV-_BOjDY}{|N9?mCA!+*E?)rqva&4uWXllOAQ#VF$2!_H<!j3jD{Qt5mE)=F#-$*Ki<Kx6kYTIBEXl3{%DKv~_QWYp1qLvVWXCfT0GnmoCOO_fb@i%Ta&mL~F|Yk#xFL?5udPbQ5fa$|Sudz(m?T$ct5WTm(^mv_4{|-njUgANfUYOL*IaUyqqpu~iplu+OVa=Gp#T|MbWN@UGSq57t8{6QcMFX%SEiew7!zvfh6@Hl(;STvMya@kEFEs_E9Hu@&(K!*kRc^Y_=>sWEzfZn)ClgZZgF#ZKGkH{q4kMnfXJbwv`Br{G__XKr3+rP^%~xm-ln7$L^*vPThm1pY4;6t`Z83<aaK0rn4)0I-i<R96O%Jk(~~vZuWyFZd;0JF9!9q{OLSXUG{asDaO3YlcjQ{4sOYwNp(34CDcIG0+e!K|jGI6K*AM~SB9hM46g_3V{mU_K7wxh9O~APQ#wS6#PfBW^RH#1v`DuhdjqvY}KR*q{C%L*$a&@2n{3KWRNv`gbT-_(Rx_6bUbID(OFx6k0kEUB^%Ts!(dYzDzFk+>h1RYH%Ap%pe@^gjOS4&oYFs(Wsp~}_ycqW}DL-A3oZj=(U_U=sa%~~{JCW|Izw1M<>e?@LgCfjDan(BjFe=a~4-$JqO?BM4@Z)-cOoq2dtt1g^t)!E6UvyYpp&c!NGmuC`nJGA3QwFGIUy-2GrU(>2vO>%*f_S1K{6so&asf%()P44n5Px^G{UjZd%d<&V>=rxm+;dtiubwa%QT{sR`uSmlgV&4e2{MBnpa`Y`7!wY3Pe=bXh$k4I^x%TvOiY8ze&vodedv*5nX-&FOa?bL}3wgNuf-o1VyDHQ6!l!Nu(p{5sdtTpdF5^{|>8fm*8lF-U^Dk7UyHwK)@q>%g`K3NxNcMYukX`6o5_Kk<cvCvfzQU#WTDq<cH_FC6BUCqcxu`Q_)M5*D{LfVC!o?$Jx^?3(Zy{ZGarN0+w-X4XhFyF{|L!TJzi|N5HHABWUFq+t9NxKRVw?mDr|+`V{&O=?$Z%umrbqmwZMRU)S=g^u<<0pE&TIVtuKRVrI<R~6ZQs4R0=yY=8t%}e?4|4$d_KhCo>T?6YJs%c4ES?EGYlS1<so8+@kpk|93fr4Y4~S|LxXlsgPsF1!jZibF+1>j-(-57me8KdLA>Oynig=dhK<qQUWu*?x<m<gPaEqe4!$83uq7M-M(MDgBV-%@yckp+yOVqtShMnA8e$*xdOLHxC5M4`Cqb>{C;pYM(4{a?Y%8^q2yUtA0cwlxS_t}@v5Tt=o6XJ+h}ZOy297*t?_mR9KE3V1LT>nY8H(4`!)eOL{m}mivKLf#0@!2laON8trgRaly#XjhBA6hL<vt7P4|j1WPqA|a<4Q+J4lo*i-QwDH4Mu%a#y*vAQ@%O+XS(ub3jE|a1sLH(;Rb=Zb^YGwbt0WD35i_tv%#AZAT$+holXWuiQ!F)rq~(!6o}+9v`B<Gl|p!f%w5)VSoGcie-fl2vZbXOFFt0L#33L@<l!GG?{gfGx#Ox01I8(^X$jok!2Gh@p_rZl-Oo3b>w~5{LBuOW6j7Su(3U^VB{W8&RSA{C5vYXJvgx_?kQxDxj(1~Ah^&`0FA1UFBRr;KhjAsVN)I9lJCo2ugL+E{UjV97g>)!_`-W;;<*;w82TF5D#{G_(EJ9v$Jj)d)CDxmR=o$iLAu)$<@!iY4RgUA-)gLPJsZ$>2i3XxTR{7<J%zY}F1uysmq&<-_4RBXE$$Q970mHN@lUf@sW-){kS#$%ppAA{R0>Y_$>z@KoC$dxNbmkpjd8B$;*%6$AeG6mgV6(-PrN`W$4RLup;{Kb6LC6t(Mk)q^ia!uS{DytZBxhU;cKpx}(boJsU#SCMZpz_C2Yw9*X}E+oW#IohA{^JeFB<_a=F9;SG^`chTh|?}_{I}QG=q##5}|KGSM_-&)Cd9KhHmQ0lsARCGh69yforOuChE4D6QrNvnnp1~0Wut6vQ3p0bbvOcOU_GG$y;z<452i&<=b0;+p#C#aSR)i4I15~iMF-<X{(RpmBL;#jidqsZhZxmbad<-(M@Z7ogvS<@!<m61km4->Ow|gnFA#*wrs`IF#D}0WAx7gnST9UBsw~3zO`^@om4tju5TAA9c7VSi&Zg6bl_@7>O++)g56>7B}P}m$C}{)S{?W$nphk~QVi8W7tzS~BR(c@i4u__kZp}75G3?Y5Z;sXD^fB>An`Km6C*F>tPm8a;Raz0+l-RoG#J)`+Hsuel(1sbM6^$@1e1tLsB~aU7COdGO6)>+V5JZyp<;?kfIbsrBjNN-pxz!1wJq_za}DG}xF=>hl;~_*77qqK%#O04$DQ=g-Gc$Hy#HJ8jR5iz4(782kP7t?2V}t{_Df=Bl9~aSNr!ZeN|)?<LR;+?l`h`qV?wkAtdLLzP7@7A_XGu#DD0Q`NJS80gwObLq>c0=XY(G*O66=4^V0^724h6)NMOh3mgW1j2iql#RFQi?xyjAM5*b+GD(8Ic7|K67H}n5~N1A#gW8=5+Go5qPJ(eCH_$)c<{&{JT(b#m7zK#+rzRgi@Do5SF6GvUdjVDAw4o`}Lh@-w``rcHI`V+b!?W7B09Che|ToBZi%dFfBq(Le>J<~h;Oc$i*tnVv9JvT2F1&Qa1AlqQ7z}`)|ARh-=_Pbx7dfILBW}VJl$ZqpDGZw_B1VXAB;uV1qkA2nzFpo2Ud8~;Tb1tzD7%{^Qy^tCCDRKHBYfF+7KId{agbGj0r%5ctDhlysKGR}!s%URYAwg`HYt&BOD3Tc(VUcK?^eko=N&cMO*;aOEekr^28-R@b1@|L{QR!blfI^6j_I@UQ9j1Crx%t{%$_f7l*3P>-q)cjhnexXg%yd)+N~W_5R0N6bBVE`_G~Wkpx4)F_$$emshOiaOA~oQy-je)udc>9AlgOFalIh5TD*sOS1vQ6Q6Rs7NeGznGkWmczQaEhMbcT+pR`M(lA@^ydo77VfyYu#zdr3blFLMojrpsDo-|K{=eAJ^ys&LS(mxM_S|J6I>yZEdQ>dF0`-T&kj8F@R3C$s}s3A=x}?+C+7T{F3?+if5Gommz*PdVFMNoCRM0G8=CyjIvTGr+7Ri=8ag>prB!uu<%j^)+yN@T%J_t<ps~six5m4oNlR2vQwTg3NV+t*e=&Hjf!3)Pp6`{1%`MuN~z^8sk`H0waN1C%D4mfa~-EyQ$?HX+;QjoAFua_ms{{6v}85%bk*7V}74`{ClZ+60gngOMr7nCN2YI45YgC#=g~U+#B&IoD$=&2iHyW1dK5Os8t5|Gi6c?Wf${PE<d6^nRaB9qi(`^5%_P-#>)}ggZm@c6x?p4;ep|_ocaSLvP)*1-K%osZQ%9*U#slq8ZOl3j(T))rCr7W1G1*U5H9JxvCa;jNrH>R5MC$A%)4#23V)NZ!y4Qee@It$;Rh!aiw_K>Tc+dif9FYx0{a6nncN;s2gwDGC1LcOUsJDHuyV}A9ZqHK-A|Nv9nrbUq!yukvyE7ExQGN1A6D3xx5hL?+RM6|-%!m2zkh+7v)oTBQ}K05-{F1mzq!AP`@O48;QY_v<TjvVVuB;AC4?Lcapjk9dtdIuFR-ZyV#+0#C4N!9O%BFuLn*zA`;W3cUK>^}Blxnk9r3n9l`~f#uqY{O8@vbtnAfOTuqst94fWeYRu7ue|3P~=U&RxHN%(}ipWmum0$wPq8|4nq6tARf33Z$$hk+vm5-2<ue-s|0Eqdb4iMKo=80>CK#;oB2Y}dS;-fPKtMe7Ij9ETOx=kj&>1J`qecRy%+oTU#flms!Ow~D<?Pw%Wk%TB)*Wt1vH>rx+KKTvM;l9+6$vAN;+XZXc%Nk^SeYde?jWOxE$>00d;pzX<P#4IIiuSbb==I9);txGn4Ss0S@3y<HAtO}~o_Y?^i3s#E%EfX7ztv~x`;wgz)K2nOG@LVZYkDLn!E*6aW%Pz>phKTtJ631iR7T14Ra#tvwTrj@K^UjhvWdS?5T{}s4X^^%JoClI@`zi;#jP8I0@rHEQo;!|uRWo-(Qp46g(R=d`$#kSJj}H}SjZiNUZt9)#w&(T%*=KHWsacN2TFo<;ON){`Y`(kEY(=CTwl_Ao-Rsur%utBibn*v<D&bFVos1nkFa4R=^eB3BCDH8sS(X_k=m%0KMgyK6sjizWIS0wDud0p7+DrUv=KbLpeYErbnvPaYC>n24tA=lZ$r2`JYg$vt1R}46w3g92&~~g<@i1ufFjNMb_cDMoyAb7c8KD-spUP+zSJvgTg8yN3D3CRJYW7cQt0-!qYKC33MWtU<$3F-^ZSm(Xxj!1yHkJ^QzKtjgJjE+gwR=_+U-=|i%<}kmu`cuG<5uUfEKi(bj<0`Y;SOmc!wQm5^vIHIFR%v7C(-o0FjY~*U|Pw6Jh1kd@58v)5SQ@Lvgg>Ha8C?$0U;iwT$z|p+Fq5j!Yz{R^(7y*T*m6$)jTotXpnR~QZttC8mQ-m{PASTZg*dyL%}4PPPD#}2%a1O@hJ}~zT@U-9wOy>V!rdT|3DUSk94IwsDunsdib@H@-#c2zm2FgeCE^Er!v@yoPBRU*MsXjWIcJn@&VZhx-OxMs|4iHP7rO(EuxjmqJav|Q4+&?7M+ZsnAPc#HXvG=qX;$;X28-&UYQh8kHoWs&l7^tUeXA=pg<r;u=4m9%wj`RL%=}K5X#T)_=4{+v~%5OA$E&1(X#Nl@PGVhE+tX=R@m&a#i1ko6lwc-_JlvbOd<*Ld~{5x|Kh1f?KKZ>E4PDS^(LqUlx33DAG2Le2+*F-HgvtBVg#=ey))LSuKTU+$no>HK2$kl)M&mY2LFUi^Hn8ys8wHAf;X||8}#EdC3r}+baPr~XHsc5HQ=#>Txd5prrj);7E^1vCIGMH<BD2K|3dZmSRG@Y)Jz);M>h(#ECkco<TbG3-O|M_R2RGBbA(PcPCsth!v6>%rtF)4U`o*Wfyw#-7G!m*Ldc|Pv5kia`W<X~xY0>XQqGNUpSknH;Ev%&($XgjH>u$(d*3wX0kUG9J=74*PP4fMZ3hp%2MH!R|1gH0M&7O=wWw~{d!wX8VONBk_JkYqfzv!tGm^Di&#Eop4x-Qhge;IwfZ!^sW0hgh3UpDb(7*6KITT}9JX=m-$Fc~p7!4u__s3!H0SCdxO?72w%|OhrEzY4+(1G@d87ODs9wAwj5N)A_KbYo7Ox6%a;z^atRtu9B3vG*k(b@n%|1!lLvc)0%WHH72DsG2Gc+oj3_vdIp=+89mN=$EhUtUJtPV5wS<w$cGgJhE0NC8I=!YZIGP4C#VEJ}GM`Un!jVJbWJ2!J!}sab)(=e`*#I|OFHaWFjAOsL(JxM{7T@<F@uf`e4G!$Wz^<E6_WQZZN;txDoWThAmB9nWd)2HuD9?|(S))G?S}ZQN~}W!LUZRq%2jLGk^0Fb~lr+)%J`R+v_idhYK*d@9$4VQSw2d@(Bxt0rCrPmm9_jFtihq?xqD7EKDp1%d~fskfqH^ya!4<}9#3?d%avQ)!Crp<3&ChIjXjcE82;^{uFm0^k_Z2UZ0X(%Tn=^p9SNPXEe_(12xHeZSl^)Zi+YdX2j2AW+)9b;fM`ERf;NB}TMt+UGqs;RA)(Rxlomd51})3Rt$nA4^q3cvuB)E``4c=tt3`YT(xG!D~*T_Nc4)GqvWIU*Yy1)JE9?DmQRmluQv7c7R&kT8Rl4osE+AS9sYSUL#Lj{5+`dz*UFlWO%ld1c&x4-}>=_=dHd1JTDV(gb;m(&?6&Z4$?~%q?eum>2bXqae7U~>Gc(-=ZVu3=wCR!IO6o03y@xN7`YdM^uoI%^deOsiO@^5Si{kT$|LkK{M;Os7Yve@8{+Xodb0|<5r!9u!9(%!HuSC`?ygBcEN{>5^&D}hxQsKeaJ%)3v37LDX-9}%GJM_Yn}e_WjgRSz1+>#km6&emNVBy>iPQ6~5KSBNOp~{xepg#%n39`zL!&rYJ5!BrM~N^l(54SIu9e&eRd0~7p2mFIU*7~Zw_3J);$l?Uby8o_FHp59FS>Jc4W>|bQ)lW+K$iMRrZRJV93Z_ERFR$QE=`bw9@1oIx=ZahL3im-e&Zaxm#Vu<@9w9KyO*xr{0O1k8@YC`&Mdn}ziydzW3QB7nN2soMS1o_k8UR~gfd}Sk(;H?DwfloTL}(+?qOqu0?P1<A8>S69NLx&pyQy1X+&ck(O5@Reb&6U;k@F5p5_o(YuO|wFWir4I5DBain(luXFHQ+r}{DN&l_%V9_S-b);^+nyh=tgK9`kjQwKGVwmuu~WvlV|>cqubol!5ODK=<LH1Bf+mw)LSG{((*fNzg(Fg49Ou3^|NhI2NSn3~C^Cg){?NvXbhH;tbL4{cF=*2$*hX+9ml@BT~oLT_@MW6IxhWocnDmDW2qnwuh_2S%BOtqq%WOjG%+ze8GuRY%R7^3uEspS7s+tB`c(5_u|g=B77y6WI|<#^~z=yjS~N`?SnPWK<&oDa(3%L0MEH^9m{dS<~IhX>gy7)_f$)x?G`ZVXjTx+Ccsp4%0r{hlaDCLDI9x;Lx^X37l`AUMAG7jgKtD)zL5S`gZWfm>R!SX8?t2F7D&_(T(AH_yW}yy(!2!^kMA_@*n(Xj#5E2Ms#BSN5goYG*NfLRW$ktN{&CG=oeo9QSFh^vwNgRT5fNVDL1dEKK=^#<(<sa_wX)6rKB8tXPvdZwmkwI@DcIWO<%Y}32Cq0$b+?qR@%<9AT0>mz#R)JqW9?B9`Hz6PJ-WA38|a97uI_yVc=0^sgoZpMG5{+hym@#kSv!|AJ}_RB|S4Q#)FQO?Fdjy><kAOSo=?Vlxa~DDv$hkW#opRMWTtB{lFXPo_UsVrY;>gkT#a(b}F$4n)R6L=#jJF5Ib3%djupw@*02%a__`BX?PRi-!UZf?=uW>*LwK%aGOq1SR<(`QNn{|Lf)yb=u$ONLKOh!LD+22KM3CsAgwiWv4p&z*>Lnyfvu%$7+r6?nn9JryCsw+1eIY@?+krcZVwu1(`6|(t7tq0I*A0i8&UUHUrh$h#KKV3muS4!Q+?N~bv~!*OQMr-WF4yY)(j?yz=X^zC)(RSEs799tM*9%Kx8Bx5Q4IvZ4!w-^X*CXK|8otiq~u@z3$Z)rT#%z*Gu+e%eUNBT4(d8ZGC#}OAa`E`Sfk(y94+YS6c67QTp6*<?s(}=+@Lag~)r^n>)qY?oRo-0C+gx6|TRwa*kmGH!v&~2^vNa8~i?Ns~98{nMq|J+D%wt8dXU(d`s<RVV*d0<!0D*K@FhDqO6fs2tip#EFW=g*Vb2EN?)50xPe)qD!=x;8s+O82&)TB+gA77p*K>@wtCZwD&oktR9%8&C^CK(1cx8^7p`*al-Iln1N(2hXK>;<<vW-IuK)&A4LTXpD1a#94W%sH7k*u7!YQ1G3M{SDX8uzv&q()Won28VfQDAaOtR}bj)~<<uNW%{71fFKA)AL?A@p~HI7IY+2w61L&^2K^l(+p3F%oV%JNeH?E|PJ!9EG~>nO*4Oi`cSke@Y4zm_0wf*G$!`mEQP>_lw`_NY+m@tb(Xnvp2?RJoSjLKda_Iunk?VD{zI}jNd(s{_KW-P-ARV_o(l>_&0u*4W=KDul=W%>)ExQuKP4l$r;oO+n&~s(b_M*SABh|*vN*vP<`}tN;Tc6*L^zk<tZs7jk9q)elQr3`SY@ETQ4)seXG<-J+iwt0V;m3yyx?O`YrN^BW|^RPos9NgBv2Kyx+f4DIEaP5-Xvc?fvJEILERn1Je759!B|k!vpSylLI$798mn*vm=6<`4PLY@|NKhD$^`W1wa?PDdG04izWh8ky!0;oaU9^%Qu5rLvxRHekhCGLpd^vUt<jS#8;J#^s|wCaCz_FaCh@&<=?QRB7aBwslYDmgREfJczwyW-@sFb#gP`H{02KGUzXdF%f0bu|LFO^b^#)PZ@7iwq9D#!`qh>n-DsT;s;OpT?Rvf*i~nYElBfs?P2~*BCx17r9zF7iO%%yDbZSERnf5kmkf;cz$#^d6vslb*`DJk{ko#_w-a0QkR-4}-#+jB%2U|V=CRrE!!1KgwSa8|#jc+(L-=G(6=V{1EN8S?*x%C3nT;32|?<-i%cpxCppyl@lJvcAVl{cJvZ|V*3MvE+VaRNGeZE);->^s^A#d?Nsh*b2>VE(Yk+u5?)GT9wFD~a`^CB|Qc-;dc=S^x5j+A8H6-<Oq_g@JNP_kKr`VfiHsTZrbTUy}os5}M*&hs_PMVfCBw-WBC^%B0?abLgd|!|n)QNpc>ZqFIF6mBAUgqU64h*r6f^EqRdeIIWr-%;EDLT^*Pms@_nJc3i2CE*WoPxi;Z@iO!}zuF8C0;qCH764a^8-p7-pO?mksFH~MMktLi{FLk4P)8t`#ilPC<B5<8`RS|&&SCwl=2)jE^IH?KUNO)&)K`b!k7X~IZPG+&m?(_a;c*=JcoAPt9>2N(Z)eh|xo7g&fS$G=G!_!4<;`ZbsJe8o$JAWCTwzKdw$dN5pVjKgL7tZuXY+5a2)27BIIlYd7$+OS#bYMEk5-!;%k}goTVAw{l^crG|Yk0y?w8GC*^rOr#1ST%Xy=v7APnoZ8>!++4P%x1<HOF{1Jk4TLzdN^GI-L>eIuGY77PHfNR3fOy+uHUu1g7pUy+vU9%=QswZ_r0XrG`cpB_!Q#7_j8swc%#2@rJJ?D<{&Vre#RV<SJ>qs3t0~8C|$Dh)u<TvNKr1&7(MI>Nf$;f~w)3M9n?f7{=Hwuiu9U7_B12+<{mW4!wfBZ-VZsFv@$SP52qu`uHK@mD}DvWpKv5976cA9QIhxM--Z}uVKBzpoV_@sdiW_myf+3Ggb)|%c&?_-b=%RT0p693<gjJ#`9qp4H7pSip6#N$6vZxLw97hU#pTpxo*D7>Vn#Ys&hJ*a?LkT+sh(1IdQ9jZ5RZeGVBKn%t*AY9<e>voxjtnPWc|5KgA;OS>#6G79|G)IRdIRAn1p_X5C}q%XT2;I<S2uHwM=0fZ2#~suzyC484A)H#pmKMQf9)XV=)rk>4?^MAj`6U#x@ks7bj>GDxZA{1zR8Kz^O8RPk6}8LBIKv`WXgrK;OBROPk%(98U|$+G{OeMf12B^RdC;OoO|XTf)jZyA-QOiv|@uc@XLtg31xV?AbcrU%C%5<A#-J=4cc`@w0H@O9gZr?kz~0ubk8=&l@X3AVRgW*ncglTYIq*7|p-46=#vQRhRn&x-8&*4I$0D~yb$`6Q`?n`uZdcJbO#)&apg-~7_Mq<AHsKB{NqfZ{_415d3JW=8O<lSPUui%9sAmr+^hPGfk&$f6($^#QKbk$>Jfp;8D7w@Hjf&Ib6n8nw#~k%4mWh3y`o-hmt)e-hGrkn~SU>j&suJ+#1`b;M`(HSsJdVP<wo{leJY*|aj_G*chM34=m&lJq9$G!;K0Ws2yD=)__{o9I9>jT&bcaqus@x7}cV%gN<U_jY@rJv&icBkm>ghRjI-K36sx<&}qQvz9yxb+(Yn_Ha^0r=TAYI~(3Jpg5K2yt2}OC}W<zm=b9ZNK)`KadLI{k_jMK8R>pd@6Y$5DH*q5t4TLdjSNIc<8Wf%@BMBc?j<N<M4CXUAJq3kXT_-o`#486vg+4VXEr{L`7<Xy{*#~ScgkCcfLbNr@W|YA;Ve6i8@QM3u!z#zv82g%oKPjODBRMuK9z|Wj(d`}lC2Z_Uv+;4g}CNt>6`lKZGxV_0z8zJYs1{ZrREW(?}t0PdWq~#fcj4$+cv}vW2T;fC*%50Wd_zn%Qrg+mk^AI#*%&cLeza=MdMqXe@JM{d$%};CaR2Sfs4qOD7fusDSW{KHkzl&0}>Xg_L&IbO-`iP?@PLt5B^|QA?(qr3!j5IO$iJBxvjma5+T1&)>Ro*+b}rj<)910vL|kphDc=|aL={X5Fk#}IJPyDS)elEQR*p4Qmp>?);pF-gN4VS^+j#_|IfWc;pP#|7t4p)4t_7S8}25@oe`#*wn)OUVVm2%T?I!fAS&)ZvrD?NMG~R8Yz=Nza9C%X4Ah=4-!vj>Uf(6*3^#sJz6sCmk~CqrLhkg}3pWG1oF&4S-IIzn{k&LHUmuX}V;>Y=T&4-ZT)$B{I9iP+BS1Wje#IK`5eqcKFQ7B|bL2^d$=-CBcO!#acbx1GF1}``DN(+xf#tMuI2*s-E9P^p6PdSM<~25;D<QE~p^SRZs5<~^2t^QTdk7LQ;3e?Wd53vQdvk=Ofwr_#*b@A|Jks7_CT_JmFE6MV_<`7*%{E{)4%pN-QdlC{0`=dM-!Ng#+K+75BjXy-N+7u*ie6xbvcPo^^DHlXT{}v9_{U<h-<2zVG{QCRgX~8IhW^Fj<AjazxScKw$TQ(1&_=O44<E6;6+3EerCjyEsKL~vllAA-sFD4uUq+3~!b){pyb?9Uq9ryKD~Pv{k<LQ~jqh4kD{yTkE@bLfFAW(M4uJ6^s1FH(Nb{(A2($Hk;9z}k5LSgC2p`rN3-l~@U_CLX+&J${;x!UP^Z!44Z`NzemSzXdE@nim6|32Muf5N{=ia<GyK0;+SC$hjK)OGGcb*Xl5V8aYBfvBUT!pJ_z?KbisZ<n_k+5;YQz0JcEMb)qk_{3PAcSopOD;Fa4~92hKrqJ`-;8E8yE*6Fvu|eZ)X9BU8!KYQoZtMK@r@BwHV_LYjyz?50l8&8E?L+p|NjYQWm3H>N8TIN9tkuqS(cs`k}TCi&>%V;%jjLT7J>SYWnY^AX^IXWG%<rr%z+*5)o0GlSnv|gzyUMTczQ9;RIPd2n>CX%gfTSH0$SLhp1=l>_qwcADsLvyKZKHE7^2@sKy}at(HKby>=8e|B0qUr%On9jk0@gxZiTs(-DsGCvM0rZ^`0B$ma~57{2itXem9aVcc0C-+H`0TON_|hl0`s`L!Gx=B`DW`#wEy$OrXVD6xWk2(YVAF8mgG9a3C4(EsFJ@k>{#mC|o?zH8(hJcHtX|&0=MVY;hH9WP%8fO_kGeMjy~9WIV@`)!3w)@_S_fS!mbPvwbbU#J(2(;;ZK3tLEaXUft`{*Aadl;aAPYSIx!udKz8@7heSzUj-Lm1sC6I-o9!szG^PMjOOCkUT`tj*H>;XyEr|_?zpStRB+KR1Q)CR;xHBdtx_J67|T4fN5EAf-y%|HuWpVm7@nbH*H|!S*a=!EMZLxgkSDO+D8b0Q%Or_snuV-|&h;04{ro7uH@-4{(a*&8P`bLTt?2!+{Nd5jjt?Fd2S=iInA8gWOips~#d_D~7ji7?=x1N4T7#k*rEa22El2N)QZGU<3feIB;Vh&IXW#W2>cy}mJKOny_)!salwH&-51e+mc-s6&U}c-C=-T3J=dTz~v6L*A*D{|%XcF^_dl9B_4v*YB@6LXp>XGOYsx>ePy@l*zV75^LG-+%bvn~hwH>tJFgc!Y_^w<^xb!QdkMhU=hUL$a>(KtQmPF}ez&3N>d&lf*=MwRek&Bd9h<ca2D@cyEr-a|r?k7*@-@ONqdjwKt9&h~Nj!SK+<9=&@}x-X34e~XDUpHV&>$pkKx{~mquS!aIs15doa$KQ&_PcIzySi|y2%yK-AnXhw_iheP$Lg_8W<aCsL6-_)As;sClckyrix5%&mz9%*C97`v<d=JgP%sxM~247LLu=DN8w~cfSflg@xDYj_s+lcx~Y+TcVpKz<9VH!mcebb;!()Fm(mP0j=eBcr02c#rY7f9RNP{Obr8U1=FBc--VBzBIUBzF#|9;9LjroV(<0CZxNzYt>7F_W<b>#d=@UQU3z7pT+lix6C-z8v%p%j;X59%SzDBJf@@>71zwNm5sKmV#`*&0dm<We_^DcYg|)TxkF8cYuH8WF4xg&8#SB<44*f!1X-`qa6Q^Dvh}P1IZ>?3mZr|t=37%V-a-4c5%~hNH=V=Cjv~>w=&2E5p9i0r>kvj8+JyQ5$>aTX<K5#&=5M{*E1Q2HlboCHK&JQOj3jzNm4sV0E?8#foF@FX-97MBzg#YHxXnNlbW{44BmlVpdpIOga0zL*Mta=_7Kpq@-sJB25TT^ecVjT%Lfx<IM7+}8#i=>{QVDKUBNS2!P7TH9zL<)DR$}eHBaY1RM~U?q_QW*emJRlrdiFi<y-4+QSIDfn8#A*ah<c1za1{uId>;TPVc(i#lq%M*FqnGOY(Jx6|i6BO$O#KQQrLR?$2Oj&))}z1mL?jb#lFN@eN-Y-}=5AKpu?-#qu=1ad;p)X?vX!+ne!~(AL+1a(^?va{T&jSvl9n01xZ%>#sG}*P82Vz3TPp>j=M&@aqV_7F^%sX?TaPzt&t|Yp$;~*B_I*;A_G4wcz?%aQ)x~*Z91Gt6$b!simZvYpjyKNXfapW>2qE_b};8ndIu&tGOMBbPr>x&-t-r<&B{t+3Qi{y|e1q^jLKoW!1+bYnaM=V}VdFE^4$QrENy)0hiwL;H%@>+oS(X3sg3wJE^%Iojk<m>si(EtzMZ^LX4MoRJ`=dD^leWKk8>jY%EvrSM#!^y*U3stz^5|$RP8%I<8Njsjb%2v)b@Ud3E}Ft%*+Tl%C|BjT_7AAh+nOHRrU9I;&_dD#T>+ua9Sc7j@R@(!!#E8khCdaOUapUq9AqeDp@xHtKPPO-B}4E^rzaAKbjk<!k-&Y?0}xfO@vJhsyW*q*fYFUK#3xbo?OJGdcTodf=b&;7l<!EQ+Z|1+9m#{Y*tOJo3|zo|_8~R#Ip0njt!QjAJ(L^hzJ7`JMT|aZ&mFgL&O<s;$=7-K@3;xmrEwY$oVlkAIK;`PonS$Ij$T0kxjL!4amn!lT#zz-XKu!!r-!lTLMvv!;q^@6L|H>ErR~oM>c5w&DDo@Izb~N11w6>fUn4{E8aNi-BsvEwJbaWd-6(N_cH49Xz&@CwI~j+KB<@a!2UOubRg?LI;yXz1R`jfn#(Ptts?;M<`3GZ8Ba6P_U8J;axgH)2Q@->ZQo8)_C#pc2H70m)qkc7ro+wTc=q&XsEKOqNSaBK?B7TaXBl~Mz!5w))C5f&<@bD+6($9&(<WZRE~Kar!LTVvA^7U%4;hgG{vA<=?&rb(ON)<KZ0^~^25)7NFUd|7c*@YAeR(&ndzUUH*XxsrA@64|33MgGNlbF>0r|E6L-xU5_hlUOSS>h$1bkQppq{AC!pcuKdbnKOmVYJ-iOg;57iq18xvQ?XKjT*HKa(2l^K>k$7ZNhKdeK4*TsGL<W58|W%*)M55f3CqB!I!b}gRBZ%T_~L?hl<tzS&+`iH_l5m^zncsIT!X6}ZJPomlgVs>xPdOT2heT%+xlc>*?XUn*K5}mm512>QcC~w_!OB?oXjlTDk{~z}b2I~`GI&7vw?C=Q&t8;x^8mz1@QV4osutu9TGg!T}moFQvwO5<_Lk4SOJ=WbNgM}XVAVwJU>Yg=N4X`TgUng%*V_obQ4b~Ac;ApKnljR-A2PvYDAwH#fUBr{1(x0pq$i|k|Dj7Lehl5j$&KZ@q9;^)RgU{!=o$6_)+;i;IrrN2hQ`bL4f?;;bj8t!>bOLTamWBFfZPu5Q`mIkBh1{df{){L{nGyqG8!M9rjV&c+x0E)Q5@9*wwZUfwhzO7mW@mKgWj3vdQfU$>ECQiRG<lSV*h!2$q)`RDd|=>q326+dgGd_*{HLQZQimv?%%>p{l~dmBNEKOT4WJqn8UP3>i^2d%oV+6g2Faj&A8s>{7-3F@F{8aM=JTf9x3`!VpZ<&QKAd-T6hD(1&=W>(OXaBuW~maZUlFRh7{6$P*X_h*GaEc2h{|C*a>3B)z&h=qONyn^RH><96RJ!IhbQ1G7YCJeMu{}lVl?Xrof<?9p|4O>c}@ELRw9uD#`tE3-u_HAJU?cW69)L216-co-oKz*DKql0XSpCL>f~8oCMhbjGn<5u%=I-s38K_@b}@Z*F`Kh4W}p;jlr&2a9Vfg@pwEoE^IhD{R1J8ton`Y><|1!;WkhbZTv(CXGv<0SqqbY{k$6c67!yg9Lhj5B6)m;%_1Z@t)CglIVv>%F+zB4|RAQ1ex}@}{+DY)!n4ntT>)}D=&-R1{R+?rX&GPqq{}C9!&aNae>^!uLDqH&x&l-w#4W)NpL$i?W9oJ9;)7;k8BSb3jibrH%4@7Xbs%-VNTs<NQi{mfW2<{n+=1dSr%CzeD#U}{m=9d=AUH$7%iss5`d?Vd4nj4b;{Cfy9I_c8v<%xn;_s)km*3ZM-6?px^H^t-X{ijU#55cr?pfm$PsxY#rN_bKF4R07>g?3W<DuceIsJR$I%N@N-;pUp6ALT3@;Nm-r(L5D@m@YpU&uYiawd5So(IuF3ZQ}_PbcWvd8bUu?NwtuyjG1eOakKv^a1%FUd9PvGy;1tOGYz7)6Dx2cRTTb3ZUvpvm+KcZRgdSAo@1&$XfEjyBel#WDPVpcC!v-!>9)_BCx)5m1AMA^VwkoWZBw)q;w8hBFYM`=62Ie~o=*1kWWr0&kecXc7OG5Gf%7FbF`U>YYb0B$P2`tVoA~G5?~G|1Qy<e8SkS0@d<v;CNWR?@Q2%Z5?56LQ*KaG`I{Dkf9<88RcEp1_btseOz$Oh=3$M#x3e@dYbC&w!9rYL}FSDYyT)s9vVkyiGq?3cro42p4_IQvG-7SLwex0vCKsVp1k(0mZ!S1TBK+stasH--R{<Yk#gXAIKSYJ|BuIidp^C6o3yp>Xq%BR5amk%RU<*?)f`Z4kz9EKgX@|bVM>u!~z{5vhC`vh79kL!{(WX&%>w_V1^SKI~2NqU!|#}il7C1a1mz!uKD7OSaxOE9TdH<xwEtOcPQ8JWONqIag28%D*<ji57IuJA_AF6<84Bi7_WBR6E<<J_*K-*}C+N4EPCb)rG(x_thIJ}ygwn^9iuFsf%_E^G#5aFD^vBw+m~Kh((ekBwXlmfhLlg~iCh8ib3(7AlGB(Xgf2u!TBoEr+e!8olx@hi${FFT>V6XV|X2G5B5$&W5e^tM9r0>#Neg9z^hYUjKUAup^uba-bTI4~k!xwbGv`U-y+TJ6Ybf3I|mE>wXl!)~`rW+|)rSPD~cv>?Lp%oJn9eqXf2+63LpQpt_Kx$3=t(Et<kGi6%#Ch;>yOz|gCvh3!O!%<Xnk#P)MVY?CX~1_ssIzV1(1+3}?BmK$Hwd5O&Hri+c+%nmF#cp*zP06GgMlikXl0w`onU7K+eYN^?*O{k$>^2JT4lawR%=&56G(o9rnm#^5o=;jpvQkl`6lq<^lej>texP@?;={_Hj-m<^BO-V}ZS4nUdZsp}EN;~jjk*%|v8Q2}jlw3f3PzH=sJ4v&Sa_+dpNHT|<!OYr2E{y`9>sow>)`G>BJ=_q<zhmvQWy(`lIT%4a|4V;-E5XpFPU;rl8Zyce!CO8tNt4~=bxGYl3M?2Qr>B}HKR~^a&Y(q3t@ldNFxQO&bBe)oA0bqA2(J^!Tz?{4)f8g}(1-?-*u*JgsKun?B*`vVQ#|^~I(6teZljiGalr&1Tvf~qzIM|FU#opVpOl~=OVKLiMC-X9L(Ig$a+Ko;axZznh7`6`fp$`CsCpWF#e;J{q2W<7@}c=FW-)vC5YM)lWif9rSj;`!_l_)P8UF?r6B22DX*2_Sbj!b{8qJLQLzdB8@wcd%kd*E&FE(Z|p{-y(3{tw(cP>klt+^zu-*Q=Zb3@r7-Pkf6(V1oj?(9C9q3l#DqXuVAmj8{CR%A>-l~){O1w*N+9rTyZ{$v*Wxmk==y_9;u>xQkGLIX)tB#lHFl!}WpgBaL~DuY-)-zwUG@;nS;PoxaY9x+)n3gER1TNLYY4htUEbjti2c9r=T{P+|**?mNN_vPQ`pR6B_B55&#UCka)VihK@Ew4nd<>GaZ_D`xwpyQRzn?hhvzXB7pGeDvdT!2oy5#WyMS<!Yq>@=J#HSJ@jQxqS?Z7W0k_iJZt^%LmJ?kTP&>Dp95LLHS?8;)_-Tw<#*J#B&}si%#+xxPi<igF85387JQf@ucnxF$i)+$88jmm_m#@x@4MW_GO;GYRLrWJ8l=chvvv;%6xNhsI<{rN~hK`cZ*){xqgJ4FFZ<O(lc#TG^O-go>^72HcdOf*<X>batRuFKL^4@8*Iye9%-xT@$MEd75Kx44Y`M8$Ru;`^4-E{#{8soda7Acn}qktS8rX)yuP_o%N`P=#PYWCh;9R&qSbrF5JgB>GjxDG?t($%*2gZ*Jy$orrmR_6EueqnY7a=5@hnMHVzA!Bq;>JpY_#!4`?e_M!xpU&;Aa6RP~KjOEwOF+Wq^!`7I;_Xt@p;@P%Ni@LEhdm-JaGZuNL?MV~}B1_>^~gjqv$<1QB2L?1!DkZfyCY@#mzU$N*PqKVKDu)q#}NRf0{@r<GA9cF|(k&>P%r<4_5bJ`Y9W({GQ;xkgs*v(migbXJNw_MIj@i5i6Opg;WaNZ_-J%t&ql6~<G7!!UsL-$Y!<TkNBND=!$EV`^brYBRIFxFl8HY`4%uuY1@-AJ~P0`=wRuH{|W*E_sY{3|*55&P?&M#aa<(Zd(J)O0S%=g})0BMj1>LGid4)~0gPRP1QxAUDB~jrlLTr|Vv0UZmm3G-HJ&NMvk~S<4;72F(!jCo*fE%4H>J7}Lj5ydWJsCj7Dtr4k&ntp*8($;0x-L0HEH7rIHWA|V@m)!WwEGeZ_B27b?lifl}vc};a)B}qtBi>WsM$tIqF+zr(m%{8X1#dN4t#k%5X0Zn4rtRy);{M_2kB+w*WYR0IO$vZlxuNHIs_1R%9{^18Ity5%G5PD3V&d^liY__7@t*wHyEKGo^AeDN-z;(`nY4kJ`B-2)*n6|6Oi3YJ64PrD!G}|ZS73oxc)l4fBXaJxq-j}ictM3);Kj6B;d#$c(OQ}|Q3q7<!w)_g_$Wgp6zcpjpA>NnYTJ8{R(k$Ljco73_GIsPaQVsSag-uu>>RN?H<~AfvbE&YoDt+7q>S&q|o8`cA7u!^63@dy{!8TVhE8-1#JJ}mkH^fe0v+Bmm{h%(><w(D}w6|t2yykoHPdg??2H9w&$U|Js!+Df)Gr&!f#|Yb*GHB+8PN5Z*hl}yN9LQtGK#E3{t_i&e!L*O(y{13xewEwe2HRqrOlbm!c;$f{8yImnDSxB*7;aekVMSG|1n!@5)sT>*FWJ-lHV64-vi6)c<we*^_-}y2IY}PM>^j92&7L(STYGAH!t3S8X-hTws7Mpuarw%9*_*O!2HXRNndw?7<K$HlNZR!zuEmonj_KR-t-HwHC7X|B3n()^Y)u&y8z!A8RHY75?&O{lkiTmM?5FeEQGyJ+T3HkwdzZ!@3Yk6BwMxwABuds&uh?Hxh7)tToV-igqoWCx=p3vU=1K`3TrbjT|EC#_Ez=aAo`Q|4)fn+cf#|GaHFn(fnuXP{4G{rvRQ-Aic=1JDN9dST*LO1m(ybqZU#3`C|HBdDOw)M9kPgXOzP00gsTm9H4l9O=tKdx~OakkYL<M^fOj1XmYZOc`p|6nJ%<%-tND~j{G%3o*+O7&0M_BZIbS;jL<ZCAq$a?lk8#OiWI_`BFdjC8_fm~`_%)fbNJM_D-9p(HtxU`k8vW>VX2ESalJ02}ru;V0u*BOlyMv|vTCzNW*iOm6d<+Tty5c1H@Rx+Qy!MgAjfpWy>ljeLrb+;;kWuoW28$+xrT9RHUMd<(Jv=4rMb`z{SU|aV-N{^?j2h%p|WtN-3<n@I_H*YLF(aikVieXXjiG=IxgdKC;U{bYoo;OE>6P9})rd3xW=y{@>pJb*^ZGQ6k%8g|rgjI)%y0#Q|qW_yLHmAF1JDm>OiL#X0PaPRjz5)10!CO7kGb?6jQp0KEgy=5Q#BQvg=c~){RuZs;z+xjGXI&-&Jeo$9s0Cw|z7jO)lI>;K;>*t1(?$!=M5nyl(3Uj@Ah<3+@J~ELIQ1>`GW&aMI<hSBrUp&XCMe2~hjP<E%cNZzj?yiSl*2C2+?BViF|gQzdpZmK!HjcHvtO3)E+XnFfx~bxRx-$&uB8JVu3-=f71-d14g{5B^WT6@ZQzPUNOctwdnxTLB=ax@Kzi4>-Ide6kT%eJ%mhnkW*RcI^VC1MTpoYNJxlv}&&P?68zz!^W|6jTOtpsSrsNSP5EAp*0*a;!-3=(nxS}}2T9cwpR5em?)-g!I7&D5I%4X(DP(>$mYfI$y8#7IyT+`9iH<V<!aJ0l^PpmnbBVph<J>!Z;-jDevqbI9DgjeaP_DfU`9JSq8L!M;b`;-qF6BdjzC}my!g(~D(gC;lqv!b>e1)fuNa~kng2Fr-z!=c6<@_?%VGl67PQ@I8gmTVX!9h1m*HQ?fdDPzJDp5h?OB_(pnP0Gq~%KJ>}%gClz@X!?R*ss)NmeTqBx<+{R>yqx4%dVD>Jx__*`uKDIog2jgAMsOWPRalW^nz_a_D~|T2=Gm^CfCd>na4Hej4VA7mUAW_gbv6~>zw)KIh4AiMMXOii8^uL8cW8von+o6=LbWc7|8S%#h|X&`3j|O<YGj<!i)megeXH1p|k)asP#893A>`5f-8|F8t=yxB^=3g&Vzu~Au=O~DkAqA9>1aMbjyQG`Sn%{5n7?6`>>w74>K&De`ze9|3&x5CYzYv6vwFA#J8MH#Wog0`5m9W#i5aQH>0p}lH26a7uRFp2l?ntC}zG{n~JBWj$)&D5$eT>BW$VSMp*_&aC>lXTzJz#;1k;>8AKZ;yQ|7>P6@1(T$6X5+msJei_$!Z1_eNp3^)mMmizpM_M&_M|82qHh|Z@JNWzVi5l*g5%v(0Fw6ZS@eltotNP`(QK|%v|?5#0Ru)utcU%Amw3~pZ)gVP?WrOHD!(b~5K>u(Z^a!IjCdFqD2QJOk@<9~eLEJn+J8GC#5ry&X8MxAPKYpioL32^7s%1=p)9I!%^3fR{<gu2eTg9WOTGkGCwPv{1f-b}{cif&d)iMn0DgV2Hy0SE8BQzRd(eLu5UJk{VR{98h`je4~=HLPgxU2idku_Mfq6!!PH+?G6mf#e)eC~?PJ!vcsv5`!`yubr9w7Tm!&QDA)n9FxFFBrqIw;P)kJ2#S4rd387&d^%&zPbMH?Mzegz@S$7bCt5ct9KOur|Al9F*>pe;EOrx-|IRj)yqc%Ta4%N5eli<vR+@H`n6GF1h)2y4k!WNT8x_K$_RG>PqXX{s&6M>*gH#T+B}a<%u7<5M9MYgTwH&9PwvQ6S3Gs=FXqlU<keH+IX`B&>0tOW+FRlpB?S*h6P6jvXx^AO);g)zX?FDf?dG)BT?s<EYDZt`}-*T?~@`Jnjxh)->zZY%-?nAu^$}Dtt6VBt38kPWhB}4@J;?-;jqhp>@h!~|R$7})^gqvk+6mJDg16N>Y`Uw#~RAOv|V$-eA2z3>{s|_JyrCG6AH**cvYtI6ym)Zf*jm(g;Ilu4N{G^nTtAHI#Pb%LD|GQT%j7~UKSHtPKFSo1i+XDjrT;-Y9NH8M&D(AMF)@Lv(m01Lq{_H#WWU(9lUS?Yktg8@+=U2oX(xD}>4->dtQE*{s!d5y9kbR5i2Zp6p%`%$%;u`?P8rCxzwIIV&ZrHj!++vQ_3Lfrxqf|x{8ktaQ9weD>#E^R|KMY+~;hSlqXxznOmLZi3!Xmyxq2ivK=Y}yKAmA*bDKu!Ej=(C6VkMUGHk`pN!7@?ngp~qCH_TH9W%W2yfaVX1Vvt_2XgMUyvm$lQHh@U-iZTJ$xcM>f;KTKF;BRZS4Ss|W^Nh1#i3G|F)&k!FK3R4FgZm<D@Q3W?m*ai$eodbPRnX%(``Oy^E{i8&Nnfy>$U!l?Vs+^tSm(@yvM$T4Th|zpiK~~ccycSIS<=|s*vK0Pl)rOlmu_ulY@@J$9j8pMUx_lLhFOo17NpFGj?Sf5(Ke0(BKo%>4j!iqCm#8k^$L2(*L9(y$7N<$;a4A=^?I>X+0dgdruBxmDE*ox;kSUcMg^s7hJy0bDyIx4&0WfC-*lt43A4~hP`iQ7V)F_7Cnky#wm~L9nZ%BMPd^~l+NknNNT*<~Y@O2bL8a}1TN6_E*R`>OHE3oZ_?GTf$NF_rLKa_Cf+exhlToNAaTzGfy;3VYtY=TVuRo{C&$SX!d-Cy{ZGsbn<moO7{Fz<FvhZkkv@+!@120GEDq6I%>2dpw2#Jyo>xe05!MYe&y|N|Mdo-FRoLiarUid1^2|Nu>WptmJM3U13%W|c1O$8ncs`anBKjnuXxchtGT_a~3KZ)rcofBA(Z?KNAz?fWPE=AOC+_m1|lvk=t5rGdx{S6ZA*!SSLrR$D`Kx3S;5i0jkPr+%=ttPW8VyM8aV!ZMukl+do>DT<?wtVp#BhgqY1Fv9&I#^*g{y0el4E&YV!CDF6Fa@jLbOQ<<f_N4GP!I`a8kG;}jM$85|C?xisAKC%83ttUrbK6aLvnkLagc|3ZQBhSZen|l8KGVS%-P?35fF8kC}{A0IO<(*X`wDX0-|oLvgwsxPUk?>+OiOr2tm!H@dF@g*|$bva1=#a4OS|tfl?NY9)yYZOR-CHrmkAy(}9z2iJfkRohF84j-6gr>~welI}PtP+|0Un+8Jtkp33OXr84r@AeE8+!joJvo1`;$`ZT5q3txK5kjW^RQ|+59?Kdo^d^S%;A(zxm_5VC*b@@2@)%0U`VxWtRauRJyb*(Y)%6^;Yc`^%q+77q3jaI?H+??`c)ZQq!E5$r!%Q9s=#)hRaRfZZ1p!a#!Wmb%}rOF5%7lOZSOZ20N*CbI|^)_~8Bfzw3lmu_R<UnpaE8rtBwmy>>Tg_*a$5>r8XatL#O5ICMr9b;_nO1lf#r)ErS7S|a=6Ytxk-!J)3U7s;-35$cf^j*j=?L(@;0!$MnK|=t3K_MkA;tr_N{kci&=|3$jT06?E<K5%Sm*DEi%&J@ALXJIH_JRQc=g;)Qt*|6QBWVeLOddVyo3@R5!5XYl2`-T8VbO*%F-mG2`%Tg(Y468XDrw%DKzml5>A73PcV`+SNqFSxaO20h6{F3h`)vjoOSO|F=_x(E3dB)UTwXK;fF->!VbAfH6_TO$2POUgdGyR%y#tZ_i%*Qz(s2_jqz{)uxxq2WHgs|y>6M1yS(dhHo*;@?|R6QVnaLG_-4BvI*$Ef*K4eG$jgZoH|V+6p$SK%z0cltl~$$heevP$A+=SiARBG_>t@>@yzO9JXC#YNxBYDUV^<lsKTOr@*$%jl&&cFQdXz7j%=_0S&-kjMQto3{o#S+ms7SoW155synAj2(2RQRlrN=k)gNHW+R=VmIm#KY?!FcPy0jIvgH36-%GWjY13a8Shn}Q2cR9LOMOzjn8itd_)-CFQdDE8fQCRc73m8BuvmmYJw2`V4aMi~HYC<kF@J>%V)*sH&bbH3uWahDul-_w=1O`K88Zv1??<ZG1}X?J7A1-wCuu2ntyhNh4R6&OUqxWYg3qze43FY{P7?S=u9xFU<0=#jwhwOm)IZ*;(a#jf|MH^|_Q1J5i6dMJyT*hXg5uLEnua2$3eM7+XMx3@5-8N+9jUqT$I4+OU_<_I@1-1wTl%$P)1OzgE>b!8-aqQkl!Y}|DYs-AQk%%;1Q8@6#cR2ENWJaJEc;h}cwH(rfk={p)T-TN5sW4fu?I$3b`D62VKZ*>i?;I7U&?>=Qhn9NyexFeK7x0(IWjNuq&2TcXR-C}n)B0y{^;OB0b1|#yj#HXLtkUrmzKW7thTdv~Z25YT0jEXGkfio%Is##pGmrJ%$)FQ!NaEnM-5N2XB!r-U1;Vt@&`4a-y%O-g}X^6#8%jN+y6)~dqdDoh=BF=yOsdMyu#HfD4{LKNxJ0&(8Zrz|o%J8LZZgDM|g%aY&d}j+vK(W0O{D*7P!UBv<N8e&!2LNBh$_n@N^fF((5<)AoKaoWsQqLfPTn3Y6XCm!s(CUW9UPZxO1tw&Ma#%a`z;6QkLF73hx0u-(g}qlz>}ZTvj+I9%Lxqf9)A{_9Y~(Ly?}k;v8-w{WOI{*o{6n5W@cb<!^p0IFpx$uGWGg~Xt19t!Z}+v66X=mm$Sa#tU0EbigBRGp3KuR9<s1;?tz>sMSnLP23;~nCD@z7};uzGT#jQCC8`?5a_u=HDl7NEnMDC&53b2aH3FbRY?mO`(IiO!M#vItKds;#CBHWb?gSB2>J{-u*u8WMCgL;O;&b-zp$gzM+mNQX8+M82sI<V@%;cWSHyC}37tcPA1tWhU5F<FmL41e>hLVBNVQbfNggT2NZNGCt7NihH~8|HnAGTvjKqMC`)*s8efQ>4qAtDQMcN<e@Sj#+Dv%tg0i%g~OHHqTOrxo32rqID8kPq*x3sDz*FZVTcHB^EB8Nk=pbmyFwgIBw`x8-r&BRcUR;AAV|Kq&J`z##vs%Fz~5oV=Zyu!wg)3x_)bU2_Vv*ke7%ro|pJ}_p9JuYt*%UZxn6u8tnnsvcMafuX`-H`x}|lDBOJ3B0PYVw%Hp6eN>hDAnKT6^_gWgABnz7*_em$+2C%6&_`MvfhgF_dENOE0e;qDFj)IRP*ma&$+vej7JGspK3O^48`x(iI-z;We7~TSDyVg&%e_|%V@GlnM?TUN_MPi0>Wkn5S~nm!kVz24g0Nt!$MXn7!gjqSV@!~*L&D))0TuY&*2=cMBfxHFS{`ce(>w~XY7qSSS5?VZRmoSqxYwtzBm6qTuOs}bD*5hD!>gp^tEA))z3kzup5&{Z<g1?KkC&b#(mh{yNl9N{Pm^?{^CvQrm&7E)LP@d;OYV&5N7N>4Nl2ZDVZ8N-HGGOz&+JCHsYv4z>zC}37x@mUqtv#7Q5G4{ObgNLSH?n9&DprQuA`I>!%~k?$;VSQ$Xdu^?yr6TwTGoFWC-pZUOAFjbh8ft8xq|7oR2PNel3d&$>%P_*9-CWLNsDKv4TX=1(|e_H!7&PLgV6TFeOhr)lC)loYfWW4EuW3G%`BLN#3)HPuhpQtABYK^~|HMLov=Jb?^1ele6P*ajMglu*<n{Ez_@5g+`+~@W;b$pLF?HO4QCd=uGA#QxERVCWJ8l=-9yM*lXyL@UXs?a3?t_(yvU9U8*7z615v;?nWKIvm%Y7{-Hk+qO4+!b^@b<;#pb6i;9a!(vjWex58s@ofjk=wE@+L`k<uYWm(AQoynu$8aI^1>qOCB5SDbyyAzfdQYZQH19>qlNAFI0lEED-OvXtvaV|I+W^$2k_O0OE`9q!4`E(cLKqtLWUpLTbt;EOo(LZ>Er@xz?`Q6!>AARiT^8HMI(iY}&SWXA(%qxpiI_U&o_J)Tl%CszF{0a9fei#cF#RA-_L74D2K%P-|vx;(`SU4p-0W4^QW52OJC3Ge22nX@8CFB(!yK*B!8LzA=K6V{es+-@S)RCteJ^9sGJMCJOiF(^}*w){YjI$9fH48ngKTGyXx&m!rowh;2t~Js`qKUwZO=c0i?nDxoD=lztqyvb4hSZ9p&XKc`tc{+KG_<0)B(9%Sxn+ZE`EDQv(2qV#IQ3%0;)vp>niCq%VI#-N1a8O5hDBC^q&iF!RUb@#WaKhm$ck|RoD!4zq1ESHvQB!H7i0SMcfmd$j(Kpbrn<vbPZ-*HOB$UWi9s0OO*kUEnRT~Z8^KK?F>ZG10;{bp1F3DSHIU8a1D>)I&4_HEN^wMCL$>p&t$d6AsEM{FN>Fd=DW3tcslu>lZ_P+dBc8f6W1<n`1M5@PM@}ugmSl!q&#LAg-#_A-iDxRAFIvF-lM7G;*FbZH36fTr7w8f9K!uP8vCP*9<e-Z^>h{7l0TGcqB2-2c1P_JvBi=uOT9SuaU;`*=6Ku8PM>~(hMmAq0OO)LcGY}eSPXP~P%hjo;+Z!Vz`%!8`2kv|synJh9_GO?y7oY;A&eUWntKn$Ca<HGbnQ%6y>w3e6o`JlAgg(S*bc$@gpqCYs5gA0IA9PCY0SrOTDs`xmvWrLw1^E21H{hyN<qV%fh=nh<wPV9wlkK<4$5uN)hyrM5tt2a*7`9rGGz_3&2z}SyLyb0he89};RylS$`Tx-U2fq0kV@?vcM@x&*mdU=K`lh1T**Z*aze;6afTh}DjC-O-nt;lGzK$dpgB2AMH<`C^Ub5s~W!fv_U(A!+tM(_rUev^6Y#-6^ai9y|QT_<j=WbWqnWFlm8ta(amWw|4&SWdB5v!{`PH#zaLEz}r7KO$q>i*PDAVr6Kod6#{2-GEVPl~Zbb+miYi;tWVu=dyCJH$T`9TTBu)QN%wWJ08kiAf!Cfh?%(qek^z9cc0muN4yn;lxQuE4_K3qJ&p7Y6i{It@RRhfb&#Ng!0xenRzck?N7b8P-VHC_4%IfZtD3CoGeFeizdJ*AX`sSo7%is8NDrIQk%b_c2sF7#f(VPuv#CrEz*FWYyQ?U!@?Mw7dxN`cIx~FL8~=?XCl#oquL@e?b6t-NYH{2%2@L^X4xHJl={|b^Y?n${GA9x^}gbA|J=Lmx7VcFJ-sJeFSN~hRu@vIZPVC+&!)pmlrC4gA+=AXQo7idyRt18v<>5~yW*}J4J6A}mDsYayq#~n=vkR<yrV8=*{eh4b7_}*Z(KG(?ME6H>2g^Tpl-kB_H<!M<HC=nzEZ&TLF7`!LWmb#jeFUj$f&7xtenGI?7yH!?_L&E^p{>CEw7N4*JAbS)7KGx9pTpzeucEWLRwxSEk9nqnSVvKyrNoOQ7x~imLCCB%lO@=09*KAzl5{|;}}+nE%2^1;+jU^ZKS$e^p#l+8G0X1(JRc6&e1EuKNr9<!%fWoO?|12VM9py#wO1R$5HVMCqR`4o`&R(a4U24hhQwe0y=^}LQmMdGSGy|<D4hsMcFtccY>NRWQV{kF3y21{H+Pt5{R3KRy?1<Ky27G=3xnMnO}nO2)X&S>ssuJMkLE1D&t!3onJ+mUxgEz;~3$>3aqd>$ob)HlgNu^ljIoN!gTuCYnj1Y>g5pbF=9QA@B1-c>FnH?E_{h_sR*4q&e0q{KZ0Bg)8y5vJAqun9N`j9KrZv5`dJvo0^|}-5H1zmF@OB@zsCTOw1AC-=i*I#-I&f`SPZ5Cc7qG3hsE)iFcTp@9zeJ}e5#MUdk*Jv3FI>3K2HB0z2&@{!#7TW8>gTQ7iXZ1=;lxtekO=Re-3H6gmXEI-3Y<G57cG6trN~AJceY6&&IioFU~)3_E#?b`uNjxT$oN<!)V~9bb=}hkG(R(y!e^o!9x1La4v>+IRU)<u4n70oU-y71j2|2vFXjrWHFljj~dEFy)BYq$)^~3CkR_}l?&T>Bic1CWHO?nM7f(ai%VHYc26A19&&!Dg^>+x!-_7d+AAtqbQoq8!nzF<w0qUvNzq_uo<cg1j~~?-6hW>~fQfuMmAd+a_|3|@vD={Flz#8mW*}K?+|Cqe&JU-LmqwJ^NpmuyEk_g{SIdi`PN~>BM7;^l^FDws2DlZAEx|xeDizfXa}(l?mj(-{u5K{Kdn+nZN=xEr7-rudNK#N;^F0RJL}k!5{?>ip|1xXQgaQ-?VDNEBVQA>OM)xV{QdY!#4v@@sKN-^R=;A;c|8k`R#UIvW2wn%jZc$Y18n~I82+7EyNdqY^bPLP9{E6{ia*t58vPrIM-SysgYYO~;8H_9yO&qAt_N90CK5FA7Xd-;sf<@qnygpI!W5}TE#u$b0Wpo{3Ry`&&u9Ol(plTRI`T?ww7vTZb$Es3`+%zxol>{Pd@vjiA1vc#B__Se&gmPh`;0_I@VuW%!bkNAGKpIfPG|OC(B^zLip;d2w5EpNZCZ<&;t3f9M$+w|Yhk3T81Jl6&O3`GFV3Rs4bK~i^so*NYhE+7!`kq{D9!Lm+k-*s&K1*JN6O^f@njb5tnS^mdeu+SNpmtn&;oDyPAf)mRRE#dSvN0;3GM~R(g<Vn^z5F_{)X|O;+V}%{cc#Au6rB4hQN^Voau|@@H0cLr?q*CsGIGH;YfPRu+(mZ!myfRz;{0@Q8}Q?!5UcwoxeTrgP_Q42z}h9{FM9&<oX7)#1o;wgMHZw{KsAc@AXe*Q>B*X>61>@d{@hnlul;LZ6=g}8-s=;}63|Fu9dwP)N0cR`%vn&DKu>U{Pq`I!ejN2Fcd;_4n!c(+&B|92$yee{NbnqANu}w}t{q_j+)oyKC6XouU<nj*l;*O%IkAz06hGiA>5Q+0p=q$7I)w@VImcHLmV6~QI`~9ZA}SUF2D%Zo<LxJSMT4#-dm>XkCr+i1<L**U#hBwbd|ht_<|5VQlAz>end8!b^6ubXk14qT_ihOHor8NfL}bnJy=zkZx7w=>-z#FSu2SQM3FS*7FY=#mykY1J=$q*nQJU>q69H%>d>+Fubu6&knM0m8q&=iHDL*|#yp<}yK8XM;J37wXj;X{2ek+5|K1j%slslrm6p=k)ofiG3%A%bF@fDkxAiIqLYC;8NO&H)9h4rO4_zWS;ALZ{>fH60J1ZkZ!Ig&sKS<Nq0ja;nAhW~_)fw$e&c-#ZGhRgqB&sLzg1V7r-4e~Pu3TU2HxUY7=CE}Na^u}aw+7l5pG&xSdqcSQxF;aB|Xb01B4w6JC`)-qLj^K+?h+jj9wH@_!!;HY*6ICr45DcA9BGQ3oK#&s#`3V4*cne1Q$re^patJHYvMU?GJX{juHw%FTFIwq@mW!CIPSI52iVHE6y{szSdbmk(;0lO_8H1A-Y|m;bKarO56CkDk8!tkJwQhWTCK*;)l=*}Vt8YYjT%{k435)D*b26-@^05SF)0k59qka%vp-Do>xFk&lxv6^%(DP+y95H|m`~ITnv0Qqx>~Vii_V}0#t0fIrFgXuzI;5CSIZh1S@S8Hz7)MN4m7)|&CYUbr^<!dVl0#-L`D;c|`gb*3^UaU4&~97`?dF-#uD>j_+kOb4-R+ZAcC#sT(}B7mw5!c}c#hC6xk8VHc6-|K^-O3tUKZMI9u(TWs=aqF-W1{g;>WYRazOf}<!vr-&Yx(`m)Vv4k|=tVo$p8ys(ygE<&|a|dk#)y=VA3^d{^ESI#O-D2uY;TDhR*?H%nqd>p-KPhYEU)$p)D%PSqC2s^WDb@OH))Hy0)7DM1LfZ?A5XsuE>&OK;}5Y*8U~;sg&?_~Oo;)NtE#vjK#@+F$lwwCnRC3FlgPEVZ;S!7G=n7^0SPObjfWuS|90?6%&KqBZ)pJjkb0kgqtAHLW5W^U9086TzkU!7oyfGdr@HO{;NFZ|8e@nuy4Qvuz!7>V%6NWau-QXHU5(^=MbI=Q@?<WS5HxWr|@>m*4Q}f#5ufRo4w$yeP;Siu6@}Bc94{H2ileztI38-#*k9HvX1omN+h7B6$2qpG<)5;>IT?7E=ir-yk`0>rBgQxC`RL#@=zq8SN?2^Tw&*{u%95yg?)oL{<9+1OHhW%PU%|rhE&#q!JjIVq1iG<-gxG02pX-2T*5%zZR40P<G7ldF?Y9nT5A}EV}c22Xk=E)!;QH$pU?^=@7<6Cf^|DLoL*jVj5fLAAQmYU4d6qy0vg^uH&$AjhbtqQs|pq9C|d-HQ)!Qh*82qN=(*4`yrA%xy+y5H3+_-uh8>jE#=%e9Z4(9dD&7*dr-(z4$D5B1}vadBQ0NHsD-c7rNRj(BtIc*jf6Q8-}Yj%uYl=a-0A!+e!y+6NQF(khhaSJ@_A}}QofOgY8;Yvti0k~q!4)d{5+2jIl4CJ{PFolKbq7d>sxBz)RDpG5eYI~+@b*&r`@*Fmc<8pHl?*(q8(D=$fsTXp%0+PXbn;h{Wwce%s2+b9{RyFwniGhkYt<(#AO<77Xfh?1LDk#NzYw6)@ZoFO;{?%z^Tm=F``ACLSe+wRnCo}u#Z$zPRir4<<k}KEm$&xz0R3pVSPrvd4=<|eO1lQDOCm)Gm#kMZ6tR%8W+nHhV-KJQsFhO0wW!x@y&-Sl4EtGlc@Kvf7I=<Ds(hdk$uPQaUsuPid0XN=Rh*Gn~^_DAbXQc8Vxl$YI8JWGjk8myyMs;H9{eVj#)a0+<Ke&9WI+tvY;SQcQqv``<WxvGN6#8e9!WLr)VtqX+%JIR#a7TRAN|UNwLfmPLB`7$*y=oJ6N_|)a1h>t6Iep?Goz{@2W`k^32bF{7K^4Kkf2oT3JE3Ap}}0$Tkd+%yxP2hT?OO6uud%a?@N^yGg!g-aXA-prAIi3%Zboxtg|B%Q2Pc^rKGBiEw9mM>=9INK<>I1Vl$^ceq4$pIJ1oqzLTgyWw}EiP4p7W9w=Mn@o$Yo1o^rWVz#jZcWcVS2$0KJ*6@zZ8{Qvpww0t^gwAPBQG~@r;cX@UG8YdWbi?{5Gjl(pUTza6=g&#qn0h;fK^gCrI}NO?oFeK>3uR-McMDlhj)o`S~n7E4B>D6_z2?#6UM7jgD2W}4}0dv+IT5g%2o)Zcu^uKIP=djHG@z7a?JODM9|Yj^4jX9H;;+r%_V|zoXF@OGf7kMmtV>r{jZDs+XqTm<g1I>im3wGJXImDs|tBj1yUlQT@}U~Ymds9b+B%a)E=q*i`wH%CvQ=Eq^kmvcJ7jXR7|MUE~-7Qm5;CpGFY8HK3;e%U%6!hkop@)Mog7Po77$yg#q9Z?1p0+Sm$3He3TaREKGbb0nvYL_r%|LN4xnAQTy;;Mj$vrM5xc&trrvonyUDUpP_=pKQK1B6CXkkJBATt#TN9HH*63Sx@>f>^G=))V3>)@<H|MHeSiveo(d9U-#d!m`{*|`rakc<Pz~CQ0%#Ps_WmZ|wa%Yry=GIae5QeWpiT6S9{*(Wdffank6JQhFsUUQhiS8C#_IsZuCgY)k>y2$89|@BV^N<q?{Pwv8`N^2*mZ6Pc<|SNl;+<%qbzkF(^~qxF^u9;-;!Eo`fmCANknbi)wez|DdrOEu@p&7sT+pZ#EFPJ(4>Jp^^M<HcJP`e&nC#)shT4sI+S#vKE%^VAgGyf5|%Gg9s0%u)~-zmDh%}l60Ab1f`{r%EDFdV%+~Tn#<;`mnBTjtX1B^yp;T<bR3?;iZPj=3MjoU}wO|*-?;cFTs;_o@=fZa>d^KX+$&^E_;UK#|F)o&$IB4`D$xLqDZ7ul=QJDTKTm08PeD-9niz{S3&NxaNO~eaa7g<~v+HuTjyU2ARCAn~c>!PnFAkMfhdf)^y>7~XXyTvP7^NhI~xD_)^)*06Y#Z4KD$1X3qF7VfP3U_t3yOHi<WCoH>=7Z%J+ydx-S|MiO3f~yl#ceRa!}+q|ij+oPfU2_2xyXBwn0&-V{(Ib?@x#v&NO17bi>sKFjQV-{{5oY#lk&=~Q-4+W31&pTh1p6w0u1Q7BXPiBDjI!J*@IXr43;BO`3tbX8ws*nQveIVUW7_zYE`Tt>_s+WnXqTRu)Ff+yf`h_@CCz@dqcI*F}cUDbbzR(?;fVtZ#3gv`2JPWhN6mP=7+ZjWvg&jTRJ}9yQ|mhLVpm)j!YX)sl52b4SXn}sFHFCz6z3&7D`Zr_`kd|iM%q2ymAD*K7AeG*Aadl;a4V+_jnrK;p?wtBClj3uVf;xWFoI*BJVkAU-?8n2%kv)F;vN6uHp=(2)DY1oy1LK!ERH@M2tzq)Nt%yr4E^^;j|N<$eev+AuFS1!Xq+~?t&Ulm}NejnIO*1@?-f#?4~(k6*)bhQ$d_L4aa&RxibH{zGxgG!{S0ts5kss(v2l`NFdQ{VAg%9i4)EX%}7}1^n{&?UhzTFkbIso<cKb0aoX|dwE0^ke-Tal_^~<@=C7RLKpE*m!cySI`VKphO;ommP`NECd&_udM>d%dPpCuUI0258aVA-uB+hLaB5$N28<zSSBMk{NeH@jlCuN)^frzU#1S73O@Qc6k!h;2$h_Ub-lVXSz<^d6zdcBuFa6-vpzm?9@aEzyM`rs17$Px9!D8iCx8T<oOBk|0+El%b#UC8*>rSl9AOX^%^Z#f?D<<*(Zxx_qj^x^2v5^Bt8M~;XsLOsJ7?M0~FlIPe-!c)03+&OWdM-^}`-(ND_KW!Y&zI8;)a`f)mBb+B6N!54qN2)p~z>NAtBNfY&M(l)JWKJ@2;cr#mIp!Jp|K5fDJ-f7`l0kEUmw$VvD{3l@c}hcYtIE(KP&*N-RL3<k)jYziQbsH)!Bj$k!7i#~mS&w$>Z8Dj5nM$HF`$qucRv6Ug5<}wTB59hyTfQ(SBYRjs8ys{OB6d>_b9`UWi=s5XSDvrDYe!W<w?b1zEY~FwM0BLnxxnp)h}B|bZ%8tfLDY<o%$D1j8mww65`d@E>Ls0w1b3lK3*+-ZmQ7vu|lV=(OR2H<DiWvnVevAEsx&y*qYQr1?{13YN1-6HlGMT6~#RPL;^|8_$x`5qY^$A%}ZAC|3I1kL-N2t-m@!qUuHL9*2X20a(UX8chlV-Fw~)(+jR){80PPhctAJJuZ-YejgBYW*Z^VzOq15tol+3T@t+GnftoK(L-s^#2l9nrswN3Q2L1J9+rW?v&WJcX$s;`dg+`_@h@d0xiSCI_Pzg8CpJE9bi*H9*CgHIFpok-GoeA*R7B33CajmNUcYYtdmijPYE#7BbXeN|tckR>4i%_AA!$07pVnwExa`|L$2}H%yMe{#R7(V%HQga`h!QUr<mDbU3NmQa{_x8Vi7n5{JBxL`fB?6q;Zyzu~t20fQM@9Obiu5B+C(VlV9VmLrkvl&t(kFv|js~Szne#>Zvg%S5q-YjJ`rev`Oh~fT9Axiz9A?#ewSx0gDbB<xqE&9=Sgj|(vH@_(z|cue?QJ-`9|rn`dwzev&89L`zx8Q)GXqH^PN&j}{Tcqe-b|L>3^v3E^kyp91EMAD-lfb;GMO2m20O`OHk?PvtpxuW07qB9@Tf79&S}g9qB4wG01b^`EUFqaoH8wN1Cp8PX*F&soZ?yYPqPNaJ@2y@0Jeb!N_ns@_jC{NMqdG2k0{Mt@#-iDnf|G-2^CjcskjW|*%%2|s3crR3|wMEQgdJ@bvyN(*0CSTy4@^@xAMfgCCV+r<lX=^C0txQn6utZOk2igR%y0etZZic%4W9v#Sb=w5bL=xie(${%YhtGv*&2dx=L#{@9tIOtTCIBN2IF~WBDRiT*b?d<Yvv}V71;zSyEn*#z}1n{UI}ovu;Ll)@FcWt~Ky*J&ouL0I53mHk&6hIZxe3zar7uc)&T)8OT|_<^IiQTbJU*T`lhiee?NVb!uH!lbRL#W1eSVW+GOa;f#!%ak$w6H(3|Dd-<6L#^|jQCj7B=*%ICC<|0;J;4k(>K*Y*+=(~%irCFL5+fI;jbAUqr&vqX?S}>pCHV{@`4fmOQa*^Mm9H3=GJR8bL+jg>8sw2@HIT9!Rba_eQ&~eqw^dxZ~Iw^6sQoJI4LtsCRnzD*jYnCckGmoNKfd`@De2uJOV|*hxvNkRFHVjD8NkDS2&Sj?+y{ag)6?_B2dqs*QRA&%=-SwRph`0^%G4PA62RJ&gZ&D0%Hw3@op09`wY@SCd^0I((|6jOYo|>!x_`a=8R?u*)u|%1M>y$sCvE4fZI+xSyF(r+<N&ve+rAli2nSbxF<6G}0x3uC6l*Qa*LNPzUKP}(IKXNy%lJ%gMVOdElF4SazLXJcYIdx=}8yJZ|bxG*(Fn*@Yg&IUtZp~bRCQXM@tCBvz?iN$XD`5k>GkHoWG(CTgot|ue5l0CEn{_QXSmWR9*F&;13_4YA&ykynxF75Tc9K?Q@Z*c;jv&U`kZPY556HI|K}UP5rfid%kV0jf@b%{c$xlR#q<E~i*bK`S3(bX}Mbjdioc_dn@thT(=k1K=Yz=|aiRY|G<Qc2VVsS{~Ks0uPf4O!#rfcj7vHCD8?x2&Daqo3|#8}pCp?J8W54a&+dT!Ys*{JEjDFs}{Y*S97nAdIK=WAmotPeV7B1y)&R@hWzEXwQ9XKX1%92Q!{E%zYUh(M7)&Zbtx@Rsax_4DYjLq|?_V(6O$jaz;_OKO<fd0{DcOvVW9bS7dvt5I=+QfaSuRh=5ergGTCFnkq^D+*N-D=eUYu(GAa^m0r?RGWQ>Y$$wqrXjM`ACnEm%Vb0SV`M{Dqpu-8i*sZ{8?SZs2-%Q`&~A-%k)AUrzKTI}zM<B96G~kB8Q%~$vwVSah+GKJRYq>3QVuaE5{7r69O~fRurPr^@P6uaNiVg*{X<V>*!Ub=i@3LMiaqkpu0)*?Jx+Jl2qFuQd2{E~K~m;)35xpKn^+$2NNo}LxYq~n(Q6dd)Kcd8POYWkvwHu*inzfSc?2-Y_TtmHLa5u(HA6z`76-&Z?yzopb=B}!-r_~Jo0RdsieA>O9QhYMSn}W;7sGSh`<d^!bLrH*XS;OQ&C^c|z%Wg~8nkrp>+&lbbhik!F1h#l*uAg5eKA`rrkQ3MwS(OI^5L7<=(}+2t!ofXt?OBkOUKUd=*cA(-APo}-GZ?cPygRZF?hvw^#PlmGgzd~a4w+h#%|8UN|dbI=+whkts>;vjavDR`Na@UiLY?GE|L_DG#X^gu&8%Vf)%Zi!U&6wNU*XP2zh*ZJo$tH%aYKJ&UtN%P75AF9I%(qFS=;=4s3*Mh4!$n<*aBRUE|E0My)aV3ReABiONgudxVJik#1Lri>QP+g+`1b%NnIqi_^PhXvw|9@|L;9`IkGpac5!*7DZ@#$p~JIh9_fLbT8dv_($BY`sVvHC3JR^LJA!8oIEf3|6vqE-zTvAU5%n6m`Y9On~iIOF$c4dKstkjsZlIaE)K?qhvhs>;zzr7Z2J?3I9Yy%vXbaT5Us;Flr8`z!oeaF+`6t0k3|{ouIW&UG_N{&t0sgV1PvQw`o^gLq|#wEAV!3|H&P=JRPB{e@FIZ0uY7(BFYc`-$hA8-RXZp@bd3-EHnN4RK{1Yl?^uM&v;pPaFX&i#Im%W)!JoHWG(ACLSS82<7=uq#!xBWt0XE5EsUz)7{=d!P``IUWdo?j9KfIj#Q|cCh#45I5fRDz>Sx>>XjO4~HV4LnCU8rQR0-d+UZm0z;2J9n0Z^bguu*gSP;;7;NISdLn^@~<PZJqdUIXrOk@b1P|wMB}Z{A#W}_9j~{U}LZh_K|L_WLk@dV)Nks?7}cZ0Ce@pA}Sukff5wUBz0CGq11sl&|5#+7g6RmbO)mb&>NAE>SGEqK;J;0&w^c(yKk5h1?6O@`d4jnN?;Ikt;(u1x_m<Z-)d%t66&Q<^cEEP#(z{DT{E>Iday3lvkfNeRPMt1BibWO<G=nQtRvgzeJMx!XHt&X_L|O+jkMZWn<p@hkW@-pulNYr$czaP1OSV@)j!NMQpo_%(2TeWKrpgN>KH__?wstNM>HchPpJBxrI}1$2bPE5?f#S>e&Fu!I6YfTxBfnMWY~jGd5;)maCNpayu<4|KalN?1!=e#cd~$YZ2n+V{+@L4tHv^*Sh@#~c?W+=L<aoKZLy@l7ndV{gK1GvE$%Qp;9aV$HutnL;hO#0-VYqV^7?mFfWL*8q*rjvLy&8h<}W6228E5uZ0stBbUDdP-uKMC0U_9(B~Y@_9%5cMEc2ITB)$QCH{Ls#{zH^&xhl*0pLYMTAO0S9fA7mE4qtE$@8Ie;_n->ons*|PBlERaCJJrHD{v6ttovG(aZq@{5i&AYnb(0&-h?eywGl1?pM7u^lF+A7geOGl-;3%FHvOcb;PSTH)zdv$V@2@8c>m|fs<_f`9Vq>W#gD_@wamz793%^;LAuYZ7!jimmRNL4m($k8V*gJyvBr4n4%3=1hHfXKJy^8<CUS3~ck_3CDC}oWNcWwZ&|oIiJxU%ID{+%QVeJh|deuOB)qIv-b!1I9BSW^WCCVyIF-zqvsS*xG+*HX?9$|2b7wDS^y&=D=;BzpuX2(XJ)k@-IAqiZz69y+mB_|9{>-f}SNBlZSb^OtbjB?i_s;N@Tsn6m&R4V#Zn;35fDF9iBMfP-P+)gxeYp(pj^g$nX5v-hP+&q~$z)-bH(Yo3|U_M_l1dTx4Au=b5n!;TPSk~nY?Atx}^KFZ<R}({tPW+CrmnfYf1nA17q-0h94lM@AbRfFe0<O~%J=8YbT?MpjmGubU!~u)hL!xW5_RZjBeNaR36hGY<om?VTwObpGyJb2la=kSCo0xzm`IGxj8P^+}VezChgOrX8dhkLdM3KZ&8-)dISIj(=kNwRTA*x&%y7Rq=D*I;>Rgx$pSu`{{Z6kg2vERm)kMs1+O3PY03pd#tnt#UNJmZOrBMTQ1{c{tOpJHNk=%7{$Tgicg_I%?4BlT|fMfz4RjMn;hzFP9z1@Mm&bACQO&#A#|uxTBU-;PPVd70h|5ELryZ6G_JG2d3&TkdWPm|sxo5py1ejK&gcYsJSXn$0+GH&`MpzO!b*N_(=j3DbGYB1PLU4-PVX*K7dfGtS#Ch-7OUZ91Tw0Y9ad)LE=QV!j39<-h-s*vtq<ZqlfE>y_!3H;Qo8HF>2;rsm^?{Hqxhfndt7M-p-Q%ODF8v~}!q3Zs@!#l(QRnkJ^+$soBqVPdG>I6^ISSEVaJgIM#dvNBU99n&o@kQbgto+z<MtZ+m#8?zghUZ)f?n5IP4ysjW7P*ks=C=hBHsxw=R-L`C5x4?1`NrMcxJo1rki8R8P`=bf4+kW^O2wS9IdMdHnw~dJD^K!S}aQYYx8D}lFxk|5gP&@+M-8HYN@8Aw7!W)#%B)eI6%gXMYUhQsTI?ISk@UeW$=0m1&lqJK|yisP9M;`gwj8e^F95y<}=GL<LJ-Oalm*=HLr+kq<fA0}Q8U|t3JeCoR;)~)(TiGe;yHWhg;Tnrsnr1q4usZ59?2gMf_1&p^4V>*P&6W6wnsb6O{<*I=X`0Vg2Vta|&XJ~hPp68;@PqKCk*qh0I!$?-N2t@JT1gNA`zn2WKk78jk;kah#uCO$P^Yc@qX}_kOP8BDU@pyBme<9sfyJxYa9b6ra(X8}a5{|IcG}x>JlZU(K24dC8{(_!&<pG^-z@e@#dJnK+zCuMONA$WAXSNHWunyrQ)^i<TK%;|v@NR%-hc+nEcrxcY-#Z{>of9dI41H!Y4oPTQxxpRqyn0tHpFpRR@_qLN#{d1_cS@41#00ewPZTK?<IuPSci!a6LBmv)SuA7RjaVhvzm)9v34sYV6we3DhH72@gewX2*-Amvg8TJ@dSA0tu>xPadv^BU@8nNpr31P(-)Vl4h2@#`88$L*V2trV(p`4(nI>qA7>4LV#-yezL-o;i{kVcj%BIJ*NE&aZTDE5uB5f~@vKT6ALi^n7m*=>aWNvZwEF`=+0A1?+4@{E{cC}6{a4<_Bl`rbww)+m%e}q7;EP=mjdtD_tL_QX<KDUnHgc~<asWC?#!Sm{<=BtRWrmR5WaLqhF7Desy}VVWgyn565g*Sp$>p$i4ItL8C>Jq$US;CkL9==&2f34W7M-apqFQPJR;Lk^Ku_kc5gvjznC_Mh4hQEeVQ*`!xjdP_@Z<<<W)3bzSjY-L=xrf4{9fH}{X2HQ`Ei@e4>!O$H4C5ZfeY%h1{R8IIkExHA2q<mdH0+5lfwmDAfHQJlnAn0)zHAB4UF-!`)w6%%ZpE_gS~t*<(EEAb4s4jYY#%#8q~8dw7wAwHEVtA*!q^~Kua_E{aW8xgox)_-_A6rurs9s6%vuXz6Ycg-ETwKS&Isb`;Rujk*NAcb)~=h;WZl<_eafKOr|XRxf<+C-1#rGbZO0(k0Qa<kIr$i`NztQ6n+|eyH25N){88P`cW4_qCQpwvRCXEO|bDq7l9Baw0$+~wu5ACGh)>yQG}f{*TYY`2xmkQ+PNr#p@K1w?i9OU2_<fAV&dG;h93<ij+%t0$z#?fHhU*u;J{NEJILb3_ICe-z1_d~-u`|9&KbF*XSksa^zbkrn+ubX$Z>N+yO=_qiNvl?Gm#Wfn2as;$L5|W6Qwp8+mI<-Ov&{JJW+BrjB}87#HJzb5w^2NQHF8=@<cTk=bq?<Qk0h(^`nB`(lVanC6}Hk1)S5;6BP$jr~=MGp7Dtr8kTNoSh}Hk>4sizv|3En35rxP>8_HoBby1&<)hBl?xQ6Y{5+}9KsZC(XIb4RHL1{@CKY&Z*jG>PhB38(5cf=WVf#pS!PFPjrQ&CSb({co$SyRTZagdQUq{)6G~(jmp^i-#BlK>TV}Li8L`~=IuxyGV{;j4KhLhBST6IE_aE<j^t<RzFL|SKcdZA5;0`$pJ3t>tvXj8UJZbyJ$Hzv-4E=^oW705ZE^@wUxo1$eDR53ovD70L)o8z2XB;uJ%fh{Pa;xLjG%PveQ^D(1fXZ|rW3jg^>D$KLkbhSHIm`@1hyy|H93ChP?!qbtek8*J8X{4&B#Ly%ICmCb_m0Ea(4cAamkzPpLPK9<R-GK#VdycvdS*KU%&z3nNh`2A04SVIg#n3jSTH>-07lzZ4;KD*-p4OcENfN~n3#!C;f(oeI`vJCO<awi7oi`>-g7xstHtdi#;Pe+fTlJuFMmxdX<<$yqhdKf$l99YAiVV8&fzTsGLt&AUli+WvWLz6my4ft{(wf9c=$P;V+#CI1_kX-d*6G>8&fKl@IZS}B5F~a^Jd}HqY(|_lOf*Ym072bkCKwfxDl(w0c_>a?UlTw}5jk%S6UW-l<JNCUC<Ar2OJqQJ0y3a6^s%*$(V}@vv@UU-rXZIt$j2pxRmZr_K0XoD`87av{tI6d@{qoghvX?Dnp0iGN_Fu7&&87D0#?B?9~SMb*n!*{iKJrK%5Y(+E76H4Txp7PdW8g5q-Zx_b0|jPT&~#YHiadL&DIB1`lW75GK+utM`3iMt%t?vrnu%}Mu|ZjEv+RFyBcOzrWPX)$(1=I(|)#cTQJ5^?J+Xx%|zTXl81mf1d%3bLj<wiE9tkXBym6gbz^X8D}zfMjcqg0w}cseOI*^oqzNEz6mv%d-;VrvB)>Z%Zi(lJTk@Q^rJDc`p|ZA|j(r}-o}PIxf@j`=wvs)AxMd|ix)^@K{gBjNF6@HOFTV(d%k;~n;tUDr?uSakIaCSfhOylx31{i3h93<H=U@Cd9mumBuE809*yziQmT5s>mTCgG%<whh1JRdVo6RPsvtuh|nsT_S(;V(C6GY{(f9=C3aL*bJYnQLt+c8^~BDsgo$=Eiis7;`TF>mWFi-xTfEF8#m=Ww>`IFxe(A$xPIXIl-2-L!HJE!&J$0Gm>`ZZi3SM59<~X+psH39RqbpWf9{OsEaU-d#-HHZww^8_OinO>T*&@htI+re!oG!4d_<WRyvCq-`qz0!9Z8#SEHHq+h%GVdFad`Hx=kc@JaZP!T*+@OdGwL-83Uc*>Zb{oS#dc%;sA%jNrDo+pDUzjk#(2K5axK^+jCHO&bJ6kCx3{jk6dR5=ncovc#jgEAvxggAZ27I}dVL)!STWy^CG3NX6LdK7X+5W&auZj?~K{b(vLn^zxiMKQXh2Hl6bp;S2)D^xVub{1p;txV8lSx_?#B2$VIU5CT(jjt&P;S~t1!vsP1gg2!Qr6Bp;G%+|;QYMT8laWp|4&wcBM*36*DXq6&THQQ|a-ETfVv95~j7p&;Ls;2y;Pnia8x4&r{BnX!P1~}OC7j#1EQc9`=nf4ye7j#aJ}9QCpT`HK>G)>G2erX>Bhzf6)=q2CH;r3~fk=sQ&p@oQLr(GxH>_Pq3c?!(Ra5~uTBgIw&4q<JwH^vDithPhWQBw6$P<-VUTAzBU;@WFwg;A9gw!><S7?{X<8tjeH=3XpbmcZyWs3pJ8FMf!>9uNn78yno^POhyMC)XkYLQ+?CCya>F&PtI`JiT8PuL!sI6LNeH2oYGM^iC<p%qR^S?l>hLT$|EXDq!eBxq3m+H);puj!ecY>cEqPI)Tl@CPrm2rNOipL#%ak9eY_k~}xp>q^<+(Kq$Ya_`%*OaZO;Z<hEXx%)iU)d-lOWB&<!2d@7lt~b>sbTlQTFij4;ATQ6)+wzuawTRJ&@3lxyu12`Lb;*a%!4d)E1&5;zU!pTUMgm0W0z~rDg*P3=#(ntKKy`F<K;URMtcigwEW+I~X5$bJ<&_3IHrDdWnZ5=9@8LjSLK8w5lyBX`!^+a2i6C|Sg0YP{N{wUvH(sP`vqMYL`!>Gs9&CJXkAp>}QkE6cOO5X!d0O_q=LxqHVzkgR3gt9;d%6Blo<a2d2}G}XpkwN6vpbvR=7rIf3l<BKHYbhh)ia15kw1iYHH*HfXGV(V`Nit_;gacM(36Z_dKACK|1xl<StY`V+&;+CDbQZ-^B3NI;m|#YEwRID|Jjg!M;FVz9q0}Z>RDoaavl7-#UOVLI%zj0I8SkC(m=qSOh%cTKQU3+V*<*2l=WN!fiLzxuM?qrNwU$!4h|&2DcAH}A5CC}GD}~!82BjnM71Tb?}Y(<i)?=k;Y%=q!O3e)jUmGF2S2h`W*J1@qJ~zWXK6%`J06LhPNr}jNUMrg`vDW2<(EhTJNlRK>WaDPJdJ`ly{yF-$TkK_><1{35ylYv6z2d%35>1|CvQeRaGe3CoJoP%87qLKVgkuP+%@}3GpqFF6;bgsjRFUk<wbURaYNXZGeim_d?pS?k(rRn?Mu#V)@lvBnwcU2TMc!8zKs`?df`cvQ|@@mjT%)^{Q7bgcFE+wSE_y`P!#@vhS|!as9Cw6BFv4|60~^aCjG#pG3ZlowJRTF;;~iTMK6-Z@_Xf4emb}fanoON>&z9l!UP<Md=FAd;w}dFu6GQ(!CrF3zvUb{paK!F7)vmD6w0N2X}KQ8))vn2x4w$_=x=;gv3t2+{fQChL@jf_YkWRJx`dehGIj?QWsTjr0bA_O-OXb6#_C>%xuQ*+V)q7qJU9m8WuyyTIb^d(z!eIM7PyanYjllKGi*^SsDP`oo|*~lBA(IC(zu#vmBys%vM4Y-4dUZ0h+mNeU<r1S2UWo?$~{)9F%bDNQDB5RUFEc5M!^g^5kGz&%`<@P+cVaD^|cM<Kl6{V3d_U~NYA8<-GYXGC^o{U@=BSK<&{rN(#t|iS0^Kj*eL%U>;op}7!0ixQIn!iU!C}**icbS6t5?PdzA_V*D!WpEduk!jSZT+d=@e;1Hz<=PVYy?U0PVC4Wn^Lz#a{{`C{K<l32}{hPGxVIM$;z^;`N;{gv8IFi@5~P(xiNeOXXP30;ve3nvr~o8LeCqJ@yAea8?|2ohe1#i4N`<TA~`s(+{=zi@?NRIsYySr}u?F#m3ii2dwws*kx)nrxwcr8~B8E{x|~fA08W`iZc(%n4~^&R%^nyNOQu<crhaih?7=qlRA2ixuYh!~837T~!f`V?!=fC&G+tTG*X9ouQ4-Qu8W|vUR*odmrz8{N68rxZ<0OyNbB&*tt1R*k*Y<@z`?*D{f3{Of9Q-Vv$zL-8sG%OA6q`O4rZQZ2|+c?0cgU%M4J9EOtkH<;3S{%cY4@6@@<*D~e2oxR%K*&6MOO1T6|Z4eD|u)n}u4Kk%(prP=nVL34Wu;I!bqEykW;NqF4hfWzKc-xvl8)_k)_r2&n&B9@T$Ki1}RzidADzxoc%=k0+ArGsVGe56U;@+>_27J_xGNwBD4g&aOwqd*whLgM}+^~B&6lHCnK>zW+ZNvMk;>{Af&vU)}U1>#>ibNKpD>t&fcDw*&wY;X&LiKuq8o2^ycs07vV<|N}K=@`Gu5I0JhA#MqZuXOyDTs4Dj*5qOza01Lez*7_(?}lDy`COy)R$%8t<F5DoSR$DGKni8)cTjIbU3}#Agy~JmQhsXHYk(|ZnwLa-?G6o3Yh(UlF#eZ6QXOUKi=9CozoRckM{F#>KHnEZ^|h?eXpuv}@|m^3G_1Zhwff4ow@%`y4ShFp4vwYQa)!uWiL!2NJ|?~Uyy8l70ntTN-3HU7jb1bos<kr28q<i5>5-|{sxBM33SRZ466Z8+Ews|xTDMQ{aQnJI;GygHPW-}8Z_JqG=8!~b$j=@w3Wrz^7FF6NTH)h<3}S{?@{i^~cxzzXYx`LAV;EO!Q&AWzHagOH0qV})%o!|h>dL_F4Ft;*?Wi2R%VEwPJZ5_Ahk8H5!99gFxS1t;f`ABkBG!tKjFzWUN0*pcXE->6!?PnSQEOy@g^%Gj&e(zXPKfbvLd(9u!L{I~&f#l7kMS?LU-d)Tr$!x#vP2K?{;%b{Y^VV}I6q($dm~Y$&Sj%7L6Q^wl?T9UnrrM_CDMrpmXt_kxTZ_DrnM@rPcwv1$}od7qf7+0!v>o*^3nT%a^5${<PYX#?3$b-DSQ*)R5VMb!F|JpZx7gy64eoV?j~Yv+Bh*G;4S3-xl5{{vQPAGljz&*#hAo*i->1~B(>Y7P@JRku@)@QOnN8U@$yzLH=V&^Kz1(?zXE}kP)ix*_2LpVCZdhM|CSkrvb?@{S}FB`9!yx+3q(Y%S&A)t=f=(Gn1yJ^sLJ^AjHTE63YY6ibg#1g*nO#*Dx=;>*0V9er(O-1lc$J<-A&YbC4|HpE=Smvo3LV7-_{mO-Xc*e&l=|z><1e${5CAN_lVBdD-3v3_XrSa&I+oPg2;_D0-p2*J*%(97i?O3f#pK~p!+r7{B|_u4fNGK1e}?D+A!1Dqx&Npj|S-7OT-MfW3Bc9{tp!t$B4Oh0ifa73D^&Vuvc`2dXySHP*f_u0IQs#a%y%ct2j|HC)QWnN}oX5CM%p`Y3-2~D<^UnSi69STKs?e!1pjgzzZ~r`DF9zy~grRb*p_K+mOKP7@==EQhKyp93TjG>{h~8zCECg2xf7>+5*S6rw&tjw^Cw%QpWa%%-=5j9B=OGx)SJQ648Mr(JBA(Ep7)G=gxv;lw!S6)8xPMQVLv1)4qcOR~dk8J<OFrMrHLX!UepPs#>_njx;hYU+-2Aig3*~PjT<ZV;wH}f<eyQc^xhm21Br}jGmIu&0LKukiA{lPf-Mi88cW_GubT#xgs{h3z}T$TVQT&l;!GXtzym^;WO%P(<a$pmgU;LEO72WdWT>Um)L@Z00v<hGNPoddL}}BR#`Wm*)VuL7BZrTLs~cN3&_Ofb`Wu0C-5{|$f!BBa*~Fi*Uj82^GK}RDZjzep4wDcr(H1z(!!vU#GJl8WtwGfG#_=6K1s1j3}W01TKe|epxDIKllSbG@sx35%2onfk)a{4D6-ce)!<T46e|KTHPDF!CjxNG00houC!iG(zqk-KI->EcW1WT*ElCc9nhq+Haf-3@G=ytz)I4E}Cd($<z#TL^9!B|Z|L|jZmGC)(<;_!h)>@_&^M%^Wl52&wVJ}NO?Pa0q8PqAlJ9gZ~!u8)=U?*QovU|x+{t%1qWloj;T+OzxHQROd-hHjvu9uB0eN!Fy6N2(yt^H2LsUHqbmGpZq_UpZ!p~T93`HoND!_q3tsW|iSjknB?cEvpkQ6S8*1+Vi;eKw*oVc%FJqH`VHRk3UXTw;BA#oR&a1SSvnom&r>ZhOEjgt!7lRF%8|Jmu5kw+%s>LJ0e_P(?UvG1%&HF_gE(-6%gq>a3w77aUMo;_NU1Kh(ZqrmS&Vy1R-RJNWaMv)2UXWg0%<q!L)WnF@t<h>2PX_JLF;Lccd&4>(Z2`Bn9{ue_+e&-S)&^Ya?p(J#8}YVTWGgqmQfBxZ=umtE}&!p0QStk#zhexb4bQdhep4KZ>%@7mZtIx_JoVg)CS?LzB{Lfea7yEe^SY;S+0xBdD(L_}Y<+!swgCT)oo`>G`a+e-gK2W0!0QsAIW6jnJl=e-xeSI(!~?Z){#N(M4QU8)9}WMJfMN=BQTb#SVt=VqxFNT$VsDb*dnUiRMdnT1{;`Ig(-y}qd>hRE*Sm`+s#aVFsZmzANC>RI8yfxJY$nw-lQ*A%i+E<VmE9YbwqCx+OMy}N0_KPPnZd8$W{8t{i!mF<xz%JQQF@u$Wr(i?|Be2R!*?QJg?vJ#eB0lHgC39cbGp_$%%oSFVB&#u3<E}z#&qDP~|>bg$tjJn2De>*b4^dsUm8kem2*1)Zwif`-&*matr0yxEFTDFLnl-8dU+W0xXV#SsM&#VemDU{-O65PWasl_+pkMOjnOT&o#c5FqYFR#kmfp)WesLzIr2(`1JthH6$sYQja4xdJHNzBc$nLq5*tAV5*mWxfInt3r4>b3Ddd*gqmw&rOS&c7Q6N7}LM{ag-?W<kJl%Iew0Q@%3h#6(%fsQoPO#wcw?H9U%1(AEsK)RJeEo?%&89+AZ9h<78Zz%^2O9usY}OES+yuCu1L*$LQ?D}m=ud_{E4jbbBMT1udLLm{8AY%~P>#LCYxad>8+?)+rA%#@665W2Kx&fA%1L>pCZD=98^HtR*e(TxS5#&|o0Iv80tx=L6YnAtnODfgq=?qogVjJ=cDF_^HSa%~7Z(R^g~&i}e~R&*c_Lo)J7dvNsn>(h68`Z}Ip_0!i8ejVZ05q^F8I>PVrG<=w+;T^u7pYv}1N>2NIpME44;&q~a#IemE?zi%f^Vo)Ge>Xk&^jY8i@fq0Q-|K1kKu`0NpF$DUlwIuU{H%h(LhPx3#?!@P|D?wzqAmGcHvc@~@7WKJFFxx~>f<}}SFPUCC(#4%>+8uLn0iTlti4G?tp~N2{P>>>v!rgL2Y0|mG*UhZfX$%wzo&^rD>6@4O%LpbtBoT;y_IZ<#9>=&eQ>q&zGBh5^)axq&xt-#pk4i=c7i@X|CauR3Df3d)x!<D`pH;-C|8k#<rhznIe##IMmz&Cj9_&8mSol~i8VXg^e=i5Vvg6c_|ai@R_Y&G*`P&VJ3T!vhe(QKO)d2U(R#lZkH=RmgXI^$SnlcR8R{RvXrd*JZW{ly7bWDq5YzlEJI{^)?C6fp%|>#5+H9*odSyD)^4>{eUbGWOH!k?&n|S7x`Hh}_C|a>5DV^uXf9mvO^4nDmyx9b!Rb{V(jy!*0*~4fpXX9IXJpb#3r->Dx&d2k=SbFt!<M255v3hmKuiLvP-wOWx(+3{ZAwBsCKYRD&0#g({!SU<%t$2K5F1lx2*X-SQIr9g9BE)eyA7AY0J@x0V{q&|+q3Gimk48){j*rKuvN?Q(#3}V%AEv=P`qr6OybaELel8}efAD@S->nxOE`8<fv_JaMvoFriBwQHY^Ybk)FF7urhI-mZugo87V@kHMp8Km-zp+BHNSyxx_vd~72LU9zzXwNg{yBF~om>BXQgfBp@k(g#W%bF%eB<9jg~5H7^Z<TH>oqlcZc=XS!~H#Km~X%|=8WHmYHTaW^tfhElz>CknyL{11jO-^YT1VZG-?v)<nrv@5@g!fzkc>O$OPi=0IJHwE}G;kk$EsZHdUCdhc-XqZ-4T4_HLLk+@4p$Dm@9c@R!gUR0Bzkh5c~Lzk?IUk1<h;-PCsb=x_ekk1%-dED@$!v5ttKD|qg*8kwsg$p<va=HR)R1pPvdjCd!}oF9Sb!ddWKfM=OUV!QMZ+sP0tPVhg{YGmo{JJz4UrOwlPuC`>e5SBdEfXL@c&?=|`-?*h?X8+UVm5lI7Et)}v8mx~h(gZ)UB3(ldAI;3p%h91yI6)&3^LP|vWc7O#nXJtFDoqELrsJ$MO)5<iD<so$Oygg9O^p?(*EKi|s!==J`7DazS|ObTY;m4J*g41f#b~8$Yp)NpCT|PkSPxd^Up^!hPA3+(sdmjT=4H8l@i%IOgO&x0*fCczh(stv()F}qt0f`|j9@M1X~qFy!`@6~?PEpCWXch}vFMI9ZKt-0DipRTXj7l!Bd(`kD|<k5!^Vxb<cT=oMqxp11r#yah<o8tTQJXQ%WI@{l7V6*gELqo(hYlA2pYkp)mIXu7BZM(boN+noyfJ4QwST`$_D~QHW%GH;8-*x&>OvH%Mg0Lq}k`BD8L3|eWfZ`v)iV3mHLkJ<#WQvaaz{!7k<W@?n>X8a<Wn=qBZ+2oyVcY>W^#^@0q|ZPQ_=O;y4XRYhz8n1=<Hd{}oNOVEqc*R|;kL;oPGqK2#}~y|>qKC?nAZD^X}&Cw^oGkalGASWKQJ%l=9!SRF$=GXDN!?vMNYZQtC&FbxMVPl7!#q&G_T{WM7ifoXGj;JevLwL0BfOJCY?A_NoK1BP!)c9w>nc~`{$a_J5(eGWGSL~fY`fdeEK-EBGhJM=phha&IUkM7Ai$o7$9(LCRM8)P2?H+K@&mowSm`0O|d94EH#9jxK1p__vvKrE6pAPtQR&2(U+eDNO!%F3f}o@{`rg%LIWeGT^SJ)>&*DW00D<=tG>5{)@!u<iquFAuJ&3C1)ETi)qo5DN)l;=_J)?+hzOVM}5l4?zMtc_tlRKHt+<+X@hNP`@y#`%T8uk0RjvTiz?(F#y=owKvIf{3yRmJQ=!~JCnwQcaYgNpgX)5$$FWsZ(#s&2{#t*W%hz!-+8*8ei*?}a&6x@nWmK_$PWOzVcNaHj684_VmrIyY>qWq^oFf4|JzIThyj!R+y*i3+uWt6?y!FB4(rsw3Ez?UK+_%Qs)q5C8pN7~?B$|6jLrh*#;ifC5~>mb#!m+G|MR3d&h9X7GDO`!)E$<W-C;dD7Sj{E!+=45cf9orcZdCRKOA}&sft~cBRx?~Bw<x=h>D)1M7k&Gh>#jF#KU<Jk(8IbEvF(PzxzjaP-~NPe?gxmogddAo#S)`WfmpaV^yx`OtykFlk6bu>WJ>^h~^*dX^J`e+-aKXG);Ayrsq!6FWkTTU~lM!9q8~>QH6NaVbS=tpC>uwwl4bn<HiSLvYTlvlWb^|$Mu7hTy3+Fu7b81c1$VrX2Q!^G*I+NHllRiOne<+Uj|h=cM&##t&P^&Q|_fEA+l@OcC=#9v$CKQ8+r;VFQBcWUG_D!WlF70ajT5rE&D_Q$sXE4EOE8tzx?RlK<A-?&PDwcm!R|bpS=iS(7N&QnS?<ZF6uF1P+!R#wcq6=(K~tw;xZGT#%k*IBx9|ynAH_jC3d>dCadEyW-$s!U&HrKKQR&GPwXu6>BKtZt4QuyYL-PGSMl>0(F$1}NXF8xurS-ogM{OBOroKbdCbZf*t>>=+KeO!)CuILC=d2Cx1n5V-(wynCIj~1*o5`%uBWCCZ|S@ke-|kC<p%yX#8~+Xr_&z51c50aUc?0M)V55JYc*CfNfgP<&mgwjpt6o(_yp^7NN(5#_C&?*o;?-~GnVRNa%v5MP5)-Xbju}j9YAW5rB~jNjbFg^h-G%K^HuBQ0QN7WZ}AvzS~<?=id?~)Ql>fV<(hOX4VPA<&=!2~k_bh<0G}Kp^N?V&L=)dVeW*PKOtP3D2reJnKt-^`D&#w1>Vc#fD`{#v`_`k0wIi!I*wHNa-CSB=)iswcb(nh4z+6IYb`^29l_oGx>e~x9Jsi2|J+eZLmtMg{e3WaSvZ>R%)HIaxw8R<`tIFO`VwIc9pq5HkwMVfqI_u}aHq$a~%moD+;d$yTPpPw*HsWXrVb*k(Yt5^x!UzH?7#qnbrCPII!=z~+#I}{lgXpVVWl#dJiZG~UI<Rul8o`MSHBwf?C~`^Ow?$)G82c@3KxU~kQ&BROO;Qxdc=<^_)g)G%mI{ZK-9T1Q_s$L&s>W+H3Q1qN$NHmafs?^5Q;lr2N<&3!%u;!-CeRkd+y3K55x?SBie$g=-J3H`#88&Y6)GQ{ZfRK)*KuHKhHWj5swKYJfmCAOxh8?>rbSc;PPg)}A;})Pqyvs~-OyX?LX%N!7#QU>P@Th+?7D~)8hHY7C>$XUOui!Z%k)x5vi3HVug9S;ha%&3*>@7Y*mnFbyOH-P4CUYh&Zq2asR!}IhKi!-J1@&>i-WY#wk&^LF<WKTl%>!Xt3H&)q_;>dhVET-ZL_l*o*vW=%Q<B9cQ-4LD8m)>ar@u6$Cz&?36-m=ZJS{6Y@QX5qeWNxHfb}*))cZ4pOzKAE0+1zn8YXM+bY~ycJGydAvH%+#%3E-kOb#SFh-8RZdg~zTE#jn>1F)-l_#qj+onjIYng7JroSS3At;HCkzI?)i&S|OU-f&#D7-Q%rwDIkjajqL_)6|7Gl8nBr3~xQY6;Zq_-=aLr_r*=#}hN<;sf<GyjXeJm^OQT{AUM0KJ)SG-gH}z&p#N^mwi6kUq33m9FGGNl~6AD{U1jIX*FpeX}fXJAITuia!EUIw9I6XxGPa`rkf~UE32Ax7u%TzQZoPVR0gTNEQ2Hf?It0Jk_M7=Y1D{6?C0EFsy<M7<0h()JKljRMgmC2`?prCI%RhJZqh)qRL+6T#Y!#x-LJ9J?zyGU?@}zA(Gj<zg}n;DY&M_DrdiYibKM;~@Uh<2<U^%Dt>rJ$r(UL7^h%(zzT|Ur#+lD`QY;7;qfui&fo)NgfJ++oK{d2ma<*;O${(Iltd|;3mgY4J&s9+k0YWc^ZW2SYSkupZe(d?JNo%y+*pIS>iiW;+eC&VtYnL)$ih4>G&{ga-VWDZrImHPcgccYrORgz{hC8#81!PPZ^9AiZU%)98kMafD&iE~Qv6@7n2W}WV#%7i;2sP;NHEYmM`GPEx<DS%8E%F66S=Pp3qp7i~$pVw*3{_LNrU_71H!9bB^C8Vm*&P<PM$%XP($+LF`wPm90lbzAWyWaNu{1Pb#-f#B!~ep>cnP)nbT&aieMT<W-fG9yzTiW1y$9Evni%r&D+Xzrs`t>$wau4SrZR*-U}&19p+QwZEFXZ`c$>~M`91X@So1oatjJVCo>`Vi%R;9~356L46wj|&D{wpJfI6pVE=IAJMzZ{A(|;3>>$CLVJSOQv|7~EMTAsOxn?Vd2yKGP-Nvy;*nJY4xKsBg0n1I4Bti&rF!2T(Y2z2$MjD_Jrgh{5l6`3VjHFMPB2u9)*Q?*uQVe=NQoK&CJUaoK~CQrnMEp)qx*^6W#Cs&mvp1ir#%_znY0bLQry1im=;i5n{59uyv%4{QAKh_6fe1J$K>695NGL#HVg&3&7W^sxQDDb^aO9{<Yl{tL7M|DohqN)C9nT;#@RAohU<c0tki=c8N>@Gj{pFShNxs|t2A~n;3^Z-tz5{#|lLNc-}<t(Mhh8!WOCN^jq8nGmsWF(D90zscw+~I7S=qW;%s-EM}zz_%smxSY)1sA5_DaJ~U4XU1T;gd(wciD%@xhp|}(R&x6Z`nq6aSD0j6h4@@-_GJ7#sa#%Q=B3V$55l2a1tG0{f8PsNbQkH>J<f_Fn4AVN18uY#(aL*QT(yIwGwPOXw0)f8P14dYHUTS#?Em@P*Ae`;+h&O4El<Xe)xwkW-+@ow9}-Z{8nuD)O%^<Zust6$xFf;%c}p(?ULK=QJ`-Ve3n)cnw9!Zypm;?xnnA^xBwt!=4PAsxR($ZpcG%3z44X^)M5qhk)+HA97^yS7!;W#&-CQI9lV@&7M*nQCWmsi%AUrwSB{f8)J_~WAPx!4N2>Ke+rg^BS<*lAq#R56QaR1HgcaSxFb+!H-jeT>2P335#)B(UZ3nDYY|CID40^QHu6{6OOCh#!O@{R#l`A*HwFhV>)T&mXH`eaMH8Yu#`5emLd8k^q@?bsc`1pyt8glt4ag3IHUD|1z1C}6|X7^NSWAbc}B-+Mtg&Cv*+w7isPQH?Ysg2@luBT>>#h&wTJUceNL~2dw(|g3m3yI+Ku`zQ+@L-M6+UkwX2MCO7RGcjg%A+{&;V3F*NWAi0KSjj@v0yD_G>&9}o24wUITp8M;r)FdOvrsDj=o37-devOmS?`0m+0qg;z1=PSj6MuuVY`Vd-vYMzn5y_S1|nl`^U>g%;JMdaiodKpNAd=h6u5<T!gW@GfD{INa}%QL|wP|7f&VJc>^0}?;lZd$F>@b3$oIg1CqoW80!rTB<i2?56PhC%0H}+lMlz@?dKF8EE+Jmx5%1yJN7tQ;i6?Iu&$wipM?TA`JO4=xyl>OK)1HsLVBiVdsqYkrdE{vS04oY#tTf$cWA*Fbw|9Bm!3#f9Z$yATczTH4vv84wV<sm!3-An|Ficlv9@jLdC+*x=bG!i*52!$I=)r6s$4G0<%;bnz0*OWK?8{fNC-uO29_KvBElpnAqg@ucH)TOj%{q&9Y?%_g6JV31qp#@ph(c=87v}<=+GciM33=(-#_M@>$Uej_nv!C72Z`x`>ws#+;h!2<{1C@AK(9dvlx}>Ywn6LG_x2rmKfEKoW((T;7fVgbR{pVhKuSBTX7wV?xEt+(sR+gP+=Ctbi`9`p?2w=%}`)uLIM4-0JeUCw(RyfZCQ-K|MXSNqvlHKY&3AU#Lh5}YK)2%ZIu9NajLqyW!mmcC6hnH1zgUiYBrmy^Vt+{&89eMqRHiAug+W+t@5Rn2Td^PN*V3i#@%V+p_!ZIQW3aAn*>aujrA<>yIL<XKwr(WsL0gF2R8LI%^<J>FQ4nziB#UGilo}4Sz|e~uPDFq2VZDP4rm<s{M}{1xGVWzyw7{4twMZ$tGmn;%rA5P)?H==6Pu4|>M<)*ayB3DQ?p}AHoo+*7LHIMa>F$>yXGUJg^jzt;XXAPH<UEvKZ3R<ebqkCASL#rnq;H|CL|BD#-r|LBj}fPk>U9O<N#-F-w3^fpO_Bx)b``7til18tJw$B#^qQh=1{uJzPbz??dBhT6m9oK^6^8oKz8rn0_o43L2H3bL22TrS|DX3)8}o0^ivC@k!ZX~KcKWgDla&8K?=3S>iNAc$Y)w0SMwG~Xi%6{-MkFIK78EV@t=E-v`CIFPDp|*^L$)V&m+&8m6Iq3GE;d{A62Kc=9m89jGLI{{YD!Z=W;!Sy2D>J+pr@4eo(D}8%;v*PI!<~O5pK11kAH(L$96s<EaV{EjhT6vq12$2l~vGf>`gP_azq;t1j#Y30TC{5|9*icJZgE>Zw(w47foOxT)re{1~^D8#Y05Z^M#Q_k(u!xY`>eI$jL$-~N!9`2~@P^UQp!cPuTB%y};@1_7{3T3!dlvXDeZo=?L5-nORqoN!n&5lR3VYT`~RWoA7@|DaN()+Fjy1?Kb7tW~RN3i*6w=CMmjfs8EH3!bn+TV$-1v9(lu@{>eSic|J`O0(xhVy`{LX1K+v2RF>}^XGYWVkHHRb%l(0l;LtBsjgV?L*lfWQvIp)m>OAg<N?8rf2di4@9EK07)A~s>nx>%Pn#uyEY%kB)QEra<p{5CM0hRoTocHPIT|6n2B`32LAHQgRgEFM+JqJ&)>r`J%*K6#Yyt68h|c4RUH$|YxM(0R^k`)>)ggzQ&m2UK-`P9pv%_JvKwgk_tI;oqh6PPGz_mzD&@v00TDXfHd=og>#C$meh<T}P_zIw7+|jTMRjVV>I$5y`serj0)5^H=1c(_M6BGUr_kx>^OX9rp=ni_5r|JuxP5aC4_k8so1S0}-SvM}z9=`BTqm<HPvx@t~Z!?W+-}}1pFytG!NWL=(HZQUmK^eINQuHF#N6eFU;npoNb6)LlMY3(c0-|iLy`Np2T^@r0+hbB;i|=>XOk6xzBWwOOyW(-3sBRD>xHxdrdkaYeR&*%+Ch;ir>9PL1P`lj0Fd{!O9+L-Qhq(C&Glqu`Z!V%)5*7+Ip}a?`H=Lj{rj@&38VZ&$TGIODPZ!x>A=B3~jn*f?+wyW+Gf3%Vf&Vg^f(KuJW^mp56Q8XfY7y!MhHIDL`V7!os2A4Vg6#ehr2U;_u{Xt{Q#@0IW~fwJtB7yAQkrBH!n#gq4ADlpC;dJVCLM=KtSNEHj>8a)c_oJ3$X|6p@$sSjnl>^aGhxSo22?;)24B?>J6*D3tdfX{U3FvgBEQJqXJ*0Fupo2UuMqz)<cMrIka@h>s@yX9T4AT9(p6sn=!V8ekCDmwT?|6?>e^&>{(}1t{qR$2!uIKrlaCt?s(~?mx+QA8a_aLGnO)1GM?PK-85-+I6_D2#<ahEhTc?V9t<9wHf7C?NKbYuTNGrcG7l;!@)gX18K1$mIW!%Kh|5{R_G)G@|m=3}LroCs(l<LxFkf-9O`_c`PclwC2|6?oud2P)NwPY8$x?!jmc^T6@s@DW`@%ZR_NA;sK`J3O_2VE!6?8a~W`rZqUpr|{!qKUTjCPth8{hFHIL8bC$HpQ33p+uPW!E>7*+_2(9Z*))Uc&G89zf6}S`&Ty68#bS7uGGYP*DK=NrO8IOG0{Q`*sb<U)o+Xlf|f@pn};F_m=`nhE%-Y;ZO`R_PJ#noZ`2y9B4mel^5iCJFUx)f6O(|U$nI*7ol2ZbZJuRiiia}AP5janr1=j&U<1`j4;qpo)QS=SFD1M`(2<i8l|$h#p`z^dK4TPUxYcFS)8XVgA#^zJNa0s39?P5V+b>q5T8Z23R-L3N-NeqX!gKgdT(8L~U(`vUV{@Up+9GMt#)~3}s#6TE*kU!Qt_~*7suW{Nrn*{7b+uxh&l6b{Oz7%Dbv4aYSF<^)^40hB-13XHL8-8HT!S~y#a2gsxh1niH6&VN`nebRKiMLE&%}h<N0Kq@^CCvwa@ZH5I#_XoG{TKp!VZ|o7_so#{p>e3wA9fEo1O7V<;y=Y_^Tfgoh7w5?a@;+2zr^P>M?v*9|a0HvZNq*(-CJty(BE*6ldE^*ayqGEL4ko5ptRjj&Mk9u_%N$*3<|XhI&GX?#30au))@9a-whwjQXGb(P-BsT-!P}U)ZjR)o)X_xzhvtOmA^s<ZOez*;^c*ZQA^<``5l2V0S$gP@hM2*Jst!Qt&5USmG?eh)9T81G;7^W|Cue?XBYVa8){GyCxN3*xNz;+=%LCZZDuU%-3i2>-7xM-98|XEIfB8rPI+Q^yj71#JcImQR3^rpI94y>IK4NPfzUYcCa%+Y~T7a!z+J@s7yBS$c<IV^Lij2XO#uCUq!>Q6jbb-XKA(sNTg!i4b}xFfFe=Zw89g2gPJP&lsu$-nskG{f#=~~-x_BGrN`6)hGRNT4ahse>=8W{tODLyv4HIvJNPdfsU=ZI3R_4GLBGI+V)nxFWnc>?6Kri*Q0z|Ks25g8$>K$pQRB5(m{iqEy+DyAa7RTWtX5{rN5TFV-jFe0MRMym-WzPaBg@dUOFf*+-?7eD>Bunk8eWO7I|8N+Iu^Lv$69<UE%28}YX+t$>-!OG4daK8hJv>q-2k@n*n;P*5yMXD*yZl*L$gG{9}IFG$G)%}>h%Lo=oKt-YAXY4Ds#$|q@v`Mj8_%5MO{*PHnLYcl}h?zu-+#Xm%`y?>R^A|zYyF=apHQxU$+RTP-GzJ*auRfwd^Y<!b%)l2<Z#wWi9DsZ$E_<hSyU`doPNz%gb}E#}-GGcSB)c79LV*1u2fkZsafHPS2(1DT9mz3;jGHwipnx5iHDlDG`JthoeOH*k7i|H6T-{K1Q6B{;tHrn2o_!8qb@gX8dLI*L4+*lB^J}6=^Vamd=RAMujid7YiR8ZpWxmOLvuA|4;}lN8z&(Y3XPEoOAeP7~9Qakw_DGQd#%e`K^L9DwlaT?^E+Eh=lQ-OM1J)Jx2oYI2)6a=L?r#H~;g}L00~%kd`_@>cV)nYA(J0+vyKWl7IT!c6Qmbi}&NLjh$<)aIoVz+s`=rnPyim2RMya8%p!w*i1V$^s0rJP4k6A+^ff!8_DqZK1w^*gb;W!heBQp^%aN0x?(xD5Kc4SJwpgorp`z)*_*JZi9n$>T|V{kQ(Bb0FRAo#cLG*ausGPPeW`beww?Q?I=crL3}douN5pvwVWueB%^I$>LARjPAQO}1^%8_u2R^Z3#2%F-xl}>(f(MCZQS-CWX6??G-J&9xb~Ed?S~NGH0^RMR)<^D!@W1kv`}YcZo<c|7@$U&vz3JZ%Y@H6z`uBIyk#zBSVa?>?ceBRL1$NgnnB+z#-dGTbKUl(vUV!x&bKktel%4xCyyQYoe<DbvIQ@G${eSyO7wj%iTmGUnz`ImeLWuMPYUb!0GBxC5%QMNYaLs4J3_i;*zO;&!;5JsoeW9rwi>p?ejL#=6;WR14?Yz~08nwT1Nhrh661*P8q|iFieX6-curcKr^PeEQ2T}?*2-NSbq8+HR0qh2&h_7pPIf_<WTer7;5X`8tH6e-u8yfKxNnp0nv1Z+%Qe`|V-V$xLeFrtik-(u<qeRRhbb;@CqeW2d+Zwd<fQx$~hAyc#D0nH#_nsiiVA<WgKCFDlBsA!#gnvXactaX&XR^fUzxq5AVa2NF)6w5$=ob}Vt-QDmFJZFv1@*_$8_(vf15)+Z^_ZSRvS$t<N7b`sI&9tnnT>zVM%-E$9ZW+qd(476c0*dlL=L)?99r#4NYIi#k1H@vJh$-mr54RM^6EwGmI^y=@yPj9G5G*^#r7V^xR=bLq3O3lKjlcb2a{A8im)c(#+iA)19kn#q<jD5OOuH|S^79mz-|u*&YB|KBVc%9_eB1alM;C#m_%|A@iD7T`HXpNb|@YY<#!lCFu{-rk4PYbadXWD+=lNJ*mHeU*$oH4816AIb{zGVSxEKS<`-}B$xmRx%w|8oj*lMwWd{cCzx35*vXNy_9p~vZHc`}<8=6J2FHTsM-HgN<^MqBnpRmf;ah9#hFP8{+P|r-ZkFCzLRdvZ$t*_Vzy6bG!&Z!SZxh#~*fBQprZ0B)W&yonE$?|?x&9H_y+qG%`waP}TmEr}dDDBnQv@PU>pLj*<RWVs8F`BF2oKw9uW9xQJse@YC1dJ1K&UAG1CIdpks2*;Hu-%OCjVj}4`znNQ$r`xTx=pLaZmLv7q3e=ju<8%EuQ)x2Jd=bD44c*(4Og>f?ogQDqP5Cpi<GbbtfhOGfBnxs&;E07A+Zn_SEVQGdJEF?47Yh=2kk;=R#!U$h~8^=Mi_hXU>mJ2>XuuYh=F_K3mvZ-qq}KGV!^`?ML~R?Yi#EP?M%b7`d(HY%aR?ibbg~ptz2Ub_rG(z{<W_FK=$lAi|XeO3))*w*dvpOXDRuhy~X!>bYtky`kv<Ca0W3x+gsYNY;XA$_X`m<@>5J-!;Rv_mJqT0M2;9+%-cPuX`Q|e2t`b9)DyvvPONtwC+VFXmMXZFYwj5Rqvhc~btVwsS_$5$_yD$gu%4^dn3S<QSvl#!lt4Ob#pc-T3g>b(R_GPBtQdK4KQc$hSRL@UJMML%l-DB*Sf$ck0$Snl9xMRPC(QTMKH_`XRLOOIwA8S?2f^vkC3RGyQHhAyK3LOIkCQOH{$N5xwZZSuA9*s+-t;s5dH37C`aT$<7j$m@16EHJ#PgQw#=4UmbRh!~B*t+jc3k~d+|3CI2PZWLtMJqE@XOciL9DpKiPI522h)9>>L~7RAQX1hES*EP`dGlQjklUU&^uMCMO@KY&ouLtVYP&Lk0eJH)MwYSK+lq}ufl4BKr27J9UsM8;#2b;Cl!`x;stKOPd9?}J;L|@F(PoV+7GTU!2vwbGh}(IRCQ%px@xfeP@%b_eg5_L-r^3fzRl7nX2n~1@_dueZgF$c>~ltvwb=6MQkVfWLJI`TEn$i?XZ$=pe!izc9l+A#9J!?QI2QOKZ(K<U*)ctCj3l7z>+@J3NnX<9L6?+mnJ?U>VyGXtGBKE9jb-E6YE!~IT9A}Po!f{}rhP1|C+nv^^z(h}*X&s>eE8Of=>H7ou3$GuG@Sc^`;u9^31m==LHuFlG${#BQkez7YI}}b$!g$U!5+c*WFr!QlGw<53+l>#<_9L3CXDe~HcHni+R;|72X{+gse)j?shM)!=|aQ9yQSWwC4z~;MhUDtxJ6rh+Fm6&rUY^{Ri%7bcXSWg5d8ytGApXeeeDG$&T%=dS>iZfQC9u9M@c`U`H5t_%m=M3T{){l1*8NgpMx`14o9cb?z*%Bc&Sa4a;Mxju12d)>DjWKx&^?O=WO!S;M(&xQ&{d)vIL7(kkWk2vT$9tT9742x*TO<upn(}L~o0e*-_tXkr3-mH7sa?h@)!Ej*hLN@INSnk`|EJ=$Tdp{2?eGE9Uy*d75Jp=JkQqOq$bX-#In06~mAs1euIhxbmwl;0=b?St(z(n5K+H==_SyLh2Z6XMYHo#<GCi)aW9Gm-eH?-T(7P>2Fz8@7LVYcK175q`Kw`Ve<XXmX=AwJIQ`dVb0JEQPG#leoo|hXG<L=hN(#;)Z?vWKj$(C$?qlm`;zSU2r)ZMYWvc`8^tje%b4tE>a9u_$$qhGnY{*+NGh5B`yyWV+E@HXr#|{i*+I;cXz~5hV-c8^JfK~4r`<4L@3QQS3Bo~O;C#T5oQ^4bREzuwAizg3^a1X1O;AW6g|gB`H9c%3D29>r7GC7e87FfpZm^Kn>~C?}AJ@nRhhu~EUyJ^@yp!Vr4n8W|kd5M-7Hu#OIoxeQk4i@x(OW+6iP7&*v{)~-L}gkWwoO3it}Knry|N+p6<p1Do~uHeQ)qCIT}dp<=igRE<`!yXk+Isq(rt2|SREkdZLt+Wn2Eu-@cY>i^eW3of?df`lFwY%IS#?7A41wBHlf5+N#n3hwLJ5vRF>=VL|z+ePt3-|5d*3Sgxwl@%^*N-Fr%=8o*ME=8-nlF%rSZH^;QbtvWcLtgUg1T2C<BJ)*>e~gua1y*f3=wv@ZcdaA#UNg=k+)mWv=V1`hK^n=f-9i93hdEb1b!LTMoEFT!D~^`+_oV3Vbgf}?aLBWv1`PXN@n#P=`>=fvbqR6jh3#Mf*$kc~hOL<J`j^glIw(50(8CptpbCD~-e*s4mb(=rNDkpv$_$xOqjHQc)g?OcEOr4@K5-t`Yt;~m)q#sY5yLDqGRH=T8XBTBwq=4I$P(%=ceaeE6m_hMv++lxwXFjCsl@()z{GRto&JXYzwYxdi4u<SmZ;Hv^}@MDdaRs6chw&F`EC;m*Ox5ivsENI#o=b#9{s<<DQlnZZ|x=G+4gC1R5`QFIJ3Bx3F+B@+Y6NIi7`AzgyhjYFwY<cfU4d;#I9cb@!!~T@bCk@g4!tdYt=+rD<gt~EJE=aLXw@5J1Bz2br<7|>D5Hsh(rs|oWLWVhhJ1|W*r|Qm<OPZ=>o<0pnpnK9Auk|!r!_{mpB?ebDXK;i;9!kw-7j9m0jztilY;nUwY3Ck_X9lmZUaaP<7fpx+c&Zyd@*DmC`cYil?2p#|i+Z=~_xEnO?^rv_m*n6MAI`xYFn5Gw`4S!6?tXvv;^R8Fzvq5q!a=4-*T#Z_d@}<<{^O(Ws2j0y`IZmagG@*S4#(_MvWPG+<>0MN9ph0Osvt<76l)K@)h9z3dH&QelBy)u$^!U9lHk<3#SnDZCKW+P9p8kK9ZpJ@d`$<emC<Bfx|IYrW~5Y9D&A3$qDl;po%`Cxt{FTYEkzuW@}$oaMYzv&56e@;UwTINP`ng-rxzen{dyzur)PFy6l^C0r*d&Majm7bS2^JFt2%?n0HC2~C+_`dViY5dM#StR!=p$OCCBo6?st6kkFdwOW-6f?F?eXFkAo88#O#r+lFqTOdw#0sZ)A)es2dNKdNzgKwbQ4GJ`W}i8yLODv*f8QaYq%?{1rVLMDza_a!K>6RknJiwK^E5$lHoIaTT`(Ll8Jq2dF;FOmtsK;@Yz$;n~NhmQrqKOt~uGl>g$>154yy!jN95#Z`+8rx~nhLHRcvl^R%IuB2R(C)ZKfUK4SZoU%<P&hgLkV}}kcHp_-m^g$=2y@nVpdtYm|-9w%N5GryUQ&oPmwPak+<<jTxUvYS25aJu|_+R^Agoqb4;&aT|>ZOE;MtXovg!w(q)_hx2*BL2~#$@`~zYq((cf8_9tjFesfjiC&g(kFjq+pSyY+KSn@K5I20pi>{vJ#ySM4TE0K4U2{6!6(D*4l9%)Y?O*{4P@;315t?58$&MOZVwNog2^U(KW?*#;rGv=o(i%B*{3X`X5shzgOk$5gfU+pL;Zv;u09bR5V9Q=EXkPGl{}I`&8I{DVUbmKF(gzA`yuW3$s-^TWmkT1Sd9R2b00zb>^x0NrD)PC%<jS<HOv*79QKY%k9f@iYKbAVpf_(Wt~~N5U{ItiLpaLw$(ra<PCzzC8bXDg%Kr2B5jI}(Ckx8xPYG7ap?<8Rc{8;;F>|U#VA^56BkPSlDbr%gdSTkds>U_BdL-vd+SXUL~|+>v49xH$)#3`%9POT4=HSll3;=^Gb1vbIdrdC%-1aD51*6wc~uF2%(vfnJAb2K1i{B6c8%JT$gC?po)rT4ni)rfK|+N$CiT>Id5)_P%R)UFK2#}ghcf%-fhkywkx$WjM!}U+8}TA5JFU`Cp-2f_B~TXl3P9^56M;!w0XiH>9NqeYHJY*{0Hs3YntX*VG_0|aJ%kb_tUw!aG;FWsJ780Kf>+91!`WGmXR-qqnV<gx<`Y@XJV_6Qweuz(<*P%p{|`SJ%@)^*xMw>pP_KWA)^oC1tnx0YvvW72p*EEyI|VmnB=`JcJr-2K#=e7=(lMh^pEX!8k>N=&e6O_vyK%8rNM}4x#CR5xlF59=!f1SVMmD?ria2KdpTuNLe)z7dvzL+RUF3gTR$EBuQZMsI=`l~eJU2=A5&82opq?=5s|U5hg|~vfCiiA%fySV_NkE+q%-Zjecg!)MNChH*2Q?|<31Na2J5fwcFscV^D#Tj=9D(3+M+_QlS?pY@>^ynlAo==cZOZ47qudpFqE%i!2Wt$>&vr|M2+qIv8}AN@3=|H?IP7%)ZR4y!L{gfh*top7c>nd+&-d%=cz)TxzK-zg2)~Z->#wgP{CR#2ALQ5Y-hW%a&!_d5am`=&*RRNbc%7wR;n>z6?z`$g%3~Ye`)|{ezrNSs{?QrO;J?tX;RF3zzxY?t!1~#*^Q+RY<EQ>Tem#5bU-X(JDtuk*#Y=wPJa~Nby-sB<^4CAD<QNOXO0-{tN_MeSvi<a0$(B@?*WvQt$X-K6Ad?vl{(*!s%D#y~ho2$$l#Eyw#bA~uP$Z@>7N}?Z_zzdos5_T1?_dnTlvQ<w`_MDxfW(9S3u>A5*Z&GPu0-RfW0-3_JM8S&>h{^x@@0x~xBfPC<<0TpivpAVQ?_w-<)U5}#pvagv&t{-1gCZ`jndk)%~$nkCw}+w0KVhqqdNcF%L`tp9mtOi@bf{&JL9Et=8V^TcAb)#(ru26UA|<b#>+mCeA9@W&Mw$q__KHX>@KET7{7FS3ewz~UBj(u;4hxq>{nwU@<lbozH8(e;#&|^2$sZ+O69te(<Sc%*Mdrz_EYbp0MB&*x-EM@&VJQTv2IPyVJN?r7qOhmRcG(afBO3$i5ct0`|0)<jlVj7`vCh{?$_VAsbCB*S2t^a70<shx~DJL`O5=>zq&~OqRXC-c8J#p5Z%(a>pLBvp!m-0R0f@K_l}uH$xm;N)4)i}#$U?;^NFMb^yc`HQL2^0l95K2zm10J(d)#WLcfM`+Orb|p{ML@*SB-;PS5Tx-kt^_+?@t@r^jpn-OX<dw?Dle;c#_8iiHN~Y)pccm*aHUe7N+!_ijFD;~CDLOPGyGxO(BwUflk9Q$d4$a_^_0p%UL*LBo1*X9^li_AP@GBNX$`Vp$|SCyKa99nmrE335|UYgs_4NNIEqAeT<MMN(@G(BsHoHn5j;Sr8gk&5zntL)#uA8qMGavJHB|XLmj(9)re=we3Zay~xJ6E<|;dNp5&%sIM5og2`J%>e<Yl7ra@;w3rjpS%dB9-BgKR#D)z0Nhto&Op@d5PZ}T9lxYZb+XU^?1uupqHuk;z>PRJPbZ-D;qJfH0`o|3~Owgy0OrRcUrq@EtYoX;eh5GvI>j=M&@aqV_7Fu2lEw6=^*Fwu{q2;yE@>*#5qflshzoJO_s~c~o@}l|xRhF@=^71On_=hj4var6A|E;lXd^F)c(`X<8lvP<G(jjc}1NEEQAA@PMUse$;aW>|A&a(e6D7Ro>Z`4TYvl@wtF5u0ZDjfEQmeM${yIj08|8<mMd$RgcPVQ%SVSnP3thd^R=D9zw#Dud-%=`~kj4>4v4VsN4KV3`xR1SwrEFS2ic<Y}=US*QYyQr<2HQsxe-OKnCoaAc8=W^rvXZIU?q2QhhOEwK^o3u$yRAD;I4mf+q?nrN%Cc@QEJM8iaT6T3-A+yyzuf$vzc&spRHc;jK-i-yA^1X4aphyr~s*B#*&iuU+j_Nm4R(F;hkF#>ljcoN;u9%f=tjth;4gPKc=63PJ-!8`3uhmnZ-u&pY$WaO~{yZ~YehnrcS%1#r%@fxXUU0QHKB`M~;i^;<x);@H?iOjHi}#Cj*AM;X3{fF%RtbQ%)I}M_mvI~a<X#zO{PgC9-LAfjk<NKhYI>mI$)|b0JahBwp7^VmR$s=B^EBQsCiacGOS~$vgd4@M>x#?S&wGWIa8YRaFFp@H@;w^RwXuvFY2nCpO%*~A6^0uWg=gga>;>$0#z{yv&WV%InE8i^jnHWM!T8B;qG$|+pyj`4I-@xEIU)Z<2HKM2W*N{ZDS|=qfi9=MAhN(?<6|?m7zMrU0PjR_4O%C0^82=M6Npczn*@0{@F7By!c%NIpf%{IF2)TgZ7)ay<46)n>1tnE7~@BmT=~=PKk&m3+>YY6?a2*4%?|8+OjU$l7rChiXNZq>3lK-1wI@AuaLt6nK@IDs(cD5++lso<>QF~Jn254dzGu7|jMi5gfF`(|-&u#y#PU)2v}4teEx2o`pKL)q8u-;6=hvG9Hfd`C5`5zzd0L8ccW63atBpQH<51W~iVLwh9@j&<`2%ZbnzNEsC0jIJ*XBD82ev{=P1oX$RR8@S6%HEEepJuU(2PBzlD50op-k>pUwsfJ8ru071-_Y@lo#`!zZbF?sY5w(=_cz?UOY!b<H4%_e1~#P;f;z7>-%K-EVJl|tDUoQKQ{k$=s~3Zmo0d5YiYr2wUhqft87^QMfdOf;b-0HgsB%duG4})QMH-Ehdq3Gkcc#7J(MU(Et2>AenaM$)(I|k;xvh3F;Anb4kX@zTj*{}vO)T~3bTy<JWs2J;uSWhpl6+qAW9drKrOcNEqKd{XKh7gT**Sh$wlRTPnP%5S=;+ckC($Kb)E14O#}_FajtI=gDUtC^R0*R@+D|POQHnWad09F_8Qa@MxgGrvSa$?52pGnsgIk&zrnBkx%Tf&7WG>Gx0U?wjHiqn^_c={5dkLY;4K~C+Lwi$cjJW-hg8NyCbnqY8%V)gwTT*k0XFA__2EKJnxX?;!B=#obVz%<r0QT)6)_lF@JtQZOLGz1@1CY`?EDW{@F0J2)CbO|`tv^;>dUD}FXuDe9`(y1Um66Hm)hHSv&|kv$<`0uf=sh3y2~2!p=`g<RXLEEtqiuY*m1D)GorK#_LMxj^&wgo0Ho%5m?1u=VTKCqcib<&Tok;^_Txy>{Uv!0f+%}jy<<-=?%oY8+P(3hcR|udYqS9ikm4Y<LqVUKtP}a2N8~obZWYAG-%|uY(uqfAsUAo~DpJhao=4a*)DUw}9<OhJQ~(oIjP!Yb`Xs?35(Nw%g2RbSuOLFo?~@`PRHkPP)AN5aX1>7!sS5$RETR%&9p^!s|JB0uN5Nq8KYm$+0p#yAN1}=3*_(_?E0tx;x_IeJh%lgr3t`SZ$Fgp5s!(09Ad&*nkpl6G1ra$7(87CYvd7!%j18SHau^ZFILdKR`9vGQvK*$+x{4&lFwOu{=~iBnZC;|aPHc)rh>b*6$tcK;>nmSuLyDj!H}1}ayQES?X=D<alSl_rdyTe`Y#JkEqNQ_6LLC@IsM=OwIgpO${sn{qi#dn*9l`*AMi}sw#0Ed7`B?wpNnwe683$Jl&Tr|y?ThZ80A%^kNkkH<DF@-Qj=^1mR=Guy52W&<yueWTb{!5}fe=oqpo?;1Y}kUZnVIQLSkMR5z6GivA0C>?@$?k+K9Tr$Ln^lpQbdRok7OyrvsIATxHm0^KO5yE{DG0-hAIb2gm*L5<bzv$3U;SI{sx;|d~lySDc$?_-*Ug}tDnVVSxV**gaptMY3XcW9eo|~D;$%a!qa(D9H4_l=Li5unrBx_DtJSf9p^Pu?OObyRYnqOu3|b!06IzzE&(TLe=c$2QhQh>G0=&{*O=OrGJ|JFQIr~FS0msM<&%8aH}jS-NOPA0Dc<BP4}m6qAV)`>DB-@BPqlT1{gb3ME&{TC*(IYf&wd#0u4OWto&Y=sbOzL91tdu_T<{)9e^FO^G9~)~(o&xMffXslu-Hke+i>dw?7i~Y@n9OskJ9Lj<HboA!hih1&FqZ6=MFE+7_WVqyetD0a3||(0j@J%7C9B5nVTyeMrn`Jz|y*|#oAZR_~0lu;^`-PVm%v@cnCb2%$ybn#!W`GD@GMz8rS8q1b{Ue(Nl+Q7Und6*WSx7ucgAwrO<FG=L_4-6m7f4LeaSi#p3Dmc7PPiMoxKas&JOXwz2}Vj_>KdJYr7gz^5Zg$#9fjw<G-~cu>}Pe_UbZ<VYpQ6l)ildZOu;&dt(`Msw5T2_@wlSd~YzZDr46V5l9B_}dd+Gt%8yXr3S4H@&u27x#Fb-P3x{Wv{2&VALNMc+NeE)ehQ-@_DvSvm-y?Z{*8+gs}y`KEhmhKP^*s)V|K|W01fuzH#ypP2HLk?Xuk08c04*r)*okAoutad61jys^mc`1qe^)K{%VAPleRRJK0`)FiM5gJf7JQ+8^>r8hxnbtRjKjd?qz^m4+g(=EMZ`{S-fji<7LDXMAmyPG_`?Mh5K*aDBegNV`Q!Xr-jM>Z%*A44z(JQ6kraTD(>@jMSfW$)fgZPjxM=;f4vlz|t)jAJVJ!sOe5!1!<!1p^W<sgWKX#lC<PLJ~mBP`Y+#O+IA#v`x#pMHMM|^uT3&m=ag;9JvfQ$kYs(v+O}nm<1<=McswF*OMKe&b&Mg<!2USx0vv7bt(()dF*IkZ0dui%pbF0xRI_B#SE|e!N1JIFfdA1mE+6ODWXWfaakdW?cLcC4A*e*(0|eS<Q;9Zi$L@h6Cv3w>0oftRu4yW96V9)&3&4|bT{X_5lHZBWR0sP>Zf7Ao4{}OOB~VU^>kX+z*Y>aq{YRff3qMMG$xyzp`Kw|3z><8^0_N*q++nf@^<NQbOCz7XQWv*^xoa6^vf8&XhMTPR5|B!_C<GPNF{@Fblw)EU)N(Vwqh_RL6oT~X^U7$DQM{a|$_<Co_v%aI8Neg?RCGotFFLs)()(*I>r|%jEkk+RB{_@pjF?qASvL%25NR?-tWv@o_VMmC7ws7yQ)8swbBxUOYcO8N!jwM~v})U{rEt@vR%d@T`!@!WNTGbpO4Hx{yiA!4D;X}?`q<L}xbnQ2GMjk_-OM77%VN}(ubIfmmM9zFi`5`D&1#;!n>3Q|Erog%E|h_u)&Y*G+{{Lg)1O7CO(h%6?;WW$iG0b2&_<70j5}s}oY%b5HE}oavo|Gw;YGCRjsanp*Nw0YH&E}HdcrUa$849o0ty)!H%E(nk94yRAlLh0Al>{6?l(Cjq;hnCBwK5(hniX0trzvagVYq64+pmCVKQz^UKCsEDMmbb+~2_L;|etJ-s%nFJm#l)U(RoSOYdyp%InkGIQ5z8roPJ8D^lz(;ElrDwh5IdX2>4=w_9h=HtC;Vx#?^ua;Gqms=Xm$e|Bt9>Lww$qW?J131!MN@vD(8ZK?4)z=areszs1c0P12bIt!y1oy8%a!|a2BUBf86nm^hy81O2n`1JG7E059?cQFm!6gtNuK6bW%xAgwYx@|~)KaZ8GvW3Oo=L7Os0(d}z^k}OT4nijxmcol(^PWa=<(8zPgNllSW!AS^Dy&OLNdO7L4yS?!q7;;Si0B~6vj#0SDaylum=%xWAo6>t2Q!z6OgDmrJ$>9ownr6W)0Ai8(pCQpCTJlxhebLTRfruMOGjadMXFn*Uh(U|e<+^-fRTicL^|~xQmLE|b*Zz7f#eL$6jp!=pNT@AzT})G{Fs+~YdZ{L&4~C}Ss><@g0+w`2&oajsvFb`4=SV#i@2WYS2sGE;9@7-PgV7r&M1<oQW2+{7}nS}D;_~r3*{`x0qW%G(tI(SXi5pO=%R7fhVx&yA{C$sQg~t!4V@4_9ce(`HaK72pZ}bnlQ2C3UZ-P<2Cuk8D3D+;SlZFD3Fjxb*A#mqdAofSZ+<&5gZcDbJU_#DjDUf`-MZ#!lnewcM`nHu_2lpqtgWH>e_uK=k@!5Hn-x_RDx0B5;B0|&B!c36dIn1kORG*>Xv3mcD|JwMdB)D*tudPaBz`vaKuf)XgtT5r(IhETeM=H)i-ZukMMmg}N?xSIz9?Y?lY;Zs-!9;_5E13HZMk3rOpY%EpcRCbYr_5(4g_E5aix)BKP1uZOEWhIk4l9no7$X5XOD;iAXK%`JF$3;_MCZ!Vyi=4#N^KALQKl4+V@J%Bl?k}!2~`orgqT^a77S=d1L!j?$0#u^e55><CWMo*msewdAg)Z^eD5#g3dYqZ@en*VtBQnOhB34LSF;{Eu4v6%>HMOCNJ(!=#g8s&BY^so_^JYT=sBcA{~>U=J}ppKw{E4YR99*$_9DxxXQ6FU5PG16^55tHL4mSRTwE5-|1SJeAlL0FGCVfL3F!qfUbl|tm_31dxH%ewphIAIk?C-hw2F>Gf*(GG63x?qm`d-q5MZe1gc;r_>{mTO2(^VWRW8*#{vdTJe4oQgNM{)T2k#fNA{I#`cze()&Rv}Boq($il4xOq$OCS)Cttbq!In;?2~2(`UjRrf^2Ty4wZ_kgOksfSSOHj7eAuYw3ir8aWwwnSFOP8qsUU~Nr8FH%RdiqTrd430yoJo`<;7Mff=95H))-~1Vx8A+z??-H$|Ae&$mA+820kgWlBaV<~c5smr8T<oCq`WoSxY^qM$Bxn3>*`ct`Io@i@4-AameMaNa#B!b~Yi%8WRnzK~k%iw-l39D|Ccbj^nvm!}==83pEi)WW)ewhB53Oux`!t`(lJ!1t9#D1Y!uh4D&-@!I76`s?cmzmD+h2)|Ncyi#GjQenJOVZ2gdyi#HO2u<2oHjGy`j1SC)fn*<=ks_0{lxYUItVIX1@0o6mjU`2ykiDQF7u4`2v={~)J!i)7{)`;M&)Bj3oZo;QTz<xKU|bm+KjW&t&z0eye`ox<P*1E2b0Tci`Np<-e@=>h!L*=f<ZqE?RHe~#JnfutV@5aOXH*i_jV{#4R_*gldGTxJ)EWMq&3ycIWY0LeqvWkm=jO=pvbm^505aW(;aZa_Z)f8_4dck6Av%INjYh+)Dn)58h&~Fr^TZZ1z3-nmc$z|zSUh9W@Hb}2#Vz}@IWzI1%%<WQjfS6bX!w!SytUlAR~WKRguxWH=s9VIcXMXsIV<#2q#5ZJJ$D?LOzse!Kk?C%Eay*AaD;ml6Eh0z;O=lwhYJRVd$)Y^f<t`jcAj9&c>2@nlI~E+`zw<43rYw79DBw!<+n?hXBY`I{EXS$hx^Rt!7h8wwLLPZ%&8%66L8-;=lD*zMG`W<$eT15cMb^tJ~_s-=X~PR7yjWjGs(z|;ljk^?$0U9Zxd)dNvZK7CXL&~<^SAEy8}*WeL`jBM5NE&XD4fTK&6M!5i|?4#U;Pvm)cd17F!1^$%NG-0JizXDQ^vHl<YRDh_EACSPmlgUHuq7QHwlVpz}#~rKT44<l}ZY68(yKM>w$d!(QxN0CrdA|AbFbsIPlZA_LWy!AKLT(kz0aqSeyDfB>>~jAWnx{%^V8LPZG>fe6Y7SW`6666_Pw#)H>=$L6k;WMx}4T!qHfJM3Kzt5Ip|>NRVmHM>3u1qEbo$I)Vs90n~GZUWf_I!q|Z_2_cwiB3VYII2ZqyAKVTxx-T0^ym`7wzKeFvM%{%R$TWe&xs&JXBIL0%2kBEL?Wy50f!p>M|pS-D2K62kWiYoa#e$dqdZCTWeg+*fGkN0i@=dfIFDyh6!Q<DXV=v1bgo$1W3>z|wcMNoG5m)pjDiF^RK*1lHOd>6Ye<hfhy%Z2J7Yr(4{L%HS0OJwAqyx+I}2R`E5ePIRKw0TjGITlP+)gZ01KNc`qot+9DBq$?a7Ii@{Ibe7p)Cw2j}_9$@<{p2~~4JmYX9n-l){Y>S(pZ))nEFz|NLsSk-L*JacH-)UySQmDPWtp9xO0k~Yt|=SRs}o0}oO6_&|p0wzC}9mVy2Vgwk1;oR`P_uby9@4P2*g#6z8Ek6V10%#KRTi~{D^YI<vYw9qo3+X_q>yuo7Z7AOytj)G3=f=>Y&S^mHqGXf0@TLP`17+2qvLqsbVZdb%XyfrBbMxgzRH@d5w|SQBov@;6KBaebZrpzTdDz|sQ_zNj3b*M=$mdWh>rqTW!K${zY@^@1D_w5c>ep(K7uJ^eJwE4<4D>O=Z3T^FGlcrUi33q3zOB_3&SG{2*E=scAUz#^&FexP^Akr9R}t)C6NMxfB4#8J0W6^@tuiZE7GnouoQ(b#MNv@?Wh!P@;ss*yncO}R*l!_27ljdM-W8J!x!oMZIKe`-=s?)oOT`5|G|(CR8E|#{j60E;r#oRGZSzh1csAZnYFA*|s4)j^A)yBYaF5}EU<UH@q)q5+w-uufnp{WZg-ZX%<N!5|y%S^4U}Sbl2*7WW@PlMDcykcW(5dSab}!#T;+XYphh1>+-agvN^CjgAh}poB2+GV0e=gCE=09NwN}`EWA8<?_mVt0i(Ci$vJp9hnj%1rgd}@x3H{Na>y(u6g;R;;(y0NWH!PO=Y^S_zreYN)WH;75ir+MIfKcMq|H)7j>%w_AcwYPErddAD@k!`rIXG3)|W}}*@otO-zCY~7p)z`*^Q4_%%LBA0KSFx7FO7FL7`GC#tIrd9p&2Z|0MkYo@upL*(DFMuyIt%UJSXdVeiZBf;Y$k7klEC>1^d{dNPx}pDG7N*@@aO~j)~JZ0dx7i;tuevL6@iMP-NS9RXl~^FQo1Raz0C&?gt*s%=UE!~x$NOK2#Zbm)dR~*Q5W?k$MpN|&&2f2JhWs0Il+w79c{TMo_a^XAz3J*u!s1FG%O?@$V;!@dbastwyAd(;}1fZNVL5`Kj;vSwngxXLGm77aTLnGAy<Wo#}GETC^+csJ2e0RTR#8=@9>pdW8KK_RLel*OwffLxTWCz+O<6qeEBuns>0XVP2jg=oIra!AmQ1j04ue|acgj9G4S2uMk>8d&iE37#p7(%1Z9SLkAPs(T@ZprG%7yoy>+SNDHS;^sZvCYW#0sWYjMmXpQna(^3=15{4~#tYzDCiG{S{WlUg#g<Y=qFb>c2|)}+B}#)#oD|0Wh;eoEh=_n4i)yx{V@USZqWl@(}oK{bH&)j&!fPA_2eJ2<>>Ber}p4HsJ=iB&_26K>DwtaseYLU~XDXQNh-G;6}DP)XvQ9ky~g5CGO`;Zffw6jK?3Rs~ZI4Itt9>%LQ#A0~GtatAESVU|;?`BBY&S*cwGzRauiQwBLZ*_w_FGFA8qQ+eW|T5_j~X!-4Q7XW5~(<%VN#?jTH<zj{#NqkzpA~;-b6S_i#QY#17m@=(5&qFDwf}w=1u>~3E17Uh{pZ|rI#zl{3aZz2<ky~L%U{eP^{ECZw6lhAoV&>_-$$R<3$hk^?Ok6q<=R|ije}%g>C{kkMbO*MfHL&>PlY`rjj@y<bV4r#(vj;`VDZfU%f`ID87U<F@H_P0vop@zhIu<zu+NpP%C()n+1~}wzDIX>B%5d1~?P%mDHNo(6*vr3<Ti-p>iC7>!H1@4Omao0=JLDH#_RAS0Ccg{DQnuw<e-s<l5f_+m7u}+a<Lc7yh7F#L^^pNX{-TAqGYF{Hf?|tYdvplC^WfIT1C)29v^(VJGRKZ1IZ*ii-t`QtS^+y1E#yn6k!Q<Z6L}(lN6dSFj)?KmF(_2C#N-1D5zI*(o#n+>CpN0*%h);j8H9#nxq^J`fBz_)daLUF2=&_TvW2`mXVVL=wDR7k(rej|mY!`Jf3jzs3pCavJuX9}hEPxAAkrQ`Cu<14^=HkI{*tfZiRN){`lzI_5OOjoUNLqa;XH*LXCk3F?;mfR^w07U`<a{E6p-fyzeBw29|xE-jV<IKvGw=&Um=~Zkj_`I*6XjYBm6qTuOs{l>HGq}hR^Zmuc*#fROc(I^A*+kit2ntb$&cl=LE~F-v`)PKk=q}Kcwi#1a`WF0^y#(PHu0NIB-dT3Z}qLGG~e82B3KN7lK?!&_-{HW6mVuCyd-2!->BYCeXWcb+a4NX2!XGu15xHk`W_XPcJSZh~f4*=O1Ax`pd&8YIY_NHhs&e&gRdcj2HT7)0Oz51TX>)4TtH&x>C3C^w9;5u?#PAX$5#WU1WcGk#ngs;99RPkI;qL!QM)gxR~BuUf!Y#@$7oS#pN0F?#A^Oa`?L!d;#&Dzfgti#=jYuQ$)hZPc~e<OUf9{wZ^<?G3-r0YL-O<mtO0RorxJ0oZ+Ob<lRkGrU}kh*gh@*fvh>XXW@>VU@sH%x>6#03XVA3g;ri8>z=~D-A7Bhr}2=pPsbPYv6{aQ_mQHvz9L*AOXt^o3j=v^z*DHpE12H}RL{c6FeUer5G1q1e7gLT`M+=_IyQbO%3}8~72F0lo{_%`g1z@xuh5eI`buWd#}~bhvn3N}u*u3@NV!R}?E?Ln&S8^oHbW+aq(6I84Fxmy8|M7alHC8S|C_V|)yzOluM1Di_)ovaa?Hig@kN*&Kb?)%#qipE-+^Api=3-UzNSp2{xDmphVN8qIva<<Uc~ZgRo(<+INz_zzcl-kG#)=cVe-p+<cc5e-z6e7_~VQJwoyljNNz^zjq|fzzYyiRcXtjpPRlZG<ELe80|zaX(IdIg*++We)8$ul!<pW6>5MMKK0W_6j?eVwW#F*t=8d0y*Y!8fPIY!8yzEMD-JJovxQqFfb6=ef*7;3jm1qXjcueWWa<ms=y3TP!PQE|8hC*%<LV1zOtrZ0H`IRrjC}5WgjaF6uDvl>y@lR?Y4M}Vs3`Pxk-d}frDyCITT})pG;$|RJ2Xah8Nj}Ob#PkhR^}iKj%AX#@y`L>mBu^fzs0Y?51L@t5fZo)m4HOED5_quTam0E8+Yt7KOb~=@Ma&yiT2_Vt66q{ega800ArHurJ`<NB&-2#w>Fl)muz}TY!e?SQT3NOy8-B}jq+Yyr)TcTaUQW(5K|nDaf-c^O6op0uUO_r~q(~z+R6!c)n^AWbTmWR7h8Yd?=EF(wqE8IrmN;T8SetwU8N@vB9uGp|#dHJ%Q!<T)nEsxs=+y#ZhW-Nz%0OuGs*0Y+pgk9q8I=wQ$v9IwNHNu7UB$s*U0oSu_mY4(m4>)FN}dAcbWsm?)LRKAc|d|CBcBpOp@uDAMiUA%HV9NF#^J_Ebbw+6P?Hg@FkO1`YzeZLtw0;B+?|Z0&KY86M#6f*yq*KYy*OVJq3h~a3hLbhNI{+(Yxua+ii0+wmQPM>a6QRBAug!sL;`<-v*!p7PKOwh7?rwJz)qkUbeL7n`?JdVNQ{K~dHr!K=b!nz`ZCk36vryiHlE@roS3n3W>jw?lZAw8&X~WzrCf-z7wTg4q{UUAnwt3-VbsPx9lU>rH(UP`yJ9xZsnCHjRx{lx3R_Y|Zcq<{MS3lJTD^ojcv$18d^zrYm6>Q?j5dEQjikmD27Fks#}y>ALQn?IyewNJEyc7`M3d&hI`E^KYC|V><oq+{KfR`0n7N9awq$%HgRFV4Z8>vky9ov$F=kA0WvZcq80S%o&Nvi9Rd%lEj8d^|pwL~g$g*Y+1J_C@^j?jQANO=pM{2Rst;gvTk&PmNmS%_dHY>1<h62?#_Pn!^2bC(X>fw@fj7zFUgqr+(&vj~cEFcvuvO$Y%Q92O6vPJgad>(P&Cn5hAe0rCt|739fIq?7X0y>BPrx(Egn>+CT267A8#0vutEN#QteW?{Z_5oo2-f9JKjHuE$L(jVbXuAWcO=sNzh5jyD0=>EJ3BcU*Vq}iQGKc0?bHFo_8JJD#7#KdT;r<tYXk->&ps{#MU{U6t1pP70G!`4~_1J1nV-b0qR#3|XC9u>>?u%L&k8WGki{b%hD43Qa91`|hn6%>9_z~Il5zz7x+hq*@zts($YXV=5u}|YLPwJsI($>dfgDr(_sYG+g*APo-q=1!=+51rew%XgM*M&H8)U*@=c0o<cZbS_R>$u4VBmGN1N)!5yXy}KU(>oJ5grhu8>*{=3r%9d_yXC@~naZ?o-0rV@=_3j!<UOW!U8Z%I#TRGOI(=DldTly|Pt55u>XprDjQZJ-7c$i4RTtSz5qFx?lEeL$`;+e9_QOw+wD{5cw^N(bV2^=0*60?{=1V!Ag6tqSV`wKV{b5bb19B4AJ4WTTSoZxY-{BfUt{pTieA|Gr*bGKK7}^48ML4C>7`gU?#bDUJk1GUneL_!eK7J!U{$PH6AYwfa@lQe&CT#O44-j6?SJyUBGT5;%4Er*FZd#7=5sz)X3QcPbW#2jl@-h3(gZrBECl?<7s{0-Cm1LLpA>SO^p7)^j$HXHN9bWGdCl<YWO<m{!l}Ja<b3D{ua(<OH%*olUHlo9qFT?&kDEF}0b7XuDCYG2V@9O9){_5E|w`0)@auUg!fTNe<Vu12IeE}pY0?vs?hxVtW7i(${WS2B;N1kYNThzJ(mpzTa07GN;*oD1lK%_9{*OYoojGVzqEtSoD4IB9{Om9d{k;Lz0>Sawcvh6RR`#axSqxLHOT#11=KTb&sz#5<(-18w*{ZZE9YY3V1lY95+(|z~!PzV2x7m^*6*!g$te}Cu8JNc*V$JU$Xbbh_SpX8x>2T4Zut~LH03>}hQiW=XY{lnyb7wEb2oU6_xye?cK92tGj5bs@O+FXP5HN7;M^YK{U)X1H#P`aWmi-U|@^Zdq;Y*^b|vfuZe54JP<(j<_eOwp+Qf2NVEgI6?2?`qbnYwBuKm20qU2dxqNLEe>|R6ZLd7N`XCE-AByiyV(x^AAa&?B9)z0j(J`MTLvt+s;en{++$gXxfR3U;nUS<mvdXLQbk9)A+mj$=O6u^AfH281$vQ7>%S|hQ^RTU6F`n*0NogphdjyB2eDo%&Ue>%E#>@X#bL%uYhN#fByLi_sG?SRHDRWJ@*O!P}2bQ(2~K)0|a0?J@d|VRC=}9d*APk_@OO*^>7CBcG481&F8rxHGQ8fqkwEjNBOTrW^%F#v7DTjy@~F!`-kyYC=D+;q;7Erwog)$*PFnQUyyIy!&oR5&(4xZO0nccn2)Z4@A7|oCdgXfRj{7O@$C56V*&Rhv<-Lau^yc2OnC)0`73_Ky{FOf8!2Y^2Bh)CcqAlOqn1_zll()?e#-$2>q>%D5NLDC>Gg@~yA2U0xCt~tEwD&2{0nc5W3rHniJOgur!~kkpmWnEmcuGY;HXHm@+A??X-yajH8rrKdfAt4OK}x`X_AN<W7dWuL5;evz-JYPRvAhk6@0UeX@xH}=w_ANiXur;-vA9p2+a=L_KwG(0ZW3zCeMKlS1QCU_o*6Q2ISDynTAXLSKe;{oapqiZSrgZY$3J7G&W~{%htdE$B=@nuG`a$``OfA_`c)R59jkfTcC!S=DyfuZ}T2$uBs3Y)bjq!6Rb7w!FtczYD<bCe`(?YJq9FuPNU__^CUlkMIBhC#HG$nWyj~E<Pv>1SM|&tFmce%SOp?A5(Bg-%Zy*reoE@>7vu^KpKz0YbL|Sk^;xtW;Ov&Zkt8%rwiW8ErWsUuYvHD1mewQ&c!5W5kzzJD3z+sr(aP&O-c~)1dKu;&3{Dw%v=Vk3rhUxd;GKF)FEQ{_Q*H7h2UxD4fVHH9x5yt2CY`Y(hkz^(mJlRx{R218h6FDikBL$~8Zb4#RxHMLgYg5OOn$6eOj8W>UwpsW`N$SzseI38XF!x*7a{J41``X-#HmbBdPLo#*k&4L7E^q`yER8CyVz3kJG(G>9`w;>s!daN92VQGdWTKZSj;obWF$Y4gd>`;s?fBn6m8!CH_$P0+0uohq7<#4crmW6^2#f_oi9Ec=D@P$W<d$VGR)ZEcQ#W8*ybSH964FLKe!eniuY8qj;d2qGMs2PO-!&0cp=S9{V13s6jF8@@RKl4*Q;O~&|U6Rl_YsgbM7o<sK2Tx#><o?9>|eRve}Fez#noWR5!B;5Sh4*HzE;7=|0hiSp5%>q2x_ZOJ}PRz48DwRxG`g$<&JS_bhllOi*$vBgTTG7%LMOl3-4YGvR5Jyeg$^(oDKXlt?%XCyb($G|R&;t@KoJ?~RmjieQ*Q_>+yBl#+cZ(<uqBc!FA)b7i5R-N~5xcrj^|QL621y5-U`93(>+ixyBIGgLG&Ejze8DZ?#DQz#Z)APEFTXHv<yUuUF^q2M$lGr2m3pOWTfp!>?`YOnhOO%--^<b417i~8ZW2q0_L6A@ECs#Xf1N&eXkzNsKZo#$QEgW0Q&EK=vExA9G+${b-X3aIi*ZlL_aWHr?%n--j5EfPvtb$L=W`MW5iR>4!jv})Ms&Oh<1h>fese^MbC#<O`S$0uwl4fSHkAC*H^M<`5SRwcj4mH|D*1O1+cAK}_6(~maj48&kv3)6tp;s)t$G&B}%`P(LkFD;H~l%c8-(C{NRCiANDV{Rzrh0(|#kv)v|4tLZvc06uey8|_D0MpE?{{6kX1FK)0Om(t33V4I2NFG#rdOe-W2v3h*Q!7nQg1{pE>)tQu<3Z1d$$_4>NtI(%s2lV2mJ*^7AnIVzdg<6^j12Wg>;-3@9_4;otsG9&){<1Xm^@U+*78&y`x_onHV%)iUr_pIheC(Rm`fS2is0|Sb3^e{1aK&TMC=}U!ob|*f$w<@*}=<4rUffx`3Bc8$~FDE{N5q2>fUTnVgJN<?!$Wr_>}In;EwghX99d+ck}IjfdHQl+p4-B;5WW+p9}Ci3Kl*Q;8&9~`BZ>U-?Cs9xNi%#a5KPX(rt?FEo>(#4=-lJjB~}>>pLfbaf_y(3Gj#Frs{wY7L_M(fB`=D1S#6Jqu0u@stgJPyR0z3LYQA7eVmC&4CalpPbp!(XJdR*q9?p1kI$x=!u;wg%qM#Pta8?~81oUs{Na~gN}u<DMUWoIsTKHZzPb}rW{(C&Dy(_jS%g+Uf=#4WijbagwujvTV>56ETN3!NBl!cX_aH;5%^v|xQA=#dmZ+K&X?7NzK?C(a;d^cUTkcS6i&3rNq_B@59}UVsA6v5f9UNwBMP8wN!tAV((nWx%C_2oID0-%}1At8V^-`D^KC9phl^*|O%f~*@**!3I-mb-gHIfd8aQ!g<=@$+EsZbZnQ#}DQ8Xs{t+vDiHNh~}+B1OUY6j-yP|CH*(`R9o@S|3I}MOaAO`l0CF73Zub9||fkM~w8r`_I(%aMT}yYZ?#X!CE+#N6F6<oN$WYk3<I@QNHdTUH@3tBJ~Js@m>GtFNpvLMSuryk%t}tQcDEqf@#Q$^xKO?+`K`sd3kO%sVFek%yuC3=^POkq3!797RouO;tBqwK~-X-cEq%R_>?T4e3Bcxk_N_^5_)o^dos4<z?B~Spl9N&#*jlC>Ax!}HUJYu&XjC@IufiH_#bJKfz`ETXN1XKBDl35N@HA4LCJj06{}Hw;nu`fFN!Uq85=>p#G@3U;T)4GOA@IP3?$0YV|t#xwx?+mf+b4!6W82uBj7F?YD-;)f*`b;GPPGvjul>K6U-HlNx03R=xs%(vm(3XfGyh(s`+}5y1k>*Gvy?I^`*w@2suZT;vS9l2}=l>3_Or*L)O8lY3lI>8)m8_IiX@)_;A=@R(4LbXa3Qs<$&I7mu^Vd;_{6QOSnFRu%O6Zg~HAmt1Z(oQIvxgkc5%2+XL6xZ~efSTv)?=8JN&pzavy*YheI+{kHy-P?Qr3XmfB@S<C}gvm&z9c_Qr6noNell;~mWB1=x3P&ns;xtWvTsl)_rIRE;c>fQw!%GK3gb9er-`(14Q@zcB;yX-ntYfO{0f*g4LCVSs5m2Qw~!^|GbRn^{@8WGv<K;tX2;JQzBZw4)2NY6T#A?k>?gI(HU^Um(~P|8UUfy7U>m2V*XTgcuqy#`x6v<{e>Jx$hW$*767!3HO1x?^L7A!VQ|)-#rg3amiRl2@1sBoyN?y^SO^ubG~Ls10?@A4;+mbua#Ts|ap^5>-cLJ;mO(VilI>Y0PS@0+dQmdr*e}QDwTFO5A_)$+<86gU_kqog=-q;(hY!fo6*|ZDirZHor2)C@tp*<Ob4)v1T5!5vT|OkHkvzJGC*FVh3&ct77Ut8LW<^d_uB$(f;QD5A;acI6zVd5>%-MMCD|}-OFV9*|l;Yh(#?EB0wv{4vkC{IIy<-8osz6g?UXRd!BqKF!>U~mtfq4e?!q9p1)Z%ipMj!sr@9`H`vz{(-#WaXhZ*#$SrSYE=hwShESlG%z@Z`9!3;>Hr_muDHTr*FXc;J7?q!OU_<&uC6VTu+|%{*epO5;35w}{?Wg{k#`*N7ax!5g(jrVVjQ3SE(LIxx%*mB>7LTveG@gF;GilGx1N4vjZ1zta)ZNQswV~i8RlZ*ohrL&{bT@9Zv<uLB7;_8V8UqvRCf-#H-NG2LagX99TlA*Br2^_?WiQ(@Ye3@WkArWAbi{k+<4(apsLWVmyW@3i=hCpejO|**c5W<?0hd}Y&tkjP6x%tmw4K3A0Zz=}AU5IRyx7cwV?wN9xL?=p&+EDp<b6jpV`)_(IG4<!9gBeUxAeeqq&GOQQ-0yOxR9HpaLUF;Y8YGHg17fEl~P&93cua~XraCgC(cZhMIWKNEIYlM;fTi;G3-suFTWelX)s~WcrMoCc-Bl_Sm_vNTfC%hywMP$qvQ>z%4r@=T33((eygJUURJX${US6Riq<e3<#z#rW`$VBcO}rQzwAKs=dndaUw@Cxx#H>n49oWv(hx=A%t+^CE*o4Dd2L|PMI4FVn!ITt1prRTyxi*quvS;_u#gs5(6tS$!#V$uw~Ynz=%T<M9^szC`wyCT$Y?YmFGK*hU4!zUKz)o@OT>2z=sZ$C5E%gc1ui?l3c<A%Eb)(ZupXx>h$fc%E)rEe5rKIT_oeL967B{2K4g1<ooRqyiBL=3Mb>gs04;E4{`oI!*i;A#W!QSfIEY{F4jZ$^H->Es;0M_GX~$bdirx8uX|!VaF(zU$TFI&O5Ee-Om2slQ(KzL;VtHqrwu1Ti_WiepO<9%wY|%ZpFIYY=jhza3N*B9>_FLN>%0687g^To_b_XlD^g@65>8E=0@2366PS7s<XwwF9@ZvCkevjzN9^n<M<<Owx-b7`JhC4-lxl<q|xnvVjJGvO5Tr<74jW0&&VuMIpZHOz?UC~@;2PNQM+zsv#rc|Z&6g38`aQ#l6QRybENA%D$=|eVC3F6_#Kc75~*2p!+4&-s$v!54xN5hJ65NCEA`&5F|(B5$mYF#KFvVP7#tnKNT#eT<ttS*elp@59ISwFd1Xs1{qose&D^#ns{Yqw&~udW%J0xoQAIY=gGuX2#_OWqp#zX=lV+SlJ@oidUMfA7@>LBtK0a!A{dDl|2v>I8O(S}>Jpc?Xblt12NTe0+-BP(^C>P|9^J<Dwk-C{3IyR4#iF$Y%rBqOgxx64haE2ubv{A(mu)nntrIRS8c>>RaJS$}=>7S`B{8qzSK*fVYqmLNv12q$iK~x?zk7+eDUb1vYG}sw2FBj;-QBjawDKGoKbzQB>5C#0YK)EOj1|*_M4@Y2wumc5uEhBmjj|X!X9*mE4DP{kqhZU6QEP?e^pJ8s)D<#K4q>E4ixrzecX_C!O%w{(-jdNRo6iNJG+Rp7-nWRs{xbM&W$OJJu`@hWP;Y*Rsq7nzXjuI}K~0Y^hnc8c-1$C~<)7X5f~}>K$MaRglFjEHBJP4j8Gn3Cl49Le&|R99z7(q%W023*NBsWKhs)QQ(K<573L$W7#ZRQ{$aLe(^e#Mn0@<BoEoJNpT=g*&7|1LSs0A(NKBzh|$@u=$%uiNS3%^leTKy!CE5lnF8X5H<qXd;str&i7RhjyNV?UHbc~`@nPgzVJ?t06zilj#XT#xgjx|_Igh@WpIS+sk`XMm<CtpvI$c08WjqS9SfRXPA1i4ASb`-lerN4--v7h*Ev5pWmELo^Z(Nto%XcKxp2~OOX6=sow@QK_*wpGLAiCN5t)8pk4W>4Aw}RKQU_sl2F5>$Yyl$-EMRXwFE#F<^b8TbwOIGlJbZXzTaMvL}eZ*>;*XtN}6rdS*Osge%Vqhc7gVjZuu4TJiNz%U*hda2gxevm<)z{{4fN&+W`PEeCT>Mq{JAT;s>QiQjPc%TRO~y5{csot=C94r_dZ5JG0@<?!OkDC^UPT83*jA?Q!{xoPzNUe*Rh6mT!5x#Y2KejhCd@HxGlZQ4UsPM;6U%47PS*lmaOA#|x**(7!-K5{0r;aJhW_s)w+p6S^ai_39!01X$n5s&N0d_*!-=>rZj)}4><kZyIVqVED*|C#Z|stA%;VrTOp~S-Pj8o;lJo$-w&By{*1a?yoFtK`+l9JSpDe1@PKPTWTrC@ySUAzp{gT<8>}$Vy0qpKTVWdFymO1Qhk^e!a>MkVOX*=_MHN%BAzFS^l?oi(+B%0NX5vxDpLOpSz2_cwO?Qh{iQ<`w08;&^ln$Ru_9(o3?55x#}jUk=pNa%?@2F@;i?U+W%MyKi7vC+Yv@2JSsHfLbbimoW>aIkS~gDNyYjaChBwxAyKWBJJ^w8Cbb5%(I0^XwYrjm>-F{EC9Qkp(m)-{<|pJ8s=vGYgKr^$YXH>u7CV0hB!)`-Z7*wh1GyMF*Gl2%EpBqGIc;O&Bi8tbI$6nyR!3ccx~w6r)5>Ex*>5@o@zwVPN`v!|EbMfH9;wm_~&oFYH~|Gf|@Sb~f*EF%3WJ92<iq0B8z{5#Rl-_ugjTa_wIOO}Fd|8_X6xjN56$W^3yM;6||%NC|0+p1lw_&(inJ)zr_=Z;1dJlbZnGdcZcgWFWpA5vPn?C(tREL0;b)<`HxXA11|i29NIP9<S*+HHhFCvTsW96|4<m5o1cW4AM-At)e^KjBaI!@<G)l*YPcs_%;@|tqTmbWyP>;K_7Sj@!jvb-#Du)q022wVv~g%_O`HTqWmM(Ql1gvGx+U*dFPwn%wmpE=qXeJtr>Z+?oczZY8(YYBHT3@qI4J`Lqr5CiW0N}S+~%&v|fm|@X*#oC8GT&nZ{@irt(A14*ynqF8R|Q{1|}xGVB9L09eCt91AzWLU9mj)S?RVgQt(i?vc1iVvyL-%f%IRP_nEm3$xV`T$lU>e(iY%241~0km^{D@oj;vIyOdtyd~wE-2@SjVJxaac^8pR6zD0M8&Xr8g9SZzeDB(^*MiELI{44Jf7cH`i<P;fgx~N3ZZ*oEZV^>jD<G|99V6kxp*@oL2t$Uie;{R)I)9N<JdR93IA##95#Cq9$8nlcMQ01*3<$SIJf#CiWe^Go!aI^yW4jF$^lW~w3x(0cUhS{`G?on|Es3fv6`M$9fmnUxn~H7?o%ulSD0NzQ^dvhp3B~y62zuZ<2N%3)wY4yup$0P5lZ#1QQhqo&fiI9YXS-l95p*B_8cZeW+UjpJ8=F-5g(#dAUjr+zdBgc69UtJBS11T`{|wn{Mz^LFF_un!X!$a#2KJ;I;=qrpgj)ZPm;6IM{u5E|6tWWXcxB^-sa038=kbxqHU`X)%~^J6nHk#b@DP*9dc`6YRCH^2p8TI}C3t!vbjzn-vPj7U(tzuad2d-HOl}5~E<PZF%<nJuc^45I5hIC`Axi~!njhIN#ey#_M7T@)GQsdLhHDDeikK@IC?~P1NyG%)g$+-uf2=o0u{G9z&UUajK0Csnzm09nZq3ylhb^*6g8G5Cdf0%&8u;^WCmTzmo9*0f!|nuPGIf|>uu(dAGkR{NRYK%X=qO%<c9CtSvR3eF7abnU0(p421<el72^_CX*e+YkuoE##Htl=sjvCN(>-+Qm9XL!q(}F_QvnwL~!VkgdKG`Ao?6_955gmPDZ!J6+(Upzmv4bnMQT<_ut`coQ3yxy`+YLuC?9W`<#gUaHx>e{Eiqqf?KmS8Gc-7V5#jC-Kv%#A>cgo<!GI&)Uyk(I8Q+2q)jZD^_2_R(-cl1oz^RlyEIAjs~F&^OLBR>hErj)(l@48?9U{OF#$xpgdXMq4ox%#@W3Dp)3#3>w*pK9TNQsv!-+w6HbKq)~wIN&IlB7#_m9;%ki4v0^!^gMDpG_z6el!K(BWI;hT08MNQGvPA341=IIVjKawtlnf-C<YT<G{HUeV(g<q&K>}fH#P^dPWX5h6dX2%${`6@4T$VclG6XTJ%<(3c+ZeI@o7+wuo0!xnm{E=e%g~M!qZB>VYk|NLfg*hooccNv;giQdt39?R>tszfnm@VYj3*VGpZ-;m>9Z|@JXad8VuEq6CIG6*(qBTE)H#Jrb-rW&`F74d&-soZR%KDwPow6sUGEw!~r~Ccs^>>K@7qMht5w-9f`RQ3>KrI$o_?vh2WN@Fu1AFssU9jL5i1Pa*@c3D!#&1IOacDG66X!i(;)z#UC-c*E(A;;;42aj+(JXk)Rk_c|D`X{A)z^CRIjlQ<D#!DICNyUn6YrEW5_6p(WS~TW-GD-iS&S@5FbOe)$*-Qu#~&lg~j+1_Hn}eHjo}I8#|?Q4|vmt$ai}M>8?jZq~qdtk9=}-lQdqqbwp~231Y08)7G^a$g5cMvlaiCdQKBK|NH4ccBB=h$EFj8VN~bEHJPp8jriU%zPm-Lwr*D)b`OJN}giNB{qpfMd8;sMD9wOTv;0HD?|uOprRBQ(ij_tNM6Y`=C2QB-XRT*W<j{g0JgE#)UnE7gnLPCoz|xBqcde>P5g~2vgQRJrFyM~{X}+c-7_5*+>!C$`ik(_iWc(_MA?TP163$SI@I*PeU7>CuIDB~29_K^4V(-4>3!d4D@s~a$_^iTU`LS1XpjPkOgiOZ_ztJQgJd_k`(`t-18P5ZZTMQB9gOf9XTh!|<s`yi3{_W*mn_%!xg~u{!S(|h*$67<Y=XN-ME9q8-y;k&Pl96#dsYnwG#xwQ-P!&I_yze!Sr>W;;l$!nhck!oK>#*pqa0Y~NT5du1h)DI_>XYwmxu-M6^VHAmIIYd?%N#GMZe>8$lrC$6TBw84K1)%B`2;|lRBy*xrjn`;^Cs<uJQ-^CCQAGf`QmcEV#-+VmKsJ-Y!AQ!M_EYD#blJgRw(XUN(zST`UC`tqjzp8}8Z&Gm)C9tZ@fl+Lye{C#o(oBxG<Jt1r)H{o0c=^cIKWHJ_DrbEB1Fa)QFN!y-mzBjG}HvL-*PbtVtU3{%>fcx-Ui$D7@sN{LUDun<(XVWfMeCh`C;gT4=)qgd)x12fv(C1VhE2QUsJbw`?~=?XG91|>!!o;SsW`%rd0vKo7mgjx7<zRlG!R{4?lqS=LYKB_Fj>>Su3N_H+AWxo;G^F(ij^H(O50no~y%1>rUgfq<307>9+g0B*v5BRlWI>3%TJVquOkPoO&If{VS^C=uP)W5THzdyiOwX}*q7_BR9ofO;!jYchB?+@YICp5CYogZA2%GaS9<IhfFkimSmx7kgbf7C#jI;am-|1{Zo@F@@U$yAlw11}(`x5_ZjgjB|FOlQMw=7+F3BnS`Zt36~VHG+ma#NFSuIlcDb>(6?Vv2o{<dqtmi=1s=pP2M02&3||0P@=aqMQMQ-hced18h6E&tlC*s*O+%BMN0}&Acn%5%_GB@u*PEO>1LOlwe3X+M369+AL$C2E)$dSEGWo(!97<}F+vxO@onT6wH;5~Ve}?jny(gF#xp;%D}E$}WDrDDI*k7U%Q)n`HePi3l${QfyGG?`EAS`cZ?C+`&K%G)hq3}gun{J;Y=nZ=Jcn^zEOUKPuI28Ho0^KYFj@1AxjhkLA9&5N`aeGYEX%jjlv&0UR#EnTa+bkKjH&x#vkcGlL(DQ38b8!5>&h%^8+a3B$eSh?VyH5?1S|3F3uabiHZo6&2HkXIlqR)pdkz7he{qQdNYoR!TZQ?`W0QaVy;B~o1CRfE?e<K0gjxCXD&H|Njc12Gv7}PFd8Px+=3z>681;uT9bwFLl)08}r8$Dq99_wApfF@<j(C;k@N)hSwjjndM?6n+WIuFcM67HT1#gVFSZ5?`Yd%;@bMR5``L_(g(;t4-RwJ-hdTuh}nCy5js{yk5ACA50EPv(H6!p2Sh7M~7eAiPZL;Dfn$1kuNWD`5H8l0#N*@Bv<tp>(<R5CDOgO6x9kgWR~?;R%WNELORD=k)|D^|mgbCaz3Q}QhUh#RH=K^ryknp-lHX!a4fTgz|^m=^?~j$s00gdU?_RWcmjUxo>e4(h}!oGpIpW-L+(4{#nVz=G6MqyRfo15(tp>$3z4WQR<1GIeW&Zh?*mmtSnnp2i`p1wcZ-4kr6BE9EO#DE!XMo(>kOjv)i)>EAGLY$V8QhKwZ?g6$p`$k>At<V3gTtK1upPdK?VMXUh&8)UT2-XaHt5+xaVa>(AWM+0SL#J23mB~(!)4xn;bvXEFC22q{BNvIRh)}ydhsW)`NV!Z<L+Q?u^ogbCyv=CW6ta>Azy_$U`fEI($s}$VXkjuXH96qS99gR@QGbKi|rzS%+`|>qary>kH7yPJ=S&hB(>;c0LRB_bE(1QG@2(N@pAlf#X!XT_pQTdDh|NIel94qP<e32~x-L)UYaV#VHfp&o}#dl1`;4<w3jCz~q1-k%-`fL~YxD+q=((m}+WIF@X8WBL2IAj;CVy-qC*0^UXwn2ZmJB0Kn+Bg6vjQai1;Q1_=bzTI&XpqltE0A~%F=lUhsPfJS(<vjB*Tj#H`wQFuwZ-JEHP2r_8$HcqlQ`r_M$%UiwN7A%T(X8q+SnMr4N?m0zKYR`oB8VpEF5kwA^d<`BuR26=(Eg*jTP4<rwQ2hic}h%lfJDw{S!|Z?VO}M?i<`!Bm<qQ;{)IcPUxMwMc-9k)9;*h8elbx93s(aMpY{g4LI-A&qQJoJc2`{e~Frr>g!m(EALj~5TW8)LpYIYq$ExY-z>C!+Q`@xgSGXJO{h6Ou5>)fZfS*)=&1~Uok;v89zCuVEMJVkI}v)5S&J(>Kit$(YNQG2T_4uTYKDE3xr%$w4uK~AEE{30U=*TZaXFuBuCBUDKTEF9uX*Fn^PB+cj@J4{Cyugn3zQJQ8{CqOs%)VqUXrGpN(v|+AFT4>tN}+fE^K4MCX!!7++ZEkyFzHcB&`LLctq2its2)HzwXOedB6NpvXZSx<zllp6A3$*;sR|<akWP;L7uRiqilEFTbfD4-BA;e9+-GcV!zF%Fm72J*zn-|ME6pC(thJ(4!E-4+*KyhJAisV_DjX|j+2-VJmCFyk6GLX;~&a%=Ye&c-N9rKeCeIZ-wv<i5FW9NPy^`Ee9q1)$K4Cq*|^#=_^R?o6NhEtamP>H1zfNp?^>iRUUS~nbsT!k7ho(}5vIfyJJNBPI}L^8k<XvQFS_4`y;%If4L{~hC3tm)o<|INioHvx-KZo@pB0%XAnD<ewAi2HV;nZFZ)1;iEC8S_^Qi%CX;>|JVGPUAF5<vkXukV_sDN#Y**Of@<3g(@GGrI~6c#NolHi1(MaVnXaf$qKHcRLYI=B`u!X_Kp&B)x~i#9f>4*Lx*W;g5m&PHMwjG&)16;XX0g%u&T{F8<s1-4k>Vg^u?<acWJ66ra>-CbZ*YyB$mpx-$I2LG6EPcIO0dP|RHF=2xZTDs*lT3q5U7AB=}UV129^^r}hp<r74DBomi8rJ?2B-|u5jZ*0MYS5wdQ)^tS>dE378_f5Sa9YQ1=OtUL@|%5<kBjnmo=$37C8~kQ)QYF7=sR*~V;$6jpIUD$PV}2ZPV1SK660s^Ld*vf=44~xO1;7xGE$7pq-69U*#o37q~H{(If6ZXpy~&Aw^1@4aJh>015n>Nf)_c8|Ir!5_mM5$qK<hp<Bh3E1Day}7DdPWdSIYyvc4p_gbZAVHM7eLe-)Et%2QaAFC4&K5l};B6dwY4lz14o1F+@{L85PYH)|SS^g~0KX)I%=U_CgMr%!_|iPZ9TlQ_kBFeW{YOlhQ-Wt1~G+gM4<%ZowQx+VQBu9IX*I4$gt6wz&hfT`T8H%&BML6w)7Y#ZbW*#T&z8Ms=$?|L0fo^{e>Y6=80qy<wx4WV?>MdU97HE&oP!BxuESf$IQGHumwmzP3SHcUxr2YZ1*?enJ<ur@W+F=P(H`oH@;T5R`pamECJz&hud#YH6|<dJ(HsKYSJ7u;54i)?m{RtUHVShVj+8ia5Lc9*jjY@#?KJg!l|W51FT6D99RLW0r|S1OKvrqL#I+Lau4HHO86N(tFUcHY!6JYj57o6KOW)pM)N0=Rp{G3bjlZY(Wq)PVC);%O=~5L6M2f{;}CIvX%3j`fjR8Y)X`XA7h>e3oo7eDr+O-??jRE@-OYO2FJSpE#D9eIf4429~C05F3pj<;6p=#)Le%DIbF+C+gyCWwJeLWsj<`&Hq_M(;H^RTHZK^UjD&oo19U=NbHHKGWi=GWOO*uRQN!mAQ=KmQ39_Ai+{zZ{VBCkeX&-pzB(TTRxc3V>Lhs>_Tqm)_KG{ihHPbSlyDyPnDd-)6okeXwH55tqGSJVVx?P}?+gdfkaDIH4U5nk>L`dsFjc%k1jT%x21T}y3z!SbP3EZz(u#FzW+!O_ZyKUfksS-sH`=X?Bn`e=D-jB=r>H$Q_R$KA+0xY@WOv$H0>x*u-{k+VFE{f7QqnJ{Fbw}8ru4-!F9WB{hseC7s^r1GaN1>F7;fW@%u8jN7h)<?;U}WH=6h6yQ^~(D4sGHK@-G<hv;52YqnGdgRrl}s;ZL~JiIHc+5NAW!z$u<ik_L;bhbZDYAUKcelmj;8Q$|t!1A}cwZ(_R|(Ds{#2M2~jfnC6Snd-di7Vv`e`@17nQEU88IAC*tESgH^O1=+AvN1C7QN*@dBQxI8uWbY0c~Ds7YSF5axUzC`n8XZ-6ZS_VlFC!*+kA7gi6~mD(YuH*g>r_J*hx~Zum%Z4_Rms%kWcB~a1$&Hx-s8uvVy*a@rRW+=5d;nJha`vVa6iI-fzDcJbX>S*R14W=0LoM(Jxv4OlK+Bu~2Fw0aQ3Wdam|at+XSexMDUt%4dO7+Op78c|!sxLxq<@Db_YNgQ?^(3dsU(fnX8HI|U=;+OH{r>lKQVaA+}*pp*`EWBA+BGujbUm@hkF9VRNuwN2PtDGZ*EM7>vWw(vGVOr^@LwMS{F#q^ioKL-Lxbw0;p5C4gsOG0L%k)3_sczpoBC9(%g@-p{o0~6<@mutmjLLQqgG7}b;TWCR5P894)r%`_stz6;IAn9@3q6<M2U5vtc1Mhu!I4ZfJyb+Tv)H!UC?l4p;X6neJY{aQb3dY3}LB5O|8~2bKNn0*3TB;>P6<KI%@JRDzAP5&LP>9VIGlvZQ(YT_xin<-;Tl|&z`kKGT2D+d^dz*(GEmY=d3Du8m={Y$ld)p>TNz}ZcBbm?wg8ssQ#x`U{P8HKGa*y)%F9xK-|56u5C!+(2=6T5DL5S9bzKU!Q<9RGa7)30)(1K);EmBOF?ONQ1aR}^qk(`y>qZGyl^qIqyzZ3^oBR<iT6%5zRF1a}aWw{2m0~x8Ovuhi9Lp@UDR$gigk}ey);3m;>`FZ*LjZsipxoIw<9w!K%iL{8j5<q85nCdA^Lg>~A8ch-11tUGR&eJ)#&ljO}!avfe-0ns)!@_nI6xR;()7n*)i!TI;_HR776J=@nRaH1|GVJAxD6SsjiV!mKI|LR=mH+c+2ahg&c~}LGJ4wNh8uBLj9;3BJhfozR(rDLwcIL~Ue)g;GFAfs{SRDSo_LTa|Ed90j9nd^CS4b0~1O5F<f1ekbSf8UmqR=1l%=@h06P6g~u*B-UUC*|-o=1@Df1p}lO(B<p_(-J}DsRLC5r|~+22WFW)zXq?EiFj9RdPCU86Vl*{L>(fRKM>Jcy-zU0$8gVXA_F7f7pLxCpwv$8&)=DyZk`X$TN>8cOuS`J9T2_Yk@Nvwpl7qsCxD^LqRbm`@lEQR^&5*8^Rg{>Jg|8L~O@3XIv0QqYW(J=Pe?iifVreF)^Q~2P`c~Nr=i*I&5Q1(IDPpimj&80JtZTqvmnqfJ3>?6PI^|!}5ZLoAwydkFiDsObg=U|MP`<+t3yC#d_PoNkCHV_wH>|Phx@Ttyt2z>~Nzp#CemOOu*1uI<sZ}kb2m(!rKW0cB9Wt#|#%%!22OwwYm|X9B;I`iKqY$*HRgQJ56rQd6QdRn%oAn1qK7Gt;5X=<Z-vjO+-SbcB_za7K3)PCb#H^h8;2CMxR@{=yL;AQE7Ff6cb%^>vQ{<*5R+51)~Ff>%~<tx<}mBDj3}pisVVsAaMi!+SAs7*Wth|De#0ih5>7S{}?M1LoiRFXUtk};NFU5ux4npS+W9B%lR(Hd;62!!2(vx9FbvSwYT=Ia#bR`;3Yj+$f!o<e1`QwE02~x*bcvZK=&^i+aGb)bbP3OaIhN$#DG*9fwx&7<<=+WAgnE^1962KVk8TLWPOfPD|-J@b=d7n-HdSseC@w(_GQ79bPt**v_f6t)Eu`hZ^fx3l8Vi(P_?!^<*Krrdzxc<L7Xvj7S__yw4`94N~kL6Pf`u7gsLr2VaVOn)F*Z!Li~(cczGGr;Z~5!Omu3Hu$+VPI^z4(SBR)*HTA77nj-3S)w?5_ys80KOys<E6%Or`FIt?dksjEHsD9>665qE8)Tb)G8xaBj-W0Y<n&xY!OLG#7N9BNbY0AFZy6!FNQITvRc}LhCe7i!DcTLgR9ZmPZelTne75YN+Vc>LXq$LU*WV?0p=R^@7j5CH0nJCuCc6|z@kOs2n7z6Lj=5Z?ALD<rGA94Jup2-y=DGLTKQ1<au3yv@aAMmTn_zO-t+S@=481XQ|!P=u@Ldq$SI)lfH>0CNt66YYdgnX<%TA&m~-b-jsB$>G$d!9-QPYzB69_)q17EmF_;e&N>k*XU;yC*qp7sDs4BCA!jrWOrrE=FX)m#n#X6HM@d=*3#newfl?Kv3}o_8C}>s`Ax$0Z+o#-DBs+&D2`&_HU;bP$P}m-wWHQ@(wP#B4ZvwjaZ_s`Mt=i?+ZLaF8B^;2KcTU?!W}c=cVYG>u$-u*W%lOy{LKGyg-%ovU!1CHa30rG>o-Z?SO(mE?;|gYrH@q{BxKR6a`eX6iZunw$s2GDhx-X4q`0zo<s!$*<7(asH%~OWsp9EUt21XIBxJ+RXeIXI+Ybs%J=9ljVyCU>j%v5Z?TNG;-S?$L(vT)lR@~W-0%CU_3NJo4t6sz84=3QeC8kcLBdQYLbpy>UD@XlVAc38K@X1Jy7iJkSqB}xJV6g^RqI3~^@#bp&TrN{bK+O%TRb6boYR{nh72T5@Oa?it@-D}e#94m5G$WHpXw9ESPd3ZO}_{J6F*u#+QDy?*%U<;Y1_MlQ|`4ROeH%Q-=qEhCaXFL7IlVH$+oKO4CtKB8?$vSi<B7UE|<2@8rFbe)7qUF&hIJAf&zKW-n~R_K-6<&9fO)ZzCpEoJ5q)QU{~_X13eoOso?;Y5HN2L0v-9-@=$F=fgA@Drv&~azw=odvjoJM@EZC}ShL?6ZHjr~?X!CpiBJw*xhbso1egsPfdPGi?^26Z&0GW+jUh%QWWm|eIIRs+ug#O{U$9*^o3hWIP6ab&uV(>!t&P@TZzGFc`=EjlaJcw;hKkxyQC%!8vB(>*tVgXNQY-_Q@17_JJhc7<kFR?)9iORtkDwulk)Et;1?tUfuT?MXPY!kCqXd*;CaZE}WTR`|achP^y%*AljiyEciie<WkKhw}h5y8tI8@8oIMo+}REDSGz_fWtVt0ZS0oP?8!Q0E3fdP0#cra8T*#S?&0j(O6+CsX=?wBN4<#u5uaId)0MGm+AnGbxIfIa9&sf^^xy^h(Le7oJqyu%<MU)qX8PlbfGObE44_K)@^=R~R6ZRl|2_fIwz+Q)GQjE|q?m^>0Yd+?2Xw?h;)xgI$TMH}0H`AZpwOA?(jBn?4a^HD*G;e24ApsTSd@@Qq%*dVcg4EJ7y)Oyho+GrVuc}g^Gv?V~DvMY%rREO5td5KCKX$aG!sl-<&Oa5Tf*JL6w#X?L@*DI(;4~G`fP!ca6d=cGXCYp_Cnhob}8cPIoD>@@KillNa8NOf{zLMMPN@B0FH@mZrJdSA3SiLpBu)*5YxWZ@YA4|dagis#~lW7xfqqaQ95iNq<<8Z2tUZeQcPtB@+a>06I`MWbOgRNhV=)I{~-!kr+n(|0hPVZ>nBlt;Y_PtC^tKptc&2D5PyqcQvVrsr|zx4rH!Jh3QrG~f4ofnJ|{+uzQZbatijBlP!g@BxK><QzvG+dV_y-Wdbk@g8>*Rz&VzTb!&Wtza&7RD$9tv{m8>dt$@NDVu+g;DgN9e6#=l&MTQ7DePK3oEAL)<}Tdu<8}na}F^=vZif8DN$6N+{#as639vKZL8YO5<`K5Fm{RU@{Rx19HrEXF~8&B+rB}R($<N+1mpqF59(7PGIK=1KynFpTs%F8MbQ#S(aIuplfccPW~t~*F$x3~E)_U2qffr0v`7<nDWnE71^Na|`kV$OO;{0c5t;S{f3Z@+=okcG$6n1K{)qSiX9Gk5fl3(uKla`wR<><D4;rsI=A2b?Rn@BXJo}t`@4>NsFSc(mRvc)Y76>U4w4jj&kOmD14I+?m6dU9aD*+@of{BSuI>-tEL<b3hlm?O;2#H5PAix1cAVdg(5(E-0I*9Ro-#^BjvmR@&z0clfpIG;Jd)->Ks%Fiab3FdX_n@rtk-8DQKj9`5cpQnuGzu5>IeX11e)_!-=urzzP-HVmdza<|(kuj=R_fl4X7}aFU`abNZG+j-<b*O4?jldM3`BXSv6?l)9r0dfpfUW~HRj$`Pm2@gUM7x@<h}SzD0(xrVDp_4JE&e-fUrk)mep9h1%6<I6in<DBAEyzWI|9bMC5luO9d&lrW2~0G`%paxQwzByGudz5NSuTi0?PlRzXo6wW4Z&)Ip{S<hV$Uk7zdsRogy7R>vE<Oz>mBDeFVDW`dPPId#pS%@IO|Zg)~4&l}6bn}dZqqU_%rGy)}_AZDQYpt#SmBSOzG&w*UOOv@Dygn`zM@GD;vAz~Po@*iZaUB3a~dS=A-d_m{6dMtVL;baXwIH_=j=Fk$ISqfc)hYYUc4rGGLsku8i0kJ~7Tz12LK(W<<_|b6#g<&}tkwX<EcfH-xCB&%oX0W7xC=851>tR0|fsPR`uH1%)?W)eUp%|JiB~=rwmoL~79`f!&j@K%nv?_f;)xgt>SgHp8Z7Po86)KKHRdE!|IMO$HeOs!EW1^|qYDY3H$G8-DACv;qm4PA$9jl?eDnz<D6ZOe@Yj99Q9}u~<oTGt+$3zpOS;)~xdDOdE$Z@ax@PEG#47{qHUAP;AYTRouxNtnWCqPMCnUD=GK`;mbTd>H-YpC#%3zif_m#wWc<woYhrhjI+S7-=J&M5Q?9s7?#Oth2MR#?iRF=)P`;#h{ttcAwn|FX4(II#m_30JQRtanQh?X0`iDFn%^cY>phwJ@CtIeG&Fax560rcT#j#c@zFu8KMu`cI<t<>Xou+#(fjuiL!Pb-ZSo5?M+2tpkn{(eBeW!T<Eir{guf6|L~)Y;RAE3r>5qqcv6{HR^W?iAm^~n22o_EBv^ZoV}<YtYQ=LP?ny-cne$_NJ5f{0akeK!_qt$oKf!?XL6mVMDCykg{IaRfEZw=l{g65OYFH(Z*(Zdx_!0ep(9xyjDNTBEd8U=JDV6_Ns3DgRd7r?Sq2g(h;5}@w|lHpR8mIUFx*kUkDcZyjR#N2rnC^y=Z@Viz7DnD{P2tLxhVnu4;MZ+U<I7g^zw5o!R!;`WnvRRUQLSD%8GZ7_A3q?t617Zj#k<C?yKW5&x_p#7SInM`X(}?BGLK1v-M~qT8Va8L`1ppEK6im@Po1BJeSknQRzPr$c~yMj=VL6n}LR+AYTpPi;3=}#N8k;-p1Cmh<oG?gXl^;`80$PD+kjzPPYC~2|(;egW7_Md>H%2TO?oa#;M3pbv#2*2J#3H#QbWR8-uWcEov>Vy`yt_LUF1*cZ{%jc&5=qdGf$$7UAoWn&2$R!BVux;?F1>*yCs<Wi!Cs2yk``;>08>+-^vz8`<`ey$!L7ax=#sG|F~(42H00aW~8G%8TDc#fRRBa%F~eaIOr}(JhlNv8j}d%L#!=g~y5F6CzQ`2!$dfP!x*QRlPj!nVOOb&5<9eHt)r6a5`6Zd1PH?;`Zg{BZ=2mtf+b<Wh6-+hH<O_CXn%EMk+!3K=U@9OnI`~`d9k7<Mx&bd+O@W#I__HhGHz2tgKqp^`~u&XD5fOL8GM6h&{@Ff}fjc_Q3JW$OwBENsxvVG`&FpF*7%@lD&AL@hbz}RSk}2AZ@mt3%~Es*daK6$CqWLYQDlQUCmm>Lh*hH+Vk^q+B5NIef4B-VkntikQuN@TZ~Yxc+4=pxwo5PFQ=1V06-02qpLcjBrEc=n$h#g+RIL6=5889X28gXheS;(%rMSw?A4&O3+qp3*Tfr$$1s=e8yT;zdC(g|)YxbX*r;S{>{rsFN|MxU-*L`ILzd1s*U|F3dM192Nv#*qj?j>-ZsF`;m$agRX;WAJb`V7<E}T{`p<R<VfaV4lB|iV#y)&~eW|T=xr263G`5*oIe!u?cdVcI*e{_X^bcKI+{Q9Fy@uQ3UX?_hK=GX9kN67E;*Zfh={OkVuP28#Qqk;MjUD*8LJ}Cd_!oJIU(~G~p(|doHrxojG!q@vXe4t<RtA7p9WUXE|PSu<FtOowt{_5Z1*VSYHs>ewTmsqJT@ijl4suCwpMwYPb1>Nh9CW*rfKdYysZ^Z^HY(#Hv-?4(Un^F}wVlXlEIGp}7@PPhxt?ENb1YC_R8;=`c#d;KM;J;<cvBZ2Q+8I&PiTz=juSOHG6Z%A$i_YpyhAt4NS<usH4^)ql?411z^FONGx#cshPD}nA54APY)9PJe^{$g&&tGuynfjP*?_qsFzxegi$)BFK_Z4E{&Gl72L5bZj$x4!W-LBs9N=9GLusyRr!-nZ?Pukb1C&oD_{<u3m)$a7Y?Gqyj$UfM>4!a6P9@6S$+KZQG>#sj^cFhU%m4@m1F1+~b^71aOPY|ZsSDLmDwN|(1+Onu>y47P7K9y3M%7jfgO+G&MGc6wTHT)v;ulyGF-uC$Xr+fXMhRZLz_?B?;-e`Yi71N!37pwr`!t?s+-uL8BF37w6HD35D$!Uux*C!d)U+v^q`^4q98(#YB#R1UH&4lzA;n;4aXT06|R28ph)xG-Ug#*@aec?;JcwfA)J5GJF-rr!;{Mvh8Jna0&E0<{b_=Qh7xt{I1dHc!|b9e3H%vWh~kzbgJ?MZLv<4t?PTKo1h)P)pF!K%sqr`#Wn!zO|%`+zRR^f@f44J-EyHuUg-Za3SfRLi`J<;mkCC0s*1faw_zN24Z%4hG#vA9vtdrYV>co)l&UmOegM<G}<3xDs#BjI{+@X5G8W4;|XU4W{4z1f<7KluUMurU0Rf5stKI#?fFr-rt)PY<bPIdb}W?ffQngr3RAx=E0^rTH|Q~B`)4SIWelr5sn<8`Ofy<P?Zn@bamC~#pB)4*`M0Wf*Pj~K=S+(yCW_fqKwUn*`b!wpL72T{qEIPedEi^aH&$t9Y}+l#vU8VtnWej>KP^VB7WccbX#7{zm`vUvi@<P&1u+6fR}I*c8n6Be`ttpBFQD7@R^3kFnY*YCVEQJ&Ub_18IA<>sg21#AQevq8lWozzF%k01a@=0Arp+PZTz!jB4P-iAh5ut0VZ*H#(=P#5H)CP&(xpQ_&)Kmudh)Li<X0~bqsB8m4GZz6^>51)bVkG9a7?!(?w_QD@u?+o2=){&B7U)TbVj#{K>CFac;aOgU<=1;m^K94|YTYb|U?%iRVzlj`zQWphKL<GsEF}yQns2YA05HIU%%Gn#CP*zckgK)(xW>Vzy=}Ly(R1Uc6j)ME@i*1qbbO$UO%7MB4Tc>`Gf49eEEZ$-s6odcR$iEi{96Ll!M=r)G%v^D?EVPeQtql;Y2=`kQglJgmN>nbG)HK8}2aI>6LSoyBLWc|))hFyn{%S<vAlXPIsF(B5KT=K5KoHar1RGL0PtiVu+M!GqDqDh?wNh#HkC0wn(2?ug{JqD6x#y4oYPhNpF9mu=X9_V^;6<XD+yXQ(#QX<k!$+k4Yfnjb8i!}$7iOyl>3qK<`*TmWM5)?W6Ozj*6)yEgOYLuFq-$jo481te>;hgpOt)Jq!L6*f^weL=k*KGLDeE4A0uJGgG$&qHW_o=GJ*23amP{P}mn%cgHD>}MQF_mnchqKOr6h<s2cRhM>rqokG7jiKcPs|LvEP0G8H;{vJ;e8YX&b?mQc1nzEN$~XuO2-s$s>2zYDX+kD&r7VjF>RxUXdvl>I7rq0d1_uGPhN`W=WH@3A!BywRP-aG_8BC@K(K11+Gmn|%f=bW5M5|rmIDq#WNvDPq3b3e78g!l~mMG@k@qj^zUUI#J-Sq8fY{Bk3^^JX9h!ZL7d<?pIlsz}TZ{B)y?IB(T#A}J(Y}~+PkfV{SXBjeo&i#h>KLwob1^^|Z=17#m35uaoz6P+{ZgWdM1I=B_;>?963KqJ(lh^};mn~P-K6Xj^Z#c)X3z9*U_%Q+Of^afw*kMWQH0(tKq?TIP0Xvr~9#lAxNr8!B;gM!>Ls7*?=vzRpQ?fBkEmz=}6y}us{6_CR1gT#H(Q&002e=q*mp$-Ffbb>IK(x94Ee>FPZnaRY#4w9w^>7}@B?qquAQ&LZ?<M@|4_>h&MhDcvqvW)*l@YZGn?o`VI|7uxAzYKdc|<sapvIU#60D11Zx=sSiAMZ<7tvmakhEWFgim#QqGW9b6t=2Xmk6~pz3>i%;V5c};P9Y`ZzV4ql`4QzUf1@{sz4O%NJ0_vn}LBuecsM>eHeS%`>NPQsI@8^Bu`-<e3rtS2wa>SRPHrFwocF*3YODl1n=Ez_vu4p{D4W%NhS5}TG~p)C_>eC=s?Z~kXHm801lO^TWlYD!?r+%E{ZX4&vdgguVOSos7S+5HZ)X~Ub1v3dsc3FRJ3UELy-OhRpX(?iK$??Heuny{B>-9&$CdkekKa_Lc)R^7_4pzIAtxR=-3-~ds}|1c1fOr=jR_@HZ3m|$6wa%%`b}fF0th|kuvL6(Sg*U52<<$%C;;n)W@r48qLe9Zf`W*UdmB%F(2wOR7HDDGp!ep*F%|bt(k_qI!;TuUgCN=r{!o)*|e&eHZ&wTUe*yz?yFpHf-hJcp!UL*Yb~2bNmp(Zm_g1g&r)^UzMz~I%c`A{Nv@R9JyH@$<k`SYWZEkF18)2!<+RZa9GjzQBViAzxN!=5eF}x7^oQQb!FhmSL3+Gnl1&HtZGwYyAgSxI^OM9sCTw;lWy=V=jLqF$_yLnh|43y~ugf1d2Q9@VD8ZNh$ugkt%`Jzo3Bw+n!W*nde9O@kP0Ky~fp#C91Gu`8wa(8He1b6EJv1mLB0YZ=`jR0$L4<d}^9X7W&;G|BC;=6zl~K<8q1-f4ty2Eu?<?sFwbbn`<(6bS^AMHK4~84Yhi~qhr%g1;NiXLST*ZT)e<J5NKr6jlYO?wOjtjNj%hzF=<7q5d#<v@80m~k^O5IBz>>h8wWqN?j=w1r1q63>>jaa8VTVG<xH!<Guo&YWF{EdVQ1D5xETZWA5NXz}AoZf>Ark`xPYuaP$CMDWGmk}Rv%*jcR5yxT81z#=ivDu_r)?N+Jzp+w6|D0R##YHu^$)7pGZe1lwuSpKjpEOa#ndi`x_ZR&RY!-QOn1+<`*#d7M1dzCdl7})$1UP#bBPf6rVOqLaAnzDrb*Sl}QsK;%BUc)h9|NOMkpz)Rcg`&4IViwwFy<S%In~AivF<^J=*;&)jgZ9$H&d%@5WL?>>x!%BU_4%xITQn#=|nQ$BP%Zm``S0cPB11QM-9NKBWyj$;uFh&2~96`9m&%sYb2VD3pbmIW*s?HdF;+GvecTk0$op??<Q^qZ7f!?Hk4m_y&n4X$ptF^*yRN_w@^}L6wcCTXs|s#O86vAk6cTiadVDjc9%OlDwkI#$wpKR(a8T~P-5<71^f8-dj^nSFcNO@^HHSO0b>^b<l7U-5H=xNoMF~K`jk(WVB=4H{ZLfsECE@)7Xyn#+P!*jJPsOW8=5wG$?T=$mZk~xJ4Ws5(Lc%H{K@~V3gF06_BZ|>wB@vY^xrq(b)>81%m<8X|1(G#L8n1%|9^g}^&)q#SS%3vc}XlTmx-Rsgs;m)IA12>a)A(gQ0zMsh>n-n2zhT{ndlbFL~qN4q%s-Cr&_FRD}{`)qXpYqFQNtQjOt#!UW`}Q3q#HOOG`$amkgYI`SkwUl0p4AE*VZLU}>>xY|E;_Rq61$C1a=*{!hGQ{F!%7L*GDfW4d8DFsd9~yQ4w4iKN1T)i=wygFYXW!XZ2~;->BP5k#cEIl|N|6Ls_OIMDDig%Zg_isdA;yhBdbQyh_v%EYLd)-A}wqKeXc@1L7hN;&qEa1FuCROr>WtLdY35M*x!FV1qaN9<qTM3s3=mNnEm!2y%OA0V_4Yd0y)IbUSb$wdU`UslwEYt=-G^GR&074S!TwWM;AOdRN!T&6}Q&>~4@gXNEjlFt5*t|VP9tU+}F>ItlAk}gs=LuVwa?N3hzX=RYrR+gS^z@jG^7m4AN>w3?nMAJpmEm~Y4=I<<69L%R4);HqI?iFirCesB>4Z=GUI#*l>n`7`UQ>0QHNr`lMqCAeMg2Y=;2mv>7W7>!i^V>yOR#J#4QEs7pwPU2<O9ort@C4M<2old}f-i9;o0CCZG})YZCY$pCt}!q01F!DQ*`-Zq*EPK3MGa?HG@=4Owu=feI9}A=*qWPnyso#TRl_@UeNl%KMWT2rM|4=q5q;PF_N&S9i@o!jM_T4OzLh-jym#VX=0%jDUy^v$sZAPRb!ijr=<K?2bsw79@badc{nBW+61Z0FmS$;#5!1~nt*gX$L_XL!Q{6aKA}iMjRfNUH8CVy|P0pb6%4)!1?LyVJgJK(s#B3BM?uh03@9U0ukP^ixl~OVE93_{*T(uaTUxb>a&ghv`^xZl$glCC`wJlH@BScVG@P+IG%44*1T<nOH<sejx)<XB!Xzs9xLJOVy;+d~dPq^5|Y-w^ZP*M5^AQ1C=-Spkd$?~XVIf00aQS%w)N7*OLN4MWmE;mcGgKA0OxKb)7J21$z&pqX2L0>L0B)Y*n)TB#RP>#T!Ej7atKHpMow*3`hHptPE6g=Kg<&$c(oASnvem%S-cTWyl&yUz?N=%jaUMi)Vvf^)T*6cQJn6M_u86Gq7|N2@Q>U%XHUeZwSUe-`A`y;(I-%UgPObvN0oqjGcVY=zjbkmz4I<8huFNvnB47j~+ozTm`l+kRspqS3;AM3BN*>PPFO%D{QXrk%<R8T@|XLUynq6%M8Os~bjjB*n7nwwmDhc`-tM8(@OC1wSQwPJcaQA}URr3(UR8Z>S#n%;+!VSLlpg=<%ZAEIHOA9)k*u_#9gN;qoCvR8#%^(gODv(lkdG+Yu&m@qBi!s!c+odb&Ihr}ZvXy0@&33C+vc<sNF+%ciEhAgPOU>~GGKCpNGJ+32(=$L8XWTuO#1_dmJ;C+C<?#j!?K#(uer1IDAKxx)Zx5(Ujj>@vrhidDbAh|_1hiBGH9w@oSO}c#CRu2Z4c#qypob#dlW_Lz#HkgR~Hy?5@m9)Xdy>!6*$3*Q+rDHfLU3FKKW$H$%5t&?-La+7&v+HQvNY|F5I~EZ0^^MfmjWlZ`O|yc`=GsQuEJwMKqN^$$j-Ha&gu~AJXF1#L>He8u<`^WNN4*$l6^rw2ll%6LLL(u(yk}B>{pAfa&Aa8{lc$isU@9X&Lp`GJa6)cMGIpvm5}y$xKOZ>0oPb`0kC!0{r~pL$x+8G~oF@YXkD-)7A^Q!P?ZTlTXe+TT^gp06g>@lvZ(_qeuypl2#WLZg(OE+2JmKnok*Iad_#ZN1$&WRT_LM5hlc55FT1c!}lqV?=qYjQ?X3Oj`UF;Mq&ZxR?4aU;PO2n*D`Z8+vVek!XLQ*1$G6xtD`v4D~rYRyBBGid~=fh0zCNh~{F}(w@6@yiLW_{Vq)0>;suydT8iy--xbDI|mZOYa3u6Dv1@pG#~htuhek1j()#z*nu^ft$GN_us~@3kP=W;hKrC{npmjj8uSnv9|0!_4Bv8oz{OCT`q`Iar<HT&Op;4E6MV-7S=#hS5Z%VsqO(cNdPd=~>i?KE2iE_x!IDRl}NDxojngo61f|a7>J*1-xZBae`=yyASE-2l%+Lr4L(&a(}k0>Tk=I)+68_I)p?w5gi;@KX6r07+*&BPqcWRskBtm${H~c<C(XKp<ZIv4oy@G_+9vYP(2p0BAM=K48OmJ%pqly6waFEbUA~GN_`j+A$*0|M7soz->=}`7lvNJE{d3)1g=EcP|KNBBgVcwAOU!r9tud3Po%;p=8BwJGZlBr82^g>eL^Xibpf7%szb>UCK^}>MHHdK$|^xLPvr;^b4;T$+;)tc37JNSk&=N5Xy_DvELn#e%^3C3%e%M*dkD`!6AK|}@~P^}(1*-_#fc&PEgeu2mIJX3U*Q@;B#MPu=&5Ys-w{=kEwk&ZP1q+lDGrWA7{C-f{v0td7Wh&J`1_1~%dJ5vyGuWZPj#P*6h?GrSJ5d$RLc?{R=&j#g1d2a7ctdKGikp=Oy&+{K8Zt8o@eU-r3^Zgd{uc~$MTrAiDjeu%HR%VJBIRN`D!fTTHcwOhY22hgh}?RuM-izy1x54d?S8<>wDTF32AG(k_&e0eAmh!-Km0bsKJ_K0Gnw|*VggFY7vh$K#Tb_IztNzj$5-vV`4ZK6^=F2x?zsOM(%yx0A%-h@MRiN03B)h<A%$aE5QDN3airJyFoAe0qSiWH5`h=+P4M?*Pg*t)p$OH*}A4_1Z&S5e%1V)9s%=D2U(HC@EkYQ+$rzqAHrVCp8a*m);gIT@x`P9$mIi1-bEtKf)uZIWIh}x^oK$<=smzlI12oh38>2@<Lhnv-m%y>@M|Mqc=Wllr>JX7YSZ4su7vm@!MVy>a4+EhqkX!3I;CQn2TH&?&w$G`&XT;L4pA+T!FHdRSm+#GwWx}QFffzjyNY(BMpzCtQ06F(GHlM#%3s_%r%Hs&_v+<{FyUF4qWZe-d}klJyE8xzd@25l`&VK1F;u{G{`)W=N>-jTO=pBLF+&n6dwtLQTbI8;B*WeVYC%~|D5`KV;$VmxjVP7tqU{BEl?gfSj?8g171jQM*>pCAClp|VwYN~o=K@Z&CKgOwR+F}dSyxFVy+r<07nIg0YYl80iApLc9mRaROur$3LHWv{5W_6kGKJhWj7>Mu6fI+w%?dh`+6XfdGFhpz3Ezoc8X#3k_d28Gj1rC_pR|0P@yJdFQ?N<b$61*gL<_mjlRv?3UkPEf7n7-~Mj&05N+1YeW#odA00V^PGOs_dC=xMqMoFN33DF@gG%bi;`?~`PG|MV?-~-y#aX%&R!NcfALX764&b!(1_@mepQ4<*%*#lEuUrlCvPPClY{;C3YivcC6({d4hVbz!)&^M;PZtbtN2h)svdbl@nNKKgSBh43aJE#<S<2FLh$@Z^zP&ps865<qZQ#{-nW7yLm`N@SZS*j3N>PCrAIp8CgP#14e6b*nhsZ&lUt4}Ib0Bl%dkjFb*o5`BD>?f@MDGw@dc{2mmQCl<5+g>OnqWA}l6OlWgWzU;nI-O-gOYKSf2vlVFnmhX6m1m#g9`fYIb;y70qgadG(z8c3IVvmyea)N>_1wr}D&@3Q;4~Ibfc;!H|8`o7aYeu=+&aRiOhT^AnFG6gyWSg?H1qh5E@JnHM|UPtN_coM+(0?_CdeZlUAK|*7AR6uB&GLPzFp5Pheb`ostMFe+l2vG;?ee~S#H!iiXxS82~!D^g{L7^F3q2KXOZvs5SQ+a#kYwjE*(zArEBWhY~cCISyo!!dMll8E3IA9lr}->M9Ar|bl6MfD$Y42ZQxn|P3V-BFFX=m|G=H9eDHWMGYer1Zd}lcVaO-xe0L~_#hW15=<O^kJx3>0mS&!pjJCt=)E&v1i~qtqD}1k&*5{i*Fy0Fa-@)uT-gX~4Q16+*pWTP5?Y+7W)4ASyP537+oC{U&!1yit`95Ua2S)3}TqN3LrqQrU4?I39b9s3;7^#NYt(vN#u3VpT6Eow9cq}W8SE06i;?$qqka9N`^6S;qwB45UUznZsI|+VYxic#icDpkj!9WAn^V)lH<2e$jT&2<an79>twlWOUvy}8+G%@M39$fXK6d0)7E<!K_xbAAFB^uzG#+0cQXDDmz2>|lu;(;63w;l^+<B}Y(8AJA{<itg5B{pMfz?Dp66A-hB1tl4n1p{s~S!SJ#iSdvP(8KgntD>WPEd@n=?6%6Bo!Una;mpy}U$4nfd7YWQ$}))I&ucRAo2tpgU-@850D<cB60q__!V*v$>9z#K%R2vUHGcIHP(rf)$`UYOi#uHcP&_+X0&32#)p#^qzAXW}llkust}X$AlmDo0rH_w@PUU5l1+{<mQk?$F_YwJr73QT|aWdyyWtJ{3NXff8?HOCNmg_w8NAhU|U)Yf<9D}jUWG-22cx~F#4M<rAc^tY$Wee!3b<g`VkiXs2tgw%u=`9Pgw4`P|zs-4b$k2qxjWSny4?f!5PL)Y*(ELBc@!c#a6~cx|U04(n>$J@MQ+!0{1T!bc1QtEY*m|05KQzc5EgrUMU590YecEgpV(M0<*xOHDiv3IPGvcmI{)@Xz^*CnHeBNk$1<VZB93=L-Y>N@6;pUfN8GChUxg6j)16_}`77W3y_ZMGrGP0~eGe0jqA{K@$o`@8-@n<(=edt)JJQ`~`uJ;$Y+Xf~799w>Ak=(`_)~{Z*=IZ%?Zo|el7i@5S^$Sr~kMLO*C@<_U#zHSAcC&($f7-^L|0hqd<iq_Hrj8(9DLp-bU9n9dfI#};$-P0g*`%i7V!!PIuTva(qm*9$9Rvm|&?IF$fV07UN7?pIrTXGN-W%qva<rK-8mZ8QpU^XKFe|TQrpgom7(j0~0dtrK>Dyt|*>mwh56obok<CN6$N4`!0vIaU|FY)Y?;?#CkblCi_DK*p;I=%=uRhY{iV14TyYhek&3EaQ{EHVhoK52p-_ovUomMTtcW&3ejC+f<U7x;AyPmkW?m|Cr-Lbc#@mo6f6Fc_tyknmYIM_P&yT#ld;w$=j3*2}5mTV&TUa89Oy*?7n$z|mS+3f{Aad3YOlAkf`SWwz>TX&O8eHt6Hwx_`UAeqyF$rUwS3AshmMoxt-4bof(>9`oAs>++8*(B*zHD~Qsh#M-VzDDbY8OJQ$AH`>DwnYXU$}PPk8q#MXZ>vn+peC8=a|n<Zj66u!fHIT}bVlN7Tp-R&#L%Q1cyL9N^pBUN8wD_&M*3tzK_n+uokZ4TIVS)qXIG$t(fk}b!5KZzRXSPsHpej$$IVPcS|xOaH-(YxEyv~N%ub<dnyHFS*xRrPChdSh<zv0qdwJPRh`A=s6{X7}oO`4ThF@}E{VDkBm*6#S@iTsn<yzBl6xZ4}@LHKb;qcAQp3Oh<4x8g6N)r!HDCuHzJjyN$+hBNdg6;`sB0`E}Rk$L>hc4U#$Gc)#eTj({KjZKWwpX&H^AtZrZ8xecKao4F1zW`9NYRJ`97VY5-Nl<{P+(Exq&0LoLLNbJDt|0n<el}P%GQRH*&1Fm!NC3w1lf*{BYA*(pjCXyl1XyFJ@lV$%j;G+@7M2l)O-=t`vdQHox6r#S@c886}`US^>x1sZ`<!;MX2Ss?RR}L;-^2`@=k!=UuVnvw&YE}^Q}io#(`oO7w86Ga~Q(x>Jr`HB<y0C)4ddPG2ntf)+=JJ)B>*Rp{G4s`+fXI!>(_`7{t&xe)O<w#GhoQnigRf`Ai5==x5}oifGf0ot;^Coy1&mF+wHJfesNfxI_%4pQ9}uWFDsoxTNAi2@C~U0wc{q)}oyXoYf-K>dCn4qHCU1S>AINH_hPwKAeVH(!d;AHpfn<hJ{5~$kgW`%hYR4eR{TLtuk>2+b3NQ-*?M_FD`^y4lUpkU)93L+SkTc*i}kE)o{x-FRr1Dy4nkY%E6aWzYek_%U0cjvlX_MK~`st`>SzQH^*71F|2q3Q3#twwCI-6mba@qgxxngZ#KXAYWw;+X?B3oT;f=B;a*p}<Fe-E{gyQ$E!n9q*>R1MLi=1xnll5nHBc&2?hsWiRX3`!Eke1n?q{<ol@}_&dg4+KRN-k@DHgU2f5WJoChL(&NV3FSyM>qY=~!#0&;udX!`D78wGOO%Rf#7Hi8%9;8`|g-1cn`A-$f{`p*4=KNyAeKt3E_iB9BKe0aro@!z~DZE4Ov@;J$p%6|fxt?sY4m?y9Q{%$9g^@$=EvK>~V2m0SghZS4!^AZHA~b+TD!S1>KmRkE49Y}+X;vseL}y|Jxjs)&ZLidCKTIBof>X{K+lziFI@vrIFQH#h4Hda7|+f@yG!j?3Rxs|M$=a!h-@ndjM3E30$KV6Br)8=G4$e`8H)mjZ=?ewf&06I&E;g=^Y6@vPQ<Rh-G6%N@pr(4lajR`2)qm|B<Jd<5vtpxd-vER?~pQ@ozN-O6Fn4Y-<+CLLKzq!MC%@pW2SJF4Gwa{A|ATq`fdxnGbSx%QkcE6DC>Wq|y^#c|gN%UlghmbaWD0n!#<<fb^Gpp_y*2ZVT&aL6)v<)z6JM}1^jC0k&SPiT9DXWURqHL?AddNlHuB)wrvjR+|=R$?CV-3NoBJ&-p&+`G;I$;1_T`xTM|V%g<z6K#OxJB%#Fm0Ua!{2mlnb_{#F<=y@?5oP>$-lG+S?07FR;?o-rwTulxW--EkcyfDIe70W8xP=v(lRYmC*}_b0d1Fn42i=s=34#}DfHQD<XLUO?M(nYt*bbt?fs!tw-Vpsp;V(6Hu<a2izye&A_a1lvvzSPRXGKe<Hw{nZDgo?UiAgd^i*muRZ3~P(Y@=d^U|3NvrW2P(h#^9wq7*Gz+tibRRTd#7&3(lxYP^67E&10f(<{SyX7R-7ZIac5d$OXq0o!V#=v5W+{3vCta1Ztv(cK>Q%ZZ#|f(@g8<9=f`AYRfdSjf@bzNkgBy(UDn<^~ad67LqMlMOQ9B(AR{XsAqQGF5|wh!?Umz2$Q%?t51mmaJ&0jgl!w8kX=N^F%cd<5=5($}d@xlu1X0QmQAdh=)=o0-DFB8>3fZj=N^Gt7<XtpD-q-7(*dJvX<rhK9z5c2q~T5N-E+U!TH?<xOrFvNid21g;%M;m2>=Yg7YBf#Myl#4U3YWBS<R2Q1|2}QHiOMNf(!(3UBu3z|~9tq5+55bE`#O%RihkS_m7!9LcN^QZX(Qf(Mxws9G90IzC{He1_B%7Sx|Yq)M~oyYOA?zL;6id-Y*rwc^0hksgR0F2{Vtao&(>kBPSjCW-qA@$?bVISL2S<n)hJA`3^i5s43;*Hqy6wb$`2*20<huRt-L<P#;CP)RZ`rwTg47xD=yT*XV71l8tI@G;5JnRroVREf<N1t097K+hy&y+`qUfVAgwkegZ?l#0RX=?r<btxMV<KWI<gxXx>JA(ezH7L(#ZR2*Tkh7}M)ydaXZu?=^CtKlm=1ckELU%MmGXt7c;%HTTK;EgqPSduUR_xl^~BYe>A-lYiV0?w|99VC-C(QQ;^xvCxrKDZJ-z!A<>4;aTTg%83~_~1<Spi_BIYKf-z(u5Cqx4SdpgQ^WXP{6b|0M%vfgB>ej#6;l>r0d!ThS7Ub`=BQj_CfN3H@<Axv|G9$f3TGh<*VcmqLD1t@&^y824<#xU<(=K4;J;mw8ZW#gb!4(I)pi93!f@x`xoDN=_v!Yze42&g6A@JcZ-zHpkiaVT*N?5du#M(4MtoxsXHY~#7$PX@D;Mx4Wx9m!Ugr83D)Cs-Eh-`i%k|1Ypw}GmKSfc;l2WSFiH)jQOWQ#C`M8os6LpXxps2~s39{@wu_i<?7AgjDWL*J_rXdNV_jd;rS-)x)|ctkyY6!oLKVx$5j?X_T>wB5eK(a!NHtO)%bM2Rk#;h8)Z_<H91mEW%T?6Nu$T4#))Dopmu;Zd1ak|D&EmyC5QQ{=;EHF;%LXj?W&bDq!FP~Kq@sn`vlB28pp1GL81&M9f;t9fV-IpH=2D4Na+3Ua?CZ-$b_lwm{E8=$Uk$)+f_WQ4Kj6rD8*!6MDxL8wVKk819s-Y3pX{LJ6+4YSdfGJU>U}Npe*TWyi5movm$egjaI`wrP8=Egb$&;JI5$b#W2L*5{X+JM)!?$kjaWB*UaG7zo*1`AZW*$PR%d#-3^L2u;+3YX8YHXgyVkXKrdZ9|9Ht{7$gB*SvkJ8n2}80%4(jPxRA-A9_Fl~NrAD>`3)H5O7#I4gv9cwd=_Phcy~NtI$rP-K)UwyqN~$J`Gi&k$B-8QtW%R4OrCfr60ghL{SnWfS$b#s>6uPq-_0DN}_r}=8mh?863oP|)-EhT@?yK<|Z{7T3W#kUmJTd}C?uJsUV1Q;0VfC&e<fdX2_LXC{PkomJOpW4Jm4q%*n}(EREp8=j9!9W?C=F!+SIMZ$h=yu}1&ADL9fBc@(-Ax=DN8|1kX7QXN3}W0_5!C%Ja7+T8-#rzO@?$+o(bXt;nVk30plJIa)+alJygax&#kvG5P>(%GE(nYALK-5R#zr3)~t8QV<5=It8xo|7UOD6epGOvH0in>Cm16Y@S$$~(V9AM%V5f;#M;B|<oONe)lCn{PLwCk-{^v#gol@;;yIlrHq*l$;DCqPjEVPPB0;0y&pw*Ve{m1OG3&uVRH&kK`-E}PiMM}SO%8%prjSDI@%2&hxTBTA6E4X1Xb9ET(>}1e`>x9=%mA(|r_eY$TTaU#!3*%aF6Kr@I~NE^6iM1t7`kUOW+_FBC&6Nwt&6M|DJGX<4mgT{H4x{rfT%vfm`HQMaHUesCA3@A!h?JxI#mW13n^<xf%N0b^k1&1Yx&uDU3<2Qh&-^UpHY$WBa0+k6|;%M*${!#X{nT74m8P~35)uY0-H?8aAVEwbl%)<%j3-~0rY9x+VS80T4V4tH{PAfaxf>85yN^j577vaowGra7G#uFH5wrQF)P-^*0)h9dLr~(g2xok5Qh|{XbxejT!2@fmEPHQU56NZEj!o%p&TLHIr66t<?W3nPjwLGph2hC+z6FK3IoJ7yG6B$Qq5cXwPINws)l(_2@MuF%QwA0IEexT*%4x_xiD53V!1OrS2l$^Y@1No|Fp&F^w&Su+QiXux;Ei@C|&nkG*pemdU=IXie8=^mkmBRKn=^VFLCi|$<T7OYQbN{j^daI&YQSCq2cwfgRNQi*p{upmhW=q;<7cgWlL4fY-P>VnYezeRtociRXqSxyu4tIrwbNoF|uI_br^0zN%o`@#b^vWX72(}*HJ08Rf+2_*D|`R2qb~|<wd4MF39>l!UV~Ic7))+xUSVi?bD*he(SyaD+Cz;7n17ICbGR+Eagg|#V}Y+30NJBL`V!(Zv$1Zg<T;Zo`ojNhKMRq8Q|R@;Rscb2pOG37H9pO-hg&*rIM)P60`asNMf`Cdv#T%32cyH5s-_tv66~^pgdi(0yMh?9^ZQ4Urf%D^C~*T(r`4{_6gDr1YTFS35pI3)Mc9+yvdg>@yLWrpQWDz_1_Z*7DO-~O!#(3$;43#u26SJ%F^9Xbd90n$TEAB@X3K34ON_-S+NekIj>XSJzb>ohwhp97keg=vi)ftD|NHAM-}Y9-ZrV0q6>xo)-a*OdUsWopTTsDLOjK4|B|Yjh0rFRFqJ0GbIF_Iy2?H>#V~BNWKh^a%K9TV*1I*lFD%+7+jZOI_L52u)`freojI}Rce0h%%2hb539;oizQl(0X=cMBH$ioc%xkUA$h5_YWovQGiM1<)n0U#F^}c~X*e_RK6r)3xwo&56i6(5yG8js1fDhpu+t8eCu+8Fu#h0NM@RHN1#5?!g3(8p?!!}rLdIKvB06UiV0r0pzZbCW!Z3(W`U;p1e(mtOr?(<`FAVWU4np7)!0_3XeP2T6qdcC^O4{m9VakkHs*EVnRCs|3`<Y_-7*><<u<h#WtZ@EeD&0?cG-7V%}wJ~kGefgG$v-HHfSMBywOHU>O7h^5&5Fa)<L*{Z^V0_6d9ACRf+>E4VJLf4!kry)X5_c-{IMv?q6T4_wZ|P-jM;ymCjuV*7RA;q$PJII#y9@vGyO`*m*yo9neR<Wm+D$44=$SezfAR6!u)W}&=K(uFS64QswL940;0CkB0BSfx!o>m|rnvWo2DAy%ZeW`zf^k4vcO9hN3KZVKj6A6O#Lb&Vh#mT3H%>qv0Z7>$_IBhHEtwu?zdQ^;sZyi1KUw`ku6g-XD?19@C^acI@}0groh*&qof%kpsmy_BX-YliTigxYN;VdEmc6OPop*1GJHHhKz5nQArB2A6>XJ&=oz?EvU0F|;(jpnz&|KLWqI&+zl{9H16U1@Owmlud6vM$fW|b%jVsMfo@piZ3PC8vZ@!A`DUs#G1PS?$)rBFr7zSd8uYdQp!@87=7d~9|SqO3QfaH57%m{TOIp&Xdyd)>5dIAd{K?VEX=?%!jal4O`_yG%58KxfP2f6M)mn0_pl;g5^@h#0yAJ{T|M<+oIx>muDQshhRq80pK_$=){=nc^O8e065iGiND-#5AOm`Kjj{_@|vLDWnuhGvP#hCH#4qbqY<Qd$^O@U-_&K!fPe^EiqR|<OiN-gacrQD<{aF8-?!(cS$h4L+Gi$N>+~G0%w+gEYf(%l5QE-yb*NQ$!kaY6d`W02X#hFpr|S1Y{|;`jr38S=6{#vl1@-jC2nqrdREaYQAPr@hOP5#055(n*g2Bj(?U*1v}l2(mo-g!O5pO|S@W{`Hpbi-m>7&@PpzgsY|<o3J5vKJ)|y26e?B2-VkaT#3Yv)T0Ge2c%5eL$oM?tlz~k)%Ju#f1CnD8O+&cg$a(&q;fC4s>vwy@ALm?H@ZiS%$GNO0YL-sm=!XzOofFdmb6jODQJ(&HD0T$kZp{R<FUSKNW+Ey@%>L-g%ke|3@#Ft?dkd8V<Qf$8kNQ&@_?<__4Lb|udw_K%rV|_u{8RNBd4|&Cb%1285I6sJ_2vuL_EYTaBB)m?<kLVDAIy91a<#*7<9~)jv#bZxoU)4P7FpdT<<s;^IN94aO31aNzRHe>JOtf|5==&S2bPp0dYEnm0#$*e%ql^}nzjJ#v;C|_~t-NPjILf*ZsgKCz$Y)y6POLK_7#X>OWt=r8?FLov3BSgkhE?8K?Y=B4d)Ysh4PxtsJTAZQA_0yh)iHK37$PKZZ}}S7)g#SiSpiurFA54`9qaX5PEj!_5f7k~N`+)V-Q7)D*>2IzE0cSw!o*2-&I%S_dVpp?;1tdDz0@~)<jgN`?jv4<av)vO#g*)PylmpjN-Qw$;&|^&Usm$1<*feX$CCJ4r_njLbmr~iUR366g^aqbX^49<uQ|{Y;M`b$*pKdf9p#-?PO1FO7~ZMsd&y?6ibA7sxYs~OkjG49oUOM_bMdBv5&Nd{b*Az+I@Y}1wqyiT9r`Bp#XO!cp=}-d2MT>9s(kGwZTv6W-FWih>2-JGnfu`eo$E843a;50*SCTYnVsA{BmKiKBDM|&CCIMD+l<?)Pise2b?uM=)iKI@4-A7lx|=w`pt&)sA)18b0<vfzh!n!4LUQeb=z_R!z>dz6O4wjUgDfA~a|hcK_Gik7M3d47&J%hd1cUIR9TzLgzC&@KXULwVXh6&;qS70Tt^pWc6C)i>xq=lz#=a^X0A3bB-}me|Bx*_<miphHaT|f9_|K}j5TP4oZ9PN)IEIpI3Ae$YkcPg2d2ANRfDuL(#Q%%bZS@+*!7U^_UXP6)^;|cK6UHbcNjMg@U@4e;%|ph=IR7SC!X3jIRT|z33X%xLkR{DPrH+UoCGm{{Tc?3oS~Kdk$>z1IL>)nH&)zsPbPGsk)r_}v$ovT1r6yX)GOyvnm}O|`YJ*9>2?Pb(#$?P2t74Maz(x>2A<RgK2r;0(qOlO{_)7jfja$r@++3x-oM1Hh0g>8thGp8Z49@eCDky7E%ruBeHtprayozNjSN4}t9+jrxji~^b(%<cWec^xFRe|7g3i~L!>uiBKP|^uaEc{yLF)4G%Jpr*9svi~3mx&890WbJtW-8%LRWq8#4YR=^ny^do6~n2)<=E)#6ySwWosVJ4u(f$x4#nEJB9&mZ`re38K1+c+D)`JgeyUXF%5T<#4Ubj=l}^b`Rp!o2Wy$MgO4L<~v*~rwB2OhAZjW?XrG`nI8#q)nu_G)nF-mviAO$o;Ad;#<@RW&(tkPVess=S$AOi%nT)cgvR0X2-N<wWYg(Y=x=DOCu`uMC~onO9;53*Yk4pVi)Ui~z^8&m&rRa{5q)h3JWh*RYqtk_pe(Znv1M4h@JT$6>!#T~e@+vG%Q*XOEyE1G2HbuY*N%F7&)_tZt1FWOyhm&I2OYFM0`M9yNg7bn+V8FcAw?$(1Zj-~-TUj&mks^#-!gCtbMr=Le%U@PD1ChW)&LKv)^Xcwf(1K7dCf_q7aHZO=`{P8c{KVD+goc;8DRKN1~{j}lAoG}{_7412X8KWk~ic!qOvMNp}e|{-Kt(JZDD0i6foqbjOX)6201Z8P5Ua&_@K-QA$GWY`*u@VjrDq`Ib3pa96J*eyIY5PX}=Yt=)kOsCX(`Rm@oc%Urt$}?>1lUbLM8#U@JsY^#zEH_iV`6Bvm(laf#%dxJCD)T-Y{pBO)Xy;jCXRDUldW>U9<Q#1M~0?7V;#}6`-m?MpC6f9ln<eiL#S&Y@V0Tng+zT&^I{B1seRgpN=7c9mpX}mCTC;7n;iYKH;SKG_^^7ZsT#!M5#85|g2%I!@3K(@7qh;zbI^dX#YDD@n=*0mLC^f4&yaiIvqs|EJz0ur6PJrtV4Wq0s!Kt$f@G4BO&+VR9&iwq@x6VQFSHU`7-pN^JYTd54SIY0lKTa|^`s?^B=B}7(R`87tPI{S1<rI#3O^fXlN*pFFR{W|*pa8C8toz5+*i_|b!OvLpQ^0z&@?&bWwxqW`1(Ry1P1Hs>$-*IT56A*m3BPXxzz&DuvoR6iFFRf*|s|vOnyPtwf4bbv7X2J@6sBje@0J_B}SVh3Ax-UWN+5KV6{{jBp%8d%Ym=C|3jBy!U^%^kuc!{av0?3$Q>e3!>ME3Id~M?!U8PJWiXXVR4&n@g=-<z>fS&&ki0Y=!Q|&!flBLc%b7j#%H6;hU@W2MEsz2ug~pJiMFIzcjBgnu65?CdK@5T^jEQOuTdc%WCbqYSwR74BIklr|nQTi>gI*wIA()Xs^ydM9pOR#kQz{=h{KXmk|Gkfo1<M42bqxhp6_}W(&n29*h6by~#vZ(?z%-bsLr^;ya~Zq}(_u=4`k?PrX?Y3z+)~||>Z7$OtYV_nn3w{qztKsMspZ3P;PPVBjaImnU>TzK&aHjzC_vS$?XubzV{7}iKCC%E=QyMK1BtQG93dk14qpRuVKoGy=`kRNHNtD^4S+tbi-|(=Bm3yo>V;oxQu)>kbYvw?%&33jRi!2<vLZ;{?J4%rTNmc`K{Y2h1LZCr9&}M9Wf$p}0cCmlxti!?dGQU%En|#(I5vg7Fxh6U1hf&@x?Uk1wXTj)E%!T5Pz{g};WI7*eTd-8!yOXt+Uh)YY!7T6fNVNw^(`;3_Ga8Yn7wPXMu8bPg{L^(N2%U3@57nrJB+nq;j}W{>FxNeRgLstf=Ra4qG!&xFWkU*Wdn;6#zJ1xEN#EQ%GL!T!Cd@FN{o}R4apqK%kigtpjt0`63~bx$JY#@4zw5JUq{WEiBdN?45G4*p!lPO179YWE%niojb2$M&~+dp1*qGgaLlQ_3?FbYxr3B2eP}|RC`zCbl2rSN)x2kGe+?J^3Ge2^oRtI?v`m-Nd$UKf*R%JIfg6HUnc9A9Am3nkKKkeM!u;8v@RdPclC0YN#?0`f>jIR~f9>>+Jt&=%hd1_(sm+8jA<DfMuiTrkd(YeT#1)cFx_;i~P>YK4g<#evjrF`Cu>dy{k(qQE$fRSMKX|i+VQGrAI#_gM?vaBva%5H=l~yN|M`GR@XTq~Pf-BYYtMg{caoo$4ro;bq<zLp5UYd4cVL>(Dz=#PZC&$wp8`=YvKWNu5%~yJU<v^!c1FPD5<w#imgflUf56TWHTp1(FqZm*yOxUt!ilSuf{}XpTa$Xe>MzC#AF1n3<kN6#!LF!ZpqJV|DBlv+{lx!ihY{uMtLQNuxXwNE()F2rja?1IID)yX1u_lOB!lD1#dX*-uGgM<H=KlDi6Jm%^4Z$*>AGnq1us+RseY6^%w|F(6Boe9*hoUdlH<s^hKVyZFN{=bcA!U6HN-O5>SDj19s0iMl9qr_&otWe<hdBhb_&F_3V?Li6rUtW9^Yt3asNVL#cJdwur@^4%^Ofn`e8Rq+uqnK%+n_pM+>!Ak&Qz6{$8vC273tz{yaxoiM26{(08fu{WHjkrub#1_J*APr$~o|S2h37f<@qM`LO7ZT7RV#%a-3OQ+$6KCGsnoAT8$uTnV4WF$qayi23&!$>e~vCL}ZBL5Qf(kaY>l1S!wpb>&MqqZjJ&#K0x$#<ecxV$B*s|5ylvdQ`ilLJVHU(V}3A}$6|g{5gLao4k7YoqJLJ;`TrpAh<k-BO0%UA&zc>};Of~$w10?@A0&0wdi-%fR|?gaE}45M5~=_8qeQ>u(vDZ7UxS*xKJ?wN&>f^v8x5Evw3*CSmeDV=ZmM<Q2-F;2f>>GlHljEa-5WnUTdTh=L7x@_hqbG7B%07zKno_h%p@r|*(BhZ2{qI9z!}~UkKSNAeoM=}X#HvWgfc!);1q3)vcTf}0;IEdR=8|99gK^uMY*?CDlDDgbcl_~+?Z)h4V+Hxm*b|9|0!QB>y(F&tO}O?b@yi$o79ubv2Idt7CRL51%X<}M*SuD>eCHSJOogXUZc*z2n1ib62~$GcPKlRi?JnQN99e_gRo&C^+E1SZ`Q{t$WOK^QnMG;8M!5x<1$VIuyil8Qj1n@5y+s|1Sivthy@yD28rl8l|6Nmc<#wrZN%GB0^i_RSq1Qgl>{wqLcSwht(N);Sj}F?&)k5h7X|o3KqI#tWTRJZXr0{Eli`NL0tT6Dp~jG1(jJ|wWo@Vec4jWh$K@N6$<O^L&4t`ev=R!P2XPvn(E{-msf@u$T{3+&!{Po<@4ws(0Q+8EZW_N~x!jym9M)RLOX%Rnhz?k8I=T@#YpumvWe$NRMR8th6qX2^m4kF+?N7t7T4FZ-RCSv|eY4^*mKa>Yy2`K`8+m7|ScMb|y;<DCttd$PI8!yCW9YO@v+w*hCWJZwSX0E8_L}W$J_NQP@#mAi9p#P{Wl%F9Xgk*MS{jx)7;Hy4McNt^E>h@mj^8pX`9ESVd9_G3)FN3<fPoxXCp(68>{CULI4$F76dvS#Wf=|9pYk%mqm6Zs25t#|Mwf0;e~OH%OJ0L3-8-_>9j-BehU|xv0XMRA9X6`Eaq~)YqNQulo;{C_n4P^EtaPUh)I#L0i2y+<4?A#ZS&jnu;NyJ9&9tXfiVBrm5JuIJ46?IDxQBFXLq$`t{W&8j3rm>7mXNiMJb1$S()awYi>b=uMg;Y7D(B8BOC(66L?au58GDrL-F-+uKOkzAPyEC{YRjJ0wk(i62FuWq6Ii0L6k(eh<zs5g$4|_bwYXY}J4>unu5N$uO#TqIjbxIPNNB3kj7KPsNHIEjtLcZkJ}8-M@WP}fcMelFmyU8Wp986mm^^791pgI#qXV&VY6_%ioltcl)j7|!?8~bE1iFrwiQ1PnD00yh*Udadu&oSC7di}FEldDr1gW@jQ3FL6SsNW**%FPsKXQi)1Z_ZG8uw~PiZPHDG)(SAdV^#Q9{gD4$-$pBO1v5T;;$Ij?y*AQ0hTjwSTRWhe8n}Vuf6%6E7*`QB3NAD@GLK253nOguuOoy6A%`g@K+lwACt*pvPcC_>iBcQ+nW(IHNOq0Ax>e;UD?l}{4yv*WC6IV%-AeZur1Ey2f^KdgN)_LbXvLV-BC)S<i7Voy;ACwm&1%shQElCBEC)uPrqswf3%M-YwlMwS-&k+{FINeVErHO1D>Uo?2MnKS-EYd@>LO>cLAgw7C>5|03_pt7qEy#{Ol=s);#6U@v~=kY%^?@0mun#RwR<C!DiD6Fgu(BW`m(+n>Bo<xz|O-v1Z?xD*E?=;+P8A@E~{zEz5pgN%BB;d!Xzm?E#zC7-M=XYRCL4tufM;t$KB;HI`?su_`pCFntNj=e=IZjX`MV(<{T`I{as^svKAVxPX0MW4BhVu{u=aVyOCUCUzm2kmgeCaBKl!VD-1<n-fuy!r?TlKxgJo+8!$HJ_@#ygT$LDl(%F0MvT}%sj5YXW%i^^XM@qRTi}}xB1d9wP8ST-$Dt0ubF08qIZH|UAqd&zUookr?!A>0%jaa``nxJP%@Nm8Uj<34$3X6DnW5j#{Ew@;A84I~+pbaMKj|p@2VV;ceuAtI0QS$Ur`!{MTVj<X??x>7cNl8_Cq3c<Zx!)B+xma-)`f||m>jq87!)#BG-^PGCQa#b5AJcp@frxjA^jA0)87V*G{~>Oo_<$m0BcexfCY6}v-)NcvOW_&x~2_cy&RPVvGMe1TJu?!M}PT)WnO2SMPqMWkVWx}{EIJmyWI@eJ@h+WtioYe9cP9sjx)JsVWvK6^_|UdYBzIQ-{H0I<bAYM3e-I0xdE4xOtLMh&~s)w0~wVVwu2j0+DE~EZfb%`&Xs>8skJAgHA$ORNtRdb&!A6<VhTICe*@Rrw1L*tR>>$db}O~Es<i@UrnbCug6lUmGh_E(e@K(qNowbpOkxKUxU0zJ^_qV^=msxq0^P}umN8=T5Y<_IV%c(}Ni0+UW}d-?T^RJb@(boet5{O4`xD*{4=ZlWurQ2`T%-r~Fyt1S<V>8*S|cYT&G#!7D<l;ndF84)Z$PgmmyKIQZcaz>B=jJ=F_>c6*enZJCc?c*3kquwlC|afJpo_{KqzJZ3O%UZr%myn-p}E~<dv`3d&G^`oIV|ffs7JwCLd!3`Uvk7y6W)J1}1@#=VMduMqWUALe0vjmfh*dIUJ*H%ONbi&2jMFY#tV<Cyv}fw)A`%SLXCgk;oyaX<<IceT}45K<_C@egjSsvG^Rwl*EoQP;As}G!Pl&#tK+fAj2xE+$?-*o|i%TFwzMy75e7n(N|<ta;7UOdEFp2f`vQGvruiZstqx4XOOIxwvqd_4ywWHD@@ME1q8R6{mQVjHw;L1?9h8%y%9P+^*7^e<FOL{OJ?Jty|^T;&m5S~C*}F&!o9Nb5RVrRR)Kr-6aL0+Jchr={g&@~zyDc40S*sXtmEHCF+j{Q+`z5`M@Kg$5}7UbDN&d^B4`S4o<U5*+VSAFA$%!rLsaF4|H`kZ0hFm3rdtNJ-VR0FUik7Ue5V|NZ-2&?;HR!~7)k`xh5Irmo-ic8dnEr-T)Faghyy^Br)(r5fMVqS@+va=nvAA6s~(RFE|XlOV=%g2IHfazuBW>=9+-57g)U1I`XXI#h>I{sO=2<jO#9f{PbXZaCOH_FqAcVxNpQ<}d*dv@g)Y^>58}n~+-7N(J2Mz8G4V0j>mvbI)`W_Sji3b@Dn*q;-C3a|{%h|O4zMm4f70%s`p0=gj0Oe5x(X8wmE+{cvf>*0c*}Ge@`{~w&;o0kj$K|5K8CUg65wNv<Q;Ey>mSo~L4uf>D(Hd%aKTjFNUI#U>FB46){w$Y6xNHZuxj9@_jbG+x876+0`yj~$C7x!?K&8TO7PA^poN-8kgx@ANi<l4&Z(Y4tts`YjZ>~h5`+i23f~ef*s<l*RqH&W7ZGcW;7ZAH3Rk|T+;d09RGBN)(jLYiSt?c&>)eF(PTXPQAODcTM~ACq!ObjxBx7RYNKYqNO)mDhCpj)R%<~Dh6vV5P*gC=T%VfcE&Kh#8H8f2yU|5VP=xu`0K*&s*P<^E13W+R7RnmNXJfQ~8)*Uk|)}|IWhdU&N7(oX`JZa<@f7i4xldaHS>A7{f8)&j#K)PxI3=6(}O#x}99bd`<4P{+#7w{71IQ^Q85TwJ-*x<|6a*$dPzyZ$OomjKvEv@&HN(d61vv9q_&HJ@6=_u9%m)}m_q?&S!ds@DDV+BsxSr}Khqv-rHWein@CW~RGu0yQyhcbE;F(A%BS-EysG><L&;)9^XI4qPuZ1pzjBuPf#YV>B-EVfmc`7rZi0WCZoF?u!q7V!<WJ**6QH3d)#6PE(UeibAc2;p1cgZeA(&-(7Cu?Arq%rZF#_GFqwn#GJ69{_C3k8Z0tuzbHQE>0rD6+t;@mnn0l_tq+;YDi*1<|c~imc)aRwi5M7Hs!q&`h+7%d`FKBC>+I`3u?ci{zLhbh*vu`+&VV-!vXAY5e_k09koXfF4qr|161ad^k+%F`l&~A-LyYRhn7uisIv%G+il1T7b1?a@u=fd;G_h(0o5&Y_#?g>RChYA=u`L%<RoyR*e9m`J{=H(={0g0{q1iEl&=cexB}&)3)_mtC+k$EAmTzoI#6gRL}8MytV$C>POVPmEk&>`hPDV5FtA4C6Cu(kbBZ!hensSGrCb9wVwR<<3KAF%Bw$u%V^z1jiWBHb!O&8ZC>&vZQ3Ez-3JOG%-N%kdJzMihlSp<v!zzU{tkOuV63xS_&i-|rzz}EURZr;pVvQ&R(A*V$&D9Xz{kX4jhw3c;^S9*u)QDM!n7z65zR)Er0lyDx#Tm)U)QyiLZ~5O0Nc1-Ay!Frw@n73$7fV&hOPgg+wTpB{N~#SD`h2QqQ3s%3Xz?~MF2S9QR{67Slxk}D3I?U7pz8m%v?ZA-zH%cKDf7h)Hx;YeOyyDRB0jZS)CdMbuTmujYYSU;-hAcPjf#NHbIq)oqnnwoL%pzSBz9{T34Uv@hIl7DlR12rU09o;UA<MyPQGljB`wRP=0j1b!qFmiGq|mW(Zp<;VUV?ExW=Yr)2I&y9Vs*9rf)12grCs;h@sV(P8xb?_77)zV<r?R{Wk|>;Q$eAcHdl0cld+uH!vHfpQ-!+Yz98vV6_A-piHuxh+i4;qk3K*_he<#NhjSq=zErN_MoDF%ph6>lENYgDO@PulrQ}h!?Q{7N`#;cj~=+#aQ`ITzp$wf-aHuqw>+cCai4JHa&L~x(dzT~??I-WWn2KuPGu(`fN{4TP1QQnL_s>5focwcfSn*og}>MR1>ZHA<sU#sfM1^gH0&#q5q8CQi4;9N86KTLIQFMUk|v+|xQZVeOX66y%sxy02>@aL;Di+RPyF6|aD%hP3vL}3{wJ)=JN{`zT1m_G2ShX^?&5pe@o8ZPPmd>ei_3$9lz~_dczDG4{<7SYKfJPVeaXfV`{=wO-&ND&TSWs>Hi{~4m+S`at38)vGjc6=T?RMA@$Xz{?sLSc3YsnFCnaqL&}Qtv_4aFKl%IM~XLn+a-82616xRq)rA<vdXDt8Xh88(n_VBU@T4m+AjXU=I0TOX0CB_o4lTsX>IZDw0b<uQBQbzd`{G5<B4*%$fymAES&livS+@N&(*+IyzUm_f3M~rM2#VBPd)pvU&L8BB_(5H^K<dpR|CiXWf_u+#E`t9M{Z)5p4(Xq$i@_Uc9yk4hrk`v3RQLT`hdbPZ&#i$bDnLBEupa26kTwE=Hg$R+BcruSU{EYjDUfak0Dc1Qu6YjQrw=(&7qC29O22*p&GH$(f!Vg(4x#;Fj?5$#&2%aa?=0k~$xE@Ix`e^bdQRQc~btfkU3T-YsZXe~a`0Jw!b*S7>hfrH*ew6PQ!F|t+5X-A>gIuFw!}X|*fE6fO8+%2pf3S?DDf#>Zw5<UQJCvcq#a1QM1gbq0O)+@V!&8ZYu$ONVLl~6qVB5NfiV=_w`3_^_{;2Wp9z0gs=?Ow@!xQe^jv7Q@h}(kc{T<QbF+OQ~J%nHj90JoxS`a02Di?4MyCgo7wvULg@4dOw;Pg^_)Bzur@yArwVRSv>ttWQ!Q5IrEhP(LXgZtdsWf=dxtMsNfb*t%lF}}mL>`)=hD%~G==Q)O2DcH<o=+3~%FXcUT7^7M`!H^|HPiBHR%hgBGsaptCBoj&&Sx*;csKPER5xP)WJ7v)IQW*tJ8M(AXO4R6>O~wU5MwBF3ToJ>}>t5SD#WrNoj*;?2p?SY10IjG<%fBuqH|+U^x`tvG?{C1Fw##T|g}PuEbZ(0$J)4)JXX3DV{!{r10#@D1yQw_dD1dbeUL!e-^PxngOyav!1|}F3oi5GQjGkBQ%PPt;{!{O;bOgv^0hW4;vDmS}TB4?D$MP3-yLbV(za&%#BvO^MjF5<{nu(aBgHRfKC~~vc!IIY#CQ^{p&e5gn13$4Rv^2gg>*I~tXz;~%5^ACC4s(0-*Y5pLE0F_TW~XPfGS4!dT`W5rX_ngBr6<XhC=c%i^rW5bok@wpI^pO<D^v+1NfP4k$CQ(x^bgDOQZ5gsT>n6@v*%oL?B%G7Q^LTTG;NqyML*o36g_!cbcZic0oW%jThj!k6Yj&5=o9Q-<SQBGVw)i6U&U=&@sjFKq1O8#apn@NY#yw-27j|#Y(D%`7@t|+7~BC3me4<A7;owJoB4Ra^@HRDcov@Du7=OUfBa&L=t`SnaF8|cE)^moh({-R<H(_rXh0PyZ@D|QvNlN3Wi{?Sx1}f~%mpB&sd29xNQ12I1JtQ&eVg557Av;NP{5exeyzZLW67HYWlGqUs3bI0n1X1a<^{7xD)gk+3D7V~Au%+xWK5QN(GI#H6_SKL(DLi)5Ro&1k>vy?B~btlgMh$K|NK0Cnh^<ZDfO<_)XgU%9mK!<He>YnlhbBl;ZQYrPZYJ+YVQ|ph*aeoefFn?t`kM=K=Tjo4=7WZqPDrD!S)w{eVP@uyJnv5RsMmK+Dy3X&V;mC=I){jRI!q>SP<yUamXMv9H-TQzy!Z!l=fD0w9e1W7)kv29@F<=<u0O$5pGAn_au+Tj`b~nkUkgeDO!CC)Y9@d^Gd5cm^Kny7JoC-U;HN*cK>JGZ=zDx{gA!Ujmh$Kqfbwk#bXSP66ynJq`QZBM%hS?&-htpT|W3eN!ZDCN33W!(1pT4*s%(7I2er@D|QKAX`AynVP=j4g@wneZdG?STy(h7`jU}u2DZg_zAP~^J{^+PNzp<ZfTa|FVIy4-<3`8s01dyR#HA*BN0Nw(q$AP5g<E&IyD&|>GkS2x)+fICz+Xv&FTW1G$ue&htVGy1Q|ue({A}z4<cI0TiUva`%?I<2Qgb%^=@03*yzGrGOOQ<Hb`)b9n-=Z4dgswDIpYi#5ToHRQ`<Evz*1s?U9hfbW;0_jq2Sr%9pIqmx*XlGnG4jmK{$aA@I15z#vuA6xr*HB%BsH$y2+cGZ&!gBRWn^vwjbFa@9aAe7(wsj2whe3KZpq0nyRqPMud?E8Tg<ASf^j;{mO*-SbqKWtL!l5*HBRk(80)T5y92>=uLD?0K#(9%Aa-!fN*2Eo+Dh`g1nCW4x~+U5Ja4dvI2NS8!3-7IS9Tw*s|gQb7a%=WP~S1#lYSlSnT|%WJPk6Jz;BPqk=;~tvP6u=#@1DK=GchOVKD`K}m)wCkDN~OHETilZt3XgP^c_Jn;6W`jeBBB|X<kq|{7XrEkK+lE5=klb5n3T+GF~=*jJ2BUR1BOwmb7Qc)uq=4Ha#Vvp#UOC>f^yZ`t7)#fQR|8>;n^Ga>LT0Or?ZT>vAYdZ6%Y?)4Tm2Eq)WrDQna6czT@jQ)k+pmhu)0_vfLV3+K&dg0!n8!4}z?q@SwMy@jm}2w(8gpi7^Lz`E|3>f_Rur1xe2oid2;ZTF1_s`93l&Y#Yp(KYwu~bXS&o%gQ!<4-i_fD9=*{dnpXtwc%kETdXlJ%wZ%v(x)CWeE=~Hdyf0uQ?Zh196gCFAbRAoM18DBnF-MK74W4Azo$opY)n$8?=7OmBev8l1J)w^_ijzlOV%K<aG8hX0payBe^*%av;8bKvhnzmA*(dn<7hRF$3H0IBp$l7CVN6A>1v#@q)ohWH?E0@JD+LZJ=l(3xa1GOBhQ7|!{leTZ3jkT(y9dnb7YSXGmvr*QQc6s2xXw}df=F0CbSl2-6%&IJGOxYO6DWALb=C;L>Aak@+6B!w9X;LmtWVFdH!e3`XussLtNPy+s1&&5E8LMv5MzF=W#GtSo5X|f*N~xFf_wox7GqpU}GMose0j`-!X;CzZ(4_8~+g{Bj2b1>T1r*afT8cLW+ols84HAxTU!P0k83v_A+ayPAf(3eJ2gy3(3RkN?;8vc`TFkKYp&h@@e@*Szzqpjfh)-pcxFn5%*%|Y9B0Kga=%gU&MsR^de`&hJNJB*|<_PxW9t7;NwSXcyaA<_R2?1vc7UKqPY|RC(RpN@Q%ak?!^AcuEF4e+Y7pty)ht-gLB&w9yGR=<a4!}dL2d!dfKTW?gSnyzqy7-OoA?`Sx^<)9!9BMn8X(RFXbV|>%J*O<8HM^l+;Z+3FVG$WD1(y-&WT52OSM4c{U@-j%Mf3_y(c2Y4d5MrumIFw*tc&$|Rf5UTZZ!IAUp6(pVD?D~1M#}H)-j(o!wzm1YwkhL8zwJHp<MAJXdeEx_pc&+U0IEj64e!14f=<kdacj?p+?gVu9gs*i)b>a0ycxC?fJ>FE8ogyW=J)S@HR(LDbOpUsI`Rm_vP~b1@F<fS#x<eglf%|&wNO!*~z{o^h=x82J|eWN&ZZ)^W{2x+A_m0xxe72p900<_#MLNyNaiIgKin?*Kv5JpXDKm>8uxI@Kgw7e6XDtwFgpL%ZrCcBvc)<?G5$G@&sU2R^^k`@X<;B(Qq4hzGRmh3#d^GJpvvokAyoMQ(YHEtmW6eolLGi!5bQJ<Y;m@1|^`{B*Yt{33&=SWsSyrO+>RF3k&{x`3jTlWXQ`w1%Cv9RI!R2j*}5OnG5gnl|ywt+mzSe+dddgfhgs_^gi(V2_@1i=(*EuM~c6LWUo6I;>H^8XXm4zSBI3V1)oZV%hL50GbFbb{|dastfpBN`IwC58ChmPbxCO6OhbSP#3!jZAq2z3i7Vi)CeOecjp21W%2WmkaLYo3;SZs0$Xic%)`P%8<XI=hZnZ2CP0p|79^Hac*C!J+Oak<(L=k;QC4>8gV(qrK;^D(9iie+kR{LKB{wMnFPYbqOHN6jXUIE=?Q9`_7@o<R+Di>``c}s9C3My!r=cXJV=%IadTXOWbV^p1>#4Nil;5WNjKLVqrd>p#nSb8y+z7#rxLMoo}#v9i6HZq$LUX1C-j?aId7$yuTRFqqB<n+}u%^0NodqC65+LMzO9X|7h(t+iqJGPuch0%$5QSzKIF_5`09~4y!A%(;}JDC78)Y{{2-%#u^*E!!}-1r;Ipb#f@cSSO70&qE#TGa*Oks-ZeaN{(I!V*h_u_YI0pKzti>5M%ME;WW3E)uGRYDVU32!xXnqbU{|4!VTjgPW-SzcpA5cWg$45@v(kj>=V&Ij_j#BdS!?vDr?Hvs&R;=iv$;Ob&|~m5Kz=X@d$H(IzURSA9@5wI#LD1niBSLDG+b+B*U6O^hu~R-B3z5>E$rM83W=O_)qZ=E2Q(HCn)j7h`P$5Zl5vO8%f69;IP|L<UFMm$&?~0nKmRZTaet6v*8YCrw%1d<U(@Z4&O3h+0V0rhFTPuE7RE)HT+tgPCBXG+%<lTTka%(RT1Mgx^P0+m5W=<KAx&I7pyh9kxNwd)mX?V#68Lc9l)TWHMBSVrLDeQxmy7(@AQmEM?YLl)nRF^^ul-Y>P~kD8e(F3ZX+$7CeV8nUuHif4FUT0FGeiU<pSStYWvJ22oCxhH|}8LVQVl#G8*oC>Tt)oH=x(L^@?(H09s^-5f1148S2pYUO~h6)lGvEyo%y_m^F4uN5G!HQ%m@)0tdOudVegR5l{Z5OcgJODDacl_uT63VK*mUbCaF)ac5xGAc_WV(OROAC75<e~@^1!W;-PuPr}6W6$-8@~V*=8du}*Mj)GrW;K=rVC|og1}j3;9oF(}90-fwQ0Y42=1dGkC(Tlsx!zmONrG*n-x=u_+$F{q0UAP(&9RbF+_|dbUd_Pxvjm@er*M?o*+QAz8_ImFM2RTQ%6&6~qEP*v(c&l3O^)^!4QGE}N%J~X8Ebb4Tyuz~n|jnlwHHieiqqhZi^aVuniyH*fBYy@cj-QTHg!A5igH=@ual63tOttzClh#&uobg6n&LA!h)P5-dowl6Td!PLZjO}R(p_tILTkb_f-!;nlL_p+>`8LdFtwW8qI?*ffRMd69ZD(D)O1(skT!4oI&b4D%N2QXRyRr2eX5Uc;~kazaP?vk>i#VPC$|EaR)Le-z6yp`b(3+WH5Bd#S;E+)?PtZIPoZn_pMGRTt2X`A)`h4Qb`uk|x`g037qwzbCI#hZMnGO=TIo#Gs!=D05@}V>5SC-d6HzOQ94>XO;#y=)4b_=<PSw6{mbT&suB>acl&d?Fwi*}GRwd9VQ|eH4t^A3u)u1$s9>Q9xdhHY|T`Ow_zmR6lqE??Y!TRg(-@P2U>V2^8W!;-zqAHzg{k^qy8BhGNNp7!Ne-sB#Z!yPC7tOKb${9OUXY9*be}+advTj_+{lzo6zkXqk9pZ&vWzP${mlMb<<o*V0OJe6}ZOL+|EfxQ8a8vxd+?GsN+meJ9Ej+P5RZr6Y8}GAme+I4-dXH*9-YxW48CDEsXm2Sqrn=ow`6JP4x}bCpKn_WhbV6}}Nx`j|I6uI6fS}8XvQCPpDf&cPdl_GI(2;<KY@ZWopfqDSfzP>uj3h77ls7zcc*4=`!H{WB7_;hjbC%qSF^fNaMy7u1%<*6%!kP3)p8UgXDjZ_%Qr}|;=;kZR-!68>LvX{!*1k`>Y^DFo?s*y3KYYcSbt1U*!k$QG>8b#UbR*hQ)%nvsF`1SCw#5#1RSZcNo1;_TjPzQ{?V1LdIi|1Hsmx3!4olTJyb&(x9er%1i{Q;-OL=Wyq1lic?yI^$x6+<V=CjRhdWo+9xYpv+Bq50*X20AhH8f-_5P^{+Md!e;NjX7af}krlazJfS5lFfS27W7B=K=*WS!D;?%?nJ#Kn-46w@|_ulTw2&TR%0Hk$k(h6!^G<?oYUX(@%f9d%pMPEc}Lv$ul@M>Mw*lN}7Xe4JDc=g>HFd=mFE89m-JYc!)Frj$JU`uV=k=Du23@3>d^Lx@xGkK^Z3<?<2(zgZTO*<F%-1N!;xq(rGykZ15Ox5!JTSGdEIGv;*#LOPU^)ZEYA!mzNC(emdmYD>GSN0r?lcAa5+bW`2m1Su&dmM0vr67lDqEtc)@D9wxLuadD7liuI_5YXWhOHPdaC!`z4*`Hao$>7c%-jL2g6U%&ko78pi%7m6$f7#S|*Xp0I<%gzXC_9rb#XtWca(7QU%m7@V{Jl9#ub?JSrvj|`$x}P^}bMlIhtv{|IX4MwaqFF65(T}r~?P{qd>W<6i!L|c&`m2EuCiW(HQNQQ(?NUqfxG1&A1?n0WL(ZDZYD@oZ=wJNj^FDQa_W?Uy*T@0MRjJTQ7xfUzXk{>cUQ|%})?-{$b_c<`8}5wrXf=c`r6p7qTn*R*>jv<*<2=|b$_YdBw2&(j)1sadl|<ff*oFlXzoTFbd1XTsyw3EA>C<j7KVK`2>tf)l1~{G%%#Ned;Jhdv%w<3o`Z*b-?tQfqSjOhKE(5ZtP_A>&LiHRjv+sA>BHsZ?wjs?6W3UZCjlOxjEXU4!JofRw`zXue4gkE%%c7VbuXjHwS9*80CU#^bRd4gtH4z~)+wlg|aLEXXR<vp&S}SkSv!WHcVe*#lu2!8_7>#JL^`dC?8gvFjq{)p5o)QEfvX|7GkBzw&jAykf@~1Vdj)o@>WE<h!j=inRVXen|w-DpKPv54B)h}5MdyMIOsLmin`W)t`K_aJ5@@S6f_izlB5n8s1r#Rdy=wS8w9(Pi7Lh&3BZ5<U8Re%F)*aAw7<{N~_!Xr6Gc%`a92@~VJfQnQ>vVs@4tw(3&0q(5<g-Vo=%hi4KGOH@#ZXE6fwXo7clU0gO&R1Qm8$m@L7y||mR4lhe@DfdC)B>WCc7?{rWJ*982ry*cc;HiZq(<u_!kw3RBj8$PVjU^{%21IddE%j~=KaBk@4iin2JC_B*-)c=1S%+qRB|RfgJ=ld+)K5=Q>`^ij&hy(RGON#WC!*DI||!XdZDE}av`y-$I62yIMXX3T58^}lO1`BbqZPuCbey)^HPf%))bMB6cMF7zNS28BW#*CR4JP{oqN}ujjCD<;WEwch&xL^AflA_w<g}eo{d*B1=9rwQBOA~+${+TEeWFHU|$t3!)&L9p6oZ5ZU6ME<&EdT6{FFs{UyXtzFn0EaaXJ2qU@hE5MtHkA(`3oAR&b11EU?M$s30=dE=7LbnHn`Vw0_lMb4ef7uM8^B4uI5g-D~s>>7%cVnP6Qkaji8Hu~yI+&8UXAx#-cv#lD$cBZTh+stR~*I2;&s_g5HXK1@s5~f-#7#N`G6NNOcI9DCqHIPsfW7=}78U&=MZ_MoXHLLkp1t!{Q+gKJRz$8T}N*_$OC@v5YYs_nXY{*@j@aW)yP;Ff-Up0?4Z|Z<SE1lOl_T@fS_M_z?i%;=Yu({ddim}m)P60O|$$$BaT;0yjxfk@-w*%G-I5WbkMbE5}%oh*eU?TA!en@fq7vOe{*jJN>@nuJay})&g>iY@4E=kkAwR~`d0X|}&eJj)C9HN?iT1eSfYpAeL_X;=78s6kFrDHF<OyTQ1Mc|Z^v}C}VJyY{BF`%VX3q?2gvmY%r@PpgNW?}+!XG}o~4t715e=}INB4yvERBtTJPpn1x2i{{f$E3ZxG?X@Sd(>6Dyr7Rxx;>JJT&(O=RBCeT8g8LBe%hLzhNUWEl)E=%>Umo`S(tHg-w*}gbm@|<S&ZFn6wJohah9g5dEdO&Q%=pixG^YFQ&EgAEWs*TzidJDb%m1tJedJ&S$i*8`>-+vsjlmibdlhoeFv3c3{?)ihujme0kn0z_p@YO(?AV%S@-o!bj+sMGR?XP=4f@cB`o#>@2kZ)j`>_o$nF351v=@ccnRz|<IoYT=vRWQezAgw<xUw~)uOFC1c|APmy;=fwr><vK;kB`3${b}#@(wYP|vwt8FNI<a<Y|L{;Rf!cG~`Ilkl^i-@H$Jf=wd*4<FG1<!qDCXy4WJzpE2Bz377ys}D+p2^>#+P|RH7vK7ie@9A7q@_FZw4+<BVwtqx#ZYYst-P2tpn4S(YJv1EPT#SvxG)CG+qEf(BLzJ!>qDWOp(GI*NCBIzzvt}?T0ciHMW3zzpl&Z~QuiLoJ>piA?x;#;aS9zjXME8lMAO7jrsEHx(I+Pin9-ksk=^hY{j^QPiww*4G`)+ytK((!rYV`zRlxsYit1-=}hPqh~ZZn3T2o{-^8w;rSoh`VNx7ELl870_RYE{S=FkVzlzT^G57vG9vdHZr=1H3~aF-osxO#UZpT*az`BqzNGUstX>+H>FgebCy4H=2Z*XH>t@;!K78d-p_~>cn>1mbs-~7R(jO?Ed2aH!BCF*FiV(+a`RFJkX1=VVvju+hap#3%ZeDjehCv_@_Z)o$XG9)j3qmR(cEK{H+5<5jzcvy@(l|igYJoBM|9H#@jV)RMoG2(`XbEsI8n#`||KcbaE>ZczT47h90l-u717c`LOs`7XsEgXdfu7M(A0!#L#RD0hq~HEgr1#!nI&=<i3J7(!3&&2<<L5Mr<KymR(s3MAJ<#H#t{4*y87)w)oWtI7pz5-#50h#DD%9b${q)dzE-<uYz&i3?R~;!j23K)+Q^oZ#=Vsh^>O%o7*kZ7}K3gt+D@Vx0T^Vx0P_oZ6#N?m7O_3gzIJyE31{^-p21<cisTB$SXdO*i^Y=Z<SQf-4#9cGn`@`i6#xFN>hn2L<Sw~mRF#TG-+@RxI#6hDMbfC(t+$KDK@lnkqH*Awbj-1YQpNcY(Xm`NXWd0FvoP(oXz!ST8lQW`J(Y9_<MQ%11qN`g7Bn(#W+_oEbS#)9s1h?VYD+flwOh}R26X*e7Fm*GwZz6fz96rUT9UvJ^Jv)%j&pqg9+^=UO*JWa;1nB9h6O+PPiazD;-U2c%;~Bp2wYO3=8cefo;rz{bH2Sa!9oGDEQ3-4%<s64?5qDO#nAOR~gzTw4J1P3O$>9(wxd+XhGcz>XRWM7V6xN_a+uQNm00W!$15Hui3^Fnd3r{8Ru57lZn#mI+4<!54u8jd9Vm~aSS#CF{z$CcKA&k1haZVXEkvh%X<&eA}u0i4&TY4gou<o;uV^|6o8lztS`aXhL^-<_)<Cemp<5qk)_wg@g&XV<&avS%}z#D@1?@LSkt=3gyn7{vRSh1B-h~uJa#ra>p`?&0;<wh!;4~y(&9Pbx&qCLYm7@fR$argtCWj;<lA+D<DFFOI0QN7ZfXlp*Vx4CWZ+hgb04K)rOohAF80Q$$%TRV&wcdCd+B0_cx?)kO1Z1B<K+g@=5mO--qyo9na)O-nzwdcbzmvt;=*fcmutU|p?akcPxH0M$leh`JrLumYkwOhYPy{Asc!1a%OAu$A?*kvbycboTHTw_E`Q0)<CFXI<sNK*29ao1>-NEjgwRJ}19z&#(Bqi$XVfJF$qq>$uJV?l1a&$n_d!CUyby$&9;wH<5w?db;9wLY33}j-<yLLW9%tZ^QLW)Euya(23CC(75-4tyJA@obvdWmcl!PIjAdb>pKsygTmZ@S5$+Yanwca|Zq9xyai=<j+mNSgMnWZRMVcQ{)0D;LB7Y>eLafJD?7r~6hKdYuK|3!N-gE*R{D%z>eAN9!Xfa<OEv9c5?ghQ3+l1pbQ2_!Yw_;H>733nIZ0FR;mL;vgKjIn4MQPhZ2!iqvA5(I7&RhAI)4v4Tn3+d;FSi-A`;mAbEfQcswvD+R1u%Sat1dF;9r!Gxw;%ms1S^N`i7V|_@nJSqv#Gwwp+a`hqlA<=>A$1mq{`ZxP!(_|pf<f=}-(NzWZiaFbA8S76<s>F305Z@I;j8F2Eb$>v<X8TRBA`Pr3qQ}+u^YkpBWRv&B%#lE7%#Cedgu|LN|T!jmo0Gj!j3%A!xZ5ZoSx_g9*lIW&|hLkTt>i2n|l2k<Qx)>`^v>TGVBgS0yBQhluu7=Y7Q84P98iw&nQW}H^~Hs2Ew|0ZK}wwq{NIJy@kvDxAcQJ{;lDsf|{&1)ZQh-F)DH_muHGxF&KnqR8`Z^#g=kRC7j&^dTp|k9@)E1BJ9MUV<c~k1$Jt`uR^P+n!c*zcj@OK8S4g<zQnVgII14Z@T|Ohi?RFzih?Qy)}0zm@EWS$hZ3S1;L9apz(!Sl=3-gdH@=GerV)Xp?Q-NsmdW~+xngs_wJ?((_c7wu-?3CmGHV|~y*IzoPW?RQIIZsZ?ACVbCyd0V-pjPt64kU6@U3h^$gf&jHJG{wcf~NH+AX2VE1<_p#@FBy+*cN<RH&(x#V(gpDgX9Vs=~UYrwQgSE-&%#W_@P@zGa8mSO!HwMAUQcASp4c_oC!}^CBm#3%5~Kcco9CG;#W~CL?gbc0ba3w0sf2@u`+iaQE+^Cjifn&V|~xDN$nTEjSNHcay}FW4-sr5nz-mXA280RBjD5tUw}6RB>P_tg6Ox$WJvSC?Bfc7}rq!sVer4C=oZ-F9D1+Jw4zc<YqXjc~CA6A90|vLgxQudQ_B~nKsgyX)hz@{oW+v-e5C|((J*G$9nRPYYl2fW#=5MuQpQFAjvl^mr)Q%#jfQ)dTFK#(}<Ki8y7X6JQ*C;hyn*TTg2!{!dB3`<%V&mSAOF+(n<KMGd3)KP+;ick~3$;%P({ozZR{T(%_;spJ7A0K(fqSm7&V~HA3?RuzaW%cS?XNq1j1vt!vO0lOwPopP~425jkB!x{Cn$8H&ue=f-R{ks08b`kB@ouF#s%E9%5-u29jzZBw}G)uUX|npbV1F5DSNG<;idq7482U-?=i^lKY3vU>PBmh%Y9-Sg@p86DIXI>9gtz&udPcvU)V+Me@1Savrf-fJD~tXyb=R6Xt9v>m!|VVl#)I@{x30h4#NTv)vaIW|`nLmQ#gG}_dnVK^xoN_iN${(`x|s>5cBqv<-oR5zrk$QgO#6QN}OgR2%mNA&h*F{CYBfDSlYO;l-w-6kVFoB0m~ZXzwfgg*{iQOMBQm}+>EzI2ux5u7ndk2m{8<fo%jh=uEpdY6gxTjeT-+mM@3=Zwxr0d%g#NzCJLV$Q>8Nbz?&h@?3so~d(Sb;C<Ir&2Qf?DLZ<Tro=d)t0TmSdM1lR`wRYS|E@1_E=qylM}BW!#0M+!A(a1^U3HI-W+>Ebq7kO#$s>enBnu@NRK(xHwM$bTb_fAiDXhF6C~VLQ=Bp}QL-rI_*9{2A^ceRHh=O})<Cz|E7e=X5Ie@{#`RlfrX30c-5%}Vj^S`d%qdS+>J%q4HGwI>7$DI)5qpthPZN2*2Jej$3zj84csCBGfviyaR>0KvP)i{e2yel=x<E2Kk*Ot_ors4hVLFytrR_XEUvFZ>V^D&L6Da3{wrp8m`!aap+neW8g3?}(W8(3|PfUpoC$=&Hwt#dOX&61M)q27Pqj;wL3etv8J)JP42ph4_Joy2;eCN4$2Y&kh{;iN^r-I3@?J^%h+#s&S4W>qof!FLyqU<k=8{ATqJycQl%i;!X{|WAt(p5Qjedt@14O|O|6!5)T++b6c4Z84<RDobUe`Bz+SIQc&#G>nOFs|-XVKo028@VHH`o{{3Mg~NSQurJe#hBxju&7+5ejOGi<BD7ei!ih=g++AmiT!D0)EP#^3IJ(Y0C1{dUMK???5`(PKGMy{*AR(_$%UIwXl})E5h8_aA<}}~buaVcPy?mzBv3MZPOi%6a7G+x1Jc(JDKJFp*C7%EhCCUP<8PwYs{d;rJa%8Ku-{bdo^0p$bMxQEDVFK7i*$2|suH7(oSjKv2*kc}oSLkB&y^~K1tXEse5!ge48GVl=*}3g;*BYezakdhujTK;wW1Y6KW_|JuWoXqBk2g4D1g*Z0R81?{$>%)Z_6fI)r}5+Gl<Bh-+CWdY)8rUTc8G0T_s6fF<?rf?z^DwFfd~sdyCu1f@E(J7qpW>O(&vSBy|u}&NJgvsI-P^mc)KADfhy&2XS(S1I>F}tEnQ^V@ZlKfV9|Sp$feMIVs?yv2XHa+=%;R5~nvRez0kRDzGU6U|dgX>>zeGY<s4%aFnwS;FaMf%Apraw{fOw9<mY5dWLw@OQP=V*mIFQ!C6a&PpEB_{rVt^u4g3!uVF~-ndAcX1_TPn5dfTO;RYyFBr1yTIGmA7{HYgx6yE~}c?l8LSJYTWY?4p0U^R9-DBJR8mKaSMd{&%}Y+M>CMsm|`)3ejlkd7TgGg?}WX^H<r(FfOK4gQM6mrcYhgXI_n0h3KU*E<)slPq?O9g!9|#T$8OkOTnL5bw4ndYbAcHQ>lgL|94b@9&)f-z%OT47vw*r*Hb1e`Nwq+r~UpbI&Q|PE~c5WAXnGjs>4|k9%Xzvgk?G3_DbB-SXr}MiDz!p5nqdi9lzDK=(ZFVzc<d^RjF+S_E<3Or!L*1m+^1%NS_ZzQ>)%SkV(+_%J)TjA`ZOYcqsFjYKukRONgtxA)oG8mLTnkdJjTJzD!GpBM{L$o*swuB#Y&gPwZ(IK5sP)FhR#QtD}xtmfUKcwpbo67iWm(QIrgpOC#p6@i+0Fe~DNol<3c+Fu(RrTXvc<DwaKgxJo(_!J1#qVTti(^EmkNGNW}&<j>>i-&%3{4ig%`3T<4=MV_KuK#>6qv9Z%V((&I(H=tm#MB5iQtq-FRB4BmBF2rIydt$h>qk4WPQ`efPpP_*G%kr-vUnKX;!u<B-CzA!`9Ox+&KzxtrGGIckn`QwPYD2*J5LEn*qg%t&)&QI$g=I}LF*L}D<UHwm6i24d!Ku5`#$>K?(4qDEzuyfCB_U8APdVjl2KbixIw~}QDYvKklT%ogt0NS>>gN_EZGb|$ViMB7>Nl?usmR5+29^v3_^lGz$4c8eZLit%&gi~`<%1SX?vf$RW~auGct0;inV@^?~!Ug&{mLTUZe!8d|;9l;d-`|6&YQnPo+5@nB*a+I7|6J|MGgNB?Gf=8r0S%O_6B6Eal{HG~r}UkOk$I#M@NY$44Wh*jH)cI7?(<bZS1ZS?2=);yQ(s@*Z-zSEx1B^1q>E;L8>ApHaGbNvr8gE9m0+QG4hW`P{ga&!vE3Qqcbz?Od7!AfB@1^f~R^NrvQA6Z1kl*G!LV{hpcTjeDOS$wE8VnoJbVz3pDoVOkQVza1T>|KscGFm;@IeRV>fOM#J!qSXm`f>Y33eYI{j@K0#Z^l=zV*rJ(gifRmXq>gIP7?vUhUOLK<MBxc5x>HwXUOkDfp#FhjDY$M<$!Rys<;a!_5B#Fllvd#Mb*l;T(=P(2Ym!n}17iJ1Y($?;_DT!qC*plHr<Y8be`xG4+D?f#D3r&d!PPBXW$lQ)-6v`)7ks(+ZAeuA-4}Ha%E{hgmUXu=!xSNQWkT(!xd%T|7xzwbHf8KifJzYbN*$+ddHo@XpVn7tKI!|l+c0kM#^X)c%b=L(ifsH~7GQ3|p^JAOMjPExHmh;t!|4P(X{i33<&F0e@z^mo#}%bpG8fGq@fPDFGMVkR91v4J2Q&Utj~y?&qZ&sEPws?D6UQhX?gE1dUmowM#MJ~*$q5|~<oR=oQ7#^z+Y_m`8tmWoehxgdwi?&Ip9%jSMH30eN>8ssLs^>?n$6YJIY<(tRqTGoXIYZ#RMT<t>|jr?t#rFk>j(U}h0=-P<%6%PR}9a2$tY$URa2i{zmVMEZ6^7i>?O!JS!P%;HHGqcOS3|3<%JGu@^kde5FD;^7NAu@($*QpJ(#M>oKZyQXD+u_doHMyB2IgAozuRgZ99K<wu<eeNyUlvqaB*6VWtkSd}H0_1kjx|U=~cjr3Oq@NnxdLl0RrCDHO8CI=VG&7Lq5aN`Hk5$&&@4-IM}u&f`Sl@6_L@os&AjmWNs@ovgK-6T^d#w*37=Lp^phT6%A(u58VZh#Y%%Vq5Z@;tgvpvC3Eh+-;o4l~SUvSQn(NwQp+n8qugD(~q&FvtAvL$)LN&?ea!cSlY2%%eQZ<@IvbpTEYOemkH|_`XsY+mVC<bQ?RX;X;rSEZ|sZ|!v{WqZi4L3sjPvWZc8J_LvULb0eZZiNq%tFf#aRjvY0qZsg}(4O~sz;;^%qp2W}6xP1ANPO0`mU4W5AE+i7ZB!GR{&&Tq}?K^E_|rALsGDjwx)4hlKvm}HuRUf)!p!j_XX)`U7D=k#;}_o32MJLS>*HDj5fsV1z>nJmeq#-x961D|xcRhRCO`N{U9n;7y@RxDVhZkmrc-~Z@Jx$P@w6AhK!BC^$zM6}{t8G|TZGKdZ{eJHHyLn6AdbG9O~v;%`mZwSStM#sUJS$T__qN(kxp8TwwaosveP*(<#96Q=dVaXFORV*zQ2sh*okwgxW^qHmgM_xFt?Q&f2uTzHN1!bsvitkqkwZ9<ywf-tW=qYy4Je;Wd23fKi5DdJaflq<!G0WJM-4+^lgQ)3<zuE^Huh85!-IR#QctH&Z^&m0EnUH0W7|?;(`ESL>A|dejd%m)n`XPis0s@}p1g<8fVm|pXLy?oCcx(K?^oVJcA6!$%CY~0AK+d*CY^n0=XUfGm3_o^%%tqm@54Udo;^_#z?o92GxUc4{<mTfeRUMqa?|^hE3$u(SXfzBAO*s|qAJ`5VWDK|XVq-8KA1-=%ahdYOcVH<$LRjHY?ZL6+ZIL<((2<;hHSk~u;!lM$5zEx0akMQ#HzPUU@B;6-I#YPn!-#Jx`(i(6*sM))-V7MQ60bA*w()&gng_1YWg=7Wt~HPw^cTVr9&lLYnPu&@+0e(c|7Ty61(iYl39^p<fmFf=k2!niqo0e0>41TH!!YXbh;IXw-aR0WCoxJMa280Y9{97o@fLyPrvA0%w{OeN*VxWAJW>eY(V6JPPn^u%0qc3-Dslxl7_as{Ah`~j_>j^#CSkz_S)UJx4G6|e?G6PX2@lHy6M;!Y0muhs*;r2De0PIiS>x74W&5Js{LDNCZ)}}t+D(WGvZSfmMFF^<I4?FX(F4Qv)>|-*5K0>)u1Yb9-4G2vs2s4$KL<jy>Srzf@r~M0*eZ#<UVL&otRe6yHi+fWJ~Y_Tl(sOVlDZYvS8tzX`dh&|4}Kh3eht@7z*&B__+EDWDil`r!XzN9FoM{9@Q}vZtD)miw3tUZ7*}z}XJk1VCt{PayZAC3^H3)JKaaH~@!t=?L}*7eMf2Ul-xR&EvaqE42mb}tZa0r1Kj3~pmQy+T5xxJoKalCiHs6B+od+;EA4}@YRS(`skJ$514;H|U5BT{8Al9_!V+5M_ILr<&1E6eIg2@M?OrGw&aLUr0cof&*K~Y^C@7=(Qp|#|PCo!h{J;Q|Ik9^1?>Y<goT0~3CwjmN{Prcrj6L$cHNOZq3sg8#rwQSn5WMSC<>{6-=H%X2jz{Q&vR0c8QLX4x)YRbNXs{A7Z;IVAoTd!=jY{GXv;<JNvYs+zO=qE1#hLk;zzU*tq^4{CUZcO=~5+y;HssXt1249>3H;D#;g@MgKm`4;c^Jss(d&#&SylS|pe)awxYvQVe*-wr1jThbtETDw9lzrhH)Ze3M-|w*H`W+IcP?Asn!?^MRVv%=&_{LUCzhzEmvG6<QX9J_qca0Ij#yZ1VLjHPE?$UO3hMslATm>j6Vdaq(t#b9Y5m)J*kg8%l>oQJN`>9SL-5|br$Nb=(TE{J~FzTlA5Y*bmai;4}4l8%(F<?w0Z_9Uj8OM3gH;QifZgzCHjdtKx6X<x`a6mGL=uTFKu#{EyV@uRKUw2}DslhGg6#k0$;$<v|b=f5u+j42Mv$8L%^U-+PsESAJS#v!$v-fv=0p6!&^J-~vDO7q(m<IsAWi9=`KV;6{myo-jBZuz8=B%>N=cjFp2Pi0V=4#qv0A4zC!^N~Mv#ft&=K7k7zi-;6C#G$DYT7dUnCC3dUsoP?K$*ECzDrJ4XnOgC4V<ud3CWzMkIhyU@ri{52k>mRDm6ru>xIMQROL6V<$!lU{ls>#etXh3?%p?NDdjp%+p^8wG`4DYEH1nRQCTkfW<7HygqrHi&1L3(uF7$`_mZJ|>EtaxA2?e%HQo)HFHg+h)=}%uY=PPhzw~kzGhD;#*>c;Fwv$$~7^AkH%N1zeu@DeU;rhuLz4e2)Nj*L_sn6D8Mwn;IF-l*`!o1DvwoX;e>sBwg#GpHqiMyQF`C?vgrg`nr7|6K_yVcdAr5^P26MS!qeauDB6$RE}!?<v7t1|{_Gf#GcAyq(W<~90VuzZNEIRmeEK{qs3>UUO)#jm)M<)cQ6#XZB4E0etzzxm!U_{B<H#&G{yq&w!oCTItrWlK?2S#-YgM=OQ>sb$XBK3pj+WbuuYv1d9?oF>c!nr7ovx@)m28IHK~G^jdZ(=l>P=Y`uVxp9}^&M`KK!qNb4UB|X=GR}%OLQG;C63FjVp9d$VgS`bm4$wVhzl;RRVF8cK1n(HJ=Abu%0Yf<wH^4~%;VM-Ov90s0&`|3@ufe%BDKtPfpwu(6IF@O)MhYQf>yG^P1~@{3f)kb`5n^yw83>6^>uJ<6feXbKCvUmoR4OCG=W!fFIJ|+%Tf)EiQUD(`RM!B$DVJ?i+qpESQ7YmSvMg1OgYm0P+>)z<m)J*{ovdD~JFI^@b;Ns<WlSb6i7I{;beG7|No>_~F;X3$ARP0?s+edbfWmW+@^-ALVOW-`xpqo>ncoF?X!Xcv?wB(%WqVu!ZI)9Skj{%7SG!Raqfsm4bN?tzzX~{R)UzOK_Ihqh{M_Q0bGIv8QCs$t7<Ayd#cC8#-{t3ym9M8{CuzW5Cg^@~8mo^}*KGc)Nm`qrvziSWG*ff-RV`=2_W6Zyb1gcl*gUIv+fYs4(Z12_)iAYIb%CZ$e=&N-@{2Rh&(DI_^<}l67~*7e7nT6cv=IKDm8R`;c>+-~^BVBl5L}C52fu(hx-&iTP)i#UD4&WPQlFW$!k69T#mU6A{`DE$&{vqIkB|R>`%N^AnqP3^XChwtc*1Rc)GEA1<u*Pd-G8j&k7&t7761|h|K#^cPCib;1}GKW`GN8tr;+evXB39aRSCO3u12_tl!H1_X30ZSh~9s=h4(o;Br?sUA#*_QY+vnnP+UBQH+)ymTco9zeA#NhNV5JmoL@+$24Z&4u#|R#GdxK!PXN3gMYjeoeq@ubIe39rlk-OO;LGTgjl-7DVnq{`GJRr96ck3?T~>aOrr>}`;sjA#`o5nG;@-R_oNQflRHVDi;-3gA&E9WTfO#^mWWzizvm-38Q-ZWe>X#8^fXLpfBFa}J_{*Tu+Z__D_C_$&<~+2tl!<FM!%y~-s2skPwD`-y%=cvdW-?(ijh-3z$Vl@AsT4iDz|ny|SGl@F4Kp|Ol~atV1m7YxjX_m%nr`EF-eA|ukW>7gw1_&V6e|<+H&uY2j5=3k0a?-VCfE}l$joy?ndBAnU;$4h-duR#wS@}2TV4K$=&JF5=$yg4c)?P26VijT=Rf`WVZVMF&#(K}Pb2(kgg=e&r(a+4>!+c(@@x2NehnY+_VzV@ZNHY&{<6P*q$uLkME!_k+kSPQ)qWb=SH3+x`|GRT`;YS2hSjgZf2m)?SM+Q9;$K6hAxyt6&q}{efAz2Ub@kZ4=y4Ec_7y+rdHv**SO5C-&v5;x)mh`@ZA(_0o*(4WR)3uyH1_F2A=C#KYU;tSs2S?p(p{_;X`|}Wtn&+GXZmm6wDoGeT7qvdX9<1?K95#)Z-TIBa*L7x5v9mYye3voWejE$g@2QSE+KvP&m`Xc@?Gc81QWv5zsc5o`GV(<u>7?e@T%Z^{>J4q=1aUjf>m^;cg6ay`i)dHn#f1j56(fG&%uVVdh~Td2>NMw{rsBwjq@|tz79IIPYrB6ReR?7YZ0D5XMK=$6V6X^{mkl|*M~B0mxem5hR(P1iA^K#-+RTEFE~H#So<2N&zVM`H~fYE>3~W2RPxQ#N1h&t)ijw`>GA4k;9n`$G5yM)=0acxS^RZ=K3%@ceww7w6Muc~UApfs{v-#16c+@vi|>M$ZLa@m9)$4ZS-tnKA8^|93&PbGgw-?aQ+?)Jy!TJj1N{q&$H~ZR(=$}wUe1|V$2r-{!0=tX*965E2Q+ImK0Y7tXU_KebtHbm+qiw$*MIGwrqeh(+vz0dv8o0~=U=~0lBb?@e)V`7v6VmW6*u+uudDL;|NC+^T%1vN4GU1+wadAPz+-D9UP-RFy4j6g_M|o@nQW$S!**d$w+=rov38Kq&%IgvS;o}X-$<1F@WvyHwhD1o(P!Cu2XJb(lQHPQg1$*ID36n?My&m$SesOG{Q^N?Aw!y8ynI|2U=t>p-`G|)9!mbsFOFyLP3sX@{mEWGFW>qi)Iw*oCrI%qO;pzjTo5ZfeTg-YO>>xSI8DVO8H7ECg=p@gyKa5&WGX{4T$G-Hn)vMO*HvvX;4;!7{gEmeVR2T|846Rt>lIBbhyta_j%ICqPn05Amfb)1QgX@9Gsx3c{J=){gFkrJpS)z|GpQ%{XmaDhkt~z(0Y<>(0^Z&sKooMk;Ty}7JH5<@?hYeyU%ttmY>-6LL|?T%fr_KohkG`_IT8DNTI+~j`9N+cJm36QeRyU^U;K)`Tzc=9d+Xv}%w=B=gSPDn+I2l9UmWjgt;?^dMm{^n9D^Xld~EL}WoNV*^!*>uy6lLb8*lBagW*@deJlOUqgw2E*A9$Rko;&fgST|%=Z3!?^!Dk~!D#TKSYAN-08xdDy_c03kAF{6o5v@z#T~+(Kh!V6HOoc|FFx{9Fm-vfU&j*X7famF5~-Z(`exXrH1?@Ia;<BUym(H@5BsE%00!W5*Hgy19dSj6<PQlp$Y~_nza0Nqxx+NiBH+J*Ass=chLP~%SW1fy@)Q{dDNhbu3;}n_mPE>DvNef7LY0#((YY~D8>XP%NYO6g7WUMPNxclIAaxUx>{xWo34JXy9xhUD?@e1FWzH)K%b~MQZuQ=q=}QzrBUPqG_D1Z*M-w-YO%x?UCpD%m^+uwRIk7hX;WCxSUwCpJZ^}HTyO@{HU-|zVnblELd*}MrKipGj&%{@NlRa$DkPP8nr1%PDd)`)k@UcA4mN8t#58&_!nGXPL@MQr2Td^l50oN^!V;CEmfb)JBDwGx42Y7O)doL_u*<ftlmTxblYKIhepQ+%}r(-8YQUX;1e87){mquDH1NEpw(b2Kp`cn^F-;NyUmWtYM-?;JK|ImTx#&yF_5}5sqF(xOVkf-K<xr$HY?JE;E!sh)9saz)C5>Ar*#YON`P|TQ2Sc}@HIU=ne`WZrU1cbyNFCiqxW4i{nCx#3R($N@Z6L{nTZ_g#A^^_qI-kwZRFyzfxe)KQK-WwQ%j9q?BNUO(}LX+*BTinc&aVY1!Aq#MS1{k66ze*N)28`egLo(p~3X80dAk!Yi%;v?A`>G6ChU1u_#5oEHg5B(z)DB3|OBe|BCBSF`@qU6Df4vxxcYo3S7mGOdfpQ02B;zGH^9NwEHj{mMkozMjdT`x@SADSmm=<U3H!$iO9x0H@rEKKEp(xrz{|IUlWjh$CF98s9x$-1CpMuGlG9VlYu>{Pw)jArLd6O_1wp*V!L8?<E;Ko49D9|B0BNj>mVkGO%le>^0?Z>JHxJe$ylECe;7ytwnF+&5&XP|9vu&E{1C?UCo0zsm?O`<y_*GV&Fr{+#M5pr&{CsT)~sz<Pl(|FStDR2Lwsxry!yJ(Du5=`=wp%*JJ85roY2bXh$6~YdXwL7V${LV9@!UK&8+iFy(g+O|?9gPZ4)u^zmMukl^D*Ph&pII0cj;}N-Y&w??pm)ID%KM+vt1zv-3V#PKUsM@IMuk79Mun-Wl}r|epHqeYr&x&bSE}0iAIO|Az@x1kW{2&P!bheSWafl^HYa3AIXM$HUSDl8CroBeNR{WzQYH>bu8TKy(ipVRV9CIAE8hsS5_`?UpHRr@E9Qh{)7)J#CnTlVnLlBwJl}TVPnfDd;a&_&S`=amTX4@x1`P;+Fb@(LW{xKtg33H5MiB`ptxe6Pu%$jw7t%ZG4eT#03ghz@g-P-h*p1~+*tPEM6@NmE&&>-h3ag66nNeYLZd8aM;qdKoDa;mBykR)<)dv-o#CI*IfW+I1{&X2vtVw)HamCXlzIAAEo$vIXxPnT~tW=NB2Njt$ZHp*a`+60R?=qHPlY*M5BJ{n8%{N6s#%_vX(=3svh#M$*52$Pz2-2&Z<RB(?Q#(UV*Q`@2S8F>+uOgmiBcATMnRwbgMLd<hA>ijKc}xLD6svJyfKly)J`&Wl``3_5mYe_Q8Iga+0r(xbAs)-#6BB0^5}1<dBI9Ewug9P#-Qd!d<T#IH{L{Orgns27DqGA*RY{2~m4)@DY>h{QcbC0>H-g4qR^gF#q~XzK2c2NBAD8iHAm)v<_&fS^A2vM}Q((9ek#VB!3`V@~{Q;tPvS-D?sknwYxM}EyP%@t!wk@;#a`84^`#ANnLr*QC9gjIagq<?na`C8~o1KzYpCN@bW@;Zix>f<pf%G8@$GDD^1n0AK_m}{dKC;48PT({D2uMGaA{f5<!N(05i(F;homCSNakRHE?)(Ci!~a<F=+Ns?rA*c!{s%M>N(Z{qG!Rk1#A;P3jDru~>8o2Hrz4bDdu+G*(j|bop|UFGBm;Ele8Baw+&LhBl~?>gE~w=rH}bp`52Ti5%j=Kc45vj?;K9oU{h|aIRs9-^=VMHd?hS6>xJAvz=(y^)ea;|Dl4>vHSu0?9C0n)3*WUO9*HXW_L?6R78UZ7?mi|SMyMa;zT?pRCv;H!aR4&w53=h4n(&>DauA)}3V8d;*WLtMHrwg$3G_8086dPvFwYV!UAqr$^_=AiJ*$eJ3=PZGvGxr=n5d|RXfE&BNn(@iSgw)gcauR@}N`<D_?b9073&v?Xgd39<^!+!guUc-$4^SOg1}sdvo)1`<%2-`)bvN{DUd_eb5E-pd2nzh=ayRVyX9JeT55s!`mi+#J#UB#vzX!SnT)Pz}y#eeaQXov>TC{@t#Cw@DNbXP}PPTQU1VUO)e9_&&Tj78z>mB3l_WVA8ByO|N%iy1Ay2<+hF^H)GEch^tR+{|U`@o`=-jZ>AqjQ~MR$|VihBK?gn{V<~i0Mzeze2I0pCHX_r4p=y@niYktcjP+Wq|HZuWaH$<q!XO&*k1F^JQ}B3p%`%D^e!!8|FK*vT09b%gGRjEPpjMPXe#xSZ2=12vP|wG<)x;KU*OqHGhoh#0CIeRYsNgOLTL`Ptg_T;!=J+GP{J4frr!FfdZeIc@y^Nj)<WuXiRX4j#fSzd)UU~fp~t(r0)5GT)$w2-7x$upMEr`O(X-dMQrL*34%I)Zf(D{wYpPs+Hwxe3i0W8<@sBDS@{NsKlM6wr1JB#YZ7y}*d{1}M~OM;D_%&<9m#{AbdfqgY*#ha=hTr<|0*FWYTojIq;9-bN?W<rcx!42MJ4a6GxfQ$j+F0x=x6yHbQdN8I?rmSv{?g7opc%6<oWi_VI@fFxy|)bL>v&vWpcKMvP6<D*)bYEL5{UbEHRcm=vExfdlZMKg(IfhzXw)qSyg_Htk}+X2U22V<-@wvR7z}P-?cWZh<DhWU{9D7#_>91rcz!DbL$j#=H$ZbBa^ZQ^)4jUWnDVBG1_F6c6y*pEBsVbIE?;Awiry{$}^B9U}f68V?;+igwHkPC75BHU+${%LEo>xvT$btGw7R<+!|y|q<5Y0`k$eL>sT4MRTvZp$(i+ItKji@QeO`|&yp8RTyV_(8%sT`hs%kB!~UDr_Ywd2O^yHSKUvsrGH-w~diR+95`1VH)C<joXX`iIfhUcCKmbC^7Kw~6^AO5?T5gi^-ab3&qmJ!#ORz54VRc7ahe_;6Z>MPT`E2zLq3sYv?)YnO+F*QKwzVBTr9|c@^kpyx4SSr&j5+w0qXmO4LLP3swE3a+HRkdf-;HkMzEocLwu&ciX)W(nZsJdge87R}j%il+AyE#qu9rtSAF2no==JdW$eZ+fe3Sjqt{B5wnhuxko>3j%r=y%)LmXCSu0=Truv=Qnpy}%?MHrf^T*|`JEaB_L85yEZ#TkooUKaCLou#HOfRi?umcggx!ScD_k}Zi<Aq<ItKINUNG`wkFSDzWHFj!<|K@G-BZLssW=NmSt8UKL$Low}Q>SOvYgj=xMye+?KGv<P<)A@e6ODwV(%kz&6K7!HRF;nhr0t##JXmJT*7hw|=g`i6gp+pOYj*`8l#%!6zKf~L$yer)S&Y5K4K?w6m!GseJJ~Ea{0!=jhEEI%s<b-lC{khAOJh2-oS2u@qZtwjUPHH7FJSbdaWW$aRUQqr$FwVP+?Vl@QN7MTD$8=F^pm>Te4VyZw6k~0RHBbyl1L{>cSrw?!g=zTb-jyY;h5eJkg$T$%jK8b;8vQ_F7A}22C_ugjaDYy}#z@Msa4=A$55?$Vx6{}p8<MG#rp9DMkoR!vvr?JbmOq78%EpoC6IEAoYO^Gc0^uVSeuWo!?S5v<6TI;aGI{Rhlnz+NBViiN8J-KWxq6ErS};SQaJ!G@Eb3)IE-8~ty$}R61{0f)vq>g%-U$51J6keTC3gv(soTcCeg<NC=hH9w5{Bd7V~KR4JFY{-c0UW>3xm}jQCb*R+aoU~q;;HF{tZRpv$I-mrdDv*hLP7ZDpEm73<gZxKe_og+CnuoRH@|FfbADf_q!;uwU`yPMhgE@i=(9oPnpNNX1d3afcCUI#5Nl>5%^w$`P!Bz388GvyOGo6h;Efhx=jY!W~Bi|L(H}Eb#{pNOCrq#$TNy=%16X9fN$Asfzd~!gRmmx?Xe7%j^(>-u$ocJj5R;5@TQg6QsWFacjQJB9v7!1)Q&kwmH>o9y^DxMCXh|pvk(N8+_iV?YKHrxOh$0qkB_yz^KVN#cKk7mr)5Q_?n;zoY?OYM9=Q0ObpHT7a>&P)xcGC|?1Fsf-;6<Z#xlC&F|-1S9{?!uRsFVn>+fKDiZ@h~KJs4ftRiWR=0}cAAa<X2fqa0A6SpTslKUHPX!MXW&8>bWRqqYl3FXAf@ynebRb-9ug^n9d)TDkK@&#IjRPi8wbh*PDMyI%+ca)W5L0}|dpk?k;PN3ZBBi9|(YXy1i*!kP-{VfHs%4>1)x4%tdDFsqb*NVP|SjyK}s(EoNl`NJrG~w$+S11LPCyROZ_up|xXz5-0K|$3NQJrCEp4D8HwjV)d*O4?pE|^%=tMx1KwZl!6k{@HoXCO5-v{DJ>n~bhLNQC$+x>2;per5N{;D_dYjo`29E`j8p&#J2?l}es%1V43ioZlHXr}*I2QpEcy-AFG^G^!49?^epL{;bT(bYm*BdiUCl;}ufG-Ac;U_>VU|K7B{vY5V)#f9Z#}m_f~r8%o~&h%bR!WGh|qC`<bE80kK3_-M5_00FI``=0v+4*iId&rl-c2kK9i=N}Q7-xC?T%a|ACMrc_XI+gYCPBl3NvZ;G0>myCqT-uHyv9R2_aty^U@mL-Ytj}x|d=Y#0DD+7jAJ{v1keN;_QE5EI@!m(P)gmkkkG{Q2gjnGV?#fnpilTspKWO*xXTGE|FD*VwnmyIK)T7%gIrgxWW2X~avw1>`-B%<8!_#H8vAi+fR2B9rw}(kEhIV7V!Er|vUeYiicYvtZCd8eESsnG)Zy378TZEV<LwN+QxiQ<K(5ayn1U{3XI|?-eE6f<P4U(_^_kZ{}EsL}_w4~ZSp<mAd>yVo)#w>8a1ex2S%sk#BC`0!BV1tnkVRBapT)4&!lE?tPvC#BB?Qq8-nmrP>redW=g2NE&FaR+<$<T8cRA-_(9`RPJ+i$+_{*y8yS(wV6$z%Br?0sZH*pC6Da|%em$IKpcO6`G!o)a%R1WO^~7q(9J3dkH}?tM^Woq58B6p4&b7^S&G7=)pEpvosJ&Oi$ed<&rmsbzIzL!Z0O#t!AiNRKLr{LN7$xyWeu#wfTNlA?y%>6pxvwQiDGl?04k0Ftb{CKzVlE3~GSQlN516RjR>co_jHWox5uZ6i}al|o66O6U=E#*!gZr?FJgM;c~!p)rkZx^!X&V*qt)1Wxa;xAK#s>hQZ??5g7WM_H<1lSMM{fSYx%Oz;tWmo0!pF>C-*VF(#fT?dK@y`7_sIZHm)nOErM-pLP{5jm|>?qo$5MAjgl3kS!~JIWBUNrp}T9_ECjT1F=rJ%QzYFLGSeVB-WHNPZ|+^xldZ3NTSj`P*O00k-_yKH&g6Fdn&TO?+wp8lUwgE>Xbd!j!lpe!-|}GJ2<cuzZPo7VTNTW^T%5Uw*7%hA=?Mcjfw8W+a<obSLiRE5+&C2!GpZM`azUi8NM>@|u^Jc8P2H$Pa?C6~RDDU)O|cONg^Ec6C;S3~`K=107|1HyIIEZ*0OalV_(;j>KGxkfSkVzr~r)Lhl<hC%9<5UW5a2vU~dm4PO8Fs|;QvZCbXC>$e0{_uN9@s)k<?Y~2|;gbO`p|8SD8EBQ`@o3Lh464`(@A?ug@Hr!?La-;b&=q<dC301^$SI08P5GSQ@zsJi)h+~JxfuA+V7Y)}T_i%%at!`SPv$2Z+wH?Q>qnR`|-0}>Ao$2(F)l&%uF1zX;zwW4G*^WHbhBmb<xEcs1MwCJZen+X}M{nj`Hwq76_8QIx{x7+S{PJE?Nr^~5fcJx9O6{u#A)R{Eh_D6+$^#^Mb^{d&T2m&fm#AuByD76xx^JL-G?C|WIMa<3jo@Db9IK?F!cQat!YF4IIbZEuDHzbO*(NrlPiB-S25IC@(Ce_HxtcMwi^hNEJ#a6ivm_cwhTy`&6^1VK<<}D0Y`IQIEmyWiC?4as35RSjz67t5&>Zk<C#FH!c*<*{Hnf;-**;`Xk@5@S?oJv(5u)s57Y_7p#x8j9YSF@pEU>hlBp?xKf(~r;R;0{w=D+%KCTAZ=bKK)@7=k;NnVH$TYdF2ww%0OMMtu}y7?C&DzI{ivboz1}dJ_7otg77Q67Qv?E6lsjU;aB7FEp8i^Evk#ch0Hmw=P~|#zXG%fDB1V#3U9Bfm7K7)#Sma+&M0pDEqfeUNRj&;F5i7TM~GjC$#!^G9I}XlmU2B)W`qOD+buZodw|_8W9}eTe=<wCjcaznvN(6ADPFXb!$9KLeR=gJ2JZ}D-7$K?GXjsp4D<p)}yS^=}IWFP>IQI$-OOa-<Vz3rpGoiGPN$>4&7e#XKceP3D=%#z{XR#!Tww(<@cr++^VI6b3RENdWXQ0!LGW-F{!_N6X~s5J}wy|<<<fYyzyUoMXW{mZ+vuRjT;%Xs7kNpyc|`|tmUL0od}%ep2DdeR0lrARI3wZXdgZL^m;uev-((f@|VRzRNi$UmM1fEgN?uu)1_&`f!rD?N&(%=6(#Hd8P=pscf6?s946WaS3avhiAoZ^m~myPxyP)6@g6=6D_B`k%WmQS%7?7MCqhC_R-X5ywcy4i>!!g<<;+5vt8bFgIMyTziL*z6#amn@{%oL=5TiClAJq~ivJ-=Z)ptkWOq3LW2!Bp2_AFfn?l~=2-wn_%`20T8&zXRC42cK2seBMtgUreamk9AaqRa%GnoT76xbQiv&GgJ=hQPnV`=M$YF>7%mO!Z|UtVDaIVp`v`L>5peqs?k{7S5)xAC)x(M%1SihLWA^Ra_zUG+E0k+j8sKlOZGMfIn@yft&&jg}12XJZKoD`TuvmRG?k%husr__Q6Mg5omj&P6B`*y<f-Lj7L`1=?U$RR<Sl}bp-dAN3FTE?#uB6aieFJlCPFqXQq=Mh|Y{e7j~oE1-U+_DcshtDRi*Oq&c+Og9%pXeYHYIBp$S>BV1rKM&U3IOueshw|ZA4c<<$+g+2zOrf!bAZ?&K?=%z`EiCna~UUNzyMAJ%eqs|#47>$t4oGpeLZkO``&KP9~x$bJRcfEz%yG6LYxl)lf7x`~E-2NN$IxIZVTLTk4ic-)x@ccS#p0HJMq7k{0eD|M|sorwMiSD#d=o?@+aI!bZyRyqU<<{dU=o)FF-kc^{`faylyl1-f;>PA;H1#n{kU5A777X{E7}+7w>df3B5Px319)eNKRUmNy3k=TunVDjRLoiRvGW@&BTFBmBFPs@-H9B#Wqm>M*tR@4E3$&g}5@j1rgTNCJpeOGT+Of==WHc-a2TM;pd$|t-%Sro$Knj9aW`SZ6Ccc=zZy5YHs^9QKJKk_Z1FA$KbrGqiu|()-S_kkmLdw*hPAo^{C?8f<R#*kh!OCBpZ#Y$sk4DD(DsaHTxsbd0_g{<^;rfNHd)ZV44w>P9Nsxde-^COtB(;BIzO`hjC3)#6<%B!z9R_&ClV#73!!g2L$28td1}xu3?glYbtL(tGxiFsNtt6ItaBkznt?<cF8Z}W-4qLqx+hBDX(MKdOP#KpXs*;{4$s02ElH8Poha`0kbpFFpq;1qI8k$b)*Wr%W$|*eIw`iD@Dk8nr*(!03?O$Eevg3p6<18;!ffFloHYW1-Q5I{ZfYgcEtUO^Mj%FS)vuv5~aRZkb4=3+{*~|i2*dA1tg!^;~rgSDHC)Ncq3{4dij0B>Wc<ZwqO1><;4YvHs(jAjI#b6^*q<YM5gl-2VQG}7qMsa18BuRP$IX*udsZ`HDp)t);Jzn8-V&#kM%#e;GAo^UVZehR!O%788vAM*WCeA5YE{e*hB0SKyF)xI^rJ=L(I+H#mtB~24ww3aL3FMAxQ%uzyXh)eJ-fV1vQQVM9joj1_QfGO%|8E~POd#L6T;~mG^s6v|wZv7J(BcYMm_T1f3lkW^DNN`aFBA_-9J+^>VL}t+G@{G5j1=0-NI|#?qZjF2D$K1Tg+#9p2x&#t6R5m|=u&nyP1W7)RGTYj(U9>L%_nOv&xI04U}bJ&4HHB(i;5Hs+0sULUYO%84h|vj>bR`UIgne*6E_R~CdBcKzX_R>_qvAqZ#r1;|JO?;&L}$S&G9VS!qj7Y&~i|Im{M6s+C~&aROwsUXbT=r89vFHQ7ge*ZPeRLd~Ap$?(?!9HifoOjjHH73wv*FMQB7y4uDs6<Y9Xe$eH=+_{_zbyfD!8adEV|e3UD;VT;rA)5GMQg-%1vv1&mny($B>;aY=8nsE?QrYr@sR9&s&!rco5B9hyK^t-rI1h;a;0;fN!UfpT~XavOI#+GfZVW%s|&=;ZYV8%=-xT+5pO@ojkm#s;5U|ICp0C}MfY{>PTWkT*RPQIhq0G17<JSN*&>of6&a1c*CO2c-JDa%z;IIfIU<_-uHeuc(W8#pw*Os+Q0UvTje)&w0)k}jV9r4{&VV$LQ>AE5OH<QKcy`8GY2?djIYHC&$4ro8f&eP%^|4-$CADL>vaaZK_4h|&FmQN!asL&@^wEvCs`iv7urDIN~YU&;$o+}>iT%~h)MP}c4TcjE!<y2mb%N;)<^#)pGrOd;@GDx1^@)sgu5F%k9UXht5!CVp=u*_}s2dFQ|TuxbM0*z3E76>qR>C<aDmNzPs}NQuy5IN4~WpjIuMAgeFeA4O@Cj4IjJ!Rki1FIZMDac_>301<v|iP^~9I{<Gvvq5DGxNZcf;!D^i%Ek=Wrh1)L_vtOkAwAY|7BKffp@=R%aG_7KiZVGyqBWQ-@Pl|Cmiax<TQayz8WTSHfJ2;li^l7j-#41`{n!}KKYe;$aEZp$m;#E^m3h(LEGC6QiJp@}*u_TGLr1wDXGW23Zu5mYP14ykDR1BLjR8@^dYZ7zmgEL0?>=0mWV6QL&dd6+uj@vw4q2HCw4Ug~LSDM7>sYkqjzHw<h1RVj4lf0%Y2`P?N0SJZgJs76C^7eI7M_#UF*1ae!{Ne;ke@qpo@RDSd`&uQf-qYk#)UNLVkwpif&HW;k+RU(R1vALFk=ko;-)g#476>tc)nX{pav-kHIt!YJwL**==au@ct_)4jHh_1t2%9J+0MM-3y#mQM74jIL2xjc*o8Ny9Xw3Fy_3Rgx$St*mDQF4Fmi_bcmdS!eO*K5!P#m%5?Uwe$p_*L)H1ktLO=E@=|9*?if#t^#~`lJ#FmT-S~qjQ*s$T~Pfly`mWMKfQnf@gFm4T5tLTT^In$<;I{dK&uWalL=wAqdHDWPlW8z+wbbJIt>E4ypv%PWA8zmNJ^KX@Owjr<-p=7KIAnYl$Ew<+)H)&w?J>p1|bRG>1uNqW)M4plxE?Z#Ex{SsZegZfnr9*c5du#loAf8m_M)HDJc1f!+btj|jg|Ye|BW{C&q|{RfSv4Hg0z<QRlB7%{DTOpMh#k6bk+Lrxi=aNK((O?_3j~o%uxjtxj`3@UT`-~tRZ&KnxiTdqTN*gxnGR24HuutRWdx}w%L@CyevD+XivrEmMSf9J_L0@E1%yM%Vv7LV7IxK?Gg&;%0>zOWRaT)16sh`iUQ>n~99mFVf8!FufmJ01H?cmK`66`Qm|TTfWpa@$a*1fX3d$0*M>>d+rEapy%50u!5k>_7%UZLlDc^CISrwE!6qFCf)~2j3Kp-)yYd|(WHI~b|$)xbcB?D|!Q4)|yT-;v4Y;4YK${WxiJ2y#3RLQ{YM+_zY?w6W+BX5J3*C~V>ir^*mWYlmvaJTW#LWh>^j0JkgrXERQt9d8%5YB@DqB`&LYTjX(ZN@pll!GLFG2M7c)w5U>DQYi+)e7Cn01(M27L!gCCl+m0E^k;L_h&Goa>Jnt+#9eM?e{*h=A=djJWSjT7N7||L@h(%hH}LXAr^|PrC1|_^;h7nePWxq3sR*sBr)sbxAQ(6PHcjCn}CK|uxU8f2FJ(SV6lYw-~Ik<FA!N-&hZEtg3Tj!@>rNd;`K0TRUp-CmFGdSAf9f+8{YG8A8|L9XWks$q?vQzGwmL2`M?*m6kjs7a`BPaJ?<e#Rc6YLDdPzDWfVc)+=3^FI^`{AItDm?UbFYI@Ez-u<^J~vr}M-nf5LozdqC~GJh|UJX-BWx(XvFN(rs_1^y8K>KW;75FWXk(Tm%+-6D_2yd!QW76$(_dVXcHA*0M}8;|#a70iR=C9(=0m$aR`DNZxoV;D9So<2DoQv4cbd+c<^#CvSGY_EW7S#_dv^Cg#bB2X3_srEwhH?9FHZH%6$Z8Z631$Q8|)-R#-3(>kFtvGnQ@@Q3&qbcT~x32Tutj&tyDcY-otKUHahwt!&HCi<(ce_0oTTPVOUJ=jGewenPCJ;a&;A#Ob?QHZF8gHMx*eK2Dd7JACtnpn$3wOF+Lx$vBiUQ(-5(lkn1vUazfN>Z`b%Bl(cB-cO5&YPls{aLZ;R=sg#UoERT9N5Ne;w=x<5;i9h%iM~b%W9rua7|0ieBAkX_m@9e9e=Vq{$vyT>DNyq{Aq+gjqoR*<4-=vpL~x0@%lA<GCBT81N+J0_>;r&x6I*qawd-LYfO&)wI@@3(0n~6$Nt>aSbv=!FW-CB+jvC}GVR;Fn=3RGt3ov(mRpJIp%OVerL9#*Af{1kg;9jCEEyl#@QG$oJ#K5IL|Un4I@`}awMI6Kercxbnu>~j;-6tr%WQ!xz1J07IS^l16hC>WGeg{kMX{_Pr`PCDt53Oh^3hOEi&IT&C*ZK~Emp%AMgHs-7QZXI-!sSJ)mIC~5oykCeb4NQ?Qy>N`WMd1D~n<@n$q*;#Am1K=jk+$@Y<O;Tyd&?&dM5hT+EZjGJg$bcBD__$GJ556H`M-)zUL}%V&&=?V0M98W+Z>OK0Nc<EMRg!!z!@&l~q%`BVF>MR9oA>({SeaMhpqd579(4TeAD3x@YO6F*@~eB~1tr@FdK{>6XIS3G^E$#8B_ym}_AjCB{Tx<0NB;x7(z=}A08GoC&FtIovi(0qu;@M=ubYu@<8L|R)oO9Vp@p>wBaf8qUnIYi5fdqrhjS`kk_*=k-j!v58l!c3kLKfJBPacY4;u%xRxheLqHPfPxK?^BQZKf3tREKbrO0b6+&@nk-lXd&9IE{-?ol-i#lTSQsH)-(x$+RzJvJNP)<gk6i~mzgQFKHs<-h7TP#z3_mu0^?@yb9TqJiUDrXy}TdXxI>q%F5855l;ix~xkLB>S-*7hSvD#ujj7tGI8sP_dU&ilMZjoMzVg9+Asx{Kd}Yff(J{I9HhcjUkQnbBQS*4bOF%~hzSD#wN&8uB=<-0AI?wOzX-jz<Zx}Ly5srgEQHGr8G(N@y=>)q2ns5UJBRY83#Q|P6A(OxYAlv~)WkSF-5AFt1&(gJa@gPQwDFXQa2%@HY-~J4{b|=>kKHsrXYX8cRfn?*=!SBjMk>5_Fcx8+mvh+8`uxTL=P34NlR1OTQMPdad3rM`~OkM-PA>r&Pju-}v<yiST`GJj34p>W5!O%$^EapcX0M?=hcE%a7MLGrmiPTbXHHW5yM?|Wf-EjnFtkKj_U=#ffMfeADdH`GQqeN55QL!CdQmcd$@Yj8%&m<9sI6DLQ-2pCRyfL;snwrBVD^5Ebeo6|)``Tc*Tm!T@F(Q8!7i9G9_ZWd@YX4*anE;xgTIEJJ@&;esXVWNvoEDXMVy4gz!8FaI?I&4;4uG@ht^$SvmDc?%Bh$*BhJgxx?o61pp(Iv*G}rAU0xe}|0UX;z;SriDo{-JC&?cNGGQuZXoliqWv4dU5>y{{;3P2w8ymQ8wCE5`*N|-2^Kp#A`D$AYU22$}4=xb(I4H3&=@0_UCWvvlga8re2%MFoW`ih^Enr!(#0)K(Jl3i{|0O}&u3Va8>)(Fc=DmiRr3rOaZxMAUc`9RH#{u<t8^szYy)5Zy8O-Z#~V_=tl$;i0`S?@`RrD%m<^`H!<3bM}D2+jngHE3mvyG=np`oA?CpiB%W0N0lye3Js-Iqce|0HM{iJPwp-U3eGtRe>-2CG)0SJ!l`~8HLSo5Zo?a-Z;Ur1<<m>N9Simwqyk(8S8pMB)_|?8g~nkyiI(m9?rLcpd0_g8DaIsRd`j!R(0<IYey-mNn;y^%_}tDP9VNZHKt^`H{nR!6v0#=%<WbnKJyD8aFnDQua>^NBFd%~qh^zg7lWWv4HdyVf}_OLY=VHBF<0s=jQVbUQ*9gvaU%CXrXH)Xi#U1-qG~QnVCNR+ki<q%Xwp_x9V-H}cpbLQg??Q*{Xu99tTo49{W!z_`HP3YtHTeN$DsRPf-BWg13Q|l&Mm^VUyL+AgWF2%Cd0W0Ke6N*8lZ<Awvy43cpK)xVU`Vj;)#VuW6UB}9p)g69<4?=##kwEM+HMDVsy)3e*6Jmk8Y?#n`~UeG_9LDrw=xvtCt79WY`-hFlcw8-0h?%hVd?I@~AILRxoY!a=iiSw5~eVb+8*9d_AYra<C!kU@C*yNp2ypQEtEfR1L<VYgfm(tb~8`D;wbb6Qdg!Lz}LQYpCNI>bQn!T$2rIyc|^QhjcCB#43ZD9-#Gs(;aLeJBAm5>w^x`X?@rsAL#4EO^b<}))SX9r8aTPCWeqqdX5~<Q11uO^#)Y<G;uMW|HijvT<aQ~{Ay6+)oIH5TwhUHl4r`4*6g&AL%gKwx<VbdOhE+QX7*Rk@E-gFNyA`*o)#-^1mB}yuC;VowN*B7@5I!^5H>$@zYmU<iIxhNj+Rp@Mk^@TIJ$ItF!MJ{#qR2oM=^SYi4VvN;0yQQO33=dN19!_xIbB7(nL^gx8?dinAl=@WqJOya*)p;b5xGDx!1)|0#^=2sv<vVJW$+|0pjlhnZgfMjJAD<8ww0T@90D~6oU9pTnZKZr;YoJN+u(JEkR#bHR8hWd1=mGPW6Vd&;eO_gzh^)=WsLKBe?9z4#_(j>~Y&HCv|u*yXo@lj*#;aQb_*I4U&pSv1;!~_%S0gvg97%b((-XPwfrVFQ^^m_;t<MB;1MF1-#-(qD(1p3em*u&WTb%<#`kW%5Bs}ZNGsc5p-Im*wy%3c1wAvFk#943b_nGd`pO@!ph~Z7Umo7P~zu?z6}(FJO`K8c)P5>WlBX0x#cYG`X1=*+?+*4l(s21vXoEPDD#8Z4RT_eQRWDb8}qb8NKEa8K&3ydZd6M$lR;6^f`V{PN(I}%#&T)%tjJ{fwpQIs)2`IdI7!~nACBnu1wRs#_#Tuo6ci@CN(pW?Oc@0+WyXm-*{JZH*Gkh+HTjs9N|lJvjV@^#?#~$GSZyS`Z{8lq|I07EMSnn@Hzh+4l<=i=+Xe(06r_ZQ1qsX3R3(RY2!r8yW9!#E@A?m9u591FWdZbX8y@+1D5G_+K0-JME`5i@E-`y=>9O@as>i;O<jE~m%kZZMP$AlTXyPEWK5-_JH&K$NM~JlmA>2Y?C8j_5q5-%8QA61s!01QVaP$&MX<#tgz&iqvXn4tG*Tn$Q_>wEM^u?nTUdMV_IXB!(6qD>!87eOW=M3p+SFz?efy61;KoO4NmmRjHB4WckJ-2vE*MVBmP`WFdw+QrBb_wQFQc!GIMd|P<jxP>PDrqoc?~bc=2g*J6({dW}+v&;~2AbHF7lXqU@k%D-B@$_v@{}9$5M!Aj4c>?o=o8+8>^k!q5H)xlT85N;UngHa<-pvigI9CBFO%kPzf_80liKh2ctCO0#7C%|r6PA(Eg?8WAbt6)hBGEs<^iL4(LbulAQwZ`Tgt$Uoh>F2{2C~zG!6$DCnR~Yp2x<J`2o(3T!LizFrmSlMqE9RsVJf=Eopc}wpKBikC~jt4-dp|v;$I{PhtY5{3ftHiw{WvCdnFkXd|g%CN-8&NxOmiiN31uV|^i=#so`Zm7Ysvenk@*P1O_;Es)mW`s!WNno-t%{6GDPB6dQ>M;Z$T#<`7C+8pQ@#ZGfrgYy%$AYyGuCsV}Y7q2f9F~M6YCYsC41pb%0RXw2fY>jsu^m8emnyhp~<xytU_Hj7){*T+HU54~0mu0Z22DaFxpQ?eWW^;gc?ji`LO0-_qnn28ILq1kNY&jK`O-uzavIa_?r;-IS4%CoYov38-My5xQcns1nsMSL3S4b{K=4ui7;-SIDII510(t6!#dm2~6yN&|~^8xJpDqq|k{LrCObI@mrfKH=$&k{<xw@W~OE1ge^6&>s97CmFtpvY|bh?@>|DwtLL)+hSHC;GxCVDhJ5KaKFG5&ks7pXdu8{%iQeUHHUZ_{3fK#9jErUHHUZ_-)2r=>GBKE*vJ-f;4H3xR69#pyd@Q3tkRVI0CEx9I+rFhhZxBG!!2<`hs5|?!8Q08bh_4D0ZAN_)A*AL<q3gFF6gpz_3>+2<jwOcwK#RYZ@8LS61ls>z*-;ym1=b5|ux{tK$h|x8y)fUuuQc7dm*&c(6w5Rs8<M4AAkDuV{TAPDYgov|0A``3i|z@eHP41D!-Jzk)<H&-es36!mQV<YzT~g^8e$mV@SGJvx15U3z<as;9(WI%~TwnGX2VWQh9J{F-A?MMK>Dn#EOH(I)!k_qA90XP6UtKH52L!W&OwW={AubAlIZ!JKeQ{)C?nvZhd6=TC$Mbp0xYVgdP|2oMXr|A%ua{L^%b4|(H^OuvG}e?Qj#*^hgM67gl;yCC0O@=N3m@EoJ!Dr@BZFUZ#iYRQTS7pQ+<2?Wkhbc%4v6}a-=aQ=+HO0x*>`$o?bWj^SQ*T?D_-{ON$Z2I~xEXJ+5AYRO)%0|Wd#HN>p#rf0+E7{hnTjb5|Ey%d$l7aEpzH&)MYxX^(-+$HS=Tg5P0*ng@|Dl2w7W(~rdh_JuOpg6R!heK>|E!Bg{{zDt0`y;jaBZ%ZnvvL|1zcfYf!iImy#$cM{#J1dLM9&F0=iItp2HQA?-@ni8)h`NJD+=ZS5fWo{if+qc|)R2YasC;9<WIs1GL<_iU4ECv%&^<<*&W#ny^=AJ)4bP-m<A1i5vXyKb~QOEKSZdI2(zRUubZa3l4Pqtijp#0J6&wZK=VTq`{eJlOzvSfK6%Dke+mOvg@2&C;dZ)gOb|}RrXNeGgH2VBZC=s(d*I4RFG!Ba73tATWWC6TyOyW8^2QG1VT8X3z)NEgJme-X~artWN$`cJ;@J^r4(%bMYa5n3#j-|&D8yRM)cQ2y*u)k-dUOld<uK*uu+x~Vzn1@&42tM%z=gg>H}a^E#rJM+#Jvdr#5R$15PJUU{doU0TBVbq%6P61<G`(Y<d4TVYYMATxd*H&0wi12RUgT8~}%&j4g62G$lh90gXT~39JJS+rSZ!ZPIFc)bL$kDy!q3ssR9Tf^e5RVL9N+g5c|pAzZuRqTJAAgiI<-ih}}nI(TkjvMJg2hFw$PI)J5>R~XIAF&YOv-@}#7JdxqecH^>glc1H0EbYJhkG_;{e(GixHoUIeBwwU3%jaqfSSsksx?6&UlFv1aM`O2iL(y8LJ~9fF?0LMln0FO>78cmEbBW!muiHt$ocg-B;JUquYY}n1Z6JV6z5!PF*NN+{2_T1WR;~Yg{x>j>TL!FU+K)btuqBlIx_j&0TSumo3nR2V-Oq;fPiBZ#jvU+(09wCcy0j^)V+S?j+yDl)Evs>gFnHq~Bfv(P=0BW}8=RF|hRQ9JJC_f>-N;WRX%i`zVD#p!@K1S{EnTb`VGRFF$B4|Y0+~d1+=yF)H+Bf`qIn6YnpeGpMI+Eagc^dP;uBpcc_(=Sbm<kAs0kkJuy_!LuG}b5q%GNJjIt{!i&yqTz|H!OdlS_iB1zV`hY+EbZ`8qpPOzQwx7<N481HRl`DO-xJFKcf5r0R3HP0#v9QHjTeG)gdL4Xqyr(|nYqKO7b5#Ul3c?q7G=vsk$9_uU)2q8~~QLVRcO(|P1<4WA(<+6s98x!dtLwYxaeX>=Ue&P74q_o6eWB^g`Mf~YUlG1OS=2+XLU&O~_Y6Ws+Jg+`QM#FvdGD#~RS-#GX1H9#U8#$euJWYrO2k7Ng3p1i*g`Q?LcnfbVo&!uiBIdq0K3l>_%NKmddy9mL=_cc6eI2*j|NLQ_@^wf*7d&~Uv{xB@<z5uFzwz;E;3i%lF>y<3Utn-#q&}?*)fgjB>^|Vh0zIo`q@pz)U!aXf?MrcCvz2lE;fEokh;YX4)5PI5T)>MHF-&se*ovo1lo%-C(ol)MiDq2U*is(LT`bD))+&CG0Zs#<f59w{$aZ9UK0xBU%(A;Yalq+TprGu6zh{-4Ssr~3&B)^WCYJC2yiBY7gv$Zdi7~&9G}}BzaD7ul&ciL4^xV!cxxh(FCBEzBZX0nIwPf^~pRE=QI2G_U4xybqEhBadt$?mvoL2EEiI6?_LB9uRxb3i_^@K-O2r!NY`>F^gcE=q*^|Zkuh^@?pU5oc7S7&7>No0tFmw8(bxFI@^@Jre3YP;tV8qPa!=UHNIm`8!;3rl1u<kPTnGT7r+qcBawn-SKASY<Z!EN(_Drl~7Y8C@4-yw#a8W@5A^+7u%44)Yzu#WT+W#z&W76G#H=ue{njy}z*PxD!A*WUHSNjlV|}Rt`+KH8)UZ83*1e04SCSyAfOzSEJ=RSpwhGRhy4{S#{#qNBMvp;p@1wbp+R{)yKinJAB6I8S50?y*}6C!lq4xMmz?rH%^UF7BE$B?d0)^0gmXc?ZeK5>&t64Kyt#LhklhkjVqB@{o1QBq1m-J>xEQG6btjI_QGVSospquu+TCj6D*V~=K&#xnF;X@G3vMYXDYxo#+(|oVD9M#GV#S5BPV0Qlx#%>gxZDeC+8_h?PnGmww%5I9LqYwS|MBvPogdbneo6hBFt7mSe?pCd-{wI&X3_P)HN`#@S%uYX?1^-B6CgXR(ROR$N2xaGALgMr)G6=T>BD2O_FceOE@)85^DA@C)9+c5%mS91{p9)0F_h2AmbTY4a*vnu~;L+qi}^>)4z^f6XjHL9~O2F91|njurH+ckX*>L;YR1r%_k{>RlZS^ms}gQP~e{>#!Z9N`9&UO?YDsZ?*Fu{BW1b#{L5j>cj}w1){!|H6OW-mUf`{SY11>>Qo=G?T}LJdJMSiVIjoP7DKwmPlY?Exf|BC`UXGcC1fc|E9ZMdmV#`%`%D%=}C~9ziv3SuBfeyHItz%JZ;PabtxsI3xqW*0iEfg|&?mbInWog{oB2p&K-C`Z7RBbZ{t77>!5q1>WDa$}vR?;7Q`Q9j%Ca|DLASpXrv(?7J9rCs|Sk1+gZQ^LG5}1iM<(`ja7cUpKGjFSKIN*_r9gnoMLhX(IS7m`H`&`+JLbPJ!&uV$Pclz~FzXnvPs9Y4<$vz9aC8Gy%r0($i7kb_{L)rkBMXFb*#66tbejNGNla<A|TBi1w-EWq3-8YK;9<5gxkMtqYP;D9Q-ogf^Y`~8vM*~~Gp+i}FLQLHp$*HBXOm~7iGHT<G*wphF?nk`lE+fRgWgrN05^^f{HiuI`Ibzer7#U$GM=lxHjsbh%ENsX?*~5GdGYOpF4$~zke8j*_Y{zVnE3E}C18am(TRFMi19rS!f~XNUY&_UGR4eG;iu^onU6$}optg!6c>a>^@%Hwqt?AXpwh~F4cSt}@Vx_HpU$q=kHM7#iY#X$0kN9P^ygF7=?8Y^lU?E?k!LT=R49u#56}1){V}RYy>|QLXmgwsy(;>~tW<te!0yi<TxXt4N&-9-8l9!7V?8H2@p@IxEXn3A#<El&MD`<aqESt&j3M&%or=jDYThz=NXC>njZ2+Ia0O(Xc=mvH6#23VBIpyhOq>g@>^8P>jz!G=)wC@_N&(r9wT;xn-i-b0f97zvzc^_>UeRXEF3#X$5qA}LUvc%#Vb`X@AmhdvLU7*)nU@3*I2YBLTSxXw9s&n)~!ga>jFr8tpLicpT^OO%nk=l)52;!RV0s{#1BtzYMTh6BoDt^fAyk1r2ZHKUlywkLU=in#iSc96mX?3v^))BVh4+x;j@ZDv!o-(DXBJDPn7MeLAtKS{MJ|p!d+D}XGs4S-pp`F#e%M$$;p3yUCU!`X-)w(z54a!aXWOp*|ttmOkS9~iKqot|%MMp9%?8MhKZR5>(t9*1SWhb>DjZ50m_ZfwaWMMuw-OdSRquOGg5KobX4QOl0jgxDC3LEK{Ayua{O{?wG7=m+<Mxq~la)~*Srs^D|^}6t83|_XKp}X9erJzvtJw|h`obEdG@P2(RHUy%<-jq9#R@)s*3nh|5)uDtHX{Va)i5v4Rbrl{g`^QdvD~To)m@+m+R*{6~h9xP#afvB9jCxOtBJun)&8Fh5y`CjmzhUr;qcx=XN~;0lY|N>ItO?NJQxyT*#g=Pbwm+fNMXPJ<V;LuaLRDg=i?Ud$dNGx+7px0G2S&WctCbO;3kT9A_Me851hipOX_xRMN54KCO}(RJTc`a?v|cqOH<V1QkqN`{eKj5ew-mU-@T=hHGEHiKC&k=uJq9MCRA72;fj_&L4ph8=KYF<nP+V7~Ialqv_H(x{JI?{zb~*Nm$s;NwBg<=DN$YXLAUadk1FdyPG4y(w^9P<aZW82)W)^+YtUwXpAJJiCXN9*JB=;B`plebR27c}+j`4xoTYM$nUM@%nOy-^neCg2|o<@`$LA%6hY>{-09d;G`sXX6`^ob)!+G1j^CwoDceV19Xfmt6m0){s+Rt2{B-<W)%c8nGSjM=^AqOKjrr+ckk6wGV6#*a|T<Ep=rq=^ZMqKG5Gyo5-wH@Q2T#Au3+@QbEpJXeNP3lDH<MJSrtb1p${+mma`a?{Z&qg=>u7#o6c4OtE_@Tt;w;%jiC0j%>jRP`on9#iC!p$4TGDN{$_Cf-zbkqW|PIHEhD{;R5m8<??L*rv({t-CxIMSgD5qKZ@9sdZg0GFLWA<jMcdiBpV-!PMRuBH#rvwN;=Qr-bK2(u;YWlMs<0vIppWMoqo65wJ2g41KpUQ|q11Jj#0xdfhx=Use<QMya|Or{|-MYoSKVCGNfTCdq(z)#;qM`|cuiM3OjgeMpN`@n|pxMO(vJrG8ZIDI2$1qmQoXu;xybcQTQslj*w_c#Pa)Z>b5Rq>Wr2P`na0(?`23=6c?l<vCvAtJvO+ExaAY_67l7g*6OI@AIJIB;?nkd~$uFWM%BDsNTW0tTx(awSh^YAxxqv{;YN?EFypBw+mhd8NfBX%pwE0)@XkgHItU88HFa7z!{-tI&G>^t-njuOgEusth3Jj^C{qrn(JmLUi<5cVCYTSWK$GQW|&8_(;B{%bza_~6uu|OK;g@1jrQ9r?+Ka3&Fi}C-)yBR{qJ9DK4zA}zgZ*OT*KoJF|w_wj|uXjDkw!YSA|e63Q=>7iAyu-ccXf3oQz;VE|e6~vtW;SIUf(yokd=1mCr7^5-AeFfc;1~lQatrQ2}vsv_<SAFgUPWEo*9HnVZ+VY)=a>+gtOp4c{(1+rMfPbMM1<-!C&4G#N_>u)TsFg=#ceAnh_a(_~~rWyhYhXNPUII0gVknuBL;fZ31sIEu8yM(~e$N*Ww3NkPP$ld3Lr)C>g*jcX<5UE3+SKx!a$7HWktxJcagRmn7C<tQK8&hT|aairQ>q{yNQDGC$p`4(^mA>oq1Z9rw92iSPOMD?nrZB<ZLYbH}N$3QFeRx=6e9%Thn5a^Jqav6n=<(d|q{%`_-3wtP&1y&i#OkZz{xZVHUS;deweIHM(7)C1>md|J&Yq`*SjfP5&W$$hFI3((ZHzwHw-E|LvzJaB~@g#X%7VpYQjiJZlAAxoZaZGN^;Z24_n{a@wDh8%CW000x429c_1j}xK0K!Uvw}&58<sj+ElysvU@IEltM=IevKGPB|m=d+laj!-d)XTdEhMU?KTh=$2E|igUW@Qnrgp!$EtE3nvX&Wpsagc+vsTJWhqwt<-ItcAYDszMos5l&mS>jgJm{vCmms0Fb(Y#!&-SsD5-RB(3zW0Ro&F;xQ=kS~Yj`b(3&so0k{;bux=yT56H#2e<`G0rTpRkhRS*x=@Yjq;+w^pYCcM|1q`gNakN4@a0Y;|&4O;R|=3f{d(Z;nk)<dJ86&c^zjT!h)`#Ik(nj)DjMeJdmX^krI{7yV|fkn!f)+DJ~@T)0Z}7L8mz7&oZiDpKi{xio4E5cyf`)!Le}G?o(861`f#b;l-c1wybRs*T#Q8Pz#odzez!%L^UPZeza4)8&#BJHWxcEryvuoG9laRsbmYi_9jgQB9}?)=8Fkk|es539FWyZ4a0)UK3U4;gqsQ7)7QgPm07_NZ`7ZDuXeYcD&YD07=;F5$;F8T&wV+#_X)d#X55Y+BEFZT&oCe4oJrYQRTY3XCOfqZhC(fYi`sT{<z`h-<p*!f8qJ^_&V!(vff&?<J~MFTicuH|FsotcAoVlTQv}9HY&WZCOd_jsM|;kmfO2B+H2UeN%<R)##l)p4Hg%a-iR(^(;%>tARTd&OD;3Ph$0QT_+7=G5x@u+b5TS%i`jrz7E2t`wke589Jq4T&blokcas<}5y>4h!6WBm8bA^0nRazViK@T>yil|%2L5Yj;8`3kEz%fH9drf3C-n|0{4A2In}LoglMd5O(IhbEY^NCR;p0rVkA%nhs`jZfjkXEE_`-c^hU6q5!)iy(_NnG#pQ<=>@Ap2h_o=krr*xC0`zOIT@7bjO*w?NZy;AZgP~n==d3&bFom}z@v2)Xp_SYq(!z?b}=my(x?9o@L67!}nPZ`ki$}Kj(rl$Hmd-i)n@te|loYeaX9S$`RNK4RX)s)XBc5Vl3*P8P2S3aUN_aY*=VwFIjgtZ*7t&<$%=4p-Yplwtd-HR~>{(Z}3FbjTEQa#M(EG#^SHfU&@5Krc%({WG_fn*#GXPDYcCsntQ?L(UT5C1kDJOf;Lo1keDET3m*t*fydixx-@T#}s$^7j}>IWBEDkUN7sa)MT+^QMj^syg%3oX0XxW7)a>3->p_VxJg>Lao2p>s!XE+UKIr$xlV4{`sQPE@~wuw!CictOzEy6=SY}DsM~`s*yre!<cM_F(7k>#@u3*odq=UQMW$O^~fOQ+nPV90m%F=Gtl(y>=uK_)QEui07&}_Hn+1pp<2Z#r)Pg5oRzMzN-a%dfF2ICWJqQJf>uxy#XEyCb!Gkq$(t*v<o&3)ayYMHE()0b8?9mfdH0*X`T06=GVtNP3VNi<p~mdkC-ddn0ntUU7dx+>P!FBIXX;Xdp@%3~0p{sJ8!jsSiFz<?rsEf;FndYX@Bpnha9bQAUItD2EuFfWWOpm|Zxu=H2z&|XQU_ZEg2*kp_`JVPh8vgB*S#cXl)dWX&>cqCmF2B)8VMkereynt7=b&a{B4^^B}7x-M^ywQW&=%N-g88}p<-3O9qRU-leJ-B=7KMX1?*(%IGa>M??cqbjX=hm#Bq@M1PB%m%Ww^8%oO&{zfi~-z744b!;8<1Sc8#;bqW0mmPxS6Y~t9{O;uz|zi_klEGi-8p{9o#fbBwSCI&T|M1|+F0w`nboJlF`AA{io_9v{xGLrzYB-s%f;$cx7iz@AguCwcqI<Y=nH2jwYO+q92n^;eSms1I&b&H8YH#q<uke8ZW{phRxF4rYHto$$%4{jRA(aLne&yqURzZThiwWbyI%hge;Z2tq>FcZE?gS_}$6pvboD_89vmRH;?93Tf72?}_2WAQ*OO}%Eeqm>a+s2MRyv-Mj9JH8gFP`{(EpKIeI`^Yla28lgKg%>|(ud(ktJudsp&T_mmPt1Tag)=|OSqDLIrCA?ARSfGtJ5s+4uI49fs#OV?>01gE2St^^W*Ysz_^%>S7jO5RF!7Q9PXFmwXCR~rz>p=cIl8gZwXP9#%j%OhRGU`d(&Kh)7s0jZPiGc==iG+(RuftLuK2#Hcaf^BL@+EFl3cuzq0EYit8!#hn}b=7(3Tphu{hCgeMaUh0MlIsIr$s#tj8LUC)y6hYQxyxL!H`JqZP=eFQZ4I2t8p14L3p5lEXDf;IDnfLgD-CN$BSNN$83fl2|03gu<^COD&F25*jX&&~z;c?Vc`{>dIU%mLAm7n9HPCJIcr1&Nb50GWX2Zp<kz;Q|`$~1W5od0s)=zPn?GdRFseWqUi?Pep&G2n5+;NTt~kdSxBl30E|(2$AL#^wdp082`G0aCM9!wZ}0hQ4Gof=wG{3HAun}>!2lsTXklhb&M0qt&p;y(EQ9r7C*69+5y~F}9Awib(62MJG86!vi~<N{v`4I%EyIfPzxx9(DKYf%L===x1M2(b89HeAx~e<VpNa^CY3@VL?B*7=A?&ILi-~!AxnTz)0HUjMEZUKAbBt*~0gU?||N8Ce96UpkGQ&uOV!RnDt$~@C#1_tPhI%I?Cp*cR*^pdb+zI(5ZG-lVA*EcO_k-F7G@gsck^@?`pnb9;b9PJMemLrW_y^xe>wiPYTV(6`%e4Oad|-+6qVL~dY5M0EHvL^(_5C3e$Q!t}{^f}!gCSpwM{4@_tET^o1JzvPKv4uB+;`NV0BM*z9(vNk0I1`S=RK&JPFs_0cZ@Llij?w=;Q@NKrHuv+xG!re&)@+rnNS_O3u=dOG*HtGVQ=}|l<j>J*nt1K%-Q~uRh)n#J(Qe)5X~d=l^lWo#q4|J9IUM3_Q(ys;e(3%?U@DQ*FA}=Ww>q#U7YGG8|e?QOw!UKjz*sZ$`Y=)VX3AeS3KF$kl}HRk~h};PCXsg2&hnlLv7g}=!p$ZutQ3wdRY7TWL=T_8%nT++nZ+4$y*9Ta4=puv5gb^1mhs>NiG=#vy@ji67Azc!tX2eo6T;8&^Uily_ggwDUa5K(n!gQO0`AM-X%~Gf<EYsV|io2gj!G*DbhJBa41BNx*d&rMj$LhTx3Jqfp|}oBX3DCe*Qgcc;0+vtj>1w(LB&(d%0|JLqSg``PN@EDt*e0SW1%p6{#AN#8mAj+v4RX1f8}R#~d?ON=;qD+A3Jns6fg&7?@^tycpI?YQoOfnne|?u|^Unm*R)56#<v4*lG#$PcLD)!bzk_tLh;x$%aU8Tg7U0O?8EmiluqAV&4+nAO^J!0Zfc^Ce4~2>=f%dO&v~p?Op9~8nyYGtVI2W`wM=YSa0QtJA&LCs~C=Q2UDcer?#zf2f^eH;)8`Ps9bD_m!~gQG7Bo7dP`X=atLsbNFRFAH0;TIi$KOAAT}Nb?#_v{xTaxeG64fJ>`4s3%0(_98F#*FnqY4&cTyXLl<jB*TkZ*&RRxB2WuEj%cu*x0M}##aT=a^s#YS5~XV1??qqVQO{e|c+yYDh%MEw$JT#RMi^P`nuxF80BZW<;hN*l3m=GZar6Ca_aH@0tyivv@`$SOhudlAA2w{ABiy8LBZS?cD}nq-9{dEA!=?k{DLJ|=h&L)7JzR+~$ZrzgG&2onQUD+0u}+M{HJaJ3tgxq)M`sa7zi9Q5T{ZX6+W%0)9Pivy)E97r=g@1h}vp$$@ZNWHE6p;nxTSgi>*ziZiCHeM1|Fun7>LbNk?lc+(Z5FmmqRJ6;5?GsN1?rDy7DrbFS0V$XUmvc+-QG+xRE25ISwt@zuh`NTezCnl35ZcMh3m+G`DYMEi4I(4`iQys`Ru$*K4%<ibu|gMb5Qt7YqYCKAAXQAok^lae3U*uMAg>5^8<s4}S}2v9%Uy%;V+(e3R5=pCF5Oq>ErYN{6jI70=nRB5lmAf~TtKfy-(3P{`1%Po(=LlD+B@1c3_D`dN%G7uIGUt(tORfr{!Ub}^~Uj1f6bwmYq)*b-cco(=j|i7ITU7TmHP-;o{O!d?jxK;<y$dn<~~B0UDsI2u(<@woCCAJ1=?r-pUu`Ci@0xJfRvdUXdS0&^OS~a#mh`nwenLYEUfh?y`;w`#$rfj8p$KXWz<81w}n=dl>kkRWooQlP(gBqf(6s<CgGLx0hH_u;Gc-DDv+y)n})KPG@Q03wF)rm1fn@Gt_juh-7i2inFPP`SmBQ(V=|$ambg)}v0Y5qFhwhpwBO<j4prja+Ho|ol&`OLy<|-}W|5UrGB@QkZDoeq!w)kuSG{k&06XPEVDi?E+?jYqTF%^P_2NXbN`fD?QH0_*-ktl0A3m4&Yz%#gx!mZzub9h=iM%r#bS5cJPUrnpEs92d*GH?>R{>$_{FiLu$r;^KAG5q*i`e?gjNU@mg4~yON-*)t#f+vjf~T!AkI=+<Mk~f#PU@y2=KyHiU<n?KbnR2PoZV3BQ9-J)2c+e#+Z?EHJu%sP$(uIt_napCo;yTH3$z)he7rX0o9j~^*@fq%4qhub=6m-|&G*0fmGxzw=94!s=93dSF9DdEfi_+^TnPzP_Tz$5Zu5O2a4jh10kIGui=vb_3#nsLMH6M~tVAW@yUyrZZH>iPbTIc^L&YZR&deEQmT9~71rzswq!0oq20<Nwr9%Cyi*h4RY$x_3ZhtwHi&$R5`))xjFVD3EtaMKh^#FkTGuQR&YNhEB3mOu-6CY$>i%q(iH6Q4Ys5khY<-4dffTY2W=X<EIO7z8X2L`SY<%<p_1{u|lR4Y~EN7W=QCAyv<mP<nug2%4gLFYDmAyN^Jfoj0|RIBPq(qmGvc~%XZ(_n5pCLZ)&R-uPLX*&CAn()1BQ9GTLd|@J!GWqGMaO1^ghp-erl<K75QiAcSw95qUOzsWGY#2gDig8FHLR-Aa1@JT)tBWxQq;|o-^KxhIesbpClu1dEI!Um~oO^^u_sC1pWZ!hupu<E*)=CsFT7c!H-)VxmYg2y>_g;|YHXU`j@ZuK55t0N^n?#x#A;0`*&fjRMv3Qot`E>N#E+5S}q9^MRQ!j}z0^4k$Iem=O|LYF1XD@!FJajeB4js-vB<WYDc;J^J-63>4<j2hcZHcnHcOBJD0a}8bM`zFA`gi&@(kta(c&X~qPbfqGh=S{#Q~(u6a^m7<d~k0mSd{N&#o|KM|MNTWjB^$COGg&s8)+=Y^Z@;$Oxtz}84;#+!mN7ZWAo@fBa=MdV`g9hxpNzqWy@FJ;W|5onnbSPiZOd44CTQR8Gm4+?%l&LzxeB7<?e5IZ+5;N5ek&^>U%D_D$bKF9*$UyA^b_Lrk-CK`|iCE7Y;0?F+6T4M+sR&6re{I`3_v016!GGMR?tlms7rzx!NBwKQhIt+Ix)pSY<lGQ64gA3MT3~?O9CVyM#F~<$tpV*f7GNR75Xk!rjuW#$M_F-p8XcFM3C1!5FM}bV1X*+B+H+LV7iq-giNA1=kbla!ay;(fF$z=Bamt%_C3sR@N)6aYRK$RHGUNEvl4rFSO-vB8*NuqJfUAK3gS`qrZ|upD{;mzZ~j*sco3IzhBZ)7*)=@X20kfwUGbxD#Ef-b2}x^1O>J=9y?2(+w1yy-?Vt%|M_+GHEV<5IZE@F?rVOflx8aJX@)K-&CZirO5Rdady1FD=1R05jdED^fTjik-AAr-n>lso>DfR54G>)<CD>7$+IK(=R{c&$ck;ez*?%LJ%4TR;-P$@sueLTbg3?<lj=Esxxpk^GXH(UOJz-7_Z;r;zNy9hO)cg~#R(pJgrLsR)do)Z$S6>$WCcclQB0vPI^XHg|w3K=@NN0YMrBcyBiK(oyRL;>s6%$bb5vKNtXN;e6drdM{Xo#}K4lJg&zI;%sfQXwH0wQh=4UzuZa@%j8+4k?StaRnUXRh5VzM&Xhy#g6b46hC;)y(Lk<K->Mc#_S0&$O!SHDmNgE-_GdX8F3jvrA0Ips7MNonZWQ*(#13Ft~T+O3EHe=>7!ewT=*ydO@b!pX=!bYG{@VI3&D%WPDaKB`Cc>ov(au`B(*5R`DnY8!=D9u|dUSfYzJeGN0&sbftH#`z21OUh-hIHJGi};2&bRLkEZA*3jd0hHh`Mn;gsdb`p*b!VB&N*;OwXi=;2hWmy_ZAhO9OLBbZ6YzaMUFL-C4EUS#{{8$L%1LFN#Qzwf=C}LCo1Ldw8lW%{_j!njXksF|lN7|0Gm35v@=`NMqgU&e~OmjU>_wMA46`mBc++hj5?Zd8I^uaxPkcxhYwmak?Pi)BfTNoftZCL|*>R*f}UmsJZCQ1m`!!yA{oG8pM9)z5YCy5`G56HlU-n;mD8Su~IXC+;_r=Agc<gi8A`91Hfj(<{mJ`9Edc#~{6u?>A~(4Y}Z_)}Zxu6a#t*Lt!H*Px)@V5GUWN`kAdPUp}d`;_bqe;St&UW@grORkbR*ce%Eq1;T=)`muAWp&6Lv^9&!X$uV!F|LjWi#`chs;gFsU$#o-IFGw%iC;JDwDX$<>yyaSqG~q~mz|=8dZ>J)vu+6jKB-+j74TIBhil!EYmN8#ZBVlL*)zYGe9bQ=zt1m508EgF=@-*}s9(&x5mz&B5-Gc>xv-4+5!1di%a|WuSjMD<Wz6T*GUi7S4K1mK>MNUNOlQg$tzWsur0N=zzO-vhtgbP@5hRlk#SKmGn6&hcN&XbyZy$rrDvDgNvX9AU_Aw5F|88=Sfle@cEXit^Kn*NRWGa1u1b^Ir_=tBjkx1gcP|*daEc=*i-ZAJVRO6U#VH_hD2pY%0H3my+>)u>*jfr2GYmAXn-ytWsY8*ot=tuUB>0eIb!B7w_Kq?QV9V?qh3kv-L5=-1v$H86Yp~g69EsM79O!ydy(Tjz{)sXBQr4v!gH!T-<=miGlD!M<6gMu=mz@331fmz<wdS0le(pAMFRJsh;Y3xG{r-VwY9=gH&Yd4ccq|;)bmX@+QMy9D7#%vHA^fhM|NF0O2LUmYin9Sr_q&30oxIx4vVWm|T#@CB_BKblitVm34_V=8;o3(4Ib?WSMlRlafy<z@F!5QL5pFcYwbN07>`fGjhL;w;HMd#+sVVF&R{mKs=MO~b}l%`N630VYHkKoN|x&Fr|W7OW*>LaF6t&|-j^i&V-BnA@t4~uiACi8q)UujHk;tAQ63X&3Jp!uWUc(pj=Q;nc&ypN@&(r&?fuThf(o@c20p!SHT>eEiqOQpRgxFb$Y`SQ9(PD)j!QA<y`zcH02GbL8GI!#`6H`5yV-g=SM$qJa{2o&%j<HMp$mFR7|kZ6SNsL2xnrxdEdieUq*L|>1+v9Vqwky4S3%uE(XS5+Db5$Z(TsX~pzON1K#yj{JG58wZCM1|~)Z*q3&I=@p$NDB-3ezpd?<HkBM!h1hX%smRD3b$o;3|xZ-QKQ-XDPOZ$*fGdFAWJLSN{fnlu|6U-XM{-GDx@w1zvIa`i9`457lyv9#^lK2ID>_yiH-~+_mnqc^{@BXN>6P1Npv~cIh;Oa<vdY>L_VD*0nA<)vx#a2Y0Z(LrLRBjo^;Z-+TLLY96xtI_tG6HbGO;>aoL3$YJ(}SiQJcN>N-ue^?BP-|3P7v{TjQbE|6VN-EP>|O-9g7xohysWr(cD9|Ia*_Z(r}2r@872toZA!axhD3rh8c;Z*XRs}K@lzpCwU>NpcQu6)S(r^YMP-KmYXkb5YwGt!a@YGW@Blt2}c($@H7GdPGhZEGayowf@(zv4`;whPa~fnKk04INsY5;OLBi_mwG(p)8T+L_cBB>OHF7tEVdsJe*tXo4Wv%cg%SyoYnA>&74>E-bd$`Hj<yLtJckb)#?s!q<OQQ*l1|>XEKyURoRhA*BrHgp!v*LJf1~fu%rkQ2n-^Tbj;o@t|34Q}(AcJwy9268`G=MEU#F7cW2B4yfn3dJ9PE1=J_k;9oCmW_j5E^vMOYp>FS3c9I{szN7QO$r2gmI|%vSVEXULK8636ij-wz$$~Ff>$}AN<LLTHpjLbZQ5%xG6SAzVha<XbcTF&uvsORS@ymU-^Cq;sP1RNsz!-!Eu-uJU422O2Rcg2#{4=^rmYXsiu<T?i36=}m1^Fytb$+{%mkp`hJGcMb3oa{1-nVajcaK;arMdssy>QJctJQbVgD9!C;cB@b9MfWL;&Q{CoTd^)_A4Qi+?T{IY!?bs?U)#xJgYpF&2pQZ@nm&l*N7`fXt#F;C?)-*YfP%GVSyvJvSnj;JI-;hNh#W`j^hNcF0}3nbT~H>HnXskwgkk!^84Be*slgponllxNyJuSBS3ol5@QtZ*h@g)*BE<JYm_^4gGeS-u|!;`Nl%>Qd^cC^>c=(7H0=~yYC&vu_i~qJnXE3I(~6c>rzd8-m@z*thxo6IN5HV~%kl_DPK1d^5GDU!y@nJ}Nn0hGc7&wPtp9sUUk1H6YN69xuoLz4TihBKSb8cLComUiB};&1EIXa-7aRHxm3X9uQx27+BRe_N2JK{6PB^nFxWY<Pri^2ssW3?7a)_oXh^5RFFBP&@4T2!QP`-Vrbc3*<8ziF!1o?_8{g6_jy%Han*bFv2dZR`!C*6d4Au1i+v*;H4lzITVOQ;ROd6An?O*ceUK#ZCu+edB<@z+=4w_no#D?GuH?P~Dp{4RV@J1AMWk?HeSiLxxUj&6vS7*`)b@nf-m_GgJg#;BaNgCdK#qoeN=TPGyS$}IBC0xYIFqLcrZc+C+_g{75XwE#Qw5j@T2U+7=6VwUgRt)h@W^HnBtyC+ok1y-FDv9DxtRePBETf5LK3T6tnQju$`HItfid6l*?onu>0rng;~bG9-8b2D2y`ebf@fRB(tx)lP8`F2a*Uq28GtF2Gsu_EE*AdrOsq3r??8im+r{W9{(BxP&SZN&Lvw$^KvKFl64H`kn(j^$kb?5nTR=^R`9{;Sk#9rn$axk_x6X1_|YB^X+6n;c$tp|(M?ak@%nDKy&yb=TtZDhb?-jtQy%mQ%-7POXIc+Jy>{+XtHtBbtA@h03+<5)is=y-?lStmk0u^mD(Sa;?(;_%Yx^-CD{7&5vkGdY6QpG#QrBlXF-rfnK9=`dR(++z6o~eWA%u86l`Vi)))ns@gg;I-ellsam~nD+Zf598b4KI)+qFP9v!k{(a<MGf@{3w)K-94yT4Gi>=f`V;(po=sG4{mA-nYjS5<V8V5vN5>l0FMm4IW2*CoN9A$QxyRf8j0+<HzKI|{sMK`HuH;Ls$?Boky1f$=G&zT8rOf>UVHGrx}&j0c&oQh?|SXL@}I*oKAYN^5tB>rtVwm<gafclM>4$$FF06sQ_n7|)ScDMJi_v3Kh1h&wDGb}IL92HTc^-ZBGDr%UEqAx4wiS8%>oI2SrBGIm%!*Weo)-OX?mNO4Q!V!bL9uv7GqH>^<RZo}z&h{45w#9(?_-ii($mWWU{jO_91S$>g4Zs>pPC9N~Lu_bAENQvYU7}7sd7$`}eW`W}9fOhzbiqKb6Lb~SQL~=Ii@PXjEdP`>t{(R}UypxefVC}L6*3XGSO)niIQd-P>xsSMg%V9-Y<zdX006)moI!P2(rl%|J_bI68?xg<*Huk_elJG!TsS(|n)=30lB*&N3V}1w2z25`>Vi}4FL(H$jv|d6xt*OS^6#&Ictk(4qPdLd52_H>h~9|8X0^16=np1YfF+SS_>z?Arx2c-cTgLd1p~dk)eW0qak8y)oQY^DoSXXR4avc_BN@n$&^OpXZAj{*gE|-09WRk_|6$clg=H+ieV{XvFf(l3Vil9+VN?Mrh?9U^ks{dG#-c6z3{|Y??hS=LWdN*aTYbstwUZnfZ){;jq`YQ>hEBM*LP%3#oSuTw3TxtmvMja(PJs<VDk{2Yoe0Y$8h!!G9@+0~{->9w{I?6;yK;;U4}j{BdSA0n{0Gj9G6DCNW_GSt2B%D)7=0*Jbd~{*n9G3YMW!EHOHR2inOp$JFA3<tQ4Cg3r>Z1UX1KK0G*;Wrv1Y_A$3CGIZ%&?rBqEZN`I=JWWDZWji2usv)1>HT^+DnK*nADLX$bAQPDjyfnK%S76qJL-sjswZR7E)oB`b_}yj)iFoDMtvtksMt1q;=@H3h<y$aAiG6JhMgjSMEu$G=V*d#0S{l<;=dD^soP`sw;m(}O3O#mm}*8?|+{%9Z*je&Yl5R=X45eY#>jiU2qp6%>O(9~z@Q&}30nkW6!tD1d)L@r<&WkVk1y8-SQ?4$jic@?=AmO)j1&tDxLYFK<@72MFviGsc1x<UR^6Hx&j_jn9;J(q0d**;2e*ZEsfb@%F73bp=&9U~Lyr)<ki2z-*(CW4LGTHpsxF%YTp$Kv`wFpq(PZd!3LoPSU+(P=o@~hLtQlM7s@;I%`xk+@E3KCZ+WeM;;i#Y;6uAfb_rhQ4#el_^*t?rg)gbW>>9&&r!?7M_4=@iP@#@wv2LC#$b`Wvhad<xLmhrBpSjJ7xC~M3<Fo?*|BK}urd^KBi9=|U-ry?iiE4erwB~(nMgP(H-cz{XQQT%oSTS*7yT?AtYxg*G^P=i7Cc9Zd$)vX#bEt}62~5bksNUw_g8$v=8*VX<`d@Mo}sJ8HM;7%-hCI1)frv&(`)D|t|5LC{D$bN{K4p|gKsxd&`D{6RuRkb6Yu_MFYiSIRsF&eR25f<DhUpjrRtXu2P<4t6_s!*QV!)jKVhl*ilu5Rmdbw>SgL`={9J)l!xBgpX;<++AXP`IrWc)sK&o^VNVPywb%IbeGk&UUg6~){XrIPUwG}_r0M%5&lBe-g-VJevP~`=L>PL*cCkWLq5<>O%8icC*Pzcp{4xzGo_q%u%KlRbUQ-AY)4rhxkn}#+koPk$bxyBjv=al$aADtlSUGp+!bn`!P@?W>I?^3-10z|;@YeCn-XO0yOp0^TKii)JV>Z!2uJRuR}AdlQiOyO~8u{z8($j+PEOsH5>I`o9TH}jMB|7Y)AVr1#o?4bRM9TAz4Sy@?GkNdxFKX2cDU#_qxeMSg*3<D!Ez)Wb=7L6xh3(;;N+w!Op*tDB&xe>xxvOEL^2=Ne-Ww3yOK}H~uFg7h<U@-$Bkc`-Ct#8L8A5~fB|IaynyX)7vb+fV}BO`Wvd++bDzO|UC^i^P-O(&H3VjdqxcjJxDs-7fRN4ojwVu}@6M7isxF^b;Kv}HVn$7@ofyx)w?1xtLa!lY=8Cbt}!cBTFjZ@8Bg8<;<q3QBxEQ}Ahj$q{_}L@27ejNOiRlRng0)b>p;#!;j>4YHkPcx{rVt`y$JN{cu583yD^BdPY=ICB!(89F;iyeTTdIf!;2%PyTku*Rqb{WvFPO>_K+S&%{Z1b=l+=g^tBgP*utV5rr*9Jn;Iq2oo&(SP86eToX3N7rh%`T}156cRSB`L4@fAz)_nK4_@!p>vJ6X}AOR5qd!ey7;4}fQqNJP9jzC#O(m{dB8C5lT}@aMM{!L7VkV}g$qyRQ4E;d-dibC1!W;HRe?)Rk}HbTQe&dy7!2_6t~kxsaK1VsvCv_Tk1#wS%Y6B@<0h>1N3L;pIcag49(Oc^qz%G+NydRAB7xs-yo4_4#+|maig!`u$c;>yR8^2#ai4W=#3)8p2BYO!;V`PMZ48C#9PnxE&SCk}JBwA7i)g3vB4Ma)NVConp$5gssnse<F_eJ^68al@mxNrbGE1%ByB_8gjv%*S(T1Qo2=sgWwOAe+qm!+Qrg=3(6Ig=b7PlwOC=L|dnXz*<SpO=LtYzwcUulC8RI56@;gpoeQ=7jUkEv<W24f#Kh%R$X<UR0}a$RkR<ejTT5Xo@0b$~08y1q9>`el~t2=<dRQym&kgRLe=OJEQRg(_N8Y4_t)=dD#*!&6PLwjhrtRuq5+N(qb@{0xQFjG&qd%k2a>O*1@IoNmODStIsoq|qNyIyIf3OivKbL9l3lL}4$yYK#liQ>C^ia%AMAKl<SGj@b5zKFO7`KacPv;IiT_R;+|TM=pNLptVZBux7=!%b)V`c0^uP0&6kNdeMlE2;xvtZDVf6&wd7jx`;(E)TZ@u+{RvLy-0IZRsBa;R|Qjr30@WEu-}ooFc916<M+y4{LODt?PgxJcNYY2tQzUJCu%n-E-P6t3EqSmkx@9&yh%oW&5XfP_J()|tkOA6K3!L3Z{jF>Q?7ccd=mlPjZEss*gU6vqn<QQb<~Nee<OsIH~pGuBwK#s9kRTB6~BQ;2?f)Z^(ls4NGvw!E{(~QZ`QHK<ED9YR=S&U_o89=6UF2I^C#)hGZx&}H0i-}XfAtv-MJ?BS(9F4TfA4ss5zT4nwg%tf&L_8)Oj({jIDY(8hmpspB^QRv<p+$;n}3oswRz;F*>Q8&V9x<SwC)*jxt81pr98LD>>GYM>$#O%Ne6joi6${_gDPzlMY!Q5B8+)$qnB#H9)*BKX0nIlI_l{!jQsxzgH`-Pf}2DV%4Lt!5)SzdXwhf*hr#TI@=YQoZgc;P7xU$SnC=<NO;SXb#jeSTjGiR2&kILqsuO$P-UWV0lg8AGQUlH1$Tz;QUncJZ#-U1O=@^gD`+{0xw)MDOE9|7xzdq_Th;^xW+&WOF)3MAN&P5z{Zu~kAeT&QcTD?aE_vlYP4(av?>#?&{DzGlytaL1HuvO*sd7&7AHJT}2bJERf!%{i;ZUBNH_4<Osy>lfr<+@a3JA|ud#t_pV)MZh3A;yiL*dPx+K%=?7|nA0J({B3eR=a<;}mwF5F*L_9rJEwJ;(RD&&xY7o-pj0j7tOn-?{k3HTlW)N6b%l7xI(;pm#sJ%uoKoWqvZB%TK;r<|n6i&%{PgAe1lWC-XO!pX5~h=JJ#CM$bIUPkx{I$<3IboV9qSWs0)lRcyRvDcQZHlBH!S$+n0rWv479Vuu$RJ=3#U%5*kMnZC&sW&GWfqWo9fFU169mzcf{{|PJb=aC&K4DuhmDG>g!7Vz|A0o()Wj=Nkj-f!`$NunTJIpe1^P_VJYs)Ge(#z~xv@i!5@f_wmW(FYjmww(PQGhkn-Xfn@`#fd2|*$Z{f%J4x#1vq{ymMu5_6-;2!x-bay;WzfuQF*{ecC}WREn&zP_q<Jd78XnDO<t|Gk~}WO9wK)g!wn(^`Kj{jp}5+(5x{?#-ayXqVEah4w4~4Xbee#dBYepQ94IJD9`50@Jn4GalUk*<{Vjdw>!?<JMXVOL&y$xuodrdbWArTNs;>anmLE(U;V~)^w}F6DIbIe^*cz&Y@ckp1?Kopu&^W;7Z%n1in|8b+co6^*o!tngK#Ye(xHF{=73?M{bk|VNBP(UP6^wwb^4Rz(iXk=X*gWJy%|;46AW~sNQ(}*@pf<HN+;m2K>5av3LC2~t%1o@CZ;d6BF);z-!E#uW0;tk1{4T`JU2QF{{W_h7%NY^+jEmLsEPQr$aO<V{MAtKegckR^vnyZMyx}=UR=S=&RnXE&WE4yzEPrG+h`;d-i_bRaDl1)$!cQwJmt;Y1tO+n1g2Vc67yL@x>Vyom_RXWn8_3|;TG(wHD4-^u)f7L62v0G0=T(l5-EqJjNDfDM=_pNfA~j1?6w4<y;7+rETli43FQ?;ik!dD4D@O18CDq8;pe9}}gRed<$;iKaW<z{pgUPrj-q$_xN7YZ7zA8`tTU_Bm_7c-0b|O*o*JWQ@-n27@JJI&LA9LnF<tj@E{n>kif@X^vNMHrLs^3q0kUmJ7%uvfGHJE1T%pM%=gMplYqf(vHJ@)`)Rs{uoR#~Zl{VQ-k_4RB~*RL(I_x8TDNK3%b(==|JhZypM?Q8ZyZ^WE(qVM_D>7iz!0h`4r_4BX8u7mrnVUeyDx4+}_zyC4!m)vjq=6e=jL*HxVEbH2_S*Z4B(u<SyU&=SuVg@YH#-qTwH~f?ON=*isO@OL;#(nYY>04;MCi59!_N|Y4qTYf@W(NGIaV{3WOgg>6BpwiWh>L&%n$iz8j7-$Oa_u)Y8|!V*%W5zPI~fUAaOC~v$IDSq?0UnrzQt;t=-&#20`w?de-$sN(g8SM+Lf?V007^!DWku^5}}FNNR1G2lowa;Hi9#Xy7w*`7BeU%y%mtJQLDcoReq&xOvlNAZh@#)-n1cynb3ZN)nwH}CBdU!7deuY|Cy^I*m6A^tgNt^Th!aYiAn)IPBb9Y2l5N2J=V5CVlnqH*Nz$KYG#ox8D~L+O%8O`l~FAo;~ih`P3}a#qAw<OW4<CY-aNw%?ijDX<%$PwGsVo9#{_;*b2*IP&b-dUEg1_f36D!E2K}Xac$Me^KSt;eNL)51IgHMSbZ^TlA7EMF(Ezr`lrb7b-1t3IzB{Xu`#~VxU{M+lyHWcaGo<sS@xT56TJJwt*>6$a1;UtLPJpwXdN~2k%p?JF7ZTvfplGuM_)Pj;JF!?2&F8cPxb+~L`uidQ-bO3q<dO7?7F{m#AdFoECOngB`O_!BfBD+U{{XaO+>_I-Sj?^KTejWY0g7?|FsY<Pu~{4{1YU1u2zqYUadlhVTWms+?sgy0wzE&+A&*-f6S;l39Tb$t+=PAS_6>7<oKY=hP7Yfvp+gIG_PlWiST_b08|}e%$DV05owhvo?MjT&vFk&#F;1`Ysg{Y$)eYbbXz?PSHy4P=JR`T{jZ>|TRh8vH{?fIhSQf6&MtX0K+`VmvtyZuD`~*qfhq{gpL=EpaV9kLbA}$^4nxl#b6c8SG>zjjBpX(X0Ha4W_-jUM#)>)QCqq4oHKN#_+h5`H9(!5;QrK|D4lx6w&!8Kzim1u6Ewre|5(!*Z^sK6Xm6wQjkJ@2AFUGe_$1$|_K5I~nzU{6Eh;I-xb*d5YCf<rgpfssD)Ddao%Rl~l@JCcQvvTxXn5d{NN9?4URH#?`?RBGb>4&#J;K!OA;_GcGAW5F}6u~$SQOwfJS#LxFZ`f0)^WHp&{0c_Q%rz}f~-@dbE+p#a*{>AuZS<M~|sjyA)0aDB<A7ZB*t4ABc-946q?(cm<jhBz2S46R*nZOI645L_4<HEDjE-#7|ZC)={lxAW@>5^DcxU5v<s!~yfGruTSB&H{zHC9!>rEDO{@Nj+eYULKSGgh%8+fUM`+E4!ON5$V)A(t}(aWgF!E2w5ubQ!4VQtZbHsxwiSzNst}qd=Tgv_=R%rCmg-y&~XB<H|5oJVI6Hol>G*RYoSVj-qgWl6SY1S>v<#IchWNHz^I5!n)jMD=96e$)j48jaFE!^q~EPDy3J16i6XM*i5X_At(WoEhnloqn*jZ<kr#;H`k>fKCLd?H`3!iGKIr7FZ8&V1;3xIp+RjiV}rX_eG*-!w^p<y1=&*Gt$_v#a%5u~iv_xl1n$CuwREAg+DSzU!By3dIjpT%cT`nEY(u`X$zeumBu``n$Z4!Bb>+E&H?C3=h}w#4Twbnm6fccU*~CdnP{v^+TKS!^z-%jZTyHQ=kW|mDASis8^|;4>^bEgrbrALmb!CJXPnb22k20X*9fWj<TGfk3_(ek3Fs9QJM|6)Mwr2}inIu29;~5B3_!(7^4SWoK@gP4P&VousR53o#$0y3L*br*T4SVHW+_`l7MJRp>q+7~GKGGR3&*Bb7-#z(_F=!X(B@&4d;}ZhQhUDx3Ka_#{&pzHNs?fVX(v-gpOPQ~t>SBt9#~r(v#6RA3uKG;NE+%&M$5~f@h*LgIu#}qa1}+Xj_nE|evsgu8lp9qM8nu`nFQHz_T8t{^OK5P<ipvK!&>58?>a<uzo4SP3`%T7##uYKysUWs%EYXg=jGQpuMC0VrgEz7TroE+~8kj~38v|RGOTD{-EIOZSXG$Vfo!TNX=oo~*V+Pg3Df>_c)e)C5V~UuzWgm}iO51WKpndfr4a&CVnN4-%?73)Dbz26o)Xz9v7Ta=jM(uk7Qa@)|b#uPg_FimzRn1DpY)O5K!aNEaNmE+x$*E(@E_dTqFpdaMiKb!*qbY5!Hl<IzC;zEeNsu)nS=dLuQ;|uOAZyo-I1^X?D#yF$KuW?bGwvX<0y;?hEz};GY$8ILWDQME@i7XBwy~J_NV4FXm6XROMuvtA3oQiXK(f#_<V0w_mVI>hki4LE2?QJjc(R!uPp)i}Lu4VTp5G&LE5ZdHyux-(9*o!r5*3hGp&4KnEuIt^Wbh|eV#@`zB_{VI#7Cux?L`z*N>rsNpT*6h4;Lb4<<}NF)XxOUp#AsmY9i{ghv$1jugm`V1=7~t34dOuLtX}|qZ$s3dJsotqDxenq}BOt;GHs<B*BO*r6;TY#x&76lj<6DXJj|<1OK!#W@w`8Q>7dp$uNCt+scGj{{=I5Hh<`~_wxpK;|@)gDo@x)A!IArwxky)Dm#j(=Xsa>?83sx##i68Mu$+ZYId`=t6mjlOG89k%L3EU^%}s)UvFwebnCD@>R?zE96nL5-<4eL#W#{n&Gxny+CyVpvErY$uqc_Ph=K*RgM|4Bt+R(gO>~tHpn~e{2CZda{OW-^ukZqY`TDh>8|4W1(jr`}1<g%_7F-9~mE5tmy3!JWH3Hq|n2o;aFr_8@*Xel6M0hFsF&U9C;RoL|CO(LdfMW|&4N*NAfSavE%_RH>h7~XdqxTL|y|qaWfx<R%lJD@@fpZ&w-32W=NEYrq*B4GyOlgYX;a70IlohAUfBWnTgF+o!9N%z-YW}^}8R9px7H4u!_TuRMw_o4y*SGQf(7(Qo@Y@K#jquyAZzKFZzlLw-*YF-6&#(Dw{venAb$|UxF2tLmexP5&@n7>d_eJ?_U|;ju^z5&%`t0wYferp^{TjZZU-Q+!0($E$tD;}$SEXOazxr4Fx_IrcdJP1rPGv8i|LK%$(PvNpno@nyTywViGo1e!M4cG@EYVZnPowy%cYb<3|LlT0b7Jau*2f@-TvNqGP^$prZ4gq|s+0id#ja=bXCkQ{>VhO!v>Hq>x(xNT869Udg-$2YMMHcE%c$NVKYNo+lAt2hzd$GwSt?@{O0%Y*G`&;*k?^GVp`PE44+gB9-toup9R2muuS#<1oEOhlpV9m-q5+H-Ulh7&h+w^+ajg2ff(5C9`FQT1-PHKb;*!*}a_%nbCD}DcZxS+*x#&<e)RsRj?Ks|}H|`0)xCRjOR3ec}$M~ZItP^~G%=pOa?dZzUO<Aw!#m8jy5cO(hdjjd2_S_^?7m)U=944vi3?*Nga5z4vKchDlO~ZWf*Tv7kBke|}clfgsupGbt{HN@vt1Uyvf9>kEg~f~0&xW%ff9Z}=v~_#_rt|LfuFrgLxNyyvFLnOG=SCyAOM|RGEe=k{7w`SKXZQSHyM+zRUyMKPvg^2wqsI<#fBMfa2Y>M?8RWTl{OqcZZStl28XxiU37TB;*$-Yc_1P`kJL&u}XFqk`(&Bs^_$ajzyk=y^H%;(%B<1nvh-v(|{T&q>|M#y2uE?M-Ia>?QXCZ1(y176R8%>vIf~a+odb+HIC!fooN6rswv4SGDB?W-ib`z&yFF2u;p4fV|Hgr+_WCkrVmR-Wx)h<LrWx#-1BZEREs12wDhp`;4hKLl@DxRvB5ye>~uH~rOW2hS3By{s5*21TkuohLG+YoC#8D_KTqIqo<t!a#rC&4ce7vw#LmDU<LD<#6M^_-?Glbh%U@Re|m*3AVXkcp?}cM)hU{TXn9eBV7iL4yIN^b~hbl?&t%#CM=^IiNP1Yah0+EoA^sJQ!6wXj#Z_p|*K}BFa1amLgZA#E9czTa#*u!CL5LI~`jX0@-(^f`a4kiQIt9G;r(5n77#V!aZ_FJs@KqpZ!c^CF$^e=-i-^Cs}On+$#D5Wf&A=ls|P3jyjg67P#W}-_e7|3D{etmh?b{Ngk{yC1}wZXlcb<Z`JdwE95elAB7dhr}pL64<^Z_1yN`n{~vu+kZWZPx(c3k1#6I@X-stG2ueeOQB*9CNv11h5ErZjP6>mz@>zvuiEY&~(E=s|L0Q&IMHxg<Q?&*}UuhYZ*et6VkBddV1fOYG?`4Q-{D#q1egkO{f8LNFg2Hep(#DnbWhFwdVJXxo-Hjj`LRyWM)T1XrO+5ZtRI5J%V{Nf%-58L^#sAw(CISKhYk3CUA4Y`!LJKRlR^LC*EU<#HpCbL|0>{h$M3X-$R8m%a>I9Plp>V6|EaSl5DEQe1#w9>>1633$RX*4%=m#V$H3@ACTLtTq%Y6Q!$|a96F3E4*ft`P?`1@VmEhNXBOdi}?0ietQA`_JBM=dlOQs>p5X8Pq_{YILbuQ7!EM*)YjF}Z#O0TM2z$fB9OXj5gR6kCPqcX9C@WARb_*8CBHu{{OGz-6@`sRYE_S}d^*8_=bw!yEXZTT%s;Dae^bzJSc0+A3Ne{OpC3RaUaxgoX*tyyb?q*m3-F$GP%Pck@5}&IjUCJMUZdRk&L%D_9vTUB(Rizn0mS_j_3``@FrO4ZG$TYDoERDK*z7faMZ7&`HVNf?F-jTLJi>2SXdWv}^^4%RT@E_N^Z`N<Ra!HdR$vIjr3TIMm*13*|Kp0mHax4tS@F6?0f&(1K@`ap(y+q-q*)JK(5JcrG-1LmQGP1v9wKVJ%@n7h(k{VY%eVCr_#gch=r)KKiWlQO*?6tQ123DE^cS|H~(#{@XUM+rdw1p8HdpXMzbYk^aG~%r<8`c!oW;R4kvY(&#3{86|D|IrlS&p9OujIE#i!zu)3ae`=M%*Qme@)1P<!XE5u^fGmm`$x0Dhrj5jpen07Rsd_Z}{Z+gsv{KZC!S*wv3@TYV35x8Gu(2n8ze+qepVaS<e|q#B!cSi(VtPtDJ~pfDE{K?xzvi(s{H%y6Dc|Ngrg0Q8wQe)XW(Gs!lYAT!Ei|{As(WW5rmm}jM>|X+rfQ_alkX?i`b-_u8)sWsq)2LNjXBb5Q9DS%R4a?ysb{-V>Ec0^Ll+9B#yW{vb0lKA;}a$m+d{tde{^L~DmPTv(MG=!*MISFT&}t&VF{<-k(<BKP8XP0@Mku=W8uXW_`~{ePIYlOv%&2c&X<^~k<c7d4$X}3WX0YGJpT-!V{+5J)-F->kSwJ4)kR|lHzm|yY$YNmJ85p?oITma!i+66k-gv{KnkmuKUKZ|d-J)#+SHKxsxB5~(^3-#)`)m(z0uuh2;~oJP*-6uxWrpabn5L&s{@|Vrv%J@Y-%Qw)_yH^rkfLXCSTc^+HZ=T335h4)GKbCs34NU*t673DHwmeH`0}p{x&&7BNs9`Ue56{-ONducz27&NE+P<9r7a0^l8m1{X<&g^3S~#pGJ}1lh%<-Tau#t=A3<T)eP;z#LCm}>h80a$cRAZq3Q-OJ7Wo5UwP&^4D3~0*kD@9&FVjug0P%f5)~Dq$`fYM*(fRCO`t#oaJ70CEd$v{6K9F0jTbD6tE}esB8oB(XY0iG#T7^phE}y8KgQk6QpZYquLzD*QN-TE(z|NuDNSGGEyZGZdo>jLdUD)C<JCH!U0SOVK$<DeL=qN>^Hfz*$3QqrbrQiys=3)j+S|cye4^|3BVCzaC<s)Ii1CH;wjw;U?~(>a)qL<ZHn5CDKH{9O8@dS@h_ofv-VkS6Noo=!4JwbPlxlG!*(DW}Tbw;~)d%a1j3dl$0p>K8{r7kfoVA&yX}_p5_^^m=M5ozN<wXPg@#gV=^M?NaSm^(^QGM&FctcCS{rWb-AOF|4p?CxRzk&YWetiS|zk&XLkUd`ihWr0Sxc_hN=Qo4(cgc^4e<W|F<4+O)-c7kH!E5}DGf_d}4TQtaqDGfoWFpduOBps`(v~xM5+pAfy@VEh>Y_K|?-6x9wgF5%0AhWu@N~h}=RE+<yEAP7X@U5k<L^x>Wd06n(6fUlBBgr35<7nMS9kPloPSpZD|>&^LO{C;(=FgNpH3w5*Z}v-hJ^9E?1RBhKB4^8>cCtbPLqhBO2#}qwOE{>>W|w4rn_L?syk`D&_FHw1a!@IJGoweO@$s^|8a-FvOR#gd-Zap@qlwj+U>iO&VkuGQ$xtSRltuZzUk4}k?!InUK}uvzpI@O`Y!tx`|3EN(v!4qTT{Y}sAtCU_<0wBtN8m7lsp2UpXncPC)oE9D}RcccX9b^?~b7VN4WXpU(@Bk*3V8aF10B5*=3*U69}=n00fWE-b;9)2Vnf`nM<9$I6ds>HqSN^91q3(vh#C*_%nl$&S2l&47)#?$7vhD(L2Xz_%K1|FZCOY@3@oiz4YLYI|oi~%8yU>=u}7d9-lk&)Qu3_Y4bpx_~)<rbhM9}AC88?o9=a$^;iztnGy5n-#M*UEJ_^b8w`%}?tj^ci@tEfSI>$8J`oG>EthYsP8L{%KuioaPzWNHjeMIa$-V|caUa7#nZC&CR_s{JKM=4+MBxBdRuj=i`Eljq$`JV~y5!(Huur1gxy>HcPbh*De!+DQ?h*%b!@&fKhU~hDdpF4Bf*;moq+JV8;05JpnZ!!HS<rmkFz}19C7Y*YKFUWL)d6Rs%d=WhFej*%g81utUi)E9s3DZI@o+&i*-}+G6Xv4{LOS_4IEgL@(b?3mh@(z32F*^cQtvuA6N6&at1q8f>$D^{uTQ@`!S;{4-|$W6^LIcO1yo1N&EXE4IaNo}o;+!Bg@qg3rP^gd7Y?90oMVZB;B^Ff;;t@y$*pb)6O)?TK{^WNPg6kC<rO;uSCyd^0y=mxuuzDv81U#QvStUQ2NdL2D5|@12TjW}fJ-%OJ(M`gG};M<>e7CNvVYDVMCANyM*{485OZdbXn8i_8&8Y{-?@P-$Zagojg)T(CymB@3q;LYpknrpmeUEO77ZX4C3r+Ou$cbHwZfV|C8GcGXBQtK3YQ&qEAOgEaWG{97%tQ~05Z5IiGKSK)$_3h^L-2?jotItCyCVYA%J?{^mc$|8=%M;p;SU**`MOB(LR<pp~xB^swPh`al{{a!dDD*(%J`@;D%>N4^C9GE8%wT5$%-m{Y<3GH=^?tkOtQ#1w1_JKRfk;YzZcWFnHWOV14MPju8G7jhz%>xiF(iqW3xZ-1!|zNYPmYLzU<$kLNm&_~u@ZT%*W1FS0qKyD?T%%H?>`s&}3js4uz!_&x>opx`88y39L>xvi`#78PZHZ+h@0CJ6>$O|hnsekTMY7n3UJUXEYg!*ff#(!93@krtwTs^)t2Yx~+G64+l7Hiop#A+8^MF&6zPG4yHfLB^lVg1k0E0A@Bm)#r(VZUbR<A?8ip_AgFg(yz{9!YUxFy$sSjLXWOr0UeEZ1{z&m4;oD~#Av(Fi0&vcy1<HNaP4BFK;zd1d?;f=Ver_9a10LRW#cA+d+%q!Pfs9M0AXOoehT>M4GeGs`~<pwFvzDLA)lfsZ^GTFFj}$<3$PG(k#b1{91DM}$2()4PXE=_;HnwA?-ICb_iS4R!!Y*tya%}Ih%o$R>APIvxm`Suuab6b@Fx(fU;uT|B+yq_0IkZ%_7ZTU9i7VHWy4yDZ{B3^5+9nEUTl!aj>+I<1BaN{VxD2GfQ=_D^!S`xu!}qL3!HG?UcmK+PYbmA^RLGB4ro0++xZjoMO^PnxL(3uvU>^ITbAp!v_rj6<plT&-Rm1Zx{hrt)v~yVl))1lJ+P;SMd}RQ%U!nue68J~!;?&--~m`Xar~y5QkfY9_yVtEEejNJ!V|C0M>gX966RYT@=b(KSj=sYWrRRfNDleg!3o6S<<@2fGFS%jb~+5pga{(KJ8o@dqW;sbUgsM~eV=(~H$?F&?J|F8F`5#K+Jrf-IYq<UOF00~Bqm9{LbU-(f@$pM<C+4uiauoItT6aiIm4R3UP`8rrIhgbJFzUdn@tF7Dr1#{9|6zBG-%4HVg%VJvv}Yt$Cum&rX)yRKCZF-L91)HDXYVV;%NW;@4_)725{B`Nx!or)R|cI$`GGSVOE>ZIE2NZDHsqpYNFX7t6Hu@eWPiEZMUfk#`(re52UHk?sD3AH&MbTDq8OtqO@}|_~a!xxjID4A)-w&b}R5-+eG?d_s6bf%k3&{_K%V?TgxaJuiF*bo(W>jTQ7d=p1(F71>p&m1_5?t92v=JTb6{*wbb+J$x97FTQsoav<-Y^%2`I}s(^KU4K2JLBJTQL<UX5$EZY1m2(uGuc00U7NeO&Qo9vjTht@>~W3S`EP?9KTNVr-rW6roLtW|bqHnX-A$$-=`&jSkG;`!>Zay>16MJo2{pyNv{l%t#^Q~|$5u~16jVd{9W0b}jkDd5ET4OBSHcg14{jGv7t0Z)c<V+Tbs7Cu0BSvzKX?>Zvwi=zxF_dQXl!HO?=2497DvBHs!V>D(kQ^GB8<*(8AEm!quelV>1iIN=U8=vq_U+nro`+vl#ZVo0I5`X(T)s$x&QC{+KyKmOVr8oe0sAC^DUG#A=^LA8Ckf$3jc)HD5PuH8z!io?g7H&pY`nz*y_l&2TMo+gtc5_>WMb*u1mG`?fAq9H6$8Ih<0{^L3=+=GP^*b+Zy&=<CIAEJCt7-%Nb+{P0L8FDzb!A4Bb#S`|M!X^7x-pGYX@*jt4uZKcHhwjPr<N;w6LuS5%Li`nQC>+3`y0-R=yx1i@C)2IHYxj#3A}-tfrp#0CiTEQ^kv*ef!zUNF8m{MLHKp?R${rMjq^{ik#e2zUm*6t`E1)9<L!mh_8ZsA2GQSoZX;7|RKhddjpwQvUA`!p0ZQ?;&%W+xeMFXxO}}+ht8<{G&rDy9jXa);<ZRw)wZYZhjhh{0kP)V{ud}*qHRN(-y^OMTIpnc6^LH|RjOAQn1*xqP8uZG&S(n8<l{!h^K~Aw23&bspgDnWi)E`YjTtU>!@x@pnxEl`hKAp`Xq=Vv0?<k>zM|Uf=p0iQiKj(hSH$REaO)PI~g2l_|-BO+bjVDRE1^$Pi1-#z7P?L>mR~9wVrlq_}Ncq8K#qs+G<yRFKQifrR1-lIrOMsz6a;Qntf!=LkCguHsJ_~fF4=VX#eUVe}pp6B7Z|azDDWd^RT=coAw4M}`5dc3PjL&|?4C87KZzuuxUOZt7cW-zBW%nH(kd)a{uc(}PRpn}61qXGksNb4t;mppbXp}u=eeQR%<r>JAZ}}g7pLElnrbmhw!PtdDT<Y2gu^BaM+1o5Jz$i6B@?lUfnmH%G=v8W{%e9n|ha^BJioR3{Goly}5Fx2xOhH1c>{>f_sPgi`DY|Z%@|Vzt)Ci@goT)1kRYYyDv)$xp+n6phVVspE`q-iMue#ra?X1<qRCcEu$RlK}w+9NCko@8Pi3!al!B?zbE2dlHj;jDue*1%ob=*)}Y1jpJQwGhJ6&%d4Z7GPI+z)pFCZ={7X`dm@iox4<@LLDk4&+?Dds5MAB~f#7Q6Q!W4HxaQnBS+eiN(M)(1xWtaX9gXZ+S3`xufU@*3y90D&ifqx#CT0YLTt6ea^`VRD)$C>_Zy4!=y*f5`<h0$t{^chYZ<iMkIYNQmD0X|AW|551OCyseQO^EntkOu&h(N>bMXvv$?TcT3rjo_u^(NLLVs8gcem>5vX6C`7q9}2$iD*yF*?s3gjh`ZcWd1p|iF$&{S|;fYE*6rGZ=*WW2ai0CN3l7l_|}wE*NLPp-VPJ<h$wQ3KLnu+3&J14$RRY$B~$<*2G&T$Zh$<#sb^-?-w;#2|}T7pC-^lpu34R_Ie%(w;WBjy0d#xtXdNDmFm6G^U#li*9MfVWtO3VbH$yECM1BUD2~!n<}I;q8srI2DZsYXIWjo&w2s0p#`EXBfD1k!m{kTjKkWS&tI&mX6Dx544cyRYoiMZ*`N4!fAb@^LvNew()HIo*q4&_#~slmlWFM!81<27Uo@X{441p3JxXiEQ`YmB^d}pnvA%RiN&5_t!OB~#w$hp+@u%|S$LxKoOG)jNPV-J_`0+T^QJeJrafxPHLGG_xK{lUu1^Jb!0{i5K@6e7ctVLZn2MM+pr#<aaf(|O4Vs~Q!XB+$ztFCzSM)`TFwj*-p!S_tMv4i(XkVYuMi%kVadH{Wbe{i<3!)HM)mDOABS=73wOYac?@9nhM$#?Ql@I3jePz4sx<6qf3!UGFF-h@qyk)$krEdoM<ReN`&?SRAdX#5K0D}?Uod1Np69tGKB&kUfmyygu}KuWoh`A58S!^zqpPoHZKEnffPwaJP{m+y!)xpn;)@G_{P=;DJD-=;31J0QtGh#|=#S#;mu3&n`(F|hr-Ec>}KlSHV=5;}?h!-cMCj%h=ZL@ZO$_JXol-D%szdDaS&?!`-pFWMcjnn7l_*!Dq6v&su_*S)tMZ5F*z>&`Ludv#CKD<vsPe!@4dc996(6N~@DQ1c_TNdB3bnx9ZAeH}K>QEt<4mxhLGBe@=m&#ZVgeNh}yx4#J>9(m+*Ql5cwwE>y%@SqDXhuzVsBmxD8t&3HZPbqR@LL&m1q72vifCsxKv;}ueR;%_NTD*w>7V?<-2Hos#eTZblip57M*S{*k_YIR`Pq^>q#>qDp&T}of!N2#SoZ%4C(5AeOyNBYnVpr}q$gh_x>@l6<&>`@Tlq3z_{-Nuh9rD2mQcM0ovYeK!3qtl-v&bMrMZg=n=ScWb?ynWrD^L<|_NmA!P6_Zor>e8m1Y7dSWquICmqFWz_zal|EVm+$o~7^=306{VY)bND^VIP!v_r1!UrC{W3-%LnQJEp-B-E)-^%!UJ(Gn~q<CnLleLudS=CZTYYgBD1)Jt{L9b_%H3nqe0@RPZ_Q2|Ho`L7%hA&i=(BI%5rh`x$4x_a><7y!*dWh~GLbmIlo8`NjVlP`Z(&!6&|Z0VnlA1|ZPcpAwhBY?<QhAx`jg14X1?8M#)v+t_B0H;4u-;A;S;$=FH7p2NI18y&pZ$$ARCBLpEVqKjuJK5OpFZeg*?r(%%RH=-tP+{iWU@foI7M-hXjjUTB1oSMzRrA#2@kRhtYa7_zQ#27@P7LH6y;>K{^z?98Gcp>7i5XJ*zLOgItP~t3+6`zYChMbsn*(nW3F<JS(z^xWL#5FW?L#u&40%z^&x~Ct!Hh(F7oieD8X<-Sog*=S@DruIsZ@KnV8$3xs!N`YJg2Zw!wIjA9B51^&u+Y_E_ypy9*G<*p)#V3+7Vpn!L){_(45K%bM!@s5hv;o^{X)7zU0I(2$d;I1j(C{hw~$PZ-1`162nh(lX~Qqa4(i)P9sO;=IB}UaN6=6A+WUTGO>z_p@;y88h8#YFX*q4(A(CEKr%P2m`DV*qU)v<X?gpOz!=edk*Emqe8d`uN!;OS^mM8kI+4DIVDw5%+gz9sS!9vLMu?U&dyz#WmP4DJ7-&36y2yWr>T^rx+)P_b%no^?P$9ib%2jU}{+L>}BDEl$ZMn3!s69uZ2$ebDhJpX<xvMqKDES;h6hU620K}DCH406{#-c==aW-Q%lg57ysK=YgmZfsmU;h}j7u6rXe(eSI*+uQepRK)s%hh(JMeT*8g`0`Q*tHpzlQ6HnAaoBSi?XtV9jlO5f$30w3AOwZjW9X*jWMO|B{SYYAs7SS!pjmbqGt$`YSks3tGYy0T~@W^!qyvAUBWUl_y6{_HT4rve6G}Z$B6h9{F(_7-ytiu;>5^Cb>|qP_`C+pXG>J65DqZJ?D|MCaDo%4;jC%kHKRCx5GvsA8{*}8*h+^*A*7J1><ty^GrgpAbROZ@^n{foaADtIe=NpPLcq0-*Ew~+tfFqS`&?U~*GU9-ve$At%I$C0UZbQ;p%#&t;i>l-p1R#yTwG7AxB>q2Jrjr9==)9#ZKzHs=6pH?v#zf^`TD0Av7GWD`r%I9Y|PsJeRmym7-nh3`6NM%Uc^jFvdEHZ=B<?R%VFZE?&HM_Oj$$KL}_i0m4Yj|5#JW343_i-#HO1}s=BM&rUGVR`LnwAQfMswMmAN$TN$UW{FE}g*2$caVt2dhdhoOcjEgK5AaO?&eEHtaDPDu&hnWzF%B)owp|YjZ1O~Bo)xuF=53G3;@;llI6B2ApCMwO9_alO#dK{u4=KHNtg-!I~G^oC&jI+qM8dPJ+HeJ>TcowD$WhGAiGapK-;Q5q{l|4;EGzU7f&S_8Qj5jeqIsBB>$Mh!tmK$k7fA(sy@TKi(ZuoA3xz+3=`IxmyH9q_0CY8)1N6Di>^{Fg`y`M<&;3aILWniP}f+!`KCzpK=i<9&`PEIaTqB<MUvu2}JCoGH^jef*@BHfFUekWZ3Vh#Hl-E|3RyI!Re%uw2R7^)lqcE+xJ1OD1f=B)ZZcd;@;Ta@)YcQLiGmMNH4D4lxNiDdqrC`A*yfhb^r1-6+%35F<|VvXdOdQ^JqVBNZO+@qNx{i*T{;6KO)v)N!Q9yG8+-r7w*hUxu_?zfPWZD@Be{#yXzGr0L_bQ_j^cGw`OyOW;ok^f+gEv*x>DgoI_Cf*K6HXvz82tZp|#mjK^L%3C*mzlp3fPGQHPUY!z4D<})&#qdygUJnDxaR`_a5Jfs1)l$2ogx}tAmAYQ0<YJj_r?+o#o+Fk<4Q>Q?^w~49-UBeLO&qd6*uQ24rXZ{Z;}BRkE+ok2!Jcj&;sdP9Q?B1;p+yGo~vJkY_ZLNZ2P{kh)+lqYjY{T{`GIN%J5=eKs%{1yxbJP-6JgL^9kds6&Dn9cO3?7UO1}l0L!vMI@1f#IjbF=rCW{4KvlU8l1lqHyu`Sg4QktIPoW_&I5fId^vgjAsWx`8l(1Pcu66`f-d&>bT^13VPg_KIyq;^-lWR59&<0CQI`2B2CVHBg1V~USUI2QO^e2@bib*_cWgcmA@u(uDK!4QFHjXqWRBfE0Aml(r<$C0jXeU46+_WUy+$1M;Gh)Of%TNhYXLP85EYnnD-Do_sT4QslH?>ErdbV<`YDQ_!jvB|SA}B)+%P^&NDvbvV24gNJ)*jVGyKt}^ihQW(&4KE*v-$<wsim<L@zrYx5;c@sN$_H@4Tc@1w>1)&(iv;n_Sx1xQeQ*-I3MBh+NiUocW#e(PSfOeHQfEjCR}@c>V<XFP<J158vRR)THH^;&r%a)x^+Vfc^}3&>51D4Hs@QfAPzAgfqR*$_wYEYzh&U~%JgDN$SQSD09|0;3M$0WH6L{RLA46i(3wZ2DXo=U-6BvO>UjVpxrG5LW)!IGpfBwKtl9G8H&r;aEOTWK)kD^@1?8;`4(P1olTP*y4wpBIU0Z7X_>r;?Q71_k78u9L6UcW4B+PYd2DWjOwR|Yo<Fz?iK7ggjOl)=dyYJI0_r6#kvXFlm&|jE=#ZN$gVh>N}Bs5y3nVZ)F$NgCejkwfvp_lBL2&m|cQ9Un>YFMY3a#eTKt`1~*^d`G?tedAk0#f}n&Vc64tfdm8mP{7+Ok<@#SFdNN0N}=Ks~tY=R{QU~(ILMP_rB4}zWw?(!fzw|Ho|Yb$Zx#JZ@kFA@7y#0MveSNjr>N9{QI67`TC!vL_K{o)fdgjCrI}558A&|YUD7ZMsDWR$m(PDhPuisaN<r3P#U8tPm2XPvLGr7<S_Bq$}B|!w&2{2Cq%rb<j1-4l6t?S9A5l$M(Yc63f)Apd`gsimiG7+EXYaJvkMC3qdP(ZX*hcqCs#hFG0p_jZz|m)^ef{?34Ao9^IvNnaempMVmI7GT09?(CDk!g=!*+JAvUf|z|Zj<dxLr7n$xALok))T*#l<u#(q9%*K!*#>7_3)9P3k;=#7oQm<@l{#IKw3<39<()z>G4$1~d0vy83R^BilMU&H=;&0pQKzg~6b3;e!*#(g_o_GNnD_q-$j{vW)+e;kg_`7Dj`C2HRDyuaa?i}!hE;!{53tA4E~KcXvsfy~%nBr|sL*#~#wPtVx-DcSQigFF%^*E<a(QSqf=3Fk)UELZV)_TuShSSH2)6D!+@uJ}qQ!`+3N&5bvzmQ%Q%uzHbvg`q;9(}fE2-ryW8Ba5z9O=-k2tSgSePdJ8Q&F)uJYJuDkj$uQXt>G9zSB1h%J8O(go7w=YR_vfowb*s+b`RDVxxtOFLv{&4Ligsbq8Tdp!k&;Rl)FVHGZ7lHySjqpzy`bmrBxZmt~c^ou;sAYS6+V}F3=YaSm1Llx~i12TeFm6oXa1jl=8=(HJsOA-M%iL8v$(#N;e`fF~C5asDX+IY}Pq%D)u^R|Fce)MiS+f*sY^?IC0}0j2JJGO}l3)H9s1DIydOvD=(TQD_%MROncYe0UL2kjM8r8#`~ootg$3oo?*+uhypZz6Sv?n8@W}8s|BlI|Ln+Zt{AyEj@%#pff>0VN3Rava^ys-1Ompi9J#(yGCq+asE!=?A({~OIA`SwWWO(&gyIaUPcGMK{K~r5jf3~6zOlh8|F###FZi8b4&e-_dOC`oMscQ7-&Y*<g&9pG!o^8#07KbjUW@S3r*VvnKfmJu&j=gUDIw0rE@MxajFp6qZ5{8y2&uxdJHodkC)J(E9zpA;3ixiMU~ApF4E{g+1G$b~w}_^^wC2i=d3GsC7nXu><x=ot?mzxoyfY2?`|~A;<`Rn{CV857)A(NS^(G!ev73rT2~Z}V5ZHY=z*zZ4JHJt@A|^o0ro|18e6cjQ<uy4h)ii0~5c(G!dat2x(VqoOhydJ;H~sJtcr7}@j(y1hQF=>rm~41sAnYX0!9>t&M_veio%A7uE!wcjHi~fuAX~saJLVkZ3N?oLpXg@9bjIFY^1SETGT@^1hSxuVrwsg+pt)!TVoPqlK7%${06PJY904bWHc3L8wBQZZ^;7}{hT?zQtfq&X`Jt?)W8z}AC{9)rpi_RvYFa#;Nz9%CSmZ`rT1`X#k4P$+_SkBC4!Om1psvEgaGDv2sU;n%eBvh3c8&}u3+?MQyJI?IH8eMNuXBfMqQJSZ9l@p+L}s2uX3-iPa0?_OIx-(+%n~WU<*B2IVC=BWbCM$Zz9PY6*HiiU&1gOy&8L0Ie0uuR$t<Wfh9U?+A&b@WosWrEs)7Q84?l7pX>tpmzca?j9x?EX$hT^0=c*8O<W^9(>dUOF4H!!hpv|y!H=X*d8T^cz0v*>ZCw;YwpHG##fa$%q1>IDtvI33hi8>?4LJNTmEg3Tw=r}?J$*~PBOKUEm^Fs_C=;tI_+;h1>8<HAMlVvN(fE7nXt<hg;o$|qG6ayjVYtZ5hEjMiPNt6o{dA+uy@?N>_EjyIh{R<nxrqq&g<){hr_w^2ymOE6sutNpyQ0?*dl;2}}O0&I*pXK5ry2LZvQ#jh5T<{-whq|5bP&*7|uIwc%t1Ec_f0)(Wa45b(KD|?`K@TT@tHnWR60PQWjBPI#5n2rx>wM0~Fx#6EX4@@I<_x!{pW$AiIW)m+8$806?nXOqPl~Dhq(ox<<(Ts`q%EljvSIC=x;iUSv#7gIz_x5g^L4Hy>yISfRvj&2WO8Pp(1f0#@@ze$I0dXMR$%|c=M21UTa`4R+EDSfdBoeY6<h%OeXs&Vkd^i5hA(D!r|K_}{KaNJm$`+b?F_;}bNKD<)5356i}zgqzVzMCuwTsB7TDlI<IVCxmwFfFuV%c#2<@l1hwB|Sz~iQt7-pf*4I$vQV~Xu#;((OoiK3iA!H~E<tb3+&l2`GT4(UcFNLWW3&<EMqR*6i%rA(t<yljY?)aV;UZO5e+Cl~)#4&rks^;-qucQ<_9K=`W_;WjzK69d<zlqM}@#XZ+VE#xjS5=iXb_N25d(_|lKosnp_!_?GTmbjL+qkWZ+<Bmj=w@65S0^|Cv_i4(*OmgX9HQ*3wSu5AJT&QVQSUh@mW0TCEoK487c<2ehtRi^O*-Y7UR1y&QBd23WR))s;N^L>04zHFQlYwaHJ`dz4f`1&XU%MrJ7Ra>%wFA7h!ucoz5nl%z`Vz>9HcJ0suj8U4jTUbO++u*Y)c^B-<PQL8R5>h?`=v!Ae59!c<0Y*fVszig{l)gA8|Kc-2g~vKR$b@JawLhe7#l4p>G=*j%FwV-R-h&ssf4<ox^fKz10?2oQ0o5IUM&^ET{<193>?mh3#huuFzW2q#)Jm5BIK7^Vfl6U=r!go&i6GCpPP@PVrfXG!JA@jv%*M#Ni)|DI}3&A6KxfI4O~IEoyC!zlk~9dJURy*8uLuz2b*)lHgv4PppK{4P9)LT$MNx&>}akw$Is|q!Nmz;GdjDga2qg3)Z4L9i(fR_$l{c5hDk~Q9iQwg9v$56&-=eXdJ1lJ<&==$OXxud?jyQyd-rXSc~WSo!&Lmakp4gyi|;Uy!C)Xo=0Lzjd1q*`dv*<SPn%+ADT0}fz1OmWVh%q(ngge$=612L;(ou|`Ml<{fiMXDswNH`s-N)gJGf-k!0}YS+Xlmfcq6HSQ<B4wy;_oo5PlXECCG}k-r9tVmw`6B#^_#iRU(Vj?T~N9$tGTo#52nU7hkVBc5w0`vbQ{v!-7IgC=!)v)A?19@SVy`PP>oXmQlbaH5kTP7b7mF?pC4@qv8`gI~%1YZRcv~Sa&QZw%jEdsyGocB79Gh^%9|HkZCu3A%nW95++zT(8nLd#}T>ey`z)Vu#ew!pY4qHDprn(WGM$MntmM;=>FLQ-tw>S6zjFP3@ItDVw7wR+UVN&eR}c6J<1-ZpJ3lQT{u=D;h?4Om;DihDn_yBX(!?u>eUM$@b%@^z8ld0&MnXB@v)~dP@u={iic&)8>E+Uq}8I>z&lS5E8-r@rtq$&k~eJnD{k*Q>m_HJ+qN)%(TCU*e;tfFSJPWH-<ok-l_2`_sD4pK|5y`OB!el7Y_77unsX)M$94$;NJ*8DHlo--FWp%k#=<ofc*ti}c?|hia3pO+HlPN#m@})dWU`8D13zKzD&k|*k)((a+02~zzLv{|)!0B%ba9miqZv~v7S>p96_PAuucCS+eI>S*ry0XzG%6}%PQhAey|_39+y%@XW+P%vMIk^{uW!&!s&;68yQlJL63nV`(zy5JuJCHj1B+Me{?%7AQ(xfwJ7%Vym*lg|fpONf1CrG7h?W{`QI_#B_Tn)aATL>tMo=$y^^ZGnQs+1$r0(FSz@MfcT)bi1>?kRc_zYDqml|$IX%QnuQqCZZoINON^fb#Ao1`tQpYu>RWTZ-#<tZn*jjUyOE{g-u0Nz>b-cfH(+IE>+-in^C-(8^-`R{*>v`%}h5Yr%JtYOZ%(we{(p_^rqRpjZ(f_0kNF~*m3nH@@iO_?3iOdQu9%EN3ik(+cbg<PBC8xm@$R-77<-xKM{1kFat9fef=GPC1iSPIFo`~d!}dD^%i(?cW0sVBkhtllt)UpM1CH;Jq;{md2^#97g4sdh1i*YxscL=qNTkHv;^u8qmza#{ILKa`EYOfK5U_Ogl)tRpk0JF||iGd{bi{Q9A#QI3QV#7-NP{WEoxbY2VLNMQ73fs`-_q!>0geN7bvgk1~b5nmgk50?nc%jRWCnG=na)}h?Y$2S;+R6ze2s!r(IhadfVI-wmmh4!3IXydoxMV-)^F<FbB)pSDhkxpnQkx-^i(u~ZW+#OwOKB6A%ScK{lDLc|!DwIM6#X6eGVb2OOPA;06@~N_Jw_^u9R)iH}pLNHPi(ay{bIs6ngo~pVce*pp(0*S<Wf_!j*HgM5oESUh`sWIv$gMOoz<nek6?H=Y-EWd$6iJHMj<v6isJER8y=i0@?XkT#J{Sr89R@=b-YYwd%!g}*!l572-~5(1s7MqJ^v~qykwTL8KrZ&i>;hZuh7icKg`5<^<rMbDI?8Kq!&)3E^!)TbAolj3B`-p-ze@cpRuN!Ub)+R{aQ++Py^M4fiR~1R@^~11kVx)SNty*R1t;;`RzEBm9W84l$p+bQ+2OQ}fQ120g%U|OesmDYiBe2qRsI_F)qK<W5jW1YXO-k+;<Md<_#z#-{tfHYbW|+bV}&m(g@ky@ve(3A>%z)xp}pe)Tz)&hROced5y4_RF`c1k7L%TQPOeG|k;I%Fuv#4i8&^I$Gw4f%GAZj>mcgxYk{VfgsHfs^JEp~ja22W(A+H!zGvu37Z0jSc%I?~P)$9_*hF(uQ>JSCW$}_4Evvv|ovGs50c#&@)vPfQjiWj9>-CC9hkId#lq&@s<{gtgCh!<LYwPHs`5Y5PJo@53_mCg{~ZXt~qhMb-;0`dHCbGZ3(HRPk*a|V2eb@cq-eJC}hx#O@p&XRS_$gpDEW3~}oVpvhlusNyzu(aRVKD#XaFh0q%f+3}p2&bAC43R?@XlttbOzwk&T*ypWjZBl1xEd*QX^c1WN>X6*g1g%clW;HCZkfqRr5{sGlH(AOk1(kd3T|=rTvP}rw#KaFy(IaHe;HlVO9TvV^g4x2TZ!)ZQ-zy;QMe%uP;!-CNu@D)3d*fZrTSx~*MIx>O-7dMT20EPqol0dv<6OII-i<#>&ky7M^LUuIZw^b;(#$hn^c@GBhXGBN;=8WBE8nB&n(>LYFR60YC9|z%(u?ew;kr(X|i@s$$ayx?w88GUH0~vzK!h^S}&jD*Pux2kvXa#MF#FGJYh;~+(o12D^vDCfDV002oL5gV2Z-E3EkH9^q;hTXVj(;2&^1+_wFl1fdR#!)}{x{Qfk8n12R6?ZUxF@>w*I<_53ilRz`m(pP9Z1_%|Uz67ICFvaCO~>S5CkcUJnvHAE(2@7x|lU!>~4Q@P)mBLj1>CERRi%aFz?haD7K6}tnqWcl8EtiQZ9l}G|Fz#wPzu*y0Av9C*ny}z0TTbbFW@?W!qBKIC~b+Bv?==g5QZ5>=$Pr5<AH{LIgZeRaYzHYq_Wp1ySJHE^1Q+N|rT}Er~6>^n_zq`SvbI6rEdJrRecv!ii@xvqIh5z!6hv|)n>5XCK?bo*vejDMp5q{%gdjDU;8wt}J3DX-1(;ErX8wt}#9oRPprZ)zruff3NOy=PN1CxQ}<Lnw({D<N}TyP7iOaJ{Cn1+k=OCh^C2M>wUiGNLJczUj9V6r6PGbBuX<;d|19;P`{kqCq;6%#LGMsCE?OFgEt4NVtZi^^eGuojhD6El+&SCHsT{DQ`5A~f=DWOX{e{)UY!v%3y+PN|WWDH|=5rDV@t|IsZ^%uJ%wpU9>BNXt~|jx5s`MS;E~XA-N^{O9b&jG`${kCh0s;7{n6+?;yKyVDPzkU7=!pXFzYBR><q5laLTqn_<%s7Q^RObbG$a7@T_o*gH+k#*)GAyasPkm(t|qT|0duOMeKeEIX7Owpa==?N}eOT~2h>y`Xc$9GzPwX1rDmg&r2gVky-(K5AX=!=eS>hu6MGhRGqq$V1<kro6(@eD<i!VUdeKf?aV%3U<R@cw1Or}3Q^Z)9;mJaa((HC+1C3#3-#m_&Dp#%Vro;T)^ec)&45R-Dc-8>KL20Omt?G)lp{Bg!jLaMjCL{tUC9<G)3{?$3Q>u}vWIT9p}ayIU@1I8`>hNuDWfa<|7<gnl8dnJKNw1AJhKbQIOhg!D?GMS7LlOPTXnNOMF)RQ=2_`-q9kN;@OW#4`tjI)vDdvYCGNb%YRNp_Xp%vuc@={OAC6TYemzLG7rSxh8U$tydVOf71PV-yHnS_jw18e&_vesE?~*LBGuMpY=oz;SNwqQC|UH^tWzc(YYgHa?2Xjy$W29YDEZN+~eaCsNEG0;1R{ha=Tj>4p|l4G=#CC0)V8!35|mD?8`N5DgPHidd2Uue#svxe|m6YclhECFzsR&5BGpe4o*gaZ(JQ97}5|cwX4TJ?1AImsYx%`k$|o>5XOv8=tkK8n)?mk-1z)M6%dt)7kOgs_^u*mIKTF^@7w_j1@z27*{JfrwF!pd3_W(bbfXu<I5m6>8)KJDs%y3`Z@B$S7n5x_eHonA8D|6O9rtR-SwUp948~4)!Nju}*2Ko?fg7%%B(YrH3UDc&oX4j$+?0Eg3}+Ow1So*5{0DS-j*?b!%R(GGHDc`tD(~k36-U5U29{1cJDc9gPRv%2D5BJ8c{8Yp3hoCW=-3$nd?lOK$_LBwJHry`oumOI^O{xm%bWlC`}E&!*?@G4O<8#%6puym64jAA+`+b0VYea$ga|(crrfaN7|1*)IaFT-fPjV^Mez*9Y*57xi%%w*9ONyVxh~$Uq0?IvvVl=1T|8<rkvNtpml%%J@zfW;z^}%<J(k8JoJGhP<C9AhpPUreun)9^jj+ujLOCj!HnXJh?gd=CMzUu_s5XoK^iS2(8Gqq=X}mybJYS{pA}30@Yk#&aLM#Dg;M-%FyskHmyp7=Ixys}bDI&)u6TYPax~Clt3lc-0-ApOZNjG=W%L_}ryg1j(^HR!_M7me9gMF4FIuujbsB=40&8s4DW2<Ot44Thwcaw|uuB!5>MT%&<Nk@;cw}sMUvMV7whRNQU9$&EQ6kbOJAD&omKY5lC)SG|%#7h|#s(-@kz|7Z6ST`3XGysv(qxwBz?h;uyeHFIz>U6H^tD#EHTN9eM@Yu2gK2*X?^+?WLD`i9MAG>)#CIK!;^gpH9XheIBr@ZBCGl}~Us`g(PRRw1%fhNz#wSG97k&uY1kgzPUX&uSgi#mEzX;vFHUUX$sCf16NnBYinO}8I#%6_BTsDoO|FKeTk6x`MFsHZzYI+aJIpfx94D}~f6cY;%eRByerT~ifOMVVF=Qq{H#Hm0+CfQf+nR{4|Y{M656jTY@Fyd9$95L<RBa037j05^az+W=Oa^s<Zj9<Vy2kZN5m-KT2m|CKW+wWo-^t|v+jIJAl%{84(z#n#HxevIkfG!;RI@HsvFa!gAGAtqz+C<IhHShi1?#q7nfi0y<pexSwDeb50zO?Rbz)Oz&9Tv~d>ckR9SIN-7E4fY1;VxSt}Kxb{`D=6*}&ar&!tz7_4tDdJ7v3omy<K7uwE?EG=dw-A#<L7|Oh(MBa73i2f(k+LF313&HA(pKN_!T(k0~O{Elo<Ek(s+N!{Z-1tKY9O1Hl3e$@yFTvLov|kHFVQINKcQyE)OUX84}Zvoc4ZpSozl?D$Y+Bwj23MkD+;zN+sS$IA{;VPFRiuj*nEBB`z3*&O5puwxWh|%#)2DUjL%|P4s&XKgDeGSIof`Kj|?I@Qc&a!O@jKLT3Mz28wr=PiKl{e+6l5aGeh1c3c6akBPAgL__oauO89J`c)8YF#rXK_x){|FR2W%`ypQJwyI+TGJ2r%%5HR%b>!I&yz25Po*7T~M?y{9;b{Rz3Ba;kK)V1~(gVe>zilj&_>Od_ybRh+dGJ?i&<Z@;U~=x1i6^d65az%3p+M)~w5%s6hnm+>4z*``*5*W2*0YveWvP0$Z7m#8R6XChR+$=3>8h5^Ys3YkD`ae2Gt#P)&b1LKOt`!{*ChAaESuM|?8Wo}kfVs<CNG-Ta(uSsanZbX%3gJjT=7qqiP!ubf>Pw15)w{Hp?I=ZsJ!>0s)-LY_cE^;nC8TWDC{tjwoUm!Cs3(+5g##%j=i<HWcpDE+FRwBMCgU_*wK}W2Vz!<LC%cWk<n>DuNUZ_ms#{f4&NJh3NDi<X2Dp|@c5{v^N?)P!oI%i;LyZ9qWZFw?Id;YMYV#5`CT?6L6?^l20_Q@+p{q~+=<QU&RiVzJ8XEWoUD7c3xvS$oOlh&1MY4m)u7<q$e_|c^J=*M$KsR~u~M!r<6Sb!*h=7AS-6b)%UKIZSv1y*rodi(#4FCdUZk_6=O(ReF|Y0s3eM!q4C#&}6=mQL=)gGTlwBXx<Q;BDHrYS^iXr^6j^E+g!3(b#xjc^C$g`L<oX6v*`gSGctqhAccw=Wa$8V4s#okh0=x9Y=mxBk+CyrmPWXp&dwph&fqSs6q$hEIov^(@bO-xZU>f>@r7*Q6s)TvUQQ@0`|D0z>I$DMxlgWIS&<gaF)&L`u2<16j-!d|)1UbI&uoIWvG+<HHDzh^VtjSQFM)3jZjd^;Qa`_Y1}t=%Ux;xhvea<1jTuQ~9!4m`*T{)KOB;6Ehm_j6-^x?IF@>^blc6V3ND<U2F;8*VcFk(I+wp9Xt<^+<<0(*5a3|G4|Lu>lxOp$}L003$!^S8NF_XUqpRW&50c9;|p`B0UGo=i_EtINPaQL}Se8O~WQNMz$$TM_K{7Au&%U$JuS_%r1{@Q(my?w?vPf#NgMywp}ODanSi7lSaAJHECJN&d~&Z9N!CnzZF|hQlArziJnYi_*R_0mW+OC)0S<OxO&~XO-pB93_V6BjC-+GE=1H;NKf+oapmZ&Wv&#1T=PplRRoG&l;@eEtj#sQgh%wVZul05<g>AqFncV)tvgoB9$fqk$*A1<CL>6)CR+s9ih}C*lnJuNV@Ja+D`zDt@5>gQ{g#LgaBOASKlz<nbYvGdWMCzv-!T`#+|htGeKg9l5eL8a)}zDM#YfoUD>j|$LAc`&;9SSLzegF!Z&vVX%ZNU3U4Bps(;L+#gF@GD!#??8<%S`A&aQCFKOLszoFdh-yQ~j*6matXg!?Nn?tvDQzr`#Ld-&q_Fv;K$wiuP+puoJ?0RogkesX!|koF{N-1@NX<Pmx%TFUzt7UI2IH2Sjn4?gggM7(jOnqb|G*ol<LChx6x%-<Db-C<}4hFPIfXSEOIQQ$nyraVcbIqE8l32HQ4YAx5s&|A~VhY_O@k+0e?z(><4OZ~e2DoKFcLa>9w-q+@0t{DtTuug1U&l^GU>5eU_hF7xWX}VPcJUtRTwa2Zz`vU35?&;a0?xRyw^p07CcVHRy@AM8&Z$Gt;Z$;uBWwkv&RUY8G3~z<iGaii6i!UZvthPi3@3=rOf5IH!(LcBB8`{m7fIG?Tykquzwbg}%fl=tdt5t(tPi`#G9L%nkTwS57L#SePv9r9v^w>n*AWOK6LdMMeM$;*xP`u-suESd1CX<2)xmKbW^VT)agpFP5MzTOk0@4uPCAgJ)9x!mwV6*(}JI<MRH0^t`*CsYL3(J<61mXeMJl-)4x3iQS{gA8_J;vMzWz>C-l!++SG&oG)^IJg8K}b~RMRje1Hp~vzG=66ZC%jk(8`XB?wyysgReX5xc4U|Jl>uW62b*wP)~{%#liICpC8L&%CMe@FX_!A+)#xv|-}d1%W{mFLR)rmPX{TBz38M1$>GK5AcVd0Sz||;bE-Ti(QPV5BDhp-iz{C|dz+y2C!@hE7W#e4|21>}5n*ULaE3;Re!A2ieYw2n+#yUH=O)BG8ya2q3fUv6|g<u>3O%j`#s@vwYfK_2%+f$V<Kp5}ohmn&)cmZep#2_7mW(?ORy7)N$z)YK08DH;E*~pu7)l?@6b;q8BX_!Wydk5d&pmP~?g`NcRoWAP=sf&YW8Jeq83md6ylqAzzm!T_5Guz^$A3B_$d$M@k7|XJJf^2qIV_bt}k|E&#y-1_+8FN$G#@m#Kie^}mOe5k`&=bpe^2`{fS|9Q!{~3(W$`0h7#)m8SGfO^}IbCt?Z3e64;c+LUliZ5S4vUO4dXai&#8W%_b>uJUSxHJ_!6fHW?o@ta1wL8wnv<~7)5*%FpR<aZ{Yq?UFpdsyKPC9cnc=JiS;pib?{ci0c{@W{@T^Lytxd1pSeG*F7(KSCH(4%rJ$A}_KO(<UMR*Y{m}(NO*9WJk!Q-d@=5@Zx7DBXw3VCEHu}hk6U>ue>RR>uH;&-K^^M{Ik5Iq2$0gjux`74aM-YJJs1Afno-)g}YcFwNfjU`4_=~c0DdOF^i2Az+y8Z9f1-WWq;_y1f=8-pTo%3_Z3H2))$=R%e?UZu<^XGB7(vAQ|DI}lk^8_`f%&qIwqP%Z1M9OXeDC2}He9Kng(9I&sZ^3C`v*(5V0Nw9qTD7QgLZL-&RCD-b6Fac9uMrY>Fs}k|d+@KPd;54z(*Z_})6B$V+dot0g$#!yW5?)hV#1P~1FdpD4!Gt%7R~ew_nRA%9VIoVzqZLdg?`aZ*N(=4v2>j_+=wj+qm@xW0WmfGwO_vvHZM}Y%u5+9^+K7pANYkkLRLyYqMUD83v~0~da%}3%zeQ6p)satN2C_B)>`neLj+a+|jyv%<MVQX=|L64_NwEPz?|EYfB^SY#Dw{U7A}_$D5&ZM<&;d|AzwOKxbT=detR|nh5GPT;qFf{d9ErBMKp;P0d3NJen%^!7Njeqn1ORcN8a|78NvGnZ48&1;v*lQ=dm=W`+O1rnbZ^}3PxUZyDm9h4TZlE$IoTz36H|&Ht-<)pU5wM8?AIBs3O72tLJ{8h=_0HBjyE3aM`l+(PKzc^W@UE~t2%KdS_)OsR00dtj;6ijXsGRC#^cA)s0)3p=>bEs7{%56`ppJ>9m9I3LA-a1$1$G2es8qvoNl2f?NnR2{66>Ljz0RAFNAX?#L3+BjlgnXn3+6i@9;jWb_ws7C-RVChRq;?TI?WO?%}IoT~64oN<iJh*JzmbUURCI<-1XWSF|xqGnJrlgUEwEiL;!93NU3Vw0+Q{i(DzTYJwO@|7%>nJQC=Ps+iFt>3+wj)UdG8bH7V|<`;nyA0xWu1cH=KG~c1=jELI&iOz5ka3AiFmLta(z7_T35ZbMX!5D$)QXlEql94{KA}OSiPZGESH9faFA8uV+GmG2kU-{5L$=g{}_>MrRivjp80VsiCcy}6o&q8lLymyO#47vluZBl!0o68Y*al|`|xYMPGyC+-MGU)aSx`{6-yLk!g%F7)W))I6lM$=slx=pc#NH7!MRUnZ_EO##SZjM543#c)bbTK0DY6uK_=frYu;q9f++we3)4Y#?xLBOlQF`0w2G8#a9B*)sb#<8Lfq(E^9tIHf{g4Zwxeir=joP1?oHWqg;gYFvR$9jeQ)TBoS(%2arUvmkMIg!l5JWn8*xU<^{-}S-c>+Vll;xD`5(RZJ@;d=ziJcu+16KcOn$lEjPmrXn}<pWbbaSBUO{=Ii%5+}s3jJiK?Bi--FuZ!KBDL<qOX9ea^vutJB-+F=>gfTI8C&G7#o)HS60UT~1hRRalKzu=DFJuu~AyvC2*Ci6XDpEw%&hcG0Em+ZWFl7#8uSv-j$d=oSkdYZZRy`o2cOzKE))_`s`glqzJXirDu=depR*aoc4mjaqFTp?~{6{MA|9kDO(LG_0Fw0~1<>dva1^?Y*0c!L?Aez#Y`x{e!%LRzIi><%B0ImHhy|e&rY^rpZ7N9P4O_2Yx3uhM~@XRg%dW{v-FD^iI4cjwo5KtM0+ACI&aA6zOKVDvdqEx%aeBZ$6Zyo0g5K$aV_H|K9j{&?JXCgm6{qJ_Z`UEboN!h8Z)}7r90BF>jb=|ppY2ArHVtq;+c)98$+rL17{CnT_d+vSF_TL{M+uuBE`+2nebZq!)@x>U{43o@XfmXPB2JGiEU}paJS8TiC+_sxA2|m&c=zj%!?svK8eqL<f4NowZyyk9*suinT#9|JrkTr@KtwVx)vGug(R@;q5oh!Y0%Plxq5~%!Xr*ae^kx0z0s6K}rGTZjHl^zGj+*_46(ZShK*g4!V1dbL5fnbp+*fN8&P!e802~OSG1rI=ZGR@l>imH(mR{eH#9y%rmbl8EH4QK&AsMgxNrv?!H0mdy!4MKSF;8IQAWi>!`Xp9=vC~})rK*pbb`F$$G^aYy+HEiQvZv1+uG|<`lFf;nAkk-ZAEqG}}ecQ26+)IbUtI$3bisb=$7J-k-#pScN&z6h3unB(MmGv%kYbl<G{egANkudp|<zjmC6m8)#yAr*jlG8JN1~8`!pGTWH8x}M=){1Y-0&|Z+?SJ^|S1?t(Bro~%MNC#O%hfd}Ma)z`js@+CB4(IXFk2<>KR^+a$&Z~gk7mW<z*xkbE$J*`M&wbaI;O8J2iKG`ZEY-za3sgF1fyrdm!a-BSJgCYK{IP@r?Q|6{(NP#Txv{yA_4I#CM+74Sm>+;rx(ke-4*4|aJmJYEp&n@_PSbUS3(!qfD)ul?WTFBpWGT&ta!G~NAHvSClDJXY!K)ME)VD6yF4vem|KI(-%5|b*Qd3x&QCtyxgRbD2w<Q8LRm%>@4^Z}O?bLPECw|5p{6vec)~rFhVb+l_F}d@xPcN^<!RG=!rdc4K-qAHC`aZIq2IZzBqf*S?<BXmGd(PjC-2It<S5AjBz#h5LWTdgkAaH}gR%!Le+>4Nrn|xWUmQ$V2|0s*)BPLF@Ra|)01CM{c{h8&){yht0zOm%P?W!@z?5%Mgly^gA$Pl_Ag^}O9aw@r!%D!^i<{Db3U?5+4cRke7*c$h376~Dx5g@K7VR)MB}9;iieO<U-&%bfVisWmCJj}o2yNI_;04I2NubV2_B3{^2FE*qp*49_$Yq_TOl-x({*KzWWuq&ji;y~6YYff<`Nc_hSRz<Rc8jcDI@rY=j2H%8_KkMVoweR2qgmpW++hDI7kFn;uQ!GmrndmkOVa-d>_eiHO>k^^6Fu=>n!ZlJd+3&v`N+f~g#T7j@o%|T1qEMnZUl&)plvKH_7Qu{TD~L^uLQ&F!?|?aH5eGOG4E!3$6kAfZ5-S+sI;WbVo>>vonL~xtP*T$i)C047naz?kRQF;$jctFZD*T80|eNHADPfB8A8@&U3{XOeV9R3(%RPZr-~lA4{*icC6x)EEo0UOrOV*?*(yyI?fn)DfLhcfwI~Rp)WlZAOsOm-c$xZG#ufO$%<Fn4Hw(^*bWv-z`)KiK^Xho?cYQK=PZS5$TVCP3bZ*KAchBd8v+o#gj45H}`OEfe$jQ!6=&dVq!<HD{rAaVc&dbd;S>cS9%+6OCAHJp|gCpB&>0@rV>zEQ|UM9~x6vdr!?w&9!Okpy|(8a1tFNCMFtZ;Ej?ulJ(>$G^s%+WkTwQl1nNX3KrlnI(Y`)YZrOD(^FoD65>sXXP(bZ~w~p33eUvDJ;qQ-vdWs)X88?e`t!sfagEh#ljoP!$Xtkw;|zz|OLY>>uQ$Xj5B?RIzOdE_*8RU2n>DEwx7Su6Pmb0tE7p(}KPCcwBpH$4C!Q9Mnf7sT@y~s7weX$xdT;XVO#Y*WAD5%kpvi3sujn_4^^MuyUt0f0hlgoDY#JGSe>Ic&Ut+d)x#gF2S7K*shBWC=x3+vinJKwngw#Che0j(2+YtF<G`!Zy0ElZRiU&1(qcM6f~HE?5HY_tAz)SvK#bYTpJcdG^<KP)8hgsBATr-5!@fk4z*>T>Z`#?-f_bdmOZOuKb-C>l4=Njel4?DEgsH+cd-JSOgKch4(iYiD+YbH8OvEm2S@NeM&S;?H4h2P6)&FTDQKo$ue{W@`si<gZ=<IXE0s+-Z66*eue%@I{tu6lG5&kFZXYQRYE7ucY&S7@%d<JoAZ?MlgjxX99p^h$J%4Aw4eT<jGY$?WfQ86j?2uSFn~^QUKNl`{RE-Nv3B8;OJ>7S>vtapU{piU$Tj~Ed3l#7?fF^B*7f4(&=Vp#NsW>C)vWx3sM=;q{<w~MB27}oe6l|ovm;eTIDA-6-K^H9h8n99*?TW&tTHXx)H<DzE^@4;G6ZXw+(+Dc2{Oh{jc&OXNEG(W~?L>xwZ<<4rkv0xTsaX+Y)L8FQfPS$wDuk!W%m#zOP3mk0RgBh+-_L^e#9-Z5wv1kkU2eviVK-vvj~QD=?3fj3XGPTbfp<)FpuSZ#K7CbV`*o@sDrtb9<6Kq4OGxZoMX%yl&p-+~YZb{Kqp)H09-peJ(f%Xvw*?me@m<Xg7B~FGZBGkvaZZn-DT;5ucDJ)W0TB?{w%5J1;l;X1zu%t6eWJa*?e)Yko|`w8n8}O1XTA$^6`z##-fPbbdS~453;^fH{jcIzwcClv2p@dqZWl&exP@EeJ0r)Go9%pzk7rX;S%|dU@EY4%MkXcOB%a;sczJc3&lN4a-1BhE`niy=3QmvLFmkBqAIaamGn$HcG@EBx5wUp9HoVzrxJtTZ*!KCh$A}?e27SD3&-*tN%g5jIfb~AJ?U8O3xU<)8dw#a<wbyNXt!;bS^JeFtZF^zb_O8g8EO)-9vRbvLJKqVbRr_hTy+3_Hdl3rH>9O)z{g@MhwB#4Vz8q<Z{jLo5gCA6;rs*+J6xkCd@^#h-So23Y;EukH7w4pk_KEE;NlZmC2or}li-kTpXe`cXsr)Ewm}^a@Q{Dc~+Bs@BZiN^yBNa3`9#oL2A30cwByfUu-iq_6S?RktiPIzTdZG$A@Jo$?oel6tS~ZP;5*GbKly+-mCvRlip&hp8s3tU3bs+rk-G6IYt6LiCYgvv4Qq7!YIokQ?Pgssdjdf230Ke4Ly+m5KqQfI*1j}H7w#oR7(vshZFoQf`Wm%<>+-PJr0uZx=MlHJx6zjI^hYfxbTMwhyItZc|3Pw>Uh%N!ESn^c@+|5`R>i(XP8$~Qfx7zn3w_O98<lY+vrS&a1s`iSvtYT8EE5pk@po7t}5vr^GK5Q`}$rYdQfO1n4&~hRopix&hF6oQPcO9nE?Wa@JE$id2O+{Poaj3WK*tep(tukRdmk;R)Ol+tTmY^Mn(LKRhcJHN)nyVL6EMhf;MqIJUe+AW9Fq-(aNpY8d>n?l&>_5-LN7=5edM`)#$Ey!QI#R62=y_a|LA#vl4oab;Q=#@Cw1I8?Q*w{&W4gDdI5s_tQbq86mmbyLQhp91jPPs{74RC@po<UcawNyYy*EaB0<MEKK(^M@6xDsl49@Nb)~DS$@vz8oz}95FC#IjPUJo45VwvcYwNiZUkbqXNTig9!h|oK~YLDwYJO9BP7A`I=+na04J@(|Cx>@~uMeE6E!P9$0>kUgiY;>Grc1C61p9dqh@nYC6KK^83dj;aE1=w5Lh+O~GHEjSDj(azS?JD%1srj4)@1N3zY5u-@%U!*{A5SNq8&-OyA0N*7@oTA!dw2UvP;Sqr>Gc^u9)sY|`0<(qngKKGW`H3~dU%ZoKO-g&w+Z;G)eFA6Z$D|Jv;QN%_fuBNO!&%f0ASnKsnp;B_Qv6TrdV^DvSKeW(<*%Oe%b#&OI*3BWP^H*^Y2ry5gv=!J*7a#FS6$RF|A{kuJ`+wkp_0li9mp<^R#AYVs)a%@<f;wDPrv^<$Rnb=(;`^nY?A%!kBNPRDk8K=n(Sct>SK}-Ou@8>Z%au!+SK^$<1p?FQm1|E5poIh?QqOj5O^URWh~pEcu?F>y6z@>rJ$7VwA5e@|FJF7*Q)G2(LS<hl;j;%J$_Cje_`{H(C2PS^GD^>bGCtM)+-n-$wXN*8Xe!8s6jMZ_4&>%Jy%{_HWAeZ_4&>%Jx4%%J%u0H{I(_c)hZHuJ5nhT;F~!bgyr(KQHLp`$^v(+*)fAVKLug$*wTc-c1CH;wVQKp#ax8s$znF+d<-WQFxt6oV+qywx+v2*N2}A-J3Z4D6l+Jy!T7R@=++>FQw)U*fgou`^8_IQLlS?^XLr6Cp1d7lQ+ZsP1bpPcXVq<*BqlU)6He%=chgMb#)BQ-_UE5UMCM--}$+|{UjQ1zxw$*XRe$iiOGg>J~E3dsSjd$bNOh-6S|qyyjViV8;K+AtX_||6s5i6qMI(;&kk$c_-62zZ*cy-(~VT=*OSM0X4s!G3_lw>d|j+aHC3Wb-`;ya<1nnE<xA0f-Nh)N{j#X|C^dgx_&rE1Meq2k@$TdCJ2tA9Ro{>P>hrOBe0b^O=MNYK+r!x#H1@~mb>p9ryRQ%K>m6|QSGdKI;dI>2T>Pb5dtOG~FHB<8Y(Fc*K8n@5dXY(7h_jFQ+3hSo>(9S4mv%pMVVCdg^g-7_2robA`KO|LW<bu5Seh>E>=iz9@$;{kj|STPPbBWe&Uy3*F21?=>hmuqW!YKT!Co)2^?%X*2CA8$myHmw$kbAS?pTH<%TM{V10pT0L?TYXG)R)&`fQENMoO-C@{=Ra0{K^ffbbpJ*!?KBQod^-kER;g*Q|oA33OT06yY|Y3ve*Td6bEzQ(tRPp`25dvp_VOb~7m2NuC0o*gS2dGI#mv4vHI+MC{~!c<H2|t*(68suqx{bQ-ZTQM}jXJYrmAcm5j3Z%wV7pf4)g0ha~sG`!yM_=b2uPne#UXlglkW1<Y?Qg#hgFG#%Jh+P?#$Sw*ghcANIR2znIyC9uzgRM~QQbd5W$*1Lb#y|QxvYyY`K6sw2M@&6NE_E$gPqFUigscbZ<6oPsX9b@U&HWt|yn1Q7Tu0UeZI|wtrssBd%+Zr7DEr{UXV(?9Ge&V@=b<3{#hNw%k=Br#*I%Qfo#)&>BPbI6YIq6H(NI4A8G2J+=}ntw+u0M?&)YymcBt(W>Du~pH>(>DRDNtYEz833?s{(1ZbEXjWLIAIGencEek^+?LhZtg)zkw<bAi~@s}CAey`K<GR}q`0N^H7*9kFS10%r;Yc7%@x?D$1PG=1hF-FgkA<6B%ZwoB;mEnCb<>+z5w7aghp#1#SZPE@5SZ_XDBEPAUuQrq~-q{iveKwv|32}biCxma|yB~rSOd6@dqks;fnZ9SR@G&r8IYOF)r7)lz*?j9Ej(V4y1=7T7syl%q29Diq0XPR>`uKNm+Ewg0}b+G<3_t(FcN^BXy?bY~cp}46mw{ECI0A`+;!%|#MDC!K%grTUVLJ66trBLiBrwF?DNT&89AT<_skfubFLkUDV`w>yiK(DV&Rwh)By^v&ep)Ly%yb&{uwV&zF=&CAdK*JC+T2!9h5^o)^M_Q9%fIBzE*{r8a*olD&1ny47M1Y59hR8{+Gzlt?1q+@<x#s=Yr<8cu#@a0Mxdy`%UJ6UtF4_!NE=j?Lltj2N+<5f=>nFCRCT4%mnmU5wx|uaW3nyCB!_1nztSLFQK%XG<LFpIL3kKD4(Vnb{K2IxaQg-32K?(OGF3rZE+o>8<G=}ABP*nus)i%{so66Ou;)uV|8E_*Fgpot+&RA9%^N`K5?q)kiaj@RQtZqLk6wv>j4<(X)wtb|EWUrHtuM)|gcaT(t?7o+l<ESyRP{{Tt3fX}Q)_$~8X$X$%9U>kvc99eWU_6`Qt&EhkaoudCJJVJ&HI%%{FmZ-OTS-&fN&vkzTL>H_X*Z~?WX&vVRD59;%57lYUy`%}&P1}SLiUTz)$QrR_wg<CuYKJmwXHo)cOs+XPcfm;NV5b~mpx9|S0fE1@$^;cIGfIHQx?;CkCP;adVb?<J(bp38qRh)84)`;+OWOjnGhIFmY%rWj>mo{Fr&HhdZTaL7{d=G=@9^IcspraD7Un@<a@22OiZf-4s^N9w3hktfQTkaC8(8>8e2?C^ijTXE%i4z;jU{Y<2sOyzE?k81__>T%x8YL0tZn`r={5YojcEW_VMiKFTbZ9eM#D+_qL;aVnHL-lXc1YTS3-gM8_5+t#PT}cIMo{j@D`?U!w)@#Bf5A$)wR<V#8iW|L7hWdp~$ch-{thi6Aw5uog^kDcyi#HIaRiPoDCjTnqTX(P7sy-U-CW;%RSzd%xq;UVZ9Eoqp%zd0|+_@vxxO-H;k^t`<!O!G#x=5yzSrR?gYMab))?I>79iH(D%Ac?VCE8w8#_<Pzb6H739`laMAKC0itE8UYE8cBHC9o?_u}CG`M7LfM7dD94>Bn(7dJu2!oCOH5h&nsv6x^_%v!rtWL0>}yph$22lhSX-~;Snk0pL!mGc>v|t&`x?1Zm;0JYYy`?whhYBKW=1+!zP)M91rsOkxVv>{nlR3}^&j6<E9qPr|DV2&bZ#hjaF%q=fj`=xC!Na^>D*byISjOIWIL62$4*_BM5%y=LN-HiN06BLO3ToVl8Dx1kQ!5YA<^7|WiD2hxwvGRyAj1)BF}nU5Y3tStVClGu@O2k&QYVTb`0Qgp}h?@vM$@uz!ZQ5eas`wc<0vQol9`O6Ov=GyLWdYo%_G+f!uN7IDQ~?)xa~M`g!6rS#ijlbB~3)upUdfoN3iyu`#xMKAHE;n&Wm1-y}Js2Nl4Kd%m~2_mXdsr<+YTl9a93RxopJ#0izD`HP(zUUj*926W7m1*|FXF9Nx%xU6*SkM0=vg{mywcE~2Sex^hmMUHCA3htvLzZ@feXlXNz)3NbN0U*=OQ5Pcutn6z$7=PxOf82=pEMP9I@JK0m#Px+$3BAdMCWNt-LN%W>>Xdr73g(!!(r|aC`4~yV(zDiM&1Fg)Qi{Fhi>?j#T4?Avt@A~;?e!6>2|Xq(ZjCKE;e5nr{X)rq_!Z|@-M{Wvds_FmefM}FL0GQ*0Y(}hqj(V7vRK?j<N~+!6dNuycSKo5qbINel#~v}6h(dAY{Ctw4ddz-wSapS@YMRvT|f*AFwl)dyP>3j8>6R8x8XkNY%)^x;`g1qUB#sKAC?Rr1~NN)>77p(7KiYYI1+pi<xkz6@T0hkM!eE^dN|<Qk8#zzZas!_yi*XyyKalQ@+2mRfa`39=ZGp~V0G(2Gacgr>)K-M|F;hnY7d^y|M^fGMBlFpwK*5_Nwj^_SH6bss%Tp&T9A~^y^@R>%S;fq>q^+9rodT{jVU_v0)i01i~Eodirs)wYmnx)VYz3~w&HI;#^STEJ1*RllgQf`x+|zd!MCTd(e;rx^s+7TzMDnfZJgYb`<L94_IE>i==JW&DJQNt$<2Fyy?X+QzS(}a1NA#J)!Ym2Nv3<!U2sp*Irl^pIQC<T2RYJb+!L>iVtLLifk<%e8sFp@PF(CD9r}p7uKFf-Ftj_}=HLEWi^yx~Ug{#!Fnz#9WXbq)X%SI^`E(IM8H1rsdS(T|NT2Y&R0g%KCXz?$m-+JH7y_4}O<FscBu1Xa0DsFB#7N`Hz}`$LyG2mbUS2isZxF#r@Z6g`2+HLpf?GQi?9^hB&a%Hy4{by-?t?gBP}{g`#RWPM!1N0O7$j3F-;Bw3$n*MiOfW?3eZ37XBd&RcZ8jK#$u{R<w>CKD`pq^w7@URO^r<J?<fB8_-Ewy$=dEpUARDTcj~1*$z!3UH%-zj*H_)`4)YG}9D1wKDs^mcGZ{LUnTa}C`XyIs{jU|<}>1chFRl@m6G+wQh=dCp^;_sgP4w>9|0;yWRwd!bo+TEaGAkBO2iJcVsP^Mhum9tr{h2SfC#x7(_0D{K;yjwi0n1A{W?q~d8khCwpvkY7DrG^v+QmvHruK4z!JHMhR@&G-0_nnabKo^T04IK9Yz$CvWNOT?ix`o5gHE<I*5nIF1q=DrG?U-dA{P?(a(rgt-LhGw_`<>70BwZQR=6n-Ttassi-hJs!yc%ef82*7a5D+U0ajVXQlN?i~thV6~!j;Ds*%He0u6&$22g+(UR6&AFF@4{js3ldeGPPu2{_3KjdBRa@%LGDf#grGk?ST+)6vRlD;JLTT?Ltt?n2U*UrZF3gTg_w=)eg)!qQ924NUGRlgO>0MgHWePwj*w?Wd;=$U=os~w5aH;=%6-aHSamA;4m<##OvghVk0_CG!~d4c!!Z=aW+It(h+S<0TgJlOIs>~ekzq!$1)QE>L-yQ{Ecuia7d!cTA-S1<M*SH(y>^HKmCL_KN~5eD9lW)206RV%2ZTzph+0fDG~Py%sqMi%RPQKxDA*7cOonIrlNa?hvl}U<UdsOa#Aq~q|#D|2Z3OD;_o7EImaYWOvG%)4n&1wlC3*aB;mZ_*L{eI_$SKFF_fr7+D}g&Q*HDyJ%yi|*d5aSqhBM=OY5CDw8f_5{FZ{b%w~Lf<Fj!-#D^XuP@DnNruS~Y0?VRbp-cionkGKdqx@ke7|Xk!Tg8`fIAU3|8kVoiA0Io3jBz-*Xo4233*X5VCz#@A%tjCk4#+~WyYGO^jg<9}6iQ8s-y-uydqegQh6IvXCn6CzuZCQzg13H7`JyPFwCpGkPRe6tYJQ>B8R|JimGUEmNtLC8Bx#*d8M5#b;~#Q=l@w?{UuKl+9zkZ*J77c0zwYNu8zPm^^$F9ge**iHEV3M*9^A?lkJGARjLQf0enYb!4_j407uL{6ck9CX35k+>m%e&}?$*H9>n9Ur|ApcbJi%$+KT!eFg&%za4G_qncribTkK<c5Pmam~;mZTqW!C@Ghf4Ir>A0qPeVsSlP^|t;0ei~wp9`tIf`Ua<9hqvcK5;YiiQ}b^+KC>n!cc{*2qYM+6-Y5uD&60kPt5RS@`+uT)v&|7hCR#mBN`fjVO+QJiM9H<eM?uEPI<YnXZ+wh`N18YbD2eVtwr`>Nr!khdJ{ezIs!1<Jgxt!UEv8<Ar|NNuuX_`wXZQxK%E!CT1;aK>s%=+AtjtISZKrC?TE5Sf`KQ4-RC(b2nDJCpS^ecwPwq&gKA!CR@GXyE_>~@_TJ~5ug^Js`r>wXyWOz_1a$rc9zX~QB*aTVypRYGc8Egk*a*oMiVd>mH~|R@2@Avnyb#0-!AV4t=R6=2NU)=Tc*_$Yo|t2d->l2J?Y+PA-MV`p?f!bNwQJR?nl<Nd{x0J;1}14J?R<^RQ#`22R2`W+!x3{QY*Zod<b$Pt8&H2yn2LfEE^vz~jKDI<`3-rWGl+}&925w3&KB_LeBB+=)Z7kGm*NKlbvBM-H(`8g&DJ7Ey{*ay`$XnmOO3r>4zT$9uT$r^BzUwvQ{li*JCrwMG|gOg*Xd$6R?kqRvXFP~itJH)ta;Q*d=zuJ5>_7&g>3YUvF=1|beL<alIY1BVpM%12;dXLP@I5^IZPbSQbfMcNhyLoldcGDMZH#O0UPL8U5J(1-|B?{QWG_k_OFG_q1*Aku{r<x=(jyU94_0twgz;yCx8_{1QMhN@QB^rDVm7=orIY}_CY>f5!n*LzVoY9#dJL7kWg)b&;2b5MPiKsZx9aIEcE8vJ3fQ}Ul$AV>knM~`IvnC&bEwH4Sl8Txd3p+cROQ=x0#L#O}KL?fMwV4rm|i}DtddjGcZ;@_Tvcc=U0f%Bev#SJl++hRPV&*wsZ7E>C8pH?gNOfb5ObRehD7eY;^7ec{q8gc@S2A^rL~nyHFT-A`DLtR;JsN2YZ$}X$^pP?85NDUMdU(09(d=!JUEOX*(D<h(};};G8B_LH)bpb>_NPXRL|=M=-pG{kKldJ<Y{R!0ri^fa_S%&HLRle&yX@6&7PLpvbd_t8j%`J)rCnC{#`Nh;zDlwCzJ`IZrX|BdP~9r5@0p)B`M3o{QqSB8nF&{60X6B@ddS>EcObG~8vgU+@Xs(OmPGF5aQ&;{CZZ)cc2kQCf;iKEEsk{NI`o@aOmM$R;iG%Om4K-1B@CLTw!2z3uX?956v2tQlI+YjEwy8=f<oepTYaTMU%>w>p){?SYS<u?8;^#z-o-yTaTb@ut^D)^-y84#fab_*2o-I>=FAW{|SCYxY)Peo%W;NPDU5l6s$Cy;Jx0T`>Ilolxjldpi|<ALv#dii>=UR29I%2WdZ-yZalj<1?*cpU<p;Y(1N+K2sjc<dkdfsyUqh)Mr{zkoLr9+6?Q#qv>x%d?ZU}8(?tonU2Wyvq280J`>R#w0<GcX9`C?Q&GoGt{zP5;4?)vmY9}~HfOb$rc+P`g?8x-;_@OCeTm3mLH}lwdd6HUsplJ6RPG&@v(N82^&J0=aohj&?4DmX{AQA{*q@t98<sy90Q;#q4MCVBtBeSH8jBzWl}1gBVSNlaP1s2d<)tix-%JW0Lh2NeYa%SN^_dz^q!O?nF0hYhS0YqaNzJZ1vRMl_d7a|0d&sRfy8isvJ-mQ?mo;!eux2cmW?!-jt4X00`WJj?c>=Cra(DmkTOUyXwC02AguFUCuEdwD3p#5K37-$J3y+Mk3AbvPvq5PD;#98<ja1wgz19_6v$_;m798N(23SI`KHNGkW7_sx8{@VzjFUA;MU%RQ(g<aSOZQwJZ`<V{UH?V(pP_MCUFZ)S^aE2D6|G=}Ui7hpxq}iaa6>_B9z!4Q&G;pXwq_3-k_P%~KJ2C%B7VHH<Yut+ytoi=y`Wufar#IX!_0dpE)mGP=IOmExOZ$DM7>D}HhX;9V6fts@Gc>&-h$zr4qAS*vbIJqzGs-&ol3q-nL0N15>e|BU|_ByTR>#dHekkPM?WrkBS^t<hC8Ef#(Ob{x=4HktSOftUnJwRTO44^qmhr8er?S_2q8xuBE6Q`$L%o67NJnUF%%PlFbX<2F$u#|W{m`mx9BKxT=<3Qx8K<M%A?V7O)uvt>fqM(MF@4+7<hUi@bpSZ)e$+})xs8(P=pTsh?!>eH!0rE(9-$;kSd76Nu&BYG^Qa2pz3Np!AZl#W1TjZuC&rVW{qi%kj1zVwwcSYGn>bbYS0u+sGlh{!d-DA$R!<QBujdPr8gxnsw(T$TV#hU^cQFjnHBIwy>-RORU1dnE`Q;FUi~Fk|8xaSmPFAu)I}^kp;WLnc4kxa5VNImgE%jvMNrH{3teNa6m)=>7qzx3>XP7Pl3}924Z@-Z)CwppZY$_2JAw@5Kjx64rp|CIn#}xH$Uqp+g=&4?8$FPOZb1OCVCpxopV(K%Q~@ijm^8#yEWHttObq_}Rmm1FP}GacUeoK$x3$a9f5qsZ{rQfr6#oi;(=jH+ziZ^ImrkGJw{Ja}(({edpJA^gZvO_C`aNfvOmn(-2w?7|600((M^%L9H!K?6Wcu>?2SEi4kQZZkX+32jKlnUMOS;Be&kLqg?8Sc<{J$`(t#!=NNS`OhK61q-E3Y9zL!+AAt3F%rpRGQvy%0zZ6C!zdcDInS$-jT63jIAe2lBV%mHhFRLmrfB!2#dC4O~sCY=wtCD|P(S_anx@;h8Yc62q%4M#7bS4ppb@8yt|S`1H2=#Jqf$?qCkqb@=2K?w;EQxSxb-?C-ECep+GY3!HO#M--eFNtXO@K6*;6fBCLz{a@R1P#5RR{n=mqVqWh5a$4>$okv5(KQey}F_C%EKMqCz$lo6+_dj0icdYd<JZ$@yMKEnz>ql6h@1nt0IaK-EhEc2+JOtEoi3}6#)8f9j%KjInvfs`t`&8Tjx&-AU?_XUm>n8%m^WyJIP5)t1({D>nzh#Vqg8t&9lpi0f;{$~pe-7V=`Ey#kH*GJEZ+fI^?`I|ZUM2f(sMp(0@u8IL|HUW4$nyw&$3=4X#2*-sNuFr^9SxVKfyl#<<AJ7P)-j|!@3xvam<SIy$UPF9i4;OYy25`9i9y`-1C1esl-8cQP5#?z7sz|&5;FC@{<=iYX_5Tr4mlLZ+y=WG$^k2My?4x~r@KLrkCzv*x+9eMn7z2c_91L}yu&+)`v3MD>rtJ!O0(WV_)KV-xZ0zt237P|VB2i4*itG<0$&<bfi0uMRA1^&t+?w?8dUpflVOQQRCzn?PK7T@o9NuMJGD`Fs^Xs+Bg71GX?a=39_$j4P6%5TYrk0L{SC{$v+5#Dl@#5;_fT8$rG>|qcaWgc%;BJ3YU=Nnj{U^jaA8($i9&K}F0h+1y!Xb{zyD5Ql?gj%9(B-2orP60yKUux&V27PE&4>F$RYRB+5o5RymD+=8zbzRw&*iwaNMQOcScqcZfZ(7SSh$3q;6(>B=fTI>vieVlV6&T<qS1Ru&1|Vmi6jW*h{>YO<qqm3(2e!xSAD$T6Gt+Zom}Pr98kO9Mz6#dBC64lKYA?73N*pgRP%UPght`-}?0Yv(@ipPs-H;aarD7cPRbsv=OY>fV0Wt91-OCxZ99&FN*Rh#Gtq#JEK+DhwcuOZkKOmuiQ~k1i4hM!qZ~+Sm&PuxQeP{O~6%$)I1(qp%As$0g(tZ><@W9?)`=t{2`{!W`DuKewF7<fFF(Lk7T0XM*w76g-BGHUeMru(TP#b$V0)v*7}c7kao4gfl#%#Ow7>BXwi|7<2ebK!$ks~YmfLs0RN;AY-RMLBD(W*RI^jrbTHz+K*Er}|L@;RfAh#P^W^^Kd?V?kzquRwo7+op66<fChwB6+O(OQF{^qe8ptLwMWk2h34oDkMqxV2HD+Tajq?MTk@a&F0Q#ovArU3z>Zefh=J6A8pz@A^~>M)7zyJ7`$L>P_DnbirD`23`&InR2OtDIFqhB_hEd_?Wcv(cG;Cz3xwF@G{jL_Eqr@l;3cp$aRA-=&YMaF40HA!?_;wE~c;q40ZlRyx~ZriOH%7mq+K*?X(P7Fj{hF1WNu;_Z$BSwgwRV1^Hb@51W}zQ=mNr2m`+<2*KT2~{n1?ks5bzc5wF?6-{-pN^-()BczXSRc=`eou11{1tbuKx+Aodt|(@f35O#U|ena!q`jd`QNU7i!N9G`56`_w^&yV7!pbhR}s|EpmNph3P{y*7Y^A5I}DSo`G{EH98zpeh&tOhBr&3x7^}3w`#I3*Z+IWvz}DP30S#UVacUsJd@FbPmm7>(OLGJYn!v<}ga4c-<;N_J)N6h_F%k<JoIJDZ#!@J4RH7prTU5sIU69;G0x@n3<%vtxsRA<_I2Z%Js2K8Q=M0>XOus7UvtoY*6+`pHA(vyY%%cS*-v6U2pYeSl9l&$=hL8^4B&&rl9`O$DTq9%{@Z6QjzaI5M*8T(ycfvVDiZvHa)NTTQV6Lzpxv?h1SWFIwBTO7Ur>PxtPaz^A-q;)1f!H{?I42U<L_MR+`g%L$*7BH))ycQCWdonUI>i>A1A2DSco*Z`htTun;(uNJrn4yRdsU7|Tk+rLe|JSAuqqICh+*>zzX8UL^ofR_?x%~YmLee?kpJ0a>j11_5S28D6FNA$7{tbSU0p1-epk><`BUV-@Y=Kq7z<A6PX9$kmUdRy@{(?%*m0{ua!hW<fnnRSXsFHwah#J!5DO)rr{t4WxYbEm2U89YTU=}LmNqUmQ7FZXX6d*kTAhzhngFpVHA>}xT<VBKgNbPRk8wtVk~!yL15kYOOQQV1TCy>QcxF|})Q(m|YK>#sV&s~Ld}01eT9DC~Wfy=w7o;wRzY>)@B1lEz+iXfl7Zmx5Nt2&MN~+ur`%K~X{e$<?;EjUGb4**?J#N>0Rj7t87&WB;qBMIa77eo5QJuIYJ}VY24mhrgOT^EhT$;pY0)pJKtE6gAHD_?Y6tPJ~RC#zo{bDr)ZBEE8%$rh#Avhg3ZoXPV>mb54&hy>is67+7*?tJLGyhigd#?XBX55ZU$l<o?eip;LVfJwQKsKv@ZC@Q3UQc7=`r4J+0=UAryp^^>r6`Y$(Ka)B!vVomcoM3>@Cfr6KvP9HF2}o)eh5CYL)C~5Elg5A{tn)3_O|%UE#%^n`61n)^dLHFuY8pEpXNW^!`bn=s+|*N)PoZ`fEhe-Ga?6a6q_~AiCfDzyhDw=UE?m2dU{moIsmR|w6mlWPIuryN6GYtkDc}f72*E}9%R`O;6WV59U-*la`&EP@B=O*f``VrgZ|{wPzLvkz38vP(`B)*p+^-FsRma~x<Z9jV@8_m#3dDhU}(frz&aVh7o{d_Ekmu*<C{2)<z-o&Rv>DnLD~YA+-hcEw84lAR43Fn-U_J$chIpbKxrT0eWWDg)u9v^KD_e2j-}A;xuLn~kDv$&!kGyq&ATj=ep-58QXCeI2$C<8V}i5WnTp=n%TQDuoOQUMF7C%KnlSN?YB}?h@Eto+Ocgqb7xS*4(fJn%;R1CUP*5=#0WY%?;la(%Y(mZymRabS<LepD?Cs1Nawmpb8f?33RdYq@<qJdn>`@MK(atWfhm-ACi3p$n`KNNo98h!&GWcQ}{G>{*05^>l57rf&KnoR-LLdQNgYXzxltb?~ZQ+yQs>>egb~}POurmUjiFkB>kC$scza5O1`buF+@)pqV`H=uua)FH%%eXd}F}@C{KqZbl|Hr$^_^Noovh)24PNyi*yjA|gqVwNg%TEbym*;ZTcNHT-gs^Oi2{mH2z$Pl}+Mg>;<f<YwLtT2X^M=p?=Uy`!?$#*XN4nqjkqv+4&KjBnD^+Q9I`NYt6JU&7(M(CBfTBC!{F+B6Xu;mN0uDi*heau4P?D$U5WgZLaic{;>`lYY)x2v^q#;?RMM~yuQTLj`Hn$qSO!W1X<xQ4vDJtc0v|`0g#I9W{$D>IcW{TW?uAPBLK?=LRWKPY-$!2*O1!m()h~$Q^a|7S%@Qrry`mR_S(o$3s)_8=ugl1NzFBcY#uf7_UKBAkg%*rgI0Ch6WbTn+(w-Q$`w93ASmz-*ajBgf`<cko!Icx3IhVt6V!!6gqLT?)Eg-)1FQgCO!Xn2#+g)hn}!!L`$k~&u%>yG(2yeawxX&Km8OGd>TR%&|J;d8YP`f`{yDop^{zHz{fRN+)_MT$;T7(oi*hrf|M_&T}t)7<}CCV*}n@@f%FM}QAOl=Hy#A=V&@g1t-Zrc)*xelT)3VX<YOW5K~-+3ksT&c48n(sfSI=%`1UKhu*SFBXLJUYP^BPHaUEYOd2^UZr`Q1d<#*g+06lZaO|OeY4@&fZx6$PKB_JBDe%7M@<Az;DgHMvt~{C`}E`Fl)WNAUcgM(v0u(sBeGT-p670Z0;4Nf`%bX;hWLd<zn?%(dhvdPh{RE8flMAO_p)7xqAe7BsP&Cy>E*yPhB2d*zOQsr`oU!|w!jYQ5j<MDIpOCk-3TyWwfGXSQS|~BnkWUGATg3L=5mFlFHGRsPVB&I_Gqi@?~R`?iDch;+gLQqkBF_YuCXC$gINtrb_!}WwRfEN#MTt2OtmlMWdQdeGO#Kld2DqkfG(N!m3%{{y^)0C`vaw)oL~?v)xIwNg|e#BXCTr92M>x$ts5`Q)_E}Ruh8<~;~j&wRw2J>CRw=eol;A7k7kC#c;iDh-+ss}=8G|^i-=S#W97rtI>@zgjm!sAmsX3gr)g?lX);i(>G2X9$c;2sVYAI(u!$0DJXLRUx{}7;iM;(;s3<d_Y*$^rG!Ati`{hfvBb4A#qs?=&z~CT=^bU*D`2zo2OM7I0@YR#MB5p6FIyTsZ#<eJ;DV9v4TGoLr5niQeq{+_rL+p$Sll>5m)frkJ^+PPDe9EOIVu^Ri27)$HvR;M;#h21UO1+7#2Zzsb4=MZvc119$kzF~u4Au{^^3>CkJfl!n+d^CEL|e&#D_R>wt11%hIKQiKQ!dCynJ=&7?AyQr1_7nN&~V(FWZ?|JuoPzg9VQ$8i4Tfn=i|#9JNeolo&&mb6VP4WT4=}5lkFrU+o6<@Li^|Q?X;(SJJdC+&r$C5Dkz2%Bp$PPfC~zb7l#<^3?wfa-;PipPeSF@Lgm$^$8Ln=;hbMuMHlB>k#DCf*gWb1<>yFj9*;42UNDtck-nnAK0nqeR1fu&V3`n404@@{2HR^-VSDOa!!z`U?1ed{i0AmdKrTUU3Uz!wgs-qpx~jlhtd31YA29(U;fWs(qOYI|HXQttz7FRA{%sSpp~ur`s{G8|H<d3_(Ov~PfN^127NW;tRLPXJla8XH*5IO8)*%3uw-E1yH--|-uNq?(nNjJS<>_n8?ux()EQp3kg0|BpD7X+uy#ttFRSnoRBU}pwScK4sa5(}Fd{g7&>u4|xNzvg-8>sv>nz=ZkNi44v^)sQEUBi{((v4z5uz-DE#m+o^%k(U&j=c+@w^l|PVhq?Z`k`T6a6NKnH%aYmSiwu$@%`Rh;I<l5%00XSgZzuM_AT!F{~;o!jZ2^L$sgdy#e*YR(WqOv^GFN#>nbl-uPiYO(~t-2iB)*8=m?;g1YC+L=RhIsEja0|)=jt$rSTXNR8k|rpSI%XVrE!v2S_#Hv!Ch!ad#p#DsfRN@-KNePr=wbO6#e55*>pmT-V-+Prj}QieWzSB%DE*Dqii3_H`{m9j!G5zv5O>2Ww5jMXX_r`{G$+PtV8nBv)3$70M=+dIBJI7lVR8Yp1v~A!B;q);i>vZE_q{8k&HOqjhy_X{z`KZ>u_Wg)7Osb$SD|p?JSnN5=<28yX62Xg8-wnwF!|d5R=fqyku~J3rtCnL~0aDPk$#P#81}m8TX5qw+*HGF6_gu!V-l*h1^~&X4q0AFq?hh%96J8s=AC>uA8L$4sR>JMN51mDtnBakg07O%8R^DTfrRGIv(!Ms11ALhvT&V^mu{=hiYxN|saXiRkJAM~*8a6oJRIoMh-5y8a%Ug_-~??u*i%W6z;rZEJ3qAN%pMfENa~wIGdBO%wlWxf;@oEz_D~bt263ePK-S<%xGQ)ZT}zU-`F|v7_PB=H#YFP7Vuliq&c8$781d@<<lsm_2mUYBG$2R})cCT3IEmlDP2Y2CW3FZQ57E`?>{DIep{5d6NyNTM=cU&L6eKv}T7Rn`SZ5sP!9(M@>W9DP3nju-)g66S37U0M%1j6OQH$nhDut%3RTcLJN4NWL5KcA6pN*;1Ub?2pgGi=qr8DaRbb=!c!%J9y~MS(5EXcl!O-3NipteAs89(N?}F+02fi|3HXw7R|X3#6w=ye1`a2w-K3cm(>MlWD>SlBlXadH@SJk~>SM7lrKx412UiXpQKJz<w?Y+Fb}OZal2umVK`OHR)0SpcxrYv;L&a!v1N`b6AS%~(w&t~8=O&@TK&qZArE-;<q=#h25iv;-Q6WHeLQEo+jXX^nH`P&5=R{?2vm|a3Moc_E`=MM*%!`2@PKnC1mE15zk>}t}9B0gb_E5n9!C9E38G134RD~IbzCM!MKw4VZ^0%K%n(>5(^C;0+ljH2?u#6RqueS`*S)ws^=kr<Bk8q6%ysiG<Yjk7LAeYCCV?m5#;tr$l;07qm8abmhNS$zvH8b9^0%#df7rtsGic(TYk^L?LBVu?1aG{48G0{_5>^=nf%J5&lPVVv2<mx5Ua*f4~Y8ua*U&-c|6GQQ4I=N6^6ww&7(T`0orCofyN@NGIx}#|YZvrh1fWc1~S=JNnoIq@W_OU!_H3>k~iY+9$b~=(=&?83T#O6^Uvb!nss9~E}T{sa_b<D_Oz$oU$K%gjX12^Qh(U#FtyX-ibolJrpU-a8&c#uA#chMP8z~2=fq|aG5;=Fk9I4n{C1})-yY#_agF#tq6g_8LIVtk}??tRIy5iTAUdwKz0R1h?DyGm%lUThw`?~fHhLP5{Vo)fsvYMls<4kd^neBry55i|{y0;#~G^u3;>OdDns76k+Uso)C-E6j98*%Z9V^Pv1!D4zW1_)<yPT1iO-%`j;297Nn?uu`3HZ5PbA<4*8<srB$W_trB>je4w)o{f~GdvbS5h3u<MHKau>1?vCwyQOTI^R@Uw))I}W#Scs^r8hEdjibe%aI|=FNQ4<R3wG(k9^uu1--vo^B*77Qvhd&ti)K7HrTbk<X+Dys#l~!Je%OX7)kGh3;ArUzM@xOe(E^;@pZs9BhNvRCo@%5%LN{c?OwZ30Q70qa5M|M<2wrMMOTolgMDj0^D@H?Wl9|~m?rnt(Bf37vFEruQK(as-LyJ$UB8ii~`KR8Zrx_miG|NttXWLSn&D7H@!lA8UELz)Rq*QU12(K`}oe1N^qT3hex_vS~M?`q$Z>~=j`-;EmjSDYPvo`LaGODKBP80&mr*h#Tn)&A+Cn4=PV;^9`?(WU1g5ctT)8M}PR8$-f@ZIxM+1^(V62q<h5AQ1qg@?O6Y2yOSG<p;tFittp3nW+iR6XS(p9=49AJFUZiF(TJ0Uuq^!tVBn?7ohdVR4T|ED{ud@Aid3CfzfWsi$#gt#DiZb+<QB;2}OmsQPD~fyVQp5g<?7;tm6fyxe^ynt1F!w?wmOQ@gR{Ub^KKesLG5tG@Sr4IBtM8W8ND0Hi&xv}onMhO7&S)<U;pY|ZVDMKQoy+yPwg0Yu6H6L*JwWN8&2_(9*x2OmHx?ipDioyf<v7B8M4gDZar9|ql$efAm}y8y3P$q;^k1G<&p14aTW$G8BV1k#6Ur&GrF)^;dgm=9-8=YLxLsSsZU|0&1d0e&HBXlv39-q6~2%BZlZP8h-lO0S6u7@Rdhew8w_e#1mYA|S{?BtU{~bjJv=DcfdVjgf)^%z)8KCh~;i5dqYbs1+Ll!$DzqM{=0pg#R=AWGLQ5TG1y)z08*FD{k^&yjgf-nBq#zlN;C8(Ofn-^XGC0Ht0JO$WMI4do7zAezrCc1;|_giBuVm%|!;w^P)$unGl0dx!^~9srBUd8$czSx~h|9VnuJ2t?#l8UCq3i)5)0%UxXr%Q?;zPgjU#yg6_b{gK=;5EQGQyt-pp}zZy_H)4DqYGaOs@rbHIOEy82geOoD~z_zM+9>F4r35J0iXnSnerQAt=E6n?mqYpyPgGG<%Hda$bJ0LL8apWU}Fbi~{k&*UGf+#)HRu+a15M=(WDuL8Th$dK*7g$<d=i;iw3oTY`Jfc6{PjU*C`t6N0edIy?`DfX^un*Ll;W*KZpvWHJBzGVpfhA4{m0z$dH>{=j&Nn1*&R!HCZLMD|!}<pOlSwOt{z$Vza|l{A5nzYD^PApu(Louz@(*pcU}4>5pM}K~IhUY$k)!5+Koacr!JOotB}^hj5XpV(Ho)BVXhiDlvoO5bXfm+(dv>tY;u&LFVS(OVR@HeKj_?BsZGJ92&Nb>Xf=msxc{5x0-@S`I^M(d(;;xT6+Vb0{ZA}WcQL!t*wtPxbb<7G!AhMKPCGsQbh?|-kw(x@5Qad^p^b);daqOE(`KX@hXp4()C9+Fqu2Wt5%xi09%HMrc6}d`bov-ko1oNXTC}0JQlUBV9Fux6#Vk^~A!^k?MWs}v8g%-<^SKdfRqT#{89om%GX7wmVsw5WMZE$AiVLumDp<?^xs~Nsyo0;9AHhbU_xLA$iRl;EQq}uJw3&!c!Yc~}_?zL_eP{=~&&#s;PiQ`ObJL()KGX1nv*9l7^0s=GeCC!?rLsR&lcZPf<HlOG_6nXXZ8bvYKSzAx7$sTQ)0}J$?WF>9|=8ydG5(uiZ#@bQhnr#RmvZdv`t3)4-KStyo0!!g3m_5Yu*z$oyK^hs4AlnTwUi|qlKRd$9R_Nwxx8d>`t%l*&%D9Win+%7V(4>aj3>r6Ffg|^6X)H{P>Jsa=;qgvFG=zq0I<bz;im|(_1Z%C&>U*{n)M?){C?9$@7S?4cc9<2nr9?Zjy%)B|Y~36q%XAd0m%du$2!HB>0?oBKraA@9IRiMtRv78ZQ=xNd0-aMIP-Gn_fjxuJId83f7I;p$>tcb<#R8p+SGnurz+LB{Ab=3j<8iSdWwKf7QMpK8$JrIalS%AO5OeVaF&7JB4sCmL&>S!3h{ujRh7&5g?@i%yb1J*`F)F*Wm^fE7MciYYcKg@mw2Q}_c1|FkF9{I;AV6@x@wC0{Ihr^Z>QoB>1SfTb<9%%-LU-%NUJ!m_3A7Ut9Dkv9z@7@uzM55o`h3YCdtqmUZ}K{9&J_#f`4`n2U#d^dDSf*%$8b!k7tqTCA%2`RPnSNd!9*^}0zD{%mMw2)B~cdty|>N4Ko^}L>RVSh#K^tC$<5uwAVX3mSg<RmL_%I&g;;4(`4IncUY$!4?fYs`n%>}mCX9!b=sU!>n`q5&%Mjc^9mRg4$OvK)?3@ouB(4JmQk)ov;fpR=@`3p@j}3<{F%;ZeW2a74g5~m>j6q&9ZG#{(LePVyglE9V1<lpndGaA-Ge;CAFE5tvQCbKjh&=T=-7WVqXYz!?aW;l!!I7P~cnh->@=Hr{K1FjhRh9UPGQ(G*lCF|a-g#lQvjkW{0m6g;s|oUYjw$iv9OY?62#`NwkbxgGW5sKoa31Gb@#-U1JZ3Z6f^MrNPZm$qb7~d&rDgI4iSZb8hKcLch`h^0M};+zpFPpdq2_928G6bZ;|A84ywR|&ALfI`g60RR0GFiJrqVf!ktwDgwX)t5hvOf<Q^vN}7OK30zih3y-<?7*spxY|5E9hHYATXSE|l(7O<NX}C!owTWFeKl*QKHaD7@Ho=BAPcpL2>nRR++IF{#W}gJS~9Ew1g<%(UFYWj(+_x-t*NEsW_vYIG5rxvyr@mG%2&G&;B^f-)i47}J)&H>I1rL74?J(t}PdtoV%NcB5=VLLtL$Mgy#sA5S!#*nzSIM2k5Q-FYI@rym(AOb-(57U4m)LG>9TMS-qARwD#kG$jX_*F#~YsF`uLKUr&T<xT$pX+S-H6HBF$eN{-j65A<5qeKsDC0@=Pg{{5ivcrTO!o`u0!54&;<Q6_x`>k|~Ngrsv<K9?4h)pUz(7cP!qwyk!(udiKnOXp5FO;%E9n<4<!h?=TO*eo<$KOej?uL$SwiC5ulQeaMr+xf!3O3c2ZO*K5bi{#GLyfzWmj((PX*cX!g2^`FIdACkMLr0{9y72hJz}{j<2ju(5)!(HORi-<?Ne9h_pJY$h{8N$;j4<Zb#|$K@+ozJ#({D`U&~2uPcXz^9Xn_~d-J8?F@8|}fZKdf@#SI&;RJGzLUGE^w(OXAQ_j>6;<@@k>Me?J7orG^Ujr+QrY^w`QI8v8?*I%iv{<&pX}ST2I4c_v>X_|EuzhIfW2qBh*Iv$2DNCeM2K*4NZAr%fAjJKkoD<>?KD2B~dZXDCcOjcHHX^E3Dyj?d&1e9)i3Y%#B+A+5!{jZW{X``ICO@vU9mb=!!-*I`9Fr*X&O_itper?`Qofw30?axOb-(C|KUC*(Dm<Q~;_$c{|47?mTiOoq)OMJ}Rdv#H=vb$Fe$V0lD9iF;_8I=8w<dR5(1>qe@pR<NyDEA*Aptc8(DNZ2`cLHxpXbi=6Ye}8tjIJ3a`osApAkT{<`Z3mcfnn5Q<{>122$@v#c50q)<Z-$;W=ki;heD#3~q8uJ^CZ@Y~yQT|D~9|W<uJ%Q7u?1h*$nZ6!LqPLH?bw8Pa1qW3Q_nYCNP^dMN#ndFFOKffK#8dB#xsBBHB%267Lj(~q5mkj4l`w2MX4sma8t(rYmP{MnkAwi<lD#(A}cZ@8cl$+mT^&ch_A24O1RXsiTH{@l5Jo;*vZD%zeP4v`h(f*FQKGM;?XxrYTaevl%=FFiYI$xLFtp`tSDFe(%lxDql3ntbTMm*lOPSMq6j$K7)SAQvMHa2y+&u%>zeHhKhF2II^hL7S~$9&X3<V(c+zkzl}=;&`e;F!LC#kdxO-(<|V_%-a96)$h8xb(<fev1r>9Jm$;4`LLfg>{S22P4l7ZZb0yig-smj`mQ=KE$AQcKwc46mH(P=y1(Z(m#uWt*~kNE9s+ulI?GfFp%c+I%Nj4`?VPmgz5oc=`+J@oI4u~9yKK7mLlPC=wb&zliG{(-xZCBIA_l@=p~+ig>j@8_>aPD`Q&~xiy*<&&WcJI^`!6qF@8!#QzU`MUBm6SLFC+Z&@@0fy=cRumFa5JWo1XL6^fs>fE5Ce4{=>^GeTQS4-rRSkpX9Oi&;D$@`tn(y{mB_v@4nJY|At<sC%<Gjt5I0$<@Boba`>xz#>?67?n%E#>H38t@E4x)Zx!9SH)Hvwe)_4D9Y6E0;bB54SCyB{iP$fNMa2z2!)HgT|0CY}fi+bi9Jgi3OlmBY?(~HSoYGc=T#zrgK|zPKzbHBIR5iau$RTwZFsJSfrYS;I6Ob=bH9<W2<@XQ_AYeb%I95d!*XBRglU3>&_U5f<+Vs*sI5cn_efHAJfsI}IV&moM&1C^%^Zb<`?`U$QDmHdgfs<soDZ8XN`IH+!RU~z+?^|uaVoO2yJS(j#<gvm#`G^~befkurgD|_VAgu(ui}ChtNL{(3@*paS<GE^lIyx*)$IVugy)2hBzYDP)RcgK-wG5}1J$q-oyOaCkNrneBc?9An7A>!F`A#Q;JDv<9Tk(9_csKi?zEMTzaseovBa7eKEJZ0P+VA>tx=wGu4DXa;w-x6iyQjuCgS~@q36m@2%h|u)4zT|H@{ax`$l?5-u77a&>zR+Ylk>aBK6~~6H$VCDO&LP}_)gvBOM3L0zv3-V5AbIWIQmo!=Z4)q<=)2w&i|EzKmF|R%cUuF?oB_iY|jq!_Kx$j6CRyyIF)~``?~bdtFqPTN`~X7M?T}s@%VtVgEl*ZudW<pNrN&JRhg)^-si*kghwFcLwVNj<li}OxGy|d^ODo=KbcbL&9L6A>*rA3gpp4vo##`U08ZWr-;Llm{yc>JERE6($R1`W_VyITPKcf$?4lNIm-!NA`1Q6FdsnASHz!5Q_yJHS#lP?j_MC690H3E=AdA8+wbx<@cS0Vq;(n(D4Ql7cp2Mc<O`(!8p$l;IfntVWFQd+B_YxwaVnm@qcrap`;P-ywiaAxs2I?G<;0$gP3S<F2{9<pACU4K<u>#lxspI?Nn0^7u1HjF#DR(b&Eb$%K#h?TJ&d?EsVb$}N1ppru08p64neQa^gC{R_z;tH{46OmKL8GHbZO?pHiQly?%mq=k*}wHcuXd6S4h!CWwFUn~_O!g_Q<P}c`8D5g&HHezd8M8=ucQfenxFNrOqy5DkzF}zl&D0l9>$w1sPryKoAS#-(ege`z%RcsRv?2cp66eBHRoSSr~FF<CANivDV|a=iSEuD5fl3Uj#-$B3gDC;sI-boDXd}0Y+OtY?ejT0rdS9iq@t77=sOV0XQWU=xC!D36nr8Pgthe|&%qk<D`6CmshO1g0GH6Bs)OJMF8<QHc?c5{tU37U97mHL#k85eD^y>`)I^*z$(m+QL#TT{P#7LP5aLF~N6?(mVuf?hAq~%A3+1r!A>2OU2{7TIGeddX8rkg$cs+rC@5gWWOY5}F?9(UE=m{8S!SQqG&OL{2_8b5kJbDyHCC5jxETUAy(+HFGP;)(W!s$+V%6?G&O7$0A{WHXewLt!{oeZaOH=xzQH>_gXJ4y}U>T7n&v#Ee84uoN+8eBN)0SZfsWV9eN72q~;htOatwoYr(8V{V%RDTtWnk-Tz>|<01LX8Foe45|6jSHjsj|AdlHhw2UGmL#G)xPqtdbEO5j}L$SzGov(EF|{gBG2AM3u7<EBoZW%eYFv#rxPvc7gkG<C^FtOp)HdK@*CTRAz%o2aPOod_U%C3;=LrFA$gQ1Zbylv$ZZmR{*8Lb3f0grypGG!SLvJ8!4)otRdpy_X8BLe#5PF4$Fmy{9!K7@JCiMgYr*G9WhTt7t(b26YS&UCE3mV=uR6Zm*-P9_4{Pt&68wSP&;LUgPK?FG2QC(77u(J+Ne&m)F<SY<p6^GnQyeO^sK!8!|BWS-n9p>BU??bLTE=r^;@z+_Dy`W&fv!t%YSh5wf*EpwRf`9;sAP~r{HLx%(m!+6XLCsU58fsu{mZMWIN!XYiWANt(R(7%v%S2ehofBG6Ts-#^l-X!dN|??TAq`{=>}9fsXONl{$wO{QVSj7>G4{Rf3;I*#8qLOwjk6y8s<}w`cxh#jq*6S+9RC$Cl_$)=o05RY^nlP7yh@o09XgA`WUbtCxG=<fOYRhH71bqqnPzHVAdCK-hbR+>;K1FgRNg{;jFc5er3%1rZYK}wtWP!UL-W8WJpHBGJw>ZsxToHgnF7H)Jc*&<z%Vl<fx^Jes?`U)lZmN;?RO@-DA}tr_>g-dN@L>PkCEZUn26HU0P}ka_W>5LY-axn#KH7OX9r&q|OQ+SE%)M4v}7ePUigrdD8pO@worxowgm*D$fYKlIi)RuSnnpzxSBH%RQaItEEK4c>*u%udG85HJmf{F4nmUfmg$aEIo8Kl1^n`#%7A9Oiw@4d|{I@#oQ4%F5Dn@D=2(a_kKPbn=rlF8X=(}N;h!U!VO}qyYr>U1rCZ5=<uqhQ?i{-$$%VGEz)VrJWN=<L|(*4`PS#-@4vhGsGQ>wp<EqGN6vgcw(OT|C-bo*Ly>>ReEh0}a`b;}N|F|KAe3uQ2<5y;tyF`qX6^1}N*aOVj9HFbc^vqz=mIUDW-%L*zpBAEyS=8ZG=zO5CcmY7+e{<ylO~?_d=rlu%AhH^sA3^)btVK`%0ziK{5-US6lQ!M6lMt&+Ai+dls<@_FUb6OLm`-^h`($U-!aB{Ktkw%ec5_07CGeHvU4;tMx#hs3AnP?W^aZKD1vnieke@!MKpp{<f3}hCX1qRg?3BD?Ug#|Q3vzkEJ#Kt(Pe2iw~Ulp8kgwrb=rJz?PWg13~Z;(o;%xvz?hxa?urzu;tOGlV68|aM_)V)xqucgCF|I#+31E5Y>|uu@$TQXRhl3B&pcVN<5E^+s@PGDS&@=+M(|{bk=h+E&S><0Sf3q3MK@WZ`I1*EEO3dQsX5IOCXQaL)Rb!_M!-Sn$!r|pC2>)akO$rY^Dx%kpWSNHfUV)vGdVm`V>^Wn3sb@gO3UcNsEaHjP)v<B7+X$|4#R{m8w5W1#y!w1L{hM$mvgtukG%$`r)!fs+<DFgD9LKJPQ_p$LCuZk4B?|}ds&C|k=`)loCP@+$hC&c*z;7WGX2=3#Yx2>UmO|#ZZg&X;78y2HsZtAbiS!y*PeRbQ+l6sK6hdqJQ1(+kNDhS=5TjYhufcUB|_=!`P;|hinmQU@_A`B6`y<aBjI!Z=Ii9n_GC8NQ`atXYoiu?BH1YlX_UP4$}m{XI!{lNQKdA!c(^c5*|aFLMg}*IkoZvi$PD3D6%taMqz&*0m9US?Y64VXk7S=s3>}{hX*IyfO%1qKl`LnV+e8}YMe=K<4GbvH^FU1o54JZV3RX)oGb!%LyoGf3V&}!RDIWeD_lxAeuC)>4$`4GpxE?P(`DUb7-%_bpJ)J8S`jG#>!L2Pwf}4uU3`pcjNoM#Aak}OAe&sxy+#a5>i)`7HbMZ|_(n&I&eMdSn)sB>L{aP3@veZT2>kcX}XCXh*K3P+?^aV+JWuf^4&k%YX9K`S@9`2^7&*V9><o*@&!91*Dku;hUp@YqWAc+QE_;2&CpA2WFL$Tpi<)J!M{-^ZjzS;y5_^aB6?S_#`P1^s~j7y$Gx22yQkCCKoF-lRvNa18(A|s|+JR-elkUWX$^b1(*z%~+{J`Oc8o^$)pjKtm_aT0!F4b)ggdGX{cs$>7t*-*RuEV~ETwQTb@_sFeo@<zRfNJF3R{}z{!=SSD#))IEtYO|#ZcI3!y&^`M}e!4iof10P)mZe6dF5}lJP>|!M9wdIK3fzNBA6so|Fmm_c{C9ck)3NmX>`N^%|8BWX*9kTmUeQgpX;2SnDKTWMRZeD*@QB}i#{SmD{%fxNW1OZNq*nvk$-@Clp!KMBM^27U=zs_GqC@k~;%!&mz+XXocaCz}RyF}P#C)KBkXc2zyC%mCHoaaT7YQk2;Vh+c<R?UQ6DMg!Cke}8RUD(b`bajI%E|4J0@`D)Y#3eR`k_CBmv>^-S%H}k8F}t4>0nvF!$1pnV7-R?TFZId+b&FzAQUI&z17;2(-U4gb5)<~#3XnydD@-#V;0URflj@dI*4kgwN2xKPXl#|3rLT=Bc%zIAuSy9=?pK@AbL%cAL-~E=V}-;JMQIqt|gmFD&fitZK(}YFfx-l<ws^i==L&ov!(}N{wHC|7|9b(jHPWanrQSzf~DQVN#uNq;;=4dF?#6~CilJ@GLCe(EWHy<p(wIoz?9C6EV>^FG4Pm@Vv>R$GWsuf;rCihh$<ciKj=2*cNAQ45iG0Axk=UxG2a^#TiZ^f?svZ?{;P}ZtshU==JLGz25fO;*F!-U)8xe}-&~%F{gQKBK<+xb;yx`IeuFf_OM4s6q$!fbvQ1Uqnk3{INU0Rg|DC9XdWgelo9(o_O1+assC$aWN>`z#J0j0{Tam+kx+f=Jn#{ndLOYAO@JaSyZsf<5ZCRfR1|&}`k9~{rU*669-i`#}MvJO8PQWBgBsyOJ{7A;yrU*L-7zIyqfr6x=(cz#vf#f)OgVo@?bq~<<H2kSKXL<i`Y{`l_Z}0+Q(TJ69J!*6G{>aBiRIRazxm4tAk_bcoub;503Jb}kN`6vdWybr1r&eDH^1{<1JTI+rnyPDQ>obJ-Zeryf;dcu4;+0UZD#WfAqP=N(W%(mjUWxyoP2M%DoljA>9Rj`$dD`mP%r#SZPU9BbGf_6q_VIOH1kR%*ZwbF0gfeu7Fx}84B4m3ya@m9!iK$mE=|D7&(4(Z$l8~Hq27%}F6kQYGMUc*#RK>Mu=;<NidZ=!}-Jf}L=)B}(R?!fit)FGmRs!Dy@fj69NvIML;Vr0V$s)Gg#9O+k2L9x~X|ikkVTXm&m2XN?qLhfT7PA5eHSr<{78zAB!)52DWRG5%vGy#-xym%W&9o>OaYP(mRjM&9zNlP5imoeE^oMC4k4iS$sYo2Y^o1v}xUv4dO!;4^e#e0@Xi#3y{^kzFyq!=bD;WH+twi3L4gdYVk|=khj?XR0wA=h!CAz~vZmS%fFPJ^A_t-J_LW+at$seLufdRs*J@&6{V5y2qv3QK=H>et7jdK9K?%^)pGE=ZDm_kM=jA_MJg?xnnZiMcfP}(`teONM=98m`PCJHmvmdhc3<6WQ4vmp%{Z!LPBGT$vFUe=LJS#VQX5WywrQ2?5Qx`MIE8s>Xz>{ygXTv4a2Dvf%7?_HG0NR)M6b18%rE|kb3Xt2^LQ*;%csJVp2kSY|h>f<U|Z5yJK`e(j|rY7yYbuAvtE(H~C6M?$qxJ@jcmO@!2YSvP_MSLPQI&(x$YPa>3+HH^+jHv&C9M3msE{tT8xtQ}l8anCMI|7s07og2<X}ty;Z-zjrO-cn~9BzIj_PhV}eL8DRH7IXC!eU-yJ3iyA)vDcI$ihQCkpQtWG262flZp6n$y0-phC#jA9PL9<`~sWlAmwBeQ>rk40bD{9T$_~}u-|r#_;V4#Eb`ppXWMYXzStJ$%b|IpG{6p=<v3~f+HRX;!t%UJ-VT$o_WL*^EN|W~VL7u3?&ptpr92jQ=XRy+!_@I%FAB_vuq*$&rEni_tEMg{Fx-1CZx-eA?CZA(a~`-QVQc8CO^Z~QCqkg7zW}^1Bd=GjTVRj#Yl&R7)Y%Tz$9cP`{nsLFK@Bazz$BgjlsbWV+J3?V9N$bjIV+GZS|)Wtooy;zYHI6!Ae8gt-7*$SJv(E9m4Taxzj7`i3GO8TxW&mmeXiaKC(f|9#s0y~$n2N>>DO%82WYW=C0c9c8aC$@kK0rV!|ALbCXuk(##I&GnE&cW-8TcZ#MXGjv3JzQQBFUM4M-9j8-miBF6L8okD>l%86}7w%YUgy^|wY+7|}0#&Z#g+A5-_Z$XQ}-<fA)Sgk|;!d%$|EWJ~_~sQ~g)0?3g%IC$o0mm^x1wUPhr#{^Py$zNzu?6?4_DR`O)X;Z_~s1{iuH3mx*T|>jVf0(!lgxAO#*K!jEOrkeScu}cQHhHQeQ5T3;QEGG+P*~hA`R&@Uhlpo_=BXRXK-h^iWL$eCIHr=(a`_{LJ^cGW8qUH6$rDV>zEth2>yjsQ7APat98Ju2CUDaD6TB?dP1;!EOKXZS!I}wJ*1lQ-J)7zg_~8s4n`5ZF#aJ@go7{vZV?ge7S<M7ap5is^inie;mtm@La!aFD7^6QJui+Q1{dtX@BL|Fm0MWPm3A#1dwiNO@qu_h~MYYG$gZvTpVd;Ie>}Bpr&B9h?Q|*Q)p$=$n>}{nEAc}OTsrl9zkrzdL7nzp>q(3(X(no{yPCZI&rux{Ltnto+^))kD%ZqWvKJJ;I-Qg=F5@shcb@RN!?yO&Trv~Rc^+#h5`qbg}16zN0dLT$tse9In&}-fcKWM}&>%&;USUVhyqT3FeqgtBsjR?_ij4glSNy5!}O+IiZWRkUo|5bImy1ZrHGr1&<ph&iBE_H0qcZOv`vZ$ukYm!C@=6W_XcTz>UgDLLFYqZ?puMa3M;v{!l+{!ICI8zVFt7vKY?p|%At-s$Ot-DlLnKCxXAJ)~j_5F5Kx8ZjqIj~r9>54z%hIxd5O4i^S_^sNaIY|zDdjE0tU%2HDtNy{&6bqu<ee8cIt;WdxQ|`yWG4r&a?D9WUdD!j0J9y5MlU(@smft&kgf7;`*^fWiRXyoSFc_HDn_}*2clp0HqvZ<p=NC`7VPE*<dcwil5I2~z_=@G}wcX+}f*s?#yHUqCJ~|qwx49;k1(1XJe`r3$68cUarC)kuDlt7h>NxkMLvf^;mYq4$x5bO*zLz!?I~<2pFP-PsI<$g3XKq1>;cN~d+6|j{Y{Q{9RwJ9`6)m-+^9=p0NymQ8%FpOF4;WBsb+tC?DC@7y#n(DH>p2IOK(pr@SY#=<V|st5o^xJnoR;fbto-_yo*m7c3MDhEJVm#jMl<P2(F{YGt)7FEwH|{Qit$(+Q&TRPQ5+nL&6x-$o{3->zH~!b9NzCNe5si^@5V`gAX@@j52|_i5+}pYz@@wMhaqaYH1M&6EC*m>a8rNqW1=a4r6om*G4qh6d16<}v<qO`m~yTwr5(FcObkoVsz(}A!f{uMv#u2SY^5=!VI<SC&<<FZ=`+GNLO;ra;^b(K8v9Y|Nk2;cgnpEpSwD(}DdAnlD1ZH`DgJ8IDnx9KyefRM1GP#ja`quS!mg4GGs*ImpHr(avr$*Zt`fc?oszdSNKn0&ZI@PEV}Y$3>&RD0mDn^V?0{#TN{GnTm#Q?KNyOwq@Et&iP&4xoO3&-Gl!GyYmS#GS8C3|V5S@yJxFl7{^9Vf@m|XFlPNn#ZXXuo2Fww!{#QQ>|^z}TJ@tgSx-!tQOE9_`?kXhk^y<;eFV0b|yB|25GBcG_dxH3Y5$Y`LG0V0q#zdR5&>k7Al=rQ25d9fB*FoEt__*DMx7V0HC<reAJcVt)E9c+g$<VlQ*4+b&H&w0&X4m_1&2rDS*R8&Ffc`=v?JKj!kTY_PAVT-+CgcC1yr#GuIGKYMywP`5fx4ExUIUAGnq)HM`(%=2j0Fg}PfZtqeK+~ePs{}(<k*IxH-W?2U%Yjj$fI5+=mIcXPS87Soneh+=wvN=ZiE&uu*b!PPa|ZHCv{4l`FTBvgOaI%FUd##L#<96rErKWU$VEiDr`{x{u?wKBh0q|UcCs4KmQ8x?Mu7L7{rca((v<AzP`=;nR||JDTq>2#eVlgY<2;uAI@0zX>SXMU8jECO&r0!eo|yWYLYV3agejIZSg@K|J0!rKQ!`sC`<1s;6!v|8Jpoqx+xS5yz<&2N`c%T+)%m7xY~IzZbsOKyO?68|Sskg9Of*h5ArgmGBWO|*i0eFckPA)J{OTzHhB!!gMCRuk?4m5;Ft)jg5=BGKq;^U)fIv49C`_ec;*K~sk)>%#j)S5fzk=b6$gvm1^e>29Y>9tT4Nv_p#<;73Ss_L?j>u?4)**8Ks>22$Af7P40>BhCP_X#Nb{t9iw&)OHSm)Ho$q!ayHDdoB>3$eY!QM$byHb}2)=FKONNP-`sdhuBIj&_Nam{&RE;zq%3;*MbuGhQL_42Q$b@1}?wPhk+UcTtgy(mh(jPQ$Q*NbM?i)Po0X4i{m*NbM?i)PnPoMzX%{rAo2bV&zk_$;)-E~$0R+mG_kojUiT$#XGlocIGM0@Afr>@d~pdQ?t#O*xOBN-BAFXgw~{<u8bI_0_17bR^Q1s+pix&9n7_6F(x-MalTDq|-GOeL9vJlU!AQS)nTxFqS_Sxne%)RAP&NT3N}(BLy2~@?8Egd9LZj6SZX2^nO&MIu_=tt59@ljxYXXgxNoH_R8@@I2FSny(J`BP`AtYj@^zwe=jphu9+TJZ&G8ADsfFdetOuk5*M*<l__!I397HhDwI<|j(Aoi*QR%-(p!}q<&35RM_0sxToJZ1mvXN4<jPB57tHTfMX4))I#!wr)zPQMU)=F8j|g6!Q#~5*&Xs-YiWrwK2LG8Cf9Zf{{Z+7tlRx=0A3VBdfAx;$f30G5U6^as&hqEgv?_bw5AO`pPt(J$oob>S^{jibA#!C-9z9(D*pq#xI@$2%(+Byw%9g!DE{)kc;oNAS4%$o^Y>=e8ptv>s%hJ`nQu0^dvGh(G-B7uEJ*}<HTh-c%r4##%=niX$QM86rOo$YBMm(9XiED|Y+)m4~@N%NEHE8X$O8}3CBJi4Q{K6TeOGV&OV#oA#+V|Bj`RjT5)XAlvHcTbhd-gyZxd9wV%;60u)UqeIZNWNMb_#*q6UPS!;KBC$78P{%Q7=Y<<#t813)MP$vXk~VbOi!Rl=-9S1|>4NgW{Rk@`1o<SQQv%WoUG<uO>smhIHp@y!4;5^`0smK1%3><x|6zNA$4)+-`~#mDpN72k!wmrqV(PGknFjd69nnL1|Bnlyx2lAmj}eyd^6tIA_sT6R76k`(-6ZFj9a6V0mI9>KO7Oliw2T%;FK{y|be(f>MBRs$`_6ILF_7P05SZxuxEs#ron>uPFgR`G)hoQ>UwaNhnz9ow79_C#!v+ASnyJVe3a8xz-y^0vEgxBV2NEf*6@D_+E?)W!WcDFB~m+3Wqp!zKsihVIVNdbU4u}5GhckWy6us)`UT!qP{Jf!zD4{gc63>K@Ib8@P;#m+*WfQWVkp31@Rl2faZOffJ?BjBC&T*?SgM;qLonK!PNBfWQiY9>i~TjqOqk)N*?$FG-!m)iq?@K8H9o!V>Gapv%Keb(H2Nw4`O@(R6%qumd=z{{B~&P1#xB>AZ&}cKOY&ADe;MYLvl+L`@@$Sr^dD@>urPvq!u0#gVqQat&1e@EFdW&!z^jg%Uxj29<b3!wolj4-;p?ss?X^j$d481i(P)a>0k_Ro>_sk=UwD?{_t(V!myKH#Ne#!=Mf75>@!E-bOWmpV-{Z(HonWOLL!!)QVQkC(!^_gLge>+8kx`uTbe6OLT%9#FN7^K=Cm_hv4uxLh!~=XB$y)^zH@A8tr)rh$*EtLLudvX{h&A%{@)jn#tTT}1xxVq@@3(_jPT0{zo0c9d+A@}<1c`X7r@2~VB-a_@dDU*0c^YgHl7XGIQcojX;>CSKeZ9;c*h(Vi{VD%E2suCMbbR&jN6SQl14@DSX^IJg;E(UxvI9iN&Q_V=EuPs!H@%1tv<$YSP5Qb`su%RP9itlP>4?j%dwKc%tep}Iq{C)IYM!`b3l&iVaOy+PGWbIX2<B(ruXFvnd)#2!*{vDLE}nikKUOAB-{~3VrBg2OnJE}v_nTacl>Xup4-b2=@F-J2v^eY6M)C$rVQz!n+=oOeEbH>(i=u;a%;NNN@SM0&DKCKQ9ubd$9Ncx-tcBsIzlUda^rUVc#;u<GQMy3=m*>jbJGR&5l&`N`G|ol+<3FYJq~w0PGDh01`LLQRfrgoWII!pkvUgt)4So!Q;3KP=&GJi|GfgDuzv@*!g)M{KSFC9gB*^4CGinxM`hymbBxO5%`(+z2OJ%F9WHVWEAnX3|LUDyJHX8jxN-}RfNkRBB(uXv)O-On;*YTt=l^<i%m5uZnjXUeM|0^Iz)(OARU82%!(W{nu_bPTj;P!jAcUI$A&xHK3dZU9-e-Ui|LF18@FC$mq{>e&%)9ereu~c-W}OBKw;9Jl7yw!%B1bRfba4D+QC~rlxFax$d*qk-zkZ(V|JAV^_37DKR4GI?k7;V=pEdCWD!t9Phun4$)J(@}nqGyS9ZO9?3YTafJz}_tGvQ2@wIpeo4drISY9rcxF9um7P(|T>Nd_Xc+k$zMgg0Q}rk*Ws5*@jXfgIaXC<L`Y=Y?Qc6f&qgz(~lm*Mg-2oHVr$H(;iTW%I1T`j5-J@h7sEAmafzq}j7pH<WyQXjinUO$C~}Kl{d>%;v&l3G-(XFFg=Gjqy=To<r0_psRHGA%vrcP}>vm!xLC=_}g*p{bcNG)>`jKE}a0kz)QQG=;Lh}^)lq!$&h;+a@U9ocRu9Xqapv54`#^8Hnui2)tP~xEP!xz0o0clKzPmqsHd}kGfw@QQ$IX)>bvGCQ~yu>C{6u~V}CU14ast0#t$PcJHuhVpO}~Z+0mU2Eg@%n642O)ayUP${>`TnTYeW*6fGFIKxx@mZW%&<D-Jg4P~ex?`?m8U5@sQNMk;ysCtuW}wQBbH;}g(3zOua*WEX9LN)8`c_`6Q3!U1BR-uE{IX%njfAP7_-vHGLHWe2~fY%<8N=~VkY_P@`if^d%z1AlrTbW2h|2~vp!k<r6%yx#yRuylAJChP{zp^*OQZ864yP2~b(Trho|r_;qH(#82XU0f&Xl9s~|DF=N*7l+H3P^nOxTgU_AyvR&lVx5U99;xF}Ay-M>*y9Fr6>~$xotTZms3FfVR8l+6tlFIRdO&!b(Z)+>5FUj|t}z<9Km^uO3yLX`BpNx-_4w78<b>pKqL%%j$mD+ENsB+<!2x*1@Brs)m1on6luCIXu4z8Okxr?jgMdAT6kF^~La`-&veA%pfK%^Nhfg&(eoc@pW{o%EEI_Mn{G9`SazR8`cOZQhfmx8;1b)h5&P3|sxF6bbU`Ojfq~*##)IkJ4z+1XduV8Cpu{F{F6Cz0XHIv&VJ+Q-!2%7^Ls0r6Wx5k#KF_Se6z!c_xx40MYXwi>``Pbi^56uhQatPaJEdFdMvRNLT2jEg!eVDBIIIMZ?UPjMHe>8^F*ix@6le+Tuk}9;3dsqba>U1R|L7B=*ZjaZn>GY9oFFO*m#aR(*)j%p@T~;Q>d1tG!(Q3TGZfEN-ze%*OEyZZdZz=VH8X&kv3ojO@qP8s1DxdRTdfsMuUm0tn1TkFb?-7g)tW)8JT-L(3-ExxE=JNKkuDAX{HwubX<$)|c7RxVq2niM=I{+W^;M!4wbC1s|rc8I07|ZsA(2`!8Kx79$!K6v=jMc2?wzlAw=(a}NS7^QESHhsBL|*X_!k>Q9sN4WgD3mQ!;g*1arw4d6sm^oJ)titl3B(avSEnExZKCul1iB*`WfPC7eOh{ohvOyp9O8FdP<Dwlscivi#5GVixLyPa`F8q><OwE(vQ5+QfEF}IO$bYPSl&KZS9L>VXs~92w&F+F_?Pyfqe2pX??JtlKi+mYRRm!aAg&F7(^VdRtg-|l;s!egWT>fs2PFs!Jz$083EJZ$RZH372H0;Z(&m%oS^XET!nx03xi{ckyFj=`4E8CIJ3j}o^H-;eS;1I-O>MnfQ?!LlP*d=>8?^Q65xI>;orv77rpRr|=eGEYyaVLh9o$?fh><JG0NX8n=0e;#Lu)V2LA6WG!PihXn?SYC;j{r?uj;zMv)BHh?gVmwF4K$yn4w3BI|9kh=2ij$$amdu0VAHcd4#})AAMi5fD@`uNPM{@3bt?Y(7x^CKbGffUMDnyJ#qBZJ#tI$mJP_=+8T>`mA%&(AQjGKsVASOz_*4eATm<Uf;@ZL?89&KVv8i}jFKwJkGLlx;+G(Z56Tk@qyA;X<e{6%Hv*cQe2<w!ptbj328ik)+0U%<m-!^MZ=2E+;@lb%vc6_It5wB-DftBUGA9T$S$cioELb$z=R`j)_Z*_5sc@4+g*-u!8>z{~DszYF#nz6<AgjjEAxel|`E|@b3Y@_yr$9>}8lPLAlbqz**#WH;+p%%+I$<I6?_U&`H81-G&1E(a+kh#YPqhK&7{8>*6MEBNuEF+-8JVaY$zltA2wI=ER433R1FAHb3Gf+mdrRy)XmIcG%LRmU1sz{d$u{2xW8Cm_EGU?2BkE|?PjNa!&y)uI9{U~`^qc5b9vWJnokxyS!ci?O(W>X^m2c`hzFLvQ?@Jj|PH;hxF=IXG(D$XL7Uc|glwRhiR1wWv%9rHV&D+A4CEQ<;GBw}nmz9YPwxi3+Z+sh$>)(0v(bbF{-F#Hcxj9FAK42N0ErN8u4W@3<r{g>8guxuoUPpJ#%H5TmWmLjIXn9S;k`t@@F~&-RvYWLuTMtA$BCVWD4$2R!y(vYfF`^pzxVy3lCb5*+;wer(9!F8eoqR{F7Yx!Gj@qs`YLWIi<`uD&bU3^^w94#7AvjO{kY)K%=(~IG(Dz?|_8xu7na}U6CrtcQpw2<HnE02q7*QYFqfzLs(xju(hY8&_=upj*$28$+&0DK5cjSUaY1{f~3#FODKy|j(h<u?ZjzkC=HQ~7VqVETXGF4s6jT!nY&g%QzCZpjF&>?iXM`PO;gEzGt(rVH?)x-Hu!R7@hFcECgjh{>e-Q#SV{<W7jg%^DN3pV-X<;w`ajPT0{zjQFX@J+t7FZ?7!>|c5pUV0Z^dKZ4OdKaig^3>*o>RiXe@MiVAeuxWw3?^&&%svL&n@G6v#D<1RHv_7M-VY58zLI1y03DSi(Y+W7o9LA%M<PMuUtvZ+8Qipe;Y#nqapOWKl+p2zrMuNnP!8~GH-VYY_#;R5!P9r9Z3l4>uALn-r<|OB+|3#kDmT0SqsE9CpCu{cRFC&@((SPY9Z2QfbO7y7Zh*JD5vM=DP2WzsI^295hE{_j+%#pBoVF%Z6EJ?Dj<j85ELXB})YY7I51d}`F)yY+<pK51ogbpp!9RX^+_De~#@tAT@Xb)Nn({>YDPiOk`(I4}!e=<}{0ZKF4(cDk=|=$kvpDys{wbY5>~U(z2`2rNFVL|3>G)5_FQ0$?Uxn-OZ0E#9ibr>ixp4Mo`vhi3cadwb%nE;u%6Hco9H+qZClV`$8Ij@n_KW9|HI9EB#w4Bq_J{s}b3<x&;M@TgK9@huhR#(X9*^hISWRD+8$bG2KVe==_{9B|Q}s1{56nyHz~!7zvO_U3Is57P1YHvoD#?KaS26Vz)y6jh$pUyt;=Z~f+a4+isMOIa2N7TCT80hKJ5vb{<rfifx*ot)$X5Y3C4q7bLNHLC(e?I)&P?z<3G#K4_Z4<W%CC_>K1f?C(YC>)p+EowZ#xeV3H+01i<dDzdokT%7jcwZreEL%mI2<?EIJ_y!I*QsU?Ea>M~TZzY@L_!O19SNv)r1(z`4mXmUk+Q`B>RjKxE)_X8==|7fUa!@|J#!Zj;)fJko22Avvjh8EIMKgy74vVVP_%(c2DIzDpiW_`<Qo%}Wx%Y&f&+Y4|O41foa~7gZLiF!SQWa86)n!b8+Rp?W`D`Q8D#qj8AC@xiVnaQ1N6g1SIiWR}X<@g~U+4m74#m_u7;5Cjq*fo3QP!F;(>$LV2vqhP+?h!)+THE%8+0Ea_EBM^D~_w)bzZGmoElNe7&^l8L0wBD`LyddmDni8S5evv>GX}DYO+7&CeEUXcg2fS=oi$0AHFxVK=I~FLC`rA(BJRt5;tC2(HZVJOy#2D>Ul~!jWo<RPta8i(I_On`XB<hP_Lcsq(;m$sS0ezbW=xrDX)z0H?&oQg9N@z$9@?R4nVZE7h^I;x9-Wh@w5aZCVq$X8<MG93zESNe&ivnULKsZ)#M;u@+5k!Bp1WpC89ef-aw<W5(L53<+CKdcK)DU3_)<ERAg%FH}X~x?9k{+43LX`x`2B7Y6Nnf%|T@(6HmvS_tzN2FDwK}uAhM92jKd64k^?7){M-swMiaWRixVy)05fdg?2oLz?haF5(9pf?^?k!Y%0aS)UZv`sVJ?Qped-v|HGMYp}7f{9TDf^eF_YFIj^x2m70!ED>+65n1<3Vy4$mRJ8nt!g3#?zjMek)9o!22|s`M=Ne$+rY`Q<bpcd92^jm+r}y+`O!5b1T3a%5RDvFdx^HDGy{oPXt6`xKS3aE27siOS|Y&53WszlQ?~Kq!wdr5i8b!LIMT@wnm)ELOiFPprxEW7fm4lq{$zy*oBN$WvqhOX#SPzx45n6pPvD(a=IaQVqb-hHYh)$MQAF)s_}BCt(=dsF9`z-=tsyf^s(w!K}%~5{zwoWC+=t+xnv1|1Q8|x2Vl+gn7a{^VZkPW!=C0K5O#w79h+?a_ddclMI!G&uGzb~Cia8oCjSC%+t$@v-~e`1YUnn=RqfRs^gx)(!Iphq*iB6b#sTsX_B>A=w2bp($&O83#2Y+E8l(6JZ_8*;MQ4vXCA?eK1;z75nk6t?NBt7BW{LJpvxGGQ`JoH3WrM^;<1DbD$SH$6*Ba53segjydCWME>a&Di)81jl0`!hS4y0i<Tu)w73!ucF)D)4=xV+pHF)-f-!)8yKA}EXgZrdT^KlgO_cjA%{d5Hq@9r}GR23nC!tT6%dAbphghYjGb+p2KMt^wp8k=ysklQ=bvCeDt$@QMsY+|&Chln)OjB#-ylsn!C1)2OaX-_o{h=85dvE#K_*l<r|c&@aVn==pm*aQ2~}bfI7*KaY>NCimcGPARUjJhLUhPhJ<P;hN0DaLZpfPo!@fZyC!p5V*jEP-l2x(2@V$aF?Y&iu3P?7-hU1Rx~o6n%TAA@w)P=0atYddNkXIxU^JXA|XO*2(+ZN#PZAEoBXZ@!l@M;b-^@YK1l<VW3NCaVStyIbG{?099^P7n?obq3lPr!G11jBg5tNJuM$Qm(q7boYp<p@Gr@xF3i0&@vbjKp1_04LT^5|Uh0ZVj3v4*c1N0kt$eYQKHyrZ7A<rYd&!Z0f9Iaorq=@jMyJz~6LoOUAhWrK{0-+3c$7E8+0f-IX%*OkclOR;>lB3=UAj>DS$Jnn2E79t{seP01Z@s`X>98Y1$3Ai_Yr>87U$$>V#8U@H0`2&J=L<~*8N_Lbkj$pMFdbVUa+eqwj4N5vBha;8yM83+u89oO*9<k)!P%7RM3nCMtZHJBDacL*V-74cXEcD>0%MDdMCB2X1~etWY&EPCyM<_<gT9eh0z5J21rq92_$Qwlu>(Dx7YQ)H<d#1P*Ly4>w_xat(Fof(Nlo)9WgEZkN<0?Cq|S^rTBe9$CR}`o;e+(5VFJ+E@k0^KD=pk$E0ekldFL@Z0S=C{{CQ#wPxK)(B;FT}6g9~rheZkyAO{o8l*902T{QHOgQB}Q{+p;;p0wl{v!OLqModm#g;h5mZzKc*CqWnj`voE8BBwDD4h4t9H<pi-&lXLj5-=Ce1IFRrB3SO*G#`~47+-ui7UC!||8Pt>p|{KM77v#odHmpTLhs$=gM{wt;C6_CCx<QFjGV?!Skf65eoyij7M~AMF`F{9HPn@TMHs%6Nr7z%_}!2_DI=MOs7{6?*YRZ=(rgLk>q?d{gnqcxSXpcu1rF7}mQUH1%taiyMuyhjDwMts4(X7kI>%Ho(MVAVzzQx8$m4|WU%S9zkA)TQxN!6O_+}xn&!Lhhhy8tNV9Zl*4-cj%Is;q!ot1YM&hO}EM<tdVSnXTMN!(jE)sD3??7atu2<ogNJ@}do@$t?m@QJL)JMHa=^d4ogV1ePqhI@<8pj&Z=uRtKpEA(<7;jO?UXz!VQfci$D3!`R624Q?y$YLDWzqzjlv9zdk`2T6%c=mx_Jy}uW_JRk#fm?b}Q6igY^-<Su?Om!SmWZ~jVHAH}TH=PFnUUXJeDmzuMRO4G<^{iR`6TskIP6pHpf0npQeqv{;8Dpx$2J$JG?VOrh1_!FCBRa@<&orOI;T1lD(i)?%1p@nV`mqD7|0AIt?Ei`D!h0mNzh~vH-1TBwVGcc9uqb_F*0L_+)<Y#kl)MnDV(F{Z`bCgJy7|y9c}>KY5Hq+9y)sIYbx<EI#_ZC-x96AyyUC*R<)vwUI5q&j9WL19)5p^e*2$9$eoAb2UY(O*Y?+$4ABpIU-L-E{-H|z=?-okFlYNU+Ya*p<sG@lF{yDkH9nOiS;u@ZTdpwoAJ|ER4OmH+6`T~20pxLR7o2_UWBiC?P~ZDDK@~=6WzQ~7#PIYr9yaK%%0IUizC(OwD|Qxj9<5<S<zpS>#k-^Dke}Gi7K!ye&M6xKHNX@ZVAl*o^T5N~surPIizFwXc9Z|=*yWh-0`F|^)vm>9b%SieM!i@6$qQuu1v38vhJAVYGQuw-{4&BXkogzL{0n6M1v38vnSX)Izd+`H+#&M=;2qWZ^c>W@JNITRztr!I{eSqZ@bZ<bjv@2m2r^H6z1w<2I`g_v5m#wq!K5VesZ4meNHAx?%NJ(*34r<?;pKNHc=@YD|EEa#vp@MZ-H;%iV&3PX1><EG1p2_;HTx0%r4x2)GDJ5*Fb0)_stZu`DYAY*pqE>)>-6(096|k$;^osZ(0)WACIidsmpH@z9n<bl-Z9R7-RbGS)mg%QKWE!_Q|*Dmwts@7_b129es{LaCtpWir-&j4KtfEJT64)+eEkW%{uCd53^PB+r+)+qAIRLNaQmnK`+DGd{}{ghn5^85p!-W~@*`0F@}*t@%lkJ3z@M}!Tm#xa6<U4*w?74pA3?>ZsQFW%{V78H=(EGivv~H4`UEHMPrDzga|fJ<#ut$Lm2bQbuD^z?_l1mpvSe6+ItI?WQz(6`rYQRfrhX`*p1xUrW)*^+V^s^~flDPV)!pa3J;=HD2I4%bZKa!1*s6><8qAaAh+-)x2wLvdrvfB^E0}c0vb_YB@f9kRgh_=fuzKa!5H}{du|P$9=F{4i3ftZ`bLUEZl-PxAt-8V{h2mtK_Q+KQi&+M&P<jFaN0&egf;7tjd$8~<WSVQp6conFmlH|`#Uw+```W<xR*6>ugs3oL##oQJDTc=py5>q*%2D23rRcnl#01zDq9N@_DCfvI@grK??!`-%8N;x&?=`uZaaVNq$Xpo>r(!;^JmhEtLtHgT&uEp@s?f7I=vYc4!JA)-s;I71dh?Tx3I~i5+$AcYj|H`S>|Xd<6ry}84UP5?{Q!Y8N?L$+1TcMvWwr1}Z%d4Pip@L`Bd?<)O6<vc<O||J=X&Iuj^MYlgO3!}7xl;i2x_Z|9ywXnT7OxOJhI$+NsOF*7^5D!VCG6YPVkrl+Pb1ppD(s6z|1fMW)?|uol5+j#;D~*+lcaSC<0tlF>;pQwW_0t%wJ27d@(Hoe@J@d?r&TrWxIe{*aDk<W^VQ_)R$2U#4@dGwRyk-PO1NnVG0{lXc*Yp($svzDx=0bkf>5U06ekz%<QQ!j<$wX=Z0loncy1m2;hUyfDiagfan(Tpf0qkQM9UF`*dCn4d<2@-nSRIDnSNtbJ=$h%#vDPb+Ei^a)KDrwhCL&Fg^i@7r4OC<nxWQX+h@r(l3S!zDo25T<ZIrP5=IrphMpv#ixs(=12Vy#2rrJ^WYDKK-oqsqz!flK!<<~3jS8&WkUpsg-S3Hav>WFZ~@OzDyuaayP!!#DrX$F5I#t}tNcj16C~DeajLM`8FG6~dnCoQe4hHi$wiW5T-7bHj$|}H<RL$>rK~dOo^VgSVUdEKVORs&AAybFF}K3N;e$&x9PQ{=deWlbQXIkCEgQs%fAwUDk1?cM`)dcHZtGp*><RHV^YX5fOFu>IV%}4}MtlYuR}6Bw%Rh-Ef=$&eLtK>s20$0h{!)$uVLi49Mr+wtZc8lT0a*?kEC4h&J{Ws;k6ubH{+=hqU0_rmXyN;1@SwJYkyP4f(egRBMm``(AbrImyE8j$Z&EjR9|e_FBOF1A(b&Jy<f)+xR9wLp6BOJm`0-XqIrW=Vai@a;&gL)CkdTSKOWOLn<pnRmkC?A;<1GP)eiCjzal=0m^<QVJ5vg>6-U2+FxMs)---t*~_U+}_-Zq@?4bIRm3}2d`VV%gKpD*HHp7p|Hle;LrFapfR>?{aFj=9xL+F{xq7>0XojQQ|a)h1S(EiSpOnPSLOU}e29$rV0pdAh^{M&Y-E-^Hr$(dW`_nZBZhiG<iJ_cX2f%{xJUiF^X?p5&;sT{R^@7P8nq$D;@1J3a+~HV$hy#KQxp=N9O_t>U(#ttQTKS*ev3$m39Hb)`S|fymf2MNTLVazb@+l|&dyF`GfDX^?V?q5}=q%`?-pDOv#FvSofUq?x2mVl2?!Ti-z7s7pC$>@;CJOt^J}#i(y#MY89A<8=lI85F92NB(-(7V)5D48?hBdNt1E^Fk`@8`Z!1Jeq%~?a)Girxjn5Z}phzKmYK~Dc2L&hsEx<q7RyG00-LvUB{PuPiK}ePAd64h($dQ(iUNuKzO|l&VRVAdTUT5?)yfVUF^Xh)0Iv#R5*<1%*Wi}4By7@{L>zP^7_*b+r6jr`wDiViknJ&zg)o~t%<Ey!>9M_KYkti-W*}yTegXCeY^a7&4`a6{?zdRywA4U{B$sT=#;ye;H;qPO6*(rIWd`R=>x*wgM=1qS%l_7z=zV1o`>XX3d9&iBtI+x!Qc5sfbJRS9BJ>y4Pbg2IZ<evgAPD$QyNt1h}DGA=Oa5oz}@(h*q$PkwBdjAVYNB>uDJdnRp-`>?LM-(T6lCnM(abizO<=&B^HR8o`9!)IX)T>ju+~X5w4%cxz;e|T*1DF()>A`B#mFKsFN?*ryNGmcF8Ar^_bYdHi@`kTR$E)gxkmO_(|rbV%yMg20wngy8r}dnPUECnvBEb0^Bq(SClOW)*JTS;O~C&uNyKL^KZ1y<I=f2qVv5Qy6_ccm3L->R>R{6liw?^P2CR>TIFXau?~34&anN?y{h~lE1IPF;XM46>WN({%b5MB@cHDcY$Cu#+r?w?XD5VvWxojUPWE_)x89bi1xtwJ2XwY*`8}JSuo@PjEWWY%0&_oVZc_iDQFY2$Kd=}L)as3$JB=r7VI_TvCH2LQ60!z(Hf#D|>Hwzbqw<W7u{omt9<~I>I9?UoJz`r}iafjN+Nc|6w=#uxJ%z7BVJirerV<zJw1I89^37r_T^QwGbxjRcN2CmKIzCa6MXCFhi#N7^bxe~AV7RXkOXpx3k5|#-^WV<fU;jNiPWPN02eOS<jE*aK)BUg;c3>Atx9ncZqX88fv^<8vSi?zH|1$r*G1l@{(;+a*W?M1b;aluGnpU2gnSmZr>U~pJyP}8M@XP@qco}q3i)alf8>?24VA3626%isY3{&!x?>xcRY7%0Nr=dTeFUE5UXpP0h(wnl9Tv%)xQ&St)SPj2!YT3<#1T)I&s;ITRn@P`#Xad||%F8bcrpOb|fXPD%jz%A`Y*5YYPAVO?zQ{6oCVq0<fZzYl+v=NckoGvv&B4n@A6|C7(~<fC{gD~jMGZ;9p>Ns`(g$Q=Gp$61IxVHClACAfO4b^i@<aeZ8M>zQO{*u`e9q=X0D<|kQ3F8&;&dml&!5O3G=r?@85xAJX}T%7IX~v+Mj3>(<AV<H=9ryCJ}#=Yc{wUzrUOgX{)`5~G~KqmoNn8`-vr6GuFKzi=Bm%Y(?81J{NQcM-+Xpe{^pxk<Zr~eP_%C%L$#jTH+hwGMf)a7`-TcNgZvHle{O$L!0ApDaNMZ^PK}dKMR3}=2+jiYMLXj&b#UUb0!~vDaB7-=Dd5zmfK#oN-!39JZQ%@<ir~Z|f|DqMv#Cb~oV>Aod8~j_iBTdI1)Of8fCI$|2+@r4H_dtZo2%M4wDQP5)$!->-B4LNR=vS3JW=@OQPmsxFCU8D&7Y}$$JO6O1eybK?ArO6KcMv|9I8b&@ekDWT9avlehNDDVSwqrp?e&Gq0Ov=90lwCL5p3hm=HT%k3>gA^h!huNeIxNnEk;-soT<_2Xl$Z&bGw-sqf^iC6etVsC^l3%d&ht-4;)f+qAM`p9Y+>!2*H8$H!FiTa*;nXAJycXO=kNj&H7+7|Ul|R{m?jcmvp3r$i?=m3)yaat?6U@dLv^q&L!3HP>;?;)lN(!ZT+@n7{S5ie4xzTr7IEksIsNi(cFm)A_m=hoL=F_iCO}_evzvAqmdK(ia<po6FU&rc}S&)2d(TsQMN2_DW`=H&Xo~6UR^h^G5}+O85hqyhm$b7dB-pfJs)g-748`<>rMd$ob{3+RWNG|JfDopvi2yQlny8+q8ow3RS)-Ay_s|iG&AZjmorxN_C2LAjknZ1!bKp0;nzXS&kBaLDi|ihQw;Ye2KNv!hyn+Y1*pec0X0JMyym1MJX2>QxIxl_K`BdR|N4r=n2CY!%kQEWy^G307HWl8<86m7%Slm$fMyq?6b>kGuEaTluv$G&NTh@`@%!VhFWpVw6}Olw>044*I;1(aXj@^vJ?p+EZi1q7nh82`aD7~wuupeTaly;v31qm6LUybC^V8%PRW3X8)W5UU9gLu>HWOL#Y*&dy-0JBFT?M7x^bpiZ#V++1$VTBl8?7i5Komql6`B?g%s=R^;drvVHmxTGrj<m?5`{x?Ti-9gEkB^_*H(6RClZ^;a4!s+pP&VB@tpJ>@tpCbuGglDz^KA=F3W01PAKdxgPxu<b6Rlwjrob%x?8Uf{i7+zzw;(;cl$z_W<?$MO!xcd42DzEgMJ@Pb9ad%O=~~R94RUWkYvXD`$JWY+_k9-gtaVU020VWVUH?$7Mt27T#aekISZKsu=U3D=P=msipzHA}B=^C|ou&GNf!;vuqnRrntxr7eKtl@@Vh;+7jkoi^NEoxI*%7yeGxiO~ej@V#^^ve0ny&^z5<EvwwAN>=)v#dUWiyIULEIVN4hEv3HZPcjQ4Mb(U@Tuv!><dbX54D=q#u{M`^fa`@Mmhu@FG&ui<BhyNBOHkB718T%wbv&J~|hT%^f{>|y||CQ=D$7Ei8Up1j5^FE$r^73~04MZpDTUbUQzKPW#+tF-jm#Wthk5=aa^Jy8B>k_X`V9u<^HXBRIO+FrXGHI-ORj>U=JqTTpREx5&+_stLL#fI6do1iKKhhk_kotwNr=Tfm*<pOdSQYpV*n1+$PGI=Kc$bgA@wGnA$e;YTx;DgPkprM#BAvh`{7+V<Ns;Pzfh%Fm#^l%dRICgPT!>Bb#cYh1Ye@7n*S6wUumTd5aWd+(azbU;i>6&Ha5p7tW#`32Nf5I7^+nUbif)123mk$RM1wI_LV?=>g0ni9U@4wJQ{A(^j?1~RlsERSzxgJ?FN1LK5%?w1O=X^s@T@uh<&uwjihp5N1S`amQgy(;2$hvxxU2Y=Snw}V_!l~*27#I5Ujn2uF@GWXo{k_eVlToMG+Zun{S(Bd5r4FXf?+a}3AhOsW(2~tQ+f?PveXz=m{wTb6cI!ElTA3!gV&yODbst$RQ<yr<1pwP{Lh6!VD+m+LRg=GZKMLBJ;nig^K9Z#7^I0d!2!0{ae%6BJS7Y&U=Q~uK!BIBlJ8xa)%`ow@45bGaJ%UfvNJwZ%kN{W>a~|XsLrnDAY!NPY^|yXO}QvIysU2Q1^HMYT~IfISVi_3;TU{m=eUg`6B4Z7$9PclUv~$qswTbUytsoKT(OoR%Y`j(%kd7a9pC8+nf|(?NO|_9lQlG1umF!wo^!b!JhTlL4ZRXo@p^T&+zscfOpsMaB4HwGUhfX#t)d5%@9~Boscm)kylla<>eq6}vpKlAqPP6k9CC)N=9AZkV_C@UdxH*nq7&p!9P*?f_Sh+`=@jk@g2fYKquTKmhnzfQA^s2Vg)X<Q3CVsAU9Klx?vdy<15El6z!sgBeM-#-Bvoh2KE-JVHk&1&q2?p<^8B1i*@qQRC|*aa9r_?}KMgXMtL+HnGAH)WP4iMSy4+@Jji+4ZNT*cI+NtL6$pI_)5+A$6SQ5bL=8U<p;EbsAo$O?FS#C5m(^K7qlXB2PSj$SyB63wog&o|VHyq`6m_u$#@mDL;qwM<tuF9&rD^Sr0d=;#mcfj{GuneIp?C0PhBYhaFv5`|b`#_`|mFhE%p|`#cK+`y=d3^F<KftNt?00Ch36!<>>b2`CJh!q{+5+bKMAyWFEwej@edNI==VC|u$x3eGk+9MS#WGQdgO4R4rG#(`IAUN%|CYuA&gmA1_2tZ=wK6+aMlTXl#WKM{@nzMj6_f}(F9z%_{@P<NLH!{t!I+GJ{L5Os1LG^okA?9y5C57^p!HzeweU{p$o#B!1Vw80>_}wBR9XY6YY@G*%)x<@jOgN4>8Ml*)-8Uqv;^X}zc(LPSKW6oH8I#RJ>9Q55Yea2gvU3|_8f7*E?S&cOnqW@%{CLi^i@=-N6?oNk?PLd@Z*S6J*jh9Od?9ooG@^&uLy(p7Wvg=t6Nk8bm3X;T3q&m>$7Eb3P!#+d6}9B^nCpbQ~9d2{`0|0exy@b8O93(tuDXLcx&YjaD<~FRN#jZwV3GopscZE){^wV{tw@UHSWsheQJ$EDE4Y@jj<H5_Co1KaITc%ogveYZ8BGH@TQP3H_P<5Q&p$qYJ7WSma`?4#DsD07vs#mG!%@ICyb-^FwRzo=S<;BHI<2Gu*^=~TIUP$({h2IQkb&}#b6W9lyN$V59KP!r%|=c(>^Ep!)BjNL;}c1IX%TOrV;9&S+1939A=KO5JY&sZ{0Ee<=06NJWxu&0bzyJvcQt4SqI3zPE7!h>xit+cMv(WY;^-5IMI7!J{0&>07u|`Wh<E7>1-Wp7L&Q_ia8s>lYmzbOb4(aY@L2#Z6M2*ti3YziGiRe+(}9wEB=WfGJ0(ME5fpdcw$CZ?A^g%>)s2Kh1Q55><_j8NG2^|K|I3skaxxw2Hbc2#%!tcR~#aj*S1>5if|T(yf&*xYIV6~^In@j%f#1>Fr~lzqm;z1N+Pv>Yf0>}_G2~~i*`SAn77QL4cN%Y8JB}t6nlDq81OSKHsM*l=g4`!MVSY;_CMQ0=$-%Kv6Uc#`+I8j^yi+#QalPKZbE1{4^W?2?bh12-Ff?b+$y#rHMgb8u+J=5q@T5ljm0?Dz9RN~fGbRg#~WvD$(FU2Evp(oZxw?HQVvf*r~DZVc|LzjcJ?L`(8fj_Ks!>&kYWCoF4d$qU;L=dLnx*bH^+k6NfFk%K}n6FCB#;U@RVW4u09A2iP_y-&J^ERli-xbGh)l|`^FL!wKu?LV%j?2>?fD{$`(xN1?!nEw6$FAHO3R=kax*e`>Suv7OX2ZnqRX8wYd1N+5!}%>FP1<kSEktiy$8QYeu0xXB4C_1rCv+EZkl*3eBXl)yBu{!cYh9wHLT%aB8kwhaE;~qa4xy^yIDb2@mH|E`8ESdM1~Cy_Xbc7TpUo>SS8j9JiD5`Or)>k9Cxqjfju5leYEQUQ$b>BW)T=c5<yo(n46x8h0bAk8>&XG^Efg9h?_7TSuh1L08<*6Y0;&OTPE!<oF*|e-Y6}|6OhnuW<iB9s(8+cllOVvEBp12M+qfz?8&^c3{(|kB5EX+n3i$F_Y|dZN;PySDepZNrr_wIq(=&70pxVm5?vY1NcZJf#N4>gX9p<*s|CXYG8?wx6M2$a6q@fXWP;SyimJLexgg!4_Tnz4_%(oe@+>Vo_R*k=z2{LZ<SYQr+bt*7iPpF8uFVG96*EV{A;xd<QdU=fzMij23yF7?T|O%6$;wn@#YFrn7$VyPc|pLx7aZsiF4tYEfva)j*6ichBR7^6;|)>ReuQ&tu5SG>7T}yw1QD}zO*($+(Yc(`Ipa}yUC9igN=9ywMmL#s&t6Rsk9mlolZ<X4{Q`k@h5}!L~Ojm=0K7N5O4)qSl*mf60ji??1{O-E(8_7>EALGTa&XXj963wJdhzXGID}FYwLu8?1P$oY8~mlaI8TcSu{d?T(CZ|GIWo37G(|GZq}6$4Sy|-zgkT(9(#2nR8Q0{ok@IP!_K$U?Zj)3A?ho`hbivNR(->a%^K=(6w@JtR<f?G0{6~O8+oSK0aOZaI8TZda5sL%@lUXK5*m>k<fLsHqS36W)t#LPCKi~~a?`5Ylv^s{x5nwet`wO1qI`-m<oP>c_=AEX1`)LQLqAf(b)C|@N2qjmD7a_`iJHImj@b@allw}92b<R<Jg{nSd!6kdGA(v?d!qBnUc=)eFQ^V!P-YD33u(;dy$LbyjORcb(`vdg@hNF<T0H?YxOu+?v%mhr_5ZH8{{8DwpuW6(kxY0YLw_0JmzOUi{Qe33OJePX)BlCj|3}Pua4)p}FSPzIwEjPtwEoYb@_%#xKE~t!|Ficdv9@emc2KM$R+PIq`|MM^;=lj@^UwMxPEyJgvJaw1j}8(N#x#%tJ8gl4lul$IF^Mrw8kj17%86_cSgvGYItYa50J4O;^l%F!42C9_jOen)7;{Cji&Nb9-n}o=_iAfv-+f|7tXQ#%S&TWxGbH|(>HC8_;qISUZO-WXZ;f3-Qo<s~tt-LmfM*p|k7JxBnC7nw3Q#sB!6$yH6_tNgSMSK?zo6qkA=97O=VyBTnkU>c>KE2*@5a}+_@-X+zq@mm|LWxU#R(bIJN>!9vh#;Ca{rYSL7eIG{a89@>ane&fo)}4q4Qst9ZQO%>g3DQrW!`6TFMXDOXS4j_aCb(tt}+@%Lccn7xlyfMI!<#O<lBk(k+<o=(O3Z!xqf`Va@D65kH@h`}?bp+kn*WWC&H!E&l7OiLZar$YAtHr4t;>Ae{z4A*{N_^<Q1$`oByi|18zM7#N<R`@hQ3e~tD2%75n%?!t%XWB?Wv`Bh<ZcYf9Y;Pk&jNgvLd7pfOo`>!4FF1K(^Yr)N03#UQ_ua^fnd*W5Bt{qS<`f&Na6pfff3w&v$Gy|%%J|@h+s=|U&|KwDDb)j(f;RWS`^<Rt911o;7=>hnc|8#M*T%9}DPh0s_2TuJU+xxV0!iCPc)?IEbBmVq{`CT=Bt7!V4t9}FPQtw>-GlexxLc~J%Ht{HuTA&+H#@IDrLQH#BmkZ0ecLX+*<G>4R4;A0U)KX1?%h(fW(;L9IG5u-m>Ybk2z$J~_{#bdio;p-wAzx;t*2d_Df~&TYCU9gTuXokZu?o@yHJgI6PPkC-jn_T_FN?hh>BvG?)$x0=2jX%q^K=B%gK~nL8>vAm4V;Ngu7I(W81WP<iEWEWlv!L_F5+nu2*9||yhzj{aK^abw#LbO+AL9gbvlxHw3q}bCEA=BG!?E!0;5sXldNphbvRhnrlNsR3Ag+86<&T{r7a)n&UlB3mnSR02#&N`d`R3>k^61P#&*BJ%TH8V<Yi%MN~n4CVM|c_D7?I91*nzvg99k{AJNN5?$<Xyu^=g*8<jON7zwU2Qv|uE2O}wNBY=weuErfGMRVKR6nqU%PRI20cdTe7Q2ja>>0ZmSvf8UI%1v7I;;`FPg$EMQ%%-iz7CB*Ahp7^+xG&p$NPA}Dx$&A-yC*ob23-Xz**q$!9ia&w&7^d!#%S%|f+w^R7bynKUw=o?^><wRLxSb)IS|;o7gH=sMZ+3Fm0VFG@T8J)3l3f8Kl88Zll-T!ryZf)3w(7DUE)Zf^@$z<prr+tK4K`4LrG9T^j}M~Qxd5*vhh=1)Np+=l}CZA_OLM;17q=NgN)c2i>edEil}L3NAp^9hkg)X2M?hUld|*o9$et$Fe5gK==+ffuz{pl>5iFf;(BH#v!2<^yp)g%DWCbtuk)Xw0)2DMLXHy+`S*{_`CC<Pt433PbbFfXUki$VRo*6QX5vj+a%`7Tw$GzRKv7w^=`~n>;XbOa136AxU&iwDi4k4B9&URh*JEbCWgSC7^rwR8@3oAhz!b%%4cEnXNv@|fJj*jw&93Fb@T9cSV`b1j!n|##xD4JGn_ifx^g>ON-<j^mS^c~hR$K#<-vcy2h(W1#&5OC!SJlKH-?dy$!v(Ir&#q<Y^B5da)brto=dXTC7{a^45WZN{j2=9+s)PYB3&U!+s1M;fBDThOLJy8wJi~Hm9D&{=kD!L*X&O6uuj#VABPM-PEbg!u99YFs*FM|?NxX?!u?879nzJhqM8ACItSv_sPhki*e4r2Q#^}Khxre`B{peNn;5TGr3nb|H39Xvqq6cyeaNHVIuQWCY&;>6ca4j_!aabS?dD1}OmrbS)gryxTn)t#5Z2d&R%RPZeA(%idu$wTYSgSeey7^a0WPA8k<Fs!8B?U?%T`12Huy6a3B^zoFZ9LhNm_Z}z+Q~jal>wG`<!vD}UKe5&YjgyO<A*#ah{_WQ7$eK&A`qqgm9t+(-c*fRc_6@~ij)r+Yhiuxr;ey95RgLBu~NM*YQTU=C!m*xYqn#WCLf=N3zV@&)`m0$+My)yA9;?eyqS4Z2;w6`ZOK?Z8eKUV31jNR2p}d^8H>Q#OpDCo;*J3|M6I~QMn0dhttKvUqa{zELHfzY$~!IY!v*c2a{^FgHfb`ANTVVjw9wWwbA=Zr@kB+gBaLy^0HEX!)~Z|?t#=fh$qA_!Y*_JR;yaGUdae2Eh@T#HA?I!+{y>q5lPF|#Qy`KBU}8q_V)wQhKoRVsfpJA_eiFwt7mF6BFI;B6(A7-8UB^Rdqq>QiTp#GXh3UT~>STYLekN{nyX&xKK3@`*dkcwr3pP!pFIL3nCJvZ2dAsSp%}t7@O-d$P#(s{)HPzFs!u@<l_Du=2xgr^A_}z)^+)3L<_a0~6*GtZ=D1s&uat6j`4r{k$LASwE9#&D{bklDM(G^FIU2ercuOH_1ShP)ra~@S?g)ie5{z_HE`i2FzktF^2T#K|dZ%Q>lwrN5*o^uRn>x=BM!D=Mx$v*3G&6fD&<V3Y2%Ye&tV7Ulc`P0^mQ?zFZLfa9$DV<hlTcTP1q1w{+5%EaP!Ztq@wyS=SEy}IU{-P>(8d_A5K*Zd4p+=!ytmb_(+tPI_)FDr3bkdaF&6{4B>M<E*<pz+O*TO;I)a*p$L?ww<d|CcL@5*RJcq5L?o5tqG3t1R~%dQuH90Y99F@aufbMOxURAL)#oH4fxj9K&wxZLOV+`yH{Kf3c+1z`w`oZ*CM-qEOXf9)NBt)9i;s#Q!J_o!B4xgvEX=8DA#Su8MUnW`_$IIrH+qJ}Aq=MKj%pL~bfqwFbr)+~8RJcER6Oa4-Ch4n02Vh<5hkMTcZbA%BdObVi9p`@p2<>V)`gq#Mo&5D*BFtM^xAhIic)yp#D@!O)TU@&r3-2k`jRTSOG0V|6LiHR!J)Q(gic3MG5OJHkPBQ9Z#16F<0Gl=-UHe5Q5f7(o28ok*<sNoy3ax?$(21JE2xq^`OLRsg27^L{<YmT$H=a-c~daK83Z>k<FHC7V<qvL<JCE)h!@y61+ruqd}KfSJCuekc@iU$^1zI;+jEwwDfUK(?}macwN6_c%6c>5Ev`KiNiD-Mb)YpVbR>lCZ!Hj@c$^cF98U}@!n(bB#l35_B)+_&yTY#~<jma;w#<?K|ab!VQ|ID1;EnxE@*j_x!Tkb1dU7z<Bc2Kk4;LjQNGrRSTd;_nxHJttNCb+}w5+H$#R*Hro;7<cpQI8_=-W7O@n%KZh8e#_GMGah|65vmk5lA7hv9LO?#m{=@S`kv2RwMEZR=`SnyRR}*9?{iGKo0(1jlu$*aK6%0FycBUQ3%m=C8%o3VrJ*)2fcf>iQu&g$!z&d6-Z}Vem=OQlyN{Oyg3Qa~rFYP;JE2Cy{(ePzL4yU)p^TT-Bo<C(QE7Bwu%H;fTE&H2P$?+ld<|U4bM~DxSyT*%_Jn#z!-N4sL}qH?1;o1}VrZGkOFA@B?38zLJTRynjT7R+QnjW-BL`1h6GKOf-+Sr2d&#t(5kvd6EUI5KqNOz>+PjXU4_4jr|JexL5*YHDYSzh;COufHFYKY|QcWvOaOL%_@_1VpDWK@KHjbRwR~b&=8Nza7HP%+`tys~vrk`dMG}S~Pnb*X%hAJ~uC@k^@mEb<h+M+z1Yeq!O4X2SspQYt^--)X{;IPe9ZA5wNrpQ}wrhPWS$kJe>C?gAFRi!VZf@u>8Yg$ddB49L&r%hJK5;n=j0ajZt-w+BprhsY1vtpifDtaysV_0}nQ{{Yg?X1zd;H890q9qve9BG&(%Z<E8EMgt9rxUteSJBt&&01a_NoUZQ!O3y6C~5p4BmM8a*J0k2syLcO+iL^d+vpxOy7RsP)^r>>l7$gtd^au4(*Wn_UXStiWQ<1}-D9P|Z5iOcjBeUcV;SA;#nG*Z>0*G#vjHAY2Do$kSB&nFwR)Wt2djB>i(hJ07w%L$T5Sq71Q{@2Kd#XUP>k&7LA__oN76oPXp0dHOK{;{JsIF}Ilu?p$d+D8vq(;f-L-A7G>Izx#+mBJH$J+5?Nx#3+=2I1k^=D&)L`I<xvvgXFYor2Le`>#U}*@5GlM(A@1i>tpcyv78^0wxly0kI`q5XDeH!w;_b9nW8k@cwKJW5~3!&M-O86{dsZ!oLyUxvxKk|fkbV%|Ex29eTlIPFpGj1$FW<aythR5intEC7&e2tBNWawhQZtb20<=<s~z2P@@I}|E*))G|A>)^biAv9gNPbw%e4_g)f5^)eMLbG}Tf9WMd@6{=o$r%{Rf<hG_2;SFgvkq-91n4_Ppp=Dyi6s^YN;Av)ua#70B1WVztUFFEw11pm+Hngb&O<>5iDb$H6wL;Plp{koHEck$zht|m$#Aof&{X6d6qF{)A+L13h;FO3jpi3NnqpB3sFTsi*kOu|)`_)t^rJ%AOHM8sXmz3MPJSl?4H^q1=c+9gz>J6K)*~Z+8=^UwAP51pKuI6R1_MaKAXIMDFTO_KYWQ~OTm96t`c`S7Z-w|`I2E^glDJi)jSL~DYl2qkT+pgnsabVJ&B{^DN`vUBM0uA|Ryzv8<z?uin$;+GWi4nGi=b7%5VUHFpw*2u=)4J9Ia5tv30ieU&}!til|O&J(6p*e(+X!!HfeC?10-sZQyh!3)zebhiib(usttDgJCfDk<+Vd5aC0VfRax51GXVyKlDGzgsb9ql>Q|iQ0@vVq`uhMe+B}Kdr3@DB1Sw&)@1TT5uX!bg#T+E{uneXAZIQ(Kzu(;fe}<d<JYcinCbtmbx1XDwi`qm_?n&QpO{j@F2_e3Yn>?OzlS>CNzDA{~Dj+bXLz?SaO-gXV?YSb<^xK=K{7)`5J>o;QTrX*Q{G^ND7bf2XOR)q`D|=q@Vs+ROCg1vf3(q+POQ9isEj~>leVlaLnB{5xL&R@E!7*axjlnK1_9eyX?ryog#%wVaKB+<&+gCcd37>|dcO$@A<ly@3=u>Zz8xXow&<6*xm!HwhQMGf%kzdtf5!Nc^m;j^4mDeC$NE|uNYrQi$RRxN2FFbwE-;i$zOKJ^WrcXcvRBiTLF<W9F$qMpC1ZpGOOQIZZf4%yp5Vv?i9p%A|DmVBP<d0Y)@;JR?P9lH<otrj+y!n{N093CpOrD={8LYrBM5LF;F~{or6O{=4GHLLRN0*H49bbAlbi{r-I+#b3;!343q!Y7zeuRanJ^yu2q^G~5na)L6i^a$z;~i1IEC^C5jezk;y&ZUKqJa`u4hte$JDZ)qqc?=K(;al3l98tBv|!KgCeu=##%6bu`mfafoG`FcL5<Ij%0Z&?6&vXaXVfkE=yfCi#WjUudX`w>^VgefYMsav?}>0+$`fa+b^|(NwDg8r!%KN$f*;`u<<90B-d9Fj0}Rj3(`WIipb(P!nAUSg4w{WCLW)~nq9vGv&m35yn!~zADlOVGG_9Gugm#i39+23@MY%KQIe93>j=2N#&kshPghjaPJwx7A>PRHUf|qEr#md{_9wUq9B!44do)os0kc%BvQX&bfrQ;c9^`C<7HZ%zrBI(nRB+AOse8FLOTVI+)o~TId0r@Nm<VNc}sh_2!9g1+es@58L8a0+{X@fHpQH6gBk`BV`e#ZfR*0ZyJ4qehb=AnVnhT-1P{b{V@w-9H*4*!_{G+?*iRfdZB9vHz%MqN2sxA#>%+;e0(d(VgcAb+?=h(xJ~&+~uxUiz<1!7zXSo*;Cd<QNb}%NNS`@a0h^rUg5WhoW@O%<cXGKSB8MPW;kUG(@!Tj}?PEOz;j=v?et-TSde4|NKUbp5NJmEN2$asUXWU(v)WROhym!49{q?yqh{@uc+5rmZecSg_NRKB0|o1*<U3h^nsP4|ED(~Iwr#1YYK8LsL<!2tZ>wTXk`DD4~O%APNgowC^k-$1ye9i!3VD>mR7kr>}uLn7^)UhF}AWb;V!Alq<%@wdaBRiu@T(imz=w!IQI%bnpF+hO)T+rN?S%UO~82^;<amqs<x1qkqR^tYUCu+7;VT&eQXd2hyaq>Gsj0nT|(v=%w?7!C57|A`~B>7_VWiGQ@?DRLT=Y*;3*%u9e}W$5M}V)QoCj+0iXQso}hbf4SUwPj1NZj_^4xcu=ApsxZERdf;0lPL?<&}vf%`kWB4dTJlIYVB8<3@N|p5&c~I{>0c9$p!ZiO5;`r$72ze+VdVo}I$c0!#<i}%g3al-f1YAv!M|h0Luw6cwM7d15?x_52hD;GPx>IV&G?w$o8h4T#p}1&1&+V)r8q0@XR_VPf(7UU1wG@>*>W2E-LY~;Kgn>Pqx9Mh;NpV2XS)R}nbM2iWA4e5mF`yx1C|so*v;o)ch-VANJ4qZBP3v`%P*wJR2`}ZBT>wLU%Sj#<_*20ugTX4X0cp=_gs}|;ZV5awp;v<ZIRnqC&Z+TMZZS#HIH~<aJ8i8C>EsMsF(`+T>*o5<&`#(}Hy0sF7KM5Q;>z@@=qXHxl2MTM$$aBe86$f`AEum3wZdsK=oW<xpkwC^Z)PgGej=&#<+L<E8#Sh;R1mR-&ImUNaT<|+Y7`EL<&M@k06V8X)aIewo~9)&Wh2c>El-ma&PHp~VAPrW_qaTTzy3bt7$<hlM(M||nVQqDsX0|o)_NfeFR*haw;Ji~nxM1c(4IItYZier3xhEmnH%(_2*{I+K6lM9b94%w%p6T1pRu7f6>DUOpNk;YJH)1qrZbAe7Ii>oKzU**?@G4Yl`$1B?{`Mf*?p*;?%&EoX^gBt&AVHRI-oX{7?CgXKn-?;bi}@P|DZHl9PUXH9U1c>zVd-Jp$THP(m{iB*%8yeVbMXLV9QT=;mO?)>C6-0nTLuD<=>U}Qn93N&B*FSPfToY?#|z}VIiFZbMzNV>vAB&grR_$E2?MNM;jE>zQqdlU0WaFB@UF~vxN_Xi*9PHet26^tktzFM8yn)6b4bQby+pGk|Mx>!ND!U3_nf(Rh;xY#`w)Mc94_k6d23jb=5zhb*B-PhAew}GQalhtUhIh4-ZVlM$P0htHZn-j=hwZR(Kim^)FBav;1+<KF-bDI#v=-9Q|eXwuTLm2$Id-*7&sPg!`?8bq1860tS$(Ne;SI-oHUeBHI)#gJeMr@yLc)9&bw%M7u)A7-m%47+rIcS|pm#oAg&erBGXSBi8)A%qZ`rn+2eI<%T`D_>-A1<fNWbbF~#ZAd>RGxZiSvd*kZ~%g)7@!X}MgaWS0~es$|Iq5SI3zTshb=})7b(*iOV|K(@>4_C~>pS}*$>$4TdPhDPVe%bPsUh&>td>`gE9G-opRmf;=LswpX32LQRymuGg-B0BYqv+86^Y8WIy;;1s%lDePb=WMR@)G%8L%0*~j|@hS$ZYYww12SZ&%1o+u6!7$5A8HyusrM-X4+Xq79TqDRGoha>kqMfsLKakt8pgq)|IepE6c5bXyoB4+R-w({uLh?rBUOtwW!HtxRsE$kBj%3@7>~Er`neH@XUK}0mex#{59jm`tAI^)7ez6Mzy(;Adx9z1%_;A!*(_#et+pb?=)W28HGsR-e=aj5+y$Q&|d!_PpEtL1M(e%<%C35{>+Oo3(1RLey{a@>E)-_e+5pATki6ou(s7<JU~tF&QS{9mQs4haU3z&>oLEow#Xre-tcp=H*l4Ew4#<el%kcr6nD85?F`6c!gb7)^sJW@q`(jI`XMRVmNSeLctqfmLceV&n=w(UUb^lyv=tVBTU|^Liy=^l;j_v%r@&-c;%*usap`|tft<*hZFYc4`LV)?)8R{|G^jSoBu8yws{E&)THJ3+NdE&!5$%Tuqz(APu4Gx5Nyt0yV<F!_EV_|QC0*}e5t?3Y2IhhWL2K~W&f8ys0q=w^&%3_0$Lo9fft#Ye>5YL)|80B`3uF~vn<{F;GxqZDV`%JL`fhPl296Hxr8h>JBHk2y$5=F;;SpuH;$efW(j&Pdy{9CpW9Fk0HR2fswxQuw9eu-tgN+MWJMb6=7Q}IY?229~emlU!Nt1f0X9tKuh9Q&Bb?{z*EZpv=<w&$+^eSXaMN;%2Nztg5M4lYK`n-G}P~FY)Z*QXp20Kf>6>1)7!gWeLN+gz6P^8C#sBg6T!MLv!KOf3pTNdjRcw!z-P;DE%8b3X*!PJTKoRHt*|9thI7jxxH`u7LE-}9R-YAX?g<TQ@bGg*Cp?&Tg>a<9bp&x)muh0RCt2+2mD_>n5Dhq1g+L9jCiBTBbinNXHR#>Wz#zwyRA$$baEB^1_0dzi7DAvhCvu-9ngBC?<k{6BVZRo-2JI{3Kfu0dhJNcN3F(YZWqKHeSYmZLm{@VDvwe$lGS@7G>D6S?UmCBx$-v+0)a(+gx!7#hDHu1j>IyvY1?j;^gy?T*6sI*uFC-`pZQareM5JaVBS-O;xIa1J}+Bcg1fy~8-mK49*Z(K6qFM%|YK;t>Hj08)eI100nv^w$Rg-NR${TW)P1%XjnB^erB5F}|}yHH2z+^gnRb-6OV!M=7_04hZ4281W74yFJ1NqpE@fs@3QO0duO*f<L0HXvj{{&MG;gswK1U`K#5B=!=OVAg>AcN~V$_pfyFG5z{7)J0k{w%O;JG8|$Q^yM$SJ$FfEkG?BA=&mBgbOoK_(DYb-jqSTs3uUg8$(ElMqXE2ZRFQcS|eSUu9;sB-LNY`mv)!qu?{e%64>lhQg%QG`MU{_D96wB|odAm6R(EthDuF{{T4L08eeg#%47OzIcr`lE!4}^F+{v19cq#d(c4NGW8kY?VxqorG2;RaxZ*Pk>WI@{u(e>>Pr7!W&QX*%OH;gWon*2L9UnN2W!jogHV>L>gr>ghspVhn78)QRY%1>ku_bP@}WBi&*%x+x0EjUX6gKcSuEnxo}2b`vS@g5?A&@GpOBp2l@znOIn5knDIJu}po5Ri=HGQs!Z*Fbt^nzCo1ngiq#%@c9Lk3{zz6W2yPJMk7NGnLquFcP*#}*S$OC<u48QREB$44EK0txW{LQd;6}#eRqAhqmF|zylsL)SiX=w5RUuEald*X02Sz&tVx|nE;Cd%`i1pAx(W0h+P-9G#q_hO{uppZKU<BTaAp5=9oH!){m@3>t@Bv<jEgK~*6Z3ecr1Kc8#kZ;%&HCKdLwQ+a92=Y_jy4_v1|Tq2j)dQurVpRC!jVt03p%t4i(?IlaJKu4GOn=XB<2m0EM>vZzq{e9El1X1s*nATyYZ-)$a0dDQlcN@sM02sqB2Y7U`n=s6R2nmi%n6THG=#)zGQW_X|YQ=o+439M~k}im_jIh23Q{!m@M%BI}(i9LTf)M04YRnI}c74L2A$W)L}Mimk(I<h*#uCIItlgGBF%7B!ZSJy2>xPjJ#`l~bKE0j&!IBwtY*0DwHBd#$AJ2y$YwFCTw1m22G#7e`+<xb_BY23xL}W-roIO$v%8sS^Td7rdk|WtJgq>=`?iJ)#)|yqC(pNVvD>Xs;C-@D_O-DE^uMkRQTU@#!*xvR@UM`$}ZzAl?Rq3p82)?dm$7s`X^^vk~4{voUU)#1D-KJ#gka8qPON#&ML|D{c1t!;WMfGM5VwOc^~mWg=geQz%|wj~_ZQlOjebh=T>3BJt~j!AO9X&@^K_*8=&OBk0dPeU84rTHlnX+#?hG(Md=BiA&-WK}O8`m3OV0H%`*;D5mC5cK8W4Bwy=?c+Sjg_$Q|q`hy=Zd7eDeXPt`tm_$3v&fv(w_3X>1n)o0TKo|stkuD<QH$1>Xb7&!}*<dBBJ`>A%G?RW$b;5|-Q9zFZ^)93nxz^gM_F15hgST9OpAvgJd6n)oDm#$V!F)!(FN^fEihUo^u#JUzd4L^;zshoW;(TUp1ofYHwsJc=zz@L@YJ^kuB8I9(KZ9F+at2DNE0qRfGFkQ;)hF&rS79P5wOAo&<XW`+skEw_TcU2XUcFghquR<(g{)fmFUvtM&@4SSpAU#;8UOd{9j3wvwqWZ6hxFzPQ$a|GVLcTPJ91AHVBKm1a?@<UglMbvY|x_FU7rok_1l+bLoK3;xsmJHfGSg99UGILzcd@%SS@%6R$LXYn+lwZ99C9MnCC>zP+0Eyr}&zw;BG7H6N^mdaWpLE0l#PE>XIp~QY@UAM=U}uH_+30fXo$;6QO(KB#31a3}0;$G~Q4?0tiz*GybvJW&T+>gLxR{T{Vv&>?RF}t)+>Za!U@hp(3N9dEeRR?buxAhrH~5UUfI}WSpSs`6BxxVerxXT%4rw-(z|?jCs7%WW|ETut7~2cWb-Yr;oz?$_3`OE5K@)xc5ME+(xW-V8kX|2fy7ZQOqsdBTB=B3aVpaE=Aw*CmZHlu<OwuqdN@jdERc(%`L6r%81z_5xbFzcWi&XSs?V&S&YwLW%oZut8R^Z%EXH4HBW|r`wca}B)@92VR}Th1LoU<=v!R8MOgOxl7sLlYlwF;ZCDPhbS`hVKXRKZg`M0f&@l`lxb0D}eS@O`>zs$k9pPH!EWm#^)fNK~p)b~-*kOIX%1uy=Q;-r-JoQA!elGYwK^iKd$fxW0P0Oe%8yQsJ2IKgMhPBp=DL0Qs?ry7AMHmhxiERr4q+U~<lO!8GeeK3QQ#>MsXBrDpm>V%HSS_feBvz~2Ujs?-o7@E5Qw<{zXU>BlI|4gn)+dc2Jcx87mto;Abc`J*dchu$RYp^3S(3F`*%)b4Y@@BlvMdv>Lx{k^t4v+XZ{#Z1ZAe~VSzP)EJ;-3-M9|)y{fK(uK_p@SQR4>^fnHpp?nrG1w8#6y5$i@L(4Nw0dv{M`^q$(wojipB3}LyshskYY95`$j$Wva+R;n3{Q?&;0`oPH3@Q*)7EXuH<n~(v3cCJ}PNfe7IL6CuV2j<EwPn-6t_7Nc=)s#r6uPg&fAH2nOx7c0*q!-P!GV$EcIe~k`;)Dq_40>z0zI<lVgE@imQ1|R-7M@<mG#0Wm{b_NUx{3GE5%gu0oT>m3PoU9B#&X#7?wu=4P}8%bS&Ln_fHtdw%yb5c)CuE+NW7@Xpo4|abP{}Ny;8i!86#p#qt6WGCvkB$XJMpJ7(JcnGwo*GqzNc$88LKPtHQcr6NBd5PGjnH6XVjv{TakSdP+5Fx9n9f;za7`myDrdaS1o~hH;cSgKka?fW{{p*T1rZXHrtJG`VKMu^LOOrWc!+O8eW1Rx}!ciQJgQ@vaE&STp>jxKa2@(YLKyAONcK6EW&Zf6kg6V*0_6U7W8n>8abnVJ3WyOBIikS7A0=K1z%S8&qK&euucLt?QfFKv#@u@4hjQm89_vcDRXq2Kz4pRg7D`Z`ZX3g<5`j8R)Xw2?q1-4L)pRKCBG)#f2sxmV+&-R<3&4d~X&$ERghttERD1PCUwSZNzKgSwdC2)2$IB<i@?Ht+D?l6lMHWmAAd|Qx;|XZd&SstK4EL9P(~Q#-$MEV#+T6w~HhF{xR?G2b5RrFr~7G<;QzO>?4Ir4%s@tbMhiua8Z(di6_~zf=~IxJdE--y5EV2T_rX6{;)$#P2Qg`nbMxV<gp=A0%QjUZff`35*o&~jx=l-I+RbeqtPEXj`Y-Sb3<sB?II?Eh#bt3p*qejPx`v_P;GHV6emXGP>$)B-z5T_P3<jvv2(+CW<?U*aV79fqIL@ZOo3+vBzIL8E(M;Ch5J>3=X~ooZwNetjb;>`5CYF|24U5@vBQNx7$nPa5o}HhHb>MmWb>dc@#eISH|Keq*Wy*YxjY|*oWX+iH=F9CM)Wr?uKTeQKB}63?BS39{n*1Fd-&V;U;nlI*T4C<=`DXv-$a|g@_*lx{qS*=zQ?{zU*EOT-_L#P-~8M7?0?_%+rNK0*1NCtU;j1zH@*75tUFU2#{Ro(mHs>Z)xF`rtIzILpOIT&&D5*k@v948#`2+l%L)DEcV93-7I3BDj(y(?d{j*}UtW?li~pYJep&c@3b)5XAYD(NS@}jh5+lJ%u&8u6D!9Ws^aa>{yJ4Z&EVU&vROC0E@efbh^(X%gx=qpB>P7B663dx<{mILxNzH!x##EU2nnmyZ;uwp6$MrYvx&La5pRZ!2`jtwymu+y5)$-DT&opp&OgE+bI%$CY#Fd)rG<6`aGK$2aCh*L@3}-JT0p@SK3E|EyZ^|(xV{6|BD^=3Vt)D`XF<$mer7*3X!8tY9E>{{5rDVm>Gz$f)^VTkgirtizlC3}M-F{+!okzv|{rm(^TYEBi77x_^YTe=%<IR<oVQyy?l^&5^Iy)hXF9gpiv4Xk$%Goi>I~#^?p{YJ8$-8Un?tVT%pTk1bJ(N>P^3Npb^&y;obM0M8o9B-?e?Mu@e3ha+Zzl0lj^54R;3xa5YWB}H_4@4?cgytIUpR7Z*tJXOfYKqe7MNe$0zUiIZ_jQ)h=tdDIsIuG0MlW{_&E)v^3D8Zu;axdZXMgMj&v-4*8B3et7FRf-KBOu(`*~M<*^c-xcF>$WRyUcpS62K2fnI3S9*SG?R?jroBGg~4)KfQPrjUf?%nD8)PYl?b@^er&t5#hc5~%#R~e!|WGKf^oj+cs&zN(k`TY~7H@53?h#P`Q2r|4+AYcnU5HeypH}MH5I~HIJ**#%a+>!{(8H2X)koCsJ2@)eFKIS%B<ENC89!1$%SMsSmo-I?9^$d*Z^3E{$c4M@i&^YXXp4xLvrCS`2sdsQqP4vsH7}~Hh3si~A9UW;Q@spd}puvT%ia%5R(Klp=?f@{UNm2p`)?<~3NC7T;L}uC2M0@0F;sz4HJMiQC?&uy$)$u+!)9Kr>CWn!w1M_o*tzSlx@rxBi5t+T_B$P?L3gf`tMeupQ4Z>OpD2_B3DePe5Jwm7iPqK;N2x*hs<hJdQj%_>z90fVs<0tueFyru??iT-TNci(e^~-MWZ=>rTk$8nhN-qrwcbEHlM4{~{KBB*TUXzgfjLH}&jci@qlI?f&v2!t^(3?>C&yexb&}xN=1g*5|AMrq&JPwb*)>t-<2Y}d({4W?1y<-7`C_0=Kl7?yk1mAP2ihdP{{3vt<Dj5LK!4@reCrkTOa?pufP!c>hl|*GgBp|92Rz3tWvg-RNULKIiIVD4#)vn?sy)(oQ#b8Kz>I%Xm8WU3_59%O`k{xe4Z&ag*e8^^Hv-Vf@UzBVBg&}U%Rjh)RZm(C#JOQIsE36Pp4Lu<P#%xHSuL?70(6ju>$!95I6*Zt9HHn6l{B>l6W-T*FbRwy!o)w5*k-xN5hb9f=4CV47>LHrT3r`i3*gvhO2@!bY6AtnZiHwqDy|*<+6p+2MqK_@1CI%Uzf-17vDC&TV0`C17EWI35f>z{t3$2~rqgw!w8Yh4mOIO_37bY6RCM{qysXXKb5nkaP#*m!1fnl24i+^#wAMhl70Dl#2eKUjI5^-d#^5VY)#$}d1j?=ZL4Mv!;wZb#2+}m-+bot=Q4rJNz>GOO$-pxp}B~Wcb1QBB(%+*OhO!rX0X#yHeg30r*>_T1=bkf{5)nLzb`BF0byu-<-<x*2f)ZGf^G=a_ROUkbueNm}h0iu?mFFSv2<jaoubgYe!q*vYl(YJvSdP>(g!@1T2SQ99D;Rcc!oB|VerS7n&MEVSAb<}Pt+jgL?Y+gQg3rK<oRH;5*1tZjFV1y(v0;v~{71663(lAV51ceAX{DhE7^xTlQl6)f#um%k{K!Gt0H?C>8(^nvh4I7|LfTIlyJOZ>l0B&vsOC{ffBL=)}Kr<Qt>N^36v)KUPxcuMP6Pdqrwu0~`((Y1cll`N>iA%57Cs<;jqUr^ZxD$}r8;babDB`$45&L2?g$YF*Nk&E>vA+%^CX&l<8o${Xgt$WmGa<ye&pOdx!c3aM!!pCllGyF4Lk%z72$7*PRRp~_yPht9hpiB_hY|_b&<}?n_J2ai{`fqyAC#(9*qeA~wkjt&l-ydvU__@VmKa}Tu1KQ~;y#xK0C?Kk@4*rRI2w8GVB1B|w9Y&fSUkZG;`hDiBs2{~>cHY?;`2PMrTl%k#h@qF+mCmSI!qWc8_}WU-ybC)jdei_6bv6)A<jr^%Dz!8*3_L7OrM;n*Z*xGfz>>)w8)9}h7z8W)YS9;SRR6y!W$u1pOQ9a1-W8lPv+Zst*@zRTis_;(Qmh?_?_|k6Y$C)`xlCSuVb%<CHAT%SU<XByTV>Ip;Y`LWI+X8*vu{wgmv#Z*@7Tc{%~{+BWo$LzGqSNYmrnw%-tSSE1%$|fxsK8e1GL_UHd?!T4nXregAARbzc>7(^Ur#>R_s4xswitR&~|wzJU(Ti_F0N<U$8~g(cO&M{;$XcJKkk<L}bJ|Imvy2-f8?T+a#+Iw4c(G&`taQprcNgRpl#C58cm>AO>G&xpl+iJqf0p)U4>;Pg>KRQTWEjE`mu1fZe)TZKO>(p^^eJ4YciU@eJ1)YBFN5_o*5GfmoaEIZNgn*?Ucpmp9Z875Ilu#pw=o(1t@EM}x(_!ppbZ&-A*_d>Ck!i>7-H|U10K>E#CU0Sx2eY>z@aXTVtkeThxH(stwvxysu0U6hpst*%Qw5_7Pfag~$>15KER)xivm*O=wbqyq%U@eI&i*f#Z(i?@p+WU1=t-}`=vcqH+7fYUAV^oQO@l((JZx{0AJkPX;zlo;%u&i`&3xvOHdl<<LAD)~9W0?-8M)kUa<Fw?&FW!S&R=Zg4O&NvbzxLWXz6Ue)qFItvxN~`<s}HE@>q1@}T)O37G34>zywbIMlnJz~+t}na^VTv=7De|#fgn*@9ZE){5pVh(0wxF3=*0KKorSLUUTj)H>+JqGVWw3dH^29H1~P9ghK1hk??~H7>A7vTh>ud+aY2+Jkh}@?9VRFaxCy>glV~jGHK)6)VhF%VleIfhQ(g?r<Bc;~e6ikAkZ@&V{e^dA^GNVuTJZtiLbCA!qPi({c`}u1oUWq*ROdw@(u$^A&WJ>*%k#9Q4PDKmyg)<xcvg!yS<(KA3EhD3s*9kFll@HoLo=as+nT<j*dGE39k-qhAN##yp>$LgUez(W1`}G6KqjH)(-gh5l3@ebhgBgS&dhQ=B+8_Z`=QL~_?NF~M3I@yXa>iLy;m|(=q<!0B8A}czKOAT!zW)e_%~MEb3&N%!N*Dom7b(D`546fT9>RG#RMXvRHJ~UcSbfTW<TZ4T1;BZdv84rcP?>*?W#KYuE@})5niQ?h=@WRg!yWoC^lZA(jXhrno0G>P-EPQ)(X^Z!K#lthP%W89Vt*ANd&E;xIpn{>b@146lW`R9#9}1_NGt<l9(DdVv&?EXX5pX)S}8aDgI#F+~R;*`N<F!0aMVKbc*>;9g~VmU?v0*#Xu>mgNs6xW;;B;+>-DY-qFO=Bq!@-USP)y-g24YiPzK&U;4?kP-a)zFa6|Im|~jV<|IRA1~WW_R}@dcLuM6<YTVIBe#hsWd?}%zuRI2ksG?M+sbySpwkJ;Yrs`R3n@!S5=cQ>BxUkxyyEQw&{*(ZpQOpnOGsoY2+ta4X({Af(#Yx)o*v~7ky^Pc{1X>J}9T6yPzbd=lVqD_+qu{#nqhCCK%8)-l1Xe421GVDu$Y(A`z>&3Q2co?nODOFcw~UQ|ugXOTler({efUut+J3vk6v2`g6a(=G2;X64e&mCF>fy&rbNeyQD&{8-Fuk`2_=l@^h<J$`s={NmkfH)zH<d6EuZ=1$U2aPcW=9E`z>|I0=_zd?#`D}J++qm?rC4MfD<L`sTPiQwP;i8kSL4ZG=66&$0r#|0e+@m00Z(Zl^Pq(e?`>aA;8gG$l`%15_=n!S)&+M=rO#?N>@P(so_C~M70X_8q-R=z*SgU4sq@?w=ed>hd_?SDc1BWJ7+q!g%-qeWy>x(5cn8V`m?@u?{=1=*JT9E%^c!!@nj);GtZ9b;Po2oBsC6S=SusG@fIT%E^7Hsxt{dTO(FoIyffZv*KVyF<IvSNx!=cT+H=BYRc46K<yf%kCbQnb4fybh+-1o9e$l}MFyf_TLX%)0)eI52PC!RxFE^e{Qj<o%syxT<61j{>KzTC08x?HsHZMpcfU-#~AtgWeg-R=%!Yi+z|lexKMynEZ)^G}RO<GSTO?dV+(S<pJtS|?%N*wb3){=L!uo&V}>3-3gjvDm_gNH|*|_&M3aw-+?qV1<6b+Ti%#yzP<ZJAIVM7{h{k`SnJAa1?#U^BvuFL#{>i%H||%-fb_3PQ;7b`B!q)HoVYH-X&USQdq(xlyD(UW28Nz+a_}_B;|mmZ&y+v@Z9*Nh{mTZ2zSW5xmY3u+*M$ic4b^_*IIt7j7TVfdB`on%pcviz)JYhSMucsj+!_6a;+S>4nmQhw6W2kmrF+uV_|mTJlIt_B3rRDBy#k&ih|&YAvn>)v(5+f$^17UD+5T|@NBV^(D!Q)RUkG<hk=+8!B~hJnY^5Iy^3%oNJ~R-lYU$D1^yfutPN~ok%>#v9Hl1)z*3@fNYV~Nhf?&RfkH0<p{+bS^y$PPo=7p{{RCkpNk{~LLy+os!zkWA=zc_MN=BFR>3-nC7=h*i5Ih*Q#K?$igNSr>^zj$kkR6zs@~UG4ZiSJy-S6@4_cox|YHNrMbs?k}#yXB9pwbX{bn(Y#6)bWQrEK~^>#J$Njn@tcPCp?fzyMPnMk52j^Q3=N2`*1h*^dnv9|GBxgwuiLmi(C9=hSb_E!pMPCNb3GPJhwC70dqnz{#=Y<O2<+(1L`4)Z*UE1_94GDn3n+0$A>%={>dRGf!?_qF0zA>x?Q3PcJ`M>_lYHs4Y-PK76s*bF(YV6d~rD4cz0R0;o818+i2qKOL}<THq7%eCdv`9Z8rSKg5XP8NQ50WtYcCFEt5@z3E1Fyy!rDjwuE(<{j8hQg6g$dTqwv(K2ZIB*hFaSdpat10Ywp@x6~vz28NXzU%{~Cm;k2I;o#${I4-Wp%4UU;t~}t9vf1Pd;*bLl8bi|mKW3vF?_9?4438G`AH}S1}>Ksf&M0=aa*X{^6l*N8d{L!(tP*iSaA5EV=zo7$8Dw%p9;D0h6a~x=qE0tWKo{hQ(pI*SXKYb*ANUnkCR-Bgs#J&WBuwFs4u%}1^4*5UA1382NKPwwrU6l%|7$Mi03dxJQ;K9hH8Y!FY|NNX{@t5vz`Ve9~J=+kV$-4>*>$W7)7x%e!}JHXh^lAi(ABiBB?C%yOhcxr67!AT8N%C2e6Fg$<fnI6`@$Wr7DEfCp-@81#8?0G;S<<gdnm2!WG$#+DL@ko~j#-c#4@FYzZtRf3Z+};PS4SOstI#m<th6eZjH>f*mGNqtsFnU|L8kOM|hNH_*tkj>vFnZ6Y;>4>kB5lY-bEW5uN@FD*)*`DPS;&cuMo%>wr)AJ!!BLMkVpZ=>$fp1L(QC<sOcfF7G{S0n&{*|At6qbSlMX&<9lm9a*2P5?+GG6hq__L+!n>lhy8-DhvHuD$;|ubQq1{9(q{M=Wk(Tg^GI9^19>eJz(hPGAEW>QP^^l3|a+b7gEXUuGatOky`;GS`rr_OG;(y-io_i~cO)Ii)olo7?R)w+;3Il`<=osjN<HN+vGytp!bI;<E%Id+Jb>A&;BN4eo*coN;ect#!GCU&8Jty0(e5jUW06i&O$1O6PWADadPDYkmpk3)M}sEG^wPN6}$eSrIlmF7a?ie0Vci>TPLta7DeuK0K9V!IL*jfCO7GJ6mT<k}Gn(-{9Kx7vFQfZQw4G*ZGFK4D5~<l5Kfln%OlW)$^uc9$X%k2)0z+ri9|7;M8D5&WpkbULrDYGv#(mF3W86?U-^4CFRyL<(9Ys?VnA#q3-Q$8**pc(CzHRW0TtRG1hcBK5WX(|E-UVO7DwN>0_^cq)7SL!yo_qv4=nQ@b4fZrDEf}>F4!FE~SrLN*}qDK5{92<Wl--gZ3kx(zl3CY5nClPp340NG~%g5dl;JTi#&qrPe~ZNgWXo3w0_8iNH^&L?Hzwx+cjAXx<=SLj?Cs5yav#k>U_qUb&h7rcj}{iJGW#3r3$%SdmUChzc7}JmFRHzFCnr8H3T9RO$KuR{oSxX=dU<hHU17aue0ig1AWe+jAnNHJwjofLKQ@RFxChJ7x#oYcCpm(*U+AXDdROyVtFligcd&fOY#zImdhp)q*X_9?C?mq;JCFi4>ZmDokWEGXd4iMCIJc81Te06pfAQ<bc8`v$};7I;9m4)8g)oB5S5ol2QrVykJh6K2&ZVY|gECm@a?0qN)mZ3;YsU&$+e-H9tiF<N}@2{AKwp3YH}i(N$8ViGAvf1n8VLY35aWiB9Pn^H5kc@`Tgq{D8}6a7Mf|)9sux20cf#b9&uSy|vk2<$xtQQ{_)O)1UV0`Ux(%k)CHxx<&{z9WZ?`UY|9olJ_f5HU>XY{@Bn8HpX07{r8+mX(n4*4$;MjXYTRZ9XYpp^k;{8_m*Bd87g0;ldt_X7D~UV1JR|PZfW78szP<G>z3bC<%B2wdAT-k$+zSe?-LWpX|VsFd@H-aqMq)&&hE;;X8qrE31}Z*ea_|*u6B`~M0xsrZ~^m0%h`2{;=8(}@S18xr!oK6UjY2MMK!&>wwLjLR?9J+t$hU$u=Pt0lkq}VFNC7b|DE!akba`18uR_`j6{LCpNn;ix+BZ30;_YmF8*@0<Fya#_r;@}VT&vk4olIcN)M}Ym*1a%K@j|ugazaWl@zP|^6?4ai1KGaAz}8O7P_piSPX~q-?aX#yC@xX(vy~)MP}A5@gn+b|K7`H{zmm1t1@xu=LD-1M@!tQSUeGAnZB#BfGIeN=#pIydXWuGecFXMM~nGK6+2bb0Kma>HZB1zK$vTEH;u~UXp?nTc?28T+!a-Y;hl&)VB%7!WQK0`rFffuL<q*6Gf+>ekH+`dyU-vLYr5CL7e6ORYN|qoon-0)fRLjq(LFF=NSN19amqitk);^ydd^RU(}YTrv<!Pg2wi}RZ9`b)rV&+vf7B0<oDSr|0p8D){SuybPz}8t19r1^ahBNS8z*2b-v#TljF)E50l4EHLh6c|wSbP8QlQzKz1LjZ?wpnJu~d%ETP%<S2w8=iAGb!lM8P+z00+~43*Z9E_t@a-wa7A9_HaN8DYo{<zipT@5uk0ZE!KpUg^PuEC&;p`JCc@*MYSZEp+qa_MJm^C;iWdwWG<KZvNl%z8ef)-W(`l^6rDd+t*>kBR=hO8!um}rg_IR)fk5o`Z&tsBX<4iL8xEr#=p7Ei!9unzq{m9caF0hJe}Gyd6<QpR*$WR%%kcw86-SPa_2r`EtE|v6(z*fdNxtqL^$1wKZv)ls{R7zXOnu%Dc?OEwhobgGJLQJ-t^X94bWQ8i5XL%;W2It$sJjKK&j$B7=<a}j9f{Y8;Qqs89}Of4$@|>Q5mmCh;u!kTeNJI1%$%O9(!}JzA5!lZua>ASL?{Y(T?{};w-TCd$tM_1<uL!rSlUoeACfjNUrNnk3R0{0&wj`Wkk*x_WM~{wOm=<rzi6Ro=%X-!c;qtl69HwHp_S2Sg=b{TJEAKwNp>H+!t}rYTDHo3Fwo0`sTpS@QoCitx-JO4#j~xl6R{iMgVHT)sDy3%WM>kEQ;g;6R=M?bGn_Gqu(G?8$pS<YgA=vwx1?bRq(8H*@5u3mb4OnT35kFOejbUlW{@XM>ZBG0D$~qPQj!0X2hcqjytYA1tRc_5+K-*PiBJLlG~e<Dw?od=;2W5XL*(9_7mi@t7Y7YCH?huBg`8EIrklst);FU?fqK9!gGDm2Eku><w8iw_>sKMv?8ZF7dd6sWgg0W6_fwdZ7o$G6LWl%~vU~$&icvy=tpWw_v?Aoe(!6>_=!kxuR)oA`)b9$j?l7`;FT$+H0<&%k%o<D=n2n&0GOU~AKi36oS`qRJ!n&68Md7?)?dDR!+V+D&uEVdt;gS9Ttr}TwEmjQ3QHtx%8+em65f%BE)<DM_4A8t)5?%{-SJ64tSUsH0=s;7W!7^KOQyN4gOY5X=ST5|1l`W36b-<2`ncGeD3=U<v9eGsb+~o5&n>^cLs~f8!YHK*qM!#uUucIVEfJk)1jdUMDBixE<33h}pj1H#0InqfR@|mL?WzM{a#=xhKDA0i)97z!uz)PGro!IDB2_oME*iE?vQ1!xOXj#(hjQD{yVp#X?-(Ds*Qt0z?nb@*M40d46{jXMy*oIGtF1Im#Fbsj|M;?%k5l<De56xJo(l9KN9o?mN!=kDRMdqD~#RjNTbaJ&KwZPjTqg@0a*k)O}g`yw;QK?8=9C3z1z|8@FgzJCDx*WO&U>#K`-%S}Ex6qunWKJbFC3{h^^BRFmijY9>%XbU54{2`ua!kJMv7%o1l48|s38(2~KxuRzm}<aF6SX^3LVO2j0aKQnDL2x*mgsEYp4{=VpUAA|C9c6k=>yDTQ{S$Q!7N`lY4}bgX3@wAJIh(oGHff;`^F-M#~KSmm&FKJ-D9^Ns)^>Ra|;%-W$Yqh(t2l{ienT#B1n<_#Kb(&Ef-nsqMa=+wS`=G(O6&oWI@Qb66T(`b9us=1aBN2LewwX8P@9IbpFG{oVKJabIZZCChT1?hJ|S<EP~(*a<(FIt`<gjLb-d9SZsQ5q8AI|Z?$_2b2qwp#@xGPKc?_(8y0+V=WLR!@W^9P<rRgndci^#jf>30&=(`*{4ONyPMz$+nKO~^__=vrwQA1ILEjjj{={4NCh!0eUjj;$E#1Dey(wMVn@|YUqjF~OB!T6wgdcUbAIVAT#TXyU^4=H?-vh53kKByB-#W=5dw+vE!kX2GJRwLg+C=hskbURLidtNMq<;p}hF)*p_<Hbda0g+T4XG?6Z$Xuv+m=G(l{t(0vIk?IM>P?LNg$W4NZJzfcVmw+gS>SkwG}T;?r<ar1h*jufQ&9qLEPa#eVf^LOIiukqS5Tz6tj=H!&6QPnSH1@KI17sfdbA0UFmLZ`Q>LaTqYTNn>(234z`m!h+f?1`PCPXFv0W%VL^j{25Mu7!yw~Hl~Q&Gt5Jjn<ZFb4Gd-I0GU1S@da*=*NRROEeyno%s2lwe$o%oYAA9&?4}a|8kL3>Ux!mESbo9q^hmYkBAIlv+mOFfuj{Ybe{nct6ULzen!@X*r$7ltEh4nxm!w`~bH+YL`MxmqXIRJ=a2!;^13_K!*C*_AA(ES4T&QModu<c6$=?Q%w=8A_I<-II@aI>7V@bw13H+|Wa{PT3M)TZ&FFEnCnkoyVj-CvTFR+WHT;^of@BV1SsTD$u6%q#Wca*r#)W?!AY7n$nie^>B->NktuCvJ&`+Tj6uX6KhR1kbBYFC?X%4`-^|?o?;myGt#1r|)Itlt<817u$fj)D+z<D#NTAoK__fC$EzNh*H18!VzzTX3KJiYCTBK%O;lnzZ9rGy*sz4kg(DdDqH#jIIEQ)BVCgP<yVyulc4VsjeY`nzfb@Xu2(<AGpK$%tsZdgvvmxY>LjKbon;xsGap_ohN$Wp5%125A&MCJ%Oca&iJG;4sg%LL-1ryjA;O{_VpWRaPaC#q^P4dElMwRq!*oowu7s%kS>ZyQzY#D*iY60mfAx71kdBwn=`P{--IaD${@Id_#b4b?0Yv*;A;|M(BG-EFq=KZRnJ)kL+UM$eg~ZfLAYxp0^;sRsx{$&x3rd!qJT)nXs}S^a82L($XBF4~$4rjri)wgu?Ppiyc={?GlxMEGFRDOdSqOmbt29<!OU>y`b!hzd9?6x~SK}>sod@T)2js-5;|m}}+~Hs-K|dgYu?Nv6@-F%NU7gPf{9_!EWf`O2Q>mld`E6SrE7#YAE+5dnLj(1zZLInh>jdCjZPi7Owo$xm7yNc3IUERR-2Urt$V~l^LS~OlhaZr98R97y7dZENvh<Y-HsV20n}NIOL7W|md^AxifT&1u)=?7=;9H~7WGd<gl-UA|^n#My00qz#6iHA&ZM;yP+X-zIe7*66%Q&4u`p=y=!_jid4cefDWWKu{B@H)`$$tK7ySMb9m?g-|ha>ZOnx4O6hVZ}yX@2s6s4!*fDcemQamp)H{&<8HKXUCD|8(`66m9yv5(#3uCp{w@LQ{WM7T)K<^e9R%pcIn$`UYai39>PW3I%P!Nk0-pxUD)8x9)&q1;1`Yf{gfaZxoCG7>?waj)tV+4}quI63Ng+3QBs>I+Bqwvfz$@0injF^~M?(Z&=^R7Zhwn=SrL(2^wYI9|{ULRVy5Vr|`Cy==1`a&?d^0^O+2-6CY&DCIuzp$?TbLP1#Nj41rBlUEl!PVd#k|RKcF6e0G6ekU4fEv~#Im`U7t!B=2T|dDB)PvEnIeZ+}6CB2dO#$=a406!ltz!XK&Xjd6uUtfzp2@OpV2i37!Lw|Q)WS{PEcy-yp;O6G3Z1L0z-wKp)Oq*@E_?T#5)`WX!cIm3pDSU%wWgviaWBSuFvQbj$O`UG<8UsnIaSC?3t@K*69T5bg^OcyC1K$-MJ>z#KC21QVH)>2j!q%io2oI8LbG<h;SR{~yDd5&O>t~ur-<}^T^BM=EuP7t~}77SMasV~`{(W(aLJjjG@iV{1qHaI5XCm7NxFXH0zEVwCFb&OoGP~V2a3aIj!FM-7-ls|cqUN+I3Tl&9NfRbl-ud3zf8-GnI+Uk{NmsXsR!fnM1$1mMs)+^-a68!82&({iW7F&@jlSJ2r01P2az%tJ&r_L3PNHzc-$G`k)&099@)+jc?Z%UU6E8HF{avn+Jqcq7dMzFY6rcVVD>-^0v1f~wG`oXvWQcQb{?H^-aO&(aGNKQrE_rX->Jb}gcQpC#-Yj2{LdDp&I<pxfOinBak_N-3G&k$?j0h>@BCZAg{o}~kK6$u-GfzKNX<a~)P;dTYwb3Q<T@5mdGk^}1(Lvk}y>FGZzUF6?K9)`wKM=$+*Z(GlXndEd3SHrBbBUWCmr$W{cJuc7k0AS>{f^G;%^RX9V!5D+Zb3MSPE|3iv(3?EAZh>_hJ*P?@sZ@HI<P<P=0n7GXP;p?kiGcZ`Od1*C3q$Kh;+Gv9Qrba=PNjQ~BBi_w`huT@3D~NrgV3bTNf1=q+kszVS8D~8#k{LYSq@1{EC$p_E<hmw^@6QUW6RQ3y^1J1p`noO2s_)qb?^}|Av>60a<1rq>21%-vxe}FHMR^&HKW<|S2WBf#cvN1;6wmXjjiQW@%y9_)}Jx@VoJSH`T``pP`}9Ia*yYaF_M?xL`YHo63R0Xl)PP_UWEsBd_StN#8^`k1D!R&MA^*EhFeWp<*|k$7AuV4Ei^4GA5p}Ab`4cj!`c~1(!P+mz@`LL(R-7%`A^>V%y$cW!#!(nbZ6r3ORQLh`T$q0^xa!M>fATG%cVo}qkd7-rY2CV_ANXSFJ<L=G?dt`5+5;vVgrF<EELdA(xQj~0w{f3N_dGL%tr>(r+cwb0Fm16g963Ezw=s&*E`U*Lk8o<^^E!TdjyUHwJ749yA6_9;KqeLPz5qDgGMN+R^bS(1?<#Ph~^HqJvzy^wnc#wJHt&`f8<o~`xa`e{x+&;saoo|=I@VKolFTfudpK};g2or2BQf%=S}g4`QW?!%mbBUQQEidCH<<9O5mQUX802B40+8L2L3*T{f*WIX)>8?>?FyJGTbc|-4-CpV7<|Y2)ghvdb_U&RUV;8k2`RQX09I2A9=HE;3PbEaP=@LsL@J3T$G$E2+aX|S8iRNv7ODdO1M}YaFFJRO|!I~W=pZOw3uUQnqvX8_Sj(6C0ZE%f1b~I^-C=aLb%=e&h1(^0EtN=cVFe7=W&_u2gRFtzU{2@Qc+FY+&lUjoIEPA;i?;I3eWvo^&>*>C-nVy@IYV;G={#X)5}qwU+my9vdGQB4@yA?z#hv^@JOL__yHppkZsJ1v}^ZXBMk0uejyl;*K+)_#mY?e)O=*izXG=Jzk?!W8v7%KP^7Rrl6fCceY}6cV@5s-FVH#58+)z>R1Pq8lqe|{a`!|0i~|E(e(kqr3g)ZJ6@Y8o(8}4OF%SomA=>7Jt1ZOvDA+{U0%ghhDdlxIH)DhiPx;lnM&Z)l3=77K97PEBHjBK0vP1jl-Zp}7U=!M=;lJ9Z!TQeSreOf%Y)9{3QZasU(}*VD(QdF~<Q~nAY2J{X@$$n=-k}k$nM%u~q=MQOe;6PDXgfxzV3=(r27f^d?e<b>+3tgumib?Ovnk+S7kW5<s$nUG$tAo#d#V(>km2{0o~noHWZu#9Q{D4%K|6Ts`eZe%x&6(aPg_s5rl4cdGxMxB!y`>!?RhpLdvPl55~&#W*f)ap?`eQBcz}+llx*IFhh~b6(oH(S>(kJ_pex8|aDrK59p7j=^;O%N+`whLJ`_`~s0N>O|LBg4MI%z^S+W`M+3@;Z5g3d`U{C_Vi2}g^##qxpT?_)j?Hdd*Ss^FW$yXxNcwaWyzxy_=PiLFGDSp0HCU{Lw^jgtRhl5xC6-7Tqse);?TewyCh#U>l1&02w{|So!e$ME+6oH}j$uINny1hlpMHB4+r7xETY(%Z(fLUOs0=8RjQ{7cjU_CKCu4R9J9S`aseU+u0@8f5<C_OOx^T1hgZ;@e^PBLin2%;faQ@4l{sI(2*%j}!v{9}GRw{YS|S*DL>{OljOzd_kcR1a48hH~ad#dLhQg&71-<la*}4qfi)vA733wD{8&@AtoQ!A7cKU7*TzNg0q|JvEsQ9F!f$-)&S$^dnLc0YM5J!?37Q7f>pJX#`_1+aa_@ipj*HMu#A4wmm2Tmv0(u9t~MES{~C?{1tVZ;$YUx{XQQ9*J+DmLN;UYSH?j;$rg(OH2Tx6nWDFk%r;27EVphHdnG%Jw4QZ`a`w*bD@1CuIa1Rc!U8<HY^x^53(;~lDFRRf;l3i;2Al?0ZdHlmZ2!{RmhBqV^`~?BVJ#5KczibBx7QS-yLp3jERRGIWlLS}g}QfIFVz?~=cfEZ+T9HLZC<L8qeFE)WBkn1uqcekjkblzUr)g~(r-e;7xKFS;rX=1_IB{BMdPOKH}JDj{OwIZD39meJ=H`ZCXJzSQ}m><j{UvrH>n=>nafikyXsG0JUba5VTh;f4JAgR4wWsR5=<W9Ebys=Pey;ro!2s`y{!!lM>#J=<0P)f3<RWfLLL@<&xk$ZhS@4)J!~MUh9^lvrAL9HLd*w;q2t6<QW<3pR!}fHp{m&NoJbpza6k-sVv^y=gDF3-Toz%|<o1kTQX-JglXZzfP8L^{#-SEb;R(PnYU5N=$*RJK+#(RyPo!%F;e@oe7y~B(7C(EFbQB+*q!Krjx$T0{u;rHb5v?5vDr-#ZTzo5)GMsskG8)R@m1XXXzN}$<hxZ2#0(3MZxrtTJ;$BgX+B14GDxQW%g7p!-&AT4W0>CjlF64e;2OPw)wzkBkaP|ib$Mpa8SI<_(B|E@Cb=a_G2Y{kFa>;!`9&JrW7TKq+qy}IO?o6&VaItL{)BvgXV*wvQhIYV&NI~hTke83V)8{dsY7z$^b<E#xydZ>4K<dQ~W>Rl!jx9n0d0O^kMMq!q!5TrO2;YZf3~WAx6D*`sDpPis3}EEBbPO%<Y?km5xj--iM<kHYU?WiD@v>k5^ddo7#MA`2fwJ`;05@f!^LR|o5>Rd~z&4rNhR%B+OM<8kaMwW@JnP=_&Q?0b(TulR`l6n3qV&I3ujUl+pBaxpU<{ul7!NO-BZ}v1McA^2zg8^5$fzU2K&&B-8%%U8WVJGlQ(3syYC=d0#83Frhv*ZFm|J6Vz?@8+fl0hXNhhfca>`{(AMS~<AoGqT+EFJhwn*9tRAWRt>q<(D+;<os^ayMeN3jyl!xiQ%Lpue=Em{#fsNV$U^VQUhi84Ux7(dtKi!uT&A0>9p{LPFiSrCug@xcn|xsvijs7h)5*=hAF{-mx<v{hHP;{2&qc4iWS8>fesHlm2sf`<6rx}4Kj$BL+u#{0q$C_o4|JDM;IEY&0nswG<~q-13`NLgItbY+;uiTWZ)G4Z#S7IHe@lqqFPzbcM5RcaXYCD}z9v1pAuC~G36)+p$Uq^X&wHy}4l2W%*Kk=`k<L3z7rX?h?_QX|ijeHZ>0q>7DWCOu-cf)+FP**pXC@N6OjTQw%39Rm_61ixD8^MSqydp8)E^7k9<`+*G*7$={>^LPRyxD$0`mEm<`K4Ht#w)t$(fSxXdB>>lgs=6BK8lA9Z<ME~5xyX{;iZ4=l5WwA%?<C){PKd?_Me8snTOQvKi_+AJuWLDjS%*JSzf_%>ZLG%27|dP?P2|7*+Es?MB}og-9*hv;&5be-IM(xjvxVLwV5?=(+?~7%4s=tE>?HRbf<rNuaa?z#Dc}+_aBEg1<_l1gNmNzBp){k~Y`G$C&ET4+tT6#QW=6pyDrF6{IpQqH>7$K)H9lYck(()58dir*VgmL}VX-xEdMn(7pZ*;vk=h#dMP)o6v9PVs4)$a*i8PDIe0FwSE=;q0Xk}oV)-T&OwGa{kT3Kq_fRtBur2%$uD5Naqky$C8La6gSPG>H#4q>4q!_LY3;Ma!*QR)=N7vuL=rWpe;o}4)>Y9k6s42e$d!O2)&Uc#O@DOSGtGua<Nr2Hqdtq<3!CH+$H6WJZ#$(|GL;={cFO@^Qy*bfuO&D|GhWACdS{6Y{%67wDMn(`A!;?i0$X?x!u5Mla`*3crCifmWwyMem|p=n>{8P&LhXpTh8LqyreG3T={qssduZ!CF3@s37D5)_%ic#L7BPfYU!b65tCE%_diM2w5uAcCt;>DY`FYd=VljJ2buVT}=231+k-8|F?M<sM8(Bo#86U@s~09nutiekMnYCJDE+ab;nu3~?`nYt$nmLI_?xm@cdDG=|sT7R-8bhAc?`&zs%4&(U_O$GRs*37;54dg3^?cX@d?f`Gsd>iCoVc%Kq9>wTvm0tYH7`KQ$j_CFQXX|b8FXYrQt%zB4l`c_tTKBt#aGKv|I^m`rE(&J{;LMN%|pw)v8;K<cD`c2Rsd8!PHZwJlDyAOT6Y`8(lzTxckJaS8~=ZV0UJeKnI)JulmI8NEOKD4boJGOzKlAZo!2QdF_=fwR!(WXU~Yj2x>Ub3GM<iqHA!lVJGu&YHyp3i`}(wgE5%$X-le)fP)n2q?6d0=Py!cV0E^D)*%)=_Zu_PF+j$P@+kYH#Mr&vW#pP66Nb3y+M6D+UM!rMmluUAgWLycRb0=-d&F>X5*5?Y&@)1Q_N9?-}`nUNA-h{5#sOpXRlu@p-X3Fhw2Z{Z)Q{3%FNg<Rm_LiTNItVH}XUF2{4}2v{??6oTC-_sV1Lp?laPM=jU+NCp}`SUCOnbfKfU*Eo*{Yx9w^F_^{=k`HEx5AbqvL5F;42)qa5o<j`akdNd~{?uybzb2Y<b19VL&{Z84DPUB$G};0IGzyv|MG0zSD{5{O*~ZWF!t06Pfq%hZ%>hv|L?Qrb*kLNR+`_U6owjpa#x&DegGXqk8wUnr=Fpknh;N+ks*uV8eT8VB)k&fd3&my3GduQ{v)?hUj(CdP-zevm7RrQsR_LTc*hzoQ>w@1P4}9x^j;lSxHdBRRv{9B9_9FuuU<=%Vf(d@#KRa9U&qglCRZ;@TSkqJ36Lh}=E~_40od~Q^<_YjL92paVk2F@X+A)f`9ZT>My~C-R=fIBe1I99Q8)IFvdpuxN*fO|LG0TL}xgqmb8}0m{Ty1@gXd<5BZlJ_GfwM#Fv(*mZd~H$szC~jY7H#MV5EA`am??ns%9t;-BR%!~fBcQmDbE?2H}i=<N1jSD@$@2j>ZXvVrb3?Do3T9*hTkxDbk3y=647_(Qbr*7!=j<$FMkc=9++E>d*c2P%wIm+#n8{rVeWey_o15O_GRdUQh2wB+Y=X&ZI|Kd9AL6^8M==rlK~OZX+ESfAGRG?6k8*LZs|IJ3K~fPn;Y6Sx70Kk8)my3T!R*-|BO+zx;)$69%cb*h8hybRqpODzipm8WXF<=MnMjo%@ZN87TN1WOw4)q8uJ0>eD1T=R2izK!Bpw1Rbu2chn=ukUd~}J(j#*wdxIX$+eL%Q6UN~gLuy!UYgE%U5XT;{Wh6oyB6tg~fODy-_6g!3zP0#v&0TtEj9Obk_&bi^`q@b}e%KlH&wSNFmHStesQ5+FOUaOBeahVm4B{7AE^n(JlNd7+#7b1!jsH@J&}$_s0)X7%X{S=6;#Hyopu(a)<yJUIOu784u9T=CHvR{{sZyTZBER3BA!*hf)~ySAP60Hf&)Q2nMq*h{$3Dw$EeA6JG<zULJ^QR7g|k32=^l`cjvW>+)%1*|&zi!fm>tNW^cmKufBu7xs>O0q#@1Z;l=$IRD+4QW?wEyV_ryUVTU*&|L1<yLjsEfogKhhGHoUa*c*~bgMNn8|di?4}hSpRE_50rcAPZ-MEWBb?=1HgF1(UjzjDe9GV~e-DcfO1&(NHvbUB73!qr!=igb6Bi%sq7PL<AC<OGe24mp;hoN#~=7py(ISv}KR!uPjm9^T8Bnyc)xb%e4yaJOrz#^Bhm1jHeyPQ@AHBZjb1eg?ea^Vi^7Y4^?*9pO+n88$k22j+od`IxKJuH5@}>F@~azA?A+DFiILm9^EsKBw8R!E9V7igP&F1PgH;S9X$ZdXE+$a8<G1!U;m_dIk5n_n<m+S-s$Lm)>KwVEkOyi8&jb}Z`DoSg7H|Z_e=~dx~#c*-Vb15bww!!6|Cm2p|ppB)>^9aha2Qnt+X}qm<Fm;+4RLgU;0januU2Ayvbd7hj7pM|Gqiy_lVB3pb#aVuEzZs&}XU`&UP5qp+9qo-4lg2w$^#40YKFPKamOq0YGO1@^bVqyUyEn^v?+;=cwaxB>*@@{|ro5Q6waQv;RB>sK`qR@gx+o^QqR*HmDh?i;4m2F{VZIk3mZX*-(GxLLN~0S>+Dg^LY1M^ba3y88^!&cYZccCG^*!2uBS=py#P3Ej(pap4iT(q67KlL>tbOe<4D*xE~`^S3-YMg9yUBQJD$@iq52kTl-T)hrv0H)kU1(`!j&E+49x_euUFF-Fj%R5AbYFBo6ItPPM0_J2Wp2?ZvpRfegAjt{d04FGaOG!!%tO*NSRqmlX+sJnn2<*Qc><Vwzf(T-j2^ssxZr=*+JSZzI{E#*7xBtFjaRRI$n#T5He8xrJa+kXz|XcydGSv>rT(^Z~I@%+z+qo^WCb6dP8PAWY{c&3`hLapC#a^WfSfAW939pf#Y=O=Gj6k&5cV3p`%NH=W{~1+8=MYbtbatZ0II+c&vUl5jo^&ux@W8)fC|n-@e<Q9l69F|V%GUb#ElD-Xe{dV@@|t!K%Z?UiA%SKh4mN`y)q_f_^vhTgB|$XwYaujj~^iO>C4RuJ^`w3-+gvcsUix{kE09W3jJ4B@@Ik|48c!b?jD)*4HS=cjjRDFNI9)rVeu5L3Pk=@Z!0e3JFWHHAt2=3>??&RMfDa))&kpLFc5=W}NaMzwqett{N=TOuL`_D?gV(g<xLT1Lx?mKZdcHNQmv_|>CywnlIPjn%uXETgR~w+z~LR=keqI4&2L3q=$ka)%xNgSVNG->K>yo+;>Cb|kqG+uMNTAR;+;oU}|}OXvtWm^?00)ko8&;{pz(Ud{Cf3rcdebSXg<#Hr4RZRjcL5fNn^nDW`R6suEC2m=B1K>2AW$T@n6gCs&Aq#H6A1enwS9rYv&Ne0m`mbGZSuvw-Fli~zl^S(%2HArq?KkZnOj?7@7dr2`g<b+yVuo}*F;!-d?n!X@y2%%%T*!3()$k(n1MI*Q$9Wa%Z^35&3-Bb8etzxl4{(gIF3)us4m4{b6v~0~hB3qIkv;zkl{m&=<fnpWI4hnM9`O>BoCsN>E;xJ`()6yo>-_vZxI~8t`JI}qC{Pkt7cYSTk+<3)YYR`OtZtVk5;t;|7e&GXb%K|4x#r6aW5H-Wgik5q+ENbnEp~MA9i^6m&p<r5X9kPRD^>d5bQN_`$7s(gO19^zE(KNXScQlAp!JU#p1fGI%GdZJc(ORs|fjc>Q3$=R|C{P(n=&2G&o!iC&F%VffT!gg!XT+bZY$X<&*or3MZBF97L0P1UhC6-IdqJ*GD_#BG3dQn8|Mr{x<$I7<*iuj0m6vUR8ifq2iGmoBJ+~_!g}KS;t2oQ&PDS<^+AB^4w|lvzOK17a5|F1X*W%n+el=j`Z0jGn^@mq({kxSrk*{@W$LGij=Q}>SrRBnK*_}Yy4e<r9-tkS^vZuOHwup$5C?r0ozJy4hmI6nJM6Rk<VT~9mIzcws=n5P6Eg7o*#8y2Urww}js~W9CS$D1(t>A#b20aohciCvApdXA@Vh2^wBkBqTf~mCkcDvQc?=*O6v^p&DudrL`3n$vGVPUsY#IxlAi&4zAavH_6>1s}KaOM=pvr(KM8?F-HHj3S16vHE~Cy$tp|GDXUweIIb8nE5pc&h;mE66jlNtb3hMeK84d7EtT1p37ojQ8ft&C_D^CjlY<<O|HvO(lfu+2ElgpS$WNtY8V^U5Oi~W6q2jgc{Qb#?ZAf!(usJal^7fX3;Qgo<!_e0h=W<mY=m-W7KklJF08#h$ej!9uYQ4F-QpLdVu+X84%lQ95D=8QHrT!7{tPG<%x#v#5+!-TNE+glj^PqhDkz+BaeJ4HD<XtA_WRi<U*6?2<PBhh4T9%Y|6vx^LMneH}s2&l^wpil^u<R=0z(z$b@(gR<=bX0nlsf)u>#D*=ZU#Kv`WhwD&I>+9kNXG2L&RZLX|*o4L)Q?fre88N)?GTMSHjB`tiyGl-iOH;1;2?)IwDja};<E$*@+$DvwYy>_oQz+1rDc5BmHAJ`8zpBg=s+NM<VJ`M2NW>sFOzI>fkGlC-UX|fHvXA@Qf$t<rVtX>T1ce$~7QLDu%`*j%L4gt-VvQ;e41x<(9;PKK-qWedzx?h>${*}fI!+~RI$w+RL*2=Xpfx^oGb`>a>sY9=R@PyfQi`c%CgXbk25xp5Oow8W<NrKB>1Uz6n@q<a>IvP3svj)uQXYM#cjb}4_^9nOuM1UWby`=k(Uab1-u2ubkn>_H#^LoGhU|rL*aE{wF;<*iM34BQ|#ZpIyYQThgKh@V+X<wtly!<^ly?oU74CbY|y3Z|3^6--Y9AUOGM%Clx*@HrxP)hy)N3KOw9b?0=vQEVkzT6nk;<9{LzB6l&$j<7B!`Mjv7n~M>#eTSMB9=Q&m3t^_M5*Dxwlym7BXW@^3B8}n{5*>lJ*y&FH<*8j8b1_XHvt8WjR|#Img=4jj(_)EYWxCex=3f1?VcTB=eZTVpz@_q73MxsJIm5OV;dlULf!*53t{e>^`}i#fiE_TP7wR3V>~gGRy>Hxy#O!O3;ymVdG5JDE{~a1+dh>Kxn<$^R9!Yz_o|AFKCkfxOnk$WUinmXYbxQDX`!<i4)9yn4LBk9JNtURiX-qyXEqA?izknEiK16;MZ>9-FD^94XYp}kVJlUOYI<1I3i`IxA3I_HD<eF&%E@x7P%0Z2zny5Dy_<S+Zh2TXV}74>g+$S8)qrP*IZ?HTsmeL6POE#dn#^)q`!H!>GZJ0;!RUMQNdM-t?a!ph7)N$5U`ZBPvTtj)J(g_y8zT(bi>L4y4MR8Y%e%KH+_8~1i`aq+?ZYCr@WzBYVhi;fVhe|5wtbOmKdE9k&xWN741Mo6A@(=l93!3*E7!9sb6~+q*Fmv`>nWA1aR!UMb?!9UaA7tm;4nLQuMIV9p9wXr969^z)5?Fdn8Rq}lre`nKO%2!jz7?CTL&M4ziVwc>kQ_eEdf$tMm}wLs<vABU78~GA}G<9poAWi)kBt`*Ap$-Y<}j?z1ToMbO>Vnzp9Ujg%x7K;0oz$geyFgu$UoG9A(j@4c-Z>fP_V>g8Z)utKi=Wt1zyy3e5tmuzeY;;8&sE#&}i+<0?Ztx_lfs1?thIFN+M$BNI4?Gni3)qwzad!{e;-RC`+=5xAl}j);xxK?avsa63_#1M|GA8nU@(mm`5@6A%JptKj!}Y$g&1q*h0wJ3m#`zg{&%LBVRW_mucxrES&IBL9L}1UrDY8%>SPKagt!EKegVzKk(LrLANfAdVc#95F%!qm^h(42Q-^Sp13-BC6$RquCOzc3xDwu?@OkZ^!{zpg<JJvi3$LfI2#FSueUeJchkWa)Fs*0DL-iC9@GU`6x9sBI0*|UcSTX(?IKJwffXnEBW;-K!X$6_{)R>UmY(+U$PaETrC=<w;O{@=A5TXJElw1+ta0+l5V<~E=^a`rS&uEQn;^b@Z0S{tvlhmJ$NC-M4;sdH3{2)q56w%{OM{`n&LBzbcm0URuq-xw;Tv$n!LXkcPxb8@}l-A>da%M7~hdB<QV=niYOzA;qo?hp#3NwLVVMBP>n^o##o%cp!iW9su)(m2G>E7!4ZtVESK~@p1(N;h6_D&FE+Tayek<{<I;hmUEkvaNn?o*QrB<1!*bk<c#yWZyRV{AlNT;79+{33#&xWOiRn<;xZo0rw9hR|^!Wh6R`MTWU&w3nk8@K<Rk|UOJ30(&%KfGqA&KUa4kzQIv9)ijF1X<iCDS~;7h?lhkh~RlI{T&~NsGDlae5!sC`?E<E4X+Kpjbi?(ATpKf}sz(*!j88;>2~w<<BE23Aj^yCgPyI?G9vtv26vr4Bhj>Vq^q7URz9l_>^Vil8&loYas%Zh)g9q@dI&2U8TLFaG$BoB3Tus4;U7(v12!kGfP_1UlWy8BomR(vo~sBlT8~Dg9Fx%i=Es(Uw;??{<I7Hw#VROz()UdL<Rhu?s|u)!1h{Hfc@N@!tlK$5uc9=L?S)o`-9=bIsULP{P=&oKJc5Z;rL0#$IL*k#Gn{D9QdFu45;v+5t~R75%jZ^eB#1UnA++TQ;~L7uWySbU$=_x;(f;oeMEmn$=ZrE(LXYI6AdOpsVlOBJN+C{T!-Q$pG|tKux=5Pbd!3cc(cGw#f3vGs9YSy%c9RIk$sjoCC;^AC!|bhEHs~tgj*0|;(hcM)ODsD?My1#Mw-d<*#T$oB^q4a^1YkveMLJd!LD$t@;%W>x6X9W=Cg&xbxYi}1rxZWa}3VA>?J7<h<7uXY_{=EuTJQs01wb{EQ<D8Mf~ZRi-Np<UMbFqrGGHqH<8jT?h$hro<siA-5-AyjS>?}-IQ25gtV#Z!BR@##|*CCK^6$qkG*T^1%G5fECyMe;C401z#|Swp2y_RB9F|LF;x~@rI*@?U=n^uQo4vVkjxKN4SoG|gUw(F;)4`tB&i=6tHNQfa6q!e1xcXXn1quj%N}_ULX(BM31EC|0p4~Zo{Y_O81g4b1)=C1f$%PGBpoO!BhKcLNW&UaF=J%;Fy@Uylk{869&!Od1rO=5Uzxe}9*~ba;ntJP9kO_z#D~W?9?W<NTjS^ZoaMN89j0ldMfN?)-Lwy2<cyr9q{$<huJd2G&~m<QZ^VD@4l(3Cak~|SxcaedpxiJIitG-KA8Lmz)QyMC<bCy>3OrR{Qs4Nxvk4g}g5gc2z4|@{Vm(p(LO8V3;EP~E&wEKnVslOtJSYU#m^z*)Cp}Bb@*qCQka?`WTjc9C+nKGe9z!9*Bz!@7=5;|%#DAjt&*1a#ehzlWek4z!FYoybzgyytZhRyaKsMTMK(Ygij_hjN`|6G*N`X!2D*yR|Ed|+-8y~P&Z^4$9EejJm8vTM65j-?lklRXB{@Eap<CX=)0gg8>gl2!4zt{P1G1l|Odw&P%wLaLj`eQXj)oJ=YkGwxX{7wiWl9m9I73xY(YIv*;t~zYZI6H_K5fQfEu8#WexZ0+-0i4fko7e*<7|~9;oW*;OZvs1uEYiKB1Mk;?!);iBMVm`t(KX@%1L;Gib$;l6q)h|Y%(lpn6Q$6z%i(}13`)~sY%yJqKK?=*vd`a;Hg076Z)BJM9`Al{1CcT8Y(9^&Jf`yA5=Ri?dCj>z`F?EXP^HpEf>BsAA(nlw7EUt^wkJ^PGJaYI;t2iEkgr|)IZLMe&w><yZZ~~m7GN@782y;s=K++2zX&-t+(^UQd~%?)$Sd7FJ9!HSnS_tH)8M3GjAs}j%&B@A(oyHFp-&*38PQK*Zc3aSBMlJf{5nvSBSc!Gn?*Sc&b6X@CzTDA4a9s?q)fBjBmgA>{*Azdr1!#GHAFUyET~BcM&ym0PC=Ad0`oh>c&Nrpakf4PAqO7MCjn7uS?!ob&nN$!mI%32t-K$kE>bY}P)C6|P$-P)OGY`|(o-Muv#YTwH9kJ|eiuz}v`5e29yi?d@=Ega<U%ycPT0EDPY4u9{lt952Ne6npC`~|LoROt3mk`p5(9S>@}R^iuALk9lfK#zy+<BZRqs18<bb5{$n^g{&o;8*=09k|fQU6kPoEe<$Q}F?aHn}|)D$PXA!LS95Kc`Z8PgODUz_gF$$#VfKp0%A=YIvl;I~If{|g|4SC{mMMM?j=APh=Le{)jOe*t0es#wBX5e9J`NZ2j{3C*kO`N=~3VM`bO$8R2L@XgjRya`pXDq!#hQh<$+fB+UPJe7)tAHGzvFfKs@dy8RPxkA2HJC`eL=5hrR_O4+8H>MZAh6MyGX?U8d6e@UpQ=wz-nPc9D>#Hb%_lBzO{#At44=#Pqc5#?Q68KJ`sDt)3D1gOugbT~~x~T`mBiSY;Q*uLJ$RlMMw(vvX^96C06{0zI1BPvD=)Jm@S`vt*5OR{#Q)F4T*n{a0?t|&3g4SmMd0iyCKUxE0-+!9-$|e#83<)>Lj6v&_sAryy!mIv!4mw$A#z1IFl$g8Z$dnEzsa!|dr;&>e!Jqk?NRgZ-(Ws;9?2s)e<O^KS|F)DzYguuQtH|b05FwRBeg8+QzvB9z;};JsCf>m-e56A^=CSv4uKlDMA5a+Y9?0#(4?Wp}QRz!d<grj7XQ#1a^s<$TPX(s7+FOn!ciWc^(u*MZ;LMS!I3i_&4glseDlm+j?n!7WR`|!qs%Pd952P32Ct@gcilGk7jH3UpoM~RVRY`yC?`h@5Ee*Pc5gCzR->D5$iK9#I$Zi$s=YB??2R6tf?l;eaSWYf6sZa8kf2aB&d1c}MpYv4<{vW<7efMYF)!_Q^rTu>_Ug|UZKXQezm`7F_)n=p`1!QqoDF{ZnIIC)`tGA_=C-6V0>xKWXX!-f^RmlG!&_$g1d@zbFsl0;y%Q<Z?xTWpdEp?~+KW9KaBmZCJjkcy&vJZy*_pdI%9bVk|YqMD}g#X*>H&#LaaA0PVaev(Go*9Ux<Rb;g(hnG6cZ~ZXy~be$eoBj`wS-}$z>+OWBXyDf-2k^w-h5z<e7=co^f$YZ7hA-GNHvifM9FfO9tk9IMWO`rAAf>t=XreBVp=Ga91QS{*mE`q@8KARyp-g#1pt*Qc_j`k-c^q{oj6%-DBVh|JLL0+gkMON9<w(0-lwhK?))LD2v-VW5*1~5FF`6Vip$+mDvv=zFPDdIsW&J!x`sQ0><BV64iqdaEcn#1B38jmL6W`Ntt8D59IbKY6is^up-2~u44x@qxKY?45eCj{{tmu2MYO6|D-6$M3~nR{m`z1{Xze1535&^_ko4xCtNxYXANlGOoDO;4NV_VJ7?;1i0gxy!9Xy5~_zlwKH~9%*+~a9?Xb2RDB>HiKW$V7dAmg8~tqlA|{}oBnBaj0)KzihOwoU#rj{Jtl09x=U@eni*hvj1ife`o&G|d{M1Zo;jXm-PNKN*<vw$(K}_y%{p2cxq71Xm?n-bc1D@5b0u8}<`zioAS0s?S>7qm=XfzhQg9E^kBC_<7zrFKh%|!dw~?ME%;mG>$7HCWU2Lbwg2}9Nae1<|uLnV&<j7B$k5w-@IJnuK_W}o<ap3RaiocT1E&Sk(VqRN$tR5qFLYu*#Q`|D(F_dU;sn*o`6(uT9IztSQ&&$wrd1Ru={PM{99slf{tBJv>2#Ddxr0rksJB*<O|CYjRoKYJ-P;<GRgp<A9}w_xEJzsDO+d(<56T-ssk9^17T)28po8(`1GH)?*G*J<154?^7|)}!nRT)?6)AArEgKg3yjfXQ)A%t9A;K_)v@)rbA0zeEe?1On>+_5N_OL8r)4PC=anSHr`prD+~{g~xgZc5iCd|+_~tgB`GFLrw+#M77{N$eF_6{WmhO3=^e?3M6t+SxssDrT-YZK<jT=havP4kb6VAE^hF`zxp<q2UQ(s0&w6A)Ike<>>f$&MiVN;>x{*+7ONhirh83$lQgyd;DU~5KUL~e1gK}HVQs7I19n?(KXQt%S2(%A^CnW@ZoBp%oJ`@RJu$x51*T{Utr`PxR35ld?)JDT@`ar0<{2B@nZ$JC^IDx-%-<^j|&U}`*?IIIg0i-+Mi8ZCLCsOWFy?r3E!kRdC5!ZI%Aw6PvG=$AvbuW{OV2$Ckv+bH$h9*xGEaGlEAs9-?&0p=H|rfy-Mi@Fc?#jVJ{VNeFJ<&*!vF?!>8i-f!R>Jmn#Ws{gT+A~5~Q&uhSM5NL~^p{Wsh{Zvm6bu@etaSs-R^BK;s9bCPveaNt(*G9n_R_7wBJ1h%t8_0BP87MIMuH7Ims(mAbR23g)LBgoFUh-|L`lu9RG1u?s!Bv!cD9n!$MZlPKKyUuw`4dl|4E=q9))cs$|XjN3Azmsqoi*dxVw;FFz;gc@Ta~Jff70+UrnIovg(2;7o}7}#kE(cE-WNV8bS-8S^^UZnM{$G<(olnV+&KMiG~D}-h#jxr}8BfGN*!x1gec@?WOXc>I7ge%-#)=6b+MWu$BJBZ|a$B77t`7PorHwioj`X&*9QTFs+zNLNU+wy~)L};~RB6m7??U*701&JE>f3C~=YRD3M#^|8MV2VrALZ^q^QxtY|W_*_pX>?{n^X_uW_TK3CN%>Zx3yhX;qDVS=ETU}Om+(UwdrgJg-4%Q6-oAO?VhU1ETQ1V|VQCLjdJrW-JYDMFTDR0Eg*6Av(~@B9805!vmX`?OWAee2YI*+xdJSk1rw|7+ONTJ{6M3ub76jXpZdTCnj!CB$L`@Ea#JvG0#-Vv;+a*TmkGnpj_IV(Amr#PZGVSQAULnpjdzj5D6fVm<d0p}J5ROV=u6EWi9bpYwTftf9%3yRkSX*W}CfvF@Zk<}jsT#BxI3JXs}cB^46R3uTapfom2{EJ!43Rxx7%hefltY-^9}W=<*E#0?6nUQuKNtDePDJsSeeui#^jKw`mUjuYOBHS%~=L*sp684ayeHoz#R=~uY#xn56$V_3ue@q1D}@)EP=!lBw){`63>yhc(YqJ5;Ko~W>4W1DZ#4hm3=iFtYryZJZsI-AyFqv0TTSgLKf*UuK*$h<zPwhgMb<<_ft<e-D2?ADKEH_uykUU@4PJYTf__9t$()vLl<IS!uYy;I2uD=i|{YAvCk9p_Vej7Ff~F~_~#v)A)+PnbFrP)M`mD!163wcb4PFvroQ=|IRtvq6e<!)|+k!9!sZdO~v0#sHSZh5t@M77v!%YI7*ndAY`H_Q;af1dt$#y{DHF=bJ!~2}F7-&f{ClgXdq2e{L?t&|Z>a001q-VMp{jVR87o1qQScUbDt4@NDCXlh%&@$`zq-uxCgNvr;m^n$U2q*T;yMV_*a%8jyErwzi?oup4z4D8(QL;vfLsOthhK%vriYKs-<~QIO-uki&tARYMyFkTG={W`R7=bqDY%N-jjc*f2(H63vzAuWT|AeKC_prUx@lOB7zd4-MBZ{o7CjBo)wHM;yKM7CPeQkaAblSiy9!{);bI+s#0Xb&R|g>|EXRCbVU#*SkTC43{A6Vg9S2VW1PESGBzbhq+(EOw7ZvXYdwy<tbvTEf`E8syjKu-2t67*+Hx!HDIf~ELb8A4g``pXt;gtmkE!x+Apa|2UUs2bpy;27kOddU>G#=ugQ~1Lqm-v<T{K%vy*?#6i7t|@VPUr7y=CS*XOOqfA?kaS>9hR=y;Lbx-Y?*H>b%dJ{z6NkT*SZDuX>ZprI%Nb;mJtjw}|JO#McWvK%k8S3Jt<V|TJep8F9<F$XnsC+jN-cr22ql{(^t-W?nKHH`3Ju{{;87c?G^MYZM@kH5v&btL=uzM2so_j|)7Bf74+z9rJlY>?GkH!riG%Q5_xeQIt#=V?BdZ!YewNvgQ}{5Uc2ZmLbgI@$atH;`-5dOw`q<lVRj>cr+WrUPZc0ouq{v1|;x_l1PI{tP${u9Q3WRa!CmFi@wiGfQwlVQW@7R&iM1hGQOXfi?gRRw`|e$hHK9MzkHMaSvgFyJsdev^F{CrX3phBj>-36+qLJ^XC%8<yn;z9KnAV&C^#h05ql|QHmPewRZQckjeKOYQ&LAlDy6gqIHYS&4WZK<`Dzhnh?r1A7^8dDLVKf7A*0$VrB*~n?MiKr7mP|Y3){0;43PJ>oIE=d0t3OB~t|~Oe;p!>i%SDU^M*4)xV8Vf1Wo=TLQ-u(?zK7$Gm85W8Btk=|=`*TJH8vN!8pdH_8>YpgC`qr^%PQ737&0o!{N~1w`YR{J@5czuVK}isd3DmgJ43a#+voQSX=r&u`V*PgJUeLKl$vp{7BB9|9vSlP)Ocn8QSruRYc)%)?xMS-bK^Z8TE*=+s-8-g{)>GROANU?Lha)`oj?&Js(Jq#0KFnf)T4kitS0)A;yZ<7F`+Bq#%)f{V{h62sjFBOi57k~yd!Tg8%Ff@%(n?YhIH@pHxIzCF(ok##Ea@>s<Rf*I;$TqxnF=f0%o1`%KRPj8!GSrYlk80dmuZn6KUXTcDs-yYrfC@SiYqN2;`s5GXdZk&6I6JpykCF0H22-ku}2Hc;!Q+({6sJJkon;f{C^|~Q>vCRQfUu~gBK&wOy9ujhvD5ND?E)4`U%%|e*9N^R2lIzYGXAw*8ms)TCiW2LX5rRzzX*L}^a*wjWR?0fao;qT{$J7x?cI=T{R5dlfaiBSRB`a;yUc)L^Su#29t>_Rmt!>R=JI}z0o7^6-Ah!}>s#1}H8}NcY&jSy>_8zNuBta;FeXOrA1<jFzy%7;F4diA~@95|~y|Y=y{<Sop?I^Oa^fE*Ty35zfU;xLGqDVVDheQR3Sdoom^`%a;745Dft21QJ(xF%R4GnnG^c>Y3Fc)>KVA7GonAF6&c`iC$i9jbgP#nthR~F=B?XmSO=mAbmUgTR#p6~=3&Oysczy<2wiA96SE0_ovN9n(I>(=y693}2f?{fr(ouM|R&EOgejpTK>)`l|{@xFwpYkbO<!w!(Pqk%PM+n3fY;$GS@VhX_ak7<7HPRW+S_L4e-%(@u`tmW1;Nz~8X<sVwvXRyi?dRH9xu@oh2iM{DW%j&tStRyBVnL@l?CvKjdcE}{zM{pTq)c#ZbTj!9s-#p<$I;-XA%%ZBDi4*{#r0ul>=jXLM71e9}QG8w!f%w*6tbQ}ZRft`P-v`#3g8wEzWnDkt$_Jqu^ScD&RrznocMxEveMzx|0Hr-;qu_H&h}gXrYM>($zQrm#hG<k2;`uj{fMjx^T3zljmRKU9!JAHFKOW8S0WHxN{f_4uOHjb1<O;_O{@w^k(dy0kA;ZAyDdDIi!l+d?bFT}xh*u??o=Hp{u=OT7!xpfdT`c4k;`jKvp~uS1B0^bJ4l)7P^f=_^N>ZE_q~zX-s#)`IK7nCJVFHp-0G7(<c3+<U&hOPq&u6iszfjB34rWnpR0R4^ANs}Dmg|WBT=gHh{v9?h!(NUGIli%*iQBlU>POz00~3;O@t|e|gQ)%BhQ|P;EOd4JVO6b&`vJ)h$?bqNL1QqvntA0FijGK!|1jSQ5HtfsaW_~P5xS$R1?JcM!%%IlYzsiriq(=Fe>Xh%qlesaO@v0nudFuJJqrs2?1maOYoQ7;x*T)WN$kTt$`S3}fXxmA3;;4@aii(^<BqN6`b$)ioBf4GfsJI(V@CbT?>1EtnnV;CrM_JroV@<}^uwOMw&&-5`r5*;E&STTuTNiF_(PuhPxI7&z}M4D-c6t7v_JOg7YZR>JL(r~+w|#vEB!%kTmRzk#wVY?cG`Kvj*a7w-+k#*|B0Tao1ZeBU3?U@J)NDEo{sOj7d$<B>~4BY%{69qZ~a?c`pWoX^|Ax{%YUi7X{Ho<z~zsihF+Rr<!LAn$_I1~_Sm2Pll|40!V(}GIZYRgUj|$%_&q*ao}RZRP~wdMRB&?ZN@`~W+fg5l|H~86Dj8J&=Qq4ku&YYycH)KUpB|T-2TN5Hf&x5S|3n0veI=;loxhT1huz^@Cm)zUJ^A|hlr{fqIx%NIG@i4)F6qtrg{b&>eAr;zH9ihD1aw_a*H}Ja$;`9ICOOAbG7YU^%mcG+jWa-oAf@rbrGJ&L#@nI0V7F;@{wK}l^=`Qlm5t@ueevbQj_-&XXS#Ohbixv=E$84R<7$MvNg=EX*Dqmu*H4$=r>pQx_8#5bYCNm6(>v)K_Se}t7admpVo~^}NJo@&Pz+@xu?Eb)Mycn$)&smw6CAx*jyb((fBkWU>Fx9OKxsS~)%of3<J0p8=YLPXn~t7V?#ZX)nV%ngc4=qVC1<^}i*@!BPn>P(QP00SKTdV&!TGx<S2}O=<F@h=us^?EyM$;8_wyG|o)(eK(-%))G0}>0p5=je){*o9J)U0Vv~4fqf!97a2Aht?9ytFy9zo}(S5AKA<bj`^(s-WZ1Apl*Pw&>{K`dXKy?gTE3&)AKe$r0WSJ$3iYw-Esvt|*ux|%op*sx=3&%b#2ML$2Kvj=ADc=p$qzek0Tf9PfPtOnkSBTNrqE!4AE!8<8wt!Frq7R9Lo(<64LEBH%O!vxQ5aI9h77gio%RNzpcKJnoEfzS*GI-y?*ia^ZZh76e8RCkiI0VbBLBp)8B)dC}Jlef0uk@6HBQ3PqAz+Y3fKdSzHw8gKWKAcpFy~hQkit1I3oi$1aVaK$?PofleZ<q#vz3<p4wMz+J3PQ+P1hfvJHpXU8{u6);Em@2Ze5?fUq7W(Y8f^ojz3P(S&b34#Kv4$ez}#vp9b`aVhK_E)?*enskruv)$<{<N06S`9B8URIp(XU%k&oR(>xBr+njn2NbO<U7NN=+d<=>f;8J^{XBx=w}wj4|klXPmu-v=$+@dIuQ7WFR(Bq6J9`qw%WgL2M~TxwXGAy90nRx2$9Z_o#?69JAyM=PXzm9WOJhTR?r+)>d`tIt0$39nK*1n7<pAO=UmtN8{##shR(-1i)L!=q0R)s|s$HvmI}>NNE4an$zFKbp5?hz~X>^R4b549DW=Wg@WI`T+38s)T{RCSit+onZR_;VGF5%O%u5AfCp#JpdS$TX((TX%pP=w=ueGAKY6m$o*cl)e!b>Ni76)jsNXMhJ;}>B!sL_{E-O4CP!V2?6e^u5TY$|)cGVk>DLEaIv~Nb0fVQZu0@hQte8g9<R_nU6tQ-bdmiNm*+O+FTZOZa3E5}6CdtFbnO))eUuQ}n99vHvQ|`D$q`7>?mCmZmyz(pOZhkUCjKosaPyV#@t%E;5^7M;BD$0^zb|EGWEQxDkAT=$Y9>kf;%*CIWo|?X{H~m4$q)nfk85NG7^yWE9l!mvMF9tsaNyWL*&u&xxG*AhD_8I!o363euMXB>D1zqP@ST@ZaAwSz-a@539)R?+3SxL{TA;J`*)NP=PnV?LRy6Q--Npd(Hkw;*uHTicjsSqX90m0VrlS2m#Q37-$6x0$x6%vysjK~8pMZ;6lZGb=2Spg*!pjAc%Ysz3J;E7C*ngBgY*I{00;EHaaG<9mM&SZ~B0J{wYD;XlG(bvt%bbOJ2@w?br@AHFy{AD4*0l$pBV_o8b+ATI*Ku*x3-7F+nIDwoasfBGf@i96rm;|=~^x}+=KAeDCDhPi+g=}dl=TSkyF2^c)@yml`+vXLYnGaIkn>)c;xGDzic>&1S=5}Za6dTZ4zX=8VxdF6upd*3fnxFpi%c)3^LIWVVhdUM5D&QO&!{8PG?s@xB+3O+z_ml#0+?D_ejkF|Tr`;TYE8Eh77>b3ZByaYMO`B-2l4j5$qk;P^=wwyXk_VYDX9M7z=t>8=0eIrEje)$bwu!ezyropNJ*OMlm_J1Ww-D;oZS2d#i2lYTRJMJl7j&(7&Q*|H8Pf#seUU4(^vmb<;ah!f8?3>kvNund@Ev(znE_V!V&gshgtWA2yoZjwz1{aJk|tGT!`c(4y`W7K^~s{>#E|i*`LSj$IYzIm6y0dB7jE}Ap<(kbR+7nkTJwPT%&&}@>-Hwh`#>SOyBqpD^wGkRCMjv`*JMejF2Bl=E49tslMbkK$XiVvU%h_*7qi=Fg_;)y7zg_6gP?bPZG&LAG6>q`sbF7MMt~>7Jy9iUZjL$|0hYXkzIA<KlzKb}Dp(ZE98=H60VnauLq$jKEZIUfG-06n%z)T3FKB+M2|(bUJE~E_cN`h_<`fvx=|;{}=HCbNxFXOUWZ!xm0V3e@7n6Q*X2BY6mX*h(zXC(s5on4Pf?KDfaRd9vGITI5t5H~Pq`StiF?1j~^M`Hp92k4vJxi{4?SUNfu_YpPYn~W1OELrV;~EsL(?LV*!`W(aK4Q*Pt~-XyA8E?4D8^Km#to)sXb73?L{D>!)6paGMrmD=hrJ{qbs9h-3;8Q+3F}z>B{M~7zXn2KeN%w!FBwU-)UQeM2+2lI8AhO%3{Ft{<54wF(pgVD&DJ?d!<M%^_ha+XCI^<}E)6)S8G{Pt+m{SDEly@aW&b>5XH_qxOEH}BRO5Wzs*k?zq^?nw;*2x?s-M;~xCnj)`{cjyviL2JymvXO#YPgjuN7`cGBHe$D+B$anyp)L;JPT*1M5_ckByh7S4}2QEdLtX8PSL}?_n9#I}=g_6=vsFQ6xgY8QemN2OhGg)*$jqtI5f*WloGL4gMz^+pGuLw?UA#$3UdqiEZVR2=U;=AgtQcQId+lh>>7RtZZGBpO}$8<rdZ<_k@IO8;upxmI~Kupl3njNIY}Pe2wH+HKfHRa$<Wj2aJDNfqa4T>)&~zIP^0r4y8*j9L*IMj(A0JsC&8MP(#I`qu$IWO%xznoCy$Zu@h6>ZxSHdJ!{QDD%3hua)OlDi+Fs$E*T>4?&?#Ij#y-fVv!-rM_yygXBtGxg5(GFu}w$KTxlog2Re1&PMX8bsSHsYv;j9l56n7(7_g^)9kKXzL`DVj>)`w~=?=-p*hxg52l<7oW*wNj*I@r~60apUbY#;JEdgnyC9~LJ4v?AP7>lw{4JulUa_T?}#CUGjK@+OcsUyyGgk)foZ=$+of(jq5YI(_{Lt?bI+jJQI;#fGSKeg%Lba~CAgIVw|DiieQjL)_Tx%K=T^4T0TYmM0zKxrcvFd)l~4Ze*waK;|Uttx!89G~R4=zFW`pv|DVD*<J8oGo8zccgwXpPh=KRul;h*$kt5Z7SoTNgpwRHD~t|4HHZvMc4vJ(vV0-_f+%6)dpCggtU*;HO57>_ad0_a*)~#kv_dh!YFN@@9hCWZhHtmNJp5KzNOL}g^F=Ov^{4(f$%KYk$Kp|_%2f=`8c~O6tF@lV1@W!ABj#skoYb{!Ffji8)bzlnj%HWjT?&Gbe_s%#aUh)co(4tjR`UIqSvC}K)q;WdT?HON?$d>^(KQ2Wx1h96+jU>Pq@7Kwcihh`^m!$dnD#FX>1<CDE=&QXWAJe3NR8<QHKshD+Lj}L!R_&7K@AHx)}gPEv$+$!Xz9GVP}w?-5QewU#GSUI%yT771q3vmOw5IfjX~ztu=FX5inJxmNvAoQoih(SYtATlpp`*-|B63Zq&fe&>(?v5WXBt=7g~<Rz{q&_nHbe6Xb^a?nSD=l}wnSdWfoVl*|T^9V$N&iV_Q+q;52w_`YPyszGv)-(t{NY~d)-|A}<=zn*`4DE{r~Q&_>NK(czFc{@LFtg}BeZ*MQzzjdawuhOVfGy0i%dmBwz=><CbTt{2!>~kD1K9$J+XWan&rfmRrB+g${7nkB=h(kwp@jTfPfw*Y6d~YqFOLwqI553n`3#Eo68530N6^kKA>`t|u)5>lXUW|qh7&a)6wxKAi<Qvx^GmpwTkCP@LXLF}q2F5QC&}HZ9DwdN`WQuum@9j|cYksDoG<&}P`NKPtT@AFX@1-9WJz3~()uWcyCu(q2Cbxp#@uy$Bb^0Y3ZeX_Eo5rH;o7Om&UJjlscbAH6L@RL=8KOvqT`0!9@X)VSJEmTaZkl5uwcc|cSp~zU{90w05-c$rUO_N5{9d~!2XXK`;Ubx+jVx7zF*yvlbzANzn##1tH%@*=e#ek@&2nzj5#QG`QlP>~%U^$!pHi&(o|-|@6<;b~^$JMxwUd8d!DwjD+WtUf45o}f{sN$axci(8zax66e*|nGw{*VKIpoUM_Y<0&<|g|wFa{Ke&KueX>;-b8yd9wz1I}#!h=%+n9^rw@4wU>K@W~(NU*9`vCMz7-$4LcWVY+!!&~(B6Q7(VW7a;&ukPPVoQAVv`?tnG0rsJ5SLgtWvl}mqq-27XUY<4))KB^&=um!*fZIs()&mqj#0*J>yYClv-bw4_j^jNI%)IVyCmmrRlAWy%-{z>|5rgud<<95mUdkKa;VAeHPa`utbaJ>>JOs3fcFGnIDNVsNqtWh%SO3;HvzA;6dh+-L)Nh*|+1H{V!q+&c}o2po}y%qXM3l<?ms~r$OO5sgtT(P{Vy%)y;B0B&u8hk1eB_Qb}UqU0iC?pW~c7aZ_dN+2IQL+tL70s>#`?aXAvnK5*&J2_*cf^`59$_B*sV#l5NOVdsEiPI5jCF!bmVQ&H!7;dc($cT{M3#P@bF(b{;tiI5@}b>CMFTIf^eb`32GTsx$9d0U+3<2dKg1c$JkDSQuHAbaO9JxqL#t|fhdwWTgrb{O&7wurfjAadLXE|fp~f)t^J`&PV+ohbamJBW9@JUZMJ~@3@vxBidQocfpF7(4jj@78E6-<^&7p;yUPC2+XwV??$dPJk4^_}O@U9IDts$PG{mQgmv%D1iZUtSD)A6Cz_`S;Z^dPeT>d6A|@^F#m^zxYzbG4vWDNrFDha1`iM>DKV-Id~+)pwj>)Pz(t+>$eLi51;yzhR=XzEX5M9a2>>!6JsCHYxz@a#~Aj^S7cgV<MfpWL~8gJFLRj$DBm!D2-CHmLOOLrvm|dEv;0TH-i1DmBbz>mbJku2V<q7vHHZ+$8k^P1jBtnDJobZZmi<DY8vjPB%V+E#U;G87bOT*R5GEX2~GJIyrh7d^U=&w#HhH&D9_3&a;b6!QfADdg33Ft`msxd@^e#x;WH2S+~)t_kxXVD!9T<j)!-I$pf?Cw5Wp|v&_@bky0k;=CIQCBM|YPa@CEHDm^J|Nw5Vfx>PHV0Cp%RB@QCCRBE&n)D|vx=;3wbZpzpw$X0+zgKdvzrQAX4oRu8m7)VoVx(=Y&Q{m#8}N=$JaOAc+#2#V4%zWnGTSFgB~bR^O{@&A3nP60bV>V)P1U{^^R$+}UHJKvRzLj#MBjx+ff1`M;APQl0(b6-tx$7q@7rnY`{TK3$U)ZL}j!+9`(owF6kM8!(WYZkw=&$J~ZsHcKwd$YygvOot06+C<Tson&hG54Fir%A;CXPDW}_nh2G&<k;a<c_R-qc77?vGU{OLL9*INh{yH6*?+QN@W$f+j#}jT|>?Ue^;NFuQI>zC98|SUHv5|f0XpoN(!WKUe*424}sjR!rmpeZ;$t;WJZH-ILkc(<K+5CX{U{{h4fj&J*V0f#KfrX#GpSCyuT$Fzm<gBfb}kK4$$8>zHag^mnC*)mIoxGLo>iRlGQ7if#e?ox{s~|+MuS97P<0|m@v>2TkPE2FM6L$d5(($-J(4UVc0rLCKZPYCTKOdUx0QZrBNfasG{WDU<(QFzP@zTEq7=w^HFP91qK;g*Jg@JNIddRSnXJ_=ZwSL7q*;#_@s*Xlb2T!>rzGhxp#kLRz)0MUPXMrapGgVhg;HV&F}|~JPJ1z48OghV3>dUCxE=OS~zzs3GNV|FBQ_Ugb7H0)v+X=IF__TlhzlCgz_pGX{9I<UNb5QK_ZtkmlAAg7rKg4Cyd3PWL0W0suqssBxz<&a$YTb$6efcwUB32tVrUi4@o@sA+c(qkMGY*g{p}9sakl+b%bSjvSuDwGyHW21oqNjDjWJ26bu`-<VnG>J1rQplJR8C@Jm~Z{NFFm8J-j#Y9u4C#sDa&0L5J3vZpZs;)lxtz?cfaZJeM_FNpzWdmBr#zgK#1`9wB=c>qna%WK(y;@fw!`dcc%jFaCRH2dOmPm^<p<v!iI{ip1FS?=>pHEsi1CKHpE(FH391Y~ut)DpNYd2dF5nDO0MOJIE8KLtK2Qp`JZ>!mJ%mU!2hn&iBYz|?VtD)L1`i!TR`{gWRk4N5*h6Q$)V_5}0nCj@{6Ms;^gps3kG#;MGYk4g*06jIDe={5?`zrpAjnH1?+CPj~XlBb(xev9JPH7OFS%3Kc@g-Nj!lftUH_&S&r5eCeGTKyxF;_jG9k-K5~pI${IUqvKe<>6kRzP9jd3%|DTtBB;Qh~%q?<g19}tBB<9M-j>R2en~eMI^tlh@`vpVk{5pPaq;`Rp?tpB*zE!C?ffkf}|B}Q<0LamG9UffzQe`^()1WW3|6$A)OLPsvB2Dq0$shR*~QF%mp5a0D9B^GL6W&sG^@s`&|-_Jd#tK{T;;$kAwmx&ghkCuS`!c66ktS7;#iijHjB97ylidKP5EBOK{}~Mr4Rbl9BT(x~ypFB&^1tV3FK<buS4gxH5W4zRctli>BN4SLWiC-nvt9-<d9_2;@ylk>$?YeX)CS*5K0@bqAdr#Y5+(fxJ|VC%TYsvf7)3BTp_zPhF@+y-4B?=Do<S!nw<L@LVbK=qc+SlM<-YD`6yh6g3}n2^($C1adigdZHcaj#T+f_U;MQ$m`;aZn}yqqL99NLL>70yRN@16M0!$@!C&6B^g;H^U`&hzw4J{NSP<zbyrj@=UR~dN!`iIAMjT-B9B!FpH(fq`hjDy!g*Km{z!1}_!WQtfw>~#GcT5(o-0URP`C6?2|=EG=2+YDv}2#@Li!i9jJx5%#e?`OLYDUKtW9*nb7|MP*z5T8=qtykI(z(__@kEBQ}M_Db1KH|ZbRh0o2d~zt=|DeuHd-WC2PEZ)u%N$72phj+WH<vD^tz8T!vf0vhgPV&sc*aBjAE?O}wI7(;iE8P%JCD7h!QBJ~DEC-m~n#e!dI`plsZXass&a#ayqZE<7IxxUUPP3VltiW_Y<0zy`m)BpOF$;UsP?z%~*+0W5Wfv7rfYsk?y@^toX+fA2@4YJo*qz8F|5X_{~jsYPEsg47Z*dyc9#NUf7DjZ`E?5Ow|8QMIkXH43WMK&7TFkWZkyu3+N|$kw2z!oD&_Tt*vS+(4jA{UHe30<R6_hhmA>OnuUTV+OTNWk>OzJA{Vhktd+Gu|RDbLT%jytTo|6^HeR+TKs=^1gTwIg4Akaw!ICdq)vo!QUS<+JfwEx4Nt3CJ_#ti)-D3G%l&gm+S-Idye(a`7H}dAP8eEVg53-HoiY#|NBNgP(xzA5>ZjtZ#=={zKc2T54WhArId9b!-fD9jZ#5ZjRX`KFcLpjgywy>N&D}7DmNV)qz!bEPPvVN4u}Z`+oD*2Jx%isw)qmJRxVH@9ZXXlTgeReqy)KV2U*!=1h-@IP>5zN<n)1|yABvNh7DohDc;@boAkd1_!H--*#d`Bl$t)PaUCO1R_wD%^_SVh8L}NDjyMz{#=?{cj{m74PUDse>2^18~6dvqOfPXk6cf_04Qa{KG+HZc2h8gA!Q-kY!(l!7n^{4z^HV;5JZLtUkEGM^3W3<#n*_+Lsv46uH^JQopFC1Z90h=h)jR+?BV`1STM8sr4*WnBk_m*jgk!*AR)}`8S^XGS!w9v&a2nRG?e&x<XJ}fVX^`H3iU8=s=r9wfOa&GifXDW`-4|34}uGyC+@uf*9If5ohY!X1$wn$^u{EPu>^DB@BN8f4%I2#+r0sE%52?OlQWA1{#SpE6A$$GjZP8^CjF;$A4)J~=8o_<k|^CnK5SNudgW4(f!ZxUg404cO3<QG98OxcUyIc1rECl5qck21!27&Vpr(UT;KJE#dE_BYXDQAPm|#7}sa_j5F2r>HOjV1QiB*&T}PkShjAx2~X4%nwUcIG=D6ijH!Ww@)R@_6UJt9=4USIy7xNDtp8tQA`mYkUWxJ>Ci<Qnz9Ewd1wbU3_BaB@<LL!Ze=82p~HJ3bn_bc_qiLz%pqJB6ENO<Wx!n$Ub?4bE@lkHuu1W($ij>_cUWY>s1A%Gdh;pgZM2-Ah!Bo{iIw(!?JY%EIccVuxsm71XEqye(a0UtZEoJFc5J_k;f^2!%QwyIvBGJWYtk(XFIl!&>~mT-dW>K*;mIC0UD7z}nO91!OGA;=K#U+i@~ET}9^H6wH^#G!z<r5x83R!3+fQ|YX*X~rVRsZ-s)>AwuXVsS6#816`Ad}m-xYrzoiHz<Ol&&fm>QZkC=zI|T#+iX<ghp1o4lsHtyPr*1|O%bKskSR_BS{`bKUTakz)DL*@Kxg$Jh?185`Sn1ic%YFp0*~Q^9#Z<1hMhMb_AX=Ymt}!nlQ!I+sZ0cHw@uHSzP4EN?}2&N^1pnU6~EZoHwk$Fklc5}q&KT`Jj}bhC2&Q3lXmWb9eqySz9t`LyQ<{x4Mjj;sGjwMi8;q)mYiF(Ifj`)ZL#a9$r;3XSE6?vB$gH03aq<0@jpCEqG+r7(?Y-sJB{>jn>x6$$a%6H8k;FkT?@CY7m>7hVcVkvxMRH4T1`1;E6mpgy!jcV@$&?v>Y}ygbt%1>L)MTBdA66?sak7&ojTG$9128(Xy7=lK~M6701aTDuR-8B?VI0cO5@a(n3{!DRz$(B4+Rx-#Po#}_?bfu<8gu*ki+hmd!W99!fokyQzx&9^u`PHOltEDM}_pa?7`l)r1f6h4(W{3$O*B^fF#wA2~7d!UYk_BIdhZ3S`H^nef&N+k!ZeH*>F7qth3#?{W}HCs6_%15x@uTX5mEh9L&KbU<&yYXT@OWnZ#QO+>`<%b)+<fdf8BwX`)VFA%*+<i5I0ou{-rKUXqW-Y~oyk|jjA}%c}wo|eG@L*_03ZTfYA@M5|3&bzA^k~VkQ&-B4SpHgV^l)PMt~VQ)*dzLos!8C)6DecWDszscH7)@X9JNHPN_GXA1F(T(U2;8?dLZwrOyH598LA=_S(yTb9cuh%MCNE25-1ZY&%jQ|d6+*CCTkH(q_LA4Q<%?-D3~*oKq<n2SSCpqWu!_1$9!wJ_iyX*q>5b#h6H+L<R_EF-SQ9o_A_o2Q+gZ%IiN-C&7=k)12zL>qi`p>a3H(|6YP>jj^|CQ(l!Ub+Om`Aad7O6xF9G>LoS6;u+MQGB!>{}7(c@5z>&wnJ<nfUSiyWyS9-KVEp;f&U3dx-^4=v?dn+X7Q<;9#IPvdrR<aJ%yOO5kxDCv#U<T`WK$Sq#v|{j9t`OJ>W#DxJ&~#x(X6;oeFK<&8`HfV(bARke`X+blx$aG#jF(k9;8rX)j$R1v9YtP-N8j(NEe-{t_e5IqUbN(Ve-60!-)a;c9Jgi^j(z~gK|;X!2sopBZ}%8@Zz1PbrP9ohFWu)Rj``e%twpLJq(=ACEjr&f`37JyiHiqz*Sgx~lW$Ey^=Dwfg#Kq0Wh{_N$d~++=)T*q|5-4H!|wSw{L<}#Za4{aLy2;Olx^~arj=cvfhmWZg?}aJ;)8e;s8|fls1?Mz)&dY(`A{IM%zLPm42o(>JQlc@_0q4#H4WGhVip%o#LG5_fC;XrC9@lBbYpsK-O+y(@egChR1Lz`^CkERTJkm9kWs7P$Bhq;z0<7XDQzZ5eo^DEu}ExkDwTRjuyE9szmD16q}RhN_?h%4W<SJ;H<eeEght2`%X#`)z{Y?olmxjOO<SFDKcgnfc?#crie^6=t&HSnFV^bS<!iq3e%{1mjOs&MJVcF~>1<x`JZEdhFv(WWL@8$QA!-!1rO;u&5?sMHjKQB&BB~Ju(ug!3i$`pkHdNL;i7+it_X?yb2Ub_Malr1@o&Lvu9xOVQMg@Lj_|INkAsu}VynElX%;)AcB&*+0E{;m=peQmag2L!TPTYF`zNzjxL8Jz{H&=Oxd3+P?V~z#U=KLIm@?ENE&7{_I#{t<e2bkT=qJYuIz!>th))|!{p3=i~Bf$8mtHM2WWET!djq8-w(mFAXbDRb)<i4T<8eVLfPR^0nmZE1%$Li#L(MfYt@v*Co3HY9A;AX60IKTH*3#+jseg9b^cCPX98S<|`KVg{vp<{;mAc=w*!~9KQm=A?vp04Ore*nY0Bf~tBVII#I=0D0!Zn&t4Wd402nWs6)JRM0=|14B>l3d@6VeZ|cCX|x5ccra$p_(^^YMy4Q)Pp52u2RjDQO&KGKe5fJO5I#0oHKh!Lyb|D`h;^nu*{c=F!h{pzCxQ!g!85l&MgG9w3YJs%$^mtc^}ZfjBO6h1nHo01)|Cz|Eg%A?2^&WA#i<3q&m%L=SakHidsNk{Sxy$KEpXj%lpDMPt`Y96sqrDrciy#HczK)b4;~s>Qp=bdxmiC+)HQh9GGrOg@|&U*D)^n;zpRuCDplSsOBsb)=GbUFx7lkD~vEYyG}LNyw6fYca3UJT?N!yIpF*`+x#Y#nYPs30!8j>#k1X{HFJ~pT%2l!i=uHGXGHYA;7gQ5j4Bk4!gIB0&~&CjWB(Qm@Dt0WH>%G0B3|XGI=5R-)O7zul`!BO@>ZvzZ<Ca_Wd&nEnWX^-K6mka@h?ppRKJR3Mp~lS1Ebu|bTK&yVjcwPzKjWW%)EE1eO|I9M&<LU(GEK=${h<8xe@E=4iSR2maAwaW6dNE!6ncOTHr03y>eqiE5?Xv)BzU7P<<=x&_E>`1x_6|r-Y0lu*uzX!8CN^^cmC-8soJrC`kj&YbrEupd4E@gL(Z*uqL)R`DWuJ-rn<z(!|bJ8dR}kqzpY#39&Pk58H#ajBBMeOKlx(<hvJ7F&k8QZkuA9k_X+#OffAh2k}W^%fKk|M9%75%c`a*@6{>BETSN98D0Cdyk%te%F`>#A1PXKdtl$X4O?fT|G1MivO+bX2`%TEyIba(<g~bJjlOSei!xKU@}o+<K0~EdDDu2#m2EcBm=lk13BlW(+fvTe-waJ~qts=dK4Jy^Mou~%lRBC&hUWkZ=92jJ01Ex)$TDtw+xXZ)yYp70DV*ZC5c|tcap7jCxXzSc3h?x4r?}dwC@e6mM$EV_AD$F|8-aM#`X!8KiQ4zZPk_5s87>KmvFwljcw^>OdAw|Q)t+JNhSKAbw2xX-WHwu_8(gmTj&d;ci*tQ3ggN!JGNZ0RK)*A0xbC_;Tz5MN4xXVih^j+&5Uru5pehD&SGD0RU4SAAv&nUl6MN5C;yvqw{cOZEU(6}4dGT`c0-fX;x-A|Ll$S%>Rv&K)cQd+8YRQ+@5~ACXzVK2=F5?4X*M<srgS$C&Ju(<APBL6eWT)kC0c;af(DGl<_)uicJk!D*`!qz=ey{p8bOoI`#jrxUVFO<oC8C6}{j*r^V$yIg1Yd#Dr01*}+}B=6hJX1ehTS8ALJXTvpfNNOB~v*#_HkHHL$rdJAtdFI?51AoJ?nN%Sm!acpmypos;N?eJ+&sto<I4>B*r5xUgIE1Q;BI6r=5n_71r|(1op(@zytL{Xvi_tWxf~zBLY&tkBCp(4Y&Vc676sKbxhnm=3+oGFEAI6Kvh<0kzUaY4rQJU(k%R9TSQ%x^7VY0zr~mh<z>{B_jCduU^3H~^PAO*@eNf{a!>iQN9}zFi)yTluu6jRBpMrtp_uYCv@V+mHu-*M_!&sic97uYHp4uG%vc@4re86p$BAzw+=x?dDeCQoGUZ^7XfW;v8i$;J9_zsX*Bf1NgR)2-DnrW_YFT@1=qjjB+HJuR#?rvIx(REukxJzR8nJPBhW9Lnw&iJ=6wvS(q8rRI8jW#{({5vcJqOVB)`>Rq-ixqKsI?7*(K`S<`Of6iK~b)tP*hRHApE<ZDShP|vWtgD_q~J11FBOjuxxYZzQ=av7kB>q+>Q8ny@4wKh6Sqq9{T6o9p>%41RQpe(<4k|QPbEJA?5=nVlIjBumAO3h=v@=(V0x(SbY-1Rfqyra`^dQdaUmE=xyI`&^A3kR;SaI?V{Vt>&o`=E8A1P*<WN?d(M97^Db+aozed2_x7^(M}JS%5Z<qew&kLFt&;Eq3S^&D6284yNjUSj{7I<Vgi+GWiwO-Y%kD_7wmYjK+#*-oU9BPTO0S64Cc@L(B3j$d3J48EYsH@NXj(7JB41k>L0N5#TID>?iV4-Aq{y*!ZJZfh5_VFG2|)-&A5Yb51;}6}0VgcR&t(l;D<%+qCK+4S6Nppr5#y$vmlUv53ldmx&lDDFGi{=nEn=ui&vuv>8NAs$6;)eV#@<k8@K=fqx!cq{W~gK#{+^3UEp1y$MO>;jFc|p41&4ppTrs;4{}Ag^Z|K?6$<`7<qB6npdo6oJ2R)*9#|Lxh3p8rlLbG2HtzKtUcjuBXJQ!wWS^Fg>kRYE&eQa;&pj5hiJ2_#RL0MZ&GMQ8Y&RRbtrCB;~A|JrrJWty)9KkF)?}Zz{LfZ=9CLhjwW9lG}yC*z}R1VL#YGHottXw)^GDxEu#3R!N_xYG~W_)B`XIB7Je+nUKo?L!LT0*{vA5DY=#6)PA*ylU`Kt|^S2V2e5*}&DAK32f$-60srefkb=orK&ZH>~NgL!;}VL$kNM35&K;@Gq+wSWESYq)-V+%yZ^xF<}<y2y?l+_f%vxoP=sBxtHH1GW#n_JY)O7L9WtaUghs#Nn3Tk_<SRvV{{wbox{68-pFTCz-X|Ly_}Zvly$eNw%)f1(a2qeSv6m6q*)XIn-m7#<x6;E_gT2MH&|x+o7LX}aoHy&(>)WE9h2#rLZ<T{L8e=OKsYud(=DGgflSv-Alb{BxdSAlFa?S6W(UaaJPHd_b?p9m2T068$MF{~sz5hBziRV8QvHW+_+_H%xZ0#Q7#IL3iqG`UZ6A5-c1Qs%^Ni37yXcrV1%2Z2fp~&@+x4niv*!G~tx=6aexXri6&p8kPg@3G`D5|HJZA-W?(cXqEErI;&9Cn*N05)OC0}d7^km+^uU43IbAKG522Vpxc7)Y~P-8e?p4Y(e;XdCJPo8(laV0{9c9h;9DtWK(ww2c_VmJOjF9tyEv0HtCX`2%U>TF&Z3tRqTRZAY+A5uHlmhJ8apO)^Zuw}5Rwk785vQLX@=Ya0U>Vi*8efwrjh^qX_MstKE=$|)-g?+qR7uLdkGx@Zn(Wk}1v3ZS%mc~!@iA9^u0*kspb8i%ih**#AJN_a!1NC`kaZJJ66abv>SKEL6`J>)F>)PoWw(kumg_U`i$`LYb7^db2%QJ3h0CX=$Je`LSI~b0Nd*nfx_a?)|ECT7Fuzw}yXi4x!#BOE7?&hgcpz>)R{9uTxaOy>w#5xkm7Oh9ND1EQhl{V~3(pJ+XzbG6q`TDfNOv0^Gn-p;2t%8%dFNoN|=bvvvvGH5FenE@5c1$ialq`zx_=zp{0topBbd5V_WZm4)hCg;InWWr@w6>dICc4`ytTBnKX3f71$gzRPPcz=WK^@m1>ot6_^VzM4`Ugaz^A;^3UUlsqns$YKDxZpoo6L1+t9SFXl^gHQufVIs9KK8Wi{uF-zVta@%p0i28$<bVjp<{Z=v9-al4Z51{GqS%NE^OoEB@9=+AnTgJ9m1`5Ayo3j|aGU#f1RVgS#UIV0D*Ihl`TuWDnqs4Bat2X*TY@<C30Z(cG(s7}|~h7Un&9d(ZuPD|>RI+sJQWcjvz$ay`Y6yG|GoLumI1lh)+lAiVT`fj;*=_4)G0{8|ch5%$Ad-Xh5JA?Sf?N@KjQ{Gpu_;@v$6E6iXe(j=(XE6gz-q&iX)z2{7h1K|~CEvY-Tcj(o*(Oae{egO6?r;+@FL-jVAk$ZlnD;uEY|9s*n+saQC>oly{nmmlSz1T+LTcTj|5w>g85fOk!K9`NYh%t!&OFO>nZMTB~dxwI9FZBT&eXt!`o+)UeiV!K*MnwTcCYmQK5QCxWnKYm(9O=n3$K8lV0q}55yk4F<dg@m?=48B5<pF(e5N(Hs%89ZqZDHk5DzTCjpn|c4+zW<Q6oM~e0*vS#T1>DgfomnNdza4;osq>~F-bh#Wo=7dGtmw2D%3h<vx{xbf(!c~k6NZv@-1q}W=R9O8!;t>yR#lrw}PO1P?KvI8uvEp;Ib7<C<c=ab|NOD1Qh^VDjE_V4@Bk)Byjn1ghq80X1(Z4gh@VM6mmYO<al7{!gNK_T|r`pN`rK%DlHaBD=G4rX#4-Qno~NUP*NxzZ)bdtMMMUVw#NDKMCS0|7<%+Z)65jjH%BK4oOKF+);6`b+seoREcRgKhz51v7TmpOWuq1w7#+mPxZIl@QIWPGem{zXt8zfHXf{84NMh(Rbo74on9Qx#L`rM46GK$=3#~f(e7=WAq~00dcO;vR%u!MeoQx#V>dW#iV@nuUwY*3}FlL5e7S<WwERKv=SI7Y(t*wo4HkxayWK_?(OvCvx)k07xGiq5keJtuA!G66iw33>v(jv%KBpwkt@hx^7i!6rf;uVF`bUGQ7_1f7dNudtqBty@`hSJk3Z|aqWE0W|0?J&LG|0~zxq08&=mWKEFB9@opp=zf1&@%WadEp_i$@?i7T3rf;Mk~b&av6kaZ6FUaSIlrj%U~!%vcN*_FzIF}5|X|5My}X3+^^Tn2)SYh-lS1$4N2lfW11z7(8W#}&6)tPXuYJ#)9%2^C3sbYimv@VGn(yGk5Jm0S!v{$Ft-N9y>!O8lc6q><8JXcs*izy+$hX<o{$lE_{(p+T1IS7d1N}<dqK^E`I#pxX2XbE4zs@CUs5a6_AAl>shzNd!|mIzenMCDv+dVCFdxYF88XU&VX&^Q?7(7GyO-3#V(xc&C3Oo<$*uRw!#}wLlgP=}OTzrA3&4(nWpIMPb59p7+t}DUT4u7VrWNaE!JKlDN8ED}j9|;=>t1tyTNSW{FOUco=aUc{9hcoDax6npnIe^tDVl)kG@^s}$BywD;mX8_5Qjk|F(zFU>->SU05ZZ%&Jp}U4U|wx=Oh2_Ax{>A$ZceQuB&^VXT#SG5fW`p$#+9F4MgxYBc=iU!bC(mEWvk*Wp_Y{#KL3qf4%x!07v%wG^@*VUVm7TeSLxU@S?2lS#6!aQY6xZ_VG98cAMi0`*N1vZJ$r?&Zd<Hef+M)5B2}V(Kc6O63C<Ch#O+sV4J&taOoZ7AM$p0!A#1s39S)7t5HQ6+psl~v#2(0{2i4Sx%mh+qS|VqvhNzb5=ay#@I=$kjl2@#cS%xdgB_O2kDGgBU>~{UZ&*A7t9$1pn9#MjgH+nb+9dU1CcVTHhj>x$6u)Z0F7X>us${7z0_jO@qE+r$U_G>l{L}d~s$a`3jitw|3Rs_YuY>t(muNO0Gnh4!L5#ful!-z~a~N}{gOOaso0BtRO*gC3Xdf4D9?AZAByVOTxqf~myYoVgIE4O7VP)FC|48QdaKkv*K~xvPWy2jLvyvwozu~IJuU*;LBP2L<F=7sknEMM6GmYhOU(p?kYSZ&^vuPc0d+501ernKEFc5!^W578M>NcDxfj+#d?wdwo+qt@dset(<+5XSa0?+6Nu1Na^Z&EcyKzLH8GL^9+#1I(}J7i(2<?}2aPhOwxxkvSZNqNRiVgxSA+T@73u#}E%HT7sE9-7%>iR|WY&M6H+f~2y&oyMq<7?p=fFOl{o_s3HkuOy60{zEP4$CIH9Tw+S=D%Bw%0T*oFKg*yLH7;L`dRr!8FTE&I>Y1=@iZnuL8UMNKvbjtD?;llrM2_)>H7@|s`Qf}e?pvSY)ithfpIh^=q&-2Z%bQ9v>bT%N#i*n1lkI#t9Ao@|HIK>o2_=fPA%)ww!0h$IY}uo(#G;-rd+cKJG8t1_Y_7Vf!6=<RSxT1}7V-q9bu<pC=f_hTxpZ9lhGts%x*Jx$j{MKr;)j$EB0gqontyT<Ox@p*HM>?tyd%l;E6K~g9n)m_;%nv30i(kLmY0g9$h^KWE!87=S<ILZ;A3^?5~`H>?dToQN@RB7Vpnx<s=r#@C~CAoPA`Yj2~86lRv`O9_D?a^5C@fL5>j$Rv?X(Oa`!8Q&d8WAwYJ!P0k&mz0aZ|h6IF(U-m27K%Kbh_H;zg3VA?Xc63K{Z(?PUqZr~d55rH<LCo0#lJZuBAvC9@EfYx*%qlrCA<EXXyII!-B4i<3lopc%!tuOdil1wG04y(}FLG;fl&kIF|{DHbITAI;P?Mgk=lqU+4%;WTzsWw-8$$mPm|FzedjK?v7Ag|;*6S~1H%FCIs(cH;TP*#xV!&ErQn2j?{#tR>&K5ji76D^tl^|kx{zxXKiKCo#4(4Ex#7VL&S(67%(_x0FvLwp0vFm?MDEMBqkasb~KaIqhy`%t{`Jvid33lKb66MM%^JM+<yyRjb%;DrE6h`3Yu9QGLr?2bq72@@uac`Hn2lP4BXIUy6vDk9I5U+IZiPOOF@S;bOVMFFW)v47!4Ys<<Oz}6{NW*H?uiUkMJWcea@d78IP>`t6*_I!nJn%%t=msQoJhYj>oV>zG`qn<t5Tc^;@Uc^kwj^M>mB>ZZYD<kpYO%aPC%$NlZijHA<cz*({|DM45{t~c$cp<QU`Ep?WlHxr1e147^;why5S6sETjhx}>fAtJcpXPXa0IUsC|MPspwPt;Z<lvIu6qTMkZpsL(FXP``hSyV~2U{4!)=Q!KD!iUzl&x8f<$m|0E7*FV4v4BhmgSL(^<_<-)dfu+itkmEEYB|#Bz-$W(&ruRdse-aG8dk{NC^W#dkm>Z2W?64F2_f#I}|WI#pz<pnXWC$JZ){>azfJM;LVvn5978um_D9^>1!?iMWu)Nql-d4i5UIFP1y|qdYbm}7SCby?FFqKG*nL{{S$IM;R~bZ|4NRf`WYBQJQ1|c#_$+h*Z}~9z3~KnCyurU#T+r2thW?Fi73hs4p68fpcA-{34`JFlr<xDUNG{Y#ko?^H*m7f?bldA96}KWR8XBDZyzAsiFv0%$}v%}c5udk$N}xJaHbh<&UTpGTY(u6O)@5HFuGR?n*zv#@U?7NUG!kG_fq*2A)><!(Xi*{R)R)*PtXXl89h(CX9kTEqIr^`cwk)!8L?VI=d$8U79OBp))2zMvyG$B_YNlj{DUX{z0oph0F17bmYHv*<|=njxIlC(o~Hyv<yQ(_eC^RyhR;VZ9EDdS|6kSI>E$9Gti$BH@F$vk{ClbXX^%~LuL{@XB95`A+lwX8xkSXx_0QqL=8xG<&hL4!F<&FmSx$2Uc6)uiAPCXP4(C*+Z`6TsX0Q~oJe=!5Eaw%@Q3QfgXfG9kfT|DsrmrkNd0*7icn;Mv+@}5D1JmOEjx|sHTzv!HG!2!M?1vfHe9!*47&9O>_OE??O(bwKG5YLezkeQ~>#sgzs<CLfQ#@4R8={v$yMj+yQ#&)&*yW2e?54Ni+i_k{vC+3ZXR8I!mO1S0TH;XaN>Lj(j_e=nszY2!h^mxC_A2XOlE4&}NAD7SaK)#cZ5E|D;+L!ZLw-5XJj1(vZy1&>N*XSIGB0ZDj{CpDXUVVRE6N944|&PMh8(66tw3hx8?#WVZp*vmroX;SG>8rEDTDJjpPweawCa*;t25!H>bW_>RpB`^w`YZyHly%TeO22{%&vS^4Qw<%M%c|s+pAS}sD7can{(^NDx6}KFBWI2Zj+>2DQ}L#Zjd6KtGZcgC=l3=@@7}^LL_Y6f?G#kXmJB?rSo?tHd=jM-pb;?y0!1W!3=W45@~%u@0Yv9bIP<Q2~mH#8p@~gNTPN%Uj*?(SZ*ej+OcAR+f|AdSfMllVI5%)^_7HbFD!p;bycW#C<|XRH{xVg^@m^yD=&{8CyCm(maxLnB~c4$T;vc!+Bgc*A{BJ!W<p)}hHuT+(lJ9>djN3uPcA)QOjW4+GdJPu9Xz#wS|*ICUI8i7(Y_PAzvvbZPP)(eYtZRn@S1$y3%h}snoV!+<Iv-1{n|jfV0q-baz`z6@F+JXCQijRzg=O5+LA0CWr|EOVCo;E3HMULUjlctt^_8Qcet@>+ok{6A~Z{rM_bBcXym!kO}nZ6chm=|7Xdm3c~EbvN9n+ixfzP<JHxl}_zT{pnz|mm<Q!yw%e`lg?OH&+L|`?&KzGvizj4c&4@=Tt2F_uh7w~*a8@FhoFt%C)OSA@?6UnK(wB|-#0d9|GUII+v7i+iU@8`GnYdOE;_05AG`~9ZsnjBkU70V6z9UrTm4*7BC-?TI*z+=3g*YE?t`~GcyeM$6a-hOTJ)&M`+Z_v@-(vNKe+HfVdSQ1Y-KmPw-wk*E_6+RxQ05tjxc;u{f+7heKd@4F=vhrcN8LQw5R^g?nqmN;f-hEw0>7TCt12_DXB!R#bb)F&KP#faWEe>QORWJz=FAv#`JIgWzR~V&_gu32a(x1s6V{;-Cv8H1hQr#GJpn#G_KbROU?!!PngyB}0$;px7yUwHb!lklhhG)y~>RY3^=C^C+0$3bPl>ib(?U19$W>ux85;=%6sQz67`zlSRTG1tmC&mC?%v36M`~3oofiEQuULfeR1EXP1UIch9K`hZR7n_O$09T!4-S^*r;xfR@#HW7N#HXc?PheJrFT$UKczvcekIMiH<w^@F&uRc{?^=_mDJg^&*?eRSd*fh%(n1rT#0nosduRt@QXCm;1+vkCYsQ$lVZnf3Z|gBpV;}-%Uj-`h@`X~~o&1=}%&UFn3Q)!SDFiQeJo4EIGUQP)2#MvHWl!;EX1WzBsV1%J3ur!&{op5OpL`$3+Q8@+HY+>`ujkBe97|F%Z=&;mf$+a5OXR8q6wOpcpl1mlH+67->4g5(k;R3dLbM`7M~F(SsF1vEfm1|#9hfpiLMaBTS-9?}m^ni*z84_G0|njOs1DDp*otCsrCT8})+l>NAM0dMYsVu{^<=uV-bvma`=Q*`JH9y9TNCqho@~)X^%t)tsmEg1ifF@yFGpQ@=;;1Ok;5EaE<q9V9mQ&4DTuAPAKgXF1x~djELg0FS;a?p)2nJz+)L1Z(MpL)$Ar(<ED}Z8p~=cGzt}oo+J}lSY$&Q-M9Kr_$2BgNxENd!+Axx=j;{RM)$d?Bt#un8DG`k|tsqK0AW|3}o2qV+hCRU03?)Y1geY;2#8`KT^hS%-URn42vm0MbbntX&2_ct>oUiDtohJqK?r&-c`Lsrk#h@CTF-oF3ZgeZ!1LP0f#p;eXwjUV9lqDbq9+2X!-^S`bk~^U@$;W|+wcj?_PW5^*`W0+9t4Dn+`ols;WB&@s4tSK&X{NQvK`-W`F1H&$*3rn@Z%Ay7m3SJ+F>gT0Trk{VO&wZw1Mk1B2pU?yZn(SyD>!#I#C!*s^GyQ3QN}>mBfllwxe(apT}3)e+J^D#CH^apm$UfqjKk8Rt`aCAbu|#|i1n>MBstT~V?kwRytt)DSzQYU8Q(A>Bo8TI2V*Ik)Aa7G5n=1h%*rB*L_81eDJ*8aA=_J*j19O=NztJtd}+9MQ2}_Q>Iq6VJq<G!Ut4&6UK6!H%@n&*6d04mC7_hbIECWc+vI{zAh2;}7(~Y1hHIjt%*C;8a6Jdp)kj}E$xxcZky9k<XTk;)Cja8;=Ed(!QdHju;;@3>5y3F9e*9x3%n%XWb6%@BUh^P-ba;1X)^aUHtHhv6jBDb3@v!r8i=m?pB{H~>{H)|RhzhRk3jN-qp?t4a78zCHV9Q@DVWpf86(2zW>Yz<3R451iViCd`2hC8_tKwdSQ%ee%wiQofkiZk=U$;`J^3}ZwSdFgo_?7lx!Ys03Q|Cpd`+k1pNVz!r_Z@5x!kK_Aa~R$IbSTD*he_~iV^@dO)vuj_IzmZ69Bdpb{cPx@{EPp|l)X_N;TuaLJW3Xzu7E~p3W%z$x_1<5O-$*9YP;k_#=2b?(0*%YoX3Vpv@JumA#Xz(gu<AnYl<aMR3eazkfLe<2$7fhi<>G*O`%d@-2qYF=kVI9Sg0%nG0b6m6A3NauvUY>lp>Z5!?ob7_K7fos0PJnP8NQgBL*Ij%qNI349<YB3$Kky4zCSIs34-FZB5?n$kuU4zG;vVbj~8LWu@>P`INvQF~8LZ(PvQ;m1JI?G~cQS%AM%KL8U$4>pD)x$&sAUhH+|3Nsb;;U2s*%J@E}dM#fi3#6Kqj@mQ-aF0al_^P?u{1`~bRPAD10-+E22SbBvP=)d21AT-PJM8}M|mBl%!t9}6w<O`~Gk@E3X(<|-2eo7tN=WR6gr`7#q1eWhH9v)%OIqnL-{UOEvD43BKErI>QXm8Hud?d68qyLTnX{6kq(f@;B3#n)YI7+MJL%nkdtbYLrU7LLpRs4EkD*H0c(U@0$=8v&@8&M+>8bv#b{JFc)hclRRg7(Nx>L&Cv{NaPyrbnCXY+AvCRW)cSbk(;;fN&BA#HXPi2tZ&Cb_UA{R6VwQ>gEB!T7Gc3CSb2E2JE6hFmbWdHXyfkTm9|a;na{Ij0&235tGEO;NQFudOR}LkPv2Wwud5w`Qu25)qGb1{e`%SDo%o6qikrny6z`0Zif_)R#(9!r*L4+Pqwy-^7V&lSza?kwVF;Ad#iYlWv<gEOQHx8v)n1oRcZ}XS5Z0WJAL3VX4vcl5b{Lg&IB;1oZ{a~A^T9&!==r-A6IyxwoK7sD=pd*jEr`{HLFaC%S1`mS<=r5bHVD2)+_`s2MPQ+s+pio2BjYyggI3lDHgO$AstR2lkW+c913JogK-X-eDCA?E09U}Uw#;5QY1>r5kvhbM<Ter?<)y>5;(~s5+|!8)a3i8{S5O5uri+M4+o00$7l41lV<V}AlY1mMq&f-ILZ#!Xt7gVWV`~3Y;J}_`e#v)lR4odGj8uLfgj%s{OFHhkJ1nxX0XSF!5)cuY+dKi0FP93dP+LDe$J3Ez69QQED=1MVjHOmd=bwWJ~x=rz5i!#iOv@D=qwc}vrwY24xRLb29g6)$fg9?AhXEMu2eW6oj4$VMgZy2uVZgZ+a~(WGT$NPYE3YurNds=0@l+|R=%^8wj_&u{^_<sq$56v%Ay-;yt%~H#Q9KG&owcUyA5Wv99;JW?xmoq-MYT^_dTXqKZpDDbjhP47i3U+>_GDU8UEE56s%P!d27VCum^D-JO>tcH!ZR=?5{yJi(vs*+nylzyoBXbiFYh#2Agc-B%GYDgtE<dkakcGI<FCJ=eL9A2s8NQ6pc;fb{EoEm<DbNy3D>v;!Fo0pL+j2;Y`?PbGwZ0vl~m>T9WKnT1&^ERInQObxEtYAen41Ee5tLCZ>9sN0%inWlD|Z5+OVmh`Lr<GU)zv@(0-!lXlhvjym^0I?<eVH}ve!NONMfWkztytIy^R;k~$K;lb37;>Pr(BJ<Jtf;V|CTT$l}N-{1#*7}*Y<eEAA{DPg;b5`#~YGUPLBPB!dnlLBtI4|`BgrB8k2x#Uv)jyNFE)vn}YL$25cPRfk!jxBAS0_49?x>rDEI5@87}BL0(HY_cZ1<3QTMSjdh=U9?xOrZXm+{EmBD_yFMF^^R+#nP=U?N>n_#_`Z@8#Yx=!;A2BBc~Z6apfj?Y?T9Qp6sr*D^Z^F!9Jg`qqPvwPfvLzsGjYDo+}_c$c(-=<c-%*<iig6&I6yZg=-ay<P2bN*&!_u*oFVtmcxY`CZynQq0aFQ~K+tIgcl>6E(0Cp^zJpNT`dow^t+y=a)#(Y7Mz=;ch9&wQvx2BCV_rGfZVCaT)H>%{#y`cS>bW7NqjLnS1Oipy-16rmlor+M?j%9{H_S#{^i`u$HYnxjWmk1v9v(YH*x5dq`S9Jl{Eb!wvH126fHlknF%(i!_3}2w_Su<Vy>kDw5%tw{TDdkFqZoP6McHo5@&Uz#N?@bG65>nAyRe&5(b6K_or=K8r>BJF50A7z?Krx^t{F*ZUtt3ub{)Sp&-{mlDbn;<4o8yS2%;o!hiEmu%Wlr3HuzfRhnN1=P<12XA@dU(}=Rw_esa@28Ggi<!PL$-c0cb}T0B{8qhjE*#@}nZ;x7jDcQ{@{c+lw2W%pBTbWH2e!Pi?Z(9G>Eek9v!y)b!faTri#c|&xJDe>bA=d)@m;&3dX{hOK%iYsMag`_b7ySaGAfeA6i|m!Ev5w@cCQ<}o@0qU1+?<PbBiqCAA=<>Ng1t&6h=1_h#d}9V}fY5mAdnSKC^EBpP$QgM$T_}0nCwQPrBWT9<*(tg<$CoMF&xd!HqK!wg;QdarkWx*)2&NOI{Q^$^fhYN?kmC2~hg7vbUbQvzB{ljwo-qSgvQD(~ScRyRc0p&MR3dNAnWWwSqT;uu<UB3B$^IY>j!iF>V}1e7us?n1me=3{>Hibgk`JN>MkM=`LR3dHPb|E%{a3(pu~iyf|N`6-%aFQb~5<gDU(IQ;g0~U&*%Q_{G5)r-hR_rMBdj>tqP*MM;z`LQ-mjWn_;?vTitg1{?g?pfsM7vNv_iihHxjv67G9>I8)h@czI1(Deeq4@VV6CezpwD_8ee6l#veqjjO@ijY*E2kjGUL3?Q-D8o_+M0$#uwBZ1=o3aq}77R9J6^PeXf#@~t^J3ng%>OoGIcSlYwv4Ek7BqB_L3V2+%G#bsXf=TO7j-vjZlKqL1C^h>1DhDD19Ja8I0v0*LBT)d`C<Sxu`$)lyz9sRjCn=epMVs*9BUUuVqce`Lust8&M~rIT4E;s8`n@pqradkF2f5UMd=Jrgc^{*L>of}J-9-MXRz6>D`lNnq9}yo2uMowHqIA`6MoGsQtQn-nUhgZglk_*1Q*eslw;dYd26D6ps|9OtmWOy3k`L?sV+=TdaKBVagZ0lL#$r(7uId^Hjw-MP6RdDl`)IXOQyiW8u2EN??zn~<33|6U^G#RsfHt<QGTOoa3*e?t;mE4BpPdG5C6mKu)k&4!ygw`H5~8^PhGGvA6zLjY0Sqm;GL-ntQbcEj=*8RaEzEa?7>^CIqXpjtR$4s1j~p@L;0S=EX@Z0>P&;Oo);AsEXkLIs{2x<h2fV^@}IwQ?8T<y)ZB}0Unt{s$$!>Y@}J$!`OlU)vE1(yDdY8t3!C8cNMIgiK6f|xujL)>H}qd?&+?y#8}gs@Uwg)UZBbI7{gWxsRL1<=cI}uTjvMh^A&AFWMzp<55O)`S)~@D71w*`)6it+=0Hf+@do^&UMsGDrE$7D=_@`X(MtPv>YJxOcg49!4cd}HwkS67naGR4FHgO-GDRp1mH*MoScpfLW*r1{Y+%@&o0)L%^$7=#piqeTm!Z>M|(}YZm@6puH#k<zQ$7Dc}5=(L^U_KzEk5~_)5jwRh)MZsjPp=C6;({BoOA7<Hc-5r5(v{`mZd@Ls>3{k1pe+wvQH=MD77;d<k4>vcartYwb~l_RwUG1%;83GY;%lCZkfY$Sv!w;EANX#6c0S`TS}m5}T~LEx-X?-{+1*q=tgJvv?`Z{!vlVDF>dXg1u;U~?fArJU33ZDm6QR88#s`=IzO;4d-}CvFtKpL_S3fvgu5Pgl6<+8kc{h@<A^A|pP^Gk<bqp<w7IZNt$I$mzRZTDyqRb2fR<G`S_42Iq701wdRj+?)4P*M<b3K@?WQpjL<CP3r>T(RF(31e>M@!n@adAo0!LOQzashxYZiV|^yPYe(p-_$YYv$;+$T=-?0iOW?Fdw<TUIlccg{RwNu4E1zY7*EVToOO=3PBqkxq5ER<2Gx!w(K$VDJvgLx1Y8S6=W|NM&}DIgn#XWa*ND(gZ)hpriL4unj4yq8=B@kxs8gCTxN0v*rwTT1`tBJz|>YfNmP;ORDept-`N7zyIDe;y~eWH_3^sJ;a|^}u6(bWYa1G_Ta7j`T(PhtC2TNa^rLu{r+DUv7DCTCEgo2b#58N5f8p+fEao|3blAJ((Yf%_Ho=}|k@qwUye?}PXu>q?aSKxm%y)cUyi|v?JjUI)l^KKqwhavwGks{OG$^C1+`DQb{yyK5(ER0(shMDB9ZR*OLhV@oqjf*4mgIZ5yi_gmPD1*Mpb&burAPwHnX7S;IodQTk4!0Rgv?7Ea9vp57Wp`c7WNG|7za{K^1MzeT_x9@+{K`{(>VdpADBoO?g3}ZGst($Htrkldx-==(gP4rxg?=zmoNEIUbh~K7#*|qwNkIF)c#yV?~3#b#M)Ks-Lf4+1z;JVpxJ(DmUsQ%et0s3S@zu16In;_16v_R#@sQSB}3>h29h|SqBkc)oY|ON2!0uKH|<mji_e9<L;K|1(VitkR0+#}7aYmMm<++HEyXCp_fYFnn=FG&WY{nAM3elgnQC1~hLA7aHYEqzSSEzvVZ>l<i9^$v1Er?YIDM?2&V+n%c;)a<gT4BrDy^{3$-@RQMT2@ZO!Af(<mr*ChVTpbZtFQ*X=|FS#D((vcIysEJNkNun+#$mN2yQ@H4%0LA!$n`J@b^o(mX3F6nYs|NAAt;no$YrA?+Pgw3StLfC{+R1J)(s#)_Uh6zleMz}&mxyX^zce?J2Hhz)!vg{}?J_O*(}K$p}!ZQPn|*-DZ3m^aaN0#YY0ME83MS{v;l{+3bEM$$jBzJ^d8$U{Rk`3L~wX3rZOjeoJ(16=Hg2#uS(S49u#TVm@AofJ5~fzDs7H~|z$LgPKbj;P#F4OpAsJOu~hQRL#~DI*8~V#~cxYa6=U*gbZ{%%Je#J-ti3W%mKxj2kLSvCS4<><`zrCNjDXg2*~e`gv%*3HaUk5MUq2pWg2YRUz3dZ4f&emD2-R(dyug*>XhQY}`g4V5@8A=S?&aPLAArSMm){|I3HZd$9loxVaBBG)ww&gaSt08ik>bm)5<Ocm`Yd1mi&k^(lOSt$Q@W5P$J_>C==r3^%|6W|QIJ$ppYDEWjHDqb0|T8!^ONE!6^2OBfYL&d#HTaEbs37SFZZ6f6kjIDrBjRAEx>KmWvvXaL1nGRYzophZ<0anst+09cK+Uk?|{MaSH&k%gtMx}iwuxMdGtN$6|wyC1a<1NlQj1cxH#nPA=`sC*^{lbz7yr->>JLKE3zXK4xwhJv8zmG#&wTT>v|xud=r_{C0)UjmVGM-_I(dl^B-G#Elny7~Y<jh&R$vJQy!NYzZ17i&;(tizu7)`VK2sku@xv!=g&gmxo(D=3!EbTqw}^syud4e1WHV*s}T6up+<d|V4IXJIS5_1}EXZ)(<`h(F*F@`x8_-kb{1ivy7Q<^_k`9yO`Z@$oSwum-quj(wRKjQsA3!6K0@hvUtHvQGKD^UtZ2jvuYYEkoXOoQec3X5IF?&%OBP`}N-#$}f-UA6LUW*S?vf{J1<4=+`CILlf$x`Ap$Iky~_ojP+~Sa~p#^hQ2uVc37A4oUtO!DVYo;kq{1vl5W&jByWB2B;xf{EcOOZwJoXG8PpzXTlvLONZV|A0R04tnc|AEHl_T=l=9K!qY7H*q!5J)cFV}Zi7(q={gZi*Xkf5g08f|pUO__ygrq)L5}}tc0u*441?#<ePDs&JX-xSlljs3%bw115pfp@9^5nRkbn90z^Tq;j%uMB+*!Z=2O&sSwY(Nk+wE**cv7F@l|D&l2{DW$r;<J|rC$GOg{jjI6?fJQ%zP9jd3%|DT>(kd3{*b5s(>(Pb@b&bPchhG%?T>x>g+hqej`{`LHhsF^N`H{s*1!0>@yVwz`tBd7PU}DJssBVz)6Gvk^Yw1_bbeNPI=<^(@bu`hyXi410mPi#{I^np`1HkC9@H;6puharTs1>+ex&h-z1|o7f#AmDT=-`i7u8%5(xgcsN60)RvzL6O;S(NL#%82wR$^_0Xu^qdkb}rfur&ONa+u<Pm`N0qCCqq+(W8@}rP&S(vAhMr%bQCIlS;j~@o5O<#ZaEQ@^=JtNjS=#{tb5F(*e!Kl=)I7iJTOWkACs^>G*Z4#_0I|@-LqJx}Trq?7GGuEhmHam-dx?#;iYarPGD`*-!hYPD6G^!C5tq_D>umiEp)?69KH;5j{Bi>&n;7jK*FGZfeG(D~d<WsN1TO*R_OV2{B#Kjm^j(wV=z*x=>&iHkL~mAB5`i6<z=9XHV_?O(wAzxao24<~MhK`%drXv-ij_m}A2V7Al3tMk2jM9f)OA))DFKbM<fF-^wm$dd2?wvICOni!f~EvHs#vjlJSrc@WNC8IHciCYn9<m!D2wA0PPZuRQTBSDjyJ6{p9(d_Xoy7n(v}aYyHQ(<MB8R>u!2fA#n%sFjb6x1hYja`F5tXJ<aPfQv_0=Z^3D^s(y?&i|q6KYQxNmTavvjE|?!jGf0FJ#eL+r&~6E?57tm-<{JJ$+N$5H&2@4iDtRIan2vu@^RLN)zp|M@1HcOn>DrbM=f*GN^w-T@-vt1Q#<eS_b8G7Pr;itxb!oYFLQhRXsTKY#4t#T`;j7Cm1`&_0HdJ|I8uXXZ<U9>NnTNDosnwl&Tbu*1u4AOy2GaWw(`S0b+aqK?Fls^HbB*&mTqqOi`xfM=J>^Rp0GO;Dc8&<L$O#irHSCE9=*Ri0O=0MZ7<zvR7GVZ*~IGZ4kc0VMqyG{)3Pl;Ue?4z<RGS@2x35W=aEp{<%9c18Xm9)G3j&wDgIjZ5flbY*&AojyN&Y$p;!5g)+gvIsfQ45*O(0EoE82Q`l@zud4jSd`U=GGPY1ms+8|zpUghSei$*@1wjc~pq-`#NuJTzCsk~awL096f(m-!O0}jDlXT<`bJ`nUNUx>SMXSgeW=ZZp#`~0}8f8j$>zlK|LD*&@nG8KVSv|dkj5)e@Qg!COIjTQ9~h=i<9uqbX=yLf`-y;EOsYdM0AB*c8@A>AWd3CUd~gbFK=Z}qCf0bMIKSxQ1gmR4DheajxPFu{NVXeTjqy_WEf|Hg>?WxHCg5uw`P&=Ujw=_>d5KUyVw$3}gsl1<A1GJfF^)?KP(=dM;u4R$JH2g>lEl1<f}71b=!Lhi{jHX)Xt#L8%TC&!g+3UzzZil$07MVj)#Rflc~k7!QxEn!}HT*+RV^1mDyT7pAR%&yOh+0x;)sF$a`f{1B1;va-FQ)EFcUKfRPP%#^`aYN}I?(hQj-ve;Hv1rpr=oqYK;*<GSH>N)cjwwflOn<NHPimuZZlv_ZD%|mRUn|_N74FyC)$7yO4*c4IUt9RKy!~3<el2gmmbYKa+pp#A*YfsjdHeTOd3*f8Nrn5QyzQ*QUCP_Bl(!wv+pG=o<!EA_jTJkibYr|(pL^E1gYwg?MlMO>^CJmOHj1UXIhH4-JJ~&7<Q^-dW4Tw1z>^}PkC&^zEWTFr+P39Xyxa~bA{&qDlt;gQem=7!KT+GZADY$6QPl6Q9%_E2Ph953y6IHUHd{VsP&;dF-_;{iV{HFxCGD&A>~3};;i#BBuVfoHWLA}bz8F8&uzfW@6P>x0t9458s2+cMEp>HXvk%np8^H}KTH}Y3bpYdFhSSpZ`8~Q7Uf|qO-Fnp3;hm-7uu;r7LMqj;t$<z1sMpHaV`*)y=DL$Yptow7zffNFM^)SNx^??h-P-QXc`?}CP!XRMeG6pd==FIix0+vFm{msYMbD0Xxt95C#rj1h>hlNwiK4YD%T{@%eAwG;b3?^?{@1^}Ts`kC-XGOj)v8k!)?cby$La6I8tt{-IImt`Mpr!ZfhX_j4SzqdTz%zi-E0uqX-9kPbVHk`YS?}@e$N}tyJ`JBdf>0WWvoy>JxbpHV>g!A(z$4NhYAp+TT@}-<{5N<CV$eLs&o$&K%G_D=m5I)>9_`)AoYLbXE5Bs>3bO9*<{5vnIGlH53Vk{27Twc-kCKmRTcalV0R6ReThs&2ni4c1Wn$ZRM(;U73iJO1{Aa!)YM75m6On){BV8q(o~6Nb7-f#DutVxDqL!+{<x{y<EBd9s*%G?zI>&EWbjMY4412^{ESO~KxJ3$SD&?CecXP~lU$<xx+mMOCG~u2zd!yd+wVd@J8rq*xn>I&x)<Bb8f+LVxNx~vQ@MQR@&U+Svqp;Z7Mgdjv$lDYTV>WH|38&B_eT'
_V92_P_INDEX = [(0, 26434), (26434, 14995), (41429, 22894), (64323, 36532), (100855, 36284), (137139, 12706), (149845, 26250), (176095, 10127), (186222, 19706), (205928, 14953), (220881, 26817), (247698, 28168), (275866, 21787), (297653, 41149), (338802, 19710), (358512, 22885), (381397, 20570), (401967, 13510), (415477, 18968), (434445, 18728), (453173, 18185), (471358, 25392), (496750, 32292), (529042, 29822), (558864, 32507), (591371, 19689), (611060, 17846), (628906, 25600), (654506, 14773), (669279, 31114), (700393, 30120), (730513, 16452), (746965, 19255), (766220, 18231), (784451, 16214), (800665, 13566), (814231, 16185), (830416, 23337), (853753, 13578), (867331, 25882), (893213, 21267), (914480, 23783), (938263, 15989), (954252, 15367), (969619, 29093), (998712, 21251), (1019963, 23186), (1043149, 27871), (1071020, 14148), (1085168, 18157), (1103325, 19292), (1122617, 35008), (1157625, 26356), (1183981, 23583), (1207564, 18410), (1225974, 12448), (1238422, 32383), (1270805, 14434), (1285239, 22229), (1307468, 14224), (1321692, 24101), (1345793, 21833), (1367626, 13531), (1381157, 25364)]
_V92_P_RAW = None


def _v92_p_lib():
    global _V92_P_LIB, _V92_P_RAW
    if _V92_P_LIB is None:
        _V92_P_LIB = {}
    return _V92_P_LIB


def _v92_p_pair(shops):
    lib = _v92_p_lib()
    if shops in lib:
        return lib[shops]
    global _V92_P_RAW
    names = ['BAKERY', 'BRUNCH_SPOT', 'FARMERS_MARKET', 'ICE_CREAM_SHOP', 'PET_CAFE', 'PIZZA_SHOP', 'SMOOTHIE_SHOP', 'YARN_STORE']
    out = []
    if len(shops) == 2 and shops[0] in names and shops[1] in names:
        if _V92_P_RAW is None:
            _V92_P_RAW = _v92_zlib.decompress(_v92_b64.b85decode(_V92_P_BLOB))
        start, length = _V92_P_INDEX[names.index(shops[0]) * 8 + names.index(shops[1])]
        raw = _V92_P_RAW; pos = start
        n = raw[pos] | raw[pos + 1] << 8; pos += 2
        for _ in range(n):
            m = raw[pos] | raw[pos + 1] << 8; pos += 2
            ev = {}; last = 0
            for _ in range(m):
                d = raw[pos]; pos += 1
                if d == 255:
                    t = raw[pos] | raw[pos + 1] << 8; pos += 2
                else:
                    t = last + d
                ev[(t, raw[pos])] = raw[pos + 1]; pos += 2; last = t
            out.append((-1, ev))
    lib[shops] = out
    return out


def _v92_p_update(obs, st):
    player, step = int(obs["player"]), int(obs["step"])
    race = _V9_RACE.get(player) or {}
    prev = race.get("prev")
    if not prev or prev["step"] != step - 1:
        return
    inv = obs["market"]["inventory"]
    draw = _v9_town_draw(prev["shops"], prev["step"])
    for i, item in enumerate(_V92_P_ITEMS):
        if prev["prices"].get(item, 0) <= 3:
            continue
        sold = inv[item] - prev["inventory"][item] + draw.get(item, 0) - prev["own"].get(item, 0)
        if sold >= 2:
            st["obs"][(step - 1, i)] = sold


def _v92_p_forecast(obs, st):
    step = int(obs["step"])
    shops = tuple(obs["town"]["unlocked_shops"][:2])
    cands = _v92_p_pair(shops)
    if _V92_EP is not None:
        cands = [c for c in cands if c[0] % 2 != _V92_EP % 2]
    seen = st["obs"]
    lo = step - 240
    scored = []
    recent = [(tt, i) for (tt, i) in seen if tt >= lo]
    for ep, ev in cands:
        m = f = 0
        for (tt, i), q in ev.items():
            if lo <= tt < step - 1:
                if (tt, i) in seen or (tt - 1, i) in seen or (tt + 1, i) in seen:
                    m += 1
                else:
                    f += 1
        miss = sum(1 for (tt, i) in recent if (tt, i) not in ev and (tt - 1, i) not in ev and (tt + 1, i) not in ev)
        scored.append((m - 0.5 * f - 0.5 * miss, ev))
    scored.sort(key=lambda x: -x[0])
    return [ev for _, ev in scored[:_V92_P_TOP]]


def _v92_predict(obs, action, st):
    step = int(obs["step"])
    _v92_p_update(obs, st)
    if step < 150 or step >= 700:
        return action
    if step % _V92_P_EVERY == 0 or "best" not in st:
        st["best"] = _v92_p_forecast(obs, st)
    best = st["best"]
    if not best:
        return action
    native = _IMPL.chassis.players.get(int(obs["player"]))
    if not native or native.get("route") not in _IMPL.chassis.routes:
        return action
    tape = _IMPL.chassis.routes[native["route"]]
    market = [list(o) for o in action.get("market") or []]
    already = {o[1] for o in market if len(o) > 1 and o[0] in ("SELL", "BUY_PRODUCT")}
    stock = projected_shed(action, FarmView(obs))
    changed = False
    for i, item in enumerate(_V92_P_ITEMS):
        if item not in _V92_P_USE or item in already or len(market) >= MAX_ORDERS:
            continue
        votes = sum(1 for ev in best if ev.get((step + 1, i), 0) + ev.get((step + 2, i), 0) >= _V92_P_K)
        if votes < 1:
            continue
        ours = 0
        for t in range(step + 1, min(len(tape), step + _V92_P_H + 1)):
            ours += sum(min(100, int(o[2])) for o in (tape[t] or {}).get("market") or []
                        if len(o) >= 3 and o[0] == "SELL" and o[1] == item)
        qty = min(int(stock.get(item, 0)), ours)
        if qty > 0:
            market.insert(0, ["SELL", item, qty])
            _V92_P_REPORT["pred_units"] += qty
            _V92_P_REPORT["pred_fires"] += 1
            changed = True
    if not changed:
        return action
    result = dict(action)
    result["market"] = market[:MAX_ORDERS]
    return result


_V92_P_PARENT = agent


def agent(observation, configuration=None):
    player, step = int(observation["player"]), int(observation["step"])
    st = _V92_P.get(player)
    if st is None or step <= st["step"]:
        st = _V92_P[player] = {"step": -1, "obs": {}}
    st["step"] = step
    action = _V92_P_PARENT(observation, configuration)
    try:
        return _v92_predict(observation, action, st)
    except Exception:
        _V92_P_REPORT["pred_errors"] += 1
        return action


agent.telemetry = _V92_P_REPORT
agent = globals().pop("agent")



# ---------------------------------------------------------------------------
# v9/2 PREDICT2: forecast the rival's premium sales from the whole library of
# recorded streams (every shop pair) and sell our planned lots just before theirs.
#
# Rival sales are recovered each turn like RACE (inventory delta + town draw - own
# sales).  Every library stream keeps an incremental score over the whole game:
#   matched ticks - PF * unmatched library ticks - PM * unmatched rival sales
# (+-1 turn tolerance, MILK / WOOL / STRAWBERRY).  The per-sale miss term is the same
# for every stream except those with a nearby tick, so the argmax is maintained from
# an inverted (tick, item) -> streams index.  When the best stream sells >= K units of
# a product in the next two turns, the tape's planned sales of it within H turns are
# sold now.
# ---------------------------------------------------------------------------
import json as _v92_json, os as _v92_os
_V92_Q_ITEMS = ("MILK", "WOOL", "STRAWBERRY")
_V92_Q_H = 48
_V92_Q_K = 4
_V92_Q_PF = 1.0
_V92_Q_PM = 0.5
_V92_Q_CACHE = {}
_V92_Q = {}
_V92_Q_REPORT = dict(pred_units=0, pred_fires=0, pred_errors=0)


def _v92_q_streams():
    """List of (ep, {(tick, item_index): qty}) over MILK/WOOL/STRAWBERRY (item index into _V92_Q_ITEMS)."""
    if "streams" not in _V92_Q_CACHE:
        path = _v92_os.environ.get("V92_SELL_LIB")
        out = []
        if path:
            for x in _v92_json.load(open(path)):
                ev = {(t, i): q for t, i, q in x["ev"] if i <= 2}
                if ev:
                    out.append((x["ep"], ev))
        _V92_Q_CACHE["streams"] = out
    return _V92_Q_CACHE["streams"]


def _v92_q_index(parity):
    key = ("index", parity)
    if key not in _V92_Q_CACHE:
        evs = [ev for ep, ev in _v92_q_streams() if parity is None or ep % 2 != parity]
        index = {}
        for c, ev in enumerate(evs):
            for k in ev:
                index.setdefault(k, []).append(c)
        _V92_Q_CACHE[key] = (evs, index)
    return _V92_Q_CACHE[key]


def _v92_q_new_state():
    parity = None if _V92_EP is None else _V92_EP % 2
    evs, index = _v92_q_index(parity)
    n = len(evs)
    return {"step": -1, "obs": {}, "evs": evs, "index": index, "m": [0] * n, "f": [0] * n, "near": [0] * n,
            "score": [0.0] * n, "best": 0 if n else None, "done": 150}


def _v92_q_update(obs, st):
    player, step = int(obs["player"]), int(obs["step"])
    race = _V9_RACE.get(player) or {}
    prev = race.get("prev")
    seen = st["obs"]
    if prev and prev["step"] == step - 1:
        inv = obs["market"]["inventory"]
        draw = _v9_town_draw(prev["shops"], prev["step"])
        for i, item in enumerate(_V92_Q_ITEMS):
            if prev["prices"].get(item, 0) <= 3:
                continue
            sold = inv[item] - prev["inventory"][item] + draw.get(item, 0) - prev["own"].get(item, 0)
            if sold >= 2:
                seen[(step - 1, i)] = sold
    evs, index = st["evs"], st["index"]
    if not evs:
        return
    m, f, near, score = st["m"], st["f"], st["near"], st["score"]
    best = st["best"]
    rescan = False
    # finalize ticks up to step-2 (their +-1 neighbourhood of observations is known)
    while st["done"] <= step - 2:
        tau = st["done"]
        st["done"] += 1
        for i in range(3):
            hit = (tau, i) in seen or (tau - 1, i) in seen or (tau + 1, i) in seen
            for c in index.get((tau, i), ()):
                if hit:
                    m[c] += 1
                    score[c] += 1.0
                else:
                    f[c] += 1
                    score[c] -= _V92_Q_PF
                    if c == best:
                        rescan = True
            if (tau, i) in seen:
                touched = set(index.get((tau - 1, i), ())) | set(index.get((tau, i), ())) | set(index.get((tau + 1, i), ()))
                for c in touched:
                    near[c] += 1
                    score[c] += _V92_Q_PM
                    if score[c] > score[best]:
                        best = c
            for c in index.get((tau, i), ()):
                if score[c] > score[best]:
                    best = c
    if rescan:
        best = max(range(len(score)), key=score.__getitem__)
    st["best"] = best


def _v92_predict2(obs, action, st):
    step = int(obs["step"])
    _v92_q_update(obs, st)
    if step < 150 or step >= 700 or st["best"] is None:
        return action
    ev = st["evs"][st["best"]]
    native = _IMPL.chassis.players.get(int(obs["player"]))
    if not native or native.get("route") not in _IMPL.chassis.routes:
        return action
    tape = _IMPL.chassis.routes[native["route"]]
    market = [list(o) for o in action.get("market") or []]
    already = {o[1] for o in market if len(o) > 1 and o[0] in ("SELL", "BUY_PRODUCT")}
    stock = None
    changed = False
    for i, item in enumerate(_V92_Q_ITEMS):
        if item in already or len(market) >= MAX_ORDERS:
            continue
        if ev.get((step + 1, i), 0) + ev.get((step + 2, i), 0) < _V92_Q_K:
            continue
        ours = 0
        for t in range(step + 1, min(len(tape), step + _V92_Q_H + 1)):
            ours += sum(min(100, int(o[2])) for o in (tape[t] or {}).get("market") or []
                        if len(o) >= 3 and o[0] == "SELL" and o[1] == item)
        if stock is None:
            stock = projected_shed(action, FarmView(obs))
        qty = min(int(stock.get(item, 0)), ours)
        if qty > 0:
            market.insert(0, ["SELL", item, qty])
            _V92_Q_REPORT["pred_units"] += qty
            _V92_Q_REPORT["pred_fires"] += 1
            changed = True
    if not changed:
        return action
    result = dict(action)
    result["market"] = market[:MAX_ORDERS]
    return result


_V92_Q_PARENT = agent


def agent(observation, configuration=None):
    player, step = int(observation["player"]), int(observation["step"])
    st = _V92_Q.get(player)
    if st is None or step <= st["step"]:
        st = _V92_Q[player] = _v92_q_new_state()
    st["step"] = step
    action = _V92_Q_PARENT(observation, configuration)
    try:
        return _v92_predict2(observation, action, st)
    except Exception:
        _V92_Q_REPORT["pred_errors"] += 1
        return action


agent.telemetry = _V92_Q_REPORT
agent = globals().pop("agent")

# ---------------------------------------------------------------------------
# v9 RACE: fit the sale-reservation horizon to the rival's observed sale lead.
#
# Premium books crash within ~60 units of glut, so the first seller of a lot
# takes the price and the second sells into the crash.  The parent reserves
# planned tape sales a fixed four turns ahead; any deeper fixed horizon beats
# it head-to-head, but selling earlier than necessary gives away town-demand
# recovery against a rival that does not race.
#
# Everything here is public.  Each turn the rival's executed sales are
#
#   rival_sold[p] = inventory'[p] - inventory[p] + town_draw[p] - own_sold[p]
#
# (exact above the $1 floor, where sales never enter inventory).  When the
# rival sells a product while we still hold stock that our tape sells later,
# and the sale is not a late fill of our previous lot, the turns until our next
# planned sale are the rival's lead.  One horizon serves every product:
#
#   horizon = clamp(largest lead seen + RACE_MARGIN, RACE_DEFAULT, RACE_MAX)
#
# and it also lifts the parent's 72-turn block bound (patched into the
# parent's reservation by the release builder).
#
# v9/2: the shipped horizon is 40 turns with a 12-turn margin (was 6 and 4).
# Mirrors are the ladder's real opponent, and the premium books are first-come
# races, so reserve depth is the whole decision.  Against the 6/4 build the new
# setting wins 73-7 (+308) over 80 mirror games; against the shipped 32/12 build
# it wins 74-6 (+358).  Deeper is not better: 44/12 beats 40 head to head but
# drops the shallow-baseline record to 65-15, and 48/12 (a constant 48) falls to
# 14-26 against it, because a horizon past the rival's next lot gives up
# town-demand recovery for nothing.  The frozen top-30 stream panel is unchanged
# inside its noise (52.2% / +2,797 over 178 games vs 52.8% / +2,929 at 32/12) and
# the public field still goes 8-0.
#
# v9/2b: the reservation window starts at step 192 (day 8) instead of 288 (day 12),
# a one-line change in the parent's `_r36_reserve` gate made by the release builder.
# The herd's first milk and wool lots land on days 8-11 and the same-day sale
# reservation is what takes their price before a rival's lot lands; the two middle
# days of the tape's own schedule give that up.  Three fresh mirror blocks against
# the step-288 build: 32-0 (+147), 30-2 (+11), 30-2 (+10); and against the shallow
# 6/4 baseline the new build is if anything stronger, not weaker: 28-4 (+556) vs
# 28-4 (+406), 29-3 (+272), 31-1 (+359) vs 31-1 (+349).  Per-item horizons instead of
# one global horizon change nothing once the window starts at 192 (28 of 32 games
# identical), so the one-line gate is the whole change.
# ---------------------------------------------------------------------------
V9_RACE_DEFAULT = 40
V9_RACE_MAX = 48
V9_RACE_MARGIN = 12
V9_RACE_GAP = 3            # a sale this soon after our previous planned lot is a late fill
V9_RACE_WINDOW = 30        # turns of tape searched for planned sales around a rival sale
V9_RACE_ITEMS = ("CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL")
_V9_SHOP_ITEMS = {
    "BAKERY": ("EGG", "WHEAT"), "PIZZA_SHOP": ("MILK", "TOMATO", "WHEAT"),
    "BRUNCH_SPOT": ("EGG", "WHEAT", "STRAWBERRY"), "YARN_STORE": ("WOOL",),
    "ICE_CREAM_SHOP": ("STRAWBERRY", "MILK", "WHEAT"), "PET_CAFE": ("CARROT",),
    "SMOOTHIE_SHOP": ("STRAWBERRY", "MILK"),
    "FARMERS_MARKET": ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY"),
}
_V9_RACE = {}
_V9_RACE_REPORT = dict(rival_sales=0, leads=0, race_errors=0)


def _v9_town_draw(shops, step):
    """Units each shop instance and the town centre remove after `step`'s market."""
    draw = dict.fromkeys(V9_RACE_ITEMS, 0)
    if step % 4 == 0:
        for shop in shops:
            items = _V9_SHOP_ITEMS.get(shop, ())
            for item in items:
                if item in draw:
                    draw[item] += 2 if len(items) == 1 else 1
    if step % 24 == 0:
        for item in draw:
            draw[item] += 1
    return draw


def _v9_planned_sells(tape, item, step):
    """Turns within V9_RACE_WINDOW of `step` at which the tape sells `item`."""
    out = []
    for t in range(max(0, step - V9_RACE_WINDOW), min(len(tape), step + V9_RACE_WINDOW + 1)):
        if any(o and o[0] == "SELL" and len(o) >= 3 and o[1] == item and int(o[2]) > 0
               for o in tape[t].get("market") or []):
            out.append(t)
    return out


def _v9_race_update(obs, st):
    """Recover last turn's rival sales and record the leads that prove racing."""
    prev = st["prev"]
    step = int(obs["step"])
    if not prev or prev["step"] != step - 1:
        return
    native = _IMPL.chassis.players.get(int(obs["player"]))
    if not native or native.get("route") not in _IMPL.chassis.routes:
        return
    tape = _IMPL.chassis.routes[native["route"]]
    inventory = obs["market"]["inventory"]
    draw = _v9_town_draw(prev["shops"], prev["step"])
    t = prev["step"]
    for item in V9_RACE_ITEMS:
        if prev["prices"].get(item, 0) <= 3:
            continue
        sold = inventory[item] - prev["inventory"][item] + draw[item] - prev["own"].get(item, 0)
        if sold < 2:
            continue
        _V9_RACE_REPORT["rival_sales"] += 1
        if prev["left"].get(item, 0) <= 0:
            continue
        planned = _v9_planned_sells(tape, item, t)
        after = [s for s in planned if s >= t]
        before = [s for s in planned if s < t]
        if not after or (before and t - before[-1] < V9_RACE_GAP):
            continue
        st["lead"] = max(st["lead"], after[0] - t)
        _V9_RACE_REPORT["leads"] += 1


_V9_RACE_PARENT = agent


def agent(observation, configuration=None):
    player, step = int(observation["player"]), int(observation["step"])
    st = _V9_RACE.get(player)
    if st is None or step <= st["step"]:
        st = _V9_RACE[player] = {"step": -1, "lead": -V9_RACE_MARGIN, "prev": None}
        if step == 0:
            _V9_RACE_REPORT.update(rival_sales=0, leads=0, race_errors=0)
    st["step"] = step
    try:
        _v9_race_update(observation, st)
        horizon = min(V9_RACE_MAX, max(V9_RACE_DEFAULT, st["lead"] + V9_RACE_MARGIN))
        _V9_ITEM_HZ[player] = dict.fromkeys(V9_RACE_ITEMS, horizon)
    except Exception:
        _V9_RACE_REPORT["race_errors"] += 1
        _V9_ITEM_HZ.pop(player, None)
    action = _V9_RACE_PARENT(observation, configuration)
    try:
        stock = projected_shed(action, FarmView(observation))
        own = {}
        for o in action.get("market") or []:
            if o and o[0] == "SELL" and len(o) >= 3 and o[1] in V9_RACE_ITEMS:
                n = min(max(0, int(o[2])), max(0, stock.get(o[1], 0) - own.get(o[1], 0)))
                own[o[1]] = own.get(o[1], 0) + n
        st["prev"] = {"step": step, "inventory": dict(observation["market"]["inventory"]),
                      "prices": dict(observation["market"]["prices"]), "own": own,
                      "left": {item: stock.get(item, 0) - own.get(item, 0) for item in V9_RACE_ITEMS},
                      "shops": list(observation["town"]["unlocked_shops"])}
    except Exception:
        _V9_RACE_REPORT["race_errors"] += 1
        st["prev"] = None
    return action


agent.telemetry = _V9_RACE_REPORT
agent = globals().pop("agent")


# ---------------------------------------------------------------------------
# v9 RACEPX: lead-sell a planned lot early only while its book is not glutted.
#
# The engine prices a product off the market inventory: below I0 the quote is above
# base, above I0 it is below.  The lead sale moves a lot one turn ahead of the tape's
# own plan, which is what takes the price when both sides hold the same lot -- but
# when the book is already above I0 the same units only fetch a lower price, and the
# town drain between the two turns is not enough to pay for it.
#
# Measured against the frozen top-20 streams the shipped build realizes below-base
# prices on exactly the products it floods (strawberry $107-123 vs a $120 base, milk
# $98-107 vs $160, wool $129-139 vs $200, melon $212 vs $250, fertilizer $43 vs $100)
# and above base on the ones the town drains (wheat $38 vs $25, carrot $54 vs $35,
# tomato $125 vs $60, egg $52 vs $50).
#
# This layer keeps the lead sale for products quoted at or above base + MARGIN and
# leaves the rest to the tape's own schedule.  The reservation (`_r36_reserve`) is
# untouched, so the RACE horizon still governs how far ahead lots may be pulled.
#
# Evidence (v9/3): mirror against the shipped build 35-13 (+220) over 48 fresh games;
# against the 6/4 ancestor 41-7 (+620) where the shipped build is 45-3 (+449); frozen
# top-20 panel 69/120 (+3,586) against 66/120 (+3,364); second panel 63/120 (+2,264)
# against 63/120 (+1,882); public field pool unchanged (14-2 vs cdb and fh11, 16-0
# vs fa103/fa141/fa238/wd14).
# ---------------------------------------------------------------------------
V9_RACEPX_BASE = {"WHEAT": 25, "CARROT": 35, "TOMATO": 60, "STRAWBERRY": 120, "MELON": 250,
                  "EGG": 50, "MILK": 160, "WOOL": 200, "FERTILIZER": 100}
V9_RACEPX_MARGIN = 0
_v9_racepx_report = dict(racepx_skipped=0, racepx_sold=0, racepx_errors=0)
_V9_RACEPX_LEAD = Chassis._sell_lead


def _v9_racepx_lead(self, action, view, projected, route, step, next_sup):
    prices = view.prices
    blocked = {i for i in V9_RACEPX_BASE
               if prices.get(i, 0) <= V9_RACEPX_BASE[i] + V9_RACEPX_MARGIN}
    if not blocked:
        _v9_racepx_report["racepx_sold"] += 1
        return _V9_RACEPX_LEAD(self, action, view, projected, route, step, next_sup)
    nxt = step + 1
    unlock_period = 3 * self.cfg["turns_per_day"]
    if nxt > LAST_ACT_STEP or nxt % unlock_period == 0 or step % 4 == 0:
        return
    tape = self.routes[route]
    future = tape[nxt] if nxt < len(tape) and isinstance(tape[nxt], dict) else {}
    planned = {}
    for o in future.get("market") or []:
        if o and o[0] == "SELL" and len(o) >= 3 and o[1] in PRODUCTS:
            planned[o[1]] = planned.get(o[1], 0) + max(0, int(o[2]))
    already = {o[1] for o in action.get("market") or [] if o and o[0] == "SELL" and len(o) > 1}
    for item in PRODUCTS:
        if item in blocked or item in already or planned.get(item, 0) <= 0:
            continue
        qty = min(projected.get(item, 0), planned[item])
        if qty <= 0 or prices.get(item, 0) < self.cfg["min_sell_price"]:
            continue
        if not self._add_sell(action, item, qty, self.cfg["max_orders"], merge=False):
            break
        projected[item] -= qty
        next_sup["suppress"][item] = next_sup["suppress"].get(item, 0) + qty
        _v9_racepx_report["racepx_skipped"] += 1
    if next_sup["suppress"]:
        next_sup["due_step"] = nxt


_V9_RACEPX_PARENT = agent
Chassis._sell_lead = _v9_racepx_lead


def agent(observation, configuration=None):
    if int(observation["step"]) == 0:
        _v9_racepx_report.update(racepx_skipped=0, racepx_sold=0, racepx_errors=0)
    try:
        return _V9_RACEPX_PARENT(observation, configuration)
    except Exception:
        _v9_racepx_report["racepx_errors"] += 1
        return {"farmer": ["PASS"], "hands": [], "market": []}


agent.telemetry = _v9_racepx_report
agent = globals().pop("agent")


# ---------------------------------------------------------------------------
# v9 RACEGATE: the same glut gate for the *reservation* (the 40-turn pull-forward).
#
# `_r36_reserve` moves tape-planned sales up to the RACE horizon forward, item by
# item.  RACEPX only gated the one-turn lead sale; this layer gates the reservation
# too: an item whose quote is at or below its base price is left to the tape's own
# schedule.  The debt ledger is untouched for the items that are still reserved, so
# suppression stays consistent.
#
# Evidence: see README (v9/3 round).
# ---------------------------------------------------------------------------
V9_RACEGATE_BASE = {"WHEAT": 25, "CARROT": 35, "TOMATO": 60, "STRAWBERRY": 120, "MELON": 250,
                    "EGG": 50, "MILK": 160, "WOOL": 200, "FERTILIZER": 100}
V9_RACEGATE_MARGIN = 0
_v9_racegate_report = dict(racegate_reserved_units=0, racegate_errors=0)
_V9_RACEGATE_RESERVE = _r36_reserve


def _r36_reserve(obs, action):
    step = int(obs["step"])
    if not 192 <= step < 696:
        return action
    prices = obs["market"]["prices"]
    glutted = {i for i in V9_RACEGATE_BASE
               if prices.get(i, 0) <= V9_RACEGATE_BASE[i] + V9_RACEGATE_MARGIN}
    if not glutted:
        return _V9_RACEGATE_RESERVE(obs, action)
    native = _IMPL.chassis.players[int(obs["player"])]
    tape = _IMPL.chassis.routes[native["route"]]
    _v9_hz = _V9_ITEM_HZ.get(int(obs["player"]))
    end = min(695, step + (max(_v9_hz.values()) if _v9_hz else _R37_HORIZONS.get(int(obs["player"]), 2)))
    if end <= step:
        return action
    commands = [action.get("farmer") or ["PASS"], *(action.get("hands") or [])]
    view = FarmView(obs)
    if any(len(c) > 1 and c[0] == "PLACE" and c[1] in ANIMAL_STRUCTURE
           and view.inv(i).get(c[1], 0) > 0 for i, c in enumerate(commands[:len(view.positions)])):
        return action
    stock = projected_shed(action, view)
    market = action.get("market", [])
    blocked = {o[1] for o in market if len(o) > 1 and o[0] in ("SELL", "BUY_PRODUCT")}
    blocked.update(c[1] for c in commands if len(c) > 1 and c[0] == "PICKUP")
    blocked.update(c[1] for queue in native["pending"].values() for pos, c in queue
                   if len(c) > 1 and c[0] == "PICKUP")
    debts = native["sell_state"].setdefault("r36_debts", {})
    for item in PRODUCTS:
        if item in blocked or item in glutted or view.prices.get(item, 0) < 2:
            continue
        available = max(0, int(stock.get(item, 0)))
        if not available or len(market) >= 10:
            continue
        reservations = []
        item_end = min(end, step + _v9_hz[item]) if _v9_hz and item in _v9_hz else end
        for due_step in range(step + 1, item_end + 1):
            future = tape[due_step]
            work = [future.get("farmer") or ["PASS"], *(future.get("hands") or [])]
            if any(len(c) > 1 and c[:2] == ["PICKUP", item] for c in work):
                break
            if any(len(o) > 1 and o[:2] == ["BUY_PRODUCT", item] for o in future.get("market", [])):
                break
            planned = sum(max(0, int(o[2])) for o in future.get("market", [])
                          if len(o) >= 3 and o[:2] == ["SELL", item])
            amount = min(available, max(0, planned - debts.get(due_step, {}).get(item, 0)))
            if amount:
                reservations.append((due_step, amount))
                available -= amount
            if not available:
                break
        qty = sum(q for _, q in reservations)
        if qty:
            market.append(["SELL", item, qty])
            for due, q in reservations:
                debt = debts.setdefault(due, {})
                debt[item] = debt.get(item, 0) + q
            _R36_SALE_REPORT["sale_reserved_units"] += qty
            _R36_SALE_REPORT["sale_reservations"] += 1
            _v9_racegate_report["racegate_reserved_units"] += qty
    return action


_V9_RACEGATE_PARENT = agent


def agent(observation, configuration=None):
    if int(observation["step"]) == 0:
        _v9_racegate_report.update(racegate_reserved_units=0, racegate_errors=0)
    try:
        return _V9_RACEGATE_PARENT(observation, configuration)
    except Exception:
        _v9_racegate_report["racegate_errors"] += 1
        return {"farmer": ["PASS"], "hands": [], "market": []}


agent.telemetry = _v9_racegate_report
agent = globals().pop("agent")


# ==== layer ctrtable.py 
_P_ctrtable_336053 = agent

# ---------------------------------------------------------------------------
# v9/3 CTRTABLE: rival-specific early wheat counters.
# Under the BUY 20 | SELL 15 opening, a rival tape's turn-2 observation (rival money, market wheat)
# identifies it exactly.  For known cash-tight tapes we trade alongside their own early wheat orders
# in the same market slots (checked unique over 4,604 recorded games):
#   feel the agi (979.0, 9989): steps 7-8  BUY 5 slot 0, SELL 5 slot 1
#   Mother-Goose (33.0, 9990): step 3      BUY 20 slot 0, SELL 20 slot 1
# ---------------------------------------------------------------------------
CT_TABLE = {
    (979.0, 9989): ((7, 0, ("BUY_PRODUCT", "WHEAT", 5)), (7, 1, ("SELL", "WHEAT", 5)),
                    (8, 0, ("BUY_PRODUCT", "WHEAT", 5)), (8, 1, ("SELL", "WHEAT", 5))),
    (33.0, 9990): ((3, 0, ("BUY_PRODUCT", "WHEAT", 20)), (3, 1, ("SELL", "WHEAT", 20))),
}
_CT = {}
_CT_REPORT = dict(ct_fired=0, ct_errors=0)


def _ct_apply(obs, action, st):
    step = int(obs["step"])
    if step == 2:
        rival = obs["farms"][1 - int(obs["player"])]
        st["plan"] = CT_TABLE.get((round(float(rival["money"]), 3), int(obs["market"]["inventory"]["WHEAT"])))
        if st["plan"]:
            _CT_REPORT["ct_fired"] += 1
    plan = st.get("plan")
    if not plan:
        return action
    items = sorted((slot, list(o)) for t, slot, o in plan if t == step)
    if not items:
        return action
    market = [list(o) for o in action.get("market") or []]
    for slot, o in items:
        while len(market) < slot:
            market.append(["SELL", "WHEAT", 0])
        market.insert(slot, o)
    result = dict(action)
    result["market"] = market[:MAX_ORDERS]
    return result


def agent(observation, configuration=None):
    player, step = int(observation["player"]), int(observation["step"])
    st = _CT.get(player)
    if st is None or step <= st["step"]:
        st = _CT[player] = {"step": -1}
    st["step"] = step
    action = _P_ctrtable_336053(observation, configuration)
    try:
        return _ct_apply(observation, action, st)
    except Exception:
        _CT_REPORT["ct_errors"] += 1
        return action


agent.telemetry = _CT_REPORT
agent = globals().pop("agent")


# ==== layer overflow.py 
_P_overflow_338343 = agent

# ---------------------------------------------------------------------------
# v9/3 OVERFLOW (ported from public V43 R148, Ahmed Berat Ozer, Apache-2.0):
# at hour 23 the workers' cargo drops into a 100-unit shed; cargo that does not fit
# is destroyed.  Sell exactly the shed stock that the destroyed cargo would replace,
# so the complete post-dawn stock vector is unchanged and the sold units are extra.
# ---------------------------------------------------------------------------
_OV_REPORT = dict(ov_turns=0, ov_units=0, ov_errors=0)


def _ov_fields(obs, action):
    farm, private = _PLANNER_NS['_clone_state'](obs['farms'][obs['player']], obs['private'])
    commands = [action.get('farmer') or ['PASS'], *(action.get('hands') or [])]
    demand = {}
    for c in commands:
        if len(c) > 1 and c[0] == 'PLANT':
            demand[c[1]] = demand.get(c[1], 0) + 1
    blocked = {p for p, n in demand.items() if n > private['seeds'].get(p, 0)}
    for actor, c in enumerate(commands[:len(private['inventories'])]):
        if len(c) > 1 and c[0] == 'PLANT' and c[1] in blocked:
            continue
        _PLANNER_NS['_apply_unit_action'](farm, private, actor, c, 10, int(obs['step']) // 24, 24, 100)
    return farm, private


def _ov_same(a, b):
    return all(int(a.get(p, 0)) == int(b.get(p, 0)) for p in set(a) | set(b))


def _ov_apply(obs, action):
    if int(obs['step']) % 24 != 23:
        return action
    orders = action.get('market') or []
    if len(orders) >= 10 or not _r97_budget(obs, orders):
        return action
    _, private = _ov_fields(obs, action)
    stock, _, _ = _r97_market_stock(private['shed'], orders)
    original, loss = _r97_delivery(stock, private, True)
    if not loss:
        return action
    remaining = max(0, 100 - sum(stock.values()))
    tail = []
    for bag in private['inventories']:
        for item, n in bag.items():
            n = max(0, int(n)); take = min(n, remaining); remaining -= take
            if n > take:
                tail.extend([item] * (n - take))
    released = {}; best = None
    for item in tail:
        released[item] = released.get(item, 0) + 1
        if item not in obs['market']['prices'] or released[item] > stock.get(item, 0):
            break
        if len(orders) + len(released) > 10:
            break
        proposed = list(orders) + [['SELL', p, n] for p, n in released.items()]
        after, _, _ = _r97_market_stock(private['shed'], proposed)
        final, _ = _r97_delivery(after, private, True)
        if _ov_same(original, final):
            best = (proposed, dict(released))
    if best is None:
        return action
    _OV_REPORT['ov_turns'] += 1
    _OV_REPORT['ov_units'] += sum(best[1].values())
    return dict(action, market=best[0])


def agent(observation, configuration=None):
    action = _P_overflow_338343(observation, configuration)
    try:
        return _ov_apply(observation, action)
    except Exception:
        _OV_REPORT['ov_errors'] += 1
        return action


agent.telemetry = _OV_REPORT
agent = globals().pop("agent")


# One-worker non-harvest service for the inherited six-sheep project.
# All feeding and care are mandatory. Optional fertilizer collection only uses
# leftover time; setup, wool harvests, and late-start days keep the old crew.
_SL_REQUEST = _v233_request
_SL_WORKER = _v233_worker
_SL_REPORT = dict(compact_days=0, confirmed=0, collect=0)
_SL_TILES = ((5,5),(6,5),(7,5),(7,6),(6,6),(5,6))


def _sl_dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


def _sl_path(pos,targets):
    return min(_r53_permutations(targets),key=lambda path:(_sl_dist(pos,path[0])+sum(_sl_dist(a,b) for a,b in zip(path,path[1:])),path)) if targets else ()


def _v233_request(obs,action,state,native):
    result=_SL_REQUEST(obs,action,state,native)
    pending=state.get('pending')
    if result is action or not pending or pending['initial']:
        return result
    farm=obs['farms'][obs['player']];hour=int(obs['step'])%24
    tiles=[farm['tiles'][y][x] for x,y in _SL_TILES]
    if not all(isinstance(t,dict) and t.get('animal')=='SHEEP' and t.get('yield_units',0)==0 for t in tiles):
        return result
    # Exact spawn after native commands/hires, and a full feed pickup turn.
    ready,spawn=_r62_input_start(obs,action,0)
    path=_sl_path(spawn,_SL_TILES)
    travel=_sl_dist(spawn,path[0])+sum(_sl_dist(a,b) for a,b in zip(path,path[1:]))
    mandatory=sum(not t.get('fed_today') for t in tiles)+sum(not t.get('cared_today') for t in tiles)
    available=min((int(obs['step'])//24+1)*24,719)-ready
    if travel+mandatory>available:
        return result
    # Collection can be interleaved along the essential route. Charge the
    # discarded fertilizer against the saved wage, including final delivery.
    native_hires=sum(o and o[0]=='HIRE' for o in action.get('market',[]))
    saved=_v219_fib(farm['hires_today']+native_hires+1)
    delivery=_sl_dist(path[-1],_v219_home(path[-1]))+1 if int(obs['step'])//24==29 else 0
    possible=max(0,min(6,available-travel-mandatory-delivery))
    if saved<=(6-possible)*obs['market']['prices']['FERTILIZER']:
        return result
    out=copy.deepcopy(result)
    assert out['market'][-2:]==[['HIRE'],['HIRE']]
    out['market'].pop()
    pending.update(count=1,targets=path)
    _V233_REPORT['sheep_hire_requests']-=1
    _SL_REPORT['compact_days']+=1
    return out


def _v233_worker(obs,actor,targets):
    if len(targets)!=6:
        return _SL_WORKER(obs,actor,targets)
    farm=obs['farms'][obs['player']];private=obs['private'];step=int(obs['step'])
    pos=tuple(farm['hands'][actor-1]);inv=private['inventories'][actor]
    needed=[];hungry=0
    for target in targets:
        x,y=target;t=farm['tiles'][y][x]
        if not isinstance(t,dict) or t.get('animal')!='SHEEP':
            return _SL_WORKER(obs,actor,targets)
        if not t['fed_today']:hungry+=1
        if not t['fed_today'] or not t['cared_today']:needed.append(target)
    home=_v219_home(pos)
    if hungry>inv.get('WHEAT',0):
        return _v219_walk(pos,home) or ['PICKUP','WHEAT',min(hungry,private['shed'].get('WHEAT',0))]
    if needed:
        path=_sl_path(pos,needed)
        current=farm['tiles'][pos[1]][pos[0]]
        if pos in targets and isinstance(current,dict) and current.get('fed_today') and current.get('cared_today') and current.get('fertilizer_available'):
            travel=_sl_dist(pos,path[0])+sum(_sl_dist(a,b) for a,b in zip(path,path[1:]))
            work=sum(not farm['tiles'][y][x]['fed_today'] for x,y in path)+sum(not farm['tiles'][y][x]['cared_today'] for x,y in path)
            delivery=_sl_dist(path[-1],_v219_home(path[-1]))+1 if step//24==29 else 0
            remaining=min((step//24+1)*24,719)-step
            if 1+travel+work+delivery<=remaining:
                _SL_REPORT['collect']+=1
                return ['COLLECT_FERTILIZER']
        target=path[0];t=farm['tiles'][target[1]][target[0]]
        return _v219_walk(pos,target) or (['FEED'] if not t['fed_today'] else ['CARE'])
    # Essential work is complete. Collect what can still reach the shed on
    # the final day; on earlier days the normal midnight deposit is sufficient.
    remaining=719-step if step//24==29 else 24-step%24
    tasks=[]
    for target in targets:
        t=farm['tiles'][target[1]][target[0]]
        if not t.get('fertilizer_available'):continue
        dist=_sl_dist(pos,target)
        ret=_sl_dist(target,_v219_home(target))+1 if step//24==29 else 0
        if dist+1+ret<=remaining:tasks.append((dist,tuple(target)))
    if tasks:
        _,target=min(tasks)
        command=_v219_walk(pos,target) or ['COLLECT_FERTILIZER']
        _SL_REPORT['collect']+=command==['COLLECT_FERTILIZER']
        return command
    if inv.get('FERTILIZER',0):
        return _v219_walk(pos,home) or ['PLACE','FERTILIZER',inv['FERTILIZER']]
    return ['PASS']


agent=globals().pop('agent')


# v9/4 VE: commit the six-sheep expansion on day 11 when two of the first three
# shops are yarn stores. The melon sale lands on day 11, and sheep placed that
# day produce on days 17, 20, 23, 26 and 29 instead of 18, 21, 24 and 27: a
# fifth wool harvest for one more day of feed and labour.
# Day 11 waits until the tape's own land purchase (hour 1) and only ignores a
# native sheep that the tape itself picks up later today (units act before the
# market, and the project's hands spawn a step after its purchase). It commits
# only when cash also covers every purchase the tape still plans through day 12
# (its day-11 strawberry seeds above all); otherwise day 12 decides as before.
_VE_ELIGIBLE = _v233_eligible
_VE_REPORT = dict(ve_day11_checks=0, ve_day11_budget_declines=0, ve_day11_ok=0)
_VE_SEED = {'WHEAT': 10, 'CARROT': 20, 'TOMATO': 50, 'STRAWBERRY': 100, 'MELON': 80}
_VE_ANIMAL = {'SHEEP': 500, 'COW': 400, 'GOOSE': 300}


def _v233_eligible(obs, native):
    step = int(obs['step'])
    if step // 24 != 11:
        return _VE_ELIGIBLE(obs, native)
    tape = _IMPL.chassis.routes[native['route']]
    private = obs['private']
    held = int(private['shed'].get('SHEEP', 0)) + sum(int(i.get('SHEEP', 0)) for i in private['inventories'])
    pickups = 0
    for t in range(step, 12 * 24):
        for c in [tape[t].get('farmer')] + tape[t].get('hands', []):
            if c and c[0] == 'PICKUP' and len(c) > 1 and c[1] == 'SHEEP':
                pickups += int(c[2]) if len(c) > 2 else 1
    if held > pickups:
        return False
    clean = dict(private, shed=dict(private['shed'], SHEEP=0),
                 inventories=[{k: v for k, v in i.items() if k != 'SHEEP'} for i in private['inventories']])
    if not _VE_ELIGIBLE(dict(obs, private=clean), native):
        return False
    _VE_REPORT['ve_day11_checks'] += 1
    prices = obs['market']['prices']
    spend = 0
    hires = {}
    for t in range(step + 1, min(len(tape), 13 * 24)):
        for o in tape[t].get('market', []):
            if not o:
                continue
            if o[0] == 'BUY_LAND' or o[:2] == ['BUY_ANIMAL', 'SHEEP']:
                return False
            if o[0] == 'BUY_SEED':
                spend += int(o[2]) * _VE_SEED.get(o[1], 100)
            elif o[0] == 'BUY_PRODUCT':
                spend += int(o[2]) * (int(prices.get(o[1], 50)) + 10)
            elif o[0] == 'BUY_ANIMAL':
                spend += int(o[2]) * _VE_ANIMAL.get(o[1], 500)
            elif o[0] == 'HIRE':
                d = t // 24
                spend += _v219_fib(hires.get(d, 0))
                hires[d] = hires.get(d, 0) + 1
    if obs['farms'][obs['player']]['money'] < 7000 + 3000 + spend:
        _VE_REPORT['ve_day11_budget_declines'] += 1
        return False
    _VE_REPORT['ve_day11_ok'] += 1
    return True


agent.telemetry = _VE_REPORT
agent = globals().pop('agent')


# v9/4 VT: the sheep expansion's last two days.
# No refresh follows day 29, so feeding, caring and buying feed that day are
# worthless: only wool already grown is worth a hand. Day 29 hires nothing when
# no sheep holds wool, and otherwise one harvest-only hand that delivers the
# wool before the final market. A care on day 28 adds to the bonus after the
# last production refresh has already consumed it, so day-28 hands skip CARE.
_VT_REQUEST = _v233_request
_VT_WORKER = _v233_worker
_VT_RESCUE = _v234_rescue
_VT_REPORT = dict(vt_no_hire_days=0, vt_single_harvest_days=0, vt_skipped_care=0)
_VT_TILES = ((5, 5), (6, 5), (7, 5), (5, 6), (6, 6), (7, 6))


def _vt_wool_tiles(obs):
    farm = obs['farms'][obs['player']]
    return [xy for xy in _VT_TILES if isinstance(farm['tiles'][xy[1]][xy[0]], dict)
            and farm['tiles'][xy[1]][xy[0]].get('animal') == 'SHEEP' and farm['tiles'][xy[1]][xy[0]].get('yield_units', 0) > 0]


def _v233_request(obs, action, state, native):
    result = _VT_REQUEST(obs, action, state, native)
    if result is action or int(obs['step']) // 24 != 29 or not state.get('committed'):
        return result
    pending = state.get('pending')
    if not pending or pending.get('initial'):
        return result
    wool = _vt_wool_tiles(obs)
    extra = result['market'][len(action.get('market', [])):]
    if not wool:
        state.pop('pending', None)
        _V233_REPORT['sheep_hire_requests'] -= sum(o == ['HIRE'] for o in extra)
        _V233_REPORT['sheep_feed_buy_requests'] -= 6
        _VT_REPORT['vt_no_hire_days'] += 1
        return action
    out = copy.deepcopy(action)
    out['market'] = list(out.get('market', [])) + [['HIRE']]
    _V233_REPORT['sheep_hire_requests'] -= sum(o == ['HIRE'] for o in extra) - 1
    _V233_REPORT['sheep_feed_buy_requests'] -= 6
    pending.update(count=1, targets=_sl_path(_r62_input_start(obs, action, 0)[1], wool))
    _VT_REPORT['vt_single_harvest_days'] += 1
    return out


def _v233_worker(obs, actor, targets):
    step = int(obs['step'])
    day = step // 24
    if day not in (28, 29):
        return _VT_WORKER(obs, actor, targets)
    farm = obs['farms'][obs['player']]
    private = obs['private']
    pos = tuple(farm['hands'][actor - 1])
    inv = private['inventories'][actor]
    home = _v219_home(pos)
    distance = abs(pos[0] - home[0]) + abs(pos[1] - home[1])
    cargo = [item for item in ('WOOL', 'FERTILIZER') if inv.get(item, 0)]
    last = 717 if day == 29 else day * 24 + 23
    if cargo and step >= last - distance:
        return _v219_walk(pos, home) or ['PLACE', cargo[0], inv[cargo[0]]]
    sheep = [(x, y) for x, y in targets if isinstance(farm['tiles'][y][x], dict) and farm['tiles'][y][x].get('animal') == 'SHEEP']
    tasks = []
    if day == 28:
        hungry = sum(not farm['tiles'][y][x]['fed_today'] for x, y in sheep)
        if hungry and not inv.get('WHEAT', 0) and private['shed'].get('WHEAT', 0):
            return _v219_walk(pos, home) or ['PICKUP', 'WHEAT', min(hungry, private['shed']['WHEAT'])]
    for x, y in sheep:
        tile = farm['tiles'][y][x]
        command = None
        if day == 28 and not tile['fed_today'] and inv.get('WHEAT', 0):
            command = ['FEED']
        elif tile['yield_units']:
            command = ['HARVEST']
        elif day == 28 and tile['fertilizer_available']:
            command = ['COLLECT_FERTILIZER']
        if day == 28 and not tile['cared_today'] and command is None:
            _VT_REPORT['vt_skipped_care'] += 1
        if command:
            tasks.append((abs(pos[0] - x) + abs(pos[1] - y), (x, y), command))
    if tasks:
        _, target, command = min(tasks)
        return _v219_walk(pos, target) or command
    if cargo:
        return _v219_walk(pos, home) or ['PLACE', cargo[0], inv[cargo[0]]]
    return ['PASS']


def _v234_rescue(obs, action, state):
    if int(obs['step']) // 24 == 29:
        return action
    return _VT_RESCUE(obs, action, state)


agent.telemetry = _VT_REPORT
agent = globals().pop('agent')


# ---------------------------------------------------------------------------
# Claude CARROT2 layer: carrot instead of wheat when the carrot book pays. Own implementation.
# Built by tools/claude_build_carrot.py (derivation there).
# ---------------------------------------------------------------------------
_CA_FROM = 6
_CA_TO = 28
_CA_MARGIN = -5.0
_CA_DROP = 0.0
_CA_BUFFER = 8
_CA_FEED_DAYS = 2
_CA_CASH = 800
_CA_RESCUE = True
_CA_MOVES = {"NORTH": (0, -1), "SOUTH": (0, 1), "EAST": (1, 0), "WEST": (-1, 0)}
_CA_CROP = {"WHEAT": (4, 6), "CARROT": (3, 4)}
_CA_STATE = {}
_CA_REPORT = {"ca_swaps": 0, "ca_rescues": 0, "ca_harvested": 0, "ca_sold": 0, "ca_seed_bought": 0,
              "ca_wheat_seed_saved": 0, "ca_carrot_seed_saved": 0, "ca_feed_block": 0, "ca_errors": 0,
              "ca_min_wheat": 999}


def _ca_tape(seat, t):
    native = _IMPL.chassis.players.get(seat)
    if not native or t > 719:
        return {}
    tape = _IMPL.chassis.routes[2 if t >= 648 else native["route"]]
    return tape[t] if t < len(tape) and isinstance(tape[t], dict) else {}


def _ca_spawn(positions, board):
    half = board // 2
    access = [(half - 1, half - 1), (half, half - 1), (half - 1, half), (half, half)]
    occ = {a: 0 for a in access}
    for p in positions:
        if tuple(p) in occ:
            occ[tuple(p)] += 1
    return list(min(access, key=lambda a: (occ[a], access.index(a))))


def _ca_visits(obs, action, pos, t_end, start=None):
    """Non-move commands issued on tile ``pos`` from this step (with ``action``) until ``t_end``."""
    seat = int(obs["player"])
    step = int(obs["step"])
    farm = obs["farms"][seat]
    board = len(farm["tiles"])
    half = board // 2
    positions = [list(farm["farmer"])] + [list(h) for h in farm["hands"]]
    out = []
    for t in range(step, min(t_end, 719) + 1):
        act = action if t == step else _ca_tape(seat, t)
        units = [act.get("farmer") or ["PASS"]] + list(act.get("hands") or [])
        for i in range(len(positions)):
            cmd = units[i] if i < len(units) and units[i] else ["PASS"]
            if cmd[0] in _CA_MOVES:
                dx, dy = _CA_MOVES[cmd[0]]
                nx, ny = positions[i][0] + dx, positions[i][1] + dy
                if 0 <= nx < board and 0 <= ny < board:
                    positions[i] = [nx, ny]
            elif tuple(positions[i]) == pos and (start is None or t >= start):
                out.append((t, i, cmd[0]))
        for _ in range(sum(1 for o in (act.get("market") or []) if o and o[0] == "HIRE")):
            positions.append(_ca_spawn(positions, board))
        if t % 24 == 23:
            positions = [[half - 1, half - 1]]
    return out


def _ca_decays(mls, a, b):
    """Decay events at steps s in [max(a, mls), b) with (s - mls) even."""
    a = max(a, mls)
    if b <= a:
        return 0
    first = a if (a - mls) % 2 == 0 else a + 1
    return 0 if first >= b else (b - 1 - first) // 2 + 1


def _ca_yield_path(crop, planted, visits, y0=1, fert_until=-1, watered_day=-1, now_step=0):
    """Return (harvest_units, best_rescue_units, rescue_step) for a crop following ``visits``.
    ``y0`` is the yield observed at ``now_step`` (decay before that step already included)."""
    myd, cap = _CA_CROP[crop]
    lo = (myd + 1) // 2
    mls = (planted + myd + 1) * 24
    y = y0
    best_rescue, rescue_t = 0, None
    for t, i, op in visits:
        day = t // 24
        age = day - planted
        dec = _ca_decays(mls, now_step, t)
        now = y - dec
        if now <= 0 and t > mls:
            return 0, best_rescue, rescue_t
        if op == "HARVEST":
            return (max(0, now) if age >= 2 else 0), best_rescue, rescue_t
        if op in ("PLANT", "DIG", "BUILD_COOP", "BUILD_PASTURE"):
            return 0, best_rescue, rescue_t
        if age >= 2 and now > best_rescue and t > now_step:
            best_rescue, rescue_t = now, t
        if op == "WATER" and lo <= age <= myd and day != watered_day:
            watered_day = day
            y = min(cap, y + (2 if fert_until >= day else 1))
    return 0, best_rescue, rescue_t


def _ca_wheat_total(obs):
    priv = obs["private"]
    return int(priv["shed"].get("WHEAT", 0)) + sum(int(inv.get("WHEAT", 0)) for inv in priv["inventories"])


def _ca_feed_need(seat, step, days):
    need = 0
    for t in range(step, min(719, step + 24 * days) + 1):
        act = _ca_tape(seat, t)
        units = [act.get("farmer") or ["PASS"]] + list(act.get("hands") or [])
        need += sum(1 for c in units if c and c[0] == "FEED")
    return need


_CA_PARENT = agent
del agent


def agent(observation, configuration=None):
    action = _CA_PARENT(observation, configuration)
    try:
        step = int(observation["step"])
        seat = int(observation["player"])
        st = _CA_STATE.get(seat)
        if step == 0 or st is None or step <= st["step"]:
            st = _CA_STATE[seat] = {"step": -1, "tiles": {}, "spare_wheat": 0, "spare_carrot": 0, "credit": 0}
            if step == 0:
                _CA_REPORT.update(ca_swaps=0, ca_rescues=0, ca_harvested=0, ca_sold=0, ca_seed_bought=0,
                                  ca_wheat_seed_saved=0, ca_carrot_seed_saved=0, ca_feed_block=0,
                                  ca_errors=0, ca_min_wheat=999)
        st["step"] = step
        if not isinstance(action, dict) or step > 717:
            return action
        day = step // 24
        farm = observation["farms"][seat]
        tiles = farm["tiles"]
        priv = observation["private"]
        prices = observation["market"]["prices"]
        p_c, p_w = int(prices.get("CARROT", 0)), int(prices.get("WHEAT", 0))
        positions = [tuple(farm["farmer"])] + [tuple(h) for h in farm["hands"]]
        units = [list(action.get("farmer") or ["PASS"])] + [list(c) for c in (action.get("hands") or [])]
        market = [list(o) for o in (action.get("market") or [])]
        changed = False
        if _CA_FROM <= day <= _CA_TO + 4:
            _CA_REPORT["ca_min_wheat"] = min(_CA_REPORT["ca_min_wheat"], _ca_wheat_total(observation))
        # 1. bookkeeping + rescue of swapped carrots
        for pos, planted in list(st["tiles"].items()):
            tile = tiles[pos[1]][pos[0]]
            if not (isinstance(tile, dict) and tile.get("crop") == "CARROT" and int(tile.get("planted_day", -9)) == planted):
                st["tiles"].pop(pos, None)
                continue
            here = [i for i, p in enumerate(positions) if p == pos and i < len(units)]
            if not here:
                continue
            i = here[0]
            cmd = units[i]
            yu = int(tile.get("yield_units", 0))
            if cmd and cmd[0] == "HARVEST":
                if day - planted >= 2 and yu > 0:
                    st["credit"] += yu
                    _CA_REPORT["ca_harvested"] += yu
                    st["tiles"].pop(pos, None)
                continue
            if not _CA_RESCUE or (cmd and cmd[0] in _CA_MOVES) or day - planted < 2 or yu <= 0:
                continue
            visits = _ca_visits(observation, action, pos, (planted + 5) * 24)
            harvest, later, _ = _ca_yield_path("CARROT", planted, visits, y0=yu,
                                               fert_until=int(tile.get("fertilized_until_day", -1)),
                                               watered_day=day if tile.get("watered_today") else -1,
                                               now_step=step)
            if yu > max(harvest, later):
                units[i] = ["HARVEST"]
                st["credit"] += yu
                _CA_REPORT["ca_harvested"] += yu
                _CA_REPORT["ca_rescues"] += 1
                st["tiles"].pop(pos, None)
                changed = True
        # 2. swaps
        pays_now = 3 * (p_c - _CA_DROP) - 20 > 4 * p_w - 10 + _CA_MARGIN
        if _CA_FROM <= day <= _CA_TO and pays_now:
            seeds_c = min(st["spare_carrot"],
                          int(priv["seeds"].get("CARROT", 0)) - sum(1 for c in units if c[:2] == ["PLANT", "CARROT"]))
            wheat_ok = None
            for i, cmd in enumerate(units):
                if cmd[:2] != ["PLANT", "WHEAT"] or i >= len(positions) or seeds_c <= 0:
                    continue
                pos = positions[i]
                if tiles[pos[1]][pos[0]] is not None:
                    continue
                if wheat_ok is None:
                    wheat_ok = _ca_wheat_total(observation) >= _ca_feed_need(seat, step, _CA_FEED_DAYS)
                if not wheat_ok:
                    _CA_REPORT["ca_feed_block"] += 1
                    break
                visits = _ca_visits(observation, action, pos, (day + 6) * 24, start=step + 1)
                wu, _, _ = _ca_yield_path("WHEAT", day, visits)
                ch, cr, _ = _ca_yield_path("CARROT", day, visits)
                cu = max(ch, cr if _CA_RESCUE else 0)
                if cu * (p_c - _CA_DROP) - 20 > wu * p_w - 10 + _CA_MARGIN:
                    units[i] = ["PLANT", "CARROT"]
                    seeds_c -= 1
                    st["spare_carrot"] -= 1
                    st["tiles"][pos] = day
                    st["spare_wheat"] += 1
                    _CA_REPORT["ca_swaps"] += 1
                    changed = True
        # 3. seeds
        new_market = []
        for o in market:
            if len(o) >= 3 and o[0] == "BUY_SEED" and o[1] in ("WHEAT", "CARROT"):
                key = "spare_wheat" if o[1] == "WHEAT" else "spare_carrot"
                cut = min(int(o[2]), st[key])
                if cut > 0:
                    st[key] -= cut
                    _CA_REPORT["ca_wheat_seed_saved" if o[1] == "WHEAT" else "ca_carrot_seed_saved"] += cut
                    changed = True
                    if int(o[2]) - cut <= 0:
                        continue
                    o = [o[0], o[1], int(o[2]) - cut]
            new_market.append(o)
        market = new_market
        if _CA_FROM <= day <= _CA_TO - 1 and pays_now and len(market) < 10:
            have = int(priv["seeds"].get("CARROT", 0)) - sum(1 for c in units if c[:2] == ["PLANT", "CARROT"])
            buying = sum(int(o[2]) for o in market if len(o) >= 3 and o[:2] == ["BUY_SEED", "CARROT"])
            q = _CA_BUFFER - have - buying
            if q > 0 and int(farm.get("money", 0)) >= _CA_CASH + 20 * q:
                market.append(["BUY_SEED", "CARROT", q])
                st["spare_carrot"] += q
                _CA_REPORT["ca_seed_bought"] += q
                changed = True
        # 4. sell credited carrots
        if st["credit"] > 0 and p_c >= 2 and len(market) < 10:
            view_action = {"farmer": units[0], "hands": units[1:], "market": market}
            stock = int(projected_shed(view_action, FarmView(observation)).get("CARROT", 0))
            selling = sum(int(o[2]) for o in market if len(o) >= 3 and o[:2] == ["SELL", "CARROT"])
            q = min(st["credit"], stock - selling)
            if q > 0:
                market.insert(0, ["SELL", "CARROT", q])
                st["credit"] -= q
                _CA_REPORT["ca_sold"] += q
                changed = True
        if changed:
            action = dict(action)
            action["farmer"] = units[0]
            action["hands"] = units[1:]
            action["market"] = market[:10]
    except Exception:
        _CA_REPORT["ca_errors"] += 1
    return action


agent.telemetry = _CA_REPORT
agent = globals().pop('agent')


# ---------------------------------------------------------------------------
# Claude ORDERPRI2 layer: sales ordered by the rival's estimated sellable stock. Own implementation.
# Built by tools/claude_build_orderpri2.py (derivation there).
# ---------------------------------------------------------------------------
_OR2_CAP = 30
_OR2_SN_K = 0
_OR2_SN_H = 24
_OR2_SLOT_H = 6
_OR2_SLOT_MARGIN = 50.0
_OR2_SN_ITEMS = ("MILK", "STRAWBERRY", "WOOL", "MELON", "EGG")
_OR2_ITEMS = ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL")
_OR2_ONGOING = ("TOMATO", "STRAWBERRY")
_OR2_ANIMAL = {"GOOSE": "EGG", "COW": "MILK", "SHEEP": "WOOL"}
_OR2_SHOPS = {"BAKERY": ("EGG", "WHEAT"), "PIZZA_SHOP": ("MILK", "TOMATO", "WHEAT"),
              "BRUNCH_SPOT": ("EGG", "WHEAT", "STRAWBERRY"), "YARN_STORE": ("WOOL",),
              "ICE_CREAM_SHOP": ("STRAWBERRY", "MILK", "WHEAT"), "PET_CAFE": ("CARROT",),
              "SMOOTHIE_SHOP": ("STRAWBERRY", "MILK"),
              "FARMERS_MARKET": ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY")}
_OR2_STATE = {}
_OR2_REPORT = {"or2_reordered": 0, "or2_changed_vs_v39": 0, "or2_rival_harvest": 0, "or2_rival_sold": 0,
               "or2_errors": 0}


def _or2_draw(shops, step):
    draw = {}
    if step % 4 == 0:
        for name in shops:
            products = _OR2_SHOPS.get(name, ())
            for item in products:
                draw[item] = draw.get(item, 0) + (2 if len(products) == 1 else 1)
    if step % 24 == 0:
        for item in _OR2_ITEMS:
            draw[item] = draw.get(item, 0) + 1
    return draw


def _or2_tiles(farm):
    out = {}
    for y, row in enumerate(farm["tiles"]):
        for x, t in enumerate(row):
            if not isinstance(t, dict):
                continue
            if t.get("kind") == "PLANT" and t.get("crop"):
                out[(x, y)] = ("P", t["crop"], int(t.get("planted_day", -1)), int(t.get("yield_units", 0)))
            elif t.get("animal") in _OR2_ANIMAL:
                out[(x, y)] = ("A", _OR2_ANIMAL[t["animal"]], int(t.get("placed_day", -1)), int(t.get("yield_units", 0)))
    return out


def _or2_exposure(observation, item, qty, batch):
    if qty <= 0 or batch <= 0 or item not in _R37_MARKET_PARAMS:
        return 0.0
    params = {k: dict(v) for k, v in _R37_MARKET_PARAMS.items()}
    for k, patch in (observation["market"].get("params") or {}).items():
        if k in params:
            params[k].update(patch)
    inv = int(observation["market"]["inventory"][item])
    return float(sum(_r37_market_price(item, inv + j, params) - _r37_market_price(item, inv + batch + j, params)
                     for j in range(qty)))


_OR2_PARENT = agent
del agent


def agent(observation, configuration=None):
    action = _OR2_PARENT(observation, configuration)
    try:
        step = int(observation["step"])
        seat = int(observation["player"])
        st = _OR2_STATE.get(seat)
        if step == 0 or st is None or step <= st.get("step", -1):
            st = _OR2_STATE[seat] = {"step": -1, "stock": {i: 0 for i in _OR2_ITEMS}, "prev": None}
            if step == 0:
                for k in _OR2_REPORT:
                    _OR2_REPORT[k] = 0
        rival = observation["farms"][1 - seat]
        tiles = _or2_tiles(rival)
        inv_now = {i: int(observation["market"]["inventory"].get(i, 0)) for i in _OR2_ITEMS}
        prev = st["prev"]
        if prev and prev["step"] == step - 1:
            stock = st["stock"]
            for pos, old in prev["tiles"].items():
                kind, item, born, y = old
                if y <= 0:
                    continue
                new = tiles.get(pos)
                got = 0
                if kind == "P" and item not in _OR2_ONGOING:
                    if (new is None and not _OR2_WEED(rival, pos)) or (new is not None and new[2] != born):
                        got = y
                elif new is not None and new[0] == kind and new[1] == item and new[2] == born and new[3] < y:
                    if step % 24 != 0:
                        got = y - new[3]
                    elif new[3] == 0:
                        got = y
                if got > 0:
                    stock[item] = stock.get(item, 0) + got
                    _OR2_REPORT["or2_rival_harvest"] += got
            draw = _or2_draw(prev["shops"], prev["step"])
            for item in _OR2_ITEMS:
                if prev["prices"].get(item, 0) <= 1:
                    continue
                moved = inv_now[item] - prev["inv"][item] + draw.get(item, 0) - prev["own"].get(item, 0)
                if moved > 0:
                    stock[item] = max(0, stock.get(item, 0) - moved)
                    _OR2_REPORT["or2_rival_sold"] += moved
        own = {}
        if isinstance(action, dict):
            orders = [list(o) for o in (action.get("market") or [])]
            proj = dict(projected_shed(action, FarmView(observation)))
            if _OR2_SN_K > 0 and 24 <= step < 694:
                native = _IMPL.chassis.players.get(seat)
                debts = native["sell_state"].setdefault("r36_debts", {}) if native else None
                for item in _OR2_SN_ITEMS:
                    if debts is None or int(st["stock"].get(item, 0)) < _OR2_SN_K:
                        continue
                    if int(observation["market"]["prices"].get(item, 0)) < 2 or len(orders) >= 10:
                        continue
                    if any(len(o) >= 2 and o[0] in ("BUY_PRODUCT", "BUY_ANIMAL") and o[1] == item for o in orders):
                        continue
                    selling = sum(max(0, int(o[2])) for o in orders if len(o) >= 3 and o[0] == "SELL" and o[1] == item)
                    avail = int(proj.get(item, 0)) - selling
                    take = 0
                    for t in range(step + 1, min(694, step + _OR2_SN_H) + 1):
                        if take >= avail:
                            break
                        tape = _IMPL.chassis.routes[2 if t >= 648 else native["route"]]
                        act = tape[t] if t < len(tape) and isinstance(tape[t], dict) else {}
                        planned = sum(max(0, int(o[2])) for o in (act.get("market") or [])
                                      if len(o) >= 3 and o[0] == "SELL" and o[1] == item)
                        planned -= debts.get(t, {}).get(item, 0)
                        q = min(planned, avail - take)
                        if q > 0:
                            debts.setdefault(t, {})[item] = debts.get(t, {}).get(item, 0) + q
                            take += q
                    if take > 0:
                        for o in orders:
                            if len(o) >= 3 and o[0] == "SELL" and o[1] == item:
                                o[2] = int(o[2]) + take
                                break
                        else:
                            orders.append(["SELL", item, take])
                        _OR2_REPORT["or2_sellnow"] = _OR2_REPORT.get("or2_sellnow", 0) + take
                        action = dict(action)
                        action["market"] = orders
            if _OR2_SLOT_H > 0 and 288 <= step < 694 and len(orders) >= 10:
                native = _IMPL.chassis.players.get(seat)
                debts = native["sell_state"].setdefault("r36_debts", {}) if native else None
                sells = [o for o in orders if len(o) >= 3 and o[0] == "SELL"]
                selling_items = {o[1] for o in sells}
                bought_items = {o[1] for o in orders if len(o) >= 2 and o[0] in ("BUY_PRODUCT", "BUY_ANIMAL")}
                best = None
                for item in _OR2_SN_ITEMS:
                    if debts is None or item in selling_items or item in bought_items:
                        continue
                    avail = int(proj.get(item, 0))
                    if avail <= 0 or int(observation["market"]["prices"].get(item, 0)) < 2:
                        continue
                    plan, take = [], 0
                    for t in range(step + 1, min(694, step + _OR2_SLOT_H) + 1):
                        if take >= avail:
                            break
                        tape = _IMPL.chassis.routes[2 if t >= 648 else native["route"]]
                        act = tape[t] if t < len(tape) and isinstance(tape[t], dict) else {}
                        planned = sum(max(0, int(o[2])) for o in (act.get("market") or [])
                                      if len(o) >= 3 and o[0] == "SELL" and o[1] == item)
                        q = min(planned - debts.get(t, {}).get(item, 0), avail - take)
                        if q > 0:
                            plan.append((t, q))
                            take += q
                    if take <= 0:
                        continue
                    b = min(_OR2_CAP, int(st["stock"].get(item, 0)))
                    value = _or2_exposure(observation, item, take, max(1, b))
                    if best is None or value > best[0]:
                        best = (value, item, take, plan)
                if best is not None and sells:
                    def sval(o):
                        q = min(max(0, int(o[2])), max(0, int(proj.get(o[1], 0))))
                        return _or2_exposure(observation, o[1], q, max(1, min(_OR2_CAP, int(st["stock"].get(o[1], 0)))))
                    weakest = min(sells, key=sval)
                    if best[0] > sval(weakest) + _OR2_SLOT_MARGIN and weakest[1] not in ("WHEAT", "FERTILIZER")                             or best[0] > sval(weakest) + _OR2_SLOT_MARGIN and int(weakest[2]) <= 2:
                        # drop the weakest sale; give its booked debts back (nearest due first)
                        refund = max(0, int(weakest[2]))
                        for t in range(step + 1, step + 49):
                            if refund <= 0:
                                break
                            owed = debts.get(t, {}).get(weakest[1], 0)
                            back = min(owed, refund)
                            if back > 0:
                                debts[t][weakest[1]] = owed - back
                                refund -= back
                        orders.remove(weakest)
                        orders.append(["SELL", best[1], best[2]])
                        for t, q in best[3]:
                            debts.setdefault(t, {})[best[1]] = debts.get(t, {}).get(best[1], 0) + q
                        _OR2_REPORT["or2_slot_swaps"] = _OR2_REPORT.get("or2_slot_swaps", 0) + 1
                        action = dict(action)
                        action["market"] = orders
            left = dict(proj)
            movable, fixed, bought = [], [], set()
            for idx, o in enumerate(orders):
                if len(o) >= 2 and o[0] in ("BUY_PRODUCT", "BUY_ANIMAL"):
                    bought.add(o[1])
                if len(o) >= 3 and o[0] == "SELL" and int(o[2]) > 0 and o[1] not in bought:
                    movable.append((idx, o))
                else:
                    fixed.append((idx, o))
            if movable and step >= 1:
                def score(io):
                    item, qty = io[1][1], min(int(io[1][2]), max(0, int(proj.get(io[1][1], 0))))
                    b = min(_OR2_CAP, int(st["stock"].get(item, 0)))
                    return (-_or2_exposure(observation, item, qty, b),
                            -_r37_quote_priority(observation, io[1], proj), io[0])
                scored = sorted(movable, key=score)
                new = [o for _, o in scored] + [o for _, o in fixed]
                if new != orders:
                    v39 = sorted(movable, key=lambda io: (-_r37_quote_priority(observation, io[1], proj), io[0]))
                    if [o for _, o in v39] != [o for _, o in scored]:
                        _OR2_REPORT["or2_changed_vs_v39"] += 1
                    _OR2_REPORT["or2_reordered"] += 1
                    action = dict(action)
                    action["market"] = new
                    orders = new
            for o in orders[:10]:
                if len(o) >= 3 and o[0] == "SELL" and o[1] in _OR2_ITEMS:
                    got = min(max(0, int(o[2])), max(0, int(left.get(o[1], 0))))
                    left[o[1]] = left.get(o[1], 0) - got
                    own[o[1]] = own.get(o[1], 0) + got
        st["prev"] = {"step": step, "tiles": tiles, "inv": inv_now, "own": own,
                      "prices": dict(observation["market"]["prices"]),
                      "shops": list((observation.get("town") or {}).get("unlocked_shops") or [])}
        st["step"] = step
    except Exception:
        _OR2_REPORT["or2_errors"] += 1
    return action


def _OR2_WEED(farm, pos):
    t = farm["tiles"][pos[1]][pos[0]]
    return isinstance(t, dict) and t.get("kind") == "WEED"


agent.telemetry = _OR2_REPORT
agent = globals().pop('agent')


# ---------------------------------------------------------------------------
# Claude CAPHARV layer: harvest animals that would overflow tonight. Own implementation.
# Built by tools/claude_build_capharv.py (derivation there).
# ---------------------------------------------------------------------------
_CH_SHED = 90
_CH_SELL = True
_CH_ANIMALS = {"GOOSE": ("EGG", 4, 4, 1), "COW": ("MILK", 6, 8, 2), "SHEEP": ("WOOL", 6, 6, 3)}
_CH_MOVES = {"NORTH": (0, -1), "SOUTH": (0, 1), "EAST": (1, 0), "WEST": (-1, 0)}
_CH_STATE = {}
_CH_REPORT = {"ch_collect_swaps": 0, "ch_care_swaps": 0, "ch_saved": 0, "ch_sold": 0, "ch_shed_block": 0,
              "ch_errors": 0}


def _ch_tape(seat, t):
    native = _IMPL.chassis.players.get(seat)
    if not native or t > 719:
        return {}
    tape = _IMPL.chassis.routes[2 if t >= 648 else native["route"]]
    return tape[t] if t < len(tape) and isinstance(tape[t], dict) else {}


def _ch_visits_today(obs, action):
    """{pos: [(t, op)]} for non-move commands from the next step to the end of today."""
    seat = int(obs["player"])
    step = int(obs["step"])
    farm = obs["farms"][seat]
    board = len(farm["tiles"])
    half = board // 2
    access = [(half - 1, half - 1), (half, half - 1), (half - 1, half), (half, half)]
    positions = [list(farm["farmer"])] + [list(h) for h in farm["hands"]]
    out = {}
    for t in range(step, (step // 24 + 1) * 24):
        act = action if t == step else _ch_tape(seat, t)
        units = [act.get("farmer") or ["PASS"]] + list(act.get("hands") or [])
        for i in range(len(positions)):
            cmd = units[i] if i < len(units) and units[i] else ["PASS"]
            if cmd[0] in _CH_MOVES:
                dx, dy = _CH_MOVES[cmd[0]]
                nx, ny = positions[i][0] + dx, positions[i][1] + dy
                if 0 <= nx < board and 0 <= ny < board:
                    positions[i] = [nx, ny]
            elif t > step:
                out.setdefault(tuple(positions[i]), []).append((t, cmd[0]))
        for _ in range(sum(1 for o in (act.get("market") or []) if o and o[0] == "HIRE")):
            occ = {a: 0 for a in access}
            for p in positions:
                if tuple(p) in occ:
                    occ[tuple(p)] += 1
            positions.append(list(min(access, key=lambda a: (occ[a], access.index(a)))))
    return out


_CH_PARENT = agent
del agent


def agent(observation, configuration=None):
    action = _CH_PARENT(observation, configuration)
    try:
        step = int(observation["step"])
        seat = int(observation["player"])
        st = _CH_STATE.get(seat)
        if step == 0 or st is None or step <= st["step"]:
            st = _CH_STATE[seat] = {"step": -1, "credit": {}}
            if step == 0:
                for k in _CH_REPORT:
                    _CH_REPORT[k] = 0
        st["step"] = step
        if not isinstance(action, dict) or step > 717:
            return action
        day = step // 24
        farm = observation["farms"][seat]
        priv = observation["private"]
        prices = observation["market"]["prices"]
        positions = [tuple(farm["farmer"])] + [tuple(h) for h in farm["hands"]]
        units = [list(action.get("farmer") or ["PASS"])] + [list(c) for c in (action.get("hands") or [])]
        market = [list(o) for o in (action.get("market") or [])]
        changed = False
        visits = None
        for i, pos in enumerate(positions[:len(units)]):
            cmd = units[i]
            if not cmd or cmd[0] not in ("CARE", "COLLECT_FERTILIZER"):
                continue
            tile = farm["tiles"][pos[1]][pos[0]]
            if not (isinstance(tile, dict) and tile.get("animal") in _CH_ANIMALS):
                continue
            product, cap, first, interval = _CH_ANIMALS[tile["animal"]]
            since = day + 1 - int(tile.get("placed_day", 99)) - first
            if since < 0 or since % interval != 0:
                continue
            y = int(tile.get("yield_units", 0))
            if visits is None:
                visits = _ch_visits_today(observation, action)
            later = visits.get(pos, [])
            if any(op == "HARVEST" for t, op in later):
                continue
            fed = bool(tile.get("fed_today")) or any(op == "FEED" for t, op in later)
            prod = 1 + (int(tile.get("pending_care_bonus", 0)) if fed else 0)
            overflow = y + prod - cap
            if overflow <= 0 or y <= 0:
                continue
            quote = int(prices.get(product, 0))
            if cmd[0] == "COLLECT_FERTILIZER":
                if overflow * quote <= int(prices.get("FERTILIZER", 0)):
                    continue
            else:
                if any(op == "COLLECT_FERTILIZER" for t, op in later) or overflow <= 1:
                    continue
            carried = sum(int(v) for inv in priv["inventories"] for v in inv.values())
            if sum(int(v) for v in priv["shed"].values()) + carried + y >= _CH_SHED:
                _CH_REPORT["ch_shed_block"] += 1
                continue
            units[i] = ["HARVEST"]
            _CH_REPORT["ch_collect_swaps" if cmd[0] == "COLLECT_FERTILIZER" else "ch_care_swaps"] += 1
            saved = overflow if cmd[0] == "COLLECT_FERTILIZER" else overflow - 1
            _CH_REPORT["ch_saved"] += saved
            st["credit"][product] = st["credit"].get(product, 0) + saved
            changed = True
        if _CH_SELL and any(v > 0 for v in st["credit"].values()):
            view_action = {"farmer": units[0], "hands": units[1:], "market": market}
            stock = dict(projected_shed(view_action, FarmView(observation)))
            for product, credit in list(st["credit"].items()):
                if credit <= 0 or len(market) >= 10 or int(prices.get(product, 0)) < 2:
                    continue
                selling = sum(int(o[2]) for o in market if len(o) >= 3 and o[:2] == ["SELL", product])
                q = min(credit, int(stock.get(product, 0)) - selling)
                if q > 0:
                    for o in market:
                        if len(o) >= 3 and o[:2] == ["SELL", product]:
                            o[2] = int(o[2]) + q
                            break
                    else:
                        market.insert(0, ["SELL", product, q])
                    st["credit"][product] = credit - q
                    _CH_REPORT["ch_sold"] += q
                    changed = True
        if changed:
            action = dict(action)
            action["farmer"] = units[0]
            action["hands"] = units[1:]
            action["market"] = market[:10]
    except Exception:
        _CH_REPORT["ch_errors"] += 1
    return action


agent.telemetry = _CH_REPORT
agent = globals().pop('agent')


# ---------------------------------------------------------------------------
# Claude SHEDROOM layer: sell shed goods before the night drop overflows. Own implementation.
# Built by tools/claude_build_shedroom.py (derivation there).
# ---------------------------------------------------------------------------
_SR_MARGIN = 4
_SR_HOURS = (22, 23)
_SR_PRODUCTS = ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL", "FERTILIZER")
_SR_REPORT = {"sr_turns": 0, "sr_units": 0, "sr_errors": 0}


def _sr_tape(seat, t):
    native = _IMPL.chassis.players.get(seat)
    if not native or t > 719:
        return {}
    tape = _IMPL.chassis.routes[2 if t >= 648 else native["route"]]
    return tape[t] if t < len(tape) and isinstance(tape[t], dict) else {}


_SR_PARENT = agent
del agent


def agent(observation, configuration=None):
    action = _SR_PARENT(observation, configuration)
    try:
        step = int(observation["step"])
        if step == 0:
            for k in _SR_REPORT:
                _SR_REPORT[k] = 0
        if step % 24 not in _SR_HOURS or step >= 717 or not isinstance(action, dict):
            return action
        seat = int(observation["player"])
        farm = observation["farms"][seat]
        priv = observation["private"]
        view = FarmView(observation)
        proj = dict(projected_shed(action, view))
        market = [list(o) for o in (action.get("market") or [])]
        left = dict(proj)
        night_shed = sum(max(0, int(v)) for v in proj.values())
        for o in market:
            if len(o) >= 3 and o[0] == "SELL":
                got = min(max(0, int(o[2])), max(0, int(left.get(o[1], 0))))
                left[o[1]] = left.get(o[1], 0) - got
                night_shed -= got
            elif len(o) >= 3 and o[0] in ("BUY_PRODUCT", "BUY_ANIMAL"):
                night_shed += max(0, int(o[2]))
        units = [action.get("farmer") or ["PASS"]] + list(action.get("hands") or [])
        carried = 0
        for i, pos in enumerate(view.positions):
            inv = priv["inventories"][i] if i < len(priv["inventories"]) else {}
            held = sum(max(0, int(v)) for v in inv.values())
            cmd = units[i] if i < len(units) and units[i] else ["PASS"]
            tile = farm["tiles"][pos[1]][pos[0]] if isinstance(pos, (list, tuple)) else None
            op = cmd[0]
            if op == "DROP" and _shed_adjacent(pos, view.board):
                held = 0
            elif op == "HARVEST" and isinstance(tile, dict):
                held += max(0, int(tile.get("yield_units", 0)))
            elif op == "COLLECT_FERTILIZER" and isinstance(tile, dict) and tile.get("fertilizer_available"):
                held += 1
            elif op in ("FEED", "FERTILIZE") and held > 0:
                held -= 1
            elif op == "PICKUP" and len(cmd) >= 2 and _shed_adjacent(pos, view.board):
                held += max(1, int(cmd[2]) if len(cmd) >= 3 else 1)
            carried += held
        cap = int((configuration or {}).get("shedCapacity", 100)) if isinstance(configuration, dict) else 100
        overflow = night_shed + carried - cap + _SR_MARGIN
        if overflow <= 0:
            return action
        need = {"WHEAT": 0, "FERTILIZER": 0}
        for t in range(step + 1, min(719, step + 25)):
            act = _sr_tape(seat, t)
            for c in [act.get("farmer") or ["PASS"]] + list(act.get("hands") or []):
                if not c:
                    continue
                if c[0] == "FEED":
                    need["WHEAT"] += 1
                elif c[0] == "FERTILIZE":
                    need["FERTILIZER"] += 1
        prices = observation["market"]["prices"]
        cands = []
        for item in _SR_PRODUCTS:
            spare = int(left.get(item, 0)) - need.get(item, 0)
            if spare > 0 and int(prices.get(item, 0)) >= 2:
                cands.append((int(prices.get(item, 0)), item, spare))
        cands.sort()
        sold_now = 0
        for price, item, spare in cands:
            if overflow <= 0:
                break
            q = min(spare, overflow)
            for o in market:
                if len(o) >= 3 and o[:2] == ["SELL", item]:
                    o[2] = int(o[2]) + q
                    break
            else:
                if len(market) >= 10:
                    continue
                market.append(["SELL", item, q])
            overflow -= q
            sold_now += q
        if sold_now:
            _SR_REPORT["sr_turns"] += 1
            _SR_REPORT["sr_units"] += sold_now
            action = dict(action)
            action["market"] = market
    except Exception:
        _SR_REPORT["sr_errors"] += 1
    return action


agent.telemetry = _SR_REPORT
agent = globals().pop('agent')


# ---------------------------------------------------------------------------
# Claude HERD2 layer: goose / cow / sheep choice at the tape's goose purchase.
# Own implementation. Built by tools/claude_build_herd2.py (derivation there).
# ---------------------------------------------------------------------------
_HD2_FROM = 192
_HD2_TO = 360
_HD2_RATIO = 1.3
_HD2_MIN_GAIN = 600.0
_HD2_LOOKBACK = 3
_HD2_OPTIONS = ('COW', 'SHEEP')
_HD2_CARE = 0.8
_HD2_FUTURE = 0.0

_HD2_SPEC = {
    "GOOSE": {"cost": 300, "first": 4, "interval": 1, "per": 2, "product": "EGG", "structure": "COOP"},
    "COW": {"cost": 400, "first": 8, "interval": 2, "per": 3, "product": "MILK", "structure": "PASTURE"},
    "SHEEP": {"cost": 500, "first": 6, "interval": 3, "per": 4, "product": "WOOL", "structure": "PASTURE"},
}
_HD2_SHOP_TYPES = {
    "BAKERY": ("EGG", "WHEAT"), "PIZZA_SHOP": ("MILK", "TOMATO", "WHEAT"),
    "BRUNCH_SPOT": ("EGG", "WHEAT", "STRAWBERRY"), "YARN_STORE": ("WOOL",),
    "ICE_CREAM_SHOP": ("STRAWBERRY", "MILK", "WHEAT"), "PET_CAFE": ("CARROT",),
    "SMOOTHIE_SHOP": ("STRAWBERRY", "MILK"), "FARMERS_MARKET": ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY"),
}
_HD2_STATE = {}
_HD2_REPORT = {"hd2_decision": "", "hd2_ev": "", "hd2_rewrites": 0, "hd2_credit_units": 0,
               "hd2_sold_units": 0, "hd2_errors": 0}


def _hd2_daily_shop_demand(item, shops):
    total = 0.0
    for name in shops:
        products = _HD2_SHOP_TYPES.get(name, ())
        if item in products:
            total += 6.0 * (2 if len(products) == 1 else 1)
    return total


def _hd2_future_demand_per_day(item):
    """Expected extra daily demand of one more uniformly drawn shop instance."""
    return sum(6.0 * (2 if len(p) == 1 else 1) for p in _HD2_SHOP_TYPES.values() if item in p) / len(_HD2_SHOP_TYPES)


def _hd2_schedule(animal, placed_day, day_from):
    """Units an animal of this type produces on each day >= day_from (daily care assumed,
    scaled by _HD2_CARE)."""
    spec = _HD2_SPEC[animal]
    out = {}
    for d in range(max(day_from, placed_day + spec["first"]), 30):
        if (d - placed_day - spec["first"]) % spec["interval"] == 0:
            out[d] = out.get(d, 0.0) + 1.0 + (spec["per"] - 1) * _HD2_CARE
    return out


def _hd2_ev(option, k, obs, st):
    """Margin value of k new animals of `option`: their own revenue, plus the price change
    their supply causes on (our existing future units - rival existing future units)."""
    spec = _HD2_SPEC[option]
    item = spec["product"]
    animal_of = {"EGG": "GOOSE", "MILK": "COW", "WOOL": "SHEEP"}[item]
    day = int(obs["step"]) // 24
    seat = int(obs["player"])
    market = obs["market"]
    params = {key: dict(v) for key, v in _R37_MARKET_PARAMS.items()}
    for key, patch in (market.get("params") or {}).items():
        if key in params and isinstance(patch, dict):
            params[key].update(patch)
    # existing supply, per farm, per day
    existing = [dict(), dict()]
    for farm_index, farm in enumerate(obs["farms"]):
        for row in farm["tiles"]:
            for tile in row:
                if isinstance(tile, dict) and tile.get("animal") == animal_of:
                    for d, u in _hd2_schedule(animal_of, int(tile.get("placed_day", day)), day + 1).items():
                        existing[farm_index][d] = existing[farm_index].get(d, 0.0) + u
    shed = (obs.get("private") or {}).get("shed") or {}
    carried = sum(int(inv.get(animal_of, 0)) for inv in (obs.get("private") or {}).get("inventories") or [])
    for _ in range(int(shed.get(animal_of, 0)) + carried):
        for d, u in _hd2_schedule(animal_of, day + 1, day + 1).items():
            existing[seat][d] = existing[seat].get(d, 0.0) + u
    # Purchases the tape already plans after this turn; a family-similar rival runs the same tape.
    native = _IMPL.chassis.players.get(seat)
    if native:
        similar = _r37_similarity(obs) >= 0.9
        for t in range(int(obs["step"]) + 1, 696):
            tape = _IMPL.chassis.routes[2 if t >= 648 else native["route"]]
            if t >= len(tape) or not isinstance(tape[t], dict):
                continue
            for order in tape[t].get("market", []) or []:
                if len(order) >= 3 and order[0] == "BUY_ANIMAL" and order[1] == animal_of:
                    for _ in range(max(0, int(order[2]))):
                        for d, u in _hd2_schedule(animal_of, t // 24 + 1, day + 1).items():
                            existing[seat][d] = existing[seat].get(d, 0.0) + u
                            if similar:
                                existing[1 - seat][d] = existing[1 - seat].get(d, 0.0) + u
    ours_existing, rival_existing = existing[seat], existing[1 - seat]
    new = {}
    for d, u in _hd2_schedule(option, day + 1, day + 1).items():
        new[d] = u * k
    shops = list((obs.get("town") or {}).get("unlocked_shops") or [])
    unlocks_left = max(0, 8 - len(shops))
    base_demand = _hd2_daily_shop_demand(item, shops) + 1.0
    extra_demand = _hd2_future_demand_per_day(item) * _HD2_FUTURE

    def path(with_new):
        inv = float(market["inventory"][item])
        prices, revenue = {}, 0.0
        for d in range(day + 1, 30):
            opened = min(unlocks_left, max(0, (d // 3) - (day // 3)))
            inv -= base_demand + extra_demand * opened
            inv += ours_existing.get(d, 0.0) + rival_existing.get(d, 0.0)
            prices[d] = _r37_market_price(item, int(round(inv)), params)
            if with_new:
                units = int(round(new.get(d, 0.0)))
                for _ in range(units):
                    price = _r37_market_price(item, int(round(inv)), params)
                    revenue += price
                    if price > 1:
                        inv += 1
        return prices, revenue

    base_prices, _ = path(False)
    new_prices, revenue = path(True)
    swing = sum((new_prices[d] - base_prices[d]) * (ours_existing.get(d, 0.0) - rival_existing.get(d, 0.0))
                for d in base_prices)
    return revenue + swing - spec["cost"] * k, revenue


def _hd2_decide(obs, action, st):
    market = action.get("market") or []
    buys = [o for o in market if len(o) >= 3 and o[0] == "BUY_ANIMAL" and o[1] == "GOOSE"]
    if not buys:
        return
    st["decided"] = True
    step = int(obs["step"])
    if not (_HD2_FROM <= step < _HD2_TO):
        return
    farm = obs["farms"][int(obs["player"])]
    if any(isinstance(t, dict) and t.get("kind") == "COOP" for row in farm["tiles"] for t in row):
        _HD2_REPORT["hd2_decision"] = "skip:coop_exists"
        return
    k = sum(max(0, int(o[2])) for o in buys)
    k_plan = max(k, 3)
    evs = {opt: _hd2_ev(opt, k_plan, obs, st)[0] for opt in ("GOOSE",) + tuple(_HD2_OPTIONS)}
    _HD2_REPORT["hd2_ev"] = ",".join("%s:%d" % (o, v) for o, v in sorted(evs.items()))
    best = max(_HD2_OPTIONS, key=lambda o: evs[o]) if _HD2_OPTIONS else None
    goose = evs["GOOSE"]
    if best is None:
        return
    gain = evs[best] - goose
    ok_ratio = evs[best] >= _HD2_RATIO * max(goose, 1.0)
    extra_cost = (_HD2_SPEC[best]["cost"] - 300) * k
    cash = float(farm.get("money", 0))
    if gain >= _HD2_MIN_GAIN and ok_ratio and cash >= 300 * k + extra_cost + 50:
        st["mode"] = best
        _HD2_REPORT["hd2_decision"] = "%s@%d" % (best, step)
    else:
        _HD2_REPORT["hd2_decision"] = "keep@%d" % step


def _hd2_rewrite(obs, action, st):
    mode = st["mode"]
    spec = _HD2_SPEC[mode]
    item = spec["product"]
    seat = int(obs["player"])
    farm = obs["farms"][seat]
    private = obs["private"]
    positions = [farm["farmer"]] + list(farm["hands"])
    market = action.get("market") or []
    cash = float(farm.get("money", 0))
    seed_cost = {"WHEAT": 10, "CARROT": 20, "TOMATO": 50, "STRAWBERRY": 100, "MELON": 80}
    for order in market:
        if len(order) >= 3 and order[0] == "BUY_ANIMAL" and order[1] == "GOOSE":
            n = max(0, int(order[2]))
            affordable = int(max(0.0, cash) // spec["cost"])
            order[1] = mode
            order[2] = min(n, affordable)
            cash -= order[2] * spec["cost"]
            _HD2_REPORT["hd2_rewrites"] += 1
        elif len(order) >= 3 and order[0] in ("BUY_ANIMAL", "BUY_SEED", "BUY_PRODUCT"):
            # money spent by earlier orders of the same list is not available to the swap (DS-5 #6)
            q = max(0, int(order[2]))
            if order[0] == "BUY_ANIMAL":
                cash -= q * {"GOOSE": 300, "COW": 400, "SHEEP": 500}.get(order[1], 0)
            elif order[0] == "BUY_SEED":
                cash -= q * seed_cost.get(order[1], 0)
            else:
                cash -= q * int((obs["market"]["prices"] or {}).get(order[1], 0))
        elif order and order[0] == "BUY_LAND":
            cash -= 4000
    workers = [action.get("farmer") or ["PASS"]] + list(action.get("hands") or [])
    for actor, work in enumerate(workers[:len(positions)]):
        if not work:
            continue
        x, y = positions[actor]
        tile = farm["tiles"][y][x]
        if work[0] == "BUILD_COOP":
            workers[actor] = ["BUILD_PASTURE"]
            _HD2_REPORT["hd2_rewrites"] += 1
        elif len(work) >= 2 and work[0] in ("PICKUP", "PLACE") and work[1] == "GOOSE":
            workers[actor] = [work[0], mode] + list(work[2:])
            _HD2_REPORT["hd2_rewrites"] += 1
            if work[0] == "PLACE":
                st["pending"].append((x, y, int(obs["step"]) // 24))
        elif len(work) >= 2 and work[0] == "PLACE" and work[1] == "EGG":
            workers[actor] = ["PLACE", item] + list(work[2:])
            _HD2_REPORT["hd2_rewrites"] += 1
        elif work == ["HARVEST"] and (x, y) in st["sites"] and isinstance(tile, dict) \
                and tile.get("animal") == mode:
            units = max(0, int(tile.get("yield_units", 0)))
            st["credit"] += units
            _HD2_REPORT["hd2_credit_units"] += units
    action["farmer"] = workers[0]
    action["hands"] = workers[1:]
    if st["credit"] > 0:
        try:
            stock = projected_shed(action, FarmView(obs))
        except Exception:
            stock = dict(private.get("shed") or {})
        planned = sum(max(0, int(o[2])) for o in market if len(o) >= 3 and o[:2] == ["SELL", item])
        extra = min(st["credit"], max(0, int(stock.get(item, 0)) - planned))
        if extra > 0:
            for order in market:
                if len(order) >= 3 and order[:2] == ["SELL", item]:
                    order[2] = int(order[2]) + extra
                    break
            else:
                if len(market) < 10:
                    market.insert(0, ["SELL", item, extra])
                else:
                    extra = 0
            st["credit"] -= extra
            _HD2_REPORT["hd2_sold_units"] += extra
    action["market"] = market


def _hd2_confirm(obs, st):
    farm = obs["farms"][int(obs["player"])]
    keep = []
    for x, y, day in st["pending"]:
        tile = farm["tiles"][y][x]
        if isinstance(tile, dict) and tile.get("animal") == st["mode"] and tile.get("placed_day") == day:
            st["sites"][(x, y)] = day
        elif int(obs["step"]) // 24 <= day + 1:
            keep.append((x, y, day))
    st["pending"] = keep


_HD2_PARENT = agent
del agent


def agent(observation, configuration=None):
    action = _HD2_PARENT(observation, configuration)
    try:
        seat = int(observation["player"])
        step = int(observation["step"])
        st = _HD2_STATE.get(seat)
        if st is None or step <= st["step"]:
            st = _HD2_STATE[seat] = {"step": -1, "inv": {}, "decided": False, "mode": None,
                                     "pending": [], "sites": {}, "credit": 0}
            if step == 0:
                _HD2_REPORT.update(hd2_decision="", hd2_ev="", hd2_rewrites=0, hd2_credit_units=0,
                                   hd2_sold_units=0, hd2_errors=0)
        st["step"] = step
        day = step // 24
        if day not in st["inv"]:
            st["inv"][day] = dict(observation["market"]["inventory"])
        if not isinstance(action, dict):
            return action
        if st["mode"]:
            _hd2_confirm(observation, st)
        elif not st["decided"]:
            _hd2_decide(observation, action, st)
        if st["mode"]:
            action = copy.deepcopy(action)
            _hd2_rewrite(observation, action, st)
    except Exception:
        _HD2_REPORT["hd2_errors"] += 1
    return action


agent.telemetry = _HD2_REPORT
agent = globals().pop('agent')


# ---------------------------------------------------------------------------
# Claude COWSWAP layer: cow / goose / sheep at the tape's first cow purchase. Own implementation.
# Built by tools/claude_build_cowswap.py (derivation there). Requires HERD2 above.
# ---------------------------------------------------------------------------
_CS_FROM = 144
_CS_TO = 192
_CS_RATIO = 1.3
_CS_MIN_GAIN = 600.0
_CS_OPTIONS = ('GOOSE',)
_CS_SHOP_RULE = 'nomilk'
_CS_MOVES = {"NORTH": (0, -1), "SOUTH": (0, 1), "EAST": (1, 0), "WEST": (-1, 0)}
_CS_STATE = {}
_CS_REPORT = {"cs_decision": "", "cs_ev": "", "cs_rewrites": 0, "cs_broken": 0, "cs_credit": 0,
              "cs_sold": 0, "cs_errors": 0}


def _cs_tape(seat, t):
    native = _IMPL.chassis.players.get(seat)
    if not native or t > 719:
        return {}
    tape = _IMPL.chassis.routes[2 if t >= 648 else native["route"]]
    return tape[t] if t < len(tape) and isinstance(tape[t], dict) else {}


def _cs_spawn(positions, board):
    half = board // 2
    access = [(half - 1, half - 1), (half, half - 1), (half - 1, half), (half, half)]
    occ = {a: 0 for a in access}
    for p in positions:
        if tuple(p) in occ:
            occ[tuple(p)] += 1
    return list(min(access, key=lambda a: (occ[a], access.index(a))))


def _cs_plan(obs, action, k, mode):
    seat = int(obs["player"])
    step = int(obs["step"])
    farm = obs["farms"][seat]
    board = len(farm["tiles"])
    positions = [list(farm["farmer"])] + [list(h) for h in farm["hands"]]
    end = (step // 24 + 1) * 24 - 1
    builds, pickups, places = [], [], []
    for t in range(step, end + 1):
        act = action if t == step else _cs_tape(seat, t)
        units = [act.get("farmer") or ["PASS"]] + list(act.get("hands") or [])
        for i in range(len(positions)):
            cmd = units[i] if i < len(units) and units[i] else ["PASS"]
            pos = tuple(positions[i])
            if cmd[0] in _CS_MOVES:
                dx, dy = _CS_MOVES[cmd[0]]
                nx, ny = pos[0] + dx, pos[1] + dy
                if 0 <= nx < board and 0 <= ny < board:
                    positions[i] = [nx, ny]
            elif cmd[0] == "BUILD_PASTURE":
                builds.append((t, i, pos))
            elif len(cmd) >= 2 and cmd[0] == "PICKUP" and cmd[1] == "COW":
                pickups.append((t, i, max(1, int(cmd[2]) if len(cmd) > 2 else 1)))
            elif len(cmd) >= 2 and cmd[0] == "PLACE" and cmd[1] == "COW":
                places.append((t, i, pos))
        hires = sum(1 for o in (act.get("market") or []) if o and o[0] == "HIRE")
        for _ in range(hires):
            positions.append(_cs_spawn(positions, board))
    chosen, tiles = [], set()
    for t, i, pos in places:
        if pos not in tiles:
            chosen.append((t, i, pos))
            tiles.add(pos)
        if len(chosen) == k:
            break
    if len(chosen) < k:
        return None
    plan = {"builds": {}, "pickups": {}, "places": {}}
    buying_land = any(o and o[0] == "BUY_LAND" for o in (action.get("market") or []))
    unlocked = list(farm.get("unlocked_quadrants") or ["NW"])
    next_quadrant = [q for q in ("NE", "SW", "SE") if q not in unlocked][:1]
    half = board // 2
    for t, i, pos in chosen:
        x, y = pos
        tile = farm["tiles"][y][x]
        if mode == "GOOSE":
            quadrant = ("N" if y < half else "S") + ("W" if x < half else "E")
            locked_but_bought = tile == "LOCKED" and buying_land and quadrant in next_quadrant
            if tile is not None and not locked_but_bought:
                return None  # already built (or occupied): cannot become a coop without extra turns
            prior = [(tb, ib) for tb, ib, pb in builds if pb == pos and tb < t]
            if not prior:
                return None
            tb, ib = prior[-1]
            plan["builds"][(tb, ib)] = pos
        carrier = [(tp, ip, q) for tp, ip, q in pickups if ip == i and tp < t]
        if not carrier:
            return None
        tp, ip, q = carrier[-1]
        plan["pickups"][(tp, ip)] = plan["pickups"].get((tp, ip), 0) + 1
        plan["places"][(t, i)] = pos
    for key, n in plan["pickups"].items():
        q = next(q for tp, ip, q in pickups if (tp, ip) == key)
        if q != n:
            return None  # a pickup that also carries unswapped cows cannot be split
    return plan


_CS_PARENT = agent
del agent


def agent(observation, configuration=None):
    action = _CS_PARENT(observation, configuration)
    try:
        seat = int(observation["player"])
        step = int(observation["step"])
        st = _CS_STATE.get(seat)
        if st is None or step <= st["step"]:
            st = _CS_STATE[seat] = {"step": -1, "decided": False, "mode": None, "plan": None,
                                    "broken": False, "sites": {}, "pending": [], "credit": 0}
            if step == 0:
                _CS_REPORT.update(cs_decision="", cs_ev="", cs_rewrites=0, cs_broken=0, cs_credit=0,
                                  cs_sold=0, cs_errors=0)
        st["step"] = step
        if not isinstance(action, dict):
            return action
        farm = observation["farms"][seat]
        positions = [farm["farmer"]] + list(farm["hands"])
        market = [list(o) for o in (action.get("market") or [])]
        # confirm placements
        if st["pending"]:
            keep = []
            for x, y, day in st["pending"]:
                tile = farm["tiles"][y][x]
                if isinstance(tile, dict) and tile.get("animal") == st["mode"] and tile.get("placed_day") == day:
                    st["sites"][(x, y)] = day
                elif step // 24 <= day:
                    keep.append((x, y, day))
            st["pending"] = keep
        if not st["decided"] and _CS_FROM <= step < _CS_TO:
            buys = [o for o in market if len(o) >= 3 and o[0] == "BUY_ANIMAL" and o[1] == "COW" and int(o[2]) > 0]
            shops_now = list((observation.get("town") or {}).get("unlocked_shops") or [])
            shop_ok = True
            if _CS_SHOP_RULE:
                # research/claude_20260913/RESULTS.md: over 48 seeds the swap only paid with an egg shop
                # open and no milk shop open (+1,254 mean over 9 seeds); with a milk shop it lost.
                no_milk = not any(s in ("PIZZA_SHOP", "ICE_CREAM_SHOP", "SMOOTHIE_SHOP") for s in shops_now)
                if _CS_SHOP_RULE == "nomilk":
                    # 14 seeds without a milk shop and without a yarn store: +1,203 mean
                    shop_ok = no_milk and "YARN_STORE" not in shops_now
                else:
                    shop_ok = no_milk and any(s in ("BAKERY", "BRUNCH_SPOT") for s in shops_now)
            if buys and not shop_ok:
                st["decided"] = True
                _CS_REPORT["cs_decision"] = "shoprule@%d" % step
            elif buys:
                st["decided"] = True
                k = sum(int(o[2]) for o in buys)
                evs = {opt: _hd2_ev(opt, k, observation, st)[0] for opt in ("COW",) + tuple(_CS_OPTIONS)}
                _CS_REPORT["cs_ev"] = ",".join("%s:%d" % (o, v) for o, v in sorted(evs.items()))
                best = max(_CS_OPTIONS, key=lambda o: evs[o])
                cow = evs["COW"]
                if evs[best] - cow >= _CS_MIN_GAIN and evs[best] >= _CS_RATIO * max(cow, 1.0):
                    plan = _cs_plan(observation, action, k, best)
                    if plan is not None:
                        st["mode"], st["plan"] = best, plan
                        _CS_REPORT["cs_decision"] = "%s@%d" % (best, step)
                        for o in market:
                            if len(o) >= 3 and o[0] == "BUY_ANIMAL" and o[1] == "COW":
                                o[1] = best
                                _CS_REPORT["cs_rewrites"] += 1
                    else:
                        _CS_REPORT["cs_decision"] = "noplan@%d" % step
                else:
                    _CS_REPORT["cs_decision"] = "keep@%d" % step
        if st["mode"] and st["plan"] and not st["broken"]:
            plan = st["plan"]
            units = [action.get("farmer") or ["PASS"]] + list(action.get("hands") or [])
            for i in range(min(len(units), len(positions))):
                cmd = units[i] or ["PASS"]
                pos = (int(positions[i][0]), int(positions[i][1]))
                key = (step, i)
                if key in plan["builds"]:
                    if cmd == ["BUILD_PASTURE"] and pos == plan["builds"][key]:
                        units[i] = ["BUILD_COOP"]
                        _CS_REPORT["cs_rewrites"] += 1
                    else:
                        st["broken"] = True
                if key in plan["pickups"]:
                    if len(cmd) >= 2 and cmd[0] == "PICKUP" and cmd[1] == "COW":
                        units[i] = ["PICKUP", st["mode"]] + list(cmd[2:])
                        _CS_REPORT["cs_rewrites"] += 1
                    else:
                        st["broken"] = True
                if key in plan["places"]:
                    if len(cmd) >= 2 and cmd[0] == "PLACE" and cmd[1] == "COW" and pos == plan["places"][key]:
                        units[i] = ["PLACE", st["mode"]] + list(cmd[2:])
                        st["pending"].append((pos[0], pos[1], step // 24))
                        _CS_REPORT["cs_rewrites"] += 1
                    else:
                        st["broken"] = True
            if st["broken"]:
                _CS_REPORT["cs_broken"] += 1
            action = dict(action)
            action["farmer"] = units[0]
            action["hands"] = units[1:]
        # credit harvests on swapped tiles and sell them as they reach the shed
        if st["sites"]:
            product = _HD2_SPEC[st["mode"]]["product"]
            units = [action.get("farmer") or ["PASS"]] + list(action.get("hands") or [])
            for i in range(min(len(units), len(positions))):
                x, y = int(positions[i][0]), int(positions[i][1])
                tile = farm["tiles"][y][x]
                if units[i] == ["HARVEST"] and (x, y) in st["sites"] and isinstance(tile, dict) \
                        and tile.get("animal") == st["mode"]:
                    n = max(0, int(tile.get("yield_units", 0)))
                    st["credit"] += n
                    _CS_REPORT["cs_credit"] += n
            if st["credit"] > 0:
                stock = projected_shed(action, FarmView(observation))
                planned = sum(max(0, int(o[2])) for o in market if len(o) >= 3 and o[:2] == ["SELL", product])
                extra = min(st["credit"], max(0, int(stock.get(product, 0)) - planned))
                if extra > 0:
                    for o in market:
                        if len(o) >= 3 and o[:2] == ["SELL", product]:
                            o[2] = int(o[2]) + extra
                            break
                    else:
                        if len(market) < 10:
                            market.insert(0, ["SELL", product, extra])
                        else:
                            extra = 0
                    st["credit"] -= extra
                    _CS_REPORT["cs_sold"] += extra
        action = dict(action)
        action["market"] = market
    except Exception:
        _CS_REPORT["cs_errors"] += 1
    return action


agent.telemetry = _CS_REPORT
agent = globals().pop('agent')

# Bounded alternative productive openings. Dmitrii Gluzdov, 2026, Apache-2.0.
# The upstream The 2945 Farm source and its notices are preserved above.
_ALT_MODE = 'EarlyCycle'
_ALT_RAW = copy.deepcopy(_IMPL.chassis.routes[0][:96])
_ALT_CT = dict(CT_TABLE)
_ALT_STATE = {}
_ALT_REPORT = {}

def _alt_install(mode):
    global CT_TABLE
    tape=_IMPL.chassis.routes[0]
    tape[:96]=copy.deepcopy(_ALT_RAW)
    CT_TABLE=dict(_ALT_CT)
    if mode=='Original': return
    CT_TABLE={}
    tape[0]['market']=[['BUY_PRODUCT','WHEAT',5],['BUY_SEED','WHEAT',1]]
    tape[1]['market']=[o for o in tape[1]['market'] if not (len(o)>=3 and o[0] in ('BUY_PRODUCT','SELL') and o[1]=='WHEAT')]
    # Day-zero idle hand 1 walks from (5,4) to the future (2,4) pasture.
    for step,command in {2:['WEST'],3:['WEST'],4:['WEST'],5:['PLANT','WHEAT'],6:['WATER']}.items():
        assert tape[step]['hands'][1]==['PASS']
        tape[step]['hands'][1]=command
    # On day one, water instead of building the not-yet-needed pasture.
    assert tape[29]['hands'][2]==['BUILD_PASTURE']
    tape[29]['hands'][2]=['WATER']
    # Day-two idle hand 0: water, harvest, restore pasture, deliver.
    commands=[['WEST'],['WEST'],['WEST'],['WATER'],['HARVEST'],['BUILD_PASTURE'],['EAST'],['EAST'],['DROP']]
    for step,command in zip(range(49,58),commands):
        assert tape[step]['hands'][0]==['PASS']
        tape[step]['hands'][0]=command
    if mode=='TomatoInsteadOfCow':
        tape[0]['market'].append(['BUY_SEED','TOMATO',1])
        cow=next(o for o in tape[1]['market'] if o[:2]==['BUY_ANIMAL','COW'])
        assert cow[2]==2; cow[2]=1
        # The first carrier still owns the bought cow; the other cow's site
        # becomes one tomato plant, with its worker route left in place.
        assert tape[2]['hands'][4][:2]==['PICKUP','COW']
        assert tape[3]['hands'][4]==['BUILD_PASTURE']
        assert tape[4]['hands'][4][:2]==['PLACE','COW']
        tape[2]['hands'][4]=['PASS']
        tape[3]['hands'][4]=['PASS']
        tape[4]['hands'][4]=['PLANT','TOMATO']
        tape[5]['hands'][4]=['WATER']
    assert max(len(a.get('market',[])) for a in tape[:96])<=10

def _alt_sell_extra(action,item,n):
    if n<=0:return action
    orders=[list(o) for o in action.get('market',[])]
    sell=next((o for o in orders if len(o)>=3 and o[:2]==['SELL',item]),None)
    if sell is not None:sell[2]+=n
    elif len(orders)<10:orders.append(['SELL',item,n])
    else:return action
    return dict(action,market=orders)

_ALT_PARENT=agent
def agent(observation,configuration=None):
    seat,step=int(observation['player']),int(observation['step'])
    state=_ALT_STATE.get(seat)
    if state is None or step<=state['step']:
        mode=_ALT_MODE
        if mode=='Mixed':
            # Private RNG: no mutation of the engine or opponent's random state.
            # Seed is used only for reproducible opening selection, never prediction.
            import random as _opening_random
            seed=(configuration or {}).get('seed',0)
            bit=_opening_random.Random('productive-opening:'+str(seed)+':'+str(seat)).getrandbits(1)
            mode='EarlyCycle' if bit else 'Original'
        _alt_install(mode)
        state=_ALT_STATE[seat]={'step':-1,'mode':mode}
        _ALT_REPORT.clear()
        _ALT_REPORT.update(selected_opening=mode,temporary_crop_seen=0,temporary_crop_harvested=0,
                           restored_pasture_seen=0,delivered_extra_wheat=0,tomato_seen=0,
                           tomato_water_requests=0,tomato_harvest_requests=0,tomato_units_harvest_requested=0,
                           extension_errors=0)
    action=_ALT_PARENT(observation,configuration)
    try:
        mode=state['mode']
        if mode!='Original':
            farm=observation['farms'][seat];private=observation['private']
            site=farm['tiles'][4][2]
            if step==6:_ALT_REPORT['temporary_crop_seen']=int(isinstance(site,dict) and site.get('crop')=='WHEAT')
            if step==54:
                _ALT_REPORT['temporary_crop_harvested']=int(private['inventories'][1].get('WHEAT',0))
            if step==55:_ALT_REPORT['restored_pasture_seen']=int(isinstance(site,dict) and site.get('kind')=='PASTURE')
            if step==57 and len(farm['hands'])>=1:
                if tuple(farm['hands'][0])==(4,4) and action.get('hands',[[]])[0]==['DROP']:
                    n=int(private['inventories'][1].get('WHEAT',0))
                    action=_alt_sell_extra(action,'WHEAT',n)
                    _ALT_REPORT['delivered_extra_wheat']=n
            if mode=='TomatoInsteadOfCow':
                tomato=farm['tiles'][4][4]
                if isinstance(tomato,dict) and tomato.get('crop')=='TOMATO' and tomato.get('planted_day')==0:
                    _ALT_REPORT['tomato_seen']=1
                    units=[list(action.get('farmer') or ['PASS'])]+[list(c) for c in action.get('hands',[])]
                    positions=[tuple(farm['farmer'])]+[tuple(p) for p in farm['hands']]
                    watered=bool(tomato.get('watered_today'));yield_left=int(tomato.get('yield_units',0))
                    for actor,pos in enumerate(positions):
                        if pos!=(4,4) or actor>=len(units):continue
                        if units[actor][0] not in ('FEED','CARE','COLLECT_FERTILIZER','HARVEST','WATER','PASS'):continue
                        if not watered:
                            units[actor]=['WATER'];watered=True
                            _ALT_REPORT['tomato_water_requests']+=1
                        elif yield_left>0:
                            units[actor]=['HARVEST']
                            _ALT_REPORT['tomato_harvest_requests']+=1
                            _ALT_REPORT['tomato_units_harvest_requested']+=yield_left
                            yield_left=0
                        else:units[actor]=['PASS']
                    action=dict(action,farmer=units[0],hands=units[1:])
                # Tomatoes are cash produce, never a feed or route input. Sell
                # only observed shed stock beyond any parent's existing sale.
                stock=int(private['shed'].get('TOMATO',0))
                scheduled=sum(int(o[2]) for o in action.get('market',[]) if len(o)>=3 and o[:2]==['SELL','TOMATO'])
                action=_alt_sell_extra(action,'TOMATO',max(0,stock-scheduled))
    except Exception:
        _ALT_REPORT['extension_errors']+=1
    state['step']=step
    return action
agent.telemetry=_ALT_REPORT
agent=globals().pop('agent')

# Final effective-queue closure.  Late overlays can add requests after the
# chassis' stock clamp.  Canonicalize only non-buyable cash-product sales, keep
# every market index in place, then move an existing executable sale into an
# earlier no-op slot.  Worker actions and fixed-price orders are untouched.
_EQ_ITEMS = frozenset((
    "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL",
))
_EQ_REPORT = {
    "changed_turns": 0,
    "zeroed_orders": 0,
    "pulled_orders": 0,
    "pulled_slots": 0,
    "errors": 0,
}


def _eq_standard(configuration):
    if configuration is None:
        return True
    getter = configuration.get if hasattr(configuration, "get") else None
    if getter is None:
        return True
    return all(getter(key, expected) == expected for key, expected in (
        ("boardSize", 10),
        ("turnsPerDay", 24),
        ("shedCapacity", 100),
        ("maxMarketOrdersPerTurn", 10),
    ))


def _eq_close(observation, action):
    if not isinstance(action, dict):
        return action
    market = action.get("market") or []
    if len(market) < 2:
        return action

    projected = dict(projected_shed(action, FarmView(observation)))
    remaining = {item: max(0, int(projected.get(item, 0))) for item in _EQ_ITEMS}
    revised = []
    zeroed = 0

    # This is the engine-equivalent executable quantity for cash products.
    # WHEAT/FERTILIZER and every fixed-price order remain byte-for-byte fixed.
    for raw in market:
        order = list(raw) if isinstance(raw, (list, tuple)) else raw
        if (isinstance(order, list) and len(order) >= 3 and
                order[0] == "SELL" and order[1] in _EQ_ITEMS):
            requested = max(0, int(order[2]))
            quantity = min(requested, remaining[order[1]])
            remaining[order[1]] -= quantity
            if quantity <= 0:
                revised.append([])
                zeroed += 1
            else:
                # Preserve the requested amount.  The engine will execute
                # exactly ``quantity``; keeping the raw request minimizes the
                # delta from the proven parent policy.
                revised.append(order)
        else:
            revised.append(order)

    # Stable hole filling: only a positive cash sale moves, all fixed orders
    # retain their original indices, and the list length is invariant.
    holes = []
    pulled = 0
    distance = 0
    for index, order in enumerate(revised):
        if not order:
            holes.append(index)
            continue
        movable = (
            isinstance(order, list) and len(order) >= 3 and
            order[0] == "SELL" and order[1] in _EQ_ITEMS and int(order[2]) > 0
        )
        if not movable or not holes:
            continue
        target = holes.pop(0)
        revised[target] = order
        revised[index] = []
        holes.append(index)
        pulled += 1
        distance += index - target

    if revised == market:
        return action
    _EQ_REPORT["changed_turns"] += 1
    _EQ_REPORT["zeroed_orders"] += zeroed
    _EQ_REPORT["pulled_orders"] += pulled
    _EQ_REPORT["pulled_slots"] += distance
    return dict(action, market=revised)


_EQ_PARENT = agent
del agent


def agent(observation, configuration=None):
    if int(observation.get("step", 0)) == 0:
        for key in _EQ_REPORT:
            _EQ_REPORT[key] = 0
    action = _EQ_PARENT(observation, configuration)
    try:
        if _eq_standard(configuration):
            action = _eq_close(observation, action)
    except Exception:
        _EQ_REPORT["errors"] += 1
    return action


agent.telemetry = _EQ_REPORT
agent = globals().pop("agent")

# V53 / Yummers integration notice, 2026-09-20:
# - Base: The 2945 Farm v9/4 lineage.
# - EarlyCycle temporary wheat opening from Dmitrii Gluzdov's Smaller Market Shock.
# - Final effective-queue closure from Farming Score V2.
# - Older V47 clone/shop-herd wrappers are not duplicated because this chassis
#   already contains newer RACEPX / ORDERPRI2 / HERD2 / COWSWAP stateful layers.
