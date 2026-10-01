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



_V92_P_BLOB = 'c-ri}TaPT;mL4>3G2@a^Sy@?GmwoATPM<#AecZ?0HkOTe*e^W7A3#V*_6x=!+L(*5)v_%>SeB77GCsZ_gyaVc`vqADfiV(qSh58?frNx)gg{Ljgh2v+0OR|<F(V_hvTD^@YwxvM?OMB(J2NseV#d6TIWFJ$#!tepg+Cu_j3vkPlQ4fBhc8Nv<uR5y;!RDZ<}lWfLz!!+4{_LqI)<D=zO~mplssJL62mx!8bgluZ5mQeF>d;hJ3A-VkcyodQ?<V?j4{`JswvHhKa6$-`=PzJ6JknfvOC6@Lmq~ZLK=o-zaMglG1>uZOD!SWUyqB}ukcqwiuh_*LK)If)2>TbG4vr?ONSD=5vSSJ?KU-AV?qtlespCGEU8TP7sik#Tp?|C)*;EB2F(lB5?pz(({6Lsk^6K=_9jn*eUV~GU)ssm9rl|L5B7c+?ED)X3^DLo?!p}M;V*iBTW|crGyR>=i(@_QZ@a>ccQAU?x~Imx!E-$A_-%*tt*5QwCEDY9$6Fsy?D$C?KgOYkVy(+O7_AGf|2ZHL|7<9%=aQXKFai}Lko3T{hOXL?WY1BoTlw7fTf0Kl5OtySIDnzBC(1q=c#vX^=b+gSZDca8x#fV=lEwkUWZjl~w82_kIUVfa-4yG9hq8%fEwoE@7!A9WT{mW%L;>St*TL6Usmu0?6Ds=5nu_)$&a!-kt2_oY95;-qi^<w+%K%dw7q>@<xkDQ;GZW`SWOvyU{J%boTmJB?rz434bFz36TGtm2X&36XH8Yov3u({y8e4nA;jKG7(xBP4jBvuFw?VcOwmlD)xQ!fSt^|y8)Eu?Rh;FlGQin86cyz2T_JJ?FYg=8BW1iG)=pJ0s<^qOsvWXqF6fs1zz3DL>tce2`WN8c1o+zPVm`62gQUv=-=V(UEL%J&X$~xK3+~v^Y;+PjBmLisl-MjeIuqN6Sq79n8zY4x$2d%@xbL@P++V$-sHOJAe%o%ZKx3k7y#Ua~M==%1?o)zErxDR{Aj$pyq5>4p$g2zE8WzI4*4?V(Pq0jM?DcT^~SPWS0XvVhS`gToQ6E;#2t1WDUO$tnzZ}4}N3s_Iq&(`Jv%kG-DPI$$L*ag0c`I`ihVK*6O^x+Nfi#Z;!8tlzCA$}9mH+FI;-+Y@NdDFiV{!;9I66yv|X``Jw3{=|LtBJ~pIlBqP9+}e|GkDI{SKXNN%qd*s$RUNKvSo9ZyROt?ZMUJtTIV!Fx0|T8E11YFCOWsN_>oANW4|q!)FwJ^FqbL!^oq%7gSF2YYh(lAZ$rVMES2Bd1u^v2dsr4Yh%PMrxrzGB3)(~ZHKTrbuLf^<HpPBIdongh2@z}O4r5Z-3_EU9Z?E?6OuX{}Q_fSyM#4!qTdNY9iQf*^D$QbyxizA6_+ex}*cRED=uP@<Iz+V)E7H!!9k-ND1@qko2Xk0W;<|>U>e;pk@r6~!D?~~zJmwYK!}ZOs=9T}w@E2nD+e5XfHifO7vW1kg!LO7c_Vnor_lHQDA)fLsb4frnP@-jY(sijFu2<E^H_KRILE32(dWhX-qL5?7D<m#Lw($xhkSHa)q*YP&Z7@wBWhxOS)3J&3%8;-c*e%D+ZVge5ez6Y0gH~?Jo8&*i_+S_(d!imU;_y-^qLKKC?TqO*Q&5;ZV6!=o*yW{Qcmfs)A16_qQlw&<%$x-qNJ2cE?H)EGph(P_6Uy3>yS+^Xj1umiD0_Jq6J6FMv^Urf?exM{QPT;W%hs?8iJv%AOnRhi>jaZpHeaJ2u=@?)m2Tg;C2<@e>zj%(aDTHSyUc~e@n5SO9TqvXw8DL-?MiG;z_+F>K=x6L+xC>u_1u`Knb}_oecQ|nwj>ONHGj4vHkoG$Mr`JVyEOM8N@eL`)&{OTyXPQ%gja)7Sb6t~TXdAkgLYf40ehTWw0cutsFH9GV&iQT@tD*jOq@_jxuT{>p>20V$0xk0R60uEwjPWO^dm`%jvEk~lr#akv0!|18MOzcsbJNiIT$c#Rkj53amO(ciM^xamQ*O7>_Ot-@(8zpIEKWrM%c<LcnpXcn{-g(@Cazt{%qe_Hk}dcL%Z7zdo`_gocuX<9Oz&Ft54hOn7;o`O$sZ-HRCzdE1$DAmyZ)RxWLNPq2@)0;yHQIp=y?@x9zygaJun`&(?aPK%E#Ylws^t%uq^0s-amk7Y2cwFgq%&G+{WroUnF$YpM{ov846kb2hsbvl+0ntY$0D+))$BO=+^lwBw@b<8i`5<eN$jr72G|i>!TD(vKsh4tJHp*$Vxb54f3aAID6ba0DxC;_SAo_Uu3`70%YOnyrP8)A3`GqQv`bMvj7QM;+$!U8Qm~U@mQH@?kO^?TK<UAC)6(JUZ9ZP3)33Ln9>iH_5F+yPK(9`1aE(NBvJ<En!#U)ztk1&E*J*88bK2t!a?7dR-xcR<NZ`VS9U`K25te**v8Vjcv$GqC~6Ljkv8%YR*IsQH2PW0?KW12lYvphj=$rW#9&#Oorg2)O3t|&az3V2jjIXP{AX`mi@bm+R)SW968{)0S5<0Tu<#eH%p2$5%Z<vzFGLZctlF=s2@`PVvLKMU^BG0WW8}?Pcua7ow*#6=_9eY25$?(_SAWxHUtq5)d#lW0b=XG6-f)q9uum9wbKN&>515->^i@GB51yfP=hWGU<!~LYp;imp>=j`_S$-9grLFpQD7fQX<E$jxUICsVG#Rnn2&xCyCrr&7cLYxHuVceitY*7<vHJT`=cuaS`~Hyj!w-QTbSM$Sg3$h6d)0xJC+<|n!|3Rj<DgDP01zY3v;QL#7r)0Y<BF5l;g#RlBj@Tn%IM6_oQI%aD&z0W0x!xShN&)_a+t#H=QVFO@y}EFIF3k0m;xiS@5PoO>C~jK{MI#e2@p$19pcnK`T#EGa=EaftvPgOXQXlB+@Q}#%yO^$;fSThkEeI{zwZH0(!FN(*9_22NTNW4$PZRyEFcpY3I|PvgZ47c(~x2n@!NzWciV)V3DS9EDw}BSLkh<yk>yRJ;xmOIF}szIJQ5iRGG7Bf+`nJzr_g~Ob47;TunHhFk?tJ6&+U7lZy|uk1Kx*)ed_lw}v!dM_q7$iNs$WOe)DC5qJ?(09~4#{pDtYVVc|6!=(kC(YDiS%lEN;Ym&t_>;YfFe8+K97;R?36~Ij`*L&<-@JAgWAnO15tqF)H4jn2Z5EJlRox1Go+YR(G{I*uKeRwJ<E~z0B;#I<ewhrV)p$D%t-yJl97{i&oK=;U*b|NpRXrlj;Ya-BDsSETF&n_T}1jJD~V9X(lZDG?EZ?0C1XQcHraqSJ-BeHw{C=1>t9h#D24YnDvf%(A+1Do0&gSv^FQ<xj*!;ZTT^(<>Pwi`TlAB)c{=t20qlFtBF*eC9=Hj(Y;Xm+}VI8Ss*VFqPM4T_{&`Vw4K>C$ba3$@5$Y$792Rl)qCK8<F4LX|pq|IbG`Co3oNdpRf5iD$BYfM+tD`Xuw~9FoI{H!{7>8(H4vjqKZAK)vgNH*yY3{NNqlNInH!ks03W?vgh$N^{^FxIpA<euYo6Uh+w@&(W38xi?24KBo8bOmYX*Z++VSCh$!DsTY;+^H^1Wpe&Q}{X}c4JB6G=ov<rmFsZMZoXQ=o=>iYXaq=b{tP~Xtmc%`LThw}X=sBE5eFsw&8Z6h%U~|)iMUwQ9!nK{<=rb*5#+jH<b%wmIn2FepuiE^w(I}ndDK4G|7tr>rjx(YR5UHlS+X9-Yf(<a=(#G!C!wY5iovAOv7Ydi7^;e*>n1?&lo)yWW8ifnN-KlK=BAp>ESO`0)qjr5nwI=G{1&W)sYKH0&@}GI#;5;#lp6b&SE{Z62lq`{w#a1o6wu@NFJ}e!Uj`bft)TE`wfxU`y+|Un2yPSIm)-^i>QUiX|;QPy9k{<`9Rt&oA0L2>0MWLARpd#*FsC0H++w6MGh1}C!LqTAo;;Pcehj<sXGrI_)TCm+9%c^>vI|cN41QOvSI9csEL*MQgIKxAwJ1#=(R(;saSkk!#9!G2FE>qZX)6pJug^Mv526vcE+x+`pt5*IJRT7(0)G5u(vR~VH&-Y<Mufg1uQ^FLfk&|-JEWfAT;VzP7Ypp({NA4Hcf$u!th~VB8&lwe;N|TFyJ0HD%Bh~QUwS$d>p3RdxcUTNOlNuy-z6V?Z+TH<&AbxcPxKHR9qW7GUKv>VFK8yvi%AAYMpd|{Ee)Uy7bYqrE9_9J7;k0@Dh&56>%;Rp3eaDZOSf=7Z3+2byRd_4u6~XlCMw>kFR`%$KU=7LKwXi}mJj*uiY)RThI=TaTc5~fgi|Y!0yYKwlX+R9ZPQZ<9a$sY$kFZNe-a1Zj+4tOv5tP9>!LBghAS}|uz~bh{eYIR6=+oN+?=b0k9UQOpr1l*)93D@7pLz!6tt%1V$8xaMoA>`_AKXKV*g+_AP_{Q`$KO7F*vGg2{H{N~_3&E{|JL~U))jA^{CPg6Z|7tBfS=d*`L=#1&HmVrpJJHO+bsP=9b3P>8`ZateV^Z!7eBt&Z~wvR*c3nNWBQgp)>nTd%uLZL|F~||z>mwf@jX7CypOMXU+8p7jGOVzYhFXCFC4u1?enkc@+-k_p}|IYoUcMv=#9Qz-t$j!w)Qcd|1lyH7i6{H1wol>A*q89o?}u_H_x5No)R5di0yPS4|IeAmqS=j)E}Y<Q5c`7(62{ua(mB|14M_GzvO?yo*e&5J5J{{-i$F%@#LKL=V7Mw%(o1dFBc4HeKH-l^_k!1cI79nCBpOwdd<X43bUoK6gz~`2w+HJzVsIaW_L{JS;G(>il-0d57HVF)(z{=JLIfY?WRQbu7)ftitt<uV{74QKQDmaC;;qPJD>YFoObW=*2x1E2q`I2ZP)A>8Ra5{gZAVP3tv6JH^7~>gODeA0p}i%u#ps=T2QCozUKAmHT`vX$FHLI+mjRG>awR#w7fyfN8bhf0pt0@UbyK8KjYaC%X?h;;?u2P<1${W*W(4BKHYGBM1TI1)e#*`X*rVC*L-?TEXU*V^qkn5`n2)sQu~*uxb$s$VPu!lf9I7?PUxTQ)#t9WK7Mw>dhD<?B!bFmr=?3>y*lFU%zjV}*6NOJjVoH2j<5VXi6j1A1gT1#e;n!~+~1|d;SM0I8~F6$)<^U!Gv57xWR&}vdLQFqrBBNepAU)QKyH|aP>EaKE9c=M`NsAT?n8PAdG`o`-9MuF69Z6(hai+kd|0;Me1A{S2i22_aXiS;9*%oE{5{)piLb)(A(zMe13U7NipMP4x67Z<lf<VcB4ECL2-;nNpe+dcMq=K7cp%!wTKLz)UyJiED{R8QTSmF=F_q`2*C0&`G1ge-RK9n^n1}*+g$+3f<ikj%UcW%(rydx1-7D0`*DlP2lh^C^6GAz5Rp%h0YUa%@hHIMT!+v#IauA8>33ZHHK+c5-<XE*=Ts-Mu+A*8U|Bb#?wd5xT>aIPi$JlGBElF^oy7T=|9@z<xOB+mUIlCrWrOnnmO40s9DBrvFpA6KlZd(@>KAj!;d7Ii}snc@thSVUg;rdqSVt-Y`c6yWi;}0H*Zm@&9RYwV&9)*9#2|rta4Z*^SN}OqEUMl_NI*b{(((=#PYMD!{%W65qp~E_{VaJ%4QhSbM$-^z+oA-}##@s^sqmnoPt$Ijt8-9jBcIpQC`+K3v($AFu49*ndoPS_5@|w`F)Np4HTFd;({x-zTvom>$br!$fOVVNtb$%uE$1%$TVyPR!6u1j2VEMI@jQAJ%1CM34<48HF`G>qOvJ{b~!Dh^WhV)Qbd1RM&w^?WmX0qk}U;fb8A=dr~EJXx3`x>xM#14np<=mH~Xl6GusyF6+$I$eU`jY3&h+x6D2pkTkta19<ujbe#h3*)rvwkZKI(9s>GFF%Jtb<eRYhic~a0JA|6B1&D+nPH+*f9~NuM8*-rn%=0E@E;L@$&-69ixnC2{a-)h##VPI5;C<nfe*mpG;Emt1jC?q~P=w0OSr&5q3B~5IdCjf7xbacOB~wIG=(42jIX2cJ44KXC#F|5SoE9cRAg1T{B-zk`<X>L+m$%0v0CKOu!`$McXzLvLbV`G<^ZoXIhaG&?J&6Q@N87YXNL;24ZBUzD|7eq{$&QbdQV;WCszHY-g6vHGBAOk}#Oc1(PgCB9#4Ps?1hXB2(fu?LiQ8Wu6V?L&u+QxoK22eq{QpQl2^+e0-~~V6Tk;mrn$u%*3$`v(Rh+8)agwqJVmY6y-5HLXf$5Ca%kdIW9R9QG$!}BJ92D7s1baqS%L^1RALzTlK?044*Q!3Q>G8+t8l$HyuV|>*woN1MF{~L1tfLn$8ztY6AgkKxhFPBP7ZAT*AlRv1qVf(-{yg&l`uJ5n!n#^*n8eBuNc<#=M`t$BlZy&aiPIrK3;Be2%)L9u@4IgQsz1<O1+gO6H&}hcsmt9YJ8bmSV)LI$VG`gK+_n(KPQpeS~5#Hr$xCa3oIpI>?~^Du!*thb6~{(L^nd&#hZcF<>2QSfvk5z?=-Hu&@=D>)XbJ{Zru&Ao;J1xqKh#X_!D?*+)XJ9;1?c%g@<lvOnbonR=GLz7-S%_^s_7PcAJ<*&b-0i(?(_NZB)Ga5yj{NUPlr+I%`Bg3y_9nlR?udrvf<Xq``oTs&0~N9@*i5l_F&*%V04J3Dj7Gbbi4U|8;OYkM=_1N@QDNF^^q2ooCvVK_bF{SInso^K&O<^xauyPrDCA(L?+QAoco%ONq#p`K<rjH@h%%tiP##i7I9kC0_3V1!IrA3Vxp2oCVHpDV3lK`rM~)Uu2O`VO&#aI!KR?8==3myd)3Cut3rQOor-r=gtXGzdLw`|@ziK~Kc7EeQ?%X+p!GgoYa?-mJ12gwM`buGZePgofd{ga!~9U{`864Go=q^{Mfje=&ByWO@&!$prF^I0if!P>K*QdF0&O5G8y-qtYH~3)WAMZTZ@EdK@jak~TtV$e7omDlHd@w6TP?GQBUEDU2-h!d(ES-OO)+ehSEOCPYwao0OGY_LyndL<$W&r9JU3HZmKgYps&bk^H@9`ze;0BWyMyrYhl^Sj@wgX}r*W(TtwwkYB{q7XLWYq_tV8E5N%YsQXn^7Vs#0(b0oQWTY0OlvFmO=O6Myk-!JtBq~3edd(<Nn5Y$dGIjaY6J>vh!;WTe)AZ*;kx>b9d@T15*unv$WW$F8`}-dA@4mTX%LCKVO8$j?V0t8g$2elU=N0|L)TMssfsaz8u*<@Q&S}f*N4MApJO36FdOE81&CX?#tgYPN26I>sRQ3mul<=$gh%Czd1MQZ;;o(L8Fz8HQ=ijl%Hyb6S+p?kwh`%9!DR!Be>l3pRL<Ws=hH$|w&>-){S-$^QkLv&T;9w|s*nemvQ$baaGO#dy8Eg;6&5*5Q5*T)R_XB_{?~u-uh8^W+4-5YKMj7)lFHOimb8nn?g|nBLbugSgy&h?kHcI=!f!n>^j@dff0cru1w=4AMhPe|FkW+bODd#~_l5Uu8S2lbWBGw->vyI4d0|k4)n^~}Adp{~C9+$29?Z~O=lne0Xw3K@;)W+?A;~U()2f~vgK<8XXq)K|qA0$QkuYHT##PoCT(h})rI7t^i+u2CfV0)TWZ&wsKcYr$X;uf%8CB2`}>0H(oi8=<Aji<MyHK9=%s4I5JI>??4jKmh(@sO_Ic`-`cqsd30<<OFVd+uP1x|o<<GA`*h+#AvGj;RibMi=*uQTr0LZW+iWJAFZ922ICQk(?U$M#Poj6`~o$Tm?lFl&-+A1^}mSbdRJC%1iF2@bcP2bw>i2+3jEuv3nhcs7L7Jud^|twrLOh)md_a$DhE1L~MJ^XZx7#s~tLX;A;4YJ<UTB0K5N7=gtrNdqyNK-oiU5X7JtRJ;B|4dXtKF!k5aVI7q>##OO@Cz|MtZ<0k#c<_W_wHZ(tsNL}Nu7zTfubjP8A3CbkUA4d_MgoxyA;DEa%aw7^`&+~TCs?<BI1S<4jh4P?e+-rB2x}j?)-{vpb@e&7dufUE8i2NuYBNKumVcs3%t?@QRdC+hIuKx>%903uBWVRjgXKuBU8P)q^?@c(itlOuAV=Idegk#u*Pua%YsJlQoCh8+)7jXk^oMW8UY4D^XW$TM@Ok8B19+2eo&U+rOr<`L&`7~w8-SG4PdT&WM#=jBH5>S@a2`1%0kJXfO^FX#3YM;hyS40b#$KYG2Y$S7f&X~s{bCnkIu?+J#<ikIG+?T$fUHFynNRRa6nn0VoGMk{g<Bnun>d!##p+_O~!hDFs7CZX2t*fiBq5l;r`?t&xKz1IJ(D#9<7C@kH?3wm*E8=yQ5uG5nD{`vr9Q-Ov1(}&qkb&m6hc*qs)RrwX!Bb~OW$1bS$ShUsu5D(A<<Ob%?2!*ZGt7>sZY0Xz<V=rbm%a~U$FFKaVh{*nVC#&x5L{a<Gq5kzl0;vGM4TF@|LQ|>{TFt;=aO2UxFQl)PVAO+xv*p$b<a5@u95Rm8cfW|QdT~Ra>kU>+!C6mx`iJ4bgO9zama~9PTZPoBCU8)l=?0I#Lz8_C`jWd6!S~sCOQ<REOwIWyb_$*;=W;;VNA-`gokQi%H~AnRvU;3jX2p7fF;xQ=`Q)cVOQZ+jJbaI9O228XJl5chtJ7#@>S$)s=xC5RC3}!gx?l>9J}MKlbj5fNKWd_lWB!~A<Qi0HRZl#d55@#40a?+Wm>GT8cxsCrdvGEG>&;28r6wMSTyf?UMH{eGLsVJm0pD$yCZF5$IywWw_=v^jvN+}Re74`LRugjXK)>#$(q=9aB6>n3&mrx1K&0L0a}=)uLREyj-0uDVCN)fBaw4bD<%n{(q6Mnx4_IKbc|>T{U--c+0=|?XC}FhsY&GaruSK|q)$(=SLBkr!z#UfX*`fGXeTa+KJSIG;KlpYey(oB7J>J*hhgcCg5_KNF;$0pHMqs(F{sA`P}rfz9MH~#sWOH=q$<~UJY@{x%_29!%_m$>;1v6hJsR+RpZN72946(O`HNH~W^6TOKZm)8A4LgwyI{Mr9N1Jxhn(GZX7elD@Rd>Zse^A3>H&Q-KE;@mC0PhnmUi?k*ZV-p%QN8uZ~l0P1{HKkFH%jYe=sgeLjj>J)%}Btn(mf}gby;5;LLU0A<-9puS70A+qi2L$w_o9Q^m4Kq?8i=4GK7|r@~9|zPx*ulQ?PVn@K$HQm#yCRRfyUHRq$rT?VaPDo2SdojY+$VSQk>25B^Kt)@Y<Ih&GN3B|*rM0|j%3cQ2h8OR9mnes&&7lDFi!XjW2<OzlAMkE#_uAvB`BaN<GtbxCAVNxK5O^<HpcDNKDDkh}^@oVW?xF|xo;RJ!3hlcLpQv*R1@B>oe*91v)u59SkX%VAI_L1lr`etWwrp%mE@HUm>G?{eSUK0ePJ$P6Jj=O~LpMogP1L$E|{?;b14fM=`ayCZl>=jv!+*A}_>HGw0PC+S|$uR~Qn1^_TPl|nGW~L`p`b<#Ro^wBn%nc2=cDBEmme&p=Y}XT;T<W=JIFpR?$$;hX=)cIKa_Ebv>XNX*_Kyh1LGn~kY(kuVrHF5fjEZ*m5ehD5Gf{;l`TML3R`)ev5wM3#5>Ac3{V!jw++CtRelO+jQquDCp{7(8=7aZD>o9?w=iq`)cTRH96uJ{`18Q?cJRoMCkiY4&Hb<V3GgYo{LH9+KE60EnJRO@xRIuoAyCW^ZE0nmHKf50H_rnM2ah~e_dL^zIwS{44XVZ}4_RdKJeT{4|tEn_lQ%e^$HSCsn%`0V1IG4CdWZ#yq2ZkP7)ZJP^8=k0UGyqn5ncd}CU2J%wi;=H}%oie%!oMS@#^790j#%4pJ~GzH^)1Y2o6&{gI>j&rM4-Nv+{X{n)TU$+S{xgIXk1h+=~;}ECQjQ8gnrYoZoSPHChwU(RoyLSiunZ{YW{f7)%$Btf9_i&Y*4Piwb(S4uZ~lAt6Y5|Pu4;(k^rwdCAoYti15`dH@FpTL+9cTt{HBLi}-U;KZM{2ZcO=5ha&Hc3rBcZEA82I%HKeDgbP6i9RXkIJg|2)KxiKM8{jgfM>}CnOi3EQmNF;Qv{1Dm(mqhX930LCp?TNnQ-D(M5d$I@kx!Y9V4}hmcC(rq+9FT*8-D5Cwj_5hjDZp%x@JyZb8<Z|iO%;j237lVv?zD9D6=Squ}01;%A+}1pEoDFtJsE)a;g!RN>1g=a*BcA;9POB!Bk{mD(1_@L$S4Rm+4J+W@fsLN&T26jMzHbUYXOm^J7?y)=EL<D2>Gnvd~(_<X*c5x^<x=1}?b_b({|SB+6r#ZgFK@W=Xf`qP8rU@)qc6*W`>#?aB%Uar>T<=sMlr^oZ~hJ9NCP8ng5%{|cG4i8w2ZD2(FIim733*|!XoCB&DzK8@Vd%aQ@oaK}ChM6(VKd^(1$({n;o^Fv{Jr|H)AaO(Y^)9w?BPHX@8Z@dd((cl&Rimi5nBBN}Dg=d+nLR)!epLQUTKLRWG)g}S|RjHSG9S1W@x1vyiycq3Q89~A<<}9jaxD+vbnV763)P_m73a=uUI1EA#P9g#V@yp)C#RRUlZAX#kW1dD*=S`JZnI0D$ddv~CPew{c6Ta|6Q($+zU6E;25$owkpqM~|r6?Olj1<PQRc}l!6+ts%ZJ4CDz9EW!O>8!HH31e7(v++I4}HpUNUs@(DddYIFs=GN1D95mG*j5|W^|9}%cPE{GX=UnA#~p5qxZM%arSEcZ5mD4u#bBOcG>w8=y$!3uVb?)Z^Gam%#rurRoALt)v0;-!@sF}6dSvsdx`cOF?L{w$0R!<f^yzQ?J4YI;;p=!RgZ*th~8&;+G=0v>1FWwof4)jb-_#!^Mok&n7qFSO=vQymn&2L(6ysxb4O$jqdeMJ2kURFja-**{yO}-ZbtkBVy=F{jy^E9*p&m|YCvc|@^w$I7W%G7lm_fV*o39Lg>oIrK>W)tV9ty<qJ3!Sm_C5`vpqKYXb=twnLehBk?zwbkMJ%d6#R)4W_!9;I%ruWxI(9fnUfiQi@_bE#d$vgYQ-*&tucr{7SPWcCPq53-FB+b6P<-tCO{;2b#^#AnA>}tR!~F(3mm9mN+6i_%Gs)+=hj(962<Ee^<KoppF|l?n$gHyK;P5I2#H`g=(p&*A*UbQra3w9dZtQQcEUR1oRL|O@FgIY&TeWH!dEf<?7O+j`*5m0ZyCi~5i2%`eqN#Mma0Q0HqHybK$|v!(qk69U=Vf#T?gYz=|bm#_^g3096WaBWEkX;Vv(N~0Hu;c{c7sejHU1o#$T#bY3GdZD)TamY#r{vqyM4lQ9&&G0}C@9mGMTbI39fwD!SsQ4V$RaQAsG+Ri&3%x<P5VsY4u|DezJjGDU>b-A%De4!Q%&{>D4)Sqfnm%qX+_E7X~v(OCh1?tk-M<oe&jgiTEBJ)N!G>fUq0E*xziGht`ZfQB4DYQm=Mb%_+@`IrgYEu5i+^<e1C6s~HSww;5?=zf3w%thA3(ZRM`Ax42{;N<OBlea!oAA<RBV!p;h9p`V)-s|$%2#1?ZkmKQ%7O79M*LlTW@~g&pLrqYSH_uR{A=*DNM91e1(K5SVQ)ZETX5Fg($U3yS6Jl_&Mc0OCc5BMP$DDUvGpIE6dY^g@HFwXM!ffzToq5h!=YS$Iw+I~aTv{2dOtW*-d}at_ED%cKr3eAyw#ZpOd#aIYyRmKrGcG)HFvzMsUZJH;$ClEXSvSCmLC*r2$pe`ltX+y~VMF$?sM43hv0z3#IzyHyW<EwSn<Xj8D&%ie6jSqL(nJ=Mt$Yws+{_njNUyQw7|EonNT;l}9NEDGncGinPyUhbt_b7QdrhtnEyBn^CdKR1B8=UIB8)*RU^gEDQDZB@n8yYo>6Rjls|t)21g5Iqw%Z}y_T>tUcS{Av%~KE*x7zZg{Nm5XpEBJ}ns?X0PA1;>xPCo$IRV(!<^&Ui?Z|A(cVw+2W?~?%(mDlsvFQpy;h`}hXx>Yf(UvRCi$h3qEP`BmoCF$*8_Y$OHLQI!L2~rG>lLn&{_aKw%qTrOCMAMy8&9y1f}Rht)Z<V&BB<1@uu~E@h5wMPs=R&$V4Bt<=ZjD|_VG~(n1nWR!=#rhh8AK-juBM@c=18c&SW@Qp@VoQU>5L)`sY9c7$I_BiM#^+92^+t&&9tQ#4@4RhTX_5M!(e6i=N46vQu@(#_VaHE5rw1X_hRIhlR-moD#V;mGwydeLQ)MC$BykRtf1@#W0q~JVGk+dB!>*3QB2D;8Mlt^-<lPyz~9__~*UU-mt*f(l#j)yH#TvxFdU#OZ3E8$L2^P>w;;ORv&%FP7S?M-FJv<K1OwW{_&rDYTE)SQ{1*a5J<a|T<fJF;Q8up>>Uhfa*a3YOScOhQ=lu0-NidcM&ihQWZDPK{teTiQ`-0Gh9w?m(%97K`B!j6WjjA<xg$~lIf&2zjn=rqtfbvn1xSOIMSkccOb5BPBV$mpv~=&CE~vla1r7QU6$}c|pTJ@f(q?U7>?4+u=({lv$sM~`{74**hin&&{eaNBjR11y$v#xJQ4~hD>yN@vC)|C|9*S5#lH|R51AxlBSMn1wwS@BP;a#%NkrD8>K?0&D!b<#+VuwJ#Qb(q^BtZ<64H1QCuxBhqUghixEAtg&(;Y}ejuld~JIP`6i;%pCgPq|byT}#%Gec?_{l0%IVa0!&W%)}MkV<{0;0!Nr?V4EDNCIfrav-JN5TZ*b`9^+e4D-*^R{+FpALpHX?66_HkVb0${8m&W<;63P*?*A2rf*9VQb7(Y7dmQKDyoDDjm){1JXjm!={4s*9xHixf`*@#meY6vtP6T}cik~wuxeq9?NXE`YQQm0u^ep5Y%YCEb{X36A$S#q&WUOR-9ivL60ADDL;(urf}%xw(h^VqsYCs=)U@jOpM^iSny?ShUoTHsm9MbH(dYgPsK%J2U7lwYYAexmtU0`e{-`9*A9|_DUQffe5_vrqWN8hGC6~0l78Y;8EvnK|s=oJeTPYInQP**7BJ*}pQ*_3x%NUR}_KjJeLZD*}WcsX_G8)sP_0OKF7Rn&e6d6*-*pQueBkvgyg&t^3OwFx9<qDifCCZ@SGZME(jirNTJZWQMO-!WR^(<PbRmmLtlp3j5k(-stZe>;2ivctwW@_s|Ua@`xnsvAey3%-@3T(*))E4p`l6D+bxH#GLh00_gAIpUPU{q0+nT+tnMpZ|Fhs8zd<^jpY|MuOwH)a&Re5ZRO$9DiUF1a@dTf6#Le_Shc65_{rILHyQ)S3854~MDm!;Yczk9EdjHXVzb^zhWLlVH;-3HJ8os$N$|m)s_N?s}JhBm9LpOF2@K`W+L@ybcfi{qtgnj0JI%gX(`q?ds(UW_u=`Pevjpd>%~=0ow&8ODiBUZ()e3uqsA!53Ofxm8hUxj5Mzx7!Y<DST(TIY{DF2V(CWp;|Z6bG@JF?sTF@DM}f`yy}XWdnriUyAxpnY2PGOJO3ExsHX{J=Omy-kWyZ0q6WzF5H#!*P_(Pme><+J~ptgVO^Gh37Rt4wM_;B14pv{>U5uugpJ->4D&4C+!JyIV&<vQekOAi!SND>)V{4YY~R7#d;F<8li)?wEk$NHj^;=yfWaLojHTK%uQY^!o-!yK79!V{>bv4{{=HXDtN%vi?Dqw92$0*fa@P}QDgdU1u7#mazKfy~d3Cfi$q5;t&!Xw9xKoEB%xgGig2;|bD)H9xBay?)iyG}*Q}r$r^{lmID17#oV%1f4TUwk^ib>xg=7FpVhZJtVA`rDO@PV+&!SIEhEIZs>KRw$aPF3~t^w1y-mERrSF-*zsiOq?$0@33xwIvZ$)F11_XYdA4xFS-1sv_U5R~H8LWOeL1Rls++DTM{Fqz>8K<wRxo)Yjs|Rdv#6q6V%*Es$aXv*k#%d7U0UNr{DOH%%fWo*x+j-lpMRjnXH!@BhK@z3jd`(QS4!xj?XK>4=}iO949&1@CaTme)HzJe3g+DCV*5G6?Y;Xq6*z64ff!eoyP!Qps>+H_e&v7U*TP?f?Y8;tEqM;%TCB6Z%-AckmR`BH4lFsqL`Zyde?JhtiV{k>7n2vo&U8=}={z4$#JSa3!?*KZb%4?jIVlsX`lMUn+^3*&Id}*$5JB0y%`B;t?hD=%4zB_|Uans2cw)w=RQ5ww-9J{|-KFn0b&NTrEU$(F!yqP0syLL=^#OMw4OZG7SP?3t-n1Hqt>S?P0We5o1`UvHS2OQ<y(Bs)PAgi1kpi&`3qT$A-S0ag>KkZGV@EtH{g81TH%A+%FUtKxoJr<5A9DFB{Ky{V0MWAN01x**aep_r_s0kPYDfCLUlBO{j69D}iTg{(e^E&GBR?NcWAf{x4sO!V@|tC#>%$N2G@82iZl#jgAjT)8eRm;VHA<-6gLN$k1#S8s9x^k45)v(}>;8}LR`DI+DSJur1!oEJqFdHtuJLtI=+VoIeMC^t^Tt#~?ZdTROslYXO~2i^9@U3)4Y+d+_!!r7EBQ4+=~m&-tgG!R2XgcZp6G$w7vj?B_G4Uc{_Jt-f9^d>+g9>jJtB2$U|Pop<XCyWRY3AWQCp0|7T*p}D%#pqWEtgEA=_=*^#H3RQgA&ow+Wb`$u-V_Xqg(^Urzq8wB3c$iZ;fk5w2_2)@#77Ce^aFFK@8{30iJKZ4!5iZ8bLyNX*R~(M6T2Wd*b=#A$*(BNW*i;h7j<`|HSa>SO)Iz;zhvo}Sh0G<TV<xjj?h<_%&WVAa@@Ooc=yom4~Sr=ia?nFe}(9FD1OX@j(m-Ye>g6p0IU)}|Cy)paUCIZV)~C(I`}B`Z{aJR<cmY)uZ`(iSS+1$$5jM!xt32}vf9NT#p79DH(>hY2rKpCPK4Dr8DB9K9M7XZ$I2FExL?wPt42v}I_<!Bg6t=K@q-OXff(q^x++bk!D}lIrs*dkB|Obxrn0oVP?tBDWkZ>q)bUvcsZ_7-1HOfwlTBO{uqqS1pHQntxKJ+%@+@;x&~x2ft{E$WO#WG5>4>DTXClkNHgC@%f`R9frl{{w2+Xo%`JPK+czKDu<!$7=g0J)R`txB@XPW!OM1KezfHP-}=_nogr;#EM{_O4aE!o*-{xE(D&u&iN@;|zNcu0y3}=hGc(%lwrP$1oR+i{96=C({`AbNp`;|BRjP-IQQ{KO+!`T)U6n>`5V8MM=%dG(M4gIKt0*IxzG_%nC4wlkhsJ~>0d2)lOk@j#X%;)G7|DUz(t`pcW*A;d=U_TY5t&pWBCikK@4rBrR4*_lk(j7Fz*aBwJ<C$xL+jj={#P`@2O4kR-z%6-QdR6_=@&>vWzYUYCUiyBxU{j~fiuKI6->(fQ2{PaK`>_lgr_lmEwE%cl2_7?smP>fI3H<N$r>mUibP9mmR<~3I2M?#pC1jF12nBudBE*9)E$0!kKI(~*krNgK_xf;;L#>Gl$bALp8m{h1^;6lz9#5nSon7sbCOAX?_w4`Qm`nxTQD6lOpRn+GBzc-DYl5Z;4~8%gp%@C9o8f#B7)r+VSi?{Tm=GL8ZTr;?xy{ABuC)nNFD6%cG;;kT3r~uu?jL8oK9kA3wdNbov|h`wt|p0Z3p;vD{*wT*fz9tv?})2400uXMMAlvYeH6olLDZq0&MRV31)7@RZ_R|G!Xsls1t1I^#<0CdeSxLHw(ow?V{irne60$K-;EtpQCN6&<iV1`@Qc=f@22{k8ov8_ea4tkOAjvt!N(!zx>U3v<ewz)}#apky~(cY|&n)wZyNm0H$nqOW6~qu1u5yN*Zx;{pis-{;uQ@U`=?;by3yqu{dX$+k2#1gJt^xy2Tf^Lq1^B#eHv~JN+DL%je-S|KvchNX(o6_7gFLjO%LJucHTHDnPlUTz|LpAT5nIGo;rYb4tb4=xL>10)$F*_k<^8B*~MMt0lRV$?GYW#TkH$^yId7eK{y}5xgV?yl#yI9KqZZ=8#SH*?;#O*VJ#Sq|^9e<RRsnHpeUTPL=A_fI}(-!W3;Uq>($s&r?hFN=`SmGWnKiNT>VQ*nMI4GZ{^Le`#^a(UE#bgx!`{BgzOgqofnWQJJNEp9AY^1J=b8VBIkv)rl|GDX9a|9%X^oktHFE*GlXe3%t&$MXaAU?p2g2c!C`%+yj-NN=o>2C2U=i9jHE31#T>kah;w@4qw+h9G<3RQCfYgl+-NNDtj|=J5x%k=Ji0kXGykN{)(qut%D@v^LeV>!ua6{W^2+9PXA31$Z7brVUy`MK6R+?DfGSovrxOw<MhbkqoMcoc;vXC@V+H?N4XH~`?h=?yOq@L^Ern3MMnq3^z~<t_Wc*{p(HF^mCq>&+nDpSOcQp_wu*@u%G^sVm0QwyC(@s5l$d9IWU0)~QrR_9b0}6lOgb=b5hXHo)D1FJ+a6lMGc1+Y&MrYV6OvOFRSHR0n5Rs9^*|2XFH``elxJ=+w7?f4^Yz>zt2(1h*zSGSOw8+nnazzpq=)E!^=~MzzmWu`?7LkN9s%*uT~5vaq`tBL&<Sk5M@#-H)D28f5ZJ_4c!N1%brVo&<KQ(82I9Cg9qN^ormArO56?AS7s;LLUabHn-6>f}Zv?iXR?cA8DYMYQh}zvMf4*H<ji_)R$b7^^QcuK7bn;B%7)s6iEpTD-Z|BB~RGjS!vSU)o6`nKcalrpa=1?B&L{3ziD@K1Q?b$qd%ZvMP<1wn#4Bu6KIDxFXpl=|>vPb^nz#0uC$l*AXnjAieR)r32>2sx13ExsU0;V~H-Vvn;H`kuH16&X!uc?)7E5Qpum`OWKq&-qJ;h%RIVR!lEX8_<ANkz7~k+o|(YkS!Zj2gJ&#uGfaX+2$)Cy&yh2k|J$7yRdiG;d21aUrjDZ<oC$B&m2MI~=)Mx!*ev$sx{bUu}-iZ$C08!C%q(kiI0)4=H@~6q<;+W0cM2hF~I-?LN1VAa{?1B;ABfJV~jv-`=o@hYi9pdG(+DWW89|y$GG+q$B(Dj!Z0KLf(WSiIjB!nI-F_yrM6yk$d78?B`d#z#?#`3|HvFeZ16px9P63^Gr<ir}?OoX~Sts>JP&g@s;>cAw%;iHlAcl0*B6{pys945;v(hqR=af6rplR4vU4zl*EKIGQm522q#*4(@r%mQf(lBNNvR9W5B%=w~`wUH#4k9Q&YU@WAn#vMTbBFEixfPyZ_!1Fwi3POWfaI2|`+q&>Wh&;Ed#QRETf;c#gX)9Dg8`WjUfd<zrmIADtOOKc3SOM&6FYrZ_@M*S}i-Jg*?1Ot?8>JR=FvR|!igKEYtF0H+YlwKe#NU_FA@7Z}3@kg0Z=1>YLoBu~y1wfdnr<%E;34J?s-_e~34VnG@ZB)Otaq;qTm5+tEH1UrqX4M$oHif1kmUgYF*Who(tN%)xB*kw9|Tg8(uILk&npC0jeyJciUKKx^^_HrVJ2PM89pcD-UVA`j>mzpK>H*phUS}$==DAmN;Z795<iem71;pBtKsJoVi#-EQ1aCNV6OB66*en?-?i$9b8IO4u`(2I@1DSk@|xW_o(^N86nU&Q%9Ui^RmL;PM(*n?cw+yoRniC~p7C4V!B&xw^4RClOCHvmX=Bttp0v_!8a#4Svht@<8E#^}jsf=ECJ%_?03Ct7T|=8<7TY{aBZ8-O&84Z{p>NT5y`k&~n2E;^ke`f_sT`U1YmO;Sj^D6VzjLB_$AlcBWsv=k2KODHWqNp*#+->Qq`4l`*`J;)u%W(Vj6+)?cW#;^;0D^#oDwMKXjgh9DEC^jBS3r?tEeK=<#lHpg&D;(|R6tr{Wx;!zi`xlMtdXZJ=6i17yQ14_pyPPBJC1OQQSes>CR*oe)H}ULUc@amO&s<7J<9c|PaXqZz1T?Pe%DA4mt~SkTmcV?$zCIxJDa9+Okmv!*REN)|CA+m5)RfZs+?rNZ85UnIa)!cNdg3wS$zaG@(<omwtLafLgIm_!(JSg^QvURo^&fkcjI}dwG6O=nzs;ci#<1kgJ`?XxtKf=E=fE50`Idvp*;>hFT8PmS$cm_0=w0);5Vhi~t@4tb2A?*7Dp-u^fck+b46|birRIKxL&$oq8`J$JQr6&{YdhzF<2AM_RJ_H{*~bGchn-z?#$C2Ss9#FbkjI;}?QzHb7|HSg^)j=Z^?>qHh>dOhYMGKZmmM@R&z}-Zn(iM|=)}c?xVJ==a?<^O_84rYLcQ>pB=VP-aXQgNJ<wvc+uJyF6mvxw&@H<mi$TEJTtF*^7$0TLJ-24Fc{g<9DNjeydZrF+$S<!#2jF96_HL!$xNxad1sn=8FYXI1L~_TM8&(G7rix}yT=RU;ZGuwY6TtzFkXvAPQG*ResmDV)Zc^Hn>|0pbD47UB0Dy!L5%>wkGQ%&0jJ(A&p|MuP(kX2x5nS65i(K&dR2Q?yp_NhPm4^mLpdkMN4s9s1m9^XRhJC1LPsc7I%ZnnIaG`h9od0#Ce^I-xzf8c$FEk({2~%ro*{_p|j^=q=W~u#55hy(k^iHk?$QzVZ{E}k-CS)(}=jmtF{eFlZ&P;nVV+lht030_QlAflxl^hwPXI%vmAhYa}j%SAZwLjB#a!$CyKxmP>iU+^qHai@SoPct=vKj|a6*e`#knew|TD;_A3YfWtMN$wcIjB3Gff;wXCX<l%TmHNb1jy;z5rNru0xp7{;S9>8Urx>Y4!Q8_@8!dO-)%Ol=Hcm1`;<N=y^B8P`JL8NDunL#6?k#8WfhI*JlQFH^k&;fTFT$bW}D5#CZR3Nl*$nM<t>+%SwF<#!e&bcX;n(Wai`raJ8cP@{uT5w-Eoio>|sar^Y`LUnQKeK+2-4AM5)-RV~iK`1zk8(xrMOE!It*#8DQ5jLk$H*I)a5!T{*?;9((RU-mR+)|0Ifza6{C-ZA;<jmkpfRz%n8V5j<rVhfS#}Ma@ui>@Y+UhQAx}FQpfXKtKJ%J-NvhbBqGK!Mw;Q1S00^^bOPmJV?)3j3PiLFv&hq$b#6(Y2?Z9xDkI!V4JQ+Ak5UK89hYSJH|q0;?-c745)c#EBG6)Oigw&rW8*_iKwjK*kcaLV1@&}#6u>7K}r(4J)=!ql;;%g4rPyfnQKbG<9z=iZCX{0nzZ;BuK$KS9M=)0cR}XSHR=ZTB;(A;SgvfsBqtpWvFIN3BAY^)K^0lEWnlOop5#=%nc$|G71_)bP6htb-$mc6JMZZsqd`el(nOweyFv|L9jk+duBE%Oh9mA|kMQFJ5DCNeo`K1jXS(IZtv`3Rl9HF4VlGvLGrWlBBdA`(H>j%zkli<pS>g(nX+#nfxhTC%Pg`56VEP@bus<FCU@kw*>5<s_9U>OC`OZV|k4y11g5c&Y1x<~0V)UM3yRf=(^;mt#2X51LyhD7zEkl)PKw(68EW#)p;k0D-c3R32+knVTaL>KxMxK_5HHWeFLqlzK`(oTMv6Snoknznr_{-pRi6isOzHFk39-hFmf687-Kc<QaDB;F=XAUZ)SCK1#dR}t7%@U@bFV*uwS@aMRx2U>eR8m?R$K3o^EKaC0p*^oNP<xtKPl3?aD8;vjSWBue*YVX(-Y;aXxqQc4c4AQPoyPGiIJDlqYc~_Qe1M6(p@aIPcWwCADDE$YppP4O^gJ`7eqY?XBhpyn23VuqHtuz*DWg!Aw`@h5S%>44?u`{qHp46S>%!{89&LWYnDtq<?El**?3NbGYpNS4e}0*>*QCK*&DoZg1RZ+u<_xD3_E=imPUw-Ry~3;|$E+=8@d<K`$xJKoS`v@#LSD~~Cmq*m;q8cRni9?@tXK*L)<vnEQbcfHO;}Y%U}Xr-j{fp&-4P?CykS-;_M(idDhUKhv;<p+LBtcl#8sQ8f`cNyMPzfITYUR8G1~P<pYhLxyI+J#%ra5AW8$VAD(o(`6}}Qt)(J!XDN7bz?3KZ<IkhT}M}912^?r`&{P%)A;S$)}z9@w~y!UMiVkJH8P6hGDIVu%Xc&)E;cahSNftF=ne~7QLds_YDR0NBt<u&Hh)~gqa6Q3g3!9UUs>Vox6o`lg~bXQi|`wiDNE)_zecjNYHZBQ>T^P3K`iBA6iKD!{^a<;yoAXXGBtY$9thw?6oEd1I$JeA0tl1HkFbBXM!?>udOe&(vICb@{6jPs&UmhS$tP^RprMBc#Pw?V1rGr26G>>~b^a=D6?@l-BP1egv@E-UNcedThYT;5!g%b#U-<EFpy>Gk5LaLn{BIA(p3Saz)x=MPYdUqLVX9<unnwC0Cu#1p+)617buj%!zz^L^s4FBer~@-=w1@yl4uO+MF-^D}(1G5=<QWBzN;l1hEKhPZ%IqxQM~8h%EbS+i{}*N#pBhK2EoNLcSaf-owJu>uT(C_!6yrhzu1CtQBvi4veiF=*uK-vMV1#*eW-Cx+@&?To}wUmOU*;(W_)!i6Hn4^;OH>Snvk_kWOTW%Dowc!N!%!wmZ24j%ZpKsmU@qvF~CUx4Zon_R?=M*9iedL2RKY*ip3R%S66gp|L;qK?)HQ)=gMkFTCQmsIWnzMK)FfS#4qeR6~P31!pgx29hiaHawKg6t@yrWQ~rcbA>v!v{p3QI!0|6aF3sb#2k+r!3S7&bD_TxD|+`)AJ^?uFNt0fMMB<J4{m(8R<LL<I3Opq!YI1rlvWYK)yC$Fu)yBvzOypX6}WOg2)SA&D`9kZDM9|ecj~M%mt43$>fE8_c}k2?^%~-Zr_R=A(18L%V8Wl8LC`Y8lltEX{!p7XEPVXz2}p6{GiEu&D74GyC-sR+vGj?J|*4llHzu1icBXg>Z$LY>j|~Ue=YpgIR8W8ahuD8`I2v`mp>BFzb9D1#^F8-iV7SUP@tMY5&7$hflhnFEJdyMy^cJ>v5m0oE#^+wa^FQ|UJjY5tGOme`av>Y5h%3573OPnU1=6;<YliW0{jMG5yVP+VByC^y;g7mk<K7GzGv1~b-*=reb%DiFfYmt344FX9}=I`tCD1ZyBl+=3(0ptPs6gUX5L4KEO=2*9^VQVtI9eKbVz$Td%f}%Ve%i8v$+j*b15BT!g4*+Q1dDyBQhr*u@SDHWv!OyGB>Z-$d@xW$%q=yGB=T$!D=koGdFWS$<9bEJ3}SRb`&K~YP&c1TGtZvQwsvIY7DTqSxNuU3zp<fK}zD(ioA>GfHtF;kC~;u&fFx)HPuQd<ycC+SJo3`9l*kJBOjKwDF%wqscZf(m+5xzPO;P@ang5W#}?#t$8qahrnETJItNduX<_%KN?I6ADV}s|>*|*<WR2~MxRc6p>llk07gnN1em(eUfF0);mUM}(D0~u<XCUI6O}A8lPMb<j?F2FrU1!bZo1zST7M&5!J9;V3m`=&aihd=;qcFiSEu}ZTn4O5&Si2y!P<(L$)<GO^#etoxE3e)-Td&tbOGoPP6+`bD#C)VD)AcDtgnVdiPDcjd^~bEts<VqPjdv!v)?NN)MHC#{t^L78jjG1yRcp(Ue{IMrmEFkB8kt=#Yo55{GpeI9i$V|o!N;;uR#ePhvr*<X8znSH&RpumTiZe>&m1+W3ZhpPUCmB>RvIm(sL$)*2waK3ZYweuo=*^o3QG?g282-`tFc;cxOW6`G19)XpI-%5^oIXs2IiM_>k<*t$r<3YU4bB;=sJ-So#~lm0#NC51A+&Ej*~M!FO-u^wHTQun?ig_8wu&j9g1X^l^2hlU!-S<9D!X@hm@AZD^f{MeP%6@LEP-hU}owS3u2{hBGcrbeDA6f*4a0w+guc1=aHSDKCLiO+nHWu0_*&=$b{U9E_=tF1O#P7Ug}J++_~h)vDAbkxvGq*C#5E8(>VK?EN?CAXjY;v?|1aA4DKmKlB)_%j3=bEbt{hvv~J}<>>NmsamG08z4%1Ax5x1xj;hbR;Vfo~jV;&1&ZB{?1O@6(?1d`$+n>RjSX^gM42l|Gv?gQ(M|cfRtcfa~qSyJ*P<s+BoVYU14T@Kr!ov%uFt@NP5rTH_vL>GMp`BP0D>qtXY?*+T_cSP+z<6y9>*DaKcW!^ZRFFx8TAr4Q6@GJCkSRA)!rpHF$cr=UeG1wu`K<bCPm)4I8hEmG>h{7?kHzcB#2bVk!Rd8rox>I0oh)*$@B#H>kIOrP)=7JP9Y})3bQfEjTHy!=5cYXo-Xj_|VQmvHJkf(T_=3ON#TkG!B7F*>u3HX;HD(WWnKf$g+rFGH<|{5{yYfws`a-sh$3GJOTAY8G`PYY79vqJ5IGtR+cf(L5=3nuo7i-0rEa-4(JnGj3nbt5Dly1a1H^GU17#30T2GC}}W5;{0GpJ|VxOFwS!M~d;cK6VNipm)lGZ9&y2F!`_sNx#dJ-3{)gz89&9zyxvt(%nvJfoQCzhldvlh_qki^u#Kpzbz^^pB)2$}}st9J61#bNnpCqaC?jcuk3rZ+HCut?25Mm%>5Qn=7<@)KC7zdt?0X1vbmKpxuJl*-}p093*x=iz07(<0;bQniuYebN+_J8UZPrjFQ2OzzMh9r^6AIUt9Gm>+gHAblN!W>1Qtz-QL--JRc!3a1k4Psp322L8A?OM)^b^yip}^B9(uFyjiFtwk%Bg?U198)p=g;IOV>hFamTbJ%T9?$9JgqmF(ghx5iDOVZK7<^U|CiX#UK-Dulq#Gc{J8F9L`LWAaJ^-I-<cZy`N>jP>U^`^_*OO=Beab!2HI0{{2)2G^Mzls&<%1Hwn3$cVP;IQB#66kzL-q+SQ5`iE|Cf&j=NmRPC8gcrG3=#nT~XD%778P`w<M|psBePwQ$7})^KR!Jg|51<wFx>Y+ISI*AhTOSLt^w2`SRPy%>r1v!)BgplgLvdO()J#RL?||r&a!5?&+80pqnaml4OHZ!!78q@!REt3O4q+mfSSO%bcCUIt0+gVajqto7<fR^gm{4hI*)cLj&L1a4q|2q%rnb|6>2;gHbIy$$qEcq8#Ot9s&#{Fv*jA_lv6Qq5iB0lgj1iqGby(g22!1w`nZ8+RsY$*I`N?C?G(3{?F*k#GpsX=wSEF8+K>h*2e?%@Q(Jl-uB$lPr0b9&Xok%l;T&q27x+|)WO@|Y}Nt_zAizZt;gLLpP9)vfgtHFLnz_!$UiLVWdo5e|<Hd02|wlFpieDR`BAi@7n`rz8D7u;nV+nclFZy!JGV>-U3x1RaPZhY&L@9yJU55G;|-vS@sy5hpe^zD31AMo?~KHt{wq}d<)@e|31w~6{4eSD&K)o<@c^{r#y=eOm>kMH%{-{RWB>5=qtAJez=vA+5vFc4n#-9N5dHH4B@-^Ta&c=A5J>V07%9(lL*=2N|<%dcKZ_4GBV*y~cq?c~oL?-%R4HOzv5DGI;QpBk@~-v9_6oPls%=ec;jE<z;}J46}5EL0)bZI_QUSUI=4tMVKO8p^`ODj?cClM4&6Ag26fPykVX>EzEVV5y+(>_-x5jpcRX34D<4$qyZrvpy2Ne$@KN`J1%5-HK)L_!H#;sMKBb`n~?u@al(JE+}}u3WTdLYVp^oY0x*kbX-NriAil-qpJ>Iz4tzktCs76H7rke>|4EQt#x+I)5fp5jtgh?2)PyfWz32Y16B=(^X!VNI66K4N%Q>g_$<qxH(>d;b=rDB^*HM$t;cbBG_R?4`Lxx?=nv(S({G)G0Mo(JNa9Lm8^P^a1rPA!iWVZc6P4<qzs&bKNAD2~ZO74!+}2Jy9^oq~*v=2W<Mr}ShL?WQ`u54UxqX{k%a5;#BYt+!U(cT9?4x(ZGmW|2lGP92aYAZaNp8a7_=e@$*1vk%@_6B)j`w}~yhCgA>Y)CXUoA(DEj%9N5D&+5VhLyS=i<lZ3McJM&$sg(C!|*F*-txr^YZJ-HHY(WQ@d=s*th9&gO{)TG1V=d5Ef6m^kP4s9y~U6J*JeIp)on0zN!j*ShhACKM5iI{&&Zz8&7LF<!S9N^0b;zx@MgG4$y|L#f!Rz_19cS2ShVUK~&nBHI6l5YE%MS>^wFNO6$t>M#m;}amOROS*)z!5u1AEo^6p=U}u&MLI`%klw%$8v;|ER(Wk&!l<Rbjf-P82)1J|DqPh2+GG$7KiOtLQ2;3q2psjNFC%@%BBe(4|g}Nc7?RLdyTUjL7*%hsyi2wCYN+`QFwCFwK{~(X`9wG#(!;v|I`fS*Q$?h_yk%aJgjz`>g%hKqHfltI=?hsiX#Pxd>NHCoUc4r}B@?o5C)qdL(=w_Kc#C~-r<i2Sg;7Y3`-nfwa;>bLR+!ynvp3EEdN}Sr%Nl2~86QgA8m}vcB9ize%J8&g4hSvH<*k!0m9bn5M`xvem8b&|Gd!Iez^_&zed@_Ol=yx@Nj%YAGM_YQSExqAn>4{}p842NJ=?#PkC9f7IP^VxGs4g_D`_fZJ#a}+m3J`jc=bk{JtIS6t6M*8g8wN?Weg`5_L_ob`m~b<tyGh(4xWY7~0sQD0aq8=I*D;j1550;x6Gn<PdxHSyfkoa1LWGuHpVaF=4*#?F`;G?2S7H8&$jE2X*XMW|o9!54ub0BJWD|7isWr-LBrj|yAW5#BR}DHr>L^KMI%2x&K)EB_cccF%)=R|_5j9s9MkSLkfji9W9+K0n5X&SIH1WkIVjdR8b>-38rF&JMNe)QwSS}#79A76#6||8d^V)fd7F0o01wzMNu*e*TlhQSn2AmhJBsMG&3xyxkf5{g`#Gf7M6IP~>Y+#^mQTYh222_$LRC-i=x);SG;1&=96Mz7>=NV2xwRyX60j2IV#4DhB`Rv7o{_Xb$0N;{Hix5AXl@9$Sz_6mSE!KFiZ!@awky|q;DGpGbsbPJwLLGgBHMM6QHnM7V%;kptHu3~Owor>6XWk}OAO;tZ1BplCD^Q+~_5QG!uu%;|>NY^|*}p4m(wIbA*Aq1lhAo~3j$XlPD=IOgzR(C|*eh$R1ic{WEUt|-$r|KWPzq%xG`9@IERU^_v?^C}E(7RSz#J$bR3uxGs#`?j=(}=E>Qr5$I0^l$y2}h9{^X2{Z9e5<n+bf~thm^|Xk2V_<6^URZ)m%1Qrvtf7h6}t(1(#+Y}UX#z_^JD>o~lG-uxn2hKb-k(y{%x(XpKnKsP$JM}lkY<F90KZUzC&zZN4~qEG`?^<`4FIIl_Bx=0y!<Yg-hFPo5wqGluDIuf528#`NM8L~mxm8a}%S=8C@CTNRJ(B|r-ING`uM_XBOw3Sv6OB`*Wy(G~=Vf}7o(o%d?<;02dK6sK2J3M_urncFc+EhLeOl=kFYV1?_1~o0x^(j+Ze1@s*7fErzs#jj?qITtXJ;&EZJK-*St?+lTww+V9m2=8Az~Cz0;J%kx+w!NSZ2Pk>W{<s!_PiM_VZmuHnEK3`^Ips+i)Ds_a<OE(bG%i56{RPYAj(;<<kK(dV&dRr`CYFpx?t+<(AYA@N`u?l@!3l{VLqmoB33=4qg#k$22fO^`t4E>&D8hmWeh5-w?Zp|8bK&E_kAj)!pzA-76|n{(rHv?%7FIHntBCtzn;`=cBU<_v>_%d`<9AAGrKG*ksDD_Uy)6@bDtOpmH*VMFr+s?TMyI`Aed|c)jZ#Yni~sq2O8V{nz>v%(+)^}X_K-tnT=U_T?Z8EXq(z(N66%o;5nXI<h8PlMOSg=z$19vsD}m-Uk7L+!ElK%|HL1%3^BH<ii}H0d6Z*B$=Y67wxxJ=Mjr18l^j@x1f2dIQocHXuI<VwH&S^`mhQ5rfEeshl@#ZL41t#_-cB^W2d_qe8pz{46OvGHHQ9zi<aWVAwM+HLdI1{%+XI-lO&0V6<POwWJ|K%lWj>%y|NrzkF6m4zX;qrual`;Domj!Rk9DWAx!jmC`HV%*FbHy9;seQQSkVKD$p*b$+H%54H&GTtW%^<POERd?_bnc#Z6)?3Yu*OcG%nm<C|ARl)q^28M||~&yh~=pVz=ieRH%<|ub(Bjq<!{Sb)zYe6+JhrgaF&BVwh4fa?kNsS{)QprcZD~nKD&js`Z$IgfDiinN0cxs>0N}wRa4p2E$e4Z&pl0sdShi(ed&s>KGNZaKayC*3eiL2To?z9jhXtA3BAA7$qnw44IW25Ibfhp(kPKx@KSK6j!n3%uO2gdX+4J;s*{9Xb94n{{DxsC`tBKT2I}jsuLHhtrlmO6xLNgtj?d*<nW3@sl-#dh>3D_MPygbi0qzlCUwFG4<d6omb^@jHmN?PO`?BZ%t<sdng8?*$;?foO-j$xCe4k@?wzzrqPM?evTwN}XA&E;rn8%a2Vxf1<ag30$zO0ro3s-rKtUmoUfK5(_pQ*Flg@0bi=0Uu(yJ%5N$IoD+5Pt~mZy3$i|dQ(1FZjJwaRp^LBKQV^S5&^%2A0Z&Srw_t}b_Edg$WO8IZ|xQjeTpK6B$4zljjmNW#p0Iwp1XOzOfRa@BOsjfAAg+?c{tM9g*tFDl%fWOONiPnoPa`?Pho&^Bj_Cw{@~s+4!}n329p>We6nGtdFPlV%@bZ50Z5&_#5zB2cp+cPz4+RWVg+kzYy-5J+?lo^0bJ5N!^2XJm9-Kqw}VnMl>99=%T}$_0jmQy!D=mXGewhrblN--cA9+J}uOfdy{wY1Iy_E5TBAUh|K$GToD6Mb5~=301j`+EhIhuLK;Z@lTwm)e~b1{ND&L+ha1<T`~fXUl~|PMVT<T%Z3sJ)rC|z3dI!C9wvOL<w&BRG%Ts@&Knk-sI5FOrl;TNJ|SBZcK$vogWBs~1p2<RERLdpCFqq}xdmk{eHpUC1laU;UgJaiXF13=^xRJh8p^wCy9H_-u;gih=jb4P1MNXIjf7&26!l3Fad?wAu*+=LY;_Ape6g!uEAv=cVC1g&M_*e}>L*C*86QG^3^yU(Jn*Bf*e%$W_fj`dk=@_h7HONa7ms=X{i*#o--qH#5X@N|xntTsy?@u37dSINnDw8o?nMyDxX&KN)!>kMh;~AHATOkK(nIL)<JUhudPBc=(G}YKp#AeX$zCp<c1&!ER!fP#o*Q_M8+kyxQ_+`@^O|opU6`6uX>e+z#$09PYLfu0i{i8aRI|lNRJW;#Q~5ikoGs4Iq<zeDe_BFv-zrSz71JARabiy-ZDML}v5`}JXl2ns;!f8?2VvfDDW0NCjsdTEMK=`ow0IRM<>-6`_d+^!;M*wNDd0LG6F77{Wqq-z)Iko{#Ns{)hE!Y`QporFzdl?Q8?jnnrHU=N${($bozV){cWGm}X=CYB8!NBV#_GGYu^n9>scB=EnT5T1?@-0ksVbK8QlIFY!EzS)&8rzKJDLb*s+daesf>DKu)M5_m1k73_`E9idA#2L`*#(W!E|nMnPoahIGar>O+}k$@SIw@cNgD|>txsySLya6=6>5$TWH25R1p6|^_q^W=uC!Xo>iW53D7V;qS}syWt~!+vz0U(J&W%RtR<1slhBOfGH|H|1zbcQte{L$Jmn-J!x}ly1ZC=_pv*1(qds@4C<<HMJ+TSLxWomC#|z~7CqvDoJ)H&x;VkSd2fxk9y^<Br1y2N`0!#{&k2Y%-r&B&5TG_X>rlS+lp)0b7Y&3J@r!Ic>x7H+<`5}xKNi1#F%uu!RElDil5{A}|p_!B(Nk&l&xj>G5%#6I`>w@aqb(6P3vX!*Gjv8Tc(p1#~Ce?GHejFPwaC9ORW!+|~=J@uDA(aioT*8oKvOud6NW+40ybFU%S=1|&2&7m6QaF@742PgnjbfNoO<1Ud94?uj%I&`8T7(tQyT>t6d~P`3O7HX0bv-tKMIym(X7_)*f(I;-ODkn^K={s!gSOGJNO~g4X_jD>l;oOFu~_+|;3$%@OS&ena>?5SXQLpoCM_PCAuO7z=)G`znGvU)#34lIRYWM#)zILDti3KJF32#KYFc`bT3kxyFe{Rea}c!p<KHG%jN@@GaK#LAC-tvjiLvLsK4XuN=bDt5vM;H8$?lva#jaTtaiQU9#mYz#^MoH}O@dC>@Ai}#rY=V0?t~Ubo2+Og20#nwAH7d^ZazTZfn8xkzZ_lFwqXvmBSZ+3NeHuJA-wW;kA8vudlpnx9lh@II6SLZVZ}0@RvAr*tIcS=6WN8&*y+dxUV|9vj<JSCbs7fuK6GhC?ZHaVD6}SzKyL1U?BRyq^dq>5<B*y!pd6{`x;ZpXB`1W*9zS5MLarzkCNEn2yllySvZ!5R+h0V|2)8bi(F@}dN7lL{?YGz)1Uz6I8m@dgK>=N&x}^Os3LSxQ%E{Fzdx~4~LiJR*QNOi&KUBa4-pEf+VgIYIwK#u7Q_BYM5%zz+4cD-@9qlvRQT>rmh5~$`NH4bt@%AFvcz{mdk+ZLI$wqoe1}e>D@yYcNWDkRxL*e*aSoM$E@NKYesRUCN{0wpB<vwuMVAwGpcj<fVa<uIMii1u0Um)uzSoh@hAeo2B!Tl{vo|)!1ycpyQIV3SmVrD&pUJ~&gM1vX40nmOggJ0)3N~QjZ*9V}+B>-jDzPBaA>B!Jica89RCFjJ@X9b|D0#FQIbj1$lea9$MkLXY>TmV=P(B~P_0mh+6nRJ$ZQp5?!6)dox6oI%VNZPRV;bc@JiU{@CnNwoeDsMeJg^LUWqdL)9Yw$xwu6B0id>zT3&7v7>61XF5A`GPVMUbk4n~lvtUwF6-5v0&5NQH1_=3kn-C}h@@7;0mni2*A*(;0;WEm8t(4XsKDRrd_FjVw6@#K-^mtt<a4TlQ4>*CZf3Zqr5agVrwBcuC|ARClIR<)1kwXSl2=l3vxpI@SDfwb^xkhBH%H3M?e2)hY`dtK<{4pXd+h{7iU(1a=Psc{Q4~%A)NqeurmJSn=H`EJtwdsIHsz7s?BWg{JfGT<6E6L#!G6&yK<xwC4A&Ty7T>mVMPNj@s7{g^D@zvqG@`^G|1tzVCcYr`&HgAL%2yh!f28ygUU7b}Nveik2@3!J=ws%al|WQC&^R&gWy-G=g$EB^4LQ%?3>$Hzm~)PzLSWG$b}<=W#6x_VbxY_w=35#QnnYR^NLXo>A5c93Gvp6Wde$TOUGS{7ew3-dth{)YPc*wy}ix#i?-yA%!*%dhwMf^$Df8W=CUvgFGs%6E-gR`apUtDuo?3BkI!bNt0l5y^tO=T3p!$Q;kv!9cf5U1gl}upIR`&i8XOLB8*k-g#|d7tH2$ik6!62M_DNJjKN;PQz48o1dn&d+$mlJg5o0p6p;8!V~*%hY2@}t=;!CJQ<VRm?+VeBR<&BH5T#~yuYK`ki94f@A_2B0(b~R9D)ZcPE)<cj9_@=dn#^xNrqv{>viVSp_K0F4J8c+_C?;BCQX=GMEenc?E)RIyh+-lF!#N>E6V)m*p}@+prnq(+K?ZAWaHe{-nk?3aJ-yK@EK}OKY{k4t4Ncx$@K^S~pT75S9nRhEM?<{@k$t$<=rab6JDs^W*`J`#;8o8;mAF6M<jA#3f|4n0=$)ijq2UF0M%#E9uF!`g?##qW<9I|T!EhWGU!xaSE{<79MF1*mA@`l6rxL9gT_+<e*{0&d5?L{2Nl_9Rbmw8V<_F(8RX%~K95*xCdIZ9XkZ3t<2t&&px=la{N@38hjw_jvoz>{=?c;y<Mhf;xNx|NF=8eSat%u(}zV+}MQ`j3**c(&W8&lXDQ`j3**c(&W2X*XkF`BUSMib`HpBI?ILUYuXc;pL1w(v82VL`R1qN8A%KWIlE03Ak5jbkEeR2?s}krQ-@eb>uA5vam+=Uyy1!YdPW#~Ap+e&yJZ;vePUPb&s1y?4hyb8g(dv0|$74D6>&TZ+)@x$5zpG@lcVIl=#muIq)5?x#OJVPQJM38V8&tskVFup-h@aD$_>X59+OIm^O1vz5xys_+sAmr0`wXI9#(E^g=5ZdWv0r@bA{j+}RzQrK5d?W0h_Icpdz-H7<?I4G;DwKpg9VaG>E>qlUzD^&$<Z9}Im>|jTxGk>lXWmtT2+H)jg=^{JW`DmW}<m{aGam66Eq7TbX7?GOXDD?Rk-gICNg1%}$Tr-G;#>}P6>v!@cJ;&s=Fm1h)cq^pvdV;W!oQCP_x5qc}$(!d`#-8WcS{SJo?yB59%WQQ<1okR|vv;<6_2y;Xv4wPOP2ct$*Vwaz_{_J*-hOgIh{rd}D4&yICAVb7I7VEde@vIiw!)=@XGg-5yDx8EdbCD=cI1gW8R+!v5A#cxO>4rk^6a-4ukhTrI#RgHGzvDv+Sa`n^6|}c9d&YK>7ti-$JVbv7oLW?{>rxmnJr!bm9OPFyzH11DiRaL8E}^M4q1ztFxdq%n@%CKlS5{aG}0pxQb}&kX1PMgo<d`<nWRmi>SP@*m~7#VSSxqViu&^8Epm7PP9xzK`kovS2NJaqrJ8|((&mtg2uqPYo?YT5v<^ZWBptnDo>)8)^Wdw@D&DL*O6U-jrjZR8a%OQAQl8qicBC}nnFO$c@`VvKCL4FGbQ+Z(<uNrRf1@G}@Q7nfU3Q)nlrjGGj{;N-Ojdb4y1(TdIlBLuv?B*pOrCs%s5vV>AE6XVJ{p6nq_vu*4NW0v+?WWEcPwF9@}-McWOE7!q*V(<f#90sD3bG*wTvXMtb|0gmXy>{(W;Ux*%eUFsrMpYDK|L3QlAPHrSu%M-&5MP2-4JHtZ=oCIg(z?HIeFxVve2WN-z_eW^pft1>jFIDsCN)@h=PX;=@V>Uw~eGY6Q?9v<W-gX#6<TM^v2}h|hDW#Cmo0%DyUhk7aWo=f|*%;mZezj4#Pru(RR5B}Tf0ZAm{)q#K5Dk-zpdoYc?g?XEGZDj$DOeAN#gf{HJ)r?HN1b|M1^>I0KLJ0jLg?*Z@)H?KQeLl41u+VCE^8Mh(dm(cAPDRp`l;NZK2VsMqb6xdm<g<B`>b=8g>B6WjB$y7Fkd9O&zlL+S&6^*rdH-;N=gppjTIF}AaZ2WtlW$}Xr<GmI?1K{<^`oA8%-tjQJcKr)e)t#>Yj_W_axc-TtQDXNqB7pU4UzP&7Ndc7*_m3-ZReo6tw7gpe>7x*@(RYQ5QXu3PrNHgGq`+pKqjo9<J}(%j{1f4?B9XZJnV?mQ*DsN8S=xl13n#Bl;roJ$;>>5Z*;MxcKa@SY-yZ*tX~y>NK+BwDQRRVniAN`X+C7HrkbdU_5<jou)bPK&_uu{sCVR0}Czr?8GapL4XGS!T6$H++866WCCJq#iMCHE|D+J{U8b@791>4YmA^Fc5y%|FmyWrZ}|L_Krc&nN87HfX{_}0U3(fqegeuGTBK_=cH6aRoJY4Hs;@rIgsLrwgHj+*FSk9i2CzHsp3x9<&~aLUiu!Y5YPiTXP1MAu5rAauTK(cuL_!4=gpGSp>ZCm5d#O8CotiDhKYn3q`76+(-E!wWiurQBDFC(-t&kco4=#K2%yIxkUnL`o$0h^`?Mp|tS#<tX_(P!ng6jHi$ZMry)S2*<Iw+I(K0Y^m<1s$gEoKCTL_RV7?{p)!9Wl5;S4r#>$&M08Ts?1(5R;c20}r&Z!o6$Sn&kYGHAOgvj3P9zkq<^FMjMyN`hTvnQ|+2e`p3UIAtksnzayc~?_<XJ-Wr#n8{X-PaqI7rgD>ex$o3BSdYgUi)gwX>xt+F5I}yYxw&lv)iovSVa{B~FkMF+6=e2}Y;OV2O(XeU;!!Pw@<=@qLd+KVO6G;<sx!L41NSh?m~H0GW6PUP3v0uft26!6DvVW$l><dEx!L%eJLw5fsPHe?5reV&|00y>|gbkzNYu^G#a72FG(=0|Qu?<l@J|LSBYUy!KM%nR0ilK6(1_Y`&c#QqC&9`LBw1MZ=u52wi!1kEPSPdh3JBR@+b$6d)%7iNE<#akLpkvoEk@RMkv6<%qIxH)UZZ@VH_r$Gr1;#!5um%+!Z5#bFR1f!L?hFf)jD7DQJ}B`UlHqKrXA830Ixy;w37pJ2Tsq=1%FZX#AJx{^q~YMdAy7@i`J7lzy77L_`B#sr-ckIAOx4pvtuih({`--<MQLu3a=bw*bp!8$XHH8}HrZ2>HMppl$=35C(pHJCmX!}_eDtN-Z3hza6t=nlb&lvuu{0@DJm4q;f;j~a-P$u>2}7huzzbV|Kf<dMd}8a<g*p{C`G;&IC)Ui1v#4MU6RD)f{?ZI2Ya8(DgVs?=~7My#@{wjCqPMI}raL>)wVNP>GLMh_^dfLj-_sDP5B3m&SC9Ii-~93pq{V^S{0Mmi;4U;-=&b1AG?1H=$8KCDqpiUBdav919pb@bRN!4U!c*Cf;NGB!;=!!jD2WJO9kD{27tKw@Jj;LvLksW{WA5y<5vm3nbd0V9!$?$NgBm242Ix7Yla--35<!MnH6(%Z+k9)9cLx5(XF<nAqU_ZGQ(i`>0M?%pDIZ;`vV$lc44yLjnfX>YnupZM&5%Wq#3x#OGbAYAuJ*p3K)(#SF8xw<ohJZj2m^{5m)A6-^#<7u*UK1p_7qG0RXXFvEfayQa(8sl?ewew8pt78)JI*;|e!gj~J-HVYsCJVdUza{xzcouz|msr?&*7Nap)kBbckYft7XD%0|*(Ogj*cKKPV32B^?;O|p!Y3Kf3V5y4t8uR`E_uNro#b~f@w<?HEIfaCowD5mk;f-pMIjY}^!AjN|Hz`mX)fU`h55AE7a!p)dp(N$`y{XV`~gotu2Ps+AD49IV=i;{AP$R;hSDpPsGbjb==G#e19SR2i?dwFT#oO`pMBrg;oawi7xIzcC)9GDeS8`#d?E7nVP8EHd`uUTpx+e_qT}<Kq~m;=bo?Zs_U;^EKc1e3c+TTHPmZjo%_}pDFGj~ge)cCXzg|owZj1MFoa^a17ZZxty%C-Xe#NsMj+Y~1tJvJ~{_M^2N?-R$wBwH->HNRovi*u#dWv?SYH^smGWP-bIY|2o<JSQ+vz6v1^1{OPAr4yz{%aF@+pwnup10U!RnMeWB-qrE;WIoM>g7x&Az_z=)Kp=PR3gm(v}SC;tS@TXnRpWf(d>CPVM1x*AWmCUTqp>RY<txJvrB}D&VBpU<^W#*t+JI-Gp-e@Vo~QQG0QX~m@#tCpHTjQlnfoO#;SX$yHZutjI^*B)p*K=mDbQ^RMWr(uL85)f@;VoUYUU&K6TJnDUPV7Qbjxer^6q}Wt+>G%lC8YQOY4bGH7P=;~{$C*`HJ3i2}tQ^`0{Nj>TYd1|zPW!^FGF!chpfY5RdfX-!A@NkB;sVP={6nTlo=MLE9Bs8p3yokx4BpeJOA-BSeQAbsMF@xZP9<RK`})bFxo^LpnGu6*4oS$q%m==xZ7G9zqAep(i0!A0~GiACI$Y=x`cBMiG&ol9;1cr=t1O0C8(?@n6%TVw~1B7`S4NU<}!S59g?tCQX7MnTo)=3A!DFExG-`k_+8beCNI_J;%mcfqIoS=QyO0Ov^=o4n>Kwk5$lW|q_g<L|nLO+Bk&qdI`7G~EcMTVdO4RlXfq`;YZ%s}q&uA_GdYF-g`*i?ix$^h~@KMR`&^lU4N^MTn)c+Ipz`V5`qb%ehrlRjJ|ZM;d2td6HXaDKCws92I4xO{sQGS*rMX+}a6@gQ{2|`PUSVQoK|q5+-{rgY*#@lApOI%^yA~qWqcyqR-KlU#ah@=_49^!hgRdTSC(Kc$G3$k8~Dn`$@ivOz&lJsxEiaiu|5aU??oBs|xJQPIfBvf&#!@@QMh^-p{Hil`^WkkR#vD+SQEO>@2;VY|2b|WR(L{Q0P+Hcul|!_`Bmc<Y~s9Vo%Xe*mvrjb{&WMCX7jp)hwP_Q1Qa<ve%S{9nr|fdlL5l3-8^{GsO9Ob~E7{Vi{P{rpsv`Z%;e;a_?ffKJC}4t0mQg%DAICwXutX8>2&`?Cz*EgA%S3;{`d>g(9X*;K?XgVVodWZJmSHX-ueaW?eO>yACpN>rer9?Ka&cB1DUIDtdJPFMg6)`<t#i39LEk%R@vRk8$?yG`&Q9iD`G0?m#ONMpb>`dT@0b#i7xuNDeQ#vQz6H`W8BMp~AoU&N{WQM0#P3qp<YrS*P;7I<>BPG_qLl#7^xsL0QU~Wie3K0<)7Y4ZHp=do*FEvvC72+AiG<e4|PvvCUCIdT%JaS3SD_<?xT6&`=cYM`b5<jUAf#TG+Eat9S3ReY}5gz%5*G_LE!E(;)NPRL>w7*02wo7_Ykg<!#i#A3S1<sU<(`?MR$h<0WF8^5GT(gQ9zT-mB!h+i2sue~6FxHbRYhAaw#uZ`m{K_fh3pc8~bsd_Yl$AI-MGxn5?cefbA{&e%5ki?6G5_?%W^b7JONT$j2q>AIDM%o&1&{9|FmYie)Zx~d@?jJj3xu`UWG{!+#;lh(p!$jmn=Z@)|rl!!hSFdVG^(iPE2C}2pp(tu)fW*1<*XL1bDXVOX+M*Nu(P<cXcI+0D7%0eZp(uFx5v4W<H-P)Y_8VbeF{!IKS&Z>kL*~Vge+H5WD=znB!GSgi)-1_<f{d!2{_Y8RkfDX@Q7E)&?(BHR7anl2dWMf}ZqSIzoh82}%&G;z&{4z>35u`qLB@BJ&cV-yDLkcbe*3huNnxiXNGnr60M~lO~P5;3oV@Nx0jFq%bcKaFRIYA|*S)V9fXE-aXrW)&bN7S}ZEo!hJb*dI4h<udLEWD;OKamFt0&(m?{*(#sswBpmQ&x4K&c-l7N_`VV_(0`WmJnQSX0xF8SnZ6(3enHj3>HXD6i6ts=QZ26<ddW~N0rK<6td)7`k_O%ptep~L=ylueuHNPvcG2`Rus$N<N_3p43*zdHT}jNzpPPB^TgWn4OuCAqR>&R+y*q2p31CAu5YGfmacdwrkt~*$g*`s>htf)j=1E)$kdftunA_aDMYA+UMftRr0TI8be2B%qP})BdxRgSaD~FsP-Ha_gX#pr2t>KfLrZ$-#W*suz%PG-*Ni7J8TU=};y_ol{%STIR4g{ED(G4%Z}eTLx&O+m$^}NSnAy{BuVqJaVupNUlN2g`-riv+p6^g!Rm3<+bx|}Q4_TU`SGBrI+X<_}cHun|V^G4eYb=^nf0;dD8~0$=7@R!2nD)2spk|pA61!k$*S+#KQbeM@4oqTloZ|e6fX8$dhRNE1kG5Y_O0-VAny7pOQlm^Qe7fcC3*96SW4M{K8K8EiorC4dGJ<kg$@+|P=-uMA;@MAo_gCMqcW=#B!>Dh}puAzf-ttzq3!$gIr0&43wLPb*%rs@epne_QXWZY|X2xQ6#7dSW&TxY=IWst0;&|)UcwvmhhSqLs6L8?KrW>qy)WU3L{~+z%l%q*La`yTz%b-x<DRhJN+yVC*yq`ED?jhrLcZ6Z{_~t?GYWIa(8}>Ku#qYqrb=r~t(^4}Sn~OE$TdZ4$hiFVoXT`~EkL_A<vhEd?$xsal*EwNYS{1EJEb*jr%x87$@~UoKN8Z2TSU6ohM6#uU6M9udv1>&Xm)hy>Sd`-*8(r)>r(7zndR=aglzgFj-K)x{->D|8yaUro9mQ^`oo-hvoFHOeV+}hDLPzKL1Rufes-zjR?5^IodhKT>Qi?b6r$@F&jQm|=dxR0UB78)2Fb}oVLCP({AC=|2O^K{x7-M8Cix7_!If5RM=fD+8eHfFD(b3$LCHY}m{3|lzsYP1_zD`P4q?l-)9Q}m5CV}l8_Iz!&F?r@4qi@*IvRpz;5+gyW$6I%i2yvFK9opTy=)Ou^CwabD497ED*>>DOrwzP%yDZMxBtKatNIjA@@O%Xpvtqe^8h46zU!dJHwXl2*v7Z&bET`ndWCF~l8;WZ(#wGR7OL8sINjrX%r3DDOu8QgYt;C!^qf$OGfO%&Z=S4=|bmQSg7P)V)*1W_2&)&Pl%Cc?QL9sp&u_7|^vvX(W-sj%?UcFbol%HLGrE*!gb!gCm25lseKt>kgXJjGE_@^pd7%Y{_Hg4eJQ$`30W0jBq2_z$fWYI-J(4b+tK?zV5g;l~pn+B{g#$55q&;Fcy?m5?HUmfkccV=W{#EP}%nx8Spz|Tq|bB@ea8k0vq8#ETfRqb7u@<H9QJC$FNmUpKs3B30eKh@FiNNU4`D^!&m3`%_JmxECM4&_5iXY)&geyK#@Chjz!>`1@`Dtnh~UgA&oY&7v!2<8*`fzd98uYdUsx&MaTe?vXL{rNV+ZzKGM+<!yvzajU(qsV>#HcQ_$%HA;hZ<zhR$1(fqyR1=0fYf)1aEp31#?3zG+ydSH4dng>;g;C8kRPms80y%QFw`c#QH$UJ$&FyC88^p?s~U8sLN?`NMkXp(U8QkCQe-ex^+e`$F60I1HxsW{Q2b|vUJC^J*`IO7!sTZ2RvO{vLeI+GyoF1euK6{1!QSISgUe9H!mzK1p11{CFR=GZx-ul_7Qp%0Sd9u}&J@O`(T+F9%AH@Nnk~ox6whGwPoeC`3m(71FD`iA6;ZisT5#@yy(|`5uhLU8(vmR+M@}_k)~ThP5)1L$99(~ite-%~@#V5${wYDQm%sHAti5{*Yk!-|%4@T@iTHj(lIsa@{gbygy&IoDZMm=8VqdStt*7fpo(XoHVdrQ3XMTRXn|;d@q)KPg$vOtyZN)8j{b9{1oq~HkW!HGx=EXSu*{7zD&!o&|x9M%Pm!SLeAzi}l7Zg?tto@R{&ONE?wW#a-<~J=keyFsIQBr+lX_xNx(k^uYhrUSKiFKMu-6aC$d|ldw)y5=I7jKF#@j}-rE_I#iD>cU==aNV2hN4pd5@(_1(pSRNVNwAfbtdQ1QhfwQcA@Ch8d4dBjh9p*(`OfT`j@M}#1drw_j{@)&$teVE8y!B5eA-$E`ZX7ZXJgnjRl-&E^R`p)xp3@%_FaxB6DHK#<4t?NsDT&5%|d?TVO2nkpt_%-A<KcOx~~-E{#|l2OxLi2g5+LUN9g!j@$yrZvBH8eS96T9ISkaC<_ka8lUPSPBnmZ3fD$3BE*~OJ4#1+Q-)2C_&DBuw3`~xnuyMpe#3SI)<bK)5_ha#@w*~D!hA{OvdVMN2-JY2{Ig~ew$A^=H-q!#TWDFEUGmXkF48vjjp?g}sl5Pw8nea%8bpsJ4N)B01@#jUXRz!i5FE4>@{|9fE$<dQVl)afAShs5_1H-Om{k(LDHl~Y0AHyE8F=!Zptn^5E|RSuY9sO1&x92Sn^F^ZgS^CJ;hM`!Yc<E-a%pX`qdP5|Vws!Lg(7a(M7T)!qj|=A;tCN@{BBIa<{cl=0l?Qi9}aMw`3344VfK?mtPxbN20LIw<H&-2o>G{ReitK^k6`?=4PRxO@8cTgt0B-U8^pBc-0eVg=4mnWyIl>nGW1I|c|@yFdouZ<MJe{|UZSM|RiTHr8CHUL-dfnzY}eTBL<~j`dq^~YWmWM8fJ#kMs#med3VemJyb(s{2`C`cq$Zy+=vdYHOr*z(J<~+C<@>D%HG%NM03#6TCpGB*%clE=pLnLThLfI<gSL?EHCyX^vIStBL&8>#%#4^@W3P>YyILb>Y}l?u*rVEQaG!hvfelR9R%U%SPAzI<>y1-`1m~Q2JZ!*eC=VB%)(oLkNrul`F9cBr08Z6>)SjJh+`b~P_I8Z$I79O5Xe~MU$X$Rr>IjN#1&6Xtys$S$^{QcCT^lyb(X>i9lh7OfY-YQkz-EIZ#CDDQn!0uP%(P&d%C=mz$OTI5abr!@*u3N0v2%y3od<`ecP)eP6#Q1$jOh4o)#WGHQz_4(^WaNHP>cOgtiRe1P5v)CK5#nL-pm1EkDqmW%wPJO-y(+Ws!IoxzHsS6G%ZARkMUW}z+`zA1A{XIlXb<hqnavE+(7=r6#IfnmABl?@nrc7N&6?e8Y>$7N_a9uf=Jf80qr8$El1MP5l>dYWEMCJE|eY3SV^7UaV`t!ArG$^*+&;(vPrpb^zFK9c(R_m$%-z9V<Ut?%3`5_<k|(vri1Jx`8KN&RYrbHbMky=ser-TUW4W{BJlEM+}{%E#DX$^uALP6IAMv#Z9nmx{i&CL-ur8y_x3r^`|wK8d$z@qpm!R+Y^nI<33`v*|9?mZ0!>IE-oGx0_jrMLC+y1q3>F&hBF=&CjOYUsftOhKSg`J5)g6KEeTzG~1iI(r(Ak`rcD%s4J7V39u07vNi`K^p>rT=8gY=ULdarMT-dh8`i>7tLy+?I4UB$gu&OSoud%S?Yv)|e)W)k{6&Cu@+(eK=xfPPOxzrz!`3V;vW8TviV(C@#KTLQE(iGKgNe3GX6Qu&@a`kgm>S0tcc0E5T3oFU=kITF5z;o`0D1|I%ze)hP(mQ5Wu3HMC&k3QdP(Z3RQsq7QpasXEn01C&WB>=2SG0y=s%mL6G&o+r`3a<>W7ij=zX#i~%0$5`fUn;z^C!ehtq!`eJjeAB|>O9x(T1r5=uWsBn81DNiH!#<E&B0wy5T_;F`SomnCG&Andj;jNP^lyg*v#9R%f^<k;qHT!pD|6Mv$~pc*<!=^XJ6Dfkni}R3Ww}Y@|SlY6(?T!`hWShQioAdo0ylj$-#?ExjE2a0E&$$98>SWp1I1j&e4MQfP?WoPgcAb<T{^VZu28u^MMQx7EI?U=GcMf8ICve8qmEXBQ}rOTM>uc2l;I5>hS6{$5xTYGqJG>ZpH)qKep7P_0y4f&i~L$hwZ2F<sCR2aF==UtONG4;bcykXp;Pc-!Xp0Wj?yK2Il0O(zO5|9i!qxkpQXpKGqH`VC*n#ADlnssTLG$gcD|A4i6A$K8AR7GN<{l9X+!80pFfa*c{xBH`o0iFXlIRKJ}oOYvMQXQ^4hkaB=LSL%^lJ)4Z34Gjan=onAp!jm!?A%1$=KY9v?UEV5R#bXyr^#;GVc<tgBV(%gBqL0CJm(Clz+(b<wW@|uY}`o0!<kz{Je!tBI{5Ltt2ESI6C(Lg+W5;214zu5Zdm5-v;btMD~R}zqLZL+%o2f-;WGo#o0v7yBxGC!&wm;{2KwKodxZgdJvYG9XamB8lw5@em$l#M<W8B+4~H~tWoqzZ1L?4RsU18w(EbJI2x^f^PY@bw4xaJC=2hZFAXmR-NsJX*DJ?k_yr`{z8`FJNDABkj_ojU427&7*CKM;n(OZPVrm{<=qt{hr;M?&<E$Gj}$+LwLS>vwdavrqWJd(S>bpyRh-L3mfUew%{^)qJa}8_{dfJbPp%(lR2{JDFuznr7!zpFP6E*7dW!Es%~_3VoUwhj_hwuj0OHfec5ZWD#1Lnr8|ot8#ZgqXJ_v)?}HmPGSzBlHjg$eNpte%lSBVdcyk;#j3&XuOQT<_%!dPGl~VHyxt08sxGnA2+XlPNTwb=wEBK#Nh09VPaL#<wEYcn=_Q6@^BQa$%w!Cwvtd(&kTBIG592X_6=TaScdeUdrPGHJ2PClsgHJCLcI~VdC)m?!psiZYjV>4ael_yu#vzPG5ZN(H_cC*ag*$y%0?3xN~-Oj?X&)ZCwC*{kU={S$T)sXVf4PUuqmt^F0&a*Sm=&oYFD)CGk6n*HaVDY!kAV*%bpK6yB9*F7ihK+J)FykyU`XhT{@)|JjRLu@*c&>wZu<XG?N2Q3S(YYJ@<9czolqh53g0q6hL=ET1`ZQU-WV|{~+omlaw;)j&IyTdxEK+*Mh}s#EMwU0E_rFsalS(X3om^<OR*RoCyNw4YRnU2Ld1@&ofV7~un9ELLB_`bq+sb@7*cFaD-h~_As>aT;se_MFIpI;wuP&^|rnb_a<`|kW%c+|^yE`7N@C{En&j-%;@dEtvNcf4RZH*V>Su1zCkuXcPa!1uh!rOFug5J&U(H<yn^I$h+t&ZA??4eIXI*s!_-)UcY)4*|K6|MC2$!8`KYXM(yf<-!S#g6a)FVzd%QdeLR40mB8qSRz#hNbg>D;nW>QP_-t&Tb4z7rUT@0TE?#GmKs@CPn|T%u06rg3^eI0#aSz+gq-N>9Bkf8+A5B&);IxDT{3+(WnH%sfa?M-cp!O!f23zJN@WLpU2)p7i^iNm3Un6_$<#%|I@`W?W_~Z_?i*)g{8*~0|k?2x4<+t561j!?8S0g3%#|P*)HkoX8J61^O{C%){LbAw4UFf41-xDtsKP^*+S#sG&>uos4ZVh1lU5Urz2(IEJ0#gf52TX9*td<U7lS4$vei#FNkN(SIfKBXN$dA+4YC?ALoF5_-U4IA2~gbd1u8VWi=6{+hL5~J5+BQaSU=X(%Hy?G3XOug^wm*6$&H|PoM)&5zB00wecy*?-u7B3f(A=Gg?pb*=ey->l@X#cU5ftj%Aay5)Tt74YPlp=nLW_Dqd>3(IMsD?dq-+v1?z7w0H~Hg@hT`G<^7oY2p7z#ui?4lA-L_CQUB@ggln^Qe-G%6FmUNRZWm_v@b&aG}<F#kACpFj8Lv8FvOv&;4EZu2IMq_FQ(oAo>1l0tE*Ux28W=?g^y=vudM~%)LU??StfFclVaS~7#0U3iutW?G2IF-$D8TaP5lipR)J)hSF)@(U{++~>gB|d+M!<NS8L{1!!?Xmv&^psr4f{0Wj>bE-8^E|;c8ckaFb_hZmEz~?J~3KpG8{PJk+N^-emX;vB1nc)6PpHu{fvKU{>on%nEhtiSJ?eBEAQF-S+c(seiKit8Vzc)#D?Vdj7h5Otj`PbR$m~y_5Sx=t&#2x+fQ^TyutmB6!VP*!O8%nr!N7AS#8u-va^_httF~<I6)%B#JRIRuaJG!v<Q^hODWo2!kIc#DQBw$Fnsjj1w7Jh+N3#uOsOy{eIZVBMFs#CHuJDF)3)R2N?eDSdGlHG_PUU3urCWG-hDB1F$L@9>ESC_L#qYFt#4jU4>?gc@a(X*}i4ibM|rWCt9B2V?!}7kSJp$`;<l~jD?)|D>3Xj@vBJQ$Lc*F)Qk!yq(nH?IS&lZQ>rq=n)t#4Q;bCqnmhw!#!`$47Zv-awJJy*{k&XX&&)(G`A{p@lO6DO#lF790JDWP>4>XT^M^Uagp$B0D22(y(v_f<V5$+hzZanq8KiQMd*AwCDHB)(tV0IK_hM<3U8wy%F4_<<O2)Ki9b_69)qXnb5bD46iGU_#(3xhdwJyv=ZJYDmZA47@v}7&HC+wCW;*j@|LR>_}(U8t&tIeinn23vrHBl8B&$b;|i;&vZv>l~wL*r&3;u7lCj9%o`))Q-yfrwk<e)gAqMK`g-Y$|c(gC{|fH!jb?ePwE>;<$mmX+=cGY&__wZDQUNZG~-1?3NcK#!r;|HlKH^`h{^a`k(%0uvM5JD<3sywIg6wIT>0*uDWyNs(2}B9Cz>qt{_*>nXu_YrAy@MM26K4bL1**ZX_sE#pgOtd}BWwBAF^18Lvtg3;T88YB1O;XwbnX+q={iwCZX0@TIIA46vG~|6xbuH>hN-ew*%v9SZSZdG)~GqBZWhfSwt6i#ua@{lMpu?zo2M15dcNKOg%t@K}Q1c<gsryYb~?57+f&WB*^+*zcYH>cyP!_fMGI8#PlDeBH*A5Z>P^n3mz+i-gy@$j-~7!vsLJdgwqhRvNc7RzDG#`gV>u1yk__2|Thil}J~~WLOf_^#WGv$nF<+h)qQHPc$k0k~p%yJBAWoDbs=-4b7@RM!PA~{3VJ>H`2_5HP<bGpeq0;(x<eCYsab4{LJlnp$c6S+UkPLd57GWdE+Mez_Z=mm>|w1<CU))D$^rsragI@FJYQ57GQz-Y{T>#H=c3Jwdo@szyf5ZTPaa(&ZCNiWChDySNS$8w<>drA|0(wD`s_=!5gv6Edf5xNeW^l77VGijD~39=<EdwhjSLFLg%Ko)_R`VGbEfBL0wHmM}t|+J-K{pMYs@iQI)j`TY6q;b^9q;e4IegmTq744tRZb%#xD#j;CmewP6;&GEYS0c12gp8TN-DtUP~P(3!P*ON+plOgWR2daI>uIp>{Pp#_m<|H9<6PT5?$yI6AkXX_)D1UAO%lftF@-~Py6?1zP2v{}J@yvQpO1$@cCiK-k~?M6sk6bO%{^097ML|FP6bUNOKPB%%k<CT2V2{g^!vUfIrm!RqKdtVZTp-_KJ0Ne{r0v=vx30IPHk_k7uWkcMx>S3)w4AY#rw7kt!s|e<5MPc<a3Oihh!sfHs_TtYOi2e4rSpx@atYCXDs)08zDS(@^hG?Z*7Qg}QEH&^3OXNx!d^w%149;z)kJoD8+({Z%EolvB#qcL9;eM=yk8PbFS_!X-iCGrIXO(bnO>4D~&<`msEjR1o^>RiZ-Le?&D@i~-RS#c=Z=ac5_CJ5)$$aC<eB&5=`}1vt-&h>q2KkLD^NlL=jVkkv(eaHc^NlL=yB<@xH@3{r#FqKpqRP~}XFQnz5#Hd*9FyLH7gFd$y^|Cb>DPv9Rt>^O5yT)9KNR4l7s!KY)4-&SGZsw%#wKDzBVA<6sS#;bVa6mWWJXwUJdP}yqEuOMT_)3eno}$anJ)g!s+ss0{RIu<C9~y~cjFb>M)dNIdHb`waL?Su**~V@4Cp%zQ75T+A>a%OJH30Ata3)7Ii1`{9nUY)h+AftcgCVwIfE)(VXZ8%<TD~oArr}T<zGdo>6eU}mvox*hkHhzdC7*lIADH$SK6|TRFgSEJ>^6I`9!Mep5WNLqye1R3oke}ZxC!2LfR*oD*bajmLEj6d7a`iTo5fT_!~Lfud#7nVR3x%SD!I|KE=K1pXA;Q=Vu-V`TA9T81v)>3FqazS1B}g!Atf?<HJ0sm-N>;Jg=VlRaByGcALg*bHUH~%wv5yPw7w|?h`zmbIMSE{aw8^V=E>4@RFs|KlSH0>{qxq{rIyAS6Mp4S!(=`RsXhY0(uAX`>XGng^61zs}0a3tV};xl4<;9Xu(?$Jqr6hyZ%=Z)CJfi^NTyk`~lPfrD5t_vEKw0py&@kK%hvTR9#@3EK2&4A|?j5iPf6r_q`~i*><%}epsQALYx|1K2?5q1#+>0*ciVBvQ9KhqS*L?WDF>hdeSc*P>L9U2=~pdN^Cb-vFOr^MIy5G2Dork^pYR|g6@LU1<*NFGuhPZgs#QK1NFwzROJuB+Rp7~wnM-1NeQzAbVm8tt!jhZ@~Xr2!dW5<L0Yn91(855q!+D5W}I25m!22Pk~Mf293yM6BPHs@nPn=a4Uq>v3bcQ{_8W+Yf`=&Aq`p%AT@Ypgmj4t2*WW_m7JNRNL<mL?6AVKBI*32=7xn1iDjcYA#qwyQh~3O!`LV$ASGQsL7nL%F(Cg0&bo|d=%#$%;zFP1U;<3(Ws5Q-fQ3;l{WzPhdq-wQq6v|p56@z%m@Olfv53ingF=V)PB|;s~?)Z*)I5b3$&6<&dfoQ40QxZBX5s@f5eYMwl6o(~9?9G%Ae8U3>Kw!b1I2>z{%v0jQna1}zaTit<wemu?G&}~a_Z3wdiM{Mt#aC}ao@g~cZjzGuvT0f5{yC!Fuu2OHoHt${b&>H-b?|^Lq(Bs#2nmjC<kq%8vIVs5M*f`XEAl(Vk4U9L03Z%Rb$E7F;;Qr7C&Yovnam92D+uW)zB}Y;sjZqNdD@v`_zwX=I#&$;`nF>DoIfoV{<Qbc357Qcq3{=wr+F}^J*g6Yi#aWCG%ur?kfg%}ZCbibo91VnX}1X{UQC#FgDtIjJzLsBE1XP7AC)Q%u(<cmZte5)r2Xyh0zbMdBx&A#AVs<>?R!2x!;(J1TAm=&j1yh@f+}rt41#*Vc|9XmdV<q5S9<q&n?dwSMwA|2MU-9_XxNM>UE<7hqV%>9rPt39rN5$s?}n@JnYq&c?@!Nd9G2Y1o0c!WirZK@!D?bSW=rTZ49AV=joFz0T83l)B*XEpK!W2F49B!bXf}J2-dNPd*_j<Y0NU{xdSe>+FkyPV`6KGPzru5@4y2|di)G<CzSH6>JjV@MbYIMKydr`9Eqdb?+uo<0)FJ(2)qmuA(#pAa@ELjqR1Spxs{>%>pyfYdB=X!`KWKnMZ2;HMJs<$e!SD7S8%qB82F<LY^C1VL;b@r~HF}BYB=6&glR09K4`FzKAvjdhHMdeQnnF%85Ma-%c?L29hV5NmVwJZLD7Gh&GKAejrM@Xn=g>dK?;paJt*+g>u;pRxV<ldGuml_{6&V_S{PBPIfJoqG^UV|8AGKSF$|I6QjysVp<7`E5wSlah$#|2WJX-z$>(<ZvLDZK6SJ;X1UEMiylu{D=zv1{9u8PnfdjZ=+n4qEGeol)w5C!UHyN{Yg*y6(tE{6d;Adt67nPGi(kCiDK-cvYU9liC$QA3jG<vMJUvlQGE_Y9YuixBg$Mt|3FM$-&ho66kP<I8rF&kNBEfBus-dSU#EHbi~B!%jrmOowbMvH$pyIotw9Fi@Q7M1)&SU%^-#QtA7O%f7FuzAvy>lnIrv@ilaj^2Pzxg;tzFOjqP5%m5ofZfk~J&Nl*pA`%f#>b78$izvZc>w}ooBG6lARl>U&O-?kbq>%QNI4R)}|I_xAe&(v5TAb7tw(I;U?Shsro{S#U9Sq}Uwd`3C4{t5G5qmiKBmI8L2jpiJH&vK*CCK61u=`7mJ2>;!+$n9^a&Yr$PXn928=v>>9OC7DW=%qX9IBv`W{p0(9P;e)0)~4XzVb+2rhB+5`Q2j^`c(BRdd5*TqOeQ;u7|0JG30fX{k%4x`K#*BRsW8we+&;D{V)0R_vi?Y-v_r=w($of2ZBE_Do4D8#A~yuwiw5-da$j96f;%ZRkg9DD0|@9V3voTfA)+TTXZIX(=~91U}np;ERzMs^);J(Nbc2e;F=X%0adN=a7(z3xN|VH;+%;Cl>}Rl$W{A0q=S-IUcj;Qu!mX)D3Vm8#L|Obhv)$`BKgn_$v0FL_44%cF(8v~No2L<r^2oh)s`1;cpkT%kuyMVgOjsP{ChB#<si)*csAHM%`Qq4kp6YUk*rli9gM~UpZZtxj*qqUL!?<T0p2<Gw(vBO*Z3IrkNE!lLjMS7u<!X+T^Ux(V+ni>(-WHm687lFVy$CebXWREEzr=PFzUmMh@xLJ!`O3o#5x9tL}wYS>9DjV(+c+zk8AK4aHhwZaNuy{*YBA&Q4ONFwEY9Tk+$@W;+4Gm=yXXr!;h*zM{T7RHPt0R#+7GVSYxwqDl2VpKjK~Q2%c@Ymtd!>gkM8}01w}AE1s9vSboZCws=Ip@FL1#u@mKKzNe8z#2?!HO2Ad;p9fd%4>*9XdC1E;ke9i`ybNnF8~IHLcO2b48sW9^>gvd;0ZtIS`v~7U?641J=ekm~mA|>W!+hGJKh0>ccXvM9(64oK7QKXc=YOiud4wXa$s|19+61-gV)obAjPhyy7qPm_cXs4LvdFy><!}D#ZXZZT#2L!3Kws(|CJ2t_0%)*)IM?trf;D7Y$=@WL{MpX?r(VkS{AeK?w%2Vj*&4aLp6~I6gUWb$Ep<r$y4of&`j(Rir)wVa4$OOOR77}{FL^IhP`i5NMYxgw-UO@`@Ja1i(bhJNdkyI>9|lvm!JmqunP5N;k&_!WA-7^GUHbvz{Te}P&2;F-SJ@x!?>vY$YAnUBIN6bnmuZcOamU!LRjjnP+c~lM&7*A>$Lv88i_;^m2@NGIvlFfHunFD4$c)u<3fuXMFP-R&8rplRg>g2+FdsvsJ@f%1ak^K~%$ecEFH1vsAKLQZTcJffEJOCQ^U8@<-N6Fb?5zVTR%J_Jo^vB&6Nq@h`qmR*0jJF$+#is@q&ibbYkz1B&d^LN3KRE)7C+p2xW`EbQ!B+a=Vj0{1OG@f(z84V+sz8v?#O)rM1GYf7uC-26<~<i2XT4j^YkL@=tFGFGEVre{T&ubURs;88UIgZ7pA|eb`==cu;2+k%mCuFJ+z(TKE{+^@39YsP?(97M9Ln}mgk`vM&4n|fJn*aefCyj1BEbZRn;V$dZaQH{c}_!SHx|!ByqV@2O(S?1us&m%41+Htf-(edzJ)RLc{|9Am9558K)>hbtW2+@*0q>b(;9uFX-u*G6~jz$^@Gl*w$N<gn{Gwm(9srJO9I{{k-Dj<)8Ogsy}!*EiKvT<kj>Z(5>e-%{B5ccr2mbGc7(wdwFrKO5RcUBIojo+<W?hjVR2W7`%+i56ma@1w&|B6ek<;i*w6S7R8HB7w)u6a>$v79hjVHn1IC7rmFz!5t*4m-?(KN*>+ojzp-}6mG@cz=rSByXoKO(8=SK)>6bOy$0zb~{mk)kBzI=BHUQhm?CzNgZD~?gRHGc2#TtT@bq;%0N?Cf!u3Wy0re)k#Go6CS&xL>B={nB9=wV*Rc~|N<L#g95ABi<Q<r%>`PQIQmuGMh{a2cG}afVXIY36kt#K0)!e8mkl00jVFn~olC)~Y!y<(}esO@}&o)GsVG9XxzzW9&u}@mi9QIX;-`J2lp+I{QI1njdd`qROM$$_#&=r-RBp`7W5xn``9^3<tL`(M$(;n2cvw#+|z_)c-fR#y!sbzTDSbH^(h&K#@sD)qvDFn&aKwbJ975cN`zTUJR-*wkKz8r_ZpDThcs_0D|5)BOqUthrH{2sSWk{{45Xg34RkX9sBtmsSy1OlOXAj8BHZjqLyjY37aEv(!ASmK=8Tu5)5_muB7Q`=GsRT!nf2U%~9WmiHx?$k^=0rCX@o;9WF#A>ko2_a1Gf-6SyLe4Kzk~Ab^TQ*2aUG@BHqO$3x+AXVRajr``tzu8jWu5UXr&>K!+K9xq<qyu-Fd5G6@OHK7y*N3xtY4JchE`hvb}`}t9{1J7gpos?q%f6z+gy#ZU5QV)5zhsa|M&vZjWllSA5!%q;T<|&we_5{mlx5vcIo&wGu*U^+(J$Jo4z%6oz5bLX*1#D^!PacE<T)GkdXC6yPoyU?^Ol%%V+yvNSjy(W|>BN0%h19<oS|!v0SV~lFmXVtje^<U{;h`ZF2&-Gn48YKV(w&8EZ2K`t*$vrFB~4jss|>s+V!P;!U@=f}Q;)^N3Ut~KWjF=~ocYBb{x)2bgm^MCW)?qb{P$nMoqVLR*wLrCgEPdsM7)bu^AW!YHVEz}A~4Q7a@^Xk!FmWRa}ZrInNI2f8CyKwP}Sn{uDuA}NjD*uWykx(nB9vtnrmAm+Vuce?A}+B^37k`3mc+;wR>#!yAypcsbZ0h)fWhgURxL*O=-2Vpu{tM)G8G~lyyF`4uv3{V_B2EIx1+d#&4Msi}R~%(KOShwPF62RALNk?J0*cL4k9WL)!@NX8tL2J!WS}cKnGf9AExwURT5Kc>(2cABT5_;KH2P<3gGf{|w|6hHJ=d_OZm1+&MLC14Hj&V9>Bb{;4ERz|WCCg%Vv&*QQ1N4=JrYw>I$3>7Qdvx&q^_d*4P&b!3M=UoDgNE_F=)mkt1D$T4_bb<I#iOd#~YBZ1bK#a&>B%IK((NhpN2A(WBV&jF{#qJjm?fKZ!2j<}zV)MRX3(C=MgLGA{EpGsE)31hK{5}ARKGLE1=_Ju%Rq@sl<SQNtffIzsjH+G@AuwJh*1tHn<8;fescb`1?8wj+!kzUc7FRnumE?I=bj74|>Jz)PxcnW<m10;SV=mBa0OXxvYpa<bO=)wI`qkY639AC^F{F(VY{!H~(jD8IH)vxG@J+R>KEMdDV30tuI*38+in9)`F6__GS>VfI=#2n^uvYc&GT385gW|nf6hDEmXI57|h9hpCVsJ5EmMN3W7uulv$^T2CO)7|Nhl{D%`LgE87(YSk8!LqVEb3UyLmU|IGaA1<wngB%Dsa)%+vKEBWxohc^0krqlmu75g1Vx_U$c$|eBbl+7lr#?MK}}AgObf_dRnmCiH2>=#!VtJeb@KTdvECw6zGU6=H*WmM&WP!LlfUZDXo4mgwRusvHw*`P91Bli&#DnuDT1e(Jb?|)x!?)J?s~x!C|ss5Jb|sYc5_VDVY#q(f@Kg~f)!gjtR|{Jvh?^R{6fj(m1}8J(uxasWBQ3lg`0l4dUf-FSs1nSdolY;i?`>Z4WAHN{HMRI3h%6Zs0uHRWX^J;^7QoBud#V*b6wPS(|KXn*gW&~gi_V@e!>e344Wb+$dbx4T~K*iFex_A&M0-SQhDxpWJ4_-JfeGk_T-OqHqRBG{F2S{E}AX|bHR|a#5VftAHKss(SgvaZgowvTN%DNfwBuiNZnHE&VE}XEfHTD56C)}M6O5|U%(|Ou(I&RY!B`Bf<1XA4B(KSY)86JV8RzY2H5{=?v@cKLv`&m&IDFj-KbQtY-Jj_v5&iV@>i&n-4*KOqRt%(OIJ|KfxLQt1ZeQmb>NM?D=_V#9Uh)ZS7f?H&Xv$mQ|OgBDOllOrRV6CDfW|H(Xy*+ONU*MfBZ?i4*qr9&wrMo-l;P9f-d2K^#`Qfu(5B)O6(~}(J@bPDwU(wszQz{7%NW{)o@Uj$Q?`LT*K07{-VyBI1u(FL9UK!0l;k2D}#2c!7*QmgGm8w$Shs}a<M}7t4_;Ickwk?q~CL5_B!DaXP|@xkB4(Y7lYPVYyv9Cq`Ykm91|{!1{F;A<;b1NJMCEUlza>dK0AimVLAyyGZk|x_gIQN!y}4kiYjZCsd{G10K51fUmCZA+YQMlOGI`2v!)`CywFfyJZjNe<D7Kh<f%f_xQ0V6Jwfs<3ah0W%|h){GF(WL061Z%;wq@D{i{MLqoY(yLu8Am1QOBz*3U~Xx(GeF5*Am!Da%xd{DJjEuS5V9T%5P?Tbe%H14<96^^6NhDO(VBZ3)+PJ5(1^Eq#2^490kX(X5vvtMdD*sBgt0-j!~gd{p;R-82-%EtN6&iv>Y?MsYmAw8(T!EK+8DxeGgB66h+20qkshq{SM_S#Sjz2W)lLl0W05ErLoIv_Jk@9DuZAb3ltc`8H61LmLn|QI9Ob$nhG`*0H63UK~yM3)xKUjtEJ2g2%EsrmHM#eNPi>Z)Hok57gy=bPB?UJ42%=Ky=J?=Px=XC%6D+_W=fLAiAnF?#s0L<6d0SgfGynkd4?{{3D!ve6Xd~77}d8+hOS>wWPzB4Sq!`cPRlx_c#C=VCEyAXKyHkg~|PuR|`hn(>f`3-504SW#(4Q($Ez!wWu}DHj<Sj;UZR;aHu(2BS1Er=ywsGVWaF2@hp-0H{5Kgc$!bU_g%EUufQi6)y7!y+BnjEKrSd>Odh@srBmt+-vEPUNXa#gWTT98846ciZTXAhV8VH214mW_QFp$nT4Efc(8v>=Xwiy!A2+_`6u3#cDk^anB!fOm+VS}?>y=+^9fb~C;hdPNaK7vCK0}X@O91v!49gB71{YWzR{yn}IZJE5<1;)+U7c=Rji<L~9eWev5Rju5REX57z%!KOHl7&jt%8j`a2D_~Q%Si7q(YQGiIDwu(fD9nqMw<UV!9Y^95874-ddw+cLhBZTj)#I$}P5xz*@_M<KR$8Jc5^;304kMH=$Nj94cWEL73|$1gM@TPoGa*)~+b`RXPv$2xY=?n89*QoDc^P6pWgKSV)w#_i9U)D59Pu?%mt;cgFduhC%7f>B~Lie6N&WrEW*<CY&pFWJwmv6f?!=lsM#M(l#T>FB;OQFitu*!Gz1$IBObZ)>v2+BUz|nLY{5;b<6JY_S?$vJ=tZHpLXXyLXvO$O_F>wg|M5sy|cvLs13%4QwK!^tVK_;fIsUm8k>z(mhodAnGdxs5kXi)1j{_1!Ni`)^BGYuvn1l3U*!3i31FUY78Hyc=NCaie;pD2xifr!5cP%pD1MZ8C>A|;ISeH&fm~1Z3*`;JM(6CqiSA?GK%n(SXDP3z2RxP^K$M4`*$QBy?8)U|A*?WQ*vbhY=|;kXbl|@7Mf8!%<tNT1x67Mw^`#1(`3XH@xBn_1cBf4MgK^43UyDB>o2bA94thQyKjzI>hlPE#-ye_6y}2rHt-~=pl-MO(VaGSH{m3Ss@IbP6PzOLnvNJuX&4f+|7RMicZdG4kb#5h9*2-5APZq_rJ>^v*JB3shMBY10ECPYYhmG`(s<sYwU)k!dK?4!gv0Px;sKBhIUckt3-N4z|iRqYo8L{yR!8vw^mZ6EW(sX{LvG;p(=6rq1fh&8uksAwjYZ{QAd)~1}*UQRHsS=EFmp3?n*8s7dh}ho$qaST79U;b%X46qRGq}xqW&mrK?%leQiG%%aTB3<&oC|PIHWaDYpoE1~ZOuVSaxriRo7Ty`0o&So{{^y;@Rmes)w3Qu_+#zbI|zh`GOD3z+Z+(|9%xJMci1ADf9czuO#N&o)r$H!7|mh=1x}za4uj(y8m0*pmJ=wPO`zI|rDK{yOav^a5fSwb#w@N(;sDj1J6K=j=@>O?KGk^?yZL0ILEWQl%RUOX*<-y1?Sc8TYav{a-3fo_)gwBJr0i!Ya5wc!e8c70adexB*uz$6X`JBlB+q@*s+keZ53|vQSC*&s#xYF_oE!H0PSMmF#qwGXK{m|?fP0~+*7<si7xQHtTc7tK{630+St|-FaRZtPw{hyD*#EBTkGv=-yu)=QrreOc*ayC1=VkiU)mwIWB)Fk<FC8?#f@A@Z0r`V@k>wx-FJ_zHWUI^HBR^7O&rcmqae|LnLqr)5pk;W{P%l}_yhV!^@{U7?P9b0inL%`QehU?CD01a398(f78y!=xbcOl$e5)p}#JBPZL;jb8O8^;Ktm@DLBTBtBfKh<7ZMa5iicWN((ZDv;vXFrb=ul0l+0OVq7as4PR*4^+I0NG#Hi>zvXNYoEs8bx9o<i{eTjfAQ)ox`%q+5uGuydBjlF#G|%Tn!3GzS}9%V-MRLi3!Di78D&@g|d8QQ#0LNBR5>M>lzaJmDL!z2GR7#1tg}WUAvjXYdlBX{1@xup5Ddg*vPFl=6#vx>MjLkq+=A_gu0WM4YfLVPe@q!1bWekWmRQ+gp4hq!1f?<j<L6xLqw};VBkZ#MQeo2c^Sk4F<2YQB@RhN`Pa%%%;;mYQm#icNE;2#M?!6gBA`Qqn_VUGswp&hod_xS*B_su0Eb~REC!(xQ#&g(fnXPX0CAB)Rxma%RbG|Y1-W5?ZoNe@t>WFOF><G;xjRgOkawfc4k4|-6fBfa*T=j3=<G%1}?w&{Xdp1dOC}|kHka9xM5M}5zZ=BN%m2?mVs4`V7w{d)z(=Wr9q2sWNwo3V}bbc{ALHrD!8W+<~;vPY+>B-3<fu2QK<IDKr0cP93AUyo~Ei{b3+uii+)qXrs|qdZzRgQY$G_{R+phJnq*8HY^%V?fD6mO=s8|vX@=%Z_$5-YAVjVSJ@-gbNmhzQ4I*Z^u+Vf?gtHN$wn*Z2j|f0ufA6b<gFk^3!p}e1dVH-?cwmTm;fI)_7`s5bQXt$QY;@viiL-68S+p2tx63g-ectwobTcIkNBK@``>fIB?HhvYID=Syf(lGeRhaCMY`wwk2k~r1>U*oY#Re5x{Hd2KoqXrU8X-xyR@ry*8-$C9@Yd?L$gl5xH@2$hPkHXg$jJg}85AcT2#NIhGNdMyPZo&#g8A6|<1cLm`e|fxx;*KRu4$@cetsv#Qn*aS)kp6QR9$5sH$9@vwjluxmf;-+-m8EQI2;1n-9fY*oEdq@PZglpm4C#3j*gvPd1<!QedS1Lc3<t#r{(<t#`i1Y_Ve$1OGU>9gU1l#q1q8J4{;l0Ciq?O;i9EV@)h2*#g)`TNYwp>mrcPLtl<gAZN=8k%XVayN2Pr@a#wIg&!%JPMb1-pP*M$xYo>b07OR0Xk|;C-G_+N!;np+)>=x20i6f^-Z8~Zc8I+-gM^dxN3<fVdg>=xl!xP8A`u3RB!ucVIgns~y67iPQ<q#J+{&r=Ohul?ys3Tw!htjgnO80u!l)TChWv3n=NHa?Msx}PXG-WaS|Gih!6#R~=9$XG1+dF$u*noF#I8;Z-V2YH$vR0gPCNjr|qhtwgB0sfAgu%cKRekr|zXcJ13nE%L#2*D>T??BpVlv`Ph1-mUH$-6OX2-7}c4zBNa7sBrdI|VS8Z9@~w4!x!50nxt|KOu+d8BB_(8N2S>noe^9Y3;D5s)C3F#BLq*3!V$MwjfE{cdQ~^GF>>N<bBd*rz2_F+pgR-6P72B^Az8)<NowJr&BMzN7Ni@s7@`7nUFqsL(Hs=$j7Qhnt?xDhd%HngfYpU`u(aTB!I%G?ta~Dx>KHHY1^@Axterh^P8sN`)#iHs(vf;Z(t~6{?#6-bT7^R9IAkI+e;7b8V(9?yde<ijOM5mBymN<Y}xmjd4_$YNHa%(Oh4pf~`-FLZjv&C6h86S&r#Sg)O<~O3iUrYMfQ;Z0^e&6sncEgFaZo%zl=4MYBW@#pqj-*(Qw#yTvc%_&8kvgCs`hlQS7cG0Lg>czzzY@H|nF45kQKd{^C$TfEZBH62-|tpH&+>w<Z|#S@+$T*(ny5!u_bn^j}!Cnu2;>cPzhmhPo@RVgT22G(wH{)_3i`I)DxUyO-xd<*CNH_RI5$@Wt>wk^|TUFuZlm4CO);M`phFLh<l3PAdAw7aoJGF(zLY~`Tht`i%eB761dIT@E|VGhNMs?QgtUbQdDc?TD3%REb3<^_!^Lrpzk&}9*kbrMl-B(BtTJ1RUPz(Qyp)sy8{q7A4GjRVun7;&zTD$W2@?`k6z$We4SptIGPiRS{%SAUPj*gV<A)g-tkVuUEnY^d)@jq5D(i$DLWS~psOYxV)(A=qz3I*X=S*xaT@fIV14upwvY>aYv`XwChigy>a>X0irk2zQ`=6nT9rB@2?dR`HG~3X&eZ%eOiBQ^!6n5<TFaI=^3mY+EGkE7o~-J7BUDe{P5s4Qu}eQ!%b!sZ*X!*wUe0*m!H3#1q?DCvkElyMM%e?N)$^F{tLy1`Tj%*0>lENi+)X)rJp{71CZj$+EWaKidk~u?qa!N?6OysC`W_42iHA9q$|u7X(n7;o(~2G(j;eFeyA1!<eE&%1-UBd|spk^;X{+A#pWuY$F~{95SZEs$j1w#AS0*GIkM+yku)<%vMfF^2T~>Xhef6?0rs+Q6TW+I_GAtjBGj7Xv(??-)`{5)Pk3+=f0F!--d`Yw>(K^NOxBCQmJIuY_N=lkxWBPMkTCmF_OWr8H-+_T16GT3@3XF43}!_CpV5rIh`bo&G)tXlwi28ulDNp*Lrn_SN7_zU*D^X9>3e1t3T~PrEu1(`{Q}9Zs`SI(5~V||NBFg8d#iGZK3Mb^=`7XPx7xuuI*4gPr=%ef)!s;3$Sob!P?Q@u_qU+Y{|l^6hM$H>lqg-Ta_;xa!EiauD)3}?o}ezRz$2dD`Xcetno<})>v3ro2OV<IUFxwVQtC6y1B-}TECQn^}M?_op;wxA<Fyk-Dt4=`Rbnwz{qTn<?;B5{%rq6h}=x`z59a$nLUDgpf|BeoUpmXLm`~t<c%91pKPm@x;)-}u<6zSSVd$Z@`b1-Cy_V#usaz2h7bXRNel~_Ipc33Y}Jb*=)|^JaCK<M!YfpcG5whSXk3=bREV<AB55L|mDm=6^K1@yYWvF6+=t_cB*96BgZM=(2HX&p7RwESU(kahakxj&51`l4=^7$=3UL|i;oaPmhLG7Ooa*)Il{~I@*Y;dGl-Jqb=+}ZK)XkwMXXzDst9#ohrJ_PwK2tgee})J@OKwE~G)t_II1v4O4ha!taF|;OQzJm0Q_8BSxJyo(&c=A<#W2N%9*7b1;8Qi<jW}$zi3H|U9l1T2%L7G%pZe#0Tg#k<9B88&$U#7QWmhqw2+WOlXXzCs0uA9&Gme<2S3pVp>)*&-dKGZ!Qn~=iu}})VW9j_$x&>(zEx0D~t>R~KmxxC&qaBS8=bF<bTA(GF>*zGGS$#(4S1Y(MU#T~GbvPO+PQH?V!dIf;g|^A;VaZYQlcVIF-Gs@9*X<QYDG&rD75iH5Qd@i_reId9=eh>IQ(b_6;~UM*Zz!wrG3KV%+*CU8Tu_6M^hjL$#oTPKy7HVR>E^67e-a~B8@eqnC*~+^-_IvzyfrIHQma{+rdip{-FGYTg74_&e8gld?t80ruT4p~59=qVBm?gGtaN9yvah0LzGxg<R?M=Y{~NF7CP1l`b|mqi(m121J2DioWaPX=PmD!IjElW$k)_D1DtVt&4Y!K9Wtq%zBy%n5h-9dQU7ylfCg`K88+Qo9!BSwXlw57%j7<T6&gkoAr}6~rdedW>zQ}6af$E3IIaiWEk;c+kQ+AWygk{DqU$2$wq+FnthT}3jSAJT3mgRa^m=WyYRE^L)7pk+bP{Zr|v|bHe^k=P(9H+v!<q2n%abgcFYpU2F`f~E}dY;Qa`<Fi^dY%jjK+o&ld{|^hP^%Ix*JRIv>`KH}A+F&@^^C21^@0gK-+7^|R1~bCa>(RrBcp%_0$-;}M(4A?l7qpHdWO-e{g_a2;NU_4H>rA4<apQWe4#oLycIrE6t-0V@K%|3SHu`cSiHobKqAi6WqCIU#ccW8{N*iLhfu7rLOmz!XozDZ%`p><s3X^)p%W{J6H}K`{)xR6AxKTnu-gsOy;h&F)UyAzZ?u)XtGfI1c$eh${C;gBE3(_J>5Lk$EgliD^f}^8B(Lz*V>K0^;bV6oCgXlVPkvzAvf3ZLdJ5c@b(Y6o3^JTGCUd~8fyq?0NKd(*rjnE(7+dZta?51{3o_N7aMO;TePl;7ypJtD(xGZY>b@g-N=b2C@-Gc(C{~DokHM^W_Sb7>UfwgPU5zN?no3#8wtxla`==K?`kUXD69GS>Y;<j~>06u#>x@-e`O<@EnCt6jow1-FyyiYAQsd*D+F}ugur0Q|+7>(W8c^qi<IpZ0hj`{VFyqI*JmdpM-@(s(hwg)Y2fC{C9b7cu!G|;70XyBbykB$Ecc|$*s5BOzNc};cj0Ea*9Oy@|4|ZVF<R_bkf8}HDDI2mNE1I;L1sx#nDYd$-`U0aSr6Nd!A&MofiRFeu5(Fu<Iq`KTI1zw#vUWowO72K!ZSRzJ!*-Joa9aXsBL7STIncv3<=e<IsW$*ubW;mfTc~gxsrj8+sytFr&P@$NLFGv{NagFuCJZe{&bqwD-6zcW6!XSN2blY#NcQ+$^qxo`JWv^<!(p|Ab{XhfFCz=EAi+T6BSkq%6RAQ)$3E_+xOGfa$|9G${<pHx=`P#1$TFJ4{{#Q+Jv+Dn_>S1+SVwB^7mZtO0g(||hDnchwmbH8MV>QnqOdqfZso^<oV$^W5P^k$X_neL%V-Qd24$dB#jO}Y0V`Y4m+j*S6EgsSAIa|7uNB!?m4c*DD&ek^u$z^=i+>$`+@54grUz_ARy6fh?4Sw8LT#LJUWpPp$FyiVAXrV@aDFDAQi+kN@NX$}#>IEuv|gO56l7<Sc3r`y`J&0mn9FJMN^JwbwEF#*tAC!IbqC_HA00pyk4OrVay<AgP6g-V#Qg%hi5<)*hJs7OUUsAgkJ<$oaWHe%A0rd}hT+^Z{@5K0gAhr0+2c-|`2fcupK!BhRgl=KLnYbhkWQe5E_B;QK*Iz#a)eFc;3n`X-v{!D`5TY?3ewAywVYo)a2|JdHtg5~ij&A??!?A>D)pv9LqnVztBxlzQCJGItCS!#O7t*Nfh!40M49Jh5Y|D`%+n|mL;?UPtc=>qmJku8IKt*X|LPRu9ST8LcJhrP$XSYUWToLwl&1WmvC^F97p)q;$S-aQE+Jtay}D>K&r*yXml=33nPsdCb_)bFSh4xt^AuxXF(R_aUQMoh-XzyiRA?o|*lR)?!zYu7V3z5)I<uqEC#4lD(Q>v_AY><bK)sn>jA6HkOkA-Otzm~fws%nZ1&JW_lW*tSWquKasQ=o>!}i0S+NG-ADDMFeCSOtAFemFn$BfOcHZUwIORcc|xL(8dBdiIm?L@dxNxizB#ZdzF$tH&mf(E`<Hvc%7q%8n<CD#Jpn>W}9q%Fhv8eE2$^!j+41fE4unlHE&y*GL#;pnv1DTr3~L6juK-sUgp@QCOh5ozQMZ-nR8BK_h)3giI9Z)s{<Gy>%NLU%w5o=>k91F#9ByzYJ<7ZoAV;V$oEzy6Ap$U8yL%Z~Ui?xHCZkU(()U2m8kH@LnB_i+?C15LYHUx`d$rI=k$jk(-x?^gFF(-9#WJ|`(ZAXc10iAW`(88WA&FVvRZ2*zVLJF<KMcui`+IOaMQ*rYm^lt?9SV|Jt^5KK-~aDLT9sV(Ey1n`VBwG;e)Mi$}Y0z>8El%;WnS78p+_tv)HM6f^<i}T)0IziwQDP)LKjzwP`idy+14HC^N1>(-ah`F-wGV(X0!c?hsOsAaFP}<Kh0_=Tx7E{Wr5~L<rGX+yFUciFcJw`$H$}7(Qu3!9U+)==!JjWfyc3%kuh3f)APjE+ZdbStbQ9$m@6oH}u;@9PXO!hdhunRe$cF7&3SI8ZOBBc*cX#q)es%725v;1%=1eBE6k460FXly&5vJiA#r*f%Y{Y^wFE4N6tUo?@s(nPM7Za34gb|zJM14DDI76h7uX2BHMENVel3PDeSW_p2U2(@Nm&rOlDu|^T(&OM?+THenz{5Z~PE4zW1d72UOqEkG62MR$EsK>fNvv}ZEf}m>47>dl*lIP(vps`r7Yj_2d(ez&B7t;)?AT+>b9GXqAm_w>YaF-dpBy)fxJGlpPEaJ0kr~t6X4ZinIMh|c{L;yLi@_T7~Aw|=3`aqWc!Jp8>MOO?B?l@yZ_4*-SErd*<N|5;HAc86GO0hO5Vg8crB)=oRpxK2ex&oI^i-8xZL5@?H6UB{avQRL@uPEjeYZL8Y5z!6O67f2@-z9sneIC0tsU{+w_K0vj8?|*ZX-KK3uV@52gcFD+l}+%4*0=dD+sc+!Q0tN$0sH0b^|wDi?9aFH{I>sm8{xMR{(Ixkx1o3&<j?b`|2Tj85BPZVns=LT<+8u&pP$H)c$=u-(x3kP-R9$cQS&yiula0z^3PX&_WwTv>)ki{(|@Etn-~8{5WF=Y=+F68>Cf?9_liFkzq=RxUJ|a<pbcaG_0~`Jdg-&xm3PaFSKqz;(_jA?8>z6CPSaq2l1kWq(YxdC<+G)V7?#EN^3S@Kh3IPvp^h7vc<7P&>Xc~NSV<V!Q4j<LC4{Aj<EF-F{X@2{tqkHh@?uL?A=oe0pcrQVib|;!426hV{xj~MXn*?q#k;CEzU0r#^H<Zm-ugpEiB;hQ-0~xm_LyC~ow-?lDT&N9M5PU#Lv*JkrYTHJLpK{ntICb9EG`nTI=k|6FLs0Fk}C60oaDgAizFv!wHVT9ygLHsn)pbxYqkqsL+G1y;Fa~^k5{P9()nHZE62F`VdGcN?g))_<7J#b6#LUHU(uiAize;6_^vQjg!W*xiiQ-fq@zYwR%6H3&lrq%pcJ4g{RxXy-qP=-d{o(6v!7>w&VN=nKJxUt&Q-U5Is5pPGdsIlGnGM4wj8e>YY=hGZqS|I?A7mb&)v)XfLj;*!qKP<%``t1`H;>Y&EmeU+)g!rrt_c8bj|bEeVG+DZGs#BDUdAXJ~jPY-A}KK|HjXbbL{E~=ZB5IEH1|1ysv9-m1?Aa{b*di8yD9zzCQjUu+<Y6cJ@V+!!`|q$^Y5TH6Iy&Z2<kn6Pd5vkwwE@yy9nz*Ufn#%AfA6s__R<Zi{Xx{I_ZAV$149P>GGdG=MZD^w!1Gg8^<(CwM?{;>cnHL~APOsB+_E6_F#itHSmKEB?EIE+RVc0j0|oe}8=NKN9Eh1E33!u1Y79O#7M`P54dOqV2(L)Yss*k*Iib=y$AL^^RoXBwY=6(Z@sBMDOom={FBn2<hqmtPX+X4c?zvw*=_N_1wEw_cH%Q8=MZ#koT59g^JJCH9sKwB;Vo>NcX^6&z{h^W>pQ4GmZ5stdj8GR0X0`rOG<u;w51KF_Z!h#cDX1))(rQ1g4SC9>B7lEfp}yH240I6LdpShS1@;9Qev`s8#@lp>x}#PE6Djw**OrCA5{6nvS}B)CtJfb&LcIv(K>}TuTK%$^!`21Nm0m@s75sF%nahv3Ef{8fZD%5@G2`^c94c2VypV*NzLdW=GtLofbnv)p13ZH)+_7ozm&=SoL>9c>Oa(ORW2jsH!coB=r?}@aCH07deCE7g<qWpCuJNSw{qy9{I9#hA>wGbHeryBlwE&kY;T0lq6VnL86t6KO_}Vu7q}bEA-+rTIn4NXYc72QWD6%o&M^Ldhm`^+rAJaxuzf$(Nd#&Fgv))3QPubG%{D!gGZ4-!Q4>y_ta@e+p<7#Z2e{r&>-1es|vGENWAi~w1J1E#+Vdy9oQ7wQX3xVb+=K-0ZcUCOOOuZxvBh@vkGyXSBQhrH&O_J%y*K%EQtSF6ZX?ri~r24u_WTixr8pTet!!~(o9&At3Z-6J@bRuf)0V2gaVQng$!D%qY%n~(XtO2^0SzXTNda?+W%T&8B!ygup~p#Aqy8eWLp7A#0?lGIEhJ-Z8%Y8h>{(<5e1EKUFAEJbys;V4Cn!Gi7UC(BwH;t$s!RY_d=BX;;UF516dxsnx=R?$-s-^ap=igVPg*?zu7D}^@ebj;*puMaIXFaaA&kG%!ag!X%I7!t@c9h=$jS{4jS)0u{)R?tu1dy1Y`hoQCza5ZQ-6GS|TTdMSYJIc+4x!9jy~@{B48*N5e`53fLw|iJaIZ$Vz=jXqF=9onogRvR18lV+!MAKVy8{|Fv)0`_dLJoM+pg%EQTT0n?LU5{;(1Wh{{QoKeBiFMFS;?jf978jL(@(Z}uJXQ&$rvE)!%p$HRS3#r4DO}uP{qKO_rLgGRAxdz&DE9j4>>`uOg17s}FvqD5jHV0h|r}3n2sG-_7#&9SiE-GnF4X)~p>d+ZQQqF*$t7e9+iDVItGs_7!n%W@MpSM5C{dceCSA4=?4pN-EA@NBr|4jjUb#B%Wbt&<wU7b?$;vi&u!fXv2su~YUKs<FxrKX^&gH|$npBjK^jiv<vEpoItcTMP1&@Y}2PuP<t(-}=>K3^BD4=M@{JL-OJun1+Pdm%o_q0wro2QBqN=uqU_nsIZMRH*07Y7PBKdMPwtEL1*7+oz`Kdrh%wqJFq+<rm_w``idFv9NR@{sinNfc=kHT5#_kiW1=0CaK5S7xH?7PkVGpiM%{74j^0`4CtG!Jv-wtv5a{o-b?h$4}=zPDX+yI2Z8beDO^RMqTwIAGaM;Wux$=b&OBtPNN<OwE;N@fTrB=x?A)Z2#WTU#PH15O5ABYAUVawI8C?omdhe}iUNnIErDg^*U$&k@DvkBZY&J(DPR!@|0TZv-tM^qX@?hTD()lfWj$v)x6ZxD}q7o#qlAzP0N0UV`%1{107%py*;8{M;$^D9nFW)o=XB>ldRd21w<|U%PqYDK9FF)mKV<IBupe>$)1SOiU`2T(~6HYnRPJEGT_Mm&CXYGx0%AEg3qOV48YWa4fb>!M`k`yZW|LCmngRXdQ?Z)D7Ej*1d6SZad>BBYFN94(mzl$SCG>m<XQ)_$ejoFP-VIag8PdG0?NrPAb+U0{LT0~AzHa74N5{oK2<lbjB5fP<}$)2foQ#vhNlFVzyG6b$@D#;gYt5IFPq&vcx*ms4EQZlJV0t^Le=SD($CAw?f_}=fWaZ^d}sxjX9kt*K9m#L)RxWJ@B^OmgK7IDDE^it*s=5tManI<N%*j2qc-GF)QKB2w)?>}T$y=0i4I*l)O)sY3s<t>%G?2T=#uB@9FZtSfrw=})U(I^Wr+g>eJR)>Q>Z(U+|B3}MZg4$@Eq*$^=(k<3S(c`V<t<JVu`ayM=p{8qUsYqN^igDbm*}Y0Vi}^lFXIHH3Ju7^0$LorX#!^Qw;+Iacz>J-XB8B5M!1isc*p3r3Na`|7ge3TL|1z4K)o0yX!#`<r?auk{eaoso4SPUusruxxX^XH=eXi=$<v&-(sio%5hJkCGg|lHzhNFa?6x=WYU0rd-KOb;pGf0fnA0OCpznh86^ypi@^OLeneXRZ*(umHrc`N(=_3pEdl=t0Z2uJ4FBe&8WCL|ktDKVIT?<C^Rw9>W;Qk%sLcO6S|U8^o-d|l6F^4`t=VLrd7ctY<~fyIQ!lFaY&Ija4hPG-nKck;F{2NE$3ApHR8X_7v6uR0T0098z*zGz?w%4`!8PT#9yUerxliFH8g2#yq)2=Tn|<gvf?bU5z=H7JskbON*Vew$QB^~Y>S?{S8scLV$Ey1JBpL*a{9(>>mj{tRwBUjLp41%D@bwG(`@zA%A@zi5r|kvzPo7x%`qU$KS~8_CFboEX71=FgxFsR5;aB_B^RxkX0P@ap;dH&DCGwh+B~c^p=S^B0);JQsQ<Y1mZX$fZawn+?*rN#U6>aKpFIA4%#KR~WlizD-_w)XWUB<1(SAFp>aPNP(fo>oum09}pLl|FX2fN+`S@Kx4pO88vgF)JT4j3j7Jo9e_BHUr{HwswG#;0HlXhX=C+u+$p-RYtmCN&&QOHi{50kQ3i8XXAWeyO5Q9(|NlPIMCeNsVLKBPLbg7tw-aMiJ6i(2$lU}28`9VrCN)j(%P-Lzi*`$ST&jJ#NiCBOGgU)Nudes>{F%e8jC>{{m*sOfmu&;~C#RUglL5D&7q|(moHMF=NghZh-n3q&0yKIZR)1cJsJb%N?(%PH>2r$~#yKC7_iiNrc7BrUnfW%s6mnb<ls0kEQh1u&QaAUA?6X$1^46now>h4$e391$xLIqUlawwGPGj4pRp9OX%+-{8H-7Z<b6)%u%{(-B#;(W3_bwVDG4Q<&=^!wNSYF*IojNH6$)(h6A^na!w1rCDkA&_s8Y(yQ%qudoN7(ejLFMe6@Ug<~52>9wKC7YfRTY@Q=uTKjNDCgE1fqwNQ-#2|xY?e@1RDl%N8{COc*aU@yJ1u}dAZ)PIVTu_&mNNT7)mSHp|9R#T6Qe(WXtdFu@ZI#HPaltq!AiRo57)S_jzJE9n-OF)-iHM3GHCH2$6y!yoeA-dmQ*J(yY06gD$(4V3>dGtX|cSM}3%a8N`3&#WFPbhVGH$^uWObaRKK{etsvkUQwf%u@DqH-Ce%XBWV_$-E_PMfg5Qx{fc_q4qGmrwS&=-!I6CAb^x_cbn-iGj|}kIQzfwrwu3ppuevYofslT|fzJhL2R1LVcQ*X5=8=8r{QWbYNB(qrlv;&*pa0SOdM~2;ioc9MjkllqFQm09rJ~-0RyTjpC-TK>)x59WhD;Lq>5eW)G^Ygq1bK!T7<8blq9bzdS%SHD<>VQ>XWA~IH<ml3I`GNdt1bUM^R&87QR^pB!GV;FsX7|5osd7cDW6PGh|~vXNxHgHZ}TqN!5fC9?;9G+hFVIjTdAV#`4i(%=#;6|>$VXWwwB6}4zR=cE<Y&N;`gTEodW}=@c81Io5CtM`TFn0-i1y+yvvz_Ym=t0^aVOrPXu+y<IiElRb{8Di6%DUC8vUSQ8W}oa=8q9rW(mH>z9~bR%8;M3rir!GLK1GB)9L9_D8NvDU|)vO>X1^c<rNzksm6dC%%UARDnt{i-dgt-VH2l2{|>8<Js~`^wgP<fDe>o&qIDJ8<d=4EcQpyxkEy2B3ss}iqUAqB*Md*(&daWvt+VJ-lGm#ANK;>jgUa{RUP4MiIHUU4)jPW6vw^9<?-liah))Afkc@2(~g#9!-5A}vW0b_G9R0HXq5cw`@&Y?gG7p(YK}k*>7d`86dd&EI%OoQ65UHpGvD>EexO%8y2Kk=kU-{)I}>D@{Nd3V-URhxWy{^Wf|_V3fCo-fFV5M<m<s9n<&j=-LnHl0xy9leJ5N?A&mL1U<ao4(!~G@^RkM;P7{%Es;?u}07QtT&`>D*GvviJSoe-0fJTV`$Qqfh!PZTVY*O_11rgAo_^NJRbu^BvI=IjmCSeOT0-$?lzymsC=c*#ysT+xQ<uTT>N$rU_ZRs$zHFzG742KUu+BcPd!{HpMue1s^6)Tb|va(1fGPEU2y^09YR9G03X_~97ktSS+FasF`t2JVMY8)ShjUsF=zPK0ADt~g8R<%2=3QZvx0K^oTg=;!A{tEe3Y=D~)824N-hruir^gYxrX)RF_5rYb=Jb}ms6<q^aU`iUzti1kUzp_C6opgK$pU^7fImnd$picAoD2HwQTVz^pyh3NqXS3t-{$89QuLCknzB$*WcnYSiLYv>wR<fK9gB`|BG0u*#r*<Ajolf0yI_wQ&)4y0A9p)je5&{1S^*HIv*<-uELNeN$!Pk!->*siU-kr&bmXc|XxJeLGUb&#eM-xmlfI--k$>uEFr8x!$|cnL@v(3A)xNpzS@<SN67(*!WEWd60M)I)L#$S8I_#wb#;<L^;0;UG`km-Pew)<}s&sbNLEOBhQW0pZ?TYL~G{V@z&5#!nKm@Hu2nqFbCt7iroia8QwBG_E$Dp&T4db4xg_vPr@_8Iv3qLfZw=6>s!-gVCB9pB6970EziF11K_B#3VzB-rBfVaul25;1osAq^Yol;o#I**fzc;%`aoQ2~ohE;7zsGKJI4`9i_EMfoDN=fG~tlTVufkK~*8tjnqRRHx@^oMyH7ST72$I?!x&ZmDP;FVIyd`7$>VjDg$Ft6Eb7LrxExWBajLj-S`os>oKxl-Ki&&$1IE-KUk(l;R5ng$U6QTV^?t#O%J@p&wf;`oqidETb74<zlhZpC;K>t>%n%JYIzrNCJ;8i!r29kQMVr-{ZcDUrAZ5&?R%%6GY#LFrJO!);e9C-jaO2#49@tD{EYADTy|~N5Tccn%t@AB@a#t1H0x$R{WKwkTKc6|h-txjwP-9Ik&qQvC~GI!@`fG#7r8BY#qO|2+@V|?ylta?cQVYuKxu0%<HIZrW-y}l96^KWH%ApGuqWm~vCr0SYeiaMNF0m9avbj@d=#iqiVYX^WLxV;U~Nl`8u}opMZQ*c#T7a|VIc0Z$8P6j85Fkz^@%%wX!A9@j@%@5G)yq={f=KDjG{yzy`3|4CRn>+5z)&=czeRxn_S&-|GE_1`i1JR(u92pLSQ_HBkFbO9cszVBgf!S+0)41v*&Hq4q_k2(LIiX6`@7V4U$Ct(hLrf6GglEI(!WyE<90zP5Uhe?@??&4<?MVGc^;2m{#*HOeNy!JQ@zbTfN2|a>Tjk@VG)X$SbLL^s`E*OWv|J>%56d7zcI^;DGF;t(gpL$+JwFNRs3^5=8Qq`zU`mlwOlfuk$bnLIjVRc`Ny|Jhe$TS<-b@Gj|7uV8OjG%Ro>?_(q8aM5No-Wf_oS=>D!wF|aCfo?j4dOvp-2Sf&^{Qr_)fnO|5jO`!Zj`=b1UqqZ_cvzpmcbNs9?Sq5LyrrKZLm&C{QECVv$Q=)-}%izDQ=)IpLh!R@#^Abe$e_HJVD2RMPLB@Q6_cMYhE{K(jeg4@1(AYeZG!~T^C&dV?zf^TCBj#ReD-I~Pfz)8y^6yX%?3h0H1R}sX^c8`aCQOP%t!GJ!mJ3If{AtHbb$+ppVsA6n!%%+uV$ashk7$R?UOIa`P((WLRI3DSWmv$AGX&!o1fY@V(@H`U4a<pZ-Yn8k1J^x^B;W;2)LCkrun75Kwb`v}sE;0j_7jy@*fM7!?PPIT_FSp|&r9>2GB=Mz`X)0&`5WHXPuZYE8`P9!=VXRDzJg856t<To*NR2hN@-_kYX-Ijbhj;0o=KZ$ED<RBm)Ci2i4sF$R$XL?;<+Uvf+AsFL|PDoNt~G>vY$U?iG-gLwv5vX_L1Ez+h@%X<NggJontr4Zjv|@-&>oRAnm*<L3WJb-W&DoWOoAX&Z;)oFucIx+!a+K5ZrC8Jru-hXXZvK%hfrcQ6TxxXK_OOuc|*1;=AC##|8UHu*90uZTV4bn8i#Xb_VttHpGFoEHrzH&QUPV>R7->hqz@8n%Yiqomw`81<Qtx-bc(sx}ECRh@|pcYuiv#kajx^Up6z8BE=LNRJwUIgxN-aGVqU3i)5aH=?q79JFurFM7Md4$*Ar5k)FV3td5PKvH(NWz^<{VMT4cPY9QPy$m_9gBRfVwcjCvCzVl%vsRAV&xN}ujd?bl0L-a<H+<~1LCDw~>*{1H>KnW87gw#50!9;MjQgu%4sd>N1=4>n{P)iX*5iM+0)i#JQ)JrNy|7UYyO%BaSUjieUtae)j^l*g-u@C(5*Oi0>z4?k(w<{=WBRF+A#_3pKJGDNounnmbVo+8nRO#L@kd`pox}Jc;!JEsYh#;+zj!T}5rf6PrI|DHm$?-Ly_=#vnVJ9gc;9`-yQ$5YA6DAmBWQcwMBukhGXrCmxIh;u5%W(V@jJGUOH@FYTn#UC$J&+|0W_o_{A(%M;<>emR@tsyaMD45sPeOi|{vh(KKdy#%{PHhK0%e|C_0=kIm=PLQ1W35Br|fgK_B+!i%@Z1>&k>{G+3yqJJ3vh|@{uJ7D|fh6xE4((I5)ChjplJ)_JC^IJ`xp%wua#ugfh6pkZ+_cHTY&ly3`E@6}8Fev%Ar);4HudP*5s;0WUTN!rKlgZL}btWLruDiiNQDP3eorZnbkAJ6jI8L8PaLf8skmPTOgadWrhn0ki?9hr`ogcxGe6?IVxPD!U_JfB-v3^+4v_SINeP8m?V6+#Z-5;l)4j9iKgZePv+!4;q+mHZbjz1Cwp`fs-bFS^bBvRxx4Hq^4m)-oK^mDJ_!+q+_Ovh4#U<S5HpgQFNlEsMQt&r=HK=_$e@^*kYjXi2U^0S^nDX>7W4)k4>lUB%@30XFz>I<~{g=<BIUt5?4<$M34u9Rb~;;f$X?5Y0--2p^&22Ol3)=y)k`1<+i2VO&x9RD!#ynLM%DRf`p_<)uf?CXsyX&m5PF-+=O)Esc?05ut77j8CRO-QFwAiTLsWB>b)V~D;5v#)}DF;`J3yq8<G;8T)4`_|4*-Ai_Zga7q(0sg-sY9;XZ6c7*C-dT)t_$VJ8MQZ0FUus`l$CcNo0NG>z2}*bk!;GCgA!TNcW4O)}E)8PU6^s7>Vy5}K|`?451b8@D{eAp8&Ds<k!m`$>RK8Re4W?CFv+mrP~=?umAco2N@BC{&yisON79qHmuPv5p;^(=i;S6v`PEg!h*H^;1r_WQaMQwL90`<H?Hx=?FPXGXcOjG1gNgHWa=i%$vB73Jjv9E?IL!)))y(Z>e!X#{KxDrUW?|mJ4ZpQ?lTaB^+-s6ta9agm@ANWwVE#E_hP^;!E*E55zZTf9?bqHP3{4Q}w0L-+6h@gy!7=!JHJAJqRmBFjbVRjXp9ZgExgUra4)9a0gI?+z|h0{1a;RK@noZzVN7z=$Y(LEIAN`j=6t_3*dT3+L&nxGSC~a%6~2FDUPJTs1`p0PS__Wgo7{mHIFkpo1qkwt|e!bFNrch6}^sp!hZ(KTMpunnK3z)I%H>ZHU{NH2or`)96BZvRUY0s>tHAlw%t3fc6L|g;9`3quR<bb8)ljQe~y!msunS^N=<BydJfIMKNv3o>U{^32FgSAllkO#7)z+O4^-?4s7!w$LW6|Wm57hQR~*^u%P?JU8Rr9dvvCsSJwSs27Kmm~jtT)7HpK4Qq%6O1f;5F!DE_S%HFa1c?F*!>FZ((K8L`$5w`!>QtcI3KB2$yh^~8_A6r%-jCj}v9Loiuc%#t8{341&sgJMNIr|A{FK+26PZ5|Xd@qX&@2vi28RB7q-NNmOlCQLpxdnhp>v4fV|R5W<6W8fgaofUGWV@r2sr><ePe0Wqktm}hzKXR^jW8(+6yS5#rfl9cC<`YDEb-U1%bL{%aS8!xC*kqBpT2?DlEV)UD@8kmbU9B9%XKne&1M(yHmxw+z)nAZZA@Hi%!4@oGwc<uG0EJy0eEj=U-h8T-wbr}|L$r~jw#sv@MJ*}SsJyO2o)KZFRXOl7t$CXNeWQ)#B-I?RBYMQ)vO7?;<QPp|k&&@xo@N8(Ab%E0TXObT{to{47H!>FTKyxnOb0w`rh~ly{alDt=@Kp{yVex(;ZWnxh*Ws6$6Lg%gr8Too&9)-o7%iSf^bF+C(*zrIP}reiG&MOW28q`6cI1=6aisNK=xc{hD6aM9W>_-+9W-Np-{oY0?j+chS0S{0-=^-WDf2fe)-90X#&h>*5hloBuh|u%f2^46A1S;w+~5^+A?_YJ)1{dK|3bqItc1SHU~XiH~?}ysTOly_V?ra-fyFchxE#8V12U7u?;^*`%@(6@$T<rvt1q*>Y{|Ejz7mx`^(A{NTm~OLO87bz&{Eq*x~E*ef`K+YmkCqVd)vMY9_KhN<VtA)f@`tT9krwS8>M-obO0Ky$>Y53Guyw<@}mx!zQpqWSSl0%HubF8|&{cUg>525_!2rFZ1ufTKT>T!0*Ct%P@gG$azNg8;m!~o5Aps2@VAyOdIOQ8{q;W&54<}q3CZGDYqQqL<U4&14gYh3OyF!p=0&hmF+B5qSC`>-NAU!RG8hBhG-N)4seb(h3Zi)%y|R#Od%B<w{$A7orHT;P>Vchk-br`G<rtR#SEYo4-O^p$v%`eB$Yg9j!)Ll5R1TEt&e*(_KkQ<X+a0Cg7?WO%^0a|>x-tIhzQf4t^QrqbW#b%n}66L0IwahvovRI31{-}KTBjPo$Iu5b?>3q(K^#{-4H-ag|KG4-IYVa)yuCTTy^g?u87s>>})pR!AQbv0lbd-l=oH_&sTatBONeXh({QX)q?xxAiW0-NzLAbn(yZCeaJInfOug;$Rx)DD<AL!bg!{42ZtSI^ot#hn)jm1%pb4w=H3w_&*CuF`yH8L#(WyDB!7jB8jh^VKEx^*{`5{e^`d*ielGv($KS9mg+FO-)Ykc*cqKp2F<XF;wse|SvsUujZF&hh(V@J~!vmRPZ#~KjMwpa9oXM)ql1gGO=!8;;rKJ<pUzm5O7P3w~Pvu8VCx>iwDoV|i-S%Bkb`k|pKF?`@j<1`86T}YHxU>%HTZ$)t^oHH&?|ma_!IBoe2Thn|_Q}H&(!D_=4*y{FYp#C8Bk&JwRd~mt=D+rld8P7msMKn~{oxV3DiE%6F+Nlq+=2Z**z$~0x5Rd#&$2~gd}SvE=|^i-aWIVFu4o@HvmWz{8+y#O(2MGlbE7U37B*n1Tt#2M#MkLRiLaAdq)^jp@^Tt^IZhpNsyNE%PQK3j;_K8`eVu#&hGKGb-pkQxMTz#5m(#q^%kh}6y+@PznTx|dYWM-y{hRnQ=OzTh@VRprC*5#y<lofvZ)}-)abO57NdJb+cA~qhY3J&>i(~mSdO2a_hNWWKbzcXYFL-XB_H`IS$k%DJuXDxGfe8AGU7TnA8?VpGnfv_y&2N8Ois@IC;5bnyB{=XHh=t5ie32wvBTY~ab{ll$TCj_{ViAL5CDEkQYg2-ghwUtqFKkjw-8QK*IHR8nsB?}hlV?hBLZi~fVGg=whKoEOKrin&pJo3i^1o~m>WSQ-mY8KFr9NXhU^-2+UR|9+=n`*S;E^@w@_G`9GY7i?_?0u4vlX4eLiq+Ii{%U{e`Y6axlCDMMn)E^#tBY9upvTkYGDF%L<vz+y-BEY)mr0GOWe}acpy<CY(FpE(67CTkiChJy-8%f{rNV+ZzKFR!f*0pAO5F*(;oY-$T+?I`6fK}COq~gJoa~&@L2k!!egUUSa^k0*mqZT3^y{oL~_gs7~&|z0^zYkAb`PuXiUtY94$zem+pdi&WI%-TN=PJbLpwzM&YqgpizGI=d;3H)u>e#O=(Q8jKX6AkcIxH(irn$*9FY396Z<bYEAyicvs7n%#YE<KXVJdx+*_Lx<NJxI;MOQvYz4EzcWR*LXj|Oq~VbE{H_=BV}%s>{388yk<$r9I$XY#yo1V-k*$;Ps54PCccGMaE}0e=vSG7f_s*SP`LnMq{&aI~FkGiqjl4CL*(^rQVMNQ?M=n*zE+xn2dP@tvv85W;ncmn{d9Aq+*Q?)6)d!x|O?q9U<k-31n6sVbs_4`Q-^;TfoW#cJivxVQ;N=L9zg#*0<z>4kZ|a8X*vloyWLxx$np(ySo*y%xTJw9KzvwQ+#^%@Ho)iYV@veVDgU#%GcxH&E)3#4Zh+S72JA1L*?@}ksi-GW}y4bB(=Fg>odaK|rnIF$zEUy&a?Q>nR|NW(~ZPYh_1lhEt=*%w;1cL-t5s0?Sub{D#eB++DWoHT?_RaNpA%w}J3`!im07c}0GCj&D^%9y&pnM6>w$h6vPaJB3g@Qt0_W}tPbR6mu6??Y$<S)S9rWm5?K3xOWS9HSY3TWIFsPhDn#;vKYH#^KjvTM%L>70=*1Xfe*<GQ?w`a&E^sI3~poOmC!qmid5mf=Fjzzpwg!2YTLr`?Q`L)``#05r+Xq1Rr%QY*5`InPHyp2M+O+$>Sz6Cm6eK18Tau26q|Va8U<@8b3Qa%<&wP%Uj|=XZuat>yixBDJJi5hsmfKQbB~^85eIhft>9-zYV1apO0INLWSPkP<g~iHw0v@j6-hzL3S0wwq=W79cxtOLaGA&=Da$np7Ej#7pC;pk+nH?9q(8^HuAwNsve}Om#-iCN%V{h?xdrNa`d77@G*-^92|yh8Fr3QD5Y_6ozvtFg`S+By>e*WVO^8>5I<D>N&<iiH!80x9a!HSAcm30`0oW7(`AJJWrIR9$ibssy*O<{XrarBN<^Jk%>XthC>ian>|*fA-NZJg<v@^FFg+f3~PS~abz*E2m;1uGfHn94Rh>`{|~AqfVQ0UBBGw13%j*lziQN98yXM{i-K9R^V39*DRF`+HjK!2ih2wWm}vQncGkFH{nlIJ>*Q>U<`j_#Q2L=MRE4oHn(f4x;>8_PiQ~FI*=G@{9c}T8@6bz*lEa1D`L3?;Z&PZhb(0jxw8%*clN1EUA~F;Wg3y2|;-<ooDF7M(K9~$gysi4@$@<k6$-h<6C7P}C14H5VxkXOVh0nUef9WRlR?GV+Vy?WrHT9_#`Ys&yL3FT5AvX;{Q`UxzbAJ#~pEawS2+)M4wGM-%CVckR7$xc6mbcsut#EWU9xK9UEAf{`t?eV3f{oh=&Eb195P|fa!sC|yd^akG6I*z46vM$sb_Z+_sTwsQfp5v*lJ0>Di-oTf7U7<Q6OF?kt(8ah<O`1CIx|dA8}g>r6Z(g06doTA)x>2QLJz!Pz5p%kVhw-mV}gcc>rC}&0Ub*2Tt>(Q=L|X|8%Xl6r{%?*NzfU3h(4&Hhxk^CBY<coL>I{L5!rLdW<^1VC`VO|5a_7HlrtD}@1KPZ1;UY>q{gNW89uh&m8N}mOBrZLgnmLTJr5efH6Np>1e|uaY!rq<Sl0w&{*in{9?70gDhY0QZGs2|wuo|x+)FH=sj?BgCux46^72Mc>@NsBYJZ5O<>uU=$eIwr`Uz<~>i_dYbZ@gKHwyM_Ia}+SGglh8=~4r?waE*CMU%cg*S&4jNcE)jtv{2#mG1I2_1ht7o}2V#EInKaB<D-rTW>O$v54Ldw?%J-du!nR*#w+iSc%@22FU(-#oHV|BA`C@<P!CBxm!a>H)65p%&h|<qwy)lTTrX0<8dZ>yI03^#3qQLt0j6{6mMzl&S+@T72R7b(C$L__OmHD<}dwguZaHfIC9_{dqw|uPGuM-(n!<S;c@xa)H4{bR|?8Ko5>USfYh;RiHXR_eo|D33c;tCbqf7y`+7!B17hvUqD<r2Rg~||850d*<m^^6KaHa-j<Nqas&-`SGXz)2Nwp%tfSZ_9txYB(SU-Kp4g|vLV0saL<O$_Y58`2}7>h>D>BXcTbhg#@(=o>EPI*uT85#i-nrO=_XoH#FHD*$l9;Vdp$m=>CK)|NG8<Ln+)dy#C7NefGb&$AWQ7PGz@e~|`zXGnb#x*}8S>uCP((<Fz)G!(c%#i`k5mcQ(e=H6%0%>cc<q}*bn5S0aP-}2En*pj37O7@I*-z*xi9`q<N`7}|Ay0nzk31fGO3x3vDzEmFodFK__d!2RwWW=8GTE2H4ce0Ds_-C3u5u5iA?FBNVhTmt_!HJC5qjZy9v1Jge?|M3EnH_+C&Fp-i#z0=teZVmM*a-O>dG3s?O(oB%gbO`4uKu@p`Q-GXOSC=hPuV=wAvyO<%xE)na>W1g4!g4GvNQ*Z&9(;PkWQ+<Ie6x*_Z&}e@0ktOH&^V&3q+YlC0A|spHr(CQ~pa#cOJRE#fKl5s;J_O;5WZLEbCst#X~X^<0&1wWvy-5qadn`#@0v6Tyl`{>jFNrjR{{(thX3iB@vUB4moa8Z2?ybqjs0F}!MnA*YWoKu-J5&7|ml{=>!7@8PRV{aI(TDZA+{v@(^&a@Es~T9xuwB*K|DYSGZ8`P^Z)ZK&!n>(wd=xBbB5XDwQugX-OxS~{Nj+M*=Vb&y%$n8Ta_#Cp+0(oOv^jlz{`8QAhI5DMfcANql*KR5Mf!3o~^J9B*PvyGncJzB{Rf8y1nK5`0Nj`~t#6{Aj%=>_d^H%47D^&IsSOe<8rV<S@e#lTl`8F$0Qz=HzwT&7;34aYujr`S<D3e@KSw~V?q!&q0`eR+i~aR^nRNPjurlPJ9_Bb}}N;qN@ze0b*VhqhYEb8gIC9KHQeynQpL$%Sqb^N1G?KL~##yya%HtEI&y-%YWrb(&FC>iOh3+l3;<6y)=V3mdET&@UwJX%9Jmz19O=s8P_Cy!<9;tHZh*-u}Ae8oK1P#zw2_CaY_r@QF_qPpn=z{M}@JakiGCfJvc2G`cxI<+4pRaBxPd2bXk|=BTO8cH#4PCHFD+`Rj;;dnfv9ri*qY4pPXrxwOyo$Tj3JS9*=I)qckR06@WK@%G~%wYi*!;>S-5f6~j5;ph>wV*X~I#w%JaNfxNqhs~;LRu-FP2VEkaLo}<A5AJC-dM{P!5I0N*m+VR8*lY&Vjg|K2W^1$6x}2hsGvza%mL|H9ktbJ6UNI5f<swR@8f@<mq#24^GU1TKYTx^o?f^C7LYQYOyg#;hCMyVZ@u^3*S9G5IVGx9i);oW0&4txga;ww#tH1C8j#iWwHWe?diJy5?jwVjrN*Tr&7t#EgV*|W{TrpyrflCj+wh#zv7_$#-HY6t^0W2QlUYmNI)8=P7)cF=th(<i+DILY~1r>R)#8{MK>l|q~D-){()hO{+ZXg&ZT1f$2vEIOLvOE}|R$4ctAISe2bVmm?HFE7AnDh)%TJzli9VrP&*5sFK$$_6w*YkG#0Wq6`{bQ;ym?TG3i)C}dEo?wW$J*ttS}~GQkO>XZzx}C=x+lxx+@e#L<aHLE>aE}0qPt?z{Wr1bEoSbwV$q>~_?$&|1>BHcYtd(QjIgBeVOHkc*Txn)5toP0?QX-){BPgx<edk2S0^vMIGenx`h}OdBN2s{^U3QMna5`)FS9-$!yO@Uf+f!_(*NMe3lmmz=C+r<h)vs3<)|pAR4<yjLG9~^4|cN_+cqIS{PKxuTN~$KAo*0ZX$z0q@w1<L&i)4<E^mLBHpHgKj#5+WxJf}!I^=RX$rK}|sw31VyvTvcSV<No?u;tLidKXBR86tZ73H}w7!)~o+#E4fR%_))5>>BASJ+2n2Jm3;Gz_#MeJElzZ13}=o)G0s_8#geg*EP&M8dK(K<ObzojNMFt;T6WN`Kxf7E@apJ_`A(mb{Ck!Rw_sS;3D%T3eLU)OmK2n<k5Vq)XH*N3jM$sV}*U6{~z$QVnS7S(z{7u28!$>cx9*rp<s4wx*aET#@B=|K^80VfYu|F_Z&F(3S;2Q7Y>B-<~edP~9_tXqna{Qm9fkjiOGZs?#3YD0LW`4(zeahgD>z#uJ9i1GXEhT~L)S5FCN=9w=cJI>En4Wyh^qhNhDqVRY0+z%$=Syi%w!5(+q~G^`5DA{0!P$W$Y_JMxi3tY|4PuJwqVf=gMo#GU6sKMsK#Vnu0n%&4Ru4+;TLGL*GFYPKnat`qJjTZe7F^1iAEIYBBeA%~cUeaJssQG?JG%Fpmu_2?S$^uFU`l)fApX+=J~r&{BNLUT<dwM!lG7!Q%mYA&vsKV5kV{^dP_sW-6Az&6&H8gl0oNr}2bx;wC=V<$ukC{mQmW9q#nw>aI<p1xzlWS@@b3WX~f1<}JMrAj46sO9)4Up~d0TFVGy=cH3<9Kxu^8BX0xdpkn!5K9Z{7n~_QsV1r0X64!-@0rx79)f!yjf%|Z!D(eF0#uVsK_XSxKr|C9=lqI}Zav8usyt8IRVBhHiA6+cI5_ezb0&hep{gZ<C~*<OIwQBOu%l<6hXp{QD*XIQrLXS5lG?=39%M@?YvsUmN%EGE?nC3PiVwul0kaomMgw+o5H8bs-Et@297oUtCi<rKo2?K7!560FY?B{HB}!(*_nqIYkl#o~y1`@aVGj@Rr2Q_^_PSC`AQp1y{O?1pA>6P1HW>?LW7@9T*`V<A14MH8^8`5{KO{RzO<k%Q`@8>w@Qyt;7i<>U#SmGN=WhRHzS%X4NGJ=co1uX2&o;W>cpZ>7%}}&8l^Z(A+E=g>cdQu|Mr6-wjUbtUxLOYz!U;0c>(&A^5q#jq%8Drq>JnDX$iVLfEN%+-G)zB(bk@5#zqw6iha=U75<qUw87pg38(D88@3Pc5$%kV~GNI@qn7c#Tp8VOL@WymrxPCo9YyX;w&szG4L?!A-tl=@xF!d>`{Zc8sXxbNAXgBdg3-Lg57?UlV_>BEraL%B(=RZevI_$J4BF(?+{Cnf{d$#{S8Kx4Bb!9l=+en_OMv=T?qk%r$^}E1_x>!iMN7Z_jlzlZF4A=*ZQfdlcay0qVDf29*H6MPM!<k?IR)dI!K}5Qp*37nU0~|w`;s`iW%sJBsZlXndHPaavp)e88>(X3f0+F*&*q2Zu(7Y>}(EiN&S|lt&p+s1Q60u~Yr#ONjgLxc*cN@Zx3lUYg5=1b9XqgA8C3itMLWv+`vw#NPA#0P*eB=k=jx<K9yK0{c69VFn)`R;=k%FYYl(i&Gf%!^uKQ)Be<P)rx$;yU=KnII-KX-upn{NT`TY&qT0C$RRYZU4~`GoxwAF~F!tj1+439)ehqH3I=#!IqFq5wJFN;R&O;utHxq#D<iY8*~I(v&4(wQp48HdFy?r-Ix>Q+eQ@&sXC{c1jk1RgL?@aI&)H{26Ml<RSmzq_#4EJf7MjkC5xj|GFb2%W_0GY)A*m`JEjnlgDe_9mpiX><SPhR=8nWs0&Icfgm*hAA9feD@(Sg2d!7Eh{%k5?A*B@r>bt<_oMIadu>{3#Gw8FPmy4N#Kdh0w`G~;;WkFXZpkf>5jFyKUw6a6$QH=<lmUnV2;>p6td>B+13W;W2Acse05L!U*7tqC6_0%Ev(LFzb?UaWbhK;l%*e=y73=X^zu))R(AS(L|I(Mc6=h-JMd991i@bRXaA3+fO_bPdW=u@f<?{{>(rfSTxeE}&cLPyRBrcGKRNVtUY~eu1=`v34xKBOeoPmDSn353FHCV_3<AO30%5&ak*SF@ehNrQ^Mgw(~2-!?*;h*iT)g8jgo%9_4-uq9pZP{BAbpnPa;+@xq0OclLUjMcDkJBv8-!HBF)i~jD5?m`kW8yl^=J_<+Xtuww_~+M7v$0>B-x4J{(RU{piIu6#;vep~xy+hW<<dy5Lr-IdH^HV*j1#Q+uUhc8BRD^!lw}*A>#Kb_S?yN_O*noPAc+5`WgqU}9Zp+T>EQ#zY2&Nlw7}BFDA$6qKT;+eSI!}Q2~OMadxwYvF80Jjg-WEWa9Zn(N)}T1-TWEe0;*jjZ?f`cj(!5I?F?E=oUCAV6TdXbk?#e7Z9W6oZnX{kg9otvC*A+|PcU=VO=!*c{TJTx_>KtB=j5NR|5E?q3ZGI}e)&Ul7V_nP;jRDvmi%?|r&_n1%+1oXnd_SG*MNW;Z~|&DmuViU9m)>}8GS_{L5;2=&}WGl*Oq4jFcgZ|R;k}5Z-NUePrN2-;6qZrABev|A8<vl5Y5jOS4!yTmX@!knxTY4tT@ZYo6|cjDjFGHmTMcx42n?>%7Y8v(?m;LDe{s?UX;BSFsZA=)Gx%DtCvym2M4>FL2%U-ZP1yT_#V7m;mRT<4y189MB-ccev*AhlxGm~kXWZf@Sl?D1EbsWZ>Ov|?~9idOcP&=Ft0xtWLB8e(b^ruS547HYC`*CB?Jj~ix|izgt#tY7q6cwI#%HS8JNEP<cevfWT{8r$_6IEuo-QX>~}5TAz&|YdmfLRL@~Dk1yy3VxGN8#BS^SqYS-ZvwCDj>R@(RL-2e7H%0iXP7yCf#I~XU%Ph`?tB3#s7kYPO3n$2NDj6%Y0x}0!m;z!lc=l*e2$T6Gu@DM-o(8}+6hfNeLqvJQ&n;uu?$zn45g}>l_*Ec@`hNgu6!yVc#aRtjg93F<P#}i$lA4fy`nf?cUKk!Cbb^`3P@xy3m$D~i*8$X6QAX>tUX*Q^IMIW?A-V5ZRHFTP%us<#9FsDRL=<U(@S~5E#?~>qgV)UIf$Q7u{x^#G+;gj;`feAf+QMrS*9KUm|>KQ=}^yRbY(9Mx}=MBse%2z)!|BhAmXb9+hB2IG@-3O6)P6(L@-azucv{?C5aatS5mzO_A8L@jz3eDsQfoKZn{I*w^@spQ~nAkNL>Q<T=usMyvpJ>G((w`-;<t*!0zVhH^F-AwR8!|RGj&&a<(!-=3W1>sh*&f|j5J+1?jxfTdxy1K@*!ouD%}UHG{`I~_9W(Sa$9}mN0-Stn4ji)4rMHK9Eci-1qk#v-1N1W)R;2OM`mXpS)SQG;l-$|b@f$*l6sxq1Rm6y_;A>_nQ~j344Cs>b#+=`LRW4T!cxzHb%DX!YHoO}fjr*lQ>3`I05XoRV^2)4Cw#PNO>T8NPF$s-w3R|UWLg{hfpl1A1ZJAZ_@uQ1Hjdoal#)h4VNU3B8^=i}cai)GjV~_yEH@<=bMyziq(G)@@PEMed?pn-4X?&G`(`Z7NWLM#5!H)sezPxnEKm2)x%zjP)tIr2A`(Xf9tT_uWt0?|`(N(83hPR=s+KLzaz{%&|e1Ef<mvecYda+;S_s-=pk+(FS>6kfzpJ986&maKj1gpmxnwj5BqTft3vl$_7=_1y$$lS$!XZCq(O)u@Vx$4H+5}&h`0$FK`8*ZM<ihjUA8B%ySXE+>3<AHH9r9q~HDU*_YzYAz-^NS>g$UnGT!V#6zgC50(+sOk01p2{{V!t<Ic;FI5x-ZRhMBX3ClAVCQV5tWVmEd&d@(NL|5w_ap@26O{-Ux7>V_b2`0|k16(B#wP4DxdbAH}FiI1JJ~!U5lA!Mt?tp$m8A33P77-^&5t==k~&zSUtmkP8>BR=F$+*U<(7j#%5hr&kQOGb}R3)xDW}&;p(EORUw0N)mwzNg0uwNwzQl<6lttlkd&~pPIT}*_|oaF^w7fquQc`8Uck-k7*tOorFI#qNANq(u<80iKT+XN!xR4z%_jl3XPxjR<-b4GH5+&6}K1Spya3W>=Xx?%abt{H8b-nscjgSF;R0uMWc0*J`zo~DUMuNa?GPQcabhhyl)JM<m@^((0Y4h<S$1?620>FsVb`J%^=eeI%oFec5+6NnQ8;0+E}R5L11KO&ecvRxTw>$jDr*w@l;V!Qkn-=iHlYX(SUXqJq12y5*u0c^;5WXUssv_#c-(|E8(uHO1X+Aw!G0F*tqGu?)e9jYV-xgO_5ZiFEnlfwbPQG-On8={WsnoH(gp_&}~h|#oR?><rWQ6hU*vWO4mac#Og(27?nPFXAC2Fiy6a6=1L+Nc}et?x1zMy_{=*ZFjSYsTbmgtqH#i&G`8=Hajh^)pbc~%yx3Ze9V<bLPP+BAXOVogGK2?$8suiStXW9hB3QLN-8*vq!^5+(-^h7#I6_3m$VV$Y(&Op^`AEI5`x9Sa^ON1xZD+0C&YC<Jqbn>KU21G2fhN->y3))iZCt*(Ht;ZSUHslpt?No-Kd4<F2}VR=kK^w^EX_09a_xpzL@tyYJ8MXcpS)4~#qMADiuB!{eK*e9GM{u@wq>(y%Q$Pxbk>%Ku`LO6M|1X;znr(_;Vo^+vaF{k?MBV1NvX7GxC^f9mM!{Eecmm~=6ujHRlaA|ia9oid0!kG576$_Ua$vjK33a6fIDV=WP~S#L+m$18WIgU8@zScKF-?XzILp`*bHTOhC6ntZiAe8_ea0jyBFVa){V-G%Ql#gM>a!OM<TV{tTCoxc+wvDIGTj$g%TVrTLlSdC7K&9jVReTsC+@3N^NsTY9jZpYMwRgkJdsh#bEx$FKN(So3}({oi|le$J%aUqMpuJ`E)%{_<1&6`EI@vpk#%$<e@GDauY<a0*KoNTD0(Bwi2KrjfVQjhCB*GdbSLhcH1ZJ|9%G;atp?6?jn3$6NG)bSh`u-uaT)A6m94ym54j)x$+hnKPSb~EI#ut2(vZ5MVovr2Qxz~SKDO9faQFR6r`hR>4r*!5EJz{ehcFv6R!zY12DiWbGKzmZMnTdxv%ueI8zUDk_Cn*wQc;8Nda|!`qJrOe!FM9kfU}bxK0==5Q?AbIlZqtCIo~@Am7HvJ-4`{7%nl<KH4vat&Y)hE=}Z?D$TAWEjK3hUMR0@JH8}!W4%tQkL@?(^rd<iCB9~M@U;1@d&Z#O>qkOW>|I_AGxD^clm$byk3`ErgtD}Zm(7BbP|tpC76xIaZcHRXm~Xzg>vn=9u&p|NsfZ5(lY3fgQpMlwzyIA=aUAYY=~PsYF>wHeq4adT!g^zKhfNb$6deL`mRX@81KLyyP3D3D>5wv1{Ls55c`D5KGA+PUGY}doAYH%=OJX^!%S%`W4m^q?zRhMk+Xrqj>PZHD1T$>;#`4n-4bQeBN~4^I1+o_6tUMcYcOCfOm^#X*c)W*vX!a|p1M_u{GF;Ymf-a{^!oeMCn||G4N6>?g;Wxa~a%9=v@a_<db~=BV@p|84vxfUEuT#AV8AaZ*$#qlF0|_hq%wXO$iN@u)eoS9IYtp#QfA2+(*mVlvT!o1FBV(uSi9$ISbLIL_p77c<1S)`+Oou#^BY=`C*;}LdkkCFs%0sO*SxHX_relI~JlJO?@L*}ylw51%g`zTYG-JXwXj9gYLXCbL|EU&|p@rRZ5y+;C-&<-1m!xb9M*-`)p{8JD)S;<FyUdY3&@&Iq%Ho4JOjL=KP|V$O7E5kDSh`mgUELi@SND<gY>9NH4W;>lG)8<mlt2HAn`P>kWtn<w)td+6t%YxY-dgyB{CR7NFU%~prnYZ>sb5I&aO<dFV%y$aQ*W-RH`mmgYw8#J^NLyO=#Kh2vs6b7lIoWV1(fLw*DX^G&r$7Dw>o`AaWEs6D~bcy@xUB1y&jMpmo&AM3?ShX$E?Qam{}cEoivhyAM+eYQN)G2=&O84{RM|m>TmL}L16fq&uMli?x-*S>4JO7O?6xC8odwx#E+Fd>hwk&v-+3sW&G4=kQ#lpuWN}}Du3PyDFoS%L=)6>#iEo-B9pV~+yQpHO}!pwhOm>lYPe#q+PIUui(zrW(R+)9%0(W<k#b2!0de#*trt1{X*W_a+LwRYVP}uVS0};oS-W7*W!^*PcDJ*~YUiAF#riGY&QPxtH)2k#a<t^lVy>XufQUGbuM?^^nX$U1UFK+5Ihj$Oo3Vzao#@hjG@MwA#+PhKPfSS9Jy@?9lD_cE;%BV4bIE)&T(M!D-|WS^sE_IDeU0y4JZ$mt^y0fqqubNg^Dkci`J?o+hV`>coxOX}eN`8!X0&&syJ*sS{_ldpX#JGC<i6@&bYDHOQdRZm%$PO2re!Yt?B45Be(Gsz7Q2`l`OHmMU3Bl{yQ=B#+<G;<<>&0M1!U@PzP%8l+ILJtKN(&@;t$5z5#@~&nY=r|TL#ub$}t^k-za9S8u?sFr+y~N+#7^%RSO=gEs5kaSF1Dw>;)q&)7*#Eql%>fB5DwU3#9^so#^8`3h?-fCY5+Z>VaT^w^_v$JbT&O#cs#LTDKQERmV_^`N79_A4!9h?xIBVv0{%%xj3_;Q#sV6Lb}m0;Sy3#W%n<K68!7$tj+ewT?)n0?n^JA!QA#9MX27z{X>;x<44RkGN>d(h&B<raR_^05aRJJY?E;ZJ8!;k-CcNYagy@xK8?<ibimmFb*3UNT;$3scXZN(ix3f~#V)n=jrm@#jh>fDMKs}0W%~9IK8?7Z;{)gd3TwImA3eeFo?|QlQzle}a+NBR8Jnq`{F&emNI(*o8fuKVXyd<i8(Qx(v>p}46Nj20dl)v?`8(t2GSDiX<Y$$<@gYaoH~nu@=!K&tLYN$PIW*in;b{QYyCx)LAm{uT(l2*Fp!9?;3@skiny`v>@aq<88eM~(%?32@@_f?35vJZ$y482bZpFw))$0bc6Ls^w@75A|ON1XodwrmcU1=>i+KCduKr+(S>9ZER!$`n;r0gxAX*mqoX>vq`@ENwo($~b)@EJG|^c5xtzP!|^k86v-Cxgl|&KB*2p4H_x3>2w_U?+jiqTizu-T76(;P^~xG3<j{NLN%LOyx#e;LCy{dgzc5r4l#}Ky}2J*g}m2Sy-;>=uo&0FS09eS*2aRl}uH>0|8H9e?YrQV}i|hlkm$YoVl{$i~#EXjF6tssGWh?D#079<3`~-p6-}Lln_;39%$-N!1irOpRK|UdasnUh@7Fg87`B{FL9fhTopF-?)%~m(D)HkPXjUg(*7T7?&CmcDl$kC^ySOSE&L$34S1LsKzb0GW$wK>gO<A}!||w13X&2`759#YP7t;#llEsKE)YwWBYM5;O*Ryt&D7HQ%=~rbSE^yb@BJdi*{{8pmNmrEJ;cd69Ed%Twg7$sCu`WD6O~O-nPDM*yEmBv$&8@WKNuUUOp%XKJ1b7U5KqC0-q?%e?GWnuERz^vCP>ce2;}N2AH7VYKL)`Hj{;oz0OKB5+mQ*EweED`Q%s;lfQ9gUhkl?h%E{*9Kw4WS@hX}3oNyz)p)+Lz(<*znGig#S1N{AHyU_eU+Jco}X#WZcoF(yN@3Ok@jQEjHh#!=|xh{AY8)DM8%?v3MmNHDIUZ^vea;<Kh=-kDtWDf{c=9WChP**w%-lQ3h<}K1o9W-1CsNpC|?o@Q~l-hyA`pF%65+qwEpjaD%y=EdeMri7Jwe866kg83(By1xs95znQl<iF>Y}b!2GF@1scbTM3dci-YA)*?qsu%NbT2(#Zq+dS4qy5@fXKgLrC+!ytYtq8n*s7X{7Cm25)5Rq<+Irf5aqB5TrSG$(CVz}y)T$aTt*XARs#&Wlv!wHd^~aYM*8IZ4ik5lB+RBCXm&!>lF03BHc&}Pp!>bn777Oc@B{hDz>*>Gt<?L7*?pVrHCEv|7BM+1vOQ<^*as$kjv2swnue14R>XzzuCCs)fT<I2j75VOtdlht`Y#Wtywox%{JZ@CVe5sw!xKYW|MuiLL=;0Eloe8qEJAyK6Hvg`~M?;i?vayA|+m*lm&igx3oSS0KSJ;+&qB$Zp`n9%-lsk-Ppj0ffnHKR{WXqR=TMI$JY-;l-zL+4CM=H|I(5YldCT<&g(|9WZ$hsPfgUrxCmZ7Z+Yoew2WQs}AIB5AaGt)iJZk?%kmW9%rvsS`l+6aL@`eHh*p`=HK3Rd-I?JDkY)WRy+l4?fX%F7qsC$iKP{R%YBI2THRXM&3x(=|VJU#pd^(H*n>;MSO5`)ch*_ix#Xw%50!`N~!_b1T}MZ$$%{u@F_9R?k#d&-7lqQ8}r6zPnK`%d@apF}t_!Lz~xbLVuZS<#4hIja(4@iz{ZFmdoyZxlBQO3IDc5^X|2a=G#}y?yIw6{!RB=Gmg`fqZ1uBRv*m>PK+s<Cbn;o#%COdSB4FEXnu|MZ`f<OFeKlTpPi_`vZY=ZS>%3C(*d+4Nj@XD2d!ELP?=A8FnKKHOUql2iH~T-N8pVNLnVKi3!!}zX$K8$F+BJ!;f>0Z<(Qqh33QVPg}lxwmL)AoZ0_*wUspL(DiwD~6v%(PRv8@&kgOgB67U9Wn6N!bGIHSVC5e$0tc0mmCt|PIw{BF;Dq|?^N0o;tqF1Cd291`2+?X*>Md+`h@|om1NGpm8K`;-M6;)~iB^zvRkZTi!{4mfY`M3vTs`RNt>1coBmfd~d?CvDZw2C$hUrg=VGTK`h^_jOU?uX3l{`}U<Y^fSX?lDb^KERVF=VuES(OL9FWXI`~_Y^jL%afNt<rn|t|HG?O{W+brESgP(vl(4gOMKL5YL6&0m4K4s?2;M8W+jABCrJnaHVA1JOF%a+0UmZx$VjfijUro;lM~+(*kbUM!HlM8#eke-ST5I(11NrB1ZS1CpdGang+If5*+g3r5?yQGlvU-vI`T9sx_~o?c*>2Ez&Kb70al@>&<?mUB!&Ys(%1ta<&2vtTcH+8vmKpY6Kq+L+v>{*=@F^rBy*n1R)e=5nlZLXa=f){XPbC4fTih!0RprTl%<L}xwh98I`sW=Q!VG95^M&p8dkzX)))3+|NHxEfj20(ysQO|@7kTpfrq&qcqa{y*UN#=lA>F0W;Do6zeN$eL*Wz&CV~<yL7J)}c(|?zZrg4TYlVvm(mQVD64iIO0*jG8R|Lm)Pl4J>(l%GLz`Ick+?W0f?VA%7@V2UeC#ir3<w)Nm{(Y{1vy;Nr&n*63y65_m_;>nHnmGUM=b2-ueAg+*5XPSCw*oGDa#P(Rk>A8C35If7==Ks`KyM<GY)Vs(feJV@dPs{*1C1;h2#%SC@<l}0ZMnjBHQ$iNe8Z{onZ)ckmHT<h!Oc?+4O0%CQVz6cl7?9&^G8y7O(@v14lUz)dS8x-2l|M?JUUS^*Mw(+iW2OSE03>kvHpfx$|31a*Ho!tMrn7_8ONTu89^pr0Y#?&@_oAA0h#p+U2p3ZfzM_BCbl)Ffo-CyB?m3^*qbY}<Q=C)&8?MlovOTLTG?z!=S|;8_W_fISolE+#*RtLHq*mgovZXX*g8r#u=cM_?Nia_KDnfKZJqL%`Pj&dA!tL+Yu+zsx?tE=y18AS-FR5)>%7+EZ(PQfiAom^-cncbqz8$7UM^#;fWfLh&4=wl|EBv@sOh8<Q-2+U3i6X5<4?=2K22_m;TyG2l`d9#$|FWXN8nOtg8DH%Bjh!K#0RS$mKZJ{HT7_io0=bV>xsX`FPXZY31<Ufc!iIn*9=Y==JMEMy0dv+b4sUJ-0a>V`JNx~%s&!|fSLvQ=)1Z)AHXc2lF0)^^aJ}QTN=MWcx6*22y;?F-{d+4KT}+r+CleXf}`0>*RwoZ#5m~<W~d|2**!=jj~z`L>w6Wb&CKq(s=&ZK;0dj<r~Q$9GXw++f7rjM@-o!0I1|E3^^P)HscN~cu9L7TEiqssgaCUZh^Y2H)XxT96%({kj)PPS^c2G(jRV>iGDVh=N#!Eo(JCiCV*E|4F-hdxONo5as)U$A_I3=FNnkV<Cta41jDJAKN=yrT#z$~Tp@KpO>BoxAWL&OlFvkhpmaJavSwVI2S*OFbSA$;qzcv)*@K(`xCR<r07+|tnzh%5Oos$<JJ=qXPAGGn9G*KwVG0e}}8HP~xWEzvVS!j_vWzWMT-(n!sh4hQ}RZLX*npTpav=;X9ndu;_h3Iw9+sV~|GA?w|t0t@LE&V8*IckN{LV1*a;ahPuGaio|pWyf>(JXcb5k!ctpjxV-+C!}3=^>2$q$(0EG<y~TsQNuVN4q<iZzMNqzSfI7OgB>9J#}XD$aIsC>coSw<K@=W)w&07B<}woTX1`B7rr8%nlIov{Cn7HU6Ak$a|zG<vZv;&B|OPk($>Z3K<_T$*;NV8gCz7@sdz%$=FGzo{qdbtJewNZG?3_}P$;!}{p7*PrGM;46*eCFX=5|yVEjoe84Q;j)8gaCKr`XbuYly|-@Pfod|3)Gw>G)SXxv)(_UEmIZ&ENfDVUoS%uNdBCIxeog1Je-d~TigrUvt6tHDqm;{3%_e`&saS(v#dO#S_3HJHXvX~&C#FoakDM992j9D2tJ9hgrsNeu=#FCWHq=cyV@Fy#>0NRB!x20a_4Q7%Zqm`uk~L1m%SGD*Q~O$ug``$%WfF8-axVWziMey#(v)TOC%B0r-DOgD+ZL}u4mW_vFYnAJ=KrkR?3l0X@CVElXQz+gD5${Y4fp$@7XRI{-09{rgtOf?j{t^*_Bj$7WBDZor3Fc-C7W>0x8eRKJzw;P=4&r}7NU<xoMuc6KjF3kl$Z<F$<YA{kPIsNI~1!<0%EX=6=axPus>!0((UjOq{)Mcg#bMi$ef4cCJ8jN3Rr;HLJ2F^~W2e=bKl2=~s{PN<dAk6s%hZm%BM%k04<j(lY`SA;(8~@UuRWM{BjB`yTX8h%{P)v6!6f>8Lng8=k-Jww1dGX?`6Tb8~&h%mC;xL$_MtzuM`Y=va?qwsqR!(O;@)dG1)7Tjs(7XBA2}_w5ypnX+{79OPnGQZ{&y!c?Pi-cQBMG%?HEavn+~1fLuSL53H{L25(n~ZXnWs9G2Uc`e_m#dO7s;*LIp1Y6lRZqRQUaK0NFW4D7oPBOV!OTDB>5<kY{Y;e^6?pJT&NqsMX8LR%#c1s9T21=FaB7jOQi|I@#8({;rJ};E(F;}zy!<XZL?c*s2#x2CE&70l?BJcw!rl|KEY;ili~h{s!aKFgS#vDOG6eF-+5RIU|{FMvs^aU@MC?-R#gU)b5mLdw(Ua$@67J#=s(SC`(y8bK8~@=GXQcA^znU=YbNzr0Ii98a<Bn9j&aqxoQVvW!Ho|G!y31w<FQ0(K;wq1=HX>7UN#=}^F+i$z3i|tG;t)FcsoNAw=V9Vh_3PRu_B0%KK9S?aOc(pJ)~;-v_<m(Dpk5qzm83)zE6Mj3u&sgwNtv@PPw*ITH263e%|er*-m5-#S&;WY^rY7RI6ZiW0BtW9XoMpr|m{QJ+b?)GjtZP8;XzLFc1LlFXf!}9{-+0T9<z@K@JC$4f@as9taN*k7vXS4Lz!p+)lA%3}2D}p9_}STUBxayG0H32q`)iWI@p5TLco8@zJd9dR9cwU@lmLsRAdg0Ov6=sCvQ~aEC-{4rn7PCvq=UUQA6mcssdFF1iNaTV7dvc$DM;z)gJ%GGeV$bsb*{HXGOe5Dt2gDh&W96a7UbBG`Sff*}eZx8};n7z(d6@-gO|+Q@eYQ#kh^jv(h4OzkmN6aeSqG7_6I2{q(5^1CpNCHn5PoSYc1HT+2co4D7oUjt)8{zj^^d-29_WXo`zEIQb~a5sdIka~;4l#wP=ZFM|{d7|$S4Yxw4s||P^3&o!-OF}sl;5gq0T_Jyr`^{^gz$8pCMR|7l6F(d|`|kut;q^rKbr-ftogxudApCY{2KNjh4LoPxhOe>o{aA+G7E9PbNX9_vj-6>f0Md-NfD)!y5H2;m;hf6R4%W_UAHL51(i6k1O?tZy?5*aQB`lsj6MEe}(s{acyr&Ldmqonag-vTYu^_ne13Ta|jv0W;=Y8!H@%ZK2lR&F9t4+fl@xdA;|IPbABuBIF6Nn^iz4&wqSPXNNBy3kOtKzm|mDvccH)quf%Mef!07wFKcj~WoCt(osm_`zCXP})<&|JbhKmzVClW`auE*Ihr2(-}eTeHJLzo$wU*j0*-dhTfeo!rcT7Y=SQG?60c0X&HbJsE+w;O}H*W;!u96-Mc|fKlcNMoHAm=u~W~W>pO!S_ZDnRvjaMG`YOGS}$+eNUNqYxjZ0w;M)_Q`3Wa3;~(Eo&|Fh~lknLH4F535iQg$hclZ$|Koie-02nA6p8*m&!?<4d31j=7NIgFJ((mGv^(+9uF}&fwBxMT#Xj`F%(A&Ud7&wnLGWo+3D0};Kz>*m`Avcm)D`!}7HtsQXgWj~psXXxDn1>U9*x*_u5=meU?lIT`=mby@hP(TKbw}Jiog{O<?pj@5c`@!g;He`gh>r6iUneUg*)G8kfP}Z`YSvlWhBjk>y+;F{lN4!gbT)~Q=Rnd`CgijcNs`|Z<jSUxG{Kla%2gq!2=q?RllU#%-lL&?fX4F-X;-{p*#N>H@z1(H6T7FF-Vo|pMiJKc7(Sv&dinE_kWPVIY4rJQz{>Jg`6C+Y^$ERpkg3_dN$crDVNV4BOGf}b+f~`T<D-e?%6)Lp?z?>;Wttv+M}wjAfj=QQ+212B+S5H8gdr&QVQ%~(m&RwF9|8IUW~G&VyiEQEXHE7NW*qvDW9Hgw)jA@o9+On%u!Nq)lW<eNeKZGi{keHS6B2M+zBKM13DcGRcKP!e-?cx`>5@dK^k-kInfL(KQ+(2NM4ap$eP08%KVnSu<pS@xV3KXKy2CgeyjaX}^*|9j@{uHrxB)fW!juu7Tz`ofKxTAnn1|jOnp_HuP0c4EO1=xvjdh1|SP3S!!A7Z`Vb9g9<2U}Wk$_W7T-mm!fye?T1rqW@=^41x4G8j%7ZcmEKj=Xu??_AT?o7_1la?0e(lT%`liW?|vGO<;v(rEQs+KMx=#K!d>)v24+7XjI9Pkb7z7~vO#e2dX?8_xTnfUU~S+Wm4tvw>ZX9-0<0TEXkKJ)blZq)D$d4?YfZufw8E%C%BrETu@Ou~VHe>Cj_1r?ZL%a0l`FfNVt_0p4?M?GHrT!HhBMK5wG4t$uyUw&tYy7Pcwbf{Zl5;KRoF!Ncj_H^4Y<CigdIJKucD10`3EkxThdpg5l1_5L#!6EgJHpuR@deZ@@n8B++Bm}r+s0@kDl~|!6;4nq_6Hl&mxg3LwW9EWpbU2ag2V2hB%bCJYCjQ$i)~(fnRta>@4Dg`ql!*YFB=f7w{j6KX%NA;2!QMxb-54SYxjv91vUHzI|Ii-Pn)7jaRv&Z7Uku>_2DniMXFJYnBYQ68Vn*#F*CjWRJ4lFi@W@IK9`Us_1+*xxgEOPitjHYAO=SuLZfyiBPb+8Aa%~5KcNwEoERAeT)_@r5iU`Qm8Bwj8P*W9m5fds<*{9|1j4_@o&vp+yytB}bk1A<jQX;@ch;DLX8*aLofM4-}Yk(;gZ%b^Yi817>Xnbym+8J?BHmfVT?)IwcfLf*P2lsoX3WLC<lbny~3zXQ8xl<mAzz>T6Mbjbb#Kd++hq@QOcEt#=F>+Sp7OF6bfLap)UgLk_XEhT)>jMeH{CQJQ9D_hgucY0Xg5nOHK5!>>*gHkR$&1iNtt4*7%8ahKC`+7yBvsH+4qC_1vjW$pbcBKgUt#H`Onv(@g~nv776WZ6E4H8lc<8tgj9<EHne)C?ejY&<?j-lZ9pK<iR`Ew&na{}%31OWes~B3-Y?R0HFHq@srRrl4xsVgDgi!DigW)HJ^Zk+WetGuyQKet>iv)Z)?v#sL2}-qHfTko8J%%%fjX}hml|<cZoqQ3}A1M>ZP&Up#;08I71ide9KJv)<OKJY+^!$WKbofK=hi@$5vp>qW7pu^ZpRqP)Cc5vRT-kqr^9h~)=-v7e4g5XjHpqLDfYx)FkC;39LAhhBMHn`v1%Avl_%VSBq)@7?du6Fy`*?Ul&n`h)%Ruqrk#kdUpeY>@H;l1J`zx<qyq~#?P>kfco#5`S8A#9N9=4&bCHJjndTQ0PJ(?1GdQeTvIs&@NvlZS!oXZ&riybYO@o1mQYRyOqfdaR}<@jCr!+J4tiauhge$+04@mRDtm!TJTZJ(fh7^HceYGCCSM;?)O%!$*SGB4tL-7_N=tZk54V>-8lf8pQx99(F%Rv@-D<*&(wb`sVsd;Lpm#kmXZhPfM42d#o%sgfeK(kp{BCq;H}?v;inHu{Ztw{@}4Sm_(?o@}wteBgOBqQx{m5hyr+`_?m_s6@zw5hB{zin*So0x%b5vg?`mNn(OoF1<~$Ot+Ri7{UWZ$i=NG7cX7uFkA9HmwaQ*LUNoLl)Bgt3|95TNcKbHyz6?O8S%GgOa9zUcz0>xZ#f27y0*2S;+%`;InUsz$lcEJIE(<gW~LRw-K0^hRnHdb4XK<O3NY2y)tnA`_7J*gi(IOONZFBFG$0z8Gv1F7Am#h8#0F&$Eoj?QWLKpq#RSn@(LI3znEs_b5{aqF+T}%=wy@;GpWe#ta)GCOtGgT@^k?xw`SYj>O+s$iq6E?lEqs(BP%x1Jsf}nyE=Df~R`6rokf(@&XHG`&4h`dmtR<*w;BZQ#!~4=gU{V->GTsTVn{mU3%pAp^&S&_1ZH7NW`lOpo&*QK`W?z>%G#;<-Pz}WJ-l34ts-}jr8s?5h`V*e^13^9nAc{5mlShhLHqhL>BMm!Cilh9pfpvIhx<=mucXiS#k%6SKIL*zeV_|0EzJcmI<?`Ubo@h#rYiMY&-ZIRmD>||cvOcfA?Qvya1RcRvrssjC<W3ii7$woA-4C=!4?3Qg4Gj#Oa4qw693Sbc9=gu=6gPv9ISIKPq=NA+tWx02vN(qadd9`{=wjIVwp1`^>4CmtL{b*G=YMcxOx+k$H@3;`&sz)MTKLA8x-q71jHw%A>c;B1(WP#5she~5hvG_w8&}FPUHeW%DU)rP{=JqcMWZVMTt`VQ)`k=7=s-KgwpwK?rv|I+IFX~mk{s1c<R~WHD(+xLm(uT1w1F8{hw0AAGI_ye%0`}1a?)PBn{#F=Q7XI}Ey|DVnmpMp`%?>QKJk@1p-a`nW{fF)_KY+&N<Z2;lRKqO#Y#(HURNbJgDoX$CWp(UsW|3r{nXC(Ej^Mw^IHz#DsRf4JPXkz(kbQ4pRuPbHJp6Cc&4yd!s793Oo?~8+Q}<=_Tmc!Dm%WCspd~=B2%3?WLumzf7UaSURYY8&wegn^k$oFS0dhs;DNy=5G92*awAKGzLKd%<L!}2<(CAE`7c+!nf=0Z`l1iCY$&cVg$VX}$z%I6%cy&aoAegbYd>vlPiaMQA`AJql6GG7+dij1UAwkx7k}<qetN*Haq1|Z-N-c>n_m*)uHB<w7*{WT%3Zs2GY9LroAq@g?Kr3Xm}=c<H7&A`Pp8DHFl+M@5|N)dbNegi+%Mnb#T)cvXMVA9UUk|zbt+uoC0^vJoe#GV7A&keY0Vl_qyD6QE_s=I|I&*KCBj#jcAq(R|F!p%a+Z^d|BgVZj;L#&SA=q)JnMWFA#Zrm1jhQcgiJ+Wpif&%N){IU41*-i#}MCSr3^K$atx&-*DNUqD(PhgHaQs57DZhO?~(B2)+F>0ha^@6?><Gak;oR1fL~T5Qm$ekx=1y_5O#!?2*wKt*kJA-5DX=1LxxXP@f#nc4>yPuV&7~ki7N;*l&YMfI5EV6!|gdm;X5#GunJh(`e9EU#N=gcKs|7Fap@(pbO=}y{OdxQSK$U_Q9K=2hDb$pK%)q(r6terz3L%bd3pAnJ2;rWMY3BZWoKY}N+<huHbO|0Y3I2uSVxFJH-nP_phFXaxn%d;9Bjmu5q|}0Ks0kOTxXv2x?yK9HwWv`-YL$^!4`VmT<=>>t~0Uj(#4yq*WFdV0C)ktWEn{ch%<{YAPHPI3M)&i707IWMuNG7RU`rG;BW-@e6q5U%B|$P!$UV2TL7)@44!=M3^sYe1BV#y8kBR>hc4%)KlNI`&Xa7<d}@isdlu0|h!~*Hhew0g#%k54wvWIb6M|d%A4HRFQ*aP~gz%YNh2VAvIc1?x*+uKl1K({(x?|BZJjd{n1<#aCJp$KL;+EWn=Rp=*=s|~y3BsxNDcelW60|cu763$tuq9StAegOQQp%E6E#C;g`|^zf6S+hAu7ma?c7DXzzf;C-PZ*;AAt7~7VoOv;T?>R4kX@^^7EAV6>2$Iaxp(P~<3#NW`x`7ns12iw2jIkdf-72=gg6GL6#SW<C>Wq^JEFSRa*i=b8hkZS!*+tditYrNU>*#9UulO{pe2maGC0>9|1BlZSFLRdM0$%Yo+0hlf@DPLyGD+#4{NBp5(7#qZ{$a)uFIQ}p1G4Su`~A*7Qe#?-T)1PPrkv9cB`gvz~yCE$!!DI1#L_^qYsK);#GzRCzq@+;xs^ENVpd<6az)KGm*?hsT#QrQ`Y}`tB&8Q<G0G<?ax~a-&*+A!ne}+tu%fsjo(V+x6=5nG=3|M|172P@bgg`9}C;?hWUyriPmd=7ctS~-?c`*mo!7w5cP7i7J)d8W<pHzN;ik@bFMN;kyecDb$QYFWmM2d7TcnNzNznK_d*5ztu=Lbsfa!uyryuOHJUrQmy-(mh1z*u)S(wecQx9g{LJSoDrEFBexmXyy|w(QSZO@_b1J3J^f={EJyp>2^!sTkJ=+uU5+WTNFfDF&0Wzo;a8gHCyQOL{c|nV`>U!2!?C$LK7pmzCiO|bW&G#m@T4hRK>K=aaVm;E=FA7!i)7#nns4jWodgAzsjqU(EgdrhJfC3}j?Br*~^^<Dog+lUqLH$bco0=@|s7rdiAkA{atf=`O#dvQjq+``{CSB?MvaD{ZAlEDFFW<sjZt%T7o~H7-Cl~Ie2EV4Sc~PwNg#*&^%9kbilcMbWAuejSi!!jX?58z#HT!g)=&mW4j=j`XtKfO5+g}vceMMP)2_^_HJ^feL)cv_A?Az+=Z@GBIY|VU}hA~FHAZx06!%`a7T`I0GF$yQnfM>5S3+-q1_1||d8d^?1@9UJMa0hiPRDg2>tq~Yn`ncQU;>oZ!Se?L9L6r~E$>kiFXb;$>O4&B(6g6Rd7+R}m>}gBb>1>QIs_`HzK&cXO`HeA|o8^id^GrD@O`=^U{Z($9@>=B2K8Gav1%y9Vl?mkQN-!{(>IRDRgh_EeW@SZJGXBi`nW_S7Q<q|WQI_5xD@iQvWAc~vv4+?DRB`k@t{+cU7X?W_m{eb+fT1(_#3219T(*&ZVT$Kff|6F8%oe3)H(pzEiu<DYz4~_g{V`?>D#p$}LL`Jp#SHv7EzB<4eCth0F+^X_%*jxJD)o>o{ItUop#``pQmpF<J9~?2gOp2OQvl2Vy8Ejh!jr$~h6FZxSI)U7!TcG7+eq!^ENH<q02`~FPEg*0z{-y6Q$7L*(6Mt-vo}58(ee>BLG-N0^5Qctu>4qW7{>KfG2n#$NX011xP+mqQ<c}BplpRTd*B24mXt!C=s{m`o!{lx<tHb%+@p)bk!HKR^)l*)9W+6cncmXtmR$yYu$*vLdOZeALdn|1IgUE#9YjE*#cfb-EXS`Nd{^Ca1zbSOJc3Rv>&3i|<(W$S0Dt~%17qyDbGXd-U*a*u^&cSjcL9vC!#a1$@9!y7l|2Sk%MnX$Mpbl8sbO@mX6NY1RhOiXr!_7$nIh3KCnSDT@<GWoQM#9VJ)_7oJjS=Q)ByEM(Vj`MCvwj6IZ2YSYBvN?^FuVPo>1lRs=Vcbh41AAd#2I@h{#I(dp_c<?~uhcqds#ScB0xtv8&bUKkD=F&=AcX6UE;e*hfh}4A5t8BB<P2iOc|-%g~?#buT+z^dPbAAxmKTPbLQ?Y(^Nd8R2Do#Y`;fr|z#|tPXz!9U*MlYg)+q<^;Ljtxx?540LRie^9O^?T>5;ZDYJGMz$l6gY_YpW@-p&@`~_Y$|Tk3I&XZV#f6K}p6!I$7{1Vf7Nr=F?OmOd9l7SbU9j`VOw!I&L82)y7*<Gr;uJFQ8d34yYoER1Hm(UakKnD1w8qSAJ4jIkBOG%F?)Q%0!pc3amijy^8L4yfCMn;hsxolf&NNrxSj;}M;;G^~*nf&Z$7qYZe{Xv`AbK(x_tL(yZH<|K*a~RoAAiy2g55=D-MOu9odvGxv|@%YGwDLI1+xHmd^wMrttL)ekyxhJG6ci00GqXwmA%(c=PV#l5qFgw6%4w~`MAUjD|Lz;bv#Dh%Eom1fWa~uYK+pM8k$3#ZA4sk2u5}e4!Xh+VlkxgwcKtW%K5igmjOU-gJfFv5WpBMWcfhK(LFF{>s1+o;SlWOk<*PpESYNGYv+%9LZcGG3c%0qpiXix%ksbKert-`;*;xRjoUt&1#M-v90+f`2X+g;qyKR0x{@4-#F-P@DxtSU2zBogl-|qAu+_%C54#9~hGcj-%m~>umm%=(4Pq0MiR%ZcNHQux4=eZarVD9};JAVQgZzmtQdMq2=G{;RBwAA{^buj2YszQaNKsTru_~%og~?3?`nVj`A9wf&8lsGo20)vZpOu>Pr+BcD?)H@E;@J|CSP&GyXKJl82Mo|5klwgQt^)$B)U1FQM~K8LN6MT^FIULU2+MdzMKnX_)+waUCb3jLc~9h%T**bnDc`m(t-X!1Wx#3wgJ}i+^u^`3t)uQ55ONgNTQ7xmqF*%&NgY3v)QR^dql2Nff~8EB8~v!EL%qVzEL12ZBgLE^i|VMAqmW3>&PteNTsk137;NkvNsFx+j8oZW6v3ee3Bxw06+laFQ#EU>oU7a+m1onc0v>%`U8R9%cr_E^_P+YSr-cUIpw)FHg`KKp6RVI-gE4&1PXta9>o^TpDKUrpNk#EatLTP#f|-P(|6KL2w?ZV#x%!F(wxlmxnv*Xjuv2v=4<{<vTgH%r{mxXdY0eGhQJb%*%)<2|NW#pEfl;-vJJZ5O?+B7sq*6?kMZ(!yYGF$aRDqYD31N2x8#k9!u+4QG;6SfgLl2)~xInv_)3}AcajAbjiC=efn{n=Y=&Rsks`}d4D^X4}n)vm)`m{fok@#dMz8>wwO~S||us`FqeL&c&|Ic5$WOOyzpjBhXtZ(8>u74avka<qiO3`VhXs}W=Yq4~=OnB3V$2qWH;0~61{)EW_q0*rYocZd&O%^7RvPhf477H0N6c|?r(DNLz$^e04X=tg@g{eT@XY$$#_Ry0Y=s(t`v_rlX_<aO0+zbcEFnuBm0d^2oH?S8dm)&y7h>B*=jT6N!mG5oZY3=YeQ-EJuE4v`ljZ)Im{+7X3>1>T+KU|yGiNu6DEiO^QbD`=mI*}D@PcEI(B*{HCk#97CN;;6)u@J@ylr3WyiR=e%Kv`wxvbjwwzi#(DV?gMX{<QlWe)zhB@LkI-_p=+GVJR1Plq2R&8=>q@3kn=G4guTj=SQmlEA-_^c*emPB%L;*2R8&hRu{fj{**Ydm)I`n6sSsvV_i+|%RIK`F1N#UU4rDMG~Uihz%>}!85{51vJJL%He}=NCEvF-PX}%9^J6*Hh?M444SX`a<u7y1)8A99I7{G+X<guzd(&`bm#NIna(f%ch0mT_Y1-yEfo^jZ#Sj0s`(5As5K-|kP?QviYlMPik)*N*LV&%c^$xV`;NXIdKv^RW+^I;vkp3TK=tAzx_$C;8s#0XG_P&eSeBdKNu=F6p9O8nzsgdxCa%f2JS*TY&wdKn8DTE#A?_f0~y=&s<L*f>B!w5MbZMI?K?NtMQP?iWS^{IIgy12(~=Ac&&1a+%zl06e>=|-M2C<lhsSQ{)XfCt>BryT9pZpR6a?OQGUNC8;o<_@djm@wtYaeiGwOcjCj#K3e6N4`7j7vX<-MQ-G}8e#`I+;>nvuCZE^eE(Jj#QEyY2Fz#Lhr5%w?L_aeXM7tM0UX5+sdPAx;exb|8Oh;MOwxvV8PDZQ@f??73+b9Mi*gpyDT^ZY<FSj)MGfOTo${K1&vO9OfUn%<z)4k?=R4^wpM`zNh{Ps+JdgbRg7b2=@*|znO`^viZsq^y7uvgBi6+m4ckjT>czP^PD-DmBPRsP+AKechIMx`u9MOR6BP;ZaVe39l;hQ1YMh6PRanB&xRwqo1imR;<`u!tC@_oE(j6sEecLoF~o9*v<O0##IIk`1_;CMQucu@X%s|KT-axGzfqdfm3a%Mf})qQdg_f(#LLdSo;LppWMk=#qDU4p1S9JZj1Czb%9G7QK@z!trHcZq0L?h_^q<w*o~Mj4#HVpG7KFALVIHfProqZ<XW3?MK}`R)qQG85-9fThB5jzB!dtyylxCN@+oz@H5)<x03Kkwj`i;)A*R`y}bq#)xDK)0fI}G|+HnMAcy&4rJC~*wb(8$h3A@-pj@tS+^#LN7Js6=xAD(?qHSCdhLE<`AFIBl+~x~aWnn4x<C2O?Q~7;_hLKM?2$E9)buFs+mu6|H(SqU%hjfgT%s7ciMiHz?Y!{_x>Dn{ml`jfG~T8x>5IneO5>?QcEDo04zt}OePb{!tk8s=n(&YRfo($6sOTEgVTpZZ`{mMp*)?puHmLL#B4x(s&6dCAep9@(Ty@^1VQi$d#z<+00L^!~{^XVmce&wvRf>G)&GiS{rGfX*Ap%Z&2Ip&db|t3-KBWH>bxKz`>^v0P8-)F!tkICe^9DGY%k6E-#E8vtAgc^BAZJw?--WGG-+f5B=tx2D2K&#BB;SrferKR6$$e9VI$FLnN@rR-EE*!DLG@-V<w^B6y7YKuXZWC)3d22mE{L>}q$;e0fn_;C>z;DaI76peooD$2`@WVzCA8qV2Tw>Eh4A}}4D#n?7J-QAEL;MMj_lrMG>fQZB?br!c5f<?^~CN?J$JhEaEW%pB>s+m5z@@BK@&C3y%HX744otrZE5+@FXB!GWtl|;={_TdYEDW|w1BYcQ!OFoq-^q3gOX#NgrSw{uazh{+`S|TeP$UUlQHJ6cfJkEA<4DLk{6!a&lL)GZlx$M(+Z({c2IpP%CYaBsZf!FQJ!k6MVO)_y9<(o$3UrxWTzuP5<YaGge3c)f34}!odlX=dtas~bb|G!^xuet_=rS2#B9M)93EUP0U_~uf3%bxvRD;kSDEVc@Hl|LU4GxAhHG1!Rb*Z0L3_$5`EgpA;NAN>ZA@ua7qPWnmDneNVjnAp4`;qJJCj_$F$GqTY1D>gpiI7Z##$}cCJc})lwkhA8`SoI<-jr@`@V$*Ckh#SdWo_Z>z%nD!EKJ;I53PF?pbOlh;Z=){<8ZW-~3`(AK{%@j@&-bbpwLV$;N-gw#e^%(=x%1jWYJcWl%y*dc!PDK%FTI{dI@NSgCc<ddzw<*(0A)%o-aG-3aSKSX0ryhsl^I??mnb5$DRGE9n4jrjZ>$og(iMD3-bAd4i1M_#>sQ{XyO#iC#V_fott|++{Lp0}M@HPP?`3W}<~s&^#UJZ?>jUpozHi8nzfQs#$&{i~uv2*{shrBx9GjazKdzH{M`rV>WLam4KCQJ!%;%L<Y?S`(*hBU>w6(vkJ^X@}K@pvwFL<1TaSfbws8oxf{+>y_XGbKuLG&=Qgy6#yzLUGBss6|4=y}%@67SYDo)35ZVbAu;mF86ksp`?jW$!5hB2}{&9fRBa(FLu{p$7ufnM8UpKx)k#(Nl7o{!lu;HT@CtRqy2XjSv2n;AV$99bu)b}xHQo!+R-k>%b$3~+0@+m>{D}gTx|G49n8^Kx-QEpjwk@3zdDwFqt?H0?I{{1gx@lS|n7mL5TEP`3THIuJ+jw!jQ>(LEnf?=H{+On@jHFtI8xBlXjfS>9b!}*$T3;x#fNY-((26L9Zj}+?95hs@36{x>7iV_o4LZIje#YCbp_Z0w!_~L5s=c_%sr1zFB1cXVZU|nNs11+Kt1c<Q1Ld}Y+ed{d>z;wk7Xs8`C(^Q20sJ&q2P&+1jWtp7HzEwF9CG<WEAE;OUOMpC5yDk5iUJQ>MoN%vT+-jweu@HykXunCrik?rUzqDHYu!yYqc)O3-4T=1UT&RaK<HF#GiG#Zc3kIa%!Z$sR$#-U=n^G;ol>6Rb_W61_TM4cA-Yj?$_S}YL6t0oyIm(n4--7Vo>QsFG=$LmQXJ3MtgZVmQw}#N8!_KF)@%jiiiU-c8vVg~?h#BoRDWJgSrP*LU?Rd@2K*$-<hxgSR5dt1{QCR(7U&v_hp>lF9)VI-|XG2{f`Z(HKTLm!MBXcnt>Q><9XwQU+$XO*y+R0Me81p1kz}LGC%3e19G|pcR`x@t$;mTc6h&9OPETA}ltuZgDNyXcFOq2>@7O6001~4i&c7pN7G05lq@`{mf2!!emx8gFH{m9P=v;t$1Kq_isjy|i<vz9Xg9jHWZumT5jr9M~D#g@PgVbIz#$06@~FEDGc`772PLBn|Gew--~3}KcDY;zGZmZCwYz_c%K;`l$lm<}GPfk_Riv4b<a_u9QIV&B@w%VX>6UY4l<EovyKHHL;F@IeXsaYswUWD}6!U}c1sFj~1Px_Q>kRgp!oR*etCxRGV7tUkUU*EItnvj$JmNL$+2%{vK6#wqo`Slt3#+%NWV16J}PPrG@T6$1!Embas*LBM5Zwu8Ua&AV}%8zhXDeC_5vZ=ZvpwCp{NxLSsMt5)#3X|vmY^*6i!^3|oVM@JsU9t|cy*|(JykeC!XR_&=9<;?tQUyl5QRmwe9z<uY+o(PEml;kk)3|ektc#|+b5UTFwiC891fXBL^04nP7BFu@*DIBdrtk}I{As$<#GL5Pznq;C^mDwTznj7?&(uzB8%VHTN$7lSq*XlgLnMmt(>9CO=gM+-WyK+KgA@_+(VfnhAk2lzs9oPJ*Qf}$yuH6Np4HBxITseOCZIi|I<SlK-EzMQ#evibuiAjxNZrLy7Iw`~n%@Yqk+n8s+hv6@i1#y}P(mcAQaTiTiokmXPGa`;_T;pum$7N6(1e!!dJEpBHgzX5y6isysWLxRVhA36M*&r{wPh_5Zst|h1M;W9^!h#)k{Bmq=rEFNHx1AXcGF9p*l~(q(P)Nk;!8&&z7_w<KuShLy;#UeuDNrcDHNjfx!~(Cp_@~S@^v4vFl$&_Dt?ij>D7>FxpB`L#K9CDbU}B<K=&*-lR`-lpraJ~$g(bh<iy%TT%`P0uWcM8IBjQCCrid2~$V}{rv%6QImKeDZH7RgGxv@N;EcP*QD$I8X5CLaSG<;bpwh3mTk1S^yT48Tap&h-^(Z3Vb#g1tBHA|=E;gvrFvlZxK0iKRhG@$)D4uDNBvGRi#jV3I~wBEebe`-jF4fg-*a{RMrm&H^7@WK-(A{GRIDUxg;+b<6hDWIU7OjOZ;QgeJJKx`1M(j;yBXh@3O4$>M5$D#x^%}}(Q6Y!yZWJcYt@u-upq1iTYM?H`%GBoht9BHtnjXsi&9w7->tE>6AkOEu2JAnRNZkAta!p-3mfgtEO?eBxEHuuWsc#eF_=ajGj8h#8#p;W1li0Wf1eo5sSCQ~}o@@wQ`zjdnqw*t-U$c?l}#ly8sBp!EzTW&17?`+w}aA)eli%f%?YyY$N34p%lyC1XPOt~E<c4*;_#LkvmDDRKaK=n)q5%5?3Ke0f7K2dt_B)zl6)P+ubp5Ez%Z1*TXjVXGicQ%}#IH|`KFM3Sr42I`qR%fG17I)>1Tk~u(#_o0mBM_aDndHez@(kE(AUiDeY|m7W5=z{wl^J3nLVYdu(DDqr1?b>7nkMeuP?JAlnfxJY1wf$rHoKd)*&jN#_$~KW=(N0deampSOk7`2`JO_Bjc?vW0;w^19?%}NHAdc+DyxBM$HbjqdC-I498oo`#MElXu>piq(7v6+iEr&m)eBq1DSa?3{{WzAnaD(Fi-IB27@Lr%GFj}=BUX9~(GNNof;cklJ#eWE8iTk7#@JdZiChNImS4faqt#~wA^N14*(5L;jrpxNh<xC_I(qxMeHumMITWKmlo5*5ZSuBKp$NwhmYHrtzuBaQTA|}Ki7m_6IP#pxVhu)?ri*Ne@X-q}FB~vU^t?>*PSUS0!a|ZlyL$rDRvh7Cfp%r}i^EfTZmOwqi)pJv%UMj=m4NWBOk<o9mFrjofFe2UL=r)>4$92(frM|AuLH@)Ju)4U<P_Zm+q6?PIWj)z9(WSUFhfSv)K?|L$^hc%wJF(&*i&xz7)O463cTIB5?B~<sOgmVU^&nQ&Ff?V8h{VG{T%^O`WD^z7Atu->Z=~{?U*1AmL##8_3{Y!*suJv?_e3d<(KHI-e?MkLp7dOrpR@<_6MZr8B@8YasJ>B(4GaRWq9NPj3oBt_#hd#GyPE3F<G$T@Y~Wjx{QKBY?&Ter~_Yo<42rl*~^<0H2}i=UXUuE(AXp^B5mT4;_`%O@|8yqzvw3%{89O(bSQRubfvvdI{Cj|mX}Utd*<x(8*VeO13=lnJe@7u>AA#RU0ShVpSffb8!iMSx^nk~5rLKdnJKpN$u+76<*9U=Fpw53Thp~yrQiOc9J2FkAIfGKk#8qgQNom!=}k!at(Y-sAtzosJzY)%Mtsok44GFM_qxK~qkct8m+8(ADEwk_z=f&%(()Z+rcup7%n6T6LD#3&v+_a=jLOJhb;q}q+s)eWAnW3H@`zmnb5NeZmKVTK3ESfm;jV>)7O5G<Gv8E=sz7{nl!R}2>-WBpgvUA7am?Sxx!dzHfBzb+Bc^TJ=QI^V+;vjqW<6{y-m}k$o{boJp2d%r;2(?kn~Djwyj~_abSwhRiuZ>}vYTrJO0QlJmXln*0PP*oBk%0w9AfX6xJQVtvtKYsH8qlGi+$i0aZYrhj5nf?mN%S3-9*JD^pW{H&ka&gU4KRNBdl?Z0CB9@j(nc&Xd{-284Pm2NO;7ab*gMO_b&gX_tW~vuK8XXMOdfN<XhLxRQ|!ft1ADgs{A({OS?kl;4+!6?5Uf?Y?|4`6HqMnQ?Kl+=qpIu1yS-_!W+w5&7h`LLXG_;nhL-6%b5<wTY;F3U4z$qp?)%H0ad=gt5ZqoX$_rmnBb3s{ItYedC7y5FAqEkN%!Srd#v|iO-@YQmmM)W8c<iP#5dfTH652!JZV%a8b@OQoX4m{z`*RWvPg<)P(}T}d#z#wb_}sa@~AA;zWhEAYEq`fvM%@rdziA$uC{SVCYRlMmD><vr`7};ut$p~@Zj|>e@B#+wCXc!BS^8Iq!;wFsV5wm@YXq_-pWC;R#fj!TuU)Ylbc736VKLgWR9OgvINTbaT}`223JpBo)uK8tpkD1j%Q<$q)JdMt`KykXj$2li?^RFQ<(Np9pRp8@rxtXZk*t9_2fZsTE#BQnLzk3yMPlN3yCx^6k{efEUy7ry-AlMRPly-FMfU{^_)VP6Ut;c=lX7$`4>VOcBB}gan#Ik>f?^EsgSEJO#A0v6+hi!3hHNu?0pY56C#TS{kIv)Mx;#I*gluougMTaNMe<BOo8`~<X5B!cFc}903RSR+|$P#p{yLzbBTPBlaQ@BDXvy1DpP>wj<V6klF<MVGW0lR#kHG0>1MpH&vwDL=IkKb^y-;DfJ;OJcYZt4p4bM-IlZHEIx2=>v&-!rM`Aj|t{ADVmQcgom(l3jdh)2RrVj-z)agk9%XO@qJq~lalJF-MNb(X-9Et2v)ifbJOpZSWWeJ4Kpn7~{2;kBhspZ%`Va#l_5ACQPRzjg6-leeFx)K>2wKZ9XA2A^z<CZf1N*q(})pI%e4roCXu5<Cza{L2cEP>bed^p@kMRHLj0~bF*CWa<117f(gW-|SK6t+<+7)Rq&apk=CzV2YkJ(k@UwwWPr4(#p*qKl=mO%V@ubxzS`A$r7gl~=rij%cc?0oMLoFRpKw7Po8A@s4Gq65_0?i(Sj@aO1a0HX&nHm?j*RN53Myu>^-q+*x8+3I{9k<Um~#;1Ro{(ZwV(d)log7Zb(`%&K;tNqIcCJt@3{0E~kd{Zob|@ZVE3(}q3?cVmQIH1mo$9YzT&RwF$vPt<aWA!+AE&L(;)N~lyEOj38*g`-N2EXSl)lduIPJs&tVW*CT6Zf=~Vd&^!R{)YSaxvVL#`2DgjCQ;g$f8&#J>CpQ8Exw4VEu!4A2HKK{xh2tS$Z|A^2@mYw_INU?`-k3TDZ8|IQ3@1$@`GZ1CId5j{o0aW`5?M|JuQ=s`x1!UTO=09VH2@Un9f6qz*AB^pdlI?d5g8BrGTSilAyf%HNrsYCc+p#srsXuH{1tt3vJ3Pr5_W+BRvQFQl`nF<#dpF!q#ZD{V|P)^`@)<<(qQ+X7A-$kyLO|>F>Y3IZ@o4C~g|_w?A(!d~4xb3*Ve5-v7^Vv!VE^DEi<2ym?UEJSc7+6d%NcBEPQ(Mfat8P*mRuu`*t5K#^Z~@twRZt{PCt5;VjM?h{qnrW#PhGXsiz)qrAjpGcC1Xo$3$IngJ-F(-=2k0Lpc&`}N}sV>l-*_q=6l0;23bA{3FAebs@sJSG$9K?kWfb&WTE-WTad>$4)06Y(XV#JO?p?2lZd>f{Ny<faC|1<c>d0@J{>_)eN=~Dt7EZig(r;4Mz`t`f0y7db;2G$@+y6>o%wKX_~3c@b<xqZaklOfEVB~Gj`+Q~g*e0?-Ym`o%_M}^rnk9TbyW9GeZ`N}1xL{ACiW_x~0dcbk%ec?xS{OLvS7Y-7WeS`_9yYU7M)aVx;9U3Vo&o^A^1E<y^Cl7t}tXN!6m});hNOO+_jYKBgOxJ(r4soLN@6WaK!v#b6(WT*{?}1NO?I2!qLh#p(6uMVfOoZzO5urxEr_%cbHZ_-p|KI02W!g~Rx_Hd#$J3?T2^Y^FPFrtwwI`+o@rCC&|Jl{+^ow6c0|9^TDiEd@-Kk$h82ul{fBtPJ3}Lc32;RN+%Etr3#REbe@|QpOQgemLcfvZ}@`Ep3Pq=!)<CDd0CRcBK#5ic+xRYi%|I;lSYMgoIzsH4>!^?lxp9@&#|M33sipwCLD3Wws8D1-Prsuo`k5G!ha|90pFv*Qh+U~(rox80u^QeR^Rp%<{4A2VU5E5;R!tDm>o`;I<Q>lx*F&6ZR2f(rbNQRd*6zZCsF+%0i0Sij_PCqdiSS4g#N=ngqzKVUw;G^!i$rE;{l1gzpjH8_5kAXBUEijIz<%Se3({w|UFEm>K>8zm;CC_^S4I4x0M-?KSsjzwhhDbm~!C%58(wiJen+y6b=#(YZ&{<4>b3)GjO6ruQf5Uoc=`cTfo!t1j@G*zNyoa94jjtxTapZ9>DUK8TUp*80Js<c&ah#P>)<`=+$c#c``-g1o8p`je>{;u;>5}MpUq#2mndrFS_s|_5pme)X9ES{r@7h`>h2pq4JR#i^=TQE9d`V@zF_m#Xd<u<Y7~f$)4<rbrfAIboz<1I+oN@Rk(&MXX{Gs=NS}mFUTh1(=7(ilESk0dcAIjy#1KANT3HWps1GwWDOCtslM@R(GV)8i*aOCp`sY5lQBawwtVSuR;dnJoH`AEc90RY2{CzYjlNPY#q3a0KLPIE`OJk*{ENXWwd<;vkD70=*)8!8==aU~fa!2Q-UvEyqpJ}~0=DoGxeFMZ?LbMsHGFLqqhbB0vce8~fH@SfdvAL$Vz-Aa*sc+R`J_LY~}e*?*Zf?@cXC7$hHh4LgmaZ{y!xKhck!PduI*GGV0+qy)mgX?SqG38Z#I-uX<Bwjoct`%Eu;}D@_uE=#_3U%H|x{|ulD1)nu6fCpLpsz)Zda}rT(P<mMNhaLg28eztrW%*dk@*+wW_kOPHlwvbMb?Ttjtz8}?Rd&VxvSBRl;EjZCjBuZXJ#;hzzvd+g&#Ru6<!~M36cxqN{9%Cc`{%LrvW?Iq-)KfA?SIHj+JzCNMs0kGg+DK=J{d=<Z+n?)*3E+ukq$U!HWxRwYMCRvi&5H0Yq#!SILM*jt^rH*Jvo85PASy|1t;D>epXQXC?P-TmW`e3X6k@t`H=nX&JcV6rU;aBZ?dtK*WBhDnZ!9B>h1)L(;0SGDz-<F<O_T)KXOlMdEXFP<N!}y;vBOBlOVOFhxwVa2g<7!<Lx0Aes3N`m_V3Pyo_ziFa(JzY&Jc;d{#k_ZTtM*#iY<>v5wG4e)j8;JQ1i<1+~Y5PNBgG8^V_jB%)9nM1jlzx3ra@cN{IS5xaYY~9dM$SA8*+Dgil+`O5&dRj}{WF!-$Kn&J;be0(#yG%#TqP>IKo6M_BCxEflQ*CuExNLZk-BJ%!<B<y=8ZWypnLiqkk7V<89PkLH_DITY7*{`J&et0WdQm_N#HX5Pi~f<5d$$V5;JQwVHi+W07{RT1Wp%&ug*+v&A!E8Dv3o03go@v5z;q0HMCITW<fBLytLm>Hh|eF0-;e5>@IX-j8dqdnuOcJP?9HN8m%GAjOqm!8Ba~yP{=gPx%<|~l2Hd#-@=MJ3OeiLATeEvkt=`}5E6Js_)1Ucjv=hbf=1ny$yYH?x6~ZGR4m&qB*bYEk#8nK@d0`E21m1xmwv457X>XI_Tlch*DJSVc0o5#Ct|ax9RYBq#6_rgwiM=oeGnB%T^QddyfX#kPLgj_~(gYi?<YsIn85X;rxWD^(I*ANOKt;+1T(%MM7zY<^L@qOPw&p`e$>)kP)y8QIR~8;3b>k%8h7%7F@@`wHln`B=tA|K{jt-duf$l4cMwT8TW$FT*qCIgB5jl(dbP+8TR&V7VQey@#?p++MLwuT$sQ7*69-<D11cE68nR^K7h-q{Wsp{dJez-CB>xxrV=_GFuG9NX>KDd_Kzw%m9%uQJhu^EU$y;3l0CtJc0SI@9v+8sw}QBmfJ*uI<W^T^-CuBJq<dnjMPYjKy{!I=-8bQ&`$?HR*UIV5nrSDnFu<pYPvuL+0F?ZD)V(%^dByPgCw9#Hxz4*q5jx=UH2Hf4oa(}F@$o#op%d|d0e+7P+gQAwNue!1BpQ5l%m)^RXlQ120$<a(P~7NlUCMmn1qojaVg^dDdFZg&7`V@7_U{$=35RXT8~YPTu(=}@&;&@DHmk4my7fFen6mVw$TDCl%rCmi|gXnAv>2;q@C@%9)bAr|E9Gn8E_J?0!N9H{UR2cBdLO_va6`;ZkwdFc2Y`PpZj2Tqoca%w0K!Dlelv8qA|=DF@qBWQwB5mllp@Z(YZBZ|69djL`^J5gWEYM`1r#QeY6G`J-Q|1C2i^AqD_NXL@gEapQYxe>!O%Ot10D?EC2Rw^TxAJ4p_ZFLA#-Y3_fvtMLBnLHempF5LLR=#Ftw}h2!+}4@5UE+jE=1s@KvG#P@hIC}DWl6<(^IhwrX-q2rIqu-f!Fy7!w0-MTUQ-~KZOcX@R?=4kxa3_mnSz2ss&grS=9#FlR5p;AK(C~Du$Okrv<n+d$3>D&ff_V6yPn|u`?~qcGD`$mz_%Ra+PA_NHO({$S5CG)8Hy3%<5}i2&odU$jQPq7cM+2_pS8`j;X}=||MLfN7@4tdU*|BgVr5`yFVgp;6RUfx!-)JT)7)W1l`3zvl9mDe#=OFeE5<MsnsJtL=mU4mmSf?9k3So7=C}hPL6YoLljmgKy&+{yF|w|trs}z#vx9R^;s7Ff(wht@24y>|yYMcgm#1r|;4x#FHc*d^n*YIcL(#=@FmExd8#kC<cOad<#bE?FgDF55(`_F**Y=wxkW}UNRfmp;g+NlIq_r&@E<NqBGcC8mSQHkB%`sxlq}Xtva8ssIQtM4$Cmr4B;=8IsIGB0&C5A?1L2@#4Mv%a8E#z6FxwTfM^wmy|USSuxEFUGS$*GNW$$=052O`z3s>5t%&jmY|$)m)>y6_DxPgE-Fpem0#lfr@C7?j{mDKk+%UV?=!&p#TYuW&K3qo?KbfQ&*Xf@?L-CR^RoWP?fXMeVZ7xo}7}opv<se{v(xd|3pVa0A2Mct|&f!L5aF?Qm=1pI4Sl4J&U%nJ;94yLHqXSLVi*xp8IwpmSxySD!2MdHlRWkr_EL=M<R*KgKWkG2>@1@?*?9T>l#VvU8QxBJ4`cbXSP->d2N4>Ag8iGfm)SR-Vl7e$H};)rnj%7=x))I)XWoc{l!UCSo(92J?yZ4L_&I)TB!=+euO!w&MZzsZk?(Vntm4GbDGyGC3ukbarOD>;>(nUZ-$e>`2p%RG!NGE6#rM%!w@^`b#IImZO1#5BDr%`o?*8PM0wsdhgwgP~zh3;$vkg1xr?qw|_#KiSp1GpT&5Q$(=NjJ7dfUa%h(%xt{0@v38Bw<5_Q;9iw}3;glIO<3Gu8!JRh#^1;m>?yNu9r)JMlFOn8!UDUJLmFFim#T4863ef6Yn(2DFsO;?Q#W3OS&E~zL^5g8qYYdW!eKP04RC>omI9PH-7JtSU-wkJfrp2ExP*vR7g)Mk9a*tf{W=3v={r>LknHS!=d@(Oy>e;(>Y)-rxcbzxmUgXW3b7jW2#wYIlf;4l=+lb?zC>4!Qd}PMBX7<_IolXch<2g^bCReXKT2lDrk(rA<`7z_W7g;PXw8_NLNf+Ac{Fit_SQ*Ji-p$Vt>XnCC?=n_UZIkh>k?#_gd?R(C(^rg)b&2&d@#lnxKB-vzxz~aj9$-flA2m;N(s%%J0Eit(60&%Epe<t(%sMvr<3ftnvL&BGb8|1i!(A94R!*64Pi~Eq3xKB=q`cAzqDbMftw-L;4FTVt2|0M|rR1&i_&BiY$NKF~8s0J;*s$D^!nZM4h^g4=N+1T^6MfNc!l!f~McHdZMchO}k257Z7z70170Y#Qc^*lS#Q_jKX|)Seo@pzW?j^W>R(1OA_ah)REkv`!y_4HR6v&V&uP8jP?M3|PBF#ih;x*BWs%42Ra$yQfq1UnstRVT1(YO{DV8costC}DeOIw=U0g{uf&f*DLBEvL_fdjQ&%Er=FQ!dS_G(m`&UQGIyunEqB*C?T9cIht25l|whgbex0dm`0mfY5e%cN47&9>@q;Nr5&<#2L4M`F$T6VgchGcotb+WTMH+#lWF^WumW<-*sfQolgvQGyO<86KRfee(`@=JiRYY3|bwxn-M`;XDkr;QoQKo3?fKlaGW$6l>_%ELtDf<IV_9QbY#dK{i-VkB+iteM;1tb!U7?h)mR{x{2UEX(fHg<LWr_-leJbeSvMP+!oNlUx)!SMS=ct0D@uWz2gyVMq589-+`$3?3y4v2BMOKYoed2e=#&74lMjbrXo~VRU9VE~i~=&NMw@EpvLL<xum$PAr>>emr>>fprsLhbtCCX&Em^vN(5P*RplGgA9_3S;=QxVwb|Neh>{BU^bJ2477=dH}DcH%*M95V<beS+!t#X?k(r8%Qgl*mJp~EJa6jrd0*NS1jDW`oiBrVR%j@e%7m=EU3hDy2Im(@pB)xF6RXsn)?Nv5KiFM0|-`(O^Z-Wd(4r$_F2A8bzgU=!}lU~O(0_<_3Ne|0Oy->S&B3f%3_TMOS>_#cfwZ%uI%w7k{nZ-3tE^tU?wtxkWd)7z=qchR);mtIWum*(fFV835h>*W`vyb-)Nr<%QVERnvWvP)E5v!ShDT$Eb96;9?g`_H9dKWa{%6zrXMZ>`xQkNK`;`&s21AMa}s(N8tt`7!oZ91G!#`u)6kKbPpdUb9#I*oU2TKAJ?q4!wA>a_?Tyx@@Y5Np$Bjp;OJCqA>Ha{ZgFM?tN;sdd;!g8R_D~FnwJzH(D3`snF%@mD8JA-qF+_7B>}7luPT=_ow$5&W@Rv@CiPcJ=XKeeULj^72Tc6_F<~upGjOgf2n3am+1>{SGHUf?7e$g$MUsr<(DeuFKcWr)c-D5=!5g_MCb6Nvg?9-=kNX5-#shj*JcUf#X9}VI*_ODb}zkqv16RPVnU0}TMm0!t#MHTzkdBEZ&l&SFu_?~dDmCooj@V4yPj)^mNNuQpxTW)k^MYD$(+9u{3w7qihN%GWnQfxVNXJ&E%NBU>wd>KKV(&=oWG-=CvBtB)|wI3h5MB6Y3cVSny(pW$R;FMYLT5Sv+su1bXgd=9n8NpDRuHJ+nbwVQppchgfvj&t=U7iZM@h_Kk*gSS2D#YRD3h-nH_Ay?rK~hj`Ojc<PNJ%7u*9m)*bD_;{eX{-H75qONLL%Nsg%21*&LM_%eLtVm_9A4=Y#{#ag@Y4Zf%{709FkR$=9Op0y4WwzaF@Vlfo?lnrAO1iZZ|bCyqh%N~e*5M%mI5enyZtvppki`pReuYo)libDrS1NS?ERoDVzujj^pt~7lWkijgCucGO1n<_Dps)UJ`M(OKl`nYlu^gV$D*U9=>#k)vbw;5Sq5Ru#l2q6V&6<r|f3qaS#Krsp{EVu5IuP?c^&{rZpYj%hZC(1r6l~gXFfJ$hp!p2l#KI86-o}AWju3lBjez?HkujS=Rg0_)S|IMReT~#zmjf>>|NR@ejTePts`TbO44MSoba6O%$z*T;u5v5PL{>_~0-<eIk<mKuGFI83G#P{Wv2>&DZSNt%NrU@?s*1^d%4`X7&CG`o0n~We413_-X#U~T!0a|BAkrftEBXJ$$&b?KBuS`-L|K)T!;n|jEUPnK~GKTP{Byl;aOq&E+CM{cch4ODNAPTojP<GkU<sPr|sjgX+hA<Z<UqrAhI|HoJV{oVB>%79TQpQAEUzENNe5ifPiLGG=lO!Q}S@vC0sn00@FP&K$e{k-t(ux|Iwj;A&Jn7_yT?J02Vcgl!06a`bO5;yAj^BHZCSOe`Yq=Y*z(>`_9Cr=+kN6_Oe}g$|Rvo~#34C<_n17{pG9)zF3o_W<cyZ9o=qX;5hBBR_q0p{gA{vbsGu$W5O4Jop*Kihlprhqbr5RY-r(P8tOcShOC7Fn|)uf*w08_dof;;vl2}x%9toJ;iv%N4!8Xp?9konX6m$9xSd!(G0_*l&Im)ci##R;aJ?@iJ;1uZvKwNh#kSU$Womc@_v25z?lvNz~J`Tv@m9qE`Fsa}5E!Z%QtuDT)n>Tc|(ki--t4ToVy#-mlSu6FWn=0qpC%21EgnH3IG%{f&!<e6!5{Us<{FkV1RY6NLr#@VO5T6NUKHX~{6i4DRXbPM)q#`c-MF<S5De{Oj(9364?Cq1B_B|ICaTWi!B^2zo-oZMIa)4Js-Y%n=iPYXsEe^zA>uHPKKVHCkuKOdt=jXgPHj{}kSWowT?*(iWFwjOc-&zuy#`}^;YYx~mVR)|T<mlRi`DXw^_lU$QqX>8G_t1)G(HAf?K%dom`xnFNxg$V^ySxO2v_^2f{C1uuF#nmX}C{l$f8b@D&Lu~SD45N@kSR>#11&AnI01*M&wrT*>G=Q7Xyvan3TiIZEi3ZuN`HHzEIu=VG;+a(S_gZ%KGy}L%Yo%oqwdd%zGnI665B{(!>EHIhja8Kf!jR@1e2MMD&?s4mPFn72&G9yLh^F6!^vfMQ<_ESota`EZqZQX>-EJY0(ly9W0$iHn(3AxR=wihlWgL8W1V?i-FMw`SBF)xyd!N^uRFm|#eFN8VN$h<_VK#0glF>(E_^hQxhhM<!&{K05Fm?!D4&k%X!SUD;^YQ>+;<eIO5vd7kSAu%#3mXYaUNEG=l&g)f4v%(bA5E#O1^zm6@yOig4pcGj1H9ZZpEhXkRQXF$vTZnZEZe4`Ex!k|eJKliOU3j+omxk=O{Pq@+z>EXfo>)86)uLdS>LKV%rZn)QIf$3?Fk$WI}Zo=^2;Y!hD|>{Qr5rYz@YcC6o#NAGm!OE&i_n|a%Rq$LSW_LrVi%TWvrynR*=ve6u(o@72BgW{t{D`7L_B{?7q*4u|^5Nx#uSRQaMR>AFI%yjkIR=vaO}ibfC6uxse|P*t>HWIX#Y!Q`9|XBIwf}t4EG3tYL+n6pZ7_kNhn5F0iLY_ovD>P}2jjss1yQT$22#1_!_Hix_Qx+Wijt=K3eJ1DCQ<xy<82*$84)4+xtwpVQ%J@^xsu$bt;w@v^0f>!a8L(AxC(ydg}PadniPHs;(CM5jZPzR@Qb#BmthkTmh(L2ccFUWbY9P^Pe`u>CG!ek$i=k~kcz&fj;AfOYO-_~?kYddh9ChVY$Ey;UD4)k_*{M?7laH5t4iQaYCT1D&x9=+)76m>#eW4fp6Z<;Z=CtFmKTM?Lca<A$5z4K}(Yg_-Uzcm?H^Uwai1qf7zMF5bB+z6oANEbH&qH(7gL%!9)QJ(atHk$L81U6u(YjrX)ECrKgk{(2q8i4sq!98-4FD}Ed*!*+oD%FB8VIO{#2=+9n(Ps}?EU<5RjD&DK*9>YrQp_0!7P9@nqoq^$)Heh!0Ef=Z8lLvi@YKhvaD^ShU)aPa#>2qjlaiiGOJYfE*1u~_vzjwtwgYzV2?>v)&jcDCP@KSo^8r`Kov(DHym%<iI=5ck9`0ixrlBQ?{%dbo`$eU0^4pA)R>=@%G!HqlDWI)h6X$vy=>#CndnLMFij0#FMYiWsJ7lav^cbsG^)V?%c@kj|brbuFsOh#Cj?IcxQ4;C7Zimvvv*<qlfF&}8$v9VdG_40Fwl{U#$V2yE{k!7=Nmr8`tE|<t?`CV~QqkWpVD3nCY;%%Zgg_rp;@8Zs*BKB@!e-f)bfgU4nr<sSI4%cY*C)l6|DRh!&6Gv+vkHxSt`x8_8YwStNk!P|$(UYWbxb5g#y(Qxl)RgrYaRrSELn2C0j$PJgQPA@ags4qI7OZ+-V9fN%miW~u%*S~q>0!e2V6N6XrJO__Ps%rKAj+Ii{4SzJfq<UxDJ(2s3zl;`>4G;_Z99}x{r#V7<;G~6h_}c#He>RTI-TPtg2JMBg?V(_L7eC`c9TdWj+8=UtO||IOrf!i+oqv5^Qg@@YBMk88GDmwe5*F&B+Qt;JYmMKfDg)l|G{>*2_trC0CuHI&RJXYUMUf9dxFa@$w@AcmOW|O;I`H)P4PB&3xZY~rmbx|(zKwySUFl0y=~Y9R4C8m+QdnucOx6-lnT>aqr&Xb-IQvSYol@+nK`vPCP(V#HTa%;)~@bZJ-X{yYCmY68W20)!vod)Lh$6na?jd?domX5P(YV#Cr*qyBYWtV*B>#?{9nJ(Vs5mU8>Qg(=dFcrEqtTJ+-Na31<M;V=0@PSF=KAbm>V<Z9}Q;A$ZL5wW=wwJ#f$I0GczXT_h!bZ2=OX@3=V4~Xh|Pr_`fw&qyc0X3DsuhgoB0ST;gR2X=EanGa10jiRmh*;XQRM-;WdHFDg==vSHG@h*+*?AM|Gj3-=ut+?V<JN4-Y_O{q+gjr9WAuS8f*q*qM^IL#D6-Frw@j(U|7^`~B;5Fw*p<>-uT{w-&XV2qQB*sF$c-mZV043@l<tX!~L!UaLgg;Hgl9*~dcVwGnMo)@1N;R8B<tZ|wOge<8)`q;H|&B+%8Ctp&VJSVSIg2l^RlehfrUcpwW-+PhCVb5`S3vS}CgctM-Ur@Y!4GrZYALaFul5;W16DrRIO3f=}71K+6i|OgdGa^N*ch|U?=3y8~9`l2}KYisQk;T2E2;`h~L;&YZVY1SXFq6E8!eqFtF!_S;=H)Y=YfFZuwq!C{$hr9BLWuI5)Do|@-c@-?@h>NsX#Kg!cK@sHr@qNP|9};gO!)22rz1c*45m<bu`<jGt-T&nGnm3)PDFS!mQQk+ebhvSA1j0_uIU_nW;y=4XWOc-XvCQBcqFm?$MVV}iXuD8Gpa5g_OP%@v_sA`QBO|*Hc;Oz1bBBDm<cC*5Df(o>yONL9W%#J7Vdk%8&-N{l}Nr(#XWrD>2!5Rp*t=%nXb&`e{1RU(RLce)$CRQz?O8UqK+p38)$$wxo)t@uVqPx$N}D6hiYS^i~r|fof&=pi5uQ<uKgz3)&9ZF61e)|8Ca6?uiyD?kJ{F-h2SOHV@P=rwZ`9h0HVtWVfPDdLBX=!GcjG7#QnCsjj}#IyQa!shf}>_3AA~_&)l%8U0$aq+?G(0=e4^Z_%5^@N6@P8S!Jc)d^mWTot9%B;db4S5uC|np@}xyvS+K8KDR1e`$39_VY7o1GAiz|TrFPNKhOYDG!Dp!qMPo7aQoHLL5GA6idN}Ry6zf4n+Dx+N+3=&F5j2MH$6W2(j;ryn%<+klz#V#Ca8T}t1REd=L1brg&zoR3)`~r-OM>8$L}R{S;!<dZUZay@C(9RK+-e*K#<@BDnN;Xd>_6Gtf-LnD4i;vC#X1nr~KR+{iYm$3@Bo<&>PDguU%#3rud1@xl-8;Atie=c>`t8Z20Y51IoeQ>VlN!#9#2c5}KAXfGn1e2tvw*wg2n;JC0^j*)BPb=KYe#6fTgM^1FMD`WcC7*papLUS6Z&bzY+@ZzKJh*XVvOjk&VY>5{lacRjnpw|I^ErPnB!N>2W~6H`fn@Xo1AzRGK~x#Tq}u6UU<H%qV4i~OTSEw&?8nMd9M?l~EarVj!P`0MYd#G9D#@Ed^XM)<B*=LHp#ijw6OY}II|2<b>bc1id4FnQE|hOo8r1Sqj<!o1NN1P5mGv8wEn=p$`jHFjeZE<yd(2l)zVL@N#2<nRlC#N?lpXPbmo=Z%r?BiqMJf6+)CUBxKn>$btRE52fY%J5l@<$g!cP=!jQCQv<@lu^P`$|RVGIFwwlkHj*ulL8)59(4fbZSOFk%FxJ!QZ)eOf{zlDh%mUweG-@*62wU=m~Im9)%lOX(1i)8&)D$DEjw@ekFPPz2F4$Ux<VSmtjtaKm0{*FJuMh!8+^93Nvn6uVVjX>Mv~boCc!H+S|STobB~szk+#dz&Wqf#6$xkAFwR`diP~%kT1#PwkUB6e-;I<^(N@_{A3@`lD;do58(zcFCN(`nz=>9z@0f+agw=#Yy^?a;zI;pPWKta!01$8;4gTyyg#!ihA0%-enUvsi8bT#G&`lOmWE7N^VJnc2VUY|W5U?~+46QXUhLN4hh-FH4P+&NKU`wG@V^e_SYiX8NXUp71a`VhViEVf*I7xPW{fbDQPid;=FTT(C|HKVToG5^SR2xq8A<@W;Tx=T->n%f~-r1ZR0S?BzntNbh%JQ@i=pcb(c!%X9bb@RRObW?<HxfF(uWJqG_Gs4Qu|yL@|A5o@OjKx37D`!WGCwOEG-QlRuLcgyK!_a<rmscEbr!AddjhW8q#;1ye!0bDaME&xyf5au%DUK+@mQHv<vVvzXo0O(2T~u2=D{;cx&{GmFaudi1HE_8SWT1v@4e5H5svpVOzV^wjei}Z2_jPo)-sq@?_X3b-f1<HZ*vVCrl`R}2C|We2OSyD9pIjsG9QWTcTyvf*DDXLHHYWG(FM%aUQ+kIVna8=W!3yCP2?N#n;WdgB=zBYd%A!(6*HJdBGI-?nHB@DEc4~ftDvIF;}i(s3<7{^IEkQ)WLEY`Oe1#lriF0&j74Oo<IQVjvcCdcqCa+Z3m_uuh7jT>-1*}(gZ~3a0c4N*@QA7J(+B3j7$n~h7)weZ6EVk?ndJ5F2YMhg#{Nd>2nS&<aq#yPpK~!Ro%mZ1K|pn7BtA+bnUs+~+>*J-yZ8+Nh{d;*1X0<u1e4^4@H7#3F8+e-moX!x{2YJr5gnsU_B+kEd-N1qCg9!g9ZIVwd56=IfxGMS%HMwV$edv)uZ_$Bt_m-Y%nsb#*N)6=BXcn<cXe3CbahO28k5apK!!RXNxotfaxxk%<4zv<I208j33gxCL*;ur4#mhQy=(_L8X24igO<;R;xrDm;p;^cW}zUr#)AP%rUW`IfZH!ab5|F5d=NSRtcFb=0F?V{?pI^l#?;63bx0h*^y6ciew69@sV)WIwhXDFG_YG9$)6#=sFPVk*-C=SgImd}Qao~14B?<BKe!#1{6tnDjm~iZ-c?2ieW99`^orgXNDUkV`H`fVTG~P2SibZgM~=oO(fmfjM`g@BU@_k_EbAT+`H`)}_>bKu-A76R;K+=<An)QnB4i4b8Ud=_ECf_*!P9s~1}kub+Z`h2Co05eRcQXg>zWgH{9Mz{!?QJ2IV}|Y@91~Zo;Ku44SA0?-c`y~C#nY<BU@_BN=0gn(ykcw4~}6rJzAvMg432y;VTaIVob*{S$&1@smJyb&+u3^21HoW_8yIj=fBnL>X3cI2jNoVS4^LFM^a=e8AU~w?p}s5R3@-!hfny(s{*?Y<882-5%oTf+{LK)@_=!uXI{2y>4}YVw2s5ph~3}$JY$zv%#hpWU8cui)2Ssrxc*-XT)6y4XY*B^Cz~3(#AWQ#X{v;%9s-x>FHe<G?9E8(%yPDjm@T!pgbGnMwYMp7>BdxsJg>Ot^zuizmc&4&p37!=bnO(iWRf5D^EuOzo8&YaIc+*qf4f9#z<B<E@k;!OG=z}mz1F`Zb#Y=LRIcs*l6ufx?P3lgfMw&DvgqiC!6ghI^tBe~LAd7LFPJch*i*S?-S`n~!B#k@x}j(76Fre+H;STw^ni)L&k}FRnRlZ~zh3Je;$sX*Z<pb_dZZZkcpb?8P-S>R%SYNsfux%Gw2DG47RAQMM_cDfi@<s2+CoVkj~zcs`$-xMU^;uoa%ogP^i0$-Gi&$&eT%OOJp;RTrz(vz)3X1cx;G2CZA-I+)@;^X?QZ}5H@AtK_uh!exDk;N6$DgL$a(TXUj%)WdN84s5~@tnM5!u6DJe>9u)_vZ#e{lFghE8b2YnSvsZw9HM9VBmQd5LP!8a3~V~lUEX7BxX=iYP9t;^x(zx&^N?bXcrwc{H@W^tkgGj6nUhGh5g#_M7P99GU$Z`duqJuaAm7Tub1i)M-qryhkbY@7=3ed%~vQJC+nS>>s_qC;Y2UKiaUxA@=X_m&l++@2XdC4bJc0~RUD)P^0QF^q*0lVvZe9JZQ^h<5W^jlI0D+~M~=C~?NiMvERN&Y-zhgW#E&x1}W0H9@FJYX_4?t*=V-e5M8!NJL|DI~P(=Wxz-!qv|cxpbB3Gu{0uUWA(!LGTg+M!LpShKxiri7j#nMnJ6<%){H|)g*9WD@3KKi!Jg+>Gt#$U5H9`>hRr{9Iqn)iI~z7%M<zs$sosV4)q_`SwL%Z5(1rm)@J<7@9mW^8-WoAuWUO>G6ginx)2Mm`t5tC$V2sLN&iK$ah(>w@46KqeHo$E7SyyFB&9*3%tA|2PDP+kd##pWt@bJYQBZ|VJhVpu%ZY`HhTd5EUui42G<?S_=K1jnQaKLliF#OcRuf+fp-OmFQ!``@ye~ZD{Xk2jb_?iEE=)kuw{h$)NR}%Nv_wtK);78Utj(o^D@I?iLf$V@W<VxaH;;}_5K0DAIA2r|8<r}|6<GQ0G>+hK3_+lL@GC1VV>=}Qv2%1Bu{=t&3k-~B4Ya!q97Mg2&SC-H@<q{)=*`nB^_}QMiUVLVDaAO8;>{FI+U|ybFOOd%A&D;ssiVvcSQ+w(+ib}^nkZB@;Es$?hTfC(vp1QmejT4)cI)RaWlQ#RWAg(SEK|_!)+o497Ip7cytGP{8X8+j`8#qCXP#VF8bEVhk0s#UDbdZp!g4_HnMjxqm`Qi0WCs}k5IYWHzeM(y?DH56b@|%S}TH?)`b83WPg+`mFvYqv4IVpXXrFeJ#Usy6u@=)!1U^|kiv#9$OZo8{LOY9RZN^0Y!p4=QBrWG^m@(5_bw`*ZUzwm?lygpJ-$8igKF6-67Kc?j*?m{ZD&`3}JRqD3HN0bxwbyj0sp0>=8ut3vK<1&4rGc|giNAAgrzqY>!HfwJuthm*v+van?BaI8v%=zmcld@g^42$1ueu=oNocZo*@ifmr>lZ)WnxNA;zh>>6e`mFPp~mM{ESy*V)pJvPxC{@fvoCVXFHNhndiI96)la{Sh(Az*`n&H>B~?N3q>_5o*gQURpE@v<oX5qrC_NsJi)-*?)s=<D^OlMRw2#8uE=XHEyYF*ET--@=D-IWbHhzB=7c)w2=h^!!``A4;e!p{rDC~lAW~T&i&(F3&*%^}BCkF2aBM9+Li&7c#=WFBlH{bs8`+vA9e$@Zu>IyB(vzZ-dx>h_18x{NM<*|zFudyq|6BX)ep#eO&ZgO0@<#Gf6bRf##yc*(MM6DI+I7#~;7*Rg*V7^BXi)8GwWUJ{&B~x=LwOmAf0A*AMG7$2M_?V-bKD0d?9=6edbFOcEQzML3!UjpzV?{6tf|+)MTJZ3jufA26ggm0qLE3QTR;A^w3MH`(v&M07t9#b*o~1bw;5|cw%I;ZxanF+7Gc`rmH%xlb#FK(cwZ$o@%-c#|8stf0!V*Fhgh_PqK&(ViXc5)&Kw7i>#T!1fC{r&|P=5g61vfSErXIgr{dT^sjW}@g1%K?&&N~p;QRAKtHA>=RqOq(|%1feg7r8N6Qquwa!$5Vk1}ni`+hpT}B1@wC$WJ`x%_=4kF4|6<-wDO5ee@miMLRy87Fn^Yk6@-`ZscsftMPZqZ^>E<3T?{g;(-ld62|FP#-$uO<laY^(rjWyIf76=CBm6xro=VOGBAK_Vy6WbBp;8L=EZykn*@p)W`wQ0ejp@)4ZEn=h)|n+_K9~UKjRu#B%WA??GdSdB%^dPrDsq&qiZ+lwh$=2t!mnMeO(fsx-YFZL2bwZD<uzj820@Fi*b=8pfKHk_pAAhn`r1-@*8UgLlnn&r4vxb8{e$LxmfT>^84IJz~N>uNe<*xlRFT)!{l1o&uqqoB`=~(9g&1F7DZg4IA+C;_%-W6^Ml@4XAPJT`MuF|>1jELvZw@8qNX+p8UUAr3U;+T_C&F3M7ydf8t&PMv;Bf2*BiRk3xgy=U0M+petKisb<$&zZVVAnaObXYAWx^4#M@PsaW9Npm6HjDmf0`KnXR50OE3&0)VQ$~mv9)py+M7by{<x`o;}D))nfTb&yElKKGpnPRtQ^gN;@~B|4LBp49P0$<KWJ;CXA}Ka?|5mkW??;OtQZ+b~GJR2_0MMFnte;nZcTce`9!#(?>2(Z21+&9;yIH^@Wj(g}nuo4rlUYcP5>&Af^^xM*M(M#0c}9@y32^|7#N*me|e;4(<HYNa+-*{9XU%Ol9`j+xk7zOy}L&)Ah9l189EFZ4*5n5yj_xf=$R4N<hC}BWx^`&6I+H<a&jh3E+{2%;M3c79yQ`em4XcoRz|aKoY~WFO?c^baZfQjzMW%8D5JMk;Zi__t-cKM2+8=Ks>Cx+IR*PbJn&@2*n#v@E(iwIY6Qt+?`nF6cNAQ0>?SYor7F;P+VeZ)6fI-z$DnySDsVQ0XY31zYW}T%M&4!bX>wcO++9Be??P34gJ7rl^h~;YDnJD6^0qgNt7p<KpRj2<{Pvtuz`^Py~fLX(reSMZFHy&$N_6Mn8YF*fZ7z7Ck8Xxj*}S9-%t%;BX1bU{|KkV`hJ6xITGaH2P_uk6NJ~cwTpzEL|5bkI7I-@h*~$F1CxumP!@=FfqN#`1Vb|OAXbuLGtOW*g4Id5E11h>>O%uyv#is<f)I`B9!4h!sU{{92abcjBC6?*wGgZ|2`^bsr3V6+02%!Uo}cgNxHIoH-=WsO16t(X_>yDZx=r<Pi+z<Nz}*9eV19NF7;Qd}{eAU`^FO@DBi-ls-+4__-dFyMdzG#85{bwAY(@yLx_9>lc{}FMqS{7Fc+V*#Cvbv~<!yH;tm5wXic~9iI#uKc3|s0G0j45&FduUKOJ=wl=YQ}7gXRkWT3c)OE*UhZQeR3Xv`@-Irox`+GfBOz8s1*=3taukyAAL!?o8=J@VViCd!@`ff(R|E1+{EjFe%MA2k)aehI#E_Dw4H9;FL{dpoEknNAZp$s>qIS2`XTbKcF1P`?{B@RBJQe4J6MM49@6py*|i&HO$fdkRQdK#g&M<0i6FWW|r^}{+oA2gb7H<qpiW~%(Rd91>5dQQ?S%Yg*7y&ND5b)f~tH(`4HW_1)+Y9f||H)1U^Ej@Ay4SLVZmrCzC)3th@zwf!>x-f9B3y^$63VD2YQj1Cgjl7?(Xlg2&YQ&r6I9=rmCivp#JuM>cFQ^7u6<GtV%wnhGIKurO<9_w)-4{JD~A<m8%Te}SVC1k9H`?<k?thUUoB16gJjZUBg*t;3<4Pb-k4?>tAULK92cLOHO!Oh#sh`R4$(Td1gfta=>#Icne&BTi)=XVr_3@j712Np+958I$M{4rE}$iY$%Q4jutJCMxwHkezQp=$TJ=Llc0v-C_am1k>XEP(mb0ul#%4@+RG4arL5Q$nV@?(mSaX)w)`~H&z>l8g*+-zky-IMoGsWE=dYf@U(yaMP%J%=gzyXxe3|D=2L0%j@^UfJco#38>An=eTYaO6LrB_fxBDszUq8Q(7WCEZD&LF+XJZ04QM9**lg`kf%3;D<n!8}vMCAKKKCG$_YWY&Hyk8N0FlL2TS<o0`$_(a8;X?$Ys+nK8IF4F6DY8CTAB)aj4c3;j!fOKbs-G63V$aqdlwD@41)w+cyyhxkcOH&36LOY3V!jdM)!MP%XmIfLeBT2yD*-tzF8#hD~+kLeymd~&8loXQ&1HN#?zyz8dN+c)v{HiYBQdpwZt_oTTQ4O6Q#|7ZEhx=sga<^T~T2Pl?U2S+__b+NW+-{9qHPY@SJ5S*6J#;b2C);Z83}r)%m$A+^y-l!DI*4FGNVR8*GlJnl;eK=6Y@|^Um*ODpl|{Q;8-R2xk{MB!pTG&2x4VQ;nBWB%)P^IAVOyK;|!AB1O`_FDa7lIVqC%Ye<pAq+DUGLlRdCBwbM;N!Jxf&gDnCB0u6NKa$r<TjWPvksonS$d7;m`Rx@*+Q$`0Jd>o|LV-jjvNuZw5^P7(`D4ikEqu6LD`Rjbc_~7YqtB~4Bodc=LW-ouBLEneIwbKC9g^W~bx6i@9TF2E3EvVClE24IE<xSck8sN4y-iEJ)IHpqmNGU<jjYc6gk})?wYLb>aS42==~^t{w&Z_DmVr=RQqUt2m}k<LAvo*oZ5gsou|(u7q~-Wqf9-=Qo<$bZ8K9FL;w(ltSy!uyNvty!ooxMrW!qsHCU1yOSy*c(QA=CUk0q=xEn$7E2s9ppB<caQR)WPBH{5f3{tHDmTf?7Il&?%bv8u;yfkaO;rk<jygMSnWxWFt}pdaTzU(*^3+Hn!rS4sw4=PksyxIZZLD$Y!^LOd~X=_C`SfT!tZgaUC${EDDr7g=|#lB<ZEkD!*@Q&-?jc#9x*gUUP8Oi{w%RcZmMA4O{`rDI`N1>N~1#t_O6RWH_&Fefm9``9lN3H=SZ*(E3dTP=Rm&DP8Rb<_X;&+jTn23X)Z_-s>6gJo~e%s)yp;yGr15+_9W3R-@DM#~?S7c+ii(YIF1p@ezvo9E}JLd82J=kNRtJFE*S+HVIs;J0mI{<IoTj@$UD(!bYY%v)!3h0uht5iLtT@!<@%LdaZgqZRdK*(Qd1FM<aeAXU?9mYnk&1{Ol>@p2`Gg%l$DX!DXJYL;yP_VTD-vntr&siH{JqSMQiT(-M_S~{|mxN54h&6b+EfGOV!u?QR8T3T?@VAsIBfm4g2Ss2#1#B?Flfn(s%_G~&kosT~>)u`-oZ#8%X-nBm^WUzbj1q4(8aBdqmbV_evm#_C<{l>(FR8E*mqcYTI%0g)w0Gufcv6LG*gz4sy)u7oZAz3kuM(C+4tsF685r~th*vj&0c^y@s6|TV-I5hX0bcAq{Fa!;xYJ%wqG2ui7iUc^7*kj71l@r59)itJHO23IWG|2!Cb(d2ff*`zYQLJ}RF-bnRhzMZ-iMVk*QQP4h1z9z5P^tKr09xL;^h?y7%S&g&LB0EUpb{`Z%fPQx<3m+z?xu=0USVi37QT!JtFvdD6HbOw2I_o70Z7t&y4>~#98aF*s&*n^0tXXAB>I8}LUVx@?o6MDKEh%#%p%?)TmKAod3J^Kq70-E^HSic1Te-NHCkJSRnE)djva#0^nC1}XAMTWKyi980wWXXz0oJ)U$^=zDIX%q0kYArNt4pHzH14R20SLj9Wp5IiF#pqsqP4zAmsx9%#8k<eKq6-!LloJ$dGP~@G+-V{?}I^WDx@W9fCtX>#&}Kkejyv9$!O{7Qx>afQ>I;s0)~JycoB624-Aq`sOioaVTJbCuVS-0u}40;So$S>h0jfXPDvDeQ2WLH@LzKIqat*eVBEvmZ#Ug4m_+OMtH;V6|mvwal)^_3~P{45l&@iaup|hHpBN#K!v{*IAQmDA6hN$>q~R7za<^V$A{;vPiC{JbBayeij#v$8fd9jDZ#R57OpFGaY9lMq_TrkwM+({LJL2d3}g?QN+N9efF-tVvrGn5Ei0*RyXb_~N(o9n(1LpChU94C27Z-fSNb+&1^>m@?MgI@g3}e&L-Iu|7c8AwV!sWdtP$Yhngnr<oKiz7?n?ED4*6QB<*0(-ZQ>1WqjX#si!>Gy${<cDsQgVPHHGD>TsW0_Qmo`RZsZBP`XKr5n<6B7vHCbWdFCD>Lc*HHUTU-uLaqEA(ZF!W1Nt=sf#;4i4b7BMsAO_mQFk;iBE~Rdr3<IT?1#2)riGafZxtY2>tdy~b$fKNIBR4*HFdQd$aJ=R(nYA_3lApO!&xL_i3iq3SwvwT*X8hoH;~!cYFZgMnvkugAOtw7ZQ>~|1|h_TSyy&Si^cWmfN*ooy4}e{9wzGspEww~Jr^B>R)IXK7lDDHMs^I>tA$So$zo+(sSEdgdSnVX&W7v*t;&DH2$_FCgxn_QAxwP_*>Iq9owzXbYhzB$Mj+4XfxHQX8l@hchp<kr1|`2IV@BC;gY=`59#sC8y)iXJBU{EpXtorWC9jBA-#L2GW5taSnzP<4#xfu9b5CHcZ!IhHtsS!#PKpDcKvj2u5;&%F$gG4bi<PZjB*DyW$;kT^{T-Vv1kWPB0s-X%i&Oe8uTg-CEX~H-TxL^uNaUgz)0jA8@O8(QebQBs#(7VEA6C{h#p?OJ`Kn_bl#A!v)sKbQ3F!~ht$fViuU>^I$6#;e+=MAd3Kg5k&S@2Hk>Li;JR}n&N3x#squ`zkEcGL}Xq_*panx=Yp0L4cece`sn<4@YhW9%Yy`Xw^*b{`s;^G7sE>gE)5^3<+2X(iou@_)Bp9Py1!RSCOR`y~sw`f@0@u6jJn+$8$wKw``xr=&xGyc#UKcespoJG<2*YaouU%oh?;ht%L>flyj?r7Ib-p7f&B8-8^jp+?;eej_C0Rd(?f$58sQP`>4g*#&-5sr5T$6qD@3$VMlndr*0l(RSc@Hr2g%5Bldjdo+opxClCo$1Qrjr_~Wfk^JlKX^yMeYzUlPulFFguV>!>H7xxJ`DaDCykb#Lj222-#DNbXt;}X9z<JYJ-1jt&awU^4h@9WJO{YQ(AVS`bbp!y1dM7b`7c6zPQZi`<?mk><)0<v<6<VT7P;#j=)37*s#r0GRk$CDPwXBK_q*4I`@!|@JmUA)!u{sGh5P^gyFwsEObo6Tujqce1p=uqxZ|@*Rm-|@TM$SNoNaMDU$Z1i3Mpy0q+mDsFoo32LB9{HVZ!L=SpY%55T?b)7AeeAA`??sjt110gg!PP@S>4bLmgQTOG<MZJx-bhvTe*01V&E5UMT@aCK~~gIxR*V$5_fYuVyB7ADWpo{Qf&yhA*<AmmSitVM8Bf8k%h=;XaF=X<08{&x}@p(1m$O#nOpy!iEMB<lYWwr-ub_V5}Bqw3!C1=VA#Ny}3?{-5j`7dkvMKwcv**tmksUw$OAqiSPA{4r^gL+xKNU{onf{jBH*eKPKk&Bjy!1XwQwOYS17u5HJjdj;PEZxo<b8GVV#Z#)xqc7Ey2TkRPBog8K@&k9(|?{K|0W_w>Ra=L?6jiv#7%t^Yj#a*wY-D<<Fl6WHu}d>pG!2h0zqIe{={JRs0+fAblV;4LWg;t8ZP5BKES%lq&SV8Hesq0(m`VR4-zW^Qo_;^V6fG}2A8fHc}aWHB&*?}Gy`f8K&W*7K8-yusQ!+VmmSIf8|)NN2J=zfpZ1q1vfpR$$#M6n+ndFs><?y&J-vF&9;<f5ha(Qhs!%lSZun^bd`t{3ycR^hz(4Ge|{r1T1WBs5jz#{SZDrO`LZj{3mZimU%i?4!KVBErpP_a8t#Zn@auIwL-|E8gevM5YB3zse-`Yib%MfScFFttck(YKR}In#!%&}#$U2|FXTQ}R8?o<9+dUiadbxgN@ubT##R+4wkn|yi-LzoQy+<YPNO@z!970zlt#zq!*>PZKbIFpJ59!aM4Iyx80b^X!4G=B_{U#bnv_^mCL`arTg}HKE$((4_055(v+-LnJ8ocLYZaz$VW%6Ft-7i331>320I9=s!r74uV8Gm4%f`8M6IxOEFr8IBAQ|Z|Zfe~TgIZ(Iq$jp7@~xOxizFuH9A+!i-q=iAZ7^53!6<mRSIEu08J9_K&}%ZPiXCySTh8Q>B~56MsF6fJP1K=e3seTxOK?EWUqFM3y+1IAH&xtLI;QeCWXSpb-+k#gJNdv+dI)pf0Z$|H(S4y#UD!{P>)PS0=OlyIGTrU0`=_5V84r38KX6?cR8LthF%^5spWv9@)XeCZ6;jj~NjGe=^dedTtORC}A2p>8Y%Cp3WgtzHn^_}-)?@nFScipzkiucI+DBEC4+X5XbX^8h$8Q%+yflwBTcrT%CSh*+rGmM~iRptXS@Kc4GCE_sUn9b+WPUXZ?%YN1wA2pr@xEfB>8UL0;$nP!n&D29&9_<nLdqHT!3a+iCrzAonEC6eZc;v2K9$eyW0R&_eOH-!ue^;1E`;V>C>>Oc!u`-$x7NOWa;a9nalV)~H!<<MYQZJy>`cOHPTiM7G0?31RMxRk{)=nDL=2DPCkj-+V;t+fcrnaO2HveXw7ik7{)xX}OntvhO#g}U4TFnY0Ggzdmng>uvq%sKJVi^ZuD*2@>u5B6$_pFvl4#N%(RjhYNGMNK*O0>F>qiZmjr@fYX<duGUW0N)+!{D$$Jy(4Cm|Wi)^fM~)JmJEC4$<Ib=e$;eV<AuO<QWf-haw~KUQ&Qt3I&++4wIV&bc3RAb`{8;NXCJR2dkk!`5#blv*1m!M6<%L;26Ad@F8LxUI6M9;sE5ziiXu<}|9BG<lsE;sqD-pS^lU{G_rhX+O5ai%*l{TMmwMj?pAe2|+SUxq7i1+LX@5fwT8&eF5yvdO!rScN{mM>;Zfl`OK3s!PEY>sF{#h5mVg~JM=vPfnbhdB@$!eWwqr+)G@>)ElPHPTh4uu*#pTO4^5sFa$QVWbPk7ZLe<wQJ>uJIsj$iV`(>?{&_Uwb1t3yg$UxGrR2hAFbMSr=_n~kxpRxe)<(Q_Fp(u<~XQE~Z<(Lf#n4KkF!m<>kP?gLOYy94Vz8V-iYHi^lK?56{g7FHbFeef?ZTjzAVbi}2s48@P4*7p)PW|{<A=Jk#*#To5pp94VO09xa;9~8q<+O?C63HJwDiLwy-xQ!S|L?ttHXn;VK}Q$1t4ufXPMq|2;=<>2IQynKEbhF~bNNzO{}fA`3BoBG1T=bfvn^uhRczD+tFQx@pJbG$S*}Wm2&jVGnR;S3izt9h%9fjr7V;Nfm#!U2YGIm@z|2VCGU_@vm1Lu05kQ_kLhxMCW8kf5Z-xH{%0f6l;NVF8`B3KI^GCLS?L9N`zgnv#FS!Nw(|tX;l2qhM{Bv?8iT`s|u0*jFrV-cd`?HWB`!MyIdfzW(gVIt$kQ=+c#=cLi=rhC7!!^+o73A6vm7Dw-TT=(;zw<Iun3giMFXoMVEg4!vGBm5V)o1K+g$Av+kDs&0feDS>4S<HRYPPLW5N4MF(pg2@Mu3J_@@XeRqp)@o2$#Y0(o`lLa<ims$p+LPFq<~>p5<WRpLtPv=m5BugdmW7<a>7;no!(#w4wL7bqxu`n*3Mv`?-d*Md7p)u<R{f-`8-coI=l67jpcNmuTb3#y^7gA2Oazj^J|of>GSOn?N;?aJ1~z>H#0mFJ^y%f2peZsciEa%Ey3_f+O+yQk&q$>~7oqT|A|HdN%?h@OuG^_kiZYdxcII1rA5I(?{?XKA#u}SXiXZpUSWBD^P@_Cal->HmtSd8u_U@dVOilsr9^)YEMy{|FL>i7WWC>j9IBYiFu0kFxDmpI>f2R{h+B|(e|1yExEffeTj3Rso50)g_fhwwOAzzzmuhUm2oy8RTbxa03n<!7!T7`7zk5Ri+GC51tS2<hjDOosYiVrlyy@NQ>C4#U{yqPxMyMghRI;+B!i|?%b?WEb5(vp2DNwvGyEk}nvUtBJNqD8Dd3`8z0DP|37&?C>rHfY*^E6q0o@7>kNNeRgM~&uEZ<Do4I9hGxVc;Kce(lUd1*R$Tl&}%&`DFTn<q)!kt+aQCZ#TsU@u?Af#0<Qo}9CJe;NV!PbgEJKlyQ4eapDpS3}D>@f}0#7OQ5LNXbOHsG$`C%EbbIMPYcrEUa`dL47zlX^M>8$&g&^1mGn5tD@b!OpmD0j07ByB&gSnUef;_FmSx}{N2cB_<Q9yTkzOzm=~S$pGMQ(JD$*2(B#FCH~Rs<99W+7K~O)uCnqO~h69t`mH(s+N&sEAgOkhA`XR55Tl_x$`0Xn(j4sFq$R~&TNi-ShsXS1o{h3-rpUHFox}%%u(>N6(6hSqSy9r?5uE^+Aq42TL^BM17nNpPykgYspAzbs>jTR;cc3uknTXViF+n_xcdP2~gq-S>gy~!rSj%kF3B`341uwYi9u~`3Da+(P8mfK)WV>eL*@>HQe3buy{8Q{xRR7G`yo6cQi{4JKRQS!BZ!FZ_q6CR^7pAPPdvWyeEqe~0h5f;CnJ(1<l!WKQ>`C)k`<(=NEVOMUdRC@}app3P1E7tOfgU`4Z8RVyOO5Uw5WJQkdq@Lall^GpjfM$d{K6qSk8oK?&JUGpxES}eNjRM}WN)l61_3+LuWRzuRb&?XtEPQ5#!LkYu|EbjtBAYjNFQ%8Hwng^Iy?8i9zmh|nlhS`Uv$S={63r^{-!{}q$sQuyrs1DB!yOxPlybnECV`v`dr~f`wMc8&)2y@sA%C)=(!z%Wj@gRR1O{?yUCEsgq_8_i@?qYun93V!y#Zkk=YyQw6MQI=mW|_tQc2-80$FipsWUeFhR8JCQ5`Ly(E%bBn~7lIZi(I!vzhlI6LhiFV+!s9ZblX;N2WYVl@b@+@L@(((m|;K&`ZN{JFQ7pdjToPA#qLqCTR^Dryc*l0UpY;K7;p|0SkhvhWg`I)4ry4shm%;2TBi{I+2c`xKo8li;XR>ZsX^(jj`c(3%iO5tBg53k`6YX)poGEWqQlOI4U7@viAuPUEl67VB{KeNo-a~*avOU$a0?8+e{@yjg+b4x-cca=*>-)<j%|lYdf{QQ$sn^u#0(=NE>IXkJbBPC@fAX1@ZYmiz`uJY86aP5mPbWeq{>RCMnqYJL+b}#?8g>g^Bl*JBf=pXko_|LqIFnIO}+oUj*`tmB#RVnSLrEUa*TTkiH9puAA0QkUrCCQ!ScRYiVfHQafW~P!Q)AXM3T-VK~A%EF#UNovr+mV6~jvMCayasG=+XR`X01dtLKLX*==7<|qDFEz|zQ<*ahdY4`&-^Cyoaj5#me6MS-ymHr0wG_2(0--$@!3<s!N-jvWUQNk!ksQJxz+0Md3xi_3g-?BmW#;yPPQps^s6uBx6<Tv!&{B<f*5g5Y=>J81J-T;gYsX^PS5bGhvgwj!tF*m`zDNuM|xTYp@gKFFWaZ<k_Ue6_RMbwzhACb(K_VI`s*pV}}gq;TTL=i!vPJ*GYTO9nRGKSYT`CD+`(5r{p9$nv6w;HMF$tV=v9wQaVG}#xn!i&3(##@$6zIMIkUwj4I+D9Cv?b)$)Zu8)j1}4ucLUaQJj#&(i4%E|i!S4|67F^-+>ij<Y${y0PTegg{rOP*<OjU(q4e2Wn{vjDB8dPQvej9~*(_~kv>gU58{GGl%gue5~9)+>4V)@-5fMxC)Y{MM4H5sL#eTz!*Ei;)y!G>|Qn;-(EJC(GlxLQ7|2wHVpJu80d7&P2NDjB|bvNtEYA<{^7rs4{%THM3clWE+mHfN1COZ$N5AOO=F7QWUylRr&d%=q?lVAb&>JA8y&wAKgRRyd$}m*SfE3+~4oZl1nVroqDNMJ?|Q`&)e@8v(<1WQCbMd?(H2uF~%1dyGcSwy|64ly$7t(sATOazoC-H*|>Iq*+Efb_8g_D0B!7VQ&ZdjvMVh*#3W0_PNO28u3Lbe<P#V8!|H$f)6<5H-;L4(H?nA`8ND@#}B@76Mq#WL@*lRUnn|g*(43h`gng5ue#?%0I((%3N!pu5l7?Ik-E@2up|bPvCEIZY0`k_jC=NmE>%=g<z#eA?Z!?OVbI;^x(Y>QdX6`fC5;b>Tp9m^>fc($fc3Fbed0<Om`~;_QLW>KkF+&=l5ew^LVO4#Qo;2*aa?BGG>TXsCHgJ-gKG9B!C%|5yfSJs!f#vAK}V50?ipX~BPiSW?D5apR1Az}{@i|3seF^-#Oe%4LVmu8-diIS7YcaeN-M5X+mAm-_p$t1%jgo(u8qKI$zVVY6$lug{P6=`plz)!@DWMXR2FQ-J({e2sCW*)*RVJZE7T#_3`o$hhUZ8m_h_)1il#_#qaGwJz@2A#%7|6DBTzH!DGY%=O~o|S@BY{4pQ@jDR;%zmi?h)N-<y1d(HJ`;c0+=N6GXqT2b-@Ge@7ZZX9yyk_8spT#5`C|N)6ychS<wyA`nod_{y^>V4SsN@s^fzm^tk`M~-!8?n5Pu8Nm=lbLx*Aqojm{1#q3vrljZK5r9()mCZ_lKcL_q1nITjYYB*>&>LlfpK>%+=}q!+hWr>|q42KO0$-=;zX2I5I01>ApFYbzuw}_2D_6uBRrM)yyPnfu7U_~CEs^8b;~86P-cHQZ8Zv2^AVExJ)#(a#T{(l-7-XcLP$^LjYF;%*%*iAcnkC@F9=%g3AXWzZMT{10@`BW2Uft<NniYZ{EqdaZ9;&I*Oxoma2_&<p>+831%6qgx%=~hZJmZvwgB;dQnHM{S&MaV@Mb8VTtny#?xKqxTH_lFZ(g|I8<l2kk_swG-+0o2p!$Ds04PoDFkF4oc^n@BMiK<LEM|<<RBPODK_QH$@MxK8V<D3+TS$xRW?+rm^yJsA+l8RZ1R5Dvl=R}6}#;7s~0b?RuRs%{<R0}{jM9#o`hVz4S{4C!{BBi!awit({MF`g&F)?TwZxt+YH`w$<bIlQ7PERDZ7lse&j?@2Jy~Tz&0o?uaD79q+fvoW7fvW1C^R_t8C~-&Muz80Jp+;;qPgPvq8QBtUpV=AhSfbR&c7|dAjs88cGdSisPO^2E+X5W#&xNSjLQz5>F)ZD*45G;__M&Z({4F^V;xZa_xL2GCf~kP$Zp8A(?}XB))$+&nqIXo*et5y!KbE!M?QAqPU14Tf=#?)b(C!0kJcsyeZh|Nbz)Oq-1HHMQ8zE2a0Jr8yy;U`ZH%7`Q^<_<Eu_r=x+?M1ml8z$U5q4a*5@u*A8xo4hqNQ`LIyxa}t|WEhE)LELFy{=akL{Qa(sntx>x)|J8=xj0_ba1V>=w!1By7T9EUEq|PE{s;i9>o4)S<{7#9KtDs#_%b?NuHaNu{caYPF<NUGS(PBGU?;{E!+l$`5p1W#_q>MD^(`abT9nIe+pAFB3&Kv!-587sZ|G3xVmxn#w$-FFUE_-MgjBccxmx%PB;KDnWukxb&z(8S_%3NWf@6?a|WvqOpW!LSt~nrV8)aTV>K3jL+<H|0v^XTR3NxwLCQ|_!RHzw~KVOoBsEYs;^nP>7O(Ja*Co8Y%iRm3bK!T#K2vizFCjBS-V3GrC#%hzIeoV)gvYpg`4<zp!gz>NOwr12!)#0dc@Y>vbuQPBeF#Eh5$j6ut!A@<;}-jV@)>rSG&fx>W0_3#^#D&bY$v(Uw$#TuNe)p&-HxGGN7#Z_URG*Yg<3Q<Qvzw&!tD5#8(~<0!iGjYUNW)zQyq^0@P@2<fQHE>Xd91&UH$zL}wY&3rdw-_+!bC=%P@kY?eE~7&Dv+N?3Od3K6`w93ojJN$!olWeO2#l1r5MihbZHy6}XzI4e@7Yx_VWy6$}?M&1ASJ`$t9vwT3yLGbsL6^)g-fqLx&_AmAU*t_+zMu6^VlZp=rXAXcTsY&At9}wFDkb1{Hz*hPPUj8BeW3K}renJ6eT8FxJjfCc*f5cL@TjLLby#qc7s?<H}?*lXlYRoUeHjOoj(>%jxm4bIUk3GX57S%L%g<_A=?<E9LFhW2Odn_WB(ZTlz{9z<@_XEL)REy}0IMz2*ap|HzjuZ;xlN?9#RTuo>_EbQx_S4jz0q#Gbq>UB*N7cLar$NGzkNQ&%M?LRPrAd|^Hy_FM-E;mF4dbVaDyT=gg+HyI@u!k(d`-ErIMbH68+uaADvxxd`6+E)<VNwo1D_{+XuIt4F(voKhiZD2u5c>{$__zmu_S%y6h#91J_VA`b@^1_oV;hgAyj2MJ)!pm$kap(G#L?&E|Lu7y>|Kj=pB2{!UOt9SrMQ8wq{U|dr$Sh>9+jJdp2*EK@pa;v&sfL-!F2YIr0VGK5!G<cIzYxnx>_!7+#h^wU`TW@1wW~+~x<aEdKMWh5wROUjvw<8QInF(*ar|fy)ZeE6BK_4<?ncF>-vfBMC$|`AR&C{$|E$5adKNs@c<xBPv#yDl`!H2kCnGw#<fuLP*{dem1YfN<ySK$U-Y2FQ|P@UM%uD>>Q_j97*f*!tq5soWuN@cJBetLisJ9C{|6HC5;JTN4-!qFA&1UI;`Yg8}?dnbIv|4pbo_mgRk(&Oj(b8EU{7!MH0!F{^mRO!i6O2TGP)p>juX)N4%=r#wQ&ykJi(TF7Y_Wb36_iX*Z9!<7%QMC~Q%i$4rui@+QPHnWVBbUf2WNlnvihB>NfXXny;QF~W;CB01|Q5zen(m?S4%Vt}^*dd6e&m8G#W(8lH|pm*{@|LfQO_hwFDaYH<x&iI^0t!1(*3lM_R7g*SX^LM=N&z>ZJdI0+q>%cs(2CeZ&SK`i5i~<s_U0AQgqz_(V!ln+wIVNoT1STxU>+!jG@P&XdT9f<$uLHtr>~pR=j>Xjmt9gBWWiiN`zb=%fLy!pP3vgh2D}YOyejvW#DfpMS*sv88gcsGBFoZ2hCu}K=cnB-~2v^SGe31%Lv?$SIW&!iCV73{k1x#EFu}Et=v=S=9ZI8sux3j1eL&c8LQuNeHX{O3!|BeI3H~%zjbadmdfJOp2z}{GKM%xhF8QFb*C*Iv@usn`Y>?Qd3(I*@?Ay<Uw6exMj$c9kB)fh*CBvD>#nt;%tHZZEcEHZ`Q#!!{pAHImb7OOh@PDcn;;M*GZQ<3X-Oj_(whmQ(z$^dc;fQ@2}R$gAMZs&<DjVXrj*wkQ|tz=)UDL`i<YX}<XuxBA~djQuN>BDzb{;rmWoE#$H_RB}UJyJ>5afFA-2>@VyOnu1d>Q^yrc7g~od=BpkpgM5*UY56>0;tj+$su;{6P;?%)bvtl>WoY6UXh=&-59AU9__>wnjhZ^k*XnLM_lS$?Ro~0Dmbc_{OuVc#uZ$ue+?YQEug8{<lPXEIr5&L`^t;JJ$_hF>fdKu;htgR-3xXDSS3pMzJ(2cqZ`>jRjp|`e0#nd7D1vW#d4h3UyfFAL$s|$()qDGFccC$`xB`v=7=`7MQrNAWO3G8q{4v6S-{wpfYEVgTr9M%Xr|6%Fv;!7gsvzum8~#Ek$SKk3@!6NzRYbfob-V`@kNpw%N}Yp>9me0T|t$JJH)xEk38|)coF+X*aM!17HPy+Jh#uR0%Yf0`SrY#N|H7krtfRZz~$83KNLB-LZKzzmZgh#qBmh4J;^h<G-)XFm~Ht*=hjLgyw^pUgLrXTZHf#@Uc{Svn<LbuxuiT~4qiB@4R}|Vp{$vPEY5OWqI7-3Gb$UJx@uLdo#t`p@qE9aT#fH~ixbHB;lQ81v7W<A^Fa4)!+%zy%6<m_c^QCD5Kyn&Nmv_DwzQ=zJH874iPQv<&#)>@X=z`<e_CtPok2jC-AytFMLgUWwl@6&`I&G2ewe$P^^1|8{Rj1V{V@4FJhkJCH^e+YD2MkX)FmO74<e;`#QAx}Z&RznFGE4+&%tf87-4E(RIweOPEaqsozZB6RlOZFa(M32Qjs)R5!glx0uSpw(O%R;hO)jA+2w33QKXx^6}#tL)In~bCbYi-z4o*@mhiHXd!ptr^<~#HpLt_79IF~N<p^HYlJRi|Q<)Ohn<8bzm~(*}%crrMb^Fc;b>lJ!EGbt`zY=-M!t6+}MMw}bZ;|%BF<DhFnOD!xU>u_Vh;>^{j}Ibdh{LfA8-q@c7!L}DIFhd8nrqO<cEsj^O*XhYp-(p}-`a5Y1av*oxZxF>i<`9&3SmSk37!$f6C_SuBdxBBDjr9doG7XpkYFYyI|dbbjh1lo=?g-7P94dX@$k`2G&`;^xj0jxxA~N$(+d<si-qo@OuvWAU#K_a%b}*wA}(H;j}U|lHO3Ti-LBp?o&VyM#h=Qkc6r-Utj1m;fVQ^d+s(Q972d|(S7#ooiO=yoSbFLg&V3srN>%3gFHU}DBC(NpK4?E((c*1566KSoPc1&4&+VpiGqV6GUpU(q{eSzGWFBJjAaw$)-hpH63o?(qYf|DruvArP$qag+Glk%Z%_l{%dbIEjIc%V!BI`lfknIeJ+D^0_8`1D_?t|7}F4dTpF~daV<<{6i{OBdYome+Z(QI`7uA@jJ@-<+Vh(#3=5UOV8$uCA$Pz1IU!oih#(8!0jCGCedGEJ~X)NHAkaI3P7pr?ltw(&0KXHy$LKv3k?QTC11r-r=#(HU#5h(Ck1qYGIF<zgZ^s*OA-EO<k;E+qr5t!jDCB$%{h7V#!9<v4y7b+HpK%>1@!4IM6~CKxFx4_+4<QD~I#_nMZ(LdyU1rQ~bFnzgA0X>AK^8l<~&NRgLiB*#PT3X3*~eN7)K7}Xc#^L#KFFGH@ITvRZ^Sx#>9AI3S+;%P`P$N+QT+Sl>@Ld^<zebJqVLbQy7YqyE3hnAYUd6C0#YH&&^5Jz@q;9ND!TDi(ks)6K77EPh@=t6p7=kGP08Vjp*>!|q!7<i>S5M~={!elf5bXfjkMok+_f?W1~@tW8zb((2bkihMxF+YeNOjj|xhgn~_^2>85-%c4P@nVtoy}Uu2WM;hyb^<D|<9JHeCpzu*83xfn`Eq*GF&6~YadB92<C3V!BNmh-#ahQYd*5AExLa~O_E$_e@GDz)Ah&!Vw>zo$p&{r%ztD}b9wnYA=@{2-5G=RS3+%z4+^RTQZhu~EH7G)5q5PQNlh<&ETlHWxdf@zV$+XVK%AZiMEc2hibDY@#2KiGvldrJ8X)F|WcdMgGOvFC&DL9Udz1ax&JUQ+ni1Vi-Q>Xo0Btw7A7xkm4(O@lP{*uJK;!lBTCtu9L_Q*92Ldvpn)AV@hjJG0Z_c?M0M2v}?_2@L^s`Ig!C|lkz$Ka8ooLU7V*_rIt8Id4}=jw<?JM_)Vr^a8c{)g)L(@08*_~s$HKGs{_^+~XrH$Ob!f7^SP9;)tv<JtNANGZN2+xWm2H~IS>2$syN;0|HnJ|FoGZ#!hS`Cui~?E}6X<i>Y+C4cJU2kS)k4<^NNI2F3YzgYbiN#XV`eTuVyh@mLF?@Wv(+eoxiK{*<sw+mGkrvXj)sVaVlY{wmS?emssPp*!E&xT5syd51q(+KircMv@XIf-d9D}NJYqfYt6BRG=9^LK}eB&8s|z4%ZWZB~&%#WzNdbKl;F!tLb;@^k4UpXEgl{u%tQI@CKafr<P<sM-+n;KWVn`Ki2^x7N_gA<TSk)JX)pb3W{SK5I@icf9-?a@iH`5|+0TG&4t<hyy9QqftE~y~R8K)GKh4w<KT@%hr*Qn@H+L!YI>e4Vuhev*&&4eQXh1G%Ej+4n052V`V6i2fcUzetbquZn4B>#ztxev6qgd)^7p$h-7R`TWM^QS0R-#x0)Ipps>QnYx11}>I2{=<RF?zQne#V8$;eZ{&+%_N|7AYKpKBTAZzda&E7Tt(7U=%yTwfkPu`&=q2=u(_hvUySrSC58^ds@zj|*H@uK-o<S2CSB?dqaf(j2r_vW^06K@Q|HoG_A%Xa;ZYw~XVN4|l3Lu$qA%Lp>2#NI|0cX*$Wf;s>c^U?ErNPm14ek%^33b>@jdIEut7(gYfynx>t11RrY-Xxn1pHG0E$(IPWs?@--<xfTeZ_)2R@m7IhJHHIzMB{BG0sgZG43g8V{<wGX2h}fL%7Ju%rfoKM%?)vX*%L#`C<l;am}Vvd@@A-ug%jVO096V*Xhh+U@+~at8!1t{@q5wTyKp+71|)JIw*AR}u)$6``Ow$kiiR>b2$OPjjCqe^Tg6S~jgKAi#|^|mNO`>#_ZQ=m;J@TCvAVY4iq3x@YrolxS<V&8CA<hY?+}=I2idR0?;Q>lKl6E=AU2S+7Lc+&49IXp-Zc(<Cpa<UtZ<_QBwSTS{_t%`<MRUV9}%TWbUp34G*zd2+>kv!<U~rOjI91j_>ncb=f$cz#@1|eh@(o;X74V9t5B?yXtJ8uYY{6CwVWs_Z03KQboEqVmZlZS#1k?=)C`wx;!u(Dy|B&q42C!pTT}ISR=M)xJ|%z|N<Wq9@j5B!A?934U)7SnN=$i?m;`Z6t{CYjLJ%qLiBNAAsI}^~veI^Ds$bC5yRwvQ!kL;`c^fwV)|+}HIO>xnK2MhWkaUt9cEwl!!L+pg{jVi-;!*B{o{WS}?qLYhQsty8jyrGc4!CYo$c01)4OSsiErYvEJfA%h)I@A$!&O-iO6?h6LRyQdM(a)Ybbzn~0R@#LuAo1mvI|mcs2}jJUS(#MEwtH~BQ{mxRpCD4FUsT_KamnTU+5JV%0Q?@AbpAeN1*0ujTU`N1tZld_@8)3`Lhm$jZ)!@%bCY;1)zjoSnKt|(kN&FHae7ZspMrYjVM@B&O54!<pVT-@=S$rM9~S6+fg{80rs>#A<VtIpIGZ+|A6}+Z>l@1DPjj2$1b|=VaV?7gkSEW|LVrZuOTuBDMNhr=O^s{&+n}?`zsIl>*oOHP~F3;o$J46A1q0dC0^ODp}g+BG2-m=8}7w9=iFV84B8}F_;5n?W-I!fJCxeuJ%!G&_riCw={bo9D8zqV<~se<Y<0fdpRV0wm(ZX!Tm41ody!3X58hC~h;2!wqp*$H?erG$VvaJ{eyCG0>R##CyM>rwa^teAsl1mx8i|{aTq2O45gU|BdigQ7SS~H0^Fc+Dh{5<2CrLpmPg8M$1&0nn8Z;!WSDA7uVG>w17Cp*7#Fhaq708Wrl%|RrF%2=Rtd*a5Vtw{#2Qm+`dP9rqMRaHyJ)Z1ag;1*ja@p^ikORH(h#N7GM=&qxPx4<r22MTO%<Y{yqo%0A<iv0I=_@GA^E$4t>B(UiMe;i4=Yt{{a1xW;nz)o$>l!6B$HoLaACTHqUpH6>;b)Vm!IA*gFG*TOP#U7?9&kT+E25wSR<W#4b&Lm-k}&f8g4OVTLX|ApY{k}EO*-@fR7~e#NC_3sT2F97oXhxg8GJ%<c&m7uP`C@9u`C+wQz8Sh`(qb869k(so!z=n(1(@3!VEjT$RUV!qQs?Esb91n3c<tF$XI-1Df<hL7(@BGXfzkj%^zHSx9V_}v2*)0cXJjhcL<=4sag?%FB#J-30akg5*M`PRbk?oxQt_IRT$Z^$u;_F!62RrAMw;QDHmP{%~aG3<1{}IO4BNyfoCc=!D*2Bgu;qztmj5Zk|y%}CA@a|N})4f=>G+YHRP@TSHEs(keDeI4YbsSQa>vKXf<Om?<X~=@j!uRFB$F}CQ#5uWi3@XjS)Q59UeeR6sr+a_=Y@eVrg)8<PJ7~yev|gq<B|@aw6a#RLIHp6iw)Cw&3<vmJG~j5u8+$h#5CH>;I+?u)MG5EaQuR)fnKSL-+W5g7yBy>g)@njI(WDXiI`QiEQ;THa)|!6rmI|A%zo06Kx#~{mW>j=EuPbiGa&AfBcN>LMygoIj2{`^*3J8n79kOhB&|c%1-*0Y5;rD<mQ+>jyVd%<za`60Sly(;0LOlZ77OyrG~F?T9%Zp2mG?t)>_oD8`FV=Ribu_)vF`df|3*!djVWVAK7<xWhSqb-xc#)Um!dA#{Q&=GoE_OE^<XaLhTcA_pXZV^Y0`h&!?omfcIy;hQ<`tIA($fq}Vd?6fVm6Dm+fdpO0DILklY^?x~4jt?vA{e)`gCD(@2?k6zE>i&ke?^RH(wy7GHpR59DBJ3Al5tJthrC0$ERokzna1$C6XjBNa$ET7&v|4UEj)9evW+Vx|VHq58@VN|8o6|DqCYCW28?U^83MO92@)j2TOI{t5MAzL6*lk(~GSUyeZlc`~uiX@)+j-t0@n&2}e9f0FkCefB(-*OH(hw!3=YDv7R)VXaL4b4Jr$Yu6Ha?O@H??$8AFY-GG5@Zmu%oTfrrd%?|Ht`XeF1w=GHc<Sx=No!!F3{jRlWTJexweLRa1G;F3IC864o2LIhb8GJlpjw~4dXI7ROf`)`g`H&0Y=U5dPMMhZ)vg9{4Udj<~`@c`C0ts>fd$s520GNX#iHs52c~Q%~>7h_j{@q-n;%l?Yi4)NB+?urAkUTCkjF2<rJk+nxD%Cf2Y4g5H>o~Wc0`CNEt-767f1h_6=p<oRwO<nud%Ll2ZvL_+2n_$tHYq)O^g(Vt}8bWTdscPvwhfBJuhI${Eo1lqMq&8$`tlnt8w?h|Kl=hx{xCyZgdH%0u1roNKnlb#U3oMD>!ugA0F1-Hz;_gB&Qew)h6JsYNOU!k)rR*awTqV~BrirKtCqfgmRr)$ig+9Y)xQ9m;N2bJIe6Qm#?bdiiU&HSL0t+4(4enqnHlW2PY>#^?Asu0b`W-bsMH6xk@mPQz=6f@C_$EV9+q7gq!n%yUVDqz0t{AA2K_C@Zf8B-m&*)XNH6ltKw=u#8cWWY(25kLcJHy9yFr`wsO8(uE2pF=;yz6%y#0dzQo@bE0(-ChW3+;8id}Hz|s7R3u87w-nIyj2hSr(h}$0zEF51c1kePgN%iU;T|0@1VjCYES=@!{{r!m#3Ft|4c9wXF;C)r=Gx3rP7PuDyx_+B_yF${va=hgv8u&2ep+Foa05|g2$@CWw2pf?+l1*U{ONO5rSm4qyKcw46%As@ic&ZLr%_W5G_T$-atJfJp~D&>>xUgg6H`5Zo>Z>~!HXgnj1zaNhUVpPsJKR)G+g(DHiW&sfw0!>g{eeJL@xvm@*7T8dF7cSE%m`JvxQg$zp-}GN0t*o-6e;Xa&4HTfRK6Ui>AA*107QOm!Aw4mXSgU6CRUm740Y^xzrb+jH>N9E>LZ&p?fD_X_D4VM>U6NO*&WeI+Qo7zSv_UX{&Rtoccd7`*fEqBBNvjJWZ)JDoz#J9Q1Kf4WzP}Tc`0&>9aDZ!4X=tmN73KyJ@?^1L+wKEyHwXF|H`yTFIOLHiV`-3}&K5f`@hlI9%R)oN(Q-Oq%B%cw?I_mOAK0im;H}1!fmTtN;4#&2`NT@~XMsulpmDa0N<Qcxa@$#!Ba+QLBnwk~5>-^3e%9%~t@LiYjfH=<~{M^IJN$>dx&prI@{`&6AMr(scVkTAgCO;r%YGw@f!z_@malMzw7+;PvYbcoQ@(_q+|CIv`?1aFTiq&sg%)N~?Fxb;cWY!P#Pcyf+e#nap^@*tF$(l=upN;uL=O6)Ouj?QK`q*AE0hzW;O}!1^vBX%bhn2v6m0B88GVm(67?z^oJt3eUD?&fLU{1!b#Ag)G^9m$abPu|Q<OXA`~1>|<S)QUQPofztCaBAlw3Ei=6ZtRC%mTy<YfvvMqddJF)EX$95O@-cY|fMlhC$jdyH`78y9elRle+sjzsf;TK(=M8(W;Q;K;fBy0nYEEjoLbre>oGnr-zFaQSzO2wl{4mwlT$G=p=pUJ_##C0Nmk+BtA506n$a_U^-aBqU3Bbew(@Cl|2vrD{m9SWeL@MNy?2(~NECuX0cp~{JBv|v9ba3$DJ*5_VH!U}6@#W>#usWmiR({}U+lg)m&QxW14L4~VGjW6;ACFZp$_FeH$QmcF_IVk{y$R}1qlv#oywk^^-ua4u_k%2!zif*oZ?hl2ES8x{9%r!(dP$2|W^KayQ~<rn!kI8j&nuk4O*PB4X9JZXV;@S+BJSIklHrC2P_)AM>^zV$djShI&VkIxPCHg<S7Mo(l~*llt%zQ+4B{7Xo_O?moCLHiiUEHUE4!7{W8D!31xL8UglETsMPLXM7V%3qKBqk&ax@lDJoX#hI&`T1_S?rS1NQCPcouqfN%PJA<-<A`ABqTHd4QT&uGF7C_cCD>wiHLhDcKaQ75-XZ(=L1sw9lxhzVtHN;$`CGWm<yL7XC#G3g6mYaW1I2ZO$W<D~TpzUSlQJn0{FL7Z)hWYy-~k!Cv^k{{HG9jQ|lj4+_D|M^L4EwL+_qrl`6%1V5tcps1RQbh$z&oakjp9jAC&>-5ohT8NA|RYRyBbfqA|cg}H8w3c96gw*X6QioMMO%UUgAvJ6Ffg!cGkXiynTBk+El&xV!)oG0@VlM*As&=+)i!Nr#dcz!Bw~N@iL*GQ*F;saU;X}lchhX7#dl6oDP2icJD#spt07&{b^7?8us`4Xb!?^U1*zP$Yn@=h39h!a*9w5BFVf`XUAGcO|h({n5Q3PpF0*ut)M$4vU>!GIM8FEyPVnj-QNPYvJm@0OpIY3JQ0HL8J!%+v)=6r8Q0^QIx@BMM~GF$n^*8^-~8?oX%9|hb>&$Te%v#g0QX5ZNw%pZ(i%4J^NjZWi4HLcy?)e}QKb;R3h9u}(-0$f!MZ74q=m(v6ae{y8J=2f=#qSwII%aIJ(4W?^Ih6egy^jBeDB-!~B@5JJ26t95C#|hr%Y@)Pg9xSksBCAN&8%K2sw<EHWm)i(snXr3tubT-@AV|5N`l)RAlz|~N4LQy3IbutVF+vFIAWVX(5VOI7G8c!TYIae56nK`+?jQ|YPG_j=s?K4epSMv&o)uTK4RHm~g5s27_&ysl&dtM2!bMD9<orTb*50XkKe=F3oXWUTX`^duiuZ<9EG7D3EULHGF{ucoOyMghfP~DDRK4WYruTb4waXmJ^h~KGQC(Wd{8Z~qAdKAmfp~MZK;d>tw-J7oe?rT_E<ySuK_1YTzGBqbw#(jQIiFI*p<0{;z8Djzrbk@4v!AK~7~AWjsi?8p>6ie;Pt$bMaGgnc-2E@FaAa&G%#N%@N9Np-RRx>%%2dAoW}+?h;x(n#s?c{HZ4s_$o!axVK9G+ZFRoY{iiOzudToeRNkT&A2#eLLDagXP(NiBZ#<YyEya~-k0RuSLuMYa{B9$KtN|;Cjum0P#d#KH>RWPw>(Q~CamG>fMYe^m0a!(f?(-kY*st4#rxZ*6@lFwT4f4`^f>@Qxg=>z;yYWjjw29)(-!j5@`Qm->V?HiT#)mINYRrdEN>-SL(fEn#hg?J8}<OA3K3oT?8_Y>!ggaEXPxv+W3e@D1`i4joNFt5IbIx(#v8wi>Z6W7-L^+WXcJTf5Gtl&45=>(G=8GJ1bMTJ`>bnvZHbsltO&_d3K-6OYRqq>TFYElv>ls|<oD09Y|UsUHMV~y&{M19z|Kvb|L%vYy+P_CzLI>M0t6IXI#%%J4k^~rMvg12!7+QT{9&5!ltmSRNar}F0t9)Qa+d*O;K<Aj(B)e1}%DzT4)*Hy)Ljl)im{N~c8Xu2zZ>Bg`=p=1ye!L6MzuZGZfi=56$CrG|5ni2M48lN|2gHTzHUK>{xi`5LrWTYtSWLmtT5O1`>V7rb;><O5+#FF&U^yb?#Ae#@hCro<Tdqg+NKqb!4Km~)zajKH^QS!o7=;DN(t|rJ|bmixy_)hE72D44FXiW*qjrpoznd-$ajR2gymfqWVyokKK6YQa&@<;+uVjC94B^^pppH$*=5qWtI;Wv%n)ChYSpd%XH1f?a_md=<q&LL)xYMh{4IdG$h2@h%~!WyeycBUBry5C9hzW5XN+3#3bFCd=+`kU<hV7&5{I+d6{2lpMr&pL9G;o8Y&AOrMWk3O1p^RZpx4e6H)-3GYUIv=5n&T1Z|Wn+(9(k0B8roz_+ge=RBIVbfPzA_%$#Df46Mrh2)q92&}7&G;V<_uVk2f~fQp>%#06$OLYH%_A?ENn%g;@O@HHme+%0j8)kM?Bz&{p+0eE&*auO2(d{v{ycX8m7TsIni5B4pq|2rSdiUx`T`FL<%EVfS3@NQ3O@XMy8pFDA@C$MS&~ikOI(pum;5PRG_)8gI#s!YyiHgRC=qz<Z=|J|6%p=+@mXrM>eSg(9(!aYVrv%PQ`5Vu}I!B2Z#kW-Kk1ofFYQtP?+K{R+yjgUXXB($mtyOtsEW6yE&LI!U-G9H)4iF4lN;ZN%dllVexG%4)zm&D3g|-F_dqac?FA$it_F}<US2?co!y{5*k+yG(+9ycCL3bE_p!<pj4{R%~WoM0IkA<b2Ebhi)aRVo>)sJ38KQT;tGX|60HZlY5s~85|2|woEqpWgZ~*)JUBm*xs)@M!E%-#&0jZDw@fSn^a{c~>$-dnUW`;@`be}Bn8NyMKF?r`hck6fTN#K^SM6uc8lypIXMpMiwpF~@M8x!;{iCaymI#a0E>>}3aRT_`ytqHoWD5+kz)}P2SnjjxVRE2y2tYP?(FEm)>GM-{jAV}mg%!_Yi=U7wWK{b3jX#vu+c*ubuoRJZ)^{|`(lbYMHq)}fFg3Pem}xD-7t`DekOmbuTgk#&BP9?cqAP3@-@h@yDL`7WkN{{pAp0^Oe)%Dc`QNAEi!m@!1s$LN3)NrAS&!QVclcwhQV;Gp#yv?w4*WTOm!@Nr1682f@><HS0Yn16+S15}4Ss(pz}B!8pBL=RPg?A7_Nw7Y^G(V(@6#>J4OD4-bwm}{kFEcV_U#mMK*TTga5p2+Edr1udd(r_Egq&n<`5CcZ!8Xp!k%2!mpC#%z|W3)9cP}m?gOcSJNkvT!E{s?2%n*a$|raNpaSPJCV!}H<}8P1bpQ-G;k2u|@%w}*2E=*|P%sLYp*R}cEvI6D=w!jmH*8DNH4OO;V|DzqHe|H)u_~I?2zXoi*sU`bjO-gyLm!(x&k+O#npS4C4D2+DtchcFQw?2q9Zv~Cp7A>%l4mh3yF1Qip7b`%-Xh=w%b+=J?kb>%P}kf;-vHB+aGNdTxsH7w4mC%b0ND1N$?aIw+8~gk#tq4cTg}OV%q9Xc!n)~>o9dpa?ZGo)sbbGMEd_-nfr)}tYp`&cT+O2Rf9kEqn8ipJhIx#c5%q~k9mI-ZJTX2r9BdfS5ftpQDoJUmZ<HG3FfD9u&5IvxEJ=BlCwnos*67F1X2SNHyuL}0rJ)ZFv!2A|a0j=S54>lUnamAJ6A&cloA@ce*XzvzW#xY350Hj8*hqe`O&`=oO`MQJHzVOR`a_PZLLWkV;Al*=1R)hBSX5Pc=HUjfZ~Z#O{lBdOv*kR%C(pvJHSxg|POa)4ld8uPEH$i`;A`(@gcaU^iAK#c`_-hJHE<9?FOny<eM?PdXZ&aLJTpV8i;-qR(!~1{ZJ0Th=A~q?MPPn5$s7xL?RZ9USjLz|ambk@oAYDuU^T|Pv2zQ(#yypdUkosNUMzSR8h@J@AFf81Dea&nnX87o#$eiy%qru6H78<HUj~(f-zhqdWWXJ)P}hgW#4=an8AiK3qbZD<k-{C&aB5-D=g+x02C|d)-%@XX_w6f-R}n(5sw~#45v6aevMABP^FFRfTQQPfKUP*0v*9bsiY~?CaV~3$=-Tq?UQkw4#qPFQ))bu;lu0p4N_K6vH9V-)6g$-v)xND6rKzUK@re=Qo>o(gPt+9a?EC?upB5<#Umvcrn6KtHtN+lAKPBGu1oqijrs<fC#m|mhp2#F48f(0!`Xd(GZuw|-jD+e6^e211;XuR6kvZ6F#&DRX6<<PLH#-b`so+vTMb`e_-phs}2#(DB3U&jb*moS^%39PX1XUfI4>?5p?rF|BZ}_D@+~Hc-UL^?%4~q%y5%bFETq*?w*9q?WkMf_&1vX?dcQ*p3SmAKwcm2|hQx#J+Lh*6omyKp^`2Jt7ev52Jzrye<-&Bm-W$#A5r#)t?`UW8v=Y%AsfjV4&!}S+)uo(wTspl9k05BXi!~t+YzQ+pB^Ok5wcKJN%pl?uf$}imO^~l<rp-8=_T7CZIGlE6wr5Wyo!XL*ymcJ{%`03~lC9}<eKznP-e+0+))2Y0Ut&5LDD#pYXN<v5i0u!CQ%J(et1<p<AOnClE1v>^f*bHpDix4gt?Ns0laPVKcf17gk?9#KcnNuA<Qf+~D3@e~#v1~-qpgQ^Z$6K_-8bUJ021a9`Js7+j8k}3U38VzUxC!dy48RrGWy}2iDZ=Br5o=0K&D<PBv;#?B0g2|goW{zc@gXOHQ#d-uQmlW|z>);DKZBJTk%bT%&9aSu!*G<XTlrBAgHA*HKstb>azeKx8ku~OAruh`-aeoq8-$F3jYg89!M3xGiNaNmM6z3XV?b7l5OG=cqyvrlS}59SMX3PrT@pOWYwVR1uH>lNI$`vpGV~aQfFbup^j}5;@d`1glGUCeU_R7N1cl(#q&b)v_Gz<W3wR2Hcr*|S;i}(AWQN__mbJ72YYxpw)mnkG^6^a%D!owwOJMK{--q#!pL2Ctkb<nV`hl<y*>Yj}F8&;PwACk4Y-Bm6E{)rh4cC#Oa6pjym9I9m;crA2NvIGY={y-WnSc#DY0RG#p}3KhTBY$PJT%}MvsHLAq0T@%0Y~}9yonJk({A(Y-i0G5@i#(%7mYnO)vCt<(G9oY6RJX(#~UwTJ^6D}%rXr*067}OnOs8fkS@rC>UN<Hsj$U^Dm)gZCttAMMk!Q+7ZPrUo&-yUMyRR__N*T(Z_7&ZdsM%xjP@j!w{?%i-y5e8Idl!5KG*rwXb{^oqi_?-%tzaZdB0vo;a!Qs)rM+VmKR+NFpn5{gWu^2jZmk#_>vyPSSnSVIBg$^#RWZ@V{tm=ni0@2A$xd#T1#o3#5{MZnvq7Pnl;1gW&AzB3*)Na^VH;@wsoEJ_)i~!v?}<XW_d3mYLN9^Q?49Be@8SLB+(E?tJ|hldrG05MsixNrK%vDp%=+zxF>X#v32$tLv48GHi0?@XvCJI=?%>xC;w5)CJL+B!$a()V>YnH>{ZnSQ%ugFTaMD#N8cno%<jlpis<gdTEUfG>#SUH<r}Fg^Pc_MySZmowg8~A8JKXVkeEMe{OJ6)<@4HA^KGkb>l)&h(7d4q{K>Kmj`ePoK-a?ehEYK84!^g`6gnRV;CT1>G&VqTA{9QNCW0GwAG#Y;hzS}}L1Bv2Iyo}h1adQl_BY<`?O9}Uc9S%AGu<Z+eJyWQx4c!6_^+q$R&B#w>l?<})M$n)vP!p+2W|j2(w$>btHOf3f!)B&_?~m^UP+Qafg?58wQtNQ*%Ul)XWNG%a+bKkCAS|{D71lkJl}}#<F2Kz+{kJqdO+W)(x<4fcPB<Er>bYH)gOa;2PDy8_-eHWqsC^-j_-^d#c%xs78|tJ@-0zY`VPnx;>0*N+*34HID{NeA8#0y#z0DH{{>-ck>9S0HragrrUn6NtPI-#Fwh3uHzD*wMC3bfs5Pc5h~@EDgv`TWOo8w+dy3IS!$Y$^=*L?o5DKOC{L*Mdvr%NH*~%yK3)B{}j*JZPr1M4H_`=*^r9=PSr$B&R>B6bux+USLCmB_~;$FzWLT5CR-#LI73+Y^Iqd>Tzqm>6RbU$^L%0!|g>Q9@jouFJI-Vi08n&WC8aiNY{>Oog6w@P<Rr7EWeMKCyor;<jn{#g0NiURhJx}9o6RYgyby^jJ-6pgpxy5j<>=ZxKG&yKsb1dAq{0sNe?gPS7N#7^ys`~eVj6Yj2bnZlwE7G_2@Hw{UOKSPsn_N5a6Q2|}pRZsLvenAjaehCHnra{Si?xZaak}q&3(lC~uu=u5LqWIb>#tJ$nMG03e_>`n@J7Esh2<7&z(S%<vlFCiZ%<}%|i~_eUq(gpUMq1+rmwij6wLf#Rv;-xF`Se1y(14hUZ>%u$fNm#okKX!_B-Sg8VoRi=VLU=y5Z`dgg*U(b7+aC$meuSuK=avhsOF5Ys39wn2#dx_a=GV3hM<Ubb<Mfp+LJmKujHel=Ygq!l2~>mcWabW>5Ea5ilY6d{_0UZ(*fmQh$8@if&Iell%+9{_aRO!HEI|;+#U7_1Le}9%HI=M#<m#8jk)&3ROQ8wzTh3g<TvkfNqvoUs32xsD717l@4Oh%S_8xQ^8R3rW^}U%2tr9;T6=I3HESap!O%x)poD`u@FIU86?$N3EaeOseEN--a}XiOxj<2~ma)euei%E@auAWueK>&`wC?gLb#r@KmV69m8!TZ9wwFEHVaQSq3dU5S>?rSQkp7AEZ4dYe!IaH{&5iRbaheqnw3_p!MQx?X#w(jb<B_pNi6`3fb4FBKLL!9%!l?_FoZ)mQOThst6>Z%bU0qL%m~LiUJGZTBrE_|#kf1H$1WWR`>EBEqw}xB`xgIonXdsQL1zwdWwXm3B0xOrYpj?!SVGolBDo$mIbMOXo!0~ffvVl(z$uvQ#$#tm@Y9<w=b%y_59EV>+Dbj-6u!G3ujG?@z@a9lsU}goIY^Y;A<Aq@H6Ny`)77Gi?xs{iiUZ4Inapw{CS7_U@27cqE-PJo%mEF)32jn)$k?+u*OnXLl!ANl7l<#5c4>bo9)n^Fd;6Q-AAHWB_VK694huy({92j7Gu)I-1FBo||Go|gu-}QkG3PrxWy>5E8K7%z_)kMs;qTl#GK44?r+*U)$uM3I3|51MDoo0=~{uW_IUA{u2<Xz{#JMgS3^H%K;NF-Nk8uXao&0Fmts%wnLtg_udcok>WtBW_tQP;&APg=Hh<tD89r!OnsfB@hdDBieIyzyVJc%$6t{Zwx1Qn~TV%1z}daPeH_#`{}ujL-FA8jDRn6k47v*i1|Z6fOSHoHgxNFZHJ=d<g8dm`#dUk2aemLKGMd^67UfU$4fHf@#BKhc8M!mXaqwB1{dJQV>KWT4UdQB1Xzt6!Y?Ks-T$QQbAH;Z%ywHh2%9jBct+(-?^A0+S62Ol!)9EIZUf`V%|;SXE<82;`J;rR5%vrW14!AGo(oECS{^Cu-}wsEb^0}6E-cLSxqfe{*1YGl0ze$Wg_(S^Joq4%<>y&p2~&zRl!?JXOJZFQ%Zn|qxPK7vT~O>&%*y|^ZFIC(O8^&w|J*J13mg#E>81HsX!dr_|ibvG@u12-8AMjdDS>;Ma}ui>O9vk&LVRf>p~1LQy{u^9;onUna&BY8Vg==<%@lo$DiDst`LYZa;-l6A1{^;Kt*Ks8QJr;tSFG}P;7lO;h}s+jsB5nV}!I_4K<Lw0d=HA%nG`5<V`T=Q78dub|0DP4RJ7@W>&k4w4yl=u`s}5hR)D7zKkL8m{LRoA3*+=w#*&Ssj+oePZLmdKh%rN@7a69Vo+~~Xobycrl55Sz06_c?+K}(ZK93i#bDmci3pKHypvWo$f-S8V*Aqm?pZxS|4pm|20tzgO2InO$*{6;Y+6nEY~);p6wF!Tt&uvB5s@@JLYK_MCiz+LPIgPZ=?=e()#PR^2l^pB$J@7uyV4#`-%xuP__1|+II2BdTW>fzrKIPL;dr$%9IPwcmE`@6Gm2migI{S0r_vHm--4DfsPBV0zVx!L@CJf6B1U%97O=)}v@JC^hBu`#91U8(Xbfv&LcQVIy26L+UE$C!y29~lSGdy1k@be%Bfa7KSM-L3aCo*iT-bxYCGFwAKDUQ|@&at8$YCTsdPxqmKUbESd%%gKJeAwlYd26|BG$~%bh|1AlMFpe8YbEiwlA<K>KUkpwI)dy<Gtl{S_4Qa>io0Or?~peW7$><>O17x5{S`@!Fa(c>L4uayA?J_BeE}O%88v;x~4=vHe7F=Ut4ySaX7>6rI^;6O;0SsY)b}!+>&ux9Yj(N=>Hl)8Pm+l0PL1CWn5H9Y0xoE*+$iJ-<K)>gIN>f6NXTaz$8bvUSemtYr;K9l`uF4y>?104rkZ{QhqGpzgw0#NeILYR^yZ5JcA9&U{S5IBv#ZRIsZ#!q)QUeU?+|r0X$Gs#7PVTR5g#H?!`D60~&sj+Oe8Fii|2JS|i3Gg=!#xt{IFJ7@#n`WOUYFfr_BFf@#iXYxXw;fmJ3v&1@=n^<_p&{VP}If@C@k7R;z3fAE$pJqh|>oNNsyWE2bZ&e|xL077Y{7de)x5i$cyjH4m`4%>a>jRPltxE;>H2I(?)1=+P>48pg7V+}#b|7DB!=A8i7VLf(FV%J+d*zIeu>u!l%-_GUT#y^8#XC(|l$OVEOqYs{X(5%B;BG@G=gNc}{MVLL!tBsLJ3GWiYKCj|ZT6qM--m068VJQGJ+Y9}zRQYBqr@Rcro-Tni1hGdZ)lFq~2-MuKLa>9{76IYlt$eVItmB7T)PHv79QYLqNp^)tcnDm@*oK@K0^vZnBeIpT=sDrQeFQ@WW!1J|z5#<EMzZ(bAIY~8K@A*lMfF#Rh6mqD+?fydBTTrtx^*J1K;trpu7rg&LBa}%!qC;p#&MLKBLiSD0Ax44g<HR6{MEsNV8lwjBXSlK;!0eNqTunN;uJ3T!HFVAMm6BVhSMxNgbvY}(Z}jIa0pxVkbK|%w^dE{^?t2=x+c3+6S%0!w)AL>ysx>lDW`s{CJP}cC{L!TENdQZF##}lcoC0!8}p|S2nYYk3RC=AC|+ja*ZNjk88*LfPHpmNVE&<QTC{==;TZI2L^K7$c4C=_atyfQ%bi*Y%HY&SyaFPnU~D5ek=7c%4Y48ALU5YTf}BY0HAs9c&)+ixLzEvMWf-|xPXpXUtL+z(5p!f8av<Pw2Jvn^;Tkj<5XPOR2T3@x7p4gn*q-};__XTw<PkTraPIJZA>_XC-{<T3$wL^f@>}hH)GfGz8vk8xT14TL0q*r4(ucE(L4uD8LIa{E(a#>_2Y7$O)e4XvD)s^@;td1o+C>nazjtp0=QE3jHh+G-AxB9>MTAlU2Tkvp?0QhYnB7Z}h>OS?mT2p82E8xV&=VRHRvtFQfAB?}u)Gz2Ty+odY~ju+Ovvdh@PBt4lXa&2fiU<U9wS?_{EGyu@%x>9B>N?R8}9KbyuJ-2V}j>-;Hix_D0@9HXGJ&b4r~8G1-=`IvbMYvP=t8EFF^jBtaIk+$rJHmzHo@pz=iyP1Vf7a-ueV9I#R(e+qir(?TuS2<2}>CDyGu7zmHapY_DpsT%DH!6Fs6(2#?D&%+L;mUz?(Xma2&fK#V1`8cY6gpTyj5Ce%5j@g|e1^%F%7%CV92nZT{YS)v`JWt{H{ttn|7qIv?T?{)+NNH%Ffie&%}(a4$B7DS|`V5>P-JvH>4r2~=S7(;HICyTOG(IbVRal{l!D5YyMzlDX)x@>PF+#t+p8(e{8kOnuEODKo{UvOI@9E(P0eU<5JD$t0Q(aAFV(lFzEO&O9=&{hecMfgBX3Q&b{FysD?c}E;EFJJSbw!n2*-qBnQ*EkRsoXrYbv!a^#!kt+J;%l4tJ7?JZ`Bx7s-xUsvD%@n_auYD*zGWMiooYZ2<(JrX-%Eelwv=vj5Uo~^PNy~4x6$N)G=D6DnfBlxBH3{&6J=I7!{NTrZTzXjP~VB8%ttQ%yp#Tz%IEv4X~N;wnyNiOPaJEejM|qQEA#IURJie#jCNiQ!-l#R6rfShoJz_LJWwRkL|R0sL=GH}fJt%x*}`PyfJK7U&HlBQ+Uk3pL)_A(JXGNxQT>r6^&D7gPeFBo3I+`+4)=$u@J|G02L9n_o$xz@d1M=I+w7jh<luyCp_N%PXh2Klfc&Oqtn#I%uc1#yo0ZH1r#q;eBp|Fqa!WkS{IA`c_e&3eHDo)hhEe`SET`!f;H9(=l4pv_@PF|<H2Q^N7(2vw*vMxELiWJ7JpH&T&X^2_MX<+`$ND92G-Cxm{&U{w-GVXNiF>M=8KYsy7wQ*NyN4<#Et_&_qKmGn>83h{1iz0?Tcx)CFblX5#L}^6(wKkQpq-yY2uv;8E-XqPBUz%o^xJJ757+W%s^4+r&#Q+AEHV_gA41?S`7rfEhy)XI1QQNq595RcyysZtNR7ASiBuJp|2W5YcTi0b02&UqBQ<v9gpJ~>J=$g21A&^YV^Y_NZ4a0GC1=>FID)(WQ?6sM^=_+Mz9FyY{#Jv8Jld@>T9Cjcve!qMzx+ENNVe1YtlE6E4Oo^{9<w(b5!OJ4+#8J5Qwjj+O0HZ_&9ae!g)blBY%9{8UgI+V&)3Y*=E~z%?XfGBM>MdzM+Tp2HXy^3gHMa%O_)+Owi>MX*z;tjvLjRGuCrEX8^vu_GBnwij+&N*wKtYhTBI@@Gc@iBDyKJW+s8t(hGA_hM2p5)oXRE$2{S&)!UQ9LF!g3?DHgsP8{(BXT*(Yw<5t<4UzZ?9HxV9VB&5@!YS45U=q?&wu`wM7b8z0+x2?LK|BdASNTviP)DPi^O{GSB&hBm&uo{iS_lweG{S>UmzVXACCjSH$cwUA-V<Pu`L~;3|($8Fz4e!s0MgEeq&tK9#58glcx|PWV@VBW-z87MH_$|9nybZrJ9QUqb)9FP#ha6jk&+?yQQ@e(vVU5jG$L0<{^CS2aEc=z|d}Ab=1WLcDiD{hdk1C;dF*ltb-yKU!97czwjO2*yrY3C8Jt?XTo*~ESnplHs(cXY<+#uj#cB$E(kWSL14DCI%-`f*R@-0%7z%9Ytu(a)9NZ1s~k;9hH^>nYg3rDSE)lyIVb7v``!CW}})$yr+5Bla%ulwG;f+GJhNfX3+sn$L=>b}b7b#spj#EAZo^Mxfd+wQ#hc24Shyd7<|qeP)pKN0M2s<D}@4+DaK{5ktpj9bGwB~F=7#too(D?eGkG)x8QU$*Ht_`+prDNz}twQ^Dq&@nG!yQm^Lcg&YcKoa{IuH9))iO#qNMPD+`2YF>gO^5^sYB!LFGe7K&MIF>LOfVyX3=H{z`+K6lS+7M=ac~g+<_81Iy(zE7yn#<xFX_gO{1n@&Z0hlYINQPXDaR<hZw)up52}CdNyy9;<E#Oerx%E1_|+`zz*`Rx=$g6XOz^8?ikjFQ6eM1KCtn($1ubdePmZ?8V?VV#v2s{c<;}&|d<k=s@Cv2hNm93{!aFN`gLoPm*AyjkRqTMfXh}iOG}nkN)vq-~Q-#u6sj;V0V-E_KI(kP2L~aofZA(DZp?-iv?bo(dCooA^<V6<#_N$d#*QnU$=?ZMVfbG??!U7muk(<AMs;8J9tH5rJgjQ@>OJHnV_qf?abalLjjjeSuGat((Ft&XT7~692R6QAvN~}<^J;UgMr39OvBG&2&Z0w0WdAGrR?#R~B7#NmQ#KbMJv~~^sntUCdXn}JuyMMWmhCvzGQ{a?MzL15SMya}P-k*;SbNldJEz;6HTmmkpHbE?H0{>i_;E6@**NZg1#Uh=i@5>@hZ?Q<pLLMh;#d_|QMapK8+USq3P<-7j*C3at0kx67CDG1%u>`1~)l%_0Trge*2GMR>t&8#(H8~K&)<z@5hm!owC5@2c<ufKB&ZKUgFN7(us!22z#x3OB2kayK3pt#te^R9ZWQO_aH~fj-XpLwatpo`1R{cjvHS^PnWatSWJN95IvcKo|aF7TgzR+Sh6D0l`@Hc?A#(WR9p%AJPvw~i8PPtVLb(pGUW+LZ^#T!vKv0UHlbs1JCDig$zeISQmB(P1I#W;v;P4+-o*%UHM6;&_@(j$FVa3>uW|9hMNccdID=}85?-H#G(N0tr3U`@&(r}sbL1Y~_n@)s7MG)oBiWBN+8UJ0{~8wA^=1r0c3lna=-iTo7tc^O9x;(O)&`I9fLUp*izV1Um073kmdl~k0B_3c!T!ng~A5tfx&@;%BY=l|`CByJM#^)ZLNY)_0RD&RUGvz9+1gdK`k-X?Hx4L{Ed^j>WUmbUiTw_h3lE+jD|vcRlbHiF5Iag#o02gLZw?)i$oVpnmugD9Vbj6VJ1Mfc+X{UMnM<R?eWA2nWvmlC%*{i#D<b09y<r!=sKsCjXr@^c&(!m*}=3nFA(N@wrE=w{0v1f->seHQrus!5pMOc-ZSKRh2TG$CXQJeH%?i024>!Y~ASUA4kK!v7mUR{?edt{k-bz-#lExV(`})QObC<3ZBxJPpE4NayC8)=%%r9;c29D{=XFCt(xWTE-S{;3eSe8l4HU_KJ$_psHwo@v`7~U1zx#JR6>?N1oWsw0AHm#_T!yF(ROrF>~G-3AqbFDZv!|rs|+yR0q}aPkSaLocdCC#a@?~oJVzF7948|`(iSpaz9NBjjV1o))hIi?JUI?jb79$J$SiO?AM%fj!BLR)$;l-N5#-0m-JO4_9hz~9ExKKEhX9=85-~%f5}ASPcXpQJZv5~z2BCqYrf?Nj0@NKe|PjQo|gEQ$nSg&yPzb10Id)U|F0)mfmoT%43oeV=@vk>9PIa|Cyf~R<ZUp^xgsoFxxG4Skzoo<!5u|^(!s}tQ2eK$hg6xlq8TH6TEd@YywHms6&Mk*WJh9u`Pr5oP)1Hv4gh^FN<M_?*F23+SvDYex{8Bs*SKL@D~YIb660a>=~Oi5^BayfTCxxf2zh}UwRL{~fBE7ei|3QZ8OPXAE@fs5aYGW#9Uvd!Ol?^BSqdr{epaGrxZ9i=^B2h3migG3#9}0kSy$pT-Y{R-hngDG1dTWmot*RnJc~ZM;ba*^S!_noHu-`g30k66`%=-kK<kjO^^?kbjib-xfQx7xd<nf+yo9e!u8F4o*eDX~5q5ym^gLZKob2rarv+`sSQ3S`qHFxHCB47)UK85o5)-=CaiJ0CVAvwoyHsj9&uj}+b|r58bXqHk&E*<INg6ag=Sjm$(%S6AnrD)R4FF;#X<%l%NE%RM!u)xeV}ClQz2!G%&r(zHXi96-3({J_)K<9yGh5{%<mxGDtt~MD3$L}Q*9$hSwD$baA&}{erVv->e(UYbQ+-2!cVcYL`IWRq=L`>=NhYVW+@Q1xN-{S4WT4?FYZ+96^3*T{NpJ(&oElu<%q@N493iT-=67ku2^mofGf`nU2BEM9Y;^EI;vGpY(ED(u8{A5I8j)_irW#F+%vPW=&AUKAW#9>G98W|95*SJ32XLqiD_IRCD$XVkHT1lmYte#aL(`gY-7aYUL!rHJ&sd=i`Q14_$a>Lehzjh9jlZd}d&pkuKQYPDfN$I>#2^Cc_dk5Ci<-($)AzmOGQ#-~_*<0`7UqCpkMy-_U7_vKlkZh1D0ab3<*uTgq;N;@xC;XT(-0@qfFfr;^SM3MgoQM@48)`Dsf9H8hZdY}|NfVzqaWo}Nl-UNt*Z9qMs(xCcxw$lwqsDNf~e;PQR9|xNcmz9K)mf0x^a3@8D_rR2jUxmV?&;aHURR>P4+wZE7HhYK02pt78nTB3hy~=Dt~z5UkQ&eI`mt7Hs{F+__mOrh}gtXP5-YxOr@_b+PQU*%Fxv=b6Ps>ZZT(T`;(iKU7NJf1H0m}^U`Sz#MUqO=eTm$?Xx?R^31Ev*(^%Xlql%Anp^d7x!VWsPcNta*yi*i|61?QAkqcg)oF`%uiBy>sMUFkW^2FbAd@@LcIoMf`4%eWMpMeQvR$+G;eD?`#=xNv7yr8#&!4;?zj%gM-k7v6#lca6ST3L0yffO{8bZN(RK=>N5`};x1EPT()C(eA@$JS^bd6?nz1U)5Q38qg(vpV-xG^#nkEA!ei0z6pp;3x?=!B8_eK|dnsP9xvcUVq5d0TO-L6N#fWFkDOxA87KMgt8tuHod=?PB7o9wZ*6_VapBWC=SA;?4!sQ1M)n4;uCH_n3hElWNlszcSOBwQSHIWwAFjO!*a0qqk>oUkr>@d;n#8@MMSt(ulE39o@LcJ!T&hMbWtTpNVFXAnN1ZZ^I-|X839&9AjMd8ONpbq8d5Xxeqo%B^kJ!7aS=e`!Q^R#4&Jdw?v%4Sd4y4)#AL+zB;k=&N4wH{C^}@V=I@T+#Xdi$1#W;@~~Q;kGw-b-bWM`Bi|V{J>q$^U0_5*nsmqKzpq$8Fbk;8R{UGlvjAvsN@sZmJzXIS<TwmXarxI2CAVDAslHY$xRi(JobI}CbsEuDw|OyXOGJZ&A-s$~t38^5^h*ZP+45sE$0fdq34hti5^mMtN0_*IST@&08fz4$+5@yN#h_}hbOZ6I6o|P!7_%iTw_x*<Vtv9B3lL6c)a?zRY)Z-0voYpRIt~r2GwH;zL(+V%iTxNt>C~8(0ERHh;l}Y{$<33hhh?RF2R?aBH6642Hu=}mDa<{}2&w6o{_Z_({_lT#s20S;pPppmZysmjFPY10$oN69`Y0KHdMh&iNN3^J%nR<DBjZ1#U1%RC;}`A1sWuR-n051qzFgBT2m*|y=L8P%={e?wk<1I-nt1_nz}F+=@5w*(BEkj#BC3TGKdTXzYlI5|t-fE*g@0l-fmvUh!_p8|8NwXz<3la@J(I<))!#9_^eKj?REytpNHXn^#ULNp7$z->2_~Q#4%O!aX+Q!ivPJB9q)1_4xxZy2$m)B+)T2R6D9?)z66M=gi@_@ffWgLZ!vo$4i0>&xHxno$hCZ<5z(A}$0IG)_K;dd{wUiJKWO>&2MwX=q8^XX-I)pGY?YW7a5Z3G0t3MZ7OgRPrk&^_nzYFn!af(OMhWh_~{GKKl9>VFC!J_93!9DCeG|$*uq$*oD-k8pvM5y!nc(^q_D+2h#{*H4gTxy_F${)EiRhy$t_*hwVe@p6Swh#8SGP{$wlu6y75Qzu$mRaJk4<*ao--|psoIXNo+f%zj5L{DM@fO1F*~rLu7Seksim~JuPh!x*W2`}FNW3Bcw8fB>0KKqo*eZYS^<yV=w)us8t2A?RgG)T#1lqK)IUw8zpu!7Jjjzp5eWOQ>Ne>N~h$&GR!0ITv#l8PH*^J6~KoYLdGkD5CAN)fyZ;3B*uG{+~!|Zw<R+&JYY!n~-uM$#uz?Z6$tM0d;)1f)|PxINbt9-hZ-Yuw{ltZ;SnH%up=Nx{@AFNLdc_gyw{g;M)56#hAzn^YvWe5JFx2YO5P;;8A204g5tV;$ba1P|xbB<aI3e*w@v}Br}>jI1gz5BS3UT_0qt#_k18-+Xsp%--GYw37{Z7rMdLyp+fMe-llIe&w=J^!-V%!B`<a~l{y^iO-YK<;3E$9FX?abV$nTM{+W$L!H|hP4@zQP|-d8aNg_pU&SR6+;MH6F1rHj0CG)<zbwD6q#)F2TQ_m8?RN)G#Dqhu(ask9GLqL-zm?;vjU0Rw-87a)~Pxdn2X`v@l4ofQ}dKkVywg_f1PJy`&ym}P;2|Uc%5gWeLc@aea15pE&S@jH^4J-@JqPkhbjKzOaJ!|h<ilt>j5kyy+B#fEa|?wVNq(Lk2WlltNmldwW1vSdbmd`iy9l~x`p{x4U2X%rZYa*EisVMt38EGByk}>hSlw7=wqF7EX^diw}L1r7FiHIK0#L70Is#*M)(#?)%>%za`Qd>@z)!3oT{xC`2Rjh1C!Hjn#i)!jIc}#tGXA9*>cj6ntI~AL^fma4Rz15yPt<0|9|%0<=3_?y$>3%Ip&;e&Gp!8t-a5__nx{{E|)818#|&xBpRnp1JR-t3DH4FI1w?C2u8xe36?{U0HNT*B7%T~MCgD-fCddBff6Cae?VfeaUQlTB8X_vW&D1>Z_LMf?7h#q=iGBEK3Au9?Y$mz%{Av3-}uJ&{T^us-(WEfh$dq?a&&j|0;;D2AZj{BcFZ<#c(UX>f{$lp53Po4wV})Fnc|i4(hd?V6I6r}W~zgxIpvWzR{LGu>U&35s_5VT^20g7F27j>EH8f|jtu<pv&&DnP(S0El1Mh)0RhT#y#t<ipfUOdGsTWPyZId$TobR~fh=g<lXoCo+<{nW_Eh$CAVLAkbo27Zi_7o1BF^ss4Cb%jf#`qxeHJO{L?2hPBBlBZ%L=7p$XgdFjn4c5>y&v`r;Io1l;KvLa#Y3nfThYn;NTyyQsw{n;>?0+1?Tw-(~5kCgV+M7V?+u9+$JK0?V(_qm3w8kxCu=cvT>tg5<4z%(vI6G%35I?#YM79=o(-p&#>^i*hbyzo(h%9ZE<Ue2Bx{lS>^k1Ygffe2Qml)HEog9pmwP3RS;K)#hhGwqO@5phq+g0%vHbwSfN#*{%E4)S9VwkG?<$?EvY!{r+$PL{@*VnsM-1aZN{UHdPN<@fszfMgHMO@{nyl??o$?$lA1=imA&tJvFKtr)S7~xI?xf>p$`_TrUgA;keYMPZRlXUca61UAlmmNYH7A44-sLFXhMMp905)0C}9G6^6)sXRfFPOhiHplCc_yI;FEab-y4rG`==v3sysESn(JRvsS;H({pV{_bM_C9f5C=crh$`!9xxOqH!!{-`t5-$O<2+JXL)Kx6>Cw#@kmS2Av*!`AlWHyh%`-Hp-|5)U+Pc0UnrS5{-JXDO3Y5w_VDvF?*C7uoH{BHQ26(txKJketJuA&{b(p8VP+1_(B47(;b28O+_aM_MOAjp$<8_M50f5dAUgw-=N?rwwR#^^yn4{q&_s25!cFAN6j}L073+cZMVG#WZx0sx)jgK8lDG_du`|gM6i82^|Df{HJ(xc7aO6owCp9j@-|^Klo8Y;UqC<7>39rodd^oug*BtoX)n9!Vq~K{5PG6`3Jc@jbC5E#N*?hr2SRH||Z-!YfBW|X_!&E*n<==shh}`{jhUdq^eil62Fw^|qOq4RK5k$n>QPVvyB;{Bp+%pwdA%L(FA^fMEzX`ereh^bqE)y-6+^)ACae2%3a@9SDdVbXX(4Q%TVn{y!0Hh&y`^&ed=)BnZiEe@cEc`M^A*JZjs}r+2N|~=uR5l5|e{gpKZ9$XAgz$G==o5iTG-WujkyY-|Ptn>ha5}=Nup`yHp}d%vY<>8GKjV(@3vOH=8AH%U+G0$J&hUM956nh^^3AWyOzu!(^1Vq_l$U)+FW6dMjrKktFJJ4C;Su8gJI9QQ&r0im5B((Ti?AgESV4=xRMLd)tGc81Y;GMe^m|@}mIZ~CoZk1gK_I1&K(m|PaxD8<OtbwER;Q)0Tv>G~Af03^_sZokGnU&D-lJMKWd#7I>{a530r7_{0I6AfGi(F#+mSI3g<jxx4h^fT<Zv8Fug4y2O?7SHVaghbvCx<`9ZO}ZDv-dlq8DAc9<djmH^2>7^cm3VLQ8qi5>(rUy#t!q1@==#fizt*HW?EaK^f7DTSJRD+l0xq5rl=tSIZS`6YVv8v1@CQXY#9q;u#28Ai;ZQ?iC;}%KgfUtWpeXPz^_6O4W8|mQ1Fw0W{WU_}|=BFP!q7?#{jCumIl0U6RI5Y#*U=v%*ql+pmT&M_xS8_NY~g1aI_UTxE>%Y>IbYQgho@i#Ig8%;vE~=;#m0uSU0$WESk69-iz;BbhBJqSQC#bRmfu<OiK846mU8izQCrYaOjmrh8qEK+jYfk5xZU*^1J2Of!D;Xfc<T(M>JOH&V%mljY6avyH15{b{6c$A-Bg$m9kY)44TEOp^YTigw_blNp;VSS}o8>KT@UH`Oc+YjQgpW6n)7jUy&ZX*ngS_fazW{FVBqEacfoG}Zdfnp5uF;!@fVUG&vyZ~k+%3o65BcHKH)Dt@*sWPkF>jnuT&w~f?H8L7?JltW~De2+E}HcUO+O`~si015<KrM`0Y%D+w3;-J>*XrPV4Viq?Ek8pcrjcD%Mu?fr6qasC*B6jQ})oLjc70JS7sF6?&O9Z5~?R$ou?`SJb6$R8!%0;|ykp7@jutiy>WR2yf?(f1W8I9vecUw@W=9b#O`T;H^dpL85<_j;XT&Jh&YO<ZvrKKv1U0v3ca|Ni(t}$n<WRtjwxwzQayDqLbK>=&Q;O5tR<@R-}x!wU0M9Q+NUxXJVcubd|#z?ui1CTP2!7J2guzs9M9=T#BguqdK&0EVIyZ1eys}#=bde!rI)gwe_%I1BP!eKLvKx(5nEUtRFq>Yj7aC!2!8U^4o^AW1IVNJIBAj7q;ZXid6FI#g{1l_iB0xdO}L>eM5sbsB^&%{MNBHrEyzj|O-X$yBCiJX@&`M@BY+He}Es^sN6Uv+T)*oTS?xMwCaBUAWvSVn_1UODSF^P1toWdz`AFpkI|uO=Qm!1_&QYLBdc#Oe!Q7D=@8IN1~F`(^iwbn7^dGrah2DDNWIwu{}be88!_#@LF!UXpQAXR32w50lSK=g8@t-hMiFm(w{ad|sK+gP#S_hP0rI>CEEVwdqWF{y3exYtvcWneKb;FDy3v0IP7%|3xgREiU3`+{|NFpS~AB%SDCh-boJuSLPM1-c8(?lvnwx6S@1yE4Vrl;YT!tDgqt#4f4otrU<imqz6HR?lH`&@N--V-VtrHohj*weEx`+tvnSOc?Gipfyzl5Q0I|pcXwjRh`bgpN#F>a47QNm1R@&0NKlJ`qoLE@_c&FedKEQXlHhARnhKvRMv$$HWve&|o0<AK06qMOHa7Pa9%pW*EJpk}@Xr4+w}s9CAQk13mu*)*c;OGrl~|9u!Q(GhSOP=6T-12aA`II&8Furse-+#bB_)_ZDhX%ZJ+iRgWx20K?mmO0r&2KM&HbJUWK{PivGkqL64A7ZCZt?~>6-f17*jGL(4`9D%l*v8P-R?+Eyu7OP(0|Q6%wF^=^s&$i6?i@Z6y#t0K!rafo1uhDyP22CZ~+AM`Fh_cl%lH#&@1@mNEpmcVS^{qc69T+qz)~f+Rnrc%mN1YVy=9o59asWK%srSg!o9+En8Xqn4OI!<8px(fViX(h!ceg&=zl($KDE$>wQ4BF?!-&_yd}*E@Ly$R?TA#?1Vs&73I0NaTdDH<qyrD#fC4*+ELP6g@V&wM*cIAIGRfWSsdjjxN!o<EC~BA&8se>q(lJPc>;)ON^V5YH7?zIxYi^MD~)vaZHpLHc+$+qlxCyhce9#Aj85SxmHoVY)5Gz5Ck}$J7ogtY0cK4uB&N^Q}$9D90HlOe+{FPC4aGN?u6~Lu3<KRXg`X$8RXd9+f8G8G)7RX%A2|<jX%fIu(y(-STA*JHmWBCyT5L<J{?`9$N%cPsEw4x)3aTS-cVo9Pr36bmqfKWtBZEeo+0~qzM5Z32gk-|+1mWXkIJ&$Ym;5(*k_y>C)TWZkq-e&cv<WYG?|s0B>f7soO^+$5DyO!t83N<-G~JGpfk%pQr0-#nj!-btPRTq6n~}@dRR9ciLEp-L)sx*ZJbRSdMubm5qnA+__+L1enw1bsmVu7)WG6sCvp_+EeC@wA|8|@_ojKOsyixmX#22i0Z5>%;X_zczJXR!cAn;JD_`ma5jG_pESssa>CqV{WDh+hH6asE%&JQS?3afDzh=ocn_N*ED^S7Fuv0$iUS-`jGFq3<`WCmwe`3N$|16=6YYI=EAQdocLo>Ryu|1*&Imkf#PKx0ZHX2pQM+bMny{+eHDX_MW+HU8D&X`Ej7Sgj2F)zPtY~QZZS<f(zX4@K7<}Ek$T{U>7n+<Ou5jBTouFokMT6&v8yBFNdQR#^~dH6WAr#}O4iWNDYz|gU4)UtWWsfgMtM?vb5r(l=2S2pOZ7F-dEzFO1l8KAy+OYP$hx?VZos_IuwgK=-#n#}Q9!X%fBqj1CGl{%pL33cOc=|A%lbz=cKy!!cGZ6~36q5az+;cdp^f6t-9etvD~J2t<tAPaht*z#+9^=*?<K(cq0)mG;~pNZ=4%Bpc^D0bbw>Yv6)Z?c(wa#u@+y0SHbuk>mkP<0u~3vuaG6|4y>g;?5=#IVbj-Ip2IwpLXu7it4_*{REr=3Ryq?s`LDeO&ny|Nk!Z<=@ws9SozEZw%YYk~?!IzBy*Q{>p&01v6IH>?k8<iP9m4Uk+Yh2QMop&X2!Wj{@QRX+(~;Rcq-<^->Dv$<oY}y3>V>C%YvvSFdnmt5zc=?<RHb&Ohs=MAlOzn=_fjA;x31rdDA+TFul(P2z>n3hnDhv`m5{0g=^si9U!*cD<V2PT9PCnD!&vn%9b<<qXh$wR>iQ2>XvZwBxe3`tqUu8pgx;w;bB#;%yJ+K%JL7Za}#^*EWRUvzUOEDh2p6cFz+q1t<pf$j$$Ymh$vf>Rt7+OjQcaiVvYnQ_Ri6iEEJN5k2MC1hN8yLg`Ty4Fpe7tT(H_nX%UznM<3HyfobAU^ooSu&956t~xBU-8xg;y}?9Tqmlrzyi+3RyU}*m_}3J&<DF#$d{dGmFpLc`cTC>^l=T1i)`<T(+`l;=5m#W*!bkKMYA(_en`|ZPdOZXEC%<gUN1t2V@PSbNIpRN`A^yF!>6eKA3e6MZpB;0`3004dQSoU6{S(C|dABawK?KuVcJqCl2}um*XvgOBZI{XZIrRU)s#q`BWvDKb@|B$t0QP1yX+)p&G7dmrWuxX^lP$w8mEmW?P%944s-%5}7HH=2uF?R?SGZ#_DmBv>m%v|{XM_LRhxvc$etqhB##d0LQ=!7&VT~d4u$EKHylrFtmRA)kv-F7}JlJ+xs|+fcE3G#U)<bLHHFjLEA|2imL5&S#oBYGs#m2fx)h2ZgL(_(1bdTkiE|g@N4p3NU^$Yd#liUdT7MaoEQx1C+Csu1C(>7K`kR2el0hIU%UvyZPp#j?3hQ2e?L2iGrd?!+H%MO&SB@bjYvrDXWfIe|o6ayoyln*(vIF0<UuEm&=(o!;*@|N6_h!3FRf|KG%qD7M1Co6-*DrprePD}+7CbM2CXsWw>ZP_a4QJXom)RSNu-Y)gJ)1FSnBorqaiCO-4w?;wwd{(O}p=}@i9@VLa_a6a$%^{Ge0p>Vc*`{rS+)p^iaFI|PDo5CXs1DnkGA_0qDsUJVJJm18p}|ZfI-3T>Bq(l*DjuAfF;Mq0yk>_1!-SqTi8YZ{6cOWe)EtOC|1P@5uvHu{ruNIcrsLR=nGDd`ia}t&4p8$!Ec1GcwQObL9f|w%cRRi@V#9DpXL8~trk8o;pDg(S8Vc}1l=KaA0G!gmhIdItn==2}NVp&Qv?ZQ4v_E4aY~1aJdl6@1)K&wcUcZRvL0`@BI4v)Z9CBim2uNAD%Mnje)Y7ybNGRc1N$RxwJMWkuJ)8PBH@B<rGw-*mSIziiP4^op?AE@GNIbrq(*1=Q4^w>0@7q~^KRWSvvjHdmr5T-gSbFx86SyA}D|6y8C-C@oxjx}P0d7zwe@GT=RdK~<$b(0=gw;k>m^Z?H0@OE&AgP(X{s}&jWvn{MC$U10s{D^dHlP0Gg@@|K0SxfM`V;|U*XvXC9af1dszgQlMyx-_+xVqQROA5C+LoO^Or`KSpZZ+%&nO!PPOungDMPsLvNF|m2nWy_9BMYy(mZs0Wyi-;)u$v)Uxf$gDJS%B1B5E58E~QyM&f%1F8~%DrcAjjJ+RrLDhuOmI#|5G^7mUGBoMr`ZuPQQ&;aaprEayExpG~pTNzVlQM!tzVKfB-iXXPz9Jku;H)obyK8n>o`6g@e3WN#i9HL@DD~c*N-&#1^8`jBZW?W+>%iNQ5_2A<5)C60xi4d8002Fhvn=iLxW}|E#$}Qn=$HXGOQ#ESoq5PzQa{Rak%75miiU{{eURsJDbkU4B+eiAf$XL$$&2czjCFR~hHRd=RB~;<04OeovwJbOr+5@p|w>F>6v4ms_2k6+}g;Su^AwP6;2Ys!8=!(|jun7-|JTbm_5A;|#;zDv;6yj<V{_q;XADRt8@1pnL2BuWf2P*I0-jAP-KVi1gKxAA=@MBO{pU>V|ut?4vXrqB>t$V#?-8$Yyf~zrJ;@MUIcb^LiqtVrKgftDHJ&S?eQer!f`gieCG7CamYxZISq2ImuAZ#sH`dOktVz6?FnKChSM{b>iTKS5x-a2@ASJP2bo4}tzO7pdM&N?*b^GFh;O;cO##cXafIZmrdd%p495he<1ceYPuBb6`S$)K#<G&UFS!Z8>`RKnR|V+|=?v6Y9p>B3ScRk%iVWGX``eZ(~G>uxzTY&o3eaEXSB>1OD*G_hS;DK=)M=xg?_(0%EqXgWSDY8cLS4B+kc0Dj@77zJ)%G8Zjo23|L%;;POLisT?~%yKxHC`NjMB-;zj)3|lKBDcOE5^g5tOaHOcIRA^IzbbP39V`>^HSXE&3-VW`5DGLS5>R3k7;H(_d3+^NG?=BPU08LpB`2<=4C<YF!{X_h&tQ2aOi&s-EaK!n18h*i6+eHX{CSYlkkO2wZTMiG=j9W3qKa*3NnhbRc;wzzjh=vtUO<TQnzhiKCA)+34vKOQIL=n&N0!vQ?3HQK8mnxFo?T@oxY$)w+FkuDF5B6dsia2zIOJ`V6udI|$(QSD`ED`usf}GHzs!Rr@wmv?Qo1qiIgO3$-CA#`F$*hBX+;F<(NszX2SUx*!YG|JPW9&6c1?*|xh!oX@Q_!n#xtChkA?wu8l6&kz%f_rmUG+9GPaI$l^I+3am?6c75}&1eRu-Q`QqUz0H6#z8V=7g&l`izozvSp_G0Gt2|XkjBzTx+nT0pA1dO%C@<bzX+7eA8G*;TMysv_<Lij`&wKh}@35cPZmgAHiV|62&nYiw3oK~QM1Vi3pobr2B<7}2#QHr1hE?U&Bt|ZG(pzsUkWkm!c6U%w8$MQin)JDyI)a<&l^azABUwxWyLJ{FVwjufRZa8_)!>5wkpg>td?dD3~2WG8aR-q+NT?WdT-zciFmx)q}&E6aJxN2SiWHq2rn%6R0w*1IjHNo&~o%fZbQzItD#F+2ORl4>s{48QNWn`iL-NCe8?i<tzF{^20D={tdT|?0`ZZ_(j)0s4_Bt=u{(<_b?o?h2Y>^l?qp4!i>+V2qi8s#;EnSk82u2c1Q16Yz&uGURBWrBm5v!T+>Nt2fuFeDKE_6J!95o<nt{i2^ZTQ4bL5Ub$QqJ-fmp$(@h#udcE7;9o{{_wu8iDGD_S**!!>Jztaj5W`dFyhVnMO(dOlhRy}9u_NOx~yWHt%=!n;m3bX{G0!9rfdzDuXdKQaY3vpTLrUsH&eDaE`_8uqNvqaoh{Znn+@A&megq)q?CVnhr|taKkGehE!6rvtF48r`I_nkwa9j?Dcib?&DQpeVL32o%JZPLabVi0Y(MU({GAU1|6)J*3HaArqZU_839r--7&Oxh>jxN&5=fqwMGi@7%g<GaY*ePPgdm@UWeGuwKZ5pYRK_LbYwG@78<_o7uvY>LYu$*iz)@or0;@`BBV@V<Qp!un<G7ToDOfdJ2b_7ibN5RWS6_h*;bn<i_f1ILer1wGcm+|XZbw&hwmVF-x%@1r@jBf<0#P~~h(-zAk{!9d&hDoNw0=)Mu3x#&8?C$|J%`s2lM4rw+Tw8Fb#3B`*M5&3s0&pM=Dvw+NTYLzAdmrs_;x4rMmV&VPp7PQT-`a<Ym_}5^@(!PA`7h=V5y}Y_mYU|1Z+U0HiyJmTY35y+^#+)0@U7`)*%}OT(o~{jUtKDM-P!cy3yn@^ttL1b=J(*M`)yY0?}6gwEK&`Ir-fm!L%<~>wc)$J60~<&-+1YSC8a%J-Ys`<j^RH>`R*W=nmze#9F_;$1BAW!Bh8cO#)W=hTnz63I072nKI}nc5M<~;H_}9j*Svjl72IADjf<vDHB7Eg3bdD`@r5%A_48e8>DT2j|tH5B+IFO=RgHZxR#(GRYDb#^@9U_?U#)R*T?j2K!pZz+mgUtFfAfnigWF|#xaAg4BPGqJyO1j=rs-^>K#V*mq}XNrtrY>RCM=7T2F&X;DaZbjJKleL=4rval>R_HdLY-rua$R5C{cl!Nwk-b6O7j9jV=%Ol4u<r=)81OJrwE_g*!TM}Fc%Ie~kXT`5<?I=3YI0-5!h${OW>-#uABr4xeoSkiT{yWpb=)gLCQuyFD{IX$ZrcbgIBxiU+~)%)8Y3Pk^2%h^{^2~!*L5|VJOmMy{N3oyb{RqRCm$b1QkR>d|o^4frWri%Si)bYH8?Q1eG$IuE!p!a~P*#5kbjT~yW+nZIo2t<=)qE)d6TJNfmy?a3+`{Rq2{<U{eZaM&0d}VlUy*Ot5RaY6-Xts&Er5r@PyRFuEC!NO07HVcD1_rdmn*bjh^_y0N97oIBp#}}hX&lqQG38|m%U~NXB%J8w2%snZ<GXe#;UutWFl>IJ2H!%?IY=>LDdaSVZ$|l5;$^9?z|9_S!#Ql(0U>QmV<(=C9nHiDSQ>F<@O$b$?!ft1t}H8G0IpTn6rKyXt{P2RN@Ci_(Aa_!*qczz63YY@8U*}<Gr}u5)kd+kr9_wTfn5*nt9A2FS^zCmea$tZyO)?HvKbR4dW8cXoO%#yf0Ru_j1Qq2EwBrt?(+ji&7-U$j!L9W^9=aVg9c{c3I&>Xs73)8==U@zt2jPkqNqYf&dx)5eXXrZ@ZpiSanCv>8QR^iy*Djk5z&cI%oomWSZHM1M)YxfQcgH8<b<o=XeV}wQz971A6#iQ-f^+0YD%f0z@)I)!=z_BI798m{#;RbCp}wYJ^*>?O^y1NsPLY=Riln`IH3F7V{uupO6oXz=Tana>~XPMy)H9tKWW<n8F6$+`b?$2@h)-lS#js9aS|72l+s6}dP>!H$2b{p#L2G4$ux_T6cR2+7ID+!WTN`k2#yCVe&*0UkCRZH7a+cRc1LO3VwsgBuvl$PocVMQ3Yg}0N+~1Wv1kF)PXUt(#3SULeFFHgXOgjWaPZ{d6ZdZI<Bz@%^#AMEI-1I@06*q!22>zZw{px^NP*n$d`wB+z%lWfhE?|F${6B&WSPwr;;cWjWLylcK<mYPF}@^7Pi(zs?byawViZ^fYY?qWJ`usT<q!)t#HR7pjpK`Z5+B6mwrUS(&+V+*P-0mvHTY$zp}UPT{m5C}pIt~Vc4h2<AYnjxsV{EIQ|Z-XT0i&|T@!Jw?y>9oxz8|ZcU{<&UHv+y)_sfKdEXD_&0QArp$R2`m&iD9#r}TFc)K%HFSgzX<M$`%8DdJqZ0smTEKsb6a=8wIn4;A5o$|&9d9(X9n=AsR({2rYn?cC0D$f^3B?f6rlqXtpTP5e_{Fg%5Z?$f#f<fmC31pALY>*;0Gj=Fzla8K9o$0)Ub(|!~Q{B8E;{Y^X-6WGC@Kp^Q<M9{Y1L(|4kjKZnWoJ(7wwRtOhR12qj<#smR@{zcN9zTT3g<z_O<k(m<~u8QXSwf$s^+348t{MI<PEt}aI9F-JH0bBo?5!u6n@}g+slgT6$&N*z)9QZWSl6o`Gj@-94W@T)P_3<`v4<WW>mQ^hd=e+0DK#Tk&9~y0mgT_mXwgK*K&R#kw~qp-*~F1z7$PxDvoiF3jVm3<yMgP6Gy^rg=m(`%!|q^+Tk<~EJ3tXOCmYLu4_8Ku4RD6DwR}TU$5v-xc}oT8LXVKO0W9`8N)PQFifpz9>~y?M&WqTGg7UF1(?N}<SXa2iB@SSx1p)6lfiftty>n*wLY<<m`n+bf-)1IfwVv?7e*P)3Xju;8Ji+m^@1ElG+a#HljOjLLMRkWceU=x(s{0*QUxMzRm_878)CjQ%4!43D(!<*)ljvJTzxWF!<yArl2yTAos}gFfF)V2B!t7N_J(LWMMA6GYMr=$d1dAJ<2S+i{dc~a`OjB}+bp|_FNfPiNEjO8ri6}GrS|2Jq?@HTpgoMw$4;YUPL=#BxF2RPUje5j@@^QMu{EBSjYl)P_qn-3=I_QqI^p__UUb<MZ<er7X%Z>RdMKZAsHL=O+PLzD291sKE)3X}H6CemzC+*QNT}fqfMZf+?PVWFgLLGmt}Zb+A8(xgtL{Gpp}CPv&=;&~mVes|%j+Y|;ou8^?X$4?KH5*OTKn)A*9m4ZA(^BbE2ZTZ>K%vrb01ET8H$wX$j_)UQGjT6)@p-7UwP3_B)V7~!*`Z9f2hMs5)+6XgQ0S^6z}T@_I{*!HQYydz|WEOTSuH`sF0;Rku(ZQ&Z{UXK-NegG?_aRQ5_<bIK=rFN7IzVZ<^_VEnm<wNQN$UYum^xGYtRt2MGr~^f9Bh$>Rz|K>i{e<QfaCOfw4yIVw|<i*e{G(tw)4Q#fcU$8U@UI#dk@;^P5p>r5R^Yhu0@5!Mp+ptQL#GUGbM@{PrU(RU_L2BUnLOuc56+Y<@%W3RU}tW~honU(S6p9>0#o=eJKQpdNIwB8gQysXd!ONed(Bh57Q=6Y1Fwy$zY<BH}5pAldpD|YynMWl6Wl2`ZDBP?HX|Ip+dH)bDsSLP?D#t*)_T^r7(FZQw#4O5eg5xsf)5gkFBx6W~lBb3ermjZH}QLTpkxH`0(YePGa@UJ?wn~}}RaXnw@;(VD4zF8m{7K1unS?MZ|bsW^o5iLz;4|DNpM6;4ha+{54_Er4_Lb@-z962dj(<rotWH{Eb+&wv##ew+v!}*_IEP{_*0n2K?xmW~GC9O}7$1!8_U=@^ceWDTXo!#ejQuiOfl&}3Q^V6k_8mSd1S?;{nJMo*W9v{(?`BDmUaMB5li5;>+ABYu=Sk5vv>+(G@&8!=*=*Z@YSdl+g!vzin0aVVgWy>YLzp_qs89bTmax0aCBjZjI%OwUFJ&+`ySU286aCoh*MQsbCY53&)H(B6|5RftduW!B#>{&j)u4`R1$26w7doL_66<a(hXty$5^w$^&ym?UdD4#E(OWFf>G^TUs(51a$%VUr|w6DA3D0>L3|0}4?jLX?_&*kEFw(V*OrR&bpSvuY&KcC@eSf$&0t`JvshCfhVILBFMSp8-%wGYS~p-wpNzcjbA>O_ov!gBg5Kotoxmz2;BfZ)-KH9X;EIjbIiBPRA2{zsB%BEvrVwU0vzLxZ3fqv%V1MTo%AVZl0u^hdimM3Qtv8fg2qW+*Kg-MYneEZg@ob~X{X@u5irtF)@&lo{|-V=;%Tl}g`G@@QS!BfWyyFI6JVE3d)Yp~~<Zn!9KmqFE5b8!RF0^Rd0pdNQO?222x3P`m-(7GI=gKK%x334DbCw?e}|G@6AR3)yfiiHC}IG;&T?ZCNp+)MYaPcteoE2%^R+VBWl8*FuCTrv8{fn1$slw1_*(k7#7?Pmx`bz#0@pF)(|!*uD#FlSsdWOpG)(GL?wFo2(WIM=5#9vdk{wgdMb0@XKrJW=gC{T>3Yh37P6ifXpYrY&voRex6vW97z@>$bSuVnqU*@%_=~8Kvnlh&R2r&^ADq;6HNldyFbKwyJ!5s2{-A7_(=B!_aTvu!=@Tfkcoy*D(C-$;5Mj9VBY91XyH3jwq}pUIK!HE!fjDJ6sz+aSlh=p(MhSPtVVB4)v9ba4W$t<>dmmHo2FEJf8N~7KmUP6|1JGq-qxo(Gy8i>pYFKy>CP0AeLJ7-Szm~`&olPi5IKhAHYIASzgDjH-0`+Ow~Vcah!<RSH9pkxMyi5i7Xn?j!^P$_+S-ugO^5C<I&`m*Bn;#Z-7@J8GU<+0db94Ao_6cbdgG|nRWgB8eYzd;%J*f}oj#V~@!$XPt=1*~)%bBljh#{C(iufgIBafR)*}Kgog=VAg}+IE1L6W#ux~fXD`&Y)dyBpu>i*x@Bz{!EK4WkPX~?R0mpJg*#4{TRYD-9SJWzWq&3dJ6H0SR7C$gQM5-;DJc4_(0e-FN%Tc5u}1$$T%R@w7CzBfl4yQjWxY}N#twvi>jD!W0yFuHuXxZ`etB(HEZ4_^Il`V|@3x)2lUp@kjq6+q0`LVz=!eTl^-X<@h&mf8TfD66gsrjfoAiEQbiWMY;HfL%_LAqoq66JjDl8lE!jkdT9hc_XCt#)Z#h69a1w$mu7Z%!(>M6o3HkGBwfwfmoACKkU6t3W=84IpBQO6=#c8J<*^*V*Cxa#^sf0OCf>_E`?t6(YDy@<miEbvXfu=Q1ueqKkt6s^Hdf(?Gb~~Al-+MPTm~vw&lKMTnkth5bs2&va$b=Sw6B_@W_TxIp#@CXMZ5}0ilFTQf_f2R+MY*Rfav5)R@Mcti*0jR}!!3h+JMlO4S3lM6+B-EzqJlQyEZBK9WNf45s5hX`3hAxd6iA5X>5YF3#TeR+-*GvO~qzTb8?kNUUKzhc8T|Eit++lZ50|V+(8kxso)Xm#h<$V3~ZF+&^45m@_uaEsz}#zU<G^R6}Om{Cn?hA-KqE#^vCdequH&ob%=265~?)iB_{^;yN;>S=&a1i;?|oMUZ*($PpW**(Mq0GqTu<2f5O-nKx`i7Gsfi^b;M4jH?;BKQBnr&-HAUG_hWuC~#}QJ(E2{;}-nI)eD$n8!^Qo^Y6-@aNC+e;Tel@(Y(1vWc<jKF&~@X{~*ar1G%3?Z{eMj7uF>D)s^IBGfQ5)N~0I8M(-_!3B;7<d8@IG)-jh^jk%1B6fY8)<}8s>djaZ?I6dtp&PHx`E+MuYv*sIgi$q39gH&e-);AOMXoIL~*x)NbL^Y82k3@`V%dDA@$2LMF7_0@90&Rq3u<N|GPQvbqP6F(2zDW?m@}d9Nhl{!SYD=NwWwsK2ZYzM}Vid0xbG=!S4HfvTT)ev$cDoTsJX%nmr{lnw%QmG-W7ZD#IF=cChb57`yAgS@FjN+KH!*dI>JW`Kj(THYc~zS3Gi~#;u{;<d(k;^Q2&O^pC-`x$U^vf+yJI+BX*;=_i{jxLuGB)$qLW)7&QAy82qWHQEWQ$jyRRz>r+>naqd2fG65Q~L*-(7(h`u*f;jV@J#8e?~IjC3503F?-pYf;~jz^<XDc-rAHybK&sx-{KJ2-XDM(gnzv&s^;y7f<$XeEbo3fFb?*IPwrfFCA_q+T)6XY~R)3RM<XmPN!onlqE?F=pPUyidkRm}H(i&}s)X270<@8J^I>eaWYmY^^fTn67rFEiG^nDvx{qiyU!8T-N5Yu#mF8lJ#^Fo?Oz7vZ2M-U$eHv`GjVR>2XwQv3D1fX~F9f25v^};x%Da)RB;8-0Ydfgq)Ge=MuOa#5U5TGkBHI6Qcwz()mzH`sNKrZ)4}>$<b7?2l_R~%n+DJMP>P_BAfZ?K@BM6jdfoP95ykhqCQAEz~bd|JLQBo3IHNAQ&pNIp11&O=?UD>%cTgjExm6Yh|50{|Ln@2zxVDd)7PcRd|k}1r5>*1biPi;ca6DMo4vJ96F|c+omWOlzpJeL<7_6W7L;@k<tyGSD3MI(Xq<O7p$gVtxP{$X^t(1LS4%ZAA*ESIY3THP9jLoe2inbwKz(KSH5iGvb1Iq#g{Vd78$i!5ANp%ArnO<%e(!UHgVo7*l{AJX(`V?4h^)4f;bua;p*xz+Uyx^{MK@Y}mUlg9qfq@i1G|sMsiSF08p=Z0g6DfTc*|QWa~cp*^Y@JN$MO3?B(QsNrtJhM+e1@6(y6<NW5;EqobzX7OYxkW6Cqm+MmWg_v&+beKJ1Cxy;4mB4SiI+6wt$+kU%W$M7v^m<dr=xAB>JnJIX%C?$5n94jfDlDa9%dT$nkUlyo(7J!ri+hfj0hxJ^gxjvP2fW0nhonKX-LC3!!()wR}dGjH6A!aL)@wYNENs*!>Qw=x1;9tm&*jl?JR8!tSjS0FHfy`Tp`z|9wg_<uDk1iWvSq&J&;_sn+6G5>A&wf;1m^w3f?foOhui_%;l=*vp6fxy_lTKT5+4cu{knMDn+biOZJL^cz9Ip$GwKwDaGw%$?RtxaOn8Hxyd+#$7MqWK<R=m+vxIE%9Dc2<Fco*3UH@Vp<${S*C%J_Cv&oKALd@P4p2jASiFI%Kej>e$$3YL6U%%Dmi9CuvtfB>k1A{&5)?SU*HN!ZLA?avD{oG$$(#a-%H;<1SP+cPs)YbohX#1f8OsfRn;6y-j02@pHZG`!I6#rMf+v+>%oHE%&3z9^)A|*M~TOjR9|z_E=^0`HlA|0lH?d2hFZ`z)0sHu8JIGZmd}dOL9XEM$)V1oJ{HD9mmy4u!>}cyGb2MR;-aDZ9^3#0YlJ9=d!6XAgTJS%0nX48;m6Dq%>5`3_CIYT%rF5IM6<5A7sKKUSc!##nKSSq!T1(L^p{B#`@{eUXQUeMDr%K<Cq8K_|s?eM#Ytkyz|n)^+5*4D&yMG*p}xfno!N`S$?AirB)fu=tF%y|Cw9t^k@AAuIzf{^mBai%E?a?n&S4BD@UGw3H6xW?7N?TsLTZz?}yfDbxiVAWiqrc!T&#Xzu|`wAm-utj4hS*w^5!S#(3VNJP-B`EB;9U6iC^?_65QGl{0Te`$s9;HIkJQf<OuB0iP1ANF*j)70B<Z5*N%rNdQOs2bGku)vZGpn<{Qhe7Yta%D3+vo6Mo54hT)9BNID<zd#q{gf25WW7TNsA6%ZLUnda}JYZ5*6-HCrFp3-Cs0}z)G$(T7Q}U-t_I-iEXt)PS;6c08a#(46jYmUCoRWexx+$q2P4Emxhh2^gD<gvnosH#I9jjrD7<+P&CUBGg)+%6d2js0s#Vj!9KRY+)fvV9Ja~|vo;Lp>>_O+~JBP=V3<fC9{V(d*GjX{U2zNObiIetkjWm7bmj|CL3X_p<bA)uQP^NGY|cUMx}0j)8@#6r*cka;={m9HCawb|eZpLMPoY#Mhqlo7j|j2BQ<CVYE98U-JVY~WQRmOBCdV~6}EyoQ~H6|jg1O?Da3Fh(-hbr=i64K&zJVx!!{uDYH85~A3xd3tEWU><bpQ8jVZmh~B+Mv9TRytT;H|Gf|1fN#&W?x&6m<nFK4upxL^J1(ZUheIv)TXF2f@T;?6ctMmAiOq-hya%7_mTTjujB0WdWPNw+xQspc?bLLsb~FT$W{Tt+KE9dc`P!O$E%5O-S}%FI<%)9~3}4IGE30AmRkGF?GsGW6)&*3$7I3(eG2xxLIz@($wkqw%%{c=8yn;Zq%$)ijz6o{fzcM*te8y1xg>}{+#ZGP<(1C4DWIETsW}IiYvs}nS*>7#JS=oVH><-MXha>m@M2e!YwnKAjm5^d!BX#Fgi(`6hEz`6nAHf?)wY)&scWnM^)n(7(PsiJjf*1p8`L`AEkJvc!EF7gkFc=3OYE2wbLpYs~MC)K~<&=~Gt*>veF7&b1setpt073te31v_163Ju5WYxtcT78;oQzd3dYzeNtT`&W9IhP5Xwe?!J=ne-}H`IvaC0y%KMC1kx(jJh^@k3371+H$kJM<<5FX=$0kDU=bbcsmAw1A;v9j%f7Qn}|%<C`BK`NL}b3i4Q3OB-7z4)cJuB5FKCQp`XU4p9uS1XdQh?A8soV6iu3MM>tuHnJfFR0h_nwI88cIo8BQuPmRjcD5QbpC3w=zPF_33$|_j_%DY(*i-BB%K1~wTqA<H=W77E7!r%}<%B^#=UaeXRl!}q@MmZJ-mV_JoW>T20Kqe&(4@2*p+@mwv?!I2I_h%KVk@$SBRyH_ZRo@rNDUEmC&6J}mc&E}F3$F1`#P&A&H}MV_EbN9M-?wK$r|N=|IL$&&c%w84Z(;_{T-K^BR5}us_L=00bQr1{<L2yG<CJGM|6}5dj$1GA}xfgMdQ@h?ml*<z2rio-0D@~OBJxiwc2x+QMJw}M9tPHM_gI+E5&F;J5;T+Dg_G+uUBe-ojiIls#C{wRqKqM%yN)(?bnL*(hkeh4uqa8nCgkaAIslR?bN)NEabe9ts_gyN(&RV_bVkwC4E@ZP#Wg*0mrwx9hU@*-DvAbIsY<AHfskv(4>q*wk0rdi8J|Xf>>hrOAFbFvZXyyRzrdl307tp8kr#09dN)8j~pOI1Yy1X4&m!d!ZR?72UOsWeK_{^Wm&P0CFl*(=1$?;L6<`X6b!mY@!g_HL?F7MkP`k8HuAhtq~l$=q9;qUA9){+x=}53FCIN*Ez5n{i8QH(OB(JysoCIDH`KW(N83YKipUDg?ck4C-X-?v_W;Uw!I~5&U}}P9S=w3|cB5j!1FAh6yPpZV9fMc+i`6ru`_<>?p3z5Ub8nPH*pqD^ZwpJ%0x*vj&~q6Ce4(g9O1o1D*W?kTKhsoI1YS~3V5uUkk@{G(mapXAN%9DWf@oICfpz?HXCN{n5#_S#_RL^ddx>4^+l2aT`G~bFrML`+l?XzPJ>8h(QP;``Ag+Df5$TdfR7)F<4Z*la83;<5p)4B6hUF2RRNkW+tyvbeiXc;I@~hv6DwnXl75;T!gI=s|-1R>6tVPD2L3PZic^@{in%$fIxm>q1tN!v@)lJ}<;0++nEpfNzLX=9X9Cx1f+bwr4fS-|$R;{<p{kTOiEAgS+it_Af)cwsE+>E+}oQmUY_Pgc2g?1gw1YS#Xl*%CY33*n%6;X{YG%5EeTt+hlgVKfF1fm+dKmQH90}0r;8+TxL?ec3rkWzx??06HHX6^&okJ)M+B^)JCv8I{Om6@<ct7z0*hMgL(ePdQl^2Lb3`i6^Hu|h3sF(vLLsYCiwK9n?ax*<S(uuyzTS8fO%`Qu;lh9nkLb+WiE4={l1=--<<x&_prR2H7JwOhfmS1cK$g`=ii?`WteMIkt3Gxt~XJZbPn+7IJ$b`YzhEny=T9|DeI8kW75_LdDrf>s>XJ;mc9yW;g)Zp)qTB~N14a?qK3&=Cb~T@y#t9e5SPByv+;+5PfIjOz?_4C-|p=jS4NnniTxq~lPQ;0?n$Ga^RrGQ}(}nlx|PQSjz0s$i5ygp?Xjn0w@wlsrO`b;)-n+{GF|bk&D?z01W8bvwMLs1VO2VaO_q$L?G1Pn(U`183NS8@`AgRE`OMDY?lV>gm1mb}m(5a^Cv`cS4UYjKHJJ^%;C&mkv9M@bZLu?zd6wY>-VtGRWD>h6hyCPUhYPfYBCv6QsS?!qO`rTvv0@OpG@qBC{3XGp4(?9^C3lMW!*thv+ML3#n&D1^O2T-{ZsplM3c1!JGQZ8jzXtl|8aO>!)DA-TR@MPcSXBVrn2TYRhj_##5@^w1Ch5SGOv^+=tf<|5*8bv`u4)Tq|n4g*%s2_B{YE8N;mXyHh#P%pnDcDTzR)l3cmd2VXZ&vHI<9wasSVN$hYX;pMO!ltpt6eYM0a({N3anJ0ai&_gNDdi6;=)`I|V({>{uT?<xG#owS5lg-wwEMre1DRTczDK&6}gItzbPBa^E^Q$M2M5?t$YK-up=a^;z%gVm0Aj{ppPudm%cc8wQYD_Ilw}QW*anzgZNwjsD&$6qTl6`ulK!(Va^k|Ru!~`5bUD#7uFxB0DCZH~i{(*^_awSy%@fTU2mSFZXD8F>CcyF`MJL^Jns#L%$p%`(C;z<v9lCiOKvfar_J!+8Y5oaGgrjYtbOygs|H^mVlvO4oCR)ZSx?=_d#OyS+{QW+err`nemTJUr2@D5J9BB{#e2TYhpy<Nln9(Qlxo&~kZy`hpcnYFuxRM5^QIbL=UE|#^d@+p6%EDUp=148_Xn=07Frn1F4f$D%Ys&83B(L{oMC&yfwJUa~8vg|jta9L(Ih<V)bbJxu}H5@dAFkyikdn`ePL!TMGk%QpUHUpMpWCUBot8^{q2?DFozd`n;*vD==2r5SQ#7Z<@k&WV4>cFv3UOusBlwpOx%%i43;jJOcGtq5c^^HWn1hpeX`NMT4?}|iMY5zr#G)QZtKsTR?!LV|n+U8N~l#M2a6%u49A0QC{DVT7#pNx5GMP7_pN%RIu97?7dJ6%arMi$9fDL_|)^UJNGByW5awS#qJVcfJ`hhbW+EQeoGGGMw2L_?w<R&V=(w|!f0d)94-H*YF)26~?gl6S1|d)A1?k~NX2VP9|f+VQ4|u!%8?CElA@NV%nu`5jyaN3z@yb*F><*RwPs=s%w-L#*8Dz0oj3w<0MnhE*4~8&|U1J;#01BXSNLCVQeHP{t!VYb$N}S79K0lS%{}abAZF?LgR3;&5AAJtEUgYFpA0DTAw8T5bY6f%HEKoi)|iP${qfQR{5+i`-uu&(3~1d;HU%@Al`X>-nMo{B(ssUExnx_|u=CuJF738Q#mE;jQ1B-{#r;A<p?L|M@lL51&Tq2l_LdKbzm*2jx!}_HEvqp8WHz-unmV!Uq49{tWNw&-~&)Wn$!Kf6mWJe~!=kxA=4MyMNK|DSJCqt6yI7)75ufeemkDw||D~KU4M<8Ep`0Zx$|uON{0Ze)_$>m(}WMMcA`{M(g9hl+DeOg4DiZVy!YmDg`?gf;O;57QtvHo~bQYtRX))1%0x3U%tM+HK&kB(uvDPR%frsela63ev3#jZWP$n;Pdvf`9EX-gt0*Hjib{pUR+gXW^cUxr#{Gq^CQfDXT_yo9>LH4jQ;%m!?pAGeq=9=zvF7}h<UeLpklO(vp>fRD~FA<(=*$M`6ZoSfqG)j@)nb9(y3ma=X7Mlu2+RKZ)a<8p}TZ;dKv)JR|w}{L1%t(cPh&2#>Kb6@WkC5Pm&E@;XSRkcqgD`YyFa7>f|iO+3y6B%gx)3f7;JrPx17oN9v#9@~Qbx7j8dw_O9;w%bq`)pPk|C%*Q`NzxYOO`Ld@!@$zS==Mb))j192c=RZEX{4U}08(lryu>8}YUS}`pW`8d4ss6dy?{-#=n?G(Sc^*x__}N>6cb5klhtpG+TBnrU`0RL(##hoePQM4cT$f|=_QA!udHRhZyxlQv*E}A%vC%btWtWWWGhK~%{o;%l&DFP8+KqQte}?%_TU_we0!jVfE@&4W^)t5<?<>rCUjx*f&>M&#L1d^iL#A15rMxk(Z9w2iH+V>{PhqtNtY;+zPkDN0Z1|iAyA~6HE&PELqsKiQfm#lgpG>|oxPpKdD`(`ws&W?&ov2^v83dckco{D3PK^}?V8A3uUTws@K=WR52<o+Z62cUdR^AZScrhi5yvY3l-~1Ju#OeY0wl-T~Ov=Rs-79Lk22;X{RWe_6rq-CT)Xf`YV@D_-*JNR=?ZXIDP_H3o(>zdW5k<!e_UWei&+M!r1C6&@`T;Z+qI6H<S5DcmQ1})rBpOspBM?#sROEqf|0MW;z7CCh0php_%=myqOu1!-O6%>|r@SIYlZ#|`G^gqW0n!-nk<1Rs4SPc+0D^bISje2&LrYvyLMIiNq>gtUFh^+WNHDk&m{u;(WXwjh4FJ9-C%b-Yih*||FO$AOJ@7rQ#4xx_0L6no<;1QgT5Ya{$EDLP!c#oqGQ6Rlx{@Ot)lu-SXgxPI#2d4KY=uBRdZp|*vEOs$MWbZ*zUq^_m6`Lf)azc5Y|L=(Qe_9|FDZ48Hc8LOnwd0Szq%&VEvu?qGTlHmv7H&O$#jRAqQP9Io3W{_#F}RAXywQ+s7hrro-j?FQ2=BvrQ_>md6}S&X?-*o#?DUnne#P3!bRu@sm$KAcb;pV`EW1ffUipZ((&HUR9ep@S|<f>%0W`d;NvTJ|MmA{Kz`(SG#%l$we}KIYZ|bC!pwE}LN)b*K#oRh6gs~;dMzb5=sxF(l$3XpIeHNruoVi6b8Eo_8wYGdHS7>J692mgWy6zc)(OzN<3NK^CN^#N;ifUyu1e0_GUg)Bs(jf6;Ql0e<%KI3uHJg)$~9VYm2*CJa^?EimR$eKkA;{0bv2jK&i<yF%ekF>Lq14!3rG7=$K~AAehhp9l_WZj&V+p%6ZYk1iCD5Y>L1<qwGT@vm-Z#T_CoG4pvmlwMEP@JUkiB-q;87NQ+?sOuRSS;@6TbEl942aIlCJ9UvmGsAO47YeDobbtod^ih9039i(B*<OTyCge5i&(nAV9<OU!C0_YDGEK2TIZI4=G<1oQcBdqTyWAB)oEHO(3+msI~W+rK1aH4^IBmt2;fvZ=GUqu0D97IO})O#8ZKHFCSLr%IyPW_&K0z$VQD0fz_kk)>JyetzMg<3h1WOSn2A#~ut78tN-o)Y3Ic_&e^W2xHWl;OqQb@8T&;^~mNme=^j2!6jF&Yvpfhq%3?n+BvLAB8=J-$@ZIZUd|AKaUSvvZ3%|-P%tJ1>qu10qEUj}QyB0Ew<QmH9WAztbQY5mNE5>rAl6H=xPvm51RB;-kx;cJ%5fHhog{eRbwO2kTr7-p1;AjI?-;X&fktbYEYHSk87GTzPgfYSKk^+c*?JhH*$He0f}R6VS%h<I8%3YKy<2hMw_+9iWxF%wTYUd%Xm<^p8z#D!F%#kkpulz4oZPpKWN?=;lSuE?+{m<t=R294dXN@eK5D%+!TDsG71@MBm9asiHuQn2#bcy0FlwrjM|toS`;A+@Q9$51#au%i{7!L9QcR&U-BS}TsUXb<8&Ri8&GT!7_sD%gTb=BT$iJb8Ew|LN@x_Vu*i4;-aODf6;^-?ee8o%@AvY6wNo^}aYKeO%Ee@a9Kp)Wft;`3rnM<=T`};o@Ya=e<wYAZ^(aP(Y<uMw1R&+^m(2ai|mXc@OM0;sOO`@CER!gkd%hgiu3ZpaKv`x4rga5SZ*{!9rsk)o9rIN|qVyWz__E{7opG##<OX0I5CC+J)>?BmfviY;?Wc$&%`2Vc?Pke5D)*`G`^jk>#d#=FUBbGQu5T8v)tggeasCvkbmKNTQJWedOd3xmW(Y9RW|Jx15d#V})-6nKvT&>T_?+<Pji~-#pIgXsvweid6)T3IlX0ihDIh3n3DPrOgilV6m&Ib|FADF{cY6G+V5?f6BY&d~?9;`tZn@6C$+mlx{J^uZ7@oE`WHN^jz&Fb0ai4pkBpCzduU|~G7c2$j9B$2uBYQYiS%BbavON)7dGYCp68V!<;y}?d~epD`7c(t%6A-k4b8PIKa-L7R{w?W~iUCZRD+|guhG-`=gj9Mh4!7kv&%e5^myjr07l91whRpaWO|7m{~>ZtbBpCyKe%*pI=2en1hNIcv5r}@r*?##lQc^6_OjDO_aTly1Y{R;o>-l>F@>-WQmxLB}E5XWa<6;t)!W>(socf{KBv}L{MmwEYR=Vl!E+=rc2y~HtT=aT+>dv{s>@_w{CnOeZ}e{K}D>aJ)`*IGSkYO_N9D0pFI2$2WQbk+4v9ig!!h(E(G(A=~dZ|jHJ+c}52YmUyj9$y9lv(AF)d-___dvSTqglfmHyt>h+z?@69j6O>2@@!)qFZ=j<e2Tw$sKw7X{?00VUKH!xwcBAogS)u7?wQ}Y%u6NEroNy5W2o@m6bXhaHq~dN!q%<v&%8LRXRkn=K}(CLj}t$B_bX+%8D-Jy8E(l!+lver>Mk|Iz1+#r;MFqR&O|+s;g&=)&oW$c|1tGj)%TV@?AU|U$=!nTrxu%cvq}6!hRd!_E4t-eR-TefQ-&K<e=&*d+*Gj~wwZjqOmc0=$1vCR6&3q=e-GKzLP;#5*)tWwt5YpvrN34QD(AAQxoudMf$}W3U9kYvytDxH@e|u$S|qkR(2M$6Vw;YUDt<A`yNRZbk_$|{nel{MO`j#q-Un7L9y`#fB1K92T5NjUqChexxy?aZp&+u$X<Z2~zWM>KtAQ`;D5XocSubg?E|LmGzG`rmx*kLhgpgfqqbVU}p1kUK>Uo1AT&amc!SPjGS#Ha=mon0t!sjtMmq+&0#M4PqSwPKlXavB(DsnH(tXu*p<3auzuzP=QA>p+sX<)=q#p}quvNvj6e(h0F>ezzgFzp`d{NGc3TfE*D5oIWs7TiU%xf*&T$s`Ad?H*lfnpxVjagE8`Hx%-^qih$75YRO}^={qc@s@`w-=bZiA-Rosc00JW{EpE13b_RV8#*?8s_&@BwLt}{YrN_uQVH$4(CwfWQ!e2U!o$Du?sCPaQK*=MX}_%Rl#sZ+6esp+5+^RX9Uf`6jDZodG$rXj1g87RH%jzbP*cL%NZ4*S6DRgksbRvEOS(Z%1B6Pb5wZgc*9y-NSMuy(GxqoJIE$d5UTzWt*NTOnPE)P~4eX}M%gS{fB*_(At=ceMDxbJTFkc^_B_4H4od?)p4R(CFI72kW;y7RB2m9Q+&)v@X!yj9S5Or9)x>1Bkw*nvthy=$Y7^<g7Wo&8vNXhFmsvg~=gQA?dER@^xpo)XLN1Z=>?`YO1rwB6c=P2x<a@|8uE0o(pq4e@%B)H|&e)5&dD4dlKLbEXrXz_gIH}ushlM6Ls)SObeV_zPjp<FJ*J=PaYgGcU$^F2xri1!CC4e+0K^hP;p3G#adod4*pl~<3HW>#J0P&HS5wZtn+ww@}l*^K;qGDlYopHNT4KdTfRu?(B+sycJ4iUaKNNaLzw3F4EHO$C@N5eoxdD(OTGa3PG`zLz-&8PIa0dTrx68ZR0yDzrTVIqUh-J4;e8?kiV5Ng>Fq)$1wMNrMN&j<!;19Gf#C8k&R4w`>!mbiydLE}aST`<?95WHn@gq8=9a$Z9A6uar+|I<HHLmDp4pWIT<9SNqf`O<JMIe%m4pP3PV^AA3UalZDi;l8?1vlKbqoQ!>{0x(~aoFEby5;sq6@%Okn*^j(=87LrLtBXQ~GzCP(9`|?(6PVBkhfkt<OeF=!ab3Y_^O*&q622x=BkzDmf#^s;LxFoWm77aH&(64F?<JQuoUYca|4`D@%kfgHb5|}s7Gp^1cpL??nVbT>sta;aAmUlt5o$4vMqk(cdOT8$84t)?l@-?Pj@%P@nbS97Ew<?`U!Ji{KJ0fOeO?6f@3sx~3<`pxo9&YJQHI3Yx)wAxbdX}tiX0}t!Mcph+MYG|_qM41~S~N>nie{>e`Ta%F?9APGkhKhUEvT4v=hnu`gz&95FDsYP5NK&<9K(I~M2AC+BMQ-Qtz6bzE0^&+q0A#unOl3^=4%_d|I;TyfUipsAiNt->eHW}bQL}^raxWbPk(;8!XKaYUkjk0i2t96|37BQga5?+|HS?O#Qpz+&i#KY!v0tPd4uvla{S+l@<081lI$Ov5%{qe$KSa5nK)*F-y3gE2<)-&?W|q4EFA`Fp!%lTWyO)GKC=D;fl)?LzvTOe>UGIl$kUYh1;agC@x$2qV*RgW(e++g|8e$$o|I&RVYstr?Wy@U(rEX7POhJSuko|$FMRRHvhSSfK$AT*G3_8N8}-Qe;sy1-{yB*Q%)bS_FX!KVgwq7S)CbVlto+>bZ;{Tv#q{+TS^*+|d4Zi^3P&>_>B>H(58%|W9Y<9Cv$DLWM;0;yekLQ(oXZH@9vi%vXE!2L2J}Kt08+&SF*u{A${oZ&nJiVZS0;x+y>~7(;I2sxgy+--Mt=QVVPO0vnc%|>qJ8I{kQz9X5pdP2@$A{@7k~4YD?$W*;+~(;$?cfU4eoh(Qa9jb&pvUg&Odn&Ka(a{e!DB@Hb3p=Hk<z9E>D;G;surA?#}q~bDav?$<{}tCwoS{ckx`@;9Tn<O!5WpQcfW}^>zHkH}av1737<5d{&6y?6O>5oN!f0;f7ej?1~Yb5+-$m@#2Kb%i^y;vV;+y<LiuVKK@(O(f{XnVIkczZ3Ycu*7XU?mJj-p1`+LV5~B?goe7DS-{wlTqQ1H}ch<$JbQc1kJAg+rb%$lq1qMsW2ohKkE!&Ig-+(LRf!ypz4)lbJfGk6_&P^14(<GSrb|Qv@dLcQQvU-N!EZx|g*$PKj9iF2#Y5dfrL3gql`!wdlOC9zk8&!N<(=NGu&OD;dx{6Ce^GN3dbL(TGx&BQXQ+Gam>uSflw!7O4UyQQ>wb8X_B1M<BITo3KfT-jhP8o5++C;uS%5nt0eX&{Dn3`zz<pr%s=d==|Q%1X+=%vK(V8zarRA0tGrpqLB%_k%9m}uf^jxX%%AxyVQ0m&pJ7cI4ru}G_O56u83t>kXtha~1921&=Xw^>uDp$w39xbJJ*nMmT2tzc-J(6%eXkX=+DCr{njo11yPw6JN8f7t!%i%sC3^JX82dWzMXeGU(A`Lf1u*`dtm#_W?TJG-swc*~f*o_a@!3WOfU363jOGM5zvDa>n^&=uT_M9Z?YxF7QwjTUJ%#AZ22nSH&vvdempm=_n;Y+NT{M`XO?!x%E*fpSEvxIN%`wfoD1hczt-Xv|)M-s$8FL(KrZ^A_5>6ZkCI))4<f`)`1lQ!bCdJ&g|z@Y=)xXj8_JD7OwEtB#udQkC)}07yjKDn10-4LCKiYpGL0TJ(g<irPWhdPO@2<Y)i5^63s9$+|@tt~A;pDa$ytKG-g<O5xZFM8a5<kFg!u{4dNm0EiDchBGb!7byEb!FniY;%OI{^aVqh)_A7uS#Uy}q^V<cG(ryA3MOGsICuE$N#+7dSjnIPa6<sKp!HIhQIKxE3})G;aKnV459ixg^A<M~O>e1rH2ZRk^vg}}OgTtg*!sx)1>I;DGCM-3;Pnvmc-hU}vz}+mcM-766EexX%y-c$sH*tT^m0<Tsb9pH3@dq{+db7rT~>+0q?Xax(aLGeHtNrK^0C*S!G%h$Ks5O;+%LxT-54I}?(#_b&K_}O$T93;X#!=OzUChuqdwDfxJ1wl8Y~^BI=Wd9e1YRMC5h25q<c0*e>Jcs?W@~x*{Ke)DOY5rN|EaJGSSAs7dN~<o`t&2T*vpA&qw*|Y`t-$o!<#@ye=0NsyZ@okPqY|A{za?Xe<eaG$nkRU>3oFkY21nm~fa6-%|Xp7*EuII{OM=0JI259jrkbBH+c<X-!W?KC?}O>?BAAN5n_lR^v7{#4Y9QIPEw!O*tvZX~x?$B`GRPXhi^8Fs^Z79b7ccb0d0rWi=E$3T8<vNEY2HI<u@y|N2`mKm+&)R~DdKnA>dlM|jaZ3BKJjnas*F<qQ<H3=w2Y{4M5Q64b4tTcNJB#NR5clx3x>$lEwBLs*!~q0&eL>Tw&N0^DveO-g_+cVO>i_Uq`r;yj`7WwC1x;TWpYKq69>a!6W(%9S4A`9^qcIfHv#sQy2D>m2`Q!5qi6IXMA3%fTD4KXG9i=9_0?1AgsQKnYcEKo%>(5@#Uh0q)gG$Men15nuwwh?F)wvhFRZ{#jnd(Ul|gwAJ;vGr?Eupq|clI%3ZQlKBf{UJ^3jYjj2!+Hmo2ct8;_Hwt<Z*5H!9qWv@QvPsVHG!XN)rIc}{#JON-DiD6f7~W%TWvUuYv@FtJnfeNq)}a~=556w1yQ3>g;9#j=r<}$btDe`zp+g+i7phhbw6+NHhbP({wk%r;&!pe^O5~p>z@{aF^%r1M$`O=Xvdv4dX^43~>&n&+E>#t58Yq^4SQ5zvU^3nq(o~vP(ooBslN}9z1R({Y)GRTXo2QxRO8^=%&0wY^{Vxc5tR7PZu5qJO9E<84kd>g<dUI5YRS^qz+cQ$$b);#C)kaH(R!gZXX{PcHw%o5w49A(s6-@BjFs<b60(C0?=|CsF^7L_zI&E)IeXeW{@mU{N?JEB6hmv8~Uz2C6G7P46^*)ps;z&PDmWk5b`|VVUT1qeYOO>LT=)$=jwRgcJikzkTQJT=<Y2Ag+zhvZING~WAH5!_4Lseh6&}Qp6kki{pFZ7k58Lvq%SfHGZ-2AagYVkjKhf-NfpWUowG|AQwUp@P2=?rTgmP==2OQ&gkbXuHN0MVDXmlb%MkwdP>6_c&V;DugRC(QT`Si%PKfw_9Myj|4n2~rQzfaEqi&?Hei3z{=i+NY&#Pl>ZDW{Mk$y+&<z85$$I98iP72lZqfwPX{wEP5bhfiO+)FfOATXj#$iE2)GgB`$3fjMfLZ@_<zO_$Wm;7=|)(QLk|DV%q`WJ%m$(+L$;=TNdHIS69Yz1y)p&GLOi=JjI<aUsjhY7vSzmy_fY{h`q$41(y|9ovxob5i_!M{fyW?v$(gg(%K!CRzY{R0%oj$acOJ+ToAb)K0@`h@96CMTy#)q@K*S^8XAU+pb*K&ZLo@E?z}LNTYWUU$vns!MU=pB5R-;*sAa8cWq&CD_YZVq^YJYS3_X{UYXk;Z4mV2<L%7iXc$UU+Mf+n`1lxKOzoNLti{w9|>cdw3Jg9zAi8kGJCIb#tUbcFH0!VwC%rG$OcZ|bZk?wAj8PcQxLJ6-cd<N1zodhJU9(9w_fKNA8gS^kvlGU*GlBz?YXC+mD{FEBVA~Om&_?aNcZbs#oEJ)XTsabt}E6#6ysBHd{Iwl2`ewNKQG5d2}GE0#HHewTXY!K)AT*9N1G^nU!@<1LFdXI#jB-ByFcI5FdsbhGQIlYP(Vvj9zdgaQVcA!2osMX{?H4|~aru9Y#l=ttHBE2lLzb9QNi-@Q^DB@BxTQT_z!Mq4$p~z^Nv<HPhQXfSf8w}ZC2@%Q3>-9_d`th1z<JYY;@vbrVHfan2efI*%rK@3=!}*dxb}Q_v?$d?0;f=9wUL}`qP{$UMON_Q21)bZHOLDZn#U2YAa*pLJ{Iu#)$IqRsF0oF5)I!pf6O&BJ*{U(w1bUuN)=Pc~Oy?=`9&xrN!}3m)vZ$8o-7MfHjcAGpeBFckfB32~x4j}Cep8BhHPd14slA-R21gaMMA%E=<xcvKZbPk-EK2lk`Q^=R`Q<~EUrtZTFXx&3^7?uCWzIGT&`EfiWJPK9tuIxV5!~Bmq|@S@CAr)!C6~)L9j-|(w=3x_qaOc}C6|Bqy|2{sA#-b`UN@t9_e&S+GKj9IE|)>k-4@l-_Jc+4rmKSpQ+L{jkTrg(JMSvy0;RZ7Q&MYppPo?2sydQkRGGiIQeTQ;nFRQJuhQF+eI_D#ski)$h$NSG|2~Qt?KfZr_rJMV!QWGMS@z5CdBDai2_^<6*5)y<9QEJWs)4=Alv;)=5!KY}vZ>i6WGI+ej0t93CYVueVOp<WW|z$@yKIT<u>><r*=4vGv*9AUEbp?^vbBsd-p(j776)vf=Sd|}9|-f#D#J`Fvj7Srm%psa_K}Ojf9)NE>1QaAEtcT-;)akXD}=mS=odnI;M}zX(KC+)Vb<C*CCnH%5ns6eGH6DQ$EzzZ2jG@yw;(eZ06pA}lGoHzUaY?@*I%v65RciK{Xth(;X8_`a`DAb`f1_@TKOGF&SbJYuxzfWdYYbzM7c%Z)B5ZDYL>@k;x&%$qf6g~;lp*mc)``kn-3hootANJ?19mhXc5;MI2v79h`kBpt=Pfr8Ut@BYg>f2#JHx%xd~EqQ*Xi4?>t~It)Go1mI7t^G6uDv3Lpxw*iZ|l3gBepeRVzX8m*(CvmzRI6qlW_n<{sHX?ei?GC>1lbmJ-<mO^*Z9yg&or$HSUyhFd-IJ00yXo&S&o^61A^frS33vVqtc3Fic&Zu_0uHo=JG~+86;tUBPD4viIGc;bDpm^GX$@D3RRL}?`=~h}g1(Tehc*@$j;T<L@-XKNc1jJNL^su0JjAa|t5GgAc1<1oL)oTyCJwxNUy_*EcydY!c)jbx?b(u#)*s;85reECx6;al})1LP^A>qaD<ya-vywjdF{q?y)TYTkM#$@gM^BE?ujN^R-GYQY4!;#exS+hP-UfrsA#I;|O1&s_eRLXmInB-+mjvJAQ`mhtGtyRuyhHey61N1S8=8_FK)l_g8<sVr*V<!5#!?dTt8^S~@e4L3AN>)~gu1LXm764@K=HkfYxM!WNT*yRwwUvlObY8Q<oC)|NgjFIDB0pZ!84W9$xuuv}ehqjczEZMlNz#d#uEoALFB75KJt_-|Q>k28$^(-)<p4GkM+eEftn6Cf$>G(RN^yu2jZ8spM2ZGVhqpaiVhz0zsFxk7qm3JZ<yDTdC8yKTC?(0vFJw#i@JpL&;3)50tN$gwS$F_424Z0T?|!J2=xTqvd;#ps%ChW}Ekj&`Ts(Im>uA}OuPsBYu-P&MY_l^+1Pl}|R-#BihOG*-B)f_!=PJe86Q?*87{ES~HP1{8Y?f`C{CEQe)~nLV$<3|Ey!M0PhEQ_8wkjP*NMr+)y`Y|9l3$&zO0{QBj}g>8$om{OhFq8ex}Nx6bNN+Xy><UmOvcAwlK#&R1<2T<YjPcsp;m*C`*X9rTWE~AO5Fs-m{3DE95E1@=4gyC%Em1u>M*gdlq<$QLtEiPhLkMfE9Q!~JjY>BFSxV1#m(XQRFh$c)+d$$B8QUFBK29*)LKoKj(E}5YxrDx8<JWO<@$MSO(RhR-Z#wY%cVMwqp}Id6a`!MZXBT)m>i)Ro~+q^eIt}U)PLt6Vsu-xM7M=SGwj6xH~tQEN3JD`if)@1D$-e%f?eIW9i%VAxCs<+4H3{SBI#UN(Np5vzZ~Os(H_g+1dQ8neiEnqq^kBwk?PZ*pRVwyEBpuJ&rg@)lXTrD>AFvUev+>HBwhDOy6%&7-MdQHx#X`snCdUhN7Jyg<te>X$xcX0n6lDZg6<~N?18~p`ME;tt0gNxm~I`9P^Ig9Jd;tAx%jACH_D1xdv~V(W-Xd9lSq?F+Cciczal**!)>!*P4&U8KNlm5Z=qgycJOo2x3wMC&OAJ+TNloC>+EFG*~iTk=wg+t%QLyU9oliDT7q=bUZh)>uj$sUCh0)Q{OP+~iq>5!)<rp`CU^OjC#|~kuYeLWzJ&~H^qNW5a6EJSIw4;DF1!v`??}TDV&BN68~2pt=v$hG7b<oBT%rz<p=AYf?dj_jP0TKyYtl&r>+I*#`gEiGoaK`jQgQVKVJ=#CRkH1cPu&!!yC&=Qyw=-X(yOY}RS7dSJf$q=U#L=dsjL^`2N$aIORc()?DzU0yU@4f>P$lMri_|>g-ao}bX_NIl#qKyv~KQrQAfzA%NFYOKU1s=7mu82*p0uug^b<B-DhjvP9ThWcJUc4yr)$E#tWFPsonYOs()9d@y_)V<0Mu%eV3&UpqmLqh8ve|dc;pUcMIj5g%xX6;hewVyvG0UxZm)r1G`7x_T8&1z?&hb;SN2@UMg?F=R+LsNmYQu7D%hjfIkN`!{Fys9wK%ak7Vl25z^(GhJS`QG-&5E=s6H09N9Y&vjea9O{VW@3GKNY#7pj~X#odo*ck2YmFT*lOO!Bs+E_nv@C~VeE#Uw#O@|E~A=~)p#h~igo#eB?nw1CB5c{Cl+nM7nISibg1htl*_*cF{m%>1?t<**$xTUNIs4co{A?RzyF0L{xH#<8ZUeiaKIr5mjhb4UZ^tJ~Jx#8pGQhY%@oThx-5B-lIdqHI<fIS8em%gE4N*B@E8-PM2f(i0i?z52oXcvd_6gyWiv2=vw0Hfj8E$&^{;Hq!RwNK^Sly8pyneKcU0zWkl0Y*4cxItiUUBCBvok(X(LL!&^Z1AQE2u%fBr;~wEVtCV{DRzcF1tPgzS|q|8N+G;K<}MpLEP8K%KMB$h+0tH(Hy<NQ;t-G{^6(Os4>}IW+;P>00oN(8X$jok!2GhzPz=w2?&q7z^+D5}AmSAwiYQHSXv?4G7#btds)S162vkC9+4S6cNR5C;$Jy8tBJ1VSOG4;(36JU6VO+_!(t}9C&Ls5EpxzR~Yd}@1kPZcL-%xF<9QKX%Kxq`oxZhEeMaXMj&vM5}iS_0tx`semNX+3|eD^Z9%5j{!`a@+tb;`p$(LfZ)D!=@Yxlcv2;01q(v?nsA0q!a%c@NnsV3;;#P-~;bEQU}bi*DfdvmxtOKsc3e{R8lHB0H5%XWsFZN2;fl9l<Hsw=jkdHd{<tdW;QP5|_6l?!Sq+2sxt9*mHBWp+#M}4sY1UOmfM!V8;*r5N*xh{z@JAGAV}}9r!gMq~Q|Ul!5>2h;UqUUN!<;%$WluXjm)0x2`){@r@^rXa*UfBtqYWuIlqls1X9d4c*k0A#VzGXBN}l0@qYQP1JBTS4cm@HH~6~0%SPCWSc50=m2d>mz<ZXlDFWz7(!`k%eS`xw_{Jf<27tdHfVH~Cfe5ar>#DYcM5yWG?EGkxb+oK($T$hL^rMRb%s3a#)k`N6F`4UstXx~Wek+K*s>K*^X#`8jL|;}WcrPFk?82C`PRa%byDeAxxQVfbd*JQEmp-O(Sf@isSj1|2zH0Pml$0MA8UpKXm#M1Xku{`NikFh9YrJGkNB9tB}zn!K*BYeK#<ToL3mG&uSm%lfyB$GPmH{jvqDgyh8u)2Y%@xR(_mN&YR7S;Q^JZ#6VX1s5=<g0q0)gZS?Cx$DYpyVft5m-M2jgZ0s2ggjYQNpfqHv5)V9R;&NYw^;hvc3P@>CiSv(l{FgnVD9(U40cMk@*^8RnUHv-5@IGE28Kq}Nn9FPT**e{8hNoodQCLPi>DqXVs32n7oRJwSZj|tHhutGu=I88Jg-4hf{qOf1$BNai25kBL~kv7tgoXvYIE0wcJ%ugG5H5emWM*=%Ow=CbMJ=iW`q>9`F%1v%2mdL;gS2^cn$58&!xtagZJJQq}nH;~3x9Oat?y>avz-P%(_s>g%j3%d(40e=c@okQJQ#tDXojB?uZag6ha(Ge{L>%=k)Ay!w)Su7=X(wF}<ETRy<bt5CTxR87APrL4>6t#-XSyIgM}1!j>bZHbC`de41la~t1@>;z1^GD0vfuyu)YER0H|ucbLUx<KnXw=~B@j~85U&V?c<i$#fO(t&%wtW&m~)AJz=#=c=!MM4Pl>|^SzD5v@Hv;WAyjx`K22gFR#AvA^PCo=Q$>4I3JGGnT%&eMHJma-BP<ealb*#4Bgvn$JKM_c%r9kkeglw^zvzC%Fe?4)2T%x+(caI*uftT2DU+|=rJV3@VC}rSL&~J4mnna|!bnGDpkz9`Kt+()KGKoBMDu;ncKb_Npxg)MXb4-eEK&nz^_JwP(<AQuo<z>XmP|($RQY$pFQ_@hnsBYC?2DiigG^({m%?F7rZaR*wUTFf2)R!q-K3s^*qyhx+)Mgdd6{eIIbGH&`(7s`<&>A9zEk-Y2aS43n8ff`-yz?{XLV3d?(b~=lUHQq?I@nm4qPSd{^i6Y3@>%f<hX9rKKMJcFL0i6wz-nZqSXN`(`|UKuw!O`SxXi>S*X`Mq{OgM?3491Fg<wJZAz<jQBJC9w1Y!Z%{YQo2b3UlU|{QNCaKM11_||Gi8Sv8Xv1qqxsk>=R++#^pw<cQusGm4y})j2`9@k1f=x3%>-?V5d5J<9ZDP4o5^T)xGmn2SHBaKT`F#m+?#RStpp@f)?~Q${Y1|v}D4Y`GuLsvn<HXY<AzKO=)3204F_c}*4_tmkeKPIHC`a9d<0A0invItuwg>k|uqn9RNW%leX*u-=N@SPJIJ;Nn$lJi}0lrq*%{5%8%Zz$-aiv|x0T*OVvmxBldt;p)Jd*?$har5CBs1@}*(&@^!VYV2WBegq*@f?)P%NfTLfA4LhZj6gQWV(lgURIfU^+-Hcq|E{=llirnguJzNZjF6*53VOdDju0t4wMU$~W7HMTd(>5b<G!eR*q4L!`Z|yZH^(Oz`__OwKZ&R;J?Xl)l6J;D2|23G=<HP2l`b;p8@;V`6|KtR;jT3vuO_Z+l<n;cILvf|zp2Wr<&uZ<B-Z+E7Zb;{Ky-kJpBk%Lu+KEl9lWQ03Cq2P{g;+6FIz0LC?H7OYB@TSNW!kkx~x^ncJE&R6loU=lu|?&r7amVg(^>PDI2nc|gnFrkjK<S=lAKmvv5;*Y{(v_((cIq{Z91cS}CWXu{az;@5e>3ty?uW0>%p4VZ;^|^eV{=oGd;oT3qKF-pI7D|E`(Obn{rl)sSp=GCEi!w?Tp>?T`upcNBy(A_ZYHV(J{WH8{xTK@br?s6+cQQPIuyn0<3()rDJz|!Uwb!FWI&*Yhv8_usepwij3k;9nkE{x+(DxJx7YkO3|1A?6Tw8zk&%{#_vwWl!Kk2zrtR6WQ4qPl4^Os$aiw%+7RZ8M`tlQ%H4@>R}rIQQB7kS=UGN&wH2e)e{=`LNQZ3E|lBn!XF0WVi~K!SKfx@*rJN4=|=yCJDzYfkju{6jJwDa_+T1zIE2ON5(xr=0fOJ|O$d4Q@5du~@5l=G>B4l84PVWpqiG5h;i5jSZ%I-8!9_3vruH{-97L{K>78v4iKOKNFiCMQ^Sonw>w(GNT0jK<dQRfTu^Q>n2OiL2~P>YGbnY691ZcfA~co?YzIHqg4}%#+%ft;agz1gn`+b))X=U8re8$Eu(dy?O3bgVbJDbs0=jkWd>z-A<F48LM?PZmC-7$tjlKw|HJ4|AZzs0?4QzBQPe=y47+HHO24R%e-M7!;?G}pzYx<lmJpJ@jVKE|#Vb;^dsY-*`6OA)^7v0+UFPKDR_C!SPaI;7uYY9W4rwC83X)Is$dYU?um;OB(e%79R8hlVTFDD}VC^yAhjFhVF5#nP&#^mUP7HJbAs(dMnV3)7UX`=L6v_7bl8;(0V|DIoq?ma$NID*=8OwJK)bm3Ac(P=-yRXopU=mFyTHi<nPi}ztlm`{xF*%xtNV%Sv@4W0kkOkZ$UFi-gA%m12e!ZkT&Ccg<BPtD_`Ly+^T<k>7zPF$2!Sx-oo;+arfNVtOy4h6<^rM|1+L&8JE0sk96`Z3ahV?8u89_0t(<5y_v@%B#Y$D8nrIEZcDWV>UXGuK|3`u)QBkY0#f!x8$<FA>;!b(aZV4!CR<!5(%!FL$ix$d(NyQM=FpZZ+*KYlcqk|=#EY<Ah=&=Gz>+CH8=;m<FVNP;{c9TV!mc<NDm&4b&@?I2ja2`T|)nPm0HELal)wCA%;N1R7e%~Ng+Zk_77-`b8GKY!;#l`}?-=4)c`PslW1Rf30F^>rn96KlRfKR#1}hg3^9r*(EFm3C7D9y`c|c5`Fe&2nimwU%oF@LE2usI~MjRDX}vG3H6lw83z6qhQNIFpW)K11sJw9qmGOv^zdW=v3qM<CZP_j}T(YzWMv61f3t4tRG-OR);EtOqv$kc!;3i!KQ~Bozx`d-1zpHJ3n09G2BR6`eflIHGF07o5nmqR;;s!8lu^0Hn*Vd;Gy>*!9?dD#?aHq=QX4j)h&B(l$0p!iZE$Un2-+~=7E}#tlfH6Z2@->ef}q9fph`{S5Y0S41-pni&BODh40EG50}NW<rH=-ivWw!AcAmz9QGb?5NzC3S9aD6#Q56c96ALZXpfkgawhH(l0^y87Fzg&X^zBX4PhjnRH<yWFln*Sw)mH<4e;|XQ`{k29Kuf)Q@pR@c36ZLoue{8qxuBU!dhzDm6+c2zPyaOo!BYv%8}+W2FWC~kpgz~E`#Mz&2g#e9eb8VDbLg~*#d;aRCeqU0B6`!vjTn3eKS;c2+ZhVHuP9Cp>|i|rnQR72kpuW4pP+)59KwF($QhEzA+J<6W_a9mBfn{pGhJ*p2OM=oQLu6emL>eF_>R%+-;j>*X~SJ@NyqP@%?!)578vtP_S}Vm{yT`?(ac-D%XW!YTp5TF)Iy^W|0&;K|a(nS_&ADX3`Q{G$|Aps&{1Vt*98ixh{q|3+zujdqmSznqqsX)_R`d-94k-Z?S!SE2^UaIEM6rRRM+c_5~sRqgSHSzwjb7U>R25E0cyAT;*1;Q8yg~O1rntm|Z^$WO#Fl5iOhcd5=x_Kq0mjjK^Z$VGyYTmaXu|Qq>S1R)L#K;V%OEQS_)9xOIE*8dIn}>Ms6Ft@-6wnBIfhC|f|~29Ar8DWbv-P>WkDG2x=KQPTbjFT2BQ<d2J=2lXAe>d>4F&vugF(4OU6KVI;>)mMP$W#WwxqR$X|WF*W%dZ~i+(i0#(u6H9&uc<h_zT)&eae4y%3#S)HoL+MQ(n}6k?u8(|@a_n`NYzIo^b#%Ba5SOv2z?AcH%H|KgXHCgc)XC_tio=D;YDKbP<*@%y=#cOYtj$P+q3&(j<{1?#+g^R-TK8?JG$buBg8HlzHar+!Pouf$MnSl+UccAOgD6-*;=B+>G@WOrj2=~$=gxCtF1Cj$xXYVQ5>wDsYbV>L>L!n(+3;ZO74TIH^^8|V?OP#Z-SazE!#bDF{<o3sW0glsM?el-MP62Qz*NsGxa4POZ_BMnYlg=kX{O^$j)__Cdfe#X|gljrS_YkyYw%<2RH9gukx<Cd5^;|p^(+J?9^n(#A4>-eFqz8Gx6RzQ(qb-cL$Ei+IeMO#`b;15CdC0+IOeea*1Hx>;!IyaAilEUKT9+Dta1f(tHwRuB?MQNv^UVoZa1)<#^PLV%Y<(6|&1<?8B*S&7e)sbOtWmD3lC;>aDNhE%Vc>p6Ij^NWvmQTd6|V^1=r_(g!_i(l&HJA7<X?iFTK+UOe3gUAzc`DJ(jy0hQ}V99r0RHEr#2od!-??LN}lHkT#hv~7vxwTs<Qtg>AG)#MY@JTi|w*w(FV?+)cc4#Ei<Y~eI>G)Ktz=e{Xdbo12Z3}=^<@8-@$7cy+N)A$?Iv6%)RbA)mUUya+rkWSRO#Wm9fGm+D>cf3PKMi*=vdFgxZzjiNl90#;H<!`yNU@%2W>zx}dOOd7nc}yGDhOIXypM2KeAz8v&q83egY2Jj-TGZ}U9=dah>=XKJ({a0r>~kgK>2-qBt0}JCS7v)Lsy%>2WIev1EESR2g7o~Xm2O2cc*;g=DH1$gZcjBP*H&$9(ESYGXrJvv!`aUuL0RNwXvVRy&9_f46PDJlkBq?8r!VjNcJRi78oyL$u!CwD?&J8;jiGh;0#yvX>B2d5SM3Y(A6#XQ(l#}ob7EFU8+e{Hv2;R9H2Me%i9e#07ryuf?R?U+JD*1yX>XDLHm|5Dj-lx9WQo3qBO&S^<=8vxm+iHg5sZM3h>dQl!5s=id+jkEtm(7TCY@zw0m}yNL$D&;qaS;~BPAsaerJWDZt6)`N1-H5k195u{9uVk@OQ!iXqSZ)xSaaHj*{x*nb|HLbR=R&KviOA=)S;;e%hn>ib_v;<i9UhZunWGj~LkxoJjY~o`fEC>A(wV*Ro8f5>B8*kFk!<H_HgIlX1DnLMfnK1BgKGotPvIClUS~Lo!!BLk4%PhYJrk-;{ba>bcS%JXi+gow|iCRcj>d?O_RoEd*VG@cjV2S|h_s$mW^jMlWsGT9Af)^~S5kQ<=G20%Sr^aV7Q6Fm+{m&>oxKNoA#p#y+4wNRVd{)qM5UWV=j+3$=QQv1>gwb-fzmbMn1}HwiM<p;~V(UP1#*p1d-hz3slDXbv=BpJ@FG$vPlpVm+H5l5*zTld67paIeIz*-}v5tJ_Ic1Lb`%9>d)!-*Q*Un$5pv>(dv$WOl=sPfs)79l)Bn(oipp(&y-)qqy6KZcPPKNVk_Aw^OX`?v#ZKR)_Ol;r?rb<`_0Gfw6iL3XC8&_<hy}Fi8F}lc2y%N(f-uPe}`WOGRZNnRw;OWY~2<ZJo$ct5Hx0ELle^A8~E>)>pMjUt0^9z$`nJUwht-@^uab%Yh8o_|-l4-Hmjxt%|gwHaM~>)r{Z+iacIrzTx}+g{#~;<uz}@z^)qS3{E_!d<V<l6(D}9EGNSc1<*gdVULC8!mle0IEC|2;i7fe%ztX-8A-gXo+}Ckkju(7lbE`WV-omMA;wBVopj=N$kAc12VL7BW)NK+LKe9+bWIo!<!u*3<b#{ePOkEii)5TFN1?8JW&*nSBDO5spAz^463>tCHLLV$kT*W!{o?m}CF>^|0zrhU*&E|@J@tsMKdX{Jux(ndD{uwUjNd(suIq+sP`hi??5OX$_&0u*T}(e7U%N^z*Ry*)-S_E2C1(IGZ0cG+Mr*(LUiI~<A|4y=E%njUDb;kN-uLOum#3tVG>*pc_`$$I=DN#fY`x92?5zSO^~mnp0H~<A@}AHC$+yTOj+kowp7!fn2RFn;dB1<90y$uzC00TY+xyQSagGN^{Pq!@iSqS^2h4_(1LL?Pzh#Q-+2=qd{0KN#dCTw$^=1~E0ssl#^lf`qI}>52NUU}^PV>s|<%Yqmp}EI8Ka|Dpp&S_{tucmsqNd9B_}NHawi$c>hNZ|iEB}Ut61g_oPX+cn+uigeK)zvX{tcXBSn_CbmET|^>dSIla=ADD>>r&RxXDH2?+uMGT$H)_O269jqZ_UBL6y=>1YOV9WAWcCP7-w<VWgZP^yJ!x)uTrqv5BJYhEA;|KU35uxe;}~G}*~TeHKfUEx#<L0vYW_)UD&PV-5KYVw@?Ybl8viH_3Y22c9Qh!!pW_Z+yd{`34<sJ5R$yI<lEyv#l4PlJbU-d0!!D#_j+m293No=&X4;sl4IPds8RC8!fUZ*bBbswZXCTvF~Uf6zdtjA^y-i1MkE5ZfDDG%Vc-#mn2q&mdJgTb3bOYWc_O|YL=95d|y^x)&|Qd-TNJ>gXNbj#31&teobamN@#U=9X2=2hSf#Jdsh_6DT8_gCZU%?4tpMaB`J4!iWU%RLI!7)iIV$1Vuy+xwB$iT*|ch1Fo(}~^lD&sxDukT3&)kZ;}Yj4LTeMgo9I{S<Eo7J72YnVBLSGo=zTmnnva(c^1|9hlTN}p_0lZ5H>Dk>rvPtJ0s{A0cNGy>AXIsAgs{8w1c{n_jpTF|H^c%{eqmrzJ7gA{Y@YWw!&APq*p#1(O^55TsrFr`*u;j=%fi!e9-b~@6SpT9;i&{|&irL~+Rnn$AfL5Z>23^6Ug*&qv1zr8O`95<<lj05CeQB0(}C$Eqqk(AND@HVf?*rI(rbtquHgxnq7^EhQXXY|Auw@4?p1+ic*=ZzTR&yZfP#U%sX4~8;b|6|`rWyi(&>yI*LnC^u|%EDqY|My-qyCSAux4+@ht+=XSR<hdxJhADmApHC?V-?!+<46t_?SHjW^UJxi*p3Gc7|>CId;^MYTpz^X$T%0cR?@ll{IDZXU%fQx^#+6;xpNq+jmIu`nKPdHp^-z&;fr<_>hBaOf4}eG@dR!YJC6HsNPr*5ikWS8jXzl))LJatPtea@b=%9}#29zJ~P<0}%T0r<z=`+&*@2%q}HVgr=f!c`t1UY5}FbF&OL^$jygcG@#q;QY`M<Kl;+m8hReH{aO|J$#wHpRu|MJRGrhglzYB`hF%tB$%!$I#=;;-lp#7;S4N_3^@#1U?);rrbrxxP{*-{gXOZy`*2Zi=j(}<nX!oJ7S@&4@vK>gd4{S=wV}bQLATeT`>V^M5dvDew+qPy0&2}{rE1Haq%$=vdT{XVd-0}qrkj@X_ogV<gNbrDdkYyWV8W*@+fRPPyVO<KzNZ1&gCrdog`N6Ugk_{3PAcXA)OD;Fa55OA_fMAX>zPXxcvf2Bbz0a+iSNrD4j99T^t-0p>=GTmGj4{g4@iP{|S<Dr!_^C=<wy$H?#w-(ALna=qlk==ezDhEnsQLV69fF{HovRJtu^t(!)_Jr{#~4!8FwJG_FR{b?7-ZRhX7?y2ujImX89YABA`5<E{K&{3Wh^OSJf=!fFsrJOjP;z+8Os}oNIkz6^-Nzk#e>r*;da}zw-jb-1Bml6bQjLHgwR`*8OOKm;?p>WHUAxIU)a>fQRhRn?~1JD)?>)P6~;cL`6Q`rG}DltMe&L#>ww^sU;cr&aq)^hec;a{YI#^advu?5Lc$1Cbu>#+$qorh@{%75-ElNe7+EAl!70F<I`YpOC#(s<-ZqI*VBDbmQmuB05NRm)UWn}hoE-4c@h5@02NC)dw|)S7)qM*zSx3}mUmefl5;pWM$x0Zz8=F=phi06DxL`EK97U+fIn7E@B>51P4xM^aP@O!GBBR>bg&q9&+)D$@&z!W|w6@y=Mc0YV8qq9~3$jUq<+&1Qlp_y~&02OxP!*7#Y!7{8R0{e5wlj0hpmC{K=ar=f)ClHTiz$}&04D`M6DL=9r{;e`km2ql%MWwWtNF+}2DX}X1IwgnZ?w)##Qomy_Tf%6A=VxfNZ^C~Ug#`2l@Z4|a*S0KraH6nb@ZP(>G40Qlzyvxgt(?v@|kB=L9U#))3~9dk`)#;>UK<N;w!wcA`l+jQj0#7i5PD8Y{g2pPwaoy{RoM;{Bu-8eegCxkLc|?l$~os-@zqR>s-3Ov8R_<a0FEUh!)yRG%#lB5hyY4|KwX>PPE+FL1=?u?PW~amm4CR12Y<*asI)fEuY=u8gf(`(+n5!EKwlZk5c%Q32Z=3k_XT$lEX6*n46qhUB4$nTE6(xvkYO6QeF5M{m>+);Gf%Cn<^Iad+enuqiO+z3#^3tj%iOUl}!9GPq^paYPb%khBu;_lL?#B;gRbpqEYPrxa%F$q`}N%(EcJU^8fALB60J8;*0siEC+ujxf@24V`PM>rVvT!G=#a`%Q86P_E2*Fi74qph@>{<5*l2~;4sfN$)Y`-zR7C8yc{Lr3O9a{z6no7Nt&=*;c@!QiJO5{&SK$9^rU1>KTp=w;{)7%#6jWNX_^pB%Nv=4Tg%ZjFc6PpTCqobzy!_kJ5ibZ1$IA$NwjpBS0jU4cbx3^E`GvFQz9u@hLE&%W@f+M%jR>hQ;TkS%xeUoE8(kFKzH=Cx&r`&;Q1h9hk)*aQvwy;>@ZI$S`L#mP;6GbSpxN!SK1rQ#I2(9azI744+P_EwgJ0wKv0{-o5U6h<bRKTLx;6dJhEYpjC(*U+T%=Yyub`)gX@5>C<lI0D@uE)!eX-DlqY^`ZPZu?jURax`e&PuBLd?woGu&46XqjO9I-n!AF;h=J8EvFJoP}ULD!^{pyx%a(fC!rv>NA$m8zk5!D^^CmWWsEAl^(yIyD(YWwp#!;Ms~Y$T+K>Yck9n0J%q~9vlR<!XxWJR7`x@a4^3&2&+O6gb(Wm8}!U}U_UYa+c>XG;uz7K`Jl3axGiz!Df<f`E$eZ~!bbW3&oC>KmR&jX-U#$ai*e1e^t_Q|sTM*3(Z5(m@20f~)W0wLlK;mkI(XE?3^FlC_N`Z+xyfU}OE?1u%t-e1Vw`DJ^ReeOlQM)c<Y)mcY*0^N11Nc2qg5(zCec5HK4KW6-$p=n(A<!XdIa`}$FImbp4Ku+fW#xp7>HY8Ze=$brl9Oe@nF5@M!DszA3A@J>4NW#q`=)b=38w#w0$K;<R6n8K<z-Cw_GKN)PS)i!i)T##aa~Cla0=}#TDA5n5%H04(=_A^`DZxDl-%=p6Hqz95=i0Sz-%VSt489#TuC)f?iW)YMhY*WQB~ExUaHJx+%X`29SkzO+DM!nh&wBg}?Hur1+|&_^Lwp`seEizmD*$lH#k9;ye8rUS$+tWfWg!6klZ&-)Y{yDk;7yDSj9w#c#ZfVpCsVxw)9)^h@JTyE@Kg6#YU*v8pN#Q{mq#<spfO%rkogTov*yqH6Z)=IDaq89H{21><|2pmoy8%U*yyf$c_NMdn>5p*vF|WG!^As_5(Sqp05a%J@M)lh8xy>bhd0_ot$UCuci7d03nriP~Y(AoMel$i)ZiQ=8w&saT_*eWWS~ia?ZVh%U7py&DR+2*D_5!_<ef5Fng=)@!I2!;<W3=L6zLoy$>7QLj95+2QJC^B;kgZK_ggi>sZ#V(i1xr(E94d<vmS%rBlrn8rCg@$9_2ctBMd(JfSKV8VC{F~z`aqhw{$*fwTe4)$--V4KM+dOxYGEoA2|>c)-2e&Mq6-&}cd`lUO2<+|YF$y>g;dgKMI!N-*pXHt=8N{Yezt2%j)$wNM+fcTZaOZ#^!#CUSGPiqQ>$8PrI-K&CpVU+Y+Or-gY^5I1MZ=vV+<clx5@{0#N^ZA~BDxUs%<+P{DlqV9E<9W<{T@p(4i-8qNZ!sq4qvWd;;;H;(MSZ!eKkL6me*Is4Rs+weAfjs?pyb!E&kwD^H&i0*e7o{(mRcduDIi~np`*2LBkC(LyWE0xaI2zW8l??=&M1>~J!-V&R2f1JJj48i6guhx$#^q`3Co$$uZJ>HYOC;J=XfL;aYF1(n-Khc3B3U5#40}_uc&h-<NnoKLwUVi0M#r|r{M=7qe#^_s2G;lx41kJOtiqIp$w9xs)!05sNC3D3JU$U@e)cbgV2$a`xC(ALi=yN1^lZ?)}e~p%!)EKek3yjT;Fpr%K7i9y@<y@kV2BRuz^I<YMq4W6+u^Q7dKUgbjvn-BEVFAD}!th(bo8Jy4uFJVP|w1;Xay|wk0ME4WR?Ry&<pACRFUC=JXJZABs>T31tV#T9F7j@M=*r?Z~*E#0p{WCW5SDQqwm1zB{lBWTLn{SS>?)AVh#<hJcQhuerrCSOYoh<7Qf3KA6P9k<NnOxS=ED@4x^03ZBslo<0+K_{@T*IHNDuJe~il%AWgYl|3=`!&%KU&1#-4-&%KzYUdWiJeE37>ztkZ?Qp%$xjQRzde`l)7B)}17WxQWlCL|gfc+|OGBE!T<;~yf{wy~3<_Ex#0DSkRPOdjDzTqq5TR(6ED524ySpJM}9DWf=w7t%V?alZ~XzS}hxxX1-Ieq=Etek@}^}ss(`PZ83Yt8kwUiJFt>j=M&@aqV_7F^%q&+rx>f33N`)?8m}u0J7l!PkQ8Yr*xk;QEypT;t0Mu6|i_r9zTwuCWUBA|>aVHG6uUx`(M(z$914Ud`=5q<a`kea??1D{l-H$zG?3-@H^dm0hFiG|H-vMb<Et_r?ODUR=~@Nx{HANVOHa^f6DqI<37u`Og$SWkb5Nn(N8MLqfh@RW0A@l{qEEcxxxcOTWA$RW9+RerCkRa`k>SFI(D+^8;!n+s#G>na|Z}efmOewO*dphR@2Y)5mK~bYiFUB=5{_EUSauqO;bV^D^qJqPeILlb^r-KKr?-vre}b76sI}tfz(xf1dvIW1YrFZ-i~5%4XPfWRc|pr(yBI&8u9#)-Nv>nNA9*7i)W{e6P=HrSa^Qq5hIie~I-<F8(?F;$QH~g<@)06jM(MT94oRg^Ff);;Wy$HWwbPq|V+oLv;2#&Y9i$ojy|YyKum1QTg&O^Sa$sTdl9VS#1v@wECs9nV@Gq{yh2TXJ6r;x{?b8)O!5}N0{CUPu}|@qj7NzFZ>dpb*W>VHC0S|cX1rfe;@yx6OGKsHk_XmeuyjMBvY?S-N)Q9zov%rVxU@Z3oJT9S%LVH!dzPl0*|fa$(?nCc4EM}-VwU;tNc_)=wL#pS35#GaEz{^HHBX82xUpNO~wlW3O2GjyiG@F8uc4cy%gEi8ZSQG4oZsW@_3v?pjTXQ>ojWz4OI+Pw6s$%XrLq_Zf9kRr?wl+IzrhF+5uWtdqJP%*_s5C$~g~l>H>{d`^&ATytd*&DGW-K-Vko@tp#-WqbOG=Km0rd9&q1#G1FFAaS2?Pnf_^d^TvT(+BE3!@1xHtKAKTU2a|@MxNF{!xO*jEvJDV4c5zh(m2~Mp1!W%pX~i!zlq_q=`!Krfp?V`=W8%vAw5<@ROp2sfnPKU3Y=%np!#ec$T-=u<cOrr*%NL`148|7{#UW1#Yw<*WO9~?+8u8X@{bFL*KNS9n$cm`NyYVeCb7wL>iE1N=**&B6c%Yv87JcU?Jl|BFE#vk{bmGPXZez+AiU)3K!``jY_nw;n$GwHY`Usc~o2ig6e1^g5TpyPPtI-E3@4PTrqs^KbtX_)B*A3R%tIho}gSD|9>+YJtLXUe8BMf?VFB+^2tP1<r$=j2yi~Xv>Iw1xetyO1Yy94<kMf5Sm=QOX2coJ0lleGfb*wR`hBgg7+a!SlOqtezdD}(#s_-1aWdfF-X5<9i2cB-n+^^cKYn4K~s)mtf@fZO+Fp?;Um`f^b}_dKb`J=*Lqh=P<UF%Y(~GQrQ-QaE-?!E)&fmNOm<J~Kc>fP64JqdPCNX+@MuPN1*|gf7wKQ66F^iSdv|ZSQix!0i&!7?cJPlR^g$ev>=u5apBkG$f*O%DWw@BFn4+RD(hT03kJ^FaQ##*^vQ*WKg~jcMXsjVNQiHqrEQX^R_&<k1;Pk`8{txocDDUKc!IPb4G4UJ*fz0sS>N-5URQuzi5Nk?Zjm>8$2S2%4s`t!O-czI_;n~ilvgPfYh)FRVIYP6Y!C%gGxH1M4D<bnstOu4Wfq7M<|uNCjEXZ>Bj+Me7i$$e?yHsKW38?2Kc}ME`Q!Vd_cESX5?|tazRqm$+NspQdDMV<3*_}bA7;(AWD5}7t>c4GhcKu0|hptq*;RKIN@aieP-O9Z{u#JYQU52ESu*t7kN`5BXX<d!iv<MG1rqBwcUb`#7jcJm`I{@Z)a|(XsMmA_dfcdMi@I0lXP6<PVm6z5|gCSC8a;rPBNax1l96c50C13wr4c3QYw3ImcQTo_rUmdaV3di=doo}+1h`6)=;c#D82O>nuTm{xrQ=Kb6Z!B5UIc`o{)h(62aN3venaa^@t=aj^9`#xECy%3qc$y)2iPWpCNzSd}#UG)xZ3#Xs%qwXX&2N+>rd|-$$6yNtb3XPZYGe_ddL_ejeto!0Q*jB_3DrKViCm2&Rn#r5OlPg^@i~a*EP#c*6)Qw3E_T8T2is%Eb^`p6GoFw+D)Tl&f%ni|;H(^Hls{y8LK7s~t1fl5;>umtfAdjVDm187kgu2>om&)k3l|X092=&HksrP27y-z09<GR{FRz4WhOaD{vxJ6#hkS1)b8D>knqCp3Wt`#8iEyxuhqI)H0W(fca&dgj&+1+rDU?7-pgm@VVxRVcKT2P0><_*9=p0WlwJ?+&k{+>1<C=CcN|lsfm7Op~{36IA2l|!<lWeMzW>aMDt<QCVsd3XJXpM)W`G%7BuP}pFnC1l5Y<L)PF}jyXkx7^}9;9PX6|=M=NL}JL18e3R%V@n>1K0Jd~dlsN1XN9C+|O^%y8Gv!b?Kb1;=*Da;L|lY`Eiw~wp#c$5&`9fJXWoUcF@x4Bm%C%@5y-BllfOtXHWuG&EQ*YdQEtf7@S%2y!@<f;y&nh(+J=be;#R6YfU-%}(~!_pklkJ0SGVc20SkIkKU-K|p8{L?SsiM*qD2ZP9X>r=~scwc)L%0xNN`W4u4042N@8e%YD9l8^G6oy?62xJ@5xsD`}u;*L!6Nn^IcLN^Bc4COcT~>z3a{al|L#`Q|Y_`Z2!sTtr7ML+gyB>l$tCedTzaed4nL&Mzj)b0Kb6~qH-`k3BHf)Y)3sIc=Y5A5LR@2KeK9KpiaVUcS_OE@|8fw~JAGvfka*d7L6T=ob$2DxR4qMkqS37J_YQp!H5kem?M5O(?320gp)n+lIIUKg=VCnA4P%(dz{Kp)sBZn%~p~5JB-~FFomy-1$QqRju*4xZ3aH__EUOYZ3V_nuqf2LvGSCZ^xxz;KcP?fCvQN~)|B5iO}1f`fYnR6R2QKR5Y%sP)^)=ESqYlwo<LXrj-Q602m3cVP2!@Fqdn2Vv_5UZwY?L>ggEq2nj_H%7(lPJ@s1)18u?n#<P<TuB*ltWG7C9<uX!Zl1kyRP8Wg+@XF&{i<P>sBrlfFNsX*^C<x)V=G*ld*qX-*`I7H&R)iiu5MOM6GrChxvnUNb#?h8Qn>(qFnDsBKd|Z2sfE7^ARa6``NT9NmKnM3BtndyZniA4*XWCNb6w+b_6mF7Z4Ma0prw8(y5~`dq;s^vPy!DwTDC+ML*ZI;1I3tifwu!$a50_gKbhCJd^TIAuW_BDp-!(N+dMbN!{X8LxU1T@RmbNQdc)gUD9=rq6$XB>8aq!1E?|58Jx(e-Ck)K=C@&OQVf>w2%#!McwIol^(TT=O)+Nuj9egzL7dWsT1+}mlGK7V!lQ?*Q&+Cz)@ivF7fj^ARh7KpYX@!cwZa#4q(lT+epc}&TA%$GRwf3MqXb8gOUV;v($=P=3#-x@)JRSIj!e;2tSVkh{_AEjd-x46wwPrxZ?9O)JzMrpET%-)BlMa@ygC_8Nvu<S-Hc{~nnNR_x#D+GCm|`tU0%#)F`=hmehbpL)O0ROlkK=9so!#0cXLD8VLNJ>g6K>q15b9J%useJk5PBCNtW}Cl2c?HKxJ2)WCcU1sU7r_4*p~o`?*<+Rk4&B!0XKROd)`zBa%jP49dgBnL!L}Kb1i&$G3_wpga$Q*b^NCvqv1(jP`d;!Su*$Sa7eVbGF~Gt8BmUQ7CY-dyn?+%YVo}TQeMm(P9L<nlYfPDokEmUWs7H#p@m|pHz@Qmn$1Kg}R_-1tw-^AVedz0EKoI$c~Cx(RMxTG@L9o)nlepv>wF;DMS1ZYiDfr73jt8DX1p7+Ejr-9o1Gd$GFj4VtX*XYXT*yp^aR*K1HyK@(EG~p;2>!W(H}uCc(_yB;rGtqv6cri;>pM>{=%_63%x?g(gYusOQ<mPf_L%*`!FN!cc$uQFV6yXH4_fe=JL9${3v2%D~h!R6M0Ou%<*5{Ak~$ty5-Vkep3@c5@LN{*o(-E{Cdip5{0k!y_8hhJW_eePYH1|8At0&Vel_Jc|BD)|2bHYUEj>&ic|r^e5swli-eBXCgR2H|}GcG<s|*8Z%H8W8%iFdo&RZ)9X3a2Aac$OwMT(1~N%j8;6B7l2n1<&uY$d%W;&ua-)*$T!nV<qmpl|`mu5NPu#!n^KT&uK+AQ&ATI<{g4bfwwWLo|ajVB?E6OCgF-U3&8qB((8+WnD#(6|t+<ve%CpJ!(|F2l+57C5Y2vT6zKIBI_ta!%F^bX5`E67&Ua-`HKq~^3Op3E9zG{tA6g0Y)30SOIG<ZZc~m11BjaG3@t;@)PP@bMI8R7&>2d*Dj=*#=sNLLIk>H9-p32jb6V<uN^(&V;e<!gpZt0e{UY5^E!=MvBsxuRF-Qu#b0mrTABJ@FVuuJ&lTwm6wMvb}4s=<AQ2x<&}+*1ZmHpU|bAqQ?|(!FWPXBb1*bx^Vi(-wXQKQ(r{v$vBDB$F*eAiH5~*7%@Fe|8rC_Lze><8rjMg|LE3jr@-;G)N@~cq8VndF56c@TVeJ<D=O(v`By8|iV_R#_3|XWA_yZRzGBAPWHPv;M6x~*fsn-6<CY}M?4apnLHD<Uyohns<t~gpilT|h=NnQ^>x3)9cGl`X&G3sRUPR{A8#T>tVc3O*nctE9cimU`egQ?RMnlhZtR+PB4RdAMt2}Bj7OfTrSt~oGuo@OFs+A0*&cJ(~bU{#|*jHZHS`-HqAU8=7-X=MTp0CB~KGPZx?or3*GTvvFn)pczt&nj=BhaSk5AHf_siTCBVHkfvZ_vN>iCj^@`i}w>=#6X*L9es>cgZ)S`6BdQKR-uu(4N22n%4@F59e07+ndZYba$vcOZK@oG6+5I_+f)H7Vhs5>*$-1U#7+RS>c-0bpcd2hNWZ$YcV;iV=6mr^J0?a3*=VH2LtM?nd6aJ(0GcF;5w<fm(1sg2#Z^=iF2?hEAdejbDH>I`Cd48{(%zr<n*MF~BW{ZuY>RC&bqN^al?PgEV8oqM^I7pR+_3V)ib_@qd_U!`Asa_uvZwjYNBL#4_MA24Mc7LCZ-Br#$sEe;I>i-v&pMK=JvBPv^>XI4r2>6aqzUi1eB`0*O^wR~o&m$mbWoZ&c~t?Dc0CDd@nVW&`f>TxePq9q&Bw9@l$jp3rUr@)lg<<>QAeqDa!(1!+O-1n(|PSEJBD4YEQ*f(N@L%I%pPi4CFXMyB5SEp><^UQ#GEb{?~?ZDXyPQg2J3&hQGy5ei*(xmVTNPNG{q<90HbO(MvPHlCbd|N9e2IFuo|`@BH)dxSx*5kKB)T$9TVyLY{P(b>&M`iDHhiJaE3V3F<vpG19cJK+Ht<rjD>cG6+^{U@TLqVQFY0ng0TlCsiV&|ilifD%d{?YJVDaY#DF<XigH-nRk7j-i@uMp#rdIU*opYDUVYL=O`W@rd)<cKKd(^0mKqoHXEU=M`d-+Ma{U|J+R9g{M%)yGU#{C7&z3CMagx02jJgRU$;+b?N`>UahJa?}wGcay@X*dy0-ru(UHFPRIpOe0a}J-nTa~~v(R1F7AyySCNgpUh=>PPz4}N}e6RbO6TlYT7ji;MO(>Cj6mYZPY^_4_7A1pl4hWW7-!=m03{npnBJLbB<o@(hlZ;l2hEcZT4tFA=Q^F%j~WTsB7ee(IrgJmLw1%`^WwiI`w|C=l}r@Lo6ole_{rj*%Fof-1IEO-dg>Y1KdF+-Cwr;QVeyG#>%uzsGeF6UcGv=X9<Sw7CXOayo|S(c~;OO`$oH0hG<W!U1&&e+pN3&TXGyxY*0WdjWy$`|}oFAz)p7<H5W0h^92OT4W?Q?v<+(&Mo_G*B^VmxiNsM<eC13*`IqmNf$wTkt?<p+A~&?rHYR^4&#5Jtc4$j>bd=Nz=8opThwLk??>GzUW9GIX3?dDAWe7ScFtJA+dkb-a;}DQvgJF+3jwe_Jy>8#$!W(bi+(TbL)cj3@(?)-*+$4d*1W+#NRU$Nj<YjTQ{a!Lv&N}h!Y5j`Njf@+=cEIv}0URoMElW&n7AvDLCsGq+pC0#YkDR;Yv_Nr{UI?f|b;iX#&lf&Zb_WB*TTXB_?}f&C#5Q0naHJS3L86%r_Y&Sq&n*N=LOvqI%${=f)cHB=g><e9)M%V3a}m>gq34@y;4Fx#^!3vfU`^oT{6X#Zeh7BZ`AVjXUH4SJ7pH$EuEU4K6I%Fh)8ii|uN_#b2h32`_kxgDjVn$R9VUDaR@AGbt`3n_dA!Q@mr}Qj=Lq=kwzl;n}xKu3Ij<+C28WBxdX5Fa5V}6a;+2PnkI>102vRw*AyYiOeFvH)%AvW?soWt}$n1>4~tMGx;ENKz3T^%s0>B(;Y1;T8K!_iRYFr8Q*r2c9(=740&Q8(_0jSx?blid^*d;h<b$?1*{3tgd##|0YFf@Z^I<)igpUFL?fYiKc*<*NTy331oRD&89`JLx!>^onXc0vPcr4#TP;NBgO2XQdhR~V@OS=0<L~?*a({fXiRn#ojH*rin6s(a#$qVH>(jS6G}7y46jm;Bn;d%KdJOy^A3cX+=JVQ=J3X}%v*JZ47AKCdrHZq%432>I;NH0Krh}*_woS5zW+l6;vTl<Sm?*g>?>o2Y08vnf7VJev0g%K3PGX$pIlrO3C<oxbEqEKz?UabV;Fc|HT$z}6Y+7k$Ul{y0DD5B(W^@DzP1muvW;{Uwn*+Y(R$no=eN_ogdnlDE50#^}YzxYt6N_?5u}S&U4TGZ`b@=Rmc-JgO%YO~__UO+;5<rYP)!^1x=V%Pz&Z(83k`_6jgeVoTmvabpopT2ZR3>NgLU^9g4Jy5vbiEbbtdtV<xS9b1&4@2pjoc|`!8Uf~>KYb{ry3l^eoLsfQGfQPh7}o~^%heYBf>06VLwmHZOH=+NS*<O68FqCEPx0kE-3Ty;LPl|;0wlu0@)Mbm;_ED0pOthzAsTjQ0&votHagc=mu+kG64xQn&mTw58Vo1(Yi_1@WU+rUw(0CO$YSAVmA@t?`%V9R`V1Yp2e!EM>a;4m8RV!Hiy|h;!$%%BpMmTMuo7b{j#*n=zx2Dp0ZwOifTe_!;uQTt6{4_j!X)gc@-D?Y5OQKoKT*qh?cpz3W+)Tp2iuGD6meElH!W++@1%s7m`lOp>Cu1;g00B+6&@(^6F7v-ShD#Q+>q)zvEo{wMTdLOItd4ey=<PJcs%alv(KPAza2KWtISXB}9bm;@u!PwmhW}F-ldA*#tny^0FO@j{>HFE3h-ogorOHF*ZW6=}~Bex(eCVh7hsRtk|rFxdzj<XMxm9;ed!nW=PqP-*;?yQp(6xz>cLSmG6ZA-76PHCmgFQb9(N}<Es1ifPlZLlFVx)7!iJzYuiohGZ=l!ECNe^?k#+>*o}TKvn@x~RT6i$6%w_q5R;mf8UDl-1s8@UY^AFJ!MC`5U|3q!ETg$EJ_9J0S<htDf(%c2VC(Yh7IU;#@bJvDQW-g9nNVvOB!O?lkb5jY3|*tbH`7GX_=?3QL;4nkMSO+g#63694P!pQzF9<5XwW*HfmImAN-X1TID=b)Wun#zD+P*fn5PcP>T#w3!5<XGAiZGGa!8hEMe3Z;|471$G6C0k__5i+hwJIU-_>dx{0O1s8E3%~9r65+!P?%t8@Pi*Fo-X*27kmJemUP4@7Cx!Q29JwvY)Lj@3MFjmh=_Ni5wKOD^{1LhZg20lyzBV-MVZ@Cazw(;>oR;W=Uf|W0p4#_<rXuF5TL|*hXRhI!>8h-x6g=4W}L>El8OW9i2<BqHP>SL-cP$>^m+OPCW86>lHMR4|SoUuVrRe;a4A>^>?vUndwm%(|XHClz!ck@LSggLA=WHW+*5>t@6lV(%h$J?Q=KknJ^2D1U0a?;Hv)!{u2{L3ELnOpiE*%zo#FNYHd{cC8Sd@SGG=R`JmGFz^w_X`$KK!U=5nt2fn3e)v<n^l#s;-m0(G1?qn3|Nmd3JvR7(_r}gY(_x0;k`8g;NwI>I^*(NwKNS^MZz@Lq)SQeh`o>r!OWZ>;6T}6vlHa%{?5g}31X&rIoELax<t5>$9caKKRglj7k-wR)bIe|ZeQyJYiOd`qYfn~W-xrPY{wpw7f{}<h#@xu?@!-MY*$l1n^VtPQg1lHpltRpNiCfArt5uF=%tv9&jmFiMN-2+8`iv&CNJveUZ(6JC`EK@c@<r(Tv@Yr*!Y1j!dRNz)IUd<+u)C#QV2Yzr{K6t=LWJ_h>6^u{^E6ipeCs}}j-?BPd`v4rKVAY#$K%qkrui_sHBB4y9@*$m(nGxZC8?E<rY&R*xfb89r=!|bjXwNYY@-Pp!-LT0fwg=1z^%r2y{>BFZQFn<V2JeQW-u0Fi>e3S+>TH!wuk>=d1ftfKg}6irY9@^z0a44oWre{}v}iS0sYC`!S!DeZCaN#RF8M-TwZf+ZC*2Y|-3mKR49Ofjy{g#h@CbGq-fg&@b?me=)bu=+(OpVqG~a+!M*7Roa>Z<t&fMwqm?kWI=_x}dqhL<8&yDonu$-EUc`}N(q;9JJH-lD}kE35rKXxb9xyUFd(WX?_8uPB~x6M3HW}#2p;qkW7Dj1lXQ=W`^8|87O*o@h-hSD8llhT+fLyZN{`)1ZzR*bc!$_O48g1>D`^rMK^WKdf5Gj?Soz_iLrg1250Aa|V=@R1l>Ur3Ct=CjFTtZp)zzapnn_o1fJpL@GZD?E#0e(BFA`t!w^>zN@(0w1U=ycK$O7chni#^1<IlGwuF3_R?aIrDG|8MP)Ahk#rq#tC+4jM&n~2@4>Xo@7w0^LNC>r<(JRa?y&LWgZy3dTu8v_)5Dds1IHt9uZ$&LWzzD>Xs)-tbuF|1>jm`X_8TcmTTMSUgX;|7HpLinm8H>r$M?W7%`fwJ!L5zIAw_8f*lm%FEfF&?j0&d86dUt`ugbA%BvWDNF*%mkegIfg8X@GGaF3UAvrcFRj+;zM|cffv^LWi|K5+wmIq8mzP{^q%Y@wZU5~Q~Zs>g1LynX^U8fu0Y}Z4Vv0v<Z*;<FZoJjG3UTPhha75bs>|Ix>RO;RrAMYMgE2Rpu(YC*Cw*A4|4%TBvf>?Ff&$hovKt(bv?qRkAuHy?b`H>#whfL=EOOt1OQ&A}ov8&E;dO%bpuH%6v|Av^@5)}tH^HHV8H}r#tHw0F?>K2!&eZXLR?7;gL;UZ%s)ZMybtrk!?l{VcJT#%N+YTadOuNYHw2Nrf~!B3&s_sW&rxLs71hHzhc%<U$qd_)^%0JNc;gx&OvcWYv=elM>1hWEx@a(sPHSKc;pMlrkb_;Sk!l^AJvW5or$L5i+bJ^GfWkO&nRM8dejKmM!=yt?Ph&yUWe(ry_ri663<i5?03Udwfb`bG!*SL}M9dV>t^IPlDJKvAohiEU&?{Sa6qhU2g+A>s{|y1j)t%^1Eh$tA>*Iv}`xF-LfS;nvsmWrIm{!^B?8RaZu$CpxU#!Nwh$pz2At!ECx;xnUcJV`c7S#uLxvmmh1Pe&f{$mcFYo)3cA^A*S1!t&;_3U$Pp)^;Va82lsW(dG`qu!eq-z!#$x4dd%#BW(>zLJ7_8h?iRcI5dmUT0bh5^G#HWJB|iPMhV;$d_;ofBx8*L5Zm@Q0!>Guj9yycZof^dTdbwpAMJ*ES1$T&q1z{#8BMg388{VSd*nC9bdf6lolWtfHwQL?RQxPLtZ+ERZE8_g^&z+;+Cr0%n=5LN5+bOZ(aOVasQid;ObBk+HE0hpFHutum1Qgpl!GE|mEiAy;bo4FubpY@|tgP@rPp{#NH$rGd_9wCkM7kLykjr4Q>`bIR4O-pM*sCbGtH6ZJP!4N{zV}UFKZrah<Q5xtMq%$&<2st*m1E`E%1|MrmpkA5G@JK}*}G+x@YZ0y%#xRg8UK)H5Ild&2)$#M3+OhSGTDmI)2hn4J=k;Y<OF(T6PlGxsje)NsKE>DUxf?T3}}P)%1)GXZm`&oY8e71fp?Y+0>v??MT<Lg6gISFqU*!OM<oFT;fdTswH06$mkVs}F}d%>ndE?eX)xx%ZavTnq8H)5Y#6Nd^7i3CHtf1+P;*evaM+pGnu8n*xMWR3l#ur36mthA9XOmVzit<WHiPxhD}y!aq#Tp=2*vPszAmKq#U@4cn=;tT-atCd^O_U`@Umgvrzqn+_9?2FD2=U(%RWWAyiK(;r%4HjF2XTu4U)O&R%{vC5z^*a>M-|=?o+f*BJ1gvoeY)alih7W{Gi0b#S7_(yl~05{fE<rZnZIZR#27JX8hr&7DjplYGIt^B@6?fdN$S)2R_We6{zdCmX`n`?HPHA_`&lMf6)C1d}~=<+Yd&|77u6-ILHETXuck><Q{HiPNUH>Xb~R4M4R_UJ0Df0K8h};Sbb($%}1iIQa0uxd^)(hA@q?JM<5C|a~?WhBEU~O3<hgI2#QJ^BFXlS#$r$K!$&KpX9N4pL??7kneP{rQU$e+6uA#-VeCkV;>bao!oG7|MST%`K<ftN1~LhPSP&LW#dw}!NZ78oWQhs#bx1PYR6qs3x3#iu?+CElnSO`b`!tV2thxh#@l{FkRY~$yBkuLj*Aadl;nxv<Rg!%BKf|kx<g1M2kG<64tA^yOhUBY;<WH7{B+@<KbQwusUr&=<r1NLek=Fzy!$Li>ib?K_=ttBhY)MF+h+(|-h-LnXR?o(ba8r@SCDt$5B`@+FQb(z61*0r7pqc)m*SCy?rkb;Hb1g@y9fqX_qmqy33Xrvs#oS*#0JVpu6l4hQEnYd1RdllhfDH+5e$6MhGryO`jWm~T#Mc|~^+q&eJF$X9(FK`YkvA%+xhmu0&tU4EcBz{x<~ge?+7<Tou4!a+k&~on6`Zt#y{kWY8THDeuR}4;C3Wxh%#*X@Z*i&9l(5^maxc@jR8>Z!I`F5%Zb!Q2R6f+MIp|8}BU4ZA%_f8}e(Bi2=-6xMlJKy;mT)HtDblY@zq?e0B_w1wO52UveHVopN6kZjCO%mO80`W^)x?WZidR(@Pvj!I>u-gp-nuM8IO+ka5%p0S!|PIzFT0W_KQ(SBi`R*wy&@**mQN=vZ=_E0<pIrNSWe!ZG$eyNRh5jBOyXQ*GR!0*-Rx7ryUVA#r0wahNPtcnp}uaQ(OQX5pQC^D49|Zzz3{WMD?d5x<o5kcbJ7;(a#+p>>cT6FOFHWWU-pKFD#WxbWBe%)PmcwRVgc^dAWZlhAkQ-f>OQe>N_YZT&<MwVV|_~KO4<<)0=8_niAF%ZM}#t7Syg=OI;>PTzeTB|nQHXpS7Yt8Yf&cZZO>s_e@imX4CG>`LJ#ZDlDd+XKpR-6%_!KlMw&=8Q4_jMW)ZyZL=x9jTHq#2`w#sLsTD<?BWEL78$BUuXhm^JTtBID%Ldo--9QYWAAOc^?!}135yek6CuGiHBgbk8+>VtEi>v}kb(kDgA54B^<T78#ig5v)5|iSg)#qHYPI{FWWBT)NgMB=n^59rab%(p2FtqcQG&(yHfH1zBa6)!7>uxz1!A&ADZsXJiR$E&JQrlQ-Ae+kv{K-x<BeH=K#R-K?KugHfR=!1l)I?hoC89U=l+S?JR9@J#w`L@!5l>y3G0}+ef%PftBd7jdOESZ*XH|2L&!2G3#0!<o4_d(d(+f}p*Fe6(1W7B*3-pM4phC!lSmtX4a?r&db$j8OfQV>1B2-2c1W$$aBi=uOT9SuCU<Q;l2V3p<($3?wk<Ay$5@ip>41_GbDd2%@xjOZ9dt+o|KT2)rz>_b7*W5WH4RYag0V+`HOu3Po8qNkR2m5*RgtIX%*IPF94CECg^dUy0Q)Kf6y{wpw$RHa1pi^=WU<h(nsY8{NT|`PKz~{l<fU8oHGkgjm7QWcljtzIYvF|E}t#*JA1<=k~Nmkl0Y_%e37(l}i_pZH%8g26UfSJ*)n%L>$|3mj5`26$6oFs0KmKLKelYKw+O+~S@b(q|KmCC*VOSQuo_e786fXaV!h$I(-6%`XVnYVCVvgBT6+8g6vY$mr??N5NcsENneKBD2{Ko`EF<PoUP-LAGXMfFEz>zLY>n?Cx^q$;cttE)XuACu&Qz|pBK3XM<H`l+2jiVpcY0X}{Zs7vIY6kv(!X!oKQA2}sp?GNF*#6J-o6QN+#iGl=VLZpp}NgZ*4EU4_GM)h4CXz~pYiV1>n;v}S%#yn6_!mAlIgXZbhdWkx~c`7GDdFxlqyqBQ%XWm(yvfR%4a?f`+^?V0TmXo$c6I~RLt*4MpZC<R5-j*?`&EHTssx*{hMx<$2txwt(X}~Wve`}dxVT{d-9Z&>2b$)}O)tbK>BGG}P+9ERT(%7v?(1H=lSo1e#**##C`qX*z_j=j<od`qqzT$HK!rSb(2U6{xKa;H&+U7E=3#rq#Y3#sf)8RErmm58h+NV+}U2Mx;*_I31hH=+jao3Fol4Yw(Y}r=c&Np84tjspvQ46!|)uHmaw9CCWE}NkCBaMr+xGV`!w_kI6y0D~i;bEz-6mWeIxm2+b;zd{EUgOWC)6_avu3;_qUr?iW9~M;fS6?A5uaK74V)g5vuOs|A!mlIz3Tb(Tw7f!EezJTs|B7mPMYX)5T3%5tzX?z+<7b}(Y~e5aC8Q-7$FNFlflnoiYZ`sGk?L;IS7tS2=zTaxuP{eCN3R6`QUJ>gH!=G+^`&ORhLG}&O`a2uqv99NfGUst8In7}t<2FMg0c7t=m`D<Jz?|8KocsDbDoShW#f?C8EVFm9RjnsI0v@yyCz^uAZ{XB@q7jYv0>Mkhb6paehbDU<mUITd$Btjkt~C#jBCAjeivbW7fxu7Q-ljEu)^jb=ZC9JA}^Xvl2dF8)9DxQWd?7lw?nwci1j#q?x%RAi*sYT@g>5gB6R9FM|1rA2y!t@lUJ+m1ab*;giAOBxy*~|7hx0&kV`m2xKwb*{P*YoJOzNH1#Bd|6mR0|#&iM0VlWM`8(cv>EY81#nF#Um2*Ty@OMT+qOE{NnAeRyMasKn<E$7`FzHtuRI0t38I0I!wH;20Lm>>@QIi%$p&gCL@BLw#@P?zzsPB@qF6p|&r80Rv+I6vUxw_N-7@vG;!FkQBW(ZEgV3{@1KdS!-r@iWDPh4g{pTnz1U26*`wtSWQk!)MRaQF(-w_of0O6Px5`m9j)pVa@HPF;Se6n78~Lw`?4Tz-`Pc^y*q4IjFQz%~c%|br-1$uGKY;qMIt{`Z{XnMSLk8(UHp&-02zD6+stEa%7tG(4y)q$tpb9Rn>3WJCO+7@!>!aZWF-y-WeTjxvN{Xr0;>R$bP160!By>>awU8yA8gj`B&ceNH?UheSD;|weE)(k2krYLmltNtFb@ZkaN79Z!;xCGUZ^$Ay4e{&mf^bR=SHsX)4GkwJdm|R2%@k@TgCMQjGdTEuTy_uFXkHrsa^|hyqE}1`$Fs<SO^+WA_99YphxmG*DcH!N(zmA=Al??h_KLtcVUBAg=3vI;7v$#eszX<sJvhM6AgrybgZdqWsupIHa2hamgX4fn*qZmgS-T)c8=jo2agtlj~Y{*!ylxDIjo&k<TK>fl6*)diUU?wrIjD!j~=h22N=16SYAGj5`a{A$%EKM?h8&AOr4{VniTy7(@>ORFW4p0(Hu&ri&apFPWAE%4;#T5Z49X?BXJ|VTc5MVWNPNVKBWT6yBkjMh*rNh8p@=hK+pMfMpD=y7+@wdt)@&tu96bSp?2eXxd?_ZRzS{cxow{AQG%sX9aQm`5kJ#irQfn4dA{fYnumVg0Lm9yM<4a7c~V1t*QIR8f!ypIbp;^wLDN|uDtLaFD4O^eg|qxmq(e6^rs8y%T?GV72M0W6LlT!JfV$0q#tNXUBJt^pAo5C3Zjt#9ZpU^^uBE{{m9(~FD{#qZ@7=-1Sp5EVU&J0xDA-}QL@$ZlCZ`t)pYhK--_zmC1pB$LiU_!27wv*5^qJ8u2E_=GWa0=>#`@1Ur)t)+a>sQUq@y4Z+>0mCS`iB&&W+cIEi)8W#62Tn~+>*L2d%&!I_ffRwVmzRI=Q~%C%}rtO`mivq>bgi8sl?OUx#f(7$o*2pE86UNW0V#1zmb7*&dR*)E>g@<B2nFq?G7Y{DQmSoobng^FBaHVI2+lUtp9qBRj|3!w$wi0|?C6}+QC_tJP`SUo3BC7a{!QZB_f<~V#^ZwBTnDdv*O<im2zrT_HpVZa_!asdP05Ewj%0dI)inj?YN6a#3bOkzl2QFwKgL^n)$U{ZdODRtuwZD)|+hMp5e+zy%uz%Ai;48L@=z=LP5d$S=yBCSdJ>LKE-RGIj-!yAt}uH4S46bHVm0rP#3<Ri&>M35=Udjdc$PEM6?I|&Rd-Z6oDvq5h{g>Ox0;TVMqri}OuOUy6j_f{w}gK&g%oipK*K(JZOL{v3htjNrN!qLDl?`q`kfpEj^|M3@VRa^rq?ddA{nN|hV(JC-lJKz!<Oh?o>?@gs5g0QBE6GW+u%1+!>9iiO8RG)*y)5+7Dlg*KaULvu<h9zq|D)ELH)x9VFT7n@MI-f+j19gEQ$vg;E0OG_)FcMX^u#yr^Sc$-0c?)LjlCZ&zuu4EODe=&95tIKZnx0&7A%?P-RV`c(Hz^KW0nyN9?U9Ox+_PE=Rivd*1?cPl_6MQOT4x_$NSjp_WphTG)n`#7SCL5L%pwomoHlEzkt`|NG$tSYs5AsuXc8MT)=AS#&ULRrG*foQ5iOY6As9uZ<<heSlKV>n$)~hgEeX4V34eG~EX90k;>6_*zo}uu<AgJ-l9^)31XEBxJS9se;bdl=zhPvi|GQ>ubNicFk~c0Td7GIeufHzI+kO?2yxV8%@iwOAO$X|VB(FB>;U$v1WEDM?<n3w4*E31pcwLe=KPt(4Q@iv&c>9F^EAP+p$^q$@mN#Evr$1AtFS9H8C8hKzP~VYERGkBJ%PVy^rA1B!>S6U{d{^GIJW_4a2ubwPDjmQC=Ou-q^{P?%L#4lL0z+ntQ?<ph>V2I_!CkP$`Knkw#R|a-?$wu4^`tDP<INnGEh?l=$&_FvGVa_-t+_on8-VSr{biR%yS^-^aH-kH<#Q9fa>>djYCgxrz_R(;^f@kW>mA8lqhHH|d_GzEiW6DWDzb&Iyx2QYVTwuoDp@(RBdgi88u#>ezNe>&vOGB3)-k8fSj$11J`;rY6qZsqca?>%Q)y0%xtLI<E%tn&4zF$r&ZAfr;IPGutel}pUxhm2xll*uzjL9E3@m;7SOeMkU7A^9!~77z<3I6is%#fGJ~6SFO2GIA$%#8>s$avsGTPib?m449#eCj4mF7RCor<@J1cFFy-(cWBEn|5@Yn98VuuCd|fho2{h*$pmJ%fsYKz9JiCYWw9xsGMW44>DIl#zpY%il$e-rU0+9Jm_1rX=~IA2c1pxX9!i#O7E_x+J5<*7?VtH9|LF;FQ8GT$@82HZH3T2YQA+@8Zy--7bSkoN`AA3n?*K2bG9On&mQodWV`qfD%K`!&(ZzaXONKnDerw==PwHr<|4@JsEtV)GaL^VW@?V)1|@%CnP^1fQ{Z0Flg9|$vy&20I{s|yLf=x+>kVz$`HeN+2weufl}y^r^*h=I@W0ME>Z}*eIC#AL%6ODx_%s=^`%MOw7#WUP8}H*J|dF=upqAG`fppQ(Bgoe?Q1QUXor+I@@Y4J<SS5av{ovI&Yh)vW*h@z52axmTca0Wh&Rpy;xdi4i-0(c0dd2ONzYw6)@V56AuP3J;M6vfJEBFMLSe+wRrrmeu#ePTPRir4In)*JEm$&xUC|9?#rg*M<`u5f_Eoh-r&PIC%tT_0w~;L4XmKo47$S{QR)yEN3XF7&@V7ZuIUP8BwXQLbdjHmY-5#r!N2cEFTW*gFArI58dY+I6lBwN{CR$S3n`9zt5PG7DM;_ardwAv@$0n&|3NdtSq?pL9H_xAN*@Th>1&Io+DM<s+9I2K8g~aE3mIplLWw}oy0%~UES0zU!n?*hq%RJ%o_>0)v6)$K9Yit)aq4CJ7R<T68#5%;=YFB-Dj_5!6EE(>fb<L+*SwRRR1X?QyJPZ)mcFo=m#pfV>d>*RC(_DZ%Ctow~p5`u4dK)SST}Z=RciZafm`Zf|QBmhaxVO9`9WfWAzP+l&UuHCYuElni*DHMjyZ&zZ*=VwL<=)uj+QBB%qU#~3jW1d5n6*;Rj#xNPian)AC>1+WgrL+`7W6<7CZjnw7O0L_1qJVD=Vb6fVi9SPL@S-*0u*ILtE84K;D}XH*{7LPg+fl&#PmKH0Hf@8<=|bS@Yby)9YgrLKRFV5!6fvmDB+ok-s7J6sfu0-ma-LADP9#53eNm<OwHhvzaH~FA|~`aIlZ=e>G>%+y}6iB6DQjGr%cim{52oS9{n$i{M%QQuxM_sW-F!&WPYxeURSmBrV6CwLc1!VH`X4NG3#L6o~S)iB^b5GnWEmJ_DEL+a_-zE{iv-_NnliaTq_@85oEABeSEs`*b&yzNZATW{aK~aCbbtvVE~sucEd3Ztm`ihK1z$tEKGbf0nvYB_r$;SmUi<qkpS^ugFtYCh)~J3TQ7h?nyUDSO^O*)!PpW{d<Z@4C=Z)HH@20PCpO3ux@?KB^G@s$;G&7j<H|MHbAVoTGZiGp4tW&6_t9@?Onc%zpf9u;rP3&a?fq@QYn?yOdd;R-IVQtB&?b6MkAE_GJsy6UM=iNDnADPu!?f8m<8_3#S6LI@X!W944zL5jBd6&fW)rGBpqBf@u5&v8iN68#HUI7f4XTHj)>86~VU(fzwsbAi_sY+YB5K>NzV(rbHkVkBrAVqz-7>r;PDC_=CL-jig#5;`g9n;Cn;>haYK}1L(A<Ge5icWw%4Wu1SUyM{>06UxJD6lt80rC%wnD0cr|L{r3dkVL*78BdxWnw6-@mJ7w+dOIRBRGfCaH3;>N^=GkJ7JN@DSpAk0y52S3ACQ;d_+G8qx6N)S)VIklmlS8Ov83HF}Y>CwG7os*2Ey;p@M$#eeYO(`U0{+#u_5!BN_1B3@y|XvB)49mkxutE?E(oC{Z2G5Tr(;*1re2Tq_N5!D!Ew|GTso-tR3TQO5_ov~t229>dR?3yJj27dZZ;jXTBHxgrv970mme6$>cM*yWzE5r<3;TvPcxC;h&xLh_|k^IODP*v7B7kMwbllQpDf3N$qe)vTK3637haut)(pnje{Kcq&}q`Y$H)QQ!7gc;G?!EB`+0S0v4kvL#56^-b~1NF+b1?7lT{sJuUR?@B3KEML77xhw^S`{k@d(jvLP1rME*xh(@UYwR|_=4fdgP~gJm^|QHIzZIY_m0!+x0-P-{NN^OLs7-D;lbOZvQ@aMEghfl-`D$fp+Aa^N2U#zR9^hz7Cw|vR7tr6U!}`PASEb5{GVSrM_xHcUfBd*|9l<c*Aadl;aAR)cla~B#m8T1M_y@1UTH^OX-8gZN8WMLzA}$|CCnquPoSO-a}^iJN4V8xk_Y6-g59Rlju_{N>E_tKN-{Fn&1om*kvUJtLV!ligeSBk-4)%OFw1=AnRL$W^04Mi7AK$akDOo6xpdB)uw%UtXPJLoA2ha+VR0j8Bpv=DJ;#z{B#@FeFzdcl&k2_$X(YjOe!)&fulOjvNOPH6<b+scaoO?YviV)4i4mducvzhY^H(mgrHsTPVJU@UeTSWBDJri)s4N(j=Vg4dBkxRzXCxzWoB*d9I+K7-5<9mHkvDpg4NHC5=taUzNk^sXNkeBzHR38^!AJlR{NiW4^2>sG#Q1tn=`%zh^N8F`z2EBxoRN3fccsgO9ph!3|8k9s<b)(*lxs<}4E_;Pl6c|T78i4!SY&+b+I5D<#dogryqpgB^6t#$T;nJ?IXJqD)Ejexk`oGyP_J-CkP&LP<Ru=H@LZM+cS#25Nv)jg&zGF|&l`t}Z=DdhoV<JS43}w2QuUquiT(}>Fr$*uNZRtO5j$fcnbVP6`B^o3P8mu5zqjFuZ(LeY^B`Yg@ZVnOikeDeo+1+5sv4*ksGSH^s?!>oY93)$DI*q@U@9TNU>8*~OS4WW^-*BN2(F^o7*NQS<sSeELGt5TEm79M-C?w?t3<FM)GE@fC5oM`dz9hFvRdW67+d;?Q);a%3h#E+S4tJNmWYQ&lN5WS`eo~guC2-s@QzTZQ~x50aSAn7LcIFg1!@kLc92l6$E&5!O%*ynR_N3<T5B_D9JKKwlM`&N<=ML)Ta#L-pi<OLEmZ6C<`dzkqPQo3NFe<gza{B*RKmxi`H)roKU}8&kUTJu5A2HFm)T92wQ-50ru^BKchmhIFw~)3+aZJp4D<I%JfMf>S4MEKM#mE#thj3$Lc4NxG=-Y6e=htKYQ8iLjVD?=kS_#NHAyNm=%**!28LvCM#SMs9^vUPWSPPsf{wT+x+mtK5^kVB#S%0Y-;S_M!eaqI5u4n)A;4o>yeKftwW|8x`+e|Q>cfDw_|V`+8$y|O2cK46gbHOG{t+j=D>A(#viH!(Z#gVwaDJ9B{0ziH$`3IQ{viRZw2ppDq7pT`xBt!Cn51iRBKt=z5#Y>z`-lNrU1-8QDbnv$q#toQX;!4~AQe*1-1%9NJ{kOTG$_T&TrSd=RhO!CMP3x?dutjp$;no8kiFk=m{sf53eKZaoXJ>3tK7!1T2Fvw25`y1&`C}0Z8*Lg2Koc{{Qm1Uo61oA-1C%a29ijePo)+6GyG*`nnubr*bpC4rm0{L$eXZxmx46O1ZjX8>?EL>IggTC3H~zxj;?;;QH>^DQlkk(Wf-#n8XCb^RMluWWm@0{BuLZKYTQv`#k1z0W(|saK4&igY=&A&`DI<6=^o&Xz5=$M(4@KH-BCI+{VsbH<-&g9Z8^CNdZT4<g_A4N@`R^3xmvQH8PYQw6<2taiYv@{xO(;()^3)Dq-S{k9rjXC8zp@^G=@mO1@@)Y062AVI&v4tKH>T`9zrg=%ncx5-GXe3^I|9?s(eJaDc?(qv-bCWWy1;7H%D}VVf5Rk4k68B9Yx>Ws#%V$7v=JMkZQE)q`^0ICTGR=k}{k-4W!?@OEhvF!&*1Z<~Dn_3wRq;4_mFS$&P&>sjr-7Wl(z>aBh_mybU(A+m%m!1yLhk6OPHZ2e&q;8;sYzIOK-%mbJ1Edk$vfz`*it_piO!gcMKh<_eeG{;COCP2yH;f_a%0nQ2;eoWKl!b5*Ts*ylEx5c+h@3$2K8SS5`6sR`K<!tCanRz_OK#s_Fx**1KC)qdoq{jfa)c{K;T<Nq{G_`^$l17gRkb-wUSu97&E6SVAlXV)0H*=Cd@ap5iG6K~<HX|7o^HFWG@oXJb#Idl@{Y$bq2js_Yq>%4-+T8duH+=gPwx;TP)jgetvq#`)8b|yG5G)w6$>Nr|^GVzW;#@hs0!2uwKSIkF(ZU%wWUEg^jh1(!U0^itrAfN-ABSj;3ON1Mq`HB$0{4(Z{4~rW2|AqUtsgnw*?z`Ga1xd#mFqCPyPR&Q$m-f!k%;oZWOiAOX5{fQxx1i*oIq{CfjcU*&SiJ1`uydGDOakyn%XjgQ1Wl`Cjpk)oR+5ejHR4xXktivrwyW|0BVnd42?8F*W6E5pkuufSY~RmmI+gm7bO2jeOfaulZMI<Yl2XV$zmDyk>~Rqh38I&Ettwb|-|X8%vMUU_RQf8B@|7ZZumkKOt(4%$7cZSb1hyg7W-6YLZ!t`c_EycyCUqKxN-5#%*9C41Vn0&Q)ms3DWs8O8!Y^V+Vkgs|dM7foor@pO$jsKzJDtePdW4s;iY^WwlucM=8ULEv&X^9^5uyZpnI!1u%ErCd;}I=cw}o@EqNBGV7i-h92QsU(z$wpL#%xnAqnOui;PJKl64nQ8F_BDST`K@8(h}u$$ThaqB@PQ|;+A_5Y(${uA7@i5o_NdXxOzOA=+Ji4IMMJ;`o=9k-bi_vQhH&jeoR^j?R2JTJS#+Tf>L;o{(*X7k-chRO3E#-f)PTY6k^o_GznHpw3t2|oe;%mA7c~>Up<`=$?H!Uh2nKaq5dgGp_|dy5NX9FMxl+@x_W|9NNi_!#;nNZ9!`8!eCDJ=t@$QYy!JCvA#P^P6<#3{9zbRp35?1s#KcD!-hx-CgLlK~0|vqSshuT#s15EPdoGQ}=O9$XvwZ`G;k+xMWke&>y>)xY!eidtJGF_FIo-UmIVDPs9r-H)fA4j`0~(5=I#<d(->H8zd|IDBs1G;zAkP50*j}U=H;89Dx@O2a-Qk2d$vxIhuhtoU%g1<;JtbwlZ=#oVD`)=YuPj4wiE!a1?)}Vn+_`k_-m@pV>*hHorUw!Om{a$@F2AxtceAkSx_jT8y7$$$FJ^1ST+&Rkc944y+US_|SvdCA8i>x-^@20HICg$VPfn36+331E(30ZM|927)UU6N0g&oZesG=?qE1<Q;9?nEPl&q!b+{0HvA~drHwelU4h#{P_Tj6nCWg;56GDwS|GFF;1T}A7bFjk@yrmIFYgFHVyp5~0^$}-K4&Ux*9P7AU@oUoVAFHUIp7L<eRcSb4zS49KqvNLlUwZ`NtSczYCC@=Bv5eMQ&PF=w&qO#u99Wfp(>xND(F7J+^CHD?XPBtyBzdYHEyAV^b@<H26+V5gCJZZ_I`_O%af7JcR=O4_3(b+NzWpHqC^1A5%hfy1SpFrhzGis1vD&@}S4Vdvo56o%-ISUe|MzKguaWFPKE$3kp3EIK2w@*ajr1BZcN}>}%NDkvrx&TxR2USe4+zDA;p`U(#phGEUyz1nwatJ+G7&b=djZy#UBMa0uAV!3|H|8R-Q0<ja@M3wvw|ssFFYaSakb^rql{BbEbie_>z*Nv0$u^vP$4XN}8&KZ;f{vA!qijVI{P>uQrY8~%s|0xfqv?t2N`eMC5G9SM=*TV8{9oqq{o*scy_#{8A6~BgImL-U_7vMMKsw{(tfydGMsj1TuTA%mu9PcSW^T4dVW<Txn(GrkZ^c^Au*gSP;wW?f90rA(`bI00woW9s93D7%cz0u~+9JhHel^z~8;~s*urcffn?<))7p)aSQFd^Dc43&6`MY{%u@R5qKnaRvk~*t`gtk&kMpwI%eemMN&2$H&2GAQ@kcwamF~HG4pU;9_Cw{z4t_bi-hAM~E7N-OTv8kn3wLh05<o~T^W+<U38pUBj&2RiiCD1if8{z=#QoY(>Do^Dptly(O!ZiL{AB0+Do8OgJq<<l=h;6Uw0;5Q)jWs`mPK3-+%6i2o7)54uf9UdG?5+NBI+4owcY#a9Rg{4-N>Z#Kl3M3%_dMYexqU`y?;@9E`X*30{B!Ql_~D1{;hxj8#dPZ*Vn-T1_>>QbK?YZ6E5kdyzVibq?O1h&i*YXtc+U<GcHZyF3BSsg0mafiddxfL<tVp0=B`*$fQZYPKVw=He2O~^56G1&b<G2<OgOM9+xvmzS6=_Fs_b|0lJpABc?@#R()>k8xRmK(S{l1b6kRT|A-Q|Qy#XQEy(Lf@<2J;+&aCB^Wh7DoeKtNgnEqpwYq=`R`k!_Gu^;{c_weA$C=Oq64e#LU=Lhfsa?Lxdqebh7X^Bci$9CpbGrx4NjYA~u4Kh~^?*m8PhAmdLu_^+DeRLL*(5F#^C)nsei0*T2`bk5<<!z6vr+c!-ir~R`|CdOexYBnWsRW3{kJH|_%*Zx4Nh2_Z%6W<rG3ua#MN4$KY~3vO|5OuejHm7~t@&c;c4E_mMeA=P_ZE6LfB(nAem2R}h)zssFca#YWQdEEoynh3^M)mdY9NPdbCE-Jq((O*LrSeBlqyXzOC=_$It|9oR2fj7plOO%IGTvBA&ILnaxk-I$3`;M%G6{b30$@_nkGdhXEaUg_}pSg{3hse{IRRFafcDQRQco7Oz~aH5q+Xfj1Pl6e=N-+dpcyd6PMhYD?c!O(1%?F^=2A3PbLm9RIO69u67BS&xhi!klG<KCyJWFeF<3BsQR`l3#YJcG4|?IDA9@E5!(_aCWHW8nUs`F=%@o?0GSR%7h7O*T0(@{%-vOJx>i|_@GYFMm^~!AHfx^;FYALEil-Lp#yH~=0jb^Ez}hX-Ns;R%^JiiLnha0wyJcK&afQW`ZWyF=q{)L9BDIMmD%vQ(U%O)Fp&a&iJ_sA-${?KY#75b_n2nNb7|Eic(P<kwnos>U_H|t5XjWR*(ph-O-XQxkn&uf9TpX#k2-}~VnC3YqMyC$yr?8bAIA||7E-+GWXI~^@^?@N-|JK*baJxYFQAf_tr{^Wfmkl<p6NcL{i8n9Pdogc?%557+!DsZgmD`rP+XBlMRC>gmM<F9yVr{MX7)7%gvF!#+gvEE(ELdqzmNsEJZ&{>hGxOkJymxs6w4M>$c0o*9+i24P<qY^KwWQ8s{RzD-5HJ7TR|&w3pxq`{nzx3Se)*t?NnMjXnv7{aUdg|jK@kY1e0wC@mcI_N5DQz!R;Dlt_Eby^_^D}P>XQu8v=b(V5{)C&LQhrV0W^p;&nhc3WzsR-ng#O0)5sI76bT59=vZTR!_w<iMh2af_?XvDMJn=8uOJ%`Y8k3CTkNIrcn2&8ku=C~%Of8tmB<y0xj&i!d+f(=fO<vxmFKdjeaG0AJ}*!E4X2NBjd9juo2wjZN5vx`ojdTJ`VQ`ZBD_KAOj4M2cdYErIn?eaI<p2*2@Y%S*kQ;tj<RH!nzzb~^2{SCn}NwJ#$h*O%y*W}?@8#+x;$?!I^~OW{DVgjX&8iAhggGP6dx1`+R83TpN%3>4hJk|376^0LEWfh*aFww)_12CH4wA2G*{vy3d>1$>Mwk=nbCY>br43X=@K)V_jIag48Ia`G&1r=@uMkk^8`Pdq$vp^VDqGp@5YbDIr0=g+E~K)5d3H>|71d3+0x}^4wy^6NaebiHL!R!8*Zy2RpRdC2Tq4kz)pL66HhjaDne6c<c1(>I`jfN%r}d@QZbz|40i%k&Qjq?2c)X_tW31}Txu;VMytP;h_+=l!5h$EnI)eXi!CjlX3a!iUByIRD2<*gJVn87Oe&xWYC{~CWyLK;o^(BQbI+6GjX*7&rIt+R=e^X9vbB*2F%icyL;VV!T(t^oFRQuu5^J|Y0w&ulqjCVLo*$~NhHz|0y-Hqi94~-Z-dcAlWMvl^3Z}xa0{Xf1Hhpnv=TJpe?Ojt=eJyb)CDz_sCOxFz_(>KDD5hLh>Z{50v?xxG;aDS)`5KX3<mMiW)0LUF{ywWx$H$4eFGXZXU|fyJEbabCP<H!NP`195O#en8Tz~)Dcw`@ey0#OKYk9U0SA4M>qR}q<V%0rCdR#qINWS*fXGzs5docQ0mMh1mV=gm<>~FySij*__m$J6t<*h33D<5--_;{U3E(gweuMUzMYC?>jSD85X5T+i=N$w?(MQ7@UsFqrQ)nx=F(3AOVgomKlrMm-QtoYi#vhub@jmwMq%g>ImX6E2pgoUi|quv&B!|&AM*1u(on;*Bi=J75!r;gx@jc!5B)WAY<Ek|~_`I9cUIB#+DesZ{A3*>XDRT4pVs~Q@}vVk#Pwz#dLZF%t-b+8YgO!<}f)11;w=(R_oYZ>+IEB$T6Le2WyI`+3Ubf6`S{BHeiEJDOf{cRVTQ`nhOfeMMpUf%=KiWava?5stF#r-F{+{i|KtGd$P`09lj7tcq1Z%n2vo>H03WnbdXAI`c|xIVPz%b`ec^`moKZ2qY{Bh{UPS>x^;x@HZ>;-MeK52V~<H6VM%zR^?}&%_T1VS=_nCPNK$Y4eCxo0JcB&Rh>ai62~0K4|C42Zjp9Ji1rxej}7Pc8Xdah}!U@fy7ah@HBbMy2QM9@&%5(6l+>)R2~cj8$Z3b`wzaizne;PgWS;z+|UfsJIu#?Wik>uZf<B7Q>ZhM*!5{9lIIDNv8Bk^+!JM@)Fxva8mbdhSN#!Bl!Of99HbqwX-Ip7?JO(GP!2$zsOI9_6P-|s@=~L|G+2+QP2R^mQK~ejr6($)rBGFxgFNFiH#98W(6Dqvo246iz0qnhRVOG?#iYB+xQ=WlJeT)6Tf6s`RPghpLWVkq2+kUHpVXv6cb-(>vtjc*2^z-K0z%vi*@f*B*#(nWP?w6I1=eu_)FHc&Io)_w+`mq;3u(l~!9yLJE=K6xEXM$EE{T86+iBSpMf_V$EevO=1-0sgBy}3=wOU_7--(&d>hwaJ5(Vg!r53`JTF|C!x7>~Zziv#N1>Kqmk1CLJLhBLLq&7v%D5zq5l2K^6YB#4jwP<a|Wht-)MSL5^q+;2HDP=xp6zt01XGY;ae@}&Z7MpH%mkRR<p`2G84PQZxcuROX^6^pgO+Ag2?v&!0wBDq344_gAuP}2B1r_Oq#O+jQXVM*5P`2l&+mLm7h5l@rBZ7$g^4PFfK3fcJCZ7_Qg$OU4mIN0T3iGt)+)t8tgji4|#uI!$<=GFgB_o*|CF#7;T@tK^Pqtx)v;n8T;MuANl`Gl_?k=xZa68lyIFXFWO;KdfjSqw#DH;lkl$=z3Q)S%Rpwi7|DVNq{M?%Mh7vSDF2D|_5gJhjvtlrGsy19f2@D+l@&WXozPtwMSvxbShL<SJljmqC7gH(|LZOub*;`*8ZS}MhPYnV6{a2~gQOF|i_vt1$s!ZVNo+0e(<I!24;Ez!Efb(&0Ex}p)66jq($I{WxcQ0F%Q(fPY=<`z%=v$v(R7=xu7MoR0`NH(Z*vN<INSpWidRgEiE9WIessF^t_^3kS0a)VT25EJKux#e7|_%`WViOhm<Bqp+LT9wDR(LCzJY5^=~+Pl701_uDhma>>|-&(R~vKE?J*WW-sY{+Jy%j7zGgpsHQrr41!<na67)6hy#_#KCKhxs}SDg|<lAm|!NLV_`cVsz0vT!$7QOrzh_yyxg5B>-a~!VvmjAY!4P*HU#ap)W09EGcVtr+zyvE!F1s=H(SzyuArWJaf}qFVDho6l9xCzvC+y>_@0s1oqS<ew3P}ZM?)bCytxJ8u%+I%QVu293$?)U^gXN2HG^t7+Es$t*Oy4<DBY62c%`r#Zt#LV@C*7U1mb}4aYKsJGi7k=JuHsENl>G(@k+Y*a;m`Lk3X&r`(T83FXRW_VOx<z_iSwOp42pTkd|W<d#E~Th0v8uE{M+^ECYCkX!yk@28P?mWnl0;*T5Em|4mN)mW-|*fPV{aPvhqb_mvO5d~^%Eg`2=?CLxfd&fLaIql#4>hrJ{4Tp8T*Cgzi^h%KwLYE|GGYVr9HepP^dP|03YXq4F64p()*gPD{wShc6pK8xm!(k7tTtmxlVb!sw4D9Itk^!aomRM<N0<!rDbMMq<-qngqsC~lTUCqGe8L!Z-B?Rd0wuHrqpG|BlqbUg%?-!F%Ceeuwt#AYw9c)-LggpU!?dr#km+%k1_qxqH7z>BO-i5l&2jV3ZEm1-q9@DeGKQ$9ilxyy|eE-YKoKEH2Zq7KJJ|m&i5kXeYXH-t?C<^SV3fw@I>JVYcDpgu1Ga|-o(|7E27j`hD;_qzPx!efM7hNSU3QYw9HJ#PZ^bgM?S9&$CcH9a^bV+@-k5fFU04j2)XcFtJs{~q^pvkgeSQ^BM6eW-j2i_a)Qcw&Kh>ybrK@)^GRSjhl`PnoPF;#9Qj01CuPHYUK?{UW6RK+8$MP9nvJc&}4k*8v(GZKZ$ge3z?*?Hjg43^>yS%rEzL8g3dNyQSRY+NH}7=!4J8GO6lpEp`3W}9C|>!j)UW=89@!Dl10Wun0@p%hpP>sDe|P(sxk08iQICMktmmLMeC;0;Quj(?o3p~K3}h4nUd5DNC`7)cnMwIkhAVwE8KI>5w#b?ovh-w0W1G@;NglaA%!IX7}pC%IA-s{kU+awNu{mAO{^%i^?1BCylUo!FTy;VgpcsNA<o874X6E3MOvvI*Nmj<a))XVcelapVfk3$5TrN<Pm|5^8@nkFhMV0G&Z)XwS8Xy{2c9F&o!Hs^p*HSFe)+EU~hmcpz<0=$@o#JU7?t%Dmvw{`9T#?Ax*00A2QPmG~mLhh{8~5%)sJ{v-GfT>nXwZ7MJ5Y|1NPnjCpUUY?(~<t@|N8Rc*Iev2IAYDB$TvwQd)WDhW2a5&oVB^unpX4)7jQzXq?c+*iB+=p)uR5C{+1I~8K(iTX+5L;Fj;($Cyo3UeKEw7wuVF0%tj`SroAp|A)_5(buMtU(3+>Bo^wozlK@uB~v57K<up|j{+``34m_OG|6!J@J(%R=Y1{&jFQEnC=|34Rk|w9qpOtTcIhP5q)~hP3l%NW1(<<I}~Sb@sf?>zgYVEEXjDO&XP^XGl8&c!<)<i}t4%MvCV7#p?Otmg!>9lZ;;45x>R%8j=%@Dt!?tdJvmaOuankFTDH0p$QIKVu#iKiy{5CE|zCI&>bGsdc-p0I{0;qLGCgdVmBo?PjSd;AZ|`3qs+~pnrP=S0cAeQdM<&$7kl5V6A^ex63@jB4&<^a_w+p<O$>&TNME)X_$c>8B_fdMg#qn{>|zYzOAva&$!kqHA;R(pKax;3GKhRcIVgn_eQjIdnb@#oYSe-3sOXp<Fu_?xiR7W9e+jRyn48YiD2STNI(3oWWS~S?e~FARhS;Y#2Phz5taG?{GxAI<0tAgkwgst(n)@Z|63FS{4r~u?l>SRbo6j@~99&ij*{sD4VOOpYDU9%GwiH@oCqVhomz>!wxf%wwVTuH#Gt}t$4qi-ZX(!uFdE%+b>NiCV>&sQxC6nr2sfd-pH26arW~*`{q3M2xXf+l+(5cbn^h1ySo=?1$pnQ;t$5wS8y|@<3_mzA3+2A&WKYz)sv#IElTUZV7@gAjU#9a*TUGErngM{RUKg%^BDHsv37}+oB5X!B6X}KQ8))vn2yS|S2=x={rv3q%5{h1NxL@jf_%f2}Qtc2M3W$X?{$r`(J1Gd<myPL)C*~(W2ouW;gVt3F}J7uY_0#@kC0l7HhrcfWWz<q2#qic-PUoq>sGSI+W<q5N5DO!<$+C-~tBvnI2f#G=&A7?@QioN_x%!)jyidj+au`-5%kB^B0<HhMJH5D@oX3z=T@$+b&0c77^u;#08Y$*S!e~KJfCVoJACN<bCXy}JxBYY~alqp$W`N-tAEVOiWGO`wpD&El!FzLl$prZ&_BYpbn#3#jumeLnJCxd$te+YG9B)wV$=8GGtGk5t$0JjDe0XD(n;aB2ZT3DtHqftS?9u0c<BGF=!SUr^nnr0?A*0bgMDSfGaN*N~@w#t4{UtB{LvY^Hgx*}l~PAD8Uzkl{Y3n5LXjv=IgAiNQaL*vA&W%_<qt5CIi!2`pnHdVv3Fvgf+{@EH4``PcQ{?3Jx8w>3#Yq5oMVZ7%0b*G2vE5hP7C%}+7d-cV}O{~agADn(xFdLB?HS}^`<SwTN^QSO!Rq-#5eYH@C2s6rPL2%-9g*HA*eX1}@%<(bpeSGlo`@c5r0iVBP4b8<}1<rPCz?>&+8+kkN)N=>9ZA@!SEvZHHSfrIXcMg-qk^;uCvhHK5<^&>T+4rmx%M2HbEOtkj<V4G9%OyuCfWjY(6$~atiI&MM&6MOOAS?<!5SW-4JG0{bz_(VFE!zY6%IzV5nu5=^7<*zKS%E#`w71s&g@J-K-z-vT02QtX38ejxwTIj<d&vEd-lB)RWofoNLuJ-{q)FZKDm>c{f;FB=TqtALBZE*@AdGAw;d_zVU+@Y^(uSaQO{(c6@I(-VDTqH=tsg-2@F$%)e0-?&vW7b<3GFa!a0`M7o_4gGtySEp+SKvkB%>GU7{AL9XQj*#w*<vkI)6*bnZY(|QmPNQ0A?Q|>#TU}8+x7PxUBS6U;{&ThdmEV#DpKogiPjips+fHd~AScV3(4m{M2!m!2`fFFZuG?9r~8mM&QF>{I9*II?B=)y8s@3OJ9tR*jRvlxi5z5YgwPsB8PzGGwWm_27t(6ZKqN6*nwUcneSuvv(jt1!o)hejKa*l>gE+!as-I=p~^3qer)t&gHWxNA=a2ibWD#-wN^FD$W`#FFO@hax3$npZ)@E?zftX*f@FsV-&@fHKfk|XmYYKoC6i`7T-E=uRw^p0P3*v@Z5713tmGff@$A-zxYzcvXsa;F)m-@sSL|1$@d9F<EtWHM+tge^xDhe$1T88@@0u{D03I_v_C>v)!P%Ze{+nmXo**Cs{t)>@NXD+ysWD3gt1~#8q1xHll_(jqfV9VO7iT2Ddne#`IAd2|z}Z?*OgG^hz;f~X+>iWF_Nh@0qAbxPy#Iromksrr2j>TDVsDbN6Rt595+pg%CVBL2F;WNYTqV+pN0yYxNVuj;x2Cl!u1_AqM`f5neNiR?yIO<I8u{pbKsoO-67qupnW9UWBPo0f7*q5-ronyY!gmG&(5PhCb2kz3(#DC<0B<4p&s|b|k$s|fo5aFqFUBO=T0}e>B&ppth2k6m&IU4PCcP8wczLUro6cY{AiI}{Ux7|asHKbmup9aeM-}FO!;C^%USB+~l=?_3B`oX}KB3ku#g;8_%~gOKqbj4lGqPRpE1ytLzIv7I$0kbER2lV75}es|n|gt@CQlIyyPFvDN(hNHT+Xm74`IcyzO9{-d_-bMp7p;iNDMY2>dh>-_lVBdD-3w9dj$9}X9d;DB;-am08bWzp4Hdl3+9$yV7bv>b-(WOZ$)q2Kwr&6Y?;}o4Ks~Bnm8Jx!vITriJ0Mbtkng;|Dl577%^8cKl+B9@cA$Zdqr2MN2y-}MWx~ku*w-KH70OvtrMeiVtuu(EC^&@vcf5r)*flGav}GDwF`Kt#s9YhzK;n4dY@5~r!lYIYb@_ox7r7i1_^_X5&D)RGe^tC0iIvSrXzghI|I6bU=|0gEl_29$|;q1E3@@SWo&Or;O)XM@!_rxl?SIGpB%^zo$@c==5~N_?kq?~Db^dqO!L=2l#mwEv~MA#RR*B3R^-Y9qq2I{(gI#eRW00PM>d$2uXn3QwX|lNrzrH}shpO4!60YuvYZwRgCSURMNfceo{MS)lCW2ydR9SZ1YcE@WVh7SqV(PsX)UxLFt;|UYjv}ZFK7Mi4eD;wCfQ$C*V=tp;M{-o7QrHJu?3j`48k&GL`hrqOoaNZvTi)HVeon^WJD{5Bx?xoZ`hjOL2z}QK(}lmqvq7gN#TKBH*>4ZBe8O){02*V>Na7WcEub>3xi57a{Bg^RF=8XeAGqyB;h3yfpITr>DzCEViQ*{o`7d~WGvp-3R;W|4S7eAEd!|rmx7{L5s0aQPFyw-tqKf4;9PbBT2Z<ZH^P2J^pAC{({Q3Csd`YFL1i*2C}IN|!hst#FW92V4sdBl$f}aRG5ozBe=M&OJ{PdO%~YPX&S%AZp|+$nwL+WOk`m8bQfPVxHGJ@ioi?KwqWv<-_*(MXOOo-&$Z)Syqx6?*wtcPHuB-R%Yt44O>__Qyb>Po<#(Q<>I~AvXJg8C9@4eb~_wfuRR_4ohefmC@R#{HPnTKz@Wq!0P?oo&WVUC@2omc8Ji;aZsUy+E;b#ynyvJG&Fb?}P0gVYI39v(Wk9x&bZfLjQ01*WH}TmyK@C&h0Yf~0{E_BTQm;i^SMtKW;EyesZT`64o44IL@n)Cy6%n{bAKlPOsLbEl~x=0y1On6n20^BNjH;G_~D{!E3!I>bat1Un#=iO}zjo&yflZ+u-X>MJjX?u#wz+va8c>1g|0HmCP3EkaGOR4y{a=ga1F1z}@~X;$k?2*1#ueyus(kxdx6oww~zA03(a9L<5V{&b;r#f0rek{y-1idVbTpJ-7(yn`0#hb{L-Q-MiaV#U60<-fMF_|O5_J|*}!C=-QMj?H=R1@M*g>2|wu{*KCjj8K>2f2RBwIh&HP-!?iq70#Qyl>H-N;=q*Zjvp_3Z#iZm`$yX3wl<+}YKbAT2{)#5@jqM%X#8bmD2RGd|8F3@P_JI)^1(IrsFaJ3GiJt6d(w#^_G1ffTF}S|oqU<G5!?j)qE#hrB#N?p=|KFck%RO`1rVR31z20u%Z;prrB;CMmWqIDs77d}=l3(y|HO;yZ>?)C%N)_8@ynjU26c_8{&r%5=|{u^8kem2mf_Y<#W!{X>^jX*0i0qoNm|59O6$*gY5W{tv0_VsXI2HRe@gK?>E>aM)Z&})NBFa*OT&o#mIOI{c~#zyw43FizA;=xsGSXEt*z=#Ek=8F_++UbF*nDa{IFB629kPME;fm3=EYE`2cvQJM&nG0%=0Roe>*CTv~%Gts5J6|N8_BFvy11nW6X(-U7`Lmea5IzMNvCyQ_$87wbatgm^s6;vOFS*(+Pb>RDo+`<~-%gXqTLviIiozw%G~T&{Q7IooI*Xnj2F_u(Xsw^@c(|Bg@DH`@~AKF;Q_gK;8Mta+xU^+aPpnc}~CC%=j{@YF1KQ>}=MHN241HK-uUwg*q6?GP=q;8kpI;yeapiXzpY^<BWup*)f=~p;BfDJCWZr3Fm*^Ix9MmP9YhGr2TU8`s<%>_vh<)e%*h*j_~UUzmD+hpRXhQHh+e%=FjjJA8%grZu7NV_PhT1o?M96iTWPLw)yJ5tNBSD+wkJgrbqvL(Pw{h1~&M2`ZIh*e>Ttl6T+q@&|-hiuPPWU#QyXz_;c~Qf7b7&g)J3aHvc^1=f#7^7hiNL_3>T!sa9{vjOZ8d>+8vWF%gpbyY?mxwSK9+<fs2!m?d?yez^xWB1^yo1YY<(_cW1cMdszI>4DvFwQ(e<w~{T9IBjdK53Y9JS1g*hJ_a`SIk7+rw5xxVK+y5?Pw8KnFl|0oS=+FyN5=X^P1Pz`e(?O9^Iyhe#4`}X2u8P0NiE%yShKTD|DqSK<#;cPFCAuArT(Fn4O;ZI)6?U2h@?o?)KU+K*89EqeSF0-Sbp)1<(Zyeq5c7kCU(*2rt!acQ$pSgG0pF?>+A@?j_%~zY$WHG&9?fJSEf@fpPiKAMLTiw;DSGWh!<X&Kj`U;q7`eB(s_RTr%pd6zg@+^n@uowRQ5XP%=2F?dl;?dY<x?<&wqO1X=25v^Y{5rEWP@=ad=!htlr(}>-O&1r-Hxy=Oe$=AwByFKYRD=22&J0!RhPvsd#!}F1i=o*X-T5x$;N9BE)eypWf{GGxeA5{rsU<z30;xPex2Hj=zt8%I5GD5~tL6eV7LG<Wm=3@isW~`MH>={?X^Pe7D|sxb~5Y)Bfa3FTOaxl5k~sFVDATdCPI}XQ-Eb^2+>oZA{5F)=NLt>Ni$M7K!se?Ea!}{!swQ9v(n7-29Szpj@s00jasl>v$!!53>3sRlfBfLrlSakMsb3Nb5DFc5YLX?cn|aHOx0)8gs_)Ls7LA)OK9n6D8nKwWjz300D74QZ4&nPDM=uom`&1TY^mc`qR&T4>E!HIY0&?v5O}8%10hdR!tRV>!EF)@v}esIeRxu7;euyVU?bQTKGw54XS~p#=?HM<<G&1<Hrc4SH4m~0Rrf6|L$*M@Z3crOtoU2@HtoT+;vegS3#1GNQ=$Eb2BCRg{T<uPGT!R0ndet;JE<LvKfi((qn8VL$El(|E3ldOCP^w{TY<#yu6o6MCOG)<hhhXbEyQaf-3NhTRLX;KTTe#0iV^P8C0mj`lKRF@FOeIHT3Y&%<Q}z9V&$rqz*BUM@>amzelaeN}#XObYN*Z&Pvmy(j>7$GD*fX{*>30tw6o5!D&#9+S$%$Q4H4#=_Fu_n;C?ibDSTHR?4>a`Y>zqwjhr6U{(I*Lqe!@VsV>l*Zg3!EY~l7MvZXLvS1NAHdWIh5ekuXKW*4*iHHItSc`d@aRAt`=c%lHDlC~y0HQY*-La<a)HYG|z7_>-%1pe+_4Mmy56HJ{-1wM05l1{IEU2x3BBuWEAUtXd<~eP7S&}6UP>f}}C2vDax9nvhXatj1A0Y*IAcHAJXOGp^iCil=g|LyWd>~+CbJ2qXjzu#9z0rHN458;s(tA$A0BkVUN2(AtyKQ<`sqZ*nJ|}z}mt_rq;pe@{r}Ui(AS;C;TC?xbc^q1-{>Ucro(b&YRD8-Qj>~{THrDjV<U}vq&Wfg5uzm&ZD}^#VxarXoAF86u-rMUql@N{Sj6zFTCw^oGkalMCSWIQ5k^Pn6uR4Z!X8imo-JkT$cYMBsVH%ELo&<YfNN<$v`&p6<0@LQ2f$ug>;?wEDTKdwC6Cs#h9x!}cva@7%=G_qg%cVQG^f}xR5V<uZ2ppi4=<dqZ-=p8DI26sE{pg;YgKQru7R~eBkAv)E;O348byKcngY&cFBygPAzIU{St4ucsXMpA-X+ScK3(a(3qkQon2CBoOZ=P&`sf7_up)#42!Ttjm#3?_)pC(RuKNqJ&V@?^Yhd=?#qpPBTF^&3^_c{!k9|25!*pD8ZVa2FVNetvMNC&5xDS(&bd-`fy0m6>z7ls2BOpVfyTHgCRJ}W&j0NB#OoANlml%FM@4BgC~DO|!kXxKHNC%mVC88(ZLVE}Opw-)X->;*sEd%B)}7{O3-ZQnSVrj?Y$j{v%1+P%SyJaQIdJG<d*jx|~IhOIFF>xb$Q119^W4PxB4xl2#oVg1-0)~SILz9aF0Ub(2QN)bP+K`bxSD;M2ibQU-_W({JMP?ZQU9vRI4Zzkz*c8773A?p6I?yzRr9oDmBF+H<83>fsc$6N2d8KNL%D1PB9Qm#Pf0?qu4EIG+3i!(TCnmT+zak(9_sCfPh6$?<)vDuQoU^Y3f7}iS_3sR;wkplIze%?g=!?+@~5~*H#QX^wCo3s^3r3W#~7<x2qXeY$v+Q(@6gp{p#pfPGrs9Rz>@X?_KJT?*q`91G@XfLUQJUz4&p5@STTz6BLSjW|gt0{?EC1FudqnoiwV`!-?B?2mdef>DJ?33<6KUgjzt8b4=E9JO2Dy?K9B@grrn5q~@S1f!t+|!y4PhJDO{+%CU?!NN?C*I-{bJuP85VjncNb1@$oP*8X3llfJ!K@{YnzQzZL4`+pz<iCj)&^yhb&KKb(rmJR;r^XR`$VtoM#tw0EX0#;i|p5ap74+hyXf_YN{O-B&192FJTxla`a$BXw(&?~L0b;Hr<8>=E#*d(Q1nhVnpc~Ny8}$jpiSqF!e+3wQCwq}3S&Z|ahWYhD+WL-3qWZtf=Uf&v1pe)4p6~an}}8!!8`Vh1QI{AgBas#_ka1)y#dfe1)z%tDlP%&@jv?@<U#A~;|s}y8n~;c<UxHUa@5|}B<a}ETM)0AxHVQ&-zV8?jnT|pSREr3(quI~E>)v*^fi>13{;p%@+YPi`FCO<@>TctB2CMprz>LhW$w|E<ng_4S6Gj2<wU}HIwsUm);wis4D4e=a&1N!1R4c$Rg_=$GZ&)VY2RZWB_;;;;M;@&?haD}h_}>UjK2f)`*I0?0r6IIgUe};V1>XG5JzGHk7`>c$U#k(Oc+J7^fRFCHmI^=7(T-K9FiM$f&EdjdtkqXG^y0l<kThtllHBI>DH7eb^yUiBMI_MW`2R#BbM2Nu2*f81DL>&%Ej++*~)o7R}>2ll`_q-39U)ZlDV|9!d!5}OZ5}E0~|R-<|M&tiH5!h`cr!hn3OI-7F-V7VDl*(I=N4nh9E)4N-~+wKJ{dh?Zhe$b~ej{=W7eBy6KXd4pToGSWGClu7b|CQU*4Yp!ULL4<{~rj|@@v(k_@tkeb@FY=ZMH<xF)>OR^!!s!R@5Q&~P3)L!YToG2DXXT2SWhFYeOB{H>2i!@p@rO{&Ah_5AtSp!;A>t9_JNf2nkm`O%;)S3YsCYkym=B-3dL|+vsgOY(&kU{O!fmMvw$WCOak-i#6-AZ!6Et=HA*n43EGE1YGqLMLglCD6;%TJ1^rka{tiWXX?0~ta+J3C>hvaQkRBz@%}>rWyFP6oS8HMP+y4HdaDOY6CsOk0p}zfT?2^v}CL;a7@kzwq6g3r@sPmdg#QAe|m*SrdmiFipc27e@sXpLZab*mo``u->$Y5W(+O{!tH*Y$O5aIb^azb|E(?JPeHZ%BNI>=!(x65^1V=Dx4t>OvEA$%v4iH;`TO_kH?`ery~1x*>@5?*me>XMC;r>g`u4M|7Y(_Vr|>j^PoA3IcBluD)(A@?|a^P_mzG&&o3{rqx4P(i3UA7bWlXmFiNZ-D^`LCNx;ali4n#fJJ_;2jz9#0f}n+j6cB}Iph(cA2*D!4hz2x>6wzaR-}jGMtYYtd?mhRMXL-MOwC^hBnrp5x$N0xzeE;_ixE@I6bs(WwQzR5U=y_RfaFPacmHBU#%~oDDc_}p6st<WF=`GTXp_3OK-0bp3aMDz~hJ;@4x(A^$)Z1Oy{1?@8EVz@L%D%|eMp!(XXW8Ru(4oGG+RU*v`D7%hd4+GYWj-0J_{4%+v^ewb-3ugA@-=yEHeSU^@UM7d=kV-|tqO6g7>K2&jBnpNGOV$MiX^(0^>%UkE7BJNl;{}QZ!xKnB9-EbB(EPuSVk2UVUMgyYj%t)M6WUvsK8qKu$--wL!HiFO|QE+S{C_uVyRplP%guXp_ff+v)9LecJlKpA3yF)!{z+?y^(&|@xlJOQSIe?9GJ9(iosv`IC@C^q=%&KW{Q-GB+@Lev;|+wOcIH^62)iQiSD&9tdXn>t*4_NQZ)bXQWB}TEr}#B?K&cMk{*&YYSffJ?B+aPszgwP<1VPDJKTddMq)_D0l1<(LY%TZZae8ASz71FMq{O!{_h`Qr`>T&pWmgBH={G2MWb3%_+_*CQbNt57MSby+<_0}u14nz6>2GkkxKP8?V?jMm9-|9>MPECDwASCz8H)q`vuI4q6b`3vJa}KmGZM~vsMamjAEUXd6HzTS%fa?Y6uWIv2~LqnuVKg=JR9EZ%k&R;l_TJIaD<CBgf7Dt3Prn1E#B|WC2~pRudNbhMZHJ;9kgq(XynHGN`#TD_KDHgfU;x%<~1DLg6f5pzVyGq8F=41ghYg!DFar`2t^p4p*`U-IOm#B0TO$!_^>PV3TDvC2|5JQY=|u5}m#%<(4!7O6*4Kn(jWNxyif3!q!Lzt6SQdIwW^PrO|`qa-q@~>~|~;4Op^hW!U_`FfmS|Z7yC-5Kya;3%0X5a<MNsXs-QG)t4rQ-293`>bht@)N{G=rIjgc;ZGQvdTD49Rgg)94z#IF=b03r`Vp*=olaI@Dk04*OQ2<;)1-vLj1P*}SFaSfo%2CmlPDLv*r!Id{0-BB6Q}EYX~8*6(uEe>z?!u@bCEcMBr>$gU`di&2`i>y6InqusCSrv!ZP&YnD$@-6<-88{87@v@JMeQOPwr}te{oY<?u%66k@Sfd13Pw_LXFwS5B^Q$R<xDhYd8mh~EojBPVZ_C7ztQ)b%LL5CCHl-MYPEZ{bIQdLA-fm8rCi$o)_r`0)Xg#=2yNiVP(^Qy~U0uvr{K4LW>h(^8^yMR5+F?og?d%4jTKnrCBApDM42mOK#vW)Wa+<lXtp{*(6za8B|TAl@xqNCyx_%)wY67V?pKDJQ8$*5nI`C9y%%P>V6y<RfWBBFOrj;*QF;iH?GFv1mIEwN%h6VH+9vOu>ced5XP~V}lB4Soq|DR9<#4`FABwFnaGI_s!eLHcTN;n8FA1_M2H8#8^PLcZyS_=jcmx<1eBEtbbo32q`}@N!?TY33F!_am4v!Wz6TN9fctCTfHF6USpmF(5Q?gro>jHZEP#f2#QPQZ(LDtg+X8T(U1T1%`9dchh~}-l;R4_j@mD^+zr<rl)NO=F|Yc!)ize!9cn5~gwN7QPP5R!iDNSFGWSd+W)}bi&D?C$4)+pb1C-^<vp1ZGM$J~>5lPB)#Hj?efkBZ;a!gM?+R5`}Cs9jhZ*s_2tL$lrJLNc;Lv6)p0}>I>e5BeCv>o&X+7f^6MLCxIp?sNd2r+tuVH}jYJ(2sACnLNzgkzPb+7`I2(B#2B8VqTpUHxb(mqKshHyQ4Ow65F?R}KIgUrL3Z-dMBq2WB!Q`8njh^H_9m<-t1C^zjw<CFF8JLKzLYyR_5RM=U|G&hDt##^l)`d9-!K6=v`XY_mJ&Ir&QTraX#YbC?=C7JJUW`rfheErM&ppuR+GypRjN9vd@P1P|8Oty%GEB|7jW1LG1ECkunpC=`4=i;5W%_pa@xsCXbQtf8dFnM82Cln6G*;zUN?U-)36?!EZ>o*jE@1Akho`DR|Cn=^}hm6Tu+&xgN^eYWoHmmdC|6coRL;s3iIFBdV34<_}IIz)FJhU6I{gw}Eq#_-N4!TU4W2bK}_yT!$LDd)}`STlS7jG{ZXRd2kIh1wkOB;LSKZlEV=|CE1-218f=VRfE-I2UriruJabfJwgv*0h_k-_Z&e4MTxd2?g9N6u`xIOzF-Q-)IKfmE{)Vd+N9QMG#=hMbUlrLBN0Y2`1(jXvY{eNSqOwUdUFRPsYYsrQ(JrjzH(7psg&y3?es+QJKExt_VXji%~;~QQgR2?3D*Tmzs?iQnPBlsBbVACtoxW6_=L&i{^!DvmmJ>wsH^UOIO(p1)z%pOry^1_60h#`{#6KF#`Yd$CyXWh3eU8;I0XuVIC!niWO~@0BLcmR9`b~H>Q$Fq2U6~XHz|!P4#j%g=@1ZO!{bYx!AWemq@E!Y3o5lOuSG@yR>mP8hU8vX1P=Z?$9X#YiMKr3;eFuNf^-8vn(nyHS&Q?Nlh~d48iN?dUpa<IO-y=HtE+`&g>)QH-7I+P00aG1Yf+<40v}X|BLr|%e2*q&#!fwnVR`|&fhxCtYBjEF;4wvWlGNG<87LDOv%QTe%8VlDs-;Dq-ocDM6|H0u5Y+cO~xJN&G?U?tx0RO&ofAg{h)>!se%c~!>sYB!PyA<WgTU>KL9zvS-We5-oal?2YPCE<E*Ux5tpmk2h+yoSSIFBI?X;_299>~_dkiw`zpHdA=)9k_iu-E3un;UA){BC_^EbC*~s`s+acZ54rzoMFVYey?U2d~jvbLgZLxZOt0VH6cF4`V9TIvJW>t4D1G5jGHh28z-y<!Oql-r*LDqRbuBq*jXU(RPKnF5Yc~YNLr?f_x{#Y4LG0XdnHZsoTH2BovQ_bFQ$i?qfYv4u`(Z}QOrJ6!KF?g)=Y}(Olrxtmv{e4S5ZsaTwJlp|&W=lZ~_`$i73kr4T4}-)k!e$Lfin_e`SG4uitx^WuAPL-5^F)3K`??x-Uea&FnzZ+WcJ{EjGbD648{oh7Av5zUA`$1A`Btx3S{|A6Ub+lw6)0(W9T3Vw5;1u`3449pMDID`uxNsm05T-vPHJUl9RvWOSfw^4YFK&Z^U=7K)If!NJ~H#zrKCniM(Y(%*q}u+)XLaeDn7bNt|*2n`#q)E^CGdwj>0qC;?$4pXZiVMUY%G;fn%#eOgu_*RU)jeS@1*Rw4PG^vGki7adY4Sz8XKMS%UBB(O~FDJ|F8crGrnKC9y2k7V^{xfAQrAuWm$mt@2zG$cs4|A-o1C@?t@@fLzs$A-vj%b|ThT0OQQYeTQrT@l%M-!-gII1Q%4nKwjwA%4VuV4mY1!eF!+Llaw}PY}+J|7bM;idgo#jY`OuiMWTY1S>V{hUF_hSz`-Wwt1^I?lk$eE0XoJn8rHsUbtKv-Yjz|RFjvL2GOj!VV#X%Lh!5ho;KznFab9_J2ffHs^@ZA|{l)5cT>U)+BLZ_-XD-tou5eMKl+t6f3U`s;W_s7Icd2nO<U6=Xt}{6{C*l}E8My;e03)Uo=1IG%wk<JpPOWf7zHPt)qJ*x!o?V<n9)khfV^m>_uXor?s&KTX*8DWP;$a)9bl@evIB?T@3wZ-pbSMKSAu06ivHrVK>)g>WB0oMJlLz5|xcLM#hMUih2Q*H?LZK#<_ek}L6I8~ua_3D?!4gJmTA%#xDjO_h`dX&Z`UrSiUQSyEDV;3vUq*xQ;L^7YuA4q{+3KMdp}t_ab`h@60NsVOGAb!#_tzls?<A4ED;AwXn%1~8Sd}2hzHL`ZldM8`IT195XsNs-6+aOs9fwH_Dq+nA9q)~WCHTY0WpzaH@xDBbJDHG~$fHLyDj+I@s}qDz*Q^+;Bx1r>-Pp*;FS6H}SukZRNM80E#Q!TfB0COb9&ffSw@kj)*lDSHmDfKyqw&^5U~>KtyimQmHkqBjQ2qOE_#<k_cJYCej~foEfgygrCu+T})blA~yOu?de7qboG})0hAg?b-@#JInl`8H@n@QmUNkr4%n*g1U8@DkRh!aKCAa$QUNaq7(+(;IHBw10Kqi<B04#EM(JI9zQrqXASr{d>#r5hyg^lUEsqZ@uaS#v{@1S3~B4Am+xW12_xnt(bUZ+-uy-gG8^^DB2=*U2+i<2Qce&Iyj7s5@3gA8qYSm^T0W6*a(vR^`oXim!=72{7%0<2FB3!-hA#(Qi`sJB<(hWx5>Mzp{zmun}EzB@yqPHpI6}pH2Nsw9o=}s})oA8zY6F<q^u}z6b>7#f*FlK8L%_?lE=>9`SgmHc=HJJG7R^YNGkF?3XuT2^fm(uJ+ie#J|+$SyraFFH_uvFilOG|L_MkP+j$)BpG~ClmK`s;r*VDoK&eQ6#gPA%1*B{MuDDNDwCcLC)Wv~!+A&Yzhv=P-gMu7xf<0*Ja5<PBu(iouH42yhu_5YnzZs+odlXTX9}z>k_K%!E0U->#o&r9R+9qjU_z}*F~(>LtVs&2HS2ti$SQB5S7!>Wai+kU%~74NzNhDwA8ZXug{|Wfytx!!9ku4x%n~KYwTAdJFY<q~Mf$!83$+g<X1L3X7<J3xu8`KjiW{U6Zp<2Xzy!yLh0pG1zq6sGriR}gj9V&S{v(6G^nmCrs=etBJvD=%mwBq5{7>jDPccW96a;TN;S8vk_%)p3Y?}%DU^$nCYVj~aTJydl91>eB3gL})-~xuBo)DtDafKUfut`l$6j6au|9P9cd*{FYfx0wT%ZVF}0&m$^%)nrV4aC#U)SNkt0H9Vvu2|o#i8qC`z1E*e>2Q?uJVwr12-RTU&w5}Pb*RI*eWJsdjj=CkFOGhnvUQqTUk^WC{VN{_(w(N#>GOE*w5XewQa_Qxl4t=sL~_iULTWaiM47AhTG@KID4McSle#eM>L7A%#B(#N=g}1A(xP&`oq@UAdt{J><o2a#IvRt1Su~BTnC>bHef<xMuH$Fr$<mX!*ULt*g)FvfRY4&7^&CqXZQzj=tC8V#z&g%q3TV6vhF~dp*g4yhumeHet(E5g)c+-DBJtR?zY~Ll+9`RL90Yxuc!k7)=ix5j8gm2%$khCWV>(U^tPU7F;>NtyzB?-uurcER&t)ggB=t69hCtTOGnJVAuY4KUe8~r!3<ZjPsT)<pQjj=aU;#B;N`^^Wy;KSmQvz{Rl){p7S}q9izjB6&`50-fUw?0y^?_VN&n|Vp6v1PKuhx-%>N32LV6O<3Hqe;oY9FicW=$_K)(lBe(03!u8e6~FR3WWL2Y?Mcw%|Ey#IsX+b!m*9Z`KI)y@9R6*b$b4ynet5ox(&;ZRK7~Yfd?mSoEBtv8%$is6Q&tMs{h(QbS)2*7c;a66juDq7nAT-3wujlqgOsKHVdfLV1C3W9LbT*0Q6R*eWq?A($`Bmq`N3&i)D|jGe5O0$&humy^$$#^y#9c75Ss77|hk1?i54Ze%gz9?zxcD29yG3OzhwwHOMq1<cR7C=q@md!rQg*jc8S)gwo!4n~}mo~|Urn1?~FCoJ2eW-Mm&$9c0iVzNTJRs_P-Q#zv?8+E=|SuCt@_&G+9TKcNw^!q|%Im(}n7)v+n<eUR9{n%(0icp$hlghWx&TqA&QNPSp^A0t~Qiva4IVZU*40NOc53?~T89smhb@Pvx-m&tjLS0%3Oy|d|Ra@!hXQvOA^#1hOc6Qmbi+AHs8++DTAz;UGw!dNaH_onHu5TQ#)|a-yv5j_W<yG@A+vN+BxKnpAH<ID+eUe732^;WY_Jq6^(gl0Mwq_x=&`vYcJ;MgnrqM`A*{gu3i8`S*bv||QQ(%-`FR^rRcY;*ZusGPPU8!`5yq)`|db&waVtjV(h&7Mi&vZq*S*w*c=oVxe<YSV^UWDB0z&kdKsH2h|mo{i#@NI2f*lrwcR_$EbEo#DOce6gLRdWR-&|NQQed0a{_e&q$zgJ1}DO}_Y|DLeatN#7KrfL7Ie}5AfNf)0N)=VybH*48kVRu~sBzH3L#(zNM!5U8V3f#w-`{otqpeinqk}Em=k?@e>^xw(p|65PGU^m&?@)yMc-lh5xe4r<gn4NFP(U6ZV_awW*iT8xLdlp_?X%Z`8ZK#R(LOVGYS5ktE_b0C5G%3FAoK=1rHNJ64D7VlOwjLCwwv|Xf)m9?Fn6iucBgpH4j-na_=XX}i_SD({YJ*Y4H?+DcN>^J$x3hf^{HUQdIf?=p8j%!HFgD+@THT;VWeh9MQf#(;iw&wFbwjHbi2!0G1MWK`L{Qb+TC?+ji*+K0+fh|P0ZUQ1cZ5%R%j@R#VTC)UpR>s@<Ri+!JCb2nCQcmx>n}19Hmr9(9sQk$enIio#);wZ93Y#{NI%xj*fwXqkE*<G$HW}cJah0k>YXhUVe{U{Z2S{jaFftEn1<x^m<4z2gS1+S9CYb9wAz)Bnk9)IS74afZsF@oGny~t)r;6I7LMHFk@K!%@&W3K?cI}iFPcR|yKjR|%8_&rCaE_3U?SDV!o1%Axqf2my?^4RX~dr_9UPB9Z4XDznj+vMNO)x5ME=O5Qh1=5L|U+`tlpH*n8)UTvH|gZ#}WSG4TJE2)FF5`w_L!j|9$~Hr;`e9H~_}*4)fx`QE!=lREKST@Ft)95nPzr?B~bf!J)J4$iV#<K3)zRSq4>bo=#vBKYhNTSrq%?gjLziNU1STSozxtt9%`cY*l`^M!17YX0&~5v&>edlC9ca@D6mB*{VaO4jARKP$d7&5811o$7wrDB8(=>xlKJo8D4GFrv29{8?9ChXVjv!S7W=jFcWTK7fqXDvQS(!SHD@3yftIfcB0@xQZ@nO1cWmkU8HAgYt)r6fLM^sSW#;n4PS-oEn4fgnzm`R*hdwMG;}H{2CMsk^@`JT$TLZ}K)-9P#c(rg<MxH~Em)IWwn+K<7tP#<{PaKlBKyy+g~SqE*pzOp%PmOv(_d$c9kdIfO<j!$pnFf%f;RT-#x`1AR4=zQ5d-(e6;fWcM0eAU#8QVFijMd^*VxW!+Qsr2Ig_>OSdi?1qI0`36CXk0c;cGD^>1Ab=&@tRSx_gxU(w!j!k(B!T%_c^_7>Oc){UV<>w21l;{sf~*jw6<wzvFJ^|Jxh@y8Iqh98OttewEaKVfV!Z|^uwQ~WN#6Cu7)Hw52$WTopg3Gf`SRKc*ExMTDWmWTViGMV_+itk3k2bk5pbz8N@r;Odn3Q6~-2hv#+Hpk{rn3scbLvOHUg}{URkv}?w`iRdSxYzkoSPv{+l^S;mXobMLw*WYwF#o3Z0pH7ZO0M&hrH17_sHlVfsFSz45wmUWy|pX#I0@71_a;Y_tQ3UK$VY?gO@HIRRQ;x_e*ikq6`fmmkJVFqF}%gpSYL93{$pT)#5>N!PL<w@!8sz~P)XClYWuW2{PHck4{NS)B6Nhz!F1oo6vW^SY{H?QrE|zx9|{b%aaPR-Zl{h(log$IOEXXDH*1*pK#F96d=4#3^DG9t+HZCUwDR3M@K(GfGBxjU(qaiFVNk93?oKth2l)P9C-w%b{a6(aIKT#ahAeNDs;(_dR}YpSDg<}5&%gHGTimfq*ZKLxsdz0<o`2-CTil#Fd&xzz6=yzO3NwI4Wr1M1B|vfJj4#vU%RLPm0hS);$VH{cvA|b(<BCeij_GmZA^}lfpT`18@{%6+x}<E&TwyI0PyM)+iMteQEE~^On-b>HigYCE*+z^q?PGpBSwD54FZZ!uv3s?0{yQI{^V2U~!ETOaSo(o?C9`%F!k`#~$iu*CQWBmdG4lY__8hm8)xd8BZv^9$o!b9PVk7S@Agp#XKQPKPVT`x3QMyhMj<#|=xLX26<pubS&6MkoXG$KfTI)qxBA6I#lt8(IRkX#s?M0GfN+1W*R?3HUr|Lc%qJLm_W<zbcuf3qeIWDIyOB~A;Wz~;c#Pl<QpFpn5e9*?ym9r|8M@n$=IXF}0aC9o|Zc7t@ljcMzcgk(!YP9N<?kyXsTR?kx&L&R{u03Znh2>5qOR#7KCe6pJ3(IAz1zB>W>rpI*NCHib;B0X+I|^T+V>+qT3U^Qj5j)kG9UYrO;eSvJC9WX0(KD?I9H3V|R{ZtF^EAi8&+7x5nLww_z9lKK6~mAs1dWVVxbmwl;0=b<*(hJOnx>3J==_TFLh2Z6XMYH2#<GB_sl`P)FYPCZyZ@I@(%G`9-><Eu?QZw9NPDd+RLQq{T3RLzZzTIUg*iia#6zDa`#F*4JuN9n5>t~%c*kqWe$Hj^liy1A_a)iy5Mp+i)b^!=Gjd}rmND7S)LR|TlKtY<GJ6dUkytYQx23#pHLkc%PI~m0vV)i>(dq}KyTUUqc|@b=LAznT-gVg-Bjkg?y?Ku#IUQs6s8;zFK!%Sn=p)?YL{Nw)d9u<)i5~VqD*r-v3or6e85?sfZm=-c>};vDKW>o?_NNBvzZRWwc_$~T$pvK_vQd1~q5<YUhr2C^QRzq{ddug1Wc2&vE!Intv`mY`_7S+;jir&fS2jewf~6Vvb5jU&3IPtXE0JaS{A^RiZlOsQ7^@8|-Nx!Os{@3*Ew-WtGf9}r|86z}y~^@|FjumZ<TIy~;}DGc(Z^k6`$>qkln&dN<e3MhvZ^jm<gMZL#A!?fF+hsI)@`xZ41(f%GYSW&sv)1WBkXR=9FyZ-Z>0b(n*icExNOL25XG2hEpkGG?;CiB4O14v`4S)mcc!IN*b_6RTm+FZaF}=6e3=7@+&R=>k&4I)1%j}@2!XApm%0afO_oABj#8HltZ4_{0g&Dj-@_zaB@S=m`QbrCK4znVYy`R=YB-S~{z>dUm%8qp;s{xnXp<3Rt17Wh%P2@i61){8HVvcJaPJ<pbN&8TR^Xi&*FQ{+cjOTm3%mi;SeG^4xaj{zlzhF+%g}Qqz!QMu`WCSCVq}Ngvr4ZwI@;0l57hfI%WqmdR_VQI_FI3n>^_{}ivq8AV~v+p{8YqS@ud_Mf2Pu#FxOTqnl{EcC<3r5?#3lm`8Q16L@<v*m9DK_Z#3f=sG6K<@5E?K__><ncfr*i&iStJ<h>&)oHKfN;JlZH{VAJI0;1c6-@pCINm;%OY2(CM5JQUB=r7P7b(8*LF-aAOnR8)Nb>XLwTaMojOw-k=da&e@rfQj|Ps0)Dp7h3OJ<V2sF<VQCp{kn&9AS`$lGx_L%`42Y2m+L?u6QWz+(U89;1#}$&7AL|@qqwO^}z>zqx)Y!iEEqv(d53Yce{Om@0R<HHL`p~4({;b9NYnOM>v+R(829)cV@3Xt%LhJ)vr%D$oNpTq2M6j%s`O;_^3Wwjo7&SlaJYhj7S6yr|eU*h%hka;H*I%<B<$i;3ZOuwFlqov%!xHe`*zpbrfG^0sJ9J@Yq(X!RxSHEV7O|zVRhH9F;Elnhw}1qsh8-D<N#mNa?54{6$_`D#1T=)z@}*&0z3oDdmWiCw-P6s(q$=Se_#O(lN4!?xlD;odA*Q)Eg;39kUCgY&*F(m5WQnwU(w{<$%jm^#qRrKts<?toy-aC`JN}fZ0cGN6{rph~;;x-*WXo!tUzCR6;#s@X%-x1|`Ia*&|OSonx1JzN@xxWQ;42HXbeYY&yH!O7BMcJeW9aU341HlBc%B9kopJSM+QR&HrD?CC!gE+3J<1YHw^JZ)@VjRooT~LEuasp!zH`(S0qUYsZp=V+Ws_Nx7Xd<*IyB{>0};mdKstA)Qc*n-&>PGg!fb@^4nuXkdN0mS#<!Tqj|BP0CfG$~K)i$G??tJJe{gSvC};_c|f%H6&r#^_tjl4`B*GsK{<iZTa2al5stkOP{}g!{H5Hh;O*#fAxb=A)eKUmzcB7OQ{fz?f{zz^Lv`DDa`uKNOm+P)5rdWP>8+51v6qAn->P|I5QNQ(B6SkMV7K{Nd&=<%vA%#ws&GBIv<EQH3)phQlc;5vqMPQaqa;V*Qer5jy_Vo7)>9*X9t$<<9|Fip7lf36yq88&Xl4Pu6T$NaEj?4Q~SPC<?R9NxU`>lXeGrZFodaTj+D$p1CvP!3-|0|;q_&oQ(pTxdrgZ(Bswh2Ug>P{`~VXi*^2E=0E5?=r{-r7GANGBwjGc6a|2r#Z1XO6SC&(Fq~<DSrCC(gnWYE;yP8Uj?F+Ik0SS;d2qKr1I?WeGlo%<rDK|p1Pf6hddS<VsD=<~P=t+QU2H6&)2%Sw<DDq2EsXhrkwqo`)iRUA#k}rGfOb$eI$`_e{;K#|OR*Kp*(CmYhH$_P>LY<ir8P4px*DU617V}5X$@`*ugkN{<52}N^QZRzl;|aS)a-=ZprtZ#~7!o(aAfd$@qPl6jJjYdtWuczj9;y_#Lz#W^z!dz&$fsyMqu|P^jd+ojomOcmUql2h5-2Nt1)y~jh`=PS0UZvcjBZ`Q8ckUefKnlKO{T&YO4iuO?tKXpHXw{R8MfE*9k3}q!7F91;p{BOGueTQ%=do<^NFlxo}|aZ*Lf9>^6}8@|KlHwW{b;2+_Rk)sMkM5=sDReR(aP{*twa}P@77Woq`)O(t3Wm9t&z=W8Xnb>6p<-iv|lOG90OeZ?#rnH!ju+>5S(o7#ATaIm~DLi^g<kG_&iE#4hXpBqn2Y!%tKxdl`}5MgF&EwS`nJX`SDS4|(e4xk;jrz`x%D>ItL1xmPQke=F!~tlk_f&=~Y<B2Z@ov-St%9dit5J>&o$B$CAw!UQY!NEtQ3sP3_;5N`o+1cJ*0F=()5p{rtT=gA8P$=5eq(?1U!<*o=5ZSv|lT4P|ow|gQ)aQ-{DbJa1Dd!hm|4m;g{*Hl&@A{|XsY+N3kz5e?2i#>fE&#(IF>j=M&@aqV_K7AeGFY?rXkf;8=Kbzj?-Skyl^Ot`5k^G0(S^5#jHhsA7N`IKg*1z{><C9O{>$87&2G+YT_0)f$r|HE{MF8t&Pv=*qr{lZsJ)SNeyB9qsi3%SlJ$T9As|SxSzSpU&MgH=yl^jE1SPAyjt7I2SCEHDpm28QrJoe}RM)n#q0-3<5clRWWQT9y?I(!egr)ZS2C<e1Mfg&*_u|PfJ#(%hyM%}rDd3)pjrJ!n6SPvaj4oE!MKd+Wqclocd;z}-lI)=H{#bJx5_4Tu<<;%3<u6@>b<;C&hi}sTJQ?_w-<sw}dx#;<ov&t{-gi7sP8l|mco3HB8m6+Yf1NcfcAJzG1&o6kTb|5!$zt0C5uZ)+<nKNGV;yNWRrJp%6cDa&~8ZY}u+D#*JT3oO_aEn*m>{m=bVf@nRE=X-_b`962fjhfvv!}*F<ceO1eb>k{#Frqa;4O(8l*+A2PM5q7Tnj2;+F!kn0zB6N=(g<jFng-MV%?gYLtmbj2cev*su!=!|GL|6i5ct4>+$**jZZ6g{Q&!0ey_Xoqr5S^T>M!3R9JpvsGh#y%AFtJ-Ni+^7hU#zw0*cdfasQ{y8NZ%9TeZ0oywpy)vaTuQF7CZ<1{eRvhis-U_Oy_fL<KmGD@{_STwrm^4VaR9zBlSDfHBr(=JZvg`TprUH+U~zjX2I!u4t3{mp4`b9&4Mu)6w<{`$L@BkV5@h@sE`Eyl!Kc{xmn&4){`J6FvIZ9K!`zWCXg_=^W_@!<O3tJ)dtlY2ky43+ri+8Ne^JJZfsvu_!k7`~W)7Rv(RIYGot>WB{UjvzPnw3Y=Fi-<;70p!w2u}C_tV7CR1W?(Prx*#;_#JAd*plT2KjAp0?vJE=IXAdq!9)re=t?fk+yvW8l6{0!{BsV-WbXSaE!GtXWm2BqD3tp^206Zh4vj*GIyQw3;hz%L~h%f%pOpIgkk;VlzWf}tAHbHxL#fu?{jeRe_I#9zJ-5UUzXrMxn@^Qlp6ZFYPlcoon>9x@ET4;Gqp}szS9pTpzejVZ0Ld$ER<+afAT4;GKw7eEtUJEUM7z!=#R}?9qy7FQy59$w4Wf{vVFR!wUAACubh4q#EZ;NH)f=Tw7Mgs|;tjZFQ4q=lYsNdB7=uMsdyoz9nvoYVZ$o{{e+=79<QX@%=8i|T7;LV#V9QHv=X)Nn5XRpkkjsk2?R$t1=-RxJ`M=B-jt+t_g?v|Apzo^8_Kd54isfcLMY$W;aR=THhII76vf!+$&{%Pb@COQ8V$*Ni7Z}+p`GTwzsay8?9xpMup-|JnW;GPOgHVu+Z+NdTfKOJTVEMBo+q!&#S;o`3yc76vfyE?0o+3KEGVlE3jRv1_eR5`z^#sW<F-Y`~BB!w-#MQ3ei?p6s$^_wZHJ4=p-SvluQwt6gA%*r-aW++d+yIFv_Ui@&^i!t`Je(K$;Z=Dx8N&&_#Gvno{H{r<i1&cRNT#tXj)n0ikmFmJpsm6CNs?*#o(u6A9F3w%v^s6&Og|t~E0NPS#Wf)h+ZT!fsGR*ky)eE~`eHkO2Wl?Inq5jFcdAmGw_3NJa)Jv-`W5;<Me=jEXmAXr~D6#k}#jwkY%i`~?LW@5uwEX8^gdh194d~Wb#*MUaWV)stFNg~L6^g<IIX`;=yMu8Ol8tlXBs6CJVPYdRT7EEovYRLv10iVn&zjCC%e^GzpU6O4a@?#v8YM+AC_d2j)E7h+cx-%ZrWT{1vmM}_2(CfvBu;+U7H$IZ>2#AI4+q`{NK!b;OnbBjoz%s+1EuX5NnjXB0x4SUN(*E7<dQ3YrurLh_+fRR>}~s44S$Rs*moh;0eW5JrXDIoe6)LjIP$E0)IA5+j6WXLux{$iE%dals4J}wb+m(tC_CkMj90zU`bq=Pq_*=bTko4t-twP!topG9cPsUiJ%~p=zq;f6dUM1kZ7o28ZyY5|OF8ZiP3K#+(feQ=3U`6xLTrw|tE2^x7ep*{2~mQoWQ)e*WWM8YWGkd}bS>V9>F@tR;h+KSNBs;9&DbL<X}en;%H(c!^#@_1p`8yw;G3yQc{T6(dm)RFI+O#KZnO^N)pIm74y@|WcPJ+cZ`5p9zl)~NGK-$L+Bqxl#^%2cJ&4r*vIS3WEiHJhcG4ew%!cKkul_wZ{B-sBh^ZHLRi_32NWEqXANKI&K_b$S^-!WDNhI(2^@hwZZ6&zWBd19ai+LPfbs+JM+(Hj~k`2<=RhVV;=XqK+6tA#31tsfv0#Uk{1(Mjx_uwrnp0yQ~aV0BBCKrA8JF>iw&f1-;b$dCSQrGeK&_vJx8|V5CF{pwMG2c2EFIR##v?NM;9S29UU~fS!VFc=xR(6Pg?!)W-I{u)v;1P*5V#;=;+BkGa!AgJ$He%ANx;oVTB>cNYV|NJDA)vMg)@qkuSxu|DsQzj_(+1A;syZ^o0l$Io&1)Kcp7)aTZMi1<>fpfAb)O^JhIC*9XbbZzcln+kgrLCoDAhnTqw>xiD2bO^`UMDWtt&Q94JeL&ulo6yOHX%suAWHnzGhFo7d=ds4*Z2Mfz{BWwYZ~DvSf6&XgL-5p@OUn#bXi~4)QAxh@<^s<Hh~nlW<-#eJ5r_?n!zn0>)%2wEjT1RxCAn-hLAe?9iPS`+2s7pGhDd=nV9{A0MTajGq&Bq$3Ay=7P<5{!a_XHDIzyg=|}^Pf3@KcRkKOwKA<su%-M@UsZEDxgu@TY63ak#t97W!KCJNY5ZO??j_7nb0j&IspYh<&lvYew^xyF?}Bj;@iQpM9hASrbtS-t8$J1Q2$~zEpQy4SW3w)YDU7QF2^g$DowTjBlRTJ{K&s@gN6{~mCPkyWHeRWGu?^{H*4!jI6N!={4rO>rnoZIc$htK$S9v20kR+C-CdpgiO+!JoMn}EY?A;5R(^qr8>Ko1JZqc0nQT))K(R@rld{V?9U&gVjhsy2gD%=%~If0e($4Pn-s9y$=td4<1gf6y4Ecc|1B9;A6yLRi3T!9ejsG-5}$T*}0IWV)JJHMj8A)YYM(l~$LOiqrYfb=6tW_P3w>mYlBnB+u89Nb$4Bu(|E#qj4y=7haxWK$udzLKupOriH!tv&~n&>w#TFDTqspHqed+&TYN_1mugY222zB=ykz4&92D8ynWqHxMgf6YME+oF~N*nmgQx0k$JaW0fRJyCbBF^O|X0Eq>oB`vv7tb=60J>LfiDfyuLvO9;2*xi?X4XJU*sRxqV!;6+e?BY{|H1h*kopAY+X_D=`tyHbq9nRMdO)1(jNg9sD-*!T0P_LbqxB%h3nfP`G${%Oqf7KLBea?9+<j+6%zDD*@IIui22-RprW7frGwD{tPNA~lB_WU_JpvDiuA+R*g|#JYBIrIdvmWw;qLivP^}|L}vG*%?*L4GxeoHux$zKnAF-PS(|esmeG&q?ZFqv$?8Xkj^y?EUoKS3~}|0dyK*sj_QMsxWa~n5dtbkGpADRw7pJ7wJSyyApzIrsRSE|?Ax)!HVbo_zw6G)2TW4@<x*(4l=FohX6mV3V-C{Xgkte@c{@Njzmo&lngW?6Of7}Y4A*<QFAtd0*~#umh%ua`4PBAy5u6*_ygzQRa<V&?{ns28GtEKMElriR6J_Hrdts)s0;}>sW~c0V3=HeS37>tWOgx5tXJKHzb>DW{TB~q}$J_k)j>}$mwZW)AtZ<)ul6W1p5#{sjE6t94gTI+C?*YaZT<!>|;Qh2r4^d}1zm7oyll6`iEWR=&Wlps7(o$=H>^z;aZTXTs*H6UUSJzdExoh$lJri?tHa{PBC*wG5FFhEA-HFFD@}~VEXQ5G5N;)YJG|YRFu&Xo_6g4NttH-4HF<hKvP+V|>)jFL~02=YID<J9lN+ZP+>4y~_aMjgUTp8TGzNQ>2gx0I1$_r^G>5>KQ)s9L|TEh*KN1kOuE<U94(x@L!4u9!y-$8}-8Md(1x%_2`vp+Q@RQxaBW7>8k3HvEp`z>{6jT=moNlSXLSlw3=av`Djj3I2#c=}tkp73}?5*B&4>FXF9odL^n+7<Y~s<+jg5{&sB!rGblg9BAKouJSplfF?E(D=ZNFCSck4jfSJIKL)KK68w-eW<x3fZ502)3Ze+>t|DmHts;A`iT>^;iNzWDv2*mCF#>Qpo2WYlgQ!lIFCv$AylSt*H6+eE7^GvAz~_l-cY<^NMluP53A6B@=3IEql}ac<@=hy1ltEj-m4ZcU;pX`YdUD=iXd1Vxzm-dxE9P^O7@aLy$!)%Wl)z`QM^W1r>KtfrZvh2Cd@$HF!MW@x+rvY^y>4<Xpp@+pQp-0`qE?RN|O_S3i(uYMkr-DxgpY)Q+PM_g~n@!^14g1i1UmDRGLgz45b%AFGj3ZauxRR<}??@7H(5x1k!Un#^qzMD~H0$J`+!B+l!@e)uh&oPtE>~K_pTrpR%g)cfKeqBg0CDOSV4l=m1=J-eg3Zc?jLiB9F^r)G$v>WMoT}jqllN5OZTaPt{F&ytkG@8b$JCpr>_!W9n*VqsQsbg2%3wjpp}`w2eer<U?qq$1KJTGd<30{?aWm9`LhwC4b>W>R6pT!Y-#D!jjKGZDDHH!Z4h&UG541VPtn4E%Ggb$K*le_M<@X_!p|*;Ea%>&Jj7x*4o@Ov$9(+n)eE_Mr7F=*b;`xxHBnBY^jeS;LhXs4a`1nKsoL#w=I5MzMJ>u{Ni`?$_}o)-c82ej`AG)*ZenX(z&kSjl$cu35EP^_TazUR(5Zr{<%#xoec%m=m*k*HzbG8jxEZnB%fCF9|k(1OnF9rHPWRm^<)RQ5Q9#&@*<^24W>mGTM&D&_{wvbeKcUDA4NX%TYClrPRV;0|J3s;mo&v)h(kAp&Y=ihEf(;e-hWxQ4T;w0v2tCuu+Y1FKpsmJxk<(yY?Z=6=p^}3IJgsk(<tQIlE89M0juQE_gX4Ubc?kf3BnGig5I9gdV2`AAjz`@1v2Td{eYMix8f+Gbtu&`mx)X_f`mKzxT|cBYQ&~7&%||A|6NSbLZS_ebSer22R1Q|A_S|LTBKg_bl^YG?W5Qqg~dZUbqU{7&c~Z*eNEYWYD2rCYfsTgS8~o08O%$*wH*erW<dO`ED-Zc-r5xzge1hT>O6G99txGgf}vyjwHh5w@O~3orV4JNGm0dt6szeb`YpE2nnzGUK{*TZO;+-BX}*|EG*<plG`Kix{qpHv4eT^Q3QsJep%db!BMmg#`pT8p=YQwtBqWUB%ITP*_bT2BlJVOEvXE=p_~ps%F@=Rl6mD;YtKUw1T0VUjmS-4`5eUs!*RFXQB?Fwwk(nPu?K1oYL#S{5zn4x-BtDmOvnGRoZ8H=JoINmgtky55r?=FwbkVehHaHSHDi^5K=Xv*>HR1A~gtn%BTPY=w{L~4R7$uvjZ;2uZ5$Qg+$N=q1Nm-QG7bOgDvSZGAsRi;?^}U?7Ef;Lyyzzm+nu1GmP1tAQK=6TXR~+fweH693^jUN8s8o2gsm*z`xJ4A3pn`&43B_x)`^+;GTkTU3E?dln5S3N6@0D~!a3ddpiAkJI?ZQi674Zq?jqP2zKhwO^N2Eo?E3s>^?;<nsbV;?SIA(`=opb!(cvalR@MuL!`ZBv!>Gvw?S0=15`=8yKytqH3M{d=&DxCQD@s~|B<PJ_upkw0IsNK^Gh)g;M?Rb>)*dY%dHaYgCE73(Lknl3=MpZ+k3IpZIJ6$W2@7h$;+DG-ohw8BR&@eDLZ#}?aZ?J*G7K?*B2N(Irp?X4j1{6%J3_v@}XyuQ!P?=-%Jrx%td`jToBpFpRvd9ru#R3LRJXIF`y@RY_TvJ&%NA`8q^s%lTtpQNtNGKlh6+eyzNlUPbu@iudNhA8x*(c2o^bakM1c}zX9V!)-d?lYRvQ8kCsHn1b-kR?uyiy#EfB3Q0eq9hTN1D`r$GrUWP`d5fO@d>S)UP{K&#L`Wh@QSlOCT3CoTd5euL%CetAfAI<)1&Q<@NH?WlBcb-#G@4mr8T<oZv6=oQ~N!B5uw!f0^EtP(<%6@i<g-@n6rGP`T<!!C%T2QqrOl!U(CwzG(ik$T6sBO4ocyxIFD>&#3+8qgK{&vRBYS5cHYmZ&G-|0^diCP=4=~cHxzF;kBXq_37&fzmD+h2*1)UywWbb(k{HxF1*q%ywWcG0h+Y0%nPr~3m=$y0m(izz62&|DG3a4S&MF0*E8K38cT{YA$vx5EvVs3C>RVlx@2K+Zb8K0W=za(-b>GJAvf!&H(rLFoADyw=4EitzcPNEPg95goOBs=zOjYdEeV*<y83mG+%<xRx-=Dzr=62K%%~0AjJCi!pM@IPt5usRFMiFOrok<lv&W|+Q^VpHMFK}|jSMfFi&|t8(+@FRYgFZJG5*sqj(iPjeV<b{G|Z|}0QHPiq7VsB%oNk>?umn^DI__+1#5%5GDFUOvRllViGyP{6&I8ZZpPQ(M*i&9a_dfE$TkuNQ<#b81P!j5v+&Lth@T>8h}Wo~!^oO(gH-#8x1MCwev0nF-=Z^^(JlMx2G6lS>-N9(ldoQ|4^RD^C)gRDes{X08?@!_f{^=+KEOT4)Nn~JUB&Y=jARXN#-i=~Z5C~Bmp$io9@#qPGz8blp0AyAe8pcQq?ljiRZ4{$2Y7dzh~e3DKJo4gKX}Q4F|sgJeqs%GOM2|<WDQT!H@t|o;W|n7Kl9S=fJd}Gp|bKwq|Y6?Cx?4fdI%jsV=7x*@+)qwUFBr4wYQRt-#h?dn;$&ptznCj-A)w|cHauiLBxKQ9{gu&$7Z{2KFOif)chT}pDP@Re#N{a99jEe-|xW#yDRhmh<8z_PrYN)ylTr}Kk;>G7C}+bYU${<2QfHCvd^FYo7G=KMF|jr0D1ygQ#8#I?BnCkfkXVj=B|w-Oj|Tu`KC$->|G73QE^|TEo-ESU7v)40y1~tXt75QgBD63yzBxUCY0oQbUE}yr=T$z)gr&Y^9>q@{aQNc=n}!UvvN)nBKgN`xb9J&6B&ihEE4cdRTKIWh^)#7925GF^6(r{4r7-fp)_q>)eRbs@+8fdF|Yw05*X31JV!3#JdQ<C%s+sht0s}Gyk=>S)v_9T@+3PVhW{9ZQII%<s<;5626>}$4e4=v@vS#(XKaY!VNH-i9^^nLWC7*q%0d^<ig2SP)v&V-<L1yW<k=nM!T6<$zIAZ>s^z%hE|PyK<{9<ZUbHr#Q=8{2C+mF`9#J(HWVtyJ<BdvPs83c)Y^x#?;@R1<_M61^&xJ$Frk*`utgQYE{Y-G0m9%-zJH8dIwYeGcOMV@#C4KT^*-@PCrtb5>8_o@{JJ;QDVxku_NS$2(xt~IpJoIn*EpXfS`S=d-HFcP!(%@d|`fOxp8_Kr_YqRai?=ZBea~e>)sHViuzv%$jKv~tREQv^97;xDG+IXCZ!(4d~RI07~+dRweDq%&{d`j<VY21G8dDz|=E6tAN{nx25$Q{tn+T~kf(OI=6W*hz9-K-%#9VCd(syy*~yw5%w=wpQ23L42~2=##z2ck-Ro75K0Vs;JJJ1;pPJu5uT>q7nU6CVv%5$s_Tgd`UtW+bctETJi_G8<SHW1?Z4jQ$rzQ9(ClDrVQ>pkeWuJTd{;Zy`fhg?(n;6%!4)-5kYkz(TdCC)nCcc7NQoL%x`w124o+RgYwW=^n9=_W4KrST^33l$F5hkT3^rA)yBYaF5}hU<Pu*#GUU`wHJE}np{WZg-ZW?N?V%lDzU>1Mw}Lf0Q@$|B}jaN7YE@CD|LOs?&Y5lIc7cEVOJcyw-0u5$j2vOXKIoTnR(&gHQLeKXAD8fRua<@$K+ud2<HT)%Tde29USdQwrRwt=Gb`W?1!T_1;iIzfoqo<+sYJN?eZ}Hn|a>XTbI5`Olm&OJ?Hxoo%e?k+XiGVTbHf9l>^W-URIB6!+kv)sz+ndNkr|0Xec#tngFQ271ssZ&IsSl%fNFLYe{VMdaITX*zBHTzb4iUrygizLQn+TafLiafLUW_q5T^R>q0>h#$kia<SkGVI6r~j<Tm4Jzv)VbVGtZ1eL&wC)i?B8AhAJfOmK2dprR<=@H1O9H}dyVCdiw;%?A&JxF^r^tPT8J_HY}7)vi2s!17W+M19F2{%-YiA$~g#ElEip$+XeYmOJ994+I>Ng(3)hh_^`jLE?eD^wQoXX~=J^cNXIh@{vHay+A+c5DvCQ@Qy)V9ba)0%D*93g$b1qHn}P|=<GW+003J*0L9htl~{q8g!z?v?TMW6y09a+6uh3QwkLuwKSo=X{|37W+@6dRXm1B3JlhmtrM5V33w|aBzI*(TT90F8d<ov-akgrLGDE#bKrrc75Q0TCD&Fdyb*bbj6*w%hRz!?t-*|y*am*^8C&4;7YNrIgo99I~gIEL_;X>U=-4a@Iv{m3b@hcA2q`_;(h~YN>1{PtyOW&jSn4Q49;PSlQVB0yA6=>8n3BdY#ApHxc7clxA9A3B)d)}Fbi_McTsR8ISa(hN+eZ{@ZmmB4AHtNzyAH{D9Z6RJcU@Mmc0brdL9<^kAF_qqHRWRky01}?R?t5kVVRF|Zcfhh7W;wOQw-WnhrL5%nFt5_j8RQ&fYdZ49)c(g!QHYCb&7CTs<+szX05A*uNgfzBj;<Ch7c<;Q;?vTG;BdK3=n4@^tsI;%Wm;#Rhf+`lLkU}B3)0gE!t~@m|FbWRiyjtnQA%{=HW(7v)PXm@<{}@(fFiJ%dAjfNUVcCFd(t1{h+`Oz?2hJBxLboFB{oiHlL$(&{OieG2Dcv_w=D^$K6gCk4iqJi`7z=Z1XPb~fi7)wv&`+b60b~4$0CP72lY<#BpOt}0Ehf7<*i6w84g?8k4An{uJb>Gz5ECG>4yh85i5j;#`N?@^R*X#hy0++emR50=nmc(vG!c+4`Mz#;R5r|MYky9xK#Sxu)(vjJ}_X&U$k;|1_AY2&^eLUjSj*0?yIdgOSs8%@tC8_96S10Ui`sb)ibPW1?*I`kS`%2&z8L=@<afSnD_o15#z0sSEy!*$$J(en3FhFmKWbVvQa%>#-Wm*L1-wJD~PWC_fNv#wyEEbyshodTgba5bDOV9EAMUEwwC>9@!7WVCws=ZKtmd-SQ#QUgnAkWk@omGS%Y`2TQo<ybH0Wrn#Y}KagxSD$Vsnw#n^d-^AvKNiG*g^Ki*W*+R8`V&D`XsfIQFm9m0A4IKZ57Y$5-It-rtf3h8`>biRVMUZ1{>@aqV_j_@m_^GiJSU*O}fsLoeZ=PRo771jBQ>U>3YemYd=1j|hC1MEysyjZ;-QuI>-JFAES;T?gU+}>(&;F16pOo5#wwIaz4T-Z#CSu_2l;7r}BGWqcdBR9uzR?a|x-c?H_tt&EG$iakj?JH1|j2O{0JvfIT`s?SMzlEXb&kv)3)<TSG`j$}%%q^gdXIfm-mAJw>KLQR7hw1#bR=4r=))|hm3@>tN1$a4KWPg5<b6G6lS}!h-(1qE-&PtTHn7%r{yjAVP;(Gkq<r(zu%Jn1rl`ckgcEM*5-}wVoxUT%0fjLDajQnK7#k;0t&Ro~Zi5A0NbfZ32FmUOm#??YNr{D}H6(3h!RREgce1+}f3=qhgQ}ry|krV7?!ciBhS5LtahnvvKOJv<s__y0=$?9o5<m}z?!F;UdkNs_==(Vr#=g89eHDAL(o*nQM>hc2ScLvq7aMDl7y(k39>@XM4KQjO4F9fc}FGX4G_N9W`;L1I6H$kwsZtDeF(p_H34Ep$@$6>Z)!VET9S7)+ek_S6OKgK0&vYO412_fkgFRGzn#(u+`|02o#Pr1KND^Sl2#PqoE#Ek#+G?Zh`{*Dj)?D*+yv@V9%=Ia&cg`CK_>gW<B5%s}rp&GtY$LVYw273_7yLEXHjNyE}F8|`}BXK-_e!}S1x5yPg+`n@~s&}Usf3{Iah)8Zm>W$^uE+2?;-BmXZHcrbjZsWUUY&{3fm(e4+(BdsUaPj=Bx#3JNR&hZWV(%`WhVh<Wy$l>yU;W{W@4EcP*{K#kgqK~*t-CRRXTM^8<=j`NgLQrr^dy?W^aNwPvK;M!pRRM<kfZAt*HFk!ye|)8`Dq0Ky}a_ZAH~vQq0y?#r^0x`4L_2EG$gUPHyAafV1KRp(;;p`>_Yqo5H|y%I*|SmO7cNQA;fQ@s{b7yVt)51?)_|m0(tUSMLn`k=}GT?0`x{u$j%UAh6fuSMyw~W4gSuM34)Mqh<Srb%f=8uBAxA+>Pkk)19GHqiA#~^d23o|cG`T{!0I>QGr^y%EZdU}zhya658hVPLOL2=PR=wzK*1lqF5ZX~g+>EjL7Hu(NFz2>K^p0sQFj(x0A!nn8TIt${iEPTpBcg}a>Q7$Hu(lJh&kXr?uEn)@dO5@Xc`S6{ykOE>lK9a+y@ktfvDd_6+MqZyA+fel@18WSSTID5R+I}aWGg{HwM`~Cm@ccAua{UQ=ptK>fw%hE8ZjzNU&t&Q(`F8u;t5Wd|}20f$GFK+*A@BpcnzvWJD`Wm!3RZg6w50(0VI(N8_lg3^6k!VLfAB&w=5cIA0^7>*`kW>fHlKL7p3H`1qwY2W>ztpPbm>dXjxYTu{@A1pWeN&k-D)4lyJ#Dy=piJAr1<aaK9+7nSpo7zy?B^l2;S-*PwgWu{pvj#Z#-9K}&MF+)?CQN4;x780siFn@tdxe#Tq)WzsXi>p30HS;mTNX9<xoqL8iTmKWgVm8jP(19^lGu<hQC{nR(P!EGedM$feorF7hSW{7DaoqcAGtsUXZ9XlHq{b8me3-Y}<t4L1PzKJtE?Xom#k5ldljgxXaHDc(Lnn6R{4?f1J;s+ta}_yl$@oYHS@T}oa^})@;|)M!%$VZJR6_+Z&a`4}(Uss=*v=Iyqf{&#D0CMrvP|q@;9Bv8-mB5^<DO3HNG(>n^*DVbvQY%k((G`~W(AhfP@vkzp0^lzP^t2&?$1fbxTF#y)ad4WZlz|&0#d;u8??w)r33M!EwcaiiwMy^3Hd+c(>q7~M}zavf&bSR&=US1UjYAaZovN=$Sq_OFAO}ev<+wXxi0P42Y~r|trehRL>0#wy6gs^?e?TLopl2g`nzBW^yacB0CUfYkvR~{?3-)N0nbQgU^b~^VED9#`=9^7(uy<c=eC`B4zcu&+!YDM?VOaIeEk#MGX?Lr5<dc-t|p~ogsf?`iKKhR9*P+;Brse8u200@BlEp^t_5<R#})gD*3~vosD!Svp0v*EHMW&gQ?>hSGODgoM+cZA+dchLCIWPej$5eRMQ-IER*RBqev2{lZj%U@_O|ef1Z7_KQXl~zCH$<`ZJUM4LkGzbvD=bmJ`eeJsXyr*rP)Xc-J<&eb{o{$SYw-{z#Sy=8uiqGWxNB2HfV)o4@_?U$go47mYT;?V1iTh+IQA>b-ITwXf{<-3j(N=sXHDZHdeFmKhODf<?nX<Qts37&wgx~&&%2Q5}D6frfIa?Zj--aHCO5qRWSs^@QrEeVWN*)g`V@Z#U*qC{{qf!^yEhcLHXbZi=+^z<advF9l9)!^w(1nAS4qwe(VO;;|Srgkc~`sLJoiaD_q^#b666)k8#1Y#ygO|CtA;ID_wdE^Tl4wwy`}|y(VQ;I&m6HFy2CF&lbL)Eqq!D8%R=gkREphFZ~Dxd34;w9y2wYf)lXIu9?QN^mK77_jFczK~qE34xFaUJEN!TJJp}8{%tq>5fTYMIQMpHJsNC$nfDCU3VL~Y6-7t^a)X4P!P;fZ0v!VK1Se{^wn@zQIdu1Ni{;fpSHiUoScGk%=Yt2zu}3x$sa0z028)ZZ#7`RpSA9gEY(9QBn9+1bz6!u_p0qy+p%%Z-V>&>1H(y=bKwaR#UM=jE{JU#8lqcMz?Z!8)HF<sK(UT+D?e43uRW9Fyhkw2LEpmutH}gLKIJP3+foh)`wU})1L{B)eD9;mhfjyKPEAo)T1MMZTS6dUC9MF0vihB7M?3sg_4jV8>7G`e(hIt}wPOj!t$8NR*3sI1Gh}M`JoKz4!l*hS0BYEI)&cs=lbPu7hfOs&wiE%%2H=8S=b{e?RadglbuCnjV--((-s$XtP`L)Ps7Cg~XzRcIKlTYC_!Ej4S#!mKJ))@m^@jN=R^G|Ek@}$2Tu>$AYDVl#Q8MJ6S-ef8=$_#uBVQjv0?>>LJ7oJ|@;NI~<veS^Q)I0X1zjNi4{8xVDUc$nRk5>3d9;$bcNn}4+<KDrtArYlW?%m=aCigo}Z<6QSbSA5H=BD7t;ChB#?`qS_8l-ti7p=qb&>p02?R16G`fORSV>FrPH-==#dgGcsxbK`2PaG`)_anBmMlJa>-C7;IVY1;}V*NNFo(fdT8Y~0BXox);?@FF1pAE7HRA+e?mF>bsj>l~IL6RD~cOzK8rK?&}f-CRZ&PnC`oxRQow-P_T{vqVa)A3!6JW)sX?|1W)6WE`4iB=Hw`chtuM$#@rW5~Z%k!@rqv0a(SM7TuuE0$k)x{xmUw8;MUFIDpu@a*)@e?Q~Sw>gt9G^KU!7VbXL0QJy!!O1<{CEfGRv`yr!f%xgp$Qatv>kdZo?1nbQX!CyVNEhEni}I0y=qSk*$retAAC`FYvNs`IcH}T7@}&tShq*1zz?MeJ<T?}maVv6wI~WVa$Jw=TNb{9k1#`r;cU}HZ&ke72T@CAryvu>NJruxAL@RHnzUQG*?I*9GCV#~*RqttZ+)gSM*p3~W-cZ3=;Y$Wd%Wm?Jvj=hj>$wsWHAK@Y<=Og3Mcjs{5Bvyh@hdD+4FAemGnXu+;?!nmA!7oe1+-_{$P!fzSsE2iHm)RxIjsrppw0z$R44ngZz*`fFO3p5V;tE~xTjG^6gZ~*&?;-_<f*H*XoD{`IAtAki~~H76fr<e;eB(!wte6+Xo`{uut{cM!<8~{%Y7=r%Ya0=y2WtG|Kj^CfJeG@Y-L<5fIZ}Im|EuSZ`rQr;rdYowd(F@#@%e{uUy}8>igxq&lad*_O~xK+1b1gj6sY9AThIBnctT*@4-aRpVgMIKYwZD0X+sJdrqU}%=0AQfmQM>9pX~wrn2MxQNoA5TUGar=NZhmvrhj&-9it2$TH*Cw4ah6`&qey!)M&2-(0$aaD7%S2l&1UZzR*qGHQ+5r|J0A&f2P}Vx={S0bb#jcgnQ&2x~jE_L_bj{A}Eyan#E&A7F6Gz@xpd+c6bm1_!UCJ-tNFcTGvjsbPP;fhyIS4&G`&a49*91N-`Ad9Z{aOY82rc{U_n>3B?#8qt8M`L$v(_B)IpI9~E?-D8?!p#S3g&CUn51xtB*K07_&SgD9(-#3_8Xz-0?g3=@ER>d}3XoHXUhih|`xrml3+}VZ6^PmqlQ*D~E3$WN`)gWw|hGL#!CIdNxB<9fgO^rrcrA_+=flS9_VoMi}Do?b2;;Oi`${VMQbH4a&m_190yA@>x%P?buKiEtiV4J;cbKqp{e(zEsDBM!6I;nO@8E+!cG%?Zf?}Yv`MIvu1O-Q5dz!}2aS+63hN5{8|b(9P-&3R>MJbkLBKrYjWxFIJtu4Xen029cKP#wl53S@#a&d5C~%IS&H!)kJX@kD1DS2|lA>6LpRq(bR$jHV!zzh}kkVbYLO88H?d#Za5zk3?)*oC$ZM<T@!Y6K8TdqA9{*IAIXYqgft)X|218-`+@_rigeMtUlVfNxj&W(wP$DiYKUFIamAf+MSF&j~5e1X`^Ik(@!pKyk63Pq3H8?vNZ)0xUz%GoiZ$ebbdn7>XB$qs7$^XzqhjB-WTj-V0Kl<@Lf``40K-^UES$-fjSDiI`Xjp#*2E?_Xr>pYkY{QA5^~t_#^*q2G`V(htBh^?!mT|0t?6a?(JL?sQgCgi2|y;k{hV8Fo8@($fgC47jkJVyyi*K<nN-iSq)DG)2d<fIX~hy0UKA7KT<=$k!N#IbC1|k8fv(Z(<z6n72zqKd6WDgTL$#`4)l8(zJ+V6P1D)nED&g|T9^i$7C(^QMnhxKmd`dhd}(n^!@N_I5YX@~HVgBr@@;M?uZ7XbZ;{c9_71<OY3z9XaP1D%odI+*ulo1*?vAWTaWbW7a}<yRO_4mP^z?c<l>wd}y{1+=nFMA9`q#Z%(Z@?nWd`c=q(Xaus&QkU-df@?0x2CWS}$GHjFF+Jh`nIp=~05G)ym;SRV<Iy(qgDiEhS?)al00`C>w`|)~zVVb3pOIq{XFHR|jxv;J%?CDN;5RB?5MjJYisN^1%1JhV0<wBjbuytNa7EFv^L3U4HGDS9NbTs4#M3Jn#H_2l$lJwBU|4zh?q`;AxR_{^9{X9kxw<JHT&T-#!=McN7tPBEYXFXY#24pT1?m5pdrYl;CQB&!pQF-CNjBq8wh#jyd0&_0V^fM87SXekQ;likqqfykFIh#e4?%+!LfS*N$E*$Er4X3hc7N{2F0?iS%(MCNY>d%08vU@}7<HO&y+)lRQ4VW(xD`i!h&v`b9OXC*#p44D*LycqygbJr+T{C(o7V(|mQ0Oqo3xK&UX;ac2>N`~-%Nq!b}N;cO4PBgSUn4z?y3;lN4@E9xL9N#>7$I;bUHV^5^ZBdKpzoIwLMIpKTl-COQZTZ>Vx38XNBpm+fqJ{MXt?j0-4)|y;D`Gnb7Bh89HN<kErJJIG$X$OFd63Z{OonMT2B(38|_Pp%_o!ukh4DD9DR3j0v_m?;GpM25qKNdPcd8&`VafS!{n*C|?-X!3iZ;_&4ybJu-$$idZME?88ADWIM#~~~ve)_R!(G}+`k)s5pPA81?(YbG_6XB!}g8vye;ojORl}E|<6FhB--%mvBoKTzS9;*JKtVL=BCUH>zXD^8W2StEKXOV|)08&c?%!2*LiHO^Y+1tE9Fl;$)HL<87CT2Sj`g9dh5Wel`<rW$^DAfs)q(N0;BUQwifQ*#Po4k`dyOIXRnX-0rq<gZc<iM34{GfYMS&bowIMQTSQfvTDhdd_P`g9~cF+e`jBm=8u>&{4worGzV8%ncUPm#xb%{2>mec`*rRxjEsA`BbBuf%N>psO6BsXY=s;tjaT(PMg^zP6)j6RIRgiWAq|a3kO@>XW4|eL?lvk1_>TN8S@&XXDKk4^dc3ujp+<r?V#G<A5#O4FnG5wcQbj?dLhkUw)~vIzeI)b+rd$V!{$aCIdGl+mNj{x|lRRU=vGyB2QBYE9Z|p%*w736`6Z5x;G#y+jTWWY;pOA3~RVPgYcQiUire98R|XLFhMkc7LfRnMBAY>+3(%Jm|Xb3d>NR~dv_pwVsBvpx%T$%GhfsU3y^Zq0|$BZ#EQsX=LxV&Te1s!Q-_DG3oJQtLgAb%=4KuR86{3<$NASE1iUP8O|Gu?l27v&tKY`vA3o2!ag|+%dW&fiH<0K~Z?gAY#nPcs@0i(RxvIW1_C!Rs2T<#Zz&G_V^=8oWh4id*8On_qIM}5<Ht+0y52c)R?@7j#tb7A0-a^2R={4Bmp>@F2>}j$d*NmE28*FfLraN|47*YnhW<6sasfr3TE4hA|KteGN)7ywU^P1@?Qrb{k{JtbhQTO7<TSagyl&Ctg-6{6A6|1m3Pvf2|kO4}qyFCcCPo$TAPAxt@`Q+S}{=pa2)y|RLR`EW$?m&G->NGNAVw>L>i<6dfo&_5a*5yURJY*xF4+0(uh`NU5XbcN>(3VdXQ}@xJZY0VRy3C1+H~)X2M@le1i55s2r5X^`j1hOQqiI?v<v<XNS|&swQ-&QHnIOPkviuspxF5xGO}KiVd??WM62g~Y+{Ac&(FC5qSagHOGgMPcNVIRTuPLU_7hp+4|C4AcXJ;-+gCTfd;E~LM*naLuWP3K=JdvpfPfaN0ODjLBG3&sFl!i(o&2_S;>*w!PF`*<Vrr&FS_0M$2rx%rz@gunvp_6|6T}7wdF^S2XTuEo~_&QGG>1KbU_Ut@B|ESAm|B-`wcv-AA6bz%v_p9Qt_llNo#%-2%0fG)=ZlPOa06+bRcQr#dKSpfaqj<>{y{VU|04-VB%eKs#g1GtP;OikBF_`(dNAK=cW-PJY=`yyf;;=rC?OMfl)mR_{Ry3^_vE62h?J6;+Eg+u&4CZhUn{aVnY-YhRA^y+buIu*8x~@cW-w|P0+D8bOC7Wl*A|U-O-EbV~45C{pzwlgK$jwpMVPgn2+^c?qv)3_|Vp+!uzup08p<anfJeDR^KEi2Pc6v9%_Ks~^*qfMNem9=epu3LoTu9@1CMGYebd0mDUQ##SX^7C}@rG07aUM-tr;dSe>!QV8R<kYrBL3@({x2NmcOHRejabHYCD2S?b)fmDutf!zzE3t=ap!*v%lFa8A&6F)k<O#JY;Z~BwSn0daU}X(@}`9p0C*nra!(N`tgc{GLHEC+YwKButK5CwHde@^i<W+PfO`t>-)r6>qtSp+5CPnN3mSfc=P_a}QP?fu>`489_@4l(h6%rX!EFso{Phmj<FWRlZsop<L=~csn4OcVFJ+&WT^_LSL$(LlnFjck2({GlV{IS>&;n=XpZ%(aO@$y|hOJkOgZSm<urX_VW!Uxret<EbcDz-j*ewT4qZRzunTW+`#Y&|Ize4h_j1w)6#wl+V>l@>=7tF`C@4q$d%Bt*Vi|)C7!SZ==>>j{fI@=wz-`eg__TjQGoTc})J6Or37y83Ze+B-$nf4pIGrR1gO&i3~iC6sjJ)$dngj1}RLxYZc6V)Ob?iA^Kr$9<_&BmT~bTNFnW_oQqSB%ox1`)N|5Lc?>p}EWsN>shL8{8vIJxVPjYSvZZ`kg$Z(&3jz^w2ZuLpC@G;!%wspFED%2rtI2;Bnitzh`?#!-}vMk98P(N4ylu-f<6VD_`DZ{hS|6c6ZETzhgj_3Jb9>AR}(pPi_|4DFD8Of!RF48rs@VG3Qs;j7<R-wzV826SNmO$nX_!4gFsSF?Mq4Cs?NpWT(G#YE2;GhD+JUy^l2-jbi->#)c%AO0c{G2(wj{5Iemm7QA*f>CSyA*R_m`fDY%fi!~~jy-3}&fooCNM=Xizurq`tdd(0^vOZ0tS=6J1CnO!M@Fe9Pnm?_kJ7&^^SBbz|NSz=Ufos&AM||Bd#)NGmbG8B-wmPK%FQ8-lwpTM%4e-q81yvLjbwsgrTLMenfMlCxFIJqmuDu<cFANDl;S^fEu5=~$Azi;Nbz_$#x^w&aVS0@6S0rL!O2d_0Rr+s`>-$OUVhCsNY5PtjE+?xqWOn9xzb*m?eWxg#H~GMt<<T%7!2Vj6xj>V)mV2jREi@`bL+8COfA2uq0c1Blw^UZ|0E?)-EM{R|VK#EWNVSb$j~Ngu!Jy>W;>9(6sT^AH2MbRIRht$Ce#r0uy-1Ce-KuI5Uh(AoPQEnPVQnLM$R<i*{wYPHBcpE&Comc+$G$B(+cmv&Y6r;@H*B0%jhnS}&(=_{fVklgi&W@vf;{lVwKK0>#S#RYK4{iBKk}b27swilb+?%co|RjCQp8uzqc7&WR#K;o1552VrXIge7vN2;j_m|iD6iRD%2s`rV98bASxcL9|L}c_slaE&_uTHAs*B6=9SN?d@}0k0yJP;XmPiLSwe$o;H(S5Wa}~V76rgTa@LCouXq(X4d%J?yjTO9ruHc*HyGwkoZLDt13LcP7?RysPI^?HMSZ(uq9pjDyG~<qGwIoLjY+!k?J}c9;Y+)-&`j_Hx$DXCDAlz%cX6_0ISK^l+r#e@KU#@=34LetV&J6J*4G?RSVT&x@LDPKAYD63FDSNg;_ACMu7hRWE(a`|5wJGj!dGD;Te&B3XW$JLOPSMo^{B?Es<ruaZ{6Qits;%*k<uhQXYk@8}ao>rZ7w)Iw!PbKS{E-)H{`X>a@TMp9hRsrYbi|t3?bRbFr!4qK;=Z^|R=a3txR1<9$&^?T2-|vNmxN;;hHA$&X>4)#4zW^_9^lv3e;%uCFWrU88f1dit@>zDwRSpO`A{X<xX8kZhVB>4?qpy4%?n_6M~W4BDyqz3cdPsl(or`d(UrC{*Vi*#Xydx|1?CR*eL|vH%^0!z6E4&d7a9?QS=Ig;E;Pmo7rNt!bFcC3y5ON_(0WgdaMu{pX^w=R7+v7(;%Ub;N;W!8&yI}__WVGVq_$arMQggEq^QBhvG=Ob05w`S{ILb~m~YEZKB3<=<8ipv%$sM|Aa88epcU9k$dOK}<IH<_58S%BW>y?~>*3`OPmJR_(jg>`eZy2YTXzxHva_(Aysx}F=;l<`x(k<NY<$B|;l|dbb+<ExskK-hdg|-7wv103I0*yO=Q~yxDa?x@&A~J(9C=|M{2db|N^fWL9#+%vqt3B2NCJSSko|Do-+b?F_AS@`CD3$Fx{SeW(fzocHf(^lJ^*eM2Z5B3w&>Xlf%B|g-&{=neE-%6pfR}#08Rt8!8HT%^@uoS<T`;)xeU|^+sr_x@L^(TXYlBr?(vqMQ-cVOA^WZrU%{l{R{@QNS_W~Zj#ks1ZbrA#2l=4tmFxHtN_;zu+qMOU+OlF;wxCbD|G4hAt6yK#mC)rDBzwui4SQSIG*SMM{wU7~|1J3KfO+R1y_>}xzEDP}1ezFmu<no;STz+zIs)7^8KQU`Awxt2D~b}d0$DfTwX|M{ws6z7L?xpACz|eO4yMo#9o$|TEBW0XoE3ojGVB9L09ZqR8VfhxLUE8=B+>V{!O=%!_efYpu{!MN<>CrDs7t2W!fbY7T04Tu8L{UX7<l!SfmFwGjB5*QwPIrgnto&cu{$p^FpNb#DDNU7hyp!Da|3%g=^U)+x#N4c6?-kHcBzB^T=nm|;is`O50up#e#osx`O`h33Tp+VwM-!pKJ42Q$%rsy`1*U&IH{8tImOe+-h*QXwc_G+6?`gAQ!3l+L1qCl)quNn<fsfn0YMB$a%XI}fvTO&?`@$Ky1$cbpL-n3hH3;x)s`wsq?bUfzH?1Yw}#HVC!bU2?5`(61+1hG6+sVt<yaB;V#<Vhyc3YAj{HdCcXGpHCGZ8(=4==ACQR<aUxle8g<AS9v$0W?UkJ5X@zt~Pnm3%!;^`iad5wZF_fMa_W^`*>5o2Ac4=rCt-N2r7Lm2p09Z~E5v66qt$A2aooI)T%Zmn#**b!WZp2r6w+ZZrI%4Xf6WoBrz!$V9a>lLe5P|>a7dGdeuwczQ6WG$b5%_1ceNCU1v<h^ATF}WE`R^c8IWPW{hmv<2{1Tm5*8M0V#r}>s0Vkr31LQcE3FB1$8W4NV=tjMyWfpQ|NnnX;%UD)xo`p0^65QAd+v+vPlaw4wE`c_=HgG^Nt&Ifr<myXL06KR{JS(8cjhy#osSZ^Kk=PhRBp)xP-QF^!Astf0RCTNf=jcvo&X95^8a_<|#_#wJQVDV8n9|r8!t|k`_l?_(a-Pb%jOfiq$(4!l4wSouJd5}7Edz=}qn#_}RBzhuq0_NWvXCh`j5pVqt5!V2gEa(4)k20e4Y7<6u1;!`W^=$f{+N3y;d%QBRHP4!Omjk(I*fDexM)AC7C)seWYqw(?U`qZ#qg!|IONK4RavDE$RG_yJZ&9|mEvP$mCTsjwX#7%l*^&NLU6>m%@c-Ng8b$fd7X#T{AI0qRbc;SqB%$QnPNV40htSW5&`;wRmg5&h;jn^*$WbIl_W>B?y3G>~>4fftSRCC^U=J{oiy$Q~>Z={ml+OmrrW$^t`o$0C?I+4@(rsEe{3OKcQ(<jL=Jtol?Uz4lZog9E-HzMo((R{=9~~KR5lo)H6d3c=&7+XWnATc>!7%Y)!x$!-hEBOgIz;CDXT#Towy*-O^C}+%vB4`12`*AzplIH)g0IBx&~tGY3|e*%C_DmzO3)gU@Ex81<F4rOMggb+g*`~l`Tw!|uwlCH86qX#4N3tvqEp%ukVLsnyE8@fS!p)xN;^jg+k#ptktLu7Ko42k#Gke?b|nl9gR_vFX==}Cmb5cs=ti<75fW)IR3DCXG!nB=3Mldg4sB_giWXMT83|xo@}R<KS(i(em8YJ0kkb(caBSiJs38Zj1{)c=k!_C<1J9Z$Qy_>tT9qVlsz9_wXoF?_>rjFbC$ZupPZv~Vg-dYCA6YZeI45diO-w}|v8gAW%^PV`JCQcc7@J5A44t~3(P4fXkfn*WCK|W|(K^Rr%rVQ?2oGFj(U={yL|S30%|Es`l2FAp;hm*fJ_UPI{?h;G3y^|=d~Zvi1q2n9DV($TiHU}mJtCTenHXy;YhXJz=*K}1(waq377H<h>L#Ry7)dJ3C$GuKkyz8jShCxzSITfLbo3hWlQI}18E6Ov?$re2P#2GwD<opDwxu8KE*KQaQRukDAc5#7Jbgoiu4KWLjj{eggsKE2O8p>?F`y6RblhV8I$!1;(#>cJggXoX8*54(s|iMS7uCLL?f5QKrb?`dzf<Mayxo%&r`4Dr$!x9P4AX@)aWL*#R}%(X(_$XI=<?7@pi0C@MH>INFEAJ0_1r|rw2}j*fpa0>y&t%2MM+6Y$=_oSjL1Mzs2u7CCYSOse2-J$UXqtYg=aHy06IT(t^Zo@bJY7S&VoZrx<`b$7^<!qFIlc1a7+4}V(CXTtPwoU*_5~H1CiUG=Y5ZG%RC8A(ciH;Frc}(BCefnZh%>k>y!1Ld+#4vMCx#6|9yzBhHR8Q%NY?~f+v90-GiJ3?)w@(KfWRoH{NofvdMj$W4GWAoDTWBPI-bS!r0L2YSnP!cQvVlDvzrm1Sf7T8tZCzWIipLk&@FNItlgG*{Al$hzi>|IN7_mU^1n!W@m79=()>gF?tK7u%eZL+H=EQ8{s5UFts)4;7j|GfB8&RM23D0LPP!4*{olAa)w^xFMNWKYBzI&{ItU&7G}fXN>r{U{i<~)56BEtJeY8+udH7;yFaxOoG4Wxcx?ShwM;$Y0bT}uA38^&)T0J^r`#oj7exoK3?oHHoTuXo0yuajKmzVJg?xKoc0Do*I}&|qn{&%;E`?C%Ti%P}7S{Qs@&~hUV1X!ExNMZ&PDIP}iSjgGQ!k)4i3)&I{&c=GLnLfr9_~kh#0j#Byg#5Z3-Jg$djAlZP(a+D9(^{%d1il3A~;v0JbibBv1(}*e>hrK+B&JH3j&Rry<Q*ucOTKP`gVSBB8_f^s*78k#GrxsY;UuhHh-&uD706<ss3rQ^Weuk(2u5Q+#Y!WUOiNXZ6<Uwd~-S*erCQ2yJLjtZ@$`Nc2Wbl;Cwjz9h=iz=fCl+HyN60Ik`9VX=mPKDBk21qR#xe3x^Utq%lZ`yEv2~6>HoTSF&zr)mvk|B^BPfAOeCfoYg$ikBMn4hMsPA$xYi{gg^v|Vfm3&A+luxGAx3EycgVZB^4udY;uz;DN|-Uo;bqjO|~>&pm?hneq>ktNQ$^1h^TcK|9O^c$Tw}A<nk#y9VT~;s?Ao&kHpztc$1wupbLkx20O12BeiUJg3ddKaa$~NIxEX^_r{N!inB0T^US#25n>#8&7uB3KK(4qKcy+NjH#-ks{Q0FgOeCy_vL08?&*h^Wh^Lus9DyPS=Ki2Cdh<0O)kVxWpW8V;@TI?tl*U%X&ZFSk<FR3vhA|ePygb)+8@c~f3w>1(PNW;?Y&bTZ3Pbf_uB25^6;}V=S99_V)@PvePrn*Rr5>-n#%o@<}iv6Wjg$r=_qq8UQ2U$r8&Bi<3It((j4I;&Ee$yA8kR5X^yZ=b7Vhs=PfN#Gt=Q$<Wr3^vb8O5tfe`4tMB+(hT!q{KepBItcfm7Mi`SF?`1VW6#t{KH!bp4m71Tvu+`9E?SSuk%4BFi0?haYR)efz3#-A2+K?5fdD?1VoJSP_6BYP`h6BmEUw!W|;Xq2L%Uo%(8eOp(Zk(HBte=u^9)Mdv1qj-xiObxRfkd;90No_RF<@R0XgY=oj1hX$F4r;~&Ygz|6&=)x6*yb`*v;6YB5vS3SbzmdQ=|Ypk^mj*+1*)!1+qZKIgz<FJhwo>gR?KRW>3T5w*nfWFNbA^S;=0(LbPCk+0(&7)iGqiJpEMz!3Ki4W(Zh99@y4#hJZa<f<I~v-x*(zf2<a2R30=p$Y`6rMGgq1NHXu_kiB6q2Fk~XZP|BANTSFZK-ofi?;M}EvyR^=bO|WqQIo3G1G-{SUIBSB(w9=tM+G{rL=+FJ-bmvvv3~>*Vi0$g!a5so*`J=n2Nke`5hppO#Ax=^OsJ+_KBnSRfMMr?A9X3~u}7Z0Uf6+ZjvAR*kpC31l{ao}Z@_;3kj@o_z2N@OKfsP-P3?d$vjw1w_JcT%Wkf&FF7TE3j?tJ}rd@zhZ_~VB7r;<2c7abz<$^E$p8E~9EikPS09Xk_1QkAestr@zGZovQ54<}1_$S&h01k{g{m|h4teACPdADki&u(jwbqyh8Z+WQm&Ii*eBbC?0kB$2ai-X!?^46N?FCdJL=CO$!@+c$e>VUE)FhW(d#z@-O;J*v<3G1>7!2pr@>jx|xZZ6*ckenk?QX=T5%!Uo<IRb-_ZFgXrt5}_swyZk(BTpFYoTN7H8~m<7ra1~{VI`@DDH1o?L(vH%9gDVU5D7%2(~PQC7#eWfsc(q{BDe*|K>yNvA;H-yg!<`5Tp?6DYX}<>!juGQ{@aC~Pa7GVU$C~`vDq}o$F+_psjXxSf|`nm(j>u``0}_`uzWEB??l{91}(1ad~;(<nUBWDcfH?6s~Pq|<|^Ddb^<ivr`hmg1tT8}bIbXhxVlmuf0~@0UvtKh=Qsh>1+DdsjvHm?RwyC<gs;|YNM)-uagj9LcQE<DavZJlQCXvn=vvsWgiRzr2>5|1#CK*#k;5KD<r;{ZH(NEXIey(&vGRWLrKBW#k;jGR&P*iiU<@m?D}~J+dIs`@-JN8+!=0s>M9>{H0qKE>uO#&QYzo7kwSgTE&Uf@qic8vWT*v`e_M5xf1ab#Z%!huhn7-m9<_-6Fy}iRMZoTmg<+*duI?mx}$`G#f$mDN_*Kza@SVpJ;^k_0?2UW%03mDn3*)#a6^F|Yfb>VBrU;PTWU_;)uNKL%uyh|wzJ?0D8x>^yVgbh2-ahV4Vg`|m>_u=QO--Nwb{jeIo?o6R~vp~rs27L^D6(0|yiZgvyWTJqWhey(4e+~~}*j0TSdZc3k^lX_=^=LoCYRL;@So?Mr2IfNZuOEmC*teLS!+<@`w`vwccCn9s)dJrF?gv_gymOt_j;ajUx%{ze@xbr0k=>094X)@?gVM0y;bIQ6{_bofhQWyVNk<XXuTj_!Ld%ade9N<y3Kuhgf+W9^*fXU20C#tVQB8U(;hx`G0D!;l+Q%0ND7~devzjo#1|gNe$m$$_v8pACu`E55?)kvxR9_$~Zj??kfedSN@e)m%so^kdz(yR(F15y~s@^NEvB7*FiI#QjYF@LID!<rA`M4;5=jo*8RH7P)K&^SIn!Y24HYBfB``9{TYogyI5?aTsl$bre6EfbLC?*>SH|h!Ak$GZdASH7LNgaTGl6q30dI<LP0R)LsaUA8^0gJ0yKLEvDMUWy#@jqBVc^}xyEsB^oGk%zwbe}P#w<tR1#{&ahlhh@dB_!B7teHbz_?r+V5gz@Pyx;)nif9@VpLlbi1`K6_u^oUNXYdkS%ez_AxT4+Z{Y>8&GX?9RQhEAuuq6>&{@f_;a2||Fk0WCoX=EAY43%xHghomJB;xh}DTC`IDH2W#`y(}Sn;>8$cj`eC9hX<-B}Cf>c|vyj894^7makX64kn*E=`b|~JeknEsg8PII_3iMmq1LSL<|^fU{ic$zr>j~ACG4RC@+P&Y?zX<_VxgS+UIv`U~LjqFk}w=_P_rkI%t=5#Ipo}z&gv!;;I(m@yN07(yY>5hZ|~WflaN!3IS&Ui}pQ9fDq2WE^^j_6^sa*05)$yXDl&M@{S}PD2;EW;^=1jXfmf=$#K_XSWKvt*c{2i3%#KrXf)z!qj^zptuhPX=oOcsE3&kqw5m~mEssf#J8Cl!RPYOekkt7)8!#n~^^qj4l(n_3c~TcXODgF<c|PiI-?TMnbX0I9U~ZbvDwdjEA?V8nmZoPA>x>(vy}h>vggm(^6N4ouisEc#vOQ{Lk7~cq|5*jo`ensh-Z+O|{=sOQDx-Rl{uR|@@;BVe=y0N`@PR}@Gz65Q1YQpo|Au$_bLx`1Vy#+zbv_F0T_CpAN%An<iRVGM$-G1C$Vyg?^2wtXa-I_v#hCF$Z4EoM>e#0nS?QMEI>P}po-7oaVG&wG9eJ?@#+pA6K`~#aL6Pm_0_MW1Ci7H#>9kgAS|>RJf3y!BA=|)#HrlO>3=O_oE3pZ#r=UGI^uY>@+0rEtuUFbyJcVDg-{k(UuQu}n^3kuRFbw}8#Q5bhF9WB{hseA@;LClOw9C9O+=eTem)bHf#8k$@LquiE_oxcTl7C?w+JqP6UohZ{{LA)}m+$`N>fdq0pQs)m8F@Agadw0aJch?dNq~jTeGow%5S%A<!~q-fIisllp20SwH?dj`Xzz`~eFY{%fnC6G8B<<$D|o^A^}`9Ps5KrZ9I!h={!FEFCEte=Sr-}jC}P`ekr{94*S4Oo+$$`qlIT-OP+3=Un8W~x6ZR(~jLK8#yL@rCgAQO+Lw6Bb^5qOMvSXxNVFKAh_RnHE%BOU1xCs`f+>n24w1U2c@yCrbhH;vcJha_kF=LTq@3&tL9=;{uYgY0wb0B`h;MOdE#zhKtER@<v02NM;o~wOUEA5CVu9?ja@>$@Nwk$N&rq}7Cp~6d{6l)us!Bp}XMO=ZlK(Gkpoq`c^>L<$2I)&mS7FrD?BBev!82+~OhIRxM=F5&)hmp#0ZR78(6b8>ng4&xfTX;J!MpEV0+LN@>Lj23`p92A;I-g^87ud0)fRhV`*#>0^j^MFG_F#RoZWQ7+<(A2{Vlp9*O&6F63+p{JpXy3f>q@6#MzUqg9~&e+PJ4(mX`+icIB(#+^Y<quH<UMGvgH^=Xj0qPdCb(2FWCrEl@tuCHG+H@H#X=|hjPyaMoYE!08~fvWH!7E1mR-;@uAsc=8%a$7$+20QFowBi@PviUvsxuKUY*oZ}X6&Rmwaqq56?6U6O#Zhi#&cM9m8_krCao=p*!KU_(~qv1Zyu?h)l;oi~OT_WT=jlhJ+z^E~A7AVh0?UkA2<@jR9y3?dL+X+bi`7WpO2b`pnS7(Bb=C0ix;DEhI{eC9CaFU7(2h)*;H1;aJ78*a`tS*}5Z<3`?D*|m-QpbjZ=D=)PLNtcbDuO`88`FZ*LjZsZmxoIw79wrE$iLr>I5<q85nCdP}BIMTa8BC45@<wiI9j0?|pDQBggnz_QHN6^13k$22S6n;HPit3IF1`>U+Q0GSm8eO}Q&r)dNuZZ6qOiFS8$!s$<KS5+RsPQ{4jx_la<d8?camWr_1jHuJp^lk_P#Ehqrt9uapv>CZuV5aFANjWR~Y`j_LTHhmj2q?4rrd68>ERsdSCR%7eywfCHf->{Sg-4XL?UqVwl4c>-Tm&+v0kjK%)PFYJG`<Ed}urOD|O3hzBAN$=D4(rtYGpCC*w}kanx(bmB5TvAg+aKn|(C-XHSnv;laqQ!~yc6j}eU|AtPqF^L;iHf4u=L*mFMk308BoF#Ya$jsLYXEJQF)SOWD>}iI)VoLUV@6ct)djdCvH3-xrP#p-^juU5`7e=G?Ea2xYBA<$?ei1P-@23MSElM$n3R604XN=Gw*kXz;(P;qO6UkBYIB~$ST<0T~ca6jHf`*&+5YUgYMFdO>;==#?rFz@`fA-!j)V6I+59;mGTW`IOJ}z_2F)w@Vea_icsXBE$Ri``_Mt#^%iV!eQ=Aj-80R@SI2??Ymb<_$~XjJMUmZ?}}UNmT__#%ix-s&L;UZN;!qT&TagpdRUpL`M9_kDlsmvNbEuC>?RYg3$k7W0fb<`{kS(R;i6m+t~r(3j)3L3@DW+3(D46DP64^mc6NoHN|$0I?>yX$cs!l`}K>L*lS$hUXarc7^Ar*NkVYfCD-Boa#n=a=1culOO>CuB|EpH%M;Xn&g%$$!)Z?z+iyM7;a7=kDDYn2?m*~ty0EC4%#nBZo!Qm88Q9}&n=$u+#pF*scy7fVu)@$w~x6x{OT$h9T{71E|SrE<ZW5W=slrGj$#ZlG2pKQ*E;AooVX=<9uTi#!djkx2(6hOSfns8XH5r$w^9>KOl=NZc0iJX@A`UYZ#kYUVYSK;l_YleM&GJuB~c5W(xat}qAHgo>`$6`T=~82@Y_eQe__D)gm2Bjhb{*v`+|TNP%^{wYo-T<^)Z<Rz2t;rI*Je@`xg}JOP<;?`j>md@mTw2%qtLU|I4<%Y&er{LGy%GNHtF_dE53{o=U-}&|OPalhrAAt<~J)64MKTj76}pmtUq81&3HuRY8BEdT2FO%|L~rcF(0gl7$G9GkV^YX^{N2B$buu*r8y#1m*R__lZ}CtY<g#RySQWZ@S>_NDi;<fEAMnZ)*K1&-J3s+I93qBBJ=rhbUd|KnGQnKfjm|0lzb+t>WQ-Y9#z;sdcms@Gf25S98;UhJI9_DoEK8jwhFQDDv)UE_>wCJ(3TGt)T@kw7d-3O`SYLfrHF<jp8{;!F$t&;Y}urHBi%lMkthf9C(d^cP4q9PIfS`G<`?BewP-ugeb~FsSDD4l1Jbbrm+KlRU3c9LC5vh)9XcgiwLmp(J`U46vUgM*Tr%!gD{zJIC8W&*N0$<Qjkb5p*ew~<+|-<C~X|IHkEjg3yUqFMUBIGV{lQD8;kZp5!gQXPuN8kRW#9ahCLVagXTl_T$~vrI8XFql7%0Jv}`=oe8Kt*tVY|q_IrRQVe1~S^W)1T&3F5E)B|Wygc9%hyP)<CPP(Ns9zl(mqS@kJ)Yb1RJVGJ(5oiX)t_SYG1jm=D=veE{RN2e;bYL$M4_hXvie5G@z-1%pYv96|oO%Z|_G!wwm$1eO6vDS-DM3>}Jxi&vm0&xL?4e@e=)@q#R39i*FjBP@(}V6Akyr-#K)Ah?5{cu6ZdH4vi({j<B3k(l?9#wCXD~isdHxR5_)dDWdS<NtKvXjDf2jF4U7Owhhrq!eMiwJ{{aKFu^KO&@(=(x4&zM~$<`7`jbS)tR4sP9kOQ386zq~R)Po%2#5{!Dnc-@yL6OSDE5&9HI2ph-rVT(%!u_i=3i17A&`*=U$3m|+|4qFcO$=0+&M#+nCTx9-f_hc{rOqESZQBj_~KQ*eo_JpaF0OR{yzkiZloro26fmA7LRoxlDoGu%)v6dx1jCNNO@8Bt{3x-YW_{?<vo(3#vkcSf8%ghFXJP+(+(3{6~=$7A2(x4vLmGbb!$cBPxcmZ1o7&l0P9(dczr8-FJIE-dO3H(WU<|pD*B_Pg(=P(@no_uT26wAQ7FX34rLfQBAOJTl8z-&MS2J{87OOkq;g$P(Q#t>AHg<EjfXl|HGZ5dSm=!<=$<rd4FJuMRUq>a{KZws}$@}<=iBB!M_EP?h^G#D!@HXMwjmN+j3lTeE7JL0rxC+8XT^-m_<&}Zx?p6se!$q$~e(j%nlq<O~itx4@rxb&^8P;m}D))u@t9^t&o?x#Cam>^kwC=85JppVyC_K^SJS9_7Riz}2Cm#2)y9SahHce?CaISkL`N|X&L^c%pT$|eJSUR2q9i=lu3Ej}@#Z2jRB(w%v0C6a&qgYU%XFYzU<EU*@LWt$247eDZ~EdRcXZTB<UqO2-1W&i438Vs34kbXdOpZZfJ)G3)CHtCKJP6nWXL21UYC_nw4dT949qAu#&ta)p>Onfrv{h{nw`x<mYi^qavAo@|Fh0vX_TY>i*MaVz(fiFV^t*2$#s<#UR5?Xt9ZTQ|<YY6Y{piXS=XUX7OxHdLfSc%U{4G)|e&iV^wtQ<LpHET$jz#H=h@!ydXXXtqGIB|lu-Nt}k@r0@rw(0UEz)5DFSDq0(vEdl41)t5yn1G|R2(mAOjIm=mCDonspZp4@(&eSKwI{9Dp0HedESR4zCnZ~Jg>Qnw0Ry*_=OFX>)@t-vhgPJ#0D)P?(!9q0K==SqF9YCSV`q)v4pEOM!i+_mLm9LxwjmaHc&v{P3~D%S?E()?`MA3nWaftaaI5PY@}KxxhwRy0PUnL)Tpz6Kt6L3Et`6CQtKE3kETa~B4%uBDvaE~{=Sf^!R366hIxY8`6MLpdV22Vwo9;l=QMucBV0l3hsbDG2JWM}r{=x^Kg}s$eO5bj^KF`!6+*&;%brSGvOk<t_hCrQR;)k*JY#1*p>A4Ezq68EKt{3!DKHo_vWgf{!5o1Pzg;f$-{hA*}IoO#ZMx%o~@_bk|Q_FN}kSJ;vZcL4?N%Xj52P}wx4g*5`wY!77M0Ij1w|thDKz;h&g0s6tk;wBROpGzCd4INKEJ^w1ccJN)-XLSiDUw$}?eB7<zOBuLs&M5}Z4sJFv*)y_{sA#qi-aK)bUH+w3XQo$L9C*Q6<W+pl+UO{()nYV`W;3JJPlX?dLC6kVRt+uOC2f}W2fTLgBO?`Z5k%@56C5OG{6-Q-}sSI#z$&M@c#I1A_zGUm1%S?YI1g}v+&bTLZbuig^fcaKTB_yh67&oI1hhH%8=6FzFZk76&;zvL7;JLgg6rhBaO8rM5(8~8Z^QY@gxJ#;D6&5i|?k7#Tkn)5z|K^Uw9@geKN6NBc5_QfeQ=)6nkW9NlmspU<n4KV`8!p)kIKX(3%AqWEN9F|8Jb86DplFx-i_h%&{XoO<q(H=}57l?*^{pD6pe$R4tEMNLGO;7pV6U?B-xg=mI2moFUBwMRr43AA&U&tVGJGYo2Tk;biE1M-}y)F+QBRR;WA5UcSL3uy%T}1l1G8eGV<rdWL`Y<ozYutT><zw08Jk`;ur8!?TqCxLJ1tz}GW7mP>y*6RjRgPQ5={0}qW9x%}kH5*o7+x&;-<P0Jm~M3m#?=+Fq1<-_$79GdJDSk1(e_5)Of<yJ&Km6yczW<zHXqt%<KlK!Dc&?B2b_Syp}BaU3T4G)`D&23=*VM|HX2kYbowuFkjyQt%>YAEeVUr;!3^dFYOfqR>xqkn~>W3Gyhf*c2WC9iKwRdkFrGF$CPrt27%qV8GgFr64Ec+j#k+NoNkn=?|Ytg~hZb@Kt2TT43{V7QMoE}BIhU63z*GmARzbszrk_ko00<+CeyBdgxM28IjMqk96xw3Q6m>=GP<q0NF(-rquq_gt{#H?(YXU8pz)I*R04BA}(`gtp|2LhrC)FVc&ZcGl+dOKG&w=&#ol9m`Oeb<x-eShl$kDz-o`;p(-XwQs4TU39uyg&>KwPw=&|7RC!vM`yr5js?Tk)amN2P!4*=O@T*40!oO!oZQq9w@8KC>n1HU9&g#C1Xk7E)D1@xzWcZh@jtin=6Fq?MJs$c+q-kKg7bcDZ%vj!U3y6gCr0lhGqPc^!k3IJT70WTkK`e!F{{YhsJkITl8g(m!gC*%{y}bxhR-;Y>pWIkKA)g)5@cV10cN_1StwuP(2a(pLn+qnstpfa$Wk^g-aye`+^%*uF2Ir$mbR(BHFABBLld@@9+JHstNcXkv5L{4k{#vcL{JsIim8i$o_A>P@O7vI=khPZ+olBgKUjF%fFW>B*-Ou%1hY?!mx)sVku@q>D=Xd!tymm5RN=Ide66zYovO<*&x@T07Sj(P{YJ8+0+IS%W9!jK<Pt5gh>mLfvuu!2ar4HQb6iflhU)&Fpmx+JapaAu-DH}Gf{2y<XCoa+iNQf&ya`kPBJ7bnWKoxR@-h1!D+kjzPPXn)$w2H)gXV(jyzje-!$|Jlwo$>KN_mE+^yCyEi23z0H?nYoQ`8D6X}YDyl2Kru90P0}o@wq-o;)y`MfiF|M+F$J4tC_gH6Ima1BV=puxzH6gTQA;FMdp<+U-DkUC$PfENzHel!H0;pk7wPy*IQy3%yAuS590nsy}p%=vQV!2e(QuP2Dp2A{$K6c%2ZNRCpXIL?J?z%ugst0(GHKoz%<Yj;SeG(H!}K3iD1}heqehj*slhOwhjE{C;mf>`_rQW!FI<V_+A_EfI{AXf>0mN1{OxA1Q>c-MCkJxa0Pg348A3&cwDP9ENBtm#nN>)bgiQjAK`a3__!)Q6@gfa)O^5Y4E`D%g6|O7YUJu8Z_-efHD&|v68(w6?Q5cy{UQ}lWDYBbuK)<{lpYu)sHVrO4VG2U^X>t6(hyDC4kS($C;i9KXlcHeG*1V?1;?ZMOtC_YQJM9>62r-ne=ixxdj;1ur|7?Gh(u$FslJQpR9fDXa?@4M`WgpY<@`Kq(TnE?7&`4Nn5}Ebaqgj0eTF7IejDJ*iF9kh88tu+5$o<2^;&B6seLVO;+zX=cA!aXUuDF`CUB|x5lT|3us4}P_50v&A~2dMF!KFuKevFx=>iSt6oFCMrUBn0T(4a|NC8I23^c3qgYAx!P)aa{`LKS{qgnus(=0Q75?!R{=M<*k1xfKFY?Fv)qj{@{repuy~|(IS90cG_SdiDPWc}X)UWBnrVsZ)>BkrLUEUjC{PmsQ`+GdCSU=;x+^_xv{hD6=tA{>o^}T6Sy_wG{^VjLG?j3$zJ$A2p9EA`ImG%-|^RrP^;_S)55|+K7ef`lScX;Jz^>K7lvB3%(!I{H%sDSNBwTc@tK!1Ad&;J>CK>ymQ>O*-1T#XGIj{{^@IuvXGBs3LS;=d!Uji~R${;&*Jg9+LReIm?7Yjq|=7l_|17;3Nws>euz&i?uNpFzs}`I9)pMv7DAff1lq@A9j6o&9?Gf~(Ke$83A&^#R@D*J~$#e%j7eh=nt!S9u0ScE2PsNf!2W^_EvMxO#@uGwU;)@V(QM_I2usaSn=0-khImd;Z?(69dV}&fCEDy9!Iradk4&i<f8XZa;Hz%_(3nJ=67Fc=6Ze<y~AKFMPGDlx^p0t!~e?Wl_~^R*y{tRjO$!6HX#(^7OHvaq*b1;TM^I<+rf+PLD5tHn0CvzW%bSZ}DgE4fa=7F`KjRf)&7Dd0s!8_dWTu3-WG%4Ojk3qT1rg^-22mS3CRFK5_Z&@=JfcIsm3~Gf_Q8IJR5q8E3aXR`u&yfv-M!<$(2DU-?om-WTWUj#Hnk_t)DrzxCc14?Dl{#wA)le&JKjuIF^!oPA{pyEoItnXl5~BEK*brzf4Ak24(xYwg=lUl&p=1*<0aztH^CArAqx*#~qf#!o>3Fs$4&n9=zG-EOu|shoKai2U)9a;`oc!1@e_qtTRn3sdf+3p?;G<LJ#5PinJ0Uvqr0#)F9oa3vnljI{+@2Hm^L70uJZqX?nXpMdn(iJr-B(dZ$1(cgPD<7g@#PA8LvEw6c2kC(vW;ZzSxJtTR|gIRa9#?uITTsS>7Vpo+T963VMz3siesv>x3?5fj?$Gc-=f0|zA)i{M1lH;G)9RXTdX66F?g4_HTo4-Jhd$m>HxbiYwsu)uX0^u+*$$GNvJJ7#6MoFDW;CC+Gl~?nx<rAK)f9z>_>h}`kHA81dOy9tU*Z}Mn5F%sM^T<7T1!Pl0EH=}4p?sku0exy?vJXg5yg&nVNWk}N?HSK*jx%I}F}ID27EMqL;S<CbxHP~p4$l}6mJ^}|ZPPRLXEnQzeC+CL)Wf3vU^8_LZElr-%u^wbuDR6oX#_i@+%2bz&fHa$Ab~bX&$qB)_R*Zn)G6anejN&R<24Da0w4{4_zpeT9u3%$RIEuzhjMnj|0M*?VI=1ahwJR3+MKDKSb67oKef^<?vN9vDF98~Fd8E!YnCzu8KnK<<iH~;D3K{RXqSBIFwjR*xU;t_ZE<wqJ)k@T+r{+y4)W1v&~C`0#qHD#ac*9w6!l3|SMpN)xlw;JESiVagETQ3|H6fyuTTe=`l+)JO*L}xb^>MsQ9lcseB>{)t?s9{7?`<!mah#@fRs#cM}gu4q<iq7ccBW!ND!h%Wr_faKesy~>8)VVU<^&|ky^vky0XhQtVer%5l?cg%n~$Io@q6&DZ}lYX)DbSmd#;&eY&Ud`$ApELPstD!8>a&JIi03^}3sB=FNvnu6~di!_I0*)@Jv!Adjz?)K6E~1S0hX^?G<p`zp0Gy{6v5b?bf}Li6)XD#0;Ga<t*kzYo4P-L%4f!jW{MtO*uPtav%_L77x--0_W)S&myn%L!HukkOl%b|uFJR2%q)Q`vRwudxU2E;D7!Mv?*aA&zuqp@Bjoa3zD&)ev^rNVF)^FuLu5*#!-|r)CxHJLn0I7j%MlmzmLO22)FeXc@27na7NBM5X^;r0p(o9Kd_^q*g-}1z6NZdUTE_7AfrA@_=56UTivvyy@G~<bvIIY8|_}5J%G4`54smAggYC-?VY&;6uDhN3VH&K@fO|Fk>d}srBstV)I+heIGd80RSbU<|s6R6BLW8d<|f?o8gXp1{%GV#hD9D5G-_aFX0CUFB`6^U1+1U;Bbz8>m`XOA!GvB1>t1Wu)~tpYS@!oL2M~JMH5v{qOD)}h*5!wVd0TxaYIqXN9bEXu4A+@OkG#tm=xxe`}{`lJ$NZ$cu{ku9S67=EtnnfNr3Q0&_J}g|3m|@KDSyZSYnt3P(lLdfgE%2dH{j}qWn(8uizdrcEsp_Qh1QGR<bgpHeqv1#$kJa(g(sd37kiSlLa-#{E>KF@O!)Xp~^Ml=er2_HV8?(rC#`0w<pTiCO~1Uf^~^dThk72K^_jGmIw|Hy7)#?vq7l>=;d{7Z><VM@s21IA-@?INYv_Wo3`_PN2^~Iy9l*bWrN&6?1Rrzdpj6`OM(+VnmAi4Xbr{7={SP-?zQ`Leq#K9RnJK!CGT3=io_^F;WoD*>I29t0uBI&O4Tj451nCKNMjWV%${jym0rbYf>4o$p=>Bu#a^;>D1laPc~G=y@q?EZ1Qq0=%!#RBxHe(o{QPxne^0Y$uYQt941z@_2L`K~0#4aXDLQt><KC3ts&$fM;Q8r?mrzSf_3@WAeA9~pzDsQRHc)ciDmsuIbUs$!L0OoEg%WwyPot4p)$k3b;Y(>MF6Ox|Lsh`n^wT;4c^y;=*ZOI=tNpl??j^35b6W1^lu)bsX?a4D<7F+u<gQBhMtFpU4CNQDTx$t6%DZx-zzk~4{w!AK?JFv3p{&|5n*2%`-96=zq@w1ziHsXXf545uq@vb0nPamzoh0lb6*o?iuaBXY6#vLOxjAQu7sSVVCfRhO-$b}Mdy={yTQ^DwWW;7?vbKz{%h=rA`|mM{bdOXSb-MgvIA|#@K?%O}cgui2nR5<b<MSSy!W*nde9O_)P0Ky~o^~Ic1N2-1Yn`7&cm`p-JLpl2M0)-ZT9e*CL6A4&c?7kGXZKSNl!FS?%_wL7P;Q#2Rx$mV_my`AgLQL9=_OgvJOt(Q*>J=7@Zo;)w+SXc>EuF!t9a1!PuQ-@AP)BobS8aP2aa;2&U^VfOmiGf2Fv(v@*QB=nXA-ET45)={f_AYGNY5!Ud07A?;5dAdA6>^kZ(fR@}2-K-MFnp3_X_jbXSH<gXP-6YkqiWylE-h?i%;lx~Veap2;LH#~d4pGvYX`x!|j%JvN(I%i5~}`nOiZ=uf#7UtLsvGr9|R*iBRE(QA?e=+P#SIP)Aj^8SL`fz2Xc4%3q|KAYzagcuT+Q1Vbl2?8evlLQ5jB1}so3*;R`tmc{yDiuy#IZ~xzx!yAh6-f}8blaHSJO>514aR&UH>X-UAl5y|9G&?-s1dUJ;AU!-4TASu>0WUa&Bo(ZnL{y<8Bj#?K(g|Ju&>=j*zv{$<fs8SwTHzAS$tv{Frn$Bv?Hn7XpKa(bm3+*(zqk}DwW+DMwYtMR-o&s`8^3;LFj>1tbtNYuh&K&Ke|}upT54prYV$E8HKa-8G3Awk5oc}^f}kkXWX14ncd~i_R8gzNwN_Yd@#WdGAJ?kl7fBw`+XVY7mS2E{CpHCHe<}<pFDg#8Nwz?i!)66N6+%n5^Vgbs~?IAoh2Zv_hMj?NV`|>jmJU5Y@mUYljL4JZfKxD?_<=i9^I47&Y#@hp#Y97Ww&)F(3a!o(fy3+fFNBhXP&7D@N-BRL8n1%|F=KZdXd^!EEb6Toa7dl%S6Xz!qsKMUoI12xj=|LDE6I+MThHagnT%#Otgz-qO)Z}vY8CyV=Y!rD}_w5g9Y1KFM<W_jOt#!Ui3HD3q#GjYfDC$mkgYI`SkAAl0hvwE*Xs!!Qx`o*ffxc3EWIyvt;B-;s3}>#-D%ZH1rJwh{r9%fnMe4+8y=6O+*zAtiD;s9klwO8Xkv`d)&0$K7feSP3|x?%S7GWKW3U=MqeU%XtJDTmiNfXItnGSQ5hLE)5Zl^SWr=V@7(ibn^KPbBwT|xV-@=L?P~fc9Ryij!I!h#>>m4<Gl69ulVuIHPH@0z@COJjgxXDtbIuo-baD~F`Ii;-&`i}t3iU~NYbxOP^lgddB$+tSJGo4aM4&~K%m&LJBjuglKlipZs4hSqilQ^qdt(6*79f^5)X4Hi%!KPI7-<_%>n^A{h=!Mj5O-dRq*y;Y2p*V6T#MV7C~hfzOH@}jCPly&1HKb;O==MbdKzYNh_z%G=mEi8WP<LYc|eMntR^X<09qiAF!)m?D335$0F%7t)>7{c;us=(-(hLpvs(V(Xe+z3`V2^78)!$8V(AnL=L3YWPLYD&3uz*0MdV-l23>fDk8i#9eMO!`xi??C{O$Vk!@(`Fk9hm?=jqySFo9Y(U+<j@huCy2AVUw4Ux!zEV^>;hW5_$GvviS$cw1fLbM2=Ob%7sCGV#7+n#Is7m$tSw)h3BsT+v8XeqB_B$}!JZRCXjC>6XwW<0zN1Sb6b@Y9YfQDIcwSK5iO=33R-!0kZ9}gGw1LYTpbUPlH2W<czyrlT(#%+d{}Ef4lkJSL+ch!j)SVb%|T&M(R&<xPpHP>fz?67$qlp?o#KP8*xiZW8I;tTmLLTAZx(cu8wXup4-E2=~b6a3&4!(+Nw2xU=y)Qtg(u!lI1?3aI=V2JWEk&Qjlm(01Bkx){0gXh+tiwz1hehq}+sk4MGkQ|L7$WD^g@b#cPm-EiK{~p=4}hj93aPZy26MvVYA(9W2rS-5J){p>%<YB;7O@K?s#lh>oMP)9IG7KyM?1p~!`;Q%8i}V6H&P8;&dfA!zdad^3LgdVQi-eIkPUj8XFm)nD0~O~+=xqgrv2P6`F8Kr5y?QEEWiPcC&{n?wmV;t>t_9jEY6;(me<B-xIP<&Ijv(_fL<fRD~(#viv7S)~~8P~O<mE{T`q{;7e~_9Hg;62_*zlSu4PHrb8bll*RIa><c)Ecvnc7XPm=C1Jl;&*vox`}SoC`x27S+VtHd>@UQq*UI&msvag=A56A>(xb=KO7SJldR1OGx1B3G`NuMW@K*%uS#V{^J4|k9H#F-#bwMW0dUvkjA>qnuPV2?az9Cp&>#qqFJSvP%YV|GNDA^a)%gdCQMLX7l_2EpgexX(`)TPP(G;7WJ&X=U_>voP@n_Bz;7>V@An{dLS9HimVP|BC>L6irMvaU5JBPw;nq#}E>wh+!ae#WtLK%e3edE^7#vks;pk2))_{kLLsjA&*e@hmUcdr81&!WF*5btDpyG-gg_nz(9Ez~Kqj6Zq?{ysY=cRU<PkfBhDOew*<Q$#Tb08Be_a8ug)3cP>7&MD;+GJIb|`kK5=$hKG9Z%tJdJ%5QdOgdl{6%YXMF_fn}zT-{3%qroOFwI+;`&#Hy(4Kbg(k!nQ7rYg}_cZk{ab=pYRj;}k`Y}4(H)YXkNX(NrZXwPtKBb^*yxsjrgE$NevisM8e&--UN+s*m@8R4brrB_Iap2mtqm)j=y?VYrR{mXkM<?mnKFyp*i9zJ^3{!1q8@^h4c`W7eTQ1ah%VVCd>VBqtC<4d7AuNQ_S&>7HCY>$L;aGqr9O+%c7(xU^#1O)v-(3boGk}Ht)!nzQ+Hxc9DSuK1XLz(cBNFAzf@Mn=y(+rcL%oZJ0ni{#B;>po~7?NbpEEAO{smY_JnZcCH>@it#W+_4SqiB}kz7~L)1(>9d`l}dxnSEcXQc+m~BVzAifi%guNcjo*$zS_0(|gkOOs|;U9&nayMYdVw_xkkaW|emhC+8wae&yWeg+ga|HNC5wb3*()mHz$t^u|Y*p&{R?aCLf{VLVmTT0$nLAlYU({Y$6|I;gDIIe~k6KSA=$VaIyyM8QUG+!%0in&Dii2U~_Z+V1WaVq3X4-L5d1onD$d2f8FJN^>9I>GV79Hwk27nX+8A(S@<>gv28SI#-lyykP}*gicL!^6~d)*ys^O0auN3e>QBSY|56_A>hv~LZWRz(+tiVTon|?m(l&xQ#{WkTEcW?jmU)6rcGq17uj=%46OzHjsLsLxG*kDG^yF(|DF!Yl2ocvIBSmI<qSrOBVt5&{{?0f-6}YKzkq$B&z*u@)QwwdiistoE<X!(jD2}PVjhPMqEk|=q^K(9ii~m-MUKiC|ALSTXOh&^J)sIu$q`2ShX}Y80%e`$TTM&r^8Xz-+%nvDjGKv4M~D%l;W+50<$p37r~v&hK^MxqxCJ|C{Xm8cA!&56O8U?S&V9j&A;~ixP^zJsaFQ=@4WY}$S~w(ZHn2|#s)Co<^~K=#u^ANy2ZB1_$sT@zup<k6sb~E&jD5?kLHD4Izkp9|J{1p-fY`PIf^txo7#~)?#rJ%(ZD{UdLZg@~5T!&+)*Q-w5^bkE&u&dgb%`y)TZBD0mdA9hEF0AqhA=7HF~ly*SNp<BO=><@3mH843MSdFzfQOL=KAjD@QsiSuJ3V!BxG9Cm0Ykv>e{LN(VmMo`x>lCd2#X#YNvJluv)}J4baL=I*ZQG^@HKrEQ=W#js=BdlV@O_qp+TPUz-7@zYM-imJ2v9Eq~l_8FP8KZ&1`$l80Ns2Oc1p$5F$fnAf&JNVxV4rhGLI^0RZ$B+G1e3cqglT905>#Dkn*f`1M}_0~!|+PAR1wI`$jO2Li1rubsAFJ!WUC+`EneO@ACJCaR~C>=Jw`Xe9U;~a!HOvEsz9sCobp%<7q@M|Mqc%-OrBWy6<zNe)k++tWD6@sp;1t)PW9_`a*lPclRl&QMgI0jrMD;H(WbqMM@W!rs1q^U>WREMx&pbqnxzOMj7%CaS217(ilAiwMsto+5TbFAFMbW;0F92MuJ+P@>Xh1H9``k4s>1zV8+rTN$4wUR4FJ^ew<hmw`2M9&|=ddv@oVrt)U?ygCnA(COc2eqK2z8{6pBxjEhH5fN7)kWJ0V=NDN+#PunX)3DY2CwgAqFP|Ac<U&ldBO#p09h=UxU8lo4zIM5N;>H(sxBybSJoQXsS|rw=tb%$w~2O7z~AzfULl4#;3aD34UA2PU?QTSDwTPiN$owF?wg!!iF;_p==D$srFo#Spn7R_k-}TPPJd+ch$+~p>(i(@jg4u~b#+I|3LC5?gwbA1a<F=@G`T8)Ah4`~3rYm?5;E7k{(%2TH?A=j2;E}{$Z7l}ztL%bhe-zS5p{a;fNp`@Pf0a#@EMZ!rP<i?ZnivrFTzUDL`FvTz*N^&kKc|HEv2=+t+4bWok?A`T!dd*VIeY_3A8t^EzRk{ID^d|PNv7H3A1^m-3V?6#W}alAh4ob7rO?+@>we(PVp{=!<~_|9sQ}F8vi*<6~d=&mH3ncK5_|d!X1jD9w;(_6NnymQKbstJ4+1mc#mr{TECp_ne{*ALFFxPW^Mp#Yi2pz3HU|gM8-G~pY~bq$Pu33NglwI`?QZhMTW1rr~P1g_9^V42ygU~^rycPXSX|ACaESzQA+^cnbV=38(2)Gg1HKuMx63+{{wEpDV)X3548Aln}&!rQ|&8r=D^14u5$+8O+0=>6SouM(VgkS5|Qr>s)4SImqk5LaXsfPfV*U+N@B5myN+89i<(5T6B`#d3;(sqqwP_%9QZ8=IOn><6_B>CxJo%z`qHnyv#$Dk=y`WWoE(DbdHZuc@0xlZxH>RkOU**bTh@jvX>}{DU6b)P4ev;lZ(bT4#&Q+soH7TAxuUWhDL~qj(D1;Ws(f&NFgs?!I<}41ieX?gNvpRgh=r{eQul6F@}8p;ig`27i^i1VcG?_CR1E*(JBzBX#qH;tK>XtiqUzoo<n%4~p@rH36Znh!Q03HD_hG!0xUUKS$c1wur0yBN1vlS^6wCx=OPEWfOKI#49`?ZF_w2MT?gk@OKbwV9sI@8Ar`*KEcp@CjO5;?hEuT1cXE&tWjfLWU^^~1%OZ>0QP5hlS)^FUI74Ut!Gc8-cutb`AFHL_5zA9I#w>~Cr#h$GUgHbJ2)E7-m+T8o5+JOpxRc;qiFT%LDwbK#|<4#}DI2C88B<<L2c4nM{8`w=f7Ao~c8IUuE>`=)Gi`Gh*e8GVbGg(uh`bHL%<R9k^E6-$^buuQ#IT?nE>7`c1hKj+|aCM>GD06PqK6>yMhNA9vO@?Ck%=A^3K@5LclL=o}O(y)>2U`Nj4VagJl^+$BfZ9m6B_Le4R+v`fS1$o2B<pT00U2A|`4WKQ+1V0Mb9Sx9y-^`-3D}*@|K`xtCBSp?AJwgN;StfPJm{0y4X<8`<A41=z6x+6y>=_k=KNHdrEv~Y^0rQU#uih{b)NY>DNKSd?8wdz-iUqj_N+C$Y1-3(Nm&M|GrC1(3+QMs!26R)neXTo*#$5omjzimg0r4K&3Q8=(S*m1YSmf=t|ZLuRCxq@&HoGN<aWVg5gbo~&SLFYr)BP+;v?Ed$bQm#g0L#^`KHJD!-SHgtHvg->#$6)&zmhd#CBDRz5D2;*uVNdBktDZzq-p*i)j|k=Z(fyz)Zen+OgMVTZ}jjH@6JS*sF`n<p9UYG@aI30Nm1Qe{mHjBbOjF^V8CnW8s10qMX#6NO=a_<%jl_J*Bah!g_y^xv*FA&#~o}4%O3G!}`^!)?95i&}|rObHN7JRf`sN^@vzzf%3}!V#NP)V%rsh|Km3H+@Cmu@8{DEaumI}VvJ8uAhc{EI5$w+cxv7t+nm(B!<fN_=5-1^Z<Nx@zn55S1)5~Zd(dQ3QzdHr_hWr=7fwQg*L+eLqwzQ!|I>N~rg7z!%v6~IlmQ~Dr6&9x57JGCRcEgW4|-sp4imrM`xDOp=@D35IW3em@3af_x<LL3x8SEnYAPK+oxvrI#h9R$yes{WUw@Zg$-k(0`C=OT@RoKx>$GYCzH__&W!zh+?fUp-+V#Y}wO9Ii>yEt@jo;F-AK9@FmmT|Lz`?0wzgx`h9A44STR`pOH)InzIi)H;e|sceGv93Yf}Q}<n!OZ%3_B)ZD`BAAO%f%6Y|Pr80>_DH<`Sk5HA#8Mos-UeDr{+xraDOb#UNEx-aO<+soknMYqvslT!|xSv<}QTX19bO3gP4wWx$~{rFTR_Iyg(&@UIkKg6*9(>J>8PYSd7Ml7Y_1^$iQendwHFdIk@!Xc8qobJ3&bNTZQHnl=;ppjDcZHCfIHp!nGps9-cVhfXl2Pji*d2b%;+TgBBk{}#!^pgQbL)FnB~ak)9OQ>dC|tok1IHf(}XJD^wjSnqXC_CX_Ju2FME>9RQf4(Wp7ml_Z)6?}C|@EW)H8NbGIt;uGJ-tH#wTA4up@b%7~;U9a4&G8YXiH9eYbg?-e<xqxg&_6YT?g?fh4v>^=xFUsz*24&UO>Fxd6D@qg;puI!WJ~8Me1h6;P+5K?U0n;dxZZ&}9S4}WaMimH+h?$jQR95Z_E(OOda%mMAIlbbZ#}58wc%tohSw}#(3SV@F}NcArI3W~fmU%POD3-b_t1U3Ew5eSykEcHQD#R_?+?7+waqR3%Ay}yuITOkuB-c<f7^Z+Dnc#2ZNKZHac$kjmUjm1{xVzMHzjZSYu|X3WXRMXxk5MilEV=GV%O*fXJHq^oc5)divbrb$zBn2#VO#bwuRcGwcm%YHSGE(j6n>I<5wPb_4t$gYvUs9BC#AH3N57ESP^a7u~TDiX=gE4Sd369qM$>>3@#Ew>E>ul2bsqy0xk)sP<2E>mcU4JkhN&10%x@dwK|d<+t5rlU`cj=7B|h{{?4C=T9O^jQ#Qv=r-p?^Sjg1pAj<@UP4Ihm!>!7E2HPh?65n^jfiEtES`JgdC5o_xkF~Fjudu6>fGV4pYF=DJ8+El8nxNU0QNIqdq=Z)unv)f_mO)l)jr*H%Ry)U8s4=W~0zn9yMYPx~qb+AwHT&JyJ8y>HwzYff{7<~D+Pwpe<{GV?3-`L(9hNmO=QgYfX~~Xt$qs9j6x!!n(i-!uTLYy66(&*DQgx$x2_uv%>wYp<SlQ14tS9<<rtr~(m11Gb@HdRQ>1!XDghWfswOcru&Gxl+3JDfsJzVYMQeMKkSCx3OP~|iGzC4XSL15S+c5Q&T9a`h)noM{qVbyam@%M0a(#$1<(BF9=sg?%!=)rydo-1HE{{8D#K;6}*axbUElZ&4Vwhj`|BORDkkT|V<{u1Pj0k}>!>+JF-zq(2`BPIM;PMXt9*UXO6ww9?P>isHKZ6twe%U?}1-SqnH#Cf>LG$VO)v$Uh50IDUJ2FGZ*{B5*qa1JZSwAY(op)Iv?mzVO`I@z?bx#9BH*OYdt2`T7@>5ESKmIAJDO<O0P)lISLVYy3%$*|Ct6z<dN{jMHU>vA(60TMsxHf<IQr8n#puV-hsGB3ITHxtsRBWsCNLaZ;oPD^V?_3KVf|E(9-%4>1%XJkjNZNAG2vO8KCAU$w#+*O`38?WUfPRl9cp(gTKnnXSnv{JX}fDmsK4q2YMyfkU#s1GcwBnu4E8Eud7j4jn`BinzmLnCiV(#spla!4ez67!JnJ{T13!4u+nYFYy%6IbNySExXUWtaRm*Z@iQ7+H!dxp*M>Jt(eh8TPizyZvz@%J3h&M=J=~@m~7R=QkWm1p`55A;9r@Z1$}9Y@C*H3oA4yJ6;&Fg_+p$#+vRCx+%UD1kcw1Cv$oybvrah?6IT15u(CO6&+D;h<>BinwmN!>SNnv0j?^lXCA;@J)+@R(UR#*HWj&w2m4m~olMe#j7MzS0;3PxsF)!bR+Q*z#pMxVh|s7Y5mDAQ^`vK&MMz0Ays?TJFQ7t8{<SJ2<CHcdvv}h4hG;e6j;ttdz_ywwdR2uyJxYwspTHg?y4%6=I+7Diuwig-n%`Oth?m3)779RjFUtRHZfXClxj}@Vg!={RWIzTS#r2iy55)jY87xctd7<>vSw5%YJ}<oyF?$I`P~*oFA3I|M%!bx%qeE>2D!*h&Qobk^N~xZ-A|9&42xuNAsUE!&bG(_nja4n?{S(H-M0%**NY*mf!!lv|0TEI>!<AITIfC>1D{yna2$JB-`%AA9;4A0&Qv~NhL5s7S!j=j7IfA4T47E?qC@L{!NokzpRpCwU61aNpUohY>dv3MJYxzfGj26NMFh>$=gcRwMSOt`IAS7zw=<t9w@)_!0SWv%@NR|H7_x{`1eKE5jvFrTEYQ=%0BR&v2T#osO<Gdl&9usd5OcM7K;^_mTa}*AOIT#!%{^pO(AQB&J#wk<r8?WPAthGu{uRt-L<r5{DP)RZ^rwTg4SMmvoiiK;L1O@(4@G+IwnRroVREf<N1t097K+i;Dy$A7pfVAgwkS2jVh(m+b(;D(>Q<t<X3vNfLzSe1VA(ezH7L(#EDvq#Nc?HA}FNox9Y{M<!YWNBdUZE`Z*Y-#>TBuZvGPn*lctcGcmLv?o{r=Yb2p>#$?^=X&1!p&j9YnJ&(rr{_xvCxrKDZJ-z!5H04;aTTg%A8v_~1hIpjCNK0+o@8i=TuKc(>aN;e#s2o2ePw8G!1#_Q8&oFk+(c1>$Y(1H<UOsD0283i}{M$E_<HHXW|6$RBK^{rM{SgJ2|!wfw<Dtbv(nAJ{?$`GZCMFD|h=3*iG5tPXyT+5E?f+5V+>UV6%a?QT$cf#A80-Q6IiGpJbauNN_p)7}~VS%VRmO^)`Fs(hmrE?kA|wV9NTsc=EbZG!c<Tu->^+=NMq6Kk$%aF!QulHtBQc`!;1B@4>%(<??&9H>5+p}BT*2B;yEsgy=cH+J0;u#`{%qx)c`iN3Bc@!I<07VFFS>RtCa2%(DQ;|QKvt1bW_iLM>XB%}bW3uR4f?@2q!4mJ4<isJ!`bGeFo8TQf+z&fH{^|FBiS<q31zAs)31d)#!1Xny$UY4=om;Imc2iHQKl8P2$&yK)EfHLaf8PSn|kf4r%+1P;`i@8)Hl@z789=iIno*jZVmtXND@~aH&CYZP0cNs@cn}C~KQt5<W38R6!dG<U`eX@-pnztH#6s4Nf!uPev`{_H%RSpOsugg{LU?O%dSJ^Z6Yu%0nac+{f$1;s2{&SLjVl}udaXr>emzKh|j3@eyky~;yo$y5aoGgEm4PI$twq8oMuAREpjfsS_Hizj*2r?^!W@baVO2Uw=kb`<U7S-8RhrJi`*{P9jW`WvdDZ@h2HdMA`V-l6^QlhdpZ4w1*0__7dwW6wt;>?;n0m*dyeHr~KZz-1`Gr)1`7pr|p5}6NGugujN^{&zM?u@aEE$MAC7g*}qy5Wi)nlJjVy>;_P%gD{QY)L#u?m%^0FhCQBuzFVka#JA)`^quf#jcG4rUr4VN<tT?O+!ku7Pk^M=N>F0N<&$|RWj-_qM;gL0V2m*OR2ju?t1W~q$~ybMplV84%Ox;rxBbk@xUE~Z4mZ>Gzp=&*m-e*@ag-ifN{cu1jRl{8J025bL%V&MBq(-lGrt@4|1Y2t1FWiYu3BuF%ab9Rk;H{i*Yq3KPos7_iS29<9S9Z;6vTHqcwHjmcf)wiM5B_+4BSD)wY95D#{a=Z*07tgl(GC`8l0NHq-q*;DCqPj0q<&kzkA9X6w@Bzpw}4nDt;FDpXOrdva9nBX9q%`bv1KOd*BZ<Ljg1aZmS(CtQ%t(GaRrPy4{??z=9h@L#yGoI>O1VmU2;1TVnt+K?tX+ND59q)5_GVd##{n5FtJo&<|!c8juJq?lZaIbh-f)<Brc0;2kOV<OE3!<8^Nm(X@m3-_|>XjK_lETpU%`7mjE8Zn`+sB6XFa9i%TiikY0sGm@gay^SA8x^yO!x@OcX|+_!q6jkZjcK{Mk^-AdNZwj=J6<-or{!@wO8|Y`ws!arztkA~r0MU^WjUCW$@^lxnfqV_$hNUT5f@~XRW+JQs!6dfw!T57=#kKKX-rc*LmX0+qB(@Aasgg_QhI0Gbsb{twd~-$gmQ#%=g6O0l(z><p6Vb<UV~1r*$S0J3d18Zxka^!>ew4v<YHOQRW`n(ga!+o<(r-kjYI*w93U~)8sAqKV!1QBrfdrLl#1OoAGtUk|K?Y<HgR;EuT8ifO4r>64OJttUSFY<qL(N8WrGi<TX`AwMJ`@bGPGQ+rr@t)M{!I9=aZiSq2cwf+14z3Y|EBs%XhhQaoNh#vZbnKva)7u&CeiI_lkMJs<w+UTwk#I^975v7&%}0It(|UBs<cHLNJCMvv&cg>!_64s{9O=YZ(n~1d_n~aw1bA7i9e&VS?m9TSD+(T-R!%_Hj{Tf9bvZD+Cz;7ZU5zCbGR+Eagg|#gMJ01gs85A|!^YorEgb!mf}H&q5PsLqHX%4DdEfI6@U9LPkfC#aTb6z_i_4sU)hn#H`*6k{GPOUX5(&yXz%b1mq%}!(^P`DNi@KFPg&zk8eHj&&I}*^C~*T(r_@P{1MU(1YTEz4~h<C>axuZ-ssAfcx1w*&(hCK$^FQI1rf{#6TaP1GO?F}D+KkCvb0-@t}#^XS!NFsJ~@!1p^9^3?zj23=XL7a=ZjSO&^;6PV$USdDIu<7rFM2xsU8Wp+a}e;bzzDyHB1)D+SiN_7)*yC#8aq_JF%)+2yNmBQ<=nhuGyj7Ha0+}=<}c@gTf9nGw89g-ml?(e$h7BtlK7c*Hn72F8s6a%!$3clT&G}T!q7$5L<5JOKeydXErQy6I9p8yw>WBOk12-wief%Si3@qiI<#M=Oz#c`{nA3Vsxm|)=RuN()UhT21AJf_z=#qfqr<|Hj4)qUveklC8tw~cTU_3%2^%###?QAfO`pm9n1Rwc-$U0p&b9N1lQ`X|DRvcKA*1c^ZjJ{hJ0={saEm?$W_;yyi1k!dUK!8&C-qJVxK3kZQkV1vXW_&r{fc=rM_8h^6g@ix7?(2=4w)&ZWr^gI>%1CefgG$i}b`buiEX$DLokpTnx3mLwwlS7&4dR0^>{e?D*Op;$|c@n>kN8ioB43m$+Avr%~-4Ke3DY^_E`dcEE9L<2ZxKjCEF<&DYnku{ZvIdl%orGsi+PvahciH@ivD$Y<)T{KbV^!}f|@p#$syU0pfH*6!d02RE242GE2vBwWnX)QfwcpMW-A+6`<I1uzas>#l>eU4g<|_`iE~pSXF`d$L7eY}*LPBLFG8!_JNzgC*1bY*B~-C{=3I_D8E<$fz)#Yh?$48>J@2Mt-C3PV-PBcP9o`PAYRCTAET%`4;z?TghN?XW5&kxbyyPapyOJp!c7ARjCuQr@Exl=xDXOwKvw&rL;&wHZ)gua!}8Ixspb0WP&)(*|wwUnqoM(^{f&lK@84PB;M|+xD(G;PrMcaFrlVM{(RkBx;Ry|>}xHY+DV6i^8K5)`Mu5NO_cRU6i(Do^mB@YHIxIhe6Q`)4QDKltG%7a>Ha;&DM^O0w#!6g2XwYP{`Z<c9^y}iGW>B-9}z>Bzz5@{y!?*Jb8Vo(D0Q=T93x%XI@$ZCB2(C-jjzsZeC8}=kQj3;nV)*To`2fOl0r(6^ly&DSHcpBS*Oq>x`#Wd{guyZA-q<i-x71RM1J6TMmPX=z@LOYHwxbo?h@fMh|p7im8=}W1&z5ZvPk13OS)lP^G49!M)pS1r|@BeJ*YKe0!2+3XG>Pj4bn$#H2>QqV|s#$Dsgil>RCmrNEr#t8n(`p0lfIRVCP77PYXFs=z;~3&Qm0^JSA{>*I4tiT4jbbF)%S0%bv=PCjS%_Q#)yZg<6w{|IbGRP3$BjT|pD!9Y7NcQ5kN3mJ`j;3E1kLp(pYgdLmHmq<IGbMXE152T;JdbM}u|Vko3y+O9AZKt^;;we7tPpfE{@3ZRG!0L56%dk>9mi)zli1w&C4ADzHd!nLhn6xG5Pogg=I$p|mQC?Fkmj-=Rp1CSK{m)}{6?uB%3k8in3_xk#RvNMKT=^pZm1C@`I`f+{`N#U!$&PAe^8%cPbi67A+0(EF4@yhR@i{DRpEftR)k$qM3sKq$SPRd8j?~cfSSrWw9NwG?um6&ML^u6o0Sm_=lcr-~J1$n_O)Q%EbRPMgns{!|;*S7MWZQ&^ELZCh(mm`<x`a81DgkYrS3YKuzn6v|`-Xneu9k3H5e6e<4mX*C6H_HaGaY7!K-*<rkN0RCoI~WWRlDBt!O~7kL4fhdQEH4TQVlC_S8%|L%DG?8#lS+kTK;4^dS=sK;%`208tir@m4%!M9V0wUNfaerVv>MendgRP6Z|(wKgK{8^>BW`oI=pP;%StTJ??QiSOkY;=t>vu#`L9aiZ=FV`G^I0d7x$tv=Tyk3+nR>B6Z4t_Jp#^+^@siF*40toYUPy5-;CiMtG<_<4XY?L3Ws|QbOd?KMEcq7+%y-r6^z(TDqj~We|^K6ce5!O!B~gB34Jk-CroHlhyH;=Uy&+bdr2Grt9Cb@oPT=V-FW7HIG}TVfm6XX>%;n15F)dap=zLI`&Go&!Jq`Gnc{86ZPgmLrK-AiNRR3m<-Ie*;Fj(tjbPB+7}XGsLUI9FlnEk*FsYDSJ1@E*?i;Y9v!oI>SkWNMhj!e-_JsYJG9uBWjsXFo2SP9iFWPdkqU<{q2RerANs0!<j3O%CVsvF-cukD7H{}Xe1R49PZ~%B&0Da%F;}EGSZCL96c*bpbmf}CD=0b#Sl(qE`0N}_a*Ai}nKOqghg<o$H$$$|?62$+r*lzTihJ#y3c)T7PJ?gnlFHRVvkSO6;)Pkj8?lcb>ALINd!4mEmjZvlHt)L)@Pz+hpWGZz81Syek6xcduVrk7A*(RIQt`c+v8EiY_$j~hynmab$(jxOCbeEcFKFPd>3uBUpXj2<Z@=YKp*fu6(R#+92#0EBk019D7LPUrG^%aeIZ^u{i=V;twR`6!z?c@Zb$q$Is&>EI$$1*t2ORAu(K{3-HCfT%?Bl9Yjt(vmG^c1Jerr?dK0GQH0;C^#qIono&;BpH4AiC@9I-4o!geDe#E%TU^Ipm&z*yQR*h4W?Nf=s{({+O6bI8)UOrg6h;Fb5NM@vdSxHMkl!I$H&J-dD3}m@;f^-j+kLcCJXpTdlq`B9u!~;0_8tla3!NmAUep^<d!9vX^?W9gqnPkLktDL#Nv)&ZgHzi#(NhxINO?mKr8uZs1VS#E!7Q#3<bjSqf-~KqOUz;3*LkS*5vrRSlYGfeaAPa&h*FQWXf+EAh3V<d@XJnd@5r>cX>nb#D1GK1j`qa2Tuk`0A(W-I)4MQ^j>uUY%sI8{$-X2P^i~QZ%tkBvGes2-jpGa&ZT?cAFZJ+V#0A--;%gc-_nKzi=`~<UMVI%opu0PnX424ys?An?%k+uouT>dZpK;x4BynzBrl&@O%+W-l&$(qYV;Y5ua`zb)Kz!tDCSRM+l*}a-v<3Nglus?ibukI<z@K6vI#bMDtIU7&Rp~{tT*L>1W(HaAi)Ijfjf&oX3n&BV)xNW@1?tN0dK57ok?mzIv29O!(HmD*iN<{bGc&G#M}0BSs)=$#u!@z(owsu_|J1iG}OAs2<dHb+mmW{`0~0Tu43Jl<|{hP|kkmlh(klBm(RvAfjR|^uz`(?SaFgQDY)cwU^%U%Z6$q6(rY_U~I-q8P(4*0w#`gN0Y5`zaDR{ghz&^9b+BQv%7#V4WA#GTSQpVqDoWOK;Uh|hzp7OpyoyIqf-00@s*5RJ}<Ts|BQ`|0cUdb&(0`*X5qu?rKYMEi$`={Ckh_VR#w+W5nRmr*3Ll##ugLVG7e?p;Des|L7yP^z-RTuw>z>F;}DjMmS>$M`Kn7nvw~=nk&`@DT|M9+>Ydf0@atz<2`vn>O>dqrT7|OS9zN%Ofp0x(i6aSoI+FlUIHfkrP<C!9aHeBY_}Ms{+<+{32^G%5jyxsRXb(BfeI*TAX9lPGRAq(xNt0t<W~-Wot1q-gAX`^o*Uc~2QhPkPmxqI$TP*<P#j4eqSZ6lQw%tK*@(Zf2O&{zR>v^dEuB}n}XY}+?Vzg0`kjtGy_GZ%;td<H{;-Rdu9Qc~kAGr<_j)*Uhgb5#z!yrdT?ht?)jxFQP>`-j;3$QSk!B{3yxkQf^uF=!lRE7Wtl9$FKnEYHTP-)$5II~Ayxh;GF`VxBH0V&W^XbeeOAaKCT_?9suA--iD#2^@bAF0*=YwD8N6Wd!drm~#vsi(<*Vg%wevtA%&A()Xs^ydM9pOR#kQz{>s|MJ^>v_B{oED;FSPAIUdz{EU#F5z4>G*~q@_TWtgrfi}PUhQDaW$-FYhba>3gT7Ox<wfjsOLc3ikJhHJiiuKVYRq`PT)0+(OjAA#2QDW@U2la;36>#xZ=1ER9R;W+YrCZOML)HDr#`GXKc_IG`aOxU!5kq1_6}DAa$z+Dq3JLn@*3eab_PK2*TqC3`H_9JYW2deHL85;1Uj-3CuY<idsV3kimV8dcYBI`bk>Erdr-{@&OoURhX-9$N!bPZWk6Y8ey%1uSzf#axup+b5633I7be@Rm4G$^Th}Rsqt?|isO5g|2&w@R!hga=po7u63vh>oyS6${E!zXb1CUJzt-j?2*4_-e2eWq#)+jIoC;t@2Q;_OC^FEw;y2n_{3#XOwUT?=|t!kwI3QV%K7Cm#meb!{gD+4S_7z;T~v$**TD_iS@1Z%=~DKSpMHY9T_FUOzKfoi?%NkAi(9A7hpI?!H>f9*AAMoQfzpG9TuLGecm2fj>AveZXQHhN`=K-Ww}3Q)IR;aH>gGJL?r<n~g+bbb=*L{S2jkf_>EsOCKz`>VhDPk1-y=d8rDpk=z8&Y3-uy`H^y3|#M}$~5h_2J-cW=c9j4C(NJy311oHCCRGIZ%hnN+SWrE{Ws3<*n`qJd3a;r7^j)gM?|?N@yeYEyLY@@Ph26{r0eEw4z;KtUkGM>(pXOei3PZsh|HwRKqej2{OrsYhNUUe>R{24xJPDd<jAZ#D6NhtkA$=_&V*xk1Xrr#SLe-?<G7P4O^g3)%fF;2oiy$I!h&kPfdLatPLAg{)=v*q{-9mMIA7`cm6=Yl23EEA%8{`A31?y|ACw(ZxY7rfM=_van6P2Z6h+C<{b$YX$az&j=)tx@x#%u*9pZOj2B}jahyoVomf#0^QL=^1vKe#p5jBY@qCKlDQiEiC$SLO*s@QW5#hM^ii3a`GsaI*jI=LD%G55z89T7wLY6zD2eCAf7!@4-<^}%X<&f-;%l8CQ99E!eF-&nqP`WY&WRC-Kt4k_zvP+Bo}zv^5<Mum6o;%H|-?ZhN^ndcDH;^(+Hjrn|PnCi_=&DCotqk7u|r;~RuIQ0e%pRY{Y%qQ%o6E=lcbsJRY3p+A?#F?rR^H>h<t0G<at@nT+m&h>Q6X5AkjtnNf>(n!rw5K!@SUCrt?|@kft2{Rey%3Hjf(7zOx*R7K7l&w;b><kkt<?ykmWc^&B$)vaP{tMLtG=xONkoP;9K!IrA}$HDH7U)`yncK=<>n{=<UB-gd(QdJdi?0l5MhkLIQm^S<Pi$O4)cStJQnk9MQ9wVIE2WTk^Wg7=l_GeBTfoglx9mKo;5p`!PT=1X#Wr)pCxrR_4q?ZR|?gaHkx}V5~=_GD~W!~rR{G<zXmmXeds%|(CwvB8w{8uw3*CSmeDV=ZmM<Q2-F;2f>>GlHljEa-L0FQt<_(bpwAQo`?afcAezuvKno_h%p@r|IZ41X6PirhJ!klYcytEaaT{9h1?x}KCzSDd1gB^)$^wh?3y{vfvBKqq)4{mdSd@ELrNZJFPKVf-#EqH8)WGS~emQO$`JeLDvQD}GidDhlzuo-##U}OCq)<1hH;Ww#`hq~MW262YeD!e)6b}Iuq}Ql(&;!9&uEenn!5zv@<zj4z*im^C^&o6mNPUp|(wp^h^zxIfiqz~ywMK67=D3X004&|ftkj~FI|MT5HNnYr5V1g`%pehMtFos~63;y~RvU4)l)yJQR8|3eVI@IJn~-k_SF5Fd1Xi=t@e?;7>O}$m;L*q}2O0Frf!4`wJsEB|EMSni=4%YuM(xq5TGsk1U}xr{d|bXEnf%<3;#|lbf|XF{Jc!e9j24Kmh-C~0>XPZJ84mY<egEYq1MGW!xtaJ4%jM>r;;_~_UP1>4BRXKYY3WAPSZgiRDzo=ADGKviqp(EStmLH|Yk$glwZshWTy>j5eY4^*mKa>Yy2`K`8+d1{ScMb|omt$%t;kFII8imAW$3g_v+vz4CWJZwSX0E8cAD*LJ_NQP@#mwy9p#P{Wl%G~YdhBPS{jx$FxU=oinKMzU!~CF9KT^!@_*c1@@kPR*CJVpfPoxXCp-Fh>|#ZaG+M^dC_Kpf$}$?HKjmeBM;q%N4crp`^i8}&{V6c2E_n^Ebk~rj-ryPoXvlsz8E`#I*M3mdjhk1L6D?hX_Uw7I#O&<VV5K{)rxqf2O#}!^dDwwN%d!{12OsBJZl)cjQdFqifH10#q?es7!aby80~Jld_UDYCEG%IP8$#Av^56;Qi{Ej-DW)om8v)eEv79@rEP)`65{(Q5Gj=G~Hzyx|e@4_QpZJl1)P_B)O<5p243^xI6Ii0L7+{+k<YQ{f$4}3ewYXY}J4>unu5Nd5O#TqI^<<KiNNB9mj7KPsNHID(tLgju&MTRl;Du35?&Qa0E*<4$J_S-8F?rNL@a_xtMl-Q-Y6`?)oltcl)j3bJ>`SWuc)E_4iQ1JlC~(mf*Udadu&rdK3oQn&7A62Qyj0w{sDYx3tc?z@Y>5WmAGyPMf;J#8jeE5t#TZBn8YXuly+N`D4}P-p<lxU5B;E{u@fVD1_gJCu0Lz&(teB($zTleE)!ux^6)Z=L2o@JOJj)B%18m6=EEAw>1%$;W{KbIfV>CHT7OCJ#9ezQ0dozNj=C=Vg#3>A^E&Dl?U$Qbp7J%Ezj7<^++u%&T=bJ4!$XK3Cr<J?jJ*6Z{?tAj;l~Sj?9Hwt%_=_kh;Oms|^oz;jkM_}J&HZ8~>rYD+Kjo`fu>QvTfM;nXJL6|*R&JZAd{qSJT>xqG0!S+qfMlHT0v3^opFIc9ny36Fe)htSZHCP<06BxribOI_u-Ui*%;rnLtT(jmWDTEa?sZjhY_e~R75#ffaZH75co4jVmSw-LBzYjaJy7<O_JEVt7-M=XYKQbHtufM;t$KB?HI`<ru_`pCFntNj=e=IZjX`MV<154BI{X)}svKAVxPX1%Vz*YUu{u=4VyL=JB6cB~kmgeCu%7}z&+6}#Z;nJo3WqaU1vX~xr0t>7?t@?}$xFPMLU}u;Z^VdYN>wd7EVCzVycmp*-2yl1AaW$8$?1ZjdY|h6ytE38m9rG3AA*og{uQHI>dsj?v3yP<uD`8<(;RUv^;M9xIt=8lmKnOu%>THl`+?SpziTIo{6`&S|Hx}W!B3F&0l@y5^^_Cgw<T6N@@|BZfBRhfKk*S4c%z8_+1CGqvo1{V#^ktz$Dok8qEQ1fG-^thdvL-H$7>)AhxAk2O?T%l(jdPAd-{Eu0jx=(0Or+UP3oHk$oh=<=$bZ&^>S1e#KzO3Y0W2D9{u$XmU&%l7885xiY$s-<X?Qj+wEq!?xEk=gen|%({U!>aGXg~7G~<BR^J)&x!ufpeTUb+mG{w7DNyr}=LTF(G|9H8LeGWi3}jS--{huOX&(juxv2>%IamIkq}Gm%)+lXSC0S0jKZ8C+iYe^m{taB~qz$yDwn|1}Vz*Ljt6D2yW@^j3B)EQEGc&aR?T0jp9i?`D%_KIPz+FWyuh;y`L6@DZ33Ml0TE>XULsVz=iDk=?Cb3NYC-V$0?82bem0vI)TE&uT-JS7vcvx{`^1?7SaFNdJVaP2u%9%KtwML3Yn(tODR!AxY^2$|p9zd@qmyKIQnw*ZpS?ED_qc_E}ezGiJnF#kLE-0)WNY<9?cLabT0HKuqEA*gtA2-E+dOwE`lUKfB?-2&4Iek71JsBm=Og{Pw^by|4x7Fce8kht|UXD$<8#w{#2{kL9T6U)+=WqzNEqlN8Hpjs`vw2vco;Y%|Z0Y$juFUb7B9YmvX<<IcU5%twK<_9?z6Ga<SbPp-N@52YC{EODG!Pl&h6-3!Aj2xE+$>z2JTJZUVWbmaD)f_+M^}+iu`yjq$?JNl5iHzco`q@)Rc(lYJA-7kw2j=abx;jnS7CB4EFiem>{o`Jonb(#V~5_`)ElAGQ-3qeHXbYCzi2id+KWrl`pkj(d{&-cF5D{{5Ak^MU=_Gee!^e7jYs|mo4@4R&h38)D8S(Xi*@)rDF%o+h8x(H;ON+lkwj*TeM%J891%46H_srZVeNQmHr{_OZbMMzhX2a1r~#Cz>Bl<;wayMj+@AmZ$$zUHfp34tmf*&=au`Yk)cRAI6HgeD-#(ImDXv_3JH!DX%2PHH5kN6=e`OUJeMv@Bm{pJa1(!)K(!m>D&!5woK-be<><>&j{X&;z68a)tFNZ~#qb9K!d!~JC?WZ#?(<C_<mZB`=GD&dDczgXU!G$i>!DaE{cy6;a%e@&4mYDeH?e&3xD{Df9#YQj%8Y)GVL)}}UB>Wri6ArL07rtxvPyORG5TikXu(rZPedRd0zO1;0KHe~$hP+}c9W>9HX2UKo2p_pDf&}<jBYDSLJ@t?2x*$Q!L=|+w0JvbPZlqNX+;sHQMQezD8-(>DE36v0>AfxQ#+@^j0S~=Z?6D*saJ%-#p%T0^5@@035hQGZTM`Y{pmVCHP-{xPYU7lvkp$sEuEKXj3$|=IwbeS0=taaDJ-AYGoWhmwDEHiwF;(VDwX}!vN0N%w$T~M+y(4#+@Mk`x@X_HWS#X%;k7P_t9O?N4tI5S4_aueohIu)`mV$Vd5?d!&dYLTP&sjqXwT7k%1`LZa1)WVW8VH$56RMANTp^L=s7jg(k7v}t*}7w9#oE;3=5UXs5F_ZIh$r?O<L{dGC9)N|8$GvHcLPn<D@a#OfV|+_*A$Ru+To=v&`{R(b^$M8j?=Hn2thh*jSaqBEwj{$01jx(-HA0z-qLzMse~ZGISbb-+`L;GllEdgaQSWJO{yu!xM#{2w^rbkorQ6ATZ+yvQ$}B9Xp$Iq>N<ofe<-6z5d*>ul$C3DMf2FQFFpuLjCrB_VXL=ECrL5_SEDntX0fgO%!ipD3uxi!h|#I(w}@}3?O|oen<;=&n6MNucB>%CKnULeAJkuK{x#SBEY=`wgGnamz@ChwNVAwR{R4oF>9N@;4lLhqgNqZ%a79oK+GR{!>7BI-sTvYlkl6+?-J*Cf(pI7#$xz-qqEFb9#CLSqfc#OsIj{B`>OYh}33zp*hFi-fzdwK-F2W&3YeVhPLzC(U$pI?yN&2%ySN+t3xo+B@q(jT5HPl%It8EAJ!i9)qY~1Vk6gVkCu19st9R7&!2GyO8EBX{Z133v?DE5h|zfT7QZ+eYfMt}Ef0_Ceh)~`VM=)z9L;<I%sQ4nz<A?+zN<byCtH&&&QAg8HL<t#<8ErzxT6)><y<P#y%MRSTWP<}<^C#77O8ZpaKRRsz31`;qUv%acZ-oy!Xq+n>Ni4=~ozNi7469ol=$?juEq@Jz$q)8+@Tws;_1y-piR*B}}RcHS;P9TR_dDRiRzE~s505o?+S93LlcR%H7+@U&)`}8e2KQ&_3A!cVTy)SghO2F^@T5(3QGIitQ$Xot50}`FhI%hpJL;Tk^+SO7O^3ut&r`km}MoOv;3;KMjXHf^BTWIl4U|fPb8Ljf?v{9<5;VKxEnu4nT*V2|`rufQ1DpKZ)>9-ZDI+@C&*hPG5yQmRlLa$;a25SpjcHUg&*Y%2k&2!DHnL{%(U30y#Y9zL67YTlAr-pbdJd-(mmR(qzp<TUI%TB&*vn4IdrRGCXslve`bu+lFhS9`qnqiQ&X1K=2Xw#_k1|2CgWZO+F6@;JA{Rn=lF`YH^;_M&J^u|mmQ2L)7kc9(8u-SfnHQoG+&2M2gj6YZT0oV*&++wu^Euc)YZNRUL_)$GCk2|t5>7)}+4fH+BID1ghKO_(>JV{{zgcL56Z_1Z`3jWz7cqKwmhDQfntUo<T_s<XY!J8)o;Ff1JIZhErF8AiB9IZZ&{~l!8S;hsh>{NCF0vLDe(NwJyO%$Y~>8a-63E1(HRQQLQ-*N3kv-|_d2=MC@fQDT~GQzI-K9Zt`C;ek15RU!nk)+9IKCa@&#*#QzEwfLedjde%Jv2fJyC;5cKG@={@q)XC3;z>V<{kgkBdw(6`U4^w5_j=E?fA5?gQv$+bBD`=gOq_-4tRLP`2M`ylRx&hZF!O;Mz~`ea!JB>!FG2RQrW9)2!C<mu3TTPmX!6yrL5BVev%j|>x>UXj#u0-S?h^@ezCTID4PevpOMm_fnD90)qzE>M(j40&=O!n(25cQ!xr|?3Ye%G34BuAQRI)X6|8%kl5}$I-SAVmTvF5lG&GE%O&LEdfS@<rY&L{QaS$I6cG#cdHjsQ1@<0BeE+n_FT8l<AGNik5j#?hvZdi0b2F%9ftAKN7@B&<sgtwP0D{Q@(V#IL-h>(;cp8~U#un{jz1>O!9U?9C0G4cj6FvYmVJoRA*ycWK-1U^mx%2GxQ8z$I$NS?9&#S=(mP{uuZ8k~kqiHjs5<;;crM<4QnsVaxTR{|Bltmk?{xzo6E^C&C>RAM6osN+p{T#Z7dZ!pG)rhd&p*o%iPFETRAjBlChSVX|v;l*1(u`m`(6hH36u8u;CDn^^JGvb}tm5FM(eHQ1BgL33{QjXWj*@_8>F(jL|49z6{KB^`5s%>-ZYInI;q7}w+dK{o-{^Xx){_tyi=-+3J^%G&9UAr#}ADW%*j>xfWN?J*#xp$4QTb9Q!I_V?(+E}6ljg(>bp+u$J3#7|^G-;Wj(!W~jV<YtsZR|U4-Q}?O>tiEUXe1dVJ{!R_J<4;9z{+Pv=jBy*UXI<E^pDzvS^cA}v{Sb5i)9>+(WUPJG5}ECp$v0wbShs*$Q(dT_8!H(ho=&MB90m&!$*`&VVS#!f)r3D>E4&X<a87SyLoWf<;Ew7<mD$UKs)L`ft_!gm2>w*>WA>8(B|O1Z7#UWqjWe*)LJg!9#&O+CT<>)-JF~`0^#&xc+>$ORc#5e?13E8caFH#N7=U#mEVNVADT}ayA1t*bdy^4rf%~cFUGgn63-PruC~d6cb;QtD#M#`51la>b;q=)24+w@%^RwR$kjvuZMpg=__YghkZ2;+B1-DQ<SMGe@@(TPW2y|gP71G}h@*}nffzNJW`lRZzY(EIl31iXb$z@-EDD{FwoZQL6Gi^rntZjQfi3^KlsmEK7s@7z8=c#NuWpyo&I&bIpLK4FCmkEdqQ>H|Y5r6B3Ies=$v3M!8k9UVN*n_Dqw}FeV~x@ppahRM8UP)#Ee+5W`@9O`^ndalmJSa|GC+dwFcw=jx67(K?pS)HW*RR5h4vyUGZF}kT1H5MR=rBB-7JL69%|_9GqK$Ggo)%Ob98J>CWwve=e6muzqg{D85!J5B!`wqtgE26d2+c{fioR`$7i#VPcr;nEIWhrVr}ixlVqushbMt-X(fDbGOn<#I5whms(chB$MFwi%1O-o2W5FFmj_d>dmzx<aV|CNqp5>dcA0G)2j;ZF<$JUNMrVs|{tVTZeZ;agj!>DQfFR`&MR^eMO=iX1qM^5-#sY1SDYHP4+>@6ub_o=R2diwtTkg(tTSIBRe`akdHwQGgeD{oDyrI)_;^U0#2e}V$TpYh$O<nST`eJ+TMvEvnkd$w)6@dasUuQXc&!G`%{uL-Kx;wWKH#paICG<VFr63g26%eZ_p|6{F@O<K;k!RylcJ3KUY@#8sG0ojt{d{YQv&4MLjvpBh=L!)K1=oCd)+mvV)JB0xdZ|<T38~5oHtX2QEl?s+A}eUOc68@RiJ;VS0;3XGfVM&Y;HQ6jnYzwskY*{fueRX!BN0BrUw@k^{rgFov#4{Z`p0K#=4++>D;7|yF!nCF^CIJ!nz^U(3ik(;h)m7g9O_`XoC9l)Rn5GejO(3BZ*Z}j$&T%Xh&fvfZBR%bDj|-=nAY5$48Fv1TFoC!Y)vM0Z#AZC-ONgoyproMeGgV@B$69dfZ+Cy#NE)cw&)JhMuRoTR9ghCxBSg~>M93m8i`W{Wjj-k+(#GH|7V)tMwPPt0Tau?B$3+Q#V4zvU<~#WNknqmo*-OOHj?8rewJC64z7z5)oR)!R<tcNxiAoRtUw(OMq$T_UBXvd7CnxbnSG|Hb6=Ik>duCX4o6^jSN@s_Nhm2@G}GA}twxRZWd@E_+>t?=EXGR@?E(6UM+tk4^z9@Gx(o^wx9_c%Q|>MdEANe(-LmbBZ=U%pB?!u|xid-Zje?Z`>ud_G<D8$3`GIUQZmnRGTj_0>Z<iY5{?C0#uj^%BdRhKuLvcqTynfOFzEn;<+9hY4!QyQ&3~ZcsjS6m+P-E+@Bc0et$|ll`RRA<DW`(okb!hT1HwSEkXaxMg^U!(dy{N0?iE^hatNzaGCJ#i)3L@xgmy=~!a~0@`O=#^qu=YaV=>Sbza&L&n+L)rV%|?Wg2bm|K`dX)-@7&4&`&fSc&6~_Tm~T_T%0q)Bu{{Sz<)bsfH-R_HO)G!eAppXS<$8{A5!pUYB!Dn$?v03Z0r>!jYmn+YlLPOndoXpWU`%aVs*Lc&X36ZkLP3B(m8?h#v?FAYOkftbC^wVqD{BaV#tB~+gVFE2k_=O=^m=_8Cp`yEDk4P<{=>?B=IxF3CnqP%sZA?^SToF(whRwT@>EYfWJ<<xF&E>dBd>~0Y&CKd1wSbVMtx=&#|h_*J)&hU71_jY|KIml`lrnQmr?ppE2aNxv;8Wi|I65J()d4TDz%!cY?*?o<fRLU`#Ca-=V_GNepBF|#z=@2%4=@%m9|ygAJg~>Ux^CiYI~^MMBv0N)>5A4`33?DgP=*QC`@AiH7=atlZPoZFyLgfP%ss>=_aRX)2L|MxW00lN~Vxz;s4Nk!*Df~*|gZe+hu34f(a7a-gl;qM%oD@%lNT2^S|FZk9WKppTLW9e5w*FuZ%Artma=9puSxoaOAr&oToF#?V_#SGBz~^y!yt?o+A<J)N&sUO$|Mp<8n4EIq?)o%o8~%R*Jk*p}x^yhY1hmsV2>zI}zpk+6t7ZF=t`zkT;?O$|+v<%4iYOYf_?qvToFJtR~IKcuu;?X*M;hZi38B29A1leb|^pEQ{=k{|IDM>2TpS=&fTTWo%Uz22+*BamwdzoH?DbB*+}?+`va>XPT5t10QX&i}1HG5#EjiwkNoC?!X5l`SevYY7k^JEb%`q2Y53Y3Q|d?^?<xu#0oACSg+S*@U6{M%DSRKhoXEtIUUwqGMlUlFQ8cd!BV{JZJUmClZZIJeSI#C7x<qk+9ok=@D}Kq6({S6D@?QgfLnPvYca#(hjv@L{54L${^g}CNq8!o#5GwG%+8R$6^NEVdj}VG5L6@5+nWwO(ytMNJb<~n2l>5hEug1n4h_FI5#~g(XxzZT)?8qUC2YyMOj*-EEn&vk#9DZ3L-iDBu^N&KMuiw#rrFKj0raW$V5->JPt#8I7Ce}mF@7U-i#twh{cr$ibA=KxZ6x=BF7-*4^OS@%paGOaoQhyNEFy!Y*fk=Z1cV}c+8t#nj3N=BMqgn;db=VhCjt1;asY|OwV^(*N-){+lY~LCFB>PVX7;EF!Ew5_hE|yM+78Vul-+?CnMWr(r&O^!Xx#qq?_WjuvXUleC8`^eCiHGS_qm_FTa6;`n_5Dc99*NpM6ekwE$7dcU3rF1Mv_!A@o#f;mHNLjidsu}e@`^$UhsW=n=P7avahyi>B0k+da2Y)fp+Yqa{?{VU~)_2>pam8AGgf#qvm(q_<hhzj^84Mp{-b^H|UnJejV~Ny+jXDEOWgefg?l^>4WXOs6CKYTwa_Xkx;eFwg+m%r4gXEq{=6&;e8|NO~cIK`I21@7Eq%WdIU6A{uK8(rn)YSSj(?_JDF5Hng^Poq+n7+2IHX8CxkPCiKq&;W{t*^CZbut`GxjC`3j?~e8`DH1-}P)SFwuRrK6E)nG5gnm3?)c8_MfXwhsnVe~Rg^z7MrwM2YkUa`8Odk=k-r8@PoTaj4;bYFu#h>JU@4KUAr3S-Rd}hNwS1lier2BdH2z6Gha9x)Llipt>X^bs~~t1nEo)S_r`~al#5Tt;v&FqcN;>ONme~@pIX?F#I8`5P9nv$2|+EMUHz^>{iPX!K4(Y+@oF48M|m=l2Kr4l_-L1sUmS&s0D92D;_?)qImexXSMrfV6TGP{H!43RZsmu*BelM7A3?ji-$`bR=H?>OdA4|QBXm{JWZ<op8n;>W<w;+rVpwUl$d3=0rY7%Yj<F@l#fHV8%r<d(&r*9Q^dwmT6$o8Z;;WCuzE~Cc6|QR$S@(JP*HBhk<(YtOr|X5-vgRf)}9=-=<u00lx-|0-LmE6D}+(3my+l7k%7#qd{9s=g!G-}xsd@gL#;jT_Lf4Msm}Q+#tpx<3<_~l_c!F~Mu5f>X>F}1796rS2KA1k=tH4I7#s4S_7PXQoKD{fR>U#PaFH-MR5KD^LlB}&FikDeFz6-x&do^Yg-x_I$k&KaqIi%xQn_k0*BjZZ1eJ<fHrt6WS1TOrJU~<4q{x_2sYn2gJSfmPHrZK5uiC6?YD?y1G7m6j3<+08C}>4?Fd@7+T5&2=IzqWKJqpF-DiKAS$c8;M^IZ)V@ZrT++W>;MaE)?HD2E5>#|WC`+`hc!R}AF8ZSKlff226^h8T598mD{cWNxA`zeF=b9yq2umL#=-5b=)n>R<-sD9xAP@XpcoSClEd4B__?)wUyR_qg{10tcBRsKb`^yrVVG9X6a^ZC6=jj3xnQ3<B0*S~Zc&Gp%Hv%2H;1MR{u=R_}>%V_RgTJQSW8Dtr+|S#V6+Xfo=;UgEah12}@6gC!i<--=m?8bmo&n)!7`$8o^531%#Wf<dIqnF9kR!Y})xG5zlE<!E_fz782!D+he3XxZ0jIn-#myY3)-s{nDU`F2Yf(4>kwZLJrfvXO{#Na3m^ptPD+dVmKj=wVHH&5pWK0xZi)uPlv-sb6XSi4b@A2YHPr%mFXs;PUem_FSJRZ5z0uaW(#S0J4clVq=(qQt$~W$ReZNV=Yg{Ke6}?m98Uh&d5M?)GU>e?#XgalA9yF=16_vF40dBU^(Cexb%C<Rm*5nMPD;w<IfU&?i+=p!uJtnax#Q}Ur8!Ke4*21#6^>Udy^y>MfEw_TQr>AsR|b8P-U#$BXCVVm}c!!6V+ZYlBG{`K`s_2Q<E{G%>VqAOx>mP_r=t0A?eCx*}YD_6Ot+@`kzhUJ;GMZ-e79m;D0I+!R$@ckDq$w!qIc2be8T~vlBWWrq7HC+?`F}#>pBcP5QA`lUtMzeIp=b=S%}sDnK>el`^Nz+pf;ru*z~p9G#VAVs-xNLNmCAs)@LIgn>?+znkJRcPx+iDlT)^Rk7BpEYq)ap8P4xj>jf#H>*8;3{9E;{3})yo2H-Ix)2n@ZeoIB*AN_+f?{mR5b|yd^?9ZhF9gLV+G;M5R>cpq9NV7>icw&4sVNrL0(WYt&YXWLCbqMz7&mZbUA?7T?S-sZzmOFxfkv59hpH*&&NRic(k%KnYpLqAQ>-+_tQq`5nl%fGebfZ&Z@z!`vgfMz!Mc}qZ+eL)cCNGd*4AY>^CqXTK-F2KFnfH9F?qadOdeLQ<i5I+U)NbQG=dSO!$N8?Tu3c;3uAI0uJkH9Uf8`{SY9Eun5`{|onvZCmP2i*wupn9+T!)LWW3pyB(!MZNB*&TlJ4JmpN;zy@XXMARQvIMp@qw^0!)bwCEirG%at+_tfmV(Z3c2kdaxsk1566;%s~4ArVj*Nj+E3=JWatZN7@Zd$2sUohd{Q^36#lODJSqLSCF2>F&ZNKXAV!e={*=S?FnO6-EPj3JF%7Vr%$Mo5L<Jb7>RHuHI*m-FdI7iP`lJ83<2GIMfsb>&Uo-m9&GLVxXV`jZ|t6zVf}+wtXXGbS1;^|Wc98JkVrRzEmf^M-xH(hIAB|BVHL)Zbg?-$>YI_;OsQkjUo*G*)jE}!$%MRA{KFgJP~Xx+NSYMR=r+o0y9&*Q%yU<j9om)dUo?+%ZqrMA1;DiypGJvz<dEEQqtwulsY3up4(Q0{z^_RuM__`W>DF^VZBP-2x(Eh-D_iFR1u<G>2iwgHEKpDVW7_6WJ{pr!gDzP=HI$Kjx3+WmY6sn~Hvg_0|E}iw<jmFi4HJ`RaBS3H@b{FH2hAOXz94mU`IG1Y)1Mv6Q1N&OG+z#_H_o+Vy>%>qx|akSSXON{GaFFGiN{l*@T8YkLeF?DXj&3?n??97$AJYQ11_T4c6w$jB}+Tt?yjWiLD|;8Sh~C{ANc8z#;>e!eTAbKX0nUH*Gvy#G&^iF;3zK`coFE<$;udW?>wUYiHn0YQ;btJTw^)~xpHo*6zL#h>N7U4r-S;Ul@RuSeDf<TFzarw6j=-~lCR}xiwet>oe|RP&RUYt$0t0YYwA2#js~#tTxTiQrE|5;B7l*2g3hqb<fB&Je60dowMCS4R!dB9<sxOfS!xNo<FeSW?Lc}8)w~H4d+<)Q`#F8P){;CfN-c8Wx`oA%tLd`Z(tQ*97ysqFPaWTVz>c@|iORpdQlXV5?ZKDP%3%7ksG#(%!?>vI4uW?F?u_$jHH0o@JyaE34cG(g2JjZ-JQx<`ggp6)$dQU^QAc@DB5ycs{Q`;KQmlu(vK$1jGi~UWe(i$!xmsyl7Xw!{!2WVzwj7lP=SA^gE(5C2&&eQV^_!KzGB*2l8IVPVa-BOCs^@T-eZTV-`3^|3fiy3S!D#?$^v&aCId<OTu?zphSF$Yb0KmJxEQ;yzdgqyPrFR!=VoOF+^_4$g6A>b_9d9s=CK@5pidK_=*~-`TqG*L~n0&q4n^or(Mk82ky(n6}2A#nWX>9rkKM#Tr*-ProL&zK>`ioi>tQf6Ubu>J=C))_;cI<3j_G>NV`-KqlDSneGRzI>Db|2z*P@O@D^eK#Iy#!{T<c}TV@8cLOBeZN2Pa)qa=wS8wggYrZp?D66wvLL4D!_p?Yyl;D^K3$7;gB37yi!%5go)uKpduBhtl-6M>#?!&0QXjpLM2Mb<?22<8HJT_H{_F`7FJrAB(1_z<EkdvR#1@##(>@d70YcAyhM|DwScIkU4G(YG9{n{2N*JM9PlYSQls?|{@zJA6L76Ev5u78WvIxKJn_)gZ{Xnkx8EiM1opt~Y-pl<lvCXs9s5%B2hk9^xz}og=Q?+m9Hlz*sq!`J_-6J1TZ#%+dZDE}a)7a{$I62y_R}dLTKWyFlO6fGwF+7ZCbey)byDieYl=uqiilDkS5qFda5lXmD#VSP&RsLPN>!yE!eu6_Def#?Mnoy!bxpj?o{dv71;dL5f~w7&a8F5)pOPS|J$6-H)X!FS=*fP4+4j%AT3UJ@Tp<{}+Fe8Zq`Osl5O=kzUCMe(10hsRB$Ame4-!IH9z5D{CTVGZAuV0<nU*~X%A2xvvB<fjdGeZa6cs*7&NQo+Nl0))ky6MBpbpZmX30!fJ)yfvXIV&7M$&Anda<1;>BBbjh4VNT@UE&VJL4JJZWV>877GUEbNWOfjVsPo2X7{j&?JPl;Z~Ieq^NI9?DyGuR%0~3IBgrt!UUL{D-8j>X-0(wB4Ukst&a`4O9Lbw+!Ly;i{+}`wB}76FleRoI)|>@$I5=RJY?}Hu8L((mc(LgbfQzh$w|^{?kZQewR7$Sy>-(8>jj({VbvaK)~Du+^VgV2{FM)BEbs!{ZX)*8<e`7r&0;Tb-J<$_hOdkA6PQ{)I6{Vp8))CkG^Hcc5wSGe2vl1xzfe~5+uG)FCQT|20a=v_U*{;mr<`O;2CUgLP98D_w3K3`=;m(r0;d0fZ#H2vkb$u_rXa;0+YZdX87y0ovTt(<FqY;=)&czk@3ER=(%xSiN`ss>brr8K=oIIf%-0tyJC$rFse27KUmHKunjZ5~kuu0x9Tow+t*z|ixVR5Q!B3ii(bg=+?luZ$Q}Qs&0@l25Uh64kXFli{6me3p42@rcRkVKDg6QfBCGCGQ1J;%TPL=|GWyn$;?<MIXu}Aw3D#IA69C!~oS6~B}*745Ga)Fcntgp+ut7oEPPKqt#teaqNVi#M&Vn1-M+PmYJ&(#3l{>LxSN<YO(+^{hY9l?rjC5G!3E4W|ol)kAtz;%ZpF_rOhG}YDV8+jFwxJm51?GSF_?$r~h=R92*bE8di5tdWItG0*fwB5xf;btwxd7t<Qn?(GdzC!nzi%mkKeOJ@}wocsmq6bZ=9yAk7;CSXiW5yoWZD=xmzf(=g=bb|yG+bn+{UbPYq6sAHp6?>w^mLHvq2U16Xlx{=F*0o=Dh1p$qiL%djZ}pc?ZDSl($}>=Yvzs;-)3JsO!ga;p95%8B`A*TwBBRNr^}BfzsirsBD#+({qUz=qb7#D>riHRe0&Nxr4t|=EyGJJZ983>=G*1<nQB`-odO8LDA%|*M`;>?<+@qtX6XG-dy7oVjRn;E-WJ@^+3H`$j1uf5wJPKb7%wU&-}C;Q#J9R9)3lsehHoq6UFma;$^T@Ht59{2<YM^X>dJLbYxI-bd#zn~qe+-KM)iXhXSy4lnkV8^N4C>8%q{gYZ;o7MwHW@tSve@a4!V)vHsQVGfnJOa!#wBT9ve2cpc@I+=$Fope;y>(+1`k-I){qMN^f4AzjeSUVy8i|7cpa_BHdZo2t<06>3IzsRrQ;`X)uZj)K<=>eR;SQo!m+Uj{fYup~tJVu3K+;&M*Geg@CmVS~m)-;X76>F*K)z0L)~p77x~V;aadba#ukcab6Kfgl?`jMr<LN?9!4Jh)J`)+~id8V2htwZSk8Aa1c)&zprg&34iu$b>3)aYnyOxZG&+=nQz2Bg&i3ftPO5xoq1uw5vB@uXHLURV@!80PL2InJKf|Loo@U!r<+urZg%Fv;cpvptZZ)b$;R(qcisTB$SXdO*i^Y=Z<Vu8?F}va3!Gx=i6-^uN>h<AL<Sw~mRF#TG-+@RxI#@zQ;H6}qyyPeQfz4DA`>iJ>)Na7HHq5evU#nDAR+S}!kDzN=4`4r(^|A)%@++X!Qad4A6Pjp5riWJEQGm|VQDYX>d-#Vgwf8_Q2KcGP*ucLaQ@!E&M5U-2R3~Zc%lE)+Ztn&vhLepLLJ2^gmI^r&~mYeK?bx)qG+Zw4@PP#gs|g?L(?m?1F9xA0NVghNA9pg3>~zU?HXr#ba=@+bfN1Yd$SXahx!m+!<edy{S#p_W!w#Hn~?32gKy~^1(bgYTY9M>;O><-;+#{n-&L1&r9YddYsse}&QFrL?H_*UtC%2jc;zZ?#erO3#bI#?hl;dItIHO6*#c$Bhs<l%^McU@w2XBa8NdZgqAwK6El&=xGi^K9?u4`{m#1lyA<OC4>f1*kaN^GI`8;88CfZ*v>0wjeGD$kX8!J!3&42WRT@{31yfB-^s1ou-<7u_Nl|;&wTqpH1)uoCCtTLQ&c6E_@E+Cx-3Q&k8YZ;y8Pr$%t2S_w!ns$VgL<H7;cLxy5w#7EmF;0P4n<KKto8kqG6z>tH<Sl%=%R+Ql&STSTdgDNw4ps?<J=k7|6!*ffHp7oTz?7Ue?>i2r&02#{fW3O<{9<Pa_X};Z9^Q3^A-3IsJt;}9(_PF{ryoeHl6le}fzy-VU`gUiLcLR93A|9bqC2H?CKl&=cuj@2ddHUmls6Ty8GTPzlHg40p<Ljj!$|c<q=oJO&)%E-%Chb0L92@uD<UJCojZ4Pn|G`H>b<Jx>LizNA)zBNW`F=$AVUdTMzZ9>$VDTA0Z(j~Z6q4g6y+LNmP*)65Msax379egF+f6=jT^ui3km)Jk67RL{Z>R|?%ezAbMCqK+-ILxr}o{MJ2NtJ#fr6l&DW@&N+r^pbncUdIvCT)Ticr{-GVu4;^IB@#nPku&+3S8ejd?eR{QnN$bir|VH0+0<j&)e@@Lc*15pl%8-{hm&!g4`B|Atel$V6C&zy>W6h0>g=+hbvNTM8gBlO4XK4k!rLG9fQ?@ET<$7aD2C{U9-gbhj3$hhAq>q1IE9Hg6omK^#dQ^O0AE!m4Ny>U`DOMdo!lJb~Y_ArKKrlEv`t%E=k15hb(<$xJhM_7LMB8jnpXBDyazi2OJAV#xUMJ&xZr5$-bp!y?yY)nIn*-+`Z-k6zc07(rpeq5)2!p;R(sA1xN!T$z%Uo3n^6ej8l7{*R&A_%@FDkULoEr^mo3+Z>4SVN?VA;rWcWa3Feu(rpvEFIz+Sp20pb!lQFUQ?#tvp<~gS)PchOEtTNz|+BZo5Y5HQsm`3q`%_9|3fuvFzIo+h|qifm+OkrEpTjNT+JuGp2P$dKkiK-yoqjPnGU%gzw#Rjd6r%lh@S0VH-NWC;5%DELXhz=UV>fpAmr{zlb{L17U+lwWWhuaScF7y%A%WkFygGjcL@@4^#HGI>h&<lc_kWumF1zx&^d4+Vhormfu7iyESPgn9!5ORC|SGDlZgZsLbH5pjL7b##(f>Vnd|kp6oOd%jbWgI8l_w6=aQuu75&xWnIgOJ3?wruqp5UpP8+7WrH+AKrR;`B_Ft1oH}RJkjT`HL-PWH`u~c+R-xTh<^h=O^b;aZ>@oXoasRz3|D|g;tF8_$ao=RhNrHYAGL%I7<!%PEhxg;Fdpvuis@T$ASo5*h(5e%9&A^DB<W_@F>;=U|VCqM3+h&}&TONS(t_8}B_^DFJ>DKh^eIs?<~%#QwoRX8i~GIh0NGp$8<8)Fa>s+JlRQ|MsQ8Wv=_B}MrRtZ^pAYmf)-E30%Uv~;NWrr-4>9rABahZ;0XnwVhkVt9#RH|szX;jKH&Xju?N4N;T1g)GFPz>Bi^_C;P-he(K(bEQBZHTn5XlL9zkyB}!XTEB=NeQHq@uKq1F0pO6*xzJiKX~Y&UP1$gC+a$IdYqncQkWgy8D=f57sx{=V0*NqDiGk&;ru@n&KedpceyI9eTtoGzrn)<z%sVr82|}c4>;VTMzrsn8gOYFfhy&FTGXIn5Gf^*Q8l@F8zl^x`lgYe&j?E}acLzHjYr;FOHK_Z*C&YSV1EmR)eCKkV1wsBfR>GqfX=+f5NXfEcRj0|5L0S#$e_+Eztc)al1pR`xL{@q^So%>~2Y+k9cf}71?mS#`Hf@;qm6qbyq9#+`Th!zy_|7hn@Um1^s1*MkDftTEJv56zHF6p$*-1F9o8c)YDPR&oBulLqk;@gNy9#n&;KY1;p4rJJ6a!3BzfhCIGt^}Cdpfa`8{D(FO$xWY`iy7P<g?aJ7j6yc8NMr6Plo^guYau>`n3%$Spj?<Q+a@8@zV+*SsBy^y1*d|gj}dcd{+LO^*NV)u<mX~p4U3qS;@~Psru5r=`(cU$~LE&^<<BG1=QWOl3(*~R35pm`q>PnF45Quf8nC=C-q=JZddFJ*8au~j;3*bsrE-<kS7F;kA!sjZ=bdCIif$m2pVnZ<a5B;>PD5$*G)3wvKjbLq$XnNmRcpncvu`p5yq6iRmPIxkK8RtaX0%)<fnsDh?R4W`j3eeTIDK+y^teN=Zum^5p%A^N$lZpVX(t!Nb&c45Xoyw08{6HC7zh{9&wLo6@KyRNeyxsrQT}GR$wegvvn(73nML{#{Bl!T%(f{Hy_hBhSkAM3m{~<N$ZYZ|B0W%T*cnVIm73@5f^i4Zw#hiw>}4%3(06mMn<@-rW$2}pkzYIwW-0$Lim3DHoyKVd!HNZmFf>-iXG#$b^V5!X@|l<w?_-NV>p}<bIQ|}TEoeVNg(V$1jwvT#7`u6s}1%Vyf;elm(wtSJL7N~$O@%Vg}PA>#S`Lr@D{wQ3na7?U0RdbiI|2Oremp9+Ro$i^(H7h1SOdC7woW>LEyfxlNWY*c{wGh<@GowexLY>DY0q9b|e53kl!MeqK7?NPv~D1SCn5t`tGTxlV}v_BKDalU$Dz}o_lxTr~lpWguFUcNOtos^9=|T#B+gyX{NWptM?^g^_K+-ZYZoCny~tHfdaPh1X)VySxI$$=v&kY+#C=o;Cr<|!PwLZx^S0NfuOwCXwa}%N)xceqVYE<R`;=RmjAoW+yNK;n+l5t21Kjc_YxMxnBy~HQ5~fIJS<Aa_qY-kVQOCsi|E1=`^(6vGn|JN0Mfbu;8erBQU);SUQfDvq$7`SAreuKD@UF%yFJHMh!ma+kyZ??lgyt(3zWKxK*=yRxv87O-LTNgqi-QnV2IS8he!+<@?>a?AEWlD|35x>?7muIzpdCk+0O5m2ENTxEYm%^DXm1+$jwHu&LklO;#WCOO&Y$J8Ejaw3K`9(ruo9)i*1AM32Rl{FU9fC2tN1c5_aLaq7_3wZ!A{e6yu6gq$6Z@^3&YO@2^Mm+f_8bshez5C_4N&2*IY`ejjLSN7?in^v6<LB}qRqa7m(eyWr|*+_8?m!DVDYvNxFuTEd{F6HzUa!Urnnnei!<Rzqtl?pU)SESi|~AYM&5(16FyHC4oVEJ;zykBvkYs?aNt8v;HW`zBw;jkr%HQ@U00gH01ufsNIVc|EDIgV^2h>6z-lQSLZ^NQQ0nl<>gPZM>(Jhm4|1FEDLl7uwE_Jr~In+_7ZZgxW^kuMeWxdR8*<8iv%KNiL9UK#_1B0fZ?{i2#*}L{-oor!#ViKmDQ?;(K5juc5m7);!LLP4Xq4tHo{yWn11152ML@FRIazjY}i8NHW@uJv%)!TCrnjMq8>Otub6E`d~cH0bG$7v5B~2FcqU<Twd$iNK3=bB%2&#IHVQUa4R1S0{Nl*;oYW2PgC2Z3XZ%+b=8#qbaDn>Z<u(n;O^Y5zUgQFl?gPh7jtO_om0x4s_HDq;{PH33Qp)A*T&po(UWQ!c4+>%^~r&(Aa<-g1%h!Bf$j={4tU<h*`^E6%XZDE4a8<MjndZ=Ad8qRW03_jlFGc%COzSW@v?)<Tvm>}c84&ikuWBjs=VLo<$d(F1}f7ngph<}nzHs!UN07;kiW?uT-R{$1|RkIaeBRUq)7~6rPR~xSk1dt@xZ>FCE^PMVz#1boIv&#RRo$1fLReQc1n%0X@8v=CCx)u9~aGJBgFX}j1z%CEeb=sIz1Isj7Z|vEW2Rkws`1Q#}CV(El2QfIfp<1b^GUonGFX~4SN^cigp*;C#IPcBlRu2K#e-sXkOg7$qiB)w0*P_b5yLw<&>JE$jk?EYbFk(TO4ZAwfkG&R6dZQn6pG%V%lF#3FKb)^;3cxpm$GG0+Q|~qPk{ppk%fAIVCvD2WDvyu4ij$kjXU)R9f<ZS>kbyvy=}EudkO{GO%c$K{0LC1&QXZQcwOy6HW#LMR07%w9R#Wd^9qOeUk@{i_8^9r{x2i^LzkcTBmSQXew6*g<5kh|05*>U$2n=f?CaMT1{VD1sBgx+C#5M;KsECE=3TNg8p~WzopPW;wei`U(&ywr9|FoVm{HoHRIw|zh|a-<KCtzveLh`CKJVPZ~NDDnAW7{??#8||NN#pOg*RG(A<odQedPiXmc~3;S@ATKU+6Dcp&5pjT^=iwrHl7q8iH_siPV+hNVb>myS{*WY}nirnY*9W%VSwf*J;frQo_bC#U@)c_V8n{Nh)wrgR1{KW{ZbLi$wzb4^l;V?b~piH#_*$zEyU{7jyY=GIau)eoKgRof}?28DW9G|0JytE?TdxBE;@<q794eisteKlZBbK|R?!%(DJA78o1EzD}qeb@SjU>f+u>lBSN`2~Y{*rK!cVt*<`>am<D$uP2SZybaR^Z#>?Fy-bFQt|-RwWdY_U9Qt_YVV2P!WtAE?KAcX_A`i`Dv%c|OLL58B=D4DCJm#XgBi>?qL?*M{)&pY7mtf|7>apWxcU07<;mMs)Y2pdR!(Cty;p^`^s%dpWba2{E5W+2eLQ1~la|a^z&IbE;y`9I-tgXehZ)dZ=MU_ONuhPV8&`{PUg=TXtbq<oX$co)BI4Ns_oN78wz8mc6<wltct$x6dTd9?p&2#Wgxr*UAFBt`CqiX8&>sPWFyv-!RQ@lhKXWI)4rshx{Z|TkuTV<ssn*0(yGX#fooCRo2R5UxIsRvU=Su%>~{KCifYR?6gQp8K|uJh8@)NAK2&Q`H~G`Tl1ceF!O`O6so>o>M-P5|9S$7RLVTkE(qr4v^AW(k8l%bAe*)zfilvyv@IO};BUku6z~(v9tZa~UTRf2aON>zuR+wm#Hat>j#fIWau=)|S7&XQ;=XW=U@?)zz)}5s~A-PHZMuDc-Qw5}Oniz}-f`I8!^+73+iavG!fdULzWHWa}}Obk?f_G8vTBxLx0f3QK#IYx(wV6Hmxap(RXA2N|hOVMsD8XUV4?KLy)rnO2ns`o_*kLHk4&54xP_&#A0|oo-7r#zSyh76Aslo=JXi)`8=llvzxiq&7=-`leyeb@9tG_XD>F+oow97NtBX%LPxs@a;Uct>8c-Yv;FS*C3nr*3u(LNfnR!HAjV<OH4A)L9cHrP+{gIjV+-DA%_ssP67^meXl&44-1wV8e_t)oXL`mW=y^ZH}FZ9TXpFHnV+mX`kCb(Wv7Bw>Zbb^=ldUVvmx^LUdLs5&I9i%F{)miHNC7O9Pb)Es_SB>CVR`)B@rD<<NqYpB3S^HoQaxtQD9xBxAj^LBv^0Ut~bM+VT*2m9(=bUei3AX0B%h*mIDF|1l^(A;C@MLw`}TLZny#-<)Y^g9y06obWV-yzHq5}hZyaj|6pTzL8lrS$|DtAS3Z0(E)d`v`>jb+;2BT|d>J@wC2&amr1pDaath|1pGNbz2Qh#=pAn@{U+?O!rwgG+pPT~Xd`%6fN<*#G6Dwd&)#b0|Dg=K}b#MwNu2|(rW=f_G;lKFGfyrya)cv(O(WaU7oD&%P7YK~2dDcH+FXlGMqC}onldMZ(sL)h0X_Dbcs7b8~;h+ZeIGw<id|+J%4AhZo=PC4q8%9VoW&zQ+b#l@Ex33X1I4SAqR6A!!8oJx{6CuEzjJ<gLm2dVY9nbF2)ICpNT;HJ`M{YX5H=$&Cac=@m!#W;zhC{{xq%jV4fN$7;sRO@(0gDWt5G~vzN$qh1;_kx%6Gnyooi-{za{q=6$`?M|y6LOubCtG7=OYnt-NmHx@sS!8&foW>8*aR8GiaL(G?CqB>bf!98gKCpr(l{XxIgNP>smmh3pTYQWFijD>>P{#7D=?AEy)>d1;6Y-foi}mqPjq8^xK+#hz{5BdhfYUQAXCoR&XwWV`uExwoY-`78%PExitB@R16)6qn>r64b}UM;7B!zaP+)zkY*_mp5rIdm2~(=UzHEmLH#-8U&8~1YaV<J1oNGj!k$Ud9xza!GoU;?;@bePcn`4WN!*$ToCQ+L2mW+e;Oana+FvujeZIvk)gC@RQr6(nnS{pAIa$?X);(|uxdNe#S35uukO%2~Olg{uP;sM-+($%7gr%mu<E>88vK&1TqD7R#e9*K<1_U3!8$4vSUl)~)oO*9D2OGWdmZB+9AwDV++GalqGzTKy*uq6O5Z7C8!8F1$XW+mlEG3>tG$5t2;U;Ds2vTdGwfe_5%Gr)hqsZ&UC+EW&7Ln44$j9wNgB?u?9CJ%)bs-q__F1MT7OV&3r-_B=aP0(~WvZ+1Wyf!_XHES~a>xp($YKB^YieC9`X@z;{*;ZfjNtf;3{>Mx@iLy9HV^27*Gd16V{J+N_XBV;@`Uzqxm&rlqDxp8mURE%zoK^U<}s89-0#PFDknby1rhfLavs_6d{D^u08Z<pi-!j%&9Qnv)&1x6V4>{vfS;cO&YSl99U=EU4zt6{0Il2Au=>Hsqo;c>#I_VP9>uzNP<$JwdpGi8Xf65SN!&4i&w}yzFTc+s>Y@C4wusi~bwf<jp6bJy6Bk5yBR)<^6;14?V0{Ope215pQeC)NK=lAt;<BJJ!<<&qBAr%Kc39N!n3xJon@|s^ynSE8^SVdxz{cy<rM$tCrKL1Wr}XIS?sly2y<M8kkzz)5gM-Xg2bkv#zBp44QZ52ZB%8mpj3`9&(Fl6;nsGgNRkKkC9Q+%02UHWZpBm{KFXR{aPzi6T`@$P&*|X|apF#HJcSs#WO~d&Q<H}!<U%d%LdS)&CmP1}-1#g(CjyryCXOy_9&9F@H<3RFZ+Mb=EXGOI%In7xndSY#_UcGI^ReB@LE^Q<2GS2;rxnd&~B))jZOzDl9=$Tg-6=XRgYVG1U)5EBQGq36?U`!%!%Qt!%$9c~;ig@{E@u#<qcH~wQ=-=CMKnjQGPR5Kd$W<O_OVk_Rc4B_1(XHkb{)+eFWh@Q$#U<JFa%r=(vM;Oi(RkXZic#)aeLi-JlX-jv@+q^8w>In)K0g!i0_byHOaJcs%-MUFb2~>4-TTd1<>N0;+l*gOTII~uw8a3tcIJjB)3(mC;hCB1TT$X|(>6UbZR2y(mKnz~XL<g*^0)))%$@LEO0tsM>nCjBgss_F*QSrnR<$#T3I!YTVz#n$(;>?BLZou4@|(88$Q$6FVjc~7khG1vx6N4!)6UbjZgV%Ct=c`yEU&?qW=Of5&0NX4rZ#g+ow;AChMw-dMD<=fdF#&y&Q?y1H>2juGxIk)D)*VmQKt08*(_$bhS#(CxFdlnoy}s5+WA~=ko%tbd@#N4XJ_=*kKQKr^xUMrSc@59UM$Bb0>b5iTzt;!+@`ALb=C`>qVb)H-aVby<;lF>%=6l#MN&$WscWl6rn>dZ6MS#_gUm&cC<1k|VO+Sk)foe|StdJSp={sO9Clu#-vrBt*rYTVe;;&1W2Js$RcSoLm8>5%SuE}umRy<atqs8UhS9H9>N<w|cg6f;4s3#U@I{0*IF4TH0hVvADEMdAIbVLbQfVk+UMJ%b^_)0eSg1tZ#;J&zu__s&y7#o(I$_f>no#eBV63@upWrnzb%?^!2$o^b26r;{jyGx$wPuKcPwjcIgL;^C@Z$htME1)_pdJ=L(LxxLQH&0HBa36WKimjk1ca;9WW=`4vqEdJ2hj-UhI$Y%9&q?Z<jt~2Dvo4I#MV8T{v8mNgh#V}Bx(@OssJm}YdwuRCJ?gt;$(1loJw_M_&kn-2!}UNeM|T!Ukhb~BJ4Soan5CP%DqcV8l`py!Q0X&IT+L2q&m4ec*&mB*~vP-`sDhz6E<Klk;!CIndoN}ftZQ0ouy+v7bA5vSg$pwuZ9js0w`qrB&W)j8isYzo@=L+r1@Qd3>R8pVbM90hPK}uw9j%%gA{tv1Y2LOp;cOsVCkfV`Jo{6M#2j+ns4W}MiQ=$x%B<Q742w0OIrt?TWq!m?OlH9-T8J(c9I5hW`gclr*Zai>K`tDHGyuEr&ilVgJ#;)zUc<dC`Z4Np>9Q|6r0euPRxdC{*LyI7Uzk%$*c=BZ~CjzGrnV75RZP5?_Lzm)c*`|Hth>*sA^itm@m57_PIQPDA9Zkcx#QGOMC~v0(`m)b@b3m8<Ja}iyYG7nU&Aief8DJ#B(+83*e=1fK?wK|84hMXq|Px;HJ++LG$s1+xn<gc#A@Ad_=nc*rY7coQy00BqtHPeUdMclf(l`1$Ta=(8*~cP}>=qqi|Kiu8*q`ZX$)Tjuf2oP*<XpA#UM)2@i>!JE`d$&_&!gGa(cgkKuE^Yv3)CDM?qi+OLv~%nk7vlIfzDc{L2O-RKNi6U^ZNuSe0X!;2r;uIvt8Fy7?6QC|2m`hMfE^|M&fM5Roh7!&1@BMw4iLWp#5KuiS<HJqRFv)$e2?-EXC*Buq<uCw@Of=V+hT(oeWjVlQqi0kYK%j=vVt&;k6L|I=}-YuehhXj8eRC>EZg4Ny#3)@_VmX<Pc?PmDN9u0NSw-QQ!U6}cntlum%f>Df^aZijiUy(}Dkqm4lD3#T#JGL-$(_T5pm`d<1QqveTO{@7fe&Y>*z79FXbV{qJb55}e(T{Tl_}QrQtSlg7UETzH;v|`QZYcVEhQU|?b&0$eGWy&Q22QlDe2X}<>A&xt0p57QQu9XAFBi{$diZ`1KaJ-%{qWNWe;VOWBmC*%YaV_YiYpJphj|#@<L&uf{+hp$)Bd^-zojVR(?tCi$2Nbs&&r?1_8s4zUVQjY@BRCEY{S{Z;J?<x@PQuYS3eAmkTE}8pOqfYfA#P1@a%X0s^5vaa_{n!4&Ki`dG)W){|wiETAek{PQB#!>G@HfbM4{$OJ|=h6hiyuiLQL`XCxK%ZRwTPinLL6Y1a7#vNI(-Zz_YWUM=Z6Sj_}K245ztx_3cXG<jc1iix7^CgT$uyEFzfy~4lQ515cX`)6YJe*Lb?XM#xr>)&kBzJ9^WM_4~>cETz+U%qkujJYhIAHga*^SfeuSNldP8qGAU>j&qcE$3jv*c=CYAq4$AyncDj^2X(vYhMSQ+UEwgovJ<a^0f#rpR+#5x(SyjdH&4VIiDZOSZ*5Xa5i*4FDEvSynpKzU%%k;v}5aQpgw16iQe!R`lkaX;Zw=HQy+Q$Mf|SWic7zr{S5poWlQFV{Aqp+c97Lym*>;dciB%9cY5ZpFTG3m-IG7bOCiM-74OM+!OJ$+|FjH3c=oK``q%e3?d1jG>I=fzGv}xJ!nb(qpXOimFRXq~M&p~Gp$7SS&crs($zBGo^Xk1Ot-d;-8NKoM%K?AkY_DHO;wQX~+xva}cm30R8W(3fpX4%D!PMk0zkZt}&pqk<+3)j+ow@y9@rFNtcve3De_yW)j5F%5VF8*~cs&<s9oZU*SCTcaZgyvvJ*kaJPM<0Luw6LNx5Up&tQ{l_OK%o`md&>HHxk89yfNyctwLN?^jWsv0i0UwWDI(+BC?Ve%j1-$mTNyLTPM9>zd{gL$dKk2uYYd~ut~HmZ_G`Xh~me~i{r(6)A<OT{mEXxEZ_PfRE1}=CrJA#&7|KMTo4;PeT_Ac>2z33MNQ8m8H7ECm3;83yKa5&WO_?-ppvqKn)vMOw^eO5;Ib4V5tMo%VRcsX846Rt>lIBliBhe}j%ICqPn070ru{$mT5`$HGRV_b{J=){0|<G;$xCp*ka}{DCO3XLl4UYIz%Q&`z}q`xv7vR$H`XV2dYKRX9Y*55ev>;HLW!`7zG^;!ilf(udp5v15r=!442fv^K$h$ye&4DO&+O={U)7gOZ~by#xVRUG+t<UOZF_=>-+;*%r+XR&^DC;6&yF$2AP6xZ^Swm<j5dS5{{vc=J@IqXt$lR}IJa+~r6hV(iyiOUfqNVCtqgbYmR_w|p3*^YpFbUp20uw{14thrs&KLQzBFH<d`}GsPv)c?$?p82eG#r%Hd=V`k)ML8%cK1|mN>s!;(nS)<<!<U!!D(1NcqUMu1j(yIwe2ulSTp<fG^!ZLF+u>ijK)25=@=bM6`cB{;{#BX(J{co`E49L8gY00OX6^Ws|Nv6da^JIdU-s+^JX+Dc8(wVu^$*CtIRRXP`DrLA{akWx_4&sh*PtS#v@3CnOou=$aGyT4y}`wA|jC%0w!hSCrU8XPqqby*K-tD1t_6OpW4=;*5_bZlIVv42%{%2zuT&^p++3TAj+%FFZSsH+3G<XN{WaJkuLm?i?sDzJvAN!#yPjO@;<I*~9h%$q?Q|%Fs~2=!>S5KGo;hGKNR`0URD7^8tVjzAgZ{2W1YJ1YEZ?O=0R}Y0mp$Y*1FHK;X%p?!B;vWrMMGTfe=Ksy$NNeW8}okdD2ySqW4La5X;?UK(j24b-C!1<4(kxBfH$*S8}ZJX2fzi_hJ3?|%sDu+|Mfi-8WW#+aOdLY|xd^(sD(w~xx9VLMYUk;--Qt>GleKe-6B;{=d|^PUFQ&!9-MABP1(as-6LAD==<jK_8jY)=dsh|QBR%x3V&6TCf_l<X<UBD_7t>!1|?&er6)9K8~IZ(xwX^@M9?hn4=7&}2L3jGI}47WJGrWC89k03)<OP|2b!fDxQwNCvz=!y@Y=s5t;)X7_5yebdOS!*MLoB%Oo=!ESa<bO>f|YZwTWHg4z=TNbGCH;Vyz^XJ`vvWjCLDEz=hGCn0|{s2tYZZ>15-W0JcSeff8-ML`@V_IBD=&q^x_(-W(E@cxB4sF!|N>GWc^}|S|4S<;Im5&IyPQe6S84yl{SOVsowT?z*-Xu(hEzB^3^tVXBje+J_phNaXER-0=MAn@rcOgOKkW~$Ell&e$x=2;j=z*XjW@tqD47AM+HnqeWCB&ytAV~E2!S6DaXrybZ57iSP=SF)n6^WXT2Fo~|H>H*O_8+P$lg!AB7J-3Yp0l+XD=!5Y=(-2jbAu_w4v@7w>Bjv0g=OP`mW{btHfkY|vTskz##6Iw?3-m{*DM>q3jQZomW|UpS~hmQO9#+9VD#nvFVeL!ox3*v4qU#dGKwr4f6y!&Q`2pk%^JU?9{(?5A;w>+@8^FYo5ldQx_X!$wo6JtnQoHVH2TG+ks;;m(b#!?wb`aInN1`0t_w?<(d*0=cgv=c3k{YGOt<=tFe|awtehH!oW5eySU1hx6`Mv<ik&$%rpEKlE2qZPoErCHSkkO9(K9z$0w9tqa=;uUx6B+*h765)OpGED(CB0b0l&sfrKCQjx>DC8@1K}8#+S_+leEII8_TJ&&+dyWPK_9!n^&4OdJB9mEE~H^%SHqVhwqMGW3iy(bA}@yKB#CUzH31R#O}`MPfz2Da}r-tT=6`K?>w})&UboCTtQ81R;s6$gNnkMwnY@IeZ3Qp?`bT-CI!`FMd*7Kn{SSSjNKH&rduOV5jRl$A5hsk5TsW*$wAEQro2E+&snF`@YZ&a-idfxjCe{t9V4Fh&k;|h^a%L5N*;575yfg88DKPHrEdvp+W$f1lJ(~QSw`faaR7b?ZivUa_r%1Rg#@N%y2$vL$?JE}lWuV7YI0mAGXCk}1Sj&0EoP#=rsSsT!g^D;#-qWz>t4T`Kx40~@WeXO_-M0(o;cW#>v(jKHAh<fJ$<?ln*oa{Fx-g9IMH?nBi;}G0Qo-|)#BjPp2Hm6bo7O&nNJDZ%q+iNyp7jBPNncLKv@dYd4kM9*eS!U7mpgk#VKj^<zIFGsh<k94<21sz;Ymc$igwMBQ?SKEZsdOfTfSDFx3<I%s&Fs52Xl(uYUA#L&hRkS$AjEL_{3<78a&oVRHB%NhluXVycwMB*p)Lc1r0$f1VB^3Yb_~mBKjs@V%k=CUQDLlXk#%t1n#xm>X)$VoowZht3DIkm{WS@>hMu599}1KXN1YPw_xnS+>6Z=*@atGzA{KUeK><fYEfov3Nel^yogv4IH<q*%%#H{kAU|WJz4^l{{+&Ebquxt@Cv-KEburuPxEXaE(R~Wa*CgL+%Dj4fJDp8_)XdP*S;2V=+7owo0eVRk~S8!Hf>K&6;i9zn(6@($l=+jZkb@IM?E?yoM-H<YoXeDr7IXzg)5ej?R39{7e*pr~_{7;cCVwKNnI@<LgNPjw%(JVz<w$b*~twc?>ruvgn78sx(_~$M;YjSO+Xjx?T=gn95jP?(A+D&UrOY?uN){g+fr^FW0+aH@q0IbbcJ)60nrF2Q2=OV1z!>H{sf?FzXFqACVSg3fH0))F<A`oI!Gj3URWn8zm6Za^kD*2Hpw>R9WvBXXnfN0OG*iN-u+dqWviE1H>Sv3b5kCFk0!#yWR&Dtqhio;~QNnF0&GIA-Y^xCEk3@TOp=D>wcSJLqCT!GfOX71>?v1y;&2lo688@ok7{egUTQN@t(`QOXg7J(pS`It5>8>-p`ru$kZpF$d;2e5Ly0eYMumMDY4F+i4mj{Sg04@QHi%fMq2(D(}@iL`pZlz@z?0)j-R3{%*CZXJTkk4r31AD50pAB%$u-B_e2aeX=j2<bhP@>*uyp+zli6jOzNI5DD4Y2*bT$q`sqi5+C(xSGh$PpY7o@(b6fi@x9U#KY3n&KE5xVY)#q>VW#yn8{>;0nBh{auU6Yu*#WpeU6Cg3SLHK(qF?S>ne%3|m{kT1=slKF+g!)$vQBm`j8zvR>tx}rh+vBaNB@~rhz%JD1>N--t_hDG%bI@Iw1?W7hol>a{EOpXvX;YTlyM!}oR?ls2kfiE}K(3IpJ=P_XbjhC4@Cm}SO=5|$<UzOMWG<{YJk2aI-TqCmV(Y5%JIRXeeSaV&Ha0%2OI@SHcJ^Ic!-{x^%?U=0NnsqXGiEB~wJ^6%VP~E;ygssP>rn4PQeD@jgPWpFR;kDb3f96|Hig6FZ)6a{1g<^<Sprt3%|%Ca)I<1ELtcX!#`*QGsvq=I?I8<yCNP7(8Og0d7EOBB39tW2df85mfm>3ONv|7CVg1-DczmAJ*8|V9<^?ks9JBw%QV;9la^m2yf7tpy;vawB;{WzfX1<%k8=#KfJ!ZcIAG!|pLbD^<`VDvBStB42fRNcDkp*ZOL%mPyO;X=G6epR}DbKeA>ykZIceHhw#7=a%ie@ChR__>ck05f#hl6Q@@%Or|?eHlzGC!d&gE8pX<2+K+^$U&`ti}j=xbbo+fY#Sk>T7&IxrzHyec=~PJaG%^DJQG9pAz|i7u6lptp0tX9A;gwk8<8u4{X)z;q{SA>-G4i_%WX`hP5;up0;}?b$FkTa!LzvSedyN<siV$G}l4X*EfnVY{<Ekh38qq*NZc<hMkKu7UjGy=5IPnU0VQWZ7?l^&&z|AOTi^u5}QI85&?b68&zp|)4p4MW@^G<k(C8C7@ul`UB*2h*{WyyeeMs%w2Nto=_erEg4O1W`cRuO7i68zPu07`BAcl`|H$AY7~LH+<<2Icum+D7mmqc#HbGGcy5tZ_v|#8c7r$GstiCR!xNV`=dj~jYl9>r1%o7C@PCWR;SSkrL(eblT5XO-c%E5FhuT%2GZlwI}9L_o4`>&kTN@93WxW>qa9Ur`){(E4YcNg=Yt6@i%ef|;s<T@yx;!8t<7c0fo+F~6P1Ja0k6;4(KYII>b{&{e9iOVp;GPn={8Hn+BO<!XeDa^v94+sUw*8mRC%i$SGITj8Eige_dJdB4rn`C1$RnpX%j0o}`PJLD?Q_lP;yizfa#E_`EQc^CGI0}T1H24)>;I;diK~eC=Hz?$}*Hb!R8IOc%bQgFo$mZ%Tf@r}Oh7$HZn#Zb_6}zNN3iUz|&=^c?InE}T;Cm<VAMb3*P}STe^rmhb|EmiS(;J_D+1D@}{~l|k6W#GVM9lle0zeq7d_-wsI@=z3F(Iwv#PaVbk6)bCatpPB`y3`-&!|WRB{5i0asTAz-)Rfg)KI08TLZS=x(J6|l-OD<idrLuf2qZhDZ*3d@vfWiF(jY^jUTbiMok31mtek}d6IS4g}DGXz<R~dtujfs*-G3@MWASixmLf<4)K0Xq?rJDM$ujUh*$^k3pQI|dD7`1tO$AgUDi^^`dv0y&8TI@njcqq(@M<LIK#~yxzU8j)hP+JV_upy0O3&YA|jC)WK;Jn1VJ@-9UQxw;r=MQ72NjIV{7mHYtoLLe#GKwUD2t#5+xZMrJto=T>M_Te}D!#<YQ}G{H5!5G@k4H=TlIfv5xL^3|S!Y0{{iSso&Ob{XJ|?@rG*BN8Zc5RV1y^{K&Bh#O~8Lk-y;L#O(=@<o?DR8a<>!o3Ect&4mPaLOrp1{Cej{6<H%3vg1Y*HK`v*UGz?-4Te)k_qC*s(JAid9cATM5SU09$jp7}3Di4%;<}@Htssv*JAb>qzoh_HeJw8j_QxcaQXutwt>_zwrF@H}x>v_i$zmx(6TX}13Z;P5-lf|X`ulIVBV@X`zE@B+M^qOWnin-!rR_&h*>xlhkP9YO_0Ia0_}bwnO39D0;|q|Q7Fwx<@-d^U_YxugKsSo^*bjEEjDGCi)(HMkcL^l-d{JFBsZ{b}Blx+S<MPh1ImKVzS&Dc+ryJ?jiAK{Q9^9F-tG_6-GToTVtlqtA#_<kP#Qm9+tMMOi27LOCz|;KCx&PdcUtk7xH*TzX_anXpYLQvG;xWqQ;4#vN+wjq9aR36^LiauQ3mp0pC7-cI#t+n=s?R?nGQTG>c2_Vj>Wz?D89LSV@J=;31+uAssOux`=Um!OA+fNWT|I{4mw2qdkF3vZ6nqhT_9*m8oF3Rac#y47tWjw^#p&KhtJNYb3XeYDB|@z51$T8TJVjB!!tZ~F+RGhE8IdH)0ChM9PpFNsaCSPcy3{Ybt@i^LfI`Evy6OhMh4sf;ot@t5^%Cw?a*=CA&6{BmrsCs7Y2kFkSWv8&DdY_==MFtqjs$waFq*03H&HBdG6rdcO9B?{dXRCf+ai+Kp<dlvw_$Bregt&g!Lq;Mz;_4KY^PuO0K>y@_xcFY2^Jn$1$9x36Fg248J7OZAkmdj(R<$EcAXwrVu#fW>ry8(SODs|!${Nttbf#Cz;?5PLVX`>FwnIcUG9NO#>HvlA-*4Mb`E|dT5vp=%?|$hQ|{lb>wXcMa$wq6pJmsh5WId2Sp81{iT704T}}xD5gmts-Z^v#s#jUY3dk8`aDGrrof*Q0<cPuns(ZizD-_UE57hT$tr<AMk#8aBAZ6AyHuU;~Uydh^3=<5lE|B+I;zzQO(ddm)Ks8Lfj;iT()a8-UB{M03Wes*~q(eX*h()BJnvO_;ni*ZRO0Xei1fitiqxES!86&C)N@7&POzVvwLyk^oNn(9tri^fB>e_TF1qKxZm_!1IH2vCJ;Ysmy_&u-oQ*pzi%v7+wA`N)JuD4eX_z0%U7LcJ>=h%+K7i`)`M*khUI!Bq4)=aE7ztqjWlP5G|ahj&w$&N3Gra>eZ4vwF96d+`K4BP!Z3>qgji%wwx%rwM%(c+>88z=BU+C#mf_g2nOXo)h)U-?=txEYp4*IjT&Mj}`3nV(wV#uvSr>;AuaV$9qVxnLwUncY)3Sl-M7%k`{WGb=UcBi`-{cmW!|XU?~EMzRe?hvq@%l$^eukhfWTDJw`_q`4#wMxDuM*EM5^{2<s^5eBsOwoRzBgt(Z4H+M-05Xacq&r#NYvl(;q2PXhCdG-k9${gt@7^vCLTzoC@zA;;ZCoR_}fk2!s?>?f*?H_+9liNsxmbyO<TSBP^`k%nC6b}(*-5D+fw?Ak9c#^j*nN9?nuv$@5*nkEhE0@DI+!Zl$qd79@Exe8i^+VWz)j5U;DTVtzUN%7%J3Nm3tWkDoxDI82BW}#PX^G25xd(XdIE5VzwSoVr&oIoHPcK;|l`!DJ4SPJ?QNc1#Jk^d?y)3mF{3S*dK}LQ@>EcI)Ke60MhnGfZ7X$wn+)R6UtFfl!qaVQdK^diWRD&>119ot%!GXd6NxtR4LxRv$i037q8mMjxY?J64C>%}9xg5@PBSoY3$D3d^RMhr~A@C>|TP@BvOIu0>bZoPU$LQ5c;QF97v+e|g4m&vw41>C8%xB&M_rf?!oPjh5E-YMOP=Lb2&+59sbwWD1GBiTj7`IJ06a(-jgfTTT!oyx10|$?}61AbhK8^QjP?NWQt-Cv^14YQOlUF#>zZ$#X!K*n753<0bc9L`iP2;Gcz7-v_p7|erJ%_UfP#`$c3vUeWSZ8Ko)2`$6V#8j`R2}t6U}41ESo`)pb<*j`aTrMDYl5nYjs}VMQqmRXUFV<vI~XH0nRxRh>l$~?sVTRvUSpO+?&$%sc12P!i2_65RQEu&ckn59j!PyA{+Ve@q1OkT!f$O$0)z8}CjU;BBliL^07;6<_#b+Q0rv1^0Xz~d2oCTqJr08t^bsCSN0ft)%wW*8H3lZZXLY6>nOD^nhLz2HMCo>LGLGcN>jb$+?TGxs`aQ_Ht#99$QP*a`HZn1(uHTL>mdJ~=Vb)Y@PaR-msN7(Gu9Ncn^9yd(%)vRIBn!PmV3`=g4caKwS-y$%m#rU{42yDW0SDgrEAJ3%5%?P)U0vfQ1}&=3YdNn+l{;-csYfU3X1%9yY6n$-PcgN+L><~kj}E<FkIAeK)}1_du@KdF9f;y7jND)#aKv=!x^N(?Mp{z9^>RfCJAj2XDbpQq>Hu$v{NU<m4JVOEq8BHwE;aX<Rj}N{r(p%FD{9>>{BOU{8hj!c<Ya|;PeKcBO!93ytW?fyq`CSgnXO|@qJ%iR6Ii^(QsU1J3JEc4Q}j{IP+~eUNLYP$gv>;V0Ep`6#9uE`WZ<5Yx%zH^bHV2ig`U=gx?@N@a7{4nM2(O&6D|>AdPLa>IJKEb?{VQv)|u%W%nX5lh3i98Gh)`_M3oxqLf9zwN!=Umf|6H2i43V{Ztlv(l=Y*s2D-4i6C7!y->a-b(rL10Rk7vPC(HlPkc(V>>j6)JrpjAXaUL{`Qv3g_Un|hA_rva)K>OgMe-dbW;!Oe|AA>)SwHc3`*~cd|KC)tMROtxoktcieWZl=}3EW1vEG1u=TW6t%A1Ka@L@m}9qR?5mo#t>`4-;%(I~ioFF_>TnKQuddMB+i4I>H4;W0VZ@K-2pccdKhvgZDxHS?FLeYU-D``&J7YgKpZRn7l<U?V3~kAeu^on{>_?!Dv)$=4>&vaJ!xl5XL~fV3X!Z0Y5faxV>A2+nX!3XyW%idbs`HE$gt#HD6e*=22vV&Vk|AWAlWeiW7mz!6Elca?~?doaj#bgpL7r11DpHva7qCQ*J#?0<Ezu<IQ6t({ntN>s}BJQ*ncf(cHnTLFOnDSTMwUVq{lX2$HQsAo9GqJOm?`t3cua6BxNks?PwJN-#IeI{drFS18_IFN7IlHF|K=qty(mt|lWb3$&g}3}qWleZUh7peOGT+Ofb(^#SSYvvG!{KG>7^_>sm5f#d_P%mO7<Onh;EKWFgYseZ!`?RmqE9SV4fq(!8f#t)&FX&b=L2qsfwI<Xv4q8wORSz+<7kdi9_H+AeeJ{lSCo3sH3=ZVnGzx8UA2-h$4+v}z(SjYnWO9BHN`7WkFA*t~j%dI6#nY5*&G!yQycNo+aPu4v@j>iaJ9aDER0kCo#xf>7!s3+Ml7rJx0mAEnw&TV|W6*4(WohB;EVUw3K8>~ws`iO)CD&rD3RiYC$c|*otlbd?*kff`Do_{!su8n#Hvdss3INtGEIfW<u79EpPMWnYnTP3bB|D`n{J3hD}F2X_$GI2)B#zg)pl*O{Nk9u*Ml_#uZ(aarY5iIiqZr~xAdv}RyIEU>)Wl4HI2h%u{h7;?87>2IN2u4ECYrOSY2{m7q(gvG-b?J`DJYuksC{jHZH$kz3VkkmK79+Q^N|GeHfgGQojZ|vjpU{%_su$NUs}rkVWM@`%r2hm0S^Aar4%9eI3&iFUYnnKxWVt9RpNjB6+{U~R?v_^0%Ii$@kbFXBW7<~gFH9hJOq*hAwm>@y{P1RD^NX^E)M(_UhLF0j%oqN*Z#7IH)45*f4GHvTVFGK3XJJCd6|gXYj*J#2FoaW>Fmzt{9h5k953j?7F34j<mv0>@<foB>5EVu&(z{fcJC76+T|OY86;)55<`SYy8P#-6akp1(uAW6lu3I#Rtff2`Y8-);ImZ?zh+-BMDHx_DM|WA6<1G&MAn)q9uFW~nTIv%wE9NF-@r=0%fs?oTh5C;jEcpNXwc=)!8};UO7Hwe~Fg|EGC_hZ8t|Pe<`4Cn5ECX!;!zsWgK{Ki(n4gWhnu)&~7K!`3OovUIEi{WNI?lq_n_CfDkP-smRh@X)LDX?(emXvLaV9SeG<{qhtt}t*if!23^!)TNyJn%&5KC+-P)e`rKyA3zAd+Sr#FVK>yDT+7tGM#@0(FSA_8{dh?i9hDd0~OgA62i;+5kF1Fu1W5TWhFG7G&j%&~`LSrW9OL28*UXNO{X_VjWl(eK9CrXagHcJ7?LC`zI&gQ)U3mhEg6A>}>U!ctaqFClaM&JI6HTnjIWh#wKtF><Pa@=b8Z=nqDSU8<#J*`UrCy8%>NZp8lyb*w@UNO%gpo>kXJM_OZ)tdZ^pet<h?@Jf}^4<t;nRiu@iV?TS-=yk+8;;{6e$`xT>x$9sm7^~qaIle-j$lbcdJ9GJh<7o@no#Zp_ENadlf-4E`@1JZSmT_DwTY<i3j2gjH~u(?z>sR?=`@ylZ(-pkR3JWO5u{zRHPkB0KjfBk;d1jMn|cMU7vVAoI#jLed3y<}h#;lyyV(MmyCEu0{eFE<=TW|M#_dDp?}Mz}9nR<ChyiL>+&9%iC73il2GTP_SxgX`xe4XgN)bcr%B!?kHHr_FbIOIpZ)wVVaaJ@6+YijQ3AlT4yah><uACJX!^-iLL5k93s`u8_clk3QfK7p|i5dgk|0bG{!L*ZCKppBG%BF*W9Z;&f$R<eSx`P$)5QQV6x!se0%r)Z@$|(k*Si(56Ycm?rh@JH9a>YB--JEVCu~K+3fbS1H-7F`)ChKJ44N(W*mM<^rK7y08+K?%O&RZMh=^xw)YA=MjgOcGSG`o7SU=gUY+IX8@F#`*ka~$>tRq!kM?>%7l=gJ8_;Cc1wIqI$MIUm><TKDCue`mi~bKq!^L1(AYKksIanO441N|vepbVY_oX2KT|&q(h%xqE5&wxK`;%Zt2N%yI2hL{K2=nmH??AC-th&;7x<ytKg=39m_Y2x71ItLX2;%H+qK?yyyxm_OX(MR!hL%I)bD+_hRlPr)pjDNPNI_!#2Kh%aPNeB98}VOu$2_u3^I>FS)+X|xfC>Q=6<nZ!_l9d*5WM>W!9u>i58&SI`UP~54m%uN-16VV+~%}*cs8k5cX=qV$8<Gy(;PW2!zsutEp$canTzY7H9KEYC78yQi@PAHti4g6mrJ)eB>q#l)gtCiIUEv!QfSc%17iWrQ@;%&a5kFT;ZnxR?s+Pr+=`<KMLYWWo{%dcx9io3R7`1%2*hy4>IB$6eOjA3dpMApcWXqy^|Pann)(3jX~_ueTx))=~)EzNtJGo>RBLsTvAngmwU#qJ$Au}9+b11NMWu_vB*s8Mm*EwNzCR!%B_qb^<-UP|CetgS?r@gGi{My)s%f?^=k#;P_md2VB5m3nsOn3r(2;olB2#V)PN%OelBau5Q0Ms3hQrNLpZRiq~K=0=Q>}6!W)yTu;@#!l0_~NomW9wGWJLZF|t%lR#}<N6D`810AN|`&T7hc+-1%R$~_9o2jgi|P!}MO7}Yf(51;DFb=_oAc;k`*Hkup>=p!y}uV6Md7Y5}W2#~#-MI)M6;PzV#CH~sintBs&gV)z7gd2)rBn;%za5`|e@h?J$*6oZHddQ|8>0oE`PUs<=2LVKF-j%a?hherE=LAp=67$7$<0VzkVpXJQy$n_>bRz>mB#T%~I+2@Lv{kvhV}0CTz=-M%hbr)3kYcpohs2tb8X0geaW`0iX7mtM422si4L5{XD6*DfjSSXbfwcCCZQ?#ikIpc}tdHL=`*1k13Fd7A8fw9&;nW%&-`)m`CB*-pw`Y5S$jW+-M+gvX9;uMW!W<H>hgqcpsa{r|2eE>9x(%Q6p8w(zcVm6#^P`*9at?eZ@6nbId@)P$HDjw6ABo-L9zs+ZfLy$Cg6}elAfMlYA&5HVEoV9gIDXl(_qy;M+mrSF_Xnr*#3p~jeE#Bq+IM|&zkAk*UbUljiAJT{!R+X#En|M%TBu*<tZ*&@g}sRuQno!%-sTDgn$56Q!Vp_oCYfc1TN{8cu`UljS9Rn!O#&ouJQZ-j5@>OoN%h!4qJeFkLj99BqhI@}RubcOX-yOJ<ir5C+J(|Mj&AX0F@PH*v{MZh<s#&YX31{G?8RxFP?=at^$7Swd<;6n*`<WF$QY+3__sSj8L*$LG(lTHFi#WxRoB0+3&E|l-`DQzqK{g6DzYA8&43WM9+fCW)Iz|g*}guQB?}8Z^=(~jWujIrTK`<R%||bh)j4UJBr4gu+fF5^*lK0X{(Tnep9SYlOTYaLrk`)s8%N&Nx~jv0?aUzF@<1(NOA@ipt;n`)wmAmZwA9SUosV~a@sr8%CzIn(2C<(Wej4FVBm8NEKRFzKayb6vaQqL}!|=)8_*)v-Pu|9#yp6wO-o~>ham?>xZ|tu<nc6SiH)C(?Fa3=5*ZKGLd#}10pV5O%^>*);3QfbRPzQ+RR^oc7LC#KTw(1CEG+M1NiV#*L;6npG(JY#~ZL5?>CDrU^hsB}R$cE9cZFF7NP_fVaGc0PIEfA#lx`Jok!%xhKpFPxt74FKMSSFD3YxJkHPq}vT(NIpSQ%&a{z+vTBtcEd){Kc)zeb0=3FT9G+zFIJjNOx)Idtp>;zn3Rp|B0vanK>~UP3dJ@;)_%D%XC^s_}r5?T=A%W$;29WTr9J>G9L!BInpQc<6N4ZiK!l>YUzcq<qH<Y_Du6hjVnvkwI}iV_vamU!wbH=FI)Cr`BQ$;oH#u1^6SrEaMhXkWpCOSt%cv`3x>CO5<g=|eB~2Yr+Rjo{Hy<3uDJQmli|{w`0SZ*W~saK)AjM}ApXfgp1Kh)(2N()|Eec3J2da(E_^m7>0RFV%tSgjZ<Yv#AVQZO&;E()^V1<(SKJ#a<EaVp{FANbvqsqOe=W@9IoZS8MjWRW2n0*|rf@hyaiwJP*9V^l)c?`Nms)X>1_{{8yND;t(c}uzZgp|GL8sLI1i>N-5@u5)1ZqPs2=3tHcoTLR%`dZ2$iCdT8-@=(H@)zHvjXF0?@MvV+++Z^=w9BBZrY*C)|PETJL++M@6sWBfS_MG`62_Al%~`SR2(TJK0Q1(g(6@yDO~yBzLJ7y0=_b{Npwsu--fTC0utlBBWfPM?-J0_fbVqSNYZ{08@m1?Or7WV_B5otjW-M#!3f7eAVo(`bebOHfpmi10Zq7(f)PDj>*5F(n@~t#0TAv0i!vc#x(9ayk!LAdL!2g=pEK{MKMgt4z0W_%uHDJy(U&_mO6^}AGLUS%I{1B^D013~l&y?$Lze!=7&aNg&{VGIOy$6^S|nCbvVg?v-sCj^91_l+vWQ{CSWb<vQy$p(<bY+`2~ypNGw%@xfT`$#opA<ikzN5nB4tXgmeBQZhe)lnJ59ihb(%T~Y@)xR{QgKz4`9nflw2w~Dz<}5WR-9NKHN9@OcG&;vonC-9pEp<8)M6(sX1(d;xw}1r=(!KuMLLFbwHaFBk~{Mf=oVtpAl%G_D=zj37`q;RBm)5Z}8Q9F^vKUX;FzM77FbUOw&Eueo{o}062@jDqtv3W8E(@GFiqn3{>!QXOg5H#jwhw`E4f=XemGo;MgV#kI*&ogkqkBHsL&x5kAr6d>$%_9qf8uw?xrY0P>*ZT?)o5(TJc^!bHIYI^dyIS?~OMZ6}K7)L|>GSs~WJ-Z@dN>slkW;HF8&)*B+h?iD|09ohPQ1pWebrMQww0O}*v3VaWx)(EpoDmiRr2uS9WxMAUcd{51c;Tqm$^0B)F)5aNOO)<4yXJD6M&B%EQvfh&rOVJ9!>OmPy4P;%c5nKpJ>(I&;cbigtbbjkNK!q4i0Ir|P@6FnKm#}M_0)$r6>^M-Ib>&(xH0{0O*UX!G^`L!F78EwaL2$cxdE*Sn7C_4iAH81?*%B0tWUT82k^JtuYTT{l@iy_bdN|(&f^PhSHp^~&_}*1`Rl`>GZvks#tjWTq=EH*H+Y!D=`2Gq>)%kK86b)>hSziqFWikv^Bxqjpj)m-}31WL4?a3)k<WCcq+0J#H+ZDX4PL@t&YWj88xex~kv86rujNyjf*WT?$EMdb2*A0?OMCW%$AweiBOyo%?SPZX8T|`FMiMivy^1%jd%gj;YUD8*{XCwC|`G~6X<nChpxDBQlcZ8co*LQ$-l|j}X1YtpjB#yU^F1e05D==|kbi11O(1ngmI;H-aUQvBfIZ1^QWKOEaAc&y{8}v4{aMWvM+}iB=O}NP|h?+++dF`&L4dI5uzN+QakIBRlVnpiz{@TYJRAEZ<YB-CHWtj1N9i%7XB)>QOK5ppN!O)pz&JwJENJIUA8XVwH8xC^@s+0Q4vN8kEsq|10%zhbZ7^rsaNB~Ml+2IlJcue2haL3JrW?vfGn08?w%qKMwons?fuje2Bki(gt8%ydmtj9848%XG+3em@Bh8Sy<1;4jA7I=0*qlOj62ssxFUf9>0I!gE&Cpyw<mT?Al*`rBD^qv;?J-2h){_Cn?_jsoX+JhUn4+^C)ev#vMPlc3B>3a_1*^ER0`!9XxhOhyev3J^BBz>udXM59PEmB$uyxBPm@k|Hrv7M)Coe#U6-Rvd6^)P{9Mrv(+$HtYyxF|r_BXSSkZ7?KUEKz>jV6lu57CTs^<M};)1K-bZgR$h;|BU-*VJMmCXz<ifa?Xe7!~_>bmrf7ny=M8)UGwmv7Cd6L2L$J^WqWWnZv5dRy(V4UpDa44bLSS41b*{iiih=;_4&{0K|X`lP(9k_UYA5!R6P{=g8ZQAKnn;)X}=4M2KWU^3pPK*4OM<1I&`8L36XRsg3c6y*FpS@av~ES*2t@GLT%xnd2QlcPxXcY$pNWxgzP$y-!K#1Bf=ZB=<Mik$EdEJ)ZxM0p6kOMao-d4i2Ua_i0mIlZM`Gw#(cm?ReONdXae{<<r_#)P{7IY>zc7hxD&k!puv-rkrLFhqCCXzoOlfsen&Q5Mj#lA<Pz>p8~H%Rsp)UpjpZSQgh1>A5()sjmKsjOcFW!@Ece`@-g6yo6TI%l%Y9WrZ=L>iN=1u%W$f*Sf&0QazhIEQOo<X8@#j$QgD3_vLR+BTh)z1Qltf%g0fa!gJ=7j3S!5o6;)Ml8!km<fcmYuDSO#KQq{ue4iBFn<q<+R(cZT+CgqW{LikQUrj<)rOMKn^XR~_><;XIl4Az3v(dQZJNy)i<9a3vRsJ=i#lCZYa<FO3x_iu?HPH2$A{?JfEPimfRldEoL*{j?2YDO807N(B?j)6=AGc4HU~R2#EDCtJ6FU{n?R_L)`4!)<uv?_(XUdlmB`92TWkLYdqn^P76teV-DppG$Y-7Sdt((*yVj`5wYF5Fj{lCX&2R7xhOdrf~a%%t=gt>Qw`91Ga=xEFi*<aKRX)RMNrUvx9X5aLKT8E3W3^&}>hx%e1AV9$n9(RXsPx`%rZ3Ri3FY1Mv$vVc!7XIDy0|*kQw}n?EePc-Tx?!j5-(4Fu|2`X2m-j`~@}tUVxlvP<xOl8j-;QU-*VA<j{s30<nWD5B+_t91|FJ9gxH8nV0T>lp@m$ki8vNEPu)X2qr8fH-np=<4R&;eb6)U`TiiQryC4z?R@~=-82S(8<?NInZ#XhgEXCuaoAlyjBlklk)d`JfOm93Lq4)Ql+`BmQej6n!SEj#~BkF{GX*UaWI<F9~VOvJ?g+ry)7mYBp1k-KrI|vH(>?p_KbF|<q2a&E<ti!m?7C+C&C;UO;oa#pffBQv!(6JF_Y8y;TMq%?SNFs6Qkec*MxXy1t1AUByAxNfg*LSB#9Clb2d=K&^PgWtS{uWm}*FD`frK!t7uA}sd*Bj50MQsuLd%m5#_AM|L9Ltk`pvN($_CgxuWA2<Yy&o_l9$Xe4-#jY+d1GvQ+%y?PX#Ic&mp*GkKX2_>!1v2eihik$;1Jt`$s^)lVq@$;PvN91gz!<F;wnA^o|hwWzrewc4ehD@3Vqa)5yC5(h_C3G}jTDlKOl^0C=b%P6RBVyZ$Bx^J}tugnbQLy;CqVr+Nv9D>ebkcdDl*<rt`-!)IHJVj((hYlO#q+&Me+ij;E=o<~|I1U`N|FQ2&e(Ubw#~$sHgFZ_vaQd|S9rKQQlw)0wDYj{`qGNFztD$@h4pe%rA92&8SOl+#zxjzn@QFk42_5|D;inP)G{T=o_!EcV{U3%;1cFZlf=>j3PXvNb1cFZlf*&&iLH`dXf#5Jx2P6z@?13cq0DY(AvnLxTHvOzq+Ee>2(mL77JslOmjYHs9uy-#fmCm5$rc50dAp9DeKcn*P^=o3mAVlgF9ze*3^bdJ?0SYZ%fXU^R4Zr+u&lphMhy`v9jbGl?t5xsTM1=WEok8XW(LJXf7^Lzlh<=9W>-fnx$h;3H<0}NZ9Q*cs!zG=8{pW{)b{<c^f|M;UK>aop?QH#QDm8zFnI(|cgXZM?Ie%qcdV70nr$kc%)^=SoG4AIX3GJ)-bD~32?r_U%R#)weyD+T3uf5X0Kwl`!(Jr|Q-pC3IeZim87kIH&^aZyjG5Gl)=RAh%B!;lUk6-06tZ?@;3t<Jie}6)Qf1cCuK5ty$;aA}BZwI`;_;D}r628uRR}7e^Bo7JnzeH=eO5J$-3(EC@T2m9k6X?BfD1PT>PD6MK*uV1LaQTeC%5?~D`$jLbRo?53*T?D_>EXRkZ2tN#tj4W-!hTprm5qw?6PsTaR_D`xInz#U;z8a#*Mi(*p3)%x@(0&Nv}WH6BKlXocAkppLj`fAqdzv#!b(JcPn2Xy&NR`V=;%+-(O<;rXhLB6w?N)EcgtLwuVo}scLi72H}rH*j2gTvIHIZH78t4kPqRQ5+Rsb4Lh=KnsC)A~iFpTv-d%&1!*-j_KlKfXUa5iT|9HSAc?=L#laEf=$~^82pxf8K4zBOQUY+$~UUFs2rf#I+*?;rxxhBY0<U$CulS23tA<TNg0Wn{MFf)*^W=pmf!b}pvO!O*}k!ihXo_-1GSz9H$&dK!>A!Ilx&CAfV2a`fr$xp%-!CbRwxaj2UN5@^*611x=Nwya*IMDW;Ka;}*fIXrMSZM#DV1-dXrzbti%&lu60<g1`g3Z6EmfvxO*B+afxj&x~!!>2?o+P3-mgWJU!d^QNv~nYC9$&8ecisoS-w_jk0IVuA&NtV~5sh#Pq{cMjbOKc#H7`;}sP7o%yHzhxp;ct&{ojSfQ%!TBGifu7%Sd%>*;yXyL&kVvk{yz!WauNH5eO!Mb--ae*z&PW+PsH4z6*3=b=*@^;U~EO7H=mk2V7YYeBCjG%Ns7r9i2W%XTqd7C}5|J<`zzu(oXN#H5IM{WLp__HN19r!1DvF(ae|_25C30C^rdOxk#1%Yk&Xi*_P*SX5Opwx=jW|3X6uVwt%&at^Bj48Ym50!+3OdOLtU`Rq7+RK537~Ym0f`uxDX~J-gJoZ6de5RKzKAiwmyXo46LS$8!f2YO>$4!oQos?KunM@Np&czwdto^EfkLt<!$;ae_CXG|=4_-hJUnH*#Tupr-rjkbZZ8a^%FpodBTq8>UN}x;pld1TGz5VB5MHrwErd-Z27f)M@_18M(n(sb#3%LZx@*;PXbNCP|w}y#$jtdxL-2yJG2L%LrrmM|wtN{w$D5q^M1}HF#r(@Ftp}Z)$nf8~7vw4MeD+-+53%JNW}J@RAc}hR=e}MAOlj4D)pC>x~k{oRWvdB+rn#cojbe+^lc7H&J3ClIe_l2oY-iMm>Ds1ly^9D?K!O@!n3pYv!`I!>Sq-@%N;P@vNf2Vc#dxCvj671vnvlN#0U>xYY+L{d+}Tf@daLM-bkQC!yf&!F(fF&Av7DWWC%Yaf{c>8dB*@DSry-%^3E{R$-cU<EtVO>f<jlfN1w3{`51_v+tbdSnkp<;o~v20+~#nSD#9s;XZmfmDP`|U*|^w25-ELoX$<gBDYv&0D3vK!i;!PVW49S-ohJ;=K!dB#N3w$-j*=Z`UT(c-lAOoe3S9BzKL7ye|W!5`8u$l3!aQi@>N=0y%#$LZa!WO+(fP;CT`8I3k;5oS*KN@xl@#xVh21~pmDU^Othxs3*>10x)fJlR|VG}rWA5(2p1GPO&ngs6}&hR!z4S5tylv@iGi0bA(QC4Xzmf6E#<M^#p2y=t>OpHO&SUP3+6LK$|2M95jx{_mfe+^h)v4?1!Yf2bXLh(G|HFIj8wXhv3&o>by}5YtOh6%jQMq><K;1eaGN@E9&Slz=XQq4HG;ZZ<GVo?vk`YuCau;?Wwl_yE`YCb2<>Dn8L?Yv1$6b|WW}dsBM#gL{T`s<++#%>2#;(KU>pq|QW13Mo;!XT=tV;iTb&ELjQ1wjW@Rs3Vh~p9ysZb^5S>T(rMzyn-SY??=bg9ntT8tnoWQk(FEM25=^8n^+=;e_{k`MO2!BDWG8-BPcM}%V)Yqtt)(3LG>dl=pF<MJv5=Yt^L=G3vya*T{U4d60S*XAI&Iabg6Tgf*0hCEp)LjIrY(!!8z=T_K17((R;GF`1;sgq$1dIp1{Xoib>YLZbz5Fuq@KI(QN06R&wvOOhWqllMwZmtOp0Q5RV(UvSE^OLF2(@Ft2IJHiWdT$5)=nOu7+_1DZ69`~9v?~PgzF|T<hS*F0Hj7@^(WsM6IxupIbTR62eER1%1@kr@`4P#fQ8l}nPH(^IS&Xi%+ZH;i1Dvk=8)(%QWriPwP2Dt)y<^s&KSa2Fr^*Q0HJnahuQuKdiRBehApQr0LSuguvQ2c!;`2>L5?_ZZU~DX4_2r8(t&2*qw`a^3vCT7XZTP=u7^gjid1O7MaX}wAN&8fIw;=+r{?V9xcnMIO_F)nYdAH}5^DCZC)9+s8}t)S4KiSq02-%;LB<QT8kRL?cdt&aL*WX!W_UMpO_W{8eOP%aa7>J7!@iK(L$U(Xh8vx~bbzE1RsBX?S#xdFLIH_djGGRr^Q(-)@^^rN?*FW<BXzm_^6O#Ccj}v+ts_e`CLTkFyue!tbD>gmDPb9{ts}FIoOd(49R9<|6gp12*+#BlK`C(sFUQP6f=~mpo+Xdeu;r>d72jek6g4=%SiBg<KpR?G$FZn2^7+lQUPsJ_Q2(~1eR@Qq_5Cc7)unN7i%6X~cdK;-VjKwE&7rF)*4sqbQR${G19e$R|HA9{MoA@s1w{f$-PyXWHWu!Xx2?fyR+?-RM`M-1(Yvene5|{8y|BF*OohV%zp2>qNM9+`-e^Kq7l^vg)x9W0D@OjbmZy8ChmU#~P^F@LP{^}~6?RKT58_DO;rXxhylsZ`;;oC+piqf>IJf;c@vkQ<i*dC~`470?s_DA#6#G3|uP`2I2BM+bGTOa`7faoMA5V@hvVKFGuzW&H-GMw7CGXOoU{Q?P_#-y;GKKpIuemD-v2Pg&f}Dh$%6(D7X_#%PX(fz|Fw`U0jBCe$J#ZFwWT1dsje8`({IJJ#DG47jaueGz8{|rBfy>AmAtX;uZufv4Z<nAf#0?w2>>R2UG*Lx<p0=(?eI`)gL^?QsLHBsReQs-d=VDupBrZE7peC`>mfuz_hhB{7CY*WqoVQ2(x?0|BBdIv!x=pZ<FVW@KYm4Ko8d*`x*cbymcNPm_>7_*9Hklr2PBAAa))Tmi1$J8eysHeJ`I48F6Fj{<1e$_eE9g3&TH~ruX6|Qyb}XC8bqXsI>ZfG5BXU2|D>b)h1NaOEK&SdaH;xo?ydXB;Cr>*eb@c0$_y6I0mbmMu{e;o_Jl)pnMJ`0PNbS<dku(yQ0nvuhS8sl|up5Fsea0GDmsniG9;z<$5?%+k4>Vj0ETypZ0Aso$e@Ej}^^RslxXu_GrZdb{$kaDHPyIj?soeyIAg<{yFn};)Fx0)b^?dq}%-7y3q4M{_dT<Dv$U99tcnN-Hj&-P+n_w0@VZHP#4hW#?@ZA-(o(lD%B0Vpa7MepJtKU7sJ|p!ddO%Bbs4k}rp`F#e>k|E&OX>To%lk0Dld8d7>)u>8C^z}p?qu9sQ*xBK_f}FuYiI8#9m%xv^ggd?8*k2A<)c?AJE;X}T+*KA%P4Fl3-ht*_D(1p)fUT)c#14+K;TN2m|Xi)*hoYSsXFapvbIlS2rfYyiGDDvCFVrJrc01E=)#*jcincz{^`byTTT_}Jt`SyA35K3=;8hPQfvrBgMD7_K>A(xEG^VX3RQ<1R-~P3wkK}Px71a5u<Rc@@vU@{P+%(96j?<Qo*TZP{Khq=phm|)pCIx43mu>0t-YQlS-)ZMi=%a<_)4n*3Te!#gsce=!&4Oj+r^e^U9mr*)J4B(>|+HdfI?MbrHe`}sTm^GuNSNfK^sK8#;cVPAkGHTCH9|=k_7ZZQ)!p*BuCRc98JBWWLu~GOY}cAIW?3_tdR-V@O^Xt0k;&m!th7I(Pf&Hf1ZkJw;lr%Q7SM|wZNZ!Ob04nz@)t12`H|s(p;K=T>jGS>&|n)wq1{XV)BT}$i(tmU(<TrFo@1n^+0PKQVfG$=KO(YjhiG%y$3Vwq*;L?zCWVF$j%CHGw9wiI6&8=CJg-CNgU$?1+e%^yuDtK9+=EMW$@CYH9U<dIe~VG)7T>EntJRi_)~p8i}Xpc7J5@+t|xmzUwmI!vVjN=HUfq>Xz>~l@xL?;LG2hB1B}_d<)W?~#;1F&T~w{hT;nH5)^XL}uqN5mJW<4vYF$DkIGE;~O=2`fCzv+Vx1B3PYJ~?_r6Lq9>^avUHxJ~RvfOmE$|x7|8^(qpTtk)v417xEo%kA@XaMUxTTha1?9LitluZlNL!?$5ftz?!-9;J*m*I%+g!ZpV2X5eqYGIoyAN0@iTon1aNsB5@b*I*Ky~teIs8c5sHYZLoA_kLOV~BtkK=8>_l5t9SJ|w-E*EtCh2_k!d=w{T^OB(?zW5>{UD@QXZEJYRNWJ$Ky0f)Mp*f&beN;th7ZCndAGMBiw)|;fo-8Z{&=I*;Ep(B#Sk?TWRrHV&`F(}#^FDmtua!+}wwHkeNU5_<)ro5AhEU`-8XW%hP#@^BrM(zOh{v1)f5;oIEyDVls-ka|@Ug4YK-Hk20Jr(ap0bYeQ3~K}OpyDJfNu$haeWGq;9GbG-!M3cX_~SQl3N(ZXN(jMxLD%tN`l~-Kco}2>*YGl{4B%R${YBJFTBBwZnmh&02sP7dQ;ll<Jw?s*Git^<>)bz|1J0<qZm!;~zpe;|2BBRsS>I%?b#xqU;Y(fTW#CEmd4dcSzD(9=zik?u&^p|_TbKRgR+`dZ|6230uoV7r-DFD(kKe~lwxK>|$cL(+RJJ@TgmO`cnrlp4x>-aU)obHq1OsxRq>x?&d&H;n@j%H%<fT^m?4zrZA`uMOkAyQxi_j1v{KZxlv5&yuz;b2Q)TTN&uNlgoR)(^-W+)rJTb{Ci$tLFBho5-6*j&(LtRcYm3VIaM&18Y(b#kW3$cD;}J!#Jl+u7n602JvCp0xpHKicCc(h@ttKb9$JaI_=^5pQ;;y3A2C6eu*Vm6&(b`jbkXmpTiz!Wdj6Zu_can!9n78EkL(I-)pIYb_43cq^nROt9xO;0i**C4t+3%0LgW^L~x$RZH8dpsv+S=46h6Rv4^i64X5^3Z@{?A!*|}3O&m;8J+%c0)UG`qx9cRf>WJui@4qY+(pHZHGLmXtQbZs7uL_{9$UH4dyR%lj&<+t_BbT!hBqeJ1M%~EHEs!SslT73QOn|8fRO5d#Xkb=7~+)NRKn+lvXzWhvML6qHDi#LTMUKUOa#krfB?cufwzYrH02=a$kcSB9`HUe*GDShdp?s17fgwQ<G5F&3hMRUBg0MYi<$KerVDi>o%u;bE1?u-*D5K7S=t5*OdMsSY-&Y#%_O{Mnh!z`kj5M#1S*aPVwSj7btagN!lh)hQ#3;rYj^#rckXjeb>DkN`)2oSpL2Xk0mu3i*5|BWcz@CAT=h8@?VAO;i~PU8=ucQl@uJl^T(mlo_FJpdfIEruH^X_Kb4Stcv~G2BTFp{8#|GZLM{kZzPUMjnea_DMoLq$2>cp~q=Z=C0{cS5F|KjTuIiK{KwL-?5YilDpZA;-QEn75l^<dnfcB@cw*URCV`nmPLtG!xVQ<26JWjcxAauSEaj!oJMG&Cnv8?|FIs&l^eFr}_nn#D0L;l|8~=gTEMbbx~gTMP?<I8pXNtN?V(PzENKOxM}v$6oD)jL6FMnC;h_Z4a0)UK3U4;gqsQ7)7RLV~E6CNZ`7Z8iO&IfV<XM07=;F5$;F8T&wV+#_X)d#X55Y+BEFZTx$qz4oJ@gQRTY37a&0vZhC(aYi`sT{&vI7|9Mfm{Dqgx<L6n=v-Q>{;11B#MSBzdzudrPmswA;RRe)$r@{+svU9kJx=mCYFhv{YtJpKhXfdA!q%k%UNQcD*r8lC>*fa>NB;bu&gFwyb8&RY~7r$@VGXfZ4B`%5xXE7V_%3_H_+IBTDi6d98)>*ejM3A$vL!FO;zmbJ>%*Ql>A~G=T>WLCnfdhD<XjKgSFE7BeI9XbxF`PT-3W87S9W?k^Bv-cp9aASArkkQkV9wc2G2FwqGu^%=JkE#Or!F+wW&q<W_o)SvlYk6s9W~phx+nWo!<l=(_vL(_O6U8OZnAX$EEwl4o75lsR+OWGl)ex$4{IUwfpvK4M~^H0?KAyoDdur#i6je~2Bo3;z4j~?4N;pa6z;4K4wRF|Hz9N}KvX&oyikQ+4R!VxmF{ZjO+-?U&@*&{$;WR-E-NYQPBJ$^;dT~|-_4@Z&9vcC<D9DT@mIekjqbP_=J>1v|IlHi^I8`;L5Dx4MX9?+#mGg%f>^>BCl2sH$Zj3oOo(sC7G#f49^~)0#e^<`!`Gue$Z;-oqYbKDh3XORPON3!%)O<WSA-j~sj%`>nmhj5kNw~UYuKW96M@l4tH8*}BmFXv$@pV98rpm#@ve-kx`#N{ZK+9~j~vK4EAQ^vk2_cdX2Z#Od4qY0;Vc}^;Vbt)ePF*9Mnl;@+3qvLRc&?Am*nTV((rO!X&1Ga5?<c+cNPT`JBu1_#HvWstX7RIq8YaoGj0K&Gj!(Kq696VkB`#zf$l?wD&MvgLOnpHc!ja1&x>mdf>YxH;sfBlCFI=BQiW#OqO_hZhHz26#{RK3YXN{59TW;}lHY)CP!~l#gE(~~{{?3*4u~tcSu3<0FUy##8m9lKWz7G`{g&^3woRM@h`4W>9;wl&F+29j{IPZbbrJ8y=Bp>#L+4NXlR9PMLlm+A^YoxS7sdWWNtj&dyoD*uc9Qix!0Zj&8OMm1;pW=XF{?{f6sH8Pf~g&`F9D5eChRO}$h9ChAZ0!obX<m8_fnlv0;`WhgE-N!0q;6Z#E?f5v;9h>z#X#woD<oE=<EBaqJZ>lAPdZUj-WSMAHWC#jZj$(1|~1~f(WTkCXlm9E&4u0eH`2)cBXR7Xe5wb?)qDCBH7*3;(g~|spVXcGo%cX7oVB11|t#c6Iv9klwg(F#A%?bsrZ(D<tpo0S3=f9Sr7F9^Ga?e2KAf7hUc;ZG-K?YsVVCp<KYALcf@J~Q$7S2$&Szw5{vp+RCPD>y<LaYi}>N9LBOPG5;`g1#C96IoXQ!kVN4*pDFWz#ywq&$N8fC4xh~mZlb7mB=zNnoj#jA)eo@t#|79ff%_3IpFV{w?5&jSC#LN&Y4f5)95sPH$D>wNbR#@Dk9l+kD5dIj<kvE)mHT9as7M5&D7g|zG-fa68!H%y*DzxwD+vnQ&$i}hGwNZM{QPqRrX|J*GJO5tymz||~b)J|JWC|C)kc$+85KD_hf(jYdf_7wo8Dh=P@Kh@lFxj^(D30<n4mQ*1yTyMEjJkTe=Y)xm{CE2IUw|&XqfwP607I5?PScHzv2~53TUVd7q2RPamI1e8UPaa>L0wq)UD6xgTV0gbO^f<W@**{5iC}Ot<hgib28QX3i>r!c*ZPA+&din_skb;YZ+$`XD-6?J!#VjIP^~8;*3u*ER^vcSz&!-2ee+s@a{6`^^bknsi7e>23DU9W8Y=KleqgQe{q;O_^Y%RSj2e<yC!V#!uhmN}j!+&Np5&qFS{~XzUoX{_xn3_lsH?G5O0jmpjb|y7p4RDSu_pa_20Evoj6{If<wYQ-GyaLoFoB}-kzce%{fP^HoRZbzg6nBHBP&N$0su3r?>O)XS({#hpMcV5!cq#i_k7QXEi_1W))Ki7M7^{X1_OlXAj4FYv{Byno`FUnUIy#KPSW*^Bb5CGIJu@xpl@c#@)Q80j2Z}av?r{XnPEl!zxx9(DPi>SL?Dz-0|NZ@8JcMLwyHampo$2D>F-0@?B+Joy^cB}LAV}ln&S>!07O^ySUVZg0Rovu)WEp!@vq;V=D`a*DKl<FD8`$iF&kL%litGR&Cu?I<Yeo(kQ<UKt2?2*rgM-lNK&k_>wZw@pyLsaFg#PyFF#w9xws{8KOA*G{GE@|{ofGvcE!Q(9lQU0KCnvqr1d{s>HC*g_WfNvYyCqhkT-Da{>v6i9z$y16Wtuxom=<)&uCEHH5wFk0K$Dw84B=*x#OWNEf|2B{&?Plt?9Hi*>=YWV`yM0-x(xeU}xHx&_Mi>2k`<V;3*lZXM;f<5sn7Rx-g+rJ~wB39|IonU(`7}JS7$<07(xXwt@!|r|JS&A^^aceUF@jjaZzI+~7O@(xATsvp_uDle=1n>xSsXnbWqB1Oec?09|73AnK6A3&i4vMVgLu@nlOwf!8pq-dOW{wRKn{phyi4wPlB3AUrt15h<DQVQb}+ct!eesKFL)Z<;bEZz&A%!Fc6NI8JO8Orzu{xn!^=1jkD0_HiNM_Z0xnX179UoWIy!Op21kM_WQ^ykteC+9K%i5-18mKXS&gys=;gEi{Wn>6{ff6r#(tG#UGhSXhR*$cD57@t!74-jZPa{2SKuy!l|n&OH0I9%y#GUbeWQpska9zEBy9FS-ItOmeuQR%5D|s@)V@y!;HJ(-z~HW5&j+X-imcnl+uAy*UR1)2yBs!`ew**!fnoXqq+FOXB2G{2;bXaqCs=YzgzvFJYx2N+e4w-*jA(4Z+^FinZvP0t+=2OUr7-)+Ojc3~D=Km>B8IvNZz;D%N<Ko1C=UyV~S5cJs%qME!>QO+U@VxBA2#ac+)P3`fO-Ino(Y&Q0+knBqZvu&@P{iwz<3w8l#2Lgmw7DQg1{0r3&(2T!JkJy~uM$XEo#R`<x=IguIHb!<*1z(B@5xdB+YNCzb8&No>T?5*`q%28n19&{4i6Y{GH4DISX8IbUxN+g;HYeu-}4PuLpwua80pNoq7&~p1Hy1#6|%a0NDOQdlz)^*QMR)XPz7=*j&n4BnW#JX8x&$v&NgiMcWp9zfvS;P1$0t9<;!ic!e8**L#qOB}#bIGP!p-3M0<$?Q4U8IjGfz~$Ej5?idE<v`Q_$uH`j1;a2(A&yKDGT`|lVyaQ^|(#Af-&W&FPFJ-1PlP3H(6O6sea+Wn;Cc)jVX*dNZ=t2w(^HoaUy87CD>|RjbY=ZVg=tj?;A?Ha5sq>RB8bt$U;TCUf3b=WMH7i7J#HOT*Fc@4X)<~TV$#uu_7wPYb$6lifC&%>l-u)4I$5VUii4kO_^1G$q*UuPb3#1v6?;ycGw}Bl@(feqi}TE8C5_>2B~5yj{LX3R<N6qgS<nq+p%O(*Fp*1Jl!>jK(=7FM3o~E?9zaB*)oV+L?NY4g5Gdw3;!Rb!4>*i4Bj<%hOeK2GkIN9(cY2Ik=PNFPO4{qMbjj^<4glb;qS~AJKs27Yq2@Dat*f++dG;H^Rj&ew}iqht#ThB(Q~zxw0(q=sD7)X%<S1J0<p2Pl4180FLQ~_{tn2W{eL!FcP!$5@d~ia+(7F&RlDb8R2yVwo~n(aGQ(jFHRGi|Hj@_V*6lSV0bp81J@j~6$u(IC&;(iL#@Z7$NNH%WVA9>>yi!4cs(k?z6fstXa}{^ffHt#?)7I2hfk&NjGzZ2tl7rC~m~k|P9KZUz!XK%|6rwLJaieNuUQO6AM=Mgb-{K37P37I%arCj2wXb%)WKB6{k&RWdH03mH<%c@J5;HPaz0Y2loq8cKd0R*BLcb!dXKu85aUx%(UeB9gETQ<(yK{f<{pa$YjiIkGmpi@p9p>_CBJaGlhdEiEo6h^WS`>}{u8&r$uVKQ3MXTAuvom_2L}q=#7P0k}8NG$H1+fEpPB8Jx)r_V(f~T`GkI=<sMk~f#PwK9L=YVP3U<n?LckNSnI=kJWK^!~#h0MJ3HU}zP&rJ3~3a1?`KIh54=ME9l3UJ0LAFoaM?)sERcHudxgVzd<`QCr5`TplWSYPION_qEcN;$#v(tv3hXy*mRm6lK=K(1KjHs5Cs*NRmh5DNjdC{}s5QadJFG*P+EN>tLm>y5FMTP((+gBj==Fg96tX2~dveA}%rn7IEVg%CzD2<iZ)4eDQglp%RyJ8_tB`^%(U-0~XU_bYCBeJ&Fb)IY=30|xHjyDnkZDou}A(2&rb_)GDv*rbcu@`2%qdV?QWzKco&$Q$f=zK4daL|+_tVBi{2zvx(FkV*YWwNf>H6i(t&qU#Avn`AVhdF=Wfq;88BD3#!&#2!PG#;AJLBwp1?$g}F$oCbN@G4Y`NvI;#!0@2)8(}eG3i`wa|WDOIUl*v+8g&QwAJG7<np%f?uof4#1rCp|RXNqq)X2%dRQjbF_5!&KSF@UGhSzU}dAmt1G_1Bwo53@P<rcO%g)JcU^{@fE}x+h+WuK2E}3>_vqvQ`3l(E_Y5{azQ$V4D(bxc7oww`r=&g%`Idj*z5@+9fj8i2CI}Gyg_Qjm5K4&!?y5cKv9^5d(>bn0iU15jbZ9(CK5O1Ym!N1AFlk6{4GecIa{bAxXkI#RI<-84sb~AwTX8XiL=Pz3(Y-3eXZ1J$icv*T2`pNV}AO;<ds@KSw3{M-*J|Bm}59k`os<<AeKxnnmSaZY(Y|2|&LCl&v&vzjS0FzLU&iOb?JSDs*nAmJwlEC(NqPee53HXC#xyd&~?hAa`!VvTXh8J6va{P?N|NTrp-(grPiGBI6HC)V+K71F!zNSh<HA-kZJ86GDM{Uc<meSH*b}#={YdF|<D^*EH};W8b|O;=+NbG=;|v6)B-?hywJ)BHw{)b6_hoH-y(csX6sKnX&y5^P^C&D&J$&r>4{qj<S(KQ!r7|Y0qK;-zCg}iT|5Bz=jb9)glHVCGXaLHTFvXH@-b4^Qw1L7mU$*M^Bh~S9?d}N=vWh()&J0vEX_lU2jQNFgkyg#yt0quz8fZ-pYEVHI68%h-y@)phcB(?uEAe&79GBM>Nop)n}V3a`abH=nL|w?U!TQFSQNx_V;UM3Zu$p*Bn+|qYMR5uOcifHMeu}Oi*BM@z_Q3oUcpheQf=_|LdFTYqkc#ORVOv-Pin}tY(VsX@;&@&CZiuO6pSAdWuiE&5dh68SAh~0?iEq8jxJ4H*@MP)3bvJ8X&qzO0c7Lt?z&utoof$@8o@x*?%LJ%4TR?-Ey0uS6iC}LFuhTM_n-g+%{Fai>d0vo-n75H%I4|q~YT<HUGpr3qHO;RM}q&J{l&XZ!e2}6W>Nu5g>xq`AbYhTB|)8q_aFrRB7m-#8lRZDwpV>hKXo^2orq7Ge%Lly`~x~G(_EEM;24FuOE~eAmZkgfQVZ|L!`gF-uCkg+x{JvmA?M+nag{{H`JqRSD=82;ng9fpc##HyzC_zPqLZsnO4=kW{UpEB?bb|EMM1m_KC?DWK}4r6O5uRXT@m)68ElNNjXGGI3t04ts{h_UXV%mmv(xAGMe=QjtOs{7@yTl31Tl0=&PSwKUM*jRXpm!Cd`v?>`?I-A@}CD%qNBcUFltRzsw0WNFl7X28;C?{6h?P=-^P_8j_sO(Crz!$+3=aFYV|cyx?AtUG;*oNcy^5)}^5aBAa3=By3^Hnb5QLf_DzdvdYNLkA*NkAl|<<fwD-1A~xmUSMRzh`TQexYzp>^(g9^W(Rm~{;(0oyyHsxvn&)_s&Gmb_cPDSe@T8dK4om3m5O(#VkM7Y!!TN`2yF(H3#D<)|g$Lr?mNl@a{>6Cm?RP5GL}}rA*d}=B6NTl)qmZ-lB>kiM0R_0wdl$c~1O8e3tfou%lr$oh9L^{^zvrFR^G{08$I&nVpC=nmY(w7|G-$#S{@fP2>)s`{%brBTb5PJ=Fw)XmCBZdgr%Py%eM)hLKaJ}MFJryxlWSxSHb&N4C^r+ewIP$)SRL{Q&E^t0Z=pdt#?AC#)h7W_^{iFm*R7Hz&f_jx<JS#4?fhoJ`XsWoXz~rjWv6JN9x5N{qFaK1Pl8v^1$<4!;aa!kTH`%_7sPCS`oc1%T(gWRZ?lXM02BOSTE^t}wTyW);cAvmB5OBwPh4YuhH2l0Ys`<HxW=TFYs{C;HRfj`8d?$z)mJvxnBK%MvOhD9NzFJWeQo2I*o<R<BS@wqiW{2tF==fdll&>Z-9ZMMRTR14%t5AHILJ5*{+roE22#Q7u_UWu0yVJmk!kb=a{O`s;UnJAM<R*)LQxl-vK(Zt*~g%p(7a>%m3NGcAm|+f;}|Td*?oS^I3|8D;}}y~c!Qkas&@=wpx?56%<y^=4~Bwh0aAIW?%3EoT2N>ikXYiTKo0II4?)IJYgx2)XU4}!k6tVsu7+giD4mEBzsX$SAsHBytLXkP4hqVM0(S<61m=3z>Up90N;e^g(C9K;r?C%poDwRndPoQJul+(6kyML)T3RdX7@4MR7>h@6(AQj8AaM%P3)Nx8VKSd<k=6vS;|3Aegq5r;jIS5<L<)vRSdpIEV(~fKH*42a>(trjCVezjdc*RKf-}UAK7TPm=IqaY{%d>jOaKxPMd#+sWSC8UJ>-W@qAt!~N>iwjge-z;NAUkYd+!n}U6-B*t=nFE@2XvO>eQ)o`7iyq?QYxcw!7VGL4=fVgb-sG1i>IdNQ4+<!XSbHPK0pCsG|^LTef0^2uKlPLSTRp7a<TN0)zqz0>OX~GGGufLqZ@0v7YC7*S^%{ocg~1yV&mY>+92X*|jfguf5j0-uJnf*>e4lAI7M;G3yXxt5(X65qhc(cM<~$^@rIxQ<iz!t*<mDH}Zt+P6eq6GSK|l-*{_%#!H2ubG(natJ2nlTINxcG@d7@`%2{zPvNJnqL)g0O)y9ti}Gc=MrKM?s8K^tdA`w=Mn5HHwpw*wRX5WT`A$B(R$hKmBv8PE6(0s&3Po@7Or;Uhqoz;<oKmP7D~1iMDt$fX#>Q%mL`p>#GCQ(3+A7pYh)^ryPSt8$U8B|bYj*e6K78xz5fwUbe3PSF*ZQqOLb_PU`ZF8sjuY#CBv$!hWbRQLRk$s4WZ)RI5;dB|pK_Va%#lI<0iEQcEwwl@?GX`mj1cKug{2F@@Axo|`p~`Vg`qE_F*&l>&&tBmL{kQld&&<n`qyV{At^TgCAysK9Cn{FavrEcBCF1_0PMUlW+T-K>Y4*XOJD!mGwCF6wYkR(IDF}T?%Elt<7~6$>oN;9ln2wgCURc7t>ZKW*QaSm^#_Gn_BOUn9U$AFyxr=iPBMaS%3y<cu7l2c{0^Yub<PpijUWRvg%H$_Aq?b@+MuPrFq~REcU23CuwUhN*ma!g99KT%^jGZ_>g<%G4dfmo?2NP|gxc7~fhwpXQrZ}wtOp12rfrNQz0+nP=NFvG#dP7BIMDVA*HEF=DRIR<O%b{liOp3qr=3aNAlbE8Trf>ap-Lmxy$OO~n~ndJcn`;B*Ns6&T$oL>(+|guL!3=_b)s+r!q<OQR&hG{YLl*FUYhLzA*DR%gp!v>LJf1KhNVVvQ2w@_TN=-8_M%x#Q}$IFKcRyd34gVHqAY&u#`8nl4)r-lZvjcYfcoSb{IN1-mY4naFAkUurF(}mlYHCtEzJ)Owvf?!2O;0*=>9ikpTYu6Ny;*@bb>Ef>AS@L!{GW+qgH$cQ5%xG7qYC3hXbl=_f0UEvqnGC@ym0z^`^DFN!3{rz!-!EaNUg<422O2Rc*NJ{4*L$mWML!Fzj>`6D&8h4YFFo=={Z6b~dDPZ{5w8UT|5N@_zBTZyyj#BQ^Jz-IZfj8Lhs78bn!Y8?Kh~!9LB#CJr~8$>}RWWWN?<Qv8zGh0Q`?%pDVh(@jE8WwP8PXFORw*frt`(%S8v0ZK_fX&X~(Ynb5ZvYgpi-Hub-Yif%2sAE6Ds|u~B0u|1+w9PE+q%#4rue@G60efrk)G<cIheT{876K%>FFi)#j=ePWeT}h4!A2Q0H;80X)l0;U8YRU^&UaJRt{$#QCTpkIQUhYv)5}?!X|g(Wjw4!HoSvBRV#a)@?Bd@x9s$F`ugfDC*bzn^L6ib~wHs1EC2f_?v?HW;X7%4YS~F<lsDVyD!A#WCa&co^VCku#oxoh6n=ApAvCMRGU~FhTRN|2gvmA;^M^<tu58BGJoN#7kaD|noQW@L6qsSnU%ORSuAcis%y;R6rH3)(%L;3Snr5l79-5?n?Ajn!&%MXba+Lkz6Vlmk8=#2`!>~tgQg{X8?&!U^nQ>p>zDWNt5`$gA;>boJT0%FuOIzMu1i2u?;|MqKIfQ1Vz*|r9s&Tqpzm4lLn8y&6wDp8iH*1@f!EsU#`p!l&EKl`JFLWfp4DhEX-aR*21Czeh~l$BrPkqcN%wM9n@F!7oriVAZ#!Ri8bWF>f*{J&7YX2z_$cXx_H{_Oi)$ZanO?F+0riejHx#Z~!XuHW)ZvnZG^*g{AyS9c~A=eotRjmtTf<>Y(YhH1@KI$+mKu8uyL;UC~5WRPxzz~Xv4llRxJ2!_?vC;eEFaJnFng#e*>1_+Hp>@$BEd1sPVYtgO6`QmD=*C@T4Y+!EBnJ?|jx%|1ezDtK=Z1Kx?DQg_|&DXh0ER}YCvBZ{UXnAb9aNUjCu=wxnE|sCsoDWo8i}SlAa5E|<r2gBQIxg1KT2P<6QGv2!Dmn}({^=1a_qI(y=;nH(+NEF5&dTY>mObTOrT^?>z=ztUlnII-@Ga=i5^~b$Sw>sV)lv-f9F5aY0-(oU2rcOgO?Sx)LFrlC+m58FjWe(F5%Qg?+xw<su!+O*G;E}4NVVlOk~-nvdw$yybs=qAKkDJIYnZawLNGLTEA|K)k4aahuQqCff|j7d0TGvkRHeG28kACmU;$8$@;mI>FsE?>m{uBbgZX7Mt0wiVCNZ6enS5rAVDuaDIXgld6a9RZ4WKHL^Z(dem=(*7v5Zu-bsA_$lqtjuB>r95x8L_+hy0C~4$$si06rFlxPads>}l`e@W<x74J@GpXIM5{?-fy_^i82FDr%UKqAw%ofd(l6oH{u$Vxe7ahh>~H&tHZxPiO9egd<kAJvwqGqH;wutDZ0cob4UDZAOFn_^a0fWV?!v{ibUM1S$=l4Zs@9nsnH>hS<=SSkiK*+eE2)@<8#Hb*a38jzL)pw822GBXkwiQFEWe#%&ZdmS1&hS3ghzGc!!eWPs%iV}*{0TMUCd3QoSOzxBjk@kWUzF*Ls2p#cD34bGstOlf8bu@8Zt;DKy8(6v?8pV!5Ro&!e<XH(zUNpe(#ZX$37YJpbVNZoL%{dFx4gq@U)$?a@Ck$?ZryGQf`Gn(^=ey0p!jp&UiY;H@7h<<011sD=3g)d2&ehlF`c?Xq|nK01LvmV$4my?Z#FX=}%R6kJtydgQ*W+Vd{68Z)ws5MEQG*RcEy5%i0?mv_!DYA^=w+}Q&5@v>_Ta03IJ&Z~q1#uFvR-_I#rB7|xXQ*OHcW)^4aRtD9w&j<cwjJfj_+SewBIPw}G*rU9B|@4C<Mh;wR#+2flx49Ua0)CCQc=-Gt3=pJqTvPD>XG%%=C544<iDHg-j#i{cmY(0)ccy{!hgknQ99s_Ei+qJGlSzwpBQ~8RkXGO9MG2m&x>4sY;1ALamnNY*nUYs2ex9cd^%Mnv1Eo(YhA`_+S%6?F%@$`@mMux=DCtYL~`<9)6zJZiBmA*zt-|;RCKfapm2RGz6LopguKktQ5si14nYhBt-<10S6URRqD+O7B}QA`E=zijyB+`5Y(|uVg>v5N0%2Upv#)v+VQk5b3?|LTZ%2(iQ_gc*@V3=1Q>E;BbRE<r;Ynuka`)gwZB?yur+)D_-a&7*J@D6uGw!1ZfIFjtqA_SiW3&hQEGi4q(O)DA;Gd8@qiiPRQ5xh1V%nl}+48b{*idDYgD27|NVn6@n;GvF1a`PG#()&0XA3Sj6$Vm`&$R5M!ydNTP`_MdZ)WlF^NkmE1z9;@ZD&x{M16I@Y@?84cxLX`Sb<5Je<v$|GRm|;Gev~`Iw5E5q&Jd55ei5XR<iIA<u*X-tWeQ#eujse#MTGwdBq53V|@?-r2iWq6;aQG|H2z=jE5;~cGeyE7`04%gvG;=m|co)%PVK$4Hn5O3s=O$<-SED(GZq6i-)IR7`Q6WicKcK%23FSjBoJy0Fme#30H+r5t!mLk#N%52%-_5g_=IHZz2+&)w8&>%viT+Od~4Ic#bkk$%JXeVD*F&$L@lW9Pt?UXRN}ekob3*Rha+c2wgQS(N*8{?wcsAPUx!dpF>x14DsvW*F;x!?~Jb6`Mj2bPD&%Ridc@H_wMiUvR^b%)%WJ0s<=Q@NpP?XReu0+u);NEQ3<Ca<xuAHBbKVKSgKsHRQ`Qnsa8zpcNIvrnggjK9V=b}QnjRNdeK=3q)KOjR5KJ+D+pCH;it+Z_=XvSd>KELD}Jg0s;Pt}m+@2Ht>Ofs>ShqCpJn7dLa2U72-O$oAXM$ULa2sg2$ki#-^8={sgDkx`fpz{Ih#${^t4&v47`?=OPoP}Oo^ZL(Fu~?HrFYmn+1xK1-qqv=jsg*AOeP81G)x2Gp%UwxuvjDR3s&$?Xm3%i6A@K<W^z|_d}P})s%y5y{XNFiZ!K4Pw0E|KgrBg`sy)G(g~fun8!z_yYVJxRd*7Mk!~@%lwu_oQLegaOrp0ldl^sf@tV{qpEo19V2O{_GASC-<d!YduEa0#hI?6&!2Gd{P~zJw1)uUuj^NuTUQyj;>~_4HETYb$wr_eVjv~!zknJ?XYg06JrR8m`vUu~DVL+}lQfj}Avml|Jp|gYho1zk&gJkzH>@paHYK$o8$2l=0&G9GJgABSS_^WF=2WH|9apG=)p%!;JaA+o><3-HTf8c(7S`{{ruGMVyC8GRkN!YmNJ1&2P1vAO}kfFMV)iu^l!yTlLzy%o?;*XvJDxTIliHyM$rvp6C1DbiCtm;B6Qj$xubm#F@xbReN#eiqqdn;wCpezKYDsTz%Od;AzEj8vlj>dov?~0Gv8o^gbBo-Lv_z9N>RGBYtJ5It%f8@H(h8;`q9(U{rNfU&{l3WLlhy)(pbO~M3g*#1W74M>zBPTLtQdL1}rG3`95u+GY8H|=^MZl=KwkZ^fIpEXC&SCk}J6o$N7tv1TMZ!?qkY>ygp$4VMsnIIRG?WVuB=k3oE(y6<WtLiha6QZ^96@fOq76@T2<Z3tw)8v@qmzw_W_vY56Ig=b7MCa6C^i(rnUT2~jK7K`Yk72ksI<Wds#Trda7xPKiRLfjF^%8aVCusL(PfT_x(B{Wu8W39-MK0RkqlQ`8@LLo>$oX0F0)ieu)lmV#n5nSY>^->fk7w~s%TA>-H%h9w^nHlPc^~Xf+Ct&Q2=TvB`{*}GZa=cf@&%(w-ewr&G1xlx)4idjo7DAMt?-<)O3O}JwZ4J!J_?<guU>pF)mO~Rob4&kx`HS=!erMQrjo`Bv;A)Ji?QJ%Zj^Lu@V9ux%inuYn6Us&5E?k@A`N<BCo1|wUlPPWJE^<aj2-aF*oC9e}h3?q#_t9X?<+BkqfOCX^yI@{|M`<V5%^|tHK=iJ4zP@IS$1il&kn_@6+vOUbS}@3~#I&>9;3tHz_VFSuYvhgqe_0IPttmCVtI~!P54Icn6HqIZZKLS8Z?NXnRx6dg*)<0o{#E>c-eS=X@hh8XtAkiRphMgq1h{nrI?he$pMXynZ#mK|~4LrIz(6F1?UgY``v!$((Q2v98C>^X9C3H`m<@!tf_rkN=HN!q77n+_xd=A#!LgM||BmlKYIL*Vq*Al`(40W{hTC&%!`|k}>MMlxRk(UXBLe9LuLiNh8g|^mTYPX|$?IBV~+EYNzv<u}#LuZPHQ3h!PZxLShxiI*KT#9{O^|=u@YQe&qg=AAZgu>*JxG)IGW32WAL}*X8d`HCM9PnN=7{Snv0u^7<qP1t(QK8XN4<ktJ`^+?yInw4P47B9qg5D#vL>#sJn>16UH?GG(1yW73wmV?PC{X6opYMHH%2G)|y5;Zf$diLc<y@Er%YlX$~352n;)PIN1HIY_y=?ED*0bYXC%Ee*G<2Nal{aAU=!WLYKgQSkby{NzC)na1vz_Q^u>s(+g5#w%WXet`H5i5@(+eN{I1)Q72dPVw)%Ue*Vd-d{k!hmyjf+&6EQNjp@1BC}36w^}M-dA8bP?7f$o5AI0VJ&Fy54|k#+?Sn9yW&3-OqTPM@@Luf{c90OF$o(DjZe={jaorc?6Lg+1?3s*91OVT;_~kYE$@NFfPj(mblYf_Y-&^J<|G+Xona|}X-z@W!6WueB=m~`K#r$M`Z}~|+itjH!IVXDNS$^_|%ujB{{N#+{nU*QahG((ymZc<nOC?LoQc`UZS;|gXN~|4TAbO@}vy|y<mNLE16lMI~lcM}{?w4YMvrA0hMEryi_=`ve3K#hg-W&*jQUiGUc7XOky5lTYI`3yZYl<icSI+fQ8fe&9)~bUo%1o0unc{CEdIk9a%%TtIq}#IhdprUADn*mIhb&D@Maf>Mb5@2AGAh9KTd8ch@mnZ?MPp$Q=EEcQ@=<xfPj<Cdm@Q$*7x%nOMi#b~)Q3D<O(l68iakv3IxaVe804?Y+d~PpaUp>JFuj4C;lbvSXlY5G?-?`!FGu*2H8@aEmOR`eW_i;2kds>7wf!w)=If+ZeMPL6u+LMMJ)H$bQe*V2=Blp%)|Nj^Y~gWLB5eZ!r*gb(masKc3E}%kPTO&&vY>WA%-@(xl{fo%t>7g9M09o|m;x~#^5M?3I@Dq}$)vk3^*pjt=3BuPuvH!#KdoXYjXIKtT&USdp$8-?Y-mc%QMRZ}ZC!3U6TbAOVz`iF6^k+xYv)^2$>f@tfbn2CtjPgXX%`*~>*lUfiz{EJQ*${JLZ4}|TAqdX&NgnnJf9ePW{A+@dUtl_>zX$_r^w3Cv!@GMI$0S7^9aiySq<W^zGw5<=3Hf^tE=$S%E~2MkQ*ZbW<zio|8}9T#HmimK%;LSt-OH@j;$@bZ2|?<#Iu^>=Mdp(&E0vGqhoix;0_drBfNC9COWa2B`S*Lle*wevjw;Cq1L~gw#P}Pnc=Jyz3-P&BWD*i@p2h_^=U;${_L3v@reYJaZbFibK<weCrw|KJO3F+c!<5k^oW^AlKgep*OWKSjNwkQ{qEb&0;pVV3E@9`Z&1)|s|E^K0k7)!(;TE9QYJIh@=0AxbLmVDj^@EYO~BEqPU)U|05YqC0)DHkRKWZdIG_5ux2W^i6xn<GTwbJQ!O*j7+&B+2<OiGA?1$cjITb|T^U&#`W}yL_MJx65!(rCJ_10yP&K8%y<Nd$?w)>0jw|w&hTVKQ9YvnBK+L0_&`I(I3Wc`=&jZw^iCE9otIQNEs60g*3fJp*W)idr(T+i4-<29Af0JCp>)E)J<m}F+a+ihn?vpl_-a(aVVJYeA=Edm;7%0JjJGEx7^x!=@mthYulqro8TWF%a{QTLZWFIzp4^@hj#7Nd1yd@B$N(4!3fRlJ}}2jF~ZSC*Xu0QjDyjQ$2ggdWUBZiHAzd1>`-BQ&ExyCm9FpiHHtw*vAtqWTL`<yXqabbL7I8ZIht+EBwxXurW~vf@z5@W^c6N0IVBeboxKoX-X$EBeeW>TS?OrGXwFG$7Om>I<hm#<oFbG56@M9W&Ckn?;6Xd<r7^<iJo}8PyUo-tqO`>`oLb`qHItELLR3n|rvy731}1u0+uGq*yoRHi19XvmC~wGq3Y-OT|J<!sC=mhyI2*yh?OIA0zY!BrY4X90v0t-P^Fr8(0Q-5Wx0$WK2d87k&?y@6M{^eh^4E*eVU1-H86i4C#Dm{O>-1*Zc3S?6)NE0%6QAC%{=xy_^7NW|9E83kmRKP_$VBd}jTwnOG``7IRtx+&IYQ{=P_nx6#Ttc@+I(k1i*95XLS76P_ux{OJ?mzkKb({{XaO+*8x7^q5=Mx1`<N0g7?|Fu9~fsaYH<1YRFz7<z8kadlh5TTDWc;dUQD+u5h^kjJTxiQGQi4qBAP+=PAS_6>7<e4<*~oE)|oLWdUa?0Mr3=-p^kOtc4^9ebwLwA*sqw<{@1$F2{}#x%XkuUaN9S2ut&fZ|0xZw?TVc}7mj8>d<wt18Qe{H1GKu?$?FkMiDZxqF)oTa91`#0j#z4|N<Hh#KCp!I}d>L>xNSHAfW>C?GuW(l-aIKG!{9Y-}jey`!Y}t+OnPT4j6BcrfCth70z!rFl89%U9!pDa-QngKI`6m1J(=wrev|(#>B3sK6Xml+233J@2AF9r6B=g?wa!5kQw!U{6D0<F)1U*d5YCLO?g*hEYE9Ddao%RYP9o9mPT@**EN^h=PVGx8y0so1If`Dm8I`hjv0fAi)9_^RtVev*4N5m@6U?CSad6@r!+sf12<KStN4~fUSsn%Ce;R%{wF8j=XgH7vnd|X!dAGg>8xtuwqX65If~qJ!lAb_ZSMgzx@e4UOtLn5zUHb1}}gzjAliR3(s1+yl7Umd3&>>G&3tom&}U7Wv3!nor)@)`9-rLDLnzLv8w(pWdccthwGcSc5V@!v6>axe3CxZeDXIxD*nD2xtuYGn|ZldK{cDB%Ron$(toU=Ix}_Yo2o)F8pO#(YlPs_+C`$;D*~?6u3TnHN2vO|(@M0f&d5a8(G<>4_U@K4YkZbIM<t`aPiwdo*5xu=S!pp%9z|6)Sz)QtL-rT0lwK>OKnWSbW@5DtK?#s*IZ@1vc4iBcTT4IOT$g_Mw7zifh2uUdg`;m?;JB9ozn_hvLA02W;O<qQ1k3c+ik6fhTiUxd@IXP1Y)oUZK-W>gU0AS|A#@g<RH6_ZRsER5+DdgtRVA!#s8==x%qWfINsItFjg_UYJV)@xRY?L#TXBrb%Q24TrLifKI3)>6J8UE?zcUq>ZIzDe4aNzP>Ul2+T0YD;?(rWyqc2?pgndF?8Ow_&JT;Gx>Odtr2<Z?ts+WlH%LLXi9;YX^=pKvMo)ob1kbHZ`JrJhw3#uX;_!#=)L2){Q1(k~EVtinXPn2QlL#QP;<jT3YbLsZWP~sF=x0I87WH4Or#T`0*_vAOGpk0EONF+v#Pgqzs6lVwcp)}lo`SC_kExr3APx;HRl=&zs7E?4l?#N=2{&?598Z#|fOl0-P8LL0UDW4`-N=<hI7YCsG%woP-jH2k28&we+QB04AP%mdKt}5q4XmHP(%LfwZOiB@TT8yGi9YPuXCR0M=h?s0wFxxeiXh$w19~f_@aSG|78`%QW-ZD-NOe2Mjfi26a-d!OUozKykl0;P}S|l1Bjqtx&hw2fOeW(uA5tlJjikPNlACLQ#rsYgP`|3k>D4UjNeX65o&&57fr)2<3{Y=AUF)cS|+`cCu^>aO|PR{q5-b>$J)o!I?wyeG-VIGBzWLH|w$*Ch{m$UIIm_~%BMN{brV^`W--IYG^ocu4ol?7QNk%fKaCl#4Q3$k|Yh%<5JTLs=d8&Vc-nd=S;D}X`TZ{haPWHS-U6l-XDnvc;yw2h^Uk0J}MS;={9Qe<eTu+YLl4k8O}LrsL%YuE?7hvEgTOAz27z>{Qp+_^GM4v~eVx_^(%tppdi@e0#5bueNdC{#dUg=RpvXmO{gAcL=1i7hA4mNmJjAU-Nhq!-alDbbap{1z7r9xhDG%G(w*)Gq|up#4woY9Z<}hv$1jugm=TCDPX2iGE&YKwcWEqZ<x7^&pMP#E_^eNsIYy;GNQ#6v2orr6;TY#x%(}Q|cOWXH+-v1HW3CGBnZksY(uyVwgU)ZB@dn|AKXQl0Wp?`#Hhgv_n&s$`kfc2-zyOE$hWe%8n-LdCrobomd#v`09s7bO`mVW*1vo^{Oaa8Y0?Q7MPB%=Kw|idQl^yTbt$42g9o1h>3DNR&te#Zz7p`+S^)a4~=QXN`KmxMaeuxv{(=wB+Pec%pNXkqN{oU6;y8*Xq18R&;xy55e5G8^<zOd+7a&MMYtFXnwtnOxDK)_xnpg0r6B-g1lZ?z8hz8@k(Tjar|m5h;pOPZWJJOPKlr9G^FjOs8e4eOu&Sp5aI=-EnT-FSumZ(kaPRP_xAu_3ps-DR$anbdz-JrZ?t%s#Bnx+*;|m{DJkm75!&_**lo6*q|MuGz8ihW#*uLQi)%<&{GsJIXEzazm?8VXNuW#S&?Q45}=(n#e{My2=E&TfSwT0j1ZFoO#!#n&uzs<M#gPiu)efyC@h}Vw#f!>DWZ}a;*P=0OLxA|>)_U&8!_Q$7Tga2A@!+Uz0uYL>Yt+%X--p<cTZ^v)_TfAMo_E)_If>gV*7tjB7O19{?r{AVjUo_Y3t^N(?{{~4XMn6mR)X&pszUrNyUeABK(9WEc`knC@1d(g1xd>_%P`nL7>ROc&;Jn!NB!4D~>Y*-3aYd`a1e41Uug&B*qd9asnJyaQOISv6hy3hAk|ZHTs(*n{B&t-#YLsTApfr6_|55Oy_o43JwhsoZoIdf#pB#OA>8+An+ULc+)q6C*if91i#eqUMH4%F6=WMIKj$lEqU_PGvXBRbovN$DiR?b~TJtaHm=*>bVG8Y}HhuZS5r5(p>^rk)G7v}(Bo+>1AX&ZmEfic17+l;rYUXIQjY|45*FWx4Thp1<(z9*2bdCyHobpdI=s$r6<&rtGJ35V@-`Zs!W(KO5l-!A?JZfO@XeZs$0faUn}=YM5?U8M{if7{h_3yT-0zYS-9{?ZktXyf+$L+9P;Ri8O-xNy#wPj&vo=UOAUOO33r78|GIllT7Iy?g%KZqWzkFUG%i+O^%r)*}PlpZ@d9#$WtO9rD~Kes)&Jee$L28gKFP4w_x^*&kl)>a$C>Pty5q&i?9rPmA+*;H}g|@HQ<oerSfbqbQF*CrsnV>F=o6_<wvYa7BiE$=O<XJ_}KU)6E5m*l4~y6GW|x^wVW6Jo#L{9yLGc#R`eomJ$FO+s&MUTyR1uJ+bwoHgr*ZGJ_VG$}ZvTq6<+_88D#M#Gp_KY6B|4VJwG>5RrnY;;BX%QJO{4T8^qchU&phK{r2QEqr<jYf<gF4YAf!VK$pDn%7j(n#UM*68r*jLEU5Y(pn>Dr9`;3o{uTZ<Yu}7d?kXTb#p-oWYVemT?AT7e;QgKKXgw|@L)h!dWyTJss-{0;XBB<98jChm51#sr3}D{2a{@tEDQB5M4J~VqI|M%X>vtLj5uz#HLI2wj6$!z(~-gusJ<%~6l{M_<OXb}fm=_eyhYXv=g1xXfJ}LO_BT<Lq{H#R+@O;uRc!9uD*6L$7_`PHUv&?TK9=SdxZ?ERF@nbq$So2jJ<ws28*7ykH0TWMX{Ec~iu0>8<S>^Xg%!rH_T|zKX33=iQD`0iAAMAiYgG-p3Z8X^YLKC6%yi`lN<)EBR4k80rmJKS2do5534^!tUWI0fZPhT*0wx1PS=LJ>8AMZ4Q3Il{vJ6XXmeq{M!6ILR&or#}a*1jBhS5fT18EU|-cTTd#&9Uo#+C815~0`VDfB4ajUXCAT1}SJgA*VUkAD``>W{!!TTEIv2IO(^|F$j@0f9hoc?R7dMuh&t3oEu(-#@P`utH})Mf%STj+g&QCVz6Mq^<bG1d{`yaI5L8;=tY{_(=of5FojMYKoMq9&9!A0}_^=gf@k(g0bW>?|-Ov$>SQA;<xTV=3guQephD;*)b=x2RAAJoH-z5f^z-ng~pE5dGXWCzr3qQWOws*4PpP$z@bb`t{*{wgo|lq(ac`7sVY)Rt-}1fIQWih@zMR(;t_$dJq^a7Wwjrr1f<+rdSV+kkV_H68~C7GN(GfikWUiz0x~(Z)wDeL*$by$S;cY_2orkpmJ`-u#_`J;=gP0{=3o7-52UAdKDO$saknTd7#XWv#ti$vR<|vm_v*Rid3!?}cFi%=koMhjYOW-J<q$bANXgwoTP@6~0KCzIp$%PHQUT(U2Y`ir>&J=G&p@nAbrn_)Yc~N7HMiP8c?}_87zfP(pLDTe4l4{=@T}4fJpqSwO#^NR8r2E+h27rJh7?M{6Wr#oma(7<u>zDZTyp1AB-MmFqc>ZOK4U&Am?D~$M(7_Uo^s)T|0L3X+ve?N@Kc%R{#53fV8TnHf9O`$H)k_=Mt^MSSU&Yilbeucl)UZd+RqSv7WCEDS?rjM`)!@+PkUwXbyZ*;)1MFhXE5ukfGmj_*-8;xrisLlaX;mA>3THA{nflCv~tu%hwW!V8FaFAG8EY#VPj9?ewBD`K55(^e|3x;!p~o4VtOh&K9W^-7fejcw|QiSpEWV1<lEfGG>#^w#x|2}W-v59#m8aM!tQoceecY~)OB^?(GHV|sfcvA^Zle+pXp<I<7^6xG)YaZDMxw@Y6m%(YGiRcaki_JE^buWbm3rXs*`wXj!aB<yu(ytTiBQWFRnC7)rJZ?_R;qe`Y&#d%hmTJEaCJ!YV$Xm=>qc#{>)@|Y`nOFepnyQxh@W8Cb%7!^JPud$Y_o!hi0aCvLg2Z_df&ZnA|k4wM!H|EDITZb<vc;%?UM_T8YHTPRMP1W>03ZFjEUnR4;f4u)^vUPu1xE-eNAOHZ_#Ks)I$Dv_!(d7!hxc8{Lf^p?tB1bQR`;OS-j0r{1nKI^Z6CO2GWbmS&=8?blLgx;as2@>QLweP8NKurm^(UhCFL3L<G4dsdn$1=ElBCc1LMZ&NTdY9UkO<(w|l&0Lg;SGOQWveTW&AurNQpSD}2zgJ^i{{Bnr(<sq<$~tmrOLBDIoa<j4HAB1TV&(34b@o}yWJDnIP<;cKow0<juR8N=267b_eK0NUX7!&+K^V>~iHZtQ)d{oJ*=Q-?&7eR6aJ70CEd$v{GiQnBjTdYcS5?jJMU-S7_SQ-7izARA46SNGeq47mOC77|y;g9PiX!$NJ-w?vJ*DYD-cl@vw-=$%*PY`M8ZYX6c4;jlfIL&2nItR{=c&4+jtk)^*GVi!Qq9dK%H9rk;gejyALYvY!a<;VM2s(#x0T?T9ZMb<)$_sEwSi?M@{#6zozTt5K%y<NazmVXC5a?P8B}ghE7cN4k|h<CTb$i=)d%Z^j4e#I0CO5k{ylC4pW4jQv|rR2d|0e)B&XTY<wXtq@t))V{uTZIvC#jot@_HTctuOUzI|=skN@_yDPBSUub}_ex38f8SJ40O<%rk6;{HDo?*IM$eLq-#m;8wMNAhOc{uJ@=-ITi$yvE-+GZiG>Ksf9yX>{2|CL*0Ulwks<Y&nxBLH3f-%V^Q3E_xIG9#PjL4PfE`NcFYC(*;|fa{!!oXJ`Ovf%u=}@69S?{t0T(vyCSqrMkfqJAU-7J9-=E$Esju?@uTM>{nsB1ia?mi9{Y7;C@L+7>{K?47T$L<u9rOb9LBFB7!QJ^6*5lI6>7P(*vffVBV@bp<bw=mOKHSvt3TE=U-EyN9TXc5LnU!n7bF3BaIuJ+tM!IoiGPxpG<_1IaR=qD8A{|*p}|%EnaLew!f>)2OZ0fVuy|+Dm}^Twlycrh<aumx1X~JT*cpypyUw%{S1G=onYTbto$i%-o@qH-W@^zk8tzHZ`0*(>u;wQmnaH;cG_on0wFdRfZ*}jYY8uK0LE|6oa*ew>1Icld6r0U+!XWE&d&kj&on|hgMD{1?Ect2PH6x~pB$s%!vvkb#5Wi}aVN*UbmNYh11A^d$2)tptD|d=&+U0)BLsI!9;grg`Ex#P?IZHTQB!#Hy{@(%%SJoXV*dOmr}c_OiQ_!M;3)6@Z<=t?mu~p#Su?;VVgWvL`NryGfkg<ciJ=AxL&P$XZ!;~~*FY%lV;E@D7g^nk9gFz~0@jEq9H7c-CfX=Ju3TIhB40(99DE1$Nt8Rc*`xXiM{vR~IPM`_Vnc4&m_X4`T{m&=hL~LN!<ve;YXJ(pp!_V8SgAJ)nvV+xelfOG^OVg;`AMTX;LLP+Rx1h?1l3Xy->&DiAJ&8#LOC0c5HwRQRh2VgKAIq;laGUw>4FfQO+7>$eVWl|wsVzw*TI<?6sul+`OR9prMP*$`{fR{|E&8>-*i6z4CJDK>S#GR++i}O>qy#DCoQfpa6`LPvn=Go0aQnDEHe<iju21W)qyX$)h%ISa&tS#N5SH08fdz_A|r5B6<T4SgBJq}g*e23TSt>M+aNulAiqLU-IXh7TJ8Z_s$uKl#8DojonWXg?N=!K=j<Uw&Tl&kVCRFBGlNXavl-ubVl4Q{4QxSfW4UjXd^<RKH0E0%YSsc3lRH{=Cy-h+fLN5_5!JwA`XkpGYkpTk|K)2JA7KiY9epeBs!4G$X99FwxN`txa8D8a_92S%v4!$|3>1ys^X-#N>Ua|%y>EUyK(h^S<cx4Cp|I?CIcv0!<wH2K#)s<36U-d(r=D<#fk9gPfG)V<9@2x8)a**QoqMcyO8b5;(d8S-c?w8_bCUxeZuOs;xFB1C31JK#cMljJ`iT+3zml<&BP<7IkR*Dalh2*sQG^uCB6L)lo^pGR1BoB*b<5R?T<1lSGrAj7HKkpSm#li{d4f974Z!y)h=YQiNa-@~VCJ?mRxB#Y0N?b`OH48hz?fpBkbWlwBL|ae=w7y8-6L{KJkz{4f=CO~K2>wQ_}ad5L<0FGVPi<!9OC-Hm(HTE5|=*BJ;eBv^&qdw5P+GDPxXGHpxeNhU5I&exBUwfnDnc&n6L^6YcGTJj?km)w}6huI|Gfbt_O{#8Dg|uctm%!7+qjRGqiRwQGob$0UydWp)hzPA{>K5dD^&0;NJTg@Y55>6(AT`v7Z8ddIJNT06&4Q9}M#8N64on%A0U^YK)dF!vZYCU8G$S0ms50>-Nr6r_+CPHMnYq?z;r8+C59l;4+Ndo_7FO9SMfNY<-t2JhzMI@m2DU4gLgT6%3#*nFPiP3!qhL*<J>Y>_?|Ic-gR4(wjFMyu_R4<rf=dvST)Q*}x%YwwPyFD`4X(3q9WF7V6@T`T{4Kw-<1|;nM=Ge(kMsy#uJHXPG}SU&QsUgzF{jCA*iPy=Ayw%RAHyRZf7f(7nFlt?NizsXdE>NNGH&(F1#GSftL-y_|I`z}M&w9qwcr4G*B=iS0MFE0rgM0AJvBjIuxzC*1LRf7D03U&4ILO}>eU2}^g|V;CV26_!JOwsC@Rc)7G$2N^7bcsp%|VL}2C-5sa4@}T|`cGGTs_{MePd;_cR^LXD|f_>M=cT6P3oXnO)_iAPvz#G*;+Bb8A?|`gipg3?2C>vxv@ZfN@6yO!yb|CJn!y~r^LyAycY#>#8Bs*?;8~|+MG90eZK}su?+g>`+x{Ty~q`Q196Mnx5_ZcB;7FEqj4jD%*{o_!MlFGPBbF_cvJ+zrR`bOSf@1f0z0c7TFY_mX1g%PVx6dpS|CMW?t6T5P`vJI9WoPRkT0q?hpG~{*(^wm(J-$YZE^@@ErBi8R$K(BTKp?R%q)};yAL3x>h#5gz*k%W8b_|zfWSSP5KK*FDNfBaf`+^*_me~Tj78aF9%-L5F_Ow?-LdI?(heA{$%fG0K@H#BnL7%5^~#(>VXH1O#uL=6Soz@Em1Ak7FdHuUgG3GEu@cRgI&bzCGnn}M>~{4Er+6Lobvd_oTi9HmXRP1D2NB159rabs9VlszPzEl#_kR5pKJ_e}O`OIHkd8*@L<%q^j=HY?}T;w^6Z)vJteU}PNqBVhyh8QnqYd6%*7fc!58yPZ~;XupA$hWW09$iVHBc@l7E=r4BAvc=X5@LARr+1{6Dh_q!7DeJO}hWu+)Tk;IAig03uEgQ$>m*Gl@ue?=&#$dOc)uRQz7-662!BLL*gireN03FB_dc>}74(1XPf9E=zlxLYIF9o&T`weR82EZxlIH*k*gIYX!JK7{Dw2c=++vaR&>n%uO2?$FR&OTQLxbx`tOlX_N(6&F0Yg?^@YFyhY(RXXk2@GwI<62Mv|M9mls{5wvcV1?CL*@W_z`R-}g$9P}h$(UdW`*)|<%vieSp1dWH-uO>W@;*vP#V&~AveaxuZHl{awu=YZUZp+!1+9Cq)uUf!>1zp9h(+{0(XwAWZyAkH_#;Ta1++l8n}m{jN51>cfh(90TIO?{JMlEv0Tx{`6u*|a-IlS;O@ZZS*-rZ1@<CJ`^{^8f*4>uH*={NDyNx_S%sNRMwc&oWI#iF?X&!;(BmW0YGnD=S*$(-ErVnRXJqbpT9A{i(~8M&ZfDZHg6}cb<s@>}_^ht6Tp2H;`nn?USlRoXx<1-+?x})YR#^-5O12rT;-1!=)a#&#Sc?JTmes%(ien-~(*akQ^s;^FtZ>*3hdD84vslByVx@QV%)za@l|9edW!#@|zwMi!1632l+nVU`(t5Y_V*t}6$*92p1k8WedlzbUG40BrCY`jDR|z>j#HiSQ|Dc4b7J~F$*kZtLgWM6&(cv-FBpE;NHs~hh^MSm57)u{i<HPu(6v~4p76iJfV}hl$225~4Y*Q^gX%R-m`?xWF`#DpJt35)!1fY8feQkYv!xJd8@9=;u%$5d4WzVbXPlH}?5Jg1<YvzG7sZP-}ddm3R@6?xT{92CkKmVA}XHWAXC5qr;h0a@|X@uB}Cbc9p%l$9PevkqfG>B%B$uG!B4UM>#zVYw?=%mS)szOGT<bh`ph~7g7LM!DOe>+q^`QWsiZkgkkvxe*kWuTmCBob9MZ7{Rl<Y#$Hm!&Vx`Vf8Wwe+8IzlFZD7HO%>PB-vF$Qo}CbS$CT!~GL8m`M(=7{6A`uf`om0p|Gj2Xp7Rp_$UK3#3m5JuNE)m|@$}0Xw;$>;k%&_%Sj&LtYh)x9t$O4(vPdZ}sj;RjQR-%qczr)J14GXqUnKK9xx<2IhS>tj$TZi7$N1jnSDqx_n?P4H&H=J^`;49~z5AeT{rMryx*_%1E4tOmT<FfSff4g&Oi#GDi+|WTz)0>A1+5)=K^FMG`%9eaf%);kvPa{MVHR0`XJFfq<#ZjU~_OSRjEHHyaW9Kwl<sQf)+_VRh!sI6op(Q4-7!c{wOhh(ty;J;#O4cxce2;JAQJ_ko87id#_P;!4NI^`{*me&?+nA1_66<&*7kvMr9LkN!g6JeQ2<TI-dgjd}@Lwtkk(&D440h%<A4EKyyU@@=wy%%!s;17lfw_Q7?m3Ea-jY|K!i0kowtqjdD>mc2O43?S(Q+P9unKP*I7jO^BC1L;iJMgoI@yx8b0jmytjAb=UPP_w0F*IK@?4!bVxu=W=7m)=xUachW#P5Jq?>4SvqPhz{j_L2F|+vd9b{53cBr7Zn11)AzHEkgj)I`Sk!^FGILnGWqyODmDG?!UY~$%w}I(j8^#kpslpYOS`?m?F2Qa_7f%eX2uArADVYH5zd|c6G#yzCW(XOe4tsbtA~;(~cm&GL>AP-0(B(N4Bg*A-BvvEEAWYJ?)Va4XT!6c4Nh68~hW?toZOo33=MIW97_^@0oNXW%o%KMp(Z~J_Vih0KEkN;A~<?%!1-6%e9=dXl~7r-eUp0x7}hU-zh@D{p4H02y8u%e`W3n53KNbb22TRBxM<D5djjcyt|`L2Lh%?6I3XN5S*jumc8(LbYPD?Gl0%(0=;1ukTq^({t=(t@L_F`n9r3oi`Rej+GNF}%Xfs9+`9ftL>aVAbn(GSU{j~i9gt)orjTlotg`R#1zW`9F_3RwhW%WnNFwZGiIv3v;Y8Q$j%h<xL=02W=7KU<-D%pye%4wf-AjlN2ihGln!#7M^zDPJWtA7;tb1>yY*x8Z+|Dufd(ovCl~M&IKjDb0T_hy;q{sgu*!Quvkbhxj-zQi~Uz^RdmD@DjrJ>>2NO6Y}Gi$w?zAS;L+usBzjXd%`DbGNE+A<iGk?lbzUN*a9P)W!MHd~ioQGTVB6B8N{P!wgj)(70!HL)zXV#-*x_b}g0M66J_)Hk57yY(Sb0t?lKa{jBb_`YFM><QQ1+&IO?0(P$DFZj1#^e-Gj8rqcCaraQ7R?N!X28sD{hCLpqICNO}M|zM3Z~s8ECnY{OVQ48BNLkY|b-}qFV-_W2XaRV`@Ei$0`unv4cLjRj&3+YCwsGl;plSn!04N}r`9nBe22CRpFk~jMT#6!k*1lI%R7sV|loZG2iQ+DJL#}dPNlO72>@U_u<q0V}p)q}`+c@)!mO~*WzPz#Y{rG|=%g$1-k?Hsl>Zv*!4YGLK1#>+n+R4J*s0BwQ`B%}05Jr<ysd7d>h`zcox_a_b6o9Tll_*dPbmIxs3)FANoiG2^$e(_i<nT}1kEhY7Jxx`TD}czg3_~=#1aE(%^%MIf%#Kxs08am+pc!NP<;(gTFM5;f3Anwewh<+Kl>EBZgmrdSg)+JO3-L|4`WwL&*)h3?RhR`g7|W}cMdzwKql#sYOG>6Gt2kt=YKl^uR6@O@o?WO&K*|fV6+=~uu$#l0k?A%}QjjwAo$SwNwcjx5Y``or8F2z(4x&jUsKW?D?-mLVRX0OA56Ofw6h$#VGty3ibrK0&gsK2(3K+KN9F_QkpET^vmfE|86vhZkT?%XDxn_kJCOkKao-v_3yYQxl=<Q&6B#N$tDuFVZMR1^pv>NV0bLt<=)|UcCoU}efP+`7(DS}~`DYKFY@-wCI=0}X){(K1~hM(so^~fpVUb4n~j2xkwV`R}IXv=rRys}@H2djh_S`h$3gUEs91$`TdwQa2kr0%8>6N#W!`rPy$Eg#<z2_s!EDidKnA2G(^A?|QDdInVugGk@QA$lcgZ4OLWS!AihM!1wRdy%CZmP4DJBxgKTxxC8dDYTTz&FpK5*&$EZDGK7$SoN0SkEtd1sD;XG%b~q(0F(x7P?-Zx82G=Qvs&X!gU?}!B8+PkVz{cQM!|>3BuWGpXY0(?rSV?_t??$3qg3|#>mQ@`qWa_4uf3o?yQsbRv$Yq9x7w_<sJ&37a5JeEyEdb866UoRLKH^XWMv0CRw1nd)1mwlYWXFaLUQmMlSbRiSG<8GFdDu^lqDfV&m~N%RhM+G>Jn9TS=EvYxi+f0gyqWI{~OoV)K5_Gxng6EA@D22H4_BBLso3X2P2!do#PtC=QVIWTf#_%a6m`Qu8(y8COCnn&3X*Ho+v&)SSsM^8v^9H*-D#5L86eV><tF#Goz$*v>yT2bcdBAaADtIek`4%ECJWrUi;MbvWmLR?h8$UUON%K$zChyD3`xod$p1>g&IU+Mx@?nMCx{FadAGe;s*H7_e>maqwhOOvY|SinDgndn00*>#@9cs5z8(gq95)=Ut`wx@3`xv!tj(<U{AV{1k+0(NqH1mQq7{3(tbHiqSSr7n1Lx{s92N6bF7+M$&G-vFlDf0C?NUVWZu+Woi?>#7I;64rk6rv={F*RxUW=2bQPzRr)!-o7%Ba3S3?i(){t<K#R4SmyiiqKSy~KY;iIAem07D3LX}5n7Z@bdRSQRfq*se36nC@}CL~y!Oxl?%??(hfjX0z^%+FiX2AlN4*`fNHGR{)lYEX@(ymT2O5LuWJl$AL3&tfRqfag>7Rg##7XaRI)ozw2lnP_6ZbHpjDj~Pw;bvNpOe(!2@@TKW#-to!kSY{t7z^qBC@!2mYsbmp3N*)cWPh}wN{iK42C}9&V0~^f<L@CKUh3qpgfFQ4V?407GgmE^|W6h?cPFNT-8vO|JM7kFx{Z2*z(X|tN7`LS?X}eyf6Fi~p<6)@!|CkxOas+(aOx;=af6ij1g|;Z`dCp?ut(HeHtx!7ktP`pGchV3|r2o*d00V3@gAxo;y2NV9G4-hQ)WPVv4BVr2L&j6(9w2^DAI#PVV~L=F9rDI6`50aApLf5FoNU8>ht7Ws1bl`VKRexqWuF};2pa9Ar+ef-SYu1;gse(Hwvvgr1Ck9$8WIA~RvGcqoc$1PmFH#VuPng6tYD{dcRDWg4AM^;EyBU%hA!OmhC~=2h`NHve=ll?S{Dd7IJ_Y0^&s0=f}wP{JLb3&68<|@G-W_1RGiQcSnW!T^AQ`fG>;D{`HNfCXb`-MtW%-~l@LGe%Y28!4N^H5L4@+K&46tCzOfabkSNA$DR2La_gQ6lkqFRE_6skw062Su<@0<Zv1-Kyt+~4n4K^<vRs8?5tdP!t|2t>3qqF*|Q5mS}&p{PwABUGDR<qFpJIyKV2wWVRzA6ZEa6YO`E|wBDONrHvpvt>Tn!U>+Li1^h2#?o`t9pv7hPt%DP?OGwPN#{UX6E@33^?q(mGmcD9=b<7+si!C<PuIrN`djHpG_QTuAtgDLqRBjipupUB+*QMBC=^owt1JF?97M}lMh2xM4joM0<z4m8tX*knbjKEpx*2qt?Jn-u&NoQxg2U7&x)W71uVmq)~UK3EEtTrm{>`v3x0609ExJ7=q-TiHM9DKys4$JwBoDh5aePgdy?QKSsM&H%4lm;EM+j(lIPi0;;64n{5Wsn@!V*vrB7~;giX^Fb~T*+N7k*qK8?b<sj0h<`565Ri(1@w5od|@m~P$B!q10mob<$L1(Wlw*CGyUKmzwNQ}5w%R)5RD@s-DmDIu%WJppuqc`K+8$IyJx_6OA}R6}PTm0fAA<mwg+)uHYOK$2T@K&=@CDm&<)J%BY^{`{sog_dEi%%Qr;8n$4ywZR6RQ9K!B?+|c#)6})0){j3a^AL@ZbYg+)I7I^a&VYouPR+nJjy{$T<$Sy*C(8%06q$*w4uA7q$Z_wA^`Y$ehXMVC8Cd)T^e4ISbj~xQRhqeZTj01q>zNUk1}=<}Jre;HoiW<wrP2QC6jQG1j`-<7mPc<sTgOIu;t^2Wr*Q@}Z)O}yv|2JB+%rr{f39B7r2>E(v#ECYv{UV0e$_vIRqB1!k$rvp+QP3b{My2=LddT|$ge`kKX&1nf7L>M)k1#NLjJMWLcablHBe7KO!Y<c@fDH%{D=1MR0}!Gw2+&*7P5G(-cVOr1x{Rv0ZL;ut7*v|M;1h-c^oFeT6IgQel0|H<B9U_soHU_LZsd=HHH`eoay+YJB4o2R6bS4J*#v47P7}lTC)qy<D)A=0%<sV6(?st*DcNj({HN2A`C0zr~!P`r1Q76jyON<P_Y|sQYoId#!}muDfGn&pC}nu>EGvsjlIFVan9+|*-om){_F-bJ!3y_v}?tTmwM6{B#rf}OM1qpSWLp7k@$5{e*7orxBB`-;drK#dRC(KdSPQd=GVymUh}Pc_U%=Bz98u9XJWV0X<ya@e#a~F@BYIJg2&-_pU>(RU((_|FZ3IZ#dn{VB0d!`zUpn=`H?>H3+l!GqI$85&)&ETUp>>$Pt~2TY2;BUxn5})m5DDkOE}juXT^!n%N0+5!!jxUpIF&O`ovd48SXCBY;L?swVcBBgw=}_C=3<)oGw(D_Xg)+8Cm+YBBc?>u&y`;Kj9dLHQBGI)B?F79K(h%Tf;Fxt_p>jc1Da$n@WHc6+4Kj7Q2pY_h7`x4K9QX*(C%C?9E+8GgR$`Jt0#lcS}rWQZOXDx`N~&|GR>uRcXeqH?>))<*?dUUVjlT=oJna;Bzgys+6)@vy@^Y%O9nb^2c9>VxQnVUl6_X6t>L^8Mnk>O)+xL$4YL%3vDYDyNS(espJMUk?ReCEyNpZf)H~fMMGVNP|{3nK}TfqN(9ahat*@6m!931&O+_%o=($gjq2+?r`ytx+Lqx(1l}H<Xh&fGfkzaNnaedusH_N;_Te^GF}y$aDcVv{oy%<*t1zDFJpzM8;g<l|o;4>F{ZMXX6_<dGSdN7<ANwC**{jlQu@|Xx1EzbU)-4A-p#4_c(5|h$Gn*|5XYOmu5oA6#+b}lU2k3%F8iEo@JZ>#KVsS>>$J?!jLF;_kIuKi{MG>0N?wD`YPN>uZE4T*5aiF4fgme)U!l=85*6Psds<n9tEgpQxh}@Gy+ibwBh_w1hI@}QYVJVPARqgHAgf1Lb5)f1?nt<S*=!y5(mRnDq^0U3r@4%7a6=yP{mu~fEJL1TlUp(5xvqAM-w1-688Zi;1z+e(Ea0iR^=$Z|%p#b}LP`kv18SXC(Yu5lKOT=QCT|1&4R;Dq4&RUw5OUxB3>8pY48}Dvc<e#>#n<+Q01t(2xdzR5NN9aR3qu*H8Md=@Y&s}-mkGpfv`(16|oB5DQCIj&5U@&sjbb{3*{#e_n37mUyH|6^^l`pd!q8@Yiw6zEPrX1_h9k%51uHBHsW)H#8v(I&;t~nrkjoW|A{l{NRKBl4We!hgXTtZ5u0MBmOG`<%KUC;ND_G6Hez(HyRQuk#86W1F%=ZzSL=$tW|hc=!<sVleTHKi!UeKd>*!vsP~sQggcA2cgKJA}h-y!n2Q_-UyMcBB^r3+XLeVRqk*VX2d(0~4{U9pxQ(IQcpVBD5h_HcB`KSXrPpJEjg4(KH6#pHyQcSVjsi_1SYp{<~-t@A?(w#vnrpwTf0)wB*+7GoX<LJ`*^{5jSF>ktEPa3;9o-Pt`%-iu!-GUehC5{7}87WBy?_m`%MVK<D*LuYtY&%!HoCRg^ef_L_z=9+8SL?QyRuBV=xIALxg$=s3*`i_}upRH1DdHKVK8`?2F>fp&2M5E@EndJVf9N$7m`n<$Je`i{^~3q3MVJ+f##1zZBBqoeMl#8;wpw*qc(0Y;)^o@)(hw&RT;d8z#TX6!y4yHER4_vslHC+k722@OHZ7|E!XpL|T%Q8fY>eE6yB#Ex6Y^_}UAq<TRnL{U;x38(_bQ6fR4)0f3l8wihJ?wmp5ZaUGWxrQ0N06LCYPQGXr2A`?|0Yjv=g=$o)b^wi3hC0)@0uw+TEt$X-R5e1yx{*zm<q;P^;E)gpXqibt7)P;&+)?TqWb0Fo2|@$Lnu?XiDIZJ?F%T)fhPutra>k`BL^&~u&Wp=fJ}c+FCDDi^Ui1+NhO`t;IpQ+@SkF*tIYXrjGgQzF)gDhz`5mUGG@G0FTMjN#Jv=i#g`?@o1^<C(sN4ArwL??pDnhcd@__gMr}df}HpP3C#XIdapke}lS^|V7vDZ8gmF*=4!d?U6IiK?}TJ~l{%XZ5yb4DW5&)}=@3YyTe4Q^q}aHAckClWhEc9w&P(Zuo0&j7Pj5Xc6ZcOqw2y=5tIpI~OmDf9JNNk(%dY*xgSFbXmQlbxH;6C0k5`iWhjm&J<DpJbT<n{BHD2HX}ZY&MUuSu(nXlivrcBLwxb9;Eit?e0{>B_O}_*)P=H!qIewCD9y3yZf{#+W+buhre(5?iWb=GSLL`RM>g5V$h{eMfuh`Z!lf@`3i=-lh_<{Q(~Dp@-)&h?`Xs)vcM$eD60|<WO)!fUy>b0g6W)WQ5aq^Ke?H?p|k;X#=bHhGUJx=81<4@ix9OVUpH#?$e|WHmy8zH@?_XDsb~xQve?J#28La&bh9b-jW%U<IFZ{-Q#EJO9KME2TnQvnusxM2%VV;Svs3_Bb9gj0mL-m5?byE}+!=OJYIlpg;wR`_zx^)UIy^}(9jufaB74@#wJir~b}I}XJxSHn<frr!I8h$90O(c`a^~bj_H2~|ApMx*=_szyIA0YiXtLqOoRJj@2;il^4U`!|d>oB--BJY$8d-rB0NxmFKB|LAc7wdU1Wln0=dXylj)RW8RlL<<O9#BAZ=d(03;?vB%4U%gE-m=%kzF;Iyl5qQF?^$h7g<I(Oo5jlmhJPc$m4h{4oPMzCMpYMd457-7<dO|1Zt9LLx{Z8m2()lKqBoOIfsAct?jQkOQ$2VfWtYD02L{@j5<5DF;5)Ju$w6pg&ae9s6ZL!CC=wH=$BiJqnc+(=AD~jWlNzYAc&bOQO=e^jES~dd@&)EIi1B(WRohd?R<3(RWl|PCG$0xcx@P1Bkzj4*G^i`n8)$+mLg}aa@=RCt&r4&J{g1ERk#g!Mnuurh^ZG%{jmh)n_+SU0CAJ_;4#46{-Xa4s!VXIE4zekUILXI@Qvuc>D@P>$w`Bt4v*sZL;AbBSYn5PLIeY|b<9@6v|wm4dv*<Sn48kiQiQ-9Db(r(r91re*d6#->e((mtc2fhc0R9pZ{Y92xT=W*o9bu1`x%_FO4+!p-)V!vI=pGkASlUU$X?9iA%yQiX#}~h)*IWmL>XYqHKy8{tAkji{f1&IK5UZLNZhkRaLMk9c!Qk}kreSrDGC}Wq1IC#o6fI-4C_=aa+-Y<woJw|4Vtl*w+L^kvz3&<=+s1lW+T;mo4HyB)*Y*YEoVtCRh)Dcv3yUm<B~3CP}gqwLLKU+I+0-903BbY5e!vj)O*7qsUaQTbDr%?y((6zh-4`T44Qr&5>)$1<!<@y8?E))z>K#<H=^nyV8gZXhm7J)LX=dcpC$dAAsmZ|2+-0G%lrsk6jMs{>?e{8>P2Y}IDEOZ?*!1;IpsOsK2j6I9TQl)5@DHu232Al)v@Rq@WwO3ijm1;Oj6R$*^s+e!rnJV2`9VIrZ67pL(GZ44&j`uRjQiLW)f9p5&cCJ?USp2jEO61x|BgSSG!(4b7jSk=@Q0`avY)hL+Jy({9?5k>(4aOp)6IEBjmS`I@(AxKs>dWSqo#vsw}|`!-Qv7D?Y9|l8g-^ImwxyYq)G!R1MTNm*i+LwJ=pw(HqO9!dZnPRCIl0tVD)*nh7;VQ<O3R6jmRCacBwj;<LkSM69VOEKo(+4Vp>CYUa^B9ZQqYQjL>0y{80)7sC#vjoAImZ!Iu=LALK$V0vCz&*~0bXH7F8wHc4pr6Kxc86OiN9+Lrzk`-tKQL1Zv+(BA8$C<8lhd2fCG~?hB4clZ#XOP5usIs?QY&$xHn6{B}24R%mfs9GdZn+}Y*_QQlIq8PNQpvJBWhb{~7FlVOhj!<V(W=(&9ev{DNvA5qijl70UE%Ne?|+Q6PJ3+h(qPG0mpS=Z%0*ti48>+yWQn-+6tg<b?3i%Nxy%loyr#?!)gq2-59MaIc#xZPE`?k<?hSP@h&P~qnCy$nfWQRJM#&v5srqGR$HlPpgJJmrGFbDpaX+SqMx|0uo!VKwVUSF2#(r)R#a;SYU*ICn6w8*T71Q#XQQk}s!q(Pfv7zj1V>Y%NR{qlu)kn}xF7}b_Wiuf3j?A3ytao&s$<j?V(+}-%a^z<qk=dy1pP8Jb^Ogoj#-K0zoP^2e#2~imYnmBg*|pFQ@s-znxTHhg1Ny*Tb7FPUmJ!pe!3RTv3a=kS_4i!+@U5@s@7ZxuXwUh3Hhvpk^!Kb8leJ`4&EGR0`FnOU_hjlM%{1vL!O^uABkIPEMW`-Oc_Ym&KIu15dPh^G=({Kzdimq^<yU3gZbu?JMuZjDKI@Jx7rpFc=U$)b2;N2y?Q~~epZ&g?!E#Z)T~FzLNL%cb>z_M&BDd101MVYrrReYZ@4io+P$Vg0JJ!B7QqXoP^rlfHw8!+`c*7f|J2ZxrxL39r1q|0(3L^+hwQVvBA1o4u1LHHrc~pXAf1sp#WBmeC?S@Fkw1q1amdh#ZO+1w6+=jKJP8j*=b0FpIKTBSOVBgBbD^~MfR&`_vXQ=!eldp^n6$#Ol9P+psV~|J*R5_Cc3jQX^)z&yHnW`*nB*_}t;ML)j4Zy+xABD1#Zu}S^Qre_+g;n`B>d^eq`4Rrjv1gSOWa78ofB2%Rxc&|6)O0i++GB(-BZd5Q%COhOB?Dn)eWAVM1{{7nzckq*RuPNEb`mT@(JUt2`Aj_>36AeLm<nqdO;y-*TQV1Yi2|+4dX`~uYto{oIUee+*xZh3aRF5Y&cu>eLZ}(G%L%9v-J<Hqu1Q#&l_*j3y4%rCD9{d`s|pEZ3nEi#7}{PM8dzB*uQ<g^nXFDN%Z*2Y@*wRU9$Md$(Sh|st3zw;$Q4903X~^x15-Tb65lQ%jVFejo(cPK{|Iw9`EoSmt=#ho_!(hn{>KkxiZl-#R>xVgt{H_=mPo5hLMf^lHYe2|mi9ZFXP2cPu21r;U`R(K%+-s6A#&)F{+sGPQ~2QE`Y|&|qhRFZkw)cPcE%e;B`Gj@!P#wwNw^pKwmiv6r5`gtQs5Agk1)p)`et$TTvP}r(Z#Ify`1$*d>LKS%gYO4^g6*N+4So9SB0B?QMjR+PjXcyNu@DG3d*g^UHW6C*MH~7CL_ynttMsDQBqc6T7w`jolniWb(JwwAgIuz?5AdDvB8+2O)5^87HFpkC7tAGkzVUW7Ynz!_N)~%wH*cv=3A#ArF5lmE?GNQR=)XD?w88E9f2GDCZ<z>Nx#6`pq17mb5!3#2JS1|VLD~pMN`--kL-g09Xdz|4;C!o5k+Vdx~=OOKWY5Vs7+xZuyVA|yRQ%hE+_^ulpgSu5=0#g1^QsK6_k&S%m#Jo`DSEDMt`T6nXw6EGzrhX)40mA{=~S$q#f?8^ow(#EBETo?V;C2#r->#`%M5cFc({vn+^Li9B#^H2d%Au@y>T>hkJ~_yfl?a0#CpoXBF`K4}D!d>;2VY*2>H_RmPe`h}?UutAk~GpsIIEiR$3Wc+w4uz43Xub^H2NIox_5%Co&<?)Wa3U*SXa>e5<!uO(Nx`MVoTI)_{}pa%(?hliCL8b3U8z3^YZ$|=3dDZL7%yuN*H;nx;^ZQ)lrrFVZDUbU27wUl19lwP%zUbU1yYQw$?DZL6QeGMTcXKoD_gp>>{A7|&l;y;WF;zA;bxV3i_QW`F*D243iQaaQ>C;l~^k=wamNXe3f&uA(2RqDns<do)uL(&1Nib_0<nMM&yFLj$L8Z@17Eh>j$AwE<tO#(|!l0Q-<@e4JkNtejGQJm@c{2LNiW>+2N(omziQZ{uZOUa%)|D#Ku1eT<VKWRkyQC+F37Fnh*O38ewu_SS(`QO=#nbK06ZYvRH!Jnuoxw(Rrcc(u*(PXOoKP$5oN0}uY5kmwLqn>m#RHQ~}rG>6iIM!7<FLD#yC?0cBS1G)ptMrWQ(DAp;TWBm9zWjM<rRdJd?F1LDRa82Cd!<a&@s-xMc2>`*E1mf^Sgq!gx>9>ah3M#_PB$Q#@!~e4!q6yjw9o;HXOxz-+|b+l6Y?Xg1kw1y`<Hc_#!p_nki`b^%m(#sxb&+Rw5i56iSCjb)4binIdP_OgJY$uIPGE9N@2_Z%$x40m4bIi%2iU*s;9C18)kpUe~WtEpa007nLy;VDl_16w;ar{t893aJTuJXY>z{Pe&LXr>5$0{pdb@x-k6z?UKy>(b~1YzY##ezj);hAgBfN&F>hE|V1$_m=3r2V5c|>n($5Y@2q6Y)+3!AUdMV+K4p6t{&*7rdj@FlJB8N%6LM#2F?$>;C@Hao?6+HT#_q(Cqu7(Bu@|1ti6FGz{KqW=I0>0>P-N2%AN5tfoHK=<PxE@7C2w&dg=kl4|l?dPw#mI8GTNe&l6<j#lS3(5<NrMv_1^d~TbJ)_wFG9PD$1=X;PnEA8oYWn@yaP<T^oxgkz$FK#PJtt?4)FbGh?Uya?H~5Q@$N*@3$`VoYYqG@;}h5j`yaXA^v#XWKT!cunRt;W){gHgVusJxp8Y#_fI<O1Gtm91{BLc(U)V#BnJ(Sv1u;$yZ^On!B9rQxt;-uu|FX9v?WQk{(>l{^pi1Ljbet8uLQ7-pgcnTQn_*3?ogO&h3Q7{o>8${l;?B8!O2bXLCb?-wAxnS)*eZSi%X4(5idz=q$kd3H4+J?XDEUxtX<+HJv%Tq)Onc!7uX2WM_%Nu53hf6V=*Wx!zLKQ1^24(I&ag!KB&h)@pk|f*^5I{37yjLr1f)}J%E}9&c<gPLXmZ@)3bw5ZyA>%QMEEH%<%Si<Kmj?qn)>SF12p95ZD%NEgDQ3yd@?oR;8NMl?d@iSPH!Y+1EWm#cC=KY{wq-~F&vrPi5I`Xug1JRcDN&)MaUVGg-eqxoQ%^j5441hkme9!02Rz)Sq^vi0<K--yfY$Hn*~4pQ*k=uAH3e-F3{o5SBJaE2c=xKKTC^{N<eA&_So&N>&@zJBe;34Zg)hAC~(PyZ>fOp*^h>W7NO5>W_aghe>>UUg{AFXoZH@c8Q#h1+$-5Zo~85(Wg9oz)y~ZCs@K~{6-|vn^T~EM*Jtmlxt=IeMB7bvc!a$z3>%Z33Dq&oz0Pd)f}N-EIuiKs#CrQFvXn30{OFUsWLTK@39o~0zFxw*IVgbuL`jbt_k?*!WNiBCPv^ySt|qFXI>#Fc&D-+WvI9O;-Ai#K=b@FdA@+}K9*9Xm(h>ZpG;57$uW^^ReA>*ZK7?xF7e;fync1JY>~X9gj-E(3y;Vq97TC15<m^RlJ((?whK(0pnUsmO;w_ebn2~Nj;3NB9Elvkf%P(7;nxos*E~lq6K{|Cgr7txfxK>7|SIz{dMyKAmvt3h-PDz}M)#y~TU8pggode9v+qcS}MCT_ylMyZ2(LXyx!y&e0DR2US4ge>BFq;5YeCX9L=5xU6jM1sFTDng~>i?B9D77c3WrA}_P;-f?3_tiSM#-hGmAm~I)4f?ELJr{zM)+l$HcDbLP+KMmsCKYypD>G=SkJ_4F>(Ari>3RZ4ThTTO8cns=!v<s^oV2az4SN`vF#1^2Iyj-so%h0ZRIN{?h(PUV(YD)0Cp?R(~8)=9gnzohL=mW0O7Sis0-uofYXRTl5-U3m_5=ZhldGYR~|zQTMvjUu+Ik?#UJPt?!Be){(kpw(dGTg`$wwj{Gy9LP3jLlJ)>9CP5<B^J-%ITP*!9}Oh59m_p{B)zZR?F{Dfw^QLOYBnkSh};&Utq?S|M6%XYx=JyGP~31nbXHe2kLx3O&VWbKF7f7JaJ_@2XenQi`xIk*xhJ*EM1ae6v9h7w4~?4Qy=5AO2oOwa4D;BXB|)`7~5E1>l8V5|bs(ER+XM-W-R3W6;LpaAi?zb(&8DoyNuf+xGJCf9(B9vHlmjc)FY+}nX?U4F$q<L>@csEIq=Ex;%NSXKyVCxD*xKo9G0O6Y|>E*+{agJx51{FMk=fqNUwm7Q+y#5D@S{GWd)(E0mz=Y-@?^LCO$?HSJ6T&T)8YspoWs%L3y;YgzDdFEPGYB-gvT9Vg@3kEA>q^+4~)d_QLL<$owFXozDTbm_$Evvtn%s*9y!%be0*K&N8^0*+covK%z6Ic9`<-u#dk3}hRP6-L8q@{Q=DpcNkN!7#$cK0WWf|hQTNQlA=BZu0Q4-5j8s+aH)SJAOInoDLJg++U-Jd*^y&>lO6Qt?2{Dly2JD|Tdb8p!Jf#^>cJ`U!{Q#+??INshKqtZ2A>6zM!9duY+WzT*(k#64E^WhmRpvEEB+1vm3MBqPCIml6g++vw=o6d&%S=5%Kvj`$86?kXo^&vt<j_??rkLAk-*ttruRac*Kz>7TNvw{)=YT?g0y2(r+trM!|fp`{kc;1^O(rEjf`3nHmN(gcCej{SlZn8hPranSG4>fpFiXj_`bWk_kLEPF4xj4}z_AtBh062}<KA=sUFP%+vE^la0I{-@t_`^`mlqi>pXjP1F!ZW+_oGlfMo7&AA<v==R#{q<(nT0xS<bbcl)a%`~urqZ=DM^|=~8#0e@X}!#RDdIWcV#|S^%B>?+z7J)p@nt3f@_TAI2o$f`atDql6kl`QK;91cQ6$FyiTBx%Rq*QtacIfCzbFpvm&VReQjHKs@T4#x0TbCTBe)`|>U@zFjPBU_ZUeeVBN?xrJ^}2A7;Cp&x2{a0tMtXp4I-QN9?7`Sl<7ZFP4uvo-X2?bPvPfa!q4GIcl)Q^k4APW7>5s66HJl(^DFWV%e08*_9O{pp9jm#n~}@GlEs(=TSRi@@yd<jPpC?Q0mWrg3e%QWoouN3(kUu)8w<rTpl`|xGD;Jh8;0R)Upc)=S`VDrDAQ0*bxqArN<TD#KgV$qOtzAuNg~m(_i&m_TpN^Ut>rxv2UtN!S+uQNw`mzEO8&)^YH=;b6T))Ms<cUACC(hQO(x=~b8X2Bc5adRlqYGOnZrld{1R?a>G_|rNj@L*)U(?X+`3~a=E23!DQ({QCL;nj1}B{YhWT*<hX+ajuq;!Se0>@Jv)>X900F10u1@iw7IfbM((OpI_d70hnV1;B0S60{EDyZxjR3;eWdhpb5Sz~RP;>Ez?3hstd(;^GW`$v=wCDo|fCuHryy+-%#o_vG*e5@%+%SYMNIACT#$n3*Xc<(7rS$=~0ujVN=l&8p_rM;LKVyo31hM!7+Sc!o)B;K6pjBV#2Z(+L1!3irL)udbaO-KtfP3b-iZ7qrnggHRf<;PZ83L>=RbJyt1*cjsAk779^G7mZ`8eK{&bmX>4vgVL)n#fQ%B{eDnoYTrrlHeSi3}6~xMa3O4%c;hoO~Do01?TM4Ofp~Byv#G<#S8%srJD(4trmjs~jg>H6Pfzo)>~4>W+Lz1H)KmF5N1-TGpY+E$wkBZ@xrst9yF3V)*D3a=+mc^$jE}{TqG4-P_+VN&5FpWoNiG;8*1azR7UbU}=UMBd_mE7c9NDgq?2~5-<OvJHFv$V5uE&nV8)<NgKRjYIU{MiG_i4-@vmKd#k7L5;*j;v!xJJ=xP(H5?cCM2`kFuv5C4s)(08lj%nYG9;b*Z<c`s*HfwpA%s3&QUrE2p8zq_906W!<tYeg6Vn=wB5QOi!!N5jCpXG1g@R@nTu6<8w)I`>-fKrJW25x}m$s6W)c9!p9Vmd4Ti#GQ`=~~}oJuba2H4d}GJPLFlh_~sybd;^phS|n?jNe!`125LWTD2X8lk2}m<pgfL9i>Zsl~)+o8cnz@<5#r2e5Jx#J))&t25N-NNac@KlK6}6cYOGq>4<x`Rn<Tg;8c_FK|0YseUYFjP9TZoof<93%7}Guy5|brX(@q*i7QTkrN=Z}Q<N(!6YmNbL*jwNEJvxQJiQX6HEpU|s1<(|<Luzd`gIjc6o3yA%yqQ_9*ltABuQndbZU~!pzQA}_fd;ctPwo}FA5&080}2_7K&C0w*q4m<5p~cU>e7(MyyY;tHxWz+SnQgrwTzL68X`^qDh|k4QR2@!t+!o=i|FRP!~6N);Kvjwdf;N>X1rp>(X>(XeQ@6`k}-AIVVdbj0+{^=8-Dx>H^9zf25!PzZW$cK4;=X(|DWmP)p@2Dm6s>3Z7FLcb@5}RErP(<UhlRS&&O%WBj-Z3$vbJX}J}jz0F`{BHZp|T7_E)rD2e9rd?6@3^$RTy&c6ddX_1YBo?`r$en5%Ebk`EjPfC@+Gpxz)8ARS#@-UR7)$`d+h3Ui^2u;k-zsf#P;@yKWxVa740u)o)6}NdZY+8jFo_Xc^&~7OyB=xS-jA@NRN+I6&{NIO^!nj+H@N-u-@J%ar6^bmSCxno7<Nk21&qxSr_vK^3_Mmk+JC5pb#c!b46xlq6|WfCdZlbeHTXSGeyagnz$`m|H`cFM0#-S|>F#)wv2#Ao3V<wUd6T1z-T!l~CJ8E#DNB~bv-=-)c@AW0<5ee%3PxnM8EcrstAk2H?IUU`1Ju{m2TC!W)jB-1iKKkPi6b}(XJf(JR524vjC1+Pku0!ao9Y@;WpPQPcx7(teK3<to<?WgpJydilX-_q9D>s%bz%)Xb{yzp`jqU>L@QO=&NWGRJ=#(o7>9>(16S1xyxD-N14{chhe>!OvhFzcf~lT5Jp`d@4tw1Ke|iX=OuY*e0GzwbDy*jI^g=D%)??{B$45sKF-z!aYE_?VH=G@)kyws~t(gFeJv#HF=n+h{<r8FQ3}cSD$v?*N^y=SnCLSLVR_p!$b-e&jY>=ip-`Sz}L?oYTa!oDw3e9Kg@w`0@08}h)JL?O&8Y<1zE}u9MC+Ui!79n^QRh&6MFk_`8t_k+cFPCZ;ohm}+>=kOqXQe1<S9~Y~LAu`ha;&|3Qq9oVEi9f)Rov{Wx|sxfnkow|IFz)4?3B7mhC_JCU}D%V#_212JJamoL}zCxH5EUdWbMD>g@^i+*_n@zMH8oPWmgfagKbsu3Dxyd>ixAJO>@anQ`^am+mEeL2l`mk0|t{Y{iON%TOaVX4eOPfHQC~JjQg+0jdq^XCG^xZYO7G(7e3rEM*qeO%ek_|$(-~}9dY0?GkIvL;d7RR5<V|?<RPOQHiOhpF@tP5hp&QBXfRuq1$B#9qe0;qn)cHEZtfV6NRvb<y|S#r%7Zb9vz&yo`{hw+`=DDFIZ|weupg)`YeKQy5~;pw$G}|O9q&@Zta;D*F8Ntp1if{%=#~!<d|IN#4ozn&#}-d?R%A!`aEC$&1*C9P6emMyw^E(r3Ph*+$iS9z=ZWPm!B~8fdlGcdIo0`a>)I$(5$sLh@}@!WwX;>>8=`D3F2HY@Knz@lcc-iG+0vUg@6F;L7u|u&ZR$pEo69Ti5{P%U;!c-V+&!hBmWyt$MK{3<Wi~I%y7F?zfwe5U6Iat+U38lr2w_HM(5i(*qH5W>rFV0*^tJ^x9wnWOl%X1;j@~#)XxsAk($d?&8be)fb9jS0RD*3Y8)s!2bNES)l@P_YqLZZ%S6Eh;XP^mQ%^3Jwh>!E(E6-(P>+a>EyRPwLJwyI#GP{Bz=}hXaxdir`6im@QPw;-YvfBwf^ugEH-Ji6?Uv|Tz?>=|K4~W8ekRlBpsQo5Erj}X1%+UauvIA2-aaxw5ws`L(Q%(F>X?1_#M7rNmycM%KQ+`Mn&Z?K8X4%SPf9qK(7l6T}gNO|wG(#os23RXI<8+2t!@9C%N}oIIX-t)RCU_}3$N`+1K&5lFklfC}Y#)%lmVYdzSbM4cF{4M3XLz*TsAj))27r|Lnvx0+R`d*XIBqh_kxnIa?C`Lc8=a}iBNh1nz3r^gJz<Wpp2zIV%L7o0%GP24YV<?EWzv-U8&iJE0f<HYt-m|~t^F#!GyrYvQRyxXKwapXp!j7M&JI8jF<qd)8mrb`9Do=awr9p5l>7}6R(e6giEUK>czFPdvV<D*eFIm2>o^~P2oYeiuZtRb3_aX9bCBs7f4B3|CvbR8%1&K1?(AmhGSh9W<Iden<4y$3=Tm}=%UK`w{R`^4zyJGw&$%z!{QG;T?{A*%`+4m9>A2&IKZ-W2876gqEwsYbPr!cu1kAes{T0)0I5+JkJOm%<3Fv<XbMALI=YCQ8z8jv<S@N2*A*xoaauMh^s6y6g&1mp@&c#NU%&n#yTXnAV;Vq}&U`e3z)lTIo;O&r@UD4VMIb>PdSM3#Sb8l7R!~kapsrDFdxCD;24uX0gA(rI{&T`@M`b*^F)=qc;gpg_8)*w2Ke3t6bL2GkN4rsFjPa9AR{7}5jyr;no;{mQ)lGrDB@!(QT-es|CI<RgAu@G*P3ds2Cm*1r_%vi8#P{TH1-^Q<ZN&}s(4>O~`3Ta)syDeTC>8f@t6!$WD@G7)Vg<?fOo<-oJa&h_X?X%_LE^LBdcR)9EfPa#tcVHcJRO7v6xtP&B9YMIwuB_fr$?2Is15(h1FQPp;8x}M=){1Y-0CSH<?SJy?S1?t(r0DhYMNC#O%h@$2Ma)!xjsfk8B4(IXFkAC}fB!{HCO>x0BAOM817i_$Hl(wN8Iebw>X^Rb*{>;O+SphI;Ya~rxe?D?6+@kIuBvI)f@ap(PTM*c{Q1geIn|i_q%h%COjxjDSm>+;rx(ke-4*4|a5@E?Ep$SL^txJSSC%g514@uKm8$VZe>pX*Sn+I|k50n+!&n<6Oc0=&mYZ|%U7iLkJX?dypQT5Dx6@ic+9#jy+)tJcSe}VH|E02wDBgt?7B%7N4r?($We+u_S(W+kF*Jmy$FP@d>cI{4Pbznt-6z~V0t6&0Ukae4Ji@;_mzAXCu>3R0ZSKr$3Cg^?GAcRxJpg8%1beU8^7b)skl~{2LBk&xdrH&Y;PWpJX4-?C!N2DIRc3g~e_sOPT7tZreHkp6Xx;)oR2HBpf6?A2-=YZFGV(+2c1yQc&7wPC$~>2qz(AKUrGd`sAb=pUXC_~x^<^eLt`{kaRn{y`TTV(?K^`iCg*36XNCJ|rU;!o#)dmL~Un}qeWYi?+vLw43J640^9gwzqcvQ$`ou)k4S`+&_8mpFxuCy+e)X{hs*blt@CR1BEEFsw~C3KlAm+oMyBcO0MnmKpI>q@5K!!x<T{8diy&Q`tN<VTp^imhc#=n*ElV}g0uPe8c#GK_UXb;A^!vO4BOAaJpgihtd`)uP}Vd^Q3cHNZ&<i+RLevz9Nvy(_^m`*1EDcMS%HQop;|+_Bf(VG{>u4cho<vKUl8Bi2xGmsLWa+F}?M#Dyhx$*)H*j&hkJw(V?EXn+9Q@Fx?RCBr4TjEheUvkx=KN?O}^{#4N;_W_|;qS^eAEo0UOrOOcc*(gnk=KU4}fcQ`H@e>45R#huvrc{;^yi6pCaRfdv^SYjSnL^MYT{JT7KH7S;dF%D)@A_o$o+u7lgS<uX(zz)g+&!NU&c5SvV@wG%&tIlrLr!*nLT_D>8@9yoE=_LK3SMrm$qHxi{W@PgV)&YY47O}*Paku`UB{F#^D=oBp=jM1=iv#n!gRfIT)J3w>4oL#EGt|>l6zuT+xl3%VdiMQLNzMuv`EE`_>>8nKl9e!N0<1dfrS6F-bbEZS=u;1<9%e;jkVQ{c^`!%@1um;Qzes*-bZ8~C9ECeXnzz88)0i!_zsY^RDt`0f)q_^O9v!!Vi2-}^3a<tT1z8~yem-zDP}<a@v$JW8@Fp8wQNlfu(Q)o<kuTdY>v!jBB`Io?#_IT(vRG~?#u9T`v<F8RO|OcT4Cf)YyK@0V%Z;7uE<QgbmL`VU9NExOcevq<i=)QOhA!Xu~9lscBU;BFXf?q5(YYQhA3T@Jlzc!8f6;#l8m!51VG;ek09wf<#x4*z)^OCxrl4SLgi#tRZe=G;G}Z0RVIS-W0|40%u{_eI1wT?++mrsI+Cq)U6DFAAd$7qVzszA2VTVrQYGOK-8zW=8CG2M-DV7D9RnP}`?v~s0IqrXBd&PzROSFvbG`Dia_XbM1-^}uMyxt1Ww(8Jpm*zjaQi<ru8i^D!*%mWxlwCEEoQTc!CRiqaRwPz)FIRsK;3b^Q`Pe~2He0bvpN&t-~q5DvX}HAM$TrGV(`x`mpfXL1*U{vPKBP%JDgcC{IY)ZWVA`f|IGpgJYPUllferlt~KXojykD0Bbk0nNMJ`W*;VCAqBsVF*%}mV)K!=O26HIbsDZ!`Ec?1(O-A&2X$s?%TH$}A0;41qsAe!>-|R9?{b0(!uIq(|I!(-$#j~@WlooKLIV2fr<8YLkmFhxW>s?x)Uo4FZ;b|VG!C-Kc^_M{vqfx#4*<w9$vF@uBLoYcfHxp#A3o-P^Oo}0P%nG!#B5M4=GbZSbuT_mtU)9)tovMaP8W4XtSJm)xsXABDtN7J3kb=&rBKcz!HcUI>Q&lzEf8gDwz!E>csky-thQB!NX&^4a>CtM6&dzT;+Zj(l>NYm*buUeLu};$OHs^7kXfIEDJu!^uo*PTd<i*@Gp9MLJPquCEH0K3<GER5~fb--0SMjTw?WB@}AHL;m7e-vTEw{!`Mgb!?oB6mto;{k%LZsz{*VxoD%JkSI@$6K`)2q{bu4v)qoQG}J&n@|?oAG!Kqd<rLQCZA8(?EzvPxCA*B8jNkgg0vqR~4NM+diN6xME0nf<E4~=lv^+<>SwJz<QsV_Ne6v+}Ybsdww?UwbxC1txbEH^Je>>O?zRQ_O8g8EN8x^N+z|ZGvA41Qu}GAy<fdx><9bc^jO7`zU`z=EN{QCFI!q-AHog~eo&d3U5|;PNKTlPy;&n*%^&4}JH|HB7w{_DC(>V%WN=~-CN7af@1GnD{AQX*e)P=CwI<W4ZhvQVj>^WZ5CdkUf*y_s^M$vc9IQkV_<(laiu0&h=~#S-(<AYEp27eJ9@O-`Nq{#+q^Sjzu;?G6j6oxrypgm++icHPO(0cu2OOgNA1rHi%Z~cC5;_BQOwLN^PzT{yLT5Da_EZ4y#|jAN7134<cqD>g87yc5O@{At@f^Yo@_><Lm6mSrEYQNwH)A5}f~|F1@?nFYoV>&6<PG&9E(Mw1%Ir!VN3rCqzw}r^77?O~O7$e^F|79eD4f<ngSYplZ)m&)M@v|VVpU9vu`;~E0|po^iBMhT`;cNp1ts3$0p+G9fN~<0nbEX0F12yWu?|z|_S4z5mhtgNQ_+@l9O^AQ@>W#0RVHlb@*zDz<_k5#vS`O<3{NnY-Fq2t<{HJ69<driBO%h{zk;PHL`wYHe4fj{br-$__MiLVt!&p;y;mUo(=`U6)+I({a30r`XD++CgAL^vREQn~8rar9CHF`k)4h@6NP3n^is1V$J&N8^{tgn1@Fa-}c#U(=$p^6<sqt{{P41k4>tF=P)<{iJ>^o*~b~osKnw=9ji);r>O~ySjb5?OZut7`Fk7QJeFB}rk;<~ln?}rt7=U44<ooDAiSir);r6s+&QtmM)@5E;H@3dM^ra7J7VYS|{)I*}<v}Wh3%=`0T#5P`BwoB|i*|NO?aYX_4MjKJ+zq*D7P~o_D)3RNK-ZM3ylg0a|3}KqT<6d)D?;gi9i06cr-ZG94=i>OaEUdk|eM?YoPtx@IOdO9!@Mq$9Jp_6JX1$vW3}Mp4+eGj))$4GZfWKP35WD;KlU6$WKl1xOWu?r7uj&Q>wtbyS4Q^m>0?}uRHK!>na*3H%;hpzO{{Jj-<))Gi>NU>4OT9*TEMoVR0vQiv<oq$MV?AA;_b($2?2;3K02A}HW@us!qQ>$>m=!5vWtH-IoF341y)WwWmT3!PzKuHcmb+p=$ep)ZcgsqBt_M>`g*b2Cqt;GtUQ2o*twmiKX0}4CBHm%t09UJ`e2H=TaOqiZ>{?oHj%bryd6g)y+S(?!SusJu>pn(1kgTCJHslYDg7{mnp6Rci>920cuWw&l__c*!Tlm#8{cF4p@9^_i+w@o4^jF*TSKIVg+w@o4^xs3a>G_!t-P`T(dfW6|KVP}IdHUQ%T}Q8fFPNwM$vhp}T5AenG2ddzt}x2pO#+M3C<lvBfa@GpF~Ps>AZN5Fyw2o&U6n0cGxeUEkI!Ay&3Sxu@15DH`=uTB=tAz7KIR5&nk>;5#_OhyxpYWB+Qab<O_J^8!!ZAlb>7|`UE0w($7srQbC2>PYxv{C)i$(vL$A%(n>uuT=jZ0>lOwsk_47~8oH<1jlQrYKWfo^LTC0yAE^kdZwu7$+N=tWjzc?RnDavDCb@K`zH*4JZVepqPaDLqBLaMLm$?ZGS?9X%zKWjQ1E>@(PD$!=1?!BLB7*<E@rK7s8;>cJ1ImhbJ$NapjI4d#L^?USK_wo3X7aZ9A@wYx7Ta$;Eetv#~(G5JDy+BiceBPA&887vV_U>=B!PSRYI<|+?b~|(OmoDvjk8;205~CsbS&#403EfQ&>_N=vaT`CooW*bb`A_D);b%_l@^ziw=-LS3<r_W!RdmlZ$oUpa(}|ru!)H$Z$i;qYw{*roUFw|2*7lb^TparRi^;ZhR(7!0i){U0aKDLaCgf!!%qudzRA6eA;mPt{pLRf`rIkd)>Ba@Wt6QIq$ZVqI`XoO&>MT%y1qcY=QH|Y?W-H}b19db-WM8uiwkFVJ&8~>B0W8456z5SUmI->TLBaY*m9s!Jnr1WDrOBQGOl<Bp()PI=x`X3}{PsFUA6`Bwpw$If!&?EV`f?E~6Qz3%2cJf6@9+b|_FJ>UCg_WHX~1Q{m<z8r+`b_m&=aQT<;Yp~-Iyr@wUiy4rW}RW8>uU!64^zwwl4=t3Dz^iI9*Uqx4~2>x)c%MB>A*#&-hQiomkHoqz|4K>yc8AiA!B8)>C?Sb0XFQYwNEq*0VxP337i|?mwEaxmv6T-Y(s-OwaA^SfeLZQ1-!x&#x<JXSCv^&O^8Hi#2TkB8`xn*I$Ft&V6p5F%*e@HN1r9Xz0=PjJ&C@@}|xI&)%EFTC=6uLA#3`5$D8d?z!hS`MP}BR#s(JR@#!mz#B6LAtaE10R|x?8X4iTkg<(RLb8QiMsler8VL)8WyAm`fEXErCGglIW8BL|%sinHBlcSB+tHlnHvfC?|6f+!msfw@drq7<5j*z&_SdX$ttZ>r6WGt&Kty(^?Gx#x_2+I@Hy$V}*l<}E!|}z-xlOwX$<dNsdEL(tO=kUA_DqD@g&C`<2aM(lv8h)dG?sclA(~!9Y?>;u>H2lVrp+0gDG=BZ-W#yvpMQk~xue_#jTM>(4;0ndn??j=IfzhR(0%oQ3PTPmaW!?I!s}_^H)T-!h3yDxUO&Kgtb-w}Aw1TKIw6=Dm*Eg$b2S_U9*2HQic%`RWj^74O|`Q!Hy>QT0eG@6^S5#R0j2swLvd!vn+034fsgADZpg)xcf?AxZurRk#V@5iT83}?V%W66+mw%6^WI3)9&<QV=EHbpKqU-3%})OSb*H8HD6M#)P@m@{r{MS;KMh+Bu9RphD1qQ+KLV*4-}SY(%EZsH1(KsKRBI4H7cqlY`<d*FuBvhcG>jah1>@N*Vb<~G0BaHpaKol1o3(NYGBGf3z)h*_8-T$xG32CxnS_vsoq|JAuK6&wCnX-XvF?g|sju*ij>7V^i|)deOA@Xj6A>;9Hy-`p{lK%SiP>M8O&zgt-E1~N0w-Fp!)!Kr&8Fnk`FsY*2a{h&&rGP6wtAXPbah(ICM6XvPAI{BM4{OjVms9d6^&TAPN=GV@aj3$)H#*woQfmtMrXi{G!WYjvAZy{psko~X5G#<isDzj!?e2jpa?+!H@`07<%?Y-Rd{)we0-Jg^1N}RsxJ4vBpgR+k%j8AKT}-}R7LjVJe73dXzvi{h^UKPAi&_+3U4(@$rjhmEZv1}lBtj6RTC3uSag##wVMQpTbm1kqa?`&b(5@_T#X7VY=&|hn75TAS-_d_a#dY^wx_y1H+=7ZhW<}q)}*$zwdqzIbo^HYC{^OMJ8NyqzE09W?oMCjhBH0?5?mEyI&W=~(ooNDoY_-JoTcGngOl;EgPP4tVK)#DO>&;N+>XaKClI1R2X~`y+!(PBWzOOEZ+JUtG?ZJ;xa50TPv)c5_y(3-CRoe*xJMupB@Wa|K#iRx1GII~A1UUGvVgi~np{Vc&`Wg|t98ZsAfBfcsE1lQEoHvny2~_Y?{6Oc=kGX=J|$byJI|whHiJfnCu@%LH$tjo5}nSV9W9GQZ##4DFpt*iB8SlP`NRoHQznh`h4RDYq8{7>L+*PI<&dqjJrP`H_ttp{3Z)&GRTD`k`Q)h@N?X7Oj>fu<VNM`47EgN%xce=i_Uc1F>hyQspBF~4@BltS<X(Eel-ee7;KB>bQ7Yru)XF(KIF1a7(D+q_p=B&ga0gG58w8#_!ZEmDjp;6#7si=Idl70#ACT8*M}|72Cl(G@QtJ-|rbF$I<4zP!Y=}NrE33iEQr5m^4Q+D$rhToc`&ugdTGhufX^a%s)*?Apd0=Iz4<<fc@8fJ=BW3DxUo&M5*qxppCH=3>jBBoZd()Z=CMw)<ck3?nUR-kP-~UvtTytgofBZ78xuM*_MXosq+Gu~7Yc5Y*a~Fx`FwnM<?N!ws8+2U~lLGn(*#p5H0SVmXRx(37<qoa4AT=iLLVmdgxm>K|a&bv6w-d8mV#XmZ_~mT+ti)asu@O2E%~6`JHVWWzp{osZWL>tQ0YRVXoMUk<=;qd<n@e!M6LMm)yK}eVn)|=(f!xw?oIa3hHSkO*dY<@9Rvhx?(qrK+tjAI=XR;csF(L;NxO1{L7lWAS)z=<H+DEq-gt(Vms(UZh7J0ha<RZz`ifsieXD2GCOsQY&)bOgy-7}zLdMv=Ez`qEjtO}B!$4u!M_k}7b-F8SKwtgl+9L0%hW(D`rkyefoKP0r-dEK$!N&z6V%uyF3-mC0u7a0G|Gyk{|-&w#~SmBXU=ZN-&#R$DfLleT-L7`Gl8s$m7TLp7WT1mG%lX{F~U+G!mv7R#J3#q`~@|Ug+cQQ0|oYwg&$@cn$%!D2jj9X(yCtQyBtW7BSuixVQVfUMUb>Qs&w(lOUWX8*t-(!--hba03WY=zE*&O4Ro?=5ob4zelG*$wuJ4xVROi|R|n@!k((J-!VPy)D9-A*0f+yz9efC;*B=rWW7aAT~L=_cGIolTPzE%<%sZdNg=>xY$s`+<bcUNYy?g~cKKB8~(NM0u;b6>JoD(TGkOPY(xt`ysA+*R97;j&};4c-L*QRvtwF5pbQYU>s5P3s|=f?9wqFVb>O8|M$MGP<!xn{x65x;P-x2sLi#Q&!X*JUuhb;7e(8GY=N6}?v-S$SZ0E-U00qa^#aa<Y%I}{4iG#DUX+J?P;3H>vO!wg2H~DX+ls&a7>m!s?znJI&LVFk=B`){1>c@}MlX-NA(L&9_w6k5ZsX*h+&$->wBLmE(Cgikb1Ga>k(>AYdiMm%e6#&-55{*$skvv|lT7!dyW*atOYVslaO}qv4|1eWxF=p2#qyk4>X6RbOMH_jsBp1^bZ8&$y6T(UVxryZHvjsUG9s^Kd8tOEVfuhZWJ&aL&4?($d~QTg#$afZp0FSo=`*^QN}Sf!MDob^GB+QNA#fSmB-_CxG4d>i^IKXF<BBT-yPHyWi=d{xZZ+<9h~T7i?oAa0Rq_(St)1y~%2=d}q%V{~8^Mc*AnF&?Hf~!{fKI$G{et%e$&^YnW2znUygnQO41s!IZiCB+YhE!o8;rp;H|JruHaO<`ZEkj$a29scr=I2}A05K(mb)9NZf%1D$55?&v>+P-bkHwi?ry%jft}^7j82=P2p%(3B?mHo`$pW?s$@hV3diZ$SW;P=j_jjmC7hqc$tzoVdA7zy{N0n*A(IkM*i>t?RvpbxyBnknBz3Pnv6C<#%9M+|a<-XkA^3`(u?yJ}fMBn`>=w@o<sW{7`-%SzDf;3&%diz+YDi%q!%DGt#kc?1`4zR02guO7ABOaMx>)AXz;PddNAhc8L)XEtTR03|12=IKu{8`$8dy%yj#<{h55}#N(^i2bB)(dA*!#Rrl9N$w&NmS?dKZ4?-KX9(t5MO8;dixxI9M@<3#Jo5MUEv?tZn!Q;L2l*Y+1GcqI{h42FhwT6hDGGF@4{jU?o+rG9_d%{nb3d=?O=vEei;-6;odDwg)1+Q4k|Xg6G~Uw+lfnV=gAbnZ|4|ZZ(rhFgu{)i2hpEA}L;v4O)6H3__hE*^Y3zmKju3fXPFW(xRfXqJ!Fy%)IBSg2TX|62B*}6dOTdVz0mo!7Gd$i?bm%l8zv2>YhM?U6N86tW&929m`Avh@M1-@H@d_;E+U>wZJgf#@`){i;l%gy!8vB`fMbOqA)YH8szLcD^pR(fm6cxO$oGDVD3rhU+(co!EI>zzYs^cH}TwCLLIhb;y+f<a#Aq~T+$MT2XA0`;$KAEa*jz@n26Pk9f-oj<XCqmM8b8$ulqU{;;)vSV<=IFB%dBVmfGlJdg?tju{)-_2fs#~m)3hxXNyF~`7L#Fna%ig=d)2g#QPp2P@Dmir1$Qy0=c4Jp-ciEnkGKbqx=pNjOA6&t>RNS9I@D}hUM$>=0hiKF%Bn<CfLBb@WWi;fhm5(Yy=_TfGm`G_d{^Fk*OX^La9mdTO{0QcO?B_NFa4}0ucf4YDl3fRO`o7EsF9<%Z_sIBsf-<<|new5X~W&lpi5Fs+bOPqjkn$$ih#I|ET+OWIp?qvZ7q~01l(x0TNn%x}TaPL@J@{BbHhJ2+}9b$Z~wTcPkS*POAznE+5qE4X5>Z*s9{VU_&3=jSK5XBuegF`s@*MTLXVzKbj8vKT=$RM>x%gM+!f>@V!T{|9}IE7xRnwIKE}`=qMNvK0Sg|X8qT`u0%haj+a!gU*-)r)TqBuz@D=FmqKc<pkNVIN2c1VPu$FW;&?5jc4CFA=u;sp0(k{%1yaP6O858X6Ei%Sd}0@7HS932Vb5~?h=vA07uT(PVp%_TXz2>mDKGc+gdcn>Ke)qlF01Iawa7j!SrBhWZ^DOTM*xPKr}aOyD?Gs}MBe-ka}(NJ?Q5nd5YCHWEv7Mrb*U7UkP^;UW@y9Q?TE5SLVqVi+vhnZ2n8uj(pbCrTAQZ?4^C5cBJ7MOgq^Tam9vu%ma=U?`Xym1Dm=KtEnJ*{Wm54Q^F9|47tJLo5bB&AP}AkQd!(tk9iT474@SysoWyRz_%xcWRfT%*>IVBl!d^>_eOT(R^cUWx&T&oWXn&!?fuC+HZ^&qxx$K{2iQQQ}Ly^i#-np-8N8PE^Q76q&%w;EtJ|GIk=owMnnaJok*ETiLQ#Qn;`a~4KC&jTi0T*+eIDw^za-p+Q1Y0G2)z?b;TcrhTpi^}rId#1?E4+ouDy5Q+?}W{v+wq~XIseM!w>?4=uGqV-0d#dBfE7Ok668nFhuz;Rnn=UF^q6AtK|b3M*%ITi51Wl+I-V*>sJ6i8{sHwNvBrQmh<C*-4CdQ=K7<Hg7Yp(`k6iram~#BVwv6n?c2c%l05}u+gOS7AOh<(#-g^|lifee|tc8(6-oYOXj8%^PC_(c16GZ0;Tk|a*?}iGh_abpSczU9A=2F-W5&YIAsN96G27PNWIuDWbo4nLA2%EqC^MS#;QW$t43{MYMraO@SdXYNm41jm)!tlXfD-1*cTc&-%Ux49hJD4_zXJB}snkH63ZM&j#=DJrytcn3AFuay+w_ZIx?bS-a;RTg|r?H~D54&aj+WWyOtfpc>Rb`J)!W9<vfVxMZP&MBpF3I81wvVahGR3rys2<SPdO&wp53o>qsfFjO7G9#>`v@tPDrin7hbL{(cwfwZ#V2q_^X+qTcz0C}?+;&K+`o$$rL`#J%b%5Z{|7VP{qp)fNu*_dd1Sg1<vbsSP#bsf-VWtf?l3_gtp{4rYf$W`8=f<nY*psMTa8Tlw>p)n?16@#u?8;^#z^9~hf3I=@M6$MwssQz4xs=s_fyEz8ply!W{`5UYYtXmepFXe%twjql5wA3eNfZ(eKh>}y-?^_dj}PLAL&-!RTuddsVabj?<DzL@9r<Yi_f%$eZH^;iuG)t^qI<7X0Kdx@0M`>bDwEL9ojRWX*aHifL^}|@sTZ^ZGgeiXFB23F9tcD`%FZ0(E7zppDCXBOjQ&+`(`w)qtBGoSYi@7+MLx@n$JNQ)Yqjmh|5b5@+BgJ1^t^@>KSvbrk-zPQMq?q&pv<P)N}gRC&7kKFYftu!*6E^i{q8r>W$Vgtw3H_RG>5BtUgi^sF4T9Eq8K+fbdHfz|-<BaXP|!82|`Y#ws9LXQL}t3?sg7GM)rhluKP<A1|&%WFl%OMekw^dl=6nS28p*9)JfSQUd_VvdDXy)AUIHC9`2{Dv=Vnbp&mAO0hiBVs8(B=qngbt;~()@x|dp&O8N<D0--w44D<IPX`s?3y!M*TA?Px%Q3Y2<hsD07*~v?YZ}XYmya}jg-y`KmqLjw5iO2uNNgu(!Dv{+6Y814={qc4C@Zk?lQy(36sf{@iUgt$R6a$dm9~I3m0QI^+PYp#C<%uKZH{t}$0TprBVV+!{cT<T{I2`Y&}XQ&^GA;O9g`N0_RpdDd}=uCA$<zOP}FM2xW@;Z#+fRu#kYorf!-~L-MBH<$17`2xpnAuakoLBuCBU!<cDF-y%%{1^jyo7-c-apCMxl6QhqJIp0*aO^)>uTD5-a#G^cA;UWAq^bZ3GHo?%=MD)z2r<k-neENwt&fw_u20Wn4Uh#6a4d~{Uu!Ww$G!5ddIUQ1D2MIs<zHM#zTsu5ot;s`6AjBUgOYa50@m;_Bs^j8)ix5KDYgc1SAP}BoLC+OhJ^b03(gVap0xF~U4_=Wj5rx4|{FSoeLX!Kmu>m`0V`fYO+JRNrin_dYvy%9!r!c6y#Pz5yzp({V3r5X3l%C-xfbooCd36c=fSSw>o8oYnXtTr=*G@LtDXjAP+tBqsUlI96kOe>+9S%B>^O;nQtP$bQ{o~bRu{ctC+C0%2rNd^R@H#H-w`s&<Ij4Ty}+en}$^8umCwQe}M8Y9IylrQ`*+<)ksUqowf8RLc#Y6zB?P!iZ$I*ZAAOvTLjQH_^zA~<D|1+A%3@;So4OIllwLL~Sz^9dv>+8`im!KHwb;@&|>*%MwU&#@S>hQh+BiZJtEVFF<@SE}-bV0=JQwguzEib>zHeu|YcY6{q2MWe;?rP>vdNWBn#;%c6Fg>qg}-kSbqxvfKa{u{>qY{>U?qWCU6P0wf)|89}3UVD9t-@Xr|MlUx?PljERxcwVk>W{tUFwNaQz}`Pd7FGq&fO-heZzwc6$n@gN55fr;pdgCy+H}eielg@Otmzc*1235Fa1h~L4FA-ks@5|*BSD^&hQt+{t+0mF42^2pA%<eTf5m;)1YwU_rb5c_9B!dqQ-1%Ei^Bs*2FkaTmHg43Lmri6!2v(Kja*HtX~oAQYjk|;CkbQV@l2RuN%50CM#5J`a@3n#xW7Y=;<H=#vHABt-@_bioA~i996i6sHrx@Ual8i%^E1ajcFwu9Hy|(4E9K#Q>m^nG_4}&wf4b+Ot}Yk)i>LVAWugCzd7;1d9F4X9#LP9+Lzd<KG?x1le}AUX|9q9-v&z2;u<c(|g|vB<9|3*2ixykuSl{nj#;-xZ5OB$5Qc7&k%lg4;`roZJ{cc&)r^E(uB`73?@X7UpekMe`EdHTZ^B-r`{H|8>J4Poc<*&|)`02R{KJdrscjNmof6lA+Cgv6JP0!Tp!=hL}s94{Rm3rGLzA44}fBHoL@-jj{@`)rp>8D0qQYPAPPs0^xAj&Y5FranJH^yA%-Ch$16XEd&Sx2HW5g}wGD#Az56vRzG(ilQHX&Wfi6n>~ifwE_=p-VsLUAU=XmBZ&A*%QyK2KyW80UPwY_spc{`%!_9mzS`*6QuW;x46OfAyj#~$18~U|I%01ojP-s7F~t#nb0ipWOu4sQ_)$0ZL`H<%ekfpLTyb2s*Da(bFDAcao3-<rVjJ=Ld~$+ntI-s3SX2q(ffH{YOB6fHKi`NAQo6l%gC~N$+%O(AZ%7_!fIXiH!S<!>WVN`l5hjlLt|x^4j!9Z383M_-JQCqDY#pE^)qk7$3>kb3B#$mz&^(K!CO}U#(M=+X6&40)WI8d5m3pzwiO0?^Sv)L=M#e>hdj)y0-UzXnz7|;jG=4ZoKNKAX@5RnnfOS!sVUiDMc`)CwplQdEDOf()}K#Ler-OMH@qZap25;s)}>D+FOlW6Wj!@4A+tW<8`cIIRb0@t0aMh}!a#>?FzOuh!az8yA`gx;73RHB2V+=FPhV+JzxL_*hum)!Ps%qV&rsQ24=DN_v=MCBdb2CzoDk%Nbl8z&FNxzRrl`1~IHN8eV}FlHcPO`V49pruMUZP{paU)TfOY;kAgic1HiTOBOl-6+RL)R~9T15y%ko&}<1y@*yB}lfV)j=Y>`%(PiSVQG{E<cs#{_6hrx1y<(kmLg@Ae`<GPY1qu65yC%;Gc(2cqk4Nq<5wqeCx3iRYwP4i^bXt|Q_LLHn~pu#NGJirFsEQ7uko3!0@$|HpJx`X4?>XY<4_^Wx6tawGYyv$-ETo4ad366<VUhU<hP%_8=s&gQ8Ppf)!%S-<FSjz}2KqxVSpDh2RyB9vJK@a&7eP%~^7rU3z>Zefb;d*7_4z@A^~n>dT@`)UPBM3{`enRN*i_rk23xy*VLs=U=d#tI?Ud_vVMu*I2vCz3x=F@H7=L_Esh_fkjg(Zvna?(#=2K42>Eh}Rizt@NWhDEyv-70nKqsWCs4#UnUN@!nkA13(kl|CWzPyxlV(%P6!M!0?g4U3gtF3|J4C^q;d-T*fA?krGzV&WdLLyCx%9{I;pq)ALk#+8=QN>*HnCAISz-zT)0jFfG6Fh>REZuT7Z_jH@kQm<DM(|C{bN=yH{xUuH>ik9F088==N<j&Oz+HLLbe;i;Cp@W?jUVVGp?w}=8RA;sR5r;B|<5+jLv5e#JI^%Cd|H@pvSU|a5-00pmvH8pr(xt06!%MHe?qd5ZkOk`rj!+$Q5@*|c-nk~Pb=!g{!PMO(FYblg2DbZ1kEox%;E@<o`ftYrN@5H6*RFRnt9E^cqIflH&IRgnK)33_;Y}i>riO@1}NZuGN^Jqay2!G#|Gkyq+1Bea3B8)>YjcOr_C!~YF)B+htB)2oY*OM;DCY<5m&e(=XuI7`e*v)_s%oR2hE7pt>i^<`5f`+5#G`C~^B@{$N8V7?p5EUmE=S<U@cxUuiKivqqw>&0ebuumO*}5l~PPK)XAfCNM-NiNcP3U&=>A!Y=+FO+NV^<>5PK5X6-$NAzbQQb~^=n??_rSH0Ki2Tm{q#w7QY54!@;|#`9e^^7;*JJoLJvn5gV-98t53Dc?<=mUe2UB$L7O(AVk|{rFZ!+{ExTvgZ4V{ZB+@oxHD--zq|~-78t{=(q~>H0#6l_Osrh7;Y;_XP<Rx=>*y1{ix3qDoeL^W_v`MEuaq4_@5&=k6no+U_Bu_^q8cj7be1tO+j?6g^8!+H**2MRLuViPG@XV@`n!O`6Wl~xlBiAP63(GrsMG9Y*T>$f3k*gT~N>c8K@D!<SvmG7%Pb4TNFMbvasd78)FooOqcRomKHwq@NF>PJ{yj=^fk_=rjYDxhliS*7a8g#OgdT?ueRxMf@5nPT-BrHH&n#5)TqTI44>C|3o&ftD2Vv}sB^6&!rB{v3bUYIV-n_7e+EFCv)zFI~h7vUP``C)X_UJ2Rkz6pdg|Azase)u6~+=0}`@z(Xff??h<d$@ljk5$CBuU?Fxr?K+`X;o<uKn}j=t#l5RqB1td)6D1%2Sk(I$*2OuBP?eCK^1|x9B(JV5Pal-su3Mpn51(2J-pfCZSk2~$i*YeL%KofLHyG}`KS;+D{no(*$KL;gBMyffCM^%3OsW&BI$7weKpUCTgzaEEzh&t;x4kfc~t1S15h(tr41b!`5vU_D4E{yvD3bwBK-frgRDD3CavzcBgD>J?jf)Yeuv9QV4(5-PH*`<mcfH!FZ!$SbXn|c=}{#_s?obyKd4Y@%t&*c_^cuj42}2+SSLebY?OSlW}(jb@J$WI^0KT>D-gBPAZ-ClZVfXq+F-;2suOA(?}X6_Wb}>pby;N~la2}MO^OU3J_(^owa^{7q51g_Ga>3_lI9F~-DRQl)6x5q#IOiNkbIdP6TRKeT;<08j8(?LTW<^M;$ixt8TI}okFz`pU$G;_QK6Fraqfl%e}B~st{|ro|CFLp?=m|PAN}&orrb;=nU#(?y`J&R!OpB9_u{6d!M3|rHCJR_p%OYT9_6SH?d|dgIN6?+i1_)x^HTPhI}{zG48C{<KX%zy$foh(!McJCXr&@jjHJG65gsFpayNusSD9qE>WYWD-%nr;?2LeAA|5?H;Lk0e-vP!;9i=cOWeXUN{78f=xx&VZW!xCR7+(iGpc2P@_`SU|rYat=?!&Nw(<w5vV3q&4>cbDW@>62hm$~eQ-Z3IX2+MYu*dS($Y@foe{khUa-c?;03ekg?H^v?a_lD7MzeVXj(fw{tZ1^YsqM^BCr7BNOCw_8b0*sL>+9+uhP;}>up9b`RR_u+h;1J|_Sd=pEBzcO&Wg#PRqeVmPP0OCuvTIP4AzP+J(&cPU51PR?w_5(0>FX)Wn=Ri`Wy#ZI#j2Z#UAs|^N0T@%B)G#;ECY{%<aI;MoSKc3%?dIK%*NFa$&X*>N2b;B8|~utU8%OB<)kF6F$i-BEv(E?FDw~By_=*xj7hz&OlOucC<(4*97nUFwHHDqR1Q_G<XjwNda;_MP?hJ+S?lIDl-E`tZoLK;dh=*6bi!hiqQCG(<BOtLuTm-FFRRg#dhbq!#zGoj6!C(@3+$_<n-UBwHNWflxtaz;Jxm*wCV*_;G~h<3a4xVS2`5U5AcgR=KUF;VCj0!0-2Xc!fNnq$kA>os03QM;mw_8%YCsVMdzaZqr%X2dVB~J%YR?YGii5$jBcu^N#f{Q+UZCitM_N8JkQy&lZ1Yi>1G-LZLXK*y(_ulSd7K0q90Qd+f(33mJ~Mr@<Jo}Rz9CM9u#T#*1Sm&C1W)9HD(16cP5CGE<K&cmLTG#|x~`s`a<&?gwc7DK_d66AeMQ;#0=&1xFJ$`tfi+a39CwIFJf#)L;lXk*8-=LSLWPG$-&mJk2|QDrGD`U;N+;!?UWZ`|?2w<qqve}3X1>~o0Q1#|DFGYRAaJ3nP|yhy7a3zNU-|js44Cc33%q4_w#xp&nEA5k^{uOoMYHmV*c9tq8<H-X)v#ozpjLBx$9Yd|O?Apt`$Ap@a1SB_T~);+ezyX;WY#zG4Vm^v5{j>nWPWmjL9Nt;rurAks>UQV2Tb2)CZW{%>B4NCNAvzFArC&@Gg#{s@|#GKh5NxPwPg2bW++ZKK4$anhn!-e8l$GFMx{DdA<nIXTpQoYd@yxswFrBfCf}831I3yiFR_LCL~9i`+YCmVD0RkjxhAhGY3-H7+h2r=G6TwXHT6r=Sog7CzF;Fl4IVYxJSPhb9tueBu{d2W@V~XRNAU+gd2v6)?Uhu=4x7-l7G*TWk4aR^HnJHas1%Jf+2u}%gOOme6T-7PL+hhXi1nOFxi&+r@d|lB&_GJQ%h;m$QoBc~G_en0?>X%rg`dEF2qra(D@T{XIw3ZJ0$S2z6v}E}2`jw_D;aPlYk=rfMWP+&cU4x(6`3f@<@KC>J2=3go(xx7jR(^xTmTr>Og4n~m~8k5zftTuA6;kHDcAn^8ql4ef$qxILOXt$W+xlX4z+_6+P|J@r#olbp^#Z~iEL+3K{1{o@tDN}Tu^wtG{#^TAbH7{c7*zP5h||{DzB;CbrU2H=lsGdx;W>COgnwW=5@s84Z`N}7=!0UlXVr{D_ZNzW1U0wP(O*52?+$?BC%_*z3v>gr=B%D!*Ex;Fs~Hx62BM8BFIglNw0_SRlZ5@Dy+ro*hKUZ6CnDX^vyx^RaC)_gJ09v@e;tlYf~}wcp9xM&)k1s`7#ylRgeQ17nWruVjM=5Oj&ygCmL!EE{bIxB2alNF-`>ICc*q_FlLDvmEK#PzQOEv1Xf@{v_ukgy*5F?g*fUxzyupNV%LmnEmmL=LL<WE2sj9BgO6{M!7!vfhbwI%>(^@L;)JHDyiwH8gko_GH-<|$atXl#j)P0RdHR;=S-GCQ3m~>uMjA2<*fEB&Rb6mBvSqhfjci!KYufSS(OlrpO)2F8UV%aWMOXVZ?)(2fBBh<r-{zCQgCCdfJZXw1nXyAaT6oyHvRs3*#4JpsuW2Aw;nAWafMPOmDXN?Ug>basWUyK{;X2g9V@TknLx8vTV&-CISZxPLHQ}?L=>V~IA~dRTQLe%-WjD{!cspv-sk#w8gD70r(I`*8qX>#&KJg@+L6|B*jg0nn9YGzPwF7^`t)z+8nuLqk!Wa+Lv&NoYju}X+EVfIOO`LiHplz3;f<SAhxHsiudf(PM<e6>q990^ch>fH3O=oGU^jE&F>eLe~Nx^UPS3nqw*9UcUd?N@$V<imjm*hzEa#X%dj>L*o1V42jM%*BCNM0pHEae+2fyS}&)Zt)Mp2$O{%F`1(q47DM(B^|PBmMd3>m)KF>y$sm{3>f54Oq>Tsg!5Ool&V0dm1Iq7GJyRpUyhvkYZKl&I;YAEs;|Q-UNLNx94;2ETg1kIc1)RuC8$8v@t3XcuebAhQ6iiAFx@d3BcmMB-J_g917O9<#zc|m_7@5VPsni(kO18_*cu-m|pCd)|{#nahdOnQ-ZHdyqmH1K4$&uzm1F?4WBkAKR<GISd>$&PQx%AGyj)IvLMIop`TZiVH|>*h@#TUDq+>cMW{DuC17pS!Huu$7DVFoz5nK`Y&hMEA`5l?q%Ed1JDkYRgo#FR-$XoW9@|doI){<xzI>dBt!@RVp30h(v_vx@n@pK2T2W#F&y;*>0k320VHaFx0Uu!_^9_U32R%1HwCqwJf*w3G<4~rnEtG^7(@8PbX(1RH@Jd@n{{R=^^aMgpxhsPO{t1a|GXsZ{G=A1hifNpp@e~?Or|CG)3V2>QfAz80m(tX-(1R-nj;Pg$p<BTvmECITp=Om8c#wpw{B*ThRqmn3=uje>tN?%fE1)RXcDCiUKg~))ZGr4wE28owE6D({j1x+dDxX4t>Wq>^`Wj`Lw0^FjqRt6taI-8{5=KlsKl`D4N6d?X9?mJsi<R6lMN#J9LF{JCe-6;U0JT}1r5Ofsleo%>Lth`sZ6GZzZ23zsrptK2!+DlstSxc&Yxu<~#y41o=pw}!sayE0nrB$X1m0Hv?^8r$$sm`fTw_sOV`2@X@8Cx$%N9AKJc^ufjkOELu?lDzQ5V5=l0&H}q{My~fe|sh5xCI11trl-`Rl$3!j<vAe3#tgwaGO|pyet4I_hY=ZhmE(UtZkAyZPioeNhx+%tk*qxs-MZ=}8JZ$kd%oD|i!VX#fm<#>KLospdpt3$%}wQEN#3sa9+u$+go_+<+c25+^o~DuvxmokuO(#G1;6nB6HCivgpU7Xx*oR1N%?+eTYPN7b^^WOg>qaeUElUSL4_7QKt!fCAyZG9Z1<x)JBaW58jF(l2NcKVkzJREz;2+AEYS2N2^UVe=4bhK+FXxH{4c2%>_Zp*uLC0S8e%@xDJ&1PSfDAbU>WI;(Y}HoB`p1mO$6<cykWq!h>%9;NRMq+{AKo3N@F_|F7ixU<4cZ)8m|m@p5@f0f)Re2y=bh^>{BRM3p0`p%swn+#T}6K?H-8F$<ZelMLKUgyzzCMimf^)axKl0;AbUa63y+qp3<Vkyw@2j4eeOEy*_g^Xx-OJGgOYKiPX(-KCSmWCWH!${D=9Y*K_qrV9Z(wxweAZW=b5{!E_Y)(tkEs6M52Ani!z$w#bWn`p@H-fYk@)ht&i=}AS`0Sk?-~;7~iWAujg5dXhbn9^JXp{XZM@#b+u?#&w%w!o7?}3InUgyMF5)CccaOy~>`7jHoQ-`_7vMgq5A{t_Sa?Uce7~^#;2P2;zaH$mO1kd-{<7zOvWtexxnz*5%hi_gED{@=xqBk>^q1DH(O5zk7`3qm8zZswRH|u^=eB`yZoVmYQg+n_-T6DJ4NU7o?5ng40I}^r9RktrKb^Bz5PKfZ#>)f6z_EoPl7#CiqW^Fn^WmK)Xy@&+XFXh5RO!H4ZPeR&r-af*R-9MOZ1<l1HC+vg!OoSYdSnK7f>>u2t#Bg2s*@L4{c)UMyQbibRbSge#oJzP?BFct_7*;rzQ{nafBRW1lR%h7*K%^^9s>2cS-FNV3Tya5*3MD-FW95;_56oxkY1~^w+@9|qjwT8`MyUu`|E*VG@<MC{%hTp~z<?q<_uxbmk3Hy?m=<kqH%!)>CLni1#*~@Zh+zmr1M`Z$2828)18JwLjap^LA@>4ew%BhNVRI8?X$;^Ne+RDj2qNW(iF?3qvbMSpyrCbLgYQ5p9vELBsmRB*6)&EEgPU*<PX;}cL-8G2yMUmG$#8xE1^P`m0!#ub$Fu^f1k#6Us*@qUwS6j7=EH^S`JcLfEv8Rm_>5!lNIRI2zaB&pP;7p$yb4?Egd}XC^qQ%F!C4dKT`4~sc1&kv!h$?R0wmZ*r;IS0x_Oq>m?$W~JQ#QEOrCH&B0zgGwPF*%I4BPvND&jgP=JP_jMb;e8+yj5n%T1bgj+p$Z&ty0rnnM6bG){mp?-@qe=etBhwd{${lrIn)UvtZXB&f3fYJrPNEPGQVr1aFAbRwMX)$<~D}E%@icfjH1z@smT$3#yE0U{Xeb-&=8)nbEPR?y<6{|pw>sWV*oe&Zg<AIY$W8fNC4rO&(@5Wz$GOT!|b@v8oIJNF=jW42K#pkU1-YK)d=Bi~j!QzM+l7UTr-Kkxdawl1?Fz=_W6GG0TMNjBCR%=B!;xN&76cU6mD}bSukq&D@DFc&N7L1NSWd3ZNpz0G)6RgQAEUmuxX;Y(y4l6dD(4QV>nFXh=dm~Mscu@bqtL$DpMrzG)oM=W+YL9T0d-^W}%ULYKU|H^1Q3-u$N#NWS2e|A{UD&MS_6A*)Su2Evz;=Tc5j1Kd%#K4Jc7y4ngEDp#9=l?};<hi*8%rw6{DABQb-VJAeo7MT?VY*G0}GkNi6EZ)!EJ=O8_<r_+h^(5?iJpLBl}nyv5hggutEnfYwNrWPY{BHHb0jh=N8o&0jEatyoIg%@83tac}s&f^VlaHZIUG{nwu1Iqi$D2Zq<lL*s&-dfx=R9mB^Ch6K-m1*uo3yY6a<3(2G6fm6Ec|fvJepEOfNR$hTq8OP+EB6xMCtSVL3!?i*L-DusA{g8d|#A7vs1tb=jVs-pqsx8+joq&jLyS&!swwhFQ^V<rA78|g$eJkn^6%}Q*xdX^$p5{unFdb9JepDR}h+5Xs*dA?JdS=^!SNTSIWmoti235hw7YPUBp7^mNE{agrn(7L6CT**R~&u+c^iPL;*H|ZQ_^8IvF*NF@+KwBH9WNVoYZRLMH82*t6ePZxX>ebV0IpZ95)-F(MazJzD$O3&NWr^Q_|D$}Iv0&Z64SycemdywtvZdv`ccPERn+e&6$bxu|W)HDE_Iw~oz{X-V*uEGb#*4TAqgOLD7Ath~WY6LH6%B{+){42S=UWZO%FwKm+m0GHT!B)8p0^j0`xFlcd(QLyglG$mPwB*Zwk)Rpx)Q84K&$)N5>e;f&mevn*k0JwrPyOu+}1+v#P(h}8;f=G<ZQG=s%-%iTO%@szwnKM&UGcGI)~1AgE_)h81>3a0d#o=pi?(cVl^m(LxTXiU=4m2c+ME?QU%bZ3ZP3*GT5b&!OlZL03l+)<6>FLWV6(%a+So6vn$3IQ`w#2=F%B%E>+xIAkps}I>(DSVY4Hf;f&Dk$8*r!lF+Vuj?nHRGR{{`5&s;s-SJ(S?b0c;ofnkn3&O;|5m2~4^|HO}HJUhAs#Pn&1ZUNR(|v6xLU-%QUJ-=Ct>=OWPPkG*U}ptqU&Go#bGdL(ys!(xH)S2Rmr4fm{Hy9ss5PkeoW5O}V>qT(4d~^85I@aYsB1UYXd>6-f*ut@>z22$k|>V<*{_?2fi60s)VIDeiIIVUlbgGV0f(eYuwrjajf8@F3$fCY@*&})vO3o!+7E73Ti@V-W{igw>U+euyJRhK>lpn=AjPht#0X*)?VOKFByJ-GQoMMF;ft<W_<{K}j}3>dF%;ZeQ?GtiLgvbvOi^AkZG(U^!qK-(NJHW;!pvA#ulX{>#}JFj%S*L~lokRBqCmY)f6IN$n>?Y=oUI{RaAYq=-pVh9{L-4tPstoj)h52A%<vOYN$(_-cUf5NA`MnlfH0%MYNNcKQ(`<hM`c<O2oz3uWZ(xaxbZqKw8v#`yyk=(kJ*f_V%!?Zlch8DoJOU7X_<V5^mq(9<IHtxMd4+lqe2|W&z|Y#P;)i07(M5X@gsLk*=X3@5A#7|LG#mOW5{ctmd;sCd@;?WmGyy`9RJpP<!yUsp~@#vn4NX_`*R>B6@5-=LZVt(O+`}4h1$caY0I+m44Qd?GQ{b7eXdG?LXFL5ZmwzYC9~*DWdIEylk03XP$mG~V%*N{Ld!i~*8?1-E6Y&a!kCWKMpprvN4Jo!Y(6Zn(Vc%GG!uf2Dew7vTYJh|lvyw%14z~4hR;ZDH_A4o6*2^8GT2)E3B<&SBdAzFG@29FT_!Sp`iZB)^dP};5g)lHiUEUS!07#BHA3J;({qq{y{p_54KvR6mNn?QU@8bm1M2ykSSpR|CzZ-8v#Bz+O7yT+66DNL*g9A)JI**Fe41z(Ld980bm4O~;YzodB!bpK9*paQ2&LKy&Aa$K89QRE-I$&DsRd&W!YV7&F+EN%ROp1)^dnSs`kh5lKlW|2si>P;rKuY{@8(Z)$f>q$b7qaHBaPe|YTupxY0$ule8avanrsuE^Nt>0;)77^v4EV?BbJ*oozr`xBB6V@=2{N(Zgus4FS@{qD=ae>zN)xe7nd4lpHeSq8i@z=wVdSk1Y`Q+Qy<N@zxvYf6hEkbz->ON_;NLb@PfK0VL9bzTXszBDHrMo=~De54;DrED^Uc-uZ0yxYnMQXsK-s<cMx$iv{-jUYx)t5xF{PC@L23ew0-ChQmqqU*IqADDQl!sMiddQZB54jW&R_TP82r&^qZDV$zN$U#b3#$Ozntjm`dtJ{A!c{{7ebpLK5X-3t|qI&wimE0Fxh2G#{pu=EIpJK$?;$%l^ZFwCyHLsgy6~+5n6GL)|Yr<L}(1oC=R8wKzPkHaydO*wyC4do>?sF;<;*9(va4Uf+3mJjt?rGrJA{{?{gVS}}=VzvAh{n)jsW>5K~0ct9_QaOgsnFMOFnFU%P9LbM{&7|1n~JA6R^)ml(=4Z%l$y;*5a1sX}fn-r%pIoOO5-Hh#=QHA%$K`^?>9rfr>#IudHg<Y89`&tNT4@S6PsUTkY3$e%_SO)pGrk2Qn>5RRu@u=|-NA_5|BFoI}2LdMsYxYdBc1I-N3=HHRYrh}+2_cXX4UUFI)2r3QtI}&=|MJ;}*v|&6zs7vEhi|x|5h=EHtNz0*s0Lvw!N{xxQ2yNeW0^c_uPWM+AP!L$<ANE6C-R<r-}}cEGky>x!!LuA9v&r;#d55QSDHC)x)SmRntbTUniQ<1S0ZX<$31cbAR{C3lT%w0*3=-t2DRz3=$y+(&}=K1hd(gA2=O|0(FJ@dj;A&RGmps%Ic2@Hg91*>tm8lK{)}%rzxx^5i}nM-W1;?A4*M0uP7ROTG#_1m1Da<n?1;6!y?1v^3kC=mhEE8qD({w?9v-;O6)T-}HnIVlhk#C{-ZGU!=p;1Hvc^l1J1@n$?*a-O!UInZoED75eKFm~F^P)rS{;$T#KPcZ+#kxHq6fme(By5f^~6UIb~k^wbym`1hflIHnf-F|`rDuH_UGGpe%*h*jquwDzm4$QpKl}lE`Nrv<j?Tx&*s;>o4<~0{?dQGC;#DXmcGZa&0pPj<=@F;8(#g{^yHtf`t0wVferpk{TaTZKl6+KWKXLRS?bUERq4<1UH^(d7r*-#{hp-m7pu%)e96Bq`AaXR`b+cjQz<)s;a|hU#9FSZe=;Xxzf>+2KmLrLoe2L=*zZT~RDp2(o+UGBvQWS?R61}9ToH0X*5DQe9g_c|<iJxk{1PFD)Mdb&dN7!#XjM%{z6#bvvE|p_V>Ez({aE9eODe7{f2=2~)-&wITamTtPy685z;*K3Yk!WM>{1z<E>AD6D-fIKcVW7t*^#Q)*iA)FlJTbOlG5x`e)?1u*0Jtyb#03?1wHhvw5pKD3h(SAej4`qQ=l5c;=ZC36YMUg+qWV0^^WR;aFWRLZhAU8EX~KwR+If%FKKxf;yiL{zMd2f=a;>BWxBhw`{GH)2Q+&GVkj0luQB@0Cxbto3=?PZa@qvH_@KT~Mdx|}D4ipV-`OlhDJj|S`tiEXV84v7)MB?4=MuZ8rWd2Vf^UhlE99Sxe}f%hUHtVG{Y#L;<+q;x;P~!^k9V{4`{zD;@c_R(`RPp=LjUwm{q;+F_L{%sEzb`K7Y;c2REn2|-M{4Crvom(%fX+2cKqeq6uR_c7`e6=hXs4Zhs6m`&NiMZywiPMd+4riHM)}V`1z5qICDBZ;NqYy&Jf%a$5_&!4uz`|)z<rR7+>%RgnX#a+MoTqWDgIO4Qp9)`U@{6R{CnVZ??^Ah;QP=s+2FYD$M{VUkU4t;5Xqig#99!(gMgH7by1b9K}wEo*?WZ80^;N5*GONt`>VY=X^J3Ma%RJAW%ww@)aC9-(vy3OtDB7g<C4Hr5NvpJYvQDUI`l1&W%HdP1U<fC}VOLVCn<W48dMTpwk^CM?~F-N`vrd^fWOX!^{=)s*a5WI-<fE-6j;sB6|46-XLY(fyZM7unAJf57jaKE+`KGH@BwTqbRb(cVHKT4)}XRM^v8Gz*`moeAEFzVHRh;m*5Ycyfgyyz3DJ?2Dk>9jvlo=^Me!1Ygd^Il4`U6>o<C}lX`Gm@czp!_!n}hl{KG}q^mBk`Ic)w#HX59nq~7!o)M^pMgPjIdF2x2m8VjPO4RCMym<nZ-bX1^eo-k}KBNiww{2#X8~^1m%?%VQ^k%*2=Ke%Y+-RDZA#NTkMzQx@t3J+3yX2rdOh|w?O*yTxopnP9#?q1NhO^S6#g~ntiEu06$piqPdT!7Jp}fo>)@~`Fwrl`hv2|Vz_Zy-GAOxn~mcV=f`}jx<+O-6G1`&6Vm+6tZVB`;@WTZ!+vqH~x>I6ze+hA82nJ{Pn<*#hisbdz2LZ62GTAOa;yIa4Jnjy3&pg0JGQ@?1M2OZO3^k$g?)MY}CW1rQ8WBRNBF0AuJ6ofvbRJoYIh)b9?A7FXTd(x;Lo3P5D2Fc1BtV2&&V=*2$KYP9J%E%pLeYpA#SW&=29DMryza0iII1~F?j$gYRzg)+!zchaRa{RU&zkUnEOc}p6@$#rAB$-NDJYwB*xa~NcfL?*mqy4G-HTNI*=9dY~>HxW89~ai0zX6{OoZ?N&M^C1Ibi_AoQ74+8A_~Mm=LRG+YQBkUYE*RK5*5-l(===AR8X6@WECDMnJK<1{4(jA$d|`(3QQI)4*0CRa+_AhvY&{6$6EYRf@BvPK-|%VPX_d0Qw|UB{v@!2CRGl3QGu6jy@QpNU=f*#NPgOiQPYc+^ShSB*PO?TrgLTLJYi@1AM^u(%N@K#ynYxd8+?@FG8Bg}tEo_wxIe*Cwrbw096!JME_?mp^7q}HuOtc^cUMWo%3E!1g{efp<TocBLM-#OH`Org>3p6PMuL&si)eOmhmHzWkuA-G>-p!w{>0r3aG}FidOPUN2frHhU6ZK=ca*o!OzU-hSg*-0qgKsgMvr_wffnM<p*J)|Qta<6lfy)!AN4xH-O@3TA`$M6ElI_4kQg6hzor*<3?OD)!L`AIS~<xE$Mg?BjRpU<ci&!O!GHR7V!^+7Qk3TVPl(dQ3lQ*u5b$F8uF26TN%jI1_)~H;{UtdXk@c)EDbn;K9GuLV%g%aI0eXpbPPp*&RCB#Ms3qY^U7D^!!+Rp<&e7p>b(%b>)8J}P0OB8C0f@r`;W+GE#fS@d+g?G61I~Pk6i+jxcqgQI2;%q>I`~<zcpkyxD|pSn-SFan?`y-0Kh-<gB(e~FX|VXNH#L*4dj=_96)ff~M8<wHqQhHPDTpdGJkO!w<S3q#p|JUyVNeyZXhw|q86`>@dw;EM%Z+MAU4@Cq6PWm%FhzwOy6tR_Qb&$gi<+R}Y^T>O=BGL`-i_#Rmd?0Bt)X%Zv4%@3>sMHdK74Y;|8MWL-<MW-!JL&%PA7j!<}AinC(K#?<;+<f6%sBpXIW!o6QelUywPT{z*L#DT0UgSk+XwyuDUXHF|>7hhK1w`yL+jnj-YMjN3~gD(39Hc!L;k65yDHsLR@MQ&g|aGc85@_OCWzJUuN-sS~e+k^C=mT{AtAbY$5-QPD`voe3W1NeEbXVZ$2v7cf#b>#M%n8oR1xo0Nrdp_M`?1ub7WtmdTC&k4;JPv5rh`-5HZx5SvtRBSZGWZbq@_oKd=QD^DZQ6kVY8%PeL~)>U=Z7Pr@=jp!;^J@c*@O1QUTcpE3Ce_~=z-7{t=qo(A_rOKA-O^3DCXUc5&1CZ`fnDG;EhvgOag>+;$_^3I)BIV)@by(V}y|Pn$#~9}kx>tADm#x`hRYJ}^TQ(D8G-`y^fU9_I_F~*2ucKq|LtUuvCSx`QcgtYXU`hO`kWO*jUMW+abTA*ziY#!_JeFi~$4IH8aY^Apr!5CJLFPl0yms2+xw9_^;eA=V8*-N_q-US)R*^=DzIa&qcE}qKrmEPf%jbp>Y*lOn<LzHvBsX3tm~kz?F&E6B_{=idi{Qx;bB#Y;oXL3gus(Z+ihj04%O!7=(dQDqQ0$?1BkpOs5%4VKn$uIq_ksWiem}e<E-EtNz&q&K%dWQi;#QjkYXhI2S=ot`+AC~WnGj8+3Xw7AQ<hi^oR}J2G@6<y8H5>8HJEeojYq&p2w`9=E$6N)kG%nzrth*^%X!Wfl6qn#Ptihxh8xWVrbXHIx(=HYxnIUPE2fo5a)!$|@>JQGd~4R?q~K4ej!bwzDdNBL^Y45c<KR0w-;|H*&OPrrug)c(J2MWRX~%_UeD1h#xcj-o9nMG!gHouk+&)%Mc-vG1U)D5p^|^OH7e4o&ewW<Yk(5G5%E~2fZIoiqWEn-)pNexq83rpBm+5ILrc{O(0T#xom=<N$NS($J5)nz5C>i|5AtA*{+5!mR1Ug*18A5=~i9<0lbbNN?vj7=3CD=NZki4N?Gx?KOIc$|SFoZhK12Gpo*ufYeSf<3xq_!sW7LvJ3eGti|2=KcU#ID~o+K6%GcTBhV0e=P(y+|&;qfoAzDL1UJA>Dj~TU(KRHdm1su(y*7%zzOhQ!B6i+GQHIBRpfD*efaL;`^R#kE9y=kz`!lfn06FR^Tnt!=*6j4qTA4P#)=!ts7eMeq@`n(EO2ShyxCeqE-_Dc3Z_?${bm9|4QXx9_Cn`Oy)%BV6z}dqJfb8hkW<r@yv86cD$-GRCg}?f?hnjT_kh9w4JcsFj8sAx8Ip@DU;~7Hj?8pk_{~-D=QfJiI>1U9%CZ{k3sxHfsAna1=TFnz*ufT4Ht^hIOqN!n;5mf#Yy<FbuMESmBmx8s7b>w7DMgJv+N&X*NV;GJs`KbD;xC@>Ig%*|65!_nIC<JTg%v8-EL12>co-Tp>6f!@^o=P_^eE?Jt=08x=i1pGC+x&2C(O$D)0ajdu+A2#mGH?Y~PouPscJGi!Zgt{JZ5k-DcQicttmE*P<TKu|j8bQQny*OL_6nykdXr)9|V9eix_d4(ZiMTJU&>CC~+wnG+|+$5to;MT;M+=HA_~cnH$n-gljB0&Ix+K*OkVig0&Jav5xTgU}_?F~-7KOJpd_7~p13(uPhFmcynxMveQHY%qn3yD<fH#9Y}iy2kZG{s({Fi_T^PN<3ubxwqsy%L3kwd~A2D*O1t1y^MRil}Q0ax7472|3&WX^@P{nT-Db)F&Q3AnRb``n3Xp!o^x-eiQ>5FY}2^n(?AyD3dEx9NO{H~NDIe&I>U=RYEIMSCptQ(xf;gIo_l$jYuTof3fS^OJ7*P1V;CIgRG26QA)Cw8&6Xa3`JcoGV<gYWDAu;UXrj><iI#ScXOZ(YZo#IO#ptC|7d(W1%sA5Fvh)s(o95KkQaTHk=3!!@z+=jaNh)l|c(?qO-y2a7s(2W~D4PheA?GVw#oArZO|oW)`QDn=*?t~%zyCGyUtOh5{b)w>R_5LJV2cym4JxdcCNH^ib7dwDYtC^YsGH)7hrDL^4YrCP>1#NXCIyn}HsykKCm2RTTyX)#4(9m=sIq9A?X|l~Jd;JJ2WqxT(4e6^BF}m6NS;35lXIxuT_7`|oyA=ExOgx(@?+|@tWQNlaA%gse!%z-(pE=15=<8zs@gaKlQ4;}cp={tsbbrzs31fVJjoRbk_H2ZgX)D&<K&H2g9`@Rr{`(FPjk-7{@>b?6=mJ%1*9s`D%p6{=IH&A2#;`9qw(^&>d0g<b^M>d!>TGQB$K1~MTM0G;SQc!^F)vrUl!p7Nqy5)J(ae;z(nt7R^Ai$rcf_E5$d_hsCp&Zo0nJCKUd|I^#9r9-Ll&G5^>ov;M<WPty#=mGliEVW<mOrWaDff-!@fWJV|kuxYtpkLT8Bc4PELzwx=VPy`|Sp!a}*EBf~dBkD5lyf>6>K1duWiVkf|hu#^osf*bL_(?i7dP*#GwKlA1gSSiPBl0hrGu*jrs1ipzP5~@UwkOLyLS{TckMeMkVcal8xRi=Sq?zn4*afgM|Rc=a3p44Wt-mZ$nG}Ry|1sO*$!)5R1EQ>*zvF;+dxXLuV&Ah7MY(yMERjMg1zH+`oG`9{F{c)P7lah^gDl&GjLnSDzZfy7<Q~p=oZ+S5FjKb%|-#nn0cMz&%1A`y;POO>5@IM@#G_hN?TJFhW-Id>*cm^X$rAl<ZV)nc_V#hoRq78nfaF>D#4A3<luz&3%OH~wV#bX4}-?aq!mH>J?z+Jp$reN)j>WoneV_FeKAs-QbDM9c}@aPihKCYQdPACI?AB7pW=W;0Dcs~^LY)FGPSZ`dQ$~K{xZktF^1vixi5nO^E1)w>oD;SNdfvxvOOGRD64F$qn?U4KH@1sOUhN{bAM==_x^1MWrz(1AGDVkk;q1X`?Lxvn^Y)-3Wjcthdg*4=@ZOHd-?SiLzM^S~_OtNB<%Vri&YoW}E6SdZE5ub<#&K!}m+HLbh?KVn<MV$KpFqRuM7e=bZT+C%3jlJaK3HTKtUz^?9K>oX6hCr!JYV=_oZhkKIyZ`+|I%};Pg|DBX4{xv?UvSnM)o!n3;UQZ{fLNWF-NlK?M0~vFsX@ZR$C0;Lg<H)^%+RW#WD`?zEPw%ALlitUD|eus?OPGoB7#|!xx>$P@r?GctIihz(Y5n*Bn!t$i`RDBo-&1(UGjFEj7>PE1ygwYVVT02Rq%h{bXO{4aerx7Dn3k;9*^RlObENmzk4d?@wOTYQUbJp<nm@wzRbR1k1*$vTN1X0!R<Pvx&jdb1N{ZyeHnRu()ktkxUiMF6g82H?fa-~7ftvy!4@<S@rz8-h0iF^SElX9JiznCtdp|>>62wrSCqM?#H6OSUI#+CJl;KHu{^LPC0ZG{O?a1c2}$rE<-I*l9_VuoUKntOy&d)sZboLm?5#gx%RWK`^-J+dE7!2QEH&KaS{Tk3l_-gX)i$oG@Xq|#FbS?1s3mnq*p0no)VRkOu=7VMUt>_((8YX-;4oy@ETaUqVfio3B)is1gCd3Xz&RC1&0z`-R~<>LjdFAki?A*p;Q&~Vm262IKUW@JOL;g^fCkSTeQHF@vNrP9ew#pQuK5cciXB%VH5E^jpebs28r32zq{d*0;z?*(_m49-f$$nx<3?`6h)E1)39m{d$|lbR9GVL8suGFb0t$=!rF-2N_7L$*)I9ZL83;R(hD@y)w^flE{=)j_3VZlBem<OqD_SF%m_x1FyQj5A=qymbsXdvP-9lNU4QF^+%8GQU#+TL<VM;MGu&jNxlyP?M8TjD>9b00kvc*_3Ihf9aCSyeIbnO<(A}{e84pmg}n#(X37rCWTt5nV37_Z@vSl{s$J4Xo^%K)Nb_G5Hwus=7Jbw;K2@{4MZwfXm3*oP&w(XokmASViYgiS6Ro`hPDxv_Un9Y9paP&e_dQ4z1I>Mb%achKD28Au<U#Rv5$k#g=M>u$y?kJeDkWGyeoSNnKmg7$!~kUE#0#AL<G3cI&P*@HTZ@70)$J?Jx!+mGzIJ?McTQKhz3D?)F1FZ`e}o^0=?0>&0?X%0oV12#vsG?g0>qTi@ee&34}lgpZX<W9&WYX|?!^}4#UWj-*uBypZZnrSX|Y|i(FWkRy3p~z~MI0)u?F*Ns*Be{nu?nx-L-r?OxloxT5`#o;umK&VOc9d1LwtP2|?<fO@haJ+oYju?=W0S+(*6q76>?c_nem9Z>s|}Z~h#PL0M~J9ojjlo1s~?$@<c?48KX!l4uYcx-N8eDThdT3V_?bi!6ZcQKA0xTT%YKT>|LDrF+kf})oM$Jw^6xFbcl-!ltev-?aA#NbqAS5*U|R30xoiCO|F(>l9eBsDo^Z#8?Ai51mWuHTrYyc<eSU4XxQuAWg#LaK&`r;d#`$e-iDd!gVEG@K53z)PR7UBKer57313l`r^rd5Uq?wjoIMTP(i{`$Uca9y7W2%?Vb7vh|QJyompv-W#1Q6YhO+2>Y&>L%z%?gT^y2*KlaMi3;zG3BOa+^mCs6?_l8+DZRx8~w&om}*sBTJygbB-*sRNOJWzjM#ItTj%{?JZV*^G9DD&73O~GpjsDx1L8c`9;wTLz%svgO|0Qf*7jcSRB((r<hS(?Lt3|VA6#MhT%&;mc`-yF2a|Fne%>{^mn8wK<j~9hA(M0{0v<B`*1f#E!PG<)sW>5m>AsDU-@k!=Ke%WilkbWAxrzhu9SHfz`QZ#Qddehb)}dJm7rD6G^WJUt`u)wDfHQDV@k_NremR9?b?b_vieb0R0T(K)YOmC%=%H97xbgtEc#I_Oo{I^M){wgG{s+z(}al4iO_^kcH}h4RYyL?XJ}2bVJ2C=3QJBCW;PmUv?lRO@)!k6gGAM9*>-8wH5S<VsgC?4n-QDlgdGU1Qwb5-g<6%SGl`fy3cdpf5o%@u3gu;;)^adr(ArGrDU}HU72+|m5SMHwWgel20+TDf*Qu2L$ORsw5=`{4IO(A>7=5RVW%_=3!Vk>2-3mKe9As9wVDA_T+%dc$gAtu7*pZLbUF?jIATb)~Wq=5zEq~q-HtQ?5frM4yv<1-xSula_S@=}p{uZ(!2jv#&*Y~6~I^5X~Us;P772g@es66K_f4SqS6hl}+NvERx$iR!iOgQj%qTdq?s|#Bl4I`X+sRzC2>d4%cgRM<N3BTQg%k^wb&Xc1^1Vw-K=L1AC*Wvx@S_9e+y<IgJvWi3#>hkVkSUV1k3I!BsM71nRZ`!FPMQ6rC5ZF3VNG7Fmkz+^bD2W-#E72uY)PnFrt03WROL{RUfE)M8HYRFFhc+M=k?5WV({{!#fVLJwgS^_w8bDii`JEd9K6Li$Z+@vM+0&u?u-UH;?q<AJDqH$E-NMItF8g&Nsyo)n*cmky$)=u_>f^jH^)-huH8TiPs%fxjHM4F^fW4+>wpRA5Y^f;hhvDf2SQBp3H!=bCXWpStB_4fKZu-XNUBg<p@x9!*TO!JuM1f+Waf%6%Dytenvywnu=edVYXQtTJK;<pOLBb<4Ki^^(WeJC|%}tUT8FD6#SE2#TwV6O+O8gRc#JPzqO-FJZ6#e)W3}?hjy&|T6MdV^f{F7>U>US}!TNTVIBe9V)CS#C}iSt(-HV6Ung!vT!rl^5}#Xq*=NK3avhX}(uuRczG(23QE{d=VQVK4=IC(&xBE)T4g#+f>4$|h!ZL#H`yWgl_PWn!*4zi<ox<C~z?`x4X&?<O+v_UAk6GraxzCiwOy<@7efZ(><*Vp(ruS#M%lZ(><*Vp(ruS-<1Nvfl5%UyVSP1c=7ZLZs`OOxCjfsQlckb1#`L7PH2gKY$`2UF%Yhsn#@;WVvtadBR-FD6m88d3CICMICE!lRVLhI#zZIC98&K8w4kQMjeY<?O#eDYp%9*s_`YAsNuRaRu!XPekmVW=Pqem@vV)OTmn+CaiNP9p3}veUp!Gu)a<DDIJ<>O5vy^r3c{RT{MiVzf9B$q<B4!8#!>T1NV2GIm+2L|opAYH7Ft*fA*{hPzMhr9ntlBIuu};vV%?lcVBra>ug5Bsb3l%GR-}`rSLT{m&QCf*b7i3?RC;_>lroocDYE42pP{Lk-zTM<o_On2;wie5Pffr0(_fxZnz|%6G~J!A`_vOESfLvHS6=+J177v6U=e3;g$o}%x#sZX9WCE=$vv%zHHlV*%Q9BZUJv6dqvq25u%}KnlWcm`z1R@>IwwyaZg}p=zET!!eDURj{ItB4y+SUH#VhgBXrB+-LXvCLg1aJhHU7)e)v{9Z=ijsDO_%&wxqCN}tKHWsa+PW)_64;Y))13u4d<8;N!?6%vd|FMk|v#-j%DHXOx|h~x#`vb9*srdE!p^mGsxG9z>~I(3EOlZs$cTg%k*io&%bDxO0f4Ffj06ZIFOjb8&0V8KycfNb*|zR0=XxS4-UYi?e`rj=<K6jO$5u`hG>_SNyv1`4L5WJB1)9yqxl9UGP#4|nb`Azz-ic27^X8cy4Y8<p<rXa_YM9GpR@IzDjb20JdrX76<40n#|Ch_DN;DGwR{fV18_{`l@Mn5iXZYK!}NpFo){^cG7dn<8!UKFR#b4#qOB%U%^?hHCr2<*fCFH8Vj`Lp%OaEC679_55#_zJqb`9`fN-j8q^CH?|MHHK7n@5<y+e!j)urB00)p}lmwTtqSNob!u-ZFiYd+0Z`$$1j7ktask1}#5QDh5Vh!HNiG((Kc7yKZ`g}Usss25HaJcUC%I^U)RzcLUQWjefQ6^In5ny&Fg;cCX9;3zDM=5R?&c%g(LcF@2)+y%p#Lg%Wz3^H6@fP#b_O+fphOu#i*Sk<<BpmxFcG|_4(@Mto2WwNAiQR@JG8KSYJN=g~{J7~}do0Y61Lox^zJ;rEYFK7A4@1iY`upLzJ0H}i6TdJKYpYYouS{KEcWq`0f;{I}E%qD>+_6^QoN0mK%sc~xTtEAmdXh4e45iw|uaLKwz%FY6kA~MX92EE<|*6bZN8tLWf8isokhf!`hKLGi$0e!JAk2l{L!&_ihARl=b<(0qnb-}{0lV8Q)Tvl$nPAt^*r|6r0WEEn}5?p2DyUr>kV(B@hP?;=kdWuho{GKl(6FOr{^OZ@ct3uwDuw}uVc7ZFl@+b%qLllt&bEJQFi7l-YLl+=9&AW04EkL8+C{Bg{_YI`+2GV%L61@HSw(#FZ_-%yW&>GME8Q$UJZ-9+Az{VS3;|;L!2H1E5Y`g(BUJckd`#HmDSQbP-jS=hw&m0(w;YQ*ss0K1c(md^r+l?fWMn&#fTwl3Lsf?CfRonfn{;m@9^WcqW$N{TXpW-*H1g|pv{9ijKksE$2#OI3T*hpaJDoBHzc&D$Npg8;`AjkYLWRhklu{+9(V{~it`|_1cb-af0yL{!K@wKx@ugn1w{sbejG5&L=y!;&6p(DLN{kK-n?avA6k>+p+U(@e1fXD2n4C$epjkDW){s!yP8%Jq&Yr0b>GE3cNXP}oPpoCvyJd8$fe9_g8P#4Z_+>W14GC@$L*X<s|h<jmfx}rYf*(|CbF>r;SZg#xK@vf%{EUd_g!7#825hIdpXR0zW=ZYRH>%TQn#|RNo0bSMe`M*zqDD2-6u5cO85Khn<ryz$DU`cug+Tl#Reu+_;y;!IE;((JQpN5M(g%x?W=>O!MK6QX!9Pq>~JOj2#vy&_iBT@4e&`3DNPF#NX<d_jUaxy)}15W1BDS)AZ99)_JB;&i@PuLPaLq|A&0SMt|K!}qIcmm^edhZKBNO<=6r|=>1GNdZZE-d)VV}6d$8E2ga3b&c2K^OsABqB#I<$Q3$Y*9afB=IL;693FE%YVZ%+5e}k9ChQvrx$BcwGh=_*VJ4P53vBhUhv%PM>Wm7YydAW-cIUoedoLOgxH39paTn2XvgJVkyuRHQ1s1Ly?QVCdPh$7n0t`Kbo7?@L>ROxBcpE2I#Ywv6YBb49SG6^>c}OagQN6J#m*0A@^JKqV`w(0`mn%nb)y{3Sr85&k*;cpqE(CF&z00=H!Bp0QDhHxk<J-IPg}-z168=rRN+W?vZ0}E9k}m)?W=rTH+)u}$dtUGiXtXa!UvSninAxi<Kvc(2)x#SHn3zmduZhVf_+F2#p-_fihlXTLVaA3Vk4AtD34{|*s~%485~pgpb{>p=Ti!2PYGkaHm(-{KMwGZ8Y3h^i}dtZR?;~NcO8nzMisSps$E9tok9Sv%*kWE{2X>=%>UTe@*KvpEuhjYF_L;<5-m^lA>70!)F;q!_=&rko`BX2)Q7>CAkQl8=JHnFs+C-^5j?o$=;CVG(iuZJyrIvRoT=r2ehO<Kqm<6o(oZX7RrM=uku;(TQUn4T7%h_WB-5V$<ZNN|<D(!!WQKl-TOXcW4FBv`{1E0=tGhJnw{^&O^XZQ3?Ih@%Bq8R8#Yo#Quh0$8_WqFyZNtgkz#u#_s^f@;w4x*+;SfhDsVCqihB9j(-D(ujh0$<XgG9r!+5p0H__q7~FD0}5CD2cFVBG?Z<>34}#^F}HYto*;FKGx}A4DF^;`xF|^5RdKeyh$Z*q4vbK<or(`zr`8x(bgRKe7t<y_AF_1U^F;ZV1dKJ_FznC_k1-i}eja*<CnltZ_qdq{9(5=5r|@Jix}_tw+MOB>$5kk4WGcz4|tU9X5lthb1vFH}DL_{I|a@mN;ykS6JerY3jV3A}*66E-WeHdeN119EL;*=rf8qT*iz(g?ijV8xY$?HtHJR%#`p*7nducN)E;tHxjCt>mk0xRQ9+@4kJ}L4DqYPQ>yC`)p0=&FJC})RQ9;msN*70S8MUc(GF!%#|6^DeL40xp*OtfWWP}aa=-eb#b55=4j9Gw2#D6E%%%-#l*&BZazg?yI^~V-1m-bx*y?Dqi5)SMt%jTfoQIHme5$<(TLNP-Yl4ww!HD04dk@UyiYT!Dj+9vhV?kyUm??`hGwF(p&8w|Aa0!}7bmb;IHc_NLz*v?YWdmE2s;!akmry{$teM0vDS<s^MBLqxb(#<zbZG3E4l^mk2pnPgcaM7sKzrc=7Q_7OlP&n{UH2Ya{Jg+Dhp>Ca;xCq>m}T3L#0;5PahR?7G_HBuoJ7gToujxGtu6J&nY>l7KdC&MxKSnGt<G06l9IWu<nDA0n>HT__R?y(I33|tE#x7#b!B3l54IXxt;U=3zq$^~i$wU^QcSk|)>15J0DNn;@KW^<8q54_$~pg;*KLLm&X^J<g5hJ?g?D~pnu<5%uNJ25mXoZ}<fCU)e!C5ix>3-oD)(b4u~dJ-L&&fgu@4{d;KoyS^N7zXj?DK?EM-T+W=W|{@NqekOw)ux8<W|<ZEeLZ(eI6_uTpt~j)(M6WdkCYcyXov;EP7(1{gviYoP?U2JAaOLcb_CWiI+=7mFo<AVTMx9EF|Dlv{;|n#dxXc}x@XI#4hie{#<uX1Aj=N>E?d0mg`HpjL3RiW2Yb^%Xe~KnOLPw&ejGsEyhf%T#C}Bg_vru4#z|jn+WWIevuAe)$-Csv_a{0d!mC<6VzaC6Gh`*4hFr?aJ_Dm1T$zx7aZtJx$F!1S1r8zzQi7bihYkN2%c!cyFrEmXnlO{U@J<a9_f2@4&Nmg=CF!@;P|BJO?oHyK|MSXw1Gf#@<q>h3rprz_uUt^qL8+jYXY_)^>BWHYIaA#tQ)&7xHCWsfLjs%0Sv3UE)gCxj<;IF2S>FouLFBZJ5KeFJZF*S$9oSA=%q-r;Y?hAnUx~{cVpijmXMKg0rQSKs517{x^UN&)hsp(1VGX!qBj26WzxoyId3bI&^qwKMd*jl=)iL360>uAdFf^ejWU}1)*ElU{P<1_nIQ)!MQB;<jWNJ!8ip(K+0KAW=~gq_<dPyi3FWV@+9RE4<teS0;KR!xnbebzi62-^b5&Gz;SaJFmnj54&jRkAsr<6nMwYloTNmVZS4c`CFF|KcBN9Fsss#S5T2Ly@1?53GjkTK+TwGf2bX&e5z$n&DWO7{AV^j>j0k1!FumB$f#p%cdkh_-gcOuhkJ02C;gnO9B@%(pt<OtBa_jAY&I;_<xOkngkmdL9R+qIb`xVV)F%Wy^Sjwq(z!~G0oRlxB$p|pKVn$|0)hw{khoJT8YDEH#F`!3-nLt8>+goO@L5q7&U#uXOE4cWI>b2!I7_i3Q%_4#+HKKOreu2{&8m2Vh57_s>n%^eB3DC_7>^Ab85}pcSnO40_uX0mA3T{K<zAt1<Il%=x#*7W1KtI+xT9Px|Q*N1`QWdmpDPNFNw`>bvRJQXCX;RCbe&I}Du$x>~e&g5Sxc=p@KDs(jOsX|y$%|eNSSKInd6u)*m!?B+PUx-s1#`T39sMa2x4B$0rd>tIYZ`KB%juh8im~#j=4Nfo*7uN3h$@#dgYv_gVCv9$il`<I?!GR9SuAC?c#e%vr%}|DLu-`m-ojBkR7Wk*KBuxG)-{bLf%l_m15HTK@)KlMeirWTKRDd|*I&IyUvuWmE87|SK2@hnP%ZZTbt4wk=k{n6cU_)!QHD69*aiivdGeSh9Ia(L73Pjyup~X(FmIbQQy8hp)){#(lA}n3AY}{3EmTcEIFuPVMo)pv6^)A*MZBnV$twwM(X%}o+rC)4nR(5dS;N!-=RZfA7ofdFuthh1HW74>i*5Q(ytO90Vd~%T$ZvnXjquwDzm4!)*TNge<Xg+a?_^m0Tff3vzrtI;!tbnp1?rEywBf*A>T(!gbg%1yxYD~|QkJjmU9i20BpWYmVwiO>c%lNwCWhc7Qw%_dlMH$gD`A_0^5jS)NboBzC?}(zw=6u-uW;I|&<nS9`eW&C^$^qp!q(5A<qOWpiE;4!m3gZ{8pUcC$1G_kmml|wrUd5~*MHIsvEZ;IEu8A{A<a5G_MiZ9!OsWK-tr@)-A~y3<!y#;*2&?Q<1n@tRI#Qxi{!i=!OZ~pk=oIAk*QwE##2jk(J^p-!KYl9;hg(3cz=0_&IkYW&(k)ASaIb>EQD`{dexj8GR#RL=XifN0|j5;y$fd;|0R%r1f-vU?k{57U;0+QeAx4Jk~19oIY*%3_w(snr+>cw`o9dn<Hc@?tF(^(DYnAJi`@&@9Q{>(!8$9#DH7j5#o9Oro4=4uF)qjpFSlI0mY{KZcN~*+2GSpU0xk`y*?~(3SomDuS`3|cF`bU*$ym+*tT%r0uYTgPmhiFv4X^5J{xR5=@*S6RImrRV#O&>7;1l$1%BUnql3JxaP)Hl!2qX*OA({K?h75bCAfQr5s~kmkrE3{Cz~D_8Jl0=Cy6FdifFW50+>}JgF$mE>c}CGYR0=b}_awsCOVU@^9jU!0{)8w!sZ84jlZFBT47}|;KqT<3z_u=9c@AQ?!!F_}u}r@p2rPrnGqdP~C`4n+4T6P8(H$kOAc1vW#wW71UZ3UG6i1#-ma&3YVJswPTLF=Q^PK_U{UByuSmiza7TqTGLV0A+4nsmx`7+Y4#0deLwqcoVFDcj#R=-OgP5iEBiJO-sfZ2Fv+tct{><L7X2rjBDQeNi8$MKxN&cw&0fkO3uyz-+5bVuWm#^a-1N#yL|utjx#vdAoDvC~bG9~`MmtuP08eiQ@}AAwFNNx(wAQ_tyPd!t~!!N?W;s4s6W9sq}96C)6L{P*+!`|ASTb|x#HPbkxfW$1$6=4C-R#5^ZI?ZPTYVY`954Zhp3a?8RRQF*}2_Khgh_yD7gF}-7fBB{CURn7zAE_WI^RPN?5Tt$q@K2^J1h$oQ0E1VRhnZu%1oQV43m!OatN80v8Cd-Px%_H<SjwEWAakrP))L11nBnLUKiIA{<Ou6|m4<PJ}(F%xZ>`_u<D!(E}*Afe+ZqTZF=mZF7+YE7ljf4-w%^Elrz;^I)WZc%M?nW6ZcG=+HkD!1EORxnZ$FGE7G)yzr?icjP#1E<@NHG9Sk4yT3W$K2|ho+XJ8TFkMlb@<H`=>AyKK*;{xBO6s=f@--{J6S<2Y|Z=>=r3+*roA^Z+<+$BsD3mi{aiwsTV+HsPa0{ryfDE2itq}_s*yh30*)Hf1uP~ncg>WE$y=%?FEb)L9{DAt~P+!E|S0V6X^W;AsIJ&8T!32MFQ{BXqNvzFDKs<)J-MAR-IPzokH!H?8wK<nl`rrtfBIvI04IXZJqK!1`I?%w1yjH;o1?sj#=6#p9k=3dYr`Ts}uDXQ-@fw0TdE27%(*AOcvsK?F1bq?73(nIVVl>aKp}HtSVy?#76TkxZmKmUVeTVRLc2=*oh-LYz9FDR<U)0RpZZtwsJnkp(YG4px;7<VMuP+L@li?I3q!FoVla*<c}o)66BWv9Dpe^VD2VNh83Fx?v6AEk+74&+N{dI4+*v@5qSqf&A~Sfu^%)y<rnbTcD~sI2XLS|L%##A>d2yd`$(9|oh|#au-k?Xj0fZ+9(kT7Y8j(3<$xZP&LTf=G6{d>>oVGNq1ls8iQv~wMe%$k%@P={lYWUsvqX2HSwd`=oI0c2Ec?~27-xYEMMxR_rPheHPW>}1&vV9kQk*69n)VJW7NB<wawPSt;d;uFS^*{YqNa#)#`X24h>`6!8a8{@6hSHU_uCGU{)v~vzcZJ7EK3xS?>HQzvCfKEVv7k-2I*U6f7k*3x_6a7b_*c)gxr2Wo&>z5Tfm`6C5@IYNl&CBy`M_+@K{6g^njgeE8sVc>bCYR?dxWq$++F|#X(Q$0Tu-PQoIH==cPN&zCTpf;Yz_sc^=>5nmmG!Ip?&+@+_7BKV@CymTR&M!!3W|Jdvhtx@9cWLev5iLfznzK}Y#_$6c2GD9(Q%VwCZ6+|bAb>SQ<J!0Rfj2K>|s=+R;y(%MpenIs6gCD4-A63eea)9|4I!l@G+b;UGcIY|qY<Dft$V}RF~bD<}y94(?in?n~o2oTQxF>CWoChSf6Vi=)Bd(lL$y@q<s1Pih&Bs4on<pLQR0YndUS#aVG+P?UYt+Lo!(NNvahP>sFM-F)z>0=pn;OA)liX}yam;3|MmmG58I5Ffm=n#l?uzMzxdJaHp`C>8Nx10pgb!(1#FMuqc%n@V19j!#C`=;Ja#=p%9&!ku1EhBimNVu{7EB1|ucxvBBlpX)?L#3u5Yd8%NlG&6Lreh04?ivGwaaHRr(6vFkej?AV2@BKLj1Ak11MRiQ(LJA4Lo6~y*r{5~fo0~52C!IQY;lRGJOa{yrUaO+fpucH5bbl+H}Xn=C+56BLfyrG=%o=m(Boy100T@u`Ll3+z!LH+hQ1h$xKFdxG@nwj@%z5UV^Qqs%vhskiWp|X#m5*vN~0Pk0G%B_6S=(7!Y#HkDY~!~9kUbQ;Izn}XU6bEA2LG{Lghu_K1rM~X+MA*%xYN2@MB%H^pT^YyEOfqsZ^e|<QcP}HB?4SPM*W6n~pc)fsuzGj)DD(ka7{y81aUJ!|@yIN9t#*4pI%6E6)Mr@L&-v_idUF=SP;85KqN7YRo?#Q%@M|GJ?g!HAtR5IG!*BKl>n|yE?cVW8m3gYri0*u@lyGhK1j={DsBmV^qwh3~ddKv#*Hbmoh1^uK~XwvnO>V%Mdl$kmNePZbO<av3_06^2Ioemztc#rb*yX{cHJ@ea&2?kzZtN?RByCb#O?>EY&4;ikU8oN&r@Hc|;y3_W#lq-g+#obkBub*2niNX?+Qm0(t8nY6D}LdPjIL1JN1S((kRjv-06UH#;e@<iTX$NkZbmx~UGVm0|C_V~C*6DpG=P$qJwDjrN|%dc4xzPDt-b3JVq(UTl1@_zaW<_xK6~(!9bT_YvL-Jc90l*#{_YM7l6)W@He?hlMQ09s4(rZWKsMN{9a+=8YF0=#v+#NZelWz;|#<uc}BC6Rke##&3hqZf1#S%UVY9m*pgG2%4EV-NiA_u3a<-5pQ1c`<72q|Axmt)s2cWD=Q^7(HigNpJSVgRF}ziz)Eg8@)BUC-}6ZFF<nxciOzZ<tTGeJ{@B|EAO<o+Nvpb1n+h+UNfI;}q+M8(B%$F~H0lxwX1r*(A)+D=zbr=6r0|}ezg?T3_dt0NodhW9@d7v|orp!YRNrHCu;vcFCt81f%~v0+YDE{l0<c#Yw|*Qw{Qe&O_J0*2cNvDCy5U<~+uva_L_g?#EhC+VN0<52-}!CCoE^4oJ1hfKcH{xa<ksIb_*98xJ@dhAxx(CkWG4|eU?p8Pa8g7DP{z4iarUu~@mm~&<{@+$N-#<*2X=8HhNrLbxI=eU`MGuY4sn=m*jdyEw1#Ezp^yyYK+mB(v70>->qneZHUbKOS^OLg!_YGD@V4A4y6sl|Az`yC?|ODQmb<_!`v<jaaa!FVo3K;w)qnB^nSX=Kzky-j{(KwZw-J6D;Wx<q8)W_sGXDmde}l}wLFV5e^S|98^CRFL)%pAy)V#m+VyeG1AB^#T{H*Zu&bw2{d^~~76JPK5!H~|pE>y%-npiO@iF_&(UOo}bS@H6f&3*=;eouJ$!x>)wNpk;lr2NI7a+`ikkj^phOQC}4vMU08<nCJh2>;RxJ2e}k8zC5@%0cc56n&1Y9}(#F7VJ91@(L$V|Fd}cd<wLmP>9*U^7<t$uz#mi`?FV!XJ2=E{;#`8vLBWV`+lxBP#N~maP;Bqn8okjmig@K$m^6)<N!#BDN}1Mxrnbnqtu_{qfcSxmpJrKAmJl{`y6in@_*kATpymp*PjxU`w4V^jX{0_s$aj<C&2RID+1up+7zAw+P@T9eg?Nc2aKOU#pkH`bD;e>Lj2^j<DVDt>{m4j&R(B)Ke$T=T!zM1koyzg_%yiwDP(=91oX2d!wS?XaNeIo>64qI>}Qzzv50#9V*OcE2o9cAEtChYm9$iMU-I@K=RO#S^Q5+wZ)#!785cL0Cr3hb8J?)h3snP>ub6btvb{u=@f9kR#94(avU(M^5Hu#au|P$9=JVQ?3fsXpbMI??l-Px0t@_F)h2mtI_sF@5#jFEXDLny!qf4L#L7HWNJy>`aGR?PS3W`(Z%L^rgVv?ceLt|iktHi4SLR1(rW30#ARKw#5UGudp<tgc|QZ%^W2~q1R(U5i|lyl^qgb6Kf_Yx$<jA2;Y_nO4av@3dhWWJ7uS1})09&)sSA<m6*Gg>8$D)cN4dX~~i@D|phDr%fcZ(-I^;ek<tyF}IVsi0PlJqlloLR84Lq0t^<7$I;*N!yWdyux1IQ&}zk?XOFKe2&dL6CiJrCra$a8ssbDK$jZiyPn{;x`R&?)>k#i0SM~cOoN=PYF)UlL7rG{y(U1;K8#6&TrhK`9cOq<0d0L%r7suTS72sb05hu$xlSeiPGi&xqHRR^H&)TDxd1uK?^@MKMCR|LLB5(7fxk%_<o+){Ny>HwwXg>^`@-BDd~B|x7KmlqHYQHe`vvviDNJE!S_>mPTb`S5%3gG7B2n#lhAv}cU{8f{w6&}{w=DC@1UG<303Un-e86V{M7NL!O{G;$qE!vrr^{++Ik$rFzJthB2{M42%f5?fmel&Hqvc(*7sQaZRoH@-@d-e@zy-#(oNt;<D>BE|elc9|lSF^OrGCiS^zXh1I`lnKeERfRdDM?l+~FiXkKwKoDBEboyu<DQ=n#-WrdtuF@D~e}U?Su~c2)c$9W9mBnRK0mGdR)iao9@uAn~s9Bl%vC*s#Z`;_6_??Jez*RMN_MnmbM|k{sizZi#gyqxoGK@;kPaIfL#A_cRz5De4)<Euj4g*a#kTD-0YyxK_i_fqrEmE&46R5rW;aL7ez*AVYjgG2hy|J&3xkcZstnraxVlcaweo1!5P=p7JU28E9NF$mOB@WReKBu3yKrsRImvE}H$N76-z5Y!i&uI!d`%%LyRMafbzf=Eg^3&mPcA$;ChLgt!Zg$|EiOu#RC(SrRKI#Z|}W+!^_RL{9V-tK!Zati4Iy+(QynR*i53B_?D4Mw6$84oE`&f=vy<&59rIgp^aiiAx6^3~)AoNrr^X^j-2kG#xK^1%AYGg}Y!0IP{Zn^GQ3tMbv*&tVW{J1$qncaMG3`D|{m&IoY>YW_#CizPC6-w=#Tbd4^3Uhkm(;e{RtWQ%vrv_QD7-n~Jj_3_0djJ8OsO4qzA_v@w>$KXJR{c6(fM*D%FUrohH}VY07$*79_T2TUf@6AsA@1NvP0J=0gTFo_VG^^vBvym&9jFOg5c-IE-ZwyU88$VwJ_;CKvRe8;B%(8giij(B+B^!y6Fw=V4+Z8dR@Yo}ILAdjQd>dJrkE6}9TmbH;}e@>uj^r+Hhfu^<!G^J4?s4;=2a3avuI-SJ&S(vWLJQ-kEc_Cc`gPp}fjpi!M;}*}M3N)4LgvW!m#HY9FK^PBFCiWs`@N%>5wcN}W9!zS1Y`;T*!<b|1R*l&H%MznK*;D5xOkzN}iU9$$^*#45zK-Vqp5j)m$o|Xo#aN#*{g<CL?zyAf5&N*%{Z=(W^9|r&2cYZt=P}TkC5-a{uRn@Ky$s|YLn#p6po7aBw{EZoMdH41gxSR&{1IL0EJKCEc+PUnJ<jk${LZ(Icq{0w1Gf7>=l2uX372+Ge7{`5F>i^jSHour+u!>%_Pss9zISXB;rjOF_l6N4LHxPr0eGElwZ+z;7mQB1Ux>^Ks;<Pob)OTH$(BAK`~yg6v6e+>E(Cn64e4b_K2;#bIiJHg^96tB7Xi9wpmU_XTR(#7Y2-wqZ4NpBxovGwr6bl5MqiHX1p)WdPiA|HP|}9~Er&Jc==<vWgH)YcGX>$;TrE6$n4<MDTVLB$gAxnGOwYj6p&p-%2PX)1$Ot#g<6LVP^S)x=V{QH%Pm-svR@BKq*{2*Q(00uy1ofEMzcz`u?R8-~Yz((gUkS6!jbq!;c!n^2yT1YiXPIL8VxEn|>;n8eFjtf<2R0b?-Qe$G_OBl^7|U<8&g0s-JfZW0AG`1sWz|;}f>z_>h_l~a(54>72+f7XNvs3jvNLSI^PjlzyQ&Upc{q>%oqJ)I$~qN4Dt<ouDw_y!(GKZU@YxID?(7!<-pL-%@HW^owO|R6{D{sLEq`Fs6IR12*2On9UtsPh%}we*w5m>d>jxI2fm*$>!{zCO9js)?siwZzQ9{;$z-G-5O&!1#eN>*&F*Zlk-@}&Rl%}g<yGQCOOHp7qU6*v@>{h0@ZlKt8tZW5w)>Pt?oi?&fSH4+FwF{&EtFEch>WGvf&BrGxvZ!^xdhy2gua0R_0gU$*Q|%ng)A1^LeEyqd`x|~t$LWEy<Bn|Oj?uA$H$9BIVGnkZe9P{oG8#~!LCa$tjWwKP^)K_^8)Gf+G#w(NZ0`DShi|d(Xj%nF!5Ml)c?fOe4pjrS<(VTu@G|J67SS3|Hdd`7(WE=LDiTCq7^ajb-v@%P)g;6kPfLHkTuk5;&>Bmbr8i|Ixv<zYrlvNou?BwK+_IYmiDs15Rncg9x3iuV(FFL>l-FNYOp#}v0h5Ok9IZZL*`S8mom@L?LzQI+O#GC%0l)v{ud8pmMcU&uHwP~teR#$7&L`>z^hXwC7bP%kroQPgN*|Dg&7=?+>U5N*%6^%lt66Jo$}<53W$4=4H?5v%dMLQIQvn3#%O(v3iH6giz&?K_gV4fjvu*uM24QNNZfkBXOu4y91|d^Qw4Cmss%bzzE~&M7ExjuGUw157hYK1A^K{$#db(}@VG|@jcv}AE+ur^E?7c~>ZQXhuv}Up9D)!pt*{68_{ontde?Q~rDuAU}2o9o03p%t=kSH5T5JE_HkWqrML%>F&wk<m(AQ1%{Awma{28{$^DW*v;X(d1uph=`4y38@gH&?NXQ`~$1d!Oxdb#%1vK5MVN)?9Ob^DD+T#&^KeKgr+xp>I<D<~vWy-+b>0`5SRA6z!YHP;H?0O<pBk(Y}e&zM(?RD1U?fpWB}laJn-E9CxmOQ{&`w5uA1@g41KZXlHz-4o*B(z-fvCPEGSK1)SOxaH@^++eHMYEt~;!5u8{=a1upuw)LcdlQ)*fQw5w#j1s9R;B+$u94Jmeh-Q+%X)ep(JgI#{E06qB9e*0%4V9%+)f?Qx3x#i<RlR}#@`Ivx^KVqY>FOUx1e#jz+WDD3p!Fx*R(&?{57hM9kZFQ`3Oe**fa$)WdmMqG&8%BF3fBFD7Q0q4A$Ga}iH?Zqm53CQ5THLX`-9jp!q}k)bBW2$w#59Y@8_*0lI<j@eHm`cs(d`%6i<-bw6bDf1)Q_N0)fKE7gX}=ON#3|4E$hcRyg2}Z*G_v%V%6w{@cNL1K3%oL?<_ue35H%4sh4;Bf~(XH_}u!*Ky6_hu@FknX@9y|ME>0y---VTJ&loH`bRIy|^i+%XKdfLwlj_)x4zcl}MyR5}d20FE$1@*Q;MmseZYaRlm|n^(*G>mCQsRrTRrCj<EpdPYPg_@CPt?&(^@MY|2&uldNdFQ?lL4&Alqf`M<wnGi&Socb?D=n$4ysYE(>Xn|9DF+vl4Sf@RZ`NO&;Ss7yPkRHs-6Lf+0PDC=AiKy9U!PKm#u>QrDuV%0NWVy(1rpqLSCtB%|KnDdi#kBUzMR>sB@gj$$=q)hM?L3|H-!tlkg(^Y=eGF=zI(BQ;I<fa71TKEF;X!s8M>?+%gjp+qJ`Fgd`^gA944;>q7#WB;~;3?hEfQNq%2KHz0)Yr*UB!sYVTc}-JF~%A42*KDUMg(q6k}|~BRd-L!Az7i&NJ=>+10rsbm5+77E_$Z-^A;B?(ccXs%|*Tpuk&={Otao_1mZn+w1kq6w^9&Kl|PbwYtV%h>+1Dae-~jGy^u4$0F&&mEFB$;7R`e;3^Vx4{2Zz7SXaWYV3>D16K+Z(#7fv@9KGsVhCNhl_XW+Dm9Pj7)VFgz`aR@*K{mD}s87spbuYojl3n12-0is=tNJ}cJ%7QLO@3ZK@nOpblEgE~t@*NX&KOi28DcIh8@jVvIlI$k6U(yk#^YP+x+;F=Q*LQ;r)5Lt7T#Yo%v9c)DrR!LtQ<(E1}2rWRV2S3DNwj<WMoL$v|-scYD{sFTP}cjgXPiQ`3)^n!^#s#nOBoMZr+WLr1;uL>>wz%+~$W*&*tBH_1NdxzrHl~y?Cph9eZsKCvs;P(|$SjZZ`IgJZPlOvJD?r3u8~umeOaX#ova%8^cEq|K|Ge`)T-jZQbec-=M^%^1?G?pCoA37>C|C{E5TAJs<wRT>a{l%&YIKCX{5}7qd)W-VT2l(MkFdEF%!##OgNN(QIf}s@D;ZR_6ipX%&>~60c2Q&TPOo8%xSfJ|1^6X{>rxul=_M5V|0#7G+<#Z8Oi;2JF!HSlCs5q&b!$^$TH7K~vJQ!}y4?D)1e!_e7GN!0?0dE+4=5wLZ?spZvGFHpF9*1E3d?PT&guCo9vWNcD%nl`v&v^8fLvSQ!|&5S!$S*%~j`nCNG&ZOyM>1tcotWYlTpgvziNO}kj&Zc5b3&WnkXAY}FHi>84U-2%B6IK;6eR#%o#h$_rQRAePsiYL%i_pGnua`u+;#@_Y29~1mC3J0HnUlQF^=J^QETH;@>`Kagk7iLAULL4boNBoOWS=ohq68{nl{v`_kLZ{RqFiZSPfK(>tFC^d72?R#$Mfie-%SEn#g4i_TkJeByOhz&RH^ahAK$vz;ufa!_8lwu+3agtUVn~0o372{B+Dk5F`s|phzw`Sz47vpWb72%%{g6lq>l3hzR3NmcI6!ZnO*{#MG|^@_!1iezpsE`$34;pQ!+i`8;I*veXIEx*KVSWp8-5D6o8FO~@u6D%B(|zSd+CGf>}n1ocIwX7s(R3ri-N<;>c&x!j~?lQx)H=Gvd;*|;3EgeZ4{Z1VEsPEgPQ+(xV5Tk(tkNG?%)PjtYye@VawZbyhCfpce+BRzwRhfo_*<L4NVp-z~htWTy6&sZOcVNuS8Y6L0v6(<2fr6WYv*Kn24I!yIb*A(F4l&xaUV|Tb%<hTkx#<y&Upv4)#yzEq`MUIYU<S$!j54;E<<}>yRfpLGH{UPYPmBox++<;nAEzdgFwuJnfK^hb+Xu@>%F|>za`4*U;s9(&e6rUNgX?9|5TAdD*Abd_YolvFuZvc3`tv0vc;RA}=SZNM#>ZJfV0Ut#$|yl)A6X$t&<3a+wqR=jM5-1zm14x5jfWbEH$MX5&=z_vC;TQ7#|5!&nl)>6VPSu;7fS^PL=Iby;ro>sPr6XXT(?Sj$SyB63wog&o{48jkY&%po_W_^XxaQTBZRS7p`R6{u*Qf9%x(eLVP`VHrYI*w4X1M*1*TV<V?>_JK$_D%EEiLvMW@=#$}~=JCmc{Q#$mv)`f3CQ#PitJe+)Fs*sBimniZqif>9mf0P{KJs9bbFriSWF<H8NLcAx#WGQdgD)f@rG#(`IAUN%|Axi_&gl+^4du*)zM;H;l`)8fRIyC3P<&OjY6T^+o)-i54u2i6m!SR-R$xrVK>lZ1y(8l*%8!NdH4p!WPoVW++qLjc=*ax64g^JN_8drL##CAZscXRDTIS#YZzH<6RXQqFf^~~uEUkd}9q!Es)>RK3Oic`S%s}_6Mj&S#VV=h~&h{K}!1gUpE2cg%yJnk-7ef^l>Jjv%M5Ma&w){BaR8Q($7L$mQGbaq(>ubW`y+wXC+3NaAfG#|%LyODqxjtJ~r(om<lb5N9K+o6To61+E^`8%3@gtqe$}nCSXm$B@##<|QfFm3Yp#ne513F3+qC;6@#jGXif&KsfDXei<Ht%z5973^IOKXg!h_x3=H-dAe6z>d~erl7sdV@EGgr!-gzn!W&omS)96SJHxp(G}Zd%qZG?xmq%lssV^wTE%GIy`3zSE{K@G^1s9>ejkkke`<e{G7s^RVW6Vc&3cgNqi_*Nj{CLWuEpq$sacRY$6gsKFaASjxmkU@XB(%9OJNXjD;Y=^Zmvh<6nB81i=HP1RM}nSS>x4M9n%t_H}9kcw9$heZGUpp=GNZD3uevH|9fuUj=Xk-dDDQ*`3bTp=L3eyRMkC5j+Wa^}uuh3&Pgv7d8g6Y{}XyQ=b?JdcvKg^s(lj2qL4$#=jygYsg&B=!(5N_-j3QVY1K~5rqB0768el6)cEHxE}J(*usGOj^CIqb^eOm$mO-GR<R<S#UZcF>XBMqZrHrn=Fc+mwHK!JmwqoLv8$3ut-rA(_Eh^Zn~X(!TsX`-X3<7$WaNy?K`e?rgTEc|Gc7jZMZM?5dA>oJ2e<au?I8@#fBoD_5W)RDwR(n2&tWAV1rs+RG@J*hPpozu?c46MeLig!Ta%jGQf1g@dKT#ytzuI#j<v6dJ--$1o}{qGSzEGYt!2xq#xGmNV1ksx6VNGt21B0D-;$lZi3GH<5eLwYR5E0kzoknxsm&KZD)SJE>BP;^Gdn55S~n`GF|>r(3K5<%?AX;up&>E5d&`;P8*37r(s)K}8UEN<f}-{Y_)JV&=bL?Zt*@+SN-tQ?bfK-~YOgV#D2IGXw%T9$XtrQesnPr?TTqLO|4CbbqBLDSrXBKxdeS0@hyE#}&|WeM(w72<$XFI`pE3%~tg_X{=j_5*2OhK+xMp-}p0*ALjM7#)qQCayt?~sA=UOg()<}9Gm;Q7wDb6gq7iQGSw6HyGC*|{@nP{HtC^Z`qpJ^v;>x;dlmPkk1G?eV*MvbI}u$ndQMpPe{Qs`++p;tOMFKo7sNOOa(xL+pHUzL~q?9IvXKdF8L(Z=xO+#tTh{R4RjSU^1FTV2Qc2nZiI=x;}+Bu=zjHhubddn|nW@>(folD)2-nDpU_^Z6^u(5sUJk5N_8JcYg#@`ZT-ABiMT{6uY#90D3!7F$9MED`dynI{Df=z4s%Ep5QP+GX++U5S3k0`+0+@{Inwl+hTNXY`D&H}vq<d4+bmM~QP`M)c8;-<0408cgTks7=75_e<cjR-nNa@?i($4S0ouc6hwGh7_hB#K@D)$>1$^%tzu}IA%wMGNYqnsD&YomSct0`<vCD#Y1ZgH&*&5uqCZwRGlxaO%V4GJ9vKa9q0D>@nWzM51}?m5lod15jmAsgR#?z$>))cA}Ri4(4L5mSJ)g#5&;6PAPdWzvq}OsWP&|0H`s-s;y3+UhGH9XHiZd`Du4$vWJX3#uxD+ZFpzyvlTWQ9y%&x(s3VI;h>r`_Csu~;@y?>Gk=xC>5~AU+rSVs*DaK>3PK4@-+NCpz4{X@^cDjRj?J-0{W%w|~o!P2ynX%bG9gbo;WY9|1wN>EW`Dr816gz-Q;SJ|Wu?FtOuQ~n+_D(`0a)X?-O+z%AHMP346T!p+lUi<Cb(?ZaCH&Sn{Wp~YQ(u%%F@`*UCk%g3P{bgD7JuwVYPhabTJ{K)&JG0^?I=<6KYwDj1J>j|i11+ho`eTh?QNfCJBUn+UEH4Ne6rW@w8#sp0~VASgZe@mbA4|@jJx1D(8jc$Z%lkj+MCud01a+GZ^7($-njlh71zIiKMK^h|Gr5kypf^5jquxl-$wZJ6Z)6L+8d|;8>j#8G3UX((fYs9`oGco|G}j7e+`xY$NT*pkN*=S{+H?dgFE5wA6aeA==*PsT|!dABFC*O!Rml#6;+R8o+g;)uM0|0Hl@HPeyIhOe^poS$>u+!<3AzOAKB+8di|Ow+%W4GmTd3F*Ef5op7X!EbC&<=<oMYMnbbS|xWKa0i!*Zng%m-Y=<@wg24@_xjk1AlWm=)rU*`i$ilge}&C^RYj8Zk1AFv;h6N}$}sIFXXA;F(taC`cto>-u0L_p<IXV*OH7L0dvdfAJ^X3YL!$?QK8KcA5M`>T)JfYk0}3RTg~{_CoduYY!t!RV37AUL)`I!%B=Sapr-zq-Wrf0;`DNveG@Fg!u`f0d*E8teU)|4uL5g%?lB0L&=ztHR{&{G<WE<$r~eKAc@%sGeo*zjna;+`=`j1vhCeoC+1ZTpr-;iC3|@c0e^7!};&IXv8R5;LAlyGoVV#W5V>QD$FSLPfq0*Ulh(>JfnQD{A*EqV8`z@JpljwpDxapt83@_X)C`Nz;PVpd!G(YxG*@^hRZEw#GigK{Z^0PBAfo_t6zm(>Yb~9qOhh(h*;>}CLTpn3v>h87`p~ch-t^}a$z}lj=*Me9C%^vq2ilZTB^xz8G8b4dIR`2raz5cz0*@$(WG(PA1V*lQ-@A0)XS{Z+8Eu?aMf1Q1dc4^^{!fV?1J<_&8DEL6TYbT#%rH|m&IO$a%7>a>iE9c1Mzh&>vROvgK~nL8>vAl4V;NAu7oYY9#l(~*fwy3qMuO(Sv+k50T>sW7l~Q~&KURG);M`jpCyW~PDiqi7Ly>QM4PjMrpDDsU^JR~lC^ER4hO5-R5TE3;dZ~gz{~HdwBaM&8t*Xi@?-@Vz>!vq4~d&9YQGKH*zRU{`H@PCyeuqD2{n%~Yzc}VgqQd10JXM$Z~*1;BYGLd{d(^c8<O(5(ODCNk>IK_MUZ>CH<IEu0;rhpYS@BOG+%q0g0I2J=~$lrwl%E;s$T~q-D}xaR(thDxlxN=9Cquf@IV5Z*|gQrq9!cwFjb-z_hp+8X~#-DH(t|f_XLO5psPS9n@0z=BQ&9-o0N{#5bgRm;0dk7MT$xDJMRg){<dp>l3;mz4g|Kc`k&Y;8kPvE<cbo3CzXs_Q0I0m=GG_mPhn3xLc3@9>L9wrfk5jMJpw>W3oL!WR3L|vpnw>^mT0FWQf*Y@$GWKD`s6AP0$1(eV>AZF;?o8hu`?D`Cx{hM)2xnWTXTzX5MT!np%Ig^^LHLx;N&nPHj3!`fe5e_NwLx`E7`>LOiX4ytC`u9kP0cE`Oz=ypP>SMbInGM6Ak%KkIng8RlZiuru^u3bk{!$iht4GCTeElO<Hnnmsz&UvqnHsdAR8%SbpI?s;&b$PFr8b^7DxiUA>%cJ0sU)Wxr(~LqYVXg6QvM#?fGkX48gtv7M9asSMBd40W^1To|5|J~}KRp?!pT+fH#Aye~GrFjDD-nk2sy-H)^Wc`vNECMMqpXn+ud((Rg!x%F4o#2??bG^gPL*WSBp75Y2}2Q>A3{^|KAKLSJeI1~4rhO1MQs0cM}>X~(;r6pC6NH^qzj22Bq)U6O5EseRC<*G_&<v5{4x>1cp8<_IJ2;+=0rw1S?Ho`dt@zb<~=f*BOJO1cwXG|MImIUY&6qSU0*pA^YBV(DQ>`7@VO%I#`Oe=P>3Kn=oOZI{r{E&zDhpJzD5jXgrRBVCl96u_PDI$8n#(>4G(eg@9LnG*F63*AK;BY@0lB9vXuf=_~WE@NczOef!Kc10)mm30MLhyfD05{=Bu~Bo-_vTL}G40_~jnk$9h!psU^hJ4rfO^{x?AOrs(7}^4iRCk(sh!jllo()tSKbps<Ml;sVU3OmaeR>H1WS1$`(k9TTm+nypK|u8$eXIsC=d9TB$4s~LoJ{W{?rjt1@=+sIaX@cMFSWB=|uC=Yt2qf)8ymxjDalHz{Ze<C_D56{$o!Ol{XV<3K4vSr_Jfg2jeOy9brs;7=Xg0Bx6xGn>dl#S==$3hDAjC8u@&Nwi=1Vjgvfq1L^yX^>$j)ht}+%a{^6d4rwxhNaG=2$;#FfZG{&f@yJ82BaLp>(4Qm@mPxLR(>n^wWTg7RrWH>nvg2r!*CHlx1Wyn8BIou}exSm{NeVK$F$>A=FVP}+QF~hhpxAYBfpNiVev-tr_=@hPFGOa(aMg^TT_!{6pt_NkTrU{8h4H^7<z#;wKPF;xyX&x|J)g6bd&`G<%QTIQFV?~4Mgo{6bGwPYO_vl;FDaR38OJ%6xKvNG3U|{T**hi6=89gZfp<r$b0=XR-FuuwUoS<r;s+WT$e9(J2&~<l0^KH0d00h$(~X}cK34=e_H_&Ld3`Y3V{tYW!g;im6|#&!{9ji^sc$s{Hj<$quWK>3=Iy)&!ZwZY#&d!J!5bq-Y-J4+^|&SW_|BH#<mAM&Be#HNI<QxSdrR7Q5sLQgKWIAwHzm^QY)dq^KU5n!K4KlI+12L9u68vK@{01+=3r56I}P2bNEBioyHKOcE>^ZxdMM0Pbt}jrPiS1y)ZEQpP8gdpnPTMzkT0)Abik$AiN%RB60OLx{DGmBaf<Lp9BDU=%8g%SIS86vFY-93*J5A-L)zxx?}4VoX4*KTZ5I-=h!xP>=j+)cj>sRn^{|4#v=7>xF_CZSQMteL9;jB&PH;6UCeC}bDzR6Qq7qZPVuU6Z=(9}H7e1WVXv(Nz3FEmVs>>(eqVXt)$({{MUi!{(hBhQG_10C-jwOx|0ri;w12#u^;K6htT6Rgo<}%NMAesH+^rmf9v?PFumCXV%UFoe}UKEet6j=qskgMeepk=R)=tj|3F(PCos^nA+lpc1nAmk)4+tr9j81sNF-wX>P-meXmPS2nD{0%+c>><<$4B57sKe-1>p;|tIVD*An=W$p`?$OtrXK}|jv+rfnENGMLK~ZB30dPA0S2F=OA14$`%ZBP_;{5coZoLxcrz_zX9plqJYDr}w@zPk-HIMU~s<>>`EYu%a%}=9!vpDFitgZbIlv8Y-TaU4qaa%kSex*hDMJDq-8EBNQ;l6b%Rtr&@BRB#!J{EsF-CCG6OktK<=BFl|qdQFmq+T%==E9?wTmCtK(EsDY^n4R7{QZoq=cI*S!PfbtYiVxUC69gxM%?@|LY0QP7<GHCZGT3h-?A_Mj6~m!Y$`>Hq-HNPC$d~0Ruv16zUMPnW6={l`t!DZb-_=a`<zp5KT+wQvZ;vCCmXEJOAgmcz}w)sp)|BF4TX7u%CFy-$CsQPUUd+V&LL*Qg81Lwf4(HJV_u#wy@Pn&2`?J<_ba*!nk;w@WxlkguW+h~N~Z&p1)ccSA}Qp8`aqH7YY;-7Q}3K<qGCF<C%ikFCd>{ZEmI3DAkrPNLd#8_bD@b}r~DSd12f9e2q7+*swEd133%d?6*^k--b>`&OQZFS71}Q~QT>t*EiLKL-gh2-w$_gS&t~X`sF0VmvW}iKxxrF>VGm808d~XstEg`YrA=LQfTG*jJaVF5WjcXp2=k5AC|k9+!lG?VJk9uLs*yc1+r*`SD$7&oD)NSt;6BU7qCA~zW<)Fur<28)rR99zil{u`u=Ut#L~ZM)Xj`wxeKx_#(qyC}BfDbNqA#a{H4~|7T0=g~Mx<LjZnA=v@RD3y!E5Uk8$uq(<S(srR<x5&9nU3T46{gTY@3g+odjBEq?C|IwCX}$BMnPr`6BO-i&*CC8H8?@E%fzrvsRQx#u;49$|-QO6lwe{GyU&<(rMn5mN>dan`;x?+w2}RyYs#Q%5)q#kb)6&d^?)vae{MpFXwoBGRLFM?tw-h={ZesUuHLbsG-d6_TuaY^k*@_<Jkm{CllPc-3w;-z(&1Ja)Z@0yG1UwXbN{~9Ie)c7lQPcFQ3;K1ZYC`)1=<<$_H{jYif%Q3?{e`ubxcsIG^Av+{lJeN;9iWiQ2VoV4B2}zIP`1@r}>!Uwly_IuGDol_WoW1TPo}V(zK~rOUgW)sJO#kSq-Wd1eqt_-)b4^jyhl?>D4|(rtCDJ^E_&PeZ=<9{tv+VKa8a>usKKAv9}v3GX6Im5SCmbZ++k$P?Z&Ajv1(m~<@|p5HNMTw8U_P-giW9->ppAxc3oU)$P0Fm<t8UhR(E<lkX&z2Q4{J5(ulb|q++*TLDMAvImOZ&i?CUTxI%OSnO_49(&R{MK`h-isAl$6#Qrzfb}QYWMZht;4k!_VaB}0R?OvaIr)IL0x8f|FtU0tip&9hE2z*h47E_b3bn8#Cgc)po&awfFjtylyYS1riKq_{+E2WG&*jU5*j<agObvOIAlxLi{-Xj`e=UUqbV1qggWVrj2fo+Xq_l)2R|s4JtyRngH{)=?&P;}&>*ltX0F;w0jzkKXg$i|Hz8Vp33d?R3RLuQykMY6n1sp~^)oLKw_5#Rh+F;Glj2rsCT@lNVmMW{dX%zNqm2wHr)z3f>0HgKSx8xRMas%i%1V>yv1EDYI#ye!YT;!mt3lz)Qq3wBHLHH6X4MomtGxv1ys23^lT2TzS#?FtYT&k&Uw=6hw5m<e3TIBXXmI8O^l70bG!$8@$GNN(50kQ08|?PCWU9Z-wnHv(bEa}tS=r3900wxHhz5g6U&Ra3S6t;n*5G;iy8tEHyolSm1{VDU$zZkbA%n%Jd7*^G8YIQA45IvlqKEZ=zkdM!1Tpz}!e&NHZYjbad}4AMwUL|Lle^)XN)tsALVOu9c|0Q~mk45fi9}OX5MV5aG}nciRNz9`b48`;_clrSpP37K#QW^IUJ~^9zKcI3K)$J!!UT_&J)68(9X7<sw|>_ma!$cYXeeKcOj9r)C($-md0KxT@mcV146wX0*q4iXNqM^48*Z;LdrXB)s<6fOl}>J|r=f`52yGTQx!xUp>Me64G5H1yAa;I&GDkJe89{zki$Yjd%&`E*h%4J5eUS)qoR_^bEmb9o@+drh*Y8O-1e01rl<8aG0IJqITFjOJNK%4)6@l8w{*w5H+h4B!Scn_^KpN%V4eB-c0?dyv5qX~8vL+D#8{wu+6mLG}App|r3ytSHnn5Vf^RU+Am}B)rBaaB<G70bwN0*H19dCLBbOe4n2AD_F;Yy_|q!X=teuRakJ^yt_n5Vy`n@%GvV=?f^cuUAHyMfe4BUC&}ZwKC*IG{w7!)}Py&SvND7!9H9bPG|ZWQ?ggEvWOm(Y4f|@v^&7`d3naP5{`ko5trr<se1*iWlh$Vbl%D=yfCi?KOE~MwYPf`R#RfwNA8&cZ4_2wTZJ=y9Spru5?eK;kh<3k&g(4@?g`3_my$h0K>EOj9GjtD1@XjruW>DfM)HAisFV}(GtwTXAUe;&1qeulost7n$S!(p`G-HS19b_OSv=WHF+qVj(Gs{#}CGw1S8z_o+<Atbz~7^w@Wn5V%2SNkC7d7(!LQYPx4xG$i<ctDUoc|67dX^^iP3y8=8cMNa8ePh_YTZUvL=S>`RkK5*3L(Aekjm+_*YV-e<{ZhoYLUmbFHaMh$Z<VQ^L=s_;jk=ODoDw_V(j;4lx&KY$@=9`e+{Y{PW#82&Ui@Ea&IV26Lme_CO;-&Tf-`7Y?d$wXZ_dAD~}Jlt_+Is2Ut`(A!=hZKoQ5nty2?!3fbn*w0|p*tebd6Hv58ZCcOzK5@maxpF0aXb{6b5?G5_xK3XkGCS1uA;%AeSfT&++l%tMLBEoa`UR_nEst_#Oe9{t;TZZ@tmr$JfTZze$VLi5YO<0Aj|tnQ})VwEj3vh^-@SCdZ8fXjFkOF3PPV*Ci<_v0?{$D?Ov0QYr%s)C1nMo21FyruY5RM|5GV-mPWC8nk<=uc?vRkWwB)CrnIXGQ(>xFO2w$kmTbG^DU<Xi1?wq2hsQ>6ho2Mf4kFwu=xDYyU^lVC(<x^enKS|Camd#$<*C}jTt*(yNT`vMLSwWkC+V@3KtKeL)SfjyBI*(<&!8={0x9{MSG?bMFY}*2^PKuw+Z6J3y#q=4!0iBR<rT0wAiJe-%~t9?`Q056_uLwGY;qay4SW2cW47?~qPe)-BlbZ8fils_+?VV)LE;!O$|@dgrw9>FTu7zG`l~#tx1NA9bx>iMe;avx40ePz6c9Z?sx~A-tfBDZu{Q-a7LDqyrp6;YMr7J9A54~97G1ZL{WeFYC>q_Wv}6Lyd1eh;X^l`>G@s{Yk`ImLMK7=P&K2n0)wNnW${j^ReQhaE>{r6To~_%oUsO^Y5Of82PRzA;hI|~<dBuc=oS|@)YtSZKw<Vq}80jQ&RCKMEMMAaM`#HRnZ*~Fn^eq>8nBh+as|*IK#0I22s}aUF6u2eu#Drc6^5+aZt0t$$Td&2aN8=>*6YaFMzDOr$+KNdz%v?7$hlX}UU%IISQJN?eBM?!hS36IkITVgw!Y9*>k3EbW4ZRp^F4Y33$)sBpGJt`dH@uli==zbN(wEcH{cLnGHFbiBHFU<dNr=;c@>8R9KrDB(!~xhj^`f>2<>s_3X(by8R?0k$Iyh_Drj_w#?mnS;3cvFyv=~Qf&PL_OkIc*Im%N;6CTqQrg%_wflUvO6cFE4!aB7bPoi#f^S%txzjjRp&(gEbjM4yLdH4$_Qoy;0dAephDHkE5+il0Uh_71se<LHbcutgJ)IZ&Qh%G*-yc4bb*%ln<Nb9SF=r~9|_R2m|iPxJ29qTR7gB}e3oHc*2dAsw-=-QBB<7FTy<h>pzp5MO!EhR_5hTZy0{xa^2&U$f~TP_5<1yzu016&cJE;F+h29OWO*d#NZ=H|AvZ;wC1xHxK6zuh~WCKpXv)%DSA$aABxk=8EK5j?q?1YTv*@eaGx0qQn(7_{{KOaxqMe)lc43RBClCyHK&hpo2k_YhA3yMmhwTFgUnHn&HP8zlxB4%N)N&#tvE%of2dDy{`I0vOA4<H00SclKI6aSM@0+e7I*JHfkl8RUM|?aOfqww7|=dtbc|gn6!_J@NvG(jbj_}NYGzaZ)?~9DInSEZH-KuLAc*YRcD3%Q@{XHHEKb(s{1!cNo1d*Ws)q29v;;YtK)6xf@oLhn8S>^HfGnHbQXyw^rrh2&?(eb-2j`vlN;r|M6&>NuiR<}BK~A93<;^n(p+tg4#=eZb@!WY<zD&o2(xqXM`@ErKXJC4lzw%~Hlh5}oxQ`u@S{Hsc1}ykT>O`x^*>s%3V-@@7=PX^2!87FlcpatU+D$EyNkb9(={BP{7H+H(R2-6`RPkiE4|=%cj34DvHW5X7rKA?cRl;v%zn4?-!(<+uvtLjCGvL-)lU3=U^03@WsASd^{*`Z^FA-SD=&ueMLSLyn1?OXOk2yy;zdW2s`D3N`68AVb$OxhYMiONbtUcE%5y6q8b!FucC;+6f8ZmdE^0ismNgk2x02HKarV3B?{4;6r`nX?;fde9B^XDo@R!UJ8@Kb{ozA9qHA>Bu0*PD^YcS+>HoVS;tnbhL&O414Z$@E}x8D<GUC9!kylAh#P$bkn`2zKhmDPmARQ|*dVHVOBzx=z_?@K>^{Q2)eh;hSR{#)#Ab(jy3(z|ukfj3ji=r|4oCVM^PpQ<fd$e}m<T<i^8<sPi5r4FTOWhc2^Zbe%I@|bEJD<wVqB?T$)D@Fa#lWfZw2C6$EaY>cmHk8enC{-^}cRJci3m~j6E{Nq2D8lfrvdt;5SeCe(2IyP*zfXyr$dzq=fcp4hVMOTgHA@<lnq-lqwlr1#(~r&WHzkz+0i=lb!2`+${9sqAEUYBt9rvLyZy*=lNTZUWcd!giuWJV8f(}7z@Yl}UUx5Mdgf7p!zFm*k`-%hCMR?O2{g(dQ_@WfZF1|KZ6ohB)<v+sI*t+zc5~!>=JG7VXjWI=}DR_^$XgtFs+Hgg}24AH|aYbTJNjk@@M<oixGYf1}!>c=b&x3=_3wb+;7*=eE;{@3ju~K|?g$O5&(xILMAo>`lOup2?I{~tAyI+(eaUFwKBU>tZq6g`TMqNqd$?>T#%liS{-E9B%Hf!Lpv*lZ<=7BC;r_!SoV(A4%Ml8tsM(ZDpyGr@<Rrza6*=_<)EW!!uZDUm9$H%oYY2v&l6u0=lQ2m$1UHO{v{ei#l_|68smB>MI8ApkkEM7nL<L=pVufq0EiK2~-%}0?4$wwc_kt*54Sboq!u(bdqO0-;+P_{+JhmxM(d!wD?zJt#a3hSah%vjD4oGCll&tUT+vY`&-KX!0ce!Bv7@NvgogQ|j&)EkALbAH%#ygN=;j`kG7-^TO%*;QTseeH*5A~BtGWO%$ZHr@R9_yZ;=OpSjAp-XgwqR9Moj;^iI?T*IwIu2`c-`t=&aeL1+JZhmK-7>ZSa1J}+1F~$Py~RA+fp0<BJgz#ICygBtk4V4)kQ%fe5U6~mzupVz9v*Vsa%1~gzMCIsZ1He|`JDr*Rj9T{|2<dTK45EjkZdcsfRIj$5%0ji+aYZ*s4F<2Ta7^wFsDi__#@hiRyiozS|>+Tw`7hz|5WvBjK#zdkZr=9im7A>Xid&%z_N+M)`$TRvPmFhZ-Z1sm#`{t+13b$CUSM}xWkB$X=VC!DlMU$D5<8wtCun`^?!&E8O-zi>nL4epP%0_J3wVPa&?+ewYP?Ne{Ub59b=()er6U2?AsGN#q#f)yxkmuXn_80SLsjV2Al5!p8_Qnn^z<9Q*A4V2U0v8KaLm?x{f)lh9|ToNHcHU(aNo^a09Tz>lZ!(l=g(m#Gx_ADwa`|Af~?)1%|^Uco+78v>ObXODe4N&p|vm5Z2O(aYD9sPGZ9DmL#ML#>|OlY|dsv$hj@Od?kS+nzyXl5VUN?<lK!dZ7XO^m|}>+26CgTUE2Z~o0oPUe6!`&OM099Ex=vxtsSZEMzwgpv-ew68kr(v!YYxBl-xls{@gb*_K`l)tdSOOp;s5+37-u8q6jHhdkA%?`#D1vpvdxM{Oln#`72hJ$Yk=8?<Q$M;#bK<Bqo^_m(Z04Sbvd5rXzuj3w2?S31LnhGv|#_K@3Hge06(N<d_QtZwyIe{>;Z8-33XH>z&#?E_5e{8=tIrIpul7d|c@&gea08=JU(wrsWh@>!4Bfw5)etpWm^}@5bi$oU=z9g+#yzlV0P2D=*hm15Es`d6wViC$ZIQo8`CJkZ#a5qlrFrM&6TS!qpy73v~%MqqyG*f6u!5d7y`Wsv5pUd;P^STT>kMRU3h#&Tim4nocUG*R^Xfv-v#MZiTik>mg7;jcn+Oww^n7+h;S47S{aP4rGdWFhf$#PVj5e`ayNw9V-6j{yb2AHz<kjoiXdI0sq<Xzn!>}a3uO_lulT0@Qv$;Ts3SJm5TFbcSx?0`gQ)g7Db@^sJ>-1EZGf#Nw{IHsbQ#|?-w|u!8JU?u;L}50*qa-E1WIs0sf*ByjZ{KM1mg+@G>|2cX{TwGd24-Q?t)zr`33SptV-4maU{?PYkGWckF;YTlKVzgY`po%I~)>tf1lw#6Mu~%-OY4vm<ngCA@t6er&?J6WWatYH;ly90i*Sz;E*c>3}AsI+Fwk0iO$AYL;@gkPP<Bh|0^T6?HcZG#bw+5CFU$;juh3%O|d==b8VIAHqgi=Q4wGv=mv<O61%iiUu?abVUHz>bP)VNU2D#>D}06W8OAefQ@K6aOOH1dN+(NZ<K&5J@Nd(juaenf(yJ$bvlGv;!{?rC#qkM4?2;JBJ(KVf~AonQRxD=NK=-8Gb1sV6@2Fi<#Uf;V(hPWE#)Qmz_NXGl16{zuJTCe5UY9Rw`yT~CpCApNb@6Gd<1O-zSalvoLQ~#k4`@r55B<SdGsubb!y#XY3!`#f+JV1=U6`0ME#(x!GI;qUlHfN<^h&)!xhS+wJcMirKMwug?sUif`bvaqcj~g=UqrA3aqvD;<N1@2XB~MdQ2Sc<kgVVsF^^a1gjMJzAS&w-t=9>g{>`l%LD8%{FOc$-f`CPKuPDVvA;Syz^{TMfC#7RMfX&TR0g;D=nQI7S8DjfVzQbxdP>}*zJ=u_>?EX?4<!fwSgxv@u0+FVqq?6Vp4!Tf?Wt%`xTf$t!>II(k3S<uW%xg;_gD%82!L%29Nd>@mV)pNtL0KaM#w!<Q+1;a$c?K33!<%-t3gJyyS^Hn>o?D>hFbI!(?u><1A0f{|2C#3e`z(ip_;J^EEp(WwiLJ)IjyWmFt3T439dZykMSi-!QE6gCYEo^^Jq0&2YjFXsB`|aN*Qj}6Jdl}ZlI^@0QD%~Awu`cMG(s(Sbf+cXuM%}1pB2RX8idn5dJBIczGJ;T{X`j>?RGkswH!q@|7IuLq+B|^S-mo+pz`0_u1@zS#^8SZaM+Z^Ox+71h+?vUU8Dff0sq$Fy#482Ned3$$*;R?ACU%FCK*CRbb0)S1{BtGU|c1xQ(!PAh{+82cO-_&E%Htk$Yj81U;{Cm!j|Zku|F**!5Zla^zi#YoE7U40Fq#$I9r|B5}Bp<#cR+y?G#vzS&~WPvxLKM(bIPJ1V~_0LzQv-+4tRFDb3s?3f-AW@5eFi<Bit7)ZAMkQ5#~nib-$TpKp|sz}S*?T_5%O1ma^3JeSr18#E^7~eo<iBy>FEkRghBEWyw)dmv~2`zS&*kL``NP{w$0*Z*ZsVC<3OM&_cy-;IBK3&ImTINa>ld5YC&hZf!*4kx^6?a_Z_NHppTH(-WnB!u<R+lC@Okg-dU%O$)!i_lIS)4*{WiQ?Y>+qC1#KOA$CGh^fDooHl)o}7~<~#{<Ah0#Ee3BC)g2(|nLxx$r&@m&N7>s!UQJEv9XGtPv)mS7qv597l<yj_t4-5YXujX@^-$*Ohtw~8>wOPgpJt$rfM9|-z;)r?{K_nsi(YXg|fL;us?#Qqm*W>-+2)oe<il^e(&fU=&y`!9Rr$}K1-miSQ2VdxQncWSW8J?8iWtM7!*i@~-wmvhSH2hOf(S<S@=*D_K0Gms$P}09*Nf0`q-GLP_tG=e4dU!-LNP#4B<g0doh6ZmL+YPo?z~hw)P<@^IITvt`44aUChAeLlt(VVC(k~~79lDwQ#I4ion8p%uCMhkZQa7?WGH+9eHr3Z5_CF(ujODQLw|B1aJB`nZZY_4*0>!Kf-qIP+Q74Qe&hVnhf({ny(n-Um^(x#N6O8C8jTAGKkHp#81SOJs)QEcw<@&uFW&T7MBi>EBs<6DUkr#8iPUGKnBahO^=o!Q-dP*Q_x9rsg;zZTx=RBZc_7!d#4Pzd42FM(F{fs3vE<a@lPgJAgUUJQhIW?B68h?0ssa$_Ml7&X2B~chNJKhxy9lH!aif9xTQjBe@D-f*I`H}AQWIQJs4)OQk$SzLbGD@V|!C|6tjdNj+lb^y@Hh+|u4>qa7u=;%xuC}gkCI?+Prk(r7B3AOiH`w7uMj7nCNK`Rz^{GSG8pLS%$IC&N*G`C+cdv+H8;fD(xX-?5jA1$1qB`KJ=iT>a7Q+G`Ul?c_YtY1_9F|VJ49^^Z+MRBVm?3-jiMGc6kD=A#$Ev*T4PUU;;_s)YE)dEMmck+LcH~hCVQP`=YE)7N#{EOy-w$Y-*kVcL2+I$5$P`Cvj~udhe(MxPv|yMdrxH)HVPBrAgn1g}ZFIL4y}BA@@cv<ooSLFPU+SMdW65Jf`~xTq46@YjxFs~qZ5`>@Fm<SyXiKL*t{q9I-Fi>JmF*&?Yls@+k*PYaEl*OqbYE@ojc7TH#*7@(&%RFvI=k8%j$-Fl!<iRJ$i|h#GwIi<<ufLpk&xV0UAUBZJ{Cq-C7$!G?_ZI4Mm~QKNe~jx2nONRx}n1tfd)vP<1E>nlx&XZQpoN>Tk_3mnQzYPHrwJwzPUUfrJTWS^*5U8P4@Yl*UNnygg2q`w-J8(@7oB!jqnfNfBi@KuYdJt(`){kzKLu8;QxLi|KV+xe!{U$AMd-;ALOz1ul{U&^1rY8>>r$g_3nfI>p#+e(~JMhZZhRz?7#D?(tpRlx>x*n@!GxUHEIj&gnIFBeCooRvAn2Xb3%Xlw=WnVOSn=-$KLM+KB~q}E-#^(*?&*eyexe_rrTqog|5ff>}Mk$iJ4#(Skw?4mE2)>`3yq8S+o6X63`OGDe9ZfScOM9`jh_#-KI!u^+QHH(#1^@_wyfV6VBD_eKKvO6S;f8RJ?b7BvdQ!xTpTBEq?kIYrwD6h&{gs_fXBhI`EkWPLJ`XbYCYIU>|X%Q#y?U$Zr`$O;HngW^abG9~A+ncf4uaPFLQPV@k!=-VfG*q#w6@3PqWCJ~EZkv~~vPbiwv@<pQGgshFB3{J%QC+SydGo3aM6<!k-6kJw+QSuwpoJ;BqfJ()bS2Wo${VR5th=89#QuCt2H;NQLsLKF)Ko>O99a`}|AV^nuG4Bt#9eH4dx*96=BbbwxmnNE8sr;?DLsmkj`IDO~ZZxwBxKIZ)Q$@NU%QpDuVC7vtHyXhT#WOr4d{;5m7emlm<GQRc~j+`#++E?g+G9Z(}m!I7NUi-yo&u&48g_pcJ{%M>5<6*|*IZmYV&h%!m<HZeb1KTc+bZlzY@A+pJ$CUHCOV|0tW!uy(kCo`e*=xHaBl@}gtlcXH@I}{iW#q@Jo$k7G;~4rfAbxiI$(!THy*vFq4&Yd5oxhmxvlkDr-CXtCMTO{}e?^hw))nPN;Ai}S;F;YLIdeRN&48(#r4H0o07@lV2Cbo8U2rmEwF8|!*o#&|$auDI%-}KD+4cn+laDFDm~ak^*}=EivTpIco{BB|{EfaLF?rMbLl2_E=C)d?W0M^sVZ-(i;-teGR0HWJs-Jt+7=fIPeI!6zJyeO{6F{&B6p^hWv_n}YuA$+(1;M@Vj_$s+4ex?8p}j4;YnVhjuoPG5_T>*5L0B0bQgcniZ(6N_GjJmjQr>TZU{%6|qvAylI=FKWP#VFbYa&QK+T`*e<VS)b^Hg9Ix@?D!<l{kY!*jYD{I?-v&jZ`6x}Cp?u6sa@6^&QDL?GO4<&Oh8Wd{)o{q}kLK^`+oTcEeGb#X(w-hn+S5uMsZ#lJ&wOA<V-;E&*icKrj;R!wm25ilB?hdcnxY$R|&6}NZnRS?I9vrf=}$-tgovCOiYlPs-LO^L+fU^f<$lf8NBF6hJ#C=H!`B~=(O0f?)FO%8#Ss(L?)SO;uyPIXUb&8Ij??+n~SH5YQ0x&r2iMx_)<WV({`$bmPZHp)pvK4f#K*}SVxE^01-gAh0CDz-68c-O1vo!HQ-6)cFof}ZFAqb4M#S3MZ?-MI{%!jqylQ3KUclPO4bUPnr2HY20MDUwU-NrmSHdrM1sXYx2ss4Xw19Rjz!pi?o4zSBmUXn+Sk;h<2EASemW3tr`n!?AbP-?1U8#Lz*MKt<si{TqlzK%O6iRg!~jM$y+Tyma~<-3)8gIAO`yrQ(LZP{|k!X@-zV<sr|Q><V!(rsQPtSL52A{fkS}&y(~41XOhE&Es`*aFNl%i@*|amPxxfj^91*C4z@7C7Ri$-VPId%Li9B8`}rQ*VFBIH-XCLn6wf6LpXupRVU*x-b2Bm2~#vG9#5aLFY?lmlW4Zd{(4r%=bG2&15QFLmzu(Y?iPrq5m#n!Qa|nJi_Gi-`!vUQ+4*Z@Pj-Z&!!|yUA9eS0ufrYm)Sht$X|2aCxp6D95u9QWw&061^g%mEuR4malr1?>7&e=a?F@b3fl8{6S8)gR8SWryS0;DDu_91)O&*02cc5%QhmR0FiIH37tt8(_16V-=5>LQM!`?NJR-`5~8an|f0c1AJpa&4+0FJp40+oafj&Sd`0Z(N7Z{7<t?6Ua^wIQWrPZ0jrnFZlZ<Z-<)*re|$$l)^T^$Bbk0H}I~8SaD`_68W<6EGZSfMH)eqA&u6BiY307y0X$VS={&y7B9^p@s7%zZY6Kk69=F$|@XYIAI#5rkKQTTODcy+{S1Op{SzB#nttA0VfQI6WbYphl-ySD(wHXK>YD(5I;CktFSZmO}M&+&m><h5ijCH6wQk-I#uMs2lJjwD`0in+V4Q~0puBp>fqZ&@T^Wm5-^@1`0%@4d=Od&Vr3x3388qN-co)a&B9KwZa>^Q3MpaAti@-NKYx@0H0**56dWIVA<kH5%Dz#}Z0gntkxx?7>;Kl!uxjqvMdZX=Lk-SRE9&Wg>;ysj;FajAFGL71M_2J;PuAOcTd&DsTZ?B>fA1{nh!Zq_#8??R|3ZK7b(qy^4zp^B%a88ZE?`zoD9yddPEZ0DKC?^2Titmswji{WKO9}dBwC7W<(c*OTGEscbGyUR$|u-2P-sI#@1J<x(B2c2R$1$G-#^(m-B*R3bTPmy4KU@c+{pk#Y+7O6#~$EpWLDfyE)1|&22uljB-zI403XmN{yqcz4?Wv%U_&m)^{m&R69_d@=N@vFl;Y9qAi|wbi5b6O0_{}GGiGpK66NSZsEa=#<b0Hp6#lnzMkuoZ*w29dtumbz`6?^>oTCyMV3mX#>S>F@2t+&-iY9M4%uY0@CNY?DXq~sO45KO}=)?;9&Wt%R7B|x1`ZN5wH`uxPd!hJCVFK9m9SlQP(EH}B&OO`Fzn%H9xE*mW$j$Z^8_(_1<l=_nK*pt~>chzMY*y44oczL)jxK$<sxW)=Qfj8AFo9GL>`LOoW1L=}j7A}#_I`P(HsG@_vcu#S7f+s1V^lYR5lm0xZ(rogd7ii)ekPi5!@Q}%&A|Nf?cpRhe0T~Hj3zpqI@QZ&jnnQDKl>frys^c~Y$_fc|Kv+s_U_Hqi{?pI;nwAiu0EiBuM62YxOBt6V#?#c+0wN;bOf|)(O74jd1FN-OPKqhM36YC4yAa}i1_>#36q0~Y~uaZt(7BpUUXPNc6N6h;n8Y^n|}AVh9_4?fT}<JEqNEI9k<CI@lkR)<db0;qRV^mEfy#a*au%4M>LnS&FO9{(7a?jMB42{QFu`(4|`|4_M)w&qTs^E`it*L+>sE$v?BDof#%``@N`pJ@Z>7hI9*2vsLn<q(u-zT&WuE9!SnQ`4M@%YyFf?!c-D3|deQ!h3*CS(rz01Q{AUsvnhTw;t?4VO^&yeaaqC(0vEMoNL`OB;RUNZyaG|B?V;X3_Jg89@#IW>X(Q}70v-1u$F$vs$E_XWq_BD|wQi~Z+;4sqfO6Liqg}g+hl3U(4F&FoI@->rxL&ZHOgt7E{tW-PcNq3x&LCy~pPU<`{#+xYFC&1>Nu|<lSPbIPzix%tN+eo+M!@&mIRdw=R(UDC9qDnat5j{Cb^VK|2Y`j#V!7C!0N%_T4durITKAHlRQ4!yEOm~UIIZ|OflF3>9Z-MH|6mBbwD9$W&?a3PKO=1juFtx~;ctn_r?)pS((a@Wef3R(Cc0jFCWQfXuDd|i;#Qdj@^+VMv6B3A`kd)U!qYx#!j>s=xN%)KJ>0)Y;leRJ&*x^F7TvmAEcWQ;t<79d$Q>g6caq=QfF)nWllA#lW6&}J1`Xmq`v*AST>=+}z<#SHHbW1Q+9)eg<(G}CwaxS^r6PJ2Z^=z!oF6k)L(lkn3SR2vpk_cdT%3#kd=4XwW<FCK&X;Y?YyK%MhByD-@=S|jLPHLF~EvCtqU=suvvkvPG<|Up#daD~h_}TNPj`-74U}51K$PEuiK63>Ejs!hhFy;M7LKoMtVQvJ%s4hZT%zZEK!w(X{_M0u12uz;%t#<wZ<vLjA2R_)x9&x-xvmfFlLw@oA(<gg?f4q8+jF)JjDm=zg<<oPk1b=vGR&gG3OI#i#ji~aS?88n^X#+K#r#9ghCh!R22<EX8vQzM-veAYFBZ9mdPX;T$qeKbHgE`u({h?uG0XjO!MffpwcxU@+0)2wltc-~n!$10JTNm6hl`*T`YIiA9@pK^FsxS6hAU!b%yflQaPlM;K1kbI4=Oc3e@-vb;z!)kkX69~2@uUN!zB{lpz)g8q#&6Fcd6)&s=~rJ{HAPxYRnra$o;p!xLUtowu^1>ZV^7VF{51dOb|ah_jWF&QuoxT08M|9C&!}S>0c{?=$rW642=ngYwK?Re!zAh!lofsDzMDfr_Brmeaaj4LRnnTRblA(B=+ezx++dd-==(o<w~i+2m3O@Sb;s(exoAI`x%hJ*dv`b5RXnSg?Cx;3md<;2nVU<_ySJ@9f5bR5u6yp|j^2^gu#WWB$&EMk^wzn5ueE>Yzk1ukJ8@&ow(wOXa;<RroNVEn3!-cALO)|0aQw@!d!+eJAEXk-w4i?caw9)Dsy5^K4(_@m*CKmmYm)8lwwFWb;o0r{gF>}6zi6L#i58*~R`3WVT}am$Wsm4K$-)b1F~Ia~O9=##8{ZUD_*exI2qu<72xzK66Ya{p*eu2P78Q|D67$eYf}20M9{?}m*FGqgTXELBGL~x<$aPS9^rV4}hO(Roa+nKK2<Jhh(h<apogqOOHMYuv;E5qQ(Ic|X2lUC}H-IPu_}TDmVM-YLHOMMp{4LA_2P2ZPP$x2dI0<tV<wx+7hTuj4w&)AeIWSopc!fphElD(#kr*(liNPWHISdF&)rJNVyTpFBitI3^BL#ROn~e7(T9tet5mXI9WX27%c>kdLHL_4LyOdA&Jr{-uG!HP}!B`{)W?UO&q^qNkf4B`ffT^jEIy9hB80g#m!`}TP4cN5W8frmZ2q}i4jsv--GzA`9{E<n<inK#1yM7SsY8ueswJRj2A5juuf~gLJ_5I^{GCrz=jAx|mhX&*hfkaBe>A-VKen{?13b5uY+2*TFqL{~>{)|H?mgDyo7srN+4~&-r1`-BRi)J%B1U%=U{4_xdAhe4n*wkXoJV|$nUSWx>Ggd4-z5HOY6Ok;VwnQO`q(wu|&90D8gqUwOaF2^hpyJGJ;I{|F>41&Y0-uo5OLv6rNXqK?AZ85D@O3oSx;#I6$w5%9O*gXTm#&D<G0K1DyaTV3EE_SI;F?i&v`m^lO7emRi@d?vFOG@Ir8^%Vd%umQUD*d}M?lFJ%uzqh{9j|-K_LjxL=zP)9~)AQdIFJJ(tCGOh8NTfIeghorpxl}d>@j3f#$Lzrr&fhZVF3VzMWmRp#>x^(RNQd1&0qhCc|`c+-3?<)E)t0TqUN0JV=i;qm-Q+?J2+ao3N_C@ez`t=XsKAnb2h#bf{mP1NCKBtq>kRwX60s=s=<y)m9D3C3DQYV#aedW;~g5>Q>bNm0s58s?%I&cji5<RD75vK)@UEdA+B<Fkuu$!1yhir=ua&jxKJH1Bzs=%)ccy1}y|(6w^$#tT}*CEH93pVXC;p+D#=2d2Mqo5o!3wweaCam`4aAdmUWS&8Uqpxa}#M(TI|m)xnm)LQ)kA#h3Ru@GyF11HCOFq56VV2?RS#VnL}T1HiJ7EK7sAmN(GI4vxrlX>BSqh7UFP9gBk4AER{avuRQB%r}GZbEf7)8Ww~<`LHH|0#Y^kd>eI->#18KegZ#y0O+yFeno-=9S0UBGKvi?lHoCmKp8foa{@r3kSUm=rwRaGbWD%(?jbx-d;fpFXt^TshZS2NiBR5DQ_ZW#b}f8gOVh^%Y#>8D>PucS{82%q14W2d<b+8aMl9wUTG9T6Ub464iha?aWjx2SW@Br+9oM$OJ|Ht@Ju#KFgpI|-S-rKO=}bMAKx9uLi8AGJQ~82>U_U3^+t^lJzQWI8cOx^~$j`<X{fI>>i4T=?yD(SOHL)~5hw_DLpR7vD@Xb**7+zL{kB+anKjS#ukDhv4t~$6PKVmN)OR?b5n<qdnEx4VnGn3?s-tISOoBpd$TyI-(m&ta%;VuKe<C$Vxo|xu#jY##pDOd!TXC;y?Rktpw_$W9v$d9v87(hWpl5LjUZb)01oxUwgZlRRidY0T0H=x~<B{#IVooz$zY#X|nf_Q9FJE>DJ<oLWLH~+WZ$df)5dD7dczOkXajquxl-$wXtgnu7#CKVs&RUfb4Xp`P(lip~P-e{BFXp=r{(!Mb#{Qxm1E#Lg+nUkg$>3Q-bB7jO_%NxwS^jfGksUre%p-v4U5%>wUD5Ri5*Qibbc^lMgh~S>sfY>}H{u@HeD>qTy6xI_rvJh2nM&1(&0n#bkP$B+_ClpHFHw%6yBP&|+Cq4b&%Ab-aO{6=hkWI8tZe$gjaTKY3d(N4(WbUa95bLPEsdfVUjn#qQwHIT(iTGNVvo#@1!|N8LL^{uO!1DS_JI8bj)r=U)9?Hm~q<6yXi4;bnDvZ1`6W7#4I_2ES9Pq?46giFR<bXmRv$%y5=A;GX((LYx4Qpafk|+tUc}9{nzNp+Z*_>NYE?s_e!AceE7WgKro>OlRdVY%5#|7r3>CN(5Y%6olp{x8!Bhl0u-_JQi(nO*39COk&lA$oW$P@aa^8+rQ!5PQW#H@2l4)heK&gu7t>a~~sAqUKPm@0oVnErHBmrrm`gY+~>(lzd%@qqD#QTQzRle}L<vN8CP-N&X@usP<!;=kvdNfWQqe2UIqJaLcL?#Q{tqdz;$yVs1;$yE7}LB96aSlIi<0mP7chNXpistVP$p_{)`l@p$f=jGnKIkl3X{T`V(PLuur^lRA#X8m;MeRfy=HOv2|OF;Yh;&V2aaJ94QB-+!bgA151TFtJTHQ&{xgx6FHI*sYS{sQ37&ARFBXLA|<XT2Qb+1eKX0b4)kFc~fk^-L4${NE`*3F#+FsWIR0)<_gs`?=V+s5`RiDzG}2`{FNmJ6?OS{5^Y=6Ks*K!eOqjROw+=?(*-af2u>}Pf1uneo#rA%FiF40FG#X78DY0?`fmU;v0+OQ2v{ie{~mCqE1HAinFN9x;b7%f9*ec+syA)zq)7>hg43mPH|j`TQrL&f-KW_G#9W02XR_*$U!f%hO1A%5a(#I{wP?djv4?sc+SQppalqXjc(tlJ&rzEXPrmzku6+NR~UX1kq1m%3YFZ@^{zB;GmZ$sxN}yNj_RXPJN7O#sKlDYb?_z52~w4+&|xP<x&R>LpiXoT3>XULH3XaT$M*6RgMFX#W8*ZTk|Zs|-Vj0;AXwWFR=I9ORp1}=0TibLxp08@GZDXprybNoufTxAtX-TfcKOB$Sj%_8{w(9A*>M7HxrdOtqGm53`Qfm0kU$_(WE&TJ>#U8Bt#S<BVu2(;vntelxiR7;YP(VJH<-*@02ffc#|GbCi!6g}4+mT!b=7|12Mtpu0<`rtV@+6DxY&4if-Kv(BWbzVR7;W>s<DDzq;mZRQEC%S(Q=M2Yh%?f@ny+q*6;*Q(fMQ7`m)Dv!Ak=ytY4?nNLis52*hr`RQ)EFWv$_FIE}WTcQ^<K3x&3j9x4&TJsgGn0cwd<XmL2^C_FSR=MMr^9631lmy43GvPR2D?*_Cd`FnThM}YOd2^6yT_h82}p?SZ`D^S!v)UPMnDPKt6`Y-U6u4#Q*g`p0^P^sA;LT-UVv%!4{x;x-s2jX=ixc{)&2Lnk$-9BIDfG$~n;}H76eMt=|tel=!X=HNX2Py4~pO&aCWGD)ET?{};x6+ht$tM_1&@lhWSlZA}ACfjNUs}!K3R0H$&wb7Xkd~dNWM~}FOm=<tKkK1r>Z37%c;qtm69HwHp_S1XgePRnd!j3`NVcE7!}PCyl&vx!4D|BKgp0Eisok<+Ul;gC<Jnf(iP#PBK}nP~6uq{6vNJWpF~@RstK4{o8O|6)*xB95WdS0I$%)$bThcHD(x2JZcjWxSxudUvghavuACJUYGs%-iAyUf%m1SlpsmOoH0~j8xytY9stW{olwI4dSj}ZL*BH!{Fw*#CfAl+~oSCM;nHXOmWFHRb4ZX%ec;5fT9O(Ks!8{Z6;1?oxRYMD%I3sEgQZE^i~`cw!thcPd(o;jK=;f+}2{g@`@mr;saDMW%o*}j1`#VAd{R*8c5vIu#yG%vOY9nr6&MaVlw{k|~k4l`@}EX;Z+Fzcqktig1F)d=b+!@5c7bJ?&ai;yh{`&!P8!g<5m{!+u*=CeYs!!N($k$w+XHL%@UtQb(96xW?M@Fr;@D)KQcfsT7j(7aU=UJG_t(K*zx9?n*DpsUfq%+}nLR-%!mcTzWO7xu==76<w|V8_ME?M8YAhql~~JSqxq^7)%}UhVMJjnxpnHJoUJU$^YnQIQ}(54zz-x{II@ZpE|&Kf)JA2NT*H7^JQ8nWF+_uDpngK};Xfpo2I#k|HjEmpE@avC*v(M7{&Co5~2F>V?bDvZdD<@dJCrVE67`-zGLt)AMqh*t|y!eqhc0uU3!Pnoo!!w=sP%4T0rH9+0&WPZhEctyrhlFc`^>;ZnP1Q&oi~^G?lTD+p0^3bi6-zuO?ET?8N4X4$%hrXT=ODLz~Rai&7R&4GA?_P=9a4nqU5jw+S!#)^)c$xB-?r&5@bqo~+<&A>TDNMQ8kyBXVu<h6Y{Cg1i@Q5t+svFc^Q={gxu8p8*s8t~FY?GBX?-@#eJl<j7!jWjPMI$Lp1?)cbG6xFkdYw%F|0QcC0wrgWB%io(ceMb_rXyk;Q)vV|lwv|bH2eN=iBb%D&TPvT&TMyMpbJe*S3)wt(k+5jJGfu@JiXIW9$bMvE9_f~gf_9O~7MI#g8NA4;FFrCOWLs!(kKDODVNHTJ&JH2!XV)2)Lg5Vl!^oUArz~^x$+aZxT`-1)(G(W#?-@B;Q8U*SMt4HFdy!add~l){3*v9JdkoVsx_HLiJ7+(p#%vpAd~xS&lI-xvb5ZRTg|K?YLKcmS%yiFZGvxd(q~T6U?82EdlJEHG^1OQ0oSTxqF+Be1*X~W=0V2Kxlqeg9eP?@9y0kZ;5vWJ!%*vAlmb(%@)Y*QdAgLE)d@Sa@F&e&mes4T-GxC1pq<rlC9({y0yAOFnkY2Qj<nti=&Wjbjxc<oa46Y5M-n{Yk;M?F1!ZsUHSw`N1Iy*NlHN`6n7WHNi#y*d3B2JS)E?bebCD!kT9&-kD>qf#VUYy+FNDc^YLree}U7V7*tN-G4Zr=@QCD4mTw{KnCKGqITIVI%wq2u_BrvMEKI1ePGyQSxspULVn$=K_{!NhQ|9m7G4;x4bRzC?rxt}h4+8YDE(8$%oh8BeN|ayVEGA}k<ZBh;E1(WK`IheXv26a6_O!oU00<?tpE{RU)y`|sNbzm4$Q2*0&EeByS8H<jqOc89lihqrczw|0j&mFPE>=nw04c!^5%1ox_W9-|cumevD(3{yy^-QX>&8HJ9jrvxCHA(%qkF!6{Io|GSgK=(7)J5yb4!M4w}qDS<7m^vONl=r;#!A;7|!q*!B-=t(0O3&lL5|+k`zR-v*LGCB8cYjGeT3rHej+Z}cjBsJ0UG3`AGcSaS%RMf%nSFKoyC_o6|GR+yQ>t0~K5;`d)D{oWvpPTTA$VF?dZr%jd^i)>cBhik-d(zKclx``obm{o>f$wEEj2}Vi^?#I3r>rch?Ad_28hzX!p0GAgl6-0hiW-V&f6yD<3HD;KD|3P>yWV46DnK!0ywKxAR}FqCFK{L5TkbQ9F2Ygc)!p95w3SX#51UVJnbHE?UQ{Bm--~e9-Vm`#1k)`ZHB1o2@&tknjwnr`15+w)roMmf3B6mKY#Jh^h1PMKg6OH!=GN*?3!PN!5=k`=P$-%s%0lc<<A-y;`EMyAyPCMVf%~MqgHghd`@=>zwfSGXXT%4>6rc1oisqSPc?!(-6nEv^iDcRN}1{Mf3Ll+u6Ia`qXZ(x`B0zrkt`c2+`OS=KFH%G#c&mZehwpF$nh-l`v0WK@qAUS9$fqGiX2a0rGx6sRrggDNGuBhuw9jgssooVWT6j@-`t_N()wz+0k8AQ`ON_}aq9R22obk9xXbU~qkypk(I)CH`TcF3&k6iv98hH$qTf-equcsTTOBLc*Mu$~Fubb<>Q|ds^)2iK;9PChMUQKvc-J=g&02Ce5YV{!H(ybi`bi3zJ+K^pK=EZ2Pr10jx!04WuXL~x4}#td+)WSS>`>&RiBbVXMT)bIns@-;8jU7PQF~Bk3oz0PO0owEpeZPlpmADzp*%Mu+A8>Z?FpB0I)n6|J8zDo)sh=rg9?)Q?zWUPTt^oB`Kis$%7bE-ATJ+|%;#x(eu@>s0}G`2$pfOok}2E^55i>MQeL6*$0NM>fwp7#52|0MXw#RKND$K<=^1$;boD1?;a#3g52Ew}N+F4_Z$%6_K{f_ap`a}|=?7v6H&sXC)-6!1;Ma{PkP$!bje-#X!+{*r(U3I!An-IBA{m-UK}j!KM=~--Hrx>~Ak?_D-q_>f4eJ~E0|gt=xf16`f=0Rbhl0XQ)dGj$DZK3^Iz2-sw2AWMd?u^bi4U^nB?T4Y$?TbLP1R0K41rD5UEl!PVd{w`RKcFcdUk<ckU4fOv~%fR`WId;JnxI@e8c%Mm!vpeQe91`o=53Xu*h%1^Sz@ABnr3fC_KNdnjm2X`g*q%`NlMJ!vV!wDZCA9C^Z0ry#ZQG5VLyab|lJdDaBj&5EofRAgo#Rm*jlauBj<>SFNN(8QpgsBt}s!_WsDRSyjH?ne+sHe_j1gAFi)7g013noZQM(m?%;{fEwwEt~)^Nq)!A-XDwMp;R%BunYjb_L6hfjS3+G?d4a${*PQSX3mS;d0dRz<2nh2x764ZOqc5qRaa9e@d656y6d85`ZE#G&M=+oBla3<tETAd2bPP0Cm^A3Bz+<pL0+uF}KY1};Hqjzm2EW#Ql9zU`mgW37{WYCvYgU@#SrI}Cv=uKLKaYjktdO5e@KX#teOGXk(uyRRq_{5lUkG7Dm3g)}b*>0R@&XWU{Od0kyyd0c7{4aSO}V~c-gYp@c_s}H5+uVMfn}{soC*xq`JEf6OC8wqgLwg%m^K*OJceva?%AG5LPgy7!6fHAQN?$X!^;nAXNs43%f3_F22O}}vpipRY)#0|5Qgx89VkzeFD(<#zJc3{Y>fcG=iLNazJ!)=uL9^fA0V`M<c&zifz68{xrwIq^dDs|^5-KD!^KlXFa3wF1EQ=ZhSQaZ8YYPyQS!=|3RXktxWdW<P?4Joq9I_+$3_S<GXzWKdLU0-AQdohH+gQ|0O&S&E|ok}Df2RFDPZmblkK~p&cN&t0q{eOG}6Hrde*g+FFQn|bb<_;%Ge$qN_h+P1w0G?uT@6}aY>z%8mRWR1K-4!)(R(!byt(G9D0^81{6pxC?TNqg4w2_WnZg)iXuC4q0sFJTid*K@DUgxJD5mv*joQvuX|RW4TQIBuw_Q78O))-B49SkeS0tfC!&XHY$T_0-zROb{*2BSOX`)n7ue7seUazo4$mKRB%9wvJW+lVvNI8Uyj`GJg~vwK59%s0%GAUxXH6tg_Hnb<R#Q`Xs3C{N_9BD|O$)b2{P6FtL5ga)Is+NnXZjY{lmIFEWSTbr`RktfR{BHMOKmHYEY7D7ygO5Np994zGzYk9A@1JlQRlJQUhW&39`&<=HZ@UVwQmuIc*!c)gF(c$mB@&R5?c`^#x4QvBrQ4^pnlS~rGJ;u!F*&eak^)_1dyifJ}XKr{K`x9U2nnJ4h@XG>zVNDcgPwC3Q@#ccN3(qz>N!gpt@t=1`Uu=t-=vP3)rb856vBHb9B;fZHxRQc7}biKZ+>$ehaBpe-qWQRLw<P^ZQ3wCzFBA7IvT>{IO-zU^Eryyea-<KKM32^FY~H^!06e>AotT61ZpTGJMH(26)HJ7vF`j+siIUkjXS-M?G%z;BH`aTlm_+MxzfAT;XBxc3<~uJ3@yZci@uBTs)kA`PG_%qw3tj)vHlHjc)PbqTXDAXRfe!<*UmpwzHL12^5P14iX%(WtNu9Y_61+W@{{sYb;>Z9vfI)LWL3h=k=VeUuxM6!tKs?Zri#QV3=fa_f`IQo|pN4(7Bn{+tvmz70I;q9p=Gai%0!6w7Q|D>fA3@zee2s2)+L{9tfO)#-R6%csa}S4+nUN>~PB;$&)+i0Qh4$0v@Q6jyPa|0olZCq+Pr7nqi22BVwgIFz*~b*}^hYIyE2J@~^<``){K|na=(|6%@&<4y4@&P9ML&;xPjsg%{$Sy^TGs0c8VB8YN1Hg~a_(KI6o|mS6jgxq|uI6$&7(ZRq7}a4}E@k|Ww?!_^j6cywzbXMvvN{FJgC&X+O3ho|;xwo&+MZ;l0%MUDytJ6lEG5ZR&q^RJu1d-#O5Y4{J@G}zoZ-!u$eoc-wCa}vhSZW__FJK8mNj69+_X3ZP2Gg5xI$y;26YsS7Z$*7>Q#UEBs|Faz<RB+7JQi8uAgm!bOuWb8S`^x;EdbKOyCSkkRJ=HMR!K4YV&z>rkF68)q&{Or0oXk6VeyTe@E(iy2T%W9gHD7<T<I~ntt*Pc%#LPUK&G1Omhds|mOfOD-U1Ai&9{Wn9{v91KCJ!+1)RE1b@TwUTqYRTy!1{EwFNg{<6`bJK*uXbhPJPw3rZsRGtPi=AE0Vz{!#}tq6VXT$diHAuyf(0YSJVY#Q5TdtaH2YJfHT%KkQReFaQg}eOkT*za`Kg!G(MFN_V2$==+oI|Z*rfn)d*fP6TMXN)8XJnd_~1i@u^^$ZD(QC9WqBNi2_6X*Z(M$f4^jEU2?z>`sAB=cir5e-lBzefXtUmD{Mrqw1C-NrtY;HZd2V=MPNNKJ+Aq9e~bt9kH5%M&iC;XG)ni({@im_+*w+feUnU@Jb+~g-qa291nO&p@G{3HIscF!&kch3L7wS@IX}Ax?r)Iw63>Hmy&*~Zpq!2mH*kXxiQIWA$6?4lBNlg$hZcX_lKuWqT=0=<co%3fo%03cpPqtD2Tsb4^Y13AANm1xh=3#oj$v9<bqmOpz%_z1nEeoXBgJK6N25cMHTxdaf6F%wDvyQ~8ZD3MDt?NhO>t%3%iS&?gV1S%V?uUg@K@$RzLh-|C1~`g8*@c(9$0FSa9O^(LDZETFmig<9eUY2^RJMp&F)A|cL)Y}aM@Q)%opOybx9Fu8mRUa#WsL6Xt~uQinIM|uQS^<TI)~O^8HdBl)!}SzHhF{MR(H%>DU{I3d)9}-ZN?Mv^3S2H|MVWOxN8U`b{>~DA1v`p4yEp(y$|pu#L8b!e39dIdX48z!%!P0jgDLgYE6$*@(tX-LDa6qx0LFdQhIv+dE2$LP;7^V_(FiVaNVn_3M-ld*|{J$f5e<S5Gd+2RPy>M?;C3s6%DuQ)<Zrf(1TxkjdyzdGJ~$wKugP;i%=MY@C$!SfzrFPRP@u@0qbj-Y|QGY=#YF)bM0TsPrh%QHb^6Fm;@0N-E>4fdvJf6IzNL&xx8L*#<<9CmI>fJh<{J_R1n{n%s{0OX>sid9o=nD9EB!X&f36m7V|wqc%b%^{Xm<$SneS{Y0)-uuVvKi#c$zU-7j!Jx7tzNhfhljoU652V1`KKH_RuM3glqbS|=$O6AQwNtq30^2*9~#$DDhzr*_j0RaY@ncT#dXA!TcK<$}58I(`MBY}OyX!EWI^8j$nmWJHV{D6Z9)|Q^wn9lx;>6re1`0#2~oKpj=C=DBy)BuoENBOKTu%nHM$fEkxmC^vb!L4bv1{&LT#tV>oKNRE<G-y{?5GklU6|(urJAIzxsU~Xx>c;%++6zC}1e9Lv;5CVqEU-mNATP^)s2J!=J6JQQbm04tjDF3BZ~}x>No6eUlKzV%myW3gp3MqAVipL--iQJcF4)-9c)UCq?~I)+VrhceK&5&Qbel@hc|Im*1t>RlUz^5l!{9xTB0;<cxa*(_o(*sL&8u|EqZw(n#6>;xMCor<FD4Z5?~FtsFo(|>jE9%q5#{q`5jJe#ua%21ChCYZ5F3c&8VenUtX8FQ><O2xCVsTw`vfk%k3O-3xiuOGtjWX`m_$mHbdt*OrZii6aYuj!X?Lv3jwWeQMbby06eF&)t|Y_AeTVr$kHkg^6f1!|T%pY}s8e9xq7|!y#!W~*UyYYB@&%|I<EMsv@kQXu2Ps{%eltNzW~}3Oe6TKhT2j6URq3lgJFPy&kJObZw(8rhGk?4)J2Tn9jnG4;jSwPTK|}CvUC!yNV?{_w<9(qA6dHt^9bFhEmTEEu)zYjKOtP{Yq$aKrx-!k;#Cs7Wm-w4=4>_H0%G9xCTos3Xl^P~}$#jth7_DIoSxuDG8YO*EG&T2h4`#D;z=nb!ayw-kl((Cft_P|lHR>!mcHw`)sMt7G(j%-DgqXR{<`s~qXA_y&s<8;|7%)g7`PE9C58OrAyFtH{-(PFr54->&aq<~Fk2fSlgP_|{Lz@!Mc^~9y+k7?%K#yMp6M*l6q`EHBH9BF-i^rS#O(RQcEB=tbgXry+WGDHSbwXTxP__<BvgPp&fhbL_{JP8;+&cV;;-wnQ>|-@v&R~v8=pz5^ms%NemLwUP9q1rLnj7UFaIWY7W)HnZ!d7O{!kugdR}52)=_HRFl0z|;d0cnoD4>a1acfp4<}2`#Nl{g*p>(5K4@8Mqa?MlIm}nhyqYx35o(B3HaZ=;-(PqCcK7acIH&aqHEDjr$1niwcVQa|rR=5d2{yR_~wKd+0%1Az9p<1CI>`7q~=@yap?Cg7Km?rJe%Ahr^pI_T}h0q6(WvOigQeD}V3$TMjVPq+f%=++@LY?k$Jad6{2nZdSc23?0zdS66Pp8nm7`eYH&6t4k<ji5#7*QBv$Z~2APR{cDE9{ArU*)Uc$ngL&<=@Y~K0>FK+)KfaOn3ZE>YQ*J@9&6&vT{#caU4d1o7=B&jlHk7hzr3QNx*l=HswcA#HF`jy7s<3Aj9-++0deuifUKuyA^i{;?lm(E2?n^aU6-2hj6mBW6ft*W|j9x-dOSm;T?>LBq%e3`542%n3(Pf*03BNGx;8wM9hnuAa<)S7}yLI8$Za84BOGuvBr$61T)%_3UjNCat9hDG71?-u$PYb7G;V)Ka-<nlZ0DZyJDCsgWC(<8uf^X5JFTBn#=0jje+$y1+bo+Aq&#~^XjnfOI$mpW8EXOgpbT2J#rq~Z$)`~K|tUKb^J(vypIWj^}f>w0Rokd{Nv&W{y*i^>9JX?XZe=l%zKAg`bJ)LKBt#cGKdzD+<P6R(&Kt@g-$xtLDqu-;6Q5}{W|E5JSB!jwu8&ayANZ%?6^V2zTxWiJaWUR=aImcJeTtJ)Jucj2u?Y+KD4bOJ6;1pC0qT;4q*M;&WZbdq)&?~*UmQoY_cDb<iqTE#G(PAu&c#Gp3i`_(wf`~+?hu#evW`nn4S26bzo=W!jI(wrekb~Y@iV6?eN`eB2$#utG&4=Kh4>fIwgFUKX_y;Troi?DAnyZ9Ljb7;!9y;56&HNQ5_0+uDuh>C;^7~f_KdPK`a=v0P!9D*DtcIX?!+z2bQR#qQA=TZUFa+%$&q~FD2ijDvT?XuFLT>9RW6jrV!Ldc~l<q2;IRSIm%q;BbjLQpy2f1)fXKtyvBJvD4UPejKMO#mv%5ye885A2s-4ihPrz&;yL614*5ua<lkMa{Fh{N_LovQ4nx(!Nacmipe7PaR9n&{DN9frRZ+87W*Z;RhSw9pgZP5Ungg<A$V33ru*FhrxrJpHI&G%Bj0vVYfm`t{!-|QRDRt)8A{%G8DwwiBUm@CS4U+i7LJ1l3%8tF&?6=ITBcG!1H!66ghcbeml{%@AcG6$7UGQtvfp0v}akXdKW^6BvHp{YMKQgfas=zJymk{^;OOq%6Wae^M6eWO+H8F)95%*i*vg*OriNG3Fo&Zn7kueeYNM{w+j#<pjP?DDz9WK?p2DSz)2J~l(8kJS|c)*~vWpIOXmI<?SP1>zC+WEn^+WH#VL_EXoiu&>d&aPUYy>_7HYs=F2EiMLW(T0Hlf%fmh#Q&QuWB#HoxvB5|>^H)tJXL63O(y;nb1Ip{)3eN}>%yFx3Ug|2&i0BJ{D!%sb0TFhh`v9OG7`a`7Y!AE_9M)DU~W0@3HnDefBtM|Q$GiXdF*Z8hib~(m#Ggv;q5GMPh3RyT~=4u0E?yb)O|cz49Jj<>mil(u<1yl*cuCT%g_Nl&?pMn+R(1Kp`gLgu-e_=JLqBhcg&*I<=Jj`a0}2d)Q~l<a<{+zx^;4&14|l>f*d$oCqiJ&s@I8_nDgp2)&t!6JZ6ifvZ|T}OQo+Cg^|-5c7n0IT*ID~N2W^l8Y7ywiw12c%)>K>)Uegoc&2M0jy+(@D1<gd@D^MF*HTmM5|lxFYx(V(yY#9tUTr1eZ#jeOCl}T5c~{gw`+i+2Vcw+@FSV#_XU!?9et9=vLe`dYSoEY!s1Wv~Y)VfGZJ_^x;n1)FLnFO`9Nw5Q44_{0Un@v&*_N^fMKFNC!u;lN7%ec^@(*`aS6Wo^Im5cj=RXqlm`ZaBJf1)L5ys|P2T#odl3mE<Dq(5j>1Rzmoi*_o9Bkm_hvpLIk0zpB!v3@juzhiB?>Kn7z%D5V+<TV?>>lkI=<mt4>wuaWQmJU`QHgaiW=YUW4qHeB_Wi5h_^>sLG3!gwRb%F9k2P!$7ki&j)y#J^ju|#cSZJc(2Un&YsjfM4xUFGqh~l)%qmoA*R*Np(7C>5%sGrZgJm>Ogbu~}Uj=AADwMfm!a?M~Zo20gO51wQBM}7dOV49ERW<HRMW!u`a&2DBHxiaC__-an3txLCT2I6eXQAM_z&ArXD)*h5Gd**?O|H?OIu4)D*qs7XPjhlzRXtegIu+R2=(<V8aSe!%qnI#*iRN0yOv2b5TNcIf-GK<p(Rt9T^n~@GcyGJn?H7o5#d2&aT>;ZGQEryNf-+AsjhrFBOTlRaQYhC>3KJg0Gl$x#3(<yb*n)u9oVqkYZX49<d*#<b9Sm}UT0Hh}Fs>V&zD=)o<OHa3hq+h<lAFclQdj<^-Ww<7?l+NPjis^xqX6M9)<!RZiFhCt6)|y5nwZt)$F%o@xYg?t|?_tb$tR>7QTeE*UbYLTPMd<}KxaJ8)DG=qkp~14pi#^J))(V?=Oam3GDzV3H9&YXENoKpYZ?Y4K4AJoazB*O-fWfmo5+$LorV3dDV09Vsc~~v8g%(4*M+$RnZ17HVhUy)DBy|XKhR)Xa<%D65wl~X!p%bvqQTO9Y&Tvc^8vd@Ls7L_E|9RR_)~#fP5*pw6RBLD<)J*P0r47rppAv@5b1E-~mbL8s^qBT}0CzmzJ(V!TiyNlevX`Ep&11<HcIeyDg&{ZeSd&JcGAxh0&c~t~`RGJ5PLx0)PPbGclUY}?g;I|Qg2_?I3KNR)r)6mSQxJ$DK#tW#XyK>xnODKRc7h)fXO6d?9n`B6e3eI%Q#(iZ?dj~!w)?rMJ)74xz(iN)b>sT>xkPwpFsKXjT8Z!+<)UT)r%Cg=K23)c2Gz1l%S;vhMUYYG%rDG{qduaG87!$+<+%N^Vq-M4*`7{~3-qGAxGJ6q{#Lb<J$MvJ1k$HisqF+;;ldJ*HY^rF7|%~xfMlxVf&ebp!L>y|U>6oaYuKoLW2>Q&>gp_TJYI%GokF99#&e%)DRi%Ff`Z!HH@Q)gpgygh+9;hi%F5UKXGB%easZ7ouc6gmxjow}55XFN;REDjHlAH-wpWJPUb$cHmB_9(?nCxUX6vt))m+&nub0(WywBrTEC@z=v?hk1>@exC+L4y+hQ*G^Bi^|yH8pEMyktsXYpjl*pWY=?0)z${7Kx}N=Z8vcsJOtP=98>1+7#jdnu~?DI2GE4$Q{;EtkQ9~o-VgBf7S9Q$g*&wZwaDUaeSJw`bIPq0X8x#GBLPdwh0q3<QI?9nT?<Ujn(^DmccB`4fDL6^}FLa4s+vjq3_~z?y$pu{5lu%+f}{AGX>qtmZUghhg+eZh)(2NE?U;SC5(i!O`aF2>Z57d(SQToSJVE$pd?pI#}d>+T<T2n=0Fi5AQ6el6{|$smg06QBVi(dPAETZgwK$dEWKw%XJlolVX_Hy)SoQ88U)N(p`-DFbD4%riX-C9`yz?epdP}=nqBNDCI-tiG~xtm&0sZL>x8mkdNh3j=MZ(r3bX6k#gM<dUhyPs{Y(ceWmSpumEY_r6soIYe?xwMb7O|=o>0ug3m#hbW*$&rN%z`;gU$Y@u>t_TijfCByy@JusVa)9xtEwsv2HSLa{WEsR{W+SF3RnB6qCPh=6cuHX6A+~?oxXe19Zz6fRc#F|M#;PU{eg77#Q0V^gz@KFBUD2QZZ`niK9dVB%?5%O2C=c+kk8#as8B0JF1_WEhhPk@<d+6$!QwHgIhX8YWhyePz8^{xSX6ZyvP=7a1c(8(L(K>#1>QrEPAYjYv;Bx0~tg%8yDei|BjHAg|Eck6tid&>gFQe8Tv&UYPi!!{Vrhl(bCnQthX$G>EC{JynKgzt(kf<wLI?w)X3v577EZ|_S~*S6c#3@4+)mfgNht8v{!-(ZubgH=fU!sC!k1Kp~ZQy{9=sF+15XB>klv7`nQX4B7fJV9iKBRobUJ;mX?O$ayWrb9YPXbyyKe`W=}Pw3R&w=x?JnCSVBBeb3r7eAs3CV@J5V8owyw4vE2{IRP`sm>e)PPFzO%bw62QXx#qNjHUb;;KzQ9{r<DSLa9RmBR1c8YE|dkPGT-a{RwK*P<fYT<VB%lkw=xz^^jpKsZ>8vG%L8V!n6`49#gpr5L2+;v6vwk!oF5y$CBAMJyV)#8L|l&%F$4c|*Y#?v(C2huyWf4S0}C(6GqcH%X1+x1b+)`sc6b8gVob(6i{++eG5C{&kbm?A8R^EZ!{uu5(4EgiwGRs<gQ!~K+Ub}xX9lUpG=O1r>CCXdj^DUur=cop-f0tO3kwSd`NdD!tubpkARN_qZ3#eq6oe5zNpVPs0lSC$ffW$jY8WsL*@TLvW3a_SiscEQ?Zi_~r(3Kt-jf}#2kc40iUW^)ENy9dG$I8J&=*6O=7`|nT2u3<;&{r_>dW`^ve%4@ikBTe+{=zeT=T4#9pplM0x#P#lH{PQ7qfDiW~Xc1pssn*(cV4lXqV*n+H}Hkwy7EOb?!E&w)b~=Wvnhb+9GYrmbCB>Pq=S-+$!={rj>lf>Bg@0o*s9x$Z=K8zrA)ZcEDR8;kHZHTQ4{cww@Y2l-ib5^C=zh+E!IIRA0Z$s~Ny5_&E9o-IE2Y75Oi(6s(?2>38{Jvr((XLHjWraEFBEbJZ$#^n%&LeDHW_B{BRXyxlL{aQ{MQhUvheT**K>mDW1Ev4Fz!n0NIwm!-p~e&vbG>t?xqrvT4OXd-%ZU^-Q?>XQPO{nYG)O-$tlTRJ#r|D*#m_=#?g=;X-_U%$W&7kA+2B|Pc=(`Oq6yK9Yt;4%+<^SnhcKUmlF?6u=IjeKqcUjlEEezCOPp@A@=MNlny)(zOGmoL8$8ZaOAK9hNAY6x`mE<SuD0D72xj6p4YdG(+-CzLKhAed_rTgTWit*leA>(ABX@j`Mje{Zns5kFcTaTqU>{{;<3V1FRKHxd3F$7VltLIwe=kZ4p-Ai<72N$CC98R*&H=-EigR>S;3v<0G9y9wxlY)shOs#JHp;P`jnr!6p$*^3Nl+3(pBsh+Q*7rMUmw!+<KAJx1Y&<F}hxsdmO^-RdSX3J_5)f0@(q7y1V>KIShrS%)4*)JeU^+L?MQO<knsmpUF)wWONLvGkBJ~pI{4Z&(WW6Wz*10zN8sBb>@>6)r|W!mZNp95l7C@+EiJ9~Tj7F_UPXEw_Dizkov6-D3P`ixWQc${gJPh#ap+*TSLb?IT&Ug+D>vh36@P#HnGHCvWbh0+W;`|Qa4?A<t$)0Kz$WlX<E9U`$hTLa<QVNTTUVQh>}i__{}tc|mr)?SR7*~~<jaWKZ;Jk!6qYWou<GUk!pGgy*YmFx$#+8#@_{goL8?ZsnyjE<q3_T}yC3+~uRn^|r_z4>95TX<!`9l3@26}g4OyxKl1wVyOToL9rr1ya9HTM+vjug(#Vg_Y}7l_{~{qywSc!u68M)jWgc-a2=hZMd)+lyH~=yqBgLHczA)7J;1o^>GouS<YdwdCHu_R3A~aHsv1}wk?wn!QZwvoplBa&*lKBFd?7TJXKpQ;w~+bdX|*vOHx9Q$yz8&((93)Y<55M>s|z+pF0IH{9n}@Vqt+;Ft|ech;W4`3KkOtinA=58p3;F6;QBf)x-ahunPXYunNNxtI*7_3Y+J#3VxC5ZH$^_W%OpajxHYu8iIOo>FXk!^S}ZQ@(kt_?=^piYV|OwLe<{vBNA7X(-9YPy^_P_mE2C0^1wRps)hvcIpj!S<^+Vm2rl@3o|}nW1F6-K7|t(56ri7)si0tO+&ij*usOHt>5+fMDuNxr+l{8)=I=?*0b;0uO=3o}p>9}`6p*D6#hm}Yy*G)qrAxDeVmGm)IdPhM?z!jQ_x_iE{+an_Q(09>I)TK3$IvjbaDf0z7QzS&wu}vy0a>`@DjAC!AO@JmE-^qLVFbp42^O6&7zRvXijXA`LN$O1F!2DxUTb|jB2IVjxv#CPx_`a887EGhXm;%8Yu2}xNF;(WQ8Xr=L*pdOenr)hNS?1Ynk~_4<wb!U??KP&4LKkS6o>*@*523$P<rPr>qS?G$FNn&M=-GxfP#l8a+o@i;r-6Ii{Aly`3|#B18t;(*{8Ph$`3OEEu8qtpXMNVf4mfZ$yVHRwV0QlZwxY-bDA#gm@ZAvPnRxBy6J4XG+juS){mr1;l5fG#<T4~%{$?;J$NR?M4;toH3{24QvC%t{ID97ruYIq9b#o<B1JL!Ejt3qDffHP%|a+HPihZh+uT)(@$E=lj_zNh?lO`~E-zDC+K-|x#Gb~3oh-^V#^n4Z^^$T|MYjspxweuRjvxtUg{A*q-m?n~7kY1nYsLY%QZk^%r2|F2zTyi>Lx~Sk2XMH<bli)pkhZwnSJBwa3w;-lOgjnbq7UTmp0<_s3r>+p``ogspDz#uCw~^}LY|Yq$3-Dk>4x0zXfVtv`(-siLd_)|PLfC?cwbdraEm)sS@ZN>Bo81?@>UP(Y)?gA7jx_5_;=7vVL-Y`^u?<K#S)5u9-l1`41LhW&hLd5C$2lpe;&zVz?I?)aSd&3bs%w!Eh|`M=$;qiBjfDxT4M6cr;Hn?bQD6{9U?%9$W)>ezaY-2tF(3$x-{Lhcv-~)1X2bp>{t!sM68zdZK4>9lqK?cHpV7wGHU~3aKPGevXi^#>(2wgA6J2&c?>=}Z1f)@D&VJd*E>W7R+pjzZ0F_}hVLbz_;^$x66qN~9Sk4N@#lr%$N%m6z;CvO<Ex6VnSosCM=^A`;ET2}pu&U3g(3+>FxFBfiW5g6cdJuOMG9K2zABb{-730^ziSrtBl;^A*H%1>{(;GxXfP3~W06qY>F0>zIus}QY|>+fb+eeH8`T~~wFNpWP8=dm<>V+T7j36R!dgC*Xxf6Ekg}q&FoQA@Zb68VD$-j}*O}6^Gihn-X{P9B2b}yZ(ctQqf4kA%SG1Fo?FzRl-xHmr?o29eI$M}sx5QmrkcUfc$Kbs4R+318s5*nmY#UYe!3mud;{iHW1fD8NoZpYnTomW^^Gb0>O#KU^iW85`>=`k3;W^~5?tbMe<|QVUx-qe|4QW}`3ri`X@HDu34J9G4MfR?#XOxoxu^41=f?L<*505w?c^;Fu#W$HPV+u32N-wn|Cnfxjq;wIPBbgr}dqD1wH&_f7K@^grnIu~zV^uiJ71~IaxF89XZzkd7$+AZt9MUANZURUmTY$HnxGG~a9)|o0QbDTq1qZhuI##mcY#xa;%rO-+MwSm_-Y7Ilzs2ZjY4=4wTKeZEI=*}4<BsU~q>P6w-m7^35QnW9FJWbres56dUfp#VrjZueS5(Mp??K`jIZDZ_NB&*szjUGHcw60wGTm)s$ZO(iB?xi#-E5%TFb|6C4vt^c4q2!h4`s@I^^FSDRv=$r`nt0L8K|4#P1U{n76oNJQT#$Uv}5OsAWqL~Nk=Yp4img61lE{39$6|qOUiO5-pY`9sJ>a`?lsz(t*;(J;m#y{LHg%)K~BVfp!&Dr^RIslyJItu+R&H3`3!%P^dQ{;bp@Zz_3j3|Jh13U$hO*7cj9&6Ep(NCb8k~YHspqTtktWEbQQH}BMpAWqzLL7Ovr5|_Wx{<$6>_+;sD2+7s73SJMY)|Z_(HD!n?nNT3a9NTK%qCMAd2f4UgP!p_eBF5qVC4$qIEPCpA1&TUTvYW}I!srHBaI&#I&TTdub0c>w3r+9tNZ5k|C=lxOkY<Fmld;+J&q=)n8Kz~L$!fJK{gV9`Uw1v=8_OzZrD``5K-;F{SM`5sXUJ)0a3h{B*W9flUeW#{AH+J@}&H)NU{82=mC<bS(&e@6pdGOTPq_p;ol^4byyaOioBxjgv3JJGIE93#OfteFstU><>!7?ItG@DVD=6c9(~f1VWYTF+TB<$n>R0Cc<Q6SDx5@xthb<lY3Z82%IrZg`M}kNMVtV=2#cdp7b44l+3+@ua~?_89LlLd#S2GGwsMOGBT)0Xm?aK=zb4I0hOZkOp>OHAjfFMl*}07&L7~Do-3SDjSITp&F@Pb2SM-i6n5UF(K)_@K&UXz@VX<n*D>kkkcuM(pO-9hZqmlcqz`-2O;D@{rOfvR9aSRX3_J>-_Q~v{i>DsgK|iU=N^J8Fb4|jF@4D>hg<sVi~R0tEJ}@!Z+pLvrcv6XW$=tkE_!(;`3dP0jpY-zZuNbE0x7weuXvAQpZF63U6!Q(7O=pvODHjLN9_-)qT<^5#(v<dCDD7NURCuzjJ#V1UdJ8N|C>D8NT8d)(1HQoYwD!FWe6cR@Y{eV%}b+(I0+G<Oq7CfYSPshhhX?%Qb9)_<EKCvoU7-*0%7p8QPTee$l&Ud{xB=)e;0&7Dd}&HO8U<r46ceLJQraQ4+9CSSs<ags-B<3#h<ry;jeytsKLjrVR#m*;GlrP7f1mXLIMI<wD7i6Ed0V#6$`^0G_bK4wv{X7Yqe9k!g4BCAjj_^Ea1i@<_}>3!Act5j#Ua3Jif8eF}KVvFT?dkl)xuLRd;_9VfC#`Z+KtqCXt-KV<>8?bq%6nG40^OGQMtt193-!N-3M%&=>MZnT8eo5cqsSEQ6Mul<`Q8EJN?rwFH*HKZTH!)S)8FvPC#de{d5_Y8A9T3uwSb3IgD6VC?(Xd97?BQNU1rgEAT9VTpR?*{Id(zjBb)!fh-FO^MQfmx7tn;plfmN2RENlMcb3c~7LSPLpWVQK)v2Ehyv*T+fd!71df+oZ~98`4e<YrE1^*;p*Ra{g1ihp2fs#c!dvi=!e|*e(c&;)o_o(cy~{3A8zy{7)GTpEs=-9nw*`+j?v3j!asRQU&2gNjwCnRw;j|PLGr<oBU5oe$^;Dn%x6?!7!Tc(164%w4-Zw(%pqP#FOE>eQ0NpxP?#A-|4lj5ymYIQ{@U+p<;4{Zx`q)M@nzrX9w;nFm)w!vD$>vWf<6yykOw@kzcDF=SoEh}<(>a~^;z=D!v8<!s}}q}d{z4HkGQMB^}|!^|4_WtN7jGj3Slu1tTL+2NcG{sU8RN?73Qp}v96w%S{}jwV7nLozoO;mhpUkPL7<B`^7)__TT=M|_AlqOJ>!<Phi<7mUjI1)>IwOOl{ea&#K|TY^50)wfV+5d<*&_VK^Okds(<Yu=pVMsOfv3|huts(F;|JCMp^or5q8J8AJS{=R{3Y0MblcsFj8R27S)uxNdImTNUlm?E^FlTL#(2|S%*B?A|6DliPRuUmYZ}(Ac-rgCK&(t3a*{!@m-5yp-^%#z&B#g*&N)%F${Ss$!7}yDpm4I9EiWG9&tJmXj)ggmA-e#=MM?LkdQq_ZEn5StzWJEHmV3$qGHk^Wq2=vP%(=B-BDeSK|(K=hi<7iC^edfD}(F^ax*TdaaM@)DSbt(f|uwdTeUk-K|^q~#+g$zxf+BbT`>N5rhwr_VTD8(IM4ZO_}bLns$#7$Jd-hakRV_--WPCk9$`#aOy0Domw%x8=YxOXzfQsFkk^g0u5yoYdFKs)M0x7qG2GxDq|0ye8$iFu+wO295G|5U$PK2geS=QMudu8vxJMsFlJo%N01l9ZIo@rPcgBHxcnqKg57HaK?cuO|%t9ap?tu(igOor`;|aIjFx^iEro3!*4G+G-6K_DmtgqmzWXpTUJIt#w*3^dWM4KW{9}jA?7SAZLJ^!n=7Oe9!R1I(P%6VoX=s=+xhXftKb|YEjD(s7DWvaSG5vyFdRie#N6b=wE+e(xYQ$hZir%QYr5M%7AZO~D;CA6qzghmp1$+D5uE?7)7Y2qL|0E1Qq-KrN1Al2Rwkm^ld5-iHml6g3+MxX?%-*U{qB}OOc*!4t<fuy!)_>LL5fj>{aupH4?08Y@OX#gstauC{~_v=I!UIqr3Ewq5~ATlh~0SxY*FtZ!=W2$Vt{zpF%#j76cT8h^v$Zn0Jx`;}=&O29d9R>?(BEFQ5$<Mv1A%RvyfRpTJOOPjnOf11gOt&a#+ET;p<_=N&FgDu;jAZq$khuP1zs1<8{YbqgTGu=SK=RcsJ*vdS8<&kaibR5g7<|ENmX}sw^gf_<UHC1h@x*y7{v)5MOPvr=Tdz7po;<KWd0%LkkRT$V@Q#hacwr=PG)iqVSbYTaW|_Y8bSJuRU{E9X#~fk+T{G*%?nQM3)Xj!PhKa`SYUi4!YHzDw&$C`DQ-b_i=@pB-c%zst8?@9mTi<Zq;x<U@G%vCggnN(yCooT?MYF$UxcDB%8HlKEVZE#2V13-Wjm&!lDS?HBpg@C;fzES_bi8@;Qd*|nlbBT6Fn(E+>^Hw5673;2OrQeP=b(5Behs{vx&fjqFC*Yut~I+^;;^TRKt8!dOdUgyo)G~R_9cRiBB$F(D1zriOk0C)MeT)2tBLSs7j#lNHK$WSbRe!O(QMh-O2)rKjcLUyKcTy1Rxmrtmz}5nwh|!|W66Z%hK{`0HC0_Zau?TdtFZBFA4TzmuFCr<o}8C)5Fw+aPblGbg^a^Y1EnGG05T{rpfF*G;w(Q5G9N1#QcX0RpadKQ-8j}mp)xupQKWcnBy3L=2USP#b0PX}h_h&zdV?kPM?cm(S<YU_qP&gv@Kpp3V|x$hUV@3woKv28wCzoQh7I4S;VC_xkGF=W$aE*7@+CDh@)IR8Z?L6h6a+#WOd$hd0CbkMK;?rHjELc2*7&8PjM>+R88eX~&ogGPO2(`&8ME|(GG_T@cg&cjS;j0WW5yXzNwc2bMySr@&C;d38Iv<V&G&qoI%}w!<*rPfNrw4+_N+U~o;ge@7_pp?H;?AfS`mqa(=-}vCCG5$#)2rMX8AOxcbHOZi_?3URdWj9Cb}<J^`c4<EVmX*Zfyuu(}FNMtlI@cJx*vWX3*n7hK=uq%P3l@xW`Df=_>S!E@#^yLDtZFe#?T8yu_@za47SZj~=QZYpMl9Eh0OqekA_}w>Q6_Tku2CV&?5N?B-w0vv69Atw;xv#gdD|yM8hq$GYr;T-=~sTyDLZXAU|!l5+i+l=FOLr+K-e>GMgmbN}$wI(=1GD+0pXymLw@VWsV}F;=Zb19Z#zl%k~(7<tTbuXpVA-0lftXLt%hcs%76zFX@}bPsbJWuNv0R5Tj|P&e$h`+SLAsWbEh?4XSSJBthdm1r*RE%4Q5Q>r6#SN2(Vh@sYmm!L5Ij^a$5Zvr7Gpzx_Uk8dqXp061H^qi=nJxA04cv^_VEwSwc&EfABc5WjyXN^4&f#Zsk){cVB6@hZFY7@<@lnl-$tX%7L81Zy8jDS;vjf`e%8|oIjk)?q|4U#ktg4fL`9U8}orW*v)L%}A}bv%p;D*z`TiV0wy*KL@laz4)z4Gcxpro{xDSla}ighaJw3N{;wL|@dY=|VJo!})CaJv3au^lw9kkW?Ub9Z~jTW9W#gLqJ|uV+HA)`p-SfyD(8iCM&W@T=#qlZCUE|ZBV_2OQ8KQL01%MpcA84!6TC=5U5U;C-a*;nVaF2r-&`X3Y3hfZX`8#1MJr1h^;|HV5_~H*NBq?pCp~E+}&%xOxV_Hza(QFe2K<&1JoCxL$bjzV3Sjmq``EtU4qQR%4=>VNHQ5xkp_J33@e%dL;d-yTI0X<Jp1f6yO`9&NN(L1<IJ0M<z%0Y(r1XOo=BfTZydl;q=>phn>kw+i*qW0qv%<-7upM=XZ4}n*&@&VFr*lvn#rB@mFPVd$y1vhc0%tC6$2Yuc+l*g(%K6una9FubB$==;`2(J{X3sc*^d6+a8B8-Yc9J)dYKJke(UCWns(WS-?C55)$Bag?DEUSyEVcUcbB&l4ezGfG|ZySUvdL77p?ch$xFT+eV|UYo>m7z(r`dJ@>47uL-u_l8m~Wv3J6z{A-gKA7<?GWV%M3*IDoP>b0DiYEbziH54XS~03|C9w+966f=nZd64ZEyP}SWrP8wR9oO9C-jr*4KU&acMYLfkP3F7jsyb8|XzltUjERujYm_8sgOswFI%sewjOsfSn1_Mpmc2Lo`YQ1@qC_X&~fLfzT+2-?Xj8H`<U&Mkm-d2pv0E81Lin`Q;>@4WriYR<VUU6+Rl9uO%)KrpOz{0emRjuyN8V-zx|FHTuFzQd^Mrlh}d1AN-*?$DdwlQvNw)6vyF)epH2C_V`W*fzdS`<NV6{pFMyA>ds51qf=_ys8C82o@k#_RT2k6E!}fh8#?DOuJtdel1x$@5pW{E13=Qm_UxKGZY_tbu-{WzYqw9t(m-B8K2v)tHC5{4%rUt?<!G-bd-*%Glr|)0)|~2SXFFlCd^aoO2dfiY%!i4uH`wRvVIbsA7;G*R`rG280B3;73&I(@CPa+hF7)E6P%jL7~DDTLPyJQ}KGkEb`}yO}{<Q5s_IeR_!sz6$C=m%}^tY=BTG%Qqw`iPyXZUCRip+-qQv;BfwiC)b-35;`H02`yN<D{ee|<J{*<CaMYD^FE6+2ecLi5;!X4j&w@rqF#x?&9CpXhY#7i@_Vi}GUPxYSv%%C?Td);SycL7TD?za0RJ`C+ygi(Xw{!SUZ%eK_sYi=gazE92`<IkI!;BDYI!LqW;DJ8M0<M&GkR4gZfS##idL<vpMde!a7kjF$SJLJ-W;U#Hl?9XI&T5K-rnRj}cIO#5(aG%r8geU@Q&m#$q61#A>3QJgOSII`i!2{Xs7=;S7=q@=fp0`SOan4n#PK_dS>M_$WB*#J*><F0Sb8a}1N-G`MKFMJNl_&|yoW@7hsa1hL)MXZ(mTyr2&pF}oINFf72nW+XAz$x*8}FFj`>aMRal)hk#L@ij#nVii7XVS^1RA|)ml5az6D#rsmZG}*McX!frfL?vJ$L;taz%i!Q>T;B8;Q-U%J*cy-@`dz0<pFfx$DBQ`!u!Aq`1hhif^Uu~7RZSY6{swj4Y_gvwZZHTtD>3%j>v5T%p*$1p#=Q`S<!y(9}Eqi$9p*3vaiqWp6=`9do@2CGad{)(d?OUlBQ$ed0^TRpwXN>qa)F~t5l(Rp_AkXeEsQRx_?{7?07-9vW2dBde7t(HVIQ?7O=;s*rJwwDLa<K>;I5Ny0Cju(L-e)Z?7KNR9B#4g0Ik#j)S|BL*QS^xYh?}d5H-x8`<<-Z}nK|q~$CBzZ}c=!~JaySV9WOrJqft^VB6?5<yqES|e=ikWkBqI~m>T-v%#1s+b-*g+h@oa`3Xo=0}Z+V}w7zGSUu5ixa@2os2S~eONGK9Q760ADnk6J}DcY1KMc$LEG8N}2HTW^#!Yypee#ZuZrbRYK{wyex7DmSajNhVmEwnJ{NBtB{ZPVSrvIcxsSH!$3iwt%H7fKugqyDJ}m{Woi-=c8!bpULIOgIQD?C4t^m*naW3$vomeRs9F9e*?#5*hz08+c)+y@fufE{lGV~XF&2bHfmZhu-f--cnHAJf_2C5SJjHBAd~<ixE&BCXbePGGp@Ws(h=eCZ{}Bl^34Fs+zl2+nC|Fmf$=qeKU7;w+XAk%VzwmP-wjXx;6a956Ti{$C#y|$$HW5RyrD+^T9`wOF2`7PQf=Z6>4<h`uxEz>26!2wxY5}D@y6Ccg~?8582^I7z(%s?Iis%f8%<ScC}BlLadVfAqx~-*-|gc|dw%SXFD?Ai!Y?iS^6{mG-{qtKFdzLp{5(D9+w@Ux`+YxtA`{}Jqkh7+O&{)B>9=#+`e*+(KKk*c)6N@qY#e|1?Q=i+5A-oz{gL79qOu_Obaq$zIDYG%@$q2WU9}yP=~7(%w>tNeacA|s6Z-Ri$;)Yy724qPM^HmA#<21+l#OzL?!mVG@jr=UjUg-nvJumC!K%-IOGWjMj~1urs|h54BLEc@yLBZlG=lBOp2q*>jcAn&%K!5hULn|3CGI;_jp?7ZOU#3*D$+y&o~?f>6Px`csN<dPNwd@5;#Wrp%s(FeeEi6qe>L5hvkQ&)Z2LvbIe!o(KMzkEtg?;U!G?gI%jp@*0T#?W*)~Et-jXqF4PzXbZEH0HtRG}KL^$`a^40h{^cL(j&F=rGxxBtDFQT%sJbN#`+}Pn8QR7U{?woE|RJP?FyhvWH9B<+etHR|+n7;MXBlzhlJcGRlFSi=+>g4v0`iA{=cF%>SRaY$h-=y$}(iMuKj3nlO`PT~W`L4Br{glYj&T`Iar~UPZ7N)o3Z9`!^$=Lbn`0?ZE#_8YV-=>3)m3#E#c;}}lpFP^ib4hpa<YAp%;*q;8J?iOi=jW-;ZJd64^rZ7PKWr;6di&GowMU4?e?Q-O^s!KI9`8KfW0V%<KFfx8){%68wx^w(wryuru~X@I(SGYr{*GtRy=l+URgO0N?3Tv+95?*Aw>*7YmyK9{IQ#bK;4|lm*B)uN>Z?m1FE#l5?@6<$^17Ng``EB!YtMgpey5+`(#eL2KA!yb<?lfv<oCT>ou0p@q%pB>;;^J~aa7XSA!iibtfX<vDhUToK_IE_l*}Nhg$h6u2@&p@liC@S2OOA<TeQAjIR6EJ!<<>kSbhV{D4@stiWDHFVsU3MjkQ<_HmqCxR`u_qMSdPx;-rM^9RN7UrF!LLXHC<A{4w2PW=BHq&X5g&eBZEL>f8#@TM$mp?4WfBwIC5pxhBFFT9`>Bg{%bgB3UU=8*PJPd}Sw5LD%w`!8(JaU~bKoPBI`nL)AB+c!50V_}Gh>Y-MB}U`PH;m{Mr+mH=$Wn(Zc9Uxazq1aYXLTabM~oScnl0i3Cw;Zr_IB2S&D%~9`Rv`?*S{82jYcz_#CM*RzdN=S~I8n?~}qnz_&y|riIWo`#D+KO+%8vw%VMt~;K*-Bx)5?P~h!_E&J?#OzmHR$i1$XQ7*0*uE7K!XEv*8Bn=;vQTs?rV;};lZc-YD;6e8-S!ijv5^KIBWahA58x;#Csc>`BnG#hGucpI}zk;y$6J2RgA$Oi@afDH`v~ToJs=3QWDKQzh}+Sa1VG?Zr$~Uw@rw{FVMzp@7-%I%l!`h5s=KCTaqsUUE_awmS|xZMGHaw6ThYEYNM<!Vs~;22#073Wp%#EP8|2a77)<%Y*5G3kozKuLss=h;_YWu<w$hxCWSpx60(KrP#lJn!-VfM-$@j*aVBYa`qvp-2*=iA=ahnOA#yIqxYAkmm=~^cs`w|d#7IO{{ph8|fgSwmnWrlXuPE7q*@GB;uxPM}gw)J@d=h6$G-od{eKZbUZybf9Qk#yPi5ZSZdefyOR>Pa+7lWTnrK0ZWXRj$A4Q#@%K2d~pgk}nJ;_52x!TlUdtxa=7;LkP~Wi=5MHKs01R^q&Bh%*IobsMO3CO{MEusW95B&nc|_#@P+HTk-jREQPofMaWT<j?_0lmOre1-k@jg$Sn!Ch~wyQ52O$H$Wlku7DK^;4>r3HL0=_P(?;rO_(0(?JzH(CO_Jd#$XL~WY&;~B)biSEEz7T(a%lobll0mxGwzbUEcTu&jY&bab<XrbukHQx7ct2IWh^l8Gv-*1a*!qFl@W2Dx=eaNr+1dvjYAjh)d;-+~5+vr6uJ@1(v(E17TAhB-^%11LGeocyDe5ZsDpJ<oN=YvCZw!5-v8Nvwjf@0(1j|VW4V(<C>rT;`0lVK$iwsat{S7u2n!gHg0B5-JEMbvVWb0;T{)49JVFkLSu1~5Y%oC!<DpY!41Vyt0b<CvrU^Q!jfhHA}a>>TNIU5P0MP?{5TuH=Tx+`r(%GoX=ZiE>uQ_$T2#H1s<!8JBdPPpiowl<I#wk6^kAaDK9QMipXdc$t7_*eh|-L~g15d<npqI$<7)M-KDJcWV07A>M}+zgbh1n&t9!OMA1)!jZHn`uBX6(Q#)>SKD%4`_ks4o+>qHK-sG?%miJp~3#S<+V^{`TOqX=KPUIT@q&bP4=mEPmb2SjOpX5?JAGxFYhlGWW@(ci(L77lnzS<HTkx^(LDt8BTF|I9tAl1df5)ztCT>*s$lyNz<Gc~OA4puao_de_%B2!;!Tpj{r5`gLUlc-FZmGD*z^RA(c=LYUydu8+i24+lX78H1Us>d83ZBp!LH=vYC^njssS5Lta<Kx`QuG|klnIB-voYNYucN5-A035Im+$Qcv;+h96aguA2Uw;o4;%J6x`q$|#3TEo@U^O*EksMB_Yn_`8a>vS+~ATe2n4#s6QlFyArukmvX9T3m_4jVmt+MYL0me{*?&r0&KB_i2t9vL)C)(4U+sY@q=h6sq0)#7x-oG@W`G?(8~xM5MmtImxZOwC{tGV+O@0vgAoM+A@J!(=t~lCaci068Oc>MpZl_U8l_#Sa?@i1kf@vp;7f)ndqIsYggQdde_Dfyv+mxIY|K^H81j#N(Kq6Mby?%F`d4k2a~aBzJDWf$<mxQNDf7fYah+LRI$9({@%4L+lj8NwsR6uUqxO&z(3ns*<8{R>kV4^$bdbpFv{z*Pds;<&pO$TeWZ`5&K%<g(M@)M2Tgfrc|?aD-K*2Rr|nfRpY_4#*SCBo+p-n4JD5#)|!1-8uiY|7Eus$>sC>vgnl!)g#r&eWlugr#FbW)+F{F>7`Yn!cQ@v&2THtww6(`TB<YE{@=0a!sEmPGwWI1JS%YCCLAqGcx+u*tEB%zBSclk?_e<6$v6Q1Nd9Kw!U4zE4{EXCctg>oY9Gh4f+p~VasxT{*U?2(mw;k~g{fN9n>6}tWb3v&iUf><-p3ghfkay^yH?v6-X^0jlG(=l?V#@waG(@*g%6G6JY8@)6MT+u8)qFn@8IgB4^|6jeEM!EnkP+oGui^3;6Op1Id80m*@~9ar?W7JtH4nT=Q^7eVBWi;ja4YM9phr+0?6IatESesXR)I7<IDbv-Ly|gnBAVw(zI{>919SHpHGrJNYmp8eNO?pHKw9aN$?z}+$VhOEg<q&fL0XJb^FRy4cq-^Yp{h~MBhJ`_Byy8qqPk@Q7ayK#c}~Yegtga8c^C@gkUpqCmh#|qc}d5EQSeVn7WAjBs%;f=>-kr#YIESVwfe4r!Zua}21L2x;M-_J<=8zdtV-2cwokHM^fi|}R>Y8*S0u~qI9u*%Z&?7wcy=nHTT!KGh-O&P*QT;+G_fQm)Xv%aM8gClN)f^U#561?qr$3b=gI*VG$HLGxsUM>?VZZZ_&5k{hDa@61Ys1m&+m2*Be&fLAH+3G+24|Hj>5*cpyEAemw<T|?94pve*Bi9l6;=qDip{<D3FEtUmg%s-?RK(xPsG&{uhc0lR8DbkQ+A?O6ok7$BMJOD&buOV>Bkj(5uK62?ugYBhrKW%2WEP39dJ)Z1Bqsg|Gmu(Rsq<%dh=zF!WCzX7G_1&!qTy2qQtX2%sr>2rIx!kqU!!AZ973%sb>spDd=KsIr?#P}IUI8zW5Q(jb3E$+KHylHh(ayr7d-F<N5H3vUVh(h$h}%6+W~u&WGHscP{@3o+%3*Tfu?;iUZdH(#r_)wxjvJHvzo+ClhnFtQWcvRD~$&)#b)*i671a=;hD0#_nohV3D?#*tPV<?P`4iQtu3@Fw-5sn+)?LskufgZveZ&LSO068{gx#sB#<-b2xNPai@qP6?9LGX>sxz#$j^OyIpeClS{f7r#=YPR;0N0`F}!ex+w{@pBz*#l_EYy!cQ={2$c;_(SFZ+_HTBECacCA442EGLYxVjyS|c!{vKx23@*=l)7;g=jpcv`XEaF#MsEmta8AAO_`pRy(sLAh7TAvNRPIm@T=q(*C8^G%sS5l`pH>j9)>`m{Q??YcCM~sIvGi(m?!t%PIb5DF%9Y4^ZU;S-x~R9psal_7P07Ai|$rEa%p`c6IW%VE9f16;@Pg#4<O2c*>-14i{>}2aWB18K3DE074nEy6e$u-5mURcjCtXqrmH-rUaD`JV?oE>a~@gc_TU=(<ANi>60_kG1Y^wa<vr#0SYo+CFj0;yxq~q|40v^0dK8W1jKE<c%_DzHlXlH?ZqpIv*V0lT&q>Rxzses;*?dRlpzhX_Xj{ZqGDz~XvkJX}7}1Wo{ee&wOc}rL89)V9@N+W!iWs8)0kDDG()mqilPf>pcPWILo9sKl7?379JGA%k1#+Xj9-$Wl?risfhWr7~aL;82Z2$K-@;mwJJ16F3nIpS6G3ColH~k6<GuS^;>TkIdG*AV}knUk+)H3GwSOaUSk~#8Z4*9BF`tx@4uTJFI;e-LH24TV$03)<fZkrv4Fk1^C9{(VJNQCId@13W}#Tp;|gVuP_;yBUr^egyJVrethD@q=>OU~a*)Y$`UU2`R8A4v_@D?!5~tW5}WB=Uh}*X)ipQf6H-da%eh#)}h?EF(Wjg>-TNg&9y(w5QCeiiP1@rjHn5VKTJxfOshBH^Fqp^rn0-jswz|M}#B-bddRSBuP|EBkU9sh`wE*8m+#K9m$l;A*-TEdca?c`Z;sbjug$ny3!-obnyUz;SVkQgGHiKcxiD?_Gio!oRj^VObw2~)uXb1-3OBW^PHO{`xmc}{gYPhCdwLkj_hBtGd3XT0ZYzXCd-EBYyQE`Xy$eXEpU17aZCwF^AD}6=^ZS+)EbIzmNkoJQ3v8!Tro8kkD408O!KdWsEq|&&f6IWjCtT_Sr^hgS180n;{L+d<Uh8x@k?U{jdGt)ESp0MQoV+J{$Qek<&iDb(jLm7ao}AV7Ft6*srwaayCjP#_}vQZBFE!HtMOZ<?Wt2_|J9RB;Q8SqS?c8zBj#d4t&*X_q8vK3394sUo4O0hHOucf!>9?VXt*V3B_@`1tNn(7%KAdm?RZF4MJS6HhS~}OAgR+@P@C6^Rv#0o<|TnE?d-4$UmkO!sv|*4&0K<D8JrFT@3pW}slO5USFNNPf+A}hEORhs8XC(_Onn^hRBAEw3rbSK0&!y&&sEcKFDdbS+s{tnt-T6^AXg=!Itta4f5D3os5u?YOht^mYqat#ts*5WS0H6pKU7e8hgm;%iBK*#B^W;PaL;Z24<3+Z<`Mi&EKv<!F$a1BqlMxvap)uIFkQNZ?Is$=hX;3)E${_JDi}5Z^0aVdda_6lq$t~0e*b{r5-h|U%qw|;x#y8@veCEaOf$-N=^xh^vnV6-4Xb;~CF<LyuPGaVwf@$<aSBXv9E%ifZ8|A~j^RZgxO&B<2qY2SiU032JOy}uWDCs(z-=XhB<n^&3Vs(N4h@7lI?m*y88FOdIvFDu1b{Wc9inBPn%er+aoTfhgm>pc52wZeJZDResURyYFUbJUj%kZYP)`ZZ_G%fxWq}S1N_h6vT)hfBgO9h+f5Zxuy~%-Bp9Fw8xwA|!#07#olKYLmOhZNPkCO{=0Lw?^egX2IrzOR;irDQu1L-ayXM(?}j|5s7U-*>S#b2rZypu{w`e7v=QmC`af8K#6cPq1Z3HR;c&iKqI;tln=2Vk6BA4%}EQM8a+Y<TD7oC2j7Ii6_rM}qga1mm|NavQMTW#<6>edFsUd$~-pGqOA&7#*4c>XOV}K@uci2<Sd)6UaeLV{zolKVZT@Pi*12x$k?QjDL=c0u`k_6Jc<jMV5+F1*5eZ+_%A?NP^S|Mye=MH%Lc9->)xSbxRMeWjtyPIl&<D>)M1<35iGC39B6w_MCAT`-02)JC3r5-+g`-u`XG}pL+K@XIaGI`B}ub8>f1Vx6n*F&KZ8gv5vw`3Bxb1NEqfze;1H<W(()KCBg0E)2Tx0mM{S6FY1=WBi)jgXwv#jl2D2zV{s{xgqP$>LJ-yEOsfPg?Ltpc@`SOdl&nfFM%ltqq9n~EN=~zdZ|KFHW(#>oMUW&OtC7S*H4@7f`uO%VRj7=ppR$GLv`3hRXVuI-bA~^0KwvNZxwN5wM#8XROCBW*yW@l*GZ~NO3_rEN$p8K9nBh_4p++$Bq78tA3Q)`iE_-YPz<xMy0F0pkyv7Oo^c)*t=G$11{jI`#%SWOCj00$rU0#X?P*U=A^|w%fi7US?dVc4YdkUdDEcfYJ_n+kRWx3BY)#wJa3??QmqYGvZ2*~PO$tBP&(epNR72KFhpncyz20ki;%(tfKOLhV+@vbvY$$27yp<_t*otL%vbl})O{Eh^ntOsbK7=2Ye!8rR-0l)&Ix;reOsM$ibGgkC;D6JVM2JQoy$PNmNQzb=uvXY|5JIT|{GJi#i>zXAJE0*ynj;>0ITUAn6Ru?}<B}Iftb0A~?SV?hnSV@t)Vfr6ls3c#gBwtA4UOv9G@JkE7wD1d+<O`ML3zg&xmE;SR<j*3NWc=;gurE}SpO{M0o!c49M*RV(BrOYl4VC1$QIAxTkMT%a!ZsB`$y)J_4FdSgOq0b@)p5-B_e`Xd0!ew}s_;}Aqsc1rH=eP;11dmoEMUeIIj2_ibArEf^pOXoinG5XW#Iu`peP!>BJGv23Pu85&(b4~{E6|H`SI+(gZn3u=J*J%oWTki;sJ5w{E5!<S~}6I@e)juTd(d#;RJ0)FUpr0sbXPvyS!&kVd<?q6%C&0aSBb|#1~oKyuBBD7bguq{ZMbvxsgJ2ej8*3i%0B`ZW7#^=p&CFM;~3NM%GB;4(7ecp2E5FZ}5~a^57%$9ups^)1ELEdK5Mv(+V5K&jfNg_;|!1=?=L0jQs8q?#Rm&jc$613)GOldW0$R^tY}*PZoKeVDZwWA0v(|#Chp5+27^IF{I2R-?|H2mUBi(|0w(9`2+k#rpQAs!Y8>4FCK76Svc=1-XG8o9`5m{2h4d1pV(P0J?D`;!*S^!qk}v;=8)m>xMLr)L;7d5jJsmv>`D9uI!pU@)+V~)Il=3k@^$=p@RP$^oozow0jcHnm;&<uoRV?3*CBG>%-9GX=kEX_S8&|Rlr>(!>f;=o5^x4UZGDfVm9gfXPs6Ps+;~;}&zOT_MZg*2ns|Y=rah$UAX!#)&%)w@d}OTodCRo_`sp+rfU<Ej(h1<%7jwRvy43kNz<pgPS?Eh-HN*3n05-Vxl4u;Ig_CM)0k#q831F!+j18rLOWq9?K_44t^Sj>@RSPV_^4Y*zQPYG|NG<y60i>3Q*;7=lL28|NX~ZHif~f0{j;d`9u2E361}ZgffqVnqWd<8pK(+=w750@j;xgLsq62|6^}8T!3%oXz3&mou8T+IG#|&zlibwI59zw(7kw>7mu|RDbLT%jytTp07Q&ug|TKs=^0I6M^gVbtbHs6L+Qb)u%sQ~2PA5y#VhNsmmp9B<M%ZtG5a`zOHwl<;=Z%fy#1)K^7Ck!ng!QKUlfN6-1qx@4KY12#H>W8XZjiqk2e*e1FXb_F{^Xpb!satKXt6NQ0w<@5Cy*mSymb%rEh|OIwhL*F^Re&idBA-+%a#B^I3d4B;tDK9^S-twZpUvX!ObC8r@s8&xyw@zu>wW&WAf|5+NjD%S0GJA8@}Qk$5gs1guq&eN5905p*ftU3BqhMSt2u6HLGjjZ-J-^11j}Vz)xmYI%_#;q*$oA`Z(Z|Ge1NBX4p;eb#8sZ)mW{X?Jn^#X>SJ6@$YZrRP_{Q*ja3^~W4*5DG|{ZQXm4=x6^1lc+XS}Krb7(?<fWsCNvm*E^&p)ES7zE(J?l`7At8UOp4ZXKUt)D1{=SdiGrEeP&7;n7+)jDg-hyh5jkLnxAMVL4s=gAT!;3c9qCO23kqO+jsm~q4-D0J}#F0Bk8!?mj-blb-lU%e1ST|2(R?3AL=KIy3nX93vbNs=f@CTDf*olx-wCm~nl7=__;Jhd&LJsQ{2zQfeS_jl^wnXK^PJ?=S5hf>d5+L7!;OCKPIM2)ZrBKK`iAA^r;SbDn;}up_ClGwNgm?MHP%)jnzpzn(Lp2F@kfwuC7&zLx0+BEe7VmGq;oN6Z;RcQ(ZKAe%1P3rr+e!f)w6h(_H)3HCCQlCPFp~CkV*W>41-p6B`!uu+8xZG$^|fxL_@3_y_-TM>^DzE<+?9Oe;1-JsFl_D_@RkH=?#XJ4*tpEhB$HG1yfg`Ku@0i>IdGxxO;B7q^$OdmR>AQv;mp3Ty+!dVCt5R8A@WZ8^?_>~V?dxaN%XHtNNm>yvKMv$R#>XcS5zucT{p483oquhSafb$H;RG4-uEo<HR{kfQjS-Oev9Ui)q7a4{aETGD(~pVle^L6q>=24DavJ<bliRl-A@Ml0n6Nh^`|EC#RS#~+fXXZ;!Fst*x;@R>F9>}2;S^Xop6laOg@A-)GJrm#4LX6tu#%dP&zpBL?Q_vt@U#M?&NQ9ekPCMX~x8I(b>jKLSt-)<DiOp20`D3CQQ8Uls$0X&q@q^c_M4<z<a?hbz$^!M4+X*Z+mb*^B(;CCd*fmowJVBbmt=(yBlAqxk1)jR43<)$d<AyN8PNPe`M-&XN&4AG+lO1#ddNFg8#MZ-*olwtTw3v&9jlj!E8e{%dT4F5xjJ<B^Ov;VQx6>V*SHVj;n|XmnBhQD-vj|pvF+g%4?L$F=?O@^u+8_UR@Umj)@2=WDAm<PpogjMU5ukV*xP!ClCZJ(Vf{aNKLKs%(epMLZm7|&%BB+K2PK=DXH5q%-@6%KtOB;X`kn3_zZA|8fvf)4C|6e05)KLe3su*?19S$)}WmQ`0L8FEgW}x>;df(c&b<)a|d%Ph%qg4Po#|mK=>B7$4LzbLsh`Jd-AkmLis!AOW|X&y&v*Xlr<p<LQ5);n|o3%$o;r?ud&pE17*vNu*cfB(axQ!Z%}i%y7i&9Fcldd*zZ@!hvAhGKiuz4;h^1k6();-!2d4JF#q|xYq8{}WK1Jml4D_x&t}|RHRkKvQIVx4gFj|1mGkkP1u=fOw5-@pMV-T=h%%C+M2ZTDKOvtVuGCUSCEG<^$qZuoYvqgK#_(HjN-eRc!9(Jaz=<c4X{uFl8*ybk0$4I?@lKTh2%LKq?8dr;W5~w9(x@_lM;<d&h0C!rk_bE1_|IyMqXjWQ9;i?NJ0a&`ULZ{B9~SFkC$(Z;elEOS&eZ%w+Jf3Iv92g+RAMY9EkpObt;d@xiXIpe=#`O2Ch@Q33;fCxf)P^$8yq&MT-ce83`~YT8?7uDp|iMfs7VXPsU;N~&zDxEZ8mJ>RkIdj@7NjfKp=evqY2$ppY1%b0>Rj^5(Z1vMxF=nJpXWEIqgAR>A_C5)TuCc;UnsVcP=R*TOoFy%JiGYiT@UNC5=CQEA}{!+rZ!lX0VPYRF*PLD+XWX3WlA40A4o$+7)(WrbiW(@-}6$1d*h4?)M(B)3j7m8mVdWWSkv<Jzm9P<0x0)-jIi7c<}vgwZ*Bx#hzF>yi?_Hem{G>`!6+$_Gr1mk=ywmWeDQx&1b+J<#)Toz<UkGy(*Pv2E*tsH*w7OHf+sOMa^h*Kis18eUV=P7L&NRXLqfuZNB-|NKSu*B9+kpNJ3HY_VXiuH@dGj?0;s=;j}w$haX&T=!PRhHxw&3h<qkbXj<8I40JQx%={}x7dPU8p<*^Ltya{&wPt`&ZHF9IW!^(FV~|x-?6JTSBQJ_+JktPL1I*&8<nU7VA*O-rX$igt8{L>5TX*mudG^B?)Kr78^?WgYf|h*EHY|FT@#DsgLy<E}N{T)StX!nwYs?axBt=E=5zHKQ<*#D^HfevD89x(6#Oy+}cvIP<I5A9?Snku$3^p26p~SG=sIKa)JTq#doJZMBN@#Y`Xqg^A+gYnum!J8{`*{<OHmVP85&N|ANoVtd=RI39hKX5v#v3t1_>e}hEx8E0N^k{!FdBa%a;Qe2Mx(m!Sj1e*w4u!7k%ei7x|bnM#;&?D#{u50JN}RTJeYMV8VOuu_)ngl#2lpvynEX-6X)h>9!s&1(T!y4s3LTG%Uw?OgIn+4Hq{*`h}3|Z=3=Q}9^VAyn5aOsIX_#W{FX#lGdA?xaZnGK4a{z)B0%e7pbdGPj*JT8P7z!R24H;DRVfd2EC3u3z1A(QMMq*Z<hTty$X!K|GVE*_@y(Xkmb_$3#{}YCp)zw*ez2>pSnn+(wau7jaDL~j7HVJz6#TPT>70h+BZNqQdQ=4dy~85#K`a8ZBJfwG2z)3-;OPRD^g9%RcPs*rECP=wMd07cO>WSosSf<>QU{*qb>QiMHTp-Ps*@P?W<}s0u~ncQ`FdA!txGj{Q>ww!j5vC*;Kjvi@MP8CmT#X5!bu$6oUaL|#2+;;M&jtBvhabKxKy~K=QZIgw8>Nx-jtefGr=rurBFMgXQd##59nW35Dr=cQI&B8A`zhEBbirFbjd2i!9jhFM>@?a!x4z%6tw^Y`nlrp_(WMaTHcp}@Kk+qfkgV|c_h-u1>xzqARJTenpD!x|E8%4cka0}cs5KoC5b~u&C4*9{BR=@<s32G6V>3%<<$y*y>m7AES(n--M?H7u6ds|;oYTba8e&29m)acPYc4YB7$j4YAle4u9iL9O>{6<(Zj_lowq17v~gA|-WLdnf{0PMypbEOHkz2uXkzT&f(CwKM)OKyIA8dsJc;3M*HiVle<YC?a1YtlX(+8Ea%`!!7?x#ex&4ow-(LK)6HU}FBAAhuNaQpDI-H`e<RFN75Tv^@CfG5v?^OG|WQ#A#=TRdMJ1@!|6BW4;>*)3ooU#_HXv8$lAP(^#p!8YbE9$Y*v7uUG43x-iy`q&{!FvXh#mI2#=$sPO1;ZwH&jrKKjngs6A2e2avLI^=XsJn}xB<Cq)iAi;RmLe3TikrJapG6+`9slG=O+y!&84Lb%1?2nGn5Zyg0-||MF&gz8#(gbv!|F1vOL#KF;2mQ?tP}1mYIY2DEDNb6?w!sbxJo?lQ;L`6k{q*V4#eyeVl<ZGJ54H=j0Dar|2Houdai?881KHWR0j$P4qy^x#s4Yxh6R+?pmYo8go%*1XO+`lGiaLLj`HhTV~m26OD=G2s#kF&ABZZSN+xK0XMQy=IJ9=pjhOj(=n){`C@nqLtsLNpASROZw^%5w%3i1ThMD>3kHRl8y8}KUd%0AE#}r4IZMHYJ}%}~Gi+<>R5oJ9b$S0NN85;%V=|ven<etv8$V&<R%N&(kh-!z`a{ReEAx0>k*Ym`zYV3wCD9YLMw)EOSyu>A?Hn0fDCy?<qS<mRJ7rp0gRpof0&d-90k`gYoEl_3XDCvK=pb4{OF>mM+%D3$S-1d66h@Ql!ua);w!~ZJ2m9HGX+D{lTl4JY<QY`PGXPpV94OC6pRL|sx9w^Gnh1^0ttAAYA$;LQVqC@t%&rYd=mvMS>3X06TEt$smPql+UxTS8rl94&pz$HgnsKIuJCst0%KcuHQs@eRa<X9sMuP)iS=B-@WBVuJ)<s9*P9Qrmv?;pssG5TN+zZL@Cl74c9V{r=u=xfW!yA#+l!IdzhXrXqEAS11^&P=(Qkvc|Z^wXj9zzS#n+_x4DM`{(Yn<u%$Oi^79;m_^2eFQd@2ZI5G{mkjpSLHlCl-+$5DbFmjixT+#V{CQkosMOecEp5{)dTIzva&{ar2yu0m;0;SUe0>shLH}IWIVrc{2#J@P}>TT}_JD^JD%MZ8oHrkyqYPtb2eCOk?6~mMg|Dlu5}w<yQ~d`vxk~SQ(*a1ae3;HV{KG<!NYLoCh}f?$+=#V2ka*l1VqiWPVKh9LA<!(Wb|ZZ^W&LTW-m_?F9toV2)@o`U8za%s-FyV3_EQp146;BoCFLWec^;JvJ2n(~<UCaE388@TFeD+LWGBxq(InGrYq)CPUluu}lhRcnr}EW*LpfxW;X_F+f2B0C?*}8_DBEs2kLB1EIwZ08f51`F4<$D<~9YR51wut|wAo`GwrZ{e%13L52a@DJEF9xpUvao%#N)|2lUgZm%~W&fhRWwcCNBe0z&|J1+tI+sNq=I<LrS+!n6nJtkr<iIAB8$!&;+9Ld(1blRAGQW2^U1<K^`_#Zq}cRTd9uQzC$o`==xcx5{)i1M<sz5mMgn6&jLS=OFX2>Q6onnh>iAN}TD)_&J-svN@GHPOUeR4-)`zCjM_qfEk=XEO;W5|rN!RSPsU(s@%dp<!m(9WcsvCpm;`7-hSQIRrlG1zy=im~mTpW!qT-p#iU~3S2yz)=O2$*Oo?5R2!pKG0&4^LNzETa>y<lXIhkmos?uk5JJ(%V}e-$GMGug4XY^UJk6{n6No+&(=77|#3}fQansII3h>l|I1t<uiG|v9mB=>>8)~AQ9p*^}ZwgF>cvh;eSL7M|g(O4nHZ{)~Dye+G<)TuHewJ(w=dukn20n4Z;h!<#$}Yt3F)#IsvO1lVCt)Ni5*)wQvPX2#1A2G7Hxa!+EhW@J>}AnvKeM{GF8NZb!l*2Bzr+L*<ny4zc7_g0rOUUISfy!*wMEC0K_%d<bs>?#QX~`c0DAMhZHsUOQ_;K=ZU75yD}bA%GViRI265aS;YsLXjF#PTJ}vMHSm%3825BU0cwpGzE}xU)i4TnH+!g@UABRbrCzl_w@E||Lx2BQ<*hFX;)P&^jiK5GU4z`-1vw^EKrKW(@yMZx~`}7S2H3_*%Zdg+Whg#G_hh}g25*BSG<6mkpP=D%SNg)%E80U;AtVjs!kaYCUlQh+E63VIMUVf8Ud|z4M8SVoIxl)IDmA`>%Y}NT9#SMdw)@^V%4&MTKBPmD$qfsdAC5DuzteaJ}^}bE8Ms6z1s`+Un^_&3MBzNy^euM{hpM`6CgJq__QT-OM%RXqm+Y?6FVZB>Z>fQW%)Vr<U!5o{_yDcBpX-t=N8rjR5xkw|eFd2#QYLUk6+zJa*cI@tHkw(lxhxQj9sz5hBKC$xeul_wZ{2WnrTy4@T3=9Ai86ya9-1dR5?iL|{Wu6gwVHX|arYN6yxF??A&b(e_Yu22fw>7d+h%YqCtio|qd1y=HD<2l`O%_&g=l+H_!-N58)%^O-Vg&gN+dW!n!SG~u;8!cmxw$_MAZ(}RB|F0EUZ^pgFwbkK@S&gYi6_rqa$KpPLLQ~}`%3cYx7*5Vj|vd~pJxN0cJNl8p{wSEfjXHN#>AFCo7Iv`_PgZH<+9yeA*IqCB(@AT)waZ(otIKk?i|qFSe=nlsjqj|gs93#Hku<WK>xIUD-_<{x>POPHItM|8l_YmM3vXDXsOLqAE~I>EU>5xH1|p_hlus)uHzNy4AiHQ#W4hLQvh(jpUwaJGY7qU*0s|mY~L$R3M-Qrm1tww&`ix6>_GtY)u<GMAY%Y@FIzmF2Uj|(7iITICNldb!`Uc;YnRNI2V#zv1aCxmD;st<PZ|NGPxIhM-KP?#UfLO0N3gL%=Ms&2q%^g<(uQ40^k<sn7o`SF(mSm%lMvLDlY(+}%itvX1rZ*+L;Yw`+FQDQK^3@m3@+1@ETrtX#1_5)O#T5~<3?9cs6HHi@3qAw<vpaey#&*_-Bw|ZNn|x^{%t^v4W;(f%k3M_(pEy&Ye-k;yIT?U4~RnN&02!J>e?GL?FxP>KdQVonJ~~+-{xs6H{Ok3p{^2h_-)ERgwKa~YaZWQfV&%tDCGuwSY!HFC(6m>sbpC#D!=cmJko|Q*^0k>6!wc7*UrUQ^G04Dc5x5Et+)_idT=)^0a)GS+u@?*IoSg^Bh7UTPwIiYuehXVTQv8oA%=G2zl6R{cJJx0w^9(davMn^+}`*vh+I!G<gOD2*bwp_p`)7oE0~wwFVN?{CWT%;%&$cf7oiZmwF2N(gwX?Glg8@4@<F#wh<A4{tT2t0NFASAdl+Nfix{LPde0eS2FxqYS|VU-Z_ulAqqhuEd;`_9oJR5mhw61St@XU8D-O`|e>{?WZ6*1NbsFkvO&&&cFSe2RmMGYKgfbebJ_MkV6lJ3yVhrN{(k;LB=Ivm>-XP)NOMU=nAIw9`GX-@{VIsxaN>KojiB|Lt#9*j;1`SBuhF&!n#f@kb01wy1>*cAVC&i>=OvWoz9?<6omF-aTIFVVUEmb*WGpxkcCu1xj_JW}mh2V>r03&*b785K=sI`(Dy~}rq&dB7iDoH#AV9h138R&+*6mp$X!i8J2;KDvgMwa1}{E8Y@v!nstjhGU`-I))mTS3r0N|S474)-?dAcPf*DFz)3b|MC&1QkHFR5T<!HdM?NSit4W85-qP81<rf5GMKjP>A^;ljDJ*3)2&c8U=wJk^xdks<c?}wc!d1^~?WU%}Y8!B2r2^UeD?|77-CVDi7!Fsh9(`?^p=HI9QhoCyY;*?y6SYoV88u?Y6Sw0495|azul=Zwv0;GqX{v8W<hKNn6}oZGK^&A$~uq23P5TWY%o{be~kAOViQ&Q3f)%S`*2B(M}bjD!<UGqvP{CJSgg&)%%XcreozOOAVZ~9s`*G{CKKrA^|NssoBNI5cIq{!<)siBG#4S02QsRt>A3bzf{Voo^_dq^JA)opipGgqHa1Y>LkIgUYD|xnpLHRGp(>N!gAtQ>^Npw4At2u3Z?0EGf3;Tvm;qT9m-9Ho~I3^r&rzxCQGeIl4!HT^m_L%T(XDGuftnv(tB`IoUw=U)mFtGYH56wxbTqI<lSTpt<D)kquOB{?V*YO0=;pQo2NEO`@p_2v^0hyC=1Nw4qg&jqa`E-?u~@2YY0@Y84+?tvAanl9U6kfi^hl~9HEPyBAPV;V9|O>lc(K*nM>4F5h}X&cZ_JZQ$9jrYeuCJW5V1TWcO0M=0=*gqzYO5_3C{fAXjqdod#qC9{%)>S4)fSF&Rr|z87SO7@v7GV>XPq<uL0D{yDiaxnGeYMeT$o9Iki2`Uzdp&)ly&U_KD-Gh~!Qg~7VI;DN=ecF)O!#oX`mO6nGzl3VW;hkw)qqZRQPgD`*m46tKh8k`{T+|yN-ZPnPfRJCMRO)KWjf{EE8j=19@7*Q>opL@;uZB@V)zCa?BoKHe*kk<yzzs!Ek7lHOUrvT5qO@56J9ql#3m5C7{4ueQyOu9(c`8{U=M1&cfBlv?HD4`P1N51YpPZooU+gSa%uI_lB4fh)&B-)yi--dD;u;6Q2OauCbk%)9yf^THY-U1~OOC6j4Yt?T79NEukRG0U>ezzq1`b^owv!c2uxpiKpu$T$$<FAhGHisGZ<t)70J{{hjO)Cxh_)Uuo_5b*Ro2xMi<WUi=4KZ!t=I-uYdIS20?CvfYNm(|bwZhM8Bszv0wnlIk*`|%ZAvq$Qk5I#^trklAuF)%jL}36=W%{|1S3>+QSybA<!&3TjbB74*1DE^_lV_;vzI7r@=vur%lHp@*5<xJ7UaAuZc~R~Zzi7rT@f#wOWU4O$=}B&)Rqk1+dT96g()l*3ALo|F(qn1@%+I=)!Th;XG@JJs%o@okjJ*Jqi9$(p7}L|iNG|-!$(i=0n`LR_$Azm$vOgTjo7qUNpB~BXG*P1(LjS3-GVSj<VB+0hF%E7)v<Ks|p$EyR<Pi;TxJbimPd4@l5e}WTm;){5{*1*;?RUIabce#)^t9b<TnBUy9X;;H22BNx@26@EILCqAh7%>whZhNW)5twLXE!hwFu!EA{}W|_C*=pOu<r(MR5gX;cVee9ma#&_5NQxQk{m9duHx~m>ocEwWFMHAXWT?a;G)z=4oVl6qMEIy9<9JbGusvqZvN%Gq#=kiRLZo|7_}ls#bMHO*mqg`<H?Oz0!AhNp_cUH&5#BzF{E{|)FB`M7tHUUMNkSGm#;>?En}G%UldE~8L({%H9~0_|FQG3xl8}A@0EK*jPZ&!F96Z`?sawaTOX^dYh2$xwdP?-d!(o?JC&@c<AV2CMICvc%=6`NjPV`TJO<+@lqlAQ6s~uH+3SbdvPWKtMLl2k*u^9_GKRL;Ty<fCQ8;~4eJ(aE=n0JLXdF^ckEb-&(sAV*nrY?hu2}gx)_=|xKZJZ>@iAJ{{K4mwp&}TZ&*8JJyBG;%86G^PMD30VWET^GEW?0D#HeE8p)m8}JqTo__btkXC4uu@?paGfpmH<UOIP<*mt52MCi$kWy3TKV)B+>hnSZ#%bdw@4eFJ*`mUIK)soMasKfJ2`tLjQ#qXoix*_uv>CdGzH$bOJWQv|JRYrIK_$`RC-Onb@QtzbPPXuj0)VlD&3#p;5qAP*-J4GA4q(ZQ6veh_sW<L1HWWpdN(#3UxagMiiC{523H!fk?5RN7v7<OT+0mo2gYtx-Wn<9ig%QEO9jVCoTlEFd7}MAeWeP{FT~m?|-QSdz|8qJK`IUbJ#Ppsov@X0&L#q7OA0io(S7IQ?a`&DCDapH3z~?R6*Pd5j~-EB?-yZm`Z;?u3ozjxIrFLEaCe;jG7OoY69#IhYi=^>j|OWd7IJ?(6^by$JkJPz#LiMBukzH|zm`eS*EOhu01M4GcX}_br&eV&i2SzAyM<KeG2Bf8%?Ui7Pcg{A5k|9sPEOq``P&7YZm10h$n|ryx4)Gve4C&)gF!OeFJGu*@b~x~S#^Q!EpSyifk5Cu}(}A%=JrvtboEq*BHHg%>Tal`R18DOM)zq>>b~527*iMLK$#x{dEnW!voevfwnqdnXb=X^I7{ZtAc)#+jOhK_MGwIykD$B=ZP%hQi`kGh-P$n?;K~<Y6^bqWI<t@%9K?|247o{W)y?@Jwv|^7+{MCHZ;s{rnVZ#A8(b&%5f@d^v;E|KbUxKFuNZz*rlq{-^ndYb8p=lY>WoRfu|S=$8>&U&g;XkFe*m058Vi^&+Xhh_ELgWov?9x!-;30=yo;0|M(0nR!HHeV&$Qb%vIQ{Cm~J%=7I6rf+9p`s~!cW#UUwb3y70n=ml6hp2jV(3Umc<@_*rhk~akKV57&)3t@1r>#u^PGEYRyg8xhq3Jfq)5lXheXXonA?jfW=`2@IB1}KgFS`OmPiZ~A;yIGOJww-nhUy8Xe}u6od}09oU&>~GKf`0FR0OTFF-XQ1gzms$Z#;3|iKFda3743R*;}Nb1Qq3tJxHpE>4fn#!7#i&GHs;Ji=sTxajum24V<iV`!$vm2Umn)6_hH-9t5~MG4C`q;K*4!I4gq4R@$&|MjLMWbC}#);Td31GTPN(bgx7J9#B6B^~shAMqiQJo<x7DiRdsxH0-&#l|a+p6E{M5M$g;s8ARiRXv$&8A6OScP^=c$xdii)nFmOjHAHdnZsW-HeTy3a1i}*n-)NaM3`SS7%M7`ac9jkk9uVD%_bCohsfvOcUv9cG@%an}rSNLx|Erqov7Cj3b(nl%;vUfM@$b15sBIhhUKK7eMjXOVw`a4UbC!s!Q=r2c|BnGr&hL4!F=Qj&Sx$2U9KJrD;e_ZUT64_QH&Q`3lR=7D9!{wsmh&X%$OAzW{kc34AogM3^p%Au?+Sq$@1a_T>*ybRU}W6iFzu<!)mK1H(@=@bewg9SckGXgF$e-35ZBk2cmgM>p^skg_fJ2=S=?9Q3j&xZl~LD#Luq0UxB1}=zBze{m=~09%$_1=s|5g;+3f9FLQ(5VR@)?@v97uxsS$G%yPYySm?SWT<<YyOo5+t{@ezm7N9_F)DN0xxyWU_dTVyp{J~A(A>kcoWD<v&?Pky3&!u61sJox0$m1u=C^UCNf6s_CxExGBhFB1)HgF7<e{EerliBC<u<l5?ld#QSAj*x%;c$nxZ?xoGhy;NVMcT;g!zN-dG8t=pH=0xw+DnL{}liSU?bz@0R6_zg+C&X?Ot6Rx%j@)iwBb^hwS#*ej3|1y~B{amEt!tp`2n{W+C|&9Njq#0EpSN^n@n2lq_g`TKxnha5zK?Lz;wf_4qnM~aUJa!tdB9S;nlFO55SE*XsCG<R;B}R}1y(3cKv+lELwzN#+B3^vTV3R;9m>Mj%;ho}Sp6mng%z4dj}uGnYf4fg$yHct!H$a<LP#4&PFjS5ZrqHk>&_sq`B^#!DQgc5&hF8r=aUf&b${wAh<$E>J0#A8WU5yH%XE}$g7+8Q;@*k+IsXh)9W-8(&%Ur52&>ujrV$QGj@GXYr;9?5{8nyAhmKOpjq!<-w9Ri<n4z|;myVJyCLb^<kkN!Y5#cWZy;)bn6HDRS3ToS>|Is2eOJhh|N@i#*b))8WQ~R$-5mGM#s0{L;-c%2wf*)fu<kxowapU<Hd`mT{J^0Ak$o`VPXSVHHpuJSXYLtQQsO^90nl&H7p+5(x!!9r2573`lv>+K<tpO)mqo5PPsl2r2MqL4Mk7iy1PvIA9cgySNuXbzcvt$3}UfX`Rsk$cHR#?SyLw?0=wbMRtcm7pNeFAJVyqos}zwck?{YwH!v-`Elt^qFEZ_v?SH@pNYhbt9~C6x;2?f>t2%km3W;r+1+0Hn{bN6xaRE#V5yhpH$|mO)Hc!xdbCD?Ar?^gczUH=nnt^iNcO!3{rToj_oSI?oWVNDuMg7JC*XRnQ4hX&#~*Hx^|Gt`wC%5bb(rL4O8+te_K-h&4si5bDOLLlr11=?CM(#d{c75@FC4Msl)c_@;xjUdN@fWrSzT-|APR1m>4(#sZihO_eYbR^1^{k<F?~O{MxEGNJl62?bbby48w8NxU%{@G4FvS-0OUuo(D~(%=K4f_9)a%*l%w&n0S0bk4=5;sC%?C!#XKfBS*c05ct*`biz1mQp@}Q4#KhL<J%H3~e5!0TzmtmbyI40kFMmO`b-k5L!g@5i#to3=35))bT+emIWG!Rwlwy9E;WpYNJKD8Exi<2?PGTt;ax(;RqOg6|Tff8cK0@mdI2lG3_f?uqxh9CU{Zgk<^Y9BAt>!2rSQ3dy0xO!>u4nHFi~BaPxr$5PlN($?tK@4UCduv&4fSd(K3`u_PsvCp!HXhyaWdF0P6}(M(wc%9dcese}9TM-^Zl3%PJ9SS!+W1h2%3B+1(rP(`%Yo*_d7lwz=)h3kHZnKJ|{`2vb~Ag7xf3E~+QTagd0bSnhL8b$A@Hl56B?RW+fpG=R|J2AX7|2z1OJBxB4Lv$V0|9GmzP#l&dDBZJolx`okYXm#>{-f%{kY-esnD59}3sph5=6)0yF(EkRlCWSgBW4*Ny-lyIO%X6b|3xb$1|1WQubCu@Qbd!QU*6d|U)qPHFKj3hUPLkk=j|E~OK1$9h^nuwS4UU=mFm|qoz{Ad4`hkPnpQxi9w;dck4;s#2*d87X@(RdUqTc=honh|NO`na?G$y-m)-cHql1q_OBA_u<a|Z_>pUr-cYjfX%cr&aSPZJcSy4$;$Bk}9g@Am(O{{MCV*7zsOj!a_;0ejk`em%{BFiUqCzU6Uwcj>yr+V#-eg);t>OsGXe!tM!*uMgz10HE~>S-;q(Tn-0%k9R)I?8SP4QpFtrBV&Vm^Y}(T+rNLP91c01K+=`2pU>HF=*bN8JwFdY`#5U4HL(2ls3?1%WnyRE*N$-;04D)+c5sT*ndUza%TUXl(DqPs|2!0T{Hwc!hP#^3C?tLTTqc1ukzA^sIHlVv~Oq;vJ@%6gRv0Jad`Jyi?DU3XJwW}BBX~36=t(u5$&x@#0KR}N!FnSe5tv2mIQdL))Sg+`WR+~d~GT1^O~srairLlq`(*~E(WED#>o}eK2O=+j{%>VY*6-hHe3^BWiAe>gX=k-u0HtTQH0V&j+`t}KjStaH~A+IH!psDVx#&x5Q-K2EfEX@^T*#ozzi0_9p|-*<24WR2ZwKOO<k@fZ<UIu678CJS7hvb++yg+p+p21te=%62a&;*VxixeHI(1g$}FQQ>}~mr#jKS0q3k1YK<(wEf{1d^6$=;EIB14KU=??&IkljG(OdC025~%*0d^~*Dqr0hht;V4j;pkL<7SZ(n>sHd-FNddM>57y!f$Ur2xkJe%zhO3)2V1P?kCQxjXfP!SHE@!>IfwOvA1!o@Ux+l@)iH1DSD$g!WR}qcn~u{T>*{I6cANgb#KVini$dx)pp5=jCs2-p#9d)${rh1T5M^m4cQH8U<zZJuF01`UWveRgcOwvfQh`!KipJFgbI}s>kgpuKAYE;#X@EwsK^}3H<8ey4RbXxOvz)}&|C}7a-T30h-#31=A`1sIbz@mS^NY(hQS&3b>ZchWb@jfgfb#JD%WIZN6L;v@=b$?pmSz<Ei0Mth^GV^iTSHOsDc(bQL*ObN%OUmp!7r+4n*zwUDt8aPL3=KZD^;qWaa3=)&*gO+!J2`WMm~Pi4f?-!d2#~i_oic)BLCjy1_(W+zADvc&(T4iiKCGg8s8s3PQasPjt)}TUngeb=A)(1^I-8U99@}tl^dRUp}rL+hsSJ6x8beF#^l?5cdyI=p4PmFTY8?KXPW|MN446Fe;q0IUfiu!svhHe;CQQXAA&Au!U6U0vy>@@~Pf97}noLUAxUbi9~+AFqM6o=BUjpN%MzTy^hF{2#q3-A|H1%N^u4wPmqu7L~ue$!*AZ3a(cAM&ZZS?tg1mvp{u^M8VDzTKpYJMK>z}?u`^gqpz7iBshbA?YkA;uO~77TG}u)I!NA3>+<@HHZS^<P!>PeS7-cm1!Y2u@;Ln~hJsxOlhzm0}+kN4}{7xjxYJMw$5<^@?Wha5NQA#viU3Zflw?l|WtE*s=lR2>Fk*%$w+<!kU%WFocR@2SGw~BXI<~li9;zbaj<*mY8CD%ZL6{Ul|(gFK1!e$46%M*b+<G>(!ihnJV?0q2+7d`84T;YY<GE#@F=xB>EGAahw%rYe|6D3$@K|d$V1+z0+vtYdJ#qsAzXo5Bw6n=2v=2UW|sL(Qmv_FDOz9nRGD3D1F#yMp2t&eXnKqeu9`EHO&)lrI(7z9Y!62a?zTZ!Y7z)2>NI9VN_Cf`0TX_ybd%6LLS9LUoipP(R4n#o6iWOEi82?yX|WFD^3V#m11cmWjITn&fxPof|veZmJu+}@l6KfV?C(I3DbMI$`SV2=xfJreWSy3U^f9!cu-7<+L2lqO+(4!rS@C3rZ-Hj)<jES@oZY%rsH`$w;_&K7g)EEP7hP^_>Ho%D!IE*qv`P6<##W|Ey<Nt$JO9l53X?q{4SJ^FR*ZE4#?zggxtq*$$SrnD5<>sr8i8Zygw7Sa}Lk<XWI8(2EDFTB#C8`8YF#MQ+4P*%@1F_O0%%xKxT?hD*YMpL_WeeLghOtF3r_vtB=M^Y{@q4e-T^7|S7#b+d}l_+^_wQpgE+IiGDFuA*F5uIUw4a!*z3kcix1i9xWEZ<7JVLCI|WE&^$<oqOLZoUD#gJRHmjc7Z+9W+On#xJL6IFZ}ikjBI`a8saW_JtK^I{Em~`>zRSf}c%y8Qtf0Ol@mPva7TfjzOwmHSp(RS8q{dvca?%*shqE>Sa|&3tCE-8p|b2cq|Zgt*~U!`{^VRa$9uTnGZPV-2c$CE1d+~-%=+lj+IX5%ACl!db!exWlrry{MtgV<<1J6a?cyKBy|Qc6@hF!#MVPg*b;)@%<|+JFMHrSNUb)tbyiS;;k2NU>Fz6ez<K8VD*rGa9IAYY-PWiJv7CNU{gK=*2s^K<Rrb4YknD2=C9k%wPL!OyB~cP$-lR650hemnVz36_+@VnxL)9<hAjJ&2$_rLuJkU3U*vY0aKNV3M7#@2}n=3M%<dbL5?F~)5xP;FrYB;_s*g4x>)i?!&J!r0_ZW5r{kuUn%qxfpc2j1=Ayjh+}BNgAWh#<N<xf~m;j<-d&B;VW3oz>c|cDSXEaxZWxSC~#}E?}C?MMfox>}(*Vzjhqqcmyd?<AsJ&%7CyzU9`Nt>_$|qMM6|-_N%GHZsEY>#3Hgf%sOEwHW_;4CKlirDJ2yr(@%Mp%*)~`AjN{&rLKfh+9JK;9{8(P=L9s?kd>`OxI1&uf+^aQCODRoJpOh7TfTD?gBv8sjY2h-4X`~kD<TE%BA6(>a4s!~saX2PD1`$Bc$8kTP#M5r+q}he0y{Z*t#-JIsT=Ir4EgE{;^ranSv1+-kfv`z%QvmionxiJ;=d8ibOj=14dkX|NytNpZSlo-YvXG>)n#kW>9Qdw3&<4UB_nDI7@q}B-txgesVLhoKd*1zO&zmVDf-4Z`od0Rv77~S2i!Op4ktp!>=-GdS;vV`oetzhHQte?K-B`ae6j7u*y<_U345|7ALPPxSFMXVcComI)!B1B7>MXyyFzo8U+h3wT}=wf{K9i*Y}_)+Zp9Q(hmsqn<{o_24ff}mct^&peDd5P3kb$wK}(`S>%o1|%@|>aebpEPnmJB4UO;DN>HqR6FK6WZmY2J1NA@hPTTyhjEkz($XhR`BR2XpMjCJi^h*h3`n+<de3C9uzh5s0U3_xOww=c#?U)J%~(-&*$IdepLL&1{j*K@jY09}{b60z}$N6JyHgvD9Gn<CiAXz7GlW%jkkJlt3%99et3LerRp9q<aI-4s`?`6nfX8%$*vdw8F|q;pF&)f`x}RDxH9myyG=t}ZD7yYNBze6c4+XBe+!4mhqjIICdcWKM1^$>TaH0DBc6N(Uh+kin#}$J$#roIQgLez+rz=cMe74zr>s7CBZbEZ)39;Q+k<tM9sA0OsLHo5;`^TVlm}W{(83J6acdt_VrVcocbJEojdz1Z7wXZ%7d_<1!qeZc`S5-b}xytOD`UDiFPfeO}D_qxs)PEC(&(&=&vnB7X+)F-qIoh$Ob>8Cnfs{zaBeBpc}UsCdes-k^3Es{<naJt_=36#)f*pXZAKK*YvqE@24e{~4o*cs~IFbxG7Nh`YYbJBLJAU7aFgKQ*UJ`d2Pth(<v{<yVGh0*KNHdI%XGL5DVm1G;ym{GFhfc3mmP#DqjCAC3T^L~rAKkvQSkj2X4w#F9A~^~AIGwODUq?TIS3?G&XZ#s{P-u*q7!y}Zzn*qe01tUzyNxzG;sf^(>b7yX4<n(Xw^yYEzvMtw5I%=yS<R9M5_<oVr5#A21sh;~|0DA`lP0jwy0(KNUdH_le9dkHKn*32IMyO&{q&9H|cF0^Sl;Ax(^U}HYGl2p=|k7d9+;|^HSjs*CC!+zmtF>~0XO0nj!N9L~*EkYA4{wdPrI}Won8~m#i(#d+BLRc^XU&5#EQza6HpF4_n{`{f%no?17@wHtk5U)$Lv%V1R?5>V>wv2$~exFz%ULVP>2`rCr<w2bD_6otZ+WRjkxYnLTJNH*aJ1MyKgxcDo1U&mk1D>gj`MJ*8VL3Qn#8;&pJkH{u?fG(WcUD;KViZ)M!*e0fL{bXWPd%=uhDxbXOpV;ic^d=&xbnME)Tg=_4viKL^`z3BG}O)nML8v0C!Gc-?%m^}?vo3pZQMK0<E$h$V5q@#jV`r-T_>jTnlO~YYhna2PNd~j9n<1_F!gisu66P;7*M#wl4J=O4+!Z!)`Mu}n_3m>vMQv<R|WoXK}YP|!ax_Vns`>avOL_3%R@B6FJCs=vf&Cvyr;DYv#}gDts+I%ui@I=aGKOY(i>bujW)5Zc`ibZ49Cuv7VO{i+y3N!#w%LpmA_q(bYEg70&v;eR6MM#KuU&b1&Xs3XfqPa2Li6+#5R9$>FTIZi>eZ#eCx&y%mANSEA;RFc+1uBL6@s<oGe$@=z|I!^xf=@Bse7RDiNxX){_#UWzhl)#v~E?_9BM~hC-BjVZiFuovvP<S-m0=I?v(tkF8-0wtKDzvz06nYjU`ffjnIjp`>*Zocv%(`&-T~X*&5ul~67KAi}Ni-fMU3iclzM;{6(Kfh}@Qi(J4lfcxb$*OzmCZq)2_JIs}gfrC2&{=qq_6E73A(V45K);zjd!=+`9rcYV<ptAkAR;U1a$q+f8a3TCF?-W~P#2dBV6kTfQ(A0EjIyyAXX>c3)9m&dM3$RTyZw7!t%D&VJcX17if>E*1bGCr>ZWhpHud!%$eYkFM_}BBLE5EDel0(CFtC17K6$>6IL4pyZAE~N5#WOy%5LV7<@xThCy0Qjr7w#@dQ=St>2j3-+&V?6~34EGG_GuQ_FD)1_z%=Y}3!?|jZ+u<EQ-_l{#?9!;3_|>xLj#ITA6iliO4%y+uA2D1kGCW=fAM{CCh)9d$(B^e6iaZl?hgnF>*cv@iFabomjwmWyDdo)Xv|!+i%i0%QF>$wS;J&r;)Lr`(`}Yd{^5WS^w2T~!g-yAbCqOvau)-?PUi$Ozh@v}xC3}C&mdnh+PG`z_Y(Jkpa%e*l0`z&E<f^v#BDwJFFHo+YlU8!m;I^Ax+@l2z}Bu>@0RUoDge0v%FOmt*L2ta&ASIf7-i2rJ+a0J0$?lH$e25ZlVAu1#ZVFsVCdDs5NEn&XN+GO-Ay}X!s1hA@6bLvceE$L5M{#h-vvkVFa|@gYKtF=U_Ioz)F#Uy)fo1RJkcb-YNlKlf+4JqZkrMVZ7dQ(s4#4>w%DO*jDeCtX`DXRk4Hj2Ihb<zCsC{VttzeH=j34no1#I!8mf3p4D$5ARYPcnJGb>5uGBG2mf}KL;&$uy2s`@v7B3lPn4%eFN2rOX8wfyKD(IP~j1^6QRw)8E7VEWlrf*HF1o@Emh9TO@vO0h&-D!h)Nyx9F=MF`yJ?$~~Zuo6`kNe+^@I4{{--wTELu`Gmq%p80HE$cQW?Nh-Ryk%Tx=z65<b~*NCkAUPa)`fdg=Zr&0#RSXqYkV(gEjd8xZ!5U7aXnHVzUF3*b)C3H`!N359nJW=}Yk_P<;cXzL;?W1d!#6cZ4<~b3^)HIlp-d4n&_ww#$<=5OBkmzE5ioU2g0i9x)>*Jb6#C5^vFcz%=8A{84PPg;%YIYg?lfT?YYTohJP}v|a^VH{J*6#qrX+9f2t<ElV5Nj#jvtPqd*(N~Nk(XoWW$x6uJ?b$Nc?C;}nfNZ-4XP<Z;E-hJMS1t>u0J|y8z_=5<(i@LRfg*u*F_gdl^Y~2%R2N~4I@By~&QTamEiib;|ro>^m0v0fv4EK))0FGe+-U=>SR+P~ZgT2*~8z8j=O>yMhdgKs}5dgvLxt31Bf<TTVD8ODBCguL~C00ZO$i|W?7NGzwveK}d)`kYaYAk;}oJ|)UR%(qkSL&)8Qi6^yd-zPWUW?y&uXPy6AC^CGC}N%oCMJT+XQDCL2|IoqsL~)bN<DU#rl4R*|A}5%kG--rzJXhJ&^H5r*r~pkK&0GJg<bJp%8xM(hDQ^TJ{ai6PReXq2mE;?M<&yYH41L5!=Comgj}I<w~`*Srl5TUQzLpS3M!qkW}4i66v3e3+ELpWP)UJ;yp~XWJPRIYVJo}!-+a%nYUZDaKj0bih*yQYNfV$K2jKEe{0*@^GEkx8<1huVfc~2LG9wuI+ZByPB3t%{&Vr&&`M&ezluE}%tI=i1KF2X7&|=nYzxvpVe|}&8wV_q>nEp;Rym9TTInI*HBcYby^v-KzLY_3=DFi2Si*65<{~Gq(#sH3?FA}{S)}=gWtXR~PjP#L62!}vPH?k?RN`3GwyX(nM><x@+E~#oU$TZZp5{M;jw(0Ny=n2d+sT5;v)cB22<D<z(&a=*m4+<IVmX?K6b!>z6Pij3X`hva!s&c946*NRpe$)pGBJ`p`0N<<Cyn1gU6XI`G7*j&ZEbBleb-v5mpfp@9^5nRki0W5R@5TafScl3vvGHs5nmEpVa6n)*wE**cvY6!C|D&l2{Da({s$MS}NBdtszT3x__Wal%Ut0L3g<o3u<>N~WzspDeVLtkI_<4HHx9OwY_WOSPL?*;bNBx9tn?BsN(r@Rs_0RroeDve9e*4?1)B5-O=s(cMboEEic)go_oZpo`j^Daxd_358S8XE`K+MV2e=8-3k9WqhQ9tK|{`_B)(F{fEkuo2)zb|Y9!HwrR^UoM9syY9o5s`p=ka0*xFS)1T2cB0lX1*q=4y!goG@3*&-CES$S{Qys@=Mi#m?RW~C5(86QIwO%Qd)<JSiS;;lvQ{uG>)@veGH-O4CSLMe@8HvXrkQl-(U|uozQek882m!$cgXx;EIPI$Ddm^M(6kEuXuEIKflS@bBz}*H-q*U)0G`#TAz5*>B0T%(*CjAka$sWmW`v>6URv6S8eB109M|JHV*!}@^h1(u|2^}&3N!c@t_&?T6Ob!mQVyBrYE|x8F^7Ny4<V_1x8_Gd4zEzROg@Q@?SsuX!mcVh()eV+r68=-1+M}ew$CeBg0^h4J%lv_!t{e@)j;2rcs$kq>j(Uzkz=%dz@*H{q@BI62*%!Y-L-2ajM4lI9E2p$)4fhS8Sr$M}Pj~^z(7UU*7Y`uUvKdq*a`@eK|m)NN1WtKXC{5dDSC4epiPZmA`m?B-F}b<0~k8m@c0G<mArB7I5+4>D=LapANgcarzHg|Jg@3wq$FaVcedM89R?V*l?wtr&l)L_S4SuZ|8U?>+CPQ&7-Dxq*<<SoYM_kK2F-Oni>=7{i7yzv!-_bpk<C)DUMuLekQAZtlwS!9t86LAe2~xOFv@zGPlRKrmUqv41<WbA4s`XxrSr{kQLgXMru&mTjjxKl2=p;Wu%%cvs*_VLDKBCZojF%tUQPsi09t+gc=bWplnb}?Y8{G?LAB8_``Lcusfq9*UTpQuvi$RiQuRnyuaB4=?=(kFP3R!MI{^A#Ome-DN*l68d8(d&D+bGcnA+gTb2SNyYoOO?(*J!A;t~}ff!LbfE0hFdXEwYOxYV}(7TQE1EE*>j@C!$D{+MoZr2#;<-98VG4xgK;_?V(NAwj6!#^DKifDs)7J8MNpPCu@ZrXw{K$5mO2fE64MWpg-IR{;-Zk2L*0~&A$rZKB30I~srjq;heD|dps@;9#Vp}3EayZU4AiuyI&np**wm6EXt9HaGmK&)AS;wPl<Feyc=kANg(eS}4E!`j6oEU%QJgIi1gYb-*{ZyrQFDl1`e7Yjm#709o8)!~G$6?ZHtAxOgFnU8(V9<eaOfC6Y|Vdi=*njQaz74jE%wLBwCwE>dUn?N<X%02w|mdU<lqdu0&ra%BIexV4~oy%nBu2zftbxLCglI|drO^%%vxhv5^?$I<hA(oznmC^W44l~)L<@PKqnljm>WXdO39=atwqB&x-gjD5WCVOc-|I%A%2@XLryFN)~i*?tmUf%W!l%?H>e-O@0mIax2T@=ni$!yHV4e2`R;RUk22jF^RVWN-VF<8y0CPA}fY?G)l<*1Ov??tvrISQw;NuMmk9e?8`!~K%se#u?Ee0=G^FCF-$g<sO!FX`=<^!7`7`z5{olHPtvZ@;9sf2Pvg;{it*?xXa!vkZ4hZ^x3}cD!#BGQ^Lgk$E<j?2O`#@g{Wcndc6QPcs|2WD%bqi_j#RShAaAdQ!ZT-P1|#F*7=*dsPv5ltlFLeD;^g*J_^IwwQ{SwgE|G<3XPC;OeLMGduGmxox}9EMJbKes}Ry^Cx}eG0)~rr+l`F@G*kgS!?^Q9xFA*_P><UzL?MMW)Bh$lG*c2w$+Brvhq(S<HsDfujY56JGXSTZYdt*<By-Eu1<6IfgFA#xIsy4Tqs!wuo}#8oVq@JN7up&oIA){kGwj3vy>OM5;KmFN;zyxV3#!Nr8M@KS{t*u?kExHEnDW#q*whx*7h`S-9DDLwzqSd40cy!#Aiw00vS2jKTqXW^QQ~5%&6`3?AYgXnNMb{pOvCM-SCejtzB8R%ARttx7p^3jP?Ale}1}p-dnss$g`?dr!1^Lm$#17-?KT|OTBTPy*`hwc;bLZ-{}>9-!WZ%;cne*5ZP@<+je@P&0{%iKO4WNjpp67{vK@j%U@YlC_f$q?|=U_as_EFS3p9cup!mxq6&}56|7mFI;COBu+t%rru^E2^a-|BMmrZLNE9ak!#jx#Rv<oMTCGN<Hp<^u`6Izs0ol>qX3NI69l!E!?NL1o-Dv0@xSK$QjhcV4SokeuxLx<!i^;hLUjw+ccbrapU)3AXthRsb*=i1l&GVR=Ln4L7p_;>RM$O@*!HS?m5i%jA!xHMqYP<m?RZK{F6Qq;|ZyJ2QrL9Bbc}k~@jR#ig22H}ogXlwSs4?EUZg7jX0_m}+k0Xy?i%NnS&b{d^h;%AH8e||gRm*(lHXpV@rSrz)uKeHs0a`SE;NG^l(A!X-y#}vag!YloePUn><>tA`cEwtz9;70h#9VxWFijuu(2;tYDY)$&D5!RL1lRumO_uyO'
_V92_P_INDEX = [(0, 26488), (26488, 14995), (41483, 22870), (64353, 36526), (100879, 36254), (137133, 12613), (149746, 26202), (175948, 10064), (186012, 19694), (205706, 14980), (220686, 26533), (247219, 28135), (275354, 21736), (297090, 41143), (338233, 19704), (357937, 22831), (380768, 20528), (401296, 13486), (414782, 18830), (433612, 18716), (452328, 18185), (470513, 25404), (495917, 32250), (528167, 29810), (557977, 32549), (590526, 19662), (610188, 17789), (627977, 25612), (653589, 14767), (668356, 30710), (699066, 30012), (729078, 16428), (745506, 19267), (764773, 18602), (783375, 16214), (799589, 13566), (813155, 16565), (829720, 23277), (852997, 13844), (866841, 25876), (892717, 21144), (913861, 23786), (937647, 15989), (953636, 15367), (969003, 29078), (998081, 21194), (1019275, 22767), (1042042, 27862), (1069904, 14142), (1084046, 18163), (1102209, 19157), (1121366, 34996), (1156362, 26356), (1182718, 23580), (1206298, 18368), (1224666, 12427), (1237093, 32380), (1269473, 14485), (1283958, 22259), (1306217, 14230), (1320447, 24008), (1344455, 21836), (1366291, 13513), (1379804, 25352)]
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
