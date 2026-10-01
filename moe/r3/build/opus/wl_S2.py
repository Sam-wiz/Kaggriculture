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



_V92_P_BLOB = 'c-ri}>#Ka-mL4>3Yp%7bR@JUuyY}V1^f{-`Io*A7PIo7UMEvl6@uU6&q6mqIF^XvuFG<rRL4zSgVkD+>5fSnsn0%2SqA>x#8HlK#6a*n4N}DJ~LHz?9&-0AAYE|vpm*3_6{SKY|dpGq~ty*i<Tyu^&=9ptV;~Bpgel7gDSYs?Xrk{lA>o|N-YAg@2Oc8HtDm90(h8)UNL%ol~F4QsP6!ML|=Aq=_Dwi0>Rj4uKXy2wG<rL$(54p2*VhyR-nK4!S>%tgw-KUz;lz3sZJJ^Nx-cE=qrIr0+j5*|C2q~mtNOt{@LyXZ5SX*id+5URm#IC|$2`S>MT?u7KLruFbZDQy{w3ZGfbR$l)yW7vyY>f#uM7wBX4J@gw>@SQVt#F65-dTqvdm1z^SW9r{!A`r$RY&g9A=#U}8tjV{OZw7Iw(hWNLOj^}U9j`7aWKTdXSoei$cMk+{cXMR^H215LNAW>w7=~R*WSVCQR|)>^BT|bxZ}4S&bOYnhL>oM>m6@>ykf_%)bV2+YADva%!ARo(E6VP67kQ5!g?;*83iLyF#<^sTx;m69ZB{a#k!TxZP(fzs)ncwrN;pbg*{RB(ZGWgYdi<dF0_%!xaXDwQcD^K43l+R?$HKob)`7i!P`}=10Ko*%UWo+>M$C1E4y#ZCPV?_WB0+=o781{#R(OCW=%zV5~VC}aF>UGhT{ig>SD6?+BAS@<L34VF?VPKBr{PSBD>3;;Q#eu-15S&9*-m@%*o_QXkA}8q+O_2*34WwPNY5GYi#WehqvzVNQ0zp9^nL`w?VcOwmlD)xQ!fS&IF8el#H4%qT6hm)FG`_cy!Dz_JL2lE1O-BW1iG)=pNkCWC6ptGQp0TiWs8F-t-U$YvRBOS=xlOCrW4-<fujoMX;}QjwE6l(x%`m>ts7~mqU-6LoP;4MNAd@?c$<gO|&~i8#H^r2|i;7&BMZT?0ml3{p}_-$I<RgiMX|&v&L`YknJgSe|uxkif?=T4tvIqV8YlGP3ZT6$3Z7$N*S7m9^qB!b6m2DHi$MB17<s#u`Rg2-P7iTja0;J3)^5q0g?Fze@DH5`DFcUZ5}Y~uK3dluNV=#!8b8~lb|x}M}`S~c+KC1j0emHd-F|*--PsyogB(HAM+!B^e>0M7`vZ@y2ex5Xr~SXm3H=Osxm@m*P+-WQ_La3Q?|b9#+)aLaE&8}6q?GW&28?wQj4|Sh8A<3Vuo%vRc&`Lm0L`8Zd36ikvhk&Ef8u`9oLX$>OH+e7;UijIb)8jq5N$qIFzOGTe~5K-g*zy0teBBg_oPE&%B{Ml;1Pz!aFs1%d@HW6WWupI7*3FJ9ik9!e-cU6TQ9KzccmD2TVDyG8PgF-DIswXeO>5tW}a?jJY+Ubht3GA8d*2O!X#Rn+{Pe#Ei7F@rzq(rviDm!GR2`Nu1ZvR6W}kp}sK7c!x;Mg~!~mJ)Ga{YTo(Z4}U&(zZj~C+A3`Alr6NB4SuBtv8PWP{619D1of16nNtF)ff_BNldekbaKEZPzMjVl6Vgswp@-OQrV2S$yhGw7WE(dafkZ9YCC!SmZ-Z$HDbt8BosLDEcZP=5z-~Ei_R~<+=ojk{JZR;jyiR@z#s|Z=vM1{CLmXZzMKltZ*vgo0G8KjC12&s-#4axd!xJz`_&AB`lqwZsGEoZF(1dt6TRlu7U`R}v0%dK<-QGk2ql8~i)V=%_Q(e|1v^Us=c6wo}Xz2vXvNfzi<0ndrX^(VeonTta<TdI6yT9wJ(#?xY62}3$zL^*U*Ec(|%bZ9Y|E0OnVUoj2D_nQls>J35d~3!6bRX5YEl&wu&xMJWnf;~Ex5d0*Ny1QA^CvrE!aPYaVlgjVrMU)CE6WbEHgM+IZw|6YcsCe@mA_u`6CHK(pw*Uhz#b<T&EC`(nj~C<*mxU7JSOc3QztZ1HnbF}wC&f>@d<A#jgHc{r3WJe`$(Fi;{t>xB?%xG7K~3Wqt>9bDwuU>4h9TXl}&+sTyacAV(sX-Bo(SBdyqJ|KEh8x9Yf<-BW&gsJO<Q^2_1|$JOWy^KU;U^MQ6nP(CT*0UQLS?Cx4C=2lm(h>SB8p(|2FAq%cF=GM+-+xXhX?9|bnJ!pgLvrrCz#IeE6BYL=<D?YPQN+<3&LwVoJICmR;(Fm@^=l-iJHXqMz+L*QGO9Sv4)VK}@LSUbKoQwYmg()@6l&Ay9S4_H|i(uy;8v_x_<nrt%dIBEKL6j-QyGpS)T<rTL@*1nDG<4CQ;Ri#i`VIT7W*ORT|ki->^V1}(I-FDZW9f+wyX)OzBEqt7gABzkn{?2;jDA;n;L6&bTjiUjww64jA$!xSo#?f>%j;!(MTr)SZN}7a5XzXv2?+WeL%<RIqpVm0)fBn@OcA;L)+&^%;9HB8|=3=@v3zEBDH;7;rY-v;2+MZ}nb6=ZGPH9798L}-=;;z>>aa$8=N+O4-LIukJ<+8Yg`J~%Jz1vo0-~ydYhv1{kbc}q?+LO`_#%ot#f=8+?`?rZ&(9_ivIpFvK4h}YPJ+0^5c2bl?$V<m{v+#NGh}7Cq7gGOXjEir<CRlIDdgI!jW{9*qb2%ilM`Cdc-X?^tsnbAf2r3??5B7!!sI3EMBzI8um@pNrou;78PQ)r@_xX(zMe|jJ8FX;~Q-Ic3dOd6mt+Q*}uPs+bC>ksu1^XizP4jj<ZY%fV*bw__n2&xC`$?>Tu3V^YO!NyzitY*R%X7Zt@<&$)tSYPm9G#jqw%B@OU||B%P=H2&?O1Zq)*Smb+6Zed+0<Mzz937zG-h&LW74rJGLB~-N}>S<F|h~9?n!~{aDmm}W0fpaSllV_*PB`_Ty&zGH4)ZoKkwSO8ITUW)ehb)s1=(lb<nnKcs}R@>jC?Pu!2>dWM)F6(E>H=*`~-11tfA`28-Fw+-Q^A^bYOdll751P$=k?J(t!;(>o9-*E`tWeA<=q*UUO!?Wt?N8;AP~uDQt+jS0&S%>;|w3deF!y|Y1YoABBOWa>HQ*pG9{v5#Z>gGrSsO)Hpk@$_4qu!cC`#NuYc@q`IOx~}N3njYPJ;QqMsT9|fNE4ehJ=_=}m1GY%K>R?()4vD~<m;vb8<m@lEEf~by#vU#$*o?NER-3*L?OW3<wqOtV3fp%aH-ph63$6ezYPsHF<$^!z00mM1&yS`c9yxSqj6hAmb9L&nvv1e1%W!S2X#4P3Q(Q7bq{OR~1@}787lj_Y(tLNY2x1Ip`U2e}XWEIrprMKWOKyq4W~D9ALp{5KC{hqd?SL_dF1Cryy?ArAVmu>vKP%3?L2E>I?;mx+OWL6sDb`?<h&8q!6d3HO?J;PZ$T<bsKp%EoeQ0M{v$5RZvHMtDvS0_{ZzG=p?yyf>VNH<jax^>LK%FPLq#!|AT7xR-hQ0(hRl0N&=|U}X7@NunG*uv9w5QRGPiRu-?*I89=VYZIzmsz^op>hedw3?(sZTP$&LKIRcq7y6ypiQ4Z)D%r0@_^{ypdCw;|DKzBl#3`MP_)fyG!24D9eFw-~y4a`4v9NddVlrK1Wx==3XC__?X_wGszWD*SgsL6nG~8<g>>2d8{hmQ<us3eq^=PokC8buCOX$Fln!up2{6}(*+)&qwppitW*^Ymc%`LTeNz1=sBE5dk3Nl3zqX{FxfO^k)(ZOaBU~w^qCbi;Y<irouIEPBoV9erpcF$M(Lzaaq~R5g0`zVN<<l;Qq6X^2{h3J8?b##Yx~6>UMTzBiS{CVp>R1`e+3$gdAK#}S&=N7QMeJ@omvK<(izgi4q*p#)b5X{){6Fbf#GJYnqYc_{HI?xIFGhPkL_tH7ey31YL-aNVzU-r+gYt-AC?YN$NCQ+YSPr=z;2=(H}pesU(U4y^O_w3tpUGj@bzUd&5wgJD+b+mfME^eqEJnEP!YdfXmoa6TkLwsLhk9Vp&~F<v8nX&A>IY+%x;3H7WQt?WmUb-l>+uW0*P=EoXqx|VQ+T~oZ+F;EhiyXt3IqJOzGSLkE1nom#OTy=x7bv;ARYl!5wB|n}7Ff&B`CsBr%bqO=;UKyV}Nkx(h4x8n&BqN|+%vQYZ&W`5o;JcabEUYxO=oaJ|3^eCzQ>1ot*PXH<MDtz7Nf`RMg)nTB_69jvAFOipgyVKMMbT9CB)?r{fLdj}kX`qdraKA~fX-g8C*v3oZ2VJwJM=3GpI<|s`1eXr`FYul;hQJy~=PLtyY%#qqbj=L%L9X~>_%*2Bg%8#+D@K(|*0`clb6CQXgdvrvwhGec<m?0USWfMD_l6I4h?tq@%T(?-_x`J!>oqxL;5QDH2@IxjXSQzai_N60#I<DZd@3|BsD1&o?-C?>$Sfs}Wi;ElA)v`g*r?&^*LFjoO9Iy1G_8k@+9#4IrdIsgKD-qwvbg<c*_y1NO+(U}kK`3%iwl`<T-#)(I$G86cwm-i0@LLc6=J@#56>pvVc|N9(^D({0<@H^@t=~$sKlJ0L7^d_lrJtx{>&N?{`qr`Ua&39`<2zmZ4^GFX_(31jNBUS_{gE&;MXUVdvQ+~=&fms&_;~U@zUqCU(<w1-#y78d4W&MF@Zz^mzoyHt1iys_8{u)j3RR&u`gVTLKgHSF$8`S3h)kT3)&468%3KLa9fa^4lY+W=>OA(8=*U8Br;B-@BNVtC!g`|q5JiZ>_(X+%J%W?ld!`&9IyC<!{}cA)_*dF-I<N6&jCmDL&S`%hW=c<d%V7C@!;qFI({Wp$xHh*tKWZ%zrbp0gCT3EYErq4nA&f=<LlX0)zaTKXV?xgwhVW24eJFpB)|jwtSbyFjXRT^KN@VY1$g-jcPqi?%7M}L=4ET)#z@D}9sgJ{H_a1*bd7uIzB}J<3o;@R@oTPBjp8R3rs|WZ7xU+T;`XtZb+~W~8lFCyP>h#;!ygt6CzYZ^46}{gcoe&qdJ$<724O%|>D&P+o&mZ=}kG}Uao?Tep;m#MIZuuJL@mjndZ}|A>hVvu(^Gg;-bTFm)NLt?W@j0;^kH^z<Vr%N-#-~f|pP%B=x9ORYok#!0JD;4;KiR8K-Di3H?1bgmVQNSPmD5g3m%4g!#M_zupc<^%9ormNv@#uE`F9dW{9OoAl{oz<)Cah~ONqlRKv>uC>BFs$=vQXE`yR<CcN6VC#=}aV<|#fM62pO9Fb|;;x4c)*!+r9F?LORvbRY8W0Sdc+K=W4&KppObP#*DqUVii49YG&7PgacML67!u+}q*r*pf?p6^;+NJml}$k^59UX3@T#|Ad|-J~a^m^Ywku>IwvHLC`l6^Zxw<(Kgn?zZU*#oPJ4R6aL*W%5?`(o}ylZEG@)XW0_L<&NX8q3g8ts<RFj_Bb9pn0+FA3VBmGHP#<5rFcD5(ui7Pqa_p+kK}6NIH@g_FxGf*{i_?;WNX$;CW84CAE<_;5s=eaoNe9!8*<Ai_^rfmLKQT~u<xxGxUQ2CBf&<N+?}qZgPI#ExU{=f7J<%#Hw%$>S_8&s|&W&F((7L*5T~zpVcI4+ww8v6c^UWJlgSdvP8=;H+RSnzeP4bW5dmy^O4(=8mC2)Ea{uw9yYyma|6DullrlEOh^p~qJX5dQ8KX0>TDzVP9<q(Gs^TdW7V_r(_Ig%w0H-K;6J;VvJh4e=yaR6F%pW-(B41w&l4f1#QLY1W-lmHCQD#R&&&m{7S(6H2SXZM=R{L22;#Lcrad5U!wzuimIVhnYDCG^KJ%L8JmYrzz_3MydvwUUhZ7kPolGTU*aoYee%{w}f<k*2|BOn`>;Fj;wImv=W=Xbfhu<^ErN-`FAM{s=5Z1UUN&uusGehuG!Zm!xQBH!`X>=6%P|^pN_Jr_6|8!M6w;4rZ)TeC?_!c1fW-2I{Qe3WJUv&#a8qr9A22D)zN7yazY};^7GivBGUlogeI&2-8;v6bG~1^BOlXJ&E{v0pyNR#xw^S5go*ZXdVtu2w0|m!u?mKsrXfw?I2Qc`U(JYho=ZToF9lC%KN`$64_nF`aQ}s@c#fDn8MB-gmOYs7!;vxP^K=Y8_sLyt4XsW^J|Fxnoz*Pq?#3Qi9^w{&4jGToGghifci`;QUaP(GIc6fGGZ-&?ae@pOtjaDZ(d0_WQOjMv4QL$f|Bjb(z#_1-%Sz*Q@LQ$<w%6GOIDTHYD#2Eyr(?~Vy?`yp?>Ii`Id`DRpUpduPWuKv%$x=`U?BC5#aI_fhZGkY{Mip8^A`H7^^6t9w9|}%#ILbE}p6DvSyA;&P0^p=DZ1eulh}Jc~2Dk5R^b86J)D?7>MChrdA<}58F1hC;bhFk=XqC`qcpYn<tRjR}j<bB1~-{Kn(~jKx2d?8J|k{*gF;tyVrCEM9b6KA!r0xDoH)B)<lw|hCE~5Pv7H*dcn@Ha3Q6mPse<YI;S2Ltek_Vab)BI@K#FZpe~0tWfmPlV7r!L#H>2pfH{M429R-U-h288)nIJ6F>B#Sob*-DhW@J<whbSa93RFlYH@sS-AcrOb*y2LKC}YnWH^O|EwEf48x!_Vhu@3jzcS|XU8JW$fWESigkC*FCHa;gm@wI&@`B7f%U|CJ3IhDr_Le7?mZWSCw9mz{j&`K%nKC#Wm=UDeZU;@C4v8RiW}GIB`S#8e%~#x=uMW9*sv?fqPuopA{W51WASHKp=8k8sn7Dvpxy4W0o9PbVkAy}lc@avO*cd3o)dSw|V5a8j2I^xv@Z`Vqsk0n183z)T^y{)560;oYX_mvd$a2V>gpX4kI{f+(vJ3-^kSXhf2kjVw13c|=r8Uf`<$Q`-)+T|zLrfu@tjq?xbLYV2BcZ@aTEk`3ay`vyC}%khLeJW|JREb-6LD;FLPLL=&@d>W;hKpzi);qrv-8Hy+Uu6kFg%se03rjdN-d|Mp_4bC8o&7$V)tXSd#FuTAm4~%z>@)`2=$Uj%I2CV;R70#_Apy8e|jv-SGLmQXsMO75lTabT!*T(TqM%Q657o4zGS8_vdjxt0c`Ciehc(dK#nsZf=b(@uH>|bq+t;$+~6tgiN9havu3*1BIz8--+Q*7YMD90wkL$B626JaJZzc93+orn=y?wLMa*pRj}y1FCY8Dayjz00Z=$k*N9`9KJ%~g`S}{sVWixvIAukjOe6UTT@}p_jj8cV(R<S2jm*00{><@9+aogK0{i#r8RDv8I%H2JdaKI?p@ZrGzzJvVTHFs>eXF6KRKfe!5j|A`-M{M=n&`(TT>bD*EC`AUlcDS%PZF>Fi2FqaQ-$I~QN7KITbD1P-GxxV(JFEvP`vXWy_*HyB7G?gPR!iXU@FIU0Y^JaCZ{6dYwGz^8T5$`Azaf7qcA1Iu6VeGHgGM<+xL_7&kiSJK-~Yj*`Trd_7|JcyAMTN9psGh1SQx(ywg%(Jkga1H82j|@djMD7BAq7<JL=CKJNT<>Wz5GsHz5Pfy>{LeN-s0(uyOYEdZbO-DD4LaZuj<c%+}csFbiP3ZP24@=1xRFPUV%Qo(D-ux@NjvS@T(lSbxaOHX_Rn4D11KCc%>J{ivLH+_vi4k)r983-IN%lzUFp#_fRPYy5f-geO&i&bf+6mGqQ9Xo~dT_!75{=?5=aiF7lZqzj*|Y@}+iHBF|s8;X=2ppLt^1*}&|?<aIRmu*F&jzMMP=`CqVXjBH;iXE~JvS$M$vBg$Aq$_w{jMDbF<s;B?Xi305SFqV!Ow2AB=X4vcjc9nsRENY(7uStZ>k_SQZIDZL`hv&|nvSU=IW_K$h&#h8#BC6B6%<WSx&p%*0G#@!dn9#Go^wBim)9DqUnGE;-3|s3`>n$e^$4B(bv8z{Htk`*I!jLQ_!D@Lh;5JgY#p<8wL@nPoDCnarg=yLVE2FJ-1%XDPpHJ%TX+k@48FU(C%BtWZ(7k#_)?h^2O0R(7@esX>~rDRxK2MbIbk@)hUWVbscT#n!{ASoZaFmAf-(v8M^S_)AtHGjIN&ac+=$B7^SoWPD)kOCfd>6oq1-DO_sZR+zR|UlZ}OMyc&UT9S765!M1GKukqJSOFz=4>)_9YmJZLxp_y74rj(~_mGuw*zGdG&ajOzW7cP1R0=j~&{vBi!KgkxBQPua$NQ+I)IOw>opF5&{(IL9c~Y4D^XW$TM@Ok8B19+2eo&U+rOr<`L&`7~wD-SG4PdT&WM#=jBH5>S@a6}FTEJyxrnn+LMRQ2R7qxglD>JO<xFWh0r>bH+RtnX5FDk7aC+Lq7a-$93ro?hC*273qO~TvKRMS0+<*w_K6TO8pt=J@hD)UYHJX*kVP$vU#-$Yx-Z2vVX%20c7Vf34I@!Y5@fL+Ma1Iw<2CAZK4zOc12E=or9~gOpu8g1sQ05duX!&%xu{*6FhacsSG{OADN|U-L=i^upBy5o;~sbxDB)8sT+y%H$BrM*`@Ep*zv2HkQf9)80>Y%8z`<VrWx25YDuCmLLyF$tN-eKa{Xs^yr+^{9=ReCXHM+qbh$8R9Cc4QB(9M2Q5sCl$x;?RiE_r2(%cdfQ~iV<`gEyj3314YMNZt3Y$7dqQIz^E|HRPEj3`LsC{*)v;wCy2TUo3m)p;c-+2X!onqf@J*Mx^^V9Mr-#;q0*QyOt)Qvf@eu1~kg*A2T1mtx5J?Nfv&8_&qBoDZLq=j5wMX{x{cv?w|8AHr|*ejKagjgy=Vmq<?P^&_!Dz7Ql!c}=-*S>7RTp@SWXQkfPjtcKI`G;xdPnZ_}1L!&zJ2#e&d=Y8@bFEc4oUg=fHu{+W>b_|_}dMjob@5o^xS(T@0&ZGs};|y-&Gg%YM4o>YaaG`iCcHp~)KR^q!?3Liz!I6^N2X;<!HWE1}HDi(xD(y9E>lT=qgpLs{p<i<Flub!AJ2T03OiLoSH@!=}l0H4fUXe?#4vX~mx$!{0pq;oO`n(s$f;aC|yIkFfB?9kjkBy}}3g&P1$5b8K)!-JB$Dke)K(P-!=74q{Ox0%CL#lFp$5X~2{#fK9xc-Fm37lg8iAMvz>w;hJz+qCZn7>F<V!~2W_EVU8_)(N_w+pr^%YjXEbjaEF&TM{#8@@8CzUtsxgn2;UjEfj^vZM=P%5on)$@M-^^YTo%z?(nbp+N;*(u-6R<{vf}rJ;b(mg@dNMNM~eM8XFdMsVgl?vUsUzgHrco-N$9isU3ZmZ@S|BvMKV{{{n`yQjii@pt*_Sx(}lsc&22X_s<kN~;>sc3o3GZn?{#xl7|Hk)?AdZYj(UNNbQq1J`OAB+c23)JiBGCMDtnG*#do1kXT5fX|FC?r{+)Xj@nWOoBY2aNUT+g2XjcL3E_ib&EOh*DnYKV%YTPcD@gn;X}iubRd2$T?-dQ7&jCUxOuqI9b7aJL;*h_4SoqoqH|?Ur%sC)t+YQ9JwxC2S(KECG6io_If}_jx9ue$812EsDsbE-g#Q#oaUMVq)ACvqUK{9%1LbUtwAm}N8o8(_zS8*#w48!cGLvHrGB6ME2%i-D#>7ldnDm*Tusvlzip&iSxN^3?nC90GBW(8*n_TL-W;m0K^T~ka@aVtDqH^eqr|Och!Pbum$3gN`P%J_ezf#1vMMg#Y^$`Xxq?xF~lKg$v4XgVaFbUYhB?+g-YyZnv8+VtekKf6-yOgy2bf_tnnfc&d%{mB>^Bi2T>CQ<Gnn8EMZ9r?ThzG>BC**IsY|W8p<jj=oThM(r<;pSO1W(7h5f#jK-0nzA@CqX?=Fe`&{r&J>cATfWzut&zo7%##v$JW)aC=dRV6Tx4W+6%gEwyyfQp0MA*Ss*+gma1OMD}gjdSK|WN!=|CwBeCy#tp#2F0)^G(iR&Y*<$3YA@hX@r10;^sWCWLlq1&Glt;!oIlqPZY!Y1<u2T$CKm^)b$$k7FO>IUNp~bNQh{oB}lAXmkX`<M!q4b-Db>nTmAiQVxRCTwQ8Ri#ksOiH!SMP2;{n?L3*q~g2E3s+JUmZnwt6Y5|PnJqBk^rwdCAoYti15`d7q|s&L+9!bt{E<gv-)#TKa}7IZcO=5ha&HcD@S-(EBCYMl)r)Q2v>p(Is(4Zd0=ldKxrQN8{jgfM>}CotdcB#O=SwyYNl#Iq<x@$IXIjPO7phSrvRniBL+k+A{UvCV4}hqcD)b{Es-bu4L^Q)FUge)W1vKcu5Bl;C|pl#qVu(kLDjw-ca%HsD6=SqF-OjJl*jF4eR@0DZDJcb>ZwLtDm|4i>nR3;gLB2j22;@nQ!!so9;&UGyG(Dovu&pDF=-!j3nR9UwpQkJ?)(_$O>3nhbCkyH1(|6rV{)%u1KqmP5d)W8hB{7%eG=udYqz-AU1n*w=&H8NnDQ3rY4@bWrFLfpgSdRJlIS{pzv&U-Id<rHSv6+vQ~nh)YZGx+W>px)pA}QX+OlsMC`*VhcYPYUrk6Pbq~VTz6o_UW9Qbq$Tc@X#rsP9mdZ+2u@^I??pVICVs!nVF_{UyCSTuM=zhJ9f!H`k5!pyTwQ=!c~+n;tIkv{?}_|-ZA|5a(1c^wDamTpC%0(~*sRT)9TEaohlX1EnGe3_W6B-Dm!w+gQ!r#Lo*9GpZ11mc&ysf!i3+O{24o{xDNNu9T<#LD!z;m|`yY=1IRGn(>+ADRlg<IfdsjVfY2{Rk8jXs{Gz!-$c>SbNoLGfPF#j943l^u`xN(XWZk#_lG-0z#T{)&KraIS%PH<FE?(;s~r3eV>6#D@vLv?0DOBkLb&!j;AvPwmu<r-sPkBx2<vZYW-~%O<A*#dk1#e`76-xdLLiKwxhfbgLg1T-g{SFtA16d=HU<hRQD(rc0u<N_jAP9fgK(~c0>f_yp38@*vG_Mc{i&b3GooUOL^LAUFqp%aQRLNB1>B^6U4ki6njkG--862OzLH0#vi(Nlr(ol<}k{mg>|t0#@xtt?&d%Et#tDiNptnudv{A$iIcF)<XW}fWhf5TPlt7T80qcVqHFCuJ1tF06`+HNZ1d>Lj=gAeAE&|GwsTel0#stj(-tS#Jqz<a%w8}79g<?r>_V<`P!Xz!kcHuK!Cfu%!$AE|n|@d~{jd`<j}ly$`r%YLz>)Rc@bCFn?I&1D>KE+g1LL<{IRFv}6#N5U_w*b>K6^yMz~BT!M+R~zSD_5V80`Y)<%lC%>xYgh8i?_mXh9AKVZD$|Wd<)PRc(R_Q#4`|wIWU2p6;s-mMlrcAh=<o!hmmRaOZPzZdCw>VJX4<2;%4kytalFqscI7I#of6&h)EoRwO@o_LKpz<M%kNpil|=56Ek3d5oFz;%ew=o|KVf{Q3(Vd3l3L%TFrT$b3t;8_2o|zyT=E=pQ3*B3#osIk$bL*<N<Slj59_nWpg90I$GqYBbH8n11$UKKMSIZc(<3lrG3CTN*@OAQ|V%PNtgAi|b&=Vj|r`3ZB_?cLUus<HE2-=YU+U0b3lPcjm|$<n?1Ar50qSAxRr{)u|bCaV3nu%+=D)8DA=;Gm6k2F4v=vr`f7Ol?(<JzdCMs8hPb-^!KQ+jh{BGqsnt7A&nQ+bTs2iY5BiH9G)nmQ)a?SKo;B;v`Y?bL?wf@ciNLQ%`8e%Cie-cGe4t42&(44eWwBjA3<Oflc!ImmFC1d3hc~-_aOp1iE1_E_(1}jve$l6Anij0wwrlb3v2Fh{SkI;7TeANdkk^BUUHF{a&%(u7N}gHMku`fLU`*FH8_}KD0Xo?)KPwW_Fk9AM(W)5T{#|Jx$Ackd!6U;Ip1}R*IZBqEA%W-Zua{}oBi?W&3>8OcdV_a{F2?G#>+B%yb~&O-tR9r``LG_4)CVjb#2os(d%9G9M13FNrf_Dd7ODCSxbT{GPfuva*0~0vCOUgy7?s$ESh1e#H0~s#buFFKY2Qr>gTaG2eVo{J2S|0aJ)lHO^+>YII}i`ldqlyi<1Y7Js>_8F2jQCp=YItg=0~Ycyu_;k>Y%e6t~^FV8PJ8QITTF$x4DOwqW^rqWG^b?9;uDnd4BCDo>p<2XkZx4;F7f@t*xxzr8}2tKRFLy>FpQ28*d)9~ZjpE)=>9ngP4%2s#^Eq02lrm`*nrx?EJbtRRV1g}mJkDb3GUxxAgLT&^Dj&A8N-M<p(QHvT$O8fAHR4Nzw4eUJOsW0w=;UQH&Ld~HW2GrlA1Nio|6sjJp0$UROQ1m1_nHX*r}F5`Z=G*1~}-?0eR>ai$TDDIRfs$OF4<2Elx&uw2|R~b`igv&%iuwzmpu(@$D3ytYHCv(jcm3)Fp-HK-=@qhS*Y*pp`D?sVokyBoTe6o)ZN^&K9lnW+3i7~V=PI4Ts8o-+mdUhrpYNtPl+XLGIUZ{T#=D;RIE<zE6pr3<-@BF#=SA&>5^xE(-x#1w@+J(`xB~5p#w%eFJm3D!u;VZW#GpuB0ive#(ZcSy)SAQQ*UgOED3&SGmKda!#{Fq1BN<L==01QO50SSDy7`;BK+mm;`zaIa*m)aW^ahuyFLt?jROastlPb7+-eC+rqX=L3nEvO5kOYEv4gsS^zanFaSZqGmZ6OZ?{KqD33+a3s3-bt_ZvJmim^(OWXxHP@SAL>iD3mwzUD+>z7TSuSb$X#S=4P7g1rktm=@6$EQXiTIEs?l@Y;OxtGe$sSDGzNMQ;TLXN;~G-QeP0#m4^|dAxRY=*<TH<q^TpCq>UX-K{)!ik=toqEC`8x-??%|5wSmr#SVkfo$2cT+o@4SOIXfP*-7xk8;0-nc;3Xi#Q`tt*MA@o83a6g%>x0%%;3eRF@Cq3KgY&nNpO9%Kl-~$1={`rFz-Ivsh@J=w^+y^bf+<TKnMRZZ<50#)6l%ntu@rgkvm30;360HmAlW-+NX;IIz@}fM??pWK49VF|Ht>NBsj(*b`mLlOzcy><FI_;o`kew`yt%b&#nMqyK)aS_D)WXgXa*wI^8I6&e~!KappyGI?G(qr9>$B6q!u%2g-cSNqaTp|gA6u(TbhyzatgZAQNvPEwNY4P&Tr)b@fc6<IrZ^aEya^y{IoQm#v5Q>(0jh?jxm`<3uA1zqBc<jj<KNmU^8ZO>03h4(1s5I!YBk(R2%3Pg3^&<)$uvfQm7Xck<*iwc=}Hr>Zhe<RmcB4{Mm)T-UoW}E(xqkgxKWhbN>ZQV+d)NrwPUIO7uK-4sW49Dv4K#kpNZ*;KsHR-98p%!VQYom$bbS-f_l;s+v`*zV>lhDN^rI_i_9ubE8qWb%NAo3`iRLR=t2qpktkB`mC6i8`FdJ&z`0hN=<PqGNg|2H#_ZG-ZP*!J(!!A{#=7fLO54V)P{o3NNgZ2mJXKjN(&R~jv}qGXJJUqO7a+_)QHoHT-i)0EQ{i43{oQbRZ9nQw{;1q?BOctO5@5Z*h?lL<B(I5wBo3W$jPEF<SW4vm?reOqf)K5$p`_hRoNAoW89Q(9uSHAZ{MzaV?uG!7u_2<z5s%`<lZ1OaPy)5xK>Oi#1HXskcVZi<?(?Y4m00}9pMQd>WqUl9Sg|xh=wc^jng90_~!Y_X`7=<ZXG^%P0_y|{(PKd9Ek|vmPveG>j?h-Y2Js71+l4vYOF@B>Scp%dnRR4MzSk>9?c8^qX>kh6=|8a*odikEk<$=t7mN0zF=I8++IO3Ahb2GGGixcf{ZYEcg+YGYo)PZ3`f$gU9|$6<bg1$-^=SbrBw|cq6G@nZBQakqO{CxWHSN)&qOC*QYKcQI+>8Wb)y4rju+y5;-h#^0SEkBmoF_`Syi%2;~a8NfEH)&hzMU*@A;jRFAiMr>ycjaF`p#YTY8|t^peP8<9`t*r_$a;J;G`!+#Po9ajY*o86I3V2DeO*3)lbh^LtgUY><&vM+gYbG!|;2$!4Rm);5-ygy=S1q{8CKP*k;NDP-JXv14V>u|VhN2h;7X2#jxVgc{CnFPs*@%Y%rqn&S!DgmqP`6uqu$W}5c4Ij7kq>6B!ujW8AzF*Z6cmG-t6Kd;s5_183_lzV7cFa60fYsVI1hvGyjZFfVj8?B9AyUXC)+h)KDxuVKRm<Kza44YH})14$pBx)8_&UR3Xj498^ZdexI!JWN1T62x?iDO@mCZ1~3E6NdDT1Yw?iSsU)TpY&@Y<n}CqMTw}%hkwsJRi}EOC)1jVsZS2c}VlYym8x;Q?Sq9Q{%IlD||!8BFx4-?_n24=xpsSe(}<q22L8<#<p!yWp1ICWNN!$%0?I4<%Bf!?%!14w0Q<%T<qKhpCTGqyZGdH{zrZ-`~~dY*1y;i6cMh)Jlks<yCE~|#=Ui5A_DG2>YMBPfe2xgsmi_B(x`S;2UY6M(*cFDTP-_$JMC3#DSe+pnOHd~-5{4>6;zT44<VK(7<)IFWsA~X!F#40s0fm>rhOi-n3XG&{g72#k=2cN>ATGwW1cQc*rA9s$lsExI;C`Vz^{;MENu_0x|LDWTMfffanFMQailSWYRQ(XiNAR@CzB{nE9!@l3b6}w5&-shzx#v?ao}beE8@}UhmPyGINCUUQSR>JM8eGJkjq!$hxRB3sFpnkc(`-H{T*E1AMSD0jueN#tOS5Ff<nSk?k*kw1!W5yIS_do6O12paGidZ_bf9dA}+MkxYfP$T`I{VVtho5cpKuT(QfVTt!qKrXySXg&&;w)NM^CF`#-*2!*_tE>^Z|1yfDZ;Z<(RF#@9umM=#;_0YN>_%~Pei_qTc>R$=y<e%!bo&4+UfxN{5m7}xV%@@s<9t%{=UuC|Lj)6uJ>q6coCiA$r~k8!=}v&W_X#djzlT*)c+fb_V5sWWR3kmcz{0m%!6gE0<Ud^<d<8f>D-Qq_xM!P~U!0ai(*IeTFK7;srDw>Sr)WomGLIXT+Wb{9%3j2W9nxU36YuK;aZsa~*sd4mN=@O@KiEAi7rfTA3%&BYwiMU?|)mAMV#G{K$`hU~R4V+^qUHRO`@vHn8fJPdVD&uVrm!A#fOo@s{D8nF*Bm+VPcL$a7orXh0x(dU_L4n02($8^H9M(RxORf|PD#fds;QHrXZyDC9>Vz8)JkS91LD@=bpBJD9OO%9LK5-QsTYfuN)!}tYBUsfRMOkZnJ@^#Ydv(tQrs$x2p8Od<;YD}C}snEUD{PotFiBZ#*1sexX8+0xa(521U8JV!X;)Ur|zjc*V15p`TxRolHvNz(iB@z|+`)FBDDqECx7A41sZGl*BtFO}3dRutaayU{cBxNIBaXlm^R>_I*i<XESP&^cK{MOK7n4<NVGX}1tKWySK%s%%oxlP!)&wY>VgtATLFq9o5P}Z0_aZ6N*1KTus*{)0vHXYzw-<r8Iq%}8-nLK4f@uG@0Rfc=?eK~rf@w$cYDcVL|=DNL^8144GX^s7q=F}e?K@foc^vt`VY$u>qsyT~M;uMi=jnKeuN+ULi*ncYY(c?@adqrDTl=V$tHFjDhf{e6>#e^dPZN*Tm$jFARS?p+HBnQ9C4hoEzVR)&XgV`uWgk6P*ygqcl=K?WRy}(LE@~3i-y?UAMSo-@8R_C4+%c5#NaP#)vy@Kf^uEkoGex7t+_Uzwh(p*#>Q5*Xmcv(DD!Nk`e7U1F(1aqcEcpB5!0;HBBK`8y0icESI`H{+&%#0%XNZe^nvWwvg#{{$a^TPo$z^!#E_xQOrZHMpQVKvn`CM-5RXyoSaJ(zIAi1{++)t`Q?;(v(4*93hGGsh8QPTCURxtc|f6ikZl25eFcQzIdotXN5IiY=lpIL%ZB;kvx4!<?ibBG{b~_Gi}6CJ^A#xHl{EW9{0JJd7(x>R@%Z+XDG3>SAnqV-+knIAzDqCi2L5I%7>>#Rcha+79sTR^sSvvaPw#(X7~8Gss8v6-oPw?g?ED-VcDH3NWZ!B=Pwsu96;?r-4jqN1I?vuQ#xEw3DtV-z>(<)Ruy0WI~z$0nwb&U5>V>!Y-^l?RUK^(U2WHJiwK;x;rYifh<FtrJ;Q!Rr5FFaaYJFvxE{vPriejVvF`VbttaF1XyL;x0F3o0hH}iK>H)!vmZV<kK#rSfkN`4Kz?$2zsKa9wB6nVL<}bLd)O9V*a~@%MHjz&1Ka5b_SHik9`a8P1dGJH{_j2!3(L5ySpGT+7N%R2OUCuLOTp4or87f%-7#-he3+iP>t$AGM0bz4SVj_Q$+(&mcu5eDVws%*xJgg`aJQF(LKnfye!%P2h}IFzJz-~AXP5rlr}(^nsuFwS`w_I1EABa7ncJ&$x&|Clu@$Dld$E$-A%31(I$d%~uf>*c7DGDS$Ht(HZ9fzKwDy-4mmD3bcSP82i8Z2*Kr>1@K^&Dy*7rHEt~Ov@JOS1nbAFv%WSRC$Y`-u!9+nJxSTwI!gxTSBPTykvymqgmwt^?vk-{}lS-_;-Pa9$DlJ<e>LsdD)<QSJJz~o7GyTjpWO33A|Z;|$!#SCU|R$R`M_A9v_xbK-0+UCFFX>H3O$@p|Ga5uB6coN@|ScT%h4gxt1pEhi=`n#Vx)b|*AUw~Pt-RE(7<nY1JdwM)_oKbim$=y*dMEgFLuVc5++I>F9FhA?)fSSJg?9slz`3^?H%m@0Ek+6+9Kgs4{=WMIko?*;A#{{}1ReB=Dyhe$+>_;Zh>`b6tBaVk*)niKsRx_eRhK{yDhH2ZwDtLkk^vW4Lm{~;v(4uNAX#+WBa<K<;;C`V2Afr5UiQx`>CW~Ln4w>s2Wx{grQnO-S54PD{=tH`X?pObY`uZDbQ0l&$1*sGeAKhj8gHP%k`;VL?=sVoWZ$e#T3ks5;*ovDlC#<dms+k<Tj>JG5ccw$Vk~UU#B;et>qU$2LbKNUK>@bn4Dmf%FI<=A!yH44g4o1}KR(bh$W{#r4eIUCOlXX4WG11Ah5|2}A-fw{mlYcuk?y2I8V$dBcm9^nHD?JW47Rk=agPjPVN^`~NFQq-32XA?CA8tHGmD<L4QG-t)t1jppXtC^(zc{cC21$rG&ZK{b52982LtFY>=~TkERE~gY4xx8MDZ<UQC++|@L^fh-rSVGeA{(})9af~4QZ(UTavfp6@=H$uz%LTFY;z;T*K*d@vTJN=;EEeh@Ze_kbXA@_YKI==t|Ykd%L}RW=0xp6?(p7jdqqf6@oIrMvRSy_I}gbr&TC(-kI-*FG9|%Z(fW|SB+w5jeDoBWin(Q!&16F`k(I4JH_#xr4}>HglPo=L)vmo}p%fd0V}kI%@X30yE_)F+#Yso@=N*|?D2Ch=LlW`r0K!n#qIpGMS|j(wG1%psUSJWpQ-%$?a33#q-c7o#>^xHw{b|mxblPy5_WQ4Y<j!MFhG}i;3y{vQN%801w&1BI<uXbg%3xZ-=4B2Y4d^r*Omy1p#F;-QBM=HVwTy$bT?T~W%%b7h3i4O4gYz*Aq?PN@W8gM{LW_NeZ&~Yv7-9OodzD5ll1Ol*kCo?4tzQX?+e$9kwFgkV!WCl%Q{KQ)hz|ahpAzXDqq6Fb)4a~pyr1(t6j3@#XI@BWxir(q#Z1qf>Gfo$yXR~do)y-|Gkqbf$C>`mev5s%eo0fN=V!O%(qrf^&hCm*4L-Fe7e_=RY--ywIJK!=7rj*%y>-H!AmKafsvm?e;wy3ALVV}boEH++3G_XUN+Bt=mbgyEk-}b$sR(UHVr?w2Of^nO4;5_N2W&+T&T6OnK&duxPvkDc<KD<;As#I^e0^rPo-QQSoETf2Z7V7nk`Iza9=rDM9DzU$fivTI{FUIs`3T({t1fso2RR^BtKfK!yCNM|B=mGSqP7(~SiqW{RYw<3>6jkUj>A`Qgo-b(T3((PP;MsD9kJVy#UmDph$%k8Rxg0$Ft}=K@DZ7QOiG#INf*H5vL0vLdURJ?a+bZth2rB>{!48jsN`04nsHDwf{5Vf1??=I-ZMZb38f`Cc}#6M(qd3NBZ;s<C*~}3`ArDnLuzA}8R%)%qPpM=Me$rb;_>I^kq!CqkG(p2f!sV0SlnZ?GaRr`t@d7~n^hBthf<Y_68BWAE7rXnd^v%^6>o6z!L<8rOE2Z+;|xgOD~uWi_?hn07mUtLq>hjHT|4N78WHTeA${gUobGtUR>3dgbYM-9|KNT6*^ijlT-RI&6pM;r<g?BDdJq>LtJ0`uTZPRJ@cGE<4%mGqMk}CY;gZ;@?{Q>|o>VI66O_=TvR`nH$HpNM2?v0IP0Gmu2=dr+6TqtrG&%L99GJJ!sc6xcD-W8@pt{^Ng$#+}y9qqVIQXVxD6Ks$HOom*O2Zv+8^VeSswwA=aP5qs@mWC@=TC4mw-bm>DfF3gyNqZQ!tNkj%gyn)_7Hh+vJvaUDKpam{_?!Q$6rn@J$IUwM^3Z;S*KaO$jEkzk4Htl7a1Zi=l*+nZPB{c<}oV^hcSZ|c=oP5i;vG|uHvK9Y<S6OHY{O6beh$L(`?0gwQk-pDa>d5W(TA+rnte@5IsPh>ah4UXRS9!8MSmi_mZh17Yo-H1vwA}Iq?MZWUvb^Dd;b{%NQvtgL}-nW3<EFANkXJ%>Kx$bgZ3uof+uO{Y^&61Pn`F?=$mwxZB^bN(6AkdAi|XMiKoGF;DEJz>`G7!|0mEndBN@ZIy56B}BNlSM{GU9Z-7}MYVR^>a?&59KF_S-I(syk-7%wT-iAX9OvG~r>p(M5A5Rs9)X?Rbi%J}gV6lcq#=*jY1`u$_hTe`3$~3JsX{1hWv5L+wX#%R3uv3NgGJ_fkxGA{TNl-haq}SFLeWf}bpM|@f=FmS&%8v5yhQt0R&+fb=!vqQw{hsG=8CZ0TXsX%2GH7EK*@;MJ$20;m*y^(HQn>dzY_|FDM4%2=1`Fsa9J}ezcL<FI8~|wi3J%|cZHrG*4-%Atg6aI70q68&htUH3EQEb$SiRG+yIl0`jv1td7QK3BBfQyzJ>P;<z}G>0DRKU5tmRcGpt(3W?r1(0CPnQ$Fg=3LGvAR3<@5f=3;hyi83X<YTMw*GUPQOPz6I4yv$5#WoL32J9ZJ-n}ke2Xsn~<{BI(ylh$?pB?7^Iz5$d;HeFN8YG0{fbDp+klG)GHpVHIu*2!fEeS?y;UsCN~hwOz>J*~95KOd-oiRrAiLE?TIpx5D$^fbl2Uy;}w)}#@6JWJN;cqWWT>oa{K&Zk)ja42#^^WaxpW{1O(PgTJbRx$!w%0%M}#q@TnV@@u+0Ld-fh$8}eP<J|eJ$~hi%wbw@d3hZOeATxj02l29+yp&C3Cg6dPc5njz3?0F6q|b2Wj3o`?CDDTm=-F%L<{xwO6#do%G&T5cyY011)`@SR4IJ$V%taVkw3~}n};egaBNd5p);44T<*;JAr2Q7TLwO=QiYBy?QULaOIY`>poQv=YwTx-6QG~J6MvmK^xQa`yxl~U*<N+TZa`kpg%gciD2p6yYX8mw`#NTxq8L-hBmh*VPw}e9nmdrQaFY>tK*1(1h+4O8D*W8MfHTWqn}|YWUfIQAU6_}_g8?NdCR)oju)hOwZKVyX_(=MPd)9RjmLLkqitR;45hYa(NZ-Irz=QOZViZs_g-KSKLI&ARE+Qwnzz^|K0#<c50^C-8n$SaJ3}uXSA`TTBlL7T2Z3cg%{B+7VDW_RXNJH8oGiOzN!;HXMiHA&Pl9Z%&dq$DBC~Yh}ElS4s+O8?Fmh%36?rBwVZ>7mc7|u83*SU%)TMm+*u2HhECy5^c6G3GYR&vR4BNja}R<x&3#$QD?d>IJKL4+ukZ&q;AOhPPVDyM=t$Zuy%#e;J6EpkIiM(4yD4|azdzB*P`3|&iOXZ>6Jl0CwY62M`E;do{>u?*>kH@E)W*-T1au8%pA5kamZ{+^&(H{YNpDZsPeG{%?>s(Q(H896Dv#95nLs{Z^f%&<QdekGUh=k&mwnH?gLw)jp%@Q-uhNrGFaEftNpElu51Z5LLCua3b9`M_n`j(3Rr`OZ+~ZBSI!U5eNgj_^;Cl_AZg+-*SQCb;9;b1hHHiuKyD^ut1JHBVz)Ghv+bs*uUiI{3@rHQgigN55>UiXNW8lBvo{OFyEC35f98`J@giLRygngj$GlyG>H2o(I|UL0K>s8n>u2ZB(*p8pquHS1jzR63adBGthcku@(&>?NNqr54Dz5o3rDqoxGokuygsAm+Zt~{fnF9S8(IKylS^Ca(Ry}@|v#c4_>w5Tcf(a2rW4-+|lz#iROQH?T$!Ki)&yAb6dEVDddbUUtY3>B4G`qQyNEBgIW)-Sg#8!w>ygD5fk2LS+f6c7uYR#EU&2yBVLSIX0J#gypY+JZU`HC_T~(y0z2E7IH3ps!UBt$9E&<{i%$@#Oj2BcQj<8q=fWTCc+%_<P~Fg}D1NPklP0iY9~oFvs&-2K!tY98RaJ&nbtoPEWog|J`zJmCR(SV<wu=fg1V6RJd51T}6Cl*4$*Ex8h+8vb!St8oR!#{I+<tV4e*(txECg!O7L_X|ezZe%^0_X}S0cbWsqS&gen%I3WvFXPtwQdR_fFaRpF^DgUa%*e!+6_gwXg^CKBgj8GUM)45r3GYQZa?s`YLx9sY)4WndSO@e3jkf%1NgxSOiS3**<N(@~i5JPz5`vPqsmwG5pDstNM%X%F6wI!>f*Sb*1RtxP4q#*^6`i)IqV)$^YMHSHxRN>$@ppMX|y{a%n%5mo&0)snhUSBU2=g6g1}=c?rLmo|asdBqqnWlk8qp%Cg;`SIX4g)W~c2`_>Wkx~F<sO4(KXEA?^}+v=%aUJ*DxG`*~BqIcEHg?f2?NiTmE>Bf)#-A`{9KZaSSmtfZQS;FY0QJmkyD1HTP^gHO{^RmS6YZ0&L&628Z7I9p<vYf{ke|@=V8k2`boBt;;*6Vz39p@)_qGSGPf?59?Pm;xbxrDfYDyR0j{~CTqldQ=Wmn%o70K>xgL?m2)A3+3{#Y6+<P?YbkJF`F=fg5f=^S=quq8KzdIBt<Y0w$laKPP<aR4I~#Z(kgU8KS&p-@=6=CLdHr4eDn5mG6Ep)yn2!4DbevL<b4_{th1aI72zO#G_i}0AGM=x|?3a4~=#S+<G08McAr9qPxsOS_mnBiAf!;6IQ96!!^EoQfyKw4ES<Jr~-OcQuoO>)Q_mxKL2j|l>ujNV4u+)g&;5ig>rY<89uy6<hfu&z4U~?!-l%HX!B!s`2=U%3z-=TMAGSbomrFXm{!EF?Ajfssi}<gE!%PBzy72G+jCKq%qEa34j2q@0@duL%x1~GP>vP({tL;?O>7ex1M2I9SCR{S{v+XqefK&)kgr*nB)4w`;*g-0^W`v(oeWd1D~+h_vDm8m?wRC*ko#PC$M+K6E2eDsTs@In--P$z>y&J_ONQI&R%CTj9U=9-bGTVwt$!{2l{o!F;bEK03i6U~XqP`QQD;xEf{nvn7Vs1}FhD>hK@q$ZiGfag!|Y?t_Pvfgz_E?6><wh6Yn&D;QBV$<De1W;NBTiCZU_`w;||l6V5YufjlAt<MS$M`EP~jk4=kFSXx9oZATlXL$M?+Ute!{#TmOa+&3s4SNZ9*ZUPydWuPVF&?rz9b7m}}lo?dB7&9sjWS@43$JiZm)T~)~(=#chw_IlMoroX&bF7`Im^`$hc6{hQ%g_;+cR*_s6h>dXm%yYFom65$+BcIR6Cev{|%g9E`6{{>|&&baCB<m`*tSgm&+)<UBCuPs@wXP9wq!t8XH7H<jv&cMP7tBf7f|Nwqon$Z(e+l=DVl*fF#4;nB<n=Twoot7-l{>~?Go`y@W%~TS>DXeH`JA@q|8ki|`}Pz|JrXB<OV)cqPInx)zA+$(8?kfnbXv`<{WM7nqbbFc>1|&97(>=r{D?cL9Jh|KxN&A1Yozvrp9a`*j$uxN>WacAA$evozFBvT`NMvzk}E%fBuMvJa&)JtjXsM>3FjTXjB!k-B!fj)3GpaQa7=UAVlM<Lf<@LO2`v;~oLG4fcVls2=i<(bH_pQCbtKcVB*21sdkJDb(hlnWR3bt?v^J+Bv-k32R>tJn&F98D!(;0%f3qL}kL{=Z!9{tj#^*(A%aK=cV9>ikndKu9kafxbczi~66v#tO82`f$WtladyE$Q*%}bV9SdJ>hhjnUeOX$io!cD7!z*z;WvlAMYMmMXH26b=*uGC+*6-g7%Cx|4e`oo$5Vbr~AY_)5y9YGwc+~3*d8(5RvE16}Kyyj;jLOOY6hirEsh$p&DBmx6^CRK8<&kYD31UgR6<UUi$GAm_d`g;oTF&!+lCs!zv*jC;=c7BtdA#wzENeNV1cD~4Bozj3cf(F%G5HkT&Dp}|*Z4((}|HM02i?PnWK3(RbczBPjBlU6RnA*<t;xWo<Sr(6xJJEITxRZjQj>vQU7y!XK>5*dz8AozeZKfWTkg3h$>?g7}wj85L`C$CLqi<z!PbreuRY+z$A)~Hac}!q+D+gldKzfWb#$oS8Wy+mBj$b$`(`-#CW;T*d*Tc@EfvvO*>dNeeD)`%<VK*_m&K_+jYJ7G#p-pgv*WhF~QN=&@Iv*P9_M(L=&W!U7#jCf%!!ui9E@2xH{dO<yCZ6)4o$MwSZnVhQG65~`xS?=j^5t$=H-}HX^ZnOzh1Nur=jrB{;n$~y)^giQ*xU85J}X(zmWMjCYn66ZeYPiQp&<=C**bN5VX7nLk%nx%M)(n2eV67rT;bixB<BntP<#70y(8$_wAR;w<aSJVvAL-kj$i;`pU3IVWXcuhHu1tMde8=+@VC1-0gy(dPa)KG%b~Ew>|rjm_7tw|%lTy9a5CGSuY1%DvuQm3YWS;h`X%xz9Ade5IGW>ha{10RLy?fb;z=*oiZ5BH<<ROQToGhi!&Fd`73W+BC-7oeM9CXKn*om<?>Nt3o^9jS&EN+AZm!tfeG4jz3qXuxWN#ZF6XiigbF6!AD6)j=NQ)jq`Ob}RD+~C8A?Uw#%gagFjJw5S{tQreYef1-Qj%qEE4Li8AKyBD7V6QC+{}E%M98;a{O*ltD3zDOLDQQJT0ZKMKmN`b|2u)r@(t+ppmw&@lO}`2&Sz0yZm*sCfHfq9`=QKVlQ1VBS(8yRY$I^O4cF;#MCI33mCpM6j_kWOPJ8;<i&VFFHg=v5&=|Oh4ZciqB)AgPw`Y`3wBV%216#QD{ZEi33v<M#g=xPXaul*U&vTPg?mH?YK$p@37$9+chbn%_Zoc;2xEVCeSIB%`Zl?!sf2LlQf8gg?HMXrU0tiH7@(Lo|+0N$Q2JOTc>(5d8ZDTx|#Yj^7$dYFS{_p7xt`iq1dx9GWgpWXx5pC6R?1#`Pz}AC&0x&b$_1)maAJ9WAom7blFLJTaB~iA{NHkhAu3!+3@&M`n%G@$FvIdx~k{l!-Ko{!u=yo`+oSng!J{DN&VTF7tQilmh?<+b+kl#Cn;&g|og^U#60nsPrkeJD}FQC{ooihlRp4{jy*tCf%F#_E?gcUggI|0?Qd({gPpai{ag$x=(Ugi-9N0p|Q9V1iZ{BfdFx?KL4F9LS@k6*V4JmuWDCMspZOuQPJ^BhYkgKdQ-P-fQ5z9r+C;veHMcxq*mHvo#C&19x;R$6M3??Qg^*fR}}q?^pmU>+!I2io0e*CmkpK=B`u3re&L0}BLZ8Fj!Gb5SSK3?bKQ51Ve8U*UNJ04Gs2xG!4S+!<tphw&i1DP0YA6#?5a^QFGlOlglRdD=(?W6Q$WJn+SfxuLklf7%DPUcHbu+t}Wm9e?}yejn5EHNExB2X^CIpL}~C-+K5>fPWKweCvt}AJfPAnBL>^`YzwrZ>8BE`tcL#hc`j}mOehRyXwdLq59Ub?{aN<_TxKU`<vWaI6aa+>|^>!AM2|>0t2Cn&F$l|RYOo+RsR^@;p55s_^S7XiFoAG*PBoEnl8V3h2+!Mq$199ea4eNcf4P$+t@G*0;VYZMt^F&Qhoy<cyI>7b)Bc;b@&LCOzaS41hW8*V7Fa9(qQG>>M6@}AZREHlB+Oq^Gwd{;)0m+%Af$E{?f^xSGH53>dB8J(v{2W#1r@++mj0&l(Re%y)NAH$oZSJ__+mp>hTig0jPv!^t#;s)$r<vnr|q0epHP()kXH#C^6_8UOFzK<iw;l4&g<IFW!5f$3@F^!y4wNJNB*KwAMOn?rGx}UB`*Dc!b;vc{653h{3@26mr53h~%n(#Yyx0@Axe9pEqFswsqQaK=nAwCN0Ntel)L@c=@!&$LJ5`!s$PqgaFgQ(n#V;WgEfSTLlmB<BAp{xD%D?puf!bI!Esj3~k5JjNIl<Iv(LGDcH^rzVLealHs{aTHikUHn(qcYx(gtam3FK`s>-VoPG4Jc%m_vTe7(Dg%eU+N^(;U$2Tm)xV-9d%j1QII{xnC=N(#`7YFq>Uo{^&w(xk6Lp&VMi6xxL&&7}P9ZuSro^Iz0C!|)y-A_Av^Ze_{J%{seQ@d@t*th9&gXgdOG1V=d5EhTR^kP4s9y~U6Ii}Q^p)on0zNWA^L6nQ9A*A2)a-6!cvX)a;*8U<Zt0|=`#>sD;LKu9<OIUx+b)1=l$r&6^S>s3>EPC5%h@Ho#qgYdiZNnyXpcY0&&`E5|;1OH(%sty8ufWbMYlIN&gjJ4p$g3@AqKG~P&Z1nUD->eFd|K@pJtvxbPmw9BbXc)@*&cx_WFNFt4*%pw?lUsku2zl4cDvxPtt|fS?26V;#Q%CHC6rSfTJ)are~`y|4-taY;mDLheKxGa%6?@`BMUv?IUex4usQma82Ci|<(AaK;_%)C62~Wk-B}=<d>AJj)E`@bu4m~X_NzOgMNZ2AS6U?T#+lX^N2Zx>I<pj4IO~<TYNC^nT9H>`md4LT>ksP~6_nY58JRJ();Gc~!%XS`TNc^JuwiHz{S@z9ddTa!Qn2um0R7=_OMs4OFg{0{dZ|sl;biKGJzg0J;biI!ga{?C0x3|ZU=64mHZ1$nQ$|&nV3-sj^y2M3fkK<iM<Nq|;<M{00&iYIM2d*z#pJzSrQ4ObMR14JkOtH}$cR&4rQ437#C_;hq@6HQ%-L%MI1en|I1nN<_xeh`{?Gi>PTTru+Jf>8LG~k#&Q4ryh?N2d3+A=mDvOVwJW#g-c;hjPQ|fBUJ0&cq+rvDUk1XAiQR}el)scF7ZO!;`_@BL-cHD)16{fEUAAKUne~PC8?2b5udMSoY%0=hrT0-GQlIM0p+vM7L$+QzVlQL;mN8no>sGJ3kZ=~o1#Hms&pan`*siZq5x{1l}Lvk(}0=~o)CsN%+V8~o<LdnK<>t3a|lB4!J)=Eh&5!xAKh5sb3pmtuL3MF7we$~M#tguO$=Mt1k%PtW3CN{uTM;fQiF&_*U-YRLiPf%Zi`+=snK^GzjEl@_M&@$xWpL+3N0+RwwxdK|^<~$87s4#gKE<pL6t9gOuFQ2`#+Q0M8DCry0jS&ZFQt9|;qA)AUdSg=e`ZlA)C<#b|G6#WYS~Wm))!Y=2D3?8pP?CDIW5PQ&xg$>iuFVFJ@Rys!^6MZ>a<uhG5DIFOve+pm6V$>mq;3tEqy5`hlg1=wzn-ZDpdsUFATk#AxS|X_imQ#-F^B<KFk}%;;|MZXtT92(7v-5|;+M-nVE5=AmaMY9lx3hH3+NSv7K@~GQfZ&aWP`38GhbEIEv^KSR?&IJS$}dyST~&#)=fkQuNQ=MUo^tHsS(y$yVu;{u2WpUFJWC*!qA72gmu=yTVUM@o$ENf#3%g%shA0KK62LmsBzYvuw*yRx(6bV?Bg$I5t9a?@V^#qU7}J0p!a#^x;QPF>$*rCcO<VXGkKlho8qq{Dm@a!7aN6LWDUka0H4Pcc3J%5FSFQ1XR&jeTSRu<g2=8ci0n$M1}GvsaD$Q!0<H&g*^N|RRf&VD3lKb$i5;H4A)Vdibatwp3Oc(An?Clbe1n2M>FSiuE<QnL_Y35KV97r(^i#X?+n*w}<7VnMOJ-lBwmavwE9bm+zzSBp!S7zCw#%QE*Y3|en_~AWZuqvd3p1E~PCUTh&?=c_QSnewo|KC@0j2euC}Xk&@$z~ZvwqI06HzH^k9%3=Iq|>_jV-ONG)yw;x_CW1$YW}Gbk);dx|v;P0FO6Hf6vt*%`U25>!GrAHB3jC5yYEw-KW(qV4>WIfq3X6=SXEb5x4=ZsT(jL_T;a#Gi`dMHGyl{msC{Q+GX*rT#K)JL(1vS9fx3@{*$i)+Fk>aKF~&hVzLQT^K=_(ZdBDBxPJR9CcN#;Iv_)+31wx*A5#~*4p80E7PXZfA>B=adwpVs>&jXmW=z_d1CQWwqaGS;g&pvlL<}b8LL^?u8thoAD$-J+<xz_k^}2hdBA4Q&X?eUSo^)UhCKNvCkQdhhnQnJRHI~YIvTmV01=L`NlFT?Cj1jz5@phu|J;+A_%s?LRnYD##)5#VL!rKcbs@<wbY7i(B*dAcvO<2$m&^s_=`GBmHm-&Du{{Puigxi^f+ld3U<A?!$yJGqFKGvOThI3)cBz+cx#UNaMiT7mmVc8QHCTsL|Y10WOT}N%JDswywsHDLczi&Z9Ei17nqxCkZpnKu^LcJQcES(O;IpV7aB&RZM7^^)Op+b9vYyBj}CF`@ttQ*aMtmwH(br#rGRRWfYk$aB6at~pUGRK4q$|}<ordbaeB*wF2!FY01&=jWKt+itye;V#0r@R6`$~T07L{BPEMcb&*j<X^m{fIky5d~$YCbA?P`k_;tjG>gGs<>Gh6tQF47J3ry0JrQ5BL}K9pSeh*Sh+GvSo%shiUzZd>F>V})s%E^<?gAwRGQ;rsp;YroB{;v!s;YbO%E@4rb;~J)L2okF4+Fc8Qb3@VyR9b>OqVb$9li1aZA<5+)@l;h+c|2aVCj9!NhajxTVt5+)`5`{CkmGN;Lp(nGsz!B$i@hmYjc6@MzUcE&U?5l$<JO+)_IcClpjW=|xen;<^<Yz0}#>>LRfehjjCZTPl4P&cFZR*@|6{q_{q7K4ABMEY+LNEeN=8U4A=vH64wJ;*>8)f$MTdI*cwJodKCtF!e}`=8_xFNMHm*N2Y4-(=qd{XXYCYk<h1e0x5V(a-&mI1w~sGyrOz{lJ=$~N2UAb>|*Pbs!e8#XUAdNRjKddF>Qa5`4~}2Xke6JC(Ax!w^gX%!Ku+{7lFbKxnqUtta8yZi~Lri$v`%6@Qfs9%4jm!oiX-t0-@qUX0}-qJ-X=NSptp3DcQ@nOWOD6!e5NtZ$Um*g=>nu$;trexvL#me1mm5z2GUOGTo7fMjqQjfvQ|aO;iuX%b*8Z{42_7_3WX7AOWKA_Lw9DkdDCPS4Lk_QMwR*Wlar&5=^SDg^Cktk1c$u<ydJTX;@NQo!6|&QCn?vh^PP1T|!DL_WApyG;=Q!66pKN+Hn*`b-_W^YEme*>&uW8OTnVI^Fk<EKg&UTLr;*UqM^RKvY$X92-bTp@EjdvZ=gLWIg(JRma0ApHUMAd8v8Pnnyr3<VR5XgS4z)TsvHSE{?XT#-TDbKpT_%;AHsEr*Z2HrGj<C~>b=a3J3NZs+Y)Juvsc)<2S=>^H{FHeMi92MIC4vF1A70iAQw0@-`nm#ZSKUP$l%x>73koQxsP^2x+i(2b<%z4@8Z|Le)NWZ=b|gL`9b@q6St)RcihLsmW?)7fb6+|=eU*!v^!OO35mh^M&iQ!oyrZT7HY^UbdFhO1B=Hvw*t*<5jWLsYU)(}P8nyjvomQO^8~5pZSGrn-MpZ~!(N;K9ci1Gnp<q7h!5IM(~FVmdg!3c8+ga_xJks|g~8~C!kQL0ky?(<R}fUBLkCil!j%H96Vj!_##3q>D{md-a80a$l(3PCi;WbLBLA=VH^op@@^z-zoY4Kj*4P>Ma(&4f%gq`~r`A|`oi$cpvc`6FeWYfMU8Z05=DlEwrBhQZ<++H{InC!JhM-r|e0JO-oS9;(PuR=t-aTiEl_yNG__QhZdA#2L`?nRBfjGCg%q-3k&Suj}tD?m-c;YeLyR&b{Z8EHh3r>O&vfmcf7MgJl6-1Izz3}BCI+L+8&#K`$2WS`{Q31@t+E=N`Y$X>-&kBVD3vQ(JC^VzE3|y)~0T*#BD=1SGPdSOmu#nIbL793fD04&qsLM_jk7FxND9Ys+=in(pi-E-uNaM58n$8UcF+c1qM+i>Iy^<Br1y2N`0?eG0k2Xt+(<$i^ciA`GO-E<zLsw)E*+_EZr>+q9x0Xzw`96#nnLbTwCYW0JhD@Ju3B&5f(5#e0O4?NnxsafI%#7siD-$tO-0Qp*+^?kVRn!QJxTmTRI{B~*?c><UlcTf6C^b3LG{?7J45_Rc<`U2*lPX)~QW{{6<6RhB%HpS4iDiprG6mMzW8)B1&r&p;Dx3>*ki(^|rxM_AT3Kd<^C*>x>T^wbE4|C3+j?vOD`|oR&VK)40}ogt;aJKf%J7vJ2W_G2XcCbLHcPQeOL9)AqOSZ=a1?2?OHL~<1<IcZPT4{BQSNxS4Pj+jK^z2b%#1kYB%&ocuOdQ`ZiX^txYgsOQC=A4QsGaJ<cn~s93}<caSno3fAnJ#>NsfW0-??zcT)cfDjj>?t22rXd9KMDs{JL6FYP;5(qdPv9656pwTf=!(RoCovt){=>vwxfpHt^e<nDw!M~keuHU{7?=pVgHx4wOV!UF}xntnODs%^m>xQ`HPP9|&4j@1Io-#PjP_U~AAR>cOp%j58*VTBpXcv@vNAubl9<w|5XKBMp>VR{Xs?K{RAX47dH-22d_1^)@lVWS$IJOa771G0x3db5w<CXPdDzJPM%@9U<}h^L%2Cwu&W1syq~$k4`$ve9o_vY#yeo7mPDF<HW`%Z&ZPc*K#~@5qfViVFb`7>9-{pH5KVyJ#+Hy^BIeV4QMtGs>RghU8g24Q>><?cNO)aDiO&)ARiQzSr(Jf5@$t4d4Uz|M@0dVZZH=sNt68k9;yz-~&~9xj~4x7YoTfZ2FGGhLuw`(nB)PXeQNBu7{xgFz8DZj=#aK{y_`A4b}~fVCsUOA^5)B1xgKu9piDEzQZm@+wNgFn8^P;sZl{qD6a<@PfQQ)Z?NT=xc!C~gQO~lBpOag)&n>=5#K>Hn9&?$BkZ-|*Ex<-sek<S0jO~fK-s<TY|2m^8G7oj5MHk&<{0{{08~`~iouJn*ulK-7-i}a9jb*B0P_L%JVQFbIP|C`&-z%3I03nW3D%QG5%&a>9hN?vjFL?ep&mPPl^C|lTMtj+Cd0s}PIPJ?T&T#^&hDJAB1y(sS%ggj!G;OKK>lL{sXDmX*bMZAhszK_3Y~&f2xn&grKyX8udNb8Z45LqU`1y-qj2DkN<f*RRSBW$o}sppb-94}_@6$y@xR#1o*MrW0%8c)T@;CG?Q)HmRPI1?XLV})GZE(umlefitYTrOmOt(`xy{dTW-4<Pisam5Wrkywd}8(!{Q;YwSwYai?m-~=NZYNlvc0R{;RzI0d>Mu12(BH?b<_Src>%G|Z2q0w{17_Cnn9B7D6Bzqe(%QRc1B^@SKaKWeGQwc=tVy(1na-}beqw4mB(~SkZ1BpAJIjeV5aBgF-WjmfCN?9eMSftm4ur`QmIyTA(EZTW7jN#aw?LF3*@#3O&=zbY6*Ci_Du|lP1$)|i;DeR66v14bxGXMM0oX`#qf;RR|xv(tfp9=>fd@Fj^`(WNcH*>m7+wW%G<^|>la1i3_=QP9vtioPwFGybxB8~#)Cd8ET%TjNeF=)Vl)anEJn1Y-IFH8<aQxFX54XQS4=g^EOewHJrOJ!Mt^F-2qzW}>IlPDNgP%wWkLs6h(3BbupG5Rp=S*H6+9Kf7(?)QXUv`AMPPA00zd&kzBJ~D4wY5`;0XQv{KcH|zx!<=n$n`6O%<ZlcHK)~JgM}~IJU?VE+Ja(FOq6u_mqVqX4>QaqK-sk3&^w(qN+U~3icjROr-D)!x6>A-I$CB`B}@1Vxr3f-Zr9`h`?~-OmS(ovQ?-;Gc0+)eUG3GYi)3*x>*Q|wP8<h^a9J2cCK3?7pXz+n+twp|NHfK9<IZ=+x@svZ$V@qt|j`6f#XhR&QA76=refLvrr}OPd7bsrMju4QyY3`GFE7K#+`9*JP%js!x498YNZijqLZ+39A{snSD-GASx7|yDr+IvousD{_ZnR%Bg_4!;=>YIR%XuQ5@UAfVYcQ6-+Da(0#i9|wrT4T2rELO<*+6UEpzDB0d+csLE9W>G9f#Q(c9a{|Nf0R?UOR6z4go+)7M)MzkPh`;Ws+9H#)U9I<+@CwKqDoH#)U9I<@!e*xzJaYUzzj&7nWf(5Z#ys4ekGs)lUgCrH(T3U)<D!8Cu+jy?c7jF=k7MAWEaXQXT==o0I$*Ty1Hh3U?{sDy-9Cg_ea@R=gau_47j%E6x&G+%n}j(_IdxO-zk=j9pLkLk!1q1SWO<2h+MXJhj!2n$ZLXFj^0{`7>I4h|=bPR6x-kaog?ZA`%pj?R*rEF>p(3+MD-s@<#VR2*C;jn2ekX{+MFotFe&aFLz%b~rn7-f2o<Up%#sLJ8;8YAgpNcDUo9Ebi9coN%liA0aItf%U*tI=QtCoi<ab9qHiwxfZ-?@zH5dF|DPG6l&+Ad2-3wIql<uW^KW-mYpynHN8>j^Dq3-fjJ2Js$ICGSqqK6Oqtg&l1e>AcQ(_Jy~s`$Qg}U!T1d`Sb$0FXO?>p`DJr(7iO6Q!u9@H~cTduPow238iUsb)HZR^hPtG<ovn@I9o+4y>auA>R_SoBxP6+Y%W*+5p#<1i&S<$i)SLh$pB}TGv>EPLs@aWg)H_ts<<A^(w>75L8dh){j+-=j6)vY}F?ZrDh^{tK+t}>0M4zadn?}dDP^HfKj9GSc5IdZn;E6|0fp{~FDks!0htHkoPJcXAXlR`yeqBsN2vM3}ARud*WLuS({WOn6{StO10NQ6|9n^S%+(6Oh`*efP!6R5hf4i`+e@P}AXc*=_U^5iXYcmYl$D;fHp91#Z+wGgG6fq~NEkcwDckv*PW<0iBYN*g2{y<?tOVG?riRc5JkmS!b%2u9P$1`Ii~0u6a#?Or=ln(#~lSV8&1h#HfPJC=iu%8&Ax8j`<JHVAmcF{Um%PYP;1|HcOaDh4L2ydK@(a*iC`|3uo611eUYe1xbu%VHm)6iPlCgG$M@!mbTXA!yu~2#|LyVVU!#i<hl)3J0WB3q*n7n&T*v6KA!IBriXOM6{Na)X~tY(k$5xP|vCNN@poIIKNV#3Js<76tv${+BFH%s>4{}ZXI(Zz2a>m)f3emJI#$?CNxdrUJ5h7pJY^AIvnF)X6VKH)l<Fzz4+7!pkFb8ooqCI6zT&?a}C7jxmIFPzq+xn%I!m0-^J-6>|*%x9xCHYvKH)YxNnG&E@4~Jj}keVvAM`!dm2vaC-ipLXlIp=zbC%xd-p*VD%sPRN7p-%0R;7dX`dYt>!tSq_?nB?t<9nP;AD1qkKBx#knc+9c8rudJqvK~T|&jYN?r=Atk%M<GaI{UM-Gv?#-wB_8^XLB(()w2IYmWdZQhOHS{z{{mnzPsgAp75-e;NoV8M8&$<F|IeKh~CMlT9I46mL4!c=vq^S|T#&(F?(B50J@{e%i&k>BUFKyF$<b=Ljk0$i1!*8(l?mO=U`#B20b;i47@`B^P+^O6==FLTsRwZP{E<CK3Q{1qe;cRv#}OY!<8@-0gf*r`x>O@!|X%C0k?*`%rN0e&cZcE3ITEz^wc-+?=Gl0}t!;w2uO_-XeLu0r~4_elJ_f>Xo)^4_ogWe9t*Stpmr)-xYUykkZ*kQD^Zvl$%|7*-r89Er+*Csqi?6D*E8*HgBk{X+Vmg^V+XEOx=IxBu}CCh=BS>Mhp%_VKNU-=g_%o%{xwc!Ny5K_>nIHPYf6YT^ww@rIiC2OTxhzaH}tN`2<w#c$skKH-#~uZ2%6uoLxl*om&y<w59t*P_ESf`T)uV`Qky!cH(g7nJaq`x48@oH4IMr#ple0f!fK2y;!e6i=e<k0BH1c!`0*taM(-?TC~}?h#!=CPHc9@5@p07f=&tkc`KW2}WwdV+hBw0^M|8#BDBtr_yN(>mP&rtpeR#&CQ>P<Qxp%sn1Ib5uKENJ0c27cw7zeaVfo2MS*_`BpA;j6HgY=6A49YxqqCY5h|r8mzCr-dpvPjCa=|X@*{JD=YuhwJWGiFbjL?KtsAHa2T3{?9eW8c;Xm={;C#1M5^k;>ch=hME`3rbrB<kp>=;>Ki4&wm43A$=g3;+RSmI(pUv<jTV?4uYeBa~IPZz4Y`0Wx-5FcR-;-xpwKqg+mODJdWb$E$0IK<1P=$?3xXWqYD+b%tcpg4B^>p>J3JEvUky$c|U^jtunZ_*4lIG*zw7{JUV7e5ph@;qeXwYMry)C64g$>Wb_@^*$uIV*?fR~7GyhB;{wy7F?5rPJbr%Y*Y$+fWl!ASVHdzwtqFv<XDB&#+`v6_z^Xh_Y|jWo9MtxMC^Cyz_d-N<`Ys)Q2&}VGtjI*r(GlF^F~+L|05DD!c`vj6p;h07!(rSTYo!V7()xfR<BkB33NgNF{F?Cq@T`r^w@l;kLL%rH-C4LFdF{vT3=+uB#KpK%cE|MVh@PvIC<!p(~JJof*a&oO!>t0G2(_NY1^4>T&4`OrMHjeb&&`fBb&L1o0+xhu}m?EZ<UrX@OOTFs$lF4aCS~6AkhOn3$7JsrQOJvKUySCzC4FtejCiZkfc3p5eP@XfbU<Pd(JuNYT5IrB|p*4R>M0D!XahF~VF_!h}K8L6nCixJP32fRYOM=^_>tP?B`PL$#5^70HrA<PI(-<zj54Q{n|Cz>+YR!iqIO3<2ZALe8WZ5W^em8c?XC$4&{32;jdanU0sSY4#bW(cmO2GSXR51F#1Y8#@7qUW-V@nNE#BE`?O)#X$v(L@K&R+oD&pL8#td^Iv)k-n|9y-a<=nAK!ZTt%u(tcW;rqx5(XF<nAqU_ZGQ(i`>0M?%pDI&qwa!rGurt={|kpv;WQ4z9w?VH&;Qp?vt<`5&oo+W6E=NX9juHl+)@_DR@4*tk}lmWaoU6>^w)ombuS<@NwjBq~kQkr^0IIna-PI67e#R^_{|Y$GqK(kvk>}yW77d`CfPyeVgZ4*m>6T@#m_CAo(E26lTv{E=sdao@THuEGWPr)iU2XF7t&?GN2XkTBcXyx4Jmz1&4H!-#y3gLiVxn{N-iJb_+xvpL7w0R0z`BQ(FEbixQ`)gtHXp(`H|MgtP4RDDv-<yyo)<JpH&xVP1Tk)0vOC%-MrDEIJxWuTY|TKIEa-lRgg2>F+Ggav^g$zLY=vuCK$(=Y(hSk>4fMa-MyB8Y_Gz^7VdSJrR6N7m}b~iU-m0`9#ujK217)6i|CPN7#?2$045c_|BsvOR;%nX7R=7SjbOa^8D+?RN^*yFUPqapK~#xc-b4_iQrc}>*07gBDRRl&F|0N%&+uypF}(U=#kF<3r^dwn5Cy^2dWl_sVh?-ke`FJuP}ZcKr>sp-9%nkxH`mP3&nqBN^cwX)WFjgi>&II)QSX~Ix>8QM?<}wRY^$LWg#_Hm?M=4^FOT_YcT7Jnsy@I1VJ==o^@EEG;t88Eh;V)1V^^LYJk}-!ivs)yJ~#^um4ur%BUIFidC_w^C~gRG$WWXa?M|%`~fK$I^K;{_fU7Gs-_ufVKb`nlr<}@q0OkKfg5fDv)+Pg$S2;JfgV0}&{rvrsHRdyJO8J`@6BbK%b3e|bLvsbAw4i?X7X_#z3}W06nLUSu}8h5j=p6vn4H0gYv(ZWuCj0x!fjf9U{G4qQGOCol0%qSW`3ffSw&HfZ!;=YB~|CqnkwiC8DjTT0XfK?xMe(WYnR*y<(c}gY}vft`GYH8cS;uD!#uh=R-McU8<L-vg;{VDJw;*>Hzix)Zg&X7?p5bf%Re3sWrb3!@ylN)t^N(NgGUj<6C0%1nf+EyYCNlx-Rg&es?AL|Or4)={2p|nQp5Bsx%}<-2?p+hi~CvD<)i@TNg12G<SMo)!8~S`)C1%1vW87Pt6`%$fT%Rx2&P+M+bdPR9a#I1^=hjVmE$G@O0qFY)=7)A>TC2&ycR`yQazJJ^%_NpWwP3QsQh5F&q>R<R8&=|q4Xn-Gq*g+t+SMu#!`-oGP0&ryQa)l{5)>$1ja#CtdRU`21hAgDiaBlJ*GkWfDFmcT$APxofJ`iO##uT=*l<hds_O42A}ZXZ^@RBG(KLXOw}Wu1=}vko5=KD7N_cRw_1?jQv`;>vbw6k&g^8TLN6!)+y$?QpzQsuic%?~x(hk-?W|qRsLjsO+sQ;`l}A=NKm~;^rM1@tT!X(mjzeBeSX1mN`W4olI;CC5p}r1d5@R)sXBJevuwU6r<gt%vWaB*v`~T&4?&b;V{2jZQ@C~sH%xTl*w2!x^9elZWF<l?`Yt`M7>Op1vqB^y)i-Q}ZL!<21QE3JxT&czja;6JaOj&^^qin*sf?l<G4qm4*p~9JU)s${K=)kQ*1=zLQbe)J0E!L^%(fuFzBvSiR*PR5`ob=@(qK?Nnd3Ty!qP~RKZPG1hMZ&16FPsl<PNO(9Iu*&`C0BN8{rw-IQ)ept>u;@73rnOI);J1tzn*m}->XyWqDLc(^{&{dy#$n{oLLqFbuA#BbZOZAZ`h*=E1iuSc+qz0cHkRTB8g2#1?jz}@?P}l{-642vmVPfC6yQ+Yt>+i$85lESw|!eHTE0XV9XY`YkL5hoerT(!>;L0>m=0ni@VTj!6oX;9M=QuPO&BnEF1fYJ({sWeG*j0>L;S5MluJ0Gl!~iOt*<e+YSWMkb$RO!_~E->nrbK`U4+R3uXtsoe0?qi_O<sY}SjusV9PE_D@$(JTcEy5gqw1?3`&aVObAFvW2<HI>i`WtthBU4%4O6dd=E3aByw8s8ka*R@7O!KT5EsvH>Rmxd@M|3kqDrw7>#$+tFq;Vd4T~J-6Fo`fo2SE%@o*7XI-Qu9E_zr|h&RV4r5b7ItpW67joiAMfrR)eS$dU2;PXB+v`k{w4_PH|)bY#!Z*Myooyay$9GawdDJ~9f>Oz5{gg;`EY~TkIIgF{#MDiH_?W6e;*(4ZG^3UPks*8ceAeC@1tq}?H+L9bU@{hA5LaPx$$qOefcXcHYUrz@Va7}Pno`{O`~N!6`M(0ZNnrg*5G6H%qwmYx@GB1HW<axrepCPXxF(`W|l0aI`K_56Li)=s6&3Nk~vuar41o(sFF$F<$#KYw)w<hPn<?{%(eQM5r4MRtURGN!`rk{Wi^~deasw>fK)U1Z%i?L4Qc<`pNYSYvnnxcHiv98Fcs(yY=~I_&kW=>bwod)Uk|DL&LK}gY2w*z8*Z|^rc-&H;<^Xi&Bnf>4y;L4##TLR%j~1{bMq*1AF4e{SHjSTerLPy!U<%Z!m>;qn6hNWPo&$Sj26!+Fe4j}j3Mo4eN}RY+0Rd4XbP%Zu8DY+;SsMAH5QAHD4?Q(=b+l^RFX(}7*Q*8;XR#RjAUb2b;lkIW0?rTO7^uWWtEWXYz#5cVOf`!q~hCc_;qb#jNW5OJyyg-KU*_cg*S24Lmfwmo>`Jxl9tkCh}4b3`njwtn7;40K<tfHS!^ai&whhvMfyn3YQLz+Lg515ku<2^aR2j-M;BNKoqJ$w%QvJx>6z+K0PD0dEj@Qkwmg2bN>|0nO;$N)hbm_4iqz-do*mZ9iIKS>V^uKtQcOn{um@G_pOZ=ybI>tEidT-dAG1gJQ3@MWFUM|412L!=B|HtN>3V3HHN9wUMplvLC3wwvBGYl-M6W=#p^Kqr+vtcYiKQ!j>%$-VHuh5g+N)|(Mo{J1({Hcjte{|qd~HICePrI=!rYr~QN&m5OG(9dB#(#e3x-OkZPIpySz)H$|IgmL#K^L(=|Qm`5wRjN@=;ltS+&nO_x5f3(7yEbZM7TW(PqE|28@wF0yVM_7;I3>GB&olabvL5YTJ0y&BI0r31hX800|@`K(d%3A$!2U@_-f~o5pHkV9Ws4_kI70M?UJY&pvw}n>yOJZdGPvWW<W~_}Bk`k3HB|@CmJpR4eybr0C@6Fy$o=nZ&#Z@9(V&LN6Yw2O)gacZH224VX9~??NG69N!aF>(^E4^EKelyk0b%(Q1je!d?l=S%Ir>f6ovP0dPoNbvJ}A;K+OohAX`)l@(Qr!zpWgkDm?hec8JI((79HJ|ryYVO3Y%9ozMuUzJxOw6ys)CpK+fa~gS>b1q0~*UkzP?Ok5X=$J@AZXAnQckp5wAPnTXdrSF57UJ@w&0m^3VB)9xJB)Z3u9n<V(mI|a@Lq)&w)!q;*D7~2G(&E=1HLO+JF!QcFvsnV#QO8~)q`pxR&dGJu)niXQ4NW=WkdevXiSa8C11uzG)Kfu6gjUm2fVz-*2Mv@eu4cRET?dug`C&S8PU^6OrGCo=7?ctj#yJ%lJgR*N>vHhGt51;W#(pd>a2@Xrzv`k*=tpou+X`-HeIh+ED}S>)`cq;iRb=^&AC4!F6JoXW2K<_g;^)lKPKUqqoo)nV{Jx>cnCEsFg+4c_cPx-P&wDHwMhQVYF+Nm{n{iciYI?8lA_2I%v42Df)1&PO;T`+8e2op_#8wwlCfj?HAr=l9oa#HlgA+6&UhG|jwSd|f+Z#UN|DvEtgb=Z2;uL=iRCm=(uMj6S52}fYOMKMY@IiHCri9o(1P-gWFk@p*NXZ(M;ZeCkyH8h+F3#z=kZ2Lbk%gEgia;Gt-}(}UQUZ+R^ASl&#je96OUK*ItVaehjFDS-wR4bU=$X%nD&Ee<Z-ERO}WXCV?zm=Iydr5&G&6Af#=unf}#NNBUt72_O7NmyGQYg@c_dvpPVP@_@yhWVdLQO=N4N}xFgHS&`};uZSv@6jYh<UAO-7EqpDj{p!pSPd3U;!z<XcuQyt@uB(5()p{m?qP<CCv97HW~s8Q3OonIRCOC^;+3H147M*@>l*}IgClSsEGo5>s6fKT8DrtKNN{?#{n$QwQ64O;*9=UWTEweTA~<c%KkMi2Rp(nI`PFMTt@dn1Ot5kvkSCx)c&vJoCpc;6*eH<}`u0l-|?4W14+=ph%XZjy9Eey|cOtt0VesLkP}mWl?F8^KaDZcau}HR#OhZpz1ua%Zl(suhN$$Y9X@Nipo)Ee_RkCSI>lMb1>?7Bq*mKjTd5&CNX2)WXe$X_~uv3zu4O^K0<pR>XzTn?cz{lvoj>bBh^KxD}V0cu3GK*cr378g1;H+1O339dERiJHJRVdMGm$&$t^;Q8~s79>2mbE_hD8soXWgL3bgM7mIdWAuf&DcTB-ixX<L9Y8mvzqAoaRa9q+iCS-ejx%ZrZ%60DLZ@q-j;hrLN+!jppS}bnT3ZC$NdxF97<gHEb#^+C4?(4Rr+-u1Z>H3jpu5f1rjhV=vpC9jL-|~cV*I9QmT8g`E>*lUMthsJjaIe>e8&BK3m<%%e)b#P0U*7CCy|wm|*>T>aOHRi^Cv8FKSZXA?C(Yv)b)CQUO$&}6>K|mfXW!UAsC&JCP+btnFY*s#oo2ESih$Bz_YY#VG08c|n{80MFb|7M^RW6#&9Qg}<(9f(8y0}XSr`WOm4KV*RKQ1_c?Pw#xWOd5unlVs4v)gdORA9Rvpa|VE7h;D1eyQ+?yAW>t^?u<B#uOcfv0T{pmd>I$Ds#%g&obMO-Qw9GOW}*@~Y`%7<ObQ=DtkrUE|;2Cy#6a<jqG8tOIvDRg%$p!&<mBVr?AQ0*N0C1JQcH*bX>y3$lcfRMGnQI$$|i`H~tN0>m{w)kU0YfU+5`jfht`gw=QSC-Y`MoF4IUy!&W3HGuyL`c%Im=Y{pqny<tit5^K4$cQjs5(U$8A2gLdpep~A%?MlPf8v|L`Fdb9QJY<g9-=RDZt5E|@e31&1!SNZdxaCC$B>5e66XbxR){lLl2(K{ZUryqzi7j|g;*UYg&Eq|8$MUV7%;0O5nT?dZUDYg12XXBJwb1)1Y9KfMdB)XBh6t1Vos@vyFp&!u?QOGp|zR=yg9VCSkaw^O_`aSLUodWa3WkJ{Ndc=J#mHDPy95xVDpZT=m2!}o(~5&&in$+v(WpgRM!ZqS3`ob;pE7IeeP1|k$x8=?X@uZ<vDzn=X@X6n7$eUz4C;Z*6h0-)bu=O%=~Uw!x9gqyv75iTYJhyf(I9SQsg+(Ko8TyKo289VuCH^)jY3}Qb!C1ptTh#Bb8Of8vrWRO=*$FA}jC}CM8H1ohP7xP?MUX+0gtIy`D&q6^Z#ow&nY+2QiKKVSo{c^poZI|7G2M!%sXz-(sgH<e)8zj?LESbv6Kuo+fP7DF2DRH4?fE+|`-_XhTjMVUOZ;;Xe5U0$FlcR%YZbCm!U;?{Z?{u+Le<LzY)V55nj)W(cK9n)tjCZiq4faH{5`CVsl%@)beouw#VB8IoT|<9+2LcLCE;M^I!dIFv2oMItnc5Q%klZP+Zwsa5W*gx>IHGh6)xHX9rvwrkwiL<!?F(|~CzTXMm}4D@m2!kVg)A?DkW9>&qmgG1B1mYeVt{8reE==g5c<tNzFj?sbM@+Egri}g^_(pnGAV=@Om2s+l@rUSwrKkM?Czw~c?ix{%2AswdlMMxK-8E%TA$Y(VJljU9v49*Np)|J4Hmc2l6gI<EE*cVKyqUC0eC(CC@T0cphtvKOV!jl;iMBecYv^^=IIx5?ac(MW}vyHRhLOIZkbb=HPJQ~nL5neM&+%CXmlRe}Z+jZCQWIb1t6+;Y1wv9o`V$m7p*oBg-gSRO~U8@mQMiEvE@_c8hfWg~Z1BN3Jc=<B!Z#ltYKv_K3PBxJ2utejwpSaKd)Js6`{WZ{g`yA+fcqQmP&&83TcTRjU3gSc1d*u56la#qohZN%d>w<WX7l?PluKdqnpy4j!9O%v+ePAN+66+od)?L!gBhbBXaYvUxcLy3z9t})8USQoFvF_#xkng1hzjng9V_%tPH=1-4^j_Zvy|)H>mlp7Zdyk^cUB$gu&OSoud%S?Ylhp6EXA=57&Cu@+(eGTGfPPOxzatX43V;vW8TviV(C@#CO9Bj7iGKgNe3GX6Qu&@a`kgm>SA51_0E5T3oFU=kITF4&F5|851|I&efA)QUtvPjEB-}H*e~`(q?f#XpOJ$w#mIJtw0MK?kS^~hT6!RQF!yEvo<Jlr{%|@8p>qQ#CSsFk~g#gy*#g{h16n-ETgE|(vuyM@@OEdA>T}uhbT-c4v2Dkfu$_>oTg!AUECy3J$?)>^F?%d2$7`oO%rBan*Gv~~gg)Lvh-3Qr=qnku$bv5O(CAsp?zlb=H@A#n#ha67wmv>OECtmpafBCjjhgK0y%*#OM;HB8z95`VBij7@3y551DIYRUUUyKhp7|-)$#fw3q^9j>!exz$Ykm12L)47W|GVnaN<ITJVbnhs;&SUmg#G$}OJ{wsbUV;W#Dsp=!5~~nqJdppfrRlMsj>L2RM_$@&Kf;%H5DLLv=E1WLSj&c!1!dws`Uk(`{uP(`=+<hOlWz)Z0WmsS#f9QCQ}2DO9VlRA7`6}2pK@0V+H8aqdSTukV59jM;?Ze3&4=w6k<}0Q_I$$T;C8&Z?*DkPh{p4&2kp5g5e+|WxI7Uqjx0KCxI}KwYiT%B&_LJewaKcH*&$TfX%4X($(4N;rBPajt=whCsVF$*DG-Emy7Qtz80TDQc7(QIw&aDpW+IQVukF03WVT~rb`sr)tU)!F%MfWa5D%ZEz9Ee{QXjqYQJi&M*@A^D2}p!CIov>i;IuEZNw4=Kp~ZG&ezevwpAA2wHwx}<njK7PV3ll@z-IpvWSz4qi9Qu&c=Gi({t%YR9d7c4nC73{6LP>%bJ4ab=yPtt!q*?n;cP!PhZEuKmaN}v5v^#P`-_P7{<(<u3(POLk#-r;MmBQ17ST2(qK(UlwrTSY{(3}<^`7ia_cVL+ES!z*5T0jmwy$JwD(&<YL)hka2peyQu;izMx7j>J;KUSs<fwg`!^!!{0$FfMq1AI4%f2{@Wp42Wfvk<H8>~(&sh>KK{jEu~z<+2gd(FEiSY);gXR*n~oHgdNb99*3!HtMawdl+i(T1fmQ(k=X);|<+CdUP%Nr>>$7}qNE;UJ5q)cnHJCqE@FOFMGgFt0P0muKV^;?JqVWhoE@XTE6`X^$4`;4Jfzm@*kD?_4QsWn76CX~!hTMM>+qR7dWfj9Il3n7xrx3@Q^BX3Z!8hdf7hS71siX${p#rpv4H6smf136ES>%r<B@%iNu<5M$1+sX*&?wjKMtWV+lbUq+^5KY~^R)IK(R<&G@L$nKnbXYSEmMZPNWOdAw^7^z_Jx6U9(UfQyvO9~Ifba+Fe90+FYWu~!ZPfSq*)j~8TM0l=)#MbP=!mOt_^D(#^`Ek7jg32yq5*)OG$D}{#$NDs-<TQD8?6yr?K5m;tW#~wzLs_J7$B5b)kw%s`Wc0sN8IyKDPE0OPtwr%OvfFrYQU#q?m%Ely0!Ryb+jH4Tti+^yA+5}pgIy6)<XyP&t!iYJO$<KzF@;BwUtL&_q_#p&bKIIS%c+|^yE`7N?HitQ?howm;|2KTk%$uuZH*V>Su1zCkuXcPaz)ib!rOFug5J&U(H<yn^I$h+R7WjE_Ryy$o!WVy@3gPH87;Z7idHy%ikXSTTEG{aV3E#SvE%#yOZ7rp>Izbo;Vx{X#+$6oFmxVpMI$^f3Y!tY>_(Gxu?tEV5K*Qu!!#UY((XT&UP;C;bhDT!pwtDvz2#__4$CL8Rwp5P{uW86EVfZZqY?<GA_|43UST>3cZ1xxGmegodF(B)U`r>hq~n6eXL)AEpDvDRXPr=!uT6r!NI}`eKv%BWEig^ZgVFyQd$F9>w%!`eq)WQGnLf+hyt)y|nz0Z->-i08Vz3!WBS(9RJVWE)G&>u+s109B1lT~Srz17PS%Sn2C4swKJQ}+yyF9x9ig%1VzaTL~UoG!ipDpvv%C0}8|0HkNhaa(Y`^fHj%quG%DXWPn-45gay+if3k&q<^BZG~+F@}5sX5piGq=f>>!xQMJuEhGlYU5K<+$~{66uMC!=WabIX6KBRTHmO?y{lsDcPyKvmBhZFE|uf!#8?m?QSnmUjR7gwZdZ4uh+X?qq{UmnE+q80rs2cKo)+<c<le%oPjV|e(xe#$K#<4MUfLN-*hCM2`>G~ra<nf({WRJmB1b=XT}CL^6S&1;sNihN;ta@XHgZh80X(6~s~4+Sg9eA7$c2yRV6UwO-qc$Nt63&;iJf9x*0?PWCKU5q-(tEIf}uClt(*EAV5|ZaS+8VSZ@{c5`PM6lqqIZ4%&*qWuZC+Ft7e&B4N4;@zsh_pySqiis>9W;6yc`G)WT9Bt=eT~)jx~0vVN#fLA=TE8B&3nMW&sX5oZZbufeR=bC?zC)RW%B?nQbJ_`2=qjZ*(u^_Sf6d#cAr4)y$X_vmQNW9UYmFh(c$htN|tXmwA)U4`b{5=uolFJa&3<kIA+t_Gq~*!w*oP;od-N;AGZ<V2wuQ~agMa6W9{jM`9|R~2FC!-P0+Y3O*i=7e^lLJN@#dHU<9?8~?x^W>4L-M-TNxZN=+Xw(BVe|M}#d1FqmVb}|3Ez~r6V7ddaDjFWa4j%UCzkM*Z9?D&XW{Z9i%~;&NW!SU#vF|6&Jj2I^VqPFo#+~d_MzokL6vSWI!=9@P%Sm9Y-t$4tq+miygj1dCz~DTkDnqP^FFG(~vgjd`XMoIDiZS7$V&Ak@1*xN-m+R}<G||hW*2?vipuAnNuWu>9Y%!a3#8ry?VF59rB$yPG!enCU%BGcIsu8)rm!J_9r1B>BzV*RUCYTX04!J?TmlUYxh1%caq74C~WK3(bgQf=VYCqlV5bD42iGU_l(3yIxQ5R;;$<6udHX^2cTB;W16Lw1wamedP5iX*wZAfRm)p}DiOu|LPny3nmXWNddMM!O{+m8Opp>Z=1aoOtD+`TBOttZtY0};0-Fzzq)if&?uNh)#WgC{|fH!k<VePx!r(zwBV(@Kbr*?4H4TgSX7+6v2-BvdbyvY#mVZ9eZ(^-E)C^gsG$uvJVyRz7OZYDd7VvNN=XTy^KjRq0Z4a@-*nxPn|gms@8Hl`fI1lNeSz%#o{{b0a~SDn8e_<D2@~5UEtzX!5Fbv6#OO91R9rh1NbKi+h*4f>u4v9=`0mg8^1^_do22{Dxk!)o;_iutOpKYp-tjTdJ`=2hcMOZ~M*|Uf=M!r8|z{dBYQ~?a$l3G(3jjH*WhK#%_Fh+aq*+S=;}Y*7kenzk0Fp!2J_b?v0u$3chaR={n$V6--O>@1^u?EVA?R=r93LtsXj1jFppH8mph!nEG~(IE5Vch0_4CG?heGsbp9Z)%5~a>ZtA)ci5ZAQG#ev#wBsI7I553c%@7Wb~H4r0vYY5O!Jp0Cf!Ig4@RzA06|v(PNYvcAFds{M)Nbb`-LiWO=znN#qb?+Ulxs<uL#d}ccX(S5R@iggiDD`ubOF1p889e`ipI_pnSGrdW{Ruxa3;*kq%%1GBd1{b36M{MM1KHWv;7yo0VIYK1C;(*18q5I?UjWSmu@hALryZG71ZZ)LKSEGI0#{0^RA^3sj+V6RowLXZ8#U=Os{A6VcJ27jsQ6pIQ+v#9UNmG+|56E3Ixn1&fap2-?!^3+{l|XU8llb?<nJmRK8R@hgi&ByLyC%ba0<2*S$!w}qTptG6@=e94qEIjOgDlO8kzj0!D?H2Dit%sORr?e1d9@t=*4SQ6N1t4|7-?tl9uN3kEa?c$sj+{fE_MWTQ&6*y6qqpIBqiHic^u~a_R4U5xHKZ8!k+tBGINp`$aY&wCaxmxzl`tK4nJ$~;?c3~*g9}@ugLX$v;*IB}q;+#~%jc!SZyH-7{wGl%%CoU~7Gu0|WxmvrhdbtZbT-k-qd$Fy>pK~Mj+uvpl9ICN`?Y*c5-n^s$ZowLME8VgH4q#`gfj1Z;SIXea?rddnE;D_+Rs-is(y(gD*>F}2f3gzp$4dA}>-^A4cuh>qvKT(AgmY<Hi$cOUq)=LJ*2C*%k3PC(G2B=38GEW8zTCcjW^vj7;!P*>O(*kBWAN?Iw-$a=aeQm!H>u1wsmwR2%r`~HH>u1wsm$;Cp2EGUWqu~L%<q;|rrtf%$pnb-hEC>~^cK93Mjzr%(p02h8?IS32p=U7gG~HTfR|n%52j56lQzy&Gyxc!gbht}k(5&t(yYQvNm9s+u+VrMRWv23ve3Fr=Jzz0SQIi{`k7TT=`s2X8OBRx%Pa53E3%E?@{W1?v%7H5+{M{Hrs53fJ2g?qJBmWU85DMU_o`UsOhR)yxrsWSU!)1Q%r5UtMYD1SRk)&BSzyU$LYhJ*Qt8USN>0-+6*VvAH0KZZOg!^a4RvwA{QR!avQ1QzIYK?<L;(3Ds_CB4*u0bhoYV_1G&XMtY!*S<CzLAvb2^qEB(`~7;xb$aEiUvM+1szFab8hzeDPPGDStktz3HFS-VEnw9vk`kRehN9<b??5<-1oUG<CsC^+?mhJeQaB*EKw^p7~W$qHcDZrfhSe&-u(_eYsBQP#*3RI-GOKP=Ebhy){!SCHnAErPDw4=h*C5v^V|uvkF&LI>T9N{Et-sj%xzA1Nr^c_iToVTR5u?@Fc9vKUkJ&{AFmNTM#`8`#o9zs|e`=ERy-f9c=yp>VVTQ{jSJ2K?NxK0}v1>k|$LcNRvfLUslA#z&5d3v;4l7WHf14+vJB8h!oP)=<=!ZyDNx`4aCOyEs%ARS(3!Y7ZhVak<?Ru@qkjq07STNc2y$XWW}OOFBOSM>J4z=sOTj@00iBIs0*NTs%DbZ>x8bw#RK)m(p2RS!D#39GtWbR^OFi@3FwUSuUpjyx#d-d>xHvK6@s)>%L)>KTv#t!jm$K&P%k|%mL(&27aSvNu%jgEq?u(dr45k>J_@vdz4jZ3heCv?(4@Xn{#^)W0ha$10@vR{;1+y7Ng@QJhY1FucpbtY`HOlmxQYfULb2T1C}KA=Sbi+9{MBt({zausTj=%Y1v>ucFV@MJFkdZn3h`LyJ=92ZUsQr+ZONH{l2k4FMv<%)QZY!E46nBk{P5zuOCiIpD+%g&vg14A;XsHU$(oUdfuPjjDG42xh)9&2zUXyuu=g?~_BNFee8U3>Kw!b1I2@x$<}UHz%;S5VxC*O^T6rN`8Xg1ceMOf>VlO*Z@x@KZ9j)fa%~CR7HfI)ve~zd(jMAb4=S|l~EHd7y4j#Zl3PiC<kl;unx0VHpEr7Ng`E%y4$nTUsBAp5WfH(-%;mNARRp+r!hy#Z+l^Lj45YkV4cf`|DTQy7Zv@^%>p9BQy+%f#?+m7LL{j^y0)80R46y7Y1!e1bs=AoSSq)YfM<+Qxeyi96BmJS!PY3a6XnxAQ=-4>j9v0&N_wY28-YH16va4I2vRH-z;;@&&Ewa>4U_P4(a`sl8Rq<Qy&66vnc_k4UtC4GXmJRznTC%N>6RN5361aZK5JtJ0ng3~ltxO=?KAbBMdN)N9RO0NqvY$lX0bLP2FdRv6j>*s{hU%}wJ5h{FUt@Qu<(`y@trMB^=<%_S<HdaosniP&n34KQ4xRJauiTSTpIQCB}9PbJwI6k3p%=rjpvnS<^C0(3@*}(&#9iNdm<^&%mOs}_iM7;YeI>%xlH62wfi_Y<#24B%RZa~p}vCi>|0`|A$jaw{xpSDwn^iNd(vFj--=iVV^=(VA85cFRi05gXy{|POT`{w#V4IF9%xQ6Zl8=$=T-QHtC$sgZ<%o;i$@@6y~EpsEHmxNC8I(|4=AolnWh6hXphf2QYRtg3w<fI7#>UlNKKt;f?y~{(a^0ozv?Mb2xVfRppH^uH8`p5YFL)en)+Pw=~9@aiq(&dLrz_C)1q2b3L|Jn!a1a6XVo?w5}ZY3#?ND(=%L^h1`EP9IuvT|nQO?~oc`2&nwKj(vpmxEB)N%39m90f`#N&Vk&{M@ce&>w37=^;$eFm6AW#T$qMb+gq+BoR`4xWMIY01pV%ZBk}fU)^J5Y7Xyd94|(1J!#ZXBzidxTjVSSH^n_8B<CPRKdiy;I?iO8A!}1vxO#lqYVvs@n&HoUGNKpSuXsb$*BN#a%4RxbTS@)LkILb;VT1z3nNLKxMfwV++K>wGD=v9oQM@mxSCkHwu<$huk@CU;*M(M^K}=WVC(I2tHo2`$><YfI0VpOB@g%kdNiLEEZ;b~rxkZ3mW>vzwnM_VJsicthl{6_45dX9Glz!%FoLYj^7IWA6Q`!X$T|5~*s5?xIo7IxDARXRXb|dz1@<;mpln=<yDsHMUV<jly+mQVw;ttNdwQx#{wgTLI+S5SNcjNQAows;-omo>5Aa7N`q*;S!m$y8-Jb)2ihp#+Rm+2m%N`Cj)gg#aMiji?tjVSDrzw0qo#2E6p%5h$s&;0wotF09_BXu6Fg+H5i)>>4EKjmJyqPj`4cIubyl)s>6J|J%aQjg0!HEgFmw`|c)`KDHDFB*i}DUX&r<W{G48uFQc|Ho{n{O_lb{`_iH#ZVY8#^-eD9{RJ~yI?#vEjEXKPI0M`4OQ~jGk2VZ+%{0?l^}<tdi#MIO1U41{8ux|%IDlNX%pQphczo%0AW`T-R0aWc|j0kB)4>K_&sj6wO)m=qe<1Uni>pyCvM>K7+-Zz0M1*tZpS8SsRsG;-%1Z#-RN7*qGNe>EI+lJjX{6jtI(w|N76p!G;po$7*n;Z3Foiqp_qm^s*JweW*tZ)DBABi0ON81u2vTvtIwOR<pBI%^{1<U*VRA978wMz{P}xO^5gd*ZkL0s1G00$pO_Xy!UC0#W>am^aAEaeu^ly@s<x|YlPgmC&XeJp+nRs&Oxv`e20>IgFhpZ&IX`=^OuUi)oYeIi&Rn^<nV(|G&tqS}g^Zyaa~qtr<3KCV)+2SK02|(2$tyAENd4_$mjjJ5fdsJjVPl2uJ9K>Vp&P2-2$tZr)yl`f&7q}|+?JmTyGmMjUc&vk-FBvq0>c|Us>HtslQ|DEt>WYnQVC3C%E=9G!<MWCVi-(E2cP=abI6Uw>?cv@z|8W_kzB^pL|)@#*gxX?^9%hWc4K|dx9ZBkk{*5jYpngTIiO+&LL`fg`(k|5KWc>x{Ryo;%#>jIHB<aO!&5Az5OL`&g*+XWwv;+zFz0a%9u3a=6f=Hoj{N#P^Oh<CmOW+vfbBqAh}(GO4)cL8)-`^#-8w3kwX{WDGE}(o9E{Y6wwuaoiwp>P*E^!u8wPWj1uFqaQK7@bH{h7(<u#TdHqZnf(J#G7^IP&@xts49<sju2+WbnuRp*}vSM3itfP3SR*VRB_^bY+ptRXGtHzC}yb@x!BP~@wtqo@r;dGPKdHn(AiKr~<$<TK3Q+})u+Z9xz<9s1p!&q2)Bx;aZ9gm~wFs_5y2;%>_-7~a|haplqbYea+jwEl}&-Q_zwav)jitdiz-{_1WYs0YR#%C7)1{0<!i$8!KQ7(eW5cpAYJ5e#!<9%}w9^!?*66<dF_oC)IFZHWTZa(O)8;|mAX(eqg9P=9f?bz%qyBo9&L+~ggkFUb@}ej{J<UQ<Es>Xnz`P5yfmFj^q!wkM=SaWd{Tq`Q0=rn(LOR1%9BJ|ywkxlxpLE7r0UVj$sGBTH1X9<lLN-VpY89!fVghGJKCxslB0v_{9cWAda`vSM$yb0YiHgEx<3_E2fY=}}jJi5Z63iL>#r3Ejce#6|kX-1*Bd?daULxA(N`V{gX9d<=~i%?Gr^>0VhY_6#q9XHJCop)C)-6<o_>X2=`eJaVFyS1|xKd!r!6sw^oiG;E|S1Q$KbzV(C{!fEpd_XkuEXpa`s+8<iO6E)L_LdQLUV~bl4_c+O5cEPyjJPdl4z#ch`^sJ9#?q&&lcjP(%CCy5mi*|$f3P`l<gT(amd3q`4^m#Qe!#Lr)_IDU0h&9i8{6CXpmj0^UTwr2>hyw`H1}GQqVXhYUF{b=_k98=7A`PZ2ZVq|2JP)T~B>uL{NT}Mg&jE03V9`gjxSDEjkF<v41{rXG6@gPNRg~^T;YE<6?160JavK<j91sSkuai)NNEskL$oGCiXc^^bz)T<Fo&n_&r;eZFf}T4=W}zEs31Lx#-9c-fOxQX81&iv|&i~}ofnAB}^3VG#<ySnMmNVJ7Z>SkPfG+Dc%{BEtL@c4+vo1BJTk_yqmBhaQe$M3)x%b>&H1ZH|lF&0PO-K(h5DWoPV4@xxlU7Y-X-qFYYwTxT(vFygkb&9Jh7|xjZH5Y%Jt9-1jLVgtC-1$2fNGBIp?jhM0GjX6!kiCR-r$^d$$ze)-!Qoc=x5k5Ece{jm|kRolCl=ja!Ogz4t8J~c?eclJ?sfpVC^@Da``SA2IsM6J`<@I7yhBA3#kLQ@AE?HyHZFUN+GrRNV5GY_XrkJ^Ywgjt&loEOys<fI+Q|cGcTkf358nfS6om7U^s}i8R+3=t(;0M#VMW_RcS;?1JP1c#lv^j#%@&cujR>_H=a|0wZ=G=v<8%Z^W%+Alv&kVSz^ombWpuD-vtxubF->}`Is%HXy)TQri^D~{++uo-WxZ?{yon8zTDT`xXLYyu#s7R6=6l)?ws2_=Ur8V|MBtb)z}JcdveD6en$S^s#duLkadbP2Y^L=*1OJ^;%uMK&-yH%;5TuzvY+3P679b@IRgKfyQ#!YJL?z|I8N@sd9~j_VR!H4*z4k5$&+)MYaf9`+0qm^@A@{(B(}vD7-+jSu}nbEaUiN%c2Ho1Ysev*&`r5*VDh_z0$U`sJsxcO&hH+1JS=8+=DiC*!+p@kmD_zk#467>^^S`_kC(7@USZqfNR;GaoKOo!AX!eE24DvgV?ke*{ro7}f#)#+UHTzGz-uM-?0}_8xrV&j!)3KbWV+!*lh@;w!%rv_=PsCk_C%{`wMWOzkpj*h*U_w!Jy*Tlz%7#ZaLcTnZP=vEkUSJUICLZ8&)k--jxsuAC64T!#6^G_4_E^*F`c+htx$WDM6#T6fD4NPM{wsR%k7n~S@~<I#p9Ja60{oOE!&kECo#xc5#<I|Em-TW3_UAl$>>bsG|=)^kHupa=(Hee;uyH$%rEwcw-K5o>?b4l%n}HW|G_K7%a5Eac8qE65Dc*}81JGLT_x~?1%j)I6vXq29JjV=upo(<IY=*@QbYBCk_jGfsA`Gn*Io__)O(T4x#NAJ&F&@J&ao{O`+7hqcJC{BY3DEP1<umH+C8@V-AO;2TFoej=nKRJscjn`&FZ+aO^MP+tx^G`IpibjP#g-_mNn($qc-i;_$@PKe|~i>opjD=ZJ56$n<gVWc={1dSp2-p;oOMmX8tJ)J!WS}cKnGlIA8wxJg$b{{Q}MJJ`V2;LWw@HXWsL~KLdrm5gIayc`W-$uAJ(%fm`ok;HF`R{8LGsKp-c73N`YYp-qcyDN<UwZ*35rGd@R~bcIJz_r8sm>c|0ozFJnzT<TbTD-;}O&`m^Lb<M4Yq<9#CGck*IV;4vf8v`{;d4<q6#1ixR+2Axe)n)-bAk^kiCGmAr6&kri`n@YM<lR8@VWAaKu^EFXQJNbyn+WZ3UmP5y>RW`mrQw|q2;>`hllQ8N?ED&C5T03ob5U;n?yGmt;6IiiOV40`M(rFo>YEz-={ol3QpP*XWV{#H9}>92Q}CY|BKRX=e^88DVt=}V{Rz)uf9~hlpBeDy_+shq&n&3(C#%0``hUo;e#J=afruMt3EN#s*g|HzX3loSjIQtx0QI3$4@{pY<}ino<!qb6AtS$lS;|=&7TM0@Bmo|DWd8V}+Ny&WGedR5K5?U&8(w3Y;ZA?7WD+?lf*)W?$kn?FmX+n1^J!hM+>0Q(1CzAI!jWRGa;>MzI6#FuZ|Rf)z7s|aH913~l1~U^Mjq0rCN3#6wL^Lk%TSty0hy~xCM)db|MiDRbnXEUcpjvow`f&?+Bx%Z8$ZgUqPyP|kh?RTuF1!6j>_l_L`5OhBGlQlY|BxK%~MUG&IadP2z6q0y%6dYFxnTP&Q?pi1t#mT9N0VIqKNLoh%FSyNvo4GS$>IsQZjkvTFxnH#R0rA1Jk3nn|?WZb@RYEnYR0TNo&gtyXT+{pAg&sC%!F+#jGMNhy{*h&T`Vy^^DlB$?0lwU4SdnIkLj!bo2Fu0;}+T0_+UjHbr)jrIv2G(9*Tdq~vrv)3m;-rMu&i4b80Zi0=8>lRwVobXR=xOF7-UXvQ?m1;bAk%jj=@_zM371*lcsYPrH=xRwmxT*2H0K@=zQPmT2XNdC!jTO%_cUzk6X{Yz3eWr#22AS{qscw@GQ^Y%i%eCEvIke+Nuy<Lzp79^j@5-<j51k6{oxyG5pF{>MuDweIL1}^O5>Ye-*?Q(ZTyPU}oL?uNgFNpJ_sGc7I9iz~GyvgSUrX94xBQoi<eMEHQm49hReRFmSLTpy)Iel}wZRJq3tm<0QF)t`S{-m^@f790UpXFBXR2hCqm+-*)15$2S*tcUP_7r5Pn!9+%)p1`6Ij(>lJz<Q)L0KYqEX>u0rPKUHow2B}?MuQu9>u{yZ__J-R;$4=Ux<UL!EMk;UI22j!fdEc%S?BPHCUwIvt#x;;Spz`hYOEKaKaFSv$5nnRFFw|*%;U+92N~KnC{C_yqI^|vEnKJCKP;j+-isEB-om%m{YmOQsfyPQ9RSGvSyj8XSNJzi~sSZ`*w&cBKc&AsE&Wuw8T;r8p?}D4O(Na%7{^sDon*|1mrUGq~NK*lB&@x>~`gYhcpR*6Lu<&g39=pl_#o$Q#YYyo*rbR-x#5uQFL)yb7fmx`KAn0QDO$x6TK1vv`}*1w%;<<;u=s$+$P!}B(vs%uxrb9UAIGfFV)h=7j42A4=|sDa%5G0UlseiSlsi{jgyb|da9d-VtJ=B27j?lke*Q-4=^)89TSU}U|;US4wxMB%3)v|*cxej4dpC2f=q<DI@83Mi9#1gGc?*CeJu_^=FI>=)hJfd0Y?iEMTw6r!YJ?>z^mFaJ}-eL;)Og-?2g!y?u1V#JFTlMYkkit*51l9;Xcq92i`^4KHM1^MH@uNTzCGWQ*wd}pm!fIVGV>g7Uc|0t^T-|m^<MMoK`3YZW<dAK|Vg%((DciHstLvbdoe75X%O?B7#g-9ML@vfCkv~k<YU?6vAT4{q<Knw%v1f(%yAnyxNqRTQN(+P{8ck);Qa!7L<gGSfRtA=4ecuJZ%D+COpGN*&*UtA`Pgx*b-!xPrLVBG~#98lZ@gKSG+d1bRUol$`_NHZ$s~*dc!v$AsbS1O(Wkn6FrB;97kLJqBxjyWm&+H6~V4M-&8F(9BJ49;l)wJypJ2-a@x4bJ1#15MvKytig8jl7Yr-E+B!Oow!%3vRpETs;eBpBMllb}kCHfd*kW*i)nWDDDwwmh_B%eqLnVej!nhhwZ_hgRCd45iM=hujwT*#iD9LR+G1OZH8+%|c;AN(gat%m@D1Q>+yX~S0GPk53FfYY)F~T@t(DJ>t=9AzGdMLIqc(0XPY`Ft#EfbD|Ls8KQUVcItIZWMzTC7x5!Xh?du9p+1NQa&=pTy){vCgb?9;^|{gyS&7#hW`Q4j?KYH3!K6DQWMe3m{igJxScVx9;yubXkmD89nODJ@@%uDZff|W349aD|Tc_7HTSHiq9!=$j+o?MxJ||NTarKLdyno4kUBkOahJBTP#~ys9{2$x)^m!`G)q}%J4l&^UF`Wa~~nexBVtbzL`be&D`EuVsA9(<HM<gb_A?NPkRA>M(`Wi{wmA(F^|lL+Lj$bSnLRvc|L=QJ(K4%rEF$NWc;wm^Dz^^Jl||nz*OHVT-g-#*C`pFJHrR;`j8*R5AzDeqUSDeL#Yd*&{KrHyx`ZMu0Na@KIR1kW_t{l@_2f{WBCDGu^5@H04B<jT;42%6*>;N)Buuh<owA1?kithSCMQFC-x<`%ZqUJr3#(-2|Z%9|0*ALr$qpbamr0!OTZ*gQGp2@kgnkW=Pg#p4Et!mKOUKTb5&kihhq*Xu}ZcgZ)`C4Bb#`_1If`r9RLx@!So=W7lRHAj(_>NQGJ2cxs_B|D_=!CS(McMlvjzQ>ZvS<ymy#nJOYmo8ySvOZ5`^qnlRb<tu$h?ML)?Q%S6VF+^!otA_p-Yb1x$~B@v$uWfyKuoRy~YBaOY^TQKMAQ{K2zQ~|lMP`75n>bd3}d(h5SZc3G)jk~<S`MU;)?L@@({vZEnZRrRxj+{0fy=#NptY;J8k_r$C6(Gz+PY|ALNCMcPgoRXX%|=QJF>nW))@gnNwzc*C3uGY?ElE|bXFYcC$J(`baOja{Tf?bsbHJwez`5jphb5x<g>Sbr^|PK-Yu9JE{&@!q>_A~`2FE@$OdTjJJ5V_5K(&)h&eVsP2v~L_BI+BoSzMXN2&y}Gn0=9_<E~Ntsm`s~%{vn()IG|!Br>_p9^*A=4a}ci3*mz7PWS__Zqd=DXg^DVyNMw24TopP)@>$b9UGw|7pEm_1+>h<ooE)Vi>NGj>y2ZY6gW4m_nmfAM#^D8kf-JYz`d|E?0mh&i}^B+t<UQaeji=<jBLV6+yGYZc1F<I|H4OT!jC$`J=cVbNlpQYl%~|r^9&cq-q~H5-eQ^F4&(I3eu=(SCb^a-e&&-=qf<ufl<1NB4WI^x=1QkTJp0qtA9~R?`wmYwF^P$E&_3`Lds0kjyLwA9RzhH3_p)~6D@eZpYmq;gr>(s0!;5(pZSp$C-y=U#BZ^8L7q^6{yM`}3o=3|KUqcIcO`I)Qr?|tR1NjkXOy*==o!<gR049SuC_-ZbxTIt1m98+~o^QolO?)e#Fa)ro20%kv%#)!7>XsIgfcF5q-0+Fk^wH@+gu=q!vNVJX=un@j$<Y3u3y*j1$;{c{B!e0U3FOR^XG2u@N9*<2^kE0s79MBQ3O}ISlB`(q5O&TogNj0Z5ss^!`G6sGXt_UyT-rQ~X8v%E>0VM@Ql6cF?EyEcT~x!?O<u5B>^9b30G~?!u<|skO&%$T&n!=^MmAgx`5n|?)mbGGmtWj7K!x0rtj#9}`;s3bhKH4&N*5eN1qj+~bDzh{_O{~__KK7#MaZ(=Dp%`B*Y1mkWxn8U%<AbdP7Z@tBCaZ?US-Q@@(cnW8V-k765{9~Rt_%eT_DBi7|9rnHfV}C6{YKrO5Sc_!7eVqkH0u6eDNB>59bH_F&Bu_rna2cSw3%mPHrrnA8#j42ao^kR2&K-B1@vlY=3<zAKRHlB5;?|fXdn?W{4a)k;-Z27r*~U@&upGav4V=Ok>=zO!kQIAEP8si(SjDYK`<pQ{cd@v&2*b)q%)tFC7&F5&QYg4k~;I_#<Zb{4bG}z2g}Sz{fIM?M+l$zFsaVcZ^v!VKu<y6@`{#B-&6Xq9%AArH3xh5o~X(bkXWj&dd!K0icdRK{a@P-T|}N#pz6lFse%-=};5Q?~(SCQy$Ai#2|5CfyO7i5cj^=<R7c<5nDRUzxUO_Awok^<`<t-Q@B=pJ#f>0v51;UB8lx?DY<U25qFZEinCR-S@3{!AnTa$KWDNdflpV~(UI7g>@|cdd_%aR2(!$(w)D|*MC@<95f=tY2S-dO>VtulAI|s_J1(7k=f<ilbp%&=f%O|~z_Djui@}m#-}`P<-^icxjBt?U26i=Q=Y1f^)aT2PL0UdpAd(K#$L61WDY@!L$c=Tm(;r>aRLA`MPTHN~GLfk`dT%iGD(@Q7BMO%rYHDE^-l5^WAQ1o<B1Nz}NNI>YBRBb}0=T{Mk66#af$Ej%CsFY$N0r9=Y6s?<_XkYAUy%usf8SejKQ?GQZrUEI9VrO#>q4%F--Q4qTJkAh;XPUVR7*qZ^UuDl3(kNdPlUoNl4UOy7F2MSo$Dya!x25}jzwM}ciBN{N(`=<kt<1S1A8QKeFhO}t5hSbX#{~TI(+hbPmy+;v|TfBNQ;Q1CT$NBUXH@J<>3lXWC#%hW1bM_hszuO0ftKqVG?g7E~+N&%3NHzssyRwU`iZ{3J0+R>zU5NDnFE+SW|GDm78B}sK%+wqWAy%uU209omD-!9J#i4_Mor;@7!>xj&Sys&Why$+2_nRlMhGfC)`ASYLS?YfeWgnM7Vwnbb$~=N|)Ht70`Muwu7`5iQE+uHWn!)!NZ#!zk+C}tv3%nWmy>|;43+4xv5GRO_*Y!J8Jod7-h>NrK|{A^Z*`Rp2Bzh$WCQd!h*u=gGqT{gR7eYykk9~;iR5h>Nu*Ls@z8An{e8M^;LF{DA<<b0+WLW8P4{kqep#5<xRu`T(%b$b+PqhTpGbd4_t?vp1~?gJ0V&CiDn=-ztn+LP9(m~3Z#`O4+HIzz!C`)NekPnKA8Ec%C?Qg5(qd|!fl0<CnUO&RV7VhmGV!emdNa-vtO*DTgtgAX%?zh5hpewuEu2dOZ`@<`e>oAlIzBNq<69fNXgt8N8xscQejIu%~Hjk6>n$tPwV@N289!5Hl`1jg0!FIT`9*AmNLec6zfXk!EW(OIX+Goz)ceK9aAtFMt|L@o_l^Cw}?DZ;tghUTVhw;j$6FaDl{F1^R1*~H|v5$za<i$9$d+~T3O!Pvzyho87C*{t?I$e8kXUucU39TTTa_<aQ=%~Qu<k>s$Wc8b$kow{I_g2%$@D0ZY*17HC-a7UDb44aqgDshr0_cxvs2P)aKY|bz{|OxYSYEDnP|uCsN8H*^i8zOdh$2A>&0M9*X(62w@7|A@k8PbCs5vR#X2GO$wsmEX%U;Bo(2=k-Bb2(^_n>u(gh2x%riZ7;3{eVQS_cac=o66$aEpYm;fnyXbHLSJ>GU&jFgR{vK50+}R~RCjcz=2vI2HP~TDQ+u6=9{^G0910Yw|WLDo{v)@QZ8#HCixlN4?_Fxoi!y+-%p{~Hu<Ps#Z(W|u2^cUnM?x1KZKaNz2K-8zM;vI1*)Ny;4Z*%acj?6boXW*VXzhA*WK)w<yR?c=ipxm_o+z@>m*8U5oVq8I|r`(&cq{EK2@kT_&6WbX#J30DyJmS7~D**4fsb<p#HE?LwxEM)uG}_!t*Z{CKq_23AWwqviwh^*pUH!GS#g>av`<n71Qj0T%@j1dU2=X^W7`CPlgYsfvntd!UGGm7fo(RNzUQ{{uRxunwhBc6ZBf?O!SY|D)&0bZs80R{R<YkOfi)&|MeNNc?##l?7M1w1Wq)t>bXp(ZAb1_$ryBuoDi`~Q+FhD3Yl8~aLhBy%e@TKRHCl?^;45<R$a^bE?S&c<xQB6&eIE-zHEF!KM%ZQ;`MU@c^d3+0Am}+C_o9wNEPHJH1`&xZUc;VMq+0Xqo_Ve&c_VfDn>}RkhZ_7yk$U&UqjQ#xMIs3V=>laGWc+vmfP^AVlPAj6V*w5ZgGwqX-(o%*B)$^*-9aW|A6}2EB=c>{j=R2~TG0K+0(n<jYIZdC*OOyP4NpYs8s^mv!{N}6L(yg?mYt|eugr(z?!qTw_OE*smOS3s%AS~TdSbB3!Sh{|xs`NQuIi2&Br!C6+@ZF#+|6=v~15igBWO+P(g7NOZ2$73vzIT6c&|t&n9(Y(R5+^J!@lYf@*m>iI$0u8Ay*H5-|6tv%0aT4xP2>wvpHGs*@?m!{K@(vt26Igp)^(<cLm;r1=+cQqWT>BL#lkBz!!k>({%G>N$&A%<%p$inq?JfC!Fe_ZJheSDp(raHM{EvGG90AXVtc?1aelGfAS6>gR9}aCZ2AG6J33uMr1UB-gRJPyJ(X3NeZr|;pI*uBdUtKjWk7jdz>;w-l#ksU%yX7rVYIrpg;K^)R2rq8B@-(ula09*LHaDQLM>D<BpnhW$lx%y5+-Uz?o-ODs9a8!pw8NO<)zuhfgXsu^N@(P*p0|`5pM!>s*Y+Y%;iCJ!cU3>zO6N#g}l*5agdFG^vbScLJ=q?@6OUIN(35arsh6ko?d~<`fq-taOqW0tV=f*B*#K2osVFI*ITiq(T8OT$QrF!;uJ0s;bD_@G=-sSL6d}*mip9V&_w$GOrNyY=E7p7-W($kXrwsBO8$vhi5@;$CUb<PK*>*ml6Q6!!kSifdnHf`gq1m_uxo`&ZHbkbf?2Je<6(TKc$I(U8}-d^=oIuZ`leUkR66n8BZwgXNT$F=-)ygj^6Vz*X0Nn(5-nC6UN9~@X0&xjaeV2R@m8;-?zVbmntEk358tiC3k9j0{Slq9gzv4=z1AfWKCGYYlH735d!;+;m3<X0^To-rWyLH{^nc~mY7Z#2avn+ir!>wO>5iHYEEzd3A1Bl0k%ncjT4X8ms!HA`Rl}`fZdoP^94W?)IwD1PF|SYQEb}N+)r~8JA&cpmSW2$eaYmX2fFAm~*{M9?&)zJirZ2J@cc7swa?X`pon#v~)|B03p<|h`%hzkAI_ZFFrQx{D&Xu25pJln;6|D(7I8`Iq(S_>lD?}llpVo^a$9UH2$Z;xsTb^)M87KC@vZmS_L|;x`UeA5`XaB;-<Reg10(=C$n-7cRShXtAa!mFt$gU(M7UCLVRL{M2FLs^y2%Q&hO+~>P#;r`QHkuT$gTU9RlF|7bujI{OM~l{I)qZp+1aJr;fJ9ZjDYCt5afxX7hG>P)6ooC-KfG1u-4%b?k!T=)JNP0nby?mG!i8J@Hh*~wG8T#zR;Xu(9Vg-#soc&4BkIUCg#Dzm;-r11lz$>yB?K9S8XCS~y4UIxmRk0|@r{;}cU5<PzTc%E2fts7h-8A-3`R|S8jlF<guLTSlmqeAV>K0^5o33ddgFS*NPZv@T!d0DmWJE1&hpqxlZU;=oLjgwFqtaS`IPISWVNSiRlKXH)|V$($kX-&@OJ#{BRS%TKDPKshpG+55RYK#QnkJ0Um6N~tgr(<2AjQeyk0Z&@}8U8)ri}!Y5tdN30T-ze0mSJzy56n5r`woLe~cCz9on-uCda}mk~t6Twg!q8bi?WTKJ%y8XxaOG{!cBMC0}<(Rda$pw5ZFp<M<J@hos)#*a)#<O9dp!Ovoc?t^0ohN_GmT(sE1hqKrLE8VrcUvo2ds2Mw`G!~yo{lRgOo)8Qi7)Ov<JdlR^$-3cR{FrOXhPu+)O<K)@0T9=eTKu)X0MjW_2^nVi{K-CNxu8&1LZ*{WlIICQ1c0)v-Eb168mBWM0lHOUxyc8(Edex<e<p$)7~z_kcVwB=8-OdiiPY8>aUn;y5hs$GM=Hv>iGmeWo+RWnUq_z8K;m-7n;Tc3FjJ_^3nK$yu8)!}<aaT8q9F4?v!4!!)$$JKM&H<>EWkom1XNP`3>8|gwu+9-_@;z)OjK${E_eNJ=Sio#B*am-HE;h9{I~by!~sGdvC6TI)Z8zqaBTsR5m|;#4}#zwS#pu*%!?>y93;1(&)*tS%nN}920BY^on<rz9)mJas^V4}tALfQ7|Zr?gozmdz>oeNWWYsI)l!hVQzayO5_Yq)ck!=djN4P5$}G;U$O@WdMNU#MU2jw2^GcK`IOdF|1A^7W4d-W$P?a>UilUje&bau_n|+m2m4bRVvg0h+G+%6nx#x1~yfP5NFRgz6)#_g$SMfl2_M-!+;t@$fins@u8#E5V$BF9&RuemzPYeZ@hUx%F4IZ@$aL2*SS$~X7^c#kA&;7^lSTva^YfRMu&Y2Gg9P$Y_dsYRBtvax`K^5l&q3t4IZjwGsa3e?96jgHqpYnYmkC?yl$giMaKXu^w)dTx+XJ^BTJ)k&=T;@*t#-~zmD#AX*sj=#KlD3DXFuO_#LKB$}qqw?~phT2;UIt+ulp#HhzGswFfN9id7jFp>iL_(e{AXUBV!T5k=*mjI(GGH!VjOjTxDur)zi2u?=lMmehA;AqTY^g{LCB~sTF<i-W5;0zB~fM>>w?{aqz^`He)l}Z7+8#mEV5Tq=$;qJb(FYVNip{7(59KnBqFqWI*!g9X!J>G#Y#e_ElpL)%@3$IGm0_n7Lkc7a{C%;7GQaYIAV~mTR+8izFp=QAu;=Jd^~JF!l_-V>W%Uqh+y&+)eUp9K6K33>}mtUqO#Nq+mGutY(KU&fwi585GslN>{%QoP@npIU=TEjz4G)g4g=;29Pe7dd-DPtfwbi|zJ@v^I=w#LCV^+MDa{w$N-!PlQv^D#aW5ebFi7Nu*xURC9Uc+GBO;BQ;f?UzTBKh*WR@I&_${Z}7DRx2UtkBcP)_xt7(kyH<#qQDa8MBv9q#fv_M5LriM$i^ysU`t;x3xk10^XZ(DjDtaf9o7s7Xi3U2tj_nV84~R*K0ZYb@j@VP1S#rXxZ$d`?n+KsrN3WRm7+Gh|LlUx?`52*zVLJL;wZculdzIOaMQ*rYm^lt`s$V|Jt^5X>Q2aDLT9X_w{J1n`W)zZ3j^Ccok10z>8El%;V+sbUV)_eNWAlB^(##d&X2Izix*%w~vFjzwQB&PDLcG)S~rDG+xSM$DCcm&xgwxTs34V>;zr*wcQ75n%7jvzSs|l^`|2$P`SucmWG$_ZS7)E3Y{J_y6)oQ{w_A<vBGj5~$^Q7Os1qJ)y?M?%7_baRIqAGdYU_h+lU&Gbi^v!Y&-n+NBzoUZENnij+P)Wp5@Qy_R(c&+@~iw^>qRKNdf;qv;oY%0kd}>s@m@4By;$w{nYQ`vooE6<WSX^3LKIFWb$|-Nw*ds|7(gqFHEfHj7%&l|s-{pqXBv8A7dD*mKj)*>t!Fa_1URAuaD`wxn!l(aLThW}epAyx`u)??53a0`*uopx*~BCD>GLxrd?_xD1at3^-Y=NK{;5%4mA8@{74JRj_X0Fb>To*q%c^Q3#j0c}W%kM{?r_s#fB&YxpXV<A&IKr%4ZRHtYcMzRK@qTZj}*&+d~0%k<z+;BYY%gJb~Cn9uM9fPJxnH4J<n68{_|*~L{U)&?caUy_65cf=PoyAUM+;qqzG@REth`xNFxaU<$1v|#Zo+GEj>P4HK|Jjk8J>*Riy?7{ZA?ba0Uhz!~zw(EIPTPJh7rP-HTaT4sXoxpBV*#uvNlAHgkt!!uoQI`}5*e_?Vzy0}Pf4;TnxBcf^3%|AS-y46vHN{&af1W@6$NAHLz{i`{yxV*$m;Fuu{6vAoTSxtt{`BYXHXrYcnzx31&1d72f4=Io|Nm)N@4nHW{v-X_y!cOo;EjNwKj&AaKgW07EB;*k?q2kJNx0J0H;nn$TR+M5(r241@0J&@zI*$pzy32e^0h5Y(_nv6oY{WSyW{WWv!#j{mc{q-&sfVs^fg6L#|=z8^vHa5O0;aOB#i7R1cHJR!txk$6ERx<kgaPggLsZg<1(rU_KOh|!|Y%2eYJw25K+s2ru`G`Pk+C7SM|o1{CRo)YI@fjKV&qm6;8k{KO(b~*~QzLo8^~M8ct1AXy|OBJ0&sAvtw$ySu<KyZhU2Nk$~0Nm6v<58!VSpS$yJTus&WSMa8N`lSb3s5ir;6T%ujGUGN&#=@eM6jE6s7p_rxfyYN?zar48*ub$lzh;`#-oIe!%(=A`opW};Wmc00`Fja*1P_&AM6t3h<N1a>K8`sYmOn0CZpep@|8L7Ob-%I(ZvbSbG&;FeMtZsbd>35y0ZvArh@hfL`cC|KD20htwyg1en;+ox{JHOeh-{qdWm-zv=F8GD5Q5l+Pek$rAojsbxeO<YoYW_^;Kbz^A=db(HE3DfDH~!N`vXuKo`nS5DUK#(5pB?+y)f3JS8-H0`jK6tb*WN1CNdNlQxO_J*u4jCG{6%1^Cob&li>82WY6LS>w3Tb#GX7cv`imzrAGxE7hP!yh&jzoX>p+x0-C0%R=TUBpZYYYvY3pLk>P1kAjlVR2G$e5A;_1NvH>eXlpg3`4u>m$f6`X0gaI%WXmfKZfd%`UK(?Ayy9r%FK<%+*QKKLI>Mfw5Ig-2JVlbO(cO^hburaYtVp>5RH(6^CIdvf4A)~<R-d3MU!hP&wFA#9@e_n7H74^{~28UCyef#MC`pIEm9=*RV3yH@v_{)^i>1DqkREq@#ppRH?tK=etz#UD`afwi7Jp>xfu8ek9`>s44K;lJs#MDtITb);@g!2n_?1ssaia4`2Y)GY~2qeB3IWjh-xP?Blx{UbZ*hBg<W!*e<CmElmW015+h+oMiQ)DxEknXe_#N=r>gEFUoe`MQpgC1j2{)`M&5iAci*!Fphbi#y(NZfZ;x7G>;Rkd6i@M_VE+9fiJv@bW;+=I`2Zpw?u>t;n<(5~_|Xs=Ub+aAZoSzhl+k4dM0A2raShJEE$##FErk4A+}$9%|GKQe0$3d3~1R{!|?iTzb^Y(iy_sTg?gEKaAij!b6&o;wh80>Ow>-nSMwrHfITRdn@$fGFmxE3uo^c7Sd$NzMb*vje78o;^n>wB)O&_6+x*{J(vuxG6Ivq98KF*_2AKVQ7|{u{qrrXad*8F2#(Zma)1UI8CzADJRvFd$3g=SOV>7e5Id+Tw52vYFzRljkOSywzL&)x+H+I+FJ~3vIIj=~lW(N81eNb(C|VHzwL0vluNMEwS7S+}k#h-MVEz6UmZX`mBv*kXrF-TFv4tE0T^<D_F$oz^s-qCffYFkN3`1XZ#w`o<qme=_`w{uOO<0nlIJ<=lXSc0@B+>>96P(1%-8SqfGepUbY(zmLTvz!HW!+Wo3j;XdEpa86E^n))%UdL(<X(u9Uw)O!W1z}oS92;}o08@z@i_F<t+2MoB){1#H1&pXRpODEvT*LF2XJRJ7G^`)#WYBn$VPh+cl1pQ1qZeFp4c69j@E{^BLXr2x+pDK%C>M#kt~tZghj`c6{M3Z^&O29Z~AS70Y}411zG|pnX{Zo5@e;mBQ#4p=biRWJ&eLy>Bbbr$9|^xxc|%Fl>5>aEu3fRPvzm{w}9zMm=aC3y5(LVuQ{V9reAWO=$9g#S{h6|YQf`nh%>~7!d`MHR4Bs4*Fx$rWfL!{P@JL%h>&;)ey)MG+zR^RX=Idd;Q(V0a8`&2$<sksBWOH{4K-Bz#uN@E#6@qiiQp<`R0n1hML7dFSIrDt6R9E^XEP_%XljF0e_no+`yXDdulU4-ImpBBhG{D0!#4%!)wvlV>e4h-t2$0=Zsw#X%*L>xs_~!%#1l&@H3d~2G?Kx6Y5=A+nHB)FsL|rwHS1JCzj!)4VNaP%XEK@jd|fmiR1_R`bW+`55Nek0h4`d~MysJ7G}McrLovi_#>H9YtDZfpHS{Otr9i$|_@+>{Po(L4b+Kxaez>Ia3-Q-|ZUmQ9Sh^5@0`n(;{f`)02=5+>x8m1kQpnyH@_0f_dvr;OyxcDi5L_D!=$mJIGUL#(OnD{V%SO!)gcfgUSVoS6KzV@@t`bmD^N;KdM~M_Hn}bs@52G*2+hM2+&E<<0i@%pTH|1pUOmManC=Ae{-7(I~&muXKO97?#-bnM30n{%wGno0Z^&C<m)+@8w98EYepXUcmykf21SD_fLd84KCTlQ?j+Sn8Mob>h*B(Rc2)}sf>BADbSe;y1MH^@RRpXcO$-R!JyP6uZigLPGJjbrl?8|5*C0)UsFa<wTDQF71*PeFnb%~#@oKTQ)(In_>jk!y0$y~(roCOKune<K@RlQ*?|yU99oY&e-TmHdBnR`>xc-W%Om`mIH$5z|C%8Ggoajq!*)_3?Lc1c`=`*EmtzYj4VKG+%=tzI4KQ0ZJOg0?;lWG#e;tf|A(4KPW7!-67XLtBFV`T}t*$t($jj(UN3dGnOWB#idHIU|ZQePMVZqOzgX&Mk(W269I;&w{xQ)y%OEEZhY_eM%+}=yJ}1~ew2#$h-E4{VlFVLa1o{|x9vC(VtRR<1dF*Qy-YI`SgfjEOgCU2yH7aZ{nZayRc|?kU>IGjs-p^$%S$SC*&AC}T^Tnq+*n&#ZfSZm_)!*Mw!GS2Squk%PF>>mM7sQ)EXqNhr2Vw*q+5)O;&5CmTAeMmjDzYhLrvFor;%N)Jova+lf6nmi}^asU{|W_Ju7?&$LoqjWBJV&J5eX2W$vAeBZcENVD8&iu^l^Rka=jB1WEAc{$(;btIxW&hJV`n+MV;?`<8u@8gf8y`6T7GX^T}-eeRRg<v&-ZsU>n}!;Nd4ZD+%p3P%YmDYRh%SY2_&KOb;pGsxc5A0NoL-_7iLdhnL-{N&YB|H7*q<{R1_MeO`u?bT!1L2Ul(>a3}l3ydZ>ZgjZS)L<P`u|ZOYy{voik&}~Ts;qk`%-j3Z+7=^h%})B=-#s#7lKYV}il4b3-J>gStC{=Jsru7M%sSWR;Nbh$`FtHs1iHr%j;vZl1}8fVaZ;vfgPDKtn1SOC9A6?wWXu_^W0A9K#rwwB^_+O#yZJxN5btS6(L2?&F@<1~%kOezNYH>`dvF8E%$({5N?Q()QGtwXl81Y*${lnSRi2~=Zs4Y#`8%fYzE{Pbk6CkD9gvJeXi9BIi~x)!L<~Jc`1?RtkK|-V!McavCN;4?=9TFlXE=H{kh$2^rI;Ry0>_#gjx7b{urb2x-}5jv=wtzSLX_JVZT0ZyOllxf+4%HgwE;3fYq$kc-hIcR7F=TyB8XiLObRMR&9ZVXR<FhY$lt$#BWqq=z<$i_uqrCbU?Jqb&@=5tnSw?^T5@?Jra+!t$eC4W_!hb&#c*8FKwJ4Xd3mNY*Gdj+0!uSeQdiiEp~mYqx{V)@X`rHLAr{Nbz8)Y9LH3d8u_)eBv893{1+y`bV&qrU$*pQxDsxNM!%nv`!~*UVeD<1xAIzLGiRPj=t9KL@omK7w^}>?3xwij*pP^;?Ld$Gt7EP#sM6qSjHnp=M;ERD!AXFrcTst|wdS8Bt-gL=ZS~$~@)=iGC+=9^Awy>YQ=U$3g@yg_UBC>-%Z;)Z-g>_iFG*3<8f(PNUx^m9M|79Y<EOqfCmaozn$5};xCF$?VbkNJci6rS3q|mv-l=p6wQ+IwcK$=C1!90gtF+Dc}+)~P$0)01+G3~Qf2K1(SV7ED*uzZo%1-Kd6(#h_b2d9z9YM2H)KeJ!u-c51-{G1m*CEO1eqmf6t_}&G@6b;{7lMaH%NH^Dw_P&$%l7e*g777}<LtDh@{V0(?6ZUemy-r1q`-nNcsCqd&C!*G{`vW3~$7fw>zN!LqLfr`i35nK&lZp9oa;mwQx;Y7dOj)84cUlWKJY%JekfDAzdAQz@?i5TCX`f#?qA9He3Z()wzS*&4mS=u<kCCt|IHcy_Wj4`RA`&60yU!id>6ng%$d0)P6eSOq-I2^HHf#}gbB_bRMJ_=1ZqQ}dvS9O%omBuED$@@$b%^+nz1Y|X-_Sj>ogUbDkb+>JaR?fAY{j<X?h>xD?k?Zxk;0YEZaUsW5|2Wqenn4shb5Qc@4*D#5Sl-7Ie;TA0v@O3kz3~WRLMSs1Uu*VRrjSm5DHp2DC8iKLpmtg$l-srQ0_~Yqmrj1kNoNMDE|-lKL2Cb_FmQj6@M9jniB#uibxbzO76XfP;vgCPgLO7sCi$z4YfJ)(;Y*QXh8|$2`V>ptJOgSjDg5`tPU;Yl~ZK!o{7)|wlP;oX&O)qSxf$VX1;ZuGAl?D*MrO(lb@W#cEVEOrhGDsCW=X%r9JCPZ1G*RgE!phzi&8MHgu<AB~Ueb&!1?AB2Y~~X}68Iu(f=fbbuYkclkl-K)*Mi`MlL)Qj{;QxhSlH)9&fL^w7YK#JlV%xHkDt%dw$jJxbt_-2QAvTvZOLnrQYdUIsOI7iCy!PM6EDXR4MQ^Qegld+qhYa~nMv+{|}*Ey@LVN$Vp=raa$%<)+&70Zsu?QqvEW@F-uy%d3FTn3qEZW$y--3WY@*sG4n=I_`a#;z10Qck_q*ST-o)#aQMa<vScwl#_h5PE{t2M%pYqtSP*4Y}`w3ka9@k9Q(KzgmDB}QUUCUU`rY=n|BbLQt3U?30rYQE%g{CgOFO3BHhvQmKgBRpSF#1s4T{2W*<A2`o3&<e2|fLQ_V4*AszI)lP88AU8fvxRq`cre9d?L=RYti9z)^{XOKWGk~_1wn&ROx7~TZ2+w#oayMjY$XekJlST7ad#<U+9`Q?^gaY5t$tK4FVjh&}XmnUnNnnNCBdxYPV_G(tLSwoZ%X^Ye-Dwbqoi}_QzP-h7;%j01)OF7DX%t~c!NommnN>OKiX`9N~=pZejMefZI0kaBXIMJfz==w(P^iT@)rfN*RhZ2f5Oelt$uu_iT>9QIG*@0<n#WlFEmJ0!=xyY{y|LI5A<xouarMsM+s@~I6-L!n{9bK{I4-3UT?s8U@B-7ac*Z>39L-;qc<e0B1DHSRSH<qiMrAYI^5UZ)V(WxQB*7s0I;6tnE#s)3NhK&ZRDvPH1DA0rQ^Wm-~Z)lpTYznY)Nz^H~Aa2l4>YG72TJmD0Arm&L!=$M;LwR$E;`XY@l)LA~o2X+nS1a{3J;2}!tlI?6&9^Z~YcPzmokEoJ)&vp`UE_*DS14Nv^cwjp1zlC1F8{O1uv68LcbrKM6soJ?*{P1u(YABf(Q>Ed!CPlZ3123k{Nfj}U0cB@52O|FNse}dE(zZ2VD>2mHAsGR%+UnbbJ7G5Pf{vUdY}wLQ+60hnIdYttFS4R7y#>%#n+zZ8OdowMnm>-k0M_{{vHLq4vNHm89z|OjWnH1X7uceMlrum5PR<}S<bykW7>E;#!sfah&eQyM7KDPF4Ej$5TGJ!YwCAALpeB_i<yvbWsyX5GA21}3vCy~P`uIO4JH(43T3=7gLvlK3=kb*S(utHdTZlesrqdBy=fOcGyB34hJ#aM+qUs7xu}_LP>6y;1#dpU_HjSk(b24oqJp-m4zSwrX=}QIko+nV#gPsZR2yTfbJ8g`$+katW+38xF&}Hj&0!<3y)-<lBGZG(q9zE*HlHSmXc|i@5q0B7OaRH`lXa(_+9<Pa<oLnTHHx~DpSG;yzj5y>wWsNUm;JLJeSoK5#?37YZoOaZ)wNIdaony4TV<-{UBsE?+WZP<7clO+{rKpY?sF>k+Sb{=cltSVMV`%+)5mRlUrKM|m6R-lGX*I>Q;<40vYSzCG;)#!$#P(x-H4ld-R!5II;3!5zw!!uG6b)-8%swdWTn2!Y7~~dVaNDIVM`vdJFF3RD8L7A%c$R-48<|fEF8o5Fxv)mGotYvAuQ@QN0oc9CgzP|pJ%(RmA!$=aV)nhaJ-Y1RG{Z87F-CvZH?i<YN0er^g)QVe68$?D*}Z=mE7fs-OkCvGHwTc9(VrG=4*Bx)n4joC~MsN9lt`TPuXaCJ7?<50(ir+tk)dj?Fr{-a&^b`>(avPm#V+SDeOx~EaN#GQ2|ZwP@Qic*#?Koo<{zjJ#VXauunOT;c*<StS_;1$WH2)W^mX!(FUEbBi1k}$P+#7wBEAu9;Ki3U{*6b^M~OU(@+FO`$ZLyqaiE2RlwXK?>P5t9#_O0c_sCZaaQ3D<t1yg&Wot5hA__oZjpnuHIsoYm8&VdN!dY1$xXg;9~JM0!rs~RIuAEN*uevZ(8^FQcWnxImUNw=5Zr-Vu;5;pWgtu?e4|7IcBI?aWf_oS=>D!wF|aCfo?j3WPgqrTSf&^{iU{ssnO|5jO`!Zj`=b1Uqgyp>$eP(xbNs9?Sq5LyrdnU#m&C{QECVv$Q=)+rmjS9<38p_Oxh4GV=at;*|AYt_D2RMPi_3h0_cO^Y4v3YDeg4@1BHBDsh8L9?Cl3yczf^TCcg(%~YaDQc1I5;~<lmtj*fD+X3GKk_&{u@En$;^3wVov@&RjUE<WD<hs`HC&lpdbxNQUy$m-%eX{D@Y_9Ho;rgCf#_r&=YrRbvLcI72YSMnFV~=dEPj(XgDj=FK7vHE`UsNCKtRMCYo;3Ehz&R-41RhK}<Q_(_Sgg)MUya-)_yXwQ-Q|GYHcsp;mC*y&``Q2vJZ^;2_D;vCeJWal&ub$kVjmU)&hORg1*u$9uza4QWYT6DK(qTG`<&&)(HJy>4n`An3!6=u~%Gf_OBiHJ!_=ogVQhyhQ|rXlLdKQ$8xktVbryA|d~@`JX|PD9-HZ@AMrcC+jzrC9O3wM`Qg@;7hIjyt&bCgwZMJAw1gs<zNDykN$;D?U$<4BQ&w7E*O*(~W$qt8<8`Xa}Ef#tHGiss2!i?}Gmx2kawJ7HgW}<wvn$7Bhv|8GLHk5Wvu~(ClgBM+-iyV*zm<;+8dNx@94BYDuvRmJJ=FkC>ZuJJqkTlge+cZ9z#qz9A$xPct-kMHd@Xx_LCr-bR0N;~(L_$vg$q8IF2^(4$S*-R3@~No~)M^n{XQbZi7Z1{k6S8jwXTPFSj{1_IcEq8{UK*)gIH5Rs?!oewLSKPchAm8-JiBV}>9MQ>zs9>{emd%ftE#DCugn!*5bB{H^cCW5n(s&i^h&Fe*;&c<>A-6_!&(YCFs+6GCmdYKRD|4G-ZsY)6dOQ0o_)ozO=A+GQsJ%>N~x{{DEJ700u?FzKVBx7CP<8&;rom!t(Scb$c8I%<YRk}A+sU?iIt|x?Z@D}oDN08P?$0bjVSkS@T&S0U%#C;8NLn1y@XjB?9xL8aCRZsKc76pTh4ABn&xd{^iH<_d`haJgc8MdD`<1LHS4ekR*@o|Mm4`fM$o}OQPFqjWEN^Xzk_)a4qHi1@wr^SIwzYlrVA6LUWe)$(Afilmn`f8Qf%-9-M1W35Br;&D^?RVz(nmaT~pCd-WlR*^_I}ixPN0wk!-QiXdS~Q&i^2mBM>c@H51N>_1NYpm8H4M)nl))XEd?T-}!8a=k&~DJEs7*$n!;Nl*U;$GAExOVdh+<<PVDNy_MhiJl5`7woR)n>0iqZg9tDWn}6*}Msk)9s@sqb_<ZKp=+Ws`IV&<27YHcx}*nY9g<kK8t^9FBYeN%6d^2QufrO4c@X#qFx$cEjWyUi|s*c<=G+D-F|sP{VYyhH0N{m^^16*l9jN^R$<31DEZXta<#6=82_w{Bm%`J1@w79$8*3bg*HS8w0Ezj;WN#)K_dCV32*g2c_!eW6EnxeO3KOueQx$PO0X+jj~9~$Xw<*56D(c1s#P6YcCR5-_hlyrHdMF!wkfF6GTCqVg-hwDAM<9XX$;nXZ#BO1=i%clW#M@#sTFUt$x85m|H|Ro7fP^08<{2X{{PSR^)vRb2_bbMT!c4%}gJ&1yph$t20hk@icDNqU#H~D#VhaEzn!KqD`i4#B!StTPe86J5WF{o(fl22WvD_H*!U#0d+Z7%zS{1qro83;gXGEFym=(k-xbv!2&h-DZZ>i#sBmQdxG2mcVWxCTG)i)5z*B~4h3|E!sVNpAOaOY=XPF9Y4QE1)N1gmVl`G~ApuJjc5WP4i&|J2Hpx`(XU+niE=rXz(0fL5v3C~DY~1n;gWyrXN7tqn;U~vKCEQC2xM#%9R6C_87&6!~Zk|n^kYaJJ*q^^8$S+{ZQ#(?Gr(@VkDU>rT92P7&?x&P@NuaYmYj<w)$deb#+YynMW{#6_vPhsSaVP>?=r?iUO&O$vUWy6^JTldv-YN&;DERS7P4xpxdKZ_3rW6U}gE`({DDDhoAbBcQ<y8SBLIj$B@TKso2ja$axO+kbpL;^RsrrJ0=)5);L@wR|4W6`ZeGrt4ShJ{|2#AZym2ZkjQFF5F=?<6?MQQ%g1W&{*LycxbA%dun=$Y(LOFEGDfWCi+3*dN1R-IWJS{@kg%zrItE{>$5tp-2#<CveE03g1=`#jF<tcTLQyq14fz9jliRa`gn3I90^Z^h3)W<u#y%Cw#NCmGTeJG?M#;?ObAs_Oa98D*v*{C4jutv&hq=DpYUKp~Grk^rV<ZjbUd@~C1O^UgG3SF5Mszdx7|2Fjra^P<X4^*i#(@6eV#s_e9g3MkxvAq9<u(Uk}v!dD#0EoT-(Z<)vlgxYZuq=lfn0@;yfPf--%J2r$iTc<3)u!A&3$SVGg7qN(px%~n!^-Cg=5H-dna;t_!0x_s6xtdMB>XRYE()}2?rW6Dy4#9kk(My8hHzXCocgJd+PTh;F232N^S48I=?<Z1GpcO5>aSOF5k^L1!;heFHl(&()M$2U?8v5CBU!`pg0R+lc7dmez!Uj1;9)%#I8FAi^?CaggG~#mCwxbtS*$sp3gpF|BE=&v^X-4@9jx3g&4>w24YGoEVHys$9LIA(3m7@8q9HZPIKXkuFaHiQzLtPE~(wdaXVEMci7m5KO_3Gf`KbZ33Q?)Eb=S3JUp=`BP?rSYdZK+0KdL43)2t%#Hir3VdyZPTY&av#I>f?2UC;@gf4w^uD3o9CKWYC(s*+Bo%pM|xXf<2-Gg8x0m%sCcqiAeL@0neJ*GVgyc2O@3Z1Y63XHC?0F)c7-^QV{I%7I!t#3sj6C0TkQHHjj@W7*@khG>~-(;RXhg2!U#}^eDq4rLUf@Gh|HU$c598G{I!N=iEVyq$k4&1x^gmyi#n4>`PRvYRMaNo+O~?e@C<|3VJl*3N<<Ka<JZ#Xi4M-(a;w5A*WPZf-}A+x5gDPXksdem{%mbKpMmW@PA6Rq#AR)AK&+W8_lhzSK0^TleF44{2b>Wqr@XoRQ)cpJ9D$ph$l34{5fVKzO2mhR>sukyu{KN;-jE?CcZx3*AIQQh6)V^mYxxdic)u^*Qkd)(xGVlMOlV-6<5r_{*LV2`#`0o5Z@b?(60%`YyvB2W)d@wJbvT1G5-GC74rO-NLwz*^S={g<@>6SzYDu9w+SS@=N{Q_(B7#227{9(1QbAcZBYI$3Liv#CnhF`V)$CT1M?0iazo_RU^M5WvuMF(Iu`d`S<X@=?M8go9ZYynb?aSW;G;%#Kyb7v+M?pj=LOU=!&YGKGDg9267E%CE`GGdXG!FIP-;M%2M&z~hqCd>F_ac0RfISlpN#Gii=$z!k9#pmN4ToY$AcFh;N+BrjWkpC#l%s{m+4Pc{~k(SscgoZf7D?QUOOhQIi0m-JClF^Sps(%T&Inzdk=${)|qkehWKJy(lz7lt{n2wUU3c4ynC;9#a@lU&SnGQl_W?T34zT$-Nd{}jUPZt1f&i75pKt7p`r68y@&2iP3lI?ck}l?<Q_4=Ewdq_l<k3$4|E2|eJoodV8=B2#g3Dj_tIz0AFuP`-jPDU+BwGi9i@rJbR(}Me}yJB99dKDibX>F$z(z}BbV6E<$wM78<wT;$1IH6I{y=|6ofkF86c!BgQnF?yP$TPUJhamD6b1Y!B^WGDSjbAloFI$S=3r;m&_f+P${ykeS+N(^A6R*N37?m{AeQPkgQL|8k|1wzAIK@(wxfYISnw5c6028<j5MA)<Lwcc=AVY(3bw*H}bM9S>t=?(plky!cQUH8*=3E4_Ck8>PI{R|3D_kJ2o}{wU11@m7hZ;CJNVwM+o`ADb2<BP;GDr_WNMNGs;dC%Y{Bm2Fdu!PL}15#^iCB7$KI@KA>kk<`*}Nm}`MMMIv;g5f}zGP`eyOU%w>Q=|4%VlUih$(`t%x8bvuy1VR;LHR(>V&ifMU)K_Djd;pqa3UuBp&}pT?_f(YAyfDh~=&!v8r}`|!A#opZ!1eehzAU&2!61(AJj6*iLL9|6HRBr_W?rHz0#h=+p_HQZ6>H9O^*qF}{28O1Fp3e=qVIaFgT)uZ%1_5S+(IbUX>+V|CD8H5SA;mv#y4J{RWSGY<D1|9rZQ!l*H{m-qfXX?5YCY7ouk_)Ro_Nks=V24f(ZE7?4s;i+y_}`H6nj))`N<$o$cg{d>K=>O{xs-Y0z&j?}T7Tch#HqpuoBeahQW{nc<?a48Ywx_GiuiliFmS5$Z`zqn3MWC2L5N)nGbJy<VhO0hkHLF6hykeR(~(5?X-W02|Dn%iap&v_Q~7$zlaV%AeT@TMkne;E|EVsBuDD5Q~YeH_cZ8$)aa1wFTvjx@wJ=)e_eAG+as=9NW*UZ}l5*u6J*)cW<6-Z-2hE@LLPNweXwY-G~3_-^}j5E52cGf4({0y*b^zIo<u;<#d-msngx)O&4C_P50fkxx<YNFY&lDeTq0b|G??)5C~u}AQ}@hC`SvD<z@6C88~7IC?*H6%-riNxY6k@6lj#6{rRj@Ts4~GMYFckE2Gn$0A!)RX>G@R*mcLeD+kX_<XZDvGojydCG%r+@z30Xude#tQH_xtO2?E>Le?`}`*&s`SQI2CQ$8Hhp5OJt@2;p&pI@Y(E^<1dRIbaHQkGFUGRnge9(Crz=Ps=I&OQ3#!l!Q5?B2QaD}VNt#h-3&Mu+RPs*yL&o%LeW97eRPedN;S?$YCKZt%4*xLew<of+I+^>dp$zrFh1RDIxS-DD6qdfc5G+&NoWuDYCk@Vz|y!O7jOzBs^_3tqPH_{){^UtYF*@}_Rs+`Zi6PIHTX5$9*T;Q2B0t~I~+`HSwt-EMvj?nx)Q8}IrjO#f`256?8wblUbQ&${c@c4se^`&}B-c?mRLwX?hR%KW($P;V97r7-6Ci{+If^nPw+_rJdswvGA*kRY3u3a0tRfnbopDgx1V`4#X^DRA$JTXtqSW8Ykl7ebgk%Amy23s6LfEHgljvdiIA36wA4*;aay$Bsiyuqbp0>|P+jf{w$^q#~t_PyPbzZ5B1E?lUxCeMKjXu7Ji}fjUnBY22FXdb7hkRG{Y~rp}obMPN0>KCa7~ltCmhh1#ki%!&5_TaPkMu{0ML12eq00sE^0oOUzG60r@?0N@bLq1RrqQY$UbxeQ7{o+GeX+$>Sz6Cm6KP^92bDOG=dVJ7Cv@8b3Qa%<&wP%Uj|=XZuatrh*LBDGYakz|h}T^odl{QiIUAsYSnH%g6L-1trB8&**_R1A(@u6EFxyspl_FIswqmDEg578FlzDH!eyIwGV;lPW`xc$tb7w5*h>J-FICU$y?4=Z!4tRA*#w0^eyx%rp=~vcoCB*hB!IFThv{*f6$;`XbMvFr0hO@u8VwqbtTXtEI6`UyN;5&j~Wh)u#WvRli@o0?a!QXxCLHuyUH<c~W%sU@Z}=_J9NS2T3%JT8)7^F9vBF4nZhwQqZW<axd%(!E#<vdTs_xto<RxQRKyT5SV;6qu0yPFvs5H5n+=9Xv;}2V%M{CVYjyHSB?5>Ljyv9QZQ>0W6f2Yo;v7a!-#CBi_GwVj+Vb@XT$}gqi>0?Q?M-+SnNcA(hp5ha*RdrZ6`q)FKL}h65##GK8u~&(FVWdAiexg*<84t@9GHuHodJ{H+j!YgPfW<Nt@tUT&<!(5E=+++_bbZ%Si*k2lIW2w{0dpMbX;gF}W&6ShI0{;8wVOZjjUE<Fk(NU%3gr)$l$_w=55Db$y!Cz6*zakXmlimYWknQ^tlS=l&oaL*w$B>(qp%HHJZwMgh4srr5f-;jM5(BOJ`eV@3FEC3)AVv3;bFvPoZoJHNLHB2e8_c-$gi;6|%@Vhc}>?o0T{?tld%Rig<h@GbdU(mhaNvB;TXM!09=M6);mwel#*0>M#SXA=|bt-P5-h5n%$o$iN2HA%gO&;u`+FF*sk%!a@9F+oF`>&#|s0Ub*2+_%ac4h=e_Igr|DPy5+9^E@>45M$6{147rqI0A@f&WC{lD3P2)k`)CVqW@VnLZG7(Q_f(_y?+)u6bMIh^0u28GJI^kE1CvmOBrZLdWS+SJr5efH6Npt7MxbMJShxC&#wt4j3jrB+>$+mRO<im+5`~_q=<5e+{;U$sq!RvPfvlObmmRH*<a|J)cz0)<>q`s(QHBl>nBt>ssGOpF<Q=%+~^RsWpAx-_FS1Rr%Ti2);cd7J<V(R+-SKGk?KjWWq;<iETivhcFRLjKR2({SU6m%CaHXGwCv4yH5QlU;kL`NaBmHwKkI-~2rHN6LV)a_w^+{mM{KB%J*8It++W!c(v3v^*>mea$Y^}ZVj0RaVm!`VmiJ;jM=XM9x>_#F#bTM0-I+>Hx?;490oq*{Eq^xa(EO!;`4zi=JdV8ajlFjNcTQy(Ceo;4*x_;c*33n?U$3+&_au`i$R&xfX^Dx*o&97u5w!)M_N>#^pL1W&ozsB5c4fOvlOfhF-&-&ymBz^4EiykRNApFpe>648v(FG*(Qeg<fIx6!QnfZ0jbMEGkOK&8tAp8T_)$icD?N0XX`3yTIj0wsIOwF+_R}#Yd`~}GZ8FpX=EKpJS3rZA-ZkM?mL8_m?kIaZ9YDaQy&IB*XT^gvw~x_4-WViqSX4^(6oiEY<F7+Xu5rx|sb%>f5xM;6)HO`T0exgZa0DAMs6$JljX>HOX}N@u3DZ+6$E`J_t!)CTu`N=~f<Cjbo07&7B9#2@&bB=H;Xm?ttSLP|=&C&0Pj&_b+~0>fH_fOvGG-+&g$uML&sE_;j$Gv)bVK$LQeujN-1rl-QzG=j^E@oxVf~8sFVAqDRh<Z@%`fhddonhAs!SUjg5H%8yX{}TRLjetSq_1W`p{1Y;Iqh$MMK@<c3Lfw*yTx;w3+t~xzJiCLNMU}`)|=A*iUPd=i|=dL|K>s;D5%+aLcJa7@GM?x+EFXKZ$W{8Ix%<C5v^M%`Ns*;t^1@8l<OPkOTA;yI_S*Tzam01>3Glkr8F~q5DA31@j1trj1JCLsPV{L!sY!O2(Dkvh=EAFM=g5yKZ40Hg2!lV94p?3y{<Pa|=znU$oAZd-#uDNzS@QtTOSl&U#Z0(_5IcDvRZ+r-@pX@>dkXnG>}*(WQCcVYY3k>M-MKm4w@V;PEqxmS>}SH-ht_eNV+1kT87Nf;%b;9P>73fbL*acPMt7X>>{zWnjy<ASjTZeCP+J{@ldRLJ++3cNX~CXB$0XnEHjozxwJ{A2kIoTYYKji&kgE^a6U^jaKJY$jcNlm^rOt$3~j_i-xZhGVX?phKEAvS;O1bhHamhQ@SHoZ1}_2>PCh!R@{Agg_JmKRZ~TK#<TY3$Psy|v~-^B4}a%L^5I#uAKGf^2fMLwag6puiS}(eO)hkk*Gaqx_@Rd!5iK{<yjmzO`EJU*TBn(kr=Cylvt1}oRY5U-xR_%#9?&Go;(W(#mL6BH@xTyjbWo;kfjKDau<k~*zb?6k4otw=D0139YSv})k5{tR6RQ^ie>Y9PI9p54#H6i3G&Mdy<+9CGad4(Nh>&!2E~#l=cM<b<CHFCp`Rj;;dna{pri*qI4$_uwb2&fHcdj9Cb7g0#x!TY49{?!$EYW`a!`7E`Q~da8LsdpOnmBswS<!!UOyjj%ElC!7s%}<Qv$DOZr#mXtbmQcp+H=<Ey==@w+%O$nvL}&kvl+~&SZ1@Et@T!8IYkp^%4a?;r|3qLd@b)(9B}WXBP;Jzf1u1z+)@dLB3Ap}w+shpp%=nDTjBk&#WPvKzl={ky1jPi$sYzmxHx;~&#gJI+Dc({`h(wA>n@X5<N?mwxLGuCxYfYBv(`2KWbNlo%X!;RO&h1CMMkaW(m?TDRNw}+YqM<B)n$v$n^Pv?(CTL@oY#!Dq~mX%55Hgi*$)U;qb%%ct71|J%to_M;_<YyA2L}_P-ycG3-2J~j-BDa3Cz)f*LAFOMY?Q3q=sgB(t6uSiU$8v2x0c|`TA3cCg0`hPsSn;ZJ#hvv9w15BDG#Cb3}!nEm3Q3Afzc;VFuh{Z;(OF-{@wo43#M2kpDH{m<MzT&Y%aTj)Uy{d^b4R6C<TTiN2Ob3;A?CZ^s|7^Hs{^m?|_TMFK@sZBDp_4fOn20p3+B?gzD1hf(d{{?tpOr|jT-U8MQV>()hD1b_2&(Uo=4f0K2wMbG_K)<sxsKDREq0uf2CT^DE7ps*A|Vs7hv$AUm)QpXRUd((p1`hWX&JMVm(e6{m37Pii-+G%)MP#00YI`6!Gk-vSW^D=k#F@ieEPgn`U@+BYKc`=36?78h_L}%T0w9+azJ=KePZjcB7c3Ha_QMpanWq<iZx2;XNF;K!QTDQf%#PPGAy3hWHACkzasj_#N7R08<ic-^1yGcQSL}bJ|d0}H`T1Qx%cqvd*_mf&wTp3l)mN*I5shW<mD|*18G1gRw;o^v<vWhi7l4z|)(Z@a_zk&yYr(w_+nUE3jVr!qLfQN*8atu~S+4%i`?7hpcZCidGG+uMeIoF!&x!2xj-&?nyw#(%zSH&0^(YSv=x=7Ff(XkPPC`tk(Hbx||garbTAdv0Yq!APZO7ahYXn;VpA{0dei8P210t`t9Xn<%S0pt6=-<Xf}*k_;Pd+xbaS+|aM?Y-7qbIm#Cc>Koi_dU2`5>Lzm3;nG;%@Ao1xE{L+eIt0U7)-4*lo_&sE!8V2Cb*KVsYC37;(&C`X(sOFX-=zx#K3Z;OwR@~uc2mu)~uCcNM(2*5Z_Ssabc-q0+tV4O!I&bwr0y2ef56#zx6&(81V(vAQf~G`es2Rv)z2=M}|Cud*C*#Wpb2wE2o?!ox>>jr!_Py0UL7<4PIsy9p%sQgc0&UGsr4Hv_6c4n4rA}`sBr4AUX;Ha%t8?)64WSc^YuwnQ!HgD(oF)89c2())lN0E3!?Jw22BR<;Wp9&J<|ZX2hQ%m~<`C`=!wzhsXsHvq|E5(}^iVw+Z^vvO-E@KqVrY4);@Lhh4eym1_nCK`PN96I+^nC_h^XtS}TR&+sql(PgO}f5OKo6GQ6yO2zp|OVBOd40EDDPLuE$Pl@_;K5dwVUI)2KmNkM2OlbCCZfwvsv?=N+?bKK4;(@%Fy>LAcno&lS1&o#g_6$Q;j2$ymraGP@6rp4i&=HH2>b+>8mhIn#`YC26Tka(GUS_DK#EhDzq5Xpl-V;nUF|=T@!k)6CU?<H1t>_&UJyT#dz||4bTZws51g$LSK(LdETqHa*oLM2I&#&ki)>G2Lm44c;on*V@NRnU_;wkdYo(S;^*T`v84mJeGCN5iX&&a+s3*cBT{+ZYMs~w;<n^SC0noH@O=Ajl!37ptH#2gF@0o>IIy%&;D16Fd#Rx^0raV6hAj?fWw^lcNiJK-*3sCv_7PJSNkPFYtt_F=n5mZ&r75+3t_`S65DI_wkYUSCTxM3fGF_y<w3i4U8w>rBftn}M)aHrPmg3;SXG`2^3YFm!g3hURAt*7xu!K{7`yE?6u|h#|?Tz}5b1<z_c5#i6(=PDrILoGo<!^Si;3yBQX_p*;wOv<flFA6R*-y3&C)F9BO4(a8aG2s_9qQrrj@MhHicwk^6W1YlTuq|Jl&u#%##?tM&kuxiNu&1I?t99?5r3uHLGY1`(;B##r-t7Z90RUxx0iq(9>!X1hqmCt@Nm|lEUOb-04{mYXoxJ){U?bMMN!{bK7EY7TgPCNSGMsvc^v2cPi3%0ANc*H{oH^pJI4_^EnEfBHNq7*m(uJi9r)9+>e|4y6=Va9FoLJ3lWR&<*(Vv|8<{PnxQhx$~d&XW~&g=6NTGF{<{h50U5)#+p&yHoyNdUYXwyKHCv`wzN_$lOG9x0AzVuG<0)5~qCx0x4$h83X5JyS;|#jEk)>apRjxQ8E|O*;Y8ztwiMXuHA&zXI3c_!6n*C#N}2Z)x7?+k04ZIzK_7WnPBcJ=M}GPBDjNSnFnd)sX|ak-9c#10;YP8tW7!dBR`06B%3txx_#R=A!6Ur1}JE0ryxH$<$ekFVAhukTA5&_a)R|T<(nz1bh4f9$KK%n{(Xac-{8K>26x)sHh?>P=^gghzsO4RvZh&PNjTDnSJgBH*j`G05=+VMR%@EIpvk@RYigQ(t!d)aqu5&~#QTk!=9X4-?NrvB#6C~_^X)awQR9;(bk#Kf1cIzGbN-0VHKobFJ$cp)kl?37%QHM7%fJ2+zIbIvIBY4Z$^KmeC-Y!z{Q;7k(8mRo6eHY_K{THwAVWZ;O=xW7AZy;OD6R`f5BCWb-J3T7HeVU1iIVKijERX|ecr*QeC^!>cLBmlZy=3|#0Aojs&ByTFC1xWUdG9R`_vQ88EATrDG4!MgM}<GE+`|RJm+n8eQQR3cp5uwG*CQ=5Ff=B{@LDI9S~0Lq>A~s-+!8I%ifaM9q?Qc@4PkykT1{+>%SKNahh%U;+2)Z+D}|hf@|exOkAhgJfCJ8&GuIo|NPo%Huh_CAEMAH`tAhAv0{H&{KJ8p%dAONR-j~z^t8A5B-j*+ae_7fRSW)hq&Q^Mu59CTd$mtztNqFV9;dGYkn{hv?8C#mgObZCJ$z(Pa(opi8Hi+v%=!tGoFz7nE9a2D21;)Dy+gzSS9{{I0#4FRP_lJKB?~E^Z!Q;afhMn!H(3#9nl1p!odJ}IHWoN>V(A9iKE41`&KEG{t+s(bc`)UF#QlH&Ff(V}gn516f8iaE?}(#)PX5j9U+O<x;hWTzU;faX%YFS{c<aBvE)(bc4Xs;F7IEp>9GuNPZ9qVcx<8ey%QTPF4n>@U?9w9ev_|?7bhbo{Ys)hMUJG4uE70$fH`$7nC+Zb7@F6MR58Py+*}S4xSP$fi&Lx0$OJ8Br9#O&}R<vs4cQS6J(MKa!)pBhE`BgE>rh9PVyP9Z;&P84l$&0er0<w3NnEHjpb#;Ua{^(%(GYIsH+Ac;-`R}_h42HLj^h}V(=@5x;VJ=G!BeAkU_)Q|lj=_I}d?~momw!8D&3RwEq+rehT7-H1!GOm?_6Ez5Ff*s7=pvQ1{i)KbgkDArWD`PMm#~Z1&lDXi@c%fh^L}*08CBxmqd95=Cu(@vHcIxp78nq4z_>k+Cr+Z6+kho2v0L1ghtLsf-7>Z7@CsV=h$}1Y`%UhD`yOSX%7~18puZyAIpb$?f(B*;DZhP+$6B*FZirDx*iDxc4o&>D+9EwXjXFcj!Il~8F@EOZIMDSDn<)5_$8WJWJ*~=<#bow#|BCxP-~0ernG*UB2ee({3YL5LWDHx6C%QsEj)s{u6&3t`<c+fI1n_L*htU*}NuRtomJxG6C}afj^#+x$=qA_5!GdhQ##4QVyexLL#6%RpjVI@8$?Sx@OM+93k)YBbZ>1`Z)8ToB&&r=iCiM74<qq0%{LZziXE0UE&!R&&C!)qTu$U-c{lxq`R@sx`$n%-R&q<^yMB+IiWFmM2$@|h`<xj<FZJ_FaTt>=>-D6T{CSMIiQ#j{Od4(B2ddbd;U6Y}1CF=p3(-_Q&h8ChuS^``4#eU^0n{XCmbd(Gt?{(u?_hBMEObR?EU6q~f(R~Ghv^C@iBj}t<d>_bAXeEKI#Ju8P?`zaC!=Q8QmwO?o$+zZXBClpTq?l8Muk=0IpiqKAKa*ia8b7V?icdn#Nhn3hot+)OA*4vLO3PS9ywVC`XO=S6Z)wcNFDY-#`OR1TcjbV$Cg`NRyR%@!yRp%@UkWr(K+Oh`45lNm%*y1gU6ZT6ric@h&?u*{RjRU<9tRF;#xK>DStTDodV$nvht+3n*qMlw)_72_HZ>$?8X~k;3Bb+cD<}iS`gRi8BUJk71WM^{#XK|^Q295FR*p%gAAT167~Jp6ONacuA6MY<7X+~SVt~gV2VljTvrxy1;@=ltbxsC(8@j5kc)^dHeE!Y%x9oX2m)EHm`&EALTpkm7OZ%RVnG?7|w%1r80&q^`1e~Fnx%MQw_C&Mn5pJ1YY%Pn-UEFtOLb%rS(oUPJZmccwIa?`^mA1Iy=DDosM+}r9g~v;t$Z5217$;NOj5=6bDcSdXfR;8tPkN19n9C)cP&qy7QEa%KJR(4#s}6+<_NWX?#7LSXfLol9_eZj1CvY#g{((a!IGwq?LX>NS!*u!kO)Oh)1USzzuDIlZNWMX6@{QyS@^cKI#;8d+3{sE60YAlpdFk9k7Y+%g)GPj84)|8b*N5<(4%30W%xGB4Wl^|}HV|;c+U^4#cetHlkuk0w%pxVT0?&mHwfa!0Hqde@BXTo|ALf7P1BE~Na1r>_)b+~lOu>#R_1GWPTqe{AD2%FB^9blH{F%{3?SvArY^3WfEh$dgo?8R1>5EWk{H(XCh3Aq%16QlKy$}Z_Kb2>vILN%RjQ6RTnO8}L$heG&nlnNl4WRUqXyR9KWE7LBAH8|BbV(A3V?ZQ-+_??e+an`?Ju;GXn72<=X;N=CqmIxyGkLd@Gm^~IY#24$LY)o*BRli|c0$2LovvjZq_Bvmii(obJg`b!v|30nw6o|b@G+Af%A&8I!lj40%JeUWOYK+*cU7CqRWz~XjecU|rpvnLPb6XM1I0~|gsl%6H-R8)Nzd-b4we2JZ;zX<EimY|CWd1kt+8^52I=edi*=>zA+BQeBJs3>C^?`J!J*A)M6#$7lgLZxsJs=WV8>_P5rLt)B;MN0I1!B#vZS$nUyN&oQ37qC`{2daYV24ET6EH_uRV(tu9YD?5Y!+yvt`Xf5+T8=<>|puF(EuYEBlR{Cx;`Xc#Oie!XrJcu28tt`?^2+0h^y3xo$ga^>)_e!Dw4yN!wCm8<jShy3>tjK5OIh)wO|#dF$f$erjD;8v9Z0`b01y3VR%XM`CH7*_LZJwBm1}+}K$|V*KQd+Anth+*hRU_UyZH)|UCK<FYNAWn0EsTc(S)JdSNim^+%YxBTV2Est+$OO|CloqabG9S*b2Djb6Ax@C+0qhEB3vN<2MOqK7MwPKFVao!il#sjo_CGsGV+pBFLz#X$bGQtzWA@&<04T%Pw4c<CzpJwgxP&?LfY=$yC!+~82WWX+Vzx-kEUev}}H!3eK+h9H(*$iDBiB!b1#+ZiTS$p8)XcD3qN^r1j6(pdQXl}SPqGaQsl?I6~watOlMDAVHJZsh;t%X`j>iqLx(xAIFZ_OB|)>KU$YrBbYdOl<2^YuXC=f!m8yZK6hk`>mH$GQy2lM%fNAZ{CI(ZYk-N`QtmGVc=`@+1uD#WG+Dc;9gU_dCFlTkwu^7vYYZAdl3=(#_I-jZFQZXhT1#=iE^hm$%6HIVqNA@tJo)n62?G+T?3Fm>FVu11GarEaz*a!yQeLI8+*hn5d`mTNn?S1W>RVfB|NiyDd{{%k34)eWg#vnFf=SxH6o*ZR3|rP^t6Nmre)s+dboj9JMRKb;6#4Q2bQS>3!WXAs|cw`8Gc8xy2nNg^7vw(S9*(b&QsCX(G2&X?7)PxiP8tLXm3Q@g-?Q>vd9nY`+<&FV(v!@inu9r_FEOGY0)$KN70$@$zDrk*ATTj4YykBw7X{l%-|7Y!;M+diHBGf(SE>Xd)59eDlR!w-Y3RZPoEhMSKvL+|!_xUI=EQ{_nhs<8VNwQ&By}#1RyR($nz@>y6C;n<lU*It1h_vqFgnw5b%D%mo7iEM=(pp?6L4)amhMT7WZYAT(4!x_}v$OmY~&m#_>hcN9f@o6Wqp58PtZlMMO@X4vwL<)<GSo^3^xMmY})WGy6ac{b+mI`F?Sb(Bx>cn=ZQ>{rlO=Ib71xUB00T~3#TgFDnV{kp@Bpa&hpZ+NHW$g;cP-60t5bpA5q^}fYs4fk7Krv?@>io9hLJ*O@T5?1(`!Mte_?cZ_zn7(?}q;Z@7?u#6;+Z4dLmJ{<w#!lN4g>os0%k`l=;k79-Q~)oT4tb_I06ko?w?+vkp?!h`1X?NElAaJu4F=_Su+K{1!P2bh;nv6tMP=k@#)NCormP?3F8w(EQ!OMzQM~6Okj-77x6}+SN!b>T0@igyO~J_SL{o`&nInCmXC9W7#Yb<Ls1hlmn7idHmfU)<bgwG9x;vDv9wO)266s7EN^@6fjQDaafBt88<Jm9Ec=q0^cPGhv3*Y~|x9~^#^WGF6%yPD-w(qX9A0&9VchoPjZSUT*ckkJ|_w3z!_JjVsVL3Z`%)ZWY)=`6`y3RrYWje!c<5|OVR1?~*PG3<R%!uWR;sAC$Fo#UX3?#=T@GT_+NchAtt1<eHRv%g?jilhmJO@$~apBSWDmPbu#b=c&raWvA7=Gp!o86hm?8|?;;9l~i-B!~}?}I;cwPlYwzY)i*{`GqqKQ-FSMqf<;TVj^Vp9dj@Ap4PMC7W&-y;4bJ@~55q=#ICk*Tc+Kce1DrH!Nx!cXoF%EG{^DZ?RCh$dfoyF3D~oj;^rvBBwv?Mk+@8`cFIT;?el($2dM~7woyrd&t~0c=lNBoU^W2zs1`b>UH8q%+FT7puAbk74&Qn5y$a$Le(ZqTembF9c@1+OV3M7+psicU7EOtGlSOnlDX@dmFuOG?JZl^7k*j%jP-V|S(t_!X14R2y?Ph*G2Ohc@!hM3Ek2%Je0OOVeBOHg#p}O(lz!H*es-y|cdvTb>LS&Q_HJ}nt!^*>U9oAcpK{kcY~70<wr7U4s{UNq+lJS)%$1+rdwt4JJx$GG7gHmjxpl3J?w#CgHQikr*oL?KoE^4+O#QXD7eZ9~j%ny8+b~G{!G1iVym2OzcL2O)U@fE^)1mf_V%DmWTbR`TXVTWaLHJg+;IZ10NIvrhOEbV;Fw!zDl2|>eSPCGb1`)VWDlpiIKE9&>kFRJ_iASU!2o^ZRRZPLNmq}pkc08<gd!bWx3?-N!eQfuUG)U<#%6b4R_K1{=GebX>Lrp5A8+|9PA>~wd|8gk7zxvMFY){;!P%Q1C^a9%SZ68pC>RsGFR!KH~#LPE?N<xHa6QLW2um=Vqo(^G~j5{a^Ydo|=cy4i$^6oy3{+sj>+5mN?A}+l6$|`qq(u9i;3#U;r9SV&3UapPKp-DwF;ZJ3q_ZYqraXqI;&;=CMbOCOJg5f>KSOTU@s0!sORVFhwQ#tuF!5xr*BrY}77;(|YfBinR-e+h%DU2r$H9__;Y;N;+#?fV<RXoYhD|zE%j;?R}-=@$DM@xh-Iqq_3xOu|U0IYXSNXS6W`6;Ad>VQD$30)XkJg7Bc73<*FEz~r+20NP#Xx`=dq=6$$y{UAopBcLqBOg_-8_Z7B$M?QlOXMvPehlsPfiiZbwcraVN(2MRNOP>uTksAe0q>Erw}7VQFkq+25f#Gc*cwY;6H~+I;6TuwnH>1?QlmbuEdrkmD$6)qv=e$(m)kH<q!xmm1U8F)k4kjsR{?|LbE(C!4{9M@QH3y-8)<<r3ySEWLq?QJ;5Y!)5o2NtH4<cDxvHZ>;X1s?uE1rLcKJ>+RrwACJc0cI?Iw*0X6a4BFQ0Md%7!xnsQYt5dOoLi24<@ShqaCyg`f8H7$u^FsPghaQ-=b!Z$tWg6?V{jrKCmV48_fGnOuI6+sx#uu%UN9E8YO@Gcolv5VJ4s|255h90*NC21$axd|A1L?*+F34-*4O4??rdgExQGau;Pdp0r6pQi7>s*d#a-II&gzT*L)p$#O)mmr2Zq;<K4rI-i?Mv0Ps@Ecm@2Vx0ZS*V3|vSh|NeS;r%>2htY6FW_ViJ9MJ5DJnB8#BcW|Qy`fUboxhQW0fiLDQaiM$rs`&IMFBeB6&N6dOpi)N0<qcvpNE~y2?i{)94RDu)?DNS3bc02nK;<!ey;HUHAqjP$IxWcs`&X=!<f)xj2y4mPx!y=HMsXh;Qic*}(eC-tA19RLcN=KiMuc|Btp{l~3<pBZ0Fde(YUV_ni?x@)_}i5;(U7?_xtt`nH)NWx`U1>D*Cv22-xpjWeCQc$4e_p~~En#~A8LN5Pvk!_mA&dZ~kkD*-heMai9uE}m06a9BTiOizMj>jV^QL$KFO<i-e1J+HPM*&R}~N!NsJq=m!A$(gdf$%O6t(Tk@GYxFLYv`H_x@H9kJV^#HH{!Oc@2b}cFCwR19|LUx*rTe7)Vqr~MSQ}ea6ValVOKQ5hq()m$`wzFC5>)y=OKS3`_@P$SaBWrfbydw;RhcE7FRVYjwy@?G7FM*(E7n#ntiM=Ja&=+#5XO7e+8SQ9u(nuOZ!D?t%Uw_Z%$KucX}Du4Q<dCH(~LY&b}XUpSjY`9Z_CO-@xIRHqcvWt+m$feu5hJW>{aAmJnmJ{fwFB>(#1x_wDGu6Df6XvKI29uPa733preONoOUM2((VY#tl9iSiI0XT1!ZFkd$%ip{a5erNO5T`I$vR1?uq7z)acjRDpKw+UVu`u$YyYmZILZs3T`a~0kf&ipSg>IP#&pBH$$hAA(^;s=uP9T1R(2b&kiy}16hW)F06^h?31-9MdP65)6A?3IlFbH;#n3-Z~kNni)kYS`sgm|w1$!%87f%Sn?bI)!%+*XWJ{{0cPmF^bf3slSM)2;IOAL>1)d2mZcNww+{3O`wnmT9_M;n&e*LSp8{NNUE85=Pisl<z(af!AbGa1_WX3{Naaui7T|Lu#?MCIK^2P2(y)4hdV#Vy<x({t$y9xazu9d^tCNy$E^e?WMaau0B%jGf!?Irx%7R|$J7tOb?nB7-r#r$jTw`LrtH;ztp+*o}&BRDapXqwo5f;2wkIJ`1!z(ezEw12~1%Y`BNp8V`Y{go~Cy2v8;dzucQElKhjxjkrAI0?2?_KW1PlrJrBJtaP(6(4~&G7OdcWiEvFO{5((w8ik?w}ekro-D`g%uS%1L@4AKPq8d%Nn&${Z~vysnNq1ZAW<L}_gZCiEI_h)6iC1uuwlaXB+1BuyO$(JR<IJLR-K5wV&A$^HLHxFv>#O-qKICR&KNXW3i7nZJQbn8ippn_>maQtDg?niR8~}}36yNGxk0W?5c0!7ljP$bjH%M6j-{jh)q8gLeY3lhG}9{DEPOS!Ys+YFVbtf|vbY~JulwU$FSDg;7`ewZE&2#go}8a8TtsKl6OkR~Pu^45^es<b0+k>B$^Qp8r}|4eYgsg#2xl|8s+Rbu(bOJMW-0+C#n~k@h|Nj}p-z$z0&Eb{ES7+7Tmn4oppcPVgBwM*Bqt}nC9uWdDT5hJ(TV{%$*^3mp9WC;!U)bPYe73|CklUt`Lc<&A|!hMeo|JIhw8}FsOSRDAmS-EN&@3xEd*GF-h_6*jUh1{n32XF04ZnOOxX&xP@3)N^qOGHiriLTMo5oHEhm}tRJIzt_0Wv5O_JlSWjou%n*l6M9}Ezng`g}|%*nOAuF#?Hmz!!i2bEwmaMiF99<si$5BuNWUkkiJx#eXoaD3P9Tn;?U<-j{>c)VT?e3lg5dNZRzZu%{X;2jF5NH7tUU<uMx6~V)8MR418dsr)6O^_bAl}l9L;R-B9`dkql+dTzpD@ohj&;sv9EpT7@FSKvYRKVM+0-mG-9+V?}i}?4Y0?tkfSASsf@6tWj*Tlcm$I`_4Z@$PJL*=_pIfgLyT)!1?(UY6%7K!{O-bgT%(?YkG@B(@hnPgL%atu_!q0vKHWEyB>$v|+-G{BG>8^<kI*skUq(wJ{JS3Z-N9j9_XPdT`G%AsM(p;O9%)=bhct7QI2Dz6CzTh^gvTu<-IG4VhjF_=duD(0H-Oi)pRU2^5|)h*WFFiSZk-RYVtHOwgO&N}1R6E`Es<SU@a^q;>^*E=G!ex>Vey&~|r%-_Ve<}|QPRJG)wg&uozW0pK{TGZTHIoGMmTc(xGhIHQajdUL{S%`%nlwj<bv}`jy%+<L{kAtnFbOUSu+SEQ3ZSIpxde_z|kC~5+ycmKu<h<tna;6K0ZKa#r?b(forM}K<J^sdJY?-KZ;pi=O70-H*$miuU)(RM`>eGDO9`tXxe->&wsl?RZ#Gr!w<k#@0<yPNJZj0etwNI5UR(i@4MnXs6QfGqtF+C&XHG#xOs~(mZE}t~@aFCmtA9U-9zr`<^x}FJV17LWCkE7QNP8jC$*kd}_Jg+&WQ!H+F?~r`YPk82^ibO!of_(B_U7e3$7EsCL5hD75eUmMXUm(1)DHDV_si1Fior0e!u1)QrdojV$?4|2jo-JaW^a*CD6VKT_N+XXQO&jY66{yY3?zyVKz&+p%T4PW9Bl%_s2o`?9zo_yu)UY@c!b<gyGFqu>xvj2~uqrJvU?PM7dn1Ub_CD0l23{2tv{8<OR15SJ!y%0W+7>cJmXS&2BH+;~Cq82QO{_6V<l9S$eA23fm_qh;43$Y>G!`damXM5pK*vf<3wy>#a7m$pLI>%`ip^wPu4*vH3EY;fUhG*xb@5rJ!?jm~Ui!Z_6y@+%(RU_WStS@?vRl7pyf&Sa7a%>^5Jw-h@t8DGD8@0&&)OM=Q1xUQlebxDkvnD2!zABgAk&5Pi}zJbRQZ}#lAyE}_VJnNAghJwb<f+$)qyfDbkeIPtL!cPD4aQJh0;QKlz!n`aWpd?j~t)i_$SdUb_Nkdh_0Yos-fCLtm5e*jQyl45-l`)76PdHJw8XfJD6`IH)+1si#tv?Qr$guX7k8&laT7fgR$e~*3{Ly2X7?q{~ud$du|uLBA%Kr;5qzz*lJyo@C<Va&-}8d=Bp(<$yn0X#ppoqF5%f#3D2V>^joQTLfhuT!w~)Pom4!V8rw9G=%r97wR-*J!O5k6>_-(g9{OoxGv;9YSu7b0mmAaK<HkTU;m@yt<mcbKE5LkN3NZIJxyxwWTloIxy@l^mFn1}KyA;e_3g#{abC-g-OTm0$o%XH<^JS~SP#xm(#Z-T3zI<7jxh72g{be<n#!qR-tAa3uSO7%Gyki`C#|j;oPccai1~@Mt#&qYo8cZ<d5ZOqMIw}S|8>LaMNWqv)$5KIMq0=%+!E8+mW|I3z7t${NoyB3Mw^n|x1GChnsd6HJKoOX35`l@#uCdJaULr87nFvfXHTxuiGU~wi_tt^Ia8{K!?3qFxR5_?-VdFje3t5<ID0W*1M!+4nyf0ILnM7c&YQM~$@?84n`cH2+IMbi03NXPGU`$>^of}-5D}LT4<x$mOq*!wP)4MCu95Y#%QTydmy2RH%=ZC%i=eelMOcUnpi_ZRZ;UzT~ztm0{B}5FIoz4$%XM!ZJyxRHY#dATJ%L@)KNac*OCrinl@s-Qt7eY7wr9Z1+$U+$BmP*X{%XOic?p!ElE*CTZ=a;%ep|<nl#aSnO>2X}>!_38DFh`C0Fv;{`oT}W*MtH59&UoZ2<YK0=Gd7@i^RW|_GB0=~>8|;aG#xV?e9@j~ugss?Oc+NJYSn7k7P7g&F)Ln+bo+0-RWziRXh<?obtn(4=&bH5eM2siTeow*%VZ{dm{6qzFwu}e2$n89;p4=1d$&pQQ6$-j0Yl{DGt{_HH-L*$89$jJeTq6DNJn1$u}qgr6NKZ(d(gx2S=L<$vX6iXmdo2_x8_hgf}u;mWsfQgj)!f5>vepB&EO`({SQ@{^5+J3SMHaFEGoY9uol3;&V^^WY_8$Q`X*ad8A#4eX&KnI4-LFCyOX2;G_UQSdI$7zj9s1qkb9tyAA(#nsmB6nP27`%4bX9ntJdXAWWWq=d^{S~xFsErB}xMtH(WK3FLUv-@u;6CA|C2x$Bm(hBhkd$8Jf6tasP(s8Xuo3g81ZP{~V78w<hQzRnw;}ng>v+(tY}MY(n*Y`sEMORBLOebi18$ZKt%fA$$6w+bOf1$RLU(&}!IJ-K?or!R*E&z3n@8;?hprjeL4y_fP-i^rwVl=6ufW0-#>I)U2s$ufl*m!l_ps3m3URx{f|bxy(*LTGw9nCq80>^=z;>Yp`4!>?L+bc6r%g4Yy>s`<5SwE*#*r8-~F^{mTAeNIn3<i$UtciS|(Rb0t<BCOm3IV3)%_90~tku@w!U)LQAk`#EROKmdodIs1fBC_twv=d}0u_Z-r?{EG=%OgJ-5kc3Tz0gcC_<eh{brE%`%iC2IrPJqb@aUQK;1i*Zw0DpoGBGCX~hw?3=Sj*(xtnGSMgl=IWT7xD98@2%3JJI)gVrlTW2ooOAh?MQ*M!vk5nsD@XayhJY4ZgR$vi2~@$pcWs`WB>PTPJ7-z7$kS2A-uK>P1R~02xo{Az`qfmcoaK5R}}SB_soQywb=-n+tj)(<j6a+yFZw>|-#g(O4lU3<OFqY|0AQkX*~}!Wx=r`qXk|<YuAaPogJ9{D=1+=sGgj63D}gw1^{H?gdHVg!d4);@FQ+>{Eb7a<r<aljod}XnIArx6tWo171gz^2bU%QqBY{*w2D1lfQ=h&1;`PV@+`6d3O0TKb#nP?1Y8l^+fkg7q&^AA`#Of@<3<?_Y4&mJZImAuM>CiROb9G;-`Ulpn<wEI};oMo*r)jqE4kMTx$4)3pytSP{vmK@J;rYo&b7fh}v~vZ#BC%0YUAV&}i|Aw&$hez3K3ES*j1au&F~b2rK`{4)}~?22etHU;9KdNcr|8#5A3f({La-U8Cf`ejj}9=rn(Z&xNNPpDxj|VGhxS=MUx&+*Yg_FTwR@>sv8FLg@m1OLX{7{k3jmjlU4n$UyH5G1dtePHYhv=pAM|4r2p_LpcOdKKgxYUTo<1l!ybhPoa6w4K;APn;GiI!K#Q3W<=b8q%%QxBfviVos{5A8}O!Lc>NX_-aKJ=3Aq|=vQ1L2N>M~h|CZUR<F*q`E~B{C%h)*5C#*~^kH}p4mQ1=fR*|%cq#)NR-%q%3lO2@m-pES$IIx}HEkk$s0VY6GZh8a~EgP8z`c1>Qto8|G`++b~KKat`;v4H(U>{(3!~9FKDnM_yf~=vpfkrcM9&6+<i6^isyMrT^)yN6Ck;Y#+!-}(UkEt8nx;0MaK}NtloWKGA(I=6`1YdfO!4|+}fqZqj48VG`5l3~B%=x-&b$R8*xbFbwkDMSn&WC)Rl%Ql=)UpmI5G-P2sKL-S^tc1(A{y&~j9jxqv`K^{8#4Yf@y?AHy8M<POF(_32}VOxq7(^jK*xHX#Ba-<43|OZ7@(k@`>7Q#SRRxx=lpf|Yq5J1(<j6kmr;b^GKNoG)}K$r6ANKYm)U1S^_I8FAJHJ!Z_sN8IqE%_uA@E__E9m6l7K@6@0D9RJ(*IotS|TMzS~Fg^=S}!G7K~y_#1?K`v=5Mds^3ntp>SB%#GjY()i5tV|Vz7S!rb-FO$Dvsgu2h8E4CxqRd=dty(8+>BbCcIV_=P@g&SBZHfF2_0P>CnviI3hgj>07;$;Omp`BJUHc<#R>{Ikzy4am&PT*t@r|Y<##{%Q4hQVLMb{~@BrFLt2?wQZ4j6}n7ll5q9;u*6GMrR7H_!#JFlEHX*I!}=iXPn>&b0@lGD!ZjsmV-i(GKCcvF=a~E5XDz*eKOA?75nC{KoG$QV)xXE8ErtI9WYsK%XB=&%mW_pw8fUF|jSNaSs)Pj-2@JU|J%bgxolnmVtwr<S^xC%i~zgPXE}eTDpXwKLE0``vh~*j)Z{Wh;Lx`wO|Y@-W%LO*<qBGQ|aEFvrIEgf_p@O&r&IU12|@B_{`TInI*t8<Qcv%tmh-zwZs#jm9}}%GYLnsP0+NDRP$hdH$Q2>z%@74*Go@op7eO}a|OW#EP9bkap1!o{=z%kBVGmsqdnpZlbG2fPDHWE8*v+E<VHph=iZ1%h0iALhG=`{jc5SiAapkMUnD)#26^pPV?>~2Ge|v%gn;!8m7deN5-T)ByQT<p?8y=_mt$~oOq<aO5hrr}V9PmsIqOHsl&5>ey0tXbs(Qnj0S1Vj(qN!6Wqx(JpLMHv*+LC0*!xJPB|}8fCI%9emez;q@7aS|b3QK5>T4YGS3|gf0d9QN*~YYb7+>lLk%H_eqE&7pcbQO%;gOY{K7zaHNNG`A2U}3%_>s1pn@Up$*5BBDo<8E_gxd}T?=nWGQXi?nEI=~U6$_PlTSBTep{A-VBpP0ztW?Y08Dl(Gp6woF3}>MoA63%6q(p#?=maEWH{5iw`m^E#*8o!;$d=g3QDn$hsUX}AwKLYLJbqWSeC}0J1g}rq5AOF&k_drICoL%xw<xh66Zbq4fgctDD)vKBj8&D44)q{#_lgl<W6Z$DEhLE&(cGp$y~h8E9N0|cz>lO#^yf^za|{Bh`;&GT@|`<$`oNvkaqkobCoeW7g}S&ID>J&{qAX<)GNh5iIcgn4&k9_Z(h2e<e1&ztGWG4t6dIGQS`4%)>)C>b;vphLCP?Y3WzPFf`FR3Uy_41ucYuR8P0t^6Wj-f0DTH-`re|nPFjNNLKS!DAl}g`1%vMgkQsKczj02Jw&i5zA`{mg`MBxt5FA~TJxKl1}B`DQ)0fMGT1{ui#9vYFE7x6}0CsU5}hs(q<l#TQExIs>2;O|SDk0J*Ar8NI@dVYgQbofK=`=400aetC&G*+P>K4Wdptg<}3ab^Gg?KkN3C-2rzXyETEw?WdK)Z3oRe8j}%_sSh(EyA!VE$~CuU``1<G=)-S-78Dw+Q;J?^z0I(wG0#=pEx%K2aencal;skw7>G&#rv7N2*pUA+X?ROnt|MK?qM5>s&e0Ij=NU6-J>b7rw7lutRvt`Jsau+tj(N}u-MV>8;|x)S*;l<AyD8}xE#L=zn~W*r|1)w>L=|Y7>`AZa~XPZ*Y+9Ohe4XhsRqIZaO4Tu$(%UNDf1$-;R7>b!P*9yHP#YJ_!s`|FTes>YXxFklbxF^kSA5wve&=1R$N*jZ<xC=Y1*nbmntJyE4?yEb4G3l+h_^6Vx!-P^j#PGjFrCO?#UMW%m<!F7i3K16MKjAw{Jb;iORxF7$M?3u9)jdLLYEprnCd|K1no0E9A5(mg&}#2Sa$I0=|e{<>Do39%f6v=aO%fZRp)IgHjj!fx)Vt7@4MMoOfOCGb8@?V#%L7S?{hb{4K`-aTB)oQyF&gJm(o4AuQTi9)}S?*UW@!xSKS7zrYk?Tq2cILjk7Rx|-8L&mKY-ZIMg03Z9Z!^6E0=Fghch34T<*4@+!N2GN4HJr$l+2UScErH)0?CLgH@-$VksvUYh<jzO$9@~1bf2Pytc15x(iN_@~?#0TZilgfh$xnYYE$ZfUoQF2tl6fPunqaC^E<QQ1Nk8wkuA_ks0nYut|7&l}sK~;c>Q(BIbqQJS7p@S^rnWzBchL4#!ioY|T;q$E-{si5fj*X4<@G%Y>WcGELL*w!K4y9-e?;Q#WtqQuR>0<6^B!1%QeGz1W0hVH;KY65hjb$NiNjGenfrJiB`DFv&`pk5VzNP74PLHW7nX7$9PMjht=49_1SRPQTv5cRTGOwguLy3RN0WHJ)jzRJk(ludVjvi-Dab;fw5z7`o%c&4s;=6Fch*5BG87@Ql6Y)8Z=Ve2H1t(myukrXeFj?AlzNfNYx#gB@@D4iF_!d?vaAv&4SgOsqm>yjWTi=%Q8E9KnQxK7q1@8Ip-syUGy561YbpP|-!uJ-w)AjCjy*pj+PS?9r%I;jfJ6G>++y1eLdf`sgb4=I16HCuDgQkD4W$DpnjX2m*&yBU=#5y|APO+^%?aHaar#(*0ys%{EH4`(BNw<nSm~r*=dlYA7MigVZbMot65b3fpx0IZ;7Y}p7R%PjhcjM&wk=m6fuWx_uf6gbqa%Wt<df1Gvr_Ww6_D0=NJ7;p|yuDaCG0f|#1ZS|NM8WQGov|0koUNbQ*}kPmvS)tFA>1VG`Lkysj!rt~JNgUio~4G9uNTi0_DWbhevQdMPggq`mCs&$fxTzPS0>;5Nli??3ww5p)8@~5#t;?oa^zpmelB11=GksnBGQuJfx#vaC51I|BTIz7GWkZ=_mRfum+YVUFE@?B{lf74stLI~P;SxG2=;l&;Qczqt$T?W_ZG)>KW%K!Ic;%bs`<Av#$GggzvSNCy0%*v@BNF8@u5chqc3`z{T^>~DE*R!dFvki!Zm&IQ`YXCo7tz&t<-P3xW_r?%p?;>pK~$Qd^%_Kg;|@QG1&af7T(`*hJX1Uuil^^JM)W;^QzO%d3)gsDfTK+@^ZL^u%H0W8I#tS8ue%GbNL8n4R!U!g$(8^9OEzS;{VF~>4?k5$N#iIsg9^?pI3x(pgik*Rlsj}(FDf&wN!LPU!X}~OFkeL{0w(4&BsuFWu*)?u5t`@OV=zZ2g*2R1~xeu(iTNssy>o!=hkGC5r-sJ1n)jYFmcEhka}cRBvP(oAi793!4P(YmI%fR2-slOGf=A~YC~>gRc;<1qzOET6k_OXDuXZxGnA^9r#Lahg2QS&Md3RzZLkVh+WK)%5zgf0szEV&c5#VyvUCVo63i1rnO9*&W>GxteuhXnen6uLtfe2+-+I+Uw(|1qId`zneT!baO3Kc__SEh6>uiLOD96}KPr8l}fo=vT13-rk7<0Y&xij5}D<l32)PQKtbhyquiN(W9WA04Xp}kX_Inyn~;<?_poLpy0@uiD5RV==%d;#zRdTD}^6cA_rbU+fgZdCP_P%x0$0F4B*sH;c<)WKm#@A+iqVU}BI$A`yma#aCZ-5EUj(w5Hjg-KB?jd^HL&P^Y?oSXjmYXLiN<hkclODx{Ah$ceB0DV3@8N4=DpGdWR1ooH^+|vJ`*lnAFqW~m?&+IA$w>!$F4TZ`sT6Z4!ZbM=oi=N>*hEFYcre^O6xSkTX<Ssl9@^?cII#x^&PPI?jW^$IGo$;{%AUcLEu>u3ZZ1s{-macF4#s|Fnsey^yv3%E2`w=@oV(i~7<F+RZ(SM(ix;J7=R7PD3gcp!qtF#tH`&8+4^0Ikw>A-QKc7^v6mLb%J(ZvIBVm-kXtxG~2gU}5AOivUH(6${>-D}wv86*v+E~sHU!Cyspf<`qD2EVVgLo3h{#%LLwYmWbx`unTaHU%QR#TL(yUVlLvwlw`CLEMKmB!!6qC67GvBb0XLO-W4ONfq0f^$v^QVFYi02EixaU`M-EQ#j!Ava95_f$M@cCY{j-MK19w!-Eh`Rv2*_pfDudix`T5itm|7W};M$+=eOZ|Giho@73{pW%2&!y@l^Bd~e}<Y5ZOqzn8}ErSW@d{9YQrm&X4frSb6NQ5qi$+b|~jiptp5Ykn6c+vMN1M!uIcLlv;~vQig;IE_wLO!7)Mht`L#GD(qEjO}f0+xTTv&_@>AqJqAu?`HQx1^ulxb$6|ZJ{`QKYMwQkJG+;&3i_4Wd0y0^7e#k9+M@i-=PN2?^l}}e>@AJm{JBzYy!dk}rO(7*Wsg2p(DU^Bc_}^H6Y)~P9UCw$Zgv4Os26ZnM_0S0>TY^P2)ByL)>rKA?DZF_=?i_@>rc)1ru17ia$o8me(_>G($_BvRd3eY+59MNdgXfJ_==7006c^tAxwY*BV3=I7uV0Kp;rpYmj(43#cyh|yrU@Y?SeGR4YQ)=dlcinN#KrE&zWwj_sg=nse;_DtiOB<Z@Izu{&<?o=bl`+mm2(*xa(D=+!qc=%PU`&<j;z-^M|;o-7d<&%Ceu=)Ya_Md7`@|pF8$aSADAIrEY&!)%g`=^(B}fy!7;6T~qg$io|cLufOHu6|*(-aT>-L^@^sh>J3X>Vt1{$zQib;*-~D-zAUs~)YpICz38Tzt0U^LPFV_fP{%?AI5*H5ft#w2yFD(R3~Phc2`m*<`5>KKwv~zAlwGQnZG%ox6UK+3wR*;$o|v7^#`vPTUa|s|DiN387?WA4uDCJJl#|jV+GWyTWd$pvPyXz4NRnSb_+wR>K)$X71B0n<ph!=c6z5}BR&*uf&&;2x%KtWXDb^Qd>HV>i#L_+{fB9}}c+F20N7L>4@nm&Tko1E|^+gI8I+ITf(r?0L8|fF0j9w)uX~oIuQ)+hOwI!#xFN)u*Z>QNLW454T?Cc{%LWoq%z>m|y?6P%aG%3XpeLXWLLj|hTL$dJG4oid<;HF5it|#p5EvgMttA9-aEdQ(SFM9}2{=6F!*yvq3=bi-fXAo{9g~PL;1<wF%tads<c?$w7JFZXp1ROxe&PBoK^n9S-C~AV}Sx@D~XIx<UvEDF@>#1VE3H^zRQIv5BLsh3LufKt^71r#559B*i3VDMdc~x<pKf|xfZ=9@}Pc9B8Iz98&%cvW6&;(89xJ;vEb{X`+a>8Bd^%yV-C2JGsIO&`Rh=4|m+o0T7j$b|cu39w<xPX><0-adCpLre2GnM!O{`@ZujIrm=;X31giN_Gve}LTI6)?sQ>)biNzo$%9hG;7^_`GQ|s-kO34WoTJJ4a8hx+Hx(eVL_DOLWW`iQklbP%=%_`Q={EDDn)C@hvSiK>bp*XHx8moU?pRl4Pvf4MEiW5KXHmR5`pVZ@FOMd)W|QsPq6LvJ(HEk2vc)<gd=C&+M+9sP<6oYPI^0`aC=|M6+f^@wW!{QPK|s#KD^gDz{c5b6@8&G^jw`%gY%(NNjt^5}5vz$w3L55k_oAco|<Y6N~yC_g64hhd+#t5Vq_!Ep&f#g52)br+x(nIyTDRE7y|tC$@yPG2Rv<+Y!h<{TNI$HH0)7m3S{@lIpUaH@?y0!o_IMcEW57Q}RH6TnxzeQ0HVvt~qZP?EEp4v@=zZXvzzQ6_S}fg$%q#RDAH-XRo-8Yl6)qcxxlAF>`tkQWR;Z8cj5QIPhCoxyRK~p9k~B#sFa?<=a$M25#G#<_hex*+*79Ra^)APZ8)CZISoyZEpuePbTAD+E=!%G3Oau0nK^lU$?nnch%N;?&(}-fm=GQnBmJzx{z$aEWjOK&ZB0liPKgjmg%(&!7wbqX6>lV#x=Rl0s<9rSIJSqpxbP>OT4gBr`S=)W7Mr|Os5YRER(9nC>=EMa=J_-;;KV1vU9L+7KRXuAzjyHwftDlzs0%?0CF27)3S#E#^_(n2U3pifjL{R$`FKFwLTs>-3Y{zDK)=#{<J4FDj}=@{OkaAk_Rqr;V--2n&P(j#`UqrZJ*A9wlZ4|gf~6_yM^D;f4FsBNe)Ef%!zH4(Ay%!ymtvU17&5{YGdDrU4%eGGQ1pSglwA2a2N0fv5Co?9fDLO8I_=imHYUl3u%quxPktI%&{#}Rc=Af@lXaNT2mGX5n-BZ%4ge1QB+5<Dymk6$;t=%xE$4A>+lgYL>VUyfHo~ZD>dhD;K4>u(MiBzc(#Nj79`pqm|E-1eg$+0q&FUr>wo|&H7g*-5hC%*kus;!%N4RS`n^R(o(M-`9#dzNSSp`<Ao2;|PeH*LO07$4Z=*axaN2)wT7kdu;_}<pQFjXnIg0A7m%=*HubPFVj-N^D#0Qhn!O&X4&j{mfuAxJ{!p{7AC?zAsoF0qnsFkCTNVeiim}Oi#AfXs+>>Wvqt-0G%*=7{Mp#}-VHm4OpOKwv&Ypk5B+#!``)2ad<eO+CpfoFI%6XN#XkcM@QH7%P#tLsV%J5|djRw0`PWB5Uu@|+~raT=~tVh#_JisC`5=!SWMnS`SMLiMk=LL|#J{e}d#q%YeNY@JJBOArY+bf$v6Weh3U?@R@o&hStkwfTz5EL<;wB+R@R7*z|qGc9cNjv#48D#cV;B%H0K7Pizt6?plX5OznfadS-t+br(^4)mHe^zbQ$3$&}*+*{}ym-^R}_;ok;xaYoyrXD_~s;`Z`66G|biC?cJDlg0{m(9`3em#2Gn}m@`V1LeQ`-ret|DV2g$>?gbL951&S>ME&T>m(TAoHB2m7>#1(O{)$)?(>!nee6!k8@zZz#T02{0Wl<LZxFFIP=wkn=DKsWsx?8Efz9lC@`)LpyxSal>q|9($G?)3sZr*&t&u#?4hT?e(^PJN;~9Rf!{{}!_9Dj4AW<_5MT#Ubpv~Wa@j4HjHqY^-8fO)Qu*Gdoz@OtGX?miwXzE$-6$n3?Qa=umCn{E_QSP_ok&cm)8Y~(JQu1CqZ3)d_T<tjO_JPW6Zu9HsH6j#9SdQcK-n^Ok;s1F29#B1E}Pr5^6PfbGX{iC=})`A>W6PS2;a5bazDG_8GeRwM>%5dv=Pegw4lI2;~22betx3*zd~P*gl8O#K_YLId~`$LV|C%{<xhzNdx`CGPJya)IMvnUq0D1z?s7X!*Cj}9O5^RE1YComow4!GE!$vQXG1pLUh;ig^K{VmK0lRHjYw%;)xamyTmCZFJpBX3in9dHnAQbexi<}0cA3iD>|l7ph0mT_Y1-yAfo^jZ#Sj0M`#s-$A5rlzP?QviYlMPik)*N*LV&%c?-R7_VDy5GKv^S>+^I;vkp3TK=tAzx_$C;8s#0XG_P&eSeBdKNu=F6p9O8n*)JS+mIW(mAEYvHX+Hz(42812y?_f0~y=&s<L*f>B!w5MbZMI?K?NtMQRF()W^$jz^ba9W}%u%l#3F=ncBzq>%(v3W4P!0^Mu{Ky(0FSs$PdVDH-HsC;+qYWykpi&F%>k?7m@wtYaeiGwOcjCj#K3e6C%!xD7vX<>MQ-G_8e#`I+;>nvuCZE^eE(Jj#QEyY2Fw@Qhr6@5?M&~mXM7tM0UX5+sdPAx;exb|8Oh;MOwxvV8PDZw@f??73+b9Mi*gatDT^ZY<FSj)MGfOTo${K1&vO9OfUn%<z)4k?=R4^wUxa<hh{Ps+JdgbRg7b2*@*|znO`^viZ{`0J3+>&mM3Wc7y9aPH-aM73m4+uwr)B!^PwxAV9BYhSPG~^(krn#IuytQc;oBkDMh6PRanB&xRwqo1imR;<`m-mB<okGNj6sEe2Ll3>&GyfDO0##IIk`1_<aj!!cvSv*s|KT-axGzft33Y`a%Mf})qQf04^*CigO2}vKst5Jk=#qDU4p1S9Jip2Czb%9G7QK@z!trHcZq0L?lUF~<w*o~Mj4#HVpG7umj&xpo3mSq(T##w1`rsge0POtnThilz*6BjM<5>K)@-?A6B{ZP;Liqrh9%sUNFuc$@xfgEeUfx)V??rr=}Tof8fZ8(qUtaX2Qq6g?CD^3Vp_W_?`7kStXmVrqiNSjbTq9?2UumaUb~-IK2o+jW%Vh0+)T5#?vK55JKa+Iz1mJSdt^-&H9d;^Hsz4#&DOKoa<wuemncSVVs15FJ8wLKuGDz#wZ=<ljkhUF`l9i=(s-(n9kJN1!)*6R-xy2_D>PxJCj28mu}z2?6<uRGEU~X_zg*fcyM~R|29@4Iq|Erd+466Ekt3Al+-rl>!wo}&bX<=w$7zBFavYaoT7T35%cb{Pn>9#6Vf)M?WLc2PgIx?>$S}~`2d#+299q%rIFj){%ayN@5s`@y{VRK{*<Dmnh()i#t(4swd#A&^o>((VC$Zbm4*0GIW>AxV;-;cuK-N0jEtHLSw=ttV6jXlg!%mQ8otXF9Ojhh$r%8D|va^QUofS&CW2-j|q8R~}Rc%`uhV>xJKs4B>4s<?Ls=evR)n4Q0Q~B~u87*k(hSvxw>uCLWh^CjUskA>Zu8`4a@_QCm%XOSEp<ZcYBtrg)pM*tddp3iz>$jQ#urXMz%LW}rlVuT#JGRzyEMb@}IVEs7*7fF>zp(azr5u}NU0Wjh?Pkso_uYde<e?m20?%DvM|Ww4{cK!s%d@;_gJHP}2P8zXK^&Kp^OnG(JZz{C-g8epuEiX!k0)+zgh!*rC`*Zml@3R2>5(MafWaKT>wZ&w-CX@Ir0s5G-Nwke#{e%3xuNBj8=5jtJlLGld2>TU8foAyb;t~)J(Ct|co`<A!X_+H67`!`IqW=~EE=RkK;@-Tk>{PTgOyv|lz@@rk8E2+hKx4p7#g-J3HBlBq9ctC8sz0ViXU`Lesl&ll??*L`J>f=qV)Hbd7@EF8id2a7AFaZK=(4QtTmq-O9Z$_&y528ovD^B!E{;i(9(>vCz74XRNYx9WB{D`Xqmc!H6uRu`-{rj7iFS@o#e$f66|8C9yFtgPA#`{<FrscNHOI}^&s`k0M56O0fjIMB8)yd@)D_=NqRqcC4$|!rIdKSl`BUdor8cjGSLar!^hsTIV;K28po>gwX~j-s%%qjUQV78%vTAtR_NvY`I1!rg_VxX7g^Wa`8FuGE;l<%>UyT-Rsb@%m3F_G7BS_sgX;ECPNokm5lJ)wW&5^TCu;X-cR|sFaRb>zs&*i696t6262-?q_gXW!gM{m2`%pqRbb@tR3UfrEa71VyW429W93EXQjiVs+aI#VcvilW#TopX%ZFGdNMfrUXY>TCQR+07cN9Ee0Y#C_rgm)hfO4!lFGa}`;Dtp2N>5*8m%{cSHY@Txc#uSLGp@AjB;}Vn}jLqL8;F5U{tmR;e!y8oEgfNLR1N**(FE$Fie0qs;K<k~k!oh`;-#Bo4IXn=8L~!-u3H$~3yT1APvTuN=a5-}ONH-z~-6tFW5$Pho^G(abBNB+n6_!B>mHiE~*8%nSEL7|Pjj>YeqV-q}ViH{D;g~fx9J&#fuCVN*tr?TlQJ%7ljj;chb79f}N-`pAN<Zs8BGNL~JWo)19DkzZzdy=TDbeFBC1_Ci9kXv-#egmB%W1ckhD)@T3!0|`eIM5}P&IQ4Uc(k6Mp%wdg`HwWCz~athGgs#SB{RsblLc0X=9aR8&#N+p9jLW72=|1g2S_{4UnR7Pl%4;Ao-8~K(l(gv`R6j7j;CIZT7Yq=`_8sSy|h#t~XhDBTL~qJ(j5{%Mp!^B4~bCqEw%FASKaG@MSMgm|!V`PcgHC43Lmg=7GY<gn)-6{|+S0@YSm@I-b;oAon1hrzcQp%L5W&^eBcqU-xKkQICNE1?SkV@uEOH1x*S#e$5+H0_N1nOho=oXnw{2k~SGLadK%{3p&qK&Mq?ESw&SiKC%sM`O?4hK^FgnXnwKytIJ}$<hN#i7%#DQSM`p%!OVfIvqW3=wW#K<uKd<td=emDU1PXh^KHT3T7KO+PS#+~vOSY?$0ZWa%3dNnl}1s*mI^TxL!!u1G({5yfFZuP+WYxxk1pxGRZ*~alUZWdm<kIG=Mf;nCJ?oJuJ*0BC;-zHD?_1n%uKT-_M`TS#ZB#)?3HD5DqAV#idE?NJba{H`7ZzpPEE`FLweLaad5)bhjFWwh(~||ibnk=4J&%#mHyId^}`~v;^XZ;Wj7=uHgcgJ%8U!+HzrgM*xW%HDu!=+9Fq@bE}l{?O_%%LVD|ZDIa>*>_uj0@5^|A-@fO~j=Q+u&8{dNP-s<;!{^*#8vW@j6h&h_yEi*EuGj`bdlr~<U;L`KR`7}u^X-^Agdh9Tuz~-gdU_R}5%?(pIiKy&{>KO}Rqq-=p{;v-*+Iy%!-3s+>wCCASSBO52_SRMbjP}Uwu!gz;e>mDR;d64Fijusuk{`xANoM8jxeco7H2yr!Uk>{k=X<2HT6&RLkk45_asFCkUJ|^DxARy)67)7wdC!co1jFb=Z-`@%&-vvQBj1o&)ira)WitDbw-{)V$l|HgCBqz*TOqkEX9PO)iS%WKU)GR(u41$;0d2zOwq=e(J?uds|6uc1tUH2+@y^3IQy>_^EECw~BC0LL)Xo9BU*5#=e|(q@9;ppXZN0IBGvV~wy)0ti+Q-Xd>*`*XsQ@i%fEqN05+xu^h0AeAOC)&{kl<j&m{wU@xhm^p*3E@fL9kX0VZ*qQWvr||z8}{$BWDnsL@`}k+StuI3GBwHB)VALO1JaZ`?vwld6DPcJj{xuq-V(UR+LHL)ic|{U+d=GxXld`j7+|E^PacQK~P%ufd+*wL%vlj*zvU4ZNK`P-9L46DeTdahp|V4AyxKmWd$TwPfmV&>ghQ%1>Bb-KO=f$j}>s=xr{6!I(})f6_cNYHHA+S#s@;xy}V+}#0gMs7ZgB6Jzj)4kvWBvA!ii3cLXS5i&Umjfkl$cMXO?EByfF${!&_T=WSUmqvZ6AU-nv^2ROEAy)GR#(tCCAqSllXBJI6TTnbwx<1@8ZwPnXOKMCSey18q2K`5*Q6bM(2-+S9+al5Dm6ZM+rDtEs}!O=wa#xS?+7jm5x;)HUHN1tuXv){uAoymeYO$2Ek-7-N>^J%A%llhE@Zynb-8}@M-)CPgc5z&rmD+^&eLeoXxp90xddfOpNEp#@>J?ao4^;Bo|mX9*1rvz6!?D*wm-%9bdOm90gU}dV*Q9`opYoQ#A)r0t-J}_j{YF-hn*u<|Cl2W);L=;zR4|8kK^5P#iH{~BvWcQiRuH4r4!cF;r+<yy*XL>$TBY=SIL=)v<4=2Iy8L>=v3b0U2e!UlQjvm8ZIF`xoIXpzfi!9iaM-h;j*b#sHpg=7#av_>rpsR9Yc>rACYryX@-yxtF9E;KLWu@3Am?%H7%x@^Jy*Vf&wfBTs6uDqr9vXg4NJ)8k<<G!u1-e*3(M(D&0~3V+=QPG48ocO*VJR};g(?WYV+gPf_W$d0{Ih45#Z&-L*BeemER+IkDLGZPUmhY-KtVZ~sA4K5IQdL~WFw5PN!s?&s2RB(R-+h>MF|a?(Q-K_V3qsGjJjRpNhe=J%W~k3dLW5zXy8jc$^(=(`c(R&glb`}HhXJBP;L3{09lA~v;0yMv=5&N9EPkx^bbK6#Czp)JV(Ceb4pkMZBvG#Q1I19M1eGQ)1<OBlPR5PoHp!o<qCv~YDFf}ksE0=OP|0pk$Bt<Zn?4SzO!W?!=0%IFOnf{uKiEmCjk1o?|#UBGv#)e*m>lP9zZ8aTxCzu$VN;D5eQxWe`3c0m8bOHS$b!SsSBO>GQHD@@#9gE8&mX3?`$|faZ-;fUi6sK84Tyntj<P-E$+%2x8~VaT0VCKX%V%SndHez@(kE(AUiBq0nb#A5=z{wl^J3nb7w78<?;-=1sLlzn#u0nP?JAlnfxJ|4*<#eHoKd)*&jQ$_$~Jr=|I1CeampSOkCeg`GEqijc-1QB$#0GJfb~l_l~?R)u#i~j)^<J@}LL7+@fk)iK*3&V*|*|pnW@s6W`jC!W_1UQ~F>WrvU)`GLebs8wJnyj5+q=%k0r3R(cE34>}iuI4X~L;Pn|a263>A$+}V!xeTB!zk-8DtIr6|_DM0bNdq++^ILD!p}>80^!9c8G@5B}C`NxQBNVCI<ZY!w5sn`$Gu?(h+(`|!LdR(mTb8kL<T;VW8calj?%E~7M=!v<aKtpx^D@Q9OTW4Z3rUvm9thZ7afFK<-<8!b4sX(PQ_bF6Oj{jV&SJu@1cZk&jd4m;u4Aoge~_~Vym{9_nOQ!N@U8N7AV0b%rXyIgBtK2VfNJuQ@j>^<lTe->^2(-4EqQ7N5GSuq$xejFa=WKE>W-wq+dY)P!U&asHb|79=V<4=PIj~bo3Y#95h$u}(T#7hl6Rx-^a<aN3F2r;61!OjPvw8uul$p*Rpx#MA{t+!ulht&xC?89Nf2sQsPl;QJYy=?G|nIW5t`h<`VCJ!fRV(W+(#ticBZS$IwlJ?9DZA9V3)%Lau2yj7V5|sKk*~}z3k;pq94QwelN)8Z_wBzaU*Twk>c`%uJe_r5*+XtRyNR~*y+)g_CD$4|7uxYI+g92v(KM!n}Hnw%J${yY}roFCGP6diUs@3C6k;PA;Zy?yEhmSSm~dcVk@6qqk2%DO1B9E<q~A~y!NW}+dq^;c7E*xFfGufmfJGv8_M)1r2JOQn6$82D4m|}&jBMo=y!(9tBiYHVee7DqQx{&&N-m)i^%~Orta&#ZGIZn9K<N|xD<4KYTzp`#K5SG3|4o1OBwR44G*#|ekbqjH82O|32b=*43)4wE)nip{1Ayfpm>J5ks`W4-bj?Rd3oz^eUOC5B?f%V-$%cu;*%lt=K1^AV8Dr%(LSfC+={M~QvvH?WAUDSMzR%%k>^?bXbJwYc)zJwdCTi%g678}(5!fWoU9DEMxgZS1?@Y_<%{Uk5k2zG4);K~E%D$mqhP;akZLMT(H8r_E#jO2NP7cBAuVq>hq{T1OGr5Lcb*%hpt}BwsBl<@88PfsvmN;|+tEfW6*GAFev$BqJ?m6i3PWYY|M~axK*6s0LE3Ftr_tnF*Uj8dz)G&}C#kxhG#yL3LgnBxnXc@qC&z3WV@qtGV|6*{m3<Yh4{5s~sgjnkZ=e(hHLVhA>@U&WNwi<ibavm0++nOkyxt4-lS!AVwkBPjN=i>_=orQXe-z}WCA`neHi0@Kz>`pnq<n0T^**f06^#3`BSuF98kLp!hC8#S<C2OejY>u1XqbZY7{wA8m_1e&Nz@IhsQ<UGRnozZ0g%nym8II3-v>fX%CuP41>ax~Q`XtlHV(;b1X{0h8$#^Vnvf0lXwigkyx!&Sh_aGaeP(S$weXW9jea)ugaZ@aI%m{dIY{o0t_F!~DJE%hmWgrV*&2?_@l!~az%e9lLscK*>dDKqf=ac!ApykkY%G#gX`aOug2ovwD|>eF_LF4_(`2h7+|xy4airRf6I`xdW#~<-*kw7k2p?t_aHj7g@fwC=%*2M}H2}jr>GgyvYE$pU&#$DOQ|uc;nJnjA-z_u$LSV>_6jMHqT0%~J+z~bva<$89|Lm*crvs*-o^vKT>@oH|Se}S18uZ_0C>xP7X=D3bV!tLsEGCI<+c5>+JBk7zMX+ObyaD(CiD4X5e($`d@h+Fh7deT{{0gc6Rwyb{faZ>}(Z!O{01z_tIA+DQy9AT^;P}}N3%fvFkTD?62m?M3;8>Pd27Noyp4bNAm4>O&4#T^J$_GxHc_gMY!ZFJV(h_Qz`!X6`TTdSK)%54VHwJq3BuD^cpx>jtUY_J1T`+7)JaHnjM^)2=^f0wgFepnPTn5$C6GH%()<`YK?hVGwM*Gl?s){8P8sZ^^&DNF3;H0g|I{bhM2^m_I@mJ!Qa<87t(NBXeNkLB+zfq2V#ET{H`mPVhhp0#{ihSkbXUN3R+-g7!*Vas?e~7|1N*(BATvM)`58l@uOu5Ih`@%Le#Lbc2-9U7)G`1;)qOQ&<x-3Lbn6C1QS3p>EtlEg}zxm?&c5QLHh2HI0HYy>`s=9l&+zvN>n`ECfW`$`^RP{wxq<xp*kcm4>3`_ZCCH^ododP^!cQm>?MP^UC)#UEPSb<s9&NC^G=eDP`!5{$R;6;m<krRAL70tAvPr}`pkO7)`MVt<!gcYlio>ow5xx|pPb0e1>JryNXDzPT1UhTq3B}bNHQmaYWf|8yOoZ4FqM5<;%oTYoqULgL4`%7Hblvn)OvMwf3eVKpblX2<T`urWfh^j53+_DDRl8Ct_(Syx$G>Hih?BDiyGOGKB-eoCXwRlm=JbUscV|^wAGkg8ol3)2K8IpQhCL8x95P7gjERfqP!mlu$#}a|3q<TO@a5nN5YfDQ3N5v#TdH3stfzoA(F?>?>M>TJ_vf>unlvheWCWc3P4)~=^lS9ktAoGN+$qn?UG#=KQ;tUkQ%JG}MmzPgc!9}INzj1fyxjXdSy*KWE-dp(I!uJ-wJM_H&pW$xL^Hp&=x&L|h=DB<G+`V}|iZ@SwUvHl7OZDcdemr7jyxN#2zwqKadHmco=8;u$h*w;Bs^V8Q=7|@^Jo%<E&*;jNB$?9?X%+lvB9i>Z9C{|7p5!3TfpQp0b%D0^&YXCVBx<6W&WtuN!PKHd%_T__A};(<oL5S4VZC$af3xsM;duZQBX$hR-7A0LXEPn_{o<ARpTSR#EYsy>H@dJ)pAzU`;j*(hRUB<6Zr?@q^H{jlum(vnl8#D(TZ3b$Anbyl+v?1{YQo%c=gcCgom_>+*GKc1$y{f2nweemc-Pi3W}Y<HuUsN?^x8pgw&$m$lOC6zKz?)$nO>~cHNHC5R9hW0mT=<@8mQ4Pyo)qa&Yo|$)(6flm(Cvg=;gDxo-oyZe2^9?2^xt^xS8L{%r)oC0mWZ>iiCwJ$ihD7h98ViH*IoWa)|M_4Q9GmSnq_}#yO!zzvq@D1U5C-4N>0bI%Q^4-@1Ct`Nz|>+X+|CAI@8EcC}|_E%AltIRDwz>-39XMq?F!>9!K47u~s!P8fZ0#((~8Ck$b-ehJ>a_R7Zt!qo#p9rD*d_)>F)$&bf6-tvPlT~D}q!Q+#~Z6;T5e8f0t;JCA9x%|^D8)}?+=D){<!_CWo)}ISl=Kt{i@QUjoo+y%ZTp3;~cBXT`1&>fl>2m}R0x-!iPo5XS)b6{jG4tpUAhr7{bq~-A;SdtDjKb{(`9Xw=?Nh0XyfGH^i3h;407!<HWFG38oH0V>(g6!f_)b4D7+57_T}lf2c)p5#$l#+NgUPmbsFF&FKa8WCqPT%HE-f%PzO6{nGEFxm`9iY=kj@$k(F&p$(6BL-epDgSnL4!>V2A`%6#OMjA|2j=w7H<~f_`IC4V}gGPtM4>UrGJO^siYDEgj|uud`ve6oltcnD@|28-~?n!+<=_H75pw|ErfwzvlyAI5DtN${J}W2$@l6Z2yprT|@aDl|5@6I9)Si=&Kn+xG-Z7{2qP`0~Ej)P7IKt@LgNWq;O&ohbN>5;vCAKPcOMIH0Hj*hff0r4C4a^^gx0@`n&Is0emMN*cpd^B0avE#vghQsMV6mzvay0i2)=wh1LAIAgtV<Jdhpnnt)GNF@QUcu{2@;afHNSEheAC07pK5kUCT&IucnZ6$Y3pu~%}@lfO=U6#y{Icv4w9u;f?J!)59Y;xu=Z5k>8pfP^gEU#=WpQt=G#x1j<o8CR0=0o-pr6M?@a;{$`DuaXpO`O;53dv5;G?Zu93dd`sQnlE`k4nDBk?jyakq~|M=56^k1YhQVp{Wp*tC>VyHS%upERVYv56E{`rhbxtAY;1kZb$tW~wyjH~I=Id@5K~@N`2+erPU6KQ;aaifHVzRA_4v9vF@-wsBwb0}Xq3U#MGBVLWzg@ZMm<?%zUZ`#-y}0MXamHM6;q8%=g9mEcC);FNt@Afr6Oy^9mfVb%yvBGp&V+oBZmxXmPvoi$e9_8AaH{uWZ_4SR)yEcU`7psxDq0QVV(?F!fC(`Hc4+Yt_gZxqmwUPZW0+n-pr?FyLrCY0eM{JfwhJU-)p=%^YG$ATWx<wq-;M)WB?J{%~dj@k>kS{#5EeqXM`RA*T2lcwEERo(^<)V8yA3GmBQj+qFWBhXj%pioZ>SjengQ21Blq~RHa#)m?Xx?W=L8URtCvkF-Gf>lv=7Vqey&i4(g8d0uc*?3XL8*8>Uf67ES|%YuFO=79@VzLAQIL6beB4E%A=6^f$uLIec%q;2tA}I(wktY&~xDu>rm=9bI>zYY3Ad0I`>*D6?S>rx=GSB0Q9f`SV{+1Fz2-cr~?d!`2NAg^aQ~rLCk)$<3R&YCoF(<)~VYIf<HF)p2WV>@poSi}ns`Z!)iPtSYZ;^;BD33oaWTWVh4<)p+8<hsMjUOXeHdbtcx-alj*(+9N5qVO;%~IbUxi=tTi75T9zEEmHBdjH?yYNV`soHi+VLRU;Kju=|w{@|3`ajOjpP_g1P1Ga1eXoMuzvTtPmHWU;Em34-|if%yF>ND6N#1)y<7w)HA9;>_Nxt97|6%*K?7p)f)@hUyP&QN}D!zHPvr3n0J5{J?}_^0qa5;MD5<VP8ourJa85tI<vr!<#qNu<X9O+EkP%Z5b+!4YmUi7jYFsbY57)8_5zQW-Ogcdz%#Bx~IifIY|!+sAlnUC8@8h3KHL_G;b10?1eFy(H@qZCtdRfZ1z(UDla@p+my-8*hn%AIz}IK#+VyezC1C@x018+C_|j<bV1!v{3yc;`=MmM3mqM=wEw5)DrX7O90RAxEp179Oa!sXWRvu96}TgSVGhI=%YKj;XOP7E9;A$ek4IXy^}7<U!knfb2Ro&6lJft+kCu^Mf>P*G;M>QU_)mS1c72NZFq?zdHzwd#v+r!`4Q$9^Iq7!R@7Z@Xn+C}|atPPujrL<y#HI(RCfaO53mv79F}bc|E5!|MablE)9A*GX>^7lYV>aCe@Ho;cJaV6s=kq9S>L5pV2sH2`5PQ^f=48_S%U{tbA}XMpt#Aw>Z^aVb+hU1o4`Q(dSj#|DBb?yWi-YsDwow5Ykv{SE84m=hpg@(YHTw4<@^x$Y+NaA5vR2z;1J-HMh?6-1dh<t}C02_mA}*VJHTLX9V_Qq7c}s`u&78<)%VWsaSLs#c&e*gA)%PPWHL+d!sKL)zmnk*w2%|68zhk@R^S}VNTqdP5kk+$y#g+Vm`<q{+zukcJf23&3b#psC?rY|D*Ljg!b4R8TNyYdpZ8dHd7tVGyZ6!CcGiN)h9<<VkBDW=1XS)CuGxD?oJptA8m(F(OF@wz3o_X4d8p|xHXzogCY~^WJcWm5Rb#XMb^J(G%;P;uQotAr~Z%voYJncvZPot+@^|awLW?Iy*D@#Cy>%2k2;-moQqbq6ti?5X=-jpR0oimDaK)Jr1%(6pVJ;NMycN&GAC0N2~`Y@R~lRb}|QtZMWx<haP-z9f+=8i0t+)P1{jNnKad?;+JIwNDqof!M>CLBAr1CKgN0r6??deU=wK<TGA_}e{JsWNYD%G|c5F`9&uv3~GzmE~tc-atox8>Uyv%?^pW?7X&)g9+nz&j_U6CKX(9k`>pbriy8VvzGoN3)O=iXfjw#AE`bZ_-~bt+$gl$l>2n7N?7QYo6<)mm=!=!r(@tiWh<1^J4NY^Y9eTP^F<5ciFwfW6eQpn<TqL7t%lCW4#r~C*NFp9vW22n2(v8Eiis4csGa!PXPgKA>QC|yD-XeE=!9TT10AmCnjMTFX-mUdWrDzuN3lO?H6-O12wm+&JTwEWYBd(~|7O$RmK3PB%!JGikCP#N^w8C2^PzY&*g-bS5|h0vHc<8ZEF+g6&%C2;^{rOcJ=bNrU(}sgx*1DPI}@>2wtQv+ihabGR5Qor#0gX3EMYs!s3{3VR}JdRC@7=XNEc1vSJkI6e^w6OlklqKStoFVw$a%VW-)Q{WU6dqnPN^s$uzm7cOjR7QPN!+N5~7KS5ms&OF3)GfeogjCBeKv1u&ak&sbJ{O?_oqc!R3tTMlw%4TEQw92H?#PG*vb;9dCItnQTO`Qm7H(dC5$R#rW0n`y(xnrZ)+kK%hb(>!>c@7;=Z*`?`S-&-QJqkQYjzIU>6Nps&j;RL*q`dX$_Hs)Y!OkE}cpx9{%-###3X&G)V`1q5Nt|X61Pj}j~@zz-NY)BYZhC)|T3#DAo*}*v{aR8CJ?oEUlgR-4fy?GZ>E7i4AZl1AB8>og!C#qno&FEq|nB%RXb{b5tJ5c`L;(LdT?Gzx4#g30%>G(~Pr>kZsLIK6&LY^+tP{5WAm)`6Vzn5EKEDB@p<`l7JQtF+159+U<2;-u<Svr|FCRUs(Lx!1mAIgTiyh3RRX6zwA<XVVhONrc~Y0N%5`OJo0<g$E{s4=HDlGO)3{O?K9V8s$PrWN*FXd^InPeY=z75J8xC+b9Y@bo~HU*SM+{B^Kal@~4_FTui==Qq~*0K2EsSRI|#p9kb~JIM=B?L&uk=6>!66F!Z~ah7x8kZdj)XxjhiPG9`8=!@Y_MYyv-@BFTN3*Xz}-oihw9K{+|-f4;-WP!VP)H_r0&Q!cJ6@Sv1is7rzRQw`--XJKBjKoWV;)0#%7wp9Gvsc-P!r$4yM!)P_r4$M|7&E<XqMVYl<wJUk7}ruM1gjz0oRm|YbIgP^gha2e=;t_5%ghJTyYY9kaGcTPm``-c`zr*+nsf<P(In_$J04)48Ws8{PTK81Rk?O&#J2eXot@b(dqH}v*C`Y&JJNI`l_fa;ii@8-bCOfJ2pq!6I@;&>@W3*rZ=83RWW|u&$N-%9ig9-Fv2sL%C9B5UKcg&0IT(%4V!X)Y&YH+w@D&C4wo8&&8VQPicFpI!O3!-R>=@mP3+KGV8T(XrH}1Ugmk)0CaA*C&J~exedXc1D>!O~`t~@_+6Q-BhS9oma(o9v^MP+AaFNTTrq$?RYQE~R-E&krb{hPB8E4gl>do3Ayi$CLw?}m#%)8fw;h=T6o!WOJWdG{_^iz745et&oF;tOwGznGUV_2S(+HYe7iyUkj3FR~UdnTq3E;}ds&L0LR!&BgIgl#0eDKJpS>Gy81qPG@w-@tkK&znfPcEh&8V$XG$q?_qrRDu?ieHklZb=}KE&{u0mVf+N+_yZISHz49>YUB=0*Z8E+!vJJzM?Wrzw{)$myuW=41_OjS0XBCS-`&ux=Bh299ljdno8jnB@051taSQc-OG{sFKxy0sSTu8B6wq(<3ZtewmH~?c+j^7Iva1x0ER3|#|x<TF#J%9~QZ9VcJFB*J%Cgk9$myd$Z<Kw`pAM3X}IVi~TWy5ky3O|LxLQKU@R{|;ip6H8q6TU(JXOz7*)FV%%Q##WTg*{6Es;gY*mgkWGWE=pHmQ#ipJ(;GS=|OfE7geX<en0wW)55YKJUDsnL_xf%v5ms>+FrzuF4D@$1hx~M09%&GA{VBxl-Vw;zzT*d7>#Q&u{NyKv8ve;yor(^nOolQS)3yXS|YzcivI`zC`G&JX^f&0rv{>hIyvF#Tf!zd3tppS_SvPoAU{?~OcOHXE9;a*%K<hA<=suRDtI6tZzcWjAPIfk0_OL9Xo$p)d*E4QIFyOyEf>=!xlluLJMz0uthV!s!R)Ia3BRH&Q%p7fPm8Db;iUN0al07}uXV=3lPk~}4KKx%mo&V_;5ey5fqS6NWhah!Cx>NmntnJL0Emfz7iT*BBL}ZP<KPhpXdJw2Zn_4jXnbxa8Cn@?%Gj`R(pa7hHT`Sk_iLg0frV}J7^D${IY3PWJZkS7#|Ruea4;DqHzMG9k%`f;fj%|hm-=uFhNdWA)AcGv&j@(4YP4w<FALK9k6V!b+v=+M3+k$Q#QyK;oi^{PWb{JGn;uNG$y_2Rnwx}kxrFCAjv~38=%NJsRKoe(GD0qLpm;%udoq&}ZvYQn7I@Vu!e)mw+J!e^TX%ctun88i73|}+Vwh{ydEX34i}SK$w%0o5qd8)tQcf>8>m#e`o##pOP*2RHveHT&Jq4eAH2-n$j0D=#q5QHBHfMdX2?w*coEx@&q;B|M+>7z|D)PMocmMO=!uJ;b`{U1hQ{3f*?{)h7pZ7Zby-t6x)8Fg#cB=MW6ovh@7gPPE`7tWk@0Znjx%DY;1n1+aW-k?Cr0=M!6;;=4XsQ|)rB-i+lX=bl3n|!-ioa(Cd*|I-Yxc-vzH8ZjR{6%q`&vZwQw?~2jJ*}dLinP7KQG?T1(I*q>{UPZVJDTPCQ&X)FJ7(OyBCy(n<^m{-K9wLRI{ff*Su`Mlt#9DpBk-RbF5}^y7(|mUzf}a+y#FwGdz3c{HB(7H1&tYO~o_a==${i`8|e<W9B7%f)8eo^|Epw<V{&6&!@6|nCkZz0>jQ<tJ%**Qp4MIg%<^T?_O3Be(hWNrAqnB3dalW)$0}d;JiCinLVrQy5QdVd;j3?UKH|cvxM+so&IGN-t%|6m)^bFG0t8wncL<qhrO(oyC{L*zW%efs%&tW;4H7a>l^P*ppe&H&n-mD1p+2eYs{UAE}x-fE?)_Llph`?mT&(uuhx&SCn3@ndGz0Nzw4Xtvno^0-_cE(rhRE^&4}v4L&^^{RQ)8Ht0ZU0CL|adlAWC>iPz8=Gz%lQgY}{&rB05Kd-IY_D*2&`kOnGjHhU<jj28=gVb4PQ9);FiON6HUwS#Hnp~eN`IG@T%4p?ov;2z1b?mQ}GaRBG}FrqlnlHs#*k`t<RfgT2w9S)zmm``Qj!wME93D+)si!Z871u|)XQDeEDXRX78ZSCr}SPVrzWy9D60dH@*$mJ8?u?J!w#F#!PLgBowm8VJ=QX9nnH4sNcap>r%v~nO=g)JcVdT#s|O4C;X8O+l7Dw_VbsS*>ZN|<;lM8A%vk1HoZ-xEl1o2;Kzyo(f=nvwMd5y@?U3|){?+!eCE0Ca5(6r-@ha_i3d`VzYgeI??vW{2o-qU^I$N#zm>sD!2}Y)lpA3+}$?$!T3~3M5-m_QMqhe=RRp610ts`fnZ$>#CwjYFs7vM|yk!+@g*B$nU2Pb{G=tfa~e}1g`QMjVOK2^>5}}{|@~02IW7e&dUp4s;a;T^~)_0{)g@_`e7tZ6J7+YgOg<`#>9k6>J#ja89^cjg4~9SZ%m*EXq_EJR#-%h#C422_g4A6GD&g#m(%5hXIq+i9sLl?7{Z?tB<H9yZ4zjiv~1lK%D=sUDBLbV*=384&)4}>*DOjy77>##B3PE40aocTxKr|VUg20NW1_7uO5Z2r&6X2e!wx1vSoE^&yQET|QvhB%vlLe0n_h)&H8gEUX1{pS$ql;-oJ_;G6DW*&Fn>y6RX2{`dyXbwEr4se8?V5{+QuAr4f>DxBEo-z`5IRh*0l+IbpL>VrExt3jM)n^*xh(>(9Gy5UX+G1oui@9u3jP<jTbZAC(TM!bye4J7JHzh<xr&=SlXvrApD~fjJYLPi?!9HpCABJx+H=-_9e;qN)M~&0iErIInwyhs6@}7vbg7dKG`GX#Kgy9j_Xt&tSe41=Mry%@+oM!shYu3i@@^XrEo8Pyf<*W9gw|22g?7ix!IA5w2|s1F(-TjRY9v4y|3Q#ehNuUuh(!GW+Oiu#p`PIUHV{%CKep(kvg-&VQT58>P0`ZtgpWWWedg&h)IngrQtaHlvk^cjs$AMs6DYkxPxxN9?jT3(>F%z-TcojFNUKd&i=$<@maFpak{let$`;kW%1>=)IY6Tj=}~yAT1V*F#fE{AY8vWe8Xr#png6^ks5paa~g=eFI#&I%0~IovGtGxc;=+=Gr#}-xVA4%ZiSe%d`)pBn&OI=I>{}$mBto*ddkx@Kyx%gx9l6D*vehBuEK<ZsVpVa5oCsuD0=B)$11Ky8C{VoOiw=g3LIjSS6eQH9Kss;)-OOr;R=Wd(6&_rpr!%bgyu~qDc{P3$V)WHZp~NBEzz-9`Vh~gs(#wCtEU;jjan-$o2b1+w_SKtn0Ncf^{DtM|JztqY2OZE<iVHNJ`9bLh3KT^uGSoHLx*VklaPL?i=`h8Y;hQ+W9dgLuFJaJLL{YYke>v&G{vDQ3k=Z3iap9W_?ZzL&CR?3x=o2RTi5M<UTacKazF4*9K1>FeNJIEZX}Y?M`HNAr9qNk!0XUca~Lpo2wo21^U}fb*b(#c0AJ#@(pM3w32Ik@daAn{2}({}q`_nef0olmJF}0bRMrB29l3a9?sErf$oD0V=(vtFXzx_{OHs0IICU)BrlBpr2Q%F&3wlexia>o&N3CO~Ot;(+Fj;|aCGr(6hO$}TsXNRvL{?FP?Fj7&91S~aLzZ7Y!!m5{9g(Ig9S26H$d_X1E@9Ip&$MS^lrwY26ap&`H<icAv64PtK|*g({7yM-Y>(Rbi%eNsRE}J;`&mYeHA(=^JvZqW%Sp2PnhFitNNZ*<+gi%}2dc`J8~I*v8${L^NqQU|r>F<aL~sW=Rfn>qiZ-C`3dV8eCw>-tmjtl(=jL$$)bs#ss{h<1mn8nI!NITl5Tor+yWd6MT>l8&(3FkJWu6wwMi8rdMA(%1oQ@}xuS4TS7Gw~Qmn}_PpTrh`)~0{p4PnZRs}sG6NSi7_bUH@q8-0dB9EZUTNfRF))YdKNb(rXmu9YqkEL1Q*m2)yl3{6+*{QdL^u+Ci!pPukmPr1$25PrH-Z`H?1^^(Tg36C0hO$Kj>luk|(z-2(MPOiiBfOTkiK(8rB?o(Wq9ostUnGYB@+zfB9(IqL&RM){PD6jm<R}nGF6!7fg!Bz21@G@dqf49EL+Vf%_95(2w+!c(>GbiK7Oekr5z`8I5Q@zc26oT(#Fyjf8W6ExN#g9Yd-44ia@WHa41J3#YDEhNk;1lx>0~i4fh2r;Wxu>vFd#L2|h*L>6PiJ5_rVW^#e9J{D@#I0DqFSQ1>Izgd9Zk3yNBSIETHGi$H4m77#{!ws*x$Y3UBr13vv;0J!A7+1B6umia*giNUl<o{n`>bUCiA#DO8R`V(@Imcg5_71MdVE=B8Mmza(0aIli<dkYce3{owNlR{B_mMs7#&|l*YVlR#`3a>w+*N^Ny2jh1!?KD;_D~#uQ2Hk;w?_vYn)=>(N5PQPI_YHaiSdH0C31lQuRBwO(#IvC<~F3al}XGqP-!?NW&ln$Hp$Ex#)+YP3%i7lo2&S-eg3rtmU9=3TteRK(sb%%@^ChtXri?KJby(>2r@&h{9kpG_;PEyrH0623s6%Y4d|{u+Cd@<W@<r}QK#YHd5ZR&U963N>XtMqELo!jOm(6snf-WEAwg10iaYkOiyGLzJpcw#2VSVLoTN%uHBf(M;D;P9l#d<(oE;#Ls7LL(!r@K+pFS7M80J%ekg0-dMHmSWfkKeyo)nqirJIBHP%E$wTUNj++Pyi{cgL(QOBDrqkF>B8@mw3XQQUG&VDZ#xic3hT6=dHsh$xyp(6`O`h?s+KiJhWBT%h8NUK9RR7&a+ubIN*romAjV?K7ZOwb7M8NF{F1sWrxjY)CrD=oPTCX(4+uSV(T5XuNw(UsMg8E|RXi@aGVHZ%LJdbM=Cz0NbY?yN@OmmA0vqyJRs!^V~%4uZg)DBFJ)Xi(~J@>3#-Lrah*Rj-o)I2pHc6@*XwYfFn$%o~hwFwVoEY_ibF4<0;7<ESW&@Zn)Vx0MZ|4xg!(_-$Fg8QHM7QVOeofdPa#oQGv@64Dxf#c4Mxie$#%$UDFm@y--<=vPu`Gps+zWdJ1n3Ug}8KWY^tN1ZEtdXE4UFhNe)=-fKkX<BHo0Ss|7LIfDb@W0SnTX{~2C#Bsy2@#IPaVtm<HY!@ij?PUnDj0pmh0IE{l&q;ea8j&Wq$rq@6kY0DpO=*y+HOW5tb9_RZ{^@GeuDM9+H)#UgbpnsaGgO$f#F2`qG<!%S9s?<D???sv(@W>t82>B`+l_7wndBMbL7gR2ioS<m07S<pqQ1#pgx%fX*LloTdUHOX^QPcI{kq@&&=km((UN$t#s$@iN!sEkC<guvO~!US)FFb6nnnoA@i?1wF$T6fa*xL%GUFdA+3MTukze%5#NM^GaF8^b+4<diwE#NRjH@HEyPP7)FxE{9y0TU%5(TaqlPsIcFUaz&TTxtn?$yB=4ax8Llf#z977L{mhrzl3}SWnM@XPE<U*sqP!%v#G9>mQ(jX1%Lyi0e=f4!|C0M1-(;V^#|la&{C4Nl2_PK?Q>eRG8D@pnUJt1mOkpr5BD@*PC;59nX`;f96~YzQbPg`x9Dm)jZB<t^V$25~No@bAyz+#i$d2-is*8s`EUXgE=*yq@{SAN()He$O-dzS}!U-QmLjlD4Q(;j_)f>vf{Q!8wO0TRE$v3LFhtE8nt_~Es<6?v5bPrXzwe<ODhK%BBcB=qjOFF2i;|ah98lX+C8*K7xS<)eLfOprS+Susg{~1_kMxTG=hEF)xejDv-|KMf`T>bD2EJ^v-@BFq$ZEM&<@DlAYq&$dP^Z!%#CZV=%Ynsrg=9tBrtJrI;UEJc`c<;U<?t2mM<s%@IL{7_wc5K)b8wO-*8e~Bjb|Q^T5;R598VgJn0}>m7kPT6>p<O{FQ?aQgsfH4yL?R>#_6&4<-}jGMtiAR=d!KvHIX5nc&Aw}|HP<Z0_{;DAK7Zo@h%O(5*gCic1<Q61#B|As`(61n+WPqHhAev>4)qCJpv^sg=7wGE@;W);c7%#NY}{$&U%}-#fmVIbE^Eg=`q5MDw7lo8++7|d0ufiP7_%cptn|F=Wz7v`Y2S+RFl_hGp-0C(mb1kxhg%9jYK#LkqFAPTA>4kgEYLAwf#R-oXkB*=piQH$I3)~DG%lZt^G$d6zTA?HWKB<4E@j<)E(3Ll8@1(|_;931s_+BB?I2qgewb-Pa{N)kk_Am-<F@4##_(fdE<ouSzY-)kVHBW5LB0<^1XfhYdbCaz&l6M}e^7qzZ2YFY{~XZ7WTQ8hE8e&|m7C({I_99Z8$wF1X3h<iO|#{<(+89{f7t~w&1rtY?@MS}j(}mYd`1vbPOSaA@2)tSIm&iTaWo&+b4=mN5L14=)~H_$F^zjpExnW0Xn2{{=-_RqKczK#SW;sS);e7eE>T_2&hRZ-qkgS5ib*9WecpLeNrCX*X-U3FYqYthHL6+hVl%gEt<kIVN2^|JN31g6c>}oTEHs)v3NYY5d^aZE#Da(40!%l-cfA%bMj^>4SzbY^Mma@LM*_0Tac>WiN98kwt(7N0id`e-jou(QZR6RZC(AAeeZ<YHo88z5m!SSygM5W!M1wYMa`**6V$PqGXPbmo=Y?_JN3xHZ`l69Mx{6WC*X@F(E52fY%JvzicE6)$s6r)<CXhXuBcp_+6eF03I22v5kHj)@kpdo39(4fb?clJX%GSt)QZ)eOVjd+X4Z`3g4@qElP!K1vV7i&SSI0jGLl-8XK4Zgo?zni<fBMvf*~s|gSUsdom=)V}suN}&=4mxyw#8@5J!$pV^0w_XXT~A3Atu2qGwwtds^)|{M<H#O=gf<<WdjG!vSFO*%Zb`-2wF>FjG#I&F5j(~OmVNWpFe_|SI%TK&2MN8M>A@AhJX_dw0EpRz+g4uSkI&!wlCk(If+z91powGM}t56P~kv<^ADmpk1R^iorX|{9H=IXC^8C4%di#5$FM4f5C~XqQ4Fo!UTh;flns`t*g=BffB{<)t=cpNhJ3Be(&}iLX(W?pZc3!#t>7ft_4O+v=X}boYW~W*?ElZ*xW<VB7)Z9^L>&_C%t&Y3a9i&f67|k(ZUi_Ob~X3Fz7+R#2v{J2dw37`5jsJ(Mizx6zZ(giKU7~s+a67NJeFvJ=pW29J`fe!a|)%nnas}$2MrqIvZ{eYGZ12jH&fT5qo2jy_B{dDZPFGXaKBt)GB{~DLtYnaUBxf9oOrC0RpmSP_qYQ)c?XU@63v5WlynXP+`s}^Ndv3*z*tSj|G$5iCnFs1b(q%WU^M=9j3$UoC0NT~TD^akv3M_UCf(*5ILuLlg$$fVA|7;_c<uoA%%u59oPOtMB<gzQp|z&)9JsrHxjKmI-dAksR=BKMKc$F#qxt3r-k3vu_}-o>;7!F0rfHC9S4^hGz=Ku3ylE9wRC$~O0USX9P;Dm-D5IE_ebS^6mwD5IIDIiiWTNBEOKGyd1+zqd^2roHgQ#0Vi0^UbcMlByj~EKz^r#PaFnwR#vIfQ=`7~lLsenwx96d9K*MBik1DP@QcgsRJ3Ui4!|48vUoncwTU)}}*)m4%BG)=>#jQpXNOegQ+cL5;Qyrn3JO3o6Dk{`s=MBKUfW63YWBBcBffB6mzqZs?WEbaj-g^~&Q>yM7*t|w`SQ<8z%b$R8#dhyO&U?`v3nIlvcp5K`rW^-S<Gqdf?)wbN%Z5h*(d$QA>Y*rgG)D6kuD@Gv~yU{A{oCBY>q9P>0?yEmky|?35jEvGtI>_C~;5-<#e6bbheW--5*O)LH1-Z337);5OK&J(8`*~>YaAl4UB<F8x*z^%VxxemyEv8*eeN4XqiUWv#d`8iaVy^G2EBL-uNEM}Fy5)}ZGn_B#B-T(;NsRK~QnI=fcl3%O9QEW!w};D5oC>7SIo^Q3s-lCnP(@36MQ;qGM(%-p$Dx_p+Cku0zVw85PQoV9^hUy`WzXEgnI9OIb+?H8IIYC^kIN^WBB=oI&Wv1;S8<96nF6UsfT}kM0rgt&G#*gF3QTajV}yMoLwr_;=AV1n?Zg#7)UxyVV7ICq77YG3)H`V}Z{(mGdBQ#3*O9AEqaM5&*-B&9D$>m;_Z7ST)-lYcMvFLGaM<!Ge8tgTjOiR^sjm>e@JKK549}HgKm$uk?{QP{{CBdh4%Ih&5Gpl(VEME=b3~>Nqo~Q!og^4TW&(?L_=L|qD@@m6zm3*2BHzcES&W)5x7dez<|S22_q;i0TR6NMvHP3fWbE<+3%P4vV;+N<Q!9GV|6dDS=>DTKdsXdZQ)8F7j$JyLN|5RyaEbo9sf?Q5j2xX=TgwP*soWAQMA_Kh=D?+!N*U6;V$SKMkML9x1C@HZ&GP8lIcmuqemE>`rsHgq({7~MbjJR6ZKwhJ`6I?F@n_-?LYeoe^(Cr{3kjieZl`PPK{s`YIfMXKjbq88qaFrb7(VE0FVJJ)nz>&vVh~MF<yv*)N05RIIHs1NXYUg$k;85zMZwSm41r%1-jXxzMzwyu{2t<CY)EgX;k)`yP1xggAp1k5;R!7tX(I-bD(2HF3bj}iiII=y=Q$RE<1D#_k`^8peiZkUI2bVL>>10YiTTj8P{+!w;REz7zB2TTT-u$wG|oiJWELk{Fylt6XGnIRV7x9yz+vS~^@jc8+tY#>Xwj{yw`iu=@aj>7%EqbiKGcqv6@~fEhE<-XuR0_~=Jlu><QM<D{NB1kl-o0-r{vE?cEBP<o!YP?w1%-zVzTT-)x)~Eh-f#z)7Z<0${l|1qY`JlY_#ZU;tZO5H3;4^^R|>^x+VxUY3*Rrs0*$}&lhS?kwi2mxARB}sty>bWaQpK4XW~G5KAMnHdZf;FT+oK87x~F0)(bQa6vC6o{2KUWX(8)R9Q2Y`7RrT6zq8$YexPS48o<~!La$~zQkSQ7Z=0k>&S%2G1a@Uz6S7Wtybs_DztHfAb78V+8*PJyI_r&F)>!U8j74vs%ca`g4L?D6);BSFK>KkTSOxR0tQw|85>|W{GzKerDi)6%GE<5rxdc}8e=S13V8U^o)JZ5QA2q>Q@57OrgJJp!fW=jL}h!8wGYyA3Ebd0ZW(^+;WuJ{N&Z(N6vN*5NB<Usv&p#N-t#m6_t1gweEvlzcCRe%uOE~b@xYI)aUA)OOW=zN2m{#-#*m%Fsl;Q8R(x@wdp>Hur!O~thsJeJM>gCs#|hOsI5Iet&m0(kvj|#3r{TepuaUxW=xZV02^N}bdpk?$ymE;V!fZ+GQT*&cT`xW}JGe0exArN^H!v?xuBF6Wk7n+SYsCjq#c2Zd8%3oP9>_G2!4}B3sV&}76Hi@UiN=XdN}a&OzDZa7R}@#5h@c_JSL{$L%p7nCnbq9Z)!BbG#5SBDMktM7!~5Fn^N|1n1Ug7aRKack6{C+-yZq+$PA6M*kT^qp>3wQjDJv40`tsX_KU(6=+DmGL%?gb+Pi1@S(Q;DyB1;MW^1rxboaCXp^}u!_QD;^6tK4>1f7aM1S(MbJ$9i&ec$inrtji;y1>dcO5yQd{>ht<YGabh-=((&{2mhFtlei11#7ZMQ{pZweNlz#z>g%k=xIAr{Az^{0pT=eSLT769JWt${6@TsUDA;U*ov`9oqi&ne0gp5-NHgcJdrHc7{WC6pZ}=tRuJY!)-QsCpel{$A`ZYnP_hHT2IseXT`9h7)uUI&*{A=c>_~vnV;4Z$%FTXUe&g!i<#IJsaWkmdu64c-Qa4M+^iYJxStH$Q(k^9_(q2w|yZba$vbX?qkC#!K58qZrQ8PGlnZ@VCE3GBYl5pi`V*{?WU!o~RgMO@4%wVP+}uk2(0)cF10Z$x1il{0%Kcn5yAi^|TB)IKwKzcGT4&~_-5A%DI$et-J*kKg}ESN&-C>D3ilmuEXW&U~$S61OV$)5~KO*<Vv%izh17H9`XfaNU%+bjRfe{^>}Rzj-ypxrkaF={QOIAQ(|O^2U6RAQsu!Wyx04lS-!HQtG&fh6u{29%LZo7YV6EHACzMI6Q2l4bHhag|<N$tAq`bsz*mK34)n!i(2sJH(q_K9uxA2LI-KXm0OjUw<^}eHqIKy(XZ}V&wG~VNPzbY4Jx~5&7*sk?VhPAy1rr3izc2FT&f*TL1o@f`qCgz5)+mXq99D7iw9yQfkKO@mIu<Bl`r1%p(UAmk%ERB0A6rYGjHngH@|_K`t17qW^O9GW^cQxwh)uQa$mtViSG@ug(>UR1z{$j`+6h^eOaA-LjYoo#YC5EYrFN<EV&7{2?h#0kMm0PM_T&;HuA8KlJ3UGjg+V?+;U6*>^HW}DKC#ZEv0qrBfr}?*2*UaFyEbw=_}H=>|5*X;l<)r4nag~0J!dT7kMKgTs~<Rn;Y46i+eda2kOoz(j+E{9yg#ZE;sT3KI+f|zU#-H{8I?VNklXN4SU=ZR?o~Bt(OwLpRFoEA{l>f!x^wt6gIa9-YZ5T=?Ct&%YAG`*jyIUryjlM8={aJ+{8_T{>_-_*&EcIvor_9#7#=yd;_v<K#)4aKw&j*izh`zFf-OE<|!4=BH9|>`d$R}8I{&Uxjcg5_OvA(?z?Y}piyNa?`;^d4R<;0NU;pQcWOOj1#Ccjjnj2T{2hA~ijKHHB_0qz4)V^NiM^9g6)`q@7C>E!N*NES9FLb4MAHTb3O*&4FFJ*&k@y*Qmy-f{;=;<=XWp5zEE-&qNR63eCM>2z`txkE<lrAii+Q8lLRA0GH4I4fby?v5q4tG^3**w1><k_`o79n&<3z?<#2J78tI4?AWKeLDacf{meB5}Y7pf~5IkIw(RKar!Qn{@F8ZRLo3A=McqDzQmlNjhQQ*RSPzetI6M6w%M$a{s4o8@JKEe$Zi4+f)1HWW?b_ol$5r{y4its41@N8R+2fU=LOE;kA<Cq8Ing;oLFK>Eh=9u|bo!JybdfH|>0(>kk4IT$6hmw1pwjtJL7?CC3E_jGz$By+CLCSo?Qo=mJ9;$g`oZpHspGdFn5){mWtuj3f(4QiSmbQQ`=>_IxUHWbhWwkO%7bn|yv)pkLE?)?l^tr?&<*tK}NqrVVFF<xcor^mNoRA0QA%#?LTZaSu{HE|#C(+`UQ*M?mxqa#n#M;@Qp@+*w$R?)hOVIvm{8)2w(&rIL`Lg!_{qAqZk$Sft_66ZS;jH=uI*T#*k3Ny=%bn{PRP*hm`_x+nQ@7@<*FP_ldIxwW@Dqz*(3BSvXBnW@MB)@E9u~0&#4w|=QRd?pUjAVkWL}EZXwWPsMrVEl7ftGhe9mHGRR&Y7dp@&*l491;^7|b(+YMg-!IlgPe+=}H|Z&{O(aT7I)mDd<4rV^yamI-mA8+2zzvg{@L)#9jpHb!JG)tFm=j;$Jy$OODmXkt13W&lEm6`Md`dC8Xul>dMHF4*K9PlUARX^BlX#fuoj6#)#PPa;RFO1RLgdw!xTj5F?-kYv)<w&1NSH)vlmE+f&TZIJh**QQ<D>QGw*Lk+v3qCAd(7>jroQ$$_Qu^}H$l&;vy8%C0qGW0<ytHsG2iO30vw6LH$V!^w{Ct{?MuUZ!zd4Xp{V}{RxnQ&UjV5FvEle2H5!R~nws~@s+Y?v`&K&3Jl&1ExBrvb3R>*-&GGbgpWlNa7u<Gq>F@ljuqgb=}6h}K7kmu#jw8Bun?H~+(LA4clAGw(HwB%F!|wCUc+y;Iq`t$Vn|zA6#x{s9wPKfed&yPU`2-hJl7kMHqF59R%LL8HI-E`0A^J(jXW((%5S5n=)F{e6XrkL9x{4bu|db0p3SNfT0i+a0<9xch_BD(BB<M>5N}qnH*jRl>6KA*X-V3|H&JFFr%}`T{iJ&X5U9y4R^Lopa4Yvy$ei3N5Zz^2Dp)e2`WMS3inGHk~4(SBaVMx#52Y)pzzpyjnO99^|e9sM>Lk;zto;^V;K7(e0v;RNKTr38`91jXdY6QOda`0)`!_h}tpl>p`YcefV-WQ0Z|nIAgdC`XKk!W==&n<xw112~3d*MC@)cV26kB-@Y%_R^XSO>|<Z2QGU9K-St;G*tMuHV65Sqa=g;PR+%ozhv?=l)E`O|)TVXU`U&+1&+l2PKWLmjn_fp`nK-g#`L5~@Gtuj+p`8~MbR5DP;z<qdv}|Y-=_s5^Sz@H?r-_<mAZT+rUu09f$FITfdI8|p2oqD^N&{cq({Euq)z@6(#%0c^M$Ywcx})xSPraWmwnwHO$TD3#0li6EheNlYJ23h01Lyx@n`+uZ?K-5u%nr-X4XBwR`SYoY$80_dZNh;D%1C)DwS9`$@nY=#fF3U^J|i5+h6yXOG*(1-1niik)PqwOd;>zya>84h0KDxM3ve$?A@7G0BI(bS-@A@C=@yG?5Qj*4=N_~KS#{ISH}bv7Z5e7bozYT9h7nsO9S681$(_N|{^pCA<w+%9c3pdl#l@CWY0Hj1fRMk0h;bJscENp!NFU>$(fZc=Tapy(e90!g+lF0lj1apU@bDWdQe?-)+M!$(j%_UGbvPGO5{rEvpneb@px|JjU6cS4I{~(m3|9Kn@)aj4>qYA!?`|262J92a1@>B+3VMv%0*;Qf^00L=Zg3UhPQnX5-U!_e#(oV?=!6A})sR$#UPfENwigBE-}_p|^O=4}xgY%_<H=I7MdHC}rkc$Tom%az7UP+tN}e#D0SJJoP6v6xt;*M!@r<1%u6fxPMVo^o1q|5c&gX@64geXBa$u-D(0=01ts0w}B#wYjG`@!Ctf8_v=R_sXP(5_jFe+5%=dKV9=j#TOaDlK;%+YSJp))rN_K|w{(pr|CKgd+7J7cC29b2#?FGO>Q3*5ACvy&LXeXN@!4FD*4rVos||K3Y<bA}J4o72BdH>dj=x;ZH;S6GYYq?KGwU*&T0b-A2Nt(?AU<#=l4l(o`TtsGyqa{Mz|IpFJlce$MIX}O%hBx%2p%TbB!%~CE0+mYH6Sn^Q|A8yym7#yHqD&~~v^Qvf$lu)11&1vumfE=f2PI^K#XY;P2Ipd{hjw$BEZ;4{gKj0^qAn3p+IOXx)MtffB9&Sze8ylrTR%d=f1GB^0TSRwUqI4R%77Ms7`QMWgBf7_W2}lHH0)=G=&N_Qn83A&t5jhKKCH~f5hiLMAiN$mV=%g~ah|x`h*s5Yumd#bvUB6)2_E?5F7(7`P);gaQeiu$@i9yXv3@R%EZNSu%dH|i3VDZH*_uPU1V%2!pr1BKyE7Q-c>Tz2j(bGV5pu+DaJPBJ}0BkJKPjjHJ(V_)MzEl>Rk^$cb3-K-Pj|#o2Gt*!jPfWy5*%VaZY5EyXL(m+*BC6O$iYTk(DkA42Xyo?P6}V7|<HUu{b$Ao_QNj>ZYQYE!iq=+2$HI0Miu^1f7BVGn5JgU$6PU<-9F~cM{)XJ_F@gnKEq&9-fXDyqr~mz*-&c+dWXs#I-mROaAm3d^VwAqg+hioj@{#;2G$g`>hD1_c%=nE(-$pHm8s_<LUQB{=D(_WEq7Ns+0T#N+-wr6tZ`;EBnH$fZ+xWTCf6!tqTW5QPeTT6TElWA^%>~Aa_|C@WfSSi;n-rUa*hpxAR84DGaxQP!un=O8mn$(YbUR(`jB7~};>|VydwCRFS`}>YR8geq(CKALF56uZSUst9yql_Qv!!M(U^2~u*TP13mKK~fg}7nfz!BTnE(~j00uT}Ez%h_vU^bn-&L`ZoZdCSouo^r9?<SlxGT4L2Eg~uaIJYeuI<+^jFW398eq%~lDkn^(Q5otB8LYev04`*(SjtVD820mgb<`lAVAq(OBu?7bR*vY~h#Je37iRgizK*KT3M>*TcAxuAqE|Rc7=jkMO3_5Gm~f&3MYbj<s-rp<=tW24`qspD={NC)HX9nJ=}XE(#7?j+iuDfOFljwk#Vbt9amWEr)OI-MmR3z1R4V>OAnf-({{jUP%hK6$s`NhHP_`Nfdw{Ln_~051iMiC^6@~_5C3ktSI(xA>@obQKj7W?q07)lOm)o5{NETSG>L#`@5QZ^CqAz$LjvUbT-o&KnBP<rf;Orf;^)FDDXIHo^%1FMuAh{?fG(3j>(b_U#eOV57>=2A5K4t#`YcLYAO4Ex8*rQ1AjXn|oy3=3DPm;)FQH*{=PM@v|eMdw;uv{_ikwJw(6cEcxO;6wi`ALAbXY}75+y=lOlwFxa#(Xk%(vnt%Kes~6i@oX(326SJ!+MFBZ{GnWe+}+j)u~^AjDLigUSQ(WquH>xVB#B%iaiB|j};8?%)r=l2zdQ8Jc8+)y&LxZ0^q*74{b9123MHD+{09)kFyBd^7OjbA>B1`3vW2S0^|O6Q2Q$Y?wYz)gyZZ?u7cVx22Q^TT>G~I)b4-pV@n%;eH}UWw<J3H^rWZt$!w5%PO*tw@p3R((^qbl5-fXW@w%)W$9V-osyjHlWis#_wEf9spm@++6Jg5-EV1p{Wip^@Sxt4jMJKFLN>KBG4m?>WGWm(f`c?XJ`P+~c{Fh(1E72|rPFE;8Np7-Suykgb{Wd5FCm`J$vKe|3plxz>SE@(!$k$>cM->Hc6Ul9tBs#oUq^T;VMiHPvl5#SsIWAY_!l^WqyehwOD^C#A2PuEwR@K`_tB-@e7w#b;By4ExC7le_UKj3&vW7d}pkK4$l!PazNIPW|Dw*6misY6>#299Dx^U_te{Ab!!mat{odTq5U97yeZci>2Z;h<yMg*7B!`_xpeiZ72O4`cxa1qH^;(@hM7g3yN%O~`81+*+y)5^fngzPl3BfwE(<9TT@wIk}*#@Q(?7T1&0?Cmw{b|({gGg&wI#EmI2aM3{(7|5e$5f~V1WY2KjEqpo{L7fr%F5LI|iIMd*8?ukID*p{*5C26X<hCUbVd{HR3<o;bnG3VLHkQ<E1oEuekmQ3<qdcJV5ZB4oM#=BlXnYR4D6#Xb2UWi1V6-C1n8EQ7+8vdUNrDs9cTPcEZfPro<}8kk8R7^0JP=qLI?KvJXUA-Wlj3wTP}M!41fJ;}GArTAlC#x|B$&A^>7&1*zhkq7;92BXU`u^qaZ2A6G`HeNDQ+a=b&z_GL@tTmkBKv;wD)Y;XI%w3#}6c<Vr5Mu*MZ-=!@xmQE?#ceFjg8eq(4lz$}#_rdljY}Q|Qk72~&;~Dz%B7Qx|WM;YJSVkf0JZ_)I)U=AMfz^&`0Ge5j~#)NUA_u)%75-A?SVVy%sa_q$MNq11Xj5QN3z;sh72y3BD>6bZ!#^|z?8S70}v1)CPpxN9v|4x-$*XjnoAv14zWbb!}|Vuob7i+X!A{xBGsr|=7$@zJc}@@N%bzBr)ao@s!Z=vQFwWY<fQ(urv$j*-ZX=?#8;@TmL&0cJgc>5G(6*s0oud!x<~j&}yfKTZG^VE14H{LZqJi#Lb(T^=^q+oF#fN6eH#v1Mzb=+5Ge^2^zS_3+Eze^0@Ez8c)u#D6FL^2fnFecwjD50gYjproaz5dU$eZ-nIwG~A<f9;|Sr=(kuu&9VNZWDbPYJhZyV(AP{Znz9m5!gq7Ye-Ywy0w&fd|M0RX{~{S57Xz$~n26^<-%k%y#fmYm!u?o%V*hlw-@i88kACo%5r4QA?zbN--2Wfm7Xm3^yl}O6#ZBEW5J*kM9bZ(cI@XQ5ia_!p7);~knkB1O%vr-F6}!oYDWqlz`a@hzzNRqG0totrFfBc`NMW8bX~W`jG@!90^r-=X7tL22>d10f^6%5=andZ38fKm#FeVlDN(nGBjT0~`YBAzCMybDjHI1(S*fhHF@4TmF_#zwnxI_9iZ0M7;ShEc!+-K1<t?T9MnNbG_U7UwhES>l!Y-kjl^X&%h^tb>HjBa5@+ldWeE|!pfp6j&Q%?+38prI197Q*Hk>$zO89Rx_uA}7A!Zd;hn?n9Z*@DIKSBU_fqFA?+l3G<2*+H>RCZ8VDv1Pnu=BP#Pp?%VCTj(ZZWF=8BqMbr}>@&m+ia9^QKbB~o$UfJAXhPV9n({kaEA@blyx((kgzue<1(2BvBE~pm=d>pG!2P_Y!J%in7yg{Jd{l;4ut#{yeOlL48J=~KRvh2e<fC0OEgi2q0g2i=Cn7PFzh&<96Xr!NJ0co^<%wk~q-Ukm6iLwQMNzYGC@`SZ@wCO`i$wUiVk<Ju*eo}oMq1xFoE3j@B3coj%-LS2hz2C$;quFw+f5haZT7L8<>PM{q^bd`t@+jin^vWPfKIoeC1T1V%6vy$Qd5E8$CxXTp|C4uNc0FIp++1g+mz+&kiPX|eq^5rCTFz!s4LO>G4QDkkBy8Ys#d_UMl-HxFE2U^sHQ;f*pi>L34Uehk7uqx{UbPD)8fwt&IXa_$r8f-{qgG23wVKd}Rc<DrsgK0Hq|rUy-~pe1PEcn1@w)=)pD&A|n<nEwAt(PCatS$=;0L{5{NpbjO-gF0=~8ant>)vA7WZTWKp^UE{1!B%TNv0zg{fQE=~iW{eky#znQS_M)Zsbd?8sZO!Q5NN#<@g3I`K|1omD*`8$&g2YSR;g+F;ORAhs{@t(aF!WYOguW+&6$+DuzxFju(2BzSmG$j!VNmq~9hXfn#Bp19T>XYxqtCp1XXNMe{K>QJ%;DuYrxI3VXQAehG9A877dmv&CaR33*6xxD}TFCAwmc^yg*ajrYyX(T?n@2OK457Xqjb~x)f+2FNIcYEvp>1WDD+8;$`-8h5lDa$3M;vlUa95a~o9v!nniUuR;hE0~ZNhg4nz%25kCM$!DrK70~q-k<9YlP4SOg|e%wonj~<IGn3a8;&Lz*<Y!WiWO8ZqdZc^H{T03LwQ3=cZq-n0uU<KB$r<AGNQeGq(FRBD_lGSF_;WKkA*<+Ce$qS4=bmWpI63jE_$<+<CJ3Hj7^wWaA+kJ8$NsiPsJ@e?8Sr>Idtm%DH`NI;yMhs#EVS*m&SV7177qLB%NCkG*wk?b|1pYULXrs%i6+Y=n0U;#+TL5?6ETp&p8XrVCS9$42=dT?-~+c$_ft^#UH_S?|S*ab_|Ieogomj3M}s|9PX8{1GwzXKIaXeA)rfBuU3i?Le4Cf<WLYI$Cx0tzBx8aY`yLY)PV{Nqa=&6$2wxNAa>lw~?<OHE1^S7wY--9rk(yDjRWY;FvvUue-fekEpTC-S#spZK9S49!l0_OC0t?%I>sXtpSJdIRpOW(x!7mW&yGdUwWMLFqS|7r_sZ~0r#jfFi?kG*tICNwoHO=TOfwYpU>r1oK(1V#Z!+I)+t}M?QnBiRZZHmP7Lva3;EAqJtKZrS(daPJL1KsN%0*A$2rGndc1@n8Kzvl*ez{JZ{xtldv&1#_Ga-a0@-_x8&IPIK8@u2*<=f7e>>Dn$O4L~ZYgtyfq+0T$FLHKG4Z<E$|C9+Vv-i6IKUm}KFI8WWR8a>PYSs%rYyRIL#OD5Mx{r5dn3s}S^u!C^%6QrT)O~7stXxN+Se*$sBexTOiEN#+2&IgAif^cWL*@6aq3Le46z=wC0n?+#7kI~iWG9$46(-VE$C~2v7;~?4iYu6!6}%aU<z|0k<+IC&K2p0+lZ<{&*xD7cNTz1UsUx6%#z(;i~|}6%3Ud}kt<xRyS1D)^IQ_e4n`#+o@B8CRF?m}H-+(I71QYH!uHNYKJO%;a3|pgPKUE^TEgN!7?)hAh4s&|w3#5Bi$Or6XFuB_c3wrDUa<;$fceRsdY-k_gouEI&7Dbo_Os##n9ppv*=Qku;dSZSk)&3p8L1(S1TLelb8^x+OI59V`Ut^uRXl{ZqPrFTA1Djq{D6ZaPwhjUgD)T1{nsB@HsaO7I^d|9v7i3yY3t;wtrOm+t&{mbSG9E%TVWb;Efq1VUa}9<taT#7LgOkg^)9)wn`=@L#EQOUIC^tUVMhhI?qlU9f7;g6jSt^>87WLh&E)q+GS`x1ZstQ<Q5{x#xxqeuNp%R?K6W<%8pf*Gb;g%jTm~4D6>S?^A6_Y^oe7P?+R0!C2hU6EOy}mbq-!Y#G~8e|Z6@gp|MWL@{~oi)1;6V^MzLUz0}7z`%*M!lMQ$o!b&Wqq4ut$-d)+ft$oYDhIdh^|jtEaFStn}aG-MTPy&xMEF`s8)5o!O#$|ouv-wh7mg4#9Q@=bZe$+y@gt9DA0{BU#|&1xmc-vaxxEsn)?Xqfn2<&(paf9U?=i^^^{fWb)(21#AHr?;_<H7rU-CXjZ%B{5rD{)#WAZScI0nn>>OdbxN|pkcbdoN&2n)cxB)NsbZPAJFn`OJrQqLX0>UD+LONjH8ukq1oW$<;CKM@h`iEpDMnjrG^xkK1elCmQWl0Si+dDd>2otoZd+Q4}LGk4FVv~hzepa><5R=yXhnN3O?G1*|45d2;~)i1&X^Ah7P*kmOTtyBR|!opf7F622gfr6R2$Ux7@3;<InJB%%B}ecvP*jv0*WQB>q1gHkzgucejaClfWNStvCmo@O@QL={Qo}h^?dYW?2gDj0*!L00~b-5bgPjoiTBh4dGvEy-)d$;2B^~F(Q7Nkfe`;3UKNTt7Mjx1c=}d_bjg8FgYTfWYpAe9YCA;!|E@{Oc$?!8=+>P(=mPW7awGc3LJl{xB03#!_$y@g((j&o7@*Cpj)A#ys&<Aw2(8z<(sL!W8>}^<M#_*G(TTHFHHyUDn39eT6w|{@Fa=n@)h{ZWZ!2J7nZBI;dkwU)91|NpF(2uQ)<<hPkvfg-!h*GZqu>;e#g|M!>ZY5QeBaTYtso?=2L|gqu{>5jIqRTK`FWM5*8Y{lcBrX8%<{~3qpI*9Z~rj3FIEBQlZ($tpB~iAonitcO&)T?=Eb2;0N3?-#nK;jV8c(Jj1MNqGeMy`wf1%Vc8S&4-8<+drH!mX*e)3@4{zw00pSUJ%Wdl1>Ka@af{!_UwZcn7o#?^Eb_^rE|pA6ek!|E76q0pAkr4NfBn%<v~--d5jw+7q<I=#=vE|us{DjhX%CH0u}=R=4a`=au{*AL0!K?fB0E|YR<HSKmc!8Yj02&4Uiwpe{@xaoVaGJ0$eQcgRalasltXNaEagqagUfBOrU#s;7kR1>AqI=agt!RxDqNMG;imJCDk&Y7uTdR#VZkJ+`xBqiGnfwUtGtvKYo^Z&+YuMPUp$fJ&q^6T-}%k*OzJyBP$RV7R7rPLo<<pK?^n_V6StvpS~7Xc^^}5NUC2ryfj^trZ=4w&VXNlJ0etYd;EMEziP3SI^I1Hv=^6!SWc4ZKD(w@zUudbz&gvwkkXw1;Dl@2y5C56fV-lNUcQ2;xqrgq^$%FV!MQc++o3qL)aAtYuk$sz0;=f&NvXW?I4sFXnaW+1+<bLJgJWT?*E)Jx!Qp=XsaG+T!VHhGN8`iBnL*VXp)F(0USm$d_iXequM>3G}ex+RB(C7^ab2xY9<(}X}kqmA<C%<ZGM5CpSvtYeRTC_y`>5l4X5e*~|+}NxM3!+O@oEYOm5J{s?ogP#4k6?Uc*Yac_q+T)c)-4}qQilRmB>)q(9Ang)WECAyjgo3K<i(QUxN!yY|6Ab90_$FQj~TEi2ykpZeKnnKUbi6lBnO}$v8kCWOzu=6(qd!FtJ_%rY-5a6z{0L-!kozmB+~4bv)XO!ZkgzMH11ER9UVdj^f{C~qoF;u;-Hcbdj2sXicKuZYTB;zrVARUO7_B(gep2YRp@&&6Repv_D&5uO+!THQ4(#Ot-hcf$UKVTl-g*R|FgIfg}Y9{)D$sQ^Bq>EaBY&Joxi7eZfgD9WLTK^Fu9Yoh=Ue(Y%yH5a*eZ?U;Rbk$>cQN80u764e_E~Y=ufbGU&Q#-2|01u}0PS*$rS6CQI#&<w8MRSe)%6DIUXTHgOSYF72!fOXAvkZWB$OpCO>W{#(t7Irb3eQQdCh;Vn=6uUiKGnJ?M;==_@pZsyOPNEl1Le;}ym9xMF~Xn$BCE58%z!`T>6;=HM$U#5;(iBQX%?~0v;h4ODW=f7j)@r_^q3$;S#rzmn&bSZBbcIE3-{v+Us5!4%+MZE#oBT}w*t`Zg^#)RBii7~g)zo{bzz{X9@`4&~q4HSyQmN-bC$-&Wp^I$|WTify@YKuqCDih8d(Q8HoiTV?U>27iGlQZVrH|1M!-++OD*&hASyIYN_3}k9b{(w;xWSZ=^TS3cTM>#IbQD3``^;cfOV)qG0lm~Xgz281~rGYuHije#UD(5URqozShS>d7xBaFWCqxIoXeB}Ur=^a~f#nP1<P^Z;mwTASSH{l^0*Bqp#Z^AAKPpFBx+AS%Exe0gr_85mg90wE}d&jnhK`ZM#J6N1K#%x+@QTrAZ_*-T&mD&ztfTt*8synp`D7#!gs|Z^4a6K!2>KHXNMT#E2c(ylZyCD)v_9o>F!D`&Y)st!ct2SqY_Eq<Q=OAF%8x|DTJCi?6VbFLCOJLRWBYS*=TeQ&!{Z9C*d6(jv_zUjG8*ZMVSEj*&_M;l<8}<!{RyG2L?a0bKu@PRv>%G(N<$H{t&bF~%iWT;(fzxr6L~=_m$TxI|{UlsSntKFj(Wr?Cxna)?`Hmm$KG^<$Q}?+@^IGw6DSsnV+Z!@oRpJyl<u``Lfzcj$OZhhZb<YpJ@e?l?BSbJo;a{v`h{Ysrl=bocWM1{aNef_j911i1Q&mXh)sYg?I@=^%ld&t0z-xko=Zt&yhAveUUG-#iOYO!^m3Ghw>AEWQXMP(WDN7n36A?822kzfm#emJxsXlQf3@j(}l_>0S!$;bh14+$UOd;-u5vj%?dU1yq+cZkB0IiQ5d6^pae8CIcvAi;B;w0=k(QGG?W*!({91^JT`0Vk|+q4mkX8GJ<>r}qUX=2L;)T2CKMDLvuwF_On^|i(6)K2Bk(SItx)-k$7v}>cqS~3{?Lj?lHr+oYdFVMC&7Wjz#YbpzN;&jc{mQ_55-y2w*mX-e)ZMG(A2qtjUlzTK<O-0i=xKR(1Y~aqbJY~eH+!FvB4;0)$|I0BA4g3H7?N2pK{IxFrz~XGc3l1jBVf4`62=kC&;RMl#9l(<8#fy?Ru{UHEPWz7c3?eBkC*>BfEJH#TGZ6{YQhXKIY%wlivZG7TJ<eJIy(f3QH}|2E#f%JzqK^$nj;B(Z!veToC|=T@@Cd+vMQ1Z;;AN<I5<#V{r(FZ$BvedgMxZ8@t36*n&R8BJEEL|=S>Wq6Rk=aN3a&*?But-Wf8DZVk-#hBOse`+&F#RcI*W8kK9|Xz9Po?{@?a+xXbqV(Oi(MPvg#nlrg7e2O9sVhCbUmd<DXZ}(S0(s#dZm#u}AM!3P{f2)QHiNO|+1*EvW0?N()4=t_9WrQ&|nA+DS*ftAS+kbVKtlPWgZqh?!q5lD9Zz;Y&Abr_76;LT45*E~4j!Q&#z}f7&UR%Nu8>Jc$LbJaQ96o&4r0kL+pYis2w%`<8I}wMW)eFnU6*mV~R5<H_E9>4-TgFneLf10&Bripfth<SafE>-UCWz5QDpv66~ek62oJZSO@g_Qohk2(4oxTvr21P*h<+I7BYSa)$GR^ZYE|NP?=aQsEdks6`0Z9Wk+e8XFeebHA~vl=hk<ems?u*<RRuRCk>JU-u3h;tbII%cIne4Ft07Uk0kGf6m+DGNZ&DeZ%G*GK2=P)jX|ob!QYyxO>aa=*AkQKD9Fx18Ai3nVrG$*>TdYe7r5do&UBFwOA-hGh~LP+m1mr8QWg8EpoUe*F;)IqaOE)(^fDQP~J{h{`j3E3VF5salPmr)wLgAu=bC2?e}{d`OQ}tZ(@2hHSa6x@Z+uen10ny(1i_fC?i2uZ|>(t$a6cuueoP$RZZcIk)llVxTdn$6VV-aHF-;<`ABwzJ(sNnFFMMx#HzGv>6`~bKuCtiNu4;MqqhRgB{S_)JEn(fU<vMqD%t!7Xo{!($|!cgMY1;u#xNMmsy~XWmWf{`ibFz0RJw#Hj)-b?i$rU_$^#QAYE@BnON!bBKP@6Mt<cF2sUf5MK-X1wo}bBSpU)CE%o53;K%VAhqUdKf+Ux0}IB7#AhMm}GnWqeOCw07gw{-d5)L?iyl>kyDNDwpE9#yR4b7~X`a2}>TT6<qKmat4{46aye;T;F7Oj?8SExSBC$z<DAE?;FW&&^;y$7lQPBD3wM|NR5^HA^?cvj#v;Q8bO+Bd4f>?9(1Ga+l|C)+27$?oh+N*F0jV9x+|@h#5uUHa#6EzQ`le9nvU5`RBDBu?x4XE?)PDEYZ9n@X{MOJDz-e+BG(0*?+Zb>|DQjooj5b_(e|zgb(ExqyL)GAp2ZzuUSTv72iEQqJQn0r<Z)|hwg3ZQ7=)Or-MKWBB)yV+>-Bbe2V}DA55HJeqEiCt-`rZ$(86WLwZ4}k_&&V84_I->Xhwr2N)BHH=z#eu0eT&_m;ys%OuIa(YH(?B299Q5?`?oJjE=Y@fH_F%6x4fX!O~CsKluM|2{-w^oPp_bi~1asH|vo<_4Oz4>-Ko2Vn0u%NhZ?r){o2AYM2Co}?zYANhdPRe;oc_5rriKl1XA>Ce6neE1oKt!W*ah6rfkyH6}-`!)U$*gN2ZAa_2n{=R{>LxZ_6*ru@|AzfhjtWxm4<gpj{!>UHdu233K`h5&R6pRoM!~u(lWpwZ;0)LoDiT*(FAyqhfBjgP&)p7b1jw1!w_$0@XJm3|7xI0(StNk?9Yz$4@prnlz{Ri&-`qL;u&L{mThtA&aPo?#ipEe)a5B=NxDH_Jl7gbP?^b3F5yv3hN3iCDP#_CKv;%?|kF#|r*jh3gheUTf*|8Dp^;X}J+myaoVs6JFv!E}W?IZ$>8I*TRgL#HSb(Dx~jd|Q`K1<uKPmK#E~yYn+TT7XPVgiDhV;YcV+Rz7H#?+@Oy_pJP?Pm~q$*>7tG^|bd?|C??rth{IYZW$C|Nqehou=D*Q2O2SJ!<K*91h@S<iGo&aEi1;CWl$KgsVKGgTU-Qg^CMRl|Ap1Uf61zE0L;<s@oFgQ1{yAr%L>pd$m609CiS&3aV)kcxkf+vN<53<G~+Y~a-td4Oz+kc6)Q{?8i<D*>7|9P&fJ5VN!}BFwyZ=afma-4p+Qj=)S)5Y82K{xo>M-aVgO~~geuBTk_52`41i~${8mmBt0vD<(S)$0UMTt;2#jMLI=R=Dz1G{3vyTg?Lv_U9fjlx()?*)QtW-jgOp>er={<YlO1^ci>F3*ZgX5YbUe#^WvyPZY8|X%tc%0)U9*0c7+b7(yo9G@Y3)l83lVqX12^>u(sV<Ed_5ina!?%tkO5+^O@7`jJ@Zw42aXqEi`PB=P<fZov@D@PNcuc`r8ao4RY@Px-GB5PMVeNlUa{`MS68Ln+w`u=cCabalAt*zIg+2Ii$Ls#$Sz@gRuxham%=2o|8h>&n?mb05AdTC{^-9e8;A2eK)Iqq!gzcWegq3(by)7PmAs~#_q&&dufUpMpoa>HbagD)hUSD5X3`m!+i?!(xC2slx9N57M;AO?_fdIoAcn<y*EH>-}1>r^YCb(fs(hFNkBOc>Qm&4a{xLl-y6fH{hm|4J_F&Kk3)L14ihFGLE&0Gx?;kHNO<-1v|i=kpq$u4?or8HCJad^)G<D0(#8=d_4%b@2#4sbBGq0u%3cSdpF-${3O8rV-`5-SY;eexN{O~}C!I0Z_6II>Jsa5ctJAoWz%nkFDL01u4nk3>=t{TN-n{qcJ#G-9h~-{}Ye5PVz9ekyX^o=J;6>i9_|q`{=`2(VFV(8?>T)$aqbr75TQ9h(}gvz6?NwH4@WBp6Wx9ri2)Zja!QBQ5*hmGA0k$jQwD&ct%$+ancvJx6$$oB#keq&&ouu6~u`b}xt!!{_*c0IC}<-^b;x=K!j-M{<b$heW3uG&R2znmXfB`&Z<rY&RxqwI@3<h33b1LZoVl*b|pJSG(SVNEIA4NLKg)5#uW^HM|B6;}_7>V)9M|WRAS&m%j2*;GRA%DD@w*t#Hq<@$Ln?0c;&LeBZ%_ztN2xo~zb$9KOBW4T~UAlVT-K93GEWa6@#RMbhQ5JTMdz@BK5WE9Qu{wnc2}!sLe5Tf|{N<RW0~YryC^GcI;tU$toGF_`QRWSCbJnd?@VqDVbh4u;nGpHSyE7*2-Bp7<ikO?3~onsi!6l)j?M#L43Q)JL9pgMtW?!QLPsgcfPSSG;YXSp~?>*@gAIl1h>`8>a8;>cHjH+`p+Zf0dd{d^k%N??oHKJbIG7@_Evx<}thai_Wc+^7^2QG6(VEwAz#|vb;zzRXk6qN&A>ek~w(g_BP;MQ-`u<dbc#opouE?4bP}<XzJCu)OgL~&g1!EL1mlX_ZBCR@#BF%Lu);Um*#=~+lK#iq9A_@{_}AFK0!c(awlPJK!wxQvh4UO{3lWqL_V8UX-Z4`3jWhtoBjd<y6kR}ktyNfzOc0!7Rb+X^ADT3yV<-L`8j-4pEqnKpNFS*eDQ{u=LhBRo`t$(#PU(3G*39cp!jWSRfJ_I=))zrZ5DaV-HR%=<MRpXV{d2l<Y24sHX1p+bZNOtMXZQ{lLdh{>pjsus)uaq`pRVOv#~^xnetZb-{zuj<OUi-`yFV@r_Hg1myO&L4Tq^8cRkCQw^qZks!>~y5L7K0pLQ_L6vp0Ei73XL3*1;ajs2{LctKR0mO)@mxk~z#$^RB-M}jRvf{=NObRUc%%)Mk@y*z_)lfoyg+iH4zBVvZMIo4rg(DV`GK_M1TGJ9Ne16tmm*gUZGMt>*t>2~E?Th5+<t|uAizG8E6-c~{(j3{NnGm?0M#8qr$;7wH<<mi$Y^)~|&%%l{@pdzo)Jx)G-LG;h5BiS+@KKY4e$5$p7o>CQ`qtp<64MpZsrMsxp@A2_3)Nu;+P*Z4;7O%`lh{A;$V~RM0S8tonfAPxVPjytgzHKQ2WUmlF+t~5#=3M=XVB_wqGmmcK$-E4fp8JJ!-^PgI>Ky;0lb@MLY$To!I!srzcpHvHS*qz%i;tIcJ2^iy3y|`Kvu!E-ckf8%Atnz}C&236aEyIH=23P{&in_KDwmgxt2cC};6=0fq$F044!)s;4OFURJ*XJ6y#Z0XiI!t4dPB~A(E7`z8iO@vn5byo89PWAgQU$f>t;EbjV|AH6lp}c2Fwz%s6t{#)yx9<#mKgbz;;47_*xGd`OtQx{Rl=<3f72*Efo{QRkjiJ^iaY!KI`&q8si6uirjk2>9P9MQZFHSV<Q%!YP5EACF`IJPa^lXkq5;EAFI}-<khuRE$^9xsFutk!Gya!$FGtucH)JZ-<GVQ!^PA_BYWk+n@Z0L?HB&u(2`h4`G3BYd~LI4ZE8RU+yR>gNwgADlx3O7@zD6nP7cCk)7^?j^#xhN5KSJ<kn1MH6^+Q3lbig9aZa>&S`ra5z}#@{>-b@z5(d1!Xyjuhu*Si)+r-sFOHDn(#9=r!IHkadBYQJ&-pz7h-i1kxkv!C*e^ee_NiXdDgQincW$W%dwbTFuce(>{wxK5YHuHMN<u7K`w6P>~X73lTiQQ7KnPvqE+-@54gP6p06|;Mob*o)io<se1%43Nai*)++4ca6#>rJ#1P<b84Q?fqMl&{Y)iUumw)0>XDApTB^!-{j5L`?y)prk(5`ryU;?p@_>De>4}GeO3$Y~6wM@`0TBlsJGkqX+#$Kc;4sD5WHMe7{Ao+)0OV055f?;%L47WwAA&UX_IkV|h<m!#!@*gVE@L^T%h?kQ-e%qhML*KV#rHvjGgsr}icbVtvz8DeUf6N0Ug4edKd+92qON5$*+Y+$9JSOh<-F<0J7A{k2@wPm)H1wUGHs7WYaxN2Z;8u>{*A*E9$z>&DH~<E1m+iS#~{$Q=+dCUVxJ)0C^u$6}&ldE*>|CyJeF6^vwOvRh|Ff*_u25*qE$jjx{?|Csw9-SKCMloIL9L-IpvcD(D85IApse8B&9_dY+k{(<A!<@`w1ejtnchA(c*_dO6SSysUv!oWj0@*UoGQ{3i*l~8vN_;Qd&-{F<=sZSrQ6FEGX#L3OM(k1>S_g6^@ckuahoCU-oMU8%EA~(fGqMZsV*90A7sNHxCXu?mq^c}KD_km2XWh0+`lOmrD6+n4AdU~c2q}cvO^c>`Rrpa{S6lJ5%<-`-Xr^WMkhl(U6HiNzR;EXn_%FE&#6UVu4?_=fm3LEls=_6m1MGyWN{I5FH`yk<t@<FHt5%S>0O&Iv8vY2<)&?+I!d~VdA1Z#FV?0q?FPBizt{1dtCDt8IXTNzrUBTd8&sn3&9JtDouJO9KhaFe$rU=hpKk&v52>PEsS^LY)LY{-jSejh^W5L>h=|B`0DJj|mr6v%^Kya9fEMojLo#Ae1uYB8~wj-)p10Qg8`Y|J}pmy=f^*D<$-+9u?=&4hUJBwYq@6EYiZBB|Puq>T}ry2mrBREp%FveJeVfviIar-N_*vG;YK_KTYopS?p%Ld)AH?#+IpvLuL9H-_QRaP{6~;zi4yC{gGkNMwN=1P%{G_vY4hnKy=Eo824mko)1}+p-(~@o(VXkXrHjGJ-rTvA2oE9o{FTpdJ9la`f^Z(n?>2---js0hhE`Pax0{1E}Px7w}tS0Og%4n`FD?^NG-j`4YjF%PkyR`D7yS7XAJ+Zxxu!%gX>xw82&q;6DezAUVw%jt8H9>VE5`97s3N3NFU3JrVa;JTWAqN&rdbZe}7N#fEBIJoEh-P^Gws_7?sq-@>B4krH*=aFC3EkLMfIfJ6?&wm<m~w%AGM5QhdF+)z9RVN!{XG4FBgT-v%|Jokt{P7qxomH1BFUyMs)_>#xO>e_*WyZn7@!uB9$IbSK4@FL*6o5;*N%6?^j@8*W0a-pmf#0HWq15!4`4KmzVc8v$$2~LbSE8Hjn30IYozxOU={AGa;Pl$bGx}NS*@~hW9Zpq3YOClvwMpl0%sL2}L+eN^7#@1|eh@(o;=HMR*f@M*GI}uDEHCc*-1*i}uQDHOx<D_e#vbD6rNYb8>0itHOY!gRED*ejhKQI{LOl(6n<yk!}i2IZPW+*5*(>eB1CPd7+loV?uDVCY?A~A{Lnp`pcPlO;+G8CcSEc|QLYh|U~tN^f}|Mzt%*@QE-$jUZs!)-8CPH_KcOMIR!_aW&dIqXUY;G=1j{rg`_KqjEv2b~@X$lSva<fVE{UmbVZ*gbIFq>zi54jQaNq*?}dnRq@2B&eC#%9g9L*(kMVd<n@irW#!^V*CvRI|wLnk`9BehsrKUt)VKxzXp|=S+>w-V~*Im%B#YC#$S}lw_zeB^r6x#E)<tgi9q_40FFS-(;6-M76&8MEBK#yNBOgfgpE=;jmw$G@D-qhUD)XL%F-xk0X8}miK&ogE{!NyQqFs-w3P$2|LBFf<A|aYBDbS(L>t)C?u;<^?tWseOTz>1e>%B4t0`g!8pkfW?r~Gx+Zn&yrSR3s#;+mX2#H91_E*l>|KGj0((Erk;IH2WIESh!LG9e|1N&f2k}UBmehuaI5R4J$P~LDa&N=VzqU7Z!DaeO2sy92)=iH&xmhLGahrJiSQ%uiUJU}u1>oV8*XJ)I*-Tr*-9{Y?2t=a1D#bFTH6!+kX!cc5WDjkJwEN*A8h!=B|(e^`=qfz&IDMT$q8nYjlT}|b^?9oUxe&iB?tdH2BRMIPtvBPrd2%V2Ak|Yeq=QK$*O3|B27A!dQ2-2X<X}!u^QVEk5Yq021_93<mXsJkUq@%QI)QD+`S!J#K%o7`mN4p{OAgedDs6j-BrhOF1zEugeS|FFhzKtc&8;`gV8}bO2CH-0X%csDp7n`}eGiTIRm7S9KZGQF&3iGm#n`=6K*hPuFj^+8FNCuq5Bx5HoCDyt|N%*lb0nZ1dHdXBn)<O8$Bx<lEKn+WhRuPoOWV#3355bBk=zuwv^{G1YU{VrBo?o#VAxx-}C7Z3-T3wx1mE)a>SPdzm;#n66PDpbZe=dVhD2`wiZxdkm@e7tkqkT$bKz4uZf@gwY)BCeq7c2VEg)7Xk(~BH}=q5^BYQTm?>!A`nOpT1iH`cPh@Q5kauS-UA;r;x<)px57=Zu{@<hh%(P!B`^b<A!>1ioZUcM=Gz4<#*V%UxySn7E8nZB-cAvB_Wtw_p&@m5+F8n$!!ggk~yg#&Mb-h_z{zF2FO+PjDJ!KC!am8tb_clH`dze+jQ$zEbJT7rKg3Vhv^M|MjmM8f0clRa-9ivDVM3uw28~D}+g9YrLUwc96Vz2@@z3q_UQ(oW=+qn;s7!XNmxcDSS&FHnB8#J8};jKwcK9cTyCsML7}h4=LwlO4b&$1-GxVWMoE*;KWVhaNOXm|C>I*^1fcOj4%GVF~UX1{^|Eb>-~w<IaEd&Z`;1omPB(B#p+{hdWK^uLaAm#3MY&vx+WU>m(fbYkAoEw0hehhg&Em}R&395&Y*<rZ@!{2aToV3aen2My>vs>01l$bEiri-OB9I9!wwlE7KoGJ2dbQ1tV(>fhOcm1mXxgr{Ib*5TGX*y)7OMmqIQebs}t9Pk`xtt0bE8OIrNP)lUK{{iutWCP@H^ge^SL6PrYLo*^!S>`$XKmt77~7JITn)DXA|I!bPv4HKjU^nIHnGwoE*Qi!#0nkJItzW7hZ3!itJ}Y9d&xyZmjKzSK?Sed6QM>sfr!>I@tH_2NZee;=yaXg76d=Ys?ln>DMXYiX#TY1pKwj#7}3O@G_+>AerX@O(ba9-*spTBFNb=F^8bs#5E#R)Qk60Zq8>Lg>y>ZIoGc2@H0g|Jzu|7AL)}0IPRBpQiN5)UeD|YEXPfDOfU1@EMX0!10|)-<8*QoC7W)yeOeM60a(C?m9+8vj84)nM0Hewx!Pd(Wv&T{0@Qy8AL2|#h#!kmwdEMd?cpJzAE8uD5^}!FvXiz&l$bR;Q56NUdueVfpK)gKa_<dk*`>_JIW0#cIKSaFs_qBO-YEYzZah$VAT9>Km>mXmKJ->?=n4TKX6W5p2c5w|E_O-48^u>3$R*wC@mds$?7n_KTr+w-VZm_1iW>7@{dL-fKnPeQwX9grzGvy@?5s~JN+Gku+f{=WjMMc<t5ol#Onyzx0KWKR%!`q8Zt`AUL}|q_R-8GoAB9FOS3$S4g3_PIIZP<u3tnGiPs-c&VXjBv@UtrC@NOa%mWrdWNrvQ=4ZXc+AK@Pq3(Ik4cp>6xa?!5dP(HLg+HWjM{&?m4wPD3d;{6k5)~L>PhlqPgH=2;rvGK7wD**OASV}91=C1<OW24#%5GM3(?Wb!22+xS<!g5h?Shfng(QKRY8v8GrXeE6=lD6UK{chpOW3{^*(h*N!)u6wZ2HqIvNhCgR|FKzb4i1w0i^*Sdn=JBE3ZW)*l0C0%L-ePLJ4ZHj8TzfHcpyHbnJ><1&MA#k9q{@LIsnUG&6|`iFC~aOX83@(YlBec3D7h7md(OieelUNm4wn1vEXQ7WRU)#AUZHlrxE)5{&dl#zMq!PYxJ@q5fl*&dTwB3-OV}B7RD3+&fk=&*FUM+AL8{$x;)BCdT{p0Phovv)fR+R*P%=++m_{3$bblnI+@2P6s&KjOi)->AR{*mrYW3-JW@?qs}9nE)fl4-%w_?tlsaH5N7n79&3cGA9fH;Obz^bR=pksFN$0+PTZ>+T9(6&;~MeO#yt?)5D)eS!di<Lrot-`y%0DkZ#Y}!m1mB$lzZF6V8lz28ZX^xIT6%dN@yw9hDizt#K(dA&xDW^?8f{rKN~D8BZV3!JSBrG+EGSwd8j}cRohEkpxRbT_fEjlBw3n|Y7Wtw^uFPBC~sDMall5>R_9zf^?zXY=`LABM#%<vnp$gAoGP?A=;M+aNOd!JUgMk6y=72?BXnpjV_rJ-({_ai(lgw24AYs#_^KpqC2#)Q5}NKYn28n%9@-J$aCz@>!gZ%QX<l~V$u?W6b<nMpb|Ga9%r1&n|INFb>xLQRRdan<_eUn-3Y4_)&`5QSmCi+@R@Fj3bu!u=ADyt%d<CGXq|%m&X|L=yzoloZ?$T~k;##mlSnsQ*J4DjzRO=1z_sDw7baRD2X}ud%+a?3vyxxGfQR8xNx8YL<M2rYtQjhU1mi)ZZKwfj5@kTx3Y_UGx8wtluX1rx=+HpNfe1$)83cve`m4%!3t}E;72Ld49e?AakeV33liK|(Jr}8$DLRp>5_Hiu0tP~3h&$eOC+@?nh%2tyKS+e^+YeB7Jfy9E(HU*K{r=~8Y3IG!VW#D5(IMpy)mIg2)J_yn#4r|w0IhH>I27u$Vf|_ahm^=kQveH20WuEJNmIB1EF*5Pn$Faa8-mrX~H|&Fk1F$>)#miTyIjQ9e-2s|#u}H1>@_3OBb%iG4hpD#all&A#|Hy1L=DI3_e3<J)G>z>l@0Egi@3aLa022pHC#lvTR3TVa;$kHdsZdUGK!!506tLeAh~%e`V8dh5!NG?Qlv*78wA`r0SC(7L>Ws=;<$<GZC%PRtQ<dR0+@x{L%n^QkJh?%X4_GFUHO@ip^E!@uit10JiN8a<Go+~A`HFw{qb!!cY>TCAvtN2yEHjlnE@Bz<k`}Sd+Jp_c0(!HBGm`>)Z{ZAXs#&fB8>kE!hgfqKao={76*oM9q7}wxmw}Ag3s|Ue4rE4l+ObOe8p|}SylPQvMGT5%5Wj%)B%sgZC7@+d4EUQ^*>zHn^+y;K9N`WVo;?c|ks(Z6#4pA8oDY1+$yh+~*iX21=urJ{?;f*kuy5bRv(T$cns4?mAJ@5rSVj2i1JuN_Q-Au>%fwaKQXLJaWOK4s_-lPlx9~O4KBJ=g(#!0smr0YC=?F?&_!liGd~1KjxuE8@y^K(<B$|kMjg?qq`f=%Be553^4LE-QdlCM|hpU6M0z{NNC`L0MQI+o13Ux70QT1R5eniz#Q8gFoa)nMf(Z?Zmn&N4#(<kF;Au`fb4WWL}m4XQ0ImbcCT7r2IQg>5G9ar%*L5$Ca)U4e{hSb4AY6%c&omLrBwuTi|=QXZ~y$CF;#@n*3x|lWVjdN_>En@2)eG_%ZQ00As4-rS+L<_IGN8xqfMxF_(a_qrJfTVxDtglX^DnCIsj7$H7?VdBT`JB_iqv`h$0Kywu)-Ou*aciZAbOcfnMUWOHz(fshv}`)I9vT{+O^M1;jL11`a@c|=#-*M#2WSZZAhhYoaMXjex!l{4KsR*Fhj1K&%vQPa%?38HOIUG%j{<IG;9A(=v#g0QX5ZTyEFVlk%4I>_jb7tK4XxcKs3(Sc>WH^BJS<iv1h`xSZK$w8E~g0;{^ZDb!>jD<#h`($mm?X98_d^`3@!A(=&$0TO0x4O-igK4DqaDPj~Ben+eB%@JXl~MMOKNdH=gPeeotg2FSixSGGq7RUbhpRK#=k<^;6mKsRKi58giOFaKx4xV}uYkQJ4f%A!dUEWiAdwHSD5>B=9Vo-BB90oX$|!Rh`33KX0RmJS(nd8{&$f1;r_)_(L{iyq|}ego~KI$cKfjti4n7esaO6IMs2b+D6yZ6z>hISW5KcSXFPWW8w&;%<(HPfP~DDRK4WYruT<1waYxp^h~KGQC(Ze{8Z;nAdKAmk$7{pK;d>tw-Nss|Adx<U4rySqC8-zeZ{1+?UudAdOo#?L$x>yd@&~Arbq1j#ZT1$jO}&NRMgn)bWDKar)j!rxXz?J?*7+TI5IX8W=GbcBXjA<T*YR+GL>(>nP>~WculEwD)e1OTZAiGr}na}59Fi9iydo2sS-P1uMM#(Nl3^XVX=BO1z9*Zdg>dEF)bskU_x_AzyJ>RtAl>KNae?h5+;%$sQ)(Y9%{2|6-;be^jvvP<%5XXI#LIA+|!lEbj8ZH>H!83u6T>K<g-@%-ybMD`%Bkr`T)Pwn!ccv5oLXtuwz-F)axuy`=qkI`s#77%Kiam{UON#Fr(e85YK^=a^NO>PYapF{meNdAposnE^J;7-x2O!Vg!^mEUT}jPE04r27)HU#Eo@-!zP7$9vKj8R`6SAI>Dqz2471{QQ=Mr9enFlod;bRw2;eT56G?9sCMZ<O-kZ~%BRo;WzN{}i<+`ztWoVu)Q5cwL<Kv-e08cf%JtMuM;J1E=4(!j8I*FnK6{&i;BB0N_HfR2^HcM*r5KU<sr<Qu2jFtdUid1@I3cE@TY;&f6Z<%LT~&P7IP3(;Zy(zfO?Q<q-5S;>)(k=-xQ!R))e!oAk<)qU1j&~rGr}QG<MYOB5S``djd4}6Sj})uMv9_Nro|g8@kSR7w(E(+o`88vEXj~eZ@#MovgJ?*!lakIM|7hMRN})7R4|wvrz%MwB`@q^pC;_In;?J5*PoN(JFQO_%{IxRwKXU==BtWjY8Jn=0&wzLhG66IBJv7eu!oAuBMCr_ZCDhSbSOoAa*fYL<P|uC-?m}fAnav;j%ainm6o_2oiS~kN6enoI6=8`!;K;)JgA)rYpi<Ng<|~cekaBI;!oITzhhy&fP4z*PsRDcc$F=6t}%TH?t6xxP2wiQwUf<22I%_%eKhOlW4oji>6a_r2DsMxkf4jsY96I!(|}vjXUv%9%GU*iEX$51Ck+_BG9KH^g8&moXw1l>ADH+UGYyF53|Nf^!i~bAbbb~U1%uhQUZW!{Y$c)M*`A9ws~njD=A<)6Jm87_>%I0a0b)r?#(|-9P(Fbgromo0(c4T8Rnp6~@->F0hl}q;3L{v6m=KszL{-a1rkRK+*z=%8fh**Y0?>M}2E_6>&|EjsuDbU&0N*;5-dvnqj^gyc=U$$B^fmD)CUpa}G-8v6d;*M9G248slDEtOQiV<TsuCDr2<9nPrZ|ihmM44=B%C91I>&M=M^Ex@4(5w+!Upq=m?4uxOGsQ&y;x&deA|kH!^9uTq~+%f<vV6x(c+@2ygLuMPeUBR$H}I|*4G2gP`A0A8~lt*UeE$4m8x_z&aV)lE<SiaGZ?UlW}xSZwPcbYs_ZJhQm81=deEEZuUH}RI90@{fx#L4&yeELhl$Lko}mnuxBO`Sx|zCVVhNyE5bjym6-w}8q#DyllAXX5*1P#UqcI-N)H$6q5TmX-%$zkwgV4<Y)d_5?c(YB2>A(0VS2HaM7OPvV;>_X%@W*9wf1=427-WH^Hmqa$FWkfAK;;mCYzU$WDiPCn&+eGW9t#R9p2ZG7Aydex^t-2UQ(JH2G`PZ2MA=#2(KO4z9L?KI%NE1b*oJYYwTR!F=3am_aNKM)3+s%OK#YjKvQ7N(WPnqEv{EGj&~!lYWg-6PA&%wW=ka@EWTFZ>zVPSWUn^OU-$#G*M_8ra_~V!kBni3U&++>-9orJ90@YU5QgIC+5(sWbBOkZ;{h<O|<4$~DurojHu*2D_h9@mIsocEJcQ7|lr3vncDsC9N@CEJLIhKHkUmD<UMxa{+AV>6CLdsh_%y29rB9Px$91?{+dpFcLvOK^qj(QzuUbgN7sepU>g|5YPR38bSp@k|Zcm|*X=QHMT)7Z>e3C)@a7;?sGyQU3?j3@@gdM!{e3YVcc8vQM&Vu0vm!7H?EOVTxL${R*^{4+LWwDhqmnl%V`JNnq2Hx`WI8*)n@TRhJZ1O=K_X0#0KG>WX5V|7yvU3MK$2|=FmJ0Oy0F|D{e&SswVHq724-~-E`Ic@GLpodV`JV4(7(~@wT9pky4eIE`rCz=4*_L9l%S=8DhkfO#7$%s46$$`u!0Wre5>7JYFo~i9kV8Y_kz&b4jg(QKAf>dX)aG6}qqJ)3uoyM5ONEbKr7&9a4Gm$!o72|kjd}uh>xIsryuuE5y(%77o8k8_CZg0(tA8jm2c~u~LF}Kzj#@=Sa4%@Q6Nsy(X4-T`Q#pQ4Zw^t5)V3nE74N4ObB$u1`IlnjP%@JkgVH<8B4R5fK@?hH`s*RdCA%|{8#%T;UC9aA?jNJ`KW0EBZxiZ0`s>(BuC%nE3>lF9@whGLS^8lZ{6?UzO52kQxRqvTpJ)K~wVZ8)j2R|dM@CHmYYMwc)CgrSwg9v(&JgMzlYchM|Kbz;78B#qOX(l91yg$i?nNw|EN(Ng5<`<L9sgl=@7Zitej9C<ioJq1dKlTn*W6WDSw>W6rQ`z{V0p`Gq1rI|TZZqS<)#x&%9h4+<)o|AsO#6vhWgM{KL`)v)pmGd*MaPK@xEm|f4RJBC%$0b7(e5s23X^7}a0fJ;S{d~Db8e1-?Bv6@)Vtq(_sZf`gwU%hi_L08=^LvoN_6nDk1NtvjN~^@l@-No_=>Wk&#8Kx$2CQCZFzMsC@ZRBciS#&irxy!q!=Y7ySCaI9#m_Jy=sbT-!_cWR8!>m#0YUut0|^uYKl#9{s7TWi<E`0k5^eNSMwY0Kl0<xh&MfheKyr;I%Z?(izAmOGRcI-8n3DOgvGX7KAJrvp~iv!<iI!F(6Dl34)&Tc9Hwc-mr&Nt9s^%0xKvP)wZC`wvY`lq6EnYx-9RYz9Z$Hj7WElHRnO)_3DLfPo^#F<zx2m@TnpQ)BthX}F`+$TUKyQBrGVf%!Cn7J`BS~XmQ3dUByfrq4o801FPyxpn5q$qj|;zSHEYB7|2g+p$#(S148O`v#kgJZZsdD9V76*#5pr=(NKzW8!wn~{zf^+Fw84~miSZ%;!%0IN02h>dtnj>SiEd<<FOUxUgql-%;a;yN*4_+78Uoeo%P(ILEJ`oUa3@y&IPS6XUFF5kM}Jc@+Y$(Lx2F6@a7;L#>+9IM_(-B+OzNN{gd`v`(J8C^z#?Dd+=R}A=dV<-XMlsvz_z;x;iAz_Ma}@n@TLE^DOb-fJu90f)d?fj7HG$?0tOb#MidR)Iix?@p(WN5k}<Y08XMY!P4Jr*=T>Y2DM2u9f;u?^a0Pb7GXHRj@VIWon$l1+w*(R0hNQ26L~~qDV`a(skh8!k9Gzn+HoR$JNut`H(MpZTLI{m!*(SVUILg+o{3wS(r=fiy9l%mKp<6PIOgYIIs|W>eAJC93LdM8OBT3O<+gZm%;i^O;#jU(CAS*?PxU2@!fu?dT6z#O4R0Q}g3!W4-_R0xYa#ZcSFnUQDdP+jTkb5G9FOz|Ig_u*x>c9}N9BMCuLU3x*983)RwAru)JcW&TG!P2ms^3UthTYqawX_Y^9Ga1;wE|}q(whNPdZPlC$lw*e591%d!qsI#3bIo7i^4t>%Z2H?^efP#b)QMGk>!}CHg3;0Tt|k&4T99Kg4@!DzY$#|p+bP9^JLg$0ygZdF@I8o;zm+xmByd&(1>d+R^iQrIs@$l9OWDHCPuJKyUnkAAC92L-v|L-H1^oKRgVLr8-Bqj<YJu18y~@X%IBt-Wg2n-ax{uFxrX2|KOz%qx`jHV!j=H4@Kl+eLdAL;rBDrCNVpjX5-e33A=gyw*)Y0b%S!TlRKIgZdy?wg`X}P=tyhQ~`<73i>wIc7i0zqCxCv#Jqiw~!->jnWzDD6{L$xf+i!KJ3M~u9|@AQ>MsMlP4O%GD4l`2l0c2C6Of*#GWIGu9C2xv1Qdw733OKG0PJol=akw(VNn&Hhd{@%a~<ElUK)a0MCbzSoK&!2#_D)^pec^^a6AnUuPT)BzE9nolzL_-*@Zkt-|Imd1q$?3S3TtzrTFOtjfK<FxC>*6yujp3QQ4C)x55j&2iw={>G{6{UDD6IAX4{?x=*@iXdpsFUAVoC<xag@F}hBo72_D9ZAB!4H?3a<1<XXUFa-%3@P_v}~S&pmU+0)Wb9!-PA>%=}T~N0+y)oY&sXx2>_QYlvS$^EMsePnKnHtaqyfx)HuNjskl3_`Or6(1)}Ej`vVbV+$lFQsFadBDi7qu|JtYOw^DH3R9%kDUs1OlA9@Zzy5x2&mxnvo20Ru={|AjYk8~s<*iD@e?5P<8XN9f-!RsuMl)QARl2P_a0|GR?i`C+4h!-GyMdYU1LxX<lB943M{2Zd-<nafDR|z_Zit)2S>hI#-2K*jxt-<TkGMm#O(OJD0!*SvjJ7XzTK9{*moFZv;;DPd`XCsNcsn&v3}sc0Hcoex1%AAOCa>LBl$~*WTxiQ846Sh^)CJMR`xYeA*x3z-tPr^(w?yR6GE{CcTL}yS@AEAyvrS~#gwWPFQfJl>JLHGzP-N~pHoXok&Sod-_3lr6>vs1`mn`fedE&KX@r`58JGzlu4gI#<%XsLpG><4{fNBC=;<CHPh%v+%&d1o_xJ}TQ2=CV5%GaK{d7I;L{l!0g>oQTAuX$!&vRl+$F3Ry@Q8tK;+e~J<;2Y&$o_#K48Key>U(|Ae^6TPL3lv;<uB2;&v#}g2VjZzwHxclFMhmokkG`kg_0J#Q^~QInKs6R=*f86$`WJeXlglofIk0V7qOe2x;BKmLA+-nL8|f>sKu6wJGWg<N()sRL^(THZY&OU~G|<!t%auZZj`<XodSToJtR7HXRF@)dK~mcN+8^56Lr)OVYN`V`^(KiU3}qTD5lE!>)gpFC8+4M4+XG4|DeTai@K!nIJrjLziG%JubOCldlz1Y=g&Qrbf8u=xf;4#Db!*oh7N#yn@rfpxI>{|0!ZGJq1{9G*E0SucMgBd|5%(Q+wi^QO2qeNWHgw8?x*Z&1DaN?jATmS(6-#d9#2X8I@8~upSDSWXAn*OI!=<&6j2JCBGe2`^fI$+ZT<Q;TU-DOeWS0=wjPJPoIV?hdX7%9g2G&4^V^mL{<W@Aw))O$v3PNf4&g68F4{#IEL@jqhaIrfeMv31hpT|Hkd*K6vOUDzdMJZA$B7BeV@x*Uer<pAKVcUQhJUPQ00;Ib|Se;Q4;bQB9p~+cBM2!u9MJcOn&^Ymq9Vil)Y)*-NyD;9eu%{BofnS=806vL?ykuXQyg!YVl15f+@QlkvokC?)vX)->{&V2`zM^9UgxZk^Jdh+3n@foON;5c8cOinX5@puTMs#sOM=RTd3}-@oRHgt=G`@o0Zh}~g5KC0G0<8(w!3{mipGRG_(p{#>RFL!n4n%_~26~NXxRv^g73=LE^|S>KaaHG+n1nhqAbAa&w@M2Ly*Jju1CekB)u~#k2E6yC+F?qOlWK&ovP3|(Pk8u>{)h{FN}QQa{X||MUMo$g+m}wnfE5gBS3S`lh6Qn7{UugJx(E!K8R4=xNV&k7;L6zZ;^LReRYqTLNKRX9(?`<clqT@}q?*F*+tB1L7K!r{$f&+Qd84N9Dj8sy7z@{U{w1DB<>sGz*-{P*#QF51TWB-Qgml(0c>oHD^9aH4K_tAbOrOgM0>fU$v>>G8l8bMC`zaPdtNFUwEr5Qz<FM-mkzh-<KoJR!PBQkF1jC?i_f12-jwX=O9j}z50gHfXy;|_?NxIsq)~PQ>uP8~5gSzNPVVO2)%R;mWz)0*DR*l)R0;w+QH??;RV~4v#{7$5dX;NEy0<qc_BMk`Go){#9bW0X|fM8_dU9Kf*BLl2RRv#-}?5qbPrqa$ps-eC=8UPF^69RRS<46M+PNHGYLZgxTNQ0Ol3K=I-CQ6h<maL>`1%pq&@p5iJq$iK2o7iJGfFh@47NE=Gq!{<%1TxgRE2q@YurXQkF`8|#LTa?V8~{^6@M92dmhkG1LVTSo8S4SCP7XP=3zk*Rm8NNiPa{v{eW)sELVTL=Ep{U(rZzRt@9NKa(#Z;iQV!ynQ{{NI`I*U5aBx}8RKK2jY9^*?KeM1-+Ezi_I8|NANtZCcC8_K5ZzgqJk3wmpEQ%7qz>^a+&DAHhu$XZgBC72=xhOTM9wrY|oyrn_7z})f<Cm~x3!fgdX?3~DbqSwjCKY6|HkY+H4!?#H;T2J72a(GeV|`EMv!nLU%+@*CP|tWK2w55?a@9)t85dNrD=#&@KK*Ipv?UzB%Bf%t{Q65#Pj{pcJ<$|Lgy*PT-vKq04~*=hk<-H|-^0}3G$agA|3AhX4`GVK209H}27{tn+TVmvBkKnN?5mWvjV9{C3g&Jb?uMwG0D3ZAI1Pj(MFTzw+*54Dunm87gN=2%b(>oEuHrV~C*_@YngNc7TZ9=+{R&aM^nLjLhG*r>TXiMa&SCB~&|`kTY_%InP+)9zRfYcjS8++cx~YQN@w%xJNSC_qsKgbn>19n75c7NkO%-38D&gxjRaCS5Fddbqc2vT$qv8UEr{3043E?)F5<|0?l4d%M2FSCGl!<`|iO2A<x#YU9Ug}TLkPrxaF*BU79&Kh=L}f4>)Vb-^R$h$<N7HO84qsHaZ1GNhL|9iYr6}lTGQgerL{Po3Srz2n)Y&j0#5&=Cy*0f*R`T`ejU+N;e&=Go_drvr5npmfp&Y9d3w{zMWog2i%Cqoa<vyN|X{v(W5S)#l6az0n_*0s($WNk9*fjEHmD8xNTQI6mGNpu>PDI;b9(m=RS$^ZpAH5KztaDJ(|E0LgloFse(_QjRJO4Q6S@>UV-mscDFm;8&FW%`dh7rOn<EpvhTt^QGNYSA6G&l{2`!s$$dDS#)IL`UW>O9vk&f>2cw?+&wQxp4j9;onUna*jDB-J^Bl`jr)9!vIfx<Y{D$hG?LcV8^&gNn%PGm7W!SWzGgu~>9xB4YWB2DlE<xoHAsHEc*yCG>YPv7|uFkk81RN2Tha*?od*Bc_e%C$I}$C6CQ{h#d(QGxmmp4Rt(_$COej%7o=xx;hU?r$$IkGfgJb{ZPlbyyp-MBS{@Rq6oLES-;LJ^fHHmR!goZ*koh!fDk$%M4YgSxuQ#mXkx*rmz-@y#0oGbHXs`ds?3Jb5MtS8Sm4;Sn#$S8xeCEwvcy{>TO?C4>G6d6oC(Luv*4ZV8F)-SBP3%RJFR89Kc?q+ci2{6VO#kdf^7lUy@qWi!L}O1Y$dOh^b)X@t^&5Ap|$#&yua~A-A|I1D^RUmp<4M{0M&vdO*F@sUxwD&LWoX+1#ECsz*e#?H3PP`6|j|T<ZS`i(j=oWTaBT$Zmy%Xiqo3WTIniU%V`wYFkAi!%+~!YFk3<%z7?}oS^d5xu&uu_!?u3<f|&`Cwn-BFF=^Z3Qt@rZW@V1pI=^eyZlHOLBsW9T?_G{2<$aMfOmtv`6|lQB1IV$~B(-LI^qd-R9h)Lcqu(GiocX0Yx1gj&uB}FkUW~@q>8MY%u<usbAidY2PB~1h@zNXTL_*8;)`zuaR~d)gDnUx7gW2@VBFwI40LU#Fr!`UHAsES9Pd21Hvn2sj?M<;B6;c{>upD$rwcHP7%71^>s``u})Dz<iqhBwvi`+Hi9%LtMtc^r@B^Eaqm_Sl-Eyi+oEOC;kj~T3J4dP`68<oL&cFmZ?iqfm(f9#IYUst#RKLXgk*gdkCe_~KRsTBb^lVs#6f=Ov6I5Dc6=mr^wR0^O783iy!VX)EW7?QXC3e<gr6--Mu+pxc((G+FE6PJQ=*HCAt)xYv}URS2m#&sA~ln>sLJugF-lZ+G51O`)u#9JE$les9Z3?i*Gm0)IInQ?TvP1qOE-4!=o`Ea+n1Oev9xhvY$hW(4*0`5};A^(>x-qU*-D1-IbKRZ*_;lb`+GgIc5GiAHEyxWGiOqQ_{h9Kn8WEn;hF^$ux4)b`jOk!`CRJ~e+Incb?cxSSP{pDoYyozgS<%!|4PAD@BF=Jq&d!&n*U1+Cr%FBk!@?$_Nhsy*kXr0+1NM^ihvJ8~-2naX9$_LBHI(@7~{byz_pkJoIb6@%WH<7Ct+mMsIAOh<5oH$`DdPxLypTJy2xzimO>A>s@s+2<rNAjR0Q1+)=QSep)fK4E$LDYl&1e52!>AVP~(6}t2E8&`Ll;9DfFm!c_aU6xyU;r#;p5mr=aO<~>zj{~@j6SP(L@fc1o)GV<D0qBuWXIq>I8%JkD1dz2a>{g%&>?v<`dA$|Bu7y_q};dvV^x!Vy<h8|ugNY|eje3iJ9;!m-q+mOlv6)dlZC(|Fjsjh%bG`9Oy<oUUV^@ieun~GLN2<6UyIetEd1KgNyEx`b<C+v9u16q)H6+1&><Xy9*s!jNH}e(bIP6pS9-Zqt3er@+K5*`a2SmR3@6fA!?z_igc?O&bJLLdYJvzpj`jHmW?+c&)050!r}dQHDOqj5l7E>a`<R1zPb+)$YvzfliM=@PHPufdu!B%bsK5@~|C`TUf1tjHiFj~_AF5EsDg2PHmnRRwRu^{K|EODV1-0S(+_Z?oArOwk;ysl0U=@SJTMhz1q72i|0i;BDf6LVh*c2-E8X&+MHk473a7X#xg9(q!>{i<R<@J`_VF?uxO8nets$NY^rSsw}FmVqFOu!QDe952>)fxsuW8%ug#`KT8s1sJU;xD=W0iG@1d4&ljodqucj`S7Y6uA%v-@{`ROICjA2^PZdclMFumjG_K$EWc6j`&V`o(G=VctY9hfjKL>S$A0b4=V7T0RQTEC!o~yfM0<8Ia}u}(35B4wnOFiqJfL$0SShb_`S^;R&=DYZn1IYWV(}IE7rcHgH=tXX>uH`8rfadM7ui2422j(p<N)@pmhr{3Bs>!)hEqvV(1Z**sPLPK0IV8s+bA&-sCmNaBlrXk#=*O^Kw>yC(*QI2k98+`${)XdZnbE0P4FvfdG;-T#!{7fJ5}Irhy4@$0^uqFV)BmJ!k1aVmQW-Tj$B5tgAZVzGVcqt56>y=KMr`84Rccz)Cf+UGx=_L3;XJFQFm=Ld9)~2sD|@#8n2)sX!yTWG~AcYQv0kuXT7;L7Njmi|~Pl)Z7Z=V8+88^Nuuv$EM*$?SSjByraDuu5nO1dgJi0W`&z{JiJ*1&b_oBcK*Np%~z9%+*NKV7f;2woFd3)c5LIaQw`{${1UtF2Y%M%XY4jd(OnMcbXtRbmrSNlydWZe>u$nBB5R$)duVB+h@8qD?6=|EW7z&oijgB1f7wZYMCJ2?Yuk8pYfaSwpeNFeP~P;*t(Ex?H&mVrPDZ;dhs~CHQxt|%&pZ({2YyBpTq7+aRH6iqN5G`G|7>Bha=;?N>Sq7yOKtT%&LQpSQXX8qM^t}gNxcM?+EY+NqOwp+>fv$)l@}^9GYAhy>xADK%%j+F+h+G9c>z~*2Mz0nK?7PUH^^@~#wuTm6$QGXv{~6aaK6L5NCxIVX1~P4%>TNBdB6MsSVOV1Y8aJY#6F&H0ba_7DA~lM4F3f)HZK&Z+9SThM!qNzvIoB7>8Dk3#^k9if<4weHZ1iV7%TAcU+OvR7fKFZoRDr-a)2RUs8UVs9;%OZY|7<H#-X9ss_GcDRNy}1R%xt1%mQwL;6oaiG?rhsXy<1U^;2WMkBidBNc9FRPpn$a$>Uo7wEG=D{)&5ez#>C&`yodDQV!ER#6&P5sS)5n4lqtgzz5P5jMQE|o=G9)!lxy^yMvmM0MKx-JtZp=Ctnp`9ndZ-9tf1FJ(Id#EV#JbFUc)KB{1CepK%?7MStgR`G&Hdhg%K!^JurmG(}>y#9klecgyd5AjM9Xv+ByxwopG%dCcB$L|9X9k*x(f6I53n=+FYm$^r&Z5Lkrz5pqr--O&(J`hUJ=hBj9ocWRGasXU^A-9Isq+^_)|pB+eE6mQ~`s<G8z#m9jsGnE~gGWWf;Lc1i+(VC&jw)E7Ru59|LmeLXxTbZG8R{)a_@Oua@Rq|7is8}Id@&eL2Frj9c@ky>N8Znb3<)m?3dFYH>L!zxUGxV)rWouzwf*k!MM1WDvUWaO2_LWCB8D6n9eI;{n!BjD<x?cW`oOa2k&?(dp;fSqMBfeyJrv<D=G&RGbG}$}{tFdqV_@&7|js;$p;m?`K{SZ-Hxv2be-xkCBb7GOd#Quz5(miiNcnD1=lMCQ)>uSCiQ;YbmxKF$dzqF)bajEU~BA!EuE#epDPpNHu%aQHYcurD#ho9vUd=B*+(WGEpuy`jl{C-1BCOFxjIH7higi{{h9ZO3jiGig|<ZkY#CTz()OC*po`2RTm<x&F*WP1a)af^V5*`;P~V?IkOI(GK~(`jdz<XfaDkz0bfVQt&NkgzFIB8MHH>-k=F7gC@k2PfvFQCR^lVmt19&!_%_gs&(G(GTtw6opSoW+XOhwf3=553Zco=^hn`5&a<_DtmRY-DUCZy;N~|J36<gbg<O85$tc>*iP1m0l`1@Hv3kMTgyo#vcF8m4WM}|KUu#tUd$GH`od*tiL-^^Q>wFt4KEH1fKwF-gN6P;Koa{IzT4YiA)Ijo>fCHxO!CTznh*(YIMPLa?DDX;7Ijc(IKzxYG9#4(9`1?$X1x|g#f|SWKP76Zl0uZVST^t(>m{H3$WO7Y%BCJah_l`JA(t3sF*o=Z-pd{3R4Zx$y$!a4?mw?*vCC7xu~9GT+{8FYz<4#=+9Z+kQzatUgez{&rruO$!A-?VCi3rf9nsvVzcCf^C5~sEs;cIdgKc!PlgVDDmSI#6V8Pjka;14dDYU0gYp7-+_1$hjsd9+nHp_3&(1KsRe8i3YJWgElgfpNxu%q+f_P_LAZuy7^8h<@=BC&kW<x-BqTiH@h6w5@TPvJ_v@vK4T>8=xMqPw2#u3JhPoXV3N(TnxQqZ&roQL<r0pdJ&dMp*#zPHUQ5C7BWs@j*OVkGGv!#T+|K2TJf9^8g^J<bxujF|>FHBd4csA$U@sLl@P&NF9P}Hh{1Rj^c30;k<=iueD4cCk}_!3E<rQ#Qkf}qR6JOe~mdlzd+9|tY}*{e2~}|Ym&JOZQ7nyo6LT>rbN_=4HXMe0mPOOlmvv5OA`tJ#*}>q+8fTvTjZYw;i(V+@((BVqFD6ah*GTet&JO45gSmXj%rD){1^wjAPffbbN@ek?-FZUww?#g@t9*i)?AOh9{cR7I=Ali_4V~Nj*WCf5RGcnLPDYyfoMcZ0|(iFY>bG(cB}*=0YZ?ANdy52iO?a908Ju+90f#!J`iHZ3ASYsg@^`S#`k^yn2+_?k5lK=t{b1y(XRbiYpyxR9P=Ol`2X*LYIA8jrP6i^+Ch+6p14PFvpvG5>=8PY)NrWXGTqP#jBaZ=?uNhpBA|G@0E#z{Hzo1~Y_3+?W>|4f9!qv_wAs_Gro_hl5+v+8$BM@#?1O!ESI28`@meP{Ne5nH#oMQ_;w`!AYEzOuv;d0t+*z(zT{A)<;fIgF#gBxkxHZPPqp)0K_;3o|5X#4D^EE(t@^y4_u*mzn-Sa))4Bg8%8;NK6LT1iyr4h0I>eALQb<{u9BrP5FIR<I$oW;^P^G|io9+{+mIZ5L?Owv&(s!Y=K4wICIIdP0uY;jzfr0kyxS#o=Z;^R)7gPfkmT|h-6$sx&0&`LGl7LC30*(!VRL?l@#nowg!nD%kl*43tX$(xe=;ZpHZTgWrfOVYGA&KGSzMAalkHIu<~?iE{Wzn*tE^-tvl54zj=?l=4jxIm2!D7tGMhN}Mr)fWg4P)ss>>e!a7XjGJ6Lv9^*y#i3Wye^P%hrKs^L-QDHLec&wj0^CKxVHv@1JRtDbuEsVyb+~DD}Q<YUV+s~br0LBK2YvD66+Zy$m*QMn!EyGX47*wRWxiPZk0-}!5wv2{CLVg4#;{Kg4B}ry8%6qnuRBLTZlY{GME2xl7j0KbqZON6}{H4<>Uv<o%HzQ8v9Qw*aw_(#}riTH<IkI`}HOgpjHdU=bwFUN%sL8W$sy7(uGq|z7nd#yz%W=q6Gtt$p|a0Ev3n|Cg&e}a&tCP@u~rU_*5Oc0d+Q92ONQs(GhftdagH88m{5{d4j%CXO7k09iH3o86-6%iFvc<qV^7w#!oRw-(pkHq;=o$H~NTeB`p>R1{{gD{L{}Gk2_dpDnww*z6T|*@d~_%vGtI5SRv0j==A1OTCuGz2?Y^Vavm1KzNXtCHjTKH&RzpHbIZ0ITu_s}7h7Z$SV3q`VE70kl8**Oi5!84a<m%x9MOQ_2VrkhEA3+*4c#MRjX|}50~9C>JSHx0plM2?JH~Ja^nC4j8bn}GdDu6tA79f#m_}(OE+4NXk|;;ZoKrWBMy}LwYIG(jWMPd(k0Sr+Pd_htUX~uOCC>(N>`^*tCWU5%6ceGJ)K-YonB~m*$w=7FSCZ_I`Se&Y_p^ezP%vr7?IekiYB<{O<$LT=Fq^z_n<5mR%u~mYB)WkGzs4GcM<Ov~PAE1~t!kXta*F4*8Q^Ci3s1mT?sHZg{H~HqYa$#i2OJ!V%pE8#ffHS|BJ2E_>MywZCoqH!ao6hy3R<+K5s`=dj>1Cu$1PVE&q#bC86sc9HfR$-%wmYes=`yhLk1!ihN-oW3IuTG)VlD3MzN22^u|?m#sLHNd#5IIWSW9da8G~Abm!Fs7Gvryl+4w6sTjt{D3C{eVcdEN`2#j3LzhT6Jm1?A6u``hCRcEJKoykCm71sVmX$Q}397iV$2G3m=}pp9AAKX)k3G@@nWbSAc&rpQdRv7&!Oevwzy3F$%{zK}(>OtU8#?<<!gg+zq{s{ul&Lw-o&kC;(G)?Da{2dSv`M4%7hv+1`>``O@JPkouH<PPFkgf+n;Hb0M)KWGi}Van4rqx%$C*S~Zblvhr7a`11fvzeQ?X-1H=Rt5qblBw<C;m%my}I>NxfLl$6A|Q6V0Z)Q6|<S?ST6J`F6pe<EI&P5jNtnY!ud`_@?zMU$e^nH@?yh?R<&}aPBzK2>mg*9qTo!KA!Jv3wk`ZWyU?Zt(6=6d=8>Z14YU6O~Z4xwNS%)V$%SjySi)|xU-#Y8c=p+nbD*j9^ccR_=$OCsp-u*ZfnyswzWcTF7^uC*=jFBS;?}kwJ9d7?KR}aa>AyCEwo>CNMt%w)W+4h|M=a)Q+?oicVuo(N>|#TnJn$UJPSxzbSrI}V0vhDK*P~TMa!TPl&9S`{45$MN!75e;oj0086E<yYkrnyoWMf0U_=%8Vn~I>In%)dwW#C{#?^;2-4KYfev4ejYZ@ok*x3q4DGC_8{-`Qv3{`1!$O|t~GQ**Kt<7pES#b_|Xe;IUTuUhjqLJpYybYp6DYX|B05i0q6%iS=tQQRiGQu;l_J<lz4~6#qXPn?viwo^mDF#7#zx(>NuE==tsM7QYE+d@lBD_->VHOUEe@b7f))m?wFqK|~f)W?pSnet|pGtRx7`+G(2n}%z4JdNvGoL!P4Li0*YE^)^*|D{_aQE7bR@5c_>E~`oKgqL_JO{83tM=#yG^oRHvYt0Plqgoge}0Xual;p+e6e=`f$o&Lk<hChX1?49LVf`4#6A<9G3+zfdELQZv5h?O);aBF0SiK{@D2IbS`Ux>D-lEH+;hTv(QpCeGvqrWfjv~y|EJff^a*(3VPGRe%&WkQG+(s48TH(rPd=P%WTu&Q?UfZfPo36qo&Egz92U!U`{a`eT>tXnY-S~Bx@q;C&8=V!eA-uhKD`$0TMws~9^Uf#4ALRNsE&_l_o7GC1IRr+qB+{nKoyj^wx{&?2<59|Yc$vzuCiUTT*Lcb+}=Q*l#BoCvng56*k3$hfn=sHX0ATV`A~wGPoF8gGuzu3Xvca~C90>Ag+Mk2{?_EK2I&y_c5Pd9sTFX(*koZ*0vqpnBo8yZFS~X`QC-RHiix(V?0Hz)(xqrls7kaVEulNiNr2vF+=4q**T_r+(e}o8#BDSjZQ~k}2~RT;V7-#hsSp`U?$jKK8)WkU^sVx_q%~;J+rPpM$S(-Fvic*F(qBu=%3cwB&A^m@;~DgJgu6(Tw2BXK7Yd$Y<^bO@cd4Trb{J#!F;NtaJO8<qN69PL@BAi=Ub;p(FbzKDRi9HqAWy1+MCV;FR-qh=^S*$p)&5h&0{OUMXg365Ay^E4)2Ns1zjtKmon?YZM$AC@(pF1`_V%cXIWmKC%EM}XKJpd`c^^?&jC^Gjp~~}U+rW&5jy}|m&Z`a!2o?d=*@}OwdXf|1&6GFKpvNm@fwG^WDNFt}^YaZSbgHiv3of0^I;T+=)Ksbk>Nd~F=LGr4!^|uAv)UtCu%An4Pmv!FbDTr&xZy8PG6iibaiPK}SH-e<S0s#0fTDu1p`&kU?X}%NK1xk5Js!;25~f=)3bBOHaL1s$tgPD`W?z*hSudIxE*B1IIB?Sm{!bER-Fztxw0CUG_6odY;wZ?d=d35Ff(0(DgP)x}`6Fc=au!C0ZMi5+J<7agXz||FSN8D#*w;sWM5a;cQPZgAwrNz^xxB<T3Yx<=eWTJl`9?)97H%m<;@+Qc)R_`Vd)qfkN+ieHaN!c0&TsnmQi(*UcuYMfaEMP&iIEHxBk7i6B*+84oNrW5Nv>yUkoae*j~w}4vAV8lkO;^9)yk0k{DPERU!x|9msoho!<+a}i;=?3;>POlAoRTjpHQ{<9eKlPi(L%%18ak6Mu{T@RKs(y8}6u#6IhXLRkfwaH+8Ev0)@2R>U%*^lIqo3dGSU9-`i@&MPvdPjFBE5@JgWGkHN_8+?XPVzGKOOiCB9_6j-2y$&Mc+k?}hUpX+lY%hD_3CE+gJg)oUvx>2wb(d%ccUkvSmP{B{QKl4Dt#s}sp9-B7Q|KG&#h}82CjwdFIp0t`bi1V=LWp9xN!eM_fOXf}(+A2JpOyZ54maw}gRf|&%>SFmV_h!JjH`1GxMRzBvnX`ScW0ct*B`;1j6QxKzptqeR4*O7cnY%aA6A#Bvu(j=JvnEu!nE-lAVRvj~<dKC-^pU=S`IkqD%HcNF(D)1z)F)W2a(iLi5#8{p{Nl@*SX^xLFY-`{hIPOt?hk=6Ev)a5?gLQaMKQp~=DWVutp@o?yeo-^3Km=Kr9is#pC+Si4R_dtEA`AH({LI+BwH=<LC$qMzh|0VPyDSB*UU!oo&U#)GQPuys*<bjx7Y-sx$|%H*|MvAB-?|=ra^nCHgD$Ox!}J=K45-hePqfbKX~uIZFG>(?7j8-xoj=sz+ZWnszC$e(Wz>Xli0gu$>0bXj{N()N38_~YKa4yn<7nh0p^0<eOh#2_yA(AcY|b1g*=4DUE2A!Cf5N?7oS7;UC!9k#pXXQ_xug=_WaFyJ!xSK&aDvu(La@0LoB=c{N#2uBXMBieN#4SR8-ob?Tl!%N~Y?FPiU~P;Qn;}gsqsPLk1zCThoPW7yB?0f~Bt<{he*XFpSqKXX1)#S(r!k_s4Je`yW(#<w-B^%{zE`3+q&!dm+d0;iOmWy{UQ3)H_x(Shy~|vU#cW3e@KPeY`Hc(!N}Jr9P8hiI#qK;XO#N-1#}&@pX#7_|V^fMcgCyzBG5C;zpU#Ea|?uVNq(LHyako)&7>2vs5_09PZJ|q9%~LY+=4r!=fF7>4eX9a|~qkYENM&k~ooXVRicn`dFu&OLG(4TR{}6qb!K-AJK1a0N0wyg?tT&X1`)HH;>^@emUmvSZ%$)|My9D?Ie7Pq-doXVVP!8bthrJIr*1fNRolYZpPpn>YnB0e&YYe8GM7qv|=QMDCy;fHWg4E&8kt;G5&9|iNlj61sD`nV~l7uT&WG6U(XaT&zEM9hM%A!RP|FGG|pMTys_Hv>Q<jB8mI>M^5KV>hz-BFW-Nz45=REfgtOtNvAvtougR^P?tlPgsoVj_J5U?_f|+7V>goIr3{@Sj-+?4(-J^HFU)+IElqV>5TY(!0DAUd14;RDlxFXK)KnIZQ)jJT}Z@<qXWg=9mpA{+9UszTs6+>QJq%?;A2dq=3S)DT6s8jk|b;?mF>I0T4J%NLN$V!#}!?QCBrWJh7pP5#qGaSSQKpi7e5a2cuDQph~Be~QmyTwhYTc3;@6`}~Eo)7J~jS|alhjItyoX|DEN}gcdd9jVU)jbs|mD}RR5DiRok+aGQ<<_o>l@4SO25Q=vH>GW_ytq0n=A_aSZE$J%Fei1!ssdO5QM!0G989PG$_@*G2G3@SODYcgsjslY|A%=7)mxXo$#~RK!mFiTR<!A}cX6Mue?@8bE+!!<Df5L}*}1k8i!S(msVV4Bd!$qN_CaKE09k2+gw&jSZbJv-y(_F81JS-mv8|IOd58!rL=$SB;0S0^2WfTCri#aTs~Qxab?6xBW%6Kh06s}N;XC6IX8&}A2bHHrp@03W3ss`H2>f(uYR>-Q_n)z$m*{Dxpa%@au^JfP98E40@mFis>hqs^3cE`s!I6Cn9WFZo@*vqMuEi4N3Wa)ZzNlZQ{)L>G;~y%QZ$x%RZ4X~R;r{<f7IsBZ4r*cV6&LaY{wB0<N<SK+VR$l!%Fy0klzMMPJKVIRDn&(!k2@6DTkI!^SWk8a9-b4bXlnJ|t9W&<t)b~mb%dM9tSqqdhbq=R>x)(V99C9X?E4dzvz)jLdU0hcJ}8hLMgKwNrM)-)^KjrvhDri;gumm`5}V+u=mhv;XyxAsdIkxB5!dYb-u|z?3sUen3#ZQ%#vXNV#uCHXhHSpz@2!qN*f+y0w?38z4^#QT#IOf4mbv?B4bP8-{VaGkekOyxo+xEjBM6AMqs>8Ds4TKfxMM1=LI7bULikTRfAcu-{2->JTqYVWxou}X;{2A)<*IuQ^?cR+5G<XC=+gH<8e+FUUp;*oBv=t?u<0R8ktZqCMXUJc$gGa){;MO!e!T1Mt2=?VAX8=D5Zl&wkw7K-l<e8a%J=BU=yvJ(IKsTMrTRim#XTn{2mcwrhArV2+_*k4hM<kK!JHDE;k)b}n6n5K&EMuHxkZV|b*A2uU-m7%U}JeT+WY){zN`m^NBCWAD`r&utL!g!B)O|E!j=eN1q}idga_V~9kpX~YmcelaS$376nY*c?reiVN+E$}H|-W#_OqB~`ys4OORvSe>QYlZ%4_jWmHf<WaYJ~IYTZ=Y0GzT@i6eN#AF==>@b1jR5XA3_A`%d-25x6xv${$S$DWE4*n_PoI1fBbUL!FVYIAF3sZ3P`5_o#rGv@IKo$$PVfUh>`GoaP^hKjd2s5Uiw2lRFH?5BzXX;OU>58xt5u(5gl&^6IEVe&BrVWD=#g-F{(dktS)HKoWiSvW!j5QHp{;9X^gE+8+;5YCFM649$s4M$;0)pll<Os22_G}fp8->R$jQ2Cnf&g~Yl0N#adl<ZV!9w7YGV=1%kS525B2M@G8%J(9{8*NGZgjt?U1ky=;anoq=hK!v#pF+{X?W5~Q1D~k!E1e9@l?KUdP7x(YEAtnrE+Ic?O>}z&QDiJ}0$=NBT{J29d<5DE(~GZI+{$T}MtpkWN82JZE*cF6ldM#gd{lCQn%fw16{BU7Bp=x@R|J_1QbRm<D+*C+xDuB4oOALglq=DN$x=B(n8O$Uz({NE;uSmhjWv##Fs1pFBxp$$@$*;eN?FLWkEn|qq&26ibJtgCKeWLW^U3+w(LpOupV_#zz*PKXUdVp-(T&u!)whk*Of0NPSEXN=_ngos!iK41yGiOZ+A2kEmAb;!%m3Czo`&+nqcb`Ri%Hxh{D#{jYeaM3j!jsiL>no3)OBPZY4k^r$&?Zk1bQeCCj!#S_C3SawRGC1iUR5<c@R%E(jQa`HYm&FtTErz-JL&1qj4N)_zdclltWtXCw}b%3?zFvbBN|M2US+<)3}<F?KHF$DzedKO*s{S%504J#7aqwo0yBi#@=-?-UJ1#1cRH8cVF$wR&%ulB8Ze_Rlf)?$S>QW4arEkxC4+fk(Lkyny`Kxa~|0<6LJgr7UhoZ`<~E69qMfv^)!xpfDTjMypQToY=#j?Z4`&asOKTAjckYENt@!GfnnxvC}@Z^+3JG~*BV_<jtXD4;-&~vhWP{<%9M#TL|#(PTBRt9K|LVep1kYt*;U%WFiX1s`6BNbgk$561BJ%&apuxcfBZv5hG5!6O46~d-Y=s;97oQ&%^WlQav1@*8jLg2%f5^U_i#g$zu*Jw9~i9_ANe;_!{@^uN#D=AU!+@yah~DDcSC*`xwdU+fB6GG+K|U$RZT-OKGcbV_1DAX6OVJ?;~Zc9IJcLNb5Qua@<b1A7DQ{(f-W9s7T2yl&V=WWk8^wNaTa%`{h1Ft_Ppg@k9M3z)3X^Fs@dbrN!haQznGV^E+5m|<p6X4Sn)mwF7DpU7JN0EqdoN(YJb|R>+Ivb8u_Rkotm>DtfCagya5~b;*5<_W54v_2k#|Iyss{U;$rSzS?D!uudemnl%LI4Kd$&li_WHOnorsGe7*|e6U%&UEGEdt<>}?8Rm=Nd`Kr<Y)KF5joVb_TVM+reC13+zO#`nP9IZ2Aqt4dDtTS>p@YP;PmVtOG3$&Wt5YDr~-ZQukM`A{%3`>n;e<DL58S9n8b)L149m>Q6Wz6RB_o`oCRQ-ThW8v?!koUJ3oljWNLuoI5$Ag=XGV`gDC<><78<g1gCi+j_J3&L-Kjhm(D$|iLUqYf(7HlbUl17OGniGgjz8605gtev^B7|NTuV59oM5$|R>JNBX@2FJFIhhO%m`~EsdJo)tw@22ENp4dJ0a55^*rixaNW$?#y!wn%)l&iNFqNY<^uP`Btir+6X=S~IEz4ND4wK-gxq<-I$B$@2eJU7PbNOaP@>d}~@sCv-h>ZYOm51EdP$m`#Igi9@)YBiovFb8pD)OL)6DKo!xhckc9NMA_^N6}K%#pPdXY(zvyVfSTk_MKby!7XyH%sc>j=RX97H(w!E21x|5EaZ|AZJu7`aWPz$)HC=<^AWonZ2)iIWi##elwtg*h(<SLnYchpeh@V)rqww!2W=Srzi@0b3X>@L{vKR{CXgPB(da2=vqKAk2sA76);#GU+dy}5;2?sh`e-vBzvSrXFqvO?_K=lQM>6CV^4z95t=&#e+-lhVM8H(f{`b0*_!BV)e@7sfl*2F@|KX|yNP#<aC?Rg#xOQB+pdy_4)^1D5L@C&26+}liW4)43xH?acHt%2IZDw>%NvdMDm<7wrZDMDO$d)Qzv3`9gPog~3%nOW&6SfhMK5n=*XoP2BB3Mb?ToUdqX)KCiIA1FCH>&AI*;bkOMm7#H%2bUl#EGfr8wDf(^$ugbuf332He{a7hcc{^V*;sw5l9rGpLB=M~7#AV`E+k;A_wUQKFo4qmrZX4xE`N%X?xp3{t<^nd&wTvB&<9v%Z0-Z>2snN~n0dztw07?p!D&fBUbzivnrM#6;~j$&0(#JmXXD9BQUPSO>G?t~vq-*vxmu6k1|fHa~yTg&+ArUXMFf+VV5@37?E33)dXvy~o;|Gl)IS*Cn$|A0MsLPRL2b!#xx$>y_cR0?~eeXRw)^G*34s%K{jC%~~N%5hA6XRyAj0Bdus3x7f1Ql|3}{9x|aaHkLK<G5m5wKul>U%t>J6zz#_(h9qsD2g5ES9^@l;rUkCn8_M<Q{jzomTrlNe@{C$h!-W=$cAn<=p6J{dp~R?N2W#hQZ#X0w#O<Q7EF?nYiCKx6teyO8a4^`nNv2sA$1=39Xk=aKxlwPY35?eHv%bOl*q@pR5<f|N^NNDZN9cvjuqcdfO=u2iL<|gS?VX%7CV~W76Au+!b9c6$qp!#Y9~wMuHMB-Yl)#w&3UiPA&Dx50s-JfZ<LJ1r&}!PSs@EDeLoRQ;fy{jNF{t|<qfsU{(KkC`PAkg2Q7jW5hfM4fq(;8A-#`Z!_n{$zfsY~@ESv?gL!N?C&rVyy${IoirtFGk+l~S1vln^-v=H}8=~ip62%C(VX=C#LE2$G*(hmI%>vKvur$<!(+odntb5#F@>T&}0IQ5<d?T03QjbyeSJAfUh3PC*u*Hf_rjs;oxtH{28?TVkN<U*poE3dXX2l_7+-*dK(TBEY)?iF8AMtalEb(8C8H0Y(R5qzan50P#JkY5Q)2S;y63@NA6rYrbuvMoMDkQ*zl=Yd*7b$x0z#(AqT`n%3xn6ImW<o@4<@5=j{vx5Ou(~W6csIp6|=G$|&?XFB%TQH^RSea9@awTSaS0=A3lb7Yw%8lO_?;eqT5)=Iv>I6zpipQWgud;gPU=c60eAzM$+WWO~0oUf5EpAs$t`)6&(qoX+$3RMVG@Vn-M_1HOy;3<fPHfgh4un={S3aU)5*&z%E{25k2UfD{gm|fx&C8!~H%cyWtQcC(SRGee=%$LYd)28OmH><APwlrAY#*BQshtOJv)9(!rKOky_#AE3jP-#;Tm_A35_ZoMIt@@J0cAqbhR@T4euG_AJf36GL$nH{Z{rkmlgJ{Pq-lgux)ssv0HRTU7?lBG)D-K@0(WM3xkBdBL?kaYw>g*&12Zg&AOTwA;VZC8G(D;DpsY{}gJR|}lKD|<J8L2gRI}urWd!^pCr6MOFxc!NehsJ+|KE#gKXcAceLf?ua3chg>MkUmBq%u9EtmCr#{7wHiOdNuHMrpe`8;#lPdcOhIK%2JX+H&@E7}iXGt?9--c_UQ+sOPOlvNs!ZLos~tGk5sxG+<b8O+sy2$b9I%iU8Hpn;{vPS|T-+?VCIK4Ssx%z)Y0e(`xkpsr}g%{`bKhFv<Q%+%p}PR}Bze+C(<=kcy^f$}BXu^1KWX^u<fGe2j8`^u;Je_j3g3HT7+K%P>C3U`M!hV<i7C(X}o6Vf-Fs#u9NWK7|~w$oZ=P@?R$-c+#UTLHAS<$@LHd>UEqtQp(b78R5Q>n5e!1RwBq;}4;F$ltU+C)0FB#5${QXu%QX(#yBVq!pjC-=R3suZ&S&TNObzx!49!=f{86VqJz1aAO<#*35Xh{lW4b$-~b(Q1+J{=n>2=vC;wm$X!wJjIfeF<%7k?$PKGfjL9i2b;GG~%RPxmK`Jg(k{yb)4y<<3${?ZW+W7(&Re^-btWyda%PwDAwnBW?W)8TTD6E#Vp<cDx)2Wz*;zX@7^nZ727Q|0ywW=K2cERmXovL~N5ztq%Y@rZf#ix~6jmFCrjL#Sb3B{p&ge}x6U<a4y#im6C4)bDb&4DsCn2ChS9s_o66gQ<8;VUyKqWG(S%QhpX3BBGTYa)$!Vn*yLIS_$AZK!GkSaQCY<Tvx0mUBlYYoKT-27v}YpsbEq=JXcBZ3KNK_}ATS`Nn_^1As#{Q?6lpnN$ABk{|HlKp+L_Uoi*3DGfxuz+5Fie@!6fm!$d}PixwOG7&Zbhnjnl$`t9X21L^isZV%aTE*iu92_~vg&-xMym03u9)tMhaW#-t#<P;%ar<}QF+X}T^{;PkSKnveZ&k07@rRP`*O1vR&D)uMj-~qxlRBpOmfttC{C;$(V=_(FGotqBP{-1<vs_;;wC(7JtCDF^V0cNcPYj@kOJdF+q6J%3T=5z5rjuQ7u@@KcmDoRYCo96pN@lNr!cZj{j!znDtk9z>|3i_@$Ddz#i?1snf}UBQB5L${eTofdm8gPBROE1l@^!q8pQ}VgA}}rA+5X3)<Ui$~J{1Q%$cv>ie<WC~5%a&SOtme-0R%^fk_|O9)gE8j^7pZb)KaTMg$IbLM*ulI)M_Xka-<p#eWvi_%Adg-)ymU{JNQy%kv-Gi;sut!-})ed;JJ0H=f#2=h|eo^tM$yS@=D#x=z5FNRWKp5DG*Qrwc+Nt(RRN+v#NAK(iX8i|6YriCst7B5EKg<@zlBb*23A0Q6M~KQaM(#PUJPFRJ<uUo_fG~HW32z4j|($cJujmKzi5N)1H{oHpIjpB8&Kys!_!cg&%R4^zpDw6Q0$XlaE;fzMA{VzwumIloOJdhJEigm_c>(K+`4}u3Eo24127k+&ieo9EO9`YAOjt=G<*1YwDVPezxsa=081_kWA(T7zltvsCUW_UEe`u&m+2`wK%N(eI!|wFWvz{>JLLD-Nbz7`?dc^R|x(PZt;2-J#p7CYm`V>e)r}yemZ`H<5CT$0VTl?UQh}C_0EDttjw7`7?R$)*BjQY!(AZ50`n!Djrza$R8Sbb^PXa*Y69(83~ZM=`(YHp441ljP}^Iv7vstQ=tK%*Yq@YxBUMtpl}pT-jiEbm>+IFaSB!Pm!Na@imcsf({|&O6D7|ymq4_+IOksMpHN|$*o^2+_v7ZbmYR4U6q^f>v`&2ek`QojNJM&FrbMej}yy3*9p6}PzkkW|t4yNA=U#(a$FvXTFPo?;ZY1~)ca;VvIILqN8jfUgR&~0gAv$Pnl&0^S<>|LSz(q-7hyjavQu=^Omo9hAm!ev-Kj7sK$#Z1p}Q!1|N?4U>v2G=Zy8$B;kD6+l4JdIn0E1nArHt~9rzjd#j#<`yxeaDg8Z(${j%Q&&!=jA(2H6#efM8LwRGTM-__wYu_h%gb4Ti>?~+O#K!3fNY?VUhLCe>cApPDr&K7IE^#0P9t7#n&InKkg+rW?VxEoZjo;_{6RFq9|kW_@OXJPqu1w1XOeaLgd%11o6(<9qhMIl)J}qHex`tq~`EIdzqJqqTQpv_K68DcGdKEP(O>yb~1W8`H?>ic^h>_uRQ!D&9<d{w|Md?kY65tJoz*lWfnEd*kZi#*z++q!H33rL$&$X@sU<UupUj}WpN^ujLnbwdE=vAU)!!JQOm>9)B+F5?UZOG#<n4_tX`h*FwfQ6<+EMQGPah_Dl<0!!<eygi{bu{cb}d>X+C>;3IHhAo|@Cs!{j(!)wpQci<x_<bkJdu>S>&17S0?~FxM8#Q=lX!yve2+8j5y+4Dh@wZWu%uH8xcZ35cm0m-CbzV|63znZovLo)(~jRD)hHPkCLMs%nq26hR$qw5S`6B+F0G@es_*iU>p|=JQ^S<pUf|Rq`ASi*VnSrAHv7`RY@D9f}D5sZGhBu7;!IbNE<N>lG+-s9j&_`@qE9$uBtPsmnk)GaW`X_A*h5q24*uA1J~%09g$vl%^FEkYM?dvuc9j*;?lcQ?Eo!Dhe{+tzyBF1+`bkh*{^Eh5C0+c{i$AlhufHgN|vPln!S3u2E?iH*59IX-^z`=}{F8g`P8or`NU<1=m#mr}i_e_FKfhT6xW2PC$2nbhGTX1}sTZcdObT={7wuXLE8DADLh!1BMRD-}xZxAY#pjuU~W%aq~GP3}O|kxF}(`No}W672^tGVT?6FI{uJ&wlz^S%{YrSshax4O*O`vr%D*%X8ocmhSE`KE|^b?l`&pcG0xV+RJHzxe@*<~|KUv8YA#>REM?<@SW>nEW^Zq%Y++mq$!$hatF}5@D0McQwn06SF>yoLqpRL2aYNnDdQTe*wJyzSYyN7!raD0>vK>mww#sv}u|1<-PRyD81h}o7m^Le$*PWHW^FiQW><2#r|9UZMv1dwnrGCJm8J}4{AcsZ*2II2GDM^EgxfGer$~cw~WR|ilAxQR1&_2z|u!MX~-Jfd{v%3oRieSC1YVj2~Ypg<GRS9i`O#DQ0nGty$mvS`)i;(kxGtYPKv_x@r1=!%9m$<cGhs5odCtZ{`P<Cs#5V;6!cbIT{{+dtYZ9F{yQ9A62M)BN|9k{(t)lUp){T^Ldy{SH}wem{&z`uo}q~D{|7KS~?wGKVUeuo`s<%=ZLsSa#NqjQKLkN|}EW-A9**fi%)r?!6R?<&=6lsz5viL%lo6}7nFsihru(uryXY(S(oo77NRdHUz8ZTXW3P&;c{`(!#0(*Cg4D3UmR^blyK9ZVxfpQ|oWYt3wZgl38(5Uu}bs{g>%N4Nc>c<gi5x*N)PheERZX*Wpn?t#3nhpM~FIW!6)yPW1dRQr5TVy)kv@Jg{n@TXI?A^|I3;kTi4gnti2rVRRuU7OTbcq=OUM+d2@NyHsEl@^7bn1~@qLFXQay=QMIl7M#a4AQnc;Q^?5lKE7>wWo|Ntcy^P%ApF$`o02v?U#%Q*M;~^K!pZz+oHf-a4sWUiqG1&jbjFJDYo4adL(}p&}$sTe%z1jFVnTRP2ry9sZgCvxgrkcg8^b>G~SBFi5RMral_<dI25899`U2NAy5lXf{oon>^L9xTavswn$*g`Pl?6to5;=(Pfj(F2Y%vxK7o_UuGFkzom;w{p7I)r@;do|-#%JDr4@qqkkfUryI`ga=`SX!@Nsh;IX(T6yUhRx?Zo{oM(^)@C=mU7EoWavB}{F|OGv`CTDDZ%FTe<oRk0)aBl9IFSQXnW2}%R<i7NJUQOENVwkyfJY=a9Jfd(Y1V!QJ~Hgc%hZf{oUA`nfwsaC}v=)bK(_VyWt?AKQ={%h|d-?j&?_{#L$IC0FntJYGi(QG2ci#dt9>b7L-oy1xvZ@8JGAgIk!a07g76mjbbIS!V$LlPdo^Ejq~WAe))mcb@m=(y3)6+lnSP59|8ble0s^@h!l6yjWHx*Lgnspd9^Zw8sx;$^Wbz|9VC!#Ql&0U>Qmb0?h59X*Kwurv|Yzu<cKniJ<=y|S!)2DnyPQ+O`mx@tCQDG6~Gd~FMgmr?<%aabm>&>-OND<iy;Q*9JmTS_#9_w0ITU#**e)B<Rk>RYZ6?MaHZ$YxBL><tdMuhfH3`y+1}Lb&(EZG~MJb)WAsYaZkmb5J5}!iT_z?lmzzS18cDeQ^uHL_g7`u;BQFiJ}xCIXn0H^`*8dfrAI$#vSXFWN5d4_Pq&;i-=ByV!E(z#6lzQMxu|yqnhGrp($QWhg-2rDkXxR{J~zU@s^84kyMK{Rc3|79wt%ip)%BN=+0%uw-U7`<^zzI&Lrt?DU0vOTQ%x9rvtjr9Tt~WpHs)tK$}XTV~>m7>Q#Qyc9Xz0kP(OKK(o2{*WV>hKB@42HBMr1Mn4Tis>h_Qw~UkFMx1O*oQ$(LNj33&WDz$lPDV=bjo^5|;+chB#z|OD2oMhh=@=(#xCV$Aq(Z8zO@kaD_%JA7n&mO|%y`Fw1xz;uOv;dtkazY8^3~LdWGo#VJUN&}zFYhF)%St!fB8yhQ@$18$Gl`hc`|hi$Gk@hRBg}al;jO6CSKFDO3tiVeVETI^O{4Pb!Wb;i^=8bznU)Qms}}`t#_;)+x&`*0=>5eQEwWm2(}HUn71i5&98QxU)+;8FDAEDdq8_`X4Qrq%Sx%iElUmUZItONXLY}_&|huy+yOztfbx=HUFSc=HxF@j?|NFNVysTsb^X*Qcxbn+U*}!@D#WJx1`Ra7E6ZbNf<rlg=g2s4#r|%?c)K-JFSg!$<M&61n&Od$<KRJzSfE(<dARn1n4;A5t^CG&FIw7)O%?&u>A8r$%^>7g(dZ1L5`(lQ@*f&<Tczn(xzB~L-)P-d1%viCQpq3H8KFn+X`n-SebUh*sWYvUx>hA0f><^$$T$FvS2xLI2wbrQz<m6<_W(L`Qsr{tZrPdBx-F)sis4~ew9mzSwj?`RFL<;$@N#b(Wqi0wOTmTIKVQ^bv_u2`kDI(ER|>W@J@#~YLm6f*-DEO8FtYCCNB0H=69C{Om~=EwlzII^$!Crf<6Ua}9n`&m5la;F+5gM$4Zycn7`YfrsIb1%SW-v2jOBbFkw~pP2@@(K5Y-ohsm_Hl?$O2rW0`LSX+L2k+!lyt9%c?IN3_Lh>{)_nC_zPXhK*}HAJ;rVL(xmiuP-C|tM7kA$+5|wJRjF6P110EXhCz@a5&Lb40XR8U5Ju#bfXPzb7N?srD;ZB0n`WPlZdZu+ntXthqj5<f2>>9ggR^^j*_E@kiX66oF8zCOUSejSk0Vi_dUm(HpeIWrX{L=LA~EpI7Ev?4tgZwHJEhbr24hWKmLm!`VPeT9Y`GhLg}3ke9eI$fv9yEcz<KyoB6;G;;v}aD+pH?QyPfbk&%?Izhfm6k->(UOr>?z^~y}-7*XA6XoHPwcL;e2U3r_w{R+d0D=Hda`#<?%hp=CaU%WAXVLpB}2XB~-T%@vf8N5i7jtE8f5)Cw2#~{Ff3X3}y)aqt>@WZyMsnUszh$_*E+LU!ur8~?&QL-$K_WrJ=T3~tP!_U7z6m(wuIbf>`{PSgNwx(goo|}7<J4F-BPfalH%k{|TRdqFc<TrrYsNy?YnK=0xpep7=*iahGMv(?tHPe0!WGJg?)NmqP^c^i(p}h@#p1@ik0U-X=FfrV5lXx^bXX1_stb+}sY2|tX;B#uU|917azLaO(8At!R1*7rx!v$a8T9BT6cga4FaW-M&TC<$J$nafZ@YliWwwS%85j_|yt*MsnNM-xPXG9aRq&(Ne4kO9hnlGW3PF_@Ba>h-IRtqNM8|`aTOefX4rmPe_XsXghVk0t@PbqRcxB8FXkYXX-nE*fy0RU=asz$8d1C>vx2jExiU6J|^J%Cw}*Wj#DDviR6^`+BJA5Y2yRI)i1lREX*+&omTEE0fx_jkUWpW>GXFP;U2XM-05RG|&Om=m!^jmzbfq@bxY+LF&n)`;7Xa=c0jN|pCB(u8Oz^35?s;|Mg0OBe?mAA~$zkw$69NjkBljI4PHF{+m!dnvqW&w8IfWnUT-#Rt20hOG~^cCnbSy}>xpUU6G=fe!?3&)|$E{McM}#WhJs#(#f_XnehS`ma@g0rC*FMAtrJk0}4!pgFtO>a?af@Bx0iuv$VfQcNco?5k7fa(D=<2>(4FO(2tfr~C~qBz*b0^T)vbo^(CQb}OQL0KB&bT!5Boe$kIa8iOAEx0W}5DAP)UJ%}EIVH`KqLvBf(dC1djOVv{z@KegDnh6EceJFh&Nx=uf@lBArGAqu|?oKUf{S_jV6dBSXj6QUcSBkROR=-4!I<%o(Sy@#3Z2$K^NI2*qIUZDW99Jl2MT>BdN-VIV_beQwpnWI80Yym-w?&(UDIC;=F+Iit9jb%_v75nMs7z~9Yht<<5mu5(qFam*hvPcMVz|YE(aO(LR489eq6LPUmyz-#BXXuS<f^wq1pAE9JrxubJ(mRPDEv$#q0%WjIJwIT<Q1v~C?8P`eGm$K>CT(~iB>cxFrwgRNwLE<EXl7L6A(NV+tqZ*qy}VUEOWhbjmu5u*B^X!yEdIot?_v?8a{CsGkX2<866-(VmO=-MqskZ*LmbPqxKik4P|QA*QRzF!L(&+*P}K7=k<K03-e{pyLy2OTTJSBWu+^s0OO=y&S=?W<d@a68O^>Jslqm+iBfSFe3Q=KsaV@u3*I+|3p<p#+&(&&#VC9I>HH@bi{JxSz`WY8FBZXLPV3{tVa%8uI9hpLAF;xxJG;;EC@dAe$(Q{N=|fADl0-E$fVNKSo!Fw*-3(}Oe=a>vm=pTiq+{9d^hDkVEN6)dpy@=02)l4SO>Q0Wf3h5{xxk^kiarDiU@6D<H-`JklP7UqZloD=VBCq~3<eMHEJ}_<cHuVga9F7aTtGH}U_AQ#n|k_12uOJTuW!C=ubV%=tZQvB6I!OZJ11rY%RP>S-dmY2_u~iz&TKt9G$WTlP;G!)di_@CK+v5rbpqEaJHB$wx@^08Xm^dv*>cZSh0Sc+)exB6o~5%i5sq&Dgr6ZlZ|}K$=*ts+PsfH7W;h$6cbv47AR33R%eep2vz=6RXY3O)-W55&K+2AU*|wlpjP~~a5qt1iFXn6UV1MR*Ai+E8l?1nPVTgXH5%fY38PxRzTn#N2tfP;AtPMk;<bjU^om5v0r8%QpHFzBJ_C3#?bpQ)zsN=w%mx?+03HY(Gs>9VvjYQ}oHC5apy@GT)HFwQ^xW?L{KHC@c%hNmzEPj50C4_}Vf~DA<gRs<q#{_~tUqHP87t%1F{sL=>Z;AN9p#U+hw5mEMy|?@|@=(E!Mh1W1<P|eWt2+_SJa~DwA!_s<&&?O?0gHYbN(Bi|VZMY0aYy-4fCQmC2KJae%g&G(!qc<C_Fd4$NHROha#Acx)OGuIw9XDpI=Q{9*|d}l%@)d3_~tEDh$Vd|Ws)!WBqVClfq)bNT5QR%`e`ClQy}%8l&KZ4z5=1eFM1Cl7xgd$8MF~9`ri+R^)^8zSN%A<myYoRCtSzx<0GrjxDN@0VbsOTi@aWZQa=Ch`D%@t1fCn+1uc9Bih%6^Gh$eCl~AyhV#ey6w~%@B_(hP*LVh4I&8ZQXx0{A}^O*JKf!I!u6hH1mJXrt0qW^{#de78AWbNNV|Ayhde!T8xdVf<ISY#0K0?KlSI6^fh0Yo_w_=P(u1Kq64&fI4veaJv|CVhx<FboVR_+2bZlYGOO$fbIzd+5!+wC3jy0WVl69tM*;+?Vo3Eb@&Pa)-9V#pX2F+K|F^#luo}3)m>HkR%LbVlFUpg^y(d#NJe04fw%?@DbfZIaK+%?qSXZB9R9?a?UGRn=4v}+*6&^KiUh$!$>W$JHL?hjIYwO&ma2tet4^O(S13#F)_GjgyVQdI2NmgTbI>{CywWQ7GJ=`QZs^7%M~Q?O)B77ZqwWn!|-MQZ`?dLdJ3HBVR$KWt9TbV@d=4AXDurA$icx=$uZ85Cryx_(6lSRlI?U9%=-F(Px6QU`>;yixb!Xhfxzv#m`Ln!-JEg6qPViLSrNA11eW}Yh!HJVX`EVxEq4o~%=$y+XWyF|P(rpY{Fx95e#?6WN(i<P8#aY=EY3*_!=;!hMqfZ#bwy~R)bdCRj`ukevrGV59rSIaOsg|lJMv9D`^aq+qZiMOcq{A5e<J5SxSheAB=Tf>YNk<62PpPfOHm2ZcP6B>bM{b30@BU_=d&uT1+40kb}zCvskt@IuSCZW5nSL?Aa@S7#a_jVjxs1ax!(DrKHL1c>d!l#%EI*`U@{s(X7A(CnThZw-?tRmcaK7klK5d<YGjrVtQI`5A(W4K6okj^i6lcP;gXaZj6_fI`%Y!pLr#t9b<Rrc##DOonwC6}9$i=m5a<SLC4_4NcBF|qt1?HFxU@ipE&s_WBI?e0^bZGbMk|rt)V8-uv}2URJht8}yEOout>ER03np)YjE9CvLUgLJ`4xZcCA8`!lE)-imPuxw0uLkRj5Tu$WXFTc`?EOJkQq0B_q{Cy7kSON96ZraOy(|lz8qX421`HDYPL*VNBs%bwo&0?WItOG0&Po1#_cF{If>ezQEz)5<Vw$G-mnq%mPOjpqJ5-=_cN)Kw2+{9s%Nt#-F9-Ag7*#XnapnLYQYBYpTWCbi+2mtlq&BDH;s8dpK-z$&6{hq@K+|_x={bY2T5LPh^H-j3-6q~uqM&<SCW_YEO~J%jb5}GowF3i6QQ5xt;RB2$6Tf#a~XM4UnDa1St6tM0<?5-dfH2z&D{1}ka0O@&4uk2CAR>U6bCAvy;t>B?=^aEOPVLjek~1)mA1^932AI21VU>Y0)0G^a*<fl$~p<#M>+{G6Z<*=vh#=j-ybgKrmHQ5f<D{`HP#dW$HgpODdswJ$Q%ldM7el-E$p@<En{@`K2OKN*pUfU5gINX>~StL@(xQ`j`l|6#llcDIoe70fT#|M5`<B`5uDi~dhkTs{A?}{MlY`x>39HdtMn7x_^e<$&twqBaNKJ<xt&XlVhnq=(38YDED)#1195P@JB!6vqHz0FMdA2Qx^WhJ)<t|ZykRyJo;{;arqSLu5c8QT<P9fvzYNf!+IKTnYR&m*#8kz*YU|9@4=6EBb64#vb<RrFWX@By#I0=oW1+3m_pPH0XiLlDK2!$yVUkE9D-(TIFQ7_OM7CuBM+CX~+^HU8)~3q)WHX0{%y9==%+<y~PcK5llUcaW`P7p8nkO35)z*~y1ujD6amRmwGmiN6(p(m@Tt<RSV4<YR52aA9mxjlHEHfnOb+g%G>PAJV!BrOz(}E={MDdI$%Q0b9v?9INlrCn5J@T2$pGz8u7k5(+ox!Vwo)`tak<R-fd16kBp397r!%<zNbAr=$m|Z;*`&qs!JQ04nR|5)pW7!vj)j|Znh-4CCv3U8^PC4R@0)WV%*BL?=^M3)>(jRa`FP9=bZSj4p>RkR9`D2@Z{QY-dnZ7E8`|HxE4b{afKF-&rO)46u8J1AJuMwc(mOfUaK<ZVElf&#uQY|Rz9&#ZOhH503Go7Oi>D7eFTYupec5Bh^T34wURFYRN1yBm@$EWK+?TtFnc2)%H3SYX$OuU^_(TdFnEka)dv6K9vfA-lVVNBcae2Q?;A6;80xM(tcg06_DzrE~>BkB$9!BkVd9C$6d(J(o`>s}j$;(kmpcYByRnwF%YEQBq1I#q+SytU|1077bR$zlF`e7_f^_9O)gI{}KI(c+Zi6z#-V=CYB``4hs5dCv8bkSzuyoaDWk56KkUu_tc#N;M5M^ilCrK=*e-0<p9cY{c-JH}-qE3bo`dQ$#<szxv)7#juQ}u(cS)e&!FA)78ZFpmAbwKh7xTHXXG)GKv|ESuXH$8aL9a#8SzuXsq96_U#3Qcg84gZZnEiBV7{?E;?}<>BIy1BomjI1CPhc6PUnW&^;jF=CVXKm6{cT-`7hDu|0byW;^+q{|?-*e*(UwXepZ9K0m!dX|D5hxu$fBXKe3#S2wPP*SO11QO%J~r@TdEGqIEZC>30^rFHV2;X<(Uu+~Np0vl$BJET@jFc%q2eNR>(pQ2Q?TdP1possVn70C@`Qj1JU*A~SPK2COUuqd%N4CH_Z`VFy&TCuUs)E+qib<Vk;j#2`I<-{9DHTgU-uzrZdiDhCh9ZG8S>6t7z$hEc<jJu#{Y*_@3=<oqe2`)uGfl7Mmbczn?$j@~$L&eP1MYTINxg|{XTh$LHv!N%vvG2nGZX2AYnnN)u;T7*t0<7wtere|C17<oWanU!*&&G;{uqbb7Z<Oa^b<C7bPMlnw1gnT<Umn$wWW^de(#98gC-AK+sRq|YR4EqMYB};GIxSMNA}S44Gs8}dUwicb00-K6?So9l$w|7ayjY4XiFATk8Ese+tf72*u-9Ym48fe9?KtM>JAQS^oTf37fp=bt;?BzsUS(W68r$;xM3eoR{gqc#qtq(fE`6vg=Rfn_o_;LfIG|ej%IWL);=YnQF&rA~Emw{_edEh9+u60Bf2gcl81ILs(&`xHQq5#&mxKR*Uj2p}Mu1p;#fe)g>u;kxKaBCbLwO!F9#;IL04NX!gNYV``J2j|YV99|!B<FDatHz?qyv0Pup&`HF)9!<S0&Dy8=U}-bYsgYW20M#E;cnWnfSD|-{-4uD>j*ZLscal8O1n{QagFJk&_4DkAzjDp&NVtE8UNYh~NREvMN7Xg!@q{21l(yETh$1HU3F%U(v1?D2$qWkO)<YDmI)}nqTA5P!gv=D{aGa>PJgagVAA^Bm3XLphBN`b{dEr^YUS(9~)+ifSdfcQUQZIAZI-)W`QC7%G~M<8gW;w&afwd+gTHuw=(7qFaRQwkMhfru{Sz21}lvEhR#9x_&KqZ>DyqgK=2Q!SqQ|2fZlM-CnA^KZBB6qw8jV%^Btdu#M7ziBT#dz%?5}6q^;_~9^=-gGGcd~@B(Ud`EL$Lqu>gZ47_SG9hCt8p+$b<-@+Wo3RpyhMjHk+jFHT>E#`u712wjj*eG`q|Lg>i5QTQd(?c5u&q1pmRUP^!ug?HAQrf9X8;e}s?|$$Gd~@y`GId;F9&)XQ4f){GaWVZ;9BQ%O3S%dRm(GIW1yM$nV36L<dhn@ixz=vVs3vb#)_2E_%h-e8Oih<!?nMx3qUDI;<LgQ6v?;mQ0v~^)^^%rbt}r(ha;1#jTMfG_0^r7&A^sq+E}+u2fWxh9Uhm8!FED&G#kVA^&k^wF6$GMX=0YO=>rl7;%agCrCk(}(S!ex0S`T#vbYN2wnYQZQGS0KxnFn&8_gfomR<@98sP@dRhXeQjM2e!YwncNQk4Q1Fk-Do?i(`6hEz`InAHf+&HNQaEcWnMk)n&)xPs`hnf*1p8{<jhFkJvc!EGh~sVKNRp)QUKwns7QHiB_sCI0<xt*4Nco7rIdDRKWRRf}sD%gtDU&l*9%@wCZ9VtUgWcz8o_oT?Y^J)@#wO<O3;i*2ZbwqSq!gGEpOvGkd8=5s~XLNjpF?#}740D|lqu?$DX7hJ;v|KDI{i&=8S^X#qpUIvUOY#eC1}+ST7f@`u&<4a5eqme#gR?B@ZiCu%%_C~P2#3Q-KO1XdQ>RIO@k!9r)qik!^(O<+R`s0^%CD>p*5QYeXwUYS2*RoQCHe16DT`p%M`&)Bwg<G<uPZ+}|lSI+;$%rzjGJH7^>i-DYMoG_$3_!eMSRdClg{MuT-w=D<Hr?CMdK=6zpG%3xSsQ5k@ElTC1mMVudEDWsSNS&MNMLMw>!fgcINxq%K5}7E)iraO(*e<6J;w%t*WPj?$YgF+vk*tvq_}@Ib=v=Hg$q<a#)ZcNrIdJpkrmCLU?D4FsN8{Vb#*i&EL`SKxM^IlN(n7deG)`UV?qgTlNqh;5(OBV&1+c}n+Hsdrlp`tY&(<hsTwe1F#b`u36y?YwtPKpWQ)+;nJbEyyQ-^p}Ig*{se2{Y`?Sk~u4$IM8i4IqI)FXpGmcOBxQ#vP+-FYEfN0u<47A9=(dnHFXeOS^^YUcAE$G5s2mjujRQ=Y*2=Z9pys$i}hm2t=f3gQr9W(GhIOK5*_A>xy_v`2~*Nxmn-7!p$>5yZL$4*33o6U2xhthe7Ge0@%M2A<*p6}Us^51m~sEB26l802&i{WraaLj@E}x(D&yf(h;*x}lKb{|Fm-&M4C1E|2KZ((DJ`hl6fZ0~MhMN0H!spSB`Rs^JoclOr`7eCnF2LHTGq$n+6efoI#h1D1D5=eiw$@~yWf#Sxequcs_-tPHzWvEUxnp0(Z22o<EkDg1@vK-B)))6bsKM`q97sEx2A+dkZu>7k+Oq`om1mB9rC6;hh5O1LIABQ>wOXv}a(`2b5}h9U{ptmP}Ycak=Op&;sBIk1kO?+hfHBuSrF-HsUyYcHW~ToX~B%^$InK_8bv--{qrv8NlN96uYms)UsbTOwWJh-zv4p(YsjAUjs++~h?A*>J>iEs~c!OeZ-Mm4L_6<d?q>MJ{1^E8N?z1ifHF9^-xJSc?oDgX)-3^FFL)+`ZEskPZTG!n%@kwQd5}1ZMzgZi(9!7owO`<*-GbjGb#FV>z!I?aau~yyP1MvlZ27+M-62OpQiSmylC&oXyNU-#6c^LVkc(QgEi4$|)kxDz_r2(S;`E4u#8L_KGu28loE8Kle4f0}<G`8+TxPZTR&(kWzx??06HHX6`)MkI8Bs(5e9yYkCse{3NW<DjF5+VNS`hug&;QE<?dv-*E9%^r%HG9*L6#%1B>I`<zBjHw1_e7K)GY$_>G9e&$QwkjR3nP8PT29(I~7MQ&nC@0Aji^1>50b}Lx+3OQr+GgTWyJt+$1sM0X^SMxk-@&%f?V>nw#f70Z&7K;x7M==e{UPH6snv!chr*%gu&cLpC8Ou$+^PS{LY%B+zxdR<h(AE`kMD3oVI8(dHuWWzm72`TX9fNwA$LXnv9%m7qIq5i+B_GCc&WwnWJ3nHU7flLc%_tvs7F96I142rPC(J!kLrNYY$r|!)4tJph5RLj!#ybzTFWccACE9o<5Q|zXiih@Jf6w#vj;Ou_r6ZfQX*uL)v)03h(U<mfLUQWcv%#LPom?;1L~e9923yPLnw!u~8Em{4^V>_2u%3@}(Q8sgDG5r5<M4h)({8F8#EP}VuIB!E-E8?}qCFq)wrF2ret%y5f;mv$Go0O5!)Kv|KtHiYIT6J0(F{;+6Gz(Y$?duAe5m}0@=8pGK+dk>eoOs$o>0f)1}e)nQg^7`Rra#s9_7oU8BYSuwZTRZdkpIr>Xr9ZTN3_6Kt0rrlXW{1VypIf+*eDor#5(vxI%dxu_I%|g!Qg>9Zn3GG;dZ&e1hIsw>MFFxkGAg%_~f`lN*X}5_4dyTzjI>HoT(z@Wx`R4z9vqxm9Lo(W6vX#xnbZ?a=cw(Nmt(-&IjH_C2OCHRDQ+eXH85`5Fs-l(Vix5!8I+_pa<zL$QkAsHVXtpQ!lS@#Mp<QG-s&cg4*)KY%MT`W(61#Cb|I-Ki<vviJrpq4stjxv{tMHGT$vo7BO&x9w3BBb3Dos(^x!&DUZN9D}_~|D5on5?nV1X<k)H1P_v~uo}C{^~_~l7qtfk$U{v?74#a`$%Qqd4xbrz1xteXSGJI2v`-IIBN1~I*Y83(F`+b2gm)Chjit1bh+g!g^=+gaYK|~J^DNiy9LD|;)VkU?ytm1vt+jmls1$TDaW7$mN>v9em{H$Tw5?z-Kme2ru&6yaJVI*PanBUe$>d!Ge{1=Of^5K=W{!Msnad<<#($fp7U=U85P+bWpK3e3ue1e~AbPsT1M{G_Ynq>M_XchdQ3&1{1WXUJN(s<q+S)^om+b{YX5lb@%3sb)!kkosuzutY7Eb3e?`MzTl^`ML8rG}yAi;T>b1pwTTTI!UW7VZfoS$y6AX!~uiGxi6m_G^5!)^jLw8CZkE^)0y!iS-)2jo6TzcvOAY8yN!Sj7aj_Hy1v(O}a;3plU=nU~I<)F0QY-N~**{=|+^hV7L69Mv_doHZe}k*a(uCPk7{DAXZ-CB~T~H?oQ)TN}WLA%~RS68sZ2?Kppm<11yl+0|oMAsdNW4N`27TntMq(P+L_QOAsxy1bV<uN)RoR*<T4U`3K;8MKi2d{uprzK{#z(XePQK%r_Q@cJxeeE*9|15Ct%&{H%Y%WdEDwr|R9PrB`}m5=$EfmF4E<Q>~7js>}~KS0>8-<2D_s(91Hj>VkC67NizCErpg)DOrXda5i62V(zqtOJQ>!9V3GmT&dWIIq6#$v_OgZ~bOn<*mey^S<s7IR{RY9U&;FnGy=OkuAy_KM*TR*$2)zr^EVYAjT_lx~;7EljwuE$vL1*EmWG$H-T+eT6g)@G8T5P^6P)lRJQn0T{Rl1(Y`tR{l_2Q?Z=Pf`JsROIKm%C_~QtF{PE)mzsryQz5M83{ND7Ezorjy&R_b+uPA@`I7>g!kN*6x>HU3B`Z%yJd2f95#}~c#56{4Q_oaUH@9D?%>>uU7=Vm|7&q_aze|0bTaq+!-*7q?vJ5-}@p7XUT@4EWStAD-y)nES_lPfTE!=pQMA0swp^euAJ_vO8;RtGD>p8YcpCI7`_M$A<Ib_IZJl^OC@*cK9wgf+4N`Z&R3O&+nDWa#Mi$s*ag^7_V1t^yf8RWfA&Hs<Ub^RVPq1R|e<kj2JTu$RsM8P&><1$t+MsAlovBIz@G<Lw{yL6tv0!t8riT)O2E-0a8T&d=XpJAda!s@V8FMte(wf!zWXqpL9caU58gL!F(TId#m3bUp&*#45{MOdm_9dU>AHk&P%&<m8;4tzon7;@RnG0!)|S&o4n|esOmSr0vGw+hlm;ZjL9(Zo0s=R$IIis<p9xi8m>D7US%DqW1ZT5^$S;_4X&8-t?RDqrd#q{A=ZJ|LN>q?e&*EeKa>a!`YdSKl*NQMb+|UkALFjS6|M-UppC_V7JeI{Oj^s{N)v0JzKy0(QtKVFKA~!F7K)SRkQEytm<n1d!r=qX!^#@-r`+#d602BJvP)jrC5!B9q-ZjN?M-kdvC*aIVW!)Tm+}b-{}3zj%mB*@yNB!uJMwqXvC^%G{W`483(N@Z!a7tS6%(;=U;7c!Jihe_5XIkacL=5x|v9JeonF*Af1KYKmg+;K?)n1*rJA|wfSoSZ%A&(eXP3Z`xP)$z2H*$&s&ooNRb$K(LRWm7|7>(*ui_L;Z*t2=n7rV3)RwB#^fxLf_~qMXNR7Fw?`Q-!_aQkSYZGLCWTDlS~M3l@1;GVUaKSfPBE!>250xR=|edwDR^A@8#am619DAiw!%}JiwU|{6wvi1I~IyRfw*Ih(U2)pILLvOxJj<b0<_zQ5vHJCLr5ktq0}OX`{wP_&0vAqSxvehZ?(i4ynLK62)yK&40wjC=#gkpnvSSbc_)%|yZKp=FI|}$C!r6y2+YWrLx`zihKlY}2whA)0kK>p+d~{mC%=gyoRG{8u^M)UN&w#Rh`EsXWDgBNToIjA0Ki(_d0<K*U?g?sTF7PcYDG^D=FtE!Q;IfzD=M$IWQw=44vU1YML!HxB7ovvpK@eZ6RozY0kWjhEyAC8!g+c_s<xMzDWz!eu3$YkHN<OkFKz@EIXI>4II-Wa@{2}&^j#5yx#IjasiY5XN&X&|;^+%TlX<0HN*Vz*BU$v(lj;c#InyER`fHl#a#_5ki4F)E+nM2-Cc2-=N6a<R8Jn8IVyfq6j1|coMHWsjA0}Wls;$g*i(DC&=cyN&uu8pD5)~vug*cKtwwAd$N%|HYiAh*)xD=Li{v_mpE4By{P2bHVanJN{C%JTLZ&Eel_2trk(_my&%6aje9raEQoR22j{8Aq^(c-2F3n<K7^w1XvHK-A3wgyolihbHr?}Wywj<8f2RhfMnu>l*Qu=s2(Xm{g;ttmb3{aQ+kC-7q&X??BG(_2n7csyg%cJen}(6&Y2=avf^No}ES7wm?kw5%5vXc)cK%mQunKg;KQXk~%++Wu$%^ZS`f?<k#9nX-0xC+VEda*g(;bdG6e*2R6VCiy0qY?}#EjiNbCRi;u=%&BLJIgs61swmf{qRh<_v1DNsn_37dE9x0O!7p`lnycaOOh{SCJq9#6>rs{9Tt(SJUIhj{75*u85zozFnEaF9`Toq|sn1CkUS*?^{-x@_bi*I59v)mv_-gu;?5qdK^Wqjggq*N+JReHW5T<n`)DllMWD*AfF7K(}ARHHe9H^+D)19UxRIGAiQ98e-ULoa@#G;<|&k0$jTP`4*541y%t;HR^<}I<9b6{oMl{KrDwUGTOCz?&d=aP19I!I8<xHk)QN;BZ=XB9+qsLW{zS1aV$y`e&Vd1X)GV$<Kh<9>=TMx6;R=igq~lRiefUPxPke)pDN8S0(jl6}=SvgS4h94?OD87ne2gZ4xm9_9J6;qZ*}(86ePFr;CH(N<VTqCA<bUTIasfIn0llFnDbV!IfAAu541<#7RGo%Eqw$dE}5V<pKBRcnIG(lOboH~_pZbO9<Z7DjLbU@*z#jakD$SGz<?ZSAy-lQO!a1rMn<=??yP9o*>b1l9u)<{qdlV&}DuqAB98>N)WnQ8@mR-I;t9-+dg^UBc#?iSA|0gwh1~hOH!n&Ll8vX$~)ACSmpc+=IJw0E7diW`?q`HgQ4gt*QG*69`GB%BqYFg22A>l!zW9m4Q)X(U(etE7)(`>a_v_&ncu5;$S9?W0KDcQSXidd{G5y{<0QNojgdlLU<3{7c|8-&{PxFR1D^pS`PF$(GHubqY$oqfh03sVd3}8L=kcmk(U$_Bczrj19A`vkB1nek%^fP%BV~-nduLHDAq;{;kC8VRikg(6U$>T^sKn4BK(`!fnVy&aTDz%$TcaPURy1(VlP)qSy_xWfYUbNmgm6Z5_7kf%DRZ0&X!6hbBm?2D?)QY@&{ZhQ(UUdMaiB{i)1TRAePOaTqm1X7e4sstN+ZU#w9JnT1CHsw7=sD+&*B5V+3)@MBB<b{Du;f>}YA>ZAqHNVw<MlJUrNzEC0V)W4^~C_|UF>yTWLFlE1&NdT(^|_P}{mNy;4Gd`j`Jo;8ymEOVbnX_6nsZ>T`05;%W}kbch`u2378?dRBHLUY3rM1OA$x==p=<=q^es_EhHy^Ar<C}AT0$Ly(|ZJro`&&+V5`T-Wk6Khw+6-Roc3u7D{;YF@ES1fV7X&ZByrII5WBrSV`t=tnS6SpwNVNXKdIH}OhoA$al&aP~O{7rA1$-ug$quuC=6Rx=8NV9}pz_pV_o?jT_Kwu{##dWI2l|BFCW;hhB?TQ&r@b`%iv%?+K7ELqpZ08^6JO8;24sYh24~3oo%DcDtr^fmf{@cD&2`iQB!;H9CuuOf(C0FEW_1}6{+M0L7n)9?}wdj{QnUkk_ocP>_omIWWF=^)h34D8dS^jcv^p=@g!1I6As36u}5%?~(deYQph5Aul#L5sN51fhE>zz76ZATD)h8IxZ^mT8_huYiu47Jznvr{>~+!$t^1rt+srKb1n@|vjvkC)uv=u_aCi=~V{>KXHFLl}pBd_6wJ-8|IdYZ$+06+SJBb=9@oVPAc9adWFDzUMM8Nk)70-TWUzg=?osFkJBjKbsY{ZjC>t#aTT$0_6!>`f0sR{P?{umEk6oMXzVLISXwrGF(XMlnnQBCqp+~%Wzv$P(g;96Uj8oa4EEaN54^hZ)tjuJxF=D8&Lk#Vsq8(A$}yoWml&W-EywsPyMSY!}Y4am>zkmi!u@0OfFm|xi;m4pNlAq_x`k*iadcK+ZNF5nF`^>78tS8U8@A;bLmTN>z8GqG|O#!7J%yK7JyzqvHitGV!H*ssGB9W@enAP7?O;#=%6WW#>kr)j=0q{wZhYT&&tI^3p!Px0&G``O%EFsNX8_$-b<JjENt1@E8)eZ??Jxyd|6A~Vp{t;>8Q1VR4DRQePyZZUgSWi28Je>>{Q~(tB$9hHz>k|n&=fA--O<BTeiKFk(LxbjnO&(W=8=+og`%()GUV}1Kh#__rlD|r8YAj<evk(_oo(mX^WBuW(+0M4%{m{qsFDT4i%-AEjUio_P#v-J4&64*V`bX40&k5T{KUzp+k~Pa<Jd*(50qxsQopp@Gy5ZRnzXMk%l4!L}ZU$wd(NuhKI^m(e!9YZUX+g8LE}crO^5EsR02SqCxyq*HZj!jS5s-JJm}h$=bHQ-9nlt58>eb{hxVvZRq2u3eCy1Th@1SNZed1LAy99LFe2Kzo|EjfdLvoIqBbfru)&=O7vM!Q^HzHMQ}S)f_9PwV#1Yjx<La8gi1(1vI7c>5XTUg^Xy?g_V@667C}M1Tt^13o`s%Pk6aEK*iGe^<#8RPf99)FwPCuHKXHR#zS={$J?NHJ4q$^7*ztLAhG6p0VZO=__PKYTR@=($|M)`jsm0pWj*3sZ6#zj%kvSZ|P(3~<V~eW?>Wk-D^-w)jknb}~i+p?TRdJ|JsPp^p9L#6t7(mAT6ooxht~-dA`FvZbN}peh1UH}BkG@eEg-_+Z&}@tYT0GylHBF52!-X0#YECiVvCj_>tj@!5!uo>8;DNj0bVBI?@qX_lxc(CrjcATqg4|94=RbL|%<X|X*s81Si@>cb{)2hR)}Qig)+7I(%+a3V6H=A<XO)5jmSNMlRcEd*IKU3SsjFfSgZN}*QvoJ(#KJ_EBt20BTnGcV@A(;o=4!rCowji;T`mn5<(rOyob`N(%SA~=cZDk-CCB8{>UGpbrJIIfM;l3Ej?Ed0Pec~040FOwiiogOaPzWtHUSK0zD^b>%3*PjtcC*cO8%6(bsAEv#HQLHmv1b*+NTBy01HL-+ZJKy@b}_;>=AiY7E-@VKGyh2TeaOx$yn{mKJ2o-%zO-r7nJYLze%;D$<1VE5lxpHiAy^-QHmGYm$O=PWX}b^sC75kmw?hf_d~KWrM*~dAO*%BX@g&6T<(#KOCk$u(QwlPv9Q`OZU9z$b8w+q3oBZLB;`Gqz`SXmakU2d+?huUlP>Q=$-DNmybBWfl&VQB-KyhR>P5YI=!5V#Ut#JMe*fJ|XEKz2QRz%}37pZXB4S29U}r@$Zxyp)UNO_^Q7x^&rkQ)Qde)v*&!W}M%;T%RsGIqzXf`}rG_(0zie~Xj(M**wx4S5somoi_^6|m01r@XQ+(%lO5UzUtymA@cmzLhq!Jm>NIvipgL5PNH<+A!(xs2xtSssbX+}i8bU)jw4A3q8Ld{u$~{@r*|AAkI)tMHLA{c(gp{`hf(U!V0~3ZNf}{~w9}KV->+`^f$O$o>Dw{r|(x{eKZ*|I2^9LHQp!{x72ZPyZez`}=wXe(c2YH*S6+j#=RM+L`SHdn|lAYnKg6hn^a!t}fnWVI-=Ltbb2nlu^_#`To8bi?SB-IAwmpa8FkJFt)x}|10^Sy;s(Mn7yDQCD~vY)!AR|PxC9%Y<F%>uAg7m_*vx}zIbHWx0Q)*lRY#s?I0~1^qcX;3+jFOaS{iZUj>au=hr^MX}nwN1L!gfKll79;@MS9m%q>o5c$gq>;wlsIxk6A_Az~cN)6j_MwK56%X|9GLPo&NWCZGS8G+k#gM)c?BYa^%FZ2W;RZI{=W%N{8u^1?mrAqe7Wap^&&ZP#bYf=OLDYb!-Uq4qE7{7@o_;7=0-&T)E4V=jcRK*wb?61=|?&ddFgb3WkJwKz9+cE1K+;jh^Zou>Y`pBtP?$Lv|nKZ%j>aLvI{Iu)aZ2F74JPq~53kt)%I^)aFbt-HpTYe)w*)!^W70$&C&b1EwBwtWn$|?BAF2`M5k@H2YAl-c9lR^Y%!*V$|{;H6|4Y7jRh!LFPCv}2xaQx-4xa+@J!U)gtb;dRy|1Ik1f8$+PNVgoaL4%leef+ZJgTACeM7x{BXoEy2LZW4E+RMY$6|3ylx;TaILI89N@JOQWu>8=#V96Ol1S_Ipdr|!xaD^O@o88EPo^TP6WeC=}3Bqrh1T)`G#IRQ{Bn4AePcZkT^<8Bi&Y>!H+QFJMZfeq?J6Vr?8nZm64ttbmEk3SpmR!Ed47tv_ic3QCNaq7{>ow6_|CY_EJLkV~wc}md-OYs~#@U2gYwVdw(GqWtMJ6C1D0zoRMwqZRfv*p8%795?sC%1J6U{!qpb_buzHPK6X|@x+l=vO2*r|}}^BhRD^n|YY<hmXr9dpfIhkZSS=|(9anS|t`#Rf7KvCsF=+;(CwcLO&>F%L0GTBg1Aib4%}f~@?hD{W^YiF3Assc}TxE>A;tQGuL1wqtK@W~|e|6FdBg7vGZ>j_uFCCvkpHh(j|nd0O0xz*`Z@eW-OGWVJKignZc5=nYdfL7L()jZ5@p#n`8+kuyo20gWfiu4-2p-8M&|9q3nW1Fl$|;1>lm+`T_V*g-Z#OX7+Kf7e1}LLMXj`_->K+m`SG5q231sYDhpsecV$R=W+`xM_-oW~XCO5Y`{;dehmnrznTr-<CKYjOG{xF`aUH*Hg8_+@Fc>;egUaFD@qSJnW&591PZ)50ZzX>wWA>go^|QRer_peiXn)R#485>k4ki0sZu5kG~5Ok$<^g(We2-F{}*7V`V^du2NfP>tA~W=_lDj>z-*y52SZY`8SwE{N(`mS3D(6On7ectpgIRrE!6zx7>)55?i?_G=ZB0;!&PC6mubWe1fh8Z8L3Ar{@Kd*ndKsjux)nx<z=V=|)24nh}kix2<l`3$kUJthyj)Z9B4=gqXPkU@`KrXYdAiQihbmK2i0>(ZDk50==ISA?|CEFqb$<lMrcX&F!^cjsoZ~!0@j}IWQ=zC(Q`x7NPjOk_ru@aPN8<?AuKSh*?wT&-eJ|c5k+>&h{@sPVnBA!)0Y)Ca)yIaQV&r1?}jmGCP7V2!9{aIPB&(Th6oLyNK%M37M{7;=5>GRiut+!#c?Tl?yStNAD#7<Y!a`nRg1fn`dK7bFnccD__IWg-$>E$`=L-qRD?%{alFO4*r1_I1l7F?GQ(X9J_Y#eSv&XSCTY`S)b^FotK$}083A)mX;qxsNgtt&h+#RIk7b%ay86yyW)SHxAOych$2sTN;#>yAzOD$d=co&?~|a(iOJ3m&+|bhL>p&B^2%)m%U<O{h4heIF62!5fQUwiIa-~9Moyih+M8*$C+-<51Rgj%58u!tSAei6l(lvVp8?qk+#&o^YAz!pG&Lr=Bj@9~MhfSp6(n}3)gEvgYl6E{s`%LP(KLA}FFPJ*k13gBNoq7g8H1LNfvw={YQ`kN$-S+nDwH>qT;bMe>Cu{rYWz1}yZ{X#ZCqJ^ZUK{%fka{0^C&`j!;CvA8JB%h&@x0MGC|6C_M-5B1p*8SswGHSVI?msZGk6;aT&tGln)h0u2hHH_!ugAjmIPh=zIrumF%Z0TGUjIe1W{!)q8*NMUEj7PE5@xtwDLD2e=RtgPhOcgn{b*ix+Q%eiHP0jLoqU>NOv{21OPFQ!^<)Q)F-}rz(>#q73q(@wU4_5(5OZRyv+<VvYb?I!2_p=8<)8sfUo{o}H5)N5uyCSmhJ&uJ|i;^jg#rJ06hqXuubv=nGD>Gr;wSi+{}nilw?%(3AQIm-L>7<Ny`(%=67$iEuBv1LatxU<Qj_F%=3B^MtjPxnnS8w?M~licl2piwaph_$t5dj@B`rlciivK8+PtJ*UB;bsi-uil7e!$;gC&!`>bCbsMVl#NYW+45>#DxjBM$7l>RYy7`uD(h`yDLz+KzdH)M5uY$<+RFpt02_#H#$5I;{SHfTtnoE2pTe>0%XA9V^nY3~P6KBde9+1sA!{SmIVZmZ#iJek;bv5egvGc$QSy+sXGux?9WW!(pKVvRlhvWKCyvF4EwbTQXuq^Lj!%f{p1Dz>>!6~ru(@Nefpt*8H_w;tme?H8ixy=ne)Ri4HKI?TQ!NTu-D6NX!H4VF>Rbi4~??bL4j2zu)nJDe%Unb?$P@lqGN;%DxDb5YjUFA*3sj^f*NI2U+E>6+9=giy-eF~+b#?^C;FA^0O0(LDYa(szCMORp?;hH{$1<KjXO|Q-53;)qO)Ds&zKPN4tQQnWZbZm3V(&<+`ESJvOmQE8wX|*`@U>fAN=M{L9kVCG<6_fp1?*#EyyU<7>Si%O9rn!1Gyj>JF@{(B6gyc5c(@9c03)+QK|EQt1QI4}cGsU$Oaf3Fy42^-UAV}umgE~^P8d9zsR)!F=z$&M~8kf;E1ixsB7FB1IT$#2B#(e~)dq66Ec#!NJENmIMDC#&kQ4)cIAN;XK0a3)Q4J(!3DJx?hfu3?(W~BL-rnvL@mn#&FqByG;DB^^J1(%+yPTS4Au^Cy~ZpQvsWQnt|(%2oAphJ7M0w%10VRX6;&j}*e!-qQI`8r#A4L=nf6dIfrKCXs_;UXvml9p?%Vu?F1Oyou%&6Yb4vO*EXGaQ7dDeOz_uePS;KL76@=*FhQ3t1i=my&BN513%rOQMIr5J-8F>v2UOWmW{+I8z9t0?D&9Qi6);R*u}Oeo@#+?RB~b4wYZlKSL&^xy|?(81-Am;f<Jyw;3OCl1ZV?*%i_UIkA;gHmx3YllOs7H|htcAqR6t{a88a`JvF$OFAJvCYiFxj64p0rkb*y=^aQrrR|&~zrMN^=eIsoHh;;llgvyv%jWBl+_`w0rAQtdv58+dh?st^bJ9vbRs1>`MUM%+Lqboc?x^%TiXANZb@(lFdKE83v0LW!%9R~GQ(a(CE6IJVCv}68)*EM12FX*3^t{aeL{3!_TT^*Zz)&+=F^v&n;fVI35^H{F_X>aHhl*b}82rN$A~LvFtLKUuglnpnU$q>^yT;tx%sK@0?K5<#u7+Js=S!B|t+1=QPwQVou4CQ2=u+L_*DZ9Z7;PO2I=6MHWcz)KV&~T+X3Kv0acQcSpF5YPVx0o1h4ecox}D_3Rb#RT=xNejCygr5!KcW3z}cEs%{%e#g8I&Pvw#~lqp7s;RZr^w{>#SP=8DGpO}*-VCRW|Cr<g#QM-?+i*h_WlRw9|znu0D#yz$!_)$7|D)%&7R9Us-GPBV?_)zcc)eA=MWCv|EvIwfehx|F6yaBu37bBuGAE_J)qrOsD6T+^j)dWlk_9{<X^)W7%MSL*qcxwTTS>QUnSxr=q4L|3G#^Q35RE01aW!6J9vmPv$1ciM-LT7N0dUlm{qN^zs`rq=E*J|ZJl#5VmX#eZ|9zElh|o%H!$rL!gbOlk8{l==y!O)l;3eH1gAufYoL{^nu@e^1$E-Y>uB2^+2?n3$MYo5#Fz6v<<&1|Bq1YUzuPR$a2ox@4Eo>R@6qCYWKFU<S2?=}&)|UDmVgvLXD*5==j3m;PeT`itx`zspj~#xlxqJEO#09I$<!CzVKjpk6$y3^S=r0w{=q|GX;OD;J0V+B*i*Pf#FREWz)^G9pcW5vgB@JVKx0+}Z@uGmQmd*4h$v-WWF#U%37<Xa>&5t1B-j;D(SuFUK4JJ*q8r!6`buSbrO?zgm}}u(L6bh_<Z4cT}3?;)|*D6T}TPGKG-l%j64T*<4*jM;#N1e2c!L^|x~UERRdXYaFUq*9Y{&hwFZEz}3i`PaMFVmT_(Dfzi5Y5!Y(iK3!Reov8=*>|nOFA>5R;EkavlT+{El2~u=ZZ^0x29bhnxo6RPc0_BV|1~sn=APTV9Pz%ZnbZPBev4(J(t)uF-A{uuTmz}ViQh;vh3&H&|K?7rS<0|ZzYJd`GH#NXYliD+Q`);{$X2FWk5bL)**#LX>HiG;07b~+}R-uVADjlzDI6Mbo{Q`zKLqZ6OCnUrSjTa^;p0;3e#`0ob)WR@Uy_Qa4Nhc_tvUYBGhY5-|NOm~_F;x;hEa)v`*%~!OYVQRB@~}&F+QV+n(0J9ZnpE1HAY=K}9Tv@1evSseWqHw@(b@$nBCmnR9q)5Q!i(L@q3F)JN_*D$n{yYt@TOuJleP0tXPCS^k9Ps|E&LT7j--ajiuH;7>PE#QuKjvg(8xeTCBJuzhdi&zVJ*g0=eNSNHOg7d^^R(DfIdcXfsz5I>H-d<Mkb4A%tYU|c<kwdhcM9yA7{#q(%u!KD^L}m1pqnVRbiyNoLHyJ0~zT-*NbgMdpax3nacq}SYcZs^5ZqFan+(ZfQsJcR)8nslA?_znK|Z67rM?2Uj+Sks4OT>#XPdqP$s*q0@z4ICM56j`)gb)8{EpIoPC(Mb_!}EQq)slz3I>rt7#ZPQSm^raoh+jud?0EIh~G1y-j9*K3TelZ<<&FM}Fr@{V$R7{5_B{P)u|G*N0k(uJ*U{1z=y6mt_}i8R8mLg>##>mcCZ$+A_onn=L~CfL8{IfXl?iN)!mluvKA}WEaKhRP<^);uNO>11MVZFPbT)&9ZINXs;ntdsSaLR&&2Lr~RP6p(dTKtxAUx5?O<aAgHIGG-_w7Qt6q~hy`^Il4Hk>Ar~f(t|zW*u2IX;TXoOHWW4^8^tV40AY+5B$#p=6S`DH%%pC=9p)uxCeiIa9LJi%p4MAv{qcQxbt+&we!-IXLTru_;ngSm(q+||XAr-vkISzxO%B|HcZcfj~nhaaCKCuiCITV!^sm~gx)@r=84Ggwk!wl5fl+=PKYt%zyLXu)Rf5DtS57l9um9;;_AlS02#u<u<$r-BY$(rp~H$!RG{dfN%Mz_^Vbemr^!=4Rr<M%*!q*9_N=(c&GBA!(#*wuaMBz+#nO`w2lh=6txN$2vDjymY>`53p0_E`ElVBG%ZM+Lu+(sLhWyFUK-afCmP@E?vJKMuu5eZP<Tejk7QsPFet-|wTo-$#AFch&c+qPzCXSiY%WP3X^-r}$jCKOrgMTuc8ATEI})2rg{-E7d|8vhux&`|$`x-_M0JtvNZckK%r#_L{YKXA*hVqVY2wIZ4S4q_4Xx`fPF~H=o*Aez|eyif!Qq5`Sk0KUc<E*<tO>{iEW3{#@M8P9~mx+)Sn~6ivT0)AZY-9XF~aNL=n&;(qCxxL-f%D@qGd*K(=scPZ-^WG5S|%S)aF{mw4|C1zZOTz&MKN&9g;bGsZLu3ihr;p!c!IYaD<s(9m`k{o?Y`0+x@&z<Y|Au=?qK&~9kuYxK5g>&IP35A_~eO$zE)abK(@<LCqyui<u{jTcTJ@ZdD75uJg-#smeH`hHYQhr6}O$|@UueoPR`CZBn`tZTk{M=H|&qw>d{E}VhTbh2RGkH^M&Mx6ntu9^{(;Id6o>2Ci+k%uCGK$yvGX7_>e*WS&XF`ADH!sloySV#ot=kFsQS>i7AsG0WG~zgb@tP!{yDp7*RX^}tWHL;Oj?=X)#S*KTil)CYbklF#BnG%p&RO`?7OB$t3(jl&|8DgguHUnJ^i9{kxdOZyQXKBkqwFMw=Uv)|;Y6weY{)=btq1%#pcw|!tNbfshw+<4Q9eStTwU`=9|j190Z|tsF~Whp6EQpRdRHf!!{*SQ@<E*BuIdJGu$qn0&R&VG3%W!RPfrudCl0PA6|f;30M7F8>LX+u|C|_9ExVKaE3jtymvIQ4*X!-f@s{KVKAi-$=CAmdFQJWopx9Py0ukJj9|Y7E-8JuZnV}7Rf-h-n2gGZ-K*viSv&$hr;nSNAEaaNM&qMJU^>FI^ao=}8fb0d8odEV29IOn7nkijCYi|Gwkq9QpV^yE{_{Z8X<Ug@<1*gx7kQ`t%+^WI7Yio@9I*)zKSCg+C{WIP9JOzGioC1t+qHu%2+*IAprBx)IEeeU8^RvO3bRskrY@Ln<MhX6l22HUu^eGU@d1#Rcb1HfN1u}Pe^<mNb0{9az4Ur8!=y>xnvm_1yIU)zcRhh-(fXp5H#t#@L&!#1Cdjs>!{Dfk9dUQX(C|n;j-3cP@5m7{G3PY2BG+WgWh*l+33P+$4Qp2X_#zATXJUTv&4I#2lR>mZRew*-^mL0}k-kuIb5_Tq`hX(Z)@81HdQiOD<8vF&-w(?=WupTJgG#U3>YO)A<&GF24oRnB+ma8iWltDpH&B_7KRz6OpuKrM%Pp$GWM>G%xvhp|IXYNzbEO^0>llDZ$G{9Z?Bu|i?0)}brt5zE=W-){kS#$%ppAA{p1L2gf`g`E%1a>Mboq5Yw9;lv{cLYaoS78htY_^!PbeJ3TZO(5;-2WnA5K=&&vE$}yO&`BJ4qvd38D%AG!HysLA=;Y1{iQna`Jo(cbl_Kjkorq#6Qm3QZOXr0@wu!8xR^5sNYJoWd}m#EwBl<=9MKFiLP><K_HEJUnNTAHfE&80%~ReK>dt()+Xb$vfSM?DYu1@=hHDzd2nEQf2$QXgtY8IbQ@rH76qURM=fx08Q(L~d1-Ko1@-4@(Hrb%jew%1p+n+Z2INmAjHRDJsAmG*&KuJrB(-GaY!sQHU){XZU&?bQXmQ)uq3iBMuaj{`5o(|(LnvB6c31s?>cai95srlBx(sokm=&P<-sC48-b|qHDB+-Gp9jFhL?+A8>os$?{4j(Iq188;Nn_yyb6iG2u2W?ja-;ekh!6k}Bia_T!m_U%wJ6?EC&aXhp7=gs|tdESml(RxmpoSZSF>EtRhSOkJ3u?!4rc=U-NfXgNof1qUDxuPWEtzi_JE=(w-GN>qOv=s_l>mJvgj!1TYfrsB9BPx}dt23z58<Ae=}@E<a9%tZ_%J*2f*!UKjIZtuaOK=ze{Tek=WsBeB!CpCk2oL;Cb3%*Go#cDz)af5YgD>u_Y>M`x2SaCHXoCcvKxKqx^RVSEG5o}!fuI=R0JVL_>3<{+DJEYHcwbq3TKm;pT=`E7$cgB1a^FGUcQezuwDE}6*&RQO>QQZNY4saKIcQrQ2y%N%>U;dY3j9{pkHDDJLjl7EIrQiujHt^r=>wgC)i0VJV@91Hb=cK9Ci0j9CZ;l9uWoEKPn0$j{1h_dtEr{kLZFllP-vH)S(M<K~PsN(^t=s1}W_HM6>ZTU678mzAFUvR6ko3B%CXPY`m!gyK2$}c^zcgAAEJ{X}8InWjb>qyUpKBSP&l*2q|iaR|G;F_E{6aJj?**p(J9=xx_wT#Pm1xLT2Qr$mxTuElN)KoXc4gDm*ctCb1B!D1_%3bBocbqP;1Fc(GlsQ9C8APMM(*7Kye=$6|(&<j>iiO<{MY=dwG$2FS>ttA4;RD*fwwPzaIHo@V0LeyYdhhp*Yj6!C9h?YzB1%A}^3DSy1dOh;uPXF6L?MUc=u(6&BD^PSgr`*ZokoIG<hgsqSlsR2**hUBN?1Md8eM9#>TOiLD2{&&PTs5yj^aP?I7MbHUe&N}2v;jlT=8Cs@V(Xl*)+^3dqQb$4T*4bN5l73cRR@F4-&TExj*AYoM<z=Yv<e>BJEsv+v@n3z1d>5b9LOr>=v*(|@A|r1H@r1VEDq;68yCPwDscR-%dVB1>yEBi6%2CcX6;fHSI)G)mHSZO6%nUFq$zn$f^?D8|F>Dn3XnhSl9=z-JNUL;_PpYo9gF{lyID%9MlpwRIVC!losm)`03H4x!G=mCg!)r&mmc}?%8P7<d)(P&gIN&-x&u(hIBCQDC9y9*6ayv@rMG9p!k>yTFura?+JpM^)p2TbOdI@lD$;4%#lr4knjD4%exHICBKSsu12d<muiKAyhvJ^7JU(S<a$h(;DRp|ls$+#t>9CZ`U3(tQmHeL?c9-IzfQ*gTxhkJ(8eCqd<$j+H@s@~)yZ#=gLxU9UJtGQ6;C+eXJy>=OU49JR(Ot_^dW1a0ClY}Y^ga0f_X1>}atMJzmJFKA^;}7Y|mH+M$#bTOC_zlx>hesrcY??3iyI?X^J1`w27d)1P(R2Qcdd-5BV<v8KDl1q0XnxlLovTD@5z054fJKLkh!^pp$G*HVrXkW^*4^BiY9{#pEgsJNJoTpHTPb~q_rd>J{Y5<QZD|6he+nnJ1|1U<9APaY<XDKy-+a@#{2ac;roxLU7po-ki~pa!ck8vSThoHtskh$y7=0Y(m}Aa0zw<uTu42~-wh}d2zkpkR07guxL<AB72#8c^l@-K5NR>&ciC%yRUe%pwxG-QyKob)sB#H@1VX5Ilz4Jniw&!`?)(_(_=Uj(xt#7mE&f4>vbBsRv=)LvU-u51z_j$_Q<Y0YmNTpYD|B<%GD`4d|f}5pIi?;|>Qf7U?rX;Uz@M;jiyhhG~S*h}9$lo5aYS5(q4~pS@B~J`S;S*{+zg4vaeWA>5log&yUP+l3@;HkQ17`?qpzz%Mk$8-@>8W>4eaj<)!B$(c&KhpO_RP!WeI^>OX!U@e<FMlXTyCd7a6gB6_k+gAnfuU!Nf0x7E89!=^u{u@tn_PBMyevTF7*-e17)EX$7Dl}%?-ytLtuwnI`Vwl+qrco!xIQg*D6{7w<n(wy_Bq2j}+<j(K%vUmu&trF(j!Rp1&WvD#$|LlO$YSuwwjg>DXXw{mDNgPf7Ih;Zl6pbEjB6a4sCUS<vP$s~~3qktAq}<9J)c;`$F;?h2`svyLzJd1uj_GJzf3uAQj6G)UV9$^%I{hqVX1jP3vj@d|a<o)JfVs+rM{*s!%GdT;t6nTiyq@u38*HPnlQn|!BS_6#53edY#_n(0{V)x2_sBvq@W@nVH$yNsH0Sl-xRx!2I?M1hH6I{OEOD&bFtPSzbfPyHF$^hkPh!O`seiI*8g=!d3Gj0QA4Qr$P1at@+fUsV~CwHNu<O#8zx>S(9+HJz=BP&D4CRt?_*RVqx(*0`pqV#8-4u4R-C6ppn@9tH&uL+wEGUW!>J7b2f7!_<QJQy#7C%DQ}4@IQ<W39?3S&Hl-4Rf`&0HN!62rqVC6<6ldE+TzbY<$fWiZ7e1veFZBEJjE-vYWK`2zVb=5nC10vV_)XtW2o~`wkJ+8$KxNExPzNWvjXQ6HL@hx3+%xXmNY&uOjYDC=vHzd56nI0yD-KY>Lq+I?>TlytcigtAjE@|Clm8g;Z?aRERk%-7k|`z8Ow85waLu0fzt7ooU#1WKt3<{k4JNMySoY<3P#a%r1XtQ@FbatZ@E|U9gCy6kEH8~`Nm8B175%#+?DR26f&C9!><*Wr`h@Z6|B<miBDUf%3vq<?0fsU9$eqS>&XMQ570(r?weh0fqt+HL>Y4nYo)YkAcJ!h#jxH*B_qgYb$X=@uvVrhf*`^KSQ^nQvqjXy@hq<AfhK7$YJ^>oA&`VxdHr*GvCw~#2^gpuLi*Vq5BL^MJNJDiVz(5L;#;2z|HrT9RuaW;g<zK@4xQnr*tU;%kNES;q$WXLkIo79U%d68So7evQacEiZvsm|*(RC&F`e231MT^4(-G&9l=GAtgIlM%@3$6_<L7UEUFnRGqxljU{3A5Y7n$I}R(+WX-pHD-v>%@^!Go%$o40j#MwNDz10E6Ng1fmf?q;d97+cFF0(fm77uZ_*XR^P?su=SqXWC#mx{<JDL72uOuYnbBma>1L%KqIx)zGQJ>Bmi5_+N*KDRJ}njR`v6(^)@2f~-ze5ScVB!g!FN-$15^flg|Yd~V!*X5@##9nFoXrH^KAQo|#A-!!HHvSOY+R1?igv#AAb2M@jn5hgl+KboFKVz?o-$ZpwZqo_n7SA<1-#Dcu%G!NvAWbW28YYVu8+ULJ338W(+xU%ZlWoWblRg^09FMLN*f*2Ohl2h0*Edne?0}I0VIP5*(APC%)S9Vqm#QfUg8af#raF3YcbSCZ*ltl^F7F_s)agM}f1z|XzWT|YmF=?|<Sp3JV4DfT$W87i4IEbIjrg&e;?XU?iDo15~M%4+xg|+0gD>l99eL0N0orn~7<xF!LgJhK2Z~;4NmqBu<`ncrujy=<&q-W~rYyrYyEIalJfHSPAS%SW2+zgf-0yBDu4Lwv(sNEI2X{Dm_MZ0pqL9E*0z8v!)9vwRC8za#<^0TW|alEL5nna@GIj!Bmbr^s9>myGcjrqmG-L_d)?M_$)&*KP^@6U~Sh(_Utgq5?zw35_weGlSOxi1V;`3~TVS!#Gx)Fj~v{GpcCQow*Tqn6mBNFlpW1vYDKMak&RWirf}VSilNBO0gDWZOfP*7G#)?g{RGv+e6^Rvihz(WDQ|3dp3l&oJp9JrkXN|Fh75Wm<i&EE;lfl}Eis-gFQs?anG=HhyNv@Zn-3S{Ci|9zpm(BDNKT$70@L5-9_gE%C=x)e!EX@X35CGpwjbQKM>L=yvZlr;vNpQ~W{A`Q=ww-h;|0TR`Oo&WqwHBEt?)i(AVv;ij{Z)BXyF-QXCB2;=8LbqDS`6eq*GohUdIvwZQR1<zZ(13WJiZv+#4g3x0}!W^WRDo8Iq0@CAtH{$e~iqq>WPR|pkC(yredU3?*HD@5b<S=s21nGshN9aYeJ`$mqD6xjK36)3aWBA!QDlZr$FE_;Fh4gwAb|VZg5`%~2<8|m=L)=}Hepo)9-Dh*eo$NBMyu$6)&&JwO6{j5`cFFK{t8Wgz?tl82x>!IvJ(r2;3Xe2POQbkG4TUJ$m}i{49r?T3O2d@g6b+5!VC{@Gx*aLPxIr5~*tl0R4yxK9V?K@kw7(n#HP=eEd*Wi0*>z%H(l21ODF@xSIR{fH(bNh15|E{SqN&W>9|uq`1!ZLCyh{`0pa(VC3GY(-P2gSn1MfldeB`UVsq)(6G)zcjbuBA3+0n6>iJjj-2HKR)ch1<CM#|lRbFx-m>6fv5UophM7LOX|DYo1q=r=oo+d*8}QKpv(i@uVchUzpQ1(_@R;7*jQtOsXzvt>FSIipx&z_m<vnT&lnme35`^mJ#U>2D8z_>D*Ln)vBOk#b52Bw-Q3t@I3q@`m!{!-+PzIdCI_#|AG#U<#WKb3kSMh(in8uDY!~#%bW9RrHb87F-sK)3(Ku*D7{HvdS|2t4SxQd7vM8u+Xi9cZV{NgK&ZdTR6^S-(fQT#c#@pZXO%Xa59|yG$R)cWY}z{`8TLyGfh7F2xSOgjp1NONAlca%rsy|a#~`?8&qU8VAIS??{DTI4&zW&)w3kYpsrF*TGZvcl^=SQP~h~EDi(2X8h4C_F34V^#azK|zGfxR>Lf4L!$r1byM^aW^2J=I9XI>+Y|JF4I&6?Xq2MuQPqTL9dc|&4K6p3KS~n(X+aFo86#lNlnFFi+H(1VqOJX_i(X0}F@qNy`SgEC#gZg>dRMs?y<G4Op8UeMaUTSX>s45!+Ia9PI8e$U>K0#kcm(3<!n1!jCBErFh<5H}!^@KbSRICX-POa+6H6ji0T2pHpaR^qpgCYc3xjr#2$Qn_aOfLCt8`*NgS{)~GtP8(dP^tRhE@($(0g&1m*FHc2zxp2br1K|mzAcr>Ev<r)RW)4MoH{l*EKqLK{?w=GX`mBqJyWp_i>DDgI-BY2X*5o0=Ch|!X}Ylhm|I>xjRrvW`Y3p>^QVEt?)lRw?n*m*8p;*U9!Oi`_hORs{IPuB{U*R&l|>mo;$3A?KFsi4o@k^#<u6?EO&N`)_0Emz$jAtw$$^T`4XgZ&bNQ~nL0ks6Rn_2fXx@ZRT9gTuiN0}(jcyni)+NzU->Bl|)aJp?9pP`3=*dJfL{%aY^Q^}MidPyLn20*mP&<~7hkSK3^aA@difvN?wStY-)+Ll7QSY;TX*l^A#9fUL5Osgn(D?D`Fv0e1d?*fSkf8FZuY$Lh%kic<LpbS3+}!xpjR6CBfQl2|C@39(9Cm~J2LY>F(I^|GLSg{vlYx+^#A(2+MqfeAf(K5n&wfEkmh@zj<pI#kv_+`hyrO&oc0GSnHl6Y%dx)PR)mqNIv(o%tc@rU)G~vC`T4Ouuu&?Zu&bYVw@=EzYR<wj+9hmZf^LYp8#{sXD=rj18<)FK%{AtC@vI{&YuYL4`#W=y=2y&!^4x;UH=>v<`D#c|6)_Bp8^C1Ei7drzI2Nn<09(5ihmCGxCy^P%O(}+|tv+uc(?ii>EsP58%18HMfmQyix5WT=$2grsQOJuPL)`$JmYHol=%Dq$5S|hsx6k$jv0BTJLUF#wE#XKMFpRrsh(!z^nLf#0N;8Im#gMEkk7_t=<AjACu<+(;MmykGMI32xcq-*V~EOp4kvYK2;0Jg;9g`hlc>Yc%N%kpRgyPa^VW)-c`iBd#C@@OOu*R4t6onSiBf)mc$deV1$VQ=O<AL96BKZ8!ydP9>Cg=9(yl~lo7q9>}O%E$S66jj>^!AR{{XBBHaKb}-zu#<bmh|N}hh=3Ke^a?Sdafqi=?s8ZA!ka&7+u>)v1d+p+k1sRd9nhe40lQN+z)u0zK^>_L-I`>{P>BcwuyU-`-zeZ0f*04j!t+-yi2faOW!S9QbpRta_<dHcDTrw{vlog%o0<)%bSK$?Ey>#jn&ilp#jxvwD#(#l9qV=@hHV|OeZ;jrTVIK7eXU|*0W-s0e(m`*%IzG8%SGRD<5zb~@in5{H`i}P83K5GN>4*_7%2l)6o&8nXYO+Al-GO+0}J?EGq~`a@(t9*S3nc1h?NYg7|?0vt<6EeQT)2ngp)ZB6`5YA&HSf!o{=wrg*sUw_-kd5*3xazc}#6Xgy+~vD9J#mAlm_1Rt7*Ms0on*G9jyvJ#<YNPvtFPLXef4u8zoC2A%4lsM}Gf`=03yFK)!PW&2ZH!T|mH@w3W<hN{ImzT*Aj_d1gG8x8EF-p<(v<20Un#n+#ev?N$YDAyghV)n*+=i;vi>lS>)Hxlh&pE~<DewPiVAJ4A@mbUBJv!0&&G*HPIRuuW8){oZOFYc=zpDMVzVH!(cJzY|DH|leru6%h(GD+iX9M2yNhiC%d#C_DqOm*<el~m8{E=_<6z%8Ho^!L1hA90JN*6-mvM(u+eLNLAGzfvs@2=rnrLA~$&rw_QsgJY}6EsCJ!_J(_`hNA<yL5WYw64|q)3XlC3$kFnV;T1|-%xec=pS)3N_bjX=BHZCv?QovvmETKvhh9T-hkbr1o85gmGqUHS4fh0SI{*4fOJ3s2y?@QB$Lp1U&77<RV(q64`;8@1diGksCJN{^M5&lvZ86HPk@NCpyDh%lYk%^OqA`rkVflLlJ`HCTH6H0#TYhz;eLkotlL^-Cc|11%&Eg`FQWhN385mdsk=Q+Y_z{~ZmVnTyitT6Q{f*@nj2fNFl~LctYDmkQ#Zn-7hH(PadD*dC^%^$L$e22$e*EiXFq#9e6UQ)PyW<C6b85Z@n8vQtpx2I#lWU*t07Oc!*`4Dn+SMA#(0vEYz-tuoy+oT{bLzdW3*fajS=0uFl=cd6?0W1T?Tcc)!q<d4duM$@(AeDBw%gL#9ZR!`3Fu{$kSa$Xvo5>-<!9Ap%N^g9otHs(xuiS4W0!LIB@3L4beUhXi83XiYPt@=4ZUFjR`A&sgW@u&H)vY+BI9Ctl}EC>7jIE*MtFzdtUIgtz7L2{;e!@GNPxapRZ{x!`G&GE^bS`74|m~qB_NJ;00;)%gzqFuBm1~2^L>SnOH@r*$ufH%jzFxn_#!V@Z#0%RTvIQ4v^yj9qI(LQDA{K4ob^;;frWRM>`w^08&5pCF=dIlYw<wLFy&_&CRJW%w#n9cf7LwY8?#OMDcf|oY?~^?W3o-GJwMMp4X5Vm%r-GRIWteiXmjN+&C_;fo(4%e#@bm+!{h~2zhawKOWU-mwn<Xaqhazals;~lj?$D&_KoZ}Dj^uc=#`FPb3!#w7>ZU6IAjef^Xqk^>a6co?4o(fJie{pvZg`7MBY>%<4N;0vrYZ(RJZMT(uv!7NawK{mQJk_QGwp}whv&Ky1)1ahUpWFBT8)0M_8qXN;t(N-E3&EB>uNyFxPkkXfqKRsdClQBxN=`DqIu_1Lc)2+!#i$0?7$2DCXutO{^+d0}zLN<er`0d$w~~%YQk3AMT;l3=?yM&ctx&W#oMmw5r0$512OL2S^wCA>znwZ{IRFYu+A0__Cb#wqB2V@Jd|6e1~C`{rFS$^jIDri^ZnQ6e<{8R=9kYiYGOJQa>21!vP@i`&~3l?QAF(&+T_TH&{bXa~7{vPO)5rud=%!H=*pDuBANl4d^<vx+9&)8BoI<guXQJ7)w}iv@IX8y{(bI)2_~X5U-zXGx#nxSB14TQNc$*wgz>J&{wZ}Ong}cQl10r-;#4-z7C+T7^i&U7-i`A8DZ%x=8A^1P|?4!uVaJQEE8EnCLXMl^Q=j}N-|8k`TS-bf>6Spt6USY9vLi@lj!&CvtyX%8f#^<!~7Uz*?(sDDAK^>!gLutKFlHueq#K{NL6QqOkq5xs@^cGs*#NKoY5JfB!@`!0v7d5UpK{r(<tF~+q1V6W@-b7^D%T6&bI8<u_!Z+Z`sACaSUtzJJc4`sbj3phiKmw2^*=$knAsvEs^s{QakphAw7%Y6;aj!!6#q;skd?QiamYc&m-zHSUr0*x^@EH3BP$XOHp}MiGTD`It<-$G*1{=Bt$`9!ks$u&l@LLn@VV!#Hbr>Q0c8!yF`dIlzXq{kOA~R@X_%ndjbyP4l8c`0HVD67Qoex0Pns!p2a21^e#z&8oL{tR;IjY^rg69^xz%E-OD-6qI4wB8AVl{+TZ|$IFOB}+S!F2{CC}(2AE$s$wX>xw+G}5X>2CoT;zhxNeEz90*!LyA=|8FBNhcn>B;txVn?N*A7DFK=4Fp$vCb<?4XEeTvlde<?Ey{-ekM+??oK=->~?^=k1RjTMXx?bYfjo~(hWpppp)8~z!CR*zuSj9F%nrPULaQ(@_V7P<Wz$=&XLZr3cl5ujjyBs%t?>`Nf7y4<s*bpt`bVhoz;_Zm7T^7&D*T7h!db=N)un<1xtg*=@w_`QkjV1cF(TQWc$SaSKV(Q5!d`Qg_j?^P0%CSh!17w+R%4!3BUlC?r-erC1M-U6?8<me#6EC%+w=l^W6VQ?ZTXBxwC_SO~E=@nX)f8MB*4`G``^cgF{<ByTvs$QE5ywT!hX=;q^aB;d3Uifoe-0n9@kP;KUw)<kVIFJ#k<2#qZBDggr`i;ZsmAkOPN*Zfk9-Sjg|OZL^H31q?0_bb%5oKs@EeM&(PqxaZz#5HhFUS~gB3(@>_vBiB=$#@PLF*E^<3gPF&m{Y7mL|F?UK#LWYWFXj)k^!#3OH;g97$OuzSA(DWw2y?qP%ixGcNXh*tqNEEUk{A(6XmBlq!#vxh!1#3frctN&<tPbPxbchhO?WCw(uCa#`qy7h+zhO877JgZCnan8d9tP+AK>mI4hqjs(*!hr;pE61+**z%!$3R^pT{2Y5fe1SA4FyHXW3{OCVk{#UX2WH-Ep$tyZ9L^O^N)64K(Ym3B2*^y=*@BI<Wzi$Gk=Wx)PLg1t3{Zt2+=zRGt#afdqyTavKd8d53vA1jW0^=Jk7{=u`htd8NI<Ox!9uF9*~nnt=d_%{E{+4hU)+QM9pJ3;Exp-_T*ribpoAk#P@b#jxJ64M$*xvcYu#bCm->s}-d^1gJ6DZ^{$DHO2<4gX~8Nm;Tx2<A}g`45!Nm@`U*a)M4#T%|~pn*^Zi9DNjAnYS1<5q#b<GYGl9amsaCEu~Ow)FIWw=;S*es9mJc-NT())0MM4%3Ori_dx;+JxhBKR0YJh;1;arQ>jttO1nR`64F~gkgRm+DLHMxF*q~>&1N(_dZO3_K632*95#@fbDjOy#26N2*0<+J0T(YoH{{J(~$|Rdv&b&9SPBQRZvn)MtBw4D3sAIHBm(javEduo)%Dy!J-4q=>YGMYNm?J4Ns?VI8vEU_~fdgiw@$_N{kgv=H&6-IW!Wf!p0WEA$PhbPszg^ZUl{b^<A3};X4AE~RpgQQIYK-Lw_K3%?C~%P0GD+yZL6k8Nx5C`YZZu3m*^}bIde4n=%UM5k{vOi>-y6xcz0c-bZ8~(ACPw6+l7>W`hn=@vB{&-a=O>tyRKmqt6xWlS3b@4;Ix?B7a9}C#EsFJ@lPIrYC|o?zH8(hJcHxV}Zqu?vwz!KmGC{=Gr%DPt;~!}hGG3zDYi!a@`MolLEVOIt*}j%P#=aK*&WmX4i)ibM;N{DoFC+Xi!Y`t&FQTpQ^k;ZcY<*E|eNk+EQEYvudHW*T`Xbu;aYS3c@rtdvzP@sE-PY-s>`uEn&J|nzLb0_9xDHd{-zw!HiSp1hdjwn+@-1S8_v+^8g5eoDc8vw2mY$$>lH_c>0C@u2jT)}ZyG)vzCVI+R=v=_n*W*Y1&heG;gMOygiPF_|aaQk7^;1vIc6#!#I5`rv!z6d=XL_`Y57wtPzmZd2SU>wn6)P22F@;xMYB_p0)QS><QP75|4`-ouI{U2GP%nlh+11Vm#E+7?qi(BSdE~Og)yw8T0xR28RT~#qJAcK9&LxGryqEbDLX((ZJc}@mb9my}d3W)EDrlrzsMf$VI2XFDf!RhWSf#OT%(@)x-z4`qQ*!lw5_DWBTwau@95qD4Ws%Xj$m{e=clOG4ZP$~xe7<_*1zFR_MO$a8v}dBN!TYO{oR2BdJ|(vL-ruGDJJozWx!R}YOT%L~d-Cp8?awf(hb|`4d`9_jqBFXX4t?^)H@fnR2R!rno_;Ex{(0rJry{r~YPjQh%zRzaWc7=I6-sY0Cg-E%tLo~h(rrb3xvM|xzeRri&pfMv=Tv*u<p=beXZHD_HTZ_2r=4$CzHKCo3UmrO@nh&{?c0d@N^D%yg5Y$kqG1|URDIK+Ow#qJ(Uwy+(2U_3<|m}4S{KOs-B1IyoEiOkC?ln|YOHpSN0NLi#NK33K^2<N3xH0n@)Js~I%hJPalJK^*UJS^I0tnaeh`YS6sUw?YI%K&%M+JP3tSq?AdLiEQK18CBs)vNwa{iSP1Z699qIo+157TofA%flUpZNaDrz$;Dq{JOHw|!o&%r3?zo*PA9{)hLTGqk_a@MPL68d@sU9nx<1YpuF+w6$|Q}wM3vOz>!qvGmn8{3AR(Pf1DXkOZum@qVi4*2#=3bRe9*h$UlAs7`Mp+=2**rcFG&h@~nMa{IMxI+>FjlG))vWiJf+msgQz%I}b#pOYu8`=XQ0_05<oru51GFSsS>*HoxUOt$b%aP84-?*V8<nO=v`U;-W3ZA|p^6;4jPtns~u6a8DzRI5aXO%rM_QP4tGtFwAE#F#qi)!Z<!#tKcPwSkW{OxeP&bd1)a(dV8t`;^=x)ypeclf%)3fQmmCIj=2QQrJr?yq8F&p!_g3BY%+>g0Om;w!!~zV-8N0Q)=|6w9CSmBTOMqqo-?vAr5!32l8HDEC+6E2ppDm6dZaQZQJD-+ZaLzSLY_>Qyg)zKrn82)~T*OTqOW{tR#N@t2zGOU?DA=K5n&7knwWz7$+v3a;<H;2Pho;Odt(SBkNz<{GOeI8t&hui4Y<)ICgT6ehVk_G)eiBHhDS>T`Z9S$SiqNcKAQLg%Hjsq7k6r%_gYEV72Fyf+pI_2QyNO9}?|L8`6TrB8YC)oJbR$$us$EF03D)m%?5K7)C~uBw)A^~#(QV!XAJ;-z2Skt&z?Qa>|dW4U_2nwKr@#rXlXlI><AgUsjZv_5^IwpuUGYQtyc)#>B4COWZGdXjfGZY-;V+@iDAobxj3tfIN75K{`I{yzJ;sIyMD78V86xU8p!3xA&e^kbdIlRj3w4;6^8>Bu6>1x~}_gPT{me63$zEHa%GP%qZ@Q2Ab;)k@>pD?|Myo&FN*m0bLD`o+J&FBgibVNpyyDQG=@?-weX;fb$)^4eT@w30e|*9_6w?>J}U&hPY*n%{*3PK(Nyf0@_qrrK(K-OXxy(7V<zoy`P2>+$EwKR^2l|J0RSD4^EsH#oxdR(SH>9~q5{V|d}0_^eAE<E*J-+PjP6aQ^%F=bUI{Mz-PnobW?j87G-~Rq8(Fj`=k;lotclf?HtG5y}e0Yia;)sXacnk|%f85!#6X=Xyuz%CDNIIzk82RKD5~+JR$q6|E`saz`jjs%<h}2vD$*)!}VALenS}gX*QouAnXOjCN2`JeSAgq&L6ff?KCqJ7}o7%c7;7dO-u#S8+Ql6IZs~VAc`JcF+#cvf2y!B+u5Q%~sBNh*KA6yxL!GJ>|6(52Az+z4eB0`(Q1g!=FdFI{D#ez}t`e-iw)*(;su6i=fQ(&(o_{4&>4%cZq+Wd`X?-29<O$Y50k|<`s#%SMnv>0PS=aS7lI1m;MtF0rQ_%{6eNWVkYmy=(30Ejew1bE93LFLZBK_B*n@MOP^yiRH`4=p}*(iz8tv|5lmUW7}aAizK|#mc~D&#Pvo~GW;CJ^Z>`oZCU*Tp;h%`Ch+4cG-x4!-L&hgjZ3Hp9H)uTu2Q(H3cvi&WlPk}bar-1XapM8EF*O*92X1M@-mTI1p7Q_W-ojvg0!)X^RH&ss!(er;k4uA<^+77hFAUabvt|aXmw5YigSGZ*bAQZWZLG(-yJoP^;~vBagI?W>2CD&9h5hT~?P;uw{i?w_AqE_+RcE^11Nk6D^fAQeG_Q+z5>)z=wF24L(pn`W$Ler$s#!Xt($+64gZtq4JhxLl?UZ{HJGH5HstR59kC9-QoiZcUTPdA@+Ye=-{*cZ3a#271JXP5}+UzfAkc6tMvodYr*ixf<i+DOo{H2`nVDOm%A_C-t*%{q=nN2IARGI_|i$LfSO&;YTb|%GB%_GQh^1$s9(il`B5|cs)4t`Ts>k#FW`7|V=a>~0MsUpj)0aSxR0{|gqQ5XP;lXqmmAQ_bJ!(9dvBh0BVX0+GEeBPGl_9^DYXMgnVhx5LU;^)+aea^^jDby0dELCFl8$wkV;}>o4x}CUeW`jor5oB}71w*F;>$HQgF_ubGwd#gVs4^iOo`8>B9aPd8CDK%j(X1nMY7jMqK0;OYHR<<T3C0W<<J%p2`!nS<{g_Qo7~lg3xcqtd@DbfgnUTjm%LPeMXR0_?Ns7ws%wCkbGS>$j38K`ub}@Z*F`J7nCWU(1C~1};I!<_*K%W_R=i9iOsT%NPJIm&|%thV=4~g7rxv(O&XUz3vMs2s?Bk__DFeZ{HiS3yiDq3pi>%EUYs1e3a#3UUTxf49_xx^%CbV=z?wUc77F+sI_*2AOH!R;9htV9t%nC0*H{sS<6U0g|G*m-OjRkrpYoi!Be8cJ`yhGrq#Tdtu7rn#-FM~GD56;H^(9*N*=RoUukxq3tr7RPU_5!@RrnhQZ3DbuRo7oVZDoj<nH_UcbRE1D~p@kP34G&dyw<qr^Mbke2S%M%5y?!6DMte=OuEAaY-Z;8j%`_Gu}AA)J)KxqboRAFRKm2#`}8(uNO3hkuyRR(=~WG@aGLdz4qPvQ1J(T{Q!4sh|E#b}<2KTMY&jc2uE=2~(N=;#v6xwi2HD#Dk8;u=CfTS>K$tc;m!hH<n1DR2`vV|lM(+PzWwxHAo+wi7FGB2^UrMQ#P1(wFOxW~!dfCB2EMdat>pCydlGm!yFC%{U3Qq)E4Z(L6ECL?7UD%@f14&1jpVr4X+frhH{j&(sJX_w;nOrzaC$dIPD6erBP{gcUenQWL|OZL&tPrP@UPxM~xB#Qj1{+nD;8zQTe=-QzPzjY0D5fq?q&h-Wu_ue^R&>DI~L9`<Mj&9WmN+^JB2J+euI)xtyhNrAe(YR-WN-&2o)@-i!G%jJU!noD7BAe|g^-n@NWwa24`=<XN{@Z)?13f%c#jhy^O4|Z351d8zbg}Q13>0is!I<kgV;wWE*D3Gf<kZL|ev!8cT>QVU=7=BMtNexRrq8}sg!C}~8E06h3yzW*h%D?{&cp~p8-oYR;-ul!sAl}#Bg)&i&vwj6O96$-Lg@zamScmR}9))4o1O&2~bgm;wB<%SX{RAS3)ZKu`v7HzqahH`LvRr>t=^@t)PBvR)3*qv%WD9ICO1mC{Ijfaxv)_<5u*{&oM@K?Wu{p3^ZXv-*zS*!jqAf&m?&sxOZdgq(%lJU%<Lpob|9xNkuw}}VULU!1HgefU?ulUwoZ}j{Sck16b6qi78<d*xy=8>Z#|yoBzs><oOQPB=hO`NXEjn1byE0T>GNhk!sE!<}P=^Ym_<P^OP^By5v|<0tiX#*t>oRCCdT@{)oQ=?fUc5n{n2k_5@@~dEdSEXUd!;c#+mUqCrW7o0iv*tRE~MxpRFsjUUSlgBb~dFjLg+Wbi>nBA`EcvnI!Ff&(k%z6IY5uL`#oRR@a)P~dNO;U`b=iw*}OT_A-T8lzz`ldS9VA@#yhMgbj=layJySM3KIy|a6l^$Mq&$|(sbu?z0r0TcCR=Ie#ZTumNwdR7yj&`7%*~1rU&eoDWr~C*7;IWZV;y{)rUt_;1(tt38sc502B?J1e%L6j1<l&9?i<M6VO0Z%ws>(1|}tF-&c<GWU2P56(K!QWY02YfR$_#EpS%_VG{*|v*eqDG%^%Yp-XU2fuo>2RI+|J2yG-uuo2Y5O-zwD(=LI^zM-pX5C&L=^P)5}yTJHMO^12*>ET;4I^oQDrOyIE^uD?znhm74hgZ^sn!!yZ+n2ly6}H)Q2cJG<=|n(ULvjV7l?M$R(3(<4qu<dY*=K%71NY&&-_c3EGX$|w`l`l-T(X4+%}4b|;@>SZx|3K*x!zC2@s3CUQ4%AjBNmqZ%x%KMDK`Bk3Bg1wQvO6W4`B-uwDvFq8$y|d4G0O#fN^Rk$rQF!5vP<qNku`%+e0Cbny>3xZ;IA+$1cqf<hToe!!9`wno)%(SigyylI6&)G-8`Nsat$%$f!UCZz*ILnPg&-L2T`#riO8_dJ4Gm07}esh9+}jTToVx<qd2$DF#b-g-``Sye=Sf{fS>!Q;bPp<CaJwkf(B`7L(4Cq_kl?2xuYf)RgV$IazAW1=IL&RU|R^+CUwAE${{%DGf=Y4^+F0Mzb(x6%um^qXJ7%M8Oj_WGzlf7gm*1D3P1^9St>iv8s42&Hrc?vxnRG#ul?I=Is@Wxo5}biN%zTdW2lJcy}kG8Q7LhDRncN86~GIqq*XDQ6?j)!cksq%wj@L!`xP6@hRzzy%F8m)F_~eyr~bGq3qy|w9G(tCX<3EyH92)J5@(1yPA`w{G-$~83t0=7bjU!0-aMk=qKa5$t?DBvly#jEhV7W4ZCv%0F#VN8o5!Z4j5+!F|hks2C*F9D!`153}R1k6wDrBcr(`Lb#XI*&%iY-sCUyj*>l)cvS+xc)VJAvKzsN4pYhL@j7MF(7{RV4jHs#$lh>A4A_$W4x<|(^1w_!~%zj;gZYWuTiP;$j)i_PSpxy{$Nx`&eyB>BLPL`VKGt((nm*RnzA^vBzGq(B)wBq;lTBKH-DlV*}*lxoy&YDZ?4rg#hoGc~OQ7X}=h*eTLNy0ERYEH=9AnD#Dl%bn6oal07&MdwdY0b>8bt0qTe3w#elG2h|-d+40D38#X60Jly>Q6t44$uFLY0mtBW$8>9h4WeoxO#>Pr}c)_m4=2N?YpFv%1jJWGpf&Su7Si~nhK(9LKVADbC{LEQ4MLuKl|!FG2w=PH@pU7U2wvq*q>xQxvr~3qUC9gmLNobqP;ZfE!lM@VncM}KE_F+$)=(aLscy<Zp^wz(@-(Frc-ICIcm(*yhdFpQ{=UASSVvj6bk;V<~+9?N3}CI3JK3ehzCCkImap=9EbnJ{d>Oo9pr#$xegfP2R(thm~<`a^HkjG@!5(oi*5{ZnnH%NZ0yEeERr_?K{vM_Y|V*%^X305;ygk$-63LBNZJ7PnGP$SX%l*f<-iqG%V{}M%F3v4+7?e{4K1SLGg83X&55AY3_##@xt*0#AQWIT309;%@;2e)Da@F(?1T4!74fqfQkMdqw}~ZTIOa@;7^fE{;+f5cvF^fmVDW)|Zc-%FN=ltL0AF{IcVQpz@JjKo<lsl_uX`F5A1f^rU+hxTA&d_ysg_qZ#u24GgL;86tWDUcsc_-UL2iP9S@Zwko-cKdd69+_(~K3Cpo+3VGBtP5mo!7nugENOD}9+DTTLHF@q(lend8kel*(zzwi*f?CJ)OSCt>Lx^!KK=iyVCLRbpLh&kR|l{`&(LDiUyk<~7xIl@z^Kiz#M@$tIrlH5iaPnrqB3c{)|9`fPEufTpT#R+6+Xer|1Ns&~?=HDlDt<ei+;SBp7*`|Pw9|L}my<P}*6h6GoqD>Pw1o2@`NXsh5X3loNpUTa1E>zV^ACuycZr>#OUZCB3|4OKT9#AqUTwok|_(xv(;lUF9t01RJzC}aB%-YM9B#C3)DT3y$c>b&w6ddR_S`4P;KlXzc#YsR!gyf44CJR#VmS-hX{A_m%&3+ZE|8tg}E*{~+qwF-^QZAhBt65exF?Yaw;PBkAk%Yo%CwyA0;R_l^zajyDhgqZSivK^{!h@J3-)s2<=K`E~5k$!b)@629!&G+J;GI_;H2rsFH?(saFNA*4f&n88bu$_s)W^U-z))6A07|-j0Ja!DEXjI&s0ISf*`*7ZC`gh!Ka9iA9TWphwi@*@CJivkjBkm^UFN%-hhLs;y6f#Sodn$Jg)j;}^J<V@(lwT%m&skGmgsp`C1_Y#&%B9S%Q(V#PSw^(Ar#?5lUe25#&?c+L90H%)L)n|MYX&@nq(q&n1j(xil(g$fPmLE-9MezBr|u)$)oebNEuhTwur)DQY?ySWP>4KAtd)C8K+?8VF9)61j;eFm)yksi*seCV&B*Mblv!dvCmp($64m}d<yFk-a`7%{kB+8IqieACryC`BaKA{W{U2sHwoFrec8)KrR%3*i1*SiX)!1>@YZg|+HbexxQILfx;Kc`ZAE9F%MW4+KNVk3rewkun$ropcGa2g@Lpm^5@vR-_OU+nlcUUo0Tm^5!aGWMdD!3qQf=TM=bD7m>n6YP8pE;f&<#0j(ohC&&tnI2+b%aIVN7v%~khAQ>`&q9(X``mhVaL60L+_tgC|pyGi}^FpY=^!VwxeAC2Di5IRjCs<#o(9gcE__N3wE3o4?AP-!btM+=!8-rJFy=mue=sw2M#9M*~;J4H&_?Gf{soooYI`asqR)KuuSxvcVmcEb!yT_N)h_MJne&DUfcxh4%pVck81Pj=FzmxdYR=W7JYps(ai@7Pc$<>wqjV+dx9VPI$_6LH^_4>o#)Nb;DqJghiTQ72zs9A=8??Qsk2i)UwN=hgs^~8f%cZ-PV|41#pZPPY^T#{JF(O<`>8WSy_xkcA(}nYGb?6jQp0KE1mZ8##2&1l=c~*4R?;kmre-4_XI&-&Jeo$9s0B%yJ`yzPlI>;K;>*t1(?$!zMyI^n(3UlZ899_M_?O;5EB8~B&H4vyI<hSBwgyenCMYV;$MVp?#HC#tj?x{Cl*2C2+?Thk7qr-d2RaM=(TsCXvtO3)E+XnFfx~b#B04DAt|k2)4lsyBhivdgNA?k5^WT6$Z{UhWNOcnu+h^@9B=ax@z;oER-Hp?}kT#I`%*4lMW*Rc&64f%gTps_}y^-Aap1&vl-Y}8WGmEr!W2!YoHzkiafsmNb7Em-@=x$l6Vua#VV6~ye)hama7^Gl~8O2CgHFG7XqLaC`rC=3RWtzaUr?aV5EXi=;Y>CO9SaUQdTF`Sw&K1wRAM;JdNLPahuhLO%k*OXy%K5Q|JjuNGDIYW@EEr`_y}bGhRlBtYO>X*UI0iRrdZ+5<G@>XCmJ!9lp~fBZfUD*<v4d4cy9O7QY#1XQQ$=?*;NmY+#)KC<#X*)!N~8~*#I)m-_n8E@kxj37u_@lMZ>h;FrSti5jqvQ-rPeN&U0ptVUJ|qQ@pt}hH|jw?;it@;lmQOt72AI5p+sg8;G1Mku9;Udk88{sS$ZNY=S)5b9gv;YIrGhP^n6E)iViYzv*NimmW*#ZJf5oH2t%G2$n+M)psv^Xik@%eVnn^di~`n#SYi>Ow7{RJ+dDG}yP}<fE0M_o5d4^;gd>?Qc@U7dL}mn0MdW_N^EY&z?s$?ZzusygLLPQ>AJ%jCVFthS9~*w@f7$)oWE0b?;uuw%_$g;ov5m!0e%GgOb7&;j&M2&0<Tg39LiQN=K|XpDikWZLCfw>No!KZ}gkW{z2wSSSQI^56pCPzcF1+fX>56TWq_K^X-BnmQrvxHWuF3n(Z8~5K)Sw4@(VzfGUI`~H*7BTR(O#4T@ZT1+ooIGT1mAGW7BsR<%scihwX!b^eltotNP`(0MMBSg?5!75NYH%1x7_M02Dh&w(P<B%TIHddXdV0N<Y*F$a!IjC`O^)9qZ)bm;=g^@EJn+J8GC#5=OGCYW}RwqYpiqhg>dK8%1=p)97s}>3fRg!gu2eTg9QrHGkGC6SLg<n-t?eq(alOJQI9JR(C0>c!D{4AISaBFC|8$RES_p`)Os$V+D7g9n;KR$_^h{>!U!>DNecUUT5d}oSWwbTD3rKou3-U0Aa6yPj|XRFzXe@1E)>A70LLV75()oUJe#mDQA1Gd)61*F)!^uiH9whvgc;598N-Keg|BGcBx?C_7XL53abr~n^uS^_5#RG{L&>XoiVV+UmFtn&n9|a;o5XyW?IRvFM?|8LQEXHQi`p+syNnLF*Edtv3q5f;)GjRU?IK^nZeoZtQvzpR#l?QwK1vKHkS{8tWp1uQVvfG2aYiHx$Wo-Dydpfe=fP}+rIT`~+vt6`BX_a(g1DZ%dem3<e7wm-fAPTYIM;st(Ov!0mJXWdD-QwBp*{p<7CL(fmvKoAO8~tRA_8dfZV((>o>GVyr7Fj40uY4FvKx+%0;Yj0urtYwh%YKJHbSxKQD}s^irChM5V6v%*sO=S2GO}^fz(Ujf`C?LNXf_0ckFjl%E(o~j-@A+?}Y!|D;Gv59ILD0^xT)nRrl=y0e`NF+-oEl5q_0x+fC~;7<<kv0!x4GEqt=rjeak)El1W>5_h&061A)llbM$p{=^jp7ltNmrK<qHyQrODSX$LAqq#4>0Z^=AJ(E!jGCbvht;?@l%+XrG!!vJ`%4k9(6KegU<Zq4`a*ySQq01_KGffnYu3BV5WbZ*(#8;?I-E;HYFy;g5pG7o<2CdT>ScOrn#4_H7Gq@#KCTg9qQlRLDdFr679%l*~ID(=Wq!%n&4$1PYNS(9uBa*MAOu#iBe#|@ga6KLPyIO67AE71*##yjLM?C*yFxG?a2JYYx4B?He!Jo5-U(WZ{yY=}F6uys_>}PAsyDXlBC4I$mA_v9niq)m*p@q2#WnGq8x2`cH6IU-?@#I!av!t<|wUIZD?v2h}T)MS?wT;65b(}K2z9q_#TAM<Qv>;_hbaXDginejojM2XhTOV+_aN?1lS+5|0eW(i+ZA~+~3cvd3ti6w=%7z|wF|D_JMCsqRB>dL3K@hL9ycr70PpdRSm^Ak(uYJ>vayHCDBS8)5HKYnYf&aurQNlLJ1Spf((eLR8q*@zQehKLm%$2QET0W?>J#cG6>i$rBd02yH_JMEdS#_*mCnaR@K_yrcdwUs$dUDkPh3=JF;b}c-41E1MRelaiMC~cTV73WP43ek2DDY=?70bf2-P6jHj|{vWrK@Ps%BIKdHzFiTI;~?H0Snf}!0MGP+5Mw2bK%;`#P`BiVNT%B;8aHUnMou$J+Le{D%UUp!A=|O_J7j-6+isYJv{jCfShgoB&G*6%V0ge!aBkNV{(nT6tVen*LsCZUa2m{rVBJt+#<n_eGiUXI&>@q8p)WAP<e*>6EX(eYBC#Ph6>y&#w%|EIn6+df8YnV<%0)|L}RH8yn+$xV1?Q1<)jKR@LN_#>mGr_6s&sF4JdR7;#K@ZK_rxER6e9LE;}}O+(v6X9=naoFd%z3B|76P>KSm1gFMWGZ8z+(itPb2LhU7(v;XL$fT+7f4U2cfQSW+73w7xU5OrgfO|SHFx&)%umW8-P2x=yc9|2LzzBLMiqge53uu^#}l(J~_OPHA66uUGR>Z%n!9XRQh*y&c-X<|s`*y&ZpPKQUZ)9`M??W|#|ouQ`Zsf_MYDkFabQW@!QJ<AodNjh_<&tsaf@TI2=nT&!t)xOD+`@?d|7xQG)?n&KL|IdR~mye@gO+R)g(!t0mC())<*BbM#?6-NIC$rF}?eKWpXcY|1%_&btxs~#`Qp{tvEVGSb>`@z2WvH<LdY@;Fg~eD~s*K=qA^6+2L_dmnO$Db_J8M@q0!*t$N$}Q70p_l=0zMLB>kEmo)qFO2jMYtp-oMDH)P1a}^w-`l(+ba`m|yzyiT-?X=6Ytxk-!J)3U7s;-35$cg3)(!lO(n<I0FxRX3jjELPo7g#UUV9iE)A*8Y8x}al!(~r6(5{>--&Y@u}wgqg=G&W|;>Dub$gU3cj*#3hIMbh)2Yimr$Z3g1Y5N5^Eq^Ljj-zitdjw!<K8?=w9U8GZt)>6q+bH38z82Cm1iDt1X2o95`i&;es6$;;&%>XWctgj2eK{%IoW+S0}e(_#u(6vO{iCO$qYnvCV8SVTa_{qgK88JsjaRaM9XKWBgx#RJJ@|GMekVUbjrhUElRMo8X4dcRl1t+0u8q@y&KUG@1LwuGd)Wke3rFI@n9CLlcfjd!N1QDw9s#`{Lu>L+YeeK{nd<*Uh#+c-z5R49O2Hf`!@k7YV3HhQ&S1cEELfgG_#;NBJ?6dH>qv8Q)Y?%0uj`bDSO!6^ZJ4V97rd6I-I<0B1g`^!SQ?@bHSjN>|<DGPMsFj87eC{~}yujD(t-SFF_n3a8Shn}Q3nl31;~Ozjn8itfO|ZY}sJ6#HJek{h>+%F+<-OOLtT1eK3yqYQvHl#`H5f$?rl?A7nZHQ(^wxJ!<&@9E0hCeA2kHy&SZ`JfUb?QX2NfLBP-wW>$o(i9S*0)t2xSNOfps=$jpq5S;hOeyb{0h8!Ki<#(=!0)wO*<acL{}sF5r`{lgI}SXv91v71W?~zeQ9lIMh~YTwN{D!arEYIwPBVtjrnrSTQU?ULFXjjjFx>i@zRZ|JH%#ocTy<q6dZNR+9c<ho2USnH4QA8*$_?8%94m1vGoE-Rzw}rKJsUMKW4@~~)3cA^A*S1!t&;_3Te|oF^j6pK4({um^X@Yygh`f`hI>L8^qAQK&lrwjcF<H1+%0zZBLc*x0>18+X)q$cOMLoy4e9gU_;ofBx8*L5Zm@28!>Guj9yycZo%jLtdbwpAMJ*ES1$T&q1z{#8BMg388{VSdm_H$Ky=;<)Nj5HqS~d@usfZD+wZGP!6><K)=g!d|5Tp7D^EXFuEtS}CxO0ORDZ`htxy7}ZHA;vd^Sv!70mb%C@E@*C3kxtd9es;^9RPd~D=R$E)60DEMhLCQ{zMjm$Toxoav4mPor$!kL8}`YdldzD6_}72%3<w5d$0-Y2a)H5++t>D6!u>67Jv&uIaZ#n3>7kZP3QCX$=y)Q-Yu(yw+8cNmb^sF_=h}$;Q3od=pDOUz_#L)$yS7(R#nyS!Jca;C(t9CkXJUPy0S>31~0IG6)s#J&;{?6o#@bZo+C37>|IC{bd1R$P#l9=w74@zVMALcwnkihR1#1Sp2$5^TLD&axxjpn$$c-%EC=*U#+U=U^*}3#UWEIyVX)TA+lK?0*>#aob5PH4*qPVb1UVLP$#N!2NPBaNO$Q<+IGioNZWo0%gZ0oWgEi`;CMN3<is84vE~NLxCPnm{GT3XpfpqfoniK=@vSHq*DC0f$DXN($jjf8yK1I5`x!Rf2qy#iK;h41s$y{_RwhZkEY4a>~n0rR|DOx9y^>oWlhRX5E?zSL$SYqMgg>*!-aLKs+htq~`wJ~^BP?gqZ{Nbk-MtTEkVVvb93<IBfHr5gcKFq)ssOz_umjEK|8F`8L(eo0&=zaqn4~@FEAB>eR9?%|ekOkh*d_7>vJ>1HiMx#^EB0PeKxY?WPKvb3bD7K(t^_gWgABnz7*_em$`QYw`&_`MvfhgF_dFXtJ06*_A7_9vuC@OIX2pL#bDJR+!{P4-j>Dj<OGtmi|Tju)(rBp$!BSZ3oS{OU>;W$#zrm*i^S5aRCAJDo1xq(cAAQprLlLUij7!tPYElGlcd>wL3=L)F6_qJBH?HvJjJCkowd!Ob}h*fstzkCrAeGw9UkqCVG^JRozM)+lfUxY;8{?G8DBKo2t`XjG&`640uA|d)BA^PJbA&PX*H(f>4*Voge7V7+&a_BYv(6A5>ty-cxBl;1w30o3UCt?_HJz@?2M5||ZBivM^af$UycFBu;htyGOTfr!c3}_~Q>GdsRp{eF<++502VwYhl!Kviqxd3P_WHI+w4?yi<sRSB=dy7|2R5jh~0ANFcn_u(E?ac3GaU=QCjre*azTSvNY$sNbD7qk1tMWz#H5cVv{25HV)h=~YwOnU)MZ3bj-ZhPkE^<<It$L$&uy^$*FQZ<0^mQo4xuovBo_TV1{4FkZni6(9SMFu{mMY3=R0sZa*zHJ{Pt{}XnuD%nJ~H*>-fTh$<Cl&NjE=pAE(s6oYYBH!5F`D{^t(${S4297qq5;B-FQ)#bCkUFXWFAxf732t6wSP-q<K|j^F%GQyZ%;q>aEKfl%pJ^8c`orvAnJX`es-1<fq0BW$`*uv{$r5-SX*#<&D%yzC0i=hUMhlNkTNZQ&G`4sbtPIM#D@Y)XhE>yt{m=OVY0HiURB;5$o#)8m*Q1^f~%R&+z<r(;I$vcI79Bo!q{kNsijWTn@|mKwWrcaY<*L;LG0dP<6PLWsJWBw&<~d;la7g24TYA0C}F#M)!$@Q^FI#f<`#@E9+B2SJIAf5YRibO*8`PJtCCx%BtdH*I}i)`7KHvd8*NqUyZfXu0@%sw>^h#{VmBj8z2`u6?#~ImeQG|B-+3_ZG(bcYov)p6J@Yh2dCGaNaAv(1<sA6AJNZ{T2a(FayF8+(G!w}Ruq@S^^+>MEJ(u1szwZ;AAOc^?!}135yek6Cp4VHMvj#U+>VtEi>v}kb(kiqKA8N-$Ys8e72^UpB__d3tIxS)o%AX%#`K$SgMB=n^59rab%(p2FtqcQG&(!d|1iFra6)!7>uxz1!A&ADZg%PdtF0{qscoz^kj>=-{$wYb5!pb9<b=W|pe1B#E8n6&YND-)(omdw%4a}q3UBP$TQd^Vh^H>im}tcK!1|Q+kyHM#C7EH@v#Pnr=TEq1;)P1)M=fCf<pn5$YoNKo1W7B*3-pM4phC!lSmtX4a?r&db$j8OfQZN)5h^1Jf~Ugz5$~TsEeQnrT>~g-6Ku8POFNI#MmAq0OO!njGY}fdjR6m2%hjo;+Z!Vz`%!8`2cCQxynN@3G{}W71*kx&Gc{RadN>=f9PH<9CY+5)`QEajXCSX2p${<{og$kr=w-!ZL<Z652c43807H<oN*$`C>>^S^0X`4*23(bppy5*pvGB#Vc5Jw7vVB)MY_$V~D1dg>O0tp$VyhKN!vGqFwtMY8)M%5(2h5Cam1C!i|Bu{%;G3T@<|J`@w6qv)ne6+iZz_tNt;6K@t5o&{SgIYyxF>p~38?(%LnOHvtf-i{$-IT@k|p;l)7}{WVxHVywLby&q9z_=`-p~*16}xzidUdMce~oo6xAQqSjW`1-1O0Rrc`2$SY7RL`jjLW1ddK^QD}Uk)Kl#QQgq1I3GnfQKwTpDr2bA+N4poj_{b>%YkvseCH{%%m<R!@P81{{6C!O)OzMaWWI<&gHLCCGK$CBHP)rbn6DJ|9S8x!h@oG$p>P&$yhxHP5fb&#Ng!0y}n0YTj?N7e5Hfgz?_2r)LZtD3CoGd48i>A3LAX`rzquRV!8NDrIQk%aaa8+q2#f(VPuv(wAEz*ErYW~(T!@?Mw7dxN`cIx~FL8~=?XCl#oquL@e?b6t-NYH{2%2@L^X4ySpl={?p^Y?n${GA9x^}gbA|Hj+ww+B+~o<EbV7ux1Bs|%^qwrT9ZXVc*|N|zfwklLqGDP3&KUD=ik+J<r0U2)fq29jl~N^IFy-p)5(^sLM_-cbs*?A4+2xwOl@H!ho?_9Kmpq}VJ8P`6)md%Ccsap7U9uM}{75V=&b5aLBw<6ib>%6V!XE7!0V`!A@`yN?Sh`nxZXmKR9NOR@Up&zBK?8R3@^eu1>SKw4fPEk9nqnSVjGyr5cMP%SU0mVW|JE#qgO18m_h`z53$7{{<mY=KXu5!W>OZX?y*qOZ(q$k6+6j$UDobdFvL{!IZaGu*`N-_)1d7&e5IZ*20Ma2yrCa0XO)<j;`Y32tSM{t%4CS3pPbC+G>AR|c9;d7SfPyeS)p<jznthU^fS#l<<Wh2J#+TLN(t(Te9Y7>EtK#yl+HE%RG29w9fscioHK(THRjL}gs-z4N;W^Sf|DbDSbvSb-Hb2RT1nZ4!CWY?7Q}TbNG2crP<}OT8V!Jw~j@>2p8DD_xu$(~U0?E)}6u$2pqg=SPr>VVb;JbtjNZm?K=m8OUW`RKEzLSb$u@8N#K4JLbPX|K}+HBrRYg;Z5--zHUqxFf0bs0K35z)WhQZOPGleACDkh9>3Hl-o1o#xdw6>aUbVDPu_Cg&EXs8z>RZIhKn;$Ms#zi3y%rn(4RwEuHjrRVmCr??*erhAM1p32~Qze;v3^!#uw)YT>O@6-#&iz92cg`)-W2lDV?E;!c(uzFfV?lc(9N@Fr15_UCsb6|Eg7GZhZLSc{(bOu=3tiKxAT*{H#)zC@QSEowJGJjKsX<@3>{-I0SBEvqG<~^^t>08`WIZAyIdcs^D5(<0!hRg08QlW?saX(h(iGJi(pb;JPB{Vo8ona~@h$eI;3i2fM2JO?xL2fjd4N2*PawINv*?qb+xJtCsXV@D+`pX`6r%5`?-e>cwt@Z^{4qhaTxn8r#Q5y0O;%@W$g!Zs<_QJ9{<uH#X!PZ|B>F5+V)dV8<a(?DKCxLVc`s7m3nTkWXq^@I<LN0D9q3p9G~C^@mzMnZ~#_CoP$lLw+L)BvBhg2+5GE+^2u}W6W|98obFYAF01d0K6P{vPFY+LFB}o;^euJP85b@RYnvtuR9hSIhE<DrqJHnJkAu732VF__TjGMFXfvy(ppg+m!;@T`t}qvr|;p9zK0=H?RKML=kuno#xKtXufxcNamqFvx#8+$g_Z#s7N%)hYvmw^i=2q%3tQNPLB#!>+F-8l!$A`62^I6i2oAWcASD`h`eWosWw9bL;0}y&cM$YKF%@OkL$NU628YJT0niMiT26I>w)F14a6j*VoyZCTTgsIUJ`O1i4Fj?0J|p?hiU{Tb0?_XJA^q+y4iu#*H#<<uWKF*7b@1yJCGxI8(6osVKpmPikg!D$tUS4&7@r(H9@XBP<ht_2_r6<Gt_nPN<XmauK()cw-aYszH<A#b@VW&j#)%X|qJGVQK__@3gxAq^1P%58+u%+qm<8gIK@>JX&Uw*y@BvlbAq5>?QbGx|>|zrl_7L3e#f@*n5D84g%m8i3V47S2hd|YjJRu~tHH5x4Uvj<!IyAImnh0W+j?tvyx)==z6u6e5yNDUKr90jrnn=+^yRgG{2HL=%-=Q9{=tox3nlScc7WBaN5L(A+^?CB5Pod~KwJC`M$fQ3Mj!|^r1C<cV3*Yf#yCE@sp#FJzl#LNnbs@c8g<TRTq<lL&1EQTLwDE_GRZL9|m`?YTB0fw(R7ap}YSItOO30Xg<d;LF(U{nDxR2zmD2K1HasE_r8>l@1R-or4@t0dFKJ5W95FNWq%EtGEl{!&j0@w5!Z$-i@00%I^f*_9e;<u0kQh*ZkWcYPo2m0V2eq97SWqPmA2zWq>ignO6KA#ZqkN|2yzyo#6ncC`BLJ)COTiwOV2W)D=N}N>ook;c_Z?c$|*mtVvMA=?OPz%iUl6^-)yMW(e<LCBbo@QcO5(%rozS9}|4ihcGQbZ|KIMXHeov>uzxz))h>Kzda5&qJR7&LER!8;msFWD1k?KyEOAtHC-aw*1x$l>dHGcZ?)TbFb@AD0I){ikmaRp&;ufU0i@UY|qNxl6}6T769yq}85mXm!!db(QEjOqg}j(vi(~;|&pNu=Py8heCq~O$1=;a6E=zT5sTLwD2--Na9IrQoeeKcq>)42zjB#^^YsJb1Dso@5)eT2$Cfwfs{yGCCfmNvgLA8<%CZHtcx2@0QAP-VWC0{Cq#RULatNleuj7Fm-2fnT%L&{q#QbD;yQtV$eJyyiqBY)4gU%2h1jvH*(DDYCT{=N-dIoN8klZRcizwRRG{Ej!Ry)qm-uxCOQy?UN-7bgN;yt2x-u#|@vC)gHwdOoPQWd7$|x43IYR$T_;tfOwjI@?!%U9BvqwOpHW)geL<<E4jOro#um%i|k6<KIZDA!P?y-`{fO2chDktIBv+#64+bKELauJiGESlzFaUq7XmsP!H4>u_eTmj}e`}P>+ac<y&Kujeq#Z(}%@IQYPYPWUc;~P@Dl|`A)sNMQT^xaj+)Og*<RXC@1Tk3dAE;)?}azCnJ!4;YWv5XnjG`*X;*C669JL8CGZP>*cMfT>>vqil7OCsK<)NU<F<${URcvIEIe9Cd+n}^?&nUp)>b*qHCSTey>z7J1H=Skd~m62~4;qL#g*_v<vNtTU{OWEi=la2P*Wux2oAsfAYwq|rTy?HuNS7f8LSr2a_8%^fhQ`zXAc6>dPjgHr4qnk%%qi<>_=|^wz@qg#TSzb9H{nGL_R}>ULELvgdoY7@=CBLLSr!rZfOoEpqn`X4<QM;<~5}p`e>c^Y$U3t@+NwtwEBvGKNyaf~7ENM2apOWe{Do-~if@QWiRa+dZCf%7_;RRcKN%%t(oPwI*uJ`Jls+wn(cl2hC%N7+<r-WayGA?)Sr1tTin++O5s{LgrQM<k@`EjWs%{AvHc;%9n_C%0?iGgMFwQ0y)+}1l14oAP12l;$L{S_y&rd4E{X?d}CqH7h~{Z&GJW=B@DX*KTY?R-y96Rm!5wyk4MoiXc!+J7cm?kRpI#(^qbUZ>KWx^*$3O#klrVlrMGJ)B3esuW_27ok2wk-mz_#B(v3hX2mRWE%8)w2w78j^Cx3CC1i|5j_42&!%&CapMyci>U;RuaKO$bEZr;+^g!sz2lxU+EZ}ql@omAbK0qRi%1}dc=;6u{_`@HH?&qw`4o0ZB``3>wg~acf4^sNMvy!YAc6%OGbY!u?3m%p+BG%uWN-Pq$oum>%)x=H!D~vA)BHixA&iSmzCp~#3OgWSI=0Tg@T?KK0ZXh@nBm$S;;?azTE(Eb>6={~dbET#V7sRzSHeO{Ox8ikB$5ie%%9$&A`qY!((|yE;)I-zB+2HyY$*&sDC8-pW!G5)PFrg0mX9#h!pG@S;er#ApAczBc>ydh_F}S+K(|6l0Q@c<;5IiTcBgvDFkW^!o{F^;Bju?Yhh!ab1b7!I1l~T6=lLP7*alrcj&Jm(Ngdz5rJ_?E85ZXvlL4?GNS))mS}7&tfSxUuEthDAlsNKfH-GLusEb;=pF?-qQsOm^0kMY~HjS-O;4cJ5=K*n<M%zU|9L9h+Gh@<omyR_WZtxJ6`bThTvn07_QKwKCadZ_YWGL(-wZW6}cx+&H#d`~u%wXq!ru1E(k#An%I&EK7>wZd=56Da;#&{dagpW4dGKC=|D)nD@jjO;&$4II3u}VI{;j5*MdDQz`A9Q=HdNU0*k>7HAT!_t>zS{G|W{^znW>n^qd*37z`hyr5m1df;HNS^v-f?V_+WHVf$1GJ(ZoSR?371VMSx}IuBAk+RD$S8<8Bnm#noEU~Kn^+U+)_cDT&tvbf$G<yRZl3HBMpFj8p|_^7qo+A+eMYg!n*NH1Md>+5O1rm_VIbl|HEfV#s8GcpKE0Wq2Lf`tsp`&Kmgw5y&H<pL5YKAs5)eGk@zP0ntAs$cY*ToP~zx98s^&YhW)@)qSFu52PeY4<sIpWxgdr3RRt(8qv@Lp2q6TdQhcy8^_HKFCaqZRjg8nHY%(pn9)em;ljV+C&-d)whV!J@Q<|AlS|p7PN^NC94-^VBDt==s>%6L`n3>V~SQB$`DM~LVT6rHApeQ3+wZCiuN34>{kj|VcRGb=3Oz)F{gvx$b4&Eh-!`(`DG=%@<$4BNdn9O4p&OB3keB3iXReDUpQntd=#jAo>!I^)KsTq9o*JHj%1h1Ya`Pf!3y?ILVaV~h3<0P%{lu4R`zx=W6(cfR>-`-QgBHvuiR!kMh=DB*0UDbP>Dv*-2?W)Y<SbJ2)tb=uXqV`B7Yt$ZRs*j7>BV83>U${&9QU9Y76{+^PRzAWa$Y6E)_;lg1BlIXseGN(dS*6h?wHHQVfZhal!!Zr4>n{#IN{e|GCO(>g=)bXh;@^BryZMEPs`xJ>5S$<)R2%Nr3-phsDn8;D=&9b%Xd8$Rp@$viVbkZvwzBd>QdvTmv<-FMiQxo%Nl|%Rx#oHf&{WS;L1JWaK=FGY{f5T0C*A`ZSesGKk5cX4-v+$a`SYyTY>Jg*8n_4AMDOYGPbRO&!!PrwCEp8^TC#DNHhX5gj?kYgYr-4#V-ynyb^v(fH2uSDLIJ?UePY+S9l-A20E(r*ctI!aA*Qv|reheT(!MS2)%3mc^OK0$wySS_V#4Aj)?+D>3Td|tuZa^86{ZPYd8&24vh3i2CeJ3w+NqkOz6$6<K}(C5kwCXJW7sSoq}KVZ$ps!v)+`M50LiZ*Rl!qrCVd8E5N2!nAY<HNcFrH%RkK^g)=(-onKhIBIau|bET~6mtSz`Q@x4bAWb3OP-?{KT%D9ak8{~bWa(0m2pZG(|R~$8Zk<>hQfC{RL(2Irczp%xB@Zs}kGq>Cz>v0MFr-^ulxh0FaMLUi;ZC9CFq>C7?Ft_y81jHG0OAnktCRy4TWVd)lYo0Mz1Gi$PFg#;!p;Rwp@z~`ha|?d@PT{Vub~lo@j67FTeSNeXgGT^0TPws2T;UsIZn+Bvc(`0PT#=y53s6<oITv{^N}dn6$p4u8tA6-70tt>D>W3ARl2JcTUmjA{G%2s#IduzmpI}DhJD9DsBfx;JI}!&BrlOH?c_6ddTB971%3pv5-b!BBT3lEF_M!(XQ>$VHVK1`LB!xZmh24!e=f!EchOZc&JQ%8lj>!YQr2|AQeeXEEeybVh!q49%Z78Z(W*)pfDqDrC+S2j)!F|177y6?Zqh#7}N#(__Zs9`-MU|9G@Ks)qBxiym#J~5#i}S*Z^TK%X^5@G4zl`w92*2>+yu+X2Ek6E2jq^f{^FodDLXGo6jq{F^_Jtkiy|CltA4AP2<|-}_<Z!ENNN~|a7VI{a8pn8XOxwx+RU(|Zwo^N?<IK5a79vS%COo0W>8@xyg<0manaMldE)UCR(oM}7N6z{6oXb1SNoCdx0ipTF^+99A85TEkMkM1eQphZcZ~|$Q1GDZ+g{N>?Hc2v3=NIf$^ooyC;N;8vHz(vbi_4BDm(A}Ym61dT#>47Nn7?v?(Pt#T2}`*q>pSd3ol?0sLS<^HTtwrO9l4Q0JR`!1;{-U>d74C?k{IM=h`dqYY*^}Ri~=Xj)SgtTo^+m;bU3b(YK$Z$!7qNsE59t*ag0;yl;TAcM~_G%)%(4Ez!|}eeOJ0nDl=Zj`7hV_a!!a$MoFPW%itd&&WRVUZE-Qz$#2HDu3cw%Tp;Q?7t!f}FYnH5&NUvLlY^tXNDnh7(K(@M3H1tRBrc(LOJ3sI3D0GMahIg3p44-?{(Pz1@Vs%j_|^%@(8;?O&v2PaCsp6cpJ+s(05hs>jl@FF8nH8`oH=FAm7i5d>XbF-|9cxPgY43Zx*W|Fm5J?zuBfRr<|%Z-ttvxVL+wPUQk~YwRPzY4N*S@J1XBqC2D_+|S(<f1sgD99MsO7c@qj|EN)!M{2$CPyYKgK2?hd1ET_u7Ap;nP*Em7=j-J=XYmendZ%h=LKoKkCDQFynjzEY~FwM0C0O4b|IFIz`+ZB-(JcZ5Qn`WI1*Q>d{L;?>tKP;<DngM@NDUM+oYs?hndLZ`0LTANAZpp6%qoM3Y;&))Uen$$uCC9Q61p<16ep9nt{#XSK;0xA0VElIbd5<V8q$E@Q2TV?tW$pZuVz^>SRncak08<$AR<<GXfo9_33p$_HR4k0{Xn14Xx0X;OoGJ=COI-c-g#jlhJ?P{u{Db$SpbKxgY^QCFXo@nhrz7R~+BstTdpPp<R7?Qym5r-#vgr~pI$P@+<bi_T;J+TQY;RgCsEJ0)O?Fh>xJQe^HF&?fn0Uq1pMS%seRn`CA?}OJ;9|o+&hm0G|gfi_8KCQe670NjLb55FUWO_+tn4*v0a#+gX{1jpMqytLLLu>~BkN{R%N53UeiJINp|LSc_(lyDO{iBu$aAv=K!~m@>G+~|;>31s9k2sw)E7EtM=qYFJ{H#cy4E{M9lwxHr7wOBYOI2Q_SrqAeYZ@|H)K+tlz29+|RqNFX&ZAPCNv%Yy+{Uq5Pk?0u;F5u%lbYIFko>$02KpoS{QjFZo61oA^z+n{29ijePo)+6GyG-sq%8F$Y>1DjCsnWqBzV}pOVOlcqDepvb`p7QIFFKB3H~zxj;?;;Q86i9QcMa&Wf-#n8XCb^R27prWm@0{B%0LIYTQu<$g}33W(|saK4&igYy(A~^2@qB(>=f&eFbbip__EWyQ92m`a||8%7y*x*Gaq;X?eoaym2kL%hH^Fi=7US(8Yy0S6t6N!`jV~Nz8}m-(fEu8MrtvL=gw}rPTm9b#XeHE|7h~^=mwYrtC5|fPi%iLO9Ngp^T{V5#c5pk6HW2-`j8k_017oU>N;2*CC{NtfT0=TQ$qE^`cyU4^oXboizA{&Lr2^UQ&j0r-Af)cZuq-V_55^+1xgs?E>Bg)x%b+YqDb>Na`!^UK!M$2Ao@E1aE^4?RMo;UqRH!*Mwv8?ZK@L>IUO=FP_7pyk)KI!=8hg9T-@C@qNx(#sya<uK(OinQ%7haYh=q@;O!BII<mval9w$xH{P9>~R!QH1@di4AX3+(a5Dco~G}_a7bqq>tarFxFJ=N$)A!vPE=g%<->-sng|bV_z3_@<JgM{K?5J4BW7%eE*#^;Cx>x+A9mw8oQI>`_!>D6`FpIKhvV>9+QZrK!)DtPu!(Lk&GgFMjl7aayoh0bAR1Eqhm$>yX%Er@+}+53_{Tr=a6X5=^J^nY#fY*O^JGrXxl%d09NL}hySQoytmi!5u9uUz{Odv7IU`C1YkOYHdQ2>-ho5l&#v8jHCBnP8GSK_0uE%N;Ze;V^n|U8Iy++Mmrp=nF$e7t5JGmZ=1@jwvAI5!`Fwm#2$Cj-RZm!p8gsg0sf?lJ!@Ap^zj%Mk1n6HU^yaP`9zn>=j;Z0%+_MB9&?!q&<O8!z#(2^~K-KOMpoKY3UMU>H;L>Xtzwt30$(y{k>CY?;<E79pz;*R8Y;fk}4O?Wy>LC0CRQI=j8$0h({a@iOe5zZ`+7J&~JPCCn09F5k1IB9g$*aTT2a3J<yjA?>=2Q{~ph33^^&;|t{_{P?wb0V;*TJ)2*M8@KouLvD(-i&eR<93_)zwUm0>cB)d$X)Hggj{h=G?Zz$PWclW(!H}Th;n&7rlj%O34I&rWm3-8f`3O+Vl{SiyDE_a{3A>#CJ*_e<-7PtVz*T?f{HRME6JjUnkiI1B2g|??V9BQM#9rwQtL<<k12DZX4t4KYVksorc<epQ3tT~&BS1fx5w6PUQ!B8&#z+}ID6wnU<50>uGL8E3Z8v?NOpxmm&zC?Qkq%BFm`}lq?I83_~NBAh@3s7+Jwmy@-3#<qP<n?IY}Lgp;FQK`gMWsq*&9Gtm!RrgJp|_=EBdxlVu0wUwS7J#GQ+u&PWi~(DI&05PPJhVign~JgDBV${PI3wGBEQup>l?(KET&83Q7VZN1my5uIVTMNqS1fVd&gcy8G{-KZnUsXkQ3Y*Q|ynAdIK@wICk)(7o$kqm@gE8sfPndNmz5u-RW<0j-UE%zYUh(JAC&ZbrxD3%F!^>{SjqFpaL(RYp~DU%r=&s3&1|8@4RXPae?+UdlDIAcuI1f{4f;|lfABkSGLi}P+3j7Sb8RI56oxwuj(#`N)M$SAD-7!z4||1@M2W;tadi`SXR`lp!4Zbn~25yK@WvW?fedV+~eEQxo<$jYWbPJC60=VWB9`6l=&PCX+d<7Sqx@R5-yrMRYSUax#)Oqhn@E%?YfcsHzCVi3Ha+Tha1+Ti~A=hE+d2_jZJ+gI?zn;p2_(ExdGU1GBEm^b%M?PX<7=T|nTM8&fs?@i$Ey$*OlBVts?TbbuO^__>$>+=U?>INU=89+1Li)`lxd9aSI8M4)PI3Z4Qk9E_l<&NL-DPCkRS{d(~=w;o?nSbfMWfm_HwY-UYKl2@TE}gsg<WlImd2X6%#l-mg)V;6EuWZoWJW9Rl-se;IzWVmXY^|7sp2@Kfa_=FD5F33Kj=i-MqvL(O&_gJWo!`-uQ+!1h%kB<z#`yF9wTIBc5@B7vM<#>}in$AfENIEIhci)@C2K`I_wZH740-mTR=#7>B!qKTJUp(e3}z$84(W7M{!Vj-yl7ok#%6ZHke5YI%Jb9X$!GL<R-tlq&MRj^T9B0DguQ%zaml;4peiL#0#b;$DjG=FI5VeFYfQd^L4#Dk_N{j#x$vk1Bi<3D_oAw0)YLNmJY!KvEiUhlp(XbYD{ABx*I%CO#$AXhSTUvTrCdNU8opDO>SOmG|9STtzWI6EX8@FAt9kje0e3I2i~hf03AovP0tM*JsIP^o)O5btAekXraaI}0b&@bOibcxB!PxM$oQFx|i4cF#s-jC&9^p_{5}gP_`51@N1wbX56jQ<Seq@I(i!$6F=unDLvpRXJCWIdBEgO>oz^H%!NMK71h!G+0jqyzEb$cZgyx5`eEnnWji~Cd)<lv4@rBEvE9dN+UGKIWGk{&1Du|l0`1IoK!(XsM!l&!dmAD?p3^hA(il^_pb^j=ZjjOCWsK%!+)Sdx<}|6k_t{oFIWy_#{8A6~BgIYrGt)+O67Kvw1CtfydGMsg!XfKB(1u9P_mPsv-OKGgyiJ^qQGw_=TWSmYxtanx}C90rA(`bL9Sv`*yM93D7%cz0u~+9JhHel^z~i3=<jurbUQo6NU{r>MvRQT=d#My`2+2X*z#Vlf}Xff5wUBz0Cj4Q-{QMV4>0FXGc~=nh5=pf{E=70(r7fZK&Wp9Q;4yqXO;X23@qs?=j!oDvwsTp=5xO(;jm|69$>Py(1Diu(p;XpR2}I<aPIL)?K~s#hCK!LU4q^#`;^n8v^LQ7DPF&Aaju^>4^WWZP@Hz(mw)V{M*6Lqx_oWxe7POhhx9P_Tn6_E!Hm4N+wZy}&`_DmuxSXen|MNy&A#d!BF*-97^naFK&HeG@2P{;>Nie)yq#xaah2G2Qxy*pYq{KIH>qkipg2%J2@a@BBb2OrllbV%*CD-m^1|j2(MwNvs;nfMV$$J?5SBa+F&gb5|@Wnh(mEzhGJv<-8q+2c&G3^6G(BCLBoS;QheyE3bc7=$t!vNqPn6JO;UDY5pSQ$;$LF4W3;km@gNZDGHIfHy{MNw**QyPE^e6h8Uo-j6_DF&&CG_(|?R|Emvh({{i<O`{AE*4-dYK;_wyM@D8qi^8g-Eu6bvLpJ;t_Ez!(idT4mn%rD(*<B+&RM&>H>K5*o1*kV;18!MVOj?O|7`ZS901ULVu!CHY$KWQkqyzO!IbWhe;5j+_0|4ve_uJm0;s@!7n<FxlJGqM>c$pUc+2A~)bqYesbP${&kz9lAWQ%$Tfp1Q}h=8K`*iG>put-p=jTj<^V;~xq8nUg8)otV&ICe%I2EEy}Sn?IxU4omLkK<?#yk$ZWRR4^k$D!wHIGfgo|B{Zt~F2?FsnUkKNcZ*lJ-H6L0`LnRKFtcXIMiS=A@Ma+iT(&cMH$^39^lt0;++s)kCg}M5g{yRvhY|8vc_-C`^<B!CeWp!}4}<)mgmfT#Iy7!44$3uGeqj2b4?D=*>48|5K69j*gSIMz_a?f=f3Z=AM~KXcqNZ?P0+uz<BCX&gDQsJey*ivqbmDg`9Y=|fAwX9qB_$I`>rmoGrUTK%7FfQP(89Li?kW^+tE@-(7EV~q9ui%fwQmM5>w_AKr_T4rxF!>U?A_X$JX)rcBG*g9pNR=*GQ+v=mT|qs6&6oAGf3%3uL&<iDm6(I)=@y=cE!v?IqbJT3XAQ^px^JrV%xtli!E7nl0`$K(>8LupZaa=2fNJeuC%PBv+$6;wffBH-Df0{air*DyU*Oj<mZ?eojRxw%T{vWpuM?qfsuMU`y%nXj|}Dfx4&Ly>;)>A`jdV>JugW`ZLn#bFk_ENym^`4i?J_MPV7MHPNT)HoY>sm78u~5(j(?P3K@+h*4B!TQ8b$oVgr(;;yY^=th6Ufn=qZXEK;-$^Wa3eG#j9NjSw49EJmWyrUS|u@Kb6@oyGbST5KTY{_FP%+>W5@C&!|<M!J6aponE(lXRX;i#}e-znVc22&Q~{Buk&a4zdt?W5*WAFbaKDObmGKX=3V=4AR0BCWczBBh*4qRiYy_h&9hDD>G%%G2QY4dEsf~iT#RfB#7vAWp=~T>nPchhE6>0Yo{U=`RiAZ8ws@x)tN2!(l5RPmV-zdWVq##k5p{r7{}ZnO@KZ2<2OL{CjH8DSr@-!ENx$wr~Qi4$2bZ(Yq8B$?!}|x5s+0Lcuzf~ge}4wl+GmeVRy&M?wot^exgClh)Qr+zGG)H(>ThKVQStgGs-iMWR3<xwHSw8(6PC*Y<^E62-f9!YtboRq~jkvf=I(4%sNXmf>C@><cTZ0Bz-oDd_5enm?e0qD+lGPj$!L;zOC<0t*sDrU}>(zM--%#T;1RJW-}`KY;_Pus_7D=qW5&FXbj&AsUn%Yqj(jSw|RnBQIfU<5wPjn$9LmZ<Q#d5S8*(1d<<U2m47lJu59UYGY8D2xkv%Mm^H9?H5+cLB2~iw<OfcNQTS4OdyXfYMHR1t$~c=Z=+F!7FyAcpO2u@>Ox_7hIZK5n9boy{nu%6_T&-orX!X|;(YCB6cmo<Nv*Z)gxuwO^tO?PJjey7trO}%TPf@TNlL}~p+7QQOS#e8|CtVNS-1Fpk7N~`@)RO7^yq8K^W9?@`OvJIwP`^SaSFOU@Qfn^0#M-TpfXVjCs2o75=Z6}!AspLL=av^7#|z+<x7L*oIqC(5f~hd9fWAJ6%0eN++CcSXwS`Vu^|eIhlvw*<ne>qU(T}shNHOKAQeRD`r$upk498e=i(^D~k<))HPFF_j`unU(9Umw3zZ8)nfpIk=v$XpoLD}t7LD~9JGW{EYaQzc+<B@#=%Ii-2&*j-ZT=B(jh(^2Yi&ggo>2dX1BKg`^pCwhN?7?WOS*{$(3b@P=vcCdrG*Zs+U&`8om$#~X(R|D$;^TEDxg0p>y;>e_s3kLcUS;CkL(qOGC%Kof9-XNhqFQPJR+kZ!Ku_kc5gvjbx$X{tvEpm{%I4h~r8Y0-Z#_H0nwf)Z5f-w-k9u3k4Zl-sZ2y+6v3}g<^5fmHPD}z98)Sn>7=VT1T8`|F^(Wo2ao!s1{p4`L7RcvPi#3AmRy8z`>;q%GY>iz-+w$Tw>R=x~ner<ira2`~=(R_oYYpnzSNdX!g_`xncI=DIbf6`u{%(D-EJDOfeX$psQ`nhOfeMMpUf%=Kiq_a6?5stF#r-F{W65HFtGd!Zc>jW~i|3<8EhbYIPpQo2vM+Jx4`*E}TpwEV<xnKJ`q4QqHvd%Cm8x*TtZ{b^T{EHr=~s-RDN_8h8j!tW-)L&CXQC;DFhLWgA+r_qteX+5HYuj;oVgx;5>2_Fn9|M_Qw$Z1d33MX{YEHp>=d;;5Vhe)1Bs(1;c4=ib&1X1$rm{CQmkodY|f)g^5ov`Kl<MOZtCtCxuZ95LmPDFVLmojCL@vK=7x4Lg*p?7U7uzm`Qb1bTZ$9TJy9k~Z8EkYQ`Nlj3+<jWPn1M1;~b<Nv1v$qgzc<Rl%X7eJW<WXxhFcI6y>ExeQB_cMw`5kd7@NzPfJf!1Z|<Jy9as3XKrX%x}jm|hUTRkdcDzVF;yohQpKdZs?>mNCOnr9I$OIBmQ?Wbq(TE#9T6jDb)VFvLU*22;Ikp=28mt9)B-}>3)zM36WIlmW>J@lp9R)&0@NY9&~Uo(s<?lhWEawii-U(cHeHO+yIGC_-dqxIrMJ_vDT?^FnpzmnQVVL;2}!C})@!xCguWA_rPb+$HYEzsCrd4aDYc+Y*>1TV0e;<>I19Qp5v5fi=Y-ZHs!45%mQhf}_#~sya@B55b86A(3CdDn3yOGpjDg9r3scH`%qZBEf5?o&fA)b2^DH*q>@F4N6GAz!IvTzrW(i}{vm%ctwIbEiNXcI*B}yYw8tDKkweSiXuA!hJy^y$_3hhj~0}IOb9CaJAPOs4aRtyZ$G`Yuyz4F;&XdCjdaao8c$7xA$VWBWjYtH>7iGPd*Rbo8B6IP!609!JWKvK%m8%-|3diZ1;c1Rm=`U{?|dQiEdo#5{BY6Z7L9f1?c7$6lz2Hp5T=#iqKut>>C4Lnt*z6~nfY?g9qO;$B@On3qAjhnRl-#$v#>5Wz2xm)K;m;hfPNbH<=EcYZ$oj7ZlXqLzTg1S-po8;3fGN7$_C{A2o6F^IaNpB4kr^4^!)^ABD19i4bWI%WZGN3W^v9*rTqIpZSE^(bEFPW}rOD2U?r?}2OJ`>dW4M24M5u3TiQ~%;UQCh4|BiW$N$$ZLWu>b_@mNXXSJR-qSGjmepqfLKgvZ#bYChA8H3)+Kb%z4b2ENDB%X;mKMM)Rnf(OB$V-ztLx0AyRqEY>YqcUcQft?O?fJ2*6Epv&YsdW4av297iqf8qlTt%S(macFmBUYQfF2>#dkG?EJiV;IKhqIb9sEkKw?+pBrc(M3uiOx!o{zd+zbKd+5qVZn6AScc1#HzjD0msf1@_6B4(%}91LW4b{H&cE^=2Ky08CxJaRi65nOYO|L}@5C=OSOb40bDBn)kYmIh80=i4WuQ&NjLE4XzSYQu!0Hs#i{7Orhf^Kb20KEaT00ZEuQ-+=+`%OUGPiF?-NXiQHr*7bgPqV3HDmzQ|KNKY$T`*6xOXM?xzmhSIpj(fbRW5*!|LEdov%o6?y=MNmCh#ZMj)(OMJ6Lqo?EChwegX3=Wgo*9vxe(%9stDquD0tV&TKCM-}Tx5X6N)us1GTUiii{CL)9~kS)HHBt_yG`!nxzEJp&Y^(pmL9*w|aYPxtk8G)AV8;f~KI}pqcOzc-^NUMbuo1;l%Y(?2T4s!w{LdyVq%ibwXR*ZB9XRHpk?-t`-nXt+)TY~#rOFcHTf$zE~22TxqzG14bnApY!zHFLnO<#Y(CIGkar@xk|d`{OSFEn1Z#G-3TBWqs7DoY{*xWt{8jIn9?1nBTj^m&a}VPrHEnc~Ora2q!CcR0^r<N>h6tyyAguPCRFpri0BvHQ?@Lm^;EK}KdhT4Eb`&khSbr6UJE)Pc|Qf&a5#^Umj2n)Da!aXEumw7xoFUbwvf&F1}Nn1g9S&K-;r8qYSu6e`TsiT$yTJy0U>G&(<_=gYGiL>1gIZd#%6rX3L=vS4WVa=)t>)p>z=LI1jIg+7Ag3H!4Ocdc!WGa{`@2v^2OoN%@zSm>Os3ViQRx*w4m`ITtp&CBHKmf#YoaS9nS*vwB4UzPGE)O=0PK0wPf2DSYM`Yci5JX<J|ctKe;Yj7N0CzfGSGR7UHA6xbrl1GTT#G;<Aj4rDn8jOiSlnfvu8dggg8GeC0^Ncz8um#JZQ383bSa%R$uzwk|FzjHt--(0vBZnuy{9%|PX0<kho&TtD(AolDaL}e&Xe%>(jXaJxXb-{K>7r1}tyNsKt**{%ZFfxMm(%{k_g`qcXgG}4q*mF+sz!?Bh&w|n7sJs2`7nXc#`>DKY6omT*pg6@%;6$CL@3t=Rh?$4uf>Jou!mNzp(P!JfC^KIZA@^G;wrR=2bwe?mHpII<-{Y>)slIrL=fIxEwME-;<#JO_%fZ*689*^NYQDHrX*NGx0sAFi6Y|DF_GZ}6vOCX<D0cm5s}@le$)u7fANDC=HJ0sI3PDJ6y`q?VYPVY$byRL+25a<i6`pucU->z`DN0+@@+R~q<vqIvG0hGqG`^!`q(lW*ftxufhw0RMyge+ynSXwjJT}tNM$0YD5Mh5Zb?m%h1QO)veSiJk)F9TfQ0_xc{G(j(~EDRqRrvHvDE!2ho2BGV(*i8VBL~|Rwih&EGYB_k={j%YC>n=Q>C_9{lTNa1VNXZH@P*Hiul<yG3{0IJd6X2Mox4);%9S4&R12%jRQro9Z#Z~ROG2hWr0eNN*&3Nuy!7JJ%iP-LL(%WoFFd<tyPVRBffE2aSR609UBNSbiZl5eJm%w8E>Da<Et5O-v*zJEQd%Rr9=#%v#wi-f&JNwl+jthPG)Ir-Ll3kJuh#)0-|)m*)kngZY~5=s6|}3e#cai^(%Db^GhrPH@*%q0lppExXU*d8^JC^+GX->9X#ho6GRoF9P}z6RxC$i><PVSMNlEqq9le=&D@E8&nk*iE{Q5`s#a}UbiVTT%{ck6Jv4E4&hc#eIxdc;Vy{ChJgKUS^OJ;1puuCT3@F5Y5YEVREn=_fSw(7$OefW_HvH;!wwGly#AhC@6eoOsY{N)%bG@$AIv)M4-zv|(9m~mX2;o}^ar8qT@ec$x(y{*pz5~~P5+|qX$2yw|2bd;D-jJ8)=WTh*w05Qi5q{93h_o8pnvBgPd<ixm7%w;+ZFmg^6VTjeW8I775e=_8fN{zz-v$5=^j9GNglJwMiU7l%a+RkD$Y-?;c5JNWl{1kvG$w^3eF;qnVFkba01qomNHBtY_bbLW>ijpMoWJ=|y6Zc%j=n2F$?j2tlJ+!MRPtttWVuFALQ?DnM@gRWl_5q8J)_X5led@a7v&k0+MhwGn@2iZFOrh5sd)}yS-D`bAnDCgu=-V)L8*z*Bn-D%^tZlYq-dUBte#)8tcZI1qL--H@9@8l>~j{BBccWi#hZq*M$vuc-B%7>&e#$=toEM^>34UrJllcp@SxsO;z-uPuUiaq*MRY0Q-bpphb9dKM$2TBx%m^59uX#>%*X%F-n+!wwx#Dm<2A>ebFH}^d+oI!_tdRhFXJ-h@-yAjL86f!9XcrDA!JA_z=}motT@3aloKPsiWJAOYzYM#1c4%fXdr>YQ=)-r&?JEnS&2xGRwP7^@qOPv=3_nf-sjwN&#8*{t)pG*G1pvkjXB0Y{>S%!Us=y35ctO4=XD~)Iw{{%?BGDMvhtgLO!+kF3&!xa#lT0oC&B=LB{dA_FK3&22yemI2q&*KNv#OWAN<HNoMjMsi<+Puee|_2jb~y<s`PMSE_CN{@*%QJ9!WGx{}NtZF*lv3Q4sf{Q8A!?#XyODTO~5W7-FB|9H6q4(Td{Y&B!x(hAtN@vMpGn#NHykzd+I^cVPd&rO%V;DKU)#2bVAqcH?qG*p(|p3L|{pSdApH)vJ8yEoU|{HP&R1nIb{TlH!fu#*0auC8RSecRb}rgaQC5yj_JI@@i@UBT6BGO7`bzm<`5)ES>u<;mE9NqZKbV>E}HfIKSo%W8i~KJhrO)=tZVmzOVe2p9pTl{+74gI&*~=-ok2taQ!H$OYUND?|R3u8!S^d{9CR8`NfEU#n{}*cT;}aTg&w@wzhDF-}P0*M}PmTirvfo>d%ZgCu*7dUE}i!A~D45m$5r2gKO;04cKCL?rs*lH-=9zY%Fc!6uU#W#HkE<6_H3+4$$-w7z+T11@2>iF<oQS9g10RD#aMgRWpGStp+ESXPao1ZmNpwDKI<_;^QocUy-b32}+a)RY8f$JyuFc5Uw&&V8mx#<sM{4!3;W)nSLJ4Gl1;d3)Xz~LmSF}?w@0Smx&*co=F+I1r7aBY=lqcl`<vEE1#JztA&=XPDX-_0Mj_y0j9|v3{@IY@uN>)o%p2K&}z2gUuJMGW+%bwjD=l`z<hCI?dL9^g<#Go`I6-TH@`BY)50=s7>(-(_Gr+}7fT|O#A=$it{7&5V?A3_Kcz3#Ur8ng1JBxnP!%|05FAky&y{K0L?Y|KZWNz(QsRqRC{8lQUjBxDh{d6CB2F~n=PF_?FqWznVU!`Q;aM1C%rO6Kjfnm1ajK8GP?~I^eWj(ha4wA3T)*!0FnvW>{LBdvYR+DLF}sQO{_KO(--=cy6t9L}&WpY4^kDuK2)ar^$B{Sz(qUny2_TGRoUYKuXDM77M(ttVroE4kK7Q}Fr#;|{FA0)xaaZfn9Xssj3EM1hC!TulU@wnp&2ppkYp_U93UoB|SW*CyS6LN`#UwE0%f2@%vCJADkj3tZgP(YpZMig2((v%dVnzE(EU0BNOEV?8snY?49w?7Zl+2Cd{lK?YRSv<UwSn710QV5@Z87!)wX?){#A$D>zZU}qYrYT~@<5HRi20`dkCi0EFG)iD@4g2~NXu$_xrfTE`ACzx<yCn0mj&xAmg;1aSW_%MTBAT1*+Sy8BSm516_SM$LF<}Y0!iq&AdG4dLB4wX0NLbUI&=8=Q0rxxJ1QAVF>G)Pg0SG+n%Tn2iW}uTJKmgR{81g_cNyYFDKo?^LGhK&-;z^ou+5s983QhW*@s9V4Q~5}US~P3QF<$|L#=U#Jr7H4`jJu;r7-}r?G*Bn;e>%*N|y3dOLYUH7p8ehh}!PZn7THGHU{H=>m$`smcH19?vVHN#psBQ1=x4@#ZY}M>oZ#95U_k^t%?MBu{A{7X_Wp!pch7Ili2uK>9t&8B9KZ(Vdh?S^NK4;U_|Rv^>uii0{exr*2)lTOd~p`N2Xe<x*_E%c-5CmoYS<m&`NJ>-M+jN`G=)d3F6G}#RLEH2D({p4oQ@Tu!V3{;K_PrDYZM%zn}Ka5zw)ce>87cvPSd0wvR>MoN;P5m5_GDhIAS)v?Q^Ieg<Ejy61=|Wm6MT>B`Z&9OfMFW2VQxsP{9x@=Ms=n_03a2#A0uViyX@=+ioN-ikqchF7+>C3fy6YC<h~mSVVzGZy!~Q)f>&lh0V-m0M^C<nTj4WAvxp@A{$aQ={HbS)xaH{|7lQ8yMI)I6q($dq~PoxNJ02NOGbN{^;9cqz>4*N~9ByEGdz4c1@RVO>0$LpJoW3m0<?AQJDy&EeJMi<fHcx2y|bk;tCk<3H-qvN#UDlB0y7n8r;`i`1U~58zruL?j~Z^+c+`S;4S3-xl0P))hBwlLVzWEF(&bnBjVX0N$s{N6z2$dWw7-#>78iD%UiwNbOwt7*}X*k3WTsiEoB7ZyIiRLV)#un3T1hH<7K7PCwk>!VXqLzwPq={>~YRl5zLILjMvoI)V;5SaXke|RJI?x<W*B;)H`XjHzv&23ynL|ku0OwO%$jlgv1&yXV{gSuwq!>)>e4lB2nPa8k`p_H5)OpH!QdJh|bq540u!b2oN5x=O9v1#krC0#gk^HXZ5xCf=x>=u>8=!=zh;PKZoY&fxcQ<awx$DkiH?)*rQ7?8{ZLRI7-9}w_~j~FaC!LietoFyR|?J;naWygRob0g?f}4@=#RjprXp6kZ~UaxZFBX=2M*0wUy?E^m<k}#nK|Wwp_@4VC@1PYVrT=fbU^~fWK`NUCZXxdyVD2>Q?(eRyZ{oVT8WvNWIi@ae&C(v8xmx`SyTzPng94YYSQko_cxZ-6~!1SsB|~Dm1w8v%I;hLnS)PBn$<ctyBKxTigyX&YcCxD8+iC5X*o2Qz<1PP5T~7iJfDsjyJr&H*LE(iX{RsrK%QwWJkKMmaliKC&dzHo2N8V;;CMue8C`R?y_DY3xgq8_gv2ofM%|m7^t!#NUo^d!;HbPs!r{e!im&Vy`r6n{xas)M)|~U*3#>Yuq31IHf@sqb@{~Irv=XaNAD3V;wQF%X2T#XLq?ReRnJ7I&noN2GaCl4$3jN*+DVg){acxE>0(zCfZF{SGHOn(oFshcbu+ihJQ6E+%5Si=r*=ZtX;;jFv@oa?o1kxxt<21g=A$msCn@WR>5+RuOW%GQ6q~qu@$6`UN5<lPt)Ruo(2&1~=v$X+a49H?6@i!<=!A=p=tW}y0_U<5(2A<W_#tdaM}u(3It?dUl57*TcT^^mv^F-NAso0-^MWm!?9dP62w7F~H->-kqmSiP!sh~(H&5kRqqb1Y7i!O8t`*vbJ%{nU=a8mnP)8r{*lD++wJcp$kytY+bfO~h6x;cA?yLS%&9<*K+jaHceXZH9mkoz~Qyus-A&FiTEKbF#9}VuS^lx14t9~;>iIw^C9iP63rB#+wapvJ0Z<!zMihC5IK$v5zbmx`&Y(zK3{@zGL=Q_HZV%Y|`#5#Dz+(GIDCJ&FDTMw9Sd%!J(xB``5l_mo`<!i-n8-ldo5cX%Gig49p8rS1uDDR59QND;2heJosPW8Ig_Enr=;A9F$aM5XMh#D9EJm&0yz`RVu2b@$w4;NFRunsX%^TrNHWg_%@<6nXU_4mFi4w99Z1j9uRl5KuB0uuD~FWE=>mKLEVSSr~h;`1f@h=Q;&#Wbt+C4^rfAi2gq;z$>d+|K(Fkc^H@e2J*c83BpVx{^BZQbCByUB#<3B+qb=9KM9u^QSHMMU(kTTVln&YH8QD(zMY5**>S}Iw%u`RgTSh?*;Ic^XYcGasH0du8dHZ>aHg38abPi(VJ(TyrI-tv($AZBksVI>W&{Tdv7^rq3cRs{I;@;Y-))il4T*Lb9Gl-33OUyWvF<4QQ&nTe_Sszit@oV1qYRjk2C7sP)SFKA@(E3LR#>I3Y~nJk{9GN{GwH5<t2);eCa^^sj)xx#`O|kBKBH2NXidc2}`X2-7O_w*N_F$Om9BUO#hvCuD`V|U)HgsM|08-no-x7>Tf3|n0`b&pmE8HZw=h~srbfjfL*5<Du7c=ra6vyNooB#@tB|ED^_eN@XV^PkCQ2WCt*~~ky?Bc{s>QNx-^W)Z^tH4`tqv09ceeqL47t{M5vt&Wv#91PA$n2b@()rwPS9Mq$^>kUJWGmuv}~s)y#{bP!Gn_?~SLQ8p!8WIRAcJNonW8dvGN+3!<cR_T?^~^Gd2Iv$p;F%lt^A1R+&RDLzD7Gt^Q`o>4D{Wo3Cp5~mY>q^JVdNWFYYh}14gmlHWDo7!e4U_-7%%RBMP(KR<Jq+n?&f$9x~e8z^<5bP5xkJ7}ooPoOYljSl~GPXhJr!{ka<vb%qs<Mblaj~;mFQTMwEC4meuPoHT$cEHaV(Gxl-sMfXA63yO>ltS(%gm0!gbkGwN!W?zBeN|3H?6ax1G}D+kp$a=lh<FLzTeZ=@%*ZvzK-zg2)~Z->(kc}exIk|!#oY|@$vjF@8+-MvcK%pkK{tUPSlS$w)w+-SN_91w&9&Wo1T37PM`h5GqAybsi)xsJ<TtE3gv23;IgOls|p4Sv8VnWo-Q8y7d;MwN=W9M%|9>rd-34$#dkWD`uHyVRjapjr1Zf1`g*blrZQC@Yj4s}>p|@$KmF&zEUDY*!9B1MjTEZD(1^!PPZNn&WL~bC9@q_68%M-=#g0dwwzbv=S3B=37R_590~`CCXnqCS)jw+7==k}k^e;@9HXo~QdDzt>WBsCB#b}lvJU{3B!FY^#24Wb&==Lf6^u8vsW@nrJMK9vw@wY6#beLV0`iE9FXwlbBPmiBNBt^2OmU=+6-tWcZ@fFKp`NcPudwPC_`UfzY=%b^X#{c4v67pV%X?~YoXGZ{bbSKwlBRRipw$-1!GM#F9??^prv=b*cF8I@%c;S`#jh?<JTCpZ6o#)4Y>hxps+f@v_*#x7%X0L<JJbz%>!)PsM<6C+>|LcXPi4~vD$Me5fdi8bV@VInX{dK3W+q-9<3jXrbCmz%xJ^Knjd-v=IrYL%X)7R}&@$|x6bno!HX79ewl|T6vA&$%W^v9mxQ-A5VpWk%5gX#3elM&O4<KywEYz|)`aY}vHhiNcRK6T+0Z-X<RpNom=pS)kock2%i*FJJ_+Mj&s#TVyS60QvI<@uJEKRGU*hI-j2ugo87V@kHMUizz6zp+BHNSyx#_uu>cM*$>zd<2(#{#o}(J#zmuq~<EG<CV}p%IcFf|JJ{OT8{fM(gXM*t=H62yG^;VgZoF+Fdx7)=8WHms+lXuskvrPlz>Ckn(96P1jO-3wd{i$8#M`Za(VV{2{P^LUq5>sWCHPbfX+{17fte2a3Yv)rYg+VLz`dlw?F$kdpArNZqHxBDm@9c@R!gUR0Bzkh5c~Lzk?IUk0}PMe5HZ{1km69-~R}M=PnXqsuk;mu)l)muB%463X*(6J8}-53of2Dy%3Awr8$z^DR?ei1kVL{mU$$$OHZ+#48h_A|Btk4WP0<S^=D{a@bcbO1GrfT0H161<Vz)J6;y$5+|n_#|1^0e_kLE3W>BF9>ywH!!H=v+*U-a9Gqdw@bf^?g(6Yrm9z}Cm{T{`Dt3rxO(}AVwI4ez)N|VG2$uxJ<_*Y(2V+HDU4Nik<)XsK3i(<G|MBY41I`pD!Q%f@Sf9CD=Vb<hrK^*JBs{G4`B**Z`;x^T;`N6y_*DwA?jd0MiU=cg!D%z6>g-H56ZP;pwhyo*6i+P%H0NAiMQ(5~|IXIcZPj4)`V@=zsZK4V~E(+Sz5&DSh>G#SW(A=_d;|+Ntj<``+P+I{-Oy1{Fc+?imbK3G6X;NjN7|V7`-iDZN*~>!E2qvvQLW1c)22+gA9;>YrxmI!tVIy1lK)}f6qDKcDi)I9RqxWnXLeH19Rh^Vy*kG)W;I>h$8QnI$tJHU#FJBNoj?1!!zwmu;`dEEu3inE(h}P`K=sXTBR)1uZc+UiOaVkFN6vt&`bQfXRD0)%0ofS>BVEqc*R|;i#aPH9)AF5<m*&_8iP9;PmI-}4M)`=gP0i>PTJQkDD%Cf&wbXUg^&y2tSqWceg{<d%KV3>v@m?yy=7}A51eLq2xL15Zk9{4WV+{=KaM{DUzJ5GdPf~dgoZOP8kuru$5_+KvF!KE+YhJeT|lOS+_6t24~SAUOwr{YlLJ^Rr;IS1K3QY@P1yKjQ*W8mhF8+B8zgk<yVI0+mlw(lLS;i{pVgEK(Xmoy*^jSJ0mV55BTAMgqr;S$*ZQwt-SLS-^3gZ*n4)Q7)@r=~u9KUW_{V@?^Y$3TVRqpPZ~F^vMm_c{!sP614O*pD8aVZ|swObp~v-0G&`up;MwIliZ_wiO`ksD5EMP{HJez414eHE_p!r8@=yTRQOdgEk0$mUuFBGj}Fo4DTSbYe08+PlZZs7H?nx@e^(>+{^3*KipH8fCx+jL&>#$a57CRNgf<2SOBqR%*Z2WA-1y{&gNK?MGtI+`QJZPj~Fo7@7f^7eVe=V)E(B3-C>;?IN>`IALx~f>Z;cKiyFk5g*@@1JB-c(=f<o-tP-jc0mdVP`TsdiZU0A8j1ubpsqV16><;VMv6x=i9R>{g`{S*5KOCx0Whj2?0|_)dt&B0kQPZh1M#ZAy{x4*TKuyPHOZtM1=`F^vUdj}aG8K|5{i2^YQQ$VNNUcPwm!8zf*vuv+5>n|wtvH4rO&i(?F}e0JngA^YNFHg7@(FcIOb6aNw1AuD%i&i(_RwAz9eHYKsVp9<s7||^!o)lYzBqZRpjJs()YIrT*rYMElnxXD6~MlJ99s5C_n;pv7tyG1kK!WbxHw8_HAG4t=ov6oF^;ZS_-?qT<qmgV1HAsFPce7D^Z+OR#AoKN+wvxCIWTj{BF^0l6E{6z*2Yn?=!ijuM|!|~jkneYWs`M_;q20Evi=Jncr52CElFI+XAA$f4%<SOjA@>(u6JfFhTVnHT9px6&v?)W(Hd}#vvH~zjSbgBhQouQ+LeiT>sB}hObMj4#Fl^e=vEW2IV)IOEaxLR&sSuWKK#iKKif`3-17M#vF&2Ue}JdkX|x8V)zneaRUJ3$K#{cj*(8%h9yOc9VxC6|>(y)_bHm$B3T~HYo9Q&&Oa?MuF_57e$Z`E1e%$?~Cwr5xctFROih9J84xh%a{XEI0uxY_B0qHYiQe;F?{T-9hQ8HqX;=4IJ()Ey=!;U>=en~yi;rC;#=@HvlZzjGNuzyP-C|LvI+Gy3`8HF(kmR-ZPw-tl#l_fo-2c+^A+Ire$Uk#-7)~3u^M(~b(N`Yh}?I4!I$~aNJbZ<=$p*B5;dMqxR9^!xbNeHXfjgRk0Sd|eXof1~{l{{4bR!$PfrH3jmJ@L7$re0$*CL4>Mg-tp}(&owP$lM-`Le$svkrbc8B+M|e19hf`7AAtAc$pe#(MK4u1{?Z?()shfZ&z4)ZRO#@c{(O>QA$5$1r6+-L_&8)QU&S`@}rao`<dHXerexh9wjED_TYHMrr#Z=rXz3Z<QV@oNIobG`6<Ns`39HM9>GL{DIi|X1n%CpOpt>bdzqw+REA&@rQ0M~we%U*=a69i*^?K$NA~zg<4!iusWk}}?wd4+xh?T2NOdw>>r+ED2sKVbEVD;luUdBpu+O1<fX4_E%6Yy}<^;SwWtuxlq@|;8xU?FjR-i{9DRJbhaO4n~2M3cXnn)k%!|yR*lFtS~bvbMUho?A^<lABDi=-?oX>U9G)U%1*6RSAb*{t@`Tw7o@G-R-1nGIS<Fz0}pz?2}im8LS+L}&7gFfp8ji9NECjh9}=M7))2pL{R-=~B~B^4k)-NbD<nNGW!ftOm98x~fr*h0$3*5hC!GWeX`+uF@iPo2S%mOdD|og)nP+%(dp)RbdVRWsD7Hlw7Y_SLJHSpcTaSmdL~DtE_cU0=kNTsAWH}a@HEbjtn(Yro$+PP2RypV`LcneQZExsasR=GL~0TWXO2=NoL)o*qfG0$d+A0R$BMYP8g~dd^8GEU%Bu4lW3Kb!G5M1DQT64iWZusl3h*UE{NYhrZ{{0W%oONrA*2<eD`p{i5SXqxk2Tv(=9D);t&U>2BnWj)g0eI%P{Uc*Ca44wa7|<Q?UG_Bq<qi0?u=2=qh%h$tZRW%rcZusqod6I3*-fqw`caLmZg=N9lp-&5mLLZGb%K(3ew@alPz22_I}bDHWq#bDzRcPCnpzpu^jP_+&%naqu3LWwpggT4-RGzpj|AvTDjwXp2=JTw`yM+78|0U=1L%0G#F4@ftGt1)3E|yj!%s#qEFRo?~8~Bz$g67zUZZu8QaskD~=E!Zv9$$JP|G5$~22zAKjb&Y0{c=H)8zU3Tx4fJrq+SjJ`>R1gQ}PcTN9z;0|;$%4gt9kQ(`NKdXvCDaN`<gL=;)AUzFLte74s%g+dsW@KcdA$9`akbBsdxUqh#=zMzzLE>eOrYv-DeHQ+T7vgFznfn7X|ycz@x+X}IG|pJ7b`RyBWJIV|Lo+aS3Z8+n{LqQ^#>!Gv*V-v^`pYj={PV^4&{u0`{QVEttJgFZ8uYNUS+suxy&6R!I=yfcO?oQbrZ#KW%VOL9NL{n4X$MV-?<D|dtHW00Pamf1SJhF=^}{;V%X2Q<5c~k@XM_!=Ei$a6-j{0cqiAC<VaIy(eEY=E=wgI+1#$w=Ku3U?6iAs>GQi3%Vu=K?P>IW3cqYNpUd`H)B<zeojUNb-qqworQfaPSJL-hr~33t;IqEzb92F&&vjBP2tT7yv%i4tQ<RiT8Gu1G+zNTHZPv<fo>8oq8dT=48wh-;ihc+XdNIV4n4HDJe&+LI&u>lIrRBzclC4%W^h2iy@bCT5r3_dinUV!`6+2B>Xlim!ae@b-RYuE_Ys#SE&a7ks89T;&K|9YEa0<nfe1Wzzeu`eKCK2eV8wQWDndJ*Y4LW?y8uU}XAd6(XC-qy4e1T1t^^`n}kma#tfyu&#Dk@yl1b}rIm2kfOkmjcB4hvhOyj8!nHA<OXR0a*;Rb429M*AI0Lxc1qtqch#7AD3^DA1>i2?FYaa>4e7U8wd22hH_HTyt(>s0X1Kq-m<&NVPKY+{#pj`X>xcvotiBQr;xr2g2E=^GyCxJupU|Kqo6Qm5^taCDO9cX;MOA#zDsGYt{<fPC3ZpB_vhz!+@mv>!v>_9^rS=A4Ga~sXsUnCn3*V#Ni+&ja@b<oFsnYnpxRQCRz>ZEheDwGb{0$2e8kIqXeuHD5GL{5Mh!jaYbfRR&5=%V1ki|#Z;|TS=hXVD=fE2p+maDv6ws&YqrphBW5&`0iRrHmU!~!Qa7U*NCb3B6#w>$y@ekIxdTYYIa3B4yG3Gs5XJ{AROpf!Dl(J|OobSz#b$Ae4I~)6O-l(KR+U41x<?jT%C@O~X_<{H`c!2_bmS%h7?4d3Mi^hd?7w)20OwBLLW$H&i_`<S0~z;KTu7FdrJSWy+K{6r)x-u(LnD@MlPskXNg#;yiaVTb6Fo%`Q`Hk48W;irF_Um)v*5xsWW|`uu|d^6E`0Jx`Zzn7oX--(7`=B9N|$Y97pIUXPT_-j`|T_aVl1HBJH;u|5DhiD31`s()_<rGgw#fvq+U^Q40C4|aisZUWz6TN9mPk>TPwllgT_1y6y%JUsK!>L3hf+c1O-jYH?FDi!=SJD=*NHdY8JCgLpx0h%D=^SPrac=?uPFUN?sCPTUPz&ZkOC{k2+qP;Ip)naIMsX;x#S1%so?y#RUK<I5*q8$GwEW1*IU%?2UIUjTI~Kh$Lk`;#7in!Jx<_d8Q{H?d0XMv*^r=H#wB6RrWNdy>gtY8;L^+#5IBWNVUFbJ6KgXRr;kD<ygvx%4NPGtnCqoaZu{^j(od386n*<9$lGgJ75K4TL$}R(6_C2^`j}P3NeV^WLP6o33D@Cdw{k=El&q}W9>d1n8}pP>`?a3W7S%g2kU_&!B^bZkjqDjv$W)k(@xtQu>`?%yr)ValV^h@`8JL#%pg73X7|i<@|6@!?H0f0Ff|h`_MCt7onzx`r0Rs;eTmq3AyIufHfF8}9;`8{v*OiB=;BKT#x*L=76#=}oceeY6*DAW`L3U$;(=JimNG6UveeB|mf9SPJF-Ck`a6&PKvCff?3dz*e0J=Odf;h!@T+-=e$HmEax4w=>G0RFFV?;L(!;-(YUful{D0@;<sxSB!K8T8#N;nS-vUE~*jX;ZR0S9%gm5A?!ZM<MxA;F#a}hxWs)pJ769JsoDv5T-GPc!VT%?swACNfSz*ui!pisn=e@NE)p!~!7H2E+p%08hmV$p!f4Mx_q+p)*i3KuOyfprZ9{45l}#rI6<&Q%6!2D-K77SfAkW2eMISOfv4mX-Wh9|Zi5pI~CXM+?xXd*h8f_e?77bTYQyDiv3BnAGS{3);#O%wU<b7?tU3?usxpvlunj7}bxQ*+F^WQ+eZbCU2~UpXLf%b`Di{Q*mkS`DtIMa13HZ;(2eNw(6bDP=E+2`Za1B?_Qv7eDj>PF-GA3_!#r3JyY5n4csNMJ<OwwQL&<}5+EH;m77bZ?aEX#`8`~~>1=9dv#D9mrg&*K#YvM-E*E>n=CXW^udQTg!b)e#eCIaqN)s8)+$@)hz#ZB+V5)7cXNKR^d5KZ_W|l=orba%nsrP9Hft7mmT)$YP@=H@C{U*&M%b9(o{Kg-AsVO<2apnEH8_{E-<bU-(ubH+6@%g3hMp2@l<@~L?(F!IuAJf$1Sf}J{K3<mwz?5u#?V+w5wL*l4b7=t0M??#IcX`8oYBKIAsmFf=ZB6>Vt1^R>*pF(`k`kSeJj@!8y05LEU)IHl`vZ^zoVD9l=pFpUbfBkpJI=}`9C5jteK2iYj&))VwY%}-W#DKxzcT%b0W0v@BwZ&TKST>||L!fge&GyS3vLQZ6F=30D;t^Kw*}WvEx1PF@*@3;+JdXR;Mj#L)E2Af*Sc_@X~EsjTX3O)VpetkvIdIb)8>x<)H|d_N_6pvB*>=B#|`yldct`r3WLm4nbdcxQ(E)Y>gbFco8|ph8yV+v9zyQ%srDvpss9jEYv4wc&^s3HrPM<VJGj%!Y}(Un_tfxf!hJ^$c;qY)Jlq0(W=lb;3(@<U3yMu24ub?#;&uZ_ib02Yq?&|*eNhJ7APL-5%S3*NH;o(iL2`q`hEfZIcJ{cvHS~Qv8Q{P1Av5!9A`$1A`A)A`S{|A6m9#(vz^-X|9T4k65*dCu3H!^tOz%12uw){r05W9aP8wxqJwewn3T$SeZdzbIAI*YUO?$}aBQuX(N(y*nQD5_fEwJjbQO4F%@ySmTSt(B0?<vh*7KuIf6g%P;rylSy%g-<K>cmP49P26>_9z4AM3UaH;D^L%Go|`d?Qu4;@W=y#8$YO7g6~<OsWproQr6i_2cI@e0&S`-l&KN_%*zp8{fO{dm$@d87jra1cnwg2#)9ksxoTQNcy$RaY^<>W##xN}9@zrorx2aTEm<ZAE^yI6Ug!}lW~xUHx13qMFF351d^@F+yDX3wWCb(&HB%dHx&f|5a*U2y;MBog?BSch!6xR*89>ZS?Zr0$9pe`bo6vMR60N%pyWlFA%Q3BtD^Gx!u`xE`gZM4@v2jD3R~g+wFY;8YN~hHQdH4Ii`Edjz0&`h6IMW`!@}HxWvchH+Zxg@GG}isf=hnlJ@8Kf(-Xs9M$chAI<PJ#Dm6Y!=Pr9|+b;QhhwO>}rzyS-0vd#8-ad8f13<hkENrf%G-eWUy@o0_I<!N!n<1SHMBS`Rb;HLLEBsEykq4c1{%g`sv`tMrpnn%Nke0Myi48j3%^Bv3>ZazC6(5wp!g_=;=BgIWXP#M$8eJ~9VOBiiveagG*Vz7|u>zGDcCBWOta@sLS>1BccESk~>pTA{r-Tav^Ru8oZ^`gVIOK^P#Xno|h(U&2+zkz5(FIo0|wdfRYwPvxwssttW?fP1pWECRFiJ&n=8}BXUABZsNIZR^hi5oWdgka1+F&swzv?Gd-_w{Mo%Y@8?MFSe30Z|!zlOeXdVZ~S_5ffYM$L3jnk-g5$f~m1VW_7hi{J)kXvgbgS@n)-h$K-2+ot8>#W&NWYA8$QGCg%?^2-T}=liB%I_n-LTr$hqa(*q|THyl(0WBTHTsP)FF&sb!N9g802csXQf>?Bo1SznNUD#zS7Rot^SlgdAniKf3d(Zi6oerqleCyJ^;>Ue%oXAjD_iOdsOQnoZl-*A`?!U3jR&zLFY+GkLv;up8I8>H;??AQ63EkB;ExgksTldBtsYF(Bw&7*ovAXk95zIP`+1SWsWE4M+{$uqn08^3Yu1xHZSom|!A+jtX0F8_X0qzj<(c{7{h8{$wRO#9%u%@1za@}{@?O=4W2@u9y=mjm5L(NN-GIM7_l#Czv0@$J$CR2LI1w1C}e|5g3Qh)8I8gtED>qLgJZBj1A0;cl~Ik=?0BJl?A{Sw+YmbOy;y)N+>n3MOU(Ls8t-6?Q6desyJ*)hQn86gTlzQ!wX0{DBP=lLKgQhL9B{0A5OXf1o2LB{YY^UqVIM>vhH`&=AaZ($nGOIw5qp>`37U7LS!p_wz4TquPpF@KT+mt=;U-Z^Lu=O<b?Zd7sotprdr6`r9FC(8ZG?iK<f!uGnHVss0Wo4y+VoN~ZdorTW{j&gY4&3MRC6qWYU=s=vh?HRbA8^xVpWok6Lvb)17Ymtw!8zTt*hq6~@Pn110!{!g(;-!n0*?tx?=w`CEdZaLgmqC{A6gEYd8*}x8%$Q`lp#r<6EZD^_E67~n<Gb@+>$lxzOAUaEGZ@NWK%^>JynW}f;C-hdJfGA4}f;Zja45*ic4V>a)n+f}1IhTcMaeqS2_1+N<i7gg|@YcG%0mD#F2+`fR!Yww~tR^Q4_rR$Cvd!HaAHM$8^lB!fUHo|MngJvCl6KARiLQ1wW51}SJ%yWGtkbMr^9LVbP-PG{GRzm-t^L-^#?^jy)5p8sah*KkzEQl2L=v;UYi426oHJn7-cDdq7O;kejdIVM7Ta?<c4~5mmZPKsflw(PU(do@-#}duo3X^eSCI{QDyWIE1d8vG9&2me?h)B2c5&Xp&RFha=+xmL`8oPLEpr(wuY6<qTo%r<Wh3UF{qT2VeR?0P)$aTz+|Cr)`%A;G-<>qYr#p~m>;hpNev0^#p>a0$fhzVGiP_lqm@-f(M<?0o*e5tF=#Lpkz2&GU2!WxG9>t0IsPEj+TpsoPipdC7ChDjI*ZQj;-mrW!PKQe9fN*T$bZ7)Tz?TAX+(g^kI{H+-Thclxc>%&J3>NNKXIYZAC1o(DJ5mN^;2DQB$y#}09rAL|Z%Bw0XM_anU;Zf8<{d`5osV>5!yFdO4rX4IY)$i#7PA9UN|ROLFq0~bX&j)2#Y(am=CmAU6yZmcvS$1#dr~&PGNF~W!stSpJHdcVgWCSeS2BG^pAIT;NU8_Iuc)!U9MPNDgc<3B+Cj#Nt4-1RJQxTLn2wDV8nNjsMU%h+a%QA8oJ_U_j;I*SG;!PWiOVoCcMD3AJf|etso{pRmYZ~2XRYu~<!;{~Q#B26|K~p09;vEDo=w@#w#G2C%}MrQSni9vY1W35O;N(=GR%a;FUVg`Y;)j9U)vOu)E+NwiYw0GZf2WrDjTP4GkGG90U5ifN=~e82QBN-Klmty*{{Zd7Z=RDtobtMWOvOu*`0bOX?YXyi`s>?Udvj~Z$hTQ=6zT-C5(=$y(TUyKu}w<nbAK<G}x=olmlh3nW-BMwr!Jb<3hFBtuwAG0Cz7rC#b%B&;7ZN)BTqxl-={Ke|Z71tEf;ml}SMoKw>^!xtX^z@(nkxyM%BY&hT~Q^q_1d8-UqlF}D7(035&{;PV3HxSRF;b@u=psOc|MeBBr~u9o<^L~z~SQHS_{ThP=ztDgL{5jy7#81D>8-#Yn-Y?L}}yGb_iD4;d~19)z56Z`}{`q9A7wRLJv1}m6p6cLJ3s5DUpsEdWIdkoblf;lm7@Gg1ijkf6m$DFsdgEYL|UIK{86M$oSP7UlCG{X(6@q$VAhA3eV?*U1!y(C>lhJzVG6UeG_S*7JNkf)(sMK%+Q6h=Ra8s{kO?nta%JXbW<mQz6`Dn9_6UWJUa%AY=}H+1a{KK(H&pnv(DJMs>sLVb3rhowe0!C;M!3=<*6Njsj%q>{J(g22^20ya}6mO5?6WAy^qPd|3#!7H%vTTOXmu86(fw%|EyL<3rBU1-96Xg8<|1?$U;BY8kyE_J{Oy($Wv+A7nV6t>D~smjeJ6MukhQ7e6!jU@C*6>hm6Ca-#3rpfVT62^bTzpw)aK&X`0e0qbdJCG>sO!I+!%^k^S=-`S77<HdY%%6j(pY5+2%8>MEBoH3OE9{lt%p(tmFo2;-#HeXTwWq*1BK9N6GSfj^dKm14Hd=x#ykPyznv*Rc%m_D7sX?JnXor!6AXu=Q4a3O3JSIh@Xv~rwU_o)&Nk1c5o<Gh_G~VRO3SIS!ML#lQLmp*_2|}x+)%ZE4-%wldl^+h3Wq(v>9@}yJjPzsPqZ39>f>?E&)nOxO#_aqCGaBWUy_=I6c%o*)_{u2<cO}TCN>QARNi7D4)32L<ywVKRPgP|Fr@o6YUac5N&ObYSup&XG&vvuRo?W~jf7(cI(5YE!9B2C*XMfY|%9SNe<JE@BFflT&Osp^BnIW@M6*}@FqTxm|{M}E|vp>N|Ure-B)<Qlb+S)b5>{V49f+A)x(#9m@@pHpPZ2ZKs)tPv>$exhfmxOq#WIw&ow+$=~Hfvu&QPP&;zA5@2@+TVIb~m;qrl3@~kjnk6D_<LQ2i`T(#YzLbcoAd`ELSv)0QHKbXlbC!g6|q5?D6Ah6X50RZqcygYCmhqU$+<Vr2S>&(<g43^*{LN{=Lv^Pqolo@$cEebkV;b7}tkq{rjseG<5NKVeRDN_cL~nHFnoUFU?*i-l(z&Qr*CbUPGD%bKkteRGj-oQ_WgVe<G5&I{mkD`v1n0F4$Ev>GDM-5-;ART317)Cy)u`Xi4YgkVVoxDXwtlJt5447#&~v1Zo8&Hf#<6^AHwSRxOqHCvD&~DSg&^0|_Z@qa~p-RL2g-sES7Cq)DI-Wc3!P5M4fkC>04jH>mT|8|*Pq3J?HaMiJl8>H=I*$`JNgTTp{-U21t1TRwtrlR6$kPhcacK%<fId8@|S_ARp7mMmYLx@nnjwjNJ!+*txh8jDXEa1oTn&?f=N)Pn?!r)Q^4FbF_dABOQFQlXd(YmxzCa8Iose1cZye|n#Zuq8C^>FDn?^oxqGwq6A6r@d79gdc9>O$=a0lOd4aZmi*=A~^3e1T?N=&2&zaQH*~kTT2#@8`F^VZ?oWzlo<xAk%KO|xlX$hs`%vi<_e6H7zcd)6;~i%D61E-TdEQs)g$L!#pFX*6t?$3TJU5R4a_htNH<1KaG0dVT1_%p*%s#gN<Y*mW(NPKURrVf$=dAuhz7sm$XQeMMb$l+*kW5g@~CPrSnyFn?wvuC${EYp9Dp!kE68z7h6RJGKA_4BS%4iEa2LK;d*kw*uvs_&#_$&N;=obwSgIBoOL_37ocs|~{l)B;$ML~~gy6`){ntMp+yPkzfqkCFI<VF5bVIW!_QeUSx|@-GZJw|S*ArIdIu_Zg@^FK22er6l``C7wt;#i9wL7Dz>d&)P2d8Ff<+6~0{Hq_5)~AfqZk9wCO_ulDX4a5$k<*9vU#o1iS}C3=AJATn%sztG`bqpCZ>z}y4$WNscF70aj{H8EdTd$Q1dJ1!;pph1lHVAoi*(CGm}$nULpK7r0V*qSGL|3l`_O8!<=%ES)-ZZwk>p_@Nage#%1lxVN!WMBMzNhS{)9>o9F0$*Sfq0O3*MhYdHP?y&;E05ArY+=x3zKqd<)Y3441_$2JJ#%G*Zth)Tpvss9K!d*jB465G>!-drRuXJa)A;@B_ykiKrMqn5fhu*VxTfq$EO+IFq&Nh+XT^aN+kOXd|JjaK|-+>)-hXU22}>1W}|<VNH9>346yR;sU)9w72+`ZrvC<bbdv1a9s4EE%uh~qwOs}aK9J<q<oC&Yxtpfz@iI0{5y;-=It$~X-+=|oNY{R)Hutx9tn!NoAf~sSgH_!$=oqk50;1ff?;GJA)cU-;%f$u;NBYZJCl3C?qrywdy^~djjxAebEv{F(WGm(*s@~e!K+c;CdTH7&mOqfg^Iz9L^)MBWDRK5tZ{Dva5-W5P2B^&m&_Yn=XaJGmiHk14_fK(f<cU!ZR_r>vwek=Fui_nYN^>!Lm<(3w9by{Z~D{julnZuP#aj&x%Ky0Jxvf9aLTPw*tDRk0c>2dNKEXw{J8{X5)uwhl5++FrRCw5??_b9aD@}hEf6=R`!3}ufg!+H56vu{LrJYzi(;)e;3pv7P0C_7>y224dCIUQRez*{i}2uwjwnvz27ME@djwkL?j3k5K4%kC+2bS?8BJl$t@-X=aIFXU{$D3d8>{{3DqS!TrYnXlpDR_}SeC9CEI(AakZGTP>z%i_qsy16oJGHVDNkO0<g;7cT-j$yTep*>7hMW7fW~@;V7X&2%gh;HrpK3i8YIjtJ<gF!N{?fKugk`jl#m_M<3?KtPUjUWko}Y%54xmc%X}rcmyFi9m5JsaYb>K^nM89R-FiKuAsC}f`&igb)=y+b%YE!O?Ov^Y_|AtQ2?<MAu%E+Tmww=F&8%HSyDG+DlS<??sR>W=-3IhttvGHqtAXDNiZR9~doe}T#75a$pr_+!eqfSm!Wi#lqja6(rtjo>aJK~dA*eSjwNtJ;od^wjx6zBVL@+VfDA5oJ0{RZ`c4tYBDS;eK`n4R^-?{r@i2kA7nJuNSzxIL>=eV49EO9JXlvO{j>1NHiAfpo!!D3!)9b*+LASF2Y9Gt0gIC_<KceP*COA@b^JLR@<HClB__m&8l4qae8XIrKQ*PgeT!g8mQC0MlTJ1WO)Dj|BO1zB^Xn^DV>h&)Y==xuQ_I|^T+XF93V3il8$6p`te9Ub{Y;D1o7F|DBmxMErrSfHSMtmL(-=V^{bnAZokZdT;c>|5$rSTPJKLNE?$g)6_>0SRlM?yd4=>uJhZgwC%xEu@aIcJYVM_)-^;o4TPTL)m?jxcmS7Bu&uU=G{7=yZ(Cnv!tP2Rn@rO{@gKXcqQ4-Da;wVXY1T)vY!)q-u|4CoMWb6iofihy^!qZT!wtowPgRQCi^`?%pQ~4zI5=WgMq~|Ci|IsYtl)wUlgonuR%ALYNr3X((tt&XaC9hF@LQ%h-DJ3zh4`11Jja6aEctX8<y+c)SWRA3FuODk0Uu9Q}L+Q<rY9CoE>vVxW}2GkU*UcrHe8>?18}4s*C_H^59IkBULw8?Rad0cG@3z$OebI7U{nZBno9GCjj0@WgCi7eAA&<`o4s_9XRyqNF#bH=Y3@K``r%fB}@6T!(lfGEnHhmBXh58*&qc$58Tgf<yNd*iO8-bmgUQ{ZL<0%B$Fd!wSlGE<UX@HKnzryO3|8ekc$6n#SpAimXGX+B9UD=bIv6W!KfcY+9!4@$J9uOy-Qi1c~mOP^<^UOthGb(7i=~|KMT;0JM1-sy0(HDg#$#Nkx$yQLu1DrljmM<r2sCQ2##a8Y{+S_;ib%4<b;N>YT+HWOj)QUi~u3HGaa46726Axiy$%v4)b1{FLNM?JBNC4bJc*Pekt}BHS4KAx>*6!DN7-l`6gLaSrRWq;g-9B&oc?<B=^GBPk0cCkJ*zd8-YgI22Lb6A~T7KI_2JGY?#QpB%6#FTUCj5T1G)ClHe^yc@2}*E%)w0JJ&z>$_l)bIM0Wv@s5;JV}Un<MfJSKn-)|-h>|atc^P_+T*(4(T;2kfUX1K;cT(vMrd%*u{(*ADX8BDj)GEDK&3+e-mfeRFd{*EMeys7biZ8{A6#1nMS$m(Z^k&Sp^_r%QaSn<Atcv?_NxATbsT(vbc!*|qjbE7}4F;+qz3y9yU$9eAJWBiMn;z$UTPc;_l0Vp+5)fJfmxlc*n@_IF>xJLH`N{eFz6`(jL~oU1PM4U{&`E!lDQz)H6^NO0VN-SCr;vu2-wsUE#i@F*<dUXpou^O35$K+*O#Eb;t>J98))Iqj+65e8kcX1l5zWmj&ansrl&vp#DBavc@yy^=YP9W~8m$eH08ddS5$PTM|Mf{++v1OA|7E?~-Mf3Y+;^<!`73g8hY#oA4wyT_v3!LNZhxJ`XZ>j%+~0S9dBQ=a2iL`lgM2dsLH<$vdQqp0*tqhOkHv#bNCXad#iwKuVPML^8<!ErBO9uK$O-I)W&bL^)n`K($)MF$oSGzR^9uMwlHjp(>mlf{eX6SSI=&4xJDij*`I-*cDWl1{bVv7)f_ReJYxs+TWcOlt=-t=$cFiDr>!>u3lqY?bC{-q=dsv<#{?aqDPs!#T=P4biUOGg<P@SF90N5>qXxf#F%fz)-{ukwd>r>Iki~&GP&rSkO(G<%@uC<8SM;dT3YfH25_ucRM<{u{!Pi88i88LY1$&G^&;>7Hc(wxq*&nvzwh9G2&9r(SEmU<5A6xcbvo9Odk;*jOSYdmY7+7fpGY2xw~E3$}`|E=YcmPgxS^(y~PFygt-8{))O+!hQ$;7lE$`YbcitA?Y4%SR5KWDnvU;daK9tMX0d6JH!zBKK0S_d+dhJ7hS`U_}eczv(FF#rkq1dBZZf?u6}CBAH*B>vZBA|5mx}<uQUH2dW}WE1r<{dT^BI15AV=VTT!*BZV+9Y<_=Z$+#7l%c^|;mctu^5Z`de|KbN@%|59SFEMA^m$GIXGZr=x=JzyPbDU8VkQZ}IrjPv#v1-7?GZO7QHZKg^ab_qqp}iwjEiGl+ku!`RnF~ybnE8&C=yG7kUQU9~SV{~Pe0GRgJI*~|;`&s&O6N>gKx1?U`0T*aefrPm#<O{FZ8e_pM)MJ?y<G8-r1hEdKPjdsbvwET2r1Bh-hy=mm%tFFp*d1A554Z*a^GTiO;rMdE%9aT<LnJB5|QYzFgHqPixLu;;6&D*U|MOs&N4MWOHj=76hY{De3%>9Dt1tIx!by&;v*gmn3ZNxS!b4b80>1UF?OiPwhSad*&v8qQtGr^7*S$WTcI)?%|1-;2zn+hhp#YIy%?yKU<TP1qqILvfim$+a;-iIJ+@}{G>Z~0sgf^y>rFXMb1GCtsTjt|rB;f@<Z|tUfpZqspU(9iBQl&h^siaW*DU4_pOg2#($!!0-S^$WUnm$s75omnM)qX8?I$9Th8Pk*!XV2Scu^rx-mX(2mW6uKz^PK)4R!X-15-#{AfKZ3jDjntHsVEAb~>e@Le-l(OQ5Xr6@b=BOAM2^0dzQ0U8M6BYcyp^07@;>Y9Og~G4(y+FZZE_30rWB-5Ivm@*S`#D}q<*T*KK}j%Tt17g_HA8s-yO%`!=kmD>Fx9_8bq+5gs$Mzh6vBJSBv3)JhM;(niO7OT7)iZNczXsAsk$xguy85!WeT#p4N0`@MTYNw1wUNl%Rk>ROAajmriyK%KvNM}6H*1ZTxDR(oY>NZkjQzY1YBq0L-$1oX_AAZ8+;$^TS9{+AwZ6WJl-juh}Lz#MIZjuu&^6$5Rdcvr0@6`$yJ{R;gxi<$3GzR^e1k~BUto;Fb#}We?-4K8WnYu!RFu{sFQgK%>s(WlI#9IIyf#C8$3>s`%>|JW?JZ0e^`TAxTNK8qG%ZI*dSZ>SeIa*_2xwkh&h~WIUe(&8ek*3T68Hb(je`%c+h)8*m6dTtEC$GOgeZQx#<M~xTeI4P~5q=%v*Qc)|{60^^2YDLa`Lp?5-pyadHGk=+AIX1souwafZ1acvuKb62Y{NT$Ha+?Doj&`AXJCW>QcuGNdYWJSR9XRk_H=$#dOE)A-{I-vv47EHlBn=;)`OS)y?F5W;yaznTIA3FTFEh1hLvbfgGzR>R<ix{Sjm=@>*H|xZ)C3_Bams)2Y*k(7-iqYpu_i&drGE0fMPI96DSf>Jr&e5e*7o?I(Fw0<{eBX0*z2r^^&ZmhD)=5K`pcX{9hGN;59eXG0e3t4qH5JE}u;;UnVPj>9e7)FOC;qWjgJjvW>GVmp+ep=ufYlReo_NIJI+Wly;tNzN$w%i2#iU@D(>7)%j;nFL<qXAV10k%?BB;jF-xpGhXxJI;BIZpE)vi`I?a$FZ)P_b|Z3HT(CXxi&y;YS4=-){L<+zNSJkY4VR{YKe=nOr^Z6$tF)Yb*T^%(m!P~AEQuSH%5^oTOWp^r1(h)EuU<z1p6dW~TlRXKJ=I^aZcWZ%s88#ISWo4e#Vhl_{`y;D#=7u&y8K1sQ|B)qV1MiH^%s6rFou`2A8VhA%WsVC=?ixL^nl>cF4Di~vge~6;`sqYx3up3myUN(d}nqlgU+~X$4sN-rx(X*V5DW^(|W*sBIy9VIKE|+YW1*W$|Ci%(J(!FoVZiyX{e`NoG=JIWoJA8IoE#a;@8E?(;$Sa)8Oj#m<^!2_>JN6yXPYu&JIYi(f}>SBv^SlPKV8hORszH=7Tn#VR2u=Y)r!01HX81`R_%UHTKE9o6MR@d~=yK>%pDLtZmr03{H$t%|DA}k?@=-;wE)O$8<}On|fO70!meH4aC^1&`aEsuTuyCIGTaIq??M+XfogGQf^QP?>uxr2C@x$!e<XYCLV*vjGgU8&_*l9I9H-Nw6OvL2OLK<+UHm`&>}?-=gtdWY(S(xBc!ti+tIse62FKI8Tv@5{?SagZSj%TM>S;{0^K%2dw0!?A&HHBFTWaI3{WK@0A!+piUbgm5)q&gRwP3*-e;hhUJEU+g_hS8>g&_j5q=%v*Aad#w7eEtUJEU+g_hSs%WI+Kwb1g1q0sVfMUncc3ooYnp!on*ma(kz@+!;t!IxB7SYIjsc33t(n!2-TG>`zwsw@%d5H|UN`c3VR!I{?kNfp5oXJfu+k^O%`xdj7zp+=GyH4+tFz?(N!IP8O#(pc7APF|Tm9kqI&tiIHf``NFsk2odkt+t_g?w6IAu&Bh$Kd54isfcLMY$W;a&a1OWC7HzHf!>Oj{%Pb@COQ2T*{WINZx6HIGTsFzxtj65T)6((?+w0Ea8HFLn+Dk?ZBi3em=3c87O&VZ(u<~vaQ4>@JH3OJU7c0PY<15oG3NyyD-0|Ks-EAwu>e!QH;xq)cI|mdr+I5T^Vdo^s^3gm-C1%x&dNC#vejd`Vpg`XGDCeD{M7=?<>H6GT#T`&%~S7QeCxExQ427BnHjH7gK3QC_blE#aXsM$S9{^DT&oLbrJB&cs7`aWNE2PWUYt9>=@(~+3Td-S0JNn}$}ql;+xU@dWtj2Zix+me`Z7j3%c9hDL&KAI^Llya;@3U#sh3t?#*Xte{$5P%3w4)xR$>Vkiecv!m&M;}g_dwqX!&p7hadSG4d~8T#*MUaWV)s#Cx{Be1&YE2IX`;=`-5>3l8tlXB;1Wsjg^hiX!!?97P6T~41}QNKWRFHF6Id#|3n7bk>h3)&?qT_LGgiZroJGuz+>ZMGqo56z3l*RMQ{yTCvo!ou5uHIPp6**c{uPPLXyJ!h6}uFA)VEddcIAkB!O`x2@F)gs4a}~lS{7rEAFrR;iugpfDf#Dbi>cG1N%0nCPJ@^+|+|J#7B1n5J#D{kGkjJnhD3F8rIzqL~We%ofUPZ)uE1dFcB4}{Fd=*Fj`+}0E&DEEXlhN+F0KTU-Yc{u?2T0^^+SAj|P5q&-wM{h)vpBfCS$-Qcja+*!E~T->Hp0MB`AnjT9GRbNsE77C>1LsnR8I`013~!Uas(e8=I)R!GV4TD+0+-~UnJpaJbi^9&8m*dr=wyK5cF<ZkuN2VtV2osUuAo2f~8J@5H@A&ZeZlp~jJvJU0-b2Ky_tm@BqC}#?9G;CPEO{UK>i=MdJIV*3+=D!|2h}8eG1y61*EqJYV(jR=xhUH&&|FIu_-aS5I>cze5wcsDo8z<qz6?}P+h_qxqlqg9S$$NRdCG$(?1ebc`G>Kv{Pot|2B;Ju*=;4NBgY<P3W*Pl?nN}^uD{M{$&{o}nC|%3~S#0Gu;4Q13wH1|dC2KSSr;67~w`6%AowZxv==O3rrLGh1p^2aYHqP}uVo(JiV!rh-UcLrxXh}@OE8yTn7VI6UC5%AbX=TUsum312xcB9i^+geP*|)MwPfQ^_nc{%okcfMWKF@o~UV~tmJdOtsmah8}(YB-m8$erFUb!vz^dJNUwnwQ3q8XKU=0Hijd`W{DilhJPha6gVPQ%`ggGx=ci)s(?wvOcqs{@9Uo1w{mT32*Gh-j2u^rWCk6sy|Oh?T(zpzL7Jzk_5l`r%i&lb}7=2(bcg`h)jvU3KN@5JR_dYszwzkKAHe_%^$ZI*-8|?K%qkV2LukL=tT0)Hz*zdMIlA%O7}xE{8D8hcKOu-)=q;=OZW10U~d=)=6GxAs+9>`Bz2}x|}4R>tJ(+#;8d+?ZW+z>z$OYn4nv#3~&dyE7SG}E?6mc#ya!V&V4Maeswx#5QQxde(^(&87VYRhV6>Z2sh5X-$>M+ngdxf$IVE6YQrhVX*m%|WxJaVXYhMY#LWC1E}it~hmoPF4gH3vdgMO3!Iu_W(UV4^r)~s@w2$=GMokcA<MeaN%*H;w0=aCt^3=M+Pr6@zsnpZ=Ags{cIh`6*7(uK~E+6<C@KfB-fe`>x<q)KPwL_=4FiW^`(tOG!CMmBxApI2%+aSq?6?Gz{u6f6SxF=VwcvG{9M~4HWQISiP3HD9!PJ}Z5BwA2z!Dk7ZCV}FhsyIH93>aKl<#nnEfbDicLO%be{m!=_pvsjaUz?_Kr9F*xnty6-615;X`rBU>rv&Gx`I>Dc72_mO-${rYQz)Lgo8pwn*jOz7<5=d7yH#^yH#t`wSu)RvGLiOzazL?vr_2(gfM-kpoHSR&x{iu%6vvT|u&IYB`_e@6rWmaR*_InGRX;CXV<*DRs?|rXvt%swMh90ewk3<yhQ3{I+HMlEqIx#D?#Z<THO5w6Mlt;nO5&2jCFc^>FNBX95MgMmy?p_v#ClFMe}z-RFE}MWO8EE-nveOXpVS^HmvMAW+2?NP;onwiNMQ`i$H`R_DLV*lyPolXf}Fi28t%#VMzc2*Q?x6F8!HgnIt`?A9+^JqumP}mu@7s838MD{n^f5(+9@{i)O~*>H}sxte?8QykV?2CkrnQ(@(8Va(_#3Fg}sBzIFcYy2t&1!ekQDabn7ob0QN`TVBe4T?hC5tfb#0!cfaSGpT}+4NC^|16_A_h=#OF@eFG^D>}4x%LuFDNA(ch{85mh|tGX;T={=E{oY$<zB-;;^w1(iX$S@MHuu=?6fYRE>rC(jkQ`;nxLJ>V1nV+(%@GPjClfj2JVp36ID~El%gq4G2nW>@UP4V<d|D{|5Xk6mN8u-0(svBqUP^q5dBB1<Oc5xc>;#uO?b@X(5lA4vlMDs`{aU^-P5v8rr3?g=OPcrSYwI@o2w<tj2{$sI|ce!Q6jLwM0r?oPTo({ArTHEGY4*AbMxS5?XJYAvg8AJN7lDcPrNb+P|EeGO^x<@isU?QB0VMfW*)4<ZY?&LN!Gs-~f(Rhl6dcuKQ^1KLNoXng`Y}fWW8P&cTRYdY!mv=QskV%@KdTg^Wr{%kDy+XGvp>8gPmP@%@*kLAm+_x6j%uOg3PhYkJWa0LT+d2~tv^s}Xo|u?^NB89cbGpRFJ$Y<~J4w1bGPHs!XIJ*eEmlr(M@!hbbAj1Onr=xUZM>LP_a%5TaU@uk2NJRs&tqUVCf?z*k9f>v$lkIy<<@=MYiot){cVbQ<y$U$-PIPO{;<Y<UXgq6sEw$c=f-JvlpFlba(NFhwvb>zCIsG3$E+^p(aY-?BoNT=$($6N37~VLomPZ9>!T>sso0h;Nl*Vos_f#rs;RPuv}4bt$~c>!&z5DQChg8W7-h>Cr72-X`$MWxW0;lVStQn<_atLiX{iHjPE1g1SoLGLI7xiEp!92WI%DoMzHncA8|EvG%xq*0S5(hc*IaOAaQ9XXRg^v0=d%i?WQV0o7PVJ<3b1Jnx6JtlR`<F1kb%!)meu-1AO~xF3-RP<NdDHRs<kye_NkfN(*N)d)3ztK-_Oz7?<f~-lzvh=TeA8kckiUXL>~SbvEL2TVBezkgvTRpzr?#uU&lx!tsexZU4zEYeeUK=eoV`<8-?k5I8c>}4Z><N>01@=jmFPpE<h3LLEYAk^J}u?Gsn2thlV=>2)V*NJzE6*VK$X$;|^>vx#NUwIVq4hk}{vB5;x)U2)h703D-B{JgO<c=uDV$H7PQ!W#_?Pim3!vQqch-`&{CCScTOmpG0dvs=vulzN`7muzeuXzGwl<^{=mp9e^FO>iDHm@<3U}OTpZ^(l&(;x){Sn;R9)mrAsW6it5Np+%VlEJr&CRncu;TV`Z77S6@~}i}cs&JXQH1)YfQUdlP{#DyO0|LIv8%4Ur_I!n?7ZJ6$rAmtB%YoM+s<l2W^1D1&&lF=CBsBCwBFr@5H%aGP4=eV@aq&L4vmJytP=ndVv7oh^lnCbe07YW8moB9TJ*l*P#Z^?k`y8CEh}vh{IG2jI-}CXwOHL+ED~d0ZC0rZF=U8O0J6<9o6iM7Y|_6PuHa_O+#uM{P?P=xH6`n8wX)^f>)lr`$KP(fr<#ZI$4tatLkon8mnarpI~BU%DeS3x4*#<}bXsSlwMf*yZ&@Sg9Q-2~Npr7>2uIm-~tv8cA74i+qijH3#r7{xI;e{;K<J&Ik!%9Z`DdtUFaRtGM-2XK+v>BRS^4PEJh5y(!RQOMQ${DeV#rF#EWLQh>LTlxVT}ZrPX1i{H^Jd${s?H=FDNs_JYz4c}<U!n}qz3UAvc6v{5ega5J4*}YBr=eKS;8*mUQ3}o|fsp(K0Tc9Dx8L#L+4s=49@=W|{q)R)>Ko4*s2Ayghq$PpUX@}<1DAI4q43seYXn5!_YV(%2ZWs)B)!cmg<IjuJ(iHbG4gC~4$Er`aSisAwLrZ;xd92)wg`1Tx2b8hwReNBynyVBJLcb_KFwxJfvGlh)^3D#bJJ<5Vjg|`QQxcm%g0RP_Ad@MP?G<#EkmT8cxtuKas8Xa`+=`?05g;(lTqZKz2oi4T<F1Q6Y7m>IG7~qh`8$}PmHQqR>8=Wg9N2q2YKN>-?vQ%L(}Dkxss~0V2||l>>JoLUoDZeTi;00M5zQ1<fNJB3TCcw5oTUv~mV9SB3}VfQ_*q#X=9hwX88ZmUh+ow(>;)MXn2L3N&-AMs9Zk^n6A>!lMW!=~B&vkw=_ZC9w#|k|Q20bS3(~|odAc-T%qE(cMy%3#oV8*3^hUfBG(ieaETW+k;-@1G>)i$C>+AEs^K%l(Nlf%~OqFRC-3&D}>;c6Cv~0ri<o1|)VC46=x8lWbC#<xbzK_c@jK>H&8r-F8o<_-V;&No>$53(*e?jaU+W+sR6BCKg<=kvkShE?51kMd=l?2%=r)RL#u;dK2g|;{nJ1Q3_ygVcD@YXxef6~XB+T<m0l2ogbXC}2<eM=IrkBW`lA|oVcr9e|-Uz9L{sReqYKoB-xpqYBwu3oTVYR3n{SPSLMHDRBH1HlKnU1?Nd2uX?zl2tCjqf+6?rZ(r%;ucXOhQcR$C04J|?laF&ZFR_1Z*VaeVp3MszE_Gb(T_A9rU7#@wX2+jtC}&)8{4~bf2Mh-k4Qp}S7O&--$g?2>5>{T=*$iaI_LP`cvalR@MujXi8{Ll&<VogIMYL!{b#qPEbh<fkz2LR#XJ6e{0-CkxrGxG>6irZE3D`Ru==X7RGD|bM;<(GOYBQmqE8SG;$=3is)k4v#)B6&EtzP&ZK`<_lBg`AJKO|Fk0=>!UM~)NgAE+ESk(C?xIhiI^-@(q!Nke{w6ly>ezt=+BsnuEl$zjE0=6opH`dW1wC-5IpoynAYPk1MBLy-cA-1`1T)Rq5<7o}h+<}DR5nu6LEJ#{{bxOT(pG+FjpDsRWaiD+N@<>otF596}Q8_sIe2H}eiMu7CQOeeQE4`%ZX#Bq)Tcq1Z@#*AAq<hTEKaYUjZTzGYI4N}dgL_t_8}G_D>4?8Xy<bw@;et+gx~S9befjyL$mL32x=hKa);)*L@=|GTp3~_@p3^fsN1)t^R5#O`(sx;TOFRy4uGt+p69i|zuG8(j!Lex}FpMSoSXHTR7C8nLP3f8s8JDLW?HQ5oa@5)y#cmXIuy^4^syiz@VS(?XMks&q%9irVmh#Gj@cQ(1gkMMab%bBpQeN3oUfEJ!*-~EFQeN3oeuO6ND`CnjVaf+4OhK{_{c4d(S}J)1T-KpU-LIH#jjbg`nUFnUsTb7nCCn)X99@#9c)#FJ@iPK-Kc~Q8lb@dvVHlmt-p}aFuhXgc=U*AWF64=rW6qV1I^W2=;FrAVCuAJDNB$D8N>h7*$J5R^S!RqRe#SOpgaty4+=yX;DKCD_oL$8)3Gc_JBf-kz7bOBmu8j;Yn~Pc;G1Ct*Tx(M0Z884SFpe}UVyu`mt+dRlQn&bo3#RgaPlPhl>;8#@rzs>A&IQ?uzc52iezIT8nTa}QHWe34D}F|^;z!#1&T{KsVaP5K22%;e=e#Q3&B?Rp#Nkizs-#N{?r|i$xx$72#9L1i;XlRF60Wh3%vjQcyFyPMPDnbg{p5=m9O6?y=Lu4kr{A3}>5AHbKjYCqVg2yW5v-iE!n<^OhLK~%&&cn6xK4f_?6T){>?6s}oIT_+NBgC7j<1AEJTmi(yvT%d<$&O?^QSy}&L`e|;RnyjYew=E7bdcQzht$)%(3z$>&lDBRxWef|8p<x4tPZC6Dli@MEcyK^>nyLrH9ZF^pms2rM%)d+Ewl>whmU33EKw%Y|DekvNh~bvfHa7!lrp)If&SI`5}BJ76o?6my;Z7O)cD#vfbfG^edJf;mFz#+w~6t*j<_bN4$$deO`HTU8uIq{^h1Ni=e1zwRDhVfX^QzxhkLkPu*WZMF|jr2v!kTQ?$hr>=V-7gZlr#=B}-jhdVS}h1TT*_O6!IsC0uaR@6u{yFLj81!V5P(PEDr1}#?l3fToZOeo2%(B-fqIt6?Js1}8r+t8xlKWw<6CUl8l+gW=r<)89nwp{n@vS#Cj&MfZ!t!oH<i9}YF1CAN}M`d`9D2K62kWiYgaZQVcqcTa$WentvfO1U=>%fsqIFDyh6!Q<DXV+$G3^Xk5v0Bzd6#m(+hAsFQg;9{Ei>kN)qDFb6at-Nm2gxL~Y-enV;bBdX`a6^^AY=jMXlJ2IU`4pql4{x6hH>-g7YghS3LxrJMc;@Qg6lYLxQnDsOJzp=l^3lI$V->`%E@}q*5hE1<@SykZ&d1Hb7!^0&Q)!nz|NLU*k-nWE*x4m_1pl)%Id$+&jhDgNt@@q<y*-Z3EH8&6gJ72Bql$W9mV-}B8?b=;oR`L_x&v=CVDX=%coHQxt{~M1!SxFEpXd!%JDtmYw9q|m6xK{^~pcMHk5A<)@HjREz8iM&S^mHDt46m@TLb~17+2qvLqsbVZdb%XyftX`}6fdRH@d5&&w>kb;63O`IO$#(zyNB^RT@WGO0Z^H!d^Skn&?SYl!cNMQ7EPm~HfX_cI=gd{E;%tMbI}@jes1K|oD~+X@=VW(f6x69=M7e3#W0&SG{0*Sjn^AUz$PmUSUoi-|^xs|fb6jY5(O5i|140G80!R+%j<ixEgMPDcNWqNu2wG8MBMQAe@(O!}t??6;7i>q;6m?}|x=+-{E|C1Igjj4^EOr6>n(+M!&`FM-bG=iDR7oBBsAq?__1{;^`bodnT9#*#4yZ6Tot18|Swo?r%2IHi49Wp^XeB{aE?$P1PJMLIyim0M#`7>w^Q2?6+Ra>9_W2rmx889H@+!tRxykT_;5w!^MDc%MJm$;%~`3y8(Qk}J&23;%A=j^;mO2uhNnl#e*349h?`CzzOyS|0x3X-A4pBR;jn#(Qr+9K9*vtKkaV_}to7rr>H{hWXzu^S;^n{7qs~%W3X8-;e0LKaAKmAamKeZ0)TafED9q^~ko|*NdTgH1exV)J{x>QWF&sfa*I@)UfT0@ZGWu0#~t?#8$6&YWaZ8UUBR<#G2vM1C30KieP)LkjDftYw9hue`8@?tSG`XY_XYq4wMAWPoOs`33=LY`kG-F1cyf-(04}B9Q_t3<IoxtoZJwoC}u|d%nr?s{Jm873TAK1!2==gIq*Ci13%Y2+y-I2uTMR&ywv?sUvf-;&HYkL-!4N-E}=&f<n*-Vo_Oj50f!`yiNYS@Ei(0xc%Ur3eB;^XhuNmyS&Tn8gCf!P0{x&vINBD$JJvy!D5E``DF2pR6{asl*yOt6po{O+0sw6N0MtapS7HTX5|&q*O(1e6=)#WNQt*0q-HHgl@)&JZ;T!BG@Hb?fAiqiRk%~<LR%(aicA!;b;Cq7~(&%w=#+MK*9%rj2C^OW11O$_Q1tC~OqvEZVw=R`3r6PwVHHwI_?Asu4Esj~2^JG{jPsyXmcgwseW)O=&BU~9*DK|t*j<yP1Cw|4jnlyOL7%|-D-^L;=cj?FJJr*ahEVweSx7c<Lbp_^1mXin93}kKM^a4h|hr<gu;)Zvo<zfruIcov>Ox&K)S?{=)g?gg`&PF*Y$r^=iWgEpS2W;hXAONh>!lMLKsHQRmtqP_bT0p|f*Zp{1ewf^i$Q`gOhgnW7CvnaMZp(Hmx(MM51~~`Wnw~UIP57<}fpJl7xKl;6{Py}40A_*qEC9pC(bb|AtqtIJJZwvFxZEamg$Siq56+k}oj1=zDX5B}gsrg!8R!FHdUBut#h1oK4~w`cXF76Q3<+%Nz?<K2k&hZ)30TZB-S=fLzaMFN>5p;5F$_m`NAoG%twE6z8>fp&1QTHS^`snx+mDXhjx0f6cph^Lijv3j81V`Msz<g!*EYFX=62`AE7Q@jC?U{6z0*921{E;Cp?phyE0I@*!<KJGBR>gFhF`#5{(b!P!vmd&HNrz9X#1IR?Umo5Jm`yG&LA=QLogz{8?N;S5tiNI0?W@uw<zPdT>IUy!LzYGiccu`wYM_}sMmpojdYB32!8zD?SfgtZJCS55?z+qF{Jw9_ix>bVO1w!r=o>&2^o2|;x&;c0(iu-_m_wmZ`}ojYL=M1XCZ<)i92U`@$DlU)yriZocs(zL$O@JPxtpe3GL#xc{k3*1#=i-*8P%jF}T{wd!22uV?SDYwr%{$o^dYFm`4U>hDa@;p2k6>J$_Es5Pats&5{0;ui=U2ac>g3q_GfkGALd#b{^q8g&b!hp<VWmw@wmy<%rvvo7`5A=Lx?<JnbI`m@|zn<e#wh_piM|I$t53uVAg$r>`UYI>N6b{0iy(5>LZ>eEb#F`HJd%MRmTSI$u$puc*#Xhw7YQnfYCSo%x9u-Mb-0KP9l!B@_s63GC$d)`$a_1gKyN?4^X4NN(Wcb`rXq$(}`TqIA+CnoGXTF`W3UFoE7J1@JDY-;v+@RI(1#BqK&NPY+HZh~e@%=Wk&sR;Pzi_imvfH+{<};O7@m#uEv>=}LSRix>fihQst>*Qncgdg}zoScez6v<keOE^>8xk#jXW;9AcvkI;qL!QM)gxR{kYy}Wf3;^KP3$>kaJ?!xsW`<2f|b#}og5a0O&Rk$wvn}In+B#iuI%f-8)($!p!&WjeqUi71^T{Lj%xisBE@2cVqC-E)sE(&)|aK6g+aRLZr&B;9rcjN?nncmx(Slv@_#NjHm@*G+B6#nfxTGBm@hn&4TKA4Zy{BgLB6utBn;S^aqzvfFA$ddz}LS3H0{7#^H7EXpKxtD|>nH}cS=||@O!kI4J_@yX|UB6Ut8(g?Y{wfIe+HE~UOZxLGnL!_4^f=CzOq{_c8+W4iCsn@_^kZ7WCf#g?ObAK8cu@@nGxi(i{1-{?f5!iZv;xh{KunJ-Pt5pFPh&mi<nQ<(%#NSVM(bjDZNBb6FXTne)g+&(WU3Dq3)S+KCQWDKFxZ1w-)-uPU<~K$P5qZ<A4%i!^Aje&xkj$|;r^W>QiH#H@n>6ggoxy3q~2Jb?fii#*S))PuyI<}aU0*QV;eYVp^hHOg%)q=flsGj%?)RI(WM1lh`qaf8pnHj@iK5&bMc2SzU%xOXQx{H5MFj8x9-XSp8SgWm2+R64%YcihnHvulL1ZX!g90+VY<$7Lr#9RxQ0q@5<-2D>QAc(=;f7f!l-eWDvefCKNZIlZuyZcq#=pTgTbhw;QU+ePsFs1sgLO!K->(3>OiqeD9HyIg_ypHs{VIEOy%99xc7?%isZ>-74^tEWgxx#9iTUYLiUCbGd$SvFk(G{Z3wr9Ob~=@OUxToTDFD&66tKuR97}a9*`q_OI(UP&*vs#Xs0cQ4Xl0>J`=;8m1S3C!|zy*)Pv6*CCrY7my<J15Ks)qpo=#mMWNAvSCG^qDbk1yRggydX4IVp7XaC&VMYVJ`S2)s(PxHmOB^v4tWCaw3}PO5k9#5UV!8tZQ!<T)nEtM+=*=2>m;M6^%0P?rtcqU7pj!&cj7kTDWGs{pQcPK_t3Hc$b!(8_Qv%{t8{%@5JO#?>q8{$4w-QY9fCNiMJ|%`i4O_X4HdJP85U5U!!>yC(0L2KPCL>y5y7c7P5@fGffi76NI~hlvGsMh{g!P1Zy#$80;(SenuB%%qsCN$_1$l0);p3M!9JB$od~#xg>q+(raX~{T68H<8y+m+uI>eB~sMKu(b^^_y<E(PNT2#(QVkFeh^QWzxf6HIhmzidzI97qS@f1hl#Eh*oqk0jUEF@IBVEzJ^awW=MtBcW-7FT_0YUX2vk&S&ic>fG<w*C{lVlmFC(t$BnGu<g_pHgUWP!EGedL4UOy@We>SnDW`I_`aqnP^{)HlNl;Qez4OJ}lVn3X)kNC<ABS)Gd;hV%jO9N%LSG_)&1Tr4u`H{u%S19^*@sxr&^&WPBupta-0pJ#%fl2?iiBW=wHqs-c1yXIinY>Pqk{Z0Cy3C>84l3f%>ZEHir;xK=`?_iA<gxTljkQj3*tJx-s9Y!m^sG&{VvS%GCVRH(MG=PgDaRI0qH`%}^}E~$(NHTn6T>(uO6K`K~egBIDkb|8MVMfN|xkAC!%kpB}ty;IbGGC2Pn_<wl;E#d#^1@Qm&3jDu?+(I$&!oUMd+j4fF%1MuX0GPj*S^*p*sx;2fWj6qAcObRttQ(-x-$hHHx92?pn0sD~%#m2;&|Yc|ct$b<vq>ET!>2Xe|I$||IN5zEwaLM>5rL;`NT~=h&aycs(mi7j#f%s-7%l<VC*tps`Q9?uBDv4gn*Br@w<{AWqpNI1TIbCM+sa+*x|?D$T;I+_I&bKoG7+F#blgGhE^#aWuoAN8YLmflGXc}V7G713Ez4dCBqlZ4cYfC{R33Urj)>isEc0c^cT3sWsxS#pw?p>>>^7*gvBtJpfjda#HR`zq%XkkCZO{s*6)?HwBf}njT52B8kqJ)GYu{Sm)!jX8LA!NrBM6{Urv7+<*jU59|1#${F5K?<rQD~}pZwVByyvs?CF;DXPSa$$-L`zi`hqTMjuGFOryeHyxGt_Fkcvy_1^xw`+vv%U3WCbP4;D!wPATsmDU<3DcJ&lHHvvL2f#b(+VLgrz9*f1u6er~Hr@q3~T|9^UoFZ=z^7l;Zd0mlrzSyhTHnwNC(xgmECr)Dt##;#O*}@OAg-<JC14)Vw(&Mh-r5~j_+q<;FOf9D14%lVL^wzPgJzX5j8#*g1K~tma22NAvozc_v8y|kYE(dre8P5yWppLP2-wVUcwgg!Nu*g<}P)>Gc6VhlCuqDsTLI4c9WqVUNHx3z~<bku3{I;+XX>KLZ{porJKSQ<}2!$i1MD4m(dfv3e^b#gLs-7F_o@)=f10wcigG^5`;6%qFEj6hB(udceKD#G--4hJJGxwy+XQHat?#YHb+_>9$Er5DYH1-XZ-=c0y^@X$ycw4X%5){W;)A^&$2vzA?{jO*Uhs7=0npn_K$wfxG779q%y&BkI`0VX!dAqvV?aK4pg}0_Vh9&f?U-1%Ra5yfZNr#=1d$yZa2lncXx^kE1%VwD09E`Ul4(GQeU%V|zn(XC<;BGW~ih4x51I_FXWUiJNmt#L*)TyX}-hQOVsE~04Z9Z}x*n+qf^#9hU*j(pBera<>P4LWcC3P!mi=FSU3#%2!;V(b2@y+DS)V(%akrX$9yx8dVqCR&=kN?bMVV7NH@UHivn5?)e-Xd2Wj1_haG~)HE;x=Nsm+f|FMz;~Gr9>vTjCG^ZX&8H(>lpbz@k8%wFT9u4`fStPT-a`7Kkc>U;Nf86%4M%@>t4&^tL?QjzXkn9YjawrjrMrH(SFzcG50%u_$e~>KY0K7)Z;tY*s;JE-5SEQxU10IWh4sWpp7psJOqD8$e#~PNoPsS_-*+~JNU6Z1e|==g09~@>T)oIbzt@$Q)LC%6<etUBxc~<7Fo<y0wF~?em_`r;*I4TojGOp{v;I9!c7^+!975NAapHcd=6}iMo`MX`;I=#9qz|&8`{pgslW3WC`RD-_wH-Xm(hRt3+{JG*4210g6zrpaSKfw%oes`A?0(26H8kp%W6O(*-`KVsh*XzY#ZwqSEi@gOAAJUJe$)YTSumYQSKm^QgE3w+dJRzsb|~xfrt-iDJ5gTh+cBTVK|zQEwc0h=gf5PvhE?IjF5OemVNDJ6iKj{U45&_SEVr%#=I~a%*)bim2e{RVn?0R#I!L486+`Xu3@j>J!pdAmQwYEH1!1ZME1M~P@j~a)~dHyf48FFFSk>AI#|NsLh-!Gls?uH{~Gee<<7nR;%U+ure_BKmKRc@^J1LdlKkbZudkH9O4!`k7K%jV8XqY`^%i=>Y}{`BTZ9m(_$X!icJU9B`)y#_hUeV&reArI4|q#wYsLKL+s1?`2Z>8F7t-T+i2PC@e!4=5YIj7&Fl}4rH-=<SV9$nR7jL~PJRB``$R)&$t+;Py0`WR{%dGy}OrTaq;xbZ_a<EiC(~fM0d|L}L<!sOwq72&Gq_Pq&ay(|o4^lnAza6{cI_89G?QI==*W;L$gR_$MdDXh9*fHc5%XEC(pdiyzX5;Pr<m{l!yhKCZ1brzlMk8sLp)urNSM`xuvg_8S<`mCc=#(^Hq?Di$_Gw$_x?gki74YozFMmJduC_hV36_$&=T_nGGY!xRLTWg9U|vG^yf+asWktZScx$XjT_u%)bVu2U+iJ9VKljvSStU!SBh}wi`!Z3MgH(FNQk7+Iit}uJW%4o9ZqF_>9nL`R0P4|uQ`hrrifwop3nik<&gxN5t3?48W1Han@_#FCc%APXSWgr<4!rHLB3lzUGkOt>42lr2g4*&GKXC78bo^d&QHXmzyUPKUSmR3uX}E98kdtg+fV_w*01ebhoeEm3MCtjK@Jjp$M0IN{QVjpvTi3KKq!PmI-g2`U%ux_|Lr?(SCg{Hjp|JI}3d?Ct3?&7nu%mj}mz$2tV*Ju11yLq!TPozWYCQ&-V;DM>=e$y4>fznuORaCA_>5aB1WI}e98e*&2W;C19)s@Vgt-|_n+h8)<O8Y30wf~54A&=X%f==D%DXLqM|y4K3|K6H8|cijhRfOCu`fO#$3nGn*Wc2N``OfA`&G}WAC~jJSfG|=)>XC1-sZiWV`JONETKB{^|IzYBwzTmx|&}vUz&Kp3IkF+r_pkjc~b7cItOBOaH(@s+4KIWvO?d@H7h30nKkcblsb_D!2v?db;fUKKc(~ei*f~r&$vmyId=u&`m8$+@V$#~82lyTl^TGIOfawU#$Q6YNUcc>@EW(gS4nGy{BaKs4HJq*rUf@>9Q8WP2N;|>@bGK<J!>9jaPUgLp_dr=u1OYpG2?8ukbm6J!CMc=;z~E_Kmr|E9xNf~zx#V`o{AlN9up<|H(+Xhty+wmJ;o1YYUQ@xV47l}|IEA1&Ij^utVBsMo1Fo;XDC3@5Z<?#SctAtouKrH`gOI<7PjEytHY%^%18vG6#!Z(^I#QirrI=RyM49ID)!qnjnzEEOh%IPNj0er+Xjpks!y(3q)K{L?K-+}lvAYj6DicWRo;4)cFV;V!yJg&*)tMd*I~v6f3TT4z%~cj=E%v~|G~KuU%Vy}c_)w#j!%SoYhr?0#|vg{(tp9^5K*t%gPe;+s+G`60n{o!HKYs+GUv|fW%^V@C3@EDa6|6M5K+uHay+Vei^{{)_e|N%8;h2sZmqbp4EzGTEQ2{ASs1q^dgTF7<XDLWl1cTI?^*MDSe@fkMvMhVF*c^GC$%_aP!jG&Eh<vSEzNZ6#0QAOa6+Z8qFEk(X`{P}-`+|FuBv5P|5~zf^Agys7!_5Z6;DtodM>LMv^yD1EiWdG8iLu*rk`B-GJ-UCV->;+q(zLTBxwiNJ7u6f3F^fviYIlvsFQO5?JZGo3B$?+osQwV<TxAXzB0PH)$amFBX)Hp>HeJ;k-^*`fXoEbAf|p0PzWf?^0ys)TYQ@a6jRL#w3ay%p;hkQ-nWqwtHgLJpeif5h3pwCwUl0NI}m0f;X{NIQfTG7s3F?GQ^B-q$@0RF_-(|-)s~MmP)g?6eEF7gJ!MO2DV9d^L}WIJ0}V_jmj}f%Fn3MAr{!C?wz4|}T{Cf`P(pVdOao4fA4qSbrLpMhXWJ6KbT~#izcwSF;ag<o;8m5|+)~F9qfy=>btdf{eo@=n@%Z7|9VqaI9)+^%-`%@A68gc(l#|U-VEZ&h%AnHIThXbE@bu_4brPf|0y@&aUimeByv$5nq!3=N{6c_dwdUz<q{1dN@X@06N>{=d8Pdhr3l^RpweC8t98Ofl@>ne$hU%`PHajP7-{BS&<M7b=HFfU}$T~B-Zd@hBQ$<D<_YKG&v7e&)kNkA`&MnMM8Tb{ip*VQu$h0Orr2N1gjB=)5S6(}oRlPDBRH?5qp10wh1AOXMTX08k%`*W$lDsJHzJGvEhi%(j5Aa*R>YfYmd#d$55#TqIGx=12Pv5cv_PB2gvv)DTXVPto?k#L5BONbh&-7$N;L%$aPeP5Rp9%1X>Za;|5Y~++YK{Ru_XNqgcB9wIv1$wl3cIW@zd@K^BYm8SNet$Viccw3+Gk_@pctRn&N4pxb_(;GvoN2nYYW)OiqwLiFw7r*{iWQo_gDn!o`jNtPs`OkGG+E)NZd*p%bi87T6dt*%1RN^6E60!KVobK?qD0D{thez5V{5?ux$PaIQlvQBX0;PeI&=+nlosi_%(d58~-_XsGY^A)@@m-w~)XG->r`wscnxAv$Y|qUO8cL*2rfjG;kCb^j`dQQ`!M2-b|cBW9Jw3EDLG;$PI7%Kxg+z++ep80p!TIAHw;~{HI?u{EwBlSDxx48Ybcce$CC@=)JKVP%i3TQ83;G(E84Q!9qj%`^X=fk0Y5dEF^yVv5LM{=PZ*94D5+_80n+;-%`upojwSm1>A&t<1bJirQA;tqAGsBV_EACAb|eCtsd%Hq!@3O*u#JQk_d261bFlodFTePu8YnT6x+NMFT5l)%o_xirRP?Ys{C+fwgaJ0?+7;xT~9B!@~uJ=R@h$+suCO75zq<NZ&F<IPVVhWS{P^Q$I6jjk*=%+uJqss-4kauh7#hWXgQULU^29kgki<{^kf&a&Nrk<2EtM{y{QFwDZpnx)UNOq)s)LMH!R|<DzP-SdhtsV%HIm-th#aZTLz+%RVGX`Sce2hkLh{(+McFO@XaXAYg}{7jexso$d<Yc6+Ul2%B0Rc3C4JxZ7^3nCN(VtMQ>X=oeim#2W;7XAVRmS?VcS^VV;xxjh7m$J7^iBa`s@9hgd?$WZ;Gr8?p<=%a+Fn>=teANQfBY+K1yFv$A*M{PYjTtBTfzZsUf8Ew22KVFTA^P$LAgSD{i<$L5A<m?*wo3rNDKR>A7~>c$U@$py5}svh6?196Hs76y>i_Qrn}s%&uWSQzx6T#`o)tN7SAI!}aM+L6Xroxb2rq@{Ya$_mc8W^U$Dy%_|=?m7Qf2X#2qz6h?a?wq*#&%58l<{!T(yRj>-Lxb9(Pi2bjQ+~r*Zf%8Z_RQ?DT-DqfO)(<d132u(l%H2Augsv83t6$wWpHwW&0&{ruz45vd#L54`#{#iY~>qh-dCj)Os~Nf53K{H=87ikal@#IwZRrAXS!o=g&}328`d*6iSpxU8zHGa6G$k=VR{=wc3Cqks)4tN&BA?6mZI*(k9UgT)+kZ+q?J|dZ7Wt`d6~v5u0RGTjqdiK_BcYS^>Z2#-^wTFzVr{zvlHoBcA`8LQ7_A7D1xfnFrt20%w|JFk+scljV@8kxy*tsm|@GJVIHy-q80&<l)8P($}@(A=m<VlOub5mDJLVXVBB7u_vL>BJyLefk<loIu?B=(A|>WGNqG-uaN$aoSky8h>gHhBp^=F~#%If~;fq(JD!o@cGfzI$9<dt2*I?XK?+xhh7B5=%z>Q~cQ}1Q6Z?LbarY}_7LredYuw`#&u1SL-^5kY$gKV<;(?&Ioz!NE}5T<U=`lZg!AOV!be(kc0DTx#;9T9{)vFqpWRWYF^D5l?QfAvp~<Mg6(GGSzqWRF4^f0rH4yX=&ctLZEr-=t|g{p@ejo?Qm$pYX-(KXOnHFN@WN+AN^*{kl5rD@99J<2FmX0IH5Lx6rLMB)xvb+lHZA7$Y|BQM_b}-qf^PI~rKoE4IwKZ@Ky7;L9N$n;pt=kHO!o%vfW)yYtx2rD1a#+jWZV+*lw(Q%2q_V!Q1W+c{B`E_y3~%rD^}HsR{L*vx`sLZE%PUe{eM>$*~-e@iHT?bBpu3Td-@76IvR>4xJ-Z@n;1`Gx1=LT-*~(lIJ-YcSDI@b)^UQmX4%;n!OLE!33gL>R4=H1(~p?DTflL^JkBV{c-9`R#a4>yhz{=VBhmGc$Q%rDL3J{gS%zUPFX-$~T-UkMn5KT4Jr+rLl&caW&i0_ZCOu0ly25^4owwvq3E5`x<EGuR75D<Jh92&)*|$yhLigh2{Gg(h#Lzz)0uOTsF8Q^4dTlk2n&IrDfAX3IK%4Wx3}BgjHXgL7=O%rfVBmhjaeEY#VFj(WU<~JitAL_a8LxkkM$t+=~G2W(U0+cBx^+IzqrY^o=3)1BD$Tm0KqK$^~}~Eb-TSSdYghh$Ef*E)rFUK2mW`+^Uv+I<`~7z7NG7U}qZOS0dC>YpwNLRzM4!nScJP8a5SzLLIi1VjRRTSBH&R;|s%f1K<awX=ukgMT-4$z%*Jhe4U9{j8<|gJ%lxqe|4N_aWqb4tJqu_ryIe1eE05K!@jP{)ojr{w=Y;eFO6+_xJxIygZ5k79qK+@_l1-6o^}T-xvYf#@Y7#)SzJx~{r~K}ON?b(njW-Xd+oLN+2<K29{1j?TMw$Li|Te!D$&3oXUH?pJOBx>FaylfY75$OBZF~+u~A!srrYYKC(yEyzypwwkUT+5V1Tdy2{2;7V}Q)d$VeVAWqsfGuf6v<5s?|0H}huEs;W@lh!ZFFIcM$l_#fY6mO&V5jJ6yQXD<Vfx1SM1J0rYuwVE0XJez3C)bpgs*Cz!^l3Oxp%N$~a_MREF9emrAt_}!c(?Op!H-!Fib<lCav~YuGgxNHTn<-TcHLhPPGHO)%Jfnx+Qa&WYR}c?3|M?Pe6jPR(<u~SI&;GqSJ9>76gA60$OwtUp0)5RhsJPI6$^JS2Fx%a+9s4yCvfSkULjxJ{uzurVp_2kYTx>AAH^_4r`zRLt>OJF7z#H3J4Uz@gM>WX!k&lM)ci}*hef|Oal#w<tH(ne-B5t^pLpp}kfzg|~2S_7j!BnEv9pFr%u7qr00wMjK@8~NMTDz_=F9HpV%Pw{3T#j;2sT*8DV;{LBy2IWOk|1>>mt=pMn`X0V6rPZ}@4}O`duZ{r*zK&O39piXw~!4`G^O;UJCFRjXO4-zi53+~Y{)6j5mCTEos=NfatH9tmkm`Em31W9VORl6w0p|Blk}VxQ;A?tu5SzlK;aaM9#^@N=aAmN-s;ZYl6*z%<HzNDw7(J&14|jM)vEG;idx^#;}k<Wd&j-+mJT7bPk^7@y6!h5Fkx<#h4Ut#*t0wv<^$MYt1>re(%x$C+*q4l87UX_?5nRki2&o7DMwHE5?qO57qnwGi8EFsCyZ3-!*;HK&~gne$ASm9jHPO7!4E7v8SLW<8vO9P1A38WWQUFGGad;v*T|u<*s-=zJfvEI$aVC5(=$`(4JR;fRGtKB2HPE@bDH#NC+?|Gq8>MU>46#yK?!ls50+?!<pp`*g*$IiyP73PHbc~`@nIGkV=a(96r+)w-K@1+LRQAtuA>*`Z>^<Hza+NW@tkgcIlX~kwy>lYSfjk7hyyio*n*`g%wXJc@BiO-ZKeXBmEQ5V@7<6t+jn%5SlV~t$=)67Z=Kw*aH!=sKy>Tww|iR$Z!)XJXFGU>4GZo~kkEL(gE!0_ya@S?XWMs=@ws-e`Yk(nKsuFoY}^f~Pv2s-t^0M%I~vf8C#Ln1JTb75?ZNJ<O;^YjZ$<i-;&5kj@RK0ir%2uY2@tMaroW!<oQr?P{kESDzWb6D;s<U(>`lf!s(2?&^DVm(CEd|qbc5<y0wyl`p{}B{0c<<7w&U_Xn1ap3*{aUe>FjQk?<U0SqSDtKwx7aDZfEMP@s8Ci;G`=+7u@pPNkb6sr{|N6g8=+dkUh=!lRE`7?)#j)t0SZ*Y}*}0##c}l!vk?&JSN>C*%j^*Yf{=utO<l;y|=f7=iE>3z%pqnxO=DMRHO&^wS+H|+mA9ha>hiB*0&myWz{<A@XjZfwZ|nkPBe6X%J!WaYk&R%*xi|~fPvO!YuMeUe!-*hSxB_gapuQvg$wQduziHNLw}!;Xm&GZtp0)v^~8lHq+r&ye+n0x(t-;;aKw4mgtBdT=oPd+5F<SFhICpZp%>{i1iScgU>T)uI{iq-#(@3&L_5OLUw}nBhN9Gh!@+S3>d*i++V%Xf4fR-W%g?{TD03y4^qgu&on4cnu@(6$lC#f|&g$c=#WGGjy18aH9D5VX5Yv)*+(6x-tg-J|>ZV2p@><e$%MyLn(?K`KnMMXel9}~}p~8*rnnuQ8R*u_bOgHdOi!I~Z9fE|3<?{o(i=NakaBOz$aMXo;0;z3i<?Xt?$IUYQ=yMzlk^rD7{I&e>m*4rAeZ{r^7-)JVk#4fR=x#nvdn%0>4}b^7NgySZEk<%7aGk9m`$tp1-oGspXiRPbfWhAEZ~$`7%nJaS>jFCEG6+VzT|lRZVNxtBc=X8dc+beGM+V1~{m`1PkSq$D2(F=)L0Z|6b_}QcIjjs(F{nuC10O<*?_hb`zQIrnJBIBD`n2bdAAZOE#zkKVEVn3sX*O=iZ6Rr*eNkty&WP}B#O;82*AIPI<s6}DGpPldnR&49keOKZj&4{H;hHw0be<tYL<B2~60`zUw=fj$UdXm^)AmFqg8q}tV7n$$Ao)grl$lxm?FexwKz*6^0VDvdVYr<eH^EYIs7Ph$<oU@nMk9M9Zj$7a4vcc~4hGmb=g!h>${iRTLG6q*@(N76MrR<^xgFz6gRMFeBcQI4>W4i9scvE{x=D2xDK0hWDaZ{JOJH!YVdRe2-IKyfp(T6rKjZ$ApMHXsd7^*q^dlZMs-GT_RTveJyJe1%@ZnHysrrW@!^_`MFHw>is43pgGI@B;B+Uyvu7;1}G^K^y5voyeEswZMXO7Aw6cAkJ<SR<L4eVoWe(#%p-`$P;as9*GHk9H9y0)|{q>dAE^@Hy_hBXZ41BDX@Z~q1&R3QI-?+AL}BWFk8i&+5I@dl$FHi>Mqi(3ES1inDooOD6`If8>fi>;DcrTM$8#wK-s;fQL@*TBweJ#aotw|5B4J2ZrOeuf$~gRN;z49G1Yu&HmO>#?5<Q=Is#E}_@|y;gsy&;Lw%b4{s>B9?XYqVhl&M?OCi*~Ww!o^jg&l$oj2fQOh&_A552p`wf7dFp?To#5$B&9q*A%O)iYNE6<FtY^z6VRAE>bny-uWPN;dQ%?~|@iCKV6|&TDr}dVdQf&CrrUJjU7ZVH*W4NbVyHqKYfpQYNnnX+>TsZKu`eMI1N~$>j(mRk$Zi%Zh-inVm@Po|4`JnFU^ZAltA`{WPBAL{PIAYU-yu4@qykJJ2oJDaDGM3-FAzt%LK#*(1wrS>>07i`3`%W-^xLXofd=}1!3A@qN6vCmi!LGXhB9LK<dF-bVY|zaH5zG*vo-`bBWl%L)CmX1!NQOV=-{;=kLPsLr#sf00338M^{8L}ch%&0p7|{)+75y-h^u5reIFLs?GLf2RB;Lz`yddltItinA&DqH|oZHSHNCV6{oVe+B12qKp7|Uh+z^DMX5x+u?A4)^rftjrF+kp5bcG;QnRo5hvF!2BI2O34i&5s6hczP7K(wG@mqv$QRT}Cln4`EmjVOYj5UXEXsR?-GLM9m^Gy7#~+cLf3hHQpR<k&A;J1?d1&lZvvuq><?vq<j)6dpG^z-;*OWwh=-P@QD$^rd|hWdU}vd{}-qKfrIpqy=0K`^Me%Muo#E8?QO%GHn#ZG#<qE8V~bPB+Sqm>w8fY%_qJ^26y&Mabnr+^R4&PmOS0cktS5%k0fRbkW~cgx2P&yJ1RkZv26g2A!A~;1hIgM{(>%STR&>u<brwqw;Zhv^7Bj2vMs*)@LyZ~6_nlAw=uhwF{@#nOM=zU(%Bbg`)I~Y@uES9EBO2LVxEQV7qtViV$j%H#OIvx=R{rzuS3g);B0I7Ki9H{$^^eBfq+_zxC*o3{P~vR$3H9!V1LOY7`UKUsm~lZgWhqg}lfB-Cx*26^C>QI58hHo$J=3BgGpH%T%+0D4HA3rSX*%KC8jeiD0^*ULl6SdA5?~n`GDY^+Acx&V!@%BQrJ`ctgaMR>=TfCOA56^gn8fq|X8%O6YWkaYA9n03yhU1-cZ25Oy#!YGL{35zqum+T%-GovK==$Tu~;s}Rx{;H3XsHTCuM%Lo$0M&U|2<pSynZ1Exf7_9z!?FuS%j+gCQVGVn&o%E?4EFzQL(9c4xBs2eYOK?bQHryg~p$w)UZ8fl1j>oS?dk`y=KciXvoO4YU3>u~32F4c2N=ASvpd;!=^YuvntCC%f3HCj2+ghSgDM5acem^-s3!h^(bs*}PXbTK-B|R|_WNS{51Cm4++rLf~9IvWx{aGL(~3r-=r2ad3P&j5}8+0_NLAxu0zetN1tXiuz$kvkg!ICcd_M@TbsotuOlTzlTgP<hb`tuAroYa8#4jYg+}knAD4CTa58vd+Z%M5C=h)+!C!pR0C#E*T>uw%#E5Op2^9`k=SyJv94SYsnY;>%t(8kFg(j?4-jL+rS{QWm82}}o2)SQ+(w+eiH4cPp;Bh-Y9ve(KYmUs0e2ZI8ynFXH8moq<%gE$VpWJ#dEaCH`q1Vb`eI-&BX0-Nmd)>hZBLWGPU4xHZitUgcoLiV2SG$EEx#rBQ*(!Z2)Hb(z?hZzMCL}}JL2^_?wIEw0d0_;)H0pT3DW=a9&_RK$U}sZQ2B(?MP`2Z3%>56G%4`dInN`&Y!hW-PjzCj3SNid`<w!I)Mm@1uhebg1R7BsO88<7hY-HaS#T;8fJZ&fMH6i{<Z<1Vet}2QmmYt62D6qd7tW@7c%Miy`LdpS#D&*MaGSyn+n5tn5F80O<l_PlM)iL-s_#O0V7Gg~mBSA`*b;S94(z)o#0`N+dw&NNDbyLZC{Exd5(zGa168-&SKigha^iHTuXS4|cqZN!oP2}rkZ7Pu9R-otL_y7QbHM=a{F#OSWSf+#6LFw~UhHa&9L@<)fNK^-@UP%)fY;~;<JHu)@*VA2EHlN{0oKX@NT%nhjk*_V#hoz;@uFiZ6n`eT18Y>Qmc{Pl?OA{BjWhHqMf104cD5iWEGI0Ac4RhhWbP1cV)7;^0<w)Mox}j-8A@Dk4SzayVyFq}p^rYBuiyeTfXqp;4}+uF8s`(^Ri2VDNJ|Kyt657Zt@{Rzst|)JwGsDw<lz$9sYj0yPw8JBbN=#}%Q1HKmX9*M!0vpjJ}uh?kgI9!g1RaDgREB=69uSp;`*JL)&WHay}~IGU$w4FCb3zF22H#_5JQaVjD7U(KC<$O0%d*(btA4b`%6kg*Jyd?;>{VGRpGAqqj`7bUPt(cq$cnI&U$<b-+chH{?+=)nZ_Cp?O}g$5yLRotG%jW+WJ=v;e&|r`qE_QlOO6pKR8hf%9(E<i0o-33}U?Fx0b8nW7eB+IM;E&sy?4<kQ$*59pdS)+MM3|@XfbIld*S~lY7UQb`?#=7EL}O-CzIiQ9uc@dx}`>-5gNH+;-!kg_2!a!A#5tgZiD@23?Awx!CZTVeX(|F^mkeTNBOBA|xW{U@4At&Dw&Ul6a96)U)8ZP*OR<KsK&INo{3z;z`Vq(PZKF1vS;~B90td97$V8BoUpS#;?G>G975lrARU5pr<t{&=i~@juHt0kD|%J0?><qvV&iTDYz9fGvn4+#rw81=PUdOPj7sv1x11_Yu&=LJ3=rP-*fE#`lp{|^`rD{ma(Ru;|pdPMO)MG)n*y)>4%tQL_U0|SvIs;R(eDel<Zt47jmdJxrB4`<pnb<1{F+74|*^CU1&5>E-^`rFRo!piSAy{wuQg;+~i+;=aNTpaMgOJ)1D=du)<?Js&_2DKQ*9F?D1x|u5>{CA}nPN(;`x(Bg~bKHrLWqWsaaS$IxmV=u}&oBR(o~cm@AwTM%=ZBVLv{Y8-k9Ru<``FukF}LRzUp?s;Ra%)wiI!@p$;p8mJ5d)EjAZ(ME}aV~be)2`vE%Kg)DHeJ-OoLHLgy=&-cWx{K{Y0J=g1U|$Ib`8oKUhEp2s6FM&`Zw<y80Xnn%xuO!;l_bt-JgHwG~q<;y2rKBwrdP+*YNY)q=(f~d<$R(ge5`HK}`Vpky1&TePj}3Z5$Kk1rhOcn!p@kq<nd&jl=uvG{G@IU9`*Vj-Q5=tX;wlTqg_ILGqF*U?0h7a*V83w`75GwP|f_WXcQ$g=_RgVzK=+PGK)ZBnX5op|7w-N*0nO3#^__ma5Jv1Lo<UH?)2v>U0IwCpL@xvn#0n*%~29Yxu^5#lnNT@TU#X<3dH-_FL3|fSI5~SWVe`lE#2@@$B?4eVdx9478<a_*3)qvXUl9g2BN=3jLB!Wc3ZvLrTcAsZ%xJ5uh?@BkL&a>b+dAGl_2CIzVBtA%Lh5Kp_oSDfGtMSFMmGF>ZTeJxhIn-_rv&Vq@ompPlNvS<Hi^RGdH^M~#wEsDDa<FPPg-Fa{Do$l#mjcJ%-I|BnO5j&5RK<p==X|APdMZA3rNDezHZ$7GUH%PGLDx9?wY3Sg)&PJvIWIfWPfzW+_~t60{EK-R@6!5oX?4@Q0%S&Ho;SmDkg{bGp|cnbg&O+D_<hE?ZH@S7g>?9xG1aEh@;%TrfRK5U)Zr0SaZ-h95WU8p0b9<6o$0&DHLJ@$!1p0r8&E~3#1Fr!Px;N~71!*`*QV|36M4Y^%ke!{}x;S$1+D2|k5E(qc`8jXdbBMh2Aw&|$tGqA{)&G|O*g3+!?4fe6e=ZciXq?ImKlE{{c0PhhVuNY}%s94QXtD!FmyIOJTA;KwwC6$hF3(k@8WeB3Ikkg2c>Q16Y^gr&2Zxj@sN{-<>O-ED*8CiN*Td&EAulaGO=Tm)KMrKj$N5aXeL?~fTt`#g_jKFI-3{dKiE4$v@RA~IyhxB?3`(!=CF>1StH=dNGKK_KvJZl(*XygFS=gifWyYv%^4}alJ%+qrMNUlNa8`MBm=Qd~|{vfz5ne)_iAb^`&_YJmufX>d=`EbSvl&%zcl{iG|HxVB&$Mo9vQPi*}X--Gddu*?o*BoE&W30SieW`lVQ7V_Qzp*V6`(TP2@G9f(2IQtXVGp<3yW@?OndBr8H31ocNmwb4$GR29BYOh}KDpk}8+owmyz#LnTs3YUIvGo&VR%=!_^on!$4Sf^9`Ja%!7MJp1kvi;xnm#abT&I1-^hIR)e&`^!@Z}!6;+-<n4xYiPA`D@<L=1htE&f1oVLwa0{`k$AOxH0sYMO-J?CA{aT+mSAS+m;;1qY1$iUk?X()(Txw;R3%>5Sji_MSR^bJOIb;|E9=sd_lAL8iJ!%2EkCT<2!fCIG$5lO-M9Pi_FaAS!h%CSJC7uHh)c(Pb6bzw}~P&RR5Ewq06iKu{M!R(wSoN=Lu)r#ukn8Kz2s{xT3?g;hdy4`yEwBh6mXLvtNu=1>znx$me+~Y<1dXWR(%xNV=Q8$TcGRF|==0p+8noLV9{F9!)3gmp^%}mfr3b0&qB-k<(u20xtRI`4RmFI6?FcrSx%fkySRbMfp*(_uQ!@57?Kebueg)OazCi4-=q7Mz)<7YEfbL=rbUXYFI%Cv`712P6_#9B=JStL=evB_c|*%%L$U)YlKSsxseVqCPp>vR%}o~Q;w<vU)gW9-PGjX6jYBo%M6a*Ug#mhH{uh@#V86rLcH7Eh-0PT~azO61H^$&?tP`V5df@>7j;F~XTXLCICV?$O&9@Vg!R2hielL{oDV|Gf*&!96u6q-FK_O313CE^&(a6`GFq`-zDzpBJUN3sdF+YvxoJ{tio3zGr(H7=TG2MSPcNzJ@tn5}(H705V=vkOgx+&HA401D6C&YOlnj73;yNJ^e7*l1POgH_7CHPsXIjGgF%Nu9@Xb&JI@MrQ`&caC?B1!TY3o8!n6eCq(NAN<$ogXOd;58yM7iiOG&ZUXYYzQ}MyO<>PMDlWF`w-Cj+BK*`3S*1W<6UMQk|31~N3#K7A}s&_d1B;MS*`FwVO>Qd<1fk`&66u~uF;#hy%0c(?C*Q4zq?EkCxaYlaJN4zQ!2&{8iS=@9|W}nSKd|q|ByZDShawPjcS|i{pVbQrKuOh-3D0jhLu#ypB6JR?a=!_L6THTQfDUG4qI*xwjn5^w|Xf^I`PKybZlI$$y!r?#~#o<6cZF*D^0Z?TDV&W1#6)ay^261ZX$P70--*>h_(9=5#Lekau*+bHG?vG@dI&F<#8>q4RR`uKP$?H-7@w0o)m2MtF32Zn0XO69A-;_k_2FtByl024_KDaa*el@_zk$>e)OTF$gbw4WFkGgQI|Jg(dC3<$O6^(P~6(7udlQT^!nfB4<s=mUVHXTkhH9k-%NQQt?mcaLe#lPd-{t_1J6xm75ik_1pKxPmM+`32|h8qde2)<lThy&#lap1Vcd)`SJ0pu^*Gr-5Ye&o$SL4m|hH+LvX9grc{{?Oa;5sRUYf@Doo#}A04n2&Qq(cULF$Y5{4wx^DPm%uv7<gfUl;cOR4p^CoOX=SR7h}DW*ak!qM&fGXgYcRt34-OGdM@vBHj=0JHpC7mK0+r;C(-=nl5L5bUm6wTA=0j9o;6dm=Oxb1K7%uUN%1dXJ7h)<?6HKGm{X2ApQ>(u)50y{qTk0<u@QeD({*$-we#QMoKmDS6cwpw)GsQU&Ht-N19^_RRcXv@rnm};gin<GI$d}Bb#yck4%-$rwH-S!&raK48Re@a~#hY?nbsI#%_3_g!R#7p*IXvNThEJnf=PJHWx0Huv;-idhw?}2XFs?0ukK8FOa#=dhRMPF70wzh7;)3I?DcjYl^j$u9IKaF#NqM5V!G(5(lt^uB?=VA^rp9L}pA}R3&v^(oN$*%cY_f*FrSa#TH!B2gCv|9tf5|qBntQ+cYVhzq0bi?@hiwNEVvT;w_Gh{%!Oo3R8wsGo8PRjKuX?2e5yc&=*-<eIg3=<#R&&b@$xz{~QHr&V!(eH7Y+HB&v;~cVJ-eh>NhH-r@^h7nQvq!=Q8AeTb#M6FMq(cbDy(liVI3w~T$VoESSt*Xk7p5d7gr1K5G0+f+FH4lsbfrk^4)77fK=COY;Gc{bxJt7U|4NXmEa7)T~rUYw?>;IZc|~ILMs*%>evjCm9V%y!kn&i@`O-14KtG5(s1rk^te63MNSi466f^*AAPvHRdGXgBNkiEQOZl5y<EUdorT>^$yr6gxY;7f*XBkhF`em;TwvU(;15gj>N?0h-v*L!$&`iIA2D-i84^vrj;m-m(ND@h+P=Q<&&d;SA{%0L$ieBfNK2@GR7)?_ib=LzG;Y!Jf^mETjUR;P0H!UfA`czQE((tVjDq=p6Qs&bV$Sr5qD3Bxc#xv?VeBILs=SVs2&0saH(HQPvZd0CZ97YBHBNzY9`e^yc$C7dh_MQo>WkvZ-HcB(s~5vHleW8-#BJ|E&IqP5?CibGLdG5?a%(S@hNP>TUU2OSEzYag?@bfW+D%Q`Bh0GqO<y>qCZ-FZvlUEr7wnp@DFXT^Q9!+JTBz`AaG!q5t7tQ|AKk33+T{0w^4e*AS$kLQ%{RqX`<gHAq@mn?R2PoqjnxZ9CTMX-2$=+D0vn~O|M`n2&mn!gSq+YB?>V%mnM`w(5Spqjp=;vE(cbgLm9PKxs~`3G;<P9d#_506nUX(d>#sZ?fY!OWLzyV%cSV1^FETM-qCcY0AMqmk%<l+GjB8k8_s*ebX`$yW+&(@~uP@VCsv$m7<3iPgcp?Ik)&dZY8y-<w(u&f8vRkL16K~@ahnxQ-RBR<c@FTuE9RL9``pmNlMb;P2-#AF$D)YdqTiL1JkTe@#;Lbe|XUUT~vGTRSl?>Y~+c|VSM{YwwIVFWD4&WW~o*)ci4+8xNbO$1i<IEWsgwZI04g7jU)JxHRG$AME{q%sPC0U!%3Qtcvm~=gq09j(o3>pCUL~+z2PCVh<-sc0CcZa9d1&uK6K7x<2M+VFt#K*t&mAGwS1${Mc8$?p5^8e1<HgOUgOmD}Q&Nai0RyCI-H*En^v2tc1e@GlQt?;s7z@Ff_={eKYF5tn0y{5VmpB$f{x=A?&0oPU)foDi={UymQH<H_Adx60KvoYMfKpxMM+@x$~_S;GsS2^ggBDqCB^<>0^CwOk@isweYuu<Jeq-Kb2JhxA|JN)U3WOQO|y?K<3-XL!)N=9!8Me<aQk=qJ?9J$v)Xy(i#De!`L4inb;_-*XWoy8)BkvVHVAiS0AX=ZA3*s=qX6@0hnd;62q*%DT(98vOScVqOe_O7J9!?$#2DWk~C^$Pp5Rvvf$U?=?c4(wkzh2G;+Gw`7u%h^64AO_U-3H+G(R$+Z&4Z>(i1C(?`h>=efiuE;5?HK*bX6AHieKY12h_(M!+g~<ZNzXy^gjUEcPpx^|_NhE|6!H40R5e?ja@SeSJ*_dlQ1V#?3ws&+T2XLJEmaltC#i?lQq=-f7;5+2>JwRraATx7XI%z4Je8!f5}kS!EZ3mCf%rc03X%2f7T)TnZ!U9>xI5DA?0R6uq!ymLa4t)|Xme?gd?pc5eC9)v0YRkIGs>T@XGFliv!tzJ=6_+d{0GSjbq;u!zMZSZ4X@CTij*&^C&KCM%ML}}JzcO*+`1?7!EiKm;Dy$wL1eC%xiN5%<>(a8$+IGuh!t-#QLK^td^$E!mv-bB1Mf`oI4w8fv};1Nc>XT0{8Lesg$f2VL`C)I2-ATEKdOzt;iTh!8)!-;VORuMH|Us90}m?m5Ef)PmqD1^f;>4|T<c@BL@7#5oY0&|cLm+{I+Zq_qQFW#$c4ob(4ofRgE6@19e_=Hq+0b5!)NRwiz=FFj>Vpf8Q1e$_FTL<xcETyVwTq^rnLNq)O^AI46H`i`R)gRC*kNGaq{ECWUY7mI_VqeD#RM^g=18E2XDHggeO6bSfa(^UewiZ8azTF_z7qR#I6UPzy!zFrRZ7fE|dc;cy(YeGA~;fsES@TFTiCZ>1*W1n7w)jbRcu}z1OhD3lzdX$5w)-fO?jajjX|Tn%G0d#?gyGjHNzOs9>VJG?oW#eiE?^GOY1?D<u-g4S~JxM7vq1wjx^j9_-S{HfJ<GV14|EWqgz{wjP<9kr|Z?!XI@1w(pAH{}?#f!^C1lX#dtL|Hzxv$pfKV4_I9_<`7`j1bE?B0B+rWOQ5WSkVl=MXHwM$Dcjv+zV7RTnO9DH3B8IZgpG6hu*Hx;3k4AmBD_8Se7c$O1yJa#m#vrjY->6ylXQ?IfWcqw?(NC1RN0hf9(^Q+vs3MLAWWqO7(e9x{T+675_Z%TQl;)y?PLIRx*p8NT9!&W+FdRkVScUw!=ZJ0U^;(8rzkYYV~y_Rx&`I1TlO(%BIbK^%a5~$aR7FuetTwQLuE%ifh`2g8>B$Dylr);4$@?gley&re^MX$cABdM#F_9tjEAr%-x@T<I`M95covCJ4nzA;Snmli8xVm3eL?J!CG%(@0yd2)MipdXYu-Dp4YSj(lj;w@v2V0KVwtn&Rl=Ti&>HM*C97FKw0c71v~-3g(3y$`V`Ig}gK^X{*QH<*O0h#voECjA1B1Td-lQ9bg7YMhUA3$E!98|*gfzXx89BeTs67gop_6Ab-ot>s1y4>VSVXh?2|1p?n{O3*Mkx^T>@9mJf8gT|(sngMc{MzBF78;6h`iJF)GBd&s3TDiq&RE<hpLARgv3#03mv8c0<?6`h_VZZbIeCG0n8--gxk=I(O=_BdhTE^?&~oV%is5bKV|*;K91d2^l!ST$kg*|@Od<35<&VA&3y{x)ljEqemJCieseYe4V;t<rbYcX>?z!M;}hzlp(|Rqmdm7jgWezNiM4M*C)9Z?I0m90C0ZzQ3cD3~zfpwzXFu>TG|+lpm#qdH7?9AqtFhtVE}BgE+a5CNX49ArzJ;-|#llK_QEGVL((u+_sB`7SIjmJf$^`zfY!LsQxNydvgU5vvb?iC=dZja}QaGmThX5y;d0vFpRWMBN(qG)1jR`n;iy((O$rwA<x1_pL`C}hpDLo!q+k5im-V@h*j|KDda8g^kRrqEo958S@nWHkF@2p0TedvOe7omjBSej!T4ulT?^)dqPRW~O!f_p?gfe14eZ4PzPs@R5D;P$S4e_&9<WorXGy83d*6y-XJ{BWyrjpdiV)+u|nmh<&wjZaV3%h7GlOixbPgKyn<)-01YdQRD0o3gBo5a&r;TT&jz`8sd+n=^Z+Ct!y%K%4$R)KR_LWn_6l5UFS>&N5B^iH|r<H!s=uUGwI^n@w%-!fI-!HZ{X)YKBKsGq<V9IMxxm$L=Sm=5#qVvz3VX$PM$-8UWozX8JV(j}q>R>V&6otRH-|O44pUBY*#=JTXU{lFLDPuv4;dVh5BoLbz|Gk$RCcKi^5U2lQ0R*;ySh@iUcJ{{BxK0uZo^9sgi6pneqGe)StbGPAp0vhH`i*~lMIMZld7_UU0%OCS+XOw6hdS{iA-&G49*Z!_;P)W5?vwvl+{{=x@fOum(B-9egAsDLYB6@MwLl6#5pI`fHP>@B==oT-x>CWAjxG151TBh}GhQn6xQ^YLC1Ld!}r_9T;a#2iwW8!oAnlyqO%lQb(T6W<RD%0d&&y+b9Gf>f#pJR2AEYz{|BGr&X`zwM7uUTJQObvIm;SJ1k-vApHDs-Ff9!c3+_IPkC3WIn4D^L+>)=FgGLmz+qsp?^ocQC}+VqJ&}{sx7is$yuE@%>yV!>mD+jfP{@Wh0&SQBXnF`YN&e_Y50h$hkZEJ+1O*Iz?X=%(T7R3MFK|(3OHkfDeY8Oy$#}dpo7U;*Dca)Tn$Jbg#KZo9l?q6D!e~on~Bel1S}iVk-FNwN|1c@vxpi1LL#Qpp-`lmPt%|v=4gP&G^NDRZ>jTl0}-zis~Zp^ot(g!f+yvvRZFRYHZ+rEsAZmI;vK`UKSywV){E+j;F<|{CC4>Bkg+ivQ4ym;C924?m)N2`iWph_=ObV?BPtalc@gkOylvER4l4up8K8{eyp|K105q#IN=1~U37fD%EGkK?vDf8CZa?Tfp`_Yu3p=Q}fkPT8g%j=O-~j3))Tg|GFon|hW8EL3_1vs`z@=-xs*XrYfI^b$-QLJh-khfd93afa5JU(of(W#N3*bJ-jzCtU1_V-KGp*8~-)SLW_|>lnq%x>i{T~B_egrRJA&xUDs_#U*$69V8T<w7eC$YLPJF7)!R)Ei;sEX@&u9y)*nq8Tk@QNWmU7ZI0gd*vMFzaE2Gk_ciNi__zsn~4j?q!M-W{jvW)XxSa+9>P{0FjA4T5rSc=As-uGBvlYq)F%X^7CAysNP-g^tna>Eymv<{(&3O#6SGo#7@Ht#7;{SI~5uq#o_+ywluNRL^INh6Uih`<Jy>|s8U2XC2E0mY#Q_`r0V8Ol=17W4@mDD1_l?Zr-r2;63qt}y;IMQBsa{ace>Yo_<!DqEzv{)pST-Et)NTJgy3$vCm<78HJyE6A(a^Quf!IH=g1QSH!OJut~<bw1WqGe!Ah&1(UyA#B6CHdt?t;S4<c+{b%4WKHIOpN&xoDYsj^50vPZV=03&4U0PMr)b%AXm2?suE0(S~QGTQ=>GQeJ#9_gKW!_0Cn80@Sq*I+#)FqfXyJ~fc6%w+1Do3SDmsqlE+<dyvCb5>`O4JSVXMG%hfJ}p+{U%T+vdPxgXJA8e&$7{o(Ybe8D{l`de8QB43Cbkoc72|4$ANI1L5krd29wLJVul|Em<4;^YnGa!y=Q%8Ckm5|Cf^jDIdF-@&JVX2^%7O?J%p^sN0Pv(}7(-2$QmorID?K`i=3+F}kqX(7xyNiige@tqt<OVex)V_@i#S#W$nN)SfDy>b0-r;ZC&`bIcteDck_-VHBz8x9945HF{0jW(YJmUyR{nG#&s?)v^Fyq`>^<XULU_ROPKws*j&}x10T+%<Q*a`caZU}n(cH<Elx?RvfKx;(3u8kPOYdwynh5HnjU|DDE<6x(h!gn~j7;jeo%W8p@_~F0l<slmjR`>&8i9kOSi-A`uHuBJAu!&=xwRMf$Q_DUeSGt&gaJDTD;r#F{h{&X2-^Sy42`QW^fSGewAQUtFN`9R1~d+&+aQSfwYoNnAhdJT3f*-iD>>DS0_)@yVa@bFgQoi6fzd3&*AtqJfH&4CcS7+so)l#Rq92XRZ^qT5aG9qd>R6%>^hoCE!0xDQ=?Lkiq6*KTfzHr1{WT&Admvdxm0mPR3ZwK+%tSMih2wOP+;m-hiM`iklxOI$Dm+fqXc5;?24>Xif$)|rV5I`wGc~1P0B3%rON<u{$mzYZ87j+BGo`6Ff7tVaPI@k|H$Xs|q@u()RyZuET{9z<5lx`!D&I_fu-iNfbbibytCRZ*-`vUbxF#G1_N_x!cP;wy(C*E%;Yo6>F*j-T5@j33*G)8O;{0V~gtLoWVFT2fEGO{FnTJ@-Uc73aO{l>&sTyaLQ6o#uuHQCG4daV~IG>i4s`-Xab}efaS<Cx1w$(4!nIDNi)^oy=N!55`l7Ci%6qB^jEcEn#qW29C%`zxEOVO`z(gs7*s4igQ22j@1?8y!C!4O*;hk=-x7BPWyi%S?acvk>u&f_jzzB-$W-mq>4O`boI(NB|KVWVe!bzGsVrS4=ul08_HBy(Tpzwu-M>;(=!Sbo>uiNAzyw*j;(%z$sVa%8e0ZJ>GD%hul=#H5QWhxDgF;mI40dBmW^hrirAGudQDnMBxY-&{TZvmf8@$DfVo$NuqWBmA=w{=M<z&xYb>gZycJ3?Jsl@P1dw@ABLHQQrAi{qgI#Q{iV5^=lf~{NY|G|7>92<!{p)e|)FE{XL#mTs{)M+K=G_{g_|;V}NvVvxIW0-YoB`@W=VL{vCe2_};(h`y}vWY>cq@l7F455?2pKmayyz-OH~gCD14SZC=cNE;d+UBT8M)+QZJT1l@QL1I(oF!}XVe2lUm=RUaycU^F&tJdRKx>QS%(#?}OuNsUN!{i5_4`@=F#kEZn~^ocMRoz<BPT_Ebe5ZckcQ9VZLjP@0lFT-_(>j!a#jl|gCWh!pq#b1Sszq<PI@e`hWq<zn}ce%WvU;X&ho4<bB-ZzMaH@9}#X(e{Qges#z!905Fk&M2*!}*cRcQ`}e=LhZMv^T~zD47L!{Z_l{znxz(lBe&3P3*91i2af--pu^u^}F@YKk{hI>Fpq?-^;u3#vj+iyBeP$>Va=+20pY}-JW~Ps;cQOzBhef2@0xAIO_|_?#lj6tMB<7evsuyehT~B`TNKJx|jc|JpHsM|0G=fZM5IAis`OC3wD6;#N+zcz3-d98jyGUZG7Ul<Z!MYynK`4@}ph-Xs@{bbmdLIeR2ZK@6Gfk8R6JzrANHo`qYHs7jeq=;1d^YpZbXp^~U?+eLHd5gYEtXTjtOG?Hez<{NXc0wEq4LuW~h>^SF8Y$nrdJ^WZF_v>N0$ti<_2Z|}#OM2WTb?cdNgQfvhmP3}MA{&*~71f%>GU5e=ouwx7>_W;p=a*J*^+ou$jy#agVbVsG*5Dy?k$HU1Oe4z^yMXGk7B&R8uVWfnZ2R`R?YmEof+2Bq*q8V!&b|Uv|*J#vbzIYN>dj1uV9y>9Y*)5s^^k9aYpk~}1|NMM5#pL>&2laS~xgXE%vXlz*d>o|HlQo_uFh}G0-idfvuW;fF%{O-Th9(#iAU~~6FTUTM8h(3zT2SK@I$@r_Vs`{UeyZIHvqQ<T-*JBdw&vDW{T$ZN7^;+V2X5^+lPm`cQ1oC%_KcEx=_4F{I@V|NxAhh7t$!To1|0U%sV1C+9is&39~xpKuv<WgOik*h44~XlXaG9Og`On!1Dy!yQyY_gK=MTd8lZUyJ<;uvz;2E=WP*tr7)>*o)*iwq=#X%0fR`d3F(51#L<`#HN7}#EY(i_7@6w*59u}QB-P|#>wN(SMK=DKxN>lF233f;&Xf7AMbKg*c1lnXhUT+rOp_%%rQ^tS!aj0RB=VTCWfHeH^JM>@&G+-yP6laYoDn0W4*ATSCiF8a{uD3z8HPbq=vXu&9Zlzh=A(L1W$C|rg^bF0`EM*8XN*2k>oJuTdB2#eDK8M_6qEA#eD8WYB;^@eGK;;s)i_!b-DD|L@ZUX|YZl_j=_sce=s84#+QeNY~8}&Eis(IM#c{8K&*FFw>hC0BM7G5-(n#W17H(>rK?X@6RNoqga>S6v912ebR3a#M@kdjGJDNwwHsujK&d~6y@(n@JjnIb^q&+U##l`dK|n4)VvQfqixS9aZo4QP+A;z`bxMV*PFOr6#>73#e=*|FuDb#oXWpT>gxybzwU(2*NJ4Bpzy-trf3y>2(Jyya5aw-++c<V7gV+U#M`stRpL!#u*KovIJ0=fiG2G!?S>IqeQ!w(gfHv^>tF5*&jpvnT%h_rUV0pLf{LIFrs){K2M)9j`=wQx{d2cKkyrkf*Jo<piq+$msKwcQwZaR2%q)b3JwJw`l<Gt}taRM$!TFAx$(aqPIvUaHW9m=m<M>((@|xQtt*}cA-!(P|l6cHh^tG*gW)tcGs2BX$4behG?0f-I>=+G7F|PWuhZBaU8&V4OAU~U=XmVPEw7YZ!A&szT*Xh620Vl=^yIT(f@_rcgleKwh<>PJ@9*|GDNx9<MZZ?H*+iERiIBGZ76Wth%jR&9w>tze#iZm_df(qcLYF*s5xrz;0=mkSU(1^+ipCP&p;34x;b;BiGqc0ZlsCA;AO*IwU1qrOd{Un&;_Z5N+X;Ac0o89HSDmZb(;3%RuEeXyWLCypk(_OUSd*UVpw>jSv*iw@e%qKkn5Ce4pZ_NI3|TT^*(>DzdZzr#00U{C94Ry7~RP|@JWF1CD1^0xPRLLtk0tstR+md2ueugI*^$Zo)17UK$PE1_z|=`#*UaB5YdlPoy%56)FEs};<)SpQ2I!?CV}&aaEhSDSU=KrjA3tsADfaX{(Tp1Ylo1uUrXsv?RcWHa|RT)iM!VbwKG}$4!rs(YKh?RP*T`Pg*hr!fbv4y+dHcQQP(C3MaWME1`=hgJJ<DL=;?y3Vi%#-s%(%pi*xWnLWl?BHcE>nB-1VI1g)X2Kh1dXw|kvFeV7?P5S-wmlE{54Z6#t9$=T|lVF4ho2si*7Dpj}GKK6!fA;VkzNPDDP1gsUK2|`60hO(j3#H`8Ep*mo_<x$b1#ScL;DKuArXf2k4;o5|S3(Lo`^F1$m*7}zmdk`!NIWXAW6mZIcP0_J8iGxl3skw@I2A*Ghcy+<N7UqAmymfw~w)GlYzKwJvu!;^8IekdYl2h(}aV65<qy_2m*W|6E$y-ykZDx7~ZPY6&atXbFydDCcm(qf`tHZQbwI;5YYr11GAv^P;2WO|uNOC-_BbeMbRqF)%yjUQL#GUI>U69JhJSeb&oH+xgW=j8rz+kMqc1os9RA=`<<uC~h1|A~QM$sQ|<8Kle99-et985wCXGp`1Q~&N$2#KXX^iD?S1-c&T?uJP=)?(TukTU~GU3Z<Iq>(e>urtMHM%Z<3?ry>lm_+(J3h;Uje;g0mifd4U5B>c*q0eS2#pi^w$D!~!_9Onu$%KFFJ^g`BAG`-h9YxkUKTELF!hH9TYMF@i{4r!$L%4@lb;08ZY7Y<oySG$Ii<Fe9@BFsjG*PWm{!{O(d<=5;=15gCxij5H<@3dG!+7!WX10Ecrp)SP(1TGt=<$0T*L4!d8wNVFbg>81Hqip1ejKJbp8lJ4e!Fr6EW2=*I!i|Hj6XjzJwRr3mJqUN@@DHK)+yhuuQBB3F>ZNJfR=WCD}B#^?L8mslyTUuy?<5T-mMEJGj6AA+T-Y^0FQs5$U?p5<fL1Q>#*j6kCyj1Y*H(0Urf-yaY1PQf=BU_n`&^Ae`K7zagEk|NpgU4fN6&=JcpjVzvy>hv&gc>q}Ghj7I*`p6UHr+Jd{aV+1bNCL;<8|(2|b>dB+f|rKN*Pg)?`K+-O*S2#i8S5=185IhmzsQh?iF%r|m#n%fCt-9u2_2Khdy5pu%eVQQ5Pg7-T~!f_WZ#^Y6)Lotwfvm~<zv+{zlul-Ee3C0BEtN}Q609l(XKCuj#(DV|al8SS(MxwbL@vxcbX_G@!k?#y6OG$Ps(DjtVpEcm1fx;@*NR_ge+XhUZT*viKJiWo@Ih0fxg{$-dQiXSSR5E}o0Qb@d+?*4c-Sy56%H@?wvJn+SG%Xu4D6#gkf_;4bZ3W~P%!DKUy%Q<6V9w%8_Ev!mVbg2IJIwk*)(v&1(tg#q7e$565|E3(#l#|!cCX$WuY-o!NN+PQHOh3_&|8GI;HX{Q`FkF=>E8eC3gF06_FI1jZ8>f3{Lh(04${^7&I`pdegP>X=roA!|L;$=U*zrun*}02FD26THqmpN@NJt2kGF}q-XO#t6#LF})Z^28ge+>XO?0bmqPJ~Ain0vjQ!7@^JB9q?qXpaAFQNtQrql7l{bG1_zcAFie`?E!%a(yRUthg{Zp)y|BDV}DvAnd}H8u|FNs))?OSX*CDEyyz%lM6VPD4M3Hutn;I54Oj-MXVexQV2~fz>zbyn~D-1ohJx%Yd7<+eZ+Q`q?<CWtpg(hr2>w*c56c4;7HB%<={~Sx*g7HYyXNW;z@p3yUgB@4bJR9fj((?}cj!<~c-5%Uw$!rGp?BI9S%!n?2zC@}@n`YqG4N)(I|{4E_M2h1j}DY03E_lTL0Tc>i@rJ-E4=NDWJA(#-|@fl4H)zDXtyv=y&QBNJ$mB(uTt$3*3G|Ifc|4{94wkD}<p^xjwigbj!#4mGlZ5i?;(3`W`}(A5rV4x-^f+h!Le){FhKhv0#!v2?hNnYyo%enoX<V^RccG2k;X*Q88$q}^u`hge&NfgTXdB_`+rng^tK$%U073ZMn@3S&4og7O6K5irSHZY^Q!D2^er_Z_y@J*(xno{q~qtIvQWwt=iFDVAQLa5+FD?wqKFzf$dzRz&&bpQ3@69MapyerU*(BxCcZhQGTUerV=o_7R^S{xXmKhFUs)8SkBshvfPWkfGbekHeAP*hp({jAaLPmOeFYA&l|0EZT<};JcbkyziW5G4zR{ZEa1pNzxW0nrK*|K~<=n$}*yI>gh?hgj^qIxkUHslh0HO8KolCYu^iL;|wOyb6g`F4N?yQKMd;N#$KvOG1!?CjyqR!Q#O=R(I5Y~vvwwNKR3Xh?BZ@Uz!c!e7*E`NHNg92bmum;T!S%GQ=76N`XS5SvQZpX1Dwt8BJ?WZ%)>l}6Gyk>=t2eh(dgDhci%?0X14XMPLGEc!hZCuqP$;O3w?dl{U<Nhd{~8q&pBjfh9?_IiY*}_zB0#7cCJZkw$~<^-aQi=cJ%cgT??-kkq0@GE^e7L+X_5_cWbN6VtNbali4*r2L$wp2UCj&Rr#%J0mZRZJQ!H+%d<*HXZmxP1f3NIDZ;_t2m9ZNfnL2E`xfXOB(O3_qgupMN5Op%vMu%G2ccrMGuAQn+&2t?6B*V)T~;u4BeZ?k$AFp$s=hSyT?Kknn;`;`#&YN9)Efp{eGK;=xytoKL5^lhmV;sC(jSEG(U08p<<m8wK{cQRemQ2%XB3}i`#Yc9en+wNEG-&}fPuPA1*q&GjF5fqgAU>v(4`YV4m+;svF26;ddM*XS>cgV<MVHkJ%aPkgfX19)Oe;A`B?w3qgxw?<mTQ%>HiJ^R81A~-b<r;tbxo%=51j&x-vo7&led>$MiS9l7q%xeYH0^XmoFO(5PV_ot59sLF17Y{-troW91Zc&4}ijG23Bav~qfrWrnKTo9B&ldf8VqNefT-Ww5BtwnCiE7@x7s2-IGgEi?SJPKtDMn>Th41O6Gmj8@~$sFG6Pcs9%E@Q0GtQBR^SiA5OY(k~-k`DLukGK6e3X(e}QnbC)uIDg&7wU?eczYjQ+e8-z`#-<#llj5i(&K4|6Fef=@n~@rg0^pHTf;sC5OP*eF?i|nyIwW5CK=ZzX8Cal}&9VPRa;JobF_QcGgnf_$MIj{Qo7_hdL0?nhVy1_*CIt-U;CzGM?&{NqK<qlQ|N7f+Kxf=dM-(J_&dPM=_-ocjrw(X(U>We1N`jQcsV}$DHzm}xYmn<66uatAc4vgrgoV_9`ytO#DRw-0mLd*@OJ(j%e5PDgWV>esliES58JS!&!f56+i|6!wkX{;2?^qYl&mW||9i&+YX<CGl#^(;w*>IW%DZm1fm+5JEK$Q1#e%5!pxjsJ=tbBtsAt{68tPuD3*yOprleBqw^O;HajW-{dX*n$qpS&{i%O;-l3zXUV1{dV$Q-3X<6CVJ+d^m7^DgEJiVM+o41Fg#LM7RvsNuk_51YoFqJW{Yh@G1mtIUFEs1L-vE3z26NaU_8i*@r3C1uuo>vB{RdN>sXMDgyPp<f(+^WU`D0Cj+}k5x%e#S0AMAks6Z*1+S~eToITFM%C!#y;w|q0y`1&Ysn_5hmFZs*juOa7u7p3BlZCfY_n93)U}WU{<ROYyl3sy{DS2j02wM)$XqnWpI+WPtjf-Dajt^o7p`p%6uR#h%e$G$XT;BQdnH^iZ@hG!8nV5MPcCl;GC@jp9bu_+kZdcQ_DR%U9aTE*y#Q20m|>4*@MU-gB8?LdZcMl|uW)YEqisVyUB7oLL9;TLHd>s$mLGe|N1C*)%AcR!X!)D|HwhMFDYy<B6rk%#NX%EHaZVlM4Xfl6w1C_>q+cv>@g!0OratxlY}l;Y)FZ7&z+XCqM9>IM5yn5<6%@wT+5Npao@Y)i@xQu96hfEtCNb1Y#5F+b*8+YQ{?0ltj4zZ-&Nqg?tA~0g)xZ?aa!J96s>b}pL*l{k8mozBIh?<*;ocfbuV5Fo`A)iRVj>Ai!D1+5UtW;7(y@oImsCM1T#L0LpYBW{sXE7B6Sm?_5ue&JR643T!bJNbf#YJNbT?r}_;bSCdLFoSy6qS@lL>$jBPGMi(9SP>CmC=9Jx0Mp>R<5)_Rv#;)Eh$5<WrMPq6?*e&4nRZIbBf7tc8%B*BC=+pRwNnnV=2ao1!`mb#=WS!#=r5ad0GXrY^cZ{)Esj3w$Z3|8tCe>#aeDrb|D;tGX}5btLGxYoMzV)rrT8)lcz*;I@w5QYPk#wF2Q!#ANPJ*ORDG^>KE@YN|{87XC!|j#K@frn&W?dTl74dK^Pgw0^YLR?bs{zd2apn~$)_e(h!2*w60oehJ?Qi{bvBHb_F|JzdEKo6x?S%OBmfFm`Ccn$#_4%d&3X#}5~qcx(Y$T}fBb89J-*TU?|^6T`8naBQ|LElU(O@a*df2n&ycFOxn4mQLFr4_wAv0p>px4wkIs77&eFh!S$va4MEd*D@qrdj?aXd6$L7xNMfbHaC}FGk3o`uvgMSMpQ9CGTyBH@{aCNY$5Im8-W_LlhqxcOood*p77vJB!DtV$ZbbL&k2=87n(i$0XFhcn9fX`Xx>4XJ{dxUi32}2@`XDJCp+P<@#lLwy27lAWjLV}>t1jcpXJV8T`tWMXU&Dm#?CX~GU>h~XTU>LXRp}l6B9j!2G<M<qXB2k;{K+AI4OOXLkpBSi|dIWWvvyPSrs#B@jLTbElTl#ymw}B5OwD}d(qvE;mqJl^gp_P6IM^9@c{B4z<Q`zdCs&P6LiY#s3=(XP4AB`zd|I#mKth7S-n+?%gIdxA!;=KUv8VW7mhorbcY*CYcwrIbv4~U2Q}@g6FUm*+M+?l4V)lkY?v5UQ*4J-V@)N!v@2B?l!Pv84eW-BAuWU`HLANzw>e;(`OKgY!wfhx^$ADDreidr*4WhGg5F8%@0zxrjI@a@>BO22P++BZsWHt4>7kJ(T|drnVuOw;*rf4ss!`)$+H+sskru=zb`4>47L$Oj{x&`KY9I)_aO8%PfNq79IL99lD{1pNW7^QXil8SKW{Hzt=Q})lc#o)sjBjXG%JY<T9uJ!{>5D3+Q=hxz^#_rHq82hTvRkIQzFCa-TxdC8x@(KCAYz{seCr_m@&(?cptnGG_0~3?znK<5-|g8nPqkn+cXT_#?Vtea){O#$%Jj8&5brPA3Go(>DIShSga>lKyL%VD#ZrYZfLkR#^@4ZYLR~zfC>ns&699w=ZJ$)C0EV{4Aa^$yo5?T<Y=K>VDG#cD^7+EQKyA$&&wGLENKPr3C*mwW$eg`?F?1&0H0ij;OQ0gd=iJc!v_5(t_fXw$O^iSBQH&*zbZk>ij>4fJ6)>kmJvXwLN|ksOIE|bZU_J_Lh*vm^l^^La=r@k2KvPDnYv#ay&aU?ck<Prnqle@f@#xO9cgcDP28TiCi}M>DdO8DnioZrOe<fpCKV8owheb`Y1&BXPo0a`z;??%3S&sY^1od;@;SNaGX^c`yjUx7^-&wo<Jv7sMBd3nhG}FViW_n9K58NFXuw}PWOP90ig?zo0)}E3|H=XoEBz0N)tEM`NOHNs$1as+xLy^~kq>)>mRP}|2gSo*AI<s{_JB9)JBwyd5AQrblXz1gjmcB$M6ijEHmyC_Z<J6r<291CAorUW!4Fr~(K#b`dgzG~vSnpfzLkC3(Ch(8$LzAq(xDV4~8-bSaPuw_HV)cRXTlC9)$k9BQwuBNTnk1*eAb7XD{=mlT>TWPnZFfU3Ef2JC4Fq{l>QAS-(|8qX>nl$E)eWh4W92H)EUo9;lKxBGmi$gS_Rrjz3v$7HXF9gm;m9`kUfl2);8sUzus$Yk#h$GUgQ~5S>Q_z7!XVEzH)3Jj>g^)3NIZhBby}kF2xv>3=Hd+1x;-2E-ppxm1N*thLN&xhU2nyZJt{eI)mourvEkJECLIgp<ivuK>??!u5tuBqPR7KzWW%X3z0|JgsLD*8TpzoQGH0ju(QSC-XY8M^$<R=MnZC+0h~XdCWa8IVlZn6j!L|VMFP1If!VV8xKx?Gi77(Adub6k^7jFSIB<r8q0t$|}>n#Aqv#Twj<?Pyx2cw(V7O=Zo|L)-077)1jPwH0sc!%he^bxN7@(x>Z`mf)|y8=eYPu+^EH9uEoX-<TcylcyzvBlhST~_`;7>M8tJ2K#7F!H3Vg<B18UiLJ(QkFq_l5SBw0(x3F@ctCa67;mH?IYNy>w+u}Om@P%dCi;gixxa?RHxP|usd;Sr^=!{X#GEer*2nFAweD`nk{COby}AGDPE#;Vo#7d6@^%-yEH9N30KjYr*p|BUDjclU|%;|N=)5FDfaluOR<0TeP-Nqi~q?}ra9cRXucdYz5!;+bH*rp4cltQX}bA!SjJvmT5kuqPNC<$_5xtTF3uO<a58dYLNh<Ftxr}yLq5sK(Tn(K;Ap<+&=_i(YdKz?FY-1IO8z;w#7c`-a}E1fuUd1nGC{Xtw8I4lT;FVP)YT&@oCV4!&KDC`sBdh0!IJp2jXnQMR}_hIeujWX|Fe|R{XIxSn*?4H6ix2k=g2l^1@$-;FwQwnao~+odii$~@2)_TN(2E^r0kjuQ21eLPwwMcX#18=Dq}RRtP9`MBQWNx&t#^`6rfHJ(OI?NkGx1fUsjzx7jN~A`DV--3L%{F{_pRAcb1z)-Sf`7NIwzepD-)GcT%kB`RWWVY2L;JwdP&<fB5>l^h*9kcPx*Vafoke*RxKm7T`O#>)(ufi>+OszDm2ExVP?!e%@ur-ipR=>DW)~*vH2m`)t6$xnsXut!*nQzqy~cqBEqQl0)R|m8$&c`I-2XF=@9K^aKdk5~QkR*fHT;3AN>Ek}11nbJorjxOyZr@GupwSuRE9z;s7cVM~)Vw@EszCaJ3O=F>MxQCQ7cyA`55OMpVNb!5h|I8sE>G-o$10}kamy(1dZXL{#0^~a(nnaR!wkQa;-OEZi*l?-%7K6P9n&P<!r6iRq;MUyD$nNuNkU7Tk6WcpX++&1}7)?~RRz?5KDpn=i+5;}z&_7_@}PR6^lk)HGr%p*q<Jg5!_6VA!ra$FwH>=de|nVN=*{TU9yq!Tcxe5}9qUKULgVy;PRMd`A16g<)e!!J3ISrvTsYw#M6_yxbla;-^|N<zTT;I+Dd!r|*(J>x&}4u|6%N)xyDDCy#GJjn$P$6&a3g6;`sBA%7hg195a+YY9>@sd3FEiAP78K-Bkvyv^H`}i4ZyHRENiIM=?u*Ij31fL&Zl*3)`CT<_V>_(0A0momxLLR`}tG}#A<c;;9>d}TbvoXA8{eZsy?H-dW(ZdT#=pJYlU$bO#cW@8=r#tex3!L}M&pS#P3F`fU&%4e&hhJIsL+gk>f8O=&ybEtT?_xu!<+q)8eKJ0?e{|$s0lUA-k@wS*H~qDrdX!`=<ZwJeH~5Ov5FTz%(G9M`E`~YXn_?~oT(Et6LClrrfU8+U>WtQTAHUYH>!)E3VrrZ|de}AKSMmr>tFVjYeS|2q>GD%UwCTjo&K&8kVy?KFp;Dbehlm+mB8Jj0(UvZ<%u@th5~rcEi-IhHk(MB9)lLP@Y87hrB$9T~%~oq!mWmcPE#Uq>T!&hcb}e%@$4;lFg+*A%)R!R3M43%geQ_La>W2o~Ckqvycf*M<E`(YRbHF7UwuO(auZ@qeYm|T{O_*C=+(H|5wO6{U#n)MX8DvRqu$f?ID{QTUtj-$u&&FBZ5@(^taKRIZLfEXLMYoQ&yp3uJyRUcMjK6Jr_tuARzpUE51B~V==>Trrm(}jLu6cRCVNFO|c4}L8yhKT%eXcFdnJ?faP%2Wz6ICr$H=18FLb<x{XLH__#V^2mk_adimzuFsENmJ6hEX?o&LB&NAk);D`|oAwJG9y<WNwJ{@U4$a2@mUDHR8!i`Oqv9%RKu8fnkT(cM$@DXpN(5GUKU)Rfl4jru@lEmzWU3a120F#TAkYJ-BbZ=MGq}fAg{(P<PceD(0Mca`W@i_CW%AM1Z^q66d`yJO(*q0$wJYZFL2cxV=a=6J-)vPFm7T?-ti?+sjlD4dEhIb&{F2?XRVoet!OT<~%&gG!uDqi+rZ1$gCxp2FK{Q{cW^sa1ATRwC9^Aq;0j45|mPRyG%B1Zf>~!4K1Zz>uw7AVH&QphNyrm+|w=-&*oU!G{^j770<ZR?-cIS>ixc5Q~R=8t^gS&belG-jWQT^isRYatt_i<z_STy(v`JEDk0Vfzf4P8NA>GYPXFQ?_sXZ@+*f2rURtTw9b|X1GC;oN=D2HAWj0>xOPtqBBtWs{Ri1@Z6tq$s>wpk%5)N6u#T=SEan?tcRk8&J`HHqjc*d3r!HMm^)T5ENCh3(8Nzf7^ZNxm}ySD~KyA6bRo?T~vWa5gv{RpKEvFvi#Mw=k{1~W@>B{vTQzX!#Y9mC#keYZbNL>d2s_h<znJKjrU`}&4M4Pqq7EJnC$Pj1hO&&F#Tx3EHMvgg2%EzHE0H`cVJ&`k-QAb6n#IEBkQtJ|SDV&8jeNFgdLR4NknhUhoy*{P{RF$5f&EWkC@`oasCb4oHiD_SzWNz)=%31Ht!Bb7;7l(~x?TVV9z7!@-F(~2@kowz(g3=tX?CDh8=rXCEevIr?@rb1Rx;{YnO<Zqk$G~Uu?Vir%F-k7W=+>;f>1K4&GMX#!m=Q|0$g)`V=M0b0*iYIb{2{w%WkG>s6-p<ytmRUO5!TK$QHr{x^^q!CDR{1QGDa|Mc?guu4e2E;d`9ggp$Fwe@M7>#Nk%yIjK@BEyoQUYZN>}$2RhJ|U5zXM`AcJ{HB6aeUVP^#c3CavYunl^=4<|g6Onk`Y)ca6IGIZ-z?kM1Y!?~7hE*x%}LP4qlOJt@L4_~_9x){wj=|DUh%ID;&HqU8QUGl65<%u^d1kZ?SLK1IU5)l-yG$p$tt@4#JRd2bm8YP^@Mrs`-Y(h<{K&<hCvoPCavpJ8grK((=<y{+hgQcp!ujr9#Mgr}}Sz1cZ#D3{!FK$)dxfX=iF;OXMjgkS*v!!l6!-!}zU14+@dLN0-%@ff5unIWgBmK)S5{#_x@w)^%Lh+3|C52csY8?nTYhc;kyGgWc%IMPQDX3bW{bLaDQ(w_Q*z8}ng1O~#&e%bOU|{)V)>|nmDRC7jK|%P|fadWQ^Y#I1bU2)Th^U`_>Nnv_L^9Z=APMcm#LCZsvm@OShh49EhwFS!*#c~0d*HixHj|qWv8qvoiRQR*qF7-#xlx43-tlyg;n!crUAffOJ-+}EdX<~i#7yPgyk08ku0N5RNdzxGm6g$u0>v{^C0<A@bw$-UceNWK8UYe1nSwwRX9}zZZU=c5bcC2WwxZ5ZY@2pG6j{c5N=tTLJ2h!J-2GW#D55n9*H$h-E#g>_=#G%41N09c;Wj8OK&;Z8i0q4v)>0?e!6t8PY1o?30_f!5cpnjo`R+XxEk1!+oP{Hj*=*@Hs!HD!Bm~905Rt$Y9xF&NCs>O}gtdsoBL#_0rBVs1CMJPl7LnlH?jDIqH2LU4jpN?HXiw`%>{wMKz6>8AJ+C8Sc*i&DNc4mi-%5dW>uc~sN46)VBsS8jeUX$zG{VZIl*DanL9XdY*hU5^iB&B%t#ME*5eXIl4q=IZ!>5XW|J*xoJ$1tN&(NZQhI$$Yy+L|xu)85VT@XTj;Am8GO-2lxm#{wLnaPSkzQG^6LVC<x1foPdfsfp-XAHU`A5*$Ra3;;z`s7VE3|%0nNNKiYY#GW2#hZ$$)l)QN+-}LHHDwBw{fLjpsape<8Y*CRAFRwXwEZPLwZHh){xZGz)P0CT`(pbzfwR}CqXKxR@20v4DOl`d-P5`oQh16-f1`jddcfvfM^R71S=s}nNCdH-Hd4?Hy1&q)#*=}@3aNlBj7RFz3O4+D{u4^#JE*Br9Yjpz3HTDwZ#_ItdXhOZlt!=`dk~GWmTIJulN<tK-<~$G+tQW#BOXMqT7ZKEi#de8;L3Ruag&1w&0RtkxB})KuG1du5=i@<W*<e=W_A00E0}-rj`FG_0?4Q3RS`Hpl2;uV`*nUtvONz;J7ZZAAeMHP&|+o1ZgB(lO`q37%#0_7jS+=PHeLHnyQd;QoeiF8;>$tG%f6ct0M111S?9!ZB%GU7Rx@9syec7GRun^T0-NgM0>wU-`9ihGwy@Z5GOBSU!5ka&)S0Aex0Y0G4X{k{pGdn4Ev=-=toX+!^*~}Ge_ltw$^q*T6b3k6y?3=@NyrPa>FfDc@83Bs@7~zYIFjBb8G@~zZ7}ZG(Y+qN_BPlbsWZ1cXQLA^b4RK%gH4+`h1Ca)knW06IAYG(KJ{G^$Ty0oR+HmMogdP>wYk->xeQ=zQD(~mu26T{feIWJAabsClxD2+ZUE;@DqWBpWyO8tQMpfY#=+Yqwz`K%5W+qXP$6uX`XF8vUVY!xM9$1op)e`w%{s^V-g*lI5qQ&2C-siCRxWgAb#?J#&w7_U2I6KMl_R)rjH|KuQ4NC_t?Q^X7#OL5TXys(YmmJygQ<rS>o~is$49KIZ4XsnlzJZjp$mEtHh*%H;BuM>Ob9oCRvuboE1tpXf{lk?tajI5aS!q~YwJL#s5*DN_f(ps2EwuVpaiS(A%)uG<D+_XL${TC49MnWXx|whaA2kUUAI&Cg*>yJLNDskc3OW4j)mWKG0)V#$6_mqf>UFI^m{h8)@s#w5R9P3-OT#BV#O)ufawqz7;z~Jh&C0B)wL8~FNEy5g?6jHLXfpgr^>);BW3+9#94#ZNFHrRy;P`<&&yLcL6%!KNHVH>eqfPgqs9O+O(W4vowiC@YQeU^nf9=+DX>Ydl&t{;(qo{&yghCgIi*hv5s3fcSDJ&Lx#8wo;)FSwyjm^~^AL?p+BusPX+`Y0sO(euH!Ie~(Ko8BKM}?+O>_#8h>wf1KBq7hL!eQRmEPHL-KH4(Ry#O_p&TI$Kk}yzt%A{#r#6Xl(4^CIwnBK34swS~ZdGlfn)`;9&e)bqvpMJ~N5W!p{iNrElfXidV=3mE3qyl+);qIv^-#E>wDHb;;zED=zdqL9#MyDZH(@-KuKNv|(?$q>dWTYqULPFR%~F`em37#cxOvUV(0aF;gTIEu#WfL}&;A>P*|*;o+q3L@+qMGR=j)w|+g6#kEmbwMl{Hgm{u{Bmtt=Z>vk6V{=?!bR-mpk9l2cn~({KZNw<k3#Mq?{7dlwkJ%}OcP%70_Mm(hSpfD^1QFJdZkLH0rrCP-SfBc0)m`&vuXJ}m<8ci+2LMZg9yHmPlG5-w1?s*VKOHN|R5z&&9mLawRVpQwT@91yhySZKm(KraChy{<@vLlq>#ZzmD&SwE*By4_nTPO7-XtUd_d8LhzHjF;&X9VGq)6eykUWb_dz^*6hPnj;IZZ+L=Nle6T!2{^Gd9L?Ebf(!;h?9Gsd0uF^5cT2N8`FbRtm~iQ}^lza>MB>DPpy;iM2=6FAIY<o`1`tSDx-A9l7%C1dvqy=@9LRT3#o3u#bNTIMpZfB8lgb~uXX4-3Gl_KeNSCovx48c_Pmkx@Ce3wtW#Tb6Ojb(pPZ@VGn2u5CvDh4<Qd0&Ia>o<$GYcI(W#99>5eG8GP)2PT6v>eJ#(;zM<`OCyR&A5bW!vQVl;RQgg+KYu{Nl%VaxSgaQ8-+Zi|cKC6SLT-g;|W;1l2XN*tI(&(-yy&ZQ4tIv5gR7;x)h6`x#I}?16gBm>sIL4HAM*^l4O<!BAoZ)`n|rq<>?v!{V03m(mNw%H>q!oiopZ`mRo46Rb8p!fgj2ne}}D)NqfRP_KWi!L_gofBhq!^ZChhewa-Pk<VQ$stc(H<f@m4yw8n6{Ombj+}b_o(K%0!;Bv@cWhL_=PlqyAOM|;O<h#`&Z@EeD&4s5v+^yDOb2^?+`}!#lkJ1zGUUb?|b9yon1R7g;hgiGG8OoXS0`n^diS40GGjgFq-mB#)ClNt1uqQVv@;KGr@h?u%aCxNHwH<LCJ2<W&M^jtXW=r=q9PBRq&+p>1dF8MvcKg%2#<SfdxDGINR{rASbJO+-drc1r2fDg)I&R&;8Cq|UWlW$Mvq|V(pa~t%zA%H9f^;z0CW>HhkRsnEX?Fpz??#jc)qUdOO|R4reX*?*C`w>lc89%PIYmpRhs9D86Hp4@sO?WyzmTzJzSbR&0*XqRi;aAz&rY*jBg$t6R$hvIAg!9}QT-G*g-6L~ac4c7=D73bZE@#M1=;aG`&g+HvZuDC(wOVwbnBkkPuDUn8QIWM*(p&y|MgCqbdU)yx@6m)CV`6K;4XEMC<$V4l_K$W&&8c|y?f%h5Yve*MGDvZ=Gt|vA&*~bIo8dZ4zxnpyv?6*F&m>qI-+nQuu@o3B<!J_nDujQ=WaM-ag6qMnWy{rn5QIcrq(W#BmiK@_4|L<{n41d6YKQHpxz;du7MBcOMUv0Dt=w0Auct@cAO)9Jv!O@rn*(!qm8f5Y<l1-WssOks+pg9zJb5m$=*Y%oAet`#Hzx=i&>}8B)W$?DJRy~>L6lQqu&~HbwqyPaYi@*cEIR`JvWL767G`Vi;2)vzm-HE!3EA-L0P2nl6c)PuK8RrXeT=^X?=va!5P#U$%6v1jI$-t=SOMHI<5aMQ%;skDl`)8NCdfxR*8}vST$^&X9LUeb-{F!grPQankGgIBz>UZW_?IN{oYygvRS*vJhNFb8S9zKjwXMV6jOWYsl`^4NPp`Sf+ltn<!+#f_zs|nl|T=VKg)?0=mcyauh0|a3Oy029OK>rK#|+it^pKqnq9m&)))#Y!gd!J3LqnT*KDSr2T+*2Mgvf!6@X%DX43~}$D*1uZ^2MB^-M1?m2hnrFp6e5jZToCxMjpQ!zdubb&aIh{1hN5!mqrutlt~by*)nVMY=b%C)ATMK9}wxuQ*UeN~s^$2ayz^X%#(6^oo-l+Le$L-8N8%MiQ_54ju!;jMq}}*b~{;^rJe=qvE9^#r*Ds{Ffy`%$=N?Y+Q|rHf|Vvzr{{>EAgmVHY&=yaHSlT(W3G<Zm$O1KljpB-h*u%bzg|on&fumGhM1D)|n8D4BWvo-Zd8Oh^qI5A7c;f1j%!(-PdhpFNfHAKy18F-1X;OB*2jbMaB*WLxg<rk<W>E&ZOx+A&cdppdi+<UcccI6)P3-06M8un+9#bZR^f<L^rQ4?x~49C&S<}Sb%{9ngM}JG}9VapXiP&zy5I_@f?%`fde+)Y2V{%6Q5RNfngVivooz;N#WLa^)G)cxx~vfI_Ei^dAm>=RZizZMmyFt#l2YUoahPAc<evyM|Zx>@=iOa6cZN=@6@!?<iyzowoy3TYoa5_V<yt%(kz{=KW!Trv7Z&w9w{acjx}$$sTsl4roM@$F^?xqXw#<tL7;IertKvY{cqUaxcA}yWq0F&=i!LX^&^}L#%zd}w}KFvoeY36v!6k19Slm4-5hT-ZfjP~9Tn<zLIzaFD3x9q26uFdae_hfU{pgi3CRUyQ6Y#FBCkSn?SiP6xNpFYF7i}3U_~jdFWU12+Y|O@Dw9N$dIki99tgo8ylBVGiW2%zZ|E7aXQ@LFGm5Bmi`i9x;Wc5`!Bjw45oGME!U5oA5mE@A9fw4HZo^XlM+<HvuoVAUGioAqqwcMT2mnW^xt4Gn{1-CYTlh<75jGfMWYHyFrEa6=I8JUM;qiPN^r+{$LHs&KAxR><s0B+6-fJB)KF0f>#b0=0IHR4zr$Rvzp%}9FDO5d)2vQRNP+;p+h@~|zZ(D3$r%KcnWC-t#Z$#&XWNz;GlMb05p}W+V3t2`$+!(VwZ(VCJ$%BHRU^|$MrD9b~l0?`D0w{zT2@xR%)K@eXf?Z$9pQj0qpi0en-pf@-iysiFu`?{wj%9GZFDb0D2E|N+m}JwjPRy%VwsQ4+8N}!?HFPWmz?A-8|C=j|<gSS=*SD~bq7E-E$%XP*Xky{Vx{gUdMD7WQO=;d<c)v_skO_FfA2U-4ZwjT+^n#cTmS`e5!8Z)2CYNKQvr~W<LNiB)!NtbbZM_t0=ZaK<)#`gAmH8|+^Qho6>-wqD!W&my-;BIk2~uLV3o@bMHG_DL=yV%h+_cYVH>eU1k4G9YQx7IC4IHY&*cDco7^S<hNKFnAh-7~dJY`}co6K2g3QRM_k^ur*F5X^I3JuYEC80Hx!kUJ;@P^xOeSA=_&aa=wZ?d}}ZzkJeFaI^|AX8FuO{hra)mdWP5vR&K*s!mbqKRE1xj%J7xF-vdi#xEj+vFq=px0ITR+Q7saj(~Z?PWB{d+MT$EbT7O!{QsCH>}>91mj|~Cnq;QGic~-?Y4`ruBHjR41!5TweoqgNfH|3(=W3wu$6Ch6L#bXAq-Ydv;mo=7VP3-#bc%0ofkwgez!R{AAR`7%eYU^aXPkw?~y4&%?SLK^oN}nw1i40(fDMrT$T+kV5TS>ArPAxgH#JH^*Iy6eP>LvUc2UOI2<J7&q5HED19Vm7iR>T(Hz)00e0Isu%r&pE5@3NO-H1mhyl<`l$LBAq=7ZJ4R);{D9Vu$(BAbRk5GW5{`rZ%+ujJxY2}WMJNio>et<WRgCGj%#U&EGih%lp!bqN7oT)5x;o{ul&ejtpNN5J%u6cSG;{~v8w&dQx3k$-QMhb`(#%AGMPii1~Pzg_csG-~u5Mhe7*3kI|!ON6q<`<zHQ#eNWU*p_puEN7V^ub2dR3gx*vB_Ga$?Y2Wf{WMGsvC^P8Yy#%Dw)PIGcwAStd=AhZB<>UZkkCO?NQta2hU<28o_l5hkHvMnVrJYvJ@5~Hla*-en$$x@!;#o;dXTz7zmowOK&DX=P9B|)_cA3ANc?SGpF{)wwCAYC!rEsdZHLJEDJ6s+%a+)nhZHn`g5?|Y?BQX#ERhrtz(sK&5J6quNqNCLRBdu_1Q5{uQLyCxVObS45X|P-Zj)&b>t}lqiuKGE%PbuSqfkw-CS?coaK}Xi@o~kJMJH^X?o6n`Z+WJ^3VBcWN?}hkYH%`96YA!iRp3_(Y?-`2_2wsNuNQHuV5NG#5|qt_W0FQKk@{l0+Rj^CQl$2knUIffpHwn-c`rn5)M2tt~>~M;^`tv2>h)d7)u5sHPUBpRN3-~T?uQkk9D$5PDv%(L1%t=MDS>4s5e{Y^7G*NVPo?oj8cEYHr??wNor{upC8vb(zCJ7u)Al2!4tFdo^wx(<UZm<!!}M{NePn*h3Xat@+_DzkZ6%8G#Elsbu(>3)3&IumpW-lCuhf?H+Pc<Z;WwsgyT9_v=T&QlzN00qnq#6izRN7k4xaw*?Z8LY4Ma?e#aU+;DsLeLZ6}hg4Y^I@$uX((iqoqTVSa<hbD7G@0(-_#IxFB3!q>~9lVv|@#8B6gO-U}+`ohj3dD;3JbsHIGd}gCD36*V^E-*)#ZbAqPG#@cdYQT=eFRJbfHAn$Z(>9A5tKxQPPz@x;g9Mj3bjVB5`7aH3A4o05@|MZB;THBaZoW}lg2Hq!%6#IHw&^w2YYX=23}Tyn=|d_ViF*B2ZO2ksKGG5a9D-3v3)%irs>PnPGU_{Cn*fCgJrp8&L6Nj^b~1Pv&?+pbIyP0X{JO%ihUwe;(#&^%9Pm4BZw2JW9nTz`VC>lmtZ7V4-62&?kr;ssWmtX5s|WHx`Qwb_X;$db{nqji6gg#&CF1<?<2rc19dA=r;5Z*1^K8mO(x5s?t_>FQy3D(e>Mn4r%ZZ74HW8jwr8xtFOj10HjADhp*nb5K|}5qm`A^H^)2DR`6~<m>6;%P4x5RE?Pefs6ZB(TvsAGk^>o=dGXnLqf_}v`f`Sk+Sj(W6nXF$T+7Yey#!OBK_19(z6tix)81+*m?#C*iTD+a~{pOM&3?02l#e?;3q<@J5M&~YVQmJP+JEdlIaEBTBGDA_6llmMNVpE_tKs19Ps6%k2tl(-w5%!o6<r3sN^~S*&F8e7WGeyShM7zNLJE?=^g}bya4_4Ga{i13+1ilg5?Do`->a7udyj9s9MsvA~hg%J*lu;w?mta&PdvMb*u20^A-#5g#hXG*NE1of@J^(HuSm2e#QabSzg*v+N#1#Sz7Cz%9(1!^56_^c&fl41y^{#qPZUOE*X!os8FoZ|k-I`l?v|g$C0fzfHouf=tSo*>{&o`KBWo6to-RRHpS{H4if4vUmq`l~Y>+O{*j8{fDUNIK(T4rhU3OidD1cr6-`*f_JW(8tvD^228`9Se^24avLr_6!*3m)iJ$=?oIGZU55awuZ+4^WIj7aKNzE?f0STQ=YV3I+>7c_1DHg=0<#n>v@($B<66*S}I6L|qm!W>Wb(HZQo1{Wd)LCCIN2OJOE3P&Jun@6Bz`o=^A@CT<84`J2yM<2eL_G}Df)7wp-7g^vvWrc^qYKg<kIx-P(I<JYh6*sUsBY)r$963f6=!jKT<o+Yi}%_pSi?Yid<Nt{Bz9CIkgN7)Rq@FmNRJd#_5n~BIw`4P#)taKJ{E@Q0DlUWSMr_3|5STCC*8)H;uF`+^n^Tudno(*D*RL_sjn@QCg2@#>_h9y+LvL5u3NDV7T!{r7>EHD`ZU*Fg;f1?U8-G8QKq?czF8jl-Z-~LtxxAj+eCng$26+4A1Lu7{t6AJ!28@7$mmx=v<?w*gFFKVa*2!~3t`X2E+5?9I|38jUNxg-9I*2YB9uyerj<b<+plGX?d%@P-8e8?r|S0)Qf8HsHX>=F)H>kQX0owm|^{#gFR2b~Z@gyt`q`FP<`qRaZUls2QaIlRTI0afA9Y@HN+sl>bf+xg$vko1!GOG`-Eo`dSLnZ-6EERxEC_m8f2^{>4#sVA2u1hx1%t=`7+ep;9s%$?J>G4#UCdqaFSCNTW6gRx_lk?Gv>hW-48O)y*ySG79gj-*G?Mw?>^wu74{a2kK>Jy;kuGE6tbxO;SDqA9t1!DgfsEtwcL4*_XDV3opo)z7+NMC6KNhCDJ63d{b=n9KpyWTdvOAWPx~X%SAULBK(>?lUyGbYU_Hj&q#Cuudd2lO;E$*@ffB=Tp6udU8HMLw(?y?+xaJ1~o|*n2b}{6$4+QC+4v}7|UZb-!_oiq3Pp@f1YT^*mM2g%8KZ$kVR>>EJxV3U?)(p1(a_ll7xzsGiR7nENIN50No`sqede2-+h$mw+`*_Z1ihr+n0yFBYS;8lIPLNhfNc#Tt&agx+z$MD^S9IjpJwc&$Kd_=x&?;LT(Tv>BG%2aJW#nMzhWwMNG@u#5CkhO#R~7QG}ULZynhfxWZ@9w>RXX-_XG|8bpV-(~Qp(XqBU}w%DIs;S~4IdN(svQMD&UxyPnFnXaIUga>9G%(3GHS#aN!Xxlg~{8`L1d}NWy^q1UktPZJrmt#AmK3|<skgG+34hQwOQ2m>>05TFoMuwr9rvpIDbtF!83hq#Ls)Mm1Xi*&=)Pq>ltf>!jUs`?NO+ohL&ESCT_|Eu!fiDsGHo(mB^1ilc<%mEA?RFSrkK$HomKiFn>(u$to5W-H&T1pxwi4LT$40Dz&A1fJ={ofdQ46%yPpE76x_;&XMEOA=zyh!=^&+F5IYQRgckRvaz+nM{<lWF>$S&!O&dmWmG(A-Fs^<6g6H?5C=TTaES!1*k3XN>>Haw#RLd;T~gOM_q`e;T)_@CZ?yD2QA=QmQk*4xcB%j;4)e~q3Vjq8Q&rlYx?Gju_0jkXZzc^8+xMq!EIsX0i7+<sNc#TGOAYZC|RzAgg#t?|)z8CGK>?`+fSkpQkY$8?zA1u5xg3a4}ooz`jgjem{|rY0!%6iG&St@cYw7>*!Gh$MYFs^=@pplnLeajfaJ_P?x2Dwo>S_Mq^jiU{80g{1!eliNC&=;d4_E3HVD6OeER*2zvGo%+-ObWYniuo4GZDOyH@^rt=z3=tC^0fwc9KZ8q0)Sn`w>YCSJq<cr94u>%Y)|!wYl7I)6uEVIR8xOA}V{@9&?b-J22wU6>V?wj@Kxti`ng|e-@(_do)W#r;BVNvTJWPA4MX6A^0cT#Ij39S(gnLNGMhaxJPvi(E7Cm2hEw&z*vjAH5P5+xB>$A8K!TyHQC#x)xIJFv$jBLF2DA&7lNWWMRwKCX*!*&Ni5%!-=-5`5RmeP?HU8AuS;ldqdi*4J-_ZA0qjF#fg8tc^2?GK*GAHueQWV#v&O-<?d1o0&q5F~Fk{czI<C37>vItk~K!<5bRslJ&nK-NJ_o-`4He@%EuAv{=30rs_=DXTW{P^JTHR{aMx6fV@h?m>~8rs%$AQH5irFkR>{akVj_EgRI%<fewU6tXrNh7%PMd4FU!8rVdGTLJFXjw%ZPo8jCf4V))VX8QJ>MiqwLca#?ZBo<yXuH9pY!Z+B?yuoFqj`Es&PT$~3J$JB@Fe6x8;Pk9dAPj=-yn1s}--!!=L-_TG?PD@^WfrLt+893(<;Yn!92cybXw@-y^*o38RZ)h>0&v&F0kU)vH+UyM2yP1*25e6z`^{7DhH5%B_dN%}MVz|-bw$cQ9#K-n$Eo4z>)A0j05e+m+}Dd<$-GtZRX)as^?$q%e}K;93x$AfOgl_v)1@Bfic3&dTmk{1q-2LDu!uwo!8Lz?UbrzlrVu=G_gt6*3_z}!1LDz5Gjkwaa0bd_&Ok82Kxk_6nO>1kiZ0G>z^M@+o)BGBAsd!9Zz2q^Ussbn@O^KoB2Bm1S#FUry%n`%ev#ZFl^d*jbuG7;7rDizwWu(C%}nCGzEE6**4U>P8pk;N7cZ(DSOB<UzC1_pZ*q%ms>an+^_xuiRx&N&wchJ62Y`Xq-#Oo$2n-h#adw_{<`t;pp(&3<A@_2S7XY<FcTC?1lPy&1TXk3#i}UnoGJ19k{452_nV4teB!=okX%q0V^K5Fg%_IpWglw`yn$%MF-pYyfbuy_<UGp#CjO!>dg{0MEBKNJ#&~FwB+_Tb0Xq|*(H>-qv(pmNoyp$Jl4`nl;K^|C7Ig^1<W0e!{My&aFD6RjK?l8a`Mf?x8{~x?{VPY^c+Yy$vA}2^m0;tJJOS;~JGj2GZ18q#CpQ5k(W3Whr6f>OZH+2QDCWQi6P=__EZx*3!HsPgP+92ZJNm&pZPj_ZrlI5WH-+!>o>(OB`6Ih>6hVrZYi%)pFdl~mV^gCT_+KJB^n3ZP?%<`OtnE<oZcgAw<UUpsI;n;Vw(p!tAY8~>u0hg0ZwKA#D^T@*tN>VXwiW^kgN5Ow-YI@=Up?N@Fe@{|>l03JPEU((1p+6J#WOhulfYj<|d9+J*zaU66!Jl%2&8Y_~Q%Bxoj{n!SGGq7Od`QpnN#+?(d5#y;_-y2j%RT?`q$^%dH@cG@9mqsxB(S~Nj<e-R&vB;yvlkOLcF}O!&M%k`oyVy*(O*#)d0Ei|%gTQ|a+5CXVaR+u$>=_rQ&Uc+8`578`JpNkDXpQZ^9Y3r(s_AA<k>hcUWFbccn1@09A*a`mWgn0(u&33LubNr{hk0Y1R!)qd4VL}?$f6D_wQ#IWeCP++@j*>wWhD9VIZl_n`hL}fIh-Ig{~P!%@dQ@@W*pgW_ey*B0|mTtJc%$#5Ein#4$*4s@10w(Hw>lUrd-7L*uWkR>hq;Jy0jN1T`(VW5OE5B54)Sd%7}gL8~Mki4&Qw08xItvpNMDhzxRL!|W@NVHH*8NIuOL%0UuYl1edCli3)mZ^)?R4EQUB@gPB#mD$*XP;IdZt}$?DkgS%r>6>UDRD;(yn4FI*7DDrmm;ZBb7?5TFrN4FUM(FLSzZn--s0;1WWUf#;i)+&Qz=`>ARi0mO+!wA;k}|+I7lHe1Pye;MLY3d|eivxq{f_|!INV~hj(-RBP_f2v1G^d=o!peD<zTT-jl$dsK~wnr0qA7x9k*^1!nZ{4imKf3tNw@@KwX+)Ix?vBb}8ca!nf|jH|iDm=MOj%{M0oXSB-!=;N`n}Ovx`#q@ar~T>l*UD9|OV2Z=cFn7RMLMP&39Nu6;KejiqJ&JcvAGRAVaW^{tFth+cIm~@7fG}WwiC=hsDg*j>xi?nR=@78|0qI1rwt8uMMMLMT62aUQsEGmTPQXPB|HJI;hQKz~wzuFoTpMpI<3b3yxR9qbdbD*J8RK3)V6-wg2^*-SM>vHk?cK_5r&Lc4z)JW_aOf)o_rys~8U?jg`It_){PEwG8HBHAZFF0?dZh{2(SR;AITRr!WX*?rM;7lV3!2q~ns&1rRjs%V5jM<gKHVW%SVr=sR)!%l!8%J+KD*=+zIAh7Z;&B~}Mk;t`BG5w3BdB--w<IM1gU+d*Lb*Nls!diyjU;HVau+@lE!eT;)HNqoq8AZs44{k3zz`$fQ}MndX|%4D=nY$UmfA&7EY520|Ht0D^jfy1*+KKQo_p>0K4+gB_vUrFDihL`l_ix0ZiR$I%LpL>7T8b*w@NPK!p0Z`E?Y)`T_7Rh2FB$ELMlO-CJktS1h_#5A=5xeP%=g~27x8S4}b<@jxoNu9{X|5iMVkiZrPC;d2&D3UTd!T_~!SG2YU+k$^XiS)PCFD<xBUI0-SvALyFe}tZXi}xF>a-FPPT@Y_17fQ~}BWtDomfchjz+jwOet0R{|<k)^#2F#6G%=O40<H1Hyq@1RVYkB=AZ=*hik5(coL#l_)>O(A;FP7zP)*vH>>+gFpV(A=rHRk|A}vfe<tY5=q|$&s=J#26!??CvhmP}b#k0WTpjOaGc3A$Zr731ZA=%T|JI00%fT3uMlcx3t_(ior;8)57%vH*c0c*PU1ooPH}=U2DiO?iu%sYfEs-(Z}QpD*A5Bw~V1Ean&LjtLhMo0<3(4MGS}&P&PUNOth`EX<vL0q!`<o_>s-trXDBN9JEH`j6>`Tk>u*JfEJ#nK#huiv-pPcMwW)Wy9Lk|CeAh7{US&*5W;uBR{LLbf5BHj#vFuYuqIapl@~V*(hb0f=^g-VtRLM<abUi_6&fdz<d2{n%=1)pruSAVq;OJVLS`LB_D$l!NM4STOnv_DfI4AE9`nIt0SX6Ehl9#*$p26QD&o^l1-FVt{;-2UhB(*gt&U8|ovX_a$xyK7i?papn(5@eO%rE(OH$k{T0@{pu-dApG=>myjEy@TpBhg&$PLJDnPDvP-BA0W>6CtjuRu`;4aGV!El6kr6HKy})97FRNT7UW$hrk6A63{fS$r{1)zpNYspto4t%WE|(w$jpAjoOVQ+eAW*b+l$m;xABBJzn4X_A@c87RLX@{K0hQYLGjswyCX&Oid@jM)`|-@7=0h7=4<HHq3eRu?s3b4^W^XwD;85h>|ywwv+^h*wypaD`Rsh*e4~JZ@gX3AAw%pZ0{V&*q5S0nMz}m%SRoyC3)xcPP)|zkFfOPnoP`h}oFw`!iLt9Ps<F6y1`tR$2Ji^XC7V0Eym4owpjAA^uAl?PjV9`_j?1thf(5BPErB1#P2MvnU<V&*aEQFfPHJj8^$~Tqsr4@C6J?Syko#OKM9>d;DZCAw9EM4(ozdZ3`hC$u8nkt67eqCG;v4Z3Hc0^U9kq{JKsNu-Q(^*>HsL>W8d7RY<IsMmoG|uY!0bJd+tl=T%sXp|#$kWG8FN$>E&oQnTVIY6;OIb@NL%<diU*=9y-t8P2gO*)VE?K}YfkSvMm~1>q;8k75{eOcw>cB>!wuA3SGvEt>1mgs0#D5o}f;FQ?o7UiWJl4a3hCegGB&pVpWyK?}%(Y#s5G5kIo$`Ef&5Ce6gs$wA^c_p=8j{bLQHMIb3Gf{?<A@=d<za|}<WLM|Pa+&voLV#Dby>C@1c2XD>>z|F5{aGVm3obSy+d$jU8{_`LY=-e-WWv93u5Wu)wk0$J2(?>>9!hwP|fq<PLRhfU#{f4hbn&t1tjsQ>302($0$(Zj;Iwn%|@M3s$0^!(Ok0eb#@o~|AH<rYq$T@zI{22gY|KNla_Gex<AFOfK_`u$A;y+_%-tess+e*CHJRqVWaTnKV$ES-YY>m!tkLJNaa!1Su+&!Xye?Q-ofA*zid1Qbi+_42YZ^AdxR(B>+S*vt}zrY$eJaV?AvN@WvxQB#MV*u3oNaT3I{ZhE2rln~rB_Jw?!t-pPI&x%HH?^w3Vy{N*Hm1-VU_;Z7Dk}Xt9z>uD<^qhI=!QC{gsouSTjfnB=iU{6h0`T<ZD>-QJI5;bA0|Lh8+NM|AyVwbJA@tfRw5xBYuYb<sD|Y7RdUfNM#g%d&r#EZ-}JNUM~~51hoWKM7`y;2Qse7+mlfAROflj(B6OJYkx!Akl(-TvObK4_^kGP}BNMG%AqJ)&ftaTuZh+UqRZHXO1fVRH6tQ4}y@$;+=D&0Ti45Z4r$E2#*iz-kWG-4x<iGME8%$X_i4atPSx@<d6?6!apL${Lpwe6FK^=F^VbKe<eS<epG6Mhx!a+Q2*)ft?W_-)K^hE@`4L-aE6bpSZNAbfpZb~miuVS>B8YA9`U0G8wylchzW2YRroaEy*GWX*K#2AvU%3ZUTgee7MJLR@bXCsn`!HrfNief<?KLrf=4cnWZC6nAkxKI{J^yR2#jXfLkgDOz|vdI&hd>Z(Y7?BWcoVEI{H1^I$eXW+p93QF``r-gDM#?=^u3}?{4m2wp@?c}}S9q_s(ONVQ_J$o>ExH<T4lVf^jk6w{%3ueI>L>2^zZQ@1Gt5_iA^f<nws{dj;keomh1Z%eV=X`Xy%P@3aw0QS!a$4wrhCCm88y|r9N}|amCeJ!l**#YD1s*pPGV9Dk~R#3@?r7rqZ7k6kyw+SjI3Kf%EFT%)hF(B@~8I1O$0h>J}RJLCN+_XubtQL&3$Z0zWx#57XUc!@|3}#L8X8M$q0y(ACV}1IOkX%F=;QA8l<4%X1|3XArL$DG2|fcbP$}~J$OV6!x@^Z?HQB#hH`>XI<SS``y*KoF`gAB?n1DI8Y5<qtW(|r<ObYA(Sxs~)gyL_CvOIGIK31fb-+huu42mZ1gD3+CkFUYZlGj1xcL1C_ocID=>F5YG`%+^WNO$L-y^)BEl_-wpmx0T>_cNo!+hXqw8R}us<)I>jw($CLr4(?Toa6(TOY~OYNj=n%=18`Q#DLmG}@TzcA>D(a;Iw~7!JBUazfG@Q^C#`8k#}r5$#LiUIa%~(1OBM>Sj>_fLzxzJ!AZm$hM%=&EK7?XW8pBp)AGV-mk&^w`R1nLVi26I=9)2o<(@kjB(g{dMjUo0D^njFy=?SHeybjut+ZMbSP1RlXM%X=oXAp;i)gC4TM_k`$b=^`(y7gbp$9}0$z>T7DWA;(f_bv8kZ8BYyj%ECS<v!H<>hzkWjANpBT`s&_-LBYp`a=)a@AqDM&T%;7oOnAb_W(hkZC&0@QqQj?!GCgC28Ks1u)jTQce`4daI={E+3|HFC<d(@TEb<}STR#!r5D5@4Cm^hZ+#hn&yBi5{y|T#~fOKZ+qIZ-}4d=_NN0g_s@)+V>nwjx|YDBl9A%PD9W9K=kbqC6&S3q}zUlOx6}FMHmJs_E7VSYP+J3h(yTG9~kaHyFx{pU68&-UI90JOFj!Z=<XjZOAM>hePD<{L82$-=~}l#p)fR0=*FujV#@irMf*WI1$-gTt1H{U_P=?y)On}e);c(pRJRgp5d^x6{71*Gk?18EsZ@>hzgxm^T%q4w8*6O2EJY!@ZUBPKSYufTg@qs|jdt?ECJKUK*(w>D9mCu&%{11Qgpe>&j-Dv;CXH}2Gpq{Yrd=X#8q!1s%;_X{97fbHs{yPD)P9DzNfN9<>AIoWQ(Y6_n@?a+G5`R05NY`9UtXsHCS;A9ySAvry8cAunfN~~3b`N58G{M3U6IqjFvnOLx7=_PRJOMBk_wwAY%k0)sQ)Ju38dT19K#Gxa}49#$oy?F$EYkJr2+|xL+zY6T3vZ!uv}9`ZI5Ch7c#L`nR%c=!PrlWmyl_9%JcL^pVP`u3@=Gl`3A#xXK7oa;*n8_e(OnsjurE?ekZ9-I8BXtT2Q3(duDrD_*`R89J5jDiN@tWxkt;Nbbk>U-|8par1vH-Rdqg{EgOYC*hzC28~y485tzJ?9G>tukGgv2n<RlUR~;~;t)Xv*j<8`iZ?`i!0L<7qe5C{4<A9Obwe$$+ib`8q+0f`PnD_hqZcBK_1_F`tFmIFP`%wyRfe985r<cBsar|SogB<TcB54C{ph+mtodSh|qvgf&-G%@0(P-`!OZd3*mQN|?05QPE92QmzR&qeMlWzyk`N>!`*xIDECBNEA+9hTKDUd<<bI(FJZY?MW#+)zK_~)r~7H2oqRqaMu`D-EWgEcwh3?{;(;fd3@Y80TbbbqU0)%}`9xz;rQF$>fbTm;CiD)7wc+I}ju*aG1MqQUFX%;<t>z~tO=rOUJaCg>*jL>&um=}X0!DQz>U>4@{F>>8NI@>C~+L^^p)M7FKWAizc=!pNPx_>jpi!!I<Zn^2Uu^V2_nm*trEXHo+T&~vF->dYI0`ru7GPe9mw)ACyz1VFg4oX-(1B6EThi69@F88G5pz-PdR>t!Os%|Y<RjGh`_u`vrv5w*=zq-6~oY7G3V&5D$z8^SNis%D~)(mieYWC;OKgyQE?G%91zCc{LKgFauSQ5!>pil|$IQn3os^7f|kmxGh3X;(>a-2B(2)5F7(h}KbFpYl7L%*7sR$WbF8Kt=JI`q7kDqv9-lNQD{48c}gCl?Vu^{-5_Zj-hMJH!+T>7sfG$e}A2E%yn!xTE<+mzABAXmY>1;3es4_{Tvv@^EC2pzv~x6pFPA1`7`&pU+ZEPgJFDw`$fYFm5`LWBM9Xl1FRj#`3hncy<lF<D2(1QB`%zxsJk&VFc7Mn31W*Tc9$Qva!P<Z-xYpX-YL|Rk4)@>;o)3iiOm-9YF=e6z>Jy@g1xECk;22sGJUGW{O|Xp-Yi5`U~N2{i(Jhs<I4xDpX3Rst7d2>**Nu=+nK|91`((jo0^({YVdB$o(Qu8nOR3yLQi*?kA}Iv0L3QTk!Y2Q+<>-1ozuJhh%E~=C*a?WL<hQ3Rwdd<{=@}s;6$yIEOM<3M4$;RY+9rvWxZgm5)X{$B-39{9+}0QmV1+)y<QbG7I_iNV)w*<1cfSfIJ2$|R{fIEf-(!enH1nS`FB^|j5C=M<R0zP4^G~h8kBQCI4!cX@Yk89d&3Uf5hy&N8KM!Ux}v|;3w|5tSSqFig89}(iSE<MM%G_qSmy_<eW)2iWh0dmxhQs`z)_9Hxn(cennVp7P>KoBws>u@WjfKEDB<{a`J5WBuvBBTO_E<9EYLG&XXX(X_;9^}TX{WdF~ZV^Ht)QCn#QO9*<9i!p7SDcOX3BiGuGdWM4ljfj)v_8d%<Tb8NNviNNoIw#QhdR0(ofx)wgBW2wT(iujxI28`#^N3w*XjLYbGzbNZJ#%otoMiMJ{ii<%0vA$fIF+p%ey$bbz1w3-jbjGg^89ok^QgNftg8DVf-aVo<W0F2xgSO&L^<dLAuLye9!h3KU;##={|zJA0dATpSHCm_<Pf%YUmprOQv(M=-EO$x+HUsnX><tH-O9zX(oRV=S76HKLnQ4XTEi%p~SKkNO3GkLYGAwMSVyPcbS7aEXE+ri5nur4?#6v6-I`)3ipsXWX@it3I$46VTHr4@KLS%I6}KyW36FdBj<gWO;-h&B<&>uFaO)T1vkRbj$Q=HN1u(T<|z65iip)B9&^#9wmR^sWuXWwXAr6sPtqwP&EiJ8H&2mo=Jn)$lrt&E2O>GyIDC4L|%0s5*!5kq%N7T-X~_%b358?Gvr3cS($WeV_*4ih$e)TX~UtAVoWWxP8Qis^V_Dr_NqI03cW^^T}*@=Okll_#?cYcbB~d)X0S%0CSez(GkZ~)rApje!8`j5tLY2_4WuoeABiPB!;S~5Fv>sNGk}S6&g<(h~^|3W;zb}5(YWLkza-keg`15VwFm|%tlP+UU-X34#mW@&!0cpIv7n!E7gDHeP|*BQlxiKpqINHDObx0BCqc&FN<Xb`ab$;c1U$`(^aZ)p1NLPgs9d(2?vbaQPMulb&v=cRV8X!79>NZ*F>cZAn-|z3?Uc>PFw)cHF#R)Xbg8=QEoLzNM3GW41WmG#J=@HFQ66Zjd}q|v0F(?M3bc)_a4=Z8rmci=1c;nD@74~MMaL&OnG_LSn}}U70JU-KC1nn0FEvC)sF?gFWU4wny7&`HA^9`nLM0h+H#|Hsa_G}jf4sc=Jn`+0CN(Qe^x{#t-7c@L5^8AE5OJ$lMV`cOa3`jyD{}*EPY?(Zwdl=%5?Y4@AdMH6Yi1Qj}2e{GBHeOk*LVG;=tjnS4NMo{O^JA29+lVO*(w#4J9!1Nmnd6g#rf^gDCHFy2L={lz%8H7eXqOdt!yqLai<C_L`!lbs6(xj2nM#9u(rFj(4R01_1DDQUt3&Ts<U&3^tzzQL$o<FjnN0Z4+8LpH9~ZqQySUaFLKhWHV}hhJa3aDx31A;rVm;-MWD;7OP})P$&_h1O_1+rF7L`CTeo)ib@q#EVdJ?uTnVX`GE#Pl6B*bN=X9f4MNS&v&hagdeOO6QCpHRqY;C#j7VNHaz-WMh=~fO!ID$4P&@LS>5wQU?~91!n#|&zo9=3~fDa$W+y+8{g=>_qLOMK3i$^dw@3;9Yf7%EWYq!sr{z#$c74iO*hpvy%99<>hr-=-Q)N-o#Oi5}1A$tJx)ee(`q%z>%viCHR7yS$$L->6_w(Y>&J??#vz(Gb6s<5?s-P7r9j|Hbw*;RHUgUP8G8-qERN=4-SN+rpxJe65pQ9dPz)jQ$^Sr!>6wS`yu0tH1<7JQv5nIye%thjAQ07tNLFoh#Gb+I&w4vL=Mu#HihJYYkDYzv`aaPxfTz|)C5&AMo+|MK6?(Q=&Jq9Cbj>40w(Er${<#}X|!w+-p<B_Qq<-|mSln(R}frS&RQHbPb#>v&UMQMy+PZN;4>^f0HqW<_17D&}dW(=LsOsXy(0DW(nnL8|18F%aZKpZ|Wrn(LV|!I29ZXXCFUkWEBo8(RnTj4w#%7P0S$xx6+mkHv4ubRBSW1_q*oMyY(+PqybIQ9RMQlr$o)65SX9<^w)JmtafjZ}}E0>1)28{F{T%ty4HEtRzt;Cu2)=h42%_y*iD)jx=02n!Ljx+SI|mqVDWZMf^dB%6;vKz_kw1^nVW;sP=(DzFS9O({x1)t#yRI_N@%vqQi4@=vI)&<+SWyCxr@m8YKNM2JjYPD@JcL<#KRowGqMSt*OO7*2=|6U{7gmyKBWxXr`FfH3o2VF@T+y%}zaP@mfx9mOczlK*+|Mo~jg;%63;Or#5bzGH&Bymn#zPq|%d$kz^BH?;RB=(Rzf`j{M2HLOpw?M?w+m**8V_wy5-U3(c%>YGrL?gSMHJvp$7B&wu+ZE3=KmPi0+*vtczcakg6sj%#r?mSjjDu!;I|r<Jb6*+vR*n<K4)#b!FTyAWriSm#`yEiT0ZRZyMu6R18}O%iQfz_sh@Y|B+$Nwjq{iMAYQ<RP^y`fUC}pRLt4%d_aD(X5qXq0eT;;Agg3lQ`Qa-C+G+?_a&_IO~0|>SbA*o}=7dYF55jx*Q4UCRj<4hN4+Xk^6L|Svjj)*0Y{?uWs3@8$P31X=nr^oyVDMWxSHDG?9;d{%gusUeziaHtbf8Hm{JaY^^Mbm18VR=0mNhT#195a^>x^WV&0HB(x|@Xtz&Qlk|V-eHQL7z}Z9XQRT<uOjnp;1z0C5%H=6<*A_-Zw45%e$t{pW($*c29N?y4FYt?hfPn@<mjmU=6i-vU%#*?di&dG1l3Ie@J_k@s4p2UUFFAvBB;jqDn0#XQgfroTA=A$2v#NG;l<dX)##>)daUxab+%XX0OqwrG{=vG{gM?vKr9Pnx=;kZRU(Hs=U2tu0bKj?(w$guZ_dIv&pS)tudeIYhToc{oembs+t-y={pr6Y%F_|U?mc<ITYYa(ei=$KBOs=nv2m+aeVyX(ud8+14Cbo0+M0_z%3OIpIh>j?hZp)tzf;yU3M&7g*m5gekp(w4?O40BfUjcBf#ivPvC~d6$e4$j=kU>TSMh@smx8r3}7BkSU73%>y)Cw7aq((6CTV6V6D2Tx_J6LX>Vblg{Nz;OeQrsAn>U6c$Q{f4{Us_{)yPfV|b^nnce%?Ku1Yn5i4L2rF;Ml0X5RR1QhhzZAkx@$X@_Nw&ZhtmNL#4wG84%`;jKA)gZyoYmN6FcNJ5?29xE^VobU4K}m^};BFBq>y4NKx~Tal;pabV}jfQzWMjb2$x71R#6**lP{xZCO(OXrWZJN`Os1`5Momv9hUPu4rQ%=#fpO3dsvxn1qq2y{MWW{i99c0l<Pje~8b*t;sYrur1+aJnk8uDwXUPguOpJJm%Cx$b}e?q^u?hpzW%6JVshwMUy}SjOEMA<h1xBnhtp!V?--#<})r02@zvmfS9lFL@RLjKl%-hHXyr>@G5U>SC5{5xt+;5)-ev+OpkEwM5-<*_GIGAZ?0bgoT0K2QLYOY5R7oBzc&nTI6PS4~rp(*m<_4`7YEi{<~?NI=p*_9qwyA<$qgkg%<k0yO4V;gX!y}g0^q)B_G)x1n>4-8K>TA2wh5~C@Z+=ush}r;M2%)(9hBd?dZ)ScQ0;>8cMAadBbiSW=Q;s!bjwlwNdao)7eHkp}_on$uusLfr}hqcik~7_DX~EB6%>S0hQ?IV311v-ArKao82-E$fQDU=Z1;uDO_gV@3KU`0g|jI%?o{S?11WhQ-7KFo%eX`<8OW|)8YmIyxY^Fm>#cp@yRW{xtbFzGLl@ew7!@V5hAl3Z!is)jF4zat5FPY;gNflv_dsZ9_iKHtn&h+5iPc!C9PhA&R~c%xGupPh2TThk{a`4GWU({Dpv(tOUqRq3{M`&Hp00b8k?8HQdjyo6O}%t?^4F<S1gC!#q`^dok587B}{yS#Cp&28jtCx*#~nE&CA3&wtEE~%wC^xCq*X|&jHcaK`~JQI53ATphRc>SBNY;Hpd9BloiNfVmt|`NHs4@cyZZ!be10A+8U6kL<%{#?xUCKS`K$(dlJ;bQVXLzSUfvl^xf8iiaam|3?8UhE{otLnq000M0wj4Mm{FD1e7xYL*|VKK4n8{w0<HSy+lX>*UAIyKnY`picHB94_&+)c0PRllB5#Y1NV1BBjqEX>elGk*8)n2hEUDDl^eX&47ANrT}D0?(<V*imNmeN0*!@UXj>k+>DaEv(t{?P)M!IA_ik8jcI1&)DQG2_)RvXXOZBW>Qba0JM6~7cWy@oB*rwe?wY`DExpAXIS5ZA8TxPWG;>yyrh$!V@uYuRHX5+P)f_aF8IIWvD+~X!FjGG`TXEsHtHB7dEsL6i3-S&@PEz>=9t{9D8?QbD|>ir@;h`U;pLuF&8ju4B!6v@oC4-!IHenwhxMw#w#CDWbvGZkwRl!|5PVz%c_=5K5&TvSWRd!|VVPNIw>ij<;Q0CkXdHOY_q;;-F|n$<#@GLmLlHHhs@c_fyZuUy<Qfj32=+8fW%R;wgTwOBAP^3yL0X<TrwI=CA_LZhhIic3{1AVv9N&3d1mXEB)zv(vV|EKGn&<I-FqnEqCrAtIKT*YenqyEK#1!2_Y%YAj#0yESe~he0Ww?HrqY9}D}@_93%h@kMxiw09O`qY<3~u2_<>^EbJ=m7Q}V=&c_QSQ>C*gcYl)N$Z;*Za?Bi;=lfoCJoQP?M7l>**tX5JA-TmuA61wFYt9q-V9^O2S;e(hX>lXcA8R$X^2>wEE$T$S(vHRg>@<Oc$0aRAA@XPg|G7zGt{1B+zeQ;XBho>3}`9!P0`K$<f}|Chu~ImG~<CuIffvGGph#7zX>c`kg_j1E*MMm6Kkse?)R9@F=&ssx>7IKQnljk37tYmqmlh=W~VCfXd9sJ7E0k~oYPY~SNDu^sfXPHZ)+thK2GjEQShU_VzN1lvAgwx$>2Rs5{qTuH_i2w1vF22bc!^pfkqeRU=__@HX-^lL&-;h%z&jmgO@!+SeV<`214XsO{w0lL1`F6l>_e~7Z5A}<2>H@NqTYA@(pEL_vK7<%u%srm~<1&neA#xn5_ri+Zw=QKG`*w|MCJV>8E%JMLOfq5v=GJ!oq$wgNOM_8C=m+E-M6ysf?GCDcFuz6qG>XBC!d!LimxpS5Bau^Vl-x>|4u`S*{PSS{}yJ_E(F9pL8jwb>b5&66vpgi%vdQi-danrfmPKGH}zgem=4I`HV1u!-b!ZnWWsd^l9m#UY9NTv~tMLhm*{>eo&JPJF7^t?&T^HOiu?pJro?^z>S5(G)BgSM5%zg#y(Xs_K~WPq8)goN=CfYXU!;6LguV%$I;4!QhoqUDh0)UT`$*|{Oj`eX<y~-V-ejamVWpbUZW<4eb+9J@bq|&IHeOH92LV$Ol=!Ajr%%(zNOk$N7n^{FmfAr=FUx1wYDtQt?Rq+!(fqVzOjIMA8o=Nyv_c(&uD{PORWm~1@spslaIVVC-JS0WSZs^YvF+lsa$%7WALA?a21OVk{lr)e3`k9w3$EoZP46>FPemzXH?&7a;8(n$(@N)9av6Vac`-Q1#>qu+sgR=P0B&(b<mCar2!u#5A<wo7^gA+a%|{qLN^ku(J#Fn|1wA{quq(HI)#e0rQU)#f6IVT#7=`^&tgWWB;7^W2t<04fqV%YmGv91G#bSOYAYARK0jQGPHrgzPp|vV(Bnm>*e{nnA7=l`M8I4JZ7_w^2o1BA=$hk10A?~~iw7&ba4wh~xhbHHG|dPkLc5!V5t|4`>$zGJ#HjzDZ*pDmV6(ri%Hnq);2?oIejjaSiNE?$T}-OUCMaIo1fgG#MkZ-XVMhiAOS2%_kY3rD#4&^2m}@h)F{V40#=`!qU4z<ZU4z0c*Pyz%25rpIB-}SOSy%?OC+ojk-FXAhVqfur#HR8cd(j%8uI~5(T;UY!j%d<wsWg=cLuAmwYIy<bNRtL_z!_>(no@KSBpt|#l43(k7nxw;(j!1cuhAd?%@#Bxf`rU_2$NT5#o4;tOe@jGC0{f?2Y=6>e_-Y`M-ZMAuo$OIhHZO^R&Obi8W+@1dZKnvRYWWJa15_AoxN3ot-lMr&|iM3FgB{@z629$C{7`aJAIkvlSPU$^Tj5L#za$Rq^3fQ8}>L9y<*iPYhoR+itxwe3frgHK&RT;xTW7okgP)!n+CEs8^L&}4-wRjsjAqW36shFu4mbVY?n5MiY{D0`RA~ulNti<Uj8D^xpv!4aje(&XXToTd>Z2XBtKmJ{&#N08Zw7BT5&B7<gyj}SrhgJX;&|rEwb4nCEoj%ZPu~D=%||eI!qzpC??St3gzY(dsxF(jjuLB+T`YORc**}df$fX5eS^L30uBS7@Qd(<R;y%@>fPl2l$M&qX_mN{9vtu@QV#Imtz+4MEz+ozvYdT&wHJ^lR+_6G+;a8jkBvp>NtTk>L@@V=3UF+ZT|!eZ0iAurcBd@kdlPJI&Ag;v8*dBBMsveh_!hlTY@QGz?AZcFr{6?13gbf`+OcNx9W@oZ8}&v7!F{2AyV85zv}v5`2a(5T)e4bomNW?LIL(l%Z1s>5RWr$vJO6gh9S1qfHkS2Vx2?=;vAkAfr?%e9G(OROA=Rd^o;^b;DvIFZnT{<vAEE|w<}V(p6IJJ(47X@OrfL0OY|o7kQ?~m(Nn_#+rmouR4S3~)6#Pcc`$AxkG3{bx&?jIgxVYEi={vG?GD}?sLZFp{DJ!R5U$1{%*L+D%ojNGRR9Xw<VW>m+(4>TaJ$X8WJ9JJG28+E&8-~feATle%h6reW|$Sd3>A=xfqK^w+x#XE^VY^Vs)$tPgLZ8w8?bSJHzXpwasNSXzSYkn6t7jgelR8_1Y%gh9ttz|(53nd3bTP_h+QxG<cc?oLM7BYAtO_!CIXIg9Q$72rWhdZYaA*mn&68N!q1Dmp=&zT##fxuxMw*OFQ7nmpSnWKm82_;$%>jd<Ws~>q7$fRqR2E9uqCOcjmYLJCt0}UM*}j+wwZSnHz3@mX}89@OCSRTke)cRVhyt+Opm=7cFcZSI&uCl+J_m%()C#3Ua{~gM;;HT;!+a}O_NGMl*!JsT1_d1r0ODnuF^jN4})td0ONn+|2#=^%o;~zb@K8N`bttPh+GHCOd;lPvBmfzq`$X~Ildg&^#{(s15XlazYWH8TOlZf*JO%Al?I|1)MfGj{NXqNc_K>9RS7n3-Og95M6^Uw*y=0f4kRM*_v9^?>9*6(2ID^bt~}jV6PBF-VUB%bNe4(Ea$yhQZFD_zoY*MylHXDVwQc0Z=~+8>9Y~L44X}<T_#F@9rFKR$OokqGs~XU3fnyx7jDcpvh$ms$<~eH`>sWgqsX1}#1u1W6^fbr<C>r^fxwXiBN8l{Z0J^4rd}39%MW1sr)8ctXX#&1Urm)l!*XB!ANxnllXs&1yp6|cyzer?Q8GtOP%DkrdFe#o<p>uAYArivCD7;2mIki<B_gq7cNBTh1TtW#Vi`PkvrT9C!l`+Z&OVxk3GR@+u`eF}IrQZq7T-TcRCtj^Y()FOm*GfFB(3gKiRaE5wbf;QV{D$oLF30GGcymc0xK3%WDO;GA*td~a8WBmGM<&Ukd9c1UdwbtbAv=HW+X&qMN83wEXYNDD7uQQZX1l~q5>m}@iwgbELR-+?ChJlcFDaR$d@=X^wo^}Y1>-`ug#N7UD_fH{;f_B{uzuT7)(fP|LdV$fB3xHyd&yAtlC3Y|XIFbk|MFh4;Myc83hFbOmjnRwurvkZyu$Rhg`^@R5?V)SYE1IQs5z{kCB;<;BUyIP{_&IU9RGspDD1G@ck~d>7vg)LN(hR(e}td{ta>UJO5G~;SmGtfn`4W05>=21@3kYsDizWiCR)h+8f;pDL>MSz!CYXG&1IJ#N=T4@RK-Egp?a%G7I(;zkF;kZIO$%z!$C++agsBkULJm8M`?+g|5wwbBj3!_OK4~O7(xFh)5v>+#VAU&2rC{F>Ko2ANSeX0#tMrabsdrn5bN9vf{dIj|4CEaRB$ShdT-q<$yE=A2R5d}j@2enT9UvebhKH^bVgRHzL!wM-<ZI0@q;2`cegBd3t?a;MEQ+)-PA@GuloudTLrR(rnD4g_U|#eZ?FYI@v2l6tT4KrROhM@+hckRrmsY%*?bbYoI$Fa41o!Y&9B!ZwcAv70O)EaUU#^|>qfDx61BTvWm~sO;n=81yWn*%>S9$m8cH^NSAen%|NZ~+je6)ec2;Hj^mR1v4&K?<=~Gf#D6Vt?;ueCtrI_;~cRGrjPU~P^-As8v^I&E9QtPBD>Nh5CQH2}JoO;&P8utpGfGhdZVj`+d_&jB5J(QwOeaV`Ji>#@nmw{KFQCFBa?N>OO+WEP}DOFXj*ejn1CiGw2^*}mcOFgMUt!RU^!`W(}N+fNcjP-5qM^yNUn7SqPNhKp@){((7*>vR)<d!6B5b6V%k1F=3owg7&+aVQi6Zyy5s~B)ac1o2qJ|h+2ITt5Uufv5q5u+i+-{V1~O)B+Jodc$L0{R=oJ>sPJ$>=B*yk?a2txa2ju^gtSWO;u9%!P6pzaEQyd2$jqK(~!yc5o9?2(@g@HR9)Q@mIK4u`jaE@O5vj&pMPZ1{43ApM#v4<kBP;DBM<)+%h#)(nw`_Rj_y={8YZ0Kl3VYq&?P36<5*44slq!X2qRpg~UL$Mg6;CI9wy<l({m6nv=P@z!jkj(5M{<K1ne7>+Cc5Zj@RwyI}zF$l)}wE0n+&l5P#;VhD!9SMaThxuu%W+`O3`2nfkxI;L7}+j)F`-qe`8pbaLCE-TDsa0h5|=Y?-$J)IJy1{)j`j|cu@O02lCmJ75Aw9CjtY2Yo_5H}e`wB;p896vR*w2fk{#HQxSw`O)%>3Z|)f9pG;O-~7z&A7^Z3+fJWsqQe0+#r}nKc`Cnyt>1ls`R0#(%)8hVEt2guaxfU(d$QFkalomK%{{0)#?s?k#?xULsABU+GxGu>Rzeqz!Zzx-*9Zzrvj<|uhw%r-1KiNEb15#%?bxoSQKfLc{41^jnpi|qGV*58(|T;_N}mp7DlnTjEpJ+$yfp)%@Y7lIm{br0K+{t)C!2SGx8-wB4l)CXB0-;@i+^S!o3h_MsGXGg*=o%sk#W144_mOX?R#ew)8=1N{AE~A~nkpi2*}B7?kC=P;J@&%?}>C&t}+<6}u-}`Tc}`uzreZx?w4*q^Jrr+}P<g861J&U-nbe)o<iV9A=bEM)Ro%<}mnT*`T_j{E9fIIR1`WcC*y~3-^*%4E?-OfKmO4Gd`A%P!k4`Mi@kMJDOk5qWM)`WQ)Ah?ze)9Zu<52!39^;oZq9kn93|k?v5dI5{2)D^+(l{dF&N#BNLL1X?)O62RWUHY?0(qkU6gzpF*ZKl#1+zIU8ci3Fr?ZCAB-c7r8N~idc^+De54y3d=+lY6Y^Az)xe{<j1%WH_0?!*Ghh{Xo4)TNg|+M4=U`ik|=P0O=;yQYa!rE!#aBEpJ3`X(pcGt^x~OM7<U3c%F2#47n>(oi^=f{xsAMD@5E8|%w*s*45>Xgxq$rvg2R3U1giu&0wg*TB~>@<&e%)**=LO;-vbDG3li6q%6pC2q`m~hmDp{k-Ih1E$Y|Q=ljL?};nG+^(%W`@!%EKx^{g10(bKC-a{wHYK4_06`YjS*HxRT9nr9RS&TC%l=?A$Q<S}IQkTe5ou4N)Z76fEdyj$hyX()?SizCk=ad}IBIypoB7eWCjgb(hhEB(U1asy4@%DOG?rbDVLW!0IE#s5(A2BCI~dt=tRs7aL_b|~h;`NfWuDpssK)s=A)fz}j(_JQ8T(c=uS%d^gSAq2K_8>Pz<nvH-qqu>Q|;i@^%2EE_~kh6o!nOAnkHbNNGNL3U?RgSlOd!M|`f!gV|#NUKug1q)mMmZLwko?LTTvbQ}hQ0OnbNakQxXG$vrqt6ZTE)9r^1!anHsTX~Wc2YVgi6*Hl>{2ylbI23?UV}L)!rTHIK_ZiKNroRB*gI?j8K9=Eee1<J3S>-jD_Ro6vbfawzz9%#}8AZO-Jx<I)^~?dHLsqIW-6IG#eMojP?-9FQ$=EB<V7{L4|i&IC5OLNvu*CwEVOa?N*e}>6D5c%Sfhia~cz)TO4Z8z55&A)_$Od+|U$lNv7cDmO$2j-+W7u1N7>8OF+irKvd0WtduM_KW+&Y`+-qch4a~5S7mU8KbEHbz^IQo##!1Abg$2s+Gb!9j)UCXD5?_8m?oe6UL8*E46U&2(zqM*`uJ(=D7HmgIZhg3Xq~bjSS|MhKq5PZlY*kTwo|Az=JG$$X5gD8@}H6Vc}=P58%qe|^+9Xs4gKIa*AJ$GWKz)oF5<y-NkBYho73mSgGU{fcj}l|;=$(nT=MtaY3|)if-E!fU@J0FIr!MTrouF5jDI&OO#j=rRbgt_^}1pOJ*5I8B~^<R^a!V*yZmC_tY9EfUkC&-mas`Pl`X1K^s#kRfyS^DDe%@&hlTVc_0Uvi&oIrNL|0G%!mt#aH^<FsGwB7%mkSU4tkjei==^1=3HsZwLg%ZKQdtCU1=!e#Kb-877S4~#1JSH*TKXKoWMEcyN*th&UW<m;w{VrYBi45B<W#N*gYmntQT>-+RXxZj`+#279AgVth}h%~wV~)B3|U>=I_df3wmShTLA)x3tk(JSyC8yISF{Nwa9FRyu)-G)`>>TmGtm{T5u}-b*@s;dA3U5!nuC01<I0EA2}16n7?kEOK1#)8!`K{mly=daG&jUs3{Tj}tk?N~=<;na=R?)l@v#TWk>v2?L8vs5tm5t=Fo^K^@rF`lRS=h+o*l%$OWcuq`S{(ANWDd4|NP4$0Nk~exb|f!fEOfPq?ju~!2%6sZc=DASGLYUnjp1e_X|SLoL#7#j+1E#YkGCz8-|iU;LpvZUd$sq_#*qo@SL}dYQ9l9_3`sF%@GbW=@+$Lij<>ghy_z)D37mH3&d7C6Jkw%ik=yQ!*<UCw4%sbJLC8Vla-lv6w&#K%<fg53reMk)L-2u_0M_h&R?9ZV*6-Xd7?dOg{Ewp$s^3aSe7{fbSDv<8P#zvf>UH-nCTn!AL>yHhP1hcc2%pH=1VHtXW>foWya_?sf7JyoJjng>KmnUQaafDP;;r5rI>YMc<|AtzyH@zj}4usUQE^HrTGbwW5-HtO`=!aGuIM}j@K|E+m}+2x?@d{xY)KTyVr<99jT6tC7spkfJ_G8H?HRcQDJGrbS=NWF3J<NQ)meX*iJ6AL+Fy+-kI{r$4|kQ+9bfgfxfXa(hVSy1%N6i>T^nKV5M8r$#NImnn{2TpXVk&IIF;MB-KnN4wC96wSQHx=eqgr)b|6I2V17;yA~zeDZdI&!0>VG+Lmyj3%K)Z^SY47eJSY?q@;{TzRX@B=M<BSebDPl1uCrBNn_bigUv(;X(jawe!kH@nonCyGjtV&*E=^$a_KScBMjh^ZnyH%9d>^5J!wXXfG95-%u@U6Blh<{;zl>=@4b$ga?e2UHN=#PaJ+lO6cyRaZe9A?u`T4Oq+BEupwfa-(Jl(C%k6ExR~^~uE4OLPZKzwL+Fy6RS`ohpGC=?_DH_WG0S1EZP^~at63Z>C{FOatz=JFZK~jkz`Givu3WzhF3SzW>>VviA1sAPnD37h+JoDjOBT@mbv0a<42VMb%z_%Tntqp7vKdAhkxH$!F(GNXxzp14x1W8goQlUPN>Z+lIqeq>b>g)VW4yW3JTFEEYf_9dtzr0r=_=A#-LpX89Y7b<l)D&_2XI|Mb^_*??cq>n|Dh@|W_Gj}9`*YUMnk(vOT{>BmLe{L4RY?pLI&vm;G8_pxsaYZ%)PM%36F8H1%<F)@+fyn&g{E^|4_(VzK=gI)T=Y(Ea>NWyN;){@&RLO$XnFocsFx?Beja||+a09+VuYsZKKpY%LMyi1upFC^0lgTTK+`afhm~PhqXAMMyWGHg)?aeNui#!IcPvB;kJzL(7=RdkIAB7nu)b4T<&VE}le`;&F&eM@l1hvTCiWA75ntJ;fyXZ8CQwW(4x>?Mus7b$lZ#@!@O9}61lntRbJeOT36CvmV=meC2(e5Q%<S`QM3PT_YlG%LxI(<y#b{eDBxKSPH(U9*>#2Z(HEb33!L>E+p7pk0{_sufCrbzT3u1m^-Ta!Uy^o^&pkTF~QMBRV!9kjbSm|&;g{?|&3$6-fkUI2BRL>(@G>n{oGyp~`^OZI2>ATrb?Ko5qBvMs_sBDpf1>u;_=ZNmOVwTLfwQ?WbYLkxi#kSD34?lAMlC|TPJ{;Zf_5ICs2_owQA)3|2tmoqs6=<A)Y)B?vd70wS6diCkTL@GZ=6;|*qEUumib$Bi^M~_dMJN`ct^-71c7zmIb!Uw%kFZzC8LkQsHsI(L<RM{)pe*}!-XDwXTCt048Awqi8r>?66&i$Y6>$|QPH`JIn}pU4KCfk61>&e@Vsq8Zn;2R#;ov#5KzONztR#Ptp2OYW_o{?NZqy$mLC~EkOLg{nr&2$7>1UeI^bQU6hC80!6Rrk;+DD*~Pa=PvaTdsZocY&b1<nn%D(}|3`ud1zR6%C{MA4EbX977trX2?nkLk=c?gqv;-YijKE`X#(pVBZS!8UtOY+8>np1A2$Z@3mwl0bgFm_#CSwLWO1V2ciy&OM&89HpDeN@Je<nI!1F5$mGq%prhpC8N)Y2|OG^GKn!jxf=IdUqLs*;5PJXk&P1(DH_sO>6#){ABdtXzcu^EFUq%)Rn5rz#TUoJ8d#RXs7M&uj|MxMG7L<9NQn=-C2zlFT7kiegnk%UDG9euz*#C~c3pP-B5GK)4JCH2h@UhYPzHxmR;4>ywC#z~CCqa<z9M_%IC2n;h^goX>i@aZ|3jEt694@Gq@j8MexZGsc`>7mohO#`c=lgYnS1pV+B3%cA)m_04}j^!?T(~eR^-pxlbpd=e{ykmc2X3~<0-E=r?c&~hBN-Y0p2`q`51e`M;vB@j{*C+$@{*uv71kiUX%jq<2;ELbk+te4v(OSOKdmKB|kig+~^-!(dhrV_nAbwCNCz@ycDhon%h!ayk^IR%!M&?hoqD{0zPOu1QT=!&rhYgaicu)4z$^6LS+hMm<b0}noU^(R6%awUUgW7d_X0Zwt2bELF5K>(MDzTJ*F&8rL|Ou4?c%qhy2~+Y%!-)Sq=dpqE`WjyvK!eZ%j^5U=DBfe@rb3OAJ&h-@c|@cV6WdB&s|AmgOrYt?jQ`dhZ2I1Ys}XD|uab3#SUEh4U*&5BLpo8{w_jKeQ_!AXs@D2t}?n^;?qTV%z$bsg!=h->r<ZIg}n&6P??U9h=sRGxSXPw?!;>6oDU@e9m`o9dVc53RF&0Si6m5fo)7FO5=<l-f%1bRw$2}cNirO`JHO+Vms5JtPKk%`XQiAB8TN$eT?nA<rl>ae(NXsGcB||mzqF#?urf4vWXsKy9)bjB`R!+dh5$d%!}&XtWV)xd>0>M?z(ARk_k7bHajc3Se=jB(^^%M2cG4TLsh)Y$12^k(7c+#>)ei41d^JFEMW8VT>7`(r_Vk@hr-U0P4|9%Rtcl$yKRjJ$o;eDs@tLgUfXlSRkzK(th>{5eaV`=)NRw9ZX54)TZY<GpXK@M&SM1Ro;%=L+GIK5*LT>!4*QVcx1#Q2y;b!#!j?hTz38pXEmnwfy&%)<s=U&YxqAzMUaWhA#w0D{?xj9U+3B&{=4EbQ*{t0#5BM7Ja}A-UMbDLJb1FTz%{})k6?xL5mt^K^J8%AbW^ZNJc-yPL-08oyqb{denAH@vS@dFtYxq2?;~O&U(xMlm)s}s^a6%d;oPw$G-|f+B-+SxS!@W*@F&8t!yqJ!WrPglPTfeSLS5?2R^?_@;h%-sc>weu{_3PExuRUsbZCgYr%WP3oyZ-qOzBP4G?nSVl1T1RBxNvK;Ga70&b#~&GSzk=mG)KP;wjW{@-FPNV(16BF{npARc#1oje`>H;+%qh>(b-F#ir)>rpUu>{4Y%(~N<kl31+Czd#By+Ky;7uZKU&uMSLb`a`g|if(MlR18PTm_$Em`^b*olRS@s&Ul0p6(Pcyv}79HcUHC_<gyf<zVoP>r7QCR9hgKdbwNJcO7#$BV56iFJXybk(W11lc>98k8{{W22BhXs<kCC<(`a65gG*;|Yc*TeM$;VKnZv8?l~Q2TDcgu}TZVF?gYZ0M7cm?lZBBik3TbweqN3Xoso_nF`ncMWIN0?gECK8-piAl$fcN(@x&O1WkDI*x+~hXW{oCH%v$#o9ved5N_h_p)`W8<(bSl<I9{7f3*7XHp0z#LL;iOP442P8OO3<j}v3z$=|e$R-oQMY66H%AO$bQ5f2DGE&Kn1qJi*EA#~yi~@n;Al>l%$kv>yN}M~T6VGb_bwO~JiRS4{_}v~C?5XW34fE>7V=aZ_0;eiPtf|x+#;4+V7)vw|O+TL79O^nd=2VytH<aQ1C|n<SZn2n}lyCW|xa`X**-07(pBr>PJB`K9slYwGYx4UhKCil<8qJjFeG#@AVYq%KGGCHTDHa)jotQP%c#U>NldsH(g3t{b7yVi586h`LkX%2B^G|w(D$s{GT5^UtmO9N$3MN&2`(2(ulqH55ywvWO0{+3z5XtVs`yiCmhRhVkB!`5eMqh(D@MCr|ajDgRfeiKqQSIZ?pLBl_wcY9`ZumkRNgq!b)(6ePYvg|86Sn(LMW`0l^T-51a+0{*rjkdc1_@FH55A`o&uJi&z!}@9<*bBNA9o|{BbD0@R7CTT|DsPRhVZrx=R{Jd<eqjYb8m}P7?O*J@P^;&I7DiS(dDJ~Yi5{p>>@~RNG9B4*7W(^o$H-Jzk>Of;PXhjRrv4|>*>|b3um63H%=BmRwv7U<=<jP6PYsoVs46#*vr;zN1-Ca1~H98<Zyo4k7kx{-X)x@U3E~TJKx3M2`bHsbP{X28&?wB66d=kOt0exX|}1KN0j+v?Yl*k@36t22bJDNNU+=+af_?V(9*U{oVyu*vhG8dgSBiBUKeJ*u<JKNoM0R{?zjg=ny=VO(QgoRI!Ni|yW5vAb5%Y$#+cgRTcoBoD57iQFn;TeAu$g*Ma4_AsB_$6wS?!68Q{B7=OQg2+iVVkErGn;d9Enwz5of$kmRI>2)e(tdxFojYd<0oa`>+rXNXMRuvDDS^x)$4&rjd)>F4(Rwx51(;m<AnxrIMJea+L)O>yIC_%Khydwjiqmv`%L<+Q))(~lHIeD0_pv2E)Q_gnSnwtdI1r)QtO(|7-NZriYU8vHkU8a~j|`qfWEVGNB==Vzs-<GcPHo-Q8yS3M@`%Du~9T+96zZ@zo~Z@B%}@~m<6;U)o9ulI74EKkP=mHoO<2<5?*@j>tl7M1F@bV4ji+NiuV^ZWwYnN*`U8O)NemNp}dq=N5*ZwJe|S3y`bIonAqjIIHuGZhQ{IR>+|!@tq(n~*;HXKoCB{;kVbf@xOkpUQz3A9(%<^QXluTnXpPFV0^v5B22{ETc1iE0%ASD^k*E<O$wBI2&y`2W!USC)x-h=*Q;u(`TkHPOsd$98_xWHEcOmd*%6i5uQJ1{g71?E>Cj#%Ho`thcX(bnmR0+&ezk4jV<qAyyNo^T%L9;bq(a_OwQ9A{zCtBz$APssiCSPj}JsZ9F6w$c=0#zUFzzLPx;pjL+l{4cc<6W^|$P=sgK=x_qlIr++DpTvyT*KT+yp*!N*p&-<ldB+&!xo-+hnMo<0z6ejqGfS)S@MSMlOo;{*K*v&YGJrsFFV$)ER`SlT(+$3VuPeb==AX9qMJM?Su6@Mq5U_I)IN!dtt&-{rsSTjOb5ob7m$Q(FbIJGi|3(n;>U==|dG*kTJW?{HZPysQr{(&zv8>xHXvM$IiOfSCp1yd=hDb0j`VSqD|KE4%GUWlWMzO^S-;!j8r|ew<?MAfcOTvv|8#QMoPi7wi0@d`6pvIIHNlY`z0HwY8Hm=)sI>P2M(-(-t{r`%7I#30nIZg1|zCG=6ygxJ<yNAvArlF2Y$<=bk<sFTR_WEwFgYK0i(0x)9nHu-FqMPL@Vi`UozF1)e^~8pu*UOqRhWIFk&*9>YxEdRASxx_2@`FmZ?^J)$DM+|6uOn>DyRugFxUpiP*a)p&-&6!3mU)Agd3aI&LW8Q&A7NJ4b;54@IK@-qzbv=pCN=strn+MT={AzD&T9#Q1Rg9BM6!x?UX`34>zjAn__F~68!+~{LIG!JNr$9yFZax4?08g<qB1S*a`A0Al%XGiQF>4GID^qDkn5WxIeb$ITMzWzhHxb))1ed*#>A_G1j24&k5WF|XwzBoM623&S=atzs(Vt)`~KGu&?oiy4E>i%bxE*s+KhNE3N6voTd*OIzDsKkzMZ9oo>^-+#c_)4QvEl+8uuaCbDMuQ(D2Lq%J5LLL@Ti+JrtNKwqJ5qb)H~8Rp<w7`TS!?0L2mT7WE|2zSFva=V6!&)#shrCEX4s`Pbg4dYuB(!4vrftP+oYBN2H-2#QE|N<a7X*(cL|p5X&~A^AOBEj{`9#MQPjYYjv!ORNC5K1>auC8?phoqzu0p!1l*~$O{6?=Yg6+iR5{rc-Bt!_Ll@K+sjny8!d7g;PTp})r3y*TNxJ8RzUCee!#B6}CWDe%_A6>YqOwjIgsnG!rYM3&Dol;m8wVdhP250h`bDr&^<a>CThPlc;g9C7JpANtKVId2Od~*w`twZp^n}_`|9%5w&GREQF-<24IN9C$0?82GM(QL{Ve88x<v--tSu)P+OuGYzN635tV1v&SK;3{c2TTI)TN;KiRAAo?8V`MevO=Z=FK#sU!W@<j#?~=ky^yL6wz%7tVq0B0G!hRcP$l=_JZcCpjkJdc>e1X7fhw)n{?q~2x1n4?P4W9L-?-t?{}9}E%^QAHtL<KmF*yN+JQn}+UA&LCkJ>}S7pc8OD(B8Ohm$0KbrWc|3m^&mJ?-i5ph#-pcN2u<00@acTti5V$94;BPYfBD_k%IaM)1fL-kwuR?Wq_fygk(wA!Y&2*5ElEy%KwGV35H1gmY$vnf{f~WIN{?gIS6z`J7i|0d6k<BlPG{%A%bBBRIp540yl5BI_q8iUDF~^=im{5pm7UacCi$I|vDa)$Eok7TgHuFc46l_w;~nC#dnaivfB2Ywq8f#j$59lW>xZ*W}C}fXP}J!c_K}!m?my&a-qSCsnjJj?q$aAaBk4Cu$jUDjRrki2rtwDod1A*!7fxX~-`I3@nCIFvVd8gaaX#fce&%N27M$Bus`itZst@;z+=af$nagLpDY%lv>L`)}1GJAwh+cSq*TL{1!aANZH=#fuJI0s7Lw?w9OS3wZt4H)X|V2NHn6tW4WFbp0?=NNt_$4$&}10LN83?RNkb3^4EW;tV}YeJ$hIMI`xj;d(6DFz(D6UIG-C_OE!S4JxJK-XD>WOck~pki>Ih20!dFd^b|c6Ptm4$idMx_^y}ciKl2nF-qBOEYFyfZ-T@~%?|+WAqG@R>`rC2)qS7ex6#YT*6ir1~Xmk_(iiQzChlv>PQh?I`Kt7@Yc8d8h8!VU9C^KO%^AYuvk0?XR(L}WJy0p<pG?|Ym1=(AsGNad-EAEz$C?^_B8R%~LiqI>u*37I#g`B?OBbpb@%?%$>Qi`2fiKfEyt!GxEsaT0_#jvECXrd!_vJHSps@Mb8L3-fa<4H!LFpr5*#0C^l(_n_8HKn|oklxZ!d3)t18lQI)O%k)mYAh?!rgmT6uo6Z4>|g07>MiiO@D!~sJw*{D?7lmOqOAoLZy1hz_@JVY_-+LiP-9%spRVJIC5bO7uDDO)TZR_5`A#py6%<`(rh0fjsA!qfwupkcuXp0{UB?nEQc!_JguYj?`Nk;7*iA94syXr$aRc2c0F})RL3)*w9K^_Oswb%Fl66Xvc`XO&ortHc5l<=jWW>|v9`RICq=26*<uL{rQLM(E0Y-8D`bbdI<`=P-%!B`D7?FR$2Ken55KnpSiHSW68<@P)#g30Vc|8U_X^&f%H^=Qj#y@Swa_E=GP+npN3cyMaEl;fbyfhvR-ksO_%>WvEo`nbIk@_d=9W-sidYs#%g6=-H#oyDf`>^UTnF7O&h>RU=V=&@v=XcPjl#?<JPH{x^!Bs`$lDzY2!@A}!Ki|BS*E&uq`_Mu94BdHv%s|*^hnsI6MXp<?O{;JJdH3)7p{4f0ldBc5>_{K7aE$Xv-r#(Z9-b1w(g$Xk@(Fz5p8)BHQUt?S-}|^CW0AA0d$4RGB98h9kKM1)IsA|0WB~U&Wy<8@<9|TEue76qR0R<QbgWvL!r1%py{;I0vO7XFxx;d+i_QVeo+8NTlMK+I^8vB0JaRz(%Afdw42$zmu4GRu9!N>c=FcCzdBcmQz=P)-`gIO4icmc!&nL(Ly}<yEYvgQ<j;ngxR}8YGe)vkBwE~uRWUJ=>+8LkV*4D2~(T8x0M!*QJrqvkaZlKga!;qJF*58DZ%8442;jXh;I$h4v#p?`ii5NC>wsrG*x&Tv8<BZosv0>s|i@Wj~qChLV4UkbGd%^YPk|l6(W_0C8q5wo4FtEFuJ3bi>k$M_mPXcgMsZbX?-j|b~F;43~>`evKcb`-WIS<G8P#u^DEZlTGAFyyMV|ls7Xy}%_nyb+e8LdzV3jF0f8aCat0ZZlk{)K?0eK}z9yWF*ry`rf6jiE5=4PYISSZE5jq7~#PUS!T-bB7FZvZWg-5Ylqut40Hd!VX#12gcd;<v4(Pbv4t=;9K;^<v2hLVyXZ$J`AIks(sgSV9`ovn{iyxr6f2rF&C=fEwjX{PdOA~`ZwIKQ*7wR*k;xe^j5<7DPK2p;(2lDp}W&*H*r?_!#_Q8x_8Me)Li<SB7*sj<j(ts`yIJX)hDv$<XuIUzlxeCfmhm?d(OZJQX5#vYd=sbx<E$C{xPN#3jj1g8kFMC(ai&YMR%B!OMZHgTwKfY-a3B_;Y!PW6V~X4h@qlAPH>5imVX*+*vjL9cz)VRJ@Nx>xxfOuVfdSW{a{d=NCsq$*wm*S1U3BKQhuvTb|>#?^Eq%=h+lumuOD%-viJ_a`fln-`R^CEB<7A-COZBCB<5BKe=jBG4&=d)x=4-h*NdF$bLvRQf8`JrId9pu(&E7~rL~NuycM;CqLNMBh5B5cNAh*=x=B6<)rC=j&NJI78RfuKCk????KHgGu+R?nT;@7y{`LsuT5`7gJVlZ&*)SSDK{>fdEHRecX($e66O6;tZ57?^Pk<GhXO-VUR&3*&9VxM~@L^r53MIC(Yb^yU;vH5eIEf~OalFsysg&13-#UejnJ)4E$WO3Bz6+b`JTL9s5UsPy<{(f}8P>-s>;}J=gAF%u`4x&B`eC$r5*>9HzEYFtV1{vi9##2=e!4tm;?4wSP&XsFHONCu-#X#*->2E~P#CyvDmwmop=p^vwhSI$C-rs5^UV8#kqeIAzqhT2)o|HyaM(X=bszDM-<0^j{FB@Cs^tL4t@nuDFTsbZLcY-avetgZ6?oJL2m~P1ERo2gw(Ub6r+JX%?{=+|4)0KpLxOq92D3ZLI^4t#v|)?pbiq<@AL<4{<c3c>(+1<?ysT~TD>*Vhp)P|qs957XP;~f9widkb2zl6h*=RuPYiRRld^5O#>r(#Umqk2r4eBX7tGB-r`G8s41Gibt`$Re1b-g~yd0#!SS*?fnM>fK@<D1s^^@1_1scCmz?ip0!y&vVYCB$K7=2n!00K2C96N<jRP=xdC@|?=TeU|X;<cz$F$K;GfIj@WPi_TJ2Ccse}Ow-_fd9e0UaLJ~`q7a6SfPUqzvNRmD@0On#iZEDYW<dqUYi+R0xaSjlNe%zB`=yvR5mK?g4Z<y$ZNAJ;wHR|k*6I9o9wipp4EgmZ1|Pxb?&v8G)&Yezc(S+zv5T+?ib7B&hftygLkHPR9yzo6JdtA9LZ$WraLy#R9YUA~3MQO*@PV;Z5@@30Zy_O!BPXPTQE17pY)-63%7D?~oa;ybwUb&&3}=OFjBHr(!3XlcGvmC6SpT^kc2u>me?-H>3W}$=XlO)ZrWi_Dtb$@d>XEO)$tppODon+<JC~=p8cuBn7a|}7G5)6LYjiz@Svd6pp#b?BzyTUrkYiJhiGzV6En@}`XROLPS)WXmG*u=ef_)FWJ~Nf6uK8DZrPeqSU83qro9b2)M}hE>0>8osyjDMR&<fu81}%B+`IL5;#v@@G)dijlvbp+-AX@M(qQ?R+)1X+R#3)u&Pa%-bU}Dp8R>>R*DuMqvvL!>6_b#C^b=&wKUx1k2`t-Ye4#V;9DMvcd9hM<ty`4NNgu$v0NG%MD<&ifN(mGBo|0<d`wQ{*FwSt>E47{IFkqS~`@Ji$Q$;H3Y5~{ADOeL2FEWddY4x1>kwb&|ZjTHW+7Dr7Hp4^W&)i}nm0qy8aie)ycBk;Qf^VKy^5>ngfcLTf00o5v#bQ`_y&GiO~hUjbgayE$f^G2E*AkQee%0Cfv1AfV33p{x$9fTPnZ;$1DcF5PV!fZw@Gv@p_!<$xOO^q`Q?#P8EJk3r?s2wwV%>f9TdJ_?ej3Ar5W+4d5d)Lmfsu>;+@&m%KAD&8i=Z{M}cK8vKr+G%F?n;zoY?OYM9=Q0u^mv9yKICI_T>O=*HWVzc{F@;t&zM_xID}dt@f`pKzNp{ktNtFAr?{t@^nqi!v5ce@nxEJ<f!KXId-4HpPF$Z5NpAPv(C8tx^r8EHDmFP73HikG@$<-!O0q^+xW|<`YEnIp!u^$8MGU8o>T8=SMyD9h8_LQtAuy0IP;>8-Pau!<f%A^?wSqi0to&`Z{zw6={8`-m^>2|_N`ch<T+z1>OZgH@Rj-bvlEqSnCVV&16-oiAyh}Sc)c4<VMW|^r{9ZxT7*SndXr9$vm9`&2Ww((uKrWbA)jR7~;<Cd&O39D0<1>(&5?U#R@+qUM_YxugKm$c<><1ewz3;1+3c(+0lt6ONx5}#~rAnSH1m7DRmm|aa6d$~^6!CW4ZlqUlG>Q&!=N8JY{vyrF?Z%j9_3mAF9Pc1S+$^MAjsLjs@ar1_PwRiu{UzUji5^t#U7z>ePq+x=B5Uc2$0(PBr%0oC!$+&c0SIUb-M3sXaOfwbeEJ+2pQ%3un+`<gk3`09TJ(!N5Nc+IPI*3jP)<&PY--MVexyI5OY0#dCYEcLkD>S_9`fU!`I(i1FJjN0gg%MGnYDwne6M1TO5-UGk3L$i7GY6%^7TU^#0nR<$xGoWiUJn?z&qq#9+1k2BvA&a!!dY5ZiI=m(=zLlFLs^B11Er%j(U044So%8nz=eVIyodDw@SIlwIc7E;b5oa<3MTQv}Y_R*2@s;6>sMTHCDC+YQb<q%I!B$EOIagX@pAxChdHXzR$}dHnCm4yGOTTZdrZ=w1vX7zhc8zJLGJKU-$sc!*KU@3(=|=wkR#~qG%_W@FFs7o2y2mZKk64dV}FQoS9;W7ZLMPCo@<8>bXKo<Oa-dsxjaTTS1||3Dy{>TJ^4OfJ(;ADeWP?AAF#8z9(9+-<b~--u<EbxAMH-3QgH@+n8Tv)uSbN{SYwwp8_`CL(A%NN@$4a*aUQpp@mhx%Q9BLo`HrG^-d*q?hsZaN3?99yawzrLjgT?roJb0&A<uv{0cz_sb*edMKekmI(g#A(7|9k1bM$Hek2PSh29tiR71zBsG6QzT^<=#GLsT`Dq*#jM~$KNy@G05b_Hr?RM9fQhLjP6l8&TSr>*4NsU#?gQ3*Y*F@6j=I+bk_^A~H%2v?@AO)FhsP|<)%B!Ea)x~(Oi6i<iW^J+g8*FDKh1<Nb80cWgwTkQd#z;syyG8A(k+mQHzMf<?$zd}{#Aotw76Kl-SclGFGTFzLUrYR5diwvS^5Xpsu<L?6n2w5J(a{mYi(Lu$cQ|RdW6CXv3i)w6~z?rm%d`BNGouSYYX_VjmMmEhgJhyJ!H1~`|Zu*B`do;&q&BOEhzq)b`Z-`tlk{YRHa%Yx#c*k@-GuPaenl+bPlSc3YG<+A<%(+Lh3`Ps_P7X@!zLk)-wboK*kg7=cQ##-}lhMv|Mi==*FvTJaXl}lokY@>Ta<4D;rw|~Hv9O<`yeUVw@M2(30A}*65z00^((p1+v!8qMxy1X*YzeMPu2+FT96cF7p$qe$dM6j=NQ0KVK6YzDsXO|gz)=@Z5oSFYE(F7$y}v)ne3?uq0!^5$$XnQe0wFV(-8ww9V&q11WYAZ59~1q!c5nlah>%iv+~Q*cWU<3j&)@3h*N6MicCc)YwFWJ5*+};QuN{Z5q2oL7ANduAIpgUi%cK$p+_`RxryD9*)&ozqqAwa#tp<OI5lN7q*C<{5sPHGYd+G4fsqdoU|2;R-US4#5m3;IWj31;?N<}pY<J4gV#~d6e3;_PF(8|!a1=frs+>1O;fo&3f1BIiBIhO^W22wO?f7}Plp(3|$_HzMVJCbWHp39U9s90tbkI}1?!1+OQW?l(89d>YP7zTCGn9m#okHR=hoPjh5PAr^ZkbuI|FY>&=c|tn5GBiTk7{ey)S_AMUgfTfX!qY|^1Nf%JHflkGzaPhGP?0xZ*29C;fg<GC$t&z>u#Q!5=T)4A2N@0C@B_LWWQc&OUW<;I&-`C}J%=*~P#`$ctg#Ppg3D0|igp#d7Yp{9rgEzf0t+MN#@x4UsFO}dj$KD8UlCMIbTmjDOG$T_qt0Ld+ZiJ?nRxRh>l!2HRFqq1pE1iJcYQ$2U6B+_qQDS1<uy>{9sJ6J<CK|d!Q2?j4j78TA8knjgY$$U|3;Q0j{-3ONs7$)FTFzpd-$>d9*GhJ8~8{Q&fo-ngh$f>>0mQ5d>k2=1fS)ecHq7$&oInv)(50+J11vTF1${Vd*qJDFU;3L)@}a!%8a^J9hQ-So9cXZv{}WzNDF4(YHg_lYz&n>*5}+Qe`@@|(F_{%IiDm8y+L4^7{Ya0C{$VAM;ajKpG$^CIa<JhFaE+i#99RY#wVBOxPd{7^7ER`^HF8>m{01-iMpA`6i#iY4DczYl9$L$`{Yrf*XPlhRl$0Y2{b06{H+~PJS`(P7ziBDU8*YV$f}W+6mY$qQNjjbVRg#%z(F10Em5Cc{;lpL5=r#p#O0~x5xokQd-yfXV0lK(tA+pd_nCuF1cRI`G4Dxe!N4Tnrov3+%;%i5FUeC#GFEiRWE*hu7E6hLD<~wys72976+?;XL?dDL-4HSpB?2I-pA&z*l_CSzoSL)m3OE=1e%I1;olti)i3hF;uCmAxGH1dmLQIb+8v&;>6X`uJe8oI7jjg#u;JY>5C#7b@U5gV{s>>5$q1Y!?Z?p<ZUI8gGY(48@|J|Che$=jkHo@)$%jD>{N~@4`nygsW+H~ua?f+1ai=2J)0Z)Oh-)m%X&T2-f{r}Z(6lmx1u(=ax?|k%Efwm{!BmnZ!`DLulc*H6_inS98AGKm_Wa$X&;S`>V8R<43PvADXWoh$ObLnj9;RlK{BT<XBg(!3uZl^Ka*3$%E;z|zgDh%d9n@Yq@HH9i@QAfDIXpE9!9%y=B;%-%~a`4{CKMNHMMorBWcONyOG3cf}ipg8lZMo+ZKZvH1;0B#@O&3&AvAJi9p@iG{e1I?p;zjnV>g-Kt;r3=0Zm(|SqKV)8<l**zInBdL*L-QYnkSJ7DhGyNgT)huDoz9<2Mgz~$WgC3<3xAbCR7Zt8aNpnw41!jIqj{7L7+9JWxRPz)K%Ue(+IW2G%Mqp#K~x^VCEpR7YQsF;yp34Yncd=twSL4ytq6BBbO^d;s6uqxk#$c0GLWJH_P1oo5ELUy?tH?GsJ52;K)bIJE%OH^t3F{d@3=Nbu{$>Pb`35d_ZW&1TWPGq_5Ay8K(MRFXHEW8Ycvj54?63NU5UZi}U-2!GERv4S%%Zfa~G+3#=H5MR}`f{1AGXmInNSU@{e^6VnlGlmja>D@^{iq~uD#O%;2#k6On2B5lCNxe~hhl~<!gIDetuo)=ZYLMGr}5*XmXZ*dD0k_x}EJ=$ieCT-~;&4dT69R_v9i+RnD{UO3v$JE_S0IWSmt_B1F>O~gJh3*`V5?AKIxs3NmA(NxjX`-SW`Aa{Uuk{Ae2TiS=c3c9dN^~M`-mqiOo11*_kff`DntwQmu8n*JcAIB=+CT7KIfW;@ii(?3MWjcatv0T){txGb?09xvoP>o6WMV<fMo0c>q{V7!A2s4MYo9QaMKgDpNwCa!7{FaJd-*o1;2hRFr6p-f9!%p*8cxg$q8X|pBNz!m&+*n5ZOHp&DQ&RWm#6NS%p(R1i6YfQ>jo%xPz*)r$kxcM%#tLDZeWkk-^Ny|<69_6d*zGs#p=ZJg>1}<j`W{EAWJi|-hmp2X@OW@Vonq1lx#1G%%>te5Vs@!%-L%g;&ESRqK9%c=gDzd$q%@J+;H0zQ?UiwP~eAyjm0m@8d9T?iyA`emTA85*FI{PK&ErP&npt>7hwW(iHk6yj&g5Dm_SEH3lkW^nP++Bh2KGnLt}UzCR9NlBf5R_NTI%t6ojZSVv)Y3#N0AcNObvtgjQ5OftpK*E@f0x6~)~~xw(866}fKF9I~eLT*z?*X68DUFhLZvs7S#uEp>F4i8&5&um?G+<2*O#Kx@e_>}SkP$l@7u69OkM`i1&W9W40&^R?n;lpFQtbrx-6>d-zYIcR^FQl3ZZO5{Ui>1!Ei3m8rTJ_(vpCBgh`RMkv;Y*-|&^D-SaZMIM>s^~ZiV{a}+C_zdHfOmD^VLMUBx%1QUxfkc=g@LAzv!j*iBj2$Vi<_Rm9!A$JR2pI%iwcysSGl29oNEwCGY;aGsg-tFDt=aR=IaIO5NYi}%3WM3f?IfDfz2P4udcNKRDxh|VQX!!p)OgFl`lfu-Yl6?a77s`n))E+Eo&3&z_jRFgW`qKu%RvIEc<bPb@B~m1~6@C%VUC_B|j7Q1cG=XQ7V>mOjEAd!Et6R0(Zck@DeIl4B$}oGNIZyUEu5|%x$bUF}isAM;5TJku#eldVta!Fkh@=x5sqO%hS<lHJqN)Du43G3bP`=v!q>d%1=jb98-Kepmo1y)bRAkP%^)GL^pXzu{*gT#odnkm;8Yg*GEjXZ4s&5<+=Op_8yR~N2~%VZ^wqGc-}e26oSpAyhshu8;M^X67gP+HsoQb;!h2vx$|g9@BAn4mrXz%dwbQe<PBC0#lYBElC75vOd^~ZPBvO9s8$Il$mGj)2a(w%pi16#u)Gn*1=H#|?rq~JJ%pz<(Hbq+4ggy&3{Zn>#v%=~_>y#qGBCrvDK4kQcX~})NQb$c3Cu0<CnAdXoamEGqD+X9I1O$V_(L3rxqtU`l?<*WfeAmo!yztQMdR(A-zVMk{m8h^KX<=haEeCP7z2vajeb$@XPrW!M8{4c)MBOVp`%cbGmA(!mH9&HCh4M^<gah|#ek?`*-e;cOY(t~Yai}XvR-3A=XrkEmwBUPhb+wnLQiyICM?~Qc`Vv=M+kCpL2H%~hnIHLIP;s<qltscyRu;bl(_e+W^R+kD>8(Ix8cl$kiR>ypSG-)__FCN8-&UHFwR6tXH&8C2kbA!h_nlhRgsShGaJTmDQhZg%|OF8i|3n#`e~4cP&Ha9mh%gOX<)mW;~lkwah>9|qUyM)wRYweKX7=4AFB1ktbv0G#LiqX?ciZ_>>agT^RVNX%d;(|U*rk*@dBvd_ihE5v$NTDAgE5FlV{=#R5EyU!aa6M>7Q*TMKy!WV^G#;UrR0pO`Ex1tXOdLC#Si1%|n?rsY;?P&}|j@s;GxNI8&vRF8m<}uPp5Js9y+sHDEGkVd7Dlbo>ND>CWY?XT5jP8yOa7^GEV_wj!hyp=2!DAFL_VHJ0ZC7ipmMJ>p2Dbe;?buN+i;z&@p|IBkJ5>sl19@K*pUXdJTA-&x@w3Gt*fH#RT$WRo-tQ*koNSQxVpcEoj1kd!(qAS;K1TwtiSPGXd4AeoRh2C+f)EmH8MVG`6QWx74GXMyl>NmXrK-7tP_unI=hpq%AITJDu87FpA}5wA3O5xu#Saw{W9y_jd%|KVe77Mm#0Oqt|oIb|Q2{hC2Iv{|eXVB5s5oN`P4PBlYuBu9N!r~yUl{aoghAq0mK6z1PJhj3t4Nx_YL&-s243UAz8g-Ks>wprv9QF$elC1a26AX=7+$x17;c%n%d830Uc)gq_-z*T0EP;QV=-WgAug1P{K#HgwPdH7UU&hsWWg?pC_uu<elKp$~&eFL+xx-clOK!9xAC>l}30@oigl=z>&QP&$d3|^n75N;@fk<gJ#!|uS<#y<-knwK+X=ppNRq=PN`ozO!#4+4lvziSu$4$W*m&IzC#B<73m##^eI#VkotY8lK{XdnYXB#T&dI+2^0v{kyiVt(9Tz=-mILl(F*NHNOqU1H8jg$%ftxIHGI5j{i|L*a(nf*V3C6q!r0LI(4%KwA66GI0~6M`svf=EslIIvh?cf_dwJhFY+0IFtg%$6H`Ah4|m|@@_8>S((rA00Dy46BY89n8U{FJgQV+t5<8E2eE>9I)*nK^Itw;H0D>{9Neguv*RoE7G?Rs4>J{?cWn9QV`KNUg%DK@KrTKxz;_u*kT*v#1d*pavZteg<5y+(o+rLTc`=WFzjHcIEb=Gx=P!52ediaqo4ZEz${o#9G)moeW=B7)8S`UkA%9ud3g;qF*sEwEWmyB|ZLUzD*bHkX46&qTl38ZBxdHeT>+;}ZR!4r*BtUZDDS-o)K#AK-s>coz4Q%5S>YuzB{n}rZk{Gv3YnqrRCkD9XF0_qf>$cu31~4!}In`iME<&zomh5KC-a5?_N)t<|9sz%dPeErmx|A>%8RIYo|27h|1NLK<CTIx==4qmLb^r6c5Zp}reeS+4`lzL+BJ&|u3<z=Uk%>Y?Ed+cT?dyYCvM|w;zgESPCMwCI`QMq_eDo4o9XCybL?ugg+bJa#ORlWgzmG!wqu{)0>6gF3^z$uy<H)<3XLZ=Hl^Mj_K2THGw27GSt;n`4wmAmZw5^$s8y_G3{m&-HpG}TG8^nHo`niQaxA5l{{_Jr4+2Q!J!|~r)Ps3+><B!y^pS_JgdmDepyp2as;#j|ny|KUbVk!@+Z^z!)U-}vA-SP4KyEk2p7xW-gz1_MgLsPIS)B$3;mAD>ikh4-+TXqC88YNd4MF?vp;6npG(JYF)ZON2KCDrU^yUC%}$cE9+ZFF5#P_cLZ85TA776{UN-NA+T@Rd37-9uei;m*v7Wdb>VMsF>C<<`kZLpjY(H7z}W!_2W*1!E-nTQ@WJT^Rjdcoi=$Ef`0nx-|5?Fe<jk?bYR9c`7f=iBV`u&)X7ToT{I?)6~LCPvUUHqxv}$YmB(qj^@gI8qDTMzsR3+X>=y0dXTcE7rvIySQOhU#V0k+EK%p4#Pi4Z9d^SrzP!&{_TG4_e%72g+;{o)%MaXiCVt+V_E~G;_qo9Ek|*&UL*g61I6KwFZSt>vx4q%!J9dUkbK=D-VPUB|^V9WlaS(rXkZU*M37YZj`QP*;W`*W`+=UlylHTQucRJG2yjda`f(TuDJo_ux=j$e#XWR=a<JyFH{L51Fq7e26UJEn1Cwq7-#BpkYK(M4K3Wq%uSK6BV_0Fdb`F~XLrB<AzK?1h&CgR2RU~+{hx4Jm&Q7N^zAXr2}!rIgbf!fdqg4_An@581>@yl!!YTxeNp5a5oMK7FjR$$z0ecQT2U1R{)s9rwyZrGs8R;F!2JMwXU-&7$yL(ngsd@BQ$l!jCcR2(TJKAoS6LJ=^U6s|nGucaWGfUm4sBswHlAH&yB0g3U^5jBs;n*?+;;5$_~khI^54V@ndQ|Eczo`#gixM#=+MmP=vDLQhZ)9@5`q!Vm*D8ls=jA-Cm7kjwagq8#r0O5A9C=&vvI=ekYo~39Fahha)&KyyH7ILOrUw@xfyOXPX-#)NVYX5SRfn?)V!EbU$k<(73Y-Nlqvh-KRu&E&oP34NpR1OTQMPdad3rM_fOkM-PA>r&Pix_&e<xu!K?U{v7HdswNL8=?E=RM&7FcsagGR}Z4(klQ+q?%HzZKxW!L!?sK9R^^=Ds>$NHqq}Xzu%M71K4sGC6`K$iml)hStXo+Pq&3WlSCL|?+oB~2l$I|V61sG6^BhwoJKbMl@yHkwL){b3TSg;ME-5ukipkK#R#;e_D>5S6F?Kxsa$CwuW;$UHH`uYX;FzMwiMbSn5KHN^`sS{1K=$Bs(_(DjdefC$kZ~XVW5J)8<QlhD2CNOncsF2ftCWa0FJGq@Ca2APiW1v&^nwaGQuaCoR3XKv4c&+`<5u03P2u|yxSISmS{v!X~RUp1UlfMRGCM9zPAI#b8@q_u2>=F#@;wlt@B(Xw&1Er#^wQ$VE2l@qmFF89)Z6=U1?oglK|92sulPKO05xQl~i(A%Mg&vCvn5VUwKc>jP4fRW$>}O1k=V5WKA)(O=V!0ZqCTL23c=Oh^1(SVD+F3rUJ5Vtq|N2kXE6TE$%j@_~`srv4L7*I03l6mfst-_by@A)&&TyrrB|zIP1){pex#Yt)DY*^4){>K|7(a84iNm#oHT4IJN*<miTD=gvgelU?gK*ABg04=UL-nCXcs@uhql(E)aC%FIq3#`|!P+@T!8XYF+?qqpiuprRKwg<J%CvN%;N@Nmcpw7!(bxompRW^kp&(RU~L$@{TRpPXomED%z7%n#i99PP3J(Dz|Czt=w5Ek*Vp|o%=%UAjFoo;4_9jy|2C7^q9iB7491(mx#`<4nl%ZR+z|>O0XE-lRSy^uoH8KKlZ^IY|Wjc#Ji-gQZHKWEAkPQ=c%iU_Tw^`V%!jJ7F|;T-qm)p_8<rgG9<A-I=bXK?pc9}3%%RqeGgseIHgnSujm!!549($P=d@!)ffaZ^k9SDrY4SjuZ&w;yJi*kbqS)zR!m;2Ybs5+qOh-WIr(R5;t0{AxdH#^r)*SVO6ys3w$_$m#Pd~<o`{3|-tf3z(XE4_GtHbOSOJlS`~x{Sz*{Rea}87{^_6912B1^hKt-_jQ%l1@wPHmAP&&#E_khQv`yRss7ZaL&scB={gl#aN)I@ZSwP?PdfA~W-XS&yx)M=QvWxCan&`A}dkFRtw<|qq(Z?SLT*#V6jW*8&nT+n!7n+J82@HI}fr`0Uu46L#TlZ<FQE$$mG=eGRkS;NM7r4HJF8@CM#rO<wn?e|E9l$z4_Y{W&6L;(BC-?=6%fM%?n))z@%%Hi48v{+jytppBs_CmZ;!Fz1usaog5W@CfB4RAe7V3?6wo4>JgZOgbQK-eR44c@HKB%Cafep_L(j1d+)n55%!jPK$58TM#Pw*4RcG_4q)ohI3ww#KyVj@0<O=#e0kQ?@H_H<PznlNQP#oLdv-_7F<}eUYigyqE149kFHmH7gVD-Ln0HwV&(vXtooZ?U-k6HXB_yziG1-g8?{ve&c5AO0(4yte(BFB?fxg5ov#Dq;>X1ZrcZWF_1Y@Sy-2MAQrxL)b&81AHeYJ(5NR$?*Pm`<n@L#V&(dZSoMw626F2{Nw3>l^jFhxw<8fYM+@kY;FDW--24vrPr%<a(O~1+-*nub(-;h<o-UovW(8>5^M_(7MQZ|V9nRP*!X@zR@;2s&PqaRDaeK00HBV(nC}jB6*#tQAC-duH<b!+x>8pIS)uV2bHud>Xq_6Uah8-PAxM}!#5Nu#yDQV*R99I;bf(F)!-Z%tyo``|ehA@xmFQ{%a@M+!%G(|Ts{Nu09<K$D_Gd|uSQxo9=03rgsZMWEPbXo&9v|HpRBcIgnZ06(n>4r3f0rFV>%^n-gCo!!bNCGokIx;8EaK268BBXi`MHK3ZIbN>$+=K_Q{eWRTNvJD9ye-Po?!k#>LmvVphuR*1+E(fvk0#Z<qX63Q*KMeID05+7@B#TPU;#*+sZb5%wil*RxXYukqKk*u=)4T`v<JiVl*fT>!{jsXx{hJWlJ3$;?x>B@!|_Yz!A^`9`SMN70}TDj98R%Kq8>+}`Xf?dRM0ZZNzoL8HfHRU8o|IzSIkN>OV`T9w`if7o~i!EQ3i=_fn+?)IJ4-)kDw7E$uw%1N`$Rq8bPpQW+9L}F?ocB@`?Ilgd*lly%Zs#QD{xk{~4Pk%a^t8)0-vvf9$nG^as@b(+2s>37v9&D}?q)QVJstVxFhPPG0Hy&>O}()_%$TFaJRBYwhZ5CdGHh@WjV`ZmmbvmY`!7C7wgo<^#9edDQ(B6@}kO2ImMRJG^xUJ*IwyP7?GmPV9+XNAeo^1OXpLV^H0R>0f_U1METG(T*Pkg#%1kItk}gu$!&mBm$T`oCRCg!~hF{<f@u3iIhidm_yCy#?Sx)qm8nK`D5TAB1O>@{sB%Pu?tpM{BtY{M>!t0rb=eTk)Gqy{FSBw-KL_PTWd};(BRo5SdmFpvtniqI^fWX$*+Ve#fG-W4QJ~HG7MN!^J&O^smW&;Xla-~3|?QvCz+&aTO1Ha&J$f;KPw!t;R$pJUqQyD<trfX@HjM(sq3JV&%d&x|4{?y?)aEH&2PR|o@15j@A<ex!rcUEsHdjFN1iPqLPc^#{;i5VCKfgdGqs`w72!!vhRVU^h8Y^0Od>c}P}PBWJ*1byjAP)r`LYT;d_Fk^$pB<z2vn8$n;_UxSXuhwa15<2i!>cGIkg`ii1TU(q+p{2CQJ=b1Pmsml0a>ey7JJ=QV~@OJ)sb}12r{$@nXRILW-4%*u)}7n8*f<COn&pMJCE(wNW^PXP{B1j2`)adW*t_VoES-qwIzFyGg&541ExmgpEXfkXS$p$yCyK;pJl@t9VP#Me`gQ2_aHED+jbXzH!lm{>}w;lLd5Cqa_Z)ehvrU{wZ6ubCdq~IyE}xMQ5w@y}YRMcsuARPmytC(n=qzO*Ck+ARmf5x_qnhBBrD$nIx9F@=6rI3oFvGO9BFwEU+N^8Kh}ZGRRo3^0n3j6QL1F00qi}YAYzWl$ExljX9hQ*>JF;z`8FrxQCtZ8&vOh`YnkPV71CYD!0M;D2F^BQ~T9oMaNo;1<;r^C_J2hV&5Ql3G0%-{+ZJ9nbPtZtp54w=NA6l!k=6CGo|JIpN7wTmd|{a&wQ58e3s9Amd|{a-(q~0=I=~C%Wh<{NT=AyEJ<V*+MvnyQLbXFL0jRzp%h`HleeXNDhkpYrNz%!7+%Icl`$PmC_PTRj5$?gB#GGP=RB8A0O=dFlu#S-B-GOfkZAG3?@pgAaQb(9#ds6Ob8&N~#`LX5$PqW^#f%rVU~mXAzGT4|!uKYpV`Piy_{kRrhYu&C&jgxo`|^5$$t}1i<I_NQnd?iC(CP)p#G0a<tsgzk#!DDUD{0<nPDZrjCF|DP*HbwqdSo!S>yl~1-zUhFOY=+KO%alD(`ROPZ9%2!=GSYV^v|$q+UaPQR2pyGnTbu~muwo|tQnie%{euGJjjw(bDL8WW^{&|w3-<WWF*DRI3VxOukrUOHt+MriLG#ho$)gN;@O{jh9>h(zB?miU2~4)7x5g+<|dQq<qx#C8*0v!30F)IUq~g+j})75%^$h(-EjGeze&9bFI~~|<f-@i;_bG&#ld;+6B{qzg;~2*S7e;2RavN5p4j-YFgu^}U?JsOw5+^Y00x;EU9)n2<Acj|TCwjLPlub<PuHFf5apcNI`jp!F!OZS613YUXA=EawhjYq9VV?r!i!9f8AOm`wpzEvW;GHxK7%W43z)wlWD-^?Y|&J33k+3&r<tG&<?kh2A^DC`)T3GO#Cik3=tE&Tzy+R0RQU^u*1dsbl(@qpc?i(=ldV%&%gb<q7jN>roolMFRb{<3Yr}TUqHd)B-hck_Ogv<BbD_&xNwEG(mo?vTFdimd)*3);bIF_QvL@-WCR%67S2y1@Py3E^*X7IZb8?L|F&Pd@f;AK=%%l)jYN&AOFcUZWe>xdW(f}GR8Rc$EA@G?S4)RCk7wW9wQ$$n&Te{IGSYg!9?n%o$Gmq;CNUdy3!Qx+3$?q_u5A;SKz-&J65#24J_lBIdx3<j#K83Y*0J>$4SuE#V^>4lpo1`K|V+UAO%{bpoSbG%0sn;7*kJAYh9aX<b6_MwClnq?IK`ot2YmWaaOcsCY3zaGDp<Q~4waZ;~m!C4m3xnLb)Fnd`0gXT~39JJSTfrrgWzu4WRq<P3udCvoiYWxSE^r(?VLIT<g5c|cAzZ!Uq+I>~?7ds4ZEcz!^qs~x4s*=Inrp7L*MF!gQ(awEU0vNag|;I9m3S{+2zt}dLG476jz%LAmC)T0FKlBv>7)xIg2xL*3|<N9g`f!{p%pL0h#jL*!JxN-AoxAc^M2zn4{NWz|NZY>W$nK<tLB<(%rVFK#&>wX_k9jDo*^6&o#LQ?ovyB17_UmozhTu>xDIf?<sVn+1I+>N_i*YnpKSQ`-MLPClc1T4%>Do2|NrvJ-L1jQu{zD$B;=$pODby#SgI<^&Rrswl2kT~M`J^}p^&k*J~EG#6n?xmnYR^t78cmEbJ^vpx!g+Bo|?;e;2Pe<wMfh$HxNaq7z1YbHxpc5lY$N(*1_SM{<qPOGXvJr?MEL+SXD}r-+kuYXO8SQ7e?s2x^IW{w|5XS9oe`e0JMI??b4>qjx7|by9O|@ZJCWzgy|ngi~t*@oB#BL++eTNG*pIA*ShZD^F|&!NsCB%1fw^%jlaXY&bEtnM;OE3)iNUUt3W1^F*#yraA1e<MKpiuRQFY1z_t@;AVLlO&V!-c$gYBcmyBUEY(IP^nvOns=%+(l21*o>PnIg9ENsf;)%hV{uzta{iHaYQ#Cwb(M5yJCTG$c_wp0GrwE!{WvyE&3&Gd1HSv4r)Z;7$yRYifrzDcA{;-WSPa6&Sjtj<a_(Eup|T#6zu!7~$`Ovtvtn-G-uAYu}%W_L|_V=psP4Ds?<L+TncZWu%QVhH<WvoJm6ajVz}webfGAnI7epS~k|g~q9m<tF_AUyrU8NUZaG`V^iGkI~CGuY6^>o$m(t4RRPcU7LJv?lH>%^m3|+8PW7YPXi--gaeD$0Kj@g-<KuhmN3$CgI{oL(Y;|BWc;qLVyOM)w_B92GbA|S$wwz&WqFpd*eG!G@oL~Et|u{ZOS)%ZaAZVJ%?i~lrJER^WC75}T;@8O({Tei8r?I+h4os8=MRq*nTLck#-}<CpWy;toQPqPJIhuK45Gxq7m%(_^i4D~lg6g<SVpmE;9JZ1fdZBWLjQu<UXcOI?fC%N`_juEx=9y+4i*Z^E;yZ*$(bed=g^GI&JQtt|C!RQx*N_HRIEn-I?{mk7{UKe4LJ|@R9E0~hR!vBNnYZ+UXI5RqbQT*Z63#(FyLOnV;n*|`J6_q7McNFc{o||Dao-t*FnDrXgIf+(R#uoD+Cy4gQZynJHO?MpL$v&5yV#d!Y<>p$<<!jN+uf=meOy_2{%ON5q>G_Wi9tSL&JXO?K(@$4Y~=a->}IB{e&i_lj)*Zq*&h@4o28rVwTy^$GRCYnWnZxWpv_@8Cz>+sfp2A60tqfWh1h=c;%gd@zHg#jwC7i55Adw%ae=!g?-C|0LtXeY7{}a9Z^_0G2zx+K)K5}aHIgBID(NYJ?)+!Kac^R+G_psDEn6Y`Xq0dBRF_Fn@8}hvc3*3@8J_h&zPs^`1ZLb7Zz<Id;`#6y>V)cvVg97Zx@emEY|`vc&)?E%nTyg#V~;-hWx%<4}jFzSpE7NV?sNZ?{09Wsv%jvFrLaYGV}}<TAE~ng>vRRAjB|(DUJ}617Mm%8t~Y<@Yg{Trub8nhCpM4bxfF&GO2)2d$9fFMh5!@QmEiwmIxq@vJ<gV2q(jns7pZxO)wG(vpp1Mr*ddd@A<*`F+7Ai2X-rbC?eNG<@-e%2HYd$KbEikKU`^)uYyyvdN?k>giw>@CHE3e%}qkh{^f+4urw#X;M8CTj1)lS)G)|+hE~J0#$-0v$OJ1~A=mV8My`o+uXzj$ix0Mm5p7r(Qh7+ubXstu^XG=76h<p|)O1U(jY=rs^ow!RVC(!M-@5!GAc)}q1)E38bou$0!<O$<H(Sjkb2KI%LxX*Rw-n~gz2sEFG+LcUCRao6CU`m6rr0So>~xc>VTTE&iwk%;sjSGqbcjnjifm0JOfYwSjj@o_VE<zBq8|cXk?CZ}q}IUqH{)_1F<VUi+meOs5s8-1GeuUW#=T7<rQ<v-<`HPaAaFOsxN4wa9bre|r7{haX(j#sm#>Xd?g9&n1d_6{HCrt#Tp{mkfz_N{StgFgDuKa#Q^tHOt9W^^t@)jW!vU|9?0BNh8FFv*L@N_SS?9`H6rv>~zpd%%(dpMG{Th&^qMB96lcgF~OGXdkNIl^Fuj_qV3~3ErCaGSb64!7p`*Gx7PnH(rY?<;eyC0VAx^EQwJz1?V9_dY^rrI*vy@xeWS%9BTj;6+bL)W@|LQLHp$x^1;P<w)7Hge-nSk${QJdQZ#p+ks$&p;65B<!i&XI(h;lS?|Ct+68v<;-QrwPU~@*b5snP(by^7zyy=Y|&l1gs&L5i0!x=<V<UU%fK8V6nIW<_X;cCE<xyu3pQTt9I_Sk^u_)>ZCxiZq(HqL$uj+`8squ?*3$IG$+i+noL5LdO=6}kzb;!2`Jzg+URp`5%Oif7Ew3)76hLy#CRoUqXgck+#IaWm%&287i~$x<v!k`-d!nz4Op9$!XU1gACvXu9thD%PRp~wVOJ2@mu$c4E3kxz)0TaunY7fekc}?1%9n)qqLBouM{3!(&5V;>|-J5H)0el7npi}vxJ4ZzW91yDwnWwvzD*C0%`#=4bDem%Z-!NLAr}<xb$Q_X_5??iPBz^7WhqYn!)tdb>+^-Ud#+W0^6pLrrLS$%~!b`)pf&PDisT7tT;FH+NZq)cxt)n*<o-^8p+Zpav$lW(QPx(S5soe;MAfD+iFn}<hI^?~#<$Btn<cIf`36<R(=7U4nM2<AA;9c+&bF4wm-1OU632P;%azFr8n(v`Q>8Yc9S)>K4wuNRG$?SKFu+K<+iI(Kjz$()zLuhAt?=nUI`8oCd_49F<-$))}%5`tf3zVCDvpN~~R+Jp%HNTaz)zWDGq9U0V7W3<zw(;h?Wj<P^vXe@X#wBg(1&+i<vM?WuZtH}yQEsuD5Kobb4d|`Op_Oxg3L9zKVXIEJqO9f97=m+<Mxr0QlZiQz&h8wf^?LAT7GIW~p}ky~G31ny-XoJ?Zl=?yLk;gw&dG*AG}xzQ1k!%JWon^BQph@#up;f0vpsQPzNfCjE8G2JCBBzz7ZOYz7DZ-}gy)7$E$_I*6cp&_X<H?pe@6qdcyGruCF?f~esQ*j6klmIK(LQ{Dj{nEv>BB}z;dzWT-Vv3km{oSIo7cb7l1@nVy272L8<z4mD>weg`g`Zj`1pG1ZV|<bcyw+p(FvV`IOovJjv0+5oc5FDB03!{}SzZP2CSE6DwrG#C~7RsK6}+t}y&DaCEs%%HOBJ-@Qk}M5GE#<1g@M8`FV`7iI0iNI-I3ndYwQ8RpO3zN|b4EZgPWCvF~*85x;gYs<DC1LjCwj!b8Gh^a^ig?c*&UNr_ul9&{F*h#$tNqm1qg^`sN4l~FwGB`lhq-+@Yy`wnB2kNo$NPN6JkQSKCJyjXglNCITC^>?5iObkx(>1nORq&_seirGI+Cj8RMPE;LK->AYW6B1aOjrmQ-k`*5K*WFFBrUaKWHc~(_m-2oRv4ciHFr@&F>{U|p`gfFf5V()6_-U4M<R*|kzj8Uh}MZw6dmCq-iIp7ooeC%&b<glJJy^_kehpQO_^>wT4t0J`5j|J5UwH10R}#m8&5n27aG7i&sLMfVj^bo1H~9IGH_p%E+lXhA1bRz1>rIr(MYKOs*>df2E7)xDf2-)H_u6t-<ve4;!<}iU6+T<nT@iE@&t6^6eD6V1we)fH~{)%Cfbcl!uuiVU_R$0L?npp0UEGTT`z3}tc(pq->nSxAovxPl#@f=UMK9!Y+`qms<U-^KH9hzYGh7vugy0}8ouQwvA3l5?jm%=CUM~WkQQ6Tqrn&yZ4GCc`cZpNS^L!-eRNHWId`JGlZh<tRNrRcF}jSkrEVCx0+jJNAbBNhrjPbmx{i|;%6}}YHX-;bz<6g9Z%YBjL4a3b4dt9Z2{7_9;E)^To$M23Ok-b#77w;$RRJo$fpMiFOprndW>dS257S@$aly-A2XGB9v)BP#E3`k0nn_F4j6#!3;EYf+trpd&(%&U&rkzkTR$1rzc?&qB;<}m4*ZR6582Z&VovBPGGf|`gZVg|`JTE_4njsKmpzvk1Li>G{e1-Jp=FO_?A2!pJ{>LxXA3LVPKdiZNSHt7CF*mNLj|uXjEGUImSBX$g3Q>KH8<%F%bVv5uI2pl!Tu3RTXTcuvvOgZE0E&I7Wj@>JN~A~x1J)zqOwueggb06jIY#UwFgUPWnK`ww^v!Gj#;1k9@xA#QhaWAA<A2LK=H7>Iyk34Ts56!jV0#5U3MFx}K=N{Prq0NM%8oT@&kEaWatr{9GzZVz0CzuH<0#S+8^J&3E@^PIBn1&~?z(!+Q9TqWG|rXicNF@QXrh-o3$?-+TqG|0%4C|^c9b`9Yxp{%I8rSw_Sj%6k)klc-p_z52nm-2ZUZU<HNeLEC8}2?ZOekXnlqU;a}2aXZ#k2o>QSd)3IZKc+AgioGF_8V=?^CWxTt$eJLn`h)p}XPaQ~OjGKS3Q`*>o;Fj~5>d`I(C(}muvHI#BJYj3m1DUmn4Gszxk@t3D@Pk2jteUfA{lXn5SzC9-Y2()8}V{&5`KJBQY%4j7kV_;e{25GrRQ@G7Yu<Qm1Aj}l_c=%RT4w8;c*>02*J_hdfv6b*G-^qjvrbPXFjMb=wdinIga8v7IW`2X)h0>DF>`kJjP&)3el~N3ov<)VhILOu8)QWJ-D7<HyPC`qX${ZmCDh>x?mbg?krr(alrBvKgG=Co}cm2j2*Ez?s?%mM7+1;#j4$mpzSbf6koaKi1XQj?XopaW{nUTBL|F>uL2}>!Sl{)*gQYW_kR_Zk1PNMuxzpiucs3D)0rA~IMNebs!!Ml&B&9TUdedJl4v#~lSCt;R4F)cs1qu@b*!_vq<|1yovi+ZzWNE7JXoG;YAStPE~yhLNK9*i4QhYF=ly$r`G=Uo1Ou~uto>ZGwmu}&hmoW!B9Vw1K4NzxJ7My=S4>YT4NOsVU2)o~k-aARKC)8mpnKfuAgO@<wTI8km^%m6gpq4eBba=XqdKh|n5WJK0pkGuUc*!F<=;+UvB54)5V!YDE|`IICMA%W{sstm?pegc|f0VH9uN4OsWb1lP*9J8|=7xT;!Xw$Gqajhb>*&r=9h)UNzJOc@`a1)obiZwT?48PxS^LJ;Z%b$BbJ-*)c+|0LDKLLQI&dQsp|K$ocJKyyrn>7$<HcGrOCp(3k$lFAf0aLVQzKT7Aj28E^fHcNR0%<V0AoWIc8H)yinFM@La}cN*Z6%5{sN%O3dqw~wob5#sVJ~I@Ub|T0khV?Pn8blISFNnuBqGRJ*dfnH{prX=I{IT8KoRM=?P`e<Re}R}p=enQ{Fi6oSsZO!q&A!?=n8^QsvT7LStM7t13IR3I&?Qhlfay_oMO0#_tV|p6CUSXty5<jZ4-d;h3nJ|$w@$l)ry*}Q_aOXRdMFt?|rvkr_y?z(jZHZH^DfsS)~5y_aea!r1Y7tepu@2_sqjf&U{$N!LQ`ZrI^R2C6X*`DwKw13|h08G(>Kyqi|>W<v?|F+zFwJ0UGDA=Y#5K9YQ5&&a@@;CL*at=oy;c+zd7Yr<D|TCwc84aXa}K>?V!#>LGG2xla>=_y^yU*m-=hWcM)Zb@$iwx=U1yy-1i5OK9W72JQ*jEv=gg@oiXwZ1K&#>?XGoJ|`T$ob{Cq5JNLqqsru}oZ;cbT-M!GTPpjCa7Q-PB+VWF$d7&F1uNL1b`ycoNQ=P8$Rq9CkjeOCIGgm&j{@|U2<cTE%Cb}y_y;y*>6H(Utj8TJ0<-31zq~`gL~}|(zW;Ee{?ejk8v9ebE{1;(R}rO=rWt^Ns2aEf+a^;{p0&7GdR6LeF@~*%d^bjQN{;s@Z=0nEfLm$gj#V?NoziQA$z+5S=3x>x8xrw1Huk%tL|&oo$&nt)JDt-Kv>NruDu0|`Uq8QYHNQGMYE7~6a*D0<YrB|VyV}xdpKrRq@{TRB7~yAs5yEC}!4$ql-z7igO8e(?rMsvAfs~0Fvog`0SS{BSg8dg#4_1G{&bWGGb>@u)j&f+s7)wcq0Bj1%F$WsF8B=0gx5cV!Gi}jv|K#&*jD-!C@mui)uwD=vbZ6V&>WZaQ70YJftRjP$Xz7OqP&}%F6ptlm2NljHicSf^^-5?B&Wv)fS7HFF?b2|bnqTDQ{Rd6W|CalqZ@yPMP6yh9uR1lUN&}#G?2}m#?f_IIhLL~*PXv>$pAJ){%fwevXc_d=gW^aOuo7jCaz}GRbYYfAt&Rt_dSJ9SL>z_%V@p%QCRw3}vd-Ed?1<+I0ADZ(#WbCaVR8ir=abPP<Z1XQB_$<g^mUkM6FqV8snbYaL^OfsuZ!rqLnbTdM20M|Dn2UFC5<LXU31J4$Vqn@c<po=-E=u}1W5#Pbx$Vxv`KYGd5HQt81(E+xtkGopkjh+@5S?F#aaQ$gMXnuc{xv?GKh<OXT<c3<U*TJc4PJrv&<%rJ&mKqA@&R7ZqHmPcJh>}QC&MPB$Q%M4OI#coK}F)jjc0<aQ)*R?|?ZK`;VS!3{2?B&d?C%jht^(#Uiw=J%`ka%;ciM8l}?{8mT(PdKrA2%7YjPg5(NQxzGvus0mhyzB-L_Ub53BFD0SS_$u8UE&Ck&tQ0l<%ScjH7j7{cU2UZ*VsT(~ae@u1kr&^K`9DiDyh>6rYv^V@4A$etT0vtD9B@{t*D<s6HW|P!)I<-t;PozoonMnwsQ2jW_geeNDYx{sK^o>!8L^+SW9)vX*JXX#S?Z$n6Z6_l;mmq>miG_}Z<hT~a?W5Cj*Lb_VfqPjZOJbtuxw`^2ie63>uIz$<i85AUVPlM!^9{4JN-+~!13PD3s4<^(M-3dp2x~Uyv92(vrh@bg0JCXkKwoq7nQN>Sj(8V>>OK7lzCI#$(W2ws%k00Ad<-4;DZ^sycNG(fn!r^-d%_W$|Ivzx?`11?mHxOgv)!V*gby-`GC>L;<O>W_pv(8=0}LG`|2MAH-POTkS93S6D`wl5u_>FHKgmWzhnLT{q@|+=JmOi72PSZ_A%+-U#kIF9HHDwxX7)fYq^#7b`3yJ=6Vg_pi14G{m0w^!?QW{e_EzgIs=}pvno?cg^>s_=zIvoDaT(s4-;sV5P73zLy$P($1z!cxx}`#QIcD(vRi=8l}{XahO9*|!6QQ{AwsP>F7Nq~zt+$o*;UK9ArQ$`XBadPqJs?IW>TR!>^%dGKnxh>hn?&g7)L1L4lv73n?P&gkmZvBmLzpON^6gpF*C!8^1sIeA1SFJ@kDT+E(4|#<sBNs_&TdQlU0idgy~sDD){C;(jb)DI6+u7ESkd({1!x4<y<>?egf8;25bwt?(wfbIt8(3xPRu2i%^V%p|W+D#g>N1`CzCcAvrnc&V-%hy2VK7UQ!LqXT(2Njx-)r4QqIYBRnOQ$j&ztjb}pw<Kd|B@V|W!M9YRq&MPLVZ-{8&`+=GN3ph)E1<TUC5X<7?3eE!cOAg?QXpz;Me6s{eA!0wU;=IJNtf+m>HEJKVEy80<X%%qcx#9t8A!v($EO_68fozEoTkaTP^c4W;8-uy@L|YiUA1HQmd!B*0ToU|R7R^-UV{4#P0iRFp=ce7>hk(5Nd!^6zmt^?_aP+|=#dIJUuuOnm1gIUo?}>e|lI8P}3w*;D70%vs7l>c?<YSlSx+5ZY;%ROqs{u$lfW(+Ph@@rn0)@L_;<2FwLb9o$gPl7nIhgZXl`5Gdpzsn-wPn?-C*(cB<tv$(XN9MbOh`(5D8UwnH!U!ew=E1Y?>KTI(I=L_#zB&*oHCf_gekDJC^?bveg*2Z-mMTC*DnSmH$_Q;x^+WoTzf^OS|aFL6ex5;??}e699V-F4&G}!9-JjO6r#%)IvJyq_-=-{*bQj~;+UrNgKdKG^Y^TdfA`MF%6YQH2C@tZnYdn1P^wHmpDE|XXN}h-klJ5SU^1mw<!(Bgy!-?V)e_^l$BdOJR;RFBb(k6_a5;klZnIiG3@ec~VdrbkqUtbNeUzO`@q-v-om<Xgt0~Oip2E6{l9JT&polt9U5!W?&SEvXrf5jniluqBVmTg^HwLv0ae0h%CMl*Kq$?|?PKA3~NM0@68)N@NW}<%E{dqr5WX|%&1F@TqSqw)Nk15jWQ_fYzBbbUud}Uz^G8Y@tKxp@t%vsH+-nOh25C;@f+;B|x!o*Q%<sN~IML>ja3|yTP*`7_qf_nnAY1otRf|-jHR}x8mmFmITT1HZi0)V%mNMTIKgDo($EB&O$h6h<9QJ<JI!b7jHaV)eYboTsSRFV3+x4+P`Ca6RnqsU)k8y91l_xxxn7*2>mSh9wj6KxwYZ+5X|+$Wk1{L!)U5$*{Bl5wyEa`)mnl0}d=<Zu0JHnY^lC7Tk9B6*C<1J{=_Ngq=JRkJTU>a<#1f~;zBE8qbQ6k`d{kjqD@W%(o@dxV_jyj6^aG3B6}%Un1D8h~!H%q$L6baCK<^&CY*3PTPOElIu2{Gn!?2*j=%Y?TX!u<=r6gO{WCm3h!{HHm6e>RTenLPonh*go-MU<$~xmgHYt#RqX4T&@ky^Hls|MpP>9me61nQRi^xH)wntLY^$@@O6=kGPC@W)-o=uh+9GzR?Qi#uzfUpHk3^UVMDbtDuIq2q>`yP^WXSV!EVML<PCz|hAE3O7fQV8a@8QJ-h$mODjkVnm!`t=l0h^s5-Ft<w1%ymH7$@DTrdj6N?+o^c>Dwg%gdyS){eYp7esVADf#&Y^_YyMm9CS*--!XaUN~NA8#~l=4VMpFJF2qyynF;Vhr&#)avdRgd9jq#b%dR$+!Z&?Tt|o=Z5vA&HkTN%bH2fkfTZ95WxaLBB<^P~0Dw&ew3c19xg`x;VPI2Nt+cBN;%!JUFGanHh#Qi5q4ErI8THV&a3MivDL@k$nhI+d45zLl9D~WxlgCX}3@T9u(5l437Is^FWCM>)(qvmx5C+D2!iF6f*GS?>H!xwtI`US_YlS~jLh6Vpwv8K=Nb{n@hACQ+Q^OWFI8^5XE635BRd&@{^^z6kxQnbzsktbpZYz)99yYI$d)3G6g+oIjePEY%=7PM`WJ$}O8!ca)$iXVl^DY?kEq?Io-2e0TeR<Eq(3j}TjXwJZeR<K5cizgw>@2ss^M1+}MbmW9SF6-lagM@Qmfgb59^F&+wH&ZTY<;CiZz0!0OhKMDm^gCLqpA4e=@!m2G;!|HiZPd+x~YIr;50Xwf(O$Q@F`sOZg;4#-Ns&!ZMrUVAj5T|v-eW%ZD3nFb@n}1h>#W_N_P2pt;;vpyF7Lmo}D^)&EV+o?T6~`zw^%OGPh+CnitC?kPsqWqq+layx`^1$Eu{>g;Ij`_lcLdP)Z1hg@DABQbMy(@FoK~QH{}3RMK;7jfI$NEXJgRnL-=bJ6UyR-cdq_9_cOB1ryhQY$1fZ4T3s=J%;>OOUY5<C=&T9rH#g5;v}FNIuuT))M$Ax6Xn+4;GY85`J2~e8EdBL2@@JNbSJ*(d`&j#Vb=XXe?-2)_e|eKZ3D=KZF#+iiWWv)93wDrjwm-elo(`GJyNAqwI9X6IF;ym0!JiiSm=1Wb_e<9&I@QwTvB3<Axbw_wQ7<HODE)2H7rg;kic={K}&HZdWdeLVYRvmKg$xe(^bjtC~{LKn`k9&yd)Z+mxeE;=q@P2AaZNlWx9=~Vu*7#3?U;mW~6+gCEippco~i5#kdEgB*#DXa>Mz4GMwL(PD$-WDGSSUeuVV=$Vbt1zG*3~h>nh3E5Yd~0hU9*)&w(+r>r2xUXYVKjiNd6Vu<1lNjkqxBKwj^cK$O%dz93eJnPE!w6u{gU(Gn8Cz%#qFNp{RH+X=QeT<Z~Y!9(#Eq<ixdG&-3Ev`Q#$+D+-;7yUm6WSg2$ISs{i88&nEk%0)T7pVVYwzIsxB4~G0_g93shHQ#(p}*R3D*aSTPluZ$HicL<vybhSNAA~As4EwrQZRb*;T#DbYvpFk#uNGuOQ2XRrHngxd_ubp;vwCWAo%bp+G`>M9;tk^58a1%a&W;;W;~nnnbSPiE;Nt7|JW#$oK;{>fXKj<rm*BX72uuW3%;nL?}?MtM57KDmhOPgmA=U3_V*)koCN2th<jwTsV;L#_+VE$|}@4k$@hV<U4R~4lHHnitu_Q-K^Zxr`pCH(LXwBu;oXz`dHOx!co>pC<-RZl<k>J;HQK+FhdJ-yx1_ppaM!SK;^^IgUOEczxV#w`HR|7nJ@;c9bK?buhx!+g+656OYgC(SjYsOZKTVPWCo-0SE>0^?FfrUH|1NIue8Dug+h^yY8136Q_i)}roV{?J*|iaI<ow1Rr-$p$`<;J5N+$_P}fT>!yNv8$+lutIj@@iqH2_(YU`DRWv1qS+B_2!m}@+Cwt3FiWg$PbCglJ6Rn;|Xf#5l&{+F(6zEh??1tir&mrQ-<$(SY`uc<Y~OTK>9j~I<fTV<}M0s&2Ru2c5eb?5HcK-douU2ICQqBgbefE=vqolvCZxXG-)5ldw~w9Ia~_Ry=P%??57y@YgKFi+^(RhzS}>cgHer-p;0ar36(!xS}t?TtlDpCMoE&qYiP6VcYgqTj^Vk*@@ZV0Qi-6Oon*rUvQkZj!GmIw)}~YvikQbWp`aR6vA@nBpCyUEN<(LKYgLEU^QVso9q=N)-@s_d-C#y`dq}zr9@c^E1o-1E!U>y!gcBz2X~cEY>H`fnDTPA*Dzk&7r(3QyEXPnD4o*Dr?Oc{gG1)M9Z1JE}v`@H)D_rqDWLQ*#)_UjvELQ?8=jr>zTx05(EWwhLBVXGCPW{US6OyY<Yk~!pBF(XJw}Z0V9Y`mhUZJs{qR~9_3^s`bju8$aoBpF!WpQC;A>$>0Nfe$PU#@^{$o%JF7MLS1~-Gf<w)A$jmxJw`Z&-$I`y7^w5Lwf_p)BRSU)>>C1FkriK!TY&uicVF^oao1VEBe6mlrtBkDtSP0_-;{AIQ-HSvhVp0C3GU~?U^LJUX>9AgO4N%4--E?vlQ%I-ukjn57{R9FEdYvBK$(z`L_!8*>Q|NskcIBZD?#V-y{ijiOhsx=R1v!5YU(cy5YhX|Pi}B>^YpO3r={tK^fp}<ch56t?$k}+3rdRob4!F=q7e6lz{z?3#Y?mG>(?xj%xc%(>o+GQ}pR_$62Ezb+nyfjo41HzLpb=B}ttE8Vyh&`AJ;}3cP*86$(yo?Df~#g_=g=Vgmd+XeG%h2&jQOffu97)e7+Ef%TufBfhV*M?b;$EJoAc?kga&DIS0j%_odo3TRjI@;OC@uh$5ph%uNzj{d1t}uB(iF$k|e}sr)Z%bG9T%zT7rO2B5t<=zA8*|ty*%e@E(5@1e(5mW`opSvq9=!XM-dFCOGl5LCSAygY?CSr`c^1$#1E-a6<YHw|!?$NZ-A1LP`rKq|d7p(sv>XS`xw4Et?ZkYl1G>ugs8AHA6~Y+6*aHGbG>$k}2b2K+_T_EiI9fKgHL(B4M$LA{VS&k-9TiB!|ZTVlqa8{55MV$#R%L4J^EoDt&>v6&Qc`iZAGmlEi(XP!TR!u1MD`kx)&jen{=Y4@u@G^h1If5~kGbKD}m!6yKQ{lBtJ$fjz-hKP19H-?JrB|8f!!nu2HnQhBIYTG>3BP-ugZnBu1B6GoMX$mpQCEZV#?;bY{nAQld1L$Y(Uorn^2%ADXKgBi3}(fBY93et!IcLs(8=HyuOd7*lxS8<Y1=`x(Bu?{ut5=yOl$YJxZ?MxPt{E&THTB=1EnWionv+s4#ZO$x^I0k9p>a^l8nRmNLYl7Etfrv}OO4crn$BTL*RZb(UNF#8zt(`2%wQ8z#>g;=yzM9I@VZNi_4DqAypN+lQ`?H_^S`VHGKmwxZ+MF3@v&gSs`K6<%i_=Z13ssVkMNst&-VDU+e|$4Wt&Le<F|}%?>=>b^TFWOfkWhbETr;J{=hOO1V{#Ku$evV?LM8*v@BH=~YmVM31YP5OES<u3CO))`nxtDkL){0JM?A&Mc8Xpq?KQ#lb1KT0;~E)+Rq;_xJ!O2OD@`6@%xtylysB=dHS(PtWbM5Ctg@ki2RlAYx)eX(=7sVo<aAAS3pk}vb%P8WSd}Mxtc{J;8i|yOEM#_MakN!@ln|j-#GR@?I=n=G^tbHkZG8BtFGp19yzx!W9$o8q3JK}VB0Jk`usbfS$B9_w$BDT|y<g$B%w>dg&>(6wi$CQyn}y4WJTW>+pj&EjQjb7H)Fq?PmjiZsdL7=3ljeD^dSU3xY)p<U&NEn8nrJj4a!>gnX8$_IRx)|hPom4o&SCc{Gv|rQI<lWF8^F#BV>VH(pcp$cwDk3-jY%iTw(SE}!0}h#0lk09q?{>zDUFi3gA7YKikR;!Hhe<Bto?`}V!$dKHRgGa?F}u8@~4qFm}njlmGXu;5YgN~MT#7w6<Ebd3Fhi1#P<d~VL%J-BHb#TjMTak$M&VqhKD`|-fzdP5w-yorN|3WitZnM_igEC;=UPfz+8?(yXTDx=dmW#0dUr$YEJNitvS=)b}Q9ud~Qwzg@ajYl<%~*j8H^Qz2G;oW3><8w~0-;k~>MXTg&m`V{s_|p=R2Lhm2BEtLkKMLkFC44Ac#o+V7X%t4502FD*nSb_<0GHC{7mORPju!kMCsL3BCfm9*Q<Dkviz5D=Y}rfO_IieyRo;1+>;d0tKL%B22Kwo)gxP>A>FUd_}zfB46-Z*{8iUUaO^#wm0+LT7o;9W>F{z1ro#EL{qFvi?AR_M(T~4c5J;;n_~ZQ*s;Npm0+i=1#W#Dfcrk4Z%Bx*BibrVRu7~PbG391M#~Wn9?<6j<Z#8)xOexjcrpS!ZxT-G3;wpEv&j+vba=rFiVNw1sA3U*#h?l8$gV+33lL~4Vs2+P;OJ8b!7{?DriWagOb@?E1j7YR08<?Qwv0>;dqV~x#CGl$5v|QjU5~)WiIBp1+~d~TaZwM1%>3ZTiEUViX^^@k3BP`I$rxzKvHx`Oi|7;vF=5Rv6a1US5gm1b}zOOnxpVg^^NP<gt@ZArhlq5hBbBFS(c!Fwe2hB4^9V%xQOp-WbDNJssE}r@_g~SeoCdbrhYJgdm|%R(Sl@jRQGjr!_sIVs9;sEElt<9c+srla{E)7-k}XB8P2tRqI~-5!OO3<6Y712t3u9uF_TEH`js+|m6!d`-;59&>hF(bn19RlEgg(bmbp=a2YcL4(f#+N+r!6G(^OfpI^nep>ocY>j;^1C=0(sFmn*pkL1{|>I08oS&;;XkDBPp|NEv54Z-xomRPCXG1jJtGfF%wKq(G6OS_YJpe?oWYGAPplaaKn~;POD*AiqR}qn~Z$Nk{F9o!fuz#SdsG{{PvhzI{aU0JG>{bT6E<%53#D6kWqzB@!?IKBmRo#Oa1n7R{kZWl{!8vYk@*u@xgsO9w%R-K^GFCfaRsCJdl~UALG)g898O1U>n7ZDW$Fj5@Fm?5q?-5LDghn<TOgb(|-7!EQ7v0O{CBpw#x+v=<`SpZ9AQV80q3f7+DeO+r)?E1&Ysk*KnW7G6d;z9tnW)#X5vS%a-xs-nkuP?IkR)kxf2rl?=nB-5tVW?B<s*68K7gmr;Bbxt!{T3w!`Ktu)nZaKxjYs4w;gTE|sYGg;4h*MEEF4Z$oJ4lI1btaZ0$x;Kn+|yr42S-hG`UqB{p1#Rj6F-oE6xs<?En318QO+omS@DMcfh9uEaJ-`<L}clj8sBYXrIh>)m8?V#q1-6jzN1nwsTv`gIxwa(Q?Aw?y^5{``F```L*-Y61-~j87b?gfT=^C$4%?CVx<vGg5pWtITiEF)m>+34fD1&oSf^C<)F`1C4*Nydgle88ZWcD>X|iwT(h&dTO2qz4`gn#LvH)$}Z9BgUZ&m+J7H)L(>#fQF+=7j6h?WVge!vQ`F@N@FnUM~ya#sJ2tXhqZ{*9~^QyD;}&u3PiG1V5Gd^{!O5K%>4S^`%q&oe*Z(`@1izz$0U-GjSV6!M$zGIO=N;g%zG{^V?NC2dvr(@a?9g-Ba4bI+9;Y_1lILL+pmJQerc#39JMz72Dd3L=8dY|ZSGx%OhmK+619kW(fYGl|aqK=i+sK8e7Kb=U==%7lQ=3j}-=MTrHQ$S0GOo{DZGk}D(qUbFOJ_Hw(s=Ad{i*Yc;{_$i&v$rP`DN?G%;Z@$b^A~vM+tDK^Qzss=c!pk1imS`tuPpM3WW?v*YL0mp1u{ls8_EMH)5;3llh{_;ddr*Pep{lZuKs#s%m1o-~P!e)|Q0>}u?_l_$bKkx4tkQq>KJb$5TDu9=UYHN{R~d+DG9IP3_OMp;zQ$Ykvx@h*p;1e|R@2=wG*UeZ&$c6rbW6h3lH(!-g;<9ooe+5F>AFnkuj;LBsvP9I9QoIdFf$3%`$+(dUBjdlSE}E!8`vZ09x5TJzIvgK3R;3HrG%IhLz?Q2YE%s+Q=v3@nHG0#Sn}3^#4U}u#rm>cl+SyX&sjggO1|(nGQOb*>>aV(pcWA$&FG7Tk6(Vdt8y<(<uX&zn{lM8V5XWrQik{C-2T{y0}|F=!e@sEA(mMM=LY_8veDkdrkBlm7l;`Gu(}+!IVz$C)`!Y|ln^pEWM5{^6J5@Luy?Xi#zq^U_IpkHD&kF*l@ONon?sON&S1x*BWFU$2Rc&r#6{t1@6l~D8qCLEe<>rNt8{>GxMoD4(qL==$6fZM<JL6<!?y&_mnYpO`puB|j$c`b&szw$l&wG;4Annj^}&@l3t1f8MsWf7r%vtaN6J`dhDn)}*PP*w)RAI<X^`K7i|^`ZJ;A1YP~wG+jc*TV03h~*Gj0NFI9YBgW8ga&kS!;=wtDmMz8KMS;%H${?i;&E&WcF;0a&FLXhjCs1E;)c*W!y>ssOhnv$srp`TyYUBl?jgoMl9RP)Vdl^rnnpmWiu~{$Ls{m=ft{BMq&73gNkU2jOOv)^pM1HIZk9RoPb4mqef&%Do6M)KCq<RwP4J6YC2*#|>HR<;bHZ)g2#^iJd?$nobFre)~X&LxBW|RlzJK>*A;cQV<CXdqtXAP+!-keTFJlW%Ne7nRWmy;8}jj>DWnskpo-cI7v-fqXGKkEfLaG+`6angTk7)&}b073ztAd1SMo$w9>2XBpTj;?H&p6X#UbmxBT}Dq0e%T7B2u}lU!-D-uMsf7o`L4ZJXJ;ni-sS`XnVmny0lL;E28qJaXjrV{4mJ&P%3`!uCr-cCi(M6%Z+-i!C$U*6TJ_%g(Xxh$+hqPTSC!BljRpoaAJps;zM{C&pk(C)&%WNy5_dg90)WZ4zX+6!JPxNBw1)F$Gbwv<Hh*A$?Vuk8%b~mKbgMxGd>8op$<Jvl&s6Ju3343xsJS&%WwSb+#oLJeU?K|2m0^npCLMhPSPr*TU}9Z`YTauM63GUKU+ksI81&p48v^+ixK--JbaA(-jMG1i+nf-_aQKlQW(d&61S`>1Yxb#b`=Mo>3<ldQd1Jm6qM1bJ_N?yxCAzn3E^cDoD3uS3yt$fJTiNP?(T{3V{%>prlHw@tL-rw8_OWTbhsv=ff;MKECzh>LDu!a=`+-pJ<W-UO^O87GvgNgB_Usbq@0LDYHx)v{IDgsjL<SsozWYNw7yPSjoae;0u5uw#sb7^%+L2a!eU<=7AB+*7_g<NdMQ~D}{&&|CPb#6c1C$ab@rcquRB>XJcYYb37bLQlPTC4DVJ3pOHk`@Pc@_Jhy19LE^9%@$eiB14!ywvB|9V8SSExdmY{%;q*`=;VNk?#%6pb5>DD1K_$ntP}4{DO+><r0zOZc8S6HUiQ=UNv0H9unYh##te#Nf*h4T@H->S4#qV<tiGRfWKK*BBaME!NC;f(Z-vE+ihLisMH8?5f5Wfk2LpW*o)^O5;&l^dGr8Hql310hI@BU6N4`oA<{@fBp8dnffDXf;M>K73QD_m0+mH1I|tO=B#!J~ZzkLC&<_3r{aIxv~vRpjWfM2<$<PQ4B}+Op8^#or@xG+jlGE?}drFr&>37%hw77t9#s+knwr0iz9IoFy!|4H)%qh%;uiTVO`N!^nHWjQ)U_(a)}7M%%Z=jE?7+QOkFK5w8M9-#c3Lue{Ewbg^X9m~I8E^4eCefmQvv2FPp(K~~7Fd6^Z2`IuoHXBz23u7-vD*xQ7ziO-y;8oX~QtP~YVNm=0ByNt}YgS_r56OZSiRr)aJAX{(pTA_mL>9iO6-b~CgGnL*f7saxpT_^MS=yZE;`hE2z!6Y~=Mwc|U)N#sPH;rkMcjgg?5%JK~q(*tanb=foLV&hO(U^62Y?*ctq0Sr7Z=hns`*JgjZ!V2~NvJ#Ht6Ug9cDKnY@qYGsyh>Bq_mWsfn$tKcX+cn-O7x)ZZLB(=%a~zAt~AnHq>YOpp<U2Xf=n2r5}c!aMlkI%7=%ogG&jz3V#X5YN2~`KR#|v|*K`h4>;vM&!-_N_v4+5@nGCkqf-L_d_h;u_Ve<;f6tu|ai1OzxVdI+by8Lx)n5k9*-Mxo$cJ7<TduY9Z{5CSgpG;I#Jgs$-#M)Zoa)9wXqM47$sxAayazD!Wo0~FB0Z-*oj2PSATPafoWkJqWflI*Zg=jmq#Hv;zdz`}K1BclL!B<D<DI_)U5pEA?t5JUKxCkr#k?TGio<F^NbznzGS|BWz<UVjhB=Fl!h}9+CxYKf0@h;jqav@VDRTZRGVvn7hK-p21!Dx9_1dOU{n<T5KQa(*|M3z6jv%RWv5$#-FB<{WqX+f0}Oj;7enysRozq#>1LVwHXl8}obv()+vFNZmWGmZgl15%0K;26^5uchZf2_o67Xx^0zG=U`;?r?kZeq=)-oSCTl!3g_EvX-Iy1Emcn7J=&YhEq}=Pr4>jTA*oG8%%E9I0?)#QRu~2j|uUvDYRLYZ;}xSY6Dm22z_sgjLR(55$q>NrYLDnjV;!<B`^quLKUs4J|l6i^VTY@;i+aEZ%{-ND+)jjr36L{eu2VjCQwb~A#_66rv;uW&NpJotO@%x`G!m=otjQirY8vJARdT6^Xw2nKgJd6sd{-3IWie=oPBV9NA@B_pXBOMk|%f)a9QyXD^^0FBNsn0E`ic7tXYv~{yiV>CgfFB?3c8*mu~VznFtltHsxmg;%6|Zi)2$nRq2@8Z4!Ubi?l>l)qjL_RWMbU;Z<SDbC|SRgKPuiFO<9Z-FIp4wXE8^8xCJqjr6+<d#@DNm8{n}e1(N_TevX!N~ZSDjKSLHi+Bgj(mBmBT~~d+;^gyHu6k|t6~R@AOzOtiJZJSK5-x{2>clks62i)xVOKO&K|c$vSzf=oeGzGkeF*DQ+<GCg*nmzSlUaRjV%?9M$(O}+o0X~u_uVUngb%bI|7#zFl5DcyZ^BAO<j~xX__}MV9t&1-V@teO#;CcPF<Nvz3j_T{#;Eg>-kP|{IU0O(DxaPujkF5W$mZFk(NL2{${1bLPM0xbn@oV9NoN@&YVI%!iB%2oETWuy=<72^A39z1FS>unk3Zv(_3@C4>z>^B3+C#J*X8HFy2;t<%qk2u`;SLy7x*O07$+G~I=LLtk)`L<Jed4aw4P3WHj~pwN@Z$C#sJo6QrHsSF=d@xV_Lp=V&8-|J%z)``p`ndY6@Z`DJ?U<O?(AchVPP668F6FVA6DECp*BrMpE_V<X?k?6@x1sX}Dz#P+)e#-ik@dvPvT0;q_Db$fH6s&D}8_lZE6}@Hy3k2i|*rgxVLGZM?Q)wQ}$j#H#*v@$Y%Lju|Sw-$%cPbj+zdH*X$s2UL9`vrhXvZ56OR8;+QJA0%J)K-$DB(LeF#K|IT25Js~c{{R&T_fXz^P&<VKG}GwnanHP4na}aP?z8d^I!_pnOvWVwfbU)W{3ZFx&3nvGb~o~qf17tdx6V)g;yOQ>ujMDdSm!5aetROb9SG%{`N{mw@{=5j?=C;NWVYu;e)0#*Pj09D<bu<l)+x${SF!b$r6gTdB}>avQeGBW%1&8I>>XaiY){W-Dbv*~WqOw>%J`#`qWn|t55xp3tC+rl_z5%cXORpPZt@?!S+4#*P2lNU0b(oZo~vBxyr1x@sTw0(IrmR#q(g1ltB$rQGZFS=66cBN732f3iaw%~?#kI8FanNMdn@w{St7uSlD$yptPG#z%!1>0k`;8*U%^+4#=;=Xhu_%CIO-7}In-KVwuB*HJn%LdS=e4uZ}Mujl;mkD_Hgy=xZNOPke@2Qo=T{V8v*=>=?&xzPqvOkOH2Cvz@Q0uIl`B$!GVIZ<lzx9%ag8$Bz#4LrC;4KW`3Erw6BQO683o-QKYM&NQx?76`A%Gz}oVIi7h<sN+jkY;8c#c-C=fyDj|HI8<RQT92c@OY6rypjoI>1Pdcb7Z(_+pXE%Z=5aU7K2cAq5<t8VGiJ5)xk(Dx|9`1mx^4R!!7eg)Ri9F;&%|;46AQg2(Q(}#>O>JuHcGH>CuQ%D&mHxD7<C$1H-<m8i_rwH@2g_m2md8rF@Vl^Y?y8nT<?D26E@#dU3-M{ov+&v3!L66c9YfCy)otAG!LEE$^M=<Xs2O_pw0%q$JELHxi1|Is-~8ow?6%!ptE_Z&7k*h;x#fejHxghr1cwO@tOVt_)Cn1AeD$-PH;}=xwQaX8pn#fqR#W^EB0TT8JFjwd?9Mmbfohn9mrh=67v9=LMX`KRH{5Bl;TAsB`j^x3xX83{*p`LC!&+PE>ZT^%E`tvrR#oXYuPlg9B$!NV;zL~%e@cAP^!4)OKj91yb*q?OVI`6WNuBn!<jpH%xR+0f`<Al+Dpwy?7;Zlp6g1nefr@>=tNP=-2I+&;1rD`*Qa97wI+KH=budr_b+YDEy5|9a%xW2f&nhbwuzm%ur@o#o>iV@r_TJu?`EuDX^z0gY=RrDuv~|rs=uL@OLG%N^Iz84bG+?u6rGEK!Saoo}bz7vX#qA&X{2%_wcgd&TdAeU*qf`g(5GG3XQs(rGRo&AxX9XZ%a;us9D3d3d4~=ZjB9-R}jP2xKQ|9@Ra_3||30K)MuhG*DX>?Ug<Q4vk+{7Nao{=*P6x?>MFCoVs5M)j7ZO}Fm(ib~%UTNr8CX`dF<sOhHt5vo9(m(pb*3HY-eY{RpkJs9@ZR5&ZPBi{UYtCLIb!q&wEzw%^zzvlG(<ta1;r-B<;wdsYdOm5a0tiW)`6x_V9F($;eBj(SZA(-joOWpg1UcYQSkHE%rAh=BMU@i#cc#W2M7m?dezbi)V%SrVLWi|$UbgE${*|ZzTq-1pTo<cG&Qb`#FQgJmGdEC6SjhokLuv#g$pQ2Ug{3C0#XF+)*V@uZ86E-a1?g{Bt-BQKqKyYMKwum9WizZUTdwlawJmf+`i|`sfO1p$BV&tCJaH&ths(p<s8eSh-=MR;(?(tN+N+I<F1d0B-#2X6vX}1hYom5;g9H{b#h6B4^H`6bo0X^pPh|gvbj3K&0QsqAC%1@kZ4&Ts&WaCAIF>u#!X#^U8X-ZWwChd_Ipi^1cdcE~S^vmaE-mAIXs-9s70>EYT}D&EQe9@e=%AKECbg~326UcQ#yFO?fyM`nRib=mANfA=3_TpTN^dSri^T8Lv_7<tmdh=tgWgAppmtUz7fVVKns?mfcf%}Pas0zSu4BJ+R`ac&m1d;HW5H|&F4M+7)xgIc;vc1a>)5xp3^&?x*KvnC_fbwA?4z*zSvKUayvv59!g*fyOR2J6S?=+T+b{_qafCt}b+zdC)1q%Hewc)hIxabfxoa}BJ0iwFdpDdQTfDg?JBJW3bVM*++HhzoZP$Ur4;lU)=7hKp$Fk5L-C+3=1lI={WO98UNKt}t%6Hwr?taHNzhD&!SU?ZX>eL<S)m71gc`v!cr@S{(KG4@&4@lV25aUwf$OmBwD7h<%)}wDCvoYG?QXCt^#MVc}z~0jDofc;W%B%sG=`d4qeKZ$9q-rHs$C(rc@x3!tan!$Z?fY84_7<j=)*Qt)i3E5$TEp<;<)|m>1Yjd{hqXE}Bd947d>bZ91^3XB1QX#ycyfYF`kpk_eveI+wla+j>ydf(vUAx*$O=QKg8UrOSX9K{iTcn;4Nf3*Kd64yvHyZ!86|#_wv@RRKVmc#n^@=a#O-yFlaJMJyeQ{iu4jwkizxdJ2qoBN&|{rj6L9)QTF|5;=8{o<q7Ml0JJ#@PU>=#o;=UmwiXWNWR1Ny*D6`A_T(X@LTB~%ay=B*k5#Sm2xMRHjgcETzu>ox$@P6P2wfhOvx3d!Vct=rtgDv2aN{9ZMR8LeIgoI+~Pbl?j0|}jSo>m)CKESdi<^+RHhAHji#vj~Zcp+TRC|XmnyfzNoOE7>n<>hAbzkbIF3NojDtndO-MGqu?y&f_^1ln!L0BgCV6x@IeBm?g+AOmyyqSJCBA$`lz8DzjzTUfD;Ysf$w4fv8LU1;gjd4CcsA!5bKbmRH(kbyt+(!u`-en>o0_Pg|$JJ+`)D&GUV`tUd#X-5ejo+@cjZ<f`u1o@jd+#xa_dArD>1`wT(DLm#WIlv{p4|k)|__2fs$IcxaRz*3YS~_8#c9=rPHhi60fv3SKZH{2~Wch@ig-D&YJoeon)1g>G>Sk-Q&)IV(@7=Hm02G@!T0U`th}yQ`O14huCgM=m4fzLN+KOf3`gC%DV#__)V%Ta1J0Y_&YRanf*hrq$feqH22)pLgv8h$Pcmm|&k+;4*8D6iR0dr$R7pDVVpYEL1rPM0B2WHSB{?xF<v9ZE9Cw5scKC;MLK7Mk|#66c2%82o*6)EZAZvgFNRWC}3(+D#6(O=GZ|KQ4DAi*oH%Yr1PF|qMlWB|HTdQ3=xjgGtOGRB`mzIR`57_Q$_UX7~m<58lSXqfUyo>JT&oT_=LiN|~DK6>C<{Sh3d(ny~YB38EQM`^emBKZ1E{OlNHu`NVrmMjk^z*f=*s!OH#jeC<PnUs9&UyNTXv)L=dcJ5MqyvOzDQ|wfg_8@NFKVT~8{^kd?0evr)w)C@Icz|LzHu>2$E<Ef0`C32Q?VJ1AriGtvy5(mZZkyS<YGzvrV6XMFl^8JatwXi=EDK0720`DvvAL%NAgZ6OttaV2ttWr|y)qW7*XI=v@rB)|LC~_9evUN#Ed9qIXba!ZzNxxhlZUvBmM798-9P2KG!UY$c4cB-%8T-rBJwv>_cNe!P?$TUg}sz8r;t_mS&C*=zT;iGho`V9x7o^VnZSZ5aTjx*k#QNEVUQW|+93ss?h$AltGgsXQ`8rX;<C02=g{0*!Dj!mg3X7u4u2=AK&yPf4OO5r;rEL<G>Aw%rK)_eyoS$rmMfu3_1XcvflVf=ic{f_kfx5QM4{(fhR|689Fo!Etm>z#-%dJ(!r@?VLrLp7U<Q~Z&+<*E0u5H|^PIsOS4Es82Ff`uujjai0HUTW;uLWz?XZ>e*uix3c2!-xH{uI?jF!D1X#22G1&V*)6$_#oARH5rc-US%Vbr{Or4Cf0gOE;9vwDdLKTptE!EkzFiypCw?Ma$1gXCKWo`Jy5?+bTlbS+p=1;yzI76h)r?A@Ih<CB+B`Vi1}4b=r)Jh*iCc_?uT+&#-hzG5(3p2a;nefQ+IX0lX*mq_etj8E8DHuUcTT(mUYfARiiQEk1M#o8nvUkl`2&Z6RdM`JK8GFqH1J6B_-HSe1`NO7Tq6yjWg6p*(91i&N!HBfGilgZFLi=tC*g}Z1Z%5gr0dYLbCSGk-*!^ITZtX+kgS#2N4Hq4?;okAJ?Cex1PjF{|HP$V`ZAxHHG4j6B~;tJ_uEzp7m*fLHHOe2M@(NoH$-oL<4C|@IhC;4v7LK0|nG{XO69jZrA_EmK#CbyT`TJy5(<9VObvYbf)9KOm9Wy|uSPjyr|yxFJfvJ5JYU#Q-#mgT0(>MXj|Og($9XVt~|LCbsT+e7VEg8w;%m2|m^Vw12dt=Ht#QRIZH@eoW^%hScTbcCrZZC~7#KJc3SYj5OI-AI<|82L`EfzhS9-8dq1UHPj5@16}Qm+#Dd2c@W>xzX=n2-sxvnaz~9YI^!pXEbUXOBbJHsa!M2oO;%<YN$!o!ebn=RBb~Qsn%=S2OpYpPc7u$O&*H!LwIs!nH(dbH}(7;nOjLz@!$c=HI>6+A1LiaDXL~fw`lRCsJVwf5xa)Gf7z3JdZq!JLqazFb`y;Y%V%-3P%eSbb@>%_b^rZ9r|kdEz1XX$tl{~AWVNz>evY(tccD0(8IYHT>S&mXPCZK1J251xW<%1-F}QPSOv;8uf)A77<zkv0f9Qq;fmrH6`H_Db%shyE#8h2rCi!rm+O}#3*MGsfJL$4|?fp^`$kf(T6&Ds;M4Y1P$HaMLA^wYoPI;*-w79S^=@-{GjT##2RV{9|>JSNoXK9FNb6H?Ix?TfJ+v-hC95@}8C#yum4I(DW^}CX*>P03iuF>9BXkuv0PDB<(wk=9#JE_fr2()2&LgPYnQxjcPP^vUUyFnvaPG3E;;Dspg550UY=qAVdqwMNeb3wC@unX@XRF^xV(FRQcm?NOqgVE@l4ntbr@STpgOoW%|JChL!1Ag>PWB&B`2(URAYS`7&B&ONP_gdcY(4>Q@4AcrR)LR?m@UU+a2l)Y?9XYn~*F(^xgJj{sbAI7K#gL{?I(~&ZUYT*q__xmvf%Xy@^9>>w+)nc!w$3<Gk+nE;{IwTn?|=OD?SB2(o?rE^A6xii3x90kkH3Cw;kWrUyqjOcTYNmf$zStVa@k+@*Y^}ceC()S(XZkBule15QU2JlZ}Qpn?5}V1*`J(-4gO308s5>b`NhA2tmG}LqF<L+rC+DN`ZxG>_1eGaH4vmamA!cWr&F>;pS}ERO7%talC#yH;rh=YvFYd+iJtm?vKRX6^m_T(mD>31ZRCvkDTrKC?btj`6a5f`)U_%lz<IIjDVLEbLyWp0**;c-2_`TmB>)pJkKQhfu!D;D5|&YHYrlAtvJwz)*S|n05_P>}_0l#Pb(-I)|0ogH`%uqs#|Hye&hPm1ch3HL>sKYYbk3V+tIue87tsL5t1k-O+(hWTpR%p`I)eonNBel~pWW2-&gzoH^1XH!^^)wG`PweECCEfheCwZ<cAW0fn_8D&T?3>HtMuBfWBl0xrk%4qW_o1xc68<7QPt~t?PD@Qt$MZUdjjd2J^Acq9+38{s&A<}GbUfP1KB>8KO<k%EUo>z`Wbkn-N^h7e^$x5^Y@?sl>Ky-WPSeEu3lSMy}0~rxcc$e-BF4*Z!h0;-d*1HmG2EVuKD(*E<gBOYXo<zk@ct5!Rh?sy}$PCp8spN>I2Ic(@(qX+HO<pQ8UM1{`2d`Uwuj)^4dFoaaHGi@^$w$J>vBfB*x^%2XA)u#Vy-A>H0BOKXtvQ#brD2QEDN0la`s@)X!PQ&|j1C^V9NoR&4y=zZAG4gJpBI7M`y{)Zh(xLsUPSli>_e>rf82T6pp~8zqoVrdZWMx@sw!q`BSfyr`Z-D5WR1Uetyzih)1Tuxbf>a#81pI~w>9m5EAF8&C-jQ#o9Oh!iBQlWLR^rSd3uim2M7NwBEfG=9Qb`1Crgh4(AOT2D>>Y)-OXOGRt0tW=irE5rqzBG5}~jXdVb?6>DIWtrS;%7Cv#aI|S|NT<!pem_E>we%ZMPy2y;dV*^ey3$iTJXQ6ySKzfm`0j+-Y_7^RzLM|(oOm>I8wlA^5lliu0!5T}jxB9LDIyl9!**tF7lVlosqb{8Fa-J)$TtqhKM=X$(Nu{-Y^jRr5j92#6e;@NS@p81nz!Ia<NLteXq<&p`Q8oDpJ-gAJq9?}k3eFK)n9qw^4~Fn#|g+Sl88^BCpQn)E+uHv8QIfHcfFHJims5;Tz)02Fg|rGw|+7cQ%#6M>-hipy@Fh;&f<&USufC8G&GIb)SW?TD9MhB<+&|K6<Oqjm7v09@K!#n(5$honkHJnWHNXHQGPfSFm@W!+;CZ+T4S@UW;{(6`4)VpVZE1IOjCr8HuD=ui}>?~l3KLVMUgfR#>+~CUZbbb)%`GmXb5RFA$Jc>fJi+4SyZb(17q#5XzdNi<Kq8qT_yqof!^{Ax<5<^{gr!YY^}b3U5ja;IDx+{N#oD{ld;h3=^ZJ-Ix)fI*(}^@x~kE1G}9u|z&Hg+psCtOrmCP{Es)8NrL2UOupt;rF7x@zQ(4kXv07+#$(_jjYvp+4>S{r5<e*bcQ~-FHLHZ5l`pG?(9jWu;r$ud%yZVjnZocjz>_1vwm4(Um69|xSG3_jx#fvso4R7gtnd2!Z-)S#yq%vQ{p#{eFWKBc;^EinwN$Wm<y}O0LoHTKO54xkcVi|%QNmN)OjoW;<wP%`MIQ7bEFOWc((8yaaSgRGsuUDKG{^@@Cr~l<EQlPyaTUAYfohU10lAj5#ln1y`w=M7Y>bX?L@rE|+nscZj<pSuLJCOj^Q{>1XC3h<|+OVVo@IjA;HgsuC1&C`N0Ob?>v{3p5h_zAZA1#M<m;r}cTWz9z2_aydCe0D=bg^O%D-2rjEGR}0a7dq7;CA5Zk?>sD?G0^6X*rDGHiwO@n2o)UpO`Lr@;Q=f!oAU(Ek<839~Ddy%}RZm_YzOJ@IQYLvE*IzW-IumF-CuBj6pErEtzC=E9;w!6+ELqw!pM5dZh_;NoA99e_Xm{z$!z~SKDW?V>0fyeWt(cmBH6tfptuOJ@j9|tgB~)MEPXINo<)G5<kWLG#sE$<P`T;yT8y<R+2m5ejzPJ?{6myw&NK#_9E_AiD&;o<No;TQ{)hS_GPy3mqslUS><rU_PzWyPt5SEw(k_lT{^$V$@bmYW>Q%ShQ^m7h#NEs?yFO<*}l83Zams?wtW|o4o|+HeSR{X-}lazut;0^)SA||*Q9om=euSWcMxa0nh)SXl|xsa?^WWan;d(puKR&cnA)`~!}q`HN~2UYO(<l9cNF@s9*$I6M5158=?@fYX|&P><`w*v#qQjydVu0;AFlaSk5?AB1Gn>KPu0kp*GqY5hSLw^KH&Lh03DN?*R^(yqKC;dqpvQSmx_7E2h(?xoa+U-jbrv=6$=Y}^+ff8#{l!tUh!0o{vRyng3e__vCukMltoJ<49pSn&bZNCSZEz>Aohv1;Fi)q(W!TXW(Pc@4+)rm-(r@O`TtUSmir4mOJDUY+jpgB2?IzW>a}m3r67{Fu~)?`Q!vLJZ=x#~{5AzclY0a;Ual!w?w2x_yt@@KlAZ3tKw_0<`mo(9{oR`5^3T6+e;Q>IL?LWWZHdVw5Zo^N7iZ1TuDV!x`dwXpHnL?C$UIc1C1z(Vq3f$N51WBp#Z@0n-HJz~|5OUXbY@9ZREVmws_o7u6DDt#PLj;6)w5_B$Ud5#T{Ji0V7s{L17k0uM22y;P70}<fdpY_RSWXdzMEO<SZ#u|gQK`6vG?fdUG3>9&0pj##bS7S5ej`hIc}lxqRwZRHX;JZWzLzc)GBeFs;~UC5svcd#%3hd+-#yzz-Tu<8yxvb;MK1@m#VAQ^g?-CNyOTB$u+FHWcj)`u#7}LbLpuIx>-L-v?W$<h%<Ldk;Et*&*N!6U&2VTq=Isbi-)fIV7-y4g~=9RPGil#$AjRg%`8p(Rh_|y)!s$|<Q=ub)UfYw9RD{T(f{uY{r|C5KXNKQqNP9n`mu%I|F0jL;v?w)Bk2F*uOC7GA3^^=&JnNwi2MIQxc_(e^W9+mUGfv+AIY2f_)EmUcXRGa@EX5&X2VRpfpFMaW->C^PDDC!D#HRyqZcMmf(*H%mo>FdUGygWJ)y2A8o<l}km_rNrwg{e<N!GDuFwF|3h}?h-<!GG@*UKm7YENmO7(y>cKqzG?(EmN{H_XC_WpuGz<w3xTX1x&pzQ%uXu{dA2?^78*$0E2d`9_;>cCtbPLqhBN~SzKQ!Fk}_2=|}`7W5Z>Mp1kYN$0&K-X-ylk4@@ROs3DpECs3^Z@4W#pOuT0oRVS+jketfyFyBA!JDv@Dqw}el&KZyZMM$2TbknD)T|#W#3|79Vb*eg-u*)%{x4zo*Ad(mn;HT@%Ixbc>+K`!yj-L*!Kx5e~FuSas6xW&Y=HixcT#6)9t_3&(1GyQ55{*vaj$2LTqjT!Q->{5?;drnEra@QWq~S4?DZft3-nHrdVEfehv_Sr4iB<?7LfF_owc0Ndq{0=Nt_mX6XDazQOd4yZGK)5AK{faB)+9da`GyI=lDy+?i)KLU5PlfjaQ7U-M;apOGKVnu6SbVAqq*8|_Mq`Rngo)+<&ej_U-2v%LGiX~IRHyYcJK+9y8|3-F1{d#jTL79p@Fh8id=q{~9S%P51!4G@aQ7)BZ!M^?9D$7248fHfitN2szga1OLZ8(>}4Rp(P-<2$HNqTIR59@WnP3?twdoc9neu_3o?OrU6}uA8`aLrgCCaYIGgjQ|B+P=1z4tkjzY&BqM`zZhGpdCKOae56qw&<Z^KIX8K*AgGpt`0Hj_`(aIp7HFvMlxEFTOI77en2#n1>Ez?+WV#?kXH&mI4WdfbSWm7}?<P32&t%oBFQ3`yv=le5Prp3D_K&$g=bO&wZ$mB$sE(G4!#x&rx{jnHb<*NMKdUEOi~%uEvH|0o?DaZAJn>K`zT}2G!o=j4b&`*Q#nZGLcX=QqaHtBcupGpTk%dBhg=}I7bJPI|7Eu6^waJw`Xj+~DTB>2^;lxpf(Lpd&myQE%g0hDYIse*G06U+goEbVDX;y)r7z@6$hb_omEYFRSZzm^L>wE`9%|@VNa!1SQ1X7Cz5R0;iq#9UEzw}Zo^6yFLzx>(7SFq8|j!xh78)ndJ&IIVVaOVKX;DI9g?PC<@V+ZB?7$_Qh<gZV%_2ol=^u9S10?jtU!#u*Ngu=4l<EqiVDsRH6C_Yvf!(evO-=y!>$RMqKL>Juh4C&EHYIYEA=K;H&(!QTcba^j1PXTFgZSoApqyFb-F365x!gAy%@$iWGp`RHc{3#hb_Piq}W{@O$pOep>KTw1e%p!DD*~IgB&I5^W9`(r8irnW#k~6x!shZL*$4ged^SnTP(H`LY6vRQnNu+d{53s)-j1`NDGQc-I^b(T{12Cr;DWpFL!N|#k+!O`T!vi9>#4F85BZ#!HIaW2-i?8h~M<kG661Il4%^_|ced#RvQ{vXAd4L#yvL58M7y>Y}HK#fGR$xv(i2jV5#gP72W-#g3U*<4%3DP@5k8a)oIvVc{G&;N-G@2HO(RPN5nrdoVV?{HxcFhqj-oS@)Pbdr?i3sQ5P+m4}61ew%0sQm?as>zmR_v#MpWeU#7r;-T>qmop`U&zWiSj1gUs}l~%dh|oaUW@yM8L7|$9lXA)#>zKy%=1zK=<7OR~??EWpEotZqHkQtIh<&UvCziD?GQ0*YQ<lzCUn7cn+}&22htw0%L_0(5kd-FUxE8qf6u9Y*;Jl&6{y>;zMK1psdDh9GndtV)oQ|fwhvuT)TMAE!4#w^#v|8Z*Smw!-oZ0{ni`fdPf?(U1R>ld=u9@2-i#4OLnh=_Lk{-Be!)gR5<~@LihTHkFFzarS>dNBBk-9Mi1<%VUapR_j1*(0AHg!ba;|!GCY8aCyw9Nu2e<_0lvWN7-fMbPI%(=`KXV0zlQmihrEx72}^f7Vj3Y36_!JOad3igc)7Jj2N^AccsC!0X+i=K-94AKGEo1K_vCOXWzuIHE;~s3%89X~6C;gPxdxO2G6p<2TrCB71-BiE`|2>{c3?;ms*3}pYL8^czQ-4UO<bl!*a)Hnl*e8=(WcDgeT;O(EDL_W4G$S1YZg__Ne&s`So+7QTevU23s+Ee^sT(T-a(t0@8Yt}CS%aOEruPp5u`5$0X-ADa=EiDwjW%7xf}uSH=qei8zj(ILy3M9O<6Vr`))?8-wi;ob|ayAt!p-=3E4q;n}NhQI1rJ9d+M&3tYRbg554>5yfm?v*|G>#@rHf%e%+R{akVvMx@br&aT{yJjuPCOwMMMxVYi!_FeGeU(SDfF2)J$scEK`*x31r?^Bv1Oi`AWa?3l$Dop1Q%ch*{n&Ddb8&R6#6SBYn3tL?XWW&PO>=%#53%(n8HslK0M3By3~n%XS204#49jhANIahVScdK0vdJv6`3PCnsL;N%EeH|${@w22=QCc^&c!tC|whB8}s;Y6X7(vdMj|M*uttAY8IC*R&PNA&x}2<<^bS$QCz57KIpN{nZ-kxi5nJCjZ;MEG}5HNa2}n(b(SmU&+U2**LH&LHS^J6}3no|pyYGedQf1g)TK73ssa!Tg68p&H8_OD|koC0EPz4a1VIj^Z}0O}&5ZD>3%HI)pDReV0RcxbU1lAIQ};eZRCyW*S1nx$_N}Dz1%WsL+aw?STQ4SeTd>n3lQ)T*9#w^)y3ft2eUZ>JbQ=WR*uEql|%$AKA55*@%*Quu0%q$NF}D0$0qczvX`Qr847P^&9vpnhhxaq*XwfmB2zL`akcyi~)N7+5ka}D7_0@7$XyKkz(KpcIGXO(0U5`LkXNVzYP;=G<8Lc)x&Qpv>TX+mN=}5`d$=`nvwPc{4AUX67|VDyhAS@d`p|`n5KtGP=?gG<H4}tDQ8HyT3mKR%K?78o|!5DE!~A0bOoNdw0Ll>4lCD#NeJTk-HWp|UqggB`S8L{^%L~KOz+T){0(H(5i}l@sYCmXw1&<1AvJU&XMe_%p-<yUW7qO7p{ZMq_MyZglz;HB1SqFysAHk3bzb29u`L^LWaF5|GJHO9>UY}cGHFn*>XjuB5UD=V%cy+g6W+n>a3bUK6;8E3ncGtQ3oo;qdX~ZWy5vCjZj%FaRbgm<o*YOwlLLrg4z!z5iXh%d5j0m*1l~4#ETv<HVHE$uM8Pska3w{MrW8Sco*!tHPpbKWRt1wgbD&|0;5<JtG6;LQ;paD8fABIT9W$4?6PM-kEE{CWBb<f6P*a`bfkyMY4ahYOsVa?`L(6QL#-0HyS8V(+hNqSbKobsIka9*w5K-%C3dcQ1g)F|A$xQc->JGkR<zuAT>S-S~)NFZxF_+saBX&Z55EC&)bo|D_?){<s)jy$+l<UOC4=y<z&r(N;OjNFRyMOMberw#QJ{yEF0U*b&j@j8ol+opzUPJI=*!b-0!q>;dK*P@wY#jqFlMQmT$H(!d=-kLa)I~5^>P1N%2xMdu;_E)Q=BiwoFQfXpG8wU|pmgf`Xv?KH71q5HO7<#R7(MNQ7RS^*q8MX~3F3~Zik1<M7*lW(7q_PzUpgzC%1fMg8KKO5z03vl9>b%%lg-)Hbl5-Pe(0N@LFkL=Z9|q#X}vr8+JLc_6l?gu1t#hn2ArzWq(hn1q&J!JkWeeZULVIFA61xALXG}4J51Om?4`>LIy$`C8up9Qcem&!<^7SNWch182`hp5MXBgVEi6bFBnA!`DliiVL0Fiiq+}MEL({?d?58Zv3`cC469_{tA1zO~=LMA2cYH)Pdq<<Ua^|7>e4!VdEXGzv!BgoAl+kEfXJvlw59-S`f-B$h-~WWj5M1V!OBBJR4;>6ecMBypt%*m9LdZom%EpyKLXj~%LPozLc{VgO>{f|Kc&T*KHceG&C`vlUb2E+JLnl{*#F!2Sz08xIEz^=MYo&51l8vj3=rawOqR=M|R<?b9mj8KMLg=cW+xyN*{&Vhk(04W>f0os04_}$A`SwKTC#vQ=Jh2j#<dlv1Yhax!9yklIR&qR<%h8^ubmJkAh8{Fp1_YP^Q9T6m-0$lGx|n!|GL1xi3XQkx5Vwx(JMh8w?n%}D0o#+Fl?=K!hK7@Nnas<+_fXzp{(MV}gT(Ln!nZsaow=i166Vr?*(%~4=mX$QV*{$Mk$3DA1d5p+iI<bP_{g#?re8L~pism1_Hs5-M|K(!N#BdwQ$;-eIEs-#AFX`q7+y9Pa4R`zB8aw?w26Qvp{*4m>Rce9EVq~u`apj>aQkgW@N`Au!?->pRB<P)4tYH(Fl8Xaub%TlXMA4h`*2=Br~8Vh28skxD(HpIxtk9=LHva`cFw&O$(46@=S7P+ndkZ&ee+sUw`;9eS~;wA$?|c(D2iq3Wpc(@xahiWa?y=e4l8}6heu$ocCrs{Vl9MqZea(BQa2!i$~;T>re!Y<3nN`RD)+4?dIB5Kfsx(D>~x(egh{A1P+uTAD~IuY7FuIw%!S(=!$#W|;#oGO9X8%#{?eOjNn-=C#ktP8F`cE5{Y7l|yYE>?V%NN^&iRrD`?_l9xs(J|xLSq)rWxlcD8c6(!);j!4@^Rdl=b}OnM`E~%rD(pwG*i>T&?zMgXR>u=9MQul|56PN~**}T1reHj>oCa^d%n7Yuob-^6;`5Wcy)fkbh=|t~|N%+w4cStpy;atUiR>l%PEwk=PAFonUoi<$D+W6X7a&bFacCx>%2$GY@|7mK1iS7ZXqQfCN%k;dLjZef^`eg&i>qKq!R0aLqy!bqwh}Ho!+aEmrb_A{0DN{wg?@?dS2YtR3Nzm2z*6(4~{4EMr0<>4L#z4%9nB!1T(5Y06g!7T5F0UbyEL&o}nW06MP)bk8mzi}A?(Bi`9_ur?@g<|;mb*Z=TKlNGOAz9&TQ&h?)o%AozMi;qr1#kz#<gd_v8*;LgfTIu*8_&0{fNZpPy?dK}#6k)?n%sKuK7rJ40Ok1kUVw$p2P<aTOdo7zd&qkZ12MN03iw-BuX7DF3efuPfZsi5I>OPpb1<^tP3FR33qhu!-l~PSAKj9mPLnO7~qR0RJut8;ZJ%4{;gDQAmUz^RdmD@Dlr?KJONRgZpGi$$^J}-f&JMIHA(y#cOlxLvNcR*S`JnF*BVfPFw3EjhCo6;-Fr?hioLL&mwrwrHTga^AJCJ=W_Il%S-CgzFAKMFwm1~MRSbBdG_MAf!j|4=sHdnU!6aNo_|DK-{Bej}gOzxi4p*fFHBO?eX!k0olws@!c+;4D|zV>rdJ!^S_-%Q<-a2e}eTiv%Yw0)<y84_%h7@<k-fP<o42s(Xg#NchnwwG~J<&`Wgjsi^X|OP>W58!4zlA<oPX!ZA2#8IceyGlAt+6wwnyG*Fo;RYqu19GhpU5W&Q9l}$|A3OK9Zp)g*q2PXmVh|2_z;n&6L^h&8jZ)zugdO@>#XQ|i7bbJW)QXLIj34-Z@xyKVVYT<6whNFt5RPme;CbMU$8?$<18;-gk3RS<9ny6LkMJ>=x7f^3dpPf#={#he``VvzMWj=noj7IHg>b%?mMDAr6qS-BY`x&jD*gIkIT~$!!@@Hags{Q=+I!0$P&B^6!!ny#i-cT)y5|B%NQ?WI=I;-ZJZOD!IrriBruy1xuo?!@!;0AMf)dcEXmAMt@z;R2-G-Vapja8Las=Z36chm(96;Vx@cD7=uiaYjjSTi#Hn^{s<#^`>EiWV4}FzXe;bT%0Q4Pg$VNhGMlMCa*NN;y@3NP0QR1cwwwF+VfW_kwj22?d3!q-#n-w&|Q4O@g1jK!OBOy<15NP4ND;Kv7<5|A?u_YomB16UvJlZ)%9%j+RHFcvYxUQj_TpCwfR!;wdzjKJ09LDG9|{Gf6~0=G)g|LWVsxOP(NKXbKp=$LQ@(mr!E-SuRqqxFkGC9-hO<5%NAo7CnNtd{6EG`*j&uCB)E<08m6k4lFO|uaTUE)`~#tZkjQX2x{eXphA5N_e2y*ACU@g*w07IaTvrMo<`50s$mf6%VTT-Kkm4G1ns4=RJK_VXZ9jXe=&zPJ4ttWsvCOYWKw7;IiA_q60<{|@O=P_s8#JP!yi*i4rdFs?v_(~+kkKa__Z<zTrlu|Jy*5HnU<-;7DZfvDCR{~rH+DOl98E6(8$)AtxMy-hSl&$u4g&xpM4*-7u6rXeC-AG*;VbuU#-1B1lv}nRqcgpuiIJu-L)B&ld!D42t`um=an7oScS9-Oo#GIsO6VvO7p>QO=9xMzL^?WtE1stL|GD)_1wawT6Ia+sxDDgm!Xzi$XQg?C9HSm{@-|MP5pvRlq)*qoJuqxu9>Ms0B87t10$P8sN){R=MC_YJHqjWa6m`Qu18x3ffEv!Wex+c5ykO?tpe`8A<>A34LU3eT8dO<Z*X#-86~B&^9TT}C#)QS3&#fQW9b}a3%JqoI;ZZJRn%Q}pJ@s7I*D+i_F6$lx&7V7tCf@~)Fcu!BK1BaQny=+tLupsH^6_sXX0=decwsi64mL%oKJ_%tm~`6i2iAhSWfvE{dg}LFtfJ*uX~x~B1UP21EsyB>|O^pm)Dym)ht>m?MJATiTn5QW(KCrp<<sKU%YA;CN}|t!<@mAF^go#lT`UAWypWpFpC70MR!i2vGf};fjn2LV&sZb%IMl83r0%6JJisFr!_=zWU&B=J1=x9ca|1|Soo+YKxNkIC{t}F*ab$(9oE88pm=~q6N)?9850t$O=b<^!TSlpP$Ld$xAXnhG!|#y1$L;uri`;x3ma5pDbru(2t*cUsAnZk{j(UV5xDD8#hPT$F<JnfS?9E;b0wNso*Z$?@IIr7|JF@<%0KsFmc^~*Y1#4JjE1Y(M+(_%k!pPQ>qRPAM2?b2gX&Y62zx)Pi6TnaM$5oPGgMMaGS4CV!c&D^A#kFkh%@2v4Ro!u`B4xS#*9Wkf#s3zMM=Mtp$frt{lX`pY-zh*r4x)$gELki6|9V1`3C&8nY**<|6IjN3++(W^IXNm{|EAJK<U)8PNeSNNsBp=MoH%vOt8%YN-)M`m{R<lQjbbcolNF{fqS%W$atze1H=#NgW39EED<!YL*96L@1yJearZ;yWE=K7bpAUqi84%0*y*+``y8-9(6B5$Js|(V8e7^VWK{yPl}x;ykZeHGkPv{j+A);o?8k7YJTEhUWdrtk1v{0e({ZC`)F{dkARJ6??7{;dNQ8lmD1eCkkD}PAb%B6`Qx>9L57MF~7)pn`XO1f&;eTL7Q%0Ub#R>g@-L6E9U*TYu=J6(_)A6VpO@jB4bxQQ065^+0S?`G0mRp2~c0^=0BeLzs#&&!{q8LB0{Q952%PPZb303WEWAl186<3e29?ut2)mB{4p1UK?d|5cEJgRkBAzdL+b<S!>S9PkRGEmj$h-&;kj<1ud&PK29w5G5laC2xn)gT(fL9Q}lSxVThrK&rED(`P;pRbDu&4(=_yn4AvwWmmRs9PIMHR*cjbeZUB7T!t02pG;=Nq@FCqYKZoz04y`E&*z!6c~^C#ln%6O4N-r6odk(s9cXi60PJHV#StZTXxCW7Lph-`Po!u>4lCoAj|Bku`V>8S*?jx@69IHs-CR^tC~?-%1X!SstC$Zz%tHhovMGtg29xFiIv>H(pd<WLs1MBy#-LcR#v}~iMBMBc6{|3g4|$b^F;myMF@l)WwbRZKQkC>$(L^{0pHgxeq6TjbZs;!)H`=)0?}y>yBe<klX`)@zKp`Uxv9JNIgI|qsuuS>#93mGr#m;c@I~VuCp~dl!Qy=9wTZ(Xkifmn)O&cfsJ~_4_{#8NO2{g8PXJwD-3ltiF*F}_{7JP6)zFzoWmnoLxw^wfb*$$BkmL>>P<uv!%1-*y9>AI%KfbSy%VnA?Yp5QwrY%?&ZgD_oRCxy32LxQ+w8?F%_0vbnIz)pxU0C2gPLV*qHy~lIOEa*IlOOP7xgM{@$?^d#MP_2F!(V?JlJVPOeQ4kC)qwuO0xW(3`jhQKy5>F9D$U%yDRA6h^&X0ABP>SAo{4~p&X{aR(_|xfi78igM>-!smPc=Xh3AH&;t^0It#Jl4Zx&p1(vi$h{0bx8U#r)1s{r7}VyPWJ>{9y|KkCSTR6PHv$Nllwk1hPMg+I3NM?v|Ig7O~)<$vPBGyhRj{-dV+M@{*kcuo12|D=}m<(sL#Xx_iFykCCM{#|OyhlQqmv(%IqkJTIMDyzVWJ260MB)}$B`S{3!sI=q5Ec~r*DfPsaSb4lqFuzod&sEUb`?Xg4>Yp<`baW>Q>6~kYpUcOGx0R1i((GPo$DiF15=i6KySTXWrT%*+n0{MzYGM2vCoT1}CSCqo>xj$C4i&rMX0`WaYpgZmnL=M(@P#6Ll~8|9Al@6y8`qp}UG1z6@2?)P(1rKQMti9!{92d)hBUlBbxRlCl;27CGZMdU%1{5~pjlsED8(=Irmsp}zg!?*!~7+(=`Z=Kd-m5Co%x0^x?hNf&zF5$SN$#T$iMvuZwSYS^K(9{|9(r;{JLOzI2SR0Uef(i2>wOC){~#<yuU^T-rrP#ck$T=cjHgb^z%!V{FgNHq&Q#iG)xNbx0)qfYniJe@7HDD=bvGn6#q}HY$Kib7eX2CZ`5q|-lSSC;d;XAMGC!!3VlvDD$GZNbFhpooo|uSh-27P9D|>64C99ES5#_&+z^goOPH<U7$8@L!c4m$My72gz>10;#8iu2N49$~V&oP#LWb-bf&}*Fp`sb8_QH{nDU`b<CNnF+l3iUva*$CUAZb;avFlB>8)`YM_LbM4g&VrBBPRG<i>@lA95yVam{|RLDW&}C>!H{eIM3J1z9kB^FXS*2gEhs-=i+ZXKJF?MyNS)PR&fNH$n}Q67UFHze<P|$GJEKrnb?Ak$l^f+&JJ=7!o!!I-ESpO$VXScd4uY!$?0uF+cLa}z}uq}9SH0{@f%}RbYv;L8wi#5;VxED(O>xxZ7HbE?Y4|nVAOPTfx)8iO8{)oniJxbC^xc-OTb1f--R+C`yXK0Lut0yi`2OV)4fsamM=V^{f1p=H`d;n&6b2S_qF8+GM}1loSN+`=z?cjtP-0&Z!KyOE@=Dsb*E|2I$yR9#MWw2geJ5*<~y|$Dz(50Za{GysmvcCT?B=&G-)}a(^VnI5Lyg;$cQ|UL)&b@tcbKsG6}~q^y69}iS7iusR>;;4H6JkD=q{C|HQj&%blm+!_{8s58%k~jx!n2X9}9vI^x8gUkz>I+29@_+Cw64jhF~hV6X@nxP!%dbj=3XP=NhAs0JsAXmWiWH?9FpmWai&x^_f845l%F&RUw5Tg-u#^kFnD$GgEK9J_@A?&eazku&ruUD0nW`=ay@yyLFC?8n`;@qT|*_?Aot;MKuk<gDogt4I7%^+|zq4{i?~SIUxRM-kF8%-z$@2Kc^w*DH70k;}VrV-DLRgqN?5>qvhHK=vAU{G(rCOO%~wUNpv%)-$z7_PJlFh+edcm*D)BhFJ)=Hk~I1(Qs-J&NQy0y;veyI#P%-k+t#IQU;2v%bu}BzO$}Yu68p3Ou41m!*~b}1i`jzjaIbf7EGOvL=2>zN{cdTLZg-!|Ll+AdfhA}Tcf=hrILyjximlIW&u5K$$92r=YX=|+z`7q4QG>S4Po0~8_v|R#urg}Ny8cV#ZWbIHKIAKUXf;f!*PvP|HpoWmZ;u~NiWPTLYTN%s0L8#u`-p<Y^XTUSZ*hGz671%wMY@7^X)Ef7=wcAU*<nb3?~XZ_YE60QUPH@_&8fMtXp*dx)vR8wdhZ~|Kv-_OEvU2%D0f%Ysi_Lb~JM|z86bHjk}&d400A2#7snsz8qlUn`ss$Cgco@SIo&WVmaER(w5hhsuefdFksw95OU_FVBCU+3Fw!28jUCxGeX--b+n`W0G^Y#Y^E5<G_s+)lB7jB50y<A<X`x8^3M{4a7!+Il&}=A^gwlYOf721(-^g9R+W;VAu0Ow!O4{w<f2JH)IULv5Hht;vuTA@O>VQf0xDbKw}FG6aAgK6O9GX(kO$WFRGk!N+<wn`O^@B=SJi7e<|miy&D3iGG`_F&nidbocE6D(W}T-5>blo7l=+ENjB3w&O_{+kL6XoG!>Z#n3#?*G)njdaOH>tI<>pKsCkxb%3xE(=y3%Xd-6&GQC9sLY;G^#d9l6pg^wcYi#$&=QFkC(BK1z%yTBK-04zAEdq|Qq%GDX9D5F|I2kMF1M)3N)suj@WNx6R3VP-{YD@QgsRy5&3X6P8#Fmqs7H`7#Oh7IL0fIwPr|kP*@@s;LBZ0cR<pB2xP6#g!Wf6U~7TA+!5Vath3GOrA>}=PW1x*-Dd1RiT9IQ`<sSE>+v5Mk-{TY2bk=q>h$M01v7=p<-dlHqG+lMVRCz)C1af(hA5~tRc6Y`X|}?lw$$Gfb*tur+LZ;Q%enGl5C)UHMU%5C>v8QOy)k~I+yp#b?-<-B*`Cr1cE{>g_X{@&OgyBR9df4>Bb5bv_iG#%Ts=f<tZ)JCVrNai&RmsEKlKVd2+#j#Vgd^a)mmeDRUJm8mxTi{r_pbX3wU0hq9TMy#`cm;L}Th&?NSn=b`ky#DdssAWUh_7E3h!enQiC>n?LeLf0?g?eJur(ew=-Vasr%ot7sOza)krr#6$3z?feE>Zvf2jZ))8-mZG=Qs}?H)RS}S>sU!fgC?wA#I-O9wu7^g8`?Z1myH^ZQ=pf{%HNq~+X1U@tJ4@<ttzZOPq2C_K8Qzi3|40h>SaAdFG{z&7s!KzoziDNQ+Eqz%NauXCCdKrVNv$~<y%gFU-RAfNeeYm74q2Fd9z~BwI5jdt99OBz7@+12YG3+Ip?m$vU21zLlz@Ok|ipsS6RYwBFm%HJ0$62B)QJXevaW4>lfRF>s%W^ckU}ADl={=!>E`1Vua`=`TSAYB~G<Cxn%Z`>mvi7MF&d&c6+{VV2s*IS6`kYnFJzLF4$8BuDNFVrErNmfyB&!r*dr>Cdar)6@pcZp{cnnaV~48{uSYZb%;{KT-6;uK<E15+i-6&l3Y3&)FVXptiiP{Cu(*pOddT&7wFkRX*O^sJ#0hJts?9W$eHfhDhWiJX@lKSe5G-|D%jA>%!^qk%Q*-{l>RnSh79p>G+Bn0DtXY*3$zIF#(4En9YnG`<n1PCj%~SqMXYt4bmU>@4X05$;2r&uy`N-4pbb|Ji<Ee3p?4A4RfEY7S0X6GH%k1Gg}7&ltbDK>pYJ3tfnjk<GOaVwX*f^t9TG>uODZ!^lT15C<i@UC!^jO1WigPG{4;NCGs;yuotcT8u6c+E#K3LT)uoMjsaU4nOc^=kAj_bFqyTSmxvs(Az+xO>A_9MQ(mkE(?{N9U5E7BrwnB`FcG`R~VVt>~#Yu#hD$wn6cMjD<W^^P2xRiiqLIz+scnr!dL0a%w$MNx&B8aYPU@TOf|3CKLEY`LyJr5e)Y}Z`PUVH7P?mhR^ty@*M%64@rDS+^K&U1JO0?`VD<e)fou~D#%f+eI#7C6X`6A}alL=>I~4}jn$augxLD+mb?trb7#0fayTF~0Bn$81)!o6}yG&(*12d#yd!Tyu^&#y|e%`@avAyG}_Nq-w7M)`(iT*6QSq#txgE^7Sw&hM=*V^Z}!TyZNF2O|sB%tIMZ^JaGcm1mIoKecijSJ4zqr$h^f;{6R>6xQ*F&7)VqyFq_Y621HGU2D@ilp~kV!^DIRWP?BOnvmj50Z;#V~%TjAQ&#>%%zuNhF#b*QkANo~Q95__p@$O5d1O>>6;k!*R*q1jhDmW!|7-}!(fgyzNgNX=P-^LpoK=v}wO<NhOb6u2LBjtJITXC_8ekbwFa=}H*t;Rf@e4x-2=NF#az<CEd()vC~7+BS0r`<<x%OvnuVHivKoA9@?TZt)<ikNKRuB3`#J6A);x+Q9$;V#Kg#ff*dmSB~wYTCP~mT~-|3AHUsMX(#m%O6ZMRoUvjqLWmSuETSmZH?V77Al!!DF+x$zX}Pe9;A9;jxfDatOuDmQ=0BsW6Tp4-Lg&mF}--B7-lQucSuh`7mi>9IB4m|9=Y*P3zMqnJQ1Z>C(4U}ug|yk-2j>kZh20RkFCq$nhC63_OOg#hb&T#?0M7_dFAP0#mHh3HYssyt=Zd~-QHJ58Nu#j+rs!o?_y8<4G?QRnZ>U9+Kj?32hpEKwS_bKhfVCs`2<Zq1F4wuT8{X!T|yvRibQ0G$#b9!O0v~PTL<cv#*4PD(3SG9ph8=VQ$&5N$TgEngv2W=!#HB?D&k|*ktBQ)$yreIeVNOOg_1z+15pwOV-pnO0<$sSDwLN<Qb%=d`buPwNHZeWXpD14ki_~$upWB?LAiFAjff=`g#cA8{XsjaSP%H^p33k^Xv&J+)zp}YA`W1bn>V5M*Pl&5e}UHXn1Ftcys0%E7-vm8Ah}zQ*ylkCXBi(ODIb#o@{;9f1W_&&|F{M9JgW(XcfN(60)Lu*aQ24Ra~VB8L&0Lm`-;6RwN{L%l`{w<H5X`(I!?=;TnHA{&*|nX63->e^5m0T<z1wgl?S))j^3(b_m+CR(*9KyvZtr(cTdpK{!iaWTBkV{f~pWQmN2J2rg{qAFjS$PWsybl)RFA&G_zyGPUkW^RQj7TJ7kkNu07<3*<c}8>0AoAa9~tH%81PGRMNO0pqmMrwURpusk&um$HlPJi(>f!G<oy1aW|%iMkZrV9_v}XVGxaWjq_|1$)CE}TwoAqRn(=Z%@khK%bW4VSZqBO8}hl<EHj9J%K!CuHAgT_F3yq7Ww9{Kj+!~$+3aXrqph4U74KRB=}7NHB-ByaKNCSp=Os^$1lS+fK?;)&l0op(8;YGE>{{>(`NDf}xTI6i0UE_wb0US*WQ*yw?GA<%S3ge-MMr(*!#CedN4@2y(45mzuly!Fs-s>qCM(e}n~r*Yq@&(SM4hRVG}EjgMNiw9kEjPb7NOciW}Y;cQl}nCo*h+@s%S~pkNHS8sr;#Ix0{jZ0v4fX?6Yb)a*<qvZlS53j^MALNDb-QG}XI(XiC{A`)!-ml<o)h%}%-gxq>=!E0reTK9YBiI_m%N+vE{Ok|H)^?Q1QDeWyZi8cBpZZ10sfJYu@WV2G)|x5G$qx>6_%CoGk*sag17ktiJKpUKZ7Q!M8LB^N527uagoL^`JpRO1jXr?5A2VP10+R-!_p=co74Nn`(6@*)KLt3>_;<FJ20l9AT6vo(6#NLP^%ZqcQWhtUU#q)3)>VIU!R5}kGN!;-O1vqq9^kgfe9oOTPbFu<jdBk9VI4kD?K@>J;aU!%U7Z#qA=htT%)Nlqp{+x{1ist)Miuu4@+VX{3ee6|$Q+sbCIipvhA-sVDc%>!tDTfY?HBbFJ#VlxpMqG%SAo_tNdEeR6rXiSC0j>bA}yiPTPzC;3NWj(VQ+!*z+X%d8TDh{_}T3kSOfwvLziYPfxkQ~<mKcz=RVE~<>Eg}I?q6g))quf{k-MFF(5$FpTQrfh1yf}6cStKt%#f!PHY%R-!M*)K%ZZ3Yc{>qLo#0!nSTCpP|h-wrtNSX$wh`<ovZXt~qhMb-ee+eCv-5hSdw1#|?d#->l1tt6M-j!(D+;QlSvt(^G5-BZ_n3sr@R5Pqjsy{64x3<qNOFxWH>RG{%ifP!Z7X?G)&_xY8)qN)S!9f*hCZI?{*-1l@%-EcaTX`iZFnPh<ZH7s>5jsDw<fPJ%iKEGJh{#8nq7ilVXgwDd!iki%R`OoTo7umNuIi-q2RC|^!n!GX7W}EgO}8lAknJnE!lI_qm^=mL*6BOExAgj7{sWVdrClpY*>seYm77Lo_;fxs>sE#4P>!Hnk9?kzoy7rTf;Oo*okyUVJd|{jqeXhHRXb_8s>{sknW=4IESPVdoRmD3!ntJaoOylwEAHp=z8!%p|2no)0Qf$|%b-Z>jybAtA_MmlPnb$N*U=a_^OC(4phI60!mT+ASfX%kLc4Jt{U_P)8nr0|0==WW=1qYpFrXOJ!FY>R$|j3oIMQ3&t-y?K&8}ddpC85!>gccKGt)N#%`V$Fu4PwQ)}K0Zv1x~EEB)dcA``LKZVx^`Dso(_+;0T2fw|ZmZdRPjP{7KE9TZ!k2c*8nINZSg^43%$3A_M<oE5a?-~Xn3_xmT4-77O&6`FfCO4Xf5TpcXi1J=zeQrHKV?MXYx_s0AA(e2Bh^4G2QA+PP8x#R0Pe+qA6R_D>$dxc#2;qSKCbPjdlh#w?;5N>-nRDQT)yzpOtq+9z)xAu`p>Ep|fBm8lMKaTK6y0zDT89s8YedJpE$hG#7YwaV~+It<?k3?%9iPqkLXw8|L%LSq}1Ix$RHL&;(VUxI^5F>8wHHp@Si!5uQc5|vN>LU>Un$FO1J)LOHl7tU%t#yS8%P;8G=7eP82`h|iyo?!#8A~tam_jNxU2rKXhhafZmTyf2Y)+J5VlDCuwzi44%)61i?fCjDHm=O>I?So#M)tMZ*w-v2d+z#=Zh0bLlWNAqA?HW-wZdv<nZ78cgCz%>$lK;WXTQvt*y8k9i7*TPgk{am8Ron@{on~_TRHz(8n!snu;CkFB9IvMY&SziYNTFU@UDep-nH{2Siz0tQWtsG!XvzE573ew|FwDs2b<x`AEsW5?i?LgaN((pYo{-tNF#TAr{$$x)dTEnXZ{+jR&$ActvSO|c63vx2e6s(;xQuw*+_x5;0cRonAj9<=w<l``y&fQ+4zh1kMp{X?>u@Viv!}B1Io*A=~Itz*NtNm-6giR`M8C1<Za^t$4q!}I>T&~!k7V=58cry1@DfS?ZmWKE@SyK%zlpl7WKM6_ntL%fyirAX29)kXv}b`+VCdzOi-7*J-#Az3kBVp3c5T13{!EYom-3h#Jf?Jw)PU>J=V(|5fMcuH_Sd_+R>882{Vn{!JrNycB4A3pM4!6gfP^S=YCKWS9BFEpl-{LLuIKMrEyn84zu+Nqx6rtf5TS?zx^@q;Lh*7-wow)RV?V|RsMZX<Ph!vl@#?A@R#n&4J<mhL`-g2gSt_H>rSl*;l&L;E*<J!_5kisjLf&Yap6#_f}4ggHdFwRG&rGAaGrg>h7DCdBe?DOUDhx8MgG&R6T8EUYrwSgytusqTyk)l6!^ye09~MpSgBn({&o)>?@mp6!HxuUt%Ck-yhk^}{@2`}_tn<dpBF$>O}xlGYsc3GF~jw>=lrf)K%s!18K@4I|F<$-z(~pyPf9)hLX1<z$FMdM*`&H=<LWiHf63pn?WW6v(>UX7AdBl>?KnNOg!5qRgcnRan_*3CoNl?{3Q7|5<@JC|@#H){rD2=zNou=M$P%CcHu4|P<vA+X#SIH_?9_;*9|&}HVEQ5-+rZLkYiH9tHRZ?iRafM^#C;AyMO1J<071vj2;eK(w3a`ZkKY-VNbe*KAPE+&vY+4lFJGtsZo>woQ*27_g-|@!zDyKBZ*d2kMupvi6c8f(6qvGQ#W9dzQmV(k=zIYUIci@TirJuwEsRf1&Pb@(R&)8wSwp9{CS(JnO!AkMTq8d;Q7$nYiD0TPet}<&_2yUslW-OxXN)#7O|+2`R>VHg5H`X#hX{eVU=r+7z`PM~?J3G!BSN)W^rwHQp3eBQPglSURKWB_0W)%;<h%A~+akmgkO#gwR>N#NlfqmJZeABPOd>_(xYUGisetY|kA?+TsjuBk5YtH>dy>TrOIge~m&NoF#Pr^P%k-1bXDL2Y$x4oL)-!R;q6Im&il)k-`RsN#Re0};_@-K<h_;*LG6{QI2)ZV_60&2Mx~0i(2D?t-bwu#tiS_oAXDQvx`L|E>vtc3bDZCD*`DzL4rcpuz5Gg&1-xKC8k#*A-{YtM+=OVIf+rBSNXx_qO%MSQZcyZMuId`p;4Y7ah<^h=mC|}Y4lxCw5?RPxo4Og2QXw~;){Xj)LbS4IBDx9?S!_kU_5@dmd)dHKAk(~WfMo(hwYQy#<N=pN=R(!-_&9bK3cerHVss!?&*7C~|$fo%CWEJGoogkg6AXB%V3$Bq6@)LK0Qz2w;y|Zmqgpk=d8H*6I+IGRlbaoF2Y&#FWQT`-q4=~MGHCi;jPzQ%-IK+ls3fus|1HcU+%r=0Yi(d0$z6bPYgpjSPrTtJ%{l9burFIXFMD$z|)SP`P!w-IwUUHsm`Dx$9bYs$~phNhS9)3QiiK3tl<d#VSsvRubC(L3^tY>1jm^gl*#nMgC0Ygc5rG1n=x@Rse-Qm0TUVI$z*!Bi{19UM^^mCxI*82jAyMuEq-+E&gfYYkysV8=C$8X#_!^<TLKzQ%Bn!@-w;4&hR<g@}Uvq!q+a694a@-l?kx`khXbKYVA)4}tOyruE}i2JLMKlb<D-;qt{hc14btv}TKjb1}H{e!~%_;Ptbj>wRhzT>j@v%~Vg22pW+k73)&SGo(;y~JqoKEgqJAa=rh9B_R1BssW8Gq5q6El$hFn2)))@x$-`l=}<l_Z)tj+2)tb!DT<`E)DRD)BVBGl|Vvff1ie(7o!2%=v;bvi=NDIU=MG~7ZqE0`K}K{L-YNYcW7jN83bDlKmp=?f0fru%0uiv=f!Rm<v8*|ALzWY8{O1fdA0+uI)931#?$>Gl*ApL7GRVBEXxJ73&2derN;f&MfAcM2Vx8HGH5sD!7tUI6?nFR@f=aiQMg7ynE%GR0-e8Y^<Gd8RnMawYR>em&55e4XDzwHQuSclS~#Mpdbo3~Fg2XgRV|y>hzmwn$k?`Kq*W)KYa>#aaCvpEN!7VpHm}v1FD3&**73r&S(?}C_+ZQ9qIvC<z3Lpf;xFfgSN#A%DRNE;38$n`JXtGLz4xN3iMO2Y_aqI@(<-qc3OkGxtW$lU6R1?Zh>sXW$IjYZYWh(K+8gDWMCgU_*wK}W2Vz!<L9Q9GBcoG+UN6u;&#UNjhwqI$1(!*R*I=xuczjgTc}TWsF~7d+;LyZ9qWWygb`>&b(Ti#Y5A(ZhMuPk{DGY*+(YM#e_;4*Yr)zU@)bFt7sp@3ivuz**e&@t%kRNb+WlYr!&W#Kz{nNI3^91|;)8P8=fi}Kh(kqEGUTlGMenI7wqBxUBsz7lj*D;5+i>AO@eZ)PDeuq&<k1L7z#d)4hN=4@B8_{LtP2d^{!EU5LhcO4Cf4u{X(LP{i8-M)Izvc0pGxJ7YRgY0kXPdTKP)%<+9<6oSt1X-Jbvqla8OijPU6JE}?boGUyQX#JMA@?Q2)EWr?3*N>18z2d(S3e&Y?bdq-fDc_Nlv+?R~)%RD8$m)9uDl=L4On*<Nt-XIgo|$>k;yJ(Mvx{9`BdJ?_g3L8KyD7eTtly5xpX*@O-f?7}K%w?HcVOm1w*=>WFY6!q#pWxAsQSmFHs310sj^2FbWk<?TO_P4uv&<{w9QPXg&+bjRU{?)c~5{u*C0qW5YVKR;8k)lK{m+oQ=k7dX&Za-8zcU6CFQ6%KZ@uFxOQa1_zg*fOMQ;+j11`JuI24rFUW2B3&p<KCJ;qBG7>Nk**0QwQ>xH~JrXr;9yQPbJx3uJLmVyqLr7Fk9MW*pIY=H`t}PsC#&tc`a`55T2lg?;3kL9N7E9wom(475jH!BC20wSKfce{o2^MjBeK3CpRx6vFv;HvgW6ZVe)K1seL_I)yG7{4pxYOgVi8PNSYqpRI7^JbqvW<n2xl{cSS~_Rvy1wTbKuDVV!?rw{qfA&ZlZuzVwSH@rclCA_Yjk)D`(;Nh?wXejMM6K&27QQBs2zpE_Nz#JDp*+J^Q({pE6S^Xy$UZrv~n5w(!9Amd)F2MwtJLjWX&EVy#C1T)D?H33VEaZ;*LR5`c?C!x`D)z9G(<r(`m4#_8D4P^FMf?KsL^WD1m31u}}U)6~2tUH)0HN*US0=FK~O0ndZ8sBB#qV^j?O+XG-Yxa_uilprWWJ6HG>2^$_FzGdbUjQAx>>$F+&gLzD&(6&TU$Jgo2c{r@s2#JlVUPNiU-#J3@`&DYbGcRS)f-1AqgmH&!an(-cf$}qWjnhi&JI&nQ6Y9-KC1(D67r1rMfX=Qxd+ae`fE%-vH39m2>u~F*#@IB9F$SW^8k_6AO}Ccb4Yu#Ol~}dfbh&bGer4)i)ZoP6*`pJwFu{ZLk8j4tC(48QEZ_?-sg_p)wEF8d9v;>v;*VAP&mJu+x#eSo@$++r13Mgg?<IaC8lF6NywammXi-7xFjOcwq|Am-LBj)b^AP0y?Xm#2Zy~cUD4cwTu~L+xQ;ghv(C*R8PLkIzUfMt`*cUt*B-a>>IL$q?frw*=sTxy?iJG?uRxFLU+Ep5-hPHjPNrj-q=r%uK9wKfs~W0KEc@|b)Qo(df_c{FkmeP`t>sTl$5%AsmNrD695aU}DXCXX+xHt?SQzM64ZK=)26iO%0zbp-YDqE{+A@Tyvgdi0UDmuj)=@Xe+B3tav81rpa*C*M?-&W`u!gtEY$jsGUfgKj+TEFHvP)e{woKVePJ~wpo57w33>-AfS$_5v*UT$U?HkhWCU#^CgqN7T;sFSKUon5Uvs@yJ9<^!<7;_&~3h*6rJ>r7X;IQ(*Zvm$Wv0SYeN4E{yFgsYw_?2bK@XIRLs5T=hcllSTRK<fgBQ35k)E#3STZOA^zoONAN}ILSx*Afkp#IEkXZ_yFUH`88%RYR<RM(B$s3N8I@>B{uK^){heVV{lPmq$R!zu;)*<#%or@q2M>Yrd>V$TgQ&zOqwYQD3)@%F&45^E;b0+bQ+>J{0s@tzeBfO?~0X9u@VdHk{$fHx5+v;|!ejNG6~qG3~6-srwT2eB`GwMuj#|KRD=lT1TE2WP~}U`tCbD#OE=2*)3oBJ{!^=pCG@^5!g67C+-sL3Txw2u!hPbUJ>GmTT}VdNSX0`K}J+Tn?V~b6TecbEME{k_B*;hc26D_VY(Sv^YQaWD(FY2xr{~Y52AT=Y}UGwZZ>$k^kcpCe^f!H>n;945KFtNW`b0cUa@eGu4?&VauQVXZS;NPDz@L4;RvE)~YP!+jH%$2P;A1aVO)!+=zq^M#dR0N;xz1S$6hvBwp!Q0!yOrWSm;Js+$oykSy!YMOb+CG|Q%+vr?eFBq%l*xrn!)5~StIa8^6bV{(vpITrl9ogo`ME3ay6)9-F9s2S*u9$V4Fg-*@b;_v+kSxW_)#<(Sw>|du3PEUi!Pyfvel!fMmFbh>6Nv~p;G~K{BEO9DpvVO(yN=N4p1+*bv13Cj7H_;Fj{B^lg4x<MAh8Mq)!4~MxuHTKdQNjyUYI1ry-Y62CkF(-3OQqhZPGkFjKb7wW)$LS^^2T%eA5D20vb6T9!A3bF5_*os&EegFfuqb34V5)(l;{IxzSin!9=um#RpQ1GoJiS`OsNV{jul;)+Mp#11OucJ`w4O(+8wW~V0jKEu*}P7ZTj=7#F#UmP>CiuO*A?-z~jUL=c-T1o=mhdxSd>^gxAs*qs3?*#sgeo#_%RVtqCYz={iiLHjy>$aTZLq`e_k_!e{OE2>j_+=wixKn3@ZC%34MHG+kaOpn&pSy3TRwXd@;(BTb{~Q<;XdFRDbuB(pUm_pzlj{}wI5R7O65(#ZN3us8X;I9^`)Iqt;c5+M@A{~u2$cZwBKpyww$xWtGORlT<=Py!)EO__j?hYo;%2u*8qL3cwI!!qR)4RI1@E$Uo??vWv!27=iD6$p$BYJR(9QfXCfG*!t^CO)f>NvGnX3<Q9Co6E7x?un5_wp%z)3HG?zpUPn(gQ^PUxS)38p|VSACyEzgaf1=9lTWq$$zIO*V7SrQ6^g0HPZwF{?|9>(d}Maz<FcsYG_C9|Vo^^o3{jydE=w7r%%f>9IT~uanDO{=G>V~*B|Tse9OLGiU%$-(U&gT9smWq49>;k8^1acnbGn6&d|6E)A^g;bYx?M)Jrd645U1v*Z_Jwm!_4Ht*N696ZcKPTKatxS)36%Etcx9F!#%tY)}DpkDhJdJe2ogA1n4D*SH8NYLn6K#rQ&i}g~)?GiL;!9Do1%KG+of6i?kFQb#DyhEjAKj9*Hz^k@{dB_?l0tVnwFoewX~rF9Mf8Ms&jk1P!2QzC+a-gSPn-tpPaTK3t>7MshNID+=EsG#fFRF#^%0-qEoom40F=RS+qkq|60QeQtF=T)8F+u?A`FXFfD=3AYv%z9NF_VgP={oN8bg-kwI^v(TFl@73ZTgYLj^o1EmE>T<-L9r4y8?sO^Q?npDX47$C7ZUSTSZl1%s{OgW}H3!{^(R5paZj+iJgw4dk6-Xp9;++e<tE14{0%|NJU5r@ADk9omInlFQczY@IHXzVY!fl#2D34V*rsm-E#$Sk!)Uh<%ajdAKEHod&YKS`quVD=QEQsy7`0~1}Ebd+g-6h74<qG+!Nk|QBw=){S>JpH2V#mewJi(IU&aNh4+B=W0+h4ZCU+soF-+tnT9}(emE4CvnsQo&D0-0IAn$`fBvIA2-aSBUOx4v<rKqodakGel_Bi-*v42<2JDL<qOXO;0#vTS+TUwNW11dcIUD&md^`w@Ji0*=pwpq-&15mz>>a`1#5MbA>l1TQHqX~4-hl_ysNI`=x5qzJOt(k>^>Zzm>6X7pI?f&SlCc#w@VaIJ*>lvKF2f;z-d^7}PQ-A?cfoba%h(xE98AQkxkJ$Kh=@3BYN%wzWDaRbz#YPv8$l|Be4R+@5uW6E!7fCw1b_{#=p<@@xQ0b1KqX)hU|Hndfc|FR2b4G;)&7s$fOkN_7A5M9IOj12;u#NdW`79?EQTJ?{|4N#Qa*qHAd82zo{+yD`N!en0?WqJ&mUO7`I>gazrbL$gmUX!v@PqI6^8FJA$L5tnFe$4JfK*&BMfIVOJ(cHhl-29V2_dD)=(e~fpM{|Gu;M}jrxu1?FzIu}}h9$$K>90U5Jb4A|=PO_~{coPI?S^yPZo(pXPb;ANCG5H1<(~U#p8IaN$7HEj+znB+VwH;^(m@rnN-?9gc5pAYX56~bc4JXzuQ#u_1qVw4<v;CIjsljGTH%z<Lk^k!hMU6cgJW*2N}TB6>>vXW!<Hd%v^WUNkc98%6<kZ<&Fd#owHv$O0q|6&c^iX&RnqV(-%jCjCI@ubftQUcKR&3Q;CfH-BKiZ2Tar4P@XM`BC3#n?bE`#1*PsrUtE2)l{`4nar!q`mu&PkQHqz+IuXaiUovjZuqu+<Lf>OGImr9(yEepk+03u$6_Nh=T56H6!d{i#ZpS^mpT-*ZZv1);wX#p)}1L%Qu%#rE&isfQ@^HiJRF}obSp_0=veFhY&3!g??IcpX)TGooMvVpn5pmyJQ^9rVFmn2kwxQNLLX1==Wq==cy$6?T(P{a(g3TC6^{W~aPGWoG{=F#*l4va<2nMr36Ga`>V)iHhPm3T@i(`;il!ja_AQo5cgc80R!JgKHx3YxWSJ0%fa@aHR=`BG!@6MKnQF=5eh#X@H(I6YeKY@bl>45wSb*+M5MZl6}`Y;)*>IiLh-RoZ}F=_j{_o)yogdhZQ>{|I7(gbf01%=zIQd|OWj3u|j|_1DrJ8UxZwAnki!U%PMQ37FT!wSS>3BZ_ySM^F>)uMvv@hJ7e0&7%5n1Je-h@4{Y`yazW>n=3zUPM>gn2M~~CqDiik>an$;b+wX|G|OKmx4t$ZFR(uEvQ=`_5&?uisimUyEi`w5MutJzt;`>TJ*DZkc>l%01fh^K__y7^#SBmW?*-t~*~#1Pv$0^Jc?0-R4nR@<qI6V!g(74_&kwoV4V8qoi|&9|^b9M3ug`8u1rFaqkUnJ3j2cPtWldaLr-nOLS!?knb5lYDc_;`Lwji$5fFep17GTm)B$m)WZUtU|jH(3ApJY#C$7*oA28vsYM}=J0Y4XBWOzf{I+M74JJh}*}qxJOQJkX7t1e2xSg=Du__9ft*r-L!tfF7XI&bhOm!DReUypk>UuY7^m7WI0gwqbfJHkL7={+y_^3FhHEK{LOX7_n2w00h@b*<>mg0<J5m_}{o^1qGjRZ3L*bpx-Sl_7VG?wR~wgJ`oJF59iWxPr<;DMtV2fJNDW;Y~$drL5V1B7K6%XgkK8o(kINR4a~40E-bN&+CO^rzvn$-)66!73J9<@KQf_NYAA4LyLeAG`!Iv7q?Ot8`+^?132?>WCFKQQTgI#jN|(X&Gb>H{@BIb_K)rR+h!g}-GH5+9Qz}adUZw_|(E=Zsd0owPazU1nE{f!~?=2p!o*j>V<&(jCqBtl!^9<*ubyGgLeK;Rn`<CIxm=b25KX1Q=oNWDs-g-iA*b>9LG%20SdD%WCD_o<OwDm=Qh`-a3!I4dw>0@rVZJ82gUZ$RTD2hAd+&y7dn2KtSp^H_Q9tlrpS>f!G+z`9klx6XXnWK4xYHiX}kctQKArmzJ>a%sVF7+x0l1ZG^)$-I~)4}xvx>|PMh^@A!s}+uPwGwJirBQj*)naE`LhKkvX{}(`2#Z;vX~CAbf*c>@q-axHs%x>|3NAa^X*!eKYbcUZ@3I%c_C+B7xGYE-fXB6u3R}}Hq!RTJX+g&m2`y7FNt&mzy*ACP^lR?7eKsFgKU;*z8owV>56hia{Fyhzd_F|3$V|Jm^^!-=_qYzmxPmpgwp|w+P$X7tq$QM8ZiC<@FWP%ypd)vPJZ0GfzGk42x1ks8X3Qo4+&Nf+Yz51YtAPiOvKxeJToV=yI(=c#>2QG)gU&{o2=0%0huSbt^>T1(wpsIpdCzLu$fx^?<VZq;V#6#}gNJkAUG$*A0d{{C)LI;R27OmG%vnnZNANyI;SRtx5ADsK7f;p~bOEn=FPX3|`YYhu=xM~l!IMwhg<I+Z?+3U4V`F5D|8AeQkK_lnBGh8Gn;5+1!5n9hC`vJ*767%!`A${OUm0)%yG(z^!NCHs5ZQ~?5|*<XX+Hcz;c`p4yTFvt<EhZoeTO>>%rEOl_tuh2|G!$Gfad`;`98cr;)*%fbJR(}8A(uHBo#Y?$(~fMB#L7&n5{v<M$V22U@(V*jr<yP!D?Ru)?`g&k8NSxQVaZVWcL(Z2bnS^?3>-DF>6fu*HyXkP_~I#SUkJhiNyooG>0T3Z5)nLvtslpvEHQs{bFfU2v5_;4F-doWaSL17>!1tn+5BM!MZOrADyVi+>GqQZp6?ZGn$XsGAq!`im34&@0e(v{aDrb@Kue?n^ZMa(g3l@xvGYj0@}HXUcs-PffTgXDpJ3X!iMpZe5k5M^G9EA3(WrGtCAbcZuq0yo(yqzPLHA~s)j#zx3fM0F(=u!*FLu4#j;7i-k!&OqPe{7b;K~9TQ`=NsTX_Cd>5n@pCkcaYtIXMXWZ}%0O!a3ui#g;+lhe*AAII+7e-vTg<Io0BRQ6v?R<=nXG>FAh_u}BD%)B{3Mkto9^C49d1afg3tD)&=i!*uLm^*L${w#_B!AIAvetQL{2K9SHP5mlq92=Wc(c)Pg)Pjm?elGq5ktZXdVkxV_a9L#?|;t&*89x1N1j;V&YrvN`PsJDJZ;-+Y}?bGH#`4q+Y8gS_k^6ua_6fG9anR@^PSLfH6M1{`_&7gk!a>mcZG=STTaZ^(v1xJe557zK^k)F2bHNg^_VD%><JTVJZl83`J)_gP2Wb`6<$UA#P*jYilrEYiA&^X@b?blkTX6lKk6~or6$v=Zhvj<9Hkq#Kn$3X3R)buD#(<N9IQkVxIkNP#d*}M^j%!U>5h0kPtu74ztp(n*#K{BThj<AVbR@2iOxoL@<z5D+F^T+YC=<0d%#z;|E*=Mt~gPjOV2crBj+qV6FD}H>6u1xcuxiZf6T6No^7wE!y|$X%V2?T%7~fLl9-7wgL;5vAz6fSqa!5~fS5TnYS?9<Shrz6Z19sxd>B>Y!ED7)km;?OQ>mpDOTK8Aj}>G!LKMQXj!k-Wt9>_;@>Sq>?!0klTHk`B+^`7O3MR$6GQ8XaIv5Qbq1w{#!xkg5bMXleC^uCBEhl0y8U=yll6NV8*I_E%emE)MY#)DZD%x_7L%n6kz7^GNl?mIq`jGBHA%_}a4%%@T-4ocd8!u7Ux_B{pM)X6dL~@(_OUUJdQ^c=KLp=Xmwc!P@|2z*LWwWyCy&U0h7axQ?s<6oDd0dhDJD=(r5~rh6q4prOfo=SKa(C=wy0NA>Ha&~fMDTr=?$q9re-0vy@N5zl@EX^kix28@B*(*zH!6Jsu7fo|HrCV>)qTed&Tfm@r`<X6u*h-1)?~dWCj6^j4;;{tP$pR`#itGlX!W`^?N364-uk{duJi2tJ9AiQTpG4FmzI0%$vbtk`qzrqlku6S*NE0DmU`IeIK}LY%Dg`hMr`86uw6m|$-?#m#8nHhx3&?v{{2(h016!UdJ5ZB=si>OISJlBqzhC1zwTr1>h=A2I`Q1F(lh<|aL$ikNgmz1t7n38J2p+P&iL^d1b@bl*CNmgn9Xhm7{a87=XmflM)h!&fWPV=@!fs%K`WizKl+oOvQlQk7j^>x+uo#7g9q3d`S_V)&1uSty~Iqb@X7mS|Nks;<))Gi>NU>4PQ6BWEMoVR0vW%^n)AoBj?Hwv-#v~ruv<<90!*E!B|{U76E&76!mLOUOIIn^<Fr6m<+*6eTc$0H`8H}CSni4rAy3{Y?slr1%=lo6RfzN9JsR!g=C!0p(puz|VP-4DLJ%KDetC^5%9pUyhf8a{vU_Q~sqIZv_=Wzy@U|P3YrzBsujd%;izGWH+fcu26vXc~?xSw;yVrdEI0zq=wm**W$Cn>R_~QtF^<KUuefsbkAFrSD*ZQ4Y_M5)^P_pqKU%tDst>4~v)qjx3Haz>Y>A{!J`s^Q^ferqRUWT{yvVQVQ^_}_I%lTF5<@i_sjF*ew{gZxYj>lQl{-mGo+(*VY-SbWu&i@<{vX(t!UD)35`7)K4<rk&fQJc1(K1{&(>ED>xP**ov*gy~2uy0+0g(L0VM6f81a&!?2a9u}LOz>|rNOdm?uQREt7iP=G1mowz_NHbNXR7w2GIX4T?fp_}eN?!gzaK~Z@_6#(7k{lrq4DX>qca?z&?wnX-VF0MS?BHC(XAa_bBxAJ7ggxh@4-Lxb!80A-_Y--8BZR%uJtBw?`MCSUi$evXRe$iiOGg>J~E3dDGy?LbNOh-6T0!2!V)^(NE~5j<$AoODD52=-E`T0c39=cH-o=?gY)m5Zlq||o;<!Y!~Vd;@Ux-A*TsTVQzcqtddAp4dr7)@ktB}V>fVK!X!_%7=tXSapI5ABC8j9K`yx*7<MBH-s+Z;JkN)cGW7+%g*vHQwFe=T5vo~n$j}HspU;N(b!M)i5PyPzGI5M1$+nI~MbZeKMxStK_iP-#E{dj5H>zAS;AJiE=9^+@Xv-qq(|IS>K{>+74zOT~<T?QdM{-Ecditd2{IX_})y0EiX_`t=_zhXWbX!kFFU994G{0J_-x%leyzf6+2v$BKzzR1@9CHLo1%>=z{gm^_wEfol+)zD=5X`gmLq@`XY;#7KrmfDrCt&!PC$@NZs@5r-2{uLk~d`mWVKZ>p7?;6OXsYdn{t6(bvT~?fma2wDCI2hwR%EYMDg<{|nWTjL&3q+%7H-i+P<SEdJ&C^Coic|3ifGuh{w(>r_bW+e(m%pqp1*D?+MyyN}?={q+$hgSv{1uMhn9MpsUzFklE(@Y>_<haeE8+n?VR~L_uld}Si87E&*+Iq3k$AllyD}<~Z4^=tUz8H0XNGaRAf0Z7tx)Y!M1Zr&r{Q?UKmI(jo=@36c%H0BOg%;}^;EK+JiDtCvK}ZCy)ju&51$gv{cV2!7{cnwWIfP!X^&}ou6D;9J*j}Q4?cYIw1RexQJmO$sAPY!rVT)(HRRT-H|S{RIX4doibUTJkKs8gYC}ChZ|V!ZY4u<`djk7;6NtzTrF|kjwf@}B>c#^lD=RL`Y&c#$o!hjXkQ@!!l~>&i(PY+-WzR&YU6`?&dcbHd5Sx1SL1U?R6Qb!!#HOhbo35TmY+9YbnF4_w;k^Mn{)uN;kQ>Tf&{&~qa8FT<ooPfsmV*f81>IK%s4(Q95?50TD!h&cew_!kTiA}E=Jh>n$0``Y8e(IOs1t&jaTyK~HW$M|;Bn|Sq$s7DV9h7ot*E4z=jNU3)&Ng-dHz<e+oM#!uPFQtNwZ)}Ht=!n!xg!B>MgMnjT_$2I2B9V<8r9efm12Uf))wbtAS<InB9+Kb~9O83|LPadrewAhB$b6N9!sWI=95#HL;1{jnD6UG4Xe6zpZ>nva?8J4gmDE2FVn}U*>PQ!kJr&dk;HFlw%JM|L|KHr*nfus=NossSFZ&zGo9FfD)lgeqX3QNM1Az6=45R?D9i${S|(~Ue&(ZQoM$nUX_jih9kGdH#QMKmo`tM-ZeX;`-b@JK_OKD@Sb28u$6!2{^lELBIm){JQ;K^=s#r`S6mq+`HyutR$|0B)&SZV^qxEs0oq_oS!DVEf%1Z$CNiWW^gTQQFzrOs&<TXb`w@oE>_AsK^F&09R*jkrhoS5x5o9AXV7{M;7U`-A(?rF*L$p**?Uo?@_;h$aX({OLQPIyD0R^}jn02B{lf4c!Q82COq|KYuUx8f??r6T|{n*@=c-Y!{bLw+lsV8J6mgQgcruHsL_J}-IxG>y!^nd#U&!#HY{@iS8iKJ|2vk3x9(K=;jv&m~VC8xgmlXed9K!)_lglf3cPqT@Ra--R#l+@V?C9s$XSS!Q(r!t|U(Q=mwRg^QHJ*TQNr|L4N;t1N(8E_*NWWYmg&&({SzScIgu4isW_R3#lT3vlm{HXt5-<2f%*`A{!3BO7{K1&jQ-gZ><;JZ!&prbI&LJ!`b=)ni-wfk|NN_cX#cL<Y3^F}5aAUJJ>H=3m68f<5l?o2Pz)P?k{iHS2TdXcKqiv+y3&4s{GlHiAWkycF2M+K!eL%9vio05_&;7k&}=)phQk>8vezV|;v|Hhk|)TT7XU5mkxKSiHY#HZVn#<<#-NgBxf>WkDby&O;!Wn(&TjFV1P$8Vh3Qwijy;cR=HvG;@6&r2FO5KT{Nr?}jX$0j+@=|S6ft#4c#EmS1SZ2tS2x06Ogx#5gUzLWK&GpV*oa4a)DpV!AN!r&-rsYdd9>`NM;`i<^d@uuVj)K=5vI#9wude~U4J?Dd1!g>%_HFR3?e7|<*N%G#`Jo@)va~^$0uC3ReNA<}J8u`JjwbEa?BDw94XV8|GMUu&_Id_;xD{&A&mHKqzgrq5x#`!{F^n6iw?v6h2t%vT+#@U_-CcIng+XVsF7QDQPl%;&~)SRU)-~&fnX3HQs5Lk_;y+O0YHJ^6>p&xbn-S_8(!HnZ!<sqyp@=4C6)k!<K@WSdS!EbD8`J62rM+Vf<0wYM)%UGCP6P_kF2t0WNsc^w6Q|&S@j5CY&B9w$sKycWM{Dw$wEgY_-#xdw_yHL6-xf4Z`s-n-;$ZD`IS!-Xjc1XE?)4o=feJ$mEt*9%Ruu2LmYp@+_gs?JHmlGSa_i?tbk#KjpubD0j>`q6IlK$6v##ETUy=u$_6Or<`yR~OJch0%>?|-Tmroue_Kl3!E!Xe+mS*Ah<(s6&Dsj!}y3eVCMVxVm!+X)jews*TE9u9P&vV(>@0@D9ECYKr7D)VfeDXB7PAhHuKs0m}CCX7pJ!mW4-6Z0@}!A@w?rx*80#75{uQ%GUM(q@9kg`P;vkyYM?1_XVb1${_O&&di`A}dUAz7sO4vAuEEVk-PU?SWj=a2!97Vm0tg5>hyc&!p#&SLYrJcVRsiWNyYM!wNMrXn{K?E4wjB$3UzIQIwB#i$SM+z9GN!()^L9TbtM@d4932VC8H@Bvw->8ap+->U{SM=$Kp$uqp5_0twG(R$4aIw~YHjkt1(fq@Wu=ldq0q)HSn$`)El@$cP^T?Cjfb*{!DlkTr^^ixF#D?Mn|Kf7UbqxDs1lz*^|>NU4%V`@&L|-lU-kVeG$Ap)if&w%+x@9FvAk<gGKI&`9o{js-&NNL02N3GnPUQH{L`H!?JIoL2QkiuTnJ6%IWn7`MudPB<U&S(6zvTJPB6{EGW6-|soQzwX<+3w4!z<+qrm@h*xy1G(Ajm^a6`p{H2U&|E8PX`B{TwUj)@n4&1ZSL?6^A7<>YP(Zp-)mMB0+yz9-feE^H=uwq^bY+~T=_=eLolTPz1P)#6uKJkNGsZg8?LazkI%p%=2L3vPpTdzK5y^jQuLU~BT~s0?$J4_BU%!ie=i1d6%JEL2GT_<`*2=x;Ljta|5eO)%`UUIOf}1?X1MJ#j?0@fFh1!Fs^M5|n20Q$-LT#?a`Xt)kc7^1leNwb7z#o`x=Uz#T70XNzw(G+3rB2dWkc}lel1YL^!;3JJ4~i|MQ8q|x+Zq67(YE4mKgQy-usbf?lat8XXx$4ENWr(K8rIVzZ-}g0<b6Ghyqh?=CpV9|C(TzOJ@kC{<djHRME2%AKi@rpuH$UK+d(e?LVWHK_oSwK(q3>+(mD4;3pjRTiU&E;2iy~{jADMytY=82?<u~?14PQ$L0UAQw{7uFt})TBb({b58yS)3as(A4QZao%BeJ9kx@1I@U_Lb>C}S|RNe@^MjPwavP@&yxOCovX3!0k`#}GIVZIbO^k{EdwLy0aeh%pW3f!$6iyG2mbT(%lFTSRa)7N!Y8GvRUsw{oWPDr1q(QU*~(Z-l<?gNTDr+qiB-AUm-Jbqm%YBvT4Wk!ilj^ZIb~L4<j}*#=i5u6f4XtS|=C+?<Eq+TfV$x4GG3!dci&pL&{`d~^uA8}4o-O12FS3{|D_(SWK7z*E17x!d{f25z4d5C(0EB6!SDl^n<y?<+B<tCA6gM;)hUWl3diI<k+Nm2iF%C$DVf`Pmv5@png3keY;wLN;5IzUpXx+T9?0!5G2_ms-g>qD;BSE7vx2Ed=lB8M{zh0ub5<=iTBN%;LjuaNqO4DLrU>XCAifOARRu<mbuuF8lVMI^R=CduXxQeHqdpZeyND1IK*;n$53>EM5h_YTz)m72L#i#MUrWX<#`)J7!)7-yXM4PFn?%5QuBse&_2|k{FR{bH0kG$h+_(?>_UUc#isi41cHzL{W=(ULdakB6}>EY;D8e1y>$hWWzH3tNd|_V<@X#Q929S*7SWlLfuroswqH(>95usPER;WO<q8Vt(fwHw>_{g00l8JY<TXia=Q@JGUj3;oN3Go<5n`6Y=uCh0iwT#wa7@4msFWr5Q9*sNVX-|vS9`l6=1U1q_n8$^mI@wQsH-8Rd5&>RO0vKm0}~LP~0b2A$W(8V|F&gWz!O(Pt~0K#JvQ`YH*gNY;`O%5g?fp8NzP`rh-EfRn`JOVH1BGjmeP3O8n_NB8sgftD`V8H5%mFwN|F03<#%$vE#B$LxH)c7(~9u?*_M~>3=1LdvDUq*96LJsN--bkoTlw5}3$=9ORyX)`nLRw_L|0Bvr&}#tuYTYcljZld<8t;n%&3h4_nk=NNL-A;GYFkEJ&Hn4W53RcsIG=FYDW=cUz7#OtD9a(+XVWo9!z+xpswLgH<Q5y;Mfq$RV#+V`O5^gYTXU@@xV9X-l#Fu|DL_1r2xgToQC&8k?w&VRgXrA)`+q|pSITpPZu3%E4JPneBh0|6ildER{q20-c@K!++-DSnM~EzOpcF$@XVKOz__z=6UQ2^0M(HLs$4(!8VGI?2`LrTIeE8IntcBJ(4})@9Q{X1&(<FIo7B@sGH_O5VI5<`w1IJ1}5%4uInPul<1uiliL6-eZ|{_n-{ZjO+=-=}jg(^#z!oKdARBPV4cozMueML+{*`3#)r1N^V?wc@MF+fxoZrrG^=PHoFA(aGLk`lnr&^oA=<30)rSY=BMy+e9QXYQEno9b^s;O>VJAyiGDa8PpMu%%^R)&r>@Twu%|5lxsci`C|E?*F$nb}pSYU&#PL!{?Zhcqu**VL1hP_=3Z!UFmG1A%CuVpu`NS^FYS>|3!=B~(5e*FhzOEYi#Ik;F-_RANQ=aeZ0YCU!esGKDoLA9xW08GWa%f(U-h>Z_mH-SlPwRhZS9pR|i2D0A<|dTgn&(VU;Nus;T1;aK>s%=+AthX2n4uMOw<F3Tsdpe*uSPw`1fd{>Ng7KJXk+t~kjiPQPIRyFi0&0OsxZFt!BX@OIMF0bMFE!=xP^-ouuK||W8UWs;-WeS1wx&(1?E0qcZW1Jw*%Cr_`yhVmZR8B7@tbBwP={{T-jisNcU{1u@6femwxAU>KvC;vUX=G9QfCc<qa84Gnd`N9K&0yXDCwX<(>PYmDL^#WwlbQ#awo3@Bl<18$F{rJdvm!=i0g?dh&*tRG)|f_@p=%C*Wd^6DP0~kuP*sieRIyFY0VU;#z3|8|YMBNKQSIRgXWRvPz+?!)sx4=yrT)Y|fvU{I+{23ML?q0bLykV8uTI3F>>0&)wcCnn=T~)VyN$L0+zjY>DyEh4tDo9ZwA{R9oP4f1B!}SYyB&#G7mu2J`JbA3}t$iv{_OdoKQbOg?^ZTSo21W@I+%05}u6y-5q$Oh<(#-g*?kvTJzdtO1rX@WJm5jFpf5BtbCz1)}qWt@#>{cTN4>TTuY+Jv~u6b17_w2zK-wRIWo<f&4ccox4c#R$gizg!TXa`vZe_p)l}77@i)iOm`r8`XY7G8UXLuh2ev}R2YZ=woLniKLf+lb}(%akHGLiR8Fjdn!ZH_&ULSLY83;HV0aCiw!J#Snv0cy{Szty4`W5QA9l<5)%Sx{=%-?U5d)?8AY5Tl4=8&C3RUwx;+&WwZTpy7&QnbLi0T1NsRy(t^#BW%mr9DhC@CVR-%OBVY0B2g#1y4W8*j7OFZcxRXuf$&O!20ODgMeCy@s2JQCdlWAipfC4d0%rHstqjNkK02%Olf`1Pk~mgxa`)_qNZsa)SwaZyof4UPGWEUGbdBM9*q2ynfVKxYnsmqY)wwj5T<XFh-J2-WR!tgg1jevayrscgRdg_kq13MmvB4GlP_aU30Jk^SyfFVttS_GxZwy)qA!4-$uiq-wK6}wYOK%_nvO$O>vR0k*WeX_(p=^<?jCG>-bC?*yl5AAY0GoL7xfjJzlxy&Mo2mr#{n~D#j;1({@}B0ev|W;-j{7wgCo5pXo@EAsgg)>N63|LF*T5`b_c2XDX8FwXa6gI{HjWjU^_)q|I49$@M8HgX+w5261@_GSEb1u%Lf6OFd(*mDKZ<EGqYo%h~4-oO(|G%p~{m+1Wk6Z1~MAVR5)nTfNd6rWL3c78U4>IIE8o1Zw2Lal@S)At3zH1@JWgl{g(?y$k>ZD`ORqT4$pxmJK7mZZe((R^&_Vv5#k0A~F%Rl^%RHh8>LOfh!pbD|f(y5UBxxWM1SQ&1t%)|5CFhY$}lwxOD*Od`dAt(rj<{zw{P{Q!8_=d3<&_kuy($BZ>}uCPQWg>*GNM_=4jqfL18U@O%udKABSR661=obX8?}@BER9@34hF`%);8C8EV~4T)p~EEo+dctRaBI9-dS3tbLYe$txug%W4@PEm+-fx5Yfw9*F9rhKbdNE_E_2_@mspzM<G@sQ*#d*qAOw!f|N%YXd640)Ns8gEVCdN#~00A&Gz0AE%d-9fXqOxYS?dtK^hIucW-6DBUtTGz8=&~0MA)U;=7QFimUu4=P!AYVZ?8mm|}Oy~CDrpAEbaV2?f)WJ#Iu*;+jKlhWe#%a+52MqJiDLIt)i*BuT9mAb=Dy-k;+TAd=fk412Pe&~0)tTjtR5xyF8?LJ5a{klredG*(cyZ)7$&LrlR`Fu0Rn_s}*%I#9Uj!S8RK!N8mC8UVd9e@9R`DRh3$u|lkZUICf|qa5GUDmMslj>KBj~wd_P;xD>l*UN*jgU+Sa#<Za`qLnm-z3YJy`4`_Z;gRW*;3L83zuMsZY3r0ydz3QQI~~Jl@%e*A(l{K{BLl^w)gYl^c_GcxT0-S;14l1ziWBGuslkktU4AvrZgRkoC?(zb>sS7+eBZB><j-Hu;FS^A*-^K2>&+D*9!76OG4^9}D97$4Ksl+E~e3A)y07@c}sk%u*!$2oBsutnxhQXoTj4RSZ>wH_Cpzm!c@^#6v?^Ncm^K!wah-o_aFUDbp>ln9G1&sbXT_vG}+hM!7oF`Z$JSpb^YS2iMG_ayP2D^en-VI4=Cc`nRTB!^<}_*?BZN&a2h35hD6cb+HQ~Zms{JSO3FWVDqW@p{oQBD%k|a<Wt)N6F4*c#iHRM{~xk_Nv#gp^v2#&gz>cK)vVP4Q5vBZsWg_B4p8eY^+X+~UhN4)QgoOmDlP-@mFATHl$fGpyA^7hF)s3*12RijrL-ZS#5~}OtoerPNW?W0d!eXyuQ|CY<3`)(FZ>VOzv-)=LPvfc<BF-K5G=!}YL4}0XW!#KWq-ksqU=ogpbtJ-_9<1WB1HshNo&hdj|wkqK7mAGGh{XzQ0f31uyX_AKjMTH0%mWdqP~2xIUV^^;9gj*Ugi1_j22D;=OF&+S-r{YCmSteD1!Y}S}9w;RN9*o8F<3?Tq*eUsLLl6pcpvj+uG;nzh(lDyeyv45dVsh(KD@tpBt2&R$iatx9<WKGV+ZwBw@QVZvP6G`ZL~&5f(S^;keyN9b8C;fWjuvZ*WpZx(vtjKjZ~qfP$1FO7}RiI1%2<iqY*Z@PZlF2JxQ8@DD7?;~mqi(q&6&NL;bCRmhQJrBThU-jJ>L58cZu2t?R0r<sRme+>z<{QGxZ9PYq1lfNae<WF`S@~CVn4*2pqay6+q9q$h;w)0QlOBe%>XTnrziZ6B;3868RP{{k!?G2KRFR$IF7O4CB7Up16#ZRxX?fD)2>6U1#!!7XCFCFP8IOo#N5c$ZH=7;mOr@(bq?+dQ;*^YzSpGWNEknf8nV&~Nyu~V7{N6=1U2?`=oOWaNxaXX2>KZ4kK9IoRD*XaXn`>P_9Ifv^YGnen8!B#l}b=roBs33$FC`D^B3vEvEIl;g=Uledoy9DP@X$b%^RD?r#aT%FY)8omDe<-k=`xz{!EwG%HX$D|&`V%xxdJKw#MuPNXd>`h|Dg4GX9Rt4U5#UW&pl$}CZn_b2V>`uH1$FZeKB*HVkI;9Gm?r(e_^a|n8*XX10u4kShU}|0j)j9*=Xtl&#KA<kze4$d@M?InH8PIj6G+SArtfJCA)vPj)awghs^cf`nX7QiG#>tncr)~M_}n86>Y1Koqf$9w4dRN9C9(Q;6k_G&C9LiQ1y&{?udscnJtW=Y9VG7l)>~^cpSenl_F(u-=z4mv&0Ia^2sW^7Hdt(RUGjXP^q2!4s$ln0gSq3bKkG3c=6%ANVWr3Xw80#{C~czm^9J)q4d&`DUy!;iK+{%QAq;`RrSzfLbzFsh6&S6^`6n*GtC<2!f;oIw{j`P0=6WHma%^)WIt1#j7t)QIx8dWWV44KR)?8pia{S=E=l{!lMMl@yIrFH4KJY9unguGW@O9>UpJCZhI7x>*%*%V6woCAbC0>oFan7<q2=g(~2H%;8g}A9HYiMYWYLqxzPzo)PAFoHWK~H{VK9)D&Gx6HN^3g`OK|x2+Ts3(;Rm6g@(B~@_`6`u8(R~F|RFw)}i?R+1mh%c<IDvx<jx!bJy;3W3SWHh}*s$OE^!z3F7r`c0jr3r7cip3Uzt={vW)Iyqk8?th7t(%9s?{W_znG%phU|>Gc!=FCCfz>Y${{fQ8x=vWR7wi8*aO!2=fIu=I8YHY*)c=exKOC0Ep|X8!bHnG(i>sRBHS2LXS3gPuwUeP6X8eW`J)~X4ha~yRv{924S8gCOgd4Q8EG__H{0+vreiCG1JSkD<T0X`(W0p+$8+pJr;7wg<^l1AdUR@qU~8kD7Qtztqne${1}t)g1(u1Z^q+qaih_wK>d6!Z`9|s!ih^#WC}=Ms!i=I|8LkskIE&bmC<>;Ap2AYVs@sC7Afoa!kKUP(vj9F$%utH}o&*PHivP{RG$26KElja}=c|4S?D?g>inG|hD^?&!gvnU^Sztt!KFnwd@~lV2*;^rVEcIi}CzQVfxeDlaBKZ>)^Vdd&i%0oSKGjjX2Nz(zoca?N?=Y3O1l|qTR>Kvb0e;Wks^5Fe)L7r;#Uor=_TF6Fkus2ttn~qjw_65eH7cft6uu_{A6{1s1J(m3{pZAd<grOB)OOT-*VF8OVQRwJZ<~s?9Z!X){RtPaKAva&f&7K}D{g&3#q%2v$arD@TIcD&xZ3iCaDWh*|0(yIbh+}s?-N_F!@6pajV>{qBQB{y@wwR-oVn#LJhBaT7$#ZsHNyFGNWs{6!^U1DF_IW~K}4C~&w<Wx#rxm}w&BhRbbl|<xZ!;Bt=#5ct}tdT%@J6nA`>GX{&Sv`pRm4JZTRhkIrTI+d1hCQrBK?WL`OEZC~o7sAhnJJV%i!|8<(n6MP@c|Fb2MN40*G21}<QxUzPJ&vqg$Z(Rt#K!#7&y(Sni?{*KFM{19Lz@Y}v6u#(8TTSa#>$dW(T%N)m+3}>?6NA1j2I03Yt(1wvE(I*o#ogtW*E377ZyBW6~lf&@{)=JN5ZpZvnxWw2p5Dc$Gc&l8TWUkMMV`Ae1h!P&|Xx>>Kld(D}({}8^72dAc!gE;dj{HGJ8u?XdTlDEaa=+m%O8Xg?Bhps7C;8{TXv4bFh2oL<!4-ZJq&fAc8h*N;J_+!EgmgsyXPd19;KET70^mOB;OJry8{_l#slau70Vw8Ak-{cu(<bJVr6}x0UpT6Bc-GH%5ado`Uo>)iR+>g-1<RrV=p3bOK`Kxzlzg6&PZst<C-F>PGKYsPuC;he8<+Z^lwt<oLE5q5gpW>IFsUf?O5KJU8i+)ri6@6oa7OkOaL&U947i&Wfw~|b+L|&5v#M0+Xvt8Vlvc;cH3|8`{Fk~XlRL{Uz-#xUtcSmnlsh8MjO-1Oyb`RG4PNCDIsd*^ZbzlG{LAlt5RL{EOrB%f+U{|?7F=NqyI|Cm0!Y$opINl*?kaYf;<IAW(g?+LTq0qC#?&M>6A<N=J;;mrRC5OROA(vYqm_pjS~s~dX!8PRV&0S@4EsxP<L0Z?Kx80X<2>Jwj@mP^*X>t<IqIKxf5i`9V#e*sfFG}2_d^Wxmf6GIJqhVZe5|Ibpr^6*1KG7{5TFsU<E^v~m7+X0M%T~i4F^P1Ujr(_!z0XR0Mi^1^&D>}-6(uykE#(JT9~AK{4KoM>}~OxTgb&D^Fz8q=|SY!LHVc<UgkgD!PyDAs=XKNJ3tE{LJ^|oW<>7$ByMe<6Sr1_AUr?Mc7wa9)t0A1*9{QYwN={CT2<dd`vN7?D?WDG7gU7*FL;n;N2tk$J?;pxHJ5t`EQ8<RG7_kyyuZ<(d_9)IgJLiGtMGJL>}%*zB}A&xyIEtm;HJz-bDj8FMIaa&5sk1;hQ!#Y{AFE#t;wR8D46ACS)EoOYNbKi0+!q=W?;0zh|X6h)HdD<Y!^uE9_{ODm4Qq_EU3vaGJJRuLX}FPJ8(nu^MA~Qs3}p>W0d!hh0?#4-j|f-#RP=p%j}rw?RMs3XZA7{H6L$HYN(5c>5FCxER#yw@+5r6juhF9P7*|(9TqY!MLNEq6-OXripHVM>_oix%QGh(NkOq*#~feJc;;Yd){uLVOw(Z7U8|ZaR=!ZE*cXq|mmHe6%NyWidsZUi=YQs@G*CAvIz}0M5r%&1YG1I|Mr;Y|3R<sTMWh(XVc8%&Mi%8}2-~($LUGk)4|TVjz#P~afv-k9dbq>O4WHj0#!Ic?FeP~l7!LeMge%!&W5qJAtWyAA2Vk!f$6fe)I%kw~JYdy@VGXBKtcJlV|FQ4FmmB#hvF-9)c0=bF5h8?TUt6pYvqknnV%Pp$X(I26ycqoW76jWdc4$?p7!7wDl<t$TWJfmqg+FU(Zdj?RC#Mtt>cj*XBUki8(<q?m&Nn{`Xyz{18(+X7k*KX`wCOfe0|A!ENL*>r5PQ?G`8@9$6z8ce)4~#hSSEsIu+6Q8FKhaG%JSBhZ!ugwU0bta#ZAPnT`9+-NgU^bg<86kLJ}SYSty5+IW-$6n-ydfn2jqTk{`d$kCe&dH`>MPyHe>Xt&@_lMg`6#w6HQmxv*q9C2mr9G7W^XGM!n*pd`4KaU9Kx)?NsO89fxys#A@q>CIx2g89(ioV9jtLwRlG;g)M)p|>9Gg-)1FQuJrOXna#j8$~f|{G}f)srT+!Z!)CuO);oQ!^XZ^@>#*KQuDixpR4;fl*6=9X#&XhO#^PcD5pAGQu3p+6jBI3`t|I=SGBKyiu-@d1ke?fLa<PL65vB!26^Cym@06+!QRzuh*c&VelT)3vEQ*(x!_>1?1)W<PjRJmomY25(j(2E8OU*&N|VAtnFG2`WD|($kJVv8rFonLQcMHoGlB(fI=*K5X3Mjo1>=f16~a1-&>o;16%jm<4=S6_iZ$i$(T|f;_JTbwjd=Guw!GSEMAmA{^W1JxVDzP3rc>uiL;ONbzdx{sO1SbC5s9b54#{{}?q$ax#kvRut@Mp$>E*yP#VMmye^2S8`UjW$DFk+?AHk#5S0@ykrJ)Gss}ki2HmX73LK7pR6C_eW#$3J-ZN^!Lg%`p1hBON*`v;@gtfiA-?Wru9<wwNscHh{Lw9%}FB|8PRn%g_hdtz&fQ>NM%@-l#X5E<x-I4Ys01<)n4zLsyuv^SDae1Bx+loKqpX;u6SWmRJmnggb9JyX(a{d8fr&ZBvMg;@(9?-;DL3i(Yd&%*uSm0GfUG&2;Z8y~az_K)O%p%|m8hzF)JRw2%<gIpWm$b2w$X|)J@nx^7d&jyM$Jzio15u(N_Y_=JUHc=wIr>cEkSJK!!iMPK96=epL?W)R`rm^m0zr12cQ3)P3+B_!<3?4#w@3A<YFYrIHv`6*_Up%?7>H0#dV~b5_T8lE8BDy82WfR%e6jX{vn(TZ_)85!@+0x`$ouTznOVesjiC(&zR>Wa5ht+x!*Tx3Lm(m7K$(UUL4cBoSIQ#@QHZiG@T{*f8*3z^N)KQcyuTWOI!aVE6Jj;M9StnDgDiZBDzpK#8_N0`}m)CLjZQ%feLpEIC3>ZwRb^%~mG1(B_W3u7z{z}ngeR7#5D_{Hlb3k`~2D-~z3+?!MzO35#vM3>^(Ej<9S?wuh7WFKvbF5i|3X1UriN`D+;DW;Ar7;FO1IbH9nI+W6lTdk;P<d5plbs-WIOi*?=;EAfQf74po5v=Z{2YnR<1q%$i>B@^-ez!Q<i|RP>Y;uTEfW$5z(r!$V0-N;Y){Rnc!uF7dtqKF;w64Bk`9!cLY1Bm;VZ<k-W6Dj)v<}_BPKvRTIs8U=qsp#EeF4(uj4s@f7_&N=<zffm!G-+mhxpP+N&T3FfJ@hFNP~dl}uTC>E{}14K9jh9U@S9y{Kb?kqlveRT#6xj7sM%PhVknI|3`PAQ~bG+D@CG;6l~}lO6E28?kG~nHUSO2%!<-as(WNrozWJ$zT|gAjOq7P<L%Kb8$k?AP_uY2sN2d%&y_uaOuVpBUr#;aH%s--!eVD>)5*hhI(bBp{If!V;DIn1lJ?&eN(F=6)Si}JAOEr3*5RXr98kZFv!1nr{Cee|K|`XZGHW9KKUE?ap}gBZ){Qr+y|tEhmFh2H7HBW!ZaEb2VxcOEjj`y22y-hIR^^iV8O{?wQj<7D2d9Dz)4U9f7*#+kC|b$9U#?&&%V?FqTfYmRN|t#C^+TaypBe|Q@Y31R_qx>;kpjSUGxn_Pz>{lC*cgjR0--xwy$dm>S(R6{{^>_Dq3q2E@A^?JQU9wdwM=*AV0cjYf(0F>Is0vX^IL0t)1f51nlX3TkDW#w#jo;X=oxgj@DPLrK!??|E{W2573<jzp38>^Do{X)Y0*kVE&DT`L|oLoXyKo^?8;vR-__`=DRTB2AM<hDk)+qUr`V`j+Lht2cz;tLP1rY9w7XUj}iV>ADrUsuRmTVkr7#?`ZLV0yw=fxRZW>nd3M|xl`65Pk>hL$FPIGWtWyptR%Pz2(2d#>$-&@F(8q8)KIhglN=lYfuZ`&H0!L13;{<}ow3=n;8@m1hn}wPHEbdE^k7UoGU~L<2m!E{`vw#;ywzVLQ;^v8ewOozq#g=K!sX7st`Mx+M`0~WN8f))k*021mWbA18v^n|tk+Z|1oMLqvhUu93PaesF9J7ahUQLE^2x=mVN-L{`RT3AW+@O_!wM_>%zOP#l8{0Sk+S_b6-HGcCb^fF+rZqd9NVJBDMveDGJZe3*ozis<qhLk;I1yWI52&8Xnp8GMGa;KynJen4mEzgE3!9GjvGuSEu4VxrVI%VmgVP5+H$e2>Q|N^rJTv2H<t;6ggcj3DG5UBR7#Z+NBuPJji*R}Zp`_fE!2*#CkN3>L;UtxxHIrf*r)Y$u#<%MY;Xf7dymJ2PW3ex#sb!%DR}LIeqY*>5f=ep9mC{4WDl70Hn_&LemS$DChaRI-v*w4{@n_$H)_}IN4X^!SdLfF0)b6=zNDtBr4N$!~;ub18NCc?PxP>H?lc!1J=Tb=OoNxv=t3@xwh>7QCKa_8Yc`?w#sn$TYl3S)I@*LcYrjYs10YWz5D2%f-!yu9&SIDjC>m#`hq@{%|f9uJ-H&1vtk8%YzInI6#QDDLN2Fnng<q9MR6Q5P}2wkAS+v@*)h%qo3<nov_Fp4x#^ndgn{0L>)AZJvMYDHXQ&4N0x09r=W1;o6S>a-M6V!w;Ph#1}oT<Fb$TkNSslwSn}+V~&7PVVv2<Qk;3^bipx1#zA?ziOLbUL@n&`Q$=<QCxw{Mn5*Wly(W}K`u%s-S+vkf;WMd2EgEFq)MBa{8c2jK>Ju8wTc|RYQ+|kTss|AO6U<IabokRa8X{BdDO5?tSYpowL2zNGGG+*V&FiPJc%E3+i1&ZDL;6e%&wXA(Ov)687i}{(YxpjC=hN7mD%U48*yIT2OO5D;e;0P12&LB#TWphy+X-+05Lw;s|WLwcnq1x`UAayASwtNy1f$`a1du3@B0%)kPyKPvgZV@vsx#PvYQe_5Weu!&N$XaN`bn-qx8LjylPu!6Z(RIe<}FFjTL4(V_l2E6t+<QD=cl{b9|}PsI8==f@U0Lv~I+`X0TG7aAOzDxZ_svdkJpwIuF(}*?HX#vHG`SZ1cBDg&f@0jcE}}frfwaeG@O$MlYt2(YSyRbQU_GUWV?74oFN(++l=1SQSPfcwJ6tNzk;^C=!f&HEd2p_B^R^7AmVWr?Se^r#DvN#2Z1{3i%57q}ft5D}44w5Acq<W7&!91VQjSJ-Ssmw6w|on4_h7OLSpRBwG^ifrj~EPMm%&c6@;lXBuYVbjmPySeDsLO^jizPtNJW7Gu1M`C#PJ11{A_aMo_+aWxp-Jj~l{P25n?!;giQiQN!wAZb|P7wZ4iPwuQm8}X*hTDgdM{01A*i&M5LQ#NtRu4YrVDN}anX7lx6jS+_<PNCMPpMQVsO`5D<L3%rqUfmkE9RP15t6d}wR$Q{$QRf-TU~NC6!TOiq<}{5aQ+;-(zBrkw^`)6Ay0tOEM~?Kf^EEE#s}lAmB;?N6+D5Zhk+rIHN~oBM#i_;R%u6iYf{Bf-t1&VTK$UKFjer&RIE0%OCUJHP8&2ZAO=2HyXI)ra82c|=k-y7s)OX%tNE#mxNsCLG!|0W~(s@W)M8aDGW3}dtN|ov?>1|<qJrTi6MWZ(@HG1Wz9Fg8yV7fU~=PiM0Fy7mm`t)fJMR9fScj6jZJ(c$sv-giZPB`9ihTp^2xxF*@3rslo+|%ydOL6wxW1{A#vb%Hl625ogM|UutNY5WQ(<1yiG&A30oG@YTU?*ORd?Myk;r-n`n!-L+^XVOM<~^s@{(uzFH}Ep{G@xQj3U~fcsHW;WmOS({Zmnl_$G`3m!U@JPk%gSrpMC~xH^fHBUHQ*@3@8%#cdjdDAbZGwy~+E%q8T;)UpmZ8JJp0w4MP|ztTePfAuEDPv7F)3%bA^0(z76~6T3B&aP*T|JqP~H-$2(TLNp;_;_l&auB<eSfaz!Q!8Z^P2~0tt?!d>j5eKfY#p`g3U<Ym0Lk=$*yMUmiia~*a8}{pP0NxC=&8Y|Q3^K>+yOn9aHdi(jmg7Zq`tP_u8PkgxUUCfXX)zN@T!UCdvZ?BndS&;mz{U+!-D|2{an?iyU@GB+Ei;}qk%JzBKoVzV+(sl`@vrl0OcW1ds+>-JO-&FyBB1|j>cS`B^?)GRlSL|e0fh}{9ZT3zuNgd}ux`ut1)~8_WA(wP=(rMJI$m4HY+!>kf3CP;iw0Gpfu%j5ZQoz<vz4K(!1@I2wCeTjLNxqtkQ7SA%sGP3o*xOND4gGK;GQ&<t7<FRhzBoQ-&GsCiV1eFlXC;>V-dr1Elabp6^N?9z;N<tBz*%B69lm6ukl}hF!S(C>+TKpbZp(5;>$$e$H%Pu&MEoG{>x>;(NYaFuoK;u_SmjVrJF=}nD^7hn$1T$TJ!{30(D=tBUBr$i6KGsx?r3d8R=}ZgBn3nEcvRjSAqZ5PTedMmKzEQJ(gD2`Lr&Hg%&F|9Z{VhX30k<Vh$5XnK;jX;aPSs9wK$+I8HPpK;uM2(;dCWffaAoX|XJ~EV_m+G!$!Sv+tAlr#7rtadU-6>sl*>Sb=7ZE;96TBNG?1OS~PFgTYs{>u}#@3l=wB*d<n7l^g~i6iWN~A^m`Y7n>W4rUzmj2qi<x=iAp2=59d8VrQSFYqnDcFdW$GR*8_1`Ntkj{)FG~GCXlg64m}(+S?lxaD}ZL`85}|?mv4UgcJ=8+RW*!sv_P=K9xoPqq1@+?U$^a%E;vOSyY(e&r6ybiPZW?hk|<b@PgV>WIh(}B+W#jpU!h&sxwz)qZo-KSw>#d^QR^Wd}1S{sI2EPfA^Iu($s2-cz_@&njd9?L@bqa(yHkR=C|QeY^5-6V0w@GO>H0(!AkutHquE{U<@wCen$3VK1zo!Ipua2z1ex#&)yZz#((9(Qoymz%<fQoAgOeN%Nd0#1=b!&tKXRyjMHy6Ue=5V12<^h(n9vKkomJ4FMr~=B!gCA^L%Skg0)oAiwr<OQ6HyzOr8!+(R$b$M4C-Jgy{keqNmqz#yRY)ZJ@67fd1`K@!>#LBfkbkQ2sd6MP&oG7L|}T>{kM5JuT<0lT-x$n2?~1#LU#u>>-xNjt?XW`<$%?JDdY(mhtDm^lTE>Y=y2KY)f7}qbE6D8{VUTyc>Be9?!rY&8TO`6&Qv3n{^=9g(n$%&f_h|=p2s^X~KJUHK*>f>br3yh#<jo)u#jr;D#C4fn1fP*kM*&7c9r5>{4i5vvu>Nb+uZHZ2=RZD~bu<`AVT{+Z<D!qHDb&p<yeGo$09<+j@qvRl{In!MFy^4l%aDdVnqPoRM6ng0W2nW1Ai%xlAL;rH5J&Ld1Z_#mcowWU86%BF`mfSBy_)yF7u`rW0swD$v?MQvW%+mKSqGcuB(38RzBC%yG3#&dc^O&damlSzq+S{A1*ohu0;)OvmJxmMMJ2PLi(#TK3nUwwFCe|L#ITyBCspR&YGt*R~RGG1`WnI5loPX9VxUg(4%HuQ>b2FF$$y%i3c0!p?}?<#pJct18O#FA8^|l&PCjsTS#r;+Rrcq?ZTrn>1rtC=HvViCmE`epCZ5Ti(J-0zdOt-ZfPVU37L^T>C;cNRk##Ztf<AEtCRL&-S?z2?ezuW2GhKL&7I{b*?C?6I@@qW8r|-7!Skpbck=a$+~7&G5V2Xj*W+j5kw#DocBs3ZX(6dyr{|Hi>_E3hWRv)4Tr5T6x>@=r<Qi2YV(>*QC>1_gRpdJwP{$hf}C%JnX$%y^JNI3BV3!8mr9#CEd&xof!f^un){eHDPjS>8w0)J$WEl)g@O+Gr4`BHk~x|xU;5vBS5ZmlB#L`pMD;9FUQ~cEW6Eoyyq;t3OgTq+S`jN4j;N;K2QBC`TQ5M^dHT%ih(43qjJCjFD@l>26Q#ULXdvm9y+sC12Ay%{IyGYXGl6k|lH_O4H1epgo`_eO(@Xi0UMg=i<o|&Aps}F&scIw9Y#x@$>nBR7YSP90KxD7~+k2&Ud~H$c2Y}kGk%0J9tTxsAj+um_y4_7NTFHgd=B{Z=<jD-ZeTG%Y>3e-$RDT65ozL95q`{Zu!%vm`H3(f@W~<@0(eoiv{+fa%qq`q3YyXZi)p;ncVN6H%vx^w+gImZ{S09%8?8ZM4y$x~ZRPXqEQ)nj|lvyw%19%tXn$JjXH_A3-9y5@4GGuG{7g*dAjaasT;G$sbN1n*^=_e{1(|!gGPP|vaPz}jQQJ_7T)d=C6P4Y$N^`_9*RLnTrpR9-91rtg^8c@&QgwbhaUlg{#ntj)?QKE;nk|1X;GL*7hcAU}3_%t!MgaXBsF3acY(<iV)0uM$q5sVIqAjU$Lz`OW78G&jn4co0K?A7TI)Xtz#$F#S-fa4RS+mC4S>38BL{7CJ<zQcB6Q}De!%#rXT%~9#vvdx(_GM_Zk@2JCn_R`S96F-lAOEif_Jm)PvzQhNi*kgf8r$;O|Wjd$###Ti4aK*J8=7biah*%Is5PF<vEPPebJ1;IZ%s!=d@icOi=xaI2?Fq*8XQx)XufP4$@Dx9&e!y)$s`zp-gz)NyNrHRJ&$jHC2$s&&57N2%K|NR$;V(oH7{3Nq7~P-3DWe`Y^~Zp#pP|L7C7|1nfaOKmfSBlPKcekJ`;bbV0K4{TkxE%1l`;YiacwI)20#KGD2Al4@dsbEY)buBvnl>UHf8EqR!?P8yYkx+3-L3tkTXe?vt7z{uzdCtB}0Nl`7ZV+r=$MlnQBOyk|@g-<$$#9I!vjQS9AH0MT@fT7vvc??p#iV$5VX(9#<0{=}&G;fAX#RlWURMoirzV*6E(#oP0RSvV1iglK;*-lQu7~<#(@cJ`rm^C~!Vw3pT3Y^C27>)#VGHC)o@$lFbmU$TS9W)#MJJ5j(doHC;pS(O>RooU;W-a&#xfX-p1QV?;L-L||0mz0s76ZZec6f>!5J{#>N_Y>;9K$;gA7(iELfVyPfr`4ig}J}m8~|BF-Cbij1RURQb4cnCGUFOAcA=5_;t6NB}Gr&t=OlCK5^a`&Yrm@UW9(20gv#iHrdjpkM9wSJ)d*^2P+3dG<>j<<tv*wct)+qzMUaxJI^VJgA+?$pEZx%Y=Wc~)Lkv;#pLVl~GFGYn6pM*5cb_dPRy&@99+gOe6(s*7)^sLWas3)c;<gw&!Y6+RNH1?&2k&SKti58MDq+DeG^)cJ@tH3+al9okxq@A)I>#}~}Q@0nhNP%Rs61HKf;Q$B{7$7F?^yk43?0VihG;qP<5?W@*re}oRi-9YeIC_nRIKQ!#raL-Ni-gQ@Cg2%#+SlgRhcf+(`0Gu<tAgn6?HQ)4b$89cK=~`zaVW@csXlCpzQz?W_LVrDLywt(;61DsS-2x%p@#Mg1!C2g8(|s6|sQ9k_fb=C61~21wpI?eW41cZHz!f6HbPrDd>TfsBN?L3JOjahdUyk1Y`118$ejLwt{qo}oe;nbDBmD8@#}R&=m*K6v4A1^-{hYtn@8X)@_~m=@A3n~~_c*ro+xxEi5AxWCXMZ+5`0`nw{ev^G!N1YV@RnZIPkza^cjLO%%lTF5<@i_sjF*ew{gZxA5&(@w2{b<Cr(;9J$(yPCQa$}t%8sA;X?U1e%2nkhb0YRjp<D9fzwxt^CdiRM#z?O$5RTumWG2}rYW#+x7(fj?LM})w-k_jEesGi=c&dtDBIJ;|446|72GbPtvJ<0m(X@&Z)F{8lXaE8GXN_YnskpZMXFXY^o?&lZi_cLn?So?j*U@J$y&Pp5Bt$q}p59y)AU4nM!gNQoBUQ1nn~Izy<4xHmrP-(a^r@n~WdspwKNYPKXf{}BRUwZR-q}a|H0<-IK*5y7eMO0?*j-GwZ$s+K9hC>+q@wBF^mKGsnva{UCVN>fX?Yi-MRV$OpF~gRm%Vsry1SG6;z`B_G<yUhF&BTgk$%r7gFl`O6Rr7j+62G&puSN>=W+okog<6i+AKvWDcSG(=XIUIei`2>#cnIkC3a6uZ$^6u-x6n6$d`+s!45E@kMfRw66A3HPY-`^{Og&Ix3ly6$3A=Z0KYu>@l6>*|M*V*<x6_>n&0r2=Ldu{2ONDW#dE{%pK|Zh0q6h9!JmJ2{N>UVI`?K6>G&6i1$)Pb#R-qjHl8ZH)_q-i=&o!vx{~qu`H{~!b2>iY?4T{q5ZnXDSkj;jg)0-)*86f8pYRBTd??S_pZr`341_|Mw=6mR&Xc*<-VQz1rg{!HR-A~}>hr{FGr-APA;uE?CY*<`pXFOy0NLXL#onHx*a^`Sgk2n@?J8fw0>9ptV(<Et66>UBnZ5!XYw2Hm2F=ztS%A+|ERsdxnj(!U##<qeSaH8qf(Es7quF9p^|o+MnIaCzJi$dpu$OUcwFfDdQCg<ZAlw^+RSbtPbH%)>V<X3w*s?~q2?er<9)7VmNW6RC@mK+Dg4FRtaZJAe<pJR4)|7h?i=Oxn>|)RXe{1N7Ld6_-%L0IpQXweJ;>@?w1jCb;jA(spQZ20kuEDpZM{Uo1??eRM7UqJa+U$Szm0s;+Cmk2Of3pSuM4H9C=IbPNyYp+l;hGQeq2`rp*}PKEI2OaAe`VIZa*h?xQ_M&uYV|N)J%CE@qC{+86^fP*X##%PW>&uO@4r1Fq17>kP+h5MVurZ6FBrwnx6O<;sNyo-2@>E<c2a9>Yuylnv9#p6;jHv%@nvIZBHT($SAo1gg*FIau0*zR7y^kTH*5gy**dR=`!&%5&<a#<OJF{LeSG8&ZX1F<gNQrGgLO~oKvE1+Rn{ZW>CtnYT7eSLHrN&lA<Wr7{?<mFQiqW!^l8X1wdq#Az4mJfo<g1mqNG4Lb&IBXFt!cGfLMn@g0&s#uh@iR63zfFtm=s<2z^GW(6xayn=orW!2FzdWLiE{p|3#=QY&w;3LRmM*?8dm?Df9MBe$3J;p*FCMF9)3_vxSeNf^A~Ob>85e$8_H>N0-ax$*0k<G11XbsHdN^7u80mq*DlDcREE5$j%u>z2a_=oR=pnm_qA?Lay;0;D;pN+XJ~vBmm&0xHL?GnTtZuwF3&_&trwe-5V8DAEE9%$gJn5d1`LVr1M706z(C8bpq07$^{9`Nt}Se&xEBbes7~J9m}8xe>Bx<Yyx>e=}l_2|$YBs-l>9G;+4)7e3GgbrLvgS`W^?U~{yQLfwR4^x5OuL`>5F)jK1)!xS0(5a$hNGfuXe0$8%LkY)w~OT%23DGT=LhG4`zQ^^w8G?0-&@q++aTw52&y28cYQhU~gZRML9ciPbB0UkA<Kl=SO<|yE7d86G)znz?yzxWmg_>@NQsM)WHwJ)32obB=of+fZtxLr~QYT=_Z#-?oAE=Vq;Sr41F;AUYSAG0<trYx3!HXXopD=A&3ELcm#8^m51%w6qUAPou~u+^3JHtE{42Z}rh+^ZVbU1<`l*VajHCy@gYq*#SvF#VaYoMV98+8N&<Uh)k_;{f+yVILB(=8t;_^*IlrTEq8DzJ$1Q521D|GLTh4M8@VGbd!5v%&wbahO?7U(@AKSJcCd`|7YK;NnR4VE;>lEKi(_}U7<*-O^zV{LX$b$=Z?*DatjB|hQBQXA4q;S8+&ee)BH|(e)pK%4Tt%P!yKa-W{z>T!zLPQ=D7!pY_`qKNbdUczkf$GTpCeyAw-2pac(`@$!^ri6tlF|<@5B}X#q<bN;!F}%U44BNE=Hm$!lJ`xN>{Yk78{kQqJUg{V)BbPE7@!M^m%9I5jPa0P9;#)&Tv1oTiCAB4K6<8in*%VxlX2qwHR#0p@3ccAiWDBJUr&Uv+=MSKlXWzC}X>yX<ji{t9e^INdtc2T!Rs>@^h$gxG6I6+CvQ)fFfL)fydF6d7zG2BAKrnt`(t8!9=}8_L3rnmVMi)dL{8CJE1(?8aW!;DDF;o$J(_Oj=@pA_o1t37X3^o9^JkivbKd)HBClzZclwoQepTw47Xc*&+s(;w*V1sb0}Y62VJW;R}OUC?dg|CRA+ls$px{2?)TWYijUPVg52=B;z48>?dwGJ3C6ulH1o~QZ{O>FAR*o_&S-G>?MB7-S|RrwRSgUlDBkv)TmsPS}0IOvMQ|W&SamFapCi%vMqM)os>cbw{Iyi97#AcU{N4JW-oC!1GfLLkzgtu4G?4}l&aP61D}#aIxwSc7gjU|NkkfX>K^!h0%_Nc19L};)JWS}osDH)FA6fxtY&PP=BAR#mJQ=MuA{OU#(u>d*&%>gzenN;52~jw2IA$v_u)>xuY33PWvAW`-esrWs|Qs@zx9BsXgt%PH?To38^ud{qAFoNp-1l_J<;x*o~Wo4SLY-}yRli1(g#c4BidKGi4q1<*Is&v`pE6oF#4ddXj>ZhIvV)X-o3fJXg$e`;%blD_ddPQzK8q}$6@PA2cO!anhSk=Xf`|U<4dzXzE*vFA&7xhy<3mA^3`K2UytqOC#{?B_ug4I-$Tq6RU${^8@KXpJCmbq+eiBNiUi@DBht9(#@@Zg6@tjpxL3~`_b4(mr>Y}04wKYHg|Hes_)ZAx(#XtWP4#Y+qistQUp#8!o733|cEiAl&Fkuy_975a;~vS5G>iGER!N1@yGLLXSE$ilj0x}|E@>qn;*|XGr7!<KyjM0BTIB_=X>EF_^&9e<GQ2(FHT6&DHEk(zcb?bOXeX)|#hB}j)Rgd_!fV>_A+uwZy`FI{n>qEEHf4H-g=QwXS3D<Xp3=SH(>#dcgKBJn(=(BqB8cq)5`<#9jc{gn2CCYJg8czCSN<}q#-wEnX*-{i5v93GqCHlSnUS4}(~*zzozKVLd4Ka!rPw2$-71#c>T*7|jI`R>eC$Zv7@jd7-;`&U{*O&bvgMCFyX^_jZV=aJaHGW0!fr-!9G(#Faw|_G4Jcip)zd6yLr#40o@BSzv}x%o7~1S68%nsh;@=%7rhi~!PQA@$D5Iui?^5Bims3|jY;b+jFF<=$VaE5s>{|EO7t(=TJ%zfb?n#J!MIp_mh-YpU-!aCyhj8%?_GN2D?Q_VvBcVoOj7E{?5^!a&&EAY#M9w+}|0wMHMKa!bFzXGj=)$Nk8cnF&UNKs76(cF{QcsRvC+>S{JGYFKS{j!W?sVFGa1~@eB$!~Q&7M2ErV;$-wYw&>yt3M4LD?wM7$EwQ`0aIzmr8rL>cM7|o{Ho)^a%dPMc(6yiiej{A9KY+H>ICTDIUR-Wk)N2yf~Aw9%FrW3>E!si6UPnyaku&87L0D8!3a(jeut<*PNa@z8Ca_@cZE<aZ!<{5Z*yYrXi6YWw*LXWvwzftz6Vl7{?RUaHJ#}DI;srX90(aA01Nz`Z47Bi_)>1$%ug05Z`zJ$d>?95}k1Fy8PHHP@Vg>7V!_y*&{nBS*a8)B&fL2oZ-QiZ7=H()bmn@(o$rc)3fMD3R+yofv2kBQe$z}TAWmD4aJcO@27zOyTAXPZ{vf0P3N2X-|eaAJ!d^U=X2MLgJ<I3;SrxZE*$P|?r?__3hAH%_cOPT{sC_r`^6FBtS&zH_V<O){Tr{7J3El@@jzYh#I3D&Qc;HWY$X!FZIJl{Lis#OU}H8ViJlbWlue5=Yb3Vi2#F>xOgUx0c1TEZk~V;8I<<tX+zh`->WCpmp{%!L8)I3JH7Wsoy!9g0RJZ8suu<B;`UiO)sBz-K4#v+#5E*7B(#kFK7SbtCT@VGi<cZo8q<vIX+K6%GH%zzq0WSk-_;!;0h03^5U95?J0vO;5x7Je|pe`z%(AFVStHD-9b(`P&)$=5~2YALlk;y{N#kV}UxJd;2UFmSTJ(+ZejiB`;?@eLQ9k2*lbH^TP<EoK9JGnqDG{5H=;(&vrh;OYtSJXT699ePyO8H<O=7=3j=0xaVvmi*KK`!S@{`J%G%ycNWysA7@H!gffZyww>QrAf0yx49SsZ>-$YR$OhNpxLke()H{RhyE5K8%`<_9Zc5szk3gh#fMJuUEgIcngFQE9*em4PK0fyFWVVoqUax@KfWJ!79p&Ctp#OhM&rY+UIB4-NUYBo4>t7ZgrbC>I1Z^hJ63mxP+Z2<Y9{pUf$ETNGT&_hLPKXROHkAba6m<nWxu|1b|3grf*QUDaTC%xQ$U2xP!zHw%WSE$lamJ;q%m|V;K(Fms(-|U2~moYS`ohD<Rtk^?;TIQX}*9&O|lyo4@^x{jE#GXTJSIoTgi(S0hDR;tiHS8vp`KoE)E8Asz&Je#A6-cSUFyBoVs2H_9f!hL{gD5X#89Sc}A`qaIGE2VsBlSDDh4RAR%7pLgaYt?49TIjoCgRJpIo2IpOi$sbDr9WYn6jIMG0&~L@dTagW}L0F88JolFR#<GAnBU|nb>oxyBdvDTXOSh&6#cE<jvtu{8b7%8?=ezfQx2dYzR279KTShvFKfnlPGzJM<SO_Fr)lkS#jj?5y5M`k%K>;2B17iVZg5&`MKoqhWB6(mez@20Pa|DPH>v^7cMYFriJl|<<lSir4K09N_j##mpcfIe^P<C{+-1oM9@n<YS%qN2&CZ{L7au%w-G>A!vU~;!RAIJ30loC&)nL0>;u(d_wLQDhGt_uLzydtHU!ZT+$=F_>oNZb`Wn@5SWInC8ns?#!7sOn^0sZ=WQ#M;V$IHvzR_9;IJKIe&0shbTW0E<7#-a<>BNQJFzc~M7WED|j39!_@7mz1CDQWj&Bj=3>kST|-I8E{#8hm)K7)W%Xe3lEK9(h0+3O4^eYP_?O|x(lys2}G-S82spa5BJT=6)mw<bvZZ5nj!joV`kO6`L6rpkBR^MqNx4nGZEh0@4k(>IFbxnNLQTlVwG<$_rzhvJ}!P+?Sb!Far+G|vAh)X@#bLCjM`#ZrYdjTQA4mw$=9RU!93pp&pa)&omN*an=Ok_4^=P?*1Rk;98u)Ft7vUAUz3wB+<O4TIM1RlyvY&FjpCTHEbCLj_;rcpv7h4p4|cByI}$o%Evni$0h2I-KZ%zZDdgW2zboOz5lQwaNE%5G0jd*sfSos34bB^>l98v;ax6HDK)z|nN>F%=0+enryg9}Ps$JsQMp3CuWYwkO@|UEe_J96_RaIC>rh~+@3M&gaL_D?n$|f&7Z->Y5)G1ALEp2_qC&<lac}G@)wtDf(R<A00_ZN11^YY5-N2<IM|3B-z8&*5tJR?^&Zuqv8udNq7*QUaG#%%1lUN&0nzg)*R`mB@It#z)+KTKx`^95bringXBm%U-sO*v_Wq@(`|wjL#omPBx2FbJB9C(coT7cpIGIylsF=V641>!IlvSAXWsVSks8Sw|zjw0@CETMK*>B=cBgwqe#t;+q&SC5zZ{5pU)G?TU#Ox4Gl0?Z*`sL07&hFSHJvGmUv)STg462p>mtaNu^?xw!_mS7xj|YyF}!4R15`g*t~FhgX$qN{jcED+HQNg^K>z&ErwYMk^KlR93#oN0%_xf08c$E7k7-6kY#-dBNPtbG*4nF>fza$r=-W*j3Ur&lCT{fxs+<>ACyw2s>``t4b=+fs&tjciuC5ULUYx9z>vn`lY|a(jwF1Y8bG7?E*_xj*_3iexMZAkb;#r(3=6_;w>`;D`!Hq+@)|&D;ZDZBmDOx?07|9%RAl26?4fEWuWh%FjMU~9P&5b55UL^Y0!96F2L*zG#Ea$i4+h;n970(E<uk1&>YkiOl04va61zXrEBz>_N`UXFZkOZqeMpi(DPQ5AsFT5v_ux64w_C4G^+4SD@qIoV%tM~TqUb*L39RW%u_>6Hy#snICi59D%>VoNl^Mfv3ObvWt9}`OYIi>6N&U%AaYW>t*_K>gFN!&hy;2`zCjCN_)r4}b6!V7#|;c~I_9mc#cpL3%&oVHK&eeSD5D*2ek9hr|MgP_YfY8h^UPgpEXQYpwOX~?3t4!WN)sSfI%a#eV=@sRE=6iE7;|BC)llJ9y%IgNI9yuClvy5N0GAL2*Lvj^rT|?dTLJ7~`rLQ;**2VrQnw}eB3-TMf{a!!IBAaBZkuBtm%K{ej-9dghq&-@X+Euw3$qIDmycJa+!pueR;3)n)ba5kW$=h?SN^@DpD}N%rd>E-(FYE17UgsA8+O>{JaS3G(lAup7O5^zguuXf0eD~TyuN5%k2TJ3<o$^}E;Nll&&x&azZNkU)Ua3%Ow#$U(>^(O+c!MG@y(=@vjXX&Wl~WQILH88U0d%1p`0J@j(f2*kT4vq4BSNgm3;|Ga4!)04k!1FxdtbO9=E+M)(<X5Hh<Zle#?e^fJOaRa{ExOVSCOh+#$ndh2eD8C!9!FE#s;RZ!LcHlO3*sT4HN<Dp)&evu<G=Mqai&SjSCi%@9+y-eF=Xs<>;eob_mmYZ;|=q|iNrmdO;ikwaMYtATy02*~f4+j7O_8)G9M-C;&p<%n<qtj9{WwDk$A$s`cV!LDi}?E&%3p&~%EENdhG+m8vP=2E=SqS$c(Qd96W5svSMr%^4kKxzz@C>5)Qb^kC669})-Y+Nf$7%_?7X2OdG)|!*&_F8p;cohR{XB!IJ_tS=vNOcC0D5a~Py0Hv|l}Jq{;;e0sY4EsO{YYUC|IUv_uyDZ%4jpqSRr~6?6C8sDx@$H^9kX5dzBT>?FH6(6HkSRRks{2;Zw8jNua<A&wt517xIo9|Jyc#|ESc=hg-e|=Aa}Z|7QS!Ki5m9B^7&H8Ft>iY<)l`OG=6BJhF>#Pm<?8rykR6uIQTbUYfwEU<Z;$g4JU6xS$izfET3T=mJM1<#_2#ZHWgedPWpgpc?rXCVQ(ujfaqN&t(RLfis(&ti8YlwIHGS2qz~Pfy*Nq~1peH#XYkIW$-OXH%ZqVkempQiyT@0^JJn8-2rz>z&ApL2_tJg2muw8ypszdJexM@CUJnF`Dv63%5qiUW;Rj8RZgV#kFg6eks8Dp<V{sIvDc^_?{U&7hFHH5_Z@Bj1Of)eh=KUYJ5;Do!BL1p6U0q%>ADCQ{bz-Cm2!}cr=X=94Az75W(kgE{W!;9po+p}nnZ?~>D()!vxZ2{ck0>wVB=<Yq$}JZ-GgZr@Xl40sB;Qd6_77X6bys4QDPxoT-KN^Le%MW>fBbGF2l_RKu4J`tm`4bxWR0PL-$^Zoo#c*B??0^mvRnN^H9WeS9*UUI@+15OSy)G|p9()l>AmOu<dFZd%FS;7?h!f9PIBS*Ex&jC2t%x`vmbwFSM{tbL1Um>Z_9L7yUYJJ+$~pdg}HdbE#-1%*ArMO#yjY;_=?r(wcX+}f*s?#dyC}A_j;-|PH%HVEDIn9%YPsrVhDXVx6-e_H}kxK5p`U~(xC*>Ov^3;>Dv-TbKOhZiVVjw)yv?yHHKDD<jf@~aXXtg5G}<iT3c`!jn&9zdF__kDR_ph=uF6{X60uJn@0?&EKFN#b(Hlt7UFB1oQ<3VOQ1P&4lJ@1+%coS)5tlGHFnF*Ek=I*>o4BTv_Ki3msQvudl!zone?pP47V~nJqM@RdfLQLvBLH-wFy}C6VLZ}2NTciV7Pth#<Dn~-^KQ&X6C$`I{h6*q(D8WmfM#&YkqEAx_f^&?piK2d@Ng*J78jPQ-AAY>{ps#5VX_%ir~hl`<3@dNs*D>a?8>@la(@O0nCXh=U6H2#7Z%bP(iDnAf|+4R*ExL3S+iHOli22X<2BOii7qjNqiLaLy@B<K1w~~qtwsfquea`D7H-rA9IiL`&XypuckOh#O5S7$0s`~&Y6!X<c6ORolAz9WckW373Y}Qs4Ekl3tv%X(pwrNs9sCjrB&BhVC$wj@>Q)#lIDaR@T^k_5!w1um1Z!BJ$Vp(2M{9E%zV{gJ|D}$=s_!+I**0s2&j<CoNaNbHJAGlI27ny@uPO7_-kiWCi7;Z!;BLjioWDGb6dvm<R|>VjN7fSqd7okg$wf?w*q(EUQl0>K^5kaH)0o8CP)yu8|X9vNj>BqD7j66eJJEd^WCz1%mSh|6Ve{q<PE_sOx^a%Ei$g}C_1^nvlYH*N^)0xXAq<OoHu-N$5Uw!VFe|fiso<wF9tnf&)W%ZM=-1|tUnk=IPp^Vdb27mbC(Y`nuZd7+lMNZvoSeO1xd+A{x3foAd-HDp?iPSfTjhvt89j>B2oJ?ygN*+EgMFK0@`PzT1J2}`VoQSIx`-Ez}AsAe=&}O94kT_r7VPg(MDC&yzoLjGF7E!PR<GeO{}+CErKWU$VEhkr>dL_lMPx6p+Qb`vKr8qZF*-Sz^BfB{oSwBB|8R`pEmo|Qg-T6scaeJw2K($sq9xNm3d~r(pV=WGioZ5O`Mey<2*C<HHR?OGYC^GX|P~5vvy2?y`*NgQuZq^sVMCG;d%nB_P6neG6D7<y#r4r99*4m`o{WQ&04qVz1&o{M3mLA(&e;RVY=t8!HA$qNg$5%)WJnP(F%2-FDmvy!Xq+2-(VGG35R=|n<%eX<V<R(L<4*U5`n^jA3@Z^zKJYNOK}_&{rDB!&d4*QC#JubS{m_Bs^N+6Vnzfim=(VWlg^Ij?-3&VuNXGi0^$ktD*#Lpfr7<9(s3BR<*V5nL)3}K$q!aiH6nkHazETmVZLKnt&MfySg9-Xj*rQ#W^WiY$BpJkTyyT2J^L4K;lF#eJN;O8r~ch6pkDv`&hA;S|9!RNeKp#AZQ)ld(^o6gS1Z$3E7Mmi(^o6gS1Z$>I4jeS`}_Uam&zV;{46X~FPWGw=|}nJUd+8{uBFTxC;kA6fOKsYJ9M?W=C{kcv?=HDbEip9hSt;GrT&6<=}=APkw@O8sap7q);!xFIPnwSrBz*hMf=jZ7v`}8t6V&X%f_XtfU*3s_b2m7r_Q7N)7nZd9x2$ca4q#uxt7i^o~R`{s+D`3-NNKoT34ai^&MaQNeh!dbN0&dMA#L>=twFgSrFT0ddF_ZpTC!dQ|ZE{bT9|jCk;wxA3r_p*r1eHx5^Ak@dU-|u?poJkRzQHx!CHRxg%-iCYQ&#@8cB@MOXYjEu>spV7l^OUl+{pRin)-e>yhc4As%6rWfw`#S=cD=gc6dyK`loy5dpl%Y^^Ji@$Whi~cHD#L1uhnGYUav%h*r%fD8!y6#sxS&I7eCZm<T@5gsWN6h(Q*G@Gv)O^vsSQEL@CyySkf9lD;(6n`Y^ZAW@-F(#Ep_aztop7$TPaADvm^wQ3UN9mZf3tM8td#t>AK8(xjc%;my_*H;_JdlG#=^ut<3-3CVw9}m91|iV!U<32YvNks<U-i8EWDbTkB%0E?Fzu7u?W1O8ozJ`=~5ARavn6>!S++}C4W12pE|kpJ;PK&z2^Y5ksHB*#2ntRL#+ma+j`cya!?55o-{t#0FSobx2T|#N8L{X%k7$Im)`7q+E@)Y3<Uy8l=-6xMqfeUpmZj7d>{xK)&+)H85&*ctI1HXA>F$g|Mg#zdQTS)n%Pi5ay8=0BY128x0@qHCAF3>p?d(0sniQ$hOhW(UZkIXP}-9sWu4mr2zi4A@2H9j%~{ZD0^J<^u#(LX6)Yh*LdsY4bqslsDQ*dNX6cCX-pQzokQ5-CDw*gh&hgjZ(eh$_Zm74QSYI6KH7y`$-*BEgbvoKtgn||Bl#Tf~8||Y6Ng41BsUNxJ%s|oxybvQCa&d+jnGg6uiVJ1fCrK|H4R{)dI56L)0pA-4j5ZxkvI;~BR7JDr$bWREpn!gXNw9XZm~cV~!|b5O^l;}5X9^e6<~+!-KLZ8vTTTJZr<wvT!NQ93@B_UIzO9Z{wgQi4GMqb0{ES`);AKe0mM$r|;qTx<BWzYQMuuz<3VMvYft`Zo1HX%NfozB2Q4By8ym(__rhLI~hox|kW|jfMcG&mlBSSKSVySPi|5o%s#+RC=#;zC+Z-oY=MKBSAMudyTBFQUDpskUq6ODI)F?)xFMsCKshT)#VVHLKL=>f<Ocq%=*{CLxyDZF`R1=4|ck>B}y9|{(RmHZ+G=e%v<WnrPVJ4WAhqpA@1EWRpge3w;)BrH9b6v~~YiP!XmsPFkaF`*N+G*^^_S__*-!Ip(`+8M3bqN5;03{gZf%#l0sIkmJ_3SEHY)bFYxv;d9%P-!aszpo&TSCGalmf-cjuLJ+Jg<o6v6|M2qfBidr{1veA3fOoBY`g+CUI81gfQ?tc#)|<PCqE}R4a<V)r#68d@0bH)G2BFa1=T>NNS>#iX}eKG(xk{8i|c(=B$YwQRkhvC>hCHsKMmdph8(bJ^)Y_KO7JSv&wtxFiQI5wAwCr>$65w67eN}-#5;cH2*u&f0XgP}A(J#aiQQ3J9HU#C-<K<5s^c|`-{p!1jVsI^y)y?$xFd|j+Vszv@^W)%hmLga_;;zE+kYpdN1VeUTuHyr03NfOGNgxYHq37G=^HFVZ)~O6t?5q9E?&3U8t5eoDB+eE50lXw->eEFwDKo6ZpTk2nII_B`*x3h#Jw;#T~Ht4q!*Qs7`VbsH#^?rc-K=07FJ}$U>I11h!I(~GgTRxbEQMQ8_zt4h^T<B>iPWl6%d8}9^ne-@eKY5t#J%;I0BZ$C!igbnb$8dDzi6BS6>`(bmVoo$Th6UlSTilcY5srw>aR+Ej$6XiL;X|4x>=>1<;5;#!j67>(MbIbmXXej0YU`rDFg?0XbB00+5V<b#B6zxEVU4a%X@LZU%%nx_~Pfr{jBH07Cqe$6v#Tg!7OpKf5sR&bRp~K4<K8YAD=hoEl*SXi<n9T*`Ul_}QSof+TTAU=sJli{)>>O!of;D@WZp|FyHVs8Wb(E_-S&gojvwUoCWQcB7kSS`xtXo41quTi3d_ITE&^ALzis6zI5ID<X?YYnr~f;#covUtdv^J){mIF)gFz9T5hN%E+i2v(8kb^n|)TR0q6#fLdw^=-?nfQ>pVqncN?o;TY;Qsy;06TiqxH3l@X}h?J`uf@IYK^mAo(+0F_@QWV)iU8Jo{p{L1hyM`-VYp!q<JXv$1Z7OKr{pt7lxNi8Y9FZw$Ar(bTqKpq{r4?pRjK_x!9}#q|0c~K(boS8l0R;O{9*Wid{1x5uiTU!l0?kHf<&YoCuC`}I05UYD>_J6bPRFO@Po5ImdSzNK0DkNdAJryE1d8<ZSbF&!`MVZHWRr^8RjOSE_?^N4F89epI{zHDxy^s`gFJ_^YzwF~ON^8rm`uxKc?dV5_T>q*Y<}XdrYE2=1NUJlCMdFs+qu1!vuY(rY=90fHM%%jHVnp44zC&W#md}rAU}mMkWfnJXz8XA(ii^<8zi-)g0usH42%Xzev)y=cycx{y75s^ATq%}q+0E-4u*gBJwJr`tks@t_1n_q+j)1#^|mtfjj|A{hDA$TGxuP_lioi{p{?1uYfK1_+|{u~ee7uoNI1knPU;bOi6Qse$EqI<bTMgENsYvbrC$TWv;Sj1{tdH*=EKxBw^(_sc`8>=Ed(*~sT(N`k!M`GLSiYX*^~acAL|B#@Mn_x1^=4r+?g={)#GaPS=I3Cx`6JL0vl`v0m{6HhTr&64H95YI%~h6Ai?H53lh>4A=sS9AR$zyub$_;=IoruzBo>JNl`)6!o%4P_EI+0)lW`!Et|Z*FxCBukG<}ncG+jH`>}N2vg$PS3Oen?Fm>ss9^4SqQq%SZUAfhAZ$62BHvBs(uJpILjk&n5y<c%br*%C3It_o}aC1E1Z#?C>@`6f)*Z#}uPd-=h_xq6OX`xIAso$Y;s}P1;X;aFd2QT8_+s;d1odBbS*zVb%+*$k9P(J66Pe3*L%Jv`-0cs0`eEdl7?>o7z2bdsxKirVKLJS)Ka&X7Zog6U`K(}}PpjiYrgk*z1AP)Od?l2FC!|<m^LRw{!mS7=Ea4j<*jrUsw%qxdz%M34}#TL@v|4>Srm^m&eX$JEhd%lcjqKu|r%4l|ybZXfQ5Vt=gqlwFyNlZn`lM#`{kx#|`k^`E#g;G*87162WO;vLgowDtjG-YGn2TYbhu~-I4gDM=`0gTAEGoGR84DzigY&IsZ8Hh|>Nn4Y#T9Uk`r*!65Q`i*3%}H|mhe~AgSDrQa^Bvp)#~mI4V_oOow5HTt?uQ#rqVSHO1>BtgkA|S_4`waf5?9`+$=SeZ@TtS6nj60%c>uk}o1h?O{~LerfGh8bl<n>~ZxOHxD`MbEEf<$4>7L`lLRZ8jS_dM~*Z#2%5<UYCJ+DA(%r&vhHS$IjQc}2HvmvK!x<ii$+dC@r6UGP@+m0mzvwID|TIb(8+=~Yy78kH+=HH&?g0H{pqGf}h7r0{+wl5g`d8WwIvaMKB&rPh#&c=Kk$GnAIk}YL)omY#-hI(C@1)#V8(w#eU0gH$bPDe5dH>r%|_IM1Ne<?*sW4|1n6(Oh%EOa(yWTKt-HX0j^#v80^HV$1ytZx~L(T3kjt}Zpe!Hou9ETKhh+3|Hg=RfnZ#qgmrHCY)2xsZ1%TQ{lkg&S)83-^1=PFAb)F;>d2ZvCTf6w=emk6YOwmKS&k2{T6M{O3HlcC;ow;IqoLrTa=sjt5c;XgffHMm~~i{G^JQ+T*}wt>=>Hb|z<9><%DVMhU&V0MTzD$6){Jvs&c_IBT&F;Fh@pH6}g6<1N*>FS>dg@=OBLm^N=sg7^iAmeknAM=EV69#i{-SP3I=a9VT7YiPM)C-Av#0rkc;&`-VYgAC3)eMRyFS;O(GX?Q>j`L`y76~ZfTAFQjoA!0rl$*QgR5fY-)A-6c3<M4WbBw_w|+u>9ZLV5^o8xTsW-25122?p&AR*W3IQ9+mq8yetXgyar7;3HK_JN5>g7&>+5ljL6gZ(pUkoa4A`p+$K?h?3icQ-VuCSRQ1Db2Lks`gz%6Y-nahg}gbb#f_e$^~7kwpiX48RC7iPZN*#WR6Klu#uyjQiqz0EB1_9?xd<9BSS<ZH3QMWQ`Wmi}GYZQ&{t9S4Rb3a_%EsS`wZ%=#DlN3pn?r~r`aDnsayd(28}fbkyWq|wE*>Fp;732yENqAB4F!Q$WCsi_9@<a)_y==;&EtfV;J~dL{ovfnyHx|x%eKa#UgzjFhM|rFhozo;?gBqGb^(brvlryvlXrppT^?+aBF0e`PWcfJ6pDQd<BXvCnYcS|8x~dE!qyg)h2#hH91>8xe;Z&nh9W4dZEy2QYTq`6E9dfFEztj(ZmO!Ja$kcKW*+}e&Qm-ydqLmim=ih$Tyw}8q4QVXD&!7=f?mx{q^3J`FH+txJVLC|bl4?CuexIhW^s$4oW@mwEF~^|PByz6X9u(fLc+qu>*Rhk`frtxH4poq(`B9@cFaTPQ*FV;z>5^e?J^U#P{BrzOw2s82+bIRvrk*9wjd8eLK4#icJN%@68TsS?mfQkVJI$2O;3mKd>h>9hCjeUtGU?%Ur_xFyEA;AIe|Z5-Gj486W!XwThKGB<Jct}T@({%_1wMkO?}r_Yl@q`)nv*JE@}pPtcOj+p<oTP>Cc0MwgUK+kRo|Wc}v~#yezyeju2}~N#{F#TbT)KJB6(L#t#v={*Cv)yE@Iwh`zV<j>reBq6_m}^a(w%ZoyyloiPN_$8*%t9lI4+$fe1&Ei58+LpE(beLYNjtTZ}an$&}F!{U*c@6w7@aair;cbl(a+)+(F1zi~gv%Qqf#dH2pJl;i3b%t66!3_eneF@Ye=jWJ5#Hy4UaAa@?NvoRKs--BXKK~>o$bE83&~LwZjlLAj=XW+UhZ0XA_{JPcR<)F(pIV~<fT_}qY3{?!h5$0r7RjTVu(g(yQ}i8$U{Rjmeoig7sW8yBvNeHo6p)YzL0Jodn=ihn2q+UWla40BJtr3@8x6^gQ+pTw%O`6zmVG%JusW62Gg9e*;6DZH7mx<VW{Y9`tRv_i7t8c-z0$W{c}K6Djo1Iaw(x5Uzqarzv+Grd_m$T5lT1B&<#fGrx?VY5KUthEdNe(klvSN$f{kxhFXM?_;CGqb?+f`|wl-0S=$S;X8OzHN6g3jPd?hP)06GX=2+S@Z=Mug0<VYmQ6frDhd4rqNx~_1#jtO0zutvu}mhKkMsvO`qZbrXZ=;}_Ytf%kH=~!_z^j;jZl;T}}+%1S(m0Mi@5n*hh^GoSW)#H7fvEX))Nvgb?H=zB=jkF&(@t2mj>Dw9G%`Mwuq+k_8ySdWtoU&ETNJ{vM@gifnlC`7X@Pbu!dcntf!TwYq**kZ>iB22;_`k<gu28r)CccJmhQr@nKiAKNbmyF?YDSzmqYdg$cu-5S(@5GmA|{>X|2+3k>HJ|&OYY9NI;T3S#&Jr=e>(o}%dh{dXyBe@lwFj*b=MSK7jL%DP`q^)HCRip@W*T=cTL%LPRMzt;A~h3yq>3}y;Q_@`s>&x@r1}U@}|x;sm%lD4zTTW`O~85TovMRdmgpb{J-VKkACYXENcmG-0wP7U(*kuNSE$7obyTcC?+OnKLekjYhpqrIZ*g7rXg|>b5wndfQKZmt81!|qJn@*9cSerK|o#0xBz+q^!Sc1*9g?+0LUtA{eYVyaEpx)43uXw=0lNr6nsxcrJZcgh24=OcI1x_^4v?D+c2e}K!6F}RvsV{_$N>5t101oDS%=XakQalT;K(k0Xx@bbV3w@DT;f+LfG+H;=)vl2_Kj7h2~nP&vI!BqZTpCSl+2H=3`|`0g-|8l>r1NFZFWF$~(p_x=ng2^GL51hN8`iW#sXT69Q&!%`#hFqPG>Se3v4c@GZv@H!n#5v+>Nfrr}lS2t<)lII1jir{~3o@tnZUgvY3cLiK*U@`D3(N9_>D<AYsEVDDkG1+n8<WS0Bl@gm6&j`Ge{m;;3=2m*<Zz)P7ziN4&aWB0JNQ7~U`0<;DQE!bb&^7N(X!aM%{^8fx&pj&jmYAOqlHDO{ITJJV#SrGOi%>|-c-=`qJH*mM!wQE*xSy&?~4|v(GmaHTnV6Zl3bSzLLFa(H-0+F!!Y^_=jmAg3%S3AaNpDIj1;t3S*3MU2odcUX@N20#?B`9Qu(b^(X?YE$B(+Ir{qtN7e-0eBVNmdCB$w6NLA|#Bnt}q|d14NBOumWNnd7L8e^D9!Q8e+l3m@m$-l>p(S77_<o%N*9<tbkJiYzH4l#%+b_ZqP(UCL(@+4wqQW1REf7TrUKpVVW^^-!dYThO&|%c><_AT+&;XscS+X>Qav8uJ5Rre67yxu3;uz{I{y#b3<;PA5fh2O$i700Cx{qEn-@e$@YkEe%xb9s$*Q`iF*e(a{!g$TwXz9`T!YH%)JM9UzvO?p$n+u541zg-TMZirG2*Le1S=gAljaftML&34AeOO0$!+Yh~{6Bn|>!uk-+<$H1oeN^T~Gvb<?f25gS#plP|3DmYU_PX>%#S7|L%-H#HyElr9fsz(52<W4KWkt}CL~(M!AN(f~@7!%3XJI?|&yw%9AyfI<QW0~K2@;!Ds3iV3L2CDj}>fx5hA3%jN|14fmptzx11qt)+nS<gQ|2f6ulL+r!>EW|+&fj%^qVAc5VUQ0P2<4_U?Xwc7)VHjdHtb>Nu2HXw^!6&Y0q<~ZeKtdoGfCH!rd-UCi&d`%2aChKz5C}UNj1-iAKSaz;k;prU4iB!biT&VolV3pdyLI&rIDkDJY`QIQRR<Q`n@7S_?rhlSf!)*$U>qPH;lT6MLBkjXwLO?tt?m4rS;_pZ4>f7e&A5-465g%qg5r5EWC=9a5np0KmT1qAC8P+<t}|M4li_n=au(Q7qP@YLqee8P>z`nGo|>E|S8hVDIp1N#0`!hX4wR=hTu&ZSJy2rLB1Pmgt}c@zMn&*o*z6f8BIJ4aBhw+`Klyz4cjAx_d58k?9fm_NWp0V@Y|sI6BYl?Fhb`c*yQ*kxZvf<;klPQ)lR(>f12`1r_CfEGJx@F^`YBR4k7Y|9AFxtw1pMZtx+%P+U0KW%T?tygIp`@pU<LtSiq{}AU%X@Q`%`%w_S%f(=kXcG<N=!XDa8$jXPyc0lgCABI3{y5-0}tciG07~E%!1FjDOG}q?i%7>BzsgTxA)L;{1CeM!8=OYfdsA6r9|d_Pnk<YM|jCfga8CLtI&^FHtBaH3V96w#4wO!I|9GKsdF6qxMV_=94r)IS$&$BsA~}ea?48m4j4AW?tY)00<|4%&72@yzk0U;vJJv<a|*Fj=h?m^#lu&72@kH?8Jc#4FIBhhAcR73;%QcqnrSiR)|hCvnFrY<bh3|Tl$b&9r!uUet9Ov4llX~rZ3s#!f~R>Z@>@;rLj9ElR7p)Z1`rLyl>eF0{E<G^-cg;KA8jBelyMzt?rwiU<tqL9?ztcHUW3=c$08r{mb(k5%Kf~12C+jv%B*}zK6~VoQROjrtLZdTOe{*Xc)As<OzVT^;-2KwaCqUov~)9$%plvuVo<N_^fJTk+FHH=<LphW#)_%V4i`o#6_a=2uK5(5@5C(vlH1uoS%cfkyipdG5ZA)>Q(qhp1WfQdOQyjV1Vhlak5<>FoaystuI<5?BXmn&8L*-_+3}_V?hoR%vggmMGQ0H;^Q8kEMZM3V0Qe13^<e)Zm^We^@?&G=$!xu$3^};aSu=QAu}Z27wssnlf(&A8VSh3BvB7EKgLDF7&&Nn7pLFYxLS%>GFbuCP)%YA@+yqF>39=o8MRu%xUugEDVJ!Mi4$paIDTXKNcn8>iYpuDq6Nc!xVIfF*KJN8l^d0?d^k2JDtrF%m~ujIm*H(cTsFzm2geh7?`9t)bXNzr;~sc+*vc(LyX=G|onhPWS^mQI=i{!Jqzo+$b!A@>#xG@3U{^N$Zp@yPmds65Cqt6!__7SCw}kR_CCeAWFkWh`Y;PI`4%KhVr|e4RB90nNBek~*h1bC*9kW#D6ntjhQ7Qpg!Q~NooY4J?7rZ?%u;M)jZXO@sDaIaotK{kJ@lXhix$7Me!3;!aU`fBX@=ovko?&)WV#&enqm|9hgR!ahtd(Kyz2g=^%qnU#Z0MX3@68&7$a=if-cCsG$u1BxFrwJ-VEZ%3y4>R{u#x5!dWDaORuB=i56nKml_)TT5t)&jFg`3~G49CUJXE8JWK=r*f468n$3R~^+iB<aLIl1=SbEWECr{DhQP*zcU8-g?5$CdoyZG~#J2wQ)OuiTL;UH@l<RIeB3x417N#buftW)jiy471Lu@1(@SA33TF3^E1*#W)6a^xl8-m&A6)T}$_#uX~#LRe)c<n^($3&0-8CQ8n#YtdAA@l29{WDvK0MIo7*Ur~!C;%)NcybYr%MfiCzns1MDjQs7|+?)gDp!4A2Hp&ZNo3s*N+R&ktyMq;1@Ey_mt4p!^U{x!I=mmh?qusi(_3-*5#_j(Kw%oZHe!dz$<JkTtlOg&6_cgb493HF0pYG0W0{ZN*A?+|XP+pM-9FrP%Q{z*4C+nCGCglo!|B*~0EWk>-tP!M03?R32+q3tP$M_lBpnmXef?Jl-%APDv?BN+}JZ{0R%0IUizC${XYch*E4{BJFW)ua3_KY0z6T5+ei9g_+nj@g%lB8i&a~ql)9?@3ShibDCKg6%M`LB*F$9xxfXZIkw7Q59AvI$#pum0jIWd0R0{|bhE{qJiFzqase3%^3<Um^3akoi~0{3~Ss6*B({ng4Nz%#VO~ROi!6Q1kBGo3Xs8Kbb4a_*voQD_0#u=ED(Wp7?sV^M-Whb)h1z(nQasB=V_Dc)3V0XTi%C$B!9+`Xk}x_a}Jys|F~iNcpor`8M5{Af030mu4>0WfuhcsNJ>r5&oqUc52o{H$pH5m4m7aQ1m&neng;`Td?c&%PX8f{ZHcM(=pI~LLnvt%j-p4VE>NoNM`St7m4ol^mldEh{P{lNZj0$rMQrs;OPCyF^kvEhWYI4sOuC_<N!#BDN`etoW<9l*pAHc(Z?|Jb3P+SknqvuVh*=|{_l4K*ZZgN^~WX-ZUWt3a@m-G>X$F|3RvF1CjkD8rf>~t|6FMK3Ech^Fn$CTpQGkaf%c~e@uSa<|2>Omzv$a?^8TFtP@OyAJT$(5+^>A&b#VPPWW6sY9kU_B3e+)h-kn0}V>L(F&oK345%u)V^0TNA>>aCGC=XmJX{qkM)a^meeJ~K`QEe;Tl)_eJeg#mT9L1wG@dQ;~=&V8oc2%iZwwLidzCwkPFspC{R<Ha9rtcIt7O05Nd|um9VcXkc?p&#l61$LRtFEX?QSo`sk*f+8vou(d^aKQsA%O-2WtIW<VBuNFG}llmC`^?vCzK3|NrsyDwSn=i60ZUXQDMZ4u^w|%CLTxVnk!`~e6Y4sH2g9MQEQ9PkX9s=a}=ET2`z5-;$>HlW?0$xnhn>qDmr^)uC#_zF&|hSYP3Nit{N@5G)ih!=vf?eETvK4&95X?R97m!`5B|a0i%R)DX<yGf?7WIAbc$fQ9czyqdi1FLf}l2wxvpZfxUdBvRe3RD%LFx0G`BVj%a!cx3<C6(RGsPKLTcYNU9p3zGpZhY-Ud!=!nX6MB;S>zm*kylCY*OtLso-6Tqt;Rih)YlSE|}JSK|0mGH(8RwKc~AeqG2Ba(|FQXb<KKt3&&<Y5q%S@4+7AX;ID#}v@kx$@dUT~NTxumEOKM6u4Jfv1vwrzvWA$u^?=8;UU@JKZ2$Jj?GI)lov`qu~KvZ8Q#U)r+Y}xC$o9HV16>^CIv}lr4N}Q8xEKToq-zfLhoAn|-El4ldM}Q47Q}ZEEvo=-fj3?--`AH9wkBoh{9$Z(0MjaS~B&d4@J&VIZf%G};<gog0>UH3ipzM*tsu27JJ00z|iv2X&EEjgnRMTBq}9XxO*B@V<k@RS7acm`mP8u$k0&)xq+v$q8b}xmDPLhWitMc!3KHO+Me$n|dn87rq!S_^Qw!aH*fNH~raXL5IFgiBA{5o*(sNkajqQ&x5}!0?O7}A#Jfb06GL@kQrY1Y5R+TN-z;}A=_dQ6c3ilYR%qL=0faf_c*K<K1jN&{7AYNB-Zb6s?hHZxxL|hBqzyyp8AfRiz3Iks#{_msb~%}i91rtDueC`_cRz5Dd-u74WRuI*a#kTD-0YyxDw%L&$!Z47X6my2;OelAWr<Nr$RjJC~obq9fZ1#yTslT;_u|)T_=}*hS<ftrhJX~3=mfga=Fhxi6Vkc)vZEYmj(tv7i51qYC^Cc%LI38E$yz1astS5*kS;H-1unf*#o$g9Q*@Mh`T_mJaUE~R>806XJW;q(6@Zft%(oF2ufek=Wu3k^d_;nhbXA5h;RfYMpOR=$x}@SBq3j5QN!k@=f_(i<-|9s;$8;>oXr=}kdTS7OWOIm<puZ9N6c5a^_GAGpM;A~-11LE{nvTch;+IDw*U_(Zn$MdY(yj{d3(9Hw+;JygEO?f;Y;%~tP?f#^F{oT1s5hyxqacn2rwISupkUM`c^Ze!?b%S3=diu^Wk4q+gNRPxa78GiXnG_wQ*sRD|*(7bcqLyW@YC0u^I;OT)G|8SDaxYAvUW6r`G)Dy&%6tJ^^=6aa7J-H7!7T&DaCmV}Rm2J_Ud_4r{l>!vm-1dT?*6xT`o<6X&?9L}dl?I8+*4>ECz{W;R-~)|%a)GP4;YstaZ|O);~Hql;Q?CU*YF#IC7y663QlU6Xh+z_8N7lnE1dk_t7*Rp`eJo<lLQ%h!pB2V+T=HXQ`x;U7dUVxn~o=H7fW8$>X%0kZuL8yxOAHdS9s?LQAO&L=y%2>HoHC>0kWV7C6$2Wj|Au63uae(G8`(TR%jm08v?${n;3JaG)n=N{(njwKXmi(O!C^VQ7PkyD&m2$6`H#2Bz3C2-7uf|Enf6|;nV2rw1OQ|rbzWFYyICik-@Z<b9CTEov&f9z$>3itF}Y~-(yhZI`**jyq1tkBI`I#QAPM#5pSs!lgR;Ozlu<bMyI`v)RtAMpO8gzIxt?a+ILdmMCd{=;oG7$=la`y0We5%zq}-AmHifWvsse9S%0@Y8tBKOOKVuRrY(VR`O1zQEL6#cd^tWlowQZAfPj$JYDJAHGgEXpZOxEtxr-QeA#sbCXTpMCy0|-Y1hePw$}LaUbLs-sfTmsFq@cf5KqNq6DeJL-!Zcr!?e6ItWDrAUDa^wD)C)Pk!w7VjS>`fR;3zKPnB48~F=dSEO2Qdm><<o5BfZ>|2w$kdN$yx_8r0A|pt^bc0;y!)n`Gxw6}Wjy<Cx`jnE-E((C35+q}Rq%ecMayf*l&+zKL93M@3$P4Jnq=KKP7L23kT%j9;!nYkylBTcLMxXyBH9Sl>`I5r%qV?Es>qLw+T0b2&W;l-D@v~%EMW)tx20wkfyMVoCWoY?knzh610^B?oqQr*w4BqGl#yIe^-)>AAEx*yo-i0ha5hA=Bg%7l`E$=Km#Ky-FX0I!+ILeQk;>s^hVxj|<5F_K!eNp*;xY%Rohx7PXt7j5}RxyXJ;mg@qSw}!rypM~qh!9Jpg34ZqV?e=vW)!>)Q`?^+c`^dx<%HnLGs9@;Lm7M%-vxa?s&CSAqftT783kJ+5@OdQs7TWZTg;L^#gc6#iHAZBp8QxJ%#guMlvEMZG1f;!sUizI#_6iau!(IEhVmpZwox}uf;c_j^Y5PDq7#N0kH<wjZ6GsR;c$$F_)>n0s5Z_z(!q%H_KDiel~QZDcr#cKNuBBo<9&r#$eL+7UUjA~|J}U&4L@M4`oP|CM}hZ>35g0Dm|<KEI|#a@TN1`{YryyiEYmPf*4USbGS1&OCKTVQI|L>+7-(S!a*K6G-O5+=_+b#52H(K-)2z80o;iSbpb4F7E*b+$fQy|I%q@kZBEnaPJH!0sJ5Rj3cv&o~HQYkwi}CCN8e=iB+Nne^2NrpH;t_I;)d;2MGrP?o!6s!9S!xaMW=0c|GJ_kZ^75i*RU+{W=sa{iY4j0Gz|~Bsr9x`<#R<bR*Os?xc>Om%6ji-Jrs+5xij5Vhk9oI~jtnOlk1X^>@?N~2sOo-no1pNW8B=n1+0qRxxn)wc6bi5?&paoT6m1GsT{Lt?D7dy`&j|*ZlkEf(=QYC#tn(+%6Ahv^Th>pUCnlbHQ_`V+N{3F)6NwJj`E+{~sy$MmQEc*+EW#Ln-4P|=&)81PGn}i-8P46O%}M>#b;qG^xau3QMwlFje*Qx`4t?XQ<Is1mI1WkXqSy^Z?v4lA4dqeN6}zD*yCIqajgCWD|GE6hbf`Nq9df6pLp4r5_Z@1NzC%6wi&n-LS`Woz)1juA4%M9gWja)w=}@&%Nul@-wMC|3?mHBV?@*%e(6*jThw{Sm_Skf&l88qtrbFG#bO<IN@cx+`hnn+_Ls#vFILjmDSI0kq?}o9}vC$B2;hA1TPZ|v&e)(as82Z<$-*ff%u>(ylSMB`FAHlW?cU7OK_($5PZ7A-+I0d2zn1C6+fv}H_q4lgg1qw#E!hXBeo)9bDfZS5V?v)@Q>OO!Hn&Uw%7-1wuV!A|UClfS(>brSqi4>R#VvHkfS(T5c+Y$+KnN}k5>jCF%FhF3c@;S{D`;t}s1~-0~XI41io^NiLi_B+SRsL(iq#8(ORBoAzO1{W7WgfWd_)*j$G8$>Bn&Y@;y~*E<+cRf%umABw)frLCxmagxqf0NUGjdT(=Sz)jhW1RUv3X9ZF;TmSx<ePMjpSlCmkW+fDLA_46&%x1!7=9Lm10ourQk^Mld<OLk7|yUARn0Wo-8|FSd^{iC@0r;r}~Cf_<I%Y^MC)m^{lP)-?(DeH0w=Q%7UyUm|fE>!Rni`1<O-YqQ=Bj7Bsu2QV?Y64XIM6O<CuP=WNS-mZPg;P(d(|16uXWml%5)0Th$4ZPjtPpF4+RuT+n9Ko=V`ZE7*?BV~fG2$I;)6Gkl7Gby-gnXU^E#c&dUa#I3hEl3BYOMHiQc9rLhjafA1li#ftHj0Nsk^UoxS+YLuEuPXXC-CrFm|*`9p87gjiiD^kE(^7bEADZI+(MXa6L$n|O<g$bt*h>VFi#3`fxAlwE5m+nQ3#23fs1-pRPquRD=7{R(kVv146k!{V^1?WJ~rY#SG0sGo44v4PnAECV{0h1l-bqmul_z_V)Ozl`GN(rzp`4lHzhg`r8e~7FY<Gwp=MnPGK6N{?aV7HNrNn5m2r%!YfbE-BEuTWYF0HQ9#h}W@#t^hs0@9#Epe0*)2n-VWR~m#7v%1StFZtFBf9q2Y}n-I^@FcAY~TVtb2*z28|O^4#!-~#%&=iNtC6!i9yYNI8*kFdrIfCEb3WykQ|>fuD3-(fYldmq3``ZX9#KXP+-d`p%6V3#q#{*kIBYb@P$g@_N_kY9;v%;k0Pz;XqrLYV&PWZ5eaOkLCP(7D8Xu^tb`!CJpuTmNA3h_SUw?7i=ia|Q*Y>@n!k%n<Ee=Nxb7<3k+4gSM_KwnXR4cOuAF~$Po{=rx=8CF<HGem5AKCny%gyhn=I6C_$IX9>s;0^dPqclKhg@T_g=6z4Hvjgt`TuJ5J5w^ReyEyIl6jxcGI@D9{5Ezc>8CJ^pfwb$yF8EPiFTzDDItJ$ZZMx#LAfqT2?gfN1}w9&q}&waaV3+jtruXxe>Olv2T8T4`IXBy^L%Z<3jKhAUFAob_cB!5A<`_UOImgqA2A^dz5~IeNPQVh{16$;$KUu`ALq`WlEb<-?8hP-KrbSLz!l<8f&r*X>-T{pVamqj|Kn4!GW>PXlF1jdH7T?)(a&7lnqQ%cmoiSKR##4_412K=j0It+M6Kp|iGLFJEr|pvW3Y%`SPsJDI94I+$`T4uwa|znxIAL<1e)rBkOo}NjitP?cK!ADi8mU(nvd{CiD4@9d_=@8AxD>D)Kkb2vmzKFjw-ez<VZlc9Kv0N9K`}Tih>+5C^gj45^@yaPKy4UBeXglp^hXNg)eA0Ton2z_<Ljj(HiiG$w(&PX7Hm4d(_SqP58)CW9n=gVRch{BN<ON;k@)<doH9*pB%>a4}OfdLFW*cE{vYGUu7qR@d>0%DyZdS=%u&FCLV2r)X`?p%l10-Qq_&;Y=a8E#=Q^R<)y6TCpW`&zgqnzH~buKH@%@C=3}+`Su9n9*3w7S*~P~qT<zY*s%U@8MIqp2b>kqEO^<Xz-3ZkdN$tWh_{iRI8AT=}7{$t@XY*h8cUDzR`Y-#%J;LCMwG7Q%Sn_sk@6g)uovx7SuY3B!=U6%!hs-t$i1-vam)pTZ+j7t_Dp3`05RvG9JZEJdxH=LE6R9D4cPFVZMnL%<Z}^egM(4oG79y^Gr+_?92RBzNu0L2n&Mm9O<h4LU2*}g>4agINAa@dwCv9SngTk6Y;lYAJM&pF4To1@8{TAYX^GOtn>zXL|mnal_Dik02jB|s@I0ES6)3Q&g`9K%!Y}uy-?SR9x1T@xsq!&*hm&!h@c*0~nTI~?HGZEe_$Sd$2%EuFn<mP#)g+g&NpN;48@kpms&Bm$b?<u=0ZDKxlhqfeU)-6SfF@tkQo$q9?S(oKTzkX4ea8eHH1#hjy&rzsC_3_|-!=S6*We&M1#b1p~kFxJ0<Uy<MzMyk+|06vLiv5t(#>^0^A~+A(H!8NV8XMV_a|}e4R~c<{GW15J0Vs`)n%gHg_9KES_I?LuQ-1$J7oNWupgWCun-yKrWCu~@(T3SQw|$fzr_5!?`ID90#3M0F-)S!sg*f<Ju3bt9w?KdfX7q14Ss*yw;jp2cnP@|l7cepg>Aq?&6KpHKs#>vcsb%OTI=;hS2dpKiKZF%Ts?m`Dfky8rvWxO#5!ubnzu^;TJp_(zdnZ6@epY+pP}O_()Q)2+t%18Z5Qr^va6l9i(A_E>l`0|WCFzz{09g+Y76a?5hYnLs40g=G@T<l~&Scp<k8hl<Ig;J&Tbx$nh!WGyb0%I4Rn%6Gpf4pNMTp$;<JhMX4X9!gQF0c9LGFG{=7G1JUrm9)z7n7d&uZV|vU`rtmenat@`E}0)CB$K>+j82t<w0<2e0^%PGx0GUTA0$D?5`4Rye>Gj)qV{9Oi-6CGgXstg&L&l8Vg!?|qEfxGRhI>1-TAnXi_!F@_?>UMK_*=SnHw85!VsPUh$h-b^W$(=y}jRMqLY8s8pG%Xuc0tB2Vgl*yTEX($*aPZ&q-F*#cuo;`&l)r>uwab|WR$el09&&vgVt{TrO6gQiArrf7fYf_<-Vj5M;Jm=@6c-ZD=^X&lgQ9(}$j5!GnFD%z9Fb<2rSO_9K-wz%b|K__S2p;L);DE5gXz4K|YSsaAtWy)f<2sTV@*PArE!l-ou}+NMm=6Vh6~GZhUwIbH;dGuIY8I2Z>PoB}n<oLU9+?hcLD<NZVPhc6mO{yz>JvADo^U6btE~Aag2))L@vqpHH8cz0?uv9N{IwpuFj-)u1Yv)$1i+<gg&D+SyB_k&*kS_r9ltTp)cGs!B8S(mTE&WR7Kgkxt4CrN-I6ca=Fc+mbt6paZ~iDHv8$3utv^^2d#e4|oQy$xSOm;FX3<7$WMq%an^+Wk27fo=XId=6i+ayd@O+Ch4{q&m+Cvze|JG9@L7oB+v_~4wJ%^Q~E6h)Z&~P3gYF_O&TDRT#`T3Zgx277prOL3*^eoaZ*m+Yij<v6dHNO?rfjYb<6I`-ot!2xq#xL1<n1YnU6VNGt22I}9#P56f@YIYaJ1GLEk|9I?EyUm?W;K3P<{=c*Ne-oFc2XL_ZZxms))M|UM0jdq$ErShJ4sC6Th0{USW{D$lV`+|;SY@^C~9wj&&0HKzS%dIsC+$BdckPwMJbr0y+(VY9P%**g8%$`n+rCTxc%4Wf?D<mSLXs0r5Wlm?T|av)fqw3|JNpk_S~c(OE1W_jAh~W+N99TDqC%QYF-%Yz=PHT*Nj2U_1R&MR@y2@^w*xfR6gV3T*{@-xVvX^>DTGIII|RXm{F&=#rBxN%jd&sqIrtMYjZ?=g2CI?XX(3^NJrW<l<ee2+})xP&Kh?kb(M1|^fac>D;=B%HmM`BIbkU7mx=Tj<t0BkA3Xj$)xU?`#_)YE5MSW_fjk5(Anx<6u48>5PpgWLccVBJJK7z2wm#k+ip7DVR{F=}sB0(l0)*mx{z@|RVshXysw$eh&=*3!Fc07(kp$X5(T*i=0ZpKcEL;OiguHC#PJsiu9-nOs^ST#ZCV-VC474`t!$_=+{!2QS49qin?yfhC@YZ>RcDhITp`l0g(U9MCJpmd_=ii7X;6b+&_^cIZu!UpW9(e;^p`aZeZ?54!>IaD+<>_Sbws*`&;#@dpM^iXc0OM8*O&Tr7idpY(SN}d9T3h7E(m#$RX^lzM`9f`ipNa(8^NVjdcatA48XNl|)F$aWs?s5eZALX1nNCbTj{+b``%iA#6S48yHj6U{&9h*vyTQpAQQ#9#uqXNkSqLhAGrr|kY(tr>Fkw*z@IZ#l^xp~gtc?i+rwx&OY8~mlaI8U$EKWjvT$p`gW#}I7Y?n34=@}~_8va_ginT~F9&2?XR8ML;ow=%D!OpkS?PVo^CK@WkhiTuLXZ0;JHX9i7(Z7hIWyx4u1@4`nHu6ld1E>_yaPAaq;BNey?Vm8;$=gL?kdvKkh^A~ObpbLF%%3rda?^_7%O#cYTeDHvRN9#OVm6C5<oP>c_=7e@+(dB3ANfcP$8}0ej!<ECXminyu0a3&M;4f1P3|jcOl;p#W5TMv?R9~P$h6qm<%z*3xrWC@UZ_j3pv*m}FFHM!*Cy<77t#`1nAY=!iBCyu)A|{p!R@ClnEn2%y~4+`SMcwqI{W(HSC@)c{rT4xe*N!j3x9eKg_2l%wNZGrQTP!H9^9*w!mE?QtCPY{rjx=;+!Nm4@29L2uJ|ULcT5QG$Sz@2wK;K2xHWYNxi?FXxUK}N1D;h<J(Af9X0z;q5|m9T@JU~4;hs>{)jJv}%p4Go{0m0G|H;vy<_R~<`h}&yzDXp`-l^x3`|i|Op*lK#c0wlgjz2E2?DXQqPhsKy5GRKMWWP;cyR_Iw*}%3kd)Dc%^M<9wQFZj@@ueC@shT@J*pKv}WvMV!7p}JW4$LpOJ^oTpEKoEdpmM3RYaXp4#ydK`?8RX-Glj4;Qy8_jkNgz;#m8+xYIoFys_16_b=7E*FuTZL@<^o-9BGhF9iRwSU9wlG&e<!RSMR^-ZXgAQD-H`6Z4oXR4P5x|^unEaam{&Q=1Nc%@qFhe+XW8)3oZcR<nluGq*2191K#BpF4<eS$=>4F8{+wn3@1;#iq)k9s#zP(f6sk7MxO{@E>boPRazbsrcYI2=3;PkD!=%maPr~_vx((ji@63Fzn3f+{L_Cr+gmP<oy(`K{GtKJc2Mkn+&JM(<6LSkw{&j5{$lzqj^84i{uis?!MxNvSO1`>rpfzR=-wtCqzepm189t010}??BfDH!&YdH$nHmRPSbG>JCzh6Ks$0gMK%3qGzKvOaV^#0;)K;9*xa<#=htRA86ASe+qgtDy8wgizB^&0*LSFBxRYw-22WmD2Rh{rfy*Dd?1iUQPB9tSGTvf;Sr5=c{YgwlwpdOMF)Z9o7N@>tcWN{^I3HG2twfxP28<hNvD#+4l69~Yx(7Z&{B5=mI-?qldd&VqLdUZOIb+niSDJ9yR6*Li7BZ1K%^(3Qhx()}6Z7LZEQMlcoTj1q)Rod{8ZcXZ$czLP<4A4lcrH8~t6}8`nYHas2y!<GoMO_w_ri7YD8@2?+55miPGC+;i4-KH)enc;$xL@D+L_$(NH<&dsnC`GDQv|uE2h)XaBY=weu7)inMf0_{Dfk+ioQ~z`uNi42&~QAM=w3@&S?$G(vbbRsf?iie2NKZCrmcn+HDN`EsgjbrFUx#LJ67Vk@G8B+ihecJkgEWb&4WSh2u<i1CZ$6)M7#bCbV4g>k)qT5{yT!MzvkMXC0O2`1A(oq{wGpJ!xBN2Trq#}l#+1^-Q14F-1?~gDeP%SX!i_X9VC}H5NLg50Rd=ffu%!0R~kx!0;2s|qMed-%u$UW>!OD1Q>Z)$T(v`t(HIzuPaFEr&Qw&LAXY?8vpSmRnme?E06TaHjl`>+zxR+|r-m7^QAFPlM1ZX*ik0qI$tJF6QZnmV&CF8?rI7NO-}+_!GgMH_u1VyWz<8esoAY<7e68wD`O)nduD=%)|AO8oQD)*zTFRQ2UIw9L0Yw$zrsrV!h5M+w4&pd%eICotCq{Jjvb*g}T#uFgmOO@n=uZXF-)kBN!4zcEhVx=O7uQo6p7ac{*)?4lo|G{<W<o;y2=lg;;yid?YI<Rm(hD_3ekZvfXZ(3DthhQR-v?-b5QD;Y&6BzDt7_tp@2FnA=%EF?|K?JKKKH=^q@GXTJ>Q2m_}CL~*bP_5C{YP&TGzALjWaE!f+V`37-XE$Bt+c`(a~};_nNt?!mJ!SlteeGQD|e-2G^dSK8}<JZ$@o!_8P)-i#E8ejA=6pgXb<#j4ASAJ8pNmGuD)pBPn&I>4DSpYDFfiV1b7dZSZ|=-d}#7O|HQ|Z}NcS7xI~-)JgC10Vc#w!>#4OHoZ1eWRKR~z@40HZz!J(80QNBZo{k3!-1)UM>BBpV@vPlG8lZn0_eu##jdJb(SUu^O8)|2>>>EO8`o^Abv@y0G0eyaXd8%B$fySx%xwjbPV3^Ie4h=BHa>3P&G`n#4V6CaOx3t0u(ikxtEEl7)|y#MG<){EnZ0}PrDtOfnwmMOPv;4&k-32JO4-H)#G#p~fERr&8jLhUd*5zo$kX_{wUg3QKCGUmEHYSmwfQ_ZtEz2XcLTcR{!e_Qi6W7^7e*{OoKl3m>qh|C)MXX)P^v*wgoHlUbPXsD0%_(Tkme2o_|k=m0Gbm41T=Y~l<AKr3NJ=`cTc^We91!&|0!TYc4i(PcLzqxgXMh^TeMkM`ElLQUZh<!DE*f{;?z5D(NXf~B`umm@72?jZt=+lj|<eC4l7(zl=z^*3sOnbLv-LylWXpBY{DQ0?7@o)JDXOyd}2-|NwBov{@c~>KFed_hLV<nDn~z~&{G~NfZu}CP(wO^J2tIEuBKOtj3;Vt0TXwz*mrhNeeOsL<qvvS>qi}PuSu=(+()(mz@sflcpvn=`BO=XrTA3i6nq0}3SBpSQ4Ta<Vc-Yy-gG_OC~H%WFl2x@2qk>zjzgYoj;%xE^+l8dh>lDfe30ja+e4y?Z6xP70+!EDIr~)PP1O(_0gP5|e))i*7GM&8>IhARiZiT;D~TS|wCZR`q;I+V&zr%f$;aoF7mkht33d(9%HUQ1W7iBHnn`?$NNB=*=e7@nc|K6qHKsmyqL}v!n6Zm7=cFx9g@%q*35*EFsgciTXsgkX!Mq(3wB)|q7)Rcc=Zp&XIww$>wy{s<ZESuHD@CjIB>&^3>puE9=tz_8HWWPt*cIAV=8X`A2{k{MVBLx*lW2T2>i`M7IFe8XeUWoFGA*Jx(orcVy0Mx=7OmuEyetxoNG+9eTwq+dLmU-@EKkL4yDx%}zG!}ppIsJ}xY2i`y@Osb0~W^rmejrdZTy%FBJ8fi(mrDD_Ta6q<Sk=ADrXrJ*o{J3O9u?|E1fPW9$!*2yG^!pEcrb>%_`hacVzFBYK1FS*G7UEEhC&f>2&XL@+&`=A(YPA=;Xla!ej*C=2jBcdCJ2o&e3lCEO`zJwCw8^CLa1=o`9u&SByJA%`KusfAB9?#bkCh1Blb<1g~o;U*|}(22&x8F!58N7Qw_LTWn=SvwB?LdVFU~l1FmVE3;Sy(_$d!jxl=LcnLH2<Z-nf0r2t{cecb?`Xp2vZXl)JRFfU-M|BX9uz5xKYI6i7`eVawX(XCEw_T2KYb7wb`gxe6F^mOtn<q3)e%i(7-C`I??JQMs0mzrvBFn;|*+~tLc08>_2mPKYD${1-jX25|n<OT`$a1-ycD+P6VZ4rp2}}((d;b7bI^yKUnf-+j?Zxzk(|x|48{}j1hweOPL2!cxZF10&@3=E{f8`z60iKE)B77(Idr&^f`KCF~MEj1gbA$|`xzS@U?A4l@)G&nc+>ss2C*Oj=nS%yT;wQ_@QgYld1ooy*Lgpu1h{PoH{{f35_8r0ebXu~_G3PR0jYx?)9L!4Cs9-EkReJUUDF*7TUV#yh-xPZq<Kl?A2=a%QvP7dSR+&Vo?pA4Y3hi3T8Y@Q&i2}`CjRe`z4=A0%^h(70wUK)i>tj>2VVIgDgc=Dp(%<tZZ=m)n>Rb>#NmP~G4l6ko`<neM?)YZj!<wrY=;l47zKmFfpyPkCDd6_~q_omfnBs|iX?h;(x#UaJg)|lu499vDa(P4oyRq!mJYU*WC1k5+Dbvv%;y7z+GY%N)wb7^{-A4-Yddy*&M$i*!th7jD(GlW?N?uBPbKSa=I*_a(kYobKD3-iMy0diEFr}*`Ju;CU5AHajntJ7`&==l%r8hnWq2#|_Og$e$3Z<Wko*hY{C~0-t=~_-V?b44V1QWo2o-kEIf1$d)B!4n9BWbBGa$-i}Mpdd}=~Powf*o0*578OLkHqtti=cVMk7O=?A~lgo0fl|a-AtAw$Es9PM#~dc=jG&XP?~LUTu>U$FAY8A!EUPGRS%uoM_%=0h<9Soh5_++-@U&is0^R)FTG>ZWvMTT_5Ff>jXDdSL+LNA`P3ZSc{AuhXMv(gwMeeJAU-{cB@MQarxIo-cHZa??U8<&x(TZ+NN?8yT}ix5>iP<k=bDnzDJ#Dvl*5EpG+~`HQ`J&al0s&2sjeTb2#PgG6P7!tuJ4z2-hL@7nU=DW@7j+(8Aa~@u^zf1y6!oW0AnOgjm1=-Swqt~VE~5U0!LYPNO?@|pxws$k&}cq(+NC7m@lj*eXX?>Gup;XC{4$!8dZ3a16_E3v&;{6rZ>D9*I5!Yb9b(p5wUGJgDmb@TK4y?3?BjxTaT1Yk5Uu$anaq@<2suVWT`XKOql8dk~&dP!P>J7p-tF?(?(=iJT9_==kbzUTp?=fwKs&#m^n9_0)gavos=WWhB3@`QltDxbnWCVJ`?vvD$%O6d5koK8sv+-M=oMn_v9vYvy>vKmy5M_c~tJg#jKn*ZdPiFpQNY%UmvxbH-%cvuxN9sgL~`UgL*eJ>iM)A*uz807JYm>PR(NnXYXG2@%E^XN9)}KCw-*n)WLn}-Hf4z(!1NUy&Dk9MF)>39XuX&aOZZ<=-mSe&z)>rtEqQOq;Dav;Y7f%)<s{3GQ!XA*JuRT8TV7C-to!@YUitKOI8t6a1pRR>fmwS!B@DE4R<Nctimse?6$$wB)^FpXVys{ym$Y`vl7v{0q?6sN#OPXeMJau-B)|;&mfj19F8U(Buhg;o*4o>emnXOb0nu5zoEpQZmT1P!&hT`8uGpO(5(O#h<i7@-sT<`LbFDc@Frra68I-?otqnf;0f=zA;~A)nCm)}^51aJxHgo5p>^{$JVvL|ZIlyhzP7c0Wa?tKyxJXAIle)VQp0!bc02{_?Mfg!qJ#5{hSYTBKCAq`3agFO6A0UimZ4cZfxq-rp!aN#>v1zM7E@@Y)&^G}mHlw-rKGYAs)?YqiV#auIv6k({ntX~nAtVc`4DeNEezD0pT}{tAkM>v3}_sBtQ6xLrj#R7H#K5Fi@y}Rr7>``l+dV@5tNiBR4mVQz0|_1WsK%$F`9BwN~lv7&Lp-<jMho|d+>u&*>hn-1!#5gJV<`401ZYpR5+}y6u^pyR~Z+uqT3K{g9()-lu%VXcf4Sr@tB0l7xjmpV-mRf;V=pO-c^&pG&2cAelZ+71iqC+V55Z$DW^-Wfa%l~uvu6FcEu9V(GpOd=xxdJ&iw$lPN<9XmVkq{D@#|vSX=@7nJZvZTmf%n<mt^7P<lK^u7F)}1su3+<=0=#i~(yi2E>_DDe*c8)M8w%@ubWi@a^0lkcY`3unl(mTRMK+<+(#4aC71oSXtT3vj7H|rvzJrSqR267J?k*LMY;S`uhM!?>vaxxtAd01lb9;?_ej$UGu_GkTpn}3L4ephs9U$|9JNe_!WbP(}c~;;K5RaKl}y{RhWA`cxvEWa=WA1Oo-1jc!(zk4>FUD&#}6z3X+!Pkmj=CoeEso_FQng`_VRg_%m~3r1+2{*K@{5-*xeuA~u=pGp68iX3tYzto9pnjat8Jv2#wrN@yrwOO#k}NhkA5R(V?g5b;^)7!8<tW3Vrmgq`wqceh+#V~&`LC|^<C?kk<#+@nJ=4HIfNvU9yT_|#kG2C7&U&|6SP^b;i{ihyiJBULRacFkghc?j&D=OBHNgvOlLd}p52N)+W*c>ATlp=cYX)Eee?pFvBlTJJbxwgi$>TIuT%sEr&iNw>ZIbJZUYaf2UNOg*?koUPBHpo=LY_tQJpBm&@fT(rrC$j3YeP$PViLw>_)u!2Y%;j$jb9I9`QdQ9Ax$;f;-xMY?Yc++D;M*zL!2J>KkhN-aYI@xpNM_Al0@?Up^%lkWq>70Z$SqwZf-jO;%R;BoeVi%$Gw&$%$OHYDhWR<mcHamaE-4M!7cQD6GraZ0F!h)n5LrXOpFS{Ep)Mc6KL?jqli9T;sh<CtAaFMPE@7>bWLpSnYT(WuR&Jr_xetVrmts{^39bw{gkM|tauAvE!E4`s%``qJQc)AT6n{#+ynf4bjJX_B_i%$iGkkrPEo;wP8tqZ!*69E@mf;sri_rx0Ff@_r0qCG=1?8;MUCm;6}3cL7HuFQE%?h9kw1GEOMK<R@cGVVQ7-c{<T#z@v+H1BuSZE=s0%wu_o3EeE4!a3w(ORK3!)qj~Ghsi>%P-F~E!ih*GUsT#NPOmRG3~%#GlPI<qi9MhwFxfD;I#2!l;0)KoJE}zeZM4&<F<tj^k8k*N{wet4i1_d|7dI4&%?<MlXp-hJcMbG5boY+ipT-(~1BV-|@Q?XVE3Ee0%1|+1!d8Kb{*_a7dtb%<J$sh3-}$ib<QMlyk*E~$MgH&3%S5{=M38UZlgY!A90Jm4`HS*BeCwbP(~=#By_6~|AwzZ#_z2REcM|DGz(iV!?++D|J1p?R<Pbco)<zKn(|_<mf}S65SF4kV=h)TiiodVLJ!8;AJi`@Zt9P^b?UnUfdRsN(q~SFCr4ySobBkv=vF$!>tn=4ifan-i%P-k*w(ygflCmPB0HTriuY5Qh|5GV-mPWCDnk<=uehO0!WwA8NO=(v%_(NB<l!{3{E>+8^_b3ZtjB`?(&?{LcWL9NVeH<iQT39BehG8|a!qc(#BNd4O=W)o_E^YqWq5w%f<w&TJlhbXqE+-4el|VoQkkp<vJ|gN8D$kIAv;rx0@K?OwH_wZoKXIS>MOzf|b-jVv!@%VLt`8NkIS>t}0oYb9X!+fpFw|HYb|ec9560nm)G=GcdC@{#t`RpuMyr~llZ7uiaDr7l_9&~kx0ND91aTo1sfw@XPQCR6l!=LoVg5Db@zK~39(zFa0IAwgP__nW*<)=ABxsH<*yd^`JVs>NE+0&_aTZ;-AW%jNWQsG~ok~k)RG)j+u$5;M9h&obZYLY&SYGssO7C5P-d!B4MVZ6VeA(BQ^2B;24D89cO*e~5iUWeKpvcKx@y?KsgBYw#Xeby87d2b0!*yHY*@B7p5=X_*dRZitREeL%OZjFOVDr&(kcS!mRItimuu3dITC*BqY(s%t0#8inl^}o4z_TKYHr_aEqpz0}A0XOkYkiSU&a@Sia_G5kBH4#_L|?jz$t`awnz~4E*ozif<YL7~l7ZB8<0BWGt)UlV&81r4G?{dZLI!YS=M8UWR^)zE`t{|s3_lxPOijNvVhx?C78Bw$p#0P*9T3YMEpY&LPQ9pYhjM#dmb8+MjDIyfjecTl%}p!QAKrb$=_&mF$MCcrC5{`FAK$aSv0v&Ni<H}XAq&q)94EKv>FrYGxM9~Gg^p`7=~;zApN*^y`og62bo9tgvzmmCg-&LTCQuaKP@Bp%GR4nH5c3^!)24MCB?JyKr3Fx)SjxLn?RKS4#q;Z(sT_BoYNh)(b5|N7N&Jr>YsH;wQ^^te;<46XMMwv%YxfT-qs7%dmG&cZKEzi(kXWDK2re^8Y%V)u+Seo<1iD^*&kIlPR*{=|0z7k9QK0<oyp~F8dSgLWFO7F%dvkMsdrda7gZ%#2Rn}!kMhHU}NLQ>Q^B!%br1mXlsBhT(h+X1}UZytjp>uJY8mphZt>}2|TC({u!azMF%C#=D#zuZF=rB0AMVjIJ+`o$Evt^FocE%2#Je?9_`Ms|CdCfbG^oU%cYPt9uS4Z`+wMKYgAvS6xmr)(2)o|!#U$?-^(DY=6A~+>f<;&bS$}x;aCuQ`uh7FLDoQ>YrObNIN_ZzvBt-#|43?Oj?a!G1c_ivDr$T3CBBw3Kn2C5-e$J;Oj(W=lfhZ%Kk%&s~4)e=qU%|9`KDb!ZofH{AsFv@$G4+7|3xz!GaCdon=3j2?xx!Q;h$fW#D_j_*TUikAC)6Ur+rA-?B#My9C`qeFILiwjVd54GLM}HdZoR*L|`!7H1f3#v1{`hA<{=8WTrPbvpO+Pk$rDy!^&i-Ca*Ra3(lNKqX=^DE7)0d=HddBbW%y0L-{9=%&guni~p8alSzuWomn&zKaEMS!t`MZYuF@8TX89kt~#oy)nSC;*GmlxfI7sL3X9XkxB2hySS8yC6dVd311uzV5Ai@LnfcQwvjGP{y?Z56o{5RG=Y%67CYu7AZxMt|veXf10p25u##?c?ls&EMVZw@$Swzr&T^y(Jin5UPJpKe2W@{oUzoqN~xevlK`aiWtF=*V*to8@gva^*gULUiw4Djl+IV(w`+ueDtEd{6agS?&=HFJ62W`lH<dbAHpnH-M#R;*6(vae*F2bAS`stRsJ(_TOIlXEJ^Pi)}hL#Qtpo9Frc&7L;k7S;wc|`!_URuz*X+iNG)|Jq?Mg)%efS74aj5epRAPh<Vy-t;8)u9!<V-$XBg;`OV%~jhC*44iBd)6U0a~7v;el%B?Pe?0?lmRRJJ$;7RwS>(*U1f|I<q3M2>8W1Ehz78Aif5-(pFFmc1-;)Rv~ofBN3+e#xXpGAl*<;2vcIey}T57FH7Siu+g;jF5|N<n_y~cd!giuWJV8f&oEm@Yl}UUx5Mdgf7pkzFm*k``QPti-EB>8AJWI@x^hKEWS1&*f*J&zksf>b?F;rqq1V}&{}$9%2N`b!h6g`;~5@6!<CpNVwE1n6`AHG`Ngvyh2s<VJjuF-7d!ff2M6mHigvJLSdkFN4zew#&-m;LJDfCHFnczDWVo0z`9cTp1jxeeeqN5mbqroawp4tX_wr?qx{}C~<5ORh_XF77q<?$sH3-;A`BtiVU<lW#^eCroMnRD~7G!;+@dx9sQvQ5Z{t5t><XFoNCy3j|U5y_f*UBv3^O(@S#s4SOe_X<qZ*hOW=kI&IvjMjfIY<uUC{w7#>uW#mfgF1kwtr4imn1eHB*vx~eH59iG#|$D0|vp?HW--edip`pWDg&FEa~|hZ}Podcko$4VO_L`8Os@hGlv}e8LVGK66zqLW(Qa0w<}NwA9q|e=*}7`VN`UE=Z8(lyTf$lpr;W2HlE+luIl{nOFujl1wQ4+#pC5w?B>76A1LafYy8vLx<of<7nz^V!L>Em?jW|;aadDB>=xCDy9cJ>Q40;}j(ZCL=dcn!BFh%qJM^<1bZdmo<EV4F)7Sy=fCL->sX^lb8<nr?uMYychsV5cxwUmH-_7^Aw|Klo|IQn#Rj9TH{~cG|Jz{Bil>Id{)sRk$5$_<r+aYZ*h!q^bR^uiJm{X+|`~kG0Ro)bBjmZ(kmdtz4f4%x$?!}}KkmrPZ6;r7Y(3&mUfMFAdtqB8Q%O<0x8*8LuUWZY6M_MBSn#j?;;|e2TyOsHTs<ec1qAc$QFD_+Z>VHpZkKE6{73I(F^Ya^K2dE53&0`a0@kWUE5B3qxV=VN}&&=Y0eS0EPEdRdE%gq6Z2Kb0~mHsp?u=y_VDM<T~yc&_8YFj}(kmBk1aqJP{kDIsEh=jHTY38LnTDjE~Z2&U7e(gO#X^(VC9Edqqv5cw&G5vik_ELqLQ2T<TEvc|cnnb!Jc}<k!gy!0%YEGDmy@b|DuW_ylMaa1gy?iBsEt;3CBKblpCi^b5gq&1gm|}>+26CaRUE2Z~n}>EEe6!`!OPMfe%V3c)I#S(9(7_9??r;1Sl}4t>n6OF|b*2WJi@)?i+CDNynh|Lc7J9J&k94^h7e!cN+e4^B-7ocF(C3OmRCx$Z{))5uFnP##lXMaBtJHLpB3Fw`=n4VWpOxe4D8%JLT~xS2m`iY-2*uDjJ73)mDss#PLVt^jF@NU$x9&o5$MsHhk8|Q%w?0|%a?10Di@H0^=a<$!5{8O?roPj%-g&uy$I`!>B55?!K9klf5ir7}*LdK{%k}h9lumZ;<#+i>Z1viD`CXn!H(<@EqYs^lpyfT`>IP5?v4oq^B=txK?HAwY(|8w|F1M~`N?je1Gh!lKQR?!-I3J634dXMB91_E_Nvw-f-<WOC>9y7MOZ7Rx82S!+M7eFk+BYlq@&gPWCDRqu(Frw7qfA#`P!V|nF`fJR?GCAv{jYqCrq$%lnnszw^EV2FH8pM5OAluvLU-dtt`^O6#dZRes5y7zEZ(X_Fq=b=&7AdYE~RZC%B{$s9Vn;N52&JRh0DEQpL_5g@1x_c(Yf<C-Uj47hm}c+NEZKIl0oaziP?i!l|Ss*l8N1SSN$r$Z$DQJpE2C{e3@)4`^;4vK?2CTm^WPcBfq$I4JKx`^4hJyN;C?L@<B-EuNbOGKCjPF1{m1+vmG>*(V2%dO3mSTsQa#<@3gP@o8cw0TRYZ_nBq5Ks5Q`Q8~(Rbcg2yQg((}h-ryV85v3L^wJQ{8a;&ybu3_a7YMm`=n7Pe9GZmp6MPo&~WvR4brYYYqU~+?Nc!pucO9Fra4c!&Vq4j|6juSdwzqtp3OeWBgZul>Ae{K~829v!GlD$q?q+7MO2iS1MV(%*N759=eawa{q19WoLb73Eh&ey3t)w-~PnL7w8U~Mqv+{)CJ$U9b`^YJ$$hwxrtO(s}^Yi}U2vEeARO$_%>Ntya2-(jFXgO{nb_6n$Fcqa4}B-ctBHQXmRo=FVgM|)&<w6U;s_=>jP`41S3Dw>oYlsEg41=&Q&7=pl{0>Vfdc*BnKKH>n#^V;m(*kz;NHd;R#sm$Qabu{pK7<X(@KJMH|<_~sMkkKBlpc7SQMy5cv3d&SS@!#WvPMYILoC|kjS<pyQg|Jz&mM31)yi7E=y>UdMy0>4T?Jtt<@{oHZ>Lj|ioC)4CD0<5|iN)yhTcz9^R%$#M{`|-m9{~%-*ZLryGmCBht<w+MgD)_6-g?$_J26jL**z&4;>eZj*_Ll>g4V#wF<cbWucT?Ld4T1MafMotTUJ@Y$m&=jWGK0#?{LKJD9h|92Ncqg5qoV?5>$=A!5ijA-*T#SP(CLZTwECKgjr<E_hscLN-N|Q?yd1jz1IPD82-vF2HtT-*a4_7ZcPN<*#UkP9Pw{BRWG%&TAE0>)wj-&QgtQ1Dh885GC+xPZ}ly#jv^4E!%Qe8oVVqwy6H;PjMl0*Gr(S3`H@`>e$5QVkPkkXht2|G)ib^G2_aU)->=?bC=Bocur^@W^TbdPJZH5W3P@<Wx3pH@XaRELXuyDItL13Wq}g2_4bJtOr$$39^_1x%m!kpHXKddZ(hlR<(cp$^CXTTXP<h@^;8<k0GKy;+6E*X*x#i!+=L`jRTUnb}x;*!z)odK_ebTAt@_m&GG%SZ>5^A}C9*+Z*Qvv76kM(7PAeKR}`f7uq@diB;YMs8=@mHrj&d(u3k-K4DRdWx*YSO^6LT>jdU&)>^RE(0it#^4jwmi;5o_4>eAV;g{fR8JG$?iaIMzrJ$PSW@<iFpV^?(f`RVZvfAt0uRgwN>o%M*-25m*KK26m=K{Az@$8M$C8cx*&!uP!gHDBre$=sY6!zK-osP6n)2!tXTxas@F1zrEFMS`@GzunOjnJD^m-Mgpo(0L9qPw7J)E%M1=@`DsLcSG|F|{(EwiggFG1i><ftKRAg&&V0u871mo>NnnF2>N3GzSGJ5jh+Qd7BHsq)aW5C<(4_xL7+n6f_8isi-w>gMQVi?IpMeO#D7(xnZ;J@o?L(SNOgkzl@)<YRLDDf_wlXS;=LbksUCxyr%@p|&<I=<5~)vuI_NS6qX54f<_E@K3Y;3BuTRV!wY15dVXp~}^3sB@6ypr^0huw&g(RxhlrA~kp;*$*Qq%Oq+syZsf&|G#LPpnIwj<l)S@6XcD+);x2lt%)5(y3v+lwqNL2&`8WBc;Kj+;%8(@KL(Wu<vO*AMGBmeWy1Fmx3c%rPSErlIm>lxDry+CfO~`<3PspNFy5W^5%p{bkwi!V@f6Ayy##FCfmtV9kN5in=8aBBQq^{M?w-NuJ+Qu9dh$fKf^1#B+`TU<`z%g`%?u9B@3NU{LWotZp$<PW96J0H*VJyA%XTAN1$g77)GgJEF(in5(dxhgu7L;AP82k$WYQ;*Ryittfsf;@;IP5+3U-G!_=1OUJ?8-KksuaO)rb+Tflc$7safZQ5Cs|EPts7mj%h59EY6UV(5@TBNSSslI<cZ9NxafDPGdQ2{Oz49@?_()Vpxk+w;+kD0vC3M)71&%2$MbQwWNau8g{aBYrSv>CS)YFRnv40<s)%+HX-3;B00i#L%DwMMz>$-9Z5FUt|}}qY?O7KuG8dW-6#V#3epD2;vVbY+AVvLn4FYG{anU2%)Y`+tzp8s&hW&eETxIu#^tB%;7KW0(qXQd3IE1&RpSpYFO}<WN3Gjvsyf=n%#L@(O3yCCk6v0uL>Fz_>I#I4c79arJ!;R%jZ5-VII@e=x4021t#`ttLLBG*Tt`1eZg2i5(I2c+g<<t$vR!Rm-%J6za!fn-!FH^)gK4nBje<y6f03wS-s)p-U2Ew2<sYvAT~Rv`ir&3o58K!tR)PEMi^e@HJ6jZivwAvwZ)ST~&^wBNQe*sLJj!7i#B1W2<EOjhr4c>k#(kuvvH#;>3VpB2%ii!gnL_^%BXwb@ZZQ=0d9|YqSO^otx2sVI9Jucv^7_69=Vyx{m3LTvxJRKQ(t>QCqw_nbT|^6kR7!&JBpcF7RpidyC@-VCt=s{`^TPZ4Eplqw{rOV9@41&eG=%R!fx{4Y?T$-A!`#+^fellK+7oRV^vAWMX1ZJ75HDz}h}j#X1b$$uj$_MHQ!zbM8+;=ev(bdTWBSE+$w22&d&5@j+-f+9B8fP<ka(th04@E-#4{3-+o}ua63>SsNUX$jzV(|IB%V=@8l-WB#4|R7h-%%?;ftVRrO0uXY)(ox(}*I62W`nWr)9o5kJ~&KFY?Xh`6%TKX}15lsZQOq{j1mgd;RZgdw%HuzP9jd3%|DT>wjNc_+9?%-^+jfi$9xQ^4IhsuK6qf_ans*uf6mmwrzTU-<5un+t$DMv+?SGU-a3ZoQC!8EB)8Mr~jsB|CeM)<zei<^Q+Q-$G^H4{CDx%J?k}U3ncPA`!_yy=FM1M)Gs-qKmXeo43H&U=>lc%_W~bPBN5TdCu#QIBQrWnpO5MGSX9mH@ipm~#3L~itOASp>`}=biX+SzAe%MWi<AGG6natLbS8=|3Aj=io&Fnio6=m?4+R~mc1Q%3KmL(Lv9v_XJ7x{WAN!Q?_GTY+e$)dj@3?FK)e=8_i|I#H(h-<ngL|yzUmf^N1G~p~Q@XFC3$Ty4LiA5#1M*u2DXY{3p4pq><VQt-=^bwt_tTX(<(N{jwfBSZ=k(*2Pr>Mpi<YUBrnNITrwg{PD;E%Dug26g*(=rQ)y}$#-IVbgm#_8PK4O2Jdd2kq^aPKu_NepB9;p4*n#Ilfn=3QJbe&an#$NEH5u!wF@SGB9_2pB}j#1s&FnmQ`G}6C0hWYuc@lE^frvvnQe8-n}qA@5co!?%B<99CoR?+7AF{i(eu4nod-H|UL@$6nIH@$<8?9Sb<d+Jgz-;N0ijj#QgBc}_y^c6awG{|I7=V!No*M9NYlUopC;W=-Pe;PZ$c$mr1jvcAIGrbw?cuCt^!?uef9Xa{>J^$?Dm~wu1?mDkrwsqa|Scy)Yy|z0tovQQC+P$CwpLIPKT7JCR>8?9BwxKT#;%CPny*Yl|yW`(u1CE8(`HT5Fd-ecZ%~ii$REYlh7Zf?}Trmy>e#Y+!p4lytGlvt{Od=<tC$}a6luEP=n9W^Xa57`H1H?3}MJpj>JV_Zdcnnsyn}Ut;g%46ov3v=P*&(*rvTpI6o`yp=`5S#hUHzu_`yM)-&0Vz;;g|%cupzsNIO(tk-6Q?cAKMo4;DNW%Z97`p*G}Lv$Z61>ps6YMw|7lLS)a8LvmqBimd^pO8S)6XQuM5bKk}Yh>s(XStQuZwtsXR#E}X5NU2Cm4w$^59sytHGtS<uk*1FZ2uHJN#BEK1W3}J-=amZb2<=1V#Fm$GdxSS*i#*QAJV`uu8KT1z3mBn^!8`2v(G*1jyI}<C5;RKL2^(Xz;x|IK1(%q#?MW36&?HW+)Qu5y+6DJU6hM@;kuv^uxqmMbdWAghAtcpPTZ^Zn<jeH4qwY40{IEaTu4H`(L|D_kTBeXur)&lzR5sxW~d^Z5pVHMgP%A|1(OZY9=U%orIhoVBUV{gP7w<TGVN!>k5<Hfy2`xDcfENw@n$LSH7^|#<f4D7^Q@tYu+qc|F<KvU8b+p9+ySD{s!2+gQAx!jNPGsEcgH1rkPbBB-Q<DrzsbGlpnx1j*sBl%w4&fiAYJp%Ip4qh)$A$OM>dcZRnq)+#sp3;GGo6#u=RQcA$4b|TVQXC_MKgd#fgJQGzX|3SMAkew~5pzV72gCueHtVZA079SC0|Tm}cjOL9vdNjSK)~coi3o|7QyhSz-!kEf#Ks{y7P6XDZ?SzkiOtHA?WU5+7=&dceMQnyphCCakJ4#_xTq5j!I_o;PSQIA+tD1164<VQtD-6MMe1U&w3%bWo9`#xi6S4eZE&dtA!0Bsd?0Cyn{^dcG34X!C80vBcGU`|N9wsJTE~=biLn<aihF5J`cCPBVqR1OWmQvnPPhw4hX86@fG`^=O?U-D*(}AtKx!g}Jk3y)UczkzQhGrdW0D%QwKUN=k9@*GsTqP2u^+`vwWGj10U+XAZHV$Rv>qL`0VDyR3fTd8vBY4=j-WNX*tHj#Q~i!^hW%@tu$^R$xuGx0WCjbIA=XlP$TMNoqC<}^IYnTracs~2#bqeQlk@?4hTLY`4%E%Te&#YFJ!HVk`~(*qzk7`B1lKJ1!|_|9YljI=>4Pi5pRE<+>*;oMu4;x39TAMK2$;44SRS{-cn<{^DvTcwjw38{_C;Qnq>Oi+xyXAWRZKAR<j4MzbC{Z9s^Jz0!x86cZ_<wQ;EQYd0*g4uTiW?+6XSQJhG1@dq}=xImtKYg>S<->3}Rl7%XZ^d6t_9X1Z^QdI<DEne9Z>^p#*?|KH~w@=m`zvffB3_7jZ!K2@WVJ2BZ{E4sZY*UsIN6!~rQg*Wn{XGo$5J6)4jnTsn&iZwQY>V90gKF+ALH?jFJn3IuN_@Cq6s!m0n`NWW+sF6aN*J7M@;p1yJ{rqomHNs8Gzn?V#jZqGF~)u0NJzqERN1mg!Fv7TZ0J7M^}0r+nS;Eyu^zc2Ap7y<l|;*^Y<{ACP3L6m;o`1RV*`+1SS5qdwjStmK<9BR*S`<$4XG9`A~YF{G(W&-)}9V`Zq99?hE;PwGIB)tgu#P~^}`~FXhR1>e0Y9O(lqe3%tMmSvLvGUatfhKufsfPJtdq`Uq2)Vkn0(P#g{SK;8K!Q^D6tP`|Z1<!~gvk?nQGVA;UP!}0B0p5jA~e=BTFUQ3d%}rk;fFg%Up{o1wdAq#=MRnodzcqAK_T#A6yi+8tgIW=Y);)eF=VKbefi%SmWa&*S$$42XtZ=5tp~6FBQp!>yceP!KbJ(o9PP-9JsNMPG<&DUFv@ij-+s2ojT2R7#5_)$lViU9W!U3t4ts35*^TbdE?|#MC}ewN3+bqinAs)bAMZT}TM&BD?+>nFQaeRb>t=j=D`N0rZn1U2!@p@@_z8mjFTbp59|#hyOv<3|uj&}|RS~;hH1J9dOt(aL)WG?UZQu948#qrgE3PMJ8rZ8MpaworyXm-r_t0&4mj?dBPtt#^$rZSsaDO_1!r}6Q(Fp^~#%flw{ozw$1|GQ&ip0=N-kCM06|TSvs!Kc}CQFntA^x{=rcbs3_|}Lvttt-{ML#P0oTITNV9td8>S;?654vuNbvf)AFzrNxP7@QYfYy2Y$}pM?L!GjSxy^)lV+kXTJ~QKkc%y+>ycbHm6ehw8-$65Ug-v6@>O8U?<J(yri`$WIjKXYhd*k`MG=;dK1dwqVsroS52G}g>3vXpHla3*MxvDUG^IWR5rq7K`bnHsvB4V6gAGJpDGw^<Ssn+1LFS5fF7MDn#yT&MXkNFi$?QdV?%XzL`4?h#l2WU<*ax-#`VtWM14IiF13FbNw{(tt~B-XlZy$)KlSaTJ7?c(gSPjQQP{rvKt-@|r{Z7C*74o&C~kU^r56#_UGiLGEEp@1mjV2}(#fFQOLLm&#sAyg6_Kp+}GD_xqjKqx5CK_UVgG?18MjBl=D7w4S)-@mwa&ei|U+r`?enB`ZDZ;WH3dRaVmT<zs&e}kJBnpxUg$-Kiq``QxP2Q&4eS&~(_b9tky_b8|BLS7tPy5+YR@_3t9x^{;Oot7n2>%3;(T9VfiSUxBaB#Og*NhUVZ(YQmvWN(_y_<VI|@PM5cyJFBfyE}~K3Mx&V{`PlP-=PW}Wn=q0()dz}bdxROgP4y<PsX%hm-pa1Oi&zf6MQM;(pb)GPIp&<H7u_~RB^zsf-&+BH_l{I#DY$N+J%kv+wVxEli<O$;)lJ3gzuSRhNhIn%2cXxx{d}=ofm~jE1GUOBNC+~*3*`@&@Ag=0}biJNg3>DMf(dTbOZXej$BW&pUH=7CUm~Hrmraeia<igt!K?{zjx#)h$?`sI!4!ELQ5jfBsG2Ms8MFhYFomh1{P;#B`k8((o6qT=5+kamox*(RB5!c!^q|?*+8@w;u4XRS9#yWSiE7+*9`s*75AJFMkvOiQZBP6dwxC!F+VT@suIiy)S^@b5r}t2J}jnJrL0>_TFiTIE!~n{4I6A%)ya27mOKscDrH1O)W{*sSMx-%!C`pWIH`716BFE#`DQvUJD~CmR`}mB+$Bwb2$Kr5k0Wa}l$;|O;zD64a<)R(o+R|%6f42cREz76M}!FkqhF*J1@=kt2ixXm2h@TFgs2FZg3hGZb%>EOdr#~@LI6>W#IicLC`1a;!(jzuSorOCG%+>F$%330*x`(~TxNLUH8sQMeljhT$yN4qKY0<R7^k;6$&ekx3=iQIbxZJ&SpX(_3AB;lvY(SL)l2l1haggIRH-$!j7!e;#Hrp?Jqz8lNjmC&HH`unR@Qg7B<9#13!*TJ`AL1|_?y@DHdX(&8&@k%(w1&NB|Y#mQp*r%F-*1uf5Ew!F&=C%F46zsI%vEI`mFzv_jq9lELQji>h;5ceJ)49kuYlu;??gZR8<Ze#zw#z=OTnE-FNdoOpcAaytQsIMX=<FE^+7g5JJVu{K$@d>fy&9xUW7&b>o>1OdqWSf3bRph?i*DDs<x_OL|iYj`Z57;@stCo)XI}y6bo!cIu@K#Mz$Pgj+0u2N1b1j+GFdf-RL7Z7BM}$*a*bnE4$QuaN!A-d^qZ4Lu96n?ilakD<eR+gB6lOuR;=B>?}})oWdFhg90EcB|dFNX7GxbgMe`OOEu!=<!+?x;}QEyW%{za-I)}{mafss>r0PET5UXnI-2#syeWxz)bm~wBHS#<YDF{r(eG|Yl^U%vZfsZJawXKk=BiPVZ}fi8hdIs<frjBUpK<Zq7lX&11rXce#Y)jOi*GlfJ2*GZ!!hfVgar44#3SJ4;=<kx1f;eEBEc}60+|2CNB;v-?R!^v$Pd^nUng4Ef=@gWe3{+Pu{JgX+-87FJJCZU0g2OkG5R=`S-oM8;dvk>NUGNjIE{do=xWFobm2$YtKJ14x7uC`?#ZbB+0EKt#xu$4n3`P?%!+e-%-#CY~h`_YGzybDiTRrxV4V9@XZ+wPgtR!uq;3Rm)CV^e$q#YPBJX0e}1`<@7;=fx$~C0Id90dh+f&8B;ADV<<Jd!aXbH7uG*Rxy2-ml3ymU6c!Uxzq-l(_M|7KH?uDd%u=H(93Iv`TKa}vqm<16~CYD49Xyc$d;L5nzEVW%18Ie!|^N`<znLoI1fR*qYU(1(UanxMt%e8XkItT}QG6F|KJ<lCEjD^XC^B^|r2r9?Ukf5_2TSY<8V+c<4@T~IzeKP+IpymL+MD#6|68e4(q6%n#bMwH7ieN0n?o4h}oXAB;7<AVmxKYnD`cioi7_1Gv!y+4+q(Mzj44Cmm=a76k2F#`iPy@wwVzFC!c4*U4Q6iDu$@>vKPJW&U>XaZ><%UtbpK`xJR#--t^69?o!VrPxK@CPQR+oVh*9H;k>fqz=YeRNmYRYX74QNdU+ID}yyFb`~-L9=6KG%hiVi@W;ko!$T;L*kJO{$2b0ZZBRgZ5+7fR?gdAvpbnlmG)vbr_6?1N}+=s8Xd0J!L;MAX^C}HWN+<mRs^ea$i!<JKxDR-))j&37+(499*#$I4?|&4JRKMXa&?I45SwAZ8iva&Oz~Mf)qe78BPDMMVonYxD&m?6j^61b?Cj^vDk@7UQ=73kh%m?HQ{DgNMS<E4;#40MFmiC<~H!^0e(7QBelRML_z9_upLF|r$z<^63_6RXe^R>eDqQmqWGsCWXp@Lh|e(v8OFQ=?~|-IF`0g+QRlP_nm$QEi3=8K=(AlM6NRvMK0ft+8%+wi50oN;Fg%#tewy*W#<;vf5TJ=mRJ3?(NHy{aL~2zEZU@1Q6&d!3IgtAeSIv*}11QJ_E|(Q+Y)n?^wy-AV$JymIv=nVb1>Q+-;_ySqV3<yh$4nuLYA3*rtHd0V8|jJ5C{;|y^_18B5Uc8+dk?|T(>TecNa!*QI@GU@f%>wmR&bA>+g1A+bRf};YO981ui0l_G2*!zBc6;ob*pNC=sWXs)p4w|JF%WtN<Pd2AmDNNwARzVKVcL_i250qr-LEY4lZsG1Bzsk&3~m_327Z+6w^!uv)O~-FHer1ZmPKa+D#=z5^ZxW5ox&MTJ;)6U`YrfYmZ!!VXBS4yX~pM)QBRS*};~;LQ;nd#h3Ru@S=J}1HDZlq56Vl2?RS#VkN4jD#NspR+a{1EpMQa6;+Yp(%MAJ3?FLnJ0=COKgNnnQ(jt>JoC*U{G5rykroN=Pd=<kpk!4}K0ij?<9_Pah}a-E5&(K^vR#p&Xv&7g5*fu#7|FOAMQDySqBF?`Br*k4^b~}^i;m$@K0S17YVZHrtEMXgf0(iLfe7zSHRZf|Y}dl~wOsl*femD+u0Cfa!yXmHJW$haMUJM#X2fK!eNTqPS6Rv4rYrVEe-iN=)0&OV?RK2o2K#_&rPZiaR-!p36KDC>f~GSua?{fw*RBnDJXF5n9@x(b_cqcTluP(I>~3UA9QhLYq93tHCGeqiZWrbP?WVoy=TN>--6YG>(tUFjp@)?fVWZ;`4=0?XH>0KAmb(tFs9D*Ir;;pq@@5H;+YV-D>ugDKMZWz5u1$aGBj?*z+-34Q-*A_K-SI-QEe}jHyGEpX-W1G(quNS#3A=R(#Ye%ZK}Mbzg#nacB)w<K?UwldZ1ioJatkHp)-&anxB=~+O}U}u^kf@yC)?2N<iul>+DYt)F2|=$x%vP3jm+$0k(s@<>Ki-JTMNIveQV*j7XDqtVODIMtA1X;(U`r_n7z@Mz0sJx(U^U`LHovJ_6=e(TYmWAnarja>18rAB7jO@%NxwS)LJMvsUrenp-u%M5%>v}D5Ri7*Qgc)xhdpph~S>sxmY|VJ}N@XD>qS36&4~lvVv7^My3@CA=xqeS0UnxN0esXHw(TrBM)2hnLYou^2cOm6A2bFWD^aW8(F?)oMFn}o^qHinY1bc#5#&OtDM08Vs_wf?WG`Ln($WTY()rD^ST8|n9egDu)P0L&M`egH6tpsP8nIv^hucYNMQ)Gn3f6!Ty;zW=iJd4@We6{d7J9!fI{Z9c!VP+vjqj(?CFf1ZelW%ND%LNMp`z$sN6KzoLf+!o&Rvb5*O?d_#v{MQ*94wev0<a878yo!}40}M{^Fai+pAy@!JXi)+uAzL}~UCli4NGuQ0pGBRa9u1J0kp8Ryx=bahPD^&H35@pVIW?QMUZ1LnMFl|O1sf846e9-PyXJx^M8iHmDIV0>YeT1!4N?-!nI41Q$WvY{1hjJdFQd&*%p@tn<v=<LNa&v@yHoLhAL$zk4I(@IA}<?A%^rEg<l(;OQRP3q~E7Am+ZRF|4={z+9%c+{TfYxCw*XMXl~Wa2mu_WuLdvJ1@W=}znHF8tRl-==dw`}pc}Hs^4)v+N|w)2D+Am@it+uA3F#)g^`3R0}$d>8(El_;a&rdi%FIkN>k;j`3{mD}aElpL3WDXPSDZ(RTXZF+U0ECrYX@KkwE^6qx%tTeqkuvg|6bI_K-+&sRHMda?XF>&gkX$Wq}j*E_4!S(Q8g_xXR-zVgQ;EFeFqBo^oA-6wz}%AW;=gxPys=(4zCF&xU<wEWhcRc$+JNlVTmGwbGf5q;Z#^s<@1QvLd(OdQfx!79aZCvH(Jo(Qr`KcumMDL9B@mQ4<Nku^+x+J!hri}^<ZNmbMUz`=7iE&(k-m}_)5jmqO_lXX^k1RL4h6;*}dFA;gb#HCQl3|;R^@izU45R5x#MJcyF8r5p=LW4}KNzMmf{G1?_w+a<@Qiu!yLJq1#_rQQ5VO~Q(E&uFBmSV8$IX@Oo6Dmp4GVBc@bO8d=4Plk*MpOm<Q9nR(I*<zocs~=>Oz7>P8hSYfY-a7^EV0WEPQY4z3f5;CFU^hvaLYY})D<;r0ZFlkor44dk)rpw;X7w#d@Plt^A-yv0UC0l=F5!{FHvie0^Gr57X!F}@-sHLdM&aHmOboohtxUzm2VoROay4_ON%vOW#Me$-4U{E;|`?dVo@zgW~hz~dXdWY8+fTrG=<qYzO0Q^zr>d%qgg`_9HaBcs`X`!-GY|}SXjSKrI4~hEf9#^ezp27Ov_r$-*6ahLGQ2^4i<`uAw5<ihI>2+`2*AvsnFtZ$X<A8T8<w$syK3RtS=WOUuA`sk=6}pPx5tls7Ju+eG3e2zO@Ii;}L(7r_n0UKvDbPp9FRDjr6Vm9G7%W>(eR>br^<9#r_ah3>1D2?n}_!0slG>uM@%jhsiz|NYd9419U)@EU!3(esEt>(+xAH=c+U^Iq-*++9s7HQCo;m6z;khfRb*d@!XP6Fq*(<{>oU|P){F{HZNaF&0z{sCi~BS$_bE`m8WEA98gSldGx<%p=ju%FoAgFGV~JxW#^%l(HOlaWXn6ED=|s7pS;5KzkM%TWj+|_<&_DEXCqR(Wy88I@VCa3t+Erb8{mVI3~VSuZ~J6t>Y!tc<>FSk@pLnsF^I6TyOYTRL=uA&we7d0VF;u@v#syI@r83oUjqq=fCYXYiL+*qCym0u76mHP%uZ5~|B?sLJy>~dgP2&WJo9QlbnYfXfcx|O$ZI?faGrp4!(?1V?%jFe2)2E3&|q_u-~&*mv_=M#tmMCqZw8A3_2hW9NG7(0sFIzwnEpHcDukNNm?v1z7|oXOMojX443qL=v5FSO5-61A8z@tZ(&%gzD0rt8ArF@3)hj|r^y|1H<Q=1aSD1B&k+pphW<3;`byHy0V7kC;1a*{Q-K4y`ELhWukXI1awVW;rrv+;_=L*&~pA>Q({-rCr^t-sLf#ud>#efp5xbD1xH%Svwk&kH!biBa;&08hmwP1G@okNY)!`X}uG&LG5vo$xRm1tyXozxA>g}t$|#eudC*l{s)yOEy3p)9u}kBXd|eEw#gXFF_lV>Lu=4F}o)hUbnIwX8~kK6}HBbQeJ*+=^)lc7!jC4kmm%&`De6Ge<efoOuy91D`&kKnH$sBt={RFLB;<VxvbTh<pcNH<e02)eDoMWl66y;s@4<VcomGzD#VO#_sttv3ZRc?7*7)U#%LkHG7CIw=sP%41wuK9+0&WPZhEc%~+?>Ff5WC-KBQTqN)l-=ADYgRuG2i<Z6Ll7!(&W+C}hzZI-25C<+1)m15w<5oag_+#K*nxc+yn%b{xk)=`D>-I&pFGr4z5=2UW1vKJLQuMs$>2nqDQd^cnJklej5$K=NzutK^8#j4j5PSeSN(r7*~)qs~KYImrF_zunjrYtv8ZlrlF(b<Z7a>s5jEN9@<P5E;-H0YE*z&tkL``Q@H@^zDj??_@6jhwKvoE0s@R?M!R@dR{hEDT*1BdB~DA3anf%~j`SEM)W8MZ%=@&Nvl^D0)PYBKwhvd8At|iuOgeUR-LGA2(#{kL6Ehglyv(7NYh%VNHTJjt(K}XZJZWhE42baH{RW=agk`KDd^Iy$i;$FfN7mEOT-;bxpa$=#D6N&k~D`9VdFRApTZ+#xOObizm#zbM|9uKDS}U7kA1g$qJ7=7FAwR2&-o-WYM_DRK@RSBjofcNDU~7`oftrlJEHG_PlD<EcL3<8=n4!YxgGb01;mTN|X)VzLUKvo!gsG2-Kr;X5~o&%UuaS>TExflhlhbK9=RZF&e%HUN;`N8F{~PQX=>M26cors}FfXkY2Qj<nti=&XX0jxc)%@45kge-n{Yk;M?F1!ZI6DSw=pBDmynVsteWOk%SWY!yb%%9@Rt~CV^bGB56y^-wi#+4D!~EgpRy8xx;}R5Zs0s05ZBb1#wq@;X1SLmb4P6MWflbE@mHdhsT@}GW$?*e8N+J0tK80lJ4Eo^2>d)I!`ioojaK54z{B^h*sR?`PCPXFv0W%VL^j{25Mu7!yw}c)DZTm8bnw?zDB60)1yf*6Ap>07fbY~^a%g@Tb09`WcwSC`R(mn3%|ASTMNIHJACAFhd0&sw{nNKa)-BahqrQvH`Vqx)%LGf>+l-Y_6hD)^E^f?7%Z#@`WS|gOuNBbR5J=4RZjsx6hknCxMAQCDLg4Z1cB~nuy=;K+JbGLYqyW+`!H2JOepVp>4Te;)P=7%0KQ2(FO=8EgC+Ei7k!}-TY}t=VDJ8%n!Bn5+#D}|QW)XFLQCG&$7fy$hnHtuXr=q=_-|2&pTAwe|0$g=exJA@8fuFU^vurBYY3hfdY`GeJ0DI2@7=M)yLadA+#UZdBd2shQ=PpB%%!I2Zc!O#al>g*5^?nJr~snWudr~$8=={}+@V?ylGCz@dHc_`;g6rr%_=0U^n}Wmz5vc@CCEtEWI_2wCB&$uJx8M-0p8CPK!nTH5Ag)5ACIdC2nV`c$8fGrVyw}bmq9%9;>BW!s-6(>?xYyPq&r@r?_M1V$@`Z|8T`vP|3W=PnAJlpN-_NLjm_@)Dh&RpK|X&m9#btVAu4}TxDcmL1Pqa)$q3tDydJgN<N0&CbNGFC;XW(>Y)QxLTX$3d(LPrQ@_d=drPe#DASr34^KUP`t}a(djI9JB#(7hp)R8O;DcroEWZuZ*EyZvVf_@4kU&!$+;`)E5$?<$utsY(b#RWN@zDj%LnXB%rDv($f0${r;4bXK4U}s(J8^5_na;5dva0_1NmGhfDa^lqS1rQ=`ad4MEe?S6b2ck{nUGnGKI-e8x$2cI%GDN?lQb)J-o3=VsuCEDQ-lKU}4b-nTvFcl_6M%EIRTn+(jpAL~;5Tc@;Xpv+_D@}rnfh@GnLRQczDM$96_2^Nz`56xrLR=55f6ge3_MK_;_Oi5qlr=hL`90Tj+%G?-x`f3Q&Bgd%obpz7nI}%D1fG*NP^mF?S=B(jA*Oi>$N9b#_0^wf9|{)j+RSqa1TmI=BL|I(r_J_?B}mGJ4+9WS%SQLI1*~zJ%7av;hqW7-1C5_FlFi~2@m%6mhuXfKOA7i4_rHjf35mWiZ*>&i3Bm-lb(?`LQ{WI7T)E-^e9R%pcIn$`c}k{6J%o$6$;vdlYStEa8q?8ZruXK3Vz*)1R3$;-Y6IWFdWD+9Supt9|BLaA(Ekq6qNL$btEHWWWgN)144~U>y0%o-mt!r|Da$aI#=TSNYE(reqT_ysaoI=JcYNtM5kxSgf>y0oPDxto%kSI-cnE^p3I*4(Uk4fz!2C()ddcq9fqEmLKW<3%x4$q1({>lLOYl0rGMmVae7~r=^KuZxg^Emoa$;q_B=|Df=Pa6a4}n`0*S<JJ1Wy}t0qWTfwtZqMZPi2+^|QoRtj&!8cGd-U~hmH6U3}uxgCizTT1cPJ;X&;5eRE0{iy|$8+%Pnq5EnjCCVt_d7Ldzrvuw&Rrz{n(i8am4}B9FslU`nfW3lDJ5f0&pCl0&+7blk*-q(TjTCR#ND*g7t30xWVriZ{sRBT4YM#L6`JBzum*x=wQOy&i%<;4Dp?TuDw%KBdKi?{y#6%aZlBhL-CfT4Kd|3IQmRO@1{IVI=HJqY`ZP1Ku&{u5>40rojb)^A%PPDv?9P%&kaL?_JRR7)A7u*`rckv~Xc7?7?B`Y7$6UIni4y`~wO%S)%(%BTiH29IKJ%BJac{XAt7+#fEOzhY-SHOrB9uVIF_>?G@7z<h~h`s=dXL5hzt{R+kFNaF{ThUbMaZJKbu)yU}9mVWgP;{*E8MuF81fa|Y1J685Y(1fT<wb$oL<@B=8e-*0d9CkN!=8K2UlI<t>a{7rA%;+)_~M!4=fM$HujGCSehP|A*9vZu-jPOEq?aH(Xb5418G6>db*?Ce@&@34{*$j(K<2I88sRF~Zn>6VzuRGd&Le4fltLZG2)5eF)XG3<o<F&T+}NHqU>Fy`4a(v$YhuVV`GNJSWZ1-W?@fcy6J~xdeZ<^ZJCi`oHr&1HcyL10ALjA0W35W=L+p%um?U|ad}*l}7Lwdmr0+yUL^dxV?o6x^jTfNc^8teYM?Q#jJy^{elACyIkN>0YN&bE0VYqp!DyDz^I%LvnqP$&+xnt5?5=XOkSK+K!OQ1Nz9x&NW1r-@cD8MqpzB2@i?t4IyT_86!fLM8K-2(ZT*XOm<%7kLHQCtIK7a)C~mt$4gZeUeOG>`fKg|BxlDbx<(30lR5Rc5dUC2QFx@&!!|hoDu74}of(lRT`9ojpH<jnfJ^jd@p-z#ampSPZC`U0`EaS%a-jL(4*E{R>6El=!jyfMILaoDMz!G-e00w19iqe{fx2c~+F(vErH`%4RSR?}DP;sQ>Ok37rTht6^Cj>%Sk>Mf($eXH2Opg-~GOKno?0%N_b3V<a!Xi2$?wA#{i$2%5V<^%9SLxgS(!WE{GQVegvIvh4I^Grp$C_E19~jrC^m9h(+*uml6XxP&pQVfzlG?4JpqU{eCd?4yYs{kzxo`Bs8dR$Om0leFH)9d5|MB1LtC9IQ|+;%GUK$iY@!o!e%6zL0F{>K7G`YQhF<-@-5T(%G&D!whaKu~QQ^xFT$jWh2^2T9mXv4ySKRK{v6a`N&{ug)f$kAa37%QrKYlmtQORdj}GKh@#xMo)O@FhcrT<GD*C1w?Tp%+_<m@s$2?Y&;VWCDjcA^ft^}<;oQMC2PZM#w&;;!XSgZrk6cWC-a>oV-$s?NRdZF}{P_W^lj#EI6&A}>>klofNTbPm=S}g)^TBty&jWRYQRunpB?PPhTi~9l+wdj$9boM;fp8zf?ndi^6uL}Acob+yQT7IlZVSUXSZnklf;>J9-k$40b!aHr<PKb7+l$WmrK?3GM;XGst5>6*9{r^KSpmX=*Ii-n%6FG%Y-cmA5=t5e?4>|s(=08g*<3m=&E{Ad=UBk3J;3Yn#E!#N$n!a`eyL@75Vt$uxozuKz~z$G-&gtPd0gh_K`C#ZZ(D1;R5bL~_ZSB^nmj7F;;I{JIy?V-^&2e27;7=Ug${u+&{!=7Lm(XG`5zm2h%9-`KgokT=m6Mb@sM3v8ax5Ee{QW!%!{;ZcU~h5!4UXrXqYb?e%WGWrj~9#vgNlZ;_%->$vTbwfwDN#+a0LGfWi&@{ffs7><X_E1QxsYTn(rrVOlv+!aP)RfD|4F2Dbd#Z_E_TSC=b*Ku1F>XM>x8RFn+SHZNRlkqJQgE`nGnQjc)Eu=WnH;VH(O*C<@tn_<D|p`#?l&SsG}h<<4Qo$E&M4QxW&H2l}wG+6CB-!u$vp6%$}OPba%ZW__VT(Y;iCp}4BV?%bP(f~7gi<@xGSZF9+9aK8`{R(oBwqt|}hS}P=3(9!6=L!wCpR~}>|8rNH0&Y?|yslTnTo{#0czx2Vls=K+_qBS}LxVK$=($&S>@FxtZ(N_OqB-Axvtw_oS8K|97Iiz%>O*vC`g;A@i2BE=&`%U|*ki9O-MFU##^3=Op2EU;6J9lAq?~TjQS}B5?K3Kq%nc-%HP-NrrW1oOYQ^)_8_>_Wpdo$K{DV6%Gl96VX8~`(YpdSqiri!@a+8vaPLzudFvgk&T62(#Zm%%FWQ80}CtrzL<zv}k|LS$hug*4m(|^5IG<r!@^;!v7hl3aX6(wLru!Cu~ow-%_h#ak?5)CzI|9wh9f5}{n^r4~r$`AAIy17LHP7`ep-8Yw3*oaz*L$lma<&3x7rn-v~(dsdE*Sx*oM@Rkbud<Z$bNm<=r3XfT9ylxREl<EgS_VxXK|2L&>K1VV6*@wRn{AVvf6U!;3nzY%W%_8w&+d`?8+6`8{9$E~2#G!_rsKmc%piCo_nuOMXmU@F#XX?Y;*VPP$N$MQHc}1i0yW2T0*U;ur$X1BgR<lJyNxQ4e?(#`AV`5@7#39`3%WHhjbIFBJA~FqF_~E6>JVhjwg&|P^FxE%r6H$E%VWBVzoLp)T$%N9zstwKb=u&Vkj)r;%Q(nq*<w+EMqk~UDSG?J+>?~-^4$&MGG&92<hAZVZqS*1g-C5SM{1fwSbztYZPmnhA?{qa6alY-jAN1T18RpWw`zuQwtxJ(WxEE~!tq>wSjxo`sglk2%_aTtZrUIni)E2g+fe0wruCkdOEt#LsVUDg#v#lM`b}P{k+B8W0>wO;wPT4OaXf7c$;Y1ZgCt{xqBF#p17yt72HV@-voevJx?jW31{HueIjKCJxA)YRg|s+^#!XQd$2#_ZSHDRuxi4Iv0@+o6`s&%q_y|KhWp5}k61A^v`ILP20B3={4t61Zl^d^RP<vAwG?L<OipEK5k!ec^D}_8P`koPc#0|4m$m-}oiWN`Fj7nXB5>w0vhoR%dTT>Z<5mr#}d!feM@tjB^lYT;ciQ*OF$b%`rV(~P>rpfIXzocL!`;%3wK~5G|mByhmRpAMMa%yAPQUSBVhuk6%*H0wx1^tMW*cbyR9U5PI6ZjN6p@cKn6g}>Ok@Dp`?<4MZMTlV|LRlyFol5!cJV+T0W$?=KxJG8zFuud*10w|*nvvYZ8hA1B2(jQ9JsA{FLziHEL~HY@2eSZh%$5tepV<L>G43rbu`!(e3Bxh{fARIRRdLQ0v7%ORSaL<|swrPaY|O?~g^_*gN@@Vs;MT-@0~gzNMih~HKNKh$M2T0J5Gg1<74q_tcltcWQ%xEP015cpwHKhY2}r%z!D}*WnPZEPK%SQUP|?wsn6ySvp=9tO86Tey;RqS4l**XvCm$SHPaQ)GJewtaL^TnN&JzhF+_2H<@pxG<-Wgq8#MA`Ug|HhQa7SSh@_0<n5>Rd`$2ZaAhR%B+XNHI_@YF#WJZs+amv`wDM>7_4sm*%EiPHa6y_#Xde_^Z=fiZlJV02zKM-<Q3im)N0L#<eZQIki6fml%<*O=&7$ZBO8N0I=o)dUn5z^Bm0578%<w716VfjOBt1Cv;)l1@??0GZ2{UfdILLmnoBU7%`S+@Z7)sLhG{tSjkqa^GQm&?B%>9K}kgA6IzP4Eq)sw`fK4p>`9r(^undj06%&$M}h%K?EYW^Fh+*%->8HqZtjo9UqKVfh#FrgsKoNoSas_;!o<zBz$#sqiPuM%FaxBcw>0c(nd^~?w}!>yDsPS)uAHBsPVq=MG79o&5kAv14}ijqiTtm3O8HX15zZ}7=9UMaUwzq($D;@xrLlgH)RSN)31udO_dr3eMx<i1}s{`7CNg)sWl4vB57*o=?$pv(jFTM{*mk}uR(dcX=!>OOHw1xl6@Dx1;u9Lm`RUVt)R@!eKya4JUpAoz*db(Xvct348gBfYK<VX!rl!&uKf90`+ndJ2%448;CZ}3V;VT!j-u++{LcFzPuu3RK@ohs5S9R3s|L`B2LsuF6Slm0e5k)%WXW~Le<XAvoWCXeO@3sZ5H}wbt;3XTd3-};Qd29wuH_779loNPtr|1iSdEu4n7tC3$ba><s|-nOk`|gB_(8;?9AzGGtmn7cLT?eU)v{>rPF@99bW@G`Cbt}dLot?dTz4d`;1aXq)~ra(S0Jd9#I9syX-2gk5F@YPny1J$;ag@#!6Pa~F0?t~B+u%jjegyHzWO6KQ*w4J4jZK<?32Q2Y^4gVa1(y~Z%@J8)`(ClV||H*dxv(gC#OxMSwtSZlk0L}n#5!)!&<d|esAL)LNG!rOKlsF^2)B<fE^qPMNjE6E6h{~b$Z6}%mvmVWPD`UIe8!a@~|L+rNaMXY7fdZV*tjZGlyBFOrZ=S?X7j3jOF<ytj9^X^VOfr{s1E7KghN|T&I>~T)~gjhx|(}rEnJ??g?wMbWdEd9Y)5ZyRUGMy|1?L3qd2w3V@K;l<y;nOKTyC;ncT#M3}y%HMEH5BHPvaZpB@KK*jIm8P&MGNUucGM10}eG3T=@qssdOA1rypbPq;N6BL=jc#L77PfYU!b65tCE%_diM2w5uAiA^9>DUYvD}hLujkTkvVT}=231+k<H|ka!<qo`9q?j_&XfI*;Ez%Ty?vsN>lZ0DZyRtA<R(~P9b5s`*Aq1};yr<Q-8mr#elnRFA3|Wx=&#T?KFLCeG5_V6F5<W48^u%#&f92)f2m%5-sN+v^_dca;$pI_H9|9GeI0&8=|6u<=ktGZkoB4VcZy8Rk_a{IOWL4*LdKo2ycrr=Gh^yy5SugI;Nq9VH^`HYda5av89rQ$=n$u!m!foW;hrV7m+;WG(&5?2O1iUuhJ`vcG$5P&&dRi;d7;o9OKD4boJKh69C0l)E2QdF_=fv|q(WXU~YiFB(Ub3GM<iqHA!lVJiw5vr-pU;4~(whDb%$X-lezt&4n2q>>d0=O1(@*6Fremy$tfAoO?Qrciktqu7)!xjLpXTUGodUkgf9NtMt{5N`l<MvSyK>#nzZN$3=-dG})ggiB+I!K?5@48bc*n>e)T1#9;NQ`H{XDNVjn9kSo+;`m@2~Q^Tfn^{BPa2}OWOIM4C4x^>vBAoj(|0TOCh+fa;rS%7P^N$a?o;}k7S_HgOk;NTNgT*dyVsWaCjdmB7|xDATeo%_)u&hX7G?N9edah%JCxxu+K;GC%?9s`LBuQ+?)&LI5bs<MJi8hIyI44qS}HcNl}8@xT~5QMYi$tyzqJ=c;H_!ShGiz43P*x8n&2<Ew`|2LZ{6Xmmxx2h)Q}od9htF5Hp3&{95eubXSF27w9WQd#y$ip<E~~W1iWux19Z!adpH~<o-rEue4A`6ud$w6~a#XHm?hQjXdzJ2Rg3y4BL$LrqM=OUf2%|Y=Ap*3qmgVeSdVa<e!aP4vVA&kg=w&v119w7Pzc>aCIWEMwutT({N-=1U}MO#cIbW=4L3tOSBHBYMujI15pF|vqg@|vU@yWP}nlKK{3mO(YYoMTN~~CKo_^ZMl=z9xLx5kTLNcSt<P3F$|!1!()TTH24T^LjsPn!z6cW`bY2<rg|;LszyG&B2)Xu@p}Cq}{y8dLQp=|osdU$cN;efM-QJAt6^k+&#*R*zwLvNS?#$W<1b<pIRQxC2!?*|LmgAmPAPDBq`*t?;vvZi+-o|~Xrnr3>`XHFz&f@mOMP%D$b#V?bSvn8h$D_%B2<bQ<Qkf5%j+~mU(So;h9Y73@q=3y0?V1}ZTnr7f-3_im3)6qWC|X_mcDsXFfC{pPG=i18`^(qOlZWhBa?vQrfs=V61lBBjorsA!&0b?Zz?{!*wwNlbs%bD)`f8CFInH4xESBeU*t7J=l*wMBMe}yipbm*~c*c+#)?OR&cn!p{2W%OM(1r-!f-B%$YN}m=RE%#ezFl*dUNuIvt|0s!M{xb@q#8c$jQS(*R&o+vQF1aB;wby&-FymJvB`c>q%@&ISfsQmMM_)){pWOth7Bk?X$@re#umeXS{(l!Iq5Aca@OFC1`t@7-|P;f+y`6!{=Vu;%@T@o)>S_LfvCq+s+C~z{IU1YHkYcEY95g6M$Tsm&lN0nR<LAnuz|N9nsb;xE)ne#_NQrp?TcG`$Hv<Qmd!cf-n-mj4=B$-Ia6M{_Q;tbl!`(orC1kjmISSwS26wa2XD4!(Pn)~x~k1Q*JCx?<Fj>MrOmKGVudF9eQ;&ivFwX2hsPSm3ONqD+$y=%v1-wz+X6@nR{hhFm&aUgt*++DSwcA+rkc5VTdwJ><t3@D-J@q){@gck2&Q>kZsrZSn6|A=+iYf*mMa5pjZ1SdZC$!!F%U;v_A2tK**w@dYptV<>NPh^{1YE)xvJ@yj4M{|Hf|pN?4osp4Et=~H?f+NfyFU&Gh4~VAysy!eoWk#7Sei#eVNJWJu`zf-OWe?puIsd7&$BLMtN{Yr0fB6xGM`A&%g8Bb@q8T#Z_)@gsy$(GR$|Lp&C-N8TxD)=G{x<iH_ZAn@yvtXBpsZV5L2B0ni?~uNpTEuRQe{PCY#if`0h{fBBob?oR_Q%?8{vtN#g7gnKA`gtnCXu6N@eV8x63wrU>%;cK)9<lzOL0_I`!(&dHU!`XsXujp@B8{9G-a5LWw{*I4lUySvvueUG!d{k*j0f?Qr6s$YnexJC~;G0KGv2kT;ZsD?JqZZ}6fB54(;>Fcyzi>h34?4^qG+R;mS<D{3vyCkGdf4Fee0&WryV4pn<Tb`~;#81|$ZJeC5ODu2cZ{~WaDm>T`Y9^hQj90u_CNTIT&a)uENdZ3U=9a9`lHPYF+=3zQRiI~D8#z=JcVEnrOB$y&VEZ2M15C@;>>0T>)U{Xy|EdANBBYYi|-hca7gkukw6_nCsqtT9&u|V@?%Wv%L<dDV+YkVQBq5kRB0xub+k57EISBOamP&MY-MR~o)1ir_oJfHkN6bwQbOe^Wzit{b%Pf-Xe?u1NIa&2XkwLEK|2rT?C7WF)#|3nE-K>B!~b)2BH|H^XHjY@5ME3~FvCdf3Zj2uwai6Wgw8!t2Wn%Dcbt(BRmBsTs*sUzHYU%fBb@6u%XEYjY}Zj{>Ow|hOh*{Hx1xqsfTYZ6QbM*<i8&|mtgu&WNbl549YiH1%BDJ{BbY@|)E@=0*|qAispbaU@p$)KIsz|l8OTo^`sS(RB05wB>c$XxeyXWjLe;M)-se-1DSmQNwIBwm=yX^jf}!#Yxd@3B1%YrWoQMI%=$7Sw`eTTh;mZ!yS>W==^T=1hT|2-Jh+>V8p55Pz1ALWRl0!RSKR+7X*)n`-XwSxV4XEP9aoxDSeJRb>8OZX?xK^62_AN4!aLF{T>*Hh_L6$9RKy9g_Wd!aco%xmdHe_FQGlQiJsyg7IK)V1b(B~6xg48MNCOic~ORL&xJ$Mo)5t1{QsqF-Y<HQn5KP)Ce7|%}?8sKcW$9i`%4=zmt!bUL(T0>smG&UO=iG0t(Qit<^%j3ceVSU}lnhM>OC6*8u{g4|a^-$94xsB3kqpW;=^MZyq3Ys8^>D9E_E4L?m<vtkA0BnGK%*L|@*7nLU+beIDdnIx=jr%%#C3At7llHFcl9!YAga+mID=P?EdR$Emo!w#3UtC987BiQ1L{{9+UC7v5dGooY1Z$0<baL;VTS|ccLOC??+N79L0w1<5yeIZ#eRfSD%BVS;#*b4Pe~8>+9kr1io9p>xKBMC;{{^iq+~`|Ev{r1NX3XsqYf1Q?mK7~AxM7kI5RT{<UFmF%-~t+}cUf5mTUl<IMe2-A1N}J67nd_tU7vD?9sZ5$OvrCl^%i{!cCjrv*hEIU0$Kq)2X~ybMAS%!4@u!XE>hJ;lTPIV4(M>r^#=<|a<ycW!DPp&P6s7BH_)7lNPDc9gWk5(QdN=~0|D%HxwjD~fSPfsY%Q`@E2~K$S4l^?<HFiQIG&|Z8!xb^NtUHJ;%U7v3XBc1t&H1|BLh%{U~$Yw6m+dESPkbofpQogO<$mY#Pkxs;(FFd<!jd~o`i+v*`-Vz2{l)}+Z}bObyuvO%Aap;Z6SLg(0l)iPRrKJBht6&K|64;(f>RW39xz*z=0tkoi1&{TmX~frCnB5H!W>4{XNZA{G|Xpz&yDXlfS&o^{%gNnHw&cOYMmd&@FucD)1t^*w1``O<CYX_}d;~lcHvLS<!MUl|`*RGL*OgX;BzYC0JhTtwHh<wtsd}JBY1;1#J03c_6RiWHgQL!5s}EQA(s_n5Cy+)Pc_UqqG*Qao|pl-a_r3MJ`naTYRciHN$OV24RY%GN3MFl{c_22#8zQO00ad6^&3p$4R_1Y@H-K@uW}sTS{rhm9GA1m8<!pfAwmA`5wU@Tk6RJ^|B36BTKZHC<uaBzg_Ss%uP;T$5}pgDzeYeUT`Y7-ODYVJIg1QfIMZn7N^egs}X!BTmQhVKfH45-!9w<=g;o=99iLX$49fYTo}%~6Q~0u;OW&nz9}#F6yK|m6APt=zCQ6K#6maM-%AWs&&udwjhJQ!QGd*mxo^l&^+&eq$vAD$>R;DrU6pm`lF<rM8f?%5!Mo>;R_e{dXeF3g6^7!{QOKV{u-DtI#?7k1OQY3ciGPLNN?$n9ZVfZLl^WA6515T&u9f2`o=jJBii0z!IG&8++-<l@ylxb`*(iobT#p_x9sg6)^<p97r!-)@zjCbs3oFPovPqX_K1J+xUU{2r@C5qB7>xJk%T3c_@J9h5|Ktnq+Kn~M%h}-bl8xrS3Ck!viJ;=z>6jB^2BF3@fY5qr%&>ZwS6s7>S^0YJw28Aoj@g3z;`iF4F={!$9o4nAgttElAPt+O7$iiPKEV9I42W$t3>bziamUm#P;{Z(^MvPjlEt9WEzT<M$-UVFR4E<bfk!@-qSxFSk@`8Px}!;RfOBw(GT~z}$mL=6<vUv0Yx+gS$_`)O%8o{h^`ey>WI}udE88NHq&%({qjDK$r)k_EfqT}_-o0pOm*DoAUKY?y&8*b>I&+&t+xz=GGgfB}ZBfGIm9)^^PgNzfxCJ4i(cNA&y0L4$qs3iT<hZKlSFhcx4e%B?+wIcy)(f_S&8J44QrnbjKBfU)+pNk9)puTJ)ePV)eHv|p?%9OZitM@<5>_vU^t*hsc~PrHdHy~OaEE~AOW7*&1%NlmZ18w)Cei(4@r+-X;r^Az48ws#xs!opO|9`qU;>4gD{91;P^J#O`jsc{x0}WGog6$bU8CsDfa#RQs*e&}_OE80ePSpt*wn!}`)3W9!B1qCtbLfw@bxRqa50m9S~{if&%9WM++8X|hIB^Yho=R|xno_^vyzwFG~&4pYzcfwa@SJWi}K`z0%R5ZTCH)TO5yxDNCth>=M3hhsodDjYlQKW0L)0XF$NU~cb>!nq0}IwKBAV6LW~W=$~qNmid{{XKm-@_b%WiH*ca=F!+4W?3zD6{>SJ6tvA86TrNpSS4uWkW(5Q-ILaBL@(EG9O*t2@tvrL<X%=w2XItCL&6HsB@$nN%*rMl-0$G`qAMaO}>f#g@rcF&e|F!?Te)$Wwad6@gG(wx^C8~q6hUGg5VE@l5tMAj%G7vlgni%vB^QO9_Kx~-ZSrNjYVs#iUZG$!1lVmFVORNFq454j~1#aQk-(haDrl|HW#nT!PJK8(kd7tZuOEa?=;<LnK3qf(;IKAx_E8y@V;rf_oh<k2n>$Umu)?LhX;G<&r9&HHlmzLZhx*2AoL*|&ud!KoOjGCd9}<u0cRrPO-%+mTn^yRjvwI}h{QnEsBkcjAn<^5m1loRmbuNV||0r`5Aqk$5?+y@)oD6p1eFV0_|vq<^?<`!gvr#*y6%Sdv+m?3<cxk0slFWrRU{@faSXVd$oPd3$}r9UEygi!F%xBg|q8S0>yMTd1#yE$rvn_F1a^sI2NV8<x&chJM_H*#CHSjCf3}T+XUYfdwboA;lIhr&KP+87%hJx#MWVnc1L#!{p$-Hq@|rCe*NS<m}t0h5u$Thrz}vV-8b(MBdsIf1um83_b*Z*V=H_8O%MK1Ej))d|LBVZME>bG)3xJP@*qE33ZbdXqTYZ6D`?ne&*M`=!rjd2x9o(syD>K0<mClh4dcb3eO}gCI}QqSv0Mccfu+lVbO{q<UL^({5xS4h9y>^nPC++FJl$_BGlU$@zcu46LBA1J`N-&_2ANXib~rf6F7)7m{EMA@jFzj$4P{+_O?DEa7FbtF|F4t8C+h$?L?s<%=4~lC@+y+js)IcKnRRJho9%MnaE_4S{;ez{9H67`d2d)6pSQdN6jIY{#QLM@~@ahumkwG(ZoXi1Id3tJ2$Wd)hK*aYflOka=;>)BZ`_}JU5MLwb3{UvtLouD3V36jb=-<+Idla%X`rCdP5G#0tKQ#mbEu-6BPD(%X-n(;W2DgvYkwvCm{G@5e7`1$nbt=%;@g`y?lq&r-2mTV)d!5c>Db<Kr1KpgO?djzCK=xzGN$A%UZl{*BgUO=A5QWJElw1_36@eNjIHMm!=Ep()yWnDco19@w(a`)VdQc+k<CPOaxkfQj@U#6V+dG!;e;j(iC4%$1OJ=d5%GKam#@~>f8H!ky%5RG%sq8;_^LIit!yNi-6%@qpCZSsWNX<d)kj8M#U$M2lru=YmCMDE2^>Op^9M@Y;f(RXdgjA&iZZtBl(j<V7SnGD~mOT(T$P;H7*@kwe)RvNE%9fkg~JG9hT!>OsKTQ-F+2JE1{4B^2l_MZac<69`0#h*|^{miL}oxIYZcipilZYu`lE``A4`Zq$=G|Spp4)HRXO?4N&ZKNr#hy*5o6oAh@~%hXYUVMIi%PHgDDD&OWKg8f9*M9RCiwDNIN=NlJMQpjbi?kbkuef}sz(*tuV5apJne{O6GzDcmW(5R=)?b_dc@*|vgRhVFTxRWn8~uPr8bK2<}xq=RO`?hpY=M5Yp*_!V(RU8TLFkTL3>#riCcF;Ko>W5;e7C)&oOZxf}Sq+65Evoo%8Q}rAWg9Fx%i=Es(Uw;|^{<sVLj>q6*z()T*q5^(OcfCVYU~?%dz;<qqVfbE(z0XGlB9Wf)<H7LZ9DiCEe*9lwANbAIaQv)dH#3kcbvlL)SL|pD11dadOiNPi1s^sw=(unc>c~1pV~_II>YHN8*R7(v_`4-#2%^8@h;GH=>K~cBi3Ss)_8#R5oPLfdu0wH>&n7)qST~DFx=~zMM1CO4<H8|YW-g8*iqh+pNQcdb5(#9m6H>)G7T#e-!Yv3f6481K>M}H4lr;5Q2CStQY6qPBEz#iWmVdj^-dD5}4Qt_6<$I!&kfsSSPG<|V>z24{3uyvrc^RB{-b#`{5fLzTJ0~Li#R>WBVzX5Qo*Hdj-;d8MD%<k&N^wRk{VOA)6ie3Z8Ck6fCMs9m{mQF&-I!SF#>CP-q;*xVETx31)8OhYbjrX*+q<To5!yo8mkFWZwl&oWA`VEN$K=;yv(1(<WnWvRm)eo>7Jf%kx`@2A%ny;9B#*}%YzC_!f?AQ-l8ctHDjentDJ@G}kOay%lW_86*&`2zdeY)I0Ti??z}rqtxUm@zlUlDcCIK+~`=Mi<JkI8kNW&UaF=J%;Fy@Vdm4<^jnnjB6*O?yslM~tJ1M+c4WS`RAL>BL}`0yBqy%{fIV}zk!vZna1!!(Vw$i7Yet@Z&m*^#r9yq#qCcK$0DTF$r4jRYCoK8Cy}ZZ?7tSKrG9$_?|N$nN0yRqc?4y7ADxy|2DifjAG+4r^3EYeEL9@^J3KV*O$2mwTf4g>Y!c!51ORkoS^~N(-DO=qLo%m^vOga6L=P@*v*Jka?_r$eHS?W;?U>)nh2kyo4|C(5f!TiTL+ce-S?a_9tO?>;@92`tmoQ;cu4OEUK6x1)Gib8?b)Cq9fho=DxZUYYcCptNfP_wiIMTZg{|6y{SlsQ=9VI;AcFoAjZOi+*Z;S$p(2GHY^|xaJ+dT-1c|!=Q{r_#(Lg(@9&@m*$2B;f2dYbb(((1Bk%X18W4hrEK0y+g}RcH8Xl{?tM(f+&h}zzMTG5ls-yn9uD0nqfb(f>6I<X2BiczQxOngJDzLNIYu!6K@O~LM+=K;Kv^fVBT_P?pkUnKv=f~Y|Xw$$ovn}!?L@D%aayTFggVJ;uT1=ONkH4=C+2?P_V>vMXH?Yb7fOmhef$AZ4HlIgX9#eU5i31oqz2;n=eBYZ$ohiMOU=-F&h(+)k!AXqBZbbM96+}>oBlJH;0SWErESd7Z7o-4myXh0N0F&{;=!fLK4B$xp8R$deK^i{hlLLcWUg_@H$QwAwWT3^91}9N<^kIZju<B*VkDs@OK7nC)Ks$j-E^%@UG(aFc?x2}~5NVBO76&>=Ad3*E7^qY>5c5Nk!_jt=0F+1qV<Qui-V1L<A{tB@x~bVe$QwDGf++PC=68tkP>q-3Y<&<y4#dJw0;1Bg+A@otPyQt>5t2Jwc|SNg2<Xn!W{1rS(^~0r`jSx&H$wt$mHV#7rquZO)cb8T1>_zrgJ)cG)5|N#Pm`S0ID}#AR^JyWkb<uHiVrCEi9b!C%bMZ>0v0$92_**Zs4PUyWn4So*bjWQCVG#=&Z^#rk$3CB8hc>+f0t()>ACY4+Aw@qG5mmO*D%8S6!4^ZYt$4c-70j?QV>o}sy*Wr4DU^d?C5R$7zl%N_580u82rvC>3;!a@amHOFe~YQ7lc76>2Hoo`p+N?UKLBY7GV&VfrQO0kkGuUo}aYnpSE=2zyI)1gAZH7a22XxQNZ8}qyQTs0Rb#pcq$bOKmJn1!Y~I7>@0?D<qG*)?NqL?p2`)-AijhJ+)&!^7#0w$q~U3-QmEkZjfIZ6We#~8t}mhlJ{qdJ`)3eV-@EiB?~B7El2LpNMeVh(L6R`016)|f*G<kO9!P&H-J~1(LLMp8uz?=}pD&1j%aW5a9?8IG=)Jm@d>e?l5OR|CTx40c=*;O4?t%$9gVtvSh3QDS5!?-oegAphE1O6ZFf=8hdkFDqqMms+Dna{iI|%pTHdchD&{>YH^bwT~C!1AA9lC*w4#A)KlStLBCef&)4E8EpP{<d!o^M;~HMXoc$5mwWC#WKW4kH^szf}E)uK!7X@W5i?Exf`<I`l&xdq3&g&#K`8h4Joz+&+BKlfE34zO+Oh3nzPa8aqZWTgi&$Eqx6$O*xX>Y~OLvf(6M3XO2w80VxwS05G3Xfnhv!Pljd5R6IWBhd>kt9ny<|7%>z&#gHp!M$!L}oM~RVRY`yC?`h@54Gp@65gD=Z-{~GGTS=GPk=-iN&;5cv4{VS}Jg>hop_W+G?LNyN{<Z3p<dud0f6iAe_<#7S^xdCvSA*+^m-hdmc&X3q|Hu`>Vjfs!RGX3N!@^yqLLv1lt*WuEu1hVC;D2ao2>)Nv^7F&1kpDrTi#YQ6U=&+Yc>(*EbK0J9OWUPe>W=q+&VYJC{=do_ZB0N4%zY;E@Y(|0)r&iSZ8i&r@PAeP`XcBb_RLH&?vIDvF#|Ezprrz0`Yt2vj&VPv*Ep>5&pL~ywS-}$z>+O$wRMsH-71i}nZR7u$mfUHM1Qjld9g)2h*T4)L6j^v>488JS2U9_|M3-EJI~|07SlqZ<Y0hr#GbP`cn`-g<fSB^EdZ!g$t!V?6{vc|=|s<KL+LguGo8;L5`F<RW6fEcTkrGMZ?=9PRfH?aLa7`xyq7@N8YM2_sNKmRp_j`;x6~Vy8coBUL3RY0UsqI6EV3LF)+1KIOVXCD+ATB|5ge^?<`hi~3!z9COr3%$V7O7(ArS`7YyK9#HdXzqSSt+AWDFi82$+rj0#42&j0ua$o3j1-7pi|c_(%Th6r2uu-$>gkj~JIfyaA9XFC9FFFZc=4<u|zpFz(UY9c~1YXi_1%!LoJVV36@EY%42%qPHSRdIWL+2h>!aM&CC1!#MC09s_8>qtuLWdpIl~vl0k_pFm`>K}w*e@r2uMnC>S7Q{J|^h6mr^iFcrQ*H>^=vgLi?9p>E_duqdWqD_&Pk4Lpxi)WOSr~lKo7i{x3R1II|o%75_(1D;k4hbrw?M|ZWRk$yjxT)$^MGAN2Hi<Sz(N96dY%j@MECu;(UM}%%K#Z}ca!N;8sL-O85ejVNCCf%qyJ9iXq_~Cb01R3cbgN!4fU<u_K&m(KTCj^oOXlIQ8i5k*e(N#+mKdF&W7iWcwjy6ECOk881Am@;VL76)0Gyyl(*RUPT{5&o@3)B@-wX^eTWA4eqoh?Gz~CMTGrQ3^riRbwKmU<vN%dIoN=tg40e{Bf>o;&61`BE;zLbv%Gp^EAP4=@jsM%MdD}|al3Yzv*NW3}XD&2vRtUeTq=s)_qjQie?)NA5B&MN=}rQO=2N=&?Q*_dm@dK<__zGZo71-*a;Y4pnPxr`^SWAPvUL__L?=H5ot8ESUX+<ISVmyjSLd-Q>g!FXXLa5PHGH&}fH)U27l^K>V=Z(&j+_s1L}c!3Fv_Ya~v0_tYRBEv-EcXMz}Q?)<;4IWIdB5rRdEdX}>W@5AlK<(@>icG8KVRQqM5)GqvIgAc139h#E;POa1RKJyXhgK#RdB)ObEQaG<VpnO<Ui<8&z{QRGAjRoyj8K;IQHHKSPnC>|{+40&2N<y+?7D@Qqqc*UcI$R>gAmLGW*D+A4IUel>=v*Ei+D)yp7vp4@@>aBZ%xYeeD@?IL=2sP4rqWvcN#n-7{he~<Xhfu!FXS57qA3tPc4^xa!E-$hG;z_Cn|tU1Z72TOOcQb&kc(<8Qrhi3%gen3C%Wk(wa8sT*(F?(<;%C+1Uy*qC+ii#cD{Q;ADO=i_A%px5%~<aTR0kgf54U>I5~lwL3D%*Kj}a;@3Wi?i5|Ructe8UQ9>Cl@g$$kmf7IbY@Ca4FMVuqk^G{g;i8=`C*VD+Q8s!qTwkeqa%pRu__h(4GB|$3^SR8`HMwV)e%fz$j2MvQ5vQwVR8OrAF5B*vkqC6-e{Ly5jc&HnEd^z1lT$KuV>rdRKVEqjT*k;5+9s3JSu*uMp8qH1j<GEi4qw~*wQkd0wEx#Q-p8{2Fq69`$36V#JaF*{OnO?@w>~+qDZ6XnZ?gaX0b1s#q^#si@CEqW){;dvzU}w<cg={Vo$FuRA=&w=~8}?NvxmA_k5aSY^Yu6UYTNKi0eX@u{+8#IxH!ev0RXM&*mCi5w3*ObR%p^h#}&}f~dA;c}J$fn0jnWaA28zbP9AQx_Ph;qDnR_2N_EaatPEk^iV2nP(Z=(m{4m(8pK5=lKnz+1FclT2uMllD)b&NXC)y7*)YoR#KM`p#ca88C_|Z#9;zTip#_sKB4DY0CQpg*K<=Ph@MzJq;O#XW=3mUSmD-D~m<bWslCwl#znHdU{rVzjIVfkDTd(GsgHDd*Wj`h_J-h5Qe_52(K57>8kGxtfwaQju2qg@9=ahKEP78I8YAd>=Tdt>+j*h4$z#8}Yfuo+UdxHHL#zV3KPq~MW+j^5e#TrNPy?X*rnjHeoI}Y3Xe2GJ;$Mgg?p^X90i!1+a(SbZzfUwP`R7Zxh?Asp@Ypw~y0fE3BCGxo51VVK{byRU3-&-~zUormboY0~@M`!^UUx>pkYXAr?#NR!v-A1U_8lOOllRHk@;vx+(8h`+_)R2dep~3!yDQvwCBkquf5%7HQCD3ebL-lw!vRRPOLc;PvFvJ=4MdKLxb%WrHC~QSqlZR2~3Lp+ddjUZ7x(!pd&*xdAfuT#?v{-->Yrw!Kkw9G0w2tUTfg_z{?d57U?BRU2+z$=+Fa6t*NhKBNVaI9&u~u|MA0lxftFeNNN&RQ9@-a-BmPws#64yODp)Fgzz748taS8M&CaaBN77SvHDmWYRm;yB-^J0FJ7jrYb@)EIU_=VCM)r|x{Z-8-|+>9*<8%BW^Z1oW*A6!u@%)`C*>x9?Z?bl@XgU{8tZh!_Z)Sz~l25fRFLp4|~_G^%ySQ*l-WT7TQD$;<@gJDAxV5mQR^>6$O*V$*c*@vQTNOIf07-!xDgeUuK6re=(`9y#+Vu;tQJ}l|qVl!vUVs%cdb(EgW_Ck9>da_=MPOkFW4?~KPyqV}^Ux@}~m0%tZ6q@YaQn$6Ch3BcjRMP*eNZHcD{qq{>*43vKn*8@ZnZ79fz2Tg`XxChJiPV`5Vx!yUI%Uyp!|yq!=9;3OnxeUL(YHoS<L(?}wqSTS)vjT-ao))dNN=>?4=0^`JNiJKYGSQkgyiagzT~G^H->=xNOWg^3Y8+RB#jP`8VjU8!&=(0lc{u0Lo}vM99HOXtivrZ8$c6_>+TW3%^=f=;te(W5ZdMk#*;&9i*s(;p>aR#{8zC8^qisy+=940EB}Nu_-{v(Y8RP8989H^nK)KDM`q|5OQ+QWx`%<LY&)npUN!MNNfhrO17)qz$?Wrac1Ap-ldobyWbZ3RW&l<Sl%`(mK@OH2Xho>LA^*BwOKU7YR8vWs0vpqYR<(vdYh5rK{*&rAG3!s`Mrlv@ePXx>C<z1;_c88kw)7*7F>QAT2K+oQc{|05S`>@#6{m?1{~F3=aowF?fqIX@4>)AJZjb$#l}#2{lERddian!8y<;*Ve^tw$sFY6zyCUO5O@ja=Xj)nZU62y9_#Sn+U{B_q4f%j*6_Czbfv8afi~{VHvF1mnf3s~5CM#k}V{Pa`=Pa-kS$agg1fyT9$|OBg#bgMsYt?NG2ni6vw_r4&lSFg3!OTbYm?bfTLaHUU1nwb17SzKeL*R~0zdf%Jk=Z_0H!>F(1lH8eP^pmSsHb02(?P^f{<GIDuuLp{O&jQp40;K^)-z*>%Wse2yReG-g;jJu9F@j!)GOCsUhdHQwq;1fn>ZAn1&xfN33{hE?2aMqFkqP6)0_3`ki6MugQ>6fV0EB`HYSf(B4xv+c*Ui7zg&v<bC^_bTdq5)+l$z8Kh}QxpDNFY6(QJikY>xlBYl(=TqzqM2ePpNWmL!XnS3M{m6Oh2++&%*j6mqq80@giRTfN+2dljfTGsYdl_X{((aG%ru5ufdomEmfqXS+r{CVQ#OSDunjV!ZDsNvR67=q@^fp0|IPy^Cl1o5*&Fu>8)Dr5gzYKnKHs#wzr%+qWDZ-pWlKm#Sk=yeZ?JQ$G~4Th{E@1%EHvk+2GO3Zr-uPeTx3D06jM@|f^MIH0N)b+4>bRq^lHyy7)pcAPoPUU%(6|33~aD58~gG-ZF39|)HcmoaBpminq2iXHvi-g517?m1l>A&(?*Yrk}Ui41yvIPduP)=zxxQ28sc^|IjaK=J`m|%5{Z`pG201+x<joRp!)-CMbmO+$G?jOVa^iElG2KSO|jf}ckAze$?G>IC~-9%(wbPRTxQY05gKbF*vEfGweirad6m6a$NMfQl#>qO_-$wMYpK}1DpjPgG<zI6}T{pJmq(!H8hz%^6Tb|>Od1RuGV2hQW=ovL7NyeN(r(IS5JXRALR;wHo{#P1^K0CdC``7O~Axho%p4b9&Y(pcrcA@?94VTTf82?2bCibgq{1VFnxZPdV+B>ak41x(Q>E5!3}WEq!{u4;F=!(3vDh%$M)jl+00Ls_)Mu=KaQ&sdBC1|>H*XYhAc#uY7Vj|*8Pf!-3-JL0rjMKce2aI<)o!s!{r)CpT})IDqgi`m6e0z?!fKQ|0sSy@z;SCx}Y@ISo{xw(>fy9La-b1HbP`8VIda7%gzmh=E}mhbJZy#1|jYNluDwfZT+b0))3Kbu=<;i($S<7qBO9?YuRDG8LOvZ+-t_oaJ<kGlHQq$ly0tN+OLU&3)24$`H__KkHWx^Yw0kL;Oy1|&bni<%Y;toD01JO<#6!A|7wH`RvdDU?bgxE&BCXbfyvGp-DMSiq9~59O{vnQH*G@D3XzOm_^m!1$Vf7^=OcZ2{}rFk6!C?}jIT^dOC{iF0ZAlg+NWV`71@=TIZhFKi}emt(9tsfP1_bVPeFc(}s^0}KyQ+-Rx@=&@~30k_i`#=l^Cu$k<6&Zw*W?@d+cI$=ddahR7EN1wmFeYdx7?fIeKzP0dM3%|AS+uOGmewVlY{k-+>@bh%dx9Nl2_Sb#;kxYoUf%*~KHod=VrN5Ee)?fYG`0U%aK|62Qv2pzJ+iTzY_w+Ws`YprRMU6u4>FlobcKp^|@pkdrz3O#Lrr+`Ezty>)j2~9lozS2EOa4-m_RtG%e*`u3Vpc0}LwQjS&^_2|fBa7(Vq*wPfNaDxU9c)W;8IZ~<)g*v*)@Sgc?6)MvbnCr8Aq@kS?2ivyb<k^LHU3F!Yc&3sl*Ye>N@??>k{)|s)}@4fM@HU%IRi52^x5(pQPDoZ}F?61Lkj!em=fs&cB*&%-My;d$!L-U^;&gB|n#^4ORij*TJTMp3CVO%K;Y5Jb7)zeY_=OA{)jyFx%E@23TjwvXOA^U*)T@JJbu-O|$zyYA&yDOGi{TmuLOr%Z)92M2#~&yK}l>QT~>D@FK&tvc-vKtqPYPVfxljkKm`L@C^1YI=33{>g4v0#)kcMcF%>)R#z-M>7+V|(qD?9%p~T3`PYaE*w=c2&nYFO56d~H5ACmCTA1FBw-*ZIN$$^2$B%DMU!49u{%u;kt=zM3$2&hg`Rvh7o=f_KClBlF63^Ui8Bs5PJ3mi#?#1c1M^8F$^JQCk$pD-_uRTIEoq+j=M{f&N>G6lhpBVK=xzF;#I~zzkK(D6{xoq2qQAJ^8;6?kbJNY}FLHDLlj;?a_!q0ALywCB4KiA9Cw{>|D%MWMY9vyt<Jn^+h+O7KP(%VZ7KL2~tEUHki=FL7f?AY4#AD;iv&u{7Eg^6RH{PpGUA`$X)?^dnnUsJ7@SU0h()>|D_>vhN(MK`O~+p|i-L3<HMsyih!NdBQh*+k-q2j-*>2IT=)XyaC`uUF200pKuKRx-P@BoEMImgLoAN#4O=8e6e9>{ylei{JG2$gbd80QGk&g>_8#^#DFdaBjZ>cPs4?->hAiSQ86#*zb2$+qiI7#X^N>Ew@D`vn?%`zrAPU4d1PP8_oA)NU<knv+r=PNJM)jv}f(ufnhY=;*OEcyfat`@bWio#M+^ja;O9{G$V2wLM=QA^VNyij}|s2nMW&O<j9B%$V=OR@j<CwlpnSnFrYR<Mm0D6Mkg8Yz?2pQ1RAi7j$>vOlbIDPqU=c03Of}2(-OVzNDR<Ko5-+jn;@b-j3H87i1@V;_k=S^J-o{&NhCuQe?E$3j9aV~kp%b&91n1#y{&&iI1_2UQ%KnvE17eCEb8~H?#=B$+GLS>ctekP-3XvKI$L3XP!@2s47qXu#5_`KY6JhfCk9}0*Z?5214?7T0GvDUG2VkP$bFZK*YN1mL$#-;(G7qhA;AwJ2As8h^p7U88sdYkYq_iY2ZI7Ris}fjx4j4cWm7EapA<vL&Tg=M00Wv-t|eESmyMnUTf+meWw~{?JKi?&AwNz7y?t<>)28VU7>~fS9^9Iw92gq^%T>ylVN}Khzf}BT%|YWuFN%utsfZ<M3om-U$xcEF!FFG8LG4fk)sSE%iKtk`S`vp~N$SX^?j{*W@?Nrq>QKC`lfwj#G{;js#c`&adHUBGB@O4+bLW&yb72cF$G9?B^_Ul~aw;n+Mb1b#TK(*$MYJCL>6xc13hXIujM;-2N42=t2_w}qetZ&Vaz|$`F}*dSXKzH9;_I7^oGE6GM|u-KCD6s2*&KtP?93t|>Sx`QkH&icr(dYxI)Z|QIXill?m;jfOQBM8!wqI1j2E47lp0GH7Ap~}H3aE`9lZ^d(-RtuoNFEHlai!%NAMO3{hEATEGh(AbpQc2JaXs&!%9HEgaZ5mE=8>7L}Gbh&ZxZ0iX}iebyomd1(4>EN}YV{36Lz~MJL9Q9Ew;MP_ZBFNTW%I1UCzC#KhhP;=K&i)#&FYsXKnizql^;$U}bd3)i89?r~+f-*vGcYPZ^P139uEx*7U*<%AQDtj=t^sidXThDm%-T2db@@IjR~v*8jrs3osV1uDh111ngbB>Og77YrVeEugs(GKjlkP}l&NmVIuAmRP$1gY}D0;Ili}3<ISx9QXY6A75Y11x`L-x_ii^ajybYv~e@z>*iehkz(#FhWWUPWZ9O$T8))mf}guNhFSW#1#}flp_d3<&NgkL(odS9udI^Z?@^IgH7!d?^W*G*JygZlJ!L68?OH41-d6j>Zc*u1s<LrMYXQ{mUp!YyZzj~S?A^ylV*S4pW8VISQP8z26|aJL^B8G)@`X3gB3K_*5OVXO_1FgEY~MYj2DuPpGbOg}Y6VDKLZt3gfW$!Fzg~bXveK;Z*R@BIk3oJXiSnW<vRx+*U{+*L+;<dROVN!=kKy$~J5&z8jg|NspQnu=#Pt)y4!eUfL_d%b@#Yod9YlR$L5@o%fJ^+i(~#d}%atU1?pY~bN;Ph#fv-_N|BKaa)a1>Z0u(I$<w?-HzP3p)T$lvy`j|PgD>J~8Bp{KlY_8Hfn*kR81<`taq}aQh1QoP0X41VU^MH$Z<f)=#`7sNwY-&Qu_k{_uXK2-geG{<MJw2+COM09ccP3dG(y=3FatBYr#MW3V05`lIXMi{ic*UeE&a{BTtMv^c>5O(5{IK1zL(p|v%p2&KmZ^hzS&a;bW5sa%6jKMRJwIi$=bpCb&5Qg5uDxd&{@4<c)IZNmnl+0n$u-rblSxDP$jNSTI%7`g);pTZUsD}qRTR?B%^NJupkXrRj-Dzl$FoN)q9R>oDf^n3-f03kV-4#rQ?K^tR6RvP9Ec|NO{oRAW+v65VP~C8NH%-QG(vUG;8d-!oK^EUr;WtpfTt5jarw&AADhoMNdYByZo+|98`WgKy=KB`b22qF`{!vpD*+^GkKv@$H_rF1dhv57f|9D_x15y#`)NOeoaHCb@&2{z?6*AgzRXrF97)8!Ht3LKtgNU{4HPbG_HM(8>!J!rnCfdh$ox3)Y8FGq@~@$;78QZB4@;xo8KWnviEiB{st(id2Deh+fv4<AdWpEwW|Guw851MXh5z2pob^B*K`;aNn22PIF;_l`QvhW}FslxfHYGK+BjFpWXBBr-U_f=VlCA3yd-8tG!Y<aqv?WQn87Q97IM(iwc#b7%4J(Ti%ZhszUswrih58j_u>Y1L(x#svX;V5U2h&`TgNYYNo4V^sn;McfEk-k&G?Bw;b;9AahbN}g>BQl5`=Uk+tI4*Zk|e44a#RZW(_(V+?xsE#i;0EFDHbNDeC91&KBI9`6ePc>mwGWZW2K!WNGKVDo;0bYV<x9I$N{&SD5%B+6%ii`$HXEW6KNGlIEL%jMBOAkZ6`GYp5!|hRb#MrZ&5(WMZ6Yc(?TyMS^(1OzD(<hF+fIwV=UxMHLCeylw=HAAjVVG7^<O-k}+{c#Uv%A+=&{N2}Fi?s`WXs7_lP1UN6QVEKBaC{#Y-D%jG4p7)HTAD$~-hT1nt0<ks__u_VxeJlTrl0;&R8P8ks8hJ$aj4P|!^EKe&Xd)Yq8cF}ja<*}TI^v`1Q=D^wWllGR?bBt%FqU;t`$A@T!Rm|-wE9Dc#WJ2Mg^(Pu87|V>{8DRBcEgofjO`us0uy7se5J|9&hiLCqqsPZVXfs3#Mk5HLuzl{^dl<Rxeegkq*3_0R$@(Z@kqfGPban}tXTi?Q)83EYGE|b!b6bUi_Xq{=5&xS7`}qU80|d%Ajp%=&s4#hFM5?)SL*YHoOL?rg%8N$8MbMICK@7brl#y^CaXBJAxUamVZ<^qG<6{Ro-%!{dKuw+(Ty}o#4}(Fc@-%~w#CRqM_6emi8(l2p)YXI)V0B!DraTbv6;vZ1@}kfDV2G6d(n2J45*GzH!LmCtn1f*)_2O=eMS`D`9tVT8iqR5lUSL&#zlK11VSYy98%gv;E~BK}aK6CJeDRu?V=|DLAOGfS^|m`VYG7x8nm{`UKMuweLt7R*BktLIEd{#?wM3zT!uH@wB+P(O1SUChw}T4+L`e~(94p?WI+~J@A2VdtAUMch(daDtgj9-nPl6BcC2;jhal%FH$_D!`nxpbHH3^j<*}Oi8HEKRoOTh;}=@7Q(bO<{Wd{AoCsTut!_&|-7;I0&W;6B<)@PYGq^}f^|KBxom$ISt_CHKHtntPFEhB$PjxzCFoL7c0G+xOlKx^z=v`4bU#UVd9ZH=;CljPjneGz*e-YC&zRqwrxge88|ndbACNoF;c%hsZoK>pTy*J7<x37y^Oz3pj{5xVnnzWF(nlUfg>-)!mlIG}H*l{htrMHRjp?c~cNElOWr(kl$^3<kI>?8nen6YcM+gsjFS5A3*s9tL?#PD$Q@&;$C`5$!^?DD$E<L_+_NbBRK#8LG#8#;b3`8y`%-T#)9*|=Q^^<?ZG|vCkxyJTg;A65KNY#m-m$0V~y<!!9+Q-BwohiFre%9^e7r>W`O`k!dm{8CheB#+@>Q$vZbX!l9-lP|17^H-}N17m%3X|Hg~at$sozk&Jz9#idP5b_6MR>uw?w)6+i{iA8;}JHUU`uBVYr$rE^bblPf>p_o%j;o9y=hV?d7W?9e{I7s!qB`3SujaA$`{G~^F>h6iptkd%19k-sNj{oq79Epy}$CpiY0=_Zmw^$+_;-G)6s1cz2ZGNcDs8MTbLd+dQVrSBX`Mu&V=ZvFXn^JgaJ@o+*PRfBC}4>S_mD7VdlQ<$v<5RZS9KP0G;k;vyIa<#=<|EN7)oI*~VM*Rl<lPK<tGK{*~?V9WN8YBfks@L4fIYv^${YtnxskamV9f^D(3W>w9M#`)!Mh`am#$Ztq$ug3=R7fWW@V^0aMSIGes#xgJW%`It7bZh14~U17yA(8GOmE8f;yfT%endzjKx~_xBi*ZF8sS4Bf#}->N*?Rm*pZ3K9I`5!ZVddjsGl<@?Z|HppfEjREf<eav3}p$QrILqg_l<6w57&8!8vWo$<*K++&rr-*}W%iNzb)e+LG}V+L97P-bGmh*Jw)?J7WiSBTx)IF<CZTFDwZ=qnX<ow7})P$1x=!VM(;AmUmDbQ_w29S=KC?MIDG^amCbFJ!@(VGhxXV%1IV*Id5ky=mtS>vn`B+uJEsg#Lo-amH*Jz#?Ou!G-}Geux$=47zrDSA%MmQmPfW!OM57T#))@nT4)cEYJ(zem$X*}zuSPC<#>K*H-1vuo?=+`Up;A2o}Vt#K3~5uV=gAtDj6!QXre=#AgzbJsk@L|v;2-TjGB;&hFfx0pJPe4+V2>stS=<pj;B;r)Yyn&sI8g;x=pPGwRx>*#YK^laZ*v!haGm|%X3aVe`J@bnM)8XgUf-i(H2%J#Y;j?tCduMQM8kTWe&znLu2`gX^f*!B}qiTpd=M65I1J=Ts2Mik`m9ieRT?N>s3_+O*E+?QVps63tntW&FO4rDq<w9qm^fA70IQ!0x7fNtAff~X8kxMLb=?OVEDk(J-7Maw_qC0Gx&$FMK$PRPV@#w3l)Om&_{BKx^xTMO&pewkM1U0;43P8Fl+$iX(1T(q~IRN?{;7L`$q(qU?JXMUCA5F1CRVN8-4d&X-17W{o@{E7G*@fVe>#uPJO%fH8mHo*WbD?odQ#w$6}P*ni$WZV|dX=?p|>%_DzI$;{SJrrvT57RIAwlxUIx4Wy2^)Ch|hWp@GUt$CZ3E1BTg3Cu8J-%Cr`^C0gdCrLEr_r#<(^7I-f7aB2*|bGGD|s@c-|lGgO>n6{V%^_1{zU#&H{F3^EN3D2IwzOMq$;O#9$MzI5BZ*t((CzWX~?yPYPafRTHG^L|2%TUpj<l;gc!1`HDX;ete(~=^pMeKH-fpnLUGr`}~M=HRKFMQ1G;;&SH&Pie>{b(f;S4aTMe?EX?crUYe4fpNw&dA`X6c35RM_`;>AIXljQ?!tRf9P`(c7czL1X(otBf<N7g7I6i;0@UCvU7m(zVmgHy<Dc)8Cf0>j1J8J2~%dTpr?{A1au#T9ps><v9fgIAF*IyB)0I}-1ogtM&8FwfwJYEi7>d%Vw%ONf^mWk?mM8LB)e<`omUhi9`s2eBH5Rrx~GTMG9I;sW@V7VdTr{wgv2B6gx!t_d#*T)eZl4YsiQ37_pZ+()+LMhGv59FSr&1)K8yIYbE?O9g5cC~&hT4~brfz&7=HDNgkiq)_W*fkws0=`65M@!IaNr}7X~2xMbVddB>K`4O<JEx5=!o6tjtA{@RHU`2;vEy3BACjUFj)Go-h`PmrcpVC|fw{yQG=E%W1aoOL}pq*+Sk?QFDpMQZ8{R<zm@FAD>QBh02KfDO-3>xP@tWR?R#xXZX_&2<){#mp1fQBn%t2<Wa(~J5CrflksfM@MEj9{9jkc4382IHG+{BZ2%-xfMPCi*<%|3_QQDtU<?JI8z<<~H8#M^x3M7mlfrxJXQBa&189+5Uy24$xAb)Pw@`p7ct4d&xpUh+PL;QhyxphQy8mSEFWY@ysYW-TWiT;m8(lGTKtNXKN-lwJiJrHitKi050`2?$Iq*?ov%WRiXi__9i+7z7a?TS83>`xs^1LR<#{<Xy(mS%NvL2v`qC-~o1mo;S1pq6|>TX#;QL}|=XO!}3soxqW`tpSqX$Kk4sgfeSSV_^NPx5lJ&R>xqyk?2ShGjg8qpOnQR+SW%)y2<INfDt09w>J(R#Mz7D=G3YO#j0h59b>X=NrS`+uOGmerw^k7JlR5eB<GK<KcYc;e6xa{GG_d8UIFY*f$=|kIcjA&V3lmi~2qAa9S4nH9VZ-i+beYe2#?E61J(Zan_1=>=3|bW||bBs*Yo}zh@$y6iCV&SB2!$7)>^jzwwL(E_f8ZQK%Ws=A4((&)E^rac?ddDQAC2zQ+aEqWCSnBJGt?GDZSj&vHwS<dgB3HuLPi#r>0obbJI?&R~TMalyJdf1>lGpibO$yabcvHmZA3I6>Ibi}Gd0NLgs{E`KuT|MWJTih$AdIE7<yBHJuIZ~bC@anj(^57mR>$qa>?bQ}PnREtN{nr>1noVYiS9!GCos7A_7;tuAc$ezNv^F4S<wz+uAyvIbQ>hwt%3q1;(j|r`f%5eg@EZ!c`Z@LAsp)m(OL%eyJ-_lJ_ae-IUSI^LFp8nSL=b1Lovr}HW^mDA6g>^7pW=g#LIEIvY=394x2y{-T>7S+UJb!?{NVB;la(t2a@!|nXzQ_4c@qWSCxctPQ9xx|$eBr}#={X7K8G=y%9GB+NF-v;P<AHrlt?9358TX18XHViUaDm#lvo_HU&)IS3e7WP>#ZQ*EI(z*Rf2OwAWB$zlV@k%|z7CQ5<&2HsdHxO{as|h|Oj+XvtUk`cDFJ5y)YkV%S{ZBJ`83=Hs+X^-{~2>|tOz(mToW&_*0f8i4w7X>cNG>F<RfFv&lA)B+n3XD0LsSQNGE`2U(NYy>Qd+90QYsFWT7vS)eP4&0qk(?HPJXq3n$gq0&FAF6Tnhu7#r#+m%JM)f<83N<_~>MR4uRw>#KpaqNWL_kXnq@1*DdU*;7=lL28|NX~ZHif~e~cj;d`9u2E361}ZgffqVnqWd<8pK(+=w750@j;yT*&q62|6^}8T!3%oXz3&mou8T+IG#|&zlibwH8520c4$TLveSfI8Ip|)-U)*5l4$<h{RE&kUnAhoM=kXkLw=G%};>WCO86@dKLht%%8;c2zXCjo`G@*=Rh+`WXPt&J$e+txK}0jGk&2}8?Au)ZK`Fb&ahmVXQ+ZF;L)eP4B}vDB^BU%zfO8bo7zech@nb*s(m>Q<B0tqN#jeP^K3Qnxx1vAI{wq4lhE6<`X49Yhz6z4@rBL=}ef0#-Q}pR#)O4_!_9O(=Ta`6kNmc#iLT%fh_g=YK0=`UWw217ZSzsZb`5`j9Nb!=oDxMe+Vo<mXf>CqkU01Xy>q#tkhf-rBue)mV&RxooRCxbAavios2GLpAeT*ZiaJ;VG{nHXn|N%@f?R5m$pJURPaxjH?OYHot<{yxDls-r(dLOlj=432dcJhZ+EAb4L-AR^g`VK{^Yr%yg)F)}b0hLjG1GucMd0#_m4+Js*5zbQM9HM}y<Io$|812h|)KX@ki>JdjybV<kew7;UgeeHtnv6S!+rp9h4y#ZHBVBM*)?VkPgrk$`_ra?u`O-Mo-lDHm3lKm6gIyVY~I6kPWjA{gO$eAFl7Bh@qR+6^doH8KVX0ThDOcJ0&3(S!zuTBD)XXvpmmy@iDP3Pq*MF_Ha(j_Lp!6CH=0f>hb~%O|^Sv7zPX>ORRjv22pt**JKdtrp;e!4A3WNs3JtLcn%6c{-q|I;?!&DG3I2>-+ME(ELFeOtxu*y1#Mp7k&q<6Px2j!WZxzN_uB2M4C$<1it2&01McvY8qQ1x-uHlO$Ge0_xpeX`&C&X{G}D*Z>s)9F>QM?ZKrcg+o3RRlXBaMx>o`P>HC<RZDHEZ=4&E2x88u7I;r}5K!tNl{5m`u=bAwj+F;!l%{Hb^WK3UdQQ3mYH-`dupTxJ_ff@^rtTAw_{uxcvaw6vLtXXIPhHQ9qKy1tC0X#B*dmD)Jx&q}k4;DjqzTw<<sjz5A(VKyN4Mp^k*UD~E<Ma<^Ss(`8euCyk#ZuBIodh+|R>5u_L|6@ds0I|%;76`o^;5npR2l$oo@eae<zC6m4;H?dP_V#H2K17^|2_Gikwub2mgJnN@}17pEi6XR0|c7Hy_fbGyU_yNs_Jq4OW?onYj5%H%83Bb#LhTk6H_zz3f3|RfD$87r0%xs0s{|=8MbKat-@I$8{;8bd2tNJBB#~5QF92Mv1ci~k?h8ioWD|@NQ9uQbA@H=$D%-y-bXi{+>Oo|-AP}ZHX5`fuJ==tYjSNDe2fb}NloO7v#1lcq10l=nciISR$bBS(hc(wym@9i;TY$fyltrsRIc#uS*F8V5vR20ba3Q}M5jOcwdMZZ$=~4oOohkO;E&~^vlla^p0OQ{!;j`e2YnlwFexBVAjEk;E5`NZiL9{$?*+Hig)tr=syQ(v*n|6-pY7*2S-y%KoOP_GJ0E2W+}NQOFtE|0ic(*+{FHw@8fNAEBd4W1TYhRuobusRmMRB2_+P93ZCC&PYL_Yyq8pte930erVdajfjBCl7m-nR`F1y$VFqPvbV!>tcVAzW;9ovX;Ig+CQMWsxyiL4<pPn!*n6~f4(Ov~G**wI)ChKrh@gvSP8OlhFfT4Ok~VUWblyI0(RoFr1eqh|)vm*_y`EeZb6Fd^225J1&!u3MkiXL#2L95k@|pm72MF0Md%Z_AI*LUqcbaNEEhbg)!dU6~4u<A)xffS?SFZY(6bgJTlJEg1Ppq&I=mi9K$Qiy97wso~rM8I7@^{H^n?@VO}XkMdEJUnE^fOVXU12a=M=QGals!zcw?(4H>>?UtQBJg80$)w!EnA8HHek_(07euK<0x{OHs{@%1e+MQPkzo<I=-^LZ@zkYYsqTG~>{)J1zMa+iVihHO=WJ^107uD3dz^bLfSN2&DH;zl|itSW%Y&^=1BiVeUJ(BnnGGF3KEd__N+1QmFI<~)7Q48D{e(O!sC{hMW6g`0pPb4Q>t27WYFn9#;$<$(KE1^P!!BE;B>k_ymZwZSC%K{#G%up59)5_>n>{R1FtICfS?gP!Hf@U0qT!(pqFzMu2RG5R*%HH|DFx)v44Hdl+swBlvr0{BqMw$o{16gf7-c-@P!IZ$Lj65=lsW4yQS6+}-nQ}c~dqR!R!4#KZGGtGuV`&w`D%mD)4@SG`P4CIG)2fsm9IyBjtCsE^2O}N`^yuLJVIaq6I}iL>Fm|li$3P8{=Ru$6AFd4jF=!|~+Nst$71l1iMMeF=B|#S|WSLS~e$%+{-{P($C8}@5v&eZH7$(FD*71bO=cj4MU{`Kn*a<S@bps$M;y@;lK=E5|OBRcDN#E%H{soUyOVPHG#3?Vv*<-s$SFCo9!XEBRG8PSwzQ3*ZI2BY25^L-as<F@gbC16NO0(!5EjKu_pg*8sN37QQ47j7*w+BqT&%sSurP9pc;yvUhj``k(y;-WLu8!_U_ZWO%<PN}Q5?2o#u64D~H{Ti^@K2zeEA&4hF*U@+@*{sQx^M3|{>+%eX%BoIe(-ujHyjzdp;);=G);Ly)6TAApfKZR=3g<o_#!S06|;e9wW3P2H3NjYRAhTA>mJg6gRGijj|CRvd6BW>nFbJmU=>%*la~e-(LdZzOPV6s?8frgy2XD~qzGg9Uk$?6^TqfH+VZv9usmGGj~ibswG=IVFQPH<*O9QYF-vSxE*2F|Fmu$EzmBPjq|d|5_?gI5W*4Hxo60B3sK8{2<v#t)V5315O18(1BF@eVnWGlUc|OWSw`LcOmJ{`}4{MF;@-ts~KX2mEM)jdBn!;9S>}*}|yk~31FmbTY7*=LjI1+BQC2MC_39bNjM&nPEC)EgPYQ%sLi)M6LHk6}3vM|k1_cEl(ZC6+3IKaDg$NzDh2eVE^xPog8|M}JF{!z5UyQiKxYd24bS~8N{hm;*ay{)^qEdNw#yZ8R7sqVNyqy{mui$%40eiOQ8@*C0C{A`8tTT;T!bOZ9hLFH^VFuR%F2Ca{QHso>QJ}TWY<vJ*>f%#EarI6OKRCYj~N4K;UagP!9<2LXhcNOLQ@L|i`NVdH8Wbj)%rrPfc>7Sc2>0NDQtxwEpG-E=}`Gc=o=;kfNDrQ-QIbqEQNGANu5naNMEa?&k@omiL5<V+*2}7YvNEb-g-+?ZnBV9ryT|zveOZeg3<OcGa7!$r*7!%T*F(EDZ)qf&XbrSdFj4r_=3jtg(yLThky6`46g*PG1DAorHUR>l&NXDCB$drjXffVb_dG-W~VNxAtq*y;9P#BoAPK9NC&YrMAn@sEpO<_+k6U@R^N=h+$R;UyDfbnJ22_OIwsULSBQf5k}mKiujmyAOJZ0+Y5*VBwc0f9I!Q7dQ#oTE{QFAyl8<$a+}NYxh?=+<wpqgy|wPDsbp30P{kBwcs@8^fO9+_fusHcWRV-AV4*%Yd!?a3f~x9EIWwya~*D*9w2VGjGBy@g0!|yUd%Qb)W1B-6h@xl7s*_zzOG1sS{pBnbejfav)=4Eqk_`h?8DLq!_2f_o@&!#~G_aU%*ldB1UDsM;67}2$eb`RI-078u*F1|5s8d`ohHa|F`$;ypn8bR<R%Pj(ncXJg4eb-@ZM42k0Jk3k|5Pasd-0kZ_Pj7{eHV7!62Bv;YZ&hXEGz2f#oG4<R8jybNqygvP)c0}J8c4D7Ymw<98-Cr{O_y0>SJZYghOp3KOI9sBX^Z>?`FPYK0`)uglFZ$RDw=a9BKHBHDQBQIYgV|^`*1@ozyApPH(1l4|mWJa|Bpiu`n)=K1+gCM3sQ0?=WV8={*r_!e-TgqxajT-H+)1urGs7Q@iMt6u%U$$IDElqYNambW{_*IWT(Ycr#8~TdIKqv0TD_gl05pJNYk^-len^W>15!j^e*&A@B&j3HDtw^h<z7ho7DL1-?402I3x!xA0z7!jre7$yZBIx)<3B0E(4U(5;qzrLfxe73q4-b!(T$m-COra=k<l7fdF>9ba_f0WQ$%FP|rkIAvLA<Hb8W=^MXtSLQvz1hszB<L2-x;)8qib$!wMJ&IJdMx%kvto>2llP|h@$3Tfje0uD^!wa({QfY+%wlyPK&$N=zVQll$lhUA1xR38OjDjUg|wjw%J5uwo)S51aEV0Lv3PzH_yh6x~*yYhy}z*Iq9@a>S(?go@3jX<>$A@w&~VK{)gN9#>WGMXz!&>!}gF1vA=A481A+`Y)!@}v#4*|9+phonva`}m~mY`+*C6hS*1j@$w^xP0bl!xJ-W=prGor1`=dYJn0X<Om%ZDXGot8_dt4<Uug2uX&13Ek%eI}Pwh_$_U6<XBP7T`3b#4%A^~~z9y>4~b-p}X+fn&zEcE}E*HMA5I+3oPE(4nOZ0HQFPTxM;&_lzap6CdnmBc}drwukkLmy;KWe$S|y@pz!ToTs_`c!$HgshX1hzO<H*s)_W4m)v(A9|*hFlxrN^-J$D|TW+>R;#wkaIDb#|0XYQ?{{@W?Mb^wS_3qeoBntbzYC6(ps__)VinfUjd|~xHIgIU|ElkLcBYV+NrDdq>%1z%9_iZmE!{0fIVRwk25W}VusEwsW{a+4_T^xD};ucWmgg*k3-4y@b6Srf+I*p;8Lcqf)4NN<Msxfzg^vNeCF`npG90%$1N*ONOM%Co55YIc1*b}pz6r?yIh{#Zv`C<f&2uS@dB0g=_-2R8jfuiBpF>&*l{Qxj8Fc*(NRla|b#^*hUGEW9+7JjkG3dNQ3^?aGW#h4B7GH~S`ZS4m*Ce>zRXjn16AtWXBl)rz}-W&L>V`YTz7i3h?*kBCBDosPHym?@g?;eal16}17da~SRm?4(TAW8(Ae#w{~C%%>nDNebeLcJGdnu9r_!MGo&9diC@tOu(eSnG;wz#?g=3=LbTA@*3)B2%BV+kzvE(7>0v2`lqNtMUodDlOv~?g@rA`DLCI(C`?dYs@kljd6w3ZeoDf3`#|;6Rl+=8Q}v`Y8x29je@&t+KQyvZehbXG9X|+p$LEa8R#qBkcW79a$h?bmH?e1z_Lx9dynnRAARs&r*6dOt2Hbp)&!__JBayjA24sHCE)N7IX%J=8JNaHRuw;BBIc5qe%Af!Lx{#40i%+RhD4uKt}RA^kQ{#gk3ALp9eUf>YqU+rkCoNw%68E@=yhfL_?7LJ3H)bS)}Hgy`n1cMWoNWM`fe|4f9gAhA-rFach5!j8j|oms=c2e3141B63)z8e>oHl_`rbkCNQBUvh0qum)kQ8;U4Yf_9}+JE4`w?T#<#{WCiAC1|ZZ>U{)!ZN7H)wZ~4+-1ZA}`YL)Xm0~3ltNs(h6<~Vb0CG8}G2|)}+A5W#2MaUqMfD=~v+GRmz0~5$TlO{9q1o9Mo#JFkZkOFpUL24oH8DOC_2Qn%%BZiv9nTI*Z;LWQnOEk;>_zs-GUjZ3Xw<&qdz@k0oQ9JTi-cxfOz|IA<fx*CM1|0sTS-iF({t@C*Z)iZ(%A*xQqB6npYb|?Z2R)&8$49f940Ihs#n3?!t==c9```$bG40K)EU{m50!i|D(#Lkj4ytmOZzfw;bK7gO<13R&;92X3B%4e-S>yw_o9Ag;h9j8Y>|VS9EVPXXZZehKTiF@%xI5C5(8ZW7+jBn6^a@1h2TTUlC~fk@w81_dlQyGI%<DX40@ZIJBu$gcPg$;zF5(AMp#oweGz_YzQujo8@*@XZ$<*1v)tRPj;OcD<45U82f%PmYH<cS!G>oEa`_Q7<8{UMzDHQz6Hwivz9U>_p0TuI{5hX|!(mIsq-FwOl8&5)*O6ujCiZT_2C7!W;;2;-tm{$1>{FRH=XVZEFbc}9;+c^9c%o~}eiWrTOdN13sG-Yj;#n$_#LNu}|Fsr7kjdVT(VUsG?59tz~*nN7}bVkdpe!utw5SM+Um7&iBWyh7Fb*>EcA5j^)`hak3RvEgu>1bMAb2McytLJv6jKUNo#=GrIxAQ10Oz7DDc{@|gLC5hIE-F(uKD`9_uND8o4L>5Qj;l@e1_J{GMdk>?JGXt}t$RQUV3B5oPTWPuyeY~jo*v03*xRmGXw8cA^R@&Uh5SM-WEC4X6;d}0zS76yqZufR?%Zv7G6W1LK<HO{%Mqj_Y!7Imp6SW7fnP2$=cfKRz}kTBu<QuSN3q6mz%;L+!iW2OPd<6tCC8--Dzu~Y{s8NA$dPXguXj|c`+r_cfZAcV`T_?+Cl1uvyf6Y={vxU+L-`NE&b4LR++jM@9syfMn`#<z&Mun{2|EXMHx?I6hsygmYhqNTPu7|vEJ6Rg({YJGyUJAy`+71Rsz%cx2mA3AB3inbl_!3KHVgD+rsm$MdJ?f7?OXmLHv{E)W^qix+Y|tv@3*%9`iDood)Bq9Yuvs!oD`O3#4CH#ux6N=p0Edj%vYjP4A!NA<*Xj%Yt5E*j*5F^sG9aB!^JFuYZk=I135<vk~boDD{FQ)Pr(hrr)lt`{!zfGm&**+5j<I<bIEWZ(!^a|Y0a)Ap+HUYeXaqMNmV1xB&=t(NrA9~AvhKH1ra-VhdRpaNx5)cPrt-wOfEB&%=QKNi7oa52>Azejg5Z2LiOSB7w;`5$@igJ*-bD<=xq^Jm_(Md=HCY7*dR(lXX&o?ECMHGy@bhoI=dxV|DY(e-l8SMtFGCgX_wfi@}<g5E3?qr>aS_qN{zSiOVm|j4u7c97qRC<zBP^SEy&$9?Z#4rJ*_Z(tSTBWMN}O3g+Fvf8fn9qY{j3Sr2XRBHFMkI^dzkhyLf;#UF=1e9^8f{0Lx7}9WF|qlRbzt>?0hWFnV$BD=z6N7EQfsh@n~gFX2R$w)fnxgQM=9*+Q9l$iv2eLFRfDL+UzVKn$VXBOHe-{|4cu_dWXD*A$yfAM-28DMol{Z>?;284>ir0;smSuk@h@C&s&b6jzwRN~Ggesdt!TJV-*PBzw=9whY26&RUWxYc}ZBsnHvzD87g4SxzJA2Z!RVfOu}g+q?l<{I?Tx<VNPmSf}ALSf^pc?Zq~d-x5WekMIzrD2@m;GHtE(MT|lGS3U5r-gY|}up0mlKH~#8`d~Y>G*i$K7$H(DtrP_mnP`>IU<`($W72>Uhv-#v`{;;90r7A}zFwL-I*PG6=48B5<pF(eP}vUM!7FMIHMuH>x}Sw~EftJa$h}}_MKSmyCcuc^p~VD?5^Alymx5czX@%ggDoH%8l5I;~GSLkqHej9djK;R6=fXb7aGB|pbc<?Mvs44R8#yJUyAuy78&S|bN|Q^tb9XlCU>O&4C<ezEb|NODL=`}_R5T_$o~W2Buz<_wBh<oGnDwH~7AE<0QONlK$?@ROh3SeUB80>aWix5HmRl_N(s%_~B<X(?^O6q8?c|b<x3hYVJ|crhkM8t*D&|0yJQf0IbC$Wn3FFgM`=XJGZD~_`vn{MRfM5?+j%ZZ(ZRXv3A{(Wufzd&Ds?yN(76Di_0JlU_T|#BiY<l%rsX~{bqxYj>YHGDQQYWUFDnwO&p;bqpPxtVssCQQHI~JRcm7^>*aB@Wr)C}<Bp^8Z^H@``DJ7$L9eAgP^ERGeiE*A%=Xl-Q$XQNZBAfs~DWopikRVfCAGNYDt)5oF?671K@Tvk%Dsx+$$X1!8GPW%%)jztzjaq)^mZaSR|V7+GcNtRHDe3F3*5j+j{^un7IYpxZkWN+>;z3%_PwRq_AI=scm#9F$z6c43eTjqGEVepaj!b4h<cT+I5yc7(LzMyf8hb9dO^u~2+o)Tnl8qZT6rC~4>Az5G{cknWk8zUik)vsmoUc$<K#f*^4-u87h3I`%d+}9?#;z(U=mC-Co0E^a3>NM>RL@rTRMXKn^@0rnTCOkrEYi6a9W5V1T6!+5RX(M-Nie>cwxA+(e$ek*a=Ls2+hd=+ut6{`;%kb6N-V26Z%+K6J%!ZM-9A<sNzXU7O_AAoPtC_fj!~NT@Zemw-v+dU&oDXFCj2Y!nVX!K$?7(7Cx|iT!G4;E&lDeK#a^t=7@Hcm0j3U0pB+PGJAa)Fd!ASy7JzZtlR*n5Y|5tX^YDwHInC&z2h&wKV5!JHkx>uavmYHnfGbKXcd?m&P^<A*}SJ<!lA}~JZ6yS;5q}%w^GF~HHnH&-FFvujvqzkalA2<sjBh2I+$sg1}359e%((fM9WHG3?jn$v4V$bue`MxniqOB?EZV1yr1Ya^@8qhCHM5M(MyiqLs0G3G1b!`53i$4H7vR}}wF3)-OVIceJLfONMvbty3I)5eW{fX`4@6PSk#|ZmkmfmfiPw&pAl^T6~)8L1?Uq9OBYD|K8l<l2Etk&4(?jBwB4)PCayW2C9vZzC2g`dSJ365>p3dvcZO>4iQj3_rBp+r<$^n!g?=#^liFoCBs{nW@yF@6^;Dy^}@68yN{BLn-yC4Wuu3{~9^PJ#(-gF8su2&_$#(q__2b>a{&N}b{-7VMJ0A=y<zeUb88&?Z`@o`tH1=8%3moksD;Q%hs%G2ad1v+i{;f7=kv`eO#OMluRxuMlOTSkfHE-05H>XC?B=nM<sjp)}gZg}X<xKOV{J*+?#*AIa_<s8J1}|6E*|=Fc8!Rv+#d2M>^%LvUGh2g$7DiC}fODp+k-HueY!4qc3x10&|{Ld1+ldXM{x?vPcRo{yVN>ww!s#~t^rL6fG5=W7f&$3fkO6D8P(SEZ_}QKfmVZeS{4e!*)0XUYQ4$`4%DsSe(xYO)&kq)ufjV_AqHG9Y%;eOx?W#p7AmXM65ZePB|aag!K<i}L9?DqUDel)0FCv=R^X?70-9(>LcO4MFO<@^GHUs1-3P4^zEFr<%1tp4xahVU+V9YDqty3}xUdrnIh>Is_!(g6;cf8I-KX<%>~o%lsIm7sZl#CT#00jgVW$e`;Jdb?N{4QP?ALjCZVg0gTQMudCy}^;TV7?Yic<H4jVLjiS1=sbobR7ra{)b<};boiB%Dj32P(F&RIxM6oth;r=Z!d;Kt5_NXh-m-A(hT};M2V`_`dRc199rPC*W^c=%Np1`z@#v%3mc&f%)I<9;}J*|B09V=hU`p?<ohm;Q@K4xp`-*~x%Dw4tJ7(T_i{V1Wz^x(OQYI`c7+D{UyOaq?i#!88Y7Uum&NG(f9Rgw)066f30vlgI0rDiS{uIwnKTl>25by>8n-*%`42HKgvxS;-Q<WFy4gwarL06KMR5cY?^^6fPn+YAWAvGQ!13s$$9ZMf2Gk!r;4&RQ!XG^3=^f(_HSVeRS`SZT@Pw|0v_J9X{_Wrf;((H91Ied!>kCCdE5Gi|&!loXW`zy6EcX0beLFv>Tp%}TZz(A)th01dx|tJK3%%axd^+6T1X)^qfEyp%7n@ToMVx9DVk$4*wQDcJi(@$ZW}#j|?kj?<Q{Ldr7MM7p~{o_P@}+l`5HA@xh<WMx)(ZokA94am$wF^ug?;q_Q%@(#sbfo4^h6_tXn()=2vPe^bkn1)dre>=(5X>&_fbZYn#G$oOPp<64f#k4#GX8jippr*$3Mx%*}N=vJ;bw3c_#zYp7b#>AMspuEPKUI=L#S&#mupLDIobUt;<@ABF%$lvyARVQ+O3Gk`NltWnWJ=eSUh=X|ac1dtCgX8Th{_A(A#f0^o8~iNqq&oxh#G-{YnZxY@0a%Hg%4AQxtxxPmQ4S;(tZ7JKT0JMRoftfPb!f;yI}{G^)nKY9a1|GdBOZneaN05DH|_s6uV4f_oGB4KtkU^i$M4jNxCIDo=grA_kgUD{ZK&t5h$zJ--rjsJ|iLL@yH$N=%mYU#r>_*b_ylKkRv8q&GY0}I&$MHqOM4a5^^mlR8|%2U%1gqjj#o<MURE~?5Xa_g3xI4kD6^1ADF13v;o-jwM|eI;hmHwW$_pkLaD>*GtSI~jBi^zvn5jjFy(FVX2?>JC1LT{+WeV=ZjaEkkmCZwkoPAA9AC45qq|hVF}$#VWAX9=js-=a()s)hSoLY?#;>^I!4d{mxABv+x{YdHw*ex*m2Uhjop32MPGU^B<TqIjYQxPx3pn!lcbCgJ7<*u=Y&9HGLcdzZLDAF3{25cf`@xkO4zOETy>Tr6B(?O*+E2?1+D{aDEGGG<U&<95&8%W$9T4f)S)y2V8(Fd%MD63!4Rp|kLIU~t*i#L;XoDh%vEfYDWCf_EG(%2RY~bManGO{92lJwhcwV$o3YyJoP|Q<a6ojf+3sQ0Oe@CGPolbd+=j9sB1x+Y4RL6>q8?sR0GgoQ+tF*W5W~3k0BcXNH#{1dAUjt<SwP$fb#nJXCR4-O0A1~!uGS||R1C-E697fnQaecgA5}Q=#Mdc?nUzZ{m1Wwke{c0m#K#;@;F~Xx#7zu$`%sVwhHwq&U&MIwEh&J@jwCT+b6q9=+(hPPjOsUow-Ak#=2NbEo47eeR?F(9sP)$;WH!Ws}nmsqQ61)I9l9R{*>Ui26Gqs!$&BzfTm31LxUP}q;%fGa;@Bp}MO{x&jHjaYw4>$qvY&`2MYAusS^l3ANfq8vu`*N3#3q-f#c}l2OCeQF+P%cPx4^O)f@?6x&|GSvmV_oDOwwQbo+#YE=^6?VRZqH5Ou?W{>Nsc+r+lx^9T#DpwoPD^EWMEdE^LrX>%nM4~nA6;VtU?zr2#>V#5IdEF9Q8(=xza@}59fL#i#d`$ij8m|_)@VEs7JAH`oi+y`>fK(b0`+!K8+C{2*3CZv331ic?YjK?MmdBFwBY?cI=P+m}!G8lk3WBVw98f+b1t7{TnaXCLW6L1zB?Rswqow?liH7hjekq5uWylm=^?Ur#&KPs~)W06!xZ#F8I#n*&cCKv|;A#V_Ri)L+%dK=v|nj3;voD5yO~>===gWI3kT*XI!Z*pfi^~nHIHGi<{8qx~cR|x}tQz)sU7vBz|CC(umCH1snEC32%9q-1O-4M1$C1Pr0Sve}0<y-0EJgDb57Gis$AC?aXiIBA*lZT8{!><y8$qRS>4Ls$tjiF#>{48gh-YkmU;n1f5&ehNMfqpzqJr11IUg45N<%f{?tOs|Q*Nl35IvzqUF5$il#T>LZYU?C+?LYW>DUZHsTWKC1tB_xAlam_hDXBCYQu(bPYufP9j8_ou6&%zclfkeBmC5I=<FW>P~Qkult^431%i(gcKcggw+35=6eR{58c@LF6GXeD&PDnA!X9qZ(cK4|<%Wkl)fF7)WZCLWTr0atNVXI|?5o6|`|PLAbr~sNciK3Mr7%gXp!px%7NC^{V#o-c`quT3`=!R&=>?2}V{+zclRrqU#@>^u^QHpa;X?weo2%>;`hT)?M%lPmo~sD<gxWnke0s4K?>sue&zUdMX3@?GiK8mPPqdPVy9;rp`8+a3{Bg1^8X7LZtQJU9N_NW~cvYAL@n4@GazJHP%yN^Bd~Ye?=XdvJcS9NP~J^Jjrih%+1im!5NQ|$M1QUO6te(l2efVCHI~wwrfBsRH3x#Qo572|8w`O`S5Z65%@H_w17Xs4zO>aWVc*_v$jIjFp^VgX-$o~L|F%#c>&Un?^o`Dzn}iJL-9ipP_TZ~bH7^`ZJlB(tYWDlzv6SX(;+=?{hNj+7<f($A-#_x5&t&5zaUFFZNJuOYk(i^*68SOYyJev(+gE4R;ou&&;Q@cmgQGM%*PXAQ1vh)xH*I98**amZ>ns$GMKu$n-k+QC+4N>wvVY?-h8{2%YVE0=Wh5hi%|ko)M<uzLk*HA*B@B*R=|u#^`FRYY%I$l*aVf!Poz}uE$PqXk5vsL6S1N*A5z^IbtpBaT*F|Z%eW5%>u!u6#Y|3$4BxeII&HaBHq7vB`CWZ$bR_<A#asYE_^J>Q$4ZFgT(e#lRb8kEjdHvGU4<&YYC6?|Zd^Pu2JotYrXsxG^;isihBSDADAOJo4Ri7$k$8auCLOb17aRb%>Wb8#@Sne77+_`=RX%GL)zB|0Fe}10;e*1u5T-VdVSrw_(p>y$7y#S5)Z}T39ic%s9~r~WYW+|;MYAX*Vp#=*Y-L66lVfFMrUo^rX=Kb?6ENV{n{rIl7+HncSCN;z{Ku4cXB}1{YZK=SmkCkcPa$}=eUhJ(411lxAS9M&)==5hp6OPo@tTCM&&3&mRW^QdkV^M)#0ExRx*6~wUMS~Qo+pw@?x@Ia`WHwujq;H%azIf}C<484@VqXA`)4O*hApcF@l%LaWE=|dk|mY6w+;BPXs-iPhDa#!%=x_iF=oyXtgaAL^?|~HZge4FR%}Vp!Q8Eo7^{`N!+lOyrl_^$5vZ;+U0Ua4BS4bD0NYqU*;6t_*V1B=hpL#0!;;itv1?S&#f2|LU1{j({znxd0%lYxqHigR4C_j4&Hd<NV{U`OlCWSA5i`U`chd{C$u2qQzi6e3NyiGGF9{Mw+3v|QG5~1yxqYZC#D=1(N~8>RdS2pU$-i<=vs<Jn0=n|wD}Ec(X{p=zL@9EtX_>j~LB+%HSQll3H0%M!d4L#s6QV?5<PAJTdho?!r>uMW*|pDRO?WvpELD(Mp-&&fn-%N6zbGLX)mRZW2G!uKaw)3gMz^F5Mf$)d78~B!ZeSFXmw+npfD{4#G8X&D8XcWU;VG8xw>7p?o!*Ro347P#N#Bb8(CcXIUjf+x4;Y=MZG8%QF(0+5-S{!cWP_m10_s?(9tb(+HA;Vbh8x7xp@}%~{@aS6q4lfA|2z=E+1wHH9YAQ9gruVksIEtT3%I}`uq(k~IZfJz@#{JM%g(B^`0uP%ssXMNC{=bf5NydQFFzzX)6Qc-WoEo;n2)l$77jALVMNG!w}2gtrD#smyZ1(fjWg3Ui!3Vg#%P0LG3y=K-ZE!wP(xQKI<$l@jU6v4O^+p^qAX4?!>n4g$@QaN6SY6h6uS%xjLG60P)g07f`rX|veYM3>o_x}VrA!=Yoeme{#c*7oRc=oqc5IhD9uUBDH8QF0SyY^fA(~9|J#$~+1G)5zu+IpU>JxW{}2f?L<D=zYX!$^8stw7e|<0u!-nE$s?@6(*TjAHO7wAyp`#5YGPsbIE#zwn1Xs40erM58x>rk!jEZou<uB&2QVyGnk03O5&?XgXr-Obm3$BfWX2>dOai_v&OA45V8c$=8kQil#w^Bp%#omO{tgejr1Zu4zrwn55yvTI#=SPl|C8ST}!S*1W3D`1+(M3{+V$67$gw@t|by!{f${DF6<OIaQ#<9}R#!gDV_^+qzjq(UzSQ6n$@)KnNHbR|AR87&oqZn|-lwK&d3r=Lj?ZSZeTRE$(t*M)`WvDi!ZAgt!7}In~Q4Wfi1lGJ%QCI*%<VE`8x~QbuQ3zOfs9fk$cx@;akcA*61K2A?Qj6BaY7m%GEVX917Mx+92ouO^P<-ZO70Eeb-~m}-2hoqg8Ns^u+L)y9+W4vpB3jxbrOl4)Lx;-OH8O(ES>&}S6uu*$5*Q?=KXpN6+Q395&6p<5w*o=A6YU+`0MflK<7ChsS$kYFPHiat(m@gq?j5Noz5&U|>Y^(0>?>AB6RXZ{!p=?eqbBGY6Mf!JC>h1ydQGobdIe07U$}ZBnzDJaW5(P{e_lLTzM$UdGpfR|wCGz+uQdPov_x^2w$ao%SND$*T)wAxc!CY=xGVhf`xKR=FiTprMD`0g08w*3ky?b&|Hl6~Qr6LACW2@SRo0|%l<-N1dgl;W{}RL#Z1$<B7TJkY+2v`D2GDev@lUaM8-bCCjiMbz`rKypdkv=0p*^ybiVl4<zyGL>Ja=Q>+}?E+X>1N!3SIG~71}t7P~y{2sRSV~1v`V~1d0w@K6Uc|Vl6+oSdp;T6y`arQX3{N9<&WeZQT@qf;*fNQkPLdlh2~1*cJTK3!%poV+{$ere=H0f~!A_l=4k?CD6x;tEl262!qP*h^y;v@_ctl@o04wO>zncR{UgRt0>=poR;MkGgQmzWU;r3dn|LUHdzwikZ9_I(p(v9po)*+ps)0S!<b>S4?r*$i8~Wop+b*;D<$?rR;iZ;@NQh;#o99EkgYV2b1*X6QkO)TDlQW_S!YQ<C(Z@Y8Le3eUJeqHbX3hjn+!@nI0(QB9LZM4Od%akD3k9=nH(}@QiE|$nSAf#`zw@5_^f^yWm3hulD&q?R*FP$d*2rlk|lAHAQC65Bi7{m+rF9U16Uc)bgl!<0OB(`*Og}Sksw)Lq())`@HEO>muRt5USzyNimdOZL;7b~kdq1K6Ekk_E|DMKi~Q)1XphpW9%i)1-e`~HJT|WNXM{&8huxB>E}t{Lj4z=#9!pUVr`$$rPhaFShEGjqbnpNAJ<(Y|kIt$rnHO>t)}oW1C>Ex`6!JU)cH0Em*_C9Bm)4O7hVOnR%+sM?$Ih0vb@b~+x<ks<nlMj8C&#t{t*54aL2D^(Nn`o+(@l*?hw+6MEV`zapsTo=I3M!rxgtmMVT~Cr1=n4sdnssYwyrDvzQYvj=X9TrZj4lZgWOJs9Z0%A!#{cfU@f5Jtrb{?9RwOs=Rk0G-5@)|{u+c?3_aYFJCfYf5|&OSZU|=vn{4AG(4DS?^57dth$si0)`+I{+d*@L8A)@B#wK$65ULTF25$=b-#$w(O$Q%edjB=)OxS00yNvGhFhbi}lI&L+OUD2zSPuNUB>Wo`nXEA_2DU3ErgBk~(UO)jKgV*35FQIeSt>0Vbbng;&^$Qh^a$l1ckaLR;u<Fr_qQ}-i(`$`r2;3)`o6fvDf8EQ-Il$THl?07Y^fX$^)nLLcF3)VhO{Llzlrjs887X?ckuJAOY5xAo5NwDRn$Hf+5xAT_p9{9^x?olrtPfq>({=+t&%IhmZxQ3sW*4kQO#GynlI{+0wYAV4Ju*)@pLO!Q?|aV5br?>Z3AvXjns<N4#^Y`3|7`49a<xOP%+`>Z=RRbU=FhyOlz$gD)Z@M>lW1$J!<vPt61`jR0epPl&}Zy<xSD&F7@uDwXjp9Lh1L4zm{4JNXDvIHbuJue(cC|Uv6Dl(JJ?W0&jp(D9OS-K~*BWM}UcZ0h+8Iims1?oPL;n=~>wG#B>8pn$}sdE}L;7mOWr4UQ(ec9lTB39PS$80%-_ITJlCBbl&cY+6iOukmr{xQ-Ir0`q8%@^?VCn@NS2EfI*j<{P9=Tr9`*aE_RK8>ml1MrE}ZtO(S5r!zs12sX~@wi5043Or!uoB6^bcPce7(yQfLB8|0f3b41A1F~~%jz!!g9LV`6dxFYmDs%loR**hrEu`aO;vo6|71&c`@GdXcgzEeV&h-T_kDbiX7pmtcW%0fMG3&hSn@mr0K3AVM7bsMH;Tx)xNm7JjRGF^Af-I(7U;PT-dO)Li%eB-y$>{hx1!8(bVw-E}uUeu`uf_ki`Wa7)gx**DDT|^(y`fVvBLdAKLdVD+lin+4v*bM2{dzNCrm{<~6&b_0&XwS`5wM2K0h2~%Xy=c23kepT^1Itc{`l)y>pNn>7I+N#qlJzA&Nx=MI;eoL<67fJA>v8ag7yenzB!B+0zPX<|W+@4cwP}lnokXrVN2U(Ab}k%GlS~6M`O2LFr%81>h_02mN17m2UfS@+HfwX)pxrRGC=GRNd-IF7F6P+9;tG>x#}H%SOu2Gdo-y6nflSSk(zhPP*In%vQClHQ0cFT^1A2ub{jtXTX`bFu=`S5TwMY-6E5t~ZBpf?v_Ovr4>$Doxrrc<I@r@UEp2UxTbFL>GIlrX{Ds4?V)@v?lmfhsKBE)VX3$`k=ymqD*`6v=J55G-&K0_H|POKv(5kNKpR?5?tQm)UTVdJ@CHcZBFM0q1tQ=;5+x^Y;bbGedK#HD}d=(5Cmzu?Wua8%-TB0&?-FEJ0-R$NK7F)y?OlduB?hH}Bu*tRWiW(5Ru2gf@+PoEhAIYDnZ5et5USJ9w}TC-HM5~kn#Ac}}oU!ybHU}ZTS{NmuOD2kIgH34Po?c`kURnsc}mP)xX@(?`M{Icfk8Eo)lhg*A2%HCvr3vTWs$4Y^CkS8c=iTD5ML)Qy1haBZznT=&jEUClb!C7!8>q5sBp%T9Xb;DQ-noA2o9+sl8()`dgSO>Ur<%OWL-9(*Nfp~2dh+e}!E#}?H{BI+cgBH++rPRGd>mk^VYRM*o7vXt?Mgy3S0B$7?gkFy#y7cND%F(ep06gkYw9=}sEcnMXUku>3)+W!3*gE}hOibhc1Yk6>*6vB=zpj^wAhaybN!FiR3#<Ak*Jx>@5vm}&;f0*E>Wq*E5K(NjwNc9+T~<^e&#GA!N?Q`+$`$DmoTlh)oc9$c{E}(N#+%7IC!>xO>8_MoH=;dBTsN(N57NdU28Ecc;oVCM4Gjq>gHBO{Mv)8SATNfH%EHlK2>eyPX2Pgdg(H0x3B&M`sRXk^yvgIcQ9#Oy=UZ+(B#&N|M-((o#&wM|apP>oQmVj8b<OPIzq}6ndxkxXyy2<E0nhN%1sn6hWt>uDKIQ@MOpap7I1+po4*T9QV&<?%;cLlZ4=}lq(ncLDr7p4eJ%?E}8~n>NvD|WwO7-M)<cz%gT-em`qmu;suN<333f-KWM((oaK$#Qh<&^|_dv^l8VNx~q`-++a<%wOS>MxK1KT4fH++h@1djAEDBAc@W`r(cQI*lTqaf$464!ygXL$C6fpZh}|D-7U9e3caj;w+`!Tvixx7Y!k=Cf3Dcy_8k2sB?mnyxTsID83s_AgKwTo@3yjiV4(8Bo<dQ?9nppo)X}b_v3{;JEw&EEFZCn`|wn|`|JjfYxlwPIE&MbYi!JKlX=ek>B%9XB(o_?<(Q_Bli32@61DgqP5oTFOC5Yn24u~{N_HyD2ZZV))`Msj!CDo{yed?;R|S5t=SJ+(!oV$FF-iBdd3o53%R@AwLZ6>B`H9Qc7M{@}!p8iuX%)$Kq&3&>n$x5flFk@FYP3lu(sL1VRAzU!wBY>%|Jt3M&-jZ5=JUHf%|c|tBu=2+P36P#3M710D^Q%RK<m*EBap)%Czp()pDs>n|LBGj@?YKf1T(<r_Bj4CpKiGtzR~6CduPklJ-)^woc(gzja1l>e5kdtQd-Yi8|Os}!YY%s@%yW?I2a01uB!p7S9`vCc>=}R+IS8NcemCs;y0e_!E7a~NMAZ$$zb{*Yhx;fsY2msN&Ax*moy#xs=F~400?*&xbLNVaM|D(_7;9cq(F<D(;^q}88ArGk<05avKzgI-41glbKsC8!T#WqdX85JTI<Ngb88;AS;MtukD*Uq`TXKJk7IE@D<gS*#)a^AJ}9@yj5p*1Xckv<LsN1?({e*opC`8g8OjbTMSx8;+s%N3O1r93=`OBeQOrEn4$l^_&dn0q>@}9nE|1qO4*zn#bftS$U)#`d-Kw>T;fjSFDS4+6qaWyJn&O!s>P5eFT0F1<sZ^2hjoSzQbl`;1V(*ehXYVDBgFQ{3_B1`-mxmQZg=+S=-egVF9baYB=iw}mu^G2AgGl7Ip@Foo4-F+z<;a(MS4qm~r&|*0fB7+(33k>oqa_8%2Qo@7yCZeWa&ZYQ@lK8(il7jBHyI>>H`dj-$gH<&!6Q@38X@xn2V7;D0E>Lm7YC%EhlUsk=XJrNvIk3D43bT)Q{}=V6A8l}e8@C|e8p_zuI9d%R3aojz!8?68$i2s$xkxn_K;L*nXNCCdL`8VGbsfWtlvSbT{PY;nlV%W83t0n&F7X0DF5S!CqtNJPd&Y2*&2)smxz%ucMNCA5E>yuWdK~`yOSZ#{1z_+zYMzTW<tW^b7Ak$+?+d_vt)>nu=Ln-BoAXU1go|r$H@N#)}=OC1i4+YU!;kq^2>U{x{wTE!F^Nb9B6Hs5VFq^gEcu0t;QTEMY+c5V|6<d^4a;h!(T=D^ACz@iG5BQHi#)|;MH*RTwst_Ph2%bfZ4mP=WwO}a%B(~DqXi*cR<?Fmk+qfsO%Lq&yG-%qB)S$xKPqFO&Lpu0F595H`aePdxb@jQ3>#nX2TS1VW<w+Z+kr<E(zOc^jsBI?f{8n?p^b*%_Gi#H!?y=E`2A7w>8T(N`c0pCzU*H+?s9PN|9BOHqm7Ts#jWw_B$!>Tis0jxz#d`ya{A|jp978kP*@36Bw-P9dB^70-p5_>~u#;aa^apDtbWIus9>vBZDY9(4vrt6Ii9Jh~1Md3*?5f<=XtFDL9bOB)dUR9ZE1*8}5A?+t8)P?yw_f289RjXtLxjyAS4XTvL*aZPt6054ol>mD*Jh$J%MqPebcX!0*P#03Bie^lnG46RQ=gHDX7r1x^QA)7+_0A#)n-p<cVSKEPJj&d;0bBrIpS_hvpP9qqq=_`DZ0QGlEKP>GeoFGNVFl#SKEl=0HK*O1R(>z;UEKu~Y-18m)+V~+}8kC#48iNkOQEnqeo9&RQ8PH6$&YIqtJDRLu*c&nk@MAeXo$C2~kfgzkS0D{GH4L1cni5w?XfP)YwVgKnTmSh7c#*&*KsQ?X7X~az{V*_9{)_y%)go}=g|Hd*tb=5UhX2&gi_?DF7`rrGgbr{SaR@87PVx9?Rf&}EVVldgN9N{!kr9o&ajqEISX2DQV7QM0@du3x177y;IZw7v`RmnJsNU5WWyW+hZYhyJS#Zd+z5H%b-DbcbPB@L0XtArOz)NomcJ@2g*utJjqrs672hh(J#dn;;moe8meFYRn;R$8e9%4GwJb5P^iu(|`+g3IY`Ww-vD&iPGA{E7Sn9swLMP1VutKtNx3irKUhxjl-Sq2uFYN??IdIQ3;_Fw$R_3>L|3IUH{mlyyqyP0E=!L4{)6GNe7nsmfG8>$YEg>cv0Zum4~K=rpE(SPbu6^JY%n<?=}OF1!fR+E@W6O=k+D91o5CBgfL3J-0T_EGdah`m|V=(wwnmom^!)qGUoiBud&*pp(J}gJ&gYN6Bk%{ASyds=SBdRZSyfYbvpue;ByKputm}GnQuQQJbX)ntYVeYn>#<fM7R_ESw6iYpj2A8B-l0d|^=NO&`LbA%cpwE?5$wld=XRgsqI)do#z8B(Tz$GJt2L5Q_8DS(Zkn;cAg4$L(aWk$Te}``we$X3mMVU#Zu`aqhzg1VK{+GS6qrNxuJIb&=^Gl#7)hLVj}c{_D#Rd->X)pZeu%3%|DTYYV@=d~M+mdFj8Im;M93UcKb6)h9XakA3->LWtLn`Wf4{`sRMC`or9|{>9&oH($Q!yML%Ut^c@}{u_E(-Tl%tU+-ow=Vzst<6qqiULHMncRdFZK+ehCkA(o@(>G&&QoiJX{_>;Q|AuT)OXnDSzsmv^!Hvhc@Xth2in*kyY1=^0l6gpGFZoW*7d)<<@q9_0CRS~PXv&*je%mPJwlw^bda9}cF_$qWOPKKtqnR*2OSdKhvAhLHDXW%SY#e9L^)iI~X2>sHejLeMQXX@skHIc{I-vP2GhfOik&}e>(Jvmq9KUX8jE?Uw|KiE7`}s-Eu50|!d@^W%iKp3T%%d1rI$gM*{j|Sz8uG&m&d@mehjENl{8Q696@cYCq9;d>E`QzJjO?A@re-|4qIlGdx~)2ST}#NGBGVP!*^K;A3%cB_3k7CjW4?s(NhmH~(e+0^duiuyI-A)6P|rIzzq#|<cX~IUy+_8u92-`&P)U5&QhCnuQiM^7Bhnh`>SN$zVV5(#V~;-XfTS8E4qJY%M;xlQcbv;l!r42+(YM${vzPwz%jxUm6My}k8{cxp`IQ!NdhYWF<g<05DfAV0be?xz!tJv<ep2|W#|NO6KQ`Wi{0`yb`B%=)d~5+1kFL%g-}mWb*PopK1L{9}>Bg39tTT+yr_YR?#~nR!xt*t5Hh=D?H!t6v(>GaXf8}nTG{uc(xxaDFpV;zo)`rE@n1J_Bn$*pj+WDiFIccRh%A>J>${wAh$@25@@hFl18!-0`uKFqA%hVn}m{3cR7zSy%KT*Z4a5cpQ;8e9njntsBx57gpC#|UTUa3k77jGS<DXHApxWl^mvhdLUAfJ2Nk!nP4fY6|Zc7W-N+eenn@r$c8VYjAoubEAbbTNyPlfh9udA~V;=?=<mC*g9SqH-dwW3kx)67_CWwl(|j^n6j058>g&%~D{XJ5QwIE*{+%5`lrYjA`$KNbx(xN0cyN%3eF8-mRS<NWDsDv^rs5Nq&ZOyV`VA=T+gi*jJ^CixZX|*;gnG|K_MyWE;eb)T`9|v|&kS(`1GLK-&5e=_;KSnaaz>oOGqSRXQ*ZXuu(uZLz8VC@=+q(--ot+!^o6Z(Nqxai5-d^_w5c`ZeB~TY{KXRi+|v%GT>Zv1S2^pP0VG<Z!P(0+Eo_2^Yl;D;H0=yi!*QZY5onu?R8Ud1ybWtc1l~EC>}>Al>R^ivzkwa>SH`pstT69{ZL(qBp^SOlW6e=4vJ7CjW&M^5^YpzD9&<gF{aYG&n5W(|<K2`+<#m3(2PE1S@`FGS^;0vQt+pB_}+=*nv7uK(Z;@w4@v=TFBjmu}QJ?EUb*CcXEtmQ|aBatY|{Asq$4(Z3Y90^oaUIAQkSX$4K_VtRrOM(U2ShFuObhvnAwgQ7=z>2^HLS<UfdKrpSU~&Mu1QATS%VaZLqS?(hN)1Oj-yF`FAi=ol<#>ZMR_G67T6m~vFeHTtT6sWuAdPF$Z2;f}xeig3Ro+^^Wx>&w>;{MvzETlf{;eucMR;q6y=`xV}Pg|}bf?N@mF7Yg1UKX8I@pTOJB5bg|b#|&>fp0{~p;>*#*JZl3xqjY1Gpi(`ZX}Eh9leh(o`21LeCLhj>ZjSJzbSK;ALGBS59pPS81fGD1K3+zD3BDF{Y};}wUUnH2k&Q<<<<YO7pU>>bH?VE{p&4EdP`|x;sQH!NxXg>V>4aySuOl<4t+lpq%dt{pZ2xPJ_EkK)on1&c0<-5xw$+BrQ2FP<_z}bQ#r#Zk<_1^ml;RN{e|jxtagNysYWR)h27%W2p~^ad)nJBG==%H~-AgZU?g+OYb#-`W=~!(gW*i}fFl+;`GmLr-#vY-y5zTccK%h6Y%wK?4{Sj(=j$1dkaBI6e=U}kA0}-ErzL_#|^!^;mE#_AjX2__$>DjR_W0}t))-Qsn&!6}kptZ}(R(>ac*xPJ#2Vy;c^e>02=e@=IBb-&OI-#)s5^f!*$BP*4wca>KuP?JJp83GddwR#?2g21?&eqKak)3w5=T0}YzJ+1?+4wzgH1DSM_vneg{wJ#n<;$bw{as!U)!fX0f<j?UsnNa&H_QxHEKi+aSSswaz|n-SJ;}XbYh|=^zl(}~7f^VokiindC$cL*r8dgnN4tUmbTqZuqV`S8KY6$EsGfxtIb0FkCeXB{<RcafzlF2AYu|b)IhW9DfVTFI(`o06at)c)<~LvL^>Exgx4a%IN@yH=Jq#DT9?lvp+dT|d>>dV)R1uK$=5Z=pXF6jPTexSy86(UZ5315NnuLu9ACXwow!U%g;QFS3=&_`aBR{{AlmrpZgZV8;bShmMoJH0}Lp*bvKDI`s^V;LA{9pJ6S~Pycy{*5}+fbjqg05SHot961VqgoU=GnjjL!lnrN9&4Md<CzgF5sdgEn2JKwtGlW?QjXM`SaiPs}F8?a*{YnSM2SIeWkEI^@gSES4Ul;+vI+*mpr?t`T+!j(lA_Yaqpkf`TXVY=1{7_tVxzYV<%Ucd7t1^nz}{Rqfhue_pBqwPD_6$c8<=0ClksdlFgW!cg5+aDszLaFyFLa<o>Y*nFlUQTUY;o4?Q86'
_V92_P_INDEX = [(0, 26844), (26844, 15979), (42823, 23163), (65986, 37139), (103125, 37151), (140276, 12951), (153227, 26540), (179767, 10351), (190118, 20020), (210138, 14980), (225118, 27170), (252288, 29439), (281727, 23142), (304869, 41828), (346697, 20048), (366745, 22831), (389576, 22472), (412048, 14273), (426321, 19859), (446180, 20074), (466254, 18550), (484804, 25697), (510501, 33381), (543882, 30321), (574203, 33225), (607428, 20742), (628170, 19294), (647464, 26240), (673704, 17370), (691074, 31661), (722735, 31909), (754644, 17621), (772265, 20062), (792327, 18958), (811285, 16546), (827831, 14849), (842680, 16897), (859577, 23594), (883171, 14517), (897688, 25876), (923564, 21799), (945363, 24510), (969873, 17254), (987127, 17721), (1004848, 30430), (1035278, 22250), (1057528, 23371), (1080899, 28436), (1109335, 15111), (1124446, 19222), (1143668, 21619), (1165287, 36312), (1201599, 26727), (1228326, 24932), (1253258, 19071), (1272329, 13339), (1285668, 32909), (1318577, 15603), (1334180, 22555), (1356735, 14547), (1371282, 24818), (1396100, 22449), (1418549, 14108), (1432657, 25896)]
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
