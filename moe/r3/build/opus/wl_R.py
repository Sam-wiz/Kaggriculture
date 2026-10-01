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



_V92_P_BLOB = 'c-ri}TdyqLdLA@RHL9w+x@XUxJrCc(dvEW(ZSQ!;PKXl3#k%1V{s1?K<OYZk_C-L*vf@AxkriZuOm^ZRgp`Yj<OW3uK?o9eL<)jjfrNw<gh0jt5s-i%!23MUJF2UD_B^b$zHcpK&-G39*Iiv*HEJB*@gAP{d4C*!HT<PmV=OtQABXAdIDAoREDy0v5pQZLHHWc=9LiKfy^q5#)G_1~@{PUbq2%Ezml(!Xs4?Vd-=-nu6yv%NxwCU(4XN0fF;)BP!WeVir<&4~_`_&dupiocJ0Yf&R(8i2bI8LGQb@y)?Ds<sF-ALJZK)+>`|EKL`xX95ND*J{N+?4bYT9*a6GI=OwR9+<8*!Rl-ELE}H73*$?MEAHU`b_Ve_;%1g)5}>&N?L7)1Z05T7oMNcG^v@I&zl|$=>AEU|*zI(wBC!b%*^X#Dl%x1v~#52SW^emfJ9eeE2QzZ|jYpeWJe;dU33${cTsc_6|mmTKCkL*LaS{9lz~xzV);<yhM9k?|AFu6+3>VjvwPtL$TIn9*ow7*8d!kh<`Q|)^o|uC>Vi?5lDLAT0>XuNV4ZB)~$SQ`>kD}YKXc}dK|z|*b`+R4LnG(#&gi@hc+@9*W7YIYDwdOVX|(^J=$QcuAB~b@OBmJfQPb)Wi7Nzbr=o1lwCJwn?wQQW7omgo781{#R(OCW=%zV5@%W7;3^LR4aW^*>SD6?+A_e@#>MRsV(!oe%*@335ZPV!1pki@<CZ`C>hVZo!JI6fgx2+iL)wLUWzEc`<3if=y~ftwaCqwuk2Gku%_E#J>1~khgl*4*C2k`JnJWR~95qL6GNRjTnbaYzR(N!*F7|;hyenH>kz=0JZRj3c(&hq&ab*)bYAIrfCVSIkI#?42F38drq&-nW!!VC()T9XZmCn(On1-||_{uuj&fMkD<KmbXBbFkTiru^T)UYPn6`~EAz25|1v4hrO;W>6bU+wyKk(%RZSLTekwcA<aH*v`J6uQ2>v1i4%J?_Jvu_IV8wnP*9z2I@sNtv?@%|nmySLk#6WEE`?Z7c??b~IyKaDBU`tqB{ch}9Oh!6pT!%sc!Y<pS1|^|Q5kz_PpItrK1`B6fjyF~3U?8FrIlLLXl9zL?_ytHIv93-Mh@@9gAI-hGoFdDFiZ{z~kA9O@cRX``Jw3{=|LtBJ~pIlB(U9+}e|GkD6@SKXNN#3@|k$RUNKvSo9dyROt?ZMUJtTIV!Fx0|T8E11YFCOWsN_>oANW4|q!)FwKvF_$U#^oq%7gSF2YYh(@KZ$rVMES2Bd1u^v2dsr4Yh%PMrxrzGB3)(~ZHKTrbrv`6%HpPBIdongh2@z}O4r5Z-3_EU9Z?E?6OuX{}Q_ic5jf9hKvQ{ND6Tcm-Rhq>Zb8AHD@WaS{ur0DP(VO(!bckvpR-~PcJ8mhR3g){F4(70$#B~ix)w698;tQ*cSBR8cc+3sk!}ZOs=9T~5@Rwuv2Sc@~whCK2WeX`~gI_5@?CH}6_lHQDAfECrb4frnP@-jY(p9M)u2<E^*Yj9mLE336^botvL?OqDS4dohY~uzakSHa)q*YP&Z7@wBWhxOS)3J&3%8;-c*e%D+ZVge5ez6Y0gH~?J>*PPd_+S`U_C!5y#Nnk-L?iJN+ZoeMrl2r+z-DtEvCB)r@B}OpK2D-IrAWmznK%p9kc4<R+dXVXK#`a-CzQ1%cYB)(7$w|2QTFmKCc3OiXm79|+UbR@qNWo#m#twH5<hXKnDj_j)(IxHY`#W4VD~$|E8V=fC2<@e>zj%(aDTHSyUc~e@n5PN9TqvXw8DL-?MiG;z_+F>K=x6L+xC>u_1u`Knb}_oecQ|nwj>ONHGi@rHkl_0Mr`JVyEOM8N@eL`)&{OTyXPQ%gja)7Sb6t~TXdAkgLYf40ehTWw0cutsFH9GV&iQT@tD*jOq@_j*-%rY(6+mw;}hOgDjlV7TMtGC`jI3>#|;QgN}7P&STH`hjM{_Js$kWjIT$c#Rkj53amO(ciM^xamQ*O7>_Ot-@(8zpIEKWrM%c<LcnpXcn{-g(@Cazt{%qfwH=PmdL%Z8Gdo?X~ocuX<9Oz&Fi%;9Dn7;d>CWRH^n(-9s#^<cf<>Q16F0e9nsA<-rcut;msG6nfZ9DEVoNhegv$dWmP$vcpWf(gZGnCShYG~HXg+bsZ%#I2xO&AU@C#)Ucnks~CENOlCoXu{<tOx8Yi`j}Zchp33Q<`is?YL<Ac$}~h`KD4sY04{_Mb^HJ^y5gW!(F9twn9JV1Fk3A$1xLEID!?n;_SAo_Uu3`70%YOn5~76)A3`GqQv{GM~;GRM;+$!ZKZNFU@om|@?kO^?U8ac9hD<%JUZ9ZP3)33Ln9>iyX01(-Obc4eEVsYqy8tamaq%)YU=)h=5mC@jG3G1)-*_3y{-^JE7($}u)RG|pQc@#Y@Skw#x`UoQKHrBM%>mWHD@A+s6qrw0p+&1gZiY)L%f@*GH`=VCPVO1YC1+fXW69GgYnuGsNj)e%l>VmHuQ8gMGiP_z`=nL*He4W&646w#C++vZx%i;9+6Tz>W7rS7~|q5*aYn@S#Mn1(+rV%XD)|i`baFU!P|ncJ#`wW4MD_1^?_}8fY>^4Mbd(@$Aqe2?KA;xdLniyyUuT)2%4`V)S!z4m;$86((7SkXq{b~y|&yLA!x9D6xc^nnr3r6ZYynZ7{tCC=A$3PZiyYxg$u=vP5pwAqI*JidCqs-{^$yUR)t-Fqf@iS7N$1_7AhbW1xN(wjwJ_~=CIqSBdob)Q*uf9!d&VlF_X(0n;p9%<#_g?Br0H-CiWoNJt>$w++a2M*d+@E7A*zdy@|!bO()7(6QQm4v(-jpKr-}J7QAUtD>hf+pqXrVKF9;>0lPz3K`T#EGa=EaftvPgOXP+VB+@Q}#%yP9WaKuvLp}Ipf20Kp0ll*4(*9_22NTNW4$PZRyEFc(Y3HjwWzBcvaDTxyH<_TZ$?`)}!6HrJSnerzHt21eyk>w*J;xmOIF}szIJQ5iRGG7B1ywGdev1><m<~9xxSDW0VZxBED>|&EM;9MxA6NbssvY)9ZVhR=in`zc6N$e%m{gKOBJd)n0J=0e`^(J)!!)<Chf51Oqiv_vmhVIR)+CE<*aN<T`HthJFxt$5D}b9?u6NkE;Ey^$K-B-^8xs(Z96D4+ASU3sI(6CEw`=HS_-(Cd`|wy&Tv9_M#H)k_Z5_yqLJwYPzB_0HF@`gFf$otr?L=Ns(M10x*F>PRQWxkUo?So`35cU~z?ef8+rp+T-dwF1&q(WM#kDtRkI3%*qbztyIy5E48f-IS4fBH&1~#=l26YoTr!Y6rhaGnx>RHxoY&Ur9J{F%@(1Y-|k<S2E*eC9=Hj(Y;Xm+}RI8Ss*VFqPM4T_{2`Vw4K>C#Q43$@5$Y$792Rl)qCK8<F4LX|pq|My2ZCo3oNdpRf5iD$BYfM+tD`Xuw~9FoI{H!{7>8(CiRM)qwlpx$-C8##qJe(-`fl21WbWQO;;yX1|G(j52(E)e;eU*VIimwb}!b95zi?)6cKkLkTUliUIITc5VS3p|s5{#oVwJXV$ODa)jMKhoOjP9djISJ;&>nAF!yPUVi)bb$xxIC&EeR*DJ+OX42BEowbG^c+s3zJsX>4VLR>u(@f%B1!s4;o44a^qCej;Y>`ZIze7n%tY+Qn>N2}G)gCVii_vL1+@LD<BTW+M5^iTwtyz8U<1szw6;6;@Iu*rC+dsvg~H`%{S~Mz=Hb?~XGOB8M&UwmcWN7eNM}e37Qznds9hgXtrhj}0>#Z*H9_?V`7gX~a2}aOkM(H^7ey31N|s2;VyhNj+gYq+AC?YF$NCQ+YSPl;z;2=(H}pf%F6Z8Xb<GZe)PUbK`2I4O<i|m&6@xB2K(U5$Q79%nsEB(PDxF=|HoG2kA@_9GP!O1?*i`!X5buI^W*0$J3$`0%Syiudr+_|>Kq8z3C#yYY=-V9wXLzV|%SDLYst@Z4OFFl}<7f@tWePiPI@*IaxEO<BaEIBn&41#xYUR&UC9x?*ozl!K`?ZbtbQf0WHJF=nN|+)wa#9YO<#*IO+(nXXt=0SV!2JR{@U6!i5!~DGoKf+qv~sa;=cCuJr5fJ3cCePvvw3ps4vT?jQiG(<caJMT+dJS8#ILRZ_X!<C^qw;k2<zF@hp`}5nRBrjG)H05FTJXVuFX=(qdb2$oHmaiutsW!dE8C0@AwfD%TzpQq5K%T3U4L7BA8y?Xp;xt${rmNtRb1Z7FI}xXW6EmElImbM|VKaZmwHwab3Z0_nm*c8W4l96L2G&9M~A`Bka<Vw~i~g?0as-2+H7`U{{!~5f<rTU~zNfzFIa2`t<g|J4||B2gfTtseOkHhsRUjr=CH1>q^A;u^epm=Ka6X2ltR7b`Xjjl<m#g@wbm3_VKMhzwM82J^a?gzc)U<b;VmJf1Z!&oB5bN;OF&yzOCO%vp@FZrx>R6HcLNI$JTG|M)j>@-{-gG*^lq_+uuJOo8m`(OyAJQ`s$B_nJHT3AD68f_;LO=zQ@Ot_wiNl3!P4haWlSo&1)$2nS&R<efl+BekJ%VG}s7_^Hrz{z0tSxd;TfT);^~5KSpHYjI8#%ASiPsBy|wNb4&{A=Be}8Q=%gav7IjFfsRn%atP~*`a={U3gZ(M`t=A-Ztt0LfauWtm;6uIljC1$$LYMrn=$59JUOTRd6+3Z@hyYp^94g%o=nGWed4#dUHMUKi7-8aUNbS1!fYul#SURK0vM8*FZ~69*&P#l)-Z&J;^{;AgS5tkWyAXO4moR8yD5>qiy_O3B0SZ?*jjkn&okgR3IKc7&Zj;Or`>zJb@D(3LQ0BM+ckSeM!87gpgsA+!dDOQ4RB}eAmmA&!MVpHY$S!J7S!ptuX%lZO@AF;_*L|NdvrovT=w*d<~L~h=(~VFU_5`=3pf4XXFU61d5<e!e7fapoX2bNdc5G{ryI_X=+A$$IHH3o%}3Jmnvc(k<#;@vo)cSBA2&W-YXAHcm%dHUjO;x6FJAfNg#O81ed;>P<7X!<#|}$FBB-2pTDsKLizD97><86gt?t;?xT2Nm_{zVNIN~2ikgCM#N1;Bz{as2NZUMr&hEE@EeMG-9<K6d2M!B1)_c0z;`ZO=`>5v!><c4_&mAK`-avtuJZ*2GBE~NXAcMlNQ{R5i6VgTxJAB6IV_w)9f@9qftpn9@m91n7|hvVK3f5*05;;V3c$mJn_&yL)u;xUW%?ffV7B=M<<2$-+$gLYRSXbXbAk(l@IABeWG7XHofH{$dQ3Y+lnhEc9NOyw!+HAvG!j5U@imG4|LCZYgdVM7iA`7lzc*DnzHsRssL_X_p#wF?vB<n^lkgiwxM)j5c$nt8K};fiMYuwR^(97JMzLLK84kaHmdIaciz7f(8vcFgATf1__zE%}Lox+{<BG4@(&OA;KY?tC|t2X?~4+y>KH&aR18X|wf?QnddN%6D%3Cj+&so7P2zPiIGd#-{dI>T14tLuwG$aCIYevA?QeJH1K%@p}(MH`u}5qN4;(kHSCWgr6?JhG1buCC)T7FO~js6~+u)Y5C`EwM-?}d9@tk&|#g}uw%?isXa%s<lzSJ&AW#<VQwM)QAr$tR^6w#4L?O7J9UHn-Mvs{=?5hMgR=^8%HOjYc|~YgYPhp|tz~{?e{16A*_k}WI*Z@#C228+I=>S7<Cx_EvDCF-3fu)1u>4v{M*NHXfyXl2aipBo{C(aRS&B&0U^6B_LwcyJJhIEXn=CX2Gud+gFMVk25Nm$~mLdY2eFfMjVuwTQa_&n~G_xBS)f@A^V`zFveaTa1M6lpn1P%vN);N9bS5xegLU#<*S-%wq9Xp;`8LLZq(!o{iYhic~a0JA|6B1&D+nPE**f9~NuM8*-rn%=eE@E;L@$&-69ixnC4m2V<h##VPI5;6-nfeLWUzw!hS6#M)NWtkV0LUGlBJ6N}Aa*G4|EkT%?kd*raXth855R#5?A&2ePDl!aAT$GI>T<f_x@NwbBr7t%hS;wO1uRUeSpk<g6m8o~$coI#()0yTpJ_!(K$A$OOyy2StOc;W8HkaI`a1E=D@_imp?hR(AUlYlWIMBTuGzzPlZ3%kE|_FF5~1uTtIBLOB{C&m(;fsdSLWGJK6L!~mYYUZ<42~iD&?uO!N<4y3ijFvaQTWrl!-XDVG^1RV53ZoRTNN<kfJ<hM+h<(&%||EGsh)oB1&*^UWC0@{UZ2zPZawQlt3dDWUGD{h~ZPFRw0THW*gd*{<gzNZ2f%wYJmOC6Ugi<Ow;KiOl=@Q4G1kjV}v9bpGx@HI~EPrYdQm><!S8@Gy*J@q@Gu6B1uw1o-yyI?{TAEurq92Na^U)F`uK(sYeAn=iq4^8My$wl#)3p%OOpfMMn_WuB8|;s}2`n&S0DYWHiltPamNej14ztEgXrHz6vtvzlveo@L|dEVKh;T<8$j)Qw&(g8W!n8D_~BBQ&`vn%k@oT!v5*-Cz1SD#$3LO^fXMMuk0hCR}WE1zU2otne0z_L8hMNuWtke0e)+H%acn>Qnm-$=i*pLJ5u&c85|DG2-0e|gEpTIi6C@loF<I<_RbT{SG3Mohg>{W5l8ISb`ej%%-Ix3%{x1D$1_(<T)?p0;@0+Nx&!zlp^-{ngb*e+2EuUlfcHD7sd>7A_?Qkn`R{+~EQd_SfkYwwx-5spEQflU<uER?95NT-;}nMucRxawp@0!GWqt4<iy=6`(|)eBh8eY-Pf^P<66ia`62i&KY_KbL4qQGG3Y?@hTt+R|)0~EKmeU~gtnJIgF$X;n$2KQ4^rs08gAy99nRv6vW)MC*Z(OatZV3&;Qwa?qGQh6XavB;sdGo39o4*yipEtdS(qskljW`B88BmH4FL~tLToWaHK%>$gY75p+k8SzNc6uBwwURbMX~>w@p(-sGiL|kVwlcjhnJJ7c^TJ&KrrpGEfqn|eaVA7iX`7UlT=tl0*hC5qJf%JHE;cf2rfV&d&XN4RXZtCZnImjAA*L$fn^?@lmTA1ue$kAc=a65-)E56Z(WJFmsVl&{C8+x*Dhqg&z3AvcBr;NqQA#SC(en>^p-A9^ZW5IrO}%E6C`{CfJ(;@v(uuM^#9>FXw`uxQp~$ENIX;xTdu-u=QL^E~f&G1l`FGdcvE`oWXeIybJ}^BJz+)V--E%`fF?FdweBh%LDeSUvp>x{u`r!?>!Op+MgkBw0`)21dN!C{GAAmWm2P*pmNJ{usd_Wdu{+@PA;PCJwe;9P8uk#<;<D0b-(rsDM1jOHvzZAR7#Px~U2_l0=IYYQ$7HE+7;w<0)D@XPJJ8&?RTkJoyk*T1nM;TZczYMkq<7UX#F$oMiz55=(mA6ReNyCovvxfzLb*+r~nCB*Bpt;x1yTaMa%sLp(o?ef%NgJj8;K1$PZpUn$?Etj^%G(A#x@PV~1msj+S;~2kl%#8>+m$t+g^2Zs%xojF+(5w|@MaP$+1`)JiN|HDemin%I^_a<IW6U$3$<}O;P@JM?}6~72+%oK5vh`%@&`$g{%haj)-nCyB`uL|hLd#Rvz?7p4YsFA^>#&(a|fv7E^YzqRnq$joz7)lk*H%(*?4+OS`r$Sfx2Rctb^>?z({Pd9S`XWo)@FEJ(_$3S`IA<xaSTwtBZ-*CF7iK!@Us=@0jY4XmoMk7_~1^>z09BveOqtX3%s@70Ib_Z$w-fULl%6%vDe{LFoz%YXETSM)yeSpgiY(3NNocRCgqRncWTs5xdu6h<b!h{yG~YYMb`3U!5f<c>D=GNW`|se729-zS^NP2d;*X*wZ{D0kHd@I(L59-xDHn_7>hkF@x_e?+Nba)0<SZ6TVa?#X$-_B}QlB1$HhR8`tTFHcuFiv7z~XMCuxM#W48Oq+1RROi(6){wRv@Bt#@{0|(qCksDFidY-q7R;AuyB~YRNDwKOA<6gPD)D2xb`6hqKj+Z!ydj)n(K;#Gc7?}_h3G?n4Z;dx8%7cazaQ&Y><Oqm3B(v>^KXs#(%&6Y4y*J_5ylx*8jx8)Y5RPFJK4lwoqwWIXn5d7GUBnHvagK3Xr@@nol&vqqF>#T3dO(uTJMVeCo^p;A<<pcocf->I=)EQ382?5%OF&sxS1>6DdaPDCHxFcsq4sIKaz(U&c?`aV%0@D$=ZtwQGFNFPAImV0Lq7bo$9?Gw+J#^Fj`To3t_ifME0YPjTkc4vrT!G;9(oi)FHDCxY_X$X*}B?<HT|zh*}q|i0J8I#guV|<wEzNrZO^oqTM@65jOYZpU6E5|=ipaaD#*l)f($gjJ+x^6rnYRE37$GLDnrlnM`o#7cWpB}EQij7XODaUnqhW4bt6&!CTDsiyYzh+JAPFY5`#bp16yajf#BL=nSp(wmL&QjB;wS#`Y%5u*MDZmdn&2rkt-r`<-~4ImkV>oQTLQX;tDw*rNP9UEM?)7C}&J5%`Ks6s$1xxPq&(u5Qm&t<ist>CenfzMXBHNPYm76h=MeZLNPxlZlXhB%3>#}&MU#0E$$np8OEf1O?apVrfjaL+-d_cp%GWM1YpT@eY#D)Z`f716=Sa7K1F!4@r=yM_3$})PQHqqP4yR_o=Q&qhw$5Mk7IYdagvka63I!uel)F+FNB$;yr$f@EbkDvkim{bsZ5I%R>SFe+H{NOnZ_}1L!&zJ2#e-j&+FtxUS?9Fywa<XV|S!&>=-%`^;XPM-jTyXvMNv0oJk90;|#9jGg%Yc4o>YaaG`iCcHp~)KR^q!^p)V*!I3k!5A2-eY$S3{YQ-cWRN8Bn=@yuogpLs{q5tIIDVv(n?93$BF*S+Y-t<1}mGtQ;_KI9`cUYvi&y5H21?|KI(dWG|7QA?$+RxRE*dp-0_Ao5nQ80h2Kc?zXuLif6JO=fc017+wm;>5*FjdB|hg9YIj;D-4yjkQXxc-Fe37lg8kw*i*>l44;fy1O+F@KS&#DuM;?58mG@S`Z<ZWnA<mIIsW=#aD9&TM{#8@@8CzUtsxgnB^Vj88G<WJwl6m8Bg$$@M-^^72f$z?(nbp+N;*(u-6R>K}}Y(ojHXOLhOCqNck!BH@D!B{*{(cS!Vw-z$+z&o=H_MRF1y%T%!}5-FvGe}e)}>#6Wkyf5#b<s?p8`eqVOyOb+aTGfDNbxrwba+g7Cm&#EhOXp79Qdl3Dtw9<MT&ro&Y|f^nRzmTxC=nl^ssisIcm^^8e5QQS#zml@nXm|$1bIT?x)F&5iEAi==t!gM7Hi;dU6>SzVbi1Axg9RWhl)w*K>S*|7A}fVZa6{U=AofG_|!lU1^j?i_%%TiohxfPby~z|CHqM941Ke+I8!FhDR`U8ahj}j*<KR_qdj<71&+If@SlPx&I9OSTK?81uMPCXfpRuR>g*L+joefeU+Me=YED5ZnaME*8JLH7ginfnV`8Q!RQgO%*q(Dgip&iSxN^3?nC90GBW%|bn_TL-XE>9L^T~ka@aVtDqH^eqr|Och!S;^`$3gN`P;5e+ex-<Si;RkP_Yn#%W;0QRCHecT3s(0vU=gr~OA=0vzx^*>t=wIrK7KFd?o!h7)1jtRX6A$URqHT;oaf+zPIpdn&=k58ZUbs_MLZy8o{+!kvNlJakuz1UZ$bB2l`F@96FeR3MpQ8Cal0ce!7G%wm_NH7_YcDd>2aRw{(2>@8MTFBXJ^xp;`ZVsg1$yJn8j2YsHvrkni_UXyyk_nCY(!LC$eu#*8@Y3E$VKmpbd{yGa3L3z0B_Nq%Jl*(#6PEL*@$+Na5d+Q)6(hC`YWVIUgD8<oXuov(4zjaGhe90wPe~O77zaX=+ol2rZ5cKs3&(mh>#fNfW2-8bZHmSU2A03zPRupQ`Q_GsXOZ4mEwe=j#2nr@#1(5jH4S;7V*7^H;|yyj89~kta(b7)gLvoswL>7)1E$mK)rHwxM(J2iFX@#990~s2@Ub1UII9s6&x=#)Tt1td;g`I^}PmJHmw^gN}f&bRO8-3=o<}{sy>A>CsMD6RRYRUrU)2YBf`}AkscizZ@LS1)+J{=u?1F?-2tc7m-hyj$op~6?VOt8rmXH_#1xyWm}Rv7sfz|5M47TuQ<7$mPF@!8H1{QIa-uET9jFo!dN3`7Uj{LtWTSh-6po7qnv8QrIJ(mvYcWdI5<~aY%moWn2Pyw@lb5d++}*xotc?#V^Tk+2_v?SwpZqK?)(^LqqS0yIZ9*pg3Pp*F}c^Sfo@&sh=EHkLmj8XK8f<!rCVHBms!#+x~MHPro07u+BG@jQoFK(LEOGqNpziVZ+b*{jvYE)R*jkalz)ZH+C-d{SrkU`XT{X8w(MI5$`azsU7tqo>1ECUX}Dt_1)^C82R<Fc*6AsssrjKWz0-7SdpPy}PiglFMW?lY{0$eKHqU=_5n<8b75##(mWw9uWIX5%Z7b4aX2$tVZ>~#V1@Q)JnLn9apsM3AP$BNcqJoQz_QPImiB18>OSvJ5P0=jbO?F=MNN&xD%cAcq&?EzxKY}VsY<q{!$Y2<Gd<D=J;+@tiGm33L9T{%I@-5=2jsl$0+HL7N>ntuMvDqXLyJk#Gh1<#^s|Wxy@)~DaLA}FQlPF`M|Bw)Q9h#^JNt=D)?K0xyg{(M}9QnWYDMu+?9HsT6A$mMMeH)oJEG8IsPGoMK#=(JAnP~xs?cg~;(84B~nUy0`=&P`iu0T3eq4yHW(I1V#G(OS&{iVL|TE~avR1Hc(%If<-jGuMC`aTc8{=2&4Z42nxJ&2b9m;|6+-$r18EV3!JjoO>o<q_Mek4BV2f&T94n(KQf7R+a3VmBE<#SDt^%#rC45FZ5@C6aeV--;Owr8`ZubC(a=HfmJ}_QMd8cI^wpGH2z1$ZIhyUx$CkZI>TIw$?8=Fb4)SyK(?V4zTbCzV7KtLtpm@4S~{V=YvshLb(cMAn0ZnV3dwHqRnsUn6rSOxAhSsy@S9{NG~!CkQ}4EnfV0SjIb(J<W1YtpVOh;WYt2nJxs(Q!&x%8H?}z0D3G*}J(ZGxq_vo+HLMt3#U9_OEKqdnTiG3vgxT3K^q`CHaauv;4ooyak-62upP)ps8hY;6Wh6Vj{!nB_^#4gb_2f2<OhELFlr)rxz=QLP4kHo?!dIJ<lf7r^v1KQKCC(X{dI<*x0{HBv##_9J>8D>NNbkd`&c0>naKYx-@&fV#+BcUv%H>hD8L039i>P+bS)tuPf5o`a^w2qATWd%UN35NBHU_!DSXrn=U8z}7sathw#$0U(<1hWKv~$LnYRimbc!v-2==5mHTM)JXz-mxO3!t$%jz<TGD!uq=!#b*7RTA`eQC?<}LQ+~n>=1`1s>+m^!4WZh_l@k5BmF?_zxGahlDC*uI?Ciu5_RTh^pL=b{NKD6qyINBVH2~7PiJdk{>l4I*qIpaV<zk*?$MCrM@`t2y%>@rOCK{~yP2r8um}x3r~-4%)3$R28-4z-pSeiYIC}MV3z#Zk6r8;MV)E7}ic&D?PITLNsN?+Y*?V0c8_RJsL~=a5(hT+~_BvPGbI#ltuc=@PXXj~=w0`?X*6;YV^;;%)rpgwRqpn*NJz2(6cY-O-2Jq7Q&2GXu;+gZVYgU}5Uhh-S@$K%eQ)~}v!kN2{#T6(ba|`<+xu(_L%CvRY%~6Nw$&A~i=0V&Mw?)qS$@803P>#hanC9W>ib1CI@d_<hJGMO9%wh%3MtT-KO&&e<2=QFW3mdY>VwE!$j#WD1(E~GwPV+Hz+RRtsWFdc}LZ_N1D@|n4=gRRBMF@StaP`7o4$Mp{#dJ!g%aI*Cdb<6@M(nSAdzBwoy%z%e(8`aDo>II%uKd_tsQehT0(R38g*CRyk9lmkm2R&5xG4Kr!J4X)al0LIe4j7-csrMUTt7x$ajPwlYCisS{0VdXq<MD@VP)cdkL%ZCmlO3}ZB8&7*^W%6d`A{oV)_SiIjvKWjGH!yL=TOALGxa+4A3yqp|n(J=#zC3oPmZyr;)s$NY=2q4`U@qPxfAbIq76?48(*6uwzmp(zlTl3!dmn7;_O2)j)zu-Kt3?5n}ic*{aIxSD>_MhH<_K3S=K2l=VqGB{xjE)?#RJjpV>oHGmf%^z6*Q8`N5nUBE2h5B1N{4KPCFGZSM5`Z+in&7X^ZHHg|muMIGg8!%ul<`+GE&}65IosHRZOBXN`zS1n2aTYUu3WzLnYbuMN`ulkD8c$w*GAy#-vnp`Rk9ov#<nuIn*xt&cPjKvD^!li7Pu}_ddi?WVYHwK8Y;KzriQS?x4N;OkvnF~rt^<N3k#)he$mNedV^<9_Q{7>SYd%DEd;Za{KelZF&na%(9*ExENv`$M5b%8UCiad%G`Yqb^`+Z|j(OLW753t-!!dE>E;84IK7uuKuv6Oi>6&#VCUWQ0=t*CwCy?#@q~(tA1mqy%5j0xkntlP;eN`wpXjvqsP6CpU;5#z#6-&!8-|2$-D_%vRA5k`;5ON9t7;$vg1_oSW8439t<B;5&jKz;^<#@<;!PpOo_uB{{QJ<7YWgEqtWV`+-;C8~@2koH%5Fj((OGW@4&3h$3AyZ2zza3tZeGbO}Wi=!qdLk^uA9;O<E-ZCqUQH6NK`9tfFbaFdQsm0cuCOvmGB(|T?B`e^HM?gXM!#6li-_MDqq2)^fc_a$qY?1^TUj#x+bqjpvVi>UJ4J+eackF#wUi`)b}jKz>J4$h^vtj24977441EQF>GpBj$*~U`#;bRv7DQ;3JW`&+0hs*<DQx<-G$9q_;Buj(hNYtNo6yLd@W~^@F`iy?>f^C|h-ZcPX=y%<7r?rp3wGBXgA|Jv#@H@JX`%)kgCq07rp)Hjw+x%14Id(AQIMdhHqb2up(DYn<8$btP%bD$r6(=%^q)G^PfJa!j{j-+i;D?+5B>G>gjLN9TO57vzkq6tN!sOULUp(jJ+Yg^Tj-BUA{t_No0R!9Y%Ag3V?k=zpa6DB+baP8XRxHoJEiJ-AGehv@g8*@2ShSi7==tH%({#LNn_vW{3!%F7G9>$ig~IrJy`$jscND25>1gIbqq+^Y1i_e0mkUj&BT1*8dM{}$y=ff3O*yja@1HlXvQmTOf1BSJinfm616Is*q_qEXNeEYuq%sdVvO1$8&q2dl9}}rxY6M%=t?7xDzGIJpkhd}NZN5!R^w#T7ZjA}0W1^xk5Rf+W-<Z_Yn3_$2p1Qnn+MDq|LeEw-k2D!dC9$z;|r*eOYRL~<u)Jdk89OcLi`vH2Z>4M;uat2;V|`m*fC!JvCcTmrej5wK5b7kZ_^_4_U8FgVw<B&ZXG^%k<Gsq{&Jk894RyYmRW6H{0IL2X|_YgQY+mgfjWhz#s+44CWlZ)_9uKEO$`CX1}00ZS~6{6h^d+@Msg3WXKdxKpj?bJuOJu@rWshOu+wb99AP%=T1D%L(V#S&^xIXdI7wmzoArBn9jCOa60!Jd({xZmFruW)tYk9+0MA4xUs7i9yn1BO-MY~cD90b-d;*4eO-0iETc2OrxUyoUrIGNsCqSDsEh6GM)q8&B<eLLG{CW%kJtkP>eoGG&s814UUHmUX<y0P+xHwoogw|o#9>@Bklj6Z`V{pv`0kQrUpSM-Hvtf>`I$|QIrm=DnRW=)qwai!s>7(m(kphb+Lr@_Cmf_PI^1@;zx}!km=LeJRttyHeID*k;*B4GJ!sS6sQO)rLX~M{5m7v$JnwlotmcdKETBoc_8N%35L}BPeO|oq<eqOxP3zBI>IqxB1y%r|xjvZSF3&oj3nsr038?}vI)@5+>wkfcJa;TIL*1?V^LnqaQ=}s~R5+#dDNju6z%9N)lH*kkraA$9h+FWBm;@Fp?il<`jigLu3Cy|ay;%o(zoZ@J}wl}jX$|c6VT#anU^AXOsg!ZK+IK?lRhcq9|8`nL#1pE9wH9niV!Z&m*LT${m4ZBc6XKi<J$4hS-T4!j6Z8K4&ZlSnhYF04kMi<-98N%<~zp21!^9;neu-t_wB0N@BeDW**W4{`H3%1+(54Mawgln<R_A+BPq)Oemw+_@iB|~;Yd~<(45HgFpO}Q6+7{$)&pwiWOI-qiNEAEDGr@e{~rSEf6CYBOPHvreKf@<{OAw+uwW$z}lj!(KPcux$zssbsE*w^ujX{u7$4_U<qS?+h2zT4C>Ca$uk8>$+E4K1n6QA$?_+=bj*X?tK9s*EDnY8bYPdmaRcGL0GBL$+N_yyw-NU7<LwxDZAP#4gOJc-VJ;;)ES=pfQad@u>7e#&z5rZJfR+clU83gXDC`<*V>Rdz1r2%bo)~-1)@)qukyf?(wS~Isbl9i1;(cK4K8=E*<|l!RL>pfIN*Ew+}kFPCw0SmYE|EKeW?m>fX7PN;ZWUA29{qhPY`wRJ(iYTCf<}^gY~XrX3|@cUaf`@87QCJHS)+oZ?GdOFdQ=%r(9)3O#yFvyTYsd9s>Hw|%(Qi)j^Rujw}%*Q5Gyt^s$h0UzUfZY94aDBa2mnsv2ZBwmhQHWWQ@^GsZNBm}0#^`_4rm;M*tqn>Uh$<_n%#Rle*tii~YryB(%FI3XSIBfCl@TiQgO-0sjUR2NBrd<!PN+R#q0~4x{JF{|)b0Au#2KSefv@C6Rp|nbov1x?MLb>(I8cCL_$SH7x4M=!)6KX3Fw%As4-O$V2%n@BweO#7Z+aOL8>=~iRUJLxh0NdY0a#bJe&jqf-Q1|q#X6M$+bj|IVcQ>sO`v8^4o(wKzPwAu@GARyyo=I=e^W$*LuS;v>lJs82S4>P?sFOCOs8X`45|lUvje3Ro1gB($>W@dHK8CGHdZg#MNq4~>)PV*tenA$L6__j2*It7@xyr*V8>-I`Rm@K^B^i!hjfv9?6}p$2zusCiF>2b<LgV0hbWW}T{;)Y+ArpdDyi&Ugny!+H0xD$*mr_Yj_C}nxM58029WCq0?TT8*;;0y57Krw>`YuhWw}n?Nha<N@QhMH%;A*&nvi0B>EfGnPcqk^lts%v*MC&n$3gkh5+NQ%W``o{znXq%8`yO!pvQ6bMlpP~b)|ficB&x)LZ5q66SEdJB4)CpSP2CyNn#N)#ao141%AhTk;U0Zoj-F_|ZsB{1W~fVDw>J}`-EN!K*iUKBg~1U70q9T9yc+6Q0$QaatQaLO5zVa;64+H~#0C-jPlY~uoC#H20B92C>tKc<3r0D+P7jR<M*`Z4p;(ck45nG^sA42XgG&zzjF@3~DV>AqC`Albg^0X9bpPB1rlxv<ripAw<sP<rneJE%`wm*?o}9ztE<VtB`|e)BbTYYOFH1j5{wsU-?=y=ms<5Vw{SHJW9;#p_=no5UaSDPt^&o+xUkhAWj*OY~V=6M~Y1Kz=S5g&<`6AKMnxq%Q6^;dF>*t39<^WCWRPJ%RHFbyY-w~O~b8NCqz`Md6`QC#~ZYVKd#=QCquNC|carl~`k6|YLVa!P;@tuoV^hm*?=x#u-#4t57gh>;X<fhmn>JkMsCG?cP>aZp`5fSXp2>UaQW)lc-X=IcY38VJgk;H^6N9tgAx67_d<MM^k8>s`a{3bapcD9g5#?u*V0!=JfaMN~xZ?_UhXNzr3J4dTxZ_OY<(^q7%E4n6RHHa_(iYllkxkXl+8*!C<u{;gzLObdNTY9~LwWFSN#re(Zv_yv&JR>u#{152dl<so0O%-}!<!OKXeVKRc;NbzTtkvC7unnZ$*(??9Bg>e-8IM*Wqs*F=U_NpSZi+41>s*@n6&AoMo840OgvTrWrGN)VL|{LBaALuY90DvvkGU>>oIMujBy)R@{BBTt-$S?f!gk1eY`VDb4Rog;prCyo9`cV51dGJH{(GN@mSkL(@O~X93G)xiCFT0t<s@mj!<iwy?wH6bf=JJ0^|~WeqPs`rBqN!nq+HDzt<0EDvCPf@T%;$Vw(HA5p^M;kFyM7-%;N~=p3s%7v(Nt9rwFcoS7o}!4`VDTSF|}^ne3|kvIZPd^%3TUd-aaoA%31(epzyktA)uoPeVH0$3`g(v!5Ao+WSk3OOB4zJ0k41#2QgXpcy5dAdbo;?fV>9R~xV{o&f8PNwChgvCM-Vi1sKmypGfiS!7zG?3m$o&Szr%ymqgmOu-ZENZ}r+v{>@cr;V_6Np_(6P-VZdIL2j8EQy0%?{IjUGE`~xE%IQqsIu(MD%KVi5mt_<{7~i$ulcWdp4T!+GCrLg+s!m1p4GNw8i`7C5Xfoxv|*Fg?|kY|-(%=~Vb)9cd7K_Od^Gf)9*-Pn6y7)F?kE?ceczO?W4DmneLlx9KkMj#n7;b#(Z2uuJ(Pr*AoD3DVH<OPlHS73*;dgXLz#Py8gonT@I=majS`c)kJOmisWH38qz=WZhe-#TFQP<-j=DjHYTH9Ac!C=9$|)^Kp+ZK?qVgnZgL%qqTMy*G{XzvmN_plMLkoOnPhZX*Qn@qAgzesE&5C(FFtfSQhjbs^ul|nm`kf>wW#7$$WeJFn?lK?1C-sf}2hN)F9a{36P}eX)!I~3WwGZZm)pbC5kAoLh7>MJ}bf{PIsH(66JUmx)T_ks|dx-?pk*8!KrxGZRS`CGrb;CM4-bJwmk_IMi(4tbJ!hIm!66Rz=>M3w`bn>i3Y?PY!Tj0Xv-%gE;sW`<JWXDQ%UU<$*j|0*{(v|XHCq|^wTrv7fY0u`tTVC9U8;?<?X810O(g|eM1$_f4mOb(p2Ns4PD-Xw+eCY5&w9<EIOP?#9O8Az-5irdm^o}S+xViSk9pHjsmQAfzTnS!v!c5v>MXn`96aJLT2)oNKJOKc|$Yf&O;|%fI&e~pf4WkCGxbXxJZdwmgQZX+m9eS{xlJUWRUdSysXD%0#Y4>*7D?*Zrm(RnI6%#bI8Fe0#L!8&XS|6d`euQqiLS_fM#+L;8A%$-RdwO7q&AM@S>oAd(?LIe<AdvrujEOKTs_1l=(=JJ+e41zZ>H4)U`?X`X@1kq_^R7*-r9%1!Ix>l^Pl}+urgyE8`{-Q@@Xmyu2CtY|VJm#49^Kv&BCqb8E@ia#$KD<LSNH4p!x!<DU{b+I^C^&?bWlQ)PNQ(?rPdPHsW|-5Yn~KAct~HH_?($}B0I-|`sl7`7Or-x!jWo23`D9f9!vvBo*<XpK)abSK-#5Zb|0Jbek;NTQhbrC8K%H@j_86G)}KKF{z}Bse1x{ssteAUF0Y0d!H?&-f5X8Ff@GE>6jTn$1y<6zEA-<j9Wm$aI1G>@{&e}P<<Ij1AIj{UBOo-AqJ5Fwl;R`6<^r7xDPCKHk8sx`(tXA}TtK91OPay3(e3x-Tvm%8iuF#Q`r42c$+zk>gDYlO0uhx9az}d7X4F9v^g|fcnA&ip#h`ea1F=X>e^=%rcbJ3^sf}Hx_qf$$>4Nis#PjJ9kGGpgHsr%U@oJYS5`IvG>>e7_Z~y>)wfADU<R&M`LR|1A?uolvvAP^egQ(^i++#TTVB+hx<*f1N<BW3MD>f5_BAD*e7j*egBxsJfuO0MqXz-xlkfiP*PIo+F2G199I*_^l-}?|J*&}`<mo?V`C0QaE7tA794`Q5R?FUsxs!$|=XdTI+4wWv^1qw+FJ7=rD$B{95rkd~+5JHoR>%ij{TVi@-j1jvwiQNXkQey)=gS`?ERfg~66}gR0_=vt-xhH-`>f|OVq>2<*QScz+;F`=(T6<c)2Q`;0_h|L>j6_~?Rc><cn$)cxTovRN0Zs$Ht9Akd-i3}B>fms3BbEnBqujh1Ymd7Hg{TJW!zmNK3@2P(fNn46tDRfo<&h=cKWmBCi@Zmtpj*_fdXb0iaze2eu@!k@ZDx2`c%kSC#j|(iS<r1h^FJLe@!=&)d{|-+Xo=T_CBEXiS~nA00`nPT{D3^E6gSW}(F2sJj<rp5Dr~d9DW&td>8-jqEDv4eIfZNW#J$9m!Qr(edcJ6b)BRiqH^aN53)O9^{OQf`Uwf5|wKK0Xqer>F$si`ju;leV*W3ytZ^*?CaAKZrIGCKRm3*s(fG#1j2(it>CXwSs3_$p5t0X2T>Zie=8XIFepu!<a*X&s2srhQ*J+fZw#&owP0}Ic&vU3hNUSq41#asNqJ|19Z?Che@3}LqQUY`f^YrIa|9(UZ2k(3b7JTnV!4=8|zK-$``mMM92*+C=oWGi8+=_^7FQCvKT9ZV!FC*A*>$H+8w?V0Q(k?h1Q*%j^C1I=5zy^TXhF;@f_-Le}*K4Wk81;l3v2vXMEacedMc}<_6l6n-{XP&{D4EQR=0LECR`c^ub3zte&bfO?l<F3%0B)fgNX6-_5s%Z9#Yn~6fP0;sy!aYDJas!|*s>H#9_25azO-j3xeG8KuMIA{{6OzLx@Dqw<#%c;VgNvt4W37lsRN77=61O98x#01sE@lr}EB(rABMlB$L9ztA-%w<$sA<;hLxqMqb`dFI6z+t-y`$#*XOSyL?YjN~(Ir3IP>-Z^t*NETu2dE^Puns{?Poqg>1oY(@<Tx0pz!0D6#Lg9d-*}nRjckKM5u9Mj-1(17?J@<y5W%YG{sHo$bdd8KZv54g`spj6C0rY*(tXC;)t3S`L=lQD{iyH;mBGj4=wA30D@st;|m1}cB&Q()e0`$1LVA9?CzlMbdG4;<%%3d+Hd*uIuK2#Z%0IN+X=V`dWJJ7lOQ@ZS3TsyZ@-tr`+c|Btg4KsJMCkxne-CZ%+ouq=U)g4?kn)(X3IJsPr1EQ_~^~HkK$MRCN|q_);B44VWw2Z<1cTyw9NV;4i`3CdQ+?N4~{$SZr*82Sog2sn(2;v>}QWrqMyGLf5OCE8qPM~ZX$}=t~v&UF<;Py6O~&CiyUle|FHpf9n;xR@}wiO81<i1ydwYH&;dWT$#7<(EDAS7?c25#erDdlnK~>Zq7d#=c5zsjs$$uUOUDjFBw_eR5iC<KqA32;KiZQ$T>;7{bR5i!j8Y}y=1%XRCg4GO&SI1)GJ#2|ib9^oPW~j%oX3s$Q=;H>HKJx#eVWiiiDYP)J`=%hFiZwiWwRCh&TD6r_l)_+tD>w`R+#KD2W2qBgHz%mlkOlTiQS%|sVxeK3Z#d^%)QJtW$SUif1ft3>RPR|_!!%NN79a~h~mIt{^%Od1ACG|X{0w-Hen@?9u2YR?)D;^LTN-5DYj)`tRHUYRNk%NrkNB5%@j@~z563{)Vimi&NCX6<V{UvQnxGA@YS(?S?F4BEUQf7PWA{tN<f@2w(seh43MT9UflX~XDcarQ7k52MR?AONI`-sO1wkmKOpknH5!TyYUhYiC~{GHA)&UmRAcp9SYf{remR%#=k!1z{tn>{+kB@X_{X`t8xeEUmV&0nx?-rGV!N>Za`nJ|$OmrIcDzF{!7W1-kwEE2_c_8S9O2Jos&|?TCfk6>O>oD(=USeY6{{j+>xYKgDhtNAW)>>fRUti`b?}$LD<?-LrG42%6+JwGg$b4Fl72)L6S%{*lhhnk>aQZPAa?SNk|sYKldF0@D9bWJ;uh6^jLKk3<CvTOischUH`wz!1GT3WD?Sh>8>RTdUCXW`6=RmqZ9mh^=JG9X*@+Rr7medr5N^G^Yc~_Qe1M6(CNTe_cWwCADDE%DtB)IZ^rSR~7@pm`BXVBi8o;F7HtuC!DnnM6w`_%`St;a{8;&(s*263IYx07&(DWmEt<SP$|6e{~x3pMZQ-49p_Vb**V$tTsoNYNw(4l8<&Tu+mkHx?3gdR!V3xHd4fZJ>qpTOLh`LsZ~B{A*J^!n_0a(A7U1_#%uB%DuJQ5p=a+)_K`li<FZu&Uj_+7+A~{pH!ZBcMo0#;l|4Wg{1L9EhlB*|?6Gh$rZZO`E5}j^3iq24K*AZo%-=ENa&uea1f#8-Es8G08;bj)|Lgr~y1zfA~tQS|=R(r<7WBu~){$rqt?C9?7(n0{l6q^FIjogmcVq`>Yi9$lo_9h?OC=I~Bwq=crUn;kCZX-9`RG23qEM{UN@}?s0vRQxPmym)Dq2Td%Ju)_#g$M+!+ds53A)dB#S6(Op?-?>7+KIM*<V-i_PG)l0nu&hI*WCp!86{p^Bx%h~#Vf>=?ku$Z~jAIeJ-Szxzmcr1}QC6Bxo=MvfT<ayfk^vqS^PZAe9bLT~&EZzNip-kCLiM)otZ;fKqXL4CW*+u*-<#H8;<EdO;F(^MYxvUh0_m#_qa(R78E`OHUjhp_?r`L-gV>i=F*v<MZ3++-V&L5x@zk-YQJ!J8D@y`#{h*$JxNz^utI4)gTP7aE{zFbs|N$%kF&@Tfw*ZEvK&QFlf#{9bpyZNs@$w2kx65;~>joRn_Yxo&$W=*!aTsb-g7#7ASA~C@G2zIF~dJE7IqDXGtnFiWep>X+`R7!vr#h{Vce+y7L=t0K*oJFcrJvOpPeQ_Y7i1RJG2^Wg!K~R4%sGIFB-~C>ymCeH#;0-p34m0TcJ9yyZ4CUY!kD71;d;zMQY;sY=`2(0c$j$`OCU6EJdT@{-r2Hiob+k@crFIVY`0AN<Np&dT%NZdG=vhhKCpV}c@jHEfYx<P|XBx22$c{oDYXOCFci9;}d_d$GWz$bQ;qPHk*A{JlOj(`aY<mIjtw1E5p4XX`Z;rVN49l+FVVauANZ+y^SN^L{I$?WmYMQeNOl<=O14JV=d%>W2=3Xdzh$Q00%*}1u5`0+d>n5*eE<nGJCNK26*ZF~b&$={o`&NbtSuZ(X4&&I#Q02PP*q<IxTh+Kco4H{5J)gYe2Tk59=7ILyJ&~~6Chx)bDd}#P6t`1TWOYKhp8DR2p-?UTSHoYA(?1d(wz;e@U-Aw0@&}^-_XI20INW8SRDlD_Ku+qONOn&QblMxHG-|c)b>sn#ZG>fSFn79^C@<dga>&ec%{4jF50Y_1pwJpun6A)urCF?zm))!g@Ed?d5QXi5r708jTEPXxP=o0Bo+)D0(b>@TZ}`wmqH;sR-rw?v#3%Ktbs6C9#+>Rx@*U7~wrs1J_R%2=UUrnnw_;pVX&(nVq&=OzUYm=U`VUI*+=jZol)JIQay`>f^CEpCGJzhk5w4$kt(K?KJU49Q^J$)>PmO13p2*{1>6Ywio;jbSa-^2Zp(1NLijqgw=No*jYuWs%1%X&%2H4vyh5+aVbEc;tC2`ft(2Ep-Hlt{gnbN*Y^CTlS)k<gZn2XU@Ry<^-!ou1lAC}`Ox{A-KYyQudxp{9-vD71R(zm427UXotaqC-JwFuWb2T!NfOa)Grv@n`dJVV#k)z4$d8Z{VkCza#YF%~z@6h@6Hd+^f$JI*o8xfNYe_#`AxSHw5#Zmv<C)|CX@3Ctt9&XV{yMH%|6P$Qgo^kShgoidjd{Yr>OVS;0ti-UT(J+Zd2&_QUS_~LA>g9zb@13MR2Uc7N?Ux+`Q98cKBAAy*UTxPmHg@}+3t<C937rgwKm4<b8@wxF%8`rwa-z->#W4pCKxOi06_`GOsIg+&vS;f2?Gg@Q5%VkL_cYH>5RA$-g;otvQ>dK0m-b?Dryriy#<``5v%jDG7w$PQQnVM7uE3C@GW@kw&jl)tr>2+`fuEbxr74r+vCx|4qx^*~+Vp@#?bIrXYh`5pVo&9_hSaTfymr3QqMyOhegX>kS><R?&MAwOw6;011^D#=F8xTAQbex<XdgiBO!o|p(+7#krj!8&Q?oedLth{*a{31O=<OuANXQZ^0UolX6o-_-O3?gz@x-;{%SUoFk6KN@b{k=<2SZ80KZgWxOo<}N!`nViLZD)E#3as<fiWG7uy6hcy5)hOTc`i!9g6xtb$GQ}b<f<~J9@V9&P2=n*Qo^+qrAb-2yx-BcGPtJ{8L_HPF`h8o)~!4y(7Kfav2!3j#u?+V_evGz&K}2qII4m)Gi%6IgynkJc{H%qt3a`ey-)>z_cK@%v+L}UK~dwg)`X1U2(Q73HBm)s^g17!y@Dg#tcjQ&8x*fLg@<QMVQyg?v4?gqSrbqB&`zw0g&Qq0woE|Fdm0qZcD%HPb#eIAJGZ}{tKKB`Eze=a3co(B-jtguVQ<&J^6bodw&u*4UaP#c>Z?6T3Jq!C$=0dc3rjr~FFq5m5q<;#*rjz2S9o`_$hpD?RJc7Z?+6Yk?e%paV;0k0Y;9_VBN#x~=W%(DXxIvCn|R?BJ!pe3_}g8a07xU!rx5D8<xp5-_E48u&<4Nl%lTs7a53AJuX_|DvSmE}O86Ub`UNIyA7Z(8IGW>ha{10RLy?$&#gksF6<@OY!=aI`UlC+l!&Fe`5$9Y7X9Z$dM9CXKn*om<@3_vOo^9jS)!+vIZm!tfeG4io!B{j#q=XtUC(45=aai}<aLN*@BPn_a<vTZSRu+(wVxs?{Eq_iHSX?b0^Jjp%TO-mxlIJMXtlV<Ue*V_+vk;GV<Yp#8B|^U4@w+$Two_gT2TgA_X!)q0{JHnW_}>X^mT$n(1+lZGoU}Pe?0goV-uBw_sYy&P+z;pcHCZ?UvN;(ggBgJnZn#f}BPzePQdidBcck>RaoW?*UL?A`vtfBYKw{t`HuzG-cSxE>8}^LyiEDVRTIED4|JXzh5(I!IH0ifPjzU)Fc}3=w`;Nj0(53VMS~(owp)^>si?7`pH-(1z3YpJKb9$ipGxaJb0zc2HQTTijz)BdCmnG=VESrB5x$I-CKf~E?hVf_`Bbl-z>nIWUzo$32GKCdSaN~gR5hyaEtvZhV5IP0edStZMLA(H=8=Or5a)|X<Dly?jE*82Z%GPO4Mr+0u6v9y+AYEUXTP8-<0JBvx4&(zk2))SF4#$<VGx*lWsx3XVkS~=fJ^|@{MaKxzfTvKLLk$I1kp?^<`lK8ZQ@Qp9ynQBf2I10^E4>9qoA}ov(7i)gk$9{VP%XPxy&wTf(96b--VpLqkHBK6G_~v)nIh+pvnSH!@~`_QV5k55>o$R>oEz6frA%0fS3`52V+&=ltxyHZ%$nJ^WIPl6V??J)9hNr$f}hP~rf*hSYLf3le)8Be4UbHI%*|jPC<~I=)u`7cFoi(yACU`6v<m~Pj%6uzz!q~;C(;Zd*J=-&Zkb=<c>@3^aca;mTG`qeq=Sd?AiODE4fZPnwx#Ave63jtEw1EgBfo@g3uE)Z7q1Wn#{B=d53ap>bzT(__BUt8-#&iW$8>y6Z$0yo-T2lg-`>Z!9)6p^zXv|Pb;X5`>6`hOKH%r|eZH;VO0z%q<0q02Zxi)f`uIris^8p=>RZRY&u`1KAK&Y@zsI$O(<ABQKBjNzV}12UU?99iynkG_Y6vAQzK!qk@#KAc)%(IkJd$+l&8K=zmtVc?>gj7zW!MX3X`&Z@vKU;$EC`sQ@EiT9@k;p(fZ)Ly2-kI<iWm1HR5Gzclo8CT7J}V&`ACD6b1Tv+&w-$!ta7Ysqs=opQx*$i%3lTr5cQW%{=8h4s^3n2B#{GIUMHTw2iczd&_OxNBhiaZEsvbPNsHSpC>f7GQ67Nm;zcj^>t7A8eyI6^g6FH6xT>fYe~p?3eZxz~MU<SF)J9CY=<vmR@AJ55xh`14{B*~@)tlB@r{X+q{G#i)a2Ah{TXkT@tOzk+iE%j3HeAKgx%5w(=YPj%ng6^2^S7<jmIJECSvF}oj`O2=0k+GhEj~tnD4(2u>m&r24wgm|S1Q{GBG4*$fFD=15W$_OR0sWKzSlW=k6>s!j%MVxcGB?(UrE7se(;6Y%Rd>O`$_BDN8jf5ZEh_;z9x?N*+G9jdzQ10-W5+Y=5k9GKYZbY)V7k`gv0R-Yr8Ff^|<Bn!b2VJ`}lc>*5<`Q{ms9cj~rWgJjfv)j_1S@&gRd>kMk8y+L@ki=L;vKRvFq)JA3o|>&Z2T^KVnTY`WOD>2ibTulzC9Eu9b+kGk|?Kc5~vHg!3sl$oJ1Ii9|%WPF&nHXJ_*A^oz4C~Wun(F+u=<&?s;zewR~Lg|We@>@U~z9v7{39P^7IyxYlQ3|5cwhJN~7LakMf^C?q*j0t6iT`l4(oEhOcie4ulW1GPCbsHPb*P(=U0`RHH3A8{HFOHw@9U6PV;a~<Qav@*!#)jB><z<Se8x}~kWsQ;Dk)M5L`<0LhMOnZA%=hE8}3We;SQM`L2DA>ZWk=LmBoggc=4S77UkQ9Ik2B_o%NFQ7DpzGNV4OrNJ@bT_~PLKH{G(hdSWybL77{Go5zO}s$k^4cqdW!YJ9fDtUF`dFjLz8i{EtL%#(}|vF?N(I4$E~X^|#!qzA^wiNydkw<@R6X(z>1n_CGP7@Am!wp;gDKdF+%Ztbu`duV`d?g_K*II%jU1^1d#D;BnEvx-G6(Pt@~&Mo0#f|rK^e118@e)C(LVMinxpRX<3)RygVvTSEM>*$3?xNH#`9tbZ=B*^UM-X%z)W-@)AF)v3Er4N&Wi(XB-C&*}%+2yI(1fA<aDw3+TuS8bzU56b5jniVmDrt|r;GE4^`?z=pYt^~^Q8`=)!L})0g<wx0drgZeel887>H;rD4D+6Y_M`AW`LOMH;#Xn%iipf7(&ndl8WZjq+OL<w!elXY%Bv;1Y$P9TCjd*XotHK`K?o^1Wp%`o)q&zzc=N_lPK=o<IwD%H?2k$YVFHGjPd+54cOiyK<ZI%oO~hKvwD8K`wM+LZk&_$<-?64aYPrQu$|^`DL-n=uIx;BLs4|I;_h2PFni!PlsWia8@GP-mm{`sHn08E_Dk2T-NT0COg`flTZ9@Y@a73WoMWM2#3faA=B?0q*NLc}ZaC4qn6;wdD3m4GwPJg@r$d}Jv0qNg*Z{YC_8N3KBv{~tpV*(p1%I`ux^!hfV6d*Z0gOc$85n45jam8*_9mtc*p2gzG=Gifa9CqW#695&n0VJa2CQ$-_gUA8QBXJ$5A;_YHSWMUjhaq)qAP4Q=#+o!Hk>&M7>tj3PY2XGHoVTJ}G>RaNP{O_ZH<7*KZf0q0pgl?r@@FV@GZPYA24bbhR_$8lH9407Ff3p!6aXudB}pYXBJulOIVO{;_)=U6b*$ph6gxjY<A9q^Ip8J&Zr2MAxGx$9+|)SWtlewcjO!HFAIbsOl`!;SBnO-|@D}iKqR~1IFCjlaM|NW(hmSOHKWa2^C&bf@2JV5N9{c!<SzMn%!1k}j1eYk(fRTNk3@%PfGPo{M#vS?K%FG8RM5HL;2=tD`#l^-77g;N95N75vD_j<3_shg^(TU-3DPn2xv0HG%l?69kX;r(#4F|eS5-b!J8Ak>$#aC4>o~ZVNCkL^^(>pT6P0kRf8i!zrt5A?*pUOKF-bh!c3~})ZhPa<2wE|0Xc|nfal|S+nPaN%&+w29+Ut)_pr;01*RB?dcRlLD{FSEtvPfHc|o6lygy^3zV8B1ZthtF7k{0*(*P!_ul1?6l(b>}#*egny+(r?`UyxdSfr>TkilQn|9{OOG4w?kvgR4WbUYsV+AJB9g}T54MLOp<OUtQkO!jS{_c)wY~A)ypSTmY9WB1T}&XZtnYi(6puFE~^yf35`dkE(N+hYw8B1f;}nW>`Yr;X-zCx_AM3FaCTV~CfB0C-jKz)b6*^Yod5i*u&dWVc@NYPAed|c)jZvXnj8Cb2m0LpiaBIE(+)_wX_K-tiH_NTT?h2*Xq(!~j*vkn!DBtK5^ZJq3^Qr%%z;PnxKR%c0>BQCNP_SZ(+d)R$XdzRswy%)A>~ms5_NTZW%riiB_w&gCq#2#WfasB=#XmG0qkv8Mg^40YqGwWJq5&IhtjDyA0!OCRPlDA@jduF0@Oer@0kdNs<6p63?jx07OGvUN45=E2-qIL%WbltA0T(2#_|DK(JJ!+ZTkNwPjOgha#*Vz_KqV4K<kQSmit(Ds_n~-DU(N8q!5Fk?j_!nB!`tmpqQ-D+odfhoOB&!ZB(XB7O*pef_>lOaN1U4Pm<_uP~qjm{e^NhY+2$Mf^)=I56JgqCN6e+ZbF6n2>1F)f=k+Gk5xCC0$I^>lS&t`t*Y256(jc?f2H$5A!XVIH<VSTDonK=bC9sfj)k2``#@EgdbjqDfs|ypiu~M)r6`3D6C^rLUzI1Lq9sl=gp3|SNyWXBneE5YP3VVCp(jQsimF#;B_+g;nNa9SRIPB$zR(%3iqM&xG>Qr<NdrX}9GcLOt1<n<4`FYT?5(t(x=YnAE|!EX&T1))t$tXYx2ehD1$9%2r!*BS%GCvdUO6Msd&Je$370&GMB-SNGc~%V`k1bXaRD(lt=MgtC{K{vTsOL=^fX=5)Hw8Bq-zqb{w<S?%Z6M{Y|N5IZwej&n%SCPq-&C|;f$_nCoY150wTS#{#V?$LSt+?v#l<2HE~EckLa4xXQ9#i@1Cug^=KB?XVnK-|HqP=>0E<=FVyF6=N_1&5>cE*1zBZX?#M9F#iKJIlU=1AxyF3v#xq_OA-j?Mnfr81ChM6@hC}4Y>70`Z$(Xq@l&R90?FwG`xI4)tQ{JF5XkkLu1xsn0v&9q6V0Kl?yLilmUnCPo6z3V}c;890kFd511w3dfI$05@m5@7Dg3T)HDz(TjCFThv*alDXaq@{a2fH&8JT4#<G005dYEzFyFgelrw>srd`F45m{!;iWvHJr^ajJb-i;7sF`kq$pz<L&}r{{$UIV;m0sa*<v!G#m5avQa&dMIA5I8ftXah_IB$SH8Q!&zyM$sBvh2t0meKqD1p;NUK6N)S{vQo$+|aY%cZ@THa`d4JNdq_#V+S?Hp+8pfEOextjDEK%6``=rcmue%ZG`^vI7iUOseb!ufElr8mT$O=zj)7yD%5$&JlAluM$PAO<8@2>0?sI9=dtOcH<gY*rw2UR>0DoRq+Cq?4no?gQ)vsts%Ef{IWu6m`6XJwy}GvgnBZ6&K8BbjKt5BVWnhj@L@kG5jBV0qq4-9XuRe{Wl)ZO&e_>K?SK_TO|DiYq}dXL00~bOH4KU146}%zSUwf7;xMn2_<NJ&L-)A#)$?gmh0nO6#Qi(BH+ce{%GOe&?bqwE02%r*ombraSGJ*b=<vs)0Q>@Eq6jfOe;%FCo`9-)OopC8pBg)JBcD%JSMK0a%a4=?bW3iwmi4Qxm81cS<>%ot;VhnCBd|MCiVi!ORPWIoRUFyhz%_)ZAhtr})rnw}U*Mu7?i7yy0OyHJaQ8UTcePDC}u*6Dj5Bd<Ex2I&|RqDBLOFI_X>RLD^<3W_6ImHL<8rf*}<bh7|G)|IZIs#YU{wSE*uij`T-sV`p^6^(AdAH*GAPYGdVf+E{%_8{5(Kk(xGknbFvr_kt>xPF1m#=ekJe%$bv-G_PjP>}VpKsbVVmr&{lgIrFkAR-RDB;?t_w=ka>~Z{Jp22GhC4W#;J|;cPakv?|&>gXi+ny*vAMTqnbxxJdIKG56c1+Cnofp@MiPs@IZSL}xNA^Q^L%bAX2N5!I9|EGL!PoUNqy=vnk{U=53u9))HUmw`()DBvR6Vg+T2;wdK)8P?``A}CWY1!ZpNAN9FYMUB|%{fWgmy1z@8>S%FfPDKPB>7gp((vmT@a?stB+$&k}T<}C7D$sjWkKTOF;&jSmL@WD-)^v0NJak3&kd0<;{M1F){?3v-Gv9~tB6+6GnhB~_z9D%gT*A=0F*GZsWs=DhLoRS7A2TB#`l_G=cwOhM5OgJNucAg+TsTz)i%BtEs2|71M;x7iMcKZYsyV*>Vn}7pFqg0^ne5Z5K+-U19Ph&5QWoXQO2k#HJSqIk9)?3uiAXV9sunHOK@OKpPvw-~a4o_L=-uO(C_dMmZ>9J7=(-*oz~YqPRkQm)Y~TS)L^-5P?g`&{anLq8R&q}ySIrWvl9F5#DpD(d6dXk|c1aWE)irsW;4By<^rXc@Gla!jh0qjUFe}uY#9c(^RYWM#)zIM8w!I!EF32#KYH89M9yENR93}w)a1Mf2f99LysBs+71&*3Q?xg+|>@@bgS7)ph@?4XOQ}!j5FWH?dNwF&yW1Q)KT9GtT(>&s(S(2~Q^}9V~q^YwJxjUhw(IzYU3Ny9yn*PzdbnE5=1Rhu&*7VEKRc#yQKs!Q2G?_#+I~L$8fB)zg*uQ5XSJm(9E|0^LiWOEY<7t)Agt*v@mOGJM_>2{g9ON~K3GWzdm{q4?aPLEx7L+2aFpUCl@(ASS4#*yE=uJO@n>Y@s`2xz360e&=<8pE$n(Xld)=1=vQuXwr#m~!@>?ey-Cbs=W<dAUdG6}vg9&u#LJJOAdHA27x#-ZWLrxO(DD5^`^@1oEV7^j?Ejk2e>As<ywg&TEayZ1u{T;Qwx^wjyk^jeGahcvZp03Trg=bLZ^d)tvh!!6Yx`D7@-2a5D^gAi{oVvl?1^c}eZE0=7fhh(7AO!lB$4?*@Y7(o<{zkyZ%pbg&!>xN1&Wx-Do&tC2VXAOoO<8hn5!!AeL?x8r?l>b?>je_k@UJsIpm>k^Sz~q@|e#47Fo{~cnvn6KM186M~-$68((HsE$_cHi(j-yoSpL=}(YMcX5cI`V`GMtVKJ#|+IuUB$i41HDrswx1*;6+#LVBU9(GWCcK)xrgU^#FaIAst{GdX#5p$tgvgfLy@>>q$+BYl0jOTOUqF6{LtzkDa+n3|r-`ho^9nVPI4zI$I8YsL0jMuAHwTdAnJxgG~Zwg-wKkl)?y7b#Sw>8R!cSmmz`_It8f^&dmHvQwKrXBg({38v{)YSkalzC>-dR5>RhwRYIt`XQ*vtsVg8p{)cZ|`Cr(wr^>%30ikv4E{d15cDcq&B6py=vpQA&ncH%P%ZefgR{gD0%^z2rT<2#vGnKipLvlK=GQ+V-K2iIL{(#QUL>ow8_aKnZqgksg7VqMBcmjnLUq)d$f@?>0-K4)zUO+4~oqy*#KPKHkkZvxH!Wy*Z_pV%SXB3uw)y<CD*ASG7vGcP+u>P}8XN<n@d`zdDb2cC8Bf5wa%=ElG1_^cxkf4gC&j`VyDr@tURQ6I`Ov%pYW7jl-aylgy7s$;9O&>QU)e=w@?b|dYHf85=EeiJYnMn8at<S{$%q>^ndm5fm<<{UvbPev5uYc!5Xp^4^BGv0l?1Y*cRo*t1F26W6&LE`F=0R(|@T5MXGS}>AY;%xDh4snCB`6qT97<t_&4{|Rd(tGBTrZ@@j22gR!BnHvLPr|X6TvE6^rse#aAGZ<4u+{$nPK5i=16dd=%ZKI%25^yJ!7y}@Kgw648h}_F?Wg=ff)G+00rUmr7=fzs5DajBlPq0*GJ0#_P2#-N{bpXRftlvx|hCqveTW>R*`sHlW1vQB$b!$ITwn^UXS)g9ZlvpAk$(JRoQ%~fqO(Tkrg)#M-&sSF)0!9vz8gfM3)D=ZA38<f#F<~qNi$=pitOlSW;`djUa=yHaJt=EGCP!VNY-L0?U+kE?Y4#QbUtB7yQQl_mlS?uEV+8{b;DSAhHkF5`D(Nai=q9C;KDx8NBLQs1o<5n;f}PDN-_&4ZV{CD>OXg&S)FY!xj2)#GRQ~Y21?NBp8n4>}&L*&c!hcsR%%2E#$tF^i-lVqw8d31>ID9SRyO6%&Ac#q3%4)*8JdGr|2gzmE&ecTaQ3k5fUwjHDPF(L$?kneJKpu=D3mx*;$O<-ah`fZ)9Yjl#J}HXWq!O-g@}$<695EF_gVAl)W*Oy)l%%F_gVAl)W*OeNe~#9-}8qZ}emi{dtC=EHp=LiASC?WD7sRQx;SMD>@3M`Ga<%cL+*^tpp*l@+rI!ohlIpf)Tyk6oD#Cckac`BfK&}cZ`A0tXqx^DgIFo{<L7u(tCIOGv~(L8w-Xk&%l1n@TCa7o~s_uNz*yOnHLsV(1bnn(f#zNC(I0MIAL^ttL1~V6BYzs3T|+8mTX@kIagXZXVg+TToruc;4*1+=ITmY)#L5F%I<>R>$JDS*^%>3QwsayseKemIA<$kg&h&D9S3D`wf5$Ow(R%_Y552&v88Int!?PEnU(Cwu;$OTpel=xPJ4>HEL~(JJ0H!HpPZf3J}#Kc7PMvA2_sUI8-+gq!kZ4vLC{z2hfC(N&=|p#dHo_!(^Cv$GsD-5gkK?r*AtV4<n&KxzdgQ*kKR1RZuT^{*UW@9b7tl4Nk*+R0<u>TtG(Ff#hd5(&StW+C2ibO9A{4s;uGH<d;8G|As*k%qkK-nmE4jQ(;0Dv{xMx5`3jc~o*fB~?moYH?$H|U+L52`WT4ZNKg`cvHZ6(L%9Gz-yuwr8>PX=()2QDNYg_hS$j3KNb=1j`xr?6TJ6pa2U3ePm`fJ}1WVU$WRlb&|@Uml4s7Oo{XTVw3S!4}p!enR2Y&wO^t{gIpq>&zpkV<lM7R?1Z_7oa>#UyP4Rae&Gg2@)%h&6hrtf((f-Xez=;53$UMBkGm;y|JnqEs_5P}&?)5m73#$Fob^gw{c5gQTN(%oB??Vjg^zSv{Q9P6-`?(loLGL(VMfLaJ4}){c}WJd*%cP`)st#$@A;6;`A2qdcaD<Zo2s0UmJ#znk-<pnURge-xl%V6w{V(fuvw$kF{zq#Ze+V&%z4h?=v~^bty-<fAdDI$Nui+Rzk&#*K*pdB+l#IbXVXB{-*WKw7mx6bP<4j)K*fQk*lAyrL5l(OObcM@6ejvSe34J*VD_hdB$D^1X-&in%Gi7oh!~(ym32RvpF)SL>J~=|yA{sh%k2*lDf=Gofh`_fnVv{v@N~*5MfcGD9yutVHnz=*6c-0D+5fveEcas1K-iH4vZYQi*l)>c+k*w-04~7pI4?i{Z<Ah>S1ETClU>z9B}sgl$PbN~Af4ago3FG@R5==<TjCxhfxjPkhz)?t_XxvZt|*u6H5>2<iiqK06}TOYZ^jH8-zYTSNE3Io|LdxfwSh-<8nq7%6pn7U1B!gd%j6ycF13t%X}B3wG6x93pj%Mafh)gn2il<w=Bdii*bCyc@%{IKoISRh&x)BR2kn&$9Tzg7IF9p8@dtX#HP}UT1k2Uc3H<sp?MGf5-KopI!e%&?vF{2@$}$xz9_1+@yd?m;1*BxGFy{1zO%MgY;2|*XX;#MJW*Svr^#ZB`L68=BS-YfzJ!ZDgRXX>qsQ-eky2{;`K}9Tb4Fqr^3l=Q~0i+k~#C4Z8p_Czz=25?zhLkWty@5JJ2#GSyZ_vUgE)tpLP%7Dx^PrkHpU_I5qq)@BO#Gh{;}T)yd_t^~{G7@0bw{WCelqY(~cfh7|`2N22oIi4}tK1dXH4C5mlmzmWWAZQzU{i(PQ-?Z1D6Nxao+dW$u`eSGWTw`l%bC%-`^-XIfikcr=?N?LqFO}wEd-cS?2-%%6&>oE_Z)MpM}{Pw-!6HfX0TKL2QJ5gVUo#<Mr8-&hxEjm0SD7d0JMuxg9>;&U;K?#4kFR_fw8S~O^x<Y6XaCkw7Fqaui@g&;*7&38=mlzn#O6R4~j!22*9?>OaB9s>Xz8ocg0X1<3$#@KzV5BBIhHxB<x=rVG(dMdhUW6xxWgW7)sM}m1&7X+m91Py6&r1stom5jhA__`)Tww2Ub-GkVfqx1l7|$USPu8Uq2}NtUf1IHas!k`DmF8>qc;d41Tq~92N9G342V**UmJt2vj*oU)icb*^l5{RQ_7YygZ}I5he6?0(Z7#-k*4peYeNrc-R{M?Y7+GM66Qo28k6%xM(djZ+;$lEwrN7c+Ji}>x-{a9w*M7VB?GjE9A7KpQr8mz&CSJfxC};0=c!@JO#LLy)o_LUF-oIQfE<K5$IClQ)K@=A|r(Ev63m}U0TtJ_1(hN2@p7R<Qz|15UKNc49JY?dvmnu(`*<19<<Bw<a?F^A}R$<P6RlF-2=A=dF%F8{LPV4zC56)X{LrqYCoCGBP_D99hCJ@a&!;(QJ+(jIX98vb|y3DKu9#<^on0H>!ScyoRnffrMI1J(=5c_l*CI->Yg6N8=M1{9Nlre}X0|1Gz7fXiX6RdZH6wq?YO~i^t8;Rsi<HYE|@DzExFx(cmsMOIjCg_}aOg1gIu(~=?4D{LhR;1Z$B0Dgu6S@Kk)|p|f!I}4K3t-s;jpW?3uk6ZKVER-H>$8Tg{=*L=CWtqoI|L_EV)>Q|ObfI+gke=bY9K}?+teUmfK7AKDfM2FM;Zfb^kh<nnwB$)$1Rh1(KCG43@xTj=qZQV9w~Y^vh)g7so^e+SY=mjJ4Tp`N|-Q+I*9U+1oudc9#B#Nw=QB)0VPQnJX9MwT#+m}MDF0nq+E=RbV|Iy1XvR0QdqGDh#_EnSR0uX17dh%T?0<)=&@6RBLeuZNv7jvY?^+CWi&X+ij;I#)Bx;(#Kum*q1Pf(ai&uvkjqIb_2QrcMj{p6qixYE*&tMJulcXO1@GR1cW<Gkw~uc<{MN&7k-N9Z-CN}DEpqo3xqFM;y+!WcB6n|*yXPZ!@zTN4-gKWn@wt^cU)HLBDRRd*S3$V$ldv5T{-lv(%5!yR26@z!)9O(vcs{zU*v8{z=X{dvJV(KnxzB#^apZ2K<21&n!fNN4&YNQr@iLF~y~1|KyxohDJ0=Ue+rK6GUU(LLo99^AdDipscGW|We2`-bvu7?BrP(G=GuRdu6kw2QneQBz`NAg|&<c1h)2nf>F3x$uA)VxR&+)sEeJnhGd6}}^0+GijT|^-jg7o&3mjB42#AzzwEQR^B*%u$-EPFkQ{QD%Y`TPM-KQ2<37a!+z=3_2%_8<<6j)u}Jl&GE$dFb_|j{|f1JBzbi$Xt#u<<GwF>+te9;hB8o_X)L}XCI%&3ZIF5eb`q|1Rv9dB<PpoL3DgRk#w9-la3z+)LzaJ_T%Ysi03@M^XSNO+PpHe_+oS{<R^df{OiS3;<k7%$GIM#b1|WK*&E@B;8#5B;dnVBwusHm@6X=Muk>}FL_7Y>k<R}MF59n|rKe~IsuqW-D^nkkpM$ioFn%3CGh1nHA}=gl9pbQs;J-4Vw+(wr;Ax9ZR`pD3MS@Ko89u|Kp<d3aBqZ#zkeVvYkxGR5pVo{unDs?XI}vY!AeueTI;>EdIEd306&DJEBimjz!0ZxXMd!Z#YJC8&|5n+`s2SIaRk5h^DlyA6BbYIA&tIYZ0Vx?eUX4}vP<N%OrWt8rGpg~FH7l*5&8Vh<3vL3l-hyh#CtjI>9zJ!@S1FFDrcy;a{~O^?=CaLY%;mc|^(f_#9vC#U`Eeh;@azv1c%neDN4=wrzGX3(oWY1|=P>cEvTzi_ZQ6dIP+HSbeiBfULzq}*exjmTMNy7#Gb&XjRp-&3D(DFrV)qmQIY^(lWjt_eKe-ReGxfV{*}UHQgDYQmN*3QkJ-Rwpoy-UulAo4^S#S|OMPd;*C0pTYcL>AoRp(OMKOPNbg;J~W%e#|S{|4E?qX^-N4N~mP?v;}o&+25ix=~QIx#@<f^K*^ggMO&gFx@4WzxyG<z+Ld^ewKAPDZqJB#wIVhifu_SkC`R)!1%kYVN=g)*r*O5Dor<n=~meGN|kR1*8XF?+Ui8*xX6H#Y)q1M(&DW88a)%QMNytq&ty@(MiFAEthOF1KiKMX(sFJURaI&@`;o?(Tb|_BS;|XeDMv*aX;Z3QQ|2mu9=CP^<De>5Nd7g2qZBWdiG;}>%OHJ3hU90iN%I>gMU-DtK=diP@{R>>rRhK7zqjSe;!&V`uAbtm>XFWZZ9j2nSyh#}Fb=uv7yS2}1w*e8EY)B}b_WKD`<~Hb4$E8`K|~E8)UH@*JqtgAz#Po_d{P9WQ(0xuBUKoNgI#mY?q9chsJ0p)((-C@B7E$YD{MoxoPsg+*L$skX``%Om|I(EF$#&dR9`1ViL;5RSTeJrbFShl?@^&S|JnB*C5pj({k{X06$?EXsB$_=>(lXhJUHE>VOfkx)dd;x$FOv5Od3Tw2sW}r5|JPSE--340EI;udsGzLBexqNco$x)lkr)vQABTCjt@X3?A=60h=HrLr2NdtKw-46Y$z}e`#=3jmdgKcM&Q5^n4TX26N5YS?%1Dp`I9SwYk<8zsMr71Z=ly_g8u7ot=GAKve$zb+~|RnIqh=3uc(i8(%+FKgjdVXW`Sw-_o(SkM~j`afjTm<kZ&4O-jJ|ueNhnct5!6Hf~ZaR$bIM8?)ORm3*nzUVbUnrQp-*nCwrf=v=$CS&jRGTY#;CL9Wx9sqW$EC3_D0(H|;qHNjB`mI>t?xzr2Y$_`L`0lC|Xfy&Z`wmZ^yt)O@(XD57rQp7$#G_9ogS*x$zod>f$&-jn@-)x+!=_WP&`GrI@;a5|ta#SbUjqg}PM)4u#=pJ1j5{M_qGH9n<Snd&f60a;e-FyX(IlF#V`PJv@>#w#kI-Lfzv8;sIh)3LM**3DdrF_W3YrqjeX*%X|4E}_cxu?FK{{g*ZbRAJ`OGd7@JUMyr0nMjjFw@<6S81ZLzOyvo^sdc+_TUl#mQGGGTBizx{$s5yIzQ%U>(?1n|g0m_SQnn~e)ts!Q9rriZS2Oi%O{i5rpkEKE{IMZVzyRXe%*gBP1iCEODXys$*w|N88MRrJVF+d!WIjqiGmjFj9BIH^3AO|FJG1TJ<OQ7q%Yay4P0@A4iDWLEqs0;HCeHB47}AbAe<d@O-F^c9Pf%5CmRL$x8UEI)sm4;|5#>2lP8&o{oeJIv<xg^v3L-4j9}{^MsjPrQGkIFkTUel#++I`4Dp1tf7$%6ccR`#L)X!ziL9Clrh2CSqHr89@wq*jTsJc1}IrY)Y&TmPHNr#k*twV`o)w=Y3N1Z|QUS)A*0Gs&^&x+)Pp0#9A?}L*IXgZQ?zN2>i&VAP`vrP-j+VYOX8a;vZD7S6{no3W7+;)(6t7OKys54eMX9vP%>k1RMe<V9-lnWzM-Dk}ySn9TEp`3fEu+EYS;BwGez1`~)+s*6|ew4xnwXva#Yaj-dI)ojIilK*=x6z9<Wn_(F{sgZXPh>LgUG(}!8yc`Rn;I=59u`J)#hN$zHZ=8r`BfDUBZ%1S>9<!hg*h=z3$#fJD<yAl;a!++Q6g5{K1rorG#?LHd$$+n+NA9Yt76=wJ$Lyl0&Po6#u3$;ZTi>|;qS=1nD#gBV`rroa??!U<&rOY8z~~G3G8VEvs_JH5wn>#VOU{rvyZl4R7$i?)SxKd174;~+O^e9)@}{cZw%K{HXGW`v~#drSqV`-HyO}TKFJ%rRy_M@@BY&J_3n+Cn;7-A*~HiE*BfaL`GB7Gs=x!g*7lsLO4*bJgZg!Jw|9SSn;Glz5$;*$P{}na{Y;>piQ|ns6bi#UHnetAn}7p<wYtWNM>)^txfsN!G^Oj6-2CiyXkoH41XKkx-f+OZ2Ja`%h&#x*-7S&iJifk{$KBoe)`tDH2O>HUh@E!i|2UUD#^z$p_y$Yw;UOAX)S3Ebdu-S0t97p^u7-j}xXuY#)S~WQVwEaYls+rHmlvh?I#L%7$J+1eA@W5HoY0FpkX@?-IhTKT->702H2eC_S))oTz?YjZC|@YR_o@o;w<@bE2gmB96l6D-f48d@P7smDu?!yup`(9)1vkgdqAD8_1vl?ofcG<VLB;F%lOtgzM*g-DRzjg(a8@F~nTJ~HAmtVjoXU#irbJeeq%pXc#p%b19KrC&b6`nOAI7AkMxC3oBv(=k;Y9{*wP>sG<4GBp6cf!ErJr!uBsRapp0CX|CQlw@01+EnmRE~;Zsb_?knt`O<j(55L%Vwy-Q9}oBu{yZ;do}NJdYdbw1HP|m&G~j<R`0&st4l+p0C(wRyf*E<4)1;3&4J+7M8Cd_Ol|e<&-~}WQN&vL(yf%IA<?<Rk1n1YR9j$v;d*+RrKAzm6-EqRMsj6Fz@W*yvWF#u02AEljm1!-T|*cb@C#~x6~&OY0+skpcJs)v<OJoGr{)%WA9ylZQ0)Ipqh`WnpLaTW3Ro|+WXvl{d+hU=a)D?%W*_nhXx&J@DD%>L<0z~h6Q#K*~BD7vYdo8h<P{&ArT@A36MYv0;Gs85`qSeC=Dz?HYTzN(53-%jPcEStjB(wd+s^cVP75XyZ2hPYE{je^PAsed}Ht{((>+fC4u+8;-@<L9Z8*}aD}RJgF(4l{c=#_f<pzA>fij*pkFF+(24%dCp!{|hsxe1A(<$kJ$q%m)w1~neqhXz;p<;}Yd&~uK6nFezy0|(!fzw|)_m~ReDKzM@EvVF@Ncv9O=j(_?clBL;P3IagY;dNStG{lyTlo$!fqALX~UoxaHIL)f-_8nVaN|w0zGwXs~Bq252?k`faFH7)Qp=$-Bk@b6H=S<F(a9ltFAIpAt^E#Fnr>pI@cltdYy^aD~$+eoMa0S{n?*!MkMBD3SAoE=0cLo-MocMrm^`ocp>-WLPpGh(t_cy2*kLByD!N7OU5-M=oZ-j*;tJtY0gB_rqPZ!#>$;vr20ijVieCh1D<LW7%zDI3ctAEd1FWAuF2WC3j(%Sn8`|8%*d?96dY;cj2x(z{7Wp{b@Tp!%jSRyHyvNDZ04WRG<*45FKHKWPqho&rsMM3EN+6<pHLNhqCeotTbtgE&!4v3*KNJB*Fx{p^&`(T$IjsYGYU69Ki<v0<q2M>v*~0_5AL>Tn7jV4=B!k~y`FV!JZ<yhR)g86rjO6m*k-rsZM2tt1Ls4!>=;<Ea4p&emJEFENolf0UFUbcX~FSB)oF}X>l>@nbgx&Zsi{sAUZ_sRI?W_d69Lq|u1>>hW0Ee7H&L2+Ax#yR(p2@8nqyI<$s=_`lqvv;vyh|dD{(bpQUM=zrbyFLKm|s2AxhO6*cye6msBCsXV<0rm#e?R5@i1ON2(^zxDJRbv<M_33_L|?0Hq7vIu1R0BMgPS38_{S1}im>ylU#?g&lj}@?0jft95taCy#82)r^??n43FQk}-M1TDUY~Z5%Lxi60CD(R#tK^f+=0D898oV)XHKVKB~8!8zd|uJNfZ;#328vv6%4-^vfUzN7k;H*wqah>zplN4u#3-IZw0={M}CU_G?vD{;r_6~8OeBg~g1EO_mV0}imuKW`Rc>-_h>8JsWQLd)9hl2Q+Ik+!LCOd>8!9TI3Yne|4{AbKom==#tus3n3pgJnyEu%oSDqWl+adAFcKqfwZlMgilh$7Tq?tdb~Nxv07U_)0Cvz?1g`y{!^(k?dYkCyck2EUZA-l$y93<Ru;pU0z;Vt2tVlOKXcA-D%kr%iNSk8qw1x!bQTrlxMsrt`PCWAI21H-tiF~@~y=^9}aMw`2|WdVfK>;tr1kO2Ek!N<H&-2o>G{ReitLfn_&F14PRxO@8cTgt0B-U8^pBc-0i$D%>Yz7-_;OYL(3O%xIjyjj1XN`v1bDoEe+TfJ>=Q25=2$k!meh!#)d6oFnZWSidR-v6>k8j)HJ047mKXGR~S(pVRW8=0zyq{QZj>4R?XW)daT&?O=MfX-+E9V3qK4n0+D_awEn+rx^MW2XPSdJ=?OV#3twQfwdO5b0M`5@Y}H6EiMchl3mLepHGauPtp<QSs$&TE$tMulgN1En);i?WWjA&YIW>52&Y8!<9-@W{chPCh5K5I~_yB%QjLs96Ji3Q)F>K!B_LbKpp|O=%02_SPucLJp<s)|i=BOhmvK1W4Ht|A08P#rweRXZvEJxES?N35)__LYqegc~fju6{5?rUl|;xp5NX)4=t(d8GY63C4;Rb&5=Z^z~%u67<An%=bx!c*{DVKbuRyH%H;U{A3>S8b|15wOG;`=N-7wI7;-VRn4rbgaFZ1Hv9Z>-Lzx^mo2R4B1te4kmr!(uHVpj%tA8vzmd)@+<}hX9gzgiepDXSfIG`>orWVFPKz$%gr25md}v1f3h*NqQS3(Co?37l*t<~N0Oj(<V_v%WCcuSfwSO3+0l&D859mY8qh-?UNaJ?F2H1y_~7W<b=UA@J$I88T?|Jyd4rV2!eYs_3!YF1<xEnBRwJs66rbkg`OZ=SgSWi~{c}X%<;%Fgr89~JW&T_{i41bW5{=t_;yL?MF9E&x*Ff*>bD;O(m7w=*iz7krG<?}o@yQeP9=ZSjkR%G4kV3qFT@df_0`X4RmH!zmG~7j;1Kk<X2POh9vF@>8-9-#M0^R!-cXSDK&&Q!TJ2CBefpvGpx*OwszLyr=n-kU@ab>n{lz=Aay}k{4Zw>S=rr8Pi&I@LkbBTMeoPC7Q_jmz)XUn)(%p~-CnxWqtqTjhW0sWqYeupP=6#yT$GxU3!q2K=?w*<(068-*j`6NyCrSd&<^gD0%uBceQ00xh5IYYw7b0mDx^Tk`=4Ltnc`s{IkEt@)S67HGkAFayQqJJgqQrRcG<p8cE02Gc#O8{7vVx9wNm;<0Wo^2A>L~0pcFVX<c(g4~j1hB>|z7(k?tpHmw$daH78~2Q`l&Y@XwUmIQYu&hQFx>Z3ZeT7|n}fTaAWloT^XrjDawKmqg0)~x7AlpT2b+0EcG=kSHQarWcr~U;bXHeWE?a~i|MZI*2l5?1RN;`_N&fN<yy(OWU;i)PR_ZV+Y7_I4XE}KBK{p2)3_!6Fg=6X+*fUp|TsvCO9&j+8=gEo}gIwnm%x!+8Yd(<S!Gh^L#T+~EJj3y3UIV&!B=zPodn@9Qz9FBDT^(NS^4Kc!cqTSh!OeJJ|Hqb+x_&wm&-ovE>9GAYzPtks1@1C0o^`-pHk`~U6VsD_@H@t@xXeel*1(*6Q@R%5qhnNDC@LoP-pAUZ1&ker?Su2DJk^4Njc~#&%;5n7&BqXrPUbWpwxdT@Kj7Q*37do4@#eb!<HZyW&!-*~b4?TtehRoe5iX8hbO^ZAq?-5AaK_JosnaXSs*%|tRN2XfSdHXLoJHb|mToJf%s3SVr#uCmP?|fhHVAE=hGvIri_Vt3k=IP*(f75;i#%C77G@_(hsYXKW4R19jRxZ3leitkV8+%*uY44(t}7u}xRQW`Ym?m#I0#O0nHjy_j}0vrk@-=$!Bialti4ficVmQLQUkkWs{}UZmmur3rfl@7Nb-`ezww8#<b`mP>cC`w8pzX!nwz$npwAhCg|9!jhqL|IJ)Cf7x9s}8=FzH+bARE{-aqHjegXS}8)=swZR8-wYaVS=JleSQXqz@i@Yg+B?Dy>6bWeA0p1HHp9m4b7o9!#RH<fn!iY{z(+l7s{UD!w$wgny26Ahd&!AGvzr+YYQpUja(PbrvSE`8Y-d$G(dzQB>SRdu7Q6I<%1c4U8dqBrm#>dRhJh6(1GE!|lJ*|1q-K0AAdc^}-Uk*QWYvw5^($@`NxpB(y!LjB{oVKfOIUK;&cWj-88x0IS+D8}Tc#BFKE-Zt2E=JK*dUcvvIDqNNV5otxUNPD!{2WOd&#FWX{^3I*IR>qZRk#<aST$Hq)OLgSwNuO0afr;lh`Jj>rVb+WUW5{z<cLk=TlGad-&2)KJo?KPWUcw`{6%(b|%`$gqJH(i?YbvyLI}67?Z!=w<lrL+h<2(XaL&`rleC3W^l9AIn&(1ufyNdm)#4~MB^r5GM#os!E9C<O9s$EieAg03`Hp-Eyg&D3m+q-Ld4VZVTW(PGq*FjWX_Fy3eQ*__x+>QNly@*OmlrhoSS;1psxAS9tnnYzXULB`x)0U50kf;nDo9R#%DZOJv?Tknx%Nx@B->HmAF&U>$F0@*!#m}1E#)Fe8=)Af-wUiP-TF_g}Whb!`lkSCWWxgEj3QZsH!i{fLV`tga!AG^9@Tlfj7uI7_TWL>o49%G3)XkpV9S>IchNqn81LymA0e*QT{KV3>#*6W+l{?)?m?c}eqiQ4JZ8|+c?`HRC4-~g~u$!`0M{Py+(5E4t#(AIbw6DC$__(o(R(ks6GZTrmfG;?~BAvHl$M^o1>V<8oD-a=uyRZ@0YqBxJ(s{rYjqtoEY(_w5H-@B(T~NY+h%&hu#t;~jqW@TCB|Coei!~Dkq`JVjw_FX=VfiFB>THOfzs06g7TZXoQ3-@o5rsm@s4$&`(I5kN`q7a-kG+L1*fL2g@wnjeS)Q5xr;B6SStpe7H6v*1Pxf_M=zew!OjGk<%)iE7ET^^5TdSGvlCEy1&oVc!X~bsDSQ<d<`3=f2m_^dcQB097G!9O)vvG>r^0h>OEtGmXQWnk<Bqmn~+~wlY*j3r(*#(fiV~qTQsPcTZylZ{7*qfDIe@OpP4%mmEX6g2k)AN{jRy<Nx6H&Sy#`wKM^|ldBA{Qf_jT{(*J^@zvXbN1RK=SYeIuIbS%obJ~pOXA;(e|Oxjq*67^(3F27Av*BQGI(?#n$gwHc2ayHi4Bf``3xSAU>kvrKTGlQtsWZ?n)86_N7RRw}4$pm~l<RhmV*R{(od_;WZ~2%8qT)^a4Q0V`(o%h9Wl617KX$1Q|#BBGgZ#JtFq#2d~Qr<$3}`9J&h5LKbI0P7^6(>J8utRbIWiinVBP2#Q?zcy{*MTHsB+1-F`IB9}NR#%+yZaWJBo-~ATTt)Qd4nQq<G-vDD3$oF|A%X$N5Me43zP8_Kn>ScblW_~qX!&o)T{Ay4dLHSiLGC5(Or#f8iN)c}IOwBD7(yCo%R{gU`E1QS<6v&$lpCJ~QnP=L0$vhV4^cu`+J%?GLPCfBG>|Vt8fUnzrUN7}eRe#+Lf3$jh<WkRHcaMqIJce%M38Qy%e+WHkgI4#XbCqk(kWd`8c?<g<jZ2eFT@6H~u=jgFpyF_vm}Y!=$caQT#wSY-+kDtSi`tO*RTW|I!-P0+Yv_2k=7ez~Lkp1$+5C0njiuiYJ9#80w6A0zw>u^Ut@QxI-yN%wJeTG*40{2sg__0;Om_fQMZ+W5!NVT&w-3hFL%OTbY%wpQ$yVF9413N#&izEoGkk0)<^>XEjAWmZIfb#16MrR!J?E|!PyJZE=YyJ2!Gx3ur#k0>!FftmhFB9{cwmaL=s}ZbfXrBmG2x<O-?UZ*siU8l>+6}B=%s*a<$6*H-mci!w-{iyuqGXGm1_PlhnP?j7zL#;nOM3Kv=U4;BKP+qG$Mmk4s!2XA1q}8i-2{=0Qp|Lnz9SEzsE%z0!GQ0)~tg}1EbncXB|TQw?7fkgbX^<Y_-;fnJ#a0zPpWxDW8_CMfrr?5=0#GK2nH_D4H75*=)7h)C?1G5wRw!LgU%CBWn>-+nTncI&Wy)3`AT)-I~#hyxMwVEiw>sYxLFrlCS6{c9=~iu6*z$Nb<(zIk>M(&{Z5aus5xU=$MTMqqa@Vd!nsGzbn?uGalwAN`9NqyH)-2I2rv<e>2!B%#W3inzPywFsqyltsz(4IdWCJlr)Yz_ySjutLJ3i^r6xva&;oZYKJ*;l{PmLl&Ru#ohQDrpAC^rm5q#7rHh6AI&d`@Y!yuIHI8(tD`?fz?BPosIv8LzPyfS?$nO{kN20~K7j`Jbf92H!KY(ceI$pSWcHk}UjN$bIpGUgm8lDe)6qoMV*q4FF68y$vzr)&%FCTljt}h$=|J=rY@BCLUrnSF+!sOnlnWEt9HlCdJ{#L=X4F6t?z1Br`ULGAL0IJnP2a>VUxTUfBiNMsibHu3!!Q?rQJ+d^FNLR^ZSQ6Fs0#-^=bQgDsO{7;qG%5X(I1<-8h7w*W(}Eoh&8k2~yD8KBC5lNm(#(T3*DZjcD*z|br?iJ_$Enf$%<Xxh3SAT0>Vo-shuoKW<EC1{v)$d8AkI|pm9HBrlT>P^J$afhVVW-%V1fB;!}J<Ao^i{y=_4M%0%WFJDP3^Rql$!N1<PDl`8F%JDszfDBdtv<W_6gs8?nqS0Y1)2&0-`L45_t@hG^pG>;-C{a~7yV=ccySdY;)cB%BvPT}?zsgIUZyxqNCxxDazum9+_5dR}RD`zcs_oIuc)ZeR2cczt%vl9Kn1r)Y__VHUqKPekN)MH<T)_J<&>JbzoznYDULi@=vmIg^umtEKWf=bc)i1(9a|!sN3~*<8E3SaSSl>m!x~Hpc3c!lnD)`^aAGhlO3VS;2k0$SV>Be96FxsvKGEMo3%~2#=-mv2Iv&WcnF&I^Kp(H%YYPm3-3)G|k<zcQ${Qpy}~@UlN6(P=8DS+zU+t9$se&SCVs*2{*cBL)^9MVXZ(6)10`pyv<ar2<B=<Vf8W!J6wsv=Cj!L;?Eg~{oc1(0|#rYV0$mBfj2KHfSa?1Xr)^gzya(mHSh*Y<VqQQIi0Nx&TXcT*J|M0Ng7ryX$@z^@Fy$beyoI#ZJi%l39pHXSr)@*m2hrNYqgNj4=F7zH|yc`az-EBvKa0wsaQQ#4_}6FpP5|tKYQcJeB;S{;~0GV^KFFRSRCI5`Hd>`jVkkvD)Wue@r^3;jVklI9#gnCw#?7OmigVH%GA4OJedFy-r&g`liq?CQs_gylN1%{*M@6W4Z=qe#2^zt6yT*7$b)H9YQGYnk%C&SCSpS)U1ZCt5ouOo#w00ZMp$q>jx3s@R9SFcCewSGQ!EOZF8<7_nfMs}1r6gRv*nd{;}zOQ^zx2*`?I@n&)mh?Kc?ag=sOKj$2*Ebz!?;FdiN?><%~jeI=PWLo?oO9x6Cf@j776@235GiT3KMpXGEGpCX(sOzlu)NFBvs2=``mL_l!LAk_~ln!2JBKv}GHqCUb;(%83B-iB!`)!LfNs130l4UT|#QAlNK~v`;Wq`sa8oKZtDeI>lwUAX;4TH*&ULW8=KS;`rjPK4boTihI*P$-NoQ&pZzD^{e_Y=E(~Z&dYbNQfTUem+X<ohj~sf>92EmUOn@xs6^fDHjUZlf}iu5$NF-f(xE)uCwMsLl%f9myLxNJR!a2YB}=D&>d$f5uW)br@n;pTvUG;C)c7w{|CVb4dI$3RtDi6n6Sq)S8>kFz`oWS+<1a%C-hv1L<Jhz7e-%MpfK4*LxT`3~?h}-TsdvSG6I6hrKL7!NB6(7Efo-xV=}U^37}zFOYnI>lqKszS)i(KIg+>Z-YIONj`P~)B#Rg(y{1(VM(JYB#;|r28ph)UTzj#0?VgMrCH@hma-DJh0OD`6Q$krR+!coynf&d7*3sM(A=TyyPQ?C=c78eiH8%tA_KLl$#x1ZS#{q`p%%o5NU<zKg|4RXt?4%Z83i7W(Z$(9vF0=bZ0v>KUlW}#ksUMx%2;9YQxtig_ys1s+FsgyQE9{4EG{`J~#ARY=HqFj^uO8Iv|m<3q=QwUst3xQkk`D_v)7(Gld2>I(E{>Wd{ql2q(pu!c)qm3eVGlS*F0?S|BhUH&W$`nGcKQGYnKYcMz#)SE5!BdFGI-jA|H1|a%Sk{(36JV06)xJ?EYlTz{;w8iDEeJondfvs5;ntN1bv(P{JL2Kc5Ir_)MhXU^r3Oz)=&(dYqUiM1UguF9mLRb=Q$p|!4<G=61$*LftVJ?Ui3evI-|NI(SXI=@3)#}}7_{D3RB0skvSSrry$N}u)%>_gO6JR^Ws&>mh<d{+Ei7=}czx7G#yi!)1G<m`QEVb4II@vj+XBfJ(6$@-bEdDz?-V~Gl?nlXI0)6@*;R?F&TF3#2QFtaGmx(!r0;)s$kS3=HB0ieGsW;90)lj|82<Hb#qc?QS}go&@1GM2Zx%w~FCb6zU`~5dCHxk1THa`0Ml~TxhYQ-YbelHK&p6X=6HdICFzp6gTJw6gw1rkUnUFpzRT^M%@15P+=jTcLJKqI<bXQ2yy!$|kbXVH<e0+u_eS)<-L8ciey7UEA+T<7n^?>twMy&J%r)jSA?(sH*=#`8pJ-mu2y)MwO8Bw~#nde05Z6QjppCd|tMF-yvSK%{rrT^cbp4&Jqxs5k1Uwjp}v2udd#Bj`(&}SHq8_^rHG5@s;$Nou%<6VIS$0rz$X^+rs_9VTrsEe~RJ9q%J<1_TeH1J`<^m_A0)OUY{=U5#`O-B~X!gGA5#aDQa8?@-YnCEy!0{dI^#x1tJPdlkY`bVq((DkI1bMN3Y^a`jP2>n+Fz|29*f5J%Qxw(GO0EgNDuAzHC0F;B@?L9V>{P7K%SwrVT4o1V#GB;}U646QC#}6lS#2z2Q@Bl+_sHAIdrC>CLoMa%to>%h>WCRS`yS&6IZy``@Pa<UqyN61BQ=HDBe~jNdge_ZLyLVyB!`jD6y!>DZI94h$H2nDE|L_5kz|H2HC%Qjsw-S{{B#9h%B3s7Uir#7iSviyOCO>(!`~lXjpZ9~PF9)u$6XUzObL1$cB=&#9@iSZ%p+EKlwudl5L%;o;7H=R5)XjDuHHomrhZ|fD19(6nZ<8{^`syAlQ#QP(aJ)Kt>xrX=B+<)t*dk{sxGC-#E;$z==3$NguH%fR8MHQ)xvR&Q?IxcWq8a|;Cu{V=_!Vu4`g(_*h_aau*;Zoz@gsA%1&m;zIMay;x0=3!u{NaA_Z63YUr~KuV6P|>Dq-Vm=pyBf1F8$HID?q3$WNF7HiF#N47;3f1OP=OBA(Q3!6p|`g16QOF{wqMx6G=9cQcxtXjDld?JIFo!Xf?_>?!@sRX?>jsV!`mJtfHx+*#j`Rxciop4A;}<7TyNTgZO~$&J{<$;bEmDIbuZRoqlz)|DWKFP|sWUX43CZ4gJ9vwd4WZa(t~Z{Z2#tvg3~5PAS9Z5|1Plg%2fb~)<VCFTk8V64Jd9tq5J4~Hd>{h|)3e{JYf)vxF=N7asShC7}iKhGFLUUJz5%-5g3s{TUtZ@c=(aNf}xlTUh&X5sif&~9b(e?Z<K_!9$mgi^@KHk)dTAr7kt+jYo3Q?*@H8<C0<3!c4a`Kj>Fo&jZxrUlTw25ufqdbySrw7`(RX8#X)zZ#BdvtpN^3K<?A3zrx-6-Hg0PH~{fVCxaoYU_upQ1VI{I5s8rcr;*7Quz|A5-uMC3owl2LpS8*P{Gv83CzcUXTBxJ)s~+MyGkrvUX<c_+;+y>04Wa6+dA>@!3dax<aFTlU{f`dDY-zp-VH~xR(W+Wh7Ww|U(L<{me~)HfyKml=h*hb(?nk5W7t39`|}I^BmBg^=Ua7UFfNbP@inYcY!1lfqg9J#kbRM4=^wRrLw~}k4>OL6e$C`#&y5pH9P|>MCAX%-(v~DF+-5wk!DGOgIcF|{!;xRVXGTTkiQ?_{4{%i4(o%|7@~WgiCQ%JP3IZLq%UVEHm)IFsp3P(pKcK0s>cOpwcfBL7w&6B|O|TNQ4YdP2e1o)jUS4CVD=X*X5&iOu*oZ}3l&ATg_7};3(B@YHt~&obxN3jE0rc8KHoJk8%^l`tScCM)Z$h}^=<d-YuRU2;N4gErh2Y&sxZPogEi(Jvl>)K+&D|a5(-y63#*n?c^Vz(9t(&vJCd51cQ-$dx6x~hc=keAisEZe~zs5e5PwT&k)m^@`BNvhd^_AFw^H+EKK&B$jP<{nkR_`!Da6A`4gZ0C?hNls%SKH74rtaj=HswG4QX1$-i{`NNZi^|`$mR8Xk1rfl;md2OLuT03Hi^;FoIL1W^N@ES<zo*cBCmYOdzpgT)hjP9j{Nr~V6}j1YR_V~c5vKlNO$=#n7R%ARCvwY1Ja9}+$a~h6|?M0)gl#8BYv%!Db0I8c2)a34-SqROR+2dcVtgyT4Q3|F|2D9M(yo(PV9^G=;*~Ud+^8N^vHNZUJ1+WL~A^3LU%BpW3{8gcK*ssCprU)_MSpwoXs%I$IxhReZWYZ?iEjSW_VH0(h%N<wmkS&KoSqjkX`V+a-tP}umCoDYmSOl*;1GS-H7u9`d+ZU^@L@>Y4Zp72jn&>+!WH<A6i2?G}DU0#66+=54RrfagxD=OmWS58T3rfKhli!tlYtNv$(c9avuQ4U!}=KAvAmi$RqYaG++5Vy|_I35Zkhh6TWMIheeW?*5+)+{}b7}>8}c51%^DVg@P(GfKzP`*{8UVF>mc~G{Ht*NQ;zT%FfZ2=b;%!N@B}cNqOjfb_8Mr@i59*)#Raiq-YggcN8jDgmkpzcezt@A-o{PH4?DOV_@B_D6TTGmV{?QFa!S}-}?#4s3@*=<{*#_8<5C#n)ul-=;^aEKL!Vf9v_I<TT_dHPy1KR|64o%!>3)q;{WBJ_g4x-csMOB+35V$^d8X2=QhnXUNLwqq24oNJ_dq$aji;9QqUvk@`~Jhx`~b0&7H`-jO7ocD0CA;Xj;@Q8&QvQ%Ta>Gi)k00woCHWnW7z-w`rK0#M7p$0P7K%v_VU`B_P?6TY=iKc1WZ5S^#K399qbR;mRAFvo4vLH9E^DUUU7-p>rgyX0tYI+erHEnI&y$QdShI9GKu5f>nGDdlpeymCCMMzKf=1NLMq{f}qfaf8gm7&%nT9UgCLIN<2d;@iZTaP&@|<9ZNj<dcL?;;u%15a9-jWN{OeLmv|5!qssFYH`D-t0DNsadbn9D^svf%is$7XO5{=6u#|i7@STmZ8~Md+sYUvBR{E*2PSx}e4$}O1;}ZoS%~mG=^E@3?3CefDRNq`iXJDkbg^6aSz{6xbLqP7_eNhFtNki^&=J(~k=8`&YSsseaN2)xerqUb=@19fDDU{^+`1Lwbg|R(3>qvcunB4N|c?1v-#~C;IqH^S2=S$hB&*x|5h)?jF=<L|f?@00JpPjTyf6QnqVG^~>uuiZY>6Yf*egp2$y_c4#i+3f1M>E$xqDH=@TxpK_Hq3FfMX?k(pfynz!1Zt;Dvy7VV}xtSE}C!`d2Ap*x&t><B<MCC%zWo}k31gYmpfAhMXB{ZC~##~zz?y?_NLx(^XKuR+|4^|TeMP=^i>n8RB$BAY14qJW}+|X%eJ2%MLY03M(s(Z7ElYV#OoWdRVgKrcYEkR*6>U>G&FfXUOD^(cWR!3`DafYjdpuX-0Ugf>~S4U#MN`x%LCjZtq2{z+F8J+uJPo-HNd4C;eY0_gbI2r8OOxFg2YXL-RIZ?V3<zar&g#6h`d!A9zd)_m2DZhNep=9Yt|$hvV^ek#moQ<9oXJk^TxIxgGAqu2vt6nRk+G<ed4@}&bSu?#W?j?Jgh*c4N-<;V8EGQ?BQ?2HA#pkBV%S!m&SkZ6|~An8jBr$nmaf{ELp_6XyqVLk6?q~ZX#~uyd%f0?HVkVz%mCh8IuI19+1q%;|*0Un(x|+`<+Y_B4BpBPmI~U2&K8U#jjltaK-L@C6(X&rM+My`d7QhR=+zj`;tW#iCTSuQ0ldX;n74`D+@|IGf1sc0R&*@BkNGO(>azkiLIl8_G<i=8Rs~^x)y^oZCV@VZ%IJLVA!5YDHBRKM>({O@NVXxGS_2vhGfT|NYL@+Z{&3~{E-*15%+O;XW%Z(i9If)Iq}ax%3-*MOmrVhJjtC?vo<jF9tH*tJLI2A;sn$k`BSLg)pTuIlm?N~%5!T2@0|WQ#-u9<@4EMGv{XlS==0SwpYKw~x<F|Ta0V)a*HzaHHAE6Z4?Gfsjal3UHm{718cBviXd9v&dHo!4$}cKdzzhhrY3GO*+W1b!t_J<y6@uh$ATFvjJdjHkiztya7}?|qR%Bne<;6EzD1^l>oDT>@LVF_~stY0Z8dDHzKEJ&v1bz2;g};GzyBnDotuNy`D&dk~ILru!7pMfbmV~E(2{WwXM?xi_Ot3^HbOn_Vo<k+vFXh`uNW$^Oq{5$>>f_H=f6bW5kYD|Zp4bDi0L~J&yOOX40dUQn?TQ&)Rb~M<!lWLUK2OYH4kydmHl@3T$Y*9LXK7euJC74NanO<Z<A-Xi30`E@G!6U2Kr;`#)->In{#Z%AZsaOHKrW5DcNHuv%QNTGx?s5%fd>aBX{|p%T%O9co+|53C{4YVP8q<6Z!K#^v_`z-369LzAu;kCi)2aTkRH_kBsR5x%vB}%2Tt?<@<Yf2_b6OGUq04bB+-}Rd;Z3aABh_=-EUG`-5G<>q_8%x7xxD5AjM;$5bRk{;wnY(RFgum!8sQcg4kUzC<F!B^o2sO)z)r~$vP|-_D+Zm;!dz)OY_ylB1i%szeHvznY?l>ZAw~k0dGuN@u+aqFITT_9taF$oqjLUU&-|LT(sd6qK^N}w^jU|l@(R|#gWWePAs3E9{V+-Pi?M?vTr)C`5MvZfSRQhe7&Eb1OvmS$O*D!`AioqpB7At=(97n-K#90J096kW(SYxo}WGW<DBSo#V5Zc`n-!KnZaBzlrFK2{?>=@@J}=+w5nTOQ}b4aZ_cgkg1}R^M7*=#)<|Z=m!1R?k|psj(#0313F53QyfNEDyS*S*o@oX+q$k^v2^4VgMf(Bv|C+mH1OQPDJ&iN%RaQ4DRV-VX25#)*?w$M<R%LgERk;XvheF^L)Qupoo*w~Fyfh?uBlZeRJ7|Z8XVMh~Z}D~|^x72WWljnf|5xcb=4I*tWmmN9>e|v_7vvv*(uRb8&Gz%3WvF+m4B4PdcwqejDK~8F+p!XR3KDzFQ=B5^sI{t);|l!B6JRwQlqGV<(o@&4beg}Yv;Gc*eMxAnqq+ky+w{ty-D+^m7vf;D0~=_I7l2%>0RO7fGSgjr4HoJ5oS3~%c*Gf~F2UpBoY2LfH5So;3Nk5g8w1CL%c4OA(|tM8s`5@dRy?IFgM!bFp>~)~g3wIGoXS0xBG2%M;+dk#nq{h<*)kw9{>PWb?Vx=_^2riW9sjH;)*~-8loyX$wANE6i8y(xkUOs7kV|TiRE&agsYbI90+m7+(j)***r~V*D(eiZP|E12;?fZG;;D|r#sF*er59Z^pj-)yE8mo5DzN^*dZJe%fZ{IBTlg)xAMOFAz0}&tg|U<^2)nj~>$)8Z52=<uzGwzxJir*(%aK+2eN}|HV$t<VH%>kZf2nR7iWry582rV8AU&fv9$+$MIwlsCv%cJg9WZHkmBWC8wms5f4dpDjf{Y%vI_uV-(bX2MB@Egxz7_`{S=k)WB2T^z)aK9zM7q=?i!gG$26TLE>7N%z6aGRr6T2fq(w&gA?3?K-%Ua*l#M)cg67B;fJD{q9@ZrwTC<+iAbKUuiPRR)_fZ2V3!5Rp>Dn0!&t^T+d%{1W)G%F-3w(kE3Cm$bdDZ_;X8}fEoI!WE?@MVKvk>y<?0nt4UfCiZP$miJ`3SnV#fBn^3Qunk@ie2|bMM{~u6|*#S1x!e4jkAqBCP}!66($^Nj@BcP%_dr5glE_&J48H7q%;mUTZ*CP)9!s2ttBk*Nk(-zR=hTjbRUol$`_M|Z$nj;dc!wBZW&T?O(R7qqhp5n6<1sSqBxkQUfIBr6+zUUZ>p9~huAgpL?@86V&2D%Z#e~SQniXooCPVQk7{>(KFoUMS6fF7#8x;brYfB8I=s)&W26~?eH8h!Lx{lzR)^JpEoaWs+VA)b4-#Id8&~7$?ODg(gg6A`s09@w>niXJCAp0!hI*@DV-K7Kyv$Tmt^uhK<xe6Mfn7AJ*p|R(=B1b}h8qVATE4f|7~EY!55*SJ)3tJoEhDhjGT}Hl6n>B3rF4Ro!_-Zv)h~xiSVR!!dT9iz9m><^6V0_NqJEXmgFQl-a2#fcUDGYZ0mKWV<{*L+CGEXBmZg`dCy9IaHvOH^!K#-~5_I}<&p6*J<yWZ@Qo9M~iXB;!g)+rV@i`?9IhnN0NDYjJG%Adf1WqtbGxpS)e3|te7BNW{YM78`$9~<ivAq4ZGJH=qAmyjsxsQ<K+kTTI-%LF0W^V5+u{X+w@!`}#5dmw_Q!L=mT93v)WR+$7m`CPAZA(ND77@WR&u1{PXYzc;;ma(EDCrk@K4t=#=bHruqx|_rP|#loi+}D6-#>}^LVgrK$~zQ`p1T}|lCeOpr&@{fhF_zp_TfbLF>fG{0i&~&*V6+Y%MYN}L(gmlFj4m8a<C9qm^ke61dwziO+q?wU-_a3Nm26?=aSpyO}P3}h0gqh9<kehl@GhqCV;^><)N=dt&mMrU;+p2AW$ar=BvZPKHBe(N9NvKmABU6m>o*&lC5Cn8`yqi6Hj;`**mBMAR^hB9@K$Crvr<lBvtZL{n5*?I&-Y{*<uDnt3b+HBCcksmDn(#X-Zm-VfF~!hLf_A8dBA!K(oU?(Ps;gnV*5S+g3>UMZ|8n?FNWt?`FvPgwJAu6KsrhEyMe!MG9pve=g611Ey&Z22ONOJuah*=NRrL!Dk9%ezBfXD1`JA$?EK<pRrMS>NPTL77{_;`=9@q!%z80JOQDldKO96GqYJc-r|ggC<-v|n$B4vyrAXtT&!DS<FbX@t0i*wLAX&I@8p!n%0segC2C1~cx2f@d+bTLD$f1;GCUliy0^k_sIH>rUE8bGy|M%HtQyY7bs`VL*B!7~jfz0u-n8yDr%`^ldE6`}ao{8l<8V68<L<?i*xR^H^O*UFv#D%;G7E%pWjYM`OV<ORQcDq~-crGw(-`me%ABT|FVi|-M}8(ddfnFs+t<-BEcwrS%x0l-h%@-bSC9Ru`Lds-?cLP-@eS=s$4AjjJSApQN*@Rx1$^`T+0qB%^ytQ?0cSF=tBqrJSKS(`&?yL9V-3~vV_->uNrpz;%GYbW$WdI5ckT0Tinm6UGwZcsJ+Z%HL+FA|{UQ55RQ>#mg55j#Q;DfWBxUx2uh=&+t?cS8J6aOl>$;cp8(%>Z1co<%ux3XKUd(%0lXnyT9{G_PzD(-4#b7xAU<GN^JUtn9HI#^!A!^Z;hJ5PKp*aeeNM=S|o!>&G9wKCU&Uzf#>Qwm}R=UD`d%jg)TjE>!gdzXSK{EgvEz&Nb1@@H^a{$=@LELcB)zsO5rNaV3$4J`{l-Z$5QnQ2eCtP^Eb5G{41}B=tIEX-Fp28ZUoG?l=$EFWEfT!~F&H<FF_{#7|su2%i=PW-bU(gp~soI%N5H|3ZQ6lJ+=D94>k7|q;kL+{O^aFSf=uO2k4M#V5fmbn;)?P51O8Sw~JTjqmoili8?lh9=Y1n1K^{=yvLMp$wr<({m7D*pZ3fCn|LnICBEv6411jr8xc^Pf-vc1J!LO`)`Nq(w{q}$axwsZEQOuY-;m|N3fv>1a|I;<+9KP7Op_HC1<7aE3F65^;aH0jlg-3P5HI!0~IqfC-1hVx2vM<sh!E%fBabNcZYCk7y1L-^7BU_WN$aN5+C(>lwl&Ch9a<m2tc>EQ97or+6Ajf$dhF<DSwinw-WLHXS!b(nIeiFq2+OlM{>zxcgh$W}j{WfYFYdB(V5vFZ^{I95rQS6s`0u||@iDWKfeS$e2JS8`;|m5OVDxcU5M2bM0l-4QxC`Cnq!=8k7D7#)jUwKvjT>Hg%XUuW|)RSlaqqA+VLvNr4^uL)s?U(;n9!SS|w6Q$s!+}dED0rm&<Uk0+zaVSepG-twPk$ncCe@#feNAgWdS}fKO3B-kkX1bykj>x-3a<Y3wU<LboUmYCWHl#*=>B(;EYZcG~L+1;Z#zfTE_}Z1i=LX@h6D>`2(^lFnx+-0>aZJ0Pce=uLrfTD;SZbZFH5%J}L(m{+5UXkszUe81lRccRxAuWS)S{7+=BnDU@rD+E>QPH4-?_2&NuIG)c1rvPVKDacwfaaRT-R>w&d;Cn+^~^r27)vw{yh-t>GNesKq;Rr5YGnlvH8bd+T!%n$WV28(jQ&ZRLA`MPKpt6naCF$y*IFUwa!=Yi1OivoI6;CcNlmtU;<!%2-J56F_Ca)<RL#*fS6bQ5&Jnhk$UCZ*)I5%Ba7R8wL|}z_Xil?uh@@}f8Se*JvJCTERy(8?brwaJs)IT_+4oJkCp<;S9s5^Ua~160r{6+HU(#JjVGMD6<by>JFr#umE7Y<*TEG%n~tUZI#1a_$wDlynb0F!#|F+wqU#K((N?L3Thj=LTzI;q2c072_$bR{5RDcdNzLXt7`*K4)?Q27@ENSzkJ&n$A1YAz2QVy=d`ZzyT+}Ywm8m>(R|#UvfJq!mmp&`_>scT6DnFE+dY7O^DYdWKu!Yl<#q9rgU(L+$2da8-DOT;BJt%CzJ2xDvBa}bI!(iDs&N<W7<HJ!B2se?RS|oB};D#!y0q);|KEMSL6CMJZ0v)f_b097@;%9|NjfE;jAnj(yuOKFA>rG=zxlVcs_(~crH`VH*HLed-Pb~l7qilJknAgypJRmB_CVa<_>{Q$&I48_Ln3Rn*(6})~J7)D88udI<$B_k5MKAWB2`x=<U1j%(vS~^2GevihAZ1Tc_NecuyfyiwqwIyHRWNqYFOBF258Q{Fp3W)?EFqc$iD6(DeW}K%s7I8Ul_@J@CI#jsp;seJtx||<`(WaXDxNmxOTgh&A+;4+oxtQqQg#%TRN_6AiXL-_CZ_JKu3Cz!DlC?UsX|_AL_Lksa+fNq66VodU!}OM|B%|M<{%|gZySl7=}Lty>Gn!3byh;1RUvKe%NrD0m+9U<SR&AVmUqQ0MR3UITawHtjR(8MFXi|+T>yim3M`V7GZ{wx&8ez-ejc~*JW*&3CW2XfSKW?Vywb`w9f`HAuwpmsf_cBi6P_Mi$$eUJ+}pF8Rhj80C-E`r!OaGi?xlBCDU@4g*=}(Di%Hh`nWw5>jC^r?3+MdT%^K#(_ER^uEt8^MN^=LKgcix5y9=(VuIyO>iL8xwH`acJOIC`l98}zOVq;fi4<bD$qfaelsd!PigCb6>wk$dCpq~XTLF9|GWT&x%s96c5!7Pq4(<GLW#Fe^kM^Q@zSO~47dd>VwbO^Pfj9{7>BhDpZ#f5;XWNjI!97Tr%Qhm-$JQrxb`g=6|=E*L4D#1_@BSc|=Lw!d!U}uqE{H0gb@X_L2v%mQc!G0s2U8d{;8F_PXFj%9rA%f`Yu)F_gqy?h7=v826HU}gRcVN5}Uw<m481mOv@s8*a@;trEw>kJz$Nn=CSm2&Izh5y+O8c^6j(E2N)=cr|h8Wne_Fpg+;|fMR<=KQS9deD0w{}oGv7L2DCr5t&N8HzL1^63-Y7TAC0EcFcixELaqu^fj0sxQY>8Fz{YbO7*t&kn_Q?IS?wcL!_*A)4XDVs46&vAZ1z`GgFuQeJM6!`*rHT+oQWAP7ZJ+<-jd65OxTitGi`qfDBjW|Ei=9u)Xg1xG6wat0h*c~xav8|nvc{w5E8|xjS5e=>o7CJS2fwPe7oSV5)l;u!kX6q*0zQHn63o5pr`%+@v9=g@s@}v?Xsa@59B@AA(aWobZHVrjNq*xLl2^;*Hv6vUCRa7z0@V~b}eyO%Td85UY(@Bopd|#_i3G(~;Y7cUMtp|B{We@WD^*zYwUA#>*`_m2-5obNfKc4p>mmc>8(=1-}e>_yFfyHUn?y4SS?<Pz8B;{=6+78w8tg{_iXYm!afEeejvmNandyTQmmc+A40R$=0p3%>;1^cqmn4F8EC!BQ|U*(={#XZYv$0hM>e3E!J7UJ3FDdJfU#|wyOTN2N1t`X1HFJ+xQ?;1|$UBgp|@;-bw8i#+W`ey>LKO1CuJbt3@+<y@wH`9FY{@}phkKi7tRBRF_Y%cLoh%`8P<A%p4+iJZxsucfV)2#tujEG6(3sEIcBBk<ScQ9HJAsq%&RTkoO#!Evut{3&uiS5APAkmJ6S16Wak~#g+=sS}MFJ+%aYD`EgvE2jb*&OiH_LT|P562N9gOdyg@upY|xFOmumKy}6q6aJFaF3uL0JfvkHAGS~;xgEqytyayBC}68)$7wMd0ej+E$L8RC%B_u3uaU|ht!;<SLm(oZKITM44DW`+#S3i;y5k26#?rku|lpy^eH+dM3BK@ZY4|&4tY)~tD>qixq3Pq<CPb478iOT_RWJr)_gbO%hmo8m{WD+EMYDW)DM2*1@LVxa~5)-9RpoVks$6WCKQ1s^6o6XqC}t}S8B!)^YjW>n1AaVxl6ACL|v*iAUPHaQSw;af4x*g8g&}3>6#}&#>`!c)nv4z@%&tKnnZWB<gXo_Cf4z1{DrlG3-gtFW0Z%Zk>cbl`6qlOYJ6y$%pR5;B|kYz-q}r<VtU<Pag+kVU5+X2TJBO?d?lt}R;%Z_A-+@HjeqkS&CPG9B=Rxlrq|q5I`LdXgi!lPy#B@9Y_GcVoF?h!tTcZTBUT$~FD@r$w0%c@e3_W>)~qBiuV!VMW@R&X->t+89;ci05tFgF@2%3kHYMRcte>2c47lgB(w)u9zKWLlqH%0lG0TSjZ@!vy0i{;jk;H#W<BXo}$h^Rkk@M1dF?Jj=N%pEmmLjjJ<b6^#+$!dlWirQ+WWA^(;u)gY9;S4bX&9;M#vQ`&z0_1IC0Cm`W3xk^eJg$4>{Om0WN#8Q(-&EdJ5cZuIp<2MFOroSYszkt*s#pl<?FRlom5D)(r{d6=gLp3&$3+a3gd$voT?FW=t6b&6>8+2pVq5UO?WO>&648G5PJJLR>p}vu&k+KgXqi2%j<bA|LkA=m|X#6c0gBv-pz+ab~?2x(Q-}pEXb}z=oR7`ZdA|Mx>t{zx&k^cz?O=FHH00RTy10&5JBMURLSUk_E&N+*iphUTD2b&3Jx4x2;f0gZ;Bl6S{*$Ugo3xiXNtm>>L1=J^X`iN<Ouhd{uOxBnYt|R2BEVpf1AI&CGN@BrBKfaI~w8`$?VJoBkIUC==H>Q;>19vlz(E+NC*-TG)#KKbg$JXEVb-^^BZj?@2c+pJl-W=Kfhm_$ck*fYdWKb-@+q8k3fz%6G=II^;k^>X!zJ22-mn@(32n7j;*#%uU-kaWu4`*7c&lLjVU{DYhW@}t>06wr>Uf#2qv1likx}bz=9;UCych^XCK+A4ew)%k94Tokdp9-URkm_m;6gZdW{t#;A1fBo&EKinV0trYF8tAx~4c-vMpdibN}fzp8nRi<wU@bC>z~5sIPSVDy@9!K{U+u^|Ov&&?;VY9~7za@lNf&2t(NJ+g@$=op}wYbHZ_GmySa`a~zoQW4|Htfurx>XTC%C!M+1sRr(Gtn(yGlneTv|?pofjx#>I9^c_?hi%+EfpvXqfcsdUBBiP?Nuo?7|O~b$TG53@W*_{<lTFrtE5ciZ?U1Zu*I`#dN3>i9LlGj*nC?t1~D4i2Od4dz+V4cVo?wKeP=MLNXsb+`mCLiFo1kgnOnFw;AhihWLk!4bE0Iuk!*0Q!x{5Yx+IJJs-q@tXg8li&9lWhFT*8x0mXIsWx2|3JoBJ;*r3uN6BHCFmd={=Dad7v0bhr?=V3p3ES9!(Zt0hL8VCv`|lbF4x|$Nu!DxOGfa$|9G${x`GH=`P#S$ex<R{{#Q+Jv-9~J;yG`I#P4LXh>@dh>XZGOnS8G-LY3K@|<}Sg~dT~D?b+G+>JDa2rTr0v((mEMq}VHC<CP`ZpCy8SlNocY#&FMm;nI%$nVcSw8)0B6r}!A3CNv<-K^|g{OjoB_9Tfi31lm>qFJ$GXHYP9ZR5i8N|eYsrbW{M!D`}$^E1VmN=#FQS4^QZF23_7Z{t*@AnT0e`U*D97a3B<Tuzf$0wegP)$hMn{Rwsq9^ftcM+Z>FBa(uoQV)KMQ^EN-algQBVh8hyq2SW6M<1!dqjmvC9L${c$H+v#VL11UKX%8$j6`x__U_YWKEQFvC*15=6(qLmP)R8}q!Z|_3yruD>oCEM9AQ(q#R+`M_klcO{>CG}g0%T$W9L^7oX4G=4LkOL;v{mJJFyI(O1-Jj>ky~Ls^duv8<xWCDkTVw>OG7U=SqSSQRaCWgmsV%^fc-sk=OvDGNYWdB}7D(j<ESJzB<KtheFVmoqVGRa+YEo*><=Sr76E?Y&+-qMXQD{@{3!7OGpGruP)lmvlL^;Wd=S^W*O^(-2$-=R&0LvJjEDTjEF3<SCi|WH_3Gr#al@+_L|VfT*@RO7;`$V&g^LPNomDObfYar7ug{nP;aIeW7sVs6ITTCH)IaL_6~}|Al;{a^6h-P%rAoI_0N4gY(LzoU8?Gh@*ePD@)gw$bFw~k%-HN|1H+=S)C${=>osgY!kWO^PJ|1U)Pw9<93@bnEP3c4XyAL*o(GeR2H>vbTEKhr1{;C2Wf)(BqY;x{A8(Vuvj|G_1-GItM-M0*oz^-a(V{<yYK7R_`~@8z5#1vqjhx|)@Z4IYUp&Z;9Dw*OO>K)tfP7!*4rsw&>eXTZmSmLI-5=wkA|yK8<$dh8UXc=cC+K<E5#PmKG{prHLr$RU4b$TW*Z1Ibjv}2XO&_A6q`$&$;=r-D5?wSQKBgl=G<;4{en4zLh3b*wNi$?lNnfblyb+AYaCT%b1Mr%ZhjGkxEU-y+EGdyn-p1@mOCXqns^I*piBe9-tqI^6>31ji{fq>|#|4JU#VJeU3SYz=sPC<9!HGD6C>H0vnRJ4{C$h^BryPsEIuwESMH(cURkDVs5p!kVWu$gS@u^blm`*vT*R-Eu1larXET)uKB}h%MW(uZU)b`_M_ZS7)E3Y{JhkoUwabf|J@*F1?+nA+^6s~I`J;8~^>DgXzVgb1`6G4gsh+kJgGNtFd!Y&k$+9fBJULhwIij+P)C4VHHt(J8M&+@~i_EAz|KNh{Cqp=8m%0kd}Y0jl!_czhytlT2me$gE7N^`tg)!j_C+nGA&4Ghh-S`g?Pngs)9v#14KDFi(Qn&}0aA=H|MJvT+p#)d_ZJNJkRX?Z`BE#x?>t?UM3=4qzOiw^ks9Vi4vpdRZ6P4IzR34*FEV<<9mOLmCMfW~6QR_GN>M$>zhUrY<Bf`9^-acDNdVh*V_!ChwXlFR{)>`))b9f{Abp>Dt)H~8K=89l(+5CP=43f;vj$OkmNBzm^#!Jp8>MOO@s`#57h!xsSd#RdW`P+Lg+a}aSBccoYxlrVouc9P!_U(oDA6b*yRr^UdFtRcrK%!%SgG+8Kw;#U-@inWQ6u!!geX{30a-0zY-*glWlniLw5PJ2YSo{ic%nHr`9<5x6-9l{AjlgcLeLRZ}U7j0!rE2wozj)47g_WIkOANJ?lcz)Y|zK!tP2>-qD=i5-c4f5yt(|?>l{Re!!dCj}cw{qFv^v_S^NW4wdZ|P5e{%-T}zNmQ{*w=hEKKbXXKKuWlf%Wbi{pml_pUsQ^BnaLb5cKE#s`Tghu6xCwi{IUgelH1EYU_@?UN?WT*Gr#muDn}by!!6#pZ@yK*hpQrbeabHlN8AlLssP$RAxmigH^<^EWVe2*0n4|UsDKm+`z;`kIYx6M9aoX!pM$-ASfsyETtbeHAd?nvUP1`5YLhCTXGS>ez69{F#A{3SFK<uMAY)1asNd7)88-NRlV^ge_o!yn%?!+A2LeE3Mb%}ACY9q?Bear&GJi0$gUwOZRi}LJ0&qqIb#~S*)UpFZhU2Nk$~0Nm6v<58!VSpnSbIWb3R@qxkjtSkVfO(5ir+8Ria(9UGN$L=A=2VtPg*@LUoqT@4{a>#?22Kzj}5@XsjDA<NTr6pKkez{v2O4$>PO#g{dO62cuOqq;MsDII_(e>$iT!V7vpR09ENvSfuinelO*t%HEp&Jo|J0v%2w-r{8t1y7kN1$FH2(+0~k<40^KVc=cF=h--F(?)+x2ewTahUgihfy5JX%MrCNG`Kic<boOW#_jToVs`)dW|7@mfp1<zPtgvYl-1tv{WGVNl>EG&pdS(1Kes-K=S5G)UZ2V<$G5+R#U3;rkBmL_~<MQ3OxSsL#@fU%up182HFPa>-X%I}-&~~o*$oOjm=r5kgeC3WT8t&p1KU=(R&I3{YbZ1qKe;nnu=!U}Uo3<{ttX>3_*!W8WNJBzzT|7M);0ASq2NWlcEH*%lr-D8#H%?X&IdZ!yY)`P_e;DW@q5~gLx?J)1#|Qr-aXCK#y71_#bTTQpuZhuw-;^!d9^6KK4SpMmr6-4e$J$lzNRqzd9(xykJcLd3{vMWo^I(OLp6<`;5J=tt{?vi(xku2&;K<dz%zx25r-L)(z2#4%;<I(l4~Ra=xA+6nJ+RiZCv>h^RRd&NW4#KiB>cBHY$?7eI)ulOFn}0J0f%BW98ALubxQ)%$Uh2T+0K><m}HuJ|Huitq1Z&|@LUdjWjItTfWpwZ?NKKt>WN!|B+wGtN=r>gT|Vjr<m);{!i?GHSP!nHG9hIT1nYq;E$(<n+te5(D$3ZqARZ009BqlPbR_x;!pj3Oo4;$vg<7*CZpBWEA))HHBFme!`NmG^^mncLyCJ;(8KNcDeMeN)mROSditKrFP05U$LGp{ND6h|wVxO!df=iElSvo_QE1WrD`-c&HMR-Uvws=bFthyl4O2!|Oir82}yS){9aT%?2oQ1RZbPFkUWZzDI^+r8-M+$LY2$Eb=kcw!jQ9YO)TxA6&gE^9btJH%>@k7DfQ1|!LpGVuWKyYmRW)ILHIbo{`vrkBT`LVQthoyF!lz<)B6xvc79_V$qQOE&IG~Y{T597J1{Fk!|ahz9(gV8rq;DO9{lJzWz|5_9F(^rfC?5nXP;>fv#F0g)o3ro^WSdyzik}^H>gV=%&fm(|Kk{E>yTB@TE$|Ef}WOXqaw=B?)at5_TK%}xZVM&IfuNE%!)wTkXh#N3Wa1xVP+i;@H5G6ZyBMKVfy2^Jb>#p)#7|;XW5?6AmwYFMntwkbA?u97%l~=Jm2C_VMHBIq)lD8Md<It10!p0s(ezRF{>J8y4#UnFi;at@Y;Ld1Wm<?$c(;#LdTkVD1(Kjs^95mj0Vs|h(T3g<Z2uQF~i_3@xC2&s>Es>MKqHf6wbkmjQj@F4c{x-sZqhX~2g?W=CQci3VWTn0%G)s~5PO(!Dxvo~cF@^E5pD{k}|He1%eQ669&a>@L<>BPFfaysviLz`EB+eUi-g8D}O26!VqH2k7YH2X?s6`*QgP);pD8!OOX@w$8d@ZC7Q#SFk6^bT$011f);pZA?%dMb4o^nF@77mc-K+g&hA=w;sHJrwix}k<@-x$N8h`6W_HZ{1aGpa*p6iGP)dajxowkDEAG|nt1*l22lRDa(7DEHsJnqTn=gE>e^?}l_K1*bLz=+(JdL)4{osdjao)-=W0o-kX(hN{Mc5)e;aQmHAZ>Y$a3-lqm&TBB(JK#LqL&Rr8Q74(az!xQ$T$#h1Ona|fn>w}7d!;X5U8!SRu>0XFWa%i+#>Oo7r5IPiDx@O#*C4uTWvsy!cl3ohU7Yp?g()Ouo`d(A4ny4QxTlt0f>pnMvODrs1h~J0(1hD@ROAGGZLs2;V+N1(G`$Aq%@M(`ODUp}w#Q}tCg8_ZBwP$A>CYCX;#CwUE`GL^lEoH;l;~-F8Acd<4R5bi!cZMTH3bxI`$(e`T7U}J<)P?5qg^R`Ci=CTvvUnyq+X*cU;Gx~o&&$suIipKKOYglk&5H(5ztqfN=F8S|NTsn}na$>C#EJPlKVae&d-c8wMfS{FTROjG&oQj6dm`R*iWwxZl2Fy7N0UV`%1{107%py*kXt^_$^E*CO5ZdGXB>ldRd21w<|SgrqYDK9FF)mKV<IBupe>$)1eLIfnF&9c38$QDC%(uvd(genv-U<gWzK&iF<YZIwS2qLI&y6|NhOv1e{@#(L07!Dc4P6k7M@0!iP|#!^x+!oBl6_O-^CFm8pgiHskOcK#_UE3G!Wv8C!80cq(LkI?eakrV<IOg8yolsiA5D1a__U6h=|g~WY5&PDYzCcN#-?U83I?dqT~y<mEGgSNg2k(zAJ2$l7BT4U?^)lHxkk-(Ov7t_kM4Un@W0Djq%2hRPi3ZOwov#V^X2zOIB`+IN)NE`m~fY=6snZCa~C5y*k~1dF(!+z5DM!WLLdpn4UU~FLu?D1<B<tmAveYZLF@Wn;35Ftt_`Rz3JpA3ozSWEml^CgFkOwVt686{!T*SXq}|Ui$&5c)<w}7uH~)Hwp#i@b(o>1>x#&IW@My<$IY7EtJJfY@3VAv#me5Z!UuP}uGnZS)%POm=_Gf|*tsZDI9>y6-?obFI5C4HJi|mtf<N~!qsdu)*1a|Si4V{SYWClbKu~?I4%9)kb14lZxu97T3+&6vXozD1^4)sOJ7@u^$1wZxr?s?zD1gj-3Yb#{>6n74n!TB(|KmY}jwhx@=tC{f6w0Kd$WP5S?7x6iqjPQE?!I@uL#-n%e)kx{k$L#Y?RJMr%O+sTD>`UTv98C|)3ypy+Qlkx9m{rIt4?NoUC*WT-p&7E&cCO?Lhn?i#iGEn&F}JAt3{uVXvl$i@;0mk$r=X`gMb({NgKRZEecG5D!5Twl`>R;87U6pPgF54{HCndIv~9SXNzow!BJPc!5-MtDZLNWsYp)p3e4pDZBnh(AG58!#~F^^4eZ71>QWvKg;Qcp7kW#IG`RYB{U<zV`a4O>o#40ig)Kb%Wow>~<mx@WxPP8KjWty0NLapOX*0OSd>*taHK5(E<OfP3xJZZ^ragcE21=jVUZS5bkHf0)0s~i{=R(g!4jb<qxgE)6(?ZHOsarEnZuk~@C`s?)3ai)3x5-P3o7qElWhV3;Mv}w|O)%7Wy~ech17c@#WR_N0iKN#9s179g#D-6lBgsKhfn$OB1&|B!E9&G{wWN9(r1X$!ZL9{5J4J_fO$rO<0+|+a(VK)gN@dP!(SZzDN&8q{aR2W!jfTE78n!dhA!PKU`adx?wX-GQizH4U_#utmV^R|JzWfrsF>SY$2ByrEo0LN7R8ujv^z(Yp=zw|N$_Q#A@?AcMe9!<36dNP`4Owyv!hsvb$~mL6mn;JFu0`ioN<pJ%Vm0cO$gC@4_AdXXwm-LMbDVP~dGAJoaOWpUpPBy?Ohv~PF>Mo8EybzHb#-&E$v$g^EpL7NcAMh~%NKcFfSa`sI>`w0;54>oT9w|;&wNg~cjHh$Kj+0yQPD$}XY7nzeD9)Z5(D4ckPZTThzZt>vayqzklaqq7E<)MLtE(9{Yd&gqpET<@4X^xdxT9dJXOxl2|q0C{yDWg$7gj`zN!MV9Nh^E38}+_lQ{Npa;hR2UpHIWn1sV1?r6N44bND~wKp8=CNI}JHt+-^`Pt`Jju=WS>Y?}Eq+E6^0%gnZ?y(Yf1zFP^yyO!aORd4_a`$;+IvvxowAL}YMw#tk`3ez-A_R#LP<tHsEz-5gU!lvcB`W40JF96m<XRtQd<XF#d9hRtzM*^MI6ZLiKyJV}lb_!S?OD`kX1oNoQg@ec^hhd3XEz=1LGniGO~0bnxWkr9hwfmMWpFkhxg9|16y5$#+arU(_Ebp_gDqpu@2l=hdmyA}aNvAFYJv@plAruv&1?G-Qj$-59{JPhQHmDsef~!e?Y+qGEB-S6G;V+9$dLM~l&*RY>fQW7pU5e%Rr9`f8?sI0r#reJ(VP<a6XYUh@X&$QijK&+_X&32m6K=io~gZr{#ovj>e45>ueSX6QYGbeihe(dE)K+HOy|*v?Su}(P5ES^L!?JIOXSs+`k!~v4&E?yec#YnHq={UZA(>W&z~5FLb*(xVz-UBu(gzkbbuYkclkjv8^1UG@*F%c&Bqtl+!R*9DIRz)hA(vc;a$!YT$}War9sfK!Xh|C9)Auat|~iKO*BCgFUb|Wi^8H<l*?t<Gu23rnZd*qw4#^rT<8MHmU-OLA_0Dvv_EoXO2zC~Z}KM}z<nP@p8QY=VevK8sS2EmnI_Z(_HJPDOX#YBJkXYVVz(oc7Vv>`e0s=_WrMO*jK%&af_K5+&j^`ys$w)6v5oMsrgTCh6fM~<68xx(*2ld-c_VC)@x~F(mRL(R??9oXVsfOyviyizd?-wBAXz4kwWDR?u;9U{Y@uJM%*SS~8fC%yzA#$&Ac5wlnxhm$I_P&Nl?Oe#PFc&UWB??|neX~HKF}*3UE&QbNFck$oryM0{_yAwZ-V-@vgPhwK~^*r$pi1H7cXsNY=-pw@<^|^p^>7a++y*KohS2@XCEqAbUfO};eL~>s#!@mjKcI3`f219iv+NR{Zw|(S<1&UQ;1thu$YfosW2;YD2f`%>&!20Q#o7Y_tHOMYz7aQd3{4Z7Is3{H&Q(Z_nkMMUNRUISF~Y@EYt)_as^M9)xgOPOw7u!!F^GsIMB>RepUF7KSGp4deoOjIXl&Hr>DAU`PiYt4%Wg>lTuO6suBqp=N|`P;C={2LKe~TH6<nYL`ud2jI*R)J{a^XH3OX*#A1Dqo_{{Hiuz(;Cu}%q5MMHHnvViAC_f)YEjgfRsuC1n=Mqg(9zooopZFw$n4zRDN{Jx^s>8$*Hp4A*iQ@LE$Rx67;7uGYhN~5ym>yto1*mM4-KIns#GV&MB1&PTd252bhOTi%aw?Qi0<%U+L6XKrM)yCNBq){Ne@9DlAoW@e6-rHnjzW~Xjv_KG58gUUO88=Y@{3=@c5Nk)ypUEv+&Bv8xg@}<gM6hp!9Zfs5rGt3PooKFnaDxJT|i=irbHMN5hE9zanU;Qo&YMA%)j=OgGf#R8Me(Z#wb#{<L^;W;vi4lm-PdV*GL&fDP~2zOQ=g6LF3+A`j@dtV{C6c#!oV{@Hu2nqFbCt7isz@a8QwlG(I<;p&T4dmrGc#vPr@_8Iv3qLfZw=6>s!-gHfLu=N2!_K#Tb{186i@=p>7Y-rBfV@)(;c;S@#B<g2iS;o#I**fzc;T`*(9LAFmo2UE7SkNa6fNBJ$%<XKQ1ARgh<)|m1@VpT|YBQ+DqpT$w9(J8{e7N0wl#BjdIX*FYT*a$u@R?4an&%jvJgw<H^X(WHf8l<8}H-5w@eT)!Tck0RZF$*Kd50<G>_=5ZtvX1}8*j4;R(*rN@vmcdhr(ee4mL;U#FJg7Y$v%$ZdazxlTHZyRiHOawaCQM>)a}PdztmGx`O-pX``+p2Oy_rIDW{KHcwdT1<CT;wgELMfKjTC?mu8zajcDa0bCRVgJi8G$&AQo7KTSv>n|}2bf?IH2EgDNlBxJ=W%K8enykSTGMQ%%8u{-P$cPJ?bZ`-KfoeY;SQ2rXr_%I8D8H{K>M^I(@%~1sm?1?#0?6bAoS|JxW6UPFw9LGC}BL%9MV#5W6+17d%SpO31hCT@Tk*}3qafNbEIElOLvD-OWD#h&}n||jHZN6sLk-wylh8xDc-|;JiW0WwYw{xb>L~S=LG<w+xZ%;UTldC)KUzeg>zg+!wny@cH8jR;~L`^TfL%q3q<QN<(dm8zB_PnjyK@j9Py2o*_Lbd3-L8Pc(n!zD*qOdn#hp%Deh9|1DX}{&*J&F<N!NgN`rg*{-)9T`d%|u+DN5cwutLeByjyU%m9#`lHc_sCZepcy*$y?TDoi|a5=fKVZK#-lZHIsoYxtK{MNg_Q*5=p*tALZ|c(vPy~bsh#mh~QCIZzYkIr#2}mOS;bL>h8c0EVvhD83?=x-zd?5h;;k9ECW&u-S6uZ1FItE`2}Iiguc{-Ws0FAE#Cf>`GpnJ1j;Y8FUl`C>MuiBtC>AD$ItqbW$-0!s{Q4CNqk(-G9cqUB^qeB3?kf$0{lr5DIrQfFNswDXVg-Fg2)#XZOj*VKO>Rif>^oO=bsHgkIf^AWl@=NQkB5^OI6o0V(z8L;(&x3NFSyx{|@EAj_GqxumY?@UlFWn;-yH`dX}VUxo}j;pLWbt=NH>3hBsqI4CSXU_H51kh<3>ArLzwNMWh2ywMx)mh6TJhLog0PfF6lZtt3X#u$;K&%_0poaNV;=0`Aa6EvCi^uaF;Bo87vG8tM^<K+%nbEpryqR~Fx8&z1WByfoh_bMr_va56KLzu|rTlnqL>K}|_^PG+d%E7-J5g?m|YtyqMuly-*xW?<_;ciR%>nY4Mv5`o5ld7bB$C@~af)kT&lo?9ZKEE48Lqy;f3#hDo*L;6#eNEj>O&p54MAKCG;ebx*y?%y!dId-$`Cdozdy|tMMQq!ASWXA~Zz0uQ7b|=v8tZH)&!wW3VT~RIq3EtLPNKwl_GdEIVuFgS^0@8mzixc91RsDR3?}GmcF4#wQ@vJHDmLJ82S<Dn-XMmt#L#$ZKLbInZ9Yy7=js*;Lh+Ed6ss9Amsb$kxux#k)eZ)MZ+o^tyNGiXzwhbi(>AS=5Wivy$QcSTyrJF}Xp>6ah1OEs`N#-e-&TwSF1H)=UberdxjM|<b=?RX;>evWQ3ot|td>e~eG+3&t212reydLXFvSS2>C&o<aJ0Dh(Gf={TJ6C1JM-sg<L~kV99oW55V!h~=t?a%HlsN&2NbSWIOax~uRp->6n)i!r&c<>A^%gM{(ZW_$ZG%Wfz2tQCe>Nc2<k^h$B`}i7YPUsX4_9~)L%}b;t|UYX`tTL4ZdZ`jMuO^cjMK5ec4~cEVH;An#GtHDsM5XRBrRdIbv;3egEyB)5dpw5?21Y(807ok8PKuFlCJ^RPeeQlUrC7p7mF;O>S<oxGQl7tL-Ye+Tf#&@A0^4n;Y2cDhU2GTyk(KP!F@pbJg)HQfh=h-)ANfD!OQ_@G56Sx@3itEd}kGSlJ>g<UFPA()$opA{zXZk%yX;0S|tuMLPMm*!QucmbbNEOGyT%qv0SsWs=w$Fkv(guI2!rL62zA~+$vlPA!nItSEq`TU=sSe_Q3gQH;D>HTSM{;!W!IR;5X8s8ho=NvFZjxtJW``)2-UVyo@yiNJrm;I9#pws-gI5B2~&4+1|}QVm~M1hc*IXmv{SNP57Tz&eHmT#!vaeAtCY!$q6Gvv_rCc_=VpGqrRPnT=0%Oi4e%JG8H-A4aWO&ux+GQebu~Tq|b+We{Gok%Z52epYa!eU(9U3zB0`H?~`H1Z2q$P4_>Y2!o*Nb<BQrxOZQruE)PgKO;s7~^=q%*q`ss0MoV$8Egpb+Uwh-}z=Ody3Y|;j;MdM_^lncl6m0?6SnE!5!o<J^)L^uQ1z)gg5k6^xbydX@(G8HiGW~!@<luyfnO1Zcg&e+Sx=v#Cjp-aJe=h}d>WORT^aUanV#%{MCDqr=6OEn_W0MCfRTD|t3C+b*;p*yOgJz^Vu8;>{TDzh#19%&C?~v0Ln+ZJ<Pu+$5&2`!FNexd<U{xFbr&qA%=K;72TPDZCCJc{okv1aEr(h8--!$&vZ2<qa^J?H#8~T(V4PK?F#%d+(3sRY!-aiXU3x&NV8TtB*@ZMA0r}706PIoN!&Rmj>Tb^MM#tC%AwUHS3Nr+F2tK@Ney4}o|lOcioz8&M{Dd7q373W0q`CEc$?5AY2W9RC03`Z%2a)t%*zh$`nl(#NfaE@o~&b0@5@}k5#!s^mY2r*8~{S?a$h4%^bCN3lsgXp<SWx&uwMn=<H`d`p_KR&6c2tcOkLf+q$OuytA#~TbqG=PmUo<vI7aH6*j-r_(1QjF9Cao*WyJ;4pnGojv8eE~CcUJ(M}hj+kpC&iu*!h;bo78OpQpH2zyP2tXIPL=}Q0r(+T%Rd?qhgzOcXxXqoKI$WSCOZ^_4n*T)?%&}8xZaT(XX=Ga{01KLUkhK0BPq11#gCvG_Q?sw;R{C3<IK)xC`Gkv$vWjrq8w61pDLg5pThE%6Z~Ulg-)f`+L^46!Br8ag<%tij>%G$z<16%ISNc~_l~QbU1m9e+8)R+kx+PMuPkGn919**5o7Y0+Ta@X6#VxF<7Yrk^I#H5d8mFepZpGE3HADc%0&Uy_b){30C0YlhylV^9NF^BRD|9#?hEjT<0Q!KfDQy~7|ots9Rg`=h)=djS$^RJX$rqm{M#>TZn1{q7f5_x_O}QYV=XRj)lmCdjXjmbwkEmnNhe?_$_sE(3PJ^kVDh?{B|#V(_PRh0#tM~A(<^!bu^U&~T`1_{{nYCcsE|s@*3$8k*pw7ZpnYn3QSwEi4=uN;Xb@({;7G9vQ2<IgmoC#z-P3G+@u=ol_Y3WQ<XrE@1{iL4Z97UNm5>%qIEZHJcA>53*!_~P;K+)%$wPCstX8Jna#I+<$p!GcT6vbw+WL|Q<VWtW5MgQR#~}Sea9PuF3zn2yaibW3G_MXm{{1O$K2^(l^3YPelB2eQr-^!5s!?5Dhdd*~P^&uPWm@wz|NBN8%Soy^UPtuGBZP3Es>yz)x<e!5={(H_%3}U36vyQ3vBV$zA1xZgu}~gFYPt@1)=YVM|Hruysa7WJQFhTOX2hY!pAqT)V2`(meyK-56$SPsA{cD*`Ut{OHJn5Pn*qTmKqnF|P>qou*<nOL)l&?GZ4cRVp&1fYmGt18J7|;i6v#rA5(_l%6dStFi9|{*TYwzgJN)vK(NZCp(Zn3oY|WOi@|OL7gkKQSY;GSCL$zfo<9jy9xPs_R%;yleii{O{**pV?YzAvF2)gX<zVH1unutoT+zr+zyFJ_RbF@F!sf}z;^#|E>n1_Y>FrlgA&oQ0wWo1gN(n~f$AlA3w9|aX9@%8z>e&nk)$WgGc^o&>;6zL!(Fg;j%4uyIyO3AvbxMK#+ccj?f2ND2<_}&14eoaJW6Icc_?UHfj@f*L5_4k*r^mKoT+~cCB`ww8Pd{0I0cVV|>n804_JR|!J8_lYywr=cDa3}!N+MtGAh$jf!PRuS2MTfLV+T{o*G9dCAFlxq8@Unm_9V_&%Y-gzwr64}*4#o$k;`6RFhNIAPfOE7dl$UDd&Ksy_nyg^erPqP&B;2b?Tx3#<{EvFZ(HDbmZh*;na43OK_Mx;PsjNeDe6pU6ScLX!ecY?Tam1WT6FYbn^-oTz)JTnAU$g~9$e8|o_3xl=l}be4{KF1`eC?Qlra5a%IFo<>S)y<0T&Inzdv@Bj&h%_I1PN0qtr>4O$L1{z4gDHIa`#^2idc=#&SnEXkR)6h0Q#uGd2hA<e5HpCmTO`d)-W8a1!?wv--C{&X8%Rack}l?<QXwQ#IYePl;eSw4~PXi^jLd@!wxh0#g0bJd(npGkJou~@7M>x0yx(D9T{`RoFT6ye}#-1j;xu}V5JX#dZ(Rw(IH|#m;d$SZ`hW?pE5UU>-_g$$y0R979gZ8ou<{SrM`BXUcy#%D6jJoLGIaGul9l&CnXSwvNE-#)R+rfq1<Ds_XHIj<{heqyj9Or`BB@-A>*EkVm0N*eODB&M1_>ka~hy$?B)Orb%8c6t%G{A;>jPq;Zyp1-$-Jyq<-%~muA%q@)3n}Z}5-9KUn>ys~_<Q`~%xD-f^h;uYF`@s{9-(wUcmvcm%%;1iV~~57h>DV80KxJfl=Tv0do1Yy%lz*-1(J(b{nw3?n!^+6T<6$Nb`k9&;^(raA%Ls85B34d^Xb(bq5Wb^1@@>!62t=hABOavFI#PF;Yis><k2zRvsN>(p0$oqPa>Vsdoe%h72?4fm9n)4b5j@tCi@N3;Ezi^G0$_yO1boA@&4CIrJNx^ovN-EeW_-_-PPY?*m+fd~;v|Aq{IqW!CB=jyqOWBD_BIbr0;rE=VLUk96S?Vj^>7(&R`X|u0$#nFKn{EJ<jXZ;(m&&rwm{Qk}FeOt=$R~7L%Q71(_@HvQ$%~6DsWMm^<QVw<-bRAo;i`r=s#bdS9B;;#T#FK~ZERrv*T1?$GsWQl>pLgkVjw_RAig-fY(#2s8x@Crod?!F??>L`j|0fc}Y!T{-<e`?RXC=i#V|!paO|xE|t3n|YQ(YjSHRtkr63a6Oy8*zLGnca!-OoZY2PKQ;3@LwRCv3S)Sw%-i7OTbyGC@EkLT_q<0#`*TRZ`wbuv1kCVV?TuFi)a}*nVExrQduLV|x>0dy@)#`}1vt-$wXtgx_S?KKxJrror}Ik+XXH^G$&5O@Qr9fbI8}09*Q`0&JsXT6l$I+ILrd4L35pM0(9gCgLba0|B-}Ab`PuXiUtY94$zem;Qvf+=wM0BOJgoa|y2CMgg`^pizGI=d%K4)u`DPO>s@Hi~?)|kcIxH;u`Z|*M;1!96Z-HYfT2s_-D(N%#YE<KXVJdx+=p)N<}t8I;MOQvYz4EzcXdKLIW{r#o>_l{H_-=Y=s>8{388yk<$r9zFfYP+=|MP5${TP)R{P(yHJcfmyU}I`Lx-vd*{xt{MlC)f4aFw8qvRL{1#-<Y!;*DFrsDcBbVxHm(pu<-KmA{+ENwlOn2?7%-CFz?A7n4>H|;fCf%}8dhJ|y&DqX!RebA%@8#JKPNHk|#R0xt@N$I5U#^`0^0M8NH+4gO?d8&IvMu^WjXUE7&ySf;t@*vrUvw9uYx8SxPYR^nc-KFnMQ3(CJTpYoY1^ly)UGS8oxND@cd3`=#j<!+W$o50^XF1Py;X3R?3U**mRAb@__@B?|Nc_gHtHKdf^1sSkmeT$f<XeS2t?cESI|64-gQshvNI(V`{sJQ5W?h91|^POfFkl-nJ#CPiVIC8P`-p`Tj@p8FAg=qLbD;Tdw~QCIu4bMihXH(@)uxlQ%+HJpRNJxD>`9x1vKso)Oi9(<JMHyn;qssy*y_kb<PMS0;?(Zab4a-?;)Nj)K(2)PP`9V?#RUy%W$D%V21ZLV1HGB({9E)qHY5W02%@3&}(bfXhq05=Q1hCb2v7On<Ywo0)!ijiTXashw9HS%othuUA%r@Zmrx7s-^Ah{Lav)wY)!7q?U9t;@xrVxkkf7e*eGu5bF5*8>PlAZv3Vo3#+Ib(*8y-u{97zUMG#;7eYK&1lA^j1u`JFWa)MW9TC!_NtK~TytJ+gT2^$^9u3z!U$y?46pNJ8RA=OD%H!Fsh?xdrNGdG_7@G*-^92|y78?2%QD5Y_6ozw2G(I$=U35inWwq2>>5JaV>N!?LiLLaXx9az6SAcm30`0oWSW-?CJWsT&9$ibssy*O<{Xsm7BjI8oS&Kp1hC>ian>5j+TDcc?g<v@^FFg+f3~PS~ab#+-2m;1uGfI#g4Rh>`;}GgCfVQ0UBBGw13%j*lziQN98yXNSl7d;YyVb;=DfNOWHjK!2ikl1%m}vQncGkFHJ>^^C>*Q>U$`z3aQ2L=Mbd0gEw(Z0U<He6tiO0J?*=G@{9c}T8)6q+olf#AE`L3?;Z&Pxqb(18@w8%+(lN1EUBDNF_g3y2s<EGM*DIppFKA0Ryysdud$!yjZ>BCjgXPT|^14H5VxkXO#iO;&ifAuExR?GV+^0B<UHT9{P`Ys&yL6o;iAvX;{Q`UxzbAJ#Sp*7^27}A8MwGM+Mq5<~S813rbmbcsut#EWU9xK9UD{-_&t?eV(kd40z4e)z25P=k>!s8YW0yiqC6I*z46a~UZb_Z+_sT#F0fp5v*lJ0>Di-nUE7U7<Q6HTW8t(8ad4hW9oIx|dAUGk<`6#9p16ks0?)x_5tLJz!Pz5p%kVhw-yV}gcc>rDM>0Ub*2Tu#Y^_Y68D8>pt-CuP>0N%0wah(4&Hhxk^CBY<co$QQ_B64`UeW<^1VD9cri5a_7HlrtD}@1KPZ1;UY>B-f@689uh&6=DK*OBrZLq=iB)Jr5efH6Nqs5}bCoY!rq<%GU&AH<Cm~9?70gDoK2JZGs2|wuo|x+)EIlsj?Bgr!YXFEAvLd>@P@4YJZ5O<>uU=$eIwr`U$B@>i_dY^nbG_HwqVRIa}+SGgn%`=~4^0waE*iNs|CR*Z*zQNcE%yus@Rkmj3iL72qLho|^<{EInKaMD9!dUvF}tv55Z;x5a;jdu!nR*#w+iSc(6Z2FU(-<=-4XBA`C@<V*E)*<V9QH)87N%&h|<qwy)_U(m;><8dbbyI03^#3qQLt0n$hlz(aL&Zu_M75!f<(C$M2_p>Ql<}dvluZaHfIC9_{dqw|uPGuM-(nv+v;c@xa6hauUR|?8Ko5>S6kJPbgiHXR_eo~Ey3c;tCbqf7y`+7!B17hvUqD<owR+R6}857lF<m^^6KaHa-jxijHQz2WQA-F=osucm2-^8S9ZBiJ)`sqV<ASjJwniziMLgh{ma%HMHiz?3P#iSl|w$=92F~(j`nN$TC8UYj2Xv-^TgPGnn_EnZ1rqu4pT{|5>z^1($lGtO_2WOHUqprDikhoz{DcO_N6+DW+4nDZXH9sOD<%5{u@}tw#Fd7HUkpa$8sF`k$;#nh*wnkbm!DWJZg04}%`Zf5e%>dO1i&V3q{3$e}M3e*%CBM6~kS9O<M;?zorRN7-l~?=8&H#t|d!X2+qSQuuq3lcH25rf6Rd|piSGfn%kaL7BF@*+h{0Zxn2)*z;4~uu$zoPxi7Ou0Z6XCS^#T{}_*3F(OBe(`DcV&&;_Ag(m<z+A|hro{d&`$^8v&fA_L*3$bT5XYt@<c7#%x8zhQEd{z8Sww@x2Rm}r@hJZac6g;Y)k;~KO?ZWrKt~wX1<axN!IC~)NyPXlPQ>z@;7>om+_SP2uM7Qrl(zyF!2=?Te(i$dag>?T2v*^h+O&LeV}lH34KK)IA!BQQwXg?X}|O2eJi<Tkxs>44VJj<x`hVV7+$r(kkiK(AgBH3W{Y&c^x-1%_wZGw{;adv<Va@Is!NLw-&2iRmGW1l(wR4E(a@#&++ntDsOm85)hY?M{lMdAEn1#~>fM=YJf8X5q9oFFkXhiE!<+%+fzia`O$9QI0-kCa*zzq93gjmr`hlrGH}z-13EufTbA0Wyjh^s5TFDQ8^3|h0atd6I`ci8aqfU?M1?_P+MxCJ$MfVf|O^v9Hi1QZ%U&&?M4Hp9sn$NR=x6p=TpSM%&s1OuqfLli0nqjOf?!LUjmN<l}`5IQ2<IR<$=A|;y+1ele?vu@jXWl+aMhltJjk$}Xw;zhPZ{{?)&`p9R@xtK;sd0q2+)Q@0w7BHEDR#9^GdfN^pFC%~P~@h9eEx7@W3?VIB+2}I$1qEetJiv<3pEP+QhUIJeRWuO!`ok%Ttk<f*4Suu-DGu{{Nt6Z^~CCh!{1Hj7iViJe3%p(M5EO6Q!d+-5eH|)fpAGj`H`9mbQeB<S8^Y7pTCYsxObxXX1Zuc;vj`=n@jsVk6c3zbEQcsTkU834*(Q=7H>cPIh)IQD1Q9304lwlqJfJ0lkLcEjaR^0@+^0FdYe_%tQejKwy80%Jw!7c`QUypsxt{}hqz%zxFk>_hbNx|$%3MXx&iE>q)ViS>aDx#1X9DvSTwTpHOaXW4!DPy6{ac}yLx|MJlC%*<14-`4;nJelzqOX?9_CodwW5IrivLU#$weavW&s{K;jKXYIVt==EmPy@<PDS6fITx;OTqSU-|&AEJ{F}5+K&`&!lTZQ9n2jlFBg(N_2|mKmzX|v5Wv{;5x;xEfkX)2KWOz6G;+Dw2Q|Rs!h(%X{R*t?tBX=L}RJ))Y4+DgAzqpkE~#^&yKvLm8o}vdzIiUHxRiKt^R-(T5rfWnJElVEAbz4736;nTB$j;XebWMkOoQ5`EG!)mJ~H>GSsyc1<0rCc{~1q08g2LW2!Ki<cU;2W^=+V<OzA8qn*8z6~i7yq!3m8JD++7$X4gf{8Omqb>^RPw%^?RyJG(RH!=S$X70CQ{vikXocVVJ36WlF{%1vxu;lw;3g_H0$9_98xrfi~o5RlhZ{P0ZokxRLCof$-o4hI!hL`y+5mlP=$?F$s%4a4oQ$!!bcOlDyW!fz*@WGQ8CamVnZ7&@co3^9uQ<0RZUNm!qdfgFB>}LJAZ9*{l<rCAkHiE)HrmASu7Vfv>XFv6v{r5j4Us01x?l5hLO^+R=rucJ{f^c_8{B+W7MgUev$Z>eFC6nHgluO(hRkald2luI(>ZdE}m0>W}Btqflh@rB=EI*Pc14eGcJ|c~P2ZN_!2oDKn5!hjSpC?a+_-S$^Sw~6EamS>)!a4%Am>h-sC}p=ArwKI<c&}JYZDn98xF9V_8p)a0OM)|h7cPe6+>$6l7KZxUq}7k?;_j8uScA>fmqf>kB|$7H2;Gx^8GsLQ%%b8ip2mA_rp<s4wk9DNT+u0a|Hg+rVfYsyJydOp2rrA4qGaXszdc=^p}J?Z(J}`}SW%_a8&$5zYo|T5QJyh09jIoRJgZ36jVBD32h=!L=%7qrAd&*(Jy6pvbi#^}_l{e$3{5A2#^@*(foHyvnx`OUWFK&ptymRIMkoL-F|S4vedHsDSkY2oT<Z~Ll^@}{Y6()$gMJ(WH^hos^O#Xd4IxxUpoS_7ffTV*yj>^UPqq%*eC2&r4|0N3i9*6L5BrdRw&D??E0mw%Z|KoABK3X8$0)%)($|Xdcu)Dt4VCwrNFJCv;xQf~Y1mv`GugWGQb5dm1oL#Drh#p&F*W4)Co&jyg`sy~`^Qf374WGj@y9%UOR{ykp*?-ahM7Sf&lL(+G78U!O-f}=j8Mz*PriJL3AmQA$j(W)(+G!Ax-(F_ml%1303?<c<Ulx6dh$}z{kPg~koQa;RYV>h3{#QmKRB(dTY#66`AX#V8mNeZ_MKnR(XA(QLyl>xc2$X;O6nOAq88A7jGBqyc&KWrLP~9g7|_UVE9~gm=V1Zrs0zRIQZ2AMP^vaDv<KNz>U=qnVv^}4r2Ei#EBOOnbinKd^U;8v9PG?=Ubo!IH^&hnfr-AU{bnn8LGXoEIossNQJRzK^L^(xD<ngbF?8^ld)UJRJZZm+w7srW9tfNqI{(K|m<ac4zfDG2*_ha^b~Z>J{UHCg!k;JTBl#iONoopp)!5(t7sP_>vAJNg$S#JMl{|O*FZ0c=S#d%QQLPUJp?|i~{r2lnw`m5sttn-JC9QfxbayN;75Ze)(vI+(fgoHD8^Q@Pa`D!Rg^5(~qHx8O1<wgfY?LH0dhezXRm1c%oM&;&c)n39Zm~)QDL^968HH<88?$dDNwefhNuFcUI-v+fn7c!cpZwYHd!tt`#K4}PwSUb-el0;sLKt-<*6<i;m>icCiYcA$t5HaARM(pjyF#bR6pyf9Urm14?1L9SN4Y-iw5T}Ezw7*a<MeyB|34X~dXKemD7QfDh*wuhUa`>-BJTQK;6q(3jNZ{|mxAkZQ<<)?XZ<-fg<LtB9_*B+7A>0(Kg{9GZ+)vlM8hB=-Ohn#Tekt|Axv=u94RKK=>s>>qP?2wjEhj1@aT2v#4*LpSt#sFC=qDh6-{V=X4WSXL!nS2EJKM{($`ZQK}5nlj=;MOG0TOuDqIO77(ukmgVfUhAa<cd5VBc-4)2h)$!9+DgK$S0W8hu2&xHvAaYySx6s1T(+Gk2}64SusCW)dNVsi2cR?Ez0L-wG9MY^9m!2O-K0QW7xeNBKnMYlDo`k#El{>hJ7FkP1JvXz8-x_?pWPPpVHvn3&eoNlFbSL$|*m0wc2>q_Ykrye=Yl7QVeN_QK|qP0`?ZsN2&@XzN<cO#W0E5$0^{flt2vgQ043cchZ|KTL@GJt8GLL`sSFU<eCBQ)G{L^y279m)Bf9VgQZY~3B0CqV-X#3WX@0bnSUO5B0)HfsvK6CaT0a_Y$;3*n0D9f`~92M<ZA2B!&PrfujG6QcRJg{1b%Rribn1PA{A*n5{>S+YGnXuV=ZL}uh;=g$2&Rp-`y^nLZceXmVRMhxl?@RR{UNQ{hx8yV9AyN!{sTXF+3f<~b3b~hjy*#g;~G5|3EfjmN%)e=Z}fCmWFU^4&)AO=Xl`o8bC;*pPi_BmZur*1n-N4xgUjEsy}u^zwm`+biM6hM)<KpIjN5*X8k11-4AIJx6K^@wu@8gyeyLQL0SAq$KP%19{Bd7E9|n&}*##ts_|RA3@BHnD|&wzpPy2q$+EfBZWiKFzjeZ%K#>=$wdmUK;|Gn|OKs*Wy1;vn^k|u<}=zh095Bt^ACM>ol9^(`=*J{=(v)Upvjle$6~j;ta;VJ7G?&rd<~QaL3JM)}$)iN)jV_x;VTEHicrGV9kHkg1;S+{5iC-ZhWq<_UUA`Um1?!_;tW5{-2h8xPO1_ZCRy<kBq&IufpB}cnd96KVfgPG_`T%9MYGtw++8{h&bS4PdrpyMY@W;wa%zyAywkd%;6mf+%@thD{pS`Cpg^BaJU533WGP1QG+ZBUqIvLGc@j2+rU3~Xxx9){eS-mGiTid?flSx;XRM<2p4@${^|NJ^&hVADRt$SKQyN-U;Y=~`R{MYa5#Uab<5==FX`FbhRq~wKtK)P0R@}OG>_B{wTgpW!6IOz#%&Qov_y<+%QFE*3i)h=9Hmq3k~ejRl_$6pHSi%R-w$|TpfS3lS19b~3PL4LbW0Chlh{zgAy!ak<99L{rJqG32hehD18GDt%2Il8;rp6s2|`6)63L6Q*8+fbm6-a4l5;ga3jW~WZ8Helx}q;UQxo5Zxh*VQB-?>BPKQW*3nNrg^#}<Kf+-RhbqM}5(t_apTmJ2oHRpZtl7b27YZ2!42gBD2z&d)}WB95mx<~<Of2`~wfpifA*@O_+CG6t$GeyS={67JQxSw8e@sx)3Xyn<zH5tCEjgtMY1&{<(CvMN<k&`IqHbACI>=t+BA#_9(w@mFiyn+@z;L1w-ev|v(zDHT868~Z!=(Gn9$@o^T#U;W;?FAXeL#^2yHpD0-?54{JhbDef-GA;MM>!qyy$=uZt%tCF*E?*Y;GrGA#oqL|Do+-Z+0Xw4_dCA%F-RgM^dIifc8M!k?qLTpY(1Xn3jH`5G|<FC@cV%`%CZwMqKzL$?>i=a^4`ca%mJa05kyNHRJx*RS|g(dlGYkekr~pD*wqpfQNZvWov$UcBl0c@hA77MNrNness>Dl=NaCXKMzdk@r%kGwB`7nYgNx+s+ONchi;ApM{nSyP`>(+`FE_cM}te}6D6CYxIu`-b3({O@CK6irNzphiqqOaa=pwn%81=#QfMao2t-pj=g)bC89#l=wTWGmp>E}*0h`kpP>Q|{VhCCSTUNU;kMXBG)Z9@ShxE>kW8H^|^e_p{m_k!_wnz6B1k%=!BaGN;F7bUJ5Wkhuvl8=)f4#3!#|&!Cv0v_m+%4alU59*yX#`@148F3|==MRS0sTyd6>0pmzAHWnH7B7IC3kjq{DzPs#VRdh711XvQkz-IRKKM$x4NXfG3Pg5WzLlY-kNTa^6t)p4e!QA<9;d7Cjd1YL^7C;yfQ134|Gkg`kEq6OhTia!d9sQQhFRXs2RUhTV|Df{AhVmqa9YCv0-N-Qj*$1z1l>7oJnQSMI-<oj<2BF5$oGYoQ6<YmJ=wYyB70MM_=XNG&&Y0d0Y5d@DsbuSDOy``#-Dr+Aj!T^~K<8KMuf(HD`fq6~%ujy6Tkk@Gf*!Tk(P)Ir;o+AMQ-^axSk^FZQea!MQvp@|G?&9Wy5|KWs0N9|Yi>F!(q_Gc%`2G^dH?Oe1OxEyr3GnY*~}%xiD0>7|`ESKU}!;&ZlAAS-Qg!_9M9(GM6XLkbV)bco~VQZP=YbklTja8k1GcK|JIet|3!nGKgqIHGcT(4*LJJ9$8WK=T;#@%N|<ORGoH8-QCJk@rWkWJeBj0Hr-}s061omsf~#jc^z*e?P^t^+tg69OH^h9{AE5geIRQXON#m_#{S6!eNj|5)Sw|7R*cM9=dQ>o<QeT{Jk9Tt&Xn`;X56s16g*_mzB$+a2;(R;E1)|dm77dJHsMlT-}=!2tDDc)x=tTsEiVTrpt)jOd5arAO4cUpL}-~_|(+(%I-|TjtSD(AJs!8)Ceey;!X1i=p_7^u_En+(rIiYUo6QaPTHPZ1Fq?dP-y(Dx2lEbl0lzRtGK-o2PHq1XQw#GETN3vsF|5pNg>3zjER~P-Wq+5^pR*9PjMv9l8_#~S&?)}N`GTOBpcYd+t#}yBY!zEl0ufZPgMm@Z*H27&^a?ix05rH%#<b=rO85_4gw=Pv$=Lc!9|^}WgMiih^LB*lF~e|N?f#BC=9f-=qd0qlLg75ub;xD`?|{XFNRC)SP6Gkg347ivE_~az{XAIb<aPLyreHFZi?h3eW`I1c%YW_?0)7@>Hms#-qKrscqMMSw7{U-n&yjHk;ckG8YCmvFV>Z=hlYsNi^N4Leelk>NH8KZE|Q#>L`U+{^C@ouAV_>3i=jT(awpzeIT6)6VxojBX>8vY<62>qKpW^jc#*lBps=e)C*AtmvwGA+SBCIFP=nmemNg40VN_O4x_5M64G)jZe#aUrl9<fBGj8ml{eGn;l?%Iz8qnY(b(M>x&e;9(m-sYD3+uMChtSTRKrkv;SW>~%_C_F0rfGDg)lZtde06Q_)x5FsOFuQXD{cRvW_~0#5p_Ne#{(t^i0wQsTNl{|5x-E0?B-1iLR8EfwP@`A)YqhQ_w3wp*1CD#vuo=%v(}Bv)=g)vdziIutgV~RTKDko)>Y}2fccHuRTI~uX}2d$`;ULoP0MzD(1KRJXV#oKHivmP9a|9~@YQ}IDz3J*%`(@V2@4VXjd2n`@$+F`2l(TxVeS`wu3S)Uk}`@BJgFtR4btr0ANz8fL1fBV$0{!_8)G(R8(XLAXl0YE=i`(a^%+70c+<-bgKRY#rVZTtg|vovSUJ^hIT*t<)v1LHOu8N$sioe`uY5%#@!IqzqU>2~VXW<@);gWo^64s~p!IB4^WA*?z^K6r^iUTM85W|40s3vDFIrHc-gdf#glyE-$62FZTscfC?ydX3-vh|pme4WfF2Y7OK}V>IrPrnX8oB;K@rr&@__(8dEbo;Ocv3XZ@-^>>KwV>Ow8__kGIPu_(M{$<SkBi-usWJ_Z>U5HaaoV!w=kkIt(;(01cTf%`&;JRmK!t_49gZR&cuqGRES}LZCl4=%0r!>zH~a6-|iW4<fwfOt`j~E1oNkQPVeiU3n66^Ot|rJ&rR~Ey-QTJkM@h9vtzWZO%u5(OS3CU%dJhl7pghio-s*GS+A2UWINV4eW~6>k+7K^JZ+!rt~2QO`jJotf|nP=oIV{d<@gZoBhhjgA+D#(W=Tr8X}>ndgfJ6RCYB-0w{P6HJAoS5Rvo`o)Cs}SJ)Jyh8eneY|IVve5_hPTYF~gcaR3RT^mM$!ie+<$Z5MbL9YT5*Y9Uzz;#CSw<_rL(k}_2M(7Psi3flNGMZm%{5L_xKUciLgk{;GlnGbw>lvRA2&E>Wa+@#c#4EjhYqp*Bq`RRv-XIl~HQO?5>TMI2%o{ibR4h(WkBjr;(-b1Z4`xV59`MO6TFY7u%xYH%!;11PMzwWT7=t1c48{TO-vh0s|cL--YoxcPpy>GGI!~K@mDHesCByZW&!6_hulox(xaCe$SpLAS5)Khy_wQ-yO?u#t5>m<Ut=n*qe#&6pb$8xS6%eA6B;kDEiM+h*v5_u+l0O45jzecSi;e~>Pj#^2;lHd?bHU)8g!^MHUqYB5?&<tg1YzM}aZP2!^A9W%9IQ~;DMMHYK=Yo(;hQGJu4lYUg8jb>1hC@x_$QMLYiT0@@0ikCmm$k_UZ>XvgL7^PH<t&!mda#7CYQnlZ6u<5x=h+egO<Pj4A!&>{b0~lQ7dMC2uganI)~Ywl#aj#C{=BvDNBQ&C6knP*YfX;d>{-8*;NjL$zrwb?nY7+aT5l$;H<Q*c_2(6D*3pdhb>6IwDkjyQ6&fnj8Lm6D8X}~+wQfyX(QqKlh~<g{0s1^JhfHe;B+8|PEiD9y0L3w@F&cDM!&WDirQpXr2a5{}Gt*bup85-hq?G&QVT0iGGh5Z{PRv+e{?i5bl6mX4x<h&&{E7W5d(`QTIA--P-^=)^(T_Fy>Xz3M^;G`66V?dAA&H)=>53yNwMZr-*SX>Bc$<1X%=~93FV}Fz%e8SQcNfFrf}{5q3zdsJie=@Jd<o)cpIR?+`qOTtqP#Evw8PFGjjzUq<Fj_bp3A(4%-wZokJZjO>x%VTyq%$5CvL=yUuB@lo5fr~a|2O%9A78cZSsC~OLxxEA9M1)JokPLOZU>H+i5s)GL0{}pq_Z1o?E_N^FMvzm&MOmZ|9QNXSm|}I=|VAcTpeH)%zOXy?EH-<LSkBm%h5Et><67{_{uaXASFTmpXg*qS>o1Qq5@ZMt9K@_Wa)kKhydtcggJ4y=eA&;@qn0&zTQwcumV(_}P8Xr~K5@)GT%}HS(Ezyt?S#%jQ+n-MQ0ic*oD#VGGdJUw?NYM0N0(hJNzbf=D2Ix+BUPCqjF7K*0>Gg_L7D)WK2AS~arOk}UpA0J=92;HnlpR$EfhXC_){2Kfs{d#0BVt49@008G^&3K&WShD*`Mca-q)6^|<UiPQs00xPu&G<f!M(~I4XhqZ1me5;PRr!0k!?LLx7Ddk3K^kc;yv37Che5Z1#iH&rlLBl1iol5Xu4XOB7-do-6k-HSit=*SiKtH?fJ&I7hi~ENv>c)?lOJz_=h#+rbeB%)Iz$3)tUDzgLA9mhs=DNG^+~OqV-F+I3Drva03CES7h%~J$tK88^RW3raoQ}Sf@;B~$xi(sCCKb_yV3o(*L-;J>dX5hu94M^m0&M#P<a>^>1WcL86$)OeOlEwja`I;aJs=`UWNWA~;-ZcJ#%*YQ$k2LJ7*8Z?f^cHkTxS4{qsw5gc#@x2`p3r{UElV<NvRl)mI!Hc+~v@4^Mt1XVDOrdkb$iAV@Q9b0|KQdbYXx7Jv3d)xz@q2Tj+6g4R$sg5XH;$NdrfidQ<6E-y6FXBOg_-8_Z51tCSwvttAte2w;YK`#>SQ(poUk6RCoMWTcDK=Pj6vk&yXF;aniIau~4F<cJF4b8L;J(21$xbFe6AV@wu(d8tt!*A{_K29;%;E!qh^tIKT|D02&(A)(PC@S_sl`BlK+_*{B3?1NfJSJW{~<wjb-?}8$FD47wZ5;zV(mc*FYLeB(QSgz{mP`C~+x-2kSrCq+0Oqad`g->(=fWt|If~$Cw@XK4yT-k6&fQ5ffNYCd~-@t5@U`5t(qwrl%GfpB(h)XXIG<7Io`!=M{S78UmSc+mq&QRP8m&xT9xy?+jN+Wvr12GTiGl{9EfgFBm|4%jdaUe7m86*+=@@3@~ei+;aOim0SJqXP*_uh<1%UzV=c+@5ZNeQNkdq@8$NMn^r`*Tqrh%3txy<ToA8_L&as_}eocD}Ml)v)0Aei`HJmtRZl8e-`lVs#x3#2!eU0Kb6MHSExd%BHByu#nH)o6v!TO3>*ajL%i3$j7Li6(?WFui!*)>_swv2myVTCyg)@q<3`$a&?u_UZ&BXfTD#*0k(aBPY|5+$fe6#ce?NyCQu^4LU_JIKhPKDWOH#KF)ow3mCWi+xDnsb2(y7lmc84VxT%%_{(iJwX#O8<!788Ly+%Z5Ngdg{tnNFbj^q>S2t{<ROXkIfsP=6$L&}7ukkhI4>I}zRs~aaudGRV;1X7o|B@;5#m5!1*X@;YDhj>#5>^A{597V~U$~K;oLvUC>nK4h2X6pnBM?<jJOeV)DQ9ZA=9r+>B#YvZ>aipfh#>tt&zsaQW`q8we3v2W)6U9j{*wr+yvzXP3J2<VXK;eD_ib(s7ug}_Ax=-3K7S^PNwXsz-5iNSYq^65YYP9vV|MJ#Tf=WMRNlpG3zpPa?Tv}CqT~)JIRc1-&3+qoVEv)&4g%vIHinWys>o1m*TwGW^r1f64wuV<NtSuJSD@$tpYS+_$`K#HnG~BV2sY*7VX~rceJC;y)Eaih`yCM_FN>cIOElCB4S8clzX4@66bc?-;Y<|bR3OZ1pC_pD06;s#aMy1S`+WCwdl{{@!xPXo>Fmc+MAWOR=D6?ks?@D|$L}@S^-`Kld`Ri|exTnRr2j_f+ZMi3!BT}PZYpY1X#CQfu#Uh*ONUue<d@0zukQB_OSASx|2}*jTrrivkN{(gXwxKtbxDtS@tB*N|4Gn}H+PbhNI+#x$oRpn|8c;Ly_~Y!>nGR@KC@D4rV___&jS%Rg4X4u@N`hsmU{!BUvSJ@cEvyngsovMEtb@^gB1>J-uRsKibEy@$F1WZcW%N_Cw_4d6%{beS?!@_xuh(vL|BkI_dwnaKuWUs#x1!DYRy2@X3t7f#^-Oj3Odqrxl^4qwyBqZ~O$&<^vwP=0w0Z3&^p9|@98NZ&kqe@Kam9?&a@n0Pmnmp3;or4r-o19weD{jkeSKEUzwUlx#&LRb^s?i|>XRA4i7`df#P$u+_>AN5%CG?^&9Bk^4SOvYhU9xPyb~2%wp9Eg58dx+TY$DC$!FyDpjFEND)T81CXc0jX?g20@e!@~2)vPD=mj8qBD8NJ?VzEth6leTyis|w9J4b&f^L$rkhMDHwxmXh%^kk|n<{5Y=i&~D0@<C{Dx+folGUR?GTwj<6SgNwRuJ61Br&prl`ysHMC=v&){VMbWelbLs1p%I^osP>pjA_l`7`FJ2nAPEK9hV4X=YI&2<F1FqRvgA=!4A-@_m97AO@O5BlloTl|FSS9qq5(vb!Ie-JQgpR?%kRi>X~(MtcjRKKGWz{g`>(pWS+yEmgzFNv7@5M|kq&{A}SvI*Xpf**$skp3<oAc=D3C{PLgte|UAOKc};nMYD<UMx!rliH{mh?Ga_B5>Qg!T|$M}tb`EiBnc_O1|iL23FyWpz{5}q8Ob%cQDjSUa^hP8TMV8;n$a||7?6_;%jNoU0L3qi;H<J1w4?f>@MoAWn`kRS0x~JQDXYqT_4H{}bOC1&@st}yg>kSJ0<1z$p&f8zNDK#Nq_GD;${9CPwn8nmYCC$xCK$USx7C*s(j!vKN%lUKtp;~KG-GU&1bu7S&NlI8Axql`0|aOxC`%P{a&50Gbm;r#rdrNHCD;sHHLQe(tS=16{`U`86K_y%d09;y-?cjx6c2Mj@lGlruNM@bB}KR1>}-&meut)bhr%fmOavuZf;3f4@o-&J+_v2w<_s4Tq<7rPQP+f7dF{5tTvHs|Jq2njiQ`;R6YoYfabNl`)N@XB#M`PPo}?ollp}qIeE7MB&Q2Oxzi;{Q(mmIg<ipd)Qq}oyzsMXz<-1NfhA{SAzZG!Nlbh-miToyBNidYtLiv~Q0=gTS=u?_<4Ajt}RYY238fb;dKyb`7lrJK}Zp#(6tNDgB<{M76(<Fz-soc*~4sM=uXqa;7lyacClT^?unLm=sYf{6Ob!Zva(>-%cJkW^@_S1=)yQWnWRFq(sTzPzTi}g3mQVvOXO6>(Des?FGaqNkk5oGc;&~*AQKcwp&kXgUb^|oFS_*^J(Vq0?>*e2>?a?nE2y}2?=-f>#g+*&!;sS0GKmCc6q?(~gxA23;ng&&k)?3lD{GhNWtxk`_NF{G3SYyaBRJ{4{5lh1nB)+vvfkB!_Mf;Qy5=KXS}3x;i_AKdlXjfbVa&TBpX#${}osC41rEp-)7dXUKH<ucX^7_92keB2)Nue)D@%1$aV^*1r7AYl0^{<Pfc)8y9}zE%5F>0+g)JYpnt1TJ+Z$sf}*LSB<te6Z?aiQ)25Qx6BZ=>bCdp7>k*lBo=ua5eyjSNJ%3&ESM#E{{E?JDcY<r*w+N%`hIK@%a(Y{1cG~s9BJYzN@SA0n7p_nLI#-Kd^7IrSS{2S2ksWFfSJLO|DaLM8&nK9ds`yS(?3+LCdp6jFaAAhC1?`-Gfy2*wM7HzE^?T?C_qeA`JWop3oY58YszmLqM?bhy9BxFGCHBGa;;0?<k{{x|rMQTM4t%5(6ee2(UMT3~TR0{cPY>dFkN9it7)a-t(k!K-)sL%CbVKTm(E?<-|vfzsWr&$%K1pnNMn$5L3wBj-fIMtjgk~%Mz0D59oP`X<^U!2tF%RQ0O2YS+SXn%T*2LIDuc2)r&nVs4hP1bh!3v@k<BUhN2waD*DcZFRKItY<larjMt`f@&cqt8{+7sHXf5E3dJ~v`B^)|5UQR`WAZi&HFKxzd6?u|3}m{He(}D_kt$!)N>r5Q#6CVV9b~l-z3zECxq4W}h0=Oeb(KM;AEh@(wNaWdkJ2xED~@)^<B{VN9RDPm#m*pt2+<YPTQyXBh*f?)gt4DgMWTgf&q6{~zsKijcL)29<R;bFdU1#8Myfxk&TKB5Zjxf1crbRn{GPg6_u!4h{r_VNZqMz)*Tj|c1w4oU0AsETBA{U|0-9fT<$SdWC>cxIx)>ek{Y5~#Dgt_t2!AUbP-xqnxgerHzLySYQ)8P3BEOUxrP{BbTs*n-kNv2^#zQ}CY{ndnKZzxS;c{bIeB2mlCLQ`U5Dop?HwBolN&)89CN~+4TMOU*ytVL63g#vSbCZI(Nx|HtU~W<{Hz}Aetkd4qV7_WK7^*{@znJPT%~vlAGuMQvzrU;o)A%Xvcu^3B5DS0^nRkps?^vM&^C>2&!2svw!<g<oRf7qp93msiQAfp~XQMRA1t}Pl=~ybLEOc5XDVVKE!Ax===}g+izqdHd^w!GHbzqjdG*wRI_bCF?O(HOn*)^8gK1c*+H4}kpre>ccP(~dX|G_#i7|yElhCNfLgDMBrZfv|qe<ll4Ey=FyzzDeGmiJ`}Fp~((MeUc_Q=UuTT>k0p250&+RRJcL0*uLPsB?o$bHNeZq&%t`j1)^we|mR8nqwvlGitw_OPBci=lrnO|2!3SnQ6kDe9_6DF1(}$<CoegqlAcov(xDT?nIE}l~+5zym%@IbAG|$1*x1-_GBr!Grn?u{6gr)zw~Dn3|R={TvLe|f4M9a)13;%%;jR{|NK&SDAaadyg2KGFFlSkeVDm84Cbg&A10YTj8m0+*$A(d(;1I^g<Q-ucE$$uZa#LxQsxD(B;7SXlBQ#(gU{OY<dykTn+fAcLamw=+d?*XNM^-rk#7IhcZ!De5)Db_$`0j$6}{PgrEkcGa_e@^cbUv&4;!nL045p|2*J{YCw!dPZtpfpPK+cQF<^*%e1;kq>IQI8D&r@!v`<k71nJ0&KbGlpX@YS4cn^9wKFhibLG}?a!E$-q?A9D=2QYLAxa?77!SS#yaJ`OCFe=<+_y?jYQ~uoG?#lhroJGZV9@YXF*tzg5pUyQrR-Up|m4W2kl$L?<`_RCBvpYIESo7Nc+1I+(#5Ba%<rx6E2m1Iv$aj-^EP&R;JvrC_9mlw8UCu-X%;3g{gJF$Z((zcLG@x<ARrByN7cU!+`gtPap<Z^_7@9Z|O}w3<iCY)<Pej-F_*fCdM<4s=cvzo$Zl&rCwXfb#`WePJvH?G-16;ORMg55{r4`rKgz0({=Gug5X=?WPMK@t)6OvpMOAOYq6}wBV7@CE{*6MmI!fbXUgP+)a&l#)>pbrJsZx}%UFqm>qdyjw5A+2H6l%S&nt_KZlge!!3h{wa_ZG;|WP42^ZWiT`eFvwtyzEuercwH1vkI=AVB^S&-zC{FL8CcEQu4hHq4JMH_C@!$p3h*=&^{OWh0uPE1&jBq+$;GIyRZbNS-cBxejIP1=mRHsu<|cUn;#1#(R9fp)mdBTZ2FIWwgo9qByaQ0pgpCox2wEUKWC$O~tr-F`_`)lVER;DJH!|$O+|SL6BRV<;lZlKKKEO%54B@8CUJZ$n{4UIYiH1EbXEg?T4Sy2(Cek*H-9WXFF_H@OUW79o*)onN{SLk{+(sdmq)?;4Xyn&aKOWEdA<?ji_FbXV)dswd73NQrwWOR0IG!JX=a4_e{pPh#pdco=sXV*<)(=N68$01xcs<d5(}itPr%1#j2>2bE!97EP1JBvF;Tx=(KbAqc#o9Lz%P~;%V`pL!z(V6Kz>BFegi8%?I2m&;0NrP`58q^e=?Q+;?!H|I_ErI#4a8^9gf4oIG`%hz@2SJrWij@5VbfYNEePlQzz+C~V+O$ad0+cPAb<JxB(y7ia?@}}V6jHYfAb;O%F$>11X~GjFg{%(9m5=63BMLh$GELn^*Ms;&D6ExIfSqTa+1j2o%(Ctf*AHZrjb3|8QP~4rkA)7u!lR$a~#G7=!NP-<Xn|#=j9BvL3uCGvJ_VJ+zbJ8xtSq09BgLjK1H+y2o@9UG6JZ<-%01pG=Xj^{?c!OzswW<l5m;PB-!N9s*FIi)LogaI&K-z<TCkcy=-kGJ)X+s@_?*^Z%-`lCxE#egM2?>dQCD;ifJRF{Nq3_e!C3a;m4Q&O?Br1D57jc2x#vN<7(O`jO}|u{P^Tczl%@Svw$4O@P=`dBr$-zZ3Q<%ZvzEl;5^pIFOaKLiR=zoP$MVgM*3{!3@gsYJ*MuU#jM3FT!OWOtnCs=8i@=PxRQGewg4Uiq=#WFKVaPv=}#xgoUgl9msehl`wl?t$O)q3e8|^H=Sa4_@B^^qExMX@mbRfk8SwJa5bI=9nvI=JA|yzVt(A#YZN#qRw*=X_=_5@r3XzgrNJawo)AJ;L3#0jHFd@MBJY(S%FIcAIuv+}H?$5;TDW*5Xh?Y@=^*x49=+9pMd?XfB=vZ2aJ{uylyjA{)2A6$8uN~xuc5j+|`cT+YI>7Q6fZcXgZ}0eMD!Z~U+_U>`AIP<)x!=+7t9;;32wnE~h?@2^E(g;HQh%5mf5fHnnde7j|A1L(Wgjn-zu{n$y@eTv*5{bHwpz802*=0lRyi!8XYnM=25cYAJY9co9?*nD>Xt8!`$yt?<@{a#e8zX}4|L2VgDU;m*NQDZfG!oEG#wFOdq-c{fPIsw7Ja$EJ1&@{>8$QB4hJv#b6h=8{f<N?DJpKj>9#Os#5LDnVg>>l-5REwcLqb3bYoK!QDqO8?!t3p-Ju)?1J+=pRL`*IYS!@^f7D3%DJHILTN6)Y<&(+^`Jwa-T<QkQddG{2ZP{4#V4!#8Gk15U1JOx@i*soiIG9Q9ro38t9E;iMAA40xmk{*FK;?CBFc<9z<{l3C26kTy#<1c&;SToYlAlbqdFL!k2;<it5#X~FCZ7PMD-ECd`U7`(c!oT~kA%~EK)aTB;%#Z0dp(nIAX5NM`#>cI=H~LF1`KRaV|~5!q~=kN7e7}Z%VW`tT#5r9=J4z9ZEbfR5RBG#D@<Z$Z5L)1@733C8)n2bMh~aHb_a#eCd`Fsd**9r;LRXpEwwu&8`1`OrdCrsARIFY8Hj{{(+rhb(YX>UG(;+<2<PL;&Muc@aB)m|(8UfXa{XY-IeR&C|H)K?d&Ro7tk5d+&Y1z`b)8ZeprK@bb-AB)t9aQ$4J_FENR}K!L_yvMl1rAhb?NWhgIaSwF3;*y4*82AT)+S~uHkGyTD@q`HDJsmek94{Cd#UOE!~%qSv&%B=_Y7VTn9@><7bg_nwv^722R_US)L}*<n!7N1n)9Nr^*^>oGczO)D?q}IXA*#HKC@e3L^?tpd?Vs-5Fy%2Rm8->79jkd{jyMk`e(nf`XGw+i=sx%>9ZFTmwuwd|P5Gzl<SYh4FJc)Xo@(@@HMqy0=$32%Ic!Ke*pBIT-{lopgXqn4rXdOuF(&1b$cqsJ0F@C}zYnI@G;@xhqD1jj_5Kw~&)bMB<uy@EZRUv8$PgT^~tN=Fgk-;ur){vnB1$q!)MS^np96!`>+hPF_qniY#$6R%Ud?MOms2WVeFHa?m=4o)x$*r6Z&#_zG(_W$N3PDKsWqwHRnqlCcGcz(W9rDE`t_%bfR}^79CmaVMP^?f?gGdW=8r%6v{*NeJr%J;u<Q*rSY^f1VP-E0rySSc#l?rJ#b37=Ax7obQi}_sg@tkE$7?UnBs_ai?6|N>Hlp0>mhh1~Py;{0}1LEcq?x*2z#I{n0XU3}xf|LvD~0+0*;d<|6@}zm(>GPR~z>M2A1*e)PuDLHnZ&f3XVv<QZ#oW`_L!$(8;0x1Z4IkKU~x(ZJtVZi9p=DQ`WO`G}dNAC^1DT7+R!THq(lpC1!AL<*(Kx>uIUwU37<^z0I(wG0#==<i+{5B#Ph;)XF6Y5&-37w>28A`~NeZYQ|AYX<Uqxrc2ih{=7cxusg!ZI7nJo*o?4vW|e~@@y4*Fz#|j!eU3SW<1)bvRX4zLZHB{a5;V#{;*z*oT86dsvotBU_2Hr&SmJuUE5o<4}&z1Qw=Qn;>aVCk~wjjQ|3iPv3q93g0&4YYs>?e@Gtz^Ux0nB)(XV7CK)!_*G`I@Wv_o}tvI)@-7t4!vZ7TfELAq8R(fTS=4{FimcJ6;#74gnVYe>!87qCm-IFc$nGZaV4z`%aC*}p`Z{K>x6O}=kFhayvTQS#@R5|9tOj<tkK1mcZOTxD)W+h1-#?u4U%SFm57cW8TFkA9Hmwcn!LaUq^l)Bgt3|95T$Pz^3yzhFS8S%GgOa9!2cz0>xZ#f27^R~60s-BDIInUszI^NFmIE(<gW+pPi-K24|RR|Yb4yl|P3NY2y)tnA`_7J*gi(IM|O!=5wG$8(&Gs2LdBjx+B#0F&$Eoj?QomVw1#RSpp)IAXfnEoYN5(&o1+T}&Ly|7lqpWf>9vX7_ktGgT@^k?xw`SYmKPC{<jq6G31Eqs)eP%w1@$&_eEE-EkvR`6rokf(@&XHLcp4-MmntR<+5=Wt4+HT=?hV3H<)q}~Z3oN>d)%pAqvn$Ph0+6;e$W=c1?rN?1|%)TyjXgprup^S*(y+a|PRWT0rILsZ5geyFK3xW&`z%Xm{Cyx{-ZJ;Z9NB(w}hDZ5j1JCiybdA0Rw(R6%A_GZBa=M~Z0K;6!eFM3A>g>U~J<-h^*U-?Jy=9nBJ9T6o<e6R#-{Z=@2m*wy+|mQx%$+V6F-oGnyC3MQ9&|h}8{!!_;aaZiI6l&lJ#?M#sfq>zbTWB6Xbj_9Sf#+3<&6&W^o)z?(Z#U!Z7F@w(mZ{|h@>oV&wuYmwYpKQZZwtKpSKpiweXE<b)#C{s8%<s)r}5x<5}H!RyWJ-k43TyH<FcOy7s*oR;Kqd{d+CLiVj(Xzm8g5tPLmD(Sde~ZS~kzP7NO0abi`4C9A5LSXE5ARouahXQkhx_y#kQ57V8K*Ybh{m5p_y<fOfLHz(UvhE;e!K9wJ7IeGGF_NU&}eBvv2!n3M}&8SxT>>1l?)Qq%qCU?rYij~j6ysk=c23txLTMn1mR&mVP`l+4mTY4mW=C>TeRl=1&c^2YVq*Jb%Kcih)YB>3N@l0W_gvI06n1t_iwUf#8?8O(DS9W}5Va=b^#KJnW*0wlp{;X&0zOeLApZ#3E=*@52u0(_r!2^R$AW8~r<VKbVePv;dj@=^#%P*N5^Ixu-I{SrL^+f||`Bz+{7!mCAk~#NfdQ$fisp%bV*?!vCp7N36#4_^lWc$2m)P2sIx^`{XF8<u?{PciX<J3_+yOC@BH@{@iUAsrWaJ*jplr4AXX4cnp8|>>2+;PqqGP%3aqgpH@pH3NBVb<m+>?1$3^!8U=y<fh^i#O=U&irEIyy~=b&Q-WTXuL>rJ0ET#Ea+QvwwpDkM*T_qTrxrT{-qZe5{9pE`#!V!{wp7*0WAv_|6PGn9Z}aluL$KpdDi)=Uf%Gc35@k?DWHnJK!dlITrMp58O}<YkD=PhN*QWg<rr#Cu31tJl;Fz@Y;rK9EsDBS>?2dktw{hP4oR#C-hGOoF_A4G<-e>*q+G>7bdhR;A?ye(5sViQu)%CYpfpO<hMc0RR5(6J18)#1#Ld}M_E!*QC{-Osabk!ChfQ>f!gpZWU=^^m^~0V5ipk3nfkNW!;u2b9=@76a7~h35ufj&kqIg=h43SdmfJPBmOD~__ebqy@^78CCcd$Nvht{`B%Fe*{)Li!KY=n>~x6gAwv5pXdZU!d<K!@%HbFJ^WtJsJuBmN51fM~8_xXwHYeZvP~?kd)yy;GdIiY<h`x!$*&TxTlZrHeOJ=)0?Y0q_EP={b@V5NF<EKoYoaRAiROE0Ea$jRdn7t4IRW!C@ut`DEokm0Rh4hlg%*#1QpL@Z@t#vB^XpIK*(*pq!gNb~!iw$=3pQp5&M2Q%fw~vxp`_!~lIhJQ}<<R*yfmeFXNH5Zu!LptfwAf`b4ggwO0M1h+fLVhe@JE?RdU_-;c=9*dsgIfhRxc&6U!5xAZbx8yE75Ax<h4?0v#5KgsE*=BN<pq=rt03bSqEwKUv!EE)CQkEub`Nn&^`-y>x+@XBeLHiLqKVt0PF5|W*4AK9Hkh&+aB`Tw?1;Pu+u2ou#UVE%`I{A>?yL88KqIQLE4wfO*hS9|XaAG~d6|GA`9D|Gs{!C944A8b6QQd1<&KM*Oh8(D2JHcN?cY?k!4+g)lv_mV<62@p5oNJE%mfGp7);0wqy~P&KkUnie`lB>#Be~ayHRNE40VM}G@*|Yx<xNQl-AU2dnQaP--(duAfCj-Q-(W|(RZ}?N^0KSswt?${HYT0X2SqOND#L@!OI8?h8lW&F+>02Bfok2ENM@o`jogMQ>;Jt~$8Xi~TV?U~=dFcrEqrU?TWS1O8o!msZ>8~DY5Z0izm>*+Kc(^Tvr!r!3)?W2`I<_Q)@yzr71HG2w?@8~G(#01^|HYhfjEsWL`?EZH;1-$t};oHR*da+UDEhfRM1Bj+oFQLsqbd@LIwSuHFbBXh&~;>rsA13nmf6dlM4EU+Ie2op%+DWHQJ*5%;zgAWb|^3qGTyex%{chX*~OLDy7eaJY{V?RnYVF`)MgX+Y|9pFdZ8(EpB!JGN>1DQb$+2rRq$1LBzBQg4S2;?(Fp!s_6@D(aTTG_omWX^-W*u9)9s+J<``N3RNrA+u8gmOL^gX;`oY<?f^W5At6kF0wdgf=x4?ClWORNLh^Y*{Yvqhnk?@rXnMUM&2q!6sQCfKcyIEhW7Tt}dFlPKtZu3x*DLEU-@-d?@Pj{|rt-Nb7w)A7zb4FiQRVc71Jd%!mnHd=qU`)3E^4=nGO)7jr!{po`*fb@u1TMcz0_5Y;d!asUsU9MMOl3bCI~M*{a4r2{kfX#yXx!jxOl~E&3v4OF-E<hhpKwRQd8DlDy}av3MZC=XRj{{?PvA%-*YcIVNM3|>y)K%2X!n|fO7+_5jbJ`xZC66$*?w9oxoB-l@HR%WjUDWE7+w<**54DHDP=hTB~R5>1WvKY>Y3eV<9U*sS<JdjWL-G=87BhOgSk{qFpBaRW_b7Y2?p7ha~w0gg;i53FPZaFff?v28#5ANpU`AWkpvq{>=QDs&s2pmtuWUmfjyLNi6MS@|S0_hS&U5aWqV>A5T^n1xY`cR9~ckp)>i!ApIs>wvm3}rsq|Hl2)8t8l`48UR!dC`=a>0`gR%xGG+@Z#?C%MB!o!C4E#7P%r4su?@dZEL|@O$$xwkR^^h$5w8Iji1-L0vtm_Fody8s=)LCCs0L%Z1`^z4}lfU4G1U7nC&bcSS{27GXNYUpkXu&f88>^j8P~L*T%8u((J^}~Ov2#)EH$C6cD-tz9^sLA7;xjI={8(=o#`RP&;Dr82#VE?SgrTZamDiu3Y=t#@-~;)NltP|pUSDyY-{aTiCnuZTql?3lF1@_<GU|pMG(nTO<<caVT?T!yoN!lqJqAod$=bv@jymTZL_nj(ZBTA3$FClIS8a9$TtLe_f=(>Y#=MT@nM(WsfBsDaW9+$exXk!p;xWYaA0YR40gSQ3I(N$N?<rH2JqA_F5ld}GRdh|MVYI$x=jh2*m!yxUr!F;_BGEA?Bz{x!LCG{x^Ot))qsTKn#<#T80QF1Jo=LGMa?bKONs_T@Hw01hLo}_PQ04Hdyyb$0?`0u-rqTn5$V&WsKH{wJkT*7?KC>!zqS`~TtJUg1>hti>5Y1K-#orp(M@c^n5O!`NsN7nK%sHFO(4Yc!FCSj?AhGQsOJMp>CI=;KMi{Xf;bnZqOf2fR++V?19sVdfLfEp`v=IHx339tzpZXOT=-4R#uv|;pAK4Px#&}zdY)2sL>q9Wj)DY5SGU2_HNvcD3-uOm~3m2n3+X=HV45b6TO)((byE-R3a?N?WVCRpSq@AgPL{nZctdNYzDP-U^qT;>RK6}M&ToY^_!CM<?jhRb#kfI1iIOY!A?;XE|m3v$*^?6ouVCUpbQoc=9W#G1*X|BNPn0;i$Q^j?#{}h3a(H43C-u8At^kg#brF~`F8gmV?70_Hm{-VtVyNi~*b3fiX3tZD_#SC9&(uHITW&!T_avn8XO`NtOu}rUJ2!>$+Hfu*^Hm=Ea77(b2yGo7<2Hj?vT;he5I>nAU9;0q$V>*4nV3|lYM(I$U&>_w?BCa|FBRdD{U112Z7}7CYHn|Vw{9CNc03f$PGA(-uV2s|gd?4lM9+<QBstmz!2=?*F=|&)yOkL}>^T$1*Q3+uM;AeMGC%Ko``CoRwF~x21$@Q_uZJ*47wlZ4|gg4#;yM^D;f4FsBNe)Ef%!zH4(Ay$pymtu_@nvP$YGdDrU4%eGGQ1pSglwA2P=@ygv5Co4`GZs>8I_=imHT+pg|tR++(7?9#>N(@Dz_llZzuy2ttt8Xh%n7H<+E+1D5|4a6;-RkWWxe|T#o8bJA4EUQN~FFpiRrqO3nE*JlN<dIte%o&z6wHg53B$Q)``BXMhfY^u|4M9S~rpW(CAJLL^=}Qsz{8xk7eEc+E2^qKi7WP9b$RiKX(%dm^7?XD%vE`L=aw?QN8w15W!NOe^qbFD}1r9d*}$kfW&HdMT_E{i<0=>iC(YPP{i69Sp4%ylAp)>_-h9>J@h8y+SD&DdzN8R7b5Gg+#K1R>Caf(g6v@U}Nt{T5QdkoXR$%2o5z!7`8dB09taJs#!A%zGG&l@@!gFz@x9Lt2FQouVzBr-d6+pw9vpCw7RaOuv4{cVimG!Foy5>iNHx>9jD<cCFXEHsVLrQ72PmTFq2U9U#R}|R)}O-USE;Gmh@#ySM#L=cB+=<;Y0;{%NSCy-<b+FUA>_^YV#G9S-4&VNtk&tFsc@IXIj|k9YNBHREnvxNH|+dEo`ZQD)90%A?%J|<K~hIw%L^f9OyM`=;2cg7id?rD7VlzF7>Y`@#}8xPtJW$LzAtTs=hY%N|e)#CVsuH2Ja8%KtB19uSXwplQ1#~?9X{^9})KI|MS-_8C^{_Xw}#;>zg=}>mLUZWS-NsQgm7=8mtt}S}Ywd6W+ApaSrSkxP#@MKVh;!sB|a;XTCaclZ8p7EYha1#X^P*1;*6@^gKtbGC-hM8d_>}VJcAfnM}HZJ@h2&`cJhf?T~K;ejfo0H^TukOmAf&zz(A72KEBwvRf`0QPB*#aiX}T^1V$vtsTB*3h+y7Wfw%cQA%3c-!j-Lovl&qhiel%k(f}Y#U)C3E>s;xC$fU=$)!`8B)P{X@{J}?Ne41J7Q#4zvSsWdk^R68D67m|Hn(Zz*X^EX3<#alpLT!E58reUzH7PVes;q%yy)VNa>U$eBb41~L4kwDAz+*R{7ChGg}xjK&o~%^q|-+9;D*4*>cTh5pArZ565HjR0#)g7tgFd=na9@L<#w2^OOV`@#@jgwxCTQzW8<A$w!yZ}hHSjO<omYf>7ea>ek`XNk<z@XflsEl{AI3r`g@8MX9=7!tqZ(zZyK)bGL^YmZg1nb@Y!=KP1_tN&~2`w_~GAjzvG)9Au1jQijo3xjZly*l2rCU2(Y*G?17dY{9UjSC~L%lI~C~{(*L6jUC4bI-vnb%Rf^2j-gi-(4}2sDmL5cyLtJn-H4<J?4h`u&3-!vUwp`ghgRmq09ju0=cTN0!NZcZC7$FCw%{FYjy=uS@$`YZaJ~I<T7x&oB9Q4Y8pl-EIvS$J<-N<tW<-o8SYlDRa@POO&l%w6+?Kt7FeXE5ZDFCb7++j5w6Q&$F&aX>|sUnb`7?_UX$aiP`BK$9}$c<cAL+l`j`yT4YHCAhq@879_IA6WlfcZ@OaCZ{7o#-9*jBn#2fTP$Ul@8}IT#(i=BRM>ZN!l<k<GFk(p5roXAzd?OQO-g-Wl^MlJa)0Us9~I^Q(hDBc@BUY@Ri#fIH~ILd?&r-v#>82k=Ue<=aHXZa9++<exy^nN%Z*Rt^EJoLVLF>(d3!%?j5)pPmkqkrQs3NX_-F!qx;bV#~NdoBN~u>WQBe)Y~80Rd^-f&=s;mO?inQ8>V%0=akUjfe{iHozK?f}F{tqG&VT@Av;93!Y4(mYC%1+V98ZT756VAp)nJrUt|hE*mFIs%&aCIWx=-%mp33u2==jffNT;qjl6wiYOAytE!xpsh#1a5hh5^|K*rJ#3E)mVjy=B5so<v}0l)?GO7d~9C*__E3<l_FUkxvL?h&CEwWQBm4a6e4uNuFF82gJ2`a+PSSfvXMwY(iJw>VtF=5$U)1VD>fRnaDlMkV+4}COWnZr#cM60aXr+@TP?o*U`&wC?Xv(FzeQUfCH}`PRnJ*y>DD|$Bly&XCZy>4+Dn!9T;Pr$Rc(>++6tdXWqNnu8IF%Y_pn7GTTS&xJ=ME%{<NKP1v&ubM-U>wWy60WL`ETO9#?{Pu?;QV{=A7<&9dXVqa*~WQ|%|v|R0a)~KVW8SEm^uKitYRCA1*Z!(DoXl;^&pG60YvrLP#?w|hy-o~hG(QBr|C*H4t*Veju*1D4IXVXT>m8%RpZ`Ax9_iJLg<*FJlMP#G6HAZne1SrVMLnyZl1Ine}tM24GZyrL}d=0#}4)Ju_^KRF00838g02m1*s-CWL*m>x`H`qjg07rWdPfi=#sND9ZOtaW(2XfRfpK^|-$zIqhk=}=-i;k2BZ?K!~NEz<9W#|l|CGl`dT1U&CMyXb7zean7G^l!wz#yr5N6#OxTo3m#OswG^J(pKHT2f<HGQ%>kpb=2HXq=%_<<GO2f?Z_G5EaVu+|ehbphEb)MLznAvYtTvbryVqlSi&_Gg?p7A{E1p1y?wgIDO&@r=I)fdGJM7W73F6_X#QR*AR?~>0ap*HwI$ka9Frc+^IY*>xm#0X+&hrNg<1d5?0Hq1*x2ro1Q9K^1qYJv<e5ct|h;`mjtHI3@Bt-#%%b`w?P>xc|chz#B(#dLix|F6f<TTE0oU;s&+;B|J^gODylJxU2QcSQ_N*|L8|c>c9n&vQ{;tK{kUNlQucrTwH8Wul6#KreVMn=3D%p^e<RZCBd+lfvxQo5cyP6#gf!~?(Gq~jiB-g2<-OAp<N!K&`F)Ryux*r9kyWM#?NFn{%xR2*ckl1C&878S#722lBB=zzeyoT<ocYeoQF8sp6j+a@?HiH~F>daR16!_5h$0y>!AgQRsLck8i)Dl6`!*i#@TggdMB=>knf1=Rl;B;*ZyXqu4fibE6Oy=i0>AEl+c&@9$}YL(j(z(;4-d#gCma6}n=HTcP0MsWw%yoamq7__>J4)~0adFkEZH3zW2M$b>oJGQ)R8<<F>7o%bR&!qVRS_^Af|SroEW*MMAR(5ucQOCHAk)iRgb(!*jeV9=Lvv{<Bt@|_6IqUBsv471m?EiF)m;V2#B1%oOWxQ*F;06pm{oQMPJi)&?Mn`4O@&DRX{%x;(&S3Y({DtlCeu%IiTx+8*i|*F*mr4O6N)iAC-|6_Sww@B4sfM&>ll<v!={J@}K^`X7zSyFkt=&>WEBsa&Mibp)bqZfCBN>&n<5e+j~xrWopXu5uy%1njc02)&3UvBD50>Wy=#L#K1rY+>c=2Bz%E62QW%unJ`K99$QU(^(u@$0d*TqOj_sZq*2=P4%<gMd&1MIdoYichrob>b8Odm0f!%hCIuY7<_&7wa%?2QFV_<^zsdm;1Q_?P@-|p2z~lyK7a8xYqVj?t*}SoQ>EHcQ7XR`bH_OFeT^6CP-<oAuJV&TpR0-(@v(&K85^dSnqMEz9@>_rLNib4%jp2OFw*`M|St;u{S%W#tEJ%9y=lB&%7K<WK8bxUi>MBq|gwiC@bO00phWO%Y@8_#Mx}^7(djud#7Gqsw+66754+MxX*WzAbWylpq0hq3sPYtzWW?Gc6AGH^ZA!^5DuPl=j_n64AC_VUj_(;9-UjTrTN^tonbar^;;Di?j<5nxIjAcEfTKi2JR&<am{iW6Fhec$?$J>3vZb%$i<U&1^85ed*Ohep77&;)K7ryOrOujQq-jr%Vr`-1jv(Gon*-B`=_h#r*7PWOnMhYd#^BiSyi*G@AZ&fcoe{{^dkh3pA%)wkDv6n;W(P8IP+IW40x5WeJQ#sLNQ^fpun-oxB^U`cEpLV?FW*~r#SjPM6v<Nwnx+tvvuP<e^_s~qa7V6t*&$FSf5Pcl&t*rtW?U9f-4RtG*bF^oIPUO=PB@|_ea*TOWGvE^52IWE<e;Vg6hkcFn%W&ncD8w4%a~4pXzt)(SaHZnyJf>X*Sc}xFGCLU+FFS#P;~3;~etE^nH#|f2np<(1%zkA11R9I6<RDG9Fvqf0AY02Bfqqt^N?5ssnOC2ygkwt>h!AaUnd6W}z85q$*!&gij-X+@b3e`$2!=4r1h%>89ZLzKQ<&RVH*x$QUrq;)RMey*)!4zAD17Z+7O`*b<K?k+buY_QfEG0r=o-UT5k{eO|G1+i{;~;3aInrogBh({6)QdK=Bn=^SgSUQVcf_vR#qS1kL#L2npx4O1f?x)?B<<hDdSW~SgdXVp70m@xWP1ek*D1}%t{LcHOnbdL?fU)Guy#m>gL_J%?*-SOTKpVp103IP+In$wq7kmzEvx*-n7|mzy6!uKXr8}?9q{ju}6bfQ1)$Q1th{n{#SddP&u>G+Lt5WvgWzR3b^lF*%KiVfC3-pok7b@3~v&~2SU}o92U#O2`E|@6hK8iUW7T3IfbLun-#lvEbC*7RHjjtSd%RIs?J*^+;fBeQd)86ZCNa%<oJwV_FA0>_#A1yE*&<~v2c*nc2`b_?BqUiDJ);t^YI4Tvg4W`RTwVa+_k$P>_S5Alq<*Yylb+!p4z2}xuv<v-S2_#SY~wnw(J*jofP7P4T=Y!ZOpUZ!#<eFf;deCX&&9u28@=iP9rDt84(pWrFN6CITt}~5Cjtu?U=T*5Vj+rQ>51^kZq+>8=^G!W`n%!J^{_|scGmfA7ub3$rN_j@yq|Yl}=)r-gahN$W*DL@LJi|LT?eP2dn0NV92J`yyCvFiC-xsrQD(5+pZQr=7xIZ#Xo5tq(7lFrM$_@ZEepyNZ}+6Gxp%p^MTA-!W<K=M~6N9x4LJ<GTkx2cr5w#UUU;Wb9UiSCcEcw9}zFI%tiEZKxSe`)ZV=UwZzDU7)(JG%8lg#MYd0YdSSjp@Cx{RqT$O*u}!cZePnUWun&9l9qs6}j{cpfRdz(fuUUvK53l?gn5{q;3vh^(J_60$aR5wziM$`YNI79i&GqKY{#%Bd*kJ#^F2_H6c3DgXfI>WRB4VKc2qlRSvi<T9kpc?J$wU<sC|t*90{jQTFHO?6kM^d>?I5k8a4brm)9gvhIRQr6M`qOR8jm{p8VYcOvyvLnFb&*1M^bHRqfeyDM}Py?>S|>!+`*Rb4j@yPo8_0940L!aNCo|?{e6&e=U(|7&yjEWoDvqGX2?(!x|jNhh(o3cnD|O!GNm(Rz=mC}T!F9ztswY1awBC^v3e~NiO1dGmK)3NJ6rZK+?jgtqUPY{+W+iB0-$gB?kDUwQ*MWe9U8(Tv9skC%KKw9h(6Ongb$YgPn;59S(M&8N$+eib)gfVr*}Hx<V(mpVI?fRv*G;2Nj<K3(PK(yFmx!hI)pYd`vn!xHP0rS?QTbC1F;^NNuI1E&w#xKvcuBi_DuCCp~SsfnIQ(^-Ph70Ezh7^Kp2jr1>@cgHTe^k$sb~104thrv%6`V{jp<<-*A74zRi2rtEN{bu5YG%Puau9H*X?g*_b>JXb+ksBX3L1*1)u5;?A!;=t1C+sG3${YPI9o0NyER-_GI0xAr9dg)QQgJ{U7#0Bp5PWTMAKff{MEO#oGyEcWOTE4_v22b~K+9QpblC|3rJLCgi?f31{6E(2)Gui)U(>N7$beNxP9f*Os+{MH-bK5$<hy?xz2jS}=6iqRj+2u12Pd0VMagyRRxOt+zXZBj$6&~ci?mSt=lc}`@p2BTinleR?o=mnS;4wxo-UZz+q=~otEAt|QaJz;Juj&N~GyR!Pl;VC^g)grmYwAG>IEGF#UqB!0~PKnBOtN~|{xOO5Xp;-rIX8AzEx60RnGUOhaj!5#IhVw3m0X3K-<Ad&jC!we_L`hA{Rids8AdX&}lAUNm<#vy8Wb3EE+r9I^WiY5~I^{iB4s=2DIyr>~2gGiFM|hRKMK`|1O5TlXtw(%2CWwP2N$h659LGKOEC1ws7*KEdCHks2n!@3Cji;3<nO&~^0qJ?hRIX{9KllTbY=Mv&9(e#Gi9H!ZNXG3<jg)mv7Hl~DwzQ!xqhJvCrbia)z!%^65j9%&@+NEzxG}#M6wN0zHmQ$Dn|P$SJOQ74<<Y}^`UwYrQhq5Nik%)^Y44Lx{;!thrBm6SIs5#E+YIagP_{2mXUleaE^$|vRxH?OE}2A{3r~rz+&y7LV5NU%imiNdjp{*pD%~awgeS-(b?sH@w|^*y?EKn?vROvt+sUJppl4-z6H<OFW=vX$lb23U&(wesAM`sz=2gbMuCVv0U(wRDy7L1HznC0wVd}m#kjI#5RC5py!{buW^{E`KybuGUGBQ}*@h!!Bvo<`)y7-+OXV<_Slqay|1u#^?_P9j2YoV$|kw)>%H&yW}5N#bL2wdL!-7h8KagLlE^Y?M?9lgxozXmypY1{TWO+_Sko%Fp~4;zd3>@y;JBSxNQ@uMa9$Kw5_B1|o>mkBi;i$JsD{b3RS=Nf_1s~4{2B$qFEd`I-id;3C%*!v}l5)$t07YtHO+a%gzAGk%F(`JY&Lln~ThI6Q!sJH}DGJof}K?<ttuZX3D(T>q6jy2nn&$AtE#8NQ>RqhuFkJz(Lm8Hv3M*P3|Va@^AHQ!6|2<tSOeCxWIX8^c-)iWSf&w!?5X;-KmTqe_%Jyn>PO*7MZ!jr|N>Xm&J83t*)AcB8Ouw;3w8Pv2&sIk99)AZMVInxh$D@e3)b?|yG)K4bKpqc@6bt)-6t)b5j6Z}z-pO!+`USi{9-vduV3V-?79_xKrlVKD0Wk-yT1~e8c@eOxoO~)k_Pa2hq#?fW~=P_auFfe<pEE0AaR8jx$UaLQW9Ybu9JSt1IFTW3jnv`j=tP8%u9;U3bt8E;TiEp=F<u-)asWtfr?9rmhMR>i--w|act@_N`2%zjIAqV|z>InxXymii~w{nn37PY_=*HTQ<Wcm@~#IrRVnd7IBEP>8`+=i;z!PS$OX9bmN5<%Fs<Jnjwse%@ZD+Ku|T2}Vt;_WBP6sBZUN4Tf<{NhNp8z;D29e&W8R<X<SIS@X~F5pBJLy`{+#h8f=%WD9JZ&JAkRSKfsi=SUfJ*P11gfdyqxxQOw{)H@u9Vvck92Gd6`nV%(D&%T1)Bd?v#ZPybg8G@gd*6c_g~*~o|80h{5h;^4w$CN@YceDjk~nG|Q{cTLl@=+29kb&Nzz0YS_jE-^C@a79Tq0lOBxI6K!mJgF$`qivqil4sWHbPT3_XrnaqXt-y4kqvvt975`9#Qsy*jWDU?$NHp5KnNC$>TIVeja}j*20;@$!zxk(kb~D@LlTCDbtYWi-0Bo;>QS>1shkb~;?Zz#Z#mkHeg<B>XcATzZKojzspTYMPK9reXjFWeJ4Kpn7~{2;kBhspZ%`Va#l_5ACQ$Rzjg6-leeFx)K>2wKZ9XA2T5#8<;ZwN*q(})pI%eE=Wd{!E^Dma{L2cEP>beeK_1lMRHM;1sC5U6GKaw0Wn-#GnxKA3fm}6jiWKNxN_cmUw1I&9?R|v+sqI*2X=P@(Z$l(rmu&(I;ZHe5IthL$}3($M>JJc6l?#D7uUB-i`zAYj*exc65_0?Ctl0#aO1a0rXyokn3f)umA@icvIK`r+*x8+dI>AB?m&bR;1Ro{(Gw*yd)logPZY)q%&K;tNqIcCJqf{s0E~kdnN;>CaPw0%(}q3?cVqNlH1mo$9YzT&RwF$PRMc{bA!+AE1}J(eN~qK?Owx+kg`-N2EXSl)lduIPJs&s~YZ!=Brf;03d&^!R{;K=;xU4C!_=B=8CK2SAf8&#J>CpQ89lnUFEu!4A2HKK{xh2uL$Z|A^2@mYw_C!&$?jL%Wr4!TQMd?}W$u^4hnGDSA^=nIh<%7uk^|VYj?n@wYZ;@CaBTh6qVLA^b0#8ZxfQHH%$Xl!}Ed?AElLY16Zx9AbZxY7vN!1_Kyy0btTWC{WDgBrj9_cyYmoiNbEvJLb6ShXu?T=|ZtT&wo=;)N=H+wG!jHH5#N`L?L&DY}QYjIPozx{b@;adyeTKMK`@!@}lo2kXu#UJ4I=graL=4f$qwD>5F7WqRRExNDN(W1Ioh?VhbJB$3ni|^%(an;U32BRTf@Uo~nIn~Z0p4nOCt9BNnmqn7$L_?(2%-25ojrm$k?iR^`qK<MHNp*o{&(8cSkR)oNSv8F23Bfd0L(L`0Ga)Wq1)Nt(aA8<+;u^7V72tUQ6eD&FdbcZo<^nMt?ET`E`Jcg0J_gg}WjA^kOrH|yVBt-%I8_|Q+OOY5Rl#3)JFo^xGJZ$>t*yZ^R1kK-&&??24i91OQ*mOf(N10*<Ljg4!emJ?`ZLU~dAw`u7&9k_%U3RGCOT9gH{0`5QWuU(Ck;Pp?N2Xyzwo1&%qUEb-HkVBphmxN{Ln}_dA{LNA2>BCIeF-#1IFTd!c_b5K?;5(Xe2V>W-b9UuZa`i0DrE;A1>I_kDd<~T@-w}YA*4TuY$jB%h0{Tup(Tyn+P@fJr(jNu&KFhBk&>DDGP}D*2QB^Kb|h#PPlmfaN2sat39zeh%Y?H`OmIir(gUs+7bA3kAg70=uX`y!ssS3{`2oTVF;69Lh$ajS3VvPE*=o-kiY!Fmzpa~E*94DmLGiSdcxHU9-l03Gr4->BgR1k$DK6G`JZmtP~*%q|2-~zAzuEo{#?K^|A!BUS6l}1M3JQ9%J5pTGj-@Kc!bgyo+Ee=fJwY`Qi>0z5#4Q#nMYl1X+&3nXn<A-hmZtZ6mB<2MLkq(pGsZijj^ClJOGvjKr+09rcl@9j1elA4p>maclwFJz$zi@QqrBq^HuCa1|L<-P3*8kl~nrGVI1X@k_@DAX@POHKsTglnWh_(e4*I_NM{X&D4^a8XxJD^KdKPvOw-j1Fhl|>3jPu%k$UAo+Fa0gLG>)DhR$O8n-g;G*HZN?{cF}kONaUK>%_~?Wt2G-<~{UWynHo@mm`mJNxz)n|LVZd@A<$N`sJ*YvPRkoLS_^i+dpJu*HC^(WzSj%PM0Li`zm1`&LqqQzlVzX0Nvb$emP_)AXjE(Qs|e9!xPdyaSr9r$CotA8`CW3!>4RHhVdN+^gx0@`g<Ra0emm@#2JTwB0avE#vghQsMV6mzvay0i2)=wh1LAIjG{bKJdhpnl7LTFF@QUcu{2@;afBolEheAC07pK5kUCT&IucnZ6$Y3pu~#CilPg7h6#y{Icv4xSUgTHM`C#e};xu;@-$U)0fP^gEU#=WpQt=G#x1nw#8CR0=0o-prlTN-S;{#iduakgc`O-I@JvaaK`eMg5J!eRD&6hkN2k+T!_mPe>Qo$6-hv&SjYhQVp{Wp*tC>VyH8SL5qRVYv56E{`rhbxuLA8dWhb$tW~wyjH~I=Id@5K~^YtONQzPU6KQ;aaifHVzR==89Y=rcmddq${Z#jWW2pNWn6@47z00s3(ie7oE28n`AQJZGeQRVybcJ9GQQ?ZkD$%X)_uXRAjBV<Jdrl*^Z|?l)D=3NLQYkWzrura%Ki22;3kES@@BoRpIq9n7p|lu7rqSm?s04a2l|KO$gWQ9)h0N=zmFXh(v~vH_MjUZk{i8KpvNQV6EZ8_Zn}07QDF7R<q0zDcesH89>B#bCrx}<oGZKagB!Z384qT^{;X;t$y{@N`>UU&2=>Q(X4j%6pjj&-3oOkP+LLtTa$%{c?GNrpj<|Q!Y(GM6FU1iKGGT_cf}a3YYFfkH3}tAnC77FNEE+V7?dd_@7%;S$-*(rPs`pRS;!V@w^HOXxy^=<$5s*?VOY72f=gfrW7T%e8Z4Y`S>Q<QxhDp@y>s2#r2R8pHViDio+$5T<TvKaQXHzF;ZQF1-~Vcwe|^&Y8^k!V9X0WQoJZS_?h=uZ$?*v|<)Lf@PLBeX0JEpz)!x<1W_%!Jjf>MWNkORNuqB$+#0X?3&|ws<8;VJKUZfeckvP%g-6Pk>p_K%iHvvf>CvR4Ql|U3oW=Ik?$m4AoijPmP-$(|`w^DY)R)qPq<R7^tbeA8aAJd`e)QS2|PS2D4xL^KK9%=dc9MhH@@vQ_FDip9O5gD#}%6%na0>KsujTbrJ^l9NhQXi%U)q0-&GsSNq<;y8oogWgPTlVHAs~cG1lBhvL)rBoJXgC&ts~vnxRhubi9E{+Hz0y4ctK@ADxZ(kkNnK`qhkd2hl;-^PuUT_eiM~aP&PIqes=DS$yH-I}HEs68LbsN!+d^C>QEj|*snpmRR%`pxbzAL(qi;GuUCG^J2lY^bN<A0(P|G3y>|cvDtzMzjSFPV4<)O3a_w!Ca{RE6uPbnLnvHPj}+h3%e%7DCCq}st{FBJ{hOI|9M2}N5o<D>3%1;=W?H%3_tBbB<}lX=C7kqYU;t;AIb3eVL@B|!d%1cyKi8U;~HBb6?Z1=5~asEAX>^n&=I+6`=Fp;AK~#w1-F{Zo9J0JQjhW}(8z8PTg!oh-GWK5&=Yo=B)Oq+ve6uPeM(6`#C8q<_?a{pb>O|Ke-4Jj*)QV-FJr)}_wXPTq`VtUSYuYIhtJQN{Ep(EM)l5G3uC^2c4+L$Cvele^>&&dm5EFPX{2FMVO(DD?$u`l>S&v&`@iur}e)xn0LGNXf6qz3a(q;{m0g;^1%hSSCyCu_;T`nm!y-7=@BIAJ;mrHU!*ulvC%vq}=R~C}_-U>o}OOw(Sv6<$9Z0KCB?gM%ud=3q72)^dDc)g?GT0W3GRoY-ixVRXT93Y_}=*=};wP&@DHJ@CNO9pFy74Q6464S%)g`NkwL3wzFo#5yB%A2<<UQ`7FrZXegU&8tpmwSWuWE4m`;gQZ!-=+xBV29SG!yj{NL1&I3EoN7+@Bhu|{^_SoA%z~;Gbt0UNr5<gXbE%4(}v?(gvOELipF*`AK%x|GOTg3do*)+H%ci<f}A=4`3WJueV+$`op0nj6t@<nde-W80#+Dny@%a3Q?(YD$oDqWRptlTdWw#<2sIoqA7KP$~N^PIvGIPONx;E&;WN5W9YdbhTs+C6n7+hr--c{88uqDf;aZ98r}%fWjx#kA|}R27soRkocb-Dt_W4WPhx)oBYse5!LPf99DMvcy4<P(iPx=CPOL%(QtNOnyd6Qw&dn&8{c(gud<>vm7JAaquk%xwhLdhfOmn#g&tHQHIb(_;i-A&GSS{G<U-C!d+zK>!<Bu_*gUT|NK#GR%T@3*V(MBSkPE{tn~e8N9*2cvm%quG`Cq%fz2BmrtPS^V1{W%acgLp){KT}ec(plQbSzu@n=J-A2&thb&^zTs-i3xG-TQ-nXD_R6$USpfi6j+hXaV5PjBj_7?ka-T*SMO%%85EI?aq_+CUjO8g&PgJ4F}E!3@@{+}&V$-62eUhs_F79aDfXW(hxbityJ=*QvS$sC*s|3tgv3C2m_bTzc9gDP3-bu_$~Xn`6Y9x!3LzdQ+JKPpvmupmcPjmGP?T_h9DThXeer9XZuZbwRnqwF5Vd-oi==ysvh$H4D4QW%(#IP)==Rc@BK|KNJ^uRc&@NdoD=D+&d>8)`f3rd7{8t2Qhq<#}p3qM*IZbE9hT`U}4MikM8g*Tukg}?D<?CU7~`OLdj$f>7AKv`oR<fnLKq61HmEL<mJ({|H+N_^HuSF!VSZFqfgz45w{k;wZpB2e^$voHLSexd%lzf?$%Ln6rUT#=SK1QgHG`YUw?|v7xD87vuC98oHKhCv>v~x4*CU5;q;#wsOw*&Uv{n*HwC!?f}k-pwQI8FLwaxa+DsF8IkpS@Lmbh>!>D%bLhl&5rm`r^K+U`Hck@1*@k^LbWO?+Q*;A7)!Mrrd%-D_x*r!Hm>xs;9{m+ox2|4DJE7RGT?Xnkap?aNypRprNH&W>}^RGDj$ulRmfLJ@70A`N96F%ItjOiQa-8suABsWrLCZbQAU3{$Ms$j{g@%B%+K2g>m<FgnqGP#o`a%V&zAtmjSq%stp0qw34l055evtx8GE}Rm2X0$E&M7Yz&Up~0m!=3d9`_$|?>P52Itc!X!yYl?R&6v<!UvXufOEWoA7nPlzy%;9CfO*|lGC`cZc#Zfnk!I%foytm?coIu$%i_=Y;=AGO&$RgS1%{0~yRZe_N2Zrcy3a`Iu;1UG^z*`7moMh!OFetHj?Ibg<F3<v+>3OdbBfRS*7(GoUvPa+=_Yaf6Q!c@iI0RH*UUa!yVD6zXguc$Mds?2M@tHyJTg{L^m`cJy-2=!p-m=gQM%Ap=fA`gp3TUS@@{^HP_I19dY6%zYMYF2jWnIGq)Dj@oxWlmvP)#0iS{QL_esU#&%GAR@BkO3_^5fBlg0y(1K~ik02OZ!bdyX%hsWlATu8B6wxpqGZtewmxC;X`)~RmpNeOZ?FYvUmlwmwU6e&Em^~gJ!IN;keAqS7W1juzB56kMzuZBjq5S~r|36xt>_&E#~Vk&mJ5@=ZWL|?R<@EMI$QTEzU$TyLP<V=7Mz6K#2S%lc~JW@`JLnJyY62j=Hb_zGVbT6Iwv#Qf?ei(16X`%HU?ww33SWGi<S`?nw_9A|Cksc_fOq*z-)v`nuxiE#LK5bbAR&Xl7Xk3fJuwkW+RZVcBC5cVS136VzXYm9rkr*3A9D+zNfo3!VmASMkP0){~g_OP}Y=X1kHA<hFUAhZ0GL$weAw#~>wa8E!pbuW&-9)Q`2NGFU63z|Mp2jU;e&2_Ns+MsNJd2z<GX0Lr#k5KGt<b8C{H|jV?34fY=pY6p7uSy}gz<k`JiRYZ!&)7;oAFm#XXF*xX}oAa4gN}FaGW%{ub1=5tdY{TIV_9QG?K_2ZMG|OCC&t_NAgO4LS8`-R>>=uY$y#-(fHg<`i*j;69~7N9H$LU;a{U$T?^IsENq)OS1YtFmx+nFLeXji=L4b(yf>rdM$8p279JWl(BJ{YEFTWR&=losx?ZK|8FOV;jW)5*WkGuXaSPIaM_o04L0vU3z0$jRS0xn=61X%kp}*V`LD5`gYRX<W&v6vV?ZmSp*rzfz=UVHsUjjD*3bvCA3voaUhUFbqCDv_rNTbhg6Sj4?hYp(ve>Jd=*NS0wFQ<JoBrVR%j@e%7m=9(phf29jqt!=N)pQE7q|tg}CI^fj#ONvb?1LHidS~pZp4PtSeXu#{gH5<IU%0u`;YaF*|JAJ+f2$(jDsZ<yZ!LUl;eRmxyfwv5hx1mazx{cu)8Fd!w>tf;PH(4b-$#nmUwSdsUz(qxg8hD3t(VP}@<y->ooe=y-xOIMx39WpLpQ>>D7AVkoXl(XUr51zl*&9Q*gNmuS+hqT^L@+qv&uI<-q#|cpK8GKW9+Rs7Qz?x`+4zxt}J@JX0Q6O4?D?|G>JMRdhufA-n}5v*;MV7=+4zmr<y&rZ02SArKYIe`_yRlnqzfg(#3~i`nqH$x-R%rea_h{r#H2{qp3eEZYrJ#uGXjTPwz3D9WyWC6MQgxtml>cAXB%h6+D&g!&JXNQ|5I3Qq6v@E*Rb|$hj!kd-t;Z=4;=|FICE4mIhsj7GAE<2j|_1JmX1a*9G_9-~0Q2_pFd#n}wE`*X#5z%U7Ph+r9Me#g1|Eis?f(?>Ovbk;z2~{QC8uyjAr!!vtq}<y~KScLIgH?s~2vTFwwKflj*aM6L7$C3F5t@S|?$s7-qPmwB~*ggpt7w#cLZj{9xj{D@VVa{i7sq;$JVTWdyC7w%KOrxW3uXm)IzA)An(yFqrgJjxq7>SbZ%cJM6Iq}0i3ZEq%wNhLp25z;_ux@Hfxx$$B%ZO~C@-=ol)Yl)B!;b3!?75=Wq1>!g#%SrCA+H}D^kYnA^<vb4HJl~Bd4zy%=TTXIBwJuQnn|ht$6BqNb?0Z<jqL$a%g>Ugim8n1`4RAOs*Ym7(n6Rx~{T7R%$fs-=n;_urO;EIa;yd<0?1K_FVuZqZT`N!3{-QRB{cE5qhT_n{QTgSLU=_B2*z39RUnosq1!OQw<Ev=;+onoPq$*+JC9V28nm(?a1bt5+!F95JR`D*<jc!KP7epktP`K)N1{q?Xko5(iYh$1og%y@tcgok7N?hnG5uY_XM28b)pOs1~mry_@G*w|^sxY5%_eD=mYZz{?DrG-hVDQ)SawS3A$f*D3(Xg&6nxw`>a(|>aKEN&7*pK{v3dn{bu@1PN&QIVfztM=&r(FML&h_ui-CnAA^@5kGDlicIYD<Lwk^4)27)jHF7Xj<w<n@O!G2xQ>1fNhwkcfdGx8dTG3G@K1v!logi>Q&fj&bMSD!*4IDUSbgx}5NAOEa&dA7U9p_)|*0995=G0xgr4t-C_`w-*qF+a)NwY|-)gI-lyAMQMj;m8h{UQ)PfvdJOKAe4SS~R?3)Y>x<I&fqk}bIk7eDU{X>{R2b`$N_|p!LMdC)gfJYgijW$bwj;A&Jn7_yT?J02Vcgl!w>(ToCev^VrbyUxH2LbCS<Bsc1@^Bt=D2Inf5aCN{u|5?w8|H*P2i*Zhx{uYpP~H8UXa1=#*2eyMo;mgG?eKa4TW~~647Y9nBj<<X#q@CJ^{Hb_CQC=p-MBbw4XR5d%sF>w3X5$)>e~#f&ffx8QifiN&hm_9=_)Ro$ZA=()iFQ;mn_A8||s+rANw%iI2ssifIvDSDavy|K60CQ_yl##WtlDf#t(X8e05#Z{T)2AbW!jl>e`}*^&IJk?Lh5E_?&5pM5oP_SKZxPa%m3T^bI<{Fg_EWnJxLIn9YqDx0AmsWU4arU-SaCeAaj=lV-fwqU$~nA8Z8=!~;Zd9~^&<!%1g+7lauJLned(TwdgePguV&Hvo;VmLbD>`z)(KT9t+PPf*mHDvGYeK@(V`lofvQP^NI+MX7SF#fE{AY8vWe8Z^St$sd6ks5n4@*W2w@5|O6gR*sg{wR?Hc;=+=z2EzAT-#SBw?a%>zNEMkO>xCbo#dL_N@I&Y&6ugStvMQ@TZTh-%l&%mDoiMt%2HCWAxX;UO|2)H{&JKtx)Z6wgqWkRz#%sIsOQL#Ls%o<`UQw6TmTUP+O}!{)HHyb(7egCm|MAbc!>ttt@(<%B{~*MAL1EKgc!RmyLy@d+^DtEvWePrblaJ@yO|z;TygiG^S_BzmA=QZwD#ajY#)Y3$wG9}a#w4Px1mEc{U)S8(#6t`2DUgHhOzXc71w3mrW|M2AU_FkX^KNr78sz56?>F%@VyZn&CR?3x=o2RTi5M<UTacKk`4C_%+e*X_c?{xxRFRkABo}fmd+x60k1<(&0)aUA$U22&r1i#V@J%(1AK|sN?$dxNo?v$AWs_rZEIy=LmEuET53;5JF}0bRMrB2P5Dc}<*;d?_;Md$L67;gL3^jlUy71#!>ME0HVtk0J(ycfgjj2$?E%NJr%^mordw_Zn5;mz68Q=jL)onF)E#CSBC9B+V}$kuj)t9waeevaEtX-Ey^nMw=r}NF87+k&D9H?DJ(cr66Qi7&Go}z&dAO;ACwCbu>GKsN^ajQ6k>j<DgEsymQ<fH$BiHPHz=*L%3BbAMCjDYLNp_#A(4dX9X7;kJr9L)R$~BgN9|pM6a~L^2j*e5*J!T@v>L07MkDRyR;GGnV<I0cxEcPyN)kgQHI5<$#1F)(7bCX<>n5hN_zwXNzZGYPRHu~oJr&KhSvQfFr<3ia8VpR_an=+r%;b`)8XuQaR4C3*!rHSjK*aFbn^!L0WOqp?YlnXfK+!92mLzKSJTMXhj3~or8`0${%Zb7fZM0Y4tSX9`4moPt-b23RBj#cOHyGOt}cQJf&#9KY(HdjOVZl~U=kCW;pjkO~lHSn4Y-ViAr%lv`PSO)a!=sHXfScist^qO+yKE+kpv8|(?`G9f5&F}^rU6R81kLx#b8o&H1B1V}4o?X0iReTe?j9Av+t#7jSyqE`v4SFhf1tas!$#E?cN*eF!u1=Cd;{EkHj1wiEP&uaTrdRwpRFCZd*{qlK9B|fqK+&JQ0-u<77{CZ<;6qT3Vaq*+mD)okp9h>uvUxfK!!d2Z?BrW6Qi&%I`V`d?wN+Q3nrQ{V%{bEM(9+^Yv8j2${96{tl*a!471IySlbF5pObRxlbr-=)>6L4Am;TK0W7}K`TQHf&)j_JglMhXrq7^K^^7<feLJ>Jcv5>Q4jGqKI?p%`rLGPq3$l$N5HXupL$f%%HkC~SEbwQYsdB;h%LhVcA6_1o~V~Qm9$Yg|d*-lc`^<bglsOV}xn;ix!8uNjEBO9BAS}z-lSZR}71=bkH8Cf>VcBw=N^DK#smfsZ@HQJ|%i$Y1XEZ!!1Q+Syl^FF3RDq`;zt}U^;D(ErdcA9zU>2Qta+JX&wkU}SUHgR+m@>mQTb8RuDzs8=VjD#lF7ClMio|5h8TD>K|7SxpW7;y!S3PU1F1UeH?l`RT--hmLcNyvg#%MOg0KG_n#8in~d&m=ueST)SmdZ(0=$m2=*rcD{7T*T%!9nqpdK+pFS7M2|c%ekF2$Q!G+9m=Wx?$5MxW3)}gJ7gQ1F?mRx&T$h#VNtxoJi6^5PIMZ(Nu&`+N}(}Ug~n#4&{)Q8(@>jv)MgyDnV0g6y~#7aQ=4%TW=vn5Fyq(2zU9CFXuI2l5xev)yV51+tgU&klnA&z!DW}^B$r30p)_r9TkDmkc$>QgK}&8c+S;}wO$+Lam7_(`+lF00h4MVEO`Jq}H?m<)sW8noD$E|;O{qqiO)966nNz!Ca-?ovgYUU#?dqP@qq~l!_JiiB0kPvftXs|I1W!IJ_pD90Cu6Y=1$4=F;>4&kvWI?k{So8L|J55U=0=OTQ3`H<-dgz9!Z%vXjTUoLu)Hy2ZUl}SGv>yOxiMq@!C=OWyq5Q4#^e`Xy!h^WGh<TzU}lVp5U=9L;IKx5mb7n%|64;v8bEfDP;FLDI9NE&C0>S*MkZo8lL4%pn67dfK2XQ<!#FYiq9Wxf8z#Mvh~;|rL4S6zaNlvkeVLzs)O$40l*$y@STB(MN`&RmAJkQV(@YW6eSl=;s8=~rf9e$q5i;skj)u<W-*VOn#yF{ny=n;O?fTcrV986#$_2Y6ToANeC{@Pk0r_|?R(ZzYdGUD>KA`i*8mFm1$ddY_k6k<0oP0rW@+Gy&bMi_hSiH<NdB@N06>OFIy%(7r_8gbD;3ob`ctOwb1;xwP&`>V&QC=@8ITw>Wq4Hdy)VxwwF}=jMn4W$-BT}S#ca58A9)^+RF+bS*(^oDMS=@VyK+ai51aQt2CM*32Gsy=iOoqz}lP?HwUOw}=wq#gpOD2<roQqE`gecERE%9pWU6q#<|8jzf)}M=P_rK(R%QxBQAF_gy3BTR>bOcC;!4&E)R)$%jwbw&x22&V>*K%iI_#`jdM@>}tu|l}wn$G3H#$WerTh$ef81o&EB)0!pUU@`OWJh^M)y2ae7FLOV%$eTr=?TCF>YIfC?=Ax~;e-#Op#Wn2iP^<t<`~MteGhoUO0TRE$v3LFhqs<iS9cV;<6?v5bPrXzwe<PuMULWXcB=qjOS)50#}j}JG(ekNH`wIYvZO=g0Pn6twXxB~|I@I}j6VO=4R1KtejDv-|KMf`T>bD2EJ^v-@BFq$ZEM&<@DlAYq&$dP<L^8G(dB~;@X>*=H-wVU#B^yA_uKL|%KG^1nksu8PW6T*(B=t0bHl23d7YYYTS7&i*Y1AcyU=nRL94!Jm9=9X{orYKT8?>y`*uS{a3+%l+z}#HdbWD$bF0#|AEbB~HaplUqv9UR)#8=?0}UWW<A97Py6H{`w_hq9bV%r+Xq677>#hN`Y0w>~1mZ;F@_ku+)8msbO|q7)={>qj>3456LG9yOW%(vPA83*){6KJ9*p`LwWzHcvem|khLME|sn{o+5_<3P2An6%@C`fPu6#y>TefS=*qC(cAbgFospyK%5@^fqSn{xaypoqyrZ!CAbc9oTz;#-|_rLr4BO7>>*2Fjq>@Y}ftl!L$11u4ymzu<QzG%aTUSu7tBgp><w|JM(99L=P%U2+`F`z4PlTp%&!_xBq0GZNFVBWvk{yhg+8yhc~vM*20c(fwQ+b7iH|C2@)FdUl2H@EY|?uTe0Socwtwrji2Tol}>5mDgx<$!k<x@iJ#_mR_S5`A3UdY)7mzkGuoib21uD9|aijS3gXNH!<PiHvrR(@LjLY3o0ZPCCe+=s?kmn(vg7dlJ4zc@~Hg`VQb|HP-54Fd80Q7PTSDFUMjmJ`be8sjolc9OHhCHLB2v7(Mp3hIs5`3G5IIu*(PDtd1K`J$o4VQUo=ujS20TYx^1xSimw=;GJIBJx!=(<RG|{72~<xeWt6a#G6^Ok4kZ`tBe6{Eq<}}1M;(B9+dB-XGBh%wR1HA6;G@JOA`C8ap9E%y1aXoIrklijb^c>8bYTMOGd4VO%g&qr<7*7Ff$_(ou8_tsD|6F*Wte$PPYZ_G2A?f$((2uE*k<IJkz}@tN$|>ymdHZY+@s}ar0w#w^CGuwMZ#G&j5F7AqBa|X)>0TEqz+8WcOxZJv{m-gN6>iXN(S@%hSzYkNlniXaH19GJ7ys;VKw1UucVx|FW=HRnN&vw00dk|gFpLF;Xr}>2T7bqCMCF>hEPckbdyCC83m<f*b3xhSR_LT1T0MyLu<{8VPvN=VwsX16c`R5*ivZK*c2f7TAHQR*)q40+&ptoVjJEHPLf?;zao<7Q<|#ziyt!n-@0Lm69q7kYQu>>BpR8Ki*3VUy=6$$JDYPOz`>YTa}VrGS)TR*9VBoJ@34G?PLQpENg>(qMndQJb*<st9?g0@mS}?LA8;C<i3;t>LMh8k=4XY2hKzCP)xe<{2(iP#^tI@?&Z4z_Pr!AXGz19TFSnQsPFk*z_r+XSSr=O}9xJn|eCO^7EwI(<K<XpWJa|S)*C4<RW*|#xp!e<>t7-E8-4A&(!tq{)X`K?I@vmbvL1ZeyS_aeV{fmmlJFRB&ZLWdC6g61LKsFNbpd;hC1KcxH<|C2)PHH6bdgY<D=I|Uix`4UbOX}WNZ0JU~teQWiiF_k|bA#2Gq&|FaPZ#i}Vg}PlB-)lK(_-M2Wxl+56;xDtoB{!yK>$z<ClQp9%*sBAX~b^cv=C08v53rcym_rm_Sb+*^iN&g0*HvZA%yq|cmDXy;Qs(p0NJBHJYwqm?14Ej2FdpW#*z}qM9gtzCVBk_fgZ?=vA<P1!a<lz9Q=L7=Ufa+C;rYu5KvtiiBHl<CS~Lgw`4BzE`AFDV(~2{K~(lE!6f-1JWa%%i$5>>Wy}aEKgVBqM8_zT{Z2FP9zBJY33&JWhtldv-r=-l;O@G-@;6^SGG`ddYa?@jtHR48vjaExwIegz$XpD|T^*J&T^*C1#$>Y?kf9DplCKzroQy`xxRVDy4n;*sg5B5kQ2E}DLoqT+FWW(mMh54>pyjinIE_PX_<GTVSt!V@@nFD`DS=K4;P%VV+|>mhA4JYSuVK?i0OkI&`=yw+G4(Nh6A}k7{rHroA7#3Js!PGoS%y?m8rUt5<j;^_)XA)&Y$ZYE!L4LfDIU2hhH%i6AKVU0ej+Q7M&~#H?<%8%zEDj|dPQ#xqy~<G{7BMFE$tw1EMIz$BS&MCXnrH%lQL!=u$b=|mURz^{K!^f{KxK-?jxlDaAd|_kauw(5i$izjQ~||76PiZ;AuP~gB7^J?G6$16BXjKDl~uLb<K%8ey(Zf;n|w1oE8fHcl0}HPaATjhP+1`?<(c06V-!_ku5c5r6M&(X;+N;2gfj*9xc*r!D-8<@D&GpF{WdftiD3{%wv0rXLzg{10pPGdyhuN^WSQAb;!QqgK(+wE2dAoBPlYKjG`h-cQ3;jDic_=!zX;?Re@cH@ith^h<YDK?qXDYdB8Z-GcQ}U^u)$FTE}5)#O`l>k+I7wX2@;xKGS2c>C}=QT>mcxE?oYjv-zsdlTD3X;xcyWG*v=W4}nYcm#4}o_GTn?W;t6%%$C|)LWL-s+S?SkbYm(*o>$y+dif(<OJX2X&t<bbx^{|MGRY77`JCy<O>!EIoHm`Qzg;3VU_5`scqRT+8bV0(Uh7|yx;U{AD%W;@Nj>PUb}@$#z_M{nS#<Qn;1Y%p`dSP0AY60r7fcvL?5SL{Zu|(gU@M$c-O#i4iJnNZ8%0q-dcZ{BXNkAu%)3#gU$1o!@i7LZx6ANdJyHyNybff4s4_gE<s)sRKvK<oT1BB2i(+HsqpkC#Mc_PhZK0%&$BrMR{Ui+rFr7VPxil&tdM4_anKgWXzQtFCo`GGv`~RtXvry}{G)rjBX3f>^_UzN#CT>RDh{(8+nGux)R8q)!@<Cq&eUy4B^g+QgO_H)I(@+YE5-qXA22;g^dMboMM8pSu6-p_aR~xj<k|Z@nNECcC(K*KW=4$rY`!xT(|Nq~*{2b2RXYaLFGw0WiZwz&5DibY}S)6FWj2o?-A=!Pr@wylRhm|wc8+MCtj|*m?MYpEhqM2gDsYl@p8>hm1Upih^6y`f?R(a~K=#Uth*OP9LTm0|xd&>$@ZqJOKl0RqJ0gDu6YQv7u7{)@0$+8z!4qMGdM7#N|#$G;D?(q8`l{n*dqea(=GidJBAb4TsZ7IogNf2t%+QFnz>#GtypQ%9w64994&J!u9GGL^VQS}aLP=zmpSQ?SFv3g;A8E)dsVA;wLAT$+%3py$BOq3ZWYsMj@!kV$nciAAMV9!ge8R=Uv2p9hvhRr{BIqn+2I2$%!M<zs$sosV4)q_`SwL%Z5(1rm)@J<7@9mW^8-WoAuWUO>C6ginx)2Mm`t5tC$V2sLN&iK$ah(>w@46KqeHo$E7SyyFB&9*3%tA|2PDP+kd##pWt@bJYQBZ|VJhVpu%ZY`HhTd5EUui42G<?S_=K1jnQaKLliF#OcRuf+fp-OmCP!yes}e~ZD{Xk2jb`I-Ma=)kuw{iqVVR}%Nv5Aut6;78Utj(o^D@I?iLf$V@W<VxaH;;}_5K0DAIA2r|8<r}|6<GQ0G>+hK3_+lL@GC1VV>=}Qv2%1Bu{=t&3k-~B4Ya!q97Mg2&SC-H@<q{)=*`nB^_}QMiUVLVDaAO8;>{FI+U|ybFOOd%A&D;ssiVvcSQ+w(+ib}^nkZB@;Es$?hTfC(vp1QmejT4)cI)RaWlQ#RWAg(SEK|_!)+o497Ip7cytGP{8X8+j`8#qCXP#VF8bEVhk0s#UDbdZp!g4_H{Mjxqm`QhzOCs}k5IYWHzeM(y?DH56b@|%S}TH?)`b83WPg+`mFvYqv4IVpXXrFeJ#Usy6u@=)!1U^|kiv#9$OZo7*=OY9RZN^0X%J-InNOe<#A<q^<=Z`Z<ze&Gl8d3~gwj^h^eT-K|De@x3s+=WzPp^={ctJH0YSCkX=byj0sp0>=8ut3vK<1&4vGc|giEB9o@U)w(kHfwJuthm*v+van?BaI8v%=zoCN!hM{hQ;qSzeL<s&U|;Zc$(**^^2cwP0;C_U$b`3zq4AtP~&qe7S0R*>bWUCJPi-3voCVXFHNhndhv$1)la{Sh(A(-`g<QvB~?N3q>_5k*jyjEPaPOa&g0@*lpfdP;u<_zb!DOPyrrT6?W6Fv3(^+P?)w}O7k84}io?a9jo+We#f(zhdG`LoK6cl}?{{txg<Vk2?3Cc``PnuoJ3~_Y%;5cC1R=g@Q7S|Jd};jt=G#Ah|65h@qy8rsS7=$D&FnbSrQ!+rX2;5q@l9#)=UYOL7)7!Mz969iJh*O}5C$$c@)Fn36*jMiI2TNG3`+!r17A%A_33uud!l4cNfwe<cOsQc&85_G5%r+*Z5oh))YPty#8HCLh+xT9yJx_e*TZs*q5NyWG#m=OHJW-vj|6d#6fVQ%NAgls**xXAdxJXi_~+hyo1c>Th<*nt$A#OR=G$yl^AyS*Dx6Hq``z(=r#Xt?{bog#_ZyW7-126=-^uPbe^2Y1Ev;!{QNhF7;w)4mZlz5P;w7<Y30(@ZC58t;yTlWV$==`GkrFL`@rEu#cbW&!+wTzUJ|LEiIVr-eJ$}FX-F$N!vFPU8@u@>Y@IYutjXOKkD5{T%=C(#LFo_6W^vL8{O$RU-0~gX7Fa_phlg%5-G>HzV?Xh@9afxu*cVZ1sD1Ysv?}$*^@gcRyt6hBrw<WVHXA@$Lze|2g-dm7xQ-BxCVgMI0PPZ~P=FlN~Kf)MiBQ4SrBm*fC5G6w=wqh2N0fiI4Ew)2G9xu&{I}26~Bsa_{Tg455pa!=5qM|E;b@JIK-kJQQYh00-W*PWL6bm9bsgr3%gA^Klzd^T!Q0r|~(@W^<k`UQ_Y1Rp>Ll#+Sfxt(xa~N38i=+{S@&CKu%#hqf!{?GASyLP$NyaOkpf=tZYZVa2f@o6Yzy$^*Z}zifQBF142ccX{wwC?OhfHAeB2Lv2NjYP2$OV#Q*8GTovo1D2=#975pbe4V8$FkvmV-!-N;oERYZI{n^f{>HSIg&5B)vw}tE!|Sr;U2sFIaZH;bXl}Orqo^gSARWz47!qDY{5`h8QXY1g@|sPp6l}{8g2KF$`>#lL>{`*)Qpxts)ysIE_Ag<HlBO#9{RI26eLbx(Wr0_8=?Oo8@Iadq(UWRr7aQDQ&?@?c9tXEMd7bEUd_rgF92JFtXdqO^<IubG>*o=>p5((sWFvglxvc06r|H4r{g!j3YWuA9;FW%das0QH4;dP>ftG>`uVJ&GgIeOnhTOZ7sx&7zU-O5#~GNjX&A`*JeO0HJ&vf+WDu^+9}rgyZ-f=4DE||^?s(h&bzgz18mQ{pW7zJy~HG+GZJQxF*rd5dkw*{)Hah62Ga8tb|=738gi3I6KlYZ<hvo+;H;P?43jvjeW~?$Bea8aa|~<i$`D_isWi4^ImyOZC~FMKgz{nK)y7n)sI|6bLNMQelKEJ~(*ZNx;O@jS>4*&A7D&)ZFdg))!y<Oc|JMUH!8F>_SDusD0ebx(z6)S<%M&3NbzA~QO@<%@e?gT%kN^gd2oyTCG;in%!wd!`PLy1t4afxZ4cZmp!AOW-<K;c+wQ1KjI@AXAf;C%I;-L+|eToefqaAI>Sq|rKs3)+IHw<Kugi~UNfC1ByFo_%!!YzT#5D%@bT_kWNx*|ZpIRtn{#DjbeOi$uMn;_N&Fq&Kw3=7SJSW$=VJOlCwm?!D4U@n`<6Age(!%qJS#x$z`7@a_<nz>9ISq}P&sJ1-=cx!ILOV(5Ig3u>`PXB?ICqz2#%zI6U2t43`H@P>)<(Ri_Q$5^bU*$M(_kb~)U%dwqH=oD;zWU7hAK&AV?(_Tayyh|QEC0QF6~6NliO2hFMhMWlclQOmJLb=#UPnuK&p9P0c!Q7SZFeZm;_ml~S1WfqRb&_pTPhp@=pukIA9DOlX1E&XfAkCo=PMvyTWc3DIXI_cVM<eif!HC;r9lyJlDu10z`X<<xcZT~+sJ^}H>EI9QYNs@CeqR-XNU#-1D?iEEzLNG@S|9YdF^2;v$a9+mQ7@!6qvuU<k*p1@0PFxwh00Xdc3cDnMyTB^W8xDUBTdt{?_Y*+*iXK;}7{!>{*_Ps64>=-(u<s58=OlUsRd^m0WEuUgoyF-dSwB3vI<xX%$-0z$PhNXe+9A66Hg5^A?o+ISOjxx|Mi^lHc)rmX!ROaZV<p5Lmkl>?6G^CI8I6x#}{eMOhPva0WwBmoYB8jD(*FJdl?dIn-&QCT@P(Tn>HMXyx&1kZzu#YBg6vq+#La&hF{w7#VaW*T^Y02L}U(EeN?Ud)`rmr47xIsRy#mD%=24M_Y$OH=kFaSKoOKWrZe|w1t9Vd6|sN4)f0ee7VqJ`BW7>c7y~0Aj+KDK901P6$HOPw3;uib3GbwOr=LSkbwy+vNR$)c?9g3sMLc{c)kIlXFlN#O#t3@iv_q7(2Ms&36Vs>^6zcSn{<oC)r;66zjKFK@uXr_>uUMlSZx?;)U9y^2Zj+FB^`UXBxz8=)Be`0=)TGCop)Vx6S9lVr_$sdy9Y~p4iUpPNP&R+5RpD+@`5!JceiAY)%lX*cf0Z1&c^h&2auy1R80)D+1g=*#UGoH&uf3mrX*zh+=G(dKY&)>kd!C^M3!f5B^lQ5C;2OGD0ddDvA4ZtIO?%apyAeOX)5S3z5zHoa(%<rg)rbM{GHhFT{sAG3>tMI+I7OhDr#~iK*XRa2*|T4-|v4d<M~VxI^U1(iScCp&LVMNY0#AwXq{SVcV*+5f@(=Ho*r%4pz<@xnyn^PoAC^-C9Y}NtU~RXIBy1Qi<014&jelaiW*I*JkWmP&aJvl8t)9~Y1giV=PXXKVpoaZo1waIi(yo#&d*(7e@&MSCVRMkA!DN5V3R=AtfEFf*mG-{cYZHZsgk*wO0>~HS-Vg&Ay{i@Ub2&zi+n0(B4T#PE5;8Dh5p`a#7z1RC1%pSBxcfn4Kb6Llq;;2OyWwzq$?UG>9U5&xqwMm1WX(SO!8W3i-3tM0w(Sm0TYlYzq^J>dtJlCGfCPlG)z<?dt7RmU^`L}082h-;lu4(8G}>JOBs_KeO^>Dkv!!yVkR{n0pPq;GKp7|Oon$=G8xa6Oiackd`o0Z{vJ2E1od-2!6}dTHgEA-_i$@!%-AS3vO4n<nqutN-Xc`TC3K>uYq5aalK&lf3PSai#2$&jJk`Do!C7Z-%b0eGB_d}bEyv&bYadKAEwY%-0G<32XEC}7!&+5La-XRvZR-~-+YZYxdBcp#!fFamYTN>kEP;V(2@GUKpz#<*Q4gTC5-h&B;hx*`Uns)c8Xujad}aEHRXuJCBzl@s^^{#5{8cRB0`*{lew+h+&3i0}%SC-(DH(8`w-Ddr{-DsSI5SNf@x;W&lT6kEo~D~I4n#8XD}st$<n6Iat|D?if?94*U4b*{F2djqZ0}5UMG1pfsReTZC|X-79SgfE_|RujiqMXzdhwQoIe`h>$9|be=x@l)p27;S)#5kZu6_EyZu;N<`F-WcfE&C7z-_8&H0|BF{nd?qk=vit3(>uS*x#QK`$y%)jNe%Ft<`cUVV?Wu8UCqp@m}fuJAcDI>q5--+kr3mU0awxt;Un%Hh!-3@3k27*4bR3L}6@1%aTugI0L>AbXVJOM*XyG6GOchMFb6ys%gS3<Tnf~gxKTdN(>7zMfTC=B}v>Z+W_q4Q2}RFu)$MBk)}nbmnpeycY(!p<Tr8ERArkjHFE*e&K2enHoCR6;H1&8LCt;4J%(msSmP2EhENBNfn(pZ>Fjhq{?JsTvd6vE;1PJ&{*;ix?!`C|PyxWXZP?H$y@6f6-hcTUlP6L+VJeNvP@icNrDXtcrcK0BZsZuJn}=S5rmKX7#W)+mtFE+i#HmFnPom~4%ctdaRDD+H244Wx+;37M!b!pqG!VN9rbNVq6BQ^@=v3mLDYIHm93fTLm;x&OCf?8_gE`b)PI*WU;%$p!y@Sk20=z|r2qR2Hp5uwy4(Bk*s)>V2#lHa9^UkGTplV%SIvbAq-Nys9gaLa7_N5vhs#=pfRjly}LxZs}Zai3>J=>gcGMqDT>mv$467SRHwl`pj@+?=i6NM94oERd}7d#N$3%qe>3P1D_7K>q;@ebMg7pTj#E1VZ)APJe5hEFAkGA6On+A_3rUJiHc5R9e>WdA&CFj5wZ(~J2hvK}gjV{#mS-RiF-jfkWd$VR^=(MsF;t|iPGAej(%$e_F@_J!r8x+8Fcq!EBXGx~4#)sPni%dX5JL%K1_$edRBUthtPMJe=m2$K1%!+H*5Zr%a9d<lbEB!gc8SAGIyT>zEilYyNVfXcPzcdp@+LjeOkGsW{9ELlGdk6@xx?*>RdLmjW~LlX_Z!4+oMV?Pz?!>o+8JiYd9@MDcZ!W)in03N@LG=2l>Sfh}Na4I{Ki%8?MDZp<6Z2YZ28oS^B*m`qcU)+oREh#}>AHTCcnN7FODK>E{P7Wq%B&J%W1k0XTxUBWX8B0Ns$_`G|G8uRdZ+tZw$R0G6MA-5HOKjU_nGC2}R#M$|(Fv=S5|n(P1$og8>D9z8{3g+_^liur{<E*!m1q_PrwhD^WSm$oSUR)Bej8+6BjCq1DdrqmsfJYCmFf{4^0iRQQ3b)<#5~$YDZwrlX)H39L9A5J37kx73d>cwa4PkrdC70w$P;+=LGs@>MT+#v>f`j~nR|!`32PdA>DfX`weokITZcOy(61Q?U3VmUXr_!pC6n8V%B6V`F@_l{T{uN*Kelx<HO+K*rvT|v7b~r;+ttP5tdaHH+}3iW)7kP#PeL7Em^8T_&LSC0Jg_#(A`0`sFUKdmfy~ZU)5^fnglsiOA;3{>GgEOfN+CYYy0TMREUv2~#?2+`b|({gn5-Lo;$ZanTy%ij19?<00s}*h>=>?B3!e^}#>&`M7w-FXWsW$`hU_D)%74u$oqt4x+$QHCOnnd8aG-OYxG?i;V@}ORAkXT7%nO7Xr5>G!uuiT9CBG-*R@rZZ6sVIPRQ{H|aXmz%YsN!pwv?wOGl^H<IeHOn#f=b}vtlg<J0I|KPhhQYEi3b_9kUiriX)>yRd;|AIHq&Rtb{9zm91V*WjJc~=J$L>f5&DE!L!J(Kw<g7;*`G2YapN^&$BT<m+96W61gbOH73p&o!zlzpL7)@g5HxMh?O<X!FqmgzUo*9<>L8v^<&|NLi)pWD<AU@syAWEF&bPsH(|<=Ld7Psb6SO4WVnHo56L9Wk*ufuD7fbWOZ^BgTIUOD9JL#UCv31<U$+%yr>I1O;r-5JGpK(Z_5@+ExH!Rui&$=$WFCC>LESBC>;>4(XThdLFhWs_mA!b-EgBa4d}!I*CP&+4^^QJT?xNn_j6d|ouqgaOWWkQNaCx+XFJBzcaL+VAb#N;%ceLvzbL2#S5yn8|#`FfaK6p_6fB>_c!1P7RDC|`2!kzJ%2**2v<DVt~3$VMlsp`tIl(RSc@Le7@mD{3^8*#^!L9u0PO4XIc8~K-$0~OtufB2q)`*bn5pVZw&D*ZILr|%o&`!G6atTtMD3h|$2`o<!?K*K#r=Rws)-gJxg;~eWx^3p(9&69+S41G<nLHDOgLcpk|lK&#a=LAeBQU3mQQT|ynJ}#yTYth5bfxep_riv9~ScUtc_{8pdxZk}s+z+mI=MlfZ6z(@4EZqO^-WLKXU)^TCctsf8Ef7d`!5yDfs#?~K+k!xHV10|@`I;rwQb<X|B?Y_5hbg3H4*LDF!W6YgZ5BY#FNA6F+9HK{O5}11%h7<^lF(}d0<Ri+HPn&iup~vN(c`39AYaEkL16S2?3EH=WWp1mxzl3Aag67D^JZ>S_p!N6!ymk-W%w!^`m{s(HEifruA<q767I9;nU?kP^~`7m2wj+mR4kqNCTwUB#qRBZc6wL<2gYh)Mw@9wdoGrc6P)X`*v)}UwbxJyS_^)7#(FLnYztM0lNe*q2(=cbv;9z})BnA%!pP=j^2@}$e!{%s2JN}=R1IFc)ak+I9o&0&<i6dU%D5-t8Y9L*SVX<SLw<l_3GOQdL+-Is@+-rg-_r|!nlBvMFb<?OxBk2NmwS8#S~2<VpTLLL<KtL;I$(Y<%?Xq<;{kzo`<pM&3~xcY7f+zAdAKKAU*3mz00Xx72$jD01dHnwF>{Mc5TjpZppkBx1*FmbF^hrudmkK_{qq+5Wj#MR$s4S#qfH-D-y>MqigYI1^BdLI5vrXkW(C&GLgDvNDCe4z*}Ea!8TV1O`bSJoEagXMN^8XWPyf(Z%8w%4O|SIQNrTu#N5I17hKeQ5*AL;-)5Mw=!hiHGbepGh?UBn=;nEms3%gaE*{#%%U2BXisv$?y72&MrnXU-@t*D6GiHCSJ$(tBVKLq5OXB=0)YW!0^@P%N=itOr49)!XmJC4q%U+GL3!uYP@#CIk1VbK8bXzC+z&uMf=H@L^=pHunReEhCJ{Acr`Xs5~ePe_!00*8HyIru^E7ytN6OOq073T@=ucB}b#q{ZEiqrN#1bvAwrZpaM`Y^}o7E$noovQ;+~KH*G;79e$aPB=Rf0t}dYYuPxL@<J;zAf~gb2PC5n#!am|Vo+-gn)Jl>MZOjDYLV2YoWpEo+8di`s}1G~Hy8yE_X@e0H{&wt4SG#RRk0(kb<3GN@~jCB5;c<Or-?e0Y=O$4{s|7q`3tC6vG)h=@urH~O2<?lhYUHt|NE~UXD6c=N)KVKJK$+VKDzIzQy2Er<hph^>p98bwM=(A>;CCyOva=h#4ub}2GvuROH9RH0xCGBH$5~uW`z_rM$!$NEUJrE04sr6<VQ{G0~<?6QyECp<Yv|gq4k)4Hr`^PAf%C)toBhA?L+}<EnSzv)bZOz6EDqU%~mOZK1!IIeyL#Yabo(QN|t=ou8hvu?$?O$Dw$u+f;;!5cUo!(`FLM3(e%_Nb#XC1KFx5a$>!TEexdaY`(Tu*iIXNyJIws`R5vLfET78f_Nj?muD+{Gy;t7G0~b<tE|d-`M&W+!tXpf}KDksY-#A}Po13`&UA15%b#^9UHK*>&p%`dZek$wODF2gd!9)y?<0leTz+)Wiy?8OqOa|VqS-8B>w*IN#Hm<*4B&PpF0f@oHEdWi@*-I33gIOd91fHU$Raf7-igh%iKjnq6`41-Ih-kcEU?jCCvTTUy@%5ty%|`x0k+rVHUavu_ByJ5Hv*YY_yOR_Rg>Sjrerlyn)Dl4s$hvHf!+uCDl%_2;VDCR?z#pqPv{j#2fNcDi4(HsDIS{~UbZ~IMJ*o^0)M4wl4N9#Ili=G1h@t%FQ@#~9D%@7tQ;$?T$zQf<adR3~O`5z;4Do^s`A^<FBYsj@mb4#R;>D*)@hu0(Imc)sse~XIrd++)4Q)zi<G|T_wY~uMW<?<a**lIKP&ffTjg08Yxa4VnThvTQ&4{UP$tC)pfIu+Euo8(e@v_?TBI+1ok`^U9z%A!K$n1e+j)x{s3b`((EINlnH=*ill^*f!wRGHM{r$4mOXwhR?E(;~E@U8SSE`J@yg7J3$pcaPm`_=N_;O6s+E5h6sWVYCgmTP=6wb~PFJV~<Qm9I1h&6t1L0=7w9o4#Ukf4DLPQiEuQ<xJ8oHqTpF7WZ+22>R~K8O6jGb?}mqEPZ<mh3=^qf;<`L8=|30vBs<EvHR9mq-TsQHh8ngQozM`G4<C_W4*84m!H9U1iFPcVe}_6PrG#!`U~@VR7e;;LDf7`sY~MOb|}lAfVB+n{5$0ui~>VScM(H{G_uy&4O1#L_k;M&h!_%S%x9hH)XlmXd!>$b?MrXq!y+bNz{x4E~Bn<Q%QI#7769)BLvSCMF-xB_Ez|Rpe%&*0}hVlp$}yaK7VBUH$E_z|C`lL@{(I%Ki$_8JV{0H#J?nXlK4Lt1y2-PVH$DG-#<$cvJX?Q$@~36cqlDJ2)VKAOZ@%BioP%$JzSDKQ9-W#Sh>lcw>6bd^{dyB!pI98-atP0R#voztY}tpt1nT|HKIsZ)qIVDE>R292{(*|vu%yXFnbL!*VfpssSy(zUI`+W8)(k*UyA@-J$O;w-B7zXk#0l)shJXOm;&@Q^IRcDi$ARXnOD`14#0CsYXaFxzO%QX3B|uhn~INH*N|bX$$tePfQvkv9F9W)?B3$_eGQMxG4*`yAqN<F4L6>I|09$IpcLBV5HII9nAOeOt>!K3==SoJC%%{+3jU?4=BKhzY^YEJ$_mcR*D;@@8?!%d^LO!-^6A|Osle|AZr%gC3-=Z}ffzVF-A*6DSNMElU}#|#H-9R>!mmJ;lCra2*W0idk89+o>ge^QHOJcXI;%Z(bN<KbO=;d|cr%8n_GIoU=EZ287zq)`9`}RBg2fDM(zm1s$9N{rfwpK@G#XmYM%SX9C<IWJ3sy$zfLvCz_5qA>u7E&Hx?v!WNj>B#a2L)1G$2Ov&5aQCad6sAO-|K*qM}(b)#09n^&2LOs*?;FUoDeVGZ9w#1u53z6%6^8RBAe=i|*`$?6rWbZuK@-^elK9;>I^!(`C2z>;!ZxG+pM`Zw?ka`LKL5l|5{38}sOHLGb0~%jc!(;B9GiOQR=E&2XM1fl00)c$u}jL<YWm6$gIT4uEqG@BJf)(0@WD?EJ}3%j#PO=Dr$Q7LxB6gSS{UyF|_=@<|P?AW|+Cd@L%*1BPWKtqE?#!AZ7c<W7dFV<&_s31$@z=Vf|C31=iCc_atEhWL{H_kfAyt>^E?PQ%|TzuAK5Zo|asl>aoEyx;MJ#)C#PvXyKO_~pR*oe#nS;ypQgNi-Z7{jU6HWs(B$yB)k>4(AVfb=>0j@t5DdRKxItbb)+wa6ZwLs;Bxvp#xy<4GAdE{p*fy;#cF?h+qcQ#Qr7(e!F6;QwhVz!ry1afMtwTT0^$-jHYl+csE)c9oU*F_;3vZv#x{wUFeBXb5gh2@%JX13_GSV9+srduEL^S#m=GyWKC*f&|7YUHP79|A;?pO#3|??Cg^}KS5XyV3vN31q$JQ{`5I?m>lc)Wx<BC>Tl#cxSHx?a=pS8L*p9IH{p^V>e-=XO`OXi^Gb!)%ULC!1QzZ;k2nS`Xom&y3Pb7Ut&d4kvl~eL=bs;PMbti%LZm7)Y2qZK^;PJuZg7nbsCu+iJU}f>VrfU>3k7bmYig1W`ZlTmHJFAnF{$?ROD-@Sic=(U4un^hZxqCJL9OW~zPwqw3DSnn5+MHA$fHO;5hcwcx68~*Oos<nC1a2CIrp%ffl9+M=oF;*!4SRAjsrN{0*wd`E0XadksnbH30}|Sb>Ia5`YF$aL5TvkuhM=8E0|goMhFWhxn8N`gC-(#&imYbiIKotNe9cH!9BS%}FuzfN%{!{21$08d)M7&utn4k}U7|koUTlLdwt7s#J;9@qCd!dYk7}p{4mW(5QKfcpZU7b2a2`)<lI37v4r0h5E~Scfo<`G;|8D@8@+{!sJ!Zgyu&kl}^v%4mX<bX_lk5TG!=_H;D=6+%A<|-F%d6Xb`fOutI^M#rV!|pTCy(Td&1bb8>~5K)b1)K1XsPUd0*2SOJ4_(C##|D+8PX0ypER=GCwey%B2lMhD#<QPi7%3NQ>nQ#Gr{6dZSU07&NK~U9wpMo+3I6?zZeROQ%c2r{?Fn{<Q}bpsVQPA=G(7K;o2kxJAX%M&e*uQTD~yxesU*q5eF^o*kVd(<r-(Hu=0ygfU(k?o-gB3CBzGMu?6$@#Gvb@wG-ygq~KJnW?5S@-L%xs=o%En`Ni2j5&AHoVI3Bc=F-kqe#yXE&TZm*b2FCFm4B;&r;5$6dFHg82xapV|Lc~Df9CuR%3Y5S+{~X{Nf<XdFeEzV9xMG3{534~<lhNd;gAQoT^>v5m#C7IBh>unyKHA+q1+<}*0=1SJ-YQjUrIf0iXvClgZzemo4-zVEFxzZK|Rte>J0$VkUO-k3iBRfOo%Dv7;_WcW5LP;<TZ7f8<gt?=%4xx0evo!Orpl{{)l9@^p{5z$&MVlB`!6fX^IFEg%nJM-QwUkl~KSx=5N7$Lo**{dvtwQ-D>8dC*@Fdd(2!Q(`4h=Dl_gfTyI%d`Pv1Uzw!n;wof=~+q0$X+~&b44NRU@gy;rnD6?7`9k{9M0`MUoF1SMU)%kt)l|9sJx9llpOP6mz8M_L_8q!xD{6jL*Gzi%q{5A?0r_rxc_Roho_&a@j2z}>|Jt}8i#rnKq1j}GH=!iLwYf4Q)`xd3-TV^taqYd+HH$e<bcdB_))U|w85wr@sdRF|@F=+aSTr+&}WN%J(LnOoMOehv|xVVR_C)2n$ZO$5fnDznBK?tWumc`aPlRr(r%n12%VAb&>JA8y&wAKgRRzRV7m*SfE3+~4wH&5Rw(_m%xNwM#d4Y0nEjeuc0vINa0zmu$US84b1J;t+U+t@9o&^i`#={RyCxgn|HBOPKl$)b_39RXS}jvZo0*!)4h<3_s=w*Mc?J{S92BSI<VZ=@W1Bz03^0D)6}G*}6Y_Q+exx8bile(=#v1Xqj@L3xCKp-8P|lQbyn<NZmz>YgJ50HahW%<xY|e~nj1ZbNI)k~vJqE<XaNQ3Red?%5+<s<@`g$>^5ajh#xy;KR{%6%Nbv60s&r8XptdGX8tjzp;t|>tm(*#Dy?0pUhX{V#f_1X>0am=Vmd501`%|!t-|`!OXU46!Si6_*)VT)ofmZ;I?IXWz^_|-?rk5j$(h@GrrhIaJuo?<Dav!85qs{x&5Y6`6k7Q_8FLk{Cp9;x5hXwnDEAxUR|ZWAb*bTQ~9-)(Iui?n~~L$!2}yB5HLRZ;|IJz+ge-TBNnTvEZB;iG+BR9@f?1yVR0G)MnbS5k)UY~&zVW?(GZFlia7f#_aN;7?mWv=My$#mk(^;q<p?x#DyE@+_rJdURQ*K6T7@52oQ*#D-t;Am=hzwZ8xky>AR3B2=zg6DKGG06gBano?|9Fk_Q7&eYJe{?NMAM+frul;S019i!ANaM^DVjPFq7VQjwI~P+=ogQGsGc?2h|@rXGx6-3*b7zQOV!IBLK)0DjTK(!9W2<2=i;r*%A;(!8^)`KX8EsR1sC{4EZs_Lg8Jl1-?$>fdevDkOmT3KYf;sV#|`nX0C`cs_Ih|eLcs+EYc;5S|SOs$1}Fxy`7k+HDuB-VTPE>sudRMx^jlUF-%E4!B(O=*t}}app$AWG)qK?J$k27K&%WGj2JE2Xa>2*yxP}|L@k6*S~SfuUQ|;En!L)}5=drG*Vpgjl=o<XnEB-*dBG_QC^@X1GB0)toms#*i=G!wS>?a(x>L@VH_lFZk|JGs<l2h^`0<)Yb~JO@aIjIfAufFFku~0mo=~GDQI!$sXm37u#Du)hUYPN~$ny`Pq?5=oix1iQJrZ@cd%+PashHJHrR3FgPHb6^#-%}w7!%>L8c>3woB+Zhk_zTCoFAOyXZc1lEwzQy#YiqKLb&XR2~yMit8k0E!Nx0^OOE*Ictv7+Vfd)-IQ_rXJ8Xy((BH3*Qd>3<NE?41sH*-sZ;SJc5_j~G%{ycWHDarI?Be3i$d+*X!p>;N5~W_-8Hxck8~Du5;2h{UDdRoe79fFtDMZZ{iW&onVd<u25KZc_S8a>rZ%LXEm(i%hz2evqOa*j(BbGmYC)Pf#mOri+y`!@B!z<SQv8?@WXS1v60(Hwm5`7VYb{|<rI>bL?Zr}j@F25&_YJSW8+z5GY2e>tf>aD6NyfKnSsh`$V7JDL8$8Aa8BKaz!9bw01E9Hikx+0<II9fXAs-qLc=0Z{@a^v8v0CP^UdTqyaRZCXWz6ioT0#k9_uZ*I(TO@mv@(F{nr23;sSDE-FPVq@`hgx`0cM;>NZjt!8S9xG0*QzS2)sky<L9~j9Oe=KqLu$w<KhSlRo#$qj)#tOsfmtGn07y8zOcdQrt9m(I6uGJ|45t&VD)W@S?4*`=@0Kp#nXCyfr!X0+1PO-W(xVDx4or<AA*cPcM@#RE#uAnZjlmV&D!gNFl}T$bzOc*vRZ7;jkkTq^d2X2SIbzmt7b|Nw{qG-FU$b=6KWhNw6va2#K5>dF$X@q|fxA3?vmSA?c88i;z2p&n@rd!FM@%RRH}QI)_$rS`cSxfM37fZi#Ma-kx_H?mvPAPp1fesQaXk5O-8I&vi+{6gY^!c~n`>+?_(ex5{}1ICgZrA%Ap2Y|*DRr9`Zdxc`q#F;zT_L%w=bnfozz*b2Z3bvSGDrFCEw!s76EGZHgXjAZFNev3g<c{SE92F=@q3)F8r}%NOV!CQ#Q*TV3Zop6ep~^1_=q?TTYoQlO*@3Z<#_wn&c8CzF{9Ysxmy|EzXLR>C!&X46pl8iBb3eeTc;9?<^nCa#H+5Wkq9UZlGTKfc>j|0QPRZtP!Al+N9zG!kGi$Noo}Ni4TZv0Z6@PA7Cr}BQO6D|M9nh4?m+qGp$2iyGB~}5J+Mv+pY13z}^8L1o7&g_4ffH1vLhoV4KF8%xa$Dvr56coX4Kw4~wiCyF#%?>GvrFQ7}S45PK{lmeD~72>f9rxAz0Vhm@1(j9Jz<lzHi*KaNxq<C7dm5?UAh;r3KOulCdApMm~Aprnlz{m0e&^`}9~l2`pHr>9=_rxGno*Ud+AefN?-MZ@^{q6+GfZsAYs7yPL-9p6%JEY7qg?uMQe!^|VyXnsnYSGiIA@4)8?AKEUvd`!uG@u3=Tr7PUZfwDu;S}aK)Iz^FyzE6SVOI<z{I4AF!ZwO`EPR|HJ0Wvi)2TewVvyGfU_@G_BKYq{Nvk-+|DJ$Z$-_{K3y7yH7n{Lamyl3-n85ChjJF9H4^ZhCZnj>G}?E^Q#ZMROMAbMKLis5w`RExO~_aTalz-@ly%Hlt_TKKP7^)-Mw8lqi|MjaqV61c1Yy@Jjw`e2d~8zbjCJF-M{ldr_H=x=7620>0VqZ&@#IHF>OsX_yBe~|E(Z_DsFIELgs;b-$otfW+mgDk`p@`BpeB+lYk)y{Fs$C1@OFC1Ug#X0S-arhqaER^5!iDK2HS@W0>cGL^S0|TXOtiwv~wPCOIHs|c)0_sp4F$fKh%#`)m#}X^$P$ZG9>3?|7UbwJGU26KdX5HYp<cL>w+xV;_=Fxh((Ip<|c#g**W$osQJFX_)f<h;?xn`0qlsBcG$t0Df@yZ_Hrfm48A{)>+NAuekj1gYE5er&J4RL<;!X!Bf7X!Qn&@&#BuPlw7fi^Zz0YQ{k`d`2Hzc+INiyPwkbjFuNY%P;jS%46fzQDpBoWJ9BfAK6s)C1_DSO?~LHE4}rU5PtKwF+pwc455|lRo$q6E<}a&M{%zXE0$oUXL%ugRcaH(VFB3co`5@W1n-~aV)MjSk2q(D~n0r{B@x;9fDLkUx5SLTLE0!^#kz@&%wXE#fGh*AiSu~lp}0OI$=v`#6wsKOt^9m=ZjR3qD6@wGYgoO1@+B9v0&n2h(%iSrIk<-ZhItNzMWO47%Fzuo}#B#N;6d+`}Z6$KK|3N(b0{+0-g!v0DGg&8Er#wXJq&Nop^VraoadX(VO7kC!cZLgk%z)Q=lX|BV9rPS7RInnnii7X#zr%+`y>*qSzLK8$(rYfB0VXwP@GbcRE7J0^ioKpNd?!W71-eI($-?RR*wM0BjU%wDR(5bvsXNX-qME$EF6$Y$f|*O#wO^n?uk*hdm2{+XKkZ$S=OD@^`f~<RlpZ`CmTr?U7Qmjw3uwP5=PwW9marSHFs3vlB#!;dA&v0M&uZ_i1_SIe;qdksM<8A<?M@O--+brp~z3?hW}V+l`T;<Izq`q51Kh5UCm>cEqL5)vgy1se+?=>EoUuVqC$c`nSMg+ya`KP2LRwnIrG{xvzW@xW|tRO8xt6E8H_|ynDrN0PREx-?y;gkGhflbJd!b!?)+VVG$&1QY^=b{nOD3Ziu$ENIE~32Zll-aDOIs#T?Pbwunt#m~PH`i&Pj8ISUxO5->W>jEkn$6;aiB3?{ifsnQiirm_{LC{hoWgP~>q$CtSchLb+9C%#B>W7$KECY{z1r7Ng1k&8Gt^^qq6953eI2z$WO&?1faikJ48Re<cAE5DvsQc2Qg!}NV^8MvI9`-h@eS2(sr?6P$6PW&g#qbL0)mnM;A9<wdK=-gUKi1)fEa}cjit4*>Y$%}ZCcXNcAG*3AZnS&RSY6ITYWhiUrDT}k7mpES^c}8VJQ+Tb4wbMNAJf80toUHMEZ*c+{KOXqgH`a4_Z64^pZTQbhT-q<-Kc5ER69m*NcM{eH3|?(1%Z_ite<C$O<TI>FQ(D>=@SoP&bY~FIWp|U*LJ<%5m90&`Kz`<%zaQrAX8mg9Xa7-sUO!Ae4^Qp*>J2f^56a;^3w23|<%39Rt~fuh_-$%c_+=>Q{5iO7Rx3>Ht17nR^9kxxZ)ZH)pj~eVjU1l4v{W<?Rt&e%g22OiPqa_!AwyYTiS%<emMB(E-iqBzF6tmRP!rl;fq#4297}lF$URYWnEGkgGoN{5H5{uNHRT9i)speLgQ-j^>#=AZG3H$0#`0<GW?{cG#@)CK0!zx3)2~D#voJdnY!MQK%v+@WU{qJtYv$GSGZ=^HKVjWg)8m7P8RBp(!^Ys7BgTV@B95%=xaJ!CvK_H`pqmZuPUzFk%C|P0Jpo-$H1c@G<|1z`ghCimN`hxZ@dSx<*I2FVBAdt2B_|GR1|*nC$&NuqUgIsCeENd1o>ND%WjuUz6U~k*OfJqO>TNzH>GT5C(qf^zDAVuZ=`R!{^5sxdXb~5$%tr{qg&Jdu$Z%J0o6djn%HmIDRJ*)wsb*uZ5I|eo@$KeZ{0eX5?yEBo)kOGs9xOfg3+KL#5v3|~{7+7PW+JhXcs^)9UD4ugI1=@hrcW(Cp3m*3ax=34DPK6-7X5$oj$|HU@*s5rtloiR><coFylYb8KSy@AC3Wb5&J>C$HlGy5>e0eC<gkH~i>wD_L$)&@YCF+#Y{b*Yxer=@xm2TK#tajsnOkEA@uQbUcVgWvMYGZQyN)7_$k%{bA{JH1P^g-jC%+hJLlM|c2nSc{K_eg9mb4$<*fzl$QM09D%C5>bf}S23@5I)bpG|H206~#kM_o8ppBfVXM`yIUVg?P?jxJ;!)RT!Mu{QFcupk!Ix|B}1wyNbllcLg+S;U(HmE-tT)WuG`F!S4@HFUU`nqaJ@Ja}DrMj>Lt-)mYD3n~B4*OIRdYu2V3thOz%Y0&n{Aw^!6ksJ@TD>U0+{xt!qU{qhw*Ym-2z6`l;dQ!m{X*s#ce;DUPi>D#^AOp;SYhTCr3%M)c^~HxC3KKI9uH7cC9$IP=4n_{cslh2JK^)ncfpgWYd*v!W$qJHCStN$aqYLSUoxj&~YAm$Vt)nPdOCmzvfiT-pQ!bkcs>AXZGiuscQtYz#i`T?%snblef&^|ijrl<pVY-UhJ<I~km0zAi`F83&i5H8!@Z}BKBs1$xuoF;u9mi9$KJjg@&oGDv%9qodj=5m4j*G(<ibj4m8O!*Y&~^5{yQ*-v<aq3_nzG<mw(h`w`9Sh_a`i)G5WJC9H^zFDx}vmYT(?26+)7Ze2f=cy;%K@3d9l^t5S4}UV}4Iw!yRtbgVE@L^T#C<LmMl9Lcy}ke+JKSW&;@HPwh<K!uqDMP}tqAjwZDc`^e|uI5K)?Bi!@kxQk%cpN>o+_j45u{WV|IFGY<8Ya#QOB<>Y|3QRlsVh*-Pu4xcbmW`XH$4h6t6??nSkvkw_OysObrzuyRkHtjU@`gDEk5ui{Dj3PmWVg<U1VKDkM>N_YfL=Z|{#y0lSI3`5QcA?fhv@oPZ+X`zMQh&t@PPkq?_GMRx(AMD=kp`y_?~p+17F<a?|UFvGOvO=gn|2f<U73Wklp5kl~A`2_;Rox-{F<~sZSrQ6WKqQR>$E~=o0^8^*bbm+q?8R&H^fj;`qKZwU%rn(M|>BXoMgyWLumDG~uVJ_#M(AcND(QTcSO=ItD%)N?G!Dbo5Lk*qz-$^c*BDrpc`QO^}T`<r9w}Q5MhN9V(L4iuCs4LuIsCMJE;C7&*>;dmjq7mmkQ_rH_1(7d`lA@W1L%@4OT!@&_S%L&$>@H=*aJ@?zdvLo0_c^SMz-5%kabu=n|_Inmtl@^8pxSGY@9-bxVF9BCpB<nWG0^@#Kq@BHmI;3jWLz)~B_R)FXzsT&ESOs6$y5^vyr>KW2A93QE|<Vl&HpXaeMAjpGW?CHds1#WVSg*NjxQd)=|b)>d_3)n{_Z)4g@id*6$W!NoH6QV;D00!9x5eEQ2fNwhRy%$TI?PYUV{I6U7%R9>-x5dXMXKx5VF%Zo)eQLJB{NM63`kTFL{)zW>r+4Kxw=dn`B_-zVmHWDz$S?^*)lFp$t-p9*TgllF6g1t5nmo1v`XuT6cH)-wIab`*9rcSlimvbQ^f|D$4N?Ms++&2X{VU(Vy(F1qT{s<9ceI0$4A8!j>xuUjNv{JWG9Nurj&=q3?Wgsjdo1pu3V5i+3I=hHm`A1eyny{0^Jo%(CazVmhH^9JC1nyJt^ac1oU-UMZl1h3*%P?7tO>+rsJpqaxZ5j_Vzsgvc*xux_5k7eA5}kpEyL3RlD^rLH#bBz=Dh?ZryL%WU7LAUzI`z0DV+HJ1Rz$}K_Ux(l;>p2!YG&8jo*vy--Xiw6)sU95!66-hYiMEPCoQ?7=gU;C(uFV*dNm@$F_=_${QVh&|MuR(Y6({8KbV?zvMB2wcdgWJO6#G{bn!TJXZ*%@FKv<LttGY$T}x}?{J{@n-AHF<P(yz7;wNo49MR@-q8+hE;uow$Z(?slU&t({^(se^K*jOU(w`Bbgb>UGFPX2+>ks!<TO!~ldNq^_mUOJm$kY&W)5uPh=EJ7bnl+%cA*q0&1kje*BV~1Js<)B(KoYO&hdH*P)pK_MC#bBtcWg~;GrVpeIeWL8R~K3x2EXvEb`^W>`HhxgpMkcBX$xHL`1z*{;H+?m6*^Y?FwSjToLk5bSDxV6kXt~&ug`L<=pK|)W2ZqcV#Kr{5B=Sa`@KxTW{i-py*GQ);(LyL`qHS+ZA2^N0So!cfXd-i-&cGoQ`x}?qLYhQsf1sDi*$t9Z>5e$O~Y<mtr=Fq`}N47SkTaI1xG8a8=fW3Kxu?p)AHks`V!OIzU&0aEVF^Uy$EWQ3-_uh(GYJUPW{kWwhCt0XJ1)jp07yFRD{Cexh7-zK};Qgpp8ZL2?)Y{Xj+6+DQ7A3P!3^YBRB_@@E|gilx9Amotyy3j7MYu-5B^gHpf=Y;*_*Q^?GGCo#Sx)OQq9%Li!w^qC0bh>{xO(xXsP1MF#gLJ)s<KXLNK{sH$t-c)y1F~trv24P?d!jPTl3BTM$|J98RmqTL_N{;yK&raC?-@UiO^RGPMuipjqh~g$*&1(Mx`(Q}{Ev*cDj@^52d_VjAhI=vUId>PN0yil(KAcdS+KL?L4u!;cPn|dHz3`oEdQM_F3h`f+xlTVdTb=Lr=WF-aCA6Q-R(~(_y{NRf2XCm~#HOo~ZP>=_c6y8FF(n#oKh!B0F|m`7(?UxzxpCRERaVaql(gMPE)l5ji0euP%lsHyESHvp0YN38h_U|^Cq+dGZ&PZ5<&+KqBqTJg6Pt3PWC~z47CnkuM9u*V7RdZ`l%$N>Obrpa>;#;6Vtw{#2l6ViHbsl-MdN4^MV{PZg)XcCF5B;#(B`W?;zkT)Nz6<7v;3D&fx^!=b9-mbs3~GNIjtRj`UZmbypHQja(dWBk*t;Z`Je;{6v(7DC#EP?@<u7`vF!rS2OK)Z=MA(%aNQ)?u%vhOOA1=iuZC!<4%`pkN<`@IRcu;N8RWr)GE5qvAW^)ZFf&W8UUAV@WfoVCccz&&9EeJTtta#%&P|HB$Uk9Jyw&qfC*6fFSo96{DN!BS{jm$4>5om8&u(2P*viUZ;Juw*<cLQ*5&lxD)h`+=g}!2H(=5KRG&O{_jG=s8G!hTz<`1sETUEx&xW|2(dsPdOKLk+6RIO;vmwfP*biB$#i3?Kps_=|VOwF-0VvNe!)GB?o;73n|ZFy=5l?yL)Z7SJ@ahi?@r6m{7ph1<Jz(OuZw4reR8mGI_t)xjBU<n>xzEa5A7xIV7W`I!r>t8oCNX*BI1YGJusSXzXx0<n+_mddbc%Z(umkN0f6Da1RqMd5E#&;g-4i6wDY5tH0eM6QxaZorrat9kg))|RxQoF1{u@vAIssm+viWYk|TX6d-x(3p5BRHuh4L5FZb~jA@V0mB9In)>bsxiPthwl1&f^{~<S?vp7j<aoFNLhk8iEQ;T6h4E^6rmI|A^jFc6Kx#~+stUC=EuQ#iGa&A%l(X7L!-H4v8q?X^<TZA?Q$1(4N;8wm7U~0)!z0Z0nRab9CH+i%fk*C0~SanITO@y+fW4aN{2$>v@9tbEBIxrt+lAqHztD#t3+iQtHwvJ1tlpeWdoLtF1hdO%1mBqE-2==u19wAjr~dWbUgKzJ@Sfdi`pk*CSJ7?=HE%Ro=-_#5AV-9DUAurafk*HNU>#NVO%sRR92miKOeKahZa^u<5P>o8u|He{q&{P)Vv`2ADyhl7p=~)=3mcVbmjNHh=R6L?|D9mS1DbSSh|*)GM9$D3hI}68QJ(hSw6jU{uiFlr`Z9mifY(cr494xeHc}Tc0~z7ky?)yV|%7YS5Xv{S#=H!wvPW>TgVp3L#2E=UCXB_>@u}uQ&9vIn^W|bOcPp%qyxhSl_}Ka*SDN<&LO-AuUgW|Ds^sKMnkhs9dem{kXp5+&b!fs1d6y2f&>{vEOW)4AYqrvv(2+arpvAf)(zA??)iq^S|>F4&eZDMLanZ09$dpXRzi2=g@Xb9;$cZ?3gOFBR6D%PMb$YWw(ezkemqmt$sQ5>-dkGiG@Z=!p!vW#aefwmx%#(V{bQ)KZ5lxF@<VCpaC24%c7mRwjrXoUP`dB7+L2u~NT`zv)`>C~c{xQ%wC3ls!Qbic5QL4+Bq{x|I#LCajZ(ahkbMI_TDH{9N(b9BfElRo;&;K!B_RgMQSvfBivfO$ika5XKb0?{iNxy<C}%+0RFafDY!J~bNb~{vAnw@vAM>*qTki|QDi3wfbFSI+*TH2U6SY|a4=!{iRY|gg4sxJW65|`l6&ER#2zv@MVIM3Smm&VGY9izN&UFJp#xW}Y#gQ_Uun{|y-K^%Oh4`#mrDO&3*KTXt1*7WoQSv**G=yuWAt1)*a6PU;HKpEJ!M-c9m7c0FE*f4UnM^c`Y&GT86#)hFTvAx6LD;~@-bez=%4-1$HpH3hWrZzDe+4yI#;8a#>q?4FbnJ><1^BLghk69bPz3^+q%Dbg33Sap%kL0z(Ygo|GFveBDi~dz^wKy86D3Ss3TS#p4eSL;m-B942wV~wCXnnw#zM4rSH~y8zyC2yXZiR)M|>nHjGs`#_KsD|lNhbJHglAdv($)@knuh~!25*k>;_8AYH^L9SD2UFKvNnrZP6IJ<DT_?%!c7l-&IvQZ<4(0cFbGR{)Vb5Wf5>1HPuk_>iu30VMaG}SR>>#v4dzHtmn^@>h++nQRISQ=}y(qyc`Y{*NBsZ?ViAmu(vl5w41#!g;<GKhI~VQ!^tYIJaeR_KG<cpkiy_M)=u)!aw4d^<j_*C4Ra#UaSwfww3l_DLrVYRv%$hLQYc}<HMLrisxp#GeSra~+MeSA)wUYCcfzqIS<!S<BZ}6fb2YC+d9&(^JvNfII;ZBTZUnPWcgZ3$N;Z)VEgMgaGnO9Ycu{StvYA__;Z(`fGN{23S~Siv4IaB`yTSwM84fMObY?NG2>x2hoBuWh-aCw)qD6v-b_DcY-g}%->#@wy=N))sn=O_)=thFLP#gv#8AYrA^4-mK%?$FQx!$k)Ba<u#N?LemB=W{e=b}-oid~X3quuh+2^r2;011mKZJFlv%5L*pV7i~$Z7NX<6bb8n(R8D0yRhEyeow5oOgC5fRqI`&+BO;R`t1h12^t1`*@jOY5b-@Y30a00Ect0ARlH_$<BfX4NMn7xN6F$$X1rl++HyTgT82My3cvS;m4%!3t}E;72Lg~5cs>wdeV2ecNyk})r}8#&P)VK3=4mXztP~3h&$edH+{7mf%2tyKS+e^sX+f=Hfyjc-CVElzLyJvIsleORaPIjS5l+?2mYLpSXaKX)xaz)|CIMOg^cZgr(+aAm<zwO-fB;M3k(YTY(`O10{a{q-w@+h%C#-1cGAr5#4F_O%{?pg5P;*kt6}kls;%t#x@#X0v?aK;{L`PFg&YAo*B@M~jHKwvEy?j{J`CvNOMZ7F}^WJd-!UHA_n7vZ1L6}K!$b`j8L?aVxut$b6aWJso;5ny2nZ%mMq=SPG?<pkNyJ@*mX^{HZ?2`q#(Ob0bL?#4hsxrJrw=`^;NKk-}$Ep{h1(pd!o0C`jybK%P1ofxU#NQ&`>0?mue8n#OQ5MTzw#AaS*)P8?mYGT(XR!==NsCx!ZNmCAqfHdfgc8nl7S7<Nn&sNFfy$7v4<%<2vu{hebi)HET48*49>|!zfQ1_8KxSm89jmk}u}sa%s}{9ZM6Xx|@e3GTJo-FN@?aLlfSrn!-AdZH?g)c|BivzrwPV2|FoX$<_$3>k)1D7G8pkOf`wea#I#hrA-D8#k`}SQt3%$C82WS8Cah;0~MPjf#K+R)U>QA40nXn35ilgBSaEjInf2*%)7rq9{Zq$okdYNtUGI8=UtpIbgf6;=%w{{nt3u<ng^9bcaqKTN-IG0625SISM1qx2v`1S{|7yfU4xH?E9Kt#@iLNN0YROw!=&?=-Us_tz*0a0~ORLw=YT%i*R_Gw5Rr+8ZH^lCgUL`IydAyh}YP!Qoe=Qt=@OE4`$>UIjL!z!L8H~6z5HEZ{QA+@)VTJlO-r$wZdtzkvgX^kslF9OS|cD8Jb>SxJ%!yH?;i`cqD-$dOpRC%wkJ>tkiu<*Kl5?*&r;F+K*#~yqD1pGJh`f4?Z^GnEvap|A1-E%@VpHkdAH2oetKzMz_`bCaDZmskXk5%I-z}%n&7^yIhmQBmnLrudo<ft6Qh?M-0{01yIRqROOfR+FNLPJabrVf<U`QDBMx}j^{`{U?kw(^ay2iU|mV#Rqr3b>V?Yhl1=SrcK*zOyx$KN!7q*}S?Nora}qTD!rkCx&|Jh_}@|ELJ7t#i|<0SAIY)r}-NG<UoAQt8DE>uW_{3BN?(AOqY-h4b;u(ufo0v&hsbUiN)0@UI9yy6THpYyll-pSYRPVR*{@Oj@lV+M`R^0w-L%RVfW%*HxrydfO$XlQ`zt-<4|fEa#r7SfS3wugb>z2m;}>UW`hG|E@EeEc2Rv4M3>F(AcbDeo~Y}p&S9dTw?Rvu6<4#3s0EOo;*?_eAsaHz&7)evMND7h{6aL>-l=Iu1Lp4MVXV?d*Gw4i4Xap6^ut&*eXV0s5lETBS55#4nIUPG$*WE8_kL=ZIh5&{QcHllw2=9!)|vbnl?4EY)U;DxiF^5PAAXI0Ld(G}LFy_&9?+M*V$|8T%id!-pHjr37M=yZ7=oy#M_jqHpQ-^Em+hjdsG;ELm=18RGAlTZ4w_KO-T(3iN5)3N?8sVlWX>H~Rj^raOy%ouCfY(TUNd;D3Vr9%7U7E4sXZ_21No@o>58?XSZJ#+*M?Y?BqU^xuvopCf-IaHJ@r9DTFVH_n~Yu*Fo3iL>Y(2)Qu(o<goz~Z>c369hsyI>1rt{oJy)7jc`w?zmc)oH_jF-tU2)E>dVpSZGR~qc`K%SY`3K6*{^I4DKEN-frY|UEKv^Fq?3h<5)kyQxzEN3Uef6+YWq*&dzRhzequr?x&q11e;M#vr3z^0J#3?Ev0Igy!Y+mx;5$;}63lwe4tFNI7PAkX;f+obowRL~}5dA%m42U%=_)TRh$RvLT8%;yW<W>nCeCt%52N@fbp7UY%$gS9@uHv4Go5Ts_PoWFSoU!H?)p^NSqq;K5BK9p16>JIf)u|qo>#3WLFr@#?m7Ey!G5L0V_L70%ZJdGjaL#t~V}0FHjL7^{{#?NWa5-i#ToIj|5L2OAfvG}eBOL?18`g_pgawk{JhdsBUCUp(F|1E08H6N$YbVUBA@toMr*l$4k}r#9gngLE0gSgHRF<RH#>B;9HN!C(DN0tE(r_rWB5g3(t|JnA0_H8TB)zbR1)KmI<WcTf#o6p$mDytFXP|<?<Tx`*ax8h_Ds*wePFEA;FS_z`(zB=aX@l7&S+u4E<;Lq(uuS#hmqq|iUQ6$7_+K<--U;?lP<f;{D6tKT;u1!sWKk;dxoFBfDF&LxZ)$|S4A2pcZi3R1YD;HK8|M(SM>S4Rt{k{g#PbI&7h#Q6FLP_Inz#K<0{g|Eu+RRQh4ljRDWJc}&JV^bZ>dv>>2q-3G5o9}HyN&-Tn#cn-}mUFSvMcsCEk!+x{!&0Nv`t|s_(4kQ8+jDxFsECwD8WhVE<~C9dl0VG3aG1y@>|_CXCRSkwri73^HcwIVB}vH692z3P<kwSyU7ZX5ToCj<B#5g^Fi;F4!b?U<R0?&K&W8BlfRz+PegZMd>tqhSFa71ZtQDd*!@xJvmefOP9*m=<5zHz7yq*U;*NJU`7#CEgP9;BBEf=gBAs@kV6VU>%kfj%Ts~GyAF2MowM=&rc&vx3X{uGoc>4E>vNB;Bp%tM4nRvIHmS*$z&I6?+s7j4%N!sU*mS2VfdPhKo<iZl!^mTP!h1o&If$oo%(rrMq$Vfrfao-gcED&S5*fmT#3hl9HHO6|t~l6F?5IpyewCqo%goCL^a|yIpGWwoAr9}tWK%-p%7JF6+uY9eZpI}qNDq`s6*8U5tq`D9cyMm!XJ8S{K+h8=%OtQ=xMN%)h*6^Tpf}B5u|nc;s)$nqeP!@JLy8CIC#srqhB8>r@}v3dW@4I&1A$&axMy9L&%ujPhD;xcb^=paU(M$kjL&f<25Kt<G3u)Q%*bOT5A6(4oxrw=H=Br<{)>NfHPaGdvD(EdPApCUf1DThCz@=5K^9nQU>(bSQ9Vo!R1N{i1}_q%95H?OR2?I^aY4|<v)JM%L>L*Be)q;7O6zT$23J^$$UEyhnr7*lqdA*t*<e&0+c3<e9pQV^+zXHf6*pVS!djzT5Z|LKTpB;TF~BK6TCq?ZXgVPKG9P~NA&mLo=iz%}V4@1LLI2y;U(H#M+XZ*{6Rc7X?l{IhDNqjlIewp}W0M0_pxW|U%B}%43BKCW$cGJne<;A#uoYVw?95ME>~Qv~;YssN$~W)xEzAuxcYJm1Ii1`3FKFLRAqPbKQV(}C0^K42IilAbQr_ZW`eP0ef&9kekmT*jRegyg^8@_isMm4kdFwuq=(wX_Xd6sNb%F31TBv-2CjcsNK4bES+GfsjXjTWnkP}Y3svEygh+;q+*Z>8ia2a~4!QFBy28d1;ynMs9BwfRh-!N9kKWjrqOCPJES&e|VrH|b@<M_zFAvN@|+4CGhzo5xzM$5oXqsW>#RyWnqW!LeP5abzq1tNJC)3UqcZ01RC!|W{rK5!_S)8?)MdI)vRJ=7a8EeW^TGM?+$_u=StqzQm+&zangMXe12DJuAoYPr>%9H@FC5F@Oc?zpM$nc5ya6P5~N+6{bKOeXM&f>dj;aG6}qqWFL6oyM5Ow-<(ajF}PjiAWv9ieWr4J~SL`7|;<E?6N9JX{c|M8sso7Y;MhqA8jm2d6g$OGq=|0$IfQL_M5!EN&lsx4-T`Q#8hzyw|9eCcM>X}gdz`YYGa!AbAGSan*++q{l*_4d~dLk{9v0tsEwL9A%|{8!fEt}99M-tg!aJEm}m(?Dm=HSs`AXk4PM{+b&C6cTLoszd4SJegk5XmgDIR^)jK9t*Apx?te4<x?`DJ*-hhcl%`^Meq?|Qy5J4}JC$)V`O=f58Zu2}dL#ihu&4i?h)hOC9b1cnEiF}Km{cMss7HZz{jKHysF^j;FGf6h*$KJtejCo_{7J7|)DjR<?!0dUk;D~7aZDM@58eOJvg_2~h8txi{X<wOD#sO<i#H79qDhIz)bR5a=J6NHv4~vOquEaBpc6&y`7&Rk>JD}mzq7T5Ib8`$-E+4+7-u~XZR~9cKgx*wHtXCsS-&kc)l8WbjTv5_uB)`5^RupgJ8_J5L=D1c<MAw#A_lmNjDt5QcvZm;)piBZ)63%O@t>HnXrr4>bsP=8mC`~m*j!%q`F14Cse5R&YXXg(P{j^9~`1*L2#e6ltS^fKN{3-FKCvfY=GEK*9EPiq1@<b*X(OBa()t|7~cFRYzV<c2ppjz4U4F?)lj?BScGls)7t@sl1y4hjiO9ht#Dzf(X_Fgs=L2zW|SFjrh#lGVRSJt9FA*kxue8?f%_fK=qdBZRL@ebF*_A04XcvwtmkC<0R=Ta#ksDyCWe<}Z|Twp_<c6TFiiWLq=e%CMDI8`xKBNW>he%WZ&hVTFN>UYTH^eYU%@=e9KUG{Edv)W^}s&5c-aZX4=A*jRkH(Y-)2b*!glzNWw0szBNLmU7X<a?~}Ja371WS7sA?D_^Zr~JabUXQH38H&_nW78*pL9i&jG{c=x*zvf>@^|GIKOfzpWVSgFXm3r|kl+}9I+fS4b@7o%J)GD=CkaVFV4{;(`JP3-z_|&X3C~}tV8;Lln}Kb2(cJ|j)e4*e4*pB`Z~CO!O*AFlfEj5&QcHq%3@e~#v1~-qpgQ^ZCtI|{8bUJ021a9`Js7+j8k}3U38VzUxC!dy48RrGWy}1-DZ=Br5o=0KMc^Dnv;!$^0g2|goW{zcu{|e&Q#d-uQmlV$U`c}7pTSCv$U+E>X4%F+G8|>=R(_PjpwrMkkPhJBoX{<aMkb$R2t{Ipw-0E@1|cH}e8|B<7!~W7C|u=8B)gSI1F}+LiOZ@d*=fwzLP=69N(F%LlHf^RW3QZWCHL0W38NR4p~ol$47n$w|1uhgSBN>4to956^PzU4Uj$<)&B3G}K${I)z*88+qk&KeSN$jn9d>V9*3t&7IW!|xYX#2A$HyK-fujPJz~B|W591#{<La^?1zBnJBVix1<-+t`{2A1CtIwoI$#P6x8n-7Kt|R~AfFSiNUu|f^A4P^qs1P9OJQ+5bfDJoo%%23PxRDf+rST^`G~gPuRd}3GXP}*cqkJ@PV)W6p+x)us;Rs6njS%2fV~<U>>Ty6)#4Y%Qsu1S!#wW0z{JAM+nT8yI91UWGE+KeGPsoJocA<T#u*HK2Jr<@XU$EXrDO7?N(uszi1WScRsHzM0tRE|H%Sz&c)b^{4_9T|Kbywo=jZ=smx`t1m>wIc7h|8K$xXFO#qiv)sP_Lr!u0-K#Lp3bRi!KJ3M~u9|?{tMmsMB10Ne^Nyl`2l0wpU_tL67EGoKCrB1T;*@9^RkUQkrKm&z-7fq>-s+Mf7?Ze-H4&xato)HTe(Qy3VWUt1FOJ1>dNBaF%z9zr_oUa3;hv%9TUt?}$c&;2Xkdb=%ZxPbpt6=z44_XRo}B{|hxtF2iiwYN1zAjLWejKrY$fCQ!$028>>fEuhHRhM|hho7U{Hj#$zR`_>s4gOq4}k49$8A^Lh?KW$`U1tbq;<D$D06~vAkF;ZEOvpl#@|IqunPgUOapsyL2WT%jrGiv0>Zq+osw6Es-RNG!Ph%d2tLl38GX$9wa^L+wd&j7t)6tcU+@2ygU&c^}3-F-fX4WOIIeNUkW4m;Z^yFG=5&>#<}6C@(Odflf$R;JMY#{0cViyY2w6|Ludw>a+AF2=oBcbL`|kzbc?TRq*j+Qz!pcaBx5p)#ha<^5{_G}0|(IjaK7^ad6K)8czhw0ovU`Q=;KmZYKhjhQ2xf9LIN`!JN-2~o{YDwNnjsh)4d4>4+xzH%e$km&w=r%Iorw%(l>pPZ_mQC5Ep>Kc$fgMq769gOmu%{sm_atOcm4_I>0l*_k74e2{zQiu@a#BfhBU?C84Bz?SLJQ@S3w*B`AP>cL_)w0P_>^C)tRbyqS2Ec$eKo}+jU5JHz=MAsML<Lbi{)%9E7~I6u==K!ZiH3w`WzdheOdS+N?fIqA2y~-JT=Tw9WEQ9`SREM?;z{R=y77gx!HS0d`_IAuy3&7Bt96Utvkd_aRlee0n7~40G?KSEfD#LdTx&x>xS*pI1~6_v^_0piq9fjq{aTanbz;4tMYD#Gch)%KLLIf#gRWW*m5!JSTu!ZtU_b~@g^*yKvGR+R1MDC5NY#L<icTWC9tD&rdU8W_#|22w8L!cvy>@E`7Ogph_BmrcH>ItKb=wtL2VmzW#9iqxg+&J}%v@@28jlonhGyXGODF1~0=KZMo`{wFf*Pp&5(?%`Ba-#pLt7jqU*JrkVf;K{@k?Pt@wL^86>dyQ8LnC|DM`6^LK~_D%I#aD{k~izm7Cg_<^9nasc&28hWx~dv_=drJC;glf7Qv-5{?+=(+kx?+hV4?v69RK`kX{Odh0-vQm=4{EisCQ?g()~dBY_a9)I^5PmyJn)$BAt@Y!;l=8USSAs>;biZEt#iNY{}QoXJ@5nOu`)Z&$VG;}*K4^UFdj<jx#vMGHrs!>sN<_r*y>Xr^D{6h2r&<pGr=A|r(fwm73VyRBU*x~N5Ll`In7ghM4U^2GFIB3kZCypvF-uDIL5N5u4mrK%XbVCIz<3b^%oB8y`h1MDj#+Ua8YcZpbMJN!8`O*-Clc-r0(eQ;nQUf0x)O#2011a7EgJLOyz~Iwwyq<jsq0SThG^-eU4B>~d10e^o=-h`Bj6v%zpHeqBre(>;V79?hwP1VMqY;Mu)IeZN63UM9t_Izo=-&1Kju1xKEO^{Fxe})-0fDMHSz1(NgefuMK<q|hvWF5+wB_fFrM6T=$_oTi7Zy1~=uVb`qfsi?x;3u4p13gG%(HfGTh&D8+*YAKTLKA|v~knFnKo_>wiaeRXz0-38B_DSDo<)*F~bB?E(JlkD3!q;CJ$7c$`aw=4c>s`=dff0pB|EFom7+SQU}ybD(LDA`Mo#}zlIX41+!rXk;@rFc~4=?p?1Q|2R7MI$9TpIyW%JMwn8cv7G!fPFEzbB{b^#&BjB&l(PIt##%uekcO)shp(zf?ZIB(`p)Z;CjO>EZ-@+;1!_*&YjwGtX5W>NMV0%A+33|g|P-G6fga0%z!1myGqcmVJQheq}+l{~L1058~dwF}^^lW+tYptq%m~BPB@qco_#>&y}P%`Tx4&Z+&zw=I0Mqz)8FrzMCp&|0F^WPtMR+V|Hb_k@9E7c5o%<t!|b`Z%m24hxv?jOF1t?JEX8)T>JvW+Jp+qz~GR-Mz=m2EKk{|%IFTq)c5uUEEFZuDVlHg&1l_+`ze@)YiPsb=H-tv9acdNGH^_8v+s&z5Q?jsuD@e{8mz_N&+WQxwHj`dCaQMXX1gN)i<c3<p{JI~A^114zL%Z?eM|nI4PClOItXfJ-R|91^XiZ$1&j<Sd7Ic{jB|Oh~F=D6zMu_lH978l2Hkp~z5TWpC*O<?(1Q$V!pJv`Q!D-6ZOUqa`a_&%#NCU2#69sWLgkh}3RUTsnjKO=-p=KM6Wv(-@jn;zH%mI9n%~Hv(BEDo;NT)$q<Nzj0=$T!?xVq_y-DNgqF@1febSOH1lX_cZ5O_+M>azrr*ce{=5^?{sHyM?cHpX>utQa3fn@8s(Zsvm&K0rjaD`s&Ur9n)8#@d9Gia#q%`Kg&1HaKXmInP~puoofA|w7Np|J7yB>|KDjwvAp~ROT7CFGUM(7cipcCUvgd7CQ6SHuc=~3lL-~vvog)#(2xGe%XCQ3@>PU%b74+rEm|)JMkO9!_UYX_%aWIBv*13yhq&W}qFTi4k&Tuxq3?T5BQhG!AD}PH{CJyM-*tDys*(bUm>R{&g?7g8ds3Sz2!e%v1&^m=)<}mX2gj8@g(FXBiFz@9=fynXQNdp|T)E@k>eQA96te&9rCcXg!9vAMUU_Iz$C|Ni*t)_f7a<0M%<}C5n=$y!fNCF<=N@hxv{497UyQPkH7bNi!z_zrKIsKTP<J}v>U1<!bZ>TX0<k-3~9Mu@Ett%XzQquF5aJ<+O4%QFuO7i~bj2xI_;1`;~sWgMrx1bpe()(bJFTJiGyn(EaD3Kji1*|0;ZA;B9;Z11?M+4O_TEd!@P*=FNe(>RPKRC3DesH|l53V$9WL;r*r7L{@hOV%%4KH?u3vbZ3q%r(A=f?0)UV+L?>u$#xEzJI0Q)ce|CJymbZd<S2K>ZY}W`?HQRVkPh>RHk-5st8Zfkjcz5H+kdiMbf#E$7l2fJss3pN&36<7WoTwpx(hA=j2Pj9v`J2v$)6VPW5`ut5TmeZf&qytLA5CFZf=dh7h!va5{4>1{71xZZ4fVi9IrG63Y3jMM5MdUAmN*VxIJW<Ca>wwx*cqC!f8jycLUs+RkqO!*(qY8am}gt`Kd9Nl_}o#n0x_aIe5-x%oHDX}=5p$<s)u>k&VS>hxW5HnZ}PKNUgHYkHdwaSuMk%r{_FOiEbNjig_IDQ1cK+O*)aSKqbJ&Lp!gJcY7_(htg*VIvDR5=kEF%Bst0|7+M=uBdC!jO{DS$_q+N^b?zoXytkZwUOVOn92sRPO4_be8&8u1o~UbQ&O-QAPgXE%|v;gFp>4t-&OWVgcP*8wImJD6RCO#WIyeW?+eNG(_!TyKlU)-{cRs!#T_#J<VM~b8YB?@GW3hLlE+R+2Xx<FOYRukKMDV^%f6y`xex?TcXytb9uM%FJRYM2}2O_1iOx*2Tz@A)?uDv*Ci)|S(uAOm_5y_4UkB0?<sbDUd5%fas|HLs+)~5DL^vYC(2u?^37CEc^!N`J%!8=z8;xWH<j5TkaE8XyAD!Y1cZaP^1(8)jvs4L|Jj*s;8&`21ir@@gonUYjBQAW1E>bN9WkwpMbD`Q?jyJ{D5$mt=MA_6F^s+U{z#^k2vXp9E0VuLF+BKIqSbt`pJ2Al)vXg{1saz*bR|Bd36fMm6o#%&Hjbl{@AC`^Ys$9AE!_Go<F5`D1jAM89g(e=;MU0CL^Bo-73Xic4^EUfGLiuoHk@PGA#{k&j6PP!f#cVzhvfVAzpZMrZ})5M^EKI}j=+<eY)g;E$orBzn{w)FHCaeVxl}9tG<JA;v<3Em?(iZW^)}#72@sC_lMkl&wNSjw!mstMR5EOG-<;ay(ZKmb#k6Pz9l|l_(Z~xMh;xc%63Q{)im!KSB`AYa8}SM#l!Eb$;6z$$_%_6bPzAwhG7CZ?wbuyou{?jz3=C0zyvi+dvz`OEiB{V$^djcSKISOEb?)$PJ=+>I6A;Fo<_1YMvKOWa71*BpfB3xW_GAz@nsDy$eWBvM@jvA2`N=~PuJT*$f7C6wf*SvQZdyd)lsE469ukMMia~0R3K9b%CDG3wv<G;9!_^9S9xC>NDB=wRiP}XCp1*f*)aEmPhBkkGy&*eEL`8%m0te0QnVfu3znI-i(T9t|8kT75at6IG*3c6g6ILEJ#DDNrov^$Wf4S-&;Mu~RQ<#v`S)iluI3Vjx^8;b<Jv>IXWce2fapU(p`$+an05{y@Q+RzFNW%or^T1OZZ&3DnV9tte)*aUVg9>~%kYjCmC!huKfM0<8Ia%k-(~~FS!+c>6p@9qe0SSf_`MvcCR&=CxU$$}iWZE0I*2H_EgH=qWv3?(|8rfb{UAZ_Z1rB;dp%7G;X_%oM2){N(0WDP%2Y|RrW*wIN;XaA8-At%+M&L~jRqH2;7L)@c=hJ{&$+AQ{NXt0i6+%-II7IaXP~Ytc1dw3Tf)2|793qf2l`Y6eO~F=ku6JtaIZFp3!!d^3I!_j5tD-~-+2n}%kx)w4<a`SY{dn14YydN`ZEyvWK?2-VE}<X-e8FvrYAhO&^+k@asX!w_MkmYcOT&zlHDx?TL0ct&7U2Um$v+jw!HoMm<{fdwq<qbb+5*>Mc}H_GT;nKMa5g1u&5CMb3U_7^h#_x2?1W+STW=myzANk%Rk+E<<tAXfeakj3JJo<5$}h3&zL)Z{Z7JR6AVRGkola}8Z=(qTY4TXqGVQ@XMDpTPCdaIBCQ3hi<4+yN`A!^SK63Hro%APEKHpbO6Ari5RP6zJ;y^P6)V|zUnSXzvwvDf3wDWQpHdM5r^o)Au)KGR{fFgw^(jr17a^QFbOp5!@7A7kPEE244_MdsJt-i-OQ1(2(qYC$k>W?g`=fF~X3VI9FE@((@xIa{dc_J_~@DE4pgx?v=BinG>X7?N;2ODGymCTw!16nEv<Tov2l`l1S4P`RgtYjWI-9g_Z->03SGA{gU_vZc517Ho=&Z=RQe-XcFx&?SC?Sq7wqB8uSTg031(C1%I24jc#4jcKbK*%2WmZu+A#TgU8un6{8@>suQjApFB$A8Wky<2caJF!kxGgmYW`9k+%YWGmzq-9esO+?W()!bCakkt3lX{*%MA7%kJf>Jv6Od9hq8?^J2sDP<r+l58xV<bPcmp;5r;^A8UvFfk6@n_Y;0~Q&I+Yce|mwcG|Aw+@+IeZBRvWIa(0^V~Va-_Q3@kEk}%72>UyF2J52mlQS+mRGIa<)eC)gJA#?14ba)-kE;#IuLX{gTt`)EdEE|0&loczU<hE#HvWbAPK5LLTkbxGYHB64~pcz+e8I4<y^^d{%8f+6Mf}Dv#M4jtFZYK<*93>L~&MbR}1=r&`&_z`~c0aH<vQPOm|k|L1FFXmjOptM=H1$|D-s-IbB2nhnVC?8wuicoU{njjaYNKK4ABsqDy<x$CSI+D5UOl?+X`rK6f<;p>g1loqK8#|(|Tf|}_K+xD^0t6@yr3eh4k7Mrq3LBfnrf-u3TA56EIDvE{a#>RIg3s*8j*SJ--=GP_2(M?pxm<{Q4s2T)a2D*!eS8Pnd!5o}7-fgR{=YJzvKay#H3H3ubVpFLRpR>E01*}Gc@cp7RSw9D>v2XnNrO7{q1)i7TuQHMQA)>f^QR!DPM1&Xf>i&{~&tK9#58glcx|PWV@VBW-z87MH_$|9nybZrJ9Q3YY)9FP#ha6jkFY=#aQ@e&kVU0~v$L0<{^CS2i{Q8wCd}A1!)JeaoS!tZ?FI7VAVq!W!zB`tdIED^O8OaXWO-<OGds0pr3`34=;;{zFqP+pzxIw_f?2=0|`>m7IC_{S>)%W%UlYEO5C2&hHH!N*C7!o!`a^$e(b3NUw?!qDKShZ9V|E{x?&|oekfbaO!e*k53=+^z<UO|!nlynK=yHsl*8+Bjh^SZf51!6>h$oayLnQeDod^;!IJ>HJC+EJWPdY=gPH`Ulo)`tPXpI?nCU9fM(xHUz<68FH28$k0`ezJaPm<rOrXmfAyh0D@Xq9#Ub<)j{<V_w8|QAKj@m@k!pq?YX#IE_fbunH2?P(d=b2UxAv=xG>W^qf{A31@!ZHb&U+GDtVZt9SbcBQ9(r(OR{G<hQ6h879>o8u|?j)WOi=;0S~Rxq)NRai|Td{wgrd*<tr7hb+8}4fofNs(<BK1kDuktnrqoSEyz9)llrfCjm_8n!@8u`Kx2bn%FB8LSAhsU;3a0JZaHT4!%feKXpK{kXU2ojmG?ZiF%UY3#I+Z+Z|PhXTfg}VMF7ZB1x_S9$*+Px#*eo8pEa9w+3*kP-!bA_f$&mLD5r3XUX`;E#jkXiH|yz6L6^g+SKX<CM}D+=EC28v!v@9B-=b+kj)pcy;x;f;AAV3^w-a|7}K?a?AF+5MVqz6$;Nfdn>|HW$4gMzS|>9TvpmJgwlCpiTj~I)MZ?L76-c&cR6Ve=V8c{|UOfYqJ+VdaHn`6nX*(Lj#&VpPFeX;oE`ec_ucH$`aE@*FuUFJCWFuP)9J<LDve4BiMcB=UbJ=0;CcdvlTDpl#{KeEYh^1@bU+Nk>vq=4Vk;Zpeq|+FFS)}P57Afh-<7BN^-o3C$**j8K{rU>U*WGdra(NnV8`)eE|GXDnfa+T<rN6@y>Z`z*+D)r<Q4OOw2SVD~_=NaSlD~P%C#3NCj8cdrs$1s^a|*0#5?_Up3_14^+Y0}Dj_&H8RA~UKVSf4zf1*`dBlt#V0gAj;{|PeB{B$CzdcvoUEt!fm@cBKQD?-FC@K{a^>EMBe1BPqN_h1_evnnAhXg%i)T*Xm`AzLOYa*kNM5oHuh{k>k7VRhm(K}gvLk_krQ+$3I%gUHro4}_IXMYB{<4uhCI@@NHj(qZwxxA}iZ>Y|dTR9M{oC<S*U-Cz#Z;0#iH|051W*0*GVVLeKth0sB!uS6%7sOz{v>`i{qfHOw*fQg(~P!X<|>BJ!7SKgmL{n~QY1Cj*B>nvx12R>g(MeSJMPUR^~zc3hKm8m81qkMAy-@a($CJ|sCa}>;O#fTaMt^;~&`6B|{p_b)sAP3j*v%Em>)s<kSYma^VmBH~s5>+DW%_?mpw)_+~>AP%*7;)J>U(r|WD(-eL=98Jxr=P#-ejFe~Bol#j<%n^l#>?<h>o$j$b;xTDENJ<Z2DTJ6J}!`cj>AGY*3@!An2Jm3>^+#|Y}t~4##FM;B0WHH3B#NT(+z5m=c9!tglvJwa<m%p9Fb6%jX>+GR@ldBfChmtsQ_?dD4Xwtj)}_~NlBf^Jv<(y;m*?_`h>i0zG?mRp6qezsIU^3k9QJ9k*#HH@djQ3zOK=kAc?Oi-5!Sgr=PzrcwU!XE(Om9@9L2@HZ%VnOo~x_PJWDlsAbHYcSb@gLySr=X}_sh=oiI8App{z`3Z->)NHZWr7Gu9ESQzYnnJ^vjIrEL14JW>9gQ_fPV7QU`bCo%wJH%_?iBkqXP{$}qeAh#zROWDM9HOrl?cVj1_y`Y)Iv+Gc1OYne8*oh_4pGEa5fK{2M+VMr3jmE`2o|zb^hNSy^E(Mz9kSmU&Aga2_Rl8#6kq@$z33NW;4TNG6nDk7+cQydlQyM41Dr7r{!Ex7_Qu24YtTI1*YJR>Obk=<3ch1bMQo}>Ri!`5lt-x&@yf4MUx81i0HB-p}_oX%Z4Z;CrSu_M;8?!qV{W^#^<ae5KCRf!M1DMu*;RiSUIWkuorbI;`8|pN1HTRC<lbRz>VWNzyCjf^~}Y~N#hJ_Y^a+ulZUt=iSG^wkZ>kDEI2Kdl?+ZRbu`><j*$5$K-!l1*qPR1B%fJV;xyhcUucM$8p8#R$Pt~K^a4wZwz|P)8AMrZMhrKJgCdDrq80yA5xYPqktp_)s(p>4&*Z#|SRH%`y;#eHuT7`~NCdJ`B-SJB0JrIRx?r%`+XZY3B8{;m3TtWC_;D+If8&EDw96$Xu&v`lBkaMTMl64+_;Q}v7Ub+o<@))wR$80OHHZo|=zGqShS#LE*@-nTBn=zj#Y)n^%yyA9px%UW^fK1|d`^4IZ_J*hrt;C0)}~jawL-0}as_6#%0)=sQ_@;nV!|0->RPWCY+8x#`JqD~(-~hOuFn0=yP2o@hW_rv*qq}mX^Tc09ypUs4r{qVX%i%6Y!u2c#8K8Vs08IHW(c<61}r)?NWqy~`a(fMkZH~D(uxyMq85ar!mJEJVa?m<;DJ0m(q5qV;Yv63m4r1S-FQt|ni`p{Fk~8kfs)F=6V`N|cnPF5l1LZeP$*Wi8cI~0O&&_>c|F%+3CV`0H3hp}&^U-fd%>WwLK_mjbDEI#qR{{r*b^InQ)Bm##?*gi+NA;CxKoHhK++$4{8|^qm7nMFd(UNr^O^8>DkCh+0kI$HYt_0!+oMI_t58tvf}6@+MMO#Aj?i*X3<OL=oJ<3XocYY>ZdDT&8s#z&SG!dUjq;DJJl+2NuT4ik$*YnWZ%kfQ?a7U3&V}*T`hD!qpjZWU&kdr+E#Hvx#U22F+beYAFrzZee7O&VI{?;(JkyQJGdJ1q;IBv{Z~5q)vRObPP%FIW?5X_WiGL+p!g$ed@!6awC&1l8ej*|lLpA-s_&Almx`^o3L2^SEo6c$Jw7bRFt?f^4PBwAULKy6V$IeTqHB4K-+@IshUAHgpOzJeRHfOUaK~t-s=W1@%(&cU+xIev|_O;FF#RazBpFtc9xU16^?cTISJwUAU7R}av(NHFppzYGrGvh9l%#9|QYh}A;?Zf+CbB%#BA};>7uO3HvMSk%D!MsswKUE1w31Yc?X7kQyZ)<=B>roY}o=Ow~$_%Ina&9k(gT=QSOVKr{&Gll7g+&P@-b+g!7Ffr~R2&GB3$b01C^UvK55X{Uz%PeM5`~_M=?=>QC~qrnH8)b%h)e`e^)~H=$7mSB#x)$Ix?K!F)q_-|)Qw)xjVw`!K_t3B9x9$o@<F3M{s9w^e^Ooh;a6ssvzGn(qb&A@hAF?|Y4rAN^^1_PiVxs!583Q?tO&4(kvFOv_qfOGW1=V;_x=m9E)r9H-1}{ql*$ZlZTw@5tG?j$bY4^=hdlSeCaR<dm-B)nwPZhqEs#nEZta!;6c~%qZz*4#7ur`Rmfl$=h@1u(N!{4WWhl2tRm^cJB8NPz*5@Pd5Rmr~g~iBsMh%mA9&HyG(U33Q@%is777)w=s<RdUR`ntt+MDEAUO~@S$O0)3LsMM-C27em7j&vG6$_r~M08GfT`)UMY^&S67`!FGK?)IG#-G(5jYRq-A?a-Sv6<r%Zp4JY>|`mpY7Qh!R6Q)4Ye0=P3X|^v_?N0swO6`<cvMov+#ZbC5|&%A@kx<D;fVz(s59#JhF3PpWD46D5hxvp=GU2YV)h|vT-Q{846t-+OjH0fnWS{%G_iE&$=t)TQoaM9U6W78D8CH?wsZ<}k1|4Yx~0GSK%4)E-yY@#QSzr}Dfyf0l>8-gc?&B)_*Sp7@~3xV<&Sh0ZcW7CzByL@GZu#SIxD|e7*4feVnwu@KlJ6Ag+Yj5EIlW1h)*vOF^nW)=+;CGhy%VJD}PTqqF3=R_*XG6ocLKyv|Qp}5Qg=`QZW3v)j(!_X)H@KS!E`3ypIpH(D+Oiw^o10Fw^IlrBW?^&zZ@zLl%R4U}F%qC}Nm^YB=Pd4`c-itjHGCX9Blig|`BQwBG7_!DOVtQz*}i4-)j-R*N|-27tk)al-@N3B>OyL^ty(BZfY(<iJ3zJpj3f9Y6(ZZ?%*V4?axeU6Ez!!Dce>lnx=x#CvWcD}?p>_3AH#7DG?Lf8wNt?C(N+V4UKSw4wfgAAg{MhKF#vWw7WuQg9DD5Aieh7AembjyEQFCpGH4J|1q3-imnsu)pJ&3YQv~mGVdKOy1^b13y+4-QSYQneBr;t<3HuYGpDxC`94`y=9g->_f>i_xIvb4yR9$+V&K&5F*zkR=kC<dp0uiorMP9iK;C5#ghoN@EB|G8xnrVKW#B{C44We8@9?{c>5Fzoo#+0-ztru+~5+AH-R=SYz{;SVq{0~YJ6>e>Ki?341Q?lM8t_2M5vBpU)=jolZ~v52PEMNJ%gtn^ua$Q^OpD`=eoT=GR&^$*_8>?$wu+P{~8gN2Yjh2x$1rkNgbMl|2&^9yUM3q3Eu*`s2r-z$=rY!zsp&u{K5LfkVk5p-hXLO_|P1^_510zR(9Y&c$ca{16ilJYLJ82!@6W}0tG>SJ?E&kpg=8gK=p!ney$5J7WD4Z!hyjJh_&90qHq-Q5d2;cjISl=4f3^Y!VfuOPfwEnxX$?-#O?W)&1U8S7@ga|0HS}|y9IIw<2=5rX^8_1@7t27kxgcgwll2Fkc`m|-_XFZ;Q4g^7O5CQ*qXS>W@nsO?J5uBFr>I;qd!;@hTC|la;7;sxrL=g|K_mWfAn5yCtg%a+`fZSqOeZYxzbz=?~iuEKAW27BokvLa{0@&6Wh1aPJn6K-^I(c6Ybk+C+aiWiD=<h7rp`7iGyFl9Y0R-7hn3ne?;6Pa$gT%8QBKPie^do%?*oE6TRB7NUrwRcx=T$`1Np)Ru(mK&~*#*of;PHWK3s#u3KUtqgQ(hnMmS7zJ}H9XXs;{axBdxxVM5R7#CR(JwC%-+x-9Rz00p{TY4WfUUSSj*P83G*IIj@eeXSWt6VNu$~JaHg-A3`n+Bpq3xsHagozX*L~H~JaR8%4f(Qi{77+v_Bti!y0yJn436v;8{09jJ8|PumB7%qpUB>VC`^J2%$KLy#d(J(#>~pp2)ZXhc*IaXs@r`eM-|qpq)=Vnl8$h!86&tzb8vg88V?B=5)(iaqD$5L$WH%ACtTZDm(=4j)C2BS&KGIxI5}4S{7<@zBv!<PKAJYuJ!D8BI4kKe(fHtQBs;3noYC6V!%r<a%vZOzPo@d+-t%hs0q08%;;+65z4$?0ZRD_CVs)MFE1ClpZ`(54Ydq;b!=->YG!$`p{zc~ghFMlGA40Q3c%TL=-Kck+KS2o=N0m^c{1D<!FG5Q5F#g4SQ`5hQs6R+QaENI=6cOYEcfmm7h6#8`FMFGlm^YX`w%kQ}&&hG%6=C9v@=zr^d7Aa{-A6K&?rTPoY3Z-JmTNf#f-TVRTlzCRCj5q3(;Z~h;6v_F3rOH6y;2*G3<^S~J%z|kJ=lKiMihPEH*aE0yL<$1jCL)FHq2QpEdu6w{2~8KWaid}qSuSwWj@u}zTwxo<MY2oi8ek>QuDP;}y45`uDwW&f)({O$bCI*k2IAJPij@vz5C&@6BB?>`P}{2@t`3Vix%Ncqw^|N!ug;jOfCZ35t6u%lG|I2+un=f4H*;E2aoA7&2rK-5P)1O*^ZDD1M;+yhI%)+a8$Ji04(0o=DNEg_EF>i*j&Lh`-}PeA#c-%K1wD13HL^n=ELMpNTEHMR=bqcp!FcZ)YsWye?@3J4Y)Kv>!Wz+pdJi}Pn$%G`1+?hlabBwi#kmd*7rjjWGakSv(Z;_w9%1&QBRr}+HHw_;r>Rtls-XV!wW&G#!Q)@Bp_l3Bq@V{3#mNnfZ-{<-;7Su#H2hhfT2a(m3~@ZtQiI4&fILWciW?$L6IUqIbIX_d6YdvEW{w|JE?=>>N0u-C{fztn6O}C;1qrAFd{A5{6Z}=|Ue$gy1d}i`2WM#SAUbidq8)D9NtL3iLgwV_9QTJw9y5@gfyr}^Dw<lo4=P?gXlrO1J3ZkhGHQyf{Gp2V!1|&~U&6)*i~Z^z%UMZW2EEvsf(Z(wC((aUdFdWZE_pceB%_l!7vb;tYMD*&TshLAn)!rR=6^n%+=y!qeDCV7ybDtBGz+IM6a^kNKgJTn*@kSs;2*4xK-f3Ktd}D<)8Jt$AD9sEK!Zf?emcYRV_`oFo^6;(0B<Hrnbim);_WE$o)-#pEEDdTimMPnScwq+)6U=Y-2*>}DJhqUmP>BeTaUQBWqY~mo<lu9>VD`?l|eBipML<-5WD^5+f##HWc@^Q!2nWz8Kh8Fbm`TJSsj(l*Cz^{1m8cnJAt+!(PO&!yDs#JKqY!K9N5Sz_vokS^cOfCVO-dedEQWM%uB^Se8GR?j_?a^Tpt-j&_>!~Oo`6$eRdDbRe@^GuggsCP-61EDOZ%2eMc|YT3(IzJ|8b%>yhCRTK_x8jEc`n`hO2OCF_f@B?4GMi@;RUgzc-kqxNiW9WeBJUWAqfg_SJd_qIVGrI0|gn^toy`&mr0{Sa2CrO#Yhb*U$v<TLlm<uLP^+Y;WRS~pb&0H^F#;)nt9hb#bzTYK|w1M%CT0fQa?0Nl=@VRe-pjsv;%*n_PpwhcT?StBtP8gr^+sZ3P`5_nd$rYqMY_QLaqq4i1h8PMuNOSR7uRNIEV1A5v8_ESZHG?_9s850*lIns+;V;TTnGT!F#l^S0iShP*F*YL%ztwo;6z77ItAY_3A@12=hfV?O(EGx1~K&(ME9EB-W+nHH1nZgFpSfAl<x~tYW<vZP-Tg_nsyo<Xe$(`6fLiA>ZrOdWp4PlPFc%bc3x)cfCXvw(B80Fan@Vu1gwyhR#NO+m+V~NnwACg~<<|WCz*gY*h*^@>xTT(=camx5YiZjR$IujgTLl72AoWR#QTAxe?yBvWQs`MeN_MUPXr3sm4{Ak%?rY)nnT9%EZk`E^boVkS?S25bvNbZgeb48HJ95SYJr<Rzc1S(POz%eIpHaW6f7|hf&EC+9@cN*5@cJ#@dduAF(OqkMgN)q#<g7Wz*^-WpGvyW)16P`7v+_~eWv>&?YtMT6a-_bp&44>I`>wu~F*|L!R%P(|3wvE(GD5=fYghb?me2+E}HcUO+O{0N!015<KrM`0Y%Fia&7m)K+owQL{%%hXGwnx^8=Dr=9uuOR>QuL^4$39Z6mV&Rif-DJTu|z#u+m2`0`LeuAz8V?k$?(=CtfEG+Mxe^{1A>OjFe!>e#%KL5teFAz=bqdD_6NAA?B~qknlHS-GNj&EkNnDI?!;CgIl?ZsfmLw5S)`bkN?1C$yztn^+O<#BZyLrnlJi~Ogq7R-*?nlD-~uXTWBoij&LiHFd-g-tqsI_$3!Q)-P*y@Rbb`zSg$2j^03T}JieGxqx1tK=ysj5Mj~BjNh7Q~6Q7DJKG2*JNfv~vnV2{-CT`muR4bzq8BMx@+apvZ&PV!6~2QOR8+Pt;SGQ#YNx=msdt@&WI;hyUShEZsQ?9S>`FR-LtTj9cSt`9IQLfpm$)_3Rn+Ro*2{^<`DKyWWjjYfv@>97nMX}qG=lpdYY7l9%#2P<PeswNv=LgbSOGmk8j#A+*F)=~tA1~pamkfnnAinxg5I0Qpnhr3mIBU!m!?EcILocL=DyXfmx8K-=vtoM09eP*)9*<?>|KiRt*lRaOX?8EKJ9yk`WpQ7)4vWGg^1?<{-bP+J$)Ajj|#ru2i&n^lC0JpG4@I@@CFfQe1-29^okiHi{<3&a4-bp_J*XI?T;!PWw6j|A_6Y2ZN>$p1cI}kmg3PMLcggmmLso^Z%=|NDUdyKcL8y#1IgGAe$XDWgs|3BhoD^Ed3UdL>}p>mQ2?0ICG-kn%tA`d1=`!J$lk*l`I2s#?Sh}|j<=1zO%<5aooRRnQKda?0nB7SlxL3T5ix#FaYX5#4p0P!Q**xXk*otdGsc=2bzQ~yWY7P<t0V3bQ<wrTm`g;y+BVm-<ZkH1(U3XJx0QR6)a1KU0sZuN4H6+8+hD0oOJX=j~2vJl^8nYTsmR)eIfQZVPv{hkSDRJSLwRG!d6(d3Gz!(1}dHRZ7}rsQLwOBKSG`<V-(%D&QSj$u2X*w9H^BtT5lKcavWPwt-EP)tJrXQ`jSGX77MQ(t3KRL0jMvF4f8fh=?6J5Tsa83Nqvu#mRVms`oK-LM8h5+PDZQBPzwS#p-m<7Y2&xgMZPSN>OBu5pJ^d(5BV%9G+~{Wf-W2w&Sm&pii8a96KoX6hp{m#UErc<g(0TxGN!;D&>JHF5zm3sZp-V_BQLF~iq_$egU~I3;<Co*d2IB?!Zh<F1fMI<s{gO{Pb~PVFp05SPW*lQi+4>hY`=8aFT15t)y4Tnrj%^d*7m*!E}GK#?zu9-K=X%QW|o3=4ndT6OhuEv5fJ5I}iuv<YOWHD`mmv?fVT)l6-O2z=IlH;hJ@{Kc-h6Bf|AjM?m^{V4io5M?ueH;L}iS3#{UZ{no%4IN9#-b##O$<(dfsJ0O7{<_gQbu^_O|Euq!mQoh4&vrd}Lw!9z<<6tL64e&1Cfq%HjO_dQ>YXXw92=iyEA$gTDvNioO?jDPpK)fKSmWYFJ_Ib}Wyw3xqgHB^v^&tE?gg?!JUl?$u2~z@BN7;dPA>aSS>tqT3JyTLHY_VpJDNu7Vcl>fwvyBgX@_EG<80E<qQNwc*n`r*$K{uBG-66i4L@S21{PC0k*Vm8IT*|l@t_>JH_230>9MGzO~f(>AcS(34`EHY2Rc#Nd73e<Y^@VS+f)x=nN5{Yk4`!ve&|7|X_<IpR*fRSzdQ`MHcPzO<c-o;u?miUpR!r^Dg(EX(Yk!rx44!5V-uG8X9<N|Q@8R2X@ObWn$fL|?GZK0LH^@+5*(kf)Tm-UI+zRYZ9PW|g1rFLf;%^K#$1vXk)DMHdiiBz`+Sw!dWLZ{=hjG0w=4j3)gPK>IJ|*G;2e^fMyF)x>TL?`Uhp(WWhm<E;p5QG{tP@TR`7TNL&q*t%VsC1B5JW51*u1#f}P-AmJZHp#}(1&tFz6X0qTplluquT1D5lxE<n{l827KOsU)u@WOB(+3O5{LDI=Pn5J&Eo_BAgNM-~9YtN-uSrV<Jm(!mYV-eznT^c*Ve|5pfrW3vnkvY;A?EyBiE+czl-Bzsp`ZFLS=8?zc>Tc*rhK6Ll0{Td^^$!z+`oGlqj%hm|K(yQG-(Pk($#HG<yu%@j9X6a@U!!BEnUuIz2S{1Hbs13wvr>;brcO_D|>kYB>aph9{|GSW<e_vyEFicy%F>EWV?#$Tu=9umJD+AUR%vepgqkNntVuu)hIe2{?yrf?^KmJ}V4#W$fk2%_0t)(Z`iYb_-OEVMtP8YJD?5@OIt;UVrT78(jo5a04|Ev`gSyGYg&t#H_7?0K2T7~#%HC7uni5EgEw67o0G6{|ZP*&e2+9)d7^=ghgW%IIe+K=pPUMq%{GXVJ2Zkq`x>_6(zj>}%`%ZK)B_!i@5Ikd~g+aAooIxl(OfPQzbZ3x+CNdYZb>i1{to+ls+P!H;<n|&A^>1oT<yK04*s&tz5211vnn45(w*C5R!+RCp9d<ABOQl%&z2+pEdZ%%<TU$8YYmo_1JX}Hb7a2S|jQ7;8ucowkMncDCTCdwK#G>Ge+5<%jPwzJ09rtlr_EF<8Xk{p4NYzVt!`Uaq?|G&3p2+ZjL&H0G90;3k5qQ6jok@nc+N?F(I8A%}dWfMR8+~S50g#OPN0{M&~;H|B{WC&C!pBMt{uv31hT6~NOQ6ou!s5i;Mb<qwYSl_by@8e8(VlYEIHmh%&RQAuY1qRl}dcib9HK~*>?Tj$6H=oK{&V3nYpszAhbF0dhVVA=4Ga;!Jhi6sZK0_BY^LSTj1LZ5+u^5$_X^cw{u*|c;f9=EkzjD7e^+@9@DA}n{;qS1<u&i5)s%74`F@MXeij`Ra#Sk8BJFQg)^~{yl8wcm2HSirfE?AKUaVc3L(kFFI)b(~0n<v7G``4xo$LJo*FI_0fG!3M%&gvJa6p)Y{>@D)L!>1hfC{C=_M!s#ViXb;ZYy&6>629oLE<-c4wGDk|o`u~0VEIm@?3NuUs(PrD4360)RyshXxGRc*5mrixoLHPjepuIHOi5`eF-$p3?n%TSP;tRYp(N2^$?cPsL1LA_3KdtT0tu5@uM{-ZUB0$#l_ROm99r;6unupRdfjPHr(zO{6OF_#|NC2`AbmcoRh7`Tj~?Y?mO@bNiDaQuD6^5ZS|W%QyJF60&M{mh6o<+Yb|ALHHK&Y=ZHEdR#>Gzc%W-Hh6N%2I0Wl1Uo1&HnXI>7}i43m^jleLWB~D^Zq!p#aI3P6#B1WK#t}!eY$BU^0Gq345cH~6^G`C_9+A#yve-O*O-eN6Yd4Naa1pVEPZ;aS5+|k&a_=@ReUil|Wet?n!tPmxY!yEvoG_XNlQqiW&zcvycNd9e!rw!fHm<Su!yWw8MTo-B$i2D8_st0{F$K$Y%Ae$Zf&am3uqu_OlqN1ktKmrQSO46v^-+9OU=-Jf2xw&0^pLxGky=ulEYr5Y+k+;GsMEddFl<qIQe3;@}e&5dW`_ah9n~ON{GR<h@!_u>#jKuwzSecQJ8HvZY%k>Et3NVu@`9rc`tBNZ=Ll!=AHLNbI!pIRO6rk2g#7WKU^&_}NmM`lhx5NrPs`5V;*?js}78b0V^7G>Q6ai+}>r=EXR*5RAL`AwstpAR;@k^Dc$Qh(FF6z^qYvFS~^||PxQML`7U@_2<hVbBJWvc5C4xmjq)NH7w_vrY_j*q9RXGvPW3J=g<PH5%^2wPBN;6&k!#P<$ffGrwSnbKE!V6#P47RK3huy}#x?>9e4Ab4rr>SeK@0XXbR-D)#4^}15GGG@=BbQMkWXbJ=rOKiD0ZnfQS&K$jb6bpW`UDo0i2rJS#M8$$ulvZxOwQ#mKoR`nMyv9nFnJ?#R;l=Bz3ASPrAu{ji;+5Szpf{5Xvso~=gwGuli}+5}sHFw-lm5%`<N7cEsh27!+#`8uDVESh^YLsS>F*+6I_o#b;eeHtdk58+<8YL)g_D+C$=%j+@N8%&#J1hqY&yphk|`pfZ+{m~fzpWl(9Iq6xB{XpT8qObJS6hU_~Jd#X5okn$!$@Ht4;XBYXpC2JOsUq)`1&%T1ii+ynA~;emedHYNvrHxsu>VZhCY|&<C&ePf1Zk1KnEpdds?Xyo&^5W4y$(tN!Po3ksu8)^h|l4WK=Xf!$J)JC1sJ@ls+7!dz?iVgjM!z4#++Emyi)qM%~1a*3HZF?2_6or7BWim~20c!WlE)ZivEXpk~}?VYm@&G|f%3Tf-qR(CR++f0trYSOB2Ja>eN0^FVLQ=?EC<-wi&&B{$<bMY=5gF#9qv>i6qkkS=fd3d8PEO=6dYg7lPGL+IsOyj=pmP5mq!&wfO=*O6DhHgs}+ocm@V@`~|X738!mu8Hn`@^D!;bO-C-d+#j7iNr6;07jh(PC!cbyF&?>g=FM4zkBAhm!|mq=!hdy}&$;TgNN%><i-IW>U)ZA3Kfnzc|{nBDdecaS>nRp6$LMdsYgkKw}~SD@KrLOLEWSD~YJVYc=h{s*|fZaV2F?@6;O>uh(n}%PV1;(%4}UC+`_xg9@(r_b1Aq2PqR7EeTqP4`!KOK5-{%*@lkx6~2Q<?rqiR38?4=geb3B3jtcPJ2>^ADEENlY(<u2NzKchnI5mP%6#bARc3;VT{WfP)z9LxosG##D%Foe-bM++E0dr6x~`V*7Bin(+I8~Fdsvc?i;OL$8`GZC*tp@X^@bX=yyBErM6e!BrEqW{)Ql~RQd{FxZ?0|El&F=<(l!DQdDUt>!%6vQ_-CilXq5*XbG2?cx7{pb>o`}Lv4tPUj7?7S|J%C{Pe3|fJUj&el)*>C;aTQ+W6-&CI()}o%-n9Fhh&2U64NZR@Mf-nv9?&A=tE8$qiKZ3N;8&MR`69gp9rJYhN>X}F;vrXoU&uAZe%kP<DHGu3RIB5$Xkq4ey{4g%@Qk05tPhDi@Md7Wcdk{f5E)0h(KgwIq&sYKB#`&sM(JiUsskMfsp2_PxDPEBK#*dB!AuwC(n8KR8kuhC`+i_T<QD3>($FzwB)JFKsoa#MK$&^QA)Add!s5>jSPUS1{6y3T3*eTA9<@L7@n>3zLI)s#H9Eb^Ie%z*Zzf{Ma-s*EY!a{c;3scgSsN-RE=yUrbWJMFnh+$M!j=7nWmMbYbxD(#gW3(>$-`pXM*5U`<Yey9b#Xjyk;=dkh|7(s{U>OOOh(qx(TODa4>T=RJu87@-hR4WWwM6AnPDv&4;gF^b^PHB_#}E6<k`BF#IIU;Z()Af>;=1O>E6x-q$rzjIK0`HQ7yl;?|9^=D89^yjj0!tM_bDnhW;BVr5L1RgAMWF}p7O_^*k7>-T5M)^Pc1XDJ&O#G0~IFnf11WsBodNE#%HT8-7&Vy&~;u#M(Kou)xbxrld2+)($k-qY4Xt<SUCTDY38sZLOfY{#0it;^VKZO<5%19PTSA5JzfZB(`&cU1oN2Z4X>jSQ9F7iw|El<-RZfI&08uzrBSC_&|ES>%wU7X4hc$VO!vO9=8+Se6i^5F}`yMrB+=zNYTawSn1R1$!mXvDS_F3LG_7A+V~1HbSP8AZ5LTJdR7bnu1mHb-<aIJ9ocCarG705MGwJb>D=<?N3h<3a=mn)$Qnl&US}sJePmVX}nJNk3f_T2cl5|w`50due1B<0j=MYkLy?N^F}MLNYddo#OJ~RrM5U6cwL*g;<evn2kJsqkGXFm8`9_;A_!yvA->(o>=BNx<<lv{9ancw^%`YQM}4APx5!1ShFNN9$Gs$FIsqFHsm)O_)>fW=g4@-nM1a~`(>i3Mj7uiKTBAtf^wC44?`||X4SlY<M4dIW^${8=USz<3()|VBoc!*OVA}6N=dIT}Rz}{>`$6hhkK}bdy8f=@&?t!POPcrS4&|W4TED)>E5#DQQ}=F70#^Bk--RR!ejbTT8T2o9Z4zqWt#GuOjS^sz-ZOA29SS`u6GM)I&I1nnz}`?I0qwyXq-}qX3DEE)%c*|nK*dYAoS-08LKTwrg9Cl-PZ|-fkLlZh3Jv16C4swOazwZk=h}CTV+I`>w%rkWq?8lUYaB?BNr#dBWfIu7DLk+|72Um&+|yu^`Cv;X<E`jA5kqxv+%OrQ4V9>dDSi?+1j52uu(1c|qL#ycN9s5yQ)L+VDXAI*6WJNly;n`-k)QZbPT*c;SIXP4&Mk?*Kqh{s5=S}UcTd(&>4cy?mUJELF8HoOC5TBXET4Q&PS5JZ-DZT@uFTbO_5SvU0@1(Ma`shJ!qkSmgd|+6WlP}s0*vrf6+4kXGGBtCRk2OIyfz@8sbaqrbv!R&`<l$lVYGq~=vAO9wm&aqBZr#p_GXnX0?{O~XjSZiR=p}@?_N;I{`exNfAw9Io({kjUm2cTFOFG%)rE#Nnr))aDF;#SZmT=qN!M|*k(!y0fd?(IC&0%>y{8o+$I<e3s7J%18pkwnOnF(tGT6oo$tQY00_aJ<`L10`J_&3Z44a>**|(5?4&o*+g`ei|%_x6Mye#z<xY^@vIEO7eAf#<+?8LLNqnQ{1OCzof{!rb=9XP*qWm)+GaILzg@La%k)o9XE64O40#uk*o-h^tFSSGO0AmAUI5njouHj1q+CAx$U?0RTlt($++0%)1)YpxO9y~Hn(&6tSMD;)6P)Pqp_qih;td<fN;fn6ANpC2%49%U_YR3dE}X~2gbG%y2KDA2q^H5R}?zo(&D#qkLfMb$ELb{@*>Yi*TphwwnTjeFK9$<Xe8^}T5ii-=ByV!m*C!$KpQH=>W@lk&rPAwOLGNjtGioD#u6{@_Zh@s5i{RbNUC1u2Ea9wtGH!5L~d_U8)3JL%sN^8v_9Z|c>zM2Pp~tr~Tl!vWpr9*fI*RZ_>%YnNgUV~>m7>UEiE`$-EI$cUpm(w8dz^>>Mr&x%1`jgz=Iqx3!^)l(|CJI2X)BTjZTPNrF$r0{S#vWS}&Cll4WMsPe}@iRy7d7Okwy#Vpm<2y<V7t5?9gvDxW;>_23P{1^IR7xN5jztTYehQdWEFK~6>=VGhJ(G;3gM%jrU%7W{AAj_Hp#NXL*3ndM1^6*<GoS*Qx|L(TLJH(|=VMCp29Al>G_0~W7sn9iBg<^55NG|Fh2vsy1zI)ci}57^dt&Q7YsWUe5~IK>Sc7O~a*GJIEr(dJAvTS#ZX93SllUMew^e&Udv0gdh7!waslhKx4c%>&=||4$eq|xm*p;yZf`kF(rPjD9Po-CnY5m|=bXml;y2q~T=RU)v-F0D8cJ=F+TK6q_?R`I(mv>prhbEK&ULxbb75n=w<L%B+z1VsmjNhN2e~2j!bF!ltu|TmN%H=u;Vv17Jcgh<d<mK+yY_bTLPJ1@=Z3ZE~CIPOh#2{^n@<dB+tK{FD|56D1t=4T-FzA#aLG4k<4bsJC-VWUx($N#CGo6>bj+110s+$*N9Dv5Fn`ANszN&{~JpS>8{?EIC&bU3H_|LL4*VkDsK#r?qJt6!Klin9*^3(_(<<Ns%p1M?p(05kr&N@`6QZ8Dbf&IrF-jFB-dy5r~);ojZsh^uo<Ohbgy?m=)p;`j;oAjfJ?Je&--qSz^KKFB&7;jO}d9ngPtW2kJQx3oK))%tnmAktZC)Jm{yp~)a-sN(xsh?z*Gvq2+v}mVub1S3rWG|Q`sNxs^J7MDqxeriLN``d|#x)~LhZmSvx5N1ySc@nD7D+X>UX~T7+m|^=%en5QYmL7u*(L0{?_$0DKjHq5uVmeF#y`F8L}Xmlc)>-r@_HbbQ|gDY=BF7+S;JDzV)gQso!UgJNt7Gb)F#VdjEmMSOYK_8*n5QhMih<Eg^Bq<0-+TaqbzKN-08xMcaf~lK{g{=GbS8L8ev1p6iTtXS|MeTJ=agEQWCdn>%mYEG2a=vwE?-+Nxu-wu<B}L^^@xw)~w5t)(Woctbk!qEy{2)gU&J<Vi$>aR;0el2iJ)um{(S~KYkND<$wFD*$RDiV9v4+`Ep=RjB8)9IVH%nD#|a1Bz-cyLGod#K1LM@s47hs;r}oL1Pfv<`FKO?j7{{kY*DhP$9Db|+J83=(uo0JM5N31d9wtNO1((=*hBf0LoK>hJIIwc+-Pi+p<%$TtVKx!^&L7KM}iV(P#qIBYcD%K8l)qeb#;l>`FP{>Uv>WxsLzcAg}z|@v;1r?%(RcNorB{5Hrhh*`)L1qRpp1rxK6O43CYCYSW_*(P)Rw|fA`@OnafDCj!cd!C<QQQXH7XM`jr>`M4~^|F??rv^M^XDBu0VgF&KVli=e;+3HrgX#fGm55BNFu2i7~M%_^)gPNbKDyz?qbI*`>AXjbNqlvODD8QVA?<7mf{_)RmtwdFWk2FcLHZf#qB<&fe3{vhF?ht6iyhI(9~xTG(_L9VgD3OciJkfYKn`6Gv}ViKr8Ifa9!vH{0fphMMgAm$!Wxz2Rtv?k_j5n(L}5Q?S?O*5`jEc93`7#(c_1vAQ*$y9<?VLp*sKX!#XLuCa^vROk<{<)x_=(!{ZCiR9}iSSL)!OLV#0EXxmfYVH?aIQz?YWpgzG_Gh~KpR0TvSNpCS#DalCXRJq-N*7JOAzhQaSQj6_iujkfc)UA+qL0rN@On^(XdOo7}1-zAJGv6d+RaBID+m>nkgX18Fg*gxvN9Fxi+-(2o$SByBT?}9M|)eF3y*^;F|^JVKJ!Fm6fhCUdKVb9MRN<#tWO-h-S@~G&md4?7;d9EOj65REX%Ty%bu*JRIv-?w%aWVoQAd;r!1p7QsiZfMvDcTr7g8lGdlk<Crmd@DIwkKGEX$&hB$M2`7MG%GdsuIrUO-jU)^dH+Np^otRKoxsPbxd?~Ftc=UwEWD!}*4@8wlEN7YOcKM#@XI7Y3^m_Bew#a#_;R1)!0cvd6)8!K1Us+GP44%w&xs@Kmk#Q%94-*3{BuJ-EtT1mwYN+B|Hq5nwjP~M_^WS8IFG4`Z{J*~WGFWK&{JO4n(Y)B0=I*^vztnc|B&*%ZbkT`pAn@jH)uYh91UYH9+|lyRor9eAhC+`)#?xLoE@oX*w_Pjf(u~X5a?j=BcDC(m3A*df(ph@xB|o3xXQ-yzd#(^yb%rC6-E#2y2@uL6jdVdEh=hvbxc}1J&Z;Oe_6hart5j7a99^PAJ3xm=m)G!wOXjT3_>Gv@U-%zM%!yq5=+{0DDGUwu@uP@Nenl|B&|$$kh4e?eI7HHULmFr(wq__T8Qr?YbS&HVGIll*2=k#y1M9ge_>>v&Q)A_atCfo6(EMm!+9SP!EHL#X&4sVQ+Mycq8`{Qb98$?VyulK}jv#>mtUN<BWxzB+E#(cEx%eV2^XWHOOW;@xU>2YOq0ublSjdKWNjy}vqmiAuYRiflr9+zu)f<AWOAs|y0rTb!`x~NGG4;m;!YnLbp+($LeiR|E<xi3QlfY^f<TEgPw%EQ4mXk=-grJPnI5IVhzMHIS39l--)UqHiiG>|hSMbYgDr`#DNv!)foC%paO90m=0CGCA2Y#NYs~kxyB^_W59Gd_Z>CGxYq(JrgNOo9)Li7)#;TTOU#JfMl%DiX%zzH|$hxkbM1@|G5Eyku=T9C7bPb%mCgWxu(NnqaSE@<I9Qs8Ef7COV4cS3kkW)!P)*+Q1h<D2MIXDh4G8`Hlk+fBoB1dMvK0_vtI72luh_wvtwV9|d|Cz-c(0ME?+-qHa)E*-!#C1>Bx0esd$iY7Y$l<_y@kRi@ZG280gm8<c0ylwm~%j_ZI1y}u&54F6Jsx;Y!l$Y&ru{n*lHspBI`#X%@-)kfZ16fA5?7xHTzhf2Ytox;>eZaHcIBI&8OdwSUaEH9|eVKr#k7cF&_kVn=b;*A<CLQr*XJoo`My3;Dn_HLlh?Ps{SnW`Oa#HH(*u1zv$=#&6oaHv{Euwd*`+wt|_)#zWjO!hwHml-Y;=pIS&uk;8LLqhXK$WsI>#DZVJi+gu$aZ>)!F+QXtK~!geK>}0ef|!$?qPaZ1=9EU-W+l4v--NRSrd}lMwa}lKnI=3=pW|dj=KfY!NSqpef7I3U1VhI!d9r^7IwT>fIDLg0d{rvB^H;Yh2c`DYlG&Zthy%bMoLhmyrqYdiCHE99y%?HC_(5=vWZyga;%0O60+4WZ-mL-xbT@AXJF+4;r+yuSy2y&QV~FCrbcQZkaaSVh`qN-A$c=92b|BkB66{+Ct4Xuw!h)lxV#c=DMWAqtI(A`+7^4A9NiL7cJeD9s<LAH@3>#{Je7r_d&FQg@b@94lQ%EDZMkn5*8=7SL`D(RY&=0^mXE9!JhCBFj(Jjh+8>CLKq%polv`Yh6@{I9m0^!1HKye!E3sQspu}rBVw_iKJbD0}Xu}Ip2AV%-Y6#Mf#e`D@nCbW<74)P#ht45@>C%&<KeV^KRi+J*j8?JrmYFZW6l+-8;R_R!OEhoGBq4d#*ut8Bt|TJpB>=@FSau+03;=%)=8O$<3uMQGFZ;7J)sPuC|K59B2rlxPaXEOVpP0=$=X^Q1M8nj6qSb7fxQ^Uv*0xdMVq`yC5o8NJvdKmfw@I-1j8?YdL9X;{<_#Os%2=cwok~Z_<7y@YkQemo=Xy3vLRl~O6!<#ep2^6eaSNv7>IIy#jW}g61aM_fxNXh)@Qm-cXx?0-Jbq+ynUBryeURj(kuBG(xA4x%3u_Yn>PqsmnI$h?rO}I4qxY7=1foy#ywzAo>zK=|##}}gjTebbbC$@cy#Sp^oSya)XCt>e7aLoSS#ub=MK`0gobVfj^_#tVv_VwWZtxW#w@Sw}(rK8s%$f;#Y$HU%##&%4&_+lG(9Ub?B<!B(B)}-=n*=s2ANqfNxR{%-wiGJ5cq@tMwgNaVM)6uP*PC_OP$AOF#k*@^w;LhHqq*gIIu10t3|6X$X6;~)W0{e6SW?cr8<7_aL*<)y6Q`G`4iRqSs7wYvSS9p6(>6aF%Y#uT-69>2;3U+3f*<D!hVzW#JBH(xwv)TLd>*dhN-gv(;<*Ll{B$6Wu=riZ;ww?O`?{iV`p5h@iUaE+!40pN4aFCa=zG&2?pg>{OciqB##YM!9o?ayF|HbpM<ZP+-npGO!z!?^G|as_ICaiOQ}Y=I%M!P`^-q<OCGT@e++mh@piT|&!z7U;EhhS`UO;i73dqXbi0DZ3a8f<S%>I=3$wCQ}%yS1?jf2KOPoFJA9$L6B`P7ovRR$W<)y`C?1ujD6anGN~5l2*6Z7vHnDU&RjS|=gTB?2jfTYUXBYfGF@XttPgM<pS9cQKh33@}Lw&PZUqCaj7&QrC>dJu{<_hf?`mLY#wmNt$#9uM&D<6suhkoM&`?a}lF!vh#B9XsRp(ouFf82uvicvV2uB(ERkE1{Ctfx-SM|o9I-LBqTCm@$$Kya>5%00Ff`MDov7ET!6Lo1a9c%QiR!--nU}J<)4XvcID6CefO2=>r!vNF8kL~IoEMIU#IQ6#(c5OINPTQpy8JuEu;9~RsQ~QHj`8fO1g(~EN>R%Nv3nO*t?og1?w-|!fq}4T^pCH`5HNsQn#asbb7uH)ZM59?Pf)wzH$K@jKteH6>WxSv>e~~Zvc_MeCV&fm;i@i`@PQ*4pt}MReBkkOrN1EVm7F<=1izJbVpMJ404yW=teWp@~#JM6sof)&8fTN)X}sg4P_y0!SlTvyydNxV+{zYIf2Ic<M{m`y4bzg)pi0D_@R9tiPzo4#^bV4&iOO)s(8-LiI6P@Bb?-e8Ea%kANIuUUa6*mhCV7@3h3cZNFbJWqFpgO^2#2UV@5|#9tEN&%iXWemV+H4MO(#|3p4MNlCEa12dx)7@oBakx9O<ekuAq)%yI#ue6mE<EKI1<4QxlKR5>m@=^9(Ez0H<WjTD5rl~LvLNR=CCOFr@Bc;PX<0)Ywa1wDjQs170|3#eHk_;|CV$JyMwXSP$0`R~Hn^{3&vhnAvAN%PZNl;-+C2Up4x1jhE&$~UcV;G^ryENXbA^L^POvYFV+TaW4l+S1Aan7uBzyf%qVXOIK-xI=2iL~}^M&<|w1a293P?W_U?<uSgCEkAGqlZIE6j)uh$PA5A!7(&<^M)DgYy);-vb!==iwMPy>4PWl3lT@xCr~b-QDY*;`tREsMVVO8cV~zS#nv)d=xzUz_aTofVI~IWxI($G=f_qU;z)1_3E~qh|__<z2e;B#?Qr(_SZi%k^ru)%kr16aJ>q8ts-GGZqd#nQd{Kk8f09~`!gJ$eIV5D;pSM826H`XkKCHbZXqw`f8Po{Kond9mtSVb~x-lUEsE7r)7wxLRwfJ^A4h}l%ZkW?L6<u;M&B1SrPQW~mehMgGyU7`O6IM6<5A7m0GUa~ax#Znu{q!T1(lsL%?#`@{eUXQUeL~}8<<Ct6J_^;3AqKYd?pY|lRTpwh0tTL`0jcs{;qDk7!p5-@cP->MWjXu=Z^Pl<3PJh;4JW#EC<@E3P;+2#0Ce+96Emw{_{SxXiyV-X?|4`WwFy0TX)9RSyz{+H3UxNRC=6>A|BS6f<8yZ_G>u;kxKaBCbM|mEcDOUWG04NZ>fk6y{`738GjP^s(+clDv5`sVp=>eY-tVoO}TonlQsuCB>X-NP_8OS$KVhuz+K{$t94J?LDIFxVSIX0O?OT`e{Pe&$p1b=~8$O&C$Gz`tl+atGBa`q%5f(J~>s={c08%7xf9JK)<i#A4Xd`eC>$-Xa87!CIz35;o%S`I6XukmOoiBo)#mN+H#qg|fC=&;L?wPj>bp$D>jtz)&e5w}l%(*$nvXRQJTcR=2HRLlZn{*}3n5A=_&*!W;i04JX|wy$M68)0riBp;<k6Ju}kXbd`B^(|d7%JEBLDMO>d950}aO=Ind4FP?Rm`@}wyStL&4rq-LCKh_mhs@JysFB@ptIY;S_^flyVAHs>p^VtwWW0d-GvV6<(kM7yWCO1n1>FhoA3NkX;Wdmetbj#CXtK+IhB1=4uESUmZlJ+-5*y_n#@6)&kPyXg&C^302J@g(kE)5Qwye(pHBz?3<*h}o{_lP827G(2ia&K+AdG*lh7D=V+Ho;$J{)SX--=@=hF_fp!waGe_gmPEocG{!-EwXGlu=E-gRJk49hb2Oznz*c)wqTr(o8vh!^bz1kY8JKuLVB-M(ZUnw_I^<nBi*~du283zKYu#V}|&H$hv?^*8&cAvM{_e|EI|C(N<0VxH(6_pH~owmYI{}!#AOB{g)@tjL#T~zp&2wqj=1X13Iv+iA?AE*NpS*c9siyDEqA~HY+>OkllgV^>F0=pGZ*@)^=!4trAiUY^3g-YH>`Dt!0|l<Rf?ksg@TA`;N_jt-9=4{ONf6Q4nK5Ek9ck|A>tv&%#kO1cPzlq1MC^HH6a%Nwf~;YfkYQ(E9oY>p~xEoeDTV3=s4mnNaprIgyZ7OjccNqSdFVOI2cqWSQXa+Xb_Vm&cjFSzE7li#~GDe?yH(uEVt+MMQ4EAngIk96!|LTHya?yF+i1@e&zi`q&x4Lzjp&ObZw)*3m@yFP3}WG`{%(l0U4*uOOs_wY0Hi;xG?bE273T#K#Oo;Sj|DOJHT8%WmCZ3l@7rR+MBeY$F>|KxJU9TKf^Im19j@^vd!XYiFx5^ZB7<>3d6hzF^zdk3Tu|!Jb-|SI(be<{A;qJzoRR#gJH(FDDF|I^P29stWG<h5vTe@9pZr%V}(Z2oO9Y3QbC55~>*wMvGGUsH1`x&A1|KI8vUaGKWsAfhZ9{cakRNWl2nw;P-4Vwy(2_;w%t*WKZ?ucU18*ldMq=_}@Oc=v=Hg*$|A_)QiJ?<mSsyRXr9rpa8X0s`e{|rmhzDh>lWWkD$Itq=j&`Xq@`m-N&x9m#|2bue~aKsRFjRR(tL;swx^KtJxamh%0M;r5KH9hpLKJMPq^C^-2xI{|-@g>X@#oqOp@%4sxy%TajMcVR;&d(7gpyJu&!W`5UV7n)ecroENfnWQksBVZ!!)rR1oj4@(+K!+bvA_*S>$l7O)rZ5=7+Una?B?O+_5lyS)51XeF`CUi{@OYDAmAy84av?mI1NSY$S^bA8I6U4d$4*21b1H_0Rthe7Ge0@oH24?Yq3f!>|$KJjyEB3Jjy+JD8DSSKVa;SiULH8)WTQo5VL^l*t!au}Do;Qkgyen7qWNG#z@550ys)a(vqo)97xlcQhCe?6B!@Vap8+_`9iWuc+dq_|bS%JA7{1MB$WFh??K>03Mli~zSP0%b$TPwqER4jNvwP$1ZGeO~F@Ctvix@&ZQej%Q4b?zB`WHI;hk=JHVwtc)UK|z&RY~3#f6Yzzi3MuVQC0r9yh*a%ts(u2VqGHsfp8ylUsVjxzDRmMkp#bI=x+y((T`RPwvbJuVqU{!;frXdYwZ1I_ab322>Z)Qp!xdS{D{H15=RDo)g1}x~T>H2q(j|2kLgP#!!G1bobJwF#2ZSK9ooZQ3u+f~P70fL)F!sWe%iNDzg_zj=x%YOX8h=gV!oS|m1R--daqj%G-78)U%D6NNL^THTcsqI5u6aYFT-C?hwYXROaxCVMqSxszl~|X`sHLBGhm=eD7TwIt%Ooyh$!4hR+T+<%#bXW8gn5G8$5Gr7(3&xJhdZ{Ff+_eK;XWZ3o9<65OKQA#>uLQx-AO;*TXC7=cyovl>3;q9$DPrhz4bOmv&5sv`@?CmV;wz=6smqPmvm>sn)jq3Jm%uIr1@>B)2Rf4yJx2pm%A?Bm{j%FEhg1;_w14L8_3y(d-$(?#e0}oytUg{9{UV>QxJV^u{woW0L0#PZMP25Z$)hf-83+UNc>Z{TSwLJj16RRBXOm$*&$s(qoCJVcdL#KKE^jB<}FuQXfvshGYe~L?ER@o$&aWpZQDx_MLA);gxpV3IEnI{^9%3n?YM;NrxasGwVraTN72HMvF5BpU2y7ZlUbXYR-5K*lDM<*#nOSXL8aDXGlY%Dy=l8}k~C*JJ+nC0S`Z5eVl{&4=B#YB8K=kI#|{0M?^B%~+=HuyVLzPQIU2O$Vj6_`^3qlD9*m%Gxj$h(We?mRKe*wG*g?jbsGX8h-JuQ8Yr8>`8VIQO{=f~~qYEQmDl@GB&Do{Hjw-{<5qp*iP@`>-1ed(ils3yF4=4nl%$^Lms4asBvT$|Y^vVa<)zmo?nhp)jY<+_a7^HSg+@VVRrm;&S)=l0*%bKYI4H|>*abiGs1vAXx{eESA(@cHN9s$qVKp2bneyHvm%qFb{9Ej)I@*9<*ma6$KQ2+n+t%5bn2enQy7OWp_uUm4(6-DgAolB}#9{}@=VOFi)sfuatm%{OsEGAPbuiWW_uY0~&4TZO=4zOJ&QoHsJ<**y1KRJiKdVZE2*_zxqPu4RLlaki;YVUR|V*!<?T~a`n8LSXY6)S+oDZ{j~jYbl;lG}c2#ev!!WFyTgsQH|WP9h|xWO<E?2|2BXI||m_tXi$YH|x*7Puk4^E}?dwN@Fc6&O+^AG3?FOCF<jtf@L;iQ?gHw)b$VtlqU4Co|y0sC}(?0C#G7Y$ixAL(I7EVG_P!V{>2x0yOz!C&!B45z2d#iKJTn~%BfOux<rt~EoweJP*p}E&&f7bE49|40f3s^qsJ6d`-{7enD0#}ML@F744KteM`(P_Wj#|__`8%oM^aVW=>j=^u8rxzX)`C;-28wE^QgCLnBU{>4cuy>q`EgSl_s+`<yZxGHp%g_gW$X@!Ie+>%Vo`&(=!nLPuvT_4>y&a;Ry^46#V*@l^;zc_>*$XmC3WikWH;?YQ440Ztw|Nr(m&w<#kwu2pGe<Jhp~HIEOwnxML@WOWO?C-y-SQ8qB6^F;9?I2(%pJ&x-B$wu541WGio#QD?y5Td8r#`hNMuo>7L4i87Cx2KB;*;8eUU1(jtIX&#ik5K|G?nRGGob0uyV!7U*hlM3W~Dh7l2h3X4PF<17-7*@#Zq3VIO4<x+8B1JO7tktG5Vx>VGq~RzXZfww{y%|~CV}S$B7|t)Zic;#~J}Y>Ejs(q9l>v@$wICjTS$TrVK@h}=HeS8$2j2E=z3o}I9p=NS%ozxpDoEb3G2vO-8Y}Gt(1v}z;cLg6CY~wAELMMS8YktJLdUqI=Ad?#8=|Iqu>X2iRK!@|Q)P&iTfH~-XxW33%U71`E^IfhBwu@u`=&?a95_t&1aqMJNKn~U;`y(_K-4J(6gc9%4jbBmXsN{Ewze`#rd!r_?M(VyMc#4~*ubR0OX#c@$Uabc{f}B_i(h0}z!Et7<?QiKf4<wFpRVVJ{`1on{&a;uUExoEe!9Z%@@IH2e}=byZ+@F+^M^R+ul(oNls|kLr61_eaQ<w5e;<@TUD&sIZ+i02w|eg%oC_QLSNb!&r$6(H|CCFUpZz&MEB!e>>)+zf#qa(_zo+c&P_6ZeUhuE0@4EWn)n{-28?OJGvaf({Lw0-fs3FQ@tmykifnRG=%46T<{Kwdc{7KpDI;o@WE0otNGh~3Uk0C?`Yh)2bY{IbGa>W|bic`=hi>~JD>szxziR8+-Y#e)bC+rt<I^(y9#1KbebPe@yFPr}uX(@~adT-RCcJbmWjx&4X?LYNFE}S1>_B$&s{qhKY_Gk3x=O3<}zxN~QYWy8ndq=3g-2xS(U7Y<nURYU(oSok2*)Uzw`4y-q<}7b9r74~2<#|p=HpqPyX7hHohH|<~XQ!tDFnxt^{uOlQ7k8(E!){!B8w^j}&G96OIu}gUYKwQmhql%)2_~w}Vx0X>{JZSR-T0^d8|*2b-t<WQGh9A3|JQ}vPo2H1yZ*B0kLG7*I6L$4&(JTvkz2m(=})};H`H?o*G|R;*zNNlpIv^JaQTg{o^4qEX$ZBm7j&~fm-kdZZuYyKRpaK58@QiG(=UGZmf+pxLB`?q)TP!bB{x1h-lOrAG{)2K!7kV3n7n;(QH7p<V+e0|Oxrb&M{aC%jbGU%qbN;RBVNBa<3)4z?UgO$-PM1?{9jvK@YDhT{@*RwA{}Kvw-a40%;{<aM5xdkh~REyh)P3US|qEyF*9)>_sEiXNUl#|wFb<Hs#X-b+8K#IC!)ngpkRZ4AT#Q557(oXL**xvuf#LHTiVb>4p(u$aOlKXL(d@CR3@mWT&|rOD-6H^t+@lut+g7U`mf6q>XM$MH{e&^fZ=#Cm6p6T2?D<PD>jMM1M+Qcw!(Q;fDo{aqS|z9ZN{qfFBVp7gkH-14f5$D0+DO7pyBpm^mJ0MA!d_mP-+pyA`ABEW>vuKj9?kvYRMkZIf;rxiC;O1gr#q>LZU&DH{v(tutoan_K$<c=<Cq9chqL#A~2&d4l(7H87jTSW1sSh&{8gv-O;SL6LeE!yhk!SBsc60l>qSI31cC1W)Cf48ws6MV4*tRd7v{P1tgv0Mi^k(T$AV<&FvtTPtD1$-<lfc9XZ!zolwSnk1H_@E)ziUpieomtBF>dYhmK)bc^s5Pq++kh`z35c}GzfyenGIO%3tJJT6-Sr;lDKJ5KC(U3t-{G`_F0DsSahJuGF$7u+C2h+T>U0dgjR@zLGs88tRj^y^pG)WyqF!)<kO=&Cy5<F2TShnWz=TwR>8sjYmVX71GGNQ<ZfYu*5ClcRu9i%0PVUoXqcbbw5vq`7decDm1;uK~(4LO)0x_ojdKT%yf~dm#sWH5icm_<klXd!{Tq36E37lKKlDUwHhly&s45Bgdo3AHS_5*}^TZCpx5=%Lj()MFw3Tjn*hqK{X;<Du>Wv&r>s8mQQ9xMr^=VC@jvc1%YiGunk4LL)b{O@E%MPPl8-0nDLGS4NjogwB3iBeqy_-lyl2ZjP$VbWfwewlT@J>W@5N{>zSF@=p<Io`Pj)!>|;BL{V(rlD7~WyjWdnv_)a1;z2zF+O%WPXpKPj+T|*j6Gyyb|b{gepT33fs)t+f)+A|QaS?Uotrbo=p60u})lx<o_5-aK%J|Qd>Xxgjc?@W?d$UO!$dDM~Lf38PtA<qE^Nv(W}Mx=9F6(;{=O1?h}VFG5!XLEKn^1tN%3qSl3_xR{LntSHY$#Z&y&@FD!V=M_v&-0;(3t?I(LM<_?Avib)aQQ$j1mU>&=Mc=uyzL1UbABvJm)A6Fq+Aj!)NKEf!k&>($G+sUG|f$&#T~uoHL;j;U}f6ZHLH<Hk3Cfq%{Jq6NnkcbA?Qv#m{Bf84)E_64)Qb9xU__;6LRdqP@$o|azzPXQ?kF~ekzFFK^S9s%b$A}(`1TXHm~_FL%kPVa^<>K2Cl{>!<VBA#hTp5s6CN<%^BxqXb~9ap(@dqU`Xo+ath>M8Y%Qee+QYqFyIevOZxUYT5K0rE+!?Arr|9>te4Vq2SG3CN~|S*QJp=-VTKR^y(a*d?|7ckvUg0L6E52>Dp6pf$wxYR8+B%)=lz~$Hjyd!9h~HP_`2B%Yyh7n=@aa7xNUPAMSH=$TXEpGBC!1>yEElmeE(_GcMY2xCc2j~6PgWR?seC!>bH&5dzUejAn?`PskMixJqf6Kkj`NM)K^0)=e0Adw&*r40YXGMFi>oHj8q0jO;xEW51ck2PT*E=6cBh$G1m~65F0xX$#Ev-X7-e_ODah7!A6X4G79|~;XQI+&{hLJ(;wJSdzV{k`4r<sdu*moLb&n;5})*y&%R<NijbR$yrd)-A+@+f4cUD7#0FFnqvbLm%;uiWzU=S)Sgeh>gxA(a??wl*XO_ok=vlEmMV&X<fUs0*<0jfm+G^4Yy|!9n#a^zKGKClo^`>pYE%pAV#oBHyl}(ikoh_A2<`zq3UnSe3gao)$=CssnOA-*B7RgTfIxL$%yH2(rT|(fWb^oc)t<PG7wTgZVX@AcZxO>DB#|YxH$)DAA_!Y$(+0oL%+mU{X#WqimJU-f%tNeev!FW$qI-%Qy4h%==<d=_L1tV^EM~)*WQE>e7Ic2m~teLF9*AC?>O+ub{gj#MYf%8Fx^ati}mD<2;9~>`9whbpx=7TlpV)F=;cYE@xrpLekE*3MR7>M{EvspdcJTU^F*~%pK11yYZ)~>3*jFdeW7Be`)TlvdeF_$sFa|S_4T%$qKu{YSshmeA63yT@{B;+!aD{;H+uDi_a>ozFdbeWl~pgVfQjs7z6iocB1KiCD_c$v+Gg~be{Y7$ahuWDS~^FM7XL;2Uf+RDW6kU5z>?x4148i{8+|1{tE&kbdGGw(vIJok^hdrN<8tY6{3-8+@Aa{Yc75f=-V>G=5UtI(_d+ssN^^Nv`1p0=zP{W33`@7#<7pZl=0s+Tw>?c9lgZ|^S4U*3-{EmI44{^Le1uI`FdcCFQu#5OC`k2)Pzh7ft+Ob%Y})Dapxg7`E10?kc_^tOJey`6KYyJke4>+$7lFzYOsEUB+Gy%(3)Oka2W%BvfF3e34w%jlyrFwZu|@v@Jv$EWz4hg$p_$KP3n&x>N6yLLP5-{3B8u6yQpF7pyMw5jjsKMWPVn<Bw*#a;VsRM@&T{+SnN_3Ra>Gid2d^>O0I?|h{UH=`_iJ;N<oXnT?2LX@UvxR*N_`qEm4+nE*#GTf3#=2?bI$pTFMR`tE5eLO`HY;w1t{Hev}-E0y+k>Rqd(~536SHmYAc*<~t>My434Mun!AW?F6=Si*&`55MM#6G>umPGEl5I~D)_DqHFYOsq~>919S%DJp+ZX1?mpghZMS1bTEFD(Fl{KWQ`7m4i-^rC*2*rsEo_+ZSkoT3+{R1OnwW<23m(;f=5_kop*#}0I=NG;XA7MmWoD3FXvZgY^tDLC;mh*!dkuYQ18Y~af}Dge_Y*GrMCi=;x4uNs`Ct_P6=p}!Z~XaY`|C$Bo5dfuQ2S88HVaC{Y4mfN!JrHr(u@Og~R<&iz5{B)93G*Gh~Vv+FOirfn`E0=h|c#wYv?B1VSD32{l8W=GYA3Jid?2Q_iUwc%PI=0|AOuL6V|MwIPPo_&zjxv->3+|%1a}7O`WRio!c8@MKJvi;zxW;7e8|shUQEd!G2*|OXdbjTJc*{eTZ_%#MklaQ*yB*wGHcjY!h1`OG4f!2D)pwK;+n@r~HD2`+iJNv^=ynjfDVJ~v;o;wWca`PSsISbyv|rYDN=V#ZYAX9QX)2f84v#cj#=r<Qos#q)0@MBE8zuTIs3~D>q{p|LX)1e(>oDQUCEcJE141Q46xjiV*@kC`D|z;?8T)&9oJCMjFE@#SYsErOrzuy026j{BW#zgKQW6WUR&AIrl~3Fvn6D3zK##hm&I4?)20Ol7oFSUfa-6U7gMIGZ=Wgfx;h$P)Cv{l6x=}kxw*nvt2uQ>u7^<g7Wo&8vNI8cxsvg~=gAksXLzLU|po)XLN1Z=>?`V!KrwB6c=P2x<a@|7)ER@?qefRQWB)H|&e)5&dD4dlKLbEXrXz_gIH?#vPlM6Ls)SObeV_zO2{ah}?J=PaYgGcU$^F2xri1!CC>GGd;v~)RX3G#adod5W(1!Ip?lvZ8kP^Dshb@D4qww@}l*^K;qGDlYopAdb-k5vkeScXk4R-L(3#R2wsq;b_~1@XzqrUFcsh=qYJad)ByxDZBe-^(0?dTF^)y|!^3{UQw)722MGob`Okv?Yly_mwN3By8l>>h)9@r7wkHM_Y+Yj?I}64b8#jTW*h0@@7<sm&zCU{Z6iLa!9g3Q4foIWHl6kSIVa}o!2GBN^GhP^2^4;t9@#el&(-@zhx1IUU_ewk3At&%0lW_$;a9-sg!oxDH&^g-G^P)mzj@2@q$9w<&oTY+Qm%95Xls-k+^hoJEC-veR-=jC-z+MK%=|Cz63PuxgRo_6c}}N22x=Bk;?W(#^s;LxFoWm77aH&9W-?f;|5@LFfSC^p0J`tNK)Bz3Cx@48CPeJ&%L>wFzE^**1YR5%ex>pPi>Xl(f2u>rCwBShdu}&`5IHN_`C03I+Hc?Tb0gaJirm19T78f)H*Ag1*@11^NN{P54SYcnnv!;>RESIJxf+MGq<efqHY$ZqS^3d(agqgEt;h(MKe{#{Qjb7c4o>v$PtH9V`+ndxjHYG*`V0GtXxJPqooUT4ENa+9S$*$C`7}xa#?e&T*mVZcSh>Cxz}yJwvqcke-Z@vx&#5jyYZwx{rO2(;S*!}(-r>o=cg<D@mc@10Q!me|B3kjW0pMlPu%}c-2YG9|3B#5|F<ISfAxQFQ2s}b|65W1XCli_k^Mt60zdZR_!~Dr6UQv@d*jW(fjt(!owduBrNclCRNqvWuQ(FbN7jEJFv=+Emwf+FEjn2Xd73i6V7O;1ei&O{tpBx~#ojCHKh9pzlag#O40radJvIME8tvZC$@TN^HGWq8g)bgi_MJ18XtIYUrX8eZqaGPwyrACKKPPd3`M02D=lr{maGKzk`T+Wxm7jb5Ez;Syn7;l(D?sEgFR&B5?C4=6UD>Df0h}7P<A|z%R+jhl$U;WI&twFea~Xl#V}lp->_&vjfL`bcK&qG^250nCnVJ|Vlch@b%4CeF_s*pT+%>6z@SNJf$giI(42-`d6MVQqwC~&#QUhl)0<Jnto;^GL;&1+PMTo#p-19R!xgE2)!95R8>IS^**(Xlb`6mzJXVL`AZ+GR~=BM4<X47BX<>^viyr44N-5Fngu2W$<+4_j|WY4JgE}n}UoNFC~Nxr~c$|;1WzK*~6Mm|)rf_(Fh&k7NoU6#v>6Rrv=+z>06T`_`F!lX_xUYu}wS^V`!mN3F|e4Vk)$Dc(V{cpSr3+a~EG-wdBu1{FDe9)IPh-iP47;TW~Oh~kBLRWG__0@E`vo21hyAS}~0X&kaJ1l20Fjz`Pkid#)*<Mut23#Qz<Yqr|peI}eWErA$Zlds;Cc(_N6EPgr3(3)x)iZ2zX(H#$4LQ1MOdYLB<EJJKx|7Y=r!n(j>aZudzvAPXcFE;)W^HxWRa_F9M>-#vTOSk6^`nJr#+8nDZFje`M)&F3fNGrC%+Q}?VaEv%Yoqp9qkCqeQC=KnT~bDF7n{}w)WoqbFW~i_`!%)e>H#zN+?2;{<<*yAklC6}er{oIu4-+dod@j^L#q^!Ov0qDpMABq8fqMPTbh+gn~yK3iIRX0kzNp?=_|g0Kk&ixGFia0_qjT5c;MJtvX+O<=*j|zg(zr6CIPO|WQ9*bt{yWupFiyWtrxr8J!d{Y5FZt*`TQJ6E`OHBZ`sSt=g#w!?L7Ok>W#~JzBV8`f>|I5F@^$k`Ad$oqI89s2@~XkdzR?QmKL{dKKIc~jfU+k2PyNkH`{r63lbgU!kR7aB$Nqnu#n^WftSh=P3880=LHNX4<6PuE1>gy36H0fGqg2B_0HQO(4D}1$+p_~7y6q6?woRY1om)zaDbU89Q4|h!L2K|4sfiF>iyE6@*`A8l-(**1cDCOH?eD}XhH(@gx`wVYuU<1;|FAN|EMzW4kpmLMVOeh<d8{{UhjkL_o`@)tyQF!MHw~Qk<BT?90q_5ktI4K7)G)D4Fv$A^oge*V$v53Vaf)W+-Cs~agwH^(b4HSXw#U4QX#m5&z@vMpwyOJ8$dh+WeZwabr}Wz*2~}qZdy1@9r|#-(KYjQa|!j9#7FaIw>4q8J)UU{i8WgvnZKYLjYVch2o>fYVjeHM*_YPyZ22xin|VSeu9x{PkSl%F`=P7nq=i$zh;bfPGI_Uqsx7^|AcbBnqp^%DQb;T>ssF|kZS;hL4wZ(1X!2jWUySLyF+9=-=8;67J>tkvg5MtIC(zL8Yo_8c>N8E1Q|n<d1S1fSM+gMQ0s>{ClJ4ji5<?r}#2R?7_SH_g>}d!2uoHV7sAr@Kzg)sG@Wmppk7wa?GgtgQ=JQcbJX>#UYUg*tCa=pyrEL<e9%OX+h=@izayn;XU82}e6U+lS5d4d@2NMqS;ah@#RWvB7MV)<xF92@@_zor_4OcU<dRkMSk&$lGAdd+W%n?P>HsH984G~Udb>+0<)HIEyAWs@^)0Ffntv_B+TX3^+VI6Ej&7C9iCQ7`)%pDE0=jChBnI~uZH{N;y8o*q*vH;ye=jOT?=VxHLTc({^8L2#kqLv}Taf#H$+)Dz*RUB-hQQsV?tFTg*m9AoR<G2iAVJe48BVnk=ZF~xvyTLRm0lM6Qy_1`<qfd+T1kIPlt~rEbsG0<cm|6-aX$>k@de~ze0f<}9;2syM|IgogH}JFInB&@<oS>iO;0>KH8%hWfqP>tM@N2J9OQ^~OGGhsrVgp+b7_e44o^NK35S=9jX~QGy-cl4G%Zxd?a)h3~!5()e_-ZoLCl-2m#GVHvM;I8sBn-dT=!6Gd<l^7(fTC({6!av)!6kh~e`_FXdFJJ2uEjbR=AW7*lJSCLtKj+-jd+i>l}T+hd9z3ZX(};P0*I<PJovi2?vDN`frF)fopKs$ta@G-hc<K6X{f3;P~{>W08VOm*xYO>QImfAE763WfTflQ)?dI<nLn3Xvdv3aDy{yeSywiJ@UyD0)IeDU#F9wX05kW-FsV|<lG<A4oa|@~B(N#4r@>PAJb4!r?iYYtOfx_#_YeyzAM4E2i)-8{D#!9W2V|x4wcfm!V%5%qpZJWvcO8=&Vl~{7_0>`oOX{k;gDnfS6BlwOhgB}@x((Ax-Y)Q|GS~)KnxvrP9G}|WAO&67M&h$Rt}a&moew40u)ikcRs|bO7wdg!HpG#rnk*Bgd->bx8MPE?@Rxc<GkJz{zin<}MZ2_AKT171Jgv~s`In5`3y}t;qDENrZKyg87b<QY2XcBFk%qofIpZ~v1`Cw4k()m@oh|-{?@&~0=@6W?j3yZ%;;UyrEuCS_!*c0tZ0R&LkWP!!3UK@K_Ob$RGjhoFxMH$t8N6`L>X{ic0!!FH<}g>UmbZ)QK0!J|8j##(2ihrWXW<F_M_00?z)y*@D`tut$-+i$b{QHYYZ}mv!3Xu^C$;1qw<wPw+>lyLmoYA*8>n8<7c8mRCe1Ew6N~@|VDo@f`uHgAHyDpHa#7iE@Z#kG3O<ArjDC&1v}L*Odv#?jS74>`i<FH1(iC^Td|3snT!6bLm0{LzAqx|a7F<?bbznWcj4WM0qrfY&q*+*L?G8)TpgUUuGgiRps#kJ+Nf5anKGY5_-?L*u>$&Kl(BQ4`aWymy7eOJCx!YhB%iMWkAh-Hx_MLf<HHs*K;UFdr;ZUuU8|&O1%K!ZX-PnA5OR7W9rQ{mb0dB<2lI;*KR6?F5JX}!;nH9md-ej^U!|@`akf=&B>!jWvRKKW{obEd30f#CtTfIOlq`ggh7#Q_C#^J5#dADf~Y0?Uz*w+>21BszdQj=DXx=DV(ryKu)!;lwq#(!9QiQ1vivvO7>eL^>6kr@RX{7gDzHzWN^K&0!vbg#a?73ViUR5pJ}GLzOyKg;HunEknenWabp8?lLGHi(^lF80w$L{ua*xh0PYy+=Y%y6Px*J2L*4Br`n9oL<EX@ywPvy>eww<4_+N)M|2{nu+3H(|RKg$|ZP8kzSVB-;-FBMOjoH6mhAUt(ee;0AYl@P>!@r+JnL$Ns=O&4TgcRgorfe_4=jE{&-E=@$1&4c-NSFn_h;1zI%Z<)77xc;e1IoyA^g-_vymhFw9stui{KMNM;LhCPrJ2g3fJmCV5}q;+cgF*~#)Cep;WY<LA!xnOLVlY9SHJiE}26ZPl1;0zJ<>>m}3#PV^Lck2qTsY<Va0Syc1&ZWeHpMl|IHzV1Q&KYrDi+g=eGzbV?hnkhE->~v=E#!<yA5%yA|xsy_)+fdaci#&Z>sCjc+sQFNZn$wd)&3Pu&ynbG&nX?U2b&_Z%tx>9e>q~uR1oyTXiMKdsi8FUgapv+(hil@@?MlkbsK<X~apvE7?<@6u$lO|~*UhN&{nEv{45BOg%w<q?x8=9A{a}&1>FOZzY>3x=2>Iog3iYm{Gf;{f)hD%f_vr~Ot*ST~Mm_qQEA^#pmWhSW_bR<D*=KT-m&(k~$W3x-_wS>a(S8F~aQ_>N75qJAmu0{Fo(F8al3-$BVr?Gt%26qftr{4yOsQq4Vp2`bE}NQNLa>5~#h75mWr7*i7A9olGP`VM*=0)%kR_O5$}Ypjm<<=%WqFsSmaS!!@peXuu{dD+JWnc-`ar^WRvBhenFUY~4gF<RwvSvK{;Tg8Og}?`Y_SBt7vF?DnI`1bLg^491?T=Ah@N>Y2(#9fDR#!ViTJ|xmq9afJYHRSIRLlB#Rb{M0O;X%6vw9W@?!mMx&CThhRn>?j1s!K3g1y~m5VQi(oYjN(8?J>!Y7kCf@O0}Ro?VWB+4!Np4MOISF=1W6R&Y}A6+Cb3?Huh#S5-R-hAKy?zD_+V-Jk}MT@xB!29URLhMaKZ^aH~*XT1WYg>f2#JHx%xd~EqQ*Xg^@;qQLt)Go1mI7rDGX}Mw3Lpxw*iZ}43W#Onef3B18m*)BvmzRI6qlW_n|gSDX^z1CGC>1lbmJ-<mXdf<DK|+xr$HSUyhFd-IJ00yXo&S&o^61A^frS3vu`a=c3Fic&Zu_0uHo=J)a5G};tUBPD4viIGc;bDpm^GX$sQ_*eqew~x6;zN<Mp1Pc*@$j;T<L@-XQJa1jJNL^su0JjAa|t5Gg<x1<1oL)oTyCJwxNUy_=-UydY!c)jbx?b(u#)*s;85_F&xt6;al})1LP^A>qaD<yghnywjdF{k6H3TYTkM#$@gM^BE?ujN^R-hY8Q3!;#exS+hP-UfrsA#I;|O1&s_eRLXmInB-+mjvLXA`mhtGtyRuy)^C(t1N1S85R(l!)l_g8g(6uzV<!5#!?dRr9Ku8^e4NP_N`O{~u1INk764=e=i<ouxM!WNT*yQtwv{MH^k}ofoJsv7gjLEBB0pZ!8DT4#4W>9=ehqjczEZMlNqUOev&FtQ*AwC2Jt_-|Q>k283JH^9<p4Gkn+M6eOz&FX$qUw*o^gm1;Y>koM2ZHAjJG{nVhvprsH`2SxQ!cu<yGFZC8yKTC_2f^FJw#i@JpL&;3)50tN$ftT6h352C`xP?|!J2=xTqvd;#ps%ChW}Ekj&`Ts-$G>uBzjuPsBYu-P(Hj;F30mx3HFR-#BihOG*-B)iHk=PKIT6Q?*87{F7KiO)<nY?f`CP<aEb)~h1R$<0m6y!M0PhNN=7wkjP*NMr*%zM!6A5^9~TO0{QBHxkr6$PgVjhFq8ex}Nx6bD>sVy><UmOvcAwlK#&R1<2T<YjPcsp;iN0rAu4ATWE~Ap4|k+m{3DEyfYA*=4gyC3d}9U>@cyflq<$QLtEiPhLjAz*H^sdISzx$!kyJEZVu0<nhZO%KCuiCIh2$Zsn43G)@r)+&WpBQ!x7Wlkko=Gf6!xVYy(k!-!P{ym+Cl<$|f9B6l~eMafD)Ea)fGlvS$1BjZivP|DE5*=(c8wZVQWM*oy&f{2l0yTuT%c-8L^&q_ZjoySi^XNMD9=6DZ&sBA{DD(zynsrx>_@ImYdxJ(j--7`NZ}BxCnUf9;cY)u%r{UExnx_z%XPpDx8Gk-JYKcc1?JBy#sj<nEKm-6xT|cNMvF$zOXg)nA&Argmq`Q+lc9osg8UZ>0$ZeNd?G11qxf?+UH2maP0>3U@q06}j{AOmIy$<fFpfC_rZI-I-3DwP?ajOig-f1L^Djib$EPxy`IK)d#o!T(&H}h0fjC!O!L4)^=Ds^YEm?T{u^`vy(|@A2-vgi&fYz&xGxEXvd9e2~t>lk-}ZRrf|2KL<S`YsPA$qZ+EF}7v-s%+~rrERPD~c0!qyI7P7X{YbF82@yzY(gn0G4@H$+*BMnE0eIrcytM`=T=v(TC7kYO7T+9xUp=AYf?dbp&P4+IHtJg^_>+IjBmFz~LI?E?7MCIxW!d%|&s<_(=pSmeycTE89c~!W%_*d1lt72zrcuIrJzfjNaQiCtV4=!ovm#TIl+3)p1cA;+x+nLznO~Ez$3YU^?>AIraC^q+uyxrUzqmGbK!7bG5f2M60E*?2kyBmLb3&FdKyU*6Toj@3s@8UD6c~9vBju$Xp)5Y`G^#QMn=$$Jq#!1$2`YubwKsS?;3^y*_^oXAn@fONC3)9xB*ExT|d5!<ybHDCa2X>FX?Ymc3fHy-<!yS5*z4YLM&xbhNld1qOE|6B60e=o?hQax%JVfj;9?4XuBc#hW4gU;rXwc4S&~qS0II?#lW(QvHn@opPXpfbHc*$KgE#P1c8>79w5?vQ`i4tZ{8|x<yz9AK`B^&_u>M*P$WE($T462UZNj?j#S$QxGu@8E^ojKl;!@$`|P;2=YKjkZQDGU_bN^K;9TN-?T+M>G_g1%<#;wr<Ov$F%@HGQP*Bahj8n8%k-Z+ozi8$Mnx#TV4WY0Ag_(EkXs7gTlv*kkbU^BWqbbP=t+0VqTwm>`ekJ`3rOc5x_Av2!(07;a4wk#+EEsKWWK!ByXsYoE%uDc>CZGu`<z1b%890*r8?aD%|yx_<BTI+4znghVd++2Bn-5Sj|MPA3DS#PFs?Q|t_V3Pf_bv`B<GltOre%w2|cSoGcie-fl2vZWClZ$3tr#33L@<l#Ch$8-tO0qNd`0oN%=(yk}4i?+!D!!w}!`KEGx&~zt=c!h`}N>d!#@~3%=#z?d(p;9;km5^FCJ+~fGBjC|-HnxPwdinX15c*xhV>)&iS2DQtAd;{%2|YBZw}kK-P?ajAL+RW%RNE?tePcaPT1qnRchqDN@|xGP+;LK3z4?x=Ay5_)bNCkDz09q09H*}SP?=Ai@-R;{5CyWzFF$1NQ_(DV!5<>+iHvE0yUI!4Lv{)nrcD{t+GsJ0A(Y6X8@T;!$odr!PUTzw06d+@PNmbCcYNiM>S<+1a0>P<jG=?g7E_iUV}s_!<?V?3Zz3*2j_5P?++1yFW>>Dm8}>1i{B$kY@k2jETl2TRQU|_F%Hc)_ehmm|xP&%k;Qu-z9M_zejQ|&O<^TyA){5_~>yB1@<B21hK}INv&^Mv0`aBbAgaB|uH+5ymn?l{08Fjb7HC0d()n3g%($8>BqZpw88ICa7rpgLBK%3Gf=cTITEjTZRP@3BE?JdCV*pu&g4I7gU8a=3qwzd6ftB>QI!d^3tqyhqNeFc<s^!XgoO>2CeA<w$;;R4zO(BG2kLPlX310^oDY{k=N`>h6J^v?pBe*Ik}Iy!2;weWSFR616!Zx<>ZWszNrRWV6);BH6iLzO#%-C^$~Mpween&ALi9rz`hSR6%C4AnvJ(a85BJ|=L95|JVhdyOU#B=k-Y-jm}iQZhy$@iOWYBQNEw5EQ8424M`_jFRCr7}kQ?aUAKCuwv3gv`?=DlZZ;FbYM#sI>t^4^FnuEr4S~0V~R?EJ`-ajx%Ew;-X0FME%Ci`4dg?(CuTa7=!aVt4+cJrj<TS~omA7^g8{C*|LgCK0P+$J=CcHl3iS~OWWgl%OJZh{ngN(ehjfifm+XE*TkRH=F5c#2LbL^}kWd9q6KzTN1O<~Q?3egRMG#_y&-ikrjr1dD^B&7e<!lo3(*|A*#)#IDz>d!?%lByywo4ePBKLrDlbeYpGO)r`&iU9elz((?=Ku4KH1$Sy$Zz9<I_Ic+EImH(S#s3<^U@%r9qJ^Q9i?x4o1@-Tj=Fy*j=G2&Pl$pXo)iTUM}5omy{R1aCv-vDNf*R8>d*zbAgC*sS-BTTgH(2UrsMXRE=bQ&-&cZqZeA=363-Puw!u_^y_<AFJ`S?%_r5;$wA<v(I-I$X-R5s*EQn7Dgj6-eD*_=N`>e1K?XCdxSQ9bkTw)(EVul-fAv5w*;_yM%mLw;9&gE<f6`q(+lURsV6ynR=sm172(cY9og4izCsGXcBk{KFdk!YLrEM^!<{+!*}R(5B8DZBF<fQ<Y__alZ;>0dv9LWqp^ekOh$rg}`7eC;mfgr9-6^X?8QlbT+p{P7AS9hHHS>Ffd(L1Ozz@AeYS_d(n3FJ+c;ADE*dY{jxj4VcwilAlhGxbu4wITKql9a&K2=Y(HSbBHzJT2a{-K_>>;%aAXH!<I~E=$L9H&+-s*pGLY#Jq58lZ*RGm^t19Z*U+81tX1~CPDsirFGGE&@+}S;^^!1&;jg?yzKhT5pq|{{+59K3$jIAKJfR)9O4$9&vqu<S>YB-$-KKr;cV=|pJmqY2C6z_116Zcp@LplZ%mA~NEOxR`uX#v`VWZe5>uX?o@UGjGR_UUgRMTh&hoqWu1gQ=vLFU!K*40c>o5u_i>cJ9eE)CFz*N$={jd83pfssJ16Wn2Oz;$|o-PH1pv?2tXW_;H9J*D#!g)-X2a;GHNnBQj}|6XdI#B1~W65!mCiOWD41F3Gkv2Qhvdm|o&Q)2w};JRs?fH5WjwaNg0x(te;>|%c4@+0b#X-7sm>Lwf)fj?_DUXIuv+#kWF;C3So4-BW})E_93T{7eBUX>$n1GfkGT4guaaG@?U>e0oOb{Pj;kTq?Ia7*uvb$0Mf5?maH@I{i$yxV50@HYuNtig@(hje8ZzJEfom_`a=%XA#B@jOXUV80J0liP#oAi3bNB#fT(7u0JOtQ;e8hf`U5_mkyaM|7?-sYNK?Y$FyOE+Rq1hZXkatuYOe_OkBgH&iph@2@dA%Y0gyimy}p4)25i-Tg((_pUa9^FM);+klRV0gkYi5OOTUm0!N?eVK=^v8f1R$|aX2eo?+n4#sOkDZPsOkFq^p8&)nO__8!B@wP*ipH~m>3awM9@&=RDV9kP6sd8(m-yX7h(3JiU+Qa!Oo)}ERC)EA?R^1ZtLRsA?Gdxqgl3pj&ah4ngjW<Z3@Lc>+c#O8_i909W@`zxt*_Mo1!v)yxc{#l=B;ysWAJFqUthhdxuhSp6o+G^bLD$Dw`p`m25F>i4*vs_v&MLI*^lMQ@sUoxvMjl`>WE8MB)Y#nc`e(Sza7jm<Pis4u?qqlZVd+}!7NG6Pd&DdyYp+L%bmr*1Vq2GN{IW14zZf3BA6XStq3<aYE*7j5|63+DxVHZ6$HY?-vwWl!Kk2zrtR6WQ4qPl4^Os$aiwzO;6(o+wx-G6hSaMe=om?=!$n(yUIb{JmxLrF*cj+Q+8#oUnnf+A`c)7X*62u$QU3>00>Rrv;4M`1KbE5a=ACl=vVIChU&>Ep$BHYwF<+SJa0oiA6aI0C4#ahiX=a$5hJZ!$@=hFE~%3*tBgXvzkPG>em+@_O1C{zjm<<`mA!Sm9eiA|59H&+tP&YxwOQG$LTb>eEk(<9Y&lO^XMx%E}GF<E<wf6cr<{GyL`-e1$vstHBoO={KfEwE<7z-&!x3YkFUy^z*2S_j&WwJIJ4Z61coK=WR<QDzsSoGv5OLibY{t>VhMd{*#3j1C2|Mo-Otl(veZ2C8P*MO#$*MRojx@Y5E5{z>->F>PZBA?e$QvcOZkB2~L*Me&tSlEo~K{{+@$PCjmR9?SB?A?En{M;7joCNiub`9zN_$@T(ku-p|*&kI8pH4LVeypRXh9`k(|_Zs37K3eu1yA$TbKo=0=LCT$p`K0YtIV((&Y_Bi*sO2(N=dPBEnMZ@9<B^)NeAhrdFXWFWOLn{a3LOe2(R8BqjYRO|8;DPNQ1Km;qj`vw>xuc!%l-pdz&+BH?w}GfNa^9%O3KsheEv3~((sv2Tc66sPUP%+`*%ISHL8rBJYe~NY((a|*;NYkqn#kym|H|El|=&;oTDU$^(;CWK{2b-BW*ymGDi_?BFuoLk-Rb~q8^E7Nj(n?Nqb2n?1BP;e8kG*ubIV$riOrlo*|T<-SGwAVQA;N&qC~$Mpk_4bK(E^(OgQR^sTVjWs5^c_<@sARxJC(^5>UHBtf2!jtTW&JoTu(=D}^{b`Y%I1eJiYOtSi8W~~VU+Vk0_BhDkK<|#J@w@!84Z*518e}DT!l`}?-=4)c`PslW1Rf30F^>rn96KlRfKR#1}hg3^9r*(EFm3C7D9y`c|c5`Fe&2nimwU%oF@LE2usI~MjRDX}vG3H6lw83z6qhQNIFpW)K11sJwz3)QxzB@ig=v3qM?&I6vHD%xYeN%$Y4@}k%upp~L6+$LWi)}na(C=W=!;MaAl5%c*`^=pmF76m^BrSciaFZIoviD769v~~$*+UJ{>@=HO(01_9dyrtF^ABU_Y2*kSQj6-Ay*Elq6m~_Jv?ol+2M+T<%}Ca6J*&2WJBU92ld?cM0fMWjj#Y+1E6_!$LjS^dWu}MA;@NTvJC;R&#b^*gxIYei4>$-mZmKIgYX)L`ZE+5rf)1Vcgr>~IJwmc5A=*L<e=yCFn5-d;#FHwOtrjLN7TOm7vb6zz{$+|gWQ#-i$zqE4Roo7X@S<~6=4Vu&09sf}O}i4)o8Fg~QMVI2#a%hlT*e@oq&8B(j^1Uk9I81kHN9icvMA-5Iwo6yaG1)DJp$kidumpo@40V=$_{}UJ<Nt4YbMn0O5C(oQTd=<dBH)d+To$R=21F2Ox8ChqI2SVSF4hE(O)o0M8|VjyMgmC{@o8Jo;n8etBt#Dv+UZPsR~~1BPhN<59T47gj?v$k6;wTocntapUQP%nA&#$U(8Cwqo*VVPmm9_jFtihq?xqD7EKDp1%d~fskfqH^ya!4<}9#3?d%avQ)!Crp<3&ChIjXjcE82;^{uFm0^k_Z2UZ0X(%Tn=^p9SNPXEG-(12xFeXmR!YH*cXy++-15Gd{5I%9VIERf;NB}TMt+UGqs;RA)(Rxlomd51xy3Rt$nA4^q3c%WryF#JV8KZ+hz1GjDuUSkTiN8QDrsWrd+3e$T~8)XZq+`w^BGDTF_0cvq;B_>>SHcHxG;bnJtjhuAxuM9;qR~?#@;n_|S9NM#d>&FY8xB3e3yiB|iLi8CzkBo#lNH0~8UU~wg$MtT+=`|In*H@gLCr(eGf8q4vh|_B>KzhmH%DoVz7v3GA7peM4gkGY>8jdDZ9-)un=jN!qV354r5RVtqn^oA2FuX_%9*U2*p?3{&cTM_Xd3$zW%n^5r%Q*82w_Cp$Ye!d{c7)g^!`H38IrzHY_?W&}Ks&uuiRp%pG+RrQI6dDA(X=toG<iGfcePc9DY<DkG>U_@Gu7yJlnCPjZTev2TFHG-^#&R1Y0Rhn^-WN7t7W?<E=HAIC-o)$0#%#xqB}R&U<ze7b*8=qWT~HIDl^x|0n$rB71_D&(gZo^Ax(CsyVQOYbeDeVJ@|f)dX;z8_j??M35Be#jcG2SI+}j>v0YWi@0~OCrBQNsO_%7}dCl}=67Qk8<@KG_lvnob1aU9hw2t_?#Il8Df&p<^sq;y|xs~fTYQ&<nky`s|>$TZDmyvsXuye4VW>TS?+jQTp%I~pcL!ouUFTeE#)+gV+*jt@O1IZR1d^Nkkd10v@X{jDHrFl<abUfOqw<_bzu4|fI)Ku}Wyskv4g)LJc?niL_22SbJqSOiFEN8n<ntqUFU|XJgY1g(7Vim1iT7#cfSyOImli$OabTmFUjKe8bpQx4@_CNOxy2h)gE^s)zz|n?m7>((-(?}iE;Ys5#WlmA9=&O1mPm~t3>o;AzfWDS1HvyLMFjC;4#5IfId+xt+FLWpe6guT^xw618rAq6a8!b+e)&r?b+t!AyIwq@p*54ty!rG&jPI+nGgwI;k`c+Q4bBSyf`g7BvyNT?JCFAvVg5Rr&uH9N@J2I-BfW&1zzM#XMLUtkjKWn{PQ4Jon(OQrMTbJ8Yjm)*RTN~6r!)MxO`_ORqZ;${j@;Ef_SP19ar<VzPYu87{;p*#`cYQl}<4uiUsxz2EwHWtt{OHEeJ$!*GjNWwQ9J;ag1^ELPnxnK(jTfDm1=2R2Cr#{~&=rk7g2LmEDE);menC5>^z2UQk;dCw<jc(~YLLIejJ%VD`W_C3sF##u@2tPJ*XBpC13n`5x~U9zC?xH*CwZ_Y(Mp?omZb$m8@O*lP`F3`_JBvqtO<T+g`{rkVOR&EBw3FtPM!Q<iAwNy!VPFwhLpLS`oIp9>gk!;F&=azZbv{{VrOW;zz#s#qgac|P<iBkC|7RyS)`j7*$<pZ_sq70Hg)O13u)J~Os5ilpj?l!j!rqt4zZKbxyQmPU|s`ALGGQHCk-bNevToTi=QEhyVk?Chnsau!x~jx=@K3+1M*JYMVG3T5^4dk5W<#&E<*TzfNHI=GA3mI%!#9y7HlnG!|r<H)e@>q-Yo$&A*dLWdS@8CGCgRgO|PXA7o)Ki=qD27aYXfBeKpxM6A?pgUt;oFPYqtL2Kt<=FQHC?l69!oTT7Tw0+TbZ%xG`BwJ2Hy4cjLf08x^3K*-8^HcKS^%(o|13GLusiC(j%0J~Rrlqv|y6Jb<_yHmd9u97>Of8Ca-FMP=ahcBO=X1+UsWpSkeUlyg$(Q!vHxJ8Nt#ZySVmmRuOtnKcUwF`!a^IhToYeVN4HZXy)fD$^4AU61Y)`l@iE;5tQz|2dCVcJzmJA6w8W+9(=<;rB(bwO>Q$kMD)RtQ8{M=T$4ZTHq!bxL1b5tzU%Q<YzP-i`8g4g}X>eQ*5gp8IrVTjoDcKk|DnY^pKAHxzll%7Vl9{R>yQb;@hrgn?Z+&KaC|PWcWN!7D%lRf$f9HwvJOc*80S{e@pw8gL5dp~6e+u$lj>m1iXVvf8dFgaoQwq_xD?bsUq-mufLq66&fG??X-xdqe2*1~G}~0)ZTWnQ_;I@lf7&Jw!^l>Fne}AGt`z*>V)>x@V@Li!Wl!vi&JRP$2jG_+GPCuZDW#Bi=85uUE2uq9GPU(3-t5PS;b9`1)^E9tgIr%XI~=z?<>AhtZ|oP!MX5jT#^IT^B#&XW7N{<MFi%)p9+%*VBEUE>v;`_`)Wz^<%X5i|<umpDIGK;a*f9J)KfbH|l+#&U|@F3Q6N=9FHFiOk^&-Y~I$}OpD(tcv6q-t_^^SqATzD{2zadJmQF{*6(T8u61xj9F_O`S1PCjMp|Me^s~MH{1NAPaKw8b(a9)ZZ+O6LI5{ws!vQ70J^Lc4oF4)IDsLHHp+3#xQ~-d%n;ve@>S!WN6^Ydj$7x>qz1%aHH8l5F=ZCV`J(MG(1UANSPn1>JPCpyT%U)vd->`J~X64_oup*a7`&WTo2nZR%uJQVkYrlcB3`-;}uJRk~OMO{xOD^}upZ(DJflUKM{@&0F!$nz~uk@=eKf2L6A5>Y*MBMd!Jr@7X;v`WQ5~j)-qE9YwSUq~=5t}HgZ|KyD@-qc)k|9wSOq2aw)Mv4z+49R`Dv$wh#NIkCJJy`vAjX-ZN{9WJf0L{ie&BiHH7vXA_{KLJns3k%xAQdoq$B$Yw%mFFDlcycvG*0SW^52pXwdk3gHD{6^U50zy*G6NywM_y0>9vnUK<=cAN!8>L9w3U8{!qcGq695@^-fDwoG=%{z_sMX^He#`S)WsSJuD!qUK8Z#`k6AWig<f(!Jl2YFK{BLKtEj>(^vLrG(aa*I{$RY*<}qymv)WoieC5U><rY>aa(`SCXQKr)U|Wre$zOu_(FkBX+3BK}#MaR8Ff_2Xpv*M{fsahbtifyKr2on=UbLBDyx=yNUj$KCa4mU*YX?MiStujNZqSqgi?RATMlQG^r(=Q!kC9dsF6NdJ3=?B_nX3bypFA1zMGNM+mz+Pf)4J-AI0CaYHOH<rfAfwNGZT$>w=~Gd$%xi%t2t*mSran`)nSicM@Fy(~Np=i%uhHgS7$5uQrW=FDG)r|m2}4f17+l^(~y<b^i95t~-a*tDs!Nq(<mVDjvCJRO)$GKNd`i6jk_Ef}`ZE4_vY;~JiDDO#cEDg9B#7XlL(<X#nPhNsNexAjxj3@8}Lo0?-h8=hvdso$NOFP+Zlbe)I)6-(ObJSq{|<85vG8Uj=I7v3T;eP;WJvNz}>qEbUUixQIVHVjyD@Y--Q*LXu&lA9B0RnsygWipnuT~sR-2#qe>8PKMpLD?TH;pS0HG<BVTYC%nQPrBxwoDAdbme=pY1MF52V(vgM3Wr`n-Zw$BDvTmuX%l`1=01Lic;&XYPZ^vsFozJnEQdYT^AVAz>}y!>Fu<W7|5Z~gmfOdUkJ+n)is)1nF7KsnK`o%vHwJ?#1L^s&iw2CFU5dqh`-fk;SwoLxwqL8lK)G(d%IbpJgsO8omvYZH(A>+SI5{z_fp8cEp)v#rOUp>Ktsb#G)}6o8s!kCfp8x;P-kbE=wx!uYvs}gAYZqsq;+|JW@iH?USwuR(0;Kl?=<@?WK!XOQ5Vo8)vJ;$6Oo9z^U<HX}By5aL%MuMLH!K?=*&rbSLfCFta=Jin06iLjV2&}qxr$w!;@<o2d698KH_kg}@3q%nYpyxJ`4!_EgOm~YE_O&@iLw&{J_52eXwwgU^}5Hzmqj4uIk1Q&O$O%cfZT|2$`_7NhK`@H4$fk(XvI=h?y`LyyF6x@$Qm;7V4a+2P4ZQe0ZYy2H|r1t_3K=17?1VHP_@ycWje-?s)lJUTR(~&=Eoq*{xiErF@Gf&rpw^*VHR2N6XQolzA0l>3F9$Ux`J6%jbyCnjLul$I7I3Zwy0<Nx+xx<MhUmup1h?nQyV~>kD)trwk71=qRcqHWfz~uF|7ITQ2WTHwvRd=qJ39n?YAC7#;!2-HO(hUZM&I<^dyQ`L|F#}pZx0gy^V`k?CCv!-k|n})w4&pS|{X;N^du2DJnT4K}=q9Wudzn%@alz2~ltmaHo#^^U4XELU6cEViY7ds0&uBT_Qvp%DorDdjN+Ae02OtVDCW$K*g;ez;<=l0)5sIrP)`<v$%u}y-Ttf#_r0dmC2_W2O%yPjWjnR;N+Yp??)tA5tR|0dRb6LJdjeO+S!F2{P)~*1I*8ywBEF~+XF?~iRBv6FOdtfNrLgY5@?ho4~@-Qc2iJAke+N0J!Mo1`T@2xbIqX9saWTgr3TbE=2?p=mi7QA1wRufS9dG20791G?jy?&bJ43=$vO<Snsfs>$<PjIot%jKz2EJ_t!PE8ohFd*2l>6wS#l~Pj&tNBtEx?PX5;JVKXcOKe^NF5R{02VP^;uK&&-$$SJ`RY(1FPciyC`7rZn*tUf2={6>h0rpUOlG*L${ZCEF+VzwUmFL|p!Ps;Az2o1i!71w53UYeV0`rF@Un_uZ8}y~G|*K>Kgda+`@B#!S5ds*L+T`5BlKEq8VhIw4p)8dLV=hRFWFjK*i2e{g8aXScY99F@j2!$tf{6zKM&6h37F8_<;G0St@e{7eM$Ca2ceFGXO>7k_q^A?#7A3m>C@nnV`-b6aau#X^3`-m5aI7BD!l=Aa70v?rEIR&5k7?zy)b4#cTJj_BuPLa20j<a&yj6uUp}ddD<rF!LC+zX-ehf4jFx+}xx1V*W78!S5w^!)S7hj4;&{A_>igFt>YN21i^VO71@rC7lV8)Ye==gG(74=Gi70wa3#pS?!wVqa<A6#xK%0;jt)56Lu^7PJcdeGqB28EPRQcl&tCJ$(nk6fV+=4C_Fh$6M|`fBXe+VIhqCr;$aLd_J|iu&<y`PDwDs+ZmBSdoDTD9WN_<_ll{)cPgrS6Br(enp0-ZT?ALqQeC~B>=`D|WjR15dJk~0dQSWJW2LKMi3qpnu0pkU~1d6)ZVV+Xt942X?IIVcL)C5poX|FI7w~Efo0Tl^95DCB82JFTGL2VY#5?d~i|Gn`WI;@T2kqv8P+yh$CBxhpj1!gE4TnB_jIq;KOQQAXA7L)y|Jn?I5yT&?b{K&)5KiPcTATS=o>9T=5Vm<=J6uV>d5!*|)qvlr1QxCKnbWJ)5fS$D)jbHUkt8toGshW#ttcH4NiIBw(;>~2FW0OG?SIcY#o~<Z`jN|I5Cd14DkbZ>r!9h^#JhC1{#l*)A2lIP_uqp&W_^@uULC<Ul_7l^~jq}PRju9=I4=Njo3lnFavcG}YC@$+%v%mgHW@Xa8D`(yt;T~x;E?JhIH<B#XLg*m+9n0ulwHAT;4`pBS|2Rbl51N=kCgz5H?$u{*@>uW^&cFdPl0Cf`XWG_$?0L<k3}Fm8T0jdM)DzeM3SZY~mCBn*^bet@7>4M#5l|g8Lu8{Wfj#2!E3%ZQwM-Hq^oTMB;#Qbj*^P!ND0@;oSns(}ZaM3R&fj6W;Cmw}bN7w;R+|oOVu=y?$K(=F`%vdCR|(=ZU~-A@A|Gh67RB{sV>E7Yg|;f@DjcYWdy8WIr)0az426p)y5<JQ%`SYF*fLg@$QF08Mka_L*;JVwXCwkyA>%o&tZb8R%I}o{WT9PC&-S(ECHA%OS6-DDUzHbMRqI~=d>!G}5q?!(d{th2r$581?Bc8J;;Zc9tL)-C&D&Sy#aHFUmr-8)#>*}?_4SpTi!V;UH14>o<5YIhFJu?13ga*p{;g6Tl6cEJvq!*HA>SfuXRmIKE*PGnW7k+Pe%J|GCtbbl1;`WFZWLl<-enTTGvz|oLgy-sz8*h{@QtsGAM`WHJ(R94D=d0{EP{A+w&RnB#mSMV9VX2}KNFQ)e6T*X`HdWlJNns2s^XvsN2#9Z(EaH_yos`}5R8I0Ono>D!NS>Ry@q-*EXl5RJ|KS7#T>;K^~wX69WGur{}EW(rYgO*xZ3$E##Ssn%jLbyrx2RN{Nh=JX`I6&&(6EE2UJxO-9ohnCZx9zUkuDPN`@wlZDZEuVE-n~wwWBG_me8yLZ<Gl&fF*j7|tsN&XpRcU%Hc5E(<gsz2%#WN1o9pd{}vLCM|iQycoQ{sH^vooaAGQiSPYg+P`Dr#-po!T!Sz?bhAhAUKH>PqXgh$BF$%%4@Y8w3;n-GUwqb;pFQA-&-eIK@%YaRr#)7(Jd(5=&tvB6oUo!_46IOki!nJJC10fzkL4;W>dRgHS^q8a>wn-$4LrvJimthb@?XO~KePs4QMs`5?aH@V>V`n4<Upb=TKhJlz7n&`Em#V-DjKFy3eo3`GD+8?Mq5smA^gBI%uh&Rq%M%WH&e*4oEiOkC?ln|3MF=qN0LD&pedhPhT!{4=mkJ0R{04zMx8SmSFqk1%IoC<sD6Pu4L=CkMXJm}^{~9Y#pOZl4le@l6_c)++K{AnWoIcU_uIxxSg{O3M-J~#0Fw*tA9)M-SCgzm6}6caWo`UOegwF_=U|lc-%+a(kAEQLBx_*<iKo>%36U&<uGlVaDh}zIZT3Wfsrpt1*&w2=@#%E6jcvou=rY26G%sySOc)wM2Yh=&9->XC*h$UlAsC+&p+*wc4wAtladP0*qGsBWp*@Kk!rn~;S;eHLZSsS6U>C?lae1&{hW0>+0Lc#l9V=gRjb*R~a@NPqw7h&UNroFb3x4B<j*!3q{_87vMk{#wOyuDc3!dVbK40^6{(Y4__fIN&V(f>LnrE8TJX^lC?iSU~Erxk4bspC_JNet;a-DN`Qsnfm+g&Vd9(67B5x68@cUS@YRo-M^{u1TQ-|7A=HumNRz>olZ_ohy+H!i;6E8|-~a04i$(V$rVjBgx%5vjDj&WP>J_)2K&>p;1`8DBYm{kE)}gK>$#I{f+9n(J%L^|fC0`seEizmD+h2)`Cw-{H^j79W4DxxUt1Uu&*EC3V5qg6nI+^|j#o-V3hrc?DO$thrKANj2A4g?*8dbIqDPy-wZ3)Hh&~t7EU`b|BI{jHN#3$C8ydhKgjbQ}l0MDx1o#QFR(+)yE=hn96%&flx0lYP2Gv%_H@IOCR&(tK-_+qyJ11R5qkLskt6qJS6AqRn_vXUYS!ujJI}Fy!6XEQsoj~>Sso5ELZPW^RlJAI6t6PvfXTCkojC4*Qd|aR_o<iZTO_TI(@v>L??DiPx8*}#<DudEjnw>IW42kDw>N5G5P%K@3WtaI_q?6VNpPh%X(@!^XKtTKh|k{^hVe=s&a-+M;2Kwa2ggL+`P)=YyI+Uk?E*_dbYNQ%J=%DRvJ%U8R{?T_?K9(<m{i*Fa8<7oGGS;MKSfLp!M**pQ&huN51;eYjfejO6u%gGejr9<DA)@-suB1zcU9M7nRTdGOycBwblB%o7MIpTB~0=n+bZ><Ikgie)bjqu`4-KK&{traD?ft@aVliFdApa@XRmqNtZgtSyRQdcW1}p^!M@4Inl_BY{U6E;fJ^~jxzPC)P2ky^J{7-F9xawx4@z!log1tDCD)JfbiH#p4>@CXeS1o%N?OBzsiqwgbpT*da)z41IOqpT2tuxj!>3V+hn{DpkO1b!`pO(rcv(!)k~3Gt?}aH?VzN1E|14aG<wAaw@$Nm&``xwMN2#Nf(A+`;&xW1kZQZZtRs}|pdFxPwHNeJo~=n>shsl=r!LTVvA^7U%4;hgl*OQ2=?&rb!CF9vKZ<g7^20Ac5CZqT7c*^@A(tR_ndzUVH*XxsrA@OA|33PhVx<|CbTDc7iM!?viMv<wCEEZ2WEWRuP)V2mGf?vJpH}=rLy5D7ybq(x9;!D2HYTo&PumKC%A`n&l^K>k$7ZNhKdeK4>EgZ|xf2mgS-u$6n_zq)Q5^D=ycSR7x1>liq7kpH)-NV@{X^lOh^&ZOyc^#VGj}HAlc+X=nB6m4j|b|nZ_#&dLiJ7M*)ndQL?>=M;5w#^p}6OkHtgLReebFHf81LbtdD@{u$c<!h$k4V&h>F=uo``ka?lHdHQKD1!Rn>JeA!^Fz1rL#GFThyvF<JzEcCbsF~Xo%_pHInz^br+oxDBSy4WuotRrH;(OPvT&O49~QbZp^d`k1Wh$lg%KUph~jV-NJGIFdAC#NKxGb(NUvNE_2j&J66s;8ZD&#_aRYNx7NUH=dXhS@1IQoWVZ3Ap`G7V2NHSzj*d=bt7GxksD*8BvfjB?iJaRwfV{TMEr?DR3@5!g9ug!Dj}D2#^nEXLRRfHm!(K$q5t|fzTzIJjz4tBuO69s0CgQ7`R<R8iUdxVp8b9!Ef?N9in_PpN2$KPI<Q@Rb-hpfND@^03f7B6b3-zG&?e2kPOQA;kE%1Bh0BVX0+GEd|sF5_A%zgC;!UZ59eJS#ZM{h_>_^`QhzFfS*pb9SA?oA#xL67bvtp{%m$ALqH@}fTrhMxuueOulVYjlDmXQ4LX`>O@C1D1;-HewD3PXGjAk97Q-i1>^btxcuSvh(N-A=|7+>$u+uu+V&yU&UgaJNqfXkn^_b=#H%8WehSuRM5I(e3tNs7wsY`iFSWv&l65=5zQ?PB`sV&=0hW}qNvlr&2a9Vfg@pwEoE^KIPCR1J8ton`Y><|1#ZWkhbZTv(CXGv<0SqqbY{k$6c67!yg9PVUSN6)m;%_1;Gx)CglIVv>%F+zB4|RAQ1ex}@}{+DZ1)n4nrd>)}ED&-R1{R?21{%<}hp{{a}k&aNae>^!uLDqH(c&Kin!4W+kUL$i?WE!R+nX>RN45h4|M#UnDX2O>CIRknIst{#zu#qk?!1ow<Zb0&x*Wm@(7;uGX@o0pc$UHz+1iss5?e3tGQ%?-(a{(XcQopfpT@<c(ad*{O&>*rza3cP;dTjFu`{u8GAhhW+`P?~`tRT$Y*CBG>BhBu6`LOUsal|kQ9+FT5w<%!;<aDAZYN4W|IxcJUuG*87Jrps@PXSHMIT5=BP=n~Aiw($hYIz#n)4WXZ{q*_Q;#>_RtxY_>{xQUywyqB4F&q^P6ra{zpVg*j5io(Cht)Nr-a{Xea>hWCCb4=BH%_Tizq?WlP1<cRmB-D~7-S%1Y#4r<mfKN3~4AVBFZHkscykwY~3wwG)q2F;&PbYhNGU26XNKN!J3sokp!1<Dz7*1@HHIgmWCYqO3oA{UAKNHh7raq=Gu%J=*_ykg8kbJu*p#D4J*-c-T*KaG`I{Dkf9<88_?1%?<>QE-l4VyGrEj*N;6sX&)<{WtN9rYL}FSDYyTyrp0VkyiGq?3cro41dv_IM*9x?2VV{5W5MjBazMMoxaC2fM320$FGMLS40i^snV<-LQsM;wWE*D3Gf<kZL|ev!Az8>QVU=7=BNYNDWJKgMN%=4-Uf)TX}45#p`aBqUQHLgD3Kq;vE@5WTZYNbUydBcY(r*aX)KW2vo3x$QbDG%fAwj_9zUa(Waal`l9Vb5(#_08udSoDpL0ZHph12iNw8Dp2%_+xspT@NkfvzMvgCf4f;$L<guU*OW^u}1<8co+f-#_P#SNzH}CD0+0XGGh}-%#bz-Sd3h!*aI6h3rTfz_|`mG!Oz}G(54V7~*k9T}zydN3t!1ZxD*wpY2o59g*tmRvbG@5QWJU&*Me2hvTTADI(jH0h2hr?ih)~fbgX_te|lI{J)@jeDll*ik1h#**4hUok5|NOc%xChaTp4Z^sX7;0J$rXcV@*x54vQqmK_3ggWbtlXER@s88!QGDn+$M@lRddrOr3^PYd>b!$rQl44JC8ElN{J+E&4T7bk{THCCA6ms0+|7TpVKl#5Lf=VOsL20M8(X_ep2Q3b5(8=OVjoV!Q8&?j+&ZeTE_;NLro?o^1hokH#Q;mf5E*BjU)@8@?cWkt(-YPQr1+}8Mi>_lGiOTV<)@31$GjW3_-+*z6wK8C0?Fte$lNl{?#(0JLzVW>-|V{<Cywz*y+6AAh~8gn>Hn>!CxhTY3N9lKT%kM2aQ~zJ<Pz~L@vO9=%fr7r*@KJ9wp`RgpuM7O#@!o9%5~jA6?hdN3;eoHVoo{NP-?N85_1d7%$~1L*yt?-mo0Gm0W4AlNyT6VQ5ec3Er}qNxJYR?n~nEQQpDmKs~iYc>vW;Is-O2HU29>#7sNN+bIUiyo6A-DZDPA;rbKRtEL$9k4AHl#AQwqMJ*<sCrR|dTJq7&)~P?(aTB*Jj|(O@;i_I=@U@pW_*!cWI#P0mEQG6!6s_Zb3~&>}+EEN7$hqYSGYNE4(uGwK5303F;X70Q6|0KZlK;9{%pM-hvn^&>%-ahVbI<0%Ba11y_z2}_QNT_{Q{wQ{jW?s&L~4}NXs-BORBT8}wwD*PSxhK9m<NS~GS#Ka(qv;W>GHQ+*4^AtcG%onCPO+??7)-VCo`0t3UyQfZIWf5ql6t9kx*k6Ct1NzYHA1lWT-Kj#eQxUW7STj8u2=_QB+tYDVn5_rh`Itab^$$8)0P-%kiyZotR}1d*XCp_J|0Z5fHCk*a9kmYgn+rrc>VGu&cboVCSdQ%I*W&yRZHs|77)YlxT|)>}u|U0<SQ6ZFwbvs~4|(G@nw-0{ymZ9TonA>KT}roxvfEUIS#_S#UpUcSYOvu+wm|)TEP{P7#b07o-gFKdhax)mNY^yr;CAgmY7cD0S3*%^c%KbBT@0^z#YXq?$Lf_WBfIGs<j8ql8Ay9HSr=*(AW5o8*M(ax|P-d@<6RnO*C|i^BOX(b6Q*A9Y{5_$dGfA)6?w^dRa_KkDDk|BPu)LV#uIOrwMITDhQlhKlU;1{;-}gCFg?RDQ}#3=-C<&u%Wq!(Vd6^W{)=*V7#FW5`GY{qWDex=+mg;NO*$+c~i1gf}80lJ(@eu4;XjGPDl)5dD!1&?Nn1*O>@Y(2e^TC$%7(ipEh?Wudq+>mE(c!<2)LRf^^SCKHw#C5lWO*2ZBW(j<MNIGBD4|DmZ}^?=&3Kl?fOQBycpCEGasC+^?(`FD_xpyfJXxEX?J(rYp4TGFSfxYgsc6?qfg7^K$}N3nwG#$7D3g&&b0w;ycHi7nja|0_ZcLNo~+!X?Nb03nnPE1nTNy~A?g3If`+94R#l?m2CXC$mOWRD4EiDZ4o*k#On60GHcYDH^91n5lsx0&lhnA5URM>SQ0h1Hy%$ZJ@d+{BxUForGh~$lU0qs8-IzDvWg(z5|O7AZ|{Ps2_<&I<Koe$h)wQcX*}vS90(p_SZd)ijS2ch%a_2cP`22(JLFHE7G1p>AD!!rm>SNa<$<g=U}+X=C8S@t8Qanq~XXkV}&IMbZn5<Yr3cy(Q5AC4G6Z!lgEI7bF(i=Dtt^gHZqh-ugJC<AQ>hP%Nr+Q6&XzICj5$YaPU>_TWik@8IuO_o(mPZpg{AQ>bgpbm8-=R$-rb2PayV&DURkEGk%{=m8w)&94(*;Je!py!-$_-+nE5HWK+!;buxKJ=k(QLj^92zt;Ih)ppr^O)+C_@)#(aNqt0e4itXAeILpEW=c3nILFl^Xz$AW}$)RbhP)ys^^F#x9jRrBA9-HkG@``k+zACnr2{Zss7Vpd0{*8AE_8)Lv;k{PZwWUz3yoDZ_mn}bnIdT;5%WrKk?GW$FZ!J#<Hfa{`C%lM(HW5Ag7^w#Pk+Lc*Pj#(ABXb*+#Y)nEb5(e`3smtmAGVPL%Ux_!g*mM3BK_Q^N@)@8$j8afoVp=)g1S{VR_+H?p)N=I)up{Pd*L<Ti+|cNF*3+TBS9bHY97v`klX-TC2@|ho#~P`+|ViWqT+Nho|gl8>=;PVsLnQFCn4AN;k?)MZ@C|HTijq<Y?J9+z!0xIaBBl2?wp#>ijU!jl^<5r)Jk9;Dt8S5JNlA6&2PSuUnXnMSyNtwt%UyuFrJg(qRg&ST#@&zXxZ9R%N1TPXHL)xlhtDmfzR!}>`jf!1D*lH%ydw~I(gM2l6E~wd+}n5WBPIV)Lmrfl+DMo1(cZ{wx&yp4U^6kYGOCi4dtE^z|_;Kt$@yJM*%eKYGqM$?3@}qIAr!vRVy){lO$S8wPb&w2q@-sxp<efM@N%M(KT2n&Xp28xL>5x{tq)8Tc#;KIfXh^t1+UT0<mGmYV5e{<%QL-4G{rvRP}rcc=18qN9dT+*Jm3Bq+34*zf7^P`iL{cnWFNFAstAR_|}f|rDiO&JFFNgu7Wp>GReD3kQLlPFi9PKu2HTX31H&Jnd1o(u_hYLX;PHK+OEnbM_BZIbS=&gWyMYul=bS9Hfk#Fb=>PV^!|B;g4oo!m_M7D?a=qac9iSi;MP{Yibmq582obG?s&Fj!H$#oUS}jy7)f3polt5uC$=UuE3bvvfewgvwo(c88SBDV{L2xWP@1y|)!nKDmWiJ8ZVa)iWJ-FW6rumq(?0n5*-fzSfNkCTD14r-9!%S;msxJYqSqG^-F&d{L>uPERt$@JPaIxfC+wK(29K+y^Sn74oUq*cFs-^0LC+K2Jd&9@H5tn1D-V{55SA+{=G#)-iT-c0*qrX3?Q}YAC&E-_KXqmZ38Spy1+Mi>&#aiCNtx5e2~S?8i9J|9&sUf8tt6ibdB-dtXI&-&Jen*^)Pk=|9|@Xt$@VgA@nvW1X`_XvqEp^&Xv?y}7Y^kM{^@7Pwtft?&i)>ojx0;Ou0d0@35p`<O?hY_h0-n!N9mSE%3&ACcjYZ>ODwkFp3XvlW5&6s*)Pj?7ZLT8z+t#CPBe(CuBAd94lsxWDs1pYH-xlf^WT8XZQzPUNOctwJ2~wwB=ax@K)ILQ?#gLjNE@h4HiT+7%rrDm?o;>Ta(VoH_blb<J%3O9Ju{KiGmEr!W2!YoHzkiafsmMQETG6;=&nJ4#uddG)|wD*qNb99vyMRu#+XrzG(H=y1XXkzZfz-8fliqw5WeYb>RL)NTsT`|vM1IY&5<neoE&n+Gw;WIlaZs<Ai}G3RJ%2*2ad{etRYV_?|sS#jR^}z85Gj4{z8=ztwEEU{#i-gjq=i|x;a^FnZYumI5^a}LmqIIe`Z0lDmvHT!jcVRq+<fzt_EEEWy+ZFf~Ppha!H9yc9X7iobo=C_A|2S6}mLVJN7L#nWc0-Kdup;eY=Fi<+7{cWY0@twm$yyf9pnR!bkj+nUgZW0li?`k3E#gECPI!Mw4simCWNBb4He)2+KK>4?+iIr*+PJ^Bl<C(W0W6i8P^jZrPIYC>2j)f-vNXflO~v4C;EFuR!iB7bEHwW)!d{L|BRlr3Dm1jmHg>uq)arxDt&d>;0Ibgd>^Gc@R)qL}mn0MdW_N^JltFw>-&|UvIS#p;S7$59_)6Fhc_Rmqr5mKji-SWE0by;uuw%_%UZwv5m!0e%GgOb7-U-&M2&0<Tg2U<@Ff&K|Xp8#mwimX^48NIA+C*&`wSqVM`TfWf>fy^})Sy;Y|m5QEZ#!FU?AJSB>8$C2(SLP2P2GL)e3Q#b7To3V@_IaFPWr&-o4QML7WfZNVUkzN-{S0gj6iO0P`JTei=%vM&sN8<cjC1~X!Wg!b>)TU($&iOm7ua;>iz+`j4+r#&=Nm50jFn#a{tkQ0k?NwG=!(+z{8Fn0Lte|Xm{M$3N<_V(ycLlS_UI@RFTSm$U_;LfR)pOO|iK#eFBu&Z<kb)9nu3)Dzw@<Pa>&<!fR=|R<^o0U?c9#=C!DjM+xtC2h9EZ9)5TwTLr@l=DO>~IOyHtH1L)UYDsv)*C~<7Sv8DeUKQxh;9X63KX=P~wich6NCT6bfZN9-Nu|7R<%CP#{?X9FxFFBq$zK==UXR2#S4rd3CrN9Nl2ePbMH?Mzegz@S$7bD_S?{E56L)|J7&r_;f%IEOrx756?D~W;IWd;aRMj5qM;zU1{1)Vsn`7BOWzJM52*VY*Yw~+AmAHj1IWh=PB!DI45fe;@&PE5bP!fU@}o^=2cwmr|qM}aKf9SB3kC=DkSFUdm3j%qQFl@ikmCKb9)}lu1q>9hq{g4g<I0-YA+CONnSnbt9w4)Wcsss;J2J>KYDOiKewfWarnYRz;mb%L79cl9>RHCQf3LDS3*Q+G2RV=W6M(t5u;S)m`wmIEiW6h_$Xi+xB@#<Z;1G!5@RD2n;wNmsH@;%Z3q!7&5F%>m}_uudlpE&v=)f1WQLT~0DZ^SE2WHF1?*UQQu$8!-@S5Sbi%Q^GN<RhJg&NL4+!|1Dh|Cyf)U|YxwhT3K7$dt%p$P#=ib66i{0q=GTU;)x=P~CwnCzo6=IUaGQ*#^qTs^NgspTHpc)s;5DZJJnq@Ti#b*G;GV7U)T9Dx>4{Tk2-C~Z`3Lc($Rw^ThEE8(2i=+~c7;=y0hoNg!_-2|Y8gsIEZAc`8u!yfvCb{S4xnax)06L3k3JqGPGq4JySczr44QFsmuuRlCVWmLP4fE7NSv}4a^b!O`F-R|1v>cM<S&=$t6G9|)Mwx(XJp9<~;KTKF;BRZS4St01`i!$+iEi-xZ-O=8cUN!+hhSi1WDS199)3CB7w^_`I#7c>p0l5=E$^~;5|;D@%ZVHmvny7YriT{hCX{tqX5G4MNG7gcy5h;Lm}W_1XJwW*jz)scon5-Mm9mY({&k!(y}l*NkQ!n>Mp}?EBRV>lUPaqD%9rThhA4boE}VGeXVxpIF(2weMTgDIuEMXran@<ZQe~z`T}<mWA5r>EOTuqm8wBwx%bTH~{ItqwgGqCjnzhf}sI0;)G!oQqptG1ig8#%sQNlLJ1Spf((eLR8q*@zQehKLm%$2QET0W?>J#cG6>i$sMN?3zt_JMEdS#_*mCnaR@K_yrc+e{gSdeWwWFx@M)!qa+o)cg8%s{9<3h}u&Pz-$wo7$i@3QQ*(URV)k7c1J5yJ~Hrjl&+#hE1Mp---wVX>9mfBb{4FQfz>Np63s^=iNdv&iSLE4!koaL!KsYy8zzzD^uV%Qsa(SZ1e-pv+y9FDGk*A?yTA9{0Xf_FQB3#f+rWB!gLQ-j#^f4vDI%8RuJs0&yi#3?_<!K}uaRKKz6ZxG9Xb{Qjql1vs60dc2}XTxH4S?*h6>y&#;e%`(rbaA{lE`y%Lfk_iEOD1yn+$xV1?Os<Rnlq@LN_l*2n;dDOmNU8&K#F#H;v+f=DRSsC-Cgv})`%xQ^BZJ2t+QVL<k7N_56Iq}Jyc2YHwW+iuwI6War3ggPBCXMgKOK-68LoWi@|sCT`kg}U?zh&o$k(<{B4&Vi`4Wg#vRf|^O=2SC)aZ&_h*6hT`JRw|`}QWjaigo$)au}eNvSFP~rz)82nPPf8N6GJk`POmC<Iy``#hIbpTXT3x13^hGZWpw9K8O=8!m687PlUy;Iq%(K=G^Pm)UwX=r$tajp?Q<jLIV`8<Y@UoVGO3&D|IMJ)<>TmA(~sSW|1L7hNwg`|wZ^<F`)xDNlUeA~c6hvPv<e31=9DL+@<(}GDK=xatf7d=*e*4u%1~ng^uC$(xD{h<sWO7ch2U@768$LRH9?kEot0hL2r#X(lHjeE7|CsC1$-pN)@Kr9tNCp57^|y{Hnhm8)V<VH`g3oWX@zG|%rE`<M1Q_Gb3HTUNZ<o?g||Y_?gGXz!I&huNfKKaoPmcuGiM%7A*0r$;t-Il#5lnYjS*YgIAH<g(vy~ob^eaH_*8TLQ7&3>v&;j7SI_Mv1z!mu1@*xz#3SO%ODNG1LEZ8si8YX|p#WT~EKM?!(sFGZ-HUvC#)7SqLK9mg;WSA11fytkwYx2a1E&lzT(E;e{ADI^*1bc;C<CNcUSHpMH5Ds{9}=k(JLD$Slpuc|+sp<Nc1VsbPt~j6!x3Hs7p=`S#=rNIvgHAjkuUFh-7+C}dDr7?f*U&D^^hZFhuHDPH{12l@9Y=5UbfaDFDFvWq~}_PCLEFWK6}?yQkS~-#fQ6x)YPehY_#pKn{9vawu5!7k*Zd`{<H0mt!CW*FjWt;9dI3=k;#wrC|@#}_xmT$_^P5(?qgS-<8+UxNUX~POa2Wpu_Y=FaOR^*k8kJ)4{r#pbk!{`Q~Q9y_}GDgF2Y5|NT|<t#ab<(a4K!ODYzg(hSj>u)Lt>B=ngFG)`Fixu`kP&T)ACTmWFU&dd%%6sC+~lWdO9HoP>S-jCX5duYNDC`HJ_(U2=SVPgmYHaYiw_@%VDf2bCCUcVoo`yg`btRXzGzO{7j(noJm1_{X1Afma`Y`T5a_XxlXdCNWi74=r}xj+w`@<~!iOV%PiB8)R_DfoGNj+Fr#>Y$G%3hrk*!9EV*A5wEb+?Jdk{#_)}aKOv6P0m1EyIl==B*S@AN8%&}rCiYscx-t?y(P7;VHtx^_RZqGNX4Bou4cj=}R1Q&QJn>9^^`U0&H(rfk>AM;;J^L8$W4f-{I$3abNUJqnZ*`e>a98J?cb_mJOx~_E+!4y4$INbQ#&8U?gQkMuZn3)?5g;}d@O9TrgAw^%;?qxSNZ;I!UuP3>Tkhh<4c6Fg7!_I68_uM7t5$WrUT)b&QHun7!7U<TL70ij2!o&2hPUW9HXjkVUN*_Yq+k|9Et?0-RK$qZWnOE}ia7tNr_Ryu6QlYO^EWr3{VB2GaO(ywQid;ObBk+{Jd_YWHg~q51Qgpl!GE|mEiAy;bo4FubpY@|tgLWPPp{#NS3+n-_9wCkMB*DHkjr4Q>`bIR4O-pM*sCbGtH6ZJP!4N{4*X4EKZrah<Q5xtMq%$&3q9KMm1E`E%1|MrmpkA5ENKLa*}G<y@Y-O$%#xRg8UK)H5Ild&2)$#M3y43QGTDmI(RD3>xqExAot!|AY(lfLDb<xl5;b^%{i|@{nxR|+g1nXN?goqfMlD0YB=F9XL7+GWwP<l`j>3kvOvHh>_^2eHAUu(KsI~&E;&Oq_9VYjk*qa>CFAc^V*sXh7LG&Wrl?{WnUfw<&$c9}P4QdYR84f%1T62(N0hg?4h!WD?oMP_4=>vze<=5?^&}Oh6dS$Rios?s;9-$ci&ew(XKHH>-ep3c}Xk6zkXr9)j7=V`z^FBox@3Bu&%|vNzRb2Kd(&cTcojFcQK>iVqS!<BYMYm$h(2kHc&r*lEXLO&UbrM-mx9nu7bffHU3t}oI7A~GiN92V|#_c~GH*~9w!Lx#@v^L`pKeaH@8&C`5EH7ag_|&tpmN@WX2ChI|zqPys5NS`yOT-t?OZ-9iV=%vEb#31pL0mkbJ>Vb<yrKEJ$CA6hmN|{a^Poj|15Vt$Hv;^qD)o(sYl_upmeqVD`YL5(9>S-CyB$IwX>kOiU^C~T^CbfOw8LPq_Jg3P#32%o?`SOc1V4PVa(Xtf&rEbeah3UgK`B*G>qypnuNKCR)GUr{s446_*HzRP!3VT%KyDzDAczHF!PKtj8HR-IdP}~VAYX@c$4v!P;Covu+xCtCyPYYCsJ&0~D8#CO@E2b-EnhV)U)Abf|9l<c*Aadl;a5$|xBoM|3R=DjTK>d~F21T+zN%Tis#*SYsaYc3^Gz4D^!4>Lv1&ShB4T+-$}%i;EUT>L&WL_QZNip>)QK3zTaQ@gpJ?@L+z2-nX<TCcl3ns5-ywCB+Ey^iA_JN!F?xN=SZJy_8#h;#l<s0!szECGc&bHN3t7zl)dNs_Sc+1H;NIeuBY{UZI{?^_;O5tSbUX8VS=>l-?nZpQ5npdaBeoMONEBU=2`71@f|~0?F8&OrBWjnrsj{N8x}sfSU+<bmMi)7Wi&p7NJJ`GWlb2DiJo-8m<6KhrUe7!^JN_1zI!y_?oeTFeeM{AcG^zuCJnVL)YmS9X?V5wGWIi(W<lbyT2;-NI4UCSxhAs&Y>uU*j60;)x%JjQSRpLUDdZWnRs3Le)B63t;^d~ZyRSMEBVAO9sE9!Vr@9{{uvb+3Nc<in7a)_fcp&C&i6jZz{O8LAidGu4`hO&5_DB26MmTviU!tzGyBwrrTEQaOi-AT<dxMO|GI0-h+<u1catkTUs6}&rts&gu%?t&QUq*m(d1{$rE`1m>c2hZ^IchfUJJG=6u!;Ws>&(tq%VJ?T|bfC_>vbdy^PVi-Kc&L(4%QD8F0-5z#z$g~rRt>_0zX9?*W3}!R3#Wu9fCY_k>^Ih@gs!9=;UGS?guLRgD>ovP@ye>=W7lD&y7@Iq9nDmuC%+nNr(KIOQEz(=+xlCQab_SFI~96Zf0pQ$R1Mm|I&DV5t~Js`qKTT&WipH4btjUzrqTj8St^9+XGpCm>Kr*6$=c`%Nkc1&OXB)Tm0LErmhT2)0R8B*gi|j@ERHCCsyQKZ4jVaEL*RC-Y*=I!NUFo+sQO^?BO{mjLRO3m;FOrO7p*?$l6BInycpA;e;e%M%`p#-)l_%5>j^_UZ%L!GBPj~wy9q~RH?!`RgAv>$65}>bU0}7fWgxYUwFa`ee88XVL^C2AXkr{u*aWnMOl{>`^hZs!HBoYYQ&0H}h)oTMJ$q|LVjA((r5O{A7#~=lvOaPu@wFr~?0Qx;_xSt~*GxQ9$$ZfQ=AT}GBDe<f6(&epVP2p|oHXs^K`iq%0y*enkGj2ZO+Z969T6%c3WBG?`VsG+KrP8bt1tsfnuD!&d}-%#+Q{aMWQnqSVg^E%@)htvwp^Why1g+nvLB^3bl}OC!E0`vkp{W&xd0U?b*9`%*9~U_mV^DgdBWM4s_ZozdIs_e68aFM(J8X|f?ifkMr06;e$Xko2QUOVtJI-N$}S=$6yWn<Z@^V)+8I8D5DQ;yYsZGW+}L-O!&W;$hyrM5tt2az8n#-IGz_3&$c)$CLyb0he89};R!!`5@&BRw4}AUwV@?vcM@x&*mdU=K`lh1T**Z*aze;6afTh}DjC-O-azN$3IYg3+!HSBBo6K9dE?IJ~GVPV|FE*3gtM(_rUev^6Y#-6^ai9y|QG5y1=WbWqnWFlmvUN;t%T3?-&O|e;5v!{`P9Kxxg22(KEeefKR2{0FK#C6eIsra@5U5M!o|J-#>S*_(7aut#VC@g#yTm^c9TTCY)QN%wWJ08kiAf!Cfh?%(qek^z9cc0m4~hwbaN;DSmD)W}QNpVkHG}5q)_RFLz<DYsLV4@g%)FPN_UGPNCbQhm`h3rKH}!l6PL`v#MU#INkgcbrPHkSSjNX<psm<TeTB<aZVn(ECSgnuR7HPoGHGgZFVPTBTiycq|J9U18pw*hc8zRwxquL@e?b6t-NYH{2%2@L^X4xHJl={?Z^Y?n${GA9x^}gbA|H9ksw+B+~o<5VU7ux1Ls|%^qwrT9ZXVc*&N|!4=klLqGDP3&KUD=ik+J<r0U2)fq29jl~N^IFy-p)5(^sLM_-cgma?A4+2xwOl@H!ho?_9KmpRKY9>P`6)md%Ccsap7U9uM}{75V=&b5aLBw<6h%WMBLOmR<2<!_Fqt=cP|Sn`m3*ymRCs2Yq9$E&({%t9pTpzeucEWLRwxSEk9kpnSVvKyrNoOQ7x~imfr@b7C)1beH7TjU-nB#OE8XMmDmEGN*32N`felD-J-9|YRJ(0aEe}Gj&zP*3I4eNmKknh_HXJ-&4vvj<r|wkCmct`FPs2X9{4jPcZ6G+qdx>=@fFY!{1JM>=9PgaR37I%8E?wQA-NOOj3GM&W^r*2Y~goJz?MMVM6}}h3<hGut}zcwc+312j7P}L?_Kv|cQhhd22mN;dhh%$!u&3r&>Y7I7gk_}%|Xr&SDQp$G@B&H*cPVK&)&-n-coOeaE}q|as1qm@k(ds#&qLLgiA%})NzjH`1uj!VwfhcR^18Y66Oe(Z~}6f7uC<gC>9`>aDs5D;Ewt4Pycxg07(njNO&&Z#Mh1K42H#E8eliLfO=S*e+e@Y;^P5?%fpxY$h+roE|)+qBktq$=h0ivyE%O06u5B;%5ZT8%7|_bb>T5V9Qt!e%O#x4S?op#?p>fR<71t0F5xjGOMEuYWqfgdz}auP^zGwU&v9Y8Yz?D<o6-rYC_MJc4D;e=iU$kn1H-u(+T{fB@^4#Jrt#r>Pt#F(fR*>E0wRwE#GsKRrT}XzPZKL|IXJG_H6C5x#oVG%*P6(S#Vzk9Rm50yDSl8J#Y{g6g&7?MK1E<iLzyza;PM1_dNfIiM1@W8Bh#XXmNhsjhpxaFmDcsXR`}4WSc$gM`S4%2Lh(y=$faES>|eRg^<3@Uw8W#a?~+fl)d%Za)oG%11bmsR7@G~Qu=yh&^g)eP&4-^=u+IPRlqW{^^@kpsn4zZU2GuQilUb!Nu*Agip(T<9WH4FZRL%^Hi7-`>1Xb3G&4aJKq;$%HyC!a_xGk-l9yRnZd3og<+qFHG*;AD_tjB`lW4AGR8+_@<?g#!ytcnwqP`-ZfaY$jv{8)6Kkho<<^yvWcUiY&h{jM$!6ci}8KTw8ZO|If~@M{br03u~rHxc5MLrw#ikREn<>OV6+b?#QGo95)Y)*be~TT^NX9A)Io$Z?=j+*jV+b5uoOQy#!qE%*$MX!H}cM}`K(;V68E@Ktmj2d)QD0(VNWBalW6q8|b3$%}e{I%rihMh>Hw3`_#0wwPdu8v`$QalzU!#HiKLkc(?DJtY+Op~yy#2NIGRx>|;leBFS346RrKf>?oLG+D1MMgwsKPGV^0VG3^PN@aM0DVpFCtYc>dcl`MsYRQT^VigTQzb7l42PT8CD6q$cPm>q*1qHLIE65sdL+UzV&_v}tP{ppi@EtFv5|WAsYFC#>nT=Ga*r%^nVV6|UFW(+Dtql#)#vjtpG$k<L@!Zdev@QkF)PQa$ryrKt++g~V8w_4zHlg5f7s)wL4qqeK`d)AwF!iG(tmh@+j%%v*>`@*Tm9|UDr1pdaI?)&clkyebiY$$zlxt-3LHycf&mn)GzyP)j@$0^h%JJX)y2w+?^j@Ekr-0BB>!8cNIU-LXdC!781<HmqrOd5J{Nt#Uxr>#{)s$Wp^j7ASNahr8l7{D)Q>tJ<<Ju9BKpVJVPLW6|pi>~Tqez%}35hKwBpU*AN@vU|43dL|_bF5;$~oqguw+iT*2yQ@6p_LZy3mdIA#Y#7I~sH^jVDIdbK+DoJ8nPaQjEin!`Jm@U@nqwE~!#pmcuUnr*984_L!0jnDK_d<2lTDLu}X_X}qS`K&#E%kjA12>ncfanDEA=6eAPs#v7W?Ajb`zGm69=G!cM{!toe>>2!f-&q9M{Ljp!xlk(L=#9OH{{gaZg^0d<z&^eVt!FM%a)(?`DB>9gBI7O*XfT_jdsq%RzfsMs$Ch%}JXiuo{unCPEqfp0`DW74L`KA2c3Uy|Xk8rVbCX5mYW~-Tws@97YnfXsR9r*oS%?x-T=y3ag{MlL<mw-@v`BgJ545+VF;IVeVCH9!q_{OPkDi{%jI8B@&P-Rqh;>PL-6%VE=9VE_99^jm8j^Kk)*ki-0wH=jy!;DJb6W=XC5)7SBqV$1!L69ULgfIZ1;v*P|FyWkg2{Wuj5U;!lGlEIj<3?C0Af=SpXt{{VFBMI%uDB3G*~_Zdu7{fx2d;o<=(YBSiizB_S_)yLr4R<_@&ERV&~mM_kI$s#DvPo?q2=ncsF$k<rEzkRXKqf*wbWpi)NLA*n|@R>f-5wM85ygk=`rWJ*8s;~cE%BnnAw3CMbzcelLeUja{|oAv|KF-!GZ~kcvD2hd}`vv6%N0tVM67IldF=YV#x$kXg)k9dnRFK#tGjrvef@wv$eVY?JW5lmy*BDO!C)Xmi%qshve_}$$GzyX@%2)x*++h&3br_<S$uEk0pP5+VS;F@;6?V{LK$a{$ABCz!z`N@PFmQSzb9H{nGO03+(p|^G2)5r!TWB`6XpFRiy$c?!6q@G^4DJ+EtBH?#TF3``e7~%9~b5s!bpviN0E;37Fu#q)4=0I4X;%w3to6$ZT<{wm4Qju@kAeGq(7gXoDs=#Sp<e?$!5F^{T9b>dhRNEh?l=?Bu~paNN0*T7P?PHURTi`^zp6rDjg$8qPHnxqNDZS1wsuM$PS*7+5x6oBqeyZM`E|Z1ih+kWVK=UvVO9T1B=9mKS>`s!cJKUnE0kc4Rf1R^y)D&iC{*QKAQD+dAgd2`f5i*=K^&p2Ah?7O%3?bt=tiHy0Diw9B3@1me|=!Fd#`!W_1Ek)bmb>8lV(JQV`T{C6q@l7ZE4A8Jq=ze_VqY@06;JpL0;rs8&S;}a8$sRWE~kes-6rYbhv1u=7D@3`ZP_7n?x<CN_Dly)j!BN7NA&3%J`|Fn$d6|Ge+pTaJw1O}$q79n2w@0SKe13~Wq5>GJcVshP-9W#7hJ6=YP<1K#|@p^Lyb8z5l@S2k3qrTU42;(A?ZxEZCS~4ctHMY(__M{QI0>h^ibm7_@;;?a9Z9dRT^m!MD9_@S?Oy!hQN?1sV$vUV|MAA5y`O~|M;0r1Lo`<y*mg96J!7=A$OHuDZAx}9iJBBj&NU4ijKEhB7AE!%&3r<LWLSP%cEnw)d7n6Minge2S=Xdb{x49xIH<c%b@v_VDR2!v`Bu|wcl69;B<6Wc>c>6q_=Z7#}8+83RKI==9x^;a^HJ&;$I3AH8)5R@XfpOVwE0tRu(6c?R<r3|X5=TDm>NnnlGNiR?Idlds<vHUR5PK*Y)7Tn)`9d6W9uSvlv|R+mVGM{HW=wkS(y>Ov84qEpT?41Kk(?4O>J$nij;_LT426B9u5(fzkIkp9cyGay8SJ`lC|lMy$TzQWowl#4?K-8(<zglhW4w)IF-Hq!nZgi(lyWP)#?@HtfG^wJRJk5Fe6_SOk9z;s2i+d4R!F9v?OSe-3!xCx#(J7i2$HGYjD}iL-J4`0Z4i>8N=P2ts(X0m9mgiAB?~chY^2D@tvAn~aM^^C1qF!;uqjDn&>X3j0fofvdzJ@0<!iZ5BLZq><y|F5CCf#=7Rx;0^7xC`;T11v2WxB>H6imz=v%QwyTm%g+iGLIJO}lke3H!f_gwR-R#p&#34zuM0ulqnyIr$)L-9FCPoIaXAvG8H&dJxzyQjGel=g;-LKo67*Y&o#J*E<!epKu^5$-JSNJq>Cse7-KfaoYP50}WEGt2jto`GG3*ZgcWS-f&@Y@+R8lWEcQ5Y#4^EO#8xH|p7O3+G9(r}Pe`l1B;>l-kOI9w_o;H0s7O)$yvJ5FYKE3_eI)BCQkUQ@MJ)q6|$UZUHw~C6(QpIaMg|WKB%(lL0)+epe3OB?^08OENNqzx&f8(HBgjuZkX?sPsMTnIEh4rC=#rVWHwhv7+G2KgZMzKKaWr-veSrPm}9wtCyZ1lk1y{6*Y09#ed8sO~GIDQugS7S>)f|Q^KOTx|pq)Dv<f9T76yB>YFN%k|XV^MBi9@RK~1>b$g`tNEKq#9%qVui`pYy70AVNm-M4{LnWC}?QyMqghi0S>h$sP!ejZ!EfauL0zoojsx;c9_QEI(00Ut+9MizM{^H=HwAjqT#0L`){Wo?`{7Y|XH$M}}5dSp@1Sg0Hm14W~0y(6qijOQ|L%pB1+!G%{4?D`krq7LSW#tJTvV<;M?(4i0I|aCIqVl+M&Gj6hhuusCiLnD8#qWLe8yeG|cn|0oZAK|J%4~ao9q?M`PqSXLDOQfja1XSJ-qGWqOkR(NU*=Iut_~)(WaBVx_RM(QKs&6g32(H0Q7j5Xk##KUv*tZcsPceX?i0Jt?EqB%2GHaDyJs}6?qga@DL95v=IYzh%}igGpC3ikwq1SeBNK%#u^vm2RJXcjcuky$XberH$Wv+gjb#T9G<h~b)=t$NVdA0b105t@MgmpNj2*FjkUG`ZCiQkONvbf^10<b=R0U7fnQRr1L71)OgN$*9**U*|Tg`42%0j8wB(hAh<zUr!GFaY7A8WyLi0{2IAY5PV_|AndDZw?O?aA3g)#D($KXE^nuej0ZMbfI=y4zav@5LbYU)kb6`0(kISvRhb^*G}wZ8Q-tux>PB-O!F>PTNJ+4Qbki3#=P`H34zPy3qqC(2(eA46<9iqBYN$E5ogrsl(1#Hz>2pSUh&kl63<=eW!3&SGyaDH%5*kDRw?sj=>{<5~&qp2Cndpv2NT313a8B8?H#M<OQfI>zs?c7oExnT;#vo{aHW!5`hFa9?EqUlhUAmo<2XMM$@Fca_iLT)qR8+(cHppr5ynVbls6SU@#SpNU7{WEENXJ5vlwISm3p!VXZxZ1z;~~r!uuFR*+~>qqqrs<_o(kZ_bO;at&WFJh?Yi3mubtd`kz2TKe*4di`26&V?UbC2c6GST;O(d!uX>u4+ri=lgf{eqHEq#P%c8hD$0hesK*SN+_zNT!OFCXe6i-6e0f4ubd{YoF=bq1+Ra;j_~UUzmD)Lr^!3~8Q$XKue2twv?i~#Ca<(6ue2ubIB8#*P2LN$N%K>v*TY=J8FCYDb(!P@IkI54skA1>X=1uO_OFtd%yoI%iP>b%1F{gfQ8VEYtx0!5mnY0JpLr(DbG<yQIg#DTC;TR-*K;b(GbaRDFT`KwAJ+$s&16{I$O#FEKTH3yBryr3yba8{FV%U%dC40|{G48}Q_(9vNMF*N=Po%SE?Hc5Ji2Ut7inlj7(X6XXTtoIGi)p)aY<N8?O5MoC)$h3n-D6?M&*$ipX|tM6XFSpNgOA@u}04%(38aeEkopuzGTBvUpD%ZFjMMLse01rSyGv}N{BELOa#C9887^@U^X#6pksOt(bGI2XH)O@@&PC0AogA9JR!(<8K=Ko;yO7Zp%~?05-o#&fb=Auxwgf{TqZ6V-@0_2;bC!~%RDm21HQaFvpJVIP>v3c?ku&(oB-vBVk6WmoDpz@+AVpGCnY?U#lxMG8G2NU=koI<=l;{i;p|&S1TjbNo;|~P8kAIhCx4{xg96N`lr)mUJZZ#ESWf12Cl`KJ4WMJjlmG8+c<39KR@79;7Zd`vXS$-M(wL`61-GgOst9T)LY3;cMy8ram{rP%MJ1R@2r$@1mCVwt6H0v)7%_sYC}su}a#axkKthoGxK>M)HE?$rZR;u#EC{uVG;4`sXX~CcA^iy9K<RoWFhHDAYh6)zx2wKVs;IR@JT#i5*c;U^TSs(lRo;MighHMA7g3B;sId~_)z>aibGWpFgp>(@R9{D}(D|`Kr>@ajn@QuKjTf1mU~?_c-u2j;)ItRnq;6`VTAwzb2tO6YJpn`l>DBlxNw=dCJ{HYOR`LIEnf^oaz(C%!D|TOIH(}PsC6b!*XItJ)cYDB4hjML)5biO|-zV{a9-3bn!ND3GPk68a!~~cot*bkwAdcfd7k&mcUz&!-6RjP{7lNspBt;qY)01rjLozrc;_xJo@bnk5Okof~N8A(L140^JTcAJ15;PXyj<8I^V*x-BTiv=Lz++pyC@|Qys`}sgeehc9!+^DT-{3|YLYa04pH^Ok3S}Jr5hpz@GQE`BCwogEDxNNy{~lrZ8Hk6J?_(bPeF9i%9sQO>C2DqW|C_flNtfhG_77Sjz?uE_0Ryx;(}a0cq~EDXKjL)KtVrL1y{DYH^Rps-GWh3cP>Pi~U!*UqE>&rayeQK5)-+_2maXO>d%xo_tJbR(oJXZNlgWryxs7ABo&d`X;F5u%lbYJwaPw{$=ojw!{nu?am7)6irzzhIB#}6sN-Oqf`18s)O;c&D!UM`T73=}|6n5`Y@Ftny4N!xf1UktV1)Uqge+IzO)h|4%-K2ABH-V@OV-`R|BN&US+6|{n3*3MNZ+cpdTS~Zi*8J0~L2=LL>;-_$P-7{-tjjaq1H92!z}6$0H&?tnN>ip^u}4uZ>=)mbv`dd7gRJ1)NxNDStQpcX8&_92<?2dvbmxLsEzEe;Aa#}}W-d@0B{e{U|BK9AF|LBKtF2=fL+&RcwY-M)E6@45tnjNDTUuj?@i|Xge1In{8A;muNAGRCJ#E53(D*dcehVPtY?vo-Emn~NSo@a@+X%M_omofSz@c07cq9et@UJUL+H{@^Y-ybz;*#QyYzB<L^+3GZE%89g+-)mQnw|!~#eS9<0>YBe%%048<%@am)42p!3wku9sm?Il0nZeVAJ@pDcASDMx3t>x88r^fFW+|m+Othp@er>rklgJrny%F(+QsIZ=UK0rR#(R-$FMtBHLiyJb(86$FWEfPdKq_C!ecu&U0Xt@-CV273t7g73utxO_J4QLZsn!jvb_rVJO`ZR|1_<m!*hHRV%F=faORm@B#$U3XxVKqQ%8QdiRvUSyp(+8rJOYDHA{wwj=hsJ*-WwmN^rE5uot-@0-JTz@l`BkUW$3m+?Bin$wCDY8xzFF$V_l%?TB!kXb#g!v~y!^(ZpE-k#7@Z1;>NfVKFWVG8zPqhZzw<xean)@Qtkp@;b07Q}lJ$MAqS%uLwQN&toikS+u(UFWir&4lba{Z)*n^q$+EmQl{ZLH6L+5+&e>2m&@xhC5;zL=)J&Qic*FaJUF-$))>ltuIxZ%G545IOg`{O%XjgQ#89hb4en)FR+7XEHPfJYCQ&L+?Ox>pM#5WN67)Qb$CSBHBXp|DnZJ?KbSm{h=>WFQm=IuzN!a=sv}5F+U&l65_ST311yR$wRx_-taQ5vX*%by|Dt)9#Sxym4*a3EtR>JV(i|5WDVqS54`Z`d2i{W{+w`x8(slzE$Dhpq~E|6J8tV;^^dJFupY_ZT>_$72ivV-bRy%UMr&c%;sBx-BuxK1Q$J;K^p#UuwW?+Xcr@~^3Fl<9ySAxemt$%$^R*xY+P9?_w7TR254I+z=>!Z$5@FS9xtobt<M%r@mRih11z9$&jYVSUh!6UkuKwF15(9a3J03}s8b<*<-kZn+1+MuaG8R5d2B?@^f~SC2>Y9@>2xC;Gohx4GrV8!0LWk+CjRok>TbozAqHX9X}$P`V|(t0LT}WR=q<#`vpXL{uojSk(f}iIs{irkA5JqNwgeOh)1T(-@JI|Cq@rUS=}tA7e7Q8hs6sWt?L&+IX$2N0^MnvUY2Xj%+I8#8;(hPG;1aZ$c$+KO-~ZX4YKbGa}If<fD-|seDFExP;*?_>4MuH>`SK5WJt-Xwpk<aR1m-={r6Lkt3e%8;~C7T?uI;8mR89%S09)^XAT}J*CX)=8erMQF-jhn-TbXuLJJU$Q0EvQ|9?jeXHTq`ust;xWNZ`2GG>@BI~$9{L#@hL$>P{C&Wqaux@&_?C@JY#*6G_DdT+=y{ua~^RK?Q%)~jOhv&HWGv9IN(y4pTUhJ-$=eC%ZND6O`-21xx$_CxdS;sHB_sy|;Uw!*xwpPqx&7^n-x%c3(j#;0DV{a{q=$Kv4<7GH@en(F(v7%2FyzUlssQB~$orIBBTvzY0lez&#)fqwuwDj1+nJAA^O#ZxwuR=&@W)EuRJ0>_nIAzts<GRRzG;(y1jzi_MG-ud~)}>)=NJk7?jpz+|etJC33B8tOxE-DI+H;*2B!@U*FP~pr)b1^)4%uhzVO`5r(LlQF%$!E8G5HDxEl~Z-OVoVCpZJl>S8$G~Y&-Q-jDO3zuoKDYZy8#0@35q3)8hKelij#8F$F6ww7sMoFGj<Y4lTNu?qB?)?#Dj=U?%v^R#hmTgZq=$MgKpHn(zAr3c;&UTLn`ocRp`i8;q8iRSI$?Buou())xn3!_#seCXufl9D52yP)-V=p{yi25rhIU4y6k~C3H~K1h=m1!(&l~y8|6cG4fR>Z<Ryn!Tzu@8gY#J&)%>wUISu8$a`Z<68qI&2?Z~98GOs<xA5XV)&x1Y8>dnVRhAAo;1@|nvPO~*C*QHc)zAi%cfX)x<>e?_aRxs==A!9|K*K6Q9>C~<qPn4=tqvqhBMLln+BE-{IefqL1aGe<^5ln?Ykx{nB#^bm_6v~RI63Pn*p`vp*kWwcJ){d|5|+1{tx+dx0gGPy$j@7`#xyMQ5tca0+&_mw;ikUP%CoH#xh{tXP9EOf*s8Wjv6ElTwa3P1%LQx<^TC|%*6OjfGAXJM?$0g^Gk8H)&ny<?F&rpCu}o5D)tAs#O3UbKH?$94e7u?NVAKG5V<}ScO(6!jA?Wj2u<OLjm&s89KFd&LzS`oHz#ulY<g2#pa)kW9)yxbf6l0^fGpJ>b|ETo3W@<y+V_m9O8%({bJcacKv`3i6f9pjkO}6=6`Aqs}@|oE7n$9qpwAxtn6KG7xSf#92e1yqlMl%R@fyLhHAEq&>OoL}QOk71b7?UMM5+W&mPIk{D4wLIAloZc$Sf+0Rg~Y$;{)``f=<e@0JzGq-{yui3?}JZyj~HZdb+$6R!|OXgkV=o$ZnzkCvVeE&EMdq0o?P^+Y#C52-5V4)(6Z~rlE7nbizNkkxt#ekrbWTyxWn*()TvVD+|$a01DnCUA2@#H_3x^>e+w^3ui%_FL9SVvznCaEvoQ^iT_vb47uk?hzTw`05bVwpD2;I{VqRxr2+A@NnSnkV?;TA4O_Xc7D$Dwxb^oy+{sDJ?@5?9-UvLfY;Oggl@DOs%JFDMC>%(b@hD4`$=2bJlbf=9&<nRqLR}Jq2M_z|5R<*G?0{ngBEF_^%qX<uM)qfCO@7VN{hJwr69#>EIWQ`TUgYo_^ld^H8@4BJFAr?PQd)G1}iz*%!M!XC=mwmY^j5;W2(TZIzTQ`gSKh?w<<EcALYrYt|oml)}(faGiy@lS*-~WlQpG`8Eq$3j=%!Il}ndxF>h4Lqqz+uVV8pz$+oaJsEDcQ})kjiTb;Yw4?QVCJQSnK32U71%Np@)hWxS@#aA$hE@c`&nP$3_y@$`EBC30$@ldMHIDC-hM3_|#%Y{3hst{IQF4b%zl$Re9^w#PMCqAbp}uj1PnSf&dsYdpcyd6NlZJD?c!O(1%?_<u;9*Cld!4s#YmlSGyC;=L@I`s{$RF6Gctot^_RW@&@+pp8NT>#n`JuqC_WtM@&tWh!FyGWl~Zyfu#=p3&?aJy4V5>)DoK1X6~*+@wLi&gm2-5#q1%`wORW-cv&CRP&_qWH^x<$2!!p{1`=<XPKsPFnLiT~&}5c!-!0>MjVmmkbi*K}BRwCy5UE@wQQ$@a4ciqn59P4G^CB#mD}#={6ANblY!*zia3qU{MyGA$hCcS&*iUkv8(L{uOK0IBdutV#(L>Kj=;BE66?|NpnC2-aMyC$y<FJ(+IB3r|E-+GWXI~_q^}<lFfAi~Q)?J_qsbA;k)AO9v%m$m*5wq@?#G9Aty%@hj<<t$N{xe$L%BjoUZGj;SDm`M(qmYp;v9?xxjH20$P<MkR!s0t?7Ob=<OPesAw=7b$nR)Pz*rg3nf<~y@1u=MSP1+HxwE=!gEvd6ue?+Sb#LIv8K7pSRbl>D?^VW#dFCP@KuxpZ5lc~+e3;9<wC<4KhZ;xd8@|QstVt?z{LKQ}#po)nBFE&j~eUd?1dcwp|J930t=&4GyfCjPVS!HFWOgg4pvp`;W8u{WD<C$mLh^!P=h0aj%88lYnfnGZmsmOo5@&vb8dayHFjNP_uS+~G)5J`g!w><KZ%E=2+wVq6XJ@%V#fNDniwWqSSeaBdyJ}*!E4X2NBoN?A-o2%SyH;P9<c6Z=C^&Q*+MR<eKnWRqZZi56;C+@bpiAJqKRD#2rTXr@wjiW3XrslOWqdfCS24{S27UQssGUi*$=JzC$XI-AR7M=1%I{w}xh%^kstTU}aFp3X~d~Icyq|Zi?H-`fjvjo$0<)DnzF>JkSuIsx~Ya9sSS(+>H5e4lecl8&(*^F$yu{sDN)pU-L&3igkG=}eml#NWlQM_!*+dRU{CP_?!2-vjg<Gb;)agIF3%QluUUV@ix<sVImD_gqU%mH)BXDMVCvj!HgX2We&q)Hf`{J`lj3g>BWZ{pErQN?e{jNA~sO^04!hxul)S1P76X5&s^%2_Hr>3~#~td)rtlC;*cVzl~eiD+9^6TATpmRa(NDcREEY1YK#)y+)gh0^G`!c!FN#-sw8pf<#DSytRq<Vn{<H}^C--U!sfS!&62e%?!EDO>xB5EF4MGt{rp$yKYcwzis!FR^wjBw(_=GAaj<>iMB2YY4}7)XC%p$MFJq<*jwKLe6%9p<pTuE1;iCiqjXDW)Ia{)mAoT)z=cGQey3cWzs|Xt)FIrf?~>5rM{R<PmAL87>=>#7RQL}EGPI_oUV+x_4iqoIzCJYel8+I0^?#tW@+~ag0kz!g0l6wWcoJ(;re^u#v}U(l)0VwW6QI>zu=2q5sh}<7pv|G(&OsYLh`k*K1-@j*}c);vRpYfI}5R2CdeDG&LZUu|D~)gczLVJH_OLdB0gSclFNZ}-l=otidqz-=T#=o9R#t5a*{g<bJ3Z)BC4epV09Tm3G`(C8sQ=6vFUCB7%RTEuWZ1rQS$O){_>L}teH8u6k#DN{Ghjm-0(ZK*7a}MTIa`Yu6ek-&Z!gmY=d1;6F0C>T+5N&b^fTkF3wx)yq_E{*aG=nYSBcH-KvHLl5Sv(m#uZHXj@)<LLKbolPSOUVVYB#3BC3pbS<NveW9<8Sg2WFUB|w<h7Pm@ncuCijzx%guCMM)a|%0CDo`O2+3R~iTG3iJgq^jhu(<zdcO6-<uT@w28}DBba`AlBZ^vZH;whEcT=pgI{Nbcah3i9Wz8s1KS3f$(#pWN&LQ+*Km^JQBp=;LYEdKjZbU}(iRs*tE>>EuD@<eoj5GH6UWHRGG4>ylkwMlVd=gjr+ljy=3#f5gRxL~MY%%eNS?pH#IW2dO)fv62X8b};92~U&9tV_&$Ctu)(mtsvzjmm?8VB^R4cK_mg`@5+_H^?15!wt<4+rxa!7bYW-<K~8TF@-u4iCv#&BKf5-8C!~*%{@^jN^LT>p`j{r_6zNg6Hk;x5aS%A9kFRhdxY&QE6Pv~K%S`P;@lIRP>S+WqrOzoTUy3byyVgor8;z4dZHqD3RN9C$TL21L&MSy4NEt)S-PQ@8?6>ob%G*QOuDN~@5pAtbNQgNwfkU61wT(JWT<k8Sgld_Nlhwrr%44q8#e8e7-CE<AjCbBUD!U7T`*|}b*cDSU>zqw9kL6V(~Vcf{p%>ZkVae_Jk+u2Vuaq!at!e1l6ddDot8~e#J|<l!f=vWP^(TzQpK@etMxhbofz?~PA{}6QGh;KY9UOi1#QZ9%k2p8>&C=c(5;DRsRB7Cv>s7SYE!g~f-1&G8HJXsc5|Fli$pwgDX;}aJRip3V%dc$Wj<yU?8-l6M&UpIK!tf0o33`}3iAn}oL3zUUqNkpOL#i+08(pCJ&lwMmC~9t=A^L<pi&F3FmnwB73qb<?Nn%I(j8b(w&$qZkac>6{%n~ef{6R_*sxbVTMTU`j}w=Lh&G&-1Q!+x^R(vNPm=hHSWqR#6Yb*V*$=QKBZ(ZP@M?29!Fu>)8+J$=aQX|Lt$I+oqMhLG@@fUQLmhz=$r$7mMF!pYK<JU8p|D8FNliFarmqbu-E5X}X-!rpbWC^w?v2~9``=z9>-22ZXztd{IZS}B5F~a^Jd}HqCP$n#OyngpfS_(v{wDdQiVSFL9*Ps!*96c~q0U>w#IbPnxb?@%f<W+5yF><rCm;i|p^vR~j26vXqIHSuG<mvoL7UDfGmdeceS9LQ^BaKZ{B@hTWr)7_woDmguyn;pX(<O5nwdkIF6iv;ssvc7;$Let$*K%5LJ~^Yx`o`_oCw1XVCYJdkjJz~XFRoBuV(DV$yGkSQ>_@h7=Ux8k$z;QR1T1kEAhwF`=#F(#kN_l@VYSzg13elfk`FBfF`ns(Z9fm!M%?JCLIY(4*$l7cr3Y!XT9&oqGDVl0Ac6TNKq0woaM>T&4}3^NL)UU7B5m1N?av$1BX~!$0PA*blw!(l;_j6HBZ>bAca#snQ~KCT$$_f(Wyz!Z--h;njV55d1XSBo-UrU0XE3UkbdJmJedcmWrQkyKDA6sYMC?|_6%N`@MK;Yq4My=pkBNn_sP2Nk>5wi4L%|}iL(b4k4R<8Q|S2>J&a)ljhd4x-i%_|{-Gy-<dSLZX$0Py+8WP2sOeOJkkzoqAmpEMKOt413;Xf&3qisIGZ8e2RYR$|`-xJj4ppf-Gs?WAR4uvK@Y_SF`VW1WUg%ji*?^TlX)JAKgBL7qsiu<43|}Ks5lh=4Si?vZF0ZwmqO!@W(`@oBQ&r`(fAjsPlFu3rYuvAS<S}oTB3Y2msr6>m_9l46m_hcI&%-7SJ`m*Gn{c-OIh1Py?|eR%?X8Bx9vb#wHax2oHzkor7oMiNxW`y&X~N?9scpciQ@*Q3p-@|$y}Ou1&NFJHYs+cSVQ-1-@!Zu#7&DrZU@41YGRh=6lJFH20;7}VvsDl;F^BEyCymna4}S2{(>oXohuY+s($fo3I*M5d6p0&5&;IV%OgvI?y5;iyFVE9bm2bN`p{4qaoK!c66LUUcqheE3U}IR|2C8h0I9FDwGE<omF>0Q^W3#^Ck0EV**s}S$5gswR%D)tvie&=rm3O031fEB(3~^o^#T8Ep?~KKq2U)6A!xcYOG<ABGh61fj&}3PVL=B>Kit^&%=X+z03c{KNLi{j6(8u9TkVMH)el|^9Qk5PG<G{426QP6{h@8<+RozYN@|PqzPok_Vc?TVvwUO&oGA|j{%gzI@XRs`7$if=P2{O@e%Zrw9Y2zAs(HKN`lR;J7{dr@iV#54+%v73=Z)VI?8+<l0;U@-h1!Ln@VsKWX?VFY2w5mdJ%_@o%FT9~)MOuKfHFQ|Hxv*rYCP*Py5ug+!D@1Nb#;U|ZNA`7q31REls93%cir(m>p<O1U%)xVR<e+AFWm#5biviynvq3B_wrar^Ek_aupJwhvFlDisxV@v&_o~L2T8ppDR5R8oY!5lk&N-e<U&qCfE4mP@s-do!#YsYK5f5TsRWh8I)Sybb=UT*G(=$(+jV?k?c`DcN>zDZqmT=!sJix+7j8zhYo}24+C6Dmv;QCg1_U%|Ofu#MnN_>&reKS`02;HG${}Fr#uKy&~IaNq>Hl@ZeO>THYUY?(~<t@|N8C!Drev35eY6R|Ezkc`}d=)TWa5&oV6?*hzBvgeiKqOOMc+*i+-G^@v6oE%C2F`ZP>Ku5>BHS$_a1O}Rv>7`#*7C}kj0m9j;fB71CWO#1-@b>3)ktb5f?o0q#y0A0H7fbP^dkME9h#%wwFQ6oU<-bG94snryR6k-YQYEH)Upe|nGi%uki_cnO-)?n2}_kQYy=DX6R==@pm*zR+dbR%<|W#d3l<BKz$c9&-7~NtF-QcO<wXbAGb2Uw{9^U|aLaTt=t)K|*^S@fe+0y9qhe)5l>waa)S)lW`3vv9aOmU1me^sn|58Z5tBd8?4s?eHbx*NUx(<E~TILc~pr?0Jg7XxIoCZSwWHQR!{F#Zd9}`gKBQqoR#ojmTL=a(;I(D&x1L=6mJ$>n;>F7{R>Z=w5ALX8?$^{<4Frb5yjhG>P1x_+Jd98^~L|FddM;^^a29b{_(+cz~(g^&=GqLB&guDX@UeWYFV1hFb$c%1J{}NtZF*lv3Q4qVBH5(%_%Rq^p2_-VZ7-FB|9H91s5$ECJ&B!yw2^=>T*%rJg;wO+IP9QCbJFvsGAzq-oBE<owQQ+XR(8+!?ZU{Rhb@9umVuKW|3Q6U@;>>2%*kH5`QzYQcp}f&|@M2O|J_&ou6HiT6%Ph)pU#-F}nacS}b+`nw#2?ZyTcH-!Gxu`@+_7$hW|JnTA9}PXePXFTZg9zpEqBq2F0y=IxtH$+w;_W2D{h@l1<+i>YJgJsMq*Ih#o*rcj$t==RId25TmzDe5dn+w6_e4S+}c-`>tSqd;S9g)>xhs3_SY4=m*>@=7;#S2GWWaen<LCkU|xD2yMq+7#_rsJEq3SbX0dy=3Y?+8XcMQ{J;RUB?l^E?*m1gY0AG&KFQk4ga34G9=o+JX*`g>>p<iV^<q38p#?wwbrZ&+kp-PpXQDAr)#K&0>zakyM5_TgGs={uRd#t2qpcG`Hz^Hw?%C5zXf*EvTkNiBEX8_r^XRP_^8ym`h>L24bmWdybo=FXM3mW>N*a)A>D`iTSS3a_wxrLUlPDYl~QHZ=53EG22ltJ82K?by|PJB{qs3<0iVU)qWxJv{aF`i*90`tX<mzukLBaB`HFctfF@$f76FD)$7hSAt8V2=hpeDQ!WNvyU|tLHEi9P8O~{gl2`KP4&@3?62`sI{*lky=o13tf>g3nvr~o8LeCpoNeo@y8HSSQg%h#i4Pc1~X~ID)T6~fe?;kT`<+~EQ~Q`n18lL#D4aBs=srg<i<k#O1y00To|vpe%<k5`iii)%?a~l&R%`7aTBrg$p@#O6^}=-Ne#W67eCGM!Tc$hUlmJ?V{0(PHNuSbS}3A8U7?N7Qratw>U?}mdmrz8{Qi%oJ>c_qtj@W(tJvS}NNB@n6}5dl_T0hG8`Bz7OF|nx7HK8_og;m*qyUqw!U3!iCvZW_zGszKX3$<_u{$C?CuUJwE;&j(75-SPcs7Y~v`l7crX)9Ec~R(rHpfIdnicN{zO|}^-yYyyZVv(M8ho}Mr9TRrl*w^}(_UK#8wLv2e6vWU0T;O<s*(0T);4&*Y=iedev3BvmKEai43$~)ktTJ^tMKfg2-Z6%U8c-ZJbbjQKp5FVA`l~G)8G}7XAVK@nrzug_>UkIRuBcWx>o>7;!iqr`1nxkWes;!a`Iu=;1&eaitT7OTdTNH@T%j(Nyd=UF@BdJ&PtgfZV8I7bpDpCIfHH1WQ8Aa0n9$YQ&eSiL$9+OmzCZM?7_(Hu;*cku=X30Ig|VyK(bCDAA9&2*rjACKQ#?zP#G}I%OY&ML+jPrIEWaG|FsWPM_Kw}XYkK&>5I`38w;?{_r*|sE$cH{<PflYX3aR6)z@6BuWZ2Uqyd}hyNUg9EWMU1MD|MLd1D(iiRR}OSJE7axS}dZnDlP+BD7Ggl_A!cMs!S%Otn_^`^Z)BsxR#T1E_^odRy!E>AiN}6fnLgKp=dbEh4kr9Fi!RO!48Ogo$;7QH*XPI6m$SA@XJ=|7Z@$w^qu%wvR<;h_S}zO1ZdV%O#B$K=<qtodNWw{t&{Y2-_#_QaO6pggJ}xnCY=E>irCn_Z0r(JWKWj0TJ+rz#}0UK~SgOGI7Mt5P1g7XKz}f>d69?AH!{&@f7c!u<PN3Abx?!Yr&G;gl_;*$M11J_CwjHMn#LVL~r2zALP7jD0MwJKVTDkla!rsjS;CJ$%#(S8{ZZqb->P5BAs}{k`hT3*L3ODv{uFS$wT<43^Uj}%0yseZm?M+AH5GK=Y2*^0dP2D*W?^Y;ah;oqHQw`?lTv@GY~*W5y+mqiMXRSPMi#Q3%P&pl4|Yj6TRCcA~}08CNb|K;@Kcc?Y1do;NyT*Pc4()iFUla)yqw1uo#ftOUdv++(T8wj-j{&*|fs(vm)%u^7`UwrPK$yL1AGpP$C&>&~MqrH*Q8JP&-Cd#@uIo!QNL&q@I-fD%+2JpsJ}d>Yda}vq?|&Y6YD<MJ()YBKa#JB-U^_!>&Ap6~p?rHhc0BiR5|K!nfdI*obR5v)tYzI$y6a;JNM*p!A#-R4W;h8wm|Oi4=NPUyCo8TY7=zMt|M?rq90<?STV*H4mL?W}i09H1_C2X^hbWMDrzLhTE}LBLn}33W{UIT>BBw`s~zV0E4hsbcK49T24?@D!u@#oT0LNb||YjkwPcdSKCVDKmsW%oMLJ1krpc#au-;;fQMTAe>>p&m>^&%8fAqV^Xk3E@=kTDeIW0VVDuQFZ#j~Sv|JpZDt7Ff!biR{prHw7alqOF+qb78RC%|ObAMFE_L>~zF8ned?&?sfd>T^Xfv?di|MG2a2N>thf@G9py^-WJfBmJjz>ubW3oWoR0F8B1S1KEo)vFvB@KUO3;U+s0+O&MVTRkWTHrqU<0uYZC!Q=}DIdkU~!B`j!!TLjbDqH8dE?6LsyrdpQRvcy=WmQ*Yx0D8p*bFbIgQ0_hxwTOsteZ8hIcv#pP<NX)$^NoH*zRS4bN|s>1dF)E7JLXW2+NQWC2iF+5$dzby7A10!RxV*k(gV_cB4a~A-g~at=e@0W3+{gno}z$kqUa<%&jty#LAuW8v-u})l!6}qkMKTsH9V;Z%;L9nH$YVU8GOajuMv{_kxzb{Wd5zarNT85YrTtV#-!hUy-39?<lhCA=ThgP!uZyF*VSMjwhnqf&mDe%T7QmqJnWFY`H`WT*o>MCt8v)3DqT3CgT)i>1hZDZq&SBizdq^o8b-`9uK4Z_kQxRyh`|-!SXg!dDfb@74wDKRnyc8ZDv<ZJngEX=^50s!Y6jzPs8<}FYu(VrA)r$Nq>mX_cFUnf39ZR*P89Rdhfp0Y}d<{nm$(t{)8&M7s-HAaq1_7-6j3*i=BfX&ro7zzI@lG?_+6|<y4$`_{Ll2N4w%4g(wi_*bLZtr9QI=RoKB6iRfHMcU3Ig0GC(?ub4YXoxtSbzH{pV(`^s9g%DRDtEycafTw&?{I(%T-3VcSBUBNtT3ovNy%@^d;%<~LB8k_~k(CapEU|}}lpt!~Y{gI&sngUD`6K*!%-I8hc?}I8a8e2U;Y@|XI>ba(2Rk5@iO}zjVFV7;Z+%@|_A4)v@v~j_+va&K_UK$)_Sg3<EkaGOR5~@p=ga<j1!0o_^Hl3g2)|nP%AD`7cO*ncZs%=V>_<l?K1DX+q{UunU6FZv@qEWryG|}N+CS1|e|QHu)0ZvxMH8|~TVln&Zt=o))_LccgL+W2a8M=+s~ns2-V5L>=hN+W<NO`P3mKs<^$ShBFmg5}Bk*l>a*D$@d8u4T&c}f%)g3=x_TF;LLb;I4&u#6a-_#OAWFK)%r}~As5-1VK%23nwtc2k}hNNEY*5!k1N@^(=A7|u}p|;f%L+r;c;<RAG6FT`k=_KeC_(iMAJ4qB}`O<;-Q{y-3jm;oFMb5Bx*_Rtx2}`X2-7Q58*ATwYOwS)?rvHg&*WX&#oL6eHMzTfgVuQNIRDU}%!So~I0gX#me9Lg_r{WvC0d}2cr~pnenW`@0C8hP})H;5SuUN6AK&^4;3RQ~VN%{|Sq!!<VKf<3iT^dH@w_~#@eR);hZfG~lL49Mmh)_El%3531om!;)>hQ@DZenhZv;twLUJWGmuv}~s)y#{bP!GmL?Tv|=DxarSIRAERAZf?4_jB1m@`4KFlwY)qr_5>0iH-fK{yYQ7D6&OeKFVv*)(o}O(#*(3!?LnGB8k%x14vYXYa|yvru=A^w4#ZuYq_@B3E0q7D$$*oljxco*+;OnltA@{LO$X9$OQYu$`mrOi8esp`N?vbDH+=!bZdFeAll3*KdSIoQe5n8){6?H8w)_$7(|6S82LWBN}U>***m`}_oMFbWIf}IN0iwyn6RO;eh52}KQNEzf89DOI*<_}S<ANla`gJ^pKtf)>v(?Mf4+|J>j=M&@avziBm6dhhWGPlc#DrW&w01`S}yxt|NKBM#Op-;fMeUdzwc^(n#VRg`?Kl6KcDs4pPqpY{+<2|@9EFx$$vtd)ih@8&-qmagN4|i{uzHRe)muMy%H=@$al`S^w7_<2ahj4>r}=Ob^24S-cm}@FW%SJ)5H<w{EROu*tfg-OYJ2;{^!Chshjo79k3Bu8Y}^@8MOZQG?8dU=H;sCf!%PmaU`g>k}Z)qZELL$u6Ev6ESk4I1~&FN5m^eftAA8+(DCz6>0g*IZ9Z0I-mt4j#`;A~m0MVT@bsMXU&dp^GZ4cFMz>E%@ZFMFv$IYAVkK>>_p<oXVRlvOA6mJQ;LJKbJ#L3cieybKej-70-W~luzG4|Hzxc-TOi!;+{{Ti4L27i<_@BKgA@7Bl=6Bh3b_8HYcXVwwlJm=ETm8{1)2WuvPGa|>oj7`M!5=@wGq21a^z=p1iZw~;JU{+ZryrBwu43TLCK$mhdmVJ<`7f3|jMj2CzNO#iKfUlYvEtMD`}`-CUVYs-JkA|f@9y|@d-vp1!Jq&0fnVy7o_vL$y?b(lDT<!p_;veKJiag&-81fM_U_wU`Ga2(;<%iTZ}#+=`g8Yw`p~On_3?{GBc>O}-^V{?bNC90Q|h}uOoMs!sWY#58=U$4TufB|;PYC(TW>sE`pDU7fApniUz}e_xG=ou=UcP9<+%7W)XP44W&XQ1requIxu0tF8!IG>#Q7g~f6+JpD1c=5_h3tIe%akqao7KV)Li9tyb{`bS$*<CU;B@t2jRXXJ%At5dQG*U>(pdBxW7jY^9`8Bobmfm7j6Z?AeZ+<2{=@(sb2v=Kpc-$%RaQIQIkL?muK&mAk)77^t0cCOdx&^P_jtuqDj6|ss~esQ-#@jXqzYe>`#8q-VGCm+w)FXr6-{leiB-PY9Ohxupe&ub8zDLF;482uT)Tg0Q&2{``Z{ica{iKtyo8t)D=8;Sr^S!kmLjEXmjvf7};5ux@g2ZiE#Z0JQvP_=K?&-W+b*t53!vL!Quq}+gcYbef*a7XRx~S@}8@5nHLh5r)m_<xe~Mrs=zmH>6qF7G<hXxd{T>MP@x9vqlz@akE}@7(8EVFv-5Ivs1#06Ys5SrWg%Jp9_22p27pS_fu-p<D@~J1lf(+iR3+2+Q(jZH0`<BEr$IGpXFH!oF-gqTSX{%Tv@FUtwIoyFV%}aKW=-A}#IYW%%D;R_Xsu2xZd2`=A8eN8`o+(v5e`}wEMmu|%2FgkA(HN=4O=Y{QD6jXF;6oN02}r^m9>wxF_URn^v0q)*0i14CaPrFqM%Ksj1Rb;ezWWW`I?OzACo8I1`i4gYAc|K30T|<kJ^HHPFr4<>PiC?W7%%W+Yr;W6Y)8)Rgo;>XhmSuLIzWe&K|3+6S-D$3SlE#`9Q$P=AwHC9E)ZIdZYJj8A8vO)B~Ng4cK6;k5nyfcH8u>Qr~gDd`|c{F3TGJ!Y_DJfayEaa8?RMv}Rw@c^q1-{>Ucro(b&YRD8-Qj>~|^H`esWK>GmbzoMxYtY3lqN}&u7CeO8L1PAn*+Uq!#5RK@JLQ7aDeq;uac4qTfOem(2{gr01I)->={QM`~pY+Xle7=QY8g9Tm3HHE{-YD7kJ(3Ip)8?9i?>0{Q+3DU|`qGXQA(-SJFnn9Gvt)MWT@nAwr8~IvIouEsxiusR93b}SZp+o*q2H-E6wRLf=$@Q|Y#%8W&GX%lgY0AA=8gw-Rjy=%^Rwe5aGcn_cVi7#nQjiw0NF~?fMgmMn(4qsdGNtg;2wSRWCKhsjA#m#$)pVS?>nQf`3e3sea*YMz9t%T%3$3GYH;4Ts%se2D6x5`!ysD{z{H3B=-wGtj1rr~K;8sN`7|>T^KyJoUu`Qu*p2#y;Xnlw)byhq`TmyAN>2;`wsi0&o{lf&XNf06H*;qqo$wACb`9tW@2SCt&EjJiK-|K$g?kNq!4G$yuBRVHFqB-|H%_K$B{B3H0NpU{-e5-Fa28@ayW(t)HCgnAtuX)VOZA8Wll|NVG49*krKj$&e(VnG)W8Yfk@!HbTvS)pl%LcfmKOq?i|#Nw3!EFX2C+)0N(2~>4CengllnQk!??*1b^lOzShMU7>)ElGp4c4*4Eo#StzWo1?DtPI@fY8dfCdKbhzJJZ58LLrAWt+-%JFesv8Y|l?NU#pjcOAXJ93r-*8<==gP@8j8PL~ae&_wXi4u-+RdpG_)(DRcn^_taO-Q8&J<b?<G;L@n#N^sDzZoqrtPtj!B*&B7q7k@I_v1m?l18#6zw)6+{hWl!<D;IqQzeryX&+LSadKtBy^^r%r{OQVcrz1}VdA|_B<krj_J|jTINnrQNHMcZZ>6U2PER1HIrusO37v)F?WW;x`8==qkpwowX}s6J=O<&9AB}fQ*{t^AS?;!s>bD%}NaE2lrw5zmXQp_1gZWLwHRtz@iCmX)?GK#RYkGQbF|EIF|IUNWrWdxfo2RNY#G{st?ALytHIW~@APk5bAB-ArCLc}qqEY$R4-%=h-Ah6Z+PBz(rBt42N;l$_;zQnuBYHCtfPl^!-0R$yIEZWG$;MU}#;iu;GW(cTjG|T+#nR*i)hp1a(JmV$$_$Z=5S*?d+_Lc`kUgRuL_1e01j?804aFWRid|e%afxD&|JjQ$5UsP1&txEK;PW0c5cQP}QX6QKq~}MML*!^8=vYn7qolw!S~T;6b&S+llNAOT1Q{o!ulayZUokQ5PjoMG5=CR=tN!m<u9rn)Sj582+~^x6Q+nU7uvFVhtdyuWgsdEDqsKIlfz5Ep(9Kwfz{Nnqi}K5U=7*F!?R(6l#O%Tzq@6IF-C^n?@s=Nq@t*^Szx>KyM9|h;;d0s=P)lG6h-fi^jI}Kj<e*MXW}PCb{uvc_8<grX3?E^A4#^F>z$UBM-Lq*UGX<))C})aN#oB!<VY)RX6du5m(nyLulipuQ_=sh8Zz4*J#RkxcAs;NoD3UvTu22|6EM=Nwqgs>SC39(I#mXR<m-;CZ5IAy(Ol*Q06J3G#bjtP^Fe!e5akw0|!PZoQ9}=iAmqC_|mE=O5ed^In-H}xs>}-}y&zBZh_4OsW9j2x>P@%|M;Z<xa?_e_ti!c2CaOC&*NHb+G0fdQ3si}?6z3it;Ia8(7GIhw*Djh`iSk@p0^=P^(tBQruS%V1no|buNE-3I4&vS9jl#7dLBhr@;W?gJeEuwW*X+fKl(VL7au{DjR<QplGg6O*vi4}cS;ta|tR#gY}U<Z~$T4PL+p+*jD81*|zB)8~v3u6O^4ah7PXR=I2+eyv?881I6!<u?*ZYkbq=@O(F_3Z3~p~}}r<D~SJ%&b2OKR6leHq{wNt29*j$1FGKYDR9s<ozM_WYfRo{)AsCH2%VOZ_YRoLs>3YD5Z3Iq-9MU;&3ZJmpeaXP<-BjrDET?oIst^BFqFyT=|#D+K0C5fb$$OsU^FR8&od_hK=P@s$_IsL{5&xgE$q=5C>*+kxOR2sw4Y*8_LJy(3ew@Lc8oc2_J;Fo214Z_bCkJ<O8k;!hb!OEdGD?-X+$yZMzN{zxiErefHXG?Y-~0=iT@9^W*vDC3ckBsUT6HMuiHBfQm(8MY6B}VPc4pV`C$Xg=7a?cEu5hKu{2rkdOl6BMK-IsRjtaBEpCQ6o?d2W3<-#n4k68pL5SW=ULwG9qqe5bImo^m}B(OKdra6rdTQ(+4Hj6;3N%XJM&+c%~oDDc_}p6st<WF=`C`Vp&b});A|B~gwr@)Lyd;<ss}4GRP24+{8#QND&0ww<)+B?CRjY1XW8Ru(B{5L+RU*vh1!@@^9tW)%X~Cy@`*~fXp-jLyBE@=Bz^MOY=SDBAaMys@e$Zw>k9j;XpE&Qjc>p4q-kRx7MXZ0b?(#jSIjX)Ingn)-(q?tMQ_CyY2q*{xr|aQ0x(&p*X$Ty*kWZSP{y?!WI0=@sd}B?O|SbjS{C_uqPkohP%guZ=9isrv)9LecJk9JA3yF*2<G(qgE5EM@zMVJQ8MOq9GLlp6vAKrIHF4ZB&wwC#zlXkt29eaZ9)1n(^cZGL<O66;*2dcZDjmH|LQ2Jl+6D-*Hvn+>naJ6yG{tJB&sB#8+G;%yEz${${AGhxQ%KIk9Xjnk)o0j39h8IIi-sHb`n*x+|YsD%F0#!-#@}myXTfZze_Q1Mki#A#@D9s%VzVr4x2?SFxTy=10Ty>O+FMp)lyF*AM17QMz4%43s%0aE;#dbnG_2K$7o#J&!BG<$KaCJeNa)Z)Ua)vwR(zY6ze7LQ%la9mFyzXh5(@x<u{q8S^eo|K0o&S#<V&bZtN%NM@2(Fas=<c{v($%V9t9=7SL5}HDMu=$T`Ic9t1xaElXWe1{HT^B@0NwFy;%IdA@*CD4ygCw4L!&^kOxMz&Bhmc#PF7Ul2;r;Y-$_oAL#<Sd%+)c{Ruv*koB5DUPN_Uy=o;^BIbeZ%GrNPH)_>_3ei=H+gqh*cxeRbxT`Q#oAwydJG`STu41e`yER|1F9`r88QegOpKTEn@<-L1QdMag6*srUF-`EnhQv{>fFST;9oIFRTTk=YA)Npv@(Tq{1HP_Ee#FI45AGIZpYhnp6U6islmG8>10Kw66%>{iL@+qnv_tOkxKFUs+9t_Q&Oo*QthHB`_#~wzh;7RB8GjDpq$4fT?onzOoz%d7ZWs?CSzM0wn>^Tam5U6O=?jM>MbUq01>^2ssrdmMLGeR0Mx}WJcuw!eb<w!l4UqYagSiEP%#y2l@~T|VUOh&sa!`_IA)V4ro;w9U<3h1Qks+e$`ViBT<U66cZk5kh_l^ZvA6J}z+Vq7FlSP4Bm6&>2Vs1`e6lW?p&~=cz*LB#6l@l!Sb<aD+q9H&U6HNBr#qDUBvqQqm*&~n)2GTSq9xe`&|O5S8v}U$vj6M_0nSn0LXOl-T+#!Hk#aEB$At!EUdpwkCo7VUq>|X6X{bcIY#Nj_A_<ItUU7%BZK9*9T`B^RLj^-1WL*+4Xck<UD5xkfIW{Px#)VHF$p>Z!lf+jF2c!2chTy!7Y~vL2#3_6*Z@-zvL5u}-d#5->qL86PH{mQg!1@m*f{=V9lhi#Gq%e185l5OoR>pjO+EGn1ztsx|9W>^(P#(^hW=d>D?#I?~Mo^(Lf8&axEe!gykAC>4uVyjZG&Iwspq^K3b`+4Q<Zk$OujD21l6lp?b=%~&JCs|R1fQjmCTHQ26H#T}W$u_t%q{>}p1Il9JKRes7Es$S&)#?>q%~WC2P7%$15PEp4h)J+l4pAI!A_npyB0rn_9lmXwaT8xv{R0gIn-99IA9_P%txx1LEAxJ@G<FUpOs_DAIg{chB&1M7{)=V+an27c`{;jV?4M#)wTeC#U>B-!LUpl?dk`U$`k|)zsbNO<c8&Dxbi^Zgi=ln^v0T9*fWzU-OwTLorfZxD-YHK7=W+1D<PMUQrl=q0H&R`I$#Ncx^_p|Hzv;pX{@asSD0Zmu+8q6=j1CXn0zUI&3@_*S?oD~>BX_}HI{5*slG&PywDuJ92+xN1P|6IvRUzJrCjhO1LG1E*A@oVquTJ{Br0Y|-21khqT+$zvWB`GCpyE`QfJs4iz8`$fANDU!}lWndvffpm;7<P=c{>%Zca}gR8oRPJRSZr_Sw3(UwZg=l41M`hX3z=yj;XAKA0p-s+jy`EK^{J5L?Sd7)?B*gb+@&BUnb%?-rrsxh6bsV8!hH6SDBwR)djC7JhVKoOlCcxq*Sq|5N@U8J1o7ht+BF;ZzO&l4OKM1EwDrS<`ODrb#PYGz<k+B^2<pPyiR-F{L|~jiVW8SC(5yFBE|fiy*+{kCOlDgMk0$6HLta=;;`ROuVt7o@rm5PR7PtrQ(XPj*#o6psg&y3}-isQJKExt_VXji&0~VQT<4Q9Fzw>)vHZsdbR4{sIJf-*P#e0DlRQe9L+N&Yr%9!#L5liGrhAJ3RD<XoJO(Q?K8w`Z=MpX#R&Y*A7dUhXVPh-fxD!hhIv$DRIF&L1W1ch)zu}_c4aD=o*FLTbT(D9*;FlOQ@k{r;v}*rmy69mbDg!ym);<B)uc12wR0PHr7MVLZk9_$;1019P>(j&1i|lWz0?JLHOrzRQzIYP<k&QWKr_64ssSic%A+b8ZIcL&<;*@(e&Y|m)RY|1iSYjIY5>hE`Cq)xYo@J2e1552%_PxJbN<$@W(5<Qk7;UJD^qedAFp%0V@fu@G{qLuQ9*peIoG@9Bcg?!yS(8(HW_!+NaH_(wkE;WKF=T}_M^IPBrPT+53|OjkY^+4m$jwg{s80vXYIBTdIx_o9q6guj<d1~2VAaZA50sUW0{ykX;=Gr893U_Kl~(O@vG$Hhv=#7Ufxsb7tWydRHmRb@nb!evXSY1dn*0ZQ)#Rm&k`gkJ(bD}j%}4fZLxZOt*!Ejp32R<rxKzTW>t63L&OiCHh26lz921<ql*V5LDqRbt|<_bXU)b*<pY_iJgJYWQ(8Aoe{e>2%<_Jtjf``-9zxyWQ_W4-kkCJ<*1(M>p&2OLNqU7)V~}Cz*|ekAPC@fjg}aud-pE-Xc(?`n%$9;^^rQDB7Zj^5><1}g#LXIz6t#-+uek3iex(e!K@zyB=81eCZz?zJg7o8tHM#Q#?d)-LYar=(GQfZ1LuTezL?X^J^Q~U7v^+BBy~G`a#4c%h9T3Yx61#am2^)snn%;B5VaZf20c5C&JE@eJ^-vLn?3H?*D1;T5&qw!Htu8F&^O2dyE+t7b(qgZ8!Ulbou~Np?Qt`=8nnx*4+3zXMo)?Kd_EfLo7N@4(Fw4&`^XkM(3LNVSyYZ;&<-~ejvEYZqX*H$#Q)yZ?_UFh0f*U`mS%UBB(WMwhQXp$prGrnKCB-e(7V^}HfARSUuWm$mt@2zG$cs4|A-o32`eH%0fLv9LA-vjzo+Q>-0OQQYeTQrT@l%M-<A$^W1Q)nyATKn1Wi!<whnvqF#J1nrD}d+Yuv#E5=)~1%z)MZE=?1tK*$!G}fl~{2v4d{{2b-8LX8<uT`3_$Jbc|m#tV7l6Nc3V>Y-=iDF2}Sot~>!^#!knC58}7r$Hp~rUU_r}y~tDbg&(K=CHH&2`YwVIfw`=`muU}Q2(3{{>9JYG+r)1((QM!Qy74gNJGe-`Gfg)y_8CDLxdT!~Bh^RDlXm5{EirRm{d7eGZomSf4zInQU7UR$g8|!PQelg)ci2o^JXmLJewtnJxJ{Hx2vTqyxaqxxMgl83)RL1L6&n9o|6Qs7?qC>^A0Lm&gRn>3e1sXp&4)J^(R~REg_=;_Bh_q9P#M$8T`*AwOBk(bee%1jY_O2&Ynevt6X0!mIc*uFbh5x`xT*$Uf79T)^=Cd?J=7x9TnyJP!Sxv+-cYYf-%-N%v{GAX(FJT4oobw7NJFJkol9HacBM4QDnzix8k`M%nYZNgC&HxTFo}jGuGz#Btk)xdVm}gM9Z-C{D^Jr-CS;}*8PL%Rh|1ur8tSQQR*Y2=G4-r&?1tnQ+3U<Kn7kHrGy4tV|CJn(9S1UxH+!F3CSNP;w3N=u>mTjac<VkgIlqrVs9s&0%+Ald|IiPALS5ZH-E;DB!$CDLrY~-YTCbcMN5ziUvgnbImqUh5J#r7^^#whje9Vng#l6;MQV2zAqUrBU#V(|c-<S);iK1$dT3GKT7J@QvB9%ZbZBm+}uRBZ!;Q-UEXUvr9(r1vT;up828zk@a5o7-+H~e^Q%?-759J#t-s8)Fy(>$uz1pM=O>-$GFxHI{iU%3ssPM+C~-}v=gFF1mt?&ONd+S;4CZT|Ob>Y@iX%bVF0UlWHCVcG}JZGLdWhBv*@Z&C|AjSu~0x*XZRvWecXn_Y9ICf>W=s2fju;%seF0~LYY>gQDb#+W5&d4#gLD=LF|F(coC&*5%+E)R4P9PoIjUQ-nzJM^a~H*tko_A8h=1q?-YS9|PKB5`W-EGttylqqg%nkGrjfA|9%sMdV&nhc><lmK`s;r)S*oTRNB3V-Nvqt}pMXN&?-xVlVwI-Fc5gbwE&Dg3g<V|mkk`{im>8<E9bs*^OOJ=yt9cnZIX>otAmlR626aZY4hTO<wIcv2)$b&A0iTdXD-*TK|Ym10cEWL#^>xK^z5c_OQVDQBI?xTcwmYc@w!zWSb?TYj)LC>6GjbMWR;y>%3<TQf^kL-RGJpMIAAlP%KsO`WK{C%eOKUc{(d4!4E*4p!VCjc{Yuumh%AMl5`GKl_~xErmJ4Zf^ut`SKqa{MGk}&XU@jZqZXS2zr^P>M?vzZv`qsvZNq*(-CJty(FyR6ldE^*ayqGEL4lk5&E2Wj&Mk9u_%N$*2W7MhI&GX?#2~vu))@9a-tFojQT%sb2lIPy${sDxmr%#xl&HLCO*9E*tBXp3)Nw2O|G|>IyNagjw)WjfY}_Kw<fDSmcfR)liNqSlM#GdYjSu_YjO?Q?zYcXwDfBJxck>W4xYQ7>ZVVFx$8yIwAA?t6PCzJum)MI$THU1Z5?HuU3;l!J)Bic*`-Nk8Mbr~HaCK~nbHgB2=n!#Y`vW!x!XIWj|JlnrD8f-f__;sO)Qu09Hqkk_M#j4NrAKaQPAso7uZ5r+qWto5c+xwq)ayONQqTQ?|J|oX9WdxT}6Yh6fo?ZuSvjxsMc0y)P&ns^Otam1Y^_qP8<;GrQ}`mkOXSd1sVvRhqJmh?g>hmsq+iRbetMkBd~S^jRh-wcUB`{SH>Q0%TB6G>UqWtfiPgG)bNZp8|=Jfl&uW{icP5-b;s%`dA-Q$X*?GllRA4T6DXhr+^A@c)k<jjD762|8zAOm<g|YC#Te^7*@~WA>R~CP$MRmKBg52Uc+rj~Z-}wL)jpQs&8D6MtQn6+BYhCY8vDLkR>7>t-Jjh%w%|Ey#MDz7b!n1)Xx51HgCVWs*bbH>ynet5y<$X8Z6#h!txgG&R1~3-@w39Vs5vUnMz(0DQb1n~*7Bs95(s0SqcZlV{WCF*6gjR}e0qa83bh4djeQ`cTFZ7~0;|N;g-E_|XV#Kn_V!m0VK_ULH2k8dzq}mQdhBdeRW}qCXTczqO^|YF>_#3mZtz@so^r~_tI)j@P>b6b`@h1hg%YthQa8$9k8NcNSOXG-YG1@j>E=pwj7b<2dg8J-YQ}>$e_U75sLcv-Tag%3L+OmLY*Y$kS+VfS;pZ5|YH6yH#~%t2<|v>x0xbQkjdPB=3}csBEK+O2Oe)zvJHHi<Mg=tQ=Iv>ob&xQ=a!Qj|IP6Fy9%o}x(tF|b>*gOXjbr6gh5XbBNf*YeRZr>pXQvOA-2U|0c6Qmbi}&MC8ynVI!C%L5w!d-qH_fhGes3DDHk6*hv4?i*<5lM{d*urkxmRm3H<ID+eUdJ$2^jEf>V&)&>NDzuZN(~VA+Bbcdj<@sOy!ZHv=`A%6K_Im`hIHPr$i}RUQ%h_?u4hPU~#Zn`%>l-{X6$fHFT4>#2E3~5on%5m?@KXvpy?r&@GrW$mk@Qz68P6fp=^eAx9-QE_Kno;6a92Q~_<YS+etGx2TAr-OZY;R?P*3KzF&8^@*Dx{4alW|6cXT$3T%+{Ci?jFZ%ZbJEp^v{{2-@Bwc)7STni!-K<}8h23?5j@-$_8~FiY2WvRdE3hYH?wePb5LC@!k}Em=iP(_h^xw+q{~M3GU|0Fx@)xB6-ldumLZl~9Gd16kpdlYy?n!oqYu*zk?pby5r9-TQwXq`H3%%r6T(z=eygz9Tr%54h=dJA1sOybOLWzZznDwY&wRNHmRZoe~VoELMk07ZBE($jY%kQm_9jMj;$OfZ`uWNNVieFndx3_%|46Cs<L5qSG8etSk7`D){RNbIJW%MfE@@uwz2ld2}x1m*kM2vYh8EW4f8-hyS)|Z_JT$B?z=uRpL3RQ}#y(e}uSW-8y53AZS_nb|J!5&cq-jPn*nY?lOZ{KGkY*_4kJo-Bg{i5QljTcAaDLS@3Vf<Ko<LjI?KC0}x9kX)C@ywCqWT9dfY~J{ojepJl+gi{ZOhXcS%z`^ML0X|i4!RT}TJ1{6%aVpKh-7T!%Z0Bm)oH$vS1)3>R9JS4N6x#7$p@S(w)a5hzGM~+y}k|FC`Z~pn54?UgEe_J7Uum5!u1oA_x%&k%_06oY2SDNWP3Pp))WaK;lUG|Ch|ufl)nQ}C31p@k6CQWXUt=>N6moXzQc%p2?jv8N8S+3om(#8HhjOJo$I5jZ8!kN@D}r8&rxrgd{ldFe()xr`~hs5+3e@X@!q4Y?7+bN7e8JC8(9XGZywKH6Fhyop;;9B?1WX>&B&)QPgsTP39Eb^i)>YXxJI~xGG?-UY_rT()g@cCJtH0H&a+i}r}h`+vQQ!a?GM?goyTcAOCpRW%ll0=gBV`y(x&~_DjTg<iYMfxv{z%Vwg3};;wP;)#blwfXs&*<WO!@Fj_sO~3AM5b7$?A+>F6R!TUnQ`qy<EQWX6hW<>>Y*Ja5VRw$-sstHma&RK%t0l47u;4=ArVJ%>D#1PTnh*7^%KvmWkH2;ZW0$YqO^uYb|Wz0Xho^Y__*t}P_i-{PjUVx4b6x}V`P-|V1W2tDfRLI7cW?H0tdCpWgy>Z1O+rHL50H@?vNsvo+Wb|lt0{7{t0=efpqPV}y1eBw;js$(^>1BA}+#(aDNzw?o62G_s!6>!I%?PgJJ{9#3V%L#jA5^<4|587LNuUj{U4z2HL4h{=s@nUajKib~%%kF0)O5+bPeU2ZB2P~Yx!#`qdF>h}<P3!a>ASYsaqgDvM^}sUMagy-aW2u6px#o`1-&-E;3ui*}tySKQfe#p~J8QLSjgc9<lU0%KOi`q>4s4FizHm23W0&4w%ZiZ)_ag&!jMV|3-E*%CrK%oTw<-nh63_~McV_``K4Jb%?LEGiy_8(%M@tRMdk~5a%~3}s8kLBM?Va^1^*9OB>vtw-R2%9JZIKU#)tmmNf7$)EuYLfU&lR0pe}~mm1<|{uy0NC@2F=F+0*Seti5*wJ6$f-e!of)u!V3GeJpA%4TMsL)aKdv0%fWQtraFoP9QC(-HB0A^^*$C1Y~!tz5717PYVlQc)+)_BW!S7?-Xlqth49(8tjn_!?5nWZA<)WqZ_iutmax>k$4Sj4nh1hh@!g$}eE0DEzeeB<R{Oyf0ytm>dWI}-m8z~ROIHn+A1ds2w9mis;w|pr>dWMOB2>JTC(l3f$t`Y9zP%(O*@|_aE`=FD<FP=n+!CEQbH<nH@#UTdl>tkSbL5iJ<5=LUym2KZWXJTl5s`qUug_zFBzZ}X2VGLOWxi0Bis^pb%0yg>HI|KMt4#^>Xhkj(HEbhBnf9@;ovfeQ&zJkyui3p?`S9%z(e@dZu3$F@GA#YT+mczkh+j~QLD*sBG${#BGMELRX?u=a$!g%Yf;58h$xglhC9#qB7Sxsf%nwX5O&H^?Y?Q83Y@@AQ5AK$LPz9lVQ#0kd(}@;{cWb>!O9T^xjS>)dP>QyAw>?X8ObO&@>P-2t?&$8aA^Hb)XEs!)`}`Rt&T%<yS>jl(D64*4qqd*1`$Q65=7TntuAEh&0#bsL&%v20hoe(zcUw9Dyi_Ynxl?W%SEE&@bZ^;3-2&Ikb2fQuaP4`UDJ*v?S%O6?BxycoT_`SFEy$81U5|1z#1m+0L~o0e*-`ik9n(pzR=9_@h^VQ??C97L3jc$0Drp6|j-F{%fB=K?v0}h4o~Jn$VO}5D%p^W-_AMEStr&(BAvk2T!j)fb0dg>y&PMsN)ih-+Lg!bU7E;GpJNrX`GL{A8rv4Tw#k8L!?*3msNn6XNdRb3P+g)#Hk$RgeJjvG^T3RLzuO$09g*iia1Vf)D`#F*44J~z)sHP^7z>b%a{hZ6-Ex(rR?@O}ZBgE`5sqIS#Z_LJ6EMu~tskbVfB>P3GW%e2bBB^BhuZw|Q>ss-jobl)vvV)i>(dq}KwIVPrc|e!wUb|tw-gVg-69kArym^NsIUQ5>s8;zFK**06=mXs2nxK$C=47RdYI@iMx&8~+ExgFRGb-j(++YE$+1BE;KW>o?4#x)RzZPwAc_$~f$wy@yvQd1~qWk48hr2CUQRzq{ddug1VD$UrE!Imdaheu~-6Vi=H<m``UfB@x3W{dj&rM;=DeO1Mt|XS_^RrEn%Y~|0WUMx@ber5~RtJcATWrM(W}-4K{C+kBy~^^D7*|r0<TKZGjzci&hmdxOy(ckM(n@SoEzdkEmF2oTk+%lc6QMET!$2qkShvMqGYE$p%qZ-k%Z7Z?j+nbGb4;Fly_EvEY$90e;Ibj7K?q}>wa5t#p>N<FHcVLv<V%1M+?ke6A-Wcm<syiTfy2Dh=F1#N;?AM&in_?OP+|!Ci{RJlc&U0|*kmcB1Sx&W$eMQK9RTAk@jXn!IT3gh%nuJD@iDs$WFye}P{D}=>rc(rbLsQW`HhfuNj4cVwyF~Aw2XpOB*9xza@8<u4fpOrJJ%n6Wd+`eZvDg5ct;X}vA`R_i*;V(O^fDlM9G)SybL`@_B#PME^h%#FGhB_J*o5t<Dwlc|3Jksv;3y!W0l^kX1@&w%kIMoJ}dABKh}6z#jlI}E54Mn<WE$3Ys|IPil&Wm4vGM*iu-X%x$uUmn*`c1=-RcF?~P*|167eQ?Vae1i9J_m{4V;c!#Up-lDv0hg!9Jj4v_cKus>$=$v$+w@cTDEIU~!LVQicT3sS7pCGHFKMqTB;SWHp{V&+`fR9*NfB$ng11JiVIs_rehq^Vlw>Emz&x+lHSSx>VyoXyr!VsKTnfFlg@P-^zLaPx|DEP?=Ks|y}VJNHmLGkAsUVlyYZXhI~wQ%&%Z-{}9>PvY8Uf3)^r*1O%l+`HwzV_hs?k%K#YI0tvY+!2oDD|B$X>uuSqPwU|Rp8L%S2bu0&8w(Ed%?t$jkB|DLZp6mrpM1z3WI`fvIA))cMTCJV2XEc!7?0Xe1wk^WSbOlTJ{!VF@25VIRHb10N5aM-N$}9R)ev;pE)`)&9p8kK9ZpJ@e69nw%4o7K-AYOuGg9Iy6@O8XkV*{qo%?)e*9`iOmST`ddD3Tz;@M}qhvg~aFFhlBC})ba(+d!(HocMW(=)p;3cr(hQ@OaBxYp9qs~m87s)pb(0BGphiE=-h2F1vp5i$En>?p28sj&Q>`yF5XBW$g%nM$Ze3?91Z<Di5%F?%Gbq;u@+p6{yX8yRB<#>RuCo=vHD>-27-&x47>CJC?cEO}~6+))iRe?`x}(ER_ET+;k#ldWFqs18OY^0p#QT*Ym{5CqQD0jke36Wv#m%JwWtc((7Ula$*TQ?AN4<xhNZV2RvIVA2b<xM`8$G=mi_DF23|Km+T`l>}?@<T?u5YhtjHWwz<WIsVOj+o5NR&9b4Seb5PMuOTYSme-oy_E4n&go@P0RHxtFSTe5Xa_RH;Z#cX$2=NVf{8v9158_FUc!@dNJeLR2xDK$1Fu$kSTE|(l8JUj8Wct{@5DTk!JflUd$L58BJI)M+CbV~?PLZW-Te3j#BXh|BQSBXBiOvTiPK^Sev6L7J_-r3*?KpRUiR)A8DnTE4UW}s;;IlnT_vt^K8_(+AHN|+w8*f_EHLiF_Qg2H2Kc?P&ugcp!sBvjOZ_!7JOJE37(Htq6hc+e?BNp!2r$XvWowU66arTN9iAZ!<m>Z?DMe+koaAF^JF!c*wXP%m$C1{{{(%N=BKFkelp|8!m+-+G-@qwzXn3ZNxS!b3U1ng>EV(d_mZ8eYpd4nKwNvYF(VMK|MKbu-3H2V}KE}&;NTKWQ0)r*1bw`P!SF^bLEG=&nsq%PGbp~qItp4KAyNUG$^-g?sl(VPlJBOr!xa;cS~G66LEAO%uU5=_u{W<-WFhwe3t`I^Q2(R1?NSB&s$zWssQ`wIml=sX^=Yt)|nW!>1_i2%N4#?fGqQ1gvRt+ZX9<0{0mP)}kHRf^l8%)WVG3i4v)Q?#B@aOKo)sdKv4r1MVbQeiJo5-2Nt1)z0OhrlGR03D9xi*9|v8ckUefKnlrO`5_MU7y&<?m`I@Heic58n)N+9k3}q!7F91;p{BOGueTQ%=do<^NFlxo}`CD)_D<+^6}8@f9H=zv&DHL?#WII)axH(^PFrJtGsK<>s-xfs7)owPQeWsIX%Bzj|J7VvG1Uzbj)bfiv|lOGCX;OueDZSH!ju+>5QlO7Z)KZ3Cw5Yi$-&29JA|>L@n$8EGA>}!}naBy^KWfBLBN#wS_z`^*X<m?(@{kbCWC|k$=Al)DuR1bEj6g@K(^*<lgKp&=~Y<5>RIYv-W%B9dit5o#X%>)MSb$gb7ycff{OpQQcuvA>IPu2n3gVV$fjAV&_t2=gA8P$=5eqQ&6Y6Z|I6D(I&5+gEa=`dwWBK2+n`&citTmi6<P8aoFkphsIffh+H(u)Pn87$?LCA-|y+`cz)GSUq|?LgkMMa_37&fzt7X~L7s*ef3|+fyY*Lb&0qTINAe$DXX!^A+xo+OSN+F%Y{QE`n;w1oqR;;E8Q9>z)YI^Rp4QKPD)v`Ddpf@=JsscmFL=6m?4R|RBr1Gd>%nvWUOaew@kOVy7WwnPR&tDmVI|trppsoIm25vfR<b44<#9OuH?r4|5y;d<gTEtTjIwWH(BXT?JtgClMKPGA2^5K`hXv{xKmNm&H0sVJ%sUwIFV$3Cp*-|VIUw<1|AJa({rSH_i7T!6=@{l(7l$pLR+rDFmM;^EyY$)6l^4g0FTzXqPua%Vm5Xs*%%Z1P&MLpS6P(()G)h~~Hec1FooL<11Ne%YkLvuhrx(03D#DTYeLl!|WxQ0*obj3$*C}Nw{mhZE%a@GQc-aSXZW@u(;)3mgU%cXHzhe3c<Cji%K~h_@Yq&HG{K;LLJvA00U&KP}yGEWNz633WU`gDlRIV#IUGhF~EvSTPfAu;F@LUI=+p^c=?5X~Wb!&1CLwQ;r#BwTEEnb=b_1E7LGuDOI)8#K3pE`f}0Q*~hufOo4f-$_D{aE`{Tz+G8k6*C!rw0Uoc9H&Bmpvct5YG=Fx}|aFzjVBV;ybfb8Fa>7J7yXsKfO3k10yXPpOypW6G;c?#qlkpR4a!i<BBeyjfUyb<HVgpPeVEF;)FryDLdQw&$;$X7r!oEo(3UYod#E@$7}%I#cvFk-#s7UaCSh7g$8IbCc(<faXM^1TzcJmHy^a|42$~`W@8f09{9zB%YQElXRuH1Wx^RM@y&%ZtOs`{oUvx#GB`0pG5;)<MZ$BUh?~?A9n&pAZt7_*3n&!@jm`n&(n+pJBCX)K1&(H5FX_4<G^(0!wW)@rJ+w2L!3|^^^n}mueM~$CjTu|pi=cLqjd5Lw>Zp#~@XQchF@gnCwTP6lnL96du>$+=jF8S6Y)9{=O8g==WauNI_(wA(j>ShBAJvp;2z1*7?cEhGh9oxjz5MD(0c&(`0A!+piczx14KGa4r;tpS9%!c5Ld$ER<u!%+`t)^#Uq|?LgkK9SuZ5P^Ld$ER<+afAT4;GKwES@>w7je+Qa*Lz#Z(?tAE3%ImQ|i#Wf?#CoGJ_JEBW6R%f?63>obi85<pp%B_bWdCO=TWsr@mSH2Y~4!4hX<zGspBe@3|l1AC!HQZH&GD!PC-Z>n(E2Q8(sth=1NGJiU%uRU6QDJS={Utu3{O4eI#L-X7(D=}eFiJ5;;#TZi&(V*E#^4+aOPvvm9#NvV8ikJRr<W(j){S~!Uv&P>ZX1`^;3r=!1<9)es{j=X2e4*f;3QIN(YMZo4O;lkz%nn$*V!uc)nkK^8Upwsd4qA3~Rw1+1J+H)^7kI2Nuo$Rve(%NtO!?k8R#2paEwM#!ZD;;k2}kvtDXTk6j>lO!=R&r6ELY6RHdbaRPlLZ&fVo`!@Ry4*_OyEJ-HUIX7CA}*#xFDD<!Lb0$of5tH;-ITc*fOUc&jeeg|kvk=$=)lxmu)&E?zIro!|6}Gem{7StS74QYU2?U&d|x$h9)e`0m9EyIg%4Bb{YYYPzA}(YtxQJah5u9{JRBt1n~6c^ZE&CiaE8OFS#FgbT&6^NP#j@3lfpI4QLJm+!-me2oTlYb@hNS~xOYQ;Qcwh2a84;ewo>y@1``I0?zdIdKviGygEL5gIK&7(dxf6peupwEQPcXVm0g67o-Epe;FW)&Y%@A{Z1O=z8i4A`3h=J~mT}QPA5C@J<BRpmh=_zi$gSf%tT~NsxyFA0i|vJT;~RT7!=2V%&k!_JkxbjwFFptoEgaF@AE%mA~Nrnje1X_SC#>AKdV#*nxc;Qx&1tMQ-ZB8RDb80f-~d+6UcpaLt6nK@ICB&D=sv+lso<>QF~Jn254de#>|@7_F}~08M8*zp@RXiRG>EMaQZiTX45hKe++%Xy8|OoL_Ga*rcrmNbrq=RB5Tj-J$7xt2X)&jYHu!Qe245@wZM|0C_>ALYI)Frb@PGJg&`m91d)Sl!&gy8>#;Le^fYVK>JZWK|?e4h)UY-T8A>ZTYdFGm}qF{V-)yiYEoX!d;XruVx$h`$fcXCLwWTS4UGq@`qLfCHH9}SHmu(!(`T7QPh9PsmA7N_Uxyw<>VMgSC%2XsyjDBu4?bqY^3S>dzz;v=9v(3D;?8wi@DCJgrto18UmheP4OtH*N>YpDJ-^<N`K5J&OFeL!M6sBs(NzZ$@4zi|e?ziC`nn3UjQ%`NtA^qgHm4wCosJ+%7qdVuw(=YBmKD$1ipsc>mGqK}lI$&6-bZKc)>pc{98Rh0gga;=Xn>7#eTNuS!H1Y{J&czxK^s~UrMr%U6Irmgpq4NKb*GgLvhxov_6v<hD&@|2M9e8B6LlR=g@5z$aU~`_*R`=~mfF7!MZ!(n18cR@E10aaHeRw})V8W=31_NR9r@y7M~d&f7$FRuhn3R4)UZsw+xysdq0jeGveARB6MWGs9P{gYp(!XU+Dg*H4<wa7tVGA*0eC=|YaOzAnm~Q@yYA<nuR-1Ad3z+;`<ngrK~yoW-m{k!zt{~e+Khqx+y_bOY|(xyAcTX&3x#BAvK{1C?h#Xm{U(S9z9;#-B>Rrcj@*#|Q)G;_Dbj{LU0gBN<T?BeG_ym1T1@EKE`BDZcpx><|9*IodNO`a+>x3b6q*ZW<M}@=BHw`3rY^+WT8T=)besWc{;8GeUV=I0fBLE#)yW%a8`$Y&1`lDaMs?}^p0n@O*t*QA<XF}%P8F&X_B~SXIa2SPvF{<41|7MF1bDox3fOSdCwC43bfXLu6*pvf*5xpTbX6o7gY~MD!nN{}3iA?6l_2&g07e3(WYpKjF_ka2AvMjK8%Ae>QBud@0w;ks30xrY*2r|_O))~ASo)eIa)D<JHPs5;^;)^N&uCO%&AF?uG^+bWqxwhjNq<`NvHszsf(H3A4z3!UzoFZ3TlD4xT*@CO0Y;>j83eOB1{Db!*%rOrkwS{J_Cw{{Z8&fRLa?KP9>)V?k`_e4%!uy7ioS<9!$48v!(B5uJf33G4<wx3kwUD41P<bpBiV6qZxx(0?oEr~&r!`0`_Ra&LUw&6V7r-G@4>CU0ISfSeglsv-nlO*$pIdnf7|`8uYL-*Wi5F<G{Qr}qU9!sb@X+_P1q273LfW4ae)2~H)R0tNZ9CVN!0EL@8Y~>idTz2w914*MN}R32>?6EkR{;r?Bf!}EjjN^67!kZV~rt9sTz0`6yvBtvNQtSkhaf<eJlH_gS1{L%;8N&@epXz2XaHiiHhv|`BXQ~FlUld#zjC*F1rFW=6R#SuWOk^?Z}jr2NQ_&nrw6==Y{Ln17R-8WKV|PygMc84>!na<Njl@lgzcD8xFX2<<m;(3qMM7Gkz2oS_uE~2RE}b+L$YRAY+{HRq}xhP+py^s|8lh_&}tc1A4Q$!d{f-H4QAS>sD-W)r^OXA{U-Ygq|3~hU5_fEhaOkQt-6BPDZsWMit=!*X6MU9yOV`Q-^I9<}`oTt(QMoOZ}Hiq2W@_7q*`%sdkNpKywp{#na{O0HOU(&R}b5WR^U&bT+eHFLYn-F{iV`-H{w)I7%nlk@gY%8{51;Zm@E)Q<i<%93nI2LDMaLm9-ar<F3gQN{TD6D)(f0%AUu-5HB9_*#}C-W7u~V66Ra?Ew8QB#aley=Et{O_PVPLM*V(;``nYz>!6J&pXbJDcH|rUjeL3cFt*@zM|cJAr)8>$n#=ih3=&waccfzp&Qz5-(N4=ut%0-ibjr5nOLAU65`SM@S0(<g$Yu0I{LR_?bO>G>-(h?1!6*c;c|4<V+8^>48f~Rylp+DdyeBnwm4@P?=EMZ`n-o8Wi<4}M3!bn_r!zW0BO&$$Fg;&sq<bP2v4RAyy6S=}gS*#PlxBtKx~o-%A>|}pvZ%e<Q`JdpxM3nGuw=-^hqPWjYKfE2Us~L^P-K0AIc#+*g;`?mPfZV%{_7V^+m3``KS^u9r3S6>gh@VWNfnmdos*~w$-QT6VK<Deze(!}k4J=IiFcd6jxp02$Q-9#fg8-db#r<!=6VQmXATe!RN;4mT9ZurMioKh1~cw_@D6(LLAB%jnk@OuG0yg(;*J28pKwRd7Ex`OO(oj6JyGjNPS}Q%0&+K!`_fdBR(%6%$Rj)n*Hz;@DtU$IOzp0pWL{RX^B_gUR07qZIL46Da%~T*(0}qtwDO~*lnmud&0h`M2X@|z7BFA`>I#E8DCdeeSQ>fMmAbeT%$>{kl1;shF<fL*mvB+KL|vz-j#Q@=N(d&>Kn*eTJD9*I)OGag^U7$D$vT~<%1MUOZ|O_J6F>|3RCGotYdN_g(wS3uH};68ONR2YOR|Xbj1W}%OcxAg5LquqtWu&C_VMa87u^<aQ)6V(b8N=>V=yhp!q7ewQfk|?rEt-tR*O%~{*6H-QYfFY!tuA>m!XkiCBr3KAGdS>&OC3jqs=^oZf23kWijfR*Gyz&OO%c8$!ZXbV>M6PP1?NImO?!W=E*=$>j1}8Zf2v$>CfWFu9A)B_l^{fL|o)UXrsq0#uYO?&TIbCE%6@kvv(zb;YIN1jsanp*AHR&XQ0k7b!=f6j@d4E1&lB<J&qRn8rfqVK<f6RK=%0a?zcE2q^@&-6j*C5Z<<-ztrz9HgTxUT_Xf6yVKVMa))HIl1G2JPj^DuS;|BEO-tyey+U2`>U(PRnTd(Zk%In?QxZF{yV=r6ydPQp26}(Y++cu%{#0=Sk|4!@d-X{I?8#kQ|#nluBQiL}oiqDQMN~|QJR`eeSI-yK?CVn;2r7g8(2e=S}PPGams7F1fMMql{ld!nUbC`WFkYyMJKl58R3<kUs`9A%*rxh=0io2MGZVH`a5xrV0;2V1XW!*L;U7yFwRoTK~@ACn9EK%?#F?Y083J0N+{72#AuKAlrQQwwimV=5}C7XVurNVwgG1wzP*x^*r-ji}~5AhZxdA6WKCN*{#5VPV|97MVf)mr8<k?BT|a7!O|mF-c5*fiytxOUaw#RM&c+OSB+qDHW1L*pn&uu64{)GMA2{0HiN6#kQNc}S-&p?u2u1QW1_)CtWLR)A^TQ$W&}oU;T6^OA3Ehe50v5kD&n#QajQ)<p&(HR4xwA$s8uh0tK}&@=t&Mn@AI;Dni}np@KuMG{r&)pQfX7TadUBdDgJoCUcjojhHdFJ=>sp+6QqF3#Gpe0rm1cA6lCCl=Ar3GvgB1|V&N^X2vV-}yNS4<pcWI;Lp9io=4${Puv1<XSdid2)M9ks*?X+gtJCw-c+DPv6Dm8OCD-NDJ=LHBX~t;8Qs=^JA!EhQDA74bA`e+=+?A=W=dVWb?0Vh9ZG;1AHAT_si)SEHx~RG;N^`j>L}21u7+a-aT&(x%?;5t*Q4`stF`Q^+G5nNoeX@lE^|tz|So*LdR0F7A5vY2_u*UnYX@b0e)49FQ;wG1shOrd?4Vapp#q^_E|U(e4yKvMr!wvMDs4K)*L)46`pKra~>^j5rrqHrl411@fz(u^9;pShq{QEE#^W@%BtG;N=733ksH8-B~GSx;iz{-h=O@zdsptyH1G5g=~D4Z>>BL5$PzqVQYBiB*<nHF9RD|76?ZW_T9KZ<%x+cvg9`l4L>6ZMvs;rF_h<CTt=i_|k$)e4#RNod;lxBbCP7WxJ-vX$q;u4cM`@28^5AikV_&)wU4j}3FSBY?HAJc~QmVYuwKDmxO|@Q!r2hEm_BR1~1}5#T2RQ5vHgMQt@p0$iBL6s4Pbk%Zf{B#@XlEI%{HYd-bE*|XeKEnO1Qt&6Q57SL9AP;YFlgebxESs{Bo5P>D#JOluUylos`9i3K#U`yc)(ZuI2I%=!78OrU@|6+=uc;#G&|5gv^)~zTJv_OR8$?De7?jwffS?o7M-SBiLew$;~#!(<zF8~(os*!zhhqhX;|HM?I-cEN%q(8-IL0{6s4zc(h}4KJ!k3vh701q>7w|r_xb0K%6YxKbeWP-0(g$c<E7HvJSF~%Jf~-Nj_8{c{a>axB^uFtOFRy4E(9Dn6P$OCivLo=kn$EzXd|Q+`=bBLBFCVjDP8lS#^q^8dqVj)AGNaXlN$vc1Vo?c|JDjmSm67p5y~IDQZT$yFuXQbzdn5(;nxv<9pP6BhF1!PR|<w#3Wiq-hF1!PKSGoCm4)Gzh2aCUFd*57CYZ=1E#-j$E^E>G>U*YJV`E8CCS*^juLU)H4jqF5N0*EY-Y-ZQ{EU^^&-?1xIpk;E^~TY#^D~a*>l_XK=~u?D3-#3PKPO;Doo{UC_DeG6lMa8~BY%mkp(+iA<7wwa4>OtrKcg_PE@+`fZq&BTlo!8dPTAm>EZXDKk+os*ixPn&*G7hy%|$KZiRp(Jt~IIhwiy3u7)R~~wZYHn8yaR+DTaDNFi}W_Czguob^pl0(-e}l--5xxUzi~$KiMzl%*4krn~Dqi20!C&@FSOYYq@o=Fl3tugDEV<bFv2S=8U{^HsZ&~8qy_N=r}THTp`$g<gG{9wI8E?2-m0$X4K2UUEw?qC!PP-e)7c&4)L*{^9WPJ<L^$FbcMp)pOJH)Pzm^_SR2l%rd>Kc!${oVXN=lDTxZk{cG+`|=aIQ%PDyZ?`1#T~$5+B7a*FvyUZhvJazOCcNg19z=Ogbv^MmJ%7$YNt3loF5Us7dXCT@6?%HdfI4wnhD|C#4@2Rxwl36+%xB7JVrJvrQ=(nIJ7npD~1l3(#_?J7r$t%H?h!sZ?T+x*}mZw*_N>~^Y%uoG8U4kGqleIGtkYc^YN^GWulrWS6=1MP4m`W5qzaA56+J;3__?5@oJ1KvfUzV1C6=v7+=6H2H`vj~ccR!c|cJxIbal70UCUw3~66(v9fBB%;rP0>J0uun)k4?gido4YoWGi}ju6&hFXv3E7BMx`59Z&@R)+4V^%C?Iotjuw05Fle###LF(wVM0l+N0&oSbPAf3Q7sBLx1m83aac<e9bF>Wc2?d?P9*=B4c9%&b0VhDnMDY`aTTF2k;tliz@bL}Q68QHdt%WgNGMHPxvD|KQJ$pvG6puILk=T_Rp7`aoX4{$iuni7vukP+msc$9v07F^Tb{&6#PA=YFbWciP!$(I)F^LMt|2|{Anx^s?TigEJgf;))PsEJge;&O?JRT&tOz$+QVl!XFm4|GLV?{u0qkF@=vy~;a4p9TcadC7DbJ|C@~pK1&DuO)Ia%*qd_dJ)kmcq`j5jKEu{v5Uv2{f-B(Sq(9X2)FKNk)yn|f{lW3}dMs~n=(%aS(FdCRwwwKg{cTCLZ~+S4aLmL0|Q?bL}r1jD)Eb?>`dPE7P-Mk%!mAor8#n1>cFzXfjlO+LN@d`%r@b!m1lb$vFqvkm22gSFZA<a!ud)Hw~PT@+MO7v6LLY@n<fRF*^}FtB}lKpT%2iI^`BqDr+cyv?)h)(I=B=2Ln{OXKz%Ps8?37;1JT^1n=rK^}pA);ix3i_WSoG27_(?)=moU+*Q3&Z<1|d%Vvf8R%n#+X@=VW(f6x69=M7d|Rt6oW<-4u6JH?Kzcen&Fey4@)I`=R}t)C6NMxfB4#A704$*?tuh-}7GtGhoQ(b#MNv^VWh!P@;-g{lnVd2a*l!_2SA~gY-W8J!x!oMZbihKjXeij)OQwI^w0*vqp9M$6Pr3&(!gLQ<NH_UM{8%>LPAW@ac&IT4Z6Tot18|Swj$j7z!lYg3Yj-0i7c{w!$P1PJ`INS_zI9@X8H_|N2?6*m5>1c<1uqW589H@+!tUjtkT_;N+hJE6ytnsua!AS7z|K@8ATsm9ziYIk`Og@FlDQ<+2ON`!Wgwgr^ezW255M=cBiW`ApPFOiowpy3-V~5va0RY?-Pl&9;A)qL`QOU(zS{cw8^omM)7){sAJBQfAF*vf=CXC!+FLmQJ>zBd$Tr;9v!Qx0MxC0dotO-zCVmqD)wklkVA~ntyLlM|u3{~Tjb3ln@&TLObL`i|n&H#~jZBP+U^}jmhXgQd>MXQ>V_{t^D8e*su$jCCN&@F6(3?DGJnc7p$uJCp!=n%A+oKYPehcI_XpIR@t_V~V-5Y*pi{?iDUP=Z9v$tTGAjG{6JkQ#|&t(s{L0Ij|Qx7aJ#YEJX9MkW+pN;8Td1y&c@&GeZceLf6c<Ma?hh(9M!XDx+(tnV6ATPc8#@Eu5-&pS~#veo^<m%98fosw7x6YIVsdaqCQ7He0Tooo-LfGW0;Gnbb)Bpf%{QwkN!&hPjViM+8s&yc8Cg{Qr+*0s*?b@CQzWf+%RpIOGCh#|8oIra!AmQ1j04ue{aa(XTG4Q>?52^GxIpa$R7LT)46O<Y1JpzJBzk(1fqEYcy@2yKEPpQaZNtGgEEc+%1T#I8?`8+kOlc$bK<hyxZWHX3Gpb;)Kj?^%rB}ZEYt`omvZ%rD!W{ena^KW4h=DYM=dXL!&%nL5h>kYP@eOZA<Q&R(2Uk#*!;q(GVzk|aIH{ynOrr}}>Bu{Dp`b^xO(OK`fmxXep0?tN_8fm43O`$NvD|>9^av%V#)54>!Oem%@1g#3D92!8v^Vfa1EI&-{O5_e$mcuNkR`acz{jyS73VfJX=@$%g_Odk{xnrvE<EAdeMYZNm718qB=~n=l1umrk3>!yRi<XNSZY1$(^@iYZxlQN_5lXEbTw}_#-aHSbpbCZ(w#F7@pbv!U$$kE3o*Nh4FXE!QrX#n(kie!6y!jOu`6vvOfW^$yeV6z0yOHaY{uoCb!*F1CG@ruV8Wbt9aXOns(2M0?PaZS4{ph%DNj~+3=P|dSD0#?_5w9SidSDB5X_K2}ZnsXnGA$j890KjtJI#}5PyquR^0$<?5_x4fZ1v4(<R=xo@YC4Ke}JF9zo!$iLU?GbPk%CBd*OG;54!A^Ge}H+AB-LAhHL#^EJ#OOVE(!27G)e)mwq>F@NBG)3>fkkt-PH<K)n{!PULu_L-5@@w+&_qH+e1|a&(zv$B@d4Ke%;0!>U%mPDKk21VS*IjVDh8@Q8Wu&k-@+ItGPmmYBR_A%Z!HqqDsD=7Ejs`7-uSeg>hTSgs(w`rkhZm)oX#8IfDtowks7OBT1_N-OVm3b&U1Xz9te@ke{cxj<t*(y}r{Y6$f-4kGRGbFzluTfb<I^rw6ck2H^a)8!<Mg^-g$@rtqY2<Iu}I1>rYvVXjB(%s5O+|JzOrhq(8_#NVD|2V*$X>1|?gss27{|f1Rg>=4xwO*gTj_~UUzmD)Lr1MKW4e#;sS5)UKs`C}q`HJd%MRmTSIzJt%bAn~oF9CMekG$w!h7|pjz)qJ?AiO28liOP*4qOtTf+?_*yjCK)fsdO>J!__=6ul{3Ig=uvFmiJYr}G8^4BjnOwJu0%AqNvrb+AB9GGavQ>A@)kF<d_9{4ESce|i|jv=+it)3=POV15B*JkjNvuEZAx`VnwwI7}b5mAZ|mw@z@3Wq6TGE5OU?BKy;eoJ(W@*Lrq&gf7eu_Ew_A#q{p<@>W%di|Yv|muJws3)heASA90BvkN|f_|6}w!gb-_49qDaVdN(pF5WfebLJXXUbGnYq93)gqJc}#^{y5oIt6DqDf)PKQ4MH<^A)y_6F?wqPVPy#BPZDNM5N9XupWaW4p*U-=g7Lp@Nd`AlJ0Rl<m}z?!F;UdkHdAO=%ud+r^wRzHDAI&o*eKP>hcWccLLS3a57BEy=2-1(_ucHeq{bHoQYkHUy8EW^-Be}!G(L|uYzE&-PSX-q(8rs8T9d4kK=5~#2IX|awigEk_tOPKc*#Y(#>Ybgpl-$7u8TOW4~d}f05+=r~F@~6{uzgVtQP7V#a@Z8p|;!f5!)5cKmcUS{K7>^K}P$Aun>SD*2l7i27i*Pz_(H(sVWsgFT4l-Kx9@#&Et~m49jWku)AZKVkCgYvhU_?%ydQHTdJRKijAyL?kyO^~UmS=MO}=?%kDxjnlG>+xTu7+rU8!W%Nicw0KJod^-JVZaCA6E-mOn?A_(lINsBXmx05oi$8qvUFY98JJsTc@Uknpbyo)P<X6nEocro@u+DGdo<uX4wqQyZmZLog({+v;a`OG+8Vb2d2<1U4Kdm63msh?Hqi|X(G+I^pR2)yZ;YVsA4M}Vs3`PxE*xzt}KBi4fT})pG;$|RJ2QolHN#4sS#PkhR^}iir%I_Y;y`L>mBu^fzs0Y?51L@t5fZhlS*%?C2@L<FJi1h@vA>0}=K@hSHF>g?5*%$&yq_Z7UU9}PNfE?+Y;!@;!-kL6&oi-mfu=-8-ObkaW%l2f$Z&{AigSU>lNC(5q$(beyD27AO#T${L&}hIbNWYB~X~c#qNF#kS>dt}-fNaw+qk-Ohco4kkGefu~ju;EpCf`5?F%P`Qosf7j9l^kqOrs&Dzo#mCwStJA|A2xr5coT*qUSMamx3~*(g7hE3#Ee;Q!Un291PagjX`!#35Zi^h^wRIDNs%q^>9bMm0*$wBv>-?DKQjk*z#pGp)g~EKy_jqZk$91C`JG^8PN*Ur6<ppAbZ&gw86^V$vEnqA!cSItS8LtIWW8x=W8N#UENASy?X#D$a7;2AHTHXpbe<ylM@?UPqI&l3o1I1z+d3(If8@JA%-MIrEU|j6KDn<W|i}PQ8^!pkx)OcKW*jwoBpc4%rq;-u?n<}r#K2HW^9}p)r-hvA)%TD^B1_33sLq;U5uWzxaw0=Gan<2+SsRq_fPO<>wjWb%*HttIxxm+raMJJMXHw#>S3@*uVqiGmv9FUYaA69$GxvI6YY!9=F`$hYD{6khXuP`K{6`@W#G)~vPIHTOglw1X&$TtKdN{(bYe%&KV$yWV|-~cSCP|}jE`iHHSe`8XD)3w!2l%2j47^6HB=DeOe@wFT?u}L?Of3rrDEAYp}Sy_Wz8N2u9Z;ey&4@q?&+kC)MBMukJBe28$|#u%?|HvR$v(o1*&cAd5e(;l`605?v!+lOR7eMn*4mvb!v7jAQddKL5plvIuJkFBKz;(N0jza$o~nS-YM!o8JvF({J*?_mhk`d4ETR@1^(YaZXug^Vc>zKZ8*D6HEPE`0L<S@tpJV@RT^jLvKxT5JCNFR)(ueT@1iBpoAaIk%snqg=144aXf8DeJRzBZ*`$tv;nN!Kf9?azEY7H(TgAGg^Dycv-WEm0?VOjLz(jSS8|gFb@31`=QUqpxn<fdx0h<7BP@ZTH%=hNG7RmK|@M!AVuF+4{J1Qz}!=X0HSvY30boJEHAr9>kWH+UbD|py9TUY%%A9Bnn=yx(~058_%u!Zh}r}pENW{gQaIP|<)Bn;=e4|&bBE3w0aTiawRS2lOUbe@Z1m3cV*Kw8Ohq|x~%FD4r0v_`!vqn;W&Ck7kCk5x33Zyf&y<uDs`L_+trk(4F2`h3P)ZkJ)}oAHAU1TC{G6ffMI(*i<3bQShHUMlmq>E}O^n5Y^Q&S(5{ltg`*_sLSm(28y60$^f5&L_`)@a&#Q$Rb~Aue*VJ(+N`yl(?~;9~4{VgYPXsL->>5Jrupyz*+*E`bd1PB>|f8+QsFnaPzWCl>>kjvsuftZ~vFRQhQQW%V1=rk{>vq>X~7o$-ZD)AmKAJFDovgvoWp^LC`%_a5kEnSo8(zQ-g!4A8e#a4MJMp6{3R!nCm&q2TgI@irXXn`DPmF(oS}Hq&2@`g?d3{qiYAo6wHI8$L!ng&$@rt4}XHh#`oU8om!y=8-3<sqgz40FXfmE(uCZwp|7y^hb?sx$Xi@fQ?{+e#P2uxw{0Qz+Ck^Sw+&d0&CKM32TH{!HZ`erYwHJ#(_l`H8w7iOLf>vaekacUV7`AKsy(d2Pe3>(+~lzyAPT(0(tz5*p1ot(yZLw5a)^((bK6a5T5CG{_Cp|Nv)|ph&z;Zr=KkMsze7%w?DpQ}AIH|{TTuT~GZ#}4p79YU76p4v&EfzhNk?9Ec*MOV|0-*$lS5qXM42ythdq3iEL8sKg%vuOpkkg~o1?Gz)U&&8&%ziaCz3S^M=w>z09ADQ3rJ=JoD;VWEmBDjw$vxcZfm+3xungtQF{;E`ZNX%44>JD7j8urA{8>fr5s#hbPe8WDRJg&*vZEUnqau4B!?%PFK1(9YhXZ!c>ZaPTCntYBbMTPJ0&}S^@5gh&znqzNEwOG5mx6r_wI|wd-LhV4*nf4Bs($LyuD+O{5xM>$$#b7-q7P@Ocz)9NFJ(pkZojtTjSrsBqA}U$nxFdA13#^K<}34+;k@Mb>cSR$mo0S#qTQ9?;51RNtdz1@z6q~j_!1Y(jIMDKxA~A=QoCAN1L=}Pw+dhL>Na)jRXnm6^$qYW;(h$c*Eq!yPEav8u4AEa@SxP5k_b18F^RoR{3m@VW3*fyQJ(JE^<6(%MX%d*}of`2U@z$B}KUkzU{me*x%XfjJTcn`t=VXSe}mWD&(y?vXQ@=pPY>bH80T$ltEw0i_u8hWoQif*A*E_W;W^MSia=6(?Gd}h35?^l~3Dg(Efs(uYf0~fByR!_r=YLoT90~a|`izH4RV?y&0T5KqRKqJ?~6wMXn+ov|A&GXiM)s7|z!|HN|N2e(p$L-zUpDAS2RIA}o=;oQy*(Ip<|>!o2h=8KZ^L6qCd57H43KC1rcPi4ge}ImtbYh2r(R2YaL)OYVd@>nivz|EK4M*ZQu4^+X<M&)Xgg04SlgxKkhY;8cssE2zm|@yqUoM#t}@s)0S)vk4CsB{&RRS_y3PcQt!52e7a!QBpy~%_;BKCo1$dM4{kEAO=}skz)8)-kQr~Ar&__I}2fJ5NtpTr%f!GRglS1A!p-DvYOMHP!sBIU`O?`FE=d(Sooz$LTij`8wv?E>d*q`RTx@jF@02k&Q_-lzSQ8IRdO2&DM_INR2d;Odu-c#9)l(=i4vQH2R2+O6}Q}{YIqrtOjq|BF8N=2*#dZ=)5q4z#R9m291m07oc%4^2Ll{Kin6-ymS)_~rvA$J9jAU+&iibE8fK&WVw1hidw5}0Atk7pX?Erh)|&TV#^=v!OBy17Y2pDr1|)k<qvg!=B;SEm9azf5rOr)d$NQrM6n!^W^~^6YxzNs-2O@P81N17(j9=4!N)GL3<O&X-ag%;??h3;7S+yMCI~U(bHkxJK3bk0%6{@_odDH9Fn#2IFaLYSo{<6VY!L+Z6o?h4SXVv4Vmto$+;FN(!yJ5FuYRC)@Ua4>BB?i80%1&Mc0_zP_vetC)R{5>L<Tdu>8Ia|{5`s*wzvJfFkOZdVF;VJB1E%KZ#bVs-Fn-{i$+z_e(-Z^!7hg6z@7bm-CGh#|41kB#MXdX-!NfwtaVis(9#OX{w%Gz7e7xUZnxhO`TB?F)7beexKH5yRY09p|Vw+VHv1uBMd4`#c<S>%BL=!d@8he$-?HgbVIwm(;x^PsTqV*GZ#<^AAcxAxz#b?7DSlZmJD05hb85{iGX6gXj9Auj#Cu{cy=YmD?nv&L0wM@#26A`D02?hc$G@2<S1yhYeT5rc-4!OKuMcsf7bf2muS!9}XXK6)!s-j>o)0(&;M>f)CGd>^?<3^~CXA>zh0UU2+BaZTZq8PCnAz($xo933zRwa7n0f?<w`Yn?w8bwFKBTHg(DkH{%qZlg_Ad;v~i!<SFl-#SOK_+=0(I(+AoG^-Z(ku_Zw9;M0Z*QcQQ$)oqW0P#$q^9gkDNl)d#S_%ioU0E7?M}w#$BRj$)KYC{(@!pK#R`sf{Wc)z-8R83JGk5_!!}5FC>HG?i3mk!a?1F<&WIgD!E#1sdvy%oB^As-_m$Drt$r7%tgx#iFZ^#lt7rZO0c6dZBVy`%)l&gR$$y){Hx=Zn^SrBiuz%H&h3tIycD{*Jq9YVW0aaef4b)+n(56CV(}GtFX*?E!^Q36<cTsAsf~SIM)vy_!AMu-rjjPEYsURrHvw5h?Cu}JVHD$;#l|xoXxJ+PHB|pfP0e!~<{ho$z;o2(Gm^OF~1Y=zb(}2_B2h!VUXe`?D*(QfCEsklJuxe@qG<=KA%e<-<2|)}6MkBvPhB4YZ{Gz6@<MG3_J5UD)P|m#SU+&!<SRvzNs*}x8Kp-?l@}Sbw>*-WRczX1jTIqHYC>H5o_kKkm51Kzr4)nB5sxG67-I%AhmROBIQwNLIOIJ5zWGFmhFIaeblmu$EayU^H%VV{)7^-7S30qFwuEj0N#^Jv8E6M}yQ4BGubE)T55gZ@5Zzzz8Bo0NAh}|Pk7?_(p@I9{~J9zoXv|<%4|G+Jba!tQ3zjny0x;GnC7(y|gx8cPBKIJ_vxML0Si2xsYV`RMFKftHMwyCZM_>J$|rvm(rqK1zI_|@c0J{I89w=B2@?%RSkTnzA;bep1k3)@ND!;9H5ky)`m`_4&(+@k3x0{o%4sX8EpRpkjTV1Um(L8^D{=(TdJDuc_wE-TEh5ayRiA7^3`gL$LuQ%bz=$r#_%>Is3#<Fjj~Fuytr^O+`HRM&bkFnz)>fB41cQtaJf5u`ivZUsKgSNFh_*}Val3bP(}79rY?U>vEHBBUpr?O}Jo*bLmk)&xiFNf5ybKL}H5^G85s)Dk~(L*&f^sd!eLK?5~H;d|Zqx7?w&7Nc5IN?|AgYzVY~KDJ~4JUGnOiWR4P!tAV(_C=tnD9X&8Xndx$1HexC@mjbU-mBmX-5x)3!`nX4**y?m(Qd_)H4+ntaDFrY$!87!L!md6r}_X~X}rg;xjByBn*_!4Em9PWcY#Mc`Y%|j$bTRBL+iuHxd;o1pMEIXc*QxZ$(aI@sUt@E;Qcq%8FADH!AFgoaA$3v%A@4_3Enux??)ntjwo?=_pZM$Ymu6TwK%c=i|0gugCf9#x5&en^5TvFUa%3Vic7>(EcLqt#xKvUCKZ*&n%NG7KAj^fBeWg8+(JtS<vc;8G^k2!)Q-3plmf{F$~(EUD`{YyDYGX>x+kkk4qWNM54tDLY79BVkw(0dVuNRej=@UoNWx+b0!Wh#EVHdUBUSbi%B}rSn&*0oPUdT_Snlf!|0cG2(QvWo+z1XPuB8Z_=a@`=l4zD-KvIq#)ARJTJx!ZXE>Y5;xaNi%0e8_*Tk0|tl%f47Q-t;8Vc~T)!Cdi}gzXH9-ZpePD>6_H*s@X2?U-)s2n-MNoaC=O*H|4P`G~69y)i>!2_ch#8<K6vHW+<PJw9MlO?4!1RE#Sh4m-@s&WRe$-y8iL5T5PY4GCLZ{vpE}uFoL6D6&_fFnGr5hH026T0#p*!bs}vf&J`n{J@x8c*J}en9w(VPdLYog#qOLyYZieqOMqgor4~D$hFt3h}`Hr5q4=yw!>g*^{{o3B_~cOoO8w8%!44T#0~8@|N6avpank4)zzN!d;XI9U2OjGi@Y1V>^f9iOp~;MWO)51d*3dVj*)7|%pS{C)vd8PBC_3s>Q{uqb)V|q3|hXBo^>um-4T-qyL5xiJG<XQDJR_pl0(&2zJWAwA%w^D8f@{<I$&z{G+7U8Mop{@HaI!c9Xl%wDFa=xp0Q3;X$88L+`~*Dp%{nhZA7AZ&GZyaZK!pASCXZud-3C~BDfVwR2|v(6noo>Ral;<anBXV0HxC19@IrZ<e7d>C4NBp<lLA3!F%d_=SXj>c%R&RpyDEx8<{$>&2NlVO3OLVf(;1t@}glLvJvnI0gnVteZv|xh6Oul%cqK|`()5N688!1=0y#h|3A<pWpe?m$|SK;4T$Q>h`ZOxG`4HyKoE;sCPbiDh8-H2C;(w?`89lTKZ^I7koG+JP@wcBgfGFki35kCQ9OUK=opV@a8rv)vTv}jDW)$JLehr*r$8ol=8`lRVh9DU$sCC7=V3(JXXDKinVRv`6jQ#`g;5<^2R5WwR1#^f+dW-Bf3J!OB|$O$Ui+(mrh`7csGLj~$+igP4CC)Ay6K)tOy=ZDI*Z3wX&O&I`<t|9=K=aheKz|K9Mt{uVzr@QDpkH;6^Ff7v~)FYv$P8keHe2K-5LWN>PNh*7`lZqV&fjgOSb4uy-fx9$;w`~W!9v`%^wF}4(W&q&Br|if2T5IiS3T(v7Jl9`ZTs{72CP7KnCn;y<Wt2n<=()VscwRPyt}f;UG5Q;=I_*f@4BFVz^${?U!|3iT1uD;<2=|5Wq`z(T+tx`dhl;IMN$r*eSp8R9wi-QCMbUEHxaieuB5xF_ltT#|ppR0cfG#4JTerlTIJuy(~Mun_-Q|HZtr@%rCzi&uLI%&v-7@<9OCgURdcEXInj|ZoJbFq3h%gr^>@TnzYU#0|i$_8@{Y&Tlz(eI21i%ILhw=0?i7sjPFXIS%1}m=AXkB6@C4Evg?Y=|C?C84<QXvG|!B59?WHfOCqlgOuL99(SMUSEu;XzJDHbzoq*Bm3T77a11q|=fps|N@A9^>LLOZ-`NKWjQ+WSD^9~t}1_Xx);BK~%1t6FoBi0fX-U42a)DMIR0DpnY4zNOSZ3RpGwGP(fp$ejs<-UtV6{3%nofFrWvQNvd6WI45+XL)O1N=&aTIxWuwv+;Bfiv^ZepSP!LQp8f)+@$A{Bm{Jm^HpIY&QUYfWe=3yj7&wEeA}a6~ot<h{b3nr_uvJm2n&=S{#j2-YV8t#_2{dAK$)wYuJ@l+0Pc;Q~QGD^U~POfV*_EJ7~YP-J$HmWnVZ+?`e0il1nf2hoAncfB$OQZ|oNBvX3@x5C<=w^QZTSuIv$Bv04rdI_^zWuV}ba)TcWIQj%*n8nvT~5y~~wYuou^lukB?q}7JFQXLr0d3I1D@5SBV9${)$YGG0HunO1j<QbKY!+JyyJ&`_S!<8T&Zv6P<akNIjF?K1B+n)VB**h9mgoAjs<Jij*q?q=Odr<2_d6V^Xez3N?V;1`z1G2iXB8LJp;%5EmW}%&8gLFdvd7DRAOk4XY=KSiKu_@rfww8lrg7z#28NcGKq5rEO>aKnLJ=Q5B+466_S|y0M;ZhFiCZr0DPpNtUgG4QuO0>KK2)tF55L-UpMQ*4f{dy?nx|VSfaOzxksY2zl7s-4!a4ib^h$T@S_J)u|?;B!C)~9JSi<*`2grvt6o}}DE^QYAW$V{5>DhYTCsU<`sluf$xh_4&Qn6OP`@>XEO)~h<g3+UKR9@N}b0X*|XK@~+s9Z9U=mcUYXBH3@*8<r;S?O+Gz3qt}>IE7ZPD_zNbNY}4R-Pk3Ge%*e4oF1e6m53Oa(r_hLRsVO$_5B2PF@&>sw0%bssgq?IvOn{@UzfKkuyivD=S|+TW_d8o2e7}EWiHU9t>xZnSPQKS+X3?4m%n$Q3<9#7fm<r8cYsAyK^C(x!7v+19CX`+^_T&nG7U<OEnZyHm+~t?B!nj;A{zyM$N~YqNX?er$~84!3FIKJLuvNI+D7t_O`Q}F@|4EWktsBW6BrGZXCE1z?TX$xwTxtm8#Z#Q#?4xKV5@3SK-}<$u_eHJK^}PG%A41&VhMuH5H)Lj82MP33uFz&y6sGr&&n;KR>W7%qc7&WR#K;|1WWCN<Bwmb3kas3R~wiebFE^pE2#rmf+cr;XDxQ#|HGFSQ-RM)FWl}M*QI6oj)dD&`7T_n-7)`GNi+nTTKxz_H(S5WQx&|y6sfLO@LCouXq(V!e7%C#jTO9zF6FD`yK{W5ZLEIH3LcP7?F$Qc9rDvhthRZ*j&Vl;nsLXpT9PLQHnKceos{WXw$zm*{c~}+gX@~>Alys6Z~g)ZS7MwWr#k22uejgw!_HS<Fhl%61H{^7+#-v&*EC<V8quaZ%CN1FJxjpECEw*$bTEKzWePxC-aBjbA2?f8nc5%RG5KnMzpjqM9K$w4*h>^fwKd+cd<N`vEzku=?mMXq!u>Qn*m@9vKMG>;|88>oVERUHu*>98grb4WZm*t2Ib|_C5ckDx((RI+;Vv;JB~#+Z4l$%&c}Y0tesDXcNmGlvw@*$<dVpWs@I`XlUOEs?vPsnTLfxuQ7FBDf!<7%NmW@j+oM`BN(d<t4wck7gc6Xq7QlP@i9Co+L{~%>`6%y^Vo%z0+;X)hVt<NxbsP7XJ&1%Mo)t_*op19D25X`FfmvEseO}Nk<N1S_2Xx9Y~J%iQ<VuZWKkWO<X^u#a&XBSU9rcu!O*Rx}zgFW9<wW)0uV9|=MC@FKWaohw|Xn-268vfXVdd#=wCmzugoAF9qYc9^SYmhg#>}yn0BMWFqzR!D#_uRU<W>y?~YvSS$uNlX6q-Ur#_6<|rY$Zlqi#Ac~BQ}3eMa9-xD=}P>v11NHg&SLyR^rYSuhwFn=&ASD+A=<F;3N!8pYK>*q);%1GzZhDaO8!(54TK|D7~G{yIK`B{HSy643Yq#DP%}|_t#&%&A#Q@KL?uLkiKIuTXZ*Wrwtpjtq*`3#a<vKq%C^(Lf|}W-#2GdKi|JK0%%Nb0)XoQ+u)jk_<BT~GIE_jr(6bkeQTIU&?$VF6x$g*x~F@*rRUTjf@8?OE5%nZJA_q4hoY82nyIx_bf=rqtqf5<s2b=xzJwCr&f>OhfuXjn7?v&Q)9ydM`(5{&i@FlJ+|*o1k{!?97B)?kf23o|Ga`Hwemh{^`A6?&F-IsA7Ak?(j67I(s2Nx_j-nwE?wSlyI*gDZB7zk~30i@yTj*L^FGO3oX<MQa(f*T6hcpLM`6g$F|3;cG`Q083z<~NP>;p&uSi^7}3pc?+agc4)q7(9ir;o<&k+@1?nb^_G#T9f=yR0h<vq>;!?FcGoq@HJB;MF?=sgC6s-xk=aV`BseUQ+(CyC8Bhj72pl?;>J~0zE}@Lu!h1u%hRV@7+4~T2Osc2mcH1-}l2$VP)<q^EdpETaEIkH;5{%6_D1lj*;-;&>l&S#GdJV$~)3ZsRbB0#pB2(gkuKv@Zxn9d>p4Km3D4Gt^sk^h`V&)s0=~@L7YeOYizfH%AU>dZJ{~3yOoTfe;CV#>L5ndma0yqyFjeI^G!v!hR%E-zf|Y#Zy-ViEUEX7pa;Hka0I@XQeqzO8pu>nz9#Wa`QgC{e1Wt%+XaIOrTh4+FqNcqtG~l+Y*OVH!f{r74XnK84d=6Tyn|z2p&-otGi0wB-I`X!SUdHh<;$oV*pqIE1K+9=YW+V}@(=m=&qT{p2u;ZKm5mpsR$axO$44UD7%)RxXWgM?W@xj+Lrf;?6{}QG(XHWm@_%kB!P5)rTR#1oMM@@+23&v4d&??eax<88@eUDWetmVDcM&lbF_I`5vQ%)V`IhZdEcntwmb<nu6ATYyxTUDA$h(q(auTbWL`=Y4*zvUb$9i)VqhtN6FK9A35?96C7^37YWV34Fe317vQ?_U_>Cp8vHJN0OIKt?Gh1WBGPQd5hnHTpU{oTGak=Li)CTNo@?QO%@Z2~YcGVmLL`5^^HcrgtlTGxbjFOAKHIfM9<D(wFAVBMw@EyEi9p<s=L2k1Lh)bZkiQbLX01MdSkR#pU(j1Awxe{srqaMBJwBRx1EY->UN<-^ChEp&}*+?Ew+tbEsdkvuVnH1+<R-;>qY6}-GBiw+=zJK=_$HUZU!V9X!PD{vPVoDlh2_j!)=yeD)cFWibm2X!{COR^6?>_;X7EEHpxj{c3^5dW-ulK<Ws3k7cSFMOceB5&T;hiBcE?1^=Y?oXt~<Z(~8BAnibFuxCBx(RW469^QcBhT57-tZiHk&VGTk_aGm((u<Bd-QdkF9Wif0Lq34W4%}g?emvGsm%gk*0|w&?w3ATP*YRol-}VYt|1RuKk~KI7Tv@tx{=#$(Ty_y-Hu+vGP<F9BK<W`E=&QAgfDX}Q;81*;kH%MQxT?ZhKZ%3Q%aS7pT#)YS~amPWQ^<V0S!VD;T5=M`TV==*~MTwlcq6<){@(32)a8U{t@puA&5*ld5m!myCQ>}gcAqicP|y~|HtmbhFQrc_^Ws~sKD5W#cE636;)2{&J?X}WfQUa?mUrt3q~vM5V%D(lhHMQ+Qvw&FffckW9?1Ke8z4i2LMAia$JcAN`s*?c%na5GufuN31lQ~=?zO3J<;ciAh-%(0%=)(tgZM!8TlyRDh{AF!~Id;5ke~VYjh*YA(0e;rC(-xu%KF1UT~^NP)Tf~6*sC_VlFR@=%NZ3RZE8FbIc!EGoL!=$71PEwJed?*E(A;uB>+A%9;^nk&_wnfIWlY{4^pNl`2g%P&lGPki(cmv(JfwTqFyb1hsr&AqdVtwl{88g>UhlWs^PyX;%Ky|KvTm*uZ(XrE3Nr4rjvhtnp%^p)--d?Pw;(y64D}v_abuTCLWs^|B_48B{f~ZU_ZM#sWujGIAu=G%=Rb4{8ZB_zwNqMzpYuImy8qV?nink4SREq;K<uyA5W#wB6lCLtJ_4OP5e966A%aZwN$|8oQEC)+ULFoVZKvqiGCvLnM{v7W3DKGVhR8NADxNei(k1&N>!NjAJmVOVwBhd~_xTt%<)=f!Un;qlCW2KafZ$uHOvPg=}~<%3og*?OV}e9)eg3(K4Ze%g6wm{<rs-3-5YvA|#Z_@!-I@kni3Pe72%wf~C^(p$8NOK5T=GMq~~x55spk1@5FYO7MF&6MHlv#I6mW_aO)O-{dUVx1=#bG>@U`it&==`T@73FQ`#}Kwlm)@|;b1@81)k{zcyRh$_vK;F!WKiy#Afs2$<^?B)ZSgcPfElkP%zV6CjfnZx&?c^k7)4y@WFxE+BwU4I7-8bm2;gf{q!M0kA5fyyTLZ4ObR-*Y<T?>goQUK6c{j$SMJ6Q-<59aUgmMFCaGUY6}<<qu37CNolsZDJ>V<SK^_;gC>BJjGxK{}u$Y)HCf2m7mwjw`8*zq{dP|(#k-Iz2UBns2Q22%KDJ-rF}^=eWqe5BV5MXvHI$4)~`J}Lod-rKElein>j&Y+F=p$voCTb23=F!)jE?0WQHm2O)ob%YfH}VPo+FADsqUC+b}X*QwDl~mqFi$&QUC7w}I|1cgYyUL;}dh$V8InS;qo&jzM{zi2F_b<UW*Lk3`O%6lmJ!{BoPCV}vu?i&+@f`KT%nlZ_y|D9OfblyhvNmIC-hd77^&(@>c*2rxK*KHr%k5uGv5Y9wLdi6u+CKcIPw=>R)=cORKIL3*Qp2-y(lnf(PEHI(x=F5VtstXf*dACA_Qwoan;LV5$5px1}+od@*gzMUUjlfBrXxa1cnF)urx?QM3`=5IC7;tp!7)jv&k9{i98`oV;x+XF8ks8!4$+(d}RZ%k*y&&)SrcSz7$&R2WLPHF`6c!>MIWpjG#!`GkmCS&84lY2v-cIHhMw#9gXA2omO%%Mc9Y>JXUFAim_i#6_wD_OO(BDIkXN9wc`;6n_BDx61#G5?Om(9_K>DR|q95QrfEEkDu~{$S==<02@?d%-nVQZYiuUOu^!GG(^oi3*M0WJ~h}hP!IvM|Q=Jq;?L1h)Rd?AG0HYG~Y%AFQ2m0VRF|fmTh>2L^$!8H`$p3x^O5fkRluZQ_H@txVE0eZL!StN%fh#H-6MqgNDhP7Xa*z5X!-8j@AG1>1SE~DNUJW%*Yin^G9bHoWz*AFE`6@Pd~&gW8L&a&9bh{vbKRYLBhXja*<@wCYMk$zJ12bib467wn1|sNwmr4+b$6e^e;|94T%y8SBpv?JvRB*U!3x29i$6hwA(Y~5oXogvwX)yuAUwG#0pXE=9v!k&W9<@VN52<bc8X}QRZ5@l;#LZb95!gfjXC^IpSHG!^`<U*n$|-9C4ZE$bRT9SX!iFrX#GVWS?f7a$DY5OLOp6-}18z!P6gpY^xDi`dylgI3_z@WHrFg|D&-tE%H}RJzno^HFQ`z;JY3(8QPD4rhbOiAUWE?YH*@9BtL2%w;CAdQM|#l96q7pK(g-FUmPav$$WL5D=k)|D^|mgbCW^=Q}QhUR~)7QK^ryUr#B>8(d;7*xt8G=FfWLw9m5312t7u<s$@94KMfNc9n^_6Ia~bH%}B8lZs0svfCZ_iNC9@F212T56Ke?;NOqa#{PEV;-2&_nYQor>J&i-y3QvXhBTV*ThD=bfkSthW_H?jNbqpCWPk-I8zLA)<8PJ!=4tB4c0DTWuF-Tg&w?<189^66%EP%}i8Evz-$N{0^N`j#rvNvowL6sb_E!&HUyc8z|m}%Cmi`E9IRAX}zhz3mkD7sZ@bzKpApn$wKZkqyIK%qUY#Lo|_-bh-oW}6I<(%>g6_yP78vkgCo5318g<A?H0iP7w-XHvb(d`zLO2*b_=KgxktBNYH!+OPvv95oWoApa@;E&(kF9*!oe2&+?s4Ws`*{|Gyd6(t+K%oc!V;Sb_CmJ$6xyTDiCJ0>HfnRWq2y-o9sT>wM9*abc<V-3FayZ*P>ox!w51TH5I3EBf}9XIH7&s1!Kc6WCO>Cd!r0O}cKzoEhXSuyLp3VzifpWRmABpYJP-tthTf$16<sk|nBY}{X1ZPXT%x7Iv=fz<Rgk4@r`CmBg!Mbt?Fg>uRIKWSrQ_zpNWteGrE!+oOijD^F^C4?W6S|v%r1#P3*umL1U{1dY69)x<1<xWZZint*0gwf7P2Is!P?_zyedSzHiYSl`FhxQQC!bqngDI3Lgk?1s|suhO@6n<*YB2Nl#!6DMW3_*Z*c0{2dyAdS{Mdli!qXeWS4_x?GVIkB;#vUK6t#|CH&GB)i<H_AiD~v=>WpMID9y8Gba;;$bVg%lapPWQtT-o{Nrk3g|O-S$huuWDo?4!(8y!C8&XyQ+?ug3~TAsV!p^SS2gs;l%<q%Qs3bSbF3Y#qb4zR_5u?A!_^#P0>SX5TG4!U_MR>Ar=@2V~`7l@DkAL}I03R~9yr{2<~7)-k;^JBl3kAjaCr<^Z!*<C^2weHAP3m!8YLawCqs*xZ_lgdI$Ag|4i)xkYP4p0K;4Y<Il1G?RG9qb49dFwwHa{s!U`H>?fpcyPX>w-UP2e&b^fxU%2eRi;ZkfJs00YsK`AlbAO=;Pv(vv$zdLr<CW;9qTyzgUM$2(h8Kn9bU&F++!J`2GFCIo{eITyBDCqadX4qtI8Wq9M*-F9)I;K;DQZ#*CGS+mh-Nz<IrQifRwBi|4ZDk!5){n*HB0idU+py&iyv*#p;J{_?kCi<jtZP05Rx8>|J`;kK)<%S&@lCV*oso7W;F&kHgOOZS0Yb1)jBKJ~g1r4yz?EjA0$xRUDWL&A)yiD&VHY>>LK{aiLXD9I}gj3ab`?98g@)BIKRxxJLdsn<W5$4z9(6u**hvHxg0!A_orU#(sy3+0UR7*+>k7=?#!|BdRT>kUYeeA8GhjV8<9PW&qPlex+t>l<ouE-4#Z))>G*v{mugC{59V`JVUqYEj^mm1a&r~?2W0BoZv53rVO$yJrt6F$R6BKFfiVqNQ787PmosCOn!)21NIwH?W#5EShbjOjSc4eNGq;m^Y)q@WBJ8C$;U<cJ5ML|;1bn9pe<1`zM}8Qp^bGAqd;oCky6ob64$P0R!Rh>!K(ovm=-DfBsXe(-jQHqBw8gw3Arnv>><&rD8Zu&FsLes#Arg}0R307egGyvM=T~s@jqH1mhaiIE+(8eGa8(Vtfnc}Z&7s2j|T?2resXcPAK1XSTp;)@Ha6@nLULq>Cb^f7N0hhRq-Zx>Jty+b^sEfAxP&g?`BQoi)3mDGg)cO6s!lQ^7O-COCq)Wxk(i1JU9{(#vr1w<ub|{oNcVcTJd6#wQkAgi|Zt052uCwkqEp^5D>3>wc3ewEU5AllWl`MAsZTv0|Zyg*IloJNgGerPfdY9!na^zuOXDiz=-@MfT1W61Faj``|s?Rc#}lr@vH#lrBIa(Q|jTt9$--W{B8xTO$|Vo%t6@xkMAQtcV0(4Ne~FEv&<~6D)BmxQUbo7Rl2KqMT9Q0cQ;xg;3Qztz9*#<!Wq~s&swm85n&TRS}y2}B_>MVk^Bm!zpqpr{Y;il=Cmt0?rIE+36&CQCCP@N#}tJCM?7t8HfkYOW&u>hqD=Hf4LFvLJj&kXG0Aa9Wd?%6iBS-eDqm*<LddZ`QcDtMZQXf+42@56XNFInkNTTeZOsYm7F-FKo8~jeQnN2SgxSE-^b8``@uQ-82-atjCpXn_u;j$VoUKf@N3HBp6>jo>R?#GuS+SNk&Y_ooFxn<(j5ZPn6QnWGP9*~!sPKVAK{5oCq6A(K7XOBK`wPm!`eLnGeRVzxBxT_5)k*R&+=|YE3UAmUb|hbOqiXdiL7nG>qXss<sI6e9Rvp`s6D!@4xo0?l{+fj_HY`GGsG}fK#8mMIA}HqTG$^utT)<pdZZc0*kUXwaZ$3FF_@g1y7ukRjeWTsVIN#u_wbIn!dWza}V;`-+m@QometD;@B~WiS`%V7;`f4*T;8^`?3d8UpqT$TnJM%Jd%6y2-OR7p9>`SLz=7r%lUdX&umU$tjG8MWd3W~m<Dx6CGg>h&TpOJsTfG_ed+fQD;`&Zn*=Z8Pz9v&EZHVkoggbh5zhX*O0#m!w54<8VmM>YNd8}bFCsQ!+@HlsI@cMa%bPQ#r8VWYq<Ao5IgUUe&Y!TI(55v!;*x+)y7J3!@4rE?|Uha<@)8Tcq-+iZ~;Z|T>zfv?;tEOND2V#&i<IXO%sI>ZV4qw!+psq`JbxZ6b(t<|?)w4_2gLrQFnDOXs7(<1w4sXoZ3^l!Kc7DC{de{8aXzJ>9JjW;57nv*=V-Cs6ikz?<-Uk)C=CE#mT@-TBC8pr6@EPtj&3U(}%+DHHuPLH0eeO4>&h$ya@&5rU};FPv3G*#Y^z{ybIrBI5sjm=;xd5qe*KwBVK1oBS72&DsRs{VR~;^a?S4dh#;L){quwzR-@1Qq7XPFRPD0(or{Zmkps&qq4un>br|yCC9K<<{DxB;jKES6`k30i-&gV|5GviH%r7W}+{jZR>b^09_}t2W!$y_v&gBg{GHl#biPrn=UdF7S}hBwyK;M<&{pujAUn8I5bFl9B-gOrHL+r<h+6RKHMFZ+)&<#$(BPDZ%bug7cf&tT4>{eRZ=jn)(G-t+}MXmoz5FBFj}g00H8XN4z%HAAP5)9QHaeAW)1}hqETOQ6?J>6(fBj-^|`-BZn~l<eVd0I9bx8a3Du8m>5}V|t$GtfCTd=g$V_MgM!RG{pB}Oz4;9lca*y)%FG8n6XHyq~Dq}Z^=6T5DL5S9bzKZO2<9RGa7{!yivYr`+4^bbXOHV&(2qXiLI+xs|6vlq~nZuO76bDx$KGB3C4A;!2zd501xdwG58AqwJYa3}$JyPUWUTO=HE*rhzCY^TqdHMW}F=|=4X|5X|CkUQt&WMT=Kxa#s>Ml&$@7C8EO$6Qr<8ZY`+Bvw-7j1dMKhh{x??!IMLf#b=*ADa3+EtZ{FMN;oZ#=mZ18aGzDx5dv`SL~7lMiu22$|?A0t=<e|M|tiqf1|IR)OQ%HHUJTk-SFHC@I?#szR+A?V1;7KK<)wPxbraF!7ni;qPltslUq7UwhpF&2w{uG!Yu=Usn2iUu0svM1Mq~KjOmstX~LAjB{9G^<vkvEw1MgS^*!Z)>l)PrXW62>4nN0@jwJ3iOE4b)t$Apq*+S~(r%TUPF%((b~pb5I55?|{6k)yHh=&UZpPV!BI_Ua-`I&Ar{;#0P1!!*kTlZf<IX)0XUUy9G4qAS)`D%8XcelSJ<U*1Ov$$P9oiOoPvC~I27!76ssj<*am^VQgwbdN3;219$fu%sVM0vI`{@BoOA<z+kd_YH8SyoE#F%2M=`;ZDiR7qxoH*c6uJeJ*yTW04LBmbEkLbtPA_Arb@$vutQoU{H3i@)rZJ<~nNBE0-+tia-V0s&tbWS_mD0H!Ga+3)dT1#iP>>pAOn^t%`VZbi*x#^hU#0q#ngtJyR;*;ZrRyXl3z~NdeBXFh3tywm?)uqX8Fk4_Sz}h<8{QuA1o5aept?5Crnpm+SGInO}%-qen_rCXTm8*HYYA8w=7~ByE$r6mPkcB`VFeqR^2_(w63R6}U#(+x56fRSRCt#TZ!~_X}<XH_65{*G1zy?GkA%ui%1QH`Ai1mHnzoN-zpMB0f=bo$5yYFbf+_^I&BO_MxH(w)=$4!!(bdk)wS1IEn2kjRmx8TN(j2M4~=N8X+ZctvTR5v<HiK8r@+oxO|er=VEj*P807s==md0SR8dL$IdQFB6G4g7WBS_hem6SpMK1L8GISj+Pdp*3#@ixdXttZ9$%R-%cCsm=b59gw8pyT0DpTMj2nSgmqI!Hn(E=v(!yq}{<&dbE^L+~;zH-AOZ#E5ElL{_YX%U-%3@;afBCp_#+Uz91k5R0i?<n(0AdePj*7Xh}VEI7En%%MFV4B~NV`{mZ1{aHxGV<`syw{{>rLHk?Vfpm{<oq?)IeyzTB<o=RP;&|OPalhrA=t<~J)64MJEkVUYtlP#zf1&3HuRY8BEdT2FO%|L~rcF(0gl7$E_H_9E9X^{N2B$buu*r8y#1m*R__lZ}CtY<s(RySSssJh_pNcFGnfEAP0aBBT2&-J3s+FbQSBBJ=r`zZPHK%-ccKfjs~0lzz^ts?e+Zmj-iiITJp@Gf25S98;Ufqqn=_(|Cj4kwqlDDv*;p?l!cJ(3TGt)T@kw7d)wRh_I+frHHVjp8{e-g}e4;Y}urHPGCdelJwD9C(d^cP4q9hJEnqG#N|0ew!BVizv!MkPHfhJk*9)nEn;`Rc-tY2OZa2PfHugN+Q5IqGLh@Eof9jmW<_G24V6Vp%#E*tRYyUBqqP0If2^jy6t5sZ5$;<m3WW~i!Fen7gT*<r-q=vtWHXR-o_htkwq0vwANwI#cZ$nkUbY?{twO*y_n=wh#@Vv5;b42J_D=Kwyym?;7QoJ2kiX#GD-8@{vGrH=BlB@d;UJCy@Qi(DF8@NBc^D!xEFQxV}(a31U~@HfY^1<9hl(wG8G+b-I-#78J`a9MdD%01Xa<?#s#=+Bz+BB7?V@)fc`~IIrkFQIDta=b}S`m3aDo((YX?A$B{i$EF7H}#F**>g$hQB(_(tiBqS2cAiE2<vr-~)+>qyL4>YT6)K)|*-+^5k*yaqz2Q1IuV;bK}R#(rARe^;{2L2B>|GI0l+x;AHu=|n42w#7eBmb-$<umn6=+-l4SBW_UST*@hsGWmbx4R=ywt+2R8K5Up)q3e-Jz>1=%9Dvlj{FFHiX()LV|sswO9o9UL_CP_c6|GIobUzE_bP`ihkBzNtHVS}jC&A2@lV?)d+`^lY)Wy9D)jxSQSG%SOr-=EKj8ZPqwMNLtf&j5N?EJw&H(0g*_e&BERAKfyP9|p>ttOpY+8qBrt?So%%DLYN^~#J9_S7|u#Z6tBG;i?em^OodSF+|!xJML>cZg#Y$0IWAO(8hZ7Y{*FGc4tn%5@qC*_$RiBpw;I1`@3u=hLitwB>P1MgVEvp|Hh@9USse2;+HfCvoe3u2cfkvIzxuxN}Ss2~ed<gU@&Ff-mVsD8nA+43E~|MC{goINcP_N0y0U~daizVfBj6C$UjH7tSlR5TbXD>m$nqn3zBVR_b4Y~K;5wZSCx4Ep*flWyoU-4M|70b~(A)Dn@1zTLQ}>FmH7O+j9-`1HGz>l!PSrXJe?Ra_Y9JElrYMI0}cPJWkQ`(L?)rZVyOe%xzzx42+waka|HZl(52BesZ9QlgFFxm=sFMTMS(oo);eCMJBfJtA8e%j+MNYx%>8@mEzQ@>G*%A3Ow>tIw}QumWt!9n0)0*I-i~|9v0$0+fG0ferc#`oyeiH)W@T!V+Iot<_tvk`3=l?@F489lhg&4N670<$Qo~P=d!DHR2>yHDaZ1Ve!kv=gC0&hveF=dNdp#%>+X80>758v<2X$id~%`wS%JNKly<#M$2>LP>(Cc9b6ue*4ncx#P`l(M|f`s(PlG+O9uDC<-z2F2pX<dRw}vSRC3mjC?o0MYAY0D2P;Z>W8NTMJaD27RX$gy+AYhFSlO66p!fAu%SX{~IPb7q^gNYmv@uV4BnYG|_nFn9p&~U=+^>^P1*`mvA7Rp6USnId(t6Pf%SFqwfa$tY(zcccnFW}R;eh%}tq8VO+{Xg8V)J3z23^f8-%wWgdS6cLpjkYzi#u$QDBci>lLIev>mN=R7ueUfZz@}TlZSE~o4;i{$-nfC4%xFAoz4eqxIS3xMMZ5wdDYD!yI%}hh(c;(;E>&33|Yj|tujv(L(2-#N!pKtHF2<}YlC%vK3Lt&!TNdg=RN?d?5%WEx|^$WdL};M*5VVXlgwdbO8ksZgb583y^I6ZAY#-TbQK3i1u4jYFW9MkzLU(#Jf4kV#?1pPA}Mh7YkC<)b7zJb?I7~V^I_3V9oMP9qM%!_Gxf<PY3Pm(v>^IAY#Q;`?jGtC)$gi|fLWaa<?W-zcK3@KljlX42xnLV|8z-slG4?mfW}<<3<*z8k+cLVq?a4@U4c8PQdch39U^;4{+u?|Wg!OZurT6+%!hbap)oHlXk9e1B9ocO@)=cFI)5m$zr#p@^8@Qg&!g%uY_4Y{xkH6=Y*l-D@WR5Q%fouW15yzj4QK}hNq(f@^MMi+yg&Xf5yKp8<V#Ej%B7vkH2n0F!0Z5vp?0g0pQTDnTLvjd0+}n_b0~aZ1KnVSJ1_%;jOEw}uqFsc8f!&~N>P2av4n5rNj9m$|K=?c;7zxWGZJ7TB#=D7@Jv+uWc9&5KGk|q2vwvv?2zas_2}*aMHrCHi3meb6fubk6Yd}u%~~wf0~)94ghHu=Ayr$Jg?MD6%8O|t87lSz+(4NYTjEnShH9aB1)g1?Tu88+gI%EuQ0Q?6R1=cf4P|`@)|apfE2pkG*EK|=p>ZBn6Ldxxapvuz<|=n~Ls?)c^&%OnrHcEEbsuOt!KWDow25Xk4qyeX9sbw9CfLN_Fy%jP+1&u__Drtr_=47H^;lB!{n;A0ZzSmDC-0ijnAy@Tq)BdCZb&9I9Vg$5Mwl)iu2=BTqo)jQCKR<FpuH?lC(^OJgupi&`llEx->j$f4>g7!z&|9vJ%Bc%*p=JxuvwMt2I{KWQc~r`Iyt5-ktXl133;oSN)y)?1QHxwnkA6n-X;j?Um*yYt01Hh%Yly4>)TQVAtUYHRy&f(LWZUEeO5M2zY6Llv@EQ4DmLlnjFdX-tXD#J0mfo0Wk|yt_mTEavnHft*M<vb)r8#XKK$SBgD9`UX;<z>R=IqQD;Fe4_XL1zt2nY(CNzg4otco{-vXHTT(IQIwCs{yh(HGVuH;%_pz-Mh*5r&r>#<=g(~H!0)+O^xWwp@guh#@2%TSqR)!0W^cF7QwwE#ci>b0JwbBU{6G|F0qAc>_@(7mx1#tThIXShO+1%u|)>FTY{4tB>)eMkcmO0K`0+|*CENQK+$CM_f)Z<)yi7UkX4Oh>Y@{j~k`KeKW$c}<%}D||WI`*TZ&^LB4<J(@uEe(578M)D)`vSG2pm%J=me5*x|+#~2zt47<XIU+uj>>aSeb03y`LT-%3&p4CoJXTshpCFJDWb%LkX0nS}AYsDTjm4uwDc0?(SrNV3QZ_2zKoMfxu6DL}z>*Y}=CZyuZhnxD6}FXf-H=kFNkFh)@JC7kGT{!Ai*Q7LN>%|a^U&Vo>rh6{<zI#aPzmsVX5jz?g26fCFFl76%sw$*Cd>gm*r;f&tavAMa&h2Lb=OAHy~@6Ks$S4MFE%b%i{FDY97(bY1p0T4tw$q)Pc#Z6xT^8bGK)qtz#HMtaXIZ8dLVdW;!)njkvArmlWDaI9#{5XjPz|Kga?7~CQR**utV;U#eCw)$LxEo98BLh*}8q@60x-nmJEvfzV9XqB&mOQjrs)?+OrCyCnW(v%x{#rkp(lHqE;wm(^Ec{i~{rI5MX}sObd+i<et$i!q)>DGJt?}Fl`4c`k*KqFy>%<XR`(!gk3v$(Q6{batE^WdUlXx{6pBIeBQAK^)h7cy@B;vCr+{gbE1k-JfdsF-ZHB`czSwC@|MXL*`JC=3x!st!sAFC3-PgJ5kox_h!chCH(wriOif9u=Ex7!;di1+G&)x{jAZI&vj64g_d9c|kBX`(ejcNgW*El`s{%z}W~7q(_q4U+$&@GCjeDijJ#KHAu;+gFOl(WSVSvbT$;zrl#{(MbI5veyKs0t61@wcAIrzDeHW(bgjEt~%kxyx$Lz6B9rZaI9E7^-vg{P9)n=0oqS!<i2>B0%!Pec<Ozvau4QZ-i*oK4MIMQCwuiT`u+ai(X&&$;SWKk2F@HdJQpBMn1*H7PPH`N`Mbtc*FG+yYB#P#s;>8E{!aoaQF47uU9UG@E;qGcs#R_D-aaQW1+`_NlMdt*u{wIvX&~@IVINoW7A!^rBnfM<)zwSRhcPfMdUsVO5eO^S9*Ba4?YS44LgMzpH2B*6`MP0qqDAD7IO6Uf3nAz+xKsmA~!9HVO+5+H1hs=nU&Q;G%@*f2V7z{y%o&X#D|uaQ6HUe|^7Se|SAV_OCy@!auyizdwHc;idTDMgBCu`VaG~f4?K7clm4jC};k4fBh!zl>gyC{e~`V`fwkVet2Qu<-PI6U*GAyzt7W(^)vqK{pvr^uj$plddRz0+nh$#oB6CVf1Up7-r?8PWB01ZQDm7=Su^1^KO0pg&Ylb`Vc84X*B?!4iC2DBw@Wt_8?3MqT=nv+c<+@99Z4N}?9cxhctHQ!sp>;@1ze2{8;=8^NgWC{u<|kyTEfR8oslRH#s08tX@lwE34J2WMQe2?Ll=l1Efj082dc+N!Os5q`5y)In&mT7oz}}^5)X_&wR)Fdz3c4P%NJaIraordJFgGu7QbFQ`Sa6uu0kxF`QgfPD6;z{g-VjRr>nQTlEKw8oSs>q;RFw!p0ux1PmFU=RP^TjRNM3SPM;XaWp>^Mw%=A%bB?Q%nO?j+TX*}Ji)&8(d&!}$@4}0}E-&xm`gp;!U1fYbUu$(ct}TnIX0v*18mbaqQ<-qmV3Q?~{fvvpd=0<I{42kOy?1(i`LlWbpYrvWU44r`dvCD6vWnT9eHW|%{>t<E*}U(`pIwl5`)j!JSMuBzPp(hWufN*aul9+{Z<k;C>(v1;ottU$F~YIkO3ygE^|6X)&jNn+$twq}-}=gzdhxzES9hHHWWB%MrunV+zIfRAjW;gQ^6?9wa&|qZ>*nk$OBcSGF3x<F78m)2nK(V^?0lTbI9O}ne)_tQVkuZPx&PVbkA*x0ux=mFr5HblS+`;3o<Xe659oHYeM;fYBM|e4N2<a4um@>0><`9r@-0xR2N$-WZN|}?sh-4Yd%ouIV2uaUBH&6qpc!imwrtF|m1>%&gGcd6r#}Jdu@$?M-J;P$GowFxHREW#9!@7yl`XG%R*#qP;^9;eOF1RS=RwRnSmS8~yDprb8j-Wg5e^)o>1cbeuc8Vb620p5;_>#-*q^4Cc{NU<rR4Z0c1Ie&53+n0{uk8fKi~X0m||O7^)pvqhD#M=YQaAoCL&r-l70vFSjQ--6NmiX#ryJV{<VC<ll6~19aH^ITE1p=?TG0c*bp0l-2y^nta2c^cTmQRw5Oz*@POgz4+Qk7jmbVB#Zv_upuqyZUu(~Jc5|E|6O8z6RJLe(WC)+2)xf0zesg4RxcYYM%q^d(Kdsq>)-KP|UZWls-3yzkV`y`$1Z189b2QzhBv2#RA=Pp@U3BKIq67)FNqWBAES#YkpQ%&EpZq%1`NnG!sG&d_{@gqCV0$!RM>4r49UiLT@&1<(G>4ItH5{(9i)wSGc4B3{<Nef1v$#V>nkFDLb;IbZn5<dK5M+>ajFW+nn50Ce;GkXdslz}Y$pFvZuC&F`f%kyw4r~{r_uB@UgEMG1WYOYwYKAyBFH?&8q{%CFD*oK4zZn+I!)jrg7>$4BLeE#I15EkVS;waOKzKU=^N^^Y1xY{BpV?OT(_0M8TtCa#h9^KuCfB1t@d3&|c+k60b!Ma|QKK?NfW)8M9g%WZsAk!rsXbC_cv@F>*@pFKk1yg$j+I%#hQc+i<~8X(&Q&w+>A|u&jIU4gHGW@+^H}J}1t555?PX{Ai?d#LGtIpDP|4K~GGEzQOv&2pe%ABx^^*GO3Y)&9zMx(YOKM-0nx@y(JGgG$&qHW_o=GJ*21$lE{Q0-R7N?t5*f$(WC#s@g(Zq_E10R%0)y6H~D3#`TXJ|RWssS?kET(PAaRJo^zTs4M9s6tSfxF908MDxUfNhqUPE!~9FC+q2GFV;>VTX-0k23wH+a8!*km7nuUeWynuq}u``%cjAGBaAuU`lZiE#tL1^O#YFs<iKmbnPXM19-2V%xs9N0E^m4&d%|~B6Y!A9?&b%i%lnuIDI>MWU%{Asbp6d;z%|;AA`9b<n)d2n>Nl2fQVNChg<qNLz9^dax`-FEJNncH^1%N4}jAh08k=ojyfecLDBfj*8q0A8ScqvpigYrC_N8?g>H`0jbQMy;i}q&HcCnk=h(Miii*-vCV*WKPDTw|ENQKVJ-HRcmco)WQ6weW`h|}e6_^+n9%&Xg6jgkLz6InuMjOMFg$0gDVNSWvpXt4OFCh&tX0N2@02iZ!vjaW}5WWZ+h&J~hX#m#eRto`446^`ANZ>q>;SOF8Krld*-;4MaR3yfZ7#$EA4^rkzRz}n&Y-Y<iY!6WSK)5D>^N4V=pvIU#(!L9RXBR(IwMYDX7yaJ`A!)ai8z1ZTMD^PQC~OtLE)i;L(&H_-$3fH*!QsI+-$<!8C{+MEy{_%8Re`Ae5rrb;Hv<ESQon7}cE0cE6s%$wq1LKwM2fnU8~7}-xIGcwoEsDYHf^_7&>Cu=)35~Z-D&sf{KWVHDW8){Lg2Nu6^T)VKrXnPz+wj{0uBI&O4Tj451nCK$Z8e&-kxb^kzd7Vf>4o$p=>Bu!C$g;sGt_X5N5P!@q?F?1O@0J?1`yhxHe(o{QPxne^0aKuYN{q{z46d92l%_3OMCbrRdlh4IBi*>b&F_cz*uj71+{Jy!>Se;Pj&Y?-E;n7pT~76&<J+Iv=ZTp&Zb{Ldd+zuh9psN&p9w0H(4P7xP?~p{oCD@@t)dyx{+x$*<wA_Ty6dm$+WeX_=!_fvw7~<q1iSm$d|wyQ=&fVKEjmgk!jJtrgg)4$F-KGpI55v{;S1uZXaPvTDa@>Mdn-_f%Js2%G07GHw+80XP1V2wUG|j?La=mavCZ+&DGDK84s){G;z=2A!dO5Fd|BvT0_&i7<oqBy~NuZj_G5h|SJaaT#HkvAI3^?=y*Xj}$3&y8L0-Ybh>43BL4ClmUG*;~l=n=N&eM&#)fxEe8`vE%)^M+I?^ikb?=Vb-szP9Kv{akh2(x^!zzUReJvfJ>QJy5!CLV-H$y`O)5}!qn!CexoM(W#q=lNR~;4<_{}|)o8(~g5R}hn!wuuZhvQ_A6HL9*$;1R#aj)l}uw9oy9F7chCV5u}rgEfAeEB*|a~wSi!Q#&MfMt^#OA(ARLr!@6J<|hZMkk5IiW+RzH)5UgY+Z>VKMUcG_XKF^#@$H+(PMc}_hra5(gFCQoZds@O^Vre*SN#hO_37!Tt<ArF~>&QjyMi$F8FF`hs`F|vi53#{`Hlp`sdt=uP&;-8Qq1s?53$~={3m#QkF)LpLq@)d4IueTQZ)-$W%gUt0-?Ew3N7nl7})%PdGVvEGU2!e_9e-AnzDrHP>`dsc_=Tktz+#^`23vNP@_u+s54LIViwwFy<S%In@yYvF={p>df~+jgVUiH&d%@5WL??HjArhHXg6a9EyR=zapB2l9d;PeeEW~jyEPCM-9NKJsd*F;uFh&2~8)V9x2^MYb2T@3^$vRz8}d~rR~-*vXrg10$oSR@JS~NGFz--4ODV^y|nuH$+a&3`1J)gO`)X9D4eCwkaK%{q>vJn)47&D<K`U5>@Ih<S1zwil8va~gQ<9sL5aDS6zt>QAIKoTU?kk*=c7om8DkdzWC7&K5H?L)oMF;GTAq)VVB=3+{ZLfsECE@)7Xyn#+MRlDJPsOW1O1<z6#L>~L;nR@C!==t=$_=2{^b4!1#o03yE}IRZ8>fp-A|f^JJQv1=1@d&?x&G5f=+|j{{Q?`>qTl`u~;DTb5d(uE)yM>30Id1f4NMA<pLr0pxAe&H65<65wh{XGSM!UiO!Y@sctfikF{7itrYUu4i;={y$BYxGpc*_dePrpFAO#Bt}Pj1UNUg<<<q-cO9rLrxMVaE6pM>hV^dZQu1fpYEg88|_&@QI@n_#T4gC!I#p4~rfnMe4+8y=6O+*zAtiD;s9i;vsIv$6Rd)&0`E`W&CP3AH+%cMBRW2Sdz^d*vqGRs+Jc|=auQD>2j%E+jhE-=W#f{M~R=bk6mm2&JS;TpX8ve5Q#ThmABAjl~Tww~o?_t?Lj=`-_~ENiHB;)2`=JZ)=K-<Xoc`YtA&TtsmGWkuaLQ#Fy=B+~7g3iv&3Um}Eu2D5vIrbZ&rB1&e1<&Tl-(C(jEX}ermgX#j*p(tvrk9^bjQe)8rvi|5JiZ6HHq|DrI191Xh-kZH>c+|Y`5;VoT2Keuq#as)UMev>^;1Y3fC7!E1k8=uNi|HoSj1yfENwg>9(ppk?T=J4~bPw4Bvb<zgNgV~6ui*&rsqv>uQ!Zb#yb;5yH5OtEktr0wwo>_G6YLl%u0>BlFvL<>6ItMjkO#vUKhwo>6C4L-XN11YDln!K_NTr@w}JuXYwkv0;V4m#(AREAyS^cjDlf6xN}S)20e2%$w*o3#NK<tm?p)Z%ri1a?8kMAf6b0TT-jmKK)4VOZ6<2SIui9-*tfFQ33V-aQ+>JL-Vtvmk!CLC|`{1lGYO`X)%O7D2pgW*o+vN3l`Q?Ywk+2zCzN-V!sT^v9`2eT*-ogq9k;}s!bYfn=vK;Nezs8dfWrw6Do$s5Wn<b@G3@g9i_f<cxTWG`OkiXmf-mBFO7QxRgzr4hacq3`4IryQj6{O6~+%Zbq^4v0yueufmwRHI%ni@#Vat87#oW1jCz2mvrY?sD)*^~v$HLtD81qfXc`NSIesK#0D8OlJ5$cNHt3fr`oIHjeaAh%Wmqud0m{Ot5bhBW0i>}p7}my}2^#adA;8_I8kdTdD+zX<hf8{^kf-Fd@cFOo}ahVI~`Vm>BT?4g^1`X;SC7a<LGRfx5t&D80ZPC;)YgMrP3$5cnW-(VI+$r~yx{$VKm{A@FR_j<LXSG6O8NsUqShElX_^rl0z+fq6?Np*#CS0E`<>nJsl07x!%Ui(c6UE%@l{4JUaC9Nw*VAGxY@yLJfDLg#=6?qca?M#jQ;f{*0R3;wE8(Vre@sb>$8t8sMB2*|raoRa4)(&OM-pI<yZ-*wAjBCpRB1?Jk|N2^b`a5-yUeeQVU)Iwv0S<ju-%U^dLK%B4qkpLpVjB9vH1sENd|a&*UlPz)9d~ovMx&FNEz=QyMLnP8TNcp6WX*O%K;KhkWD?MK=ZYY{GXZ_sSc>a?Lp{G%a}(-;lslcI^IN=8A~LGJmnktzfUMQ?!<l;iLONd<P7@Jo)&lySFDc?TZDYB1*!USBF47}!!U>CVkRnJ!U12sGQEWKKN7rnXC>xHAs_d%c0`DEa;Mm!t>#>hK@}5>+dy}(A)t1-(JFz)Lv__G}mKW^2^yo9e58vZD5(#e_Gbb}0Wi=>ZHw7OI{B>Ji)_bC~u`!pweg~?<&3KR0yW^;gCtiPz`p~G?7oS=1dZ1<=#b3(DZS)|+(7ktN=$-cEH@h>!Bf?PTzxj}RskAAs?xh*?9}~4TnU#E2du(q=1J#XGBQiEs7Qb3m%nr2EM!L42-Le9lZf~TnZlp;YX`Cg1hFcryWIxM|6m4+{sdSV-C!TrUKg-!}&iBs<V^1&jLkj*hR&u)BHo0$aC3Ngx-ZQDi|MG?z=iPGu$!h?=WHK>7O+l&ea6%3xn?9F`3D1BTKJPiclwt9DVMqe&0aeEKKwt>xNv8NUq)upRFi@I6Kq3TfCC7k(3q-=OE(GpPL`-<r9-qfhCcI=<hXBdF^4c#Vb*~vRL+35JzJ}6{T2pB>Scg{+kVU8RBo%(tf-}%_nLVbF9zz9+RVTJ=G7DIVnD$E`NZnctzRWH%HLj>rff2Fu@MD@pVWcC49OkclnCU&Kgr-+aZx3)xwvyefAbfp#bF<3ZhLdv<B)@WQ^FpD|yqezCS~?+qo*D`Me0t-f2S^pO#d~#nn|nPq*;)cHry$v8IL%b3GAd<Z*EvCjdOrdD%<jiJ_r%mjZrm7fahl;=s0UkyI(h(a7t&q1Hx;ljIj>$iO$S;wEed^~-gfnS?zaewV$ri)wvmd%1JO-^HX7v`Z&(i=p?cGteEfqMo_@q+z~ZCapAFkGo3f>K2>5f0kmxR;1qT}tt_lj{%jo{`DV}FeEt$KrMr49?(<U<1i|pV-)Ybz2#{bP_To^MZns9CKe@h3QO6p!IoHhILat0%%7BM2c{|d8-))^eXU%|`K=T5;cs?e<z%EY-5W`Jcs#=cHk*I02nNLWe#k`k?$D{}2kluRmP{3`-9h=pO+1$+(K)g?z5X=WlASU|=M8Fv6-=&xP=zvG5mhTE2LGcoT7F=8}S2+h6xk4A$ipqnNjM0pptU<c(Oh?*fJjV@M!AbQfduQ)Lzpr!*#gESMI@)fQjRK8eQhak=dUM@j3^)kD@8vHIcqvGH|hzJbg!_O1MWPvX=vVW4XZ@D$-MYQqf@u|({V)YST+g5l{4(d7M!^*e#zHjatI?b4DDdq|!E)kP8`!b(I0xHk5_ft|`B9-tKAsG(kF)cL9M)j59Rmye@>CE!gzOovXTG`dl1`j^MB>RomsX*Uc-`yO(5dgyV9o3*=UelFau-)p~sr=ENOF;V?tVzdlGB9eVb$q{C#6u0xAiKYg&d@`I``RqB85xcRg=3R}VV<L~o_k-L0nNV*zD(o`s4*>n+;ACld02r^B3A;6cK{<iKz@&-hC?y0J&cfW?NofMPDXyVF`7i4wddvEFt4vi@HFCHwlu*%hoKsMr7gW=*eu%-AOYRsM#fisF}WOae8H2)K&YUXWZ9O~mBWYzpRZ=kdzeZGp%)Vok!h=Hny?T|9Qd`7FFaBrxDnDAZ{N}15!N-VtO}1;)`F9m8;|zs@@$n1Y05#K84S2gq%O)QY#-Fa%C`H2NQaTWsdi<-AR=aXeXMXrio7LX17(ilAoK1Nto+5TbF56pbW$@;j2Fkk6zU*BcfPd`-5w251&@;dsrgr7{E{o;J^kI74<##4i3UUh37I(!rP;pc+<lY2KqSNF5o$q6T|~;LG2&o|8jR_d>Z0w0Se79@?v9L-G!@mqgYkGWi7xP8y!9v1is1rIxGfe;dUZ&f9L8-Wm2^^RR9#SFv8*+)?<X#>u#i+^ZWFzyfac{Zy+RDL<4aWH8yK4o!6ZpT)jjh%liJBN6*<}J5=GI9AMBwuN+(0(RP|E+VjaDFo&La96jQKK*Qc>cHJCD7SGOd<uw7e1812QR8mp5_$E^|w0vQ{)phVy}A)3wW4=|Bb=o;gc(8`AJ9;@zS26Wor8?bnjY?Ct|(7KTODTyl%rbklJR7|IiZp-8MqQ3-9WMpIyOm$r~9PT*LQd)cM3Yjkoo3v`nMfjx^vLd7LPp{?LAe|nJGj#3YWa^%pFq=mjapHDR>hrD{1bvhRWY<8ZK5He!Dc;Ahzc<RaqgnP-<G*C7LTI-;B|hbVk6c2VaF3#>2PREW2V#+3RH*`J(Gr6^9&v3(>%Ox=vHqt#sJ!K~nQ4I9n)x4hf{~Gikugrh&V80ubA$nTk|8n0L+v9_k>P8O^g=ApK84*WOk|bx$3KeA+&%r9RFk7bCgAhT=}^xNET&QqT?I~~VR={)0tMj|&SK^V`i;3wL;Ra*0G2tkXLn`WIRgVH9>1ZZ+zIjM)>LMR@An4$C<h-nzR`=uHiU5k7%(}m5^OBruH%-&q9$?iMB2s8!VE6*Xgky_2d}=KSV3IERKjH8DaT5N`n7jfX@3uO@XlzMLoju4f36N*Q_nqD2L^1ZS?GexXK^LeZl$$rqTr?o9*G&wOSi>XuHu|i<{)WURF)&<OncHJ9=KDL5AOHo4K0w!UE{T47<5fS?JWvo;m!;9dq3-f&(R5`!I|ep<6Ut(Z4RV8hJWszCEC|g`SVR6n(_sScJB?q`j-39LOX#8{Kb8!;_R#YFkTAg*MxuM!nu%T_l)0yo9{!yePFas&`hLdYU~Yc_Q2z#GMAQjgORGAoy#fv+LY^4Zen6Q5e{XgaVpf7PaM0m8v=`*SwFuT+)lS8{ugF#{!WVRH}1>|MnBz|mYv{?^}P08n*I{XRjyKReN5bn9a|X&%35l&FPfOSk)6GHlM2mMZWl2$Ld>_d(-I6ZPm|I(6=$eR?bvvBX2XIT*iAhawveOT&>2H^sN{r2Yb8u3<-nVnNGdRbBMVA0v-5_$XR^#X8585243Wk3QmbM^{b4G?y3lTvIX7w_J@^ZEQ+K;2L+N~G`YOvHhQF-Igm0=Q6Mp@JEdgX2%uB$^;|fbaZKT^05Uv|FOsny$mw*zIbvKrPj4keb2|)4eYze42yH?}gh!wU3Y|rL@vv2AW;5qpZ>Q=h&i0G6=3C{fd4oh+TFW<+d0k){uZpGQ0pDMGo;Xz8?)@je!Vrse0GoPTQB>2LXT<_qGCMcuPTEm;BJ?)&7Wsr!YTU54yj%EeCKbZvlj>eT;07Pn8kflAj5L0!|o5hJHJZ@C0)+#V2VQ#0&u-I$<UjQ-h7MvJ?`y>x74v=+P=Kd)@qHV+zAV~-wOUl?f8m>P~m`i$eY~s2O%LMzp*^)zSSEbndPhN`s%kMMdZcYBHyG-@FX3>1!Xj}!%<XaXXJ6*QLh|_R$%dm{Sy0}~paGXpBY^?>^H|zbyRh*1GhtSMVOOua<qmGO6@^qs384Q>o+E*@?####N{Y6g4UdcblmRs6oPh$=1SEpKYHSIvRVX(~w8(dcnU)0qj{+R{JEBlMd2$U1MTk!!tZDY^<V`pT5e7ZrkqSIH5@#zWlm`wzO2ihG^&1c9qC#~=>W^k){okGtWrS$S|C9+$ACOP*Wq#N!#%C>(H>x;W^66~$!lgb#4725b8*E6u7E3agx$`qgs5D_;u;qQ5nZaS<wdrf%I19OO&)B?Oe;ryQ-f$WuULs|1q+d$_G<e#uEerlx6((%(7T+*hD32Mo^(trQWcj=Y<i`bVhrm+uiY1gw(s}|rpx9eZVy@lGYk6))<PuyF3rJuL%*jv%~Egk!j9s6+Eu}=mZoI3W~#oV@%^2`0a1#mxpOE!^{Q>yZ_w@2bNXU}#g=m`+6*-Jmjuw!0n%YEHV5(S2A%-Ws;|B7f<6{a^e34_S`lRkhdY-y0DI!OD)AXQb~9O*`B=c+ktw?gDzNiAr!4$L@a?}Z>j;^aGJz@apycSJ)v_*B{OuY_Sj_nkHB6*A^(`%s3GfzHSr4hzJYsZg302M?}j5+yzJ<fDQ~qme$E(i7RGRp^p6S<VS?0@xL(U^F*}PX5ULLaoyIV3R;;tC;`h1|zW<RENDu#3W}qE;na(3RTmLRV~EchD|VP2lOf*>%Gp&jA%s6HEOOXU6x{iL%Lx2r3SQ31z+6~yv8kl#;>tlYa*N?%ex7@Rwj_&f3ve^_y^x%b9_W;;^7G;U2KjA`JG`K^iPeTdxDvWQ6ya)u1Mjb_4mN>u4r;!VxomN9G>3xO15;K!W-0fgUa$F$?saQ#T*Y*{n*12hO6E&+&zQCj2h=Nw!d<O)Pti|{#driqxGQ5)`pYW7+$k{L08_p!{CZ^t3ndGqcv{HlF3rRJ#?RL%WGFS@7M2l6zvhz`vdQHZF391vgn7FD|&ms>*{{z-?ra{icm{$+wZz)%w2b}<(&b$zs{ETZONPd%C{aR88X#OuFws><}id?*)_VsS=hxer+q2rV!#E1vsc7iaSFJq38MCB?f2mu4ZFS#V-Q2*@X^DrK6qztxN#A7i4^51qJ~YQBHFZLr^dY3&SI{x7@^WvL5GMLTqK6l&C!+)GLKUPT#{j-hKYhKfsy7QYtc>x&T0{Ab)-zTp_xp@lFS1wZkoaUoj(t?Bx0JUY>u5y4GW8~kg3l>mdOvBeE96GTXp^nwokq#zVC(uUt9>a9HxLvgkuXIYhN2*VOuEyRfI3qytsxo>S`|(MzbrUejQ{<SFhSVCo60%gRIsX_c!CLc8;@9V_5M7f)F-~Xt7yFTh6X(_S<iE-VDEEYxkY=Kk~Y2_ZBdkYb1Ft-0Nz0Sk}Cp+ps32B|Fw7JFHPsXrF6IYs>*}4U`Jht3*{x)s5;*j8Lwu`^h|JWo8Sop2+Z-GD;IxiiIu1-!SS1fe*A`?`01<vD}@kYx`O|g`f+u9<KIrDOO?Kt4cgsX#ANOV4g;wATaC@yEZ^753O-@O(r~*u<Fpp(vUwmDew|P=<hv{RAGUnLJ#iC_gn$X@sF=t0d-gPf@R{##m@y>2MOqrs>~`#oYp>n33A2&Tqm1#c6k$XT_u~5f`BY1&1t4<W`Am1%Ty8deif@W5>&P2ucn!9di~wRdAP_lBYAVPP^6=rswJ2P$7s3yZM14|4lBpB*PHvHEw%EhmyX#w*|f2_;quqlly<2wDd>l(l}>7z0<LgPTPL2?o3W~Exl6suuu!TL?$hf1t{zkCax)(Rf<fpuZ59iqH|!LzXJ@xEFS-FY6Vj+7Yl&1stS`P!OKV5<n@&#u;)`qLwK(?+vLn}~;bjHc9;^(I9=JGeD{YyL*YXjk<rMMICix;wk|7FOsRFe}h&Kv{EQelRnly6M2bNWm1qSJiwnuoz9kp;H+kde`BX3F4%NvS(NOH3h^N{a87!>Wn6XJPlS_32#SLEzhXiA7>m;7C@0g{dwS&A#Ucp&)QE3RxA_O{Er{b?e~@bA7yD+t-~PHNKUHym;&WP+nQ);DFZ+_B=b5rw_AutIaP<Aotxn29ZKtf?rWo8ntR@O%w$GN*S^w?kvZ9y_WfAu7z&<Pr6T=r=02si{LUe-q@EJL$7$9>6?8qTyN5lIcu@6}gHB`&Me8Owxkb|F&&`(T8nR%n%GK3jVa>@(3|RXjG6SDQla0(zD7Uq@>yBSVfH&P@yINT6LCjN}G{cJaKwMw3={7Rung2TTK+bszRO~C2i(UV2=^q?ckps$q6RdFu2c}-(C%fm$VBOdP4UviV1CQDG9B)L4==#;{tUuAOnu#`btBH(t@TlmZc=U&<*M=pHp$4m)?k&y%Z*>803kMov{ICYHKFcp|$~)U$P`Amz4^oGzAFRBoi$;m?WzS|LB#N<IUuhtZFgupD-pS`9md0vX;3XmI>1jh>+qLuB0N)5u6{dz|H+4NP^4nFTG06ubktL5u67-F3xVsWG3Y22$D)L)IK$%sKgXGr45f)g*UlN;Oe!1!GOc;xz!@C<sXePS_m7!97(JZQt~emf(Jnr$dVd3Iy_*Fe1=vS7StagQl;DV(SH}aFJ=}5dz~Lyt=MyP#0O%B%P}8uoX<$L$HdzKlf?amc=~|o9EF2meh3Fj$@xPwh{Olea_Uw5=Ii(tYvt3^D^QGQ`9w)3RFX`~se+F1m3%@HW#L*TLAwAHd`vTTCSH^oRbsP6!3R4i&@<6k??F5tAnmyvq)BcMQqy4dw1&Le)Fmy;(A!b?uXS2oNG0Kl#iTfkiX$vmUI8)03nDoi+i(lG8ot7VS1619wLK7x7Ah5^46eNm-cVDAB?$v?zrX%I!UxmcyB6VG!P!k>2hmKBbQ@J!uBr!u53Ym{aD+?M1IDpS;RC-EKDbalXjR^m++}3q;wRw)-tG26_@IjWW-8Ej2B5mGeXwOEjF>2Vfp}Z{z%Y6*Y9Dlj!ahhJ^3IhFn|@hW<PSDd5`C5YK`@fVTK?c6*1*iP4{RZW{K2CB7nj(bh46t2R(n6kZ2nWlZ2$Z_FFj?zb~mWJK=540?rxCM8C0zI*NYg)Y445xtig!O<|KPgjla<f7p_9~+DuBvRJfpkH^F*bt|#1dZo;JNNhu^LdX^V&lHtBQc`!;1B{ItJ(<??&9H>5+p}Dqm2B;yEDLF(;H+J0;u#`{%qkC_qiN3Bc@!I<07VFFS>RtCa2%(DQ;{cvnt1bW_iLM<XS4B{6C~I1KB<&<S)Z{ZLj(aT5<tplB*h@PA>xg>Q%LXcIL6sG1!FVwcL_TH^T=7hKS;m52_J6`3TnnvBDq4s=I|35{$|$7EaB#d4>KK@f9muhmOC?fCQTpwnt1s)>A!u{?6;C3+%D`@ddFy?bapbfKxXC4zPWY8D8fc|w&*Ri5+X$k0tI<b+s!4l%SBt!#zoYo&fB^Ek_~jOsWar|SJ!8MtZAlR4CTV*t(^%p^C)p=fgUb@vW8HLVDU-{1qTd*~B_~rIPc-Anayy}rmr3J#>EgO}>RLA@InLS~rXwN9tPGkp4#h7CL$X2+>giZiXOABCUd*+pMz)y+Y7@B(3xV8F*^-S3UbaiY%i6R_6s!p}Bhb`}swRpvYw`pn)A9FZ^sBt3T!PF1$Ejbe_901RUi4rJf?17v+h}@s#@NM{^fs9bEcI;NaK#SISN%8My7`C7$j!G*PCQ2LK&@ObKof_sdRGB*Qy~cZ$}!u;u8jhw263xOLKmn_LrSt1w-Pqz9xNkDLs`I8GU_s-p&DTUBF9>bU<l*12Tw}MQV@e=m3ZS&ZI1FS!RZnY+(Fm|VIN47KHimQytqL4^j%fJIN?ERaWt}r${6RlbruF9@TS{I>>AbwInkNbmC1`W>s|5~2y*eN+=HLRxEhlm6&y%~Htm)ZjFAfXQ1|X&O`W%8FlAF>?O}WN{D66N*Fkd?<%!ETHeOG{giTuioK7Q~>HY{f;J!9v!U;?ym@K&22zB`{>_9kXJs5}zRg~_ZFfLm0_V24pg}2HSQm7riJ}MqZdSN`_f@}_kP@Q_(dscVfbvcEb!;R$>8b=q)Y55~~0dCudG||y61wtZ4l7<RHcWlNiwS@5`SS+*ml=ULT<WkH5OBk>Q!dw;*)yEqXX)YM9WX8FKwu@T0m+?od%D`eFWzEQkNgmXQ33WwX>j#J1;=xr!<bg%~go>2wStQx0m`xncKm<;!rBa4R5S4FC8P=5)*knTToi(@PWpjI49`9xepikS@4*%ZQ8iQ||{&+6S!JJG^8tcv62O~hXjSY&pAfv3R(E$1PNwF@rzCoqvk<fD~R#QAf98#2`IfSWl0bYGldS}~p9b)XYY~kaCa)fZ_$e&u2w+Bm}>L5y9gHErx6Do-mhDT&_i)s_Kwl_4~#j>2M2z^Hh4Hh`dH$Ckei2``}Nk-~=_7#R$?##9+o5GPYv)kqq7pLQ2`&ereN5}cvgzKSn-EGiNH4^Lf6-p_3d9q(N_+a6cmtkMz;x#2h%hhTM{wj79$3$>Gxg!u7UjLeH&9cX~Y<aePmn#>StvoGTs%j=HYsS{x5kmFCm=~;S;uypA1*<<_ut<xMkCv~)a05!RBb_J&W7si!7l68sN~x{N9bvha(H=)23Cu4iG9_|B*6$G}NDj0m1pmc#ttM)p7B%)4-n+j-kO6QZu`X>Q+pEP=t^`^P*=kC_>R=>7VyK!^sDdr*3i<FXG+{ObRDsF>Z?l9WR6!zSbQD>f^>d0=+r5=aqKZq*>b)R|!3ylv7MCu*UV=qHF4BigHVmHfbd#5(`DO6<)&u`yY%DpiqC+eV2h-gjA>BaWb+rqj=s>0}+uY!du55`1CS3X~{mc~bj~rMK!F({`+bty%dnvd=o*yYodq>eVhKfDQ>_NgOdvY{Xac;~@H~-GOPJQ=$kxC!BXX0M$nFRVS#C5FH&fYB5ap88`q<X?GEEcAQ$wHF*nymtZY3gV@i;28kd<51P+Qbp2GKuqCGgrB7lYmUo=Rr#bg&ky#&|_mguHk)t(Kgwv+a~wdRC=&3{E2tw#9rRXskBzE!hTJNEw}L{Hmr*?8y2|<s%vCkYjsAZElw<3i)&7-T_ME8OHQnF69|O;a`i<qI#g-vC0-oqqNgl_p~L`u2<O;9cfD+z#RH2kxfAe`)2YNeC+-F1tPXzTtu{Tt3kATA<$VA=Zikytj(=Z*YxURv_m8yCr>pyXKUv5jpIc3;l{^7*)%7OtQf0l~+~;$%^ftNJ=gDiEH~F)yWZLBEAH`~^Z&sUpyV&F{H|d;tq?D)I#XPJ&w9{^1zUBTRJ#o#ecKdNkPeuY4LoM$RA2v3I%;mVi_>$Q>zIKPW8A;7%&QlH|FC^e4jw<prs=ebUc2U3H(#zZqIF4-`XE2$u&T2Ca`vx}l#{Vzx;(~bQe<()w^;P3$H>n(;W9qE@#f4kL_KNwT1MC1@UHQ<~?%)ImH<&F3(1bH2T+GuVjC-G-fHq#*4QvwyFb+uTu7k8)fx=t3$$NF5xOvmb5{3-Obkumwu`)899XSR|ru*6O5Cc%E)Tr%`R=<$#VLI2!4gxnyO^S{DM&F%Qq(<&e46K|~=0LPGrJnLFj+tA@U~y;Jo2Iz)__nz7TS3tKk3LrFgzTv<skBX6?QZRj^>isMl8_C}m7N^a^Ixu{Q5%^cj&ru{XyK+94&FbjL`e{XvlNN9dn)e4^VJitg#b*bDUv^5H<zAJ6)pQ(L#TGrA)tK!=56kAvlSF&y%B{IH5C1vB4G{Xz%1YEZt8|J7RS}To5$(yJ;o_XhOxHGL}LeZwmkl~n_mp^M?)F@xTue`I=P4T4NmHw%5!a?T`6_5wj3i}**e+#rXo|=p^dN3Y<%V{Wsn$iESaBrzMg;D%927#k#vKO#8<*#iCL%6B)W%Nsr{ADY9YK<qTdp8wM2g4c}6$@cEGEIJvR#95$+P<T8Pk7f0e8p!3B+ZHnK?LBulzsT=SWryN%3}q)*|)276Fz!~}|(GR~H)oExN%+Gzf_NjCQc6;<NqK-9B}R*^Cim^EyjCj)r#bHUD$?4A~KTG|B*B%P;7WO+*9a(T*BWyC0qkufka7|Wi@jwb&U6;nHDfQ4F<i2u(g1WjxuBwaxh;T=E|3sD(vf0h%?&<U9IouMc48G0g6?WB1J07a@VI|op}2Xyw2SYjxoV%n}S6hKCFO*H|&4WKYdhzg*H3joDft$_E9ZHsEoyahv16(60zRKm5bU=-C57@Z(Da>)oU!zdsfb&jOid<&2i{+HibitdGUZ-;NWO82UFQQ2R%;a0kbykbw~Bc*<vA4F34s;_gA=;cNdUT5M*bcjG58cDqJJLux~6JATjV@G6P)jVo3j<S>T5%aqP@?Vw&F?Ld{QfDP5+BALdx;w0N4-!0@q>h4|<rZp32`wsjY<6nE{mN@wdC#_RlyxCcACb$EOY{&PS!Y5p(sKn%IBQJW0afo2zlILj2@<|oyD!ViPX3)`gV;DBkIV1dK!77jb&MShh6u^qd%h;%HKT_6h%A;D1qHE|_4*B`sF;+92hd5SLNcK4&0Sg9?$OOFlY6Yf#8H0S3Kn2`fM$T_6iqZP)i-+N%r9^50$zi1AZ_l&mFzmaY~;&IEYNR5e`-u$R`RXotp3!;lK5Mv(J4*o%-hAisLVMPGU~RbA@0Py=0J~tb7TEsKe}~wl($+rrSdmpc*m;mC7;A93XQ_yP6Hi59y5`C_D(m=#k&ed>?W133zfgVVa>bQl#F1kL*InHn8y<)w5daXPob|!m9L$ojsIo48&A$Zz3y&2b3Yu=xxT=u;F|SeeJco&*~*?Z&;b4_Vry?ug49g$HsiKxwA)fuT|1;lb&T@fnPG5CcaugiXl{&Zh(;l~fGo-ckwTbMNUp6HT@d#T*wI;12^*|vkmW-=?qEB@{!AH>Xi~?3fY1XW7=#yXxmZ#59f|`TL-r&^17b!ImEK`=Wng$sjI=l93RVOe`>JpNcv%2_-?8HmsVQw(>i=NIZFrXA-&AuULO06Vx(@(w<dSO%x51x~hQ5RQZxYFX5k?Zk|BKje^qPi)TS$1k9veOCxlJ!l7^9FV;aJpyrC{zf4;dfh{3pQ@?ih_xrQxlhAc;^6S<+-Gbp!+{k#7{(I%Z;N&1u;to71imbOhOTJLAaEEg+iLHr~=A^CNVZnrJ@ByoL*7k|SwT8%**|ASl>2CSz7u6_dmUHi7^OVMankhynE#jd^d!SMuj*++xP^W()4*1f$6hh}6&;mTAi}IL}L}psYbL(;z0<w3j3EDweI9NKZrh7f8VyQvoogzr+33!oaqz0>R}Jc0qL4*~2zd(g{s0{95KQDRam@0kO%|j|%6@#08mv6Z|nTm2jr28BF7b*<cPP?BZR;aB6ThY;?8?@Vu|q)i7n)*t{)=V(na!inm&QXGAEMq`(~%d?p<~Rw{GlH|xQ`qm@9VRdQ36xf4@a@;aFkwUy#*dR?^0Q;CP$BW-f2VG`yB4i!!82n$S%(%q1yfJT#5QD&f7PE2H#=JHiFXrcu&KtRjI*(XX>AXu-&*M^c`QU_<QYyGPW&+65=<;(aWH7mkltXAf$pQd+X>OV~t*HL+OlErR_Q{^43*jG!@#4eFUow^}hlZD8|9k{dG)QHrs&sF(WG|9y4UXK5jlQ|;qX%l3=Xm@$KEUt1;{o>ptau$NUI5yKOy)M1Y-FooF(KLYPi(v9bwR|3Jkob!Dbn~e5Y~@?sgdI6T2)&gP?Sf450CsS{;9k<9%?Y9ye(Xn@f272yDY@|{QT<9k>BfO8bHZ#yRJ7wfW{escD+VzW%c?k{{Q0E_wOaPoqugS`xAs->r?Ko8Bb24dc)=bq0$EG0OLluMVsQ3V5$ldvxSosZUR_s5+c)ArA6(Cc)U!<)-!y}A_IsbS26iP8U^f8~6>Fg<HgM@T9QKVG6M3q=^p0OPR1>Knxt;`LGhWK5evT0^JzavS_U_{2&6V)L(6nQ$BYJih@TKANBXf)LAvALEbqxgGHjKECs1Ish^gb%Jj~idf$mR25EAh|R*cfmoNB``M;%62<tX^uWda-y!_jRJ+@oZ(BZ4|-9tZ(fcG+=BokuBp;CJsL6nIH59xd%S0C%)a0r5J~>T(msvEXh}03Yrx}lZ>3?vFhpp2T|{=4uxO8&`M}wm~DFVe9<bD_4e>3_X~XMQA-?2;M17|fWj%YS%$K6OMx>Tlfuu&+2jUf$xEnk7Ix$*sYZLqY3?g&&^j|X)u$>e+)tVu^D<l2EL?q|EdtrP`nqm@xt7}F$qPN~?c8bsC@)s6#>6_aaklLadXryJb#3}!zgW*h{daAR(m$i8hZ3WWl7w9D6tXv)zF@Uf$Py1_jb+c*oc`!_m~cdVc_2)9j~oU$I&y~q)NpJWcV>rTn_qy1xeUfKiOMB<v~Z2q<fbwNIFP(F9>L`2T7gRIcEg!H^2*)87oabp=RJ@DJ%z@Qqy+*8yo_%dBNF0U)<Fz{(f5&R4I8Y)V<NV<WK3l_+fh%G|HKHyX=c4Z%0e(Bf#}Zz06!(kE~ivJGXJF+{Qtd=j|EEvg0&M0tST@uPoGOT7Yz+ojg38cQ-LX)sDoEK7;_oC3e#bVg!-WGRB3q;``l99n(CvqDXe0m)R-FcurC*`l_1lU55s}WiBZ>E;ZlNSh~C>~?Q2H?s>#|eseRE;ZQrR6YtGLp%&2}(Vr(!+h=9Gr)qq@B4MAu+42Zl&c#WL_(ED{UQAmDdAFW!w@N11K-#USgti*{K^^d-))C5IV1j*YS#XdUg!rVWo<^*S;)Q0_oE~=#L0{t?eEH6J-6P+wCz5}_X4`Bz#CchIV+pLv<HUeAMDTJfe)gh?mesl!Y014sWa1rQWy6ytpA>ppA&Qr_w!0-TM(_X7@d4aVz!}h`KU4u0W%)rS%h4B=mde6KMXP%B2YkA?cG9LAIeAcQ)`Y*vGTWirX=i3)eX1p@MqJ*)K(=>~lFR-$;UP!Pe`~)S&N!W&Dj^*X}Q`%Flmput+#FFD{hERL6nU@d>ZpcWfo8+^otUW0HXyL$@sY#alXvs#eED`9MiAVwJ)+-!q)Lw=UxR~5tN|?@1LY*i|pb`>Q`w7*&XJdc$SN{p`=KP$Mcowuwm(w}3N3z$m_l|+<y;PZ|{nkLf-tc_%&*_Buvp?Z0gS;eJwfT*S;Yr(iD5L-8`5k*uIwucr>>J}W6Z(iK_at7qGhz3Rx9f>3B%5^Iyv?B&732%StWO&2X&|uxHxrSWbQ#E`W163x*}||iMOqy!IuiHDY>gb5RR^Wj5#^DPHpZE7?2h0{b^PkQnQ|O=GNozpe{K1f^rVxfonKf`%{MS$g2~D8{Kop}fyy7WYZ&J%J-;&3Db~QM_Fg#>mOtT4Oyz^JLkd^=!15>t6butKteK)H8M^<Zxg9yL3J5*eHYgX}hpt2X4$L5RDg;r$!rT)4Krc$RkXbfkZa$(W5k<6Tl|^chj1M{G+(H$5&Y@Tn#46FC|2p+5O;{&aV<zVQ_@X0X2wx4s5}(i9N_1Ek=e#~xjn7%U>QNH$)rUjTm+BkK_f9`Ug^@~+Db68feGN)0=I&RWOUS73&Rrbs?5CZW<Sz3Zf?E6>7pF0wPYqMO*{QjD4P{hsd*F2P4hE;*pyBhCX`A_k-E_jH@TzWu>U?2K#*a8tRbn2?!LcgRh2MS;2y%%G<B<SQhjL^v>0PIuv7|kvk-*A1@O*pBQds4=N$7=eG!ZP2N7CguvA8%yv#c}6$h%sNAZnSI;6{=e00CuOfxhb73Xnu(NW&ovuPfq`Fk6$-?9A)O*Hdne0zl3~^tR`m@2tm<?hFye7>uLeW<wsKAnY(d7|UZZzpDt1eHDig`7+W!tK<BCkaxsMA&b&%X~eT;$1=Ejb^+}lBIL8A&ZZuJ$mmL;`qD;o4@DyN-+q+nw_Mu(X7p=Nv)6~d0}I_=8nwZIIYOJsY-Jh!BI~AF2aZ6^;U$QbrEepOGts?sv$M7O>k{;tVqm{^bq+)m8VhK_B$t^a1t%v7cxFPAX}jkPpAe7EU^{L@%e`RzY5IgRK9ArO4MtgDaee{P*)>+UoNziA7aNOm@2gZ;Jj3Y_8<V&()0i4Ko!T$QO(XwPzFO8P_a9jmEdCqKpIvNHPfZGSllpA2LqT5<sC8`AUxKeb-T}o!00rqa>Kyby@RciZC_`|IvQxPj8zOd8-b6hJ8x~R@<i7M~eH^{~WUC@Idr_^CTf8|g<1_$EcQPxrXyqP(40=s)G95%L&?qxVMBA$DsguNWPmR?^oGm5r4Gxu60AE;1(9$O4JHpj!sULyW>~#FZ4TySCfIoONa?3#my>g&+a$8S^8x9K?WUl!dL$*<SbgGuMz6#ixxhNl(Z%8IT_oFx$a))3g6gm&$G#sM^;wxeqgMqqa`f7&5{h!}|xyb<gUSDn|e#3IPIj1<RwT_q2!NG_QSZ-Rn5jECY3$@DZJxz+jyw)fz5jHD%>Bicha$YSlgF9E<rcmFkc#I_mSFo-!ti}f3*(z2c#X@Hmw{R=+l0HsU4QLrUEz|6yyTyc12LNk|_|i_Zea(l!79{?B)VHJDv7!uW26%198eU7ovIYj*0Zx&&2KlQLdYt38%u4<j%_XlE$#N}{r3e_vo^`T=kB2T+^hl#+9F4-gyss>yLHbi(26(iw?$N+4;ZNVhd(@u-qw12^;7WH5S?Ue0F@T2bhm!%<vvlnTRo%FGMLE&ZHE744M@!7kP7PMN(|T$la@RzFpp=IlIJ7K#0etXruH|OhQ7T1+$_)sk>PULo*&^ISIyO+z6l{Oa2+G0|rm!JottAhhaK89G_giABvbYgIeH_cVv&s?((kRi$Krmy6a(#31@egK1t@4Q<8Axr|v)Ysevcq7>EjfWD8jAt8sX;!bwtW2fY*~w|rMR=iI_2tid&lGtVOvioNr{BUD$RI+@`x0pqqCa6KXzWp+ypO-YH}w(CUfa1C-XUw>WIms27-5Au{WBDjZ;$~2J3{X3#ra|qGexF{m0XFyiC-ttU-Z`rnqkADS~Y!GhJvgaJ4W2nBk@3#zhSjU1V)^cx6j8@czgh&J(l&d1>6MEh)x8TF@}L6X^|-HF)r&l_v*()*$g_@Qc4<T)V>xg$G#9oMFWz4e%A$oUZofJFZ|kVnndGz~Nb5z#d>rj$oMpT`M3gHsP-ZEFYuEVX{aCPwMdV!rPk>G&R2ss3A^aNNw5Aq5P7SA+iA6R%UFHDA)#P@_pajfrE_Y$#hz|>m4a2QF7mtSFe;h<>fGaBg0=rNdaG{gr{Fk7JsylE^F>rGg*IHs`x1%W5N1A-UmEOE7=)8OS5v@Oy#R0IPU^Tn-@S@p#UV~gcq=gMEvYIc-B1SFY&V%c5E|jmI25aY*r+aae~dp6<{`B0%pCTWhZO+M02mJier;~W31@kD~e+(WW$5tCA2L2btTCI+3kU{pR@;@w8j|ITTwftS80urwrtg_bFHy7YmHT*F@@<%SU&IdN^T57JD*+|7T4iFdsXGY0>B0A`xd*kYK_&Q8Wuy<Z4$8y(S$UYVu$?{0D4w`r+jlHDpEL{$ttihb0=*Nm3AKlTS;Ex%@oSpGJPXPEK{m#(P5cAY2(FUbnF(mNe7W5F-=Yv4AuKw2jHbuV62>_DE$zGZ1S%d)lzrP%8BK35^?=)6`baXYpJh-q}5>{ceTvWZD#(*P2CT)PW*j4QRF}ADEs?g3krUMtPcS8&#b4M2)`|{%7J$yl>FQ0+W(1<xWF4l{Li-j@11pFf;T3|Jv;`5%oU9qkfBjiy4-^kZa7{8VK}6p;%>ToZ;=N171+~{Wd^V&g#wsYhc&5h79i_0;-hQYAlA!4Sr8jfkES)BWO?*gKUn5<u~|&)tt+x9ZjpcS1#h>T;kt)@XA`P$*iFZoe8X`jO<9<!k6L|a$me!5=k*<4`&QmZOQk@~L!KLOIngBBq6$41rZbRH34W8CUZs5${O6`7sN`Jvdy-l^GFqdwX_aI-)&30n6e*^#mHRhvt&=v;n%XKEg^Artt*vUUfSIW+?~>s9P0h^E{?{MUBzBbA`8AW+Yyx)`xx8NUF9%(AvL?`-Y-t%ICJ#}a)hCuMN1DVk^`Fc$xUdU@URQp>d}tL*s&#k9+u>owjmZnc*uX_PvxgzK*eGY>Xx17j8fm^;u~;Fg5XdW6)p-EDnp`$+5ovNd3TL4Q*^S;5%lgT(fMp`wo4BB`b|6_>uHO*=h5&?8_OH-`+J4#;|LOf4K1^QuhP_7^oaXfTF!W@UI5YX^E6_)HC*M|wk7-~M7<oB1<!<Bzq$kv@d}`U94xGaw*tYEb(%T#d@66_5fqLS|&9bHE%eXSfXNp8-ucn3h9CtO6Rsp@EB>5dUMa1HBAX5@M$Ut$TW}|_~AU9ONssb5SQRQag;^cYhr4J*W08^o#oIJXUjEarvN=jbWOO0UR4)ZKjTc~P74BQzctEFw^eyxLQ@VW|<b729&t!BS6?CcB!QXM<=-lpCNou2xeVYcyD3I9d2@z7pelGbMq%;&T6{Bq%5*?5S@iwCQ~eex6j#%(<E-`V^H*LH6AbASTuAFx=5zmZ~qm}9tsZ3&JJ%@|2!w%DgcVa)+SlmF})#5AlO56#B=FU4&Ls@(8j`4u&QGBy2p&!E=Xp@`e_Uq1Qolq2x%&)5>&*j5fhiGW&vDs$oqL-M-^@-M}eD{qH507QApMj`?zM((e!BBQU#XbQ9Halha)$wfMNqwD!|Iuq!6x{LjuNvB`vvP?o>r0eCd2y@gV7Guw}kFEW5#$}o$2g6d7g<K{HZW(W{pC!1^rP{kJUL4PDmS#Dc!C;Ar58hrM2)ME)R9I{TQ=p+zR5{eq3MJuRd!KNCb-C~pcK_5rP6II-6bNf8Ow?D7lk3ZhYv|(*(`m>nw$efKtZ6pv@`CV@%OXgCk2R9Fywy|xn63*F#7tB{7Yu+4rs_so<-koxKV7tj=<kBCUSx$;12?_5<=wb<rZV86w~9TM!~<^E-Z)f(cSZs&)I5TOEpSVs!5VZ<^%QDNsaI{Bay615Jjhk}o@l|AEvL3x=MlY#SfdA5N{&;w@*U-#TQa7~T&b4!F#bqVu^L(DCaibl4io<5hZH{A-y{nTv;2{aiHRdUpI|k)*x{a}u-q^&C)iRDuTo;`1WPZI1^YQ`NTJryG{JyjF{Yri2}T1UGigHgk&Y`QvK&-NbK&uf8aP{b%&b_OTHG9tND486_KJ97&oTb4X<s5+p}Wy@Yjro!WW9oP)da{3zI{yrX{H@s$^s2#U2hlg66QGlnv4*n!`9f~%hfVVtq9<N#@wA)v*azU_mfHp5}dPey~54AwJ~Wg)&rN{R^FtVa*TVXeDTf-oU*epu5L@w`DM!Js|-yN!%kg?P~{J0^eAFLn1Ql#?XGAZTlU2VL5VRhls|0sHt8fuM&N36X4WjWm7n=A^J4)m933$_HT@Rx4YfV240$sJPzn>40>*9?BpC?dTi}EG>&?I7+MmK2gl#a%<Q&+OaTIA5Gp2t4urWP08^wX;`)zP>A{nj-%0at~i7UOcRv}eGA`3EiK}@$O9*ne=s7ErC_m1cj_9XEg95x_-5O2<_{f7Dv<xc`$-KgQ#vdQoFV26uvh|$_mdvxEV`ayDlN_>+3EYVdz^<b`>_9yAkvS|%<7Qt%UfxK`b;ustEIz9zXN|5VO-7<$i;=4h0r{jt~h0j1v0vC#XV(RbH0l}MIBbU+N`-VXIs*v?7P(He_Q?dALok|o$Tu4ZJ3Jv)nOwx^2X(Y&Ls#7^j5p0X0EkXqhtP%M{h;-4Mq70N@5&20eSEfeHvQ$+;0=<C*%*w2<>XtWg0v#zBT52MNBdjlKz~)3jfnc)x*b%8`Yd&cb$qpA-C4Yfc>WNjNd3e>?zl{^fVOCysgsv~vh%x}pUD4HC4dLC7xf*w<&f-3QOU_S?n01KRnM>~rU9uAJJHJ+(k*rMJ_&D;G|IL6zXS2>(56uw&wT*VQRE4~Bvh1mLk&Tg(YQus)pXyoE0q7Q5yb~Cg;7&%X{5fruYHGL&2BoH;>i@O0C7CI{a*&FY`C|IJidCIV<x%V+KDAxc2r{8pu@Zx|g)KX8uJY@8MZo5{X4cH1nVGJ+URX5}+qH`XzqM0CycM3w96rk~tj*A_-l}CMU$)tjmgQ3Op{P{hV3E2R+*ZSAVm8e%$XYX8V`H>w)OmxBlo@i@O)M3JpV0jXeyTB@HT2@_AI|i~Oej$LpB#{d14OXdeseY5{70JK#%vgWy7B|C8Mt_d)e^LTGRf`&er3du>UnwGk(Eg&op@@X?^(v#gNptkfoS1L3JV~laH0IHeCem)pG|^SA_Qf4bil>>)01@n{7@f!_GAFu@{A_ODdNcG-W-&p)#vfwgG@WixB!-&%1%H4<8D2gs&%4?f^;-J)f_wlJ6@6se^>LnuAOL>e+U@?etiPau&YQ$*cBfmDSCL)KQ;p4*q<IrntbNtDt>G%i9^*gdlTIg0K)E}5mMMa@q6>Z9nKmrxNo@dKVfCw@=ra|N?NWzAfh307vIy4PYXMEdOS7vxI8#W8HnY8`$vrLFUvit%0}hdfB$70M}#}JAxkcdEn1BHdlD9ywBzw3m&y&%A5}EpPvRoTrbyqZ?sEaK64G30=4XZ_(WHkXq7Xk)8Z@x08?*3t0ZmLYEW~0e+blG#=sR+^0f;m6y%dfFL<z8~tU4fL0oE77$WNrKjPC<0?qH%tDpUk_@h?&kKR4s1s?~1H=TSd>GrzdZ=xrH%cPJbHJpKzG;9~D(a#gQ4O^3oMq;2^Ih}*Yp+s+-5GEbSi2t-DmX9x$TjwsuNgS2}_dblhBDkWtnJO!pPVI$&LxtMpjHUr7OEPjQ&L6F>gg&Kr`ZOhr36<<8z#S|ICc1m72ugZu8G9ID-j1Z0b5;%2Hg|I4zB)#R#_5L?L$~C)hQVwY;jB}@~W*)K});46zHregYhb*H$hJw?0C51(UwG}xl&&<rc7`3qvLgQ>XWZT7%-PR!sOaMh4%ZtgwB&wdH7AMaaBYLRAH;~3pavo%cNT+Q2tAn_c{2#>@dz%u}jd=Tj9@(AP<1XRt<;&)uZvKJScISV<>g^k$sa?A(ODfu^?UtCdY#LojcD(nEP+?XfSoG*ecFeK(33Mqd?tO`OxywlL`(UCqK}`iU>&HgAA_^I{3<}C&@z=*jeA7spNqjcyYI>BL8zGy|jQh*0?!COgVXpS5?VWW+8df{yA%CO{-7&iKeSi@F_uH2+lv}6@;}HT1(5XG5Z20h0B3ndgLu6ozf-KB<chIH+ekC1!33*NjfxDXrhy8PWg8W{7LVUBOvJ`m#whcOWBnKdbCk0J=?`_+{02rn4QR3lp0e3LL;xlpch`j0K%xegz7sI0t_^3Kgh!0pO%XhtZM8rPI7>;=VCVctOeBRh)=>Pqjq_xj#0MYSce22~UT!HCo$n1INIfkYJzgYs&bA$1GOgpM;1~uxu;f08aO`YaPL@BXd$c{vlzZL~k7baJ^9u|HZU%6Oi&~?&|1^FBm5=qafeKlLh3s{aRBe7%A{nStL3f?H8LP9*5pHH+8aBEuEieR?<>rzO?o?mFDC?a+44orBvjCNM2_WG=ITRiF5k{0O}hfVXJu#K_?buUM*@@P<6(kLYfWTwuC5<xaf#em{I-UtTt-nIloSM19wwbTFO@33@uh@Am!e2=l%vTa@#>T%1WCe_$@0Vv@YQS*`XSky8?dbKKH;sa-4Z+6gGX9tUg%qL7FF9D@PV**5Mi9fIHjQ!Edfo73#l>83OlvuGr*YxCatuJSK2anHYP@iNayjXSyDbd>6r6<XMDGyJA@6x3BXacb?#5gn}i>fdcCG_$4V9H4*{AbGY(qOlDu6rPa-El58?9iz<S9YblI1bE~gUd%W7)ED{ZvFywon6GTHIC4)p)?_d7e%HJrA{`;<xezoQ$QVQu&h9E%RfnSyM&;_gVjvoT6gcc4Wek@KeK9;n?2fQzI(<n-q6E2@o~oWgOCW=GmhV`CPn!_ezEa)qxqB@h}E~(%1Z%sva@PH&!G`%D;6kPx;-~2H=x*cjrAS3r67FM6?m*^tgqXGaFgPqk!MR(VgeX<Y@%ViG0ojtSN+aXa>)dR76}+)hYCIsxz`+i*7%c-q)EY4dg)&J2?NX8ID@w27Wk7W`4%*CJNka4M7V1?fl;Y3;NYN@@Y6rPOp0fmNwXC2SHtn{6H!URUwxb1{ricevs|>V%F1Ut>1z%DE9O$FUG^@y^YZ1HPP(V13-<>UpG+s+yzgM<jHo-#I_a&IXVfl0t0XUJl<kE)I-3`5P%aQE)sAJJ)_kN47{zf~Z6!>`P4;(hwY+QH%y*J-lj|^j_g2ItMjZ8p;C7Cb;Lx&a>Go1xgXzdrwFF_f{LLKjD!XYKiBoOnZYDLkPcGO0Pc^@T`e*wyjP?f;TWWh3pR6{6G1yCf5jk&rf+R}WNDj~VS!P|@yDmzut7#8d(e9x3g@LeTZEL?bay(Y-628(5>2bu&>@($}`>I)1cQ#yfcn!Pz^4CnTL&*iB+1ci3)o(OLGZ3<3r3_MgF~)mn_fTd$NHT1sBPi+BWl*4OezYo4xx28!JR0e{WkVa^Jo8tI8<by5CMvP*je?Z`Q*KJQ<D8$3Qv$J*cxR=c+)ByA9KqCb_kZR?x@a#u-pj%=Ta{Z%?Ddnv@TDf}!7e%D43>q1p=;x`YgE{*Bp_RFz3#*oRW|u&tO6j2QQK_x(hf}?=C*@v5RD)ucpl}H-is7V1}b;Dvg&WWZt_43uE2+`_D@;hHNS$MsE5|R1FJf8v<^_qC98)xuZ?L%+iXM_xtA>y>biCM`OdAZwGZXj-@3{9gRM8Uu{_jG5*vT;YCbrVk`pYn+_dtiEdn6iSgz*?7dMb3Kz;`*uK7YD&IOnR?65(4@=OlAtG>ikyn^MmskAb}6Hg|yqYG^U{#3Fek<pG|L~@K-Jfo0JuCJ^i09rD9T?|I-^GY&I57X=QZJd-MG^vO|HDD2Y0-3ir)}Nf5EYvowq-V{FSE@BUENNLim6j<+!^K=&nvRSuw#U^XPLvX5Er!a^D253^jXk1eE*04xZ~x!-_Yk0gz}N8*NGlJ4YT*4U4}r_rZgLMe=RmcZt8B)C1LdVSi2FG*isxyR+kVqJfR;;$70PRFF`@3NZvdw86($t5%hga(d5VyXTYRWI&GQYU8wP=%SW%d41ZrG312gwiXkd`cW}%HL($r11)TU8IxN&`DOO;F^&6WbFB0ICNP8Y5M?Xu@sVG4;2^?TD?BcX+nW&Bi|`QL6m&3j&rH*mQepQ?DvE91)t>n4;1sBah89#uex^K|BLw`iERj7^POua0!H<4A<=wR}xOQ$x?@u$&D`wmqd6^F%v}m3*&MsBiSwVM1DY>QwXRRuufcHW_7?%vo4_?~RCt@}QS-Gn&tIv6Nh(Od+)#tNk-Fo|9s8n(fl6Pa$)YfummiB(^*e%OZQ?KSCr`I$XFIdg}#Ab6b^#!St$eobtIFXC7)S2{K1Jw+51pnkMDa8c3V$BK&Pk-nZj`?FpNmd;7uYLw!}F8U#iSOJott0p2W(g7lYZY9JRF@r}y^7W#D=d}}k6g0X1*p`hPR9*Q-W%qG~v3n=}7U@2bqwoOO+R74!#zCM@63uMt0ZIkjgcnkE*<db#86<S(<z^%NTwU}Y?L;JX0{u-xW|I$+MBs`T(;+o(IW@kv>3B+NbDTE6<2m})88cy#YDdUKn9>9s+fmUC(77$-EhlbyoymO)qHE!TwYc9~rlFVdXrmX3omoQ^&VlBM2p}G~cSPjWCqxOs~)9jOP0VmaZFjegAr>U}f3m!}-8NaE05?HEs)kkKND@cK9BUu#~^3Y}@Xg@gVZt>R9uW6XN^oR_WGTMlA60nc#mUk4qF!Du!&V2<O>FtW3oTTMP%K;=u*M|DMD#7I4PvQv4zHFRSpxON<xX0<*8V+Jsg4;K<1a}9@WgeZ3qEbZ#p(XskzJC?r>x!kEm8forrO*{NtzBXJ*%j8v_r9qmgvlE=8UO{G!P3nBY}u6?>10t!jTHYjpIG?{D5I#gg!gw_bM6I4*|!<4xhDH+xRx&5WvRqUB^IdCP6{eeDGes%G``MlZU1S@48PL+t{Z;<;>zJWBuBIrCG{D)WvpL^{7je9eH4FPFGye?5uW;BJ1=SvBrKN~=SL(|Ewk-`s&i=sTrR2d$!d7tNYvBNIC#EfmxBe=sD&N?`jzv=5yw>5g%NA{b!R7&s{8XmdzBPS<j4Rb)DVRvM=*I-0phIDc+x~PQ#rp-H7H+Ult~cTR;b|jfCVd7k#BW0nl5wU9lo-!es)87{mJ&hV7gK<{pI%|O^hg!-oQkjXFJky&Jr_kVRIa6xStvq+`Kx(RE-r?DqNPXH<%%*cEQ(>G-frE0TtWr>PoQ8fa;Pk+KDy~Bj{|>=0XUDi4#_EY)zib8jYc_TZ)f*$*Rj3hT#tZi^yBg*z;KsFtX>PVz*kB2qw}v<sR*VDA`4msf>bYt3(l8OMQydLWg+MS@H1U6~)6(KC9g?1JxDW=BETkuS)HE`ssi~v?w9ov3R&dc$JIR$Fw2j83h$I%+urt;OUHhXg0*?Z2F)&L5W$m8-S{|vnmKiOZhl-yRr0QE`2E~H05y|MXLwa_Xb%A2?faXW6S41j|>ws3Kiv695{XT%w+dc{ym^+W$npPiw>XpjDnEmq+7O}d<92}PgC+7peE3+DjyV73n4M6d2VFw%us8GyM0Fq&s6996yt{9UIv9YspAbHyb*BpM8aI_i86<vj)BPIC}L755yplLt6jvEE~nEI>tXT_3>OK&Lp3AuHH0_HUek0a4c%VC@7#>^bl5~&gM5t$CAS9=C6%j2^V5-WOHiq(WwV{gb+y8=&X4$X6FFl>r6K{;_n>X(*korJy{f*dsVxDO$(F!4H>7eIRiPD)!X)<MXvL{ei4Nt?^e7aQ1x0*rBF}c;%y%_dz=s!OZ3DdC!Zivxp&TBhOw$CFrgr5mziRY>yXL-p^+(DcZ-{=USaLc-fpZguCMHfA!oxA$vm~hvgjjm4S9`NIM`^wUhxd+t!XjhgWeC3ysJ0zgyT`pB5ID$oK^?ZN=N(Od?y=$YYP-sOV>EFw<0h~M)2fMFo@pf@RhBaAE6TMaIz=dr+9D%`r|`^BfsrW6g1yp46KEHz6SwUM;0SgOmT+XOE6yTn5am>96WAHi#{mr|0J9JZ2EHz54mB`QiP;y8>Gys=N6QOacL>Z{IpAwW%f3d-p+?Kyb#LNZ1&CYCw_B2fCW6#yYrP1Sjh+Oc-BqzcsX(oi2KQFb!<zD%9d)HKSeBJuSsD>jzuNr6A#U*x!W~bT174QI<>wprT%RbK8@QoyHU4e@vWXaF<F0_L@P_1O(cF$$%abu%EPg|!>wudxG7ud#OJ&h}vYeB&=|~qll4`h1^iu>_4)_3;{*FS}vanRq*DT)nvjm^JM&T$G(S<TO8F!$s^p_we(rL2zqW!?p#12N0hz|A^4QF?%QV2R!8EZ!buE_^e!#!xC+6zYV|7lyu#o}Z-HAcbtA3w^}U3!XNOx+e@v0Rqj>x4le)`Ft{*#zDpY{l#irsEA}sS**)-b7{ksaGz9K1WJt>8>?9p&(+)&zQj7*#vH!OlQ)hOlvi{MfuP-0z!7q)J3H)RMTB)e%ie4>bwoBELW7&S+gcqPq8jEgKMbAh^rU8xD;=Zt+}u0U&+?ocU1<qYS#2C1u1{ZGWxMe+s!&spF*wXKmEu$Wz+OiTNhGg*iB5T>>7gOQmTwC8Df=fp+3*F;)PV%M2O8L(yDl4mSg)fsWM7eF4fAyS~^b+)mcq|T8!;1SjG)pSyyi<S9>8?)-MFhN}y4u)V`{fxihu0tTc<x&|0cG?G!7uGHV9EkY>$NWuG*``fKmsz3jQ_eX#Cj-J4z_pq(o?zO{83&RowaSx^-m2~Ll1u{@7gEziTs@7!0v^Xm$ZhDI<7c36lwh6@qLZee-u!<AlT#|yiYzsoB`9J940v2#pq$#SR-bsTYU({a4smW(&sl7tp5oX$U0PtyIH@3V2g0fP;_N3|c13zc1l6}b%U4aMVBx674f5v-;QqHYFqNJ_IKiUUjv?#-I}0d^7uU5*s%Qanv5FDG8asLTd`m97a*NI5VES5Dw_t{^=rX|!7Q&m5lMY&;k;?FnO6-EPj3d-0(0r#IAJh^_fpj6^t-^vaWen609Hs9ow4hJbFqqWsNbXWaWH54QGw+GQ*LS9Z_Ku>P4>tXXF=S}*L0<O{C~kVrRzEmf^M-xH%LL||KNVM4}`bg?-$>YI@?O%Y{NcH>gz*XvYbCKK{fOAv1?ivmud7osDGvzqzQUQkC<jwnfM)r@FYih|MH)45GA@f85qT6`KM50XQ2%Z*Y)Lv|4X7&)LLn?1iKMIwO-f?8b90kuIzAnGC*_^oW63lzj?l^tw1FYrq}m6d78Lt$!6N)5VX{nSuK^8MN<;^PjwUu*s?H~vk{^U0ZC^k+;=p24wEf59IqR1X3@^o4?S*X4Yo2TXsqC_}}=KG4=VwBFd<j`h~D{OKrhH%OGU)h2B~87Cf2r2BDy1T&HGTF|s4?ly}`T#f^CLk3(#wQcpxoisA-fZO|$rUzwP17qp(vb^V~Lv+9L&Gi+Kf8h)A#^P(HhcKGawpn|W7Yw`z^Z{jMOdPop?N3}Bq?zKfs^J>bDah}0Q$<b(QC^?1c|Gmb7nQwS@c-Mlzrq3=@b*fP#Q-DuT8_4;uuRz*A<gcrB?;wy!V|it&U58x02|MBmU3M>SL-YS7zJ-i00y#Bd~E&ki95$S3%l*CmY9^wMap)w)Dm>ZW!_=ifs`7mEfgm9;GGElbNY6zC3#qsTIB6@3yUGY)Md4$`!@71{_}aCI=uUU9d9cim47>>LMye~y)UDc!SrQOLFrqEaZ%YF1n&;q8RyYz2we(>s4BP`uzS`G;9AIeFf7Umd2%X|*A>&Ej>4lv-f-CZ1rood3=nx`IS5{7s?#l<;05z@wbHmQ2Ciy={pG-HIVug#i{imt22`P+lR=v8H!Fc<Z1(FiAd3p+I(IBo&*3ure&;RnEs$gbX<itE(*V@yo5#y??7YWg7yi4CvMg=^z`MRIis|usPn&Y3w-;+-OGZ+4tUq595hAl4Z!nD}8X?h&R+BW^$}#q$XoYT=9K+k2Rp%8(BUo&`C|bP+oxu=kZ2AbN5P}ccOX|#>$h;`}i&_;-9<5e&Fg&>@+X&}&=$4%3S!MaSkXSy&Z&StUSFDEJhxk2IXAmNN4oh1v>DnhbZ-@8?I0nlIE!)IX$oC35SiL^sPKr(_o&%z-gJPlza9|BvK#AVmpb%L&B*zG^R23*;VmJw?NNp=CcyZf$Y^*%Mz15>oi4t<Tx{pp4WF_1U`6Q@?l@=zktnk#hs&;lKsK^6jK<|Kx<+cc3qKU^^KvdE$Kk+e{5>VU&44Kay@F`nTqxBK~=p@MrxK^212MYQ!RAfn>c<Ab6uy_8uZxa{-d*F69G*LdvsqT!9eJLk|Xb9chYqi011wBiSQl0tK51SQ&Gkbt7<q9jk&{7_G%UIT9<w27X>XZ;Ioeb8=jvV7!1+4^=+P2a<X@KQ5MWiJ~L@AG}DUX>$o01W==SEKFu9^I*ss<3@GLwlFca|<AqLib%CSGRG#wnSCl|}=p)@Dw)rzFTvNf31;yQ*92XOleiWWTv=`=?$lT0IZ05R6{!t|5NX{i-~OyIOTLW$LAY5USb|$;_4q2_Y<ZAMH4kXtlo(tuFaY%bo;<Q`x#$<lNEReod1qQ0%8)NN-A_a6*w%A_|}m(ynGPPFLNgyGg-WNK;1AY^!>)ohcT?HuHt2ITrA)>NPv#8QN|Yg{c+`2DWzkL?MkU&Q%9*CXmo1v9;k=l?9}zZ%pj>*?CsWHNQA*8_U83m{2UO2E3_Jg#{vFjd`t)4Y^BeB^}%os;!IVs*<(lO&u_3rSm$6uH47UezZJf@hPs#a8G8(Vr+DxQ@|riqHgXgSGTou?gYJc(*f%RoEc%&cxhI?=8N+;m`MDGAJVem1-RWr?5oK`|FTcUPT;yl_5BQA7v)qiwR~`d3}GM8zLjZm4$-3^E({8);g?@%w)wl-=5Z!^Dt7{zpbB5-DD9`5WJ(6C*)vY=GzPSk7NzLsZgv@_vw?3mVX~%yWjCfEWhC1U%)c2dTamJF^B*vl<|kGd{X_4unq$%)uMMR^9-g|2*B5l^_Dr_!i<O-kxs!;#hMTXApJ`2xd8u_7<k=4M0p8YD#&lfV2cqC7wZUj>7GrlC1+(3Gm<0!G-Z!uH6v;D(bqtC)X=8@QFTpBWzidHtb%m0v0GR=6vjQix0>83)u>?ZoUM;E4zJtmzhAIc%L!KDe0H$@kbF&cPq-^W!vhM1c=$MmY%Q)*Mm`~Zomay0loU6w1IOcP;mbd@$3$)Ttagt4Jj6+ATqFc%Ay2T3ampi3zs={#HAxKPRyc|u>b^1nL1te|~TW>pro49-R1nN0YSH^s9ll+P0f$*yBVLEMhu}QdDrE%UTKEWmt|A&w0Yjd$lXtZx@`rp=x8((y{3Dw<Zf(abX+-=M<<hsF4rlWYODfzr}$lZpE%(Q<5XC60!WZm;!#G9TDGCedL;75&(#56{xjYOq@n>IIXwYib1kfI$phDubs_GisDQnKFcYlq3$gZgIxO{xUNah=wCO!;&<-Q-s}-B?8TiKQR@iPxx!A@ACk86F>>0#4}!2uI8C5=+}wm!|n{d3~nZR!<KCf-uT8?#-*37Gt??*0~va|Kr{w({f`0^*-8yJ33qa%a~DuoupQUd;#M{#pEOJ&q;i%Bblb<#4;RVAskBwZA|_rYg~n@gCu{%2Ul0FBTd&&Zs)aj;f*F?<`~rvTAb;daB7~2Qytk(+c3A(%e;AgnTccg|7PW&_&VrDdfSBek_UP*HVpHee|v1$*n(~(SfgJ$JN|i)SZ8}9!s;9<CM&&pasJi;qlldb#a_gWjf!+<VIvUfQFiJzY*f{6`li7sCQw^BoA%}5o#^CNB5-tm?+ra(MSI<P%X5D5uPy|vb<h-2SPkE?YKfsaEd*dDW3_m&#tYYi#gV%T+KBUtKq7Q=wJ~A~!DPgiv_MR1_~j<2iU(W#%xa6@e1L;^>iB(QD@*v(->9cYJDcW&bJHA*>&ez5?kMcYz+i2iLsQNRbB{1pusicGW*TF<b8%|yzuH45zv!XkuX*UC>Y=kWe-D4#;$vl?lTS8&ce?WiphaHsfyAcD9eb-#erj*1<X_+vQ%^LhKUbQHgdsBMV7I&ib)-pyYrqw1Qkqh9;3XZ%j*?<SD;Jqy;aV|YO|MBVAD7K*MFa_%_Yjt+jWuUey_wdc4Qsw=cnSVqUjM+#X^9{lDPSSYl?+RJiB^ZIdM1o^riRiXw1=u9u7dMN|2hlSYaQ71ZQzCe)2|leeH%;&vW?mt$>d(io<YDY2;WkB>9Z;?Uk`tJmA-RmJ5)_<0HWWa9*=J&$s3`#J9mAA5p%W@(b6Vh<sX}^AU#<|QdCP~j@&=9Tw!Y*P#`(@wy&Uk{sWRrT_|s#zWkRm<gmwF|75C0%#XUI*6vDZ7mbvvvb*_(cfRlv0J(qlwI6ihQT4TpomN*m@Jh=x3;M?!`VRK>8sj(+q=}5kB0*mMj>s19#L6lfN|fGafMeNo@m+5%g_3jwjshMT+$$o?xDX<pixy|Dz#Don(=q-~-c?S!Rc^(_Whoy0CqCpgbCiA>+1<Sq=u2n)8|(Kg+TnW*$B5EacE$#tuI0|QFN|86QRAX+-RQ0jT!62gmjL9Z*;3il?9cd2Kk7rVae+86c;U7+QoZ=Jp*ciaLmr9ePWUcm)hk!GCo!RpR5zUKLF=DM#!f$R%sswW|1W-kC1MID?m0})F1Y}N%f-Q&o+h3j7h>mU$Y$H4*eTm6IiwVdaLf^*LmS*QN#}(kP_CDHuH_4KL>ohAF-X4Kl*3q5syssoUC8Y#<c*DjvUEf<r3fuDTGER<5KeXQKulPxqAyPJd=5ym;><X#0=`++A7-);mm_EIqV12(jSfO-@wxen<yLKe8ewr#ANj#pjSy>LH+ifq)k7cC8;YcX@rMi)_hZ8|plArSN63zp-G)HiJ;gx>0gZx((5~^Bq%MLtmYcdML(h;dz53J}0Qo3c;}6xP##3o0wTOSBG@dcfsZT?0L+B*{f!-n-K4S$w@(Oe!es3B{w8j6Qy*K%lW!uw(Ru?N)L`F6{ckbq%d*7|{YwA5$xk_>g7ZN%WV+IJ21+qahG7^$4BpTzQwUDY@wvjLxL#bQ?%aSFV2|^4QApuiQKn#$OW#a}g#zKNWz$4c8eZLhEnLGDB`<&aH`|R`He&_AXof#P!v6^4=HGa0nl7yPM8ZjBLIYku~)Tsm67=YKrl}Tt=9bx(1i|xirq?Pv8Kha*yh?0K13cZ@SOgr*?Ks9>$*eH{n?3ApoiG8N5K~krWAJ^$eAi&@X#aR3=`rjmhjTPL83QL?)7(2<LAc~wQ`GokpAl&~fq~B9wjrAtRMiW=8i6;r=-5zMP(qYiT1u?~`OA`?V8ZvdV|7f1<JQ0=2YMKtEs)O$~iO7Yd5Yl(Z<3;HIM{4?G8tOD!;fnYxHU8=rTsgtITxW>uoFGTYtRsZC(T%J(B5CDUeoIACt?q$hM))fTh}^r`(-IVphw)M#qfH~xvh-1!aM^;Ef`M5ITh#%Tm_Wn%U<_d8AyQW2f&+rw)azl8IZZSoF6&&8IY8j@#b7p5%RRBfS}^9EY@T?YQTlvulBpdPV$6K&@W>IT2CyCNtLy!@T!^HCje)s>I=)*90h4YS6~@-fGjR=+%0fnoH<d2V`Oj2i>oL&Im2LgVMsgB+DE=~+A)`;QZTw?ZeZ?E~O{%|3zl=S?71QCwvz-XD9yIl=BESY?`6pB;RX(meRZM*w66A*(FB|&IB>~a~m7tc&UEN;ZMt;+XsMg#YNz|;9^{pAN`?7@3{J3u-i2h$KuaoB6*C8dG&$*H19K%R>GhrrI!jy|r6NcMjs_Eh-J#v;3W)5yyb6TqjH|is_U@gZhCN;wBJ1h`;%kJ_S>f}sQ*svSiS5|plXn9@nO^EDCUgzJP*ENip#63Yn#^og#-`o{VO}Oqbqos3HXGC%77Wx*8lrZZ5+ZPFHUATz~Q<cko)GY3|Ow-_i?S7!UZT%vC^r?kkxcj#dH-I}#=R)ftr4d`a#BsyXZIftwEIw}?(N3um$gt2ta@Qct3M9frNeR~FnuINf{M15%`k`vnaShd<ntbqpdi6{}CYqAIx(6JDL=h)x5o*`rBMy{#$o#)d!;FYrM4~tI%b2E|Ot0<@Hlrv3A?$c8Ztu9(Am)VOi8c8KYAhsK^W{1UXrnUMB5Bu}8fGL?du>=1obqJYTw^U9*!dB?Bnjw2$C@o6qFyGSew1j#-(G-f@oPn?9<G_cHt_yR6!I%^tf^Bjj`b6uY8S}dSxQ8dynl{eeFeE6nv0@3QjJ~hqyX2=I2+SOFs&o9zSfJ#<qFbWMe8rPXudtqG;3450l2DPIM(4Ajx`!rooLn#w_4mLh1*^Y(=(3sS&ym<w}w~^-xbg*!+-xbzS0Q&%ATJrWxkGbJ;2rZX(^NR5(*t%0IG$iE)-Tit7FbWqsu;6cQ;c3&^p*z?a~IR8tlCZO?2VPHm8yGWRH6VX5Y2iWwW>B*gPv=+6bk<(%34P;i7^m8DwCGS2Pk9F~<##rtADt5t9lhPnaYh39|FwJ?lqw1khknX4=q_=zz1;M3rFKO)>_yIT2B9Ct~TA>?T!(Smj3L%ZhzTV%J&PNU-T3SKk~yk)IAqAyyVZYNRG|ft9Nmh(y*#oilDB)!4ZfC()q8g;NltA;sVGL8KEZB~P6LmUx2ed&E7eW%$K(C^hV4lnkvcTY<40{phU*FR-@|C-d85GuBQ{A_J^Kh1J1L)F5OlcF0z3^(TG`a}|3d#|)qM#=vAfO-qFd@vYB6E=h7sk|PsttI1!PvMDK@vY%?WxDdWyzs+yF%BScCd!-tk7-GjbZC$@%X4;`J(CyKS?idbd#GJDIrD$?8hZQ&!3;}wv6M-NJE{21>2JekhF6J-{AOSg?2C_nlZ3UVpI^xD1--35_fy{iuWNR`z5u8!ObS$+>+j)Gx-jtDtpahc^j2+f8DE0Ss@WL=KFQ)|AzaGcL?-M^UC3e5qR|WC|I%4F6^zeD>iD8T)z49was6O>HTa99m#6I)n3wC*wdG&qk^MCI<p%YIzmEF9{d;>}g@my(Pnt3{~Gk!@S{$-_w8!E(yrVxK!X@R{+VXsnpRvTU)`VN@|HwQ!t_+G8FFgBTmF5D$mAgEI|8piFF8VfA3==vL`tovAi(f{2>?tq*AO@&1R1EN*Yd<lzU%<-A9s9vQ0JS<8^T)7e!VQ60qi)bel`^(6vGr)=!0Mfbu;8erBQU)*#Vo%<Fq_vQ5Arj%6D{G-J8)C;*h!ma+kycc*ll-wm3zWKxK*_*DxyiJ{rm@hIq;DZoV2IS8he!+<@?@}*pQ1jm|3AL=*nPFaep|77vYp>ANCX?FSf+c=aN9~$jiqf&ahj;&c6T;TP2;|o9d20BBN@%7CSJqfi*1AM3H??iHpTJJC|CFAT72QTq7_3wZ**J$F5`+Dr6XiQ64DGw=&wif+f_8bshez*S~~nRDB7mK_#qhGj{5I6fH0=EN|HxoD4E1InsE1Ymqs0XgWJf0WN&&K^tM4wC!$&;sS;GqGviawj;}Q#cdXeE-%W6R5J9LM=p^Lknkr&FmZYdjNWVW8s?aNttph$9`zBw;jkr&yx4KpFgH01uflZzO<9bqK2eG>W?K5SLqilYF^$gqSsYQaN+X!4O4;jVzUhw8LwrD#$_FN=Su=$ev6ubZ7?jXLfXC(u#VMy(n<N|^RI1I-T(4-Q_2$0K2lsDaRI3t(%6EB)NegG)*8a%CUUFVG0Bwqs4TI_aEw&l&aF`7>KB7Ys(xHN{2w6ERRv(q!fE<1*1^w%2F8jOab53a{K5-k$!HW5G#WJDAm&1+p7>CL#A<o9D#jkE$yZe{2Zg&e@bx~b9A)HbPtBd_6UHKjkDoT2a=xF2-BJ9n#Z`k8-a0!<IeT$<D9lyax4I?J*6A5?5XZr!tQpNu0{<_tSDqu=`EKzb89R-O<EoJ62aM4*+QcX9R`!}IcwGmZv9=1imXwS+7qxXkEq!5pzNC)%VZyufO9aJl5lTG(a?gBmG(qN&RHR&Vd4w>40iE?fh8S?8{PWLjfE3W=!f!F3JLZ#Y<QAE(z#5St7aR!Tixo7KEq6%Xv&St7nrIc86tMs8$pQAMEH$(R-KVyD!or}o#G8q>^x^>NYMLPDI+!N?s5)C7%)tJ70K#TYSeO&1JSZi|P0b^NegwB-oiE$0x31aCh+m}_znXR>#(t!Q_lePWu~J(3Z#8`L<EjjzUyn<OW-LEA?=QD8;CTu!N3qs+t>x26;^y2YU;-Mhd2P2~d_(mzYICCPxRDS>SGzIsYf1N81`N<jAD6jI9vazlKURZ4J{56l`TT+h}TCzESjuC(L>vsUFCXDJ^TUSBV@WMC0-gY?@ha1zZVrk?zb2ArG{ieOdJo15$U_-JGl`=)ao7ricAot6)5&hr7Ff}O%i86mkcDAby3`5!46_-cjx7i4!{(`x$4a=v(e(jIz6%QvpIe5vM`6!gE3kS`qz5Kmch`jU|Etcmho1M`WHuQ@Qc`aLtv8}}}8l$DULHJPa5d)vRJ!?b2^e>XZz|K~T=Vd^>bhGxsWlma8=O`o7X3En$fH#?X)<O{JL#uBz@rk0`_T^^~U8Z?HbNP)MGnka-qYlNn@dWL27B)WoP42GrPx;ZDO{i59?k1YJ+SFNUWhLk^VH9-seRY-XaQmTBwIRJ@`xV*_;Y2o~=0uar1rqFW$g8!?wQ{n`L3|choyoIZ*9kI9jOikqpc`tq!64ig_Ro#PnvUeC|{cS98Xo!6sP&*0$!W`Aby_2?1y>=%+B?#fBsMNN;{t!f#8=6j_#0K*=OdGuMcoX(=OD4La7+IMGn456u<DG}=M}L&(Yuxy7Izd!DG_%n9#(OD>>=>Klj?%iBi{_4ai|G-W%ywH3h#_Bsxe%(yj+fn08l;9NcS5C!@DvYsgp}8%-^Cqe!MY$`JN+{PMF%*<s9lfG9f;IByV$?`-GqE*Z7r^SH!c4i@+wlVmAGGnhO#y(G@EOwbC5nqR_uO3u30nvRMT++akHnF8}~1?`T;*~CA(sN)xkFjE{5m4WmMLUs;SSfU+I5vnn_Ejc&S6q{v8%f&7nNr(w!l;%1RV9`6YU02o4K83(%T6YIerA4<_-lWE9c)g;?&@o(n3ah+yAcC)lq!<j!B5tz!FVx^<!;X@{nSnMoC_-`KV}0dyBZnicJEElATOTUhCvwHWfO%R&lUPwS}7N`ECaV1Ia`zp`T2n{2_&Wt>R-o%$QCbJ7Ob`cP}xm2+X~#PHx-TmJsOp&om>KE1P4SGVRzM2-VHv6-Z+c*9ytY?@jCcN+ooOtw*XtPc|U+IKB`jcC-7cF0)LS+5SrWN>fec0Calmi8>y^6lHE0+F3UOSrKPa)h12kmS71l21K;3bxfUttt)ljh&Io{J;m$+K~M@l{K)_ZRsj`2yV+Fz<}2?$q&vtaGXh*#l%Unxun@|8unZ_zbs>)B&N1a(*rF^LQ~!mo`B)od1za~fsWkHZ_Rf?e)FxRN05>#9`$RE3OSdUWFCWF-&CN&%t0DkLLHHFdfJlv&^WWb@@PIRSZ3((3Ey=lOLELH9U@HNlWw=_(nAcU0M#_U0Q!|L3|6U|?pyUw{HEzz_5KWvvDHyF=o)FOTamU#;v`B>->Xi%Efyks;Sra19ob4ONd+|Rr94{5HA31`PhkR{9aw;^xGbvf7@3RYtvZB5Hw1CP>ZgtMByYI(H7;Gql3^5+i+s2<qEY*+_cQNE{v~HTubw;TANdBUULzxZWQ?z4cy;iAwhXijW$^GNsuz1Ccw&CNZ{X-8+MJ(y(pxqTl>RJxrx0&^T@Jc>gbfj=8$+(z#il?<8k^@F&7D(`<H*^Sn|gx0BKdO!+=C>YsLeQuU)D}cg4~&!jeqo&*EO%nT=&<RT=AUA)tdl9lY%yaCk&Pl<E#X+G<MA=tx(b37+aJtL8(Qo7dmbx@f{fWis?-Uqtftp9mTov6eu;ONhg94*6jhbxs%ra6h`n{Ab|<di%p1NJ5V5#n2_5$hU4{r+ogQI=3!msb&`ig64vkk_DG!_<zC;#>%@5NXHw^~IE1wB<?{mfZCR)n_!jKWI()lh>^j7SVT%<2F=ai}KJ=LT^>XnVq=nXoy8wShUXP!+f7>p{=RVxJ>C5NSq!u3JBf)pwMcvcKN9ueyf8PUcRHu%tM`%3_AXB-uO&l=^Bfaq!d+QWTcLx0b`r^985M+b>^a!bqLo<xWzOzOCE>ul&hM2)GJ6wT=DI=h4K=*E2GarW2zT=(VbBm-DuZK0`Tzki++_7Vx;<6(%jUZ@h!WuKw{c+?*SyxmlAZ9}vLXjgJ;R=YYmZ|RE+nfe~{vUr;Dq1h<FCg_B9w`3v;A;$;@4QqBP0sg#3-yMv?BNmL22ja+;7m`V^*rD#kkvl$-}=T|MDv^W*UWF9YxvPw_%J?F8sgEJ49PFh^nh5l^uVR%3VJhMZ9ZY1LpWeeX_}G%d7~%lXheWUL~P1CRN*8=Emu@ThY?jcA5`kVk_#`y8$4vAK{u5>q`Gu7{TsberlP5NAv7xzD`zVU3=4wo*gZxg68Bqg!7xHTW4Od7&LxUTGz_N_@g@i!h>vTZwff;3<qoLLllO~H&WAM^B;x>-0_;PB9Zk6-(^~1BVd?euS*FMqto`Gsi8b(W?F5`9$*b>W$8XYcO+ikQ((^tqGT77_X7r$n7I-QVW(7kGUYXFwnO$ZSJH8CZJk&w|PhxFJ{P`j1AbCP(y4<ZCZ_%Kv3ro6x@Ly8@c=H&_1Lpg&p32Ej0AR%ZfpkmuS|1c`K7da9=;GnQNw=-er@Bp@9xRHU9`NrQAc@nSza!ee$6<DO8Bl$@8qq%(Z}oKV1s0bI$)gA#4+^d0bniyq46P+UI*GRC@3|F@|N4h4q8{qGXNzc!1~!C4k(z#=IdDe+xx~4gl8UL=cI#$7liS0~OQ~+$EJAw#A#zzzncPk*d6rJADVsZLwM@)HrcI~^RLP)j&UZCS+JOkzt3i5$B}+?bme%Xh*RAbX-+Q~>s38ay1`Mux{GJs-;Aplc!WdYc+5Fw*io$pRJ*c;@xvmGVLOM#2gMZ7$gvycjudeis7w8OBtc17Jec>(q09f#=&mi&hJ7lflt=A8(D}O;O@-`4;nzi&>`g)O&yk(L+?)bT#vGJxh!ZLA}19^{Wdv=B-t+x!&hgoWSVp*}?y=}x@dMmgvtvBs9&aIQVSR^GWzIewZ?XCLvnRgh)Yq?5l?c#N&4^#<fe&18THHn;-Z}l=>=RMyj&gWadh)ijt9l6y6dLVbaAcdFcPUe;{8CD8vOVnH6c4B_1(XGZ5{)+eFWvoi}#U)uCb7`})vM;Oi(e<>eDl)rg;rrMvZt(FHpsUOd;@b37)PPK^4N%v0E&Y2RGG^~x&g~p|={{`Csub|@u+8`dRb7r;4O?7**N)uqWZ2eGHas(OeXEDOYuKh|hHZRq*fKF$#w^cYcOEmKj@${~r6jBNy?($34%oW{R|^dv8?EZ35ReKY=EZ1b)u=<1>jj48P~|smHJP`7Ud22b=pktvckddr6!)EnZQbT>I$O1SR(M_mYppkZb3Sq<jhouYEp_C6q4IsY_Yx+2?clBdK5(>hXuKUYUY;4h*-`z_jG{6{PtHa$!!^8~ea{`aQ|W9J<EovH<%ag}StAIhdH(E(-cnkHgL-;yP+zRYj4&^jW7Hp&>3SR2xeZl~>#P?%B?34T4tzSU%ad`vna8z9cczpk_19L5Ooi~52l(DJ9GQ!tH4VVahH>HER%cwO%`(`DNM+|Jb;}z4HdsEy{-`ks`k)DomHMp}#PJY!vVPQLvAAbga%Hf$4g}vDM!#CA>owfJFWmrRU=y^1FG9A#@#?kqWBJzVk$-ZX^W}#tHHIS6cQOi7&w<m0g~iluoa(0;tCE4adr!-<6E+=VC_&6gK8(Ik@N1bmL}6(J!Let3Fd1>k8!IWX7Yz7)YR`k1)Wh(E9|!y-vR_65^{~LG79yyO-E`0!K|`V@j2q!CfpC?&me|&LR_JQ>;5gyjx)h)t=1~Yj<jtB#Dvmr(#MV7U20DN_iOi;Al2}PNs{)uxuk|$Qm;mSEi<3OwaVXU*!{>1vL^zy4^)2C_el3a;ie%>~$~l+KDfccdX_PuC#EnZD<zOUtlRM?=;H9`yM<-hdYSHUwCs@K@LY>LvM$t+s!cP<4JIn8SE=Fpm5D8^&X$_c;1W=&*Np7DlH4N*10oP8car3(XlrEscLf~^IuWi3KRH5aRhGz6)D7Kbh1Io1a#L~nI^FyKcjsF*jlb+9Q4Psm!b7?t-EBf1hmIn_!x7e&B+PnPHHuUY3>?93cZ5mz6X`FqWT9?aTP2}7pzSZ&3MKgVG-z1A>fTdqadAFidicKtCCuWyw{*LyI7Wa<1zpWcIZ~CjNXH?6$fGzzZf!<!$nz|v*#)n~zl1(cq_(gl%K9?sDWjvq@-nz2qGU>suu%_-pVLr6dh9v9fB8Mb^X7%`WOMi7T@mvx80`ut`R@TSIf8YH!x^~?!y6H2q-+Vk_S|7CvZ&AOEk4X0)n;a<mqLBrF#K1rKeUi76lez>-1$Ta=#>#0TM%)>Xq;OTju1`&}n@CNrBekwPgq`RHi7C7<;USUkCn28$8kqZL$b{nJF}&fs22K%_y-(O`zf3ZNH?U<$Cdpz3;4m3?qcc!XFqa6t9!0kfFMedFv^#hqh?Dciw&Bav$*6~|pT&wMDrNe_dMO5?>WY~=LLY<|#MIhQ!})=qEd$@YPdJ%fcT}Xi&f=d5DouxOk>PnZt|V$9uCpU7uXBR5O6u1UWqnzBzlicZ68v>g>1~DttGyACwz&)~EoI``&F~XLAX7_zE3x_4g_-Zj`ptGE7`urX_ryr^6{!?m-9VIrNLszSV+%7k?Ui$ksRZ95HC=-yr!`OGx8AVt>yT3<tF($b=M<|DcsW;qpN%@t$^tSc<|Nn?qRGs2L*eW*_{Rz(OwhkT+2^J@aPxKLTZFhx|3mMZj3sVZYW`CC<>L8I4?pbTr|bDmKm2rsKV9KZSNPMz*F5}mDXu&WU(dtv0dLRm^Vj^1oc33J_$@^dp9bo;cy067_gVSVwSCXGrxzc-*L(j#zP91)Vent+VfdOJ=2t%qjSDhAT%VO5&VTjq@$l?-|Ek}w*dx5-U%H?_`{dQXKL2mH{;$<p<Lq`!YN4JV<=fXD&cAf_=|Um2U!F+X2Y<$oQQww+bFD}lRhMR+Um!aZ;qxYN*y`0%-Gg0E@MG|0vZ{L*ghiY2(>gt=#8aKkh^;Z0aTtDPPh~>-?8kKW{rX*(&jeE=*3WEozkb2XM_4~>mdq+RU%qkuj5$@GAHga*^SfeuSNldP8qEx_>j&pWTh5_j&<)Mm3n93`)BW<A<&DcT*S-!qwa;DHcB=Nw%l9I@e9rnH>n2>D<oPpa=X`!BBiQLuhqFuP^KxSImG|$w<Leh(o_1_~4b<mMsL>n#LO(iS5<ZorKlPF4UqmgN?acK1*}s8*rDDqbkpG$$gdJq{*X8;2^j-F^=}JBG*O%U<dH3W`vT;ap#R7ctUGTEa^*=2aAv}9l@BHfroc8j9aP<Y@?3wdZec@ZY^H1|H`U$JwlQ9VAXDENZ9y76B=VUJf&3g4-Q*~b*(9H7q`{f0H;cTzpN8%^EUAGVW`tSRv`7|!hc0S4FS_Kobzx?`bkUaOK^Jl-$SM1C&Ib5~^FZ+XM<@5jd^^(Lmqy8Eep!u!WbCJxFt&w;o3H$11cXr#8+L)vhn#d5_g##^9{Jg~4LBg=~X7OiPm0N!!QFp}~nJ?NZ#8pL~W$PWlsl`slpa&}sEg88yPH95D_AeFlBvtHJ2m%Wk(){A}?`;7#b(rOixk(~XcX@enym)UqzXE4}vez%mx4sAk>DlZFlATI3-*^TW#0F1aV+~~79TsC&lM+b=VUJ;@T)gV8Ti-jG)RVYY5|vOBpPl`-s;w@#+>FRU^=5)KpVfSZ!W8g+nVnRmN^G*DSsULIrAVr4|4+P@T=Me_^0XB{u+jbC58e$YFRlMV>d8Ht-1y~4mdW%0PqcaiZ|@Kw3OU~KjrGZ$Ugkr8hbwVkzsa4vsKk{;Up1dV#nJ1-JsaR0h{HYojl^+%AVK#Lzi-utXLj`EAJ&&k@BDI~ySNv9+}FdPZF_=%;DEswr+b<$JK3_4dwFQh{vgDB%=gk0G};XM{tswflBDLRTl?zJj&9#ROT_f37CYXx1MS!NbeyWdYNA!kQ#$DF^QVK+V2*QST?0{to4xm?SsLYg^4&Z>kuB~J?);&B5w2NwweaF2KLtaVNBa#daelSL{Tz|XsjY8@T}soC@{wy@mt=@^N`BlYT?t?SzHkGzwDW{JIwpTeFvd<3(f;-L$420$gBbz;4GifBGBu0@AYbe*n`-8v;2@y=aWMqksaO&z=h19Bjf5&ETcY7VNKhMwpx#L3G~pKZ6z)lbT)~>RpI+t+35gL8D=)YACUB7o#}(E6&{-$JeecbA$M~PAF*S-eb~QelxPfBIG!bI8F>NXOB8I1emw&Ae<>?on9mktGj%o4c&7#t$8@l}*sBFG-L-r5%R68^U9N=UR+Y2N^cpIsJL+zx`n@IaqpJ&S$KJy1~c!bOc05<r#0OTH&IbafS-_kUNsgo@{=fl{btPr5UlRM45u!d!Wv2|O&y^yLsQrvx^jM9*fy<}ktR0(i~KN4OVX~GTEqYeeNAD6fOGyvDPBN07Q*8KA~Zo2nBav-{K-SD#x>F{cd$q6Xrx%pr3;`4a>s2m#P({hPau7ht4CrSRvP4JYlEEr5!i}Ldvk?hA|fsh;lA@Rqj5EA3DT?5+_Lk6<+WDK(zJn{r@&m|>$YQYF^Pu)Do6o9iec`iq<#NHbiByc_9n%QBce<d{8&N*W;OG~4k^M)+I{RLoz?h7helm#$?GYrXq_h(pSeFWtWK+No34Y_afob_@X3*=BIAwjU4UDG>)&)gaY0+A0enxK9#Lyf;#49MF*=l=6m9Q#1c2`-ZHDLM0pV6t|zp*^Lph-JabTvzGN1^W-v;)4AKZi(X~Rcg7EO+5HSS6)9**Qjm>BSk&{Vy<@{Oz&_CrX|aOa3aJKFyE|oG%E8ZVKQvDzHEY|zmgn6>DvW5WN*Ym>2OSB-Fb2s67&^W)c`li@4=&s6l9Ga2r6QRM%vio8Ek5aHA?7Sp+JymF@)dcXCcNl_|XuOOXA#UPo@}Blki{}r}HNAQs4d~Rb`TSsL`DeC79%AS2b2%3NX-h53c71KZ+e7Yj>iy|E>$S$OGLXb90N-LLgD$o^Fw+<`&sEx5%!!MSdCl&#v4er}uP=?0T0Dpm)Gy%==%WVPrZtjQkzAeNkl;xkdi4xkaWX88iDtenBgMU&2C+zfxMz|4<H*0Y-TqcB;5+T`=%yZVr)tafoC{Iom^aUSDl?h)m`XNvZ9^QYH>bu8TK`*ci0XV9CI6tKSHtlE&4GNu-d|R~#birn$S~5J^h0Gn2^Fc)odM5}BGw<X#L*`b1&~TX4@x23;V4Fb`6CW{xK>h{il7MiB`ppr*mBA~Qvr`jF~MU5~tf;u9HP_K8fADaURslgK{1&##z7;`-dY(kIee;B(;?*<HFtB1kxVcdR0d1r=`?j(q(=MI-TD3o4+qcSe7D8dsc?_>$s^=Sh6$p~ZE+(>vk{%4xGwJ-r-M6xOsYqG0Xoy?A_2V+l4XC|oN-->cYsa};FkrWiKe8hMJifxZKP%GL`(dX<wL#LRBW3)J+SbxQegZ3pSSh^NJfr@MY3p7zfXPbD%5__<0RbAS=WY8)A0G*72*32NH^%g80`<o|g_<e%{Z{0>Zr$GZ2##F2#rre?ax_?XG-chHk=aO-MvTqZL9X&_ZYzdDEN7Bf-WQ%YBLVZEta<I&*Vb+6w|pt09gcw!xCe6-O)J09%E^?GzrR7YC;J$<?ln*oa{Fx-g9IM8+mBi;}G0Odh><l^9zy~7yXbhM<XnNJDZ%q+j&yp7jBPLc93K-3Dud4kM9*eS!UH;?kg#VKj^1^P%+q4vR}%L-Tyqz_p*#&x77IG?4v#{{tSkrk$T0-yOuK>DE+!SL0OK5ocZ<SOg#teS|3Bj3V3^-By6{}XA{!`DoeGWoOkA5u&w9cT^IK|}!qE2~l%M<2d7G|NT~N66t0*lzWuYXEaYd0UK02I$cFfc0jbIUs-4SNu>`wDlu5G9DEVq?Kjs>yO@CzeQ8v!RrnEvIZDUf*gzIV@!|k4JL5hqGn@sT=m<&V2~wUyI1n86|lS~TeXhY!T1E%QopuDAHy{o0VB9fc`wM_K&gRN5bxqye-%n97iuhqhrw3qbh%157c2PSVcM+O*8S`00xUhvE8YmjhJ|x2?#gS30!2m&AfrO|g8R!QOW^3t!pP4=0f;(aVh>j{K3U0-dKzC(0&rBR&=9+QUMPIUIL%|YF?~lrd{mL!IvqbibzmK^FzI?ZU|}j_b-A<IFr4#hp3H{GXoW&h;4jzNup3?sSUNwB?+94Ry8{+~Nbq1EY1wdXD$IHV*heG-nZmVb1@(z{GG~z7p+cN&>qZHLw4C^=*}$oAK$Z25ady6(2hb(%R(cuy6P-^v4-kWxD!_^l!)T=|?>i4HS{W=E$2YnZduAo(Lhre-O1$})Qz525<^CeYhJFEQW|ma53dWE1d$T59H<uB*JA<-`2bDkk<2{#qm&_c?r7vl-Q}0L}yl<HA$WJJr$d;4d99jNqYMumMDY1^6i4mj{SO_QIQ3SX_Mq2(D(}@iLTH8!2@z?0)j-R4C%*CZXJTkk4n}mnm-+?Ntg?SV9=$?q7rYcQviH=r38hhBr;}`M#lu6z51*Lt#2D@SSTR;71P@6~wWJYZ2Qw@T8er{{O<yPIPIc+@$W`+3lyZZbszO2lf!=HRVb)@?5XV)a=Zm~@a`~*nMZ4mxmO3WR}gP(PgdOvQ@YN{`(Bcc9PLsZnfWyDGGeyfybSq6D)Y6(Rp1F{SCxw?+j?|m2+`5bf?W&t|SYNrHp152H>dfJp_dY5pf3hTMe4bn>-5y%yCw#T|ek}laZ8a_c2w@EB9mON-GPG$g$!_!9-!|mS%E4HpGzmu%k-uDMmVq@dOy3{pFY-iuKHLQqt*qq=InH0wHK4YX(UJGOE6n18(!}}wrxDNF$B-M3YI=Cs?V3mM<pjIwSZBsZ*{zl#;OyKG>kR@Pc+6;U|M?HiubjfQl!#Kars`^1cXb)MqGl3cO%}8zya);8pPI&##(nfb`4BV2MLVMk43hT#K!IL~FCi8*kS@VLK3y#r$W2uMra5->r*nh?PKH?w0Y4Lyik&p1Ea01k;caPC8!H2Fxz0jPHwtmAMc-9CA1R!L#NaQ|R#!%;Joh0?WLvfN$o$@>-SeNXvx}&YbBzB^~Rx}R-wtB~qdjyd?J{(LNjK9}yZHG^(k@*RI8C-*oJ<emn82p@93od7bJluF0BtYwHD)lwKpWMWKslM>@CZ4zj^^}9v+rJX|fDP6i)2#kOq8w&jua9y*R1a*`>*4*8LG1PTruZ?RF^07?9iFy(CUtn9k8(;2aaftT7Udwo&h+&`)7LkOFcew2l!fP6!q<y4a;2S%GZy8%F6M7KOI=$4XKgSogU`!@l}o`TTN0Z>7!m<}%3D=wIBDOnJ~K68u*k}S8jMf1!7k&TkL(gO{Q>ufV%o(t#Pl-|Zoz8vd3~tOm<zH_=LdC`SY$KR=N}n-1f#oSq}<s66xQI;;u6Fz!X_vRL6;mti53hUWgvLVmDSgU6w|i8E8PLkndGBF2=he2gcA=wF_uaKO?3P$6ohf)gmN%V((8~su^TCCJ%@A7_x?*KwUQVf6s|F{VaEqAs6P*k^X_8)Gd1k!vd=%Em0btLQ+#Q71!AR`T3f7xVn7-nB{7^-phg#_<DUmtm$(cME`tjZkbxL~*Yq`pk-{uo`hZY?d=20Lz09SNlw;vwphz>2$;0!gvq3f{QzcEE$%r8D;m~KLGUd#Fg;y%Zkr)zHS4zr75=VjXkp{oQ3%qte^F|8Z_y&bM_j*bPEaQ<djqU=^1=(D^MG!4G(oj9$N3(bJa)FnWNugc{0vdyfEyvj;)0*!D{^QJ+3{}ltLT~D}@xQ(RF}?NaS9}e_@$*<Co#>9|A!6Py?gPSL<s(W9)7kdOn+a(hCzgLlDe2;@mRqP5+~+Xyenv$qD2c%Zi~A=x|4v(|hK4GY+#0a`)<rn%qQur>QPfH`@qt<#nIb%O9Phe$jv)aZ=sAgPHfkX7y#({+%#(zSHpbn=VRA&b$|T)p7jyG7fubSCTKzgZ#QQaoW&-3HMR)ZhV!eQ$v)KZ-l}-m?MabLla<w|v@3O&aMlCbe{J6rKR$`{c876n+MiU-arzF&l*?86fgqM035sAzon?l)j<gSBbS2Nrn<@ADSKRveg&c7+`*y$%Mp4Jtex+_tVu~GV2`o+cXrTYg+l|w$Z#>HQ_Zb#3%&cB(0>Wua3PREc15<dV?;G6nw{np>Z_7rcZCVk{w?yVwejpj#Qn?US7JsbH8Zcf~u5J~QDyrI!UDs&k8+0+bBFca#D)#KNhA5~<HFz1dN4b-H59P$PFwKVY{esrDT9ivms=N)C`SP+;<7|6_h>Iu}DK5^Yqy;hLNo}Itl-rrIHtG*UDfBRDsODT|gzE<=N#8SS+Qr)X#sbsN~p$XqlbcIqtYVXqM3;q4K+z~PjWIrgVnj@+U49$z0tJ3x(sO&nD2FL{yt9oz!N__2b6Q$(G*zpBOO$)75Liw1{)dz_Xe@zobd+gUXS4KZ}?`i~pU9$v|d%mcynp7%zu@U^-<hYy}Hm3N?drJ}T=X4{zI?-r4#DhCicJ&u!R;C+snbo`Z%{bmeinu?May9<r&45qe5qO&adG}xV@pFuz?#7KZ?|#IWKrJ#$S3E|!96Ux^fEzwqEe=3HTj;*$et|<jqU1By$oPT!Q}y{rMCSKI#_kHnMV$zlm7!Bz5ARfyQy`oAhq^w}`Oc;76cP)|+0|nxeu>BW`^fstM!^@cXOBXk#OZ;(g9kYp#Tu2yQ=IO7v|25~qVVYRT_VH^UvO8q!c!ClEd0^;sJ-0zPN8I!vxkRu3Th)PoSn|AF7Sk?^MMP1S?eH(9D?6=^;)e3+Ue|G@8Vun7a3R7)ERa#sy|Lt7fv?}2St3DLf-I>?gCAFh&YP~uv5=baqlF3R^Qy$DJPebEN`Fsc31qF35vP;F!X?R%4`+WEmT!hcc-TwD!y3*d9zVSu#rW{_uu#$t}dhHj;f+K>iQZFjD+hr8#$zkUEmtr4%aSlzYhxj^A59pdSHcq3mYE_rkXzkxCr$s7CgV**j2>O2AbG*ApuEk*D}cI?3v3+IQVdWMI%i$Q4FmQH_u(s<#LYv;*dzLU;GE|KdKu~5u9^i-ddk!+ocdae+<}uP63(!RM_55370ZDj#A7oqVnORBWDLBEi!jMsHe{qWkYsG;U%t{&;d&%;9CzA7-g{=Kt*2tOw>clEUawkbJ*ij63B+D505hF3oZdHhZGH!qL6YJ_8n#0>wS|+N0-bc1#USA7m$wu_8=OQqI$YA(FLpKZ&r#nsE#n4G`qA$aVJwqRbk1@N*JrX5p+lr>MTq3k%p;#=uF<5F0BB;;sPeI5a{X?_Ez~)Kp%eZs|{V;@F+JI?C;1!9<c51m4rTmYO@7qDb~@rBl8AP!;$GnhqlsD#;i3J?9DZ4bMNGb&18VCEqAga4C09dIV(N#-#aQGvOkA-;~wUele$$WSUzR0B|&`WVBIbFzK|3X@2#Gq*cNr1zxtINfa|~8XB>b>hC)}Zsh`^a#ut65YXGu&VoKc;I$<n1a@%D5D_`n?{Q{QGnHF<dmmhCf&=U|5K6Cx8Ba(eMx>FA_yyEcf1pUo6^;s~8G}ffKsxuw$8d43B9|XHC;*i$9z6ph%5Eo<g=Bx<?<QN<MI?DENHll9c=tO`f&nBfDskt;EJ!H0Ui!)y|<~Qbx@TBMaBoc|U-QPzv`2Az=W$+v65L0*OVM{FcKm!(-is2#RygLJ?VES|Pk0<&1l4?by3(F-nhYsjavUECZ!(9<2IGQDd-opEsP{6FSI@U3^qhsCu9xt1q%N-s^eijdv*dQ(g+<;@&q$MyM^(FwuYrL_enK%F_^%=%l^XVlk<r0THxM7cnJ4$HgiKp7prkJ%}!{5Y+D$L05C}IAn_$!th2?4|GH(Xr!KksJV%{xs+rC<F3$`R@~t)&|TvKmmH!WtZ?OpxT+4nQUtRfT|J0=fY!r@}Xx#(~P!1ii~#O%o}awm`fIR>VbffglEtinSF3eY5kWRzb%;pNN!Ry$r4oS~KfTFzB$8(}iJF8I5|)IdCtKwbUWV!{EZg6$TYBJp8P#3tT58)GJ3N)U7dX!l4*~Fd+~M-2o4KksRvA1GhMBXffTgbIEoll^??0o#crk^x#Qs9O>PSUGU)59fk>7U{yUyy8^!iinwpZ2d!uRtFI@K)({K~%ROep7~HXr%)+i=$Kgf9fR?Fx)hD5q5%gp2+xHY|rzOZ?AeXQyx+YpGB+jLzJIq<<pZ*+-lA26C`jYmInR9B=v8&gZ=aGAQK&)Mn98kj05IEI6Q2ix*%AMnqiH<{N-c)Ed0+;k#+mb*bJppB~ljq63P!xc&qBQ@9-s1v$7{dUci5>_q@GZR<gA?`=*~by}=p$1obd8MyO7vSDX-6h@b%kMRH6Kws9$2WyU_Ek~;w3zYr&MFIThe~(+c)MEwi&REOw8)*x1%*D5;JX>HP_oyh}bAHG)Sz2^851(Zq-e~IiI9Uy+dG`7{U$ODAd}%iS*X3AD0Xab87(y-uN%PN32EUaeQ=jjhh&>s6n9RydG7~y!E6Wow%cQPT|xJDnXxOYK4({X&*fx0(w0Lvs!3(@)yQJRNr+VjHobjgM+~l!=>xOfwUfpSpitg6(#I|R@R_QcbwD#<`((E)z2DEVzERoQeItZ?lG$1`G-%#3RYLtx?A|a_#tcXiD;CQbp|{cHJF$r{B&5UoLOjd^-VIG$C^Y9bGApYc#9^*e>+Gt#HdZtM|EQfD#b;@>boOmCrX7tTtg=UeUT&t_ngetcLSgeK7T0m^Cs3l)6^0Tv&hw;uxP_2LR6C|9|Na87x_gle8ECDJ(HOs@UO6)XxSUH7ALM&O{%wz<Db+%(k>`{2PA+<UUPGnE+*|Cl{ExL)Tb22nw{)b*CFdQS+}g%a_iX+A{ps`KW({zoB|D{w<se$=rYP~;IDn9K)cR|-7|sq!AJij(Dnqp1Yk}Ee;#Wy9<f%FV(o;^OIECnG9htA@}qCwvHN;Fq3dYZrQ|Df>nt=81jm|@=*s4lyCB!+G>6-ISTl1tbkZDLoyj_BQ;WDM=g<Xh>IfGYjZw4A1J3VT+^x1*4c-SCc%kmVsHtD#?prNr47%yhV)`1nw0lnVg=jJjZqhm93P$6CGiQsTh1+ys_Owy!X<n<r-VYXT?^faV=1MV~0K$(RZvXeoI;?`v=T_}`6q})QpcwYpJmKi##9(qY`5wL?Nj`JMiSD#dXjx!4aB@~CySmFc<<`?A)Eo;t-b^ks{nj(d_OK)7WKCR*<`!xVGDoq{f<f*RBReEoz4=N6Lf@OsL@;){3M39Vg^`=28XdsN1hdnumw(p?6UE!>1#v^HMiY>Fw3<QH)nue+g4R>1v23HsANU~iWd?5u?O0)^{DB1i*}20~AM8nd{7C19K=y-IW`UY62EItgZy5Y{s^9QKdrr8qL-{a~HHlQy2r4vFZ5Qw}qS@3LPb^22C<|CtR#<v0<OEAWPLKg!A6*&mo3;Wk&J(4bfA7^W6|P@s_}5KUxReEXn1n_+@?A`ULQ>~BmRn1fGI>)+i8kC}?=Y+_o~(O*9FGykJ|-_`3S{LrayK9fQBSgCFL>#6D|KfcoZI+#D`<3-JdWI_2X>jM^TEP6q7OP|J7ru#$4d30CU3~tYjRT$9+HGT06GXq@x@WEK(_f{563&+E2r>;-=bqus)+PfXRE|D=D)ONgvSRr#6{VtVK&Zq;TXt2Kv^tHe5n_yT6w}sm(A>H7R59_U;@_>FLUt{)$tD7gUXTtE(yUz)+8dux*#q?*K`acG4M6s`mBVSFH7o!-Nw3f$7Cio*hmzq9*dhG8A3G{!841oYgr{pQvE=V&(B6GHSka9iF;L?>zCDu)i1I$FFf*(0+BTR%KHa$ASOm)V~I6QoKvz~6qQd!cwml4nx%8pFvMeCXR3=NG%_30wo-p#0=Z+_6jSph+EHPMla1Xs>MBwslA9Vr>cTQ#_}{+OFo9I-dY?CB@SlYVtR<d>2|3ES9AN@2AuUW`2&XV%=)3?#C~;^Gufv2c$mB$~ZyhP*r;&mn9mZ_ZyHuDvj}#JZMxfypRZpPk6QWBw<#bK*w^wbho<&EpT{MfXr94No^*R-EY+-^pZc&kffogJemxVb_anKhztK+&h=fJC}Pu#4iqtN9u>L?Ue-f39sKX$O-|L@nTt5NUNo7q~lg=xU`LCZn;VM=u!$(`7bsM2RScng_M1wbjPQKrERb<|c({N2D%+~?(bY~paCd1TS@7S7__iqHd<5&`e(#KR8at~2w~@tKP=d10XG<LYQ_`KWhn!|tl*r-#|L3!R2oVw0g#dQ~sfhHDKXX~scJnTo{IQZv+wD`PQqsK~1ik`Cie5!{&>7vuz@>eX2rKqm|cH@0GH4TaHyyo3?jj^+uKf@{)b(c}-QubE9P1k0i?h6N1m!iLh$S^nq#$;tQBIl!{9Zl}%lnRr7aiYFANV>`!0?V2AQSH`BW2k;BOLg$(T9hzRIlpB{XxcUgQI~z?6FP{FHGu+us+D%ejK<f>lGd9x8ZF;EN)2;D(xICv#edR4%+=~1jq%Dh6e!OMknBx5rSNBUs4UhK>CF_&77$$cq4ktIIcsMYBsV_)zdyA#EG?mOlUArILjR&Ue9=kxQ>Dcrb9}bQ&g>ZYRZc-BjPvRHH#3rMo4|<ro`2C4Idmatto&V;;stJf=ukRXGyuq%a7#Nu)>4M47ECQ<GWTTaWvRXJnE@N&uicKd4R}#O2)r~MOSXQrbZ;7+^5gum3MGE&0AZsohScB{5CJn3j(v*pEP{X}xHml9}dP`o)fVG?j%sl`wVycf^=#yNkObL=e5he@#AkM=&zDL?x23N?S!bcx)hzncOcs=v`s5#$HjBNc&&yNc((HI(YKykV<F7nN4P$-lbI4A_0>{LB;R0?wDQR$X8UueT5T?~`@_8s3C5H*|+6PDSMj3{Lrh`W?*)ELrwT_5&s-DuSzD|3NS6kS*;TlZ}pi?-Ym1Kn)c`tyjxOT21c`Auxn)JbKY*)sr2%>BBR-DNYY4B^aNapi)@&z(3<3%e!0C7mrnSlk!mN)>gr6iWcX{-qj{ve4Ky{i?9?fee?rs`B;>bd0ljzCV*+4H7ZxW-rHfenf!LYOb&Gj;@1|t>RNj*LhPbcIF*laD0KFs{O;fiGwNBu53B&;9<55p2cPBwBwwst1Y!>WJ>q#1yH~5{Teb4&Q{xrs6MG)J`iW1mchLf@N!T||G`#LbTdeO24{}`xg>MYHJbayh7Cu5a$1YGJd}B(swG+guj@#dML*=unJlJ+>5nydWn*VV|3cue35zis6Zfj5<0BAC53Z)3`Nl<WY+RhpzgpATj+j=2lCg=8u&0nSw&x=^Y0v~b;z*Qq9u0@D8dN?aPbnRjEs%CyLE{Sl3gHEjMRxiJYy6`io>b;W@`6|PNvkj=FQc4|vHBn*&Ot#^8Ysc68V+iKq1!vDVWx>}M*1kk9^JP{#hIQ(P@h!k_Nbl(;@72>wRgE^{Mus|jOal*tBDlm%2cb&^p3<cJ)Xp99wZ&h2vSeh750DmHj>3Y3N+Ie`BhEXM^?X95Dq1a83DE}?5Zgj5{SALiX%A+yh4sBQgG<9rVJ%Iw4kv5#x;Zkt4a!PCY-MGMM%ssxeANG<tka^647}Tl%=DObP!jTlFceBvw5OL7!?34Yu#B*`Hs8HSwXo+LHS@raVq)(1QMgV1{4CIymMVQnH1i*WPpvPhXVeJ1DNj#W@B^Vklq1v*SlG@qNx>bzr|4EuYaYXH*p%gzD^<BPy{7nAeo25fxC@=5jwPPXROdeHuT6xI~#XG58*rrAZp{ToQ*qNW*c!%2<ad-VGK9kQuQoWMT*wTV6{RM82}=A)MC(yUB#lU%H<vF<Ng9hR3{v&z=L6$(S9EiYffrpz&^#@U;&!ZLzGbzZm2Ze5MrUoT8cF?Sbqi7+b6b(`yfF)12MBce!J|$;lw7Gw*hFV1sjG_YjAvf8!VO(|9jt^?FAw$>p32wfUtR_L>~)tNW30qnGB?QS$Q7R65{DLyy2Yx{1LOUKJ(`2X1SgNpUHc)<pW>LQhd$W>di-D_qc}=Rt6jxubg1~j3UUJTTm2Hr@ZAz#|4gGwCueue8=`=o&Wyebe`DcPZ-aiA5i<QPwsdAx%!N1N9z)eO1FbbG-=v0=Eu}R{W52Ta}hA`O|+1*?SV2^S18bYj<pho*vc}=JUiUlfqaQ|dGNWaBg1PlFgfv5zyVF6#cie)WCw``ws8vePu`q{?O(N$7`IF8nwTd;@>=aeX&kR^@#b-Wi4oeV28(hLaz*omH)r_bv`(l@EUA11{2@LDo#AYg!dhgE(-QpKOi%{w=PFIm77)x-MSs=(uj@i^EAjcY{k!<9R-THihgdTp#H~jq3K6v+_^RYsJx8uJ6i}#pQEX+RRxDcoyRy4CsJWk$rb()nt-I}1l8UWX*8JyZr+``U-o*Udzrh6jt$O1~{90FacwswpsJA>&OW2Y`taB^UJ)3Wj!8I*4^Ks|n-Cy|Rvi!+q`IAHKr-z@e@TV*M=?Z_cSpH<O{K;bZAFhYtlfUw}bYVZ4D}ORq{*IX|&!)&RzmLDNzxHHmzjWV>zp}qHRMub5Xxm}+@QJPR89m5kclU0o&@`+Hg@{;gC9a1e=<JkctByd&qtyzd2w_DELUaHW&7#@swn~X)TFvivSS)glY#9C8$JccY75mJOVNvU7fg--w9XvBXe&UY&?4d5acvtSoa-p1Gqd%Q}%C(b^hH_e+YC1O|4lB!KHH=Z@FK*>7eC9NKVU~RM)q-(Ex=Tml3#VlJy*&B)PfVT9+>y~}N-z5&U!1C6hSPF|&rOlT6_f0jT(mLcVwv5Y`7oHzl0K0i=hAGAO!*>JOD~KyU+_q_XPQxKTzRstO_A5XKX36HUN8oJ*)#acpYn_D$l-aLVSoODtJcUbo8!LdZTul$FucnY`58y#E1$SJ)wA2=U;Wo|#ZGu0443Z6XU~K)Pv4cHua9R3@lOu&)DC%pX1sX*S51-Gq4^Md<Fjj$-sg?a45V}SXo+A5B6Mjo?Vs3AKfOfjihDz4Jas{y|7ENBtP%Dvz7}TkobKXnBaX+W+0r+O#Sxk<C6m8C_%xvYk1oFCl9Mz@z*gQxJXwyWmxy+&i_;A{rS>N%CQ%VFn;arg8+t)-2Or0qu*+zEnU6#E<;LAGeCWC9g$JA!7&m)giaX|}L%2ov@_uyF4qdjkY!lj1kMsMM4&eh71=GnFIk==WrRLz`NFnj*;ju|10i#Lf%m??SBuo?Vm6=VVV{-X6d<hkhNFAR*MG&YPCHA(5E*wePFJeR2Uxcai{NA39n78qUAtM;!6ayNK6P>2Vcp#l%cR&+vq+mo3+q^i!Mkf>!SOA1Oz#~lvnC`*dKxJBz+7#n4Lut;aKLI_}z0W_(uHDJy(U&_mO6{j!GLUS%I{1AZD6;yA)Xj|4!I3NnQT|Y-rgBARDhGzuBC&#!1tebgCa(eDkZ|_YWeg*(<<$5(<$;Y)Ua(9*LuxB=<UQg5a5X)!GtPi5(yRbTq)e^X61pDt6sdJ~rwN#`PD4k5P4qX^{~yWe0c?4Q(rYD0#ddJ1yb?~phx<mKNg@n!bO!Ld0}ReMF}6IKn!~1OPA46HN(#pN+Te1z4rp^?ME(=pkjdxoGXgEt{wV-50W?9O%#9}U24CG5(<p$F7nOKoq0kP&G~J`^Cq;w~fU{`q0)_%b-u)sYljV%VKn4HqOcS-E8drHV!|x;lEfsJ99NR?U5xORxP|P&Z2An4{!Y8_{&zFi~2fLp4Em5@<fILWvmx61S=!DQIVWMCHE%?x?tTVsf+lk^i^|BS$ycp}n-Z@dN>slkW;HGKT)(Mf|H;aE~A=~<W1pWebrMQww0O}*v3VaW#*a){wDmiTBNJ!?BxMAUc{6Ni&;Tqm$^0B)F)5aNOO*OY&XJD6M&B%EQvfh&rOVJ9!>OmPy4P;%c5nKpJ>(I&;cbi&(w4UpDfeJC409-%S|C`1CE@9U;1PHCB+j5{f?8-J_XySjxubDUX?m_#YEGTS-gWz`Y_Qn~GEr6C4K6<|(vZZJk$ynD5BKh5Q)wo;f^KIg5^>Drm1l{<jZIsm${>fE%Rl`>G?*MDFcMqT>H6I#|55tP86nf<uh)=?Ct0X5aJ{$v0qSiRRVQQrePX)9n*Ynx;+sYuJ88A~-O+LPmAgd>~>xn%j=B}H}WqC_5btKoarn{-bG>k@JHKjQ+4*=6NQ8w>3BNo9S`RJZXypfyF$ZwFLOPO`tFmF0<@XD3Mo104$xg9V_5`dz4$6x>2?h<*#k$WuG=O?hsFFf!?)c&!Za}B$Ue2Xv|Q63S|^#v0X2C%Rnk76Gpi`>MK8+aswH&E^bPz-2^x}B#CCSj|9*Rs;k$@#iP640yaLzwS|oYDIzc|D#R_qWmOir0k<J`(eN;AdHMw~^;MkT4SENLOzH!6sOTWx*a}Cf>2W@>rkwwU2ZkRyQF(xdR)!{9&FgT_}1@Xh!xaVhz_MAw8i;lq2{9FB8`7dhm(&qyz9eDSqOz90$$~@`Z_RZZjlZ-jH6~K5s=z*X9O?32oD)l?W5xv~l6Q+-CDU8IK^&_n{7<U;R37!n1dPDirHGkXDy}qYH0WT~a0E6s0o46Mz1yXFr8D4Yv3~J+5~Y7+#a7r_ED`(a)ufm$~C*PV>0m*r1OWSDHr#Rc`})zOL~VP07_jhXh3%<+zyt!FTHdw;cdML;cgBON-Ho<>hQNn@&NZ++K|~>WS6iRri#g78!c2^=21K3@pbw1ao@ayeT#q-w5Qa)`y<YlnovZSI0CWH#bBodCZHwIn_L~&djxB+<|a|@r~nmKX$(#9-xUP6i+=s=M0kOSunnI>GWWBd6q%mHQOc1_anM}Kso~_y$4q#?H@hT9@NGC$>OQ{O>ZIM;5QGZ5m{eZpZ}~L<TI!<)uV0hbt9E`)<cnD$q$+ibnReV`@6vbfyJZbd-Fpbr{L*Brs+ig7-A1kgy|_~sk8qx3b0IkSYy?`N!x{g?zN?cda5@J;SMM!VBl?lm52Z99x?GiQcKy<l8|w5J*mTk8Fbf&J0j&LC^-2yH^_w^MFzgp{gQPX$$bxShfRRXr+fp^4oY4*eqHl|33no-As#tNODaKMEXwxn&WQ;^t$x%m$_UJ7k-)^g$ypz$(KY=on~omhQ3zeXMheErpe?M>@N%RJ%S^2sMC!O_a#g>?#J4n|&geR%qGby5Vt2y;(0RFt<fO<`q9j}VIXM0xQii<i7H~YG`p#TH5y?|BB2b_Zvx_26X3HohT~O}8L8%-83th*;84F28PPa|2vxTSpH_l2ubkrj#e?{xWAin1U?GKC0rgXwOX1YSgGEqi)Zw&sP3V(WIglOYRU=y*8u{=%n{sk)`E9n&X@ePIiKl|D#`a>oH%HbZUJWR#84R!_8(FEfKcg)j<ri46((O}3i`*V7F`vC{7*tgHD+a7MiBYz+3)w);v15#^I`Ysd}J~AV$v+ny8y?rC4mRpFe;ZF}>aO8VP`9QMa#F0q4N6qyfp)teI5W+Aq{qa{_fE(~jl#~KPe}r+#AZ?cp0@oe(G9bC(zE@n`Eg`d?T$kx2NCm&1WxjfDm`l{a>{ZaJF9TH$S#;kZ@;HISA=qJqtC0j;*Lc`WA;*q0y=1(l@39+pR2(bj#sZm`U4mVggdaN=e|mh1<BJiW^|S`=xmx#73cx;IPeTqxeLcfK+rRo^P|qS>$vQ$QI3SK(7rGeh0O{~XoIuU1dMd&6h0lOr!sF0nCFh`%ub*<DM^F!U>v&%W&0l@3g2X1}@A-H@P1rP3DEXz@d|fS}lSKS~{j827CN{zZi-}^bG;KsKhAI=)3p4d@4zmV&214B(>Of%ygU8U_7@;6Q7@bRyOfqH=d)J9#2o4yve<gtpSIumNj^&ui>H6Up(K79T)D)Bkf(h1%Bfy$T67EWBOwfzBKA$4d(748dvX8#`6?o>%$v2&q*c9^;32V``QB$*#MCT?O%Rnu6npw&Wk^iSZQF~8d{zxmvK&_9CUyz@btU(^mIR%Ll7P0lwlL>k8i?^4FPvNbC6wQ}s<}65*s~yl<%|@3F`gg7QnylhP!Bn>D?c;Fp{U5VUyI#^?cv`)iOLwbX`nl4bN=*ky{+`uU=AueAU7NEF`Pdx9<?U2AG1cuzcBnD-DB2q063Xb))k+-qPBu|crVNr@Xhlx!SM|H*iM6_jl=RSHW1Lj}M@OLTv;(ca;r7Q12fGHZY`nhr?%>BB4W@%WOT2mPRy9balx;oAv98CIC$(77Qka~~UHd?7-1-qWJ<4ma_xM|%SQnpI7oYIdpB{d?!k@12rz`x4b@Aa3!zaqcC(6Yq%Ec$j#V5+eC(6Z78Req?hm&$~n8_BB(lx$C65oPOUGhbg@fD81>OZeokp9FtmwUQsMtz2|pK&T)-ZPzn@lDG+F4TcFn_=cL*z4C+j6oRQE6j<IjT;g2@&XiEydb8_D;whb{hl#szfm#VnoO{~tLF(6x2A5)U+RoxAW-u;QNuu}S7`?`p+UzNia>JRCu4X78dLlBd_!`b(Ie)Efd(i~zk;+tFK7^UDcafk*@kQW3Nx=FtuLCBS?m0jb?fczshtvS99Y|R$>htQ=Ww*I=Fh1iP3y!huUXx-Gq%UD{=W7~{{rEoEJwR!dw8RFEQAk#PWa%>S`j|nn)c!6gPb!zuG2ok3UPmx`LSXu%)E^iP2s~SApUt4$cMaf0n}e15WJfr@Z!h4z~uNU?_F_*p3-7uY48#e<SN<a-7hHDFVvdM5uT70eB(VhKeIr>Q;Nft_lC=7{8e^Hc-J?2ncwq4Z@hl3uF*t3_{8R~@51W3bx-&r%T;Bg;{3$smxa~&v|rBDW}DoSH<!8~zn!PVk-z-4D@j_j?*-d|tL{WkZ3mzmxpE#D8)#u=JFusvP)W{I<exYXOmH4p<osycV2Z)uDl|XPT$&STB(`}4SJ*eac~8_=qBk@4w}x9_r~*9A0$phTUcwcU9~ed5n@dd0J6{HO*TDF2N~c#+eM6$VY#?7E9<WIs10?9=JQTLF+dG3a_w}!X>$|X5XT6yFUfHs#8)*^u-+p^O6LMm?kPhvnss2PdwBB%l@)zmQJOHsJBe%75Xp(ejqPvr<U+YctbeKrb8d2GOPC%pLRx=!wN@!?mjY%P_1Uq3QVLoHDsC4o|q(?D~9NOKMh}{b}+z~f;CLjvPe?%9s&@e^83Zs4wPrAC9zu7?WW@jk{n}1O)zvBwwJ~sP#e?B6HYg*(zX;*J8%>zD#y>_@i%fGR?qPgxr{1C!JM;5^Wu&T^B-+V$xG{OlujA_K_1nOdHTqGbO0J@Y@S-nAp=9-!FzYB{CoyJ0EVsN-FBlW~(0D7no8RLaX22vW5fI4=G!6dK_IBW+aL$*nqTT{n(ZD<!B<S-((G3gjE#XDg+;L3vF>y9B@-f&Uw=#4@G7zV{b0XvOHx9|p)+I+{Zsc;>jC(Ggtw+_RsJK*^NW^!ib3`@BiSCpFstz0CR|Mh?H6@bfglbLgMUbo2^Nnug_)fTW8{*~jnbQY!hYZ#BtrgTTGU8O$qH<Vg?ytbJ44SN<=*t1Jz;3f;)OLv{Jz_{U>-o&+tZ=XBpc2h3^EByOu0-y6%4j<QK;QRhJF^)3>);jDbA1AmeN;Ten?%n5(1T7aPNRYap3+eY1Xl+isxDx=he#3NWQ&&gg<x2+`*tV|5DZ-bIGe&@oI?R7GBR4oIwG7oMRC-qqK5t|LleCG{TQGSug!o6jE0!*{j4+0OtY<{#&jOi5Qs0EB!HFHh+h`WZspVB~;VcO>5TS;E&-+C4OwJ@vfG#c05~a+e9TvZYv9A*)3Y{$1k4Y{ob@3{G44ABMxi?XiB9a?UrVQu^aq8imC)iH?Tj`;4jQ4hOsxx209ce6z_<NG;cvey1u<sM;lenpk0-TWVB{!}bO>{tt0GFc3OYqD@vklC7tg|>E^hX&+WpCe_3cOx^o0#JDwuV$X^A?ywdOL=FvQ?Ni=lH5fg!=f)3?SNE#GigF2Y}9LjO8x<GCm$dE0B)jdH1P}8t$W)w_E+l`gML1V2Q_R<aBPbV!6dC1JKK<6=uXF3j;lN@D@%io&zxM5o2Gjfm^~z>lb{>xkZD4d6Mz7zKN;!S3Yc0zD@_=f+wq&e3gh;=VGV8&Bv>Oo9Kwd#H|^Lfx(e+5w$8bKaVn#63NM+)wcX!w5H<=kYIx;mEy`Btl<8`#zX!V;ewQ?fx~;af)^)Zm}DTb6}?zogMn~8;y=4+ejA-F<siX`sl2s{ANV3^B=j$sGZRUgOwUIUE9xk_o5@X?CJPG6p3n}hlC!9~FQFO9haY44{?F>LD$kfRP*fS?>qw8#V+2Jxb>uwUQUHM483xw~vU82^2AT3k%%V&pvf1!z!GOU6U*izk$%->#x6lgc>dncDPs!gLxDWb0K*PDmiZ&1)*&x6;S|n%XSg#^?{4~(Lhak2(7Iqo$O|Ff~UP{i;G_T{f9&kf+9^sdA2iA7aBXk^h-p;ee-0-{tI~h*S5ca3f=Ijf|uSPwcj*}6Nj96thv|8>aET*ZiQ5nr5<QLYPpJ!sUmc+e|G=hk{Ts-q4V0?51?uO*;{^9qwd>@`TjNA#JOcxK$B8ZD43abYu+?pFGvy2003IK`|7^9MW9{BbHN!qDz?j-ke7{$X!*_Rw)N4c|g1otZI<6uM{K4bKZb&95BUubb*(<VaN9v5sdPK{9(FjQ~t<nf6CM()}6VP|^#kpx)yloCUJTh9kTY9v;_{@$3-;_}V;LMj1`m1kCd;*FFSWatGfv|f@K7Rr_LfDpqxkT^q(vCcAwWXh4c@ZqQhb59eKndaUZry2{U)HWI*)NbrB8)m^Fps>)e<?sdISdJIg3gKdS5_KuaLkM0MVR10R>QrAk&>nqsehPP?t%2nXABxEJz-28(=9-Y(sONO7AN&8fdQrX!PR-fParrfbnk2ik*Klf{CDiO+PpAoN|LiB68f3sI0W?kxgNzqwH7sk)erTP1n!*)w&G3HYnka*n`>=AM;59L#4f{fB56L`D8*X&|(le9VUG*DvWzDrw3k6hjF>X4f&abjo%ijUczW-CUj@0Gyi?4<)->GkQwvH^(n0O2w@&a!q%!LQerG#a)wvNokd*03PayT|4Q|LJ8X5+nr1*OClyc{D72|^9XdX_v=!<MV=RD6rEP}Jb~V)0@a1C4uWw#TB@$mciHdL1$6M*VCZogWa1*7vhSR+q-TEh2T`+^yCT$d@2+H&3&s@oxiRM{S_G4Af;M{Y$Uk8zn9U78D62b!Y3g+E}<l-nIs-nUAtf9F0{15A?3i`B-=HdSiRD<O+uaep9jIkxpEwz0tO-E)aE}t9wz1R*d{PEl>AO4<Gd~ph`u-rI2UWFYK0#9>kHl!}DM2dD{%>UR)QcL7@`&aBlk`|9b4PDvNQoO!*JG->&Jp?-ctzTCXr3X`iA?wPmz>3l47GfFDnezPo-yW3_xjOx=Mz7A1(&pJ3{Y+V~?j^)iL~39q>;2(fP&2!fo1oXUM(!fBX|ylK9Sj4;$A*Nkh&fIV;&lEsbv3SLfiuujN$k;^4~#K=u-$83-*tpzS4YlIMqIl0{fcD!AJ785sY{IYYXR?v19`FYy9BE6nKNf;>y{dvvteEZzi^xnm`8cAGsNI*?ur7gd!S`LLBlY2OGJ34QV_;t0s8EsOd$8{UyX(O>wg|Q`Cd1OT`2TBou2tS)HOJOGZw#oEJbBcLqv7W$9EU?q!=Urv+%$K~(ui%2_A!!xl^Fg2X)EZZPGCM^3vt!vzK3!OmocP=Lb4Jaqb5=5r6fMXMfKK&;Zct}Wd_inZS)K+=>gd-Y@Bh;eEOFOQ`x&G4dHU1Un_P%&kv^!ABWb-Z%cc#ZuihMjVbGL7G{zcPmss4x9y&Pl5?(KCA81h*SW02*0akuRj+n-$>K*NyaG!B)n9eX)q3OHfd7$F~*QyB&LEO__U;trOYN&f}>-qFS#SbZ@w7bf@?GQGRGfg{q34Ugdb*Pz}#27nay>vki2%zfayDMlt6^T<&TR>@{c^b0%-6QNXQeUELwq%;>a>@|eS>3xX(Z98nzQ4Sjhxxs<5awF<=CVP#$<KBt<KCK*qwLVP5?@+-p+D(Jrj-l&c}?4RbKWW+y-L|hElA^%_Oz=;VIx_X@2T1$l#ObOWkx(j7B(OWCKFMv{V8lD9)nb!hB{f>r!fSVAdN&n*!vQ5A}QD<NE>wH&Ck4UJ7fQJW5$$IMS71)h8b?ovkpDH-&l$bfoQNdbq3NQyk}{lMpCFc)UYD$RI@#CW4@)X!h>c1*okkYEQJD7!KTP6lJMMcQsp<UF-4E7KG0c7JpV$Etaxj$XGzv?82sXB9Vx!jYJjF3b1ETg0^|c#MZk8k<yu$lPbhWKp&R=c#B>mv;QNHYniShVV$V%JSQmoEk$8<)D<eS84x~%$KOH3r=pLuiF5yXzHiI~tdPm8&PWwr8j5Pr|luWFV37_?S^GgD^6u83htKjG|P0GKE8g#cF7bc=qU@~-p|MoE*sCWTe_c{|$Tvw&JG|9dEh1=Ji=YVay9{a@P5tR{&MRk2m>oH*vovG@9);gpZ2EEMr1J4?h1bL!)T%R;5P{j8~bQsxL;WUF%AcF(yGu2fbpF4?TeDIR`VABm#qV&LI?kOCY9<AYNM9B%XOPt0QN!Qe4SHYj^^I4=%968d>6JtHu3;N>w!jcU<2C)$^yg`fCfQbK<sV-{A$hg25-CHi|+F^XU*V;v$zsxm$g2*3N{S9l9P5%@{9O?WeM1q5<^w}UrQ*?sOHJ$FcGNe{`fVnI}(ZZf{4RZ59t|`k+N2`o-A-`d42*NdFIl#cDxZsJe!HEX2&a?F->0j@x5k{f8Km|#v>k+t#H`QIFfp8g)XeP9uCbqbNhpdHds(jFK%yUuX=O!(xIMtn6*YzfIWuvm6Z0npj#fTV8q>dp1UJz4my3#l$JRg!?%=?^#hy;;6K&CWm=%tN-m9b;!yOjsr;B@9umU)mF=K+Vhn%Fl=&3rk%9Bo_+H8PjDch;MvUfwr@cINIoe?=@Tk6a(pDpfohj6u=Xcu}dJlzYm3uGQ$H>w2uYGv%F3WXXH_J_C<YGWM31FmeZ|^K(S;O4v*v?Y5X%dv8wdc!h5ofj74B_S6U*1$Y(KFsv=xgNl<dagDO~^@&QGacEkA2ivl;$pHBcycG>$f)YY#noFzrF#WZk7Q75HfNOY}RR(aa(f%T8CaqC33Qe8@XM~#RwW&t6{+^;{`WZE2optV?&jDxDTsI%|)?ZfyLrc}Jm=JO@pFeuEw(zB{^RhgpUOzzw3STB`wBI&WQm8|2-mlC4aVt&fZ+xZkSXc`Gxc<APg~uP_zuQnBGvq^6P-=mm6+*cvM2$5jF5N6Uj_S2>GJ*lQP*O-Qf<5BX@pzzIF7i^VeD=}RNRbEz>_@_xq(x{55&mMti`YkCaA3JIYid&+o7XIOPb&-FTeIK|-z^v3zhnb*@59f$TcR##FxC)Ydj&lTv1_tG@;W)wU}QsO$DXujhwW@}3;>FB2hZ97vmfno6lsZ_;2+D7G&ow4f`~T*Sl#BR5egI<*Gi1L+$*_2Y9MtMYK1YlNZj^S$uvLcDEr*r@O4CSq}Ey-kYKBjqA<ap&wwik36}(J11bYOz|Q+Ms#h&-tAe^#Gntb)23ldTnn_Uis3@3%K!?Pj>s9DkuF2^1hZ6u?*h85tu*%??&|}*cG2Q>nMa7UceIHM(7)C1>*3al3Te;ACT@95S>)zY#aY)n+Z%ncWa`E+U+)4;GPA94QvUpcdY6=4u{|K~Wh*NS?32zD{+Jpnlsu-Boj6qs%aVgwpB3O0<1W=$R;grG;n{tqJWNNxm4|pG#>r?8r=QEjb!IUV`j=36DP_OSE8E$G{%&c!PU8q;mnFB|(5=voqt&(DxrERdl#8Jl6rdEX4Ou~Dn`5<&nY0MEqpyGHSW{F!>XA<KmTuNv>MYEu>cGn+&?>^^L_q}JdZ+6f2Imee2aI8OJea`xY_ZO|sRiAUwzFCmF$p8C`{)CkjFIt_$MXM8OzqL9IxRWS<Go1H1ca%9#>sBX+)hvZ`Y~bB{^yb*)L>_t3=j^P{$wip0PAtoJ?kITB-?1|CFTGC3^GUy1D`dR6wl<Q}wiK??vPC0T55^5@Q-w;wUY^*fEkNXFwO4CvD$-b@z9$h}PU2A5u}NEjp!kGpqjqdYb<VdQrquOHGlj-2+?bv7e7mF|4{-2ci(w%UC(3Y%6@ZQz%E083={mdo*sHye5m~t&v;8{R_JH}~HBogQ4k>GdQDkbi(ny>_0@tO~7>vOr@3qDPNWx~1a6ba(T7?%iW@j}n)|n&FreTlfT0>~_g7i!fRj#{x0TN{4ruP@I=0=_2Z#UfhpBJUeUwpYdexCI_TW@WW_W(^@v^UZJ%MEOHne`-FH4tcaD!i~JJBOR7+eEbiQ?$!`6?+C5E#|X;G{!~(>9Dw<^hR_Un+AcE1iVpe5U3e_BZ_qB;`a@EMgSws*F_QGC}sm*SuAl#+pZ=iapcO?I_tKG2yzy7sPlQ2wpd8VcuXTGA_LQ|UK+MME#QTsRWb0Nya3PQWNDGE;oL!25PVYapux|m-5v_iF?G;kxG9<h=A7*m!##XE!|hwb<9uEF)P+Xd3}AfaKD9t{5|Cl7qh|Y5_hg@HICJm!zMSt<>3pBkBun?tf^pulN&V)xqBl*U@pDP_@SLPNhUB@p_bfln=4FVB2z4Jw+DInxEnZKQ8a2x1D2}RN#ajVEYJ4SP81aHB4!mQC>L0n-c4!=!P=eH`8)v#6v}?0vHX{Ja8dgc%^}-d6>889c9~n0cYn5t$e1}T);&A|mlwWDFQxiY^k#9*YJfFJ~q;pGxO>2_zzU8&na8F!RcXr1*h@YO{u8#K#2b5_PVZ$Al)`A3n&{~<BVE7mYo&2V5=`~G2CoFFHE|zAm`9c7FU*~^6P_{NTh477C?_J?WLnZL=Q-56z@kOQqx<z?)bsMq=m%m>wGdqkp8q&fZSNd2_e`A+<$IIN|GNVIVujKATkEk{cWba|uwWgh8d%nkYExfM7m+pW1nw@nRg=POF%*YIrHEg0U$<Oty;pKYPE@}}cti8n*EJh}FG-GKoGUfhNBS-eqEOv@n?0`oaI`h|2Vi<rQK*{_-pD07KZ(Hi3-Xl}X!Wh@*#a{<Ov2hUb0hkR!?CmT?Y34dAC$O~<E~@6(x7M~g04}3*LxE2&c<4fPQIt1`VmH!Zkg~esSq2FTX~)a*>8f_>KWh2(&${3C-OsmyQvgl(O-m#-`Zh+#KADr*4q!6k%-Hnhun#(a&#bAg!4FZ028`2#_IflK5~XNzp+_2qFxyzxYXPHJd&U^?GAuw_dYg60W-Fz46~yg`xd~{HvrxcN3hPk1`J81ZgRILM?Otj(N}Tm^XiTHw%gS0fO<XIYiRgYQGU5)^hMW^wjKCB4sA7b4bRb8}IY+P^ie>fNp=HoJnL!37P56Qc<xeKevq>%LKSX`p1W>-ID>DiTWVO5gR$NSW6=kD)=U=HIU5_)Q400KtnXnim0qhf6BdpM1mD$8;p#Q9Ro_^*3>sil2wnaG+^&ay|<|YR9xx~WPs)lvCcc$X3AI9MaWSEE%2d0{G)X)(+LUB=-i>fMzzPJ03dJ#@sH0YVMR6=LY7VR{6JC&<iqnZGCQzFm-d8-L1h`t#Xb6v8-CNH%Y9NgrUqg4olU(|f&pNv96GxHVe%(bi3ga!@_i)Lt-F7oPg5wB$FIyc!MR(9N?S-_sDm<70)BPX17Q}vp~z?a*)3oRKZU$=dWV8_=Y720?7?Q`w=$gHZ4wNX0LQB{lIX|J*GJO5tymz|}Tb)1-GX9^b%o{I#7kWz~@g9<3t`lc_FnS0JZv)3n!43>SxF<3mQkw%9!{xlHm>g}EbCO-1#^dG+fnR-u4F%1C5F6BIMiH#|CjT;O{q78+v6}t?Wj(HW!oAh;Iy?IHiIJdgUx_g5bHmQx&6fJ_m*pOf2jTzXfGY+sSp<U}s7I|n}R;Hfj%=q;MNw=_5cMV_VZ$R;$jL?hzd5u+KGp@|{5XSb+;{}TCgaysGs7OLj9mpLwL6ot>H8kR{f6W@@`|J7d=H2=486_pLK0RxcU#rtv9HIO-Jjs94wfwh#zD}z<bG=S`P&Z|%&|>YVA9uTyXHV<2w-`9!JoBB?UPdCo3G*fpOB#ReGEAVDedHHSH`w;;f*+@3HNcub(CS8}o2ozn-c;Xl;1RMmy#yZvrR{{n6mIYNo)24SknF4_t{;fDX)6pa5Tb(&`&ZIcIqf|IjX<0Z)`y)W^BG5|2N2-7TeBKEoWeR!Tfijkg?hCoteBZ$Mg8ynfwz?K{dgh(OQ!+h|N0EgJA7N!ok?Fs1j6(cB3*ZLi?S4U)q};voL+9+frEhPsvc{{E)}7dX+-Uf`yT)L-Dz69z|S&^O@v~c42@C2N~3fhE+<2q3CYQTb0JkES5`BjyryH3FUVP}?rT1%W6|*l$FOf5i~MXc=weD>J{&b4{_aOX9c+?32GRBYDyRcKA6T7z0y!A2;0?+v@dhrQK@Ol$$O+s~2eRXmw~=52L{$fN1=o0kGx}9`jebS_fpFhb{sMeu?s#a23w|K50iO3@i8^gfw%swp7#c{+cLqfm*bz4dHju{TU%UWCcuK<R+1OAghF1gSWO{%ypPRG2j{!^gFYA~co)Vf90IcxvBs%oSe5FJHk1_flIR+b{IUl*fcl@P6jt6Fec(^BLwqC9qq9$i9-A2*}fDHreiM4}hM_yhaB{!_rbfl>#TN(;np;2wen%}FP#2Nv`ad4<DI}-z8$q7zO$pjZ0gn)!E(vCw7wlKYEpPjs=FvKO}l{3*fu|+YBlD*`T!O9R!QKc8ig@oT%z&jh=3ZWCLL`kp&DE3hhqa~EahgMXoErQN6fnpSNj%OUpi3Qtkp=czA=d8e?5It%-8taW1T!y&FhO`55PLrN*NihEXo7QW+`PvAjd3M%4(3X6?Y;i+DJ1O~mp>7sm^lz4k<#0tM$J97gyD7GK`5C;YEygj&jE&9HmayEkayogia|{NiSv_xtwXwRe^Q~slv~sM6#lfZcK`fu*)~ndr66T*@!b(H3NDfyH_qZh+g3N6dYtc1@9cn6;meq<aQ_zwa)ON&9G18gkat07%tl>2`S84NiwYh4n>W^88`c3y+ewqn)^@%&;>l~{Xj!Fx2q%)+Po6<rsrG@xlVGAl38$$JI$(79gitPvHs139Pq)FZOv!pMAJy~wqTxo95gI*TA%$2*2P0<AS$+#yc0V@}2h$Q>@CZ~eEwa%m*1=8(7W5Jw|PgY=PSI5bKga=h3(NkD6!cA|`UTm~AboTsQl-`Gy+dt78X5(Kzkf>iGjf=6adw#MK3>U;8yidpEL}??|%@TXYeWF5S_K$ofBu~AbMp3m)&;x*lNPa_(&0nyUrEM<R)G`#wV_qJ(ztlzgm=fr8L(Qnu+2#^tCyK8EuEt2gi~yale3YUQ?sjJiJN39tFoQAWs4thfaRgidI)1XUI8t@Pfv+=g7L6&4IY?L{4Yu-!R&k258g7ag_<al;FZC?=?RnqO;f1?N)J3HRA%ZMawCjx>5>E!kZH{#+XDw=BIG6_4b4##rgDMj%qEgznf(E0AwuZC5L37d&@@yl9kBi)tS>>1fk?{>ht`P#P>4IQ~9imxip=me@zo(s11$1PPDyHJdf9ER&yBRsidjz{3OBQu4l)%o@U4zJH3wBFXITFDxjbE27gNR8KQtBY+4ga?24xlu+LVb%lyvFSC^)p~6uZt?$JMuXKJYvvEZOyOfp=6buY40ffompz<8^>#{J;zqA;r3yBM^k@ZwvXVJP?)7v?jt0auC|i4k8lvxZ^fjU`v?(!eP<=Z?kP^^5)=L%kX`%#Y_#rJ#QppgAf35^)^n(K&&jtosLni88#QKz;Tl@UOZ99fOVX*_Ye)h(wTgP^Ew_@1vJ#*P!OV@dCoGiGP-wv<!^yR!askx>1E?=z$_igA&Zq%=X8EYCsk{OQJL7i_jB6xAqc1SycM7?M^>>9oQmZLMeOls1waC00uwjl?q^7^c7aW_qytU)#pD9aW?Rv?Ya?Bzdn`LRrY1qn#b$}ITWUhLjy|6;{Mqu!^j@*TAMp}>DX!YVmo=m-;H=$X&fAsF$-~aHjyk}$RD~#n%?|qN4yc)<mZ|z|Ymgk1^ey$cp<K63{)#__lG-2R?et2#~50vJtFW4fszA~b>kklaUCeH~bUb!04RAumVbmkGdxQuAUnCn5^HP9ZgbQ>(eqw&3c3QtEjM1oY1>g*RX0?*qVsBk?q*as=AcCZ$m2m78oL`W;38;5+nHsrhOLmt_M=b#Q=D>%k`|FOpVpZnVSGS5@lyH``$3EG$TOv^w!F9@(Sj2iKB#b&qhK6A%bZ1#Xy2xv*M*}Ij>GFhsLig{L|lIC7-OtIWzF%}&R7-fLmWZju1qb%}^x4vNF{*M$w*vKHL0~kK2fAvvD=mdv>Q&6vw%+bYZui<^a;<VT2@`(VUXE=hu-u>z8(s`}Y^oRuw3Ehdm6yJ(Xx|uB>7>=kn_<`lSs5F3l#h&MTXoybq#W4c|*NFN>#~Oo7>PM=Ts_RF=CN3qqpWw7hz7tx@uHQjow|IeJ5src7!1`2H^(5(cvcGv&9h=i2jXNeDw0%~ghZt>|3Tv3~y=+lCot0o~kx7}Xd{wydqR~Us3Li>gRM0p<wpH3?+IprmhhugOAtQA_q)wqN-joV>8lBa}m;+Ka;oo|_Dflp(f^X`eq&}Y1U*!uvK^}bKt>}vHddlBnpd)J~fEX>n`qJ-p!Hm5r{f4<0<n~Q7UoO0uqBug57HgNtkR#fdKV~|PmKuv^rJheutMB^Jj3WjT9x?Qi$SQE`29VUpNa?};5C`_+Cn{4n-|o=k{6ms-c8UjnDKafWze9f99nhAj%X{BbSQVfpD2ep;4DNrghmkfd|I}**mwtf?_>U;K-bsK^aU=&WCgX$qoLWicUM?^$H0eRV1I4*CO~G_zA-<EmV@wZ_PAYVar-l+?S|^OEH$HZc?lY3u<2^<O7LYq&1p`Ed-46HJDbyr#1$T_u6JaP1mdN-66Ls$%{@|;>E>`a0hI6y`c|s^q&ubXC=&CqRqIx)DF^1+SWugXtY3#fALR>fyq^9t=p%Nw(6;XhmSmZl!Z4PW@=7#XPCnczUr#DLDju;<>I$8N1SAA*<A>k<d8Z-qHrKI*OCh%Rt9GK~Vxe{y`VNj)F5Nh&n?UQ4#^ndf)V^FVpM|Hs%t#|Z<A$YZSG_ExKS}wisgOn1kC(?CFvVzh1tMuu)cZAKO%=K2*E3I)vF-KIRIt4ANlyfh%<!|Py&O4%kj;uc0)R?2cl0sjQR&Bo=+kUBSnA6{{88M71mtAvMb&WEVN4<)$tkm4j$umKLxy54_$#cFg-S@F|`~I(Qs;}7^1TV3vzj9ymYh_bY<WD1X&8BvqtX5K{y4F*C%BgM~|H;^nO^Rr45YYJKI<1;RcNv}?#Mc1PMN)ztwQGF`)L_-`glZ_~O=ka%SSlN#b#=>agkEiJ76hfY5<6Xi>oruni=pbno-n75lcRG>((rMbn!onmLX$5LWcHUrlZJ`t+smTg#CH*71c+dD{t^?B)+&<*=`7C@WEwgsF_krf%q2RgVImqJ!h|OAj8S85uc_4v4N<q)k;T;P>j$L<h`4zrAmY~05a}<kxBdLWwtt6ZrLVty=JH<g4R!F^9Vkc7jD?y#z^Bo`$II4|@g$r1o@rIxYbJ3+pbsMV0aP6N#AFO|E)?<!Mva%F<Fo;Jd{^(JoT(((kwE&^5kgWg$Sea&JH0^p&UypKgtt$O&uXRwkr@aB*3YdUs{qR?9`#@o#z{DKsCbN!ne$ub6T^V6^e($!;eZ;XOx9Y1#d;0?A%;72aHy*dDNtwV_Ke-+Sg&s{&FUb$;9ihj^@6cT`np`!rJ)8Qn_}uGY+=a}(X;k~cMi$TB$_3J@d5GvtqG$=A{4PH|A9K|rsVTa*s&?tFG>fL@kGay+z9XKl<rcU9yIOoAi3-Jbni~y2<b^N%N>@`+ac`gO&{H(hjR9h&~}Fs<%tbBe+%!$xh-p8PyNJr^6hsj<V0!kde}91=pu#X#iNk3@g&`)`T+&F(0doZs2BXR_*qSt?kS~23OgKGc7D&9)$>nE&&Sa)0B@3APHaQp7&K_Y68_v4y6fI2w#%Lb$8%87U@+3sS|!0XL#az>kbO#VhChw#2rpy3>XU0^4mL*CTPQaZwY4G7*;pO&CC%neId7ps`pL~~Vbv!ALH4Xw;@7Q`CC=k6TI1IZJMH{t!TKb!(`d30#AT;wp&lw9>7rYLfKNhO&jox<JmOln<XYoBeiuY^e(u7mrd+eCDetnX5dagsWs(r{hg#LVop3kHCXp?ix+iWmKW5r@;a2mLCvG)q<yP}WbF2ArL_<qLrTWU|R@0m4M)qfhHK`faq_1pP6PsZTa0JQJOEIBoTa(tdHOZgiyPa#WSw)cx&YWw?g>#L=#eX}S*Fd6}J(grOOrQo<{xyxhKy3lcKYYYn`d1`zUnnMnQ<ihhHQO3=6PjmDzw)e+0R=s4U|54CHM=+03~S=oW>{ki4{wnZT=lFW4D?&Jtr=cV;=!dLT7Xm@s!BFCj}{bK6(p9pDa?ae<sk$)YAuVl?#%cY>EMfn!_|=N9HkRcqC1%jJfsSPauv-F<Dj67C~#+BNMLSzt)3T}pLG+E2#qeobsGCn$04E8s)uAT|JpBP5lO_@r=_)`kCAEGhOu}P2Yt<j1rnzqol<8MWlcI~OTLfBcH;&S*Mya<ER3%g^+d{vMp%)K+hQ#`+eT~GRO{5)=O%qL)q%tEje;}8k3N4fU*_n~e*SBF@k{^`5Jl(a%-onwem&%ePNFW(UrIx$k%TOQYDe&9^4$KzCu7v!nDr6!Rc(|VBlI-;?<58i`VXsfrX2KgSl?(&ZsrNuoeEMhWT5%u-+XUf$mbeC*LWXmH>aHm#H^zxX-h9q_fhQ;Pr<33qL)T{O)zGhoAUK_olKmXK%|zQI=?ZLW*;Y3wt5X-bvM&F@}2a1WnO+!LQueij1P-01**4sr49+nQ&UC)PAN2P7sCcNb-)38V`sfaBBdf5nT0Hlz6nGUBGikx(=;N-*JwokS-X21AAa!FhzjNZXYXxdZQIi8p!v7vT5IpMf6hMpoO|lMSFh}<vRy8_>{1CLq}&!lw4o6s8U!H`;YbD=h(yGR5DsZM3JH#7%SMQR6d^hU8VK<t1cD$yD4-w^GzcLL8WBAt1X2)ljPcF&vwzOn_rCk?wO!}w)~S8=S$plZ=9+VUf8!g&TffQ4qig+EE+N%3BsrQ5c1Oc{7#pknFm~>dlU2AaQ-a_gv{Gv{i$CQyo0$@XbPGDsR9k9MJ}>r1gy!@RshEY(h2VF*8Ao2~UiHGzm))2>vN+Gm+|oob2sQVV4`TPPYivPfHvS~KoZUH`K4s@TlKn&yp(Oz9yf9{Cs})#12fCKN{<JmeM60!VfCU`Ba6fyiMPg@rUh{RaLJeuj6xT%BrMtRMljwaiJE}j(&9Yx(+tdxR4a(cCcGbuTx+!4~KDiG3?(utohF6;-tQ$cFCPpEsA6*#GFttIUzA&5$p1aDyMA)x#JDfVs_?2rv<n&YH6{>a0(Kd1qIstlGB4BOo;6V0OHB#ChpK7ze`lfA<WP7JsA?Fu8lM8d<nK;n#a@SCy)g>`vpG<`AMI?8%nbWSM9+2!_%rBUXQmB-S^=yJ5*kR*8CEmlS$aZ6p5f^4=cKYCWaELQ=R}F;|5WfDabdJ--S9x|7^U~}La4DsICzQOj8LFEz4J^5lgYvia+R}J!vlq?6Oxd5(_zsoJ*zi}!CrVnV9z6eQJE7j^?kymx7f_$Q2LD9aGt0~V7p`uY4Jm_%VoAR1`j(;#M+;;W@4)5z4AXzd?o&vQDM?ujODFh(mA;GrKMbxPxpCF6pw@=u9)v6_`{979+Cviz=B(Y1?f7M#ZM|_kZ&FpX1TY4!0n~mYHbY^ALS;EFC;tWoEz6=zdu%%$Nes&aZG$A9useUgmW&Qtxwmfjg%?~_V!)q&=G#a3(n!ty6?fyFRd%ayq6SeyZNt^l9vsqaZ{l`COHTS3BKsAPiD^t^7iNXRm^&s0r<(|-im}`zXMM6-*wy0-;`r^I0ZQ3^(l*8t*D%4+Whuh3x*aFK*H|2FspCAss|u}EfePnZoNDHFQW1gJSKhB(fc<Ll)X_)9n?!6S76L@|FCIwYj=i}1ef6<NqDTotH}GUq<!Qu&8mY|LobRTrUH!Ty8J(VdOKpf*tCv=qX|lR?jyqafT%J1P)fw}>a*BV;`UvP2e$_sLffHfuBZy+2uQEq+sKl+(8Fz$O)~x<}Pe}+J9JSHuBd|n0r5-od3oJerj1xK+sA5ZiWh|CX%8v~tkBUE%A<{z<>&QwDX-QjYr4!Dq46d-!WJu%KcO*9?aydjJG{jbBWSeqXD+fW4R4G5cs_h10)^3ojH6TdRRN;q6675KQU1BlV@aT;Sy_|F->V>FuRL`QD*(uckv`WYg!Fka&q3V68RRKO~8WksL8sfjW;NAU-(qrLDmuy>|Pv^Jcy~;t!+>I_8K@lBJrdkKLiWV4G2}AYAV*l(<0)-Bva#9Y8OyUlXl2a_5uu)bzl_%<BG1U<rrN`9Q98px5s~A@Gu@ecy<D@%=`ZY6V-GjTA7xHI6WFWV_LhvuJ>PW_YA&RTC$Bf_djI$`19@&DxE>~4373aD|*v4><WjX2Xwqc6d$^`71Nlnrx6B-13gdL<CA+Q*4XZHQ|D}rHV`ovqSCY&w^WFbIko&iFm5c|wuMn0LOXf3+6dcGK~_1dNPll;uxCDErtxt2fo&QIxhiY<QmDP`@$zWFLoiKWucFG6f_m6m1Gh1(v~hQ)tpPpNE$rnsQ$TAV*6ftyh=Ve7xe)Nv70E1<sgphBeiV9{Yf@lQ*rJli$_p_}W2YL_}edn>1(N(F(;?mzt)@S!ti!Ujl!s=<&?sYt6<8s$J&OA^vcZJd509zE4yXxYBdbk{T(l%B=2?buYcai+08LcUW~ncq|lHgPzfLXi|JsdAv!q)zzvfq(6Yx)7(XANg=NHH=woK~x&M6=wtm&%~?JSNXO<PD@bXfQU;%s#1-p2Bj21SOAoxbQZfd%-c8tOe=%9fqmJ`s!2VoNlYiglFuX=to=s)oE@Q!i8{i{29OoW`G4#kM3SWfS#~PQNevW2$|L{=692xO+aLO{NB+i(2WbBw03VA&4B+=iTkSoR1v#8|fhBa{49j8bgFI@KzDaaNMhz2i^kwHfQkVsRQzzv|1lm>ZSb{C{{ACF9bml&YIAUeTV<KlFDpwTI>IoCT)!t*;W(=5*zj`Y`wyWsaZ@FfGqtak)0M=My(qZEoVnbVENz0RN6Dji92Z~==m&zOP7?e<;4F+-@p{r;eHPt&D+(toT`KM0f>aoswJpQo*EN2KhbVS@@8|1g(;=B4;PwW*Rl-eYQ#<zP6006AP8B~`k%`5`=A@Ch6$d(&jTjd0JU-am?akNlW^^IL5cSUF;0%xERXw@632Tr!XuEiJOB;{cCcDA0#zkmDvJ^Fze&ACUvSB9{9^wubBDo+cKes7co*b+&>FG`tybm3{dgUZNE80h0!3l>b8M06Rk7|>F<Hr3A?HV2zUGLRvmZ&09Gv#FEf?c7wid_>m!50!9|J7fFp14WsHnPKS`yO`7#qY_9#Jqd^v$-hl{RNMCHs#wz98w!1l0GQ9V{F2kLBOMtRwy+{%Ub8_%CEQygq^U4YPp)dYHF4ImtZoNf0t<v>RCLiQ5f(`_ya9_IS?_HA>a8LF{fzgnoTJ4HpgP3f*DM4773W2nfIAB_TURrKW28@vK6yng0vs@x0ndvJKQ<Pea$hpK0FGZ0(1D{EET2wRNrcQ0h^=9)%+8@k#F=BCP>MGZ(UmA7l9TS6LgQrOQNbGj70aiQ(arLM!u7HE8l(^r@-k0HzHaG91a&AV28&}|X;G+(5;IDc7;X8uEa^F(cKlhh8Bq)t%6V%FgfWokT=ho6*s?b=7&RaNI&$n8bDmSc+g6!Qm9p!%>r0J_p3N*?sv<PhR@Ev`>KFgwd+@EcM}GQvLG=_4aA&Qc7z|3_Sla{j9hC*?sB01h@J~pdkv0?bC=GH0F>NuqEW9jlHe}i4=83cl((RNHXU2O4f*nT2*pPyRPtnUwhJjT5GliX0_QNq7@}{fo%`84XzVT{ZK~@e}+ZmKKk=GqC+bHB1*382i5tt+a_L3kdyG$EoDI#Rw2|42=-H8T8C?FZEWbPr#ZGhBSp`xLEhIX7t-Upm{MGt0Ua}W-s{~I3_QO|_`LX&Lthe>R9QI+@<wM=}3`NNTzU6OrEqi3N>7TH%8Zt#c8bBoqQLs;U>AD*0H;Ho?;Hkkk`Lm@X3+`;<;h@`70Tp2#qz!abHgp*<;kVbeGYWm2z2~T)d&*I54ech%pj;J*2bCf_!CQK^^t0xpcb|0+C5zDy0AW=5C#J|fV%KYai=&E6fuKJdD-$G$^LRbC5C3F?{5Wfz7O>|ZF-sq~m&ucO0q%=aSh~@Y>@BSVy*+&Ca{a_BNiVH-Q2nWkn^#|Yw%Ux3zm2fJy97^<l#8UMYOO-2@%6|wf)r!gdt^%o6b0AfuQpQU_s+O&qUhOOdQl*PPsu_x^6@;pp@KePIzGcQBU&l}7il1tLYASBYb^Mfft2jZZx*3G(XXts45UL*$LiPD22vz&O5USx6LS^~xxA7u=>Z60F{@a(t)n+D}S~?4yfmc|$#2NIbE%6gSIziIg<~C+@lU{L>ez&ymoV@`AM8NQCL)XS<Vi^tIw-i>2@}$&gdn&iWMv%Sad23?|&qH<B)s%y5y|K-NiZ!J;Q0RNpUCGQ;`l@ZtrV}cRF^`W)xAR74RZkMEBi(#-F~y23qTF@U7)5VqvNoQY=QXKO-fza{f+apyVN$e4lRJ(~yHbCNH{8pL4a^@)fF-^=Q}B6z$q9V>Orxs1j@^#;lQh*u)b_3y<0#Uc2H8$Cyf#TwR|;=qrNx{33<GkdkyQI_oH+^Y44oaM8x@t{97Ma1ZI{j<SYy<Jewq`rra6AZW{^Sm1b=l+=g^tBho87#V5rr*9Jn>Jq2oo&(ZBD0eToX3H?Ebn`oeiX3ke(7e9z@C5iqlPA2d`Ckl04tG~9#w2)!T!UHnl~K*iHqCy^j|qB+2N9x%*@WK|bpk&@Jz#XFBx;lfjS6a&___g2bOL0Je)Rp1innL@NkEj6Zhj==yA?~2Q84d<&P5(^#X_z1%TvdouXI~rl7KXQ$;%SnsV^k&bAkYpgtmt-6`A`<xR#!KjuZrsV7RlJKL$LK2yffcD*ai4W=#3)8p2BYO!;V`PMZ48C#9PnxE&SCk}JBwA7i)g3vB4Ma)NVConp$5gssog3{tdxNV68al@mxNrbGE1#LydCBgP9V2n(T0{f2=sgWwah#;Mkm`9O>S$3Ca?s<9d1u@RU9a|Gh^p!u>MsfS<BM>k<tbus8)4)!zn3`r#62z9#e3x4aPof5MAb&$a~-`<+|Ds$vanxAd=x~>i}0Gb$xG&^vf*O5$q>draCm723t*#mcSqs3RSeG((cEp&ReUrhNqffZ9yJQtSA5tloA**_!$bT89_A_mfHz%nr3*aINgXPvqtRGNTWZZbZR<5nVuk=gJ9AAgu-5U)fgA3r%G*4<jBZJfAYcU9kJ~beUd9>e;(mUz-7gKtXK(wj$HhPL2H$MVa<wdm*4mCZbV*H0&6kNdeMlE2;xvtZDVf6&wd7jx`;(E)TZ@u+{RvLy-0IZRsBa;R|Qjr30@WEu-}ooFc916;}6SS{Iw6Mb~CTqyDNe>R*m%AGqsx(mzAuS1aHEO$S9m?-XtTxX2xJCdqcbfcIliZpRTL2H*u7`DObHzzKMYDMkaM*Y@SoTQBN9|I_kvKzY)U9n|@6+k}W^+4q0Bmir>Jagm`Mp`V>PiBo-TVm&RnuH|tpAanroHs2a|=d(klbiQ@6U@ku)Lj0N{yn)Ki~G}k@8?oyNctVypi6YrHVYA$AsW>e4HK!27o>b#g}##X%?4Zb;+PfwCYvclALcs6OYs!1bdjLvGObDyzI){onylZ+85DCmX6N{)5nQBE`T<&4p%P8a=}`^$d#S%<8T2YXWY<c1%b5FuWdpSvoqWY(Eg7*bdt4r=A~NeT*1ta=nSIA9`+-lTajHj-#Fo$ZQDP9Mk|r-+OWtaS|_B)ntFI=RNEE%C&@4XS4H=(39_RE26>KySpO%x@E4LCf$xM@_dKuRIu2lN#RB3R(_gZZ0SPCKz4lT<J)|Eo*@SvlDh!OiGqjQa=h_Kb4O>$|cj@9n&G1OJ4a;Q$2Xad(V#`zhR>XukBEo%{}>Hs+?2&`);T8L8bTSG4H{oa4gTwn`F`+RiDVL)9y~80>ZP^0ekO**nIFr!v2lAq44HjZAXV7jAl9h0Zq~Fp}hH^aSD4-2$AIeo_V*jpW}Po=j9zto-iDkj7tOn-@Ew5E&0jyN6b%lSMrm8mv=u{<|qHaGC!Fw<tN`R^OIA%XJVr#5Xx8cllg<?CncNt!Sa*yM$bIUPyUGc$<3IboV9qSWs0)lRcyRvDcQZHlBH!S$+n0rWv479r9hu=^i0oYDbvL)W%`gQ%J{n{MfvC4FU169mzcf<{|P(r=aC&K4DuhnDG>goHt_V_0PcZwPb*g@?>BhWBvBBqobgi{DA-tH)xm-?<0MYT_?w7cK|TOh^bwPETh9J~6>z9jG?{0};>47f?1egKW%wwe0vx{;%a$Ae3MQ~<T^NM<@Ed#Ss665$`&ui^mN4Xt2i_(<3yUT7Ca+eeB#&FMhsa&WaD#|JeyaR>EUq?g1n?iGH;^+tnjMLjmh}07P80BQgfH2E0|jNt!vlPlCtVMFQmd-BzoXB58`Y|>h}GiudGfNSi=aqyj9%ni^%cO{@`H&ZJVqtrHV|+s$LnGVTSJu)zJH?d9cL^H8VC6Njj2?5ldV?-F9IN<vm3z_i1CpAcc#>#g54x>@EYoQWTi~Ef)TJ)9veSJF{DNvn}=Me*+`)WL@I1(O4uk1YExUoO=rZH-dGG5bgb&4%*5LH)>twb6B95VEQd8IfGX|6??T+%)z;$LuhVI`oDreVxL7UE!e?g(w_ci0bUiajXmP)LyYh9-8(v~$rR&*K1udOLM!__~@<(Qa_%A=O_-u2jveMNk{JgSqO%`NlO@P@D9M*rk;8&ul6Ee`+H%}sOAcJFTVYeAjKutWWDSi$So?`CKs~jD>(||jW9FFkPQJUyXYL=)dmQQNHon`^I@S!%poQ}surkUWZ7`-2sR3jIIns~hozWTHzBY*aSL40C^$!HTFs!jZk`bpE5<;j18J3Po<VtNBhBuf6e?aSm%mNDFmw%>i%nFE!pEFtt~9}EhbEovZv74WM5Fxen|kTjX0mQQLh&Cr=WII@F*oPeWJozguI0AyAL1$<UnsQ~*GXit4TTh#T-ME2g^mlkOW7<x{Po%0Ywel)vgAM{4dDJS}YU!5Ln78<Zwj8Z@UI#?atZw-rdwYdE~pZ~*m-CuIQ>6;%~d<}iCm9wmC$7Z40pGhxH(tj!Mti=piqK!v^^I-TV^_7|oFq;5X^^Aw&*VDJqeof{x!0cNe^+de|lgtcwd+f|;merd{r#G0y0|F0m5l}!=`oV^giTYQreOI%w-Uhww27|DZk#Ge^-d}#a9QDMmH!SNr?AD3?tw1P1kJ9y5@q#KHfb*q&2|EP<@I9L{`W?0iEzCx0govZOxO%q{oKa}IB-&J<Or@l^0`fI#^%tbduau4HxH!-)5Y@_?Hsml9+HbI$ta_*<c+~46N0RbCeNzNmu7`5*m@{{%w}BIt0(x9%K&TJo7fuK4ZG*&O9xz=yW~A#hi*(7j3L@s@Kv!KE)#5SU^Yy{xPUI{4GNpFrD>CEFGwg83c>N7mJZM`fHjQ~q;0Lvq!}#sY>pb3>{5q5HxTG?nzo{NxCAz?m5&9z%myJmdqw^s>*tW_CST=YxfE}=8j7AYR{s5Kl&Z^{o5J)#zl!n80YJX#fbiOtIcVC0n`|qvnw<zxdVazWlz*$edo&aZNk^s3Y3Gif4v{?dtCjBl;ES5y`IV}NhJ;<j1zDR(#(aJb^B>m!yE*E(e#x4RAo=LU*=@a0;eCy(W1llnk$mv#Q%$@67w%yzVit+F`siZ}*SsW__UT<aydT!TobywV57@<gayANpFIi&EIM^nc{ZXfOj1*I`J;n2B5!yF%1R7;tY;}%=!&_bO(Z`={H8-of%do=6VGp(l6mdCzbiBURseP}ku=~X_}GI6=u0nUIHFY<YFgNV#C(j;%3YIUrtEC=$JZXLz4aeX$@dvoL-%ow)X!H)0~BzYg|J~j|Fyyt*5M}mmBb*yWSDjrclc;u~bj#hoHXTaXrkfM7}O7A;oSr(1T_JRIj#Ge`l>}yN&a$}dS#v@af<>N=!jGa`XxrN%US)`<gzXni&IjSg{6@z=;M}NNK{lg3T$OIvPE~~(vhQz^Z%lolArpE+_ZomU0edJTf_wLJveU<kl3n69Sa1bL32BticrxbU4r`%L(;^7|SgnU4P1T5^ci=VOJnbxoskq8rXpEdFGLy&%&@CjK>=G*{VHR>tLlH#}St=V?$OSgY9ezWXmZw#rhP4N*@%qbsZryQ$C8^Zkqwu0_&e?pCykD^yZv7(v43!n_6SW)A`v(hdviWP0%U92e0#EQ~2v7&HYsmN8Oq6%kzQLIQzPe5y|s(wo`Aj$A>ee=%BEox`1Vnt?8(x<W~fAgc_@2il@1%bGkmWvfsvnjd^RCFox#|o-5QJ21{EEJ<aoK&<%2tK7<M5?_a;7a4lFjG82Rp*^jqFq%+CbEvAaDI|^x0G4qv-mk`GwO$whD%{xZnKq?7SrTWt;$9#ELM8Z{z8?~D?$pSkRfa)R_PFw0LhjU)tS-GWMOh^>4)8I>4#6N3->{K+()Kx%*`u3?q$R8XM1Q+Tg=$t?p2>em+74qElEMPly_^Ofr1>_n8sp(t|NiFuwX4+=&W{9kwS1+^<xfeE7l!Vl@QyIuWWLdQ5wk;83A${D@$E@?%<89lmw!-;vScmdmP0}V^fScDGACrY(y)+Hx`&}rH<<j#tD+@`78(uA7(x7@gKavFI^pkLqc5{;l&eH&6_uxK*c)<=@_-E7mx6Zgsx#Mrzei+0YPlf7O=8NzPslc2vhiZRgn#R41Vz-KON43N<~yLKGMf0%CO8K)RG(a%DK3A>F$eA{1iyHl#6^rXSh6zdrbQ7$#0B7yEreANQ@Yt5Lh-OX9xJ94BUV5@pe&#-u;QD{B>B$d>2(0Q#3s8*u^CN@vd{#XIgeKv8zAMy81($@@ayl)O0s+aR9o{B<7pNE{aLHQ5B(4i|OeW>ZPp3sB*rA2KTJEd|(5eQ7NKMi(Ry-TPVHXWK3w>5tE$?V!Or??byr61>;RLPA)xoBU@nFTl%SiX{4|*uw}W_`y0rj^QCsCBvRF>EfRx{LHOTnLiKRUzOD(?5tlJzikQr@kEe4=W;qkkzWO>Rl$qt(oa)Hgb9GKtvkYLVpK-V>%yM%<?Rx@JKR2_gaek0_FLQfUr<ID?lKK{fc@#F1Q)y|FQ^%HFTH{qPjtEbQrZN%6skFIyDt%&`{4czd1X&}Jg+t^!6`4c{vUcr=GjZjwa=d#Eq$J!j;|>xlpo6sELhYf+CL)wc*3k46AESV18_N_QNfunQlJeNZ$k32sp@o1PNEX_LoCvMgwvX-}k{7ftfq;VmPd3xz$rUp>L>7|j`8_hXB3$6XE0}BYV8lL<sDQ)@&46jq;z^M~27h8Dwp>74VscMHd{mm)UPLjaL{*CNS==o8a3Nw=er;i)em+nJ?SFDN6Hyl%o*xLkF81>aq^-L%{=7_wybM%FH5^RpK^&EdE>UHYR_C{YcgkRr1S7JPo~-&C(?sV?s%y}lk=?)#{L{*qp^2_fm2!9_!}O_bD-&M*7i_w-`9rV0pEtN0cWA0qdBQ#lAzR6|CA~ON*-=D2&%5Mj7Zye~zWSy$I)r*vvzx75^{Oaa8Y0?W7MPB%*8oQTdQ&5!TZiRQ2g9o1@QHH$uH<SjzL8{VwYRm<9vb6{75}t_MaeWp6fCG6B+O4}ojnX{qN{uW6;y9GXe|TdR}a*Ag%|kCx9<hrC`WjZ7U5zqXm$}=a2;q@a>v^0N?QQ-2y~xgHTtH*l9upar{gUX;ic%uWJJP(AAHl8_#i$4jx8)TMD=6<ZnhFNlkguHR=^mH-a9Py))qMg3fsg*zQ<<=u5J8vAGGNpS-AJyU${`Qq$z@jU%~ZKcAT>Q?XxQk3UzF8e8U~8`FC4qh~LOsoXI)ai<9?Xe|^7SU&r(7{`GZ)Uq|?LgkOJs9pU%+HGG&~!+U%@zsq0q*K*lk_1BN&LcC7Yuj$ut`q%v7z9_#A?7Mt6J^SlBefGy^V1xfkzlIO=YrgqcKySTeRrKrps`TslSN{&bE?)baUIRg@Q`w8>e>x>w^x5;jrc_@vx16p143~cfQ71+}OZ3$D(<r{`ou6LMKfB=0oS6EZ^)Uz{*Hm#4)GEMu8-&!gDkZ>qvFq9VnMkUKx**9Ftp*c}E<=57M#mXVq0>op(GXw4GOBmT&)#H{B&bOBFA$1EmdaR#(yS>cP4CoyBs}STsOPuig8?h2cl_x)Cx5;6tCCzg=hd^-XEeWyXaM8I7lm#bBFx^;I97e#!Gcu5e7y9}ZfbmIaY^b~xpWuxlI)tJHwl@@Ty&@!YRjLNb{y}~8~21?Tmy)CDv`*wWBkbh)(Jj8W_)Dzc68<FrmWZV;$t#;h<de}djjd2_S_^?7m)U=944vi3?*Nga5z5aKchDlO~ZWf*Tv7kBke|}clfgsu$;dC{HN@vt1UyPf9>kEg~f~W&xVU1f9Z}=w0(R2rt|Lnt}lFVxN^<cFLnOG=SCyAYlEymEe=kn7w`S0XZQSHyTu%szZieoW!G^VM~@xg{`{X`4*ud(nvj>?@w2Nsos%!!*Z7E+PtfF&FMjaqRG;0ly^}5<bMaG`XIh+(10SUf!Mlvi_@)Woj-)*P5;2V*&EH9}@&EWr;ED|Tl8d$Qd=a7srJE}hvC(vSCWu-Wsi(_Yc=EaYdF1?{7Aq)XTT%dMZ#QuY_JR{i>4~jZYeN^+PiD{}W7#E~UF||7R0a&FH8Lnvg4%#ea2U(sYKTZdt>USA8Bv@?;#!WXJ%*~mO+q(6Vl8}n32Ra1xec+_lVLWSE}ECAXiZ~`JPCe*xFGK_W@)XFvr;15TF+(5GP#Lv0AC5`Xx&^P0-1Pfeiwn((w_zw$dBC96Eqkwm7e1Msd9n50r4GZT#l&C=GuqtYfBk`6OTsK4q6uSTc~YbposF$p{2+bDKX-B*w&<4Vz3r^&7F=d41w&sQbED-4@7Q2W*WHlWXxOadZCTnQxC|P$7eqiSxGv4A38Uv<VhBrd$)@INErsj80Amhqoa<csRgcR{yTc`I01W$)RG>kFv)`zr37s{17}*9u6OGB)fIA^%Ws4g#-|SD){iF1r43PN9seJGRFG?B4Y~=QbpvaVp=nHX<pfGYf>Bf~Pf4aLWe_*41WpNqxAIwqW{GXpHqinm13_8VOGOz(QB$=BL|<tcme?$-8IPMqz6PIZSnp+sY5a!Kc76kC5r5v0AcDehDALB2^<^bOuQ5}oQMw;NG=#JoEvZLOfSP#xv#3^o0>;|HXzdKh<Kq8qQzilef!Xp5x<8Bv{e>1*Y^}b3nOR_k$$pOXp9>r>{}WCAq)<s&@u?F`3WUO~ri+XN2czI;8yL3$(G65lq*VD}tDql{u+$_p6SfN0C71d9LzPP&V_cHox+6RPTJiV0YAqzkoJ=0vS^=QU0U{HW>qjj#PNdGOKh5;ZyZVisZobA4_8$ctieYm72m&NrOp!%1d(o!KNGY}o)9>QuJI3Op`mOmR0%Lm$jDgGQFj5JKxwXv1Hf%tbq7HB1gYHNbRF)uD68Qo$dupp_dGNCrPP4L-<t8*tXyq*p*23cWrNz1NPxtdb{jINwPwldA)mPzewX9%gtaKSO?EhNRw!GhK=CaS*8``jIPN9aB@0L<?Z30+skprES+%34(!n_rL4|*`Pp-anFfVk`fKw#hc(NOvsh_$Jz!pdRoC%~a>t8J9GGz1Lera9o9E>_H8g+U9RRmPzw;E<|m!0mveI^nr++8f%CL@8LoZ4PS*3%U?1KndF=Pd<54O}MxAX7kZ!osV*+h-Re_`bY7nT=?HV3H9H$c{dAwPV?NK(>xPQc#ZTA)5_-N%z|gk$Cira)2uYQ32{bA+kVdd4B}@&UoFn!#H8PEai%|?mBH7jz$T`@?E24O)|CNS6f=^QBDPG1#E*VI>2s-iH2VEjye70#)WwADXG9rPvUCy@Ih<f)&-{Lscy^!E?~lJadJf^|ZWA#*ryU=gRrXgzOv_*M*cpCN#FUh8a~;z-ikMornPfAAq47yR4v7{{w_Vk}GZ9nQ)xe`2CJ|FL(&5SX6Kj2@j_J;s35yg-O|3CUdTnY)DVS<!aeMV_S1MgRsB-8+!PHnMv1(34O!s`kWMW&$m;NuV3`*sO3VY7c590bS9*)aZ_arRg^m}siH?nkrc?EyL*qsV5uD~DGhfAu9!vzDkXE<MCszyR{OgS_&zLOPuAMpG$fR4#ccCB5a=pk81@2iW(3~oxO!PrVfPIlJZ#x;9p#lnm&G?BgFF+d8dmp@g#{|EEAz}nQ1`l@ag#b~Js1A9cgv)<@#oCxI)Yfx9g7F^@4B|7zPrQHF~=u-mbKQ=WJNo&6nJJarroyk{rruIXzGeOQsh<e4X6BR^K7<-YLDFx$?_eQ#M*54*)XyigB$IB&Nrrn&BiFdbXjO3&{qeEV#nLh2bN`J5Rxcmz*#ivoE_oQ{?)|RB`zPU8NxNC-XF~!Q$@2d4#OJqbK^H6mIn4PhNuCF}v90v9(F6Llb%FXIOm4dLHSrQc$qRJCy(b*^|;7y=F1aP%_7A*tWM-yj>ri~XYimR;V_9BWh4`=Jd_r)DZ5QbK@AV0?4%u>fndanqMR8hp<W2Sd?rl&N0k+&3!;qBE>=<CUG3yoLne0FKAMgVE1I1@=&B+gS+NgV^>DAh>>BdO+Q6KQV;yYY#x-;Z=<exV>xH6q3r%G-+Y%)Uz+7*+GZ*Vw=^68VI4z8Z8BG7xD?ti2)5w35^$MjBKePbt;nMzTvPD7QF!=&BFa8yQEK-2%*MEc@^AAh>EXOVfT)XYgSW+lWrHqsog0_T#PN|Na&I|FO{jucP|fQ}K$He*N`zgg^eTuS4+)`hNxezyA6P`hNxe|6cZZ{VVSO6XE_p+|Lh#^>@jSh<_w+rsK~M|K3fxE5U30&Y7qn@dm<SXHla|E;146#H|bln6%|go&?EDMlYd7pStLc_<KZMk8J=`4}e%-D?DAW^?46~^X@_$Kw2RF=lFY*3Youy8uaYoiAbp)u*8m^{MDWO8t30t!OGsBwGeP#h3OXXnolPZd2E3DWkbUFUG~9XC!bLMYIR_)4yQ>(P$gp?o?0x<Q1z$n0n=SDZ`GZ(UTC0}eFC~>yPaIGzotS@uK%<{VA&qP+`W1^(s;n7BklIxS?9p)ov9&Y-YVcn6yNk{>_~U@5ibrH$KTb?2Yr`)i+yz*QRzuqx2-8*M$|Loc>KJJz*YSH2udCS(9iS_xHIhgh?PIb&AYh#wRb1b{}bH&>96VfU+ZV57uQ-8{OqzX^a+I6Tmgc|XYVDv&;v03^}?mjUYs9xa+?<$2~LM%e%bjsK>US4NEfj0Zid|-r^k64z{xwOX!tNe=dbk}jPJO!@4fcmPCEzAZpx2O_T*G2_a2`+^VE$H+<EgrUHF%;`FylbnjcPv!kg}OmGxK-+JzDGm)|+BS1d{#mm3UD^6vkJ5f^>ohA*EL1AHPD;2SRQtWFkKgg{ITHc$v67DK+xlw@B6p?HX4piEz6bt`r(<{t@IBcgBsE31iUqx`sXab<{n6<u=h9oQ#P?%ZaN>L(Pz3BTaJ2X~1Bx#3^}MMHMoMB5EAx!{L28EMx76nH`TSthYkZx%EkHw^q@Y{}*+nUC_3Ms>iM=<=*q6wC>#r6B&gp4Wa@6KV+MY&=}hOtw^2&V>1Bf{;!=4o;#ALUcCuE8?irj6t)LtJJ#=&cvWt_3F!K);cZ8&Fj-IPq6)G-Ea7&^ZBPi7X?&DOXF}4V@}nPbRbV!Tw&t|cd4u_=)wV1hjT135WJ2cPu$myFS*qnVPaBqJ4#2v{Amhky1ZgX;HomTLO=&E1{MnO6$2g}Mb_+q^oWA|3Pp8S?x1OT25_l{t%njvSw?%oP+dB#Q1;K+gNU4e?MQ%~k7CXY5-rareB+6+;5$3Wg51UO+(`L$bkb<dcR<vv1uACmXgQrgYS92<QG!Qg1B>Yo-zu#6eG&baKfCw_qHx(!xAMM<6bDl#z{G_*2S5f7B++jlqk2BJV7`xmq_GG7`XrG$J_Jzjo8Au4Yy%WIBa})=Ec<<0jrL7>6N;?yv1;-J6G!~^6TV`glh!_B3T}9Y^yox2yAp2a0nttw-_Jz4yc3<LfHb%^Dd6Ez|Cy;5WJ@q1gu&zf5&J_wb%gMzXzZj2%Z(XL61~sK=g#j*LW<5JOjL=U@_6n8iEkeC$Tf<L^CFuwx}C9_QZC1fR=xAQKz-2;;QJKRgMyQY=`!yj=C-n~SX7h&zUjf2m?Rj0J;j<r`n?d0+)S#VdpUmf0M9M)O7p=QL|TaUshaE6ukCA(NML_S*cj3_hq!+9WwPi`iJ?#P05bk$Gsw#r0x+}jsXk8>bQ=h>3o&o%w!b}rNx!^^39Epx_Bu%K1U<Tb2k2<LH_+(ncF<^=Ax7JUMs!Ds(FImCgKHOt0*zl+@S%(eg~4MZ!YMeEmyMeQ?!BJ@KRtn50fd1S`zhe3H!#2%@Du3z!62W0gnWvkyb1T`!f44dEWkqCN6IA;a4h_>9`B5GI{h~{gR5rfzH8vB{j+Tu48z#l^B&-;6T<M9rSEcu=XUWjzDnA$!Jk2_f&tV;lR#f#0kkS3+e^Ta^XOa#FB{fMeDfxQm-x`U^kRcVc1#8@8#u(o7V`{i1#CQNp~vUkf?eE^U*L@M_6n{yd|IH@UwCI+?||0Ri=96)U&ZyVgzF{jCA*iPy=A*zOFPsHRZf7f(7nFlqwCnVQfC%7kurE<qX+iXut=Sudueqmz}MOxIy}iV3Lb#P6UT4rR4OZj0AJvBtYv{BPI%(=`Dl)Kzl8aghrEmM3CnalU>hM26_P`Kc5ni5c)7LN1Q{%YcsCt}Z9)VQ-91fPS*U;99$LBC@7=b~H<0?ijQ71G*mr&U!~jvsPMWVN*|VC-2Gm_(g7XrPwss^Ojm0yxkfO0CZ*bc+>G08Fj6HgbCMlwIwK=cEZ6C{4ziaU|;G{2`Vpp$u1$VVPoK;)Z49j9`snJ$0sdastQ<c<z<$(2g*PMoRH}0jN=LD<@+j3#4Y{k@5`{zEuFl%j;FB~onbAGom?&<MhjGG`4gpN}798{-P$&O(M+8rTs=p{c;raq+w;tty@aPet{Va^%sCa~;l?l~Hy$kbRXVF&=n#*t1db~v}l7+xA?PV_p`)Sf__-C?Ml!DVJgVSG#2Q7vA}l-5tWf9h7g-L4XEe}}Bw+K9=S-LA+NO&Dz6dNE}8{I%&QDNnF9D6}IZ(MVR@vZ-{gr6N#IW@}L5q6HqOZQyNF5HmuV1-$KRsOj~Pf!FsUd)f@-;pS&Sxt&PV+u<FGQs7(KWXCi;)G{(Se;p5o7DYKj!qwuk8**>+<MqsJhixgd0kLGB2PC}3ch+I$dRqL7X>oJd@=a{DqaY=81;0VLQHtng1Tx?g#_qXS$cphBsF9fOi_eWl0JgFOJQ)g>9Tf*z00QA=+1&QQb;RlyR~usR2jW<Rm2dJ401N+Qg(Dlsc+P;T1Z>{P<D>UnuIi0>(pW)H6!j?I_=I=*GT)DEJ$i#v?T#ip5`X75-IZrsSzhvzyASInQ(k~J?$k?8SG{Dcwmo$h<SWN3zH)QXSN7)haN#26p*g$JW1hRq7kuS3`pW&OqueU6s*ZB2%;B9$G0;~&b(GOl_>aGX^4+&wzxPt-8!~s;BMfzMLmDW!!#d;!tr|-Bl@*aT&<re}Z;07$OeIySqg1$q<Zg_OUk%}@<woCx{RZgtfeu2{R-VFP$5j#io<j?Uf_uj{XWuaeI8b%)xWg`5R^tN{YTQPl;Sqr{%pch#{JQu%vE0$d`6tYga-HyiAQ!>)ESiAGh<)Mq{l=}rLo}7o*)>&HC0)}oO)=Bm=<-$34fqIapCx#O86T0SW7}}Gbaf51^t$Qou@%Tu)12);t*8M^K21bg5K=~<&(6^5@YSHrmHjemu6whXMhDPo>SHYDA}vUc6<gUWduM$b57hc30SH;iT5J$^EHAd8FjI#$C3OXIFUOb33d!DZoOk+c7C|92TY5(k9z41`>HS=c3;!ASTfX^O^nPM{qrHU=@*M>p(7KYOeBgfqYQpP-3pHJt_GMEO@mk8Ogrp&yUL1dTREAcOC50Te*s$9mxdlvgh!!<TO49ocrb&5!AQ1qRs*frfVt-Li=23<Po^zrHfu#afU3AK+IG+^N5kfy6jL&|?9OdeOPPGK&eDS3%VBYZpiuD~Hk=EH#@u-}6RRwP_3y$h}QO7nD%bC4X(MW&F{@m|1m#be`zU6=ZG3m!WPp}j(g3%A9ywvv*il12{aCS#aPB2Q(kc=8soMzU_FS?x?Dtj%3=;3I0BKb>|awCdE0Wp?J&XhE?+ORc*hbmAXoZ|DAMFUB7NY7A;%$dq0QDxW$mTi}xZG^hcrEyW%=wk=xf6DzP=FVDOP{lg!Ah3|N-ySJ}Li&h@C#FP`BxA9Et(dTld+q{E8Xk@&_pzfo)36Wh#|&C6D>#^8+fq_Hxu5I;rkEOTq@IREEe3Df!EYTncOVGs-IK~*E6Jjh%>uDT3EHSnnA}4uMl1#<k~S>%i3N%;e9MC|nLEmcU@r~Wts>q*qb%OEwiwMdHsCoqfojo=1dd2$cbF8-S;Ua5A;Bh-_|QalS`kU#izI9<{r_I<$_G(U`P3oYwimFWcBPF#4X@)yz})D@vT=1U5Mzv+?FfCK&=Z<mZAYL2cILylydzYW6Ih45+!V-cBITQ&`$A`pZ6LbfzJN*hHE#`M%OGdQjS`aUPrE_<&O1v;Ui0M2JKNLjT^v;;{gt_So~<ZGq_tT&>arJ?W$S0z;Y{K<?l?0!$>P<8DS;;~$y_EY6s|1o&pEh`H6z@)nJyY?KETQ}ro4_B-EtO(nW7}6Mf=vXjEF#VMbB<+x{}VQa>Q5|*k~J_<%Rh^D-M=$!EFv<t?-3~-E|p<wKt!?%%+;#TZ46MO8Bpha3o}Z=G*<XkK9nbZEj2W-|}EzO8cMoRFjUTr3+x>NuHh6e9kdk@2~bK&J|Bt&tKx9Y_Z1v(w(IJkxs<bDpp%*Pmz37dGcfaKh>?I_FAWTuQmL5oa&^}`r)+5GwmP`x9uRCPrHNs%2dOBa>Gw^9$8q6%5bqhtUDK{JsnWQ4l2LGy0HYb4gQIBTfDhbhM&6ch@5%wgI89vc=1mHMM6tnd@PuxM-VXhM`wl|J`1X`tpCzxQ7xM;y+;6iu+zel@8zN3dGc4`5-gs_zhXPWBTGi!q*2QxNm&YAgp>rU7w<{@0f*_0F*KB~5I&^mk-Y$blyr|hGl0&^fbKX2q_rEFf5baGF4hK_{#?6o@%oS4nyh%^@;$LCcdq{eUIuj-U3_$6?9?T6M<f{tQY5`3%l3x{;UKX*1~#ylZ9i9TlL$Rpf-muZxX?AHW7?2r5!+NWTTnKudznp~XRRRVLCl8uqWuxO8H9Sv+&)UHR(Szh-3ROPX4xFo@*HD-Q2#Z(QqrpACw${-ABpijoAG}LdVnle<e#7E0Sf2R*J1M<<u(oXX=u1Nk}ab6%!*gj7sU~Ehg|@5$s0Z=<rye=8;~InkGk-3*gc&}Vpwq4y3C65DMe09XhdLJl;K(*@nF{k$Ka01i`70r%{LJOLnc(;pda3?kCB{OvG^$E`d20R-Z3fmg!^uGPQI~_qH75j{_Ph95r>e5Hsy8PKNhbQR=L~64)Jj6v7F-2A@GkBH4WbWp>Ll(_Q461O9n#nq!!avzKF<ia?nsya7XtX2|o%3wnB>qit5ci6<O&i0siMf<p?qhkdZF)gOJV)G9zL{WG1lOiadH2(^sTuNwqa9$&bxb&%E#wx$=i4g#s?vPsBxKg_M&}=|0tCoC#1%@{pWi-rD~C_=2j<&Qh<D>G%-pr8+7XvKrh4lTjvo%G}+kfTOYoR2GR4M%7c%d`2!rUu7L#y?9X+fGDAI9%ux*@dD}%>a*j?mp`lLPk~O70!+t`m(gfEji!<jKx8aK7tL<L+s|n8#NG+B@2boK=RZ*)jj{dWWkQb^#m=<??yk~zL@_BPzph1QU7b)r+4%FX_&4S5cfvn%V)6{DFmrCOmsfI(&Q-og)-4bMdQzFz>8Z!#jY6o_HelUTG#Own4CEZWnjdWH>EW<uWJC}Xx1<z;Cq4C9F*!`c9Z+9P)`<Z(2i_zS)M3Q6cMHmhO2i@Jh-Azg@}iiZ8T(j*O%gF?gi0xClo}Rvj@16aPo(&!bM4)NTVuqzE}1&=oCHHHE4((cs4<~DyYZ&F=<Q&6B(k`K%BeD{PjI6LR~w!}b1q2C(HEsgoXA7e@xpxjl2yY%Sf))8B#=rb&yVQ6{rTcb3_nLB^@b+lK|IM^MvmCe(X;5`wB>t(XgROT!YVF?A_8D?;5o3opua|fcUvn0X}W30L?Wma;Wx!h%iH&a)`%#KR7Z&CBlb8f;to%vr&HC?iS#`rr&r?Y=Ej7`LZ$G8;&x{CB8!MDhc-KL*m%->kwFjbDlNHpGv``jcE}UQ3h`c&wtCC($JDY$-Ga8Z<<{OdKwblfsLTNk2L7+7RcoA)`Z<Is0?kH2kSjfF6dsAKNr_11Y?IlhH2!NqUfx7DJ(aWm`p2lfsQ&oXYcHtJE^06SV(kTNux6DOwHMMJZYCOJ*Je~s!o2oE7{kcJtn6UNDx_6lI+R~REx$ygTn>I?Tx$mjl{e5B#=y7mvIOSv3}I5Ox}-~0m#C`Cs+L^XyrZg1SVrdlU%$1ceg>=06>M{gsb9gbnK1PovSKSPjBI3ijxmbQYXF6|#H9-1fQgu0A1NnJZ~|4JwG6yg6xR<z1>Ai@#61sN>98n_6;hSG;VONmmy}M<BP5)juyO=092(fiGC4{JxYqGHr|y?k)NOX3%LICzM1U!KEvKX0{&wv(O3D;!6Nwp~dY|E`+pWdL^~8!B;6L9pak!1X@5J$j>U3hxr$aF7`pUGge~J;yDIcRB?$r;+tnJ@%w{eeQl~&kK+KJQYCDf%vk1VNX-bxw29440QK3>hhls!~!nASL1NxYI95prS5U`e4se7woTuDfbB6)>wCAgk{$g~rlv<YVQzQf1|ppHf!WI+-(4=H0%!9z3l<>mrK<NZfgWvKU#K4`S}4ya1J1tF%JpTjvxQ#QRkXM}b|m=1s`&XeUfaurZm)I9J|}2!`r$h{Txhw?;NL5s-62^)+RjMc>t+8cV+FvPZzPFl8w#aq6G>P|_98=X9>@iW;Ih(3y2kdpZ}qiTTOlr>s7vH}TiqNG$q;o8iXS%+q}0vqfZ?eI%o^j8x;ZUmB@o9yv-L4XRINBkcV|s|PP(6D<Q9O<6=K$vnC2GjV|+@p_z`Y^KD8HXwM-M$ArF7&99Eh#Ez@7bX2p$^y}~6CN3lrG&IyuhI!tDCc+>s-OTYV^_Wbe{H7etolE#SQ()$%6gtwOpUN*38ocFr=E2pP5(}$q>24Rlt91++svQ@Lln`mMsiF&Dm`_yeqTE7(WW8&DG&IevpJY;4g$dk?2xyHm5(v?{)GE2<YXJpJ52sNK<YEt{W<A2Ec@(XAgJ7vo*t0@V2v%U6S67+*-9qfjz~5jX-Eh_TY1ULaP~vEQ=XTZzY>6bQNd2->2wVAtVe)-xo`)Q8@lko2NI#Apk5ew{s;A%Xmo*qgJcZ6UXSh_OE8oPch4MGLc)K~il!9pgo+dT0nx75J>TG9mgey$IfU`38f}92k#$PUpyJ}EL$P=Gx<Rz*>Np|aY%?I+erPP>6B5N5Wy-Jr`G>4Byx3XLPI?Y6w-wNOgyniZ<7~C!f@1Ej!+^~TN423~Syo6Fx(PaGwWEuKtx*}MD)>QKY9EJ}I9s#z8FsQMoCpjKjj$B}TSzI@)-aY5HcQUdj-bl>Yb3zSB0}?NiwJLSXKVFjYYjED!B&$lyH4kco@OQ@5|oM;1Ro{+N#}=h6wl5wk2JZMSdmhoKk8?OBh4vU8)qm8IZ#o#9=Rm4<Y%m%mSmex$w?oL7%>SuREpIZp(-HDoT{-J8qciO*k0;QFVd=>tsJYGQJV9s#__5M%8<h{Olh4;1j2&Bn2U+E%XQIk94v<-A1Zotpn6$Wzu-%?G?pU1dJRFch|)U=UL3f=u%q<0Mha9qV=Ws;+uDihYlt7`BRpOkmAdrK-3e1_n%u62)_-i{wb$ofST_xI_c52zKfkEOeII_7+9=bV8(IhiF~&(xG%GO9cV0mpVn71-GE?v2&8+^Gf#WO7izy+i)I9-o0lO7ch@)#h==h^*6{?{#kIJdER&sTVKy|3+0g&Vl6HqauKxIdLX%Aq{mLK0$>Cv*y6&tFDtZfV0T^k(GS<fh)>^&SVZzR38)%x)x#ST$vNf#Cv$H^1O_XZ@))ieX!I0|Dvmh15{PL>Z~DKZmV9scI~blbfz)`vXiUk~Un%)sJjpg-}Cr%NInt<ucRy8_4kMG=m;RD_|I?3oCt=!{W+FO7Oy=a_O;chv9>WO?)^+;ytFr#=Fb1vSoq=FO}r6Qh<)SocC}roU9LXQ%++#>~_XpVrj=l~+RLSL)waV%pbVUq|?LgkMMam09_fS^1S&`Nz&Z^RMK}ujI<F<jOzx<jS}IB&q88o2kBNK0d{=pMTK)os%nv8M$&ZCs$S<t2fkDR)G_DVt~>ZO}kn=%8><8ktm0W0aw#fG-3<Z-grjkdrqI6E3>KhOVZ-SKWD_im`<UaNSe>7b}teqzXOkQ5_#={MET^7kU$zP-o@FK&xw#T!StI-*a!v8IFbsV4C(yWT1T8;cBt45H_;x?M`KBr%oO_Kg3qXtE0^$dOv&D0-niy;?P@2QWPkC189}n258AEl$V-CiD;&xC)HQ-+qd;cEpEdF8ru_I%QgZe68D;W}c=aOZ>+MX*TIRR#2jB8n_w27Xo%sqwu%EH#PM3Y1VE8@n$iM#wuP`Ww({nycgnW(M_cC*EIA!yFp4<4G5&5QH>&Z_Dk6)le_E+hUU3~VzUHQ{9^ZcAH`j$Z+sh8`WhLP&{+OUL6BXg1M_%i?T^fN4z;{UOgZA5r{Bb4F(O3h~HjjH7wt|zQsB;#SI(C2ie!hA3|2g}GJyj4@0H<C2r82p4|7}o55MWq(V4dECzgxMO70d!R;%(Sz{$h4^quxiB)>Qswe$8PsvjgcGN2s>n#5F~VO?kk$1axWYRnL@c+WHJ*aBD<?ANDh3$D^OaMVeERNuLWBUt9|A5=iv$g;(!f4*P^RRDf=}`DaP9TQA#O)Y(ejK5sH0=^L&9t4~Vf78l0$l0s&W?bW5tYa(rA@D0UZ{cFFeEk{Q?#*h0LqCb%=Iw+ti<%eEcqe+j%U*SS&y=Zej44WJTbX7^>Xkc_*hbah&z`uad~o7Tj?w{$WhkT!jJn0sRT*CL0ehpL8V#%<tIIir9JfbNA|tQ30x<nQJ&j^qIE#Uzmk{G!j?aOngaZ}cC4BX30l8IQdrXX5-gL4n&|fljYi*XKs8g&h7e#zzeBY6#tiVk6NtO}OK@riw+M#+AKH>w4D^DjvBA|LBJw$a5~jOM`cvi_mTeCHZmKNJ_|ugYq+qxEwQJOpa`Zq_1aV)<^a7lws>YPR+&-a9*+bw4CQ4UdL(Vl4j&$<S^H9?V9U#<XTS-L=E0=f5^dWym2{Rn23JwBYCKKjee|yFZdEL9VxyN^EfH7y*BNvzCSMik!+T;6Z=4lZAK4rsDB!XA9YM-WgpX&1cxA6U4v*7w<?fe2!jq@msyKT-OWiL%TRW+FRk%J04HLZ$`w=T-Ij7M*eh;egPiehf-^8yDQV5P$~5Q3Kw6KtNyZhKD_11!?LYE?7sGrdbeERFeSJ`;3jlW7x?gRR2GTGKt=Y{s>EL#eyDu)z4N;qhd)nG|u>*~dJC>mpS?1oYo3P)z)r-4C2aa|;=f)kr<Nl+s#9Y%*Lm*!Rc`nf`VzcM8ZyMhV0N=!XHs=k^5}=MgVYvHpfbsgJiA0uY7Pwk5n;tlL`o$EDktGYJCcME*=%EnJLehz11kvFIREZ$qjW-SR5xOlx!;YQJfMI$|l$dmRV=(R{*1|;CY)57Zew{QbgihM9O*e|O1~6R!MmuIL<V-czH82s@h%1fVzvP<Fwdue`>n^W<0@E27FhP{j3I><ldVK+}vVevHVmU%q46l-eS82gKs_Ur~3=HP~SDQ6G9M!LD)^xPav(0jvH33@b7iLY1hhvU)q)<rb$*#DZH4Pa=BF$BMI%|B{EL%JWYC9|@PBVi+wIo!PSKUO;os)@^g%`#Jfa54#m^GYk?0?5|K=&Boy_h=!UM;B5JgLy4wMgI=NN031eUx)cq#>8Dk2Zv{M>Ef9j_5s$Mvr|{<>R|?`gEK=?Mu_Ar$?S_2DQd<1Q9Ca!CJoaF%eJIcn>~&`!*Kl7EFN`CL_DdXoRA8KI0sdM|KAFyS~iZ+JN%}A>Is)x9ilY&G2c|HR!l!IcdCA1b(XI2TTyQEeNYpl{RQZaMT&SRt$BbCF9l_=qVY@j*V<tdUpZ6BjNx-M=0^;p4$x?nbfkHEZ<2EtvF(GjX+ELln+M47zk2dgIH&1X@JQ{Q7%jb`f8&r@0IJ`vd4*@8|DbON?LNZoU~E?SX-#Hv{31ag$lAz?WuXn?_r+O%r^0}++0Msc)>h{6Z7PP|C%k--P}U$F_gLTpRBAh;r;(<vu4Mk_<)Rj=d%VrDWI>#L1+?Z&GRVTUOXh6HQ>DSIiCV`cOy`@TTYn^?3{jvoQ3Yu1k`Qt2wS=v?P#7DAgRw<YADvBjx|5S>XN)58(QC~FSJrUi~RcxuFG~dU)M^q4of0-)e{p&E@;5Pa}#>P(zA7)GGag$tF{JAjL<;rwpGmo$`KW@n@7Yho5=;yKLm?Ff@WEde)=-)?o~f#FF={IpKH2>6LS_rS^#+WpBBLTU%lt{_f6mZJUh;euYoNxoV-~+=u&f|{M9CJFiQM+K*N@o*qpY-#9}$-f)3r(bHxTUu}DgGg&SFk@w*y)vT@7QSy+>#d&Sh~W~S`Y26R&Pwb>%mZz;>D7qeRgpB`I<qsZ~N)#Bu0@XA4q@Fb6`F#c}G*A2wST2XeBWgKJ5!gOL=H3j0Fv4Z&OE-?~F?Edy7#VpI@5NExWXxPKj)Lxdjm$l>kDj&xkiD++;()<LI>$l#gtq&{7rK44mL*&d_xwhp-&1r?rqh~)i<p9X~gt*s3kpR;wf=Qk2m_0`&0mDD$jXLr=G|pFY4E%|$c`lf&3$sTZ_60EQAcJEa-z^EaK+hGZKH#mH&PPoUF@CTmFoDi!L;DqB>$vGiC&pU|xJ<x1Y7lxqG7x}vsvH){9@C<gK60uCV>YclW^~_}WMYHUj@kF}!E$`QQ{Ot4#W6`3#`tVOYR`ArlZKXuvI8~AXerb;)s<@)7$C9Z9w~@_`JJV_Xr<GMPQme#Jb~(?45KcZHZt|Zvh8N3oL1O=-2=Lnd5d$q2I_S4aa3*%$#j5Itc_Y232<@d+M{Qo5PhPpg0F!)2+dg>`8`Q6+s>nN5UMfTErzi<yKF<pnkn7Rh}cCl4LgpHx8zrIwY`2u7z;K}P@~b=U4=Ucr&xE$Moogzh$o9vz8NMl0`!csGkJ7yx4-EBA_*>N>dGl00hrLmjucLG-}3HTpaZ4YQHQ1Y3nBg8T`a!CKn{d~Nx*@Sjq=XGTw&Kh&1F;OS&HDcW1?HLpiGCK8m9x7rPg+tVa5G^yZ3p`X9H;w`c+LFI8;C5-B06^RYk{B{azakQR0o}22M#1L-uNF9zys5NKTOYYP~fY7cT>idW{jr=BkDksr(_|ii=Im9*Jj`3ogcA_59%ELyXFDWv=0Y^A7t+=T|}Edn!~pSs%GAlP*q!VXT!kB5SI(5(ybqr`Q|Xh;ZL5S4+pbV?nZ|m1L;mMCpj|JxN+jl%PRVyWtB>s9hC7!M*_|fFMSX$X)L(our0E1y4KM8F5yuEEUO84%jsPIwS}Nu#23T*7R1fUW?0+n&XPqi85i)h}Xs+(Tg|sQg%uG470R!;aJCngO+|&>?0^yjHJ<Xo`|ieS2umY*Oy!SUO)#uO`g-^V^?IjX98<qJS^kxAVG~IF&E_u-g<gi5%*Y(!rMyQvtip{aeLodH#!>|&4lrbz7CuC>)`CUnINnA#*7`S1ks;Ib(}K#$DX(%olMzebCn*}nkx}M%q2u9C3ZsMi82RzY2WHFmcFUsLq@F1gvh^wWoe_-x?1E=WFkueIUUvppTgQz#K)*3NmC)R9Xj)UZI=z}xq-CmVml2+RHkAsW@EWkh`NyfiVBwWmDrq~W*m{x$gGTe1$&`&^9E(4xptV1h&2_309D<>L6%ev)%<o(_0=SxR>RT_<tw6kk{RU|Bh>v%@62s|g)#7y+j?Hq&zcU5vnC5jTF8^q7x<<u<752CV=_QqvK)<|Ztm(IcVM;7aYkv~!B2rdO+UDJ!)EL#N|N{tRdJUhZ%1(wqg7JQAdIX(U{L8fEmv%_wy=KAWZjU{Dp{7NoaC-pk(G9N(1z~mttxi!sCg%Sy-bt0qNnTkH)vJ<dmkgMb5?I_5Hi*<C!ey&NOzd7*er`I{+OOTTIZP^<BYkK*`bKol-VIs#cA!KJj@mgxk;B&$hEz`AteW)4x}!Va#Gn4n4sAxxucM(UuJe(3`;2*mLI^tHBTG&V|r*LN%f@2oz)u#G4y7fXP3w;)6eDtgE%8gTk2&@;WfRy85M=a)?=}uoNHr}yxdm)ldo%zV47T=BirjbM3^0!Io;Xp=sIJ>n@X`?x46oQl!Eweqq2XduaYjSDV&I$zAUj4CW#e8_olC?qkyn$L0#f&OZD*@1$qx;182>d%1T>yOp`eu41}syff%Y*>Dq_yd^N4ojz*!qq*dDZZFo_uv}R1!Vt6&J(tM&-+DWLCsgpFL!zcSk*P4&02Rjy_x<t~CG?y!-)IpgYO=ZFF$ODe~NTQnZsj_dkV-G!cgcW0-b;ps5UedU8-O_Y|tfL-yx;Nd@{!oQ&8I*6=Q@S6l8hhpX=PIShtu&f|he%2*YL)&wACjUJNs8ExwXcoHyPXQXY2+vEVcr{WP^WZ{!4L`f$_^uU;##3_=*RRoza<WaR5;Q<lb=TtO3nwexi>a1U}`r6QKl^fsSqxwa4_5uuen97p4zDJ{PaFR`u3kCFG8@tN<S=CA!1f_q()~A0Xt*PjC2)=4iyvgco=<<NcL5Uq6KmdCo$z#KP(xcEo&sHq6v(S_`DH;g#j*w5=l3HbP&m^Ql`SH{59&U`KI$D@|=6mD#^*jXS@I4MM87^8`i1msCjh24qtW(N%@p*uZhd%hn3BR_MQiD`|bQv--|Fw;%X+Yv_Q<7o_r>ikGRhF+)M@Yj7Df|lrdRiw&aFY*0XGbTVpjfy7N#^#o=~Liwh$wTqr_baj<4cNT=A=M^x42WrWo(6UC=qPdh3Z1xnj9st`AK63?-9farM9cObGzUVe%fDOxox%Y#R5^dQ<FezpF}W)j2;t-e~ZBO{1r<VH`L21d5d5Z`VgjTeTTo^cBC{BUz<e7PI)Q69Jgewuak{6BtOdQ5Z2VRf1%>za|H#n{Wt5M1MEQO&S9tNyUG-<h3VmVOwY<XORxVob2ri-I9?=wcn5>OPbE;2=0M(`F-A<s{EW(p^r*oxGA1n7p8Mn_&_j1pF;4IjQtxx=V5#BJvR?mO{xc?w*SZ;l%ftmAsdzU-2)aYkJ9u!Hr(0uxaOjFDu;ii^2_wgp#WSO)8DaQ&4VQO4%PPz5Y8tHW^v&Yc(mGPLi^6(;7H=>2hk;tt*3?96`Ar<vcYzivz|4t&nrry4uM@NoP4)q}Muis)f5;XV!|D+76oq^Q|*oZ-+H^o~)gdI`96J`=w&Hi*1kTTQH|ki}@VC21QzLn4|g*GH_qw2~(uwJ{q}SS+b7;bm&V$cr<5$BHL(4=(et>|D^ppqc(*=VCAUX_fR1U3@8RQM?GSd62Bb`W%_8=3Z%={M+ai-`C)9%jQ(CeGkp^<ctXS^+-qNDS$}HwgV7H6R{F&?L?&YI-2qf#B>TTtx!<@aiQ7dLuHjsUxK26jsMred@_dhRc)<S4TT_W7@B$2SMh~l;^B?-ERN9A|d9;<8Z7PE{doXhE5myJx_JGjuj_laMmHng}<a^`&^5_orPvz^@hfvn`in-(aTt0<2F{{gH9lS!W^6>XN7@cFT^wWbl)x+b;4UHe(FkbktUzwa<nVeoZT3&yB9pTpzejVXgCa3rRHN4U|z0x?n(m1`+IK9$1ebj+{<#2lCaQX@yPR@iPu5dURSU%3KfyIAlCd36h5piqp$>B6yC2$Ja%~^a%y-xgVy1?{vJBO1c37?^H>MP5RUobh%xsF6ZRLPup88dn$mR{;Hm9J>J;967;!-Dsy+?u$ZoY;m$h~gJSP!lDRcOx&<>Gd~kT$$Z<n6pxi#7^0Woh&7L>H1G@dE#~wA^${A<ws(tN|<Dsz9<s)CB2h)q2@nlFJ>f9aeAyom<4}E;N<4yRo<O{@Qe<sp8q1lQydwd@Qv6akQnuBH$z2gWOZ6lI)zh8r_200!Hv8%S1Fys3zSaJFdm)$wRs16C&QON&*~K2C8nR?!mVUZ=fB>_P<48z^;f&9XNa9H{54pu<{Gh6dw~Gy<fhIKU^C;@V@7hLkzHv)K@=~LJSp7Juk|DBkF4xR;|uR!ri>cjdGSUT2gC~p)L+B3PrX2kHI7Mi*NC9z;}$OQLX8KUl5EB446{)RV+LS8bSI+}ygMPy5{Xy6jOEWT`#Jtw)a(BIN0#dZBCl1M0k^y5W`<K`!<*!pRwu1Jz9RGsan4L}P9ER`OQfSLXC|aq8ZT13%wF1_r&63FBBCmAhS^6<mR9N;VJ5#h7}O!eeiYvHv#%qB5F53Wf1lOcG)4?S-IgB*TTDBuZmx+OX6qG3=^u4}!8b?0`w{Qpjo*8}AL`?3SkN!4{0E-MA>08fDe5cWi~i0HEIM~YOm10&dQgGujam`H7Z3QjByRV`19*dCWVzj~3&*SqZW_YaPys;F;DkoOc@E_owiFNq;f%h^`X#?z{`Ba??(oGuVA^F~JU##}IXF!UeB<f}$&rRwseL{E@c<m}UQK$zjs$eAfwX3PLN~(U*W7RTX6N%yR6tZFUgU|j<NJ!3;rcpoe&-HQD4=Hs3Qv{)txa+aXXs(+(oQdkaccM&HpWkxRM%`>-q8F@S(9xyeHonA8D|3tA`fcES%J%@4931Pyx?qxHL-Deq`?)GB$mrt0WQUp^Z1m8UAZR-c}5{ifCAXce?XV#D2f%gEX1)>Bi4Q(Fkua-I0CjpGL_uf+4N4PvT=k=I^8zB8B|0C_X7}g?2G`ul1*#ngXQ?WVTtrk(g2dX%_{rl&A<9S{dZe7Af01VR$d6jQ(3)4edP{!ux(Y?tw;eO!q0&zJ60S6x$7jT>Z^nh(2%37o}rixs@P%k$)ux$KxQ*n)|)kSdTT;9Fv_H?M>Qu>&l2Sl!->A0`r;S()tI-Z;(CO$2svYnbZKIwlV%(2Kug#N+Z-aar-D%!NnGziz_nXMe@29Av*=I%R6U*X58f`W7bvdhtGHg|LMeCcFSbR9C7=v^dn&Zo^`^475!^gip*<o+<hW$Qw^Ts)oJYfg2GM6X)7o=V-klWp!cuWB&K38(wDu&j?v?CdpQWf0rC2vA<<4~Xs?6NjDw-OD=Cj+~1gE{Lx_)YrBHC_J;v?*Bp%t0zO3033!g;3X7wkHP*Ac;oC)V3fo~0!D=HEUsTZV;hpzu1F=IbS_o0}3EfJo_4{hly)iL9HxO5=HTI#>PHP(|yl3C&x0Y}o-HD&?knB<HS`vLW`5-8>+Z0GlNGpVDkJqP@mb-g32h6L}9+Jur;AgfpE%6Zqp^Kb)*ch|E<;SQgl{j^yk`9X;ths|_13x?+@xwc;c8(N^u(yktM9y6T|T^6ToVCMI{Y!0NdrNaq5pl*HzOYo)Pzqa`@kSoPLB+ci~Vm5r0JYOJbl7i>%yZGg#$`&Rjr=={{rWQ`W>DBT^R;SgJPDbN6b2Y?13%nZPai(d0$ZUa^qG*+#vrTbJ({l9VnrS=qI>w2QpfJ3YJ!SB#ZE_1Cs?Kd$!m?|Ua5I(1eUyf;`$SVW6Ws-nuN6YpJvzUqXOw1M&#}BkvdI&mTsOheBh}w^ym`h7<@LdNlJ`Q+n2ZOx<x)`V@IM7*J`3j1A1Ls)2_0}!`r&Z6>irBq9zwzJ<FPAI;;k`d<3ghR1%ZNada~J5CJ<=_Q#|d9omLaySNB9*u=OZ=hj}$5Q-qLt~zxy{SF#qKJ8?x#AqKiMp)*s4=Mz5ip{z1HY{B?OiiO7(ce#2$&XNQ%4Eu!N5gkjssS9%kgC+S?`eT0MdK<tF&IN<o6NOJImW?*ABTb!1Uu^jVc<A>LO#Qi4vJ%{fz+x#VSaK%r0lLq+3>FMa`N+2O~cuE81zssjH<+i_sxHhyw2NF20fYQgpSOub?`Tm!0(8&5_5Nt631&H_kU0E-w46*wOUhKB&YXdTRr1Q#dbQ6Z;*^a#G@+qDfPxsrQChqXG0HXw8SuUVm0A|u7<+Hyfq8HA%bgaA#vZg%vOEqW(o^3EecnZxE*C+_{fA)2O&Ofv;C@6=TccUC?FZ8U<iK?t;ExF24^=#W(IH9O|zH_ZIHJsB`Et}Vf3r1JS*tTY*RcD=RBT|@fd3CNyFt%AXuVu{_Qy3tRaoFWW^IDG2wmdGH*Us6iE|Dw#$+Ga8UqDcboKr%=DJc|B)(VvmUQ{*lk<<N&1fgYGB{oFC!blu9<s+RyrRqg|#3(xU*5;DwM<Hl$m1h#67sg{xS1KNfStSNJGh#<ZrvbfQpnqOg(N8#hZ`>=mOcK)tV@1Q`qnge`vPFye^*slNCLR#gm#u8yAafSIs8;YWzsF`IDEpGaAm|u<dp5?0d$Bp)n~S4<hYe4alXcH_fe`q;6R$yez}=nk+A=sdGN|;&ZS|H3_JiBt`tQd)o!^JrdsnHwjVh3yFL<0<GSK;nCy+gYAS8=<(Gi%{M7-jT-($!#o6F1UEHkSo6?lW|L!w4X(8zKOt{;{xy`ZI7kSdpvMhbF$ftJ_!o!yL=`cHh|VV+a*g7557V|N+dVacDon{hE>bd8yp)YP80D4r@etkJ4?KEOM+P>ut9Sj&0zs_trxdyd3_5e3shT1k2syIk92zbkwG(?FZTMM4S_U+fR?;?wAY{dm28j`Wy3>Y{RU-M}s&bX&2_{#QTbc;856eent0%wxUlDv7n5$kn?9V!{SZBYq?|HXgB-)4dGm2E8Z^W6To0Tk#$(Nn!^JX-#s>wXuM;#eUZ3@WAP=N6{k^@p3iV#YDgDQQ%r|eO;xX#&h^7_iJNgE1Df2Z|-eH-qEkv>R2o?o{eXJLiTyEqJYWQ94$|c$=t$;EK@Ewa(zK)iRLRtY$;4fT4A&y;Y=ro&}}RVfGydS7i?xNQBfzE^tG?;#7Q(0G^%8XD3`h>-6&Znn!u0ad*R2nV!=u3-{DlFg-#4hiZj!asZQ<3@_$OaxNhC1rIRY=86(NXy;zG9B1J0@Cwa8Ea&(L`2Z%wgc@wS#^${vX)8ZtYf3Eo@JfgBpzQG~+Y)p~Q9!qfRj#Z#X7e7OiC3n8baQ>}%l==w6{CkQMx5i^fBPlCFWk2YP>B)XeBm%gjY(<c_s70r7F|PwN{QaIWHgh5a+RxDd$_5ks+FS1lUl-fA#aC=P*MmsLAG2dJFC0+b@S7F9wKAfQOp!fm0(+xyWU%A<Z8#)9tlTh!&)My4d6naobW#LXw!`%ij{?riA9H^hlY8Kd$=_ghg1u?+hj1U@=(HG>;i!PK%mX;ygZ#hp&M_TGLb&x|+sV`MOdyo^E!@F-cW7W`QyYA{t@z?ss&&;;1v_kz7I?$vTl&rSWwP!uv;)J3P${9>$MPs}o@P^?q|x_um7N2%2S)3bLt;p&<>bSNJ&4G|Y#6wr8ImPz-9C?0E7u{|!QtR*(=7K1y4u($wyx)mU<12ntEJ&^EGd}ol-MmHFw$BF+{)W8kXGxSo-J0saq{-xGCF<>_Dug)@9^~YQ?bTY<m6Gaw&$nH1ALpIC&H=_4@ODBmnm3gZSi>D(i>m?#B_X1%VAk1v{5m!be6Gr%dGBds|yPQqpN{etH!aOoKI-qpIt3Es6tnVP(|1>&+-P#V-t0QEKSn89y87xEvJYA=$?+U4r_UvOm-oZScy8zTQ@Wl5q7B?3Faud#fk7X!T&$-fPsUCIm^$!<(hfRsr^7!*2IQgVYCvH8$1A!(OagM_Lge$QWIh78Ds8)GR3|}DnL|W8XP93`7NNFAk?SxqHwlB8)gS<8Nane3SO*(jcPk`HrIcRDj7U@JF=$w%Iq+PIZe1L`&YD*K<&b{Qb<dt4wNUE49g#_8uFLi@A&W;Ga(OdtAd5Pk5kS62T@e}^mziAIWa6^mTD9WmL2QCDAyG=P#c3f4l5eKGGiKsGv&^T;avgVNGOt;+EHaHt5;mOMvGNz#A=<zK0CM)I<I2!0`MjRovs$&gY~{QNi1Ee+8P@)*a8l<?NV_t!c$K#ja&<=gFEBh1({aDqrl#@radoj9+^S%Do^VjoT~BW{5BR|;ZnhcL=FK=v1n{7euIu&_^_VD=v=<*BPn@<XL*&oQ;RuLSr$nWw=P3hwq~|_M?Z8pKW(!3$rz)tEPyO+S7SGW8?y8L|Gi2N@fmY2GUIK^L#@)UND>k8DJX4aJb7lqQmuRVv;Pd9R<%_qw79B&w6ca}1Xo;po53nnc-+Zo61U=L!zSa5Hlv;y8XbH4b>!vfSs_VccO;ik?o?J`WjR?=mW!~`u4$G{KWCL9`<0l<VB8bleo6|FE5li7t&GW0-sM;i@^*%@;aT-frcJNiSZ^^*6g{@8#0cT2u>;)u5z&+?a*6(Xs>z{VADo^BkDvaV*RLuI2CMKYP?3GZE@`@faaiJ1^<sI0-<3|zA8JisZSQmjIBx1vukhS@ryNEN_yaF~s|{P2FuQ&?md;pxRwcse>3Cz%b3V>$kF2D5W5SHx|8pxH3W}d8ixI_h`kzdBZe(fWRicY>MkFyBtDD2S13^QbBNl9$!)5<a1?sHK;z5ff(j6L(;KbPtI8#%3R4gaYSd}|jV68aSfKwHDv9fq2jp}nSX-{58XVafoB|???gi73k)5Nl313XR~P;&Z|?8!u{lG@2-B)pck2oJ{XVLZT9;skHvr<#DG9nN9mJc%rMj<aAY<xYzrRJvoYN8r!DLKjn?!h}8NDYI(2X}Y{nYsU4vbe-eUks)UFK24+QQ=NvhFKWcoqit)({bEaJ{w-R9sg68C_X=-^ZSrs8czN~bXo<%qLZE>Ezi#LLi4BNnFHd$*O%X(>a$r*{%>oh{aXlXo9RSs-+s@{K?uI0Hb;>7h#7UH<D1!*uMFMGV5KN6Je{5Vq^V=oSMyFzwfDOtj8123Iq;U*6hlmgMHkV_a-4kJl_HMxdrRU;if2xOxE2ycA)Iws3rpPX-n;1X@)eOeN?P8q%WWUbnLTKph3Pt4Nr;Dufcf9dXKQg=WaalBRnpSofvFi3#0-;c~J|!Gb=h0+KPKMepW;}izjk?jtnjSEOhEX@ouixf?uVYy6G>Fe_@i@lw*YAyXozpG!q*H1uN8RT>+|x(@<_qCm32`!wz7aDH3^S7log3a~H7eo#@<bjpreQOPcoi08OB=ol*1ZF3RRZc3zD9$ZHR$w3JKo&WArT#l@_!|)LgYc8#92;4sjspW+CJ#fMeY<^f%^y2+8ReKj|A$VDnYcUD&6xbHB8v|w0FtR{31}jV??)HK#+)u<~uZ<5iFZO(OG>T?!!H5FyyYnx1uf@Lc0~=6(bN`>Ki(?WLi(Gv<X4ulZ2Z<xlU8(!<}oR08J2eeaD9es@cw>!nXwYTn)hQ2&@PU!@Kk7dlq{0;k{k_W6&KKZj-Wl+gy*hizD7y#GS51+&x*SmO-~y&`sP#vF0VLD=+ulSWD2I7)^II=r$!1BAiT?R)It!VcMn8yEzHHEuh9y(#43Bsv+R%trL5<g}2v2Z^MZUHQeU*24SiO$7Bx9%INLzksNC;7RQS6oC13xtS)Py30}h(_*w9tbMcjR*;w4Y47zKKAL|wJQ<KgX$WUi2bImoJ;Y6N_>3Ie<#GTzuxTUW>zV7~{CH}G--uUh_H~f$QkVlc>U_l)=2@JW+`ep70$dnzK@`+Pein8W|6GJwkYh~2^k%siJCvPmQIa7W}7tRW&p=R02vcK~z(hECbtVM*S5EY{8dIOl(Kx~kuz=33fcwERLYC@`ZOAbdQc*%Ik4V-jDWpcG(`_91>Cy>4FOvAJMwHMJKGkWBghCJL(aDlBe?4@+ylvH@MdTXGrbCX#Kb*kRugvWz~@QlbFslfm5U9Cp<1RG&9kJ*=(H=q{0Zi@}5(FcLlNmK4`O!+N0AmRzO{`v;A_N(;L2DGuI(p}qty3jR2{>wgG+<?HJx&WRvRw%x@0ns&VFYG};8yFg`%z}gq+o=BW@&**8Mm6U921bADINyMXPGGXHi`se&xZF4suj%Q3xAWa6aC=S4PTjQc>}S9>ql~Qk&izaKP6Wc}Q{tP;RiDiLE5yFP|L1;B+ZWCL{vMk9n`h^K9_M~Ko%m{9#TeEMlcv7{t#I=SILueTZ2CXkV0ObLvzxF8KGF*4e+4%8d$hTqm$~nTCrp;SrZq&>id8OR3<p)n8pVu;{HHCpUd`Of+*s7P(wlcQ!NHP1<xhK+qX6|oVs=GUHRO=lj<&6|FF5AGs>F#7&K@lBG3*!uM~j0%97uF$S;1KXU|v57y4>0Y4?r(6&D$C}sFB1|{dRQJIVJ~m*pZhFU;sX-meG8mwhjFO#w|&WFL?3jQcd1vHTHC9_!-myahFs;#-D!qeJaEB1)BynY~vJe{Ccl6(8c;NGx{sw6nZ1xg%gz6k(6rvY$ex!UMQ9a<XHqhDHoT|-aT6`?f`aJQ<J*`@|697N7gY%BH%lgi|Nf%jD*MROZ0|HPS5li5H>D+9&P1pSkUNLE50im%mW6s|H-dj!Bp*%eA~|#F<HSZSJ#{sF;o3GHnbaxm|<4IY?ZwK8j6@qe(arjG%FSd#v<lyOJ@-?B9A)NF@1&7-%`r7y|HY<k=(%&LY@gahH7zcs%h4OX4c+L#XJ}M<;rHc)R_E4ZsAo-STy9Y&{+#kFP1yI8_J#G+yq=Kbb<l(wpwRbLKn;dB}kjvCGu83X&P3nc(%<)@BgCMeS(2Nmuq=AN8jaX!@}AcT>eIS1KfC83&Z>5^S%4YG6Bn)xc6Tu%ZTD#SRtqhPxpw$fYLqIlx7tLc)->Wp5BCm7+a5SpmbAt+MGV&{tZAtQV}NiO3EYhymMJeN^Z+Po!sW$be=#8yf3?wqtpZt-bsl23TtoQ1a2}6${w}-G1ya@Zin~3IGSD%at8mZ`&XFZDgS)|bZv3+c89WAFwwjPe5eGVD1T8|DBqz7+0yev?siL|Sy|CN*l#_<O2Ds+o6>;dbr9qY*)wC#QGA&Rrt8&@#VTtSoi2?MBFJM!u&_gIt^NctX0QO0hN{4W_F^mW0%X)AP{Jg88hciQ<2^vWT0AP`vQASLwqjy`Pfgci=*s9Kq>k3|f%8CCaMIJ2xD%4yB4L-lbD0iCc!KWnMwWALEoI5*gLox7*spSd_ZIbfV?JSe3mCm5U7NuE8amk&Tq<v(*V{|0)(KD!J#I4km<WP!%}Of%b@xs|!8f@!0>nJf4iy%5#9p(OFR8y9!7zt#DIIqU28Jxd`<d-H$aa|Fpw*y)kc`Ek@)<jt1b0~_%&9H5VL@D2Vi)s!^lFbTHe%b(j6wqh*oGgO&@34O&1GMFqMLo3K~~b*_VcHT9(f3G#S(Syhin<MHYi;N&(C&gvO^!X*Z|aeB?&=65T%l}B4$cuDZ$IspE2&hM`m8vGZ|HIDWt0!s@+G6N1Jz!M}OBRgAYV;P?h8zoR`i``QYyPd~o(1!;LW|%shWFzlNOb{Dj`RAvbJ^;eDEfu;sk$ZpjK~v>JB4%G2;Q9T^<i)|o!$hP#d_VdiD>%tKM!8RzZ^v%(bIatvLpy7WSLI?D<dm*j!i)wV8+x6B;PBUJ06oq|+6h)<cI`7`e<yL7FUHIQrIqU@5VOqUMM&&V#>eIvHone0+HkzGotJ=H$eQFe)qPYJPO9F>=XVIwSNh2#M{rfM6&ASXpeZ7IIQb{x3usl<1^DYCWH(8&AZMX<XK$UiO%_LSps9iqb4^av$AeMC~h@l0XK1TK>1Y3%MzQYrnK``3KgKJNZt)v0RzVMr_N+-c39#UPgRA#z1#+NGVBdUm<TO)x?ZtjUd8T^OK9tk}p}CnePu!An`RPr^V)T8J`b*&@7Qpi#`w7i@MbTL7q4umssDR329g4;*DT=$g1TEC^Osm0+dE1x^GjTV*0>AB%<BGEep8;3QkP;R%b)>e%O{`--H{LH}CIELMw$bL3sDz>*S<(XE3zPs55q-(ALb*3rQcypK`118~hlnsLR8Cn*S;MAs`X6{$Y@JK)>sX~as=Qcl~4N6N+?26y;FV`Pl~9&fWF<w30pwU}8GgSR}J;|$Wws9UH7K;3D+Q`Pgg2Hb#^SzT~&umCJX_F_H6&e@DC5dOJvxuY6dU`puaROq?gp=H7L%lgrib!^iAZx$%vc>qm12rrPhV$RJRby9Ig(i<0t!Jc5Uo641H`Z1WTLBU2!hY4UXhk}jt3v|J<uK{bahM|{C7)@%0|Bd92Vsjvo!i0UZ+ce^ZDgU~zHy)~)n1#i&tDQ(5@J(|_GSbH3BsD9-hZ^f$3(&8YMuqS+`P5)AxJh-)po-DD%==leo*1nA$^y}giOS8mAnZmA{V`*Kh#j*6?W~9zzh;Yx&dS%S#;31pY`;oXLnRIHPF$*LcnM@(s_0ex>IFzaXRRXnV-z-ww&GJ&HQImR{Y+r-AK%v8U~$7=G<({Ji*tGsO;J?(U9Fw<35Zz7%wG4B!Hd;Mzn{&cooKI{y`C7xOY6oGGkIZq=2noq_@o&3UN$f2ozdVK0M3v0ui{r_?L^Rn55A+d3nMPv!maV0kvqxFEFa_J+0s-NA}tMGW2R+f2r?t_tf}MWRWqL}T6k&maLoF-kgp0UkJm7AgXkYg&Ac=Eg?O@>XIT-kQ_T$CY&2XYlQL}k-0U%8NLWE1&+K{siemZrHV;_u3uccrqQITKtJ(82v)A5c_F6N0vU#)f&&*z!%-#(-lcnWrDqB-~Zu!pGn%Ylm_I~w>rXZAy)0@iE^j#-nWXTGK1N-lfCM%d8{h%^6rydhUkv(A|6=#irHGh-??&;e|iQcPdpV<DA#K04SFmZ|P_5R60J8(v~<VU%_Tx&9&>h|~6&QZH@E5v{qsi4L2Xp;2yk)xGJ0vBlKtvHXGmA;FMIK3fW&yz*q$S*Z&aW=pk8PhZZN?7!dQJSQYoxG84hj!S3qnglE)gAE_-Tz=&t2<8AcV+JxL_=^XiM999pRxCh+TorI0Dh?#dyR~3MTbXR36{YE9nqvUKj-Zs%pecgSypK&G|vJpq=YjJSr;tUZP^bS{3IeCMiFr^c`y`YdMk4(b=<|0uhQ0I1zC*{mCveYlOEk_-;bPa4d{P+Z`6v`x8SHoD?YA@NwKaBFZX~BM$1O1uJ-$|#faohe8L0DO-(?{i3n~+z1X;<<tg8FoJzN!PARtRkH0n*ZE53BZ`reNMRi+c!uBp7(-RoRP$MisI}W3Jg1zj)OY<{VFQ&|h)c^tw&l7$LHC3>l__aw)mw)Rnd;#n~&%;OAuC016NBF0z4?>zv?8xYOT$35Poa!D5n4?pn_8_!@ZT(YnZ`jB5U`=ssdKT@9;QKDUQF}}IIfyXAvq@CIYg~gaKB&u)91joPnAQon4%PtKT2oV0_Z>4h`yFPVtaIXFk>dc<WW6V*3#(oa9MEE$=#sTkeD08dR<B#z{eFnhJHKjA>pXk^wK*)@Tw1m_*Oq(O<h{CC{d-00$>^@rdqnFEOFe9KoMLuHW!_%~BewBs*e;&=WMO*+;;IGMTib|S|J5yR02PjVKZWfo^j@g>oCWWn(uHaMj(g2ry}ut%C!Pi?y`vu=F8T3msb_n4_l}_4o=wy13w}HX!C&y>wFtBVX0w|ChA`>jT|D?1;dZ!7z+bIi@ZEj;Nh_WGAO8KHvQlQkS9Svc+rCPr1`n_|Zt4rgn)8$udx@D=;gk2v{{LCx%1tF3)N7o7pL&h(Sj6rr1u}k-HRq3M9h>QTzkeBNV7HtI1eiKcYlbFPCu%HDgjtay)~-^n$7zAC>vPeRw@h0Y^KGQSx7-ySLY}-;+$|ONIUh{j72<q&Pewbrc`fOMv=(_~nAr-k@`s0!eq5u9@+J1^<F&Qk*uAusW^H0huk7fR*4vmqD<%l9JFAC^j(*Da<*yqB@wZ;(+F#|`Uxk=oe|;U{*Aadl;a9o#ukdSlkB`49w!bR2zbdxBDz?8Ww!bR2{~l6o&(FN+-tC09E4JtQ{>sgD+vfuA`u6(sif+4~blbtLwI&f3^DUO_3M1{^M6f81a&!?2aGj$nCiu4<B+3?r*O^4OE3;*5dg624^SOY#iJp(b!80Xyzf|HL1<?IcLfwE(lN$R%^WC^Hm*VUvXE;5fQL>%A8Rl=Y&fB|_TRXYt7>${3E{}eqN`Lxwbqvkl&})+vCl6iU`MGZUB!+Ik`uRH-uAC%^$%b)0GK(u2Ro%xomyaf#D$&<3N=spPzqlT6Daunxcatd}4{O}`X7JZ<aQ?m1jZ{g~v&VN~*q@mgel~RYx>%8FszjS^yZ3&^VOYhumtyX^ixWxr=ftu{3H8f@=B&h2!SPYv-N(~+UJ!rxr+@YNR24nE^zq9Fj6&q$;td-6<MVpx&&ar6RhECJ18)9`rC5A8AGZq^f9=+umq+)DDKTo1Uz8UgMcCaW{vOmBJs#s{x3l=Hzx>Wzvi!n@UB9pM2VDmty!@c&pNj680l7S4X}YkBSNP1u&%a_m8ff=FlWrF~=gA|u`sU)RFTa=+Q)gudd%eik|F-)LR5L*@8zEkisiguvtqe_;@B6d|A}y^%B2FPNNNwHuY>muDO0IYElOxXp`B#8|@EzIM{V29lzH1<lrW)DTtb(lxbXjvM!fiko;9!jNC=*M6z1E;YIj1UTfoL>YGbpu5o&ufNJZ+@nbouHIiW`#p>*RfS>7<~oE<lyu3P@EFj98f{-s^H6F)p$@e~sg}rov6o7nRz8%Yr5tUT=7OLp-1-OwUUUw4A#!Q3i4;y9TNkBwlaCu8c}#XWByeq67t{FpTDcbh-^pq1vU00B4g=%khkV^xepMK4<&jWwIVI^%%L-tz<oAb~k5aJy4zc%49t&_>^ew@5=MX5H>fH^+4ODJEiHl+n;juqzcMD`taFp1?`McoY;9Nbbhs_4M3zd<mUBP=xFCTx6cTQM86td!gDl~MSq6g)K_}b=Gk`k1orbb5Rn~f`$W36{@l&##sd`%8!pSTalE~q+q9dI94*<E*ZmC9WV;{Bo{3PqFk?0KfYDqbHudU*#!~MmMAJ>grl}H}uHTK=v^j$_1p+(5M+0{J)9<i@JW%d}4*cqliW++ph=3*s;mHfGuO2vIXh9_|r4BrJJ$Ls_8PR^RaRha)AFy$(gTbqzM%IcqA=n<ST|;cmb=M&3IP_cclTsTF_<nGGQ39<@%(b6%XUq09%%bQ2pS?GUwPs7NgmxD@BF>4^+<VV$UXw3hwoW_K>9nPS0^XQ02qA%lm=p*GfCR!us8lYn1h@ocBiS-ZBVj<43Ne5QAVyUNOHkt)nW8#dRft(lXvB!U*7|ldr@77l{^q6gK41TN?zwT|MC{o6+h4Q3wQ^{i6X`$3p?yo_^M<r5^yIM?&xxX~%k|wt6lD0={r;EIMlGYfeKxvU7;j3_tvL#0bB{S3OVVLvGY}Pqu_hrvfC$u59+k!(h-#3*NAkEI!K`8OL8%f=EF};F?MJ*d!@$0_V3|BSc1lv&g=#b+SS4l%Y(G<{(N$GSfrbHQw3t1+B^o<EABRo;0q*ORZnKUrAu9%^7r1wo?S;yF$R9arbS44mVb0)plxw~oyO<IW+gKAuKG%MD!dhYJ+(i@O$|dRBkgy0Bh8vIm?|k6d)Wq!1&8Ci!xo$R_pp+A>C1N(4yk=8!YLGs`?St?yq$eg+OOrm$CVE7zW|MLcXD5_UL1Nl$4A`COgo?($TqjhONO<v_YU-TIbxy?*ouf10MjFTghuEE&S!K*awwZM^+fR!7^#;@G>VpCW{oi_5($Hs{OR6;VI{Ek_Y3O->N!5k!dnrAR3M30%Xn&#$9jM#v$9XD+!O`9!9ul7yDMJ9&vlZTIl9E)en_0RuO(#>k$%`f?&ah}YX=>96fVnmo0!K;84r)4CGY1<Leb@};HZbo#NwR=5Y3Qm8{bcKPdusUJ{|x<~zN|@YYX{VgsOtEycv3h?L6Uyb0hN87q=6KlzG@<81_&hvE5>x*0VP4Ap5HjLr&2;o!`VJ4qiN4{dOFF*CJPF3TyDo>Hxzi&TzS3GH*SpoheGTK4>r7=G#bh+XI%2VtS8gf>W>4NF7vQuecU15iP8{irL)EclmU9ZaF|4pQ5I0wOq1(Cu6l{qVzsU~A4CVW0z*+tr=`sI8+V=!?fuQ8|Kbhj(bq_-^v3fjpUj|<2+Dfs{FMOhm_)}jXh+K;ZQRbBJItfCn$4jxeL8VM(v(T#e2EP^9sRw#XJmfoAuzIawkLw}?9LiA!L+mk0c#>RC7(RSMQIE8z|nu#F&YX)(Bf%tfr`K3(_Ve(N1guY{dr+9<9JwQ2%Cn)fpd*%@(V7!upFh-jZLkbvxDQv;0e)=J@ZD!!gP58b;`4zJOVekV2#N$nHR>HMSBry<R6g!Xh$MDWHA;FS5k)%1eRT>ZFJm;qG=M*=W1m&Sb)mf*R1bNuHUq;HFaN0WnZf@I;NnJ!rD41$6^qy3}wVbyX$?N?Q3LKUG8fpzyZ6{)1##SwV6@Um2YoabHT)zJMM1XnHG(6ZvFe8s+E$ijQ{taM@cu7J2*>8=fE!Q&r{OniIVOt9~}nTHnP2nzhfV-OCnrAyCGX8xFb;c+^uAWc1kf?3qop41BNto3l6$iIq2e&gKj4Ry2RW>T+q<j^jV4IB4Q(S;-jO2UF|2p<3jTr=E%BiLj!_7lS#+oTCmcs#Y&gpd?%#NVt4CqL`nC5*#o(u;W&OE)oS3GP#Zn*nXEYE&AG?IU09E$T+U=QSc*ipByi_s2`>f_)~o$JirbHFF?e&&cV72i;x6)Zv#Cmw&=uPXR?be0QJIRs*s0-Fm%C>`$1GZaO@V(A$ZQoPV2_#7G42ahce?G6Yi#{Yr#Ol_)yxX+qa*tqBYr4tvq8IKTb2SqCZnS+M)X+O*Jd&Pn`i!UBU-e8wXnh?r5qCN3u_j7lZGaQvC%>mp){(PdbbMZn6y%Occus#Nz&4@5@fAsN-I*Rz2%Fp4Yx8hbez`tA{Y1ii1UOV6O3D9Mkkz)_^g{K`FC$|{*3z_zq;n^{<`n(FC@^*mEU2K#``Fi1Z3TAV%Z$ymY!lmLvuq6Ry6VgD^E!WVN6lf*UcvEKztZiSEv-+s=TMhaP9))U%&+2I5Z<lD7Z25%5)WOlg_3|icbB$b62aF)EvZu!regLXD>DM>B8a=eilc9Eu#FXyAiq+chQJ-8cz=geEmMIde^PTP>y#BI(gS^u~r_$6A^Hot<WA(We!-k4kXku9$?oNWB+&GRj569I{)WGZP0+fDAeX!%qP+IuCHtk-Ls-?A-h0fI`>L4RxC3?*sd#`lUfF6K{l4?$QlT`1TSVpJ}CAIM%f^(?J>POM%#+N{TPeS!tS_mPfj9l<L|DJ4+Y<zvPaL4yrHITk@w9k@^0hgp4>j=p0r<u^w7)QlT*fAF_xS6{BrjM0)DgoZVzI3D6Y9D+>=cAq`Tmrq;u|x7I5sx6c2KwkGLmZ8O8FPSrm~R+jD%AM;LRlgLLRJ?z-xm++d>J=r;exmog$RC4;F(q+$AiMr6qcbIFJ(!F*~&P{v?rlOC}k80iyMn98r#)kN}03^O+$jv;Uv+9cb-Br)<V1_xYP5TleU1G}42c8j2<y=*mZcZlF5hwe>01jY0c!L6OidCFL%v)nLLOB*qc*Fg+1sBPS|VhWw;VfqC<43a68jmE@1<avEKo*3f!zT5_v5!bw6ZZ;T$X>QKLZf$VP_1oO+FySohrcXW1O+Gq=-7R-FGUD0>2P&dk`DnpO1caeq#N6F{cLRybNwu9eMG-t^s7ekb2KS99vQ^250v?Xjv$3SIHXYeV%}O{wiIZ2h^89R#i}<@I`$Hyko*=B&jjcMGpLRDW959A3W}Qy@eJE2d^2*s}u7%($dd4nfO8|o8{=8c}tEYeX4ekg2w<Y|G?<~Vse5oOYfkZ6D-WA{e6X#cyOdg<C@4g$-pXg$lM+3)w0Bp&x2_anvzi#0$bPe3ZO~lqPG-+TtK|5wy2j3aDPEK0|l28I`-Syt*b&~3gYIDAcDCN8GBk#WEP1+iz@ECrv4TQ^zU|eV()W-)bnPP3j-v?J7TV%`n{ukxrR6$TyyP-xBM2zYC_QW))dX=d(gXymx3r<fsN^My{h^?6Ng10>o0FHtfsT4f-R=HgWY8i7e5zaJbgK?{wOk&=FC`a_yvKC2=du-5>g<%lt6v=i()wRr^q5@31l9Uz|ofRF_hMea;R}~xv29<c7yi#n$j)~*~D+KQ_axBh<NJ~0mu_=!NrFJP#Wsp;)Vs$Jt5ul9{8N%;`nt?+SRn`I#T^oNX8f6`emH5-oh!M1reu~1()M}8k>#R&gy$4PSqd_GeUxB$N>wme&?*+G^>Hk7h=H4`RZ}70(mW2I>ifv9RCV_HV`thI_EKmH4h+EDv2{IG0ny~{>znE0)&h$#SZuoWYVj=!Y**S(1bx0ZN!DFe7KBlKER1>>Hy1n;n#Cd7G7sIx=cAVc*PM6t?ukCy`Mu>RVV+4vbV9NF0U9Z5w=vOF{fUc&A_w*>g!31M@*K@1*8XS&TY*xeab@}6cCkZkRCygdZ!@BU@Tv3E6e#~qHk>Y?XlzI1EP`#1R9)d%uN%14{a<n^ggD@nJ2s`nLK!G)6S{3;96N(!}`J`n>xpUGbD@*fJS!ZbL5Od0p5JXi>2PxD#BRXW^C&qu+{Y4U_{X$t$uDb`-QSX2pEkE54O*tZ!(Deb!tbYJElxAc(KHa&M=^>|8MIe_C>ive(dOU1Z;a;$z_wLGt^#c+mw=RA509CGmuh$PI*ZvO`m*4?T^YsJuAzk>^14x2E6~&ABS$rJdvUzaS6$oEDfO}^B*WXp5A5O<}s@Ko+h8s%RpDAEZS^je&wO3HEh^iw~?bRo4W<GJe6jD2p$5oK3kQIUSgS7%F{z|3$d-I7Io=iTm3$q$_nAfmpxqd`L0}zhuRz9(;pSy193ezbs_w|S$d?P=&!*edH=%$?mw<fa0o6(!_;m{F);pS=m5A6z1unKWJzroyugjf5L=?Nh8B3O%QOktfXMJ1$!^Mx7OFn2qmERsOt$w2vejtN3R3X?R}X1~_vDPe}wRGoM|;}NeXY*eN8<b$QU8z7%an2L%bu5b$%Ct#Vx{>Hq|8N@|%4hn=iX9sX~x$YimYHkOpOYwt|DjY|#n=n3&W@{Cz-n+WNK9kqiQez*MAuRpgo76cj$sz5}R5<X{jpYp)O*5DM<7Bcst7j-uS;;&1RTQZ^Rz&I~O^UhfgyaWAp%^{mvpdlu9p~DnCVI+-m{gyL0{Emj7AN3hjuR)a6j3g8R*GOprLQtvNx!SKfDLr2E+nVsxMqbvp|VOvrNbLxbLe(_Xl%~EF!^l{kd7<%u4@2Y9SC5>4}k>v0W4#8cZw#`a3|TOSbUJrHbl0>c<94s<Cu=8SQ4r&@VUQ38A+@$;0@w!F$;tF_MQ(R!q>%u{Kf+pe>tWce{EYvc4OBmJ2C*A3H`Nk$lFXug(lv46u^pWc;&3qk$T_3UmF;!9Q$#CGW4g2&J(ug8$8|(g;wvx^>*#)iPD)%VLL?7V3(kB6T%uSuf^!xN3wMCQp+H0{_rOQgLk1Y@Jtw<9;{4vAWQZlb<!CC@7RUmgS}K3hyb=s`+`3M!_#&!Z4ghu@W4n-tb)3G#rn*3ufACo1CC&LExU8QT7TM$m4NGKR01Byitaw_mho%v2dl7}iUC!;Jw6IoSkwdR9)UvDe2+M%nn&9{rk2YT(>|hlKwIkp-AO&bLgl4op0AR5iL&q`q*&siIhksnBuL|3G5Zytz#YxEPpRhJR@J;ebB37zHe!_4Vw#WWZqUs5&WxVFynjcoX_;RhnQp~Q&qpED#x1<J>vAi%n4k~VDlO<WnE2Bb&zVf!Ds$njMne4?oyx@cz}C-LgBJ;7B#qqb%Ilx-X3$5rb`rgYo`4AcsrPC9<tQ*SNIBRw2P-f?sQD@8gEV+a%+IgBR&V!RH2nFUQ0Q2D*DCrx(5<|!F7gdhRR9OyN*TJ|-S5AN&$NYoKC=dj^=u#YnaWsZuUvEQmT>-4pJ_w6+7q8?H?D_(mcR+|ku9BVfWgscI-=e$205PkOhj|g`o&D2DIWPuRXaQTW;Cs%&y>_yVoE#OoYj1qPeB=!;iWT(%S+JvB_e|b{i|8(8FQ_sp08w4xp!R7K7ZiUbNXeQP33~WcXrRO8-6=WSR5|YR<E>%slE{x7FA@FlD)PPNd=)s9v|1-%pv3(n|6skZKI~7;9iCSDqqoA5hUwu^u}_=w3^vZVk^qkuCSFCZz3`mwUhRDv4=hE=YfkEY8v-|gb=I&j3kxEZTUf@o3;ZDW1D%clnAc14Mo6u3Rf|fhg>Z1^^f1e0Bfx_&?LVwz{sL==4sJRA$N$&VNP`Z^K!5S+zK^Gj>Ck!_8hb_>KyNAwClLbXo+#@ZnG={tCNGto)&Y1OUl;z&4(X`A@&5*^x60{ki%OAWB%1B^8C7MJ0_Qh2lEtN{l?;lGl5fXwrNhg@Iq|4CfD;lygV)e+mM|M?Ytw;diTcH6r1%(Ol@o<#g_g}_n)KhQEl)Kys=wmM;r~ULo@u;0NF!|70{$8vx3JN@9lyzRbz`24^0LAwH$Wk#-u`G(;z1HI`q2en;`U9SN%%z)iAl=i_8T2vSs0HDzqNUfxtRFlHycq592`NKB4U1fnuFLAVxo-y`1vr=;wtMzgAUwEo;ioVuE%9Vi>FiBqRu4+DEL25=)@TlNZ*|l@8vxqw!vf;!YAF0?XF*CsfV);(14G7s=R9OhC6`tcA(c#6-tv@o_thx=EZgsfuB$$KDRk%=0i?+8_rMECAC4<QL}OnPQ>OzTBEEqtVl5td~IT=(o*9ly=-1K6@p6_C{dX37p+Gf-lr)hcUwh%VvN%s}C;#+2wy)u4qEBQQ#eW-w<X{_O+QovEfD1cBk6-Ry)+J_stU(nO1^Nv(npRnyB~%L`s@-PgCoJ8}Cl2PWs@;#|(&kuWIU5h1|JAYL@3F5)sP8L#Xnx8&0mqNP4cz7yg&-KlIJdqT9HPal=qJ1j~RZ+ibm~#S}fHVy^tC4$OcQ95>0L<J2h29pOkOtu04k6#QyC1Qm7=d9~nnK<#qxAnfdkW0Z?pw!wx%$Ek`!^Iw4vVQg0_Cx&4BL{i$t=CNXSxvZZwIHSsdO;^|((<asSi$p4j@B>#9(ks*rlM>`~Y|Cw3m*>A>f`J49p57Y&3YV5<pPRxKY4Nq!r}*vrK&tj~qjZ_rj)~j9!li!STe8&r`fC{Yd&$(Q(i%{B;rR{jMo*mKLis`50s|C8Szfzai4};U4AYw4_df7~>30Va@Wt>?EXsF1(?AjkN@+-3vDqqk$N|x)77uPH*83OSXH5{usb$Wk4A1oqv~<er@0D%$9;655TgpoQc+Vk^%I4sJ@7_eNCKb=(!-2&>{^<t^W8m>jn951<(>+GQSA}#Gwp_ToMKa{G8~2F?5<cI-9BiBT$qhV8zmM>6i3T~`0q^;lV_!YzT-qCA7<ruXa6WntoM8RF-~?aWb5K|35e3C1{pJ!;@WmWaP@9`ZP(fmf9BL*@TtOOf1&ObpKomR;C-8(56vw03_Ajbp+Z;}S%t5(}7F*>ABq+X9qQnC8S>U$Iq`26g;s=6(2fkUs1KkolK*<jPSWvMF;nT~=flMrVS^PtV4Lr<X16_p;bPR)l8Cad51=3Sc0RWxTFX8(ze@@{6CN386O-}#=!U7dA2o=zekO12$zAC7IfAU#K^)f==^NFNE>4!$7QYPAPN5d6pAj&Y5U<0uYQ%Ggr?KN>Q5gx9P-X#1JaY#l+Bzz2wL)`QOjUkkrwt>P?;k)WcD0}8Q+%e67zpjziTIKM$N1DbneZoeHdcX#a^*vMe`EFDM<mDx-?gS}7CP=QZeF(mu?(hy03xDOUwZYC@rA7N9d?s{dJlY1U9$2(+VB2i5*mACUh){cA0birT)Ld$Sb=>u5J+Q;Pk5MzM_Q0Mtz`_@$P4s@=0NbhoR^6`)(uoDA(^9`Ild=&-LM7~qY{F_?_BSm1-U^s7Rg#ngr9@-(oemyb*+HVJKexAP*QNk)B?ZX54IdW;og}cR<^mfg;|K4J{hRL<xtXzZmQe?f)mh{w6X;ff=*{;&!ver?QVw~TmmfH7m&IvI3>jnCoCSao%VQz{zB3V@a8pxC!>Y~AsI{}8JXuzz-;4-=p8VQ;EN{R};z@($%Zv_y%3|X0Y0G+QSgU3s!Z$2JG%D>NeF0O{)Cxq0v@;4S^9n>bDOV4UGZp5&QLAKFOiy2FS>O5e{L}8o#gp>Q$a_?F*K1T4ueA|u*yFP+<D3xWg>=1Rq9TcN3Mnwg4aFIC@eunvOuFlGD~G_`R8$1HR;oMDVh>p7p933<!e&EESC8yJ9$Muvwb%iX2$T2^Wj-FljzxkorY>fG#lilx%$o>58qXj3%5X@);B*R+D097{!TV+}P9|e71qECeK0?jgHwp)$>u$)iLNB93(?f~pq@WHL36QY^;tTZ<WQAZG<3APCUZA5|oXQr=PnC|4S+4XyevlUGiOA;JE!5>k@<|JIKekYJmk=w~LcI*viFuku>`5)uQ^P^+qGnoh(MTPUnVv`Qk#brJ;N!$xvk2hXfPJPo*)B{20z}=y6x;W{SxtdGztlHz7TfpL3Y3U28J#o>AgCgSS=)4(^{9w>E3}NINUZsU@?2mqHT_N`f1+akY@CdElz-~Ej@kq0xyt3_k6paSRNfI7G~8H?Nd;H<J=a#9yT(k7`MxY3;bw~W=Hebmoxn!Bd_dyujsaOlMaPhg4@3yV>xyB(dcdUroHgk(HffE-vzmieH2dE)S<B+LO+}@ir^3_zm<w1RFSGtYcEa)%cfO)_`Hcr;ys&?5%5-2{ZTZ49NNf6Eb-zuQtNi>tYoB|ps}>{-HHLG<O|&SEwbvB~Yq<-LY=a$!N!ETuxN!+7_NIhg>>H98NmP(7@9=&JbcQS52RE=ScTS*>R|2&f4zb+IU3qbZG3#iKz;Y9r81e9*%cT66^_OPLZzl|6MT1jjcGFr4rAtb56l06x8@>ygzepgaodHR4sXA3;W&;Of;8%_zZ*k5*N@+P`9Jyf&2PI3(#37kvw9KOgB_aGhSI+n$z!V@_d`n=8V4B&2Fi(&Qf3DXuj*xL@`m;yvmQ6ST+?~)Gk;Tm?Q`MUxESM{7Ci<-z_ZE}G@d$QD&uMPQ{ByXD2x$(6ry%@JF3yR@Hi6Y><bJ&4a&LJ|#_FVW+OtPcc%W(v&tXY>iOh@C?yJyN<<o!Te#={w_I+0((oO{Y<=^WnQs^p59%|gY!f%1pBY&ddr~B!X3bIH@N92EY#X11a7{z4`ZiXI?E(WnRVp*RmoWNHARrwStHi9;77Hy(ex-)#!ktW`=xVMKgY!W-1u`IJzHBx+A77akmD3Wzj6=I>3^VEE@YQs8-x0)CQHKW)!W8Jvar=b)x`mxiVfOtMSi4vqL6)BkolDQ)iji%xmKE@e|d*+;n4H$4YYXS*TH`^ISJ+rE;l67RuOiHU`<l2OMVfjm5ky4mt7vM=(<W7dal9W3l4o2$V?0ZL}6$z8c)1SqPs@x7+S>g8m(Ff@vN5SMJrmgFrwrjyvHlqthO(}pR(cqaygKl?Hvu};hszpm9RLpUSgaukmlh{l^lw0;FZ`*Ut8Qd>LY?3im9$sj|<i?=Q3p|E-Q;RUfzvITuSIg*5M7YLzemy#BFT{p+Uj=5Hf5rU;KYSN6?wVB0@y7MPfMMP-d$@lfVOGSpucnWnr?K-x<7;gJWaWF_O6O21LM2|j(Tv`3Kr|Vkj4CiZ!g2;MVG;4m@pck0!AGu9HKIcclT?nsgEw2eEk1J#xp-uGNLMI5hz~m`9~Hu9<xlr;c7m?z+6$H%KuR4!O`f?Kk%T#kPMhb%t(6<TM)|wj;x4k<hE(Xf1tPT8_|f{2??A$ilIfKbp{>US$MpZegRDD3Ce81-BgD>J?jf)Yev8XUpt|w?R)6w&EQ1HdUi4St>9W|@(xXa<RHJvZ##6!Jn33i>@mWP67#a~Fuug`=*eF3`T}hqs^IM7E^0KT>D-gBPAZ-ClZVfXq+F(RCsuOA(?*s-4BpHtOby;N~ld=hFf+B7qei}lPYN0!DL-X?=W<u07B@G<%%*#UQr=#~J$zw5<Ao(&oCVIP_x$2Jn8mp{?w<a3Y#l!SPGbw;cu4j1?zGFv<3_~XgBKHjoJ%OrWT+vh`&?-ga_+@q?KKSLCO-Y){HY*)-d_CitgPmDJ?nQ!2gKc-MYOYwrLgkoVJjzk8+S}y~aI!rs5%KeX<GD07w<tPB8GI2Me&VvP*ia+hgLMV%&`L$57|F5MB0NSG<#q_Wu2R-;)fEqQzn{Py*cpNUL_B)9$FEyHziSvTwXVXHlr3O5@FNkf<O&-rmT_Z9W_%rhhe{mx;ZOF?D6x3Jx(~w!PN!Jcf>r+Gst@1Y%1?=1U*@tKddG+mAuRiDVuP41vQG=U_UB3yc~^CA;Kz3$0FJQ-l)hm!+;363PjtVVBOCsyKWk`iS*gmC(}|y)m;htsihfNR1r*)+=GOw6O)K`sS8xdOJS<8XNs~N9qQ8)lxYD8__NHZXY}qxa5|J&_A}Mut!3WJ?n_De^&Ghw@<;|9FsWRzlvSQUu#ID^a$D>Ic7n0y%Dc*rcL6*FsW=_q<$z}x^1!m)Fh~&qw^CP9}_>Fe)`mR)a-f~hB)~JfPgceq2s27%uFyBp5BS!9CSEe(|7?cFpGLEBJ(b@~4GB<~+o^mQyGQC+%QZOIdo3qx<Z78p;KHPc@EcE8lUg(6yBt?Jbi^ew@U4$y#GQL=imehN9EPNKy_@)>hB&J|rEghF&SgHA4$IsQB80ul#s5Aj&`=$Xm-iA}b7fDJ{;shy#AN^+W;G698&vO6om;ky07d;k=PXc@h1ziSih^YY=73^JR!=5tP@Pm=NiK{(ZDJu>J%kDrxb@2tRl&<qaUnf1%@|l4ge5rz{56T?Sbz--(fQ3ni1(oJ;5@>=9R2B&qxas)J^v#ZE14R6aI2FP=s^Sx%91RgXkq@ev&xSSSAJC7JQ}!t__^o)sdbZ@*YDCs*$Mf9nP+;^G&fg1J-x9x&>GucLP~pXg9U>A>sRxpUu-wazB&x<xaiY;T)}>bh&lIPOQvQL`N%@DD@!kSE<R|cG`RarMur@rvd^MtEz(zF)TxhBobb>^B#+b`jBEUF9fO`=TZ`lT}vVSlNz$_krYoBA$tUMxi-}=^uq>E-XEZHfj)!g23-V<9>oif$Fke316gUCQvRr-h$u7EC?^^JT(roEAb;`<|OpqyZEI5nZE{)Mut!ow12f`dm%r_N6oX6rnf_g9&J@bR9(TBnfTM4K$!4_>JyyGJuaak}v_n{PiPFALQeHC4qb)v*e3ZXM*>_*UkFsY|Ox*wZvQu{;|n*7SIZEd()ItFYN-Fxo_^Se(j7d0k0s?<C&-B2<(aP`0b7Uz*0ckG=SU9S=2l)M)dZEHHQ|GQG#*bh*I)&e9&mAN=&$jTbi;QXM;NLepB5(G(FUQ7zlZu8W{jG}2_}TQ07RZIdk*p4AyzAGKVp=akL0>tc;}NH~H{RT68)7R8s^rb<bReE?0+ahodq1U6nUsZm@xx(wEGu?ZCPl0KwRR{P3~>BWr6fGb(2MW-qf?Kr=y(qFDfd08&6=j_|T0S3oqxX{x)m}cSvz_4brA-u<A!{7gvqVf6oGL28U_J@~%?)(gNSGE?~@$-B>+4y{@Wu(yl<&-|%DWwmE)tYmxK7$I1@dSy-EFR#3!sDee20H`EOGfD<)W@?>d5utcO>N_wAbB|F7go{5IX9&A=_@vmEez#35}U_k44xNFW>&ni=;1Gqbq>`-{Ull@BoKg$#IC{ix>MMmn&a>c!)@`xyi&wV{9YtoAvc94y&S?<i7maWuokOh6VXRZfOvk=R|nBoQ3X2=eobG;a{&LYO~ugTX|%39bN_AS%T%;iK@MPCSeBI-c&r5|C`@3rk*GDeD3*1IK;^AOZ4rzF1@o)Hm?dUZdT)992D94{Sb+u65=qeY+5`m`;;8ok6KvdwT{BL%Sb;?djR=<`;2^XOKE6!`!;lspuC#^BV5^yn6Pm{JMo~W#ip4eD7%tsdECdTU3@-KN>072}<$CrmfI(XsY3My*#~8+*c)|5Z%iU&m%wYwuX~z!-bAdZIrIZJF1qS&SFYY_s_y2uFN;{vw&L@8hKQ7&R@*z#KXV(E~;bH5_at+E7voKx8J`cnyJXmxDP)r6cMU``)5Dpfc3|8wVT!-3x3<;bB5AdhGD8QH*R@(tmP5A6*IzaTG2#so7l&iu_+0An_f{@zXs<ubZAPU!YFm9D^D1u^`Pdo`{5T;5{$E1B-M^Hy+eaD}2D`}#&CgCEsFvdgmtg)w;V+Qg!i&hh56Q`a4Xzit_Akf+=?o3IU-nX?5d1jkDN0o*qV&mw1(^;A-{lUAcPCY`$6#O>71!hvbKd7VQE5S?}D>G@oWMP_@qw;wcCRU^(h_L%G;s%*R@+v7}DPK{UG>(<04hN(1M8Y#wo*p42jZYDhHXodV=`TH9Cy^0Zr~Ea{ud>$BfYnTyN_lqN8I>xrr%~c;5yP7v>#S1_DOP3ftk8|x63L6;P0+`1dp_sRGD=F8Q%{QM>Iz3r8{;g2$F!bh=v%t}0h@)I04(lHlDA{ep<r!WZkHd2>9c?rMz*yejpF8sf3;kV>BWv|&8a#Om-)UpCHTt3yBcfnW7e<!+sN3_@M&}M^CM@6MLEUlGz`-*^M83H3v$dJ`gt`O#v!PQC@QV25>`!IgnENk0@gMi-1xq3L2Oaq`fuN6!|7gJT&VLWZ84qMVfDjeqET!(5s#Y3wo|&!VI<TqA6GB#3Q#?jHL0?RW<oZZGFP;smIIzCiQ59+$JWCxxXc1R!bavB2B!~tZh&Q01PW2mgJ)(O5_q+RlF(v0DMoKC1S11piMZ$=;3Ax!K&UBqWw1bWA+c{};Bb=0&zeawjZ-v2MB@WBUFlf?&nxGzJ{J2@npzfmaOJ=ewHh&WE4ZYxTP;1*tg-?RvYnNmt~RU6J@gnIN>-D8;Md;*7rM5ytvak9r9YvFL3S@yYk8FZWPmEi5%)>eX(2#$#(g3ok1|bKKbLAz=Y%u3Sr+{XBPO1o{ZPIm=EXn{r(Ed8O757VD0A>yG-}L$4iMS^hgzJa83vJ{xJtf5UmwYBAT2Fy`76)n<#@)!d6LVlEphfsh|DU+H&}+~ESDKMV)(3@C+N%s-d6wbV~l3WAeYCaW>KVOq9>#8;72IS7CECls;O{|wF_#q3TPQo7r}MXU8yM~as&8eGzM77%_yH@+(*wP%KIuPWXAvMO>&QyCf6V(n8%3nDA@6``IT*cd66LR=93HcMRA!i8~xPeQrab?N4fH#hj%os;7y>V0WkO(>C1K|&l8C)&^}g1ts%##TCs&B*G@+j1$x9toY*|7TzOY@9<^)}YbxzxcE_YI28?1}3>=M;Pw-=I8*LdK<<X9l+1WJE@kPILhHB{}dKbL`1;SmWTKb%IBhHJ5fWs0sX3!#jzy>m?7z04GS14HyAjU^R>mk$(8{y({b)XjzL<K=ZckP4*9K<Qb`~FxFBt-gx>^Xt!tk#J`>9z(DgfIM@GY+VcQXp4&l)g8R_i4v$!m486KNEc6)(SJdu|maQ3P33TRTio6IlfeCxmHqAK{JjrKeytBGFYijxU~yr+;J!Py##@Hod@fg?7eP>Sp7ROO8GmbLJn@{#<Yl~K*PWNfoNc695DHW0A?MjRae<x8d1N@d0)8IApI06K{V4_PNZzgXbXa$S2t}KpAG`GbGDr{vhB1J?+dETN<A>1#(eAo<troW)qwhA2U&Y{$kB@pH@A2)<@mN2G{NslI1*;c>gU;9oJe_$&?QiW>U}&D@&z67@;s0GXyW2&W>2FP&7fPTUyo0NOe_ofBi1v|KMk~?pq#&IPS|kz`Y2XzU4Gr5N`0H5J%#F0&)8ui<~XI)nLi39c4nMNt4~~&^eLwIXWpS38=rP#>o!(g@3nTaxf@%BPdfu}bhd#>Y2z%BUuCd65%x({cQ7q=2W8uii2Tf%-JU8AR%bRCmtUslZn}m_sycpq@e{0{%jJhq=^uZZM78G(e}H|wyEl^!_KXKwx_kGTcs?GmxXV-7-@6Bi`MU6<dq<)3cz593i`WCu0QrD%Dp6z!R2$lN824CCh4=RlXe9YW4Quznrmi^It`7(szky%l>K^t$3@hQ@A1XafzGs?LPvg$|?DqWY^}$4q$KV%n@W1{7s9%V!(0<x;uQ8xV`rSLx+{0Af5Gtb`^NKY9(=_BJ%TP5Faxn~HXaF)ny96RBRF|}Y*8Z=uk&)5?p<wJcw)pm}f@Q*u{VllaBZ#0QChj#hskN1p;ADNj9DEB>^uVwMxk^5+t$6)}N8E%vI7n#49EwZQ+64p!Vg?@s*3fUl0T>lfQKl8ZDv)keubyoBjctFSGB++f+W*x3OEG;K!)F|W2N*{b=(eOwydsNEuXGJN_5@IDp;Vix;K5lF<+Lg78+Oc+WTK5cL=Gf4M_-TVow_HN)tD%V!1Nj&flQurJR%^5GPQ0KFg~a{Uz2$zdVvcKoEfXDk~eg?QH--?`zbvL(CMs#(N}RLmdTB4>zP4lapuqEYwWPo2|*}6<%5>Z6+hb;LIX@Oz+0-u$Id0g`~}gwH_W!dVO{Yfp%#+L`z>&oZR473X<l(>73;h1V&5<+=XG-C*;la&{J4(goY)C?QK2I^c{F0LfmK!(z4h1l8;?dSFSPF7kP^q%y{-Fc^sD%kb>BNBEZDQPOj1~QG6P7kcd$FQ>rx&ic^2mVw8KJ(dbH>Xt<37!=tg)ae3_6S<XLeMt&DV76QLQH6SEk1#5eP2<Ai{p@Sk9PUSVnVy-%AOjC5GB>4?7dFiTiCHS-(k`^4k=%P+Ef@erw%!*QY+K?Og;1Mk6d0!y54RolU`+_6v-`p}Yqx+{Kl*`K<wS;y@anlrOj2<waO2AwD9|3vg2hd%5E({%^s?It{Q#e&6cUxGqbYLrj{hYZSr<sto$B;MOw^S}qzM+rYcnE0KW2y-`}%c-}|!tfTO$*e&*usx;`i5YVi@QenQ?0FfU*aiuOel9)HEs8$EV~w1A3tRU;ypJaKlR#k70VfB;qGw8xJj#JJl2_@8JRpmz6!<qKw~6FSKH}D<1~0szE{x9TQjm<T>6K5j%z>#k)hu+tMfA5}EKQ#Eav8OWy|F&2^4(Xi%54fr{RpW_G(XBj7Fb^6q*bE?%x}x3*hw|j0Jt7G-)x0xLD5QBS2og#D0yW69DAVH!}TP^t0W@3ee`DMVLw-{^1S_<kERcgZDw(Yx`XQ_(6O1sw*>GUNEO_h7mU+yw|*|<JZRn0Lat;X%V)P<{={(_x0`gDGiii6sskZx!K7h&zvghubZ9Go^|iq&3H&Ft4;5rRJyL1{8cE+8@y&qfaAdJQkO{?aKr2!{&d9QE;09|CY0Dl55b@G--Z{}<<BthRjmSECj%E+BJobDbNqEU(HP{syASR4I|3@z-ek@k#>d{ul^$YqK<BipbS5J2^js>S#fw&ztdbk3mWIgX%%nbfAi^B2gHbr!s#>aGSJv$*&e_6@a`l{7bZTYR!rfTp>4D4EL>Qd}6D{gB2cVerrRFK8Gc~U`Ie%7{ti3Ab}$e;O2A@aHsQ=KC6yrCyyD~!?QxwyPM!{w>TD6z<tLCry2Ua-DF3p{7Uc&Xy@QpM$^M~U&$NQ~#9fPfG&;Bm3qWwKvtfVs$x$JrI*vl;SE;CSf-j+ZJN4?TfPL>@2Zh$N3Bi8G$O@6WM#OP;*$DW1HufID9`QT$Vcd51S8%uC0Fd0q&iFNi+>N+9fh^LcyOOEi5h6v0+PAI^#t$NSn&g!I<xy&|@SThAF0pKzft!G;aazJ?`<=6pS(cwuLRd&)X&&s8Gi`B&ARP)l3wDgC@O({M~JM$pRxp?{inX4fXK(L}CEF+D1r)-7*gB~f$#3-6lVfi5}`+Bd!ul#$qhlUqqgZ^=RnjHumZJr8PG#7axbhlGziq>s@i9NemQ)WHGG7!Rxe_lR$I$vW-UG5V30ip@%i5yUFmIUkfr+(rt#c+nZd7hSWS1oLSg8xC7zD7d$#UTv^M;*~X-qP%3<2H|f6&j$qx&w!5$_p7@LBwHwEju1~?UaGCBv=B%T1?r9Z8}4J?<P`-HZ4D@cBYP43R@y4$m)0bdO6F*)<nbkCk{^jmdMBa3^TKdv*|nkqgc-Y58|C#J^X<twD$|PiqHsh{13zd%xz~AtNX}F4HAj?t%w}{II@d^EEuE<UG(r$ai{&k{?lI_$GuNpVGnk2{3dkTod#3wC&Dg{m_neZ(kCZfJqakMi%m<AH%}<k!c&~k2`e!xK&@_|Q*9Rhq{M+x94(^SGHXi|Zc19fFPw|~pBsyjviRzFw6-*@;YHO^fEvwZt#OE0%5~uI=xhfe7j5eRSxu(IFgr(1wF*MjsuCvv!p1_HV$UC<SE&6y_&v2C9EJJYvV>&V>UBrDJ+(LS@`LJ|JxBi)kPY6z?yyxq-wyL)%vtULBaJ9t^pOM^dlx@gXWWdm5Xt??l2(=USP_cmMUng9=Ol11>6a9thS%NwvKB#`ECPt(v&{D{1gfNjN6Cv|@TPZIZW}NL$*7xgzi7OxtsON8DuQalsR)(<5Ud`Al(ZgCvkTXYN?qIp>IHR8MX<~Z_6}}}chtJj9E8S&s6Ix?>FbWX@pK60O@8a`hq>HgOd3K_`7CJfz0<BQT^hCYDrV|X*j|kN1HS48*YzJqrQa5#AQ}=jI5|HLdR&Ckl%o+hm8Yw%}6+HXZ5Qh_|hkZ*l*(p5d9X-Cp2cg(wfn=peEH`C3r}xHiLicdZwH)S6@M<exG?x>uSY|AIRZ+q&E;Y<Pr54jP@)_uBImzt_#`Nn`d(PM2erb4$A5=f!HXl`dxfnutA?TAJqVlsXJ0?<=GxdXXu6~dQiz57mC<5cx!V05fOxQ-$<0ec!D)J01)*V5hegru#$_B(y7W)xxAG!{y)(Nm{uNSG5HBu=fI0@IbregpEz<~lP3LAg;Rm-O2x0+4y7qTf+m!tZyl3E<!j=+GQ2@IS`qMYq)%)#>6&y*Qp^5c=7#&p!vI8z!(Qxav_))<hs-GnKX^2J<oVA0m7`$fb3tvi=f;qhcFhsV{1CwdyY+S7Qap2jR9tdoXD&pO@98yXKsS(dM66XV}|XL79->iF&zTPHHUM@3s_45LObdOn0hbE|ye^Td2%M$8wY6`96Bu9@87GXk#G*`jL*KKjc&P;-XSNM7HhIE~4{W{l`&B<hSRyf<ot(M<+BeK;2XHZmACcZx=AAp|}ckAtOxc;(N8IDcRn=O0g<mI2cldtKvE;~~E6p*CBVncEKpP7KyVnqqCbNWK{u$UW3HLbfSFcOx214U48%2a8vw*Ln!bXB$FF8;}Vbq1GP0;fhA2*w(Gu8nd7pgsBAM$P(`PbMFsj@~pk8Xa|Bg#Dt6sW*DAGr}Ay@A6CrxLFWuF2Da;x_QZTcMP=5$RQWM*C8Q%X`O}e%DOjhlwAspzd*B8@qDL6uG<8d1O$`EU3<$KcSfa~E(8DX3hreceF%6iriI~hikEi4WGmps%Ic2@Hg91*>tiwO*e%Cjh-~9+(OZ$P~u~7dlhy8+Kr-lb^nh&nO0(&$TcEsA=-nm<*1;Ya#$ftx=mA{so9`3o#6)T-}Hj)gQhkypC-ZGU!=p^*yvc^m8JkuupCJ@FU-1FqXX~9_B71Mnflc@Nv)dA^CEDT=8-F5j@tV8%KG=&>%J@ElN;LYD@ot3oMIFzhRW-pH3fBp5%etjL!cm3<@2)~Z->j=O8`Z~gI@@sf2zlIloHoxSr`CVM|m;UuV`46wN^gWJketX}Qf11ZOy!f-}(O+Nm*`J<)4gO308s5^c`Psj+Ro3`1_3Qkq^y~On|AJo^ul=)LCy55esva1h^RG+(+?%PsXr6y6WyjC_Yj~Jg%T@JP=0v6@MdxP?i?h#8Is!+e`XeQ)KsbKSl9{Als0$h@%Q$tj2)Q5`af^ZuIfYSj;HesZiI79;GGI<U7)(=at)@<2b#S6c`0MK!4Ip4Y);Q*pifhXs>&dG1414oN9B}&8J~%dT9ewuFuOrpF#LK43)0^uG#OC>3nC@tHq$)OcQ<0NoyeYe+H2ajFK2`O4tf^eh;G$wdYd$NjD&(=kJNt;AhJF4N*tNU3uP7k~yNl`eZAg8+qxvA6l=r-wo{kPn^KrA)WWUx+THb}Il$;v6C!xgoWiQ^D?(XEic#`n}%^rb>kHz_GM8WgP;EyN6M1{PZHo-4GsBcu!xn2ND=g8uBHcL@TO7>bmUe_7y#rRGwc3W{Sv3qKIGuk`&mN>gY{<`=#*a1ckP~XwN1Ua1l)8ii;|9a-*-R%7Ssn4E0z%NgJd{c(dKfY6c`I4Tz<}Z26^8><}1CBnG;<;h>&$;*Mfb)Ol;LkrhzPL1n&b=8%3h%{X!QSy<al)gsji(B4bYGVqx~p4_u4FuZe&h?zoQ@ATJ7|kD1oy}>mNckC;p#-S^}Za&XFLKSAL_IAC;u)<$wMXCT9%xC@7a7!Z--K6+q{HNCr)Hd`8-+E3~=&R$aDn13Fjf~XE~Y{K=!ymv3I8^c0%+7VHa;<w=S2kz^`|;*t<EU(K#tvrmp}mQ~L8Spyv4&3-D!%MY1T|P}nWScqil$EADqn(4cm1)I4me-c_C&Q_%ncAoyzt_A*|c?jV&T%28Arga>22iQy1tu9#PKY~<w;!_Me7p+FYV!!Py*3H}Z|9xH%NkUD;-j_Ef+c>uV%HRT?}yd}N^yBKu9-x)fh(zgcQvH;+tyZ{QbIP;x!gz)4gJ(%xI-k~$VH8^_osO_0wJCVnBmAN3PHv7MRrB^!{4aWuVzuba<CN*1G^EpWo>-?H;x#mNBta+tbHm~FvFI!mjugscP&M|3u3ZSS&tscg!M^Nc~l<?&jm7?WCnt*@DW>&fJpa0S<Le3kJ(0b9${i&L`XPiz3y1AOMIh6@j9$c%2&PwQnQ_%yDLI@a(5Fpp?9HA2?mq)uVn?%uv!@0vXFSoqX3AL~klOium<EfePJFVDHuP*$xJ$A|7)z~U9RiG9>w;FVrBJ?o&%bPnYkvXt`MrZ?i#6UB;r>m&7h`z#ZPVV%pZ|$*o(tQtvOpVV(eY_2&-WI*}z8g$G(SDL14kQnIvcAvT>p}6PvC$(UbhOO=yq?Exv)+2~KIu!b`X`1Vh!%z!*OQpw19;_i5<QSIorY*n1OI}U2?#d~=bB@`o@Z5-KWo=g^e=W5KswlS=p(=7mLgKW{>OFf1>rR9vgPo%8va-%CYKMPfBYe^eSdropb}Vd3s|3f2p(#IZ6dPHS0b*UO@ui784=f2tc&e{C)57W{hIp^eDm`}k9EKWve^t9u)hN74%Xc!<%6fn0owK(_R+KDfC3T(Y3Bw^IqDFKYwB}!;87JEH*^2cs44Q!TQVw-bkr1{708+#Q{)O{%m=!S76*J*-nmIDQy55u>BBI5FF~%1T`KP2!lwfo#VG}dzy2Vw%_mj<e9@p6-=o7;Ah9M68Hrz8v59&yl77=F4O(A#(=@(JnJDaRlZJL8z{7)=fZ2B=C6f<Qn}*s_na4fVnG!cqnDbU0W|fHOSKh=SDGTA-?$%ePhmE_fOlRd!ZSB{oB*)}-Cuc(}bG<jkG&ml7o)m?`8rh3vcW~Do)wv@3t_Roi*K7L~cQe4x4_j#sfk2@AKYDahGNoj+j&cVFuR|Z!Yf|8-pVWoh1K&^JuDFF62Xqe@&Yh*3nC<kVRw)Q(I!1dW0p781DsS0Yfu2k-ZZtsbf|PQF4FV5p<s_LL(?9q)VEyafeSHa7|KYm?tbg&SAkViS5#)(yaOwkb>cxCslHyS&?-@|_$E0}rb5cBF6k4BC<LO7tI$1-P?f+yp^b#ta!0YKT1^{=hzKKUQdAf>U?+Ncag|N?+dGe&pgR4D4v43&_#SYhq<FIoT$SzaeUVyU$bA1eFPct}sCpdcuA|exn`AI~39ue&;xb}bCK<$6`oq^gPYw&Cmsgk}lqJ7t!l1tY;0cWr39doKAqi7i+?5(RjNfp1I=lFH<GtU`Y*dfkXtqOQFBar=sw<V1Y%GO)vMkS}NV%g&nmVM6ZqUsZI>FnWB+mKfuo$%}I`PVGwr#jN|jSzO$_qal>>vN0)hjR+^7pRp!d<Mw>Z|}7!nO1p0@0CqTD1S+MF9v=`^j`k?^j;m+A<ol#S@&fVqln|YaeJ`}R_VQ3K4eL;v(0p_I5V|cv~_xhh1?8Vkf|dNCc>2;m39S`PwMTDaN47h;Y+<kgl`ef?A~gN*P)icz)(@X%#spm*-6pOr({HisuAC{<t1jEU!peRqkQM{@%P@}d{jpAh;FWlwO?mBA3G)}y4if}$zK#+Fdx4x-5mWNo024r9qHz}6S}z|$}3f<-J%)3PD!J8T=33uD^DXE7G0qA^DJgdYFM@Z7Pr@Ao#-l9(e<_%O1QV8p&KWre`I1#Ek0%_qo(A_rAq1QO@p=;k;-iNWylsO%=iHa&hiTTLOQTzebifDkr(oc8Z>Ryo!KeAV~q0v&97VR%hr*xDk0~deWi&p8uig?z*W39do%7pAgp8XLrtu2CZk^k!OUQ?Xh|fmiRpku?IUNdVkGlRT9K+wde4%J?ieX`G%hLJ>$K(ICdhn<H`q>FJa;w^AumwY?uG=bivQURyj7%8qAwm+z8%uegDFaOYDKzY1Y6bWK+F5r78#OfiiKQClFY?ID7>@GNF#X4jTWarUYyCu|FAxLhKhc+M9U>_RCeGJJyVgQcO!yqx)Ja!<(kt|$M=Gz2Y&yG$)?Wedf*-OY`9nNe{ri#ezt*6&(!fmob44htW1O_Qh~`-11QNXnovxQE*h6klmx_#O&jz+_{IaUF2q@|-<NaOmB-$I@zZx%{qH>I3W>#rja4aHNYHSjIYS32+g{gUb0l@lIA_J|5SiF;83&#!JCm->TAUO+3e}Mb?<bG_M?d+_x6vZLq4Q1YyzbQVo|FHa^SLwQ;F)e-c*5t73x~U(JKW)fNf9DzFW){^k9gZuLSGhMbM?7*KM_9nZ@o$G>_Fb5110qmw>HYqXHub}%tp1npbUdmw9E7~1=ohX=Mu+5<keVajr?vLA+e=|i8sP;91>ETq%F`2PRPi$o52{^K{*r?L&s-F(hV?nQ+}>foy!{}H<RRfmBUtP1B21?JP@+MgB^^fg0)o4OzMg<Zy|}l)CVzfilx8A{gMD^8g0b5@>`}`{D5Br*=Y7s%%VuJIzBfn10wHyg<D&ZA~#oo8&J%Xu*}dKVtgy_{n~l1xdS|7pV-hT=i=L*l$7K{`<^6h+%*a1hOH20<giO&&>grSXQ4dOAzRC~qzy@lWuf^4&kzS39L4`8mhQF+-;_DB=Kht+!92{dgqqBW(80ALkVvGTzRSOUGM<?Z#g121hU(UZpV6BKw~M6rm#!7I8%8P(MFBc9E@cwk)NXe?MpCw=B)tWrjFWvyjF=j+j0_@43Z$*m3vk?lizIn{971M1=l&m=Xum(=B>cqMtFem8;we|uq~T|aq4woj_7AXY#pdtskz3uBjrsryhoRj64KAU~kG{jLW$dnQx2FJi;>hjLTl-0Qx;P+wR;JgUJUB>Qrf*Qbpu|lBDE?3txChfdw%Xic<nEye;LFsfV;K&`ms(@~-Ef_5Gi)-vqARy+Q4i>-Ze*NRUS^QsiQj#}{?@1AYrgwMPSYLItC8I0@fJ&<3#f%BPL5CLfTIRUxj~D!y}N?Hg68iM<#e5F0&Ix+K*Ol;ig0&J1{`d9gCH={aK^$}OJFI?XzFH8(uPhFmcynxMvePOHkhK#-IxM8V6N;KUE}&8eS}}{#JRHpZyz%9+*|UkWdUzT(zsjJYskK}UdFxM%Jd3ibz(kPB|dvS;k7qc^`%Zsh6huo-FZJ|<&7}t)SGFdh<G~NG%olw(5|?E11URFo)I0=!ZDxD@FI_T+cf!!j?Qte#;F)jU%@rmrjn}Z@<Kaj<x8VM9OqP+cn={N%+$@69)S6u1TkYIPZ%@Sw!LVg(HDu9c8@2K^Cberrk2I%rBf3<gnrC8(&4i74vm}U)Yeiu3o7YhqRYTz%8E%Uw#dlA{Ds$zcoJ1SjA4|Fgm9Acl~QBvF6Sm$GsJvvP3LVtkGkLgn)t6Ta=U&!<Dx6`?pv_Mi9Hb&drXs;T)DY26NfeDxM1E*am7PkGyDdnMv&|`oJrFwNp+iY!CENf8Av1*&i|c=hXzQ;Xq)Y|yGl5eMW}n~)k<}tp*teadGE;ZKHrmbs4Zw<T%n!CT==ATFjw+p>b9&;MT41VmdC!s_^<3{;b2FCj-x|W8z*2ACK0<Yczz<EZChm@1e<~<xk5qGu<CG7y&!a)ywPfK!AkP<JPn;{&RN<2TU)Z?)f>HlROM-7(E32NOYJ5}h+^X!^SO%MWYLNIpFd?)6&8|7r2MSH%7PULPpx?*$cxX5@PcH{X{sJeTc4rJ_cJT+3C>ffmmUfAT%~=z5be#&E9;-A@=E&uZ1Qed?R<`~?ildx$l}&4X0DmSbMm@irb)7KwvTU{s;!=+wo7pCD5Ie>#QBCUi6Pt5k;~rF>n5wBT+)$-9HB=|qh;Yd=?ntx87Rpnz>5H%4T+2!k<`;e#Pv}7g1bNS=1_qt$83_}KfAEVq-_MgiDEmdY?II|BK})I(3(Z;xQTakQ4Jc(fAehD4&x3Br>oqQR7@!#WesQ*ENaq5kTWtOV}{G#&#54TGGpCY26UBac$;}u5#)$Cf~r(gT72bv#gT3uD*EFzPe&yi?Np={Ux&(~Sl!t0L8kn#xF37a35}xf#oxR}G4EQak_`-g+&fWw7Q=skaMA;B)epKS)pl22IgueoGGCSGe8uc}bHI*y5RM!qP~kQO6&RrDI$;0WQ!%rlNG%>Cx)EGUBytI$w*%b88)gdD-uT!Ur7)%yn-%gA;pY-m>4f1fk?zBqx#Wa0(6>>TaeFR@@{M;xG0%oHXoEHI1uBep6oA<#@@T<LWkCd&php2{4(bZVHEW3Qy>VwzJaI!6GgsUA{>J+#k&#C0ydqPKC&<ORAtsPy<x?JM7oVxfgvF2@idfBYm8`K15iiJ<?%IZ=^w!gOEXovBxXol#CIfC}@w67ooQPX%?H2Kgxa!OiIjP+?kJN6Xq+%ot03>6%L33fG*v!RT_R-igfDsZ|T?5+e*4Bxz3uXwE+N6*m#^LHGV!!*}KcutPx>5A|36Apy+wmD^tx@gvLKYs{iUf$&iP@c<m`udSOP(5ZHhdh(rB%4qti%khLQgg^r5OVlz$HY%W3zGxZrr{VyDlP_Rhc{dY!^?s8N2Fyd9*gv_Slip949Sa+f92+XI^&6n{hHW;gA+|=Iw{2GiO%8|MKy!RL0`&+^$r7m?k|OglkR+yUM?N%KGuP8meZ3NAbYr&7ypneZwAM&I7k3Yz>3kbx3suA_N9C6nJ-F<n?LiSJ>miRuWhpCBCEkxNH|q_*#N3XrMG0nWPJ!QAMy!+fR6a=bJg1Fm%VbRhiTkCBCVHsj02^flw}wch6WX5A2(XRt9bp{>r(8BzTZK;2tLr^tlEvz&OKRNMma=GW%tJ`g6AIBa~Xd6zR2c4ZHJt$lWMHozKc;5(%qqTvg$n`LAJ8g)>k~>Woz!dq-mo=JdnZo+K%<F(_^5Vm?O|8QO4`QQELC1pZ4iX~VS=%1B{7a8AWh7@4ZbRqPULqa5ACBCLx?H~`jTC0nxF&*hQVl1ENd$-y&6Gab>gtd0EjKPHfxOa4NKV#ftYO~unB2%j3BMzzQasWDih$Q)YM{o~9{AiPG_xRIMMViJQ{!izeNvdMFmiKarls*a<#fWqQ_iE}rGJw!YcHBbFm2EtCHAyXg6O_j}tzp(y^!XEz3pA2W=f*=Ye=1{Bl?r}jBItvt;YL6ynw~#++!wFuN+9zGA@uf9In4HZFENfpa`JSD70)Dta$CenXY%!Kh4kkvS$rzD4UAu++$#cAh>#BTs$z_-;pxn@?RX*vjjMwn1)*QXX&QSu!GJxpn{RG__Y$%Lnoly?Hyio12b|`;@eOPKB9Xp)|61T9C*)+Z3NvJ=X8++%}0YnK8wLIS#U-GI-^CI(d3t`Zmf%MV-e61cO^5T7LE!cSH!MdKAtmVb{Y99|w&|c#!Bq3%eG41oR!tSh__gd}Gcj}(T9`u>V?MF5SU+aM&QKjBmD?)F1FZ`g<vTSds0>;+kU=-c1u{o-xsoaPV{l@3=r=BJ2T-M|RcS0svJNRF&*VUCR^Pb5iDF`KUVRNZtbG|by6Ou&@m0+_JOfc7rp}CW0${kE`Pu8RL4u5?>c@ZbM+v8SlxWSpWNLfW|%XcIBjxun#-yyBLR#%xaHaXmG-M$OMe$u|-cOyBl+HmQLUE+#)gosMk=o*B*nx;8PZu#{7WA_*R`bTbf@C~JeV9?4V{E?I#6ZcQKA0q?J^L~oU|KQ57+kbcPoM$Jw@b3-3cl-!ltev-?aBElftSiA_U|R30xoiC8|F(>l9mvryo^Z#m@!9o6mWuHXrmSag?#Z>?;4-2e6Z*SJ<u^S!8mG6pC6)z{gXMo{KEx9GUKyo7`_?pM271(K=}X7zNHZ<FaHMal7tMVy?;JZE$5bz!=gvB`qC97AL7Cxf2_U*1n|N%)p*Pkbn-vr-b(8Z9b*))Hf5Xbp<Tj5OP$_wJHtHzrZ_UNmIyvh(N0vZ~=NwsNskmc$f2W>vS!<k@+Z(L>=Fh%3nmLtGW>$HQZas}=^0T5DhBA9S2QO<q1u^XTwK%4+7T}c}i`|(BCY_037{2slSsdQ)B7A9>Iq#=Qe@iX}v>v!+_>yMB&%mX>3%6s`a%tdG4Owo1iNQ_%!5<UF`A1q(q$jfsS=wiIrOdkk=8Y-mx>CBSE5)R;1g(0aF(n>%rFiQ~q0d$uQ(8tc9SiM%Wtn;-d?WOutSDWM=BTM3rJ41kG|%Wqxmxt2SeO#uXN>YcKWd7<9PtVfn-l8_pX^AylB?K#j8AZ{WW!9dd=-|&E6i*(&bU|Nmn2&XmIjHc*Rt)>s%tE;^-~@BQOYGY%?UdYSf>&qvJ15;O=l7@c@%sH5F*sf0%X+7I<4hk%%HWI&SSn60xCqdVj(UmSIRs>4+SPydaqL{{puOAr4mf^usG?y(ky+WjAi<EdBXS1xZMalS{!6nxM1%X3fwZhAk7k;D%g=v)Lrb1kRUM{=w*Niq%FVR5;p5Aw}F^S;IsvC8d)%b?pgR$;qC_7CfCX>(y#Byy>xwRJA9>9VpM!<5To*(w|sHSQz?e9f|5=}jg)~GgPCy6+lhWpFsv?Ybuf%@=A~ZiO;<<ewj6A28cO)>?p>~DV{)EEN@7v^Yd;wvlDSy$+iMMIJM?zdV8|*GO{mMehhgnFFe(&KMH1DrC{b*umK2>C4?$q-M75ig#zl@Dp`&hRB(Fr5R8bRU4xGq#B)VhI3IR>5w^}WNCke<!B)X@;1gNnKpsj__Ag^|^2GEvWe&a@f51sw`TVHBQ_H-yeZ1$^zyBRN)%9cJ(xA1YE%6=Uw|BiJsc1BG_vZ-gK`Z&)_ea#_E%?!enY8otB&8!;}U@xhet(E;MTPh0sVR$?N)`Xk%l}v#B?i=)}#Dj0jO<&o(Ygp?xzLzU^Lqu7VsG>|XPB9^pj#VRQRuYKoJcAAl=+`8dCom2Y9+CO^7P}}*IE-zsk|fiRGikgM4WQS}1PW7!n7AX(O=M|0lH(+iCy}u)8g=%HnEn-!iyiS#s^O{M#rSwtFsro5#vqxD<~k<MUv=0Z1jG~OR{)rz1_~Dc*p4H?-wquj4C}o5IQc;*RwMTBk?x1V6zrXpwVk>=uvQvp5~?Yi;@TCR=CqZ4#5I?Rx#Il7E&SzI)vx!Z`W4<x3E}nEHx`k2{q<Fq?p1H<b%b9Py<Qc)UKPDw6}?^+y<Qc)UKPE5>J+`+@4s(H#Y-wl<7Yukeo4z~*?v@h?$o)LOuUO(<IEpG5s<ERsmD}nnn_pPxAi<>F1Qrfq4l(cSGXYIHMmJb=}5vWyM^3V!?O*76F(v0MM3#5rQ$W0ggO=?lbF?TS-&e+FjhF0z+yh>RDg?r+E~dYAO#y2;$7h>@viyB6SYKPk$R7_TbN|K8W*c-&GE&bj4=CW&R#j52&ZBkg}H<zi|Tfn-m%*W=kH}9*tJmW8cc}nNu93Q$4?JC*6AYF&6!RYo}l`AtU@^l<cMcQVs3h8F3jcpBz82HKYBz;$XD4bb19cfP`>^enu_^-RB!5$KOO5(MR)Y6>4iUj@q`@KIZdSL?tI;+9+Bz_)!@JI;x8TWqQ43jaq_2d=7UGq93H)+<zHQLkIQyV%39&P)|RvP!}!i93^hOOu~W@-rCxL|HblP8$)krGo_ew`)Giy}eEuLmuEAyRkV|9nPCPf-r-Qc84I2gPF6eQM|FU$otd#tv_bklQB|lc~-b{&W_fD0#QtiY(Bgw-WViK+491|ivo(WGD8sb{gB*xRREWDm+aE(el-5S87u?V~+8^3S{`BD*h65uiQo$f>ROa4ZgK27%dXAM&c_MQXKMt%eb5_5RP3AG*wZd<X=Rh&W~_r&qR0eG<ezC#6_eblRoV7c26?XogSn=ZNGimpIJiL!h&U!g=McThYNdp;024VwzXbcRM3`)W26Y|MAQ!LQ+Sw%${PBe0PtQs$uI$`kt70B$!$3MaOf&%t{Dj;Xv7!VF*WU0!6Eeo)#IBV|*@0SI}61@Fm<3eH)y)kLZ}gkkOE2qp?}04z^TM3Z7!Wb#|0omo7hymxlgB~S_wPL+-H6zBL~-ca&lb8e}3XtBPy)Ei1bP`=@O@6_pPUlR&ed#7y8r`c*BDM;#qZ`t}$My?A+lfVTp#0ZyMnjuE!3w{veLS6P*)C)%op28s>oo~~EUl|CDG96yD3PcK2;n{d3!!=`2a8$oVbGRfXyimdrJ7{1YZiC@WA;#672N|x;KtaNeCZPRLCg2h*tP1emQ@h|>nrJl?crdNKGFj3`)H*<4hG=Z5l2Qi#78*3dW+m&$kPJdak1-n9%UM3~yJ!ofz6Ys30IDEKmuhFqr~Gy(>qT*986a$rxW613v+4ASeS`DYQ3?=WYMdJTs=K!n8jwnPL=0LZT(T~bva^7shzzr&L9cg#HG7MVMxuVYhT)FHVbp}q_dtGZKws?3<IT6m@D`XA$Oqm<dFOAxD_9tI@{1UpZSyi>A%K0B=$n3I6=KX1TxH|C%qk>e={coPnJjI3j8BOCp3fr_I$=xml}V_pYU7o#Wx<?whAX!6C<qZl6p;jTB+_?|Ev*wn7a%#!n{o&(K%-wNPKE#X6{PVB(s;!Zy#D&S@Lxyxb%bBh8c+Qi-r(b}fQ?tc#w%ds6|nIN*mwnOyaF~}4A?mNIl*aI7DPXd5$pud92kq?M&c`|1~Ns`JnfC!jU<vrMebQ#U%5)DjFwzg+x@Kmt`hUp;Eia=0jpLY<2S4XuQL7oUpps}8-6Ur=ZfXnNMPn7NQ0bs$L}1WIQ%&v$NVs4l4d8dJIae=bZhhb@|8?=yoT|+eC43=wX;X>%mEVq2qUpE{&S|h{2bb$BfUTVw^q;X*9qy7=5PpK)9*8Y$LyvI>7kpAv)g?72J6xrM`?Czx>F}IOWkH?pqC_|gkNGjj7D#K)76ep7fx>6j-O64K~Sdm?H<F3dtq+6qCVouEUF(daD|_4cD%>&uBQnstjLJLFt7>{Ba&=qsxmR>iXJQLzco<D2oX^MUDfmXzmI?@?B5Zta30SPj?fy%AcrGhNqPd>;Y_@KiBXxoS*QBqfTJTHhl@Oh6?wAg|LC1Qc7R_T@W?GZ0k%oAlPnG+QS$}RNI1q$od4_5F(Y*3XnKqX9L=R;07C^ixHJJs#=m+$VN3iB9pU^LAcUU*A&xHK5scIEy)OVE;mPA4!-vH4kg71du;9;+`6)hUoOK!~+-8~vVFYNAh#b9?^T7$TMg0hp#2<l4{1Y#h|Au9<|39;GRM|tnceWN)3sLQ5P0f*bsPS=N0e-#Ux!I3un)$e}jH(p~&L$1GzVo3yqPL+c=$cL<*q>0Q>XL02d5zB1iPeVmP1NimN?^sZwkQ1%p$4t$$&FB`o;3YV5@M-ESxA~d9eD*3nUA7b`+y256etbQ(5wv*5>=ZTy`XHqgJ1!vov5X{EHM~V(4?Ml)3AEPX%hxkjMg(Ms-{Y;iON-s2UR}9uu*<=Em3?Tb~JVyn&;MmG4IE3^C4gH2}8@}h|ef086PF_S%p5N{)b1+kAV0tkWs3O4GOKZhulWW(u!1yn1D74Q@P+Rnm^$Tjs{6BkYLIlFTu+eBG|L-@LSIZ8<r0i>NjgV(mTzv@qu$jQzAF6nv*Bl+cON$eTIH3j)bS4A*o<vQYkRTT%RO3{r<go@+8M{F(BHZYY1tXi=~gxu#fGkKEMk0njYYqPY;sE)A~%a^_g|5pw}_3pbavv%q=~@Ef*)Wv&c4s5-vEeu--E2_gt3kv>I1cG=mEgHFjHsLW+P7##UofKDehJyIg+#z7mE(nQMAhYrXT-gKGWaDPg_+^Kbbn&CO|d?y=m=p2_q;Fl9T1OC1*#%k#tT%+qM1Ye=#OXMAL8!^GF(aSyy>jC~){ii(9qYaF0h%!RSRLRq_TbL&>4#4in3K0k_e2${NBZ2&&H{<`~@pG(8}b0E&>z!wGr&cXS0jKhr><D{B_7ikDxA4Gf1vj2ht^XyNVuB*;!@8^%tz#0W-o&l&ix(e(ZKe7sUy)=*`q)9^<t_Ue7vIMXdXjYb)kB0;(+-*4UNr0-GAwW35!hJ5yhI<4=_|pS{W)d#S5OyTwjqyku!VX*4+QXEY3>_GfV*bN-#cv1hmka!M(bRyRPi~h<ZWos1cD;yJIu1jkc=ZXn9WG-={6Zyh;Ut0<dgEP<%w`&XB)ZF$3ML2Rx*Mrr%xMzSWAg2!c+a3&!a!t(iN_?}BOc|9l3zZ9N2$Dbt&!eE;>Fftyki0<i}Ws#(C*9e-U)Z&MTGm6qQ3i;XD$A62e&|1#s`4QHf1(#NB~vl;g(w(7~Lt%bSoH=;o4RQ6MXE5_G~re9N;{J+~ZU2RoD{J8@QJRV@i+dD%^RXJy*o9^|vJZB8&_Ip+I|Cgq%sVoDO3X5gd{x5*NA&4^0#u5zwJ!PujrNq-txVSSI|E&~_#cOfqAS84-84<jW?w2tLf7i98cwj6gt^fA_eT0Gt{wU@^?UG1-F8-gI-a#m@`ea|pW^EdF9CidnWDOPrROwUXJIPve@mtxIHr+)+}@tu6J&nJ`zdU#Xd!xQ8Vm#ZFf;_U~L*a(BFjO;wQ8fN8Z{oQ}Y-7Qz<Wx-v1&*R~p4t;VbJe{~&}H;GNQrI>8_t);cl0J7I=;ic-bH<q*7lym-5FWU_7opC%$zN18A_dw&099i*-%-cfa-EfjMntXJx%B!33pc@4ttg=>?%uDqJ9zur2h<*5&2RELAp$B|c5pce9;#WHm@Jljq!luiS<j5v~+c?+;Zfh%UiGFV+gO!9FL_#FCDjN`4(2KA2uRUv2u7G|NCKwuaYXH{s1C*C?Q|6*?b|v@(l)dSElcP|-nL@FU6Hny7%{-<Fc^xQqj$gUw5N+InU`!NGU58K>*FcryW)&qn-0LfHAoLMBJZ;MZI*>9U9`aBxw+}Y1X^CTv*80#neuQm``4D^RIpOsHqOkJuuE(ho=&b<AZ2|LkW%#kmGGvom>=+Qurdl6#D=15W71A>NZV{F8O(4}378QRnUjO+=!RP0Y=Q}XOU7&|!Y<~(nFV6v50`64bD;g(p%?oTPF+<*}In>;bN`TFTGsmLN#F@J}&YWVu9loOM0OfY&=C;y1BeRvk%R4&Em1cB-Enl4jme&eNiCo$+2bP~hl>=<=nx=xux8YX36bxh5dBIrR9%>+1tVAR=+tNxP-1s^F+d#BuZXP9a!bD7AXc(qM_X%k_*Tn1&9Uj_uL;4eCzLs@DBRDYMLX{@J4t|X|yjXoK>P_)pQ-rWNm!+P3nF8M#r+}zaISb0{>531(FN-aaS~N*mr99$+^o?JD&OR!uEkyknEmNI-AvTGSJBI-?hp_MvzKD<jLTQ3I@Gr_qN}Sr(4i;a+wMbQ3M&_z-Fu=*+TJr*IlT$cE&Vp52d`@%^E0xfb_8NTC0TTpi_J(1l%pIl|8&R-4VrnpSh!RpzH2|}Za%^zQDJK)zJHV~aOZ;-{?SRgp0ob^Bov@JQ^*5`_T9*Ba=CT-weZ&+lr`iD_jTbrbguxV}8*tNNMrP_<vNS{=g4U<2wG_1UfY=RY0_=<2-ZHx+THJg3Vg;FB0o_;B-7UAlh&KKb%O9pOiK?Ib8BS-YuhM|uW8VYcf1CU!K=CUuE#^5TJhja-t$LYW<)*$D+=i5cU&xqpf(tN>85=;}eyA0|Bxks%P&7ZK`fb@#z91WL*%rR2Jnb72yp}ut!kIK;H@U3*#&_Yk{?)f1T`joW%}2$YTQa(r1J=n$e?GUWrk$okS5fG#ZwGU{cpd#Qhq$?1GNxU{_G=n)Xv^uFVT!Txs6%HB*w(R;jwm*l0*Ug&nqa!td5Wke_VB(gf>|tOws?-}PsdS|rGf6KOoKt%!cn`fj#{F9PGv=`C3Ft24vjqr5gwWZqU9~f3H>Bc-+yqR{%^c^kG|y0mv^=^-2m!km!Mj@0qaKmtxxUIC`-FM>;DXKMh*`0R`cXBO*mT1Mlj4BxnN03ykXw(X{InzORlTg<peRiutr-c9Jf%_2;op>loLFqJy$d?UgY*70VX3RR8dd%Xl(o98)s51Z)UAt1DyXHZC-$|6TueU_}N6zJubHCKlj>H@!AdWill!1^>u__NBDJwU;8ay*)d<6Eq<CC0$w{UUOO#bJ1u^?IxVQ2^4wMlcdkEUeAB(Gd*edag^6&!u<OG1CenjEv;AV$dx5H92xI$2a1vMspu<VPJ%~@SO+k5bBoZW578hih(a)PL9_h3=ZnNlx{5t-zbho-6>H%TvXQ226+vUWSc>2z~Ng|ChyNhF%1ewc^`$ap2^NZ_0YU5b2Z<5eX_4trxy(xQ;m$=~P189HpBN*RLT?NbA4Be~;#V^NUY>cQfQ*-{yc_W3JwGKq8UfV^EsI`r!3h1KO;q-!!Sv<ojYiaQQ{1BZE{_(HJ4HmH?;*Ams-wfTYIjd!u(_79v72FKYe1@?voOCBFTM$Ml{ZYHXSycXW|CG-k_B0XZ3_*X&ZfKnc`S?%AzrOtXzYH_w**=epgp~d<p2fwR-7|P7{Y7TPIxE6)4}pJ-Z*mTke<lrNT+l9_Zx(qewdC~IaZJ)ld%@VvaBfJ=4xBr{!sq&@#n5>d)A4v7jn(|udgDj`>L)I137`1i_Nu<-?}H~Q-*P#ZlU$>in7#cBe1g7B8I|NnI<AxlN`MQqn-bt5nfvO7+<-*JccwNLMbo8g88^V-P18Kq7orRG1CYcJ+iHmV7wHolj|j>$a^azpuL-^<`M_Rc#KP`Kr#A5?L@8lq+BTRp_7!wA{zQ2=^7XNV>tf}n4&vp*F5)Q;?Sn1-Vo}gDXBM3hg=jp#L9h^M(WAr_Bn{8Y_*Aym>$BXN;>ZxnGFI>^jD_TED<Cp(zB8cDAc#{KR(VgqMYl<%Qyv+#!w7rp#KdZqy9n&H4a;nMNx^oo`d#v9;x|1@+`J?K%*Hd@o`zSkClE#Qy{NKCGnyA4$8!QZ6CaWW3f24Z$`2mU9gRa8kB@dGk+X-x7S*%LBC|BnjyFkua3o!|!W>Z1Q4mOc1PZ65FAMcfJ*S85jo#q>qJ{KT`n$S#0343(mq6t4-_QT=cLlobOb|UEk-ZVi&;`HE%Ytx-c~0Bfg;kD1egk(Ke79lcmW4H<@_?7^8<D;70Y)2RddC7qQZ3x8oCm~R?lf|!+|6OQiWm)V?`vBQ@dWaBg_DA)bXe4i6H#CM5)?AyNI0L!!CBF_d4%4^k^b#G?)DrH9IJ$e<RDu&5fau(DmNeI0aT+gS^+VQ-BoI-<yYkBT4KS}$6ECoodDrj!98(+jU*ex)fzYzz;^I)WZc%M?nW7^=uFu7V`w+R5^RCU@hc%14bzOZ`vpBRF`Ft0QVc-T<C4B$nYtnLp{eC)Mtw)c<j3mF{xQsiPyep_u^-Cte4mtwpHz478sP2$yG6<ywt76^n;))WlA4s(#c=PTF$|zG^n@LVUk@M$gzY`}J7=Vhgf5_pKTxEwOz$hWmiF0>_5wzYAlellR~tad7s)*ODHIC*kc?Hn4E<i1B7yg5G|PXVmy_=a>ZXQb%kx-wW~jZM9hrn#)8<xyHB{adn_)Swty3PzfPn~z)^MXNTsxxIF-!a8^8jX0kCS+Pb)s@)>JTe7fI<QW18zy2$wEA@ouI=du}cTb>v|Mx+^}aFtI9YKvC;f9?zg$Em!F>p33R?9cH)3Gok0+RRcxJL)%f*VTR9)&P!k3i(2tN|7?K+{QA=wJwo5c{WbSBcZXy5@w4DGPfa5b@?j}rz6`KTZ4>Sjnu#>@By~@A$3AQN_c?T-c!8Z-DA2c`R1(<j{-|T?{xTdZ|zXPu7z@mHmK$yy{E&H;t+lCH|2jn9jc%CL|8JEXW9Gj*}O$3fKM)42cmC>F{<Q{j<`E^rKJa4600>gFGFR^Hr=*~1th^LcNXB5h1tK0?SEU=-dG^0P)8qwCNe}d(C$~aG2xrAQR-eJW8^o~J}B#kv(Pgzncpv0cl6j9E&zT6Zs^7KZ-X3v@;DB}Kp+ac0F_I&tv=8}(Pi30K+heI^JTv1|dF#*aTeN^^`9pJBfSDA0O0CG>r?R(@&z__{v9Ev2^==PFmMmo^@sRR`dH6%~>*r~Pxe$%LKYv0noZswU>;T_)`^px&lLC`P7Yfy(@y5;Qq(`6m56pWPT@e$YL0Zh_4r!AIeu>|-j>ms*YlVuog_=599YP{)&u}lj&4onF3u}20S<=-85S^A?m|1}Y#jF;nvMkY|<y9w94uCi*ttet=!E%qU;E!CGv-;i4ZEom*W{L1&{aNPjm)CrEdVw$j=qy@@xP#}{rz-!F8&=XaT?o^=7p=cfi2xtG8$aNV(@moN=3?r0iFPg};*HB5CU_o|;gk}ekUm!yxfarlP3r^fYl^Fj;Hk_3K`pq)r?QF<f4teB|myte{Q3rmG)~{GnM0m;HGkwV+7mgD{euWN!SO>djGO6bPBzC@*1)pv>38L%P9Q9rRSw5Kq#(q0miB9)TrJjs`n-!i(j~&@1M(}u(aAW;f>>CmBRPB+RJpR{*N~%G=b9E9sfq1F7jAQ&71A}o@^ES}6LA!n;L$FCA)7M06uV*hZ@y>9AJ)c!WEHdTeskh95W#)_quvlPhafzrr0@8q{1emRXbz-*=?Q_&O@=Aaw=Da{c-Nk?4xe+_i<7JTm1576TlW={&67nmCz8H<TPqWlCpHi{$`@Y6wQM~WWSfgc%7-qu7#~40JT^l9<ogF_CExyviEw(ag(U2t{vlHOpw8)=l#_&WRGD8wVWpv>_Nt`eVOMo2AG*ceKk9E<~M~;f_()4ep#(LJ0XUvAyP#G~fc@C>?I^HM~Mh1mA2KFmL%0;DPlpzWZ$8W43sh_P1PBmbz3=NFKgGI31w`o3{ANgrQJeCcqG5>f>Jz=oR2o?|5AbI-Wc)}3;?1O~v>fmmSfoF%U{enuzPFT|!7Jkq27Z#t7Q8Ak`v^6x&z9Noa%A~-)2K;`^p45>nL)2tLlI!@o4QaN-`gJwS7vnHqYH}8vCV@lsujNzrHFJ?hW|XnD*Tve`!66;9ROfg#W{NH<0a(H1fvgz)KX-v~9}6qpap9Kr@$E{tUqYoo#{K)+z*wf<0UpdibOyHcJ1g(3e7L5Yos?Me;Nb5hesOQzRM)JPVeh?Vh@j3Yl9_MGXP@qju%F0!ywlxGNbgC+3l<n&Y`nMl44esf_zDElyuu*&5#9<sg6^K#2WW*vx-e>HWDv%Og)GJ``!^46ly*x>hyNeujTay2(`V~n++6U$cW_HD>R%KStv>3;Z-dWnW{GIaT1N5bg)puNnwi+>#g5OeT{H&~Z(i~HmQPauhQ~hDjaoP>D<wA3+VbU}W1EZA#mRQSN^Uvw65!O|^GGsDozuvP&UzuNG84=G*xLml1~NlQtGZE}3NM~X5;Pg4U09Q8q2X6F>JkZNylA%}{~`~+EJjn)@SdK(U7MfxK$X+>xB+yh>91tez-4c#8_4Kj%^iGCwEp^%uRd7SiY|HuV6QN4{WyAf{T}`He-R;f8HOLa;Uli?Z!j66AN0PKkxs*d%lzqY{WfCG4qLVzmH{d|GKh4_zU;3We5ypUp7~(5Tw(4%u#*TIu#zqtI4L3nDC69%IQ!Vg_z}mTxer~2hK<t7fnA)4;puBU?9g3Rer_DTL+ooCb{6#ktzlW5ETq%8rsq(e*wr41^#jf+8v*UYoETs?3`5Jn!`pJJ=(bz+hlI_p{MEC|vD^jT+25;Oi__`~*@T^Xul|!)$owm0{uK=S`s?cmzmD+h2){z+Um^3akoi~0{3~Ss6*B({ng8PsnI8e~sLtn?pyvI#H&cDld@!v7Kc{}IP^$%GJ|02liLdwjU`S_P7b@Z^O{|!dL_U=XFP{kJta$m#!#@L1zbCx>^$A}7QCWghr2N^Ra+`ikkj^phONoW)vMU08<nCJh2>;RxJ2e}kD<K%8%0cb|6n&1Y9}(#F7VJ91@(L$V|C4z6d<?XoP>9*U@_LaL*uP_ufZ02y5TH9f{nwq92M9}T06$kssM-K0IQnpM%;L4TWj^~l@;W6HIRFx3%G8=m&f@D&!~o{_=wq1qIrje}Ncc!SKZn~t|KB$Q*N3O@^~coeegfTJ;=Z4N>X$F|5wLuCO91>?o5Ev2`{zQ-PvG{afbk=!_#8EV3ba2(h#!4+{PirJ{i2$}$@}x}2Y2p(^U(MTa)0C-9|zYzhO7^jI)AogSb;hQ&ihj+eR6Y@{R~q-7Ew>%tUrqi!L?^q3*~`JB`ww6m%Kg5xeo^7JgRNwt6JD{#^w#?Ns+R%X-v@apgt8K0er=zdzS4b2kla=aK%}LE3$eOwvb{bxv@Y+eCG4omI~X!HgoT5eU#XRVy*hhCWYc;n)k@Lip8u0Rw+FJful>H1woo+fIV1v7BbDZWD1H?<;x2tgJP1Q=0js(e5=H(076t4F=MR9Tvfy430?EGEafRiuTpebM`8l(D$$U3B$RXHoP-H2Zub%-B8_2K+xMC{&a^9fdt|<jhF3A)lT;tXYJj7RLOEI`jVkmk4tkc-NbnZcqAF^fN^fD-QQ?76g1bb$_Nky&jy(upi$YY$wV}}-Vi+NCMoHU|k-WlQ-cwmE{^7flPM>2lPo&eE<cSh{wtD)CIMAhf`mQJVt?u9xh4n@CbO3@nH&ah1t6CQ>tEVTHTQ5ncvkzlZPZ!MGPsHrW2sjC(@%6O_yP$xXaRJP%0_r-I_&beJD~Prc<=<H4!sgQHEWc}2ClQ&yk$U=SUIhLssi*tjf0UH%0%~CoZ1$PCIr!LIMlBG_v~ASp0Sh>%{yT;#RKbRkoh{GJH>@&hyd#Nf$1`-$W^wGPFpjpCRp*vvUYXzq@Ce|8&wvm3On~SX@}Q}-s!6n}LHl%B4K3$Z5Z-qXxhg>haC6yr5zUfXUv;#+YxaT|(zXg)&@w&&h!?oP*p~B6vuPz&1nU>W1wTsk2VClhoK64Mv!FxYBE_dqpOr`b5XBu%;`118D}l0&R?Iu>4it9)Re89P)Y=$9VxbaDgj~q3%4ej5rLsB`-IMwTC)ynjTL~W|-c^1i-w6^M_Bd5sT^n+HOM4`Jw{o85mXnJl$GEB+Vjan7ep`n8mMvw@pnJkS4TeREdWLZeXnz7Wg2&tl1BVZ;)o^r8zcP>({f6QQ!EV_gPW)>iLwrgx-`HP!5OrJc5@%0Lzg3oZlYRafVi(Jv@-^Z!(70ld%j@!!Ng~*~ejU@M4ln?^X!e)R9SG~4bcg`YE~8|zL;z$t?yvyR-1uPZ*#mkhx%da35O;x5d7y<K)-izE5=K&Kqg5BB{UP!JDW&KuR>hsUw)Q4<a}P;SSvA5Dl$ebD8%>@XIv@%80-G9wn-xFa2`Q(36PK=aFu>V-kqil$>AU28XgXf-3jB!W3U|R0aOfxD=96~(6H)(7u^Nd=7w9d(!%16)tniJ9<YeDoneAQ6`QG9T-OBK#<ry}a9Qx%V{^><8Ofk8u+6yDVY%0!zFyxq9?W`T9y9UGXppCH{{;As~x7*{AyQWG7ZLAk2`^sl6PnUSWB>Z*^*U1e7`ds=w(^s@Gi4dFhfu^;*c_+v(kx#(glN^<{tDywQN)~(Icnn~C$EN_$#$nx#czEFS{0hCdF6~`cb%n|q)yf*Eout*3f9oxX)@aLWoXLPaE)q48eqT_CYN-$vM~$Jz6ry0|Per2KQU)xI3Q?Z@Ab33r+rVaL5mBSR3KPD=IZPfZgCSn|Myx2b4Y6+}R=KY@3Vlhg0jr{HHA9bXUkq*Q$l!hQ(=sR-wV|>^0sK~YOtnWmEey5L8v^R<TkfBInNYwTz8f|MOs{2z;AtIe1(csPhODFN5<9urKUeio^A!MP*TCoT*F&H?Od#kz-hU7eds&lv1agA$4LZ2|;l>Tt;z;E9l~BLf#XqJqo@MHA7|&Ubxx*R0i`V?q0e=em(={B1K==7mSQ?jhPK?2{0Woih&R5H52-`pTIC{Q4LeF<>G@*s?<#ofDk!=9E=K*-1jk%ag=vL3Bw>k;z3hZv8WWk#71BuHcdS)^9Ybsrd5?vVjSX<i5kbF&{ob<%PxON1f=NAF|XRvi7&Raji@o6SS!fh@-AiZsEaiuHQ5Qtxn>;)qC(@$oDi*VM4ATEbB7Ap7}Jb;#+n>*F-*q$v!dzj+=G2dSsU4v2+L|xC|*P$Mtj7cX5x5yYd%p+xMIrF}v=VNUj9Z!;{uU6d3U)kv#C)jt*NCb7M*uOT3xN&x2I&2KskKYNi+>c}9(RhY1eY?K^C8yz8zL{s^FuMRh5A7AF%LNXGo;Lt}nEmU=9LVw;t#`ThK2P}m;Kx3G#cB1Og(TMaIO6QJ3vvs>7~{FHIEnSpTYiTPeEw4xez9t>mWT83-@9k_xvW$1#Ny|(ud;~%C+|8Pi(PwR<ej|`WS;!<43L8@(<%oTWSdP9KuZusHLQkJtc!1I-@x2YnwwORXjR|x)=?}@1T~9e@6Xc-J6Oq(Q%#<+CxyHNf$g3ln!bQ(0;#~GV{DG7Lx@eqDNR?!hLO}&o}<7Gr%SqV_B&HpI8f+2R=$HcYfJITP8-?iEAK9)+Q(7<Ro~TUbwuls=HrtTo7Bo-y?E0LP|r2V1jhS{srDY`>3Ee*KL4Gv{SDuz>vhlBaZA2($N1X8A0Niuum?X$zG44U84c*zplLFW#(JO%U?c#!{Cj1*=bffQWSmZi01ovH_8m>D;3!!`pDGWbZQOO$e{Ff@2pGK#I>|}229(cLvq?1Z53Y&?nHUB-<;nMf@NKmju}ai3A}ALVI0dxEQfBc^c}*@Xww<Xhj%%!eXE?X)W<jDEW%Xq=THfuf>qSHZel+Fv#fnMx%rju}P{gCvM=YPz(ACSeM>kYqhrrZPi9GQ7ufD6!>lTTV<Ln;d1a$Hh=RF_kC(s{R&}B660LRYjFp4LT$Ia9h87y@ax5|E*<EwdZY|1kU1?BkK+Ig+6YI-QRwqpqeX51zf1qr6poxnbSBBap5YqM?rL`Y$3yKZZCFHG6JNk}1I^Fc>=bIfldqnFeiy_Vt?{jXaVy~7z5g?YkmeK}#b|F9{R?>sJ`^L6jO4yOM}K<9_=Qb6bHj|%8~`w;;hu{KoooWx*npn6VOC4E)TNm9?D#?2_8gZ-b|pEPv(6Ac}Is-e^1<Z~IFZYiU)!hF%r_(CO}bgZG%Rt=qo=3g2*jcMq(tuo|QMyIQ+19KUjRAqEBWpsAUq@hzbmM@MqbeuRTa@El3XBs-ttbmlw|IgmL#MsuY*Fp2O-fKT<*RDEs|Np=Ly}q{b^^1q4SO^NyqXivW2zt;Up%uvv7;u6ez%~+ufNj|!0f{Ks2oXAnG-v?AQcROx(n^3RK$A#8beUs}Z?4CF)Z?7<pL1>3QK_`guC>=*YpyxJ`8~!r#w?)ITo%xIQay)O9vQ4E{S3YvI!&j#Ik<%vO6NSQn*;yl2SqXGUw6OltDiswTDRP_^D}=y^H98VeKzqAR0Z3TtAc(Cdi-I4>As==9D$+DtUEah)<1+My;d<HcDfO%l7#4$m=@9)pu;iygV-?Q)Z+(piOJ5!#{8-8=dC4?FD0r08g9!_K3?AzPmtTR@@ij4oU@@~bPhMapcY_Xl4Rdu;0HT1;DCF+xn*iCpK);E+tHW@*qf(RDL0jTkrda}t`jDXf<$kmaTV8b#qvqGnZh$~Wt{)zn<|^3G;y_T)+TPOFE5*MQ>-sn&NvM1h00m;lFC_4Djw44TrHllwYa%nKWj?;%)hLDR-e?*Qr=$4ZS+y<XXNsjN@(Gvgyw``fXREdigsmFwi23zN!z{B^;WR%RfEp|{WY6eJ0HIDg!<58Ha$`0Vq)CXhZgz5Flnx5(^Qi(VXktS`cSEFv62KqA+MmU^F>0nWj@POBrvMJ71`40dge>485a%|bBe9&xZO`FLy7;Wd?jdRYD|Nuh1o~S1YZ%w7@;Q&Ukp2)3q#9vT?EI27oU-z6BrvI6v)I8I_$GUwi#Pf9LguZ8&;}-$75l#V@s}BYT8>orCS>C`0v5M{w$vQrnVFbK``7FDxaiuKIRdEv1NMH`3-5#5L>(M9Z`$ql|m~j1(^)WxI<n)RR#SRSRlw-Tyi4N8%4W|d>LNn>BgC6-Q@_xd+um8iblbTNjz2lNcOEkI8v-@&|kxSf?*88-h={evcIzUbTDGI0OB#s;IHy?q&{Tjgn+>?@AoGCREtup#xCRORaY|X(Xn9|L}6A0BfL=G&h;2>AP@|?vK?W8;)bhwNj{eB0ypIDhP$!q=Mz};&)Blb&+8{YY}r86cp=)gTsGO>)>EGO;<BMTtCh1qT{fvKn_x`9r82DYX+GtSCU;&o<bL7(HRD1;o~dHy*2~I)_-bTQIa@_C1d>FB%SJ|qq)%HGev`%&7rEmCNVixX?S0tNA~mdCf!2AL1$Ogpd?ZQOO~MX>6#ZR(`1EZ4tyhnIp8cCkW8aJU>e;c^=5QjIhB58eWA7JZ@5!V_@-5r&VYM*!^lT}fR!9PD_`4~5<nV8=4}X}4pV!u%4*xBRbSf`AGxoJ4(Hdjnn})yU@bAut|F5}UpObmjJJ-aL%===I$;;c}4<kCMe-z6I)H%uBWjmS;?VySu5p7i-uuu<Cxh^r|MCQy!Y_qAP+~nhNCzDERQ2jf6YXl_>l4?ozmD@J+d~L)I{SFJ;<wu%h8Is2kI2AP|Ejx^l7%v0g0sl`TT?!08IP>!HH=)wU8TpezSJ#GkEO7wzBGCyP;D55VO_J4ch+GMCHYWccpGwZ)#Dy9qU(C*!y{1Gzb8Q=b1uGy)87CuOD<@Qjy{O`)0+>^xR(4)omV_~@<6lG%tO*y;zThRuK{Oa+B^0<FAULa{NuJ^fH0~WM^thZGOL=4O`u&dypP8hGPvA2(-BjlJ2=H1XXs-FF=Li~RMX*9VNm(ZZjc{Grg?kb~lL~?+2|+`r)Ic<A1Wkn4Cgv|h<LeU;jrfo71r3*rT>lz!)rdb@!_hDq$pqX2O*2Dj+9g2;A6eZP*_c*X)f5>-`jbt(%%s;|aw+T2j>`JGe~81NO8`P2CyCY%iG;8|0sN>72=^387|gRtCt;8#+5$<~K8++)b>k&rP=Sm1j{zgRmX-YM+OGZ=-0%4Dr*XUWm*jVRaKlews~WYJKB&&F_9CLM?rp8Ai%q#GIJ~TG90eNbkuInjfwU4km2eC`a`4<nkqL>`F=R}t`LBmNtE$%eFXzQQ++fFAhAbDhygkP|wsw4{D`fiXo-*gzm#(cP%7O)WeDa*j?cky9xM=8=sERkLFXnzar!z@c9f^dA$bEyq6Y~{4pnQ)v{77Z1bL3?U;8nesL!QmS%@c~v-<U(rkkx#0!@$5HuRpFsUegKkXAXI-AokQLtmqUT%_*ce-Uii<pK!>@WERu^@L33VtBRoR*AVUo67HVJW;4K~9|5rJdD*Abd_Z$`vFuZvcA&di0-9<*qCY1nNo5~aJfWGLtaccp+5>2ixm;~WAR9W-gMOKpS`qFxOKZGjLq|HrHCwNme;|vjsCN0-J;ss{P`~Efg#~9so$urztIKj@*u2V3I4cMBLTfs;o5)omnRfKQWJt{KGl$%i;;&X_K-u>JY?rRPFJRL=|JdyV0(vk+!!kry_|w5+MglTcV-u%x_JK%RD&1%r!(g2u=(ORW=JCmc{Q#$mv)`jpC%^wr7oNYkb9ioLtF#5o^@+ZV2U}+M4ExBWP1eSa_LG&|nn%J)-zk<!LL7V{5h^8wTL2m(Gy1nQ7I04YIBYCuj;)p1u`)){m@1Zu7K#t9RWm86`GPpK_xS6Gy#)1#IDm5*1Non5^-i3zC_fg?*gX7OK7lrXuh+sm;VbjAIuKT=*>fNj8dGTv#IivZ+cF0ScpLG_t<q7o6EIv1W%U5e@c7PrU|sdt!PKN^$BcBpDg<)IG8TAz<899oi)`QGwBq^`H*B_<crm)9P>-N5B_h?|x8uhVrv{SmvY14aoH=1&Z{H9|A1v~#$amK}0lM(44lORb=lX0}oq~}cO`xVChCN?@Z#rR4>pven@FShd$}nCSX!Qwp#(XPxfFqm?p#ncF0DM~0^+8!<VAhfZ!{LAb6xO&aoA<djj<MLQwKc|4#M+CcpTYZ5iuZ<XKefqRy)l@^!rCm;->zL%pH}1B6SJHxp+qW-y}uY|?xnF{lmcNKRe*7}Iy`3zSE}h$G?Qia>i4=_kYAPy!jc4?RVW6Vc&3cgNu4NHNj{CLWr6m&mOpIv*<>hye3a8u9Ag@x@s;IzImU727z;s!=lhL2#=rbN34#ZT5qKc1uv&U7iHdcA?CVqn@c53{{Co$AL(674kTTcw-k1*seigtGcwgBHW_LPUhl<5y?z-aMM(`xy)dSN3EC^e#VB8wWvL)}YOnuEjFc9t}t&k1>L=YK0HvSc1Swrr7Mpx|q!C$K}2$O~8iYV+4wg8AO4X_{q;d;zFV+#WwI(}oe)cGs!5|`KB4apJC;*r;8^+?S!w`~7w^Jkg(x)G-Im;WFov0X`|R^M0>d#?SMO~#@<t{mn)vuG1GGI7S`AQr`*G2Bh~nHHPys@`+rJl~?sgIoI>_7FxNzW3Zp5Jmnws{M?Yp2Hv}29rl2G@J*h)2t#&y>W%+_S8O~Hk)lo?ro_u>@z)!^s8pGxfsXVSHhkTaD^%P1Y^A|*|OHMWv&V9W;2)|<?sY_%AdiI=kvGZcW)8_ZEWQMw4*K=GR)u7=US^#7(XiW5Q^!=?$I+lDau<vX|XZ1gj@>|o-*v%)hDSUal;48nc^EOQl!#&CTtnu*jR$13I_PBnYPY1`{lLHw4N!wXkFKZ_?D}^!g!(_@+tXlf9<2$f~`}l`ct-`5}W^%wg5$Gx_V4I<O%hpMG%wyQ%0e^WE7-O1s0O2EZjb26q-e4t4+_@g{claYA^83<kUQE9S#_!opMBf{l#153m(q3T>7FF^+GQF>26e<S%fjnsFSN<ciNE3=R-5mJlB(IHX=RKklI!kyHPEXj<jhk*~zV1Q48fYYut^<LN2Ay>nVlqbZ}nSY#m9~J%mi<I+6aWyyRzZZ%+S_`z=Hp<4<sd_zL$A<RM@I>5y-Ald2;id|<J^o4A%Z(eBtb8q(ddF!sx9r5sB3y7uDYhbzwKuOvgSP7XXqRYmg@`bx+b<^e(?l0fkj)kSg$Xnb32DmAb~%-d$36gZ&k@!7UC68CDC$xn0;fsqC3<J2db!gndeF*45>7+r7a;cfB??R1Zl_ri?mlOew;;sG?6&c9WgK%Nn85csSWXt0F<*#UV2UZJ2J0dH;~rWr<Y`ebu528$i@kvJEQ*;C`p2(1`uVMvqZSYh@4mir5MXl-HFs{d(hNgEhdA4+Qz<UzzQo?m>&`<wiDG1!QQP@ANTrb>s1oJy;~)ak_J^TcOSEB<8AUK1OyusM=u0u)|R7M3?>l>}_a1bbp`unR%OZ~C_k#kOR9iZd2f01sryjLw{3&&oPsARM74pGrrDARKE{M;46`9~Z1oa)#~+-lD9D9nQKElHsqV5?HAzCSb3w3DpxhOlKk?*s$~MbO$lxV~9p)_%Owt*{biDvDrdjj&eNY;Hs@_tH8bU(?*^tbpVyZ8_ttr1Kds6aQti7J4uzu4f0Y)jme1G)GW_V1d|)A)pFCSUzJ-b;kTv=uyqPdL(xvf81np`F#J(L5rYU?{HY(Q;kvHtb&pW#>`-vgP9it|^C#v@U`_6WC=+(?Nts~P-u7v}gv7Mi#qEjCCwmP~i@YF9U_qHNXehKZ*Y_sGxGSavZA_cx#>A(jy=n6T(BSU#7R-L{O)cP4sRe}hBT;?(@0;kt8=d;w2*3UJZG=C+BtS{5y{Q7csRH}~a~}MgFu<EIz?(3@A5CF^*N6dpyx-3$0X!iCa9IE#`V;p5iPh#z0N~cxB_u{HdfmziRtG$*sCqo}G|^OpeN=+7DFr_9ORdBJT;<+V4`4y)e?rGU@z>7;{S{BRW!5jQ`QnZ7Z}CpGWRUmgIsxwF_{9mC)I0sSz_Rm;GkJiOm_eEe_rq8QXBx4svVpBLwbA*n%Yh}ukvn<w^imC@<dy;k_9J>@DFlq}%GDMc{pAI>r(YU~1xiK)R4#RK&6D!MbVsL`y*g~64G`Db026iei9A5K`nU~9?N6qVOMdZR?<U6o#YIM=M=FEh*#_w~0SaN&HMIbDNiE<q8U2%F{bFEvLNMSe%l|dr{44*RU-%0zo)QvRknFp{1@FVGBEaQ;h15QtU0!t0^8Q~t;C*i4np%UO)f!Hv4qh%WaQ4Jqa@P)Ui!ogOUdm2PvIn7Dq*Mo7y*?(+pK@_Q%71dIu==8S_Tm}sg!NyGRs=hKuPF+I=l^tZwp?91*H7!hY5=EkknepuIPt>ZTpKRG79xN8#r#`6eyeQyUvj?=yVQGM{bXTHla#U0y-hlb<`(D%v@v!Km=NndyUT^;+<O9>$#D>bwTBLH&C*gu;>*+%Xww_Ow=o54?CPDK+CY=WZGUtDyr~|YSg4m-tF<w@q2a1^QWZ`t<n`VS9lIa{P_uPZ)d^qJ2V=&sftSTzgmPq|tLpf^*aPu(E$egy)Pr(@oEvq6QW`iD#R|G3*n@h@lIsR;Q1mmZAd9EXh)TtU7DS?!fHTJZwiQm^(`QNItJ9IJqorDqQliaSK~v*uA}|_FJ+-xM`VI%H+f+0VYT@?3y28uvUA^Ta-5GN+@$zH^7{QTNi4TdJDr&zC+1TzEc=?G+i@Yo>O$jxRF>DEnABC3>>;Sd4esBQg@gsT}#r^6g)NDw~=SF8uibkWW$`nEF^*f_EZWDlt`L4ztC`I$Nw{;8^I5|Db)8DqHl}P>UXry~B+sdk-z9>Jb*^9$&;|dQXpqWkU#uhbUd55(VF?lH4e607Z#B<{{wf8`9Xa%|obg~6>P<uiXI=V^q(T&Nje+!;aCoWP<n%{d*(Dk={`%?tV+jAhWmDT^6t)g*_psIb*G6<xS@hkG(j>X*Sr2Z-FX-8=H0$(kr+I(eRq6RB`HEydbY-ep0hmxRx7{8Wir&_e!sK!rqQN#7gRUQSd+QY|a42;F64LW0QEUI1*E25@Z9nH4p4&xxe4jw`yE@mI@1K7mLVMc5e(f1<}U;|09>N{4liR+n}%z9Qcvne4JQa<xzSl2(J0|9i!MvfB|`cIF|`P(jEt7cPvbbGq%9|gs~YHt&{Gw~)ZS-Q(C+viy$pr}0D`XyL?;XYi~fgGo;E@S!m#E7n5Pq)31>#?%mvX7x4`s;$|?`6i(V2WnbhIX-ClIy7q&-M&;v&&o<o|Ha1iJpNoBFx)%ip$`AvFXK$N-tI<`JL&0y!FoqVZ}8u`944cgcy`=*KEwKzp5hs_^zcnjTgA~zPwhU&vS4@Q_tt0p1<@FIL4=$c*AKptWl!%g3B?TkZu&ljos3g(U74tgEl+>k5$bLmD4;D*M^(;H89g-0dHvH^uPfn&_7zs$4)IDc~9)Jj}wmGHpFU=NqDC@OP=JkXWSdKwz$0#cX4}XGiZL!RBjsbJHzu-;mw*V{E$cchum+xh${Ss%xsZl9X}=uDrS42$N<f)&;d)wgJ4~76awQ?!Jxw%X~>xdGQSr0-;#i^CJu(pNcm|^biCXjh#G=B)B?u|w~Bq6qrNwPsuuAcKGk^bAwW!lo=9JmM-@!mVPyM;u801fd`qmR5k2l?qM&90+r9D@5u2bdVn=K81dQW@JSRxYYmzZ0w$3G>OZh2ppGv%`3VriHgGpm4A23$J{oqd>5mq20g+QcJ?=JemfKMm5mriW<X__V<pJx(uwnp}eGz8tDJ@B7=inqL(IaCPfBU)|AUOpOiIoSzQ-NzB2Olmw9xwM%gnT^IBlWWLe(cC6JpRsilueec^*PulDeq*hkmII=3JLsGM7ny%ro8qL=k`FSv)y!fML{B`?lIuugpEWQjd4y%5ol$%zL7Ti#d(oy9PbTi;WDMBiDe%NnkNP6-ZzLr_$%>PVWb#u|lFeXZNeE*4wthg7?cxH{isbwxr)l99z0Xj1%|fBBnLfMDjnZHB6HB>XFp!JWe@h0+{x*F~Jm+@Tam|9hBrOk?9u1awnh0R5q0LWxFl!=rQ<0l5DV<(YZ6atK=TyQ}Jxv$y=R2}@O47|20aC;APR!?CN<q5!G^@y73UoymG!c?BNjCFY`z0f~O`h_wik_#RK1;Z+_;T#)R$TP@V7Akua4P)s=rAkX8Gr1*bVd4aSl}E<*pJth2wd~-UIB1hPiV(;z5$^f6Gv>Yeu-+@A$xphORRG3MY|&}fo3|gb%Z-ly$#|Q?b(jdcEoW?_0`)xX;DCQTlzsFA*tBp7N#b5^%C-m^3~?pQC&O@y{kk}VjjC#q3JF;+d=~*Yh2X|fyfgYwKPS1^Hv$B-b`j(xdG(MYY{APX?7xYqN+qI?yPWNq-7K%yb(_pPGffC7g<VzW;cjS4sy5{n8*mXIfQorSHf3nys@|om|3(7Xzug%+#syTAG!;$f`GV>+O#o|@91Fpzxo~^*TBYb^)1$%_vl<=>moHK=I+G=ku9)knMN>Nx}edNQNt3(b4QSuPrgGRQjVGf`<H?Qqv0NH$z>X>$({{N93kTCG5<$wj&R7M$wIVjnuN_|+6C?w+sWx%+p1{E2a}x50uf*7tzO<0kKY!R1%s5U0|yx9pa$ti!B{aOBq?%ownl0hdsz@t6qxO5#4C(>zz%Rm2?_64hEZoA!1Vr>4siAmD#VHG;>@4C0coK+K%!9gLR{x@7^EK=D$cXC=bJ7ZgY{;$H?9X`jr9k>>G)sG1l)d{$gE!XS3eW>*Dq_{D`9_qB^sl{eA-qm?JeYC8VkafVSnR_%jOo5|3q?r8vL8ZL8E15-GE@AVkg~Z3dM}-;+bfyUPWUhHoqYujj}h~x9&u8A%=6rN`T4}M$VqCJBzx;IqFge{oJ#2^rv}&x>v}Bx$qd&yz@D5(f|F*^n4Q?{r!Tw=cJ>*ikCY^Tbi48O{*WH@i@PXU!|c;M%7;H;$Lv;w``L?<J9*Pxk^zcsn{CLi7eNLMaDv_ANb7GXY>TE{<4c-P4ROhKj)OcnVI!Z$yG$~lMPlEq_1lg;a&9HP#W5ohDyHx=~wSd>q`ocpt1-!=n%7ELHuv;KVNE)WnP{yy@wj!2~8UI_bW0Cnk>}rviZ`Q+`_5IDxD5Y7BuF&RgTC<wS^+**C2#EXW}^%S;cf{PiS~FO_(f1mZlPRKpZ?GiI$tZq(&3nPWdgq2PT-4@k3lNRcmTA^6{iKNp!MYevoQ>km&0fNpx6?tcEo^TD@jRd*6BV**ZP`KbxUjf<#`@**baBqzbF63wvmNslSyjxN7{?g}kkbED(g-jB8I!tV}2H3~{-!8iT9$R#>#HX{i|<jho0MvrSwpva(u*CZk}m3GTD(Gs@GsVn)Qma5`CxSz6Bbop{S54%<wfM-<C$idgn$+GlGxS(=QLcx02TI`-vMu!JI+PV3L7*+_JYr%hHU6JC-}1H86gu_4rQOi$AqX~jb6)c{=r#<+;2rY`#A+gb5-!BGj#MJqPsHPWzRmM`)ixrlZ8o<Zn#-BDkyH)}<CB%r~?3|@hoWlYm&ndyK3lTPzyPM}7|B>u$-9&C1xn%#Nd0E0S?9LdOtIlh}r^EAOZyVrBPJ(=UlX7@;=kMx`-cqp@*KGaxdcYASmGl#mI;OT6Fr;`cp{r&~Bdt~2UC-p%$&u(!|t$M`0`bgcT&_s|8^X2mzgD~VT>gP$l=arA7fY#I&I~YuG;bA?Q;AuI*2i(Y(QA)EYREg=eZD5*2n||X>0puH>-M{prM06g&dsj=(_z0RX@WtG_1GUh*y_J(?bdW5K5qW0tNQ7PThXOjoCU_IJWQx*lbu2{&H~FVA-+PbtYm~GZyW#aN&$t+y4ZMUe6HJwA*g14=Zo-i#ykkI;Pq;NLTo68g$(V6t#WDk(<!g9IUK(3Tf`a+lHsOJ(i~ag)_iQfz4r}cV-?7`F?6J2iLHE24&K3=+Y3IM?pzAzr)dWoRL9z_Z>IwYLbB^ANC10mtU@FH@5vYy6s@85DuD#S{c2R{DkaNJr5+ekKp5^^lDloG;BZ3(AAlEH)fP7f#z0OWtfSL}9%9IKy`VCAeC#G&H_<-hr$#<(K$IVhgQ^R*uQksZ|Z0UND-nzAq78X95a#2dClikReVv3K}iNSUZqf*&Rel9s^RiW;#!%hww^cG0eRaq&36%Q=(Ue)p2m@L2qSqNYTD*AX{FhC_tLgkD4*_UWt4L=xKS3mxw)>XaGx<Y<2o(f$(O6aQ5MuwErHF2x@T->TzDO+_#*~(MdN|WfZWO<jeRy&HqWixb9*=kg{vKF^WMck@ih+8#9-0DVpbiu@}ylJqn#I3p_ZZ&e-%CEm#=v!5$Z-q10wrFtX1LSHUEi@LDtH-6v6%UipRU7U0cO<UA%eF%<aC0Vl<*aNLSO5cBNxXy6l(5nTB`mIT0d4R+!+nG>ZC=FfQWA@Pf>g2E_fW-R)VvbLVhxhoScX{sL6OJ$zu!Lqe}bp{JYlooDYq2i4?a&hjoL(29!TYIO|*%c2{FBlr#zkUluHvay+pCe6+jrvA<cE&CKb34_FNHd`h(3`{_iaHJ<_}Exn9!u_`Xj+Bz(S!m%;>3mOY!i<PKXx=G(Au5joe<N@yrwi(6BuA1@6zR(aa+F5$DF;}~IiQ?xG^6O;0EcemVLQ}&n&w^SjI?VV0;BB-%w-w1q`IJv$&hPt=R4ai*_w8BC16=q~}QXif1<-1CZ!m?tX1u#Zj*#_y0#FyiP?43!gDp8b2;qklShTKCisTDMuz6DAkx7pKTw!}k{A>``>)JFD~L_ggAs{7+HZSe!8ly`nq>%kWwf`p04^Yo52i3mP)ZrTL(=3^cr5Wb<XdVWbW=)g5Z)K|bUNB2V$tq9{X>G6(7UmNo~-V6xnhy(QuFpnn7RhK4_PAv2J5f;++{MS8EpMm(7mPS~{V&swOjtF2j2W<;vhD{JLd%pEV2_@bfHb=B}HamaEXb5GeJ7_%BMxd(Gf=R!dTuTiaFT0zRfTjHBg@>J*YeEiG4icDmyhva8qi)GfuN(QVuc;L?vV?`tZ*Q`zbs|-~C)#l-Rh+%r4XBNAr8m?aUP=`c2#HWA4>oOh?~K9*7@l2V%o6H?LZ~&y^qxEN(QJGXRowC`T7o(F%z-7UIISy`(vm$x)1ApCw38h1fWj`mlsj`?lZVpym<KR_{9r^%Fv49QnDTaYM^Z61za*0|R^1l&nAkukDI9_Hq_(w$T<oZrl1N@HP0u(h0TraTp-E_nq*X)0D1%Rhg2M=AUz(bnQHj_Ca$6GAjjIc!ftIRvEF$XaU~3d<R4~`l31=n3#eW|14#Mw#+ovu04)ehL!x)n0Ax{m=Hca=9;ZI`&zlBf(cKC<<rvbbD&KWA^yI=<=F}3sZZtq<>+;e7m`<)N_k^JHwDH4?;zRLgI2Wi1J1<(9L_XMQ#B*%y}TK=MZ58pe=#k6F{@laIHS-IW6!$**Qyc5^7ONNdP{n0VG!vgO>b!*ae^Q!2W{@riH>G{Jg&T{7QoQktNAya97&*bzF&+vpk%lj!+_R4y#C0ZJ_R!B8^B`D;Lqy0sKLZ4YR`metN(J_(lUQ?56L5n^oWre8*L?g$qd^lYHb18L^MzMKXTQUXn6x{I2V#&(QX;;&!!c?`CiZPe1$#+RxCM8Vj*HeiOkB#7tu;kwz#lKg;((G`+ZeoR}QwlQ@YXZ*Wk*{5=Rkel4jI^MMP$MtF#$;1YN@RmTKm?Fffi*rN>S|P;!D40wQqnmOyx%Wh=0AVtIrVe4Ddg+=5}f5Dw*!!uJ79CbeM=pioy2_dyL$rgxi#$B^D@3O+Q$bSvxA?P%*Ev%aTBE%C=*?q`;r|eC>|q58PdUaikRTU#kzD{f1M}wE)Y<rhAJ%cZzGS7!A_8h0-^^<)rP!?6$F0*_NK@_qe;xw#Ce3rNKD)1gGrjpqU(+-;O58_fulQ>mP~Is&#ZAL=@ANz=JVXnYNDyU=;f8(`vSeYx>ierxu=F`s4V4){Yn_vvvphFtSTuU2s*1124b#*H{|1}Ml2>Y<P62D)PpwRx*hRs(KslHqoQlQE)uHaJ}lv-e6x#St8cl;;{tywSY<R=B{m@KS&cBZvA`{XCnoetkUwwWS@k?M!CEgSc^WU}pJb=4^hG*3(^gE%Vdna|S2VU0`qIx0iIPa6Hi39EgSvYP>!I-V(m|PTd}?XrXz0aMb8#!2CX;SS$N&a*!SH6Ls2e82%1};A_p{N(RFn-O*3cXICLvBE%1@2b0jb>48V6wK)Qid@l-tv?q?K%>Un%o6$>MBen+BuN+<!vz6o2niNHb1MosG(mADN~ztZ6#cTh<043okHr)_yh9+cjBd!>K*-byjQ$WfcZ<HnBDsN<&Z}F?}AIVdm=;I+-<^NN!_8Z7SEu6hDn1>>YB`M%kIfXN#U7bD#pTly{}t?aQ1>m-jm(>+C+)PWNx;sWc|`qUPPLMfYP{mmE<jQb7%Ng!+hm?f#w0Xlb}7VRT~7hxp2O><_IWY%5JP1eYB#?He{7M2ffkco3f44~fA%0iJoP$Wi{`yqAhGb!$#mFREf<d-HJq@P<uw9xT#dtE|h33>SuCX1*w(<rr;HQu`Jb>N{p15hV_k<TJyE$;B`=xu3dq6mIn`n^LjDAd5kiYgMeqR<Z<`FgUnHn&BrHzlxuJ#~i;!#valVof2dDz0UoEvOA4vHRRbdlKG`4SM@1Fe0;}3Y|=_Dt2)lR;n+)sX@!>|cmD!KaNd=bFLUeJRXp+am(|-EHb8<%wt8FR)@BeMwi4MH(2fciK<y@J=vH<A1}TZ`Q?yKyMX|-B8e(<4EnN`p3LSHpN!P~gnwRV%(S*Tdz#=+@TGx%R`FpuhAxJ|DKzHYdJ$U(Rb79C&J(cDvYji*+<!|`k_Je=r&m+vv#UG_j8vUfja#H%$uiJ$3Pj~hX55tfCG}<{WA#?Fxe%AklV-^1N=P><zx#Ih&%1=H2nE9$-@VmSCdzi1`@Z?XuN*T@9(3PLQB(>@n{O&IN_CKCqjG{&lPyenKznjJHcKN%ah8;EwD83~At{~!x-w#YikEm?%ce(z-vOn+hqPy~9oL;okgn@b3G0n8Ij4WPs<g7Y>5!WwLc~O-Y`mV;C*jrc9uB|+`0-{lbt87Qh;`#?ZGRmZ;V{2KH$#E+w?T{9~EB@{lzjdl@`5mA5-CKfjk`8~#Jh5>*|J~_qYFDH3Tq%&q6|n|GUT4GWY)AtC-0!^81kq>|QhED5GuV|Z@yUz!`U^!u-IFg+?-;BmB;xWXeh9OW)cED!m409P3DeJi3x14S?(*MaZ>z_AfU@45r!2ggQbxyV95LCeG5@%>NF&GI@N=m*aFu_srj{y}rj@<acexeq49H_5cC3{2?3WazAPkE7AurjMGmI2_MB<X7zilj=F;S{P8t-(pl@>r)U0e{$AyAXyOJ|!?WU;K~ZW<wX8U6t!auQdz`2lL{hlLTp!}nOypz<V(9F?W1@}GWualdtq@;`tS$v${M*?=GHN|l9`guLTE6e14fq8mw8GW3p?q3Lzaz+BKFXbt|_1^X*7;GNLrdDpk=33^{~;HKzs24myWf16N*1KGvb){gq{%)R`Fm>N4@f2Ra0180Z!(i<aC5r+!iQyY4|_9NPG#mNR=rAKi^+E2A)k6DkZsTa>IuuYAi?&upH9Bp36+d;%Iupy2UWLLCH@!0_pPCY4!1`dGOWSBDfN(b)+$inS@QI5oQj6scTb&(f6NM1DQN)k_wPkmM1kLd1Z`**Ne1Bab0-%2%)bm2Oc9wit{FDNl$LDn}}|6tlX<<E!m*On^Y1fE!g6V=<ss3uI0YcQqaye1U4gum?m^Wv_2kMaG1zwi0Z7QL0oL2?-<X`8HGKlS6^u@zs1?VlE78ylOC;uMmPK5->E*~3(R&_S@X03%7mT$NC^MW%<6p1%pkLdksxpCuI5CwrKwoFRG>da$3-=0##d9k_t(U{`+o0(A&!&s~EegNaNWg|2gX*nGS{&R3516vE%8^M}P%UH*OThi4*Bon&Qryd*dM^7r%uVkk_Fe*vLO@}r{2{B(}Kt<dd`#`Y?W8&cuiqB?Q+j%j$*LSuc$*aE;g?1T@<vc>ie^K1_`24VBK>U^Fwc0f8J0S7>8)OtXm^0of@PC)ngkmHtH+sE?V`~+i*hg;0=98e9>?T+C`yt{kA*6<(|S5N~Xot6^bfq%D0+F(>ya74EngCJl|m0Ac#v=t3GDB4*kM^d+Bjy-?T{RU$(F$83raIa!283I~U_ZhKl(zr8X0EBGP3%RjDDjG~!m3M4wghP|Ky7$~+#LqOCT%AfwC?`s}X$<P6j7<F>5;O<%JpW#j%y7uhZ(JOpG8|beOt(5%LwtB=AE6y%p?7&^76<IxYj%p|-?w?YIReoDIo!_aPtyjQ?*g9!Llv7>6Y^7SD~JbDJRLud7!fj$Ijn{!v?E9}Z{5ktt-f#ru*2(DK0dRFM`MmvER!lhyzfa7b4hX1#ilP%+L8^MDNY7HQiKn&V}3-;DW-z7Y@WloQnZkhDYjnZNvDh_wJk&OFbQ508=HbG=#uvYby^C3K_Dv}nO~}4MlrebptLOsP;$Usg=P~)+zN116>hQnS$9(1N$rmR9mI7~7*B{3V2?0HY^FQOal$WtBhTbiOP<9GZP;hDGx^{+l*iJ>s#!D7FcnjBRz^G1G=SG!V4kTX7*Og7&m7Z|cBaLX=t@^?IOCkDx2Tfbu>raw;S9At&)H^{R5PlTU89;|o;?9Fjocvyo+LAW{u}1_@x51j$c1iZl>33XUX%TxMPkkOGp&ac%AWy~@iOaA%M$66%OI*vxrxo$GT3Pu^u*0De}xblo@WdbSuNGhMHQQu#9bA-jb7W5fI{pR9XDDPV`qdwIi4I|#0FIK15Y@CHtrXINcw3vev5m+7wZgAasG!k0hyg$%P(n;dAU{P8>|Z6|Hcn!6|=qs1?kAJ4%|QJ1+;xO{b-BLpY6cch=(`Y0~4g1%z+Sg_Xo${-1A2&{6;0_gEzLG4Io8Z{<jk^6OKf$j#3nxExvJ+kpG6|qZo4DKo7NVB(R;ou0>%fKg(|!wM%ww;Dg-Kur&<-^Zf$5H2Q{T7zbVws>*nBUEzV*jPOCdAj|qq#}pJ?fUNoPzsakk)z%!1QZtHDvrgG$wHogL1lYg|+>mX?K^!yQ_(1l+vkg6AOr!N!b*dS(J`NCyMHc~}^vnac63inUie<rk{LR$ZbuR=Rqu%J-8}J@%9l+$~S<<Pkl|HSdX$VMO3=+(g1BV22V3t*$OQlG@VerxfMwS5e^$5A;?OBd;pk!$NLw*QbWwOf*$`M#%m8>R@2a!3TW}tfm5LnmoRBa#!piS?_E*tZ<(F$!u{ed%A$q>PDa-)+pV(H!I4|b&WkYimSW2*fjd=q7}!bh<Q2Yk?r&lK5Afgvn4m56i~U`DdF1hE-Ux-8|Fp722b_!Y+fY9~})au0+8Bro;#NA5_Egd?#+SbnR%cH<=&kG5-mWQUKSH6c{`Af7WTAmP#L2jjsPSUit`g|<%ZfGoG2)p2m-;CqhcV?`tpS|tpu!kief^BW#uNjzMkEM3de7fg1?vJIX8Jv9vzZbzv<%G&!_pNPCx*5A)oejL1I!s@Z+XxBkaK8+d_6rQm1k?+fD0_=C+CtTRZ62d&d4#QvR_u(CHT@+M}-WkEHw*$fuJwZu0RWAyuN<=ld)kkmemCC7!5R1v`<mglJkNOsttgzLPy*`$_`eV7OZoU!?qmAm#0!7ujFtxm*>EW7)^aA(NGv@w`xR>$&aPP4cMsN(<7<hO;&nyLDCWiG=K$girQnq!g4aiTc0Slsa>(wBm*<D`^-uK(*RzoF9i}@ngs{#F}@E#fytiQAx{OA^p1uIsImn{XZMNTX0JIrgMV$v*+{9}5_Qt-FV#>8@%c^(amb-?%8<GSQjbIO{tMhPR-asxeG2dHrYV-dSoE`n4R!SG>=pb3Tt5|o&lo9P$k;QFT#Hs)!Vchx+Du$wfX!<Le6ov-9TA1X0#n)jW3-i|G}ewWSeSFXDev!@q`J%7pmNWgruh!`hn!gpDS&Yo>M(u0M;VuGO};JdY5?28AXgB2`u+ZD7mPAq+(Ms5@A9eA_}?7?SuDk*cz4#?-Q^nyNGxJxN?{K$rt8SHv3`Mb#Flr|x6w;1M@eU#29+!C?9i6we$f4zAijOf|6&rhWmPziOYrai@F#Sfbo!@v8A?qJenwb?N}qAvpL?VX5Te7Z%5^+OVo2xx#vcXDmmIIO}iZ?`{kn=37#+$k_HOg8xKQ2_rE={aN<+B*Wf$ZmlDZrqk^phr=HdONJo-*RIimcS<>gX)Q+{Ys4jgmb9bBA>3~J1z6CyvV3dI5@{gTv%(DF;($#k-J;hs$IjQc`*mqVWZAZ@}j_S#J=+5p2Z;1$g|*ue9eux7_4hl0u(Fj_E$kI{HicP_f)~j!<q9W$brDl`1nb9hzKG_`3xBr@j}NebIoWi0Nl#FD?LkcJ*#dbMT>1RYb?*Q#`h3Ra0qH>m-$V!a@~eB2UhQ8jL?HN20;Y<-8qh^77;|PObNOHK{wEgRn#A;2!ZPf;c$fA=mhUm!ENvF>5Se}vAI*EFn~)eU+y6k247~3<92~j<#(B-nqfPxH7M9;#;C@B_9+TdCK&yMApi(;%|A*?Su6>{5wtt7s%914dau49Q5RB!i8TDGN1#a}SQdDT?G=!Fr3+NE=YGxw+#_oz^q`^DTSEZmGm}Wn3$}+2=`i#4^g5=o<esTki~ZD343VDjFeC3&uZS20jd(JZ!=~TC`@$JDJuAAk*mVoM(-jP-H}IrRm?rGvMI8qnEF`CwOiUY;2QYRSQD7R;W-K2`i?a!yq)f(yrHtkJgP)WHMM5JkPrItPzOadFbG}aF^z;)q)5H=Q#Z`JrN@}+p)LG(1{}`6sqH*yRejW{DGxY}YoVWswc{Hs*We3mnrQ&n)&4P_Jm8+V5czJcX{&pfDO-6O1FlKSQFETxL8DY}tD9ol9+g4W~sHzVWh3d(8&PpHR1j3PBn!jaIVYh?hObwfs+8-xBg#&H*C@~*wQpIujLlUmGzHep+T{)(`|HdL#Qq4Em;U<<E?7v7<F>m#$L)QvqYxyV0L6_G~*jVtdh+!LxVdc0lzG#YJIoXoB>fH10d$WjPfw?cNHjOoX;!%!kCtikU32N<5w?@p68~=&6#{Q3^edEVn-uA{X*uL=((Nh<&<rYifkas(BGsQT!U3Mtoq>*v|nD_Ss8ZmZQQaQp3<2|zaiSj0g?493vMG-AnE6LNulWf`Rr^;iVMtK|E??l<I<{P|!*deE;=r5F-YR_2m*s!t$S_FeZwR>&}4Rc#ZIyOulDkj>|=}#L^B5S|7A&AR%5tB|tUGm6O9oJSM(Ovz{ZSjq0V@$@joa&!@pA2+%wYMC_&JW|67fBe%mBceC-6<C|C7zLx+_^4ZN<1G6ORN&l`POe<k$47g%_!m_B%Tor!mIUThc5!PkUYmlvbk2WIid3*y9aH_H`nWYb6&UE7O(Qn<@qS(48E+t*|;}l>2F?=_iYf~w9wy1`0c-MBm6ePKY0HQALYN{)t{|j^Vj;DxaJT3?<evf-e&119NYTieOLWQd2GY0KbxNX@2fuhM`vJz|DgYdkM!UA#s6i8n({FA-{n>5ztdm+EB?EB?O*g7wFTnfUi=%My6|QyFRIs^FkJo}3I@m$u9W7n_j`el7C1|Z*DU^fq7Y{3^C{h)3e|Kqy=IRb@kq=BtH7cr<D}#cJJuJl{OyJ<WwR)kXj4(&^u|;?Dc+y_H|jP;gsUI2?2&@bMDI_2LS01f=XXr6i9hzKqKH0!(1(ent-Rx(`meV5`CF{1->JEKc@6%-Ex$VQnMO{J>85mFCl_EJ@umB^o(7QLGK%h^BJj-KjAuV80?h9Olh2*6yeY?&imkmLt*J>re*F}R`0;XNoYJ&*2Jdyj_I2d~k~FWFnr2IZJHOh+RI!_~rnB{H{kD(TU*}mdzdt|0)2lt1Jc|cvf3;!pi}~h@WtgwiC6z~{vd%$BViv)3s@dyYKIQEg)twE)w@_lA^ymFGP53Y$px1FB1s}_)Bo1i8^?DIc-?{c%MVqIOIsbifJ@dB|y?S$rmm>Cleg_}fU%Fra+@)T>9b<W!UWW@u&KGv=D|A2^kXbb>EN%g>!|JnVw;;sAOWvIRG);i%FyjWDCQ^B4elyzf;v2VtZC6KnHcIRF^0TXB%K81J>wMy}ZR(cCN_67lwcU}C2VH*F{uKlGqU*Ub^3&DMcis7E3_}@^usHtY&FSO8pZ=Z(a4NJeUo7|8iwD?luKMk&LiBIEqR4UQP0bN}e?II8p4qRFGsiR74A{?E>hPeN878z0*wnm4K2`+}bPHiS8U&IFZ2eduWU#s26nIQNreI^@IW}fn{JY7~GkPX&2cQlOhejKp>u%Wb6RleV?o5~eT6#Z(8@riWL8zcz8dBm@tq%5$A&*Ss>YsE!|EduOeH?jEfZcj<HK8m3bdM-WTYYJdB2U^tWq1b){?Hx$yVBUakKUvJB{I#cJg~4=1Oen-8HHIHXp)D`57X3S1&-jhB;0-2MuD`1Fh~82EO~GaAE1STiO?j_khHbm<ZIiZj@txkL<+06$4Bz<Am8CR{Vo36kW=V^0-N1F+$P^WpkfOdmR>Ry{?3Kth+f`Nlt;gN-pr84jN%*UzHEKkl2CXIsml`(z2wB$e~D6=M1op@DZyOr`v+jR@~mi&0Oi=M<^kZ2BgG7A!o6qbgIGYk^{PfU0J|T!#>MaoD1Q<x11%6h_F!)pE|lGa>Q(5(UnrHI8z<cwa21G6g)I}2q_28EiTVe8bzW6eZ|$)-N$(9RM7<fZs`>&ANk;aRNVPi173IL2lpF;w5+Aa;=WH)lTNza$u#|AK-m%eI(!fDo`9zw!Rv;sGGX`P}j69JDVRdvc65xvV3U-PfMg@#WMJ^*%jXg=H*)ENSszkP{CpD;7{4y;CsL3=rW59yAfCvK%0%E0F1fw?6#1=g82}cE%gjB(s#!a;oXEDpy>K54&qheSiinO8(j&2adHlX)U(dyDswxlQk7v?<uPJV%0YP^tX?0NBHU&w9@)U?3c)a4;Bxb_OQF{b3ae+<*wUi?ezjf5xZBPg;MB$)r~mrx}mt{257z%jGBa+<z-+L;74TZ>4uk-i;gFj$DbY+bgiOt0tL34VsCEfH=Ll!)L2fwfM?VY-KcY7;_f(qx`LWnUDeawl1D6DAI<voBS-&j*~8UA}G#PrF~?qb8J^y-9_)V<<wnD<sttEoSGhjNjQ4*bdwHKnB<S&%X}E&{G}98$h<2Hu%O5<V!e3H0;1=XIO@IiG}r)hbchVNa@;aK6VQ%LjcC9I$lLFRA(rLS{pps9gdE$*A1B-CKQ8m3mrZ}EG9;7$XiLikp>`z1~j7pr^XxKK>U%a(daJ)JOu#UxBxOhE(ECPMtD|IN_c|D+XhUQ>A!j}1hUWOEBg-$oKsIo|IV8Q;Z5Xmy)f7$7%4d9GV0X{2pMpyYJouRgg_1kKfWRSI4$7Ep*UA@f*&XHozcY#*Ad8sfQ3yHHXFkp=S}`b*yB8AoftM<JS<ShG)zq~iQUc}DunOGxeO_*q8Y~3^>_hw48RndBY>_-pA~o<{;XO8($g&gU~P4AZ~CCw?VK1_^3@VQBgRG%(S)L;MW%jm1NwRZ@~5rB9z-O-v5`s-zFh(n>`Zk5;|U6qu<ylKp=BW62$HZ6*ca$6<@e()COtvoVZ8H{dcu_1h;b!<{wR%V*aaCVI6m}3yz%0ceZwtm>dp(_PukV%|2F72Zr-sc$%|QsDxs5_)zkmjR{|INl~}DW$V{`sYVl%E*4ufLunBfs!)UE;;cn3?JOlkF#Fk<GFLVoE2W<^Y&{j*7fAYt61=?z2X%$AUgCf1~nSD+4)_ve&i^5)o!_hZP$<>LCL5pr-OTqGC?)F$(`2;r&H0018{HI<wwC@OUbJmF6_fK|V_pb1#t_FC}08@a=pA0bMuoWSG>;cY3X5fBuVSt13nHu0D=|D~g_<*kS_Zi@S^x5VG8*(|WXPpb3AgvG%!0Lo1T4Nb^DM|1tiN(Ss<f-Rp+~uL9-O<xf6@NlF{3NX_{BQ6^d9wv{(AorA<xL$KHJyFVQ!5Q1O#&D7v_-N6svt^PlUW^RCmHaQh)y}QKG;{rNw*S&XN4bV!R?re8)@MG1)4n=h~50XSp20p!}a+NhM_CH0OqVNJ=@8@UHGxM9kD#f%?=hDFYVIo;>O}YrnRRU;>1L4Rx}jU{mPO~E`7PGxOnqYqNk#Cf^-?|O47<>oL`@eMxn?KVSTAK;EOM^!{inhPo7a@Qg4D$V9(=kUlhuDp12-<CYiLvvPHr#S_9<U!%1%V@DwB%k##(Es@JU_r@bm+@jLoun~W9hREjwMn=fqud}pp+GEdUQJD)eY>VRgzE@tE4>s$U6Qy%}#mag5Szo2Eq$0pm%TPsmn`aMJ?g2bA2D5a1_)a-Xim>f(76z>mrmh;*N5q3q{+5K?>TdT2d{@vdhI$iw*swMSzWQL@=-8Or~M+y3P@}1*@UEYK5ut0IZO$?<CMRPgZobJx07y+;*F?dbcdXYSjH{O`{MXXEB!<CQqSKgBbq(%hOigNH4s*o3;*iC8ZldDwWbR8X_DjS7FFPdRFGZLktFVL4ZST?))A|2`DSrgynMTaXcbOTPUj>I_fpGmQ3E_A-Orgzj6L?WT%*0bSbzxV90PHNwC9kXk2p`|)xDs7=Ws7blRkoj@d!G|-mj}H|#N$`FycRKy<H5n?BpBa<kI1vO(i3+2IyhNhbT;4Y^7jG;_i{#(vxaY(;6_Srmm6)D{%=sAP{90dIABz#}BneXigzt^dQsjXuxV2ccSogt3x+VP%HrUQpb?A!HZ9O8YloOHA;e#|^#S^6_NVgg+C9;_mh>R8HT}QJ6cDQJ5%N^5QqM1(AKu_eFRySRwJ~XA}3crds3!Ntvc#VUJpn+Yc!i`uaCC(*$eWGsB9$YK`VB6f{fJ%kUn3Mri(wU5n`A;3Ik*a*wNFa*jQeFp*LXs>zBENhk@vpq6i>XCUV$Ez|#|zPNS>ZLmQ!9KKC(}cjL*=lHlUHeqX?a_a3?&<^@EBjvb%6+(?JH`I#~6hjpK~2b?*(J!F^Z=ZJvL1x=aQ?v=2CB5&o<rcl1@@GO{2txH6`7xX$AJD9Q({-e%6>d{pRbQHie{iTVE+p(w4`5-m)F!q?RerVw&s-T|scM=-1w2UgG(qQ@aUcSUi6!oj*MVRu;a2Ao6(RGglzsN%yk@m*0=p=m{IQ%#A?0)hB45`5(#q@PlN!!*+)y0+S~et$jE^TMw4`fe-evM;tF%?}s!CrJp>&`jb7tKjGdZ<0VolhsRiIhI(#JV2YP!6_+758(m>$@wiU+VXvpOh2GCon{W#gcmxdv^H?>qQ}Cs-(S}GQg1ib(1}nd#hzcr=IohjOJcNITr!<h?&{Bu@wy)M8V+fj+sb<FTUw*Z%i~d-bF{}Krzm%zXI*@MFWqU1<p7{t~8bVj6!E;xF=T^b<5xIZ)8MXS!7%D4f=59uLrvt>uyOtz*IaDs=cf%lgTm;GWufMixinN-lrX3PIRZSrb*^P9?VxVA+JvBS>^ZZ-djd*4>;<RJHVr&^_?C->5qyB3Iw0ZPqS8&52%)3X>=8&fjlc+loVD!#^H;07mn!L%zVF*pDq%|A!u$Orex|_MU#V$M2_kRq2lT3Cj?|Av^j_#_tXg`^`_=_KVcQ;~KJgb-N?r^r&&U<#5n@i4nu&q6R#27fPd+yVY-jPAEO7zyrv^Vzj*13Ogw14Nn2HV0rF>Nfi@F5WgSD1lLw(#u*SvYv1pRuVp{k7LU(tM{6(lKLNP(NY4ksmyDrSW`6f8CL5k-f4t$!2-m%OOSa>~{V^q1uLDbdz_97P1#s@Q5W{NY@x;kL0(tg%?tbfa%+n5(pwUz9}yAsS3g!GH)(c2m$F8h^&2?7u&U5;Hn}LOJW|1PH^)_{{!G9{Kf~xasy}0D`UA<fm{bI%0N!qWSGrmAV;F#DTE^hYDY*cb_NgtgR_!Z5Iiv?CwfHI`GCH*_zjTE2(~voTbL5Yehsn;7=H`%!03o%EcBC1!A{a)MVk_Ar!o3TA})o3n~qG@MqXi2qN^oq%18`|*P6j0***+bN?i$%0TUMNTSayl(}|?KCO1t86ZVztA_>F~Q54G!vv~iA{|$0lGP{&d_ai=z31}W*nxb)1jLf(;$Vj_mNPn!2Ie@9C;5s%SWf<w({bRxZ;|;jE+6sC`U5s^#W0giSS7{17`1GT*&=yII>g@VKPOND_s@D!kPCud~zywnjM`IDd^JIMFgtKR)9L5Gz5s|b^!s)<stHW6PuP70luVk06wiXFK?(}CpLa`jb4_q8uE<W&Q3T8+cNF~zF>=5vrqw>=PDS#d?nWR*UF$?0Y26}}hvd%cR@bvP7#ZE-(jmi>*q_-APJ~z8UX%SPt*~mREDS?VJw~^l-5vKz-QVD!Qf-v0?wj*i3<AaznJj3^rap2|o(Mzy`dUCpv9lvxSKF34}nDdUjPI7jn+9ctO_@iag^iiT5G+2qc00SUbxbb~RkA2uBQ`hWc6r`@A;QP-o|JN83QH%mK(L^Q7$HuxsJ%LCqDbjms*9&Tf9KP%((`ET~z7J8tNOS4fAz(@!w}ta9-_AbU&;mJ^tb8CjgU1IwlVLhJZnKU_L?IDjoD=Us9;8Q_Q3~Tt_LSfIO<2|6`UuI;^E}D5Oz1idI#w^vfrhfHI)ukh?W+9(I#AP%YF$IrW{#N$W;}-}<H?*;H@Fcx!mQ7^(_CkF<~<E6J}eR-V4?WD-qT;6F^Zyd{1(mA(U59KpSH*WC30Zq-x5QET7xi(^+H#zIe?xlFOHsJs+h>yErll}a1n4=FIeM7Xmg|ABLtD16TT>WRK`Bs_7wJLL~zXNU`t>jiI0Wi%X=JH9fPug!IqFvebK4}f*sc4RH-CXz_O4mOM|(VH_*g>ki>LpWjZ*94>kB5i-Oo6lcQ<MrbWfG(2T;*ncfgdT@e1{!<rg|lB&t)+o*b6Pt_WY6v*l$K#xuKD{6@3abRI0lepCq`683(m|-J2F90M8nSv=|`>cs=>x}!KkjPL~A^e{&TCPa^VZ~NQf}OW+u6gy?u7&SwY5KT;4P>ZCeaTCPKZ?kexyAf70~uy&4kH$G1vTsNLN7Vka>c$F&N7};S+lXV-A-%UU>~887)R+eE9`Bo($4kPf~GTlTLO`Tlpbu#<EHWj_rQM6xVNcEyL?4h!tN%Xw~6hIFZv0KR1zO5=XP<a`D=1+VF~4n?xwaXEyFiYU1NAz2|hZ$;@ufz;?3l#x8<s%F9Ip{;;|G99)o!TWafg~*?Kccz9<5JgSP3v_{8<LfxAq$^9^?y_#Mv_+w#OTw`)SG=S{&PxI8P7Y;oPDq~ep{)Syz%Mqvb@5h=S_a=Rr7W_J2^EV;!}a_d=gtGNN~pDekdVeV`j@@L!7?Ht5oliEuvgCWP~ExCoi{YJ&~si>IVM)i$b<!yxD{`)q<ZzKGNh=Hm2IIsG6^+v+<M#A()!t_SM^hUz;VUzZahv^51hiU!hH_yW~zo?(5Vj=>lB({RV+)J;8YLhx5A{Xk_5R!nOP>VtxRp^?uE+CeJdJPfWGq(_%$Hb;XXu0z<aZce-@e`+!^9w4VSm=~axr+*oP&y%G3ZYrCJsI`UnvLn{|GIEW#WYj+ph7m2NcoAQXu)`-`t3Ob)0zj!86ehEfK%-R_8Y4MzpEhrdy^TqE@x{(n1|P|D2{ZV`GEEHmv)Z%7Tkhn$sWqY$)tDU;)xV~Bg<*2QNX)X3M=nV=0G5pp@?(1lLHDB&FU6Tc$iiMPK&!UZmpSzNfIZ#<^|=_^uqahvU$HEaJu~FisLHUE$~fLJ?GvY^!ya%kPAFa^PA<hxLcMCMpxOGCfceq_MmgVrJ0cFIUc5KltpoIktbwG=LcLqgEz*enWyKJYUnA3p40D*?zNZwAqOm3om@B>%y2rY>nFG*ReG9o=^B&Jbink&2!YmYOd+fy*%ZUX6=YK@+8pz7_1|*_rkSN_IYk#Qp18+rcjW!*(Vra_{A)((WU73~AYc1yDqMim0Aff3!_q=z<)XVbbjx>KIpN88Uhd6X5;cXz?}>@yG}-^py_Q{I(NA~YXLsdav;J>=322{Qe9q<)u69wKM0@&tZ~^lrtJ!sn=DVtt@EW(G)0qDoE&%@gqMP1+wwLjL*2^)St$hIyunkKNlkvh(FBGQE|DE!akba_+8uR_`j6{L8pNoBqx+ANu0;_YmFaC13<Fyy---|~%!xq^p9G7ZMP7llZ%fFxgaR(PpNmxLB;3RbwmXA*WN3=f+3JJIOw9#etjm2>&|E<@5^%pg#PDav-v#8AaC0;~-?LT?j%<sEjU$u!tcqdw?IIhI6n#F5^EbH%RE?^0cV#wr>gI;6<SD$_%&e3B1QT|RHH2`q%oQ<!679h+u`I|=VarDVL>pX&wY~hN!!tlEmks4I2o!rpPzBF$$j)>8?a|Q}g^~s1Ld(gzi+L>T>3?<Hq(x`Iiu#>)B1Q2pmCwc$|3<dKF@=y6=H}VvteV-3g<8%<8TaxP;V;3QR+YnZ{X+%{J9`peerz5#=fcG;=z#30Gs)t^I0f$+;I9u%UjT5kz?}GhV#!Iv31l(~CA$3K?UO-PwDbQ@*epj?@ci!6g*eb{1Efq)t6tH5&ms=xVqEZ~?gQJPYMQ{P-du;ISmB=#K_He)zQl;(B{GegVM1Z!rW~>P-ix(U3PLO3=e<Upzn`%iiLv2^ki#XqJ5v4ZC^f8zCvNpMXjW4T>W(`l^6rDeHt*?9RR=hO8!iG&<8Yvxmfk5o`%kH<aEGrFv!)dewy~9B`Sm?dQ`oW19?%^op4^T^_LQCT@N8zz)Ie!qS;>gjnzg(1j&KfNfy&KS;<nP_19|6|;78u%mY45;}XR`HS$SY9PKKPLwXugoX4PW3Zeba_|h+`GU(W%)VvT%{Iwb6eCx;x-sN8)u7xc{)&M*~TQDq(_-=#u3(j<Fy8S5&0J%IRs9CME}dkV3)uX^GlGhN5uSr3jRCD}~yYe1gg35%Zsnr49Y`vDW4lN~<|sL5lqT#m~6_>UHNS85&14lU<+v&w41D`e;lb9=S~Ynt-y)(8^?d#51zxJ<*j|B)iYvVfsIQl&vx!4D|9~GRWD9)Na|ZuL}xs>1?a)MC=CmpajnvN@&|Y*_pQClw-NNRc-^r3~vk~?CkF3vH+39<V0orEom4c>CbHIJ92*E+$n%(m82T@cp}c4NuGL=HMJ~IS!Q+;NB&D5!0=!Q+6J+(hP?8sFn0bXK|c74e9If$4sf1;bi-vF68G+GIHGM|oHW?nL|0Gwa&~E&;2wXrp&2a;)RPU?GMU&Gl3I4!;`;CPsTeB`V_slAb2K}`8?ngyDNV{Rqp-J9hy;bQeFJTZNeY9l5(V#N5%OedUThIMqF*PAkavvgePPxeX4dXmnDtm-)=hy~gXsdR5!6wJb(3!Bx?xQgAzKjkwVWG;^M<vXOATw=&kDJYzxs+t`Xjiik?q!E#ej~bxbA|1H%SxW$j7t>I^JM{=B<+OTClr{&Y^<!@V25OU5y52w&JEVh(?y)N!74jI2bEi8tLnR9TzLNo9G!l+HyPcs3^F}=WjN7wZm68RzvjGaH5T2)3RSjMS=)*>4qEWK7mHK71I*@h)@_EOty1mkT&EqCk4t}c?lPTm_DIF2XSyBMO*|gao%)Nqgy42d=FqZbrwL?3zwl~ORqQL2lj};?%lt>O>Cq>=;b!CWseyAz>51{r5>>jpAbWCWBOnk0?Us)AR8l|Dr6s8v0klVFp?d^rFO%nDu*WXPR(KiWGy;{T8Sd!ZIsh4f)8x7Y~4ar5P+zZGA@BQQz78yKs-YG-?1-;p#fM&mCE;1MaM71s;!vg6sF`TDs@3Ka7hso8GVIr!S*4s?of`&w>>%vjV~!ygG@MGCj&}j_`p;HUYexc!3psly(LW9Zl>Bu^HQR-fqQbt$9|&Eo=seXhtfy5$0pld8G~8=-dfXlA~8!wPS{z^ik@NXOej2(P&^sg)J)&%LOtDjbQ8^0=NBww%iKkcMH{?vDvn9?h#*A{6BF}9w_NnNi|Dqv)D}A9MVx*0kp&^!O3{1b&gBU!61;JC2vNVd&bXExXYd~<=CmbcnO{z>HDT|HF)U7|uqcTy$k~cEx~?$!6UyC-#A4Hf6TMgzf2-YNoQKh;Gv?kU`!N-3+qmG1J7<$*hew`^YOg4S)e9D~WL#vXqQ00R=XW7RcnWM6&YX#SC(M@@)T`$Gob*lc@z1_?Zvqbx@g<-{*)r@q+nef3dlMRgdUVbVfh4fpmGGg?_9F#Jy%^(DG4GAh@V(>rrXx3_5Vl@A$|2mKkFa9*Ax{X>i?$~DJjlNDVnr`*I5IwiYs08FZ+t!YHn@YZ&4yH#iMOE6&TUJDa%aJ!-t58H7tl?_X%fk0E0VUF^}DghoI%~XkxWYvCwDxO1A^NS6F^26rzGz1pS{lQyCtmzdeP|iZHn8++Tkgugxo%K9G~$Npg{rWfgp9a_WbfQ87`BIy)GQA84k8nIEYc)=k?W>h_Ht13&Mg12@Ukd5Qjm=6Ia(c9CV`y3&__9?Po?b_49;7qUwc-{+tov-+SwFcoUp{12Vt;_icpVM)+-n-`X8Mal6Bt=JZ>;!&|$<Tf4(syThC2^qc1NhxIzVM00wEdsRG-(F#UO>w!LoDJ0Ww2$t1MLPu3|0uap*Od)QWcti<L$`4VX`vvTssjjwQ+n37I6Z$^R9S<|gd)fNnXB}wa>kWW!!n7;h=;>g|RO3ZoXvEea_Y>HAxTHm`E&;#9%bzty__$KS_SNZ`SF*?D9#=}w!JYmt`qs<;uHgR^eipw^+7b=5!vhSg&M$iio|dUzXi@tR&*ZxOsX%q`m#*BO{w_18Jc7nuyaueLrs!@_8D@3C^{OS}<maRTqV%t@am2JtSM3gNJxR{nCYIyBRJK07JHP0Vu+|eQTZRHSt5hH(U6Uo{SDg@(67Uj@egb&E&;SvycR!>vsD3)_9`NmxeGHfSB&HsnWgEm3FP?3NaMg^6_h-!zMaBGib!vAagB_l0WeCq-{4@O!anTR4YQ+er7q+<OS7Goc1?A<7=@_@}gmB@kaUsp`2pA$olL@xJdOaymr_1N`m+<@k%5}Q%WJ|~5ul}R~qJ63n<mon%YomA4K~l<0m;Zb1wY%OSF^v+47?(qR)<?2#r0~mzlI0*zmz3gF2>LmUd?m-T%Ip6#Cdc!&8y<Z7<rO)e-qi=ynO*larJ5<-IP6_Lx(-~vP?$b6VSA6_N*mmG3ts2JhwTA1aq9R22$6O;xXbUqLjhwCqD|CY^833gpA-1UG@{Bfrm&|{N4E>x)*YSiD?*nK7~Y|Q`qehMzJ;9toU3(R3b;0kckN=>ZX|~T0gc-~{ff%ePf^J1f#vW6iZ4St<>CV8UQd?3(!oYN2zoPcH$8~6W08+0N(B%VDb9Lo;sJbXG@2|$-GDM%fRSEMk{h4^nt~#U8mCPV%5yuRtzxJ)fp8hGGf4lr3+6alExExps34i|ZbwPOO=7X1pW5!NJSb)f^77%xe4eJ~r&u98ut1uhJRmA8nZmsYAWRM|<rQ2w9^u80v>oGr;C_>$O<y^YAlCP!XXJ&@)t{Ax_jxish|&uvg<5=l12N<T*%(BHg0|qKABiE{x{k!HJD^y>ubWUHBYr#>1tS24BRQs%A!+zQ;Ayr*GBk;Tl0meNWMoWixFcXdsBvk%vBxDC);IA73O1s1CC-lojdJe~1%+F?6%HX#csodRdVx%6Ys!=JnGCHLA7sl*iYmlQkG-~PrzVELCh9Km0PQgK#1g7tPg6a+KrhG~yAj&CbT9qsSIgK}>{B9MdLd&^n0<m)=c$Z+v(lq5g=gw{1NBG^`*zZ>m+E07Z3Vh}chvdDO!MOb^;(I%jT?wH0EN8;U`!~pYViB0mI}r<0|u;W7CzzKO4uG<*cHWX89`rBqqit3o2F)aCS%Vj^4(J<`%@Wv6SF^>oCTObzvup^57%s(09@%go^NG8OlT<|K;8A4;Q)Z~q+|s5XC<jdVH9JS*uEn;N9#b!XeT6>%Zm<1zv3cFFcLtCj(|8MMO9c6ser;FSb|9(jjL*K&VzjNrbxRJyn|zEd<1Kx&bxxhK?@LzZ6YI0ASYt}X2|?la02TU%b$W+G@E46vYw4mqDI%N4LU#9a7}yK8ldJFStOGJf~5<`FXL-AK;-8V!yH%7-xd9=-XfVNskjSL7-O7}YJqK2oiC!3ya0qS|LTiHba`pF#@PwNRIXW=%soteo=M|_M9wfrV6B}AUV#-mzjF)4ssr1IFfRZ-)23w`(wNQDJGMNMq!IUhFd4f*r1HHa_VUBpn~G+31Mbxdf)k>JEzg%d+a2;VgmFD!SIg7nE6eV)7vav40TQ74Y%QP<Ot=d7KLDxo0YZ=`-iV|j*bo_OKU1Hc{-bn8{(RzLxOfWl)qn1F;Fe)#O&vu3Fw6Fc=2r$<P#wb26{;S9wA?xfk${CCn=6__#%KxR05q$Qq!$L3C(o^0fak`*rIKeVrDG<22FzXHyh9h&ZJ3=bfQYEOMvD1D`MQysW`_uuj+Mb(nJ+-sQ{GlX0p!A`Y}F+~tW)QuFsl9Xz&Ei?w!+?G-Bsj3hejrh0Y#S!@(9SkXtrr=*(<A`qVi6xDYQW1&Kv?Ad<5>u4kkJsTS54p*FCGiro=lo?J~>Nj20wZ5k;FM!~<A`Ya)^=>`bQ;;wP=O;fx{}OX`(c8rUQur;+F79?u_hB%9xw7^VCsq-+v6e!EBki~uhBepIK5(XiIcoK{39WxqLlf)#a|#|jc#Y*|A1(X?=-#5w=vHJDNb_h}^S`$97Vn-XA3pG+s`KYiUZ-$~QR`m=3i(knQ9;N6*8{1SZT&~V`0N-)0Fqt0WqyWER3Kk8>iaw;Ovs?Z{|36g5AMuVO0oCuDIJR68SW9NZ(k``SNP*myL(i2QLVm>mO;N7#G2T1*PpA~r)f9<83v3KBshpxtr@0mpG_sB#?id&>Re;cLQz>N!gpgL~g291zrb@2%C2JF<5oaPR;J$mWEwnfqsJHt(}KZ;WLehc~5aGTTx<(9&*`TZlTlS#{F3p-L{{@Ah+F_|)S-V}c-AAFaed88CAdIh(=v}Bc|iQF@F8KLA)W48GM)!)aszmZ*#$dl>NP8#3n>)pcWwm@A*8;w3D@Q=qa*nPcID-*i@xC58;=<4D8E3eieoRsVizM5hNhHt~+qJ~|8d=A*V^3~-P+u2HU0@~t$gG5YhnbqrMwp3rM7i+AZ)>y=<JvOkqgdZcJkk@mzes#+Z6K;2*^Sjm$fOe7@KDhkxJTLS8pc^!=x19}MU1Zoc_m~GaT0H96q1BBQmF#}W{RXl86P*9scpz{F8iVsQismfOKOEpOv1=}WBv0<B1K^M4sCuOGI^uv424tJEk@oFAXoex4&OgX5WLu6;wy?~UW6ejl{44qZ!ne`&OlN<jvWg^IM^gC%`;XsW^O%v3A_&FKe#xHJfKmh|x00moLNNfSsc~Xp%df)LT*3V93Iz}=H}rD0xEQDn$q{X{;c5%hJUT#;2SJ~6eoEO6=gS!3!&A>S+bDc>Fvo%kC{I;`y{)2PDDT+*rPs~i8~B8_X@n2kG}th@+%ycaoc-wibF#?KZW_t-K-vv<j69-Mg$>yo(Ldbe9WKH*Q?Ht&S<oyK4g(YgZO4cXj@d@)@)yL_ZZGw!?LKR-TKL6Ry8?a|%X{5ZjZ1A!n(*rEsZu>dj^778)c_gGyrbu*y65A981dHkwKc`&>u>ga+Ip%L6(Wm3T3`bk9%=ny&$AJGj92bMEM?eZUy1&|rvt|10R~<PpRFI7DcQ;}>7)UGj`jtiLZ+8%CSo-3jh0jI+Sc?7E;j%`g5`<~@yYOy{>bDuQjdW>pb@XF0iY|2g{deON^!WR;&6mB)-;eSgW_=e3I|MH$jNdFPV5|?$_M-RUnd^wZL>EC(bwt@ui1`Xsv_!f@G8Edil{hRu*`Ogu<9O}qd`K$5EKqSMm6EDn68(^FvLUoX5L-5x2WN0p&cL{=Ia3)Q7e66cC4u*?v~qBcU5IrPfU+%Io==RLH$!N@|5#^{3MOiJ7$00aaG(~8kD`5Oqx7^xd`6WE%F5Fm4lcw$ENn-AwQm51o5Lh(+6{Y_7B|OAQdL=2<xOnfAoWLIw9V|4MHSxAE-u$ArFjL{5w3f^b=M<2!HB=k5s|CK-=n)gCPI(6nQ#uQg)nww@E$L52$TKBq?wV)1s<{K>7r(5uCy7htL}-E)%;XJ(8^1_n@X+zG<Yp8`5&LJf?H}6osJDVBX99J|Bb7X^UfGc4P2Y=0U!dJr*Ts^ru^MMQ<NizK|GNzPeF#m>e+jgjOB;<2&=Okg3h?NJV!D26*(@SFM>Z#Fguk5)e920xT+U0DjPNtL+qL`;)IT+ZEdNPuKFhwc;rA`q_QoUX!5i<_*%b-x5`sErr4ta^dybRAb(pyYdUIcys8t*;J$GhjxAHL9+0}E;B+w+7_yTJr(T8=Lu0@==nw{Vbxn~Z->C<Hg4)+gE$-A<iQk)@_gRiQ=Sy+)R-DKMW7mX?C-nZq#W6oJ}-eBsy}}H<YIh)BVOldsAeYW;LLnVfq6u*z^4v^8vQ8`UdyERwlZ`b^}&>llUg4O642&}d0O;6Gxo?EX0MP9wvj9yfvgKoj{;qaSPvdk$BX*J83zt5C@7-PrtEo6)FH`WAj&;a({Sd&l^@uDi?nI&_sm~XbCA!IjgC=47OhI-(cGx?1aKXdku<3XR_Q}-5y<P;<bMT&g~Ys=11F;vUkB5O6v3Ue7dO<+?V|Cz<ty(Ku67_wtugU*5x6*&O!FjVHk8RLD+L-KTEqMf?+>H~7-(j4Yqn8~%tb}-!0gGWd>S4J>?1~-cRiX1fMa$v<YD0l97Ni-_Qa-i_Ge7T^#9$5SF6&JZeXC?Y+Ta~K%yPR>ApajwkAxA>Qh%r1MmiSrvDmgY}*CbK;4J2pqZd+J77W7QRS(a%}3tp^Bk`$G7+E_&ChOvFo{h>>BSD-ketZ^TciZ?vg}94Kwo;qnn9(jKg7B(6~K4`u2e~7Di@PdjKrCqsRf?R3O-^hh{gzs0unCR7}<EdJec5(@ho9!f-OPi{{Y0C%G!B8*4_$Ge(vZt-Q0%3dnE0GxDs&JQ58HJ-twDQ>6J$_B5Vnk2Ih(CzvW&`QV_m0VuHvVK4&l<UUo;6&zD8mk`$m)F2dNY6VgCzN=_RrbQrQqmBy*h+={m;_z5#8!0NjcYIa4pMh$^AS#t%}B08#d5@#4znk~J!CuoCIK32I$<F)7~=_63y5!YEcNjq}iVSX?mu~7m=C*X)LR9pt1ip*QIVv5kX2^|>RbQu!|fyyyqZt@og1+ILQdN%7fGfZW{WNybt>&&Mm<%{S_um0I-^(lU&a;5^SZ?|s$>8k9^WEeM+5UYxNk#7)p5LkG(a|U;GgsC(k6v{y%Ot{(6g<)c;BKuG!9ZW$lo!uaHc8w&KX%;UojVKAm-(Gsi_4%euZCu7xX}ocD!=x|SGwKmWYurJq6D74qNnaFA%{{#VTUvd<hJqjRMP(b5x0{x(2dX3$>MS{S;eWx>*mzdb6RZ`)ow?8E6_BTAlbG15un6s#L>vQg5)k|Y9}@O%P&(!JH`@0jFF@#?e1^c|4PDV7==Rj*rfhWH2YK2ypADkY(-*-6;JYBxu8Z`IPT2C|@uq&$$dWFLKjZ`<BD^JmO1@>C5Embnt;3RRd3-}~OH(PoE^`LA4u7H`ss?ie6hzKoj!Nhv|DBgw8S<diGBkToOo)g#$vxm)&;QLHdW(du%%X)m*$NH}Q;j_(j~tRiDV2F#b>uyui5a*xD--iIIL@TfDkW07QEdQ3B`CQTsFO?tkhxKah)SOXeU3CMe1>GRUl*Uh{ehb)X&+XHP3i>pPNBs$w0kSuM40{^sJYr2mxeRqkW}bf=m!VVq9nRSq*6QkUK*xZkJK4frwz+%o30R=1F|fYZ9u9k`*Hzxa4ak@<&jx$pHisvJx*sXunvK%Qxq~M#IQarile7c$e3V&D$SUH>Ez6D(QHvzXULpt4^GbV@+<6#le6XP-^%d-GUeaTzCJ>ymV8bzOze65O*)=<m)_kIU1jB-G;kay(ww`magBX&JH&-xq9lksW}EV3DB{vvs6~<)+5<97-<Az6`m3mRwV@lhOAzb!y}Y6te-Lkyn0^RR+j!P|_GMN9x8#XRFj(+t>?To}8O+BNN5;f-Pq2pN@R-RD$RuK3+(t2GeZjzHbZjOe=Q3<ZPsbWF&Ix9;BfaKM8|5C<N@OWA-r*o^@*T<)eSRiK%O(l8wDH9-IfL*EGMn^>h!8?l59&<!?Zz4awgm)VdqWn~|Ie$#y038Ul%w^J%o08_hxEvKY`+!d-3S5#Kd9qJ^5cE1vnL0v6h8=HskG@IS3mIoDbY@k&0;;vw~S}rI~3Tr@~ZPWgPf94REy;E>nOjTHmfW2(yorO9t;3STH_QpQFjz5TPy+}Tt?n~80%%nEk7`XIdU!@0r|y$9|>&9b1836y>#u3G?il;V%sXR<24XeveTdJ0M@_loVedd`n0HW?QQeVCi@XdKFp3sEE<p$`%2vA`3zVqtx34Roq5FK=LqP8*@+)n2lggd{8%nvKE{T~1`2`R9^btoGDV5KDwuonGn{>Or-bkN2ak+}D<%j9rMmluL%Hr>d?{?~!TTdFszU+KxA$T$CBQIW@Sd4J2oPfyAiksj`bD-iO~}UXz!G&*^yk9<7I3e`%t?9|qz-&kg>gXXx*Si_5n(fE3PG2YN97@p&^`Q-qs(<al8MFuTF>xZebLdvYn&&52Kq=H8Z6^?(j#Vy4|sKvOUL}xP>hd8W``WWAs@+){K{(Oza*P;b19YMF;pFlR9@H&Y7((Tl_gDTWeF;yKWc82*~Z7S;SEIaAiiL-=7202G7*3@?64GDZeiJluD5eu#zfe?(6acJabO~5PMw8~2+SF-3i>S2S4{R=gCtI}SVG3UvQuw0`yKP@$fqd$O$uJ=p-ez(rA{2uPWo%M3t@vg@NED(t_n=sOf8GaW?44uM<zBvKez*@6XL#qY4+rw%v_GEq6Cn!CeW}aihl=ORyF#nCa^}8C&1HiWU2{#q_YZZ$1LV{EXhlZ4wq_P13N=11NyT=jmoNfJYZDXGWt<D%NnzDLn^N}+4;fY+J*|*L_EXYK+SprXNNXquN_GI%Chu*i;F>8v|%7X@cx%^<`mABF@MpHeAoAX;Tz#+o+~u3CMbW3jg{==^|NfOo5IFg7dF=3ob7?Q{)V}ub8=>|lD<DVGZMj{7Y&tu?jy{5U~W0@*+_t7{_@!_rhX0%^Vr+Gk8aM}m#Ghq;@u)|Ph3RyU52Y`fW^{f>OP$;24qO5^-!1fu<c08*c!8R%g_Pb(kKep+R(1KrAWfqu-e_=JLqACFPTNF%Cp_=;TE6?sUZ`c^LM}dx^?m{2bMG%1vzlGPK3Z(RIh7dV$Q4ASPyXL^O&uc%HSHbK)Bwm3L~dA>>9@Mat(V?9+@lI8;oe)E*iA5Fb~fhQp5IL<F2lNI1Yd<qY&B<!CP<zTuY7H*H9Y?t>w2X?$SeJT-{2--*E<4PcEwQ^RB3$e|6_ewk_47?Ip2{eLMlL!9b;D=_~l<`dRk5gms_G3=CnP%eM5n&<utz=y&nI*6k8O9v=E`YH48<+=uTeU~kEFx$(oe=uA<!O9fQgS-VQ<b2+S<ToM!VUs#8WKW}mwr>|bNxBS|Nj_%V<MYZdmC^CXE{K9zSr`C`grVKf(4Gz8l9HgCT*VsX=CG3HE0(sqbtBxY;_0dm@+EvqA85TeH=Lhpeg-pD47wOHoI1e9nw>f((>^*uo?LC_MmawxepG>TYKKzw$_Q|Z<y~fgnU)sH3(DY;;u62B&^oq5yd?x7zAAwEtWnqxxn@`5&59Wmt)(Zn6N>yfR1MhPO%r7|PU%W6*mPgsRHZNQu^P@QJ1S3GEt^7maGx?K0fU9L?own--vM^As87QXF7QJ{{8^Nt_ogE{AtHLrL@6MJ)%`wYEw+k$iAvDf+t!_Ku-t!j?r&h~yfa)8`Bk<?G5$lew$70}>tgFi`zi#F^xhGG_6k<+CR8u^iP42Rh_Y=-xF~AGkzn)thX5b%cZSAsGs2k+739o!^vd{>3wg66=ASXJFFttL~qO`@C_kka|Vvc$}qRNWjH+w;zefrlvrA5-zKWRYipKL&Ve%@btGU4KrDYL(NZuY0Gv%#y1j)`aYuFboX^>Eo<*{aC1xN+@|xj*rq5urzowMoQD(Buuw{hV~i*X(egEzN+j?wF3KXm;zCAeA!Q;@c;34?D6iJ94*Yp=hx*nwzKNLU!&uYIUe1I?sG+$Eb(_(ViQ;xIvBGdZ%k1(?IqtheBAK%UF8PFd@4(H+iz&A^kW0zpu^%KVa}INk|Q`t9f7+cnBRp@+A)IRInvT{3DfIwl;XD31KyxKay((31M&6=yEnVFURdV8|;Oe^c0G@k`SJ<!3M5$RH2Cwg*eX%D-%~zel?g9_*5&1XH?AGCgp_7@|m;2OkykPihjiGOZDiS%>%gS@&2i7Fkaj;kD5cU{A?aeD!4;amM#p5zsHKY1Jvz#<aIt4q0vV#UV1`63e&#jftjhik_wjGNE8N=(r1`ZOfFdZy+1|x7`*4`F5*T%T|hKM|Jn(DL=s`T_3ZCno!~<rNlxwPy7qK-=RM%LslAxj6_8?A=XK-z_PHuYXBf8&^IBDoDu>G$^0Cx9s?%BrF>Wne@XS;(q5yk|&iul12Z~?1n9(w}u8O!RbiG5&@9DaS5KSt2sGN<+eyF_c!J}A3kQ>KJZD%YJ7nVTMakU8Ibbjhc)FxvueCK){Tw4T0?O_qL27J3|Y&A5J>0M+6j+gOnr?_`PE&Zoj3f(I^+#nD5O>UG_G^mHCHcGFJ(uL~g85LgilR(riXlS)p?#}kgL$oe$_yGBsZD0$c?Uiw{SKh4mN~F#k{~>!NOEK4LroQZw*K4LkX5{fJ76c<bSrY@tc9`^6?MTaB(qc#Cyzl*$f~j?vUNR-HH3pK%Pw$c`0sIEtsD#UsBu4d9l+)n;^GQ}0Z3^AI=3*5!%~jMKv0{g1QXw0I-Lth+CMR3|L|GPY^equG1IMSCN~?sr5j`cdA`^oPW)C>gU}5zrz1avF(B$67vW#X~ZkfdIjLZPfaa<ag3r#hjbB7)O{OerEZ@X%TX9|9x9a)q_CpaJ?Mw|H^7cBt|Qqn?AF3*eF^~r(;8gL*tE7~6zl-gGkJ_Q#QmpU`}v8QTGLe_a;32@g^4N)~hOa$;x<)>XkFEmJfrY0mt!Zd?H!bug;QLwa-rVtHfRjeimt7oD^b(-LeAruX@2E{JyryVH@P$_1Z%@Pkuq*^mr4c9txN=~7bFQCB4VcDUTgZQG>RRd4LzTWzPr7Q?QzVh2Wm1T8RY+lLlZ*R?zy(7-{@Pdbyy_pA8&+2#Dfuqg-r-2|qHH*Rt4chg&X;aA?kcc4lp<>-++T{8Nx~=$431wg@@+j8fx|!=4NYl)XSKOucEC%S-F#t6*QQYYlF~GJMI8k=CC(w|j6<#b_9;IT`+7m~K21rI>I+ajSZLk5^K@<HcqjprYJo|_87v+gOq}gej!h<_HMC$0TYlDnDMkD|7M&Bb_tieGzIYkSVe-b$23^n%X)U?2DV}T$^>?AKr?cqz}kygGE8;{JQN!gu?cyG`qiSFS}AN9L*GEA1P`ecoR`Ah%KtK;Q+keQgNCk@Z@K0t-WmeoQ*TEw2)m59Q^<oZK`<@2B-#|-V2pn}`I!qR21eC7!#QdVej9xT5YKy|kDk5*53+19^Xg%e~^JKym+v*P)Vk6~$P7%qnsXu~4j<i$I_X{Yv-&vMB2$I`-Foy8I&0b43)A!)kmVum+jtosCAWv44{{13=f4JW?p**tA9>L2Q~4#n<Vb6UX(f(?2kcJi{*O2tSxt;CY5!An#o%2`v&@%4VIu`6ow(rNWD@h|XO84K6+TjRoSrAlne0~WKGwsM-qv+HU>ar71xr?Xj{9~-_Uy>1r!#VkfdTul)%1OIc^^=cp3=X7AZ-+!$G3oj@zv&oQVxkT)Bw!BStcp~FsOvZbQ<>qBEhLeO)cnk&h>Zg{{^=b&&WMlYm;tHlB9-g%EI_AuoL8`GHK}oxIX4pK*Z``nrRF%l!wTZJoN!4!`e%fx0S<4aOsJ?4Qbn&C`sqjgPLqdSxJGdWM0jYK4h-t_UV=NuRq!z}rKy-8`VtYE>q6`Xw)Q3GVZBpVKdE{g1In1MxsDOc{C%QC81P9kT);|@2SDsd1y{DJGVO&(a?D*kcb~09?XT9tw7vd9m*_M$6V6&}OvvQqgr)%5*b$8Lx-aqSTm*n=wgynIzxzqM_?lz}(2={qq3>O`3F>+-~S_rFWP(M9xfiIkiYhQ7?v1`4j$6YLP8r<^REB|5#yamj0w|2etg5zN8snJ8JY)Lhr(gCk*Rb@l<y_b14BPb&uC*PoZvS2lk-1JJp>e-ZjmoGLOwMwMLAHxCnNN7G+tzx@2Xj{w&PnT8_!$0;egq0f}Ug*p)9XOUN8OfE?TKhg0P<+0jK@IC==`gAv0%4ckBDe1q-~}m@q+kwArz%!;QsA<mifzs{Q+d&r4$j#>>A;L(<`N|Ie0IY(FL1*}4EcH4Y`XvW*)GuTS{EqD?<3zl@BhpX);B#HDY;D}pWDEfz?<aOEPa*e4z1DuseVgq^=#CrncoM;TS$7J$-H{*_VmjZO?)H*SDJl{QT>^D^`P-8mKIRJ(<?Edr_?a5tW&Y2Gha+#vtd3g-<e&H$nUCz!+4SWFE~yjn?LcrHL?9^>f}V5D_TznUR$GvPa;`)lGul-?K7}>HLy#TeWdw===nq=eiPB)+L#i&RjKZI!Rhb4PtRv0Z5!$Bvfr~~8$!N{Uab?QaT)GDo8*?Qp2j{wJ`G^W7Rv7x`;nWZhHq>ZomwuEjtRunS~Dp+IU}Ofpmqp9>A%knlX=e6mF-jckXsS~Ox=c4x3{_q8S@&C#Kb=x;&e=T;f<l+icXO<x)S>!_5tby_V)ZOxZu&wY#Id@PoC^6BI*CsF&jyKSTAmEdGVoKd?;P4y7ai{9Sv>iM>oWfGe&*uq%Eh4rPFos*@@OW_-Q2PE04>|n14^gRnDL?>^nL;%u5R(PF?Ty>a@BS>(MQzwHK4fIy2E_9E{F6&-8Du+Wtg|jCo}L43=b3CHq0Gwx?2Ue`SV2d-0SW6O3=(mv^r(xML%27P$oxFT_P|;gtn<<QA$|<Q5LgYWt$pe$v%)UJa`+FgAYLg4o}Db&hx{tX!|E%!vgr;Sl8(u9sA<<{2#a*7?(H!-dtLgu@)*y)@OZeInJc3gqmskE{62at@=-Q|27z`iP>nIsd@0ZJm6G;jXpmtTR}6wggDU8Tqu~sam&+yR<~AMN*<KNeMkB>yIr-uSa^a+5OC~d$GfQ?i9rMf4Mir!V0lqaE1CK!WEt<Sj-S8&az}u7w?5tK*6FFLBmJFDunmKDvWEaLbJdsY@f#}gjK4yG2WfQxa)8oT|N#R6V>SJ?-iY;2NrOUXE3MuM)P-c!^12iRt2+<NL*2WNkrGxAcrd`xm{DI1?#+X4cYy3$WeoK6%YbrFX8)nZq_7{s9PP0;rv1@5c;W@3X0aFzo+C2JFi_&kNj&^5$pioZZf&Q@Q&OoVEr1|0cZ>=YIP<91t~aD%n?IKG@6md)RyR+#Kos5DWeveHkmKcYUf4wBd<aC8w@!h4-|+3dDg+GC4e^%R`p`2!(%wAB%7EiC%~^%Ik}CHO+f3Z5mUbh^zuEdPXjTnmG!BtclP5LpuvlL{&|9l564R}mTW~VScz8a|8MVIVrA*l?4a0>*zw57$H|i?&$;)%_19n3e|1$?cNgUX3JWen!vvXT07gjQi4m6R24p}D-Rf=`ix#pNU><gh0RjmlFcwU(cnO1Hz!atkSpp%{1DF644>0Vt*0&=fU+3hx&#Lb8_w7@Wk&*G(u^-=KeQQ167-TZ%G+o*;U7DVsE?t&%)7f-sx{xldA4!+OeYJv-XWN6Ccfw_R@Jxz{K+Df+61Klw{RKCCzZ#UL_yRp0>UN}=1=GMSI|7+U_j_>(Ls>9SY7e4P-BpV5?Z`@x?q8#*Hj*eXFH>9EkK(1op2mZEF3L5=<oqSYuyR*Lw+hy|w$h}IV1Q=%tpC}(XBQYQ^xg^zjo@*mWI&Be2dct-#TSx>5+9^+<Zy@SxEB#6ZE?4+qEXcsZZ;m7c2ZtOAIRN3Z7b^+oFb9-xg}+T%1rVBe-`UPo|Au;i$bc>4T=5HV3<?(%W8n;o=ZBM44}r|zpA?67I!G2=jpu|Jiv<Ot=QMuo{FSB=GMpY@1UE)fOM0hk5>nZB@_VxM_V8m`k;%Q-wQ2HTz8oNJd&b<E5#QglG@nnKvp1IR<O#@Juj?QM#$u~#N?Mx-9Jw0sB*VEM1T^JsYEA!L7Y)nY3(Rnc)Dki?uz0Gj2l?ku^PsSH81JgM5P_chUD{Xj4Il6`3A(`fVJafCwI@+p9g?Ht^z;x7<_ct=s!eMz)$I}cZdqCE=2{{&do6l-%E4z@u)x~(ldTK7(Sfi&kMtk|J(I}-)s%XR~26~1Gy3hW9V?f7j0ocg$Ir3Mw*+TBc=oxCyv70SEratv7=gjRV?|sRdg4B*JNx!^j8$Utw=Qe1Cuw=U?P-0BU`-F&k@CSC{FU(q{j^FW-&=O%7cnW4P0fMIK+y}$x%E#+D?gV#C#}m@C7>|b!cOuePtxvf)FDQsJEc5Gih>XTIAN#Os>%mIQd(m!PPDQcB8$oXeS!h!mY~pL?<0X)4`k07G~Eian}~i@RCw8IPbibq(C7a)?m8q#zTH^LO#35L=}OjL>A}w<1>p%wEVnMoDoz1!b&McQZ#!;j9qvR`K!C%yoy$fiKT8#ENw$tR`tSCN~mECu3keX3RIxIYw8)FXh19mS)Ab3HOb*44oIHI<ZY3OX3LnWo2}AI?MOHZzauGKL|RbhhpL9Ye!9V8un6J@6^AIPKpCsTVXkn3vcv^RpnNk4Cr_3=@*oH&D|r*Z0NMh)?L<TxoAEH@Pml@%`7;9HU0z5!P?koV%_EV9Ii_O9$ns&#8-*t6w-`Mw?Y_uIOaJV|wRn$w+!5EJWDk+Wdll~=;;=R2C9I6E@eRvp?>Y?ANQ>+%${)4&U}%jTrKC+Hxw7+Ly3lgGt!~7J@3t}IHF32Pgt+=nHc)Pu2Ss)V$1iG!EYyvM?C8GwMg`t7FzYXU-PwRNaos2ut?FA;AofJ@3*pd?oiBnFKd&VniS9W}@S+e{W9oRMAoVOM%bj>DL*}9SW~t-WXlJ&*dI*IWmGA`~TGa(P5&!<`--ge>{vqs+%|PBtU;gGZ{7ot`cLSs|d^Xp+8;~x+q9fbhYG2)nZ-ckcRsPMrO$FJI8}6}IufU#{EejLA8vKkV6TC#2klRYq4%r}&!-@sO0gg8>gxmgh-mmlDqOa$LcYg;dzCPHs`dzh%s?+ov9=YE_3{eOolGp%~73xY(YIvx&uG+55INORS6A`wbR!9B!Ty4|y0M4hiO>BW9jA$pF*5bX#XMvqX9_rrFf%k`j!&Nu{i#F%LqKAkJbfnLj*7*hZuWQl3HM1@9vqUNMY;rgt3WL&g7+MUMosWNO8?w*ekVbG|{BK~B|LxxW9Sub1u(J8w%W|K}YfBtJkmxn$^5FZ<#HmZ=lLVuX>fcrNy;?ZUFxcLLVwv&NIuJ+bf1dpPTF+TB<$n>R0Cc<Q6SDx5@xthb<lY2ORQ?$9e0Y$CkNMVtWh2jYdp7b44l)Tq@ua~?(;DwELa0^sGNdQZOGBSP@H(KKz~q%UI0hOZ(0z8GtVf8nMl*|o8XSB@2T`gkDjSITp&DtVb2SM-i6ju_F(K)_@Kz0x4Fd~m5`qzVA*WLiC7!|j4ly38@lu?v4?@U+*Y&M{sI;us%%bO$zo8{U{v9jt2OAUt-Fet-uy|ouD_u@sGRom*NWd-fyQ{G%H9o%W{W_WeZI710GcLL4<(cG1<i<1#SJ=AMcLfTho@Tz{J&Jwej|g;GlG|Ot0>>_)#K0YeT_|~rYv&vLp0Acf?~zwm)%!5=ZXHNFcTE3p@@OOJM*czz21Ly%g8P;sgxtVy1D-T5jT+))yM*ji3c{&LG-Vuu;e+Ww9es?S0%35jp8pDj!B0m?{}UjCt4sRBtfc>45C)~Bzd0)DKZ7v1DwgnEgh4zEB&=qEgyyPxezH=3-qMA?`thL#AGe0#S*U`80tR0o1y~3P2w>5|+fuRc3r|%n40F)H#$wo3u8^<QPUQ;Asa$~s&WEso8!F2k!vcbpG`t<F6e@UpW1(YinO$Cn>x(FXPll@Qehp#utxIosU+gB4gwA6qYO8e(if}RQ;KDM#ZfX*7NA^+4*4)q+@<^G675otRd_gRdh2M|OfNt9wdatgfo&_o^gq$S(6<L-oHfj2Un_xP+p!Hcm;5Sn30e1sq-@ndlWfO@4hNK^4=b-&d)HBaUAzuHLgKipbV?k&No#og{o=)j-^t+*>4A{U)hv3h=CsH)2Ni^!HLcGWp6!HbG=f{?Ec`Yl>aTVG838J*1!^p<ZpQ!$Q*Z+_^?paK{hFADNhknR??}x5^RSowjjCc3s_TffP_Gnc4(h_+nl-Sv6>=?alrRtQI^d-zR<w$a~ecM5b6C@uTIWiRoq)gBNz<fpphVjrn32vnl@bFOe%pBr{^df*o3`IPVTUmC_f72BvHbSUz-P-SI<$>=j&+QE(G9p92(>+i%kS@6+yH%v0`vrX-*dPyh-aHOsIl1`NUge$td-YlJ%EJFY=BpO`e`_3ekGZSC^}|!^|4_WtN7jGj3Slu1tTL+2NcG{sU8O)A<pZs%v96w%S{}jwkTMYdzoO;mhpUkPL7<B`^7)__TT=M|_AlqOJ>!<Phi<7mUjI1)>IwOOl{ea&e$6Hr^50)wfV+5d<*&_VK^Okds(<Yu=pVMsOfv3|huts(F_!?P0A2c;5q8J8AJS{=R{3Y0MblcsFj8R27NxSfNdImju2uqbStFkxVio<(I^@X~@gP!7qy|y4+@w1KNnDYv!T85laP2&g?^+BCg_45-z7c!Q=HMQVVaQWSK3f1#sghUX!0KN0h|`Hq)Vk8G#M?tYe@OTR(2O-lZEn5StzWJEHmV3$ig6N|Wq2=vem08R-%&b|K|(K=hi<7iC^edfD}(F^l145lU{_QTsB1>7f|sHwTeUloxI=KX#+g$zEh2;>$rkCP2^Q%_VTD8(IM4ZO_}ZlStYWP&Jd-hakRV_--WPCk9$`#aOx}dWmw&AK=YxOXzfQsFkk^g0uE1cNcisR<l&20J!wv31y8I@;0rY#k?G85rMJkEF++f<;H|S*i3d_oZd-PExNe@5{-~j2<<J~rSXB@bP#{gRJATb%-9uCXLECfQ}9%$S(ND0(5o^aa@)BR*%%F9;Q@ZcLf@dgar`U<W}w!C+|!@L?}O>Njtv?=oR@t`(q@r+VZ^uJ|m!8$KP)$k^-oM#q-4%EhRNDz5!H`2VW!oEn7rm9;MCDMgkCE6TCz5)@mtrSNw737b3y2Q5uF~*+46&+Q1LW^2P2w;(yEE`Gfg2hCW;1RL|FlbfKt$M)##`FyVsou0h!TTF6nTNw_1WK^_Eyw&@VswIzT~D+aRDybj@0gJr`19lo%MpzQ-~>II2B0#^LZKaczfL4DW?+EXLJJrVBEwQ0z~Jr)GrLhgri9AtU;POor1kA#LG+{KzQ#UY6hmH@qA~kdO`NBT+IO8hAo?vNw2P*ymo7ZQI(u`LY_^<7dZCT9)2*dP0^mG(hdX1pMw|S`?>*jeKa#hpvGa8qzCUIh_e_Pg=+^P|1zy?BMcQ{H)mGQA%N~<jgLx{yfnWYi{re1|IJ@{6=IVi++xx-+g>01@?%1e|Tt-4z<A{3A2SA_3wXZMs-Eec*qO2lns9to?mXXxYrwu8Y*E~btxu&U_+v<1nG~LSfA>mhg#i}$u45s%6t+~za0({N54N~6CRsrP+A7pU~eN<_c?{693zK1ml=B!(|8){#eOSf(#e*{rgfOjEp(V!oquigSbV4(-;e$!A(%z|wgaIL8t2!>%!Dv3FsJo84-h_H5nQbKhD2wGnEKxJKPI<`z_Pfd$_a!Kks#!5Xy7^*}}L`Oxg50Tgj&y|D55&fXr3q)5Fl1xQ(C(T{+k`?s_M641on4PUa6gm{eRxC>t98Go*)4A*uxi7Yr7^E2dCWbgbYn85c;9^O-#JnhD<F`MG{tkVs_tW1wFDfDiNeS^#Q1A*-k(nY-L!<;md0_D&F)L2C{4hw>tYG;y(SVJT6A{+rSe*xkzXW=uzizB?PgOHjM|gQb5N`+!X_za7>Gvxi>zyoTFJw{PMtk@w0*A4^hjTB%q>#?(AU)dlriR3ZZ`AM<LeIxr!&CCy6b_bDaLG@UNEO1CmK76-#W1}V#4XTS)<VG#%7`N9gjwU4j#7MIAEx-k-aJq7y(%fbzNGll2TJkfm)$YNmu4xxq!b@#JZ1TMx<{cpljuvA5`D}j{W#zAX|AuKhMT)G*QXi(e7dhYO7}r}fg_d^^5)T`Un}O5aGLjnaR*U2+*lCj)hq$Xd=ztlZSm3%(|}G9=R|)Ci(^#nge3!GNd^vq+HM|-Z4D|J7^f0^j4A(kkP_s3;cAOkD*iljgSracxXbB52;wz#_usODB`+~+E*we~=A(xy$b@S_sf$olsvk)h!cWgH=oW-lH1T<R4ZHal^R%JXVyh}bD6}LG@vfiDAF`1AAbB__d6-+T=9z;|jx1t7W)VGK*=ZuNC`^6QbmBj9wQ6JqTR)U|<egIn3@dF9BYG{~qFc_Vl+cX;^<$2Ey<@NEc2Cqj<7vnm;3>CoHd}8JkeK5rLbfLYq}d?iyJ5H8=S%ELVWcO*2yG0UTwM6C#LIDSk-9dUQXQ$rvXi|-(6=TY29^AGlnUc~6KHgUbEx7xzO}G^zGD1Sb7qP59J2)QbRiD61mhFshre6c!j0gkHTFP~kSk7FJIaSwME1eiNHnujGW?yueXZAF1OU=70<aFIG@7k#sG{vgS_v{sNMJh%4>;qXXdFYZZV;{z6{g59@-T#?pwZSK><TZ#>o!c`JD+EX28KRw(_#WnEXD${L!x##<-?8jqAyzM2wY*tX$dOK@1f!PrGFbznxujO>{u2c`iPD&Kx7bPHCE7+tpD7zJP?!UWOgN+#5FxNXyR$9*SA3hCN6=e#N>rhRf0~8UIjN$4nv?;UY^Wv@?>s?SDqrajDt|)qPmgr;SIoMli#-nbAqk*^0p&R4nUPu+j4iW{W4)&tNoG`dmzbZTsJ@q6f#pA3<EYfw4@T<<?RyeBUTS|E1j0fkcu?mb7xr51Q_biUxpk1t>@Wiw^dkBz$3YJUyL(vLaH;zy%@|01D^=-MRf6+Wq>6QTWscRSuD<JR*n*U*<NTbNbuE%;(Loc_rs84NNpy**H_{rStOXp0|obbcc@?4(87a){FH}ZM9Mc75}s=$EEk_waPQywY&whd_l9#ii(PZsCDO}m5Tsl;&r?{;HvE=-YOby5sjZk_F5ay%#JIb>ooIMB)uv(EZ~l@Su+M0{A5LEK?dSt_Do(Y+4YHgAgOZ<O*%%b@6Y-Ay21+(u$=>X$v|{jKAnjgfiuXYF)=b*0;;_IA$2{BuJONm*Nar4aRu3|bsG?Bg9YW)I$G~oAZF0^{J2dWF&VLyzV8E$Pz$J*wvl2lJe0>#7vRbSLaWJ(?ro>os9GNO-P@7f@coznmvhAQMbrq-cBvAx_gtWHC>$1(~*%$+iPQHi*8ojL;nE`4jP@;FK2iaMaz7@0iibUwzW-2Dn3#qB35rKtiMXOrfpG7Aa4gX>FZ(!7)#*NaJIQYbH5#S1lrEO!})@<nq8e>}Sc8q#?fa5lb6}70^-YQO$A9pJRHy;}DQNI8O9)lln$aviz>oH4=EU+Z0CuR3~Mvr>OsDA#cmOoJ`u?w0*#)p~)cm?pKv<$i+H)WC6NQe_$s~Yn#mtUshyj5yijs7S^T^W6SWF9u#_Mns^xHHxU<8#geOOZ7|1THZ8#qvn<Bvs5xRFdK1{W#j}1Viv!U?!s7Pqr12l4~3*&FL`b3zgUsNPvhP&>JQz0atAL?Rk!fOuMnnkV&~9)TC~PabKFFo_<M92N6H{kFT3xnc;a)8|aK2bP0>sGh>L;Z;$SKU={TTR?+!zR2sukSI)h>+^+X+%aDjSl_oq38X46K^iFZu9YKC!KsVXboAr7jd9lp~Q(tXCuRtkb3?9}OEs+;YRFE2o&zMie+c{pTw<Xt|6wpO1xu0si{Yy&tVMYix9i-WG@IW7B0awa8$d0sVfcw-jy^@dQqLRb;i#?_Zj0l82jY<xyTxG%JxU(YYplNMu0`hqVPIPj6pq$)F^<S0b#^`_-Fnu0)`4V}~>S&hbDLSE;T0db3nj;6k5dl06*mDu<?<lQ)YqN~~YnjC9$QiMu6PSnD00Id`FaXO*Q8h@sheSe(Sh2XsYbxwCTT#6$Dy_pDI0UE_-_U?()uAIf1?HlT30VqkSYbG!d!CDqS0K=d-4v(tyvl-kg&kbq0*2t!<W);-!4uv<!#QYK35P)%KNSUG@(RXj#!>obu60dsRB}b{^e$Uq@C@aYHiK)(o08YzS`KF{T!aZ$*Z7ew2M-XTG8T)Ceresp?rj-F>E!+~%unx>#b0nQNt?*1n^m;6bWM{u3f)b<(8`X%DpRV};^@bcW3eTas8f|$Pp`5PH=<Y<vA<4qo}D~oat1_{X2vN0Q~g`_klk<IaH*lIC0NcJvE7LX4M7a<<$?2fd8eve8!w9E#dwHc{kiIohqwx{3-N2@8~{`JB7Y=IA-~Fdfi&~C#1>ZhZ^&;D*sNU%v4jBPKt-dF2PER{P75`_9tpo9XaGYr$_nxP8(B|f?5A2??l6{^BBEZMZeur|&EO6#!6f}H?=u#ofI-O>&Kdlj)l)@FpW{LX>DNc1Ye&FTt7zs<4{jE(QaC+>m^xwWjYEemU@^N`YH<ih<bDIgm6=8LaaB3Vgu~Nz$jy~Rpe=;Vom1s$&A<5uhFkJ1u(k%+FQn|s$KUx$&Ga04t$s@IoXIfMkLDIyc&bLXc$&+R2eYU)N&=;+erXZRed(_7Q5T<^eI))9)qmjnH*j2rodhDXePb^ZuW?n?4}3Fw1|(l&qoxG|t9|c=hXCL&XoCEHRjmkPLd_zA+W}#M#!!DX<H{=}9T5)yW_}f@Hx1zU-C$va>5i@z7+>@EL$$TEE$~$<W=pdD-SFfO9_-CE0VfTAvf5O4Oe_$89O_-=t&|U=%Q04+R7|-;I-=bfPTOIC0S|{LZZvrUys@>k$O)2iv%jERu#xO}&Zw*WZc~+PIjqQNd2ib|+W+$L-9Emw=g0o|(!wt-{L;cNA75JdT|W8`^U=S<&(m|hO&{g9-}mDuG9g|%>L+a5^x>|Rem}RZfA(+VqaR;7?Yv>f#_@;WKKG;lKp)f99~sUrvJi4lXLqHK<G1b^9}l+ORokSHt0t`c(|@aTKN)vc&pV+%|CdCfrm>+7E`J0y^rARBfcVc3&^_3;KmI2*uQ7xrKsI8UE?Bu7aH%L)^3me-d^LfLbp)WI#JH|R-bSz;>E8Iiyb-OELHU27@D+kxRU+$CnVbG;yTm-0sv@ry;Mw}8y0+O*f;!&mo-{k{Eq--$!2ILU&&Q9<`B&48IlIt!&$eGoqVoq)^7HVt!AkMC9c&2bxtyM{9ALrBlWk+r<1HB_*f7R{*|t_Qz=B7XOoVg)DqoGSLvO)e)9n6_n#=3k@**l5%d_|5%Z(kr5jD>A?9S<i#l2hZ!HbpF>IWynvnpJEgy~y9J%XQ}!ZX-=@N%p1u1;?6sBhR`XZKuaWp%|uSWeE7C?TX6%1B}kn178SfbUux*iTI#?JVb<cG_QmXkmIg-Zm7*lkT3MjvqgsZk+x-{%tz=Sh+_(j(2`~^4X)EJePz5Paf9UB_6rk(xaaKc7C4f+{Wp*M^8F$^TW3C;^RMkUVDUSg#GiKM;{Ak=<&|uJ;uRN?z3!oXB|lgXnWepY1?*U!^_W&!KS0J2hRVFXVATA&(T$mHvH_C#`_#M{JFP0eOs4}SbjMB_UPa<=ZV)IX}9XDOCK*a`26olv#3<Onm7B{uw!e_e|UbUpWo8ShN)DZ{PpGUK_cXjKD(Aryp`b{>nIn`tfO40wC~QKBE5=M6KfUknU>lang_g{<0PLOcIQA2CR?V)G669)l|9y6N^ZsrS=k;EA-$BxUAG57Cw{B?chNvUkEC%@e)bM{9HdsgQna&{>OfwZZZXj#KX+$92Oz+2?7}HQFG8?6GmF+C)Ivxw1Dl9uXkj&x)Up!li)5<+akLG{1eB~qL0!w|2Wt*;gt>87I>~@!4OQy^>ID#?W9j=MCR-?37TA&h6P6X;KubKfW6gOJt!u(sYl1l7&`ZdkAWqRnv<A-9+VCl#B#~!N)a)q#FxskC90e$ScRaw27Nq_KAtxj!PK{n?gjde_v0fbVZLl62GV+Qq!W$mK>qY=B(b)>IfZp_I>u@XpmOHXGYDxP0CURNQqX6=;0q)>{TsFVJhqwn9jr*Fzad`0QzS`1u?gjvBkg^8HKhD}d_y^PP4DsGZYJS!Iy@6XC^;(2LTknDBSQXpwha#WY*bTP#AlH(BvXoHsDCk*&G~5F%m0Nec;cXM~@C!6K+k5w#t8~9Ze*{8v=a%GqK-c(Ro+Y{%M$tu37sYR>DBLKwi&&q$1fnC_Lb;u9vJ*#tu=NBqLmQO!H016`;=on;k#q-GWH}ObyGbFCl!|PjIu!rm<S@bg%#{)aZk$Onp8j>lcEYjs*g2&DT!^U4F|Kr0J?4e0oGKPd>@gBxRX=)Zad-!Rdgkehf-g#TVfG+Ke=Hhr0wXm`AD_gTlFr#nOdpLy*c->9sNkj}XJU-wk=}GQ3El8!2*%(i%c-bS`q^vBM+2(xTTj#^9f6y|oOruRdvI6BQhL+e5C^mkM!8LZMUANola)BT8p2LNyxj&WwF%!uI<JluH%Th4BOD2(YfZi`CKW=5I>6c*9yxRX7A4?0LV+>?X(7UFVvA5cE>Tz3-~g1Uy8?75fRBwV-K6?X02vwOHc@+|=fk|vK>6K{GzM;{JF}!jB;Rcyg2`Y?jec%wt>aGq#dYCs@AAeUdmip(k1NBWtc!(EyTyhJ$PuKpo8d_pPRQrTdc(GxiZnVcm_)n)2{YFGA0b{UZ`2Bx;4UpGODeGRwH*kj@*vr^RT>x$Vf}k^BdiNo#UMu*D2;7yhnDEE0iE@WPynGD;5`SbE;z3F=`TLNJ_&ShKq>c7;F4jI*0#Qyd3AHH{m5Q+7L|Kk7jf8@Ko5<zN&-~7IVxA&4+TaPOX-rhLe4gAqKHhI;fbs^+;351Ry8e)BOQ#y+~ZZlw5Q^MCrI1MlGoKX@wKR!DOGLH=|)oRkJW~o33aTf_UW-je|;ij+dk0?x>m){RS+c`V+U`2p=7g|%*WLlTzzb*ufgcRH;)Jn9_W0T$XEAlaY0-{eBl%qL`U9Uuk96CJ5{LB+9Nf=AWw=MY*97Ft`og1Ym6saHR^e#=tdF2aJ_~LMX7INB`Uzji4X|d{LDbQZfE4f_axi9xuU;=11=o!uCliM67}lT<yYBqC4ZZHROOW_fUBwFtJlx}Vs;zlUh|>=aYTQ45cK4)spg`u$Ah3<9+MJwWdwMZy(cnZ%>`g*Bfuh>;P9@G#9$8xK?NCxnJVnbIN&56d8+7GP|Fe`8=4S_ePTdt87wr-*aUQNPmgM(DIQ10ov9&)bnM6(lm6RaI$lJ-qXM`dM}VsGdBvnF&SYl8)ztZz^j9d`c0`|Ig`n$nFm51`S%wbAWi^uLjWw|Ga||8u(EI@#J$u@oH&0gFyLQjQ^06f%$!s1OG)tBX=It7FTgQWjfQXaT;&jBEFnM=0m)}!(Vo}7m&W#&P%^(&sE{dK4AjhLe1eN0RWO4SADAj2IIpcupF0*>}=L93gZySh@^-V#yKW8M>V)$m|M@Tk$$}mE`$>4;)KO9x_$es1X;}D(`{cZWm(;u6UHmS@ccW%Ieu^IJIzJ1Ps)8b@8TlUY>c2-J5WEI0n@oJo}TlK-uohUb|lCg1C)as}84BT3uK_dFMpJ%`2k@qHBwQwX6`&!|JBqRJp#bux-R<m_04qO*i3c=)6<74BcTUN8YCzgK=C7UQVn|)Xs_0Gs5Q6F>bR#BCOelxg*0uMZ8Pd-J&l~$8lW6PKrsT=%vHs-7cO4NaLw#Psu2a37!NmcSFlz~~bqiQBuk6|N0dRfuBD9tph1eGFMhuD+%OO`6JvZF0&uhl?ZhQ_fP%`NjYvgoQ|t!!eUY|nB6E6S`;k%64--*!Yp^aIimrE^Ln%>|{Ac!7qfdp-?OLmHxk-pnRVWF=ahuo7+Ii76R4u@c=rDL=ycsCB5Mb}0rJ75Du}+(h2p)W<p`v2YW`!cCOVyoSqX#6*gM<c<1Jilk<&w3E68)kyFrO~vP!o2U(Pz^%#$f+Rs@vB#Puv1pP+S_RT1;rum`5lO1qi71~Z`SwLY63pFelmv1Tuf;)hAVm@_0BMy>CL<&sKhh1wLN`>SJ}pM6k)Q=)JQXCN(AKC%5@+N>66wh=QQb0unh#I4Jf}k<!rkkoNDP#5$R^YuOObH8yre_IDEKGk4*FA8<hBaA_53RqxjFFiTDez1of``T1ESn;@NKlAknElXSEUFo+b7vB`kG4~3uMSFERtw;oGtgXx2y+aJUbQ9u&By3L^G@gY*Sfrnn)89O6lx<qG5vZrU-BVo*Gt{Q6bi}f8_uRsgQP&+|781_D)r2d>n)}L!=flf-nl(=Xbk@k=yQr58_IuY;j3HM?qy=P%WRcOTat}c4nS-KYq(lNj}eQ6$*kO6a+*3FAs>d?^z8mn89g8{|iNh$)qBh$c-BcrFNdmW5rosh4C(e@fs6i=v8xzgabLT5$VBw<tcsD1lJqYH|XYu!e0Q^YtWP8<=1{U7#JuIGx$i1XHvX9gpuG{1lE*ngcV?wNreGB5W*Bx^&Rr0PY%^kROL<NC~9GqjS(htY>-!@0@|%HNpL?2U(iXb7%j2p1-}HGX~5MR-hilFr2Y~)jgmyd`2wKw#cN`Y$zW4{{F|@U+v?n?ft^7_0_`CDI2iW{ZCR|0xM%M*6>KIP4ms=#e}OBJFoXIKYU4-?j_P($|3uJCkXBdaoGsM`KV`_OL2!`2qS0BT?<hj>fwTlZpGJKs8ujTz$lWPHvU;XKJr6k45||0px9248I@1zRYSgJ2{Y;>~jYhZh3@rh!qph?AIF1(|N=V?NIskv%9DrL^)1PHf7Y$^HLq`VnJlPSJxM;Y1Z_S`fH;{r4y_c(nR6`QC39|LF#b6{J@OM*YXk{-7JEP$Ph7HoAZ76gr`NegJ%p<eT^MH+V7MX`35NN-ERhONstC&tkk}2lNy|+`{t$9pC`uY6+^TD^q#TuZT32I@=6?m4WyH$@|TAxVFRT&2hddIIm+jaULL`5*$?u>ZR{H8VTrI$+S%H5>GCDDp8MWQcanisS&FFe$wmB-XewN7&^=;V9OBdgpVTw{M&8KwkF%!W@8jPbvh_mtaXiRB8xL^-mg62{~(;MHyEQ8bcc0;P#GoBS<J+BMU;O-ImQOG|;YCoQl3Dt{z{^BswVx?9+4OBt+Q21$N)7Nu7ZQ`#}NKad0uQ^r5^44{Gv`Z*bXMMzQq0N6lo>HMa%$(5h)I}~!wP4+Xu7?3qOJGA%k1#+Xj9-$Wl?risfhWsASaL;82Y6bT=@@MkZcTPmgGDmiCV)~bvZu%P(mau=61lV#XSfL7%A>G5usAbIUu?E&uRdb}x9P(AU^yls7U!AzL!wDf$4gQ2J@J48(+%`K7VYU`PJpMuckm%Tz1IOyLSmUFA&>An694D5Zeg*$Yq-{omMakxN$@zPUvU^~!Yp&$%BdOtfC8U^y!HH;&L_V+zo87TS%B(9!k0&9%XmTQwWuz;qkWLO@Gy|xL_LMnQu@HXC^btWUOomn-5Dz6ACy1|@-jwgfaRAE>0E`AlMWO`6r{s%igq=bH(YFg!)77`JBe#+{WK}dt68LLTKW9$bk+B)jS9-*nE*>C|{Gnxwut;<YFD=f=7L9p=bFzh#slhS0dQ`Ts`#`dVo^!Kg3*!~Ch0@yHL|FsRku5BC#s+*nAkBHpWZCe1%|h52&D_qQ1upMBjwu0Y7NS)(y@RxuT1nB(vS!gN>OdTeE2hTcQBz}>X%@B+<*|Uvc{}5PKo68H>%yVu3Zqy^++XOM{KvL7ere30QLglfWpil3vDc8^AH+1UJhG))+Cv#M4!ldlLTiX8lfNQumt;K!zgvN9<am5&HGZqKJ$07szj~56JU?6{tG#?;#9U0MRWejqqeF)_LA4EQQ+FY`X89dw7&Rdk4Y%a1;>40}wcjvMSzk!H9S^Ch2z?R5P+NTfB!OBBYV%sr%4H(e$RyCEogG%;%VSQ=b>vH_nM)8XgVTY~z7|$0<v79utCdtzP-J<7We&znLu2`gsgL8GO6`VzK}jlDAa2a!xoR5jB_*D3``IbHwO5@G<hCTVN1>haFL?0-HK(JQsfdw=jaHteRiwn_3Z%@+i3%$3Fzd%I5z6JJ1j9!j?zzqXfdlT$Jc7T8C91(I=0I;?v`{)G4t*p$rc1Z5-NefH@ZfH;1-_tW1;YkFo)*eXPg3cDjAi@E?;j9cf`xd4c_l9}_dN1VHv0CQX-4@m{o@*A7G*@fVRcWrM}52WHB|(#*5A4}PJt<oV{xRdO<iTsF}&ylSFgAfpCrON@&A2>rvT57<e}LBxUIyOWZfu8f$&1ap@D8k$C-RI1BTg5Cu8J-fUzdHL$u6OQ(M0}PJ3>R|L$Dq;nWy_=WNL_)n}#UB^l${F>Nsk>M7ybUM*v|EYN{L3D2IIu~&g-@bMP<l~{qYH#zX?lYlWNcUJ9%xIl16a>db?X{g8*a&jRKVEL$AF#!Mbw4|t45xbpdAl)V8Oz=1Lk-#kD3!gH(_?y+AcM?rW->*bV3Uyie&pWW@Ze{i^;l4fG8NC@r$f2J10F0CCBl(^-iWX8!4)2^4RA3k*<r9tmNbvraVEk6RZUff4>>QxKZ+zWkFPABHMwSNzqeC-59h2EBD1_t-0o_Nb0y(H@td(5(2TT~~i7h-g_g(Lk(a~{Hpdz+sA`GsxxKnYeU@TXI`!)y_$(I^IP!+}T2I))a6ZWO6Zt0=5j7O~@hZrQ@U7PSLA@PViVYOqzo-+<(UvN49z)=?QJI~J|)+LMhWAFapEQ>fiKa2Qw<5Z9F77|LwIm2%_)={`AVff`03B!Ep?*Q`7Y~ftSB)ENiI#oy+69yptMH!QLBxBMNO<JEx5=y{itTjcF@RE8-2x7jRNteK-UFa!Fo-h{Cl2ysYC|fuxmZX_t$!WIm4ZXP2Y$5Nc=##`_agul_PGZ?YAK#v)3Y8J{Q?~G&6baMtteUxJ&hSUjWJC1lOxn;tBVpLEC65w@-EqQ@nT$tshM!t*<o|wl%<w4jP$L+5(FQ<51t{hMmp!%tU_YEU0LD-NUgHFPdX5b+^KC51{#N0=<s;Dm#sM_RE-ys`D2aKx`dcW##G&67HNkVsJ%!vImiu(A`%f<VvfSsHYIFly1{0H((FHRH1Y~ut<PzwX=y@Bu3U16L(7x{<10NNB=37%FmZ}~Hf$NN7a-K+F=(s`_`K-#trvu0SiFf1+Wj#O>MewWY3C7uv3IG-u)!ktMMa>qfosp!cLut@B5po}hRCds1oGK~Ola&-b-btQrmia3(Ue_#<Sh0*padcHu+^Ukovby*=Dk&mFrUME5$4ZKu!%B+W4b%Vd!Yuj1EcwD2_ww<jg<o3urG;OZC102&UzjCdm?dABC4U;3CFAechJ9g{{KU+X?%d8;HtG++ENNNjYnUa+je2C3e2iAo61J)EOV)~aY!JX_W}2jys*Yo}zh@$y6iCV&SB19H7)@4@zwwL(9xwxXBLy?!$T`!ZpY#2lW0O4KSe*SG84M5D1I5_r6=|=GWH1uwdX_D5q*IK?M386y9o#>8HOEJA<qTHH5D$1H=TCH==F*96jhA4O+<J8{3MWW4dQra2I2H@h+vPoTMoVwqsYvonk5gFlCi=+o=Iy=MyEtj^>4$oQ&W((s^V>jND#jzSNH^*4O>B}!kE4$+R3nKbaR>8WWKZGT`8Rk<A9?VRd5?)6)M-x`3q1;(k4cA(T4(~f9DF<?lynDFea40N2$kez#zr?i#RaBFUp+z`dHP$|pXZJ|&$oE#(vR^-79PEHnfveZ;}}xrk#F4vYRfr6q<@r*^85k*B5~v)HQ|#~h8GVwWH6j}74HvN2oLx8(*x!-g-`4(m!8u~o}s+-kFi4@9dk(dc-*m%$s+wTTE<<marPws0=uPsJ8Ki&@SN{;&Hy`pJow4st<JWeVuaN4ddvv<e@@A`+v^ayZ)R)+kMnl`kt;avWy%^aVD)hhP6;>zptin8(#lx#&Zps4&~dz~{%6d=u_E9MaZS9yTGJj<b&xD8x@Tc=K|V6p{Jdq_fBkeC4nWzs8R-P@?29>HO<n4I9N@k#lq~cmvYO%fOaL2Pdr35o(!xo#wE)|Q^aQZf8ODanz$Nd7ilC1Tv-x}86IBZ=!t&X`T2a%4Q%EiP>H(ydh}lzAtwCy?cxl8UF@mV;kB+Ks4X#m8wFW9RZh?FQ-DL(FS3tG~Jr(wqHsUhc@S+2OH1)e6Yzw?LlncdTuNnKK0mlq#n~F#AmL5XG;*m$7wy{8M8$xZ}1gtgULK9jo&|3U|cL1qfoP*SAVm9A~R8mL8IH>^S-yc%D@rI|>ET04vUdxNX>~i-MlD0OY5N}J@tOcA31}6+HAHm)QMNnyoj-&ijAZgP}-Rg&`TaBe|wSND))o2in_4DgiU8!4buB%&3R<|mkiM=}mm6p2Ik%-M*F@~12(p7*ds41URD{@j*q6))#0jr#g&sn|tN1jdUO`ITjq()M2Vo=iV5N@(&VIGOR6~9SD_ASKR4WJ2Nrox&$XeYUZhX*(8ijsTYzGL_4g%dCE*2ZQ!(1@VMzN$lUxA#^P6sq!(^KlQB(5eQ(mD^Ii)Q(3tcJ06P0h-}C+~&hGxy|SBo3O;etrhwafpcSon?cIP1%cx^n>4FzgsbIzSe4M^7^7q`0_$a-2o{j&wiWUA+>te3=B6t9kAifr*_PX8tJ?vphg{5mRrv!knJIwiNq_`1V1t^Y;UD~19Tc?mrH|@<lRZbxo;plD_1v3j0Y=@b7p^cR4fo_bRo{JJuU(g3IR5J(?_953SkJoY04GNc*1k4o^VjU7T|)1SEKZ2ut^V{}wLP69HV%c@m<-2GOsV37Pv4b<y%8H{YatN}nePU8VinsCC@5_S7lr`|mG>f`PD&?W(F0N0BL#9^F!F1n;Cd3haR(+M_zgyQta4L83vmhW@~fh<I|+$lJOdzWQt=qdpgIP?x30i&%!5TpoNu@Zg@ZXtEU1zOd;~c$PuohV9elVQSwUi<Hzt7(3Ph6jbXcAns=NogdGHQ3G+7%k`ht$OZlz40?+U=~z`4W!VRt1FI!MoA0zRC32D~L<t$Wh#B4{uBH^~-Op)qaMTP)C+^#U!B-h|Kj8ZDlvA_~X9#98~k_7+~OocPvEEy?rcGZK!ks0@#?Z#w>DO1A3)ats3nOMmOFpi~~R(Y`FaDBWVw<7wR}S^`JJv+~$DP2<RgUMVau{zaA*!jSM|4VE~@qZ?1|Mq8NHyDv5}?FaIN`zfa|c@hWocL!#vn#dR1TqkTpDSeAG!K&gMxFYzY8|EW;GlX@*F|0H>HzIehT%kF$z_PcRIf+;4;K&n+y?k^d%Kf{Ozrp#LjEARv70X3u8#Aeou^o=1J?63meH)rE5zbSO!FfNcee~sttg!>{1-I0N(fty$mkQGD!Trpw@$;K3UqyD#I#$!2k1X+Se4*x_S#MDRpD$uyO7|RfvvU5CLeQP9_OqCI**R4K%3lfox2u2C)qk+sqze4g#$E?|5@j~KYLQ3q(#4h}W!W0M;j{}rIt=BwikNU&s};6lr^cFX)OjokM-3md8LEv>OpE39e1WK)7^*@xZAnJO!W&%F`1?H;03)UXbI}srnGJ)SSzhkr3S1D8atS>XKE60(k+-C5bHn^Y6G8wpvRTS~o}b~&z)x$a6+bZEOojs(r}^<&7fcljE*n^bc4jfum5FXR?)2CLJ}3}qv2N$i7F`;=+!LA608)L6+vB8$gCTd|+&u|oF`@jO^QG{ypyT)XC`#v$ouMU1$;~}EAmkU_yVqD}LC&(}M%ZKR+i2%bWkD#0T;2L?0x5n*>IwGy6%uuLWdt_&dy`&hH(nLfVn*<Ph%?N8{_Y|%xhWZJ372$Yn0&MucUO%-f_9XOsVOahSxa?>d}l#aBrYv0wo{P}@u=>MBu|mlL*h?JG>9v;)OX3&QCCuySpHf$iMTQR)|-S(wwjVD!GHmR6e>Z>1cK@ac;gX3-%*PYt3+lHbwDL?tV^7TG!d-XDie6*F+){ICM#pFuv3lytOz<<bOo%2iczo=avtUd!X!&#K{$3&t1{;2LMY};bx>?FC`uC@jG|d3_+y$kj2pD|cvD4c1VaM7GV;hIVz_*P-+V&JVhXK;Tn8l;I}^Bp$<V{`Ag2$!*o8x}TrjdP$?JH&v?^`0c`J9HMIw90&WHyB8#Sm_=r{Xp=Yg&W#*WoiSPnVzJb34xhCWTGL0##=PPNpjFn8f23Yd2^!#U%2ilecS(m3(o;;y7csBcAU$8j4NmB9?w@q|jBrfJ3Ct6agbGbcwk06rLYWae!ZF7q~Ju{M%ydG3!K(B|ZBJ?G5Hlku`jd%TLp#!*MXy&*x&@ZkH~YKv2WBtEgEd8d-*{C@U$_g`uh?a^|BBkA-#>LWxVoX>ze%I|iEf%h6zfK@8Z4C>QeZsM5lZP=QnielF2zQ0B1`y#&pEGBVr&+b}R+kEq_v9JCB)ia_0K}8A-gdy@He<!-HHtc_9%;B^<Zinw(Z|H_2LpKyFH;5G{PiR`%bqoYO+|2wdMi)2YfuUkHFs)V;<+WyjPzH$PT4mltmSvDtQ|z(8+9xmWYdq5cz6H$UDlzer93t3)>uHG!2OHg(9$R<t9|Zuy7;RO9u=RW~eu9>K%{HvYmGR@ojYBau%a)4Q33OrP2W-p|o1{<0JQB<tb>**PWH@Pmm>EA4cg5^Nw0Kk5qX0HcmRRo7&kQyiRG|dd-RQVGs~e4)DCgmS(>R)4G+GME&vw@8)#Yct@_ydLqmAlATSQ5%uG87P;Cav1jA5d@o)KEiphx64Y)g{Ft`c0qMU2Lu7$&L_LDHz;JQmT}GHoa&dSqdmq3&f!lS-_v%yD3#>i9qQ^I+Dg_$_da;XiqHc6HQ9@a}ET6rr2vpDg!7syVW}qrB1WEvY&cHg3It+f;X)AW{R)oQpM#d3+NoWNHV|=KO4h@>?=+&1l+#W1(U;FuR$&0j-aLHso=hG%C70g_fygfbmgRrEbx&GI2myUAMFrPm1xQ<2LXhcNNvsu(M?-I$K^_5~eL3Gn;pXW6e#8%dWO6!nX_|H)H<8`JJy?$dnyu1I&WBbAFJI5WD^HQFZ#y9#*FhqBodTr@t!I=|ibbPZv0@-=R9aV|99Db$UFhPXAVJa>G<j1?pdy0`)X6P)`SR);|bUokaCFt4{ZBQ4@yA*SnHyUCPv(Ql_3}jMjq%FD{m;Co5AoAiz|qPDbnIe6c#U2PwueGFl(is}D>Orb22xFIHcnO{QY?rWC8231(p{<p3BxE0yYfK>xBzb?_~SLyapC849Iw$%KcZOIETDa_n;i*J)O=jzAozs0FCm&sD9*C+gMF^1f86r|OFf?AABWW4Au8R8Pm1>X>TR<hXYJC#G24x#!N{*)ZLd>=LOyFXLnK!;KJ`bBuLQl&LexSS$SX&SmPeJY$4N+T}8J&HF4??=F?8lam2?S`IjWTB&{&Lrq(9c7X(Wwd~n$;;Ffcw=Pb3#zo=Bjk6;5zF<=nM2t!@j-++9@z-?5Ut|9kH1HEstyePE`9gff#E8FLPi5`?kql$NJ!Ds>q2`lVyCoxIAe*Iu4nB6`eeuss{8hh*U`AR(XQl}d2o<L$2SLn(Al;QQ!H$`Ir`qQwTSQhqj~aQ{c~S0|sK||2N4Jk4yR}$FBMNK=aR^KS*U$oAQ7D#<4P_i7rcnn-6;1W6a7P1KY-BifbWRC3gJF}q=fYAkItKZJ#%f{~q_Y8EHrX9FV4bZR2G_gF$Zlebn{PHw#P2<SC_e4{q(N-Hw3NX`DiU{w@*$b9mguc`YRStZN4|UZ6th8==ejAzDR|Jm&lJ-#a}XaT#SF9}kEpOtd9Z2{`d*x3OkN7qn9;S5Q)5O(uRL|8`~e#l-2?m8b+|ke48WVL5f!QlYiK#w+*~u)B&Wq)YxG@7ZqJyp{K#;xW6079HlMf5vdtzMQ}Gd|A$Xf}TT;RLt6>dpq{+<FN36j8$VsPTP)GB{@D#Yg6c#@pxS`)1$jxo98y~me{k#^X3Y9r7#Qwa>T)0|gt~1t{0$P1sWv*t})?~A6#Ek3m{!#L{5yVIM03kq2WVbhd0_&~Ha7kdBWq<UCj+s~H@w`-4dxFawN{>t8O=^wJ*(ANLP{`UjQpr$j&h<r1=2#EQM7{=r1W%OZy35LP-Sq%E=#9?ctq##aw1$>~s));7<dw5<0g@<;Cf9|E>@97Hx6BXrvk}vLGL^aJ*~`f@IF@I~xOg~Fo)3##y}zK`)yOz8EuULUh>Sz{!i!zGj1QPy8?xgK?rPKZK%BIw&~Po06qmmS>`hET%YQ-RLzXq;Obd6Y@eq~!y{Pff6=dgR!wMw_2fng$iekq0PvXFfz{8!;f1-|4bmdW*2lu%blHu15Y}g$vDA=(11{y;kk#3cPV;6@7`9~`dA%cz`!ESP`-Z5{-fOQ^23-YcGBNHpx+f!>~?)k_E1~DEe4;u&3p^AvBsPr_%t}vgsC$J|L^&T)Ef`5*tF5|^87-5k5U4(twZs`7piSWPW&oOcHoQna;yuesI3{}ajMe0m1IFxxa2($2qZ6SnBir4dF{uOODq?eIb-cdz-fIv-Ss&SSp#xImf$vx$_4%+($^43@xA+rS5N;EbQLowxPXkDBKHu>(>@H3#X?Lgm2H^cOYOq3nQreD#f$Bl19`iNU@NeJ$RP~~8bXfXN%jYG^okM&?+?TwzeL0Tjam7!$|wah&>R3y}q_F8a;F*Wd|Uc%ZWs8YFsMwL9g!#gHJ+w!qY3TSu?(G6x9jmEgfZMQK%+5^aZ>qHyr_5qMs)p7$N5)S}Relz)Ykd!MZ6lGK~2>-4pQeXLn+{XQb``SSt0@*1hShl%y-@%>v?ydhicO!1EH(>PNFhRB3fjfPBi+MXQ0sGs?=@A07$Z6ab66ZZ8VlIjKvhGK>AsTWdTW1oGWA;hau|gCmlf&b`_fXyK(A&P=plx~{R;S~Y?W|JE%gXltE8An5+n;1vdrG?K<1T9!osoa^lfA6{p`WN6!rL|R%Uo11WfHzYa_yr`!k1?=2`Ac^-w9O<6gJX%Q!=4pX4xH3-F7EAglnj7yNfvlKIsL*TfySnLU`NG5(o_lZ&i8Y(X?K2N4~Z+f}+|OwTgM3BonGZL6Jk++c*=+B<!Rl6M_(mJ{~jQ3Xs7}0&ZB<Lg)E!Etx>{nJ93XPasagM~s_xo>G9P7DUeAo=7azCip}mT-Z<(7w#}mGI*1QDvY?2o4q2>;4dT@a<{2@&QM8y{4E!iTD-WVnK+kipfT`?6Au5hDQb2h{w(uSuc-IaNfHxAq9VcZYb|?32R)#7$9q%v3lw=mX~td_t@bmkd+U-fH8hOMGWSbNAVEG4I&5d?pj5hiJE>@zxLI2SHW^d`&RQ1|OD)wq5f7j@&)c>LM=*KMJK+Yf(6$1&NyGEbs(cW~-4ULIF2-ot9p}>muYh&F$7GO3CW!}z4es(esp|N^xXx_>Q2j}mq<M1r0ZS3`Lwsv0LV!(#hC!K1?w+Uyz2{)789E!dI#UA+SiKt<1G!J%K<Sf^o8*Qy^?4|gJ#=XHmM>w^Rx<u2Qv+G59+ng`0f}+WJS`^70v%y4H+P<Fu7;CPP9^v9n?zQC$^y@DA2`UBI?Sv54diUA&KHev7<9C5gS&C~7RVcER0<f43T7{rraWcctg5Z|ZGts&Q(;!kPa7#T1;8drg>UmCJh1yLT-zHgGyRR~_kdmYK@0JoFv<=K@tRVI=ij3cZ~YGD*sKt5`KW+ox+EaUUe?UjBWZ<ARbJPrM{eg<SeUY7cTcNFVh%dAzwl56y7BQDpZ{p}@44aUh^pgilU`w90HDYiL3rb~4}5jE2mvhfjL-|a=omLe`NYFL@dS6~^(tGl=KQ>^k&Qxpp;2ZPj+^RMTN+>auy}8JwSqhMH@q1p49NH9*LM~p$Y<E@(LxJ`C$j^;T4B!3{c!-3JjFQK5mxs?jp2lOUPFZs{d`Y6dG?ayN(B}2D81iT(rv%pR$hBl8TtP_8vwO~xB3jhHzy3#$-FQow*1+wmh`*dC3h~D?dA%Nm+m03Ww5EXCFbnB#*1?2fbPcXjK)iSy|X4nRX(!O9AN?ar-fx9J@3|~YT>S#G+xrE@#3KNyoN<f(Wv@J-pyu#MO~n|SCULbtVeepuSjR0K8-AnA$Xetfb;!q{@0&A=-sofoi1VfUU5=bneM67B*TVgYTjTE0+_Exr5KbV1E71^;^{m{+)=|QyGQz!**6)^MiE@QWWGEQbF?IQBf?wRu)BE`Dl&bV2R|xJl{obh^}srUjTJhV_}wElv(=S0>`LNg(<HwrHDJ;NYK57E(x;ph)X`f8C($p6@Zj_1n@}VGm#$w>o~|8(%QPhmTRbkYg)ab;e?Zr`(bW^G4_O3#RWV6<4{2>L!321>Raj#ZS<RY%8xUgy2LOe9`v!SjgRIxk)XsOeBI+Lyh0dF`1bfxBH)z@w{8WBaL2oj}qOHEo(^hW08^1zbCFbzklz#}H5AoJKzPA8(H&l1Z4fe3c^s!FVxye(>vRYJr-&c904PUYqfBh)z7dNh*tHkDwyguyW9!g+wA;9$DZdd}ay2-c0Magrr2XIDW@ED#HDtBLTNzb-u?o~q!?Z$rz;h*f@(_e2TZEoc@(rUQ9@m~<Ro?^&dCk(J5<UK;*HThRCFTG!&&wWj9zkHZqi@h#Fx_HZ11ZqDRJy2X}tnMoxbnAq8clW{y(^!cV7^=00F~+?ZOKPI`oKbneyyC1SW~lZCy*f8~%MiskP(90OBwui-UPlvw&wIM!04@K=BQ4riTC`ZFA?w!UVMO<08;Ng;g3U)rwvmHG02*mzHu@pPApS4i@>_4-4hHNE5)QuP2XOYmJhVJhP=FOCQmm~M1rV8NW#&K(hN@@KfQ)ji(w?dHMl=e5hil^X^3>6j`_eHc;}t3o=yQY0b|}W2Ncqy1svOcRR-zG<F_sW}!O)6A@I_335xql;2^J;PT6r(Rte(>flfSAY@l>WYm%L`68@gA>bxNWaZq0%V`yhQ=hEwt@YFN#Z26Q)KN(gsnKBR61LH8(4t|5lp+o*#=S1hI&1UlG>7>p8B0M$~_knq@0F;`##moH~%lviQYi>gML<nu!z=7UU*2Zk<8PbAJ31a`<$NQJA?V!_vjD=3^a|8q4j=>WS)Dd~7UtLIomMDQqyoVTZ94v!i`kKSl}n=13o)=9dnT9Jm<Hnq3g%8CP+?7_+r4eGuvxO>mcMy+aKbPy-eb8pr9g%*eS{iqsTr2~>#v-#6~QiU!}NAE{{%G_#ABrQifRfwwmLaUCB&+qV{sCQQHI~JRcm7^>*5NQIVjLY&XtCp}@)v}XfVvGzyXsk25SsW{3T`3Mw(c0Py&PHKQrHtxXmuWaZrdkLJMMf>^ro*C6671@ADJ!X2Ra(g03Oyt&Cw|3_W0u8GoqeKEnoc)^v|c+qk|ork++^r^+E9ABXeO#j=Ql}B+F^RV`xh?RL+97wEk-8R(&agOC|_+=?4g#%M~Mp$c}?C;#?b1VF*M3B#?c;{2sh9hH@SIgfW2EWM`RnKr7;viSzso2@Y3!YEg?yRZ=|SQLpgiRh>$B%;!PTP+7KjO$bRO)se`oZF|V~!k7qAw^0YfJb4e}}Kt<R7juFjv%10<{&8ReDOqg4P>|Uzs+(?X<6eWwlUcC<l<VsS%(}0Y?!=K*qYH6`OrmyMD_kunW<1>$D%!U!S9A<sNKPOiv_bXC8shzNd!}ac0KcOr7nfrAI%m<=<hKzEkFj!X?Jg`{R?m2m|nEPE`N!@}|a_ha~@Q-?6;(GafL6|>z2G}t$4Neev?&&JawrcEK%5Ac%rWNyM!Bln;N8E7{jHs5)&%NgSwklu?Umy`m&L<%@Ixf3Q#8`&HP{mS0hG+t&(})h@A3EA=gewyxLL3H>#F%uEtn+)$0*DARI7jdYIZ#3+o{xOp{Q%k<@nPc?tgAcTXT$x52#L0)<hP-m1}ylR7Sn)!VI(3Qmf#!NvbR8q#8SuR|628X07v#y8r9`Juiq`nzCKg-@T{orNp782DfDVW`}nJ4yUk&SeK`y7woiw5XVXf9K7P~ULj6B_;O1&f0(n%_bVE!VxVgJ~m)?N>A-lT^MpBkdXsz(G8X1`3hOH5tMYd_<Z^+t6=OfgxYO96PzH9VKAW;~=Q<;8l<dqP=OBR(j@UWDA+}t4o`@kiC!{iyNx^JBb6S@{}kSzUJo5WnqpqJ{zL0*(Q#V?w%OZ<jdE}80!B$NU-(JJ>WR6Vr&eCd1})emz^W9c!O1LkMl%V7T8DVoju3}%gF6vkcv%0!{0IgIJ)U?dmf=j2S3)6KFp^5eqQBiSF0<jrg(*H4dRcbceC4Wa*3Sef?kJ)j8QUoj4DLGTCTvY`jbsN@kpaJa}1Y)>}!2oVmQwU`4f=KhSuOi_BgS9FKM+Vr&DY+MI)4;?-3#|BLW@$si>3^>Pu-G&n-(1#b9fzwEeJ7+gA7BIhLwf_@kfhXk$uFwJpZ&Wpfe0XA~GM2GI#1Lr^JJKpHpRVHZtm`wMdt@J&m}lHXM&P1kQ4UHMmg2yzrXH=pLo?eJL2v%$yrdzB%v6%O(-^fPM#W*$b7+BC`{T)tR{};Q{-Kui<IRu;E-|EavD6_T02j>fpG8m#8<(#}zAdA_7he=h>KU+Y3N=D$8UL~KvbjtDukV$6M2zu@H7@|s`R;Xf^jjaRt7}}}KDFjyNqeNIE<2U1sN;h7SVbLqpUm^+aE$RC);tE|CzL4Gh7_)Mf!XVa*|JAoiA6nM_SnUwgEEG;*j#mCgHbqrlA|s*Ea(Z0>u4NOPmiZG*3xn18=7h5>#kV&I@W*A7C(f1VDT|p)BJPKr$?3Z=)&!sxR&9;Q<BsZ;@ZVTT+1-v5k0Dyc&He?cn`{236UFREdYI}hg$@avn~LH%8gww2s>P03^kDrCj!@Oy>@=v8N&hcpZQcvOhEbV_16*67XCuQ|3yUms`{_0E2)qchy-Q>JRtxT8|E$hL4s2;)}Ry>)e-`E#K9%gk#ct{7~F`nFSR0>mjR))x<D~V-HF^pLLXN^G3C(`#5TuJdoV_t+?qR)kI7Xb#x=jO8lV$FJ;6dMow7XG17o<$7Kww_*dwD+M2Z=ywOKqcTZwKN5JPifcSsc5;8#iHmY8rXuV*LGKd0z0cp&ltbzK-ZqXp;{u&7CD6ee=W=`RCxuJ$4eb+Q_2uR9sfW3)nEA$x{_gZ1xnCu}r#bP19X@_raVX9;KHjLGrL!DQ8~r*onu^S{1!U;n4?#rcOCT)=uK&c6k_VGqpg6NG;~9Cc83V6>9$Z^4uo8?V)HFp;rB_=l8_?@?K<Yyu&dH4%Gs^%=zmNse78pqc~#L|Cgr^{~%~mUldJPjE58&s!lmn`|7T02Ji1%suix`4dts13^eaS;9BT^Mwbf*uU_i<>;~n;BdvtM5<K9VkSj2GQUXQP_w;J<f+n|Jzqwj)&%dw8z_CWpaoGKR>wF~<}mbR<4n^><(wod;RIWV|7s>VBT?l|p_n2#nQ0MHm0?kNdj!Y-nsEI792|dmCLDkHd^rA+ls@@>evHiHF%bXfU3F{jpP}%7@dSmR<|us3;s(V3alYYNxfN0C;E`VyZl4>va)jfT@$b%q^0|`0@i9ccc&#sj@=0OYnz&i+ci*~z$Ol$|So}jWA8}uwXYyH{Ve%nmUp0~We7oT9+Zp~o`@wISD^s9dDEvY|4A|`<5FZ`1Wm$MRKP=>-K=4Uv7hBGBZQ=82Yg4lm{vIc9PFQ_t?ad+h@f3nzE74ZCeHe8*OYf72>`!#%u7KTBCXlaq4!&>CF#MpQdgAXNA^8cP7<2!ZvZv6`ARMYLLF;S`#gXUtEi9$D@q~&ej<$Q{Xks!laPf!|hm<$=;I$$Q6!zAH-0=FyOp`h<>iEFmxsufqI9ccRYb=cpdI^I!D7%miCeVFi-f3v_k>+-ARyUCiyJ6vsY238*FuAvaK)?oNfULpjUWqe2pyUurnk{pZz9J(&xdBy1(P4&Y*mH9$f!Vz$)P#tRp10jI?#2nxRM3!eur7o+S}l5XiT@=t50GVR2>jsP#*rTU7B>LYgePjg(K2bUjjkl58KostD}63JAi5RrQ?#Q}NClg|JbNYY^BD|%;nm3hS2fp`Ig29eF!{nNK49wO-*Z`0+cv(wDqJF&I7F;&&n8ai#1dC$O@}isBV(kT-}7K&lt)yxoaP4jh<!XmBhg8K=a}4YWRGwr=@hX%oU%tO=XueQI)Vgh&!vt47ZCfVuPmy0S2)*r57jbU#~9%QgX#W;nNnS@z5=D1hD!YR!wjOnV}D$Xag!QeZ(m=c7Mx_0K6;7ZKlu#*a$kinh<T#kMqL9zWojU|`QZ%lIXRb@7nGvR&LwB71u&Y~?9DD6(5rPNt8LQWSXW(;9*TLE-A>6MOcI#F^5|XCv*gFFxRt}`R`!00tR^gtU2n*jEfOIvADI`mb%&SGl`5FLCqGd>;d;nR9^80HQM7`l$$do58(n3~x8$b3zDzW*4em&u^EaNJCO$P+lWVIJx~A%>IYKV|<B_GO=$bYoT~mFL5l;1B`K}s>Z@dp3oD(BhtC&*#OgcE{){W&wRg1n@oN&QSL~tc3I?};`z;w<9X8|R~K3L4ym1q*nyskmJBbv0hqS~eNH%3ufeco!9#eZ>a-+zS}<ccNI`aU95i>LT(kHV<_cr}zV<^i$oYQ6~KLRfAlZrd@>f!9@19ay0>0bw0s5A~JkZO<%!ZFP~}b|?#9Gnf8kEcTnIEmkxiJx;{7uPLvIyjUT&1)(lt2qA48X>1V+x^XjluRBA<=4a^`*Q`BYJG)1ho=?U_)cwX)sQlalcgVE~{8X=iuj#1y1n)1p#k~_-bp9FGJ!rfppM7CB5Q($tP465m9<5&+v=_A@`K{cLK^@hX8>1j6&zs+_FhgxwVjU&JObX#Ug$x5~wlTpif!0}9f*?z++-h*!rT@VqG)p5@TS}Q|td668cT@YX$SP7V0@x2KXm34;J${VMkdogSDvsx0@GaG31K}fQBl}DGp4ql*0T5H!tFa8aqqhI0Yu0>-p#B`t5xcyAKS1$p(Snz3wFUxdjT%q{r}EO88+8ScKAL$62!>y*-7T-5zuK*(HIMz9du{vOrs|q(TVWN;4fz$f)lU1o-T7B7B@M96Sa9AC$iIJ`_b-V#&F<GGy9T&uzd=WT-S849Hm+1-mQ-DwxBtKAEz2+PhWCdz0K-0mD>+NJwnR8IAF2p7S<*3Gjc{-U;qY9n()-k*-hAFV)L*Usf*Zci(t^Mcb)F$!kx}BoE%vNosvs?*YCc3aZY;{6EDGvS9|(}Wv!FkNKUM>ZNW_{tYY25?)S+;c#rK0z=;A#LtfDZq3nMw%GJMnd*kNL9nf5^O6Mw5;jdGq}t{DqpN;Or2RailYbVxR<Dm9f#ib$U7-z3y*rRi2HYAf-^XuzwUmHgg*x4>fHOG<+eh@#tp)-We8!a|oQN6|SKn~DPfPn`(l2><N|P6N!Of9fZte_E>l1V%-;6RH+O`7^Y6m<CuVR$5B=EC;~$t~GfY|3YXH%}2zrx5_OP!ch7LfmqgbAX=G-WO1x>D?pDH6>7AZ8zv0+^R^xXH3mIk^i@z4FEuH}-C0#rnOwH7T!FWEKbhb~#7F8pK{7r{1|hIK6Z$EN&<wYNTh$0zeSz8s)=c<G4=BIKF*h)(jLi}cLisrpILDHdOws7{Um$2ON`$#821PSv5vX*6?WPXy&mR?yb*%lurC_Z{1`<>hEAlFDTc8`!UVDZN5m1W3au%-pK4#7ktV#^P<AF4AZse3_RBS~Gxzeo=7;6;0qjGjKtF_}9$dxiZTJJ;(&y?}tJMJuEgACDi6b$645<_uVl6ow5t;%z_@MWtj4;{V#sFE_I8C6*3J5t<2h!C#1A2mr#J5ISIELhBlS;j|i(<^IJG*8ff(MpLy$Asf+CW)d%)Fc3ycec)#_90IU8;Tqmk)*<TyT-#3O@k*w8%CD6qbvVr^*fkOYrVz?5=&!ED>zgSU=@bPrm9<nVfT<hLyD0vA&SyN`ldsqqFStWin`~^ZhVp6!N;K`@LbY!zM__Qo)pl#zo<d~(^^R_2G!uK4kfDNMz^A<KtA9mRyTaH{Xi?GECDI-grs!+GFEqy6&Jdb%9HxqZyUH%y>>>wf>>wupkGD5U+8S?Ujfkpk2E?ZxE9&y#eCG|cH?0krNjM(<*>0*bq8Y18x(RbXl^j44u-pd@84Dg4Xqy;ns3hx&dn7z-yTSai556YPUy1b2c=;;r8V#e$3fdL{=C?KMJID+|D9C6w8*Oj5>H(;1Un*x>vsvxbaPu!kr}Uw)Ptz5nS-=%Xc4k{DZqoV5Y2IT_gagvbtZvjmPH~8h@uu|vtAMHtxLoP6;Vmnp#^*?(|49Pcr5S}0B!mhX0?B9sRs0#sQq!I*p;Nf7%VOZrMSsSFV|j2GJFJ_jWd}c*6D4yCd$fO9I_49a|m92@WZ1BrRgF$S)zVMhd?^>PabYw{LVyR^>rY6EBIR?7zXB#e+B_FSOj;R*D8+JJjfp$zP&X;x|UQ|s=G?GYvNr|zVmU5p(BS95nK?3R#GWM23I17erMKDepf5Aj4El1Yg&|9DZND5N1%<`%Si=y<)AAT`mAx#42AP5?o_5~K>=gL;%y9~g(7L}R@_#;x-;6VQO6!vY4=9wBJnnLUPQX@=4Xy1nWO68-h2?w1Z<i8s0pZ3(PrFFG+7&aI;^gK?F`frN&sSS<5=NmLnq}c{zp^vMsb8MEQs(RGJ(1R8lfp5s<!IhklHmdq!+5~k`o#8c40vKt({d$He|ur(o`F=8`8iO#xz}%Vu4f?ffWoXDi;6~d6|E>sggJtDkat(aOizDuPuv(%tBCII>d4!p+y_!YG9a>`m&+97M$fiVI~mOAp6Wo_>XhMz!S1w3KR~5Gq~)+%Q4C3wV@AXM06Cp$<B_%Acy3e1`$E$%<@`RGT#wT2{aP(SA9^?EpnnF+RKyXYb8PHi7p(t-SfMy<0Q8nSxMT^PHjo#(SzU%S`4`-z9LG_nFB=#9&25ht1jBG&Q0^9Cg=teeQ_rgjN-Lk!YdYDp>X<7TlEMfwmi`>V{Bz{S_)P_qk7~Ma(uB+<g<oX+JE`D;B1%OXtGwT`^N|@-$UF#K-6>e3cvg&DFR8ekryq2{lX}U&gOg|v<RdBmH&PuNuQAh1i=<kVHj{EWXY#`<6u~S8>R3z`y_Jz^}<y4WtyX$uT;<<V)Z&AM<O(eJc@kW&8XfPjBi0cvJ)o?RS>^<Z({4wCOex}u(7HJErqW7(#j^BC<SpeI0pd;%*M`OF@dUw%cpK00IcPK%QXReZINwP;RFL0w{in=TesEUOb@39abc9v<O>BQyn;V_#`Jigts(l%+-&!SKJ#ZHiCObo2~;KGDk?h(G>;Om;p)1Z6uccmJX&1^lbp<fHIHm<73Kc>X<1$~LbaN17QR)y!!p;&$r6=<C@^mo<|?@ca<V8L^py_Sj}bOI0Q8>-+!<{K`BwaE@oMi2=eQVMcjF2#)Ryr;Y{g((jFC}fxMr3qahWK=It%(aVJ?`R(V7M0WiMJlM-CLU$)NCq1D&UmBSpBDA*B5gWb!Q`lS6?_YB0_rlW%=|djT>D)y#K;Ose!!B*x%O%9aRT@7qeWpaf1biNwk305$pcaTUaT09M8m*5W{F_xJ>Baneja0wkNW&`3A{4<lJ|jTSq`MaB!D$mVJ|q<<0xIY}BmFyi*+9Qg6Az>od__9*7zVFr6#80?Xl$JTZJ1n@{6sK*G0>!)N4<8$DRhs46eF}9IR!e{Y};bVgt-P>Qe#yVTft+P}J&_c1oI&{(_{<&<Jf@~!~Jef&$b|uN2<#pti=DVNKtn}#DvA3md6a8kH-;iRpMzhjVm#=F9>uE?v-&sgoL`Obfx@}<TsCYza(G8j5T;gitd?>5uni$F34Q8}#T=xa;C8Md`y1w>zJ*HSchx_!@)+3J>$WwZFAo=|a|Kc+e)=HGTwsN_!L%BWb9GKkQw202IzXs(jh6S{6dxG5a5|(cz-Y}gRY_g3L-Ew{sl0Dym5JEBNyhgO0-wv81Oct0^G@QuoZAfEc8n`L2Ir~DSGo5_==>6A(Gr`ZMyNvF0JEpd^B-vG33&$W;up0Pt5wf=^GTC5S3~X0SO!YF4E(=;p${NchOn591b*->u(EI76Dso$--I)(K=-j{d?Bb~0#*l}fS4I&c3k8kqE2CHz1=!Ugc&)c0eN6ADkK&uTv$Ck%`Gzg2ph0IvEZdIdPe5=Gyc7@zMXra1Pxh~aN88Nypr9u2sX-|=FLOelakC%ho$GQxWONL&orC-8`VuKsk&#Cc3-uS(FXt9VKzm)SvPXY|G@>Kid9`(QqW<MAS(^||C(i;+!&Jk{gPj4l5iPzLs(uj%$#>8RU$DO8fnFz+S2l%)swnKhq}gLaUXgYspFI17Z)iNmCA?Ab)Ugx5g4*t?#wpb7!MQD|l>iBme9_k)WnD|=Kz2L0g_gn69Dr|Go)F!goS6;Q-P@v}lJD*2&I*55JKR!7?HM?$D@;^1mqx7<YD)2SXVWYFwd2^yBN&Vt{Unqk2?QkSA}sD@kwSMS68u_&EPPh)w{W19VtHB}X5G6JwGDlJQ!a3f!IBr0iLE^U<^^{Zki5aXRae44ZIQTf5BycDa{_d0n9Wv-;GMaCsysl2UViRa>I3=P0o47@QJHR#Iyg$;TsH0Y%-M*cxQn30^g__IV98=p9pfJkeB@E$$-;X8-EA`>6BU^26G^sqxQa<F?AQ$X>I)+Bp*C6s;@^-na6y|ot<argr8UEUBbreRtjijhP-&!)6cO7ZukY4I9(O7d*PIiHL$()SEC5$VJQmPH3!J>=gMU(mxL<!>-@KbTX05vTjS&WhotSGm#pVvUaV{KAv5W>X21kRDv#dHDn3QU~Bh9a>GHm%`+l^7@Q$rM%YD;p;g^9pg7jx`laSeO6=SnjWE4+4vb1lEvfq=c5e3toz=g!!;Wt2sXDWDD|>r4Sac)=U&&o;@9^j-PnxkVOGufbB8#LL!$h@+d)(+>NpF*-JL$!@$L)Xe|?<x`T-$oVZVq}f94S+=*L0&ZK%OR$88!osKk<Hi{U+`X`{JpDGC{uXSGCB6#JGyrpelo@Yd^q0O^2(71=*U~5Fi1LQ7CGW83bmIW$E>$a{1{SH6qjU<(zJfP-vXNfX2@A`-ZjE`ku^Ky42zdp)F$p^$A;<wL;#~85N^&@u<S+K{K7C0PmpHAt#%2Qrui7zVs%6DqQfhbMwX7PIV|0cdOXk|+ii5M-7*6IS`jS?!lN_;EX`@6Ll0qa*M|+qIb;H>+*x-kw1Jfb*FK^tO6@9$Ov69c<>IQ`{@cys9>v{nIi6e(2gK}(%m8*L!3N^>#!Mf0MMMz5XqkI%=L3?f?D8o`nMk<;avEl%!ow5-0W>hw16^NHsf#@~t^J3l~&HpxHIcO2#w#cd%6E#?vQ8d>^q{lta&}snlFY<R{{6McqEmi*X235&e9gsulQM=HoyeRnlJYNieI5x()=?4DK7@x%Z2?*6oFLyyi_hk}1q}b}}6l?pb32xHAatWO@sv9bEGdvTTlumF-$R!Dsv@wLyy(@+Fgxj?1O3^E(I!a-31hgf38|RC}3BP7Es`aMa%*m)HQns%}!3%3oytQqo_&3o*V0eK|*7EJ;g@!ES<Tj?c+ZuZSI<FT{MAgCQFU<dBcam{~PK9n1OJg*ik4$=pHSA5E-;Jy=Rzr<As+F6P$~7DSmhu-(gFA8KY{iP2z=CDX?BTzA8TQu<d#Lk5D2D@{=BW!d=7THgDvkMA2D~#?f)(vZz#2I07mgM)hdt^aYYuzl6e|%fG{GXPVsO6WFiW$+zdB*Stmnyz1ylPaFzY^5iemV=qd4l%A1c8q$u(Dk+m+Juy2MfI3vtx$>Nsl4*jn!QiKXZDkp`S#_y~j^L{M+9P=Bkv|AOjo?MWPUe?=UX>Tgd-zb#5AwSP2}n#!1;i@qHen&U-$RSM1HEVA03FEn>&Ro*VfR|RK07hFxGyFg{u<Kk|p!5Wp_Nc5byG4PLT${WR#s*8cvXn|HwUf)U3?M%3pQ^IvRZgAq>J>u#<xoX?Sz4JWI8fAl=8UWb1TMLYKqCKw(a4C!_MlIvSpiT)iExrd+KNs&>Cm(|Wg~%*PBZ2XNkltfGh*lV?RiQ4cLVA2v;13sc#Lg`Ybn&W*!KEw9!_BxnL}MTGWuq+{uJF}+T8l6n%VE<hQZxn|uH6l%Ni8J30YTJg6ZM<tBIHQ7>}+Yl{yo3#Pwr>DqUCh?+XWQ>q^u%nn7vKK!^#SzG@DkSI9q`>Bg=gtlsit;_Xn4*j!M8NaS_V5Zrs2O@TrAM|L%{sTn!&|x%$S*a&?VZsc=W%$=*nUL-MYAr3z_1saIMSE%0khdZlkKvZG)qL`f+ItX|#e>gAa)EPAE$>|p=c8pbfb=Xx+($r4d4hbtMF+@)7a!YBdN50<pQ<?NEClV6l9<pKa!-U{!%cDJsmmV&e1ui+NhBImTo1snq)VLo$xIh*K40a3TZT*(+XSSjEioFh^3GC>=ixq52NqnkBcTJ~uAl$8&X-;WEI3i_7}>+=a0!oTuPu|-C_QAJJ#sD=(rO^2qVL(`lFw~;xL#!a>W+cfiL07aw*O|5Vj*RUvn7E4HH3s~=F0d4jgi)Pn{>lTN9Jzu)=yJ{{uG+ehDIWb(Z;E@u37%}>h1j|!A<3kIf@SGM8tU#(*Yrv!7?t%pFIbn40UGnH$cyXk_r&(m5W`X?@rUAE1!ydOVuEPAr*G0*7IEiE2jIPWeEU`H>;Oq3ECC{N`wsP;Pi5&cROG5J(-zR4R&pMWDNrg<E)KBaFfE}@3p39baCmMfQP%ypQk|aT5?V?>|dOD5LBU8v4Ci4;}T$gHbvwZRo2ZW%9mN^j4>nzEur1_J(7?^uHCjk3B0|~<&U~zc{`HIoTT|>W@h!O-n02P%+6OwlMksqYA>%pwiF<M_M^vaCyk5w>Uv5W(@cGY^fY)4Z8m<aH9wx7CMy#8<AJs83$d+zCp)k{z#Tfs)g+%cR4L#S?sVsk)FuMUPd6Hz;3{L<)d+9?wjpE7%g_R+bcJqd;=6PEujIFg4k7=l$>%u|E`BG;uhSq4eiuwUefCizt}<+>0IVcm7xlo)7Zkr0BAVS}~B4ozbWl-x|?^s#<C67tDmn!`ViD%fvTX$3zg4;$DN4f55H=v!itrw6VY!a>}*t><v1sA{ql7YZJ?TenBp(bu<l$tds?=P5fvO{CsHXxmaj&pc(UXaclK5xB7ou)Q;}ZCWMBhqN~g(N>n#0SM|&8_Y{W3l=?hD8lh+kGXflZ`*s^|84{Z5@YyAOkW$K_G=}Lfl{e?+juqG;!3f8GCR?A0`MR&M0Y#UX<PY3{B<j78!;D%`Wn)8U_BeG$p-)#H#@%IXmuQ$9YD&C$kMpUzAAb^-x8x=%2I(B9H=|Sj1$0xER4J(XcCzlauLh<%~Nn7u0<MRo^*r&GPd-6T65@fWB2fg8A0L6dn%`Ri|zve8aHI7Vw)|zsz_Yh8d>Q&2x{vz>F1&KD&V^DK0v&Vm)`9Nd1297+Q4?SlF)pj4Ha7|)w4plyxF*o4q&Ux^YcbN2pviK-j!6#)Bp7D^Ij}K0Xp}Aa%xFGj$qQLTPuaA<GFROC7!|7J;8yHL46D#VCx=bI8+CDxb$gC9EK}k0kg?)|7ZZ<7#85Il%r*>8XYm%TP;}!QcE}%N6xKB4&fL95X_!y=@cvo<T!!??3H0s?mu5*MKpkHEJ<_`3eX}e4ZCS=XaKCn^4G)JbkSiA*jUY_uDT)F=;*SC&qNru_}%wfhk^WIVFiaG=9y4HN&z1u3+;$XKMquB5E@w@J4;hgFeDa5udK&j*&36<tvl$Ofj{h2IZPl@?x@19crO{sm<B_-iPaz6c4H@HwyXoPJ(7Ks>BSnQJl0`Pduu|j&{$zfyouW(SZUARic(Eye4O5kLRr*>hL}gyWI&AuO8r`b{P8S!oQ19I)_?Oozp9ykBL0A9$Rl30_okD8UL1h<Hzhj6_Q-98j*r6>z#5<pI`(BoF!Hx68jD1>><^s<MV<0}r(~&gT(lZphU{}3lMO9q-S(@Gz4+(%^<NtfHjn9_sfIVMeKkjLa(N_(6LjKvZA{3M<~xP@MQ+jUp$uWep4%97GW10+xWl@X=ZqE0rIOJ}5((iDDCtI?M%KR%o&|k9nUB4}T+Jm_l?OSD+E!|{B;+<xAV5fgh9*g4tc|C?F`j-j`N*c$IWbKkgWb}yaH_j)u>MIpNabV@dqBM}#l?b#2nw6}U_pdl1Pfr2wQ5@LP4Pm^unJ>J)tLn&sL{@MSsRpwt3{q1w-amr3R2=&01hi$IVU!LtzHwyxepEqjHVV~o=+B&eEWYiRe^tyHPq0PwsExo<>R}3d}+^*{qd!RUt0L3g<n3twD7xp^dIJ<e}|u^=X{$!%5A^z$4_KJymZu0*tY4zT`T>5Zd?EC-^NEjKI^x?uR5)NzmNU{eN0z>^o-ZL*~j@^>ErmVd&b9uZFki+G66?bf=~RdlpsFd8OuifoD=%<e@)Xf6x~S*h}izV@EFWW9MAkSu8eBVENK)cpfzM1lF>`<Y50NXl|Y)WN!P=wjS!81(Mv=Z6}=XQUy)W*H6SK7#b5~|o?%o79g96Z6R~^+2q~+iS7;n(+xi$n*%``5SN@J*E)h_<<G;Zkd^(|ts4`y4AdwT3^1&4kKaM}QY>dwD&tLKA>VAHcv*#KwT5bmIFAgm`#)L=lq|<}@*`@tsw;@@i;4B+Q87YpD#IM@UsQ|3J5p5j&b>-(KYGZqXo0{?9iQ+*s>b2_T^(>)COH5C6Wi#@kW^}n~UN6jYy7CC)MySp|(dEB>_R;R&=oX6*oVI&6f4TG5cl<V=d`E`C92-`!P%%9=BKs{YLrkMGk4S}}i+=<ER`xj49{cNy2PE<sVc5#H{^C@P?QyPbgp)nP!LQgvvycA#$LZ(ehQGY$kzcv$^hv8YZToV7<d)7fg?{1=?(?cgc>JyoH!6Se{79&k!^T%o_Ap&M|H;Xnk1gQh!PB|J_dXqVdE@jSvi`G=ZfwccI>Wd<9W!<wcd+3~J5R4{zU`--=ikopPS)99c$-H}@kp~=-#DimwtSqlVKp@-()&kE>Sj&t{6WhcwNe~eviwZr`&dl8{5=Td|6|a24KDqF>C4<6-<q<P0x=At^nM_jSLGU#2|%!DgBqzpWp9-SPfA`<DZ!Cy^4D%1845|@*Sh_t`m*xie;}TF+Y@R;Y=E*sEmh(254ZO$nd1-FdBX0D>|8UOgvnyzrY3@;dhq^c52QOFx4rnQkrkC7WfQBL8>B?N8wpNL(>HG~YvLiY5z~-NF(AA1Kq&6=-hCl15J-#|1v`Kgf2Del5(Z4!8)wkFjq?McSNV?CN9ZfDkPvRy7@g+4D*Q3@Rqf*P2xUj~6$-;Y9Q2B4gLoEtm7AYx9QkhAf-pdmwmAp7%6CPi@@hE;U8!!BLVN=na0sSet11BU41wqJnYb%=g1hoJt}v~*kB__hr`{FyYq&MH0x&BjV-Yw;>-B(GvjD|UNZ(<StyUiaNyz#Li{gg0i$_>q$yNuqma^DbgqYtvD1cN}!s0F#gbFK=U-hcP30*5zT2ewprdFAcea#-RFv5TWXlG&OdMyGU|AiIu7k9NhBTTiyp(h6F+*R)3zqd^GEgSW*Og5zlSn&(3vF=<ZJ9o8Otg=%YJCM!?nQXH6tjLOq7IKfKu?eyCEUb*icXF7?CgHbdS<#fqCfQRyx$@90;StRdPbNe#4>Q?IQxK4nLrZW7lG*i1GFyDUX7%#6S0F>}M*M?tX0j~E>Fc6!4oYTYHf~4+N)IoPM?L`88w<yM1dqXLMq-&?bz?l1s4?ZJka+M#9!oh2r-DqMEW;gt_a(#qlHq>IUA=sK>A)`?_@#wk(%UcT?U(fSOM3eyz5SBjeo1e?q_=;n(%a(!M;Y#;^tQ7McS&!@lHPW_Z<9#GkE4-!HkRy+;*Iepq3)UI4vJ4R8@Xf=pC60RB*$2?n`3%Xyp!G2N$xQ-I;MM75qOkD^znT5m&w;^p4+yVikE5vNo3<ep7P-8r}r~E^CP)!yU;9Oj--Bf@l^9CedICE=1r%3w#oZ3g4$VY`>q}<HOBV8l+wPK&+cXq5)P8t^GvqYhRm|^PbcHY9Ja6KccMGDbhU0N9^~VXpQWx&bM}E8ej~U+No!mvSqHEh%y68#K7B{m!V8=`$Xk!RI()MfF18Xgj*v<@Y)fF5H0q@^_Ly25v$^gl5$G*j=Fg;8{Xy3DG;iHLmbbRIbD9ixS7gLzN#6n)IoLl><yP~j3$x6q?ey%}=X04)W~`r;qCVa5k0h;KS+>faa<I4A=8BB<{I7q0x_aJQyg$gZs#T{ftUs5xj?>?>IoeCTah|<CkFI#)fJfiy6@T9`U47wh-E0uqZAaU7dZEo@Icz^0zo(7n-L(E5Z1~GxSyd=M9t7`y<r*P`G#5f(c{m7%sf7^cS_r$t{Mwr3sU;2Dk?97R*bb>QrPv;%f3USm+PUmOqU-@k-pOUK0{00sYc&}7xot!|xjC04`05j7fm@_!*WPbhad?(_es8HX7&WXl)!^DLjF`6D%1$8(djxH@H?@QD--*satm+L2S=&GJY(<H~hJ3E5#BfGb;-p;<btQ_V3Mn9#5TQ^@4<NN-0@Ir`rqqDb;PZ`jDr8<lClC%&u*PP&t~D6iyMeq>H#YWy>GQeFL`1sUTHV%XoZn6oOTKhDX-|ZDvPyF!JWqZixM70|>y5|L`G5EWyr1}VFCWzKSNHP8g<g)*@HHsqa(m|<->oScK#uR5hTI$0rw==H?YB3sdp${ZY=%d>@6I*<KLc+LAp'
_V92_P_INDEX = [(0, 26605), (26605, 15040), (41645, 22990), (64635, 36721), (101356, 36281), (137637, 12829), (150466, 26238), (176704, 10292), (186996, 19739), (206735, 15046), (221781, 26590), (248371, 28213), (276584, 21919), (298503, 41209), (339712, 19737), (359449, 23053), (382502, 20522), (403024, 13501), (416525, 18878), (435403, 18758), (454161, 18368), (472529, 25446), (497975, 32298), (530273, 29948), (560221, 32645), (592866, 19782), (612648, 17984), (630632, 25681), (656313, 14764), (671077, 30722), (701799, 30156), (731955, 16659), (748614, 19330), (767944, 18680), (786624, 16214), (802838, 13566), (816404, 16655), (833059, 23478), (856537, 13967), (870504, 26005), (896509, 21450), (917959, 23906), (941865, 15989), (957854, 15367), (973221, 29159), (1002380, 21317), (1023697, 22890), (1046587, 27901), (1074488, 14247), (1088735, 18250), (1106985, 19322), (1126307, 35182), (1161489, 26422), (1187911, 23595), (1211506, 18452), (1229958, 12505), (1242463, 32464), (1274927, 14962), (1289889, 22436), (1312325, 14245), (1326570, 24161), (1350731, 21887), (1372618, 13603), (1386221, 25499)]
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
