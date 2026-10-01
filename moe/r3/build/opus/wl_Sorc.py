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



_V92_P_BLOB = 'c-ri}TaPT;mL4>3G2@a^Sy@?GmwoATPM<#AecZ?0HkOTe*e^W7A3#V*_6x=!+L(*5)v_%>SeB77GCsZ_gyaVc`vqADfiV(qSh58?frNx)gg{Ljgh2v+0OR|<F(V_hvTD^@YwxvM?OMB(J2NseV#d6TIWFJ$#!tepg+Cu_j3vkPlQ4fBhc8Nv<uR5y;!RDZ<}lWfLz!!+4{_LqI)<D=zO~mplssJL62mx!8bgluZ5mQeF>d;hJ3A-VkcyodQ?<V?j4{`JswvHhKa6$-`=PzJ6JknfvOC6@Lmq~ZLK=o-zaMglG1>uZOD!SWUyqB}ukcqwiuh_*LK)If)2>TbG4vr?ONSD=5vSSJ?KU-AV?qtlespCGEU8TP7sik#Tp?|C)*;EB2F(lB5?pz(({6Lsk^6K=_9jn*eUV~GU)ssm9rl|L5B7c+?ED)X3^DLo?!p}M;V*iBTW|crGyR>=i(@_QZ@a>ccQAU?x~Imx!E-$A_-%*tt*5QwCEDY9$6Fsy?D$C?KgOYkVy(+O7_AGf|2ZHL|7<9%=aQXKFai}Lko3T{hOXL?WY1BoTlw7fTf0Kl5OtySIDnzBC(1q=c#vX^=b+gSZDca8x#fV=lEwkUWZjl~w82_kIUVfa-4yG9hq8%fEwoE@7!A9WT{mW%L;>St*TL6Usmu0?6Ds=5nu_)$&a!-kt2_oY95;-qi^<w+%K%dw7q>@<xkDQ;GZW`SWOvyU{J%boTmJB?rz434bFz36TGtm2X&36XH8Yov3u({y8e4nA;jKG7(xBP4jBvuFw?VcOwmlD)xQ!fSt^|y8)Eu?Rh;FlGQin86cyz2T_JJ?FYg=8BW1iG)=pJ0s<^qOsvWXqF6fs1zz3DL>tce2`WN8c1o+zPVm`62gQUv=-=V(UEL%J&X$~xK3+~v^Y;+PjBmLisl-MjeIuqN6Sq79n8zY4x$2d%@xbL@P++V$-sHOJAe%o%ZKx3k7y#Ua~M==%1?o)zErxDR{Aj$pyq5>4p$g2zE8WzI4*4?V(Pq0jM?DcT^~SPWS0XvVhS`gToQ6E;#2t1WDUO$tnzZ}4}N3s_Iq&(`Jv%kG-DPI$$L*ag0c`I`ihVK*6O^x+Nfi#Z;!8tlzCA$}9mH+FI;-+Y@NdDFiV{!;9I66yv|X``Jw3{=|LtBJ~pIlBqP9+}e|GkDI{SKXNN%qd*s$RUNKvSo9ZyROt?ZMUJtTIV!Fx0|T8E11YFCOWsN_>oANW4|q!)FwJ^FqbL!^oq%7gSF2YYh(lAZ$rVMES2Bd1u^v2dsr4Yh%PMrxrzGB3)(~ZHKTrbuLf^<HpPBIdongh2@z}O4r5Z-3_EU9Z?E?6OuX{}Q_fSyM#4!qTdNY9iQf*^D$QbyxizA6_+ex}*cRED=uP@<Iz+V)E7H!!9k-ND1@qko2Xk0W;<|>U>e;pk@r6~!D?~~zJmwYK!}ZOs=9T}w@E2nD+e5XfHifO7vW1kg!LO7c_Vnor_lHQDA)fLsb4frnP@-jY(sijFu2<E^H_KRILE32(dWhX-qL5?7D<m#Lw($xhkSHa)q*YP&Z7@wBWhxOS)3J&3%8;-c*e%D+ZVge5ez6Y0gH~?Jo8&*i_+S_(d!imU;_y-^qLKKC?TqO*Q&5;ZV6!=o*yW{Qcmfs)A16_qQlw&<%$x-qNJ2cE?H)EGph(P_6Uy3>yS+^Xj1umiD0_Jq6J6FMv^Urf?exM{QPT;W%hs?8iJv%AOnRhi>jaZpHeaJ2u=@?)m2Tg;C2<@e>zj%(aDTHSyUc~e@n5SO9TqvXw8DL-?MiG;z_+F>K=x6L+xC>u_1u`Knb}_oecQ|nwj>ONHGj4vHkoG$Mr`JVyEOM8N@eL`)&{OTyXPQ%gja)7Sb6t~TXdAkgLYf40ehTWw0cutsFH9GV&iQT@tD*jOq@_jxuT{>p>20V$0xk0R60uEwjPWO^dm`%jvEk~lr#akv0!|18MOzcsbJNiIT$c#Rkj53amO(ciM^xamQ*O7>_Ot-@(8zpIEKWrM%c<LcnpXcn{-g(@Cazt{%qe_Hk}dcL%Z7zdo`_gocuX<9Oz&Ft54hOn7;o`O$sZ-HRCzdE1$DAmyZ)RxWLNPq2@)0;yHQIp=y?@x9zygaJun`&(?aPK%E#Ylws^t%uq^0s-amk7Y2cwFgq%&G+{WroUnF$YpM{ov846kb2hsbvl+0ntY$0D+))$BO=+^lwBw@b<8i`5<eN$jr72G|i>!TD(vKsh4tJHp*$Vxb54f3aAID6ba0DxC;_SAo_Uu3`70%YOnyrP8)A3`GqQv`bMvj7QM;+$!U8Qm~U@mQH@?kO^?TK<UAC)6(JUZ9ZP3)33Ln9>iH_5F+yPK(9`1aE(NBvJ<En!#U)ztk1&E*J*88bK2t!a?7dR-xcR<NZ`VS9U`K25te**v8Vjcv$GqC~6Ljkv8%YR*IsQH2PW0?KW12lYvphj=$rW#9&#Oorg2)O3t|&az3V2jjIXP{AX`mi@bm+R)SW968{)0S5<0Tu<#eH%p2$5%Z<vzFGLZctlF=s2@`PVvLKMU^BG0WW8}?Pcua7ow*#6=_9eY25$?(_SAWxHUtq5)d#lW0b=XG6-f)q9uum9wbKN&>515->^i@GB51yfP=hWGU<!~LYp;imp>=j`_S$-9grLFpQD7fQX<E$jxUICsVG#Rnn2&xCyCrr&7cLYxHuVceitY*7<vHJT`=cuaS`~Hyj!w-QTbSM$Sg3$h6d)0xJC+<|n!|3Rj<DgDP01zY3v;QL#7r)0Y<BF5l;g#RlBj@Tn%IM6_oQI%aD&z0W0x!xShN&)_a+t#H=QVFO@y}EFIF3k0m;xiS@5PoO>C~jK{MI#e2@p$19pcnK`T#EGa=EaftvPgOXQXlB+@Q}#%yO^$;fSThkEeI{zwZH0(!FN(*9_22NTNW4$PZRyEFcpY3I|PvgZ47c(~x2n@!NzWciV)V3DS9EDw}BSLkh<yk>yRJ;xmOIF}szIJQ5iRGG7Bf+`nJzr_g~Ob47;TunHhFk?tJ6&+U7lZy|uk1Kx*)ed_lw}v!dM_q7$iNs$WOe)DC5qJ?(09~4#{pDtYVVc|6!=(kC(YDiS%lEN;Ym&t_>;YfFe8+K97;R?36~Ij`*L&<-@JAgWAnO15tqF)H4jn2Z5EJlRox1Go+YR(G{I*uKeRwJ<E~z0B;#I<ewhrV)p$D%t-yJl97{i&oK=;U*b|NpRXrlj;Ya-BDsSETF&n_T}1jJD~V9X(lZDG?EZ?0C1XQcHraqSJ-BeHw{C=1>t9h#D24YnDvf%(A+1Do0&gSv^FQ<xj*!;ZTT^(<>Pwi`TlAB)c{=t20qlFtBF*eC9=Hj(Y;Xm+}VI8Ss*VFqPM4T_{&`Vw4K>C$ba3$@5$Y$792Rl)qCK8<F4LX|pq|IbG`Co3oNdpRf5iD$BYfM+tD`Xuw~9FoI{H!{7>8(H4vjqKZAK)vgNH*yY3{NNqlNInH!ks03W?vgh$N^{^FxIpA<euYo6Uh+w@&(W38xi?24KBo8bOmYX*Z++VSCh$!DsTY;+^H^1Wpe&Q}{X}c4JB6G=ov<rmFsZMZoXQ=o=>iYXaq=b{tP~Xtmc%`LThw}X=sBE5eFsw&8Z6h%U~|)iMUwQ9!nK{<=rb*5#+jH<b%wmIn2FepuiE^w(I}ndDK4G|7tr>rjx(YR5UHlS+X9-Yf(<a=(#G!C!wY5iovAOv7Ydi7^;e*>n1?&lo)yWW8ifnN-KlK=BAp>ESO`0)qjr5nwI=G{1&W)sYKH0&@}GI#;5;#lp6b&SE{Z62lq`{w#a1o6wu@NFJ}e!Uj`bft)TE`wfxU`y+|Un2yPSIm)-^i>QUiX|;QPy9k{<`9Rt&oA0L2>0MWLARpd#*FsC0H++w6MGh1}C!LqTAo;;Pcehj<sXGrI_)TCm+9%c^>vI|cN41QOvSI9csEL*MQgIKxAwJ1#=(R(;saSkk!#9!G2FE>qZX)6pJug^Mv526vcE+x+`pt5*IJRT7(0)G5u(vR~VH&-Y<Mufg1uQ^FLfk&|-JEWfAT;VzP7Ypp({NA4Hcf$u!th~VB8&lwe;N|TFyJ0HD%Bh~QUwS$d>p3RdxcUTNOlNuy-z6V?Z+TH<&AbxcPxKHR9qW7GUKv>VFK8yvi%AAYMpd|{Ee)Uy7bYqrE9_9J7;k0@Dh&56>%;Rp3eaDZOSf=7Z3+2byRd_4u6~XlCMw>kFR`%$KU=7LKwXi}mJj*uiY)RThI=TaTc5~fgi|Y!0yYKwlX+R9ZPQZ<9a$sY$kFZNe-a1Zj+4tOv5tP9>!LBghAS}|uz~bh{eYIR6=+oN+?=b0k9UQOpr1l*)93D@7pLz!6tt%1V$8xaMoA>`_AKXKV*g+_AP_{Q`$KO7F*vGg2{H{N~_3&E{|JL~U))jA^{CPg6Z|7tBfS=d*`L=#1&HmVrpJJHO+bsP=9b3P>8`ZateV^Z!7eBt&Z~wvR*c3nNWBQgp)>nTd%uLZL|F~||z>mwf@jX7CypOMXU+8p7jGOVzYhFXCFC4u1?enkc@+-k_p}|IYoUcMv=#9Qz-t$j!w)Qcd|1lyH7i6{H1wol>A*q89o?}u_H_x5No)R5di0yPS4|IeAmqS=j)E}Y<Q5c`7(62{ua(mB|14M_GzvO?yo*e&5J5J{{-i$F%@#LKL=V7Mw%(o1dFBc4HeKH-l^_k!1cI79nCBpOwdd<X43bUoK6gz~`2w+HJzVsIaW_L{JS;G(>il-0d57HVF)(z{=JLIfY?WRQbu7)ftitt<uV{74QKQDmaC;;qPJD>YFoObW=*2x1E2q`I2ZP)A>8Ra5{gZAVP3tv6JH^7~>gODeA0p}i%u#ps=T2QCozUKAmHT`vX$FHLI+mjRG>awR#w7fyfN8bhf0pt0@UbyK8KjYaC%X?h;;?u2P<1${W*W(4BKHYGBM1TI1)e#*`X*rVC*L-?TEXU*V^qkn5`n2)sQu~*uxb$s$VPu!lf9I7?PUxTQ)#t9WK7Mw>dhD<?B!bFmr=?3>y*lFU%zjV}*6NOJjVoH2j<5VXi6j1A1gT1#e;n!~+~1|d;SM0I8~F6$)<^U!Gv57xWR&}vdLQFqrBBNepAU)QKyH|aP>EaKE9c=M`NsAT?n8PAdG`o`-9MuF69Z6(hai+kd|0;Me1A{S2i22_aXiS;9*%oE{5{)piLb)(A(zMe13U7NipMP4x67Z<lf<VcB4ECL2-;nNpe+dcMq=K7cp%!wTKLz)UyJiED{R8QTSmF=F_q`2*C0&`G1ge-RK9n^n1}*+g$+3f<ikj%UcW%(rydx1-7D0`*DlP2lh^C^6GAz5Rp%h0YUa%@hHIMT!+v#IauA8>33ZHHK+c5-<XE*=Ts-Mu+A*8U|Bb#?wd5xT>aIPi$JlGBElF^oy7T=|9@z<xOB+mUIlCrWrOnnmO40s9DBrvFpA6KlZd(@>KAj!;d7Ii}snc@thSVUg;rdqSVt-Y`c6yWi;}0H*Zm@&9RYwV&9)*9#2|rta4Z*^SN}OqEUMl_NI*b{(((=#PYMD!{%W65qp~E_{VaJ%4QhSbM$-^z+oA-}##@s^sqmnoPt$Ijt8-9jBcIpQC`+K3v($AFu49*ndoPS_5@|w`F)Np4HTFd;({x-zTvom>$br!$fOVVNtb$%uE$1%$TVyPR!6u1j2VEMI@jQAJ%1CM34<48HF`G>qOvJ{b~!Dh^WhV)Qbd1RM&w^?WmX0qk}U;fb8A=dr~EJXx3`x>xM#14np<=mH~Xl6GusyF6+$I$eU`jY3&h+x6D2pkTkta19<ujbe#h3*)rvwkZKI(9s>GFF%Jtb<eRYhic~a0JA|6B1&D+nPH+*f9~NuM8*-rn%=0E@E;L@$&-69ixnC2{a-)h##VPI5;C<nfe*mpG;Emt1jC?q~P=w0OSr&5q3B~5IdCjf7xbacOB~wIG=(42jIX2cJ44KXC#F|5SoE9cRAg1T{B-zk`<X>L+m$%0v0CKOu!`$McXzLvLbV`G<^ZoXIhaG&?J&6Q@N87YXNL;24ZBUzD|7eq{$&QbdQV;WCszHY-g6vHGBAOk}#Oc1(PgCB9#4Ps?1hXB2(fu?LiQ8Wu6V?L&u+QxoK22eq{QpQl2^+e0-~~V6Tk;mrn$u%*3$`v(Rh+8)agwqJVmY6y-5HLXf$5Ca%kdIW9R9QG$!}BJ92D7s1baqS%L^1RALzTlK?044*Q!3Q>G8+t8l$HyuV|>*woN1MF{~L1tfLn$8ztY6AgkKxhFPBP7ZAT*AlRv1qVf(-{yg&l`uJ5n!n#^*n8eBuNc<#=M`t$BlZy&aiPIrK3;Be2%)L9u@4IgQsz1<O1+gO6H&}hcsmt9YJ8bmSV)LI$VG`gK+_n(KPQpeS~5#Hr$xCa3oIpI>?~^Du!*thb6~{(L^nd&#hZcF<>2QSfvk5z?=-Hu&@=D>)XbJ{Zru&Ao;J1xqKh#X_!D?*+)XJ9;1?c%g@<lvOnbonR=GLz7-S%_^s_7PcAJ<*&b-0i(?(_NZB)Ga5yj{NUPlr+I%`Bg3y_9nlR?udrvf<Xq``oTs&0~N9@*i5l_F&*%V04J3Dj7Gbbi4U|8;OYkM=_1N@QDNF^^q2ooCvVK_bF{SInso^K&O<^xauyPrDCA(L?+QAoco%ONq#p`K<rjH@h%%tiP##i7I9kC0_3V1!IrA3Vxp2oCVHpDV3lK`rM~)Uu2O`VO&#aI!KR?8==3myd)3Cut3rQOor-r=gtXGzdLw`|@ziK~Kc7EeQ?%X+p!GgoYa?-mJ12gwM`buGZePgofd{ga!~9U{`864Go=q^{Mfje=&ByWO@&!$prF^I0if!P>K*QdF0&O5G8y-qtYH~3)WAMZTZ@EdK@jak~TtV$e7omDlHd@w6TP?GQBUEDU2-h!d(ES-OO)+ehSEOCPYwao0OGY_LyndL<$W&r9JU3HZmKgYps&bk^H@9`ze;0BWyMyrYhl^Sj@wgX}r*W(TtwwkYB{q7XLWYq_tV8E5N%YsQXn^7Vs#0(b0oQWTY0OlvFmO=O6Myk-!JtBq~3edd(<Nn5Y$dGIjaY6J>vh!;WTe)AZ*;kx>b9d@T15*unv$WW$F8`}-dA@4mTX%LCKVO8$j?V0t8g$2elU=N0|L)TMssfsaz8u*<@Q&S}f*N4MApJO36FdOE81&CX?#tgYPN26I>sRQ3mul<=$gh%Czd1MQZ;;o(L8Fz8HQ=ijl%Hyb6S+p?kwh`%9!DR!Be>l3pRL<Ws=hH$|w&>-){S-$^QkLv&T;9w|s*nemvQ$baaGO#dy8Eg;6&5*5Q5*T)R_XB_{?~u-uh8^W+4-5YKMj7)lFHOimb8nn?g|nBLbugSgy&h?kHcI=!f!n>^j@dff0cru1w=4AMhPe|FkW+bODd#~_l5Uu8S2lbWBGw->vyI4d0|k4)n^~}Adp{~C9+$29?Z~O=lne0Xw3K@;)W+?A;~U()2f~vgK<8XXq)K|qA0$QkuYHT##PoCT(h})rI7t^i+u2CfV0)TWZ&wsKcYr$X;uf%8CB2`}>0H(oi8=<Aji<MyHK9=%s4I5JI>??4jKmh(@sO_Ic`-`cqsd30<<OFVd+uP1x|o<<GA`*h+#AvGj;RibMi=*uQTr0LZW+iWJAFZ922ICQk(?U$M#Poj6`~o$Tm?lFl&-+A1^}mSbdRJC%1iF2@bcP2bw>i2+3jEuv3nhcs7L7Jud^|twrLOh)md_a$DhE1L~MJ^XZx7#s~tLX;A;4YJ<UTB0K5N7=gtrNdqyNK-oiU5X7JtRJ;B|4dXtKF!k5aVI7q>##OO@Cz|MtZ<0k#c<_W_wHZ(tsNL}Nu7zTfubjP8A3CbkUA4d_MgoxyA;DEa%aw7^`&+~TCs?<BI1S<4jh4P?e+-rB2x}j?)-{vpb@e&7dufUE8i2NuYBNKumVcs3%t?@QRdC+hIuKx>%903uBWVRjgXKuBU8P)q^?@c(itlOuAV=Idegk#u*Pua%YsJlQoCh8+)7jXk^oMW8UY4D^XW$TM@Ok8B19+2eo&U+rOr<`L&`7~w8-SG4PdT&WM#=jBH5>S@a2`1%0kJXfO^FX#3YM;hyS40b#$KYG2Y$S7f&X~s{bCnkIu?+J#<ikIG+?T$fUHFynNRRa6nn0VoGMk{g<Bnun>d!##p+_O~!hDFs7CZX2t*fiBq5l;r`?t&xKz1IJ(D#9<7C@kH?3wm*E8=yQ5uG5nD{`vr9Q-Ov1(}&qkb&m6hc*qs)RrwX!Bb~OW$1bS$ShUsu5D(A<<Ob%?2!*ZGt7>sZY0Xz<V=rbm%a~U$FFKaVh{*nVC#&x5L{a<Gq5kzl0;vGM4TF@|LQ|>{TFt;=aO2UxFQl)PVAO+xv*p$b<a5@u95Rm8cfW|QdT~Ra>kU>+!C6mx`iJ4bgO9zama~9PTZPoBCU8)l=?0I#Lz8_C`jWd6!S~sCOQ<REOwIWyb_$*;=W;;VNA-`gokQi%H~AnRvU;3jX2p7fF;xQ=`Q)cVOQZ+jJbaI9O228XJl5chtJ7#@>S$)s=xC5RC3}!gx?l>9J}MKlbj5fNKWd_lWB!~A<Qi0HRZl#d55@#40a?+Wm>GT8cxsCrdvGEG>&;28r6wMSTyf?UMH{eGLsVJm0pD$yCZF5$IywWw_=v^jvN+}Re74`LRugjXK)>#$(q=9aB6>n3&mrx1K&0L0a}=)uLREyj-0uDVCN)fBaw4bD<%n{(q6Mnx4_IKbc|>T{U--c+0=|?XC}FhsY&GaruSK|q)$(=SLBkr!z#UfX*`fGXeTa+KJSIG;KlpYey(oB7J>J*hhgcCg5_KNF;$0pHMqs(F{sA`P}rfz9MH~#sWOH=q$<~UJY@{x%_29!%_m$>;1v6hJsR+RpZN72946(O`HNH~W^6TOKZm)8A4LgwyI{Mr9N1Jxhn(GZX7elD@Rd>Zse^A3>H&Q-KE;@mC0PhnmUi?k*ZV-p%QN8uZ~l0P1{HKkFH%jYe=sgeLjj>J)%}Btn(mf}gby;5;LLU0A<-9puS70A+qi2L$w_o9Q^m4Kq?8i=4GK7|r@~9|zPx*ulQ?PVn@K$HQm#yCRRfyUHRq$rT?VaPDo2SdojY+$VSQk>25B^Kt)@Y<Ih&GN3B|*rM0|j%3cQ2h8OR9mnes&&7lDFi!XjW2<OzlAMkE#_uAvB`BaN<GtbxCAVNxK5O^<HpcDNKDDkh}^@oVW?xF|xo;RJ!3hlcLpQv*R1@B>oe*91v)u59SkX%VAI_L1lr`etWwrp%mE@HUm>G?{eSUK0ePJ$P6Jj=O~LpMogP1L$E|{?;b14fM=`ayCZl>=jv!+*A}_>HGw0PC+S|$uR~Qn1^_TPl|nGW~L`p`b<#Ro^wBn%nc2=cDBEmme&p=Y}XT;T<W=JIFpR?$$;hX=)cIKa_Ebv>XNX*_Kyh1LGn~kY(kuVrHF5fjEZ*m5ehD5Gf{;l`TML3R`)ev5wM3#5>Ac3{V!jw++CtRelO+jQquDCp{7(8=7aZD>o9?w=iq`)cTRH96uJ{`18Q?cJRoMCkiY4&Hb<V3GgYo{LH9+KE60EnJRO@xRIuoAyCW^ZE0nmHKf50H_rnM2ah~e_dL^zIwS{44XVZ}4_RdKJeT{4|tEn_lQ%e^$HSCsn%`0V1IG4CdWZ#yq2ZkP7)ZJP^8=k0UGyqn5ncd}CU2J%wi;=H}%oie%!oMS@#^790j#%4pJ~GzH^)1Y2o6&{gI>j&rM4-Nv+{X{n)TU$+S{xgIXk1h+=~;}ECQjQ8gnrYoZoSPHChwU(RoyLSiunZ{YW{f7)%$Btf9_i&Y*4Piwb(S4uZ~lAt6Y5|Pu4;(k^rwdCAoYti15`dH@FpTL+9cTt{HBLi}-U;KZM{2ZcO=5ha&Hc3rBcZEA82I%HKeDgbP6i9RXkIJg|2)KxiKM8{jgfM>}CnOi3EQmNF;Qv{1Dm(mqhX930LCp?TNnQ-D(M5d$I@kx!Y9V4}hmcC(rq+9FT*8-D5Cwj_5hjDZp%x@JyZb8<Z|iO%;j237lVv?zD9D6=Squ}01;%A+}1pEoDFtJsE)a;g!RN>1g=a*BcA;9POB!Bk{mD(1_@L$S4Rm+4J+W@fsLN&T26jMzHbUYXOm^J7?y)=EL<D2>Gnvd~(_<X*c5x^<x=1}?b_b({|SB+6r#ZgFK@W=Xf`qP8rU@)qc6*W`>#?aB%Uar>T<=sMlr^oZ~hJ9NCP8ng5%{|cG4i8w2ZD2(FIim733*|!XoCB&DzK8@Vd%aQ@oaK}ChM6(VKd^(1$({n;o^Fv{Jr|H)AaO(Y^)9w?BPHX@8Z@dd((cl&Rimi5nBBN}Dg=d+nLR)!epLQUTKLRWG)g}S|RjHSG9S1W@x1vyiycq3Q89~A<<}9jaxD+vbnV763)P_m73a=uUI1EA#P9g#V@yp)C#RRUlZAX#kW1dD*=S`JZnI0D$ddv~CPew{c6Ta|6Q($+zU6E;25$owkpqM~|r6?Olj1<PQRc}l!6+ts%ZJ4CDz9EW!O>8!HH31e7(v++I4}HpUNUs@(DddYIFs=GN1D95mG*j5|W^|9}%cPE{GX=UnA#~p5qxZM%arSEcZ5mD4u#bBOcG>w8=y$!3uVb?)Z^Gam%#rurRoALt)v0;-!@sF}6dSvsdx`cOF?L{w$0R!<f^yzQ?J4YI;;p=!RgZ*th~8&;+G=0v>1FWwof4)jb-_#!^Mok&n7qFSO=vQymn&2L(6ysxb4O$jqdeMJ2kURFja-**{yO}-ZbtkBVy=F{jy^E9*p&m|YCvc|@^w$I7W%G7lm_fV*o39Lg>oIrK>W)tV9ty<qJ3!Sm_C5`vpqKYXb=twnLehBk?zwbkMJ%d6#R)4W_!9;I%ruWxI(9fnUfiQi@_bE#d$vgYQ-*&tucr{7SPWcCPq53-FB+b6P<-tCO{;2b#^#AnA>}tR!~F(3mm9mN+6i_%Gs)+=hj(962<Ee^<KoppF|l?n$gHyK;P5I2#H`g=(p&*A*UbQra3w9dZtQQcEUR1oRL|O@FgIY&TeWH!dEf<?7O+j`*5m0ZyCi~5i2%`eqN#Mma0Q0HqHybK$|v!(qk69U=Vf#T?gYz=|bm#_^g3096WaBWEkX;Vv(N~0Hu;c{c7sejHU1o#$T#bY3GdZD)TamY#r{vqyM4lQ9&&G0}C@9mGMTbI39fwD!SsQ4V$RaQAsG+Ri&3%x<P5VsY4u|DezJjGDU>b-A%De4!Q%&{>D4)Sqfnm%qX+_E7X~v(OCh1?tk-M<oe&jgiTEBJ)N!G>fUq0E*xziGht`ZfQB4DYQm=Mb%_+@`IrgYEu5i+^<e1C6s~HSww;5?=zf3w%thA3(ZRM`Ax42{;N<OBlea!oAA<RBV!p;h9p`V)-s|$%2#1?ZkmKQ%7O79M*LlTW@~g&pLrqYSH_uR{A=*DNM91e1(K5SVQ)ZETX5Fg($U3yS6Jl_&Mc0OCc5BMP$DDUvGpIE6dY^g@HFwXM!ffzToq5h!=YS$Iw+I~aTv{2dOtW*-d}at_ED%cKr3eAyw#ZpOd#aIYyRmKrGcG)HFvzMsUZJH;$ClEXSvSCmLC*r2$pe`ltX+y~VMF$?sM43hv0z3#IzyHyW<EwSn<Xj8D&%ie6jSqL(nJ=Mt$Yws+{_njNUyQw7|EonNT;l}9NEDGncGinPyUhbt_b7QdrhtnEyBn^CdKR1B8=UIB8)*RU^gEDQDZB@n8yYo>6Rjls|t)21g5Iqw%Z}y_T>tUcS{Av%~KE*x7zZg{Nm5XpEBJ}ns?X0PA1;>xPCo$IRV(!<^&Ui?Z|A(cVw+2W?~?%(mDlsvFQpy;h`}hXx>Yf(UvRCi$h3qEP`BmoCF$*8_Y$OHLQI!L2~rG>lLn&{_aKw%qTrOCMAMy8&9y1f}Rht)Z<V&BB<1@uu~E@h5wMPs=R&$V4Bt<=ZjD|_VG~(n1nWR!=#rhh8AK-juBM@c=18c&SW@Qp@VoQU>5L)`sY9c7$I_BiM#^+92^+t&&9tQ#4@4RhTX_5M!(e6i=N46vQu@(#_VaHE5rw1X_hRIhlR-moD#V;mGwydeLQ)MC$BykRtf1@#W0q~JVGk+dB!>*3QB2D;8Mlt^-<lPyz~9__~*UU-mt*f(l#j)yH#TvxFdU#OZ3E8$L2^P>w;;ORv&%FP7S?M-FJv<K1OwW{_&rDYTE)SQ{1*a5J<a|T<fJF;Q8up>>Uhfa*a3YOScOhQ=lu0-NidcM&ihQWZDPK{teTiQ`-0Gh9w?m(%97K`B!j6WjjA<xg$~lIf&2zjn=rqtfbvn1xSOIMSkccOb5BPBV$mpv~=&CE~vla1r7QU6$}c|pTJ@f(q?U7>?4+u=({lv$sM~`{74**hin&&{eaNBjR11y$v#xJQ4~hD>yN@vC)|C|9*S5#lH|R51AxlBSMn1wwS@BP;a#%NkrD8>K?0&D!b<#+VuwJ#Qb(q^BtZ<64H1QCuxBhqUghixEAtg&(;Y}ejuld~JIP`6i;%pCgPq|byT}#%Gec?_{l0%IVa0!&W%)}MkV<{0;0!Nr?V4EDNCIfrav-JN5TZ*b`9^+e4D-*^R{+FpALpHX?66_HkVb0${8m&W<;63P*?*A2rf*9VQb7(Y7dmQKDyoDDjm){1JXjm!={4s*9xHixf`*@#meY6vtP6T}cik~wuxeq9?NXE`YQQm0u^ep5Y%YCEb{X36A$S#q&WUOR-9ivL60ADDL;(urf}%xw(h^VqsYCs=)U@jOpM^iSny?ShUoTHsm9MbH(dYgPsK%J2U7lwYYAexmtU0`e{-`9*A9|_DUQffe5_vrqWN8hGC6~0l78Y;8EvnK|s=oJeTPYInQP**7BJ*}pQ*_3x%NUR}_KjJeLZD*}WcsX_G8)sP_0OKF7Rn&e6d6*-*pQueBkvgyg&t^3OwFx9<qDifCCZ@SGZME(jirNTJZWQMO-!WR^(<PbRmmLtlp3j5k(-stZe>;2ivctwW@_s|Ua@`xnsvAey3%-@3T(*))E4p`l6D+bxH#GLh00_gAIpUPU{q0+nT+tnMpZ|Fhs8zd<^jpY|MuOwH)a&Re5ZRO$9DiUF1a@dTf6#Le_Shc65_{rILHyQ)S3854~MDm!;Yczk9EdjHXVzb^zhWLlVH;-3HJ8os$N$|m)s_N?s}JhBm9LpOF2@K`W+L@ybcfi{qtgnj0JI%gX(`q?ds(UW_u=`Pevjpd>%~=0ow&8ODiBUZ()e3uqsA!53Ofxm8hUxj5Mzx7!Y<DST(TIY{DF2V(CWp;|Z6bG@JF?sTF@DM}f`yy}XWdnriUyAxpnY2PGOJO3ExsHX{J=Omy-kWyZ0q6WzF5H#!*P_(Pme><+J~ptgVO^Gh37Rt4wM_;B14pv{>U5uugpJ->4D&4C+!JyIV&<vQekOAi!SND>)V{4YY~R7#d;F<8li)?wEk$NHj^;=yfWaLojHTK%uQY^!o-!yK79!V{>bv4{{=HXDtN%vi?Dqw92$0*fa@P}QDgdU1u7#mazKfy~d3Cfi$q5;t&!Xw9xKoEB%xgGig2;|bD)H9xBay?)iyG}*Q}r$r^{lmID17#oV%1f4TUwk^ib>xg=7FpVhZJtVA`rDO@PV+&!SIEhEIZs>KRw$aPF3~t^w1y-mERrSF-*zsiOq?$0@33xwIvZ$)F11_XYdA4xFS-1sv_U5R~H8LWOeL1Rls++DTM{Fqz>8K<wRxo)Yjs|Rdv#6q6V%*Es$aXv*k#%d7U0UNr{DOH%%fWo*x+j-lpMRjnXH!@BhK@z3jd`(QS4!xj?XK>4=}iO949&1@CaTme)HzJe3g+DCV*5G6?Y;Xq6*z64ff!eoyP!Qps>+H_e&v7U*TP?f?Y8;tEqM;%TCB6Z%-AckmR`BH4lFsqL`Zyde?JhtiV{k>7n2vo&U8=}={z4$#JSa3!?*KZb%4?jIVlsX`lMUn+^3*&Id}*$5JB0y%`B;t?hD=%4zB_|Uans2cw)w=RQ5ww-9J{|-KFn0b&NTrEU$(F!yqP0syLL=^#OMw4OZG7SP?3t-n1Hqt>S?P0We5o1`UvHS2OQ<y(Bs)PAgi1kpi&`3qT$A-S0ag>KkZGV@EtH{g81TH%A+%FUtKxoJr<5A9DFB{Ky{V0MWAN01x**aep_r_s0kPYDfCLUlBO{j69D}iTg{(e^E&GBR?NcWAf{x4sO!V@|tC#>%$N2G@82iZl#jgAjT)8eRm;VHA<-6gLN$k1#S8s9x^k45)v(}>;8}LR`DI+DSJur1!oEJqFdHtuJLtI=+VoIeMC^t^Tt#~?ZdTROslYXO~2i^9@U3)4Y+d+_!!r7EBQ4+=~m&-tgG!R2XgcZp6G$w7vj?B_G4Uc{_Jt-f9^d>+g9>jJtB2$U|Pop<XCyWRY3AWQCp0|7T*p}D%#pqWEtgEA=_=*^#H3RQgA&ow+Wb`$u-V_Xqg(^Urzq8wB3c$iZ;fk5w2_2)@#77Ce^aFFK@8{30iJKZ4!5iZ8bLyNX*R~(M6T2Wd*b=#A$*(BNW*i;h7j<`|HSa>SO)Iz;zhvo}Sh0G<TV<xjj?h<_%&WVAa@@Ooc=yom4~Sr=ia?nFe}(9FD1OX@j(m-Ye>g6p0IU)}|Cy)paUCIZV)~C(I`}B`Z{aJR<cmY)uZ`(iSS+1$$5jM!xt32}vf9NT#p79DH(>hY2rKpCPK4Dr8DB9K9M7XZ$I2FExL?wPt42v}I_<!Bg6t=K@q-OXff(q^x++bk!D}lIrs*dkB|Obxrn0oVP?tBDWkZ>q)bUvcsZ_7-1HOfwlTBO{uqqS1pHQntxKJ+%@+@;x&~x2ft{E$WO#WG5>4>DTXClkNHgC@%f`R9frl{{w2+Xo%`JPK+czKDu<!$7=g0J)R`txB@XPW!OM1KezfHP-}=_nogr;#EM{_O4aE!o*-{xE(D&u&iN@;|zNcu0y3}=hGc(%lwrP$1oR+i{96=C({`AbNp`;|BRjP-IQQ{KO+!`T)U6n>`5V8MM=%dG(M4gIKt0*IxzG_%nC4wlkhsJ~>0d2)lOk@j#X%;)G7|DUz(t`pcW*A;d=U_TY5t&pWBCikK@4rBrR4*_lk(j7Fz*aBwJ<C$xL+jj={#P`@2O4kR-z%6-QdR6_=@&>vWzYUYCUiyBxU{j~fiuKI6->(fQ2{PaK`>_lgr_lmEwE%cl2_7?smP>fI3H<N$r>mUibP9mmR<~3I2M?#pC1jF12nBudBE*9)E$0!kKI(~*krNgK_xf;;L#>Gl$bALp8m{h1^;6lz9#5nSon7sbCOAX?_w4`Qm`nxTQD6lOpRn+GBzc-DYl5Z;4~8%gp%@C9o8f#B7)r+VSi?{Tm=GL8ZTr;?xy{ABuC)nNFD6%cG;;kT3r~uu?jL8oK9kA3wdNbov|h`wt|p0Z3p;vD{*wT*fz9tv?})2400uXMMAlvYeH6olLDZq0&MRV31)7@RZ_R|G!Xsls1t1I^#<0CdeSxLHw(ow?V{irne60$K-;EtpQCN6&<iV1`@Qc=f@22{k8ov8_ea4tkOAjvt!N(!zx>U3v<ewz)}#apky~(cY|&n)wZyNm0H$nqOW6~qu1u5yN*Zx;{pis-{;uQ@U`=?;by3yqu{dX$+k2#1gJt^xy2Tf^Lq1^B#eHv~JN+DL%je-S|KvchNX(o6_7gFLjO%LJucHTHDnPlUTz|LpAT5nIGo;rYb4tb4=xL>10)$F*_k<^8B*~MMt0lRV$?GYW#TkH$^yId7eK{y}5xgV?yl#yI9KqZZ=8#SH*?;#O*VJ#Sq|^9e<RRsnHpeUTPL=A_fI}(-!W3;Uq>($s&r?hFN=`SmGWnKiNT>VQ*nMI4GZ{^Le`#^a(UE#bgx!`{BgzOgqofnWQJJNEp9AY^1J=b8VBIkv)rl|GDX9a|9%X^oktHFE*GlXe3%t&$MXaAU?p2g2c!C`%+yj-NN=o>2C2U=i9jHE31#T>kah;w@4qw+h9G<3RQCfYgl+-NNDtj|=J5x%k=Ji0kXGykN{)(qut%D@v^LeV>!ua6{W^2+9PXA31$Z7brVUy`MK6R+?DfGSovrxOw<MhbkqoMcoc;vXC@V+H?N4XH~`?h=?yOq@L^Ern3MMnq3^z~<t_Wc*{p(HF^mCq>&+nDpSOcQp_wu*@u%G^sVm0QwyC(@s5l$d9IWU0)~QrR_9b0}6lOgb=b5hXHo)D1FJ+a6lMGc1+Y&MrYV6OvOFRSHR0n5Rs9^*|2XFH``elxJ=+w7?f4^Yz>zt2(1h*zSGSOw8+nnazzpq=)E!^=~MzzmWu`?7LkN9s%*uT~5vaq`tBL&<Sk5M@#-H)D28f5ZJ_4c!N1%brVo&<KQ(82I9Cg9qN^ormArO56?AS7s;LLUabHn-6>f}Zv?iXR?cA8DYMYQh}zvMf4*H<ji_)R$b7^^QcuK7bn;B%7)s6iEpTD-Z|BB~RGjS!vSU)o6`nKcalrpa=1?B&L{3ziD@K1Q?b$qd%ZvMP<1wn#4Bu6KIDxFXpl=|>vPb^nz#0uC$l*AXnjAieR)r32>2sx13ExsU0;V~H-Vvn;H`kuH16&X!uc?)7E5Qpum`OWKq&-qJ;h%RIVR!lEX8_<ANkz7~k+o|(YkS!Zj2gJ&#uGfaX+2$)Cy&yh2k|J$7yRdiG;d21aUrjDZ<oC$B&m2MI~=)Mx!*ev$sx{bUu}-iZ$C08!C%q(kiI0)4=H@~6q<;+W0cM2hF~I-?LN1VAa{?1B;ABfJV~jv-`=o@hYi9pdG(+DWW89|y$GG+q$B(Dj!Z0KLf(WSiIjB!nI-F_yrM6yk$d78?B`d#z#?#`3|HvFeZ16px9P63^Gr<ir}?OoX~Sts>JP&g@s;>cAw%;iHlAcl0*B6{pys945;v(hqR=af6rplR4vU4zl*EKIGQm522q#*4(@r%mQf(lBNNvR9W5B%=w~`wUH#4k9Q&YU@WAn#vMTbBFEixfPyZ_!1Fwi3POWfaI2|`+q&>Wh&;Ed#QRETf;c#gX)9Dg8`WjUfd<zrmIADtOOKc3SOM&6FYrZ_@M*S}i-Jg*?1Ot?8>JR=FvR|!igKEYtF0H+YlwKe#NU_FA@7Z}3@kg0Z=1>YLoBu~y1wfdnr<%E;34J?s-_e~34VnG@ZB)Otaq;qTm5+tEH1UrqX4M$oHif1kmUgYF*Who(tN%)xB*kw9|Tg8(uILk&npC0jeyJciUKKx^^_HrVJ2PM89pcD-UVA`j>mzpK>H*phUS}$==DAmN;Z795<iem71;pBtKsJoVi#-EQ1aCNV6OB66*en?-?i$9b8IO4u`(2I@1DSk@|xW_o(^N86nU&Q%9Ui^RmL;PM(*n?cw+yoRniC~p7C4V!B&xw^4RClOCHvmX=Bttp0v_!8a#4Svht@<8E#^}jsf=ECJ%_?03Ct7T|=8<7TY{aBZ8-O&84Z{p>NT5y`k&~n2E;^ke`f_sT`U1YmO;Sj^D6VzjLB_$AlcBWsv=k2KODHWqNp*#+->Qq`4l`*`J;)u%W(Vj6+)?cW#;^;0D^#oDwMKXjgh9DEC^jBS3r?tEeK=<#lHpg&D;(|R6tr{Wx;!zi`xlMtdXZJ=6i17yQ14_pyPPBJC1OQQSes>CR*oe)H}ULUc@amO&s<7J<9c|PaXqZz1T?Pe%DA4mt~SkTmcV?$zCIxJDa9+Okmv!*REN)|CA+m5)RfZs+?rNZ85UnIa)!cNdg3wS$zaG@(<omwtLafLgIm_!(JSg^QvURo^&fkcjI}dwG6O=nzs;ci#<1kgJ`?XxtKf=E=fE50`Idvp*;>hFT8PmS$cm_0=w0);5Vhi~t@4tb2A?*7Dp-u^fck+b46|birRIKxL&$oq8`J$JQr6&{YdhzF<2AM_RJ_H{*~bGchn-z?#$C2Ss9#FbkjI;}?QzHb7|HSg^)j=Z^?>qHh>dOhYMGKZmmM@R&z}-Zn(iM|=)}c?xVJ==a?<^O_84rYLcQ>pB=VP-aXQgNJ<wvc+uJyF6mvxw&@H<mi$TEJTtF*^7$0TLJ-24Fc{g<9DNjeydZrF+$S<!#2jF96_HL!$xNxad1sn=8FYXI1L~_TM8&(G7rix}yT=RU;ZGuwY6TtzFkXvAPQG*ResmDV)Zc^Hn>|0pbD47UB0Dy!L5%>wkGQ%&0jJ(A&p|MuP(kX2x5nS65i(K&dR2Q?yp_NhPm4^mLpdkMN4s9s1m9^XRhJC1LPsc7I%ZnnIaG`h9od0#Ce^I-xzf8c$FEk({2~%ro*{_p|j^=q=W~u#55hy(k^iHk?$QzVZ{E}k-CS)(}=jmtF{eFlZ&P;nVV+lht030_QlAflxl^hwPXI%vmAhYa}j%SAZwLjB#a!$CyKxmP>iU+^qHai@SoPct=vKj|a6*e`#knew|TD;_A3YfWtMN$wcIjB3Gff;wXCX<l%TmHNb1jy;z5rNru0xp7{;S9>8Urx>Y4!Q8_@8!dO-)%Ol=Hcm1`;<N=y^B8P`JL8NDunL#6?k#8WfhI*JlQFH^k&;fTFT$bW}D5#CZR3Nl*$nM<t>+%SwF<#!e&bcX;n(Wai`raJ8cP@{uT5w-Eoio>|sar^Y`LUnQKeK+2-4AM5)-RV~iK`1zk8(xrMOE!It*#8DQ5jLk$H*I)a5!T{*?;9((RU-mR+)|0Ifza6{C-ZA;<jmkpfRz%n8V5j<rVhfS#}Ma@ui>@Y+UhQAx}FQpfXKtKJ%J-NvhbBqGK!Mw;Q1S00^^bOPmJV?)3j3PiLFv&hq$b#6(Y2?Z9xDkI!V4JQ+Ak5UK89hYSJH|q0;?-c745)c#EBG6)Oigw&rW8*_iKwjK*kcaLV1@&}#6u>7K}r(4J)=!ql;;%g4rPyfnQKbG<9z=iZCX{0nzZ;BuK$KS9M=)0cR}XSHR=ZTB;(A;SgvfsBqtpWvFIN3BAY^)K^0lEWnlOop5#=%nc$|G71_)bP6htb-$mc6JMZZsqd`el(nOweyFv|L9jk+duBE%Oh9mA|kMQFJ5DCNeo`K1jXS(IZtv`3Rl9HF4VlGvLGrWlBBdA`(H>j%zkli<pS>g(nX+#nfxhTC%Pg`56VEP@bus<FCU@kw*>5<s_9U>OC`OZV|k4y11g5c&Y1x<~0V)UM3yRf=(^;mt#2X51LyhD7zEkl)PKw(68EW#)p;k0D-c3R32+knVTaL>KxMxK_5HHWeFLqlzK`(oTMv6Snoknznr_{-pRi6isOzHFk39-hFmf687-Kc<QaDB;F=XAUZ)SCK1#dR}t7%@U@bFV*uwS@aMRx2U>eR8m?R$K3o^EKaC0p*^oNP<xtKPl3?aD8;vjSWBue*YVX(-Y;aXxqQc4c4AQPoyPGiIJDlqYc~_Qe1M6(p@aIPcWwCADDE$YppP4O^gJ`7eqY?XBhpyn23VuqHtuz*DWg!Aw`@h5S%>44?u`{qHp46S>%!{89&LWYnDtq<?El**?3NbGYpNS4e}0*>*QCK*&DoZg1RZ+u<_xD3_E=imPUw-Ry~3;|$E+=8@d<K`$xJKoS`v@#LSD~~Cmq*m;q8cRni9?@tXK*L)<vnEQbcfHO;}Y%U}Xr-j{fp&-4P?CykS-;_M(idDhUKhv;<p+LBtcl#8sQ8f`cNyMPzfITYUR8G1~P<pYhLxyI+J#%ra5AW8$VAD(o(`6}}Qt)(J!XDN7bz?3KZ<IkhT}M}912^?r`&{P%)A;S$)}z9@w~y!UMiVkJH8P6hGDIVu%Xc&)E;cahSNftF=ne~7QLds_YDR0NBt<u&Hh)~gqa6Q3g3!9UUs>Vox6o`lg~bXQi|`wiDNE)_zecjNYHZBQ>T^P3K`iBA6iKD!{^a<;yoAXXGBtY$9thw?6oEd1I$JeA0tl1HkFbBXM!?>udOe&(vICb@{6jPs&UmhS$tP^RprMBc#Pw?V1rGr26G>>~b^a=D6?@l-BP1egv@E-UNcedThYT;5!g%b#U-<EFpy>Gk5LaLn{BIA(p3Saz)x=MPYdUqLVX9<unnwC0Cu#1p+)617buj%!zz^L^s4FBer~@-=w1@yl4uO+MF-^D}(1G5=<QWBzN;l1hEKhPZ%IqxQM~8h%EbS+i{}*N#pBhK2EoNLcSaf-owJu>uT(C_!6yrhzu1CtQBvi4veiF=*uK-vMV1#*eW-Cx+@&?To}wUmOU*;(W_)!i6Hn4^;OH>Snvk_kWOTW%Dowc!N!%!wmZ24j%ZpKsmU@qvF~CUx4Zon_R?=M*9iedL2RKY*ip3R%S66gp|L;qK?)HQ)=gMkFTCQmsIWnzMK)FfS#4qeR6~P31!pgx29hiaHawKg6t@yrWQ~rcbA>v!v{p3QI!0|6aF3sb#2k+r!3S7&bD_TxD|+`)AJ^?uFNt0fMMB<J4{m(8R<LL<I3Opq!YI1rlvWYK)yC$Fu)yBvzOypX6}WOg2)SA&D`9kZDM9|ecj~M%mt43$>fE8_c}k2?^%~-Zr_R=A(18L%V8Wl8LC`Y8lltEX{!p7XEPVXz2}p6{GiEu&D74GyC-sR+vGj?J|*4llHzu1icBXg>Z$LY>j|~Ue=YpgIR8W8ahuD8`I2v`mp>BFzb9D1#^F8-iV7SUP@tMY5&7$hflhnFEJdyMy^cJ>v5m0oE#^+wa^FQ|UJjY5tGOme`av>Y5h%3573OPnU1=6;<YliW0{jMG5yVP+VByC^y;g7mk<K7GzGv1~b-*=reb%DiFfYmt344FX9}=I`tCD1ZyBl+=3(0ptPs6gUX5L4KEO=2*9^VQVtI9eKbVz$Td%f}%Ve%i8v$+j*b15BT!g4*+Q1dDyBQhr*u@SDHWv!OyGB>Z-$d@xW$%q=yGB=T$!D=koGdFWS$<9bEJ3}SRb`&K~YP&c1TGtZvQwsvIY7DTqSxNuU3zp<fK}zD(ioA>GfHtF;kC~;u&fFx)HPuQd<ycC+SJo3`9l*kJBOjKwDF%wqscZf(m+5xzPO;P@ang5W#}?#t$8qahrnETJItNduX<_%KN?I6ADV}s|>*|*<WR2~MxRc6p>llk07gnN1em(eUfF0);mUM}(D0~u<XCUI6O}A8lPMb<j?F2FrU1!bZo1zST7M&5!J9;V3m`=&aihd=;qcFiSEu}ZTn4O5&Si2y!P<(L$)<GO^#etoxE3e)-Td&tbOGoPP6+`bD#C)VD)AcDtgnVdiPDcjd^~bEts<VqPjdv!v)?NN)MHC#{t^L78jjG1yRcp(Ue{IMrmEFkB8kt=#Yo55{GpeI9i$V|o!N;;uR#ePhvr*<X8znSH&RpumTiZe>&m1+W3ZhpPUCmB>RvIm(sL$)*2waK3ZYweuo=*^o3QG?g282-`tFc;cxOW6`G19)XpI-%5^oIXs2IiM_>k<*t$r<3YU4bB;=sJ-So#~lm0#NC51A+&Ej*~M!FO-u^wHTQun?ig_8wu&j9g1X^l^2hlU!-S<9D!X@hm@AZD^f{MeP%6@LEP-hU}owS3u2{hBGcrbeDA6f*4a0w+guc1=aHSDKCLiO+nHWu0_*&=$b{U9E_=tF1O#P7Ug}J++_~h)vDAbkxvGq*C#5E8(>VK?EN?CAXjY;v?|1aA4DKmKlB)_%j3=bEbt{hvv~J}<>>NmsamG08z4%1Ax5x1xj;hbR;Vfo~jV;&1&ZB{?1O@6(?1d`$+n>RjSX^gM42l|Gv?gQ(M|cfRtcfa~qSyJ*P<s+BoVYU14T@Kr!ov%uFt@NP5rTH_vL>GMp`BP0D>qtXY?*+T_cSP+z<6y9>*DaKcW!^ZRFFx8TAr4Q6@GJCkSRA)!rpHF$cr=UeG1wu`K<bCPm)4I8hEmG>h{7?kHzcB#2bVk!Rd8rox>I0oh)*$@B#H>kIOrP)=7JP9Y})3bQfEjTHy!=5cYXo-Xj_|VQmvHJkf(T_=3ON#TkG!B7F*>u3HX;HD(WWnKf$g+rFGH<|{5{yYfws`a-sh$3GJOTAY8G`PYY79vqJ5IGtR+cf(L5=3nuo7i-0rEa-4(JnGj3nbt5Dly1a1H^GU17#30T2GC}}W5;{0GpJ|VxOFwS!M~d;cK6VNipm)lGZ9&y2F!`_sNx#dJ-3{)gz89&9zyxvt(%nvJfoQCzhldvlh_qki^u#Kpzbz^^pB)2$}}st9J61#bNnpCqaC?jcuk3rZ+HCut?25Mm%>5Qn=7<@)KC7zdt?0X1vbmKpxuJl*-}p093*x=iz07(<0;bQniuYebN+_J8UZPrjFQ2OzzMh9r^6AIUt9Gm>+gHAblN!W>1Qtz-QL--JRc!3a1k4Psp322L8A?OM)^b^yip}^B9(uFyjiFtwk%Bg?U198)p=g;IOV>hFamTbJ%T9?$9JgqmF(ghx5iDOVZK7<^U|CiX#UK-Dulq#Gc{J8F9L`LWAaJ^-I-<cZy`N>jP>U^`^_*OO=Beab!2HI0{{2)2G^Mzls&<%1Hwn3$cVP;IQB#66kzL-q+SQ5`iE|Cf&j=NmRPC8gcrG3=#nT~XD%778P`w<M|psBePwQ$7})^KR!Jg|51<wFx>Y+ISI*AhTOSLt^w2`SRPy%>r1v!)BgplgLvdO()J#RL?||r&a!5?&+80pqnaml4OHZ!!78q@!REt3O4q+mfSSO%bcCUIt0+gVajqto7<fR^gm{4hI*)cLj&L1a4q|2q%rnb|6>2;gHbIy$$qEcq8#Ot9s&#{Fv*jA_lv6Qq5iB0lgj1iqGby(g22!1w`nZ8+RsY$*I`N?C?G(3{?F*k#GpsX=wSEF8+K>h*2e?%@Q(Jl-uB$lPr0b9&Xok%l;T&q27x+|)WO@|Y}Nt_zAizZt;gLLpP9)vfgtHFLnz_!$UiLVWdo5e|<Hd02|wlFpieDR`BAi@7n`rz8D7u;nV+nclFZy!JGV>-U3x1RaPZhY&L@9yJU55G;|-vS@sy5hpe^zD31AMo?~KHt{wq}d<)@e|31w~6{4eSD&K)o<@c^{r#y=eOm>kMH%{-{RWB>5=qtAJez=vA+5vFc4n#-9N5dHH4B@-^Ta&c=A5J>V07%9(lL*=2N|<%dcKZ_4GBV*y~cq?c~oL?-%R4HOzv5DGI;QpBk@~-v9_6oPls%=ec;jE<z;}J46}5EL0)bZI_QUSUI=4tMVKO8p^`ODj?cClM4&6Ag26fPykVX>EzEVV5y+(>_-x5jpcRX34D<4$qyZrvpy2Ne$@KN`J1%5-HK)L_!H#;sMKBb`n~?u@al(JE+}}u3WTdLYVp^oY0x*kbX-NriAil-qpJ>Iz4tzktCs76H7rke>|4EQt#x+I)5fp5jtgh?2)PyfWz32Y16B=(^X!VNI66K4N%Q>g_$<qxH(>d;b=rDB^*HM$t;cbBG_R?4`Lxx?=nv(S({G)G0Mo(JNa9Lm8^P^a1rPA!iWVZc6P4<qzs&bKNAD2~ZO74!+}2Jy9^oq~*v=2W<Mr}ShL?WQ`u54UxqX{k%a5;#BYt+!U(cT9?4x(ZGmW|2lGP92aYAZaNp8a7_=e@$*1vk%@_6B)j`w}~yhCgA>Y)CXUoA(DEj%9N5D&+5VhLyS=i<lZ3McJM&$sg(C!|*F*-txr^YZJ-HHY(WQ@d=s*th9&gO{)TG1V=d5Ef6m^kP4s9y~U6J*JeIp)on0zN!j*ShhACKM5iI{&&Zz8&7LF<!S9N^0b;zx@MgG4$y|L#f!Rz_19cS2ShVUK~&nBHI6l5YE%MS>^wFNO6$t>M#m;}amOROS*)z!5u1AEo^6p=U}u&MLI`%klw%$8v;|ER(Wk&!l<Rbjf-P82)1J|DqPh2+GG$7KiOtLQ2;3q2psjNFC%@%BBe(4|g}Nc7?RLdyTUjL7*%hsyi2wCYN+`QFwCFwK{~(X`9wG#(!;v|I`fS*Q$?h_yk%aJgjz`>g%hKqHfltI=?hsiX#Pxd>NHCoUc4r}B@?o5C)qdL(=w_Kc#C~-r<i2Sg;7Y3`-nfwa;>bLR+!ynvp3EEdN}Sr%Nl2~86QgA8m}vcB9ize%J8&g4hSvH<*k!0m9bn5M`xvem8b&|Gd!Iez^_&zed@_Ol=yx@Nj%YAGM_YQSExqAn>4{}p842NJ=?#PkC9f7IP^VxGs4g_D`_fZJ#a}+m3J`jc=bk{JtIS6t6M*8g8wN?Weg`5_L_ob`m~b<tyGh(4xWY7~0sQD0aq8=I*D;j1550;x6Gn<PdxHSyfkoa1LWGuHpVaHWE&R{k?>ib8UxoQAA|szkU!UV?Y_?;Fy<Q5>l1<R5r`9O1k-V^-fF!wgUNz_hsiP#3>4@p71Lclz-;Ms8ST7YzMATea7?n)E1nw}edq_^RLM)R=(8L#;h<R8T*Of<Wm+n=4COIIzW4VCTa(tZ}RnSI;%xmW*T2KX16$l-7!6I`UPD<BQ8gO2?lGw0BEEIlB|0Q1(5r1~1Pgt2kvVnoNMdc&78c<21Q0Y<e>0T6%fLlNaOaKDho@Y1()#mNO1(dqe5U+sh<+B$T`nTU30DMa(EkgWkRyy>T0K<yPwpio6zRjqzM{doaq&PrzriS&!3U%}i*3_PL*vP8cF_#<m+sG3D*+MOPoOzpAff!ss4kR9luRwV|*89U^!bUX=soMa-XaBCONn;XeT~E|J7`AvCIC=%Et*FF|`a&a=VXv&M67+(gv$!_WBx{ggK`E4((A+W*vplv!(yCm^xeTCR0dt^$P?2m!s%{a9qwmTwsZ({0;w1F1>Mk>c_>(g(w)vEcZ6@$_v*Kd=qH(d!jf>6Ny`k;4NpbU`Tx?wlLmx(Ru~`G}0OKYqtmE(!dh?59876}FNXPc$M#pwS0Nv==9tp0okH3<|xfuj7|5}V}i9!un)t5=x;=Cqh>mp^`k(aG3ylg@yikgjp>qvZBZ0u~2Wyl6$SDv!7Wl?9po1iT^L7S_S;%Mtu9BpOA(N<bPEOE4f_L4*gh4s6UNlWonl@lk*``}4B?C|srnc8M&YE$_@Ftt^vtFcez8`QK&*QZQv@foJJUnIo=t6q7ni`tdn^&DRt?S#ARwZh-U+ICLaR?aEg0E4S|gZo})ZOfmQvhB~lm_7C?+Vf_#gaxO)VCpk#&U-PRES4Dx%EglD&hb|LRg|7of+%Obl25;+i;07i<#)ZZ=z^)YLu1PrD-CXI$7e6;g!!0SidglGj&32289-5u>bFZlG*jQJmoccU-U_V<Y6PLw-1n)F3Nt4USs>K+NT*SmDFfO&Yw8uq{d!Wf*_pPy(uSC<>{}`d&Fr$ML~cYyeML6q&V6DaRQ^-1!jRqoZ9Py&fMBu(RP%fnYHlpd9cXO(Yvyw8OgkX?rA^ApWHx5ybsbQsqit%F9U+rTg6DW<k=M#H7G1@e1CQWwqaGSWd>x>P1j8l5{1bo3GQ`-bDl#r1<x!3iC2M<S*_Ptf8F{=XRB~V$5^(x=Ncrjjy0$B$+(_j$S-Q)f0%EX3RZ^S}G6Y_#cstSf9=sX>Y9NpIOh`h()npq6k=q3e)h^W|>ji88Y!6`GHd)XQkULOg`G71ImHB`+{r}VFxTG_=q*ZBp#}NatbYcbLKGvPe=5k}o<TDmI!yw3ci4P>JVMPxpCL8p2Y0C*G-9%XomFbHGEXklk-?w;}ww2hEta%$$)3|Vdp<E4HRu6{Y9P!m7@-CSXi`|}^P@z7;y?&P9lJ?nS)s3b=R`lGg5&~?iieXB{$UVnjX?0LYnLfb{Wy(~Asn%l-62926W-{p)s0vf>*4{CY8VpyFzgaO2rP5)7M90gksAE*r!U=znSwmx095|U-cdUwpe&`eeVw9k$Fl1J8K<t>2gr0<@>zaL`Q(VQCGdF3}>s7J@iXS*cpdm<O`uiWkq9oZ{X+3q9s!m+2wpyHBQdn30usVNIlfx?tr4mo+A|}e!6_H&zBeHwKnbZj%Jc!KUSn@J8+NAoFHi`auF(=W;Wd74LBr`XSHYq(%n>05ryLZwiiQfK>$-d=^oJnlVn$B(x9*9|3lix|3B!9sfZPHGh00o6SdS%~F+_yqwPCB!#E^;PuNUxsICZ*3pXZPQ~Sf1+1EUquA53v4^)hg4u1_95c&)?3yC`TotIGYKwySm(w>7k29XFw*)Nj-9Y`OJ-H{3b$JBMCG2>6p~jGpP%Q$W_xhHxiN}b7Klq5i#2pyr^(@lF_C7J!P`y?9<lSLff1zp7;f`t5V*@V@CQasV|~P&OitFPMUp$wN)tKK^M`<ia^bR+_A`NR>f4QMSdwUKp@dIc(RR?K(sm7osrRT0il>cW+GLadh|Y_C>IzKPI*keTRyr!AO2G8ej8GaY9BVD1Qxixr&T+!t^`ZfdCfo0%5+bP6*(gdCsgG&YE$)4yb^Gr#y@eMR!@v6@P8w~Y>&xYcgYAmeq~@G6=lNUE*nY^R2Nd=C=^pjdzkR0mLrLN(y*kqJ8xKUqPFtDn4W&4`-E&w*!laU3~H}`5$OBMvN(zYmY`Q^<rb8+^kv8j6JXQZd5sV4pXDIi&~ra2XejTl?G~tUz>=p0o}+{G4YUW<G!lw6Qq(6!#Nkcez%H{{v(+sa@x`ust;}O(fswo7AAM~_sh=RJXM70xG2DcB^T3a`Vz*#h-b>v;MRtF0TcmByUOegn^r!aUd>@J{K`>`=<c?|k^!{CAUf|69VAg-Sx)(tp<34*7SA#?5A=(M)fxM8`Ne`jFk6-`v=neheMOSF^gZ9toBzw7Z+A*;uS}i5|dT!u3ZsY;&PDNir&TGEabYW^rrNOC<8grGEt4#v1E{f9zP|X%6QQf8{PUY{Ea<(`-llC#s{b>oweXB5;S4?lP#fd$Uw27&?#YRr?p_N4ki91~n9fWzqrFe=mIR?Du72QzS)8bX6l%w+%+zaW@fp4R5r-18(OyJP*l=a1;QU^I)6N~#K7*cU%NFm?v|N3xMY{Y7Pl`6L6Du1*#c19~)-=&S^rj4ajZLGXb8>{cq#&&dlq^6BsW)}A5y+ajCr>a=WOMRkq2FqFGH?L-}>}VpKsbVU<r!wk|!Sb>yR-RGC;`6H5=ka>~@84Bi2GhC4WtQn2;cPakG!<>0!E<Wq-d%h<u9IO;T&3HOnEP#0ZJ`;LP(l0;)oVJgqB9wmc~*JKB|yXYh-y0)mUT*P&Q{WF^enzNu$DwhPeL<_%fO`?6mSuJu!1s0@syK@3~S^(6O^f!f-<-CkNVuHq9|;2_rxX~;}RDn9xssRpA0pV_H-H)gtM@-9Q-yX_exeg7d#P&3NR^9KH98VoKE?KXl38hnvPCHhpxyTveC?qpSt+j-&&Jc=7%s|B(bzvGegzNw<NKIOBh-=hGtTFBpF39<N`VJF*EX#uM4Vc*G=9E$yU<#I%<T)NmEq|m{iY&`f+T$z|o0Nly#e_n&aCqhEz5Ta|uI|$pWoPAPoz~@h%K5Wl^t8B9LMQNa0ZSFdTwPHHu+UHDRF+a=2uAD!2QVYY|pJ?;giQ@wwrAE4|N0*Y(%{7KsGEnce^K3LdaTF0GWw0pU9@4%$Y?BI$`Fr&)qkQj%*z#bV`;f}=>rF6o-Q$|Y|ToQ;CSnzVRmhOlU=qW8k>Wk#HG5{D3-R}rB|S3`prvi7=^xFEw^s%hy#YH=x*!>mX?&Oy-XkAIt7F^<Q%z!fvdoz%aACB~lj`iwn7o@-KK%D$xXCA)Ky6uV|o#D#{Z6)Ph}%oBc?H3>RhzuQx0n7SB|yAxU%ZL*?~7yvDxfAl`xx%mKr2X=)G{c?0w+lD#Nju0VCCLzp@h49MXJ^BUq?^#e)b@aN+<M6Cvg%!(qT4gjLt~R6fPGlE8W2Yk*cnxBtJH{Fo)oB>q`_QEowFfIbqtKc>0=c;ZvWFXb(~saLjzem`fO4d!>*mlnm7EYJd;Ea43b~?Gn7nB5^RgxT$)a|NZGRC-Biy=7MlXy<99ip*wBKTH5b%I;Xt?s}1O;@7>XP=mD0BqIDJNH>>?v-^3)NHMM*Y_A{ZIiHcq2bOh5fI-*5dpTO)VS1N7(=QHeAErcC^oMNA*WO84B=$BE8%q#M_Ht;{iH-N6x;=B^&7>8K^Xq#V6N8kUb1$4u#`yVbwos!?(e@r4me8@H51fm;1n3gJH*b+@<fa%h9$6C=NE|e}Sx@VBM3~gJd2i2luxyd1jj5@M4fJ<dDQLiJA2XdP&505DjKD2SEG141S&CD3$srULSxOmjIMq``(rerz1m8-8I7Nm7EhppA~?r3P3S<(G@$G_Z_25J)%RkZ~<UFK%Zww2N;JQWzt#tNf9R?SFpf(QUv0fAZf$ahm%o_C?eEjXHJP>tGxB_6fQChjOs*Zt-%i!x!T#4^K~SDHj8GkN#KsKi7=4b7eT5HZZ<Xpec|CUM36$KAQi%ynSW{SqL5irVyKOQCI+nNOlK4hv`7iCHMA-rRNXVwHnQXt5Fh{Jx32uJY}r%gUz33FxJ?(u4_doi<0X+hP~DkMm4D`#oZ+&fNP1NV>s0f{)n?cE8O}^)DX@^7R;w&<tddXEexg61^E2TE64*Tm<ke`_DvP$e_#K`>Va0c&upGg)qq=U=Unnmi7Mjk#bDbZP4zXtNKRXI*(3;=7a=BelSoT%7IBH)*6e{M-&kDi%&p(|p`o8lqopQg~e58-)B2F;V^YRoV*sVZ<Dq6lE1dFPjEmKliM0GVKJD-nT(+JAxlvG?GHybp4+>}&HKpC`e(~#JdoyWB(*w1Go-P3nI6ZZ?pTYc|oct%+(aCmgWPHa#0Z+!@T@iRfBdUJ^-P*bDI+r|>&7pKM<gcRC5=*3r_)F+hUnjMYx4f3e4PT08M>jUYrs1$bCjHpYyCryIM^+I~gXmMp1Of^a^bfh6Y5v+zqe`>)9C)UL2h%i>Q7Z%`Tt^#+6K6<6A9A%-<GX{GFPlYhX5Io))bEkL_2#SvYP(b1@jX9!2rIFhop`V|>PEr1MzAHpiTGeW)LX?`-z4pbECGLzqiUio2L~HvZsmycFxlly9dbBU<XfnS6nO2ji%H~5Y+9QgI?6hGxqL^rnNr{l3wJazmx;)@*BZ`R#4CjOtO;oGMgaRwWn&R4R1R1Qg!I|pSYO+`x_Vh-tuuN&^vK8|pH8gp1!C%?`e)`_SbvSps9}V>uME2oYqt6&P?sVqjWPgG_gI7HZRpS11lOxwE2}-80p?8vAg@za08ExZbxI!O}xHA(gjpGrW1jBJ$e2rdQxj1Ga6#=NMh1_?No=UW0be)W>WSfc)OJv2AB}GYO(4B|bnjd`YRQUv^a@@>l>k$YmLZaocAq*{Z=r#c*D1|}0I<90wc2=Xew~znb8!6Z)B?WuynKu%vw;q1`_}0U3Okr<KVQ)-fZ%kotOkr<KVQ)-fAJnnG#c0CP8%>x)e_mh;3(Zkm;*l>5*}~88g$323ijIP5{-7Ow0CX5JHI9j>QFXk?Mo!Qr_FXUgM4$@OoqMt52(L`g9b@1N`;}uuihq=YKdl(7^xhr+%(-#*#)_%RGq9gBZ7D*p=c>nZ(tJ)d<^=yMx~>;Kx}W~^goWu0CydTBwSJIx!iq>s!3~binsqBA=PV27%vLH(tHMhhTqcb!oLOnBy11QJyIs+2o%VJ(J96G>N?~6;wU0sx=d59@bR*)k<Djgr*4~`ZhaDdwtsjA<u2dDcwGExNu!9|$&iuJnlwtA7Y0r^}rHkxf=c9S@le2T$#}$LviasnmVMJ<jqtNGHc+-J72>Po1aLphV8Z(zNuiwd+^c<7d!nE~H;;oRv>j}a_avG+y-yYw@CvTo(8GD{%Yhk2XxT|vaEVI=a5!kB;&feMP)ti@j#}?ADHGSK2Tw~7;;xpeKd;7@=As*i>qkK+=mE4jQ;}~&;{xMx5+X|Nso*fBK?!LTv>Cqbf*^wviWT4ZtKg=&(HmwQE%Cp~Iyux$e>PX=((<s;wYg_kT$j3L&b=1j`rHfwT9b3NwU3ePm`YYcOWVUz#RKAwy@Uml4s7Oo{XTVw3J7g_p!ekf7Y&wO^P7awx(nya)NF}*Bo8<}}dkT%cW|B66s*`oNV6ufbVy)acE9%RWx5(iIIE{o`=zDTR97xnclxhYBN}EF}A}mGrcy@`K&^ichkaYBpd1CQI%!98ot9Y~OD4|18nnpHY$eG1eNO@}4+L6+PXA-~)$`?k|m~7m!(rHwFl*iPN{Edn@z$1<^b=i4RP{#PzKMGJWFj?jG=>C>-<mmoq(vBQZF?sS4qUNmle1uXc`DhHPlGbXLHZ+BxabqGt-m!#b$(Jr(k<BR_kX9`a1%hjiqe#wM)-sa3vJw)}T2fL+MXO4(WLH2vr{0TrrQG2BN_{F+l+tt1eotxFB1lt*vBK3l=16)m*F>r(iaB<gE5S@?n#H{o7Jxs=sJL}F#=k7kiw`Rmd;xm#sS!Yb&?f9`qw(WVA5nE`AU@Bf66@8~EBmV4J(kUVoFBt3hA$r=GQK2h!On*JmKf<0wk7>Ik!~2qMgH2;a8f^`x4Xuus(k!C@l`)~2r9nFp2j-5*@+Aws1Ho~?1)$|y$8TI+`R5=4Lt<sX~TQuX55B+UqZKIq}1tIfP?Q6iosR#QebDb7H*xi*Ht@mh|~=hB~#fD=Di{<Pa>RCR5aG+-574f5k_*U;#@iyvGMPHmc<VijQ3jn41m`s>;HQ6ddI`?+Vw9?Rd>4nJFfry;`%3oMv2|ehyd2FeOU_RCIwVN+&`|sRrzHp(DH5>q>n<pM&A`KN`a7HlmfT!k^-A`j@qdd_`G18@=t`nibUe>XM$EKUcW@XWoZ+3E}XnJh3^Y0iZh?tW>eh*{80AnetY~orWxD611)osMU@BQB_5slY4;eeL;9T$Nc_BpQ^WuA-hcZmnC!(?om?JU&wMEHo*B_VRuDMPW^_zom^e^45|#f>tPqqZXdHDZ6>LNMh2%eL^kxiM?1F1=|HB(h;;m-VTdeu*<695EMf2Y}`3*Ah2AOz+O#B0?q{TPX#2aej4K?u(I%=YSJ?0^l`oh7B-@Z3|!YMyr3!hkFC+h346J0AggV6b|MTZvz1y@wZ$WWJsonU+}DB&;nC6<vnV_srSR|qWv4ln2smU3Syo<!T9LMG1f5(9%->AXbQ5h;<}Bf5r6gwn#_m!stGKuw%MGM+*v7^w+QAsolzYV&!0vZcD4s)BhT`?xB!R+Vt+h06SiNY26Fo%+1A5Yb6hvm>IQgr|k>o>qxVRTTKAK!WicGVyGEIFV4amixyA8lft2a#?A<W{)SXE5NmqMSf&y@NzJwlV=IhpYHf*rzP<e;UG!ps$(zVCHxjo4lY+~)y|fpXlJd>?$Rf9Qff8W$c~W(mN-F5#PIa>Bp978gC#Bo^i_f@J;gJe#`irQ{d^6!i{Gx{1n~*RAYOX&0%YPHcnRg~y$&yN28Vcem9=Lc<c0U|F58x#MNk|&|Meh>i=9(0_ud5%MS3Zq&o^lS8ywGh4Gdsml8YY;3waqb@!Ct3XUg5J`sC@yv-x(0NI9$Y=D#Z56%BLJB6Q{5J(f=E>a7nhTWv#4P=K5SB>v_{#nEOE&Az~rQB^bPlq1T%-IRruz~hRg9P`fW87mQKGgBYN6o)~41Y(~~!^|MsSrA<@m8kF*h%yEdWdI-%_F~CUe1i3kkOEpxxrtb@=t?5_s&Qg;V0el=UKnnRTU6@k8549)JSLl#J6K(vC<gj$eJj%J4Uruf)fruZ1nbN&*5J(hwFR*3fktxfB@{+W*I@co4C}LouKuGBBPNKqp*sX8Qeyd*3QP;MI)q_WKWZRGCfn2?Uw}<>(kb;`kw+Q>YxHDNg_@Q#ipMRJc+oR_Hw-PNtI$&pwLMbwZe-~ds#3#U7_rK(+IEaE7nLw!5OomcAqno07(Jk*0&ZQzq5?{iE_kRma=0Q{a){i)k4d>08|jpIfeElA%%!km4G=@X_^?JXDF(#w#<~Wa)X`(71V;q$Uz1G7%h)vi49jS6k`*cGtf&Fl1Bs2DfJ3iEq~c7cMj)4yRO-b+1&l;0x<}ihSF%B<-d^)xehc2c1@GQMOK%_Fdibq}-y(N!k-N9Z-CN}DEpqo3xqFM;y+!WcB6lxG?&76`rM>Ased4qKEx&zD<c@EygK*s^VLKxHNh8OU=jzT3@~A1N)uU4Id~{i{ji<@Z`6StSiGr<jpZ(y|$lXZCX^hW>)y^}WuZ~H?>pa%?3fmp?b}vTmm@MpW|CZ!?;aT);USeVAS<lDYRS!Y(L5?ZRp1E9<W}7_CU|U#FfI+HtzH?mX3!h{_E8w+Gug1N)xa0+gbduk_#P34(vGDxmb;@=NL>`}X6@^p?(%Vy7{v(SLr@4f)6z0=rUwnkK?DZ(}?~}ad^9MZrxJqGOeO%I+kGag*gE%ZY8cMHFqIy2$q1Tf>4b189EY5Nvb2+{%fA)P}hj*V7UdTs&pHRzr_VH<~@P)|Nhkf--@G)ITf__&#h>p)^l8*Cf((#jk+Piav{djsB;yI7+JUOzSHm}Sqz8D<~`PrYm{CY8!xGmnxajvK5Tudll_eOXo_!ZB3I9`s3tzvV_`?EL8D}CK3(T+cUr1SrR%l0c~=_%TQs>NaM%G?L!=OFDXj9&-P%vPG4$O{YChd68@_^(aqZNr`tc-~@@RXvkhkzi9thR^V5sFyR9goIrdQd5OFQi(AC)0(jXv%aWlXW~r|M6>7FgbAgIgE(zbaiJhMvh7s^%q|foI`{2Yn*(_Lx5`#V&A3*qibb8L#4OW{V8+Nje?s{KQZjVB8msQ1?n+fnGt$ClRO2ZdR$4=wQB4CEyb8>E3#uWXcx489_|!pPr8uIRN)_$=pALT@mu)U%F5l0oM=6K&$e@|ckB8`mXMawCCkhmM)O*V4I~Ie<8H~7g4ioPx3r8W`rtJp`r8OPpCjlingqdaLXDXUi6y^9fqf%8;bsp`hf}W5ec25zIgY=0z#sjzZlZT)@Q@_iW&Fh^%xbk(UWbr-Jqw8bU$&9ce`Dt001sBm%Bo=W~vK6j&k1*_BbuP92<Izx7D76~DygO<2Z;>55iV&XIAjQt?UOB1ptWI{P8wFLHn{Syqzts3W=!Z%T(_M1;+aD4P+y$TRXIYoC0-PshZ1S3`*p>wIm|0Q}jKAv|HubEAjp_iR(sU!3ZiQ{HRrz*c?LXG5txi;qiwr2q#w1xMEzYX1(KGQ{6y-_vOjgxv6d{(%YU`o$gRMR%E$3EIRi%crA8DMq<w<UxrMxtja#WO&Hl^A%WvSxlacd_q4ys~><X=-bO7T*eNSN%g4AMtrNPgy;G=KP{i1KR+h(1SGex<&rrjKaw3IF|;Yzax@<5kL3J<?gQ?I-yvGQF3@sk+=vEAo3zfuXRht}3uIJK3qw3km>t!7Cytdq1n9RLZFCLXLbpYgaRBv$OPevMDp=kyQ>*L7_`&<23;{;O~y(kf#}YiakX?Vc)59+I1Z2n=mFZR<n3!LB$KZ%U)9+c0?l^?@8GIFT8g*&k*PD+0BG+h-F|&n=Yq)yglvU%e{-``m|rGu9j2}D&vmo)W$9jZj26%vb&?w3`)3Cj2Glg7mAoNfhVI}g>iyhwRH|&r!k?znRV5i?mEc8twROawcB))h!8E-sp!%DzxYXJ?Qgp7B(UbBFAouQJjU6()ASPcC8pg~x&y697*+L!>%rA&6o*EqB00R|%1*6+=v(O2g$n=XJL}ZK66u9Cj>6KfXPwIT>eRaG(a2)G6Farn1Z62_mc>9_3(QWsH0=7f?9qgs&c+SAXuEVb@Qo^w#5P9->Aj)wUiIkykA0idG&{)aqI~^&k*_uI>0@101iUO?JFLCax-%C<Y<VJLSp*4q8O+_}B9`1gKpR_sn<}`~9>#huz-mt@rX^VmP;!TwFKcl-rZ}0n-GrM6pc#m9C=DcTZ8mM1xSb^vP>~t^y-(-j7Bcu(!ash(|52a_l%4cs_Iu`Q;Q;h3o4(8T@&3V)&hUNOPj1Nzgp_;J`GfFp!#-?cyz26ow^0Xw@QA&=mi(}{BXMGJorvMghg+-&R6E@BUM1h%MjQV9Lwv-y5&G)`hk-TEZ1U{)QFU>4kNDwyKsAjY&8AtnLTsmf`3HS!nf~&NuPZS5oH}TWai$Pl*BG&FZ7b7+QwU55$BL5IRGYhXIY~Ac1;gfJK^jP$rG8{4pNK8ZnQyYGWy`umZSG^`$iezAT@eO`%8~Tv4XE;G1{r4mOmZhWt6I&-h(EKwDo^N58MT#KSs`XsGcv~`NYj+yTU)GOLzDa2pNT)kS(UghPO&^&OFKG#SryKd#tj!lKcHU^sr;TH&p<BX*~~QU>;yVmHz{s<K)`J5D{7<KtjaK7v&={zrJr9$iME;a_O67X5B<(8Qn;o;0>R=X)>oSKl?CQIN8=aA*_+~tN5+tLTq2cxT6X&xtVKb!ytNRoGrYuAQ;h}GBZ`Ws2sr4cI+f{BZbH<GFTAExZjpcsJJHyKbt@B9SII~=r>wF{osD6FF#9HmX@gdUOi=hb%~(Y5vCJH+M53Rq8LUj3D6vr65L3^zt1XE<=|)qDcxdCSwU>VASUK1WQx?Mq5T)PXS&>rFvjQ%vlyGtZ14wGnZ)g*I;~sYw2d7<VZTW_DAU)y#C=zc2no3VA!nTZWrgUAL@MFq3JA5x&SEN4wuIx}(E{rS@Rj9{POri*Vsjw-N%Jy>5S##d2DcjBL5q_M)6)Jkeg3v$=D$oe)8+A?(E!(6Q)yv4r%KQmlGoHv~+&9syGF{Q^HnIJU(+9DfqniV~(RX2A{41}j(-=V?XHUPqmI2R+8S;%yQrK2`dj}P0zC&SKF%l&eq|tmlWU1(0PV6deC#(unfA+{oLha11(U;QhVA_glOoN%h@UHD*+TVI)fV(Ccb)Zt|UU?fSB2m}~z6g@b;{1t7({vSv$=ZOAwqI0Av`&PkC^-Z+sm$$py5$ay?KKZ$xS6wA{&uFFgXPNljq()A?2q!K-r}|5*-v}-SKqI9Z_P-?sBg@YzhS@L@>aGBp{Ko;@xZRNJ*TR^H)X+~ejVLe-{06~#wvmYsg@<cbA$RsGstq{c<XME!r+t*t=-fn;J{x^H(2o~LfZT-gUlw=N+$&;*z3D2OHLKP&<)me2i$A$e&UR{hm70Z5&zEPn+L@SJP2WJ*xz{gqyz2QX-ED~OR;8bF4l~1v0xw`qETF(RfV%Xwrf@4x>uBhLm4Jqr*@aC1t!+kQXTBGf`NHeFt8)x;&7~3uO1@H)xZh8s$SW(>Xl2;diUrm;)0DX_MLNGl~y(|HxE|6P&V*Yb?fg`3|MZN>7;;Vw-l|ns})WVQQlG6#2|ExN=$Ih+^%ZLA-(bHeai-aW(KQx6MuT7*~G}-HJVLW&nu=)gk|$kOC6-#BJNaKN8OajDrz@|B(s<ZIgulHDR~Zj(A0-9=@^#IO<9rytOXt;L(N*WRjBu*JW+~?=0ej?xN9<_pu?W8%{C@ad1TlV8(Nkxj@fx+hV?-AE)ts0n!!W6dl%hFjO!#%)cgP0d$&+qwmv_o#-*x8)vS40bIm!|+UK0_(w$@HOTK(fr-OOgKKP;!J_`y;B#0U#A|WOwbelFBXgY~`FzuxyA{av>sGty0A^0kYKKKywV58Ep4UJKsebDjy{r;ma^Rg~`pR@N#T!+m%Yt31+W?e>&@xS~ou9~)#_@{)awOQic%WkpF%G<{Bezg{2;`Zw31~t)bGp-cndy(}7Mqy!#X+NlM9G9xklwb@wHk8Pxb0g={ywJwBaDM$RC<+i~KvwnkuBJIVM{#X&1H&%woIC0Gr7P>}V&m~=KD+~dR&w`qlnm1~dGxc3MiheD?Ca9Esaw*5`4wq-b~=*4b6@dO9pjE9{wqSEs+?d@#aX``M7MD0+tRa~UmEmFCFMMc*7;;xdS;b+mojP+uJ&a3c<aFP4*bycF2mQq@<y3>qfETP&ENifyTWf*_>D60Mwxh{OngTv6aH<KzL~?lktN>95`UMICDM1<9FEAe?~>9Pje<-Re=c?gpMx8ei3_DO$(*4+SP81tkqk1_=6X^~Spvn4V5J#12k5ICbY}lH)ni5pFjrmG&q7gTFgW|9qIK?|2FyJRuUF_3XG&@d=>OTDaVCG}X1-#&!p((|n7erjm-=Y)WANe|#D)2p!MjBsSP`~zi!D(22A4W<D9|k!3$trATDv*3cAKttym77E`9X^1Lg}S=#%Fkn-Y_2U_!WL}z;ilE<*u3VxeM92SoG8inP=34V+oF8b|z_5%d{pI#l1PJ;gZrYp}phF{n-3dPHZoK>m?)y_Y}$DwuqS5VsR5{|AZIX6Rd_OPi=ZPKEK;?UbkJ=UP~BA*S9=#N;@Mh%!KFse0w+hmM7G#&W4jwHQa5hGk5)F&9$_Gd%afLxZCE%1c}+FrjO4&<YuSo?P@RC4(FG2$#Ym}hb>4BOWi>Cq@miPuk$xQw&D1po;s!l_R*d?-RnJd>VnFBk*5~>G?T4P1ibvZrw+S~Np3pctaRdqp;lZPYSmYIj>ShOU#S~bS^-F$g^5mI3CxH=1$@+*k4{V57fiAXE3MWb;%IEVqzjooyPMX(Sp7w|AoIW9Q#E<SbwFH!*pP@Y@U+qalrD7ZIP_q2aG<%g38@x!gq@m49yQ(l!j6o+JeH|PYn&AP<d!YKt$E9Vec*1VPBI2>SPPd%tc?SLKJkNLAX+aN0{~lYK_D>VCayld4p<I$zNAow0C9~^brHK7p!S7hBMKC*S@j(~yS!QQrbm1n?>^c|4d8@=Qq*tA17Sb3<|}c>?iIf)G9t`}L=mw(22HsR@X9}9Gs4#SAAB5~FP}oo-t1Bc5Mz;ZQ{R}eU6^<sAjr%Z9h?w79%;A{ab6ISgE)gFkwZA#R*+l%i}rZ85OCw9Fhk%1##N6L4#2FEgk||qbp!B~dLRRL-V^k;O29>ub0hwaHzFCHK+GvMaW|+-JQk6^{AjJ_pl3c>Tde3#k4>4Gn?nDQsBR)$B>d4l;yrPN$R~a`hG6rKx99*g?4CCVIL`b64W%&psovHIs#imnvEk$>Y;1ru99-WbEvGQ~<vDzn=X@X6n7$eUz4C;Z)*QPX6y`i<%=~Uw!zK<ywI*NDD%745ir|LDp0qK}G|-6jFqOlTAc4IW^J<>gNHZe_qsM$mjBjOK@dkiO4O7~NvB?U2g~{s?M&}7AAk?I$kTi5~ML8$ZV@0w$k!|^W>p|=rei&c`BK>5;{eRhT-|!R9P?|XC2{~ws%3-rL%9%X?M%fa!YLvvp*cwSr2JUK26|*5vjIc+crE#9T1A)vjEGsj@lM^>^<UBbsQ#j@<;vw^?p)X%_dS(cvN}Bk*kx+;-0C1}2t@flGa`}oNIoLMB;|$5Kqj90~mb-xIs3Rz{6&%VI@gkcUMH0lix;AW<<J2n0QbKR|vze`a0-Ftv5Zg7*YobZ<p6P*UDqC{FO$_ul<ieV&ku~Mpkut@nog0UycP*3f6#Q1$jOh4o)#W?b)1uIU^6@1zsKt6Hxn-?~=DU~!9|Rq1Z_@!`kDqmU%wPI9zeNn$)sPNT`XZzY(M%`>{^z}#fyweH1_oyaChJOIM;lw9xWNm+RO|~TRnc-Y$CKqfB(0yMlUAJYE8)ou2_irB26~s26&=-HM?6^plUd>{xKIu>Bi#{&1CIvuP=wcvvabs;*<_hG#&+E`JXz1xWW^A}k%3~6vRJe?`Rqd7)WPqQLZ{V;Dx)x|1$n-+Qo!JCtpV$g2)uk4_qW_p@jzKT*G|@m9I!;=wx4*+{>)22@BKB<d;1*deRw74J<r9Fpm$Dud8Xo>C+IzL{r@RSKWIP-@&0u|yvGZ~J7HJ;XYrunEaDvK&Wt{=5O|4oj|J;4IpY!N-nTfTOQ3t+4wUl5vf~BT-4W|<I{EorT5wJ$tUL0`JiF1jnxOakHt4-I(7W_;C)|4!mFz0+y>j*uLf_*B^qoX^ubfHf_cTMlH$=a4aRT~13H^>p<SGC@Y-i~AG(*4tPA&;BB_;a(=krdQ>Pyvo=ID2x>|OERegO;~-*Se8kLO7E;zEqKz8iS>zy8_t{#tYDxJbBXvVRb)uVw!#*rl>gc&h<iDF7%Pk5&M%F2%eC(69!;>3FtCT(j0?dc7zEI4c8asSv;#qxjNVmtqK{Vo=*b2R5!5VQH{kyK5x@8Sc7q*<iZwr`o{WU^gdsJwcpSaOc;PcTCCYVzUdaXQ5K5)UcWJ$jic(kKyivEVnUCqO-o5YT1$@`KMn*9LQ(<P=$j7-7o+04r=bi3t#^)pH}K{RYVi>GL<=asaQ7$P8fh<BMZmSJCHM1naMmTXb;#J_w!`Ui$S6D3Da%9rEA`h;lYyWJj5Isc%JEaGw%W2J4%sro4qx0C_0h%MplOx$sbEazMhH1Dufvi<bP~w1nj3Rai9NzmtM9X<I6jUXW%UJ!?O-p%Z8H$Wzwhe4}Qn|6^Hrg*19k!-xSsYVsu;;7mD{vz4x&O1F|N=uzhg;l!sbSvJp-gg*iPyqWKu&(P=u(o9!5p)erdgyu;?;c09T6|9G*m#Pg*G<y@1ngr5>FPlSsjiw+5w2)}tP4QHwn7&^U@tQwUaLY1B75bKd#$+IXI(lTsimKmp};8dqT5X$M!iw0plY@yi^+Jf1V7xJ2gJjTA3c~RYK$Hwd=L=oA8YOIza(r6$aK1q>6x@)99dex&i>$;MHg)0R}gf=<cK!D(sm)WG(`;pLM8JQpLCd_-n&*+VUyPJ*$iyBxZTNSW5z64q4Y)Ya}MQNIR{Ea_^rJ9ACyb`AQCy#_2Fw|VMZ3_CFDOmXWgE^e-H_hQhIJ+h5_gX|N8t48ZqP>4EqWuE%3r?h6MzoO^IbMrsn-bB+WklPwIfK6*(PF(Pd(%D5-aHFuqdSD>*_-Vv*_$dmeHBGEzZt^D+aYXZ2-`wL>IniTrr;x=+NU|3oS!U^1*a7HHJ7pMi=$Z97GDs^+EaCd)rlqbQwOrYH3=K|4~=E7`Pl@E%$DISl5EUbV?8@Zhj|^`h{#ln&U~(UpmilLJ~{OdMX<<m!Dtd9yfntOs(d&|g{d^Z@VUu%iObTC+&0YXtmWkyd4>3M>Tp>J1i_hannl^8#X2~vd?c1kM#?)^%32jyqD9)V$Z^rqdal%whbLoJtpsNI;}nC+*o0Lx%A%ppQQZ}ol3H3rHInJ_syv0No?OBsmld<p+080<XDh^5vui5Qx}BwCpO;LR2j$DibR0*}YDoF#hOgX_B^f!K^XSYYx~s@nC7x-6rVk?(Jp8RQ$dQ-cs_2r!1F;<5kSGU&8AqAvPT3t()PQlPZgvpixegK_vl|Noo8nf-;BMr{^%BS^S;i#7XAO@@lh2R+Y09f<^6EHjo3?!1l0;SLNTx$uq;SWG+8L2XRySnyzf&8N7C25!E>NvS@iVg9xN%Ykoky34mP!IB3wq1BY$w)Y(z%dU=F7&ehzs&8-1t^CGRr0gA3ch~qsXr=tVdE?p{F^fW~_4RWY5ly8!LUoUC!fy<9$2;zuXdWVxg_^U_5)}PA3v(#a6DUT1a@BPIu6|**V$`#c3Ywq>SpQrO0mjbV;Y{yw7LaSKiEr+}K4coIb_OL}D%A3r?^|=dIcC{r{zUAuV+U`NnV;Hd3ffcFpkUJm82%cwQ7XBY@eBOVY(Is9-=unZgXyHH=Bwe=MVtj9+L;u~0y%3w(Rar(xPG@5HV;3DNVnNIGS+jUpPAKsXgqC^WhX(@vNTGI3`d9U1f3TVTPKL0U=21-H-Y%#1%>9Lvtyp(bCO1bvZ5vWbCCRkKrInVK78{5AGs*{!ACdYVa>bagX*mbG~eBa$^^A%NEN6V$|DGm@Sh<rH~_#>Q#3Hx5yIe60{*4@y04sTs}+BxbS*+~wld*iqTx*#S_zW6b=51pa)rJZpWn%r`4L{*eBooUji+X6yEm!}FL|R@_o{6VbXI#{9iQ_qLI^BOgWv8#ytCd;(_Sqxpt~0?ET2=pYcqHd|P2d`gPDB{qmgH`?RO){|m(&RD7Sjr!ZWDz<*dwn<t^s0mt<IlfMe1@RFzFE!j4kaF#Ibyu3$wJ%Ltyant+!iZ}c-hAY=i2oyV3$HQBRCc6EGYWtpkCnZY8A{khH-LFn6Er#67omR|?G}-vAG{7Dl;a6ZaTqE%OIe%&In7#)r8j^l)Oqz{73-nFCTMcu<2l%CYk@cQ7Q$+_iCp5K7?(As#leJPe(PH-w?ahoX1R4!e+0%VP^I)rmGuV9iZW=uf;dV$)XVy6&H8G%hOugv_0^y<g6gZR$8xw^M65ns?Mf4FicBpm71F9*R#yG9NGltM`V_>Q44)wtm|0}nd6`p|;Pe{IYCVTpp-(;OJ?vhj_kge4e%>hcPgH-!4ZpW~eB`5^zwRCbt$7UHs1wHM<o*zP$_B0ODMG8zoGGD{b@LMTeNHY-p6Y5KDuun@0|FI?)1)-x%S}!ciZK;jD(~ja2F|Dr<!aRthCWP)1DA%5duvX(PE=?iav@KD9o23b_hX(sQpws^njg1276pxZfXm+<t5Nco(`y*^0$K|-jS-mc0IZ6JN3e~DJ;rYzOs$7<SE1QrTtqY5wr?5s9DN-7i8IgeO+zs+kSJp&`;<8=CJP1eS8~{M#a*fEkKKFTsF@T@NQrQ&a~&A$r*vhAHSt9Urc4$+WbzD<8A~%JTy*T4*18~d^z(LoJ)0(a`L<fSp0bR$JNET01(+>nla9Dbkv}XTCX@t|f=ZYyEL}-j38os6`+Er*Q9&vvx%aIPRx-hifaj12^1b9SH80fu9tUj*7!_k$n;kSYFsuD^vqPx=#wP-rP(f!Jtwvp#xd}JttJ{c}@@c7Bly}%ILBt`iBSpA~R<9wQjaC~?%`gcU5o@9@H12IXsurQNtzkQQ3WvtcK*S~0t(m<js;wv0A_Eb(Cc5n}^@?s{he;}N<%1_dk~c1o!F^>mw9>f2eA7yZj@5YRfZM>lC)x_jmSjaQ)T5th`E5S$QuT}DVDvx!IM^ztA8Q{qXT2j}Ryi12L$11W<f?QjIXUhS3tU02o=cE3hDw*n)kzGi9p=bY&bg7GOf{eDJn&8ZY=~5<Y&3aQI#|qK2R;o3TZR5SWPE#<x`I|c&2GLdt%Ctp^YB0Hi2R0zuk~-!y|6<e{>!hv@VE4&dp<zVTzJbnV|e|A&sVzRGd#cWglqfrYhNxr9>I^k_B%Yg@#WVZq3g@8{eN!Pe((HOFBap!e`3nL(KAKE*KItN`2DShX}SD+sUI7Q?7TfXOaN5thYl2D<>Z#e?k5sc-_8-Ikchre-$#|ElISXx3`?Q9UcgEn)&1fQxrtmBh$dxR5=Xgx$5g_rWLmJJp;;BkXg5`wzeF?XMwxjqa@_(5x&m+_eaiW8?Km`=pS?XU)S+uaTU}^A?@;@)XxzLuxVO6-14MzKH2ET&J7fgaOl$HqUcxk9EWv{E*@opcE<EFsYr{u6fCb3Ruu^X397h!e$qJUauJUPCZdJw<-BDT_R;=o<f;VEBTLOHXlLyBrEErO26%EP6G1v=qZ09IYht5s3)_PvqGbEgsKwV8lM}tw!HMx9hMYs@aQI*kztvs)?y8RR^K29KLE4MGW174pUtEAMu<1SiaZCJ&xEE18pT`}}>hW#N3E05n6a%QdG(nH`&rJTh{z17k$p5snbXhEdOUzlRnshVqN7fX%*?D>eLfQ@VQN#WA{Z-2v4?1!aYoU?-a<}$BH6!4`2C%SS}wHqOEQ6N0F%E!K8alh$j(CK&^I^876j#r9JC(txk%ih`eU4o{^?|n%YhDQA{0dOxg33Pa!6<jIKNhRFqmV~%#-NRam7=}4<X?dBcRuRh8%EIbp7IwIjh0RB?t;L@+5&P|Lvj+~<Si$yQ)B|r`(g3$$4cSV!Y=8sUS$g0N9+4|;@a1r}HaM4=K3?mAb0ulmwd8C#Ylc7B3HM_se57@LXeYcTCT7_TpLN2yG_6G;VH{E@EjRn&^>RcX-Le_(D|v4{)em2$Z=YFQ_CI^m$$ZnveA5_w`}6Gzzo|IBUF0{Z%r~jbH>u1wMaMU(%r~jb?|M$*-qbQblUn9?ODa?Ep6O%)M0i6db1ZrbUPz-4aVKdi(ytBItR94q5{N-1ekj08FOUbzrh!EpXDXTij7`FZCb~$<sR?OTVWuQ0WJXwMJdP@wl2ln}T_*E;noBGSnJ)dzs+sf{{e=wUrLyIfcjFb=MsRt@y8YQ%xM$Ad>>o>U2K1dSQO7fiLckdmc6#@!SmjJYbK1FyI-Vb-3AfA+?@UFrat2knqFPyC$!9{ELMBq_%D+lZ(=Qb@FXc4nH}_0D^HL3UvB7-*uF$egRFgGA-Q`38`6R08p3vC5lmVR73okS_ZwPD_LE0yjD*bahmLDXxd0pZ%TnH^L^cy+auc>ifQE`0nSDz_=KBc|spVZzA=X)M6^7W(oFy+Y$5zfnZuS#g@fS2l#riXbhFX^vqcwXJ}tE5ET>@-c;=0czIncMnuozkJ)+$VH6=aQlR`n!5-rdCSy;iXEaf9lWivR~2O^yAMeTvh1|XQlB!R{dM93E&Ro_gCMu876MwtTw=turmK(S*G!qp@nWi^l0q&Wc{xqqzkY}<`;Lc`2(l}PQ&!OBHsiZpy&@kK%hyU)LkG=7A<{Q5fcO3#A?m<`(BdKq+M;3A66hzNK>QByUOpbATBl#8{@Y?)=6eb5*uGoi~&tjPx-|IS`h;f;l9~biFA_{n=ZXnBqFIdz=flumjnS2bQhv7fX=C#Nm8#9x)uiy)Eiq<l|KZdo!iem5B=sR70eRQnO51W+90<)>TtbrmZ(CImTFl+B9IH~MeC87W)}LT=gqQY1n+`lWDj<fM4dFV%%!v;^1w%d_OJJT1MyIZ5EYu#SK7Y|!7RY?pF-gJTL|2O&nHQQVDvD-AQZ1d_#=N&4+dA!Kt(8)uQr<4%?y?w3oL(i8<v03DN_o){=7iP|MbN=858EKg-#)E>wJV7Y3_?ku&gaP6Ht<>Mc*irwL&Te>5}2~7J?sMoOdZ?xOF8#9Zz<AM?4$|(IZ(i(l8K|8r&tJ!x9mRlG7Kx&i8b3r;vnAB?RAa0|F4(uqO`3D3W<dJUH|CUMH@?>Y`R&$d-oNfO=oirIFanj$M3l6Y@Z-`Ej$9%!kdHMd6<#>J3k6QGxTO>mwE!&r}=3ES`8Yei{^I61lZ3P;3FT-N>Iae?@+$^bzS)2mr)Es18q7C5}2j`-C{~ai%f@^$J4z!FNYIEwxp%6i+*I4F4%Wkj@>$zrO7lKG#o+ML+HRb4KCK!YKR&;%OerX-~R@-%?J?3(d=<CS>VwA)A(N%cl96X4-ARi5Cl|-B3$wUayw6@Cv6A(l;uV23XvCXQ%f0b<+OUcR?TB6_GUWK2Rdv75bi!&#0tNu$CvpG~*<fzK}|r0)rq9IFDz<N>6Z_<_dR@rx_%#WJ2lTRYK`?frib5(q+y(7fNr7P<s8GQ2Hwvd^bXc&#aaHe}8&y<FM2=-n4x2Rocd?309NBF)5+XC>%GEHzqOvwF<}nNrmHGfdt1V6plF`fo%4qys@N<b1*x20JP&X^2VIt!-VPe7LSN`e?{k545X%`ie=F`zSF~3bdDQPbYHA<yrO{pEqUV>%igCQ)FJ&N)qm)E%F4NSh#7h%R1Sjvs{>%>kmWz&O60M*e$WLDwE<j1_kaW_C%@Z!EGYTo8<1H;=R;0L!_g`?B6>;aB(LL#lLcar4`Fz~L~y9&Yi_MzkU~zHAfTRCa}QJm4BNZ>h*jQFpxB-y$`E!Bm3UJe&Y^#d-#>&csjl6-u;pg$V<laFs017<H5nRy{PBPIfK1>f`Q{1sN9|UU@`x0X<4R<Yah^qQ(Lh$tY`m#Y9<6?W=hn~pAmZg96n0X47duCRQc6<)Hyl6HRSEiIEg(IF1scZf=dySMQJ`+N`iLY#iVqjKoCa`%K;0%)hV|7wo=nZ*J&ohV=&dJ>8j3_OpTib4OTkTX&Irl*5MmtG;CCHoGR=^+sVrPQzHBx5yb#Us=RO(H3)ioBL)6z9b`r{FIb>T&{l|~W;g&E$f#S?3BHSW<1ygNEh4&Sgyss$U7t|}tfJ#{S8iq)D;ehKxE6pI5EAky?f{i4%wTWH9Hxhti5)n^gTae@;N$}Qq5R+R3xMkKQyqn47M3YJiX<tc`5&`i)X?N*oug0k*NNq89o!_Nh(4&hxqZ@UHiE*=9au%e+Tgz_5ZchG4zn|&>`Ci3M6=tji1$-N_zeL=@p0^fGY0*}In|FH}NcwJkUbl0Km)Ds!1p#uZ0w&EGJiDCo?D7MQ@H%|uQMyd`2vzdC$0qct>Q{`6qk2SPm;7CisUpUZpQ{|_wRz8f=rdfcW^t(kFO?rJRn6<PJG)3zNWqH~PWjJ-s3<X3-Zl9mQ34bN-f-{8o2R^Njz~hyQZQLKIbq#1iiqS#_?{Xkhdh^JY8vj<u0wW^7lg=bCao0w3?Z$B<fqW#SJj`b{%u$P1nCXPL-{=KL8p%2hcH=QAP=al1b<>l1IZ?;*3G8c;<AR-gRRTd=c(GRs!eJ}r58_jUcM9jvuDcPg4O{++`#3PWkJ{SpaY8{H5pP=Mr%0gniYAJYV~-;bex2^>@qLq0~ZI{Ft#3Pzk(z9E+wy`iX&~aht&!6rPScXyoI0`sTVX@@}?Uqm#C%e6(;9xpv2!&1#HVtg<U0`GB45feBE}YYyq<pKG}8R--Ah12N@0_EJWC0i;4^tnVdAdlC>JpgK41PQ~yd1moO3i6l&CXdfqt_gSeZ>V|)zzM|^*Np?^dq-S>Q}t_<kr@kD%$c{?@-bUQ$1W20zaOl$f_&2FJT;i?Za6_0++@@&u00+S#FI65o;O`D}HWooz(dmMwu1!r%8)f!%o{Q5m>PHNzke4u|oDAyL!EndkFBO_MXj`-0s>8LowQqH<m7jWcxA*m55HI?;+xR~>-cSIgHT!`^FR098@yMmi<pdZh}Ypl3u4R73{Uwn~Xv!tE!FyC{9Lb)Wg`IUg9&OZ;X+8?k1^O}(7#6VH&4&yScAq(X<A>8rm?x7-}s6|IdK@te6;N3?gCSivlB4;L*Qq}y;-5ti$7UVwD5Z~STya0Wzle5$>#5?~pMGGYqXHs@B@YW`X=Zw)`V<peK^<Tv5E}z+v50aHVD(NNXukQANT236H{0fkI?=V2HJs*Gu&kx5M?nW>+yWu6w|H_|*Er0T*LfMa&?;<wYmKj`EE<exr_`*Rw(EKcQsGYmo1~EwA$wLq~U-AyJg=BdmH_eB<*HloudgY~7lK<WWJS`C8+7k|-7zgJX(p}yRQ{4uCssO?23<|Iu+-Rt|75flcOi?VUk>S^@C2xF{=kET_L#3p~qu7-UC6cw8C-Hn|@0j?uN;LO&Iwvv*Jvh(UW)Fp3>>f2?7*OFcJ8?E1HlaJ160``rm^**zr30NQS9?#ZHI8OX%*W7ZO?<$WINht_z>(o4&dZ7LKD6b=w}RSu%nUh6$xlwS))*du&EDu^u_{Xni^LnL!oUFyvu{12J+RyS!TkZ%Us_w`CC?vP!-6!^6NQ0$0zVR`9`3P|!K_|!%=t0s*}iz>G}5!TiMgBY$K8?Z08|hw4K7;6;VU4ou@4eL%lql2cG8E~md7~ZyY_c@Nb;k#IUDi+M2=|st5#uwNg=z%5EBhho!i40EAC@V`Sl*_PzXiVNfo#p5N)|1PQxhLY?)1}QoqlkUTk2mMx(EqN?nh%^<r{^R_=<RmzD}RccNb+_)+F3i?4hQjQ@-FGfR(2h%cmjh!66)pHQxgQln>;2KB-LrEaHzpW}j_Q9Ub&4Rm0zs6nc}H9s9h{eQ_~zP0l|^>o-*V!r(I{z~f%H>c%HHpYB4qX&d#Zqr;-UPHtZ>b)Ylk}BtiYgLN20%tjwpUAyuAl*p+-AVq;bPypM!x%AyrbTDBkvKb-9F?HFw1|<5xTI``MeKo<t%lWG+--&mm^~uPS|Ht9iI$w@3gVZwL!+VB0|1KV(85>^N8Vtcb*Wvg!M&f9-}N)>SY!1F&b?{<6&N7v$StRo6|Fo6mH>xfJ+Z@{ZD#iEawwP2qG_4*)~rP#ZFb@Bd%6iWF!h=@!QPc7*if2a%{L^up7Mxb6D%Lk7uT9#1B4*Xn_xp}f;ICd7zzmJgMGyXH2^|^Set<!PS#ps?1P`;c|(jQf;4|D4Kdt&XV=(`3hcG~G;?w_HOFc^r;<g0N^8w@<7SIYqm}KEJWdDo%JNyT7&<o^8kkFOF-5bM;xT1BBhl{Meeq4WDb((<=lA8j=B7h#*+7e|*s6gh+HL3D?m6F~BHE6RU+<(<xV9%}oZV-n+pXh}uK+3rai-qB=&gCz`O;YH^Zwae;~o4MCnEd#9ci!qvy+?aPnb<545F4b=n2>)XV<*iZ=jC4_i|fx@vhW3InA|?KoM+d=$f;>4XZ$H@pJ`JYE2vpkWYLN)#*4WFv2n95KYLGd~IORx`TRFBrG|n$W8HXJ#u^4gYL{X70u}Tpv0BM06)Yk&o}jsi$AxQC~;n4+u|mZ<UpIy$3q}lcAEzDeG_9rUzYuRE82nkG4WG+*+6`0CFSFQrAn2EyxPMdvqogP;Y5?y<CVitsLSRdn1A*}8fmp>y`XuAy~lMln_JISFJIsmg;zKo*3J?(@#>R@8Ur8Qi1;&KOZddcQj<+&UL-C8<mY1zz{GUoI<-RIMDn(BIRU08s<F+?O?JsEU$bk|P)CL34ps&*(LoQNr~oYcF~}AVrD9c_*{7@w`6yMu=uDk5(5_Us#bXxev><BY7?^P87kk9p2u%|5$;g~p;;!-Edxh}yk(0%aG0h!<AvSg5U9^Uo#96RFa5a(ob6%0-)>aKRlQ1&}X+2XWrXEo4#_bJNEg|&UOC6tD9g?VaJWpJ+dr5Bd*_Hx%Js=dj_mzB*^OyDl*63gD9$WqHq<u`CU6iu*1;X*ymWD^OsjVz2@vObIDg_Xtp0}(+QJ3entSS8+m9$smx6D-8`PH>Ft~sZ*Vg8mZb_}TQ=_NDasB@OXxe?LL{8JWs%=VCM`x7NhzWlZPTn)eH1$xbW9NroH4P#=D18GkDGf<Qnp&?rV$C6KS<<zJROudJJNy85Hr&2h9xJmvL`kOUFn-<Mel(h2L+8{b-e2#0<6%2gc`!-ssBM0>PXxZ^_sblA)&?lV1?htj=HB$}As4xPLM5$vGcY*YtF;JrnQwVKC94L>U7n}x_N)|8zLT&Cs63#Y7n34CP-@76q-3>&J6-o%zcJUA;$||GY9-$lUi~7D4S&PWB^q2Dnfmm^G(oA)c3}0gi!tdxe7p=1IzVh-%xZAr?o6?vo*Kr${63k&H!Mwn2kbD!Kf^N*voZk>`1C5j=Zlf!>jqn_9<9=yyKY})nFP2^Y%wi~iy86qe-G=(=SB%6Sh?a0xu-%n{EhLg_)@)a-=&E-OKo$n|!18%w4RbhI&9*80A7aB<rJR*vQSCfV^36e8=8qq$tp<28qSG+!6BEsR;q^>2-06>%4E{zn=K~DoxO!K?s<Pa3-mME(dl9^HV3F1s6jD1?t@TtHf1}Wzt(-EzGr&lFCPha?=?Q_%$RQb(pd~}4>yRGA5R=|qK;^2EK?aBUfB7NuihHznpKq}1E!qsA@5wsc#*fmL816U4zwS(9Y4V_(chq|Wz)%FUh%EN(Ch;jn@>Ek~vB5qUB8ymEFGLmvYV}2AvDMOUfyp{7AMBklEkx$vi7oWBNoSD~M}CQ2Q89VtTFxnH#Rqs}=95RIn|}H9>g0h@F<tKWl0}x0anFY~d_r9IpZd1i<Fjs}+T+-gHOol{)iYwhCWWfSb<r44=Us7=Le0k$N=w}P32ZSiZHgQqOC8j7p@VA4q@++g(<8pBgSz9E4ULF!i|+Z^lRwU-P*=S3ODWX5Xr>~p1;Yyz%jj=>_zM37eWO+1>YCrVDtvSGX%_@9yJd5p<F-adEWWTdDA|^zOvw;ms4v*pvhl`h59jTL^z_VC!J$0aj#{Yz)Gr7cSpRFTmJtw5QJxxS?zHS~RO(o^ni{yUkE?g`S9GV{72WA#Z61omSrA`CQ9VBbD1D)9c#}R0EIVk0M`Y3!k8>%TC9si-HZ=zY;SsC!oHjL`l5!|oR&_1um=_cue^ScEzh>+C&oR|IRfhf0Aw01EfRY;)_U+h-Jq6ie<{?g-cl27-$Z-Xr<_SR?4yqElV__XOY@OyW>Wl${v@Z#-b`*aCqfM_2TCE1hdLcHZezL*ZcmSxyiV~qdEi2t6)?kx<&w<%%hezyz{u|sL!3jeQ&c>2rP(vo=Wn<tq;bYODgXz8;g=cxD9Xp=#-a*4>$5cB^J3(ruW=`cEOOt1KMDt8pWz9BK&uSS^82{r-^L7a1q4;ElsE&Wuv@=o^8p?}DJ+#I;l!=}qRTx6o2*_o|NU=%*-PEI5Sf$Ft3}q4kCu~=I3M%8yRcK{&^tovW3-a`jB6Y&Z(2SysOO`8Xapjxxn2OFYu%GBv2%!Cq^Ok<g5Q%F*A>bO}UMN(}1!32gbX})IYbN#5#}{qF7&kDD`m$wJeqR;qvRItY(v6*u)@bURhGJKyHU@vOBuMutjvJVfo3@F?2d*z?VH-^DW@R%V#chqWTthVrK0zj+Tb=0{%mjUl8x=0vAAc<lK*qZ{p+%j18|Yr51&D&OM>b&;cn#phY#E=IKojvoo+frjq@+7xi^(kNDyv%GbBeXM@=Ul7G&O<m4AO@?L!&4`bgXsfFFGYBxBy1?0Tb3hXj)M{(A4UWdkJw9zQAdPQqHE25E10#gDs89P+&vd4v$U}pC7So@GI)z%SIu(#{tj)n?CY>_J%@OOu4`MYPYR>&Q8i*_r+&RmAMtGGz<mIYHN+XjY=;`xQG=79D0t%qR7)G$U?$1Y*Za0o+Z*eh>I;zRC%|1-$f(M1>VUh4rs+=<CX3MYC-v6^5xsmcc$L(4ak3nlw8xubISy)VGqWqEq_rQ%yqCV;HZiq>&_=t%gIFgBYB_`YFn}H<Hom~5;ysNMHSA1Jmg0|K;9o#z4EKAqf2BfoD)kG&UYQ&XX-HuF<^d_JhelL!3V4ktN&WToRziT@g5#zP0ui{#@*YqkG%<T2&hpDDnwmc;2BDB8+Q!-R>8&|I0|@}sgzs;N+GJBM0h5<Xkxl8q2sJev0RKW4j8n2ZmntDyMi8yEzG%V)fQW3V69ccv2iF0D8b7M22T!4H=!1z5S_4yB+T`4Q50d!Gv<>JxGT1YmG*-*LX~iAW|(GkcEkomRHNr02^SUZy*S-+l+>NXxqBP_&IEJCwv<VqzT7j<_bT~SqKaxY;aIUPOR-Q>F-v?-g+mS|Ei>{<<3t*j#>pfonClx^$7b+mtjuD!$wmze^3*h_TT<`aZ>z%hBt<LV?aqAzMZWFF6!~WMYBy_pXNA4dSdBNQ4$27Fi=J`;e@4z4nc8a0__2=6o7$F)AS^P1Wu4DpV$an1Oy!tW5{dRN>U^vOu+BG23PywYi=?2x4yXUz6}~@+{zASLKguf<o1VLzhEmf(p{K}JdBLwiJAODZe9Q|7jM5k^<>%=Ex8;X$G-7170+=XAayeNDD-0a+U;!lE$hDCH+*iIhX43Zk#IfXdc@eI@RHHNBp+~ItU**m2v<Tp0oGRdm+4#y+RA2!Igc*3Zd5hIC!#>*Yk4M(tT$PvB;g|zTtdgyO_Z!Ups3x9pLvnOb2S7w}Fg=K)!=M8X$3OqvQ+<Kexm8qIt6oJsS(HrqR9A_lS*b0Ex_6i)7y`Es8<|B_Z5`^qny}jWEz!LTTpJyj)kLI>OxF$Bo`aZ<wU?1tkdT}cw9VASS!+7q(%AdG1#`YW<;0bQc+|#1-I{@>=bCryK^a=PsZ@e%+~oz%-!*`{C&JzL|L`|<Egd1ok<+H5?`UwF^=tyHUAlMcN>d!>@1`Z1XeL;J@MJ@Wj}2N_DAm@yNJ$|E&S29z&2PZAw%&h%DkP#MDT4Lv#}58jyY>$5D$?6(IJIpKNO}*POYV1ABAS2U+Z{~(Y$Vmn`V8+sA3%WvD2$iEaSRR901C?i6wU@v?IdwBjUg5SmcxjM`Ucl5uFM|--JLtkzNphNYt(qE^HuETgNYOB9&KBaP~2vZ=QUJI1^{@SF8twFU(wNFW<M)|yNN#Wk&kD`tJ_SfDE5RF)(Ia^nglehn4n;e%&sn?vOKIej%8Bd+_2tv%BI$6me&dh^3;3)xEFSGov*ieF(1aU^?4n_@1uj7@p#yY8^Fli#)*Wo|6SD|c~Me$hvP^rxuJNm4}8V;%krzMx1`4;grRjW6FI(uVgZl=`Gff(%Sj4e%yWK|XI=gt`H>oHe(E?CC&Y*~9H?;vTBaur&8GF3x8S#-?l^RySphr93Zkp?Tj*%R&MYtC7?Ob5Xq$SaBh07gTQTGk-^x1-`Cm>h0b~FZC4UMSQJU2Oi~^)>!)K(XV@C%K5-dY48yPr&4&8*BT+r{i@ObB*tn&;`f{SsG6vw>OGeiX|G<l9qA9es4<pGxy4RyO!36bd|Zo<x49ZNBjFA`O?Gsht;bS<+f2s6!VKITN#n8F@)?BoszkQq>piuoH}-Q)%GL~OkFf}>P&qLh1*S+;AR!OOj;k>O86HUiZiwO5Hz<rnu1ry%Si6XnS(yHqoXIALGHoW_HI>p`g@vl1S*xBNs%ArgEP&zar29jzlVv>y%cUFgOdls4mRFnE=Xs$w5h5*#Cfo5{UUBRrB2N4KKU=iYRJK;h6fB215lOXfY!BheX^DpR#^rXTm|$6uVZgm?_$NAr#SSh>P(Q(JcHtok(Hrx}}%rxT}*$A7jfJ_@2dN({yfMtx~^+MWe@cb6h$sxc<kGt7OR6}bH3_y1U)(bHMxeIy<-#toY~j|f)rl;jwtYnfQpNXDB2UTvL~Q5x`@BWsiNZVSYh=Qlg(eIY!Jn9lRRME>WFdoZ{en?kiW`Cd5)<?L8{^PH+0k{hD1U5uL=GSX{8y-_Id@*KhIZG9P<%E<$^!LkaB41~lCjGpr~wq`h;3BN=g8>GlJq30e&DtU6TsX@dHA1sj0it9Ks)D}g&?hy$H=HL73;1ExsgzyVb^0u#a3J**%FX9lhV<UyOD-FU8(ncqNn>br0n*~2Jhh2{4>2uC3%FXnD9KBDCGh2fq?;C>aID*)Hf`v{`OPw5$Y`wwk2Z@wMnxm_`MS==v{E5qzPQG(vkC2LGs~kJ|4bnwqcx&-3^6PuwjXeMSDbMv7HCZ4ngYv`!A(1{GhOC(K&H`~?m_9cD=u4?UKSm{|%Y**tnx;DD`*%_<g~LQ%ee~Wy)m4sh(<9n!8>;u<F}%Zt_iEq+4u^zxcaWwDM@GKnrwUN)%0FT~2V<vKU7EDIuN?K@?yDVmTHYTp`F=&*e*S%LrRdn;;xWZ|sCER*!x;#b34Rx1xM-!4e1!Mp2UC{`g}OigvLQHwH9Qfxtw`;><Z`P$D&xpe_=8XMY&aGocOJ5XifVYcW|onpSPdMJM4=g=p{-Jlu%;1Uw<vzeSvo};`_bUZpbRY{lA0tlOn5mcWPr{Uo;U{fx5ug$_76WP`~zr|h_@t`LtNDO+m-o6a#ab^-N2MM6uv(@-Rl{ndzEj>P8=WjTFN)9HVoc0WHI{x-B)Wo{En&~Tuvj~JG)U>fOl><R7ZG-O3}fpRvdHY(8rsjVhK(n-?d1D!N3Joq6J*P1rb09B27Ky9|dAv3!5)hH{wi%+l)nYMPTM;$FCrEXY0+aOEp183HVA*T5jrTMWetE^kFRj5Tk6lr8L|?;vK;H%2W7`AK9r1NDxbyeK4tNY2a$pns%&yH=NY-l{$`kifRs#rzKP|L1>koBif6l6wXrCLDrT%?cJlkqw*#f0Or*TTaZXp7?(!yrUTdErf0B<Mns4fK;klxVP3ixYJL%oW$nDmG){rdNZ>StiBg1ost;!Ks3v1$u>=B6H5^-^x(VQIWQs?7N)@P6>3p%)X146!`j4ggs0Lgi78My(ll*B+;Jb7iRalM|`l=LcJUzO!T7Z<y2X2&zW+)Z56z(fM$62d!)~&O#uV_%HR@M&sU<EV#S>BaK6+skZY)M(5G;Zt`zm)CcbO20}n4M3-WEh=1r|#qVe%vDRL_;!|oo0z$bvkbGN~_Rxl<2kwgq^Gl7X6k;c)D?=MrciBZ})E2jb)sir0l30H@mP5FTJZuL)j{@c7pR?%>2&JB31ojGLGY0*yq1)vtb@=KXYT*GE>{7$#;J8@0Jyuy9?E-uB=%BNdJviH}*(|OMQ#20#uxJA^|FrtH;R6gjkF0Dqd87zSta#zNFwCLbfgIENNL6G@TKVdLTc{CL;SJ(kn@PQrGQhkBI~esdW@5%daFGP#YQtQ!{hKxw)(~1JJ#zO;jLf(cu7QtFtMd4`@F6dk|yuV3*L9;F`!0qA;_ezN4<Nv&=94!mE1SpaR$A0pB6nZ=~1@QZ44(rbdE27$Mk@GYoaef<GF$Uy=~L8qqA)Kn&py+L==RPo-r+CEP0B5k*18sCW4^2Y>3w)1uG=&Z+bJ6_m=QV83FYXSV|;OZn%9SkbWdU$7M83YI$M(S#)(#*d9R+9dAS&X~l>(J9~&=e1h_CdQ<imp14Ehh~j~k&r~A<X$v<fUHpV;!c*mh5y-}kR7|gukD1jT#VY+G{aB`n`s%(@o+%^wHY3+HI)-I!vc%KV>65;I+W~0cjf(}o~pP0)(DBKfnyu-a1!7#6I&&FRZ)GLE4q<IFp9dZoymeZA;}x#*l-dJu1Fs`5u>1f$mg7kxhk?{Q`30sCVacW7gGySx1Q@#Vt*SB*j)1DHzLzs^-E<jUXx%Mi=3M-HRY)AY)j4!an0ED3e_sA>18<CTVS|U8=u?+HWhSIZ8x9S>QjQ@zP`%U?XPilhgWiS*RSX5g5!5vu=d9eQVM5W-Ji_4x`hkA(5%Ia{`ZF}HJEW)(L%-5^=_JJpA@f+e6~aNynby*{aSoQEx^LLer?D3j+|UPWlITLl>mY~ZO?>kNmafi<Wjv+LWeUp?o}1rRw}kNJ7gCUw(&^`+gK!Qo2Mjfc{yGnVcSx|c5_X_wtlI8?K!(PowIAF6y<&RZV+sLq55Y6Fftodc|3lCpY6X0k&9_QcYknj0zh&P^d=UG6Bd_vD1s9lym7<rlP$I0o1}<;u;JDKSVd$Z>V@bgCy6)tusfLih7bXR`7;ZdIn!?;Y}HF5=tSBqv^un6;T78MnE6hBG$GJr7EU>4k*^cVN~A?#Kbr&Y+MbnAv=xpck_0;$4$>E~9B@NaS}Z3BaYhe)$>APJKY(6Gr(=i|dBkCm!@Iesh9j#_*wyRHEBU(KU0ZV*P+phHV_XZ3RX2y8oRwD?t?q51lm!hn4b3JV`WaG7EwvQ^(5$dR)kX06910?+;IOt5CL%x{Q>v<{xl2u(&aUywOJRx+dLTy3LyXp9H{!5G6A7%TI%<2cmIsLhKk?^%TWdNCInhQpkQV{vm0iVxA}}}Jot0Nq2sDI8%{*dWUV)zTZ+uj^^eW)crSAiZW1%#9$JY7lO&`+e_;Af3UCqxDE)kDllXf&coNGaoWPz4SxMR>nvieL3u~u?nu~Ki^^awOkoMI*aM65)&5G|8A!cw5*r$EU&I|=h%uiGnuQXmM*v4mYKTxv_K#1hPE^&D&9JH-P0YacZ>Khl%rn;4s3V^ihCb2kz~(j#&07h|)%8p?B+q?@DC;z?Yw+R$xrIWVKGJBs7Wz>K#>B^7=(D$_J7n|b(dEnesy-5ie?j3s<;RqnMRiSS|l<d9^-Js*|sY*hADw8|GJ$Ce$lJkkHPS8EfX)yjD!@t?{#W28GO6tHFFyc}apMMjE?y?T+Q$*V4TpVSSvj=5EtEO4akFZzg-_r$zDm9xwZNnJOt5Qc-LJ6mbF+Q1n}0f5fv>t?(11nYV;vzflgdfb85k*GOW@{f^0)!0*ZlUavV#x7s4RqCYIqP2$OvN~6OT7Q=9dRLSYY~xgo&^#Bav#${0b-r6KLKov%>m$dh@oja&S!bNs1FM=UH;BIMyu6;r^3VOHZxTIE1q7hy^={rQk`dIZMayThXG3-+;j0kW2%~!D*1fo3LeF<zC@VDuYgk0GxY}q^Kn8)YQzxVIIbO-hU`I2^Xx)AcC<Jf_A%L4yzbW#1*J8fVS_;t$?<pEv>VJ6a%)2X2mLn`)PFhf4XX&!M8-!xE`fdL57Stg$E38q^0Xt5_F;XL%1xECdYsk<^6~sxYOC|qAZbb;PA~fuF!*Z|nC#<yWfBmDDl6O^if1dAB`JdmfMPx;>+ckqx69vXC0+v2!oQdKUzIv>t1~g*q4#H$yFBr)Wq%Dj7=*1~;TlQHVdnw3p)R;#Emj)J7MUkFrJxwJaMku!2Rn(Tt6D-73d%{gSe)f@!W<(!be56CyhSGgUa7w8UUFt6lWhhq2fRDju?;Nk!th~HuQo9;a#x-rmk}UxX!Te9}7WLP^tsnw%L|N$CV8gcr5yp&FS@|-8Xjtp(XUtg04_*r&l&SIdPPAC0A*98&S81`cr~!RW1P<*oaENDt11o;y<)I!p#twcKJ9Hl$J1|sb?BJrs4nCa44p`}~)%}{Au|v(+L9Ma)MClLSZd9LV;J`S7JlKJx$xk*6|MEAvrfjH!tZdSH77T#6rqp6v^#w*vNkxbT!%<8|9m@rUA_%g#bCT~)2qFOMWbcNPD77P<(cbBchvg=3;I;(NME;owa$tmOw!x8YQf~mR=q3tQTcmIteGQx_RUV}%=O)5XP<xUDseBxH3IpZH8Ov*2eZovnF)xe^fVn<OWRKs)=!x>d18qe*Y*x#qn2Ek|8QFk^2nL9cbTla>Ql*NHJnp81bu3hBMlNUlZ{|s-yQFVXWi+S%2maf8GPnTvj#%Z`M{4dD#I3e~$cQY%pa-4pj-0N@eda|JGY*Pd`L>|uZsH<DV1X~qR$FHkje*;s4V0?5l_Dr$Wh=(AeH>w81_1D*Qvmr|k;JML<ReoFcb$aYtn6L<>lowq6jL%YWoxp6)K`%~6HJBLG~>JqB?^u?qiKU+J#oYNnfFX3MW&*^rPLV*-+432aq3b~okhlf1)JuJp(%4Nr@<?$68zHY_g|_05Seuc;;|ncKoyTD3Q}@B_$_vY;N!&g0;`E_%sYmLOG7R@N`ptO0?asAIqQ#+g?__u?wNn=jzvL;BE00dbIyD~;E;E?*|RH1Y}KKX=XOXZ$U+ynZ4;njfg3f#rf6^z_>|8Bb;SIQM}7t6<*8cEuO2v#JKGyp>;cV5)G~Kc<2{vrQ<0$|PK{m1lawf|gxOUp5Sk=<7^T2f1SO)(^DqeOplIf4bXcMQ0PJZ-V`?jiNKzbW^PhWliSZ7Nperl+Mj7O+#5k(ba3xApebH2D&g+ZT4PVq3w*;3^Fpp7Pw2@~e#*U8}bT3(DtP6Gv0yKDH^SkFI#=vGoWRty`LifB#uA`*TN{O-8fHs9s77?K=)A8xdfkvNHR;(n;+0wp|O!9z!Gou*8ZV{Qd>g9>xgO+zl`2{&h^;2x;+hu(bf~f!MH;3&<IJHYvy;0o*5llX!x?xS$hmIASU2R}kbe39S`*FO6?MGS@*xQK+p^~_|p3PAL^{FNY20??^3%(Huwh)#9+?8AlcyC@{BapUC<7;RcV$kd3Z4!7ENohXdR`TB9N+Qr{jVTB!`yfdYVsG;obht$fkBBsKhBv}}Yf*mj5Cw7o;<ub?TMz;Ad4V0!Lg&+qVgNN^wAbD5<3mMAbhyjw*l)a|B=Szs^Rgnoi@Rvf1Qbx5K-U|V#|^IUp?w@B&cLZ%)K?-C*eNFKsj-lo^lq^?S&j(N@Ht8K0jc5?NkrN(&5${zd?8wPBN&h2?5Oeu;5DTI<5=rhV3X=tN+Ok_joFq~Krk;>!THq_r7@3N6Tmad)K2jGnOKC63k;QuQ<cUQU4=PN-y3bgNnn8}7U#W9=>&mKqL3j@H5Pq!C|2)_GDx&pDG+xSM$DCcmx;fb6sB6OV>#tqhSGk95n%7jy_iZ~l^`|2$P_HOcmWG$=NJXqE3Y{JyME~#(~bfr<vHyr(tYKw6t24~J)s@N;n`kjM*+Drvr~!!h+p?oGSBGzgk5+kwM*?Ny+Z9MG%0;}%1B9$T`l_#p6!QA7p0`aek{&OM^oGRl#QV4CZ9{|?~if#tlXm5enBF4g+wk&x0@M&JM;OxfuXt93xdo+vrvj`7QLV=ji9GMGrd4Fgj%z)=cdfrRHF!T=NeI=EbnIqh`i3CmEAzhJgo?M!4!|*fksdS>alJ>77tuXkW_7%Ls7X}_B?zHI9aU78eU<_XnL>qi+KiBFdE=v9GXqAoI|cg2$z|>BnyBencM?47V+6NTmZ;%L+riNqz5<~GJu>{`MnI%P@?HMd~#r!9{dR$E{0+txMPob4_^S-7aJIvz?C5J&p`rHT$N&NP{RBrIY@p-d_l7dQE~+??-mzcq6RrnVNDb#qQOGL5Wk|CQ>@LjgH1#?$V<d)=YE&$#`gKzttmAT<(q|cJx^-uWWJiRo?mei?2t|%n^ZNy7g^utzi2Caw1TKh3Iyzzv)AAL{IEaYuIIP?=i3#2yTX5W{P}h%-Y)Xz`O|+hfBFyjc=MWfn{VZ?Klaa06iB=c)NkoefBtUs&3#exc41%h+4$t2ulnr&e=e+dAN8mIhW>0`{3k*1MnKS?^P|$A<Gbz^e=dG^FZ#U{T<Jj@#`^26pX7S!v(1%v%Zpdvz5UZ){}~&(uok9ius<m!Y`^H;@%QrC(nSo*=6m^PtYsnknj)y<1{NNARK7YDS~k`aMs*YdK|uv!IpVm97_EP(*0q&EJV#w@*(wD4#R!UF_OG~<TEkF?sO3M?{)zUdzhAtoe&b92yxe~^z3Yu1GFq$(C*YPJk+sL{;BC*%@=GaXrb|?4=)6RCDq@<$#B}Lqm(jX%<134U1gy@Eyqt@jU^%49;u9x3@bMt2$yqHfX*As(0dviKB-%0C0k2{7O*!z&c=+QHidi~83x8!BH{Wdh>e(5AST`QV`AxAu-SQRvIlgGtzKib)Q%7hIMXP8?;YvPgRAn`FZ2gSEbO%ZUs?wjBk;+^8y|j-idu#Ud?9chn>c&T&e%HC`)-Putzp`g%M{84M(48&Yi(?HTuGtB?^OL>$UGBManQw6GfM0kuDnm2PcSSv<vs<$`uPdih&F|^_XEPo1{B>VOg$<kF#(zpAOS?~`f9w0{mGR&B*>Q|r-Qj$*@t4KH_?zc-?XA*{^sm1fm+!{K@r<vJzX)vg#DSfC(G;*v7s2fRY~`9?8Gr2p`ina<e{x3^4R`U1pFO;8t^-m2bZ1?SKY(^ybVJd<O<NaRb}xcjZ2YAGq#=P@7f%lcxIv%b0nLdcn+-6nso<l^g_B)GUb$TrwkOQuzZ>Wxq5~h$x?J)1#|Qr-X&yfSy71_#bTZ4duZht_+>~duJ+zJb8u~Ue6;BR)$J$lzC?-zP)o>SmJcLd3{vI>^=D`{vJ;R^XAyB-*`xE<?0R6b0YuD;t(|_>>XMi*0wdGHu<Fj?m4~ag>r}#t4J+RlaCv>h^RRioyW4#KiB>XpBfoN5!wvM!TDHuQurGP`R8V=_5g}x<$Y1Fd^uxw|K3Y27;d;iD*x}hmU=x|>Sd}TOPD}chl-1g`b6ZOO;K~`Z2w9?Yk5z9wRK)$YRWMG(Mj`iSLI{48ZK(HRzx8jU<oSPaGF-04D7o?*B%F&hxOGlxvAiO*fv-!Jrd{ApL;#Oo@3<+Jw6;<BkVK*|R)8Dr4?}qUDXM~p6_Z?AHTVhG-EB4^cHODV%1}QGGro28&DSE1o2rfP9WoZv#?gZw9?H@+)72zSxNb!^<Sal(yl}tY*6;rMRy1g}eaTu-qj)k-L3=3%qWZ%ws^+rE<N2zUJ1d?1+kcyzxs2@xQS9t=H!5mG@RsG=6Bv3Fn^!+`3+Cf_u2#(Zma)1We?pjxvJR#}I$3g=SOOG)*<~pb;w52yZFzRljkOLTKzLy~#uIHxmU(Pzjao!;gCf`US1S;Rj{<0wcYYo^>-!1;ruf~!{Bj*yj!2bO$EJ-tANv;A(%J9rLVhcG0dJ+mqViGc-R7W9{0iz`k8TPXnj9WJ7N7?^cW*KrLo3JE9@gWNrK4e<~Nu&)JCOC;%k!?6oW{8p<*@%KhxUTXY+PbSe76x#@TjEMCJ;_!}PqIiv$-NLIzw|1V$3T_GuI5y{o^0SH@i_F<t*~p4Nq)0gXzC5&s>CBJW#QcY4dBjbEX;<oi)oNDkv;82+|f5J6dZKD_r&gCaJ2S#J0c(hpo`LyrECk=6v+}fO<45zSV70U(%8{+;!VGeFyLrdsXznUBrA~<NrLRucZ6msbKWU;>S1fuN;jq`KK3)k$NgXZSnf+(v~ZrKKb4!4-vXv5VM;Wa>Xx}cUUNnVN5AAg(cMEhwKSM`)Pl$D5NC)Dg<NtdR4Bs4*Fx&BWD_r`P@JL%h>&;)ey)MG+zR^RX}gn8;Q$*8a8`&2$<sksBWOH{4K-Bz#uN@E#6>5qiQp<`R0n1hML7dFSIrDt6R9E^XEP_%XljF0e_no+`|n<@ulU4-ImmJDhQ%kf{5J*Y)wvlV>eAv<t2(XZr9nt~!t5C~R5fmtfOuj_rKX^&gPvq?pBjK^O{N6^Eo!tlcg^Ti&@b)|ci2-V)0s?W-d`7u2NeZ}9eqDHcnCF1_d<M9L!;HB9`vXeL5E`B){Kj@tU^6UR%_@_%1eQKv2gjIY@bNe_Zni=B>iwn<rm_w``idFsjze*{s8kQfc=knv=H7s6eqy1%~Fq}FXZP5G40VM74q`9I6!c1FraUq?a7S8z%u2PcrVj0KM-2HrM(t84g%!`O1MfuMVEhMXE;ivVA&j;f_d0dQQi)Zy3ky{XtDTvsdH0K7WV{uJAuLg9oik^ynHW`Gr1H{dhd-iFBw4nQnP}Y4_o&k6=J<Ao6XUL6Z3w4$igeu>U|Z8J(xFII=^MlYgik5BJYz<RDuLnGIV<MAXx;H{N&Gr;o=4vp5^_V+^?GX^3CbsOk=RF>aB5XUSj$?hEM?T@>8xhB_c`=+QU<jphWYP_}@>{gi}qmlV0SS9CUB;ti4H2S@7S;^ws1|t=?|3j(j$pEQLz_KRRptfEDkJZY=%QqSJ_JqP7Y@W4Ok6M4tNiyEuYG!^mr#sO_~kWj9)dK@eX$;XD8p4PpUkmk*k05j8<cY~UXh7FBl0wa<DY5=xhnJxlB6bXv3|S=Wr^61d{2q*$=6MtAvA?g(RH-xW1V*`%5XFdV3z8wKfA=&p6*d%rj0ri$KGW4iI9RJ=zlQ^~(^fk}nuEmgTK<3Nb%<;)Q*=9=^}%}ijis(LZqfO+gb;e7Ysf5@tOsW3e;jW1T!Q3c86C6&7DjV-LMJU21iSX<d{X?nAxQ59geyjrd-hJ!z+E-^ikE`KLOZBQp^mTZ}Hi|3;F@z#n~XG<;PpgPP@(>1+RWUea5I4;&?uhP$AzRoh(l`4DB4j;ntx+2k7?&!t*(#aN>xpQ%(a6AUgecLLw<G>8Ex(t&b3I5!_OeSabS=ZL^kK0(gbN+kZva3%+4(KgcpL}iFV(e3&yZUtb&y{IviQL&RagDQdHms>|l(3RQ8zz9&6<7T80b4eM%sBn=fsFgz%v`1iZ~4wo&NB6}`m-n_I@ji<?EBZ*XB{Q)yT=fYtg%Nfr8^8r5`1Yfn1AnN;?A<twhD5a#RzvDTXJ11mNLGs=VS8T&HrIMzo&UZ@6>_CfX5@5-{pN2{hmQ)$Vqqd_FxVaVjLj)0nyVWf9zg;Ca3_anMQxnz!a3#CKjB&SH=8LH|0sJ14>5-q^LxQ`-MA?^{r>Xc^~LOk({g(Sf%&dq&})Y=6UoUdpLSGkZ0G`rS%(%Uc{Q=@s{#u2;=ek_dF!{JK3w95R>&q2|WA-BgRMS@Sa}GjVE8Rh7%jb$afqV!8I1ofQHmSQomA+C!5@2qiJ~c{QVoaUFNwET)li9Rz>p{nE5;wdKPI&s&5ohB$uZR%DKtmnK^L7x4@62bc-vBT`S)vFF$Hl2FbWg;1os*zzQia)Ofwdu<--(V(MQO8mx@M>j5$b<jRQ5iB==^MJnhguyz39Kz>D?+^UvcEfbI)R;7*g*Kwv`U)PkUV4aU89~ZsZXrm40tj`>%Zk4>v4E_K642jSe5@9<t6hgH=ira~6Q#*SEe6hO;1U96R874PP@5?XIn~HWzdtADGy2&k*0W)1g3s={BM*ghfRwh0ZQOoi<oy&6r)+eW&!czgapcl9Ztei8cdRZRGCf>YW<pMND9oBzdNvOIq)$a0dqV%~1g>kNj<h>ikzn!1#dS<arFozsh45iInv^1Wku++^XBKxd0t-Nvc?KH<7mM`);05_usI$7y*<22GPtpjiSXRW53yXm8!@AKlPWai<yGqN5R-@710;==cKNe6*Br1I)U>(t39NFk+03*~p*p)FGCeiU?{$xyjjWL{B`Jz`ET8dT2qi5M&F{;=rG@mUX*ud2WbMt8!4gtFkl$sl?-Iduq3i<|T`7T9nRcbvSM4fj|nY&VSRCO@usB<BPZ@Y%yM9+%P@cHq^UP0NlAo;>rrdprrdf|_X#Ue*YWmCX=Px%)gYown)NHtU!<qlI>`T7*PFkzPcYqdgA%7J1g(yFrIt%P`D8cGj<IsG~m2v<%`u^kN$td_(uh>-4~j2jK#anSB3FpkC3Vn7I%fJKbGA(IaIRot<>NhkzSpHT{Zy+YU=EgSCUnks*+L<Z=MFPcZqNmPaOd?WvO41?gbU@2l=hyCIZcaL{u>*@5Ima%aQ;Y7yC&&fh;1dE`&0N4ZtF_xT^AulEwVulURO({%e;|3X=-QYq>^WOefgeWG5xo|^Zy+fYd&-`z0;i58R~o}kV!6N3(tRSZPVBTFdvuACx+_bl5baAUbbih)n%UM>0WS*O);N?Jcj3J#)VEY)!m+X?xDlk&+7g(!V+R-~&dahrG1Hr_BTecy1hZ0M!LzLh%4o<DINikvdNdfhhSz}9jZ(gwB}-{l9TTKwKTymMl}5*}Y%b5U3Yr&#~J)Vsjs!@C?QI5v6u%3q*k_e4;KeEoSDaa1{|YNDBqc-g7oT{I1)kX#PK?y0WiSoKRRFDo+%&!r`>W0~h9EsEQBN$Vq@OgWVO@=a~z19a`9gpnUAp(nnE^HhOKv5JIx|K1I3Yza9vP~+L^N{rN5kU$KSbI(J*EgQ6)Vl4BIvU7)m+9bBDU6o0rk&*~EYYNL5X=bTpQM^YCSs(WT+>MYx>Qx;PY)O%1^A7SzY81!4%;j<GYiXUZbb&&c^wW-3Wy1pxwPZ`{LS->F>(FTV)%QiM!UvfYH`N@07}7z%J2^P$)^(~#RwcWan`S=iU;DtQcnpa*oIwJWGw#fgX^Mx(V0aV6#mX~x?+R+7p#dH=O}#W{8&fJ|<d?7XiVGU$H_9oN*w}fhN_lcjsgUDA4M+G*A*yC2Q!tvd)5NDyR4jqN7W1bnch1T=R&_#7O7X<J%}PyI2|v-WNKt2gX`9O4=*}xyK;~wMfLXIQRAW&dbbTY|Z|K^2)8M5#K?y}0mcK$x5G0@A>986E*?~n@#WgsumJ0!=xyY{y|M54F<xu+crCH8SJ=*E6Zd%^<j*i1}Glf1Jvz%2WfiI3fUVwq?A>0PpAj`*;RJfDi7@I533VL~CNUPLLbZUr(^*#9fylEA^!=OCa@S?$3$)aiA3XGt9f0(u8gr=!VQh=395=8k5;spJq6&a-ZB<E1t2O&`%CIzq=CYg^YPOpkA5PK%x#K_`uwbBaH4GgY;kWG%;Tn2-b@xmxFDf}}}O_0{mHLlo6g_25O)W`)W=&15^`JYVolB(Um<4kg(tXd6+NezUKCX>641~Dx+-a0Ev_%iwA7r%(@+S(iWL0SP#<7kfOlEA1A)|Arwf<Q$_bWw0UCr!Y{B>W*=0*VGSCBsNE9i|ew+Hle|0SqizeC=uVkem`Snq7}Mid^jYdlXDKC=&PO`GJ0Gq(!3Ku%g~2j3thMaPO_O%Uq-}B{y#4Ckt7`9GXp{TkJ;%Y2GFXP*Gzvtv2qVY#hyVOE|5vNFq8JiyW3h+W|2YZ*+Tu$(os-77xq-iTN}GBr@2<q(X__+PGJ06r1DVlts_1sj!4$<J4H%Hohg#FH^Y*QNW$x&9&A(?q?Ytt+gnDXGwK{F@#TBQ^A8kRT0#U^h2OF7Oy%donq>1`MEQ@3+IbfRx>7tjiBLDoUDqd3?_@3kQqxpO~B6-fz;6G#*dg>kBR;2Og)u6W@+U3!7?<87LcD(*74t%yGomAy5S{%_M>a<^vjssvOU!MMXs(q*~c+m54Orw%d?0xgRuD#&JJMAy8U?TmtJXVO<L+~-#h)BdHBv|%IV{l-j_zvcqFCD;7sqx&-9MYZP#Xm5Is4`f@Jvx&rZZmqi*)oPXkh@rC)x9nHGXq%f`|X1zBl@vUh?dZ`d(@QP`57*d5l0JG6^~w`J7tPKG%cXl;$h_%KU@nT+Upj*!9ho1>Z&SQB%i*yq`9YfV~UNF1BP3LNibd=%(ViUk+)WLx7Su(u^e4Sf*OB44Yz;)<M}Fc5b+Vz+&=4T{r&`^23;wE37_M{SZi8YUR$e#fs6Mp34Z-u9U~GpyaPiRd*)c)P<nnq1v+{kk;V`o-$6a0>epg21>BNA&B`JM@y9M_z+NWp^Wg&z`4MJD7bO$M84~)`XTcH$)QkOEWlRPBiW2>xeZ>xbQ>=Hm$e3c#l&1c`##?ow=DX#k8JxQ7Vy6=h1Kg-ugA}kTcFbFOMrygFKRY$2hAnUGkE(S?5Jm#yFVg01n7O+M30{mO9IniKIxLqd+8IxsQr>L*bfidhLfv5Hfi5%v;%?<)KZv$x^Pfp1C_P1q<$lRR)48!bcSvkdba*S7ktnq5C_!#K5k|d3`~+F(E58U|C}5D0#PkWqo1AGJ)y~?ThLQj^4^J&1z<M&GECoR2h6Jn`(V|UkV@Bs|=`kPlX0fTn7JbCGY*DK$Os;pI0EN|5Kt1pds=F4H@$R-p>T0_&}^&?DNkCfX3#LqOs`AI5|e(`Ab#TGGp%Lw&H+t8z>E?CI1fXz>ei}PapzjhrS{Z(~L<`sP$|~apuBSrGDD6Qk`FHqtx3>^)Qs5zRYK9)<?8L<|v&U4>XYu+|??<TNyLp#U6s`3j)wc^l2rdiH7aOHBT00sDaNtn<UT$P4ro6oUjP_X0<u2Yv_+2f%cP>SlF^=A@5{qS@wKV|DTuEJ2l-r66u?48p_}BzJ6*BN}Pk5QtX_jp^mR$(K3haWy`f<6Sh*>8Qz+Kw1DpROq55`=9!rY68+2LJfDdYQ(<;pG!w=1nTQCAgmDo$gBVQWY#O5a`BO8I@KeH;aadt~B%5XX>@>u@f5S}Y*v+b&6b{Ar);3L0cHW#IJ7#e2O?q~kcLL{~Rc)bRc)^TwS6qo8aJMyjD1_C{rW?5|SLc96f#g5mj1%I2RsE3=-v$3YKCq7jORQ<#mT$#|Rm>D(XJDUULmXJkMzg2s91Y{Fj|F^mh+Foc>FtEjsU;ySST%HvK4QM4+o^wzOe(*%wgn{xdADQY%hL?4NHN3)wQe2_VYbnqO#CC<B3Y+kIm1!i4(h21*=-(Un$-6ENKfE1o{o*6vH(NWz^<{W#R*GY)j+saP}E~=BilwmcjCuXzVl%vs{$1qxN=q2e58mgQ}jlb+=0xDlIumcq^bKh(82@&AyJ1dnF!9FRP9r1YF;n$bT+mV=%t8D5iM<1*EUEn)XOSI|0lVyriNx@EP*STtan=s^l*d+sSo_|*R_NMz4?l>ZdXv$CUEL<j?=Nhc4~cEVHpw=Vo+5mRO#L@kXA6-x}Jc;!CT0qj3BL1j!T}3rXVl5oq-sO<@g#<{6sXPu#>b8aIsk4sh{S>gb4;28KNHm$r2_4-X}?64hNFOGQ56D##=V28=MDh&EpEU9>|ggBR#+P5NtYt<mDdA@tvN0nA%wfo`U=?{Xx`Oe^L$a_~l=e0?NF$>Z?`aWkzaP5g_5hp0>|<w%?gIX&%sMeU2CfPrgq;>;N~>$Xk|RtlZ&L5n42z;M}NsH5$kHu?JMs){&?*v^5ORAe6x!F8M~zQiE?+luO;<qM|n$eGWIe6@mp!0W_3KUm%K&f$+8iS{p6ICrL|bAh8hEzA3zTtX4bMk=b&<38Fkb{A1tg>$IINQZG}VJAgJ2^ziaDxID9K!{sAin^g`+zJLIB&gy~8xv!F48+y2Q)o}a5<P0zVf$#X}@#`xWrvIP|)6FhS`{aembM}FQCVpA{2d{Q9VbP@K#Duzk%g|F^CJ!jbOdSiYgKIBNPT$dVqNS<T78g#O&))PYa80qqz~2$|>9w=^wc9g50~{WUPTk2ym)OsM{)DFY;0ul`B3?^;dXgc6JP@p!76Bc|fjf&9tz;gGD0<COmQ30k^Y>G2Th86|(blTs3w$WVQiCi=NSahl9$JLfnk`o8D9Fl9NGI+JM^^{CXeKt}3TYmVCs({x0R5uh8|uAM@!)Fh={JzSxh|_ACDEyct4jR;^a{23d;#vlmW89R3Bx18hm8c|Y1D(mH*Ytr#K4B_yojr!Ur)8e;MJyStdBrGj9SQyjM;2iILkH3M8{`B@1CYMl`lwWhAOdlwp?%Aau0*>KY**&M&9?60i7z!rN-GaBxNm`$^cvwZ5uZ)mrhWqI2TaQ-x4I>J{4je8Jp8Kyh<sQJuC$8t@`Vynr^8O^Lp0q+;fjRFAk(5<Sfk$0OO=sPm|bC^o}rY;=(F0NS3-(%?(*&A}qa?#swMo<DHrc<WyKLqV-Lwg3Fe0Ji$=J@<|Bs6cEbO9yncyr2e^=;)foHZ_e@D2_b483H7GxOQXN@ik=D0y90tbDKC2vR*GP%s8Aa`G8Kb2MKh*3S$S{=P=vw||7iLXqWYi-u^}%!>La=*J2XoUM4@Bs-{AoGyrXQ)vIG_A4Or#B7WNcd(qL2%KN3#NPfiF2U+`-ldv-QLX(nCE&L|%eZGb999eIcU6drE{h(BS)<W%~Qo!QwKloKgT7&dX}SV&ZRc;}44P#|o(cYNB(uFA>9_CQ^QM9em(Wyb$GPdchw#KI~)v31pRYX1GfbP3S!JD4?4zEnS*cYcR!3D@?4jy(aL=`SQ`knnUR;$!d?M^b&6rt2-!e1L8?c7nPGWH6ut(d?;FAppaM*j*cx<rfZ+rsxXAzwshchY@LCU~PTL>kwqbs2y(A(DPY@mP#g5lg;&{kH0jd1#l+?A!b7`TUm^fAbbfq9<V{NCZ5yqie4b)#ub_ejZD0sI39t{ptLG2Opin|PB3HgiR_`mgv<_FE>qFqy^e{4;&yh(RgNv}%1*3dQa(I79me|LydOE%yOH?8<*sc<YoL<ufqa5YuWlEfa*nKzd;~{!gUuG1Ps?g$jwLq*@tr~dzpGV)_^gzVd_jKX{vy$b=K2e<D<obu8EnA{Rx2(P15nu2!N<Qh<;ACJ*=x;<FiabH)mC||wdf_K8lBg5$Ri>QwK@l0Q)?dPf6q9_a*%3_*AX0XgzOFyEjdRMD>5?I%)@M;9pul!X-mN#+uy<e-r}tr3)Mf;%XGlKW;w|F-_Hk;E?vUq<j|TXKD^ZUGoln8?DiJ3E8*u=Z6_ZOc~hI8k06{;!$CBV1P2~HgGhuxHLmoiiX!2qo+coq1mwtt(~u;Z<b&qiL5rlPF%&v@ctG<?u_1IVQ9!7r8JR<PhhKg=TA2VNn*I2ilw=tSZ^?TjG=Xqm3;R$ssjY$+-;+Gz3feKT)<IAwsyX0rVFTFlq*}^(Io^-&d%ull9@49>f#;Jf$2R;t=bvIZk9U73$#(g&&=(~%b^Ljz+Fw@YKq{YLGs0o-2k}u*!wz4c&+A9NT0;~B50>r`yJiyGqxGYQTFs$Iu0=UGcNJI6!10dq)B8Z-n-Jd{SkAABHf#c0MCREsK6(7cZ{zv<3s<<zU!pFz;4=RXJS*Q<1NdFoZJ8#JgPccXzrpoJdovhbG9jP<glR+ncoSS8q&czjHWdHOV&#@IoXCX8>w?iMjYf|Jc<9)@c4awBm8A6WS$8lUG&N>-g%FJ<$N|C8rbs=C!kiaS&k|C>am%Ly%SpIb2esIP7TX(frNJ2iiy1&GZX8PDlVd0?NNRa-IzAbnAr^zVS|9f!_KkQ<c|ixShWE*-%oyoy>x-wJgb350ss0`GbW%yin}5(D0k0javz*S_lFsDce~!ph2G?oh>fXbzqjl!vx*>p;4q?rBx+{l*t5;k@xa!{Px*}I&u(R1f2O|ly1@JohQ{G!&JRj)+L^@!$kdH7Os|EMXNqP?%lA7Fvn(yZCeaItXfO%m<$Rw`^o_xR$z+Pit4gou+(JywK)V!BmX8w4c7x#`Bc{Ydfyx&nNW~`_2Nb*-`Qp1)t)rZ&x!=K)1rCzWn?C0{oe*6u~Quq@VMs1z{!7KH7j(G+MY0IE#HKUT(Zqv)qi2>zx9Uj;md*diC6k$?=a3;GpODT!Dp%YpmR+dh1e_`FBTG%@E+?5|aogAvssW>&$cH4Kw*+~*Wc|WHCKE7@aPLMiO<I*~aw-itQ=ncEk-}^?^f~72a51BBl>{Ev)q<e!#9RB|5*IoUHTi_o^Rd~ls&42A9>q_P4P>E{6_2Ch^Dlo2cF+NlqoPqs5*y9=HZi(eWpCv_Nd}SvG=|`igI82Ptu4o@HvL5q`8%E5v(2HWpxzU#i4>n+_e2Tt)NvzX<l2|9TD50j+6y-FEa-0})>NslBonoE$CDy60#yWWeT#6~sd9OgHl_c6zQBL#1D92;G_8uhjvk-?oYQzE8<D2-h;3fpa@VWC4C*25f6yMa0Z|pJi(!dZ}kns(b?Id?sbDpc`A&%A080Caf8<vh~*JB+lzR<aSI@Vzdp;)KQvCfr12PWt*4so81Z@fOMVD9tBH^2RDIi_EAg5yA)oZz5iAQdu4^F@kqjWR(w*=@kcwPY84#bO4>PNG?-*X9JL2-{gEU(}>nx@}Tra7I5jQ0Ev|CC{ATghpkE!y0tU3Kw-gfL`8lJZt`+#Q*Y)P*36pwahFlIrW*!0n2F`^<s4jp-a4Rfk)OH%j?M`&I0TP;8%`Zj#e;(h4Kw57AqK1{mgdQ@-bzH85LPPHBN8>f(?;+(+d-rBU*@3>P<$KtJa7|Epbav<AEfJu>HJpL%;rJLiT1t_GXdw_UGFbe!IeNSNP3-?8E=`Z{B0y6&t6wKi`bU-i*iIjK}`YG9F8x)Oc*P3Jb5W3j6N5j^RXxmspOO07D#&SYSMM2m~+~5RHWyw4(*d^737f&Ka=;R7(R`W^O$d+-N)&3N*^k{(RQBs~Ww^qB)J}mC<-i0J6~EbQ)tl?7D&3m5t|~Uai?*neJ*ilKD0|_-9VRS6A)FC^txwpkv7=q3Ri~{X27XD-sElM;bP1&(C^cKUPG6&kxd12RZFfqQm7&sXM3|8Pz%ok2*6&a~Do&=ay-4VH-BP?B2QaBY*al#h-5O4Tj^iu8}uVnT=xf97eRPedN-0?9y^<?zgn?8(X?zo%xMjwbz;(alQK8RDIxX-Q?FbT8^FjjX7Icu9{AL@VPwu!O3i_zSzK*172R?@s}(6zdUUB<VoFd9ecUunC2G!B2vqE!1Hb9Lu-ES^B3KP+1UIT+>^#&H{SJ6c(B<#AD+2H({9_REX1xmjh($%&Ufh(=A}S*)m`k?EA#tOK)qFPm&%XlFP2w|?)JH_*#G`g*f#nbK!R*qN_6HI2ZBKYy9h+v<ySzgq~5qEZrPawh<$TC9tdIbXoC_*FF+ABpv;dl%DseBB~ZSEXItw<mM0E9!6HE+uzP_73px&WiHe*p-uVl#w>gHWyU);o{T1ynx&j(^1?oHjq;YEM>&-Uvu<V+vbUJ5Z3xVAf`?wBolD?3J5_+qKFelyzbTsM|#d5j87?|O`4cK25;Ix}*a)@n!3jmVb9D3~)E431<oa=lP<T(PH#mN#SJ^{i_;X{Jz)C%?I2WD!e{4O59FQ-;c2i?+kwtr{n(^}D=I#Nri6=~8q@{vJ!$nXC*A0nB4f1}m7#fjfEB4HPGLrL7|Wikda#p`0}`yv)sXgAGdEI@VOmhNuOpd&(hG^sN5h?mDxLCZ>t*@KL{^HuAwS&+yvOnpX<CJ=g7#7qM*BzKYmj7<da`2viULJMPys4wz-6ozvvFy1tiBy`1RWVQ4e>5I?E>N&+hnT+(Gx9j&SSAcm30`0oW6huxFJWrCP9;_u|)gG|H{vZv)QH(H9$iyIR!yyQzO^y|1NbZGQAz02UO3#-86Kj76aa1v}3<8tSX0+Zo8s^xW{vTXR0Bt$xMPxlY7j|nqe)XuoHZ&j<76r2=^V3X@X>o!fHjK!2ntBWm7-;#6c1Bz<zV(*)ItAO3IYlM{lzwQ6RADTNW;-dScxlH}(zxzV_E}_VM|=3Ccj#qD$;*Y)`K~_U-=@`2>n1CZ=^>{mOi~gYi^)(l2tos;h?@>W<^X5__+U01@wV%qr|MT*EdN%;muU8!AD9Za&pqTcUHGg|_%Gjt-s<r_N|-A@-WvM!3Vjz2`ye^kq?DTzK~tU$P0sy6LVZS7Hxr-<O=}E;BoaQkH6}^Ax5r!IhMsUR8;=#?vz7Eqqn_;}m4Z#%3FPp-O%Q?dox<Z5e!d%>!-*|CIhx_%BfA3@h*XW9kifU(Z%Ow+g~g)Ri5cOZ7blvAKd6;Qaq<O6ah**}a2xXG)f4)MYBU}n4%MV(8bS}eU_Jmn*kv~St#1-Eq`A&qpBB)e<j!q`%y7=2Lz)9A{`IuIm@^AHLk}?qHS`eQN^t}b&5Y;*6+R+4ha@WsIz&6FYJ@;X6{eiQn0x;$bSMyx<YYBAF=Tk#dRIvMWJ?)nNP>PsEj<q!!Z9DCqy(H+w>&8fMX;_3ru-xOh<qh`2B{Rd;jsxK6i5-}BXTdZfTqfm;5|k2i<Fl)d18Md;8FWSER>t`2}QFB5v-q3#-si}Kg9PoM{=WK&z7ULzBzK`ftxNpa9bO^FjzF}+jHOBMntM7t#AFA^{srDuesk2N#oqCFJs|wC5W6aeQ&+lV8&v4JKQ$C74EG;^k)Nb3Snh>TL_T-^NzPUe?&rk?5QQ{=XSS-kZz=6&yiaPLPq0Lj<=9j5#w=Ydb=0nIbspSrK@FnTO4mW*`3MIq$|F+ctE=g-`mgT<e0zouf8Jt$L+|8Z|s%*-#N8mSV*HxUx(Y}TXWA~zFsLQ_au`i=mCkbX@!Z%%zkoIh)ThyoOMe5IrsI<oCf6Dm1UWxv#TuMTQDXW!pPArGCwCr%{Zq1=jhszXP+UsB2KC&0t&c^Mb+ADB7*VhLk=L2RtNKo@S{#BS9%B!)5TaaYECaEanMPt?Wb)_*`4;FN-}f>%xI!5uYd+Ky=%&(Y&}e+-BH(d+JJyfdp9I0tBMC_b{3<bw=qcEu;`TRsdx&F!C!?|TH~4@QLOPnDrx!FX=s>?1IEaJ;0UfxkUy3N8G*Dl%5n)I6Q-wD=1^;BH`@eMBP~+Tg0`RVQ<8`fB9#2@&QhLy^B=iA)|8$fbX9)ZPqqgH+~0@%G~Jdq^2sDGg$uM5&(+~Uja=;>3`33)Qeuik+V~T*QzG=jb3bg}Vf~8sFVAqDb)5*O%`fgydonhAs!aSDiq(}7yX{{-RIAJ2vK#^#^`W0Oz-Lh#i-x+z>9krRk>yEtvzd<$nS$CNLNMU}+i%ga)lX}a=k3nnL|K>s;D5$gZp*1Y7@GM?xg;6WKZ$W{6_Y8MlH)bKzZUtFcmxz>2I*-RWXOBPy;Y$Tm!7NEt(H|OGNO(=bRTFcU?y16#6L-VXo}c#DD*o|O|(*5mLOB?MX<zS*Dd_9#`LNUhMYdW06FbHx00g!g%3ARzelVx@w3iGQx4Nxcx9@J<*KKNT9xWo6vCMkwK&nG`PgB#ZK&!n<7$<H+kW8oGm4hyMfL8?EgkoKZCMiKI;bpg%xTU5VZCT3>E?czM&n9R2DW?)f&%%@hkjt`&rSR+1i?FhXMwMMw$UBF2bKKrFTMJzkD3CPSAFTRimT3u=>_z-8&_R6^}OmSm{+J`$3~*^iwj>VWZVrG7akIr=Qj09ZFueTa*7qTqd|R6aLZLUGK{g}?#nBr#35CMBmL#|o=oXoxzc&IKm6?{$%kjrerT(uJ?F;4#WC6sCEB;?G`Y}CW*+e(;D_LEM6}#Y^J<~E<g+RBYMo|MmAXH9%yywzF$Kl^;bM-}^UyCW?l~Xw`t^Dq7($JPw$$Y}LtAau-H7(rrPk0Tr)O-Ob=@@UnkjtZUBw-%7Xg1aO~2S%OH;t4)F7JNoS$mh<{CIS6V*dVI$CqobZ5JW`MXm4n8*BeM8Un2{58u(I|>IWW!qfN&-2VR<TO`)jhd_dO#cCZg3l7|$3JRgIbVvOJZ=2RC`S`VkDL|bH^($y*=i}Wz_mVXR#mgI+%yO1GU*(m%^G>*p0h^p<tiQGhUMT=J&C+Fo56fz<^8$Y+GsVFQ#5g=yyw$$if%N?Q>!IEF%j%?38m5vw)Y3h48<*#a42H6?|sW~fF5xn%&QgNA6wj$6%4v~*Q47jJ5T;F2*SnLJAZD?2dk|VR;M3UfBpjkttc;SI$juwpLJATP3*XpGmI%Ng8Z3t1H6M;F>;!Lj~;$)VGz_XXCFv5q$VN(EFRarHupNG#m{`G^C_edO?b-FI*RQJI`ZHVV^fOMIm&QWW>yKQQR1!KKrl|UmI7F@-oS2}d2oSRdEHQcApdK?jt(F-^4UMI=o#d+=DPttQZkUNsV~=313&Ms=jr$ZayBLV$5i2BQXEkf%jSer*g%Yqy~|y-VkV;`6CR>}>r+qao+^v;8J)f)uba{7-um$~x+^of|CkxQ#mN0uW^}k8J~yMg0&YmJozZ7~jIfmOVO8cl*2WS#373b@9d2Wu`QN_X!8=dzt`1&CaW;6>^$RZxM<N<8=Y!WTDv!?$URHg+iExC%306F}O#g!iFQ%}XBe%VbMQqrPE=R>drFzlG4Wh3jKiJJEwrxUw_~jGBwl>YdK=G+)!xj;><7YqhnEm%Z+}{2$Er?Bz6{V)vag&0ebg1QYvMEMRRY$l_c!>j3v63oETp87fm8=HWshVb=E8276V$kH=adE_@vR*4clIVIxxxzl8GJqR{yJ4UW`9l$_VQZhK^n@g5a`aF~IjnKTBodab0a_0^`qa_6Z8Z)PO8WC$@i4WO;iFK$YN@+O8N6POlNI6^l(i)}O`m5cyJ@P(M}|bbY7}b-l=@P;Sh358N2-A=Jv;M7+!byYCcSvi#k3jl!PXoTgDbY&?%(*3JB;`OI))0s2->m)D9S}W|JyU<8LE3G5G~7kL<&`^rqR@iQgvEG8<h@2(?LC!^{|S{)VRY4d7yS<y$ib11%e}Ry$4#Dg--A<O4)H~)<o0Ek1#rVBjBEIWL_!M7zG6!T^d#eW)TV|OJb^#+8uezAy%9za9!&WIfan2YKc3~7yUQ{E{GMa)iI)yI36?tpk*j~d-QBm3SB3hPo5pN`N;dK9ux$rxr7>GzU)K(*-9FOp-{euzouK)NT>H5Z=?L>s7NdE;XU0NH#C}SBBfpGh}(FGR916w&HCxe%kVF+5iGqyZ3c5=jiI4%K2emYE26st867(zQXr9{S{_U9Ew#lNhW3md8y5StJ)cm7l2H&nEK=%J;tI9A{>hh5v8L8C!`M0bRGNk`x^ae6_wwG3@H@n#1@{Y%l%7(P^lh_tZBX<~X;crxJ%~m{R`d|GvK0ZTNtPf{s%v1H36*nxMaQt7VhmLtr|qhe;FQcFB0L-%^_MvkA=^;ZGC`EN2w|O(%U0Mivd@<VK%y%A!b`2M?x2#|#Lylzm(teCLFba<Eg{{9##<L3h@k^UFT{)ntmF_}X7IY@O1?Rcpa%@}P3<>ZAqIjkO38UnejJ@BSrOlNezQV-Bbn$1x4FlBct9lWcad|iE6oIAA&1WYKJ*&G{n~GnsZciN?W&ax4nIFcCWk*yumkc#vYpiQrK+*M`!5LZ*kf_QVv$1(i6wci_Fv|cU9*XVwxHMy1$2M5(EaA?fV63bqOIxN(8<=m!aQ-uo>5Um_UzUOk{O7r^_W9AKt_4pT7V{k54==aF=QcK!mb$=_`QI|P0^ml)XyZH{VtAgE>k(+NVTB^P@8k6%G%T>)*Gq2EH_T-;h2+5D82|5?ohTTfA$C7l+KIRujgm&Uo+`h%RiB*L~V&@cuX|Read>jbP6w?_C*%jP5RJ6JWw3QY|AD+V?Q^XGbrx)&(WO@D=nHx^Y1$U-Z=f9=l`D$Qwzsf8BX{%il>SwlAqXUpbvNbEbyT&7Lo4JwO%b{UrieW_JK($HAOEun*Hfid6v?e4?mUDncw(UlZb{%M7mwp%yZoaIEFCg5eTGMb7l<OM9cPSmNPC=VIrQ_g<N9>k+W3TmsBEfdRI1~^_l&(NLYkYiLgv1;{V6qoBYbM?dd_Qixm->k<HGXyE*sWcVAPltM}?Xo01AKxPO4BNH9QR;<CVHS$5I5Od(;H<PyjT8-c3IRWLBJ1+qP50Ac_Fd4!Nvl9BKL4-lxpW&jL843L2Jecx|Ilg&Q+oVw?p`^tHBwC~=Tk&zKAR`XlG-`CWP^t6v4$Y8#Yz`L0+<SIlJFKi;XgJ_utX=HanI6~b)XwCu}c#o`2Ir9TQh;SsEsP4Lb+cqI$-_ZtWKWV2Rt1o3O2~%LclG;z1Fq?9M^)gwRDF}45o$klp;QroigL~WHzRL!8+TAuN)PLz6_E*2i8tAebS7u3=g@;#F;{-Kcid7N?$nI9FakUi3z4B|Saeb}E;nbr{StqRam1^9UE@16ckeg&GkNorP)wofelEq(D<Nh>)tTJ={gq|y<$-gzZtqc&4r?<#6?E1>T{sER{Wk)z{DF?~^T>>Yw$7}r^#3Z5Y3J@elxM5o83rZ+~AT%5LnzQ6z`f|6TEG)bz+#70<H%|c$Oc|$%5}VD8iHW*=-oZh7?cF_h0Ydn0AnJ+41=5hJd%%Y+9OyV*#>pM`sYjeM(2p8Z5@Nar3t3=XP)0&|&fDzz);!kmG<Mi%pso@jn~5#_v%R&tLpZsUp5xzp|7o@@drP8Dz|cgz^V$%g+{DZ4zZU;-nx*;srIo)LCtOZ~YvpH5T&LMQpJp4)_7@ia{Mu<Y_G|N7qC_Y9?gS&TGId$}!yPx5S(B<<8p(C&Y0U5@*c6I!f;InD3;uQl=Vz3%Y~yo%wNEFj{mP&T$FBke@&B~!!~MI%Y0D}-d}KInd=;D)SlSrnS}^uU%4FlpIixSaX&Zj;5OKi8o_MHGiF6fCYn@TaLJGf|Kf_x<wQJ-}R^H6fPoTA(L2HSV6|8RJmj*fVy#TPyX8_x+wt;`}0Ji_6`~Ut4X3n|^t@*zH!aE+{5dr#~{L}Sc>OWlJQ|ihue`wA^zWgt|_21u;zi$3a>z0$bS$Z~eUGx1K5Kse7Kn><H%_Fr#`Qad=uLvZl(NzTcED__{@=O4RLJ`|4^}FOvaAD<%*F+6`NXqvE@fYX=uILq_`MKgs3H{vC^3_x`lyHa@XW4jjdZ$H2Bg4ybZ3CG>G0H)CaN&EJXo)LDUJ}WRveyD8b(NU<g*bEdG7A3SU{^B;uDYTPI#UzhgO@8@S){~)G){*|d<)-CvhRrU3_>0f>vRbIGctW(bX)%Ilr`sl@sfgR;%gD+^#_B@3X?ioyJPsODY{5aXn(APAmMHi1KETS*Cp)Y^)p4s3j99<)3={oF|Cv=_2^sKz$6$pqm7dNt_3^<>?Ll`<B^jn<~E?9O6(SQ<sozg3Aaq`I=q4wJ>bep`+kG_-@Zp#sB-yYA836C<HY!>OnOU%i`ok^jE7pYIc$hgNZ3u66An%Mq#F9%KaL7HX7e5%;-?;3`Cad@iGpQx{3d(T<ElJaOlCj(7u@go=10KLl+b^;L)#^;V7Z6G!?5*uqAT>{XlOsv|G@7D-YCmXfPFT8813ws^vQeU$1n#(OL#HO29>VpgVxA<fjqQ^PV*G@r)3@Hl*kFaJvv`YW=G^*5<E_fzLN&I0##X;4$m`uTK+sRp~o*OchHvOcdk`EBglcid=?$LITG)@fjL6?>PP0^vC19|0i938X^x`%AQI0BArrwHNZywgD}O3ZYXkZ6^2aD6c8^J+nH(VyP2rqB;}vH7<Rv2}c1?!5m1YKPPGj&VS}}<9X9;XM%lehCJh)km(NXM%jLnT>-G_<vFlon_=u&pJNB0#3($<h8jBsf#@qHk+zLj{h67!0Gy{}Qn3_Z=UU+#qfC*PU_hir7|?O`4Zz7o%9;6d>K{Y-`xY5cUlD?SM|C!rK2cXoFChL9q~DlKCbF(NDYnpw(Jzojt)x}>}@=Qm%K%asG(niP@p?#_Y@@5V;sekoA;A2l09GMJ9MGAonqaZRrJnj%h2LZh6*R;ij$dK@^Y8NXCpW|e&W=weZ$9af*QVP_&zD%nB3+H`!JsbA0-BmnV^ub_Yt>)S~*g;0r;6DXy-7V}UVU*+F4nh+-0Rrp!(V?ebpFCFp^e_A24Ul73Ri-F939Do&T&ce$oiho~p)hUhPZRo1D;srl)^7+@_-)!dPTwbSM>{t1{b9qeUEsbY7W=`N|*k0l@2*5eP>T!l<<~Nh*HxtclMu=Owh_x&-cX8jDecoErOFM0@y0Nyz=WL}wR@&l*o9D8kA23jc6dukQ4#&}WV4O^8km+E`q-5Xk09xAo9El<F4=$H*MCJ6LN3r2{@_+z=elVoi@68w<xCD{zOY<C&_eZj1C!jA_>VZQgIGwq?LX>NSt#<kQDVD7_0-Wa<S6uQyf!-iA`7Aku{2an3F=`SHgLIE@z|XK?UOM;Cg}d?uI=ABQ<$!N?e0>Pt?l2w5g^O0JTo#4vXafO9tnJ>@D~8({78&E}-poB{flm1)*6Kqgi9m&<jL6L-+n4|G4;237yR*Qjrmk0ZX9{*qW5)idwkV-SKw;Elnnyq<;m?fdXeX5PVk1RjsUUIE_S_n9O<#mU<7d59Ej*VDT8~=A?S(if`KdfR#X;usWQ;}4%)Cl!8^&c!)SOV!XkDa_M3ZfbBNvt&^XSc8q)QU-8v`OayUq=?-X0nG%aM^pue^P#ifVc@$aI9xnLW9koRMUv+Q6tb7V2~m7}=R~wG#?1>U1sRAcaLdRaBIe=7Ck>qSZn)pq)iefsdKQMizbj6fWJ@Ri=M2Tx!QkxT~sCuA+%8Z}bN?ZaS}f{(+<#eW180l4|rp<0eo$E$P|))S=RU?d@^Xr3D7v)?{4FT{Kp1(I92GezC4}J!C<wUL=N5>4SI1FoL(3F^pucB$APrL{E7uN_&mZydwfbbxFLnnQ<Z-CuB)u`@R_03Zn$tK=;9mt<~7E613=~TVHz?$ww<gcp#`jZf47xg~Tm_Rm;=8BiBDXJS+Q+oF|7PL}ZM7w8A4jt}c*|)cd+W@d2Bk?5=J*YxQ>4<iQwSVae!HV;c!HnJ&?lW<F`-^3}D0hk5Jb_kL<!R~q|4?fOVCA_{vPe+Ob|p4pabH?$&hq1@P6Lt^~ojoL4E|H4<K@AmAwan_dkq~o$Jn`K+ZSzD&Fwmgh&NtipDv$y=^ye$uJX-k%6Jw0hRYEDf`rA5PCa9y`-(SPcTZc#SpgO;iCJ+oHKu{q59;@EhAcCYq=Jz(>(+6DsLG3z5EJRuxnzai3)Xwcc<t;6<l)*kn@V;#n3D8n<{u}gIu<jlK2`eE;0e8*WgDlabEU_Kt%3|$?G)N-@Nn1<m=d*I_}5~3GMaIkC@B%qaOZn!j}WaFUn1#v31%^j(U+`FoI)~r8T3$+x3`4_*WL3eH55|MS@R81XgyNQW<I%DP2^+4h0*>vT*`AUG271ol6x(vuo5WNZ@ZX0OP!h_jLfQB?0>LVNSC=BV@GGN+m|J(=bd9W4jHU@~3kXadek=q&tgDYm@o2?(0-GQ@LZ(|U0iHP8)VTk1t5t;S8+GZVB)fSt(y*CvzNH?+nQLT)vn8ohIPsERJh<zDb?l3N(8lGou)_st$1=4eFFiN!l)DyhkEOCSlq5Dk<0mqi}jkwW-wuCW^W-F=<Lbr%qhC0`W`9P+{a;OHv=&1t^26&a@+7!Liz&5%Ow(NbyaP=r-wMmf+DsCL(s9`2{ZIN>GEO^QDE_(+9-RP|Cx133^(<o~$KtdkkKpSi%W9B;Xsr$d*0XE-);hnn(AL0ZdsxFq!nf7Z`mIg(~`bp*Nj{3tKlHBhl?fnRr;HV=k-1tFl@)f?oiiR37nUQ5VUn9lyXxh)A(ssn0K91kQ_}#>og4L`H;LTb?2?1KB15lnWb7-8YT{+2E!$aK?70INlIzN5sbTGf&GrrAHyJ%b|j6g^oN%frG*Bw4KFiD{Fru0>&WJd93V)%WuUyKV7qvZ&j$P_@DT}fJQr0cy<4%{*nNow4BozyhTkHqOq^)5=%&FtVQSyOWyLBH3JgsL#TyckxHXqhU@kZ2!?mN5$@6dEs^1yG^%{n{)y!c2{u$eA!t7BEZX1fgMDb^KBhbwqyfw1TzSku~vu_f?#nJ5=Vi3&of?fO1oMI$mLYyt%_BAFQ7a8%V+epm_wEUkXj;%nGTSGF1G~yC!)mBKfk6!2>pM3KH-$AR?d;f^RA92+al*@qC-jCb<vX64#Rq`UoO|@{Q%E9~z!*MO0Ba4-2|2#DsY^PJJEp3b53bPw{xndtLS`s9E!MkFs&rb%NfhOTxh&YVm&EVF%lTKIAvN({g0ljq~oXdFpijG6(j)MREc6TVAKy7&73zWs{eu0u2(Z_?f{JYp`9%KX~3MERK*VYyZ6$IgQsTt8>*X<~!@kK-AQ^_%K(J@`Tr>c`;uotTeD1m50eT9L2JPP76}XYNa7eI!!R$9l%GxmMp6^p#-KpTz3ipK_I6%76^ip2>mE5>c{b)D)0f??LC8*Y(5UXr4n&T$_{cA5Qh+I%238Kno5)v8R;&)VhVin!5fCJgckrGY&nZ1w;rrKAq0Z%4yD%n$a%Iz=2HU1d~6ycY8}d-|HaMX_sg>Qy|wDiv-8%%w?A(!{89eAHN^)r_pPOvo4@Y|2_9}8^-FBqo6GOb<@e_Ddvp2ypg*se`;KnDuQT^`)Xb^=zEJF$&T!r0*YHQx?su!xSJV+RV!5J@z;y`BA=8@##T-egOL+s5Q*q2{j1I5W@z+VyEBG<bffPktxZ%FaH`iZqw547w4;w_@nECQ%cjD&z@}Dlam)w81)n3&5;7|O6*`rQx#Id4s`Ci6PjfTF_SG&cQ7`yW4oseyisYx{LO;;>+seCgz0nZ(a$J^BFVP;@FnE{6@X26X*xw{w^7aYB}Sg2g&QJg-PWNZ;f|J{0#)1P)Dl~Zu}ryX|oXnb|P9G|rd_FU#YWNyzqd#rZOSy!yz;_VFeI&mZB94rS`-Yn({x?_kq=J-0Hm6Lg}TiUyh2CI{K>bZGvSlZt%?Q+A36>faVM)$-t_uMo1nt|>Mzbt;ndOMfQV#5{N;Q7s7yo>snuHM)9?#06vA5Sm7yEJA#Z9V_u^`AdVKWkV&yVTjc7u|w&k!nVJH@b_a!sq`k7~<AXxl3-r?nSrY6YF19f6k1A!)sdR!q4u#KINyLre?8=sgcjzB-lmwPCmh!?#``(!&`pN4qHI{{^r{YA*zzcH1v}}8zd=V^d3>(IFWU{L%n-oEu<XN0jq&x)~b;&n|u{!BI13mmDhsDYD?jRnG0K*0ZfCD>}f{D>d^=~$T0EqLY-CUfqi^O!6;wR&k{RHJrGy$;;R^#XD>U(*zI^&>-IuZ>lkW>Kls@0BWb(R36;qMR_qbk8E4jsDu<f1O*cAxTtapVCi3M_*nj1nwFDozOQE>medz@>MBLt^2-Ul|f2b0I{D|3{29<<JDIlUe4q*?>Og!F&Z8ENF=gp_Ey9>`PPEy|8r_t$@j!he&Bvr(P>tR{tj!qhe5u*3Bgr*mSDK(U9qep8}5lwh$nG`;R&mykp_yBr~!kR9?_ffFX=NL=ClnJe(ysFA%#=a{je<m0SlBL8^hZ-X;+W2qXhSvKGtw)9N#7!s2bcW4!zS%gs3}lTb`FSN9eazAIE&rPoCgNy`K=t4*hlZOcJPp9m*Mx)&)JQmn^a~vjC_SMILyHHsCahu|{JMquOV?m$vw<u@c|K|22vct=-Riqzw_@a@>UD$Ji9QeBcWa3fCc@?66);eCv9uN(7)9Y>AQ@>x_IV4QY$QP=Ql=SD${YslG&!O|_#9hf>A_-Z_#B)a`e0MDp}f?nk86v-Cxgl|&KB*2p4H_x3=~y{z$}6Il8Znky7Q}m!ST7&jo1gZkglkjnaYi{z(WQ_^w7;CN+oa{fSQXjv4wgLvanp$(V=i1UgT`x2ur(sJDCeY2g0bxDWD>db_ZMfCgGP)Idf&h8G(fGIUzltQ|kq@Rf3mY$Bn{wJl$N0C?N}?JkZpkfbH9mK3|0$^oc3K5;;S0Gh8N@pXW9+xhllz-S@?Fp;0NOo(AR%rTxFAxsL;(smLH%CX_ELxA24DHsB3o0O>(!mbv%lWLxf{49BB3DM(5%RopuokU@y8OxmA|XhZB{j_CEW<JnLwIaB-TbMu3izpjP_zxP9ovtNEKjc|yidx%4LI1qavEe!ku4&ksvCn}qwGQ&cwd2g~BlEp!%e=zo7nIa#fc2=BxA@+k4y|EX`Gb1eWS*Aw9Opr|2MT752KcP&cKL#NXj{@2b0Y+1>VkC1jYu)L>XP7{V01M&y4*fu1l#|WHfi%oaqF^$wMBzq!LnqY+CTsR?XHvRa2Kf8YcA@!yv<0htdiNU1rX^8n@3Ok@jHr}Ph)R@fx-QTd8*(VN%?v3Mma<`|-n}zeeXVYs=rYEu<Rl2I=9awMP**w%G^H7i<}FfT9W;jtsNpC|?o=f7l!}DI`pM0E63|;GATk?*y=J0JM!@TNwe848k_uD0B*Y}`CN@sal$lN@#MqCnM_pK>cbNoJdcp6gAp-!bsuxprT2(#Z&tE<vsr~v_XKgLrC+!ytYtq8n*s7X{7Cm25)5Rq<+Irf5xb>8v()U?XlRw4}wW@|otE#W7YSyaCEa`k<{qd!RHNUX1qGevOwsK+p`Ertr3#*5a<Ez%z@T!Hi#lm`JNsV9bdit+@IXjkyJC-t4$tO0=$S!5a66%hHTo!W?t(+<E>uf%n5T?3a3A61ASGvVsMLyBvUIiT}+eRgwZB$IlksFmVUux$wZdCHLQQ-nQdJe^DXM!y4j-bq%&A%)0(GaEhZR~dMcIB`C=KUR1&P`nBD{RX>(HxN){aRZ^%5%muP%0ML49>hQvgJ#`1&4rTHg|**A6Ez<L@FrG(5a*-ByJme(<Ceb$eNwPSeXrEMB2Kr0;ZZ~Cax4Yg!WW3Gl}Hv)|u*TStz|Z!6huFjS%RgkE_!fN;+?-U{!Bc#NxU~Ev%B+spjdeyr<E9B1>J-uRuGFb73ENe7LwV9sX0dz*^ZF-CWy`Zsq#*uhwpK|CX(2dwnaKuWUs#x1!DYRy2^w4H3|3^-Oj3Oz*WDmGjRRyBqbg=nIP#vwQ14w0Z3&^cT2R4kw$?$OX~AxMId>x$MrD%M`Si@NZi*?_RrTzJ0~)zB()B-*mq*<2XGzIwx{t^~sFj#F(OKV*3VZe8zEjW!Qi>>DOrghP{>xL-IZK1QPXvw$zuS>Ve<WBm-?plF!KPL93PlROVA2Odd=5((=}0;v-t|5qKlR(0M{;SZLow+Cf7b7Y}|*c%$-UIc8_>7u_V9!dIw`?4^B*%^kk|8!Bf?Rpkze0y<TVRYu1GB&$b(gwX*TCTvfVj7PY8Nn&ILD`9HYiP$Ults7O|${0%fQI#Z$=oRVYLSwKX_i)Tp5qiOiTsFF7(mJI=5X|#uMOCFhi4mI{<T3`~Nenbel<vWpDt+ouI@;g3Wq02<yE{pVt)k7s7gM{ojP@2reeNxb`!VynKfU!bTdIbUq)U^nkMQKl`Psttb{0Jm*>U>hJ%xDR^5i9``r)7ae|UAOKc};nMYD-;;-d?2iH{mh?Ga_B5>V1iK(d(Ftb`EiBnjcl1|iL23FyWpz{9=_8Ob%cQDjSUa^hP8TMVAEt<e<N7?6_;%jNoU0L3qi;H<J1w4>Ii@MoAWn`kRSqRaA|vZ~xy2dPFy7jOm<Pq|UT8V743z$)|<+5tC)#Bg9n8hZewoN+T{E7U?6xuY|2f{ie8TYVWJJtDQ7WF}SFYVd+YGsZSaKDw6eY!h#W#WX1~K!6s4vQ#lA*Y>(XhrVBKs^uJ1g3Z8H!%BF_`oiw+e}8}N`Ud5em$mEhUAt5H`Y@NT@1!~NdinZUQgrLhJPEn!w<y?mD4Zg}L{NeyNK;j?57!m!ZQJc(1#&S#ddIC?qFNMJU@0if73{IyQ=qnz6w?*$`fk*&_oe?rtLa3wzOAbDNvichInuX?)t@Ui?WD-|`xdJ&-E)0OtUi4#4X6M1i_9@pzU!1@2xHInTLBk6xv6fE$Zz761VcG3bfyU}pqG|OjHM~ZK*c5+lcYtafyS#01jkH6`643hwp?Mmnr}#BzTs4<PvVQ5%Kbd$;N~fZhAD?mDF<4KNpr7~`6H>kCTwk4hn8_Yy;{e_1AXsccAlv4Y(hyvMG1DvmB&}NSbxJT<&bozYpN<SqqIBejAKvSj3AS*fP&b6`959mfXw=ZuDA7yz~{1*6Wf~8z&25Zm4g=k0nL?J@{ZG@=GMx&PF0RIt!y@=Q><^K`+&(pEc~DZW5=Xrn{is}T&2gshEzJ2wSR4DpNcm3QA!jhGB)Kg^Rbb4NYI9y*SufObiuH#bRWDvyYaBp*LkhS-?)q|6O}F;yrr(<Ne>eFyj;dw0fSY2nvdIq{!RBwP=87#rv3&7735OChCeO0`ZT$NhHutBRk~Q|DUTQl9f3=o89>DJjF8s^Js+%kSYo(*)YQX4Zt9cpSs?xvzhvsrCY%j`;T1lPUNbmhn9F02>CWbP%_*H?ac|k2(tYzIp7|#t5m2)rAAMI>=L47pR5E#h=|f=OWJ}{02nB7*1W|Qlf=QRde;3!LcF?_;KyLQZp)JoAF;04e8S2P$b`KJxVMo)(`d$TUGhckJszq?SctUIJY1bv67XiV-ANDV*ybLug&V;a1y`zj)s<3XWODe2&OAMF@A;8`UqQAWl^|OIj#RP4XLnhTNJ>_vo<AAn>OuS{hQ@IFuw91K(7=IHNO%kQ|QqG^WRUxL3y&Xek5*XvfNtY!g;~&sr71P3=@ey2osGtC0Bww+ajLTIG<~V^nnAM9tE2u6$>vXvGYA8*=;)bFe-YWXeWLB#L15Baow~W`ObMgYDe;nfI+czGQCJMzkhWS}L!w{;TOk?sk3+;TT?0J~vTMT5nkbd#Lir*?<(@MgYR@gp1GaY2L5WVhsJGnZh#)Ynb)ex2)s~?44M{QeLevi^Gd@GLT+vAbr6CD2}n#Il_f(X$SRQEMhdx%x+KZLQLR7IkNX3s*fSHH*SXm>}UB{yjl*NZz$H&Webb!PK)b(8S##DlTp<u2CMx(9D0?*AWKaC>eSz9Js5FW@=+d)UBTkem&3$=Up}2kfgQXUSO7*2U;R?=CspRms_dEFW5_&O+Pf%yToe@2EQ4)Yzu+5>V4G!B3vCT>8g;RAJ+xpEfpQ4#uCvlEHAfF)coB3^Ws}{R&9b{+*iw%$KDAb8C~EjK-~nZ-3re_$CE&lY+TP!Q7-^Zc;EeDVUoS%oo;aZ)z}Kwi*o8A<kb+^_S+$mxY;Y!qneiR)cB$ly<x*2t$YkK!nUY#-Vqt(1H0Blhj~<^YUR#cb=-j1XB)??dhnaV$icu8s&l%jLCE?6;u{FEt3??)}&x2xsP-v?c(2A9A<iJ<>xvuOI?~OC-VCgf$1g@n8@rJ%WUr@0<)Tlz%)~{PZB7j4vc?q9T*H}Re8gnDbzuggKBO!-lIR0g{cO3*L7e7+;PkMG6k4P1m>dl%j_x7rEf0(^mc<Y{h6u&6HEcd<Tcc}!KJz2KW|bVRSiapC8s~VyCBUmlZ6?zU(TgVeEoBN*z13uin`1+VNSm2<WCn~QiJhJ?UYeM#K76<^Z<7vNb<_7onKx&6@)pz;P8S}&M14bl-wC#IX`|ObmL$8vkHbRgmJE^#EidO7K-Ukg<|G%G4p?ZsXG*EJ1<_Gb;6e($C*CNTpR{-)Tj@WOdrOn%Drra*UIUPN4`QXW*R$V19~?fJ7FpFf>)C6T9zBrG1I|k?RoOb{He`^aU`Kut+8z(oBMII;<ZS(|JqwcLwbpZB=E5Xg^Mc}ceO-Re#-T9>vqm}napGl)3lTTCK?h5!P12%e4N;B?>0%kpClVGV2FHth8h>@25?a-<Lh<#f#8539eMG`GF??o5RM=3K@Z1gS$84GJ_06KE^nLNnnUdXhAsh@J*q4?9<~Lp*YOFqn41i@N>pXapBvm=xnCLxsrb&rS^xt(7oOz`yN3VEQ?{xyker*+GU0LMh6Y}*-O<r6o!9oq-T{3aW0z+D<R0kb`yiKB>ahS?6Zhm`19TkYs&zRN88Cwz9}b2!Zb`>uiPC_^4Oh*>%Urx{JnH9(h=+RFVPk0GNHp<wh9+)Z+&>Xr<KtsR5FdT)pX1@qtqFQa)ue2T<^fcybf115n^1kq{^$p3s<pLKy53H?wo_W#<~@GV?UdP0WDvy?Xf<rAZq`(*VD@-G<FTC%Y^Uu;zEZLKt}}ENup5ex-!KpW?l0w>_8$M9Lt2-AF+mOolnwgO2p$Lz5RYfX3k^N0liW_RWDH-D0G|t%+FMm}0lP&F^av?B7Gy!t<68t0mhsW7?Rr*3&tNWCgQ)`Nwg9I*F{paN8E}V0Y7S^4DkpL;RbEU@ICwj`OfI?x-&<Z;dw7)O0l-at3o>G@Q*|9*3N{<p{tym&ktz)UClmceBqG>-u!129Ah+fs$ruW+H1gf%oZ85D2U9rrAdVpC7)<RkRull|;xZDOG6^;0H}bnMjV1c-w49t6uQmKh0GqhiunPoZLjFdovwQKzaAeDHoGd!nzi>B%kdS(d!jzFFQ*CuThk2s!5Dnr&r>hNk9Sg;uEK5Q;6W}=C2VEh54fmVZK7mP?V2bkW@~3_{a`xW|j>7AS?i(&_lR8BrtU&nf&<ySwLK=9^z71bz>HDz^yDgTmfsl-W(j7a~d;p{wZviDtu^?P(c*8lBqaCcB)joWK{iP>{S)25B9oSpV;Z0aPdnWW|e56x)>3B~azAlS+zYCkza$-Sn<p*}aXB;yCmCyUyC*twTw<m#CX|9}xJK}>iO8)NqKqN<V`V)vG4Al5^30Mqslq76dFstIWVwKqlt~V#(3d;~s5&%d7ba(2nbthpE@|Z>vaA%;MPS9M!J3s>NFq3f@8!i{(4G6T*?_0COLcga<7uZ#bj(YBC0G-^-fENyKF*K1P=m9*52|XEsx8Uz&Wo9~uHx)+dw}4UR2}ViO%jm3as%BLUAX)~l%vK#Ee>Azgx>_$U<VdTgGPyh;dEi@;nc7%&swSMcjDLJTL32&{O~Pj*F#O{nCw{vO-Qh==08KpS0brnPd<ID94C8v)CyecTBK7#>OTUXx*0TTr$MA;#l9Vj~plyX3LT>|;Vc<O0$dnRKpzQ6_0ZV4&gxpAGt(;-S*|^8l4SLfWr}DsqV;)WbVuNduNF;%kJxl~K2W((I2cs$=E3<L;bdt>Zx@&cL<;A$~fTxa}AUe*6e4VU}WV-}E021D!t667h8`_Kk_8tv*PEw?~(b*(Io&!l&nUK>)BuRctkSm)$(gb4yDOZJ@BG5ZMPvW;FEXHLJy#q9!XGpu^1<M!^exAST{%q`?VtPZUXBkCU-(&d1W&Qa`NT)!qG^TwvU}br${1FZH`h;FP$kgoKr1kWnu%`lmr6Yiz?W%0v@zKO`<(9c;_uW2_GEI-Zqrp)5z@HGD?C%j5?df(8!VnbuFgN~?OXD-oj{yAvv(m~wUM7EovnG2BGtO3igaQ2vtJV=w^_Zk8hb8nZo`jqFEy1^;{<(QT6B2M+zBKM13DcEbeEIVk-?cx`nUzGS^sBGcOnd<ADL!dBB2M;>KE(msA2BBSa)EbTFv+%A-C-OKUM%LgdZ36M`A8B*+<=;GVaf<kuD`?#ATzo(%x>=tO)dq-rsk6nCEtbT#=1i}tOOI=V53yeu;*&l@f&~GNWdv3u54S=Kx6@v0txw{^bB0;1_XJ>i-~R7AM_xSccdkEcP8i1NlS}!X&E?}N$#ffSa}?a+3BBtRZEu;^hW^Kb#E{i?TE=94)_LkUkk>t;yvLG_T`eFOniCgEZGNN;T{p-vxFj_fQTy%pZWR&H)?o>Ji`wKw|hXlmU!aR(l+;cCgDK9KbrP|f(lHr<wp$|812UTdg)2cqaH7QuE2T6q8GUo2R_W<FTb-x-FZMTI@GN&iJ3#)#MPPX>9%3UFJts@YEO4i_-y)Gh_+|;bcVqU0?1N=L+T%GkUekprUOthgI9q_2yn|#84{f<u|h+@VT$n6o?Pj2IR+QU%mvNpa3a?aww$w<Glic_{I^%ETdM=D66l;6;6c|Z69G0!=2w^dS+|OpE!4n*y^kcjF+>z{eIQ3<={}eKp*^TI=i~CMzQ!ScF@y^k;6@po?KrF9?75T+S)hL6x@5TJQpZK|Eh9mA#Mjak(4x2w&WuL0B6Bo1l_?CkwGpg5t;b2rwH*lFWsFX-G_o;S17fHvA|O*|M73%{O;y}QOsGI*pO(8b#(1tg+dc5`&O$prs-%5Mi2xfRy2*)cxand7eq}DfCe{)ySsg~27(>2_#^-jZoe>9Rv$~>7bg!xos8!m2aKC4&FbG^a$@!SRK#BdBJLQoG{ICd6G##Q&Ol)U#sC(gSSBwA~BWE>kp$d}-s5KGbHU1}lRx|OlK9VrZpEm`?F$kpeO4^+%DDKed19wt~y;BsNya;X7O5$d$%;<`XvcwrkQUx95pmhvAD{x&(M<__}6_#Gg)VD8FXiT<hG0>*6VhbvOhmH%u_@%3sIq%!$=MiM#PI52Y0S?||6@S!~`JC*K5Y`E@ilH^lMtOq&ER}v&sy+sh3pw#h2n8Q87=B_n-ya$8muG(;Rr*E0NWh2VPPw?1pj6uhXi6f{V>olz7(~ojNz}d8$rmC0kuq@%W#jw<Zjcj6(EHNnBafWFl;(d<&rgU%hd<<g_{I`G`=fk&u?qe88EbQ9qWk{ImHqd(p3v!!-mM?ez~57DgS;mRXg!zth`FO5lsm>+gke)!;KxjZ9}}oR3Z=@rSC-1PkB2Ap>=LB43=|(8IX49dn$i(*!x)RSzxdk4`<c54#Ympp3GVKif%IJNVH@gNa^GsEr&c}Nqbaec2i3H!BcQ81Tj3qVxtx)(*wJzskM^mo){K-8C~zxWj^BkptQRAv=p&ZuN9`gQk41}f8G3Qo_9@zjL7K;@23Bry<PmAdoH)%X^CG_2Ju_m#+6I|5rgKa97yg|uz=c+81!7xM{+e89Ct=O9*T1w@oV(C&n7c7`&?@+qDk)Mcy)sC1Qe+3`UTJ7zqu+>kTNnF`mA>Kb$rk&}2cAbGT1?{;fr9h5Z$0CQN`y=pA)=kFnCnR@0CQm`yPkQUBqo^U(%TfvbZg0jAv{ooT-=&+@zRwJvnAhi$v4(4B*&RSsf+!<U{z0yWIr^{yRP?{5r2EO<j>87cb69amScdWYg_v%&bfG=^9+uP-0dun!w8^jW?CWKO&Y~o^=y&ekjkl{08?#U&FP?L!+72nxl{|0vLm->Kr}LEydNPz%J*T34ay)|(6*<@u1Zmg38J~8(?}kV)U-z;F*RAcyeQKamVEfrTe)2>@RV<Lm*a!}EIufI9#x@9$PHVRKzgBtk5U8*CNdzk5$(vu=*7SaevBLP6fyA3$q3$|Vcd|l1XT?jPHA*_Us?!E3IkBaJK=RRZupp)qxf6%89rZ|;g66$=_b?jIBbyF*JTck$Ll*(12MdJC?vG1siCZfxucQ(gs1&LkPiWfVvYXfk)oCjG&k=^!_Jc8D8FoA9iEx4(YL@|owQ11AZaX4b93rgn3=e5pgK>vJUFl?nv&xh8XBy(4D;!Vj;w>M&#P~HT-g^vN3fOYd7vq|(*+|&NpxxV1MSg+j^|}V0|O^q%RC*&NBXLVuJb*`&ER8BLT(4CV0;U!6gaai&f$TcaWOr*7`DDG6%1N>psyH_lm+hjAKVyIH^$VBZF2kb*21?IzA>h5jHw%A>c*J5v3hQFsT*DD=A8YpxKiQ9m2yniz7tW(WLu_xuO&*+=!yW>QBsSw;lw&R&`z<fR@us_!74jW<fyPDM>P{Uib=PMJDAa>^m`O-V8+#9x^uEjUT~SRk!O^gv={H@oS90L3hzdX@*}$@Pj<`x)PkB%eC1B)QuVMIV@jVrBTbFck9N-FPN`F|(h`{0RSC{uONpAv;WB9|jyYRDwX=Ook7UpMmP5G8oAM{mLNtkVN;&gq>?unPCtoj~DeRT7c>Eeu;+?K`@`|3l_yU2-j;~~@`IDN+RA&y^7N^ah^^Bw!mR9JqpUW4$*=F07h&Lj5V6X{9NnwrL$P%HiWUA44dt_4iB>`jp%T;e?zwn&C=mRYqifc?Ef_+}{*uKm%>R#d|y~Xs}PaE4)T2Y+HLjJ9!ofrMK&*@LsuI<{zpL>>{9x!X1I*MmEa*f93mqfU0_vjbK)r+5U*Y4cR!Fujyecebq&S^iUS~prvi!9{RDX}Wd+Wdq><Y&&@{)##G%lCNk2L0HXUu>LLopw&03Kw{Z7rAQZ!!3jb3u{hVv&Ph@KWU#!UgqAv^x{H^@D--rXO7)}?fs;j<)q@jBT%X%>e}ZOp&TgBI$uS|8(uVlv3@NfQ_&ab)7Fxbg#|yuAW8Ev#5Y+fLyfB(L+QvhOUi*tdYOSu4u-TvQJ2DdBs{q_2|dIii50=SPZ4Y+vIQjImlcVWs~CtbQcW;~9ib(H@d5%inEM9=Ly6ju;Zs%o#s}%c4I+iuH=9c03c?JfDyJw;46)#FdrndK4on-Y0+zOZ*i#2Fc^Ml}51d_GdWkF@0+s~-x=`j-xItMIPsf!ZQV|`{C<1F~$@9CfddOB@o;~Ld4yJFB>{dzH8Q7lE$$p)U5E5nDd2S2V5hBpd;A8;k(1c(v**!N08*ydCUx6AB%^VEZnJ2w&*cr^t!8){eiZgStg<dz;`<9dIOsu<f@uuo^ca<*yUO+EdMv?;J%pwd(0@sbg%F=2DG8>?gU@l=5Nq{;y9Kk)GtZbxmEBWs5&`rh`K&v~0C!afmO<wT8A%?pK<=phK%em=Ky%w<ZB-=BeT4M2@MKlp22I%wQ(crbQTJ@>zBe2JW;FkUe(PY~c90VXCd}dc6xZOccStwL?(Yo`%cN>!KSo93fF??ddGi6hc!1a{4C3oR@ki`~y(4k_2aH@UEHj}di?Tn8F0MQ|Ai4_<KW~-N!vZPhZH^T3}e51fb?oht#p#6xQA2IfCmvP$@hUkAtNZpgz5|vTc0^tQ@*D9^Wl08;Bo$N&JUAp5qQM<za2Fnm?!|37xII*7Kiq<6|j=?Dff2Jo2258%ksP46#V+@i8Uk%i-o#3ycJ3%Ix2ZP^N+MyL_31hSj&Nat>O9}K<YnuX*-eQYqNV~Nl8BzMKk)!Lw8mg|ufRf4^`4Ot?@}{I`?j%g?%>9JL?=XTlK!f0uZ?L1?swo_BdD&HR+rV`}8<WoHgCduBmEpn3B`b_L4Nw>o?nMm6K+)|?Br{Q}MsCBD_5a?g<G1Sgt+IIg^VY(*7QVIctu%fsjo(V+x6=5nG=3|M-%8`ZpVD~v=_rklg>87ld_|Q+>ovcNm}v6vS|i^}nxSfldbwGPK%7Q1AtrgHn?v_GSDB<pE5`P^ylDI~D(EANZBaqr)OWLcp@RO_n!3AGM4t{`Q@G3;&7IuKNd^5v?L05)(2JtG8f{U2=JOR5GI|+5QF)Z!TK-h5G@kuAmC|Q=oN}n1D(HFo{j`*x?TL5^k&X?R7B{;98Pp3nsiUjiQZ<;opha4BJ?krWclP=V)%1l#=;f#8dlOr&GNmtd55IV^9_i~Bg(~^!?QDKjm%MO2aeT!_cK{y3kPs$7fe~(Y^0VUlNj3CBA^E(Zex>+LO_q1mCB0sdX1QTj)O?R(yf+onvFbUKuJnFcRyS3U>y`DFZ{aOB_}(8+Q~BJJ3-?lkU(?sTC|3Hy0cm;V%aZ&_QFi_i7q#0(8CY5N)0(=PeL7Ec*Az_0Uh1k<@VwORFAD3vqO86I6NHzZ{;O;1{#+FHZT0oHT)bkoW<E~C7^7a0HC4S~DGlo`71x&-g%fAMv)7k}_Otr>@3|KZEhnG%b;?q>gE|%}z`23e2n;QK-0gAkWLO)lPGG5^$_MG>at=(i2kcU%Y#VfnnlL^Lt<^L3v?c6xHpUm#c#svKREfC!#+b~_a>b2#rks=}(JqtzDmPAfE%IldLz4Ug!XK;31oCwy7#K`-14Vkmq&Oe5vZ5;)e`fwnRe`msOR>HvOYe`BB$oCu`OErP!)t!3IQkyfk0+~(f}|fzsxMN&(3yN<kbV;`+ep7K#q%mbNh?lfi&C>2uPr&neNp^geLMaB7_$WxV`m>B5<;Y627a6tW|wWg^(LhlqOWJ>WT-%udPo+2+F^;%0^AfS*7by)y+yS_%B8O<faQP1{Z$X)$)9sW0vo+6=iHNE{tUuxq;_)_wBQ+ljnz&kC~rYvWykd?AAtkt*tw|Lo1X7z`G}ezde&ok@fjCbeyleP<9ezXa6*5iViaXu!cf(z%Ii;1w!)e{@PT|=N+D15ps%>j@AB*NlapKS(Z%6Nvt8bL8Fj-BnxM%{Z|QZ*E`vT;PPi+*9s?$!WNqRcN1gKyBB0UYHYhii<5v&9t8TdhE}&%|K_`~=VqVAcOeKDRKmWFYG4|X!TxR?)@fhOz50Lx20LIv1ojc|C_mrv19)qgoh^028D!QiBFgjSXbM)k@OVY>F8kd?(k?5Ec62B?=pk$gT-OIh6QREpO<6By4fcm9q&!pHBIcNEtB*|E{8-l3$A(~cCsB(B!-g3dh_i}<gQ|SRjWF`JRA92=q$l{t&pE(XYQSG7F)oS%0^?7(`h~|!o;%^P?qof}O=rcDFRBo+AW`NCQXi$N=mz^$pkl6N+B{2OblY<gABaGOL@G`z)CKmNu?yq624u1q4A#B-eTFCn51i9U<PyGrEbZnG=P_8BIk8BBTW4tX!wj+>(^&yyMY6xlaitt{_B-Q9TZ+xT0g^SUi?S$DFzR-adr5KRyU7eF1x#qlGu=B@E(#}*tqA4#JR!Dy06f*D{QSshupS|KXt_e1e;H{0c#>{LxNKphM9CHWm_m1Df$~~@@`aCNcsdMrsDc`25GH~0@G*{qQ%s#T>sp2}=e~LiIXp6jmZ+kl+dNLXJ(!R27jhTPg3TWmZf6?ZG-9=~Jxvg%U1+M9|Vumj>=|ZvvvjBH|IggsHCQe(CSf<x91jDcZo3)dbz1L9ZEFe%3ca<C!47$zvxWo%9b&4HzJVxEh#&r6C!7>?YjMAYRnnRpzL|k<UMs^Mky221*F{JUe+-@Jr`L|e?0YGkpWLowRz!)uL`9R9iJuqkMRT+Ze5bWcT(~UqZnQGr_=Z||rqY}ajz|ZcWPI52H^1teSV~X42lj~!R+di2EZDqC`2yeUxb_>6w|8VQNk{pP{nG@S8p|?c{b?*|C-pk6c)yBRLy9j}XWOzBu2-!53A@J@EViS{z>j$YwGAcn2EBEoH3u%quxPktI{E016Rc=A%-B1Q3T2m_Y5n-BZ%4ge1QB+5<Dymk6$xQ|NxE$4A>+lgYL>VUyfHo~ZD>diO@L(g|?J3d4vn3?4ASiy%)LLf_7@$KSy>X9R2LxEDSphMQ5Q$fglsT1Nu8^G(mhp^=Xok+MQ%IdnVyS%cp2#P;l8cH{zHMDvdmClTfYbg5(+d3Ai_33YN8L3b<S44QUJC0(ziJkeI({ap6Yot%2SaNGOPMS;`cXrNdWD@?s8C8qia9+N)ln-)A(5P&l`zY=bU;Ee*w{Og7F#nIr?Sl`f<p}whHXwOfR@~*YSvgeSGhwf&!$xcJo>u2N(0aEY9_?(ef5D)3k|$MtLsV%J5|djRw0`PWB8t*2%IF=aT=~tVh;C{isGGC(GBwiGYLiih3a2#g-Dij^%V(hNnf@!Ctpfnr|L`|PE@eBj3EX4ovC2coEyrcHeXShh3iF-gqaruqiSJyriG2(5hSfhrI;#<gtN8O!j>AS0xv%k!tMw*ZZ4@{o9j5hfnKwQ9zMlzfp#^gaSMIpQvZ4qzwYKX<J|YqSHZ_r^|i5AqMT+l@#}T<X@4*y@ySknJ=%$zgpo;Lf6i<Bh_F}xpTBm==xVY-tHzF5-^7_*|2T*s^PHxYqSH#zV5Ml*V(D<1@TLuqb6~%~9W3|!36ljvr9&Aw^VNZyEKDM0kv4@b7BXZgFs=@u=Q(1P0RqL+&{CrdQ-QkA<h2#-p(i=ee@&ax4*6E#_YuHwGaMkp^r<Wa*g;g?z+RwScFQFrDw;tzP87FPzPD+owZqp;0e)$%?1D%)N=ZxmTLxRDvo(tSaBX5I5)<mQxI_uhg{s5oL{_jpxpYdCB=^`vzR?6K=|E=3LKr7dwv1gQvLCnsWtExB<~FVTy4~}P0ijd+GwyHr;TsOZcP+Qv&u(~zrCi)mj+i@bgt9v=C~(j?1Z=aPAF2MY(3d0O83$vKblQj>+z|L!UHE$WQ{up0V!NDEpeh}Xbv3y!^VpiZ+z!)q36h)AcsnNn*I;O8Y`k;JHrUqLkd3#OeBahQ9kjjAkL6S&Qkqva@X7R+zsxmHe^0UEEP*qob%9szO~aL4rZP9n?QI+vK6`GZX`AB&y3JJ-Km6P7cYO0hM8(5EQBokT5ekw;lFA+k0rr;GJJ7O&g9|nSWsNv+ry~7A`hS$63%M`jn_%pzN|CwR`z~tpfsX{i(t`+dhzstfM#3w~p&`9zp<emamMhz55O$=$gVm7qu8E%yiCg3iBjkXz*@lg`R}J_<St7L5XXZud;vT!1gI+lh)UCEj_DrCq8+p#492iz(ZLqKa9&nqUa<p5!9Va}tZ?*6v1z?q%JFJFd!jvP&`E>~~RRq!#1Jf}a`R=S=g#YCgxsmH?h#ll`-$DJj#%fLS{aY0f=c_jxFrR53?oQ&i6TQQp@oiiLa1=YF(&0RY3(`7fB!@>aNgL*6JeM!Ub6kckq-(}3%2`OKEQ-{R$1XM(HH`Cg%4-5X&jC;azH*xbCskdZ@1(bU7WO405}Wk#Jo57k&db@#k90~mi5`EvmH$sKw0FA_O`Zww-hrF(^jMx&8Xhs7mg&Pkx*tAptTA>uq5;`QR_GVQ)_pC7Z-rnR9ViUPJ%eOhoiH&fuC_wx_m33G_wlYV1{MC@84#dsw!iBs&E9e5<ks+k<LQv%LHXyc8jNzvwS@J}^8Am;nf07k_sKonQ+fUg9sl_b>C`nxaxbBF38MON*n&2mSOS2`Fd!QNTlDhXC8AlmPnj^3ClS~gWpMtYO#yelELgAFoLx(dZWP2afWR>2yDLP?Oq|C6mI}u?0`VBPX1Nuc*if+me>Sj`E8(t05~&4=59aFclcZA{Ba$slUn<MdK*O04RflmnkXeIaPrt1r)7oWuFB@-U-I^dCO}j>-qiJ2bgH=ZBwfl+XBW1f&R-dxR&Gg&q{^UEi(>1l<i|tgiN7htP)1$a=Qx19FY(1MTSDP|&iDKj?=33*m^Ts3SN{!cEYP@vPc$>1MFB-2aji(CP0gLTA%yy6Tjls0ALKAjs!ax28wh2+AqH9ctCH9r=mrMI)*Rb*0pwe52lo_8lTmH8Db@9@2)p?hOv60dmBc&YzG~ea=lUpv_<%aK7De|2+*B@+`2Hr!52srH-oUh^8m7Egzkp559DP85T^H6MW5cY$zMnewI8{lXzx3?)1BR0o@tTN1ioK<Oj7q&`$_aW(`BL%%1>_0n_d^-mDoq?((_e~M%X!*`4ooVf`Xo!#o)tj-DC)L~N(&Lq#;e%o-4EN}{Aks>bs<09UmgNMkd&))Q44rCqp5+hh`&tH-(1Pb4JRxZm!tX6I$X}FM1R|!ha0x6rvU{7+ETWc`7$7Xzy{Saj6T3I{-09B4CE5v-_&fSVNHf0%P1HE|N_e<2bdpH4rR7Jzh&vUOWfl>n`-~W>IVnBS0>Y|KwS<(DvdL2oN{)3BhE}S-R-)u^_mU*^nPr4b#+bj}`8FtrB-bWOUU+UlS18!Im7=^%D}?gdLG`I9$G&@}LPZWnd8(}zVTzLME=Ud@1EnUCosRrS_}GCGlI(x}wWddR5@?R?eVL-r3D%p^e<Kp&BNFitvjs<ScyP4@gv96l(NcEEVpWV?WvbJ|;{XD8`F)QXu5E2rk#(U5?J1+=$7yAPckl1CF{N2u#MX9IVxI(xeXJNhocYe|Omh9k6j(u~Q5%+lGWp&aYqeaPFhH_Ug82h)P}>8R1Iv8u`xX|QC}i;ICCXl`cjkTsw>f^}z%XjKXQ`ba!o?H#%kH;*^K)f=gm-2+a{EBn4G20X8~+j8BER!Z%LF?%%GeW^K?ybK4YM=>b*3!z*Bu&TrPf93G3&`>k9<loYiu}lBdiNyO-1`2CS#(!6S)gSoGXW}qyw~>Ms@&oio8dlSmv7N2{MY~kCe9d2YH7idikUTuC?EBm&v3JFf@HR?bf!Ni55yh^K_uU*_uXyCgRR(*kZ(}X8DOQ0?b@yvp&<1j9uc&0VM|9c!Q;l*}QF30#>^9sAa4W88j2@ljR$LaSUV4DliAhfBO5H)!U^dfH@kdBQib7-Efxby=-U$O1fJ=x1mKe?m0b{sVU3(hsybAen|gUOIjd;&`z*`El-%B0D}o|2Z5cA5CNw3j{~G0k)%_P%^|*e6-H(My7487tn>7~C~bL%4IjNY;X>6tm@CRdU_ik+wrjkgzK=nZ0*+tv2DQ;RHWJO3PYIe|34Brb#~r8K2-bp#a?7%djCWR1nY@o|w^+XP?|+cRKOvr7EdJ`U2xk4(OuphdrsSfoM>m)WhIN)`%f1%X+|`xe`ioBjeyVE>=WD(#_*=^(S;xs5%vtt6Qm8*ioLG8Sp#IV*N=#4*fubK26N$#$R{$8|i>tk#ulDGY-dna15GI*|b&aVFw1_?sAi@p{H7l<6t+yxu(-kwIp?1tnQxW!~_JWl|?U?M9WpXO}R^>#L(EB`mq+a<i0rE)gw)|syF+6f`!o7lVtCd2=LL8E#{U!}7dOnr@(rWd?BC_J+?LJ{QB=ReAp&rVN3xgvj4(=i>7?6Ss-|{#n-<gSSO0@)2?t6pT=Nsj0CA8jqv*1bCa~qaXxJI7mC{tQ|3&MM=Q}OwuW8Q_FeF<U?=Ie;v8bXf_JD<|V>m%GK9yp)M0v?+pX0+R+fC8JBW`p^(<25$}A!kG%-dAr#2zb;*VfBA~kkQ^l<>XqZZ=*fWhPp!ZakRI#3ShKH=3+F|t-#IEo(U6?vr3e-lclyX=1Hc2uXh`iy=?qxoWC6QHO?=?mAj%4Ymm=bKym(BV_s5|insHaC>6vkQenyrU{r4G1mlfkkk9$$6(ipe2-O{K#bq-4k)IQ21;!$QRMf&8eO94oEoTHeP>I}N1rFv)eXgR5ErA=tptWU=L*DmZVAf#sSFAgNhVjn*I8z`P!YmWm<|1S)MT1U(X<y#N@qc`n4j!q2Ne!v7gEPDL+Py4d-`dB^W9#Z(mZ<<OYAC5ShK3^WK?(YCM@z(H6OiCwWrUV6TDdB^dDhKUkwvgpjSs`Pk!7r`KE5B<H3K2D22asQTiV#oI|)g~DfPct-2z<PFZOW*R`McGyLp%u0|-Nwx1*>*z-4B(gTK_xyK$QvB#f4P?dCmipM#*Z>^+URT84b9R`9xMv)g|4H@pAx)upgUM;^u=4JJU@x0Mx;m=rly?Wr5(%=~I!j{KBW$~{)Vedo%a2#Elc<S_3HT5e)^lQ2FIs_x~9SSC(@$GV^ZD(dkf%!$k?9IZmE*u7&R9$Ta`jjAY`WTID<*&+d&8}ygbiaT%1Vi_gJXZ*6)>O8=iNb7a!u#p~vgS@f3azbPw_lZkk`MREuH`taP*ZinbZt3Q(-36fy5~`hCIezDDlg0JqEp5jw%~kGxkHor(NsVD{*)QZeDZ~lQ6AwPym}kF-;V+W~aheFyJi4WE7fn{3Mo#84B93cZ<80W+Wl$RgnnXl9rmZZ5?FhjXO?3)nTj|P%C{?`KATPU5WS)Df5PHi;8Kg<Vf*p4Ja%^s;Y*?nZof!=>Rq7~}R`#_}NW|*FI(Hu!vS~H1NG)vQR|-ifP$<AP!CL9W0<XOIr_43<#}t#4n|Qgc?U`#Ryq{s89$b1pkPAy-Vxn2-u!mz-_l#JkI|f*VCBNQ_AVM$AE*#2a_Z;pc;zbswh!+mXOzeoWyH}u=7`YHNDR4o#u{@wG_BG&CnC}oE0?wRh__9)L6U;&%S<W)F!rq)hJ9?v|e<!Mo9ntV>mQKsVD}M%NE6~LPJRPNIK>KwZ0GnQ7<p(bsO<0m?y?LqsmLVNB*#ED~@z0)J7E=Mh3s0PgSP%fFNV0)!zdS^wfP!)|QAGnv&GDH4u|c>>leF!lAt`b@NNXq@ixSi{L(y_hz=!sc8FjnHqfWktX4}9W^+2-7(7=Clq`{Up`b0W<gd||CuIA%H3T*lA0Qz&eS$?SrH-}FJf}rEHzYnt7+$*2sIr1%^Q^Eph_%RfPQl&m3s*kDoC6#BGOzBL^uaS%W)~Wj63N)`HH_{>%57#o0c-#$cxv}iNvt=K{ov8;eG7WC7{m<Sf0Q$P`e$0L|<#w3Zp@lmVJ6mp{ygx<*)iWJLz+d_Q!~y~OMCrYg^v)Jj7dr8IdZ!bz-J|?8rs$R4*>Ha1q#jqi=rN@;7@m_^osBA4+?6+O&9liEyW0_rKy*fCk|!(4GhnZQ?6B0cJyShOC~>b=W{80Z^|jPP%QNT}po8ORnz(mEP5y*s@`tDu0D<P)>~7j-f9%-eH{4&L)AHW+EyLY1aeX7@dkPgczIhV~q{ifVKzq>E7<pT&tOlkX6L)^)K@Wm+MAftsQ>z`v1`tX?`*sc|zO^S+FKiK~^ue(F1AwMwA`_u43Wi8yY(k#OWU)t&Sm`Z9Kj>Tt;>fV~z@;*14B{FXV{4@(av4Bdegy}QR-X}s=#ye*lfY;+=C|G;@`3y6=<VzFX%vm;P>lXiMkrFZ$=gbWA{;+hX1WdiW|JCfg^trCwk%`g$a5l#H5gf%F0v)UM=!v<aKJRt^D@OdNx!lP3rPy??g>m=afFKn+LhHW4o~U1siwv)rmYSwXE9+{0>Zm8jd4m;u44@VisY~pNd(P0C^O3k624i!4kRD<$aF-KQ*;w-(@xdo$oQap;7KUM3>i^VUzH3i1Bj#7rer5#Pr2P=9QpMr@OJM?U}40erc>U7<v<rSuagC606y&YcLYS~TXf@FtmNIOuX@C{V}dwXlEiM-%Ol)lzw*z%gJtxVU!t#iqbVE?)p%N&BG={GACR7BOy!!!`GY?|dls0M;gJV0lGu~ugJj&!^g~(4WWk2RZ%gCoG71K<WqM?x4t(*AA90>#FK<%R00{GYL8^R0W0S0iw24QG%M+r>R~|k5qMvZ^C*_yYq1frsmG(aA<o|kEUOJWSnX}JtxXr*00A>5~bhd1#=Mr~yX~lwl=8{QlxDb%&%H0!21XlWIrr63S*Qg$pr_yc0Kw7YDP1jzPe*1@V$j+~QD4S(OzMWh}2~$?4HzDP>V#cI}oOtQ<bU6(e@j<^cWL{<5>k501`V}o*raM2N@QcX-7pCq@%Xf^KMl}a9Cp<0%U7uRd$_p_tDkFo{9p6%JH*3R#tc%~tBX$kUL3sjOUI0TSY>!KXyA}>wq-GS)d{Z^50`bvN629fF-~Av7k8`Z!n7@y6x94U4{xw)fOxw24X)1=e>!irdde~UJXP*&08!_@ciytk)KNjyd6%%TCy-aZESOl6C?+=q?H`fT1UcDeJC%Jq9+B>30-r31H#NID)j}TpFzhIDRY9!GX`@k*YoajOsZ$u$2Z#aj#iHb|;BlCBj8>FDR{)*^FSmPK0;#jjC`8?avMl2OG803DD@Q6L@RM~9qUH(h&r}d9r^Sv~Ruuh}Nx2~J1{DXa0RsK^|`ENRwc7@8pWinmaQ#Xm(G_#2(pjhmuUfEaCSCF;~qU5)PH<q`WK~1ZK8v9E$6@KlPGaZb#0x=uA2Cw%*{bbSts(gP}r;^gs8am@J!5;<rX^FY=k_RVW9(WRx?#svaSntD{oS3*TJ7RP+psrYnZ@4pSIxeYr(x_B4j>Z5uk5P$$f!SkakrdOQiu!-|TEz(L7-Ea$QCX^e`F$YNq)dxtUGNR|FlC)xZR3zkF1z(Aw;{w%tqC?@j}}ef!RuZAjwmZ>)o0d5kYYbcFX(4ePdG5)t#d}bm4jrhsNS8pmSU17H;))6o~_}?96yC*36$~UHdK`juAaO+E2vak2LhcP&&DE2m7rK$A?Qlcva%-^Z$DY4Fzul_!addE7e}hyIKk!W$%Edsid~j7f$(8=0Vg^Z5@}#4#!PHjUIVatlP*Q5;tlm){QOGlIfXJOl*w|=_1!Y_FN8GgNHId=sF~r^#~oo)Ay-?N_Rqa4e!9aH)Xxmr`yOm2L>3MDZ!?sQNSU;;eJ-(IlOc+b#478U0`DEkuSgN>m>q8bK0so)r;j;8SvjQV68R!0AzO1&T&+-4rU1<yWuuEFqX8gf=yA-7Yd3w;&3Ij(?SgO3*+I7H)iZqnmxu=L{C1>0u?>=QdPnDUR1Cppm)kpz#B_#TF;ZPEp@z9HqtUhX<WXNu9|~Hi(~|<0>sU8?9OiT-;ZH1(<RzXs64|4wX+nCK9DfYT5(t+;_4vpTz@;@(%dvaHnAvC_+EG2MghE5SOJTEhB{Dc_YqAbMVnRa3EoJ<bIHugI=W_HN(1Ivj=i+DO_y@dL0<Z7+aJY|(<f2FhE`Ewk3{6}H#BgoRWcvFkY@<{#j>f6t%6ad7-NBT5EW0mkGeg`Q*xe087fWNCA|C4MoTAG@^oZ#yuXqI=(Nt9fto^rMT;DD&Zr7mW9m_@~#937ryO!JG#&45sLdL8xO*kr#enom?2@aXKv&66z4p!pHfx0BXBX&oli%Demv|CLsCX5xBRqZ^J@_250Qg{ae7zZ!<rwmKrzo%%X4Sf>s#t6G;<`r=|j1pF?MtWMFsO1tv($0;XP4rZhP^mbWr0%i{N0l5|j!CU1VGBxnK5%NxFc7KS+&D}3mc2myHTUmxSyNu|`(<5BqO>vp#wX*_q4oLOd=XV!M7d=Rv?UR9OQP41<!BNU9@xL_@nlr@553D$c4_gV6e#xO2gUkK24?p9wI#puL3I0iS|%I!B@nr{NGy=UCSsc~ore;Er=)s7Lo_z>7HdmO0Y}9oL3#J<gn`mcgfV<l^+z>txDVnM+LTvHKPHApdJg!dOp`;)=^*ojt<h@xV;T?ZO<4iTH|6-v-pjKhso<j0-+z5`qPRIx+%)EIf8JX7*21?IzBy66|DWMzL-AEn^uPUi^PsqSP~1EyK8goLeqRrY?o0KcsJ;_oWxU#eBERtBJ9$}LHK33sXowfwC#tedHK2%R1{C?K0mbM(kt7Y#5NS1YqECKfP85?LMRFjaqZ~$3U7$U)Gsg)eiJEBU3ZvaYFjdr0b4hYJhzlP8=amv%SWKMwJS=<wcpd=7h#iAM?aH6|HcSV5zj$T-XYiBrz;t=pjcx<ervy4!xJfKd6-RmX>vvIg>lbbetU;1=-%&AZYj6w|gkA7+`-r(GLzp{DoLFJBlY7Sa`e>3cnMjO|3bSh-@7g-X%zNSTl}k*Co)XB-_WYFefaB8p!jJ0s(~I6O93&?D2oq3u;|&_9(JwqYG*V8UZ@AP4POU{w9{T86vACWv)qZ@C<{k+eiA=beuK&y(;za4+pKIrb3x@KeOT$Iq1D~$iLA>OI;IA7gbg!_O2-giFLXCb;rS}PJYAy@^zt45bw4uIr@tD((r%SgJE}lP}w%+V&PfQ8o3(s->v#ZzX7r%@K0{+}pAWSd1Q@@BX`ag{S{M$|#!ens}ynF4Hj|YT{2ZTE0FMsf*<_eSVgmt{-2Vc6LaP@-6CyU!muHN{FanQhVC(UyHr&~7EIP=VZj|(S<m;bCk7qHC#;r-zimq9#HB<Z*^yjJW?&v^?Tp%j7V2p$Ark{g}0-Giw*cUxoTQ3+eB&Q;PGpcTR)B-$2*+YQn^4;9;|QWtq+Ea(#tfMo%Y3@>RY)HOL{gvzA@7L@Rvequ1NO31pDl%nx`75k9EN8NFgC+tuqmEv?5M>)kG18H1ZU>r@$4Jlft>4qd<Xtn^-SwkU8p7#P8HipuVDnvR{Vf6wGk${SVzl2GoH#v|t7xZ1wDNCxMvzY$ogq-`8)G15<hV{_WVSe;Fx$$%1V-AIR4?UL~Urlo3$m3j694Gj{dM5OHKJbO&I4h;Bk#>TR8HL97582o?l;2U=v(|yrCDHM|ijIdf(Q(1=p*uc6>2{$w4jBsHwY5wN#c^?XLb@l;q5S#ylFE2vD&u_k6dK1czQceXNDxT>;QcXx@1%D)<M2<U$5+$%L+=5#S~B^!oLM|EfW)S-nm-pll*@?+vLjv+@aZZBaK|y0Mhqa1kO-p1<Z~F{$mb7IhiXJeA`7L$08=IQN)~nUk%+GX0EQV)DogK>{0e#%Ox;18=8kfCs67*qkcIopmBULap27V#R5~Q%N-{ox`>khU$Jb<hV8roNk~}P5`o^>8=AT?&?6{`q45_a9k_Y7AJ-h8b(j!K?l_L4@oOgBYD=)ME29g5>!|*dpJlnqt<w<<vrb_*ArIKBPt&h2`j{w28b%|65*VzVQ%B%WxK)=UHym%yBE4JLmAwtPqk?X`1>b#S5C3T}w23Hp;SZ0?&UyB;`WRdxz(>8vSOt`xZ5dBn4H7=ba^Do%V^7bWdMr(nJtQB`08|X0G@sx*hSEC&%!BewL`eR1U%wPn88zdnMKXSAxygmjKBp1Y$5D^UXWWW+m19q@U*P1~?(DND{E9vHt$Pn^ovNGGv^TiIx<1!DdHC*^!<IRDB7Z=)UZ#g1m`$-}Lh}dqfk`av@AI2cA(NI1i^Z>a2We%p*ue_ShO77dZ0PLz176%huAxK8kGH}N!K2zdH6ge<}i2Y7gg0P86`h#qSq*Y;MklYnxv@S`hrK%8$#OLOq?nuphu`nn{=%KS=ikM{KG(fn9EirFFGV>kuX$MN70Hog%@7PLzBMhCx_m&IpF=D8*2MW&C<3=AE;Oo-Cb$3+9XA%S;_R<t(Hq7A|<50yihjKB0>C0*0^+^M-rq*rPx}l+vQC6q4m6R#Dc{6kMw3fEXNG3>u7_9Z^EHgHCnU0!8dk3{QnOB)k0As7C+Ui<x+3+B{r5>opBNsk2UUpqFe>5N;$>!@g;1Nvik(Apou71dzuQw9(qJS2NPc_dL{Uay$ZWWHfb)6J#5XEOPf?M;->VENqJSDIpW4a@;dn;9hir;I%bPRe#<=_?MqevF3>aQS(&mV~2kLsK7Kv4i1S7ckSA|uZ1&7xJ8yTWWtnHUNqlw+v=z!qi9^61+J+_?bqOU(C7C?;=PvwKdh-rwyj$)&W@pZ#jI6UFf6O*JgL@2)l#!XqFKJ2y4h4nSPQRSeO2VGVBt-hm;ujHPpFZ<FF%_q38JC+R@})hu4FB=wb5LE;+~l}$p4y)Xtdl){qpsB7MU&3;Tm<%Rpw1RJm9W^5!G7Q3Igzw<>pi3~_UMal+Twh{3d2N!KbE;Dns=0iux=ZZ4b#%T;!79JvX<0RjP6AuycZd<985M7<Che&{q4w(Xh?kkE$mL4Ky>H?jjJ#h~aIg9&r5iJ!~Z{;3RV+JnnT^y}Le43D`_<iOcq7H`yf++);dkE=>X><>%>fxMzxH0$Zic?kTBySKhA2q~2x|Z9&@>)^MO<4`G8Hhr?QZQ;KTfz`m&#+<I9Y<+VQRa!*zMJgx$lt`SrbMrMC||&9ahKe|nGc<G8Z#;F8N*XKByhY}oxy?S1Bb}335U+@z~qb4;CkG<o&+%-Q2Hqj{#FmVOIe~eWrbMNf<jWA<=Z!WT<f^n5V_h>Nt^+Gx!EC68JO4BaWG*}?-7~gdYf4mq+pvyI-3}sJDjxiA7AipcK~W*Mt-3FW#GS6I&i6Kw<-7OP_<alEjOi)O0p$@B1vzSf!Zo4=yX~q9Qo{Md2^r$;gLJ>_824~7Ub+RlwB%4<{T^>sPGU6o@5J6mk?(AkQGCD==dD@*=L*wPL_{yYA6rEXE4>VszM3ox$aLRXo6A^RiY~J<5B!0in>dC08%SEQD4kzpqe_w{J+^WxFrbxEi)nW6XRq^$CBJE=0hR55yLdgB&WSAJbHCjDkGO4&%C2;bqG}6C)c2}Ut~U+JRFmsJCjjXzGh~(gq3XE)|t0m;)F@&O~=Bq_H^2YbY!h%NyT~dUF)K0Oe+65?%>M7ds42ned|<SQy`aZ%SIzs(pLkx<XttHf`US-b18r3nW(T-HjtS>ucUaemv+mv3mZ(wMUqW{8Z<V$p5XlZy7|g7O9WZKw;bf!x55`S%`^#DPPRQ6iV@*!v&?6nXDp%_^OYCwA|_`(Yny4q$C_#X=a1qrGGpDo&S7N5%D~cIr0+*3R`*ti5&2W5xx<JmRo-YNEd%<Ed4(BQjA1A=<1FRS2kw|H$HE04e>UXIaR)+zB-yDZ&&j-dL&}<BWL-&3)pI>(2j`r`0YvhoHyKb2%63+F;ax~CPuEVtW5zOVpdK4F|AXm<qKoBV-eOiaZZN&>KstSk!w7N)Q-Cn0+dg)#?bl5psmkrE4jm5*fuu-DYg;y4dfH=WT5g50C@c`0W5k+CvEe}Brc9-z)|<XgI=a!tcU6UOF!Sz942{Tw<YeZIAc5gp$g@UsYpqJ@tDPLZ!Y*=IK1x=TQyb}$10VhmM5<j?huO@Y3wAD(M~R1Z;hS2Xs8rTLRUUOFg#*1YD8ZXjW}<w&1Pfc9e>6s4;bLM(Ps`^48HG*+*J_+iwz{Rs29w^4+GUq>;gD=P?P%Kn<VK+RvIsQc28O-ykZufvTMOUX;nu=Gtt^=uR^Es*A7p{Mb<`VI=Ejw|ab^CXb7jI;pDXi4{JcVu896cM6qyA-#xM9W<7Y4OW6V2T{~G<WbCuL0>`KgZSBUcJ$d(W3y*W!WP2go#p3Lul&T@#=iCi!kgQ-+Hf;o|SH~wxWVl$!!^NI8gKc~plq)RZ{Nm3lP;{o=mQ6qX{MO^<gBzM9xIVGKRc4oWm1?{F@r*K^CNYjl}p33|y&VKUDi7g=dODCk3qk)4D_bg-j#(8&6moXoD@7;`0;^OS$V`V7?OID4ye?ppx^3WKc#dwj)oivd<W6TJ0XqP0pp6Cp*c8%HNS#O&iqkD1Tlo>PQKgn>xoi_gR!Ob4-tUuVNX3tSCk``uN)U(-@=O;GB6x;d=(CS>8>3X`T?Ck8tFyZda=Dniw<Lt$243dd`GUvfmddEaKSaL)bf5sQz4QGF*#h))wRovNyEqF6>k6iL*Ms9@t{_gCV7v8#jF)v^0*}HXYPP`d+oj2oN<jtIOWyZJ0C+_@$G;_+^h~u9q6^&1PWX8B=_SxE<P6#*SIZwDISFb!;QuySNnTtL7G2^=zSu8KK$;8n~7uxFlmv};08OcW8&Cd|(m4{jHGFDJ+lku&Q?-G`LBXyzESB#8xiS;t^=Y)qosaX8E*Mb=yU`G@mHBWQWcmQ$$h#g20vUq!-En^bQIyU#?LW<S0C7(lcb1%TdT^Jx%PML5|ZjF-*fTtIvywVAxNa3-qN8ZT|0pFepIe6@)<gN4gII!x+`t42{-ZCB7u-uZu&tR|+Q?b*PKn%Jk`l8*0&*(skve$-+xQT=wXG(T32nfI{mh0T|Jdz-b10Z_RY8R$F(^f9sOK|<H>hzoMM?h*?h-Qa-C%1<vkRerGQFvb4i}=w+nu(aiYoZrb%Mw}S!W5Q5uVocjLGmA?aV;*uhLt*2H9;<xwlui|Bqv#&#S^qdhG`T72Wq>NjisxmT$)vBf)F#knDi}S6PyLFQ9{q`(p``vphQjy8S<6)M5@mKq3!bSCR!CdkP)(y0&S3pGj0L%`#v<p0>(Y?EV8`FM3a?^fkXGoL|-Gn>&R+5pBU_B`jK)b(j4Xd;{UXGdLK><S{=8W5kXpKED-rpyy)Z%B1mI!oHQDh1NSIHTf{p#EQ`~0WXK);sw)K~&Xk}>7D#`>0wJ2!SRj}D91T#>_}olFh_ZB(wN^7(HyfJ5zeWJM7OL-A*fy6dN`adP$wUF6`m>?j!2$sbh*5GQ3Wyh-4GkOUlmLd44~JlAit;sGuTu1k0y3*cn`-8=Aie*%1?j)1uA0A~u9}yo<K4Wgl2ZmPS-ODGsBMX$Xs%Ko<x`vIIEv(UA}kT?Qz?&g(Q^41fn)$F*vZaB$W=UanJ`tYa+@8}Xjt2XZQbpm!zP#%R<MuPiebJfr+qUdEzZl1*<R|H59Y~+O1a#Z)kjv<y~z`3te%)jrlOfIdI~=KU=Fz684anYNA7taY)<-M6Yk7lZEhL(k-Fi3bt}f-s>rtr-0ja>3*TD!AB{h6O>q;nyw&M%f8Of!w>tf;PJgS@+o{@j(X{lJUQG3u=BKD&zh74C<rk&A5xh62n!R)^k-np{OH^I6p{-wBlv=$NPUbcHFQi~UYEGUM?45USt=S`w`L1RAS>+oa?`sj!Pc`8AG4@s*3*n3U{k(WTm*~7+vseAthn;jjnnb}4y?C*5?_SWlY^sP!bmuamQ_Y^DF!QqgQk>K7eQLCN&9T}U>EgpMeO)p)S{MAO(B<rv)0<k}(bOLnHx*BmOY773r}r4nj+vM62|k!T*7M4JkULrx-JQzzVXEJsNnARAsb)Wy=?iaHwp<kKy?a^5^0jZ}mn!8iYiusm|1MYPgY)i0=kTPm>w<gd@BRJ1dsfJ=%@V?kb^4ceAWz@zUV8Up$2fV#gch5(9QLwW<Dvw9{rXSds=}3Fg0sBxuCKg1fkIw)J=YK|X9$=;wHtRL`+0(rIe#ViQ2=uk`MmziyjnlPo`gtS<k5e}{kCs@$f`^^e@8!0+D4_VH6yAE_bK1g((g?)Uo*~-O-QiRB0F1V-wmzlvM_Qxn15+f>f~9rH#ftik{_xFX`seivxjWkc(Iv&;w!4JWQtL!_-5KOJJ^QZ)wn<$=VLj^9aftzxCe5qJKBZE0i5T%5ygR)44;;h98s+cRMDpJW%$I!d@TDOR<J0FwRYi~d{Jd8kVylq!pikLYaJ$RYgfO;Vkq({8^$IGczaXkET8zcJrMgK#`K*c6wd2fd8&vOwL$D(19>hKhYpSg?so*Mum!|k&yD{=Y5FQ4gIOA1MbqClRbnDl2@@}k($~@SapffFdjbirll8NTcagSkGqS!QBDoC^LJHC<x<J+!fUb>!ViZ<bZrv$gUvg`quS9&-><}GJlzmnzsa!$<mC#g$jj6(X#@!b^Ij!Mby{eS`aDl;J%gdDnZ6l-pn@7XCs%VlL7s>sRD)RuhXk$O}`>DhlhQvDHdOAOWtNcbIN}qE5n>p9NGn;tH%hd~Bs;a<=@5?O_{zvYw_+cbX6J7+YgOh0<#>9k6>Jtn%89^cjg4~9SPbSa<w9bwqD=eZ$;yT8id#n6jnWQ-W%jt5$vn|cMj(&(`4B<~n;&N1(HVL#$TDI;A<=<XF6mFNG?6RfHJznQiU9%_+VJ=L*h+tWE23V!X;7-Zcd4*%8jET0sD19IJQ2Uk>Tf+_}Nka6p?7O5=pHl!{I<qwX;M`lK6*V+%M`pix(#Z|G3Y<*CxU-=Fc$kiq#-DB+zxNzXzM4?hayMRqkE)G1?i%zT@kNCH26NV|I)G~v_~`yI|4Qp*NNBPbWU#yO;-Hz)Q@kh*WjaSgp<TU1G#W2vxKEmus4J+h;Vkw*N6Vo~GqAKzy(&1ECRoEtG7)R5Nk2gVrgTXJckD|NlFam3?|DFHdtr_=J~V0}^QZYQV_ix1NI5a_v6$yCwXf=m6HGhbo1}3HT5hUprPLy@e0XUriy!X|+-?VCZ_t7A|1~!|(lIqsz5KX^Z=fz+bwl>m-Plhdi77@J4#SL$N2_98?d09eiB58rp&qF-D;%bpbE<C0Gt=byOHj68ynvY02-3QYvrl=o>ZplrM$+078-zRP7VOcC?K6F2wBF7C-11^LI^yh4dO$x*cs5SA)~Ge)lkI&txv%=Cb<0uMU~;UU7K||dtjZu<zd3xvD1xniK1Pumdve4c2O{sw)*gehQ2=jjJ>&qMIVpVi_ue1Z_NB?K5R;ZKDXv6QT=7yTxhA*L*rHEYW6D-*jz;K~VRhYdzuvkE6AGrXloV|6QA=t{%B-=9t5L{NqzY3sj=lni*yPn1Mj?l=M!xk65K*`QA_BB+)c~kz05_p|lZhI)vcd2Y4YFJF6?02;ES5gRGpXwDwe0F?25_U+O3Nl{&(UpXD(U7P{Bc#%f5!hNR#h4ZLz;8&CAJSkqhujEX}PO4$J@{$ntl_~FLdyjAK2os>c!HJR$P~LyM;(f*C0O$aA}G|Qx+JYixqp6aq!&{9L>$V0J=?yG+Wp0eO_x)P14`?4P3`1vG+NJ*|?ENMjwgc^OhDJegUsTPt9S#*dcg1gwIO{$74s#%L9Cg*GgYSq$a3c3F@gYY$Pao!H@=1t~SCtJldIkG^Mf@`0L2UBXgfSP{p_p@N&m|+MvBt<u66aw&B#VY@3F*{2t8qr7Y+z71INCY8}-!nKIpSL%?JOx|PURxERW2eY@^3%Me*bNd_adCvY_EJRIQ5FP~x=HvRZWS^tg$gWk(h7=n__K-N<^|1&YlnK@$$ft81wI+$CRv64PtK|*g({7ykvY>(Rb^GsP<RE}J;`#vMa8YKYdo}2XZ<s{jCO@#(+q&2gbZ7qeS1GQz#jr<_M-krn9>2Y+NqV6#hL7)CuJ#u7W4J+)VU>sL|<Y%#Wfju?4KUKDYnjU~n^`D#MlH^A<IQVrRVzm7k_uJ^3>z~jLT*^k}GLH*oBZyT!AZ*HfPKTq(*P-zu3o?ku%a$gtk75fzYt!HJhA?Hu)lqiZm~%@Ioeoj@MxSC3$6;_o(!_@cwRH=69VWU%nZlyN_Pd1nshpEZ;&7}wf8RL**13z}lOx{hDYv;A!go6LR(+gQFKMhD@u-2<WblSa=~(6ubjC8ES4Y=jdcZm~+@sf&Bljt;%8qRv^~?v18*YX-*yxfJX1c%N6_i(g`Bg-WG6g)lc;~A4CU_aKtiM~|WbJt|4-OmjRPG8!=9!aqStgV;-qWU>B!$HL>vb3>N<5)*OxaDZ_;IKV+X3<`FY7trtoMMTKYIl}G4C*d5ztVoc(0aw3@f#VN<I%bm1OgD28LtWfZ55nT%;0D9`q@yC2Fg#Ks8fSpPO-{&!MHojbc;tfcdv9kSUG*y({h+oF_4R=b032MC&esm(nZO=q~-4b;h>26t-Y8kE?^kcPB%aG({^|er1|L-h?7@h+-jU#~42eZrr&h1A^X3TadwDSN$}~<O%&^R8Xo}OH2H^Ak4_T<0M<5_NDQPM@qOcMG|{tGQzrSC#mXsu+VT+bhV$&4g(d9`9R~2jm<)>m!Ctdv`MZ4YmDQJESqJ!R3e0SxkN_G?~02W?bF0Xp(I)sZxg*Kyv&bz7k3^Nv3CpmlUVHu^cZnF%{=sUxJI)-!3I4@p_4qDI9l^~EQXEQpP15LV^30!Jd^#2o+O3CZAaJYEg7GnrmV+^D`-?05>bM3?6N+Kf}VFEL~RnXVAcBqW2R5G#IHtSKF%{q4-=jTbG6<n<s|ZWQod;eQRaN&cM&ZL1oV7QVPW}Nu$<dT7re1*+o7E5@BdUQH%8k;yhXOL8Iy<9=^Qr^6c)uR%%j^5;zXyhn?xFMq!b!sRcLHx3XNslHVw6zM{UMYn|UeE*qc1#TeTS{VaD|32{V2Ld{F-TkG8u_7_mzOuq$11&f1#yN{N8m6I^ylPI7s)>`BuGx3ykrinqC25VYDbZEf3;rUmuI%F&|eZNo00LU|t7CQc%~8`&_YRG8)(6=sj_rc|R`8<o?@%&FZmIZ`*T!S~#=c6HC{(Ot(<`$6;6fY|XK9;oIQf+ruAd)6l0ld)Kb0=i^7abnaN*+aj){)lnr|N4y<bEC!FC<V7aZ!LUl;TtXHMvJ*ASl*a1Hv-3v8FORC+?X-{XfR_&Udy{NWAY0xUVQhRnK3E9H#0^>h*$Ara9ATjOZp(g|E-}S4IsNns5UDn94s8?5-&qYBNMTl$pBVPOjkJ#@2O+?ew-M8QIYbL4U^tQ#Bx3Rpg%iUxbL{&zRb@*>OC50N@a>{tQW|BCBkwdy=p4JX{HG3-b1o-)T^ARKlKWQ2pRP%M`vX7Z#ioOW1LjPUNwaCcKz#Qu;is=<$~Q3E(lsKlq%!&fP6d`t2|@yy!gBbAJF+@jnh;hWJ&$e$F7}gPQD;G`I6e?IeDcLEMDfCyya*23bso9-iu5QdydOna1(zeyr5_Jg5u?CXebx?D6f~4oQp}GP<bv;YF;U;m|o&rOiw?a5h+r=yT;8l55q|Em>=x@=_?nBEbbjeAm^+j0yt+1la+pindChbCc|Zg$rpq-FQ55bTQV%QC6mcQ&c!DeLX_vEmUy-GuF6Y_e>uTK>(52D`(Jgx<(usD4_HCTgx~IbIs&A_U<!2?E5oeN+Up@TgDDK=M1(hE`6P$gM@>}tu|l}wn$E#zmgBE`wyo-lMvVE6M-tnAEU!GGD6*qGqw3;e4-2bAJLF6g_4EW_1NF^9fOnUHnQ+1f(NF-f{=|IOF>?%M;l2mFVWn4AiR2qq+{34yPFHsny5nM#>B?OGx0XI1ZKqLO&2AL{Y)N-2>UaXMfd*)k>js<rT9$N(9N^t`s5Umb_<tVOnbGH;xZw@w+Hav<?H}AMfvX>$fh8&b`kmkQsBH~f2wtK+hLi_UYy6!DAi8`IcE8XT6fE046Vs(h+;7X<DC^_1YpU#ZIMo}LK$|E0%nhsB<#lSpZ3z{5Uc38&??TIQ1g-j>RaW}Vhl8itX*uQ*Zr2SN!I?}JnrNdfd$xM%bF0#|AEbB~Haj>Wqv9UR)#8=?0}UWW<A97Py6H{`w_hq9bV%r+Xq677>#hN`Y0w>~1mZ;F@_ku+)8msbO|q7)={>qj>35%Mg4)Nm%JNNoKF}mp_<`WIuq_MU&74DW{9Zzrg-l}OHn2huKP$`yBt7E~1PM-{0+cAo_u;$1iV9he(y8Kkf{NpJ%FnIQZ_4q<fFdRfy|LW!+ErF=il6G7E0x_4QnELbH&6!6hTqOLpd9?|E=Xxk`~|-&p=mh-$YS}3Af#Ma`@g=w<7g(8?ULhY-Y<Df;R1;%zq{9{pOKh`9a&57<uw{!=QX<WHqx(ojqc~tm@6xtE{RKY*Rv~pi`S@MdX0jq<mAsgF_jbu@0_~itGq^=OJ1YmikCTav-BFh$Uj=tVmo4$dE_17o|DmN`Y6DFzy5woyom`9zX6zTgztKFUQi*aC|O>?R*iOwkd6domvnCrlSl1m2wN*pfD*eV%p1Kya9}nctI95kKGNn@V>d?O64YOPkgt$Nw9=qW4!;0MO#VrEwn<oZ-Wd5lvVF|-7md`>Rg6-;ZX0a7;wuKI44>6l?sxPIRj5R20@agA86_;GOoEAsL&*jENGuaODc}+1Q3qh&_6`H842?`ERRd5i_$V=n2!o5<CxO`^L7b$5=_c`Bo&OjNU6_FSj17<6vh$|@_!`4(VEl2YE2J^Z%G`8c8D<{S(}H2P!DmaGw0gH3wi$V5B$=&Z61*~_C9+U8_h>m9X}dh_yvQwEk#Lp`<IJ_3sLh6;wG@U3sRPsU-AKt4ZI%7>5j0-8lEFN`;WZp>Qqwa8oM^@Qj#&sySWP(8D=DY#%eQn+Ce={^00Gz0;Lko(I8Y$}K@#VYNeM2eAykqB-DD9(MnP#AwgUMW7Re9-0ZS9b&|33i7}=?eSf*qL1%?9%wiH@5HU&t&mS$;nw#;oLH_sfD*oL=)lVsP|uZZONl%{I_;`@yMPu;M@i2@i%wc$h`5{=Br#kS$F-ZCWWoz1xs;9$(Fxd-;8EKmD@4iY$qcUV3`C&<>oq>$`)Bcb#Ay4G-Rk7hj{OEf|B4>*m_M1}Tbp_FAN^RvQ1L&muDYT(cegxKL=`dV~cXVKceC*ZnG8Uh6Fms?B*CoNaV`(m!EtcxufkCj<fzH|447T9WaAoY=G9z3I@YY^ZDGmxb;(0lic)inA4?)y9$;dn2@v`&f9_}4L-ATpI;ErV(G{zb*&omMmXHrK#miW)3rARCEz(2?=n0q&V8^O4AYCp8jzz4Fjnb9fFMUBF!JC3WvBHgqFgR?VN%M7|Nfxxs2oQXjszrwe#fF@tF&5^c+rX)*B1GGE@j3M#5RPJsZ<AONU_lL*R4W@VqmG-5YzS_r4lSVU$z-n>>O`zydD`eRqO03xDp2qAvLoj*P^_&<OYK=!B)kC^&CdteTXLGt~8v7`ht5p!IbNnZbcpa(Kz>~EHia1iDa2Y*lTITypyiNF021XNc>;*&IzNg4UWEt!kFi{Au*SbR%K5S2YkFiCz0PZM$H;?K%{88br4&++FT(J{(oztfDnM^B+;0^a@Jp|pCEcQ`E>xVtW|{Ownd%o&FA+Q=N>s_^p2?7+=^?a0hFG8e;gSBGUxSI1<hG1)8zWT*p@<SRxYC!^6a?&N`wLs1cuVE1)BRKB<4P>hVy%XW~Xk->Q|X!&d?PUBD;zFst877B7}JQ%QKN}$sMxcxFTcXffs2a)s7YuNM=K)Ju{ekrDHOnpq>fW!ezKfXrOk1}09)urHPEJLa&4eXXj@@L2|>SWeXwvwRo;8wD#6pvgLLpbQk4{nDgKamwkqjMa9ca_mWU#O-fy`nb;QUk|8ek5t8mUa+0mM^`>k)yFmG{2GXNf|Q_Sj_hf%en_deq<{#{$uw^_mNTnI5J}|$h)|Y2$=$<Mu4g}3jx(y@HC#0!3x~qc87@hi3;&q6`H^By5__kKi9PL@N7+0P74M9|DU=y3$=Dz(}PC$jjx&CY}Z`PZqBaL)Ty&iRh^SVK|+xK$_u>_^ipzRfl7qLqAU~>j}izG8*G9NRul_zRS3Bd5ij&sh?1zcHfXF!QBooV1@A0$JkRrvubFGE?%#X=|IX%TvG!bZe)DU_c-!ZFo+I^6+RGa`=tkb)9`EbORi{x8-i&OeF>4j+W|aGiU4QEsW>cd@oGmzP`4qn5WG}{a4ztu(2w!-lmw1Nf$}ymUC8hVcsd)Z7SyzYZ8$Jk?8b7dn+MPKfQ-@L1Wa(}s7(-?Pi+1>g&pazk*I~bn)-xjC$C+7-nlHE5hkE8ERZI80IcHlqyc@Cmn_p+_@(K&NYu;iWgPBt+deHx03tZ^_qceL|?POD9m$;5yI+;q4>LGB6{<^7*n%;~YompGU2y3a_5-dd7*xu&ArJG6_(!65M>7|eGR1pJ}db-W>=-N4I$sB$-EN!OaY?9M%q}g=F{&sDs0sHwQ#w+os;t)ca_o?+Is*4K=p>l3F*Vu!Ob%{BI09K7-$)ckk23;6F=xZ;~W8j*(Uoc`2O;6=ob>l~nf(<yPmZ4|w6DyI!ZX`v)&;tyCUliVwGwnvTe!cu2;$v(`Z>QnA`c6&Q<8>hWL#5#fEgxwk29he~(<%zJSQLqokLKq&7J=g|xrLGz9v6NT_memnFzM_W%cY6=(6dm-%B<l7^ew(J^o(5Eow_v6M9X9rCt5J$MyqE?cAsFpE=Is%<xKU4{o>oxf*EMht*N(Yrr7Z6QH09IsqjA3j+YgM`Obz_o~ExlBu3`-s2k)L|GWI&x<ZuOGoz>E&qa2?B1N6rup_jFu~1^N>_yeXy19sGH^0-^%ZJJxe*dEqXS{B-=xO2%ntL?}UYL1XN-|v&gqpN=Flp2USEJ_(HK<4;8k5_3Bn4Fmj8rmm@1X`&`7(&55m_6n7si+2C%z1ptqcJ|Qz5vZmlDrJnPIYK973wB8OwZ^4MGa`yu_N3zXgME>31<~{<$x4*Z9T7u=zSNA#zOhF08KsyjrUjdPIdbZV&|THBj4Qd~p}75i=&nN>@XXvq?3Lsz<O|m9_%LsQl%P4{eKRWI({cDk)<F%!XfdRi@NzheEk}DCCqvmRw_u<w^k$U)nRGs4QwIuV?Dka@llFg-CeKUY4kAud(()S}uVjp5vC`ryhPI2AJf3EkZHuoqzOiF*uuy3+@|!=KnrA@SV>;a$@(&;{N)@@**Dii8YQBA94wNQ2}8fyTKT;lQ@-lY|)A@4s_2)&G+=>#_!O$?&-*eJLWi{S_el4hw_;N<8Ky0OXxH_Sn@SeI1YU+<U7Gab8T;D37uCiF+!Lvi9L#+9jNQYXJ!XCX5iL7W%&l?<;k^_nCsEZopG)BAgVY`pnjvMbixCfCNkIp`8Ku1J8I&o%PY}1u}P^DnAkVzivNn@>Jkw&1o?^`YK55t4k5Fe+qydY&xY8B6T}Fm5o~y0dwo6<Ab>yz35hDW?Z0mHk!qJ8-|lp>MF)v9#FyTuww1CXk*P1gUHGFV-mJZ(M%b*-X!BIIw;nAgr7yCS;4lA+OU6kas#_0iClYm5b-&7OclBqDeUe2<U3#o1H;0FL#mu@q0$T9hS{N}b{GdLsk2KS9{DPj#dUf!Rc{z!@kV>pH($jxV-Inx(a-zP@YK+U%mKhQjX!>bfrmu9SM$hxaJz4SB4v&J(CfErpZZ+z*`5f>_(}FZ}{<^26Y}Y^I;`fGMBJL`0zS}LH=H+L@;-_B|bb24wtex}ktd=j-`2326^UA+wZi;UnhX?NBi~RCS^XjZ#ydi$|Gb|(GkCdSP-iK33RZu*sq+T^PPmkQ^9t<Uyad9I`kEi3}20U4fv(R|nQpte!NqE}@X-i=DeU6B$JIQ{<;Sw&!?=RwFMycIAdw*pg`=`e5_kJS^yQrMmE5SSPvt3knhNSkH!TXI7goL(3sSNq^wekC#Z~yrHKjx|*4L`ZMLhJHuXUCbZ6;I+;#eRButRnks>TB^tg}O#)fB>$W5|{3{+`vB_iSjqEhBy~dt0NsJX&(e5Do5U!?-9fz8@nvoYI;)1G+as@7ts(w8P$Ufg#02Qm8fQj-2jJ&ZM4BTH#ebe5XLHDgQV)o5ln($rrV+xy!ov+->S!iJfhG++HmDo<>jr4HL;De#&Ptkd)D)w<v9}IJwt=a?pgEbo@KjdYKpFJnDnBFCk2;khf`3Qx0Aj!$dkl`C4?vllj!1sSV^GJBC6$qv}Watw|r<xre36=;RwJBZffRDJ^jG_PPwhEIB?4af9lcBI}+H@;GS+8l*GqOW7(jTmqp_)a$~Zj<|Furf$HcCR)V{>Eyf8&mQ43io_H#oRZJjUw7odLGm2M-6nf%|_Ix}YvSQzyz)Z>9$lH8Z8}4%0k+l{S+LX`51KWT}7^mxuOF8z)y-zTu#l(to1fhJ+gfq!ZiEEf;U;x>~P75qZIUX-9i1`XO2^2NV2s?TGNJs)3c1f`jp*H30Gw)1!#tp7WJh2Sh6H@&|M(J!y&!BWh*KVWRLZI}{HMH^ix-2~PP+M(++K>ZQN*?eq?E6I);}S_gVY>g`H}e~}$<VdrH`WY>D30+;FQ7~?zFCEHsp663_qmUN!!2Ht9LTvLcOZ0!$+dEr*^CKGUPPHXA_-$Ginu~?%!(cHYu1D22ZOQB8ZaU8dsE=j({d1HQ4OX<O>Gi104_%r>>7FOiDK7?c2!d}+_Mp9hXqG&Fm!7W21$gvv?40}492qSrN<)O7$TtH&VA)To=z`|x69RWFN|B&lZlm<IV{PUt)7}{FbpHq`mqz2a2$iZL4Bx$u0o-nJxHf&v3z7;$A^6%H-DEE!WNv;-p}a28dQ5jvWogR`U|ZIqpEd&dVC9#>cyK$_E*P_rei9hV=En|?_n`B*s$<#49{u$$m0`Reuc4zDgaV_VdP?AZvmylnLOEFNM|gFsfCvjKcEyb;(TX<u^-$2+60FswzGmmH~%zJIz=jf&%ZrWnSJrTe$O=1dAAO9eO<)>n&0!gOpixI@g<*N8;gY!&~MNP8w+JKrC=nvUgc&2c%&t>crvMlM5kWf4Z#I(r7$6o#4sIdr6w319o(8{P}(@dYjGmdxQ^u>TW^7=@f#C}hn3eD&!A$?#+C`8cpDVF$0~gekmwe7C)GJc#P7GjaZYmQAXnWeF0r&}GXV6!BskDlUQ*BjIQ<{L58QLd6CsmyTEaa|L?Fg+MN>cx{m5yR5+d|!NZ!yD#u>^<lqZ=$TTlU(8?>*mfsp{cHpqL@Ytyc6b*L@K0UI`$#3CDk+7y>31~a;zlNdhSPz_)!Zy3q{2&csQev6Yi5#$gySS-jV2(RrLp9niizRCx1iU6JwwQfEKCKqX;ERdQC_sqVHhGgbJtR%x`oWXDetCMh7G?&fPhX%lAS*L#$A)3@ZOkNODO-yDE97lacQqvu4AzEt^Ub2}=4+Jg&GWrj_Jm1lCXWnbRL#=-gw8*{jC8x4=Tla8_eN`gB{R4(zes&KSZ8?v_z5C3EAK&AV9?JXgf~G0&UHIO;%GPCxq|<#dBZODo`}>N#9m{7?ZKEZ;=ai8bI3c9^wmTG7arXyBs?ML!j{JaeM|~o|R0I#^Lr#Cu3|H&JkDg)Bd<8&jXU*OvgXUD~%ejX3S$W7**b{vwskc?bJ4k+ks~>r{0sh6EDSZe&H~jCQlzC4Op=Gt8mhCDgr5)$seH6zquRTshvMvgovP}$>kW!Q=-g871+3_tw1uXJMl;e0`4>FZ%ZI-)%<k`XCjNvxugWOk}IlAAJM{!_rC82Hr=YNZtB|L=x=9?nI1SI6i*5Gw!+Nb-1U4Nx1SnH(18X8n2$16=iRX&n@h;H73P`^Y$ZCW=1pCHut{GKJDz9y8jNgza4-Xgm|?@OpZb7!u4gn3bv#38(aNYo=t%N`-YV`}}EB}N8xny86cpEj2x8#Wku`U;ep7noR0g%BrLnYD|1`Z)&ve9bjVa?P>7$WaLb=IfsKlu+qndt&N=EYrms0ODxtaOn1P2Xgd%;7C<$Q%zea2UeEJ$n3EE+<@&CDk`6<9>;!;8u-MBQ<=wG_2N^!ju%T(J)mvIBzlAc*)U;6md0uakANMMlzI@z&Nm?REGN9B3BcQKu>kjiY4Lt2A(Et5`Mv9SlWwuN2GKH<ckVIiomGnJd?VkR+?Jt6(;3rmWEink(s6)Gl7bXG?Vo!USvT3a%dTs0VsWwMRNAs*58ya2A!6J`=?8EhBGSi1U9?u<{+7J2I$sj>?zUmq+mQY42x@Z!nu$NQSUXgp!l{krybkALN@B6k0|@2A14!`=2Z<6uVsX`0k|FheQoiDbVr9|Va=TlGqXGK_3T(ZWrh*=03xJ~|Q#Wi~j2m1<xD%JXk4FK9L4qzkx=vU~L(QE;ND#CYzj#rj`~9zEJfA5cm;2E_GM=oyStK5u##C89)~VHIRWY79s)_{T8PHUXDjt(+*{V^E8PC{R;+mJOCRC1z(q_OmH<K>ZNYLYUR9Hggf%X%3Zq+N&aArhDy74tUXIYB1Iwy8+hU%fKhEbt9KX-+@HD5QF?7)VF2#I!s&GEQd1C4C1m)5fE{6VHt1#dHzXo7)ocA-N;sMV%@$xdRb@v#(%Xw@N(m_9I&`FpRCA{joE6iNS*6iN3Lq)1X$uCUf2Nh<}CzABL9>k1^7@*{nfAMunQDQl&x@*}>=kN9WgM?iu6{t6`B(+VVkNz#6yK%x@ayQKmNwj=5MvE-u`KHRRAF*uXF6d@_m=T#jNiAz2sMbh9A0E|l=lJtZQ$>x1^NXAPY5)&bb-x3j$zt2xDLEYF-aLVJoO-sDiJ=~g>GB!$stj_#|W)O$9w}|ev1U@u$Ef#QF^1mm`Ky;5O=#dD_GwI6^oOSlD4q4|^BXSnfO8l+A4$&0P5{u~!(8&&Q5u=-|t5wA$)|snLwtm5~?Xe7VFvO=UtTmIUr7h^k64sZOus&7<+JHe4^#D36!QzWs?zsd1#VVVv;m;|`SEip?)#J86qNf?tK+)7qcoGS?z${pxpXNYc(;5rfaS_)$B?G<>7UEmn9~F94XQo*po|w3FvWZf_)ATb!fjA_7MO3kitUFf8RYcB5(8%qnD{vvaMG(6|<-KX9C}9XHwE)$RqP3OMv9Mi5cRq_Tgz|$M#5xk^1SWDHhh-w6zack!3<|(jOJ8@h_3{7u>3{#1Zz@LySl}i2Z0n}MviE1^A0-*_5;H%E6Ow-eEq}P6<xk3s8NadU+o<JG!#w}>^Yc@o;u|IB@52o{tP3gHZwETycWhz))QxA)ZTwv6KWH(Qt+TyCXu{ZtmZhBd<^r}t$XsKi70u(aO^VGy1P?Sos-`t8IhQwVSO~Gl%as@xQi$xM%}bJ~S+)V#%cFkHs$hesiXu&iPA^k(+3pHz>B&yw-Be|pEj4oiQ@#~q5jMKBwBW44t_|}BPA$fEVOY}=(}hq6j)6nlv+3-0KH=E9QQ70cYVZiWn{dv^U=QL8h^PSI+_r4!)ZW0pT<^c}wTTO<oG_I}WvDNdh4L~0xKI{iDK~Kl)6XNTQL|A(vSJvG&{JPqIby^j5GPZymF3g=I;uV^TtldEXzn-Z2;n4Q2wF(hMAH#s!ifqL32>a)W9p=p7sH3^ThlM4-^3f*YygL*FDVZ}5W%)6);p+}B%fPFgfM_a+&G@7?Qo8QteQBeRQ#&|E$@B)1!~TfrL*Or-hDb!2^gSd;8)!E;2O={xYXbkh6ZEh%XqLld$Bq3Y$#=*&PNo0B)zB0?QX#F6j-k6CITjKFfl};FL)p{7ii($^m*tbEEdBo;vKT}FHo0fSGX+7ND8qa1s*4WG3Kbz+A^$iSq^vX5R9hhWB&qcFwzA|(~AihnMm)AJ`w-A(_cyXkVp<tjDAC!l&%YXN02n&F){6tL4`on3(HGQPv8V89{^xx^xq!brYs1SU7171d}D-<C9Mj-u>v8B5a{m`9P&kn^%8{Kz6bF58iKS6{=Nci{0N4+fElMp<2EnAj2lhgJcTZf6%6pq49;_)V*NBcf=NcbADs9CGrYPFZ8H1@SC}D(!&Ib?v#!<h^t!i!hc(0qZ#cdIHvBS9_zjq04KgaiadswGal#ifd|wAt_*;P!_P_tJ)#ARoG#C3@(s6uxc+UD{Hk&%9*u<@PIhd@07Pm?XmOZn0U8#!`l7b-B9h}`V8F&sY{A4mvJZP?ou;l}m*mmtQ8Bn#Xrn=pt6V@mtsQEw#>Y*Ewqlp{%O_E*t+mIFf7hkn2(Jl&3S6C0p7qMKhbY_|THi)t&fQK6r#CdW`ZE|&2sz>z5*J2|_6$Nh-Z)lgK<GNU+sftiWaY{kuZ!)PlE?4EksWg*fCBJbiPY~1xDSzKqA<;*xkF%2(?ja#0Y-sGIMhhWS7w(7#hCAM%U$Y_b+>@rEoiYlQOl}=@N6R8&3^O`iI3;F3wskWt%zS*W0O?v6E3d8FlZ(Y$BkQ@TtK~qZx8;)`g*u_~U~)ZNL^76mU~SYz6z6eW4nG6~nO&@=m4TxP*=Y(wfTPAHp3-6vLTs3gvr}3ut|teC+iTYCPA2j=SvUB^jgi}P(Lrbx$fITv7#M0~&v4x>d^$)LopGfu-1qs3Dd034vX8VX|1BeA{t*#!+meSc^*t8DfzEa2!Yr?iB{ds?JZm=OO(4`L59mC^b#k>)@_ROBl*2AcKRW9{m2Wv1Q$sScWjus-M{!y5iUjqYQxH8?+6tjL>&;>;^8r5(1lESmva-<GF&p8eIPeKnbq^?kXF7+>O1QG*Z1o}uW^PMH-Y@Cz*lZzq7WowjC?8my(su=o0ywfX8*g)+P2D4rOJYo8;*7!9JzMr!S3w%*1NnVeS<@72;P;lRPEAxUUT)VgR%R!pKTNmEG5^552~&>2Ug!OUDMt#G+QiPOi?_&dBWE7636djO&*f2Y&qbE{5nOaWRMa?XHw;hMV70z(C&En;fkwmoU5H*#y*eHU!eVi8f(uuv+c=3dgyMtxTh!Pqu$#|<O^axBpcX3!v6x#lEbjQ&vA0czwd>j&L$cgOy}cQK7>plL_yx|QX#8t=w2CiZ9MEvjG(b)CD=>Gm>m~2wL|zfcNaV)!2ERUdRQ`Yfv!1~8Man4bRPDmOv5^SJJA>mNCjbkud$5^kXIaX{n?w9A51Z?4(Z`K;W6Ge|vNfG)XYoe)<?KNu_x(TohJyQiHMpO&*+mKcIJl?p+sOA}@Xt7DwDc6>KhE@x1A2jmdz8+DXp5}p7VD=u)}O?ofv}qA02dkhnjC}fPji5PQB5WPMTpM{m{_Cy!|S5_i)4IU%mg+fcbx-$KRrwpE5^7A_ha>m{nO!o|JHCn`oUjD{NY---+r)g|G)pH5J(9VgR8|Wy5D|*Kx!)P_@YwPv2NT|1d<15TN*FdEQyk0&KfSM*iAl6AvH_TAL445Fok&*K+rFQY3Zp&3iFi7#1xmK0gWZ0PYnpXYGl<=N0!5q(ws(*lV*`@8}kH#kyEf&N`R5cMu4PFixI~$mh$bJnMwV}W+sh)@C_})SJ}|V9n!C0L!V?Cnr$fIK8v1dT`ynFj5<K*;yk2c>BQGzL!$_CZ#QVC#|3a;bPF@uP6O6+v4o7?T&LA;Zn#tj4V9p^5H`<P&*g&cpy_ZH-|Gb(*1~jlAIfxwzyDPj*|JQ2g_ze*m{;7OJvW}+MuW&ez%Ud#p)!BszTKYdxF_KnBgR2kM7_a7et_Nx?knUz?y*wJE1SD;pcnqMTsV|nJSb;w!*|Os_xK95V#?h=gUxQh$Fcf!!17?)GYDhGBLeO2w_YF#-hnbNok2SDa8ItivJdY72JG$;Dt++@7S}mp<`$PAK0arlk$##5q|yE{i-F~PA3S*Z%NG0<JwG|g8?3F9O&?O7BU;#sbf(zz8`akls+}FP0_$d>@O!L;ac#}){U+WSbCFy9BPJ)+@}oDMG-Caye`qX~M-lI)R|ct^K`NprU}1Yhy%8UphxqAv;=GITKY1Ur%=4vk$aSJ`DTH*Dn<~xRRO-jB6+#x(kdvu`a8~m|6$JiPM8e&~B0QR4O^T-e0cy+(hN|G&@R-eeA@{MOs=5&OpsdH9qciGPdXsf9wyHF-RSA7q6+8l(`bgYM8r{<k9`O0+G&;5)zblab#j+^6X)^v3(wv{cK%Y|ye$e~HKmO9uq@;#28RfR!YCaxmalhxNZwW-bjo*UVaSH?6s4#U4JKd^m)lY>_IFn5WkUBgkoE@nEHkf<s*f^JNLMJL8rn9OCWF!5>O>KH&P#X-I48-;&z7_LoiNvIw!|Y_*TbpTX4CV?qm;?_G3b~m#<1*<D22Dn})Dzdb<4hh|(u4*{8c7V(L>)@DKxI(91PA2&1vIGG`vY@$>(b8Yn9AdjA(!|6;I-rI<O4(LA<lINJdMOh_dRv$;$fOx*A8brCmXz$>27b`KmAPEc+jKxfg5K~J!QGXR2(FKf@20#GoxcxNYP*<-LT2hi|7Qf5|~AP)Ra1~v2-+*fiz8SW{nWqfazyr9To~g3WwQhAFe7N3Rr9Dx(ud{-z}PWc^+%FN&(bO;@tGh6?2ah(+5?u<fHa=bjEhSMub<%{Aw25`$xUgT01Dm`;v)fpt7h>i}CSkhC5F--)8YEDQ7%HBRtKVH1XPD=C7x^N&R5`R5`a#O`3A`U3Kc+1se}s2+jFeJE$0i`?0rft$q9CQmuUBLp5!FV&eC1!6oYLOyX)zJ=8-n&~#xc>)0s&qiexL4385g3RJ*jJnOx9G0sc|!LK>Af|0KN$v<yQeZNFZ|C#a)8=rOnG)W~dQ;rR0ksuIwijG!YeQTGRWHf!s3tRG%Xwn|hc*Vd-C{I+^kiz5ZCk>j7{Dl%}eTTi?fO19L8aQUp+3RjEAsNcna<~1|N}H%9g4&OD*%F8SkV+<PS8Ko_e9nMBxwPrrkXe9i!}mSTc^FF|fYa#V;DCEn85pR;F6>&AT3aT;w=EDu<<IAGD{fS{b;VPU)G8@ow(W3pT2)QjvQ7-~f(!Z2-aI3IR#}#`A3Ng3r%CZ02gf<bXcDJ{AQ`4yz1S^nN^j%9#d~$30`_J-AOhKYjvG++06vX;=GmCwX@5J^Oh~MVscwlKhJk=UFvqYGi81lI+R7s88Df$ar8vMH=RU~nfn<({CQk~vE~YHHghMyc4UI~V`1VFBY_k4gS?eWqkhpdMh*TFckhHH=#!%lJLzu*UC|t~^EI@ocrYU783ggt7s2O5CW=jHQZ;6+%EEOr_vKeBH-&@ev0Aok3EgU3jV1rXILBSN}L?Wk6|Gg`0`nM5Pg`Ur${O`=EpT4Ms`j{m<VvGZ{@ycDPRgf!Oth=?GHuGE(`Qt|=BA)!40#ug&y*JV3Q`INv>B9ETbQAByNq;9Ud`^e6Z(73QJ{Ub$sD<^<v9y^WoQpv~qh~+cB6eQIMqRNAdw}^#MtPp)s)UGuD#)FwC-$?50?4Fnx!GtTf8llM+L5GIrWpy$j07&Du5;rg8<na6^7Ijc=c*n9Z$)=2{6A0@!ubIQN9xaqItO1qvis{Fn2G<*S|w%4EwG>dtI3t*DpwL-k}JvlpQ~~uimfn>xMts<g#_7$Y1Y*HVIdoomlA^9*v&QeePTsl7>?dt6D?6euKQTI$)B+`b@bsouOo%&C`0>d-nh4tp|vDKvwB-|!5&v>&<6YXC3_s0(AeDoXc((z*BJ$2aTy?;RkUpcXn3WZb|y3mYbS$n89XnoGwG0<C0$D~py7zww3+v;1OxxVtI9)1z_la<f#jpyyW7~t>b{c=y{DaTNg&pizoOsIHC!wTr=5Uh@9_GefkWjKdbzq-;)k+C+dww{5w!o1@oY;3SJD@Z;+EY6s)3B76|dH8@bU6u@fY})UBgcmo7Yl428<LOi7%JhMn4vJ+m-L)DV5W^5fFjj3s`&rG#B10_QEJ|IJ%oYg0BeW#6ZBpB5nCpd4*qrA|y3ogRZw_tsU3MPc<p%OB+tDmzC56irV~7?oC<TXLvJar4A(Ksn)|-n;7U2r=AWQP5p|t*K}#g-Hqu>oC8hGz6vOG9DQ!YDpC2JEY)+y*??44obwTcaK2(ZOjlt;n37t=Q(P_>0a!kagPTh|>EocRn|hck?IZ=OBBH}Ri|aQ`22&>)HJw@qrDmS1`U^6s#VeTMubI+xOrQM42iZyi7v1V@zKTuoG(=o)qNB@Z?8OP_R%m!Etlu0hGzxL~X3B2ZST@GZ{er*C&zH|j)4{vi$CiLjo_gIpN#c%t1?Vy<^_c{F<tmQ+u08PNoXz{w2*7_rnd<V%PwVPi#@)efI@XEr7-Dx=HTz6TCelT1Iw7EZs_<77hBugnmF^{|4>w+#A|rP)Bo})DILZF1XtylW6Dl+#0mmZ=>NTU6^}k099Pa{uH}V<&?!tBl9=k2`qI3DvXxe+HGx`deyx5e@e#9?Fmghng)DQ0|$w{W+z+|@zpVdJLpzHQ<awS?nmep~K-^X8h|4Iy_3$g+7$)SFdOh$St57cRYrq<AB3f#Z`<R|(xPK5|X;3jf60qnaK8J#K=Ays-l<Nd2ssuBXSm1iu3Yd*Wt!sN)#OND=H&X;8ywCCbL2%4Al%$~ou#bnqqjnJ^>WOfx6%qlb%>mN%_6G7f`8?0&UCW=6wD)dLe_Ans>LcI!CRVTRV{G*J&!}2vszAh{n4|RXyQ&i^D!F^Sh@nU!Md0{)^;`fUuviw=uqUSrmS)NIKX9#N8)tf5Sp2{aEW9|KlwS3~>GwwwO`MI7_@T&`1k)wO5r}rCYMn@Q+8R3o(o)(;j{xC5QPV*>>=QUlUfOo8tq+C@!g7*s<W!YJsq{J~RpIK$Fbn)RowYouK^XBf=^m5d;C_Z@*52xr?N@#Od`VVK8cOF@yStb74#U?A+LxkJ5{1a!mQ%jCg4tUcfkdxs+$|bcHX$=ROl`bOW&o)$A`EbB7>nKfNAg9jP+zCMnyJI9D=KV^!zM;_@5aw_`$jd#!hazd&dQK?S6ka2cjx$TWvDvpors<CAXc3JL5V6=y1Pgad^p=>-LJ*mtPn{l9^pD_XWP$Qz%A-^%altJgW>O^`lo|lNv>dn7nq;*Xkb)8tH{@@U*06Ef@&8-kp#tkOc#j#dD5z>|K7BLoYhIVi`6LIR^suQj=?JPjRfx3M*z)Q&em>h68-BO2tC}!p%;AZ2u;r|F8@pSkw;YY55<(}3kO9#R-5vu*zBQM`W`%@(&<0H`=ZU?|R6^89nJTUeQxdA)+*C>K%}lVi)7U#Tlrs&xm`6#paklzcy|0GC;*?qtpZ~MC5(TDC!PFEnRr4KIrf_YNqMg5|Zf0uzTnt~B_%OMXw1|Tic5E>Ov~rEJj#vFfAiv}^h8ODeQw{N=U2KK)Ju>LJY25_rGo3coqFJ?;hBhs=H#P<Zaba<`k5o7eN7%$gq`9=SE-VRF>$y#IZhnR;`ucA*&*a$anny~zi7&Q1@xNx7_Gi9im19Z6AGn!6dm>>hdFg@RlY6Z6cc7<XC8zvOL<(m(K;81LhJKk6MkPWmZ@w#b78c6C<2?F~4YGHB{V&u?j-R5)RdJxaVc3<gQ<;ju7)DU<XcqMbU}Q)Q+PO-shZqw|M<vGGM*prt;ep|rn#e7xaT|z}hAr`WK9eh=!EFABWVW`CN7TShoT(-3G@>Vp2oiM?41L|=;5W_~Uf-2(!F@xo9%g&=L+@@iQZbNGDER|MDv)WiFKmSue;tjtESr4gddt7^2DY_NI7&OPW9$9)!7B~SfmMX$HxM{xF*JElPd636L%3V?mB*_OhvF*-NXzcnGAfp?+<-b&6{|I*uRMl_Y@BFNnLUPG67EftUA3xT4s#55`t}%yKAZ*=#(Kx{yFmc!+%?#SIc{q*N>Te3mEv1wGL?c2<7zii1WI=*X;X2vepV5*>b81T{M0FGxQA3SeDQ2=&UQnjk?Kvw6<W2phpQ*k`ZsOP25pw^0nb4IrgtoSt#>AWnz)$p?Ulf)=STMV2)AgX5Bi;OK=UreHSrhRk9XWWL$6GOh1W;5ym#zx4Xtbh4BLqnX7=#CG?#m)-OKkFjhby^ztkz~S*xYvD2e2joQ3b`5c^59jCAY>(4tZ35E{bX4)Ps8+I_J7|E}(Hk-N3xi&FkZMzMEfW~u}qaLVrtH3FkO@|N;#`0Jh@eCH?rDn^K4G{V1Fb<m1Q+9>Pe{mH!QffE71nm80@_@^q4#;YTBp><$M3?^e&9)Z`S0nZut>>XXIsHE!2=$6`zohrhhyU}%3ipu;FZzf9`9}~GU{)g`0S;c_O$*DeZB@8Sl^QEZPal=R2nghwVSxg~5gb}IW`n@<Vi)|W3tdA1?j{HFldz0X=?O0wJH5n0ho#>#G$Q=)iFAfQmZG86l=WQwmMzehGuyrcm<TSB51CmglFQWI(2*rg0-ul{#b87qX=jcC`U+WlMBHFbPSS=Y0sG$M@<5NC<#0#{ojRig;shY}yow!G{wGS1~;r9j>r)7mYMw<bN8rBFLiR2!QR#VXw32xMbqy@P1EKeD+D)$6x#sh^R(5G=sL&N@md-<t`iD%WtU$i(IZSaH1M;MK<H)1y=SU5rS3kR_IdhvJUP3#Rpgwwv`J%gAB%SpKfe8>=c#Y{v3iWFZ3HU*5cmMq@Va*i{neecP!?#+FuWHBQcqG(RTiDQ(Mkgx!*7uuBc96SPWO3~S@6!-%w?m>`V>%G>1I0?N`C-^Bx<7#h`k299X2n&UGbr$$~P5*6>v4Rtj$oc8B>;qetEV6P%oJm!mDz_Ur{bi9ZNzyVoegmGdwdU=_0<9sFh6xhHR92m?*fh=?yv86S&4fxxYEbj4Ibu#GvDhvFANJ_IN&(3k>=!XwvdIfliv@M3TWMAZezfR`V|u8eN;7GbcQueKo^EK~$0;As0x|Q;Me>4E77lW=cFMfiDRgE5<05)qIAxXp`lp?8xx8_9%9Bp$$|E;H6u<AD^2nZMt{4vTif;+~UVCIsuc9Z^YDu^{;hgNvmyVc-_Sp+F9vFH4QH*m^AZGEQSig4!mF-_}#7Zh=DN@O7wY?V^);puhAOwtwa9s^3K~XIL;Sf0k%NfoO&hxW;BZ-u{O4(u@mKGsgcf`b?X}ndi#QnymC)#U{`0?~aW_w}tQQdL=f8Bd*h%><5ua8nYHW0`Pe;KH%{yA@p%Zw6t^c|ab$PgODR`XQF)tyl+;qHZ<(Tz1qeQIYY2GHo=GdqK0p5r82_jp@?<Nc)&wOA-h2xNw(+m1mrnZ;hUEpoUeCqi0AqaOE)Q$a8l5Zz5!{`j3x`n+2HxL)**>e`R5So^2C_WQk!rsgZmEDOEzMFiS^WR2&Te%((Hg$?i$Bf&uL?&n6xb34GVIZ|&`P2r7^@=5c!rn1-*(VccRc}t|DNOpuhm#u^uI?9H`Dza$loOdTL1kIJCPTa-OTLI>hLG`H}(?i;>1b0JKYkddQ#M6Fd6pP&=*_(t-7>s4rAH}K4#4mG5Pl7rWxr2C%2vv29M8Cbt0~4uKRZ(?ID%Ay#Dk3ti(8&*}A*1|2*Hw3(pGj1o&k{Gx5;^BjKH+7e=x5f{>*=DnQ$r;%omf+urwnx`b-a7Gbot&?OL#ezs8A(H5D3>ERjgxPY7_|=9i}~6dtWq`uuNzSuGm!J9S5sST7&V0T^^ofT<t37tg@EpW(A+)UHx{EuJ+Ua{*n8NrJLbd10bg;I>GLdQ&d6rX^$AW%k$Uk5w~l1sG-zr9x+spn67%njG}Oxo(>dW<q_!)X%wMQ^Hz`8g<Dn^uX{w6Xx<SZXcG3Q2%^0Clxu9r2LEQ)*tvf5HrLo*@r#~J{U6FNM*kI~LH4;`u31Ku72iKSqJQn0r<Z)|hwi2HsF(Q4(?KAK`&F%cZpn8zzD0l<txcS?eOsN9t-`rZ$(86WLwZH2k_&&V84_I->Xhwr2N+|9H$e&Ou0bJ!_m)E>%OuIa)3;0^B299Q65p^7JVh6t@fH_F%6x4fXhhe4sKluM|2{-w^mmsJ=r{=ep|YaUnHy-<KH%_bAAr5vENcYlp0>IAfOz2mc#@hle&hpER{>Jrun(}6{*jk|O#kHDz=xkvfSJ~zX?!c8dFUUpl<n8}LtyWK4}vQ7!20_J8UzjImtdR5hQw)s;j>D?`;y0A;18>68oNSiK<W1}1W_<TKoAEkB9_s?_Xqr8B6arz!G~0f=#4lwv{Z5FQ#g$j3geR;NAguy{Ne6gL9h1H)SUtDKcb|K75zu<oAswr!jVt<Qw~SH>`$dhmY+5s*$@3o{uB-4=Zh++NBV_7ZC>!Fl5BiSxv@Iaj<_3oQp_rkbfe`dZC~X^@xL2BPx#Po+2vzO9;y%3^eSE9P7ahEg3e+|`p_wg1oV9hBwy<CslYjT&vHYk%65K6?+K8pi5O@yA{<>L8OR6i^8L{_>^&<F=o4i{eD>R#K|Sp~)&Hj33M=o~zF!7KSkm4q8|-|)%7K>17kK-~O>o<<lPGAK*0N%JT?W-*F2sL`;v#UHAGxylFRd2-YgT;&V2);FSHn+7XpKZJD?qOx<BC3*RKmu@@y(tj5dGvU@hpa$8K*&z6V0e*Pq&_^SYfKrKs+3!>lL~>8x9H~c~AJ+vJ#zyNO6#bRzg`&hladZ<aOA4PWgC})|Z77s(3hu`8Dl60G@^NTRBmznmkJy6T*&qp=e$pgpGCR<X&6$T5n6vJ}#gR)e(cQ@Wf16kA1AMQVB&e$(a7fZ`cc0lBjD<Ki{q!9M>H2s&1Q}b;LZ{KsUO?<D4$>IAo;VKH-ktL`zWFqP9<&Bn#zDh-WfMb!oh^2e_>pzI7z~8Ruwz_kuCPi#H-U>nRb=uU?oWFI{4Qw*Y#^V+zjF*coVJ^AylKd8PjiYyW#QC$P97flp_ANu$;>S(OC{K^ZD6?7@dSUiTNz5<oqG{fTv8o>z<3_>(Jf?<qzB3D-WZS7O!&A7jF%4#FiSZ1)T%ti<c-rFig_fG}E<@&K;`!W!&zt~-v!H3qABdwpdw$XmWH)}}+02<IzsU<WIJOPYQ|e8Y3_uVArZCnyLnsyAT>TasSbQX26XSNajYp2OuL6{KiUqQ}ev=3&8Xv!NC+aWTXqt?AHes0g<`5-;D)qEZYMdrC{uQ!AyJDv!fA95BB7=V7ChAAc1z6377##)>oAhTzU9?)y9G?oNZ{X-r}-!M{&F<G2aAA_AvC$zw(~gbJ?4I0__*%39L|ga);NQT-*6DMUX;S8sp(UJ8v^)!BDCL8t=X*0P_9T(@V^Vvjn0Qi)SGAh!V6C^cy1mDTF^f!NZNQ~Zui4c6I8_Ql!?bT+bvsDTc976P|NaGjApeDBJ4bu{GU5COMeIr8m^O0u3KJWNgi02@*sVo6uOOmVvxM2O*Y{6GNJ4VUlZ^44<zRoWvt#QsB~Qw^G$Ukgp0ajE?q@>8}O6E($?otQ%N(|aLOHAL)*OP#A-FCbC{M-7s{y+FkHic1Y|fy4L(G_{z#8v-&%-t$Xe`6zHt9~YGR57<_?XV`f6iroNKi5kA|V8h?(Mh?$aYdQ|!UhalPkf=$q5+@FiM=Q7?y3Qi$@>m`i3W=ZnnbZ|?L|fY;Hg#dLIO{FqFd%XfF!nWI^qd(N3$3r3sq+|2_6IVdD~il@D@;+O9xMk#>-<lsa~ljNLu5~Uk>sYjhgwZKts_cbQDx!|@qX$fPy9AP#J&mkfTy8Fn(!4b?K7(Y**Uwgo>x*y(q_Z-eO(>6oSOT`Do0l-w8Y!8bn#yFCd{KJc_yDH4P_p)tH0>nIw^z?x+rrHuTHB?ks-^A1XFMGgqpOEDG!;0R}N|e-Zgb7Yo;Mfvs{-bUElGH>V~GSnoEt>JnlT69~P9W>6_l-1Tua+@MmbP=kVG*(0|+TpH5WSFW^5P2jCL~G$?lx)&`U<T`kLwZ^C~fH9_RFS(T==w6EYlt+nYdAfU_cCYgg09_}k!n_+?cEI0qKnY)|KtC63>NA-EbX7YJ>YNuCkh<Scc4)0m0OGYdoMN0F8^9zdKrdCB*hJrp^g4<>>!rZ;8Vmm&cpg#6?MxzZ@^=_k)!%LTztE9n-z&2SBcwFy^?omBtQ`c7}yPS<Bigc5=V*iqhI?4?+g!VhoYfqbF2`?MDCmIe@Kkj;#GjFYiV^yQJ9wDe&GCu8KoGD?wt5QacITyIGavJ+tx9@^bH!Xv}nsSx&E0d=z&W;3Igaje;7U@11la+hTyn1;C<0geqShv;m_(sGGX>+Q>#-NiU#)E<(o}}xz<_7e!J+XOUla2mP=+o`Wx3-);0bNfrZg|D!;%2RcLKsoXf@dW01c_7ENUNKwipS9<FN$ggB$!DljzL9Uqa~bt`ht+2Q%AC8JbdyK&5o~3F5VRAZ9XOI^diO3Ql-17)9>-|FVq_f^-xo2kruDaM~K3O8e@vMZdY%c&VTXB;!kx{yS{BHR%5RaK-<{y?dDwlieTgJt22*o;&Z$VmY(~CbKk~@;_4j#qm!SRNNgmY4?0X&w0IkiMERuYQ;Uz6bGvbVW)>jj3uoI>_;25n%tK5bq)vd<J93PDLFQ3*P0suWmMWK*%%Dd)QwW~ed{PptM+e_f!UifTvK~|n+1`Mt-9*c=6%8NfK4|^rQjKXDGfY%o?u;EIj6o9InRT<A%tn{*I*Bx*Tmxo_SX3bap=xG<{9<GUMPNH29DJ<@jeKZ3(tZRZ(*$co!<LE(w<_C+dU_~f8}D*?HjVKEL`7~rW#3qRYRT)Lys_qr_%m8Nx{`HJE+&zq+Q@_Af;Uv_QZnG$s+RXmf=NqekzfK-p5s?Z7d!F7%x_E9(BWcgqmh#G;7z3wg+>W~Z)iy@r2Ic$OTM;Qvo<v#t?htKgLGF3Dax`;<alU&Wzhz)ujxZYqxyn;UWg{+Wyp1ti;6}#%gIgt!#F2eJT2)38DMU>_I3QQP_qJFUv%fO5-sE4+HK<Mp{1s7Ug9vE8k|xJ#F4!jIPYdzEAPUj8c4om(G)6=uA~=s{z22Jsj^CUo|<2PfjixSINMMYCY$-E<MJ0XYT8&5<g)jR*TinA*G#j51a3Et`9btxx{BF7%=*eMEYG2SJ7t{2i$&V^`UY*1ne`^x38=h|<0)C6=(N{o7)1jW>gi3#To6>J#bL#bOQNQLSWuD_YaQ$2efO?%x0HD7ubOb+m$vReZuvlNcT({~L(qeMp&wH-N<2~0F}~j-Sni}3IDkL7Q*pH3{<7E_P=v}tg|WP+tl=KF>cMFA!1?2|X`PKOoKdi>^Pe$roY?>d<x_i;udu#psuXs2tD{Lw#6I#lIF5|H*$DRnIqnjO^QR+Ir~OhSLw_w7^~*`4!CJ`tC5w9{oFmgtzF30ok!u=+ly&3g>G9GT??lcXO5_fR7!x_`(P_$6=VLKZvAl7P!4pL}wF*YEGuf>(B0&((H3^M&=$qG1jeo-Z5AO8SL`sSD?jiXhH9Ow*NwAtXKR)1pyL+D>T>rrF>~emj6hDw{e8U&F<@+88mMp8_4q@P-9Qh7!I~KS3U?tSu1HK&O#&>w7eCpE&>qHI@CdF|)SGvT%;C`E=a0j11$5}wcP!!&GCdN{1B-*K<98J*Mg({2JfF}HuOWz^eaZg?QvL(8+Z&Kv5p;9GpM^Dc*g1p%uMbAM_Vwy}BZlY||xtw?cN3wYS?og4W6lAa$ADq!<RT)%#W8ygX?R~7=USUIiE`8*SvgpA-ga1{BdLJY(Q9cM&8$uquxCsM4RTlHk8d@cUna_<niC}jwhrKUn&57oomw!VpyUJa{@>Ygs=13E9Bt>^Jsz;=^c;`R*2HfN=30TCkbt2>@k-CvE%6wjfCX3e`c%O!lI>Z*O%D<#TFAwwN3<dI_7mvV?&xpw#me|bLNX;Pj(vj4L9RMGRjE#9GjcxKO<T~coP=f;$R`_^BzEePb0NjKeM4L#eb|PtGEPE%M&Ztr;l7kvZ8*T_>9YVM{`1T+9rtZ^zag*Y+cW6mydHck@*-uoK1d-~-FdQ1L-kVIkXt@(53Oxjg0g!{h;eqJh+`2CF#xQKNdjq~~Kiv4X?8blmYq&S0R=mE9AY)4GZDMhU_X#Pe2SBkLy}XC?$5-LE;sA2MB`wwy2z0~%Dp}<P{MHyidFRR|*>3rKBJ@nYk6_E?7LKiaG7)%-e*c-b3JlxjWdJAIU@Hmmp95f!oMsKDgHK<&pTCv^=?G2RV(i)*;{J*!hLlkWAjvSzOa$c3P#245zCQ!16!*}G!XM>ZSkyOCqHY@wqPzF;d_)aM<UnlulmB3gopcUyXuuT>Wo{5AmFO7r9;eQwtqaD-j`-sS;vl5F-iiB*aY+o{=P|LmcHoLGe;=E$J&0M(SIQ;42srO1GV_kIUzy*#Ia2&Aly!pGK+;-3%7(Z>h8xSS@!&hbi4kXo8zms&sxtC--iI{4Eb!q8QL0SW(_Kna^}5F`+2dnLq(sWd>aT<!S)+Sdtg2^h%{GTPsuXPw{*iDMigglAR`Yr-Vilm4lSGBh{Ew5afeOshv?7^!Mh1wQ;j&E}9Vy={+x);_h%>PbRexudt03-E0+^xn<4lj&OF<7Y=TiErk@Qt&%8SG#ifeMkNIwyRNO4budb2>SRj-wmb~97`f~MZrrDPM%)XXZ|uno7t)FZ)BpDpouw%muLljN`~zWR@*rS%_tC83jmav$_$By@5QLy(s$Cw+C?Wn=fib(2CaW;$rF3Xy6V+-2hV9FU-9Vk=v&%4Va~p7AB5wU}yj!E{eI5SAdIz)9i?`V%U<Ahm}20sk6QW@gz!n~gbQ>ng7b_ZfdtCf|mMl+cGtueeYKLL~y}Qvx^wHBW1_=vy3&RIlKF;vMDBCK5JEg)c5=9>Z6F5_Vyu*DFh-pat0IP|l^2m$@{eU`aXesU}tq(Eh0l6~YlkCq!;1;fOY{r`;K0?%n;wT9<|g-2Zgr?yRPW9cUc8=(@*Eac^h*a+kuFH#U9^kwHiq;<LYY#{U2Ay_IHv^#OnVF2Ffd_Xuj|hF`P~)+EUiuj1EGUJt<-aSr7T_u`!M{w_)eZIUc}IHP*A6MfDdN^R+$LTA`}@jJ!zoW%na(_fak&ObF<UGDbhYxme^G-%CMe=iP$$fmdlZzy2IwxrTg*v8^^28(zxM;UEDG&ve|uXODFLQF9GaoN>W-pd}1#LY)85y;Po4N4`w@)$cTmyXc+s3J+iV0=!Kq@a|iskp#`LysU08j{wl%q5jD39JT-9%Ub5%Yc@O<VHG4Q$>xKmY7x6%FjHpp?I_-nFm?Dp+yZMIy8-*K=!RlsMP|w9QJK2f!=t+jo6S!uq^4%%3nSOPQBR7-JLn3wyMFD#BcM{H&B?Db=+Ljlfy1b<aI312SqaABqq5vaVfFZHA-rZjR|-@AhoH!Zm<r*&n8iWB>`$!lC+ATG$zwM;C={JL_r74v8+#Zj0cmFF!KD0)d*oil`Pq8#n$R39eM#Ort>hQgo<ZfAUGk-W&F7eKA|{*RlH3o+{Z6i7LE2PkpbELu?wCFf=!psZe6VCLl>?v!%i=92%?)Paj8`r7OjU$@Gvzp7T;LQ{=y@sSideA&4u^#2Up*%I-E0h?vUqh&O+r50n{nG6%qK7G2KbXsy>vope=WmiDTk2PPJ8GWXC4g7~FzEJXb#AscBL#yb_wJs2Rs;ejwJSRk{GrI6uK@kom;QifgRrMo5w;^86*dcKJ%BGhgWcMTs?(t^e1)YG{y|DOC-$+{ao!s{&{ZW3Lb<HK_4Of#)C@?h+<Y&_-n~RXL3jJT^TZK+Y7a5mWe<JZxfV@OI=LHh{b=QkkT9SBr8Y;2%`TDfSdi=wi0u_EnaQ%xDpuxJkr}8=Uoj(+61I*Grc1#XmPjxainF{hnyOKe0N8$|&P)+gI9>XilP7eT+@da4bbA)l5j?gwaITL__~FT50%kutFl>GR>bbBfHRw?ODzllyLpcH#8>h;=U!$ue`FCzNH$#K{UA~CQoCD0&#iRA!Eb>aT5GMm9vXgF|O9|6;8{Nvh{#pcG_BtI(BP1kg!VBZn1iG;#yFWqGB(A%jhGAzHw&qYWZC;zx4%*lW*-$syO4RckCiN@)2sEh`V=HY@dH88F@J+^#ww>=ry#asKzl9L?G3ciKlQ;##iBSI{tjj`W{+XQE^XA1Z#DdzYWuux~aTRd^~zRi!WN8VZ*;(yy)xiLsiA>rta)~kf36-W|ed;4Rsz3n-tYi3No_kf3|#j@53)VpHH(#IBD09E^nDnAL6J=t*=@Miqr-);kpY!Hb+%VX4NGy*m?eMV<B54Q<L)P{8T<o>658pnX4q8_>NMrWSZbJBpra`JCkTDukSbqTtawJLUklwRqEVzjD}{RHsmsgD7j`!o%f?r?N|971PL;TSmug7K~pZ7W1IL$OqYFCY}-)$ci<ZaYc9~>dy{MP3%RzId2j>c=!AbL3kM_a)x(nX6UvY0q=s>w9BN8JZ2i6X`~aiocLO5$L$I{iYkrsMLHmJo;_@v1lKU&Z`7u<>wk^PF<)O56xFxH@{Qf}I!h1g)sa<#L_T(RpQmUkcbEXhPSx!kBrRBM7@pt+=1Yx5$O~!C?C(0nQm5A37vTrH-=B?Bc)HGz2kiAMUG3=w6OE%%Nr{-gM7902}N=91C`&_?>CK9hdpqv41PiZppuu)X3pqU3Og2>zue$3BeuzRQ+q&(C;&$(e+TnCqZ%v3LlJh<?O)a@t^I?91kYm09nn_8k$AnYm3gnh7zJjV35R*HI083=N6QT;BB)M12;*rV)bH8(B9XXP3ttyjKw*U&B)nO#T{sHvtQK4lsrVtkID;~G>`8oUJ9YmtpY>@>WFD9EOh%pzMueQ`xV(L9$lNE%QY@UgcNiL&xqM1qZ0L$j=~B`K7k2Fn-~NoM1uc|^yq*j13|CiJLBkS<g(iAmd$sE|n4Jg_7VnG>yxIANCs1b5L0-J~eSQIRBN-daG@GiqTkNK0IH`$FN7*eStCk1`e_hI?|r5DfJnvvgLD|8vAg5{vi=HC*pl#XO7inQOB|ISqvA%Yqy4(*wLuEY5C2ja4nK@pFfX!YxFVA!L?}(>fjCY%`{(@Tc#pDqS{7*>!v7t!NNKR+Pd4IE{vKpk?)buY@q8-}G1`Wc{#%Xku#M&$H_FAb3&af^p(r)zGpWj*e@@OT+a*XhS^M8whJHUYJUxMD#-7puFL1l~<lQ($Wy^GCPPx@EaR1ePlTi)LlwwDc6Qc3J96Up=!FzI?y5If9=^|VHqjZFySe=R?&_!lFLH{%Bb32;sVvSTDo@vmL_S<d{T3W)};3huS0pW>Wc$5lD0bM%BlYYvrl))A~H%gz|+)PqvBMd%|RcR)Ih46x$_#|ls+qi8XTcRYZ>#>sh_qhJdmE@rem1SEXG&GTPu0<-<HsHkHJi|Nbt~30Ef$aj}xvt)k*WR18;1zrCJBwN)Z;4yTI(CX!T#ezqxLhL0&c2hjo8s60Sf=3lEJ{*I4OXG-_3`OLAefJ3cyLr}+v%Q%R*Q6MbIUZGKD7R^6rDrWA89wRsY<JvQATl2)f$Z+O2))?22VEBs08-Jsew8Sv)q2E2_LmwVZUPaP03B6vwX#uqI4d8O66<~rkzdc@gceY|%Pj+xAO%h<HzdX)GIf8rE=?+q&pH|>2_)>jV%K)(NcAi(-AA!!m<vj|V+Z6bxTI+yL^Sb$k678IUs!<@NIj~0}zCKa+|_kGraTE_y31)psSBC}6TT}l-ICIrgB$B1yMVYbZl7O;A>-*MH0n`Y%${tOrZj?)TirsZSu6adLe1Cf_`uJc(65W~jE#BU$R0*`pZ@^#*@4;l`@?)>MkU!mrtmMe4zXu`!Jwc^X;MLN_Knus5!+L}-DQxyFpv(=dEstodBt`E_)psT!B3g*4j7L))?959`vT7yu9U|ETal}MyQImrPT%EVH@enTLVpF)BSk4XmyA3jiOaq!b}qZVITZY`@bDsPnsj<%iXcHm4^hSzYD#xXNT`0?@N22nm>nLyS!2er@ZIPOhUe;Q5v9parKMfJ{C{JS4zvHT@lEM=Sh%Ijj8spN4H%b=IEh-KC$Y{(VRn=PD)v-G^e8QfH}Tn9E#88QyB<}BjA?I;;;cmPE!jL$9u8M7C#P~#lPjO?^ymG(83X;^vHqSlHS6w4rf0q03TpT|o;%c2<YH?gwoq#o-}Feo^}9VR?`7Azt|n7D{vit#xg_>hyafa0;=;MSo-^|#+YX4zohzK>_2SC=&3>|Z{va|yAE@YM&XiDjq$^re@HtFWay8cxaPWUcVG`kHRxYoL8bMfIhZ*;Ox-CNI+wl(z6MT2T1b{)%%!&24)bp<GEc5%U@=vBvb{(!cmfNoE^x{s8tO{EZJ+2WbU}D0xtfW<H`S-K!PqVxFSv!4Uk2s-vQ6F4E-+op7R$L+Uie(^{ub#?wM%q^TN0{h%ua5x#SdgOarb^CG0~rjR<W;%R~ypAD&5yN?X1gN4)*AksRmGNx<|E2_?GToHQ_SXPa<Wm|PIYt|d**t%Q9);;<r>W-nx`ve~%j=YH$UU!ee>%NUV6IA8cgO317|7KZVokmrD8QCx{{S&r(&dBC-P6v;s-$MWhZ)jP+DAC8Ql^)UwNJSJuT9g12HMr5T>DYQ`Xm~ayDn~IQ=dj6P3!WI4deR)AB>;fXrX#~q57OpxZ$|>%&@~^zX$&%3<;FJ~*u*Yj#RWbJxRrrxVS~@ICc>C~Z)>o8Fa;@>1$8%ijT1GrcAKD{80x7b-q!H2Sd|dqat*Yh!UnmVCQ$g3BjXLPva=V12DV<0WGHShUqdpq(Ep;piiax6&YyTE7FVly1w1}p@HTG~r4937frS)VC9>Xls!RAik(IpMRw&Di-HUtOPH+N2%EQ!8Wy7Zq45?|zY4*SoTWX9ELfAxM5=@1d4GxsKI1JUWiyD%^vut)pY1nc)LtR&O4m16{jUw`_xSDN<D}ojjr<CFk*^u#m9%d3QV)`N<7P7MTPR;wt1*76r$CYXuT~kxMH>_eQ(T`(Qy|s>sBakx3FTDT~GDA}Jl2@DFAHviw^C;6ZrIti>Z6Whhoi~9na_>jt&D8>h+a=vb{1f~WS`Kyz(jSTPfT8vklg_qV_8#l`)FKYm;w<pRn1GuevGW%{RRb`#*F{rNW3$sS0g9id>89a2lk&LxU*F)!*hrWiS%;3yr6Y3{oAt(2zWI8hE%f3wrPis?cNuLFu4tXw%d$R@j~Xv_tPQ0~?0mg8#Hu7AA#;Sq>eUov;oRt{j~ZiIMp(gw=8}K`9PC#I{dSScj};|MBtcOBZQ4E5X4fj1*tF=m@|?;C5wmrq4(zz6E05`lm2K4n3?f|d7H!FAt@yt`P<HkguGjPdeyKHmK`A53`Y>UqvO=lXS)TTd%KGZ7$Gs~12bA@PBnQBZcCSJ_2Tsa?oA5m?WES@`=Zu5^w2HZ~c{zMXxO<5aP}Z=lzLq*Mogf<snh+B=*8L5e6z+LsK&)B8Z=LA`lO7p-EiFZbJ0*1Rty6U#bY;*&E{8oJw_>B(r2{o7i4!WHLKl=dW5X|M%9620wKGv4_AL+<><IJKsUDT<shf^4WcbY2oES4G<#v7cl7ZlDoPqXm&UW)t^R%THk@>0oxq=7aa?D=%D$6(_rlMPcsiG76ICx!EeAhVa1j%n7+Z0WAl`q{I)+g2sLL#`07v|Lv`hJnqdFcenmnAd8Ax`7-#%vIs<>-xZRk2vja7;#uqE4p88!Pcf7Y(-SiNv0Oc}pzGkW6pBs{^v-PzS=Km%T@HqYPBy!wgg~m>j1nNgpLI>|&oL?6jL8f63RMlj1wAPZ!NL$)dG2C^zP-ie+jRzqA5y@>+&q<MAT$3SO{>ipnDiK#gr!6qj@;MSXIO&qd@FIE3G}VcQ_=Wq^)obQ_hHxE-A_ZJbBUp42!&xpKpeA|^bjod|2JdfA0y{M&vf#rxt<*k`|MVZDHS3g~Z&^Mmm!Tk2e6`V!pt3_qL1O@?bHn}H0_4+8pV*3HLuNjIclu5=sVTI)lCE;_4ul$K2cZb_dpW11^p7Z9>6JC>X@VED>-Y%>o6Oc<dtBa41u;$zG-Aeu8^H692z3Ww79SyU7ZX5V^^j<B$mgo<Z-F50YeWCoa%&K&W8C-$%R+PegZB`FyPhSEX#1ZtQDd*wuLGdWaAFW1V~7@8g~z85KsU;$!6U`7#DEgP9;BBEf=gBAs@kV6VU>%kfj%i}<E-9)?U-rE3t>r{GkadJ6|)BlcpeeTiM#G{zh4bakvO&anEFiyp6^QlVSG6zT%Hr=aAV1OZ*r&yWdFjiQe@IjDpj>zd8%dH$e$-6n2FTx2M%r|0&Ob#s}aY^-JjbZU^D-I45e<+idpD~p0n0ZBui>mVOJmfwNaReVHn-W`J4>UvF=5}uIGcI{S3!qf0(#<%(LV&vX;Qh>Cz#^J~o+s9lNrI@dtN2QxqD1RKZ<@big~a1j5vK+QXYfBmibo$NGM9RWGFaa7qxtJ*>XwNmfL=kkXI)n)!Hbb<Odm;h0#jJ;=JSlkcsNt%bk0DGy6P}<)));!Hv?2Bu&v_FHX)|};-6T}v?N%pZn26pixa>fm&N^wCR<>T1(w>dj^)2_50e9xLjbZNh$g5+Oy51bQzCmTD6DuEJN$%9A*0go-h^Xqy^Yi03QG}XXMIQ0ECX{iZ!;}h3{ztp#+lY4es7w40n)&6v(+rDGg1OEBKpcU@xvPfoC2hkDhYt51Bx#T@s}RrSpIz;zc)rEs-WWwf8PDolJ)p~^v6HOD)q*n#&jS_$dNzCAJBAcOP~r=TUkrRHGoJUxE+mr+~W6#3T%x#@p-|{{G`JUXRjKbwA`d}^FH6f+(4BkxD%?lVeG;ev~TBF0wR8CfV&xiZV`YS(Q64QZ}Bk0sf36?eq(V+6!z@hP~*t*0KYitb)0$Gx(}oR?&%l07SmCEBz%Szs+`~%fC`+?n8UHLnX?j_H4!l6jMH{a8x9#!42bnwpkNd(Lvb|vTTaCQ(aC~WXxWyeYuJ=GjPCSjZOCZpV^uV35b$>Nu{&=p7{xc_mOi$4o)ZWPG_A~N8Q5tQSu@A#rW(5JI-U}OJmYsjB+p`6ad(`}JnL<ky+yzWmO*pc+*Lpip{{v=z5%8s;Wj(Qb3OY$9BNK90kG{QliRbXwM8IBjT@2?cbby}nN0#>gmu$BH`P5;+hbtD;?lr6Ed_-nfr)}tXRvUYT+O0{f9}1;n8ipJH}e=XBkD7eI*1kHcxHTPIM}#BM^La!SCi7%+$c3DVOreYnioIWSd#LpK=xv8tuc(f&4eAcWqp$%OG6(VW<86`;SO%E9QeR0GnpHdCLl;IH}P|RZ_t|~%F4qw93c&Fu#xg$+aaornmHkdZbrsw495~z#UaM-$kCW&2|}(+u&Ao?%;ODS--UIG`+r*nX2*Ge&t8OGYvO|`oLbd;CRI--SZY`=!Pmjh2rIk+6OEc@4y#EyYv3S)UL;Ry`_`Jw-uTbvd1i)Gk4BmaNfYl+vSH>_o0pQo7J>Q2By+0dwc`cFVI5-@#UW>sY|f9pgVh-G*3K;s8uwH-{%C+X@M6Kk(1zR0_;5A4Olb!t$y_zuH3rjuVpbUkY&a2<hdQVn!(P#GA_MNm3UxzVOe}LHUSPDl3!1{D87bTW4X0KHeg2%AV<0>E@GbT3_ujv<coiY^rpjWo8d3V%DvJ^wyzJwOv=t-y%~NGXF&n<2tmt#99_MjQ5nWqe-7Ct9s@UDO%bKFMf-)&aNy)CQwuT4Qnqse-qT06&qcqhNIX*E$+|z1`>6w~hQ=C6Q^wT0`;p^j77R%NAmiv$V_*3Fd&tRWTb()UZSo-3`<%vu(p|QqmYCd7H?Us*b&q%0opg%eA4M!SQj?BScGls)7t@skky4hpkO9ht-Dzf(X?p`(&L2zQ`SFsxi#lGVSSJt9FBdF@xd?+E>56*MWdBZRL@gCR0_9{tGcvwtmkC<0R=Ta#kxK41_f4TgrUSLZmbAKaniWLq=e%CMDcvUe~BNQJOe%Wf)hVTCk_uFJU`c;Ns<)&iXu6Q@{JsmJxHM9u1I42}24b<U=8?L`pg3YwSlzNHrA^^ilLmU7XlzXi3yljbXWS1|H4*CW)r}DzRUQevO8HzLns@0cYz93kXUYg-fto(7@W97Tbi=U7FSToxa2z0lm{6}z1IG^k5*t+;gqGC+ypd^GOATrS@tNg$sU*z0`&V=W$RIq1&gU!IUy9nW;(N0Cq0LSos|L;<+o?UuYHcP4#Myf5)j$s81ES8NZ8n|;vf4oCWtR*C4Y+*Duv<I8uH!aSs*aT97VB7?Cat7cE?22Xn;S}L<-H0`%p=NFgBDxJpUjd2cxSYnylJOyDfm1j-$5L!~*TRxSwLhbk8j*z%8qKmzc*k&*ty}p~4ueiZ`#?H?rE)^IWEz=rk}*~h3f?}TAzOruk&Q-@qQSPaj)}rmiA0K9d1pXYiV$&G4Wt82<yt7(X+^0B@Ld)>DQN7K6RzZ_+IeC0k}~v^gn%LUL<-+e2I3WBP9>`YL%?#Vy$A}ysY!D%G3?W3!xr!qHsaAhD1@tiCy^O;Z#&k~Hdu3LMyl2doK;Bg22kmZ3Roh8SNJ}RfBYI(mjx-vO5KlyeJGX-(|76DphxRIlVT&wF->jUo^7~}422s6sb2=Sr44^4x=2EW07>V`u*n2$*jZ!#qzJ{0q|_>nKjEPf*I2B=y9sp$+6g$ycjiruV3~HCU-wNof*OA#1bEfhW9wEu4v22}1)q?MaUO4c1nViEn_`w}$N|XFD9+>>g2()bOsMG=>W~Us0;s}MWqJw~>ur=mHFzQ6W*kVcRB41<Q?X~m=z=XP$?sA9&Kd1Vs&DI`h`+a9A#&_nK7Fq9snH;|XGY;Blv$3p74v?xio*LEg{uwKvMevU7+@YT@&>=tR~n&SbMZAjNU2t;IC0uN5sM3YG{@p}$_*o+&4ldX{pl>Fc^32Bt7=9X88>T&H_P~Y122rL{=id{f7;e{$>TqN0@AABdz$5a3{iuu@0xPu7>7He(IAP2Fk0O<wc2xz-87QZaV@!uaE4wam*IiXRmRrEXKWh7Gj|!(F+d}B98GU&4mtUcS~gKw?ExO*ARV&}Ys^7aO)$lj47%eeeRB$J#>4DSoTW(qPOKGN>5b0HS69B3sxt4{uYWW5%oPg&Dw_=x?i@4oM~xp{-nMdHdpF;<#<s2@ehJOnbbvoumcg;!trF-)_}(}Q=-uP@PMJa<(grx*LphBtkeo<`&!~yuhTX^h#uQ?rhE!0PBDGG5jJA>7OtJgTZ}#>qGC8|R8oQb96NkQ*x2j*>szm(P^LMMU;jZ-!V{K|Q!<AU2+sXsCfE($~v8d&+Aa7tdFf)GOTzgQG6wcsCjdtx@GfFlE&)eAzag#Vp+~Sfy{Ox>d%^kjpyJ)q#o_Q>8<0c+D0Qe4DB=7@!BE?iT2gDXbCSzk+i$^+>liPTWGx)QiF~TmFt5)aM&pWrZ9J~9}p>7E#_i`hCh`W}*^dpPAXsLb2<<HTu=+6xL&Te4nI-H_fG2|rSDO)MWn8w)w<vSCZ4Z84v`v@t!a&Oe-zXQ;Ruse=n57ZzQtfQnSryB<ODU#tke2=KV#BW!FfaJ(w+knqCIfIG-TeXEX%!p(WV1_;z2$0zyQX~8o8OUa1#EWp+2WtBygO{`18pd1ZV~R`<{L*B+y-D1$#c5{JH8hq1j108#$je3Dgi3^AmDuou=P;FhZEC82y(52XAh%b!;z2;m$__P>E<1u}4B2sKlU2B&lT};5VK6o7>VT&wh*CDIn~-thF%iR{um<YJam9{W@KIN-D234tg}=P|J<-r5fx;xw+Ku%WtFhQW%Al&N=c+s-TS*n^DOPlY$)^SK(HmLRfdB^UuvUpX!%KQ2TQ`BPiR{}~H3<L`Cm3UG+Qmg%G0p^aewsNI9f<}D?Mo*<r;1^*tDe}Z!h&z9{t_#YP;;lv+?ZS(q+H<4OJbx)aq&x~m<f#);1$D70v+Bh=&2+aJV7|sSLXI@fN5AR66dGhaD9LB#wgrX4yP~?O|4;=%Qmp81V8h#w8VJE`ShY&NNUVHLRRN`K=YU|(qL^}@)TBrwk7b>ATu#7c!ap*;=A8@iu}n^bvHW=u%>pLQM%xNYDw}W{-@DNefW|W5{$dPX*g!x1TyjBm2xz+kT7IX^Yorvd96}ZeKAUWNi6D=vpuN=y+Jh{S`)ytV81ZgXQdHbhzPrD$sfiJcZY4)NcFj-Zo-5;vMt8xZLU2Le+ALaFKC=FNYA@mD+$KoQ~^jnR+hh+#$N<;onebYeSfsRJ(`2WSD`~9=|VV(hNUJ=wCE!ZK-W=#261VSSw1q;kPrzBKK;h)DV^ZIAA!<Y8aja4AdWp)P6+VlKAf;2T6g7?`nlULOFl-k4VM2#+sgsnMI`-(tYhX?cU15VI26U9cK{lP*wl7Gj>mDJG>u*esm^iTDqbU?j_DO*HxlT+sewgTf6f4P%kL!kKy-Sg<}=vyWGOgrrW&|kgVmdfVARj#b(gkP$OI0<RZh7jI%CPjH~pKr_|^z^4FW_>avJ7kLKL|Aq!t!4PT22SWtEFkZSi69K-H-%VI#pXBRGBuOSbUoF`LASn_QRL%4Sl*0cddg#c}vGRCcXE7(0ku&KT=^Dh&}O8)lNV$%cByGeLl$Fmd8lrnb0X@LPGQ>GkPP6BQv*l$8Y^Yv4Cu+pNAL^V<zgaYU+!lEWREz4^e%E*hsWobo+P{juSkr`k3#9zFQP4;#>HZy5}VA!C0GpGF4Q0i=0UB#g$z&%|@L4R=GNgF?-;Y_FSvo#bf!YV~A`tr)i9k8iNCZf@PCmMf|zLHOnJ&O426#ltPajHZ5tCiD9~{9wbga^|hNO(ZX0EfLXU{-A8NqnN`nZL}&L{NbA@z}{R7L(0Fdg$1(QtqWms)sB8$Eew1LUqda-*IHQkYPB#WNgt*V*3?2+SQf%upkByJg|HBAgAr&qi{Uo*Oi{Obw*EB{M^FR$V^aWiU%u9#qK+i&++x%#VLjTYm-uC1I4Dohs~fPI>WU_{Qyjh+3R#(-{D>e*TuM=hn`Af%^NE<yXN@t)yQv^$`c)N}ioG?xKUU7%=#ASeWPayjEbBm1smUx-eUvcG>BNGcwB&HKY`uV4uc=a2&c`${C~wJp<0qk~3+&{SW-RiPs1r76qgk9Tx^O{+JE_YN9W?QyhIvwncV_vGGwtU>ORU1zCEG|&{wXEE09SWO59<8moM+*GwRyt|C~BnGgI~PUUtmbXtiGpluv`(N>?3MEZkl%kGI5$3o4jh8rMKq%WObhF7iY~rP01k!m>DJgIuBHMvrOlN|4kMCx$?y!&eLRmPFIL)8M#&;{*PBHF`yzc`;6jwJ604(9x3v}nLkoKqd_}PEIa}(uVzHZg@LkMCIkr0PSQ}A^Qa69G`mlXNXN7>+G{oss#2vn50P5HV#eOUOQBA6@R$;q1HD4|madL*(5bN#+DrpwbU&2eEblo4gSJq<h~SUyYDA;+3cbu>l<$eTf|rs_H>POb%Zpc%GtrauIJmw8NOy;dCKy;fK|50<4u<BggjCTQ``Mt!aBNyl<!t0!1-vX-;;nIHkzkUnMgr^1JTc{2@J{wi`R*RSizMb|t*-hpJ;(cZ+xyyW&tFrw9dNvLw>_!b-dL+Wd8MS6efD&<&mOJG-q+;)oj1m1&emV)u;<!g&)<R$JCp>XIllb5Ci@opLE@SAlxna(d$KJx_u03#&z@{jVbN#T0E$}ejWyYi*PHCITQu3z)h4^s1edki{S&SB`!}@O1sHj;)n3V%z9rrEzcF{)fAR{btGITg<ocLv=Wr?1Gq=<;C!?I-HETD}JO%)oq3QQ7M^j+ENE#*<7j}cND4H4fhqWe!9HSBDuwM&=F6#WV(Wh4ZObgn%1(P6hZRzdk#b`8Zj<OO9`)-8|va%d1ICUcXl}s#wq%GH5AJ&##WgL#g2MN#(X45l^FuR%oAh%?k)<ki>W0GPGNKJVrxd0T-o6s;Sq%`OlPVJIvxgW}u|KTh#@)<*@Cs3!OUoWwX+%@AKWG6_IA=$kWi{k~9gA6JQH1&=pPVy@;gVi)@yv$&uGFVirEQu8pOUeH-3I4M5NZ69&M}W4}P<9q!14ZJKn2<4@$AE@kr0%vxxe}wwi6x40NM&w_V7~^z2j)=>eww`XS0Kt5tYBKQ*@pcMA&Qj=Pb09(T|*stQ~%1>F)Nu)Ls>JbC?C8f=~0H98V7}==|ZK7WVAL42C7h68N@Ya;*QL~GUMoSo3Jk+mncf1^5JfCiQUMLb60SO8)PGX3n=Rlg#2H&cyGRuIRIFX{j;M09UkoNEu#Q_ISR0w%e!rOVIY8&Fa#lw1_Cfi5-6|DI?UsN0BQ7K!02ib=0NjmQ#leAd^`{^ui{!-d15A@Q(GIeXTZ63kL1j<3++@+dEHDvevCunOh95%-8!>FU^;)(KmeG65fE;Il@FGYb^2I~`p?c34!=rW&c4zzZz5MQwjl?wz~9jC2^3~5ddc5#pFlW5mAV~>gh0rM3HL(?C(_p>FfFHBF(+2u=1u6NmCXnH2?hpz(|PfLpmAA3SE6j%D4hyKVd&}<<2XtklL4>@6^fhQ!L8pi{_0^tFtMiI5h<XF7$!_fQSkWSIMmF2aHeLIF*o?Q<#5m*p+oX!^szdQoM~4*q};dveN~fvyI<>`ugNaO86MSSJ9;!m-q+mOlv6)dlZ7r9ggo<9mNk#I7^s*#yog7Gu_jPgg**x**{OalRxh*gYeOgL5u-yer#5*s5GhfHE?Gf`a144h0>mOwP^pfWc?MkR^-iq@WpHXEUI8yvH1ZalNM{Y-me>$VOL&dDL7k-un#(@b=O37XA<9or61Lo|hbwN9)%GiAi#f87IbZQKA$z|b7>*jWh~r+vnB;Fc2-AcL?7;oM`P}sf(y|-(I(PV?@|)j;AM*9`<e{_Y!cO}ibqlVbHvE8_7Ew4=l?T0tZ0xLJkT1nSw?RxV`Z<700`G6RT7h{)#a_5iykSH3d-1K8?>!h_{7g!s&0k(`N%@jc5uq}}QNxg?VjtBnX7^H@?BWH7CEEFtK_99$41~tSm4}V#AAVIQtZc<!as2~4TfFlM6G}P@IOQFuj=c$~APl~T$0(Mp{388t{C;O2DSipyhI@PpukRwct>AeccxvMf%3cr5S<%h9!`gpPf$s(yw;k^U1U4S<3y?o&>zoC8@=Um0sFW-;aIrif!H^Qaw>iU#jub>JHm;mZcjMPWgD-Tjs;M+8^^;X2yQ@+*SI5sl?2jlEI_@$JGqeNY*S5;aWj7HkhyZ35w<#YUvWW1_gnDnR=p?4KexkTmIfZjMV!4ynO|pY@jPreEi6tvWQcnQ&-JU=IsZcFA#tgtARz8z1gC^G$Y_*pnvWA|sbRaPtW5})ZWKq^tc~|H|Ck*ApTDm5YUR=o5%l5W{VZxkt(N{<YS%q`Ggo+3V6}Kh+wq)$!SBcZ60*zQMy)1L64Kt1_)tMs&ZB76!!Uq~Msw#|w84q{NJJJaHfrb~g1FpmJj`nJ}#`(JFZS>lj6>g$m_hu0YS8hM-*k=3Z-aPw#S1CbUyeY=zCW13y$2KlI)qoz#FR|->kesz`Dc$BMma+kzPHV95lBp|coLhW7-7!2Qk_|c2xK=nLjA_3O=N>bXXHJHnxcJLX`eQ1eA6(nU<E=GS2Y{Y9B~Dek?{BTle>hSwC^#AIvK%&B%7jqQM?G^2Q+v>Ak(U%{5up+#a6ADf#r<asla&J&3061z*I#R^?{N-kN0;*8;yt4J6HDqPu+*M{hy?{9S~5l+j;_*qL}muz;bfigJA-)?8*ba|p0oL&*z6!Z+AwH9OXZ0Cremz~eGRii?u|Apn+MK!5RJ(ItjFw^c$oQLcQEgl9{_78c2*6e@{34g^DV$j`4FXcm6YNC{AFnLE44-Ti0`nGFA9Y0f$w<wX;qvtRS}C|Pc@GXOB!y*3Vi&RG~D|I0k;>GmzxQ=VaOL^B2&AEqA?wta(QCkZYYtbI)?PqPhMN4vHma%xCuPnX<*V=e%Yd(pT)0CY2ZFCN*^Ohx3N62YBk=7Yxy(ocm4Ql?%@H848`q-82L*%O!E*E!GxS>g#$UjI3WQaIAuCgGVgRI^M?zcmiX=tA`}8Z!@>4s8c!TpQhaqlyR3L1Fx~Y`>UxnE;&Q)FN&pJD;I99a>loz6J9o=Bl=VE^YA%yUyETFk^5G=*`ly;%e&+)zcDkHZSB|y?X|>8@_J$L}8mPJlgRurGD*#=|l^ZAlH!`pY^&=b=M!GX-`sn}piW%BmdEBWzcBS%&26q3%99hE#WPEmxY*D<4Q>w;RgB2eKp3GEsWXjz4)(Y*CsN!mdCfm|eBD9hqr&>x&6xw5k#$7=n`j&0`R5|M~`)-A3u|kWY+VnMH#wV4XXnYzbhD~Y8N*`o1(bC$hnW1m}Dq9Qd66EM7{%B0t^g2`n)-wa$CBrMWCW~PXE*P1)RoBbEkyI+#gw=%lAsn%FYQ&f9?q&h25xc;!C`~rc!D{RqKYnTQPhx?WW%x5Daz8{AS1v05%(unx{)|}U?^8wl`*hEn5FSF)$>aj~+q#<X#nd8xEAA6-!!IqT=Ur-hy@=;fVvG1i`BQ2e-*VEfwej@S-r;9?1fN5+z?p11CfvzK^;;T1$I1S(6KWS@=;iU<v9!e5ept#x%FTXi!j{~V8r7g}@|><o4VWwK4cNvl0v=|U8kLIqEQ!z9-3N^HoMDo0k)lLy3Fd~iZ3jcbrbvk#c6_eqd(~Yyxt?4{dG_ymO9>6;!dbeWPyH7m7Y{MOU%XdP6h0*fg-Arz+Q&vcxN=@M_ozUO=nwf&Nk@zAE{kvPC1%Lm(YZYpA0?uSV1MhzcCtPU2>z*;>{~T%E$5Utv_Ba)fab0IWc|`O6{LU3h6&*dm!+jlp^?tYNdrK~yolYRisb#NTq*%c>}U9HuYn~x;|7d}*(fyRl@T=|65LP<gS4jQVQ($!pgd%T8HpscC<i>;6aCG4EsBa84;^)WFtXg6%UUcO_>A?EZ~Vwlv8~Fco{cJnyzxUWF$(Wn%MJCHzmYpSBAmlt&$zFjdyvehyuP)K2~5T5?k37^q4y*YT5mARqB)6F+4Rgc4u<z{LRI!6SjAZx1$P>vUy{xP5(dMBjCsg`jTk0#P9QXPv*mQzzEL~Ck&v6mgvTrQ7lea2nITF*6+m@f7oh}9rcmNREpyAsp4&``Vj1I(kGI&RE|w?}bd<IM$_hdfeuh<Yoi{x-)XFX<Lx1G{&1Vr#Q%JhT!=7Iu5ffIE;2S<yT-%zr=0fhSXGI~im#YZ|wFyJ*Q&(`SMXTkqsp2qosIk#m1Ls}<X+(`mv*0DQJxxl(q&^7?vKz6Kw7xYcycJjhlj$hHz^a7Nx~jcy05pe6Xl;q)+7gM1ZhHnZj9>jCe%;mhwMV%JhdQiXp-x~Da49w+{_QvG7_ULh?ehimasj)mRiFiqnUjeYh&|B)&QBH0cSgZ1uDB(RIjtcH?D_g8U4t?=I+>Y`=rNADdkM$faqL<xG)}gxK+FTPo((HMHta@d+%r(-Ga(dyi~HP@tEM&VGH2)sGh-$68dy1pCV7!!m)zs<dKno*p0WkRp{Q~p3o)5mB;S6xkSfmI-fwD=)^6_-A2W4zQtj%5m%2L7EYh%Er0G2t>BK!z7ioTvMM@6-G+8T_->)oE_V$E&czT86>u$LQxjYS5k8C?jbRmc%L-ogwdiU`W-&<tP<EPcSs8&*u1}R5lBwBnZIov!Z(NcPI!K1|y;++qbE(lgNi=@SvwY>j`ZJ&R+MBmL%T;71nvpoHlKher=kQ|}&0~u;Je1ghAc{+*wRPj^KmYJjWL3t17zL1d#+*cBJ!sUTh1jcSG_h1(*oiHIrfCi+K6|X&ppqWU@Ib!i9l)0=l6ZE<as~3?ELjEC=K{FADD8+6ZM7E}QAgpZ4_+>{87-A|(9vA&thsFQimj4|o2265ZVWkfvLYRg{5zu98un8rY@FNbaHn*fcV!cqKpAi41uSBPusQ9!+ZbVYth%-iYhl#eRf00hr>Cq^*W8R-X_1bdd1CluAQ!F<^{GeQkqhNCArt%@ClNgM!3fPhDR6e=<?@$Gyvsm9xB}-v9X+#YO*8!111a$;NqShE}U<%jpYh{7nt82tc<N^EkOM^?sEPhb-1Jrsz?Efil(s$XgGPb^ZzM`+#JMMPKM39a&<e$IlejK5`B@=;k@`Q1*HpuW&;JIY0O)P5;)PLoaHf;H7ykA2UB@T=6)KI_(2@Ni#xA$Puwqwf(!fM$*i}Ve}KMdPuOrHq8P>vSc7>flS>(Ls-b403Pb_K1;MqwYPHCiBzflb6107NAKujeswc_Vq)GYPlHBaq#Yf#$zXr`LtH3)6dw$7zznN?bnPNt8>mmZ`%VcnSErR%e1D3w$i<=jBg7e_imrE{k0Yo(+CCAgym_(npvS<F#GnIer~8mz|N3Y7#>fP0w;F=7vQvR|t)KVE)J<JvGDZbxA1(6mw>|y|!|XW~1p3(}35=VpMBQtTRyp(mT?mOruIskUPbGZAVZfOBD>zin|gO$CA5C_$?DERSXUe#i<f-v|wJ>bs8l3i|()Z=Et~&Eiu8{2a+vxwMbrW`4Q9IP5IwFy-T1az9mq<T*E#p2_T*>rpkUD$SomGax=rs*N`0p15F-=U~1}!fzQF_=)AA8+Rh);08I>2U<&Rid6kbr4N6V(d=7F{bp;&F7}4&My{*%rLEONA^oS!q5vtA4c5GNPa-wbq$fHrA<5We%)A*cK9%9{H+SqnYTXrF{Xj&&JD)tJ`((i?_Lh-@MG?QFLEDPL--OKy`%U93Dyqq-7u+x@eK{L6F-(-<I0-+Nxw6+Czrkt3;oh1o~yUh{5@CfMKF(11S7)>Pc>ua3G8x|_}R@-3sL+QKXv=kOtXTTl|*32NvVl!gw$(EH!Pn4`Uo2$YLI=!4SII9}ldiqSxBZ+k*)X<ByX879d+hoe8ts=1jVFw6(FVh8sHQz2^bx<ZvHBngW8K;k1f&J?rG@)HCF@d2y7aCzH1_fiuMwPM4%(fz%SJLj!r?nE8U9LfN5I|COnKZm6twq`Eg`{B%JYP*3nAt9p29yLr7f@*jp3iA-`HjW1G?e?A(%Srrv{tCXRj$CyR=Ef{mTFpSOH4S>Yp8<tg3T+X$*}1W$n-|iiL3L!{eI@DxuL&1GdAbAQQo1^i3iRklf!g=qqGS+N;axy81E!&8C8M`RPY2vb_<rH22A+OEkmV<AqcqPcWK25$kGVn;xNmEP+0R&I(Q^ck_1QSeYnyM9Va!JL^s}0i>X0oD~zAUlOP|o;R$PcQoIq8*U6-F@F?UfS&cO+E+!8xkFuT{vA7gN)0u4JK5AS?p}k=0SfMS|4LI$|deLYA80?8{xM{F^$lV)0Gr``7Z`>=yAYkkdK7Or>isH|cSAN4~gv*)z_bMYS%mJ}E`771BVmAOnF{n^b?Sh}mT~#?u;f~OZj|>D%Lz+wjik#)l=Wb%lZlVob%0N8XO*Ff3{1(WqcmLpP)6q}Lsw4&<lX0#)`w`94INn-6mfbTHs~~B+Mbx<C8*;hWBLIpAg>D=+RfbtE_knN}zz&gTqHBXZb6fll{)#m6mXFRWn+0SAwZePO2Fo9w`B$P@Obp-_pGE%#aKu=ih{)eiP5-YxPNlD@%F#`f#@1C(KwdiSelZqp`;(iKO}4yH!@J_K%hKr#b2u#b=eTm$-HSVu;^eE%*)B@Z6zCYZnme`Jx!X6~pFvLhsm&S0)wbTBQ5+e#tJ4<k-?T*oK*sYHE!KX~@F#Po?b7oz<4DwrPNoxWWxICm!-qk0r;#%}KK*yE9v6B=e({2;g7L_kUh5*}LkVKJd}i~`Xm4kL66;Y_tDb8Vg0>zcGdWio#gP-bt)=Lir006E#loTl67QuYj|(g+DIsfj@iMlnx}3%U7od_y;e+L{Po}zAHQjMJpcZV!t>$`~29b&2!@;KU@E8r_+4`1)Znuj8wPqvfG@%97b3IFxXcTiakfDm_vV72}kAJ`f<ew3$V)Lsr3tdM%#Yq->OT$!N2{d{KLNP>`>CyuP3t}KYDu7{(U7F;_1MV^Vm?(;-L-<0hn8duF4q+E3c|L=~8$TT5sxLU*UKZ8JA>2c>i8qNLmb~CZ0p(9&3nUGLTe~Ab2*zRzyH@Sw@a37Mca{kfr!_`WYj$!O%I#4V^PE~KAx{t|X^HI0*$xSX#l&|e4f_NhZ66uYP$a<f`5zn$2xbA**-C%Qy@*#2rt?=;(DN0tNJ`4sR+oQGPj$xyottaLg2&=0z1LkA3{n&I>NYP1qX|HfEJ~2^XSGKot6|9;J6nEi=Cp)^G2yQ}S+d2N(}@$663gZqAY_fgG^+s4rW9Helx`p%mHsxj2V=I3<rZzcRU}<_V&&k2qV8aLa?=T?nv)T=(s77ifJrB2Q?kaXP3p=3W#`tEG%zzuKn170x$23oV1WyM@Ux4ZKaEp^YQY9IJ358AN0}hB-qGKEpw0ioZx1tubSUz(Iuz~GIutc?d5aVU_;8<;qR8(hMUm(%{F*4ke|=IE7c3dw(^3>-$v8KLSr!p;`Ox>*EEz&<W9fN;LqdLuC}Sj1M!zP?KpgPZq$mc`MZJn2BfN?k<IK-$;^-PbhA_q-mLlVyUJcAP*T&{FGgoJ3$NTiqXj+2F;?C;t7&iMHvu>)zA2`#R_sC+94{QxWm_*zYQ4NRY`H`$Gkrml0bv{y}GqT*@u@PkTy=dC$;E|N)#Rmz>?%ZNdjsak_Y3cZYcLI@pj>*q_*NCByEIBX`>yAKHVh2#RJy<OzrXxwY^}UH@>5a|I;3*wroQV<rL?#LA^&9S=jU9&4V)(>M06g5q^uRbJAZbJW|33Yq22LL0`Tu9{-F{`;()*xsn`6#dHCI)ws#=$G&hFFgcDvJ#u_JW|;$c7YfOz6565<6R;Y7qlA{Yq=J6H)p0))VgMFar}iSR-s0zB|QBv7IV@gG1OY@CZNizq}q@XGl8e&3jvx~$7Sd!Kze-bcGvuT_^>v&J0r8{hc8-{p?UVj$(?0dXFVf9x&NlQ8ZN=JF^D_A);n?@WG-e2cidCyj_x4a!&LE%)Z>v^PSQl|^@VRN7|yV8<x4JxcnTN*hX%c)(ygOC0vG?lN}|(z=ev&#<*!(YZy4Y4a5dmcs7X$S5NV<H;kfh{}UU37+9HHqf6WJd{suz=;$78qp26$}hg2CB((HJWz&86rlsY;{FgB)8fr7(tQ9bg5dA?*mBixbg4ni5hqB(mV#`$z0@&x;qz>iqTv>saHXCx&;<Q9JZ4)h@j>4AyRc`P-Avq~5p&B%@oo4gh=9GthpLjR?zfQcvAqp%%Gt83e7uv}Gcb?ZLv>{{x5k6tAy=)uu{kp3k;QBX-!-a2Z1=(X{am&dao{h%OVyx-m)TS`C`s(?vSe_CL_~SK>`@y*fjZ)V<~|EkU4Xe@@Sj(W65fEA>-`{!O(74Vzm|8QYvf`Nal8`3Z%f9W&o=*Qx#w?@x0hdTZYG_E!TTEoK=e;neumru-754ABXMNmeN#7TRQuVX?Tl!%&ZansPiV2Q;QI984qGv#unlpO?bbBQy2U<>WL0VZrf_SUFbw0R%9(hKS{CLJ{rzF@|G@{91$ovUbn_1Opu#%2Q+ve}Kb$Oxy*IZ{`GgXId{q`?^IBODD4~b@bXgXpd%Y}3b0Q0pEdA=^dyoaW4Rg5T$0`2eLx1-p;vTX04FHx=4WiCymULg;u&6cBs|}0nn{Z8MSPGF}4fkkeQ4?=nwlLqRVbP7jbi(KQIR-KXwWqKX$(+d7u)3=W`q<=>OLG&vvVtfSF<B7ZKcOw$0<JZaviJs&pnk<>ZW+U$`D(1xvD$iu|6gS}z><t80-cp+gk_pV)tyA==EPJwN=l*>yBULTsC!nH`-z*HX7CLb(|~9)Vk&2MH!q-i`d^}^W8Bni6Ne{DdMfCXMjg>=xK<mwyq+munJ?`ieK|ozs5qxOXqq!rd11BR)uq03^kj?v^}`RN3mblObXX35B907n{*&RSSFWE?gUS1wu7Ch#xn2R!E6^DIf|+7RTIBo+46ccnuRs>G?#U|<&aObLst6Qfb>OW5%5-)3<Js_gu88w1&;ulU@d`x$Tko?-nF&=|&5D%jFDxsRiXpEqQX2dG1J)_?tWFuP)G5QYI^`&0^Z`qifxyAvXQj&j`Nf$9(+b|_FH9@)2@YZdppFqK2ymN-6t;(gVO;K&-QprNUC73bib-U~z?*j5Mu~2>L%D-eL+BdN8V%NKXWOW2-BY1bxh-xD(ZDnpIjd|suI;K==|Bcypr#Fy8q^N8y$a&$u$Yr;Pn0IZ<uG^ZjJXO}0ExHy2^>sA{=yCmfd=<xPD?5d`>7vch5wJr3~IJMf1B~Bqr6l{EvIDDXYbR#eE&6N!~2wlq@)BDE@kh#UM#v8_O+&<r}p#%cj$w~DnUYv9;D{na~nDs?_Fc<7>M>giV2)8$wNd~Bbrc;14lrUI!Z@^7D_zM8`YqAuR~);FOxrz2k=R>{_l-PnElfc9#x(iMd<afsZ@!oaQ}0)sX6<H$G>1hFVk;JK@S*;qZ=6C5dC(*l_soc__I8<qUg97{CK3LMwFcZd64WBHzJC1g+e{Ie5pU>e!gVp_=n2ngNV4O?cwKV-2WfR5Ox%dpic8%aiQGc53zfw{b&eU;m#bKp}m9X-oc7?xM)XJimFPSlbLzk?I-!tKz0Uho;y_0)at!g@#<b%L(@R&2{)0ER%GQ5Rjhl~7hU=iHcMFSS9e&>O5!r;#m*FFP#`^u{)5U(cW-jm!+|Fmoy5}!f5%tLY=Y;?VGq@8DLe>z273F5YYu$x>aV;DQt&tnr!N$39yM9U62r-cY`);{t&Tw0H^Z!#4L#G~VJaV(Q1d|QGIu|n;rX$!p9Ie~%p{s`CQ6yr2qNO`D8Zi>3V<vV?wE?J5I|Uo5dPE7-}LtbKZq$Qmx-23Zr59nxV&X^zUrPrJwNJx=uekPF(jXV0MZb<{pH)!BS2ybiRO<1q6uY^Liy6Aha<B(D$lQv6ru^fzjwC+Z9ziGd<(W+=o5iT^w8L|kyWnIPtl1n@OFf;WJhIyhH7wLE(75U{)}5=g~OhLF$8U-4d#^S4Buz>z+5k=w*98u$sI~ezBgr&^0M#f1slt&(cb6d<!e1MJi?1%>zGmTSy?meNOf0Vge?)k3R(oFk|t~(>W<p8xwXgC?>Pu93koY9B<*a2KuRHjW>>8MS@yG-X8R$mPD>xavg%UrJIM#|!R0XX0o)MYqgpprAONTARpN*N@rNt`iI02p*8}m}QQ!cA%E0aH8&+4z;n-6R0ei4D#n6F=DQhI=LSs&XES0IMKmyN-)`4X_VlO;zfETprGoaOlmTIgesJ0Dz2htK?KUEY+laZ5t02e`mjm?LKj()ZYlgB0q3yrT1Ioc-LYxrW<)*{bjF9?A;5VAmm_s+~lKwgwtnH5<j@YbLjj>43x?aVBhOko3Ptk3YjyNlLE<vZP;S^;7Kyp7u=Nu=05LX>EQrOdWp4PlNPJka(iEsF$iw9H&(%<^mkg<i^ln^ucAB-YH8vqb3V_sOqDbD5;_D_!=?F$Kvi+<c>?P@FflR^|tt2|}+S*o!4j;A<VNPbO1djzEiB`ovZHRk^^@Bu;nyXsKhSI-~hrmd&S<4=0DBxy2q=G1>`9j*ty=MUct7Gp17~otUK5D$(=6IVbNtIp&-h0M#=r2XCsk9oFP_^f8@#ni@w;n9_1e5?iFg_3111O<BmZk7%k>p*5%6sUxYhAG+wPG2;B^=<Zae&urW}U@Cs5EM$M;$&J*s)whk*OvtLumt;xgQhkRu5jIRc+fAcue4xfiKWe?O%XCwvQz(r)+Q*}?n8i)PBitTYBbxhmY{D|-!${Gi<{<k>wOWcqMfxWh;xQC269H*$`<`LzJGwwqMFI7bGKhB#(jQa`HYm%Ktg&3w-EBA~qj4N)MhxoITsGuaKfpk;hckz0zHm@w5<ZQqsjN;zOA#F#UDlLy1*pu%n0KsHuDFRg8*J=d7voJ(z*;c4`FO9~u5LBgTOfi+SyuIn@PY(~^%B$=DHm4&QYP}_g?JFwk7F=zaAeUlZ*b*~-TR)<Rk`R*9rZkpdW1$$*}RX+MQnx<NNp5{#i*AdZH#P(;mMoo>wsbABNW@inr!t!hHH&(AV-BSTXRzcnZ0rXEhV%>8X_;LWUW#=#h@M#Z|{O%-LtE-ftiyu>C2bAXAn+pI1UuSD#w}27X8r=6&Y~NOlC&*^l87025B5Q>o#-D@Zd56a5WfbWRSHM4<6vuC-1vQ);};>Yu@q?RBGqVo=D#>yI-VRhjE_a#kWIw7rC}w?0)$J-r8%-t?28Jj5l?rnEK@~`ONJcc{``q-_G6n?Hm<8FWk|Cp9Rr|w4k%wnZ>nBw=?1S<L%sCx}C+H>AvUw{9?lounPD5U&NByVh}&$W*)ox^t}LDE-FlSPI?F!nFs8y_ohWn$}8~#OdZNqB#Yrlgdfomst9z{H^?KqnVQ++k?sWzy2CW9I^A(4ct^C&cBTR=^7#W^w(=Cv<OpU10+o|Apw1)H?(WEv5qT|IlE4u-8f+oC2}Cr0k)Rd>XG5pG?_sJ$^(tz(Bz@j^FwsOg!XR52%T{sHp);|10DAZlZEWr;JkHE#S&aBI;GO^DZUdbGKq|_Rmu*+xd*KhuNUTSh=kXUSEP<h31~uNX2*Wl`*+iD((5+W+CzO=n*{LL)b@#}^dY5IE7rFZklAcPzoKkl?CXi9xo5a$0LQ6!qRW#k}5=_^WBgdSQZ-j;_gfDk9*GZLerHviKW<c?vlU7K8c&UFxK_(vE9k-Q0`~V0`Jp`8Je+u$x*yNP?^+@b^=59aBjQZ9S&QhiT_bx1q-RR4$h{5)T9SD;Akm8AY9IMF!wQL4Idy%X703E>czv?QED~wuV{tP2e%A)np*rg#HZ3F%M93**Oy{(yfk4RgpbTZVjkJ0r`)(&#DrV}+Ye@SU4YGx8SA?%H1?1D<MXk2!Xl9)x0t!%%|v`uhSMkONS%tmuG^&SmUwNnT|+!S9=(!_kKr?y&R+>BHQYCh6&8EB-5m;{bvqQtO)qFoq0PnWi#Y3|n<7Jk;Xit6POOTUL8!13JJ6i82Nwgz=wO#+@OrP|;S$gKTq7>!5yi;cMxw$HkT+3dXiDB@<2V{hJ`l0+YUEYzy<CI(BN*0D6~tz;<HOWm4{>IuQFuN$3eM-%Yzzxpm}BV`j5w96!m*y=t?XKs&jNmQG&nx6OU8M2S(t5>OXaBO~-t<6vTs4UyPHreGK`;2$Sku@t0@;+b*FN@utp1@N7q`iceb1%>o;^7`*b<NtK8<9XCbY|H{%9^JeQ)B>wwPBfnTHQ3R59@|Av6X~rNLys9jkBAEmKdf{#GaBSK89aH-H0hIHTj5%8dx0dM2?~x>0q!$#Dj9=-Xv;Obw{NRZ6B5`012cLM43@*$~VyY%g)n`h-D+5Ai}1EgJm;SHa$AygzTZGq$XtIiCJ}tfc^3?;MXkKW|J#QV+ATW`m4&;-m9$JMn>!MS>NK;_>WK6=$|39aZR1jBcuXmZD>ZfHns=UAP4!q-%8+p!bYPi`RHKgxU=;fEd|#0QQPg@&>0g++Cq93n)BtC8{4<5bk;MBquI7bm3hMreOLXsvve_esPf8vGL!C<3@yD$q1_2?=BV^UojiOT+S8wbH^qt^PhjZSHEP+s<gJL>DrW)2GMR6row7k^wcv_S^wmjd#{l)kE2XMC=z8URt*T!&4aU7`YpT?136q>Nj=~j3Udp!SC&Z|`rCrcV#Ha=6@apG#wVj0Og;aBcgtr-s|2?M)`}wt{@7Vmpf-LAoV#}}b)n-ph0m<G~R$H9|Z9%FXFRR9#q1bixs@)wUy~$?!$qX+U>dMv#zS66GK#^=HFT|y>Sg<Cn1byiq6T>!Jc3<wmwzaBS8K@hG0Z(0qH19H`aN8RK>*LCw`2Tld2k^e;>|hwRd}Z2JmfVSv^wl}r^%o|rEts*IoJaX)OOy^V{Cx8II(b<+aen;0T1p7#Pv3a7ty)V@s`XVc3!P>rte(zfJlQRYxmvp$TebRLc{hovcm7%HE3%#<*__EF4ly6Aleh}&(Q2kPYZ3=SE3~g4(J~2+1VmP!EZSBo+4X96J7x2-&DxD@YmOB|%L$<SV)x7h5q2MSYR6@7_2pCh4Sb^UZ#lKg;BEG17@n6rZa}#^*EWRUvzUOED*X~NcFz+q1t<pf$Ya%qF4KfISiP&(qp3=vS@9usX^Od7IB`wVJff%knm|@yP$)f$qJiKkiuLBqIP+m!BXemJl9z_t988CS85Z?V&{c=Sxm#yy@i(|p)~F;vEbo{I`fjwHHU2e)?097v0pFJ72n=IG%pKA<044qZy&Ca9hx<3DGvWd)TKI_mOwC1FVv`GKU9V@L|KyiV`RH?t3qBCaKS%uM6U4u_HvJOuU!i$I{Ig?DIiYH)GAcfepnsy+B=6QmJBVO<%Wl4pGa-q=l+D?EzHSQIKZpJwSQYC9yA0J7R5rjf0>I9EL5=8>Ud93Ft8CQV8nk8DrI7zj7;44oS(UU;&;rdo-c=ev`3kozMx|z&;}ZBQ_u1gT_G$j#xL=!kp78<7bShN%TdXl;9@cVdxo_K;zvWfM$}D|i3J<oO)+&Qa=1S|0gHzNRc#SO=tVlz?L{MYH*e1JocCoQ;Qng8)!_c(h5Zz<>r3)pQrePP>S^YvW{v`8AzD3@F_>}z)#fjD0$h3`B5#-*8Z2%=c!WSLZWoUr5wxRFLBa+)6EZ>O~+_D2@Ysmu{&Fm5@9iUI#6~({^E9FDpSiFt=u&%|JlG0K#nDUm~lZX$X;)0XnNTQ>a+a)W5#42eODo#uV5+<`=DQK#@d~Mk(=TVzEwA7Pe8s3I_-Dyv!ViJlIjl?YfhikJSeLkyImC&|}euwH*!|RWLzUCB2)Btn5TiK><gUo7pk71Bd94bfHf~XFcqB1Ww9V&2`7hBaY$Em?gBs#kdh)Gb~6jeMp^Uk2|V|c?31EvWrh!SfettcYK>8Lpnd;VQ?jbW=eUrg<nc}>T;Bkv!evlWBDfE}RbgIMPE7Hiqcb3GFG=Wn-sW5kBxmPYc#OH42G%0F5112h!igDB}6<^VXQfer7HiZ<o`Ya`))<kOaT+R&|ziLi0E8}3D%iBVe(h<g1Zo(Fw3$K$jd92pwLC=rmdaF-(<qo}26J&;hsvy#+l_jlegKYBLxZ?0}v-)G)$Rj-=y$C~apP}r?~o0)}%rTYu-B&PV5-?y{;el$+<=GspDOEVfLvGnXG<90tLR%V=J#_jQSxjx}P0p?vLe@GT=RdK~<$TCSTlGXKAm^Z?H0@OE&AgP(X{s}&j<%2uPC$U10s{D^dHlP00h2`yy0~p|i^(g|zF4w1M6Ri?eREdi8jaYw<m+?!LsK^1N6EQn~xRt`^eCl)2Kcj3IoUBpk07SU&vNF|m2nWy_9BMYy((846Wyi-;)u$v)Uxf$gDJS%B1B5E58E~W!2EAr*=SrGA7|SBi9yW$rWnr96dy5xX{(kd=1cH~=tzH%j8i2hn)U9r2CTbVzR>ss>l&+#_7)^nI;)g9a$E~*e&547Wk7Bh?HrHCb0%1Zrhp1T4ilWNRw-(O!iqrLpciLFVGPCPkEz>xjy1`a#B1GmL0L7f`=F8=nxn7&)bxSzhA+d<>RE=6%UO(w~9Y3z$^`CyJBElV#mzLrOT{Pd+_K|)q@&UAda~$?qNx64WjX4en2~{|0!<F1^EyvV`_CRdgt<4s7EFqb~0Xp`#;TR}&$Pc}_g}zombVX}%xC!@(JTbm_2lQAtU?90I3UPH4{?Ho1ADRt8@1j-X4Lro84^-a0xf?$nf5L2~fylU$;K!h@KA*j{V3C{|21f(YTK9Uxx^=vb1Xp9e#FJ6~_n!+2ql?yagfvZ{9gBh8Qer!f`gieMG7CamYxZISq2ImuAZ#sH`dOktVz6?FnKChSM{b>iTKS5x-a2@ASJP2bo4}tzO7pdM&N?*j=aD2xo2It9!P&jd<T$M+?fJ%YN0=z6-Pt~sja0sPD?hn%(b!zP4ToS5Q3+><8*4~u#8w_&v<pj}RN)%ck*Q3j^bymzue;^Yu;p-)!zKD(rmLab(!_S@eA$@urLWn$Lif4(rRn&vs9`wQF@U$11NfQwWfZu9$y~IU88~iA#Z{dh6v;u}nB{P?S&Q@pNwyc5r*Z3eL2i9PB)plFFa5_(<NPm-cDTsxw{W<`*SKT5FUSs;LMYITNI;2EV6Y`w=kY<JXz;d8+py~7B2QdNnbceLhQ-r0TgdWCn4mOvSj5RY2H2p2D}Me&`ExI&A)^^V+wk5j>dPl?MHNFCi^q?ZJa%WRMo&ORFCavD&06TrlHI|12SvGi9A_i)BTH&tZrJqHja9Zo&#p2PT<oeT?XG?nm+frKR8pgU9P&0w3SPMR$(QSD`EGINQyaV9{PKF1#N#4kOX<pO&)e9z-mUe98ndwCEv<-PJ(^0%;6$hyTNtIY##_C)v|Ur8R)(c*1Rj#hA<;^VZSX5kqp>XyIOb~I^4@l{jIHCn%8V`iIA(0zV)(!L?$Z-s&KFNl0RUy#(QtZ}`@D(yBE7w1FJ^9^&_jYjf`@6AS$H!`z+77_PxO7KEzvYXW2Ftt`zrV<ginM~Yg5&bfS9UjIZxR!RyVSliR;ehX$2}sFys~Ul;5lRoU_D=QUoP%(V}iOk}N-g!Y`PY6%mL`Ea$x*%Lmo}95wq<v+KgrBM{Pj^=ZBdMTGy%rsU7L;pllEK9$r41<Dd?Z!YwG;H~Rr6<YGtWuTn-jiMTRo+zc*?7UHrtL6njRs#y9c`a{j%a6QO6AaJRd0$C7HDXdsjQOriz-#})&mv}1W)|w-CFR|yW=%p<bp}Va64N5zH55JLW~1IYok`P5QZ$u5z2Z#a>2=-2zB7UEsr}5V{T8vWQC>5c3CJxBVp(>(0W3)>SL=q}vE^DYXG5i%H%(q<z>q-r+aF{dM6CJn^^1PuY`vs}L9BvHixP&Pgf^V27#9!=W2}ji@P@jpt%+i2rCF@WZt4@aZj3e0l`!Jf`bAs4WRucdkRBE*V>+*5oUDo2b>YW<P5eLp(M;JIE??~|W#fWaQ??3b@2;k7aa;;XYeZ42u{v9<bvB!}(Hz9nG)XD{@D7O^>VDRH+E}Rdc~)Bs7xOjM32Kq;P*b*bnVYTc8N+g7&XngtYvaVUS=oNvS^3)^1pdW-@DuQ_SECkJObIX44;VDl3+o4%j1owmmPJlUYRk`6h-_A-v4kL>gk=dqia&z(X;#K1<ZJ5wT$-5uMX*-_3v1noufSPj6#}bDXd`602U5yQ$m6(_t0`DDTnC(axpH?)6jxt?4dG>pTlY;!+<tkIM0kLxQ@5q7Iolnk*<5~>(|D8a9)Tzw_C%uuZpjYZUT62y16sdFAJ-4=^F}MLNYCL7#N@&rrM5WiIj&7yaqM^4fx1xDVD6g8hBP{d2m%>Eh;Mf?Z-hf@`E<%^$JMP<y++y7L7ylWEwa$60hU_YaVLqGPQV64YI8`8wUwuT!ENhPB0%k|X&tgrz(xDF)+mxVee@9NqZ>^gL!YZIQD@C;eS~I;ClGD*&$|E6H%Gty!?^8B*18+&c*n}c`#C>I?dp-du1DA3mK+)dkzGmi9^JkilvwLGcX*{(B6#Y~tx3Qt-|)MTIKjV1B2xza#I8-k3%nGL*0E87O44rzPNhSkCuL&DQP8=^Vei=+N+h7&dxNy??r;M%JjrsZ-`P{a60RjENR?29WPR^IU;8B^!u2tI8&IJ^+_ofe7fg!?m*TzlUE`QRSB7nOgdQp1MD!X55%u;X`^zM)ZBw{sc`CX)Bdw>wB=EtLOvYQ$I1xj2XWTFum<^SvhFkn7ZU}^evtVQQ&^axK{f^Xbj;69O@KaJX`X#b6raP~i$Rj`TzMR0F%C3~FVVzr&eSysSOl6I7!0#TdpVA3IdnoBT*j?~Zh3XHJR9HCqo}8Z5k-N<Z^IVywWAy&^hXT>R*K+nnRKnDTJclG)s%1;C`3#KkR24gsKQdo}qE)d?jl4D>pQ&QM6m>i=Vf&iQ%Q3Wq5$HXjDz-l@WFv=~?e=DsE&|acnP^q)f!4b!WN%+k$o}}ErGNEZl$-Xz6<?U18!wJof6-NjHJVMLZYd{G@2;yg-b$x&vW1$NiGcwv@g~5>M*XH0A;;13cBnzaavH}pa7=kw!ZO&#GYKbpIRfZO|M;$5N;nB@8VsACsKK|8a}H9BSPD7K;hRx@m3Ud|D{!;N+i(sWc0fqm(%gwBb4Pb#1T2lXGWb1pA9v#XYZsQ4F96r7YYNW=TvyE|EhRDSVrXnZ3G7X%W{G723k?GP-WlPQoNA-k+ESt+yl2-#`)XbMqZUBRRNruo=<XzDiEPG1i5_sky;BcD?T@l)i19vDqXl+h)P26kta+4G#6gL)X`TTey4S=ET%kbo4%H|C6a9_`WfjLKOcYhf$l19sudlUL2|hgXGVWNXBtyIVv+qqySVVLp6!V#L8x|Vbwh?_CpOh2M3pwHHH`<9^;*<ym@&{L1jkjDZs+v-2C@?83_Au$$4$e@!u|HK5-b&Awm=8c+dQ+pmCMvumZ`G*doDS$d_gGxktCBj7-nkSB9D7{sR<FyQwwttVfs8n~1AV5_Uw@Z4`K-9}#W;z<8Kv|Qsh(1`-7-$bD{-=`aWc)~B!z^_kwx6JIGL!vHG<;-i=R1k&*LOi=LLwbp50N}wpeB*2`pAy6K6i%g94_xol?q(S1ek<^i#m30`UlWXP*Fm?3rXN9UMG4_{6<i`}m{p1O5N@wa%t;DZr0;&4dbM>Q;{V3Mr7=p3W)B8#pFj)3nOoTp2^0&n&Z<LY(y{mW+$Z6==Pf&*ql|>4~lPtR36@N{j-lU=5;`$tNP%wwz+Yrr0#Ux^aGSPvV1^+*a)Y?YW&*8%ivzr3Sw&HFVcerXM-0`;~?CVprx42oeUAm-^yOc`7|TruDsF(KQicb%$No&whrRcH4!Uva4Um)VgocJMa6!yt&I_J~W{O@DdpZuGrsi8E?0S>c!T3Z~XoQJwx2mFdI9F5epRSz6{r15L1+zzEj?KFK>3gW|Kw0blR<<Z!-w_Rpt5OsKg*`iSk5CZmZ<noc~e?`;FFZRWRs$A%W~sm<>|IX2uR>ZPL*bsWY9Iu#S@id8(TiWE_CTtD9sp1iq?)V?O@EdjOqz3G(=OyX?$q-4@eR#qc;S+R+y6+KStf>}b8<QQ<tuxT#B3+k9)~?kxA6P}N+tL<9bhi+n?_6dWs7^iJ;#ji;7wHiaK}*!HrbdO*Ph061y;9E}rYHlMJrpCiS1mD+F%VIN?`${kg%%l=QkHvr#_!pPZJLV)p|#*z}Ubu8xti9~8${l-&8^`&TnQ*n%YRPe`GmP<j}PaFxi6{1;&nS;s^?Qj}<mLOWHC6SzA<C;##wM@`hrIO0)>xlk@`#-;u!O97%^s--&F-+qb!_<oAfecM)6pn+Qk!m$8z%14zUpc2uv`Ry{3{7pF4925q-LinL^@$zDWJ+KZl$rPpqy<{JFv@6Fc$_ZG*c8dC7vw0S;bQWhBnLJWLZM)~t94J7&U5{gDiCq4Vjc|J5c923RvS=OX&<DjhN@-c>XX45)~vRYtO^F}tSn&wEXismAskk<H$>AZ5?bX}>%{%bD=Wtzz6s9nzx~zBf4(~0X4zeQIou{f!q5;mC3LhZwJ)b6-7LKU?O}XAb{Zvfs^nL}eLsWw3OFs1cf;U}t?{&MJet|P&&>rge>YCj3D<A*qVuMBvxJ38lSo<CefgAqEu~e{#+5fTXl#^sVZyGg@kpEVE&3J*LJemC9Fr<*&-*x<q$5Xlb&kRLc=PmMcmD|p&5dM&zF<|e{M(#aULRl%2VVeepM}l$(SCZ>+K0!uPB4oJ$t2xaDJ{QH?>N+-yKs!mP^3ghenypv0z|X3RvQ%h%8Py?(Z%WzzO%geL!DNVm_YOx43)E?cwa}b_an`#;Xc9xevYi)I^r}#g)HTfq)||E9-^cGStEhaWbQ~rb%;>n5a&Z2O;ZxTX{H0Vd_l`38M@f5Z6mMDF#LlL5)OLkV@7S0#}$fz{6#p(H5OQzW)==|RHh^s<Iq*40X2cAaL`na-xv#Ys2UE$#{<^ZnL3=-#C$0ttR?J0X>(y@#&wG28;b>_?@XW!M)@+Cdd(`gClcnzUT<eut6-@!E91#O7Zemdmz2Mxj&Cbzy(v0)S)mD*5ZwYsnrZ0G^{9-tuX0J_isl8M5nv)KcKDV>q;+eOS9jGTET41#(BvF9W*>Q1<|n7d55Brxn$D&#_OclbQ<Jk9ee?Pm9YLG7&T)(*l+FZ~0&<*Dt%m)$I<=ciQ#+6FuR67xk<H3^JzweKe3=WrSs)n}lR8~k=_-$PoYc!1Elp<+bMa|Lvyw}4o6TtURs9)4x-YvNIVoAwD71!TIMlh^Jvo=ff%y2-`CnWtf{$DQ%W8jfwg?_eTAv;dW5(pcDk$^%NF&}`yUyvT?mvDhU;A6;r%M?%QY%oh+<L8d;x}16KB6V_r4;1gq!StwJ7k4E5Gxw7oMmd(<vU`USvOwMk<AmaB7dxg3mggpsGMQTmP>qpuugTEJeliqE0u!-<4zLGB?cHhkR+d2H{L*Sc&)BQZ40Am_~iX>vcP8{AmjeOy!kS)XZifPu65BI)0pP&ys*4fZ1JR^UCVUQUt=Kf=0Vk?e7=M(X%F1dn9iL-mv)9Nk3sg(zV3>n>>;rJub?(FE@#U<my4U(wyPzSt~*I*>3Em?{0=|CDqY`mg}ADB_&w!?bDVXC)o=Dv`+&?5>V)I|OZRqGortkdSWaIBs3Jk;k`mei5IlOZh9|r%XVt@R#Et!h|B)n`$gq!o?c<Qb&>-l=DEg9L5h5^jSg?*E{gEyXktE%a2HJkD8A?k=w{CGemhF3)J2w%y@u5irtF)@&lsn+3#$pavE0w;X<k7mcLwW_VU#di!S6+j)LzUsTG<VTFM6)1<w^%~h=VN=H^<+q)47g1oLGc!RTYQn0`Se??CGZsn+zJi<(C9AYT*!uFNjy}vqmgsEYRiflr7oKZz#D=LMi4bt0r$;Yb}dAhV(O0@2zO!m3N7M}@*^7A`(tERB(MerQ4HKY8*JYNwn?O4LMBEU8<|Q(-%VDFgrk(aWLajHaKaW^D){9Mbu%T_Brg41-U*rNNr22Jz-&5l0)CEIsvJocCCGmbbedoj>Fp{&dO%h8NX}P+?(+|$p%YC4#JfMhdb?-*zzH|$hxkbM1@|G5jl-rIPmqa*Pb%mCgWzsZlfZqWtDuGNK-rod8siLW-U+uw@ldSJZ((g8-$o~;rm`BnHC3y!-87U&z^pgJo^HCO;`{UFUjF$HE&6Zh_wrhw?#%4(l|J2Z>C>GlB>Os_?pa@mxz989+z>g2<TfR0tG`yR_T2HhJ-3Xlhlm$kbT!`B@<ytHV`l<gw!_8dG}_vb<5h?5FgkRvkt7V{4qY?p4l?PEReH1Tm!5X(&U)jh)KxNpRDHS~^2+yR)tx?;;ql-9@vYV+|JC?$M2($L<kAU6PB?6CUDhK4E}bH<LxsOde*@wI7qD+v$tx$hO?!>L9qRty*d%^b!9HPd2WiNvc$YZw*~Bv&2x?16b39OcEX{hQZ8YcZyC<@po)RzLoOWsX(Ek9wo*SRPLj`+S6IR*t9lkeb9J{B!Zfw>BnzoT8zbd;yzc9Ldxwz$Sfh4bRFb`h+Zu%7&*}4!D>Y;@#uN6Sd*g}9aoqdVLC23)}6qecmw<xQw38s<06Nzl;zGPyS34mQrlOYNVdJ|$ILK>bj?2wRyhWkcH>l+t7lT8e)IUuK>crq)h{7?V_xXaW?0|a7CCjGGUc2h{S%+3Mlv#vN>tm=sd1rp<LxHT@XL|Y0GTyQD$nh&<cUMEKn1eBfp%7?0#*#0^9Yo4dF&}omDj0Wl6hjjGjc(*CnEn_TTSwOrKp~}YoLuUENYQZBLLgko8HJ$yQ*aw6XE=jq?NUSK=+^Y<GD5)`xIa!I_n64yV(-FD6f|RNUY>8&MkXoQcbEYz&oO~pQDi}=1f6_Kjx^e-8#UYqA09~BD?X5DsgJg$_t+y<90g+h4cn)8fNLylbTP6v~tHu`A{BtE~KrdM*Cc!fKFu8xYZZKzTm|Gw_9(>uKrKyI@xcT?q+d^=b*Nn@-GyTMDRye22!8yjI_7kmU%fxkLOtZF)3Kt{$$%-KJ=8+>dO0!Ke%qL{A6%TTuXESfuh%Ck;?dT^u5*b%Ba(`Zsrl0HCENNoBJW=4*fNLguhQ=-Ui>ntf#csqDgUr7xd%{g?28Aaq#zphy5|QyEQ^tI3e(!@MFAd~=7QKacPF`4(=vNn#mz!Dg;#C?wYc+arDNG=yG|yX&b+(SV%xcVKWTbeO$TTO3jM@uOf5ho&FL5$+yHg3V<(xI&plc*DLK>txL$JP?phufTRl^2f0V1k_yniHOOj~BnggmwpBEeuSpcH5$B!gY&wRIA<PjnJsfAdX(5S9=9zdu~e%@<n=6)&@q@N-)M9A~q5t(fc0ifpLBXXWDErLfzLK;qGY@-!U>#$2{3RT{H)u*bQ~$U7{F<lU9Xi-n=G$h(QDOH_wwv~koM1Iw$@bf0OPpUmaK2$61)jz=&JYCpk`_X?)-jJP|7<CV6P+qozn#&D$;dKR7B0&#vi5JwpCE@Sb9DBOKrQ8@imew@XDb&=qP2WCU@#WVWORE4`1@)J{qyyc``Edz9P`+mlwYB(Q_N~L(`w%%;0z^T$S_ipdhIUB9VXUr-~-0IdpRic#~$|+pe(O+*BodJHBB$9f?M4#0Q=qOZKSXmYk^JvaYs>hglpYlE#BjG0V+<{g*pfS+XJ<ITf7Vb+vwPb6RiN<ubGi_;si%@yo@n7VOBjU0)mxYCt^_8rrlknt{c9ab*zW$oECEibHwwNAAr51a4b~7z_UBbZ4s9hWrRz)2NX~xZ-Sxm?oseCSh%Ry`--E;=85_)2kphY?#DoNkG!RT%5ygWIYD)vCX=9n1*6RD^yUsYr?KRu`cg}kxui-E%?=2X-NNe5WGd~T<l@J0bZWM-;Llf)AjU@bj?3wpj3;ciRsTL<F&&%{5w^5^fq`^xlnX)<3H^J}Sx>v%g~CgZ!t+^fyr+NTMi;g`-Uqom(OR{mjjC#e>cbPeSz-Yh7QOy_8vcQK&~)?c`W-CFd!Zd|UGYGgu6vyRfx>G?WPccl)rofU!l%J6G26R+n~G!F_<i_kZKo?kxn&%T(}hH3k~&k+t*N8eS_7@AC<p(`S?+De9-3H65VU^;(6o{<*aXz^Lzb+3&=_3I4mJ|3oyrX^`83t<bM@7&-mZ>`K}KuFEsGtM8!?|YHJ?!=k46QFDlP5DTt?k0{MmyL4HpOG!ab8e1=Y%v(&B=5~GBP;r_CvMkDH4QZMQSnkh54S=Bv9uFy#PG<2JuV-Nj!ZksKF99Qyf+RUOb#i<Dh^zjIhvGoHFG^^y*P(YbKtm5N9~RrI7VZZ3xb(6i)JNxKf2Ym)^9U!+={|G;lQ=mIdH0xf(ExT0$d&ma089RC-xf$9=BH@FoC_GdqBX=7linKH7f+XZ<eGtyZ7#x?UZBwyYOrMX*lVjrDy`t{PY&3xjxXBm0|;dv3<4jP3s%D<N9(JH5}=DSGI_3CiZg7qvn9NwBBsJqr6+2#HKS85q7vjYQ;qJJ;2lt<gxHB%C6g51qym%e3!uUejxWx^dI^RD2DKMvV(*7gS}xSYcbLxgGE%w#x_%X<N#FW<$gLzy9y%d51#tRWny6c5bX%d#9qp2RF%>_S#gjz+EOs?LRE9iB5*>74`@ozDar{rDg4sgH0C2e*UP>SGgn`#+p)<lDV5)JKbq_@o^f-%j|12k@J4A5RaT$hc!v_8Yj%3j?0N^xbWY-`$WiW%H49-$Zm7XXdexkhDV@CIxH<_|k<4&6sUyjXHFBg)sDdP52s-IpHdO{BRi9OPNMw40kz}2ehN_uiC&r&E^#1?{+6C={OnAggY^J_g8UmSgg5-?oCegrHKRw#(F?WV&-lTRM^Pn7m`fT2)7|F;hFAZEDWMHf^t{shSd48e^)y$sdH)>F7mC=ko)YtQ$xy4R@)?eVtu2)V!#}}`h{4}8{Zg078<ms1CkJ-(>`{{?uT!8U@Xq{HaBwtk~L%S0E{|oo)ei#8_9*)o0Qdxf+<@sTZ=RL~vVDGTvp9DaGlnrcO5X>K(c`MpKO4+WFtdtN0N=Og*lwd_7F=137zpF}IF#jY09O)laQpQ%74qa@jxH0kRny@e5zH@9chn6}ZG?k7_><In>U640)xuY{yjh6nw<yrc55)r`zCS_G&G_?(*xB-sZfMZ2-A~!xIf0|_97buK|dyoVkv`a0gmFCxYG?c_CDM+K6lKRmE&tP=e<;buyGN{nmSZ>v^8rF!hCl_e~H~DX^0tR<L-g;Eb0%QJ_xj7G1jV_q;U{3&lo;J2`WF;G6SwSQp1w#{KZ}MmiI*j^;UKi!~C9#xE(O^CnP`svHcEpB&Zbr-}5|`a=NpT0X#t0J&J@1Fi(`l%D-EgbT21od;bIoA4ac5H*vAfB50aazfw+EzA@Uh4SUNvI56W~8~$Zx_M*jZQsi-^!<!+?e{lDV$KTo7)c!FCcG<sNp`^#qU*#cs{hLmLM7L8l&76IX3np8;y57>Uapi(LKR````u_EhVB>bOAe{!$Gaf|s@9Vv2h>)MCFC$4(5tItzwpL>ZCTd}vR5@VRceZv2!{O>Tm$?~Wapu?N4Inl9Cjh9J^Rk$l6)H<LVHTXU}kKK@GUB`>#Jac+a*YZ-fGHSE4h)*54m_=Cv0fJ)Z_4tFvpyfs&+$neotrTutwihw_@AP_Axr@n`8Lf!f=O->k}F%*Aco%KhtlN$$gU|SQJ&h>8?=h^Kn1Gz8ztqnFSTab(0p4s(q;QpUTQ54p;XilvXQVeXQZk=jzOpmQ)n%3kacmt`H7YO@~&3~=B>{$Hic==HfV?ZtcHX{BJ8%LgnqZ9}x<G@3$i6d$VrxTKB9n7tqk}{z6^$pgAKGr%FaDJE|=sz-{?5SNMd90YMy4XakPg8BG#0-fo!L_#wW&kheGJ&%;Uh5X!;h^e<8j-w&YdwmH+<-~i1Clv@sEM$^)y;N?-h|*K9mw>tGlGYPh%`(K7%JA$8u>4jYu+@z`2mtYti}(J$HH3L*fO!72douQ;~A1-2BL6?Vt^&Eve0F>Zm<Q5y&)?~G8Z<H4Jn{9uvV@82-V85CN6qq`HZ!*)tLGGP_p!$B|TrTZR^K>IrPDvT9;SOpJL`35zIYb1JK2gSd=d(4DvbO0_>^^?)rs4JL~s$_2A_+Hb4Xjo)Lv6rQHZMiU*@bseIH?mx~r#ku@CY$x?4aC)Pk}h@d+O4s%!%6D7Df+l%e%tfDvz#2(pG{rDYKyv!tPlmq^EPcAxVD^4~9BR2K7Ty75BeEF%W$KnQbotFC3ex=aV)xsXpQ7Y^a)E9}g5Uv)DQ(wFL*p>E@3yE^8SA{QCz!ukP&s|2<I-?LZTcezDWzDY?qY>>;wa%&(EHJ!YsR4HK=)tH?9n(dvGj=k|K~A+_E7D6lEKfTSda~eFPYnK8{)TF&=DlPg=Y?z?SyEP7n6SNHDLE?X!;*&5FrN=NzSZrxBw+4FTSv<Imz(5f?O+F*lyS(m1O_f~CSOeuOYDAeAv;mFv`5NnNN^&-$_!H@6U4d&4*33&6U2xhthe7He0@oH2JYek6}Uqm4!wO@R_tR5dV{pNQ}}k!aHxQSN%tteTQrFXL^l*t!av4Fo;Qkgye%Vov^4vX*WsWG)k62;(Nos4T&Jx_lWMr6;m(tq4L)^4or`j`9fYNbtiZh;`~l0m#2)<)K>03Mli~<WP0(GIHdcncQL*42)t(!>o(Z}ggID;A)ia~})#vX$qmRt)y-^ZjN49;uE-XO{z&u(&&t(wsg`x^6?N%jRlSh#LOjA`6IHbIRrHZgd>SN7XzLI+<$s-sFqFE^i*73`gfyjtNl*_8yGlOC6C3dZE6Y8_&Bi6E%;xZUkA_zJ5bYqf7T`M1exb|^Nq)Qr6Ep0e71mhlLASh*qvS=V1mPd3_d5>zeW?9rKf=s2!uYMh>T*C5F_&0qGda=53*Xz);78!d6)iI;yb-0n$?9S}Z<+`0&^_SPGE&|sCZvbg-iMuryqEu4lxb?K(Zn<*-{ET$8YQ1Id$1Q?ci4WyclxL5l?r+BAX4EC*R2*ls-!0cIwCh-I;I%YIsSI+LkZ09P5!L8IlX8c`Wi&%DC|%e^AgZzZbKk%#kbsT5as{@RhF|vsDJ5vmju(Mx<}Q%^n61`P!chVhYq}G<awn|ODjGGHVW-BiZ_KJmz8EoB-*9nPtWb+u+!A+^)FFK-?@JmvT@WBXSSUWG3l{{B{IRciK@tn9I$2zndl<lV^zTg_-2!S*Dhp5A*rj0EE0&DW!ckMkI~wXqQ3wv%%>C6oPnvv@_QM#?4q|n*C2YjvL%>l?!?M@X-m;-c(2CQ#r+8dsSG<nprd;`6@+3BvgU;N8jwopBnmD3v&ruAM$W3`=_e&o!t~1mzsMmR%pNr^e7SWlLj#F8JHw@>@h#0xcEoOPqq<Pbhf;T5o1+zRNq||uA+#|Q7<PnmrA>Wp87i$2~s1J3#%V3AP9o|t?h-Z>8WfjF^_bvCQ%*N}Uci6ofzK9)EjtPG$xydc+>AmuHE>&Q1-uXRuLXR$tz@yCd8GK=v_FIbZ@`QTsw^8hDkWE4|$l1$=dsNhp=H3N>(FS`Hq`lU{(kt&>S98!zj5j1AvlZYoZg*`xxYd)2Ok;=-(O2>YQqPPE^e+s)$B6+Z70ge97xlp!keTw8J+eLPr(nX}`JtLmFfFrUY9KIb!*5jPQ>xyyfY1NsYn5N_!|R5Bto%OOrm;k>6*b<%txGEV?tzz#VOI9tsvKzMkOIV%L?Ba1u3YK8ubZb>{dPCnX0z`kcDR!8a@ZS`MRN{)wZts9;hH2fPx>&Shf<#P>XUY?2Laxu?M6Vl7ObL*zd<P`o2^+{#-2n{<o=mbYTyV5xh%7sXg1*HS5F{`RBMgY7~w(BIn4r=m3>t~mb-nQv@HVeKz%XQm|B)@1%E-~s5jS>XzMbcWmhvL`}9bG43R16(H`rG2{?edu&1(Ms=NJ6KwTL90~0mnN~r#0FS0%@!R!yB{L($}+Gd}()`jG)QUR}oV#E!KCq3Xv#>URcb|)+Ks6nPjoPG4Th15r48XxnWDUJw{)tO(h8q|n?Z@9c>3h#cG%HU`{)xNaQf}d-Lw|CkVNmVxA<A!<E+cnMaaP<c6Sx}qY87fIPvv#+T3fkIDj+gC)i)AgVe9B)c3&Wh}fDnJ=rV4hkscf;1pgLfU>RXmjbR)sOlXI@zJX=iJvg|jta9Qqd5c9a<=dPP|YB*>JVZs78_E>@nhdwiWBL~6IHUpMpWCR<-t8^{y69iVFe}n8xv5(z!5LArpiIr%+A{)i8)PZB6ynJHMD8mYWxsRF#g|~(%&qTL*)i)CP64Z_m<qzXb-W7?i(*BDeX^_@Pfo?t(gJI=Dwauf}DH}};D<sHJK0qP@QZV6eKN<7XioBSylIRVRIFw8^cDj<Lj4YC|Qh=@o?=QEClDzRz)DG5>g>ln%9foPOvK)R<$$;r95DkfbSiS6fUiMAB>{*u`-n^;YGtm1~ki2Du-?K(EmaK_H4ZC{5*NzuWgiXv@Eb-pNLdqqD%<tebIFjXps5>3(zn-NDLI3$wnPTNq?~H~Sx)n)rF|4|<xp5`C-ErPGJtF78X|f|K0%bg+vo_L}e+UENn^Yp;jPp8dXa~ZM5~thR>Jgb{Qk#;NNEuw!(sB{l38eo?=&Y&6hDv$;k6LGoU*!JUcy{*7$>X2?e78S8jpv8{^V0}_8sSeP{OQk6Bm6FZhWGMkc=dbpYo5&?;+((opI=k{@M)HQpg+Uuv-$mfQ2sQquX%5J^3PYj_xI1h2LF}*4DadB{Ng`lV&rFk&d*AJj?em6{JHquzv%ary&bC6FE9D&>bovJc=6fmKf~ppDf^0yHi)!03m3vAM)L<h{a)Y8YIU?C?8!f)_3>ZI=4MGjYF{z2R+%A{f}ILM8(1TYU^ElY)Rqxz$j?ndpDf;&udi>-DI}6~;<Ay|*(<VN%m|F%A`*-n1$H&~yuEDx&)7d<EYN%7=(LL$SCyIB8?XPV4|3u32(#Z=ap{*w@UuUoKRy3&>HNJP*-PW^80{@F?{*1PjCOJM=Qyx(*f=>ovyGS!>3jt0i8;$#OtML*dVZeMkqx_E70$e!t-*zE)5+;+0!&{aoPGtJ`PtQ}D61=jZ<FDPt2v$|8@$4MT5a)GK+D$pCBf9mS&Xya2_%=Bw;TVopTVBu=}nK+Kg0P`^PetUf9m92-Q|}(e>6Wk!`YdSe};bXjok8OPk-Y1&rr`HTsj$>VAs!oe0KR=!udD4c(!5rr$N0=UeL|{TwYWCbF<&=tQt3e+)(m7ntt)Kw*>Fb4>C@tr-oXml-&62c#Xza(l<`O2OF;QIeGoy;@mv_#t>e2Oxrb&M{aC(jbGU%<N8da5ibwUIB2fEz0z*HyZAHAf7;@Lrxr-+|9(Nc=%}B$nRs7e&ifjm=7ior1PLNTof$ICVk_kv^V$Xkj&y_j<oXm=YruL|LhzKQx5kFgiLh%i5!k{XNHKcc!4atCRQbu|D}yTtXt8oeF03kdVc&`Rg`PpMTNy9I&~DXOVE_h9g5=dk%nLN{C5ND1t0y5$F=^!uVT~74vdD|vAMni|*d$gD$hWoG3S&|(Cg@&K(>0h9R;-fwqBFI|jHPbgAR9YE`M4$vV{IQsn1Xr@F`MRrQi~`$R<KVu&3|TR4H;;>)Y1>2u@I$u62EfFhK0hnSRv7%S{i|nGN2+4bn_>`2lRDn+zAlJMPSAU9Ae5XGgMk{$3Ep1F`8T?yMsAZCkT+nc!y+mNN(5}Dgh9@Bj!TpojtU~6(w|1fl2Ck<pFbqrj7)I8-Z!%0!_wjG}{2+YjU#jTT=|YBYBzh4eEjKFcQPyG659#`jjKPnrOAT79N*Qmk3Ysgv<1Xdg@A!a8yUZyQ1~n)DUmX0<skX`QVkZ<HUZ~l^2bY-Mgw!@+vduVX4=>AlaDV+_}mQ&|gyO9&M7Iku@`Eynb~_rdw83*JQeZYGOMxUXtk!Gev{BOgCdwTZuKz+|kOBUr?3GWISP-I->x{TuR5+VR@OLj%j@~XU5J>*O~WgfP{<C4^o-EYVSPPI`iR9$N^uK`laK&o2j&(NVHB0-jsu+kio}S@cwJ>$AJ96`Di-AueJ6PQ)`;AfWpjm_(C=Hf<TUDYZN-aI(jW7IOsm-iIkLgk~w-28?X@yi}%)o2{umHhHBU$+(`WI4wMZ~rdcOI@0Jq{Mw!^O-G!^hT-z!+bIq8GJgf3$7l8Yt<dqk$To}Fe%#~}j<SOTU=;X@vu`Rj&*B=Wn`^#!Bqn-U#HJ4L6`-Xgw=oXIlqmIj|sr?xE1S&~%9GwaKHYV)L%@VO>anwJ$?rR^GQZDUFeC>tYV?dMH8;SC#!oC*r97x?1ou~T3WnX(z4&R@{E+r#L40ARb`CoDWl^_1FdwldAL9F?65{4e37>i5v7)!#^^L(g=LYUT(P)pp^Q0^N9xV)#RfN)&=a|q`1-S&ivIX@Pq%WIl7QZA|f>2Cj$kkv@2V_$MvddjBG;*MVPhFHuwurlrHn$^hd#-1vPW}ET3WCEKs4+I?U%}17M0r>fagN_TuA}!(SgdDp!RA{KLTv1EcB;jwlpCXJ=XM(Tu@4SnrFx4ZQH~h&^?**4!xvrJJsgbhq<!I-yCW$a=PbAxK#(6nI1jc#DGqfcb(nG<R6s#jrF^fhCa!+BvAKZpK=ykN%F49>{N+3-PTYy+E$>I*mSQ2PhOGQG}nkdIvOm>psf!769-Epxn&J_TIS-xY;8U`AzWwJaQuVtJp#vNT@$o|N;uw?6DkY*=vGZ6F~fXX7ATiYo5^zGb=6TcO!;4j*hDc|DzPeZ$F*t}t)dmb|(egFzwcge|p(?|w)88eCWUd@e6dw9N+$*Biv!R4dYTN9j5rdg3qC{!66G-^X1s9HQmDg&dYDtVL#U$Nh~)HezUJg1mzh=boLj!B9sbf$Z1!X*`?`CudJG^u%hjqo11FKDZioe}wOC}PVkwQPKGqCGZKM<HDK0;xFqN(^5y6Gh0)L|#(cijZ33-bstYCpORrG=3}d!EENz?92Y%kHy-EA-uFUdN*2mJ+nMUL(hsXDGs{v@555^jGJgLji^a<^U`XG6??f_%3Wb}rkl12*JSXYRz176R5n$2bGB46nOiKCebqjTV&rqF%xNinmZZcvEs~vtYFIXZcAacLIv4++cmKK1t<PG7wTgZVX@AcZxO>DB#|YxH>4?>J_<^d2>}YA>?a1TAVw<N&9v^MXRsO%d!F*3ugP^+!-5R6yS^53mt%5P2y94Kule#v3`J8%GE7nX_AU=mON|Pcc9-%0jO5l7DA^n~?T%|TJ+b^-jw9kekxaYwdbg_8^%DX*!Rnz0&e;2QoQB_0ykJ(*4+dMG>pZK#R^#d%7XV$K&QHvxp7hWwm!mEs0F1WOq7dV5Uw4%`<>DU|WWavlbvV~U*dlIs1$&~@!c9-p1c6A#RuG+Osp2{6f)<&b2c)_SeG8*gx-gvpTg@soOG+z=@T(4?e-Sa=~&q5v5zWTGoaG!ZIdt5<n(KHiJcK&I;^PfAj@M7MESPA1FdH0t7_*lQff7^E|VdeV$FeA<uEEB}>*;mC>{dY4fZOuDk?P=PwUi8bn{IYX1PJHgePO4twn6z_Af4;ptFMoMI+MP@-;Q2o{iduCSG^cB=o;0;tp?(y+urh?m11GxbdZ&)i*b&5^;TLGGT8+2$L+$Onhq_CS&bc061_86qg6VtuTGM-RdCi1s$FID)(x<>ZmueY(l-T9j#yAf9_<DSbzj~;}&p7_hDtulP>)fTwVLyXAySVO|-?_|7CD3ktKmW&2;kzjk3>R#wPiBR!TjQU3aaPZcK)r*O7Ed21e*Df?%5XEvqL(w=l7+Ts87|aaYKD8hlcB+@Ww@P*dLY9siDaH-xa9uh)^AncTl%nL4^nUL7L-4=*u0zF#7|_n?CP|lTh3+WDakZtxIy(7lgQ3Z70Y3p$;a~~*QR_7b6sCiv7h(%kWDR=#3GtKQz5)M)go5<OO>E<E~}c`hGiKj&vM%p3qZ|F3qT(~vHitGV!H*ssGlXa=@6;n7qh&ZXzD1rz{HCgkGRzIS;F0W&&tJP2Rc=xC~04dO^+KCNX8_$*-I-FM0Po?E8)dg-@|n^@MRsPbm=zhCGFKkQlZFK4bD>6y~u$OvWsmrC8W%gR~=71Z%~9QH8ChSKE##fwrqPTBdsZX9;0)4WJgUrog|e7)GUWa01T`m_rlD|C4e#><evk(_h%OpUW<|jW(-xl4%{nyqsHYo9u=jIEjUio?!MmtJF0Js*V`hZ3}tA+T{N4kp+}NTa&Xw}(50rCr9B(hxS9KgLSDC&?LrX(x~9k8t$RG)@=)blv@0|uHxbWn2Dg^q5jtNXw;*6c$A(Y!9rd_wP=V?iuX>48Lc1<>Td2j9Asj-u|F_;<uJ||#6>~D}mi3(y5;y1K#6C^p#3i@GBh7{}FhZ85B>nrqbU*n<i9QQzN?02S+ihp!#9k^jOt^AMH|S}APzg0cc0l1;;Thseo;}=*{XIO+A}FYrH;I93#X?V~Tdo8R?54`g%D4`a<O;4<ZI~{VPuw7wulLXrkGiDJ18lGcJH8Cg5KXZ-&R6-tKKJ%>w{?F1M;9VQ9oDXH6d}^300;si!SMiw>hVz-TUtL-^195bNB8KUC}%DU<?`IC;^6L3=MUdInDxmqf{gn)3VWzr_t4V{<+4yHy}TF+ZaKA|d{7yMcjdj%Y>We1JRkfGeRaysg&HwxPN`h6FAvaAF2it#^#!-VBX`634y6ag`@NS2_)j}}qa3va`JDpJfBI_W)dQuORae<p%~fA5@ye2|r^;(?M*cmSqbr6_s3+o|RSFJRhD~-=ow-%T0rq&Lan-Q|@yW=h0!)^Og^4bebfN~h5Jqm_%RLAg&~l-AZR0u`FB&c?v^@hk>-o|<OHwcHD_1^AA;_!M>nYVqg9pQowo+*vn=>IAnuE)?Y!jn&!YH*aoeA>$o$S+OHDrOJ9v0WgYA67&luv0ouOY=sY^n`1p2otfeQJ~@tx#mYWf6v^bFa?Fo>2T`A@!@|V{Mq^KD*77j5WUQ!_Mo=%*UX3K}G5ENNzlRS0;yrWKz*cT)MfhPddxKyw#c$doFmO(bZsI0^;x756NAVj#r(56c~RbSACXo`6n_ii7co^!%YwLs~W?&wKS=hCK>%hSkWRRsqDD~=FRhrt24;w&TK=NbcGOW-nF0QT~KYOdP?qSpqx%pFG`?8AB2y5jj31s-FGjY$>aD{r86n`b4F)J#Eh(|PKsv1DrUpHVy4x@E#0Z6nR~T*)}2((lGV-3cB(n6n}w-pHauB0v-w+#X6ZuFOqDUeJ1d%<xEl|$mcgzC6|?Tt+E|$ozV*$^%4IYJTG|=MaF;#N;Sl49LNr_|mo=BlWjs$P^GH<Y+FrN$+Gg(m@<|Zj>k<SA@5Yn*^yepCg-?v>Pb2*4&rc)#@mc@10Q!me|B3kjW0pMlPu%}c-2YG9|KIQ2|5p+AzxvNBl>d?A|0>G=^zTWse`rSF$4(r7<K}1Lm<4`syg4DT$HKR>cG<FY7^s2jn`)O8N22=3`VRy~8Abh^?;onyC2Jv1Q|1>8_iV)vW9y6czm`SUdu9E{*$aA7k`0F8PM)===HE!O-TOJYe*V42&#J%h#UsnUbEX4L_Rz$%gS2eaBjbw~)cgA9Bn~kD7WBTHfA<ki6Z}#iKwq=+b5FlTI{6mU*I#G_i2UURc7iD!&48pU`;<O_Q^R(gQT5Nt@}3@9$O!nEj6icLBXE6ga4=6UM5qktg`NPUiV0$HMo*PHh=DR$s${QB4ug8{Tx!5wk{SrlsSS+$`nkfu_)9Xuhbu(;&OISDa3Uk%s#W93v(qpB>Ms|B2>ir7KcSP`F`Fyg^YEl@z{{R};#8e~@*sXDO|blS7tU>d+Rb$~{n=HXhWhLUmErDA`0{g|3fsxnN2DivLcMqKRNUZH>mW?>1@2r<Aw2bU{Mk41p^6pct8aW(h~Q*c&Ic!46jHb%Rxleef>XkzPB0EmI3E^&`H>}z@DyKXZ1eHoqK^JI-i3v9&9oUbh*{SsEL%S4OBzJ9ze<cYNOUG7T7H`=*^2t=-rQLir_x;rfbIYu$<!T|MHd(>B_l{+MYL=$s(%BnkOy+JA34wyE&{R)(K<I#_)U{w=G%!F4(f&EXv*ptezSCAb7m_XU3GYl)}--MlLp<%X6)0L3omuplWbJ+aZS7A@;UQ}I_WAd3C$y&56rEPiRSvZZBE_#@U4p-@7nHe&wMdXCe)3_o{1D)+U8hf0s^9vcQ|Fl32PJi`Y6j0`1ZwSWpiqx*_RizBAwGpj7}NtcA}ROzk?M!S5keM1DP(9&^4coz+<9`t2w@~uZJ+*Dg`8ykX*FXLdGJk$~80tn6#3+fgh5XhnOTC)81xHp@uR+*5R(NZD%5hOSXckaYWm$Oha~2ft);cV{dNe_0qzoIsPH{t1mWzd(NAEAnGYrZ}vGnyyeRpzhQ?mpBl4IuI%i#s^cwV_Im0aAu14h7;kWlRLNXc6r?b(T|!rIF%m7y(&Bo|?`X70qailSLCW3Nn=8Al_lS9MVa>*M5_Uw!J3fpd6CNlBw2Iq3o>#lSJh)%ef`G>CCFmWG&M?#rz*}#jy*q->l5Gv~FSP##h&ko*2;9^7-~g{pOn^3JOo?*o0J7?+$uCtYKLUV6#I52(pxuB|6T6l=C8R}9sH~_Rl&x2^b3lIfPb#18;E}9Lgy~A74U)2qL+gX>;;Iymtw1D<Mfn)pk<I_Yd;@^^kYhOG5^#aC{}Zf-f+n7Jfk|I5glUau%AN%$#7UYuMn@y$psipM_JsEipFPT4KnW`uGyrZ0pcb@VY8VCS*2`d)Z3;I`2>NikeKl`!Gtu;xnn$xQw@AO-^v;xn#D%So%wN!rb|JGPgbH2{F^|J;?w<8LTfU2cWuA~p=4HN%RzX$8ho+a4!cF}m#$;H@1KqBvHtMoU6ehLI#*S7_W42L$#-oqD{tPZuas{Hvf9-xDrtik^NOzY<(sy=<BSVg12TKzu<McKE@R;?Pp2H=AX3${iIMvb3g5V1rrzuH{ej(knA^NL<HECbnhRaTMkWINFD^-eAx0i`FCce1g_3<p!ZRR?@!~J}azs|-RN80(V5Xb8>s8H3BfrES?9}&^$=S5>lFr+Er(*&~!4ute#1;P!7`{7%P-xcGD8c=6n;R}Ek0jYyENJ9j?xH_%r$;fB6X^@=+$>50iXxnOB#)i11oE>jF-kPSI6y!AH?KUMTDobcZ09r7vF|ZCUn&!C?y}Ys-3LXWsBo!o!ZWWzbR;GXR)eF!7KEj0s=o;oW8~zbqG*5zWH%un8@=Q4cMJ+=F*%E(?doKy<R?)3cS6bq46;{f!(pBVb9G4+1Oyy8%qyhD~j86e>Z*ZHG09~%Y&dKc8(S5~vLgC9|*X+X~RHcDLq%7r-v<8)t9^m;#cx^d@I}B9+U%ooW{~0jHF*ZjhKxa941NJ8dreVH$A~xXHUImm;^#)|I5-f2BVjkdLt#mx!%p3tGV2nuVhDX-5CDlL6t2nxHgr2s#9#<y#Y8}+m*-l67c|bCMfy_%n=6lV~2tyk#{tXW(0_Kf^o`f~Hq_1fI47_ZTGdvB%ylp9ETq$ub7@7)%UonPvSX-H@MiVWI^jD_7LZx-6M#F=z%j<6GiV`?k>enf!vBs+BH8^yLqxwSCs)5!PLH_VWyTz7eL*be9+h2+N^90zmM6mu0Y)UzTa!EFM2{sKe&+odjwS!Al1)BznB_NhWasil(H-<Eo=9M(mGVjTbhChOk0#Ry~n9R-7O!OrHjhJRIQ<DA{1U*)dsRGxyQ7Vo_bxz1i&}+RpD#faZ1-tDTDep4UG{kD7B}1#F)Ri<-c?DbUS0;wzOymkCcx{+g@^*nbmH%|0lU{lHFh`xXSExQ0Hi!7EkE?bSf9FHVFzhbLvsD=eQ@eT}N(^zNpC-#hY3}_xm7<o?3;tZCXePRFYDeu|Fo_~(seY6uba+~Kq4O`9xo6S~N=1!^=G#!!7tXZVI!@&D8tH|;5;Wr_=>-dvvzePeHc2i1$L~-oYw5F_wTvd&8se*GKP{bM&BJo(Y;5T?jgL-?(+VK^^7gU<Z!&Vo^|)fP6&bwH%j$#~-vLY5Kt3>6ua=jKnms}4L7I@<W(S%iYG*-nW=i|Cl<g^TcEwEbMq;l~n_Y&+$Sw!eVDLdbSw}6|#4U>+2w5OZ(>sjI=nb^2==POVLX#4gwh2b-16+APDt&mAq8kiD8M&xeIC!z`0Pr5du|aK2oTLqlaNnydV;O-Jm88rg@-I$t=gXJXrOE)@KB@PzeudaeJXmm9an<SinG-Q1OV`hc?K6ve3oET%VQCd~Co5pa3K*BR_Rj^8%i$wbPy3F}uFpjWg$8ehkBgyUI137qeB1`BSmw?P6S>t#vzyF=tWiV>3<oi33Wr+Os#f;<@_+wO7d9VWNnq%?lw2Y(z;d`*au~vy_Q$g{h6~ysvm)5WoA?#QHC`nD5mg_y>gQhdi%PWVE;AW$sPeMa3lu=w>tu$3QNLpx-iUN}oy?FX1rSPjUEnj2?&%~TY4xb9lm>jdu^Qxko|deJwU<;K3Oy^S0_3OEKo*%%z`;)hLAEn0zhptW-b>Bu>sxVt^Fw9x=hQJNsPwaJzKPkN>XKQC6tEGSsAGdT*QXL5ouolU9g_$0n9zG9^dzB<BDN!se@Pv~qs-}5ybybAnbRv*_Ot`_kwL8{_o<nP`!%gMI-tCNrxfXBnf)E<LRmya<v|fc&1}WwGX(P@kcA?n<)+;${E_-7>eyh&21|%YPF}BH%GZyV1RK9@rHOZqxz|Z!2<Y1vNG@FryPVGF1hQ*kS9PB*yoNW%x_Omcx<VaWNG>tjdK7f7OD@UL`WkyI+>moDXW^$+mpXp#Ty=?c3Zxd2rkt2$QqES5$!?(M`DDH1m%wzMBJTlbYceeFL@A4Esou^4ZqkgVh``r9ssE?18gttV^5Ivdm{&6$=APQi8EkM=F-wF!7hdk9|LAV0Rgy)CzAnFfb6tLUU*(t6lk&@XCcnIXUVfQ(8wBViyiBs9wEEWPs>=xOZ8Oqoan6!l?v|3v<(m$dB$wNj^p;VN|HzWdzw_Q#>iLwpwo<Q~QN8=6i*=bq7gU$ar0A}TYH9nyB6ri(NrYQ>+J}%eey%(3D&_*ExKUG5Yj>ZXP{^t}l3`Stzq(SNi(#1r_<XO@+md}EB6+U2{EUbsmv;X?iW%)UU<LQTu~@<1Q+8SQ%kO!@#tR81CMMSAF|Qo;-`J{wy~>nYhAI)&)a<gU*(GEsm{^PnW?UwiQEg#bub*d^%`CfYiR`fiGfdfKIGeNKEW0f4vedG*j51!&C@~iYY@g>zB~l*<^Uf;6Oe(Vg3L=-ktjhM0i^G5Q9fRp-D3C3d;P>K&kS8mIyjtiNLVDoTwFA*Jj|E}Y+A<}~7&j4Lxc)L|M$X5JD=#PDhG@4SGZ+9p+?JBp)Kgxpzb)5at;-OP*_i!7S6AU%il}n&#Z>xf;s#pz9Z1e(vOKVCuBm#Oo{2=cMBmf;>-=h#$7SL*4(_8%--Y4Bb-y^^YUIr)4&YA9xHk5{=t{JRYYiNYE-b{}gz;AFV0Mjxx0JOlLR(^7)8pI(DY~h*VCr`sFqqcQW)n++GJP3?T2KWL1z2pTg;E7@vhlvU9(c{xQP5ctjXR3-PS{nIJHNC%;C`8)fib#q6%I?GJ86%b(4Ety4h-I*Uv8XPup%_X`Yq2kz&?5#!T<SJi;kUFp@}o99j{9`JP*zI3WhjALI{c{B*YAj7bhs5wqP=S3L+IW!brN6mQKMWCn%n>c5Zlw35qvJQ8)oHRTDid=pAF(4Qhy#m5T!8VVCN)huxf@@!ZZ$0%Ts0vGVF3i{`rAM?=`MylAFh-2xR+*1+SA*Eu2K#qQ-$CDpvso;Cfoxj|cea4ci8cK-PclUL^PE`phaXVKxvYKW{^pD3?xRXpO_ubTyp3^Y{Ad$+jB%bFZ-L?-IPR+zR{Ijb4EQAiEY$0V9dHsDlK!C{ntWburd=$j6=Jq_LvCR*X+Oq5WvvO;u43cj-dAagetM<&M|>vUxx6YbSjA`;Pg%?fiS;ExbiiA0F}cui+CtYqevVs800;EDK3$;OhT6Ej_leQ#bSLbZET78Iva8Cl8$lQ`u7HWEh%$-AuVTHndx)tO3hh!c%WL2X2e21<vwJz8Q7y%4CE9jT*@3xVZTj<O}E)6pm;$;>ZgOZV_gn`+=F?_8_@CB9j>2Qmg?VE*rZsFmnqf4h7E?90ls?2|1+T!UOZbs+0#*_1CWL#(jbG6Zb1Ge`ss6wX$nNI-_I3bQ1;iYezR#o806I29PcK9V)hObl$6ZJYdf0|nNL(#grqt;oFggW-x$a=x@G9Y#oG1C+g>o?((-ovli>XHJh1)IG@i95;qsm;$<<_+E4QRgT`ee<>#8<1b17*M|aRY|u5i49HNcLCF2NS>81?#$2Utf?`alp(~CU2u*V|Mi^z|77}&1u`iS>#y&$^;X{U$Ea5BWinlz)VNfr)v%1CA>G@QXVT;x$mH{G%lF}meS<}>7P3Mky(bjADTzZ?5S`g*>d1y@|Q3T$%%<0Qe9mZMNghPsgEqgc4P)tnDP)$$PY`?x4N+0UK^N%pPty!Ym!lD`WVt^Ze2f8EI5=BL~%?lOjq)NfA?rSIM%P?*N1zbV|bc;wjS61|t`1UWyxSh4f@;3qF_8XtX={~8deNv?Q^yjA${xrhBKmPnQ6rZH)K1tVo`ty@?-6!d~PttXtr0d>Qy3Qqk>A_TgX+D~Uoh?u4rAl@}Qo@v#))I6#p=J*Z#>&qXT3;<$`N4GSc!Vll=i`Ztn#{#V-MUd$%-Xv%^*3wLgqcK|RMH00*Zl?QF&S=~1#7AgZv3ejS$u_h-O0gEMc>wTSUdCZq;6d})vdFWNhcpSQ=p4gt}f5y>b7XdjcN(fO?#1UUB0ASx0<8_CG)56axPkTu2>i4l$zZ6SDv)$PQL<5%=i{EtkG*GS;O(n?dybi@w;#wE?$v_GsM1;OINNb$<fy|4bN2S{Ha78B16jx<l58MDVmsFJk_L=2G+^Xr}gPZ`8mrc&!pn&3&LEq?xJMd3!l0wPIpPx?Rl-YxujQBsjCuZYIsUn%)d~j?p#?f#1Af1=a*V_A=&TsL3W|9$<>*J;#C<n`wHhmZ0WL2+$bUUjA-55@uJR<QI{>$@jp?l3ulj<XxNRvyh6tA?CP_%ZYK~%J-hgf7T!~;f8zkAOKNxivg+SOX}nYY#5jo+PTysz1L$S~k>SeFO^^6V=Wd~#v#?^VDxC8doYwgNJ@@N=wP*L}+rE3a0K6G;8g9{}?4|M+eBQ_5j#LFWY=N}e4ES?EGYo!C<so8+@kplL93fr4Y4~S|LxXlsgPsF1!jZibF+1>j-(>opme8KdLA>Oynig=dhK<qQUWu*?x<m<gPaEqe4!$83uq7M-rs=SuBV-%@yckp+yOVqtShMnA8e$*xdOLHxC5M4`Cqb>{C;pYM(4{a?Y%8^q2yQ9s0cwlxS_t}@v5Tt=%gxRXh}ZOyW{x~&?_mjFKE3V1LT>nY8Hz8chtrgg`=S34WG|@f1hB{8;nFuWOz9$8djn92L@+@f%Y7EoAL-&yo?_<;CYFwn9AGs3y2Z8Y8jSi)8T(YeP5I{NpXth%DezO{6kvoCg&PFs*7ZA|*NJqtBqVal&jxR*fY4O1bvhXsC5E>xnqnvDQy`Md&>|7$R0`oOGI!a~VbOaF{7I08$cFZ6y!e<|5{G~sk%yP4e9&<~=8mg23>c@trX_HD1M|yrhhlmLbU)u#t`C~-1QD+gQABBqLtFkd$IuvwRwYylN1zf?%ckeXLuv#(I^K;fA+laBy(ENwm++X59mbVxD?NxL>`X!r4eBi+ya80D3h7V~_bt`7%3<GH50plcjQbrmS%kdic$O<pN~||G(KQ6hLShcz;=7l7s~pFvt3OocQ>Q%46AeUxtn$kbnfp{U3tsRCNP8k<8sM&Sl6R1u0*2|POlobkn8grEWYG=Wel}$N3J9n2t$zTXPGqOj>C8L6@<8>pvLiSK`xeH~!DfpoOOLrhOXBi&#QnDsgODToj6FA3H?*iL<M5V!%p{jw3wHd_57E~At*_L9FE{0Ir31ePgfyH(n=<f!9TARe-j|I47jxzS2^!Xl@2%^OR(#`$Bbq@*D2dQFp{x2l6KaG2a6>nBWy+gE-HF9?x4<=3P!ly=%@xwma808ap#T|<FxjTc3OYcW(mCg)s^l#=FNRQ>+Vbr+!0p(R?>L5y$p($i(nQ<Z{<PJ{@k(K@nMP6p0k^&aN;<lCj_9T}zRr+m-S}_@Z35_TNp&Hku*`uH7hAUCX`cP6$r$~!K&D@R7m1FJnr|)KS|^o`mFwGuN=I2_*J4#n5*@hOk@`^OiePuxdx_DN@Udn%fK~^7i6$0DkrYF9&`~t<{fLhVT%tsz2qavi2?Pnf6NLBV{EC!}5lFnu`ozdfIV%JOYPdld!#1O2I1PripmrQ*Iwh=_G!gC7E5Rh95-J_ol7)`3lXAPz9at%ZNwk=v5}?n-*hobECQxq=huW0*-nj<yA>0!)9ZGb$EsF;OA7)2c(BoEG=<ePCSKj~i_eKDD2?z680!W4Why$`<68j}FGfB+=%%pv~M5Rl1J)y03jY=1<^D!aX0#-<<0;h>)qdS6vNfh==e54`>F~TQ&InqY@k+XS+Wu<a9iTP;*M}sk<btJIkbIbC5+=1;9MykjipxoqUVu=i_aFugDbPVMmotydpydzD$k;(CEyiMmEb&sXT2R=)Vx_@38WHdRQWU!+oi?4Iko61r5@5E6TapMV5ko}XQAmXTRn7%iaqyB_0NIU6*7)KqtAZG-1<uWVx0%?%SPS5nwKG6l~IqUmMP|wYaMM2`JBFH9~DzJBxF3870mi^w>r=E75yjiC+7qaX8&5Q-{DS?oxhIm0B#ABZ|0nFnJU><8C#+*y+14hhnMK5GVeoCA^$l8+RgipDg4WYsl^Jx+bv5G=`ndh_^ohsU!Qb-Wn<r1}1s^OFw8ex%WoAfMZ7)kz=-Pu-lXMQQW^BaJS`~~+ThEeHX--AMkjP`COejTQIOu6~mZORG%2G-8ITck{CdYSUa17<oZ10~bh1}cKY_K}Y4C7SPow%cFI0_83+M?=_(Wsw?iS8qsuIzHmc??~iKY{_(FL6v_;{DPW8tO?hO%DxCXF~~HAd?_5ZWI98~R4aLwhmiX;(oO0qh~0U6%bld3m6y4Op3`NmvhQ_7Qcigp>N}NhvDd7Zgh>p4<sI@}d{zhb<o?#~fAWfqydA|8+JdWu-M^f8gyE&GnH<;cwh#W+><gTyoNcb8vS@Vx%XAxFE9{sVVAhhwP8RBQA5vo2DE7(v8n``p)$Nv6>7txe(`W~Wq?&OAsSYSX=D@(#)l5>G#|#qc!4hfS3($twj`Btt<5*<^BY|2cxWeLq>+}M<spT7KMF@7A@mc40l+H^O%4ieIoswW<exG^#JE?gRug&jEfOAJCE(4_;2YherTiwRJ5s$(#G5&gR-84@;EfTV&kTLyonG{3W#r(kKN7N_NmW*=LO*k(C|E<}0IbeHmcL1A$+l@5bGn|%Fzo$fY$&9mmC`aA|ZV&La%5JXVLS62tM;BMxW$ZB^Ynlz=lHM8XZ10&QxHt^qizJzOx5-xFZxVJ`gB#-y>B=sA|A=BSeG<Zk={UULd6J^QejiLGw*%8ba=~Ls7(M4NsMjo5IcDM(r?U3$C(FAI=v-w|i%`DVL@YX7M1qJ9E9}c#V;UmuW!=r+P|XCtzroE}?x&Th_&TNU@ILrk?l0he?`jh`|1&tb8_+Q^!4cLHLXL&F^2@iqFZbaaY$}47a>-?hUzBf?gYnu>O0VMnqim1YhLy_*zAP<ByzNls($xnnO3K;>FM<H(HEI^DN|j4P{q~U6gQoO<&>qfL@x)*fKB4aCH|myv7s~2Jxx+KXE9qcD9cRg5;0S>P3eUwKg~w=%p15=3EsqEWyW5g6Yq$X0H7}?4g=D;<^#gj2!;0&3`8xfc>p8-^A2dGB(uWpGf|$`8#a^bTw^pHLr(cUQN)@4XsgJN9C^vdZOm3*LdBgF~@Q&e<jyj*#b}rq?@C3rrwc0H}+mqLbSxVMkj}qz3(K%upmu&vBFeDck9={)16;z?`DH1LgtQ7xSCN>ybfAY`7Qxda$q!d5txl*hiIT!X^EEw~bU68X4k=#{E;&`ar;`$Fu?h2)oGsYKr-dQrIEMNz>Z71n24brB8^FWe?U*&+8(H)Q=UXkwFamP`wYUXZ8YS_9bdT;(AnT{0Z@u32(5$YwvO}$gz_S`-o`^*h4HOsMBt9j<!l30?5%{OIqNtY2RhwY6U-0pSjbYd>VZ94gbLY43*w@$_mo|pbiY<d*ExsYgf{v^wc67&P96Qco7k5t!9mYjp+)>qZWWbGyXHS_-Pi$2<Ee@#cLCKQb~sa3<bz;Fo@vo)<LWCAp@anf2w>p<JFR>i}h&BIU`Xx_^V%Irdv(`AHO=zc1rRa{w@&kFvB(V;-r=&9L1rLCf<fvOp{(H50{Q62vv{ItcNzvO;CrcEp%Bz+rE7I=yWQnh<l6d!z&EM|H9C$KK_=Hpi9u`ExVVvetWWZ@2JBEt%jPxQ!=Y%j0|%QMmRyf9T!!(dv;f!wq9nD4^4*ASQR(X!{*9dS<#bO9kAq+FSpkJ?_9v%)Qs?e!%ewOq#P+|@`i^JtKCJWw;1?;5D*h5Yeo$!>R7p+mtWnvS%-kqDmL0P!jJD!$|9XznBBdSbryvj0F9aEElI+pB~OQhNBclJYcLpTCW$G<@dM#-}paiJX0JKi7lnJ7hh1!14jvh|G1fs}$%*J3+KDH;7g$iv}t<M@bCpS#&ajVpgX|+JI<fjw0AZm;p;8d1X>WJrd87dhQvLc9KTe1_c7SgO$hMFpGtiltREj&k)MbZux@mFtl^sXCZb&hblhxx$uAdXf7pD`c~NNvc;hz{D8E5JbT2SUnY?Rc|JNO)PM2RqxPD6w~^aHuzC|z0?IPU>W^8lCIo2DXPb^VkEEKX+!)+C)pftM9XWpf_J=BGj2g|C#NeNhX}+ig54GycO7JGue1(2|q681AmTpe#>`W@{ss=oEkPGeR#<ZK|(qd{YmjvLod|Xg#>0hY+9;;)_lbUIR;pj%emW5y%o4f{Ayj?olh3aT`c#hDi#_7i`TlgO##FTyW_e}{p-!oa?!-A|%RS20hEw=FxLBEAf4>vlgNy@qL?K5|N7~C=3NLu=6;U+bFW$&BDJU~{gvxgd@*=aVnpv~Z+_aMPU=kLeR)5zyFq!!gJdvBDKDC~-G(;jg{-gBA<YDThl>shr0+(GpDpOgjC5fEHOb*wTBT7fP~75W#xE0;VBi)YIzY*`io7NbD~;r=-6Jm4VMxT&t}tQm;;wZS=b3OdjpF*D^%+#@855~3}%@CVZziOCwmNIa=h*=k|ZVxevEFIpSm=U%3`L$)}CpDd<$U&ZaP2roKE<^GK76F>`VscBbYdei&zGU|3>r?@Rgn#&j@lhj5E*wMQTmP0kirKWf6Sr(-{Q^#Zr5Drt>u}1)$VNcBp^gZ{@P}w0cqlekhW6gxxZHb%KDk>keEic$hRXg05*E~u`hspYliRc{p-qorkUbOg364CLT)^6Z^82|2v6Hgt3`NhWFrdf9FPE-ZY_YoA|p9k|0O~MTYD`$mi6{+X`9>k||T^OeJ9l#f}((q^&Nx>83LoK7FfB|VHEwMq9LUEybN7mkoiqSWh#V}`q{b^^9Xqrk>Y!B61&ojKcXSDk*wy&>6brb-{kUp>~ppf3aAf$ivN_6^{UW5iL)9QQWrlAH`xzuaaO$UL}?yNIr<7a^kZ!R&SWz#<Iun8Y1#I}O*Sj<~YB2~b$75-SN8p8c5aC0gAML<7_9#sRkZueeu3bjXF#XneUe)$2n_n<b)22i<y^P*&msIUXn;?_z`xaiy{X@9`WZt)uV<KpLDeFv^OG$+Heog_H4XZhBT7d&tE72tW9cq4@96NDZa33HHMsvy1e1W1qT-H6j`Do(GjI6Y6Co<RS?>BSMJ*PMa$lEcWo5TqC09ibPg`bdOcqQx4HCR84wkKt$MsJvj1yxb6v7t-5R*p4u~NDLl|kJq7h4RLo(`eAu{c3;d9cZ$n6^9r|HzZh#rSDbc)*d@c)t-d+<y5IPizF0szy;O<mijFi}OO!Z0-3rmPG0!x4JL-3}RfZ|KX*V>AgS9i&=ysF{;{t8^VB=cJeNgoV8S81xr~TzkP;;$iyCW_}m0c(GCH(?boARPtH`ibaWjA%Az64~cpJXaC*T(_UOF<Rcx$e>gIp`rxcA~q~eiL+;{^j@J<~{0F-c~p7aT+ERvbvU?n(UZZ%zV6WVFPU@-dkttOQYoOz&TkvuguHXzONW!V2ell?i5=t5zL#N!0iyO>}b==f<<3NPeV<bkAlpVb#N=mRrZ6kyWOxHkD5^|d%(3qcA1QQIF_v$wCS17z=a!ylHpIjdK9mjpI-Dtr<Fhw77^M?6}pxeKIoA?=utOqLkIL>=6#-Mcj@Zj={jieA`GUm=&%M<#*a9(u<2^r+GCss-n80%q_u4>OT=m063J^9yP;TR8UEGe6VyC1kKEhVt!(f1WgrLP1P!)uoH?2!Wc&-?lo7poYB<BmaPr;Uxo9B6&1RZ^gE}_T<YSIdhVWtB4u*83&Mn4F17;$pW$$>4j*JFuntAD`+<)s{=r|5&bIRXxWx-&Il-64}T9zVB2lALUtPNXlOg{OnzeTcywL~qN^3r@0K5J3CS9$2xC9+TGw@t_GCbG|!jHlNLPOql8c3+w8#i;fG5|Q=zg0fUZW((5uvsStl$>1p)t))otbh$j$m|R=6wL$kYe4~A~4-F?jg9K%fm!TQQ!ZzPNy-ZkI8y^{gt509v_3hw|2Q_}F&R_@CGTg`UqZ>o(@CB+Edeen-=&srq<UhE|9Heb(Jm<u$jyCW-X=3SwmT2@56cT?#DKC8S^V<2OXLml2G}7K6|7{+qDUPY=Z)J(TgCim8ALZCv>zD1cnGuYDkBE(Ks=*x!Lp$v;?yc#w(k7i{W&z6v?nAI5+@T-4$0H>r41Q~cp>FC)SVy5GO^+%z9sOX5NAS180ce+n6u6xFz>bpY<C)nm9&{vPM?h6#XXw7bihkOm_=-wTdE|dABRBjE(nrkfd)`QQ%$|fEb!pFmw6QF=Qwb+fqQ_iE=bL4O*vYuuW1$q#t^q_K_fAZbhBp!Z9YQi!K0^j~t%nN_H{X<cHR`$2A3Rtl<gL1eE>&wJ?CoI*ge?SJf$;qRy;>u~O33D!<3=xS*IJN<ef5o3i>ESkHw4IppyEpEonh+A?Lm8NdMA~YCK~&I{vbh~MO5?ESCj2B5iZo~CC0Ax)YSEAh|kIQ65b@pSchu8wRi~)FnRLIboRFUilRBtfPJF%D<tcHkcstden`rhZ%?ZF*}=UMw`M~@b+2wGRSlH)!FUW;r+mw8C2KbShOJLu_>$QTUp{@C`EC!^#D#`>S(H9U2OY)THgsz$m_oX}?6{p`ZFj3IT(CNv?+Vvn8#KqTfg2dBC!xRyVuRmhZ2*JhA2SIG%%p?>ru~$(z&BJ>7Lti0S8j%F7u42?EVUX1g}{<^#PSi>c5QuCoAkA{fE$=)r}Asht5Lqro?tnU0UN)%<G#C*4z^X1R@4SZR;8K|d_a-MtIRii-@kB`Tc^C{MHtvs<2{2D&ne%+@^=M@pDN4A@IwLg4{z9Gp}FwuN)t}uJXE-7oi_8IT6sniFRSN@LILEmGG-D}*Kte&Un;~{NvM-f{0=!f?De2)8^jEvt3${lmxith<DtCmVu*Zj)7i;YK5~(av*jq%b<a#d7hlAdW&2YCpFraI@x5l1UJdfbN4#JBUPrQiq9G7OxSG8&PUERZeEnIK1cGhTa$SKdkY@buVRT(LRD;@Gqh?2a*V(`EvurT^czo?DwOr4x^>p2*flAH*T-emLevH<B@xAKnQ$;*B+*|6Sr&FrwM!oLSnJ-UCA!(eA<MD%mgUof8&DeUGY1vx^OzM%{r3p|`apgUq|I@F?BM!LL`W@}pwGQ487v=r#K?QQaLQAZK9=7+NKjIwsj`-~ZIuqsV4fnVkjt-3DlKhriWXC=SD&YsfxyoCH2h^KcYzhD*c+<D-S?x@Oog%T?;yBHN-^mSwSwnM&b$%#|-F-PSN?KzK_e4#V?eVjbylgXe{w+(9Z&&^;3ng-Gw4Vy>x3;_KNq~II*8E#I#jxbjVwB%vBkId?TXMO#{^TE>9Jt9v<nIlQFr1aS`AWaq@S_{8^Ffu;Oaxue*JJU&S)3&5Ji<shL+Hu14Xa0wJmMybx*IyRmi$ano8(5+`O;)37xh^zQMUZDxE07~H==HxmmO=!ZxQ26A*I89%)d?6+urj$@fwy<wtVATPR+OIaNBtr9@3G`1e<NW0F{)tgv|R2K{Iv-C^2Z{y+vou%Sq)er{3Fo1H9EDi-Nu2i(VTXJ0JUw_Cc|p;alPly)*DWjPJJpKYMT1Ys;2q2hA>KM64C7*=w)8&%SMDW!`F>)nrwI1xWV?@Xj*=VI+6}8_BYbF^vnVT!4{{<pL#zWF%~i%~QS6`N6Ugk_{3PAcXA)OD;Fa55OA_fMAX>z8TGGc5}|X=iIE^sgwKey;iJP5i{oe=GTmG4BK{FI=f@NBrz+rMD8n{`yq=Z>tA_Rv83GbUD<h=8!VS}=XY!!EWczS1`)&hH9MP9LaDp!5ZurkRuvhaU6CZGOzI6f3B4F{So7eKY`Mc*lz>nXGB|6QD8BClB2@UG#Saq7rd8>JK778RRs+4ml@NVhxLv6_E^=-nv^L>8iF&0zuF8C0;p0*|5`d}9-iM>3_;~puFRWcO>LgrKFV3PnW7?s63h)*wAn=^^RAGSyLX{Rr2)i3kkf_nuh)!qmK+G`ZXBsAzLuR(g)_H%`Jmnj+P5CL?bhvDrYTb3RO)LmK&pZvM=IP8fF+4dlPsM0+<uA?Cc4nRi>8!=t?ncApg&w_Pn^sHPw5hg9`mLj3@~mDwZkUb|dQ0|=Yyv1D7{ch4jv->WnkNiJD^xtGJj(onVd93|D+5jQlzDtxzhzB>f{DDTKE{*gX=a=H-Km(;@uWSj^U$+miaMQIB|>$)?QQSDFm-?81%~M(iz7;G&_`IMhVm4}B;9Oiu%yVfVKCQtLrt>RCQ^E)rAf-{KvKA<(kODCUAQseOhtFH-dD`cgF4GpMFL6%8Q4ABFZb-Rus+;!{65@6J{2bB2JJ%O(96jCCTLZKk+dsq!uKH7<A;bNx4nJK;H;x^2;uW`+S__PYK$py4f7oaAoSx;6}e)0e5~M@TuP`2O<CdcS;`R91WNs2FxWAWoA<kDK)2aYES}phJvUfG&0`j?Rid9<gRio?AUC1xoUWxj^9?xkvRam$I;K%r7zBwjL<jTAaI`HSvAwO4ztgVHBrUI>6cG3>c07c&bvD39K(+>L_o1&|_n7#y2&6m*7Nw-Iz<eE$7%@)y!ZFIw@iP{|S<Dr!_^C=<V_(OvjaeqLhD<zIC+As{e3fKCQS<rDIs`%YI#(OOV?8odt@CJ^jxnUFVVY~Kzr+snV~}P4ncbt9ypjvkW$^egi!Atw@gpODl(D3Q@t7(_!K|uAGS+iOXDn|VBK7=Q)H8kE6c0|LgxhV;-cp#U4Is|P&|Ns&5<+iLW*pzLi%;Vi*8F#<ePL4@N1YGRzALhpTaO_FR~Y-0=98qh(M&^n7R4)~tOJ5ie))&q#>Ff4^npK*sO4ex?9qMJ2?--m)zK_PB|9W2$xD7LbjQ&=VPugI1*ZUa>c~HDoUkSYd)p*NfpLTKOSRf1LZqSGdm*+5aB{#$$Dai19z^I<-1-6RRrf8>WF1kLeRVvGOPJ|hl9e!aH#V(I4$U|PalvSeIf_t|bDEW+Nb(^n9Xj=<pgMUVMMkx=3p@Dlxt9i*pE+r_X>GR$imnrzHKJJ}7i3O?<+&1Qlp_z>W-YrTs0v6=wue44Dh2%j+u3l<pmC{K=ar=f)ClHTiz$}&04D`M6DL=9r{;e`km2ql%MWwWtNF+}2DX}X1IwgnZ?w)##Qomy_Tf%6A=VxfNZ^C~Ug#`2)gX>@<QS_eOm$}C>*zmo(&K+pDgAc&2ysoT<Qtw@1-WwGPUD7-N>*6ZsM|56iLda&ia>a9OD+0TCSthVvlT1ZKC%Bb_d_J&nxCZ_>VvlldPHyEq3m26`VKCkTIbUJjXk}@f+L{%N3_s3L<3`{9)S|${!hLI=0wY#9fURr)?UVxeYqjBIWVK~8Rs7y+Va^guAzxaW18V2o+S!I`%wy?GJy@KN%8=CMRIs10&|m7tLqmcq~(i0HOmn8DAk3J(GN{x3jVpRwW(quzhEy_8C44yTwo>CcT9U?sWikN^Mrfut%mDxYIq}>Ihn929Ui%!A{xc+kGtM6O&ZKR2JJ7xBLCm+EfO~mD886K%yRHolDlCvIYvg9Y6_8rPD7a6y)1(xZVx5*pNNt!gh*;rE}_A-3=Z>blPucP>6=FFmzSd?T;awq(l_C$C`l7`D?CnrIdL<v%2_OYiJp|K>F3FsdVGMpk2okiJ53XUX?Y`aaBDf53<L2vrWJd{2TafmzZ;dwpJ(?|m_$p5c{MV)b;rqm@8Tz{G$oRfH4u`v&dkQI_p<ri>(ruK9`hOj=t}si70?|$t?mE-A$UH>*dd_1;FLf`=N;xLMayB528zv!H%p-Y@=AMynYdMSUJj_p_JLrW%{E{+4hU)+@g}i_0{P#g-_T*ribpoAk#P@bMSI*38!s?J+2A@LEXskO)QZv`s<4>sH|2@nS{pUiLG~lBLjP>@aYSG|hSOyOdBS`IiX(QX<|DS(Y)8$ll&2nOHRzgj67;-iHL_pzORI67Sg9I{7p#VQV~Kdh4&u#Zq*IeYR94Gu1)i-agN(E4xhBKR0g!uy>cK%!D?G9uM8(9X4F~gkgRm+DLHMxF*q~>&1N({T-^O`m632+<%m<YX#BGT)PuX7pX<3g;7B<TNe}-9^wCu{6_eP*cT8wL!rRR+#OSKRRi2lVgdN-{_p#FW?m*#(*qJu|G%penUWZ!!AnR7E1yo57wz>GAWUW_xXYCiU6&7=%r3{A9v7B;9SumP03E^C#_n@RK!p^q4b=(iD29W*yIMm++1#N$_F9ZzeSBtYU3WemivFt@TB4O39|q<FC2bEDjH)(@S($8^E>MpEGJv-wt=4sBnF5&6gD22eXt=Pg$WA~j%aiSQ!7XR#K=^<<+nZgGV+Dds91sDpcpV*RINuWA?y7f*D}4UU^#_$;vntSpf&?qZEh5J9i0GBwUf0UCvjm$<JQn{-otuM8jy?V5VFujLQ1uZ6$zs-*a;r1+{r_xk7S2)~Z-tCHfYlHxo48D3=+Uu6_uWfWg!6yIsyzA7ocDk**#CB<*NjAE{@uiRWrarz~@)2@zl8AZR4QLL(p!&LaUN_j})A@j^00at~5i>R8tx;eUFc!rK$W5M`dCup5?@)|Edp1^jaup;v=lhB<h5waFKS5@@&_)%1Ed}aKgpGoMUbah=Z(fd<T!;`a}o;)m0jzsM+X%PCENaW&!^{LHo<W#KD&puKW1Vtc9HAI(Mj@}IgT!dg0v|;MQSqKo$KI=8qi(yH2wetb-qt4|hrl?mQx$JQDviXm|$~ILgwZ+xWUorM!=~FK6Wj=+_B<2^-B242Po_KcNT|A(wjOZ4sH85ekg_vSswo$S&X>1#_E(iNJX|T=Y6}_KS))umJ7j@%CVZU%$`ERbgIQ`O{y>eY}@#HO^uO4|pYw&R;#hFy(nUZ4g{;E#iWAczsDIk93@6!IA3NfBs?bDiq;jx=NdH1RyUl=9*787YcqkK3K|6Az!J^A8`uKeNw&wRe8pNgk{UODZlGUbUx<#--5Uzdau{bFE+(p!wl`6&4+g?K7ISy5l^>d*RbkzfDUp4Gr}Dv0Rv1C;zS`~1)vd_yI|&bKSyHc~4DItAnlF?6){ZA5(~Hm+&GI=EHQFpbiNzG+Y<>3Y;?%c&X&Iq(eg6H@4?3nb%hC`?$+jD9_oky2ZQ4?D*r$%qqTZ`y?5?@Q<fKqprD33)}GGa2`<-Wtm5<pQW?fjSL82pL7H#zDofyuQWdiD04yE)8XnMyiUa(1FU0ou#1AZ?l(BVi|;voZO!PCKuX&>n-44Ia!A)YBMX!)cBFi2ylJR!6@gyr}iQq|3C^!*1`r7Nvm}dqE`f6v0dC$8PYA=?1=zV^{ouDK}1{Q$LVSt+lHOdWrX`^UfPzJFf@b?`1VX*p-rgRNzLgY7(W!DMiR;nlC>fca^TgXX4;W)J&6^<-c1Bq#iXWf@_lz;7ifs$@?f<L?ST*hk{JRzR=(yI%U})UtdE;%dHG-x3r9K&e&dFYkiY-_>nnIhD|q^b$irtAJjEG(x#sEoS5@}hKdbDCu^-NAo@rL|Z28u@TU0x@80N9md0OY}<Zp-Tb<W*ck<+_wceSv2(zVb>;F5gZVFm10d6R+phbV9UlKXSm*z@;+Ap!XAO`TkCTztb<#<#xj22etyL9zT9-#Gjtl4yIK5!;*bmC)ALfpUK{zH<8dU0FE?W9or*_|4av>ub&RwO;l5=j#Z+j_~UUzZP8I;m`0EAAha6zSdk{Ypy>gb-~wy>ubUFwcz@d7hL1Z3a)-xbEQI(YOb*g^&%zb@|r!pPTj-QD`1kVW3T3RAksaIr9S7!l9e}xie#@-#BW|Io64?HbsA;W$0BQ(%6nshP%kcOw4`8QAEerfUHX_OU!B(8p8RJDpRys{S<Ut2;vpelud0@B^~#(QV!XAJ;-z2Skt&z?Qa>|dW4U_2nwKr@#rXlXlI><AgUsjZv_5^IwpuUGYQtyc)#>B4COWZGdXjfGZY-;V+@iDAobxj3tfIN75R;$3{yzJ;sIyMD78V86xU8p!3xA&e^kbdIM{k5}qsnI3bYzj`0;gf|!Og2&zSb`<7MV^8s26K{sC=)_YNhe)m7)HUPJfB@N-q96{o-Hn%Y|ZUSQJxF3R;if`-O^Tc;c&{yfzmet)$N0HA8gvJI>j-^E-W{=6B(M)1va_U*>hYskT~QceC0aL}>L(XEQ<1di;6v&(FTXKXoM+3aIt^4URCq6`s8JM@Hk~7+&}#KI>A)IBTky_U__1oc})lIVT#Kk!?6XC;Sjs#!04LmAa3)V}4By<;6g?;1*bPgt7whC55@R6a*ey$&)+l2<^mxbG;*U<yXy99if8>onGw-?Z7d*iq;f*xg(S%)ixO~1Sr_Z>hLxlp=s1_K=o2&S8KfZbUP?1p3CEL5`kWE!L8G*9W+!iRMFB-y`X`Th`61VDW2MHFzX0qJ7@=JS?vXVl4olYOe*I*#HkB3UhOZpp7Pp?2c<A5QF=qTy|)(7;g6wQo&4}~5O~0S@5M}8WyK|MU1s{H>CGDla%t0`!@rL{r}$`tN;;S{{KQ@JhQ!?~`I2pbps|aqGN`0W|4AtG_)jZ-Aycv}llNhC*+cb4z{bRt@o8HjPz@=PVr7P<&#@UQ)eq~?U%0q0NA5%fQ<g7A^%#sVB#J|x64v60{I(QEMl|BB)%wN6u74=}6Ok2Bi+AH&V&-nh_#~>0AZGUlt;YlP)VJt6H{tnQdA5w(C((%;54eq~!B9MKOB?oXjlTDk{~z}j2J0hWI&7vw!tfaet8;x^8mz1jQr>xCutu9TGg!S8m9HDDwO5<_V+LzuJ=WbdgM}XVAVwJU>RvQh4X`TgUng%*V_oc54b}-U;ApKn6Wblg2PvYDAwH*hUBr{1(x0pq$i|k|Dj7Lehm%uc&KZ@qepwmZ2gm2Ro$6_)+)M1#rrN2hKG#1+f?;;bj8t!>bOLVQmxcO0HtWkp{p|Ck9`|UozaR=yro=$l#>xagV@u)KEd|S^FIdiaF!;;>5dreS?2PWb%%&AlDop}~MIdyECXezEJ4uX(G-`X70|suFkj9`ih?o>QaPXVlQHLm>%%>p{l~dmBNEKOT4WJqn8UP3>i^2d%oV+6g2Faj&AMP@c7-3F@F{8aM=JU2Zw~sL|KKXrbKb-e<6hEa<<8wxCOFgLwW~maZ-w>+07{6$P*X_h*GaEc2h{|a@a>3B)z&h=qHj1UvQ~{}B6RJ!IhbQ18R|l1JMu{}lVl?Xrof<?9p^s21c}@ELR??3H#`t!J-u_IDJ3nTV69)Le0WN>uJ$yj7QfB0F&vHRh)XB5FPEu56XZE7hmAO9PND!sIwTtPii`iUsF#`oQqoi4a=s4kJ0)1xOop0lArfR^G?JS$;G8cJMAtQ3D<-&^8o-x;x8MWPlkHkwtz?ev)bZ=*FsA#F3ulGLsphg%w5tDRW<WBIw=Ms~o(Iurn)lM>=#st;!Sr3oudA4UXuu>{}Z<fE``}e^3b#Wz$Vdt@BRN2~pbk<O;Ybd?-8k&V{Z@GpVnC7;w9wAbJS3DsDdnAIhRb{KE<?0bhSRB8xMsP1!G#7$6Ql?eEFFr&5Hh*aO+tt7FtZ1%W#%JlC(cF;y=ift^(MgwPFHaP-y7xZ3v3?%ruE6UTzAYYC?>}L>e+Z_H1Em=VQiYK{RdR~bZ+OE9E3}i+R~hszrOL$+TAt{A3bzM}ew3?lfQ#=eM)OqsVY>WiJgXfu*OGHUN0(sEwT&lGrWq>UYY6>pCDlT*GG?wB#?Ahxz)jqY<-LY!_eSaC&NPVHPOQL*R8jaBxfOIuU#>rxsd_q>^b%9`mFAM3FjC80k^<(JaT01tlWzN>d19D}KEUUiCx&U8(Kba(Azm{~`O2Q2Dcn2m>FI1wPbR$d0;!39W}(W26*yl~6T_KpvPQC{+C=`aY7@WL{j)J`W9no278W$>9-lyJ43cjT1k`^=JiF<O^7>t+TPJ^e*rOFR%Z_+(r$UzT$R-U|3lHTd1?u*yIR_qmPdx_8%dDs^mk*{gEQPs&baK#n^Y(Go9*+{DyJIlGkMkAC;^uoba`GEJ*j@Dz$TaI0>Z%Q-e=Sez$QoLSqkI*jK(6XQs`(Jje%?u`N99vs_&r4;H7xmvevG^ahhc}UJmx#`x?80v|1&S(iM*qD2ZP9X>r=~scwc)L%0xNN`W4u4042N@8e%YD9l8^G6oy?B5XffIxsD`}u;*L!6Nn^IcLN^Bc4COcT~>z3a{W!Ehg>r_*=&(5gv;BKEwI5T?Rp62tX8hgenZ;8GK2aa9SJ?f=D>DYzPA<MY}g#p7NR)!)AB7htfrS`d?532b|`}XuCIOAGBs_lk6bz%xoji%#IOa<aSdCn!`5Z#YKIL<P59n2Lg?d#h_qklfTkr;Z5Bh?gu@mcEZtohD&{Ye|CmE{<WPk=R2ap7{2Mq_aU81Ma-0rzkha%HXh2M<5jueJ7bDbigqi^imE-W_+3>V=c!GwfT=w_e|M_)Ed=Fwfy)5y)ZP*@9IX&>M$4B+Oi{a?c#J&5<9-b@-T~!pS#CJdHd+S>ynr>35RQV>QaQ0Gr3eHr%n^EOk8Jc9BVvwLn5+@_vh2~u`DH9TKyIMvpqV6{+ugQHoF+<b$m_)z*T=d(t+q9cQzqhZOwI&UT-?3jeq2@LdY3NP*8+#(#(ctZdECmIKPM8vSE8h|bnKeaz#vK{5=XFPJu(4j>kvr*Hh9I6sUv;V|LNCX;`Jg*>{HtX~carfa*ZYy!&*38@eqbzdM6S<%<~AjX&EF(pd+67cKT+p`Lr-~aJ<PyXN#-X5f~7KGoZ3kOepIaQsC-PiP0-Z#(2k=T>bh29qV=P(e=!8Pv_ht^f6O~BQe(^Ke;J%?rJmZ<N!{X8Lq=^TcuTG($<CYBFnP>JwFzS<^^`W{0Tf^93}@xUL!f*W6aO&7DF#afg;1q3ye=Sf{fT*2Q;g|QV_it1R;Q+;7L(4Cq(NZ}0cfu4)UNF4Q&`f;1yjFpRX#BI+FBfZEqw+ZDRo8G<yF;+MnEve+lf*3s7(^&Yx9H+`FvB-g;h-vipM5?M?*DQtSVkh^ViK{_Hd|PY%$AX-d?eod-gJ(SWKzWM+jMqk#;hg(w?U*y&27nVoa9NT=BaoAd!^&FE2J`F(EWz4juB_6uT}<lYPo$@85D+cXLD8VHawdo9RqI1W$IK%usf!8&Z%oCrgG$=}a;}qU0@3vVx)1)DHT|$Y(N({oE|ZD&<OX<aNWoRY9X9u#!gB5bEZ|nL!Nf%auVa$F~Z-Vk3jt6E+01M}XRl4|z=``N(TnkkY1e8sxC6G{|t?sQj{fkM{1%f5<;uOdS>DVg$RIN}=8?OkP`FiJ%U~>mI$Zl-5A|FFRQUN1>PpCT3^oOk?{1w|FD;A*IBk?Rwa0I9X~A%uJ{FPKs|<hWH=W&e-ZJ(4^i|X-+!6sUoI2%Fs3(<E**FzG;RXM37Qk97P0uiYOi>S|pi5qvnKJ4HC6Y!r!?`-H0wn=FH-Yk=D%YS|^$o&Ub03CTS3<8QjHBfqw{%X|zh7qW<)w9Pj+knC6@aSeDKtLpZOMnyP20KvQohR;f$)(Y{M`sLaG5ouB&b=ITKFrK#}3CR7>tGzTCVP}49-{Ijp_6H`(6cOxNr4s1E$QM^d9o?O>eJkT<j*03L<KT#!`l!)v)6HyboaUbI(USw0zD3hv66*p$xqp6FSkkP4V(i~4^I#;7&l4;f2I4m@yB$ot#R&$<Pj-w8k8zpw<^1Oo|C5~ei){Vn|>iz@Y{0_1sv|I;_euJJsT}--`^l2(?_4sVXB}F#|**;;WSx|N3E*8lsfN+%C54PsSj`H&V6%i02nj#O;8>BOUE=z|M&x8WK!*bvXdfv1gDP`pvIBkn3vxZ7f@fj)Y?B*0ng2@w-TyAHj<N&3~Oq>)6fxJ!lcnUL)Df{3(05|+>h6tqK*ll956plF)1;%zo@pR^SVXV9G9awzef}0cxLXw6h4#3wP<XzauJG@f-D>?WP`|F-Y#m7om#235Nbcou5ijC!!jj<<b&!CcC3~Q78X)2I5bC8>0Fwgwg-19}iF)z|^Vw$nS67)hgNHgXR%8O=*`4yQ3U?uhv1fA*QC|-~#AhVxYhEmxc*;d0x!{lLk<0LF<gBad)Xpx-`zKV})?U^BqR7QW`LPcsS(7dL)u9CvpYB9xmFxkX2#J@qDqq)WmuBTI_s$3RF3ut=NW+h2@;^)?OrUxe#S2ISPOy0>keYKe5x6e*%@edEE99NMgQixM^x<Zr8v)PK;zqSg_vM`~`=(Sc%yskO0rjTapY}zUm({}Yd(eP%YL5wC3XZwV_B3-Jl0&-;n4M4ZWhcdQ*<DG*2M_gBUuhn&Jsaq>=p@&e)mLI_!If?h>w`NQ`#QXAF%M*f4n#KDGFJhog(~mwzs=<Dw$_uMyU8~T@+=irSE=f99b)dUIQBm_@vm99NVw<WHVpSl?`R1zZMerpbCmV(8hS&*tSKU~-9~7y&9_d$?_Rj2u*L*MjX~)FKARCQ(L5Qn)IFGt^2GUDfAz?d{NzL5QsXC)tc`=^X19|KiNYSY5H$gd}9{2vd*YxkWA97pVU|VdH$!@?9uRLIM10(Jx<<E+b;f9qTR+RWkAVMm44Lv>jl0D6DbCh2uYtLCzUWBcL{|0QJlm4U3u2Wpm>{(#5wWkg+yk5?nAYCS_#~cEm+e6u#vTFuB1BRLDp!|9ADvu=XdQuwW#T3W%<MOHd$VM)kk7WxeGd*lgCKVedohg*)j*>Cuo)VC+Yt`jI=e46A8+Ns_C^|NBjSVF-dnodin9oU}t)+OgKTwktbGlr-OWLEOskZ1EtTE_D2_D=p(rN#P8ICQ}6rY?Uud3A;!B>HK(_%Gt-1VA;)vyf_0dG_>e+qc<LET5_SYgm-GXv7CAA?_}SXd0j8RAUfdBu<poKAde$N5q-7TO(F3>8<wn`D~Q=A{n{DkGSrjy~6@9*-O?leo<B1Zip$9OpDC%3*C+Rh%O%`aZfA=ZDZ^Cq~SA^+_8w1pqtlbsKvByh0&<YFx~pd1gEGy|5kS`Zu_>m9H9>xG4s|T(>)(Em^SRqy^X+rxiw$mq#a*($R^X5_#pd5Ie9F(au(8qrSnq@D+}8LT;4i<VJP3DuHF9=e!$3tg7IWK2VC#|CwnY{QTl3Sa-m-?tRo@PdAUIZPv>yH&NQ_D~WDCSa_nD`LPwlqTUl0*w+a==DI;EYw0|1js_<z_dZOku0+uDL^qFQrcOPN^7+bxWg>)ig$hBp6nCQkn=Ce`yJtI{PTPsUmDx|78M?+SZwTw_nVwlOLz5a#8z*?X+tvr`=lSY#zLnHGp*Gpb$61$&0FS1TC2Bz*rjG<ox@3D9w)nC$_O#IgchM>DHne4pp(zgK3;yXBsK|bdf>Qs0O-Gg`-qxTg+5|;S_E;VoII6Tu!%@1Uk#g7tn)~vWbx9Um@IYswKbmpwY4*$V-9<z_C2$yyM$rbX*R@2k!vO}7xQPwE=tzV;HvbK{<p!=;gj6>nv9Z+NLNX6i01SYQ+ub<r3uy!K%S_~WW~L!SNKnm`%jNO+-HU{<_xwHa_lAk2o>`==8&j<zx+!_Y353Lawt%APLU#*3Hm)enu-0^W6D6J$oOKLRFvg5xBsrS75>(O2+}cvGTB9;e;Gfgk)I^nJxNx?_WKXO)niG}eIalS1XWozbCgW<WL4;T7s5XyO4;+Q=SVNv<-usjf8WR?bGN|ia{e`M(T7xDx{j&<c8`Z8;b#oe#cLvLd;^0u@4tc;;jhd*sDllDx3rjYPk&fwwyBcuumnmby3!dU2%Oxce>rFD#amxElQq;(%S0vRG@7TB0WR}wT{J2JV_U+O!m&>mHmpw0u+4}g4|E(L95})u>W=_fg2lR?<KlM-|vk34_vL@HeE1AbN=8P;o5tef%AA}CbPV1cc<~gpsqeVq;6<JI1+!{;9x1BWarELg9o*2mV7R8{h*ZGPoZ{%V`y~2zF)`a*|5uvm|W~dK3GYPw*oq{Wo*&QGJn4*LunJ#${5Pn2v1W`rge#7%Obe-;ak}1F5Y9T^6b#x!rbN68eO!OZbnCO4S{mIEDrZ>egsy6Xs&Zc4;i=q6kPd~w-QH7mRSh>h;a%d9lG4O+Y^d=ND->gm2)KgTlQM?E#=fn}VRB@v$gCo*ExHm4m>7aIsZIg7Wjgs9}ayX|1icYS{`_64T020)?27A$<07%9KCzaCjoZrx1lmqbJ7KD~)151RZaLX2GuuRN5cJs8dFARP&N;^n{8Baq(H+t-?OHmlfe89Kd>MI7fuky)h4+&T0p_*vD?CNo75{q(4u}S&U4TGajclhjoc-JgO%YPYrd-Ufa39wh4YH(|;b978_=hVtiNsAm9OOy)O<T`}9&bfmHO13k3A)r&}29@6QplZ?0N-0r~D-TevMts3)<W4yY_V+7Smsu>HYH(CRE}_~+jq95lRy6pmx0u4HB4$Yn`*~V!OCBgm5-=!~xM!|m0Yo69Lz#~UXJ)?zkuok6kf#90BybW58CX1<urE<VQ0&votHagc=!`W#nSg{D&GH$;hi-+hXx$|D_+b|RFTc3ur~`Unv73kqdA6bC)jUOpXR*rl$ZQ;9Y1&O<KFszJkD4PQ(a0z^DuhMtm!(}s2i)tMDeHx9u^eiD68Cn|l3+J6ES70xGq2)eKW!f+h7<f1711&`S0OP+-_tlF5(Tm;Qfplip4;<aHi^<nIn-_RKHQPjS9?KRPhLIht9w4)WOBH8;CGyBzy9d1erZbw0rHiHfag#jf-(!8J%r1+q=qGcUI`K5xOg`RjxA3qM2u3EV>SVRv1ZvP#zz6uz!lh;m_)=E5uk-FJ&&z+7@@9WnYAHAtTZb&>tU`z0q$8K^^$%d)RP%fG8Ob4JHeDPauu*+=}F}~;eYqah0zJe>S{PW_vLZbeS1K_pQ~2&8VN>(U*+0%)A|g?D>IA0(w~0|pDcEx-^*;vk#&{Coo$6gEi1(2tYwBjaYey}p$S{*D!_a$(jyp_RyE6L?u%~#6l++|WYmHTPkCVL^6M6Jv{vx&%p0XLn$XCES|=r$jU$HKWBFm|vI^f!6GbC(7R?TMZ4egm6{<G(+&njo`GALK5lx{%>vRTIVH7K|jJM$oZV8r&S|_X&D7s;uIw-5hnS$1apeP3E1&fwLvOFtN=j@4yWb!BzaE*r_^A0{-PY3?4R@>l5sC|HO7A(;b&;J;V51_k&J2(WxJ|k=JNA2O4^L^{xI$#G%!pBSYv$f@27Ei*GzG69%gJO2Y>eBSk!rX+iF3YT2*BFwCtCy~Lax11;(%9(P$QwsrL+36o-P+mNMq&RtPMKcc5@kpYz#k(mNSP5GolCExZ5-89^l!ta09-Ddc;si+D~LlM>Ow`s&&;mEuRc0!d}FDyp+{Xz>n$Hq`VC9MZ(SP%@hZ!kp`iS<O0a`TbD#3sH{B@o!Ynir)Bq)e#Q!7sPfQdgY=caIGKn4io_;{8wNd4lkWRr|**c}=gG$>2w<e_S54FpMHE3oZ_?Dhk$NF_rLKYuXf+ex*l~JfCiyQFSUa1wH*0aIi*RNCM=b%K?p5g>%o8ZJCdAf@Ne`Z&)EIivitxWmIz}r!}iWaSGdfa{^LZYP8Is)ujur3BxuWZSCAC0pL*H$LJ7rqK}0)GalGP=)9BFX82Ww}wgh6xDvpkTNEm)xKA!w=lUgYOQ=*~X7zdO#Zq*5ezjBP=i`*O*HY&mDKIH@M`L>QZb+KzqS0671Ob;JBqj$3mddZ`lZyXQ)3x@XxI#vqfa6z^!7u@+Oe&3v}@ZesEhpc)&<Bmdd~@7@-bUm|aj#dI<x+Wp%W^3OG!`syE$$LWdw;#Xl58LYYS8Lpo!5W9!3hw5Hs#52p+RvUgLWGrl3yKgT%8!#vn_!|tQl9xx-+c!4?lTOR~O-6g6!yc>>s*IQbsOHY8P8>?)3rI*ts5Vf`}#3e#dGim$?h+6ioQ5YP>7gvLo%J86+MWbKB#DS*RrMXa7t?=o<Nw>sKx57>nLo&xsuPSyrJc6BucN=bJtxW9<H9b#dbeB>Y`5TbRNPqcRu9!{InLB+R(}aaDJ!Qyb6wImiO_mTImQ%i%C!?xO>ZbaC9<;iA9Q|tgu{+W6MMgP^Hl@1On0IBr&GS5&g+6VE$J<7$U|?=ec`^!-l*g4~9<ybcnkHlS)|e_ojRnyAJZrft#@bS41dj{B-?k<CQN(NdFs&LryRs2rS~W_7w_e&PcbygRkr-QFNQ|xKv&mzuZW?sOMNXyeLrtYW|8|*HcoxO{(w|TC=ZiDfGeeF9K2TS9EA;FxU<?zC*pizhv4z1Ic-S*@=HV1FYE3E*0l7+y6YS6!v89a@7C<gNS+ZE??}&>}HRm7Yq7^sGJTQ3m+)h&Pm5)+TAG|_5BEGzY5*-oLEl-kI1KAo1z_rTKB;!mi*S68U$hT)K*eWSBkyjE<gLF?Y#yD4-?NT^!$`Hc^J1E3o!vxN{cc>UO0I8MN*GI1&XT|VCB9mi>+@zWk<j-T9*<ivB$+3H@di8ra!fW87wVB5F_kL8iJYX`K>$_gJOvqi|^*Ed0hR%0A<Ve}<cDnJ+c0IIT`^B!;SnH6N6Dgw9ORYl_j!1i-z3VE+Ox^q9<K08*F;zh}+V<DYwm*2=!CK46oGa>q+4dI+s7QvzJ<N8%b$mf4KhmT8kjcD%dGd^JDk|k6cGWpf4~U9H0zI(gpNWYrQE`AXA60sMLqB+ULtv$=ZgH8~2Mor?4up6SE;2?!ZNDqlY5|2)Y12)?1^GIx)?KFdiZMlZU}3iw{1l3PQLg01?V_?Yg!|HCZZ|>YBibkfpbh0Dq#0nmTN8WrdvVP-yf^NW<Li66^0tXHirJ0Fms>ul#7MgvD=y#-Qgp5A(YG{(M5w?Z62=w&iDy;dMJrH#esrcGcguiD#F@oR^hn_MTCOY9H#*?IV%PiB8)R_DfoGNjQe(wTY$G%3hrk*!9EV*A5pS^6?Jdk{#_-v+s1Qf$fZ+DU9N__mTVK<c8I$OSiM^Jqu8c%abXd28jXUI^>Pff3Y`R~$VH<~Ir8H&66VK$AAL}iD<JAb3zN<0Qvyb5+rrVmWlLcqPwmRkYR@d+j?(3ZM?h_`2Nh6kqdqNrXnAsf87>;3f&{PoIEq3=K0>q{QzV4Q3Fe1N8eEMk(>GR$Abv6;V<t~nHus(CcsK}xoIg{d@I_LFzxn&zgEfVYncZh@qVJ0Rc41QW0-lE@_KO%6wY?6mbP%Va9HV>Goh!L&nz1Ex+asIC7&e87?qxuo^H%G7#mDq5&bAuKs!<VwT#kDvmN{Aoxy)7sK#r96{AFfRc3oteveT#h^0DKTDD?HHC%Y5-h2(8HeL>7U_!-E8J8BCU)iL|Fds~Z}76$N({n2;IDVeLQ&unFu3k>`ZmVrFL)_Fi@LgC#&YR-Ua46*78F=krgI)u5QYTUH5g4d%-%d5M_u4|xW`^S6x9J9fE%hr}t9tq47>s@~m$J=ac7phq?#uWU+nWsyV;USR(!T(~@-``IfyQO>!+Vn3>72$%%kSuzL|$DkH1?#xlx(3XkE5Embn1QdiPau3y3fK^;BFyCWx--}Gj0sWFO=D=<}&<dg#;l6Abto8Et;Xr0~U1Zc8)H57*=Cw9Kjs;w@oQV?B-kf67fno>_XUnhKMWM}LJ@m?8jXJ4`$$Erh_&Z-0()(hQBKl1k>^0s%I{A4`iUD}pFz-{8@gDmW)l8JeR>ftXB3<5G?aXOX0&0|S%vytFF1i(4hIWLsd6qiNJ)`>+t&_-lx@9LrWj|$iTM%(7v2gK1I-*&)WZeG4X+yW#7(6SeN^3Lz@KXyTy#ci_&hiq5floafYl#CNX5b3c^;^qJ0Fm~LyhQxqd5J&leh4DEMqS$v##a{)Xb(8Z0&i%(9<bydZe>oRkuYcx9zoID?2V5<s!Dwnk4~}r%(9w~L|>(B%tQEeaCbxKBQ1_V6l~@^biPD@pLQ4w)_xEal{iFN_8pDIp5TX%R!+|b_L+%J2*5JmFDRu7Y8|<QAJoFwktxQJoHd1g=emmeBKUyT4af~-5(KdzEEptELi!I0+x3?8IYGV-*_U$#RN#ACE8F&t0K1(Do2b1{^C-kB$nY0mB{p9rHebc_UjKX@;nxv<9pP7r&A0zEyy|Pd>TCYUYe2q=YrcwWzKU!9c!_Hw-SbV?*Yx%EH0fwMf2OH<O<6N6WHqbG=FW(IL~X*Bgw%-`##@hA!#~mLncWCC6=_^z{gPesBHtl(l-gD>$|3`r2}62)%UEctIU6?@xs(iKSc+3B`FJjkSqoXr{nZ0ddsu2@hTz`fl@q;5H#-2>kl^Omd~!SUds*B_zH}qL-iWU^q7mDP6(ou-$aI{%Q9;e+Di?nSlQp$V-Bgv+SzXbtu&;MbBcqF)v`(uMrycBF{mILyR~~&Gig7Nfd#`7noE?9QOP!{K-OiPJnZBjURT|ZSKOJ^E(&bZKRlDY(E18c>J-IiV5W@JSV*{gOuc1rA!}?mnowT(`zcT&qQdQiL!r!R*H;NiwRID7uApMytXH}-O3mD}jFKSF)m7hG((d@3j6`p$QvO41^l&D73NA(@AYh=FcN}l}GxS=dwCyMrp%BEXBov^%-I?0y@<i)U@ygP|&26rmA87KY7x%y_9X=l3Gr-FBvPjyN3)Lqd=oy1dp-9V$Y5}!Ut|L7T>|89EWXJ=P_a@fi3`<WQ0EzISxoDbB6R~DCa)(O7s4G&eJYFWnk)1a9i3mC-$+^IpB@Har7XMEFrV&RnV1hAkHj{U~^l+cy5BOC-Y;%pO*fO?MzWxTSg_}Fz=scwFYQb(R@^yF7#?X+uAChBd^VOxJoGR_9b#ZHAD)}N&TCXt0Uuuj{cVAmRHBGE)SbPbtB@VXO8T&}dhxsfO$`WaFyiaJNmMzS_~LekKR;*z+2QstHnuI0Od7(hSzEaBXX5sM>=pK4BMIERfKD-*aKD;pMB1(ND8O;mj_`H_*!d?72w1#n7CQjk`kbICgCRbGtgH{S;Pcs%97v6|`*cRgWf=PhY;cBG79d^h2Q>}J;8axj9ML}J|R)CE>sTLx0wSZg4g%Ln|)PBbI3fkej%g-t+9$kbN8MSs*pTN9-&IQ5jzfY_9z*t550B&HEhU79h`i1C5-DeEJrFknkE!>(slbC1uTaLvREmCO%X!2B}{Pz2XNbAt(zR+ty)5%)lakO#5M*9hdGi#_W0!ZiUAkvk$(Mic~3h4mxeKY?13hjd~CC}|UHwc|@WkJCmrUnEPEJrFYx8VPX$4`j>Lsi)f;BP07!YC{K}d>Ooa=ZrMSh0g`3K&dk|Su%4t8?YSg=WQmOjfvdevY}@nuOOihF&dpBn=j~P#biVV(dY-Al6wF{kh4l1s-)~9QbGYf5B3IJmBgOmQwXu}#kO{AxNEX~S2=981B57mcGgO=63t<&6-mPY8iwk5?LE|Jlg9_ljBb@<r;GoO+<)kspEKqpaeK717;TyC`>Ag#ik+>)<o2sn_61m~9mcpPdZY=c{O3a?xfradn7GNjh3k?f_bSug82@6P++MXm0rsLM9%K86hK~bX_>NjopgwoI+RhZ!AJtgL)VAF8(RZfdVU1W_?Q!~;Bo_pZPHj<We4+?a?F3SE$kz$*@q<8JBKM>+O;ks_7rpq%DFJJL2;U|CiRhRJX{SyUBp?$aZA?t+hzn#vWgj)F@9IF4Z+K8l5QGyaA+1+%5U74?Op5AEfeeH75_N#{R8EBQ)~}j*FG1~3zq4v*xt;app6_nz`3{^cCvA(SMkyd$Plcb_yjU5%En`xfzajlpX(+{vNYk)dpR_H~fM06<)-uDw7@HS6pa^#A{02d*HGgL!(Sf7dA~NmL*sVy=f)UDC^EYPMJz$jj)OqvwdfEJ)2t)P0;&T7O+w8XoQth5UldTup<}#}bsnfP;?7(N!;WbK^8$FQPr&1|hY|CBQmJ8a3ao1gO*Np~}WvfbT*;d}pH(vCt%r@RpB(&_+q4K%3%e^-)o1pe1jf+IeED2DzUvqo9u%vO}VX3baaD5QDRIw1^MOWiq_Gg-MY8@-ruon9-sL{I*3o81nuaK5kNXu)n`t{G(5q=%v*Aae&w7f!EULh?%UcQ-sMYX)5T3%5tuc(&a2B?<tv(Evx@R$7((h`hgSS7Z=r_zXP8hy8s>Tc0jW;JB!eK<$2Fh@E^uLS>60Lu(FG5a_5r8b5QA>|vJJSQAS#V?!zRUY{>BzJ;anWH}hWAPQx5&Q{y!seBMCR85hJQ;7w#v!>g)QllJ1ZHt@4s79fO~95w+(fkE`3weP!>%z8OL)ut7K}&8&F@|JVs|tmSq4!V*Lv^#F2ejSoX{Mn2p3jhh0Q_E4_BK+UNoB|r`Q&z(=Xo34Bk?2hj5P(>v8(rPw`3@=f-s7ON2{B=+tqJ=J@#$<YJg6uU6d&<Pzoxmv9DhnHSYB!YCFXmvDw~so;+J@6Z2v3IIt9*hqLO-o)39=>mquU>aaIxPp3EoPP;35#r+!gv;ZX`oz1Ja4y$CE+g*a{O8GA&bv8$;~cng4$5$G2Fi$T4t3!%K^*#XNXs>x%SG%)2<}~=F5_dJa4z8~BujiT&SiXYe!#_Vx%TbjSI==_x@--jft%79swh15$_(@3XNm_4=>x;L7~16w@bWKORp!Qr&z`5F@(3&MO$9_IHp$N_Wr?D~n%g;>D9%XCTmFt)HjYE!Ha08t>RKN;sI*bdRUHy_7pV%a)isWyn=0t~I%?)cd?_8#k;@a@=?$(cf-aWi$Ta7nMb%f5Rd}$gs^7GCA`!Ub!+{{&CV=z3GdkLGSGQ_O-veLK_?fl|7$HHZ%c5TFHu#qOufFe*&ZMz@e54y|-48DwZ*oJ2I^Nl<vA?k)=Xg8cHk1%)C<i+Zd19Y`0}|?ErMpO!rh<G@%Yr9L#R1R@kNPAi#i&2j^2s#DwK-|Yv>fsqQ6P!hAVNrnT;)D}?7r`RomFds28ydN_&B66G<0&K`-H?QE22XOi0ita3h8%taUkJ;xyOMr5o>Y@uY+H=C_i=$9MVmMxa82Jfn*qZmgS-T<oHmzo2ahYB-gd>u=m}XQb6DkBcDYR2P(OJ>D_~m+M)@s2w%3~8#tl4Pt*n(Fzzf&hwx=|9RXQAfDE`(iV=a-VGunCP)T0Y2-GR7nl5taykuGuD6hrTLR=Skvx|$=h9MI4g^2=6hQaiXP<V%88aWt97;5Ne88-511C}wg>f#S#?Tyi7x4IY&WDz(=p=pPywxz4nz*9@n1d(99IxC3d&+ky{Rn!ivXaM&;S=&4?6ND{+-7S2Yyr?NCXieQe)>t#C<%AIv)$%}<x$?qyyqH8t`W>h(T^?m)q(5CqU#`L~so-9|ov7<*=Lv260sTNz>H=QQ{j^BsQV@*{=y00!1Ml06=|}D^cyWyh`G)&QPJnXw8b;}7g4=*eA0=BoF9~bhQcY)%@~x<@T~emACuGlwW)PT>FY#7n=^CY0BZCj(zb<<M`Snz+w_So?_jOcu|K`_4Zc?WA`i$HJgp*hYUE}i!xe3X27UU*S9-JvzZbh;mM<vT$tX!+6#HygQGMhv)n|PBPyu@r$3H`HcN5B9q^OD&_BBp>g!KhNi%Xaa^mJgBvf!U-pW)lXn!NTtpDpceWvq@Moo80Q;6Rn9zTL>-aMtqOAuizaGx|i&UVfCCim28f?OSu%|nB(wuy&0IRq?k)8lMl-=m;ST2hXH#`$ps8}LtyY62D~A5YmNk7Qw*S$GKnF9Md8&|65TN2fl2vArqqo$w4FhMGd(AYxE(YRfLp@x7=Gz!fd|iA_q-uNBCSdJ>LKE-RGIj-!yAt}uH4S46bHU5gZVy4@{!~`BFGfwJprH=C#TA{odgCJ@0h^7jX`fhg>Ox0;TVMqri}OuOUy6j_f{w}gK&g%oipK*K(JZOL{v3htjLD{grk99-qpz61L20-|C2A)s<;MJ+S66?Gp!1!qg7zAcEBYzn2xA%-kVBA1Yu2%6GW+u%1+!>9iiO8RG)*y)5+7@B%33dULvu<h9zq|D)ELH)x9VFT7n@MI-f+j19gEQ$vg;E0OG_)FcMX^u#yr^Sc$-0c?)LjlCZ&9SS28tlz3>lh{^vHO;4`45JTC^sur$?n-mAGfN1El_DDrT?pZB`D$-J@0`&EN`-9MCts5U-NSjp_Wj>?L>KjobSCL5L%pwomoHlEzkt`|NG$tSYs5AsuXc8MT)=AS#Zt7lxXr}CpBU-RwhhP+umP^kTNbWBQB%jh|wIu8cCj8+|u@v(u$BD}uep6<`<AgJ-l9^)31XEBxJS9se;bdl=zhPvi|GQ>uzWwbi$s3oFym=<c>#s}lwqJ!L@AlbxyxFw8=|EkP<ke<9yhM_htfHrqyglvsdM3#muS@bak4p01)Goab-ag^~%KNjtazOf}<!!F8)1Rr+m)Vv4l2UpUsP9N7s?LGA<(0ad(jun<^{{#}zAJB99;r5Igd}=tl@4Hnn<a&z^{P?%L#4mQ1cuBOr)rC1)%!Y=g1cago2z2=6e|QTxL03F)swQEjyH2$wy2OgB~yZx$hdPSwdVHRYyh^e_Lp56?fSBu!lh;(*PNT+l}lDOQS&(_2A0j&rq6M4TklBb8vR-x<nzhOSDeV2R*@}y<;C8K3R6ttSINqm9a+t$)wrj(^F2LHl;y$MwvIV<###>A^qC;Er?8Z|xvMO6ol0|B%*BK<ZL#MIb$E44a2~~~0EaDJWaSJ+`YO~B&xJY~{yP`yXn>_}A8Q~Rze_VqY?vP+c>E`yO_lB9#wR8gQwbQ~AUSd8O!aHHS4NwA$317Xr<l(hr_%hVv{UgGkw6fs?HdgIr)4Z}Xsw#^DeRI;U|@=E5#p8qeqm5C5a<pd*#y%qCfBj-nBnu<kuq`+Z~423(epjb!GWv6Yf6$Y`a#nnjEhXZLCnWm(j^%+w$4BPtP#2a1E&;j;o2PHuyKvraG+=Cn_V1wwA(dc5~tiz!a_<+)<GpAl4iNgpWdOS5TL}+^RSk}Z=8-KAm+SmDY`u<<SD0RM^6L3Q0kVJk1*82$LUhxf)kRT5Wq(72^ci&#bh6WCV*Jh`CUA~ZEi@KO=XB-yzFv3)j%oq$Wt{A$vW0(@h(ybynP<e^Fz3<4Z40D-{?z|x@mn&wVXOKEPO;J17Ja1%k|&3QlZ5GJ=@n>F3}Dtapco({^(br+-R*-4xKwo`OG*5#2!k+G`2=Bz7TJm2gGF>Z5IJ?7z5(Wj7iU3I@V~o!9!ST%fPA4k~^YBokC&6(N*}3p|FqCT~5m5u{qQg?=4s|gI&>?vSNKkzIlb~w0%`=(J57~6*G|-<836%I9eRb6oyEnlvUw1t^y++BmB+BDyIX7uhuo@QSaY+uiInQ@@S|x`<C0|Lde6ktDYz1fn;hoqluQ3_9mH#8ibyx;?az4&pkZzj$@P5GKCmAW+^6e>uu&wxNJhnf`UYa)|8|HXpU6NfI{N)J<9{0^0M5g5dq~{`BlkL$!3vH#WGL0JpLl~cEt<Y!Lse5CNv&d)hd=~msp2*TkWb3&k_Bno+ZQmGcJFsl@)|ALZG#Rz{3D>ZI}0MC_V@2<C~#sJk15To8)We-P7C!N^e8upbKf3>uy_J9aD);KPu{+2=|tEq$B2n)VEi)_{)r@Z)&lf<@HLRz^=brem0tHUAZ?lxpuJ0wCH*WYU4|mJ7%ravm+MHlVVTl5lY356d@?Jl?6Regvn^mjRmUXRYAc!+Bq3~kXS@oB+*KzxBx{N(JHBB3piqxRQ74+RH2a5XkvPw41iJgyK?X@QF!ZCl8zz#-5(zby<if0Rg~~dMelLX{8U9R1xwiqs}!$_2?b~VIi_at$zPB89uX6Io}6A=z4YcOIlZ}<P>vIA{Zl4s3jXqkvPb{RBLDUkB`osI)ojI7foz_urPoz0y{Q5zxzMgk=#8~UWz0HQw<l_kR0&4yai*xZs6EnEft)*cNk3{UR1z4~9@ol8SOgiYP9L8xJa&Y2WGP!AsXwbU+NAcvC=B58$8I>Lfpz`G!AEH^&%(q<6A=A3c2E3EZ)rC_6A2LiWdwo~M1)GN-Fg8G(p1GqY*Nga3dWXr;zQ_RM|s%vxv{ORJh4HR&}B<}op)l702fVE9#^ipo&)r%^Hh)+JLFOP-bcToG3|->fWFXXluDxvw)eLIuXX-B>ouEV<(LNUfi}^5di;~g>+$f*JZj0M!K9XK9Hz~l8LuO>y~>*KMynUaa)2EG9yv|_Fq=^20kzyGcAeV+Nc;_;ulW-fG^ie8T1&|{hEay<C!}kcz9>IGil}Y7`qoD#+FW8imLjP>b<6OYI1$kdnuw6667n0%4jyRoY=W$vsyV`}Lvsf@MZAmzDw`R5Vfi3+q;E}%?O>8oVW<a4+6t)(o~kohDIkL|TgwL-;|{ZPe($cD-6~{-Qn5)`nWW0Ws_$f&JW9W6!9$4eJ(}26U+wtLg)b<PHKO6ksY6xbAiF<tGnTJ7YV;y$PwoIGR288Y!`FXhi~r!mr_W}^xIxzAf}^z2M7+X^k;RIk9mkxutE?E(oC{Z2G5Tr(;*1re2TmZ9h-wV7TfCw*&zP%$TQO5_ov~t229>dR?DCQo13!JIa93Bm8;LPS4k0OOK3a~!BY;w<6=DXi@Qtxz+yw(XTrL}~NPgr6s4DB6i@X=z$$MPnzu)~iKl}oL1V;~Lxr#~2sGq0L4=HP!lvnPYI<dNsFeCCE%vRbFU_jR$i30{x(TI*bP_JxTP>x9DFTetCCEaT611tc0Q7@ILRk4Dw7uhIi!k+oU?#7$*;<Q}Dw-}y07^;Pi$pgNn14J!-ahzVi)r@oD`!`7&iYk_w2XBwcR^h6)bbP*dU+>q2{wOvcnKoQfdGTAf@S%jFO3EepDqThbDM1n9|NP21^2#~#$|mso=j#Z+j_~UUzjBVe!=K?TKK@EO@=81MN;~pOJMv09@{W`Cm3ibVVIIjphI%^8Ra_t+;a1m>JfMjz*ljB9h;fdXZjSw{BqMX(oOWU!ne%ik1ZdPuctShUUD3@6v&?5Rlg_za9+uB!ahfy!k@M?0m(H0JcB~iTEc1`+gT^*8EN<kCq{CmN=U9@A1X9ulX5E+SIpMM-jU;%^FW9N*6(6M+$(OlBPKZSommN<oo8Lv67!kUUht-)df8_#O%1A5{mQpy@ci4%RqVgJq%7RgOUdAUo^3H^KMluq|32>^RGYRM<v2)81d7~HEu+-NWy-1iT>8MmaY3MAeMqDK<7zrSPU;K<$epxV&7+=pReTL{`9+8`=_j~<-Gx84mu5_8OW4w&>U#@YHoRCC}axICL!9PMu5-(ia;$p57i;QnwyUy^q_|A2nm(u}X-ksT;YaAsf2S<02dSgydazcR->J`oiGD7W^yu@P?p3Ab~F3A8rsg-m6`H~a=dE;>LtrG&5lXowk;WAB0s=kvy(ceJ<W>hj7Nn4&ZVrMKQb2^eMKdVO1DI>}M_clE7*`*aV51K0s{@V*(QB!HmQ$&JWRfcMT+KEu5I<1kZ<`HI<GGb8)rV;`Sc2Om>H0y*?9|cB?;3|rZ0fk&y{sE8>BtNdz5@ikC9Y))_N(2i+ts>1@qS)EGM;U%Bt5x2Mv89hVrPjKl@NQRqrBqRCiFjx<NwGJoU$&0u+N%5j?+ArD^)I3rr%+=h#H+7epyqIC2MOhRyjuF)RH5@@g-%_gwKkK+K^reJIl<;yp1td_HK~OPDn;GYLbX0`J`sK@ihBZx1k#`JTas=^C44NJ4_U?kBW3yz$pZuVz^>SRncak08<$AR<<GXfo9_33p$_HR4k0{Xn7>Ej0X;OoGJ=COI-c-g#a)vL?P{u{Db$SpbKxgZ^QCFXo@nhrz7R~+B&o=tpPp<R7?Qym5r-#vgr~pI$P@+<bi_T;J+TQY;RgCsEJ0)O?Fh>xJQe^HvB|A70Uq1pMS)?iRn`CA?}OJ;9|o+&hm0G|gfi_8KCQe670NjLBTjl(WO_+t@1c+1a#+gX{0w3E4G<5hd5F#69}>Vy>*%*6Dp9k0``^5cNxCK{vVYVP0nY5Vj~JlUg(l3CBK=N9`Vps-W<~lAQX%Ecou3uylfgengHo)_<syAqb*V~MG>amAZ%socIoWCsviCa<vueFs!Fg1QGZ~9$mD@O0>j|)I09-OKbW&4$8;<XWf&RcfzyF5KrZQAN`#fcufg}>=Q)$Ki41ZafCQF$H8{#9%G!^Utc@uW;QjjK@APrE1odh%+&ZFd3g8vMFqpM$dRHI3k)Mx@x8OAJthDI<JRW%w;nHIPK3DWem8h4af@vQl$S%c!9&)EwA+dwU){IV|3bPw=GUjbWBXwuy9?kF9Zevdtha$!IJwwzoBz0oqb!pRkBdBW42TrJtp4C&bz6<2taiYv@{xO(;()^3(e(lb2&4tpu6jgr0{8bhSt0{hZx0Gzrw9ZeU=KH>T`9zs)gnHxaBx&_%5=fzM)RQZT-Q@)oJXYC*O%7zoDZ;t2!!|1oU4k68B9Yx>Ws#%V$7v=JMkZQE)q`^0ICTGR=k}{k-4W!?@OEhvF!&*1Z=C<){7w|Ty9=2LtlO6j&QeQdE%Aoc%;M^)BcpGeJw=19e3Zh27CLEJ*4{mKxHyE#bamWqjEo)^T_8iRYz`*ho?q7eg2`Qf1%@r=W{Z$jPn#8Tx1oJX0GSjr`IDr}dHdVDMv(IfZA@u3;3$2K8SS5`6sR`K<!tCanRz_OK#s_Fx**1KC)qXTf`(b+q@@fuv$Ny=X@Q0W92E>k6>wMvvTqSWRCurIA&aN?Xv&|?+;=)^KPP~P)rn$UiYUtR*IFpyebLb?@*-8M591S#J)_DbswG_RYxedjVb#Vmq8Y9ETNJVgF?M!fBXqM7h)N!=-Wa1rxjJFB0f&)Mdub7Vn-3$V$yT0>63b#Ry1irELKtKmJM~X)7mIyaI^A#b0&C8fWJ}he7{}=Apr%o!My6<Wy6(k*Nz)+^)I^~bJFYTS7nakz%n3Bd%B@|uYZb8XEbK)I|8`Ypmuz1<=VdpTRm;~UDmha*p37S^P8qLeFtRx*5YQ(R&B2iLKZCB+1M#4;85(GSq$CSBHBW0?u*}mVT=~U`R(gAE?F~PiIwb_EnOG=^X`E_jPWRHu8ND#fOYgNIz`)1!Bl3iiYrP5c4l&=)QgB@TOX{7`|zIf>jBCrjqHdFD0e2Zanw6|(rHmTDnR7we7zb<fF5c`pWuHFJLEL$uz7k&Xd5<8jx^gEH6?OgnLMrO8#-swbU)+4-(RdjLiplre_Yw$1EcE)tTju0i-%OpWJS2pgw9*=0rx-FcO6&<||xma_{9>_+W1x|V1GG?1{8O6MA1COuWm#{u)i-}|s>skR&k(Ma0L$0x<E^$~$6Sv%hU?T!G|2Ugk@x)t3$JOJ}M2EJU>_o#i=^MBFc$V@orS!s5{g|{6+UZQwcvgtw1f}pE{R8#FB74=sl$2Xu1tWw)Da5J=XcDZHXfb^_Iw6YBKE@~%zIr+#lGmRy3dQS;Lj6;WLN}wYA<~LVj6xf)b@c?Jkl4=dj9HP*J)HQe_{>R#TJue)c<pDTLfp*q6<#3{9zbRp35?1s#KcD!-hx-CgLlK~0|vqSshuT#s15EPdoGQ}=O9$XvwZ`G;bvDt%ZNs%d+YX)g~z<PcWM(Ub2`7VIVDPs9r-H)fA4j`0~(5=I#<d(->H8zd|IDBs1G;zAkP50*j}U=H;89Dx@O2a-Qk2d$vxIhuhtoU%g1<;JtbwlZ=#oVD`)=YuPj4wiE!a1?)}Vn+_`k_-m@pV>*hHorUw!Om{a$@F2AxtceAkSx_h5b-TUg>7qhiuE@>uNJIK8UZFFq(SvdCA8i>x-^@20HICg$VPfn36+331E(30ZM|927)UU6N0g&oZqR8bd*70_B^4`-qtO4d?z?%}H-5%TOot$fEMVhHE#R(M=jnTSTN4ANq#jFsk0SJAp9jFsqw=_-q6kmskzlh0_bEYs}hoY&sxv>+SA348hc;)Hf@K{?2NXQTpfRWy*Uab`}V)|h++EAgui<t6?-;z0b!sVi7TRMwliBgTVe-O#DU<=ru~<lbS)$=u@l%ah%>3o!*NAGE!s{Vqnsla?&H58X%j$J`Hn^Zl7HI$K7e3=R%XUKjoUFlwXk6R7-dMhy~7rKa=E2F&=P2WGW^oCOI}qgbR|9E=T5%XyeYf_8B1?GsTrseFdAlITPblEXNZE&vt7K@}4$cS4p|=%?Qw=unCouR3|FCWIa=3>%~K#;E_)kp=1+5F<j~8*`CZsP;-Ic(J_TTRy*o7x%Fy$iW?*N*YunI^ckxXDVooWE)PtW2Gt629$TdMaRm^QMMupetgVD(-R4XRf0T#(ey-hB|(E6h>|QSI&#b8|H~Y{UwDSMS2J$%!^^clr#KPFo?`n2NN1d!^%QK&NN#NPwdo$xm2w5k%z0}RhFZX)xjympR;=|5i+qG7jvDTt!=P|e-)Lph)`{en!viM|?`~{WTcp^@ujblg1G41;Hio@mv*_09qP0RO$`0<&E)26We^<{eHsUcHC_%AIQfF0=&{k^6=xSH84_>^u4c)=00rbWeq#~F?3~)5i=d)nfi65^aR|I$^LzTm7i&FxFm}}`(?a$>1`G2dK8A>RMMsZkB^BezB33ScWhB&~wRIfIe%2Rm?>-T7nFpdA#2cZ_(Ht)(S(!Y>b#J1OTfl;K@#@alCPK3-+%6i2o7)54uf9UdG?5+NBI+4owcY#a9Rg{4-N>Z#Kl3M3%_dMYexqU`y?;@9E`X*30{0r{S`r!xe;hxj8#dPZ*Vn-T1_>>QbK?YZ6E5kdyzVibq?O1h&i*YXtc+U<GcHZyF3BPJA1B#`4^q6<f%TaE1%w4gh01=lnf5x;Z_!M^-9*`?l>Y4{ynQ&lJw)X?aue|<URoU<0CFvEM^BClsrTL4Ha4FNnv@~{=D7su^Cb@g&-hdG7-V!L;xD7F{8`kp6G7_nPJ{un#O#d;;wOo~D{m;4o#1H>~dwB3=6o+qd4e#LUHxJ+g<eGO@M~l`E(-M`4j_rn5&HU26HV%=rXJoE2?*m8PhAmdLu_^+DeRLL*(5F#^C)nsei0*T2`bk5<<!z6vr+c!-ir~R`{})M}xYBnWsRW3{kJH|_%*bY(Bnyn8a-L#Dj5?@b(Gp!QTQ`gSKh?w<<EeX0YrYt|o!InX(fZrSy@lS*-~W-YpE;Qt(TNESW<uSQ3~{ltGx;-W-mv6Q4dhVG7dcc%YIHL)q|{nMsnQg)RAQ2<(_rjOl>y}mnx=S#qlx$$lDG;Z2QzDSY$Q{yOidP&z-2q5X;M^jM$@#8&n<SuZ-O4jAHPZ)cNn2dl|N3+6yK#B(I?u(_%O)x$I>jar$gg*;*wi)<p-t@`ml?j-b~}>$;1JMs#S{C)h+?^`B2;yQaeQEL{U??F9FLMRo_-+;S{zl#$KHYB|7mtVq2obgb<)Blai7N9d$qqAk%^9Vhc=8ONdb0aCa4&u2t3}d>bb$W)F$3&DuAEm-Rsn#ZwD)W1Mk`fYfenVC|Oaq{#Ks@MmHInha0wyJcK&afQW`&J0pI(&WJlk=jHO6>SvYuU#?oP!9V$AB2r^Wf0DHVx#O|%tlEzjAYT!=(LR-&8L1F`#LUjG%GD@=`1{CZ;<^NP4kQlE{;@Ngze8wOn#1u(W!&_DQqPN4%*9&3yjp;*%ygeePBq|zy0+x+%C|4)RFV^>3K==WrI!YgyD8f;?2wSUd&sea@z({@EN^r<+kPSw!rcQl^!wYQOIa4v9?xxjH20$*mi>@!s0t?7Ob=<OPesAw=7b$4fEh&ym!q8Xgwpg?Sh!Jw$Y{o${FxeYDt~N`V)FvAYT5vuM&V6LAy<^G;a+t{qjK(le#8(G#S%;ypn%4gCY=2`SwV*Eq@(kAr`idtxRDQ?5UU-@Ke*o)F&CFX(vn!B^pPlg`TR!185Lyo>f+6%A{ku<puJ>)5sI76bT59=vZTR!_w<iMh2af_?XvDMJn=8uOJ%`Y8k3CTkNIrcn2&8ku=C~%Of8tmB<y0xj&i!d+f(=fO<vx)#tLOeaG0AJ}*!E4X2NBjd9juo2wjZN5vx`ojdTJ`VQ`ZBD_KAOj4M2cdYErIn?eaI<t(Z1c&82b{H~^qbwPw=B+ZLJo8A(W?(XlaoEimn>)+q_at;@U7oiVo$^IG{=p-NGz`M5Lo6d0#Ro-#wz5moXQN1z!vTv~!ezR0P&eurw!r1v`tH=C24Z%W=1P1-VL8c8{e^EfGn&s<2Vta|E-|BdPp68;@GBulBO`AVKbrD3Pw=Bjnvx&_Hc$HaZv1GRBTw<8jU|i^!H>4`PbS2bEnRNrfVngmsazMc1{SYo!);ZhO5C0N!09jw*lBOi@no~8A~a=2ZU~~LLocwye6!dq71J5Ra3?V3EES$~K&pz*%0#QrrPi`ywEAm_Xj@hjya5fCS@Mao*wW%@)=cEpRZQfC(&$ZvrzqHsNd+`PZHVKtthlAfldgwu?s;-N3)I3{YRPnd-b?MMu{IJRCgNCTs9&Lzt5#v{Wi=OHV(nH)z+`)6R1P53^F!6u5RUDrSIG;G;|1`_Tk9@`tn30q!BiMlKtGq>rY|n-9IB|Qy=%&<uO$wp#M*nyq=)odKh8n{#gwZ`eKnb$7RBi?9Lo}!uMycrZtk%-U72a?@3Sg(e4Lp3QbdLX#?^?-((aE0Ww%cSW$R1H^lt>h^$)&{NA?k@Ydi6{mS_8L#TUCF8tt+#R^1b%$JH~1<ZEAjmQ<ax2cw^5xpHhe<}yRb{s!!?NIAoQDQgQ}-m3Dx@-df)kJp*xa^Rfz>L9tHCdBA@m5Fl?Vd|lr<X!?<bf#{IYN-WST}Ds>J(<5ocnEr3x;p^Iim&Y}D{pJmxV)IZ{Oky8W)7}JSjY-L>TMx6{7x-y{ad!U`Ei@ek9WB_bp&5*bPH;x1{R8IIkL;mpLDs!d5fF(lfwmDAfHREk_fU})zCne4UF-!#cdUB%ZtybgMIj9%CEkk=9E04*B*tgHK=D_>2D(zYS!P@vA-?TftE1xyY;uR2oW#!w_RvXVP{GODkLI%eGf=0THJ=PvlbN=_n+)?BOCRt>Pmm(s~2WmJRkMFF`2S>N@X^eeTh4NIO|g3`p}v$ha$n%kIr$i`KR)XRCfwyjk|N`nl&7Yhkg`4kaCaJfb13fMpI=x6F(q?3EBn?8ET+Q+l*MXN%>&s%=Pe-_`wC`gLbZbV5nfsqkF~fH$sVHr>NzDs0}|FNE|f@Pm{;2OKkQ|zQB=}Vogg~<-tI(@zZ;||KNN3yQws1<c?n8hBgqr!+dP6OhzKd%?<5h3UwwDyFSfC@;qTOwiFqgd!kH~+GK1)raCco)gSRhNysqHLD~_UhO|f6&KgA-$^pm|)m)r=q7zC{UTV~r2I~>E$@`cmN|olc^h8Cp6sk&dkY{}6hK8jZ8kTNoUb>;z8?6>ob%G*QOuDO#>&Rxpb9t|`wR>+#1wT(JG*HJ7!C6-KNlhwr=Sc-V8#d3ApkYicAjG|pUD!U6T`-9Sb*cDSU>zqw9kL4zryH+|``1Z!A&s~=c&KC3#R$Ed<rv`2CGpRBJ1v`{h<~f8h2bo<pjMrbq)ubKR_jaXJ2BH)onB~Dq5yre)Iyk23)+<JmfI2F*Nus@pj#8+Q3Y~NXg#8u)TU?|1yzhsG72qM?dCM67Ol;=ECsfph;PG~R4ltNrOd~Sf?fIh%qaZl@2N1)V$;p;Qei$Jl=G^i;VY;SZwXIFK0a!`si%?Bol-oL)|<4B0aR+?6*gQ$K}C8YaXS^-nREvhl<hg{He{V%p+8&Zh#=y=JT~l=&lW@5kWY!rLWCDiOM(jvg?U<Y?k7n+LM*5f;|ac>^6UrLl99}fl62naE(zAdC)=<?+JMtv@NCtC$`$Pdcb8WyxE<;UoJhvxrYJJ##s@-=6b*$%N=~Z2sWNVDQ0Zo~luK)}BcWr$3vh27gWdo3L9$LSR&VBRoiAYme1#yfbK<ewle977tYM;AA_EBOM&)mkL8{1rw&tNYaeYkyEtTTDHB6ieIFDPuC7}$|*)EX*;Tgz)#?Z&sI!24;Ez!Efb(&0Ex}p)66jq($I{WxcQ0F%Q(fNCA<`z%=v$v(R7=xu7MoR0`NH(Z*GM^HIEC2z!s>YS74wuL*)Xba|`DoK0xj`y1h>3H-+;Xl}e4F&GL}o!a5);`rt;%EEXdZQ9wE&hg?Ooq0g989$OIb{~Z!Os~Sqn|A>u(?*HZ*3S%j7zGgpsHQrr41!<nRaI)6hy#_#KCKhxs}SDg|<lAm|!NLV_`cVsz0vT!$7QOrzh_yyxg5B>-a~!VvmjAY!4P*HU#ap)W09EGcVtr+zyvE!F1s=H(SzyuArWJaf}qFVDho6l9xC|NK`l*pE=N2<)jz{3ta`o4v#~CytxJ8u%+I%QVu293$?)VCNDo18o{+j4TcDtto4maZdH31JW|*VyWZWU`Gg4U1mb}4aYKsJGi7k=JpLKSlA%Wrkmn)uoF6>h76$kPr4tG63Ug$?B!JyfoYjVnG}~Hx7__m$t{N}x7;v9yC%0R&C~GPLvHz3-cKX(EEQ|0#2+=PF|(8ls<Bk_uw{m?;pU5K>=3NmA_~;jT0%~#*wuL|_Kta;a@xQ7)#qU^8V>7vuSwW3>6IcWgf2<WHYkiu*n~0t>Ma?Dtr27zNLc4^v3WR@YXf<DbE-XC4Tn9nat$rJg;mFzGO(lnO9qtUTVkc93CQLr%)L{ac~>hcq4o)TcQpgs%y@-vEg?W}w<Rn_{A^-d8BIyBc)ys8GKo%fXoVxd=wQQ|A?yj*Yga#Nyo7)Fz1MBt!B{vH_Ab<IJ`gXVXo(W?@R*+c{i&IFqFi&w<@;Y==5#9Gc5}w*^ce}AjtH`v=8VdT9Yuj%Re>9*QXL{JS*1$rWJbhzZTgO#?!pd+RQ#PSJD0P-e9=|%qL3>PD0fyr(?2|qrqZi<wc}PWqD$(teVpP+1yGSYMUz-(T_w=U1WlF&!_pv5q$q)OIPl(Rmx5w|Kztk~2$~?gscI;b$j_#Uh^cZbVH}uKbYf!=eUCHlrYat3E%MUU=1G*Yj64-PoslS1CM+3H%FY9?XRs7!XjG_|6J*NQmQ*Z3%Eo0m!x%(&Y{0kM{ie}6G28qyS|?4%H#1tN4L%#0EfWoP38lbVSho_xf)c8p0X$`+o1_$OS%Q#kgEuItI{tCCOox@53+rv_AQbG=F_JJiYe%}L#417K>i`q~)v?R3d?RG3(S$;~Ogff>=iF$5I?0uySOpMimLoCttjx9QUlylD5`mp&?!?Yy31<;hN9Dd%$}q_hUum6Ylug(knm9Y>cs6|<7e`Z}d7%~DNXh5<NkZ+f<}sEf7N9ez4DGoVvDfrWGB(DwkSh6S__ga~086awCmu-K6S^lU8qdx3x-u_#v_E~jJo|R6Hb9sC+a<n8?jeumG2&k6*nb4yf$KksvQ6a$olSWqOp_yT$jkHdw!CFpJEQy!-)oU$T#cxAYjzKxgX{su3l2vczC?pN*i5sLGDXtNg*P3A!F~9NflB6RWWd>OS=s{W7h=oGLL89iXdCR<Sj#JCS{T5sha-InO$b3re&PWhR+e5&1UKWi7~7~Z)cDZ<(g$h2?9f^CuKnw~NBh^?(_m3qmSv&yTK_t@nwBl>d4k`B7%lXS0xM14Uanu1XGlALhO}!QX?(iav(BEkd3|%`g2jSlze%Ig^bBc701r`G&7%G3g^{9pezAIfxMjK+^dzH~cEs=SzmDWYR;4c@MGs<gim8|9{4MXk<<JC&EwRID|Aml#XBW$}9q0}ZYCU3^aUJ}+#UOVL8e%skI8SkC(m>ptOh%cTKRMCPV*<*2l=WN!fp6`7UMC{(k|dss9URDIQ|{>tA59E~l1N{+82BjnL?t4S=!F68hwNeu;Y$#D!O3e)IU&OG2S1WfW*J02q9!PX6Mb!4;F;L4WNOrb?5OCNA27jLMTz90qkjpnu9%z7(<q3V%Q|(D-ejOeSbvF(FoxKtI0q;oV61bvcr)@$ECK|LMYaX0h?@H)>k`Q6;SOvM%}W0zqs?a;1r9E&glyL0hOjGFh!jTnw6PRgVkbcP(3hOqEV&v6H8Vv5(iv*>d<QQkwX~D%rabYK8}*x_hV|tt?2<`!uT;cJU>f`Z4YO4_k<fHMO|%+|9_ZA_P5OaHf6pi0N>Dz?#AB<vk6v7h<@?IL{7i5g!k@q7)|o5%<Q7%~e7r{~8gUncd)GUL-5?>k;m>jnND4*-EJpTAI)rj-Us|q*v9*OW{I0JfKKk2VSL|M%SAS;2IZ?~p?;4*^04pJ8zl`0%C|P57Zon41b9b}Yy|MC@L8oXFr`R3z)J|FItAG`{azHMQxGB^JEpQ*(&*&PX^jFM!QyFMru9^w6VkugYfZ9Z>Y$R1fMS<aY5Fckj{EEH&OU#NqsES!p?y)k4fsc=g0^`N$Dm4`|3TDs=-0|~ho&jXvUa;n?Z)_<4seg(bSSEfzdM0J;7Buuju@OF%SIU$uuY6?kTNYZnIvH7uMiuX92blC?Fwjv1tdTx_b>fp^Lrdw4o|D17h(Cn7Fp^#^0`tX<)S0_{7Qii|BETkCJp4+WOAE`iVKgcT*rP!YUnE*g604`uK-0_w$9lG=eo9}epHjvNhOM$+)EAe@LKf5*LRTcr!U=`L=J(G&Xd$HO)G>q<5QH~kacG=)wM^fyY89$hFL+=W)uw8A7RDGe%s*QrVn6#m)!(^LnrxwcWi7UFE{xY)zwY!feMMN@<^&irXRp4P-NcG~_QC0A1+x*UQA021MecHXFn<aoR~7%_*jEdMh%lp!76d0wS7_t2)Taug#2g>f-p2<YzxV6Y9`N})*3ewsRp4yL2F!WFHp|<Ir=B~=ZDU$vYDq1k$0DuFxpSB-mJ~3Cm31FewMigSmVIwjVwvG$k;U!^lbmQdZMig23ZU@EVg-XqQKDrsOEV?82?&cq4+JJA#?D6Ze&AcH%9ibceC75KKuy7CTZ}z1kF3BRaoSsJ|H44Qnr{}VG=K_Mgap$5$J#^gmp$bEhi}nC-m)}Xo}n^pKGLLac@>`R2f-T8Breoo*CT^aqd*whLc;eVwZGsMlB5km>zY*4N#Kbf2vZP$vRXfY=;2Q~bNKjB>t&fcDhcf{Y;X&L37&Seo2^ycsM^%=;UuFM=@`Gu5I0JhA#MqZuXO&Flrw{E)}&M)Z~@FdMAljH*f;b#%W;j;TY(J>jXUglSRy9;NG4=5rvru6Ddb}VJOjIwEaj(;y9PV}O!Ja2uic?<X>9~P495T3d#a->eX$GR;kWd~=!lI4*q8fasJ@o<87*=MSU$5(7GeO19M*OkMUNfmg^~F_HhxxmEmxRWXO~f!xmVr1;!2JHu|8D!1=Ej>UThGmwKBvS(}<4gk*U_IW*NB(UiGCC=QM3Cw9?yJx6f}>`=%h-p~3f7G{MjBubAcLkVI)nvmUPMe^@IO71bto;M2AW;$2qqkLGxG>qFdY`&hJ980BhH`3hI;SETU*Vx29PGj!Y3TtT=IG4BK|Do5{fm{S0cnI8M1-p}A{&msS9X33r)AOijn`9w&@uG6V8O9ZPkIGdr`+1QmR8M1)1$8Z;CB)@wn;CDD<S6{%{T2M^q@C{(O_yg{Tekl9YC<jrN=n>xkLC(vDdd-9L12(ZYN!baPjfDhBPP9oLeOrvw0XtWTbmEaEB{CAO>C&xft%~c@4B?|P%%Hv~6M<c=!Dfwo^gf`R_ZbQKL4ZurCCrf&z732idLGl@K6Bwa0|97MGVHmVh<It^L}-Awko)H@slLcQ(YsAzVY3%w5^XIao(+=JZks}JjsRx^nKP5#iFUla)yqw1uo#ftOT@20CneNUMgZ6ieTJh7^S^0Ep)9X&J+GAdNGl~Q>=izt)-1)AEpYiNz>QIr(cT%^uJ@Hss3%{&%JyRurE02-dM63a#&nx{fwd-25evJU81hO8i8Wl#uqzK?#jw7uosxV+Vo09#zb!}%HX`b6SZ?nTov&9I@TTq&;KQ61R4bE^8`%InSqOSoUyCo;wDbbYjsBYZ4d46{dg})IY93<C%sy?HY3$L&k&O-mEbS#?hTE}L7Xbf<3W{UIT*3V48+O9y!yxPxU7;SOehn0riZ8$_XQ<Sez_qnbjLM1i)wZ%AkbTJtr&wBhq{YgG+y~Y!;Gq`(-wya5CJ5+#Mope<UcJ{?-m7l44<ro|1|1{xZAWH~mWu;Czm82u_{et#bOXUG4p>{D%J!5~D(_Zi>yOIV-jcxEg<s^uT^%Y9P9~om$PS(IFF(QU0OQ<Qkc?8SH-?$~*FThy7SgnDA*59XAX_VP<$+OIy=rLzFQuv$Zn7gAOv~51)uUQkv&~Z!`tejwOTJ)`Gj~}|i-o}uthu5mK(v{QY6X(8SD|`VL1qMBRg`46)YYQ&-W6#rv>!0HHmYlNvyLxk{p=Zaw`r5?ud8eAJ}hwVKYoi~5x3ZaOaKO988V`zt$HRxeO6gFp4l*XJr**e6+@CWg!gB*=64WWT_?~jTga$6wQ^E;px4dZD)UIJ+$q1o(w@3aSf^bv2hzfzl8c<aJtdW8ZZsctkv>UyNkm}W3tIa2+o0IQ)r%+K86Fvn_qBo+BSS;pQDn<Ns==k8C{_ewYM>LBO+>2#0}wcuoq$%9uEdS7UlILd9qTllXi2Iblx9$wObUwFfQE43M$HShXtD!b+7Ys<<Zldr??)fYtAx)5EN`C5v)1{nm@m|plw2#c4O>#;c}ogS&!C16KC#ng6hpLMCK+E#UVBM0{umkVb!wFUQq8unHQROd-hHjvu9y8NeN!FyGoJBY9r{kisUHn$l=S<rw%vU^Ly497@?D?4hox1PQ*q|u8*iB(?TUL8qCl8qCtc^2`fS8T!uGF7MCUrXn_}4pxWqbm#oR&a1SSs;om&r>ZhOEjgt!9JQ&p}3Jmr((w+%tkKnVM@P(`?E5z*@RVkqy5yHUP~3|K=)N;kDa)b1vnVc=v6*8kjTYKS=z{ygUFfxx^>!v~yH0>q!GP*{hUD2ZSPq%sluz0q^Pf%>hlt3`d~#n64RMSYuJ)}M~H&t-FZ-_jz~1WV;2Lwvq$PFD~%rkG~6zJ%}#{pr`5(;eA_k=uFO{`Aq2iO<m-IO|UrT31ZiUL@I3xvO}!OZ|x!^}{=8fqvL>Uo;h%v?W&T>sJ12D~k^uknK}~e}ghnSmoH9_g(;BIiGH~8|Uw+{Kp7&DgI~5f045(8T)P4$*FLjo2Bd@2@?mVRCoM%*?Y?|3)w%?CbzW-eN#&ekxjTUos0kBN<iZ;D?>rli~4^9>4kdrDwhwgsYj(;e4H^ehT4-(46z?uaMOZDPUz&zjE&$X;1{hbX(LgT<x2<RPmLU;H!6Vm94)}wqF!!fB`mc9bhlIlTthWNGrf5~GyUIxas91z`LfIrJsQ948O*3_O!c=D6HGrM9?-aC#kU4-{ZxEoH^8pb3>CmBCX=K^yri`LoR`MW@f9n!6nJJ;(E6tozmskr=148R34eq?Yq~Uy$ZtuI)0bD}?MS;>4(hYvB0}wKC~Iw1cWN=(tHY;}>Jf8u?8y&1^=crghvj0EsAgUag?ca=XKysll*l}<!uhwO(nvcO-hxV_S@39_lXG_QoOX;kv9T-EU#8C(6{;v|M{Nq)nxU3j@{E}?EGx?+k~p2vXG9gaMrO`azKnLs$(cx5*3>pT0UL7V;oOOKh_1OYWduu02~=+=<TJ92hG3sqX*MP*&J5I@pDdS|lCcd!x7N(*H}i}yqpD^l#l_BMy?8Xbu>jN<{iaX{BUwgQc}D{?dzUxmeiY4}tY@5&a56gv6E;-J3}Gjl_e{e1U$@SR4y02^#vy6HoV@<}=iB}HI-XzmpRXhQI>N6b{QBqX2*1sr;j8&Gyv4`!OWw_2%VodopYO?qc%7*4acuKf_g(qNd2GXrKbs!?^F^Qi@fq0Q-|5fr75$l?{U?M?O`yg8oL^NiScv`UU-0MRcmJ&4O$%EpxNQD;#?Olfk1xLHRO;iq@Kdeck{Qu2-q+WY{bC{{^>^(}8fyJgd&y7#xiCxWHu~ir*oZ~~CLr*_?@dn=iB@D@u9_a$4ObgSf_f|25{c8c*81RT=Y7SZdFx|fW1kZXq(Hm+M+pQSKmU~eg$dK<W0kcHyLx1-UzDp>!SaLW=bZmC9wVNC7)CI<eM)NSmc*K!ZTc6zcrC|!S$yd*yDIe$t!&VuubrMAw?iaFvZj`LK(yZP#qZ-QmcjCiZ!FLB{0j9CU^KCdMmLTB#hViHUWjRamtAK^0CsdI*JdL*zihVEpS&`iYWeJ>6ffF|lLr_4=|jBm%KSl3Ulgrala$W$<3Dx!G5PH(2HtFfv7@rrL1&)-V%fuJEob9f`hEV>3r`a(KApeMe`4v?*NwyD(qZ-PPG7fo&ps9W<v$<!r4H%YSNPexXE&Il=m}0=w@<~>3v<!E;J#+>zRi_C`V}FL%lY(X&!4HkbnoX6z3M%mzIZZXdU5=H{8KiEuaG#UzU#v@m?xjQ@QSy=na|I~MD>q8ujRY-#>2IbT%7hNUwZMy`IUq#!+UwY<>f8M#h;;G_Q@;r-?cF%+gLCCRIA@uAz38O|A_mGKL4Wtl07_tYB>L*d!Ssc|30a?%IkO~v=6fSBvrokA45#ReL;EvKcw}VQaiUPH+FFUfEwl-FpW9m_o1lT3Tiv9*%Kw;P_?G`0{{VWJW?(DU`|C%0-ao*y<37z`})(*eh)H%_&GoZBC(4m`N~HgOjb=5X6vEN&-mG&{hYlUCJeXdov=zzLM{9xv<B5cQe$C1-16t(#PMT<(kox7pa22%w}1DyF?jAG5vE$PPWYTFc<#EWn5!VkN2JB(;JKNS{6bWWcqg%ypMdAWMetmJXPHN0yYv{_$q+0~@V~7^#nQ)bS$_s4Ixp{~5|Pb9AM#wvAzvy%tDp*e<Ccz@{ZEruYQSf;Xa*H(us*3s6a2`EbPYXxG&4IdM~6z`1gS&J<55$Q)$dU&vJ&X4G#yx)j<eD<sWeHfkW7*>jX&izHCCWr*Wfg$M(u3pvnYmZg>(|I#d!u{=N#t;qm{C)y*|vEye)`hJy?~0`H&DQomkwa+BH9zm*x7!&!`a&S{5u~$6PfX5}^=D_tS>0mWU`Yg0+~Z83%w3doz`_PlY9u2|)D5qC3{Ko!Ta<-q)g_O__=JxSoEa>;cU!8#g{CPs9-q3JYp0popnIJP424f_Y9`UL(np3>0J8Zpqsa(=B^h2pYkp)kjFd9mrsc(b;3Qbt2bFP9bb$D<23L*<AGCfMd~&KyUP(Eko$}lJuUFFaR5j^^qz>&2F3CRq8v=m(K|w$7NZ=U-&t1@+p010?10Ch}P^2I*&t()gRd;-ZOz+oQh95#c>%>$i|xfn4IWk+gZ_63)Zi|eWg%_2j?C=@u4cZ?7h8?Qwh<C&M35mb>c^60BL77kHu70vh1$}f7LO>Gvnt!<^Gh<-|@{I4AXD~^CZ{<LwciR-_MX_5STWX2fmw~#HZ7Pwe+POCqgj2JYe{?WM^sEnRi3{FPHA%(&unPK;)K55I8_7(cP7+zem4QaVYYh{pg;YgKQru7R~eBkAv)E;O348byKcngY&cFBygPAzIU{StA=h4&H&9v(ttEHE;Q4Djq=5R7^n`9zIn0%rWQsth00`72Kx_P5U2bEf0{Vu{al<9jX7no9s&g{kFJUW#x&|v-s>=EegrV_VLy6sh83eeB{7i4ARU}MQvff=_w?1a0)!paFAN7Nm>Q)YwY>Ltd{%m50I;QlH|24BDL+d*8M>J}Q@Dh8kl8h$C%mVC88(ZLVE}Opw-)YY_JSYoJzY;fj9@6awr`wF(@IL>M*!V0?cQKU9ytrKo!xLY$C@m9!&aF8^+WZD0h9gG1~Km2+@+`Puzu_g>(syr-;wx0uUu4DrHG%^Al59@D;M2ibQU-_W({JMP?ZQU9vRI4&y#dGyTiE25Ox1pcUWF_hxP1OOwa5N0|x!=@z%R<hA2oGil6_Alq=A=Kr=rhOHOji;tY<OrVd|FTy94!DxUvB#RAlHY__B?*q9tw4C|$e1u0W=q(J?wpEpteFs?|gM5>pb)X3P(CT#^$=|Rjgh8|5D+6gha_A#11A!REbXpHg+bxTYKK0363$1G8h-}k<U_L4ft(?d()Sq?47bvK2HbzGgenv$qh5*GC|x(zmI3@w$VL_h_wuOEk&ebPPX2g^k?>f58zN;xi$N-GVKk_UPQOjV4dD;B;R?rFKhlh**RfA@!&yYD=}iMRN~+;v+%ge?aqlDf7G=U{X9!o*E)Fl&jU=BzzpP~njtFkj=XwL#fr-C{VqG@Gp7a{un5eWF)(qvLZ07UD^_MdR0gp74+hyXf_YN{O-B&192FJTxla`a$BXw(&?~L0b;Hr<8>=E#)jqD0(Lw&8yAC-2o<M(57=oVKdm;D6X+fg)t$KUBecn6$7A^1)#JRL8S(?ShUL?2dLnzO+>4V;2nEL0*N2mL5y*=`@ekY-T>&K0?<VR6_)_?|DU}#iM4H8&x1xa%QaWI*V=pE^Uk}k^s{+>eu*8WcRENk=+U8rB8rAlVgXjH1Q8Oz$gznL#vMDcWp@&R2m}RzXdodah(a__B<NCvV1Y2A0i8$@J;wKa|Cq%p_TJ~-bI*B}_j^bCu41ma<{ER1fBePwe_#AhKM8rzs`BwY$%AURtLNlFT_JMR-d88-*wI@MubH?t`l;`e?6t;dW-hFbkqT+DnjV*`(K-4O%1Z_+OeFaeQ;YmNF%bEpdwZ3pWzo|WvHB|R(URoxoo{-q$EI*1;XEx9YA9=-Gc*SFu_3uOBMbtK0=X*kgWb%9$iKAfFpm-w13U0-!T`62sR6`WYA?or0rdNF34aRlR=vmNG)J&PU<!yMF@Z<5$rI$DCQBxaB3b$w(6(z-*)a^CVSNtC4cox}sMtQT-$I&H>S%Im6M;$lX2Nu<a}+y(;G~uWc|~S^f!HIK*`uykZIlC;z>vztW4LVjJfACy1&2zW=GcT*q-LqOv?_(U;D(p#Cvpcka)``Hg4GfYeUJ2~b{H@zU4kq)AGXHklQ(p7pD+zUf{b1=na)1-Y?AHFDh_rw%Y#?97Fco9B{dzUel)O{P;OlXolT((tS3S3h07k!T=otbqRLCVU?M@POV6?i&bw4qROhrL8<MQb<WM!0<%2=(m9EH%Vqvt_+kt4PVG3CyQ+-;b(dsFU7SmdMEg{Sr(CSkEYKusMKnuo9GODAN4A?Nq)CVzdC2}JAqCgpx3@m~SYM&0QVl+l}B14Vz)iCN-k^^qhq!z~B3mcGG8qE}yjB%561u|ZKQbaY?)T*Iqp=COdA=JII6NVz&8jViU7ap?iEOOvvu%D@>Hd>{jAU9@dJy()x3li>+siT^H!TlBAE2{m5Zy&BW5kp=sdsIPM-O{`!4sl?bhAl3R3MRhVf?#6Tx+;P7ra^=Vez*LOdVpjj2{_N8A}eGYsv3odfe~N+l!_2-_8CJWO*K!2GsJ<3SfqiOYHCT`-h}+|ICS|`WWUb)PQnM9R-%Gvo!g}_<dYA$9!TbOAfZ@OBosa9d0B06k_K{>`LD}nE3cZo6q;<+hrF2d7HP)N$%_tdc6lQ>X&kSiMz43(gHRdj?LKb)3-=rg?j)zOFLJdB7SHBc_Ba}JsBe-sb8JnaHWJjl!nfHnpNv&}V!<t1oO$=|1rjOwnmjg}pyDL>SAwx~1a`){Lfk3_VyP+P+xMOfYiyw+iLPb6eVYD?^o0N=I!5+eOlqV^rT8Mr8%7b9QAI`ABWu!{9pekptIPx{u$De7XDj7Uuk*X<b)QDdA|FpIm5T$)Wq2|4vPo_B`uNXIetzZS$GvH|oL_%1(l0wc+Fw7ay_}B&la^31_=_J$52>H@khI-Qky4RFn&p+Y;A@#lB5_xu_)I&|y%vTwl69f=bksvi=KozvA~m-qkp!k)C&W(DLy|^~n(~L;oX1O*2#RprMfG&Yd(g&649PeESCmIcQ<leXCp{!f>m1o=tTfaA^CRrEdv59TyA<<gbjGu2RBH;qY&Ks?s9DqkbKRah@Uh(0<U^rCEu}D0sotht^h&0(*5vEziZfrANwFYbj7F3F0_H{011>4q2i4O``PsHvD}{JQv0lnNwPdVWgf8l82oO54b(18Tg_~~X^JC9%OlG6u#(tJLR5bJ>$Ibq0KXNGprmLr90bRvb6Bhc0oKu|OLCAs8veYGIP;qBgvViOfW4@r7=L<N6;#s~x+ZjJaFIJNXRKXR4$5_qs1)&5TzGMx$DPK^F@VFxlSA%?kO_tS^$cd0hv1EZsbcUjoThat5u^X*xefJ^FP2L?Awnj2o-O|=nvGzAq8Ur{k7b=a>e#g?#fF+AohRy#A6XPY?=F`;#0ks;rU^}ZL7yE*P=GqUgx->E5=2r|-RYm)un#+|htxRDHf5OmIOG8sr1(`(XK%3fho=NekAHf>g>10Kw66%>{iL@+qnv_tO@j>zWs+9t_b3UkR66InS`_!nGziwJ^;&gp4EjW)!y3m3fShJRAE)r*uM8>u@Sd!#c;)-e5nyjE2)H_T-VHtXHOb0N5iZ22k{wQf-c%(OurB0SfR?r-EIf4;7#Z;_SUf8^ay_3xI%F7jw+2o1juz`jb@q3YM<m9cg#FICdx*CNUB48|{Teny2E&M1@&qKz`nM&J;+>hl!7#}cctV?F7$WSsc6=DDbo5d+spu_hzEhRcv6zA~i4wX8ojHdFXc{cX+sq%_w$rAx!76Il)-krbfKY5P;=Ok|d;@#4P^Z-$$9E|mGAs?BSaxK-!ihLodBsORoDlsOTd?bxX0$HC|+~I7S=qN~+inilWNd?^r+sMFY3NB2~Q|y%-8&p8!!Y7ZU^0I@;zbkQq(R&xUZ{9|>aSD0j6h4@@-^}75#sa#%Q=B3_$55i1a1k9~{f81kNcoXT>Yn0Hm^-tGBh4QxV?ICaC<K|`>IGpA8uMBJ4QC`VCAK1MW9v90C@z`5aYelq27TE_KmL<9vzTofnrTu{iYqodYQI!+H+*|g@{&-;yz1Y&ZF1WkYAQ{F&(cUvv(UhaV>0hD_e>>b7XSp!+-&O|?j^(qD9e{;Z#)r=nytVil9crkrxMf#21O>xGd=leC(oB%i&{E+lS95*Wlv+;DaXkiYAZe)kcb54Bh`kW?VvBvmh|&4%CY1R<;#3Sh|wbq<Dk^-iQK0=8R4}t9$lVlTi~{0lLz}~Fr<xk^`og=3cZEjWVjE~x^gpIc>riaDHR5KW6drcn8}pn=aBc#W6`~p2kTMO$5-5!kjqC2Wi;gO(oS0)u>`?7yQ5+olV^kE(bkSD%-|K+W_QeU@|6@!c@)3qFg128_MCt1y<_8B1lNQ?eTmq3As2i-HfF8}9;~rjv*OiCbl^({#w9AQEexthq2S|LRLqdL_iZ;t#RG9+4J9?sB!a7@M6fv)Co=N>;s+CT@5R^m?ATiy_|sC&H}ewRoLM}mqy&q2KKy0uvvqI3^ziSbp!gLG|KI(1xrkYOFsYAJG5PB-q`(j%ww8-9hId8@A)LuRu#BkREiT4OId|T`irM>T6y33{2IGY+)aHOE@dn0n0|QC>r~E@Q7`pNgtMlZ;xsdxcwFip^O!_UdrrnJFj#jv67z(UPDBx$I04}~`N_VdKMl;Z^EVq!}Q@=edf&f!4O8%=40{*K{FfqSCJI1I%;*H4kLbmFBGB(~S6*n|-1UfGTZDk2&5V={5%JemNMHre{j2cUf>PP<Kpgi!o)NHztnpN{fb%VLM4n+e|acSwlXkMr`3z9lwEB8>o^v-4|09_Pd8g*v3FVLCYKc_Q`5%`}!#yn~+RL@2OcTM;V^QgwCSkYDqkQS$^t81q1##AyXG+e;>Y^r9nsanpacx^VtNgquv7yEYR5^0q$Z9Qm+Nf#<<mp1N3Ll4c|ESHMF9Xcgo4Q;G{f#2172?P3SmPJLTMn149sc8m*A$a{<?@pu&M^)t2CjA=AnSG@E#_xTpDLJ5t;EQ*f0q?HlfAKzVnYIe?`L#|nQ!_u$`CF%%6-;bCrm5eoOv%}NyiL=NDcSha&sz9Gh0YC^H0_#?h!%G4`iA?|WZY5SjQ<GQnzUB?JcE?jk7}5aDwvQw%o>jxoQ<Gg)=`H01CRrpwYx^>9sI>~pr>{>&dMqrak-j(Fl}6pWnvDc)9mAA;Al60|C8vvuab`+q8+k(|8_{fa0aa%G6kiHpK6DcjZ9y(9nw$jkVdHSA}xW^4ynB0*bynz7OUsCIwGHGhuqBDA)!ZMR(1C>F#GUnbH{)7J<=jMx_CqqWS!^Zn%W+D)@+;vI*^&lllr7Or8UCzM`t|6Eblkk$T*klA=Di{)$GHDT>L?`25vM7eLUe_swu=1gU340rX9U@YLTZZ+_&W8M$Q7k!yV9PwiLvGAH6TRpjdU`Fi6ZIZq|ULsLP9gMO#nZDrLY8lE6(hPvnQVuiUT;l71W3q`e=sv&YSyA)({h0RPPonVDY^i8#;9w|d3W^2nU`(q&MqKuOE%fLIoih{^Lw*z4QY^qvzAOD0GOAVW>uNu|uJhX5cHtJJ1M4XeO>J{q@bHBcd+kIX!FDXEc>(R#%bHfWKIl`^)Licfx$D@t+7eotxkyh!Y^r|=B7IQ8R(S$=+*S0`3d;8<6PiAPB;C&KEA1wSNCt0~o=O24TQH%A^2-1tGw5`0gO2E#D&`B;}J9emm>iDjv_kf%oc^DjqubtA%SmFJp3Ud+)5;Wa>!7Ynil<f>{6;ngOz6S2ku7-u%_J7f!ppF(sVH|+Q)xWGjNd7)n`o2d>t+<a#BA>go1QreWUZEJzNAn{hCcP=&2rW@c|Br0f`1x_v8#SXp+9Bg8~oB_nVls9|@&@q0|untwLBhf}#u_LK~xg68Vxbg&u8JiRnK8W9f9~;-idF9a^^de8y7iydKm)!6A>U#)A1m?2NT&6vI;i5(<rN?F!?-IYw^sasH>&C;7@8BZ&&g9s<h+_n0<PJyyj8va6Pui8+w#3YNwZawowgC%>61w(!c5x1Q3<hkENrf%G-eEIw@n}u0`Du2=<2F(0AV_?1;HLK$@&>HvPzFvyQs~)Z{dc9-xuao3etbM855fU)^9g1QH=i93Xq<$FLQN>|k?IpCsEldlE|{KzC5+azKKb2MHdx5?wM?V+3GlYOoVE;7I$7X<1r5T3ufJt*-TE`1tsZI->I;Tzm*Dyg&|RokMkR&p{u%`Sog}h%#iCP4(;9aMs}khcx9v)4l2wQxCxXThEtPkq;wQqS<1mRqC9c_^6N0g@#Bdn7td1x?-j}CoClfLgc?@Vq1w>`=RSn_OH7mv{iJ0(JH#Rczi|ln~7EBonl9&Ak@&8JW$c_V<$D3`-Et9Vmc3P@l<@JxwXuS0hnVdhwAXKleO=joMxqsgeKc$9jpB^~*xZ$807}Mu_qSh;?o=*|mwJdt%<K>W{$&R!Ed3`~OCm*wSs<_wMObQoBO*H+z3DAYK@f&l2I8js$QupbDbUskVO=JP6B`ZpE^bLpUARJ)2^Ng8NUHT02RQ&v|bc5ubp3P-{WW$fw*4$7_f|08mhH90UG0mfTO+X!wx4wT;Z#t8|`IWn%>*Sf;_>JGV^MWHN>Q1icqpiIO)8>D_ss?z_s=S#^@ilQM5vG0c+~x;2Y<SZf{U&w4)A-O|rpuB2E1T#I8__jaYT~`?4e{;LXH)+YEwq5$YQ<Fj#z-M(d4#gLF9LyiF(coC&*5&fdyJieM?BuCO;kn54z1<MO*CJY{R$>50Yj19)gC*Q_?Ox|%gPiFWr~{+rm0EuAO64ws;eH9BtxhbB>-MZcz>WHCsitk!e2r~+3R)2DA04O%cQ5n$#p{LaNd!^FIzm8H{G{iu12*H&)c;+NmDwDo!^A#@SC_^lU6>flR(qvOo6pU(x8oJMG{q~7+kT%YEobwOsG{U#*|EfwUz>F#X6rSvMQM9)tLfonklemb5!N4@9DYa2U~+uVe7aAZ!U#bN3FRvvqUxIT4Vaz7x_QgB7NV4h1v%aGu-7xjJoA;S4it%#SPL3H)ahxV1i@B!e{rh-`UVoQzPsS#x0dE|B=C8{eb8!slDkAJvD=%mwBq5!cXX}Kru&_6a;TN;S8vkgf*PvY?}%DU^$nCYVj~aTJzo!4v8%mh498YZ~?<mPYBW7xWWxK*ji0a6j6au{{@@7dmq03fx0wT%ZZze0&m$^%)nrV4aC#U)SNkt0H9Vvu2|o#i8sZ1d#yi{(%~rQ1&o}v5URnxpY^~p>QIMq`$UH^8)IM8UYx?d&emyaeLeiR`&T~>q`RI<r_bZL>qXtPl=_JjmP8BCA(CU(6jHPCB+BgCYh~-<qG-xSP3pq1tAoh75zo!6UO-cruNRf;?F`J_-Xnu7BzGu9)6p38%c5yw#dPN=^z}b1x{jZfC##>ty<RqgEo8BMs|o_qujg3GWCM?^ScMF)2i9>`Q$XWYGz3e*!_L{3gdK?LZgrafQ~#HsiNs^m{!R=IYNzB~@(}cC(iIX1o`<`9Ys?W8AXD=fj_EixusUGyh#L!5`|hkvz{ZRNJeQp`lhoUc83I|qz*J)Pzw%{Z^Ccf_Z75LeOWmj%R!52BMHW!wrDT}2)k~#7F(nX3MJcRSPRmCD{#V{GF&`tX^&9UEvp$e(=-H(nmLhnp@Kri8OkIW-66}spX#<S~uJ*ACZ`Sk@W6h8h1${rltg-c*O%>95bO6}EV+)?MMm#&ESC_`vhh~jXKN#3LjvZk+$m<83&?`*j)K>1*wC0o}Nkz{o8M`WMi~6JTY-E>qDmC=gU|mltD}nCiB^qIW%)b!UNQvTl#ix6OQYbGFZtMdI(OPyC6I&&wEd=w0`LdRPvbVoN31cU#q`((N+~wu7)?;&{3cI0jFbfH(go1QOV>hyxagXQH^AtlyYK0!2uv!d-*a8-2U6csFk-bq0d+aPz%o>m*R0ktYN>5jkVa&sz))SZQQ8N~^`QyCV8!=g-T`K}%>M5Pkjg2~AtSlB*IQ$$VNG*L;a{5D|u^i>kMvSGOb#l&umtkx)i$y3+uu0|HXXm%t(WqbM-MmB1vlJ4>SI$Z93IiQ!z~gL8N`^0-f8G4!rFX1+s!*3Yf$73{wQ4K9{Ot6>lHQ*_+s-a~cJY4vX=Be?D+KH~&h|IX{-)WL%k@p;)rQhGIJVJFt-NX;X1jc068GvZ=0-C7y-(7JHDLo@%$|_fLVdxWu&r2#Ewt0jbkDE>m1#6mQuZp~X`)VOO`T62{1g~v*GnoL+?^m56)X-mYhNl|B5&uush(~Ulo+2~J7UdK2s2&LZq{n04Y~!H2KksIvX>yYI`EDSBkHK6$E6LL7kpb;7q%Zqn^iksc8iKI+TE<rYSml;33S)XS)aHM!vFF|_wQAbd<qwN!@nmi^{RhAuxUCx>)+qRMbgFRg*B6l-_2S!SJ+(_0Lh(9yzw6pd9a2Py#n_!=DvA_IjBktq~uCYe<D1jIQ@5W`v2yWF4#@Bw){nDfOn~Wgb?Wo)XdH|<Y>spmV1(2;hOh^xqB8~d}$IZVQs94_(D557FVqV8ShV8!)a1{+j*<}G-`a~l2C4;C2Tz^Ol_S=Kh;(uz?ia&`6I~dfsVorg7bT;Wd~|)0JXs=;u~6Bj?&fE(Cuv>1V3tQO^%`fhDIbs5{xZ$tX4OuQ5nOEw-lRg-(rJmNZrt?MIwS2$$<Ob2oY5Ew$|)C;9{M~;dWA0P{2|Y?mgj?!ScF!eOTd+>E~=R4EcyM@Q!5I&cun+fBi)!!iM$Er=!2~&@U>!+ITS>o&#j-Gt!T>H@3}L@1rWO+c7bRG|wD7j(TUyMA*FdF&qDyEx5JNIhcmz^q2*A?1Qvgi5zt4Ikei9keVfl9#>$T*lywLOEa1;<kgGVEftR3;*s;NV)6m%itRm+cQ2VmL%VN-PRfyV4<@NH{9sM0jfHu?0doDs)O-KfOVfxySvoi#f!ZF9oHa$jN09KuzKQ&iN2TyUGl{fd=d9k8&zQ&NfU*Jcea8|05)6azfYc#)H@95CZTNlxJl7``+;9Ml;T`71fur6s|ELbz{NPPK`6IY6v)Rv&<AX<M*^z<!FMhlnHnI$=;5?ncCVu*SL$fIM#R;pjn~_pup0EnH6IS^;7TK!&aE)*WmCR)O*k+lns!O(Nd%-)<U1qBeP8~4HWuZv^TOYDlJCD<LmP8m$miL=#hBCa`s7?E?RW@3!6wjzdX|Kk1ZDA(-#4cKIipfH8(OmszN%Gc=P1`jE4{Bu-Fit=?)6qqGwz5WD2?K})$&3}X#?kOqsNRybZmVgVR*QX9sYpZDCB<NMAFy6=dJcIe2^Sc4t+g0#W^LS|aK1%rlFJq;U;m<+`;edhXJ2IhxwVj3f{UBdjdi&N>3)XmY_WrOA+)Kh5dn1XwOi1}p553+tBdO8mL_80-uObwtCr|)+L2i5@I%oNpXVCeIZeA*J`-oMRvinH9Z+<BH)i4!C>&2*Gr0b(uK+#v>^O_+<PR&_TTa*$lZcCye9+$Fd)>M*bZC7~b8uXMix+!K`_cB6Uv@tiQ5}Db>1+6*c);2TJp2>J7W4Lw)3i?C1$ZK+H|mDqTaT=CohAXE1C}ZnmTT@9{e$J<K6fS)-&*nANcaG=y0>nt*7%gMJ6R#=-t<5^Yr^K(918PtG;Zh(wyYR=a6j@#$5<Wl*#q~wPzvjjrK?ioE&;6&c=r|n=M(1N)IQ*Q*-puIezMfCyayF^&>wXQRySg{t-ZH)r5-0?di~zyh-xbZp)>N);Cj>F^e?&J^3@MO=eeSD>+i98svw59R5#X_+@Sv$SRnC^GqL09w_<QkNH{oYI#_L=mWN-yW%psl6;6bXkU5y{+f+v}cmtbosAlOLa@NNJgKfN3^MTu`QZ34g&bp<Urwp4l%zGq7vOqqEmZf<XgMAe?I|N$!?j3k5-V&Lb_c&>>M3XRZE55r^4ekNH|JRAV!D>Ic!T|@^K+llnty0yMW$CKH@<WB-j`sQ2-+PNYy81dlpEwn-<;nApe0GbQQ)e%^NVek4r%Pc5(5NgBEVl$G&YbaOdVIO3K_kG@;~cr9^f(syDsNm#3E43{Zd@cF>g)4ZAW2@*<3X2{ZJ95urQ)d{w=!{;VvS|v*=ke5JX(>CL_OPxQKo$?Y$xld4)o<d_N#WURz7^^Lv((Ir7PIYu?$N;@UCRmu0j|TV-R^5IZaB!lO$#VfZCqpR<auSt>BGde6myfe@SfQy#<8Te&z=znI??!RyIo4DZ<fKt_OEZps0cXzp0sW-RVrp!@IR!q$Prh!A1#`J6J_qyxU$RIi>`1G;O7PSa)*w*%1AGyE7YV%YE$yCC+g<ZCT=2t|+U1+#;r*5&T4QUFL%}mad#tp#oBZlh47KDu<&}X?I(i0K7COO1V>R8&{)Mr*v=GNZkV3%X2n)YH;m&n<*@JDp`U>D==w3W?fh=TP?_vBVCVTF+>t*YD8~~li5-D3LVo)tyZ{)GKkoz#_Z_W6bk=?Vkl_^v5lT-Rp0=F^0DHtFP^747GYi=*vtevZT2lmiLDrh6d`D2w8E8NZ2@mEq|Qe9veh(YEJEj3oEK8ZSUdYeKr@yF<faxE>AbX`B<}uSK1pZGrh31&mbSay(<1FPSE!P2_q4Q38s13ua|&~Y?udszPxf;n&wE<xC`n9BBH<mcCHpy-!B2iG+25CBzekAKVN%<d4&KO(u~^1rKT~g2I!pG8SIg`*I7Cv(^xu~9y4ASiKRM~qU&sz(o<yr3l<tbawB!+uq6h7U`Fhu7XH1X}0{7-Uj^uPq*`r$JTL2k8!k~|Ek86TL0?Ct=E~@Ea52W%hbhq##56;+_Q*ncZv1VtB)Bd<cHaMIbr2krU#^s%ys3sqkZOBIPO^XJY`yB4JAV#Gljp!|(_mR=>kGEJawWMWQ9JWuu<!&sE%)PQ9>J==_xSyLsm{SOFkX=bE%jajCB6bT+vdCC%VCgow&#Vp*^S0QE8q6eNT==Wm5cDd`N5WjmPLj`D*EtTss2@YxCAOc$R7vTuO|?Aps8p8g@<iSmUQe9HL=Xd{2yERJd(9vyZZM;8fT|kuNjt*sw#+ek?)6p*;IfGzu7k^loCZ;hdDbE)G=#o^ci1pxA)GG(LU3nVI)yzkW6DJk83TuTr_Gl+ki?xs4Hk6~S)o7>_7@?r)$~&JK(EPCNXJp?l94s-$U6YiTjG0|gmdEXCY~Q2MB-yM8puYV`=Npp3F4oc-RDx*ol_hk>ym6TVr*3<)@d09sYrsiqQs_Q)Ee&HgLbap|H=xy6XW`asqv0H0%L(Uf*R|x#+w%X--wd0mw6d_js$oDa9rO4mR^kPaC=ti4Ms;hTK<80UuOADi^nRxH_d(<j+Whr6MRwN4SuZgvWj09@m72(Ma7?~^wyYbs})Tf;~W$LSQYo<l5*h<Q#T3BV^F1QE8iQ<I0mXBXWBb48WVo5=J;LoRfluFD?EAcNDAkT-W@parD1={=97TvcH#GLeR5KkFGJcmaTcUlr)%^VXpg!{f3cXP3dGF0u&KK6Q^+mHZwIF7>Qp^ga!FIQ%+sgg2y{<+W3--TYq*%LrNrQ>W&uYS<e}7TbK&L{=U4;*%2roAly>f+cxLbl-^FImchQ7MfT#N4BfruAub;%V&HiZZzpQt=eShzk`;IlTd_@lK@ZlWX0dq$<maovk?QVBwuRg7V`@8NpCLCmXaBVC&$Tu?(<Ucy9kGc^Xmw)mxdyol<z~PjAN){0YrX0LAsAD{8Llp#xlw$3{xB6@dBg3CsMN*Z-S6KjmND@4@ZZ!lQwo66UQO7r-WQUW|C12A4TV*s^mu@A5jTtHZl#0J7NJ}M#ht7R%XV(k{kCsx7NO{s{iK5zPx`*W{;x9cTd+1(@x6=y{sZPC-^3yZBFv_-*dsDf%nz+`|)T<nDd8(e^F#u@j*@<;OnheEApb;_q$n7Y)L<zC{uKR6Y{X^`ou9-@xMhqSrE#jbrI5B(Vsibr4>z?nb?Hd_m2hzr)rJhY^ckA?SqR)eg!`4Nw@ho|2OWaY*G=D|U*3kU_m0Z&NXp^m8X{rv!Ci1o-PF%%p!4L$_)B&o`G85fb61w&*NqBbfshO198B?yxH|0-!eq@Q<OCHh-wYX`K;WUF4Ehzt{qecVk%at^1^5i-R+iOy;5>>Y8#5w-0eA}T$i_Nm3AbrpYX|Ev(%dXd&4fhbH0ECL{#?+SI?JXJCbGh{S`!^ik7=-wSJN}nG7!~4Kjd+PU+q{$t(dZ7ai7>yX*;>b0zZuDn#$@`~zYq(tcf4RmtjFesfjiC&g(kFjq*RfmY+DjR@FR280I}_zSc%RDB2JA0pRtq}3i#|0YwbAqfQjo<=_W@Xsa}kx58$%{OZVwNo*U2V!8OHr#=SSC=o(i%BnddB`X5pIzE|b#0qnT6pLb{_#U(I=sc4Rr%tHf{NeK)0>{H?OWuH@C`#5_=i$o+kEX-c%Z1Ma66P(zJ9ZUd&*O{m0X9+SWp3Jr#j}LPLTNrHfE_YX!Q+%Z6DrTiwRMwfL2m!lVml!(~WLpg+K;9sTTvF;ZUl>thq|m0^2+ckvg$wAJy_UYfRP|yY0j?QjTZ|%fHd&#>FR4rQN$9Z^v!}IqK9VZ=vbWykKs2X9kqL-loLp+9s7wRRK1g{}lmrvhnHiDc%%OYDV!mcEfApNZFRDlQb>IHL9sHGo5u_eZ*fnZT3bStN?yQI*@gocpTD&o-o3_hyT!mN`>dEb)N^v`s**6bN!C#Dgiq<m<uAJJ47g^b9m4*sMMBpNUvcgvYS|@=BOyUaA;YiBp))%bNlqCTu6;jt^Dr})-jg9O+lrUif!ibY$doAAqo6-}!Qsx@Y&T>4H9k|GR|5q@d$ZF<EdMtdMSMewx56%8R{=sOrxJ<-7+i8J%{ZoXVlg(n4cTI(zn;8wYsU+DcxFI90=a=iTpcXdv9ki5=8I5|;V8KL&C$;dc)(Y&##abbq@jM0NA|xe;`HX+jnC^^bcKwmqW&NMPWK4ee30G$?BhkCa|Msl5kjkZA=eN>Bo_cw1lISDy@3(+@!l-ZV)e0Bh3i_Jdn}Y=!gMLi{>TF=v{(!t=jsdNQ9KeH`WbuSB!HPXnMoloPdu%GiTL2t^;POBW8f;nYT&nCmdEp@W`etkT=aHk_6=9-HUOh)^49xd-PlO20f9H4J9TT}H9FTF?>HfRMS%HXjG)b{>d2sgn>(ejx^mRPH>Zh+G{5ry~BmDaGb%ejj)9^u_hWGw#{XXy3U&S?l>8Bsbe|VjxA8~B!5BFX5ALg+Q@BP{I<kR>1>>r+i4gO0#4Ik)f{o<!0fc3Md^Q+R+@m>EOPZy8<iyo6ig^z1Jc*)<Z2ahkl*Qu;U{_?Mt9AjZviS{(8WEV>%+fR>`Y)N%_9M1oZ>@{QrGJ(<H?@1V=?3);L_#Sdk$tYz}3}$HpMPf=~fqKS||8OOZx^oHh4#xdUK~+~+4?R;3NIclTpq5#G`LD3zN-lmnhPl?oVT-5L^|Ptv%e3OIeKvIE#qr{c_LBWmwsCglB3&1`==qhi$}jE&r*<xl($=%hSM_KoX7}*`zT)PiI{)nX1+UZ&<VWuJ`5@z!@lrW+#%o?&r^Kc7Ge^cQUoukTWgkhqX+%zo3$_P-@rs}Qis>heUpn0dscp@!;o3CtXLoJ()L4jo(F?Kf8hM8J666$uC2^xtxvu1N$@{>ypc1D2)$1t0a~*(g%U+MOr}`__t;snI<!N~k%c)$ocxC?A-+oKXSXW+8*S~0d>iqQs>~HzK{>qOE#_)3SW9?IM`Hj&%eZkJ39}xV-Mfw+A_I$KMygY#Dmd0KF((w+8@61kR&>45@m}!*!^x`-TjI?ZgS`L^`Bpsj^$G419tsIt&F1ma+8m32&6L$(d4dt|p69%ED>};1m=hiP>{JMC38ia6j8r+;7vjKEhzcE~Y_i}{8#Q`Z68lc6P1S>Dc>9F~5>2>eje9*=-EbdE~jY+t8;1>_B|Glc6!9Kb7)6P(dZ?2tTJ-9RNj5Yg~!HE%y`Dd{#5}p%9+@y}^nC=L2Q%`GIK&gmmbPgbwPKrg+X$8A2a5MvZN!JCTQPq5_O*K^QA)nC<ZXnyBCw%tcW8yJr%-Gsq1i_1JjO#*FM}g#qXNK;I5iFRnMWm9=+<C!^6$pT5gml(mJ9;-&;uo<YLmvsnKbnbgEI!issHRLqpxY*B@2+?;B(bsY<yS{)SfhIbAQKH#j8Z;scwvG*g=Et7Kr_7-T3!n+uPM~mr>`UYI>N6b{90&vEwsEAT3!n+uZ5P^Ld$ER<qt!l<^75x<x^K)OyxoK0jexxS>@$bmhpoxsj{%XlK*Y7Y<x7yKGSF*0hCo)BGMsj@&omo+8=|dv!7QHEO9pGdluRM7nEBtuvcm%^`b_iq6>KQrV59B&{7)9y35%s^QWT#+mqFoa&kZW74{LQWWCikG|&CA5)&4cnE3})j4>4v4VsN4-`z_0R1SwrEFS2sc<rA?US*Q=Ur}2%Yy9nD_FKlg;3QWw-j^%aKl{DG7YgpFuw>Jqwn>}RL=~pP?1059_KWnQX(C+wwZqQupk-HQ6*61h^GeKRfyW91i-9WV_iik}l<$pW1w~TW(p&V_cII!Da8$pUvbwY6c$}4Uu4Jpna>cA{V`YZ&H29kZnCrz4f4vxEPphZiz53R9k)sq~{4z6Mo(2<+tiNFK=85YGFSyz(Z`Gx`a8arW-HYlpH;XjU#oNWX%bR|6hNzG>s{}w>>Z}ao%eajnxmAW4-@STa*Q+mMq_ZqaO*b?=c{gvDXRdzT6Q6o%^=0fhPvh^!#J*B@i5Df7aHSY_S#eqXy;W!lXN8u({YChZZ_$8mjb+?O3rD7F%JG7zFkGQ1T#)m#7qB}RCn4E5Cr(0R<{u_DLZjse<0rd`qA?JHmjA5jjI!KILjH*iv?a&QI-pTf1cTxOT~B>MWP!)V$7X6V3VPcC-ihEEv`*sW_if=O5T8yr3G#5@Lxd!Sr_6LfYtTtuj5|=;o{<E`ktC3!)xNYa#!oJ}^3S=y?uQ?`17&a9M>qUYc3|JdR7L1@k(+vOhWKdr0CD75`>1;ku9<K=s$t#KnOo>-TTxe99qMQY6H#``?-;KJqxF>rph<1#SGFNEvAh*N?^yL?3+`6xCwmZ&27YzN`Ss?AP1;(31m8GHn3i(f9h%O!YNHR)I27(8#f8`$f9IqHkQYQMbO}j<s$`4C<Jx@3;mB4<>F8R#k?Q~B4+;kjXg{iFXlTYBQAyj~>QE+ktFJx?6AkTri~`?GP0Fiz&)*AKjMSkVxpb3tD6gKQq48i<f4)Pxrtn6^hV{E-`Yf~PiL0Hn@@{PY>(GNp{V!Ya<kr%H*J>yI!N+V^{ss5%`Qc~W<0GbC+__E*{*ijk6h7?X%Y#IuA?u+;NotY2=hquDzqC$psYgzeC>HZHy6QmU9l3=b_9Ppmud6W2=+E=CYA9Y|a|%k<=>(#5F$>gUE8l~+ta#Q|RK}I8B$-_F-S5cqK00f6zS8aGa7tY#+(Q#V18kh@JH((0KE!<MVZ3|^+R&0H>2(~O$b!8EwS*C<JFV=P{>+Eh`}O=m^@2wv(TFMAQCG&HI|^0;Ot2A?p6jYu^^@@L7LDC8Qip)r9$2egeq}YS>Z1Cq^-LQ$)2r&p6bJkUzBjLF^m*P(&bQ^7?A^hGrRzRNv<>ON2GADfSMKsXJqSU8?NO?MXh!9oIZzU>Zs`{ww6(6-JT;&=`aSmxFPEO~@?1TU;C;=W`XG83S0DHbVFKOIqP4iAP_krnwrDvO_`yNeh2k+a84mI*4~V0~VH3pt-ji@%GJPjzMD9s?DFVjYRA|G2Zmn2q^1S^f8rY#bE%x(l3qO-UJkS~Fc|Sf%D;Ym0?np-t+RO!;@%*0_j&HzZQx~#rtv)4PI^Oj(|J2H~F2R=aKYdlr>Ew#EO{<CIbQ>oyxCd)Br%U7al5wxb3^hlRV_CPH_SG5V9_jWR>Gm!d_YgmWg4{#-J6=};Y`D>rFNdJHQTmB08!|TQa+t!nDw2S~`qN3<T6xKXc?qOS{(2PsB56`Gx@+T=$`{*^j%LkGqBD^wDdJFum!#PwZGo&?BXgBE!U#!XX=;+Z1>Q6iR4a7UYt7!hpgDat=c~TaobDIR=^w=p{aMY&`iD=7805=1x@vHKPgmitXv_($ls`_=i%9)4h-7sPBocJ7En>MRZ4{~Ohsw9xaO4VvNJj+?jz`8JEy#hH1>J=e{SEPiftJRH`(|=-JO!j5Niw@5ZCD4{8^k0hGUDLgDj;dxn-;^LBbgKSo{>$3jQUEtb~A<Eqg#CrCZRv}23}CScb`*+1Kc_Pw)-7l{S0o)T9SHbeur*F%Z&}|=o^TYunG1QInI;f2+bXC!~oloq|w!qrQH$I#d*!Nt`>i2mHmQpsJiMCKy{KHOTgsW$0dYY^4yywwlgut8Y`I6Gw>oPz)^!(X#}?+Ri6+0cJ@yP>AO;l!<%&CG0>zB<b#M4{n+>OsrJrrW|B|FML<F>Z~rvrd5glYYq@21WJk(_2^4xw209Y*!rkkEDi=+%Co6B>of0*N8)UL^|FPIf;M&mj2E@AZX{D5fA7!{1Gm8H#g#Yk^o7ovv%nc5ZF*f)rIY0)etxnd}f+=SlAkxbLrP*9nFG}Z{2A0-!D~7mg#yv)13s3byPh4R`!UzEslbKVgcG_MiquLdtijaWo@>GJ2n(W)D!!`?Zn!oGL%LlBb_{*ixa4F{tJIvHmyT%-(xe3MM>GF1faDFETur&oTOPE>;n;EY6bYC7Yr?ZpYkq~1zNgLXc>Jgk9+q^$+uyV3Hmi^Zp7BkI3(=APvwHIaME_-37vI48}KxU`xc?=Be;t8L9q)a@9eP>}{zIEUB+FD(_!{cp!e8*+4yV_vXA6B@}JxRQd+KBRb_D-`S-{5cN%X@&a1(!QQDtJFF(?ir*&aY#Tz+}B61xs+Iq|AwSURr7mke#Pfwk=<h=lY45`|7$XF?U7&qGw`m&gSRC?%FsG+e;5dVRy~r8F|zGkh9RJDkYs12^!`-sj;gx6cjZlCaA}x_%U3ZWKdjigH<}6Q2-k8urDC#`AQ?j6X}N)9&puFS6ms~y}qIxD}>fvt;!2&Ch3wz?bV)2PFlkalShGNLM}d}^6F7PoE-kr-@bzi>oaU&t8@9w5@&yEN~rW-zQ?rfND}tbwDw!-&KftEB$Jl(V9DJ(3AvEad&Us9XFUBaT2FX9A_+^p+w^sejn07OIPD62VD7D(Q-U$SLs&cWesG`)rxO&KWYRaP0vaEf@#TYS(1Qc29p~3%$!Csnwht9|1Tg!AdwRBrWW#JK(Z(H!R6lXTHk=fQKqc{|sU&^+26T`ocoI1r9_LZXB}8Wmcl{*ovXY$#5hA7%=ncgyhBTIIdsv13lTV_RA7!LuDBsuo)v$eF<h^PE^YyQ8u%?4%t_Xsqkvm=Kifh5#rDQJ|)Y}-tRR(p56{Tx*b&BdpZ(5;jV8RU44Ku%ksf$8aN3TAwj0V}O^LeT~WGFqBzBD-jsE|)ZXM|FglN%y!IfZv)Uue2!D6hLDi#X3nK&8oa#ZU$j^kT#+C0Ah|Z%%VjY~eOFMj$=MV_ZH4yK*e7>@)GCw!K&iS50cQ_|)v*7(^n4@+qqtf9H#`GBT`WxMb_&jt;<u=S@bmnTOELEb_Q4Mh)|tiHvNCvhh7z4PtJr=Bc_#kN4J6s7H}J8R%&p;F!wIZ1gz&S@76ZveEqBk+zX2i+l)e^q9rCVW!7<&0o4D#shx#uH-MgNFCiNAnfw`AuRa})E1_8Eeyjc+vTnR5Jq;#(IVd>c&r16+<p`Y9{-&CP0k1@>Ku{7Y^}{rGb_9GqIq|aH6qL2z?Lvf#+^x7VoQCD5qBQHZ(#Ou1Ilr4xoz?5^4+{I=NG@DS9Wma^=@ta?I_Q&e=U5YBAx3B-YC3nn^4H#W)J?mt+RWZ^v`eHbT$-JQy54K-jEzVJGLmRl6+dxe;nw9GUb{0)kv4N)RP_HLJT_9Du|RGHJBD%Y*FmN;w#T#_R)ZqVHEkyZ|xZjcqQ+B`jgMAT+$SGF%8`mI>#b(wOGJ=djDnJHY8e~$I4aN!ea090eLJ@<R%$+v{ecRp_AlC;oz?Mn?@numIRiA3RoqNzSmM=qFb!>NDy{774-I`*4sm{1xcPQD3D2q9R|d#xD`hctwX7nxlClb5hUEv$6aN6R3SD^c_yx1^>;Br3yC%?(y1sA9N5G-iV&<)-6Hjhrvv|iZXd<|BrG1%sZ02taz4RC>nqCMQybbBU3-c~`jT^&$Y5Ubt?e*~H6!9@Wr3Jq3f8X3Af!h8s?I|%?4eK@EEsyGU)|_vg7=%yGF5PEI-^LUO0k-5V%TEatat<!6qK_d-=veLOY_BSqOtPFqQS*k8<tP^YG9`cQg~t!4V@4_9ciG^HaK5ipZ}eolaMfiE2m?M-m7>kNXBmu$U?4V6P72p#}pPKQMkPouYNo6Y5DYBT%KV(Mj*7{u3hsqN(MNUBQrmS+GY3)hS1Rbe=nVwNPI5mW<>`7%4R4MID25~Sgl`9&tR!x>7r>1ZEz%ZR4!1d&-3niYr^F}32jaNwo*zU`KcEwF-bO4-;zWSBGP?skrCRJlCmhVFG?7}WXHVqQVZm(>U%kDTQ1nZdE*0tH3gUCny}Bpf#3t(t~AoQha_ru>9gkGQK|4`Q=9W>af>K6K?Mc95{uVp_nBuXwmQ^BxNI>OVp3MszE{!_(T{upCMIz<wF@u3E8-K(8{4~bf2Mh-k4TG(S7O&--$iEN>5?i@am)@2I_LPm@v69s;n9ke^ksId(jQdRcP6Yb`=8yKytqH3M{d<N7f<~A_$wwFat9|S(lH5Y)b8m8Bqp7sc09^??2reKn;iSnmFN-_NO+l5qpBfNg^}{)ovxM1cWtWmIwbYPM|ao<Xc(BBw;tfIH`u^oi^aj6gNyv*P(7hM0}3Wq2B4i~wDLz=sLZkXo{EbJJ|*yPl8mYtS>y=Iv4BAnPnE@R?;&fL)>IbGk$vTwK2?>cH2_K+3B@D6;>WQdX$e*-bpntvX+(cI`=r@{{-NcOAkmt)L#3kX;N<fq)(NB%l~mTwTl1ZSSBj(Y4?ecqua6?;s3*1GF)#l-ly1BBli=7S_3IDrS+!pZ(bG3+3FLx?vowFh6~W(hRq)sQ{PRb(yk1_qOvxzwJICPhQfY3U6Z}P<(=$6q#Lb!JFVmY6is-#19tSrU{|%f8&bucCe<@o?Ned^05mJkN(fnnRV^GnQuK7^o^0cEpqxPGRT3N@*UO@*z&}W*zwZan?_&#cc@_Vne3$L^buMO3&PhUs)b%b9>_?33ym3HBkcHxzF;gxpbm3H9|(4>83UU+3*_`u8yNcN%eB{E4%Nnn7>T6DYmp6S-uSW=V;*)zIpK@DF*!C=7AB@2W13nB(TV`BF6UV3&5`B_K3@iOfEj2HPfFN1&nmGSFBJ$3lcNtaRQ8(X;jl7RWFt6%rXUn6L!N>kx@+BvzyjM~7@XbY_KS*Ve{TD6(-;@8Y+8vK$udwe=FH7tHnB5>r^$ndhcs6{q0{Sd>oCRN@R<3A1K$k(9O_c>)l!>lR=P|rvu3X$-{OfkLgpE!7$LXz`aur~NBGvw?i`^B7@I5=igaY5POXM7EQ<j-y`x9$~&Y!hKHg_(Fx(BR#ig?G+C{1ib$x<&;ZN7jrRq}ors^(3SAQ*;mE7M;P2ZaKIcJjdaz+yB;2zIwqSKJ{~+U}t#x-RY8U(3blPLhdvA0RJ3Q!zI16OXp`8$r}8OMcaqlEZV^?d(P`TvUSX92(FVoUpwdcO1MTyF~7*GlnOTv2>vz^!?Wjn;@ua1@R9{%WMOb&Vh#68dhF|D4NuZHyoj~oI!X3F_0sNuN3=envhqlz&mFoahkI0d2pvIVDqCFgD}JqA<z%sSu#!yJJOE&uA3Wx*VT+R8P8AV$-wMk?#J;N^!e?s7X1i@Z$)VKL!X3Gv9gal5V%`ysto^X>_Yi>HmHB_fyC~Gxy=T+BYRh0h2~}wpK~d3a>FBlxF*ruD&!7Jr?k}UF1c*QcJprsKnq~?132EoSA%0+U*G3YiEgG&u<LU$Uu7=g9w0HHEHPV`0pM-(}GI!u;u}2Pr7E2$z>;fGol;nDJIrK!QpfMTMqOiXU4H}2TS~}?H62Z2!@?H`m`NwRy?opl-8HLU)67Y?y2z`k}R^<bZHTsY8@ElPNW0xSIG;QUo1`S7flIF`8*nkcRj1*RZBbRU<&!Q;iA3)EpsYzB|v9!l(Sp_|Lk{uDle~iK?NE|{{TmVs{yivJ^^tglg)*H4nHpK9-CP*O<a-b8kfO536&?T@U+-ONP>}<ohdGrefb_WG8eyO5w9o)gS95>uW@-L-4qyF-X)&_KH^L*uGy?5~uRdYd>n-ekKsMN*kWVOWB6_Jp@&X#r9)NKD;IJ9i)*#pMP>c7y>1gBX^o9DdaTgh6Rn<2jx*2!AZCqI@Q#r56PeLe)kx#4y1yE{%y^kPP-vkM^i)98|i{w==+Zu>qT-vPd+4zs#6xR<&<8`;^0^6kOeY<u!M3@z%M2GlO9DX9x@Isi6MRt+jkA`%z|T=sxA9xviBUmir2YF&7nXW5+-R#eTW^p2Ls?bn}&?VYjG>`2~!oeG280sX99z9kl&Ra;`V(eK^O8sh7N1kqWQCw`CjIV1ypjBr~)BiRh0K5*hdREckEwS}{oUBUIvOAbg+ho^a6s6T$<qv0xoJ#3<o<U+)ZgcX1#G^JH$1IuDeG>ntc|Dq@=>ZVM^>`ELoEIyM*CIb5{Waz4}&&<1Gk|DR7qu32ts224ETYJgwkDGSL7xVMrh4^XrNEVpx5esRbf5eYv<L#uZ1XhO{bI=wNdN2U@814yXAQw#9g}!!svA3YfbwpmM^v|cXrS+W?JIr9jX-NpcZ<Abt#3y)h5YEu4>l1b_|AfRb>)8&w;^4h~u#-bRz6N%tBI%Hs7yezN9nF8n5R_~ssXpSEJS+p@oS<|$YI*pBrya>Qjri0Y8}GdRaP+2t_<}2N?d!(2G6h$=Jk0-Ap7+((*WV;2HJ|35^Zkg<`@@KB12UJb%huk?0q7Yot4FrszMc)$qp|4JMD4_6C^d1K0I0qd*9F_o2;a@iAaE6HNo@3btCkPg?4D!4Ce{q69%y7@R0P{`g*+yJSyN}B{TmDGVnGq6VS~-&El?6TKY`xlHsfi(=}U%T5F8$TK;IeFH}qQ|u|aE0aB@YUqA1?*Gg~w_^7m3ED44y?2M>g}*Ma9*8~C~G;Wh}XU3uz(<)wg#`jTV%tM2Dx`gR^#l9D`<X``bp_ry~l2sk7QMHKcBZ;|qY!~=Qh)q7t{Lw;kuvlxGnk3^#F1^PjUaI`IgcMS6C_==NI{tdY*OsIsg$yLEYXWyv-0NDBgD6WRD#0tbD%&%1IK;%r&g&n!2;Pu+IJrR8QG1{uaH`q<!_hg(vdpjWE*`@$1wZ(B;@G~*+-Q$N;dYqi`B?ODd*{TW34D}uX!K7b72o}+(c&qo;rIM#q<glbl5iyp169lfsF{^x@8rI2EJ0<enJTI~t#3IlL7wSgpme7);tpeAHUvaP|4PG-w47d3=u?X{B`X0T<>;&com*@2c+s>h^K%=Iq0j#eE(!X$e0i)l+;e{Kq=bdS|*a8WY8h}0%w`X+LJMLwn+^B%FQI|&gC}C4*3-QVUTe%zv0PD2ys3jAMsSH7@f+>dvknsF<-z&=xle-eR1D545%c<3Tt7gBfl$8P>=2iMRgPenGO-H_%D*U)93UN`bxl={7{C4^k0A_(dDFDO9(bb~mVul+@d|JIBI9zTMx<Z6fD+kw@GOahyLn)|&p@glm1sUiAVR~|(|GAgOMGuR(sIKYAZ7?LTsRM6*#YH}f0VQBD^K{?kz5IUU_oP3@5yvnb*&WTNaJL3UN^G3YCJ~fk`PY-X3~oO<Zd(#geeQY89Vkj3^JBy-2&f*}0$tkVW|`Zq6R%85$0CP72lY<#BpOt}0Ehf7<*h_s84g>$AC3H^To-;8d-)IW(+>}HB31|wjp^x+<ZCbd4*5Zs{c;A0$sd9-V(q!sAH;lg!Ug7^i*8ZIadqi;!v@dB`pAGGf6>a@83fd8LFYtXH#!90yLa1QmT;5j;xR{;Id%-Gy!eAV*E6hY1?*I`kT0P|o-KP#<cR<tG4K63BF0;%pis>cllLq{Feh<xmKWbVvQa%>#=*(YAT$)q6+~D6`zPUV+f?sI-qv>KE#%#jxh=TT%6pr(tz|!2dbVx+$)0g8&{&UDtPGJFLOqRxNPGO8tReW;FPbC$IbXvQ&Ewv*I7wq6<YZ91V(dJ^c?vnsL_)LdA8(wrw(=2oGdH;@AkQ;?hj`vU4lrjLTgX3Q>+fHEg>=3`I$yzBuTNh`_;rL|NB9-e`6Zr)FYxhKROc(I^A*+kit2ntb-toHKOL%bf@Rk41MIAyc+tHdQuI>-J6%G7@Q%PvZf})1a7lm)roc{;T8ZQaK5iz(teJjN^rmj*On!XA$jvdF&Kn3Yc(+v2x+0^6985gdz5+GLh!L%)2j>vPaQ&R~w=fj_`C$~$T8L3i-!dwJ`302mOp9x}5?@&7N5G-sFn!oo>NcL<I>RxR;YBX3057MD?9VT9E{g?R>&4{}x-dJ~TZs}E)4TJ_TU8-0t|y#bo<Z-fTtBj3^~I>pF8B=MJAa@G*Oh-WFsF!wk)Le1c-NH7nd@44(PG$(e$>Z`1}?qSxLOG36rACt;^W;_1)vGeSJ*zz0D-JIxo6>yoM0~#j=E62dJ2v>+=NzMBI};QzuiVlx~K7wvv<b_^Rb#g4!4n_*S;d0BTMJkd<_G6cED4p%L|y_8C1{0$uK4Nk`N@b!+bjb$oyZp5V#t@6lJm7mkMr!EBDCX1i{|AtruuXe|aS{=;MnX$JvsJGuUM1&Sb+R4|axrOiS3Lo6V33A?X({s-a-Ue#4yqBFX(v_`gOgP|Xa)^tkZEjQ{jBmSfKTjt|1@_~~r4E{50U>kjlnUgTU=@--z9^}%eR8opAc>1-SZdl1XJRe2GN;e5R+|I+LuX*_;@!sOSt$Q3`_zjH)t@TV7lwoyljNNz^zjpf-cABb|@yBh}^r)3$p@!c}EfrA#x=#gA#@s=L=bpF-caHbbsTF`~qyUV9>yr)+$1BX>tfB53NF28Yhs>KiCWmj_RZVcerub5vs_toiOo!<mKiDoc8!IZ8nM|%*a>l`=a<om@n6mpXg%7avXT0uZBuY4Uwv9wfZw5sx{IG%9BkJLgMlGr>Lj2cp~zwZ82Oq-axn7#qT%|NIQq<@5xe2`Iy>6@tPe<#G0-#v<ZKU<(ko;+4jkE~M$(z~Aky%7|$GlZDo!G?zs>j`W_xHDveAY>b2-k{R5F$9oEXFI04Y9r(UInuYprO5NVH7ztdZ9Z&Z^_%dS7*1A}?a7AUvK*-gZymLej)s?$Gffas49B30HzGx$(STQwW*aHehz(VcM*3#dodp*F*`{Ge1HJk1D0tClhHy(9F&3;%zJUy49(a#?A@O25fq^NRMng=0PgV441>rpZ0R?3s>UU8^&tuRo1!YF1141$uN(U*XTCA%$7_6%sgY2FY5U0`*S4YWHpqwu1;f{JM!6Xkzuw>*@Vkp$G<;!S7Va5i5>clwQIEfBWi~wpfq7|k~Po6D7_OcadgO$6Janw0O%*;qw&zRS9V0b6a*F@;Lx|M=@_W)9m=f)a7erd%)8&Jz9CpNgAWS<ZhRCFSNzrfjZ1P7->3`vYi-6mis&<r}xD(C&8ay}9xp?+R}+RFL2{7rqCX;zA36=)kzaTHF>*f=w)SCPp=LNyEKFK{UrqU@Er7(Hom)u*OrK1LX|u}=r@pW)5c|HQ7CjdLn=V2ssFcZwp4R4g0R!(fqK%br#*;SL_wII1j;dtYTH+83kEr=^k9n8JV$3wFDLWL5~uz?s)&i=?HPc8X}yJXi;QRPJo(#EzVQ#{8$p_|jyqBBw1GAITtV-fLUVT-t7e0Z5D)Q(T#9s369fR;(?$68s9=xuP>l#j=4ycflgdnmr6$E1}SPH9CIW(@7nv#Y(pxr%yySiU3-g9p2llz%m*NRNL6|79$TTRbJKoIq4XeRE-EV`T3sf)a+P5Dp+KL7TKzFAbzw(_TPRHA=)P)|7U!9=cxZ=aQ->)|M~)2!vE6?;Q!4H_<sYrg>2%5fd`hh;p{%wr5*bKFn_PL0ysugX`G?UZUEZuKx)%jH$b7ki<UrdE_(tn_q-UHBeBe(xz-%;jARC8lR5^5PiwgU*$*tOIHP`U+nMK(O5ey`kx<;uN!iKQKhZr?@O~@tBjD*OQYt3Mnz~IQ-81%3%!r`|!zJMQMEpH6-<#)JB=>n*v7cz|ws}I;=ql?;>%3lLTRAnZ-Di{Gx<(xxV2*6}^iP=x&@DP{p>~(Jm48?*N~-xS#w_?vO~7=pg;yjf^Rkx$3HT`CXSIIYEL0vkNREizmMrsm$hS-V$>1r?MoQ=w-4C$apw7k`+tdo&K_ahFuN$z8ci_+lt#Imr$;}@bcIeYm^LQPZ;1s>~o%LOv?qLg>jcY1F0F^TJ#{<O1D)#;7Ilp${ZpSa>KAryb$CmlLoSiR``AlV+Cd=(M`72g)r7lqwLof{ASWi7n^l@G6IbT~`LMQMq;M_(}epC>Y4}P#n3UNw)_lVb_%koHny)FWTWCF*J-N1SrAv_kdk;zWT;m>}Bt2=uROJesiE|}JM2lDrt*7Mp*m)^pBu@|##Y|pOOq)bXDPGbqiTL|sh!Vj~BPb*;qNs12A<F4SPAHg7xj+@kDre;%c0(RLq(^!_CE{^4%&Pp$6YIN<uY0A7adb+;j{)GE0e)uU82|sxMc4|EuY<!vbjBW+Jyu6AMqyV`=LeF6Bvt@w}0eOOJYPhzwnD2Aw9?}-etAnnDZyT@(+d|I=50qn1Y$8&t)YcCc7h#E?HVCfzgg)7P{BAI#>5Y69fZ;r8e-c71VV}ozfbed<y0(G3z=6G5*em&W*K#ONxJlbhXj*IX`p#n@N3!4DyRSK)@4>^r;eMMOBH7Kn&p(c>$akRHr$#L%8$8hyPAtmvn!3ON%8iaZ<nTayN$geD#3l!{+KHlG{snvHpr*qH%#npTn1ErPNSl+d_|&tT?Z845Bp#AA=0-0S!~o@S?$1ab1e~+xtgCeop|F5>FuRFqKXNylE1`B8xY22J&>60>?=9SknnS8zeoOha#Ap^g(Nez5*RYdM5j4SYOG(B~_FUE(BU|wTI<oUmYt-_jzZ<av=i4coe=HfaXnWpdDl*Cpd<|i2zH{$Bf4Uc*UgO~3@j|lGkge1^_N2e_<(2$be&k-l!i<kr_(&eAcaTYBKUw47!LlI{rAY4G;vXjWyFhP}=iGEAt99n4;K=BEhF$L})5{v9c}W+o!|~7_q;BnWh0^+LS+HX?nddi#WXF2rnmxGhyb@0wEdlovwzEbp`7_;G9lT+(;a$!8agBH?QYmY&3<RSg_Gr8-d7^wa$R1Fg<y}&?3l}*av*ia#YV6;QVEvY^YDo#Mf^R!7mGgJ@IwM>seti8y$djkzy9#-tj_lv><|ikxzvd-cK``h`c`+JEy9|vX|GFaE$V_6pGLeaRiR@P_zwmS+UGiy>{q0|H^A+&y^v{1k<IcA^lP@%-b?z4azNP`{q3?o|2f9nT=bdSr$XNsN)18qqw58V_jN;i1ZHm$6{oIi*zE2kABLmS<k}HudoD4rK@#bZ3Lb&Y6VN4WC6G{$qTbzL{jg-mtCi>%7<N)_D7K)FvYvGaRE4d2hh^yec{GXm1UhBIG))RS`18;jQfSZI?-cEhbgH!D%ub?J>#V@<}G&+7K6$@;~o=tD4;H>Z^gQR6QdC1uVIe_(CiHQoLX-;{zK2Z_3A?gD^0$cnFixk7Z^482H3#mA@*;&X~gU|xnGi_pts)8(y3MU(1lEa+VgmzHp0z0agec87ZJmHrn37avFY$)8*s3Qs-Q(<V8HT3e-)mpT{ml~Y1N;$>>9!QE9pr#0+Ibhp9@E9~jNd(v=GqB-G8Mx&>Rm01GM7g@faLNDT`z?S+x^--2Tr7Y+<ZqZ-=In3Tt{33?Q3Ta>cQoUEHuYD&?>P0ta^7bP)G+(o7n|&D-bcnDMgmYXv+K<7t2OVzM9-hqmasp6Y2pDr1|)k<qvg!=B;SEm9auWVrOr)d$NQs%4}CXR^^E5k%(t^n|47}!0DZ_Z<JYvGk{|myxq`!I+@#-Jx`J?hRxJnk-o-bPX=WL<LhaLZd@65k)l{+4n#2IFaLYSo+Iobw9a?)$zYcyjZqPXDWta~zIA!3`-q-DziZO$OSL!{z#K3n=Ny)2Wf4zY!)tV08YCv!)Ig11P`ek{rgdj`n@40z4BwguvOq3eYfT{VlVlnnRj2}2&@@?H?nqr{;{QJ$$2et)Ed3!!P1K?P75y!r7FtO0!o5}>GN7Su~ZMM(`AMX#><|uO!EmgR)3zO$TA8n@EG-VfHvCXPM*ffpBJi|;zat2Avp$VG`jkHRe_6-7=j>*K9E*w>!X#K=hacPw|UK!_n@!2p3mJ)X>$_kcY#s+_|nL5BW2ifMx$=dzir9e=;rCfDV?T|9wM4)M6qT}BS{bh<o!Bm=%M%#figt@a`Mbv<fZ=b3p8Dg4qXK6frs-i$H(}=hsCpNBTGd=(l$c<1P#wH46f-~O8JsjoqMCoBQIly?5H;pTutxELD0}xWN^fx9`5X#@P;`K0T$f=AN3yxx}Oz=k{HZ9JCyHRqTl$S{}IUUgy;V_&qissQQ55Kh1UBz#2q)t;rybM;KY}}+?>`UoPiE+gf)UTYY{RHh!#-7KENu#t;ZD-R@E^WL)(txq(^8~UrMH9HPgUg*VEP-@>V$tf6Xisz|UyR@DEVvH^I~kc>)iHdR)GGtsS4LNN`dy%o!mf@y?7#V<9`!u}$eJ}i#MBR}UjqD*|2BhfD#%0Uc~|vd+o~fA$NBE<d=shsM(BwGs=SgLsIf4COhw411&<eUX)L_vNzvr*qO@5BPX*JeVe>gZ;x`c+SCc<dLBNq`^H6h7*iss5xRBE+hpdk9l)$`6evmB#`g{laJq_Q&wN<9+Y;YC`w7M3i0jI?eq_@$~ShVG{O%7jL9MdrG)YJ%Q_!gUmc~$u~H<Z`HXymuZ=tX;nU(_^qJbt)#2kOoMI+<7f`+IjsR-`zY>SS{ikONJTJgD^adODR6o*uoXRyvskW<~nfy<gGCtC`A-)aR)S?E$LBjd^-&iNgq_bhK!_bWt-#hN2?&f`z9?37%FfhZ9w?JXTAKp*ppcjOE1bTHK;+93EP~q8!fw#RroXms(vF!Ks1!hJvI>*-(^-*gf)ufw{>8-}4%>gO`s?D^{)Y58T2i*YxZ1Ysb8*d$U1>krU&27v4L-r<|q*cdYq66W{|+i=6Wp5Af-*ZK~S=e&hT0xd6YTh~N_eel<ChPX+k&Eeno-`?jD2R|9+|-KOZ?!gdnn@M3n%`BtolzH<`&wrKj90DmZMstyQYRe2Wk8Q^nIkjh*;daWF*%HS!m%L?-=g!v`X$C;SKVBRSEloHE(HpVw~ctTF{`0Sb~%&#uOd?M->)vTV3N1rgvAAa$rly>)61nHhUSAkFS)jcw0_Fw>^!eqytMF{c}7(QyH2<ZuDd)OT@HUoFCHNgl6R$5q52SG_~{s^dpTH-bKM7lhZ`ewx$G*FWhzSrKr<qoyA7}c6U3L^-L7og$uu_fc)(P6e$<od}c%+4BVRs>RtqNv=7HfKsZ09;hF{8HKZ#fV4JI(}r&+dk0QJrd5)ZpBMA5&?&Bc{Bg<7Y+Yop%av+`Uo6ne88{SpGNOZ0^a!+DGJ8Bz<-_m=PX9#zmNQ(^>O4lgoVUUKNc;z;+)mwC;_R{2_t><{#)uqIO&7nf5uI?x3)^<QS$u+Pn+WR6A?Qn)F!$I*FTiCNR7Z+9Mu2$OCrEQ5#Z5V<e?jY)Di)+VE^$V;`U<pHg6CNTb^4@DyoPzvmFS1I!6>lXghkjg$52vb%G>mP?gxI9dRZgBPH`D@8r&|q=9j!teqU`o-8UkaHR)7=$<&MG2{?On(Ru74Z!J;$0S>yj-)3B$VZxFV6|-B8Hur%Fm3IJ(yZ1~<S}1!#ll@*_%5;4i}s2L!$$BcaT`VGD#v7Mk3^3I18#Ekn4YJv?P=PCDv6Tf#5FhE2)K)e+ESOHp!)1bnF6aP?+LH73FeB&BrIi6^tPeXS&{K^z?SU?0*CV2?g+#V^PJ?bywq5oAhC$L+JiAMVF@9Vfg6%-$Tk>VOg%ne6H9d>Pg9I5AC5cB%Fc<3%s&|28xWQ4+6@U?T>c@$8m`YEd?vD2p)h8~YR@!G6b+ySBw-}c_9#vEdp|HH7yd6_1}6009|)h=TNpsDy}kb|6g9&Fq#X3XLms_mMP#q@MA)S**#(2C!^74^mYg`DaLyHTGmnCd5~s7{{Ob<_UKY3}S66$<r}<0ncd+@#&+~5Vvg=T7F-_7265aKi?0vgbIy9;sGkYvoRd>doh{*N;YF!cd)_tmbGidojde*rN<wgt~?9v{acXq#rQck)LBx9<rd;=-oLcoscHQ3^zb->i@X|f*IjG9;*Y;ba>J9btWQU<zWJ!74yiV8F<xqg{ILNN~0+lV{!n&~N0+E82kz9dUg_u|J}MQ|&Ws5-LUDfYG%tFSyz<DM&!0ZOI2JqWc=q?dk9B|bj+<lLA3{uk8M&XL|$@jkikKz&8(G%{mio8K6Vla_Oy1sf37<we6hWFw#t0v-v7`iA9b3=4M9mQNK^_sO7cB+3)I%!`UQ|9_xIN-#f(7DyVU8W7ct5qGbXX<FCHfgl#OOo%|H3_CP3QGmVL@@x3weiX|!;p%zvp+MJ52w#G66XOj<6L|h&(G4EY;HH+4WZz(4Q%qkdz><dkC(%^i&RmiPLkyw7BbfuS{XC4w_H4X)B2y2Zno!D@x-hCS>%fMThDsvMb+V`H=kHZ9p(H4#-)n#M&veJ97nPF<Be@l!lVSW_MW@^|iOHN?NoVo+Dox|*XMdCS>^wmKu+L`yk%M}8S*$h`45P~TtKzWtik5E1ZI*Tcf(~PDp<81BKmCYz6+^c$Mr_=pc*z#Msh6k#Em_&iw#=G>xcTGY>meO6nEANJ;O|vtEV13`GPZMRSf9sstztVj7RZ1Vt=Eg#ZZpMpPRwZw$R_}UIUK|$T$~r1S#V5<{|mS4y8W`QE0NrHL>QL#5dvn(=Gn0bNPkN=97lSC=sM*Wo{I~)ISM;$455a5)lcyDI;K)8>saB}I{+=zE8)arX;S4QoR(#$cQb77*tUheiTUMs<2enw>lx3*dK}N1$qOqT<7}&!)Qxu<B6NAY;Z%8?N0Zj6V<6nBXt9^oY)ik0|AwOf3rG1~K%iM6mhoK)H0!TA(EO9wqN1<APc~a|=YI>!_c5d)idLDC&ZD_(a7pB~f!P*uB>G+QriBy$cpmd|uM<#MUBRe=?tewsHn0xo{C(awR>-4^mVS7EdkXJAXx<^C(ST480o;BI8h(Q3F=8!I*e&4fNd18Lp8%?c3BP>7Z3RpG^$ynKu?nJY<-UtV6{3%nofFrWvQNt{57_r1+XL)O1N=&aTI%?*Hjn~nfiv?@e^tY#LQp8f)+@$A{Bm>Hm^HpKY<mDdz?e@v-YQb;mIJ2Iis9=_#A39PQ|TeBko+s-M2n+w%3H<y#yIT-^YQKbZw<S$D*M@@dv0H_d|n#62XL3pb_eaZwmX!4xa<pO={@ZZR&wcu{_xXZfj@7i{l@OhF8gTH266P_6@Pw@=*k}96|3dYpyS>|wTOm0MSZ?gASJnGV^2G}7@=G<y|$e%M(J#WNLp=(E7kGPTxJI)s$Sd;?h&RQrIryj>#A`5PM%Te@T*7k&@<^nHaH35;l__o9!G107h_lOxb4~Bv%RBXML3AZI*z>~K?-H>xCgZ^ls8#F=Lc)MJ7%%pF(9i83vnnQBW~7DZWh`p0KSER**w7-+S*Ss=U3N^O#v6SwHzc9v==$Z_!Vyr{a*tycJ1q*V4X6Oo&L_NHGzm5F6EH+AysHJO4TD68*0H+qU9Yxn60XW*y#hY;FYgPcOFW)u4P;VbU2q?s!+M?Me3dnT#Ld!Vo6koy&)vgYlc{o^=TT-q8=qYA?av^Cn@*P{Ao4aF_R{|N&?<O>IBgUT$AoR;_HSnCTtU#vlZB|)v1o~0y?&D2Q^bw0MC40P(@KuM-of7C9u>DNVZw_Vx@`eI@rPa!jJ$IPNCK7N>_3p()H_7H+D&)JGY-7r^hINB_al<G+fD5)&C80eLsm^4B_lOZQqH+<z#h+%+5UT*CpVf?-YgeCLdU{JR0T$*k8*s7iiMfa_=;(g+_&F=)Cvk?;R*Rfb3@AmdffKU=dZ2#VpJ#%tj6vskRC0F#|#+7?d1aytt+>l|u{uVByK2YSW^?4;dby7pal5Te+sjD}kKfbtuhsSldV*vWZfde@fBl$P^mG35<ryvu}&ec17=;+Cj3!4I8Ib<7O>Aur)L&Aa3}>5*0eUAP+oo<;`nXu>`?ph?+G%jQl6e1+s=>-EF3VXXTbqE8;8X(HHYwE2&e)fu(jFQ;lDz3karG$94iMlvnI6Wvf0*u;i-mtfkHSfAGG=RN%AHdv5oQ>(a7(M}q6Ad>5|P?wEh8B+`LRt$qTco2}pGxeDH33Q#vIcr6PSv`y&jy<NfU#tL3USMbg9-6cNPHdeo81rJE4_B{)C9rDvBthRZ*j&Vl;nsLXpT9PLQHnKceot5cYwy>2X{Y!DUW6#o65bm{JGk*nyEAh*ZQ=N11SKM#=VdtyQnIV3p0b*@3Zjr@1XqvBCjcC(7WzSZ~o+V)7lJD{=IvT*XGQ}M(@0~T)51g&4OdXEylzcV7Uss1;j$xZ293;Y`+8XazJ_B~T7U+T#_np)Q;eHw(Y&{6T9|f`Ie=oU1Fg>9+Y?j)iBi77ruO2};WidPw_r-0}?UJ40J~1aHQ({FRZ0n6(5{`Ko+>U9|)Z*?Pl2ei%;MX>Mp4_&V?t-%hnP_#ZK3P<)oeoz%xLP(Yv2dcH`$e-m+1Gya0@&S=Vnu<9Ds$M~D*uCY)J;gV({|?jYK9AKe7C;9+@ZctNHnV%BUXRHg?i#b6GAYn+F!$krZnL~cN}r<HKAP>JoF4&ABYj|8bdnGk<b&P3!Gg%?U+W%MyKi7vC+YvAE=VlHVd$5MOTy*HP|@zK@}RHMyrNDwxAyKZTZP3^t)y}4!4?l^XwYrjm;XgB3lVL(zWV1^B&#<w{EVP702Fsc=^L?#&I3#5NeHm!&En0cM;dJv#_1Kue>|x<~VEJg-bFvzG0|vW2@4-+nK`DS}YGe_4Qg?#-|OOgn{Yv9jl8J=EacaU>X&Uys!`9j)@Ybx3hVVt7-UA=hzt}0YFp8e)#Thy!STymTUhKXu2m|#$dMSe%wwQHb7e+05^(*KuSnk^z4PedDgyfE~b9Ie`^HLnA`*a*8{e}H3RYWh&W~BI)P5P4AcqR%s{8`VNz^o@aUfI@s^%bg9wfx`>qsU!K4sY5sijg25F{_R?(eqMz=CV`Jn2R>-Z8%d^?NVwgraTvSL`apijI1`0jVyZ!GFc=yHpay=38ry)A5-DE~-*lxIZv7W{U=yz`IV&0>yFC?iw?tr>Z+?oczZY8*v6BHT3@qI4V~Lqr5CiW0N}S+~%&v|fm|aMQL#C8GT&neJx}rqB-^{azX?`Q09z6@dCO>;p&uSi^7{3pc?+agbZoqVMs8r;o<&k+@1?b=c9%#T9f=m#ixbv)P4d?FcGoq@HJB;MF?=sgC6s-xk=aV`BuGepCLjyC5<!j72pl?;;|I0zE}@1A92>9IWWM<9oM`y%tov)WLto{kwkn8LZ3$W%Y(1a;s7PbdRXQS^;S->lg_i4(*9#L>MxB{XJ=%)X9sS;%Q{>!7+ncaq+qeK919r$~JqDSwKuR;w~LIDuYl!5W|t&8QX23YG?C%TWE#u?<CvjAIGwx8i7%@rHT^iB@nCcd{fb_p)()I=hS)o8;DQ=E9rwH=z*^s9f2>VOqj>J1~S!?A4&X9et2{OUm$JHcEMo6<Ual-m`YNp)!$_{HmULpp*AbN23B74hVxlE-NP}jP!Q(+8M4=mZcQs<teyJM@?}&F>`6Dofp1j_wf-L~`G<V`XQII=1R~_t%EpTw!By;ed?d1s0W+j*)*V`AhBiAq#ALEwu}TFM-5Q=J|7Twbo?b}S^6A$sQZj)w;QC|UTUH5^o57@u_lO|#>#MuGi-;kJkwnRmrGh)nx9pH&!Iu_t+O>U|V0akAEk$HSmX!>YlUUUxVgl~Mj;GZ>)|;ak6zf0z9!(}E;;O7~#m76yRMo=yAn)nx<Fdm<+Gh2v$s~Kk5k?QJx1Ra)7BlkT%!_-J-tE?P@x0Fj4RWQiZ5aDZ03$~3eIpn@M7IbmJ__f<fZf{F<ieq{!K%9dT40AM=CL1obc3!|@L;+CQipDjGow|Ld9sc~Ph?KO{Cnd~#H=Uct=}Qy8o-j}!$1E~MwDJ{jS*de@yT~Ro4%(uDGuZwuMBL>vnJl<KrR|~44s5gJnz}5Z8+DJ-?0s_uET*wx9Z@R3|oxlG=Au)KyM@7qHJ+nP<QA|*7&W^_@(Z$BmJwYFgIY}|CtXoit?K;2C}<8irMGs7JZgTLdmzCMlqZZVVDnLn8q(I$1jS)VFe43qezVI12D=}n<pI73Ec^?IJ%?29$+LFQA%9YS39C9pAD3a8-Bw5(g*YQYsziXZCW_|B*g0L!rD-q+aD*lU;e1M{Yr^<J8q{-x1Tb8bY#FqFnRt`V9ZlDk3vnxwAKm?hKUCo#xT(|bjmf-Au{Jb8@?vCg%xm}SNR}_4PI$Ta8c(4isl_F_)6>!Jr{S;pk?=f!XprHg4URX@96v=cSVmk2|x`f>_KwQ|F7ML4byec5GnC)PztaSozj+oB+6~tohhQvO0!{C+Id3Q7Su{LSpr%B^pK^k`O`MWu7rVMa29KCn%Xm(CGCtDx{+*2ghUz))rS)ujha~~1r+%Lhqg3LB?~L)j6^Uk1yEtMtjpDwm8YJ0l+zIhaBSiJs38Zj1{)c=k!_C<gTR_7Qy_>tT9qVlsz|g&Y@=oUt5|{&FR|hxPZw2Wg-dYCA6YZeI45diO-w}|v8mTOTQJh5b|P(>F*cDL7&>)5qr?0(B1@AhO*C)`qIHhLm}8c&5gxe6qA@#YiL}C0n}2L?B%z9H;yX*Td<yoa{H6cV7a#=#`QDa33kWKlDV($TiHU}mJtCT;nHXy;YhXJz=*K}1(waq377H<hswUPAF_Ki6uY)EdM`BGAW6AEIUMa)1(9vtePs(77WS}t?xK|U6LtQ*#zL1E)+LnH_yJ%1(Pod)ygG8dA@bnE4x{?J~Hpcn~5vmf9DD{Ih#(*J`({YRW>qD7$NH?P?5biJlY^*7DtR@)QT~hm|wd4EfOqEy@f2Yc;dAlbmPOC9Lk=a_m8Kw(q;%MBnz9I~^qQyK0(dD6+K$VD*iZuOiUtli0>$!=LX(b0r1Ls1%dq42mijtC)lE23u7?FXbP&w3(OfKbN_#UUgy(BM*3eRTZ0Caxr+VHhL<f!*soCSxLbdLygF;rbKUb0+2;Fk0`#nO*xSR;6xvng-Y2O_sW&-)(XmU$AKQn+JvU_f)RBd(ooZh%>k>y!1L`w$*kMCx$n@O_A{#%z=W%NYq?LLh+E--Db5?)w@(KfWRnH{NofvdMj$W4GuJoDTWBPI-dYgt4L3)vDpd?`l#<RUTJS2u|EwG}cxA$b4EdBPFLlb`t8XvQHh32^F?;aB}c(!DLEd&CcNJ&~ul~V)PbEVMQwgwdaPrHo{4yU@B|S!I$<W|MHothz$K0gvRQtvsu6T<P5#WU-$$e)o$hlg=vRHEX;<%m8e`z`c>;p9*`NPbTHx8;H+OayFZl@oG4Wxcx=N+wM;$Y0bT}uA38^|)T0J^r`#oD5Jd;D3?oHHny2Fm0yqXGKqBrpg?#%^c0Do*dlG$VoAb+Uu8y(Fx4aj{Ev)lN<qu}zzyeXSaM>vPorsp{6Xj{Xrd~j05)}Za{Hc6rhD6xHJlszLi4$a%cz-}+7Sj=S^!_0-p@6u*ehk?V=b8OEiQs&N^7P#i#;T=N{NZR_Y3rn(E(kPg_IiB?-+e^G>f8CjHEDDmsxE$U5`zZjv%Sr3+Wf5sqR>J8ruwJJ&VwKGKtGzIaeL$i1ocoEwwch$_|55T_?h`8?2ZYdzxis9*-4Gyf(!BRcWh2?efY++-ehdta&m9z)6TrfSiH$AM4kC_7Y-$QNK=#!cX23VU953eT*<1PRd0>;mQ;A_f(VGAa8~okFeaw47<#(dB{yw*5dsk;hUG`PLS)MXWLyLVc`vx-N-9R^*yJWxQl`vyJaL54n`~*mK=D>B{K&5OkrZ)35K-wc{tGPEkZ;;J$>mdaI!x{wRhzAlpNO-)@FqKRKo<^W1$JH|Mrzsc1f6#d<F;7l`m8L=-5Wn@D$c@W%`@Y6M~HFYHOK1z{PeRd|CFZ8GN!7Es`it!3{GN9-ItqXxThatma(Atp=McEW?9?7n;;Y3G`SE%mB}Ueh;Lsovtm$sq;1eOM>c2D%C^f=KmCjIYJVb^|IKR4M~_YZ_4iJBv<@8l@3q@A<q>9O&Wn7<#PXdT`oz*n?dF*dG?j-b&0!QD%5;P=(^2MHx|Ze$N^^82$AJQnr8(k7n#0TaKiYyA(;RV`=E#2NE?8QmVx}Xk$fufSWNTaASW9#8R^Rcn48haye{8D}SQA~Ej5sDc-pgu$DE>!dZ(8K9oSL7$u+`9E?SSuk%4BFi0?haYR)efz3#-A2+K?5fdD?1VoJSP_6BYP`h6BmEUwiK`;Xq2L%Uo%(8eOp(ew>?Rte=u^0f5^u1qj-xiObxRfkd;90Nq-KW5B#1&~ywF7$fwgU9My}ygv^U939k&6*yb`)XmtU5^mr;Sbznor$_;Iqy}`TXLn}_7RUmb=0xV!@Z16g56-^Wnmvs}*a~Qbz8sbvW+i(C3(0~7W={tTRmYG4^YqsY1RDwFnjv5bd0<<|83Oib3I3!td}n+;;n6MBr~+tikkK}KiyRP2k!0S<A$!AK43v)%+p_PLkVKI+fU<@3-Z?&RXC1#u=n_!Iqb60U2Xw`vyaMvtNMA}l9~J1d5>Y&?dLxayn*Aey5QDg@6xP{z%l`BnKB#~ljX23OB}TKSW<oXf@-Y>kA`Ckh{HRM=jXm=0^}-HRan#7fg8Zk5t%7lD2Ltx=hjhLu>_z{7{Q-6yD{2RPnJoZav>(KAEF=1Xc7d<NcTC3AGVKD4dYk42y8woIu?u`!Di?g|_xx|NZGmZx2*64l5~%RmQ*D^yo~hUdec<jG(jRZ*05~w}^h1ODvtrhH75u6}KD(_z)-}YKz2%|GJ0DD^j8t9|KQ`_!EDmam$y;llzko1$n#U$_$dinuuOiBtzzDfyjghpmF?<)~6V_!FqX8oG*AG}Y++0HVAvs5qq(sn9nGGAza|8w<+wQ?M=UAPTwyZk(6HgfJoTN7H8~m<Fra1~{VI`@DDG@i>L(vH%or<<;6bVG4(~PQC92#)jsc(q{BDe*|NdGbfA;H-yg!<`5Tp?6DYX}<>!juGQ;oF6tPa7GVU$C~`vDq}o$CZvJsjXxSqMC|`(j>u``0}_`uzWEB??l{91}(1ad~;JvnU5x<cYW9<s~PrD<|^KKb^<i<XV~y!1)~rRbIbW$b9L2K`WbS1e$5+4p63Km7qr$lI&PGmTcL#b6Tz+7kjhqR;v#9f?_lzQ<v3d9!&#$^=vvsWgiRzri1>kZOz+H&B8NSQ$~6)-Z?<Y&bNsrmV&(nPOG!!gB9DvBota43!4y|$SBjfE^bF()yF1Bt$2&_iiJ&`b0@4E$UrFru*%Zb-YXdtTobTwJ6qmH$_?QE(>^FCn3FHo-n2-HhF}>p?<_!;cy}iRMZiDd*<+*duI?mx}$`HQv$mDN_*KrIFSVpJ;^k_0?2bJUQ1&nOm>=}Gjd83KLy70B*uYLtwup#eSq$b{S-qm#+ddwHFb+sZ!i5qsF<1!B#3P}?$@53*+--5kZ{m>0x_omRhS)k+*gFeRIrN_gl;!K|vnJ6IU;gPi1pW{OucCK$@k8~`6o-OmK0qtj4EqP%K>(H*^z+7nl^#f4>`xdiv7_i5MR?T9_F7_#`THss2{XmP5cdpagQ<VWbS2(&B55g`R+1<#{;EOIbC=L4^F6J=n@6JYI7>tOYbQDqj8ioBJw){xLw*p(Ka4`cYNb)N+dxmr$;O?$4s<oa<xaYSQ0N}6t_VEP*N^j}WtR@VwK}aPqvO33KtSX6OEK3iidp@!`H5AB-AElE_Aj8^Rf<%*MYB<aqun~u{ORaILs`rX(Y%t$PqGcVsn%8Wl$}jdwJ}%1Nc{-^%m8b?HP%ECQqVLF|jdf6~eQLe2HPLSp39V;VO3a?Y3mG3w6q5~v8}$V5$UHGJkdnEBqz*toNj)i2Jp_CD0D?rRIF54dfW=j;AAsV{5v0gb{0|mT-UqgFiz4RDj31^V-DisRTNEAh<AH&$N$Qf!5)y13*32O<{7p=f2v1>4UT^?(MKleGPrNx$1BNoe*bcysGXx2)<=w1le9`U<VWw}4nS%A;RGxkuY)Pb+KR1axoCjml<H(do8d*j;gR_m5&?w2DB-|b#WpJG&MZ#%ef22lk69kOpUOi}{;|i+0#AMqbPsmO`Bgeqi@^#niVDhPx4pUPgkO?iA>Sze1V=f|p3B)8y#DK9zHpM&pCEm38cswgWc_~z7!<3A5um>2_KEGQ5Yg0o7L*^iC|NAeZgLYX*JWCJ=th3B4t|}28j~x5Ho>jW5ctZ^>vZ*y%A>b@v(Y_}M5W*SQMb28Vf)Qa8z~(LJj3p*Y-jT!urSYv)9Q{lmP3E*KIqqr<iwTtyn<H6xp*Iu-jYd3eG%xC{Rb~Mkz2Xw|MV2;}RyFFc<uS=|M`Z?r3Vu-#k}6+k1E$2WK2l37Wo>P1fz*Z1l1he8o{#!lH*L)s9Ti*&n49J^$5OK|1bx}S()0{so$;fzcL>&ikS8}~VzA^yQJk$zwnwe(Q5E+2KdWe3zpPlx8|To=KNxM3GpZNqUr{|Kf5W|u4kwxlA4n7=LqI7?;PqhfZ+N#qr!J{4)~eN4=cB;h1!7yBBoD)#cpikC%sa%6tYmJKPad_9^PF%LW5yS?73|ciW1ntfrCWOI3<uD7vQTJ-MQ9Cm6vP&oD*iwO#eAIxMYfL%m<!8I=BWzOX?1E^CpiOubch`x+rWV~+O3QX4Zd0{u?eoHs699K(F%;&($yedciLJ4g<rGZ<p1xlHuD1V(XXa34F4gf^yM-y1E<V~$h<({%YT@(%e*k$#w(eZ$}%s+RHnj1L}knOs0yc&e_<Tj#24gWFyM>)%l4C(@BU@?@A%=5yT?aHo()5s9bp5H@$pd-U~zLFMNkI>=SdxLz=nLzD5}3_u+8XAtX2csd(&|5z+@<}3m7g_ombroUT}W>aKb8TjmHTG?2eE>Q|VmE_u)j=MFu{K*fv{a##{QeZQv{S3X5DV`cx8BR!$C+7yxm?{$zwvc`ALEFYb2G0ZeM>E+R{zoFOH4jFc;^LH3aSvs54DQ~EdD1PfDc%s)0+LEpmo<Hj4qIL%2O+U_r!vB<Ia+b;(X-xBaOD|whX5WivcYnDILA_Y4ZN^K;73a3ZU)jq40c0?3c%w|XVEO1I&7Md#4>kP?I;iXWDwT;bSDtU||u0UHLSOoG;!3a6^Ys$}hh2kU@S`8#3r9<5q{<idnb_5mX%T8E_iOO+p6Yi`O2G2)=+M76Ac)K7*Qsvg#leE(QfA-!i<hFH94;o)HzVVGQ$87)kH@i9K?5b3AJk?khM!ncqiV!eY$wgf#0R@R735ld6RmKWc*isj<OvNg5qd`l>8$lFuR~I7KL{Zd4gAGU!BoT#NdFS^$&-;yLHf#NB?X~yX6lb5sf95~`ImaAxjIVi{rwQ@Tyn77<km_=b%|jq#MF}S-466;Q5}cu9iR!`j(by=&Z7M8NXvJbexi)=ZB`j=@@O)|;Nv*4#h7n21mOpnWdORLs&ZL1Z<>0b`56(Y5s<@%L5sNM7AVHJXKF(vLPI}2EkgB3!*ldyHYjGn%k3N(~PB5-iTMs~Wq)ukX(?Aj~^&cO)BSsFD_=9OeaTfI_+O)W<<?AzdPxW&{cl2B?IjB+=X$jSjYUx@8lpMBMIuboE*hEIKW5FZzAh4k-^3t;GqVR}zvCf;q3pxL$++?yJ!6FYuJV?<xKeT}~FdoNBgh2wL8%;<i*%H6RvYn)17)DQ)ylkr!9z{P9%@+Yv`B1#Lo$!g~pkTOWvf-9Wll2@VIBw#djh)-159&}NxAs!5NV>A<`DQi@SDaUl-<i~uwVRd(=3$25nHh^TDgku1f~oGpY(j2?&tPukjW=;qW0)?%eXg3E6aEn=*Ysu*Ev%|mUU}`fJgl8nJ^3nxX#b{zH<Bi;zp4x8%mTfB5RJ`!*bzb|9S6@wsp@}j_2Ma{uQ#j0ac3L$$-mv~)<ZA~wD)b*91V8Pt0Q0jbc<j0{lYj4eTDIFXirIBXX`KD4?xS<+@VYq(z~KR-WQpe*65EQ^ha1lpXnW8iD3y#Y~MNb%r*3UgoyqJ>h&cWwp7GNtX!zF5syS5Qn4F)O#Kz5B`zo}D7&=^I&m5wIo$lGAPy;B@6Yn=v;laiQ!~#d6j}eU|At<&F^L;iS;|i3hQvuv9(V4AI7{x-k(I9vj%3(oxjCWhIdB>B$|=eBK7eJ&dx9{8JqYw8&>aZajuS_m7e*s{Ht@?9Q4U2{zlfZe_tOEE7UdX3hbg`6V2aQX*kXw-F=znX6U9-BIPrpWJ<k_T?-nmB6B=RKa{wP>j|`YAhzo!FD{<Sv3i@i?HfRq}Jo}xwZQ>+WnBI;polAxr9U#^uH!T5UwsK}Be@GlQ&G0;9z;5u|^qTQv6>uO2UsBzOPYySzZW1Iwz_nFH;10>HTa(;UCAp2Z78ndL8N<y9<Z+keCcz+cwN=Wv$U*xB$t}3CBO}J&;JL*Mo*N{ID%FjaOAOJC=k_sIhhJSKqa$PM%~dk`fV?d$8GRrW$x)0!CI<X<;93X$hBLP$&jaE$OjyhFkD)cw1B(;}=B(*}@K$PqiK)$D%MM6V@LgZ;>@BCWC9GCCqLRe!!RTA{tR!l|Q+l$LQB>t}g#B4Fk1M~o9e(=+_Ad<hp7E_2_|WCxY+n!%14?Fie$Di#us$ZUpqHF*OeYayWdDL<eaTZ>M*nheIGt+WjCloO?SIAAmknpqJ!qcL3aRF)C2!l_%2O#A6}nrgYO*@zuC<zbTw;15kg*6B_VUZLqTmo~sw(JDR1dADsu`#-)b6>|N3sxMaz@X)G7XZym87x~9Xk{(m!Q0!_&)Ipk@f6m-s+~S=1o`J9m(Of9k5~&;Z3bS=eb_AS-Xy&NkkN%`4FY+9q6En^5>TmBH(xCv{gL(&y0lsBDIdT0p6vn`)Y3b&(V(xR0SzJ!s+bt4n^KQ&1Fwqx<~TCur;*cg_f5=yQ!0BC~%PZ*eITp6udWW7~W)}SOYZ;XoNz!$AQ-vcxRHw>0}23OVfA6>vw5kONgQ@l)50zCwT;3VH!K&SGDms9CTc7J-uF}w}=4i0UZ-cOF_IDdR;8%G6<6iha*RebA1SwC<Tf15}FezTCUq(hSJ7SYg35_xv<y*TGTk4HwG6axv^*u6oKu7|Abv+QAHCyXV`NwKWIK=&&8QBg7ZW#CRzAlNXy1U%@?fCz-qLuYrhY861MIEJ3qcm(tNjnCp~}`MJVx}KL)jTaMCT6@d#?f6wMa*qOSf>;SmbKPe3yuc0F(hCOE!KMaNoqrpjK%rvrPDc-S&QRrIoP0WKR!UjrA$<kUN$u}@RZy@WMRpb)+tO9`3+>RC#StpwX~WDgY!M<)g`rusmkf|07Nm>zV`h{Q6;2g2>Glt>&mbgSAET^t*=717FfV3!8AIfL;5%kxJ}<D>Lu^~_lPfv9BQ|8Vnfxi-7~&jAN}7+H+)^=CQq&$>|tOfQ6Py<m2gm_vY7)3t;QIJkBDErGHP{PM~GJ(H@|OEBsg<8@!2OgwVrN9a==A#5Dehb=A{#F`NCAi~@8?c>9QFM#k>Icz!9CtK4B86_{magq6_-Lt*;b5%AaMMZh`{@kec+7qTy0*oJU{r*vQbs|>O1yZG~Rdr_obGmHI##)y6Fxp*BJi=307Yv)$>4oY10}WWvAP*(FmzfO&c^=uvpf``}&@Des(x4vLmGbb+$cBPxcmZ1o7&l0P9(mi!r8-FJIE-dO3H(WU=11aGB_Pg(=P(@no_uT26wAPSDB)QkLfQBAOJTl8z-&MS2J{87OOkq;g$P(Q#t>AHg<EjfXl|HGZ5dSm=o|Y+%Pp2Uds-yyNgJ)f-WF<g<x8t4L{3X<SOV>-XfRe*Y&aN4Epc87CZQDDcf@JYPR=vv>z_@!q0iV)JlR#dk{>){rAJ89N%M^3Ta((MaOqoFq2e5RtSxwPJi&RD-A{L-FhR2VP#74cKp(HO>>>ZbulFKt7gs1PE>9VYI~F7Y?{wL<au{C9l_(oh=r@2vl}!fvyr{DI7DE96T6|_i+4{pdq@#IjC6a&qqwmD%FYzU<EU*@LWt$247e4T}EdPE2+wSMIMOjs3%Kp{6G#E08ApL;mKJ}+cs8cdOY|<ScoDDz&gVKy)QGWV8_0S$%L|xRkS@YI%nfPqb`$O5W_BH5)7LNtTK=h+T3!yt<w*v1sijaTm17C&;T2ITeRc{vtB((P8+VH)z))3y?L7mv#&yvBnaBXa|uo9n@8Xh<`ob?yVSUGVFYu1o5fj8z2;=dCo&d~AVapDARyNv<8;u%#bY}4gSfRoHTuRJ4oV#6_73qG5(F#$(s5oBKm8DqzCN~$~MKlwFGrRz&;YfoCQJz=@_STH|bPD-}c3f}~U0|ss<&q3z%t<~tU4y{Oe0Rpp(rFo70f$#yKUIxIu#?BhS9ikpjgc*xAhcakYY(p&Y_*5Ss7}Rju+65k(@^Qx)WaftaaI5PY@}KxdhwQ~%PM3o<+#am!t6L3EZVuUltKE3kETa~B4%uBDvaE~{=Sf^!R366hIxY8`Gkc~dV22Vwo9;l=QMucBV0l3hsbDG2JWM}p{=x^Kg}s$eO5bj^J}=ZG+*&;%brSGvOk<t_hCrQR;)k*JY#1*p>A4Ezq68EKt{3!DKHo_vWgf{!5o1Pzg;f$-{hA*}IoO#ZMx%o~@_bk|Q_FN}kSJ;vZcL4?N%Xj52P}wx4g*5`wL3yyqB=R1TRzK6pg#Rz!P#+9B=Won6Jrc(-oIEfmZW_1C!pz;K1IfoQzWl|+TZ0yeOH?cRpH8|+9EWUX3u$3{R3jK770Tp=yZrU6&iDif>=cpE3}xID4$V@r1PgT^*f9dcp9((^fIb|!tQuRmO4}{#!khfM=vlt+B8h)ACXJoXn-pqzVRcaj8D{%;QjI2L=bWyD%0p()a2|`XW^%xg+>S33mb<<ewN-Y4F|mFaUTAZlp&?TeYrAFDmpQRgFxfh2yrG1MjC5Lh*D2|HE4t*;#mfu!T-iR7T;YTiwhQCBBqZ-zVJd=`eb6kMm*(q0v8wpDE7$IlA3HsU<n4KV`8!p)kIKX(3%AqWEN9F|8Jb86DplFx-i_h%&{XoO<q(H=}57l?*^{pD6pe$R4tEMNLGO;7pV6U?B-xg=mI2moFUBwMRr43AA&U&tVGJGYo2Tk;biE1M-}y)F+QBRR;WA5UcSL3uy%T}1l1G8eGV<rdWL`Y<ozYutT><zw08Jk`-*50!?TqCxLJ1tz}GW7mP>y*6RjRgPQAZa0}qW9x%}kH5*o7+x(5}>P0Jm~M3m#?=+Fq1<-_d~9GdJDSk1(e_5)Of<yJ&Km6yczW<zHXqt%<KlK!Dc&?B2b_Syp}BaU3T4Ud~u&23=*VM|HX2kYbowuFkjyQt&6YAEeV-=J{d=szrl1NSyXNB;^%$6OU11vw7%N?zZVs^}PLWVYIoOxH0iMcuQ~VLCBT@StU7v{SW6H)o_)S!c}->gEG3x0ZG^z;GXFTr`V1x*%WrW)^ka>puLy?*j?1%4aw3MpnIh4Gb5iNB0DXX)77B*(EpzLz@MoyuXJK@3~;fZ)n-(x>9irbQH<8L_kZ=32n(4h2CMqUZfW*?V`=)m(pmV(O+*VI+md_>!Ps{uxxW7RBVA>!qsa%Yu{2wyXthc3PBQUpWtg_EsR&9j?RFA91Di6sngY4p&ay#y8@4f1e6ecIk~AJZjlPN*G*bzJl?ZO39PESsT+<YeD`r1;(u=C&GDK(i&pq@w#Q4eg3EqwZ%vj!U3y6gCr0lhGqPc^!k3IJT70WTkK`e!F{{YhsJkITl8g(m!gC*%{y}bxhR-;Y>pWIkKA)g)5@cV10cN_1StwuP(2a(pLn+qnstpfa$Wk^g-aye`+^%*uF2Ir$mbR(BHFABBLld@@9+JHstNcXkv5L{4k{#vcL{JsIim8i$o_A=E_&U^qbNQFxZBqjLpILa@fFW>6*-I~>1hdbKmx)sVku@q>D=Xd^tymm5RN=Ide66zYovX_+&x@T07Sj(P{YJ8+0+IS%W9!jK<Pt5gh>mLfi)@flar4HQb6iflhU)&Fpmx+JapaAu-DH}Gf{2y<=OZ0SiNQf&ya`kPBJ7bnWKoxR@-h1!D+kjzPPXn)$w2H)gXV(jyzje-!$|Jlwo$>KN_mE+^yCyEi23z0H?nYoQ`8D6X}YDyl2KruoC0heUTE%6o;)y`MfiF`M+F$J4tC_gHJ=n^1BV=puxzH6gTQAeFMdp<+U-DkUC$PfENzHel!H0;pk7wPy*IQy3%yAuS590nsy}p%=vQV!2e(QuP2Dp2A{$K6c%2ZNRCpXIL?J?z%ugst0(GHKoz%<Yj;SeG(H!}K3iD1}heqehj*slhOwhjE{C;mf>`_rQW!FI<V_+A_EfI{AXf>0mN1{OxA1Q>c-MCkJxa0Pg347_}&cwDP9ENBtm#nN>)bgiQjAK`a3__!)Q6@gfa)O^5Y4E`D%g6|O7YUJu8Z_-efHD&|v68(w6?Q5cy{UQ}lWDYBbuK)<{lpYu)sHVrO4VG2U^X>t6(hyDC4kS($C;i9Kj*3s`y`B#*b$k*i?qV<)qclJ(kI7uGwJ1Yatko1VQq9(XT)ShVO9frK3V(P(G1*8kH}0H+5C{eNrfDS*@3;9lD2;R>Fl651N0dFa{5Nbv73D74J~TSv;~Az5;pcLDN-d#nylV&&L=~e&Y0KU^1FH_ZjDc^7toF{p<0`Tn}c1_iVUVTUHRKVbfK_tSG|RNjn2TD11?H<`476r47!+6MzNCWgNx^X`0M-q`ort_b^rRqEBwPN{CnfqA6|+dUgVGStN$>+`u96RdY8YZujS0Y>aX9#o$@~%sNc|qO&{)q(ho1}ySz8P@z-~H@9*)nV*QN&YQOpq^lN(cuO9lW)%T`R^=3Y+%wMO!x_9_>_1L}YaTG!<RN6~;&Cf<viHj!#OIY@T_Vq`T+~JL%)yL6I#Re;E1ZNK4p#rui)hcep0R8E)zx-$50sU*Ist@H6a5Xk;JPwdq=}@o%kkC|QiT{qYHln^0`@=F^4JK$O^ocMRt<{+fT_Aq5V5q?!s2(E;I{WA6e+DV@mrvpd8!1ke2S$Kez00rOb@A)<3vNDBAG7V9*9UZqUvHiK<!L)tAr{V@Uga4S+5M8lBw5(g)mvW4;OZGp&#cdI!uL*3+SjQk#yKc1d2@NH?d5x?PYfg@J8uKq?<y=g$JNP9FJ7LlyZ_A9HK%~R^i0=x;f=p8FYn^|c;TyErEEK2Yju0BEsLsVvwCbIs8UT+nQ#(Olc$gUjEl#74Zq0zE5C)kcY1vNvw8iW^6i)1e2c$$Z?M0zirHLz7pwsO#`F5wyzj|hT#$GBYq;@O64e$@u20ghzuLvG_KC}Hm*4c)n*(4vHxt!kgk!svo^f{TV^zPN75M6tHx5|8^^Gs}#{1%2-Er!Z_5OOB=J($F#>38UymN_`kKgbq7uR#TZqB~4gx#Cz;>=fRagpCJ6Q?JgosTme25arxPhS^OECs73_rK8mGa(NFwAn{=DaOx00WhrG3z*UQ5#4UKPpO>w0EqnQiE^$!9KiYvhm+Bid<#?VlM6fWF5~FU6;EojJzsNrw8n#p32-GI(2TVOTL#^`$`#Gi!J`PF)1QF!*omIWZqeu=deJ|4HREV19?oZzg)OgnQID6v;^ABmOFblc%!65Xvc}U0dR#a^H)2<nBb+!w(}V53zN#X4XzZ%fi^scDV}F`n=G8cb7?R_k*c|~{S!U(}{DRy37n{F8k9)OMKXv70xKuHw76ig!Vv_Y_*>|9Sb&Qfak-(2G9?Prw*YXL^)<5>NJoS5t@tUEtBc^X)Lu>$c3kZ?1>UrcIyaKYRAr_lyyimT-iGV(}G1&(sC|;leIwauxwf2l>H^&(=!I;~|MT;gVhVThu3tSpt7>8#J2+IjkgSP3J`m>tdM?QA-HR@r}ez2K3hBmiKK<23sN7r0x`ZR(aQtp=1MQ83RN{~RCq~}}MF#BlEW$KjiC%+Dby78I>RsoQPKlctj*d7hokyNZnNQZKEy#FNx&0!?x42SFNqS~CPomhG2ct5q$EbfpKrYQhT-7p#>CTo^51R13L;^e?1DkzaDIB1uA>M+npQn<6XD{XOf;60!`1KY*)`VR8ZX3%cPqQ&jh3~_E=rWEx_R9Es+{JBwoGc1~i)q^xK8voLTp07{`nEI)+5KT35@OA=b0#QE;ntbFhv#su@w-}hYewMEdPk@w6Z%2XRBcyxqpm(7P#YhmMMrDcsi9feHBI&JQ(O?Ws?U7o;)4H<DHmpZ`d=XD_tjrQLRGw)yuPMXroM|h~50=ege0{p7@%utu$3jOg0Kq$JFFVU$ob|e!Y39v`O0Is88N<$MNY-ZevmlSJm()*J*aRZ=1@(G(O8Y9cG`*(Y!FB6?9zyf;Oe(=KNOH8{&%Y18Hr=$se!`J-rmP7TO{{o1@IjeWZQSvVl39*hL(2(P4Uo~NG3`o@3#c~m4d=4!*k5B0++AkMn2jU@=tCUo%0dH$MBqvWr>i0Cu#sp{reSp31G5Vnc2CVJ+IP?s9xvzw?JhH;)eNSV2GKHJt22)o<%mlEy-3?#;y8f!>PfAJDhjZujr8aoPb^Z{yX67B61~`T5_!|Nqsaxk@6<YWbs>(Vv-2^i=RsE8_`Yf5%)y6vm5yHX_<|tt5Mjnl+*9k>|HbCFocjTAx&r`8M9ooX1ScpKRrwmgZa2e`d<Gi5mc^M1O%N<}^B~~|1}__~s$FQKwBT@#ed{HOC?RA5*ahKa)Ud;n)@s<3TS06oJVg^#PNJ<}_=r(~iDBW9W^qGN#YgB{K(1r7F-%=o;FuKVl>7Xt-h1#;!tkQzN;?j4F<LM?;FAF1i=csMbN`VBV0~`2P_V=>3!sDq&I38-;Pn6m14Q|~h+n}yV(f^~0j2ODX{}^sL~X+6mW;#p0HqIvYZ5q*2qz0_jQJz+y5RSA@k5ns#LssT@NE#1c1ykRv2IV4uT6l$Rt4)4p|++S-hw<FL@f~<9(3`Iq-KLs1<=du+TL0fh~gblC_;WSFp#L#+cs_I`;Jz>Ds~ZSt;z<uf!GIMr1o|&0+$3Qd^B;kR?r%Xm(y_s@7-(n>HNg_0jr*qN=n|fv=xa_gu-oZLDUD3R|FgY4wb4~Y#%zqwvfgu5|};H&MLi%(FCC)4MW*bu8O^6=}-c#-14Ak(c%X$EeI;eLzxp(!EkND!uk2@*#4eo(O&%|kr)JvOb!fIHwB!snNoD@jK{qxzg6ob$H4Qm4=<sXmg?hg*6>Yl6!2YQ%eR4&>sHZ$?4a|p`VPv%EG(4Bt9}}d%&LZOFb!WyQ*klRbs4GxzNVkn3CQc9Qn=Pn!(HvirF1WGy`0l>H>ZSJ)lbV4k{mB<2_|<{x;MfjEMzFZaOGM{s8QaP8wF-iWA<mUI&a@lQ43|&j?v^-%INMXk0cc}&rM|9DEb3#{7ouqeUmvhd(%n69#V1R6#4oXYDw{rypx-AhIm1IdSH@GH~LM4o3kgW>#234gg{1Yb|!1f2)m5U-Gl!=lSubOl~Je5ABKaL;u4hLOaDX}&}Vbb;cI-}V^jDP>k;2_GIi5(Prt9-2j>7im%v)*ClQ`O81D{x6eE$IKL@Qz@1G&aoAEq?+QW<cu}8{51?py$Gk+{MO;oFx{_Ok8yMn>GIZ}E_7Br7R`Fu9qFg|>EnEY*m$xk}Dkl-pF^!zin>oSPL0|T8&pVfh*9I5kOz7EqIN0Y%azMFgmEIV_RI!i0;jJF?|9w0M1OYK!$VDqjK>y&5fN(}jF2wUD0prsqPm58Co@}7=m$TV249lYj;$HtqMvhA*MkFA?3BkqMv@^Z|vkvJoc!<q}eTH0f?iM6b~8lZn`MU4K8Tk*|B)i<NNa);eCl^(q&Ie;E*0*N!vp(F1vxE<Im^5rl+DdV$w-av>UaS0_4Wt1Rraxh6y04c(>G_pY6F~n-F>7Y{K#FZme8kXxlqfn6qkx93W+0AoMfZJfqH*#~Tr2}H!gUr#H?}Hj4yAN)rR@oqUzm@J4SJ7-dUX?i%1DOFuG!G;zF9`eEO@tk9OhAqrfKz)|e2~Q_mH`u*PD(qHs*To2G)ot5HY1HYlCM(Ptzl%TJ8cEJj+)<-&=rIpSj8GB#q@e@^zoyMRsQMQ3v8M~NtIDJOJAVJ_Vh$0BuJlgEq%ewIg#02?rg7IUYR5tQNafj>>z^@b1x~_$G_i~L4LtVIO6A%NU<4X7XReo<H-;<QCgf~(m#5ZkCtHLPhI^`ROl=LS-lqni$vPJdT%@q8fF6xoSY>0;%P$z1$rN&cJ<_*Wp@7T{tg9jWGTC?JA<|yH&5;-O$P+&YB}>vMS!11$_P3QV*CI5W33mdeZ^vd$j?b`ak)%%TqayyCj9j>5ta*t*n?u<nOJnVy++7~1It9aSSC7KCM285Fh15|<+M`BBs*BJt@R>U(9Wpt)$2uncfBywyt}nzgn7xp$(K*>?kySAlH-!mND(Y9R*g*qiI~96^fgOHt`z={ykz|OcTPh;g#humWjN5Q99_GkUbu;<!hzK{%eaG9A5_ER5OR;3w%Z2~k-Etpre>L_oBO9s^ULT<Bo9rNi_G!?Iax=cL^diTqh{K;APWmBO7ER}nQT+av7d!&@Mf$+-@aW<AEkpJt1I|&mYdyU|8gd<%ww{wq1Fiw7!Cdap@mSpNpa5k0+UWIA~^rDq8^&5nn<BO32#jW{GProv796m2YM%$sgVe@h?3c0`D3KKv-{`Xwg%M&s6$b7W_oWd0Kx*q5{DXD-iVoST?Hd;<7wRmH3!k~(h%a#OOX`oX9vLp^N4G48xzGXrEiJq%EqJ!*kZtUVy;Oo;y_QsEDo`j3<EtNn2Su%Jv0wU@siafMHD~_<Pipct_0-~1`A-4*W6m_y+Is9WbZpHt$S9>A02IFcUGSPNo)h{NK!1FLg9RX5Y{<T@OvRmB&~@2i{GLP&+zfB*S@dFlPLG*TbI9GUw$~aCH4{TU;aE@`wb>g>*njdbKwx1t_5W1G4kv1N^k5+Yi$g92X&S%(hzT}YkaBw^r0^BQ%NS?cTBSwdgId8wx-%7af>S&smia5s!%!R`HISpq$AxDnq(a1QWh&OK2t4Z7$oJRb<f95V=#e^*EK-4J$6tj!$s|zq2p<A=!=|j+%-8>`L->DeDZgj-+i?n!6IC_XHl29b#A2oG>0qrm!KYQeu`0Yl9w)ZuDKJpv^3Ton!5GR0tB)KobBr9cH_A{?3P}2*|Y%6sIIMA0|+(|tHc_ss47|R6ACwrSjDpxl_mv=)&!tH8g8v<MS%#`<=LB!3_{9H*w-NBAn}i0BC#SxHdMR@S=iDdei2H>HpYmhpz?;{StR?{Jk-G=4bYuojU7rCs7TUHa}k7435Do5Iy;^3DGT&AG8l?n**bMZ=nduyl)T}%;va@4&(AjFcW>7xdetW)xX&0hpHTgkt=V*H_B*N-C+Vb6pbE5NsuQIKr2XVl=e0?cU?ZN;fZuTn4<+s=2tktV$XJfl`knrY%m#dPCNuuDrN}D9fQRzNmUc<JBoEIGq_&^1xtB0D?VUtohqB3T<eubrLz7F6v}4JS#kctXd?g9{y?Q=xlCW>zEMZ?l5?Y(Sn}q$981-7Y{#w<;Wb1>;)=zr$xLPT`NwZ#+*Uf$BicbEqOd$LX!Fm>4S@I5(8`>SsdQV-DNweNvYIsPvvYOL+v9s?8*4O%LLIsZsqmx>Fi#JO4MfLJBC1%l%wP1a?5UgLQ)eCiLvOmpQv%d2ssr#m#BiE)DKLd<Jdg4tuV^I#$@MtLI%l07311DM6nv)Tgx?xh0y;)lb=Nv!h*g2q2afm$ff$mucQ;<iUmDm0|u{lLFGm&_f7wo+x;4|S0-{U$G2}l|<Co@f4H7MZl1nUX>byr^2d*Z5*nU=qP2SUHicto<?aa6`LufIlpXw;pHFDy|#Qss_vE#>1jdXV9v-aGTqPKWZF-5DVW;o<T>e8|02Y7#g1Qp9MmiA${sqvVTfVS7i+r*5Pgk+G>t^wk|=HhrBo(zWC3jy2nKe<O8uBTd>!<1E@U+}lVe$5(EoXk<(Jq@&_E5y<oYS<ZHIxqn7@X?p1uQlh7^BGL7>$$fh#ZDIfBJ(KeHZ{9HDyjvbVde;7nChYRllz{pUC*)A_-%DYa@B(1q%Yoxdp*gP?h9uA#&{1qpgmQ46Wa>>roP^S&1H}Xc{Xx){`~i|HkoCg45V$uH<KS5>d>KQT@RCR!s&4S-ky6tPlcCHO9aWkdxt!w3(SR6|WX>!Tl_#mmqo$d`l*{ZfS#oA6LG`0(mf*e?fSCoDq>uWm7<`$1U#e13Spp+s?_q&7$+$@Q3Hixi{V>ye()CQQnBE?6mTX0~S>*Tj^yX%jcMT`!B1nGa+~$QsXLvQetDAE|{5+NZ{pIw=N0*@?->GnOdYfT9Rn%HSCZ{0TW;p#zs0%u%tk*e#dwM@X^2}k!dhJBPMsC~~aB-U9T&M?IhC15r?iONOxi{UeFqxfRn>z=(BrQsFAK&Tpd+s+0WMY}JT(;4LvFwDzBLzBFlxw_U1$Tr_O>_3~_h;DX5k&!4jdFiBY@}?;mewKQ&n-ftZ9vlu&Kq166vmg){o_+S&m>yHbY+dmgw>`^WT+R}bB7GA1^kWwyUVyRE=x42+2H@44$6{Ls!}*>j^E`BMv5b1M0o!tW)s~iIDWr`eWK5uf?d>&TWN}kC8I7s3w4Zrc|c+whYq4sQmmw?D&~reauY?4${7EWkP2s#)YLtp3Qx%qM*4>cxD^6ro#k6iOY8Fg9XH%E+;)tciBd<15u@Qa=%?j>G#aP?{Vzcm%DcD)J81nth72KTbg@eM&<4(Z$%!G!GaXQ>p_y=!FL4c_%f(taBy2XYPYJ4mm)Z5@;P<f^6$b}`I^fA3ex9%+3w)_({gaG+%dJ88pp8F|Pi;OE508M@wgQ53P?s1VR=&meeY0(7?qWitm@5#aL`>Ek%6t-Sr##PYO-Xf$Ey7!bJvf!ebge8K)t81aDcdo`F3VT@(n?KgK35AFJop+W*{{D&xB2e+?&k1~kPWWyaf2jeTGN$WutDnDsr=DiiZ=TitVwxs@(gOHb^Nee#6u0x%1pY5&d~LP;n^&U85xcRg=3RvV4kC}o_k-L0j9qWzD$-2I4>=K+;ACldAM&-)K-#*Tfhe%A(+Qe!=aehwn0d^_6(+cH4pN$bI>HqY<3F2ZuVMFU{=I~oM3`~2}AYPN;}%Ou)Vb>qyb97jl8D#VzMt}vVtcc0>OP=B4ay}O-?8sHop2JAK>F0gf~pYFs2>+6QZFPm^kojBVTx;sBa@|Fy6kWr6Sy7SRfUGuB-)TaV?(g(`Az?;n0++y4yGgTqY|QWzBU6>N;iHeL|$EN8eP3uwbAL^O%0907J^MC0_$&j^ZG{>=dm0#jSI!+{1KM`%D}a=cL-dBe;dti@y4q2?GUNkpH#$H{i9BD@Hy2LClAem8V3{AHjOe4~AlD-*fKRq|Xt_u-$`NP*UHI!e^4RM~E7Xo0jUL?SwIw2R!bMyoodw)p3K@cQR2eFjl;E6wy540#1M|7ED}LQxk_*T1h3HbQM(>l)Niz4eZp3y({!0^^@B~yC>jp`AV-4!yNDuwetqXrb93h(NLAjyw0Td9!>X6PPW87v|{vnsDsix&{$Btw7N*)EnlZUv3bN4Y}EB>RGr4gwCB3IBV~mR))K;KFD5xyy;quCl|T?!*1!cN0(l9UYhHiAf214N7z>2%F$Cl^ev;qlw7<h7gZGF!y?8*kK<=lcnmG6jN&C`l?0Gj^9={i1C1@feBYR}3>#E0Z$BCBG+TK=JdXdhgE?X|bFRri<8O;RR8`qZR^kAI9W{+pn<J5%NJkf3hw}axG+h!10QLc+!17Z2Bl@O<RjNx!JlD4Bi^>gFDV5vg*w5<}Ka=<4pp-niVDC&VC6F7nBVHZ`Z0KT)tAWsjtHly{+*`8VdQyx^_^6AVCKyA$|hdTkkNSw$RC*sq-$Q?Pt^E=4{m~x-?5va)UH4n5OEYCiNJrv=MUXuRw*W&DUq-Bz7aul@$;GH=g>bZf%R4SOOz-h!O5BERd7M#La%=|!$FSlukSTohWGG`8KtnNBz@ZH4YH#BiOBOcwEE-VrG-k=)j%6M7S0~ObE-U7HwR;nZx%eU*e<*=wpBs;NjakKDWi#*yMHOqnDf`D_bJ6r*2`--cSW2G<s>O1SIzlWZ8XT-@Nn4Y)4)bp;X=YgvO1GdyGl)PnaxRO@4(%LN<Z`1IOMET~W!C@>{an31okeDkf%aH=4JqZnu+^Nb3_Xo3M7OZ32c&!))Hj}h^i-K6#dLea>vy%55olwl1d0sT86t~mnM51E&m)==aeJyT3-vr_x-yo{)y+Kajavxf#9Wa5vx(`)OeRUtkYl-`s@Q++L7eeZu@mp~7eMrGfP_~4*M7os5-r!-6Jbuqk>*8)OQuVW0IE7l9a(&88OpGVOsjM_kh1&9oV|Q^w%H3Ef-d9iA>9)lG#@xi;Nn`!aomm0jr#sWK^$Sa+srS<K*Wjyim3r%A;#Tb0$}kw!Qbm2y#H7u=Z>k-r@K@z_5%nUBds{m#!7%Rh1&vd2hDy?o&1PrDDY${%)MKGiUz7nkW5^DboUmxEgvl2i2r-j21*&gkK}r5`-mvmamRTobVw{s<sF+@ARcxpjObu5T+Kn>jM(v|Ve`P4@?$=}}cF#;-Wf{cq*EN~&P1R(=uYIs3fZTw230V12VF{>>bXx+#ZEJ;THGcIHP(rfq&JvKZ#a%7|D4ty`0X1jWYTO$Y!j^#D#r$s$O<e*!C;v&^N*A6GoyvngiQVw(r8xe#@8hcgC(>KD;$qHEm023+ASG|>v}bHFwOr?!-;=^5_`;6t?BI>qCvVSM!<(i(4VaW=kUFDVRJMSQ_5!>=nUwjCUXfh@Gjdswr6V}&`O};?QxZ*h+^ANqRp3g(+)kB8u-E**f=+H1EEd7>B<L*Gj&)k*{wY49ZG`M6ttSYp0-tYsoIg$|NxEum;<^sY1pBhtl0$4)rP$*~FU9_q_Ze~bCjZS{rdmw1Xg+T=t^#KAJ=2c8F56<nX}Gy%SjJvmTrLMVPNwO!)&k&`R{M*qI2pMFp_!kSwj2u&92e!J=0wUf;4VM3uk0y}wG`I-i_C?+l7EgZw{)nU#v0bIPPOK0vw?2IV4DjzxUO2XsH;cBG7FS9_7@}mmlNBr5d0svvFHB81$;lB?~tSD%@t#Oeg>gs6T!KG+QxJ9DYDH;-8+mKY-nDm(DOzqz5IKL#a5t6mb?c|CN))}#{VGJ7kA+-BzVmyl`$HRv++N!XJ8svUdc?ADL@$@qFQRgA9;{&I;=W-O?cD;^K_W_{obE({?AXq;>u~Eta;~Mpw|WRPq+m?H&RpS_~{HTX)MMBwd7stfBxpX^h*9k#miUI*oU{Y>shB&3-F!W^>4<#h1#x<U!`47+*^C2pSSMVThaI}9s7|T`*7W{PX-*EI`+H8+|J<@{k#R#K7LC!k+V~(^0W6x;w|&db}#4&Ag$R;@yD=Z0=5zc%H1SU63E7^?J01ah-NNf3Q?1khuk^o+^52p25G8;v|kKTRpre?Zj{=snzME*M8}mlf=27WjAM372%->9PEiINN>h4AG^B&Glnwt%@g>;aS)*PdW3EOGWhfcwj9lNaK%ALwq^W1{;EE<u(lZx5YK}A->7!{gkq=s>DOr={oB)cSU4aTlb93kfWBN2#>3pzBptMz7ee-XTJPfMC-b7uJvmBS3GdqQ<X~wGWVQ<4G7_|d>m5=pa=VTu=BIX)3SClS`<L{6z7=Eb%(Ne)zw*;?oi=XjpEZ3TBrs(Z%0<V<`<PYEM>>2*Cci0@CP?~srMoAZ&<4F!>*arP`Bj}!BCgK1|$%ZRZcx*k4u-C-4FEG)<Cmf#M_DZ&Np2H`o?FN<QN7B``V2kS=sMB$Pi3?Y~hp>GC>lii87i@p!2&o6Fto*TTkq_2`Dq9;)W@C8G@&#Ra?;e9I(q9Tm=pJYlSF&XCN^lR|$J_GS70&zh`yFL=1oi&F`(4}I!>=s*q2-F+-|xD*-}$%gccCKG(%bgCE*jU?U2S<6!0xZI<$YW7roZ~FM@fcE{gE4VgReLY;V*WJZg3HHG0bV-6mv1)f+g82Vy-v^T-CNvd$jiZ@QsFD--a=Wp>g`!!>%5Gl7DSngk2<-BSfKvlp8CeO*?jK%q{IA<_e1uDn%4@h?v1eVkq4lZRsHMI7PrE;S{QlD992RX%4a$?Ns2b7NJ&0l4Bd1$p$RR?$6?;8QkCb%TP<Qqj}2a*y+@;um}s8`W$4LV6X{(&u+L?na^PRWJu!sZaDD8g;2|33b;fOw(zm`web~pl@d^8^HR-=YiOgc_CgahyE5w6L6(&8szGzI!qzg#YOQg9H_mG3I14p~6;B`tVY7%9n`N}+?5bwJ`)23O@Y}X_Z=L^<*HycBfYIEdwR7QKSG&Wq=H=XmH6bn8u`bzRjgmt9TuWMGo^@-WRG`8ns#>aUR4-wKa%J65<_atOS%CFKU(Xainy^wVY#IKBQ8#_<1Cx+wiMe(QC$rhU)=nY8Lac|YeO$^*Sof+DPZp|tX5W{m(I*HDJH)OH5Vu2X99@$MPbI8+4krE{PEMM+gb@0p2a;-OaE~6`7w@?Omg7IXZUxj`Z7TP2N<6vvxnS!c0X@=zSp|vH+UKu9&KQ8}WV6mLZ}O|FWHVC2kL9E}&2-J|C~a$*Dx%)6V%0_xsJ8soG}BG5-%gx|t4uSJH#bW=Itrj#f@yG!mdoEps|M$=a!h-@`4!qyD|dM*kFAqU8=D(0e|=49mzt1*ewe=Kq;DzU3fHuC;#u7ks~(oSR+tP6ZAsxit={kIF|{r?^ARBNgKpDiu~2%$PVstnb}RFu8*n!vjXJWHNF~Jj;_I}uc2vLV<n-Tu<63zu&i$P1$hFOPSwVIuD+8oQE{?m(Q)c6}e8hP<MLg6*K2MX#hk{n>HXRV+jlv<zQ<s+}jU4rXWtC)sLAs#r5uUN7dTnI;FLr3;ElGNLLs<@qWL9Dx^4&*+qCI*-JkL#QfMnu|oc#(F2(j#v-v%2X=>a24aU~ZI1iuHxl`X^Gc6qlyPDC00!}n+fAv@kn|M~KUL#bdO$SednK99|w6`zgMGHzjo=48hUL$)vzTi#gHJwi9dw}RmL8sKD3@1$;r#)v(3)Hgy@n5m*8>J8Cv)LK(hheUmBn=HUpMfJ=Bn5#!LJS$o<oyn#mSMgxqO23myT9EOGZChaUVH*`Q1jC9FJ*~JrLJSca6(l0c+NPfLtg;9xX@)meQR4+vXvx1;Wn`SvW@HvmoZb+vCftz~#SPe26GgA8kf$e!k@+*&V?=j5I9^9`f(bSZ?z85%Rs-TqVg(BYpyM0me>V5Df7aX}!cW4(0(CMV1CHYQO7(|gfTj$VrTx56`spm6Q*ob{-iVmJgd(W%<B5-*u>od7Yqrs$wgHu2vLq>AlnSL(Pg)TV)nNoQ50g}nUWqy0Oy0(-7W4iIV`3sb)NUkend@PhF#UiCDPG`8D&ic$`NIvkxnBfH@a6r*R|)WybNn%a^Pr%`*-c@~g!~*qQVE9I=Vla@n6jia&he`7CU*^7z4b2`aF{)}TI99-qcKJcVFQ>Wi8Vrs^hvA&$~q7dHE?uz#2WbmbuTQaKR~2Pf9ePSUF^P?S&-Oueq^=cz|j#Oi5)J-e8O=)CDk4iZx2io_Y>mj1EO;j4uUxtoGAY0Pt70_A8f`cQ}G+G<6Eq?O3$xAF<#^oC7Do3GA*YHI>I;d35kk@TbTp}{!#ETmDibgQD#($%@ze8?4Ur;L}R@N@qB=^=W>uHfjo#qgVoa-@@i9;v@8p5N2$KnX>}o$gew-4;w&nTuvmEo#1Jot<ZNuiE#PYS3Xfi)EcVy-L^N8cRE#pX4mNm0O&yjb48Z;V*82z_On2{AgmVLDH;ElYvn|qXRAsrU9tb|T5<b8Yu2l~h$1a5r{8ISfO7);sc~1hBk%^0+gb#SP+biLND#x3t8QU3v>bCa5j+HQCqVNUceeDCo=)F<<pd%FaQHqXRS2k=qT-}gA*hu^HRq_YHNEU1PgU46{Gt)k>g$(isi~3(&Vs{q82P#+{{2a6Sj}^21%kRAOlmXk_q4EO3a~r$6K}u&(vEJV<Vj!nI8vR*=5tmJl_K~W5qZKY(h3vJNl#Z!zLCI}`^|)M5xar)4Nr@9{u4!<V7jKf`zC3v_N)06o%J9=GMp7K8KA54oc5?=(A(N?;Moc$$-4d{rPywU+V5Nz^t}pS{`r;Pr%lPVD_az9Sisj=3o>{9d03eC39m^!70IUmTO=}-WJIM|;`3#EV0gH3Fih3FL(hk5nqF(i~fdX03QH8!QUJL}0j~N74JX2nlvEY~epYR9QLY<O|7Glqiz(jyD>fjmCk${k(j)B?OfgFpuR3eoWrMMot`m&xKf;N|5@g(xA4D2SDx88RdM^2l7n_N=qgkK4xfx3D2JWhSGjUbx08hsR{n$*JgwaEL~JIYlK2q16ERqkLSb}3icGxlrUjs$UTlD5Y(jV1nbl6_(|xGZr!)=ig|!nTYj`i+rWax$IpMEjg9f07MeX=1isO17?@y4H<}gtIn>=|~7ND}!ccL%B-AkgSk{dO8->*;R+V7xUSvk!@yy+GHuiLee%=wq#=xmF-fZvNmlJ1#1HB12naws)^#vnmhr?bo_l8{VH!Mmmo91aq1VVeMl0S4^^+s)f)A#(e&<&v5PI~Z88^F>e;&CiXECS`)|B;^GD0b&G&3cJVx$7bz3k%6Nj*RR{?TUAqe}*G26wijRK|yajQx~7pP4`O0pKW5;o@^EF(%oS-@2?>N29C8est<$68CNyE5*2@T8<H1^Gr+i8l__<|wBToG$Ue9fWNV_JK4Bp}5$2ae?sZ`>KF(#)AaKK1mstG0t=AEDS{8O@ETuHLMSEqBE;2lNW2&yW}wt<l<F1f}h2>8j~Lt9Ef{1Ev4~1BNgzWj_zblowsE$Wm979VR!NTfO)m;ppuI6#Pu5+uP0%fCUt&Jr;*Kc{{T4Pp*CZ}8B8SDBDmSQbonprK{#eT7>Ej0l#b7i%6;VRAFHo~x5^Y!s6D<uDjpAXuXx4<*_;faI`y;<tnR++ati;2JIg6Fj;@x|@<;Fj+^!92qN804ghYxY4Hbs&*o;}K|KdroSZ22<>qUymrI-UIE?^CWxhx>6k2faLTrgY-gL4UO7qxINtBzKcfyF|~nvoBarl%1T>WaEn{0;ZzeyfPcBa8Y86)D%VNU~8en>d_-2%J_+r7Vgd1K*gIt1Bt6$%N#sHMiq+b9-7Ix3dJ$$8Bqe|L7}?!B3k0;Zl}^IhnjK)|<HxMu2P^8x(OtMp;#(sic||>tgF0REi!6J(tEb#WTbqMJbv?m?{_G)hDHQwq4gD#$L+~&Pymq2zQSBsYQ8vu;i%@qU1H`^qQ?uNu)45A(LBFo2ZVxp+zp1<y>XsJ4$G<z*)ZO`Orudz{>#=W3BOhg&~$Zvunzx@Ia~9UGtHP)A4V9U279Z$K~3D>!EbrZO~9P66@_1N-27IvR^j%V7ir;VPE9pH6=sK)oKd<Ds~jdL~uU&84wy?|C(*hvd6Y;dA59)D;JloJS|(QY9=dd#@74{LUpg07p!W#7{l!atG`^ZNQ;s4m9N8a14^<ZohSrj*fDz-fVz%KsjbS-V7Zpj&_*B$%r7T0C2~R5?-3?Q4zwi%|BdTfP1HUvYV0q)cYlQ-1K>hpUD`ypSBs@w3A7lp)s%qM!AOL}P_>g#1zXq^^5I!%!fXhr0+j*YW(h~Af<(yZD6%-~=M<Q>dn=Vh6_=RRdqEO|71*nhEq!;r1dD)Nq;r^z6FlYVCig{ixZv@v2mblkSaM!Phgcd8rj$QIx`Dv!YVbkPflOVtxxpJ<*%D7oxb#{2nJKv+Ij|st`DntoJ4z<@QgDT!K2nx;OVKrkiapEhLBb~oax_$NZp{5Q|Mt92efM&aN*}ss;@;RZ33N(`>sYCs-BhYa!u_^Mb#YyoB1{dFg|hZ7BLoK1Aqepls^d<qY8FD9IKosWah_XtDEEyGkSY2+Xvv_kgUk$iY^)D!c%NUiO*ZSc$?=v-57vc0^Uj>u>pMA>*2+~ltO>E@Hol1s>*CCYMQ(!X8kyHxosnsa6U)}(niFeR2r==J6YJar0%5;geNl`KRoZ%q7f1TuDa&9eF#sRJIX2J_FWYAE$l^=x1ia*QD)G*ldqFv?lizr&O%HG{0kC6v9{`Wr<0h2jA4_np{`&v<HSP21=04v~rf<mSR+DNaPk>x?y~(>&S+95Z`P?ksNUrvI^4jK2{vs=xHhDTev0Cbz)h6FAHhIfUI%lpX<>_`Y536(RwA+_&dALeXT=S~kew@;ik-)`J%R9t}jg295IW921WY3PT-63v9QnQ)!l#|E{33!PI6?q!f-tiN=s9$gCWo`!?$2N`&n9Nvbwb^`q0~>qe|Mz$CExd3n6eIigs&TiQ1dV*A&dOh0xHoKX*cCd!4$#$=b8PJnPH=F8*<t`qI77n4JWaj0_xTBE<E7oeHc<fMfVA#9NZS=CyoLX}SNDmVH@zoY^u@M~fII?_vODbT$T3(l-Om<<7=TixMs0tz`h|=N)1_8+5V%olQf%Zm`tCFjHF9@iVCAGT2co4Z^^|Y%khzr%7I&7tX^J}^-WGR$D+qf3+1HgiA$zJzDvgd-yIXr_JzYwRBxFN#WhV#q{Ff_f)J7(V<D6|fnyx8^gImukQ4+-9B1Piuo{Bs1a`nV(ApjF<isUcX&83S|Ma#a{!l|8f2q@pbd7IzcY~Dm!Z$#ll4MjhvNLWKTFw6JaPTg?E;<(z|d7SRwW1Ny?7;C#sG<HB|%j18)`Qst}Xeh%U7xf7-bP0SgUdqdlRGw=C4MwS(wc{A+%GSx=Hx-$}9&LPeX5$NIDTBnAW6Au~^Y#4GPL>o>ill#YB)$@sNX$BgCec0IN$szERtw>^68)B#t0nRS&ojaSumk=i?730+j&PR<pFxD4`m1E+2rg*MWsyZ1Ct1=B<C;$e-ECxVBz+1WHrRt&BPLMPlySCX<=h~B)JF5aO){n@sHhS*2cn);w2G9Gz^q~GJQ=`?p9^-5WcRd?(}XTqAn80sBFj?(mv@adFRN8%ND~7SgR$(X>}c{&Q8BfX23V*yiTJlaB4}bKA?XU52=4%zScuAS`?H*AhEBj%?*cuMFVGW#YA4M*04P#@*(HDi&YiP=#1cax71MTwp#U<XYpQMUeE@|?LR0`nTmUG>YTkQjY+F=w<}DbCs`%&xrV_4g1*51IzUTzGkxNE+GmHY#QI|-H&9?wa;eY9!rRd&}?(Oj{SLt3~Ur=_&a4+3MUU8uEky1a-4<adi)z`U7^l~E!uM6=bIz*rjjU-<A9dz;g39qH%u_LmtY96&1N7+gFi22<K`7cX?7&|Fesk0IjZJNG!-4-j|qXds8siPn-xP{tLLW{~hG<!ARe)+Ynycb(I%DND!kI3c7CA$8OtTQ1P>A8X>oHZuxfU5V1Uqc7%1PNcP-Irx$FUQTYL2R6m$L053Ai$BNI>rtLLxkk*k*^7O&8Xo%B8%lkK|!o#y?(<fDkdf30d!KSkPN7Mvn?yz5#78pxyLF@9Oa;`U;(BFXa;yr(L}3JeWNGN{PN~5;58@*(wJUc$*#l8M!u}X0{t%Z=f?D9CEr@k>Yx9*B>vWEbV^e?^LBABDsxVSjJmC9h&wT_InX2E+*p6uk8WKZ<*imusr=0t-m&U?$=R@qLZfiF*FZ;*$4sQ3-Of#Oaa+NN-K6q$rSjJ|ta&$^k`at`=$p_N^LWC9Hg)J9DD)Mn^0k+=@xNww<JtM=*WHa5?uP?9*H<_dT(dr`Zv`PTI~l45TDIRrY#j_rkeVspX53b-aa*dYYlrlxj#1t_GYoF&Zqf(_&5cnF(I_MrkVTmwQV5d@$+h#M3*x>3J331$VS^P7vV3UA9c)k7pD7~}P3jmB5PBd4gYcp)7c0uXLvf&E$eyHVK+Gtj(k(_;28P$fNPAPRU`3FzuL=i%mj%%G9Xk$@n$m`){!eDyhG!}MlWHzR=tfyv4*>v<TyibpHuw|L&|CQRCXoynVI)EPKacH3uW2~Ag@niJvC*TR+w|guF$#$ijzuk43g%Apknu6je-bR=j?oxZ8r}*Dk_g3+B~7MMM?jDg`9^`QV<wi?ype6PIqfPzN07m`GmZ@10;0KN<1H;RKSFn@iRP2cYq&5bd5AW(!6e@Vf`V;hGG>KUF-dG-BM6`nW+X&}7*Jo)nD=&kC4Y{_EoKF8M&3?NFq-^;NDZxFnRYCL^Sq=A${G|i4Puf_dpR<%V%e%G`%6!8%4`bWm<oU?{R8ed7nZYa6$mb;un(fU&aShWl1^x1;ny;cNtr|L35ZRuepEPLCN9VXoZyd%sf06C&0rcg%m#BXVHfWzhEs#9VWYEEfaiTRn}#XF#^!A~6l>>-RJ_&dJ0n85Bn9rE;4|s?u~L~UzgZ6k9xZ#R2ipOe(D0aE+&px;jpA&2U9`wkiHF-Gjcuu666OXD6;1323rvjC-H@e#h6qGbH3*&(F_Bf8%U9K)i5AEJ0WBA2pD0y<V7(Gw8%lmj9h|wY^{+0xs8{EfFXMyMtO$p(nvbu3n%<46|1?!xN9EN?7P}!%m3OdWUoAxwyF?Oo>V|Ml79tmSU~9Lj5vg6DtMaXAl8M*79REuvb41?LCdhoz?(%e5T;-tp#koo3EChRTY^GOwU3#0l_27%6X#md`!Q_o<`8?Vn@fGpu=27R_%D1`+J92~&dMhW|1)1al?BIUEy`)2%6GSom*gtK1^wIh6ypH>HkJGUge2+{K>KrV0>KJ6a3`y`hv23S?m#qw3VIGR=X`0JoFmMgoggbJSJPcxxHdGH+Vn7Wi8Ul-Q&D87Z6lztn27r5niU#RN_ecjaspNgxNU{)}s5*C{IS#<z26?rX;O<cVh#eL#46M$X{UiNPjsRBA9=N9;Y5vI)`={i_pF~wL{iGWQ?sy5S9IoA-SC_GWWDFj}_$(K3L|OR@5tX%_s`tCYLfYC8!k@;n506mnCX)zz?+C;)IYikVxH-U)SH;0CF@`-itAo1Pj&^#))jqnO8<c1JH-6F#s)ZbV(%#aQi^?tyB30Iy&uom-b~zjxHGJ|^)9M|+Y^dg3K{7}QhH)ICQGGHaw&FNPnwOO!_;h!NIWgq#I5<Un?*hIw{F7uF5@GR+>Q~)cfMX6LE+p!%T5ozERWgYiUrFBO^I|Je)!5kFawhZt;*2_J)<~=hYYFsXM~O!5L~Z2R%0k?zmy6Z3wR6x!v_)EWmqS^Q@If#9pihv~;j?=31{~R+aR|%Jz_WgpeAWA)2}Cq0&PjHxuF7y`_0H;h`1Nz`Fc#igFfp$~THUkW9=_l{jBh<^>ma#)I+FmfJta)bP<C!99H(PaP}{h$+}JHC3>79sqyweuXuCPBsY=GQeh*G{zsk1vlh(<+eN~kZS6^t0Yc{lmuA5)(QTBLpg%1Ziw^~@si`}3x5!7s4c)Nq%WGz&+oIcnu_Q_EH-CFzg&uIUl#J;1XHkUiFY~!XcSgk6uL|Iw8I`B2;KXMy>9TB&m2){lcH$?3Ni+unZJGPAHvqKTnFF@GbUSgR<<q|zv7)-BlQ*Q#yN**OoP)OiffeQ9+!<jwu%5CAd(3g<@2n0q?0XHPSfq)DzLt)0=gie=r5QAX!eWVHoEWgX@OU!gx*voRZr%oyViD`+`%zA+on_%(+F{MWUsobV1r&K;N|K+#&lYdZ*T_V7)ozQhv*^2d#xiogwC}K6<SebW~t+I(_c(vIvm%&#teXB?a75aIV?idk2ELFp)>ROxaD$+{jilqhhjams^O?3u1n>jHRdn*V_2o70M+pPTpDeN^_1}3$I`l+2h^|#GYJB67o;Ym0S=Cl#8cetA92m>Q%QilPN*T}iCGhlzeF4Br2fncRo3mrbVQDt!_Fqf5%F{A$2t4erKx<&A_+fziPv+maMQMEicE~Pdc9(7SA5g6!00>ys$<eHdgdGQvcp%QHD;e_S)!n&Jf6;NDYK|6)U)DSxbg*Ok5U?m_-{3l!lIvCiy0M|{pmaC)Jvh6ZF0x@>b>RVo5ZR4<eG~3)@4Hz@V^3P#B2e}C_pT?P|2aL76aIhI4^mcsKs`mV^!hBq7(F^C>=S^n3GQj$Uv5?a=i<{4}vbA0ayC(burQ1n_hZK?3JMgD;pb9brF=+3SJ8ec=2gZH;Yp*#oQbH*CEQ)Xs>4d~+(QTV#DW#Td^dJ)f#F<DRpqahGu|{os_^XQ{@1-#6{3L+NP!tsd)zm^YMcUY3{mp;E5jsC-d!Es&>76=fwo~?cVj3`Ty_ee6wBH(d+8a)izC@j{l=dflWst%oS2w>gF+6Eo55@W4xV&SJN|WV{j(uaCW<nnk<(|dYcP5zM@pe6Pg=F)yo3}aC_=5a4m`zK&J`E&n;ASE+limdxiY%XGXLdU*`H`*&>yyMiGFyX8Cg4HkiiomPNE_p#ICh<Ir8<6f-b^{UJDL5o_`kONOM22tE6^{jz2+MjFu~-Id3j^~^gv}L+F*?Hm7ZUj>A-6sV0*8e9?PF_CZ?W3IVXiHePG!c0}4hI8`h#x><!(2(cF)mSB04#$q-VoW9T}>@4#YG|3lCZEX*xICG_}YYo6su);vbkdZGjjSiO?UCgVd+Ik!+7pL0{zTCqwr=xa|sU=u9L)$ocn6@1YVF@&#1Yl+WiZY4Ubi*vmsSnbqVyy{VE^3~r&(U<B*%lA${Lxtx`=PJ%2Wql1wR_2;m9bw2+@y=Zx?c%4Mm}Err9D-W>92ciCpHB@_z1h^cdJUbxxXxf?m0k$rSZ|Q~`O37-e8O%zVN=dk7f1Eeup^U7T(m0PkLBQ@D*c7udJkxKi45ZdfwK-}-e8i(PQ7?Zrb>H)9SPth516H}Aas*}4q<*Gt{{)3dvs#ac8F#LXil8lTIC@coLK8dQX~LZWn6*2>IMtwMZ`_RAq)>O;=M3ilhW+W>&Mqq#*e~E&O=PN=bY~hJAtkjk=q!Iqu*sibfJXdFh3Z}V=>=W<jbLoZiv(x=}Xpe{y)l-<E)THX|}ZYSqo)*LA}s`wi=lSSrT#+b|PeS`%u+tqq(vok@_FMmgu)!+Wv0zYY@KIhrR<F2wvL1!2nM}@yWzy8T}&brV0v<KrQDbIG8O3Bj7X9-MZN^T(|`ZB~3A~U%O=oqBM<NwP5JWq?1CPle9iFq0ZVo!E=UBNK$8TD7T@NVX(eG{Z|>EM{u<Uqk^#Mu>e2q8!HG;_$Q2ujYYY~D!~>n@J}pJC2q_#{09E1;t+7t$g7oKnIRDT*Q~Y{|DEQ~FE**?CWX35eY)78pxX#G05<9`paU>&fsP_Dg|sDgWO^VY%au5lA-F@?sa%W=kx(idqaK6}3#kusUwYm?jb1*zRq2~OzSc-X-khv)8i4ydnZR1Kazr459v&QG2N5<j$_#4Kwkjv<B=OvHW3>@yO9}j#LuG5gZ&%X3v|ss-@XA{1M^+<s{KO52I$VI2cr?h%K?c2Ype1!%Plg)~3m9Ys`Wi#FQG0Z%R=~ar1Da_oAD3@Pg#_+LaW0S#!AdA}bi`>mMhnEP#4-j0_1^T=4Bz~}z5jBP0iwRW+)TWY<#KaL9a(EgFCm$O5lFDyv~+oDtYsN$_1=4$KZSX%QCK3(Tk_K5wLj&&T4Dxwsb)?A#92uiOAM}HU1eB}4ZO2e1Vl=Z&a8vs0_7zsov6mpGIUy|*$?g>!$h4GtSRE5JI(er&jeeLbP1xq9c82yWl)R3YdhBPS{lJMFfI>p;IuW!-;^f6Ij*#&_a9x~{EwUaU@em6S|m#m@R|ebWG5d_U96~_M$0%Fum^dHSw@5Or@RcXb5k=wW4weveG`wUKLtkBC9lDi?i#ZH8(d=mIEgbLv#@9B+7GI_ar26D_@x`up1q`&Sg5@k*L3~$)R^S1i2y+<4?CM^1@{6@;p1G(&9tKgjS7_;5OLM%^|A>@xQBFXpi(SU6gVR&w@diPhETwk`T~SW#_ze`6a$#WjQ~pNSk9eQmO$`JiADy3L_3u0o3oF<KO<^ounDW#7AOU*Kbx{Zb{H(VCD*b<V==&vHpm~=mX9Bwt$=a06nB<br(E6c;F$a&Z0pI;DUr}vB`;4<bdeHwbXL>%51m&sH^DZezyryT$=pxM$$SO|0Ali}f#BVj>^Wy*4%HNh!8*+9?h28RXoZ+m|M7HlFB7#ZYf#{#DGs4|wP0JxOcz=VTrErhym+bOaZy8O3RxSSbJ=PRygzc?^K7v}wj1|qN9r~ZEHt9-L?(n35FY$!<sZWLHb@j3yzMU;*Y2@G;Q^L2XBa$5E_}%~r>mHUjw@J>7!fQkaCnv%u(!%qUAeijYXvaICj8}q<zqCNQ5LD-^&Ng*JO(q^rk1(^V8qo7sV)0C6m_yPL>7SC$~aCETif7FzVDkYxZPNuO#ha<-UB5%O7461>OoWgy&R@*WTcEJDd6jr@bt^cI+3>AWzGF^7D1SnDt^k>v0(jQ?*mGvMemGDW+&4&Q~A}Xhq(YK=LJAn=nBbW;RP%r5tn=kN~S4f@YlHHE1SC+j?4h$0*)+l&N#u5;|hqJuYt(kP{_W@Dkqwz-Bfa$Y%ya+Ro_r@Qz0AP4sSvsvtL(|Jdg+<DW^)?#Yw}BF})SFLwc2l8|mOyy}HzJOS6Vs6>w9SzN9<wUaw@_AYk<I6?btR{;OA24lDp%!0GR?hO35K9jak5RNW>K6B13JbSWa)PXVB3^>@lQN1{!IZ<;I^8#B$)_E6;vg5W^OOB9;|ggd5h#NK5}fGs*Kv)6CD8jOzJ0ypVPawMk7L4=`tpX&g;wqT5v3l^ozf{;zVAfsC9&RIFJd`==?qOC&S9C0mmYml@$4CJns8M@8PtGTPEg4T&Ywv+V0M;&GV@N2==&yY(3ap8salrv$?C004{ZiJG5`&|1!@d+1rqlo{-*8hXEE==&okU7G;QHW>J(*eaAHKofvIOB%nH4xlG`YBGVJ9>*W$Xmgl{!nHBYf>nHd39Km`ep%gNh3bGrVU~fos<Q!@$_UG{z+C+f9->1URRsN#EQEiH{%xh7hmvp8y~KF=yx`u3bNgG^2v9ceA1MKnX0SRcZPgv<8xWx;k9q&DYaB!)I8+50hbd^3NNbAb7kfOd79uix#?BfN5Ow?YJ#HAmA@xhxFb_IO7mAqmQ(G|AZ3vv6+5}A11~&jF0CoUlBbwh!_+XVmKB(p+VZZ6!{5}*4DEmaA<cJ3smR|l-_0f*SP|jtHUE0hWhcuA-N}|#JYq-@EnEF}*>a@$E>r)>l!Obru>E!A7tDtiyri&q7knrlR-B`}Fyakdq%(UMa^a0~e2!*WlA?(bbSri+q$&dW`l>n)pskZ5$SopG4pQMF^dM{0n-W|<SwXN&gnJVg)Zh-}b<6cT0>BV}&?4X!I$OJso8mvepL2>q9Piksgu!V}Uk*c0rj9f7l)eIegm?07bxxTECIP3{V^gkCP6P!)&B~{i-RZ<R9D;4j-Y-4laq!OUGZv^Pj$CjZD#x8Gb9|xrX7*}Yn16IvBWV@TJ4(H8!PO$ifdiRR<3Yxh6XhKZL<YH`0)Z9Cu!<^|5EmyeQ7_#cVKPnKe{x9aDl#fIrq?OiVlS14h3n3XP;H^AI5BW%kgS%ri6&?rRD;)5n4Aj>Xmd4DmJw=a7?A3OqW3oSM(Fg^-wd-o%1Tf%nmvm4;*zw!aA3Y%l;@WV_sSkc{AfH_1@4ni^EYmflK;WxFS)jJ`=0|8;P8mWI{cj!S;QQ}4QxwrbZW*(g1E&#B?@a!2%7w-FChG3?Rac9-hUy^NKoa5|H`kZ0hFof$0LJUXNMwg&wugkzf+FDx4&RZaARA!AteH8{khDEXAH^jp2%wz2eG^zq6-i^DjSK2wHUd-vWkqpB2z5PYSR6JBPMt5;Ee|9FKJ?+LFz8{2PU0<p?5P0sF4Pl!y?R4lUPhh)0DRM(*;Ltl5z}7u^V#4BxGiM$bObKLzn8{viOEPw^{P$!HgSAOnmb8`ar;yHKD>{BbWjWm7>a_9;{Fj{>}FZ2UwR2KVkPz{o^zcqe0=dw!%bx<&L?&thk0g-Y}hpY-KBbInSDA!!9p~G`TE-1o&7ZdB<Bl^^fUhA)(Pkb$P)6xL~Soq*V^sZ}ihe7m0owg!LlZt{UU%y)Ey?(V2RKhmI}wSQ0w8U3=rE3EmkAv{3U1(!jtiiC%2bIn`6B;iX=+arM<mf}kT;;Um$4En7})wIn2Z5wS)O4w{_2aOFG7Xt!jdmAMj}Ve8JK(0j$=toCxGAW#0YA5u{2aF>KR%(7B4d?t?ca)Q<5Vvl>0!g9mBo?uI%!Ado*6D+-%gxSwoLkhKqrU?cNi!m^rO)wfWnfVo}k94vjLFlAPnhQ@Cl*`!?Wo8@O)Z*swfTR#3=%9!v_8jByn)W5K6}me;w^nxpP1YMoS51Jt&@refAWh1{o3cPdS=ZYIyo5P<za}FDnX@&P{c^R;Qh@?EpfT4h)+~8T>;0s{goOMoT(5BRZf*G5i}k?ex0UCsrX1s*DPP=Lfm1di#({1r=D$oCeU<k~VlJxd5UQ-C3^YXy2s2PtZs--wW6QqyASf~Bg`$eB-X=*UDGpqX&P=eyV)HZ4Xnri9g`?9*r>5T`zM*D{l_Bq@07_xPQW)B;f+PbWd<*<#f35k~UHem5gRl)Ina2ZrGL9l6W5)E405+zlW}`T;e7_AYP9$>}K{@EGF>$4L)+(eLOJqT28^j=t;=xF>iaIYtdGClmVNY`8$zcQXC-D)z+Ha`;P*x`3)r}f%Et~xQ0M@;ToEWVQ=~ss))en-hR^pTNy@{^+)CY4jwLeMU*Em)WGU^QNK)$^Yag2?79iPH6CCK%tZkcl;@!gORpp%V0h0j2y0~d;YV)`1;S;CtRCYRCQ{f0pKs*v?7P(He_Q?dABok|p%Tu5_!3OM;7OwyfIX(Y&Ls#7^j5p0X0-9!ZptP%M{h;-2$xD1qE5&20eSElyPvQ$+;0=<C*%p$I@s-bsr0v#zBT52K%Ijk>gz~)4uhG2FE*b%7{Z2of+9}ibpC4Yrg>WNjNDSP!VxQ`RaVOF$tgsv~vh%x}pwbIpG4dLC7xf*w<&f-3MOU_U2opp%Wnfvh@x@0BbcYdwpBe|Zs@p0rW|C<4c&Sssn9-1NkYa8umsS0`NWQA01I2$7+)rJNAQ`NJm1JErrjwdiK!JUj&`E%MR)zokm3`(s=)&Fa0OY&WO<sfw~^BeWsidD^(<%(h#@u}^iMvw`;ij{D!Eo|9&bCqA$D*`qzJF~nF&CDRq^}?!=*sk3<_^q89;;ryZ=A2q~VQq$X^;RuA`Q6P{zbu!UzelBD2aD9rIJg>d6SHYXOxBv=8XKccqs|+2q|A_QH?dR@enL+r_^HNp(a?*tFFVs4GxtF0e{z-<4iLd+`_0vK^Di{Nh1oFvbma$NGjMT>)e^LTGRd|9zcS)S^}Iap$jYQcQ9L)$P4%SLA~FgIL<>(+SO6h~3+1QfOFswyV$#MEcPPW711{E|pQWehhx*{tX9M7tXEZs^5l1ff=A<00K9Bz%WrkYD1+eT?%mM-!ck9X2!V}FYq)+OplHm#1@sg_ehnnAU?L@Qu1IP&Q>ob6cT}3j&2KphAqK7B_QzH<L{ppFM$rnDZqSD5aI8}|fPojGUK-fJtLJGTQes4b5;;iw4W5b3287uRSf9jD|(#rl35e<pE_?~urS_8r><+(ZH^57t4AeI9jo-n?@DEH)#y=_~bDB=irY(p+d_%7J)&O$1Cl?~x9E*#7C<!VW}WL(N>N#G~xma@+HK;(GE{Zb7e(I+w177*nKVWc!tay7848?!pF$kmA5#u8crYzT!>nqk<&c3S}x)i{AqiaUxY61IYMZ&Q*^uDu(63YSZYWq^i;F|;Y;hXoMyhMUcX5GfAg1HumbQzRiAd)hz#p)Mr1uUd;nGcu$jXzX4l2E(HJF<>?(Uxl$dgBRe6B)q+3Sz+tN6eEr!K-{Gq`AqUVNS98GHWYX}T!4Y}Uc|^7#K06e7xUDI9q?NC))G!R11L**Hf)$+?;&}{`WMe2kwJ0z>}ebuGNnV31gbL^@?ZXt7fe+-489Vm0A@Yc6Uv>&m77Ol8K4qz89*Ixy3=YDDt&|DNHkS(2EtxEY<awqS!R68RL3F$-VQI`0*ZyPSfcoGA9i&VVpK8OjGYnh#I8(KA?~v{e;kw}x07<bPL5$rK#U>Tv}I@}=^|2vvR7@JV^_P&gA%PUR>gucfAUW^|Hx~5=s#eM^%G&9UAr#}ADW%*j>xfW3S~)V#K%V1Ez9E<o%E4?Z7flOM#_l%P@+=q1=2e|nPg8;>0d4Nv5~5ZHufF2?s8cC^{EjnG?EMwUyNXyp5$dmVC4&=^YW^rmlHZB{gXCfR{v<%?UXJ2LK%l+bm{wm3;>jOD8rl^oyyk{G6zuUeL!*V@wvpGh@%GSVW4aZE8;zrxqvcB555E@=aV4V&7;FEH$FprFh64f+EG^v?0nm-oO>WrKZIw6HV5x*bHQC6rEgNA)^Y*&P@&*6ar1=i=IqRA38xpslMeW#YD<V^59E+OI^tHJWQ#{seiOcUY(8u3GW7rPU255<b(`;aF}}l=c&_kqwM`DZ^BhA{8Qu($=s3ctJElFgMT6RD-cUV6t|kI#%hgB0uU&|)L=*oOQBoHsSFs|NXB%G`Q)SR~QqBcM9CZu{@2JV-Ds{@>--u8p^(<1Jx;|bZ76oKTTPHvBndS*@O}<*uz?Oeq%E;LB3&j}4jm~YsSGUV(XN8)q&pNlola7sJQDbq~H2<l51%cX*@*^vc1|<)T5{E$k=zJ*ASfjKCC~f4820-U=O9OPpzNkV&{hxe?rNcw&4Upg?#$wCnc3E}D9ZQeYqT>aifMG;sM#5`R%Lqx(s#l4%n}v|sLuH<QCYBqYF_FCFqfU*<FR^j`vNm(}4_34@gNO%-57A1BbrtkB&o0+0aHeze_<|3zda-6sU3LcP@Y>p?C&^MN56=SG(xUmn<Z)pKa%x2BRQV`Mj^htu%1I>sXUg(YE)S+$_eh|*<6LUkM^gu_>@wRp4$NtT%MWM+jLsI_{5h&G`-o+09HBBpVMfYMit-@hn@pg&MMG~vjRo3EQ)YqU!)GtS@e(Kwk5<`)XW!9tTSIBRe_?GYHwQGgeD{K3yrF}2;^U0#2e}V$TpYh$O<nST{>Jv)ofc7UAl2XADgp(NzAke1o<k$jR4q`lb$4mcZg8&K3iEqzOF<~48z5Fwm|r*V;HAYyBhQAg?A$Yy*hE8MW173Qs{GaxXNmcg9X~Q2&J`je3a<GZtx+N!sf_}Y^iuuw6H=8GY}T=pTcAXuL{`vl?dW=v5<#iu1V$yW0BwW(!B79}I(41VAkEUgKyAV8M<RTLzqV>VelUr67Ih9)SNcLFe(hjz!&*xf#@;1&S!BFWiT5<L;r@UUk*UO+^B=6Nb70M}s>HWeL{U*64UN1cJGNKi@N6-(K_Pvpgg6#sT657d_!7ryHPtW?JDLBz)$p%%Gb>5*O0L87Jy@xcNN!XCg4;V1cSFnCqB}@)4wfrZZ4tEI@;CGUs~n_hBu*8S?Myv#AKk3rpKX2{Rm%2fm{<-biPZKkK3fF^W3ZR_B$Cti4B?Wpk(^%ev&_15a9xzBR@0uaqHUqcg@LeR1?q4x3OiQp628(3>S@Hx>@&r(`>HHfcQ#yfI4!$l`D-R5p`>)t%zSgS8a3LN88}vPM+RxK7%x4v2k26sB<wZP50xb7GAK~oez00jxw|j|eK2Zv%eFJVdFHQ_ASl1)&ZNdS3RVIv$thrubAB=A2eQeywSrA<rMF>zXlji6KldR$#Fu^PW%-v4#T^9(`$=E<T9Ni-mz;41i?_iruyNWoD!5ewn60;tbYdeZoA@<W0noUZ70yoLp~=JC9Iy?d5%2@gL+7FQqOOuB%AKyP`a7?iJP;`>h@h)oPL^TKt)VA2p|$V8+6(=>1GIw4y&)QFV@laJ8xckxWJ-nVYn^_+b1P%<Q~C8b?=tgXYEA_!4-JyU_8gq5PtFA21l}w+t^8?+00=jh>p8+jWcxUg0K%-fVj|83<O3Y8L2CL;4!o<b%+#fV;kRkjGQty^CA04e1p)q4vLcDqj*vkzfmz(5+)S>otRVmzCwyHDM!)k)GE5EB>-BA%^c*y)h!i#W4=eYXw>Q?GoSZDDHm!tr&4^gqGCVBFQ$2O2DH+4XT#T2Fyec-a)yPd0Ql%Uib+2K_C!90(h?cojWD~pn|K8t0f%XYs#X%vh92Ba3`Kufhu4B8&JK>V4)M~D>WeTQ}mo6ag=g26Yr%`VEUE>5AP9at(uerxp+E&*DOye7TB`UY8?V)lLffM&wOL>~-8we~6f+n$|FqtUSxNwF~9;VR1fRoKa8CKM$yPT#?qoQr&`pRi4nL?Tk6+-U~!_`z~(_#Z}mz}{1CP-|1A59sJv=c^_@ndb~f4`eVR3QukkI(VBO02vxzI?Qre_4R~c7ec=pUH5U&YZT3wsy<d)EMyU8#jB7M5unt)ipFV^lVPc*|6lqQy?)<<e*q7@=AsJMt>b9Jd~$OH-GL#l<#XRP-fAbg|$Q8hz^)stqc+s>FD7pQ9oH?YB^SuW@J1kz3McZ#Z{L^<|YG2y}CYZOd^&=_QZb#GOBdA@No3jv614qDhq?Db>leYb2rW$<eXG$x%jV*kz^vLNx3ve(k8nIe;X4w?l@q3f?MYfd@zzvUp1o!K}N$8|HE>CHv^|2^=Vo<$OA{L;PQa=dR+$J+DxUaD;jht%D0n)WX&bB$*S-Iisc_H#mnBd=}4E3h~wMW=hAqE|Cyp~64M56fu32MvW~dIH0uwzmDjTtGc0~+7rX0U<MiuaUdob$=dwxMk|n|H4Cy<8XbH4;aA5~QH6lIJ>3k&p8ZpQNn5%n`-^<nldTQp-@Ou-tP88wB4IFIE1*TZSmaNN^HT|;^W{gd&g|{|TuZ9+@A-P~wh_Pjw-RvDepIQ&5ik<y5?No2UgQ-O0H$u0#<FwWf2Y@zLC;`((avw0{p`b=+eQ;98;;o}w)iCwa5g9B+#1ZKvAQait?kG!P6o~+p{|XDz+Z91M3G0uR14uNk4fT0dg2|4bBn*;$**Ixnvqwz`j?=X@w8E^{c4%e+@(#qvJUZEArHb7_<M#h}|0=>)l{C31QQeU=p(k!yd*b%9C$3TCeN#&alQV8Km<Tq5U<+}$UUuchIvI3Q$;7|SC0DKr$|!0r;r+eloO^?x?%V9<T$6pZn@d;Ty3|XhUJA5hC!G^$i3XEf8eiu%clfwvhF@-e$BjP#z2x*AQW)BbW%?A|GS;s{exXO}A&O<L7bI|m2qJy7ofowS(u&KA^Ai%Pmf7||ZMZZ7)Rt8FWHr2RB)w^v89ZOI%fSL_)Iv{y=F0cu0moF=g%NA{b#Et=s`vFkbD0!OipXFbRQiN)Mlcao!PczNc-BNTOFh5P9w=X7ltmIbQK;be0PiYRk!yD}GA(oAJ-)K9Zhk{~{n_@xVCqjX{gwBjHjF5d-a#&2W;;?_&T0d<FnJC&+)s@QZeAT?s<x6U6)sEH8_W>(r)RSJ#CIfB!R)t)+E7;_Nr68ak~$GdF@kg^1ucYNm^fhtn%3mWtkD=&x}`*@m-xACaTxv(R*1ayg5#bA)FQ_{Dt4=7iC|KSQ|{3&=!{)7G07+}wMrDhwN#NfFVuoJofQusUr{{#=(F1W60ldnZGK9S@v5hOpqmh=K8q6Kmc_#*4y#<WKBf(U$tb9xVV)+{eotTcQ?ntGX441N2};be+W`8so3%SITFS?v+l{3cbLk5amMLQ6C@np(zBkA~NmxCmA3Hw(S!9@yQK%@l;>78zXC||o^6wE%D{D`VT6Fl#r<83hC*88;<ST?xte2AK^pSzgxqMJiErj%)=B1IbHAAgE?)H{Ko2kzEDaH-IwG0YzQV)0J>PCRZ6KQR&Cl(yCHwN{Nqv%7SL>L?Lp!N}08qO1)U_~6m3>OKLLp3AuH3T8bT-4Me4TE07@7#=ZUf4uigM5t$C5i{BBbBR0a}$znO;D+*WwV|5a<#&-&I2^%O^S>em5Kz=$b$l%W0Rd_^s3FOrnY2GCi4Je#*lDjgo0LN2NS}JqZOw@r6ZI()1y#Kt`bqSiEP+IGvC!<0UutBwGAM63)d*OgmQS0evF`5&h5)ve#Jok+vZrl`V+;8H^it@(l|XpCvy{p`6Zee^1v}2S(4NSLc}}PtAiQ4qcmTF!=s~{vM5t{8N%-qs%<CM?s4x21P(GsP=_t+c}L5mBQ~5~ZC6=jj3xnQ3<B0*S~Zc&Gp%Hv%2H;1MR{u=R_}>%V_RgTJQSW8Dtr+|S#V6+Xfo=;UgEYr062o3gC!i<3X55Y8bmo&nk05c$8o^531%#Wf<dIqnF9kR!Y})xG5zlE<!E_fY7ZG$D+hd~XxZ0jIn-#myY0+;uK;nc`F2kj(4>kwZLL?KvXO{#Na3a=ptPD+dVmKj=wVHH&5pWK0xZi)uPlv-sb6XSi4b@A2YHQW%mFV$=JN9s_FSJSZ5z0uaW(#K0J4clVq=(qQt$~W$ReXXU@cF^Ke6}?m97(R&d5M?)GU=j@!4`tlA9wv{78M_F40dBU^(C;xb%C<Rm;FrMPD<x<IfU&?i+=p!uJtnayEp2Ur8!Ke4+DXa7L4W2a_ZiMfEw^TQr>Axe6BOP-Uz=AaG4Sm}c!s6V+ZYlBG}6MlKd-Q<E{G%>VMWOx>lU`qk8JA?eCx*}YD_6Ot+@`d>`oJ;GMZ-e79m;D0I+!R$@ckDq$w!qIc2be8T~vlBWWrq7HC++9rI#>pBcP5QA`lUtMzeIp=b=S%}sDnK>el`^Nz+pf;ru*z~p9G#VAVs%vOLNmCAs)@LIgn>?+zq{fxN0vu?6_+`7Rjjot%k(RqCx6be<FQHG&1z2{LsRCz{F>Fors=1)E(FD}o0y>3Ed<B4pcq>+guL5AeVJ*+D?zb|wwg<%Rq?|t$MzS3VicHMYKn!mz?~YZGv}X*iR~;a#tmFqS8pj-dnGH@FJ#3^pi!pOp=ye`3r(@CG>g92TB<tj6e~?JYX-j|&6)+pK5ByXH{ZW|*>lzVVBO2QH@%4_cB!-Y*4AaX@O-DRK-F2KFnfH9;d{Jk_#Ren@4mXd-_}_)G=dSO!$N8?TuCi<3&VFGZuBZUUf8`{SY9Eun5`{|onvZCmP2i*wupn9+T!iDWW3v!B(!MZ^Zv1VlJ4JqpN;zy@XXMARQvH^p@qw^0!)bwCEirG%at+_tfmV(Z3c2kdaxsk1565zW=#GF(+7esM@nibo~GcIBkhJ}?i_TaLm=Dd1j^*CloR-jD@ae`7>%a=3x_A%^d1eF_KY#BZZ~JiQEX-W=@Y6X#May<Mk1U^P36fy&PLfj)GqZILqIoQQT}GJGah`C2V46-?y?pCJG<v)SpUo`)~q-Cc`o-vvU*nqNTeIVma5iW?upTK9I!36unJ>Hy4V~W_033arqr?NuW_mJ>vbwIlL>jL_=h)^MFA(!3(*n8EY19AFQ}vGJCvlgDm%0*-M?tw@!Y1D_zHk)Ek2DB@yH>$<wmKYAybC{j2zIB&4FK&QjWj`LDQ}0fZCuU5Oom@{8qNk1qx!c$_}=hH?TlG^^a+rL-}Y-N)5VX{nSuK@^NkF@bwP5Uv2(9H~wAC%h{P*_NPotUcj+Yf5AUcP98LO5c-1D(dAE~2TXr<C_}~5A<)!1wB9(^j`h~D{OLgwY+zZn)y!-_87H33fx?qsS_wVlwV-K9+-(-&w;Tr+gbcWdYTN0Vt&}Y7fV*Q!(}S|Dfw6RXSw8U7A&p;I;ra?EG0bEagRhw$!)P|+X24NiFz_PKt&^28=H7Wk`x6%jX{H#bYPiO94szw(R4LLy#MBpTUe5>hMJplfZ+!bJEHFWDZxmS!Fp_WOXp0KVl${aM>@Hf8(8nh{p=;_qSB?g-@myyq*QIl{&LV)3c!JKb&E%t2-h8bBTeU@$bXH4DaOEmxyIX1ry5q9gu<by43e~&`6MOJZwEH=IyVa6BElMqN;JSy!kgMsk+R}X+`WOH8yic9peZY?Q^@+;Ay;7l-ChftO(aK=@x~QP^t;4ve><)r=2kwmXXf=c`Wj$0CTn*R*>jv-^<UAM_<%B%>iO7+PX;DXcP$F+QZ2ba>-%_lHys{hwuQP3EloKk<&(%ufx)`{s0ruAev*oBXI4_C^a~V*Deoh7{tKY2zma*Bd%YZB@l<VBFP(6ps?E77|$ag@J4WxNt3{C@3qi-HB%dztwk6rkmzLsTi2LRsfWl>Cz*E`RYE4{l~6I(Kpnrg#*u_hu!W;@<s8cj4pq7|(s0kf5_>s8ST-7xujw|A?~D~v|4*m_a4dJQ^*A=23N5q=&7AF`L!nTL=$M)X&;Dp)aEt?FcWa!<Aq&h6CMy6o3l$PWu4<a7KsRjhv5YS?{<-$Qi<A<}0sp7j!#eU?9Vh`*0xu#C{MO+1HuRM5fd^%-|kbVBhQ5N(|l6IFl%YuExx^yb-w$ig8xMtG&FKnWAWSwKZ9P+7r?+tyQK<pJ)k9)(JjkjvG5axw}l;cm!hK`pGbFiBd4=f+h{vaO&ZkBkAm11gr=B6x`=@oE84NxS^S$7D)C2@Wu1K6SvS>`0B)NB9RP;Y`4_%EUTRc9)?dOY+1+SHFRS^WS}&3=r4@_p_mi@=;E8Z*=Ty(H}%Z=;q$44PNTpS#p%>%%{rNtmB*618gZOSm}k9^2h<kvK}iBn%GaLglOqEuugX5>((l0C79H<mDWkAE3YXcEh!>Od0b6-%);69hNuuXayoa-<SJE_dI*=9tfsiLbQuw)eAhMcGJ7^o$rKDP8VIU3bHY6(L4HbtsP@=Zbx}WC*`X)<&1Ks^^=fJ9d2oeb^lEnt@sp0L@*wVNRlAh+mIgwonn)xwTOK5YusnFQ<4n@h{z_W9<TEXM5|lS(>tc~}NAu)0<tQqAl$>c+FO!hqgd(Mo6F?oLUCol2u6jaulg_e`ri`T7R`p^#Q__cR<}2rMEZ|*LRd&WRwB0HSQ!N$@%;)rpLK;_`s}9~wAfZVJYs0N73rJDlnAq>L^Q^{besS71mW2s0IaeA2c+-pu3q-^k^I9Jpa+d~3I=ClPTNle!y=l#xI$+RB=XDNUxsR3oXnDxuQ(P6xo-B#Q*yu#3fRmG?*W696Zfob<33}_M1J(;TGs3Dp(yUL-7w2y<k@!zPq_Myo;C2(SuO<)uo82t-0@p37?-%&GC_jOz<%1(+c({S~txQuoG93|1vyDKt<?;(<HNUNG9%s^|@(_?!sql4<0({CzrewgHJ>%pdV?awOMv89kW-nm+5BO#iCIcB5Yhwyh?6K{@{F}kD6)F2RmjGjFeq<fcKky!_IVSDHt)Vo?X;WA6_JU4vp2>WDv9eRic9Oc+aPzhCGp*?{FBK_+oYi3wz}wo&K8}m~KotC>2^ek7V(f0CU^XQWvn*iE`{uQtQg-HpjzJM81<TO*C0Ir4mo12{u29ncCo^DeDd1!&;8%t$)$v}EE)sjR@1Qb_p~`{xkaGn#fN34?+$<M3>CgJQth;(9I_9L<GS0dQ<|cNvB`o#>=c>Isj`>mz;O&3>0<H8@oWu<q<IoYT=vHF5Zn1*<<xc6Fssmhi2oh5nFGo{doxYJ*0g0Q$&f5;*ChlH6fqKr<l`%KkBo|>h6})PDm`>YWZ4z$QQk?gRkFZI^zy3A4&s=R18tuE9{<n4F#y5J<gz7;v!30hh9yDg`aodI_)Au{olziSf<UzwlX4*f3GbfrrvhL+B;!RHnnI0MraE-=BVj3gUMxs){T{D`tn$bvANYM^_Jtciz`?F^5DDiFfwZmk;LHRj=CRKvsxK8UmrhK~mX!5K4Xe^@p$kGpg>NRR&$h!_@hR3JpfKxgH!qGCk#L~9YrD?ufUZ1J9)zc|}AdGU2dvlbg5m>I9b#8{<|G2lvwA@%gy&r7B9i6TIWy~nSPExBvzJT$fV)6s;&slt{2Qp2|iDme<Lf(}=*O>gz*0>5)2T3l5kFKs<541)<yS>-ig*TdnnPXHxXmO^y!MS-RPIY8EZNuF1|7Y(_eq`JB^q|%6CU!I#8QI+C-73F&RrRWsT*5{|M`FwX0kS}b!nTZL;lh@SMh0U%v0W}B(U_(v*TAw=!Z1OIfk#NdlnICd60&UE0LEBI@CSH+Sl{>k*4{fJBlF}r_uPAK+2_@%ycv-ZJ9ezS_FBK@YxJ^Uj$CH782`UTIVimjx>4SC!w1O&y%-zD<(_|gZ0Kx3HxjJTFTEZAGDvK9yAxq`2^EW#-hw!P=K-ULod(5T#f(lxx{I(8i1Z}W^A<L$>NkJWXcQButz6vp_1CTF<W?f^^k*LoJ>H~s{rQ&X!|GpK2w3Z&b)&Evp<~q&Q*&Mjz)Z$!ac7Met_7<jcMY_WmKA|SXm_<SVhh1+msYeu%$oJ}BA12-Tm9_S7Jv2^93)W3?^|10;;(+I&Kr5LwuzV4HkjA5`9|7P*pY$3xxo#sGoM&+#JPgqnbR=S7}K3gb7TM2PB;CFPB-D2(@kkkH#>9T2+tdFoY~y;C!4=}U3ml0BCq&BVpH{sy;aV><Y%<(pWqbBKs0H%RGLbJAu{M-x4Z#$q)CG@;0iS>O({AEk`81?NwJ}oi%hWaT-RPruUXU{!xpq6f`rU#2xC%b&Dqi}rnP9}IbSrs1b?ruzhmXJMi8D9uo#z0hNZnkt3&&|CyaKXhSJA#fT|)!!H3)MI-}HU9oX_+;D!F-w>8FQW!<;IggS~-2;)vKq4i>sq6}z}MA1xVnT*s_h;hdmho)D|BdR7g0ds_>BX`&_#SYraHpV?YI)Y>!y4ZD)z1a!ILw$&#X-rkc;ejxjI`2ldO~`iXW5{%l0?NOJErZk$aP{gNan8l<cg<y8>CeV>nS2`J{3My1|M_<w#R8ebE2Fp-2l9Lr$JG#y4QW@-hAnc~B4x?Po?|v}z~};6=Q@lG;DRO57YgOpCr8+s=FaDxkT!LATrP$zr(bKx_dwvJUD)$^!r)A_zYghPQ{OU6I=~yNpM{(M#Sb<r2){Tmo7Jom@<j9LY<;VVl&`r?8Dy$U6%ANrc;oD9kOnRwohAxUh&5}OyyZ{8!1f-HXv#G02q{Sjti$dGAeL>$HqtRpfmoX-vL%?}1&kDL5vKH8_;%NY=%${>#%%`UK${L$4Tb~QUWgR;!mqmVkAHw$a^AdeIGHx*8iWGuwUG;}ogv<?w8;i|*BOS`b_4dLB)Lv^u|S=EAhBxZNq+?1o&*O=5?2!HodQeXh3bgzl+Kx0To~Xr6?5~BuM?=>G{9yG16@g?H>rm@z(<dn8jeT{v+Ai-BE3oHK3S-PF^#;ny_wQ2n4=~x-a%h1J-Yw2j`-$h5lt4gU+;_z2#pgqVW&p!JPxURMr|<=<&d~xSU3DUYHd)mgQP-vNeKJQspv=Hb7Fu#t<iua%7HgRf4uHf1`rw4-rex7WY~Rd7A%1RH6<f#NRmdz{YF_AQUc;2-2}Ac&?lK1UXX0bPJHQ&ld@Uzv+t9X$IP;aF*Gv`B^+!W1d<qlN{K56%&<Db^1ByFj0HTah^_xcdocqsn$0R=Y0fF_$nyc!AL(La8dA)LO3(GiEK~zXYLM~cvi=D>7hF#b6aRDm*U0-~;WMHzQCGk)W~qrF_?oDcgs`<ol>AvpzoU;eM4A{<Ok6@Ho+JcoJ50+yBd&qPUy4&s6C3fGGWDMQ@%f(RiKx0%vs(x}9emy-HvE$!FQ1YAiU<D>)vUp!$LS(M@A=<ZSB$*Cv59dtpZIzb6IA@TH-+#fx{+l%<a+$dZz$y1cd|hAZ2!6eygdTn*$NVZjEC_O?4k!DcTbuGO&GR7M?@eCCVIdkB!W{G-PD5-XBECnkcg`Xcx6+khe6IO(fF$@4@HK~feR61z(NW1#KvTgIp^eI#Pf`jwfj7oNKj8`mT!#_*}c@bFVma3UVlp=h{fL+1}dmgx}|<DS&C87Umcz)vJ1~ZvY;}W`W)x9VX9l|80b~XZg^z>HHmZ+e}U1su@2a6{Ye!|MYr@#;XbEdfb6U5O}-M(X7Nlt*xg0B^9FPIhZOcy8mlYSn`kwZyAL(YG|-ky!f_3%+$;sJx=Xx?{H77Xpji`=-&k+fH|8qt`z7k+$9)sA=l^2qkfhQ+gaU7Qr5!y*=3hi-V7i^z(O<9%X9ZrSu9j@3wFqxx3_?QHQls7!I+(PE1(|M1Q8@!^oJsK-<bnIjDjf<f9qN74?|PCB`M0M-4VooQOt5z`yu`4Zb)bpx)*WWFEQq3psL9+y7GhE0McI7&BCjhW5@O|CDbPnvetzAg01nvh2U@q*FXBg^S`>w=e+x|jIHY73TI(f^*y5!r8;)+9#CBuNcIyZdN{x4gg%(P+hWu3^5hf}zu$<MDUpeKc782ACRey_XsQ%PccL$VtXXY+Jh%}8o;2`8zI4N>a@(mwxpgKa~e+qpj>cvc>v|{F$5x0IanYYie8Aa*tV8>%kc*nH{bszYISZ{2gG(nQ@T&c4l$UnzQc=RGo4Qdf7SvIWdG-WbKtAYIwY?z3Zk%W(+U(lAwN-qaXKT7N1Z!P$)_(8#)hilHJ4fDRzQv6!fWXgMsn*0RcnF9$gOJ#*h@z0TxuK?advj|ipr;(DKgwyg2PccaWlL#VNYQ2bDt|0j;$bEqm^X+A3C!0_VFiG7)O%BgclhN<VVkbAaXYV#C+;-|So>7y}T01%18qhO*SFoN8|NUS8S~K)(8(Ojg_&TQY0L$X16+p5ws1J03Lly|RrylWH`ES<eT=v1byBT?2>tME$pG{Krr90DS$l=O1r<wI+k9!5w-L;Zm^KMigxvu)z45cp7*b0B)qVOm6U_fqH><iZZ#tn|9aek@xM`4gB1dNY_bop<dwedNkKfeeXZRq54z}f0XmCn~qGUBos_)w%KV(FGzCB=AH97Ykwl)qKRlHrfsEl6=U`%2`egHni<bB_9ti4<DpDu%s~BT#lm$)kul*Wx7haJVqoVKk)pdp?NdH6?(lbHEZ$OnQg7N3;sRc=e<PIgC<owPh<XmZRCam9B-67Eoh;du*=J$%&hfX&b}p;HCu-irl1i$FKjyPhqZNZ{(ce^WKPyCA2pN)2~~fgUp3wG$bP<Tvk(!GC@!>A?4cC;AA0uzkZuvd6m7-4faa)2QkHtaoW0W!^||JFp&3X;bw-z1u>^QZK*Y!%$Nki{zHJw>O}lRg16dWufcnx1b;aV1GqB|r-7_c8dazpbx=GZo(FHiyK*3*o#@h<%ud8K)G!@Ot<rWLpRYGT;UOr&q`zRsS_Xmpu1;Rq<(1`>pqAI+nD~9-C#J-v5!;afOhA5%REiGvXdR({QCv}e1?jt|j!vRcq>I=Uo_vp8K6~!nfuH_&zZ3H6R3X{TyUaHrP!P`r3Z|Lf0<Yeegw<abD7c}pdT7Gx*98jL!V_dErDrA8^`UQ3CvbB>q=4_$0tI7JC&=M0sRBWHuhF1kuaqWWiACdYP^|p1aF+j@&D;SO{hJDl1_nf{+V>I`#aQAqVNo5V?mR3?#`m}q7GY{%3ybK&6T8dEC>zeh3IJ(c0C1{dUMT|@bgv`bJ<^fKw-AY_$CV>bnBAV^Dnts;g-9!g)=B2ip#@6$B2Y4nO=;@pa5wB}<<YeeDKJFp&O;;y3}rGj#&4nasQ=$Tc<jDfVZW`|J=xChmj=GgQ!LXRyD6<i)yU08ur4Ga1magYPfZ%WlNoGSu?iW@r>6PB;EQd8{DieC?w8{DX9S<Sa|yffT+xc5pEnjOaEft7Dbf)NJNaqu<agJj`Ryv2-_%XEDHI)kD+s}+-+UivYo=`a4f<oLt&*gl7`P-+yIpW~H11f(-rzE_AlaEr1ubDv(}}1SN#O&P^TPNPN~@tY6?d%J5Ee~LdJwOsKhS{3%{5iTdMrs%%8!ji7OK!IkQ)L%8v7<+#*Mg3CR4gq@q<khRDq4vk9j?*v4hy%@acu>z)|ivfJlaI^px<x(rvt_mWPa@N-r>NVi(%Zjy)I26Wp<6+JxFh-LDU#*?Lwo@EV5Ho=Gl{Ye1239sz_YO^E=Ni9}V<9j7yLi9hqA7vg(h8Ly$by4E}{h)v2Ro~y-f2W4B{3=gBpdoQZdk&R0uwn#GCjU78ZGg>h-G@~umkk%M36n!ur=K!uqjMzlnF_?-`FfOlkZKS2)W|B>gF&xqgYq*sU27&xg{_t*7qo=8DQaz5mMs?Mc{&aE%UT>Iqu;A|8t-k4J{*?(dtrtt*3_7P&va0GV$KwAX{t8a$9@oa)VbPOn8Fpy?xb?|_tRQx*JOzSr5`pdtfev`y#o49{&&zhrs13wsGmX;M5+IA1EMt)cGm<L2(I!3Nh4He3%Uo8Dymp5$sF5%xnyS3t>g9d(wgxKG?Fk_X$uwo{pS)fyNFjfdJ-FO(@CG0C_HlZ>bfifPVWrg5>{!jaRq?>Soh9N617fzKX`Ddz7F7hA4S-n@@9mTtW7GaRGfJ9=u0AfB$wr9tIT$Abfm#%Xc6E9xs2GvNtyy-#%5Cw`t&Sg-L0gXC-Et0r0P6P72QwQEq8fHCwiWFzv`<VkDMspBc7Ymou+hA@ag!UQHfZ~3C+4VFi_0lBN0FHi;?_(YMz=WBq-*!LzNvhmKrv^Dw#2l*ni9yp?(3%nH9*f#Qv#CiCZf7#Z=htg`8g#x%Lis@5UyuyX^_b^3RGJ1fmz~lj<b{x46m=3S~9R`pFuHg)&+^?tx`|^MiWj31HItbl4+ak`uJ#M6#FI*92c1@j84l3Hs|>Oz_d=`q|j8Z9~5fMwfv8i41B#p{tId~uW2=XZ53QRKWPuWB7qy%61WsWObYtnMgNvU|A?n7Iekh0c9s%(r-}JQ|JIC)Tm7Dy=8b!srpQYF)|yNdzrF2V(_vbZp1&I%rvKxc>M(VjdP8$FUP^(Hs-Vryc!pEZApLCJ%<w=c7aBK=C2Y}5Ek!k!IZ{V8Xbek{0xun<M98qw3{7qI49n_CbOkjG3`@avb52gXMe;`0QuxKMT21K;V1C|ef`s&|0Op#c6vu$zJ`x*IV3WPl!ugpzAI+_$r&K?5@>gxA#2XaqVbLJx7Ot{(#NO^RHI*lvxA<L1RR7qkx(D@S?=Z`{+t|a{Aa->^?WmgvPf-{5PLecr>`s765HC$Frfq%wA&6r(G<iK~^p$OxHhAOlChTQ0OmszW9A6e-Zo;99cOGUL-BDJlapS}31TFH=JT~ha?<K^sV{DEqO2=a^nmghxrblEl+ig7{rhFgFyiYxLyzGvO8Z|t*6DmzSp?J6p3?h8}eMdE|97G4F?F1p*(kG<kJ3e<HQtxcAfBV~c?9AF)T>Ex5`&(2=B>E~%yao+rZBl49*HY&oS&O3B{eqLSCdjF#<K(-+o?dB`xzOqd{J51`iP<~{-;}Eup7WAXkT$BOKEHk?o59;m5<I<^sN!sUVZqcK%Hu8h46)U(v_z9%qGyKSaE`M8t%-^jXEgO-$|y@l5uIQ7*k0|qpi+u>>G?V@eNDY~{^D#E+eedo6LUv9G?l-M;lF-k+vWt&U36SlY`wLPOH(>wrEiunD6^ainO_|pmo_WelGNn8!V}q&6)D}={x_F#BJp?XZ?w)yn_%lht<_4-^_UaGgKus5`+J6Z>}Zzs)>2*FnjaB44(!Aha+Tr@Yb~)!Q32d-1dKDaLtU{hNFQsTTlN~!s3TjCv81zJ9gxYOtj6v7MpRhZv0TfyZ<}~RaSAPAVmio3bqYh0VL3}a_4p~+R?D=iZ=i4Nj1;s_WbvTOiT<3*8rbQ!G-Esjw`CDv!0Vah2WK5P-bsbU#7SziWT$T$_FNagU*>+`_F&sIt;3>}CuO<d2^hYer?wRwXk_jD*6bQ&)81No1SzTFQNQM>kaLMi<~iu~O$90}oTRZO)F9*#LYgJuz}I)mqxrDMGDBlb*p)L`lF^LG_uvLT>2j+sJs|Uwbw@X|+@tJNuu9$JZ*ji=5jPtmfA4i%mghY1t`ei_#aYwKGU0gF=utVxtR{QQ)+G@g`^NuCsztH@DmfE1?V`ZCOmFM88c49-xLs$4Il~s+{xbNyA$}2Lf&gw!G?oJb3<TXFZ*adPwp%v!EjL^Nk8;uT2M?L`dOD}ZbzittokNWFdp_7$UeKvVhVn=S*Od?78y5(0js4c7Dew#^1il|QY<=L6_(|>e#N-srJ3o!)aSvhuc|Idbp}yYLxuXlAN1vPm;(SdFr}~CksVCNhIaQaxnyV1}LDj)2oVa53M>10ibqN2ZR}M^B6Q=I3)rmIEr01N#*u6ktT+OrY345`$NfssYw3=i&iJ?MM$)rh!BcUd>Duja?(BX6fSMq^%9WYQws-36M4Q?1A%~%9P-`2@R``@lc%;2P?qf_mi9ck!p*H451cQW?k@fW|@n{+(8LsNd9z_`9cGe>SZzc-;|d2w$7O~X1Kc7{X20HiSvb%1Z!f2jk%fdPvQo)9hEBT4OW1LE$(0TV`r{hc-{Kjr=n8<a16xOLN4&*v&_k1j_d;PS<!^6`-x70%yxq#JI$Y%^$^3^bA5XX?5!+!}B34X0q5DY!rCi|blIqzg8+BV-~D&FmbD{}xHKpe@N6Yz4pUK!Iw&E~2_XYV_Nheuxg2dA;}Crzj)qVJkQnz_BxCwyjfKwnfJBL@rIfE)_!tan!SJw4r*R5ge%|5ssc04$>?=gy;B)bR`}B(O2bzbx?l>`PcA3;hG0u1Hp3VrLbpGv<D2-=L{$hkN7sgE8YX_c@nqg0cU~K@_|1c7PvZ4oA%ejZ(nXPOSOlOkCZidbS9zkGfr0Zm~{_aLasn4<JArj1mr<_A5)s9BvjleBli(e5@D&S?0Bn_v@AzYglG|^FdsDSkpaQS?*<Q9?bk(RBd6Y5%)v%)yrpPLREUpy32n2V1eya8Z*1YB8;I+zw_qA!nKN);6P6OsBN~uW*>DrH4g{&S&szQC8|7@rrcvbe;*;}X4U0(WMC9Z4p}~%(1dh3-w7L+CdiyL>6ARXZ@zcaYbhvf`&N9{2_p;+R*|Vm8COKpURAe!Lku|lh75$T<MSsdhSw?VtMh2>Jrg$08O`8Yw!Rw^|$Fa5~{`&zq8D&CyxW8MuwW3Q{7nXGY;J>1F@8&V|54hit^;AxN0tzDT59B<u;rXDD?*W|FM;8wdPMTx&eyaP=>A^zT=>b1K2b?$U`8z`HdmLtmmjPP0t6}wnkw;JWUWjceXgrE_@u2uNPWNu)#n4*v<0o;){5=cC<G=hqi>Qb4>)9e&qt^{FNqedf7fxId;f?q>B~>)BpMv!rjPe~`UP^W0W&za$Sc%Jm$_#T_NsDByrtGk&-!U;2m^PsvP<i{lhUayU-hqwRsY`i-B}+?bkxuE+*WK+{-+Q|>n<K@H>IMgytqhpw4Zb*24^l1yOC+1Wvy3Q2^U(-;^O|uzcvZ7e2ORtxb_Y}ww4WO38!zM+_)rONsr$kkXxX#sR-Zxk<#$LOLruf^597*TkYBwCM0yr2{gy*sWCd@Ssg65-ZZ=BX)Mi*A_;DclFm2Dy(6gf2H#yB&CVFCRuU@@v#8rAD%r0#s?J~~&i@9PW6(qiR$4u#sn&^dB7!_nWB5Lj8IMc(Z4`*K0Q^1%+-j;9lGLG|}Zxr$J&EijQ8|}!gCeXh(b3l3y(VdJLVUVjl(3Yq-zU{>PQlneVDf|`h#miV4?0T1E)61pJ&dR>5&PU^Eqbf$ZXZ87*7bo-h3glB^8*gpcDSUn*;04g<x|aUk_nEWzu9S9;9J=?Lv&zR`p0)+QptQ=Ft7(e?c<sy$Po{01Wy3Qw*SDg?+oo-LX4=N*rY$p$WzO>ab>(pf)R{ZsyY$IQZm*xPffKf7W4TQqo2_bR5ETkG<i%`d=_Vt}^+Kd_s`8t*!pIxopJEved62Y?ySL3*3e(Qhwr+Db*;eh2WtP`qOADl2&StJ;T~nL6eVw^qs)nBKy+rk1J9+ER2hLVbjW?s_%QN%0I4bv<$x)&7#n~)oxQ5rW`M4v2DV@z?jN18JZjk$q`Ft?F?q_H8){ovM_4M4NzF3PHVO}i9C<4Oefn0pf>(ZvG=5^5vo}%%ciQYY(*Zq@uy_x5=M~kHIn@n9>Eeh4GU!LH5(;s9mf<zIhlMUm-y{*m|sLe9j2@7TWrslBo8vQ0%KEx)a!T7tN8yYM18>>p=A+BWosL5h+&#>gmWN&Q%zBi11wNlqH+`lX4A9G+6w1Y1qtif^gS`V=Q){26^y3YB^!<9-yFXnYJ9#O}MlfyzK${VL5X2Ggti0aPMZtH|i$7n*G7lN_o#$AHf$dnO<r4cN{jt%Z)>>Y2^AZpDJ1E1RSU<Y+D>)^)$#E9&dkw85xfTBHNOhz#}=#4Cn;r?(Vd=U_?Qj-zeI?oEN#STOxoEz#vz<9vn8<9859;tUEQzEwR$n?)ZR1zM|`jMzXIIA95kxuJr)G>jO#TO@oJ98@4k>T?=4k8@hK=m!*pL{Kp5sI+qP{uizEva-aEoqe683b=jpX6XnbCc@i>fj}NQfDXY`0A7E-%i+o!9*sLNoAs+(F?>(jO{EP>$w=IqrrNuIej&BI1)f1+b20yw$w1Ji}qYQr6kSo0%W+*0t<`InKZQh-k^P!QyQeuize9mat*E0dIU=+EzA!Ep*Ip<kkNcQw>6S*b<Cyj7p`bW`&rsL@Z4gvJ!tRpOYhFNQ?ipZh%*y(zdDVxk5m6}`Kt+Zn>@AJE*dn`ruI!YXhu2ul?-(&I;GfzzI9?YRP%SVZ?rg1%uQxppn20@jh^ux<AQkfi+uN@Xr}&Wh_h*5SVL9QO2&NA&9=|w2}FtJYrtD;^jzXQ_!Z#OU8tjnR@#u<`ds9Y4$rK7zV559P9~nKd0zl8eFLoe`1o(R-$3gu|D2mX69vu36K?CHR^crQx$zO{{$rD}L~}B-0FazS@b*c*L{1V9C>7lKkwPb@i9l^<WR9Mz5_WxDjc^kwjCG{ol!v+!oeXgc@B8qO$hni6&H-J-eKQk6aq$>F=eq{pB88H4b*ud<$;jLgk0F^ZikVl#Alr@3kTt;^4)A&u-7;SM$aZBuc)@s+^G12$%jo-!!`9DYMH7`WePT?MM~*lMjR_&r!2vN9G}Lf@%+GdrpTA2uSzJCU(p_iq&jgibR=8;4JR4UMIuO^{5ti3EL0TpC>xi<xtbezN@*NWVbx`T;4hdF!BP?ul8CqJ(#I>8@Cwny1LElO!{dHmHTe5z$%m_v?V#Yl&(tJfKMMpBQm7r8sukP5w%uRdc9AhfMw@6K6&@`>)+xU$)0Qx%Q6w@iKqRu(R>WO}wE5Of2oo8hM8SC;U*b^to%yUE0=Q9k(3aCruy^zu8hA?oVb^W)9Gn@Xq&Kcm17c4bzB>i&n{HKTS_wdtre$x*>jqs-t{xrg$9=_(`r=hs=FnpMY;XU47-sP|58#(Q-`|w+eB0f#jZ*gqPhx@GZX>8x|?dipb@ATfkpT{<wJq-S9Jq#b{VR`k#&<Gjx!}VF|;rv(s4iC?M_pkb$s4Mp_Kk4B8?2}jj`uxvu{ioGg<LuN+exIHn<vG_L&c9^)bfFO1FHdykgFhpwsBcTJv{s~zs!OxZFOZ!n;dxUTZ1rkM-@$4o_%Zl?vZ{Ly!lKFhN>WS|Wj7h0*x02pnCTV%&3?dy^w~cXyZ7sNT|N^`5?KFcllJusUOvM5VY3rf!TIuy>u1bm`TPi0(V5>B+q>E~QqgFpVO>8s2W>eA8^-21*a;!%=i&9sYnC@I&s_UD=+r(pu<casnU}9cc=??5LDo&UJjwHC&d&M#P{wl8P=~Xj^JO`)dF1_DulV`}m!}<DUjy|yQ%m%QztBG&FbSVZ=AHV;^Dp9e%~o9c{p@GpUnyHMKjcsIW3Yp){<=J$p1#X|nz++5e|_m)y6>L+NnQ#muBdoVz6)Nqx&EhR5W=%(_13?>$7wGw2v=Va&Yn3x)fc|STmLlwqJLradomi|{0ue7*K;PeaZdI!aGh80HEH$L0nO-*zh4gc3uk-%IubwOZQS1P>%Z%t=F_-1+xaAyu?nUpfBE&>Bzf*h=g)qhN9@e)_lh_C`NOmF`Tz5JU0|G1cMS{Byu$0bNbAVfNW7A)d3Ce1UG}6lCOLhk^uu=HK;IHSFR^xzFf6@U{8={J*561JKk>$>i?#}JRnceJdIxZ7Zzp5WgB6jLv{)XeZ)&;rld^Tv3-&7nfrSide)0PEwg8(%%ksw3bcrZ_yu3JGyf>YXz}cVd^~>_DFG5v#HhY4!pVCbFoxugM!PD1R1DQ^T#Z=VvJd#1!V_3-tue$5j_fDp_BnK)fJE)1z&VF0fRs$|eAre8U7ZO%yHJ_m{1-xF-WRob>n(S!S#`i=il5g7mW3MHb{4|3+ZN(34bU%QQH=Mi#_j^)L?$PANFGsRWrU&?i)eCrgXDl|fj`_y=<W4X1p}WIK+}Ce%CqpO^R?$~2Cs1+p`f$$%I49z8Pm>`LO&`dTeZ=ou_2HQvef3NFa_OyK?h6<9;&A(V7_@CqQ1Kfu`Qmg>qhNkTHS*ap<`@Ja=3}{+sGreh(D#2p>#`$$Zo0Lv4gu%(?TeH|k7}{wT|01ZW4V>#4&KtKRm)R4=<V~TgVEq8sciu114I=r_TKl+SE$@m1HzLzDMzw9e`sHXYnF``UVP-IVCwQ{zk(&sua>x<AW}KC_06zLX&O>Fa;?iru0*Hg$9>XB00Z!)8z^X9CS1`m`9p%KbDD_uug5<&7By|e#KSW%q$9}GFcN@#vAb;2m4_Y&sZWkv3;}oQEs2zCW-+luLY0#((S0^h8>XP%Ncl417WP!nNrSApAo>%MjA?Yu34N_I9)4PG?@eVQ^_*9f*h6QXEc3lL`<p0&Mrurr-W$akA5GjqZ}KoOTJ#|3dE3ximhj7UDo;Q6>^$Doc}$-*YNqo{Z)mx5puG4F)_V{4lpHh}8sKCP+Y2N^coQi@Ljj{Nno{~ypJ&S$9_a^gc!bOc05<r#0F(}tIbafS-O@CLDa+EF_rutrtWbf#lRMpeVGYX$W9znldm&Xjq`3Q@T1G=UcG6}gP$j_C{786dq=7V0k2(}2cU;-}(*RuGj%@HkZSgNYchkN9aZrb~ZunUYba*w!<OCG*-2AUs@p-&`R1OW>nf?-~TqoZePLlkSi$FV007*FSX<+>filq2)SRf=vKuG-YDTKs$Y}df{#E^m5JQ>4m29G?!+jB`No`NjG+f%#_S^?l}O`glqE3x+m1_@kGxMpUo^sj^_+c_89%o4Py=e!{caDM?9p#_3U7X1Pk!5M~R!22^SvOa>E10ZJRS3~ZbMrIw3V-HQzNk|avX4gcAVD`3#fk0{FhAy%F0yX|-F(7aLy!($=aqI(yAGk=yr{v5ZfXSL?Gj{4t5zB&=xvtXL1^XY<;+}-=nwpP~l#1n2Hu2!lRvn-OmB?B@j8xhHh`C<*h>+_POwg49;Y5ffV7^7`XjJA+!erRO3^Pc7iv-*lXr2W+WM{-eiD67+-Fb2s5=0JJ)c`li@4=&sR7H&*2r6QRMwHJ$+uUGNORP~sd<q4EM4uo0E>np{x~BS2JrQzlv?o)MsOf01jFY`7t<<;wxT-SAjLc{e80h6WTbr@+(gOos_uzVNFooCwvUVrkn4i6{Y&_7iu{6s@Ed)~b?P%F}YL<;%vuw=Gvhl0ne{^NpIK87~WA0o!fZhS4FYkYzu8ry3weh#%@<o+VWZC$GX4#mUZp&=e_$BrDe;x}l{z`p6{{z`H2DsJL!|bqKQUc0!lgy^kFE)(~DQAzy?Df@Vo5o}|jnupDS;~xFXRf$gHjP|puw-Dm)o+AZiM?j!)F|Zi6`RJoY3{DrG?G&6%&9Roo^M$>HKyj&xEI5cW{ruSxycd$kyMcbmLR!h=6Et>Xv||`6p?^NCp!rEH5Mu*bs^Q2x*mD|#H=yCY}S~h6^`9lPK{l0UtDo&#Q5C2(yY;2;B#Twm@h3G5hNVGJARG51r?t&9Qp7;MI-TD3o0OXcSe7D8dsc?_>$s^=Sh6$p~ZE+(_7*SYFe{WJ-r-M^sH%HM8VqEJMs9Q#u98&P(4<JzE`pN<|xS6O)+fp8hMJif#Uyw%GQA(y~;@rVrDm$1!{WEI;DoUwuAIe#M9o0r_|Fi;%WCB@l;BWfS;@6F$Wk?tj3W6Ml)9WmY}BHA3!cyZ~mWVME)5E;J4w1c&vL*Oq^LrU}~m|jE|YTeg{422A8fT$NfacKV6*QL|(APOw`wu+*DmyZ|c@~G<bL2>vt1q>~$5MSVtNkZFbNT2m5gyj|^FJq{ZLUr~9xOu$ThFjfjjBZD%mz{ooIf|C3QI4o>Yk%)w2jFGS6J`mim`^6SOhc<tj<3J(L6r7)c*$P9#?GTeIcs3F`tC9S^ySKWW&r=HpekFF?SIgmbN;TYGEn&5nv?j94s(nnU9>Ir=29|7ryQUt?SKl->KW09+@yR&K{B93wk3)8PKIs6YL6c2MTRmx<N;(tIprF5V_PlkvBCRS0UFpfTaZ)m=WoQ}|>9kAW%OV<GAh8nY&lMK+I^8qcSdgp-rRbTM~`N7tY+{pb?JdjqFt*<|Nv)&d>fd{V_^s5?RG#zj(o{up-y3cU~$1Q3$M#ojZ?Mnt(5|?`=&sqV?JF->ld>xEWa4q#~OY|{ZqY(sIy5s$jyMa;z{TSZHv;I1iR4&w53=e~?(&=)QZdOt-qr+{pW?Of!rwg$3G_QCg6dM-KwYV#<Aqw<zGXNPCvKQQ6E?ELcXFfuHCJI2*0XOz=HRF??3#q5^^&|jCl?qL<+vnA~SB%p#h8q)E^utG0nyt6vd#Dbq0~RJ-F9$44WvniDb~g;?yqYI>Lu9l<At>;d>)o&$UJO{WAIG-@EdAR97Jo=ELLcdyaP3x@^#-tyNQ*IrYtaho6K`eCAh|<@IN8>X5(sHI@l|&NZ-oP@tapsF%jJClap1ht%iy1AKg#<6F^H)GtoSgDR&xKY_kl$#gC*nmMwg1qti)W1F88bwZ$9R&5YwM^ze%y7pFx^gq?fFM@nikotclmnWrXg|plsqn<q!XO&*k1FbEtCZD{8dWD^e%#=gfCx>Qhc+%gGvuEPpjMPXe#>vCf={5u_4Ws2AT+iMK&UTK*W*i46ey%S<Zq*XZVspQ0<w#ic$xGP{JO1GNMXlsfI1H(`(Nh!|?p&IFg}X!WD9hiyE55zkMV)IDF&w=dXWHw=I4rymV!6Ul%qh)sQ}K~TrfZSA+xsyj8Ot>?h35TAZmpTEVIm4kBl)pt`zsy{!wCNX!5ZDQajKw@r#@b^+;?noZ|tc%q7aeG!%eMub&^{*PDqUJ3(Oe*MGrL@Sm$6HfNC@Q&tU8v91b)<gp!?4Kbpt~>&(0NunrBWMM>ZIS&reALFKAcIjdTw)rBvnTQay>cQV_hOim+Tk~pCC-zB$gOU9&{^C=E91@)65dn?cW3|wyr8aMOJL*y8|h)vGHMD%8e46?Yp*y74Z(66O0;@!Z==M%v8#2VQ!tm&OB{+ePq{`QSU-hUDu_9o1#rtsmKQk*1}mfg~Q};WDvpxu08`<0#>HYMMrehL-<ldUV|CN`Sq@<AM|7GAq#gVFoV7s$*n;aO?uY}um4ec*-njt+ovXzUN@Sa^<%5x@p)2T4?NGB7tCC6%>EloJ*<bziG#!bA?y2yfBboi|Jy&A`EGjN0Cn{4G5aO>kTdFqW=FL38}7ifMnE6{p|C|F3($TH^**gPNqz6oJIS0*Wxgd?m+Y{*qpiavcB0EwG$R4FddE;Y1d%&F984RGzt?SThfk@I`3Zd)j6r6P^GHqCFF0DT8YAT4#>=GuT3=INU*o&UP28923%_XMiCa)lIa$5^l*k9XsP33%b?+19Fzb4Kl=HrNV5?paua8_>ug5pNAIlkISWDC4X}f1qhxhp?r*9z+D>K)k90b^f<~nHl`bH6k4LO&x@H|WSdT~b9uyb+7qMX;o{7q*mw*_$42GcV5ygXQcDY#@yVp9l1BA`!sqbdz=+IOqZOidUpva+BC<5O+0%edzwTlGx8*Zskmb}<bx{Ro6xu-bf4A8Iq^f~?c|v3i$SWHZ(09~pcEqq}3K+}Q*a*5J|N62vaTCMXI)mmETg77QKb;&;oH)z^g-w=MK~?*QjaGBY8Bd7@y#i3gt;OC^COGCvCiVH`Q3989P3Iweo+M#|sL;hf98|H?_NB!&ltYm98z@xcq~zX!&7cd`7r8g}I3%Ma-%m!WuyFAWJ^tQ1pgi)APVq!INhoU97e=)z?Fd2n@!D=@+`xDWvui1Bw#Ut<_4%)+G)2nER301nW};TcIe77hlAbmW*kjEAyKvN4$|Y04%eg1m=QpOwl~3V#Z()Eh@)NK{?vQ|Tpf6bK(_@GHE)YxgsQqTr2h(39t0Pw9YVJQAjnFYsKD&DC23(Sj`uCG34Pk5w-#c1fA^)C)mCV=%GhIGbdG?^)nK-r16&s<}((Ox-sAR~I0rH$MGNU&C<xd#sU8bjR}$vFsNM0AaAo5v7IcY<uLzgtU$m%Rf^dzjs#4?Wq;ql`!#oMnx(piNT7B`zJU5tSwYiLzPNy4cLC`A{=&6Vr#Ki)EX)LOD&E<5uQ4acX__Ykbn*}e#AB#H4*q;g853}N!DE#<^tRR>lH({$|T)pD{(UwfubSiTKzgZ#QQaoW&-3HMd$hvu@2xDY_`DiB<moo2zmQm)>6m%T{c+FsAa~QA6IzON-Wek!_6JJ(S*m<DG9Y>UYa!k;ZW})B9R$nQ}-+cK{a<B9J`v~{wTW@-1gIBYw!GP(vF>e$l_^T(W$!<B^eu~pQT@1{9d|$fCf3_V{2UerOP`S&t?Dl6jW!dqdOf#5lH+1K!I=SxAj|p58G3`p_=rO_i|?yNozDea%=*z`!r7EFSs~ydqO0+zww4f52>fk*N>*=LV`P?o>)D8z4N1rtPu{`aifWv)Q_VsdX{N};ndN6?NerSiu-v-SveL2CK3h;bDw$w^-iC-?x<cX$YaOO-)`@3DS%a9i;KVgEfPy9kb1sW^bN#PzQt1c)v;8vSjy0Z?<TrJDIm3X>9&Rb{u}NHg)Xk|6;#a;)dhy;Ma@-d`w>)j9Z3V^f{9hVvwkJMcDRXB@?-4y0;HyeRw|)<%;@U9M2J7ojiNpFgWW5mAM@K9!5``_f#ja=RaZ?amAu#pe(vVDyfbW0@t1d&BHqvGMtXIk(R7Fhcc$#>FUqV;H|8>{ckh~Uyn_^RcP8a({KuOCpS~mTwET1KKlkGom_hl*jWzFn#Fs!VvPf4vM!6h3M*46YK3XjfKtNmQzUO{{LqDSAGuFuXf%;SR`A0<N_e93-dd!P@BNSGKPIW!JQ%z2RZ0a8B`bhgZm$p+#EG!pSkD>S_9_#NT>oXe#U&Nk03Vjl%2lfsgWGfVFR2olly7$p)wFryCqc3-f5G#DaUEK;#Q53N7``)4Ua)(kzB#AOW9ge{hY9lP1ozAN+^~-MS{lEpFr(s!Lb%Wo+`eUumPH**k3HK_w$hD&8%`ga4@o}QGaJpeEDAvmq%7&M7haM|O0=-}u&D8OmC>A*xgEYb=0gHA$$T-$*5lQS&ukNkeu(m8e0=n*C+23&B^8q#6=@&o1@G#uHK0<VYg$GuTx+um89;b*5`|img(Unlqd)eW3ogP?Xht&(~QYSN50O~noB<cXxKWZ>wyP2U--vt{Cbgf2LI-rtqaoTu@?+2TmgCB_&91mu*gTMaXk2NI2wILa9Y~JA3sP|->G)y_`y&uL7c0uWx=@K`gA5qxr>L8&p@9QM1(}jMwb=cfk*z~EP=BW;k;&;!AJ2(pRX@cb!r%U;P`*-S|*b8YoFs1f*XG{Rk*VXzMurr<liV{=L&U;E2k?1%U^cA9eQoRFYI)Qvj=I;l=4VXP`NF3=oQgwekVD$#F?19>+tiuCCIr1$8WTe8H&xSsT@DlRG*x}}b;|-(_m)M#NZ8X7S6o?NuWu~Hh9e(+T<YWdeu=7DAgHZz_Lkue=9CV8c)Dy|ks^o?u61<dVnAXG2GL2M$n540UVeO1NME+8?1iHSlP+~co@;F^wfzQPNCJ`he4bk>ilvAz|e%GtLX58>7qZx!ANRb|J-S^6mAHf3J0!|g{{kJ122m#HJnNdc^>nP*anx%H;CA+zI^2=tPLPME5SrrCRScr1N!SVBs;*4w^A{4rZdF7-=+9?cx;D&fF%3#!B;{+Z^38`1~-by_RyHR5LD__eYxWMk|x<l~DDDA3s^;3J`_@Zxhjg2->OshMhI*h<a+MSGn<y$?lmBFe$Gj?-@;!?N(JD_iT<_cVABwK`ZuO4LF$?2PgN-l~sSY6AJ#+x)>btW-h*V7^LgJAJRh}7EmH=za<;$ocMoHrrP9AjgKN7*9IM%B$bo#52u**}$Ib)?r~pq~Nj6l?kWjafE4X-7W^lHzO!_z?|&|HL~P07shF)YxIz5@tTo8wO^sc!&`6&M-5${W<%`lYD>40wV~Am7JR12Q*Jv)g89st`}Q5np=h5!t0n&TZKhhonwd|Q@G#bWfLUB!{f-$8f6uS>(CEy3ywuMEivmTg#pW6cc2~3#(|Bg&oBg>PcK=OnGos04SPJ?QQfmlJk?AaW0s)}8WbZ6L?geWJOiRa!`R<QqnIXf7X$wn+)N32tLdnuwI9HSLW!w$n}hIQ1GaLk!GWR)NuKV&ih}Ib6YET@IS}s@A14VqP*j_Ee7V2rMv5kT5O0Fjm(lkizQUuJZgooE?0zYuklBJ1$J49L!u3IGX59$}9d>dW7zVu2SmC?}?uGxBa0MwMTv)impg4zzpVf7N>x49fW%h)UI&PbA=ndSM5YN=85f3}@FC6^$`lt;J)^fa0gBsxVYu(*RIVnP_o}9~(-rm>+4_=LH__GBT{F7ugXsAbh`K_p`_00e1>-nuUk^=dYK7nI!$2v26HZ(J*7r_i#rs}9q0#YL%!P>X)s3A|clEXlnV-uTAbbCm=my)h9?>hhV-@(|j$%L&h8R@ulPEFNz^%}Eda!(J4wJVaIN`xE&r@9BK^@UHlb6hgf3@J?MditQiMg7*cB(Pgg06^?y$8s-#2T-=?8vMa`7+??28bC+Up5XxB(*H3y!9o#q9#JYkGP^@V+t{fD=GB>YWX@Sv7*>7D5oPVc$yAdYuM-^sbv1G?>-QidxxRg4CT5!f+sMR%L;ZGi_(aaA4YQ`9duk*bd*=rGbDfmmpI>mRMi<WcB+2X@0?Wh@ZqP=duKP`-_ip{TWH_B$3pnt`UwnsHi=gQE=;|6bF=$cmLd$tQs+@c4Nj*BzTI)T9Q#+_Seu}BpZ0gWHdY~8ddQ4_@_wM9BjD@Ja>p+B4&&Unt3P((roWp^PBk61b^UM_`>;R<Jq)d0bsRMjB%7d$)HJn7SiC%ocy42ibR>6)CpN18zuBdgl@W1&!Yw(FcnUggwJjp(|G08>BSgD*@Y;*NZGNQ+tM0s^~Zm@WZ!Ns2$>Jc$&Q}j`dV&YvfNLYP$gcC&xB!~v-#O?2;R>3`|aP{2)1BA~Xdis5n27n>)z<j~b6!lZqlek2P1ruel;M9U6^~r@VS%asiGBX7J6^<B9>4{m36OC-B3t^KVNa}297nJk_%7@57OLLy?&2=CuYoJ4|JHf3t`n^g{B;+P*<n^}P`eeB=nw62OZ$02C&~SQ-3fF^%QBDYd^=k#%^?ukr6KEfN^iKk9Pb^LV9A@z6u{Pro>w+oPPG|}h#oDM~67nR!`sP==ug4Sck4|Drz6!U_p8kfQe=`!bSX*dIXW@35!)-lGu*A(W4_DK)-n6Mj+*F##L7O_l1x90(Q}bXN_!f7oqgR9XLEd8M?l5ZVmbm*?3mSuNTF035N9o%&r!Yh`1qnCloH2sYXzI+_Vrb!ZJs+U2fd;}R&5;7OZm@8Bw+gp6SL*b{Hh%PQ`@db*VbyKEu%gYQh!)v_{n%migxQP}xyr#k_)GHl3s;=zPWyyz3U&i0(}#XncR8ordYT02V|~V(|3;x7d!Y_Mk8qf3BwUQ<?rse-M-k+Lu>lezyPg#xSzZL9@|y!jFyg%mBn}XYk(;D?Fo5s`bNZ~qziV8M-rMVizC)}=f0BB%nnBgoWTc&g)>8?^Y@;bNc;Y1V<Q+mg7Qd;?AnyS-6|vL@dlDZ%(o`alnBkRKpxlg!FFy3=4F0p~H~i3!H{6&}tx6<xBGokR41HeP0DeZGotpNE<%mAYotBjqR=Rr9l_hQ`Gy}&+BjbIOec<3c5dr$+uSU>t{Q?%DZmNRJETG6Fpu~~yVhR+Jn&Pp)wPdM~(sh)c#2xkyg8}2oy64C77~wf&%6BG?*55|%1_VgzNrDN4e4TD3Jk5i18y|0l+Ky80iHdUA0H*{AYxamfBH@zCxCGplAV*E!kg?a~rXD;bX^sF75ssp=qh5h*^T8gDcf3|k;R(M*W>Tt%^j2r9#5I<`v?i;^2RFn;bg98f&M51c$Ula%SdlJNC%(7xgq38RIp-{5ZhpWGJS1~A@1vUWVS7+nl7861^xvd!#kwGdAvcM|NO*pYw?6Ab&6lM@!bWIax??i`9Bd?tRFA!zpk_j$7$HY{BmS~Vk|aoi9G{<!RBGU#(609?9M><a6RTfjXEuGLMg@X=x|J;vluAq|#pV)gnmDIqxhN{1its>c$Gi|GnKswT>r4=mTuWwS+E(f>Odxkmn__B~Njr)k@n&OVkdlwoujHnNkh*7?FZ{3HYM4M4c)iXWiVK{D39Kcag$V^$z`_K&Ra%(95KdvjkiD=?C~@c>UWW-e$bUtbZyhO=r;&otCPuo_yHuDvj}#IeP#`ZBRZpNE6{1U-_~fQW+^IHK&mxlt7|lIwDbIx(M_^?xv4shu-$g|VhW9DaT^8nei-TFoyE?9Ga}JarwjCB$D<lJr)e7;Kw|c4ij~y)d|Le8FZ<J#7<^vaPVHz+#XgMf9OsTFTC5xDeDt(c;xIpt1CzRM56(r2-M;+h9-wmh5eO`vlrdt=9eHYz$VS3K32<=&kB=D+EJnSG^Ju^QYpSd`b7Y3R>u8!80k9x&6Z2WqDdYB!>&}oQ$YzkRQud+HwEc}Vsz?7+%u3KteUvcGm23i#<|3Ru|+$n-P^9h5}K~%lEXamTCr*LEIZLOhZTae8$Lfg^os#0)GH7%MlBc(r!37KG7^u56pLmSx8w{w;?yMJ=>9VHmBY$)Y1G1FF`i8lnvc%pPN+c~DU*R1lmGB)u);BxpCvTNpeXnL85Z(P3M>LbjFZ8V|2c>1T#AaOIFI7tu!tvBG|*yHbS(?i{!ZjExp<vDHYD{t9-SLF8~*;}0Q<1G`%6z`81-LDumJl->utWVxzn%t#0oZOV+;lTW*z97ZzEtcB833wjr+Wp{eJm7Bk*acEe$EL^laBz$%1Sw2)lbWE#62CkqV&NPu+QXFN_a{mK@MtLS{N?wnCLoTzzH3<V2D^r0U}TnLGA0As2t$XHjaCXOYT*PKpt<2FqMyWN$w?1ZH^P0vvU-hs`#8%o;b9??rRUxO(9eZAY;fJ&q+u0bayL=tZn!qh0k(N^Z%LUMu$Hrcxd%2!B>IsHeUgEeiBuB9!eoIT#QU($?~#t1!Sy6};iC^Y#D(K(yq@`e)ST~!#smNP=jR2NXiSYcpg3Kb7v*L(DHKW!oD@QIW>pUzMU0%;XS$`$7uqyQ7t^G^eaANjL=ETDgk`oQk4!ll;wmMZH3kA-*N1&uH(GVb%3L5jMHg10+g)47qAhoXXE%qq?mXh~($$(*e$&A;;Z*s0b_{?LbHBWD;%q*eA)NU>t_&LaxfADU&u)otNoPwC7Gub`5^P;9#nNW5pA>3R78-Mt)(R_&%5W+9D%;UOGdqjtyEA3jAbq7g+f26e3&Lw4U9Its#=&@C@u}MEys7ne=9w=zzQCQ;{$aMs!NhY{j-ht&FuNJgy0`VV<2_ebTgu|dFYnt6pnmteHDn%~t+o>ZhZ5v`AkIK7gL@}T=%AARgRP|KW{{N)Iv=fl$ups$HTR1R8;<_uv=(o9D6?%<OSA{_FO$oQe#o6O#ZGDFA8YW+#?FZTg>Y#T7GpLh?o~<0M<A3QTunX8jf>uh!Z@2hQq$Q?xGh4-*mP0YQz!-7^O2i07z`e9BuYAuMiEdAsvME0^qI>R_{6S9;|f0oK7;-vJN<(-{!tK5Dsv-w!7IC@RhVj=QKrjSeUK5Cpdcv?REJg#2erVE_fA5cX(G{*77wvQ_bpNkr(+S+Csn#Vs%L@FddYb0UFjIVcGv|YdQi@4B0Y0u3TYPFTH=`wPhvI?Qnh6SsVD0S`#*mh$zm4;nrVyts;2BCt6wV!hmysD0NWOJ)s%a3oAL_9ksP&Wp_CM<g>+d{hDaV-P*{KC8p459MQAK>Vb}R0)bE&Fg++UFl`L|J$X*3yN&F)n#K=-jT4iN6PqYZ50)S;LpVgG_xXYXslsgoZ55{4q*f2mKF{*1ojRGo9*L9Og;f+fM*l1EMpw_s!y@J`;T$s0KkV88+3u-hW#qGBkO8m92HT5Rm2CuJE2saeL))>e$;&k9{<6ndht=kzZ^pH(GQsvI(ozO!B^s#GT^R7RecNk`yaZcdvAfaPSH(pZpELKH|*2`eELN_u1M6%Dtq!aOrMO&52Gwb920!CDCI8=cLgIlBhJ|xzh)X0Fdi@U)BG^2;8@F?6+-*7{Sg(7Py*2rM}6)1F{*e33RwE7HR&HDK5vJZz7n_%81prICQ8cwaj@$GG}SVH{odV97Ph^(yVc!W5^=8@`wEX*PCdYBbFkm?oXc@T1lr`zy3@A)qtaW~dyK0mryN$9|5${ua`z!$R=Uo*CP@sZd)?jh1u09M8;CwNk$2=e(Y*psMJ-g2g6fa8}fd#?-Mu{~Mue}8Z~Pi*oh%;zr-sD0Nb_dEYweMYsTb%{o$+d(CoG;JC4<JLm`vJ{1L5eW57w2-pxf%1J<D9|jJwGxKd$}-99MBLgOeTj8>@VTlZFK&`UdE=>o0|rHl+f2sD4iXJ);}q(jyqO@|PqmU5w@Zhcm?tN8ywxt0#&L9eZ}tngF+w}lU{NkYu4s1kW?J7ntrIE}OT`}ne~6DkXE-~!uofBPv;_ZlCny8<bCo7&3kc@-qQC0;*L5Mdl`j6;nO@XdD^Eq%L#!DP;?|=Qg@{`009A6Vo+CpYYCF`uD7G?DD;BMPE>$VMD_K2<=P*fdvvs$fN>Z`a%0g($6J}yCi}9P!K>HcYTfnL}j-0f0Rfhx1ZQbk(<|S-NBG$PTnW)WD$l#imn)$f%@$N5vGJyVM0R724_tV2qBm8NEKaKDw_vcUU&!60%|G|0~K3PA1O9T7K_xY3W^LNbmdG>3L<z1|w{k11k`z3!f*3bUZ>sf!De_y}%s^jw+J;)S+_im}sG^`3Wl2~pfu7~>U?35O(jzD6h)e55sVZFqSXig}aMRWdbl@ck)nicP`xc3^_F#5H{u*(e<`^-PXqSo00v3{>Bc;?Ie#JKs{LtWSeuZ){zkU76be>(e=YbPHK<+M80bncHFR&LH}7^BGFyOr_rnF;cRkMr4A3&s)2muANoCeHSI|K#gG@tZy~ZbqXiy=>WhajJfqPRj_N`!$Cv{@pJbeB+Lb{cJqVhrukM^ojg9muA;yDl4g4dg1x`f_<|+(>!G3$}V>8*S!AydH3P)f@kr|cE(r!R9-Z04$nIv`|}rEb!~pxxA#Tc<@fo5;cb4+&zLn|`NY+!o?RyY>c93^oQ~(oaB19p_Dndl8(w)0`*?N`|KuP~othVD#*62F)vuWyn)h*DJ{yztE^mBhBApvsO9Vp@p-ca3|HKjd=@6|e?hTdk)S!9($yW1OBkcFR7H0CCB;;))j#CQ+f+by3e;gsb(iigA2cHJi|Ix*ll5>&<3E0ZJh$s7_Njak3>f&^RPO1F~VonrmET+^5)P`OV+`-53ChQ8DUuH2;e1GF^7(R5|^uhzq3XGe*?|XMFO(JoN?&baHrX9L$ZP_NYqaNpXFCD@Mh#jVr?`1BN(v+IHj3b4_r-#R;-UN&$MLi$fS5j9^z*iPFiH^yY+wc`sKw`XiM9t&(T>?59@SPlvB<=TNL)Tw~sq_5ao@Sl5@rEHI7~wbwWctX7PSayNkWR2Wpb0lpFrtH_UmW4^6M7O@0E9chzD)?2{NQdNfGxFe2=^rOy5=4AXCU>u_vJ^~wL7^o`u>iMQu|kj3?v(`4t`fBid={yB|T%@kfpydhE0KJHkB)~sT>$qi^K{_7La(|nY;#oL&DipGBS)9%c=2o`Uf^XIbelWi&TE%%zMNEV7Pi<XPg0Bq>loSNQE-AeaIc;ep2h~P7^R=SyM-WP4qXkCK$=-0c?4Ql9DAy#ddHB&=O9-hx<mKNg@n!b_Vdf1H9LGV{CaeHHS@XohCp0loX8jwZU+?4752hBL6-v$mGlS8G-iH{^<c^0%(F7o*UiB8+>)&n??ad#;C*-dkXCkOp_mNKj}s2062@DGhirCf8H-LGDW663{>!QXL7BXLSg-*d66d(XerJM;MgV#kC2;qLT`SKHsL&x5kAoXejX}{9qc+@w?si%0P>)6-uD=@M3aWBgo%O)bO%JMvflai+D;VDsl(R0W)oQld*?*8u4|3hf}19%TW^R2D_s1XHFoRw5%>$#mEQG*1fVWbt-yCsv5heDq>{r{W{G4zi5nLFhxgRX7_Q-6CLi-9m^RKJYYNTnvVmQOH6!OK$a+sgEJZ5>s|RH;HIQ|0jo_Yuw2W4^xZ9K|q$^(L0QJOh0&x9QnsC-7yo6ob6d<&kM$m!6wJS%5q3II#e$Bk8R}b0;{er?~I0$YRFK?XT*aB!-;iK~lB3ojMk&Jb{Ad=r*SB<-sbl@hwRuAX9K+uhUz-HNv58t~AuWHz;?k!+#j5S%f)O=WQd^^H73Ey8Ksj}~HgQ9`0Gh2{>o>hjSiUiF|`m!hcX@U@8rgb}|iTr8eGMin_Zr9^ob+TlUsp(~2=RzDHQkVANGlm=bf_t|cv4jm9TsKHA5uKlpLV{3onaGnYSPZX8T|`D$t-0gB^1%jd%gj;YUD8)6XCwC|`G~6XlzcIM+y+yOJHpMP>oVY7{UF;Dg0LV%631Id2VuvY6_~g%x?RnC=+MU{oid0`uc*GLKS`kzWKOEaAc&zq9kfWbaMWvM+}h&0O}Hs7h?+++dF`&L4dI5O$ExMjk150vVnpiz{_@8hRAEZXYB+lv%P`~lGNdQsBriPtK5pn_!qAyU*AlFNNJIUA8XVwH8xC^;s*~E&vUvm0sqY{sSo|{5Fqh5jNB~MlN#+socue2haL3JrMraz^n08?w%tJO2ons?fuje27ki(gt8%ydmtj9848%Su#3em@Bh6t%dc;Usdho1>FYFJ^6kaNM{g?+uLqeQ`Rq9bj18E0UZJ(^@h=ds;F4ZaSiZU1%EuzNgff_C7>?Sn!oj9=vV-BTf@&=!D$cs3&u!2aRy+z>WEGxkoKi=;2r@N927wY`*90&jNCLOhe<%eM1Wt@B~GvzxsSaD+@?n2}mr-?4Fh&$uW+*duZe-fb`>Tr5$3+hDPb5%xn^q~rNLegjX`aD%br*#DjnFpAAZ05+bl9L4zTGC5=$&Kf4|Gv;EVH9?JV;@~#*nJsZ&9l&7qH9+T1<onhjbc;Kh8hRnuoOJ{elj0q9cvu94P+`c4>TCmJ`sBvqG7}ik+EeT~Fyl|Ue-<vJi8dHdT}bCdk@j7%-gN2oV1|8`DBd;WCmIMKh<!lT0x!P@R|D!Ff22XFi~Ey>P4%X_g;s;#JeU+@ePw<AvwD!vAi`9Swz=0RE4{3TB9W3GG#%(0!tnLCgX#g3NeKv-hq$5q5!9GYbg&`B@I*A8Qj<EnKBLac#D_H`?V5sJ_-9^QQK+YS!$|Fbnn8qCKOpgNpxxt|4qA<OG(}{%TTklnU>4!^;f{d#2|`W&^Bbf*kK+8^k&a~Mapdqlz@Ih&6`#rtv^l73<@j~YjV9cQcLp@&Ns>_sGGbB2b9YXJ54r`QOwo^kcJ|VdxHm!V1Esj8ziIc1hei}4)DOtC03Ka3K@IdSPrR_)Mu&PEWqNIR-Cmaghq8fsyVWTbEg_H_yc-5?nCHZcLBczIlroDy$G{)Ny^wp}f`P}qo6Uz50Xvl;0(A&cl%bZB8AFON7nCA!QYsYyayPR+#(GgNuid7~Y08@V8D~KrdioK2zhZA<65oT+hH}TOrYSkF%!F0|SmwjX;*F@^QOHkkjL>FW>1ZN2F*2v=?!RDWWR;uVeSAwJ|4+a67X1NL=#;8Ga7CuD+y+4=%4I_9f+FT=gj1t{F^q;bj>Vs|(Az&y&3gOxh2`19ZFuDGV;!w~bvdA@7A50C{oo@Lzk1hwpW3#cOOWLjnrisd1Be>s9*R9sW;k&slGRanyGKaLFfM@pOH6<IRReGX8i{gGK;@6HP8lTOl3@y);r9W+HvIp3*Tn##|KxI^mm!7vI#%=QxiJxf)Mcl-Rec#4aY&ZChJ?onBu>GMoxE;O@O|T93-uZ^@AMiW)wgsVh##54V!ipnKn-S>U>GKS$IKcJ)ViTsQlF_iT20cCMs!@QI|u?GRH>&SkEE`iVW9C~eK8nj5wB#qpzm=&9JwxZHEPK?V8;^}65fK`zvnZck?=UQc_}66<m;y#=u*_dUpwB{N%L1;D-^Lw<$FFJQ2I4#6e@eE1YcK6$RQEtUq35z#>B>pV9ikElqP}5#Zc9tIxtgbi%A6g2l_6Mn1={ZSfSlL(*WxQL#mrgkZd|;ta{F35`yYQiC-yQ!`HJ|J!3g$avDGUBKD;nkkWyYIxt;2Q2|&QNrG2Nbjd@xN$oso#e_yF4peva%`pM%3&}nvrxKemULr3ongnWUMwV#M6eAO;vraor*)j4z`V%GggxQZYgAA1P$ozu*tYm%ga84aaRH}%rU7k#@i(kCGOtcAag`#NAKr=N#+FR{_)=@TAbkNVWv}>}$5_M78k++Y-!S{c{Htjm3Kl8LmH&^IZyYzDvI#rYoh#i;EHnM!8mlcz*Ioptr&BI*oQgstkd5)Y0E24O%tZ=M~^wkoTJ<F&H0+d1O3ayrj{i=S~GO;8Vk&YfRHpWR+eiZ)OPCL+S9DaiwI2cA?-<K}g-NBC?`bY<Tmgw==t!j|UgsdLrSl45!kXo$hSoOzhDD#U0C2;FU+;pg-!C>TXej-<VB3FEZO@Dg$X@ozG@TU>}M6P)Mhv5^m;uEvt6SLwIv*Hu8;uEvtw-~dc`v;R*ahN$3Qp`14MG~!ohFo&nlfM<aq1Hm~D2f;9w{7K~Olfo@SNIhlz{_GL8|L05yW_$TSd$iJx`Mra&A1o@)xAQH2*oH6p)4;zp~VYHy1cRhyWi~@L+~5p!mT+2%ey*Z7~GnnF@LEuE`hMi=X?yqnqFlW%)A91Kl#Qb@Zn@cjzDW{-=1%Ptuq$H{4mhx<mp$C<mUz3!G@xpt)Jbt=C3f*C(?S*oa|!fudGXNZ%^%%=+?m6u1ls;{ybHqeKmj10BMpYZh6h>s-2NKhV}QgSNa!t9sP2&OHzk77RSQt@aMb^UaS?b!>!pJem=-K!Q(o+Bdmb+R|y^~Lc&bXSg{e_pXuSBCwsil8yDRC6`sJ`nE)?-+zW(_uk+p&HRvh(Ma~5;@jb3`THgMG{`x?zIUC^#C&4#*gYz@lBRpj?TzPM}e8yiTfrPhxqnBws@Aby(V|9%U^4=#le|;BL<CdS$LY7fwqvHI;=9h)l`LtioL}i<*k~cHDAX}ZM{E+|bg9}Dlv+o6WfvYA&Pu&F|54kcJ7#nC|<u0%%e6&x_#NwYA3`{T>SXBGy&S1j8pd>Wg&(b%;&qxUK3a+qku=0-JJ(zlML{q~pFjN7aW`QoWpO<ij<OfDk_htqY%MQ@RyN0=kS350{>KhVGWCLjt@qkV87@#yKgQ2jMtKJ!MxvPI2T$jUMo%P;K_WCWGx{*$B|Mj<LCn3X?3x&`u>GUTGq4k0Td%q}z7C?f{uWhXmnxqh#XyPP?*Lu-BjU>{uep7axlk23;$Z$|%prMH}CWWxl<%C~^*@@AK(#i6WR>bgYXjfZWbuV0S&=9ge(+LH#KcWlR(-%d-3Zs5bPnx%xjoCnGWVV!o&A+IY-*E+G9}UQk)qFi8hHH}J9obcHEX@Nxg}rt_i)GW;%+Fl@x8H}?kVzIe09I8P=bIhqh(<V-V`Ca|I)U<+ninY(13g9=lGO{;(?hfH{?B1Co6}s#rul|(87UhspU*>m$QUn7@`=)v3|#~?0>LD(4mfOvUm@G1&6FwgUEoox<DQy50a+LDzB^$#;L3vF>y9B@*>F+Lv_K)x3zOoYfSvxLTUdZfR6et7DqIIx$Z|4kK=ypV^8-BN%&{5HaW}44ZW6R|kwgC1{{9#G?Vr1ud9TjvHmM;gEaJY}0@nJzG8UJdqQrd-<B{!_&Xm+u>LVLNiL%FQi+R_uXJLgsyA%L!>c5@j)v5lA3$ELnxE9gsONKl*WdX3lznk>$IX&g@alHh-?|%*RxG-R?(|+=Cf@z|};oTSBec{N%a$$nfsQZbKen$^U&546M0YK|FOqVuwb?l&(+-JbRwskd55%zPuV+7c!)BMM0<OXM@mZ5qJ^_}YvzHH?7lC+7`OE7u!efWpH>n&Yu8DR|nNXLlGp9M0B+`S3625;;T-b8acPA#u`0|QB*fe1D9I}fgGmT>|DFIkip7*O~^G#wq=Fi*#>-Y8L&GMRf!GE=FGSMSGwoAnL%CTdSaQowN!AwsR+sDnYCU_141eFrgPyf@2`&g=(wSXF}}{*D|vo>de$?E6IeByMV>04Jn%$#knm6B$Sm;8GNM37(ngsX^R7o`kfy2PKeTHT%{S+V!&4#4TPgYe;=I3xO%5H)Gf*TZQRnj<1SDsEfbA0HWQC_|s2H=s!Env69m-;Nvm10x4deSDzB7;XZm<xYduWU+0Gb&Ud_xoX$;-E4Nr>0D3vK!i)%GVW5=`-ohJ;=Ku_U#N3xT;Fd7b`UT(c-lC7de3S9BzKL7yzkk0?`8wl)3!WTZ%2mE$y%)0rHy^JCZekr06SpQF1_nn)In=7qY&-gydk8#Pprf{IUbLp;3zTTY!xUF0U_Gus+&W}q5iYognmD|MD|m4thDkmlThS?q5(8mf3NO*;Xto;JmhxEdViA(JR`CNFDUF2w1v6kG7nAAv2m$sw%kKJ_p-wLa1!Ygzg;vQ~#M_t9j2y#{v3&nWbz1e$crZ{q8T0E%E6`&E6FFsa9&X9==XQq4HG<Pz<GVrLyAgL$A>Y{CcC}!@M}e<#2<_y!8L?Yv1$6b|6vd~cX%5^6{T`s<(qTm#2#;(KU>ptRS`j?)jyrxDXwpLvTb&ELg7+rZW@RVAW^hpIysZb^5S>T(rA&ae-SY^U^Um9O)|eaCRv;n6uo?ROw9}mJ|HNm+{+@X=!gvv@%!ZE2dBS3vx*C<y6GFCNo!NFKMr%nF>qx(c$l>Cd_X5U8*Tck+^xR*1XJ_}}iIK>i0Lo-=>MnwYIHIt6V8X4rfilZD@J<0haRN6~%FYAdejpb+b<Kq2UPhvL_$Zf>BiLX&TSsuMiarj0<KZ(#&seAEJ@%y*7dCAo6znlzgK=t%vVf_2YbTFS4Df3&whud#)sN)4!j6;}^4oeo08%5d`cv<W3GH3Ed4}}Vtg*@y3#76jLoZ;Vbx3AdC|Aw{LJYGy;vHhdbe1`!Mvl~l4@WJSq?F~E&7O@qjRjMp8VwL?7j~F^v0wzyv(T{R^abEp#unBJ;bM3abt%Xy2$mLMF)G69R9`yK1$}gW3U{Hcf&Cdi6p`zpG0!5U>u(YAAM3~d->weIH^HenyEv}AhES8_YW5mV&9j7>{p$%eVQrKBgj0hI7$tzlsbP@u0<DH+joJ1r%Z@2rA=eD=My`qSQMnH*vk8ug5pCEPQhP`qY1(k3^Ox3`l<2D8DEDiwjan#Rmy2<ekvhN1L9KiTsQLcS+B#B~%P+qkwtT0)+1Wa>L}TJHWaI_jN|+0Il1mB8Xl)&t{q?+?;pH%9My8NC>1Kbu9t%nzSMYMoEF=guAnRE2NDW)Ax>N64jD?~G=NF3?!x-q#OHVx(wMIU_nbzxw88qtOmV8)`NVLA6C9=9S?rjmN6X$NVjzFaZfxB6kH7S3a2s=su)n%YAE9qZ&{oW`IDX^eOAgMcB-fCmv4td)etmZMwHgPmo39Qa@z2{@y#p{Lb%y}yu4){&Qjz=19q4q|1uDU?feXj0BAzCr=C$v1>J3V~V!+<Ikb(KPy&AqT&GI|h4>JHC;rRQxkq)BmIqy~jb+{3x;$BBPESy_y$Wh%el{YFjKeOB!EXuZOCq)Up1YRhQ%7A7@y1AaU?+Uxoa{nN?`F?9xcEK2vLJHfjdwed%6>irb%C%opaM~HpPKoI04<W%m9KAeWxubUpr$OuC{a?QAQ4A=u_VI~6wq;uRO0j`i8rc0mj5hFLT9kW5Mv=+FGtPw&B=Hzw{*ztA=l1tpM@ypJkT0wVN<mYMYddczxD!)h|=r8CVFSpNaP48T6tC7TIhXm9lR@%zjs^t*UX-w(0snL0R#ILL6%}<k3JT7m7g?x$j$6i|;XVu7xTEWH`U`DifD@#Zw`nJh*NOO9#$YMQ#n^<6{#m~FS;F&LZd0fHl%tN^<$j*ay?5Q=bx@4}0_Gibkne4c*BB6dt>OUg)BTZyWi#CAIU;uQgA9Ul$t;Y*uGsN=rSyD&8PI><yyl08Ke%g;1t<Teju3qGx$QH?f8aa{<>vCq=F#77u2pB$02}EP8k#&j1HS8dFGcVzFV7ovky1-HjTMuyT>t%dte5%gTr3u#=W5aZYxeCemhUcjth$6L{z!1bW-30~^=9q@M_qLu-7gYR^7kj&^%-arO6M3g;2k(QQnPV9>b5jyyC#;jO#{mIU9lpCBt*4$sT9Ia;N(;@pkk#)FVV{xu63wxt##EP6hS1LH-gSxo^`-Rv)#ZIy-bwCZu61uN8<d;!Y<Dv5ttmOm^?WOhrM2bxla6FsnVp~4w2e3Ct@6>Sl%3RqG%jgJS85bCl7;!$bUP=MjcSYijChJHY(V)-UZGt3Q`ksd4XHYPbBeZ4V+bxm8i{^z@g?R&imywMHt52eZF${x#_s9Hj9X3>={+hL=Bqj1b?D*!%2I3yM1y@^??4)XcPuT`ND5Vl8djv8YPKhC%(v84c(CjrJMpaqq)=e$u_>~OBs@0^Q~8Z+OhNIIfd)$A`S-NKinsQ9mSp{g!7q-MN%56d1Ek}aQwdoUpc1Gm0=A1S*Sg;Rgi;rcxUrA*H~|!@5-VMluu07+s(!s-T?qO^;x%5ai~!X-kS?+RWJ(gyBu=GW!jl}`1aUO=j*@Mi_Ak*G)^z4jGO<P`?9}(o775%^;0nVZ1xJ@@Qu$d*&E0woOhl=`)aC+zb}=2OcmenJdMBW`u1a&?l=aG&ZeMqv1GepY>=TnmR7NJ2*Seb4<Ay<Wrm6>8>yTm?^fKoUJZsz}NwP+mVJFQB6!HBL9Y%Imc$+~Gkih}ECN*K;=T71nAE*q*SK{sUf^@)S?x_!$9<AYNM9B%XOPt0QN!Qe2SHYj^^F^djs@Tx96LUS;3%cHSJxexF2f{|c@CGej10w#HCa$O*qhNqBySH4_wZr&yueFPEeuZoN1T8<V`Wx0Ho6ISSIFj>Ahy(`{<FiSOrsxDWYZ}^fWk{{?01sJ&qCI=gHOMUkxuz^P9j!9Th5UxGAqdxy<p2Yp8iFUj1}7T8Ixp6fq)olEMi}+v0)-+eqDSB+-c)yy2Et`HqC27eYnqB1SjAe{rpgD6#XJ{9es0pDic{UGbzLtqS2hax$(_!LQ;dkgwCETj-~~{^GWlqn5}pr9FXnYlLPUbd9-u}VHTBX)z{;2z`fg?Q2Jx7vqMW?i_B!BDR}=e2sd+4?m!pkqp+?~n_ttuoM9RD7!_M4&_at;gk~ngGNUK!wXfOsvTjNEgep2o!let!-k1lsub7#ssnaEP{^j!fSqc7N7TEfU3px&P&idVvB`e>KMJlQ)lWXCIflLEZ4g}0*=;3&YWu!dpn%pO#ngjZ{ni?2@<)Qm%u{5#l|)ufR81{R8jFhL0+m|^NVK1_f0w+dbc8NfBX%qj!8)@XkbHIvq;8HFZKfiptQblOy-T7OSbGu@1uvCca8&*y+MYOb5zdF!t$f}wM2?oIDFnVlc4SX=l~*LgXcQkI_}1BEY>HQH~R_$WjmH}BSE|G1T=^w+=EeC$~Y|F|~0eG8A@$7Z*oK4!>=s-TqoJS&89QHYvrOkDD;E{^K8aWaAdxlmF_FM>Vd)A@Ly7A5jht9*9R)ku*D2JA<|nWRN%2oe6`w~N?EU~pi$3TtXpotxL3c26s(-CJ|o4c{%Z-M?fLbMM2Cyj?#oXfoCiV0#5U3QcRWK*~Bf(_~~rWyhYhXNT=<aSQ;8<b!8zfZ31sIEu8yEcnMVB@K?2q#)wW=T(<EYK8)Z#<ddjjv|PX@AFb;p;j1!i^OeTl}xjJj&jNE3|~hSM{2Fb0SUGWDGC$p`2x6tkZ?)hHlQ-l1I*s9QN3zuTNTu`n#r8ZG0+Nw)l7oAN4<h62y{sExsF1|a!o;}Kb!#Iq5><8iId<|=i4G~_dj=0F=S2O#}g}t(aMGOGxB3A7kaPJP|30Gy?KvAqHcI&l08s`uUF%i@Rs`fN#eaM-UTSk4p{sn(2gNa$xVIuyr-Tgqm`nHfoaVcq~#Vv;WiV&vKt_Puu|ad;Rj7QNIEh#-KYn=56tzEO8Ab?6v72lq7pmq)u@7cefP+4Q~P3JeS_&j9Z6?K8_`NAJ+o_-6vHfSg9Rpz@|QNXBD`i2-ZRYyp*c!pjt~MB#{)4-+^VuEiKB2SJ@FLHX~x=JfBK#KoKxNRp3%P9J=^CTUsAxa{)F{8>lfZ%v^rOP&PDrXLGB{|?=JciR#LoZbq*J;PNe<T>NMa^qWsNp-sjv=%{;AJot##)6wa}Mckj`gW0Mnk<VBw|Tc4AQFk78imhaqA@SwkKW#pfKoyg{sezR6cQ`p>GZqz=n3Rh{_qLHfy;|8@`g<8a3*4GpkuK!)_)!LeRX)IB{ln5>-aVYHAq^&?)bV9XJJ2s;_=UWd`>Uw?ie#Rx-m}~QVxg-=1aPVM@VNW1Vl&=yi0GS!ez~qwYI=lSXtG$pBMY$fc{d%+Q0rSOcqUt=HQq~Bg$kgnZk$4LUT$fT~Fa}e$*BT2T37b8_{Ro(A6<*Ysoz=KlXO2LdhCP~V4WZ2e>6jp@TzB^ZB*?-|?=ND_jXJ~MZn*hBElQU^_i}msJnMP3-rAJy0h+pKZ=(NK8rbYI>q)k1AkfSzys#!ahnuL|M704^v|+xAJ%fxE^I1R|V<UlNEG{U$5naZnL0}~TZ`2wDYDU+HA{kx$u3^szV1&oIC?cH2Y``mvB@StuYhn^du3W9NZi|Q@XJLmrAC-_J3+b4TX#_=NVA|CYC8`1k@Iuk582DdVfM;>Cv`Aw(chD6CpVT{O@Uuv+ZVz-!ophLPiY9?MXFJ7k58uvo`<C!HA8Mbv&}f?hjIZ3M7D!G4GOTsfY@f<c_Nj(5_kQpD^L;9v?^C+T(*3hwoVRRJf9zY4)CN-eLg78E72XHd;U%m+u7t_YgteuZ$Dt*XENmK-hPD9Ovsg4lZK|hmXMJ#>&NjXYp^E`(+i~E9>S<z8XMeBKT@Ag7Na_%JhCG<A{$}K|lEUsJ*B2CSXGQ(pthU|UEH1_0DW@NQ>01&nkFVC;9s#3Vbb%8L3SwF$%xhGPTqG=rC5&<601t%h*3m75_-3{sJACpW<HIc`bT2r3J?ew3_(C3SP-VANk8pQlE$e3PE!Dgt+>lL$m7mhw@t1$g4_>f_EqXVRD(0)e$jBqzGLXsmV>lYxd?WF$jH~iP9P75!wBSb$WSy0F_w2_VECRFP<h;DWyj+ydhp*iK_<@aV7!4KwWV<g6SGCne-zPuUm4=t=O1r4Vl<@Mlzq2Tq*jdzYBUVM4X0>W$5zW!2H%A-rIYTx(8zpD~eSDOz542@6RQa~05b6Ok#p@Ys`m)&BAUHKHAU*)5WJ1pEELCV;HcIQ+Vh9)2YwRCu7aIVG(LtfmCixBM2IVN~8N{g@`7b!Lw?JIU&03-5cv;3=)iC`>Eo1(N?l*k?={9kCK*W91^hk|HjoGnJW*oKysEc?nHeWr_9y)*e!qh1fAEJ;2n5PHrxhVE0O2U+$mSmX1Y$sXI1I*sQopFqK8E&pEt;BM&qBtdR6-@1jeF<n(Ght^*Lv{|O0V&JLpyP5PyO-*W5?Fm48pMfC7I@cbB8EJgnC(|01@4gbmy*aPL|@-W6$PYc16g3+a|FH769NtyXoSjpF)(?-7eq*XGJ%{;YSH&0>f>Omu``upMk9gja@XC86UpwL7VkU%N-gJloFNsEy!gz7H5iFlm(ZeMr39<YCQbwGUd6ZcE4y9Kx)QP;%6g~=SXOc~F{s}pHawRVpc!N5Oifw;7!Mz?zav%~nDQaGNOpuwNG$4OQPthhb#@(6C*p^T1_6_%Nyt*biS0CaIh8Y7!<ayHQv}cfd8yghkG}Z>b6v8-CNI^MkbRRmj#jA)eo@t#{}m+k%{y1@FV{w?5&jSC#LN&Y4f5)95sMV*D>wNbR#@Dk9l+kD5dIj<kvE)mHT9asFPCgd7g|zG-fa68!H%y*DzxwD+vnQ&$ltQgwNZM{QPqQ=ve(%6oqw<U%g)lgI#0|YGldJo%tZ=8h^0j$L4^!!K|8X)46){Cc&Zf&nCx2?6i1mn2b*a$B;&sZMqRz#bHc<&{yY79FF=>x(ZNd-fFVnNPScHzv2~53TUVd7q2RPamI1e8Sw+?+LEW?NyQDX~w{nyTP>cFZ@**{5iC}Ot<hgib0fy;}i>r!cZvDYtmerOWskb;YZ+(yCR~V+dhI8^apjuBxtfhI_t;T_vfO`m3`{uO*<@D_;=pm5M6IqbC3DU~w8Y=KlePFHd{q;O_^Y%RSj2e<yC!V#!uhmN}j!+&Np5&qFS{~XxUoX{_xn3_lsH?G5O0jmprf4aXp4RDSZ%z9140KLE8HoU|%ZorvXZ(|wVFE?vBfn^k`V$xYI3=sa1=rDXMjn@{1OR4K-*Mm(iZ;CjKLMrBgr)S{-pf57w$LEiSxe+T5cSel7z_}ig95iz(nfjPdj=YTcp0n@J4x3wj!^a&U~!u^frg@?$Ws7}GHM{y(Vnnk7KRn||LzaGq=eDO6M;}V4G8epXK13~+p6wNf+`{qroRtqvzuGm9R=!$1mSwHX^uN^0T5l)W9{VB2MA;uQ3K<?$G?7eng=iNq|DJ0p%`z5#%y54PkIZNH$%G<l9S)%LT*T|U)>4)YdQzzf+WQ%yY2^d4l<8$gcF>Ke&yMs%*8E%`{Ahj;qQEu?*E3Uw=33$@7Vq4^MO^;C$0bCO5eYKW#8Y$v(`V90(k?s?!RoY<T0f7J<-j9-MMw&|BMEeuhF2W0}$>z%20qe%pDJHX~6*0^vClaY)z-F$+kO27()X~`D~DYft_h%LId$j9>fcffTv`rjtvHNL^v8K>%yH+`P`iCeGGWOe^KY`@RV4b03<zl_$?ktoT>|89{~Wy?0e)KY{cSn<OZMlON0In%mVRnPwr|Rt{b8kXHMHj5(I$n0(6PBgQ!CeFA$3x7HKl+;>nhV9wyAFdSlJ+)Yf5*fFd<G)RrBBf$-o2N2FxJhpm-Q;uYz?p$1#Hz3En+yrnS22ji79;W)8XFpZL*<dVUf5Uf0<+sB23-&X)Qo81bbasFa^F)2zCA8iSx@sbslYKx%5OQ0wOjoKN<^2UNow$LmRrE^x`P>3!!*JSK7VqqELA{){U#Cw`Fc}s%v^KV$s^X7vQJIicjd!P&WdfDQJg0@cb<w9jFzG#;$G0EYIT8*h<s&>=c;^k)$owgXq95XgnO<TfB)2zv|Jm(w?OtU&(3~MLlu=A~E(KKtUm&D1X_(5!&-mO=$vn9+wzl8M-Q6gDd8Or05YzX$YRjftV6j-RKSXx#qwk|;rVo;ljVPd2+%hn7as957^ZgSFY?`o6N*v%ia67_5D*ZnjT-|7>0#JM?EF&q^S=16Bqr8LEZV2TIv!NL|)E;fYB(;6$83zbiUrK}A+1jI+A&m@@|_GEvHK*k~<wz@~|&WX&poY|aAfPsvAas#k(kq$`Goo})x*jwwJRHDGL9q1&uC*)TZ7~0i&G9ckWl}I!Z){Jn`8^jhHZ4I40KNl7Eq2=~Zbbr}^mmeeQmq_Dctm~eitOUaaF$i~)nVcwX#JbtXj&YwT35Dj}z7QG*vWD?h1PJ!xgb{IFHsreeMO#_g=2A?xLXkY~%LDh9x=0^W0<CSR8Ff0_T!L&p@m0W?7%5y4ptn_yQWo+_?$Zc4>v5ZK1!KxlU#@WD2p9l5Z?dvDQvJe#H#6`q8dDfckibJ4Y~>HF;zZDDOR&|t8pFm*#R|T6-ZzwX&)p<yP^kroAPW`kdSQpelYxO6TL6;Ea1BerG`OA{{GzFj#EPgCudSfLD59<5tZ&dHG=wtSdEw(CH)U4&B|~JqKapI7#A^B+*kOlgR#s@?jl$7sXH)?l8KjD-IP%~ATEQ+1Uf(6y%`92ewNOGgPj?L>kS*Blqsoy8c4@%6Y#Br@qL5N2L1#F$h5wJz;0k>$2Jad>!`IKinX)dbXzwWJNbHD7C)G2*qG^)dai)Qz@ONg5oo^hkwb&e6xrW<^?Hx^pdD%XKTS8%$R=JOm=(*ZT+CIWbRKFFIX6_?I+I87VhWRO8<`SFz9gsi!e{HtzSj7F}6=0dUf!1-V=I3No8)Rmls*R#D!(k0I<E1_}lNM=X?lmO=U|K~z^mtpzHCYMJ1X<?B+7mWN-_T&eq`S#^rGfxe`vNE^Vyp`1D(<EMZDtv#t*Na7k2>RM4vcFg2cs`A<7j$v{Oa!tf211I6Mbok8&w<2YQly&T9K;#7GH2|D(}{gqmQMmeYNW)YsxW;Y^;){DW_>GKhy!1n31{aeeuHV)C+;h+d6U=`W0zCbEDOZ6ZtCjdfo(M3B`}zo%?(5KbQAx41JBcob}#!n9Hk)yz|x`=45$pI`8LdQ8fO$K3c85h6xiEt!4|)&gg*>ne_!*#MW14^cK<<#151>!Ne<9Gn(oMp3cfVLXOLfR*box)VYD@fN9%c2_B7i?NfL<yWOEd9JBpGX5M+50~M}kCi@_T(+rExd9v@hLxi*foN>y>Yg0a7pYq5qJSTPVTEQ{jyN@;B|NIB*%REmh&#$JG6Fe^sn3jQNFDS0Ggc<>I#VWV?K6AKMtnz?Z2&hG|%JWL?m~7ER<vJ@-N&Bud##U*u7>f>OpliU`WZju1qwM9|ZhgVT{U0fWFp5D?2QY0=|LUR)$rIa&!-U&kCgtLm*YLhuam(v-g@~Z;8Ll2MaR2Ug3A<Kldc=Z;gzm&&df$pox|l5=7>=kn_<`lSs5F4Q!H(y9Xvj+R#c>A)t`YT%jx`3E)Q?mvRpUqDBrYYop1`z8MiZLHuG>NCw)X<15`2`{V~EliRj-=Ft2zmJR+-IdkhdKZ585xQ&_g5;&3!dZ_+GZCoz6<uFp)`_EOk}5@uIUsTM8dafl|;ZL3&l%Wg2&;_=aO<hLDkZ98!tU7H^6HJdJF1G3J1jFZkDAZ_Yi;=G>b)DXCK@6;}CkPmt-Jcqwx4b4M9EOmt+e1oEN<SYP_R9L!*w5^T8lf?T(0s>_8Jw<wN~q=}jnnQBD+@}HT1qou~;Szphmqvdw}XvPr(iHDeaNu&`tX9LjbW26LNcZdUf@e>uIn}2rbaQ-1l!aBtRzZ4k{q1z!p&Ihz5>hj)o6gUNF35p(_J%j7t>0zW@%0Ka1;iI3S68$3zu6GgwR2<2Pi<|MmeL>Bl{$6e@E;I>1zXO!5Z`yw8$U=OU%wkLrkTB}$+)gbc!n979RiFEqAKhmplgE3^3@jjbZo{%{{pvehXQxn;$Q4{MW>18nJXj**4@}g(d-(mY{<>JXha29Toi7tYfqGuUz(rTZc@oCM5sNXjKPlHV@JnOgy%*xbfv7Zv#|;%Jp=^i(^u!|HfopSME3-6&*FC8@^*fod{Sot{r(RXL$EZ(DsUsX^BZH=3qNLNF#RR@fm;)34H+O&yBMhoV3_?oYt^I23mHuyhdran4@2D;qqxFuSF!iqXj>eUiUdyHTU65kI^+dYflB{54f0f2O_l~f6^mDzH^-60TQB)DtsH~txm2&Qdw*1YU(RoKS(2><=n<{ejS5oK;@~G{XW7{va4fFQ*Yi0_g%4OFaR$Ze41yHXdEGsp)bMj13U}^E#Me<y(OXz)U{k;G4o9b(}2Ej|L=C9q?{GhC6itTBJu362_lU+*cQf@uPr`+bowV#Z2*d&4G1_2F7uG5=2b(iUxA%X^oE|L=LsJZnWP=i&!6Y8D3ZwmWw#8TM|t*cvUGxTa}vqw;RE74IG%s;nH)qF8keb^J`lzDSxw<HZ8r>XfT-&yeS1)|FSQt;6*5nX#(^qc>my?2SVZA;IC#%qo_=UQ_;_S$Pd?!BjO*{*Wc^`q=k2`r?X7DBY45d@6{ArWFB6B-dTa3X|5T8=`DZP~&I5fBlgL!f~W4<QgF0)zqz0zrciXwZo0At8`JjPLvYF(2!(_de&IdyY-*t5dtyUVE;&=3~q;{>S%-&k<Dwh+uX86cdr=YL5o#?5+}3Dmo}Jl{KQuDLSZPA}S!l1RwE^QB-a(sm2NoQI^;hi>cX{FG>{<aq~hz#I2zr(!Vxe_VW|V{vD>3w!HYv<(=Xi>e1CZ(1D5J)gh&z8I5$j>?IjbvYGFhR+Y78i2lGS1_IA4Uzbm|iOCpbRVb(vjG``Q#bFH+_qN<gIYdb~BY}LaJ%prQkV*G<_3#2^G|LTKC478fd{#0gh`m6duY7O$S_N2E@hCeRFiyguLB(SQxi`OIKGFB+N^i6KB@U=w3SqT1*jcZ^Kg4i{4i5FLA<5|s-JY?U9Ln`=r5zoF7u*T5t6nfBNnfVRGBuPyWZjtx30qilCiJYm;FEo_tTM9mV<C(Wi1%+zpez!hh(-C2mZxq=K7YlIO^5ZOYk)Ey=sc1u@jM;VT`G?U&2v1+=6ap(-O(E{JSk?m!xVbkhi$p(EBEN3VExl*yF(H3$cCK1g$Lr;mNl@a{>6Co^);1hqO@>5Y!f{6iNdt;O32xGl>Slqf)2RQdl%o73;tRBtfWi#lr$oh9L^|PzvGkD@=r?7S1ZE+e4gxbVj23zpg{ws@M}xxwt1J>E_)IUm!P2DV5D7bl>}Ffolc=a_AQ+={Arv=cp39mn_MMxurV@ULb;fztqqyX%Ic6mXf~I~aS095F|MWuvpxxks*6^MpSMb;IFGAniC@?3wDZh@^+{xFQRN$m%TCckJybr@Nw)+6p9HV21$<S+;ZnEcQsX`Teh{<y-ic*QcgZrQd(JXO08H?QX&IB>*D~hqfV<hP6Ir{dIdhHqKGVJv*O;%)Tw~JAHRerqjro2=Lra38I%RW>X-)hh`-O2#s>U(tYa7SJY8(R`K{6FlJkYd{Npt&{<d5-r2N^6@QRIS!gG_hgAmecH-;O3SkP2pxC0Pv<sDYV}Or<Z7<B#VLU-6bc5=q<_in`#C<sfs(J_g-{>K)V0yklepLGKtC$6!j$?(<8=G4X>L$C%Q>TjT^6y<-Ri{mAw){mV%_xD-SSkjg`K$I9l>ghI=J#1c0Ja`04n2r{lTmqnX*MtqF)=*7a}Y)E#F(upYXo6HFwl7T_Fik=VSprDK>aA#mhV6Jzyo)@aGbQN+4l`g}18tYKQA)(T$hjcLi+D>E<NwwIwrMa?>k!k9JF?j?Bo#w;>i9?WHsCFw3llfeWv?h2R7l=3~tYl?j++NfZDHs}IMS5zJ#ph_>tW{I3Q)l0s^wm`94bvF~XNVtt|73#9(VzYJ*ShgY01^;I$L7prm`#5D$}b&6T^vtJL#UF3EP|?g@MgAL|Kpo6YHiH=it(ye%8n6wsttD%0}1_y*)da=dD^Y7G$uFlgzQcQsR=UB{Qhsfvp(asM$jeR$J|wEYeFsas7V^n6V!dB_K2tO(^k<-rM)H?B#uq_vRxxHr7F~@si!>O7)qm`5-VG+2CurCX^DI%A6}W4pA-oc@F3&Eq)VabO`fSVLVDB`ihxrJRb$1lfmNli$J*FfuaQWp$VO&I7Dro!8VM0<Mck=cjjNYvHU5U(y|oYD`Fcc!&Kuw4<kq!*tB{Z`7P9`#2D{_JdKigSei)g1)J7F<%N!Xv2dzYnX7i_<W;1hSkbgiYxo9gbj!b(*L>(hUI#(feA^06{#!(--SHCdyWi}>97W-LQSej_cAaYOnAZGvij4dR^#-Bu&lbyriQ)bR1RY+vjSrWj`3u87?t)Q+sFtqgbr#+KS@>ZKWtboI}+|RspMe4ZPtogdELJj4?l-ESAOE-0%rr`Rt?5O{sFw1_8ZBr-6HmGj5+SNry&`lX^@XmG6S&v@<8eZ2NVciHaFjELY{TRYP4yg@F^@ZV7^4wJ|B*K1G+u_i0rgL2Rkke0HuTWQ~9Bm@^5MgJeB_Y(tHV#xl6_L{B_+%qEh&OF>B<Y>D3OT>vOfHrS&%%MWSGa}_tqzG9`?N&pTqHJE$((j1b%SK*VsXK=D1|DGSobCff^9bbQ{g?Fnq4;r8F68@%uXL1Hx6;O+|`A`2?$^RRawR9;Hyo#nt5rq2ZWUJpc6`79tkzfnJz3fii7I6_1MyQY_k{5Vwti(rSTm)h>`GDuTPZ4Pu+O_)wV;u&)Hi*QZJxBxdwl{%$en7{|i?q%!bmvLs?0_>-v`F2S-a}l<y$q`y9i6NA@W!z*M9x3ri>Xg0;R&{67q?A2n*lR}i%!xjP}t%6vGWt9I7}gE?#VBOSjyXIpPt%bQf4B>{{<XaLvUh{;eGp-|O^%g#Tev1EBD(;m}KM=`;2L)##$CCtuWtYv3ID)-jy-gv=fWy<@-=f1s1ERE9KUv@8?v&wAsE%YEts%^Mht_O!So0~Y@a3!a&1d;tp$fWosu?t&;!dN>d2B({Zp2}jmNzQn(da!H66{NM>I|G!Ge$qCk*4D7V(PcTavAZ3oxYyJa?NP^mf>#$>PX#)hYiXNV*hyysVqbZ_b^!LP!BfW=6>k!;mDmW7<i7M6g**1r(DyaQ9t9g^(A*%BNmVZqH)@m=Cpq6uRlE9iO)^<K#g>{7vz}hA(kzqJsdJps(&F&Mj2AQJtFnuK!*~P?3%@RpVBkO)c?3}k@YQZe0hP2>I@6Aj+L`r#Z)we-jiV+yeFQ5}Ps_!Pae<|$g6jn40^MW@u#9D;lLKQz>!A{lWSHepOggfYLwV3vp5=rytAZ=6G?mJD?K_GL61g0r2@7H>Gto<htW|>`$TE~4Usbw6n9&WAQ3HakMU{R?tkAZ^*CjTC4UgWa(aS+MqF#tfNB1nc**c{jfSwX+LvUPlO{l&bqADOpO{4Q8mxlPyF7$7|rUh8I!jf%k@ag<EyjMFYS-8>B>aP-IS!x~JDq3P(tpvr7#r)ZyBnlm_%1JvYvWPo4T0gOMLZYnvB2QevVyahkv;Y&YIijgBcN45GU?*0B$I1T-{cBdtx;uBPDCEz5$V6^?MQC4O)ln4tLKau$hnc_SnPyQiU$BLcT(0g+YR+|ww2kQ;+j8=~ZNrqal>yi_ldGdoX7~sA2pOasA+VTlXY&5~6~VAt`lKH#5>6KcvJfCN&j6uOh<(;CBkxR7wiex5oG)f;y=LkCWCL?^$$aThj^)q4^IbZgVvC=@OIh=<Z@$i5Vym?CixgX$q2;mZ!pm;dhRuIxcd1N;=6s;;TAbe{ft%4WA@$#K>bS_Ml~7;0QGv2!YB~&P{^=1a_qI(y=;nH(+NEF5-rDJ>mObTOrT_S2z=ztUlnI(2@Ga;s5^~b$Sw>sV)lv-f5{=VO0-&c}2rcOgO?S-;LFHN8+m58FjWe(F5%Qg?+xw<su!+O*G;E}4NVVlOk~-nv2mZAq>O$JKe$>O^&@g4Og<xpxRvZyD9+R$0Uv1O|1ua3110pU7sY*4Y8dOq*U;$8$@;mI>FsE?>m{u<02J6da)=lc!O=39_EBVYC!RR;Qb9RI_Ci?lR8bDPf=l`L1Fe{cDW0|RF>om}iC{u_RNc`KfZ-3~+9`ze99iaW40DNo;F@fJ7?P>4f@W;z}6WBrr&aiB@J}9C_>zhJXRMapdMPFvlBMnjjICXMhM50}7hh>~HuV02RFK6z9gd<kAJqB_nqH;wutDZ0c9PKTJZN>%j@z-7oknJiu_S>!*5U4bGHUMiZIq9%*4Y8puv83frw~12q<bmQ>_NDR$ItC>bXoG=VN9Zc3qvk$`joT<_EdSK$y83|%n3-WxCIc*I7%Ox{++rH!x8UHr`dLrx6>pSi5<}zLJuUzMtic&nmnF?CA@(8g9XyaNC%U%E`t!UP(R1Qx;cV&~J4nuo&`ku+Kv$p@H&Qp8YJXjeFTzgB#^iRkp2)v{^Zg_GffdbpM88*sutxMo6gIb|MMS?h$pTD?l){&!Oh1P3T)czY$SfG><5>@Eg3HN9)0gxk8>%0uf8LNBY%7w13<-UM6V#fdPMWB5Qr+?v8TTJblN4FT^xFrTBMCFZ)-7f+xgJIpkb*b~$Q7xBP3cpc_8F>J(cK#gearw@&$jxK)3&1=86Rw6MWnoD7Y&_oZ-tPi!Z<xOqZQV~8D&{)2OI($gj7^?(K->9Ni;kG%O2V9Z2rniQ~ukT?p@hOix)t3NWHIFCjKjqi!uOrmS(oDRtCpRpBQ~8RkW4?4j9XT=S8L;8%s_(FPU5buU`_-fmbnDJ)NqONSR^OTGLo9JBOMPQ!y75k5yx4o-0X2Bq#qhrN+rjoPrVmmCL75(aq|E!u7HF8syXv^0H1xX<Yd@1ThqpgT=A0v}jaCnF=K<jJCX8R`eWqJN~TIj3@;Q)x0$X!kEZ&ta=k+Y{`ubCe6pcjv9NWoadDAw$(0Et?c^k`cjjGCz-{|-Gd9Yb+yW!`o-UR553j)$WI?HxQ`+L?u-hGi$N<Iqdm}PQB{zR{vuHT|AgWhWiug<(x5gF(-wov(#!H@LzPWVo+zuJ+)g`hR=igb*kNXj2`Na=7F=#B45S*LDea`g9=6#~zg%r^R`K!ijTdzVRXJd7XHeEeeRaTWqmW~GX71L=z$DGTmlZ&nW!j*XBEo*1kTVX_on%mi0@8w&EIdTJ4Ujr(R5V<l;o&B+^#OZcF@o9H7(@W+|Hel})U)8f@CF;>VG5gFbO$~~EfXJM@o*$&m!jM9%2{}WMe@qR3*zB&-=dLd2uqyB!&5K}T$N|XCKF&~DC9=QH+X-5NOX;atHP%UO!0|GI4L)RXoP2@rjHz(h=gbTEbc5b)@>Toh)Oe_ql{8AVOlX*KcU32`(PwTJjVS6tFS2~{(WW@=D#>WR}D*a)wjL-HX5rFy6P7$p{qED_;v7WqN}?1Mpx~9UQ0nIr4d?1EXU7z_jh>NFB+)o2XjzWTp+3>I9R5tUqT$La7|TI!l_6(l==LKrRpn|DpxF({}5QJ6^r>@1yZf%K&nW`isyh-EvcGbbQS`s(nTQE3`NxnLe)(8sj>*ZWyK(0$4}*opK5?=Dq+cW{FHaAI6<ho8HDQljJ!t()sG0F`r;CVs(oJw)o==-vU>O1co9GK(ZN&y)pI6ivn89JHVd4AS6aEm8T6-=_(>m~An9%MGG%nLKyk8Qx3ceCy#WG5!0>BA*TiS06%F3E5>|?eq(rnmwLKvbWG|cCN=)H?=(4(+YLKlrwV6<{rZnjZeQ*9JnUzXkJ;q5oq0<-Z_!x9MZ*o?3C&3u$7NbikR$>w5teeIpdONe1@$??AMUC=)Gm;CI_*kV$(TFBDyfW=d{1R`tmlX-jAIk_OzPnQJIltrtzJ2Bu)m_JK$J@yw>LO};*Gq8}Wln=^rx{+GqNyvTx3S9N&0~fEwbDqb{Wi{mgm#9`4)Sk`DsT>x-N&@cU=XS?qM)DF#Edk@kJtz@=$_!OuIU_@iF?F}`vrzt+~vTjnS_pKF-QNd`^_mUY#v;z)#?qR{3#`DT=SL7Um{^9c^@)Vcd)uf-Zb1o`UqT*fg%3rDWK+Q?UTqDJaIX|^E}`(ACh%lh($_rNtW(Bo(dNp%dHsjY<q95Of{5+z*Gk=L7pi@%hXb1zT>zU(BWP2F<T?}>WIVw!yF%BdO(%=@@vOMSmlpg^K96$^zLELfsnL7SS-mra6}~V+fA3yC7rm_a#ry!${e|nsgkM=QY-DV&W#wwsLo)tIx7N3^|ei*P|N|JMs^O{pWa!ns#-)lwHFCPZ9|$dM}!)bBBy4nDAQ0T9w_K<7+n%_vC3?<{_y26r*Hzfg^D&j%^{%Q<F94pff$`^Ry5nI8JfTf3^zDE*+%g~A)FbRtHJoID6*DE_eUxljG$We=?$l(I-Y3$A|BKDtqrC=Y!F@6n5cW;tK_<9h}4~{LJ-Mtwe<p5A$5Ikij2#w)Di3_pG+|{oG!LVkXFDT6bfCmrpoTesn1)xw1%geU~NGWO{^#YT__bWV(>E*Rx^TXDlE4X;55zfRB<{HD`t(@r%^_KMCsIWf+{^hI0wO^{fUIV@TxH`P)}9bp2(3=kN)I?(>qezC;B8;$^JaTlYq;L`&h9O0v);dnL%q+eqqmww9B9M@n%F`RRL=$&3eg*jtJsVQEg*w#?O8RgStpXFjUg|c-=-Wv|gk+s;d4YtgC{l!UV4hbJ*`FT^Qsz6n|LG;;(&3x0`v_-d!=gv2LW_p1Iwmxa?#-XLu84LPp`t^Cp@2H7f>7+Z*B?FiYn&#dKY@y@{jkO*!hN^GyVFH?pW3WAl{rjW}t1)X^uV|BVn<-u!E#iEQ~vcgX7c)%*q#C2W^k_NSP7p|IG1T^f@)->hTJ$IbKRqI);<?ge4^6XoN7<C8G-Oa=E{NP37In(Gl?cZuXaBk47^#CuhYnu`^q+0e5v(4SR|Ixi)fk*b%Y!8gbD=}FN@t1x{Xo-7)zYSBm)qqE-WJZ5Z@@o}4UQZb?g1*4Ey#j#Ez%4vi?UoraB<)UAAf5{I&<52bSP*3U}-S9&*1jOs|b63rkY;|TAh7#6?gQ&bd$w9$MRgcC72MlD%n>2T(MiOnLldj0(^nuE8%E%bN8fyS4;SEdH$u%Zzi97aFkZPumE?GpOIz{6EdJ`UHeVh0St_)u}xShluk35)ClR43?;N>9Y=Cbo|LD7Z5m9{k8vK~-icEZk@Ny(~8;-ld8WBJIvLNd+WF&&bH<W>JP)s0s?_k0iW8xlQuY=^3B?x_z`?VRG@^>SGsbb5at;~q*1$8z7iStjk#^@*%H?QWDRAU#_hF!$a`%?EcR>>tF2!kc^1jt)T>&9eO+NYU=Dym_bV6!wr1qR9O%>uzN}$M?D~$~zc5VK}fDmk0p9b@9zh>XYk_SfA{!)F=No?|!hXPyW)fKAA7oC*LmXlM~%Dk?0A8^40oe{$TY<K8hc%J~=0P=2?C6N32h7#`@%p;+d8u%7#a=@m8fIdrK`#t5Q;J5mm}gRZ8Rz&k#M+lU2%eu}YafWQj8V{wY!ZdH2gP!PzCIZzF!f4E#kT1BFTcy*CHKpVS1Nz8j!DkZ!rkmBITNkD4M1!j&_BN&^iWORhRtQf8XO$rOJR(JQD2U=_W`Al;U|-{A>3R4JOwJ!ENODoXZ3owGB1lu-e;-%4f6jems_STq&}VLtrEUOp=K_{hHY3bPdq`QnbJ$;iTTNxjLV)l!njso2Bhu4B4E#2`Oaem#~@8z%zz56c^<86IsNiB^{M`Hn#o@N$GN*#!p*%8G{v#4L|G9&%EvySBe!%=|K`RbLUSCG7LmWltADk<=KysJZGZfVJfZ6R+@?l}Ot_z^NRsn<Z=wRYLgwiPLtRsVwL^Am(q(rOKOqyfSzR01=(t2&O=chkUp*tqzs!CYf~CRL`R-Wxf^6fUWb`_$iB_H0nqma-miug&vTou%RijMp;su+L~@U6TbAOVz`iF6^k+xYv)^2$z)DUz<974*5m-HvJ1Zpd2?5(#g(tq>2f&}LZ4}|TAhXW&NgnnJf9ePW{A+@eD`+b>smLwq{zz9v!@GMI?IfLd4%PUtOoH{Kd||1bE&h^)hztHvvSQAWM?G6YzPkH-!Al(xYP+5X!OmK%p1ty*jn0c3n-u_p4}8bhX_wOcjwiPj@@a(9ViY*c<E?ObY?Y6R217MHQ`RPgj@Jf8(&V_;~>+_a8`=mcT1^}i%Ctq-UeTNT9J`IcVR(%B*A1{6YuJp_#N>{)0gGWf5sUeVlOd0U?q|yf1UQV<V`DMxRq?b`>wM9Dpy-V_|M)M6f|4bKmjY@RsCUFgY-elWQN*4smU}`XL4|~4hCuhj!tzd_uK)HSsfJcSyiP1)~~?z)YrX59lw^y-rM`~A}t9+&!Mq%9%jh*wyxO+y$N$Fh`!@jr~6uk25c5rsh@uxRvnygO^bB2IQ>2E|J|>A04wiNQ0<1bl9?lB(_HoeLZ53S$m|wIm^;ZIcj9IU6~hN+L*9Hfdt%*P9BtHSb~Bm`9>tc&jnT$V4@rpY68Lt`G)Y#(y|&@LV<}`n@ZRpxeo4E~6BygDx=C)eTWQILKY2K|1SmpgfH_9z(|6rpbid=9A6k_HE@>-gwd;<QtIBd^EGz@Xly^qd10rkV(I!3^icIWWGgBs&QoZANDA^GsG_88nj{{ku^-<4-x0Iaq6>kp@>%!$cGDQgoGs-~vCPfEceYr3j(kSX*Ird$xX?q*GWdsaDphki|9MzNg@v_w;xr3M-Z?NViW(k7w0E5c}N-ZFIod6V>_9b~2jKcS%w)8tpw3^-;c{(B+^-?_EMksHAyh_ZjpsgzGZv}^JB$yyznqR4=)p0n}dtHR+w4oB5Fq4CIw#7t~ZB(y=9Hrj>%!}#(<#;w&pYY_}plb<bS=tbCx&qFBph|N(V1*cDxpRkyzGGd#KCF>}E$5PmCwpMRqq=m7yKnjWV5TvOxP2K?JBzs4H{c$2IAgs2%#}RE<{O&~xJ}>(H6w=c+gTmEzoG7<wK8x>Wk7#ROlXx0p)wNsBg(&x88?GJlJ0DA;tedzBxrO8Ogtt=i4(trS9)hy13w7r94yzxW;>AxS!bRvF#q)j4qAw&{sYxRkZ@oi82tG*0=v@J+X$@h5@vX%jgSn`H)|tIAx)=vMp}~=xmz2-nB1)5#$_9!jn)jyqjVZabUDbQkctt=`b@#<Pv1uPm6tyJ_rQ$C1C{a0h`DinOY+h!04;a-lh<67Cdjc83G`-$E$Vh1S2ra|z|s|&wDbYwr$Y+&c?=j>4)4RwpwvF*CLB6<Xjm!b6V=iz=D5WaI<)Y(&l`7KIi=EA`HmK2^ej$lx8=5PSJLH<T_2i_DWjE7wJiUxb^wKdC`VOvP7smRS_U>7r;aCkQ_Bna%P+l(W#amL6iMfmyR*fx)eLq-v^8kTs`J=D?Dd`(tT{5k;MB3MmA-gH5OU8`-yE%nU-y8yv7ylUp2Fxi&T3V<D%(3o)e(PcSoT<3v78gT+)3_P_$?nlx@P2~Nh}zi#kL|P-TXD<4Jvj?tj0jIx6z-^c>lmcgfqcTq053Pq#^O*wdMWT9n*b6SUli{QH1j`<XiV;Lw4#dC08hXI2@!ag9}q`$zzJUy;FrRHSutZ>x8OGf{`xPXBR(b+c>SURz%`-z~O7+7l$AhI-xwWsQR1$ThSd=t4i_Pw?<hW+5Pq}#&4C`?7{FJ+Z69%Xr1ygcB)i+kU4JeFcoxv>k~TVd=%FwT0YHeasUV!EuR_}o;1jL*79ld?v_t!X8Dw^Sw4m9eowCYJylTnvzAZN%L3+QRb6n(0+I|>*f;O&e<M<8wS2PmBz>y&<Zpgd7DKhexnQ$5bHuT>bT(g{fxb9p{8(FhW{uM~Rm)?v*^?L9NMxWvj-<&~gsthiGFg`zljPTl1`5?6fClSc)_S7?yKpE_9`so%CzaCsAr1CYSeMgmWk|+mLloiL#F?e-5AkGpdwOL^fkHgY6Js@CK_iu#Ls9&ec4n@VTPx!1URK2UwC;KzL@8h_4`6IwQ3@y%em|Q-gUCgrOn_IH7hK&NYyDElZE2F%z)1#`#<3X4HfKi}d?D&uhR|80T-6LXtNO7LxRrL1dUMEasQNYq%xEy>Nzwt8p_LT?J!kO7RbdASgmI3`%Q=n~u(2tNIE5X`b=XLpe{Whk+bY1<8yFT+-}6xrls?Rq0^;9$L8ZF}2#193JkpCtJT(sw8bAp(kz>@XULwLb3EXQuPLI5z2PCmQiFD;5`R<;3AlT#Q)r&U>H&oh#;&cQHYPiu0`p6icSj{qq(2;M*ICOFE(#@Mt;uIL*l!JU=FkJ4%Ee3t}=r^WAUV@iMJWGs^NGuyl+yg>VF5G|i@n%t_-mGh_laJ4Wd*-vKxM0yx%_A2~D(+q9YRt6cf>9eG&a@FioT`!n_td5V(1oB2$k1eNQ0gbr@kYIvMnv7yDb&lKj9KM;3JqsdXtNaFZYDuWbh|N&HgyVR^qWjijx%DiUBR;0w6+}?p?qMxS??*Nhx%p<W<bk0HL#2nHU?QOhkE-0$?bfJ6qY1SJCRFq(Qy&}XB$vGg0gRFKy^g7%=9*<W!cBmF{NcWlNPZ0CI^%)%d;`nQTgcVn5xS%;JJRLgtJ(dn+u-l6CC}ikyRJxJ1y^JY_ICD5+p!|=@NpELYQ(WE!X7Kk@(Ejcoj@(!_(-h41{qgZC*T-KJl9T&%Be7TO+B8L*zRZ-$f(0cI}APapkWHyn9|q8R2E-9h9d454YdKGo#67#gr*|(e$)%qYY~t%Mc%>DqORYf7_&M(NL$Ng$*C1D%yt160O&?4~`TiAX=9oV?vlLB?)ln$}%}bw&UvlJu0`7t>DHhEZ0;MiG85l1LY~20mGujouUp8{=|MZs{bV?_p}v2zm6m=T2du?dz8=OWWi>J6<qnX#R~QFfo5|5y?e2ocUi;p9RciR{d|M6b$6yhm>H0l3)Rt62!nc%(r02wRQ0&UpEn3pxtNp^i3B7h>!HUqiDFYQ9HMd5i0}jdv@(5dauiY(ZXP8?eQMjPCs_Xl8}6jg=(YEAnE+E@O;vDE2vXsUt7N$hEGI!gTG8jZ*1+t*!l-Fj-!!^Ns7EzB*{V&TzPyzoqRnN2<>-10@HMC>HR9s6SsvX)3`>BRDA(^wt|}Us)To~Jw!#%cV~V>{@wT)mnKO%$1(9mPe22!5Vp0=bRaL0e1Uo?^UW{Ko&@C5H;IF)VF6c&6$AcUl7jr?gi*VHIAYPL@Hr!U40x(B_!;h!YHys{n*(Y||-YOAZzKASFBs}ngZyK|3#7Cf1hDQxqJ$00ut*qf>p9q~A=q`i7h)2D(ha5JKZQ?_|$7csV+xY7~XwpHkaPK+4@Il2RO)EkC3dNi<<CN#$KD)w2p&Kx^Z#Y9W|90yPHyzoFGgB;kaq|A_ukZKk>-GGme|^2euUGi>3cvpPdWGNT*YII}4e#;s{4RgZ-^gKq-CsXa2=O{lzoB2l>0k4Q`=b1MVc+Gm>B(Q;>9apR7dH5>^=tS*zvdVJ3IMaWs)~M{AC-O`|LWi2*Trl9qSru>YFGB+>7P!;7Jc^ouPN0R%}e%He}>CHg9Ip}pA~xQ`)RbW_0CVP=bv3DkWPLF&e$M=$TiiX1-%OB1_vQ^txE}TUhH~OXcMIg(HEpdrS)KfiH?XJXriXkd`_LLD-H1_ETb4$e)cA*rVw=1zd$GwwLW9Dn=@)vn%=4ZC>zuJQ1@@!2Lo14@A%VqPX2oBR~5Om&#QZ@_h^0=(E!GaFACjsi7<LU=e6qV3>M_A=HsP*c2eUzi$fCg=h9i!L$YIz-i&x6Ytf-P(Jg;k*>OBaZwelMaSV_*s&XvXw(%z$7@vN=&3Mb|>FCJ8Nv+58>}@iUje4{idjjd2gWqKL7f|-AN-(LqH6>s5gm`_<e@1U!q=xz6uZy37TiS_C@9<}pu{nMJ=}*~DSBY1rf9>kAg~f~W&xVU1f9{M@w0V2}rt|LntS@|TxN^+b4|V>*r>;hD*DkXDwAeVE9=!LL?%mUW?G|HT{$l)Thh4ARc=gDm_vioo^5QQ(r2%>A9X~s&(=qwnd5yPtc?ZpO`r-$#4)xh7+dJv<HWxp2d8Ebpb>OYkLhvqEW_;6ZgGXs2e@WiQkIUalv+;lXTHuNd5txg;@O%-X2EU*yLc7u2jV6d%7e)U;FFg5N{yZwD(9sr5qLxAmn%m9dgN%AYDLt|EqBe9<tUQAjnN~63>>^!JmKrdi)+Dvi32Fm6!C`ENix8252=}Q*8BxklQml^ZJ%;LJPFXxZVl8}n4r@_O&JD5FQ>QnZyPVfj(V9~m)h7G`aY6NHjMCa8XQxECwVsbD+vH|l0(>QcqjhsdPGwU2`F#XhOMeE6DnD|Mk8rZUP<o8}$Ev9E0Qo?O;T+MM&6UmWD=`niiF*^ghqw(@LL@#QP(*p>(9$Z5!Xk0pY-@%$F_;j6#!g2HL!gGSykxNb9g!O_>jrK;nSL2rFI*${bX79__Sw%wZI=$;2j&L-P^krU>sHYpX=b4uqx`A6cXR_a&&3s&|Bewnc0g{Ci2Z>+o!nSiO3<V;aHN&tdL!nvj*!z_eh^j|pE{INKbo<bCPbli{J;NEL9SJM=|%9Y7icdTn#QbaPM|cDX+_8KRI0lQFLA<3Q06drEALfkme^KJ6D?peu;pdHRKiQNh7~m+`YLX*#AaE~c$_TqHTX=!elJr@Q;Cc=^BYKu`16J`8?@I$lQyo5mz4;;#z>*l>wW~$5YlSmt{$8Kk$C)*s8)Xh#@b@h+8L0?#sAZWOauf1qvZ*7e;5(^3rDfoT7UntKEn!w{T%5(w~1c<C$oXc=ac5_6BA56j>4^`i@FU5Gcq6zj8lL_8>+Qbs;aux7LmMGM^kn#VXI&)xy<_?s_FEY<5EJ{9m)J_<$~bqY9UkWWG3rI1%ST^<Y3UQA06d5kUB4Znz_Jt^&2_de9a;3KiXiFg~|0J2#|0wWfslsMVqRwr!+sz1&x#Mn2V1d!WNGRjO}UD21T&LD99lF+W-#l2BI_K$pasBL&2r;2=Ymy>Ov-`wpzajKYQUcDy!sh0%1Z=-g3cOtT=wT;=J%rxAQ;!uiua=-R0P-ulDDntYBuWq9Zfx|60Sgyx(i&k}dBIZP+!ZP(zxa%kR390G3naz#t`e3x&EcrvmUs4~8~$X-Nf$OCA6c`__*OrJsRVo9fN18rFUS9BOT~iSi|cfMJ|82fWk8iaD$>Xu-3}b?6B=r1u<fJ5c&gxGx;`hBl<!44&XNhqde(U5FK+gz1typCYLy+#0>vV)PmFQNa|^thAH=DDjjF|H~&4P~0}}wt}CFW%uV|*#r|_lTO62vavZ^!868VOW*ftRGMgql(!i7$GL(w<g*2RwLFUhlX1W0nf`oK24AxR8<_rb=s$y5R~=~y^~juy*fK37evJDmLQL<dG48JxK%tc{F$QculN+HQsFN+r;RG9d7Wb>gv-_lRfBdyEatJ^7GAr0~@%E9dvcF;lTmG6yX81)bSPJLO-C*Nr1#4_GnU4lT<5R*NMmHR8yXqcjR<N$CiAOt38W$qc;m-Gy_J5`u?9SN|7HKt`TGQY3n$(W+fz{07_Tp?;L1NsfvgyJH*0ekE)SOts?s<o)XSXnc{U2SqC{<xA>^Vk1Na(+~IWAZCn6QM?@9A*RXr&9REBFhG-Kl-$3My=Uxa3_qTv*`tOy^5Z)yS@oC5L9F8nYtz0rx)x=$PEJuC+@PJ&Ye2eRa|F)y+>fnC6Ql-p<Hvd}hy9u`ttIO;j(q4=@z#6;IXZ|IT7AXkRrH5UZ0#S+qpLz#I{8j2qpJ1EKt34FNE$1=rMniB7#)X?DOp`jmkAk1cRT>EExVakV?sxbjuws{K$JS1^SVqF#CHBn6R_#$FV-O2Jh4y@{@z@!J#(jf&FLc)6r*wVO*@@$44FNDjI)QRzjQ>C+CY^ml5G%fIkkei~&RKyge?ZHdJs5Zunk7iZ1TE{0gS`(0gq*0O35$UIc{1y*OQpzEtzKQ9Bhii<IrmZrV>Ppu$KXI4Z-hp4KpS#~xWGkCLkkc?jKo<*xb_R%bEqB#r(%i^jwyuFAL9>m@{situT5`>{uFUXI1H>=dKS_deDqu>^?_ZaD29qB1eU*xUCVt9KI3Vq!<PNDIl&S#g_A_B;H#+lW`qHvz7*X)=GM|pQ58A-J^n<ySU*ojZ32YwWN^9vt_>a;PwP~BFtarRwu5~<D^zUBs2k;o^?{dGY%I|zxk#L5kE<~Svi7{z3{Jq>9~7)h2?P;GH`)72lWCo*1PvISVvSn}_2Bly&2wx<1}&)~x%w~;7mNA)mW*pK%d|2MDb|Br?Kf4!=&oQhYp^y{y$SNP-q`g$o|LI1Cy|JPq%LI1Cy|3AnPuYbk;e<Ixfhx_?qu>LOj5%G`W&9wbF;@`Web|rX?-#N2pB;G(c>@0zKnQkT`oj8?Y0jBsnizh)Qozcs#(x)zZ6aF4i*CP#J;s8kXwZhW{Tc2|PoOc&!0BM2vpX2Y%aAp1udeF0tCn2S}!4f-u@>h5AYn*>q1uJ`hMj_z13ezdzHSbO&^4I|POG3i<UG~9XJD*VgqB^ivhutJ1sFEoUPZWzYRQ)MEU^)xdt-3Sng)Y>RC!k}t)5-PtYbo^P_)i%EOL_on_u_J-af3@++UdJ9=D_Toi4ZcU3iuJlH{BZB(p|m9iw(x>?<(^_-(}xoUmZtOdXi&sYkr~;{meLSKW7oRioYL0$s+*z3I2dP!@iGL`E%U7i_2eocLM!C!Ofrkny&w~es+3sjiTUZhkb!35Mpx$2p*q2m+%Y+VEpTaL!G@i-|XZxFA@n(FU9<@^HYHM3l||>z`nZ~c7Gfm=QMzmcTUmpVS>(I;~R|cxU=uQcH>T&17|1Y$2)tntCMq&PwjbPBLsI&9;grg<zqg-+9%|PlS|>vJ-nKuEHB!HE9Ni1bKb95v^Xvk3{L9q|EdWWy>Y{rPg*KI5)1H|%RB3n1vVj&6GIIYwvuHb-)0)yuYpiJ#4yn8FtWQ9J2vx=1gsHJI6#%vtjN)RT)DV1M829XIrt9hlW2Etvq$$6zUqWuaNa|>#0$CM#RQ6m>bi+*H^k(EAJ$Z)T?<g)1?6X(#9F;s(0rUQ@Qbmfnx||&%10XY0cY0LvtCiKAgH#2`0IM!`(aP0A(XT62thN|Qq?&V=A#KhI{7#_nJx&?+0?IyquVtun(bVz-gR(hsl~2WUp}+eZYgeF?|!+1?LXmu+c%xh--BEfP#rB7hg&S>bR9_t>ZHXLCT?h#YL$gtIDqO1j%5ad*Ae20`#SL@x4I!rOrCg0`6yUCO&d~|S7ZdPszNJli11=yqYz&);MUQq&NfK*XvnY7RCnbJnwEQjmTK5~IB}H6XfGJ5ONSNO{yBRHk@K$|1+eo`%9%md@7e5wJTVr0X9ru5n^^7}CEt!tPM7%xh?=!P#pI5b-3g=?4Ima}8$~s+nEvQX?MZ)DLjUE@E<VU<hwh)Z)#^EzGXVxJ+&KU;xTA=EdmqL5*h2X}28zZW`0Jyr{&*80y>G5XK(h_-HH~m8p|I@Fa@A-b%A4@DjrY~rD450MPd(x*1_o*EJ%-?hdr0?AQnM@JcJ7evl<WJsM3;Ax^AwN<$0i>^-0D9&aY42O6T)6S?(Z=_^b;e5KP6))UtLbjAW8H-C!agNrwA#SMHr~Ej^*~82NK^r=$7j$GS7=7XLLJLHKkpSm#li{d4T$&9l-Y~h=YQiNa-@~VTrdgRxCQo0N?b`OH48hz?@>FkbW-&BPSDbQxrt6?hv^p9%()pL8OKCp}M(Vd~IJjB7yvpurZ`<4sm_&%V5!;5>ub%4r2VtMv&KH2*Aw7r+Pop&~0FEFT}ig1pf;YnDon+8BU#p^iI&D>vw>T!g-3I(bdaAqiKd1Z5K}49gSKSSkVlvT`UwJeqF(bGA9%Uk3@u1a3~KOCkfnpKLdVx0=WVN11t7Zz)x>rfHUAH(Dj2sKK%&!ltg(GZqM!Il2urMg}9BhOCsP{_+#DPnd)@<FJBC<nxXryfvfgU(lVHak=yeg;HneB@aGK#bA{)2@iM+j4!psiL9BuS)FqR^SYZLQDp$6b4JOCYxtU-#td;cU%}g-yrg^#U2AS-bnP4_>h*?(V8P*Eec*;VL_qm0-xTC(nnda>kTyOZaK&#()XI$?9>gh%1Ps~?wy({5*346)zIcRU0uGey4^+J^s;45^mZ+PoE(pKuo;v`Zop48}pJvA&+XXsw8x)tDSbcYUiGL41@Q1Qg}n>v)rlR<zl@H$3WpotUic)dRwBi=7zzU3zGB4WZa+zyyV2t<YDke_XwARJy!Z8ks#t03M?n_-%eKty-TrL8=u|Hub67M#!X^^S?8n3LI(n780$8^9aYLE1NShVOu^WS}^34JaFAJn-OfwG`kL+;$-DtHUF=1w)EZU2Gs#dlWl%J-z^J;xZk=Ob`R0-1ahv)@3H|BWC}y|1x$q;VvU&&7!I~$syw#%lJ5!Z%Jidr8(L^{sFF;2Kq+cULW9^5d+A|+jz|aEfq$rI#GBW=vbfx^h_Me<;*rnKe+yKIRf5q6=`ek66mX;M8AoqEbA4=Zbq!%t$<$b214^%*R0DW<N)Pq(vlJWoslHmW5=fs)yBF&wFDCWr27*umB;O>PWE>wlC61@64&jD^3Fu9=B<~Yb<bZLAm6aMbaXdwA`{0*5!*5cbgrd=PfsCgDA)#$G$w*HBgEX$!zU%QYnb1a`J;*YUKBf<fwI~BEEKX6b#*(uLk|gjOPg$)riZyjhD5L9#;}ekdq_B19CkygY<|4%ne5e;t{8BL=6;}=TS8rJR*t8|uejwe&N9A*nQ`=wgbm<l^jM|mT}Ivk`Cm+Sdu5ooegiEH^KA){f!inZB;d}_U+k!~#qtHXRcncC@5(bo+Omg~b=gJZsyU|;?6Ky*!i=A2>)1}jPU0(X6reHKEl2fWfiGs*M|yCSZ+yf%eR+V6WC}fCSG%LRgv8%_nN7-*%#-JW+U~;!wR8jEl5`r>rmI0Mp1eJ65)|6TE1_+3F|_p-q_72q6osqL3j^GFbbBGRO=D==pT@PV@}L^mwkq`9m~#R{+tauf6u^J@9gOO}?fSi!nck2&fgZ80mPMg~Z9QU&+<;l3`doP;(gqfP<?{_8){U8($|RJAbnqFDvGJ=RJhq(5o3P&iOg?ZukD94dIPCaTM8D^yg`mK#BP-c=tk?}S2|Vt?npy*QFqCl{WpYR4wFrnP{@~XoJc;FuHqJj{jFjU<zyfy%KF?zHM<&>dDDAgj>J!8O>#3DX%}_bbbgU}OY%;oh)guEM;%lGfPlXX5QC1_%x2|IK8E6?KGdLr2$J5B2Y@N0`3@1w&l#GDbok`@Z@mbBWT$wMU#=0W#SlRoXhCZ(4+*1X$tda}#Dz+J|;*Qpw)a#&#Sc?hbhTXsxien-~(*akQ^s;>!tZ>*3$2l=)v&i9KvC=zw=HS-d$e!n78uusN@A~FvK-I+bwkA5fT)i9mF@R~3WK`gP0_MN#gA28~nD%8-lTKR7tArXKVpME@xK}|{i6DI!wwSQnAa?{hF_-(_B-v;0Hy9@6{eirF*mED%<HP)-63V?676iJfV}Yey4Vd79*rr~3QW8eQ`?xVa`#DRBs{=y41fY8feJ#J;@c_!|JKUoRv!y{%+4HLU(_j=FMNtvKnswkzs#7$L9=J{KHI{4qTE69f_%Wf+p4UT46v1SL&Re2sgxHKGwInmk{V&RXkOCMqh-Q(=FUUy^jkvl+!VC|9PMUnFDr7`S9(V?U7(H|#v{tV1x9P!~bZ?nXx2*BYSwr@NGEmMm5{c@XHdxtq`AOc=b?J+XK13fom;Tf4cQAI=A}zt~9DWE{^X-w2B~*L3dt?PO$>A0A*NXMkxaTau8sFh)?i@RsDGmET`ee}4vO<6vwk;j7ll#doV2FtyBeOHqRdMmQ9pcu3V+a1N-aV>IwUUcD#V3He2n{FgGMV3{vWUgNy3dBaIf*v$g>Shr26IQ356q<jvsJ`9;I-mSW3gzgkuT>I1d34^iSv*t?l2jUv*(~tL;gzU$f1Gk^h6|mFKVW>Q~w8%L=Rn`@~K03*<3*W>q--W_^IPWz*6SMif45$kid(Z%?N#<FB3SaHY3omI`d{+o)M}j308-^oD?WTBBPp~^Fn7lH0V-rUcjLHhNlLKTTtTSg^rKwPdh>U-a9)!UW??)JKNJ@TO3Uv{gttKsTk3<HY!IO^%Amd{j8Xqsq@AeXXgG`qPj5E+hqNi%V0$X#;WujgX>rexSgBXn4v`jXiH;8=@`*1M{$@LK+*}cZ#}zyNJLkR?AB%j=}g&10)v6P*yyZ`%lFwJfElz<v*pUJmA<eKyDryZ?Jednqp6nS)({Ds>ho*U2MO7q#dd$~BlDlP&CBZZFS)VLRq0PD&{U6U83LHrktY$F_c?~^bZC!WT8Wf(|K;^bMl|M^?xaeO8X%5Vx!Ou|irk*cogd5fsZJ%88lC3UXvFc@)d?^9?zAT}%^-I#n?W|8b_V&?spb0UhVOA4Sz3!mZdrZUCN4pHI-n#P)Gfv8#*WQ4_(!%`@#anidD^ribLPf(EV_}h`zQ<}tluS{f<bzOUV^`Owy+~+LGzUDTCQ0%w`NH1kpLfTw^+&dicoMr`Kw?Ame1o~Sv$f#J3QW;Ov@liS%z9ffCOvr?y1v(fa$>m70Oo#&e3zrUU)q^u*aSiK<Bl9?l=TwjT>2i#5+4atPKkDxsqn_`j5S|Sn=TUEukehu786lgSLq--a83w>JYjkiVVaQQVo(__QRcEi+DT+^3BV%pQ{u}gncZrlK4Ly=$gYZZK#TfX)4-UP$sKeEt}ZST1nEKgb49P`y*yE`0AFieU!DV>H=JK?~IhqE;pLnImZ4Vx-_Fws-WaYeB){#3CTSh@qZZhee5mdpP$+H36|2=%jS8N+cey!q2b&}afcE!D_>1-N+9YEy8xw;2i_;u8R$=2CZjU5-Rr>1X15F~2|2-L>oO|Jr<6Idpb-H@QH5)L#Eo4O%Yrkej8%IF^W8+m3WZC31NypKA0s8O&}}HkzbeW1jzzIYoOiQxij4*AT+3hZZ$0Z@ID|B`DX-)HzC^89mAefJ^W_M8JWg@wkoZS>kOpu6K(i+$J~&}$DHupu)3S8IxgK*CC1Yp-xMO&Zf*<|;T7kO)J@96qifY@q^hHp&fkFTjkjwlaoGycw5eXQw5?D?}5j}g~D=Mm_%4AB4WAj9D7rY@?xv!*Dzy<q>yr?`OWhXSIPjwq-e$jF$q{NpumcAcf&}7+J={2$(A3{A;N25VDZ@XZw$3#0>xEqylRFZ!ceF$MRDU~W`<b&v|3!|$CFGT_98dQk_U4d>qfO>-Z?6~vg&l>sDPm>(}Y5Vao8eLCQm1G7GnaeOlvs3W)Guk+@cf#zust~~WPc$@RY~MVuzwxX$xt@TVt7;oj!bi!kYfo55XI&_hyT20Ol(XLnuE>GOJ*>hkxWQarwJbVU<r&p1b4)2&rmW(Sv8pLbZBhmGj(T>XA^|Bc%&QoxQiR<c_KZxoVUmKBq3>jWKI{F4NoNCQiOGl)2y+lkqCg!+7<#u*c&NG=(s@WGl%Xh!^_h`&5^Ru2;38B7NK?SDq;pi_4}Q|HH(P4&7E%}^EOjZYk>{EfVwmvQD0;?%^6bQ$8lty@)sZN=5~>8sXcobV9@1*K3(dKIFt5H8Fyf^3A%Y6)?Mo31!%Uf#M3A2;g*QK9^!67@C^7sT7pVs>33rk;=40dt)f^*>9zk2aCFYgmx;$7V#85^62n`|!wioo*NUUvZO&|?7&6p?zwbJLN_h@<hmPi=sdQq7O`FzA2hljYs-RK!qH4Gws4~OWLq_sIQA+yL*hmCM4W%VLUH!O!XJ4w!Xs&aX?%Ts76m76)%601X=uv0X|sj=#<!XHyh?okVs*_Km#+W;sH*q|y0Trlu|Jy*5HnFgOjiXx0_6k@olsYbzv$RtVx7H1pGHl*=i1Fi8UlA~1i`kNo4_oDve*YCZcKfCC?_=~+4h_~9RwCKH1rEoK;7P~g1a}wsg7eW+9*<@7*J9Z(h1Jj}X5^DP;nnH5$8<R#m$XC39B`_|0izrJ%h@L4-s$G|Ksp}Heby?Mx3%NGxx`btB?*EmS_SDZ%@VR1RP9g9s#5EHHzC%@P#Rnssww+^+;`17~o-JXdLO5U`X4gl$e-oTQ(`G#eUQZOCAEXL6`-T8{Znn~9QIIH<Dtm)L`phUPo$N=zHQiy=2wXTcSRc#aC@J7t+iRaXUv^Qq*?plU&}%2cH`!|i9p&`5Yp<)MN}(o^m=US>8Iii3T3j4YthfRG^F0fP+vxjFl5FTsC)RvAB(tus!ua~99I@>3KKkKS^fgv({~z}<sW3dH71)z@l3;ocBq@&~E2>$vQm$VPlPGl`uU25n94gkN@f@q>R&pbtEld?G845@~H<>qeSC>sC%mVLc(ezSito%kq5cid;h_2$4@^r0}1tVqL?Q7`4-5L@uvRQz_ofoQ#nWe=b7CtHpP@A<nAyj#E4uL^3UA1u(NP4wsLUBhsVM2mklSw;s<^70Ys1b)WhxvYM+F+AjI0sZ;OU7AhTMfFgl$S1Z1R@JFg0dE;{#gtq8}NLtzDg3)5G{bt>~q@Pxe!gvcaAt^^)aJ~zwSmI&>y@Q9eizhnh$(3I+oQ(3NUMtYJB#~MJicDj+RG*?o*ivdq1h*AxhXptH4Gx0#QjaPa*rv3n0jA9y_P_C}Erp^jNd$s1p{(ibg+zJW=jNOTUv5Ky>W{AI5DdDQ(xQb%H09V>}F1{~s%3SH1y%ZKmO@{y$f-a)q{N>v^tX;;oiPFs;x!_3RUA_;=C}O{D+Ou>ccnGlLQgQM$ysl4I#n<*B35a~Zft8-|Rh$~{2*pfQ+j48{^c13To6U-B`A-aqAj7d6?2;|_!W1_<~JF@6rZ4ck6@ED$u>Nso7^f3U}v)(KUWfNCWRZ$}gxP&6b2psh0E<#P5zxKW*#mA{gJy{TZQa(6l=dIsqyjTYfxazhvHctawL4@6x-<bMz~L{}FGI5@l@>h&PoSb?DoxLek^5(@r%b~I%`Csdr!56E^U#`%Da*_y|jl>Ei5YBUMnM)oN&f=Y;=4rRT=*9}rR7eR#bu+4yK`=POnPe>HwwUl4~(+}BYc$NszPWB7WvjDhygyr*mCb4SG1?AjbhYL1u998`PvaOIVfd4yZy`zizs!<iF>d!$HX&;B@Bv!N00z0iK90*JfO<xrRIXE9xCKp=?o2A5RM^NSMHO<~-6QTLEO@xP+i>rEytA?7|V5&)%L#OjXPc!rU2nHN>-dg&TEf3uzo*ZQ!WpW9pqNKoh)Xx@<G*?h<oS`5TKt<Jh6q0BqKNH!sBHMgOPIhL*h{=bcDx%KxPXSrxP>pq=@vLf%Y*26Zj@I>T6<F1Z(p(NTjz>jMh60vhD(h6;4mJ$NT1>2@)CE5{SPexnRP+`=^;%i|Lf+KMSjzb7F$B37%AO>6N!A9#jxyRB6-yb6wd8rWl{o5aiXZ1!csw>5Yw4Yv6JgUdg<TC-|B-cTug{~fZo1Un$9#<b=|wN@XAx(K^_Xtl(8AA$IZk@yvVz6=#w&?K4oKi$X6ZdV%=&K`IKJ|Du_R=jx<`O6ux<r4;ux9_+Wx3sg?i|$qjD&%Rb1U7Q61`j03^A=094K>P}xym+5=d#<;Qo`DYQ&;WewF$*0cqytqnHljN-{4dyjz2o2IT!wSN3aS%+whqyr1g;}i+xTLTj2x-<jZIQm%Lm*eqToU9(eR%9l&I{eM|A;-Nh)`zm=-wfz4%)sJjpg+llr%Rq0t;)>Jy8_4kMbC`5G;m>*>{$q?=#0@WFOBwB=a_PJcf?NzvOIe8**Z1K6OVw}K8-V=c{Afs;;JR{!M(tw^q2beOcem!m@T!#r(J6Q@~i&wt5WZ)j_m8NuUGi>3cp_AS0UtAA>>yf<R826%)e?OziJ`BY9asFYaze<CpA#d-%RyI^YImt{rrRW?_3Kx%(Rf3xfZf`tlm&pSq)B{i2+JuG^=UJ9!EArrFk4C!CDPVseUa)cH^1y?z!4=u0o{VFExf2|D5UgVmO6v(o{ZI#=WR>{0_3mNm{cD&Eu0ZLIG*Gcot_zKG!YI1k-P-z9I}O<ER0Aa!KdE);{9=utUXexJjjWel?cb#w?*P4){#TxJv&%C2Z^s=8a=c*N%2lHTD-bnCTh&`9*uFnDJ6i`ii8nK6Opc*c6LN_%jl}PRft}<os4&pD7&AbW$%$w7y)}SdaNj<bGfBSNG(vFWU1JL0>-;yPXdEx*qU*o{@k54_*;G4yXHkQn&b;7Vl-D-*76v`?M7Cxq$JDeyuw{(I<XJz1Uw>FLv?C8+YYTPmJ?(b?28{<WVWPo@p4BiLYIjaOuii6eqqcS3La;%cA&yXl)zm6TcA3aC@a^v-2j^at_xMRxeVZFjVMsy3%1j7@UJ`Wa-n2ltvuGy5bo8gku=iWWS<Q3*?4y3>(614aWevDl}%=88I?#Dgjnh>>#FE>^idDgApS)I1w^rmk=bdH}@6IP_-8hgiN8`Eisu%!I13g3X+5T?+TJu<uZ1?sm($yhuyyN`ipQyuW-NwpKH@qt(5(mtrQbk{wS@KKk+;i`wZv#jOd-Gux(z*xFrT_iji|ZRdNGfXj`G!O>9<6B{!gnTyF?$A>P;%gqRyC8X7W$l4fEHIwFf#B5-z)YY-m3jO@M)7HVhrbec|UbYJhd+?H|FwhS*K@b(x)djk89{6_JZnXW-XWksm84>z%j;r;PXaV-VaxqdBU6~;5YM_{lh{1O1$v&#uZKeQX!#U)@PmhVEFkK+%p>{YpJu@|Xx1EzbUt6RSCi0il7hIVb&JM*$7;mm!#as-)=mu(m?+cz)-Pc#H2l6ZQx@QB43Z6CjGH4WO}%Qk>`wOTZx3GI&gM%M|QT3`j&pg0axl#Y-tf<hQ|7jd;Z47zG<9zu%;A2K3$<j^)7Fe@UhK9as}2>q}WNTRCtcD#fx99I$$)KxSA!2{6~AMjdkJ$1@2jzYf&M}}vd$%tOM)n6QlBX@rBXcNx{)pOAv5^-z9M34f5MZmxvY}R9FHo%4g?B7A{5+`Q3zc8#_1DGrki)D4~h<aF=#sCIuxwK3%SL~#(2C{FwyIGNc+PZG0+_)B;H1XQAjh;C}AJYZ>#*!DMzyAXd<@q@7E<NwJ^#bqaQzn@Vz^jA7$XU|~R*(2&ZL=nD?!oQK-`7;W%x;K!%-!SG9`IfHt_OGAlFPexLk^n*1Vb-A*O9vBfb2Ey@E!Lbd@cEyhPwOt8q#tJDUkv^hh@|FUMO@u-%Hw$K}rHAsS!xsmkmr@ZycOEF%B^}V>S<MJcUwMZp&**QHuL$7!QUCgp^SEp<I8^tN`s04!iN@`#s{Pr7GBwUJNXxw`zsieK&@sPLd8x#IAOfci`8_*Fg}W4Y{&W!ZE<g0=3z(bfAc)G3frJ8Y96nQgEryo-6X-MWcAvKS6E`GL%rOXoW>fZoR$$8d=~ofpZ*jBL*5t0*$ng|J3nR9Rz07|C5cH9?{}AHEKH6A7+!;G-?8LUN4Lq*xS!c=xJO<iNocnX(;0nsR+}aj+!z<<`(yXeh7<!)6B3)Emchw+Ll=}x{AFY2Tm4f7Y6{Lp>$!?aJZ3#&S$@g!q{T$2>rCsBlFZFi^fyHDR4PD89pj}B}#WI;0709BueJF){s^^-UyPH%Ex!(@aZ^w+UJH(&#*Yz2x?7e2wKJ{MzwtBW5SNA5y0TXPrXd+xP@Hbg~3Rw7i2;dB{h|RDqtKX5=1(EUOcsd@Ceq<86<Aki7w3?X7mE+IA=NeqE#4tstN=Qk=hojQK{MiG*TJrOyden01dQc0#{Jg2o>u_Hd&TOTmXSXLL8uFCIw-f#Ts%)sc(>NOgR<^4H#=GR+^`LFg3(Lr1%=@Hbcu5m$DG$z$7{^E@OGG9QT$)Ba(PAMj#l{QaI&=%lKoxLZ#&jm9DH%K`T^yx;*9gSf0{sZQ^G+xk&Z!!txYOmM0hdH@rgK%vY#AE@iGFBr9tVc>llKsM+ySd_Y;e^HBpTCh(^vKxh(2&C^iXUSc2|H4vWjIiI3scOzQ1TMn5E5}AGmUxioDgqCe^3tNU8?YKOV*demB97K#Jj%R)bn5BY1HpsjaIkW05OM&|gGfPgHug^*{nj>MeBBq2<kQtcl+=QOk@NCpi>;j`KR($>>%M93TTOBaqwoqZSd4$c9(Jh?(Ay^+FXq5FJwU=Rct0pc1`DM(0q2U%zmNTS8a}@3V)1qkq^Y@(ozU8~0C+*8b6UbBH;LVCbmp&EcuQqst>C(?L81hbHbIMJLW#!1zOvk#T5ueBcla!;ZN;r|_LF{}<b{Gk!bFxKYc*XkUX6A;{2GAM%%6Q0(Tgqe9OI|HP)Q)`JsO*tbEp{#$E#&fK*s`c-34TfT@w$OwS1a9YN`2#+vOAo}ZKkQ3GieTA!zE?{i4<&4Wy<oH9OA4L0M;BHP0eMAb6Go%uLyUBeU#eWqOSM}2G{St54R3al1oQx<%Y<SwQ_CCiJHR-lSfZdH8uGuy#!8_hb;hxRfL>5IgvfDN&=96tnqXdS7@BC3KcZj@M6x$3Izo4GTsKt3?V*_M!RmQf(4DNKnnnGj5Z%NKqR|CUS5Kx(1z<*#9GHmN8T#l`mkjH-q5$t`%wk}+D~P(NC}q~eD=tp8cbfa61^C{QNoKXqa91&<%4DWd?WHW9*bj=nTm<ZLRp^gkQfHuL79P?WZDoSFLmV@1|~?Py`$#v&%d+%6<6tWVis_`<Po4ICDW*jOB?INu}r&}GEt~8l!pqGVV>fAU4wqP#W?DDhGgEkDOR==t^@=zb0x}ID#Vy*tK^FXq0Hqhjv|{>d2Q#}IaJM9RFuruT;jE1V2!#f?p`}-J!2im$6Jb=xyo^$skTB=6Z&Kfc30sh;29A`V<V<sH1)?4ly8Q~5dg$Z(u2nUcl(R}x2Q6~rLOD}ws{Fua=<sD`?h!Ah9)Nsf;v2kzYx;j-o+9-3=|?5Sgm8V5~c-1i`BDhP{Z7mah4(k=18H|C@90>r^n&I$5PLB8DS;-e!KU1&3glX55`qZ9C)d|@7?!s$ZBQdu71@9gLQb*nn6&K!;rn0#X|@`fYJzRU9C5^Z;3L%mTOG4HCG3*Nc#=NR(#kbuaUTCh2WCi74Zf;A0jE@kx~>iP(rV#JT{$Q1sT?<TjaF*C~TRGXBu3_+TJ3(rLI;|0;5wC37U;m?``F38CZAh3btG&nW{MHDk6PPvg492XVB1Y_(B6}SDi>OZ-9=k)(EDmGV8r%kkpWl@43!)rd}1RR7A3p113$s4hgFLq;j|X>s#e|ZD7S)q8m|t5wPLf_#;N~CLv0y()UR}X9&k;A_BDZqq06i7sZqkJ;#Y8gL+Zg1HQhT+E)QIb}o5Nw~y4saLWSLzC>6iph1-wM|CWE2E6r*uwrDf7>ks&b2jAem9Y1%QNqbCv?YvR^i8aZzX{=-7pqh?pUotyN)r7=6z!AQKjy?0HC@Uio2y-~p1G3oW4VNJqZ~)5{!qq1FTYrA#{M&nbSO(z<p}v#NF8mY86cio%<P4+VpURb!!Y65RmR7xBgxnxl9QbIzNX8DP1Qhcb4iW{Qwvi^6{E47Dx6g)LPgg{#!6&}r<qV=G({;BKw<YG7>AZXFFrf0M#Nf*LV_yFZqQ09Rx`id)3G!OE!8-A(|bx#cronI+KAmh_s#;-S7iH61*Yen^{nB*JZoA3sm*wzE)CHqtN54*@mLH{l&nA_h*DkS;||i&InH#YJH#o7rx^#AXxJ7zI)fzML$$r-V%yOn#I%i6GYF&f4rEMv4$Bp}&X(5C<)j-5OC_uFl%3p^Rb-`E9@?FIMytx*JNm@QlTKZR6(e20e}TW_zw<H5I_;^^OM{fLraAdk%0*ti48>+uWQn-+6tg<7?3i%NrOFPSyr#+y)gn%N59MaIc#xZPsf1iP?hSP@h&P~qnCy$ngunvLM#UYaRQ<BD<6>C)!La=R8LWBPxF5?yqf)7-PVKDUFi0jhV?Vn@ahHBJ7MR4DV%gHPVoI+W<<0aUEVmw;4P{>&v$5s0@*jOuV+6zG>KNHxHv_`x$gJtkMn~6~EZx*I{iYpGPW%icG8<L>Gn12a+0x*|81#9clQ8+57{oSxO)~?eT?_pXUwO^PYdYjTpbs21XI3X|nK8{8d@v-a@cJ=Sf6uiK-}!p}o*fs3_L9G6<G0~if6rPmSxaWs{5|uDzh@_NPnJ&7Op~4x99?TMqHgTigz6HNH`3hVlYRqbbTn0pzKgP<mp@)#K2_%Jb|kW6Mp!ZTS$Dj0(aTPD?)8~Y;BEBKPPgXu*&nJIER*u>dMfur+G4L-|J>OVwUtH#@DQmhMSstK>qF{<qDT?jvG=u+g0@qmH;p2pJ(l;z8{R10;$ldNdu5wZz;LZp7(rO7*Cw;^!6s2SGCotBM<qy(2TH0pHZHK#Zir+|Tew0YT~6U(;-Ng|HmoIe!pKkW11WF+S@9wS`>Ra6Vm0q&S4Wm`hRWZWd}U;)NQkE7kjKp!gG5T8%9$)s@Ha`Ww#H$}RAt#CNp_J9ULDTa0Bj8KQ7D;o<HrDz(k5jntjb@bzM5}3Kf=E`_pFkFOnkQc_nuW1*S}$%nvTXp2h8wgrjVabnf98vWFV|;EVQ@WfYWd1mnK`pDk52IC&4l_&0^A>&(zbA;P{@Csj!yORE15qB{S(u6lhh|vrL0qlNL42@lbcg%k5Ye7f@B;Or*RLLd~#UPC$+57F9=fEyCigM2VW$-Hvubfp+lBDkP9Ch)ktnXnSdBAhSqbaf+8RSzTI|8;=6zLE1a~YW<ar4&)21zFN5>Gl*ssC{G#&rg+X2-%cTo2ZoxS3HxyW2y?jjayI0xJn#wlo-j23-8W^5G!GnBr&Y498HG}oNULi?De4(EXWbvR_B&f=m#rV>CwbN|q$3j6>P5p4HFQb;O?{s!d~k66m>Hx|Fmm!pqw*~W<4#dY3M^i5b(>)l?u5QAPjXW0$IOouI7HMV%&~;NS)4r=9l}X;F{^klXT1_%M%VQ6@<JHBPOwQfy?Xvs<ECFUZm8yyTvbU@YfO=XYU^^B{#fPp-}|wt$Z}q*McH&xlvSA4AjnIXOS5iWWy}-^D)cD(snuC*FcxT&n$zV9v{QtV&T6zMuXUn}g_~SQ){2$d4wD7zty7RvhEljxteq<>@BXy=<+5%^;6}fV<rHAjFYs$nruD!Y)pt;V`x1AUP8qk+6!yv^doMtTz9fWu3l{K*BD4wJ*7b~^G=FFGrjQ7%9PRV&Dnx+^#UO^#J)Tm6sDq(E?`^e$^0ATGpe{Y%j10->Zxu5$Hi3*L;n}yESJ~E|7<X8-!>zS`aSU|jUfsF_^t!0Hf2(%C2|xzcVoSQ&a4f^&rfhapZUu~YzQuL8!~DxrQ;Q_<01R?g0l$CW*VVH=yjaXymD#4sSd$2mdyl+2ShWYLdN-7)4zA26-JsYT@0VM5sDCP7w?2gOY_C{5zRl%RcoU<#T&;sw%2jUueuqWpn5zc#AYt=xzj8z4hX>{h|HZ4E(yN@(t5C}8udi45^$NdU;a54O_y0A#YAL;HDZOeby=p1FYAJox3;Qah^eUwEHH4I$xiwr7QZlf7oE-z3|1d6y3yC1&*4|S{X}GGQ6tbI3=}`Zi_}6qnZs+AfN>(I%LQAQyQa64fr!*HFk`7Q+RN`UGG>X`IsoPZ1py_~XQ#lL^@u6~R5?FGQ{E;e&U#Kxnx<uZM;!LN<-;lU6JL@o)h8oqCvZ*UsN%qq5pPcd}uq0LdNh8XS>Pl6$$SQqNO6E(AC5bc5f6iXal$PRjTZu3W{!B&5%@w4)JOALBCR5%2MVX~I$}Hg<F-4#->Pa_4M{1N-TIec;Q(dLYA~(T};xSismBKT+N>9iRo&L3X2aP4emp?776x}7co#4Vt6_w6^eW6U$>6zAF?WmqmSGw@mV7;1a>Pqbe6{3@qI^Td~#;e<m3PYpB(Lx6(UQk+6x}jg|N63$?5=7$*@1NIg8sB;LL>3#w3mep5!?jO6qfIqlljyFgG0m@AxFpUrZg8q}6{kJSu2L8)0P{<Ca+QL2C(2b)(yE8C{269H$A61{-Cy{~o|!=8wQ4iqbhn($u&Zo%lRPub<Z6$v2>rq#Gt(iH8$dxO&b%=*A-ytMk?mymGT1!z!yFM2)dn-nK4RXmvcL#456r=!4k7lV`=y_K9U+96sAa$Vr0J!EJ32t!mLG?UN;_I#u8ABb^$J(%A9TOro1@?Th-dKN_ulV^db=7n^vhHJ15e}-&H$Yh@e25&zi|Vb&K(hxTlS#t)Zls$6(PL2!^h<_yDt&I1DcWLbhj=XvpTqNw6BB;0FnkLGz#`}D95m+i(iCx6~D{)l0Q}cbnm3@@a7gU?J_Rz?*Nw^oCXEHadm|6M?<XCzHWbi0FHMrl3uVa0bOh0Zy6uKMmYSs`)%LseEx|Fh|0u^JhFFuTM;vSz78DUxdRjm=$V1;Pvw7W^ZmjedaQJ5rx(OHHM|WQ6NyafYql<LxctlBlC+z?T%6XKW&>3k52E9&;1yaf#$I^A#Jw5T#IDml7hFL}VmZ7O;8NT<w@+!<m2;AtW)!jnD1fcv2e3RxXR5emBaTdsSouJZqk@tT^_B*<PCMJ1-pRBVj_@jH*oHTQnyAoz0D_Lp2;eJ8S}Pwc+wToaq<4}oAO+N{vtQo)EAPX<+me8Ej!jv4Arw!&?GjCnJDkC`Rb#gz1%wDc2d3=UaSRlYldGw(K0ZK0j^1{LVm7E^hsh^X6Amtw&D`E@M(FfLLN+kUWN$}HCF;Kt<r2e*$(?xd3;b%#+f#=-!dZlzF<H1Y$->Dv4eLNl*a&G35e87fESBYPcPHT5OPqH`gle<kr++F=XZ%Aiceo35xbxNFF7iPsXYDW2BBT;fE_{3HcGvZ0b+-}RJXg0nB1IIqWWu-9K=&L+!$OPDXE!svbF#mkZ12L-_AbtC@4O7}<aF*;>>$rldWEu$8|`Xm=6BWWZKR5(#-RCRyPNB?chy`^6e*(ZCObUB-WG<9$&Q5T80KDQwtB&iQ+OQ-e0XBL{S;Zs7jORUle}bDnD+^<gJHg2!n!#rfdE8Fj~e%cc}Qez`sz>T#dNMFs-Zf^8wt%@dTiAJAFA%9IFj?wO4ShiM>Y?{Bp~Ss{!^M=jcBiNm$!V{%&9(vYT*|~bHJI|pSkRDt{+aGNI1P!NLUuwv|h>Ci+c5Bwk#SpUUX$qCf16#So&c`y8Q+p*$--QI*3|+-Qv_7-Cpc+dcG2*bC*;4QuBdpWpw(&mEhdy)EjrUYpT&HiIcG!or<;#HKvPefO&cQR`rwU{KRK6qD4FUXNPDw#Fi`tE&$L0-~te43&4sGy~f3S4Om?;IyF{H_o+zzzj^_s_6W61a4rdIE-{ti2fxE8xs0`Pw;y7<GiyZ1A$-9IziiV+NlXT6%OnBSj#ljxW-$}%nOH3*jvr{TbQiS2P|IEE5H%k?vX+(}@LdNlJq|={2ZOx<x)^BcH!xUR`3j1AKya+sdTR%O-HP+HB6e@jZ#+1|%Oy)dc<%Qa!uUDhFd~rToCP{ok95l6e!|z4#}L!jJ>m-N^PWcWM>>UjZ)Lo{+x_cwd4Kf&foeLx=;BY4`a@68=ymC)e{hf<e_d`+GBOmVANbh&*=FTmi>x?5;<D`&D?NnfQD&2PAL*do5Zhtd4miF?iX1$G3~b6~i{0`zmTeyG`r-8-bH4+==kT+vHh;+)T#1t&(tx-)JsurH2^3@wk7=L>clmUt=k=FxxP~O_KxM`iQ2KZ<R)J_}zW?O|h^$`*!4?BhfOy~El;<UtOYDAv2fM8%*MN*38N8B>ZtjfS+mT0IKE*xb?*3G$g*)6Wz$gJ&RtRVZfRS`h59@DB=!GLL9jh*bR#R^Lr3hMqdmGG^oo?^MH44J~pL|oG^AGLL3CW@6-6V(F3!JsNP?d4klB+6JPtw-HiA2@Y%(bf2a4uK1B(D({3|7cUTQkwBGv?Ze6ee6=%r&{THcRqa)_5_Qf2s<HU0#saa(t5VxFD~ct5;nTSNv1u!E1g2NhxYh2?eL5R6H3KDj&S0YT`YI`y)j`%dko$L}7)ILv6}O27xNoOZbRcbnK1hk{L%KX>V0$lAsr^$DW~7JQA}?402}1j*3nLdA-2+ygWre;qbk2ujDex(H4po4Y!XXorh!(EymYZ4gpO(AgeD^*<OzIUQ#Q#nO~8N1bbad7zAyjZ_lRqa4R*ZTMKc-ci3=OIT?Gl3xvS$opcS#4eoACiI&N^i9w}*)Slilz<%&Dxc*0wg<dV?m81zRwLk{Hka8+xYi(Q*Nd=N72z++z7o@-}9`TBkevhjTjw^+>rD<HIl!nT(caqB}i@+@kg8e9QjL95=-FXicqeH;RHht)S>;qrFxu|aRO>>E{J(t!kbJ}{Qu!sxB%8fDYMa$-R-Oa96kYq8PpUH|GFW6yI>DrmID+kJs%p;syFEd|?cn&z(@<os3){!dThqBc8vXTJ#JzY5n6t8*Zj+{>@zUI1tydChPNR0oJAM!$0!LMh;p(XeJtT?n^8aqQtH9{D{lfr-kOyszX;EJTG^F>-PhGXly4d^0`WW0L%1aKf?uH7<kU718z8H<@4L|)oE6yriumj6UG(c@Bjd%U^_3O@%Eehw$P+du7oePow{ad`h?f+>oBenq}vSr&1*JxK!D=fNuTX5@0TVlfuM7Li<eymF)X6RMJ6KrwAfVcOEVlMPj0Iz?q}W1%=E^i6p|Mrq>ZhGF>HS59w|)&o~I$~2TiT~qUu(hp7G$ML-gCR<6-B#~%1dbms`<_6_iYkAMa0ag%FlD2j0HZ3DX$-kIVEzZSwLP*!FOPdr{;>bbUWFd|^*H*mX;1-!rb&}SZIec`@FXI-Kk^dPl$>(F8dUjiaTX$^5+`ITWrOi9vWJKV`;G|Q)F#n#w=|R#zY|E6CuP^g|_FKXMAmEfW)F~d+g6=y&x*cWqe$Pagg^2+iaIi4R^1!dX5kUC5EI?a)#inyT)Li^AJ66=f0X+u4Sz+2KSM;6}z`g2Y-gFe1akzdP4#^KIHw@tmQjV>-ahxhYN`uO@v_9fiAcFWO-Cx4s9ynt1XDktrAQpc}+xk6<S|F($mGzZzfarHn5LVtfrUR7#x1MGUxM!YOe0kq;4!m~*7Acu!2(Y$Pd5tSIoNB*-G#BLN4`jgdal9>qb&pFsFoq9Rm#Mukw*vcVHswy5hE7){GSC2E%4~%k=5>0Ud>8=$5yg-VvqvxzIjQONxuy72hhQ6rgRjh0&J(Vh4{Tk}6TuX9OTMFlVXQKjZd6?@c_?a22b{{=H>hoOk56_CADlw&w@gvrLc-F&)jQn1{S1?&f6r2OhFb$ZRc_$h3}+3tX1Fox`o0XoGHOfM`IaH^@+XGlTP_Ax+5wk|)t$4l!CRJAS6dxe7`XNgJX*20dI~RrLq9uO3PFXgUP5(3%Q!1xMR`0nQ76d$AVb`-?7Pw96w!s;Gg{SVEl-mbC&cqB=~sE9B(oY|hq{q<j4DhV2yYXD@B=p(c+oIs`PsL8X5MmW-%%Phku@uzRAPmJ8z4P-%Noz#>OCw>XVrgk&3#b0*7wNArPrm4!|E`<1-cK!+jL$!%68F)*~WT|-&!>TFV?}XYC8%i*ME)L3EX%)N|*X7uQ28sO}HuZSG2l(rNUZ2qNQ90dW5V<<&V~q_>1oMeE6K@h&#7c*FY5DREzLII?+CTk)S9}Ac^Fi8YN_9#=0}zbA|4-l)#0FD=vU##5Bw)%9)jgcLj_g@jzmhqt#QMUJ25gHdSrZioc3^c5o$sUBwaw;7tT`UG0DeBcL})Qdw%9nj|wQ`-jSXR5FSj(KGO(;DMUa&ctt_Xq9j)FgG!7#r8**alCrOdI!5|yhW^y<v2K02ojOVk0BOK^2BdIi-i`Rr#d+w-}RBYxWTi>$=RvJ7^zZ+RBBt7OIN05a;~EvI_#fovP8m|D6uw=QfXHcD8u}be*S-7)oA#fg%2&`ZOTJ!m9MDO5b-H^PG#JAmZMT_KKQf$3?pViE`^Qp;VLZ5eu9<dR($q0gSClpyOU`ZZY7k4NyeFWMcp&pME3UUD2~yyO_3zA$Xp_K>TR&So2)X*hp=j&X_QSrXYCsMmB7Vd0ubJQ$`p`KhO_=wxh6+Nmt#}L+aAh<XDu)-ZF=p-riTHO7_n7P!g8?dk%sO42rEhzKEwz;)e23o4^DT3+fV<^n@ClPf~|0Mi70_#hcunQcv<4qdSZ`(-<3}GA8KP=+;av4yl$e3SBz{uQ(i`0@H-y-Rui^>S$6zx>|e13tagCY-SH-4=X{(s0NKv+CPx{&|LdiiB<Mh<ELjrI;eRsZIgzD}SD!2@7?Ig#tYHq%4k`(CjObDspuT1wXvK8a>+sMflJX4~j^HGmjfA(UVkTA?XZp#REU;mlY7VKkxTI0MDmV2$n8_s%qqE`9qmru0d_W~m!D*5@u?sv79Oz>Dl<dw#YgO9LwMck9+EN`Dr-yL^SJex=*??*QO8Ym5Nq8i(?>LTvsh>JM1fgmUd))$m{uMfydKV@DICq)VSWVO6h1$5S-=*Um9~~{kY@w&=s`^xi;p~eViREb8nhCJjqci^&J%XuT`2^V+!<b`j@(*!5y!vxoiN{BT-Fp9jyj*}MHYihF9_-M2B9c!%xu&*zh2}H$c-|fc0BRPuos9*Z4VC8VkWZY5lXOMVix9kuD$blBSg}$O*93d!r%SbqP8}h0_6l|2vs09`D?XHgAYE@`Io8oVsb*;I78XyYDsJ|tx|sxfnkow|IFz)4?2x)ihC_JCU}D%V#_3P?>rAtQ3!NRI)KvU*kahfyCm!lYW=B3g7EPRnm7PVb4z^XrCsfx<srT1$G_55km)Z_y+<v?ob)t{8JYX;h(@&Zozl{N3uVFn?vnE^Ij&c9>d!rrabP7E+joK;{_k|C)jM2aKOgdLmoXkbv)DZ`!naM*_4ezrhl<<DJBlj7@uo<L&iWOwbHGCC}LW9++B-AZpjRuWlXxdBrySZgRB25yN^h#QV%!4tBvzmme`{hw+`=DDFIa6$fupg)`YeKQy5~aRs$G}?ME$>pps(H`#F8Ntp1if`!(Jdb!__Rce9h%NmjxC<(tjUh>;TDY$3P|Bw(VPsS-AZ+e8Hf(`fq^aM&J){Rg0c7{_ax|^bE)&;#<fwXBG{Y0<4uF!YiC*ETcT{PCg3+LAO@!4-FfysOTBsX-Y)(z=?+Y{sT;j*u4mjO5brGGPS-N-o>EZDq}wa$CU~K&<|VBwFZY~SOVXW~O?NfvHaif)jLe`_iA17m*`?IGIZ3@Op~j=6gOM^+L)6h*Ckbs!Z?C1^2G$sAy3Oeg?obW3$-Fo#)0o3Ya;$_XUMo6T3UP(Bx;z6-@VbnFpN051AHMQjHkNlUlkS@1$9jbP)MR!AMbeqnTXPNUHz}B6c%I??aAr3Xc<39?ue(2Gg}>~E2j6|}h944zaW6$0JWz*Cf=n%|ewniYDrHBOeBzXrqPKYGBvVcNSh?!{$c6N<r+6z?bC&#2E}V5QL#?uv$Nt8%Q!W65Ne2-dLTH9s+zqf+X2$6Zv4*^|Wl5hq>}gDudKP#oJID!~nm}c6wUFG-!E7H;y_SD0rC58Z{js7)k!N_c?bNg1Is-t;d`(4#duw_IIvh8d?MSB<I(B$G$c@g_<WUOzf8TZ0=pL~~*vMn`<@pJyMQ3X<0X6y{;4*2d{f#BR<pjj0{?=cgfYyGMo|}L+_Na8%CZH~KO;G%@4;LpOh?p+WUyXHZuTDS=4ciNI5L*5Q2`i%@;lMWPe>^_{MOi|P^}d1G-#X4GAVLIK?CYYY9zzc|&KzWV#^3FH_6eL`ld4lMns@dybeZWk)_Ldlxp^l7=JP2*#^tC_#{Ly`-T(iO{hn)IwDtE7(AeKRIrj57_S5OW7k?DjuvVBf{FP{h7e4`q`4cc3{&z1}cEhD*H{l`pNKZijt5|ct;+p$K8T)Q{#9+y5u7>DZvCBoE-=Gdzqny#;_gssOFqvB|H<op-^yUqh;9y0d@~6GpQNY`wFuS6)8EVL~w6EGL*yhf<#EAjU9#ZWw?3e;a%Y&faM~G#4g0oz>ynYh-xU~Zw03l?Vw>5}PBcG-E?Vz<e76-K1k%tYa1wJU=W<JnhhVcONmL&EGUfjD>i+5S<nhva+K`exuqy{qn^egYv8D=clH0WWQuy5nndzFDM_J>)~Uxl<T!`+gXM!KpU8^yg$9=sauQ=?cBkY^M4q+MJ-d-G(wxC@)$*B#Ie9pIlN=^fd}9MyPl*e+%?Pe%}LvoF~jIypVdXFv+N@I|yIXTyd@$6oPGnPBd4QTw0#`W;O5E-8BbbQ6;u%yM+iSraqWk7Gi6K@&5~I+(3_zkm29CW{|?XA#Yc&4ICrIh)ei#Eht;PJK*Y@$4^YW!l_WCgDf{U%3&_ToprIabDEZtPRbqxt+FkF8Irx&2p$Q`AK2ItC_H1#jw#?8&1!*JG&ROJHz=BaIw(|8Pb>aI=hm(U<{~0+El8>Tm9tHuwuuvZ9X~)>yIEeNLV01H7z&i=({{kSa`Mump@An0B@(YfV7W3-@2bH1F$?3xBiW)jA-746_T3pc#B*NP}yTGX;x+aJ4_AX@gW=}n|gEu{gcYw=I{x(4*&tl%9jEtDUa~)&Se!TIW2!Lxy`MaEkT)gUuGpozX!mqlVI-^Ti!kdPBKi&?lt`}*;AQrhxgwc&9nzKgMZ2Wi>&aJ|K0%NT7taYp-dJmG;aYPDhVjsU$pnhH)uk(jQmi$-O}w<tLPq>GS9RU80ZqFG|*Wc1Q0~^%;am7UuNRtdXb{oWzEvG<)VZP@>mfpq=~IX5|C^K8!&08HaOt;T7wrLqb5O@CE4BBvl|?5fwa}bqed?KH08loPV8@KtXdYja&?hXN8?>!Kk)XOOl{?`gkrap&}Fh*hJ&e&fWqBq<=h*uE18B5k7S4Ss~q61Wxd|yM_As9tyN6u5hl4~f_XSjK)CiYjCDeF!xWpcI_5+maIuPtf8D)PQt&N48v%|Q;3S2`I%2Qc%a`BY3&AjlaH$;k5)2Hbe)qGr<Dj*}77nf&wDHkmF{ph;tfAm8tAsJN#WXC43tQ}xUyoiK<+4U>+u5Sf00Fk)M<z5&hD&mp7atjBA7_x2w6^*Dv7$%r0z$Dwv-u%g#jFh~mm%`AS(*~fhb<-m@t@@5CkUdfs#e5IsVyaVnMe}j418qebv^Skg`h#YYGm4dw0yLA=X~_{eKGhz6bG$A-XVDD+*A+lo~{RH-!a`7OTw)4m*v-xlbxT?TQ8^$TVZ&gCO2vYFT0mig){hmov$7-e9b@xTefwikG0{hV@a5GnLLY7ly}B?c*3eMU9TKd7waxPlb+71!X+fRBX+f|kHuS7j^-JvQCX)X6*uBj7HIzLJ9{5p<C6vw{x5nTd3t4O<NSp8k)1bktDSitg%j_igx*snlaAg;WFIBuj&Za<3WklaoE5$Uq%Bq8{-7X5i`vowiJTaO?4UgKW{cL+$Rh7c6hVp^kbitENbJV#Iz*+d=^l1=`iT5`<C)EoxlAOD)7agbuTlDS_b>Z0ecb$^Y8KV{!;n^(xzn0I%Ys<;hs+g~X_t0h7S`n)H^Edf@Jw!O)x`o7i4_~A<78*rB6%qf?V~Wzkt;+QvgGM*m}rz`=nWZXWeR}42_8Yxb;|8(5rL!a26GYDhK0(>s;ZpyIKWBeWUER9*T=F#ZCR)Ka&RI<Y`DX+W_2W6>AWI!Y(OGwS;cB`bB;WV6{JeSF}igS{WGkX^xb4kXB`6^!TXqnI{?=_{1I0?cq(&%skvTxSvmF5-vHmnNF!FAl(O4C+|#@DFu21X9y4S7cmJ|=q}-@Ap%$~%#NaJY);NQVE9w+#2~c-h?^O5vtpPW%%B(H~ICuaoMfQ>&#LU@@QVjm7bh)D?Szt-%`BLcly2F(P(=Yo+k4Bqh{NF54!1Dx}nhahbapjzwIqIb1jAZ&PA%Q)?WG`x062&nX%+{b_qprdPFqlKZMhygpVA<D%H5t+8xh0HCYK8xe3XGCepqjyieY4Xv^@FMYx~?Z4>M}7)i)TkWDJ|fe=8$BRjl)T4R;mj%*SnUWUu}&F;b|VG!C-Kc^_M{vqfx#4S+bs(totg(&`S==%>)_jL=62glVXS+s{-w;i5kD*6%+Kv*RIB=?`mwnPFF)M4TwKn>S}noR9))mRs8A&NI_>*k^C_l8>Sucsk$2N-}8P;V2K~!*4khR!=GLDG!d8J^dy_2v-7*IcE%Hsx{WP+-E#|Gtc&#ft$AE0+Uv_+PYmOw=f(;%d9n7)S3%C=lWp63t$9K3j0>It;QYA$Rs5<}JE`R0gYUT7g%KBS>DKtpC}8AfD<AXY*`ui{L|QI*jV&#sOph%RPcC&lyt>TiiWXk3dDv$CRLWP~jK^ab1v>PP%3|J`20}b}nrBrJNkq*SyxG-oRnf_??ek@i8AHMo^zoKG?_W_YAAijQ*89S;M=ej_&fay|^Rs2Iec7_t+OnrLZ?^y0vKOXh?*%oJ<;vGo$)xst<vWv1YCr9=_iI;-{a_!Q9;#T<cb(LU<?R;^WlJmUL)hWo4{B3$=&?`~$qAFPH+ux^`J)|h%h*Qx0$xq~MEXmT3{DKf#3gd*{iB0{-%Rt!kDhtC_GCKs?Qf0FQQ5c^V!(=2(8F<WzVP;uqqRr^AJEQQa~?e_eHS0%^gz6xr!c^gUuyc^B*2>@(sTt>u;}ljj6oxrypgm++w8!rnn0@Rj`)i1zqP8>4F~GGO6UyKF}WzALmh-u37yfv+fxC+pDG|+RzzDd;E@P|Rj{B5G#S3n#d8QV$OC4URa&~evq1|#-;9N<3zqA)<iiF(IeCZC$s6iJOa)oq${b1^XR+j~zx3Ea77?O~O7$e^F|79eD4f<ngSYplZ)m&)M@v|VVpU9vu`;~E0|po^iBMhT`;cNp1ts3$0qv$HfN~<0nbEX0F12yWcO9qJ?WePAE%W2APfc5{ap<?~$y-t1R+X^5%g6KxnJ@GROVW<b7@lA*yYn*M%r%NBBVsj#Mna^?e+f%dh?MxX`8=0@>n^+j_MiLVt!&rUy;mUo(=`U6)+J_Sa30r`XD++Cg$?BxREQn~8rar9Cig%d)18sxNP3n^is1V$J&4{?ehw0h@c$osZx$onmSzX-=}ZwPhK!8J%sbYtTUEEJx~i+oEt&Cu<{5;LKmtEtBxDJLjOeydV;i@GWDB_)shg%TNVGs$Mm)d^LOhv<mcY+EHO5o7Y{Z*i7=(nxUTb~(3^8TqKi;a!TdBV?B2Sz+XP>>l{SE6|i%p^eUgH{c@j+dV<ajuEqdO<yI#>f_V@*v_-FM93Y&V#F+MN>*iyQ}RP1bv2;;icRzyS?OKa#aleBzLRR<B#r{xn4BtzR_9b)Kz%XATREOT+f&(sGYId8=+#|60*{GS2Dr8qs>iQV$y)$C#Z_nfK?xh)uj0wu|gNS=e5HxM~6R);1#7fAN$yfC9(89m94Nde78+PJ;Ij>B3b1pL@w&y}ln$C!QNtdZr&A&iV06NmzS#^Gr}~$ENA!89yF_;LrH+S_E1FliAGxLzwjN91niNdL3>O@K=jRe0Se`&`M|b$A0=#R?1BH!fpUy+nZEs@Blj_h(1%SIZauymzZf4K6yXy|DPnT+*q<fy~g?1sn-aPMeLqZAj20~bN-Olv6-&-yT_3RcFT!CfU)zmWN2b>qK5KBm=q~u=_=)V92e-aJQq!Q%d~|d-$ovK%U#hS<jEVw-I7wD^1&3V5U0a?G}_5cYe|o!wa6>O%vOkn#5)We;2KqwFJY(mm)3e^_tJP%L>uYK3q^V1);7A$f(Z&<&oSB;Ng7JFp?=pWh(CPMOn=c#e^EnzdHFKJFC+Xi!Y`WXZ}2j_#>Zb|(_duMUu4r?WYb?{(_duMe}ZJw>nm@%=biBBvgvhsf8nO$=~ESTeS7)$f_S<g#nZv9wImT1^DUO_3IpxkNU$i5a&!?2a9u}LOz^YrrHmGZ*BO<s3$tZoqTW;S@u`ZsDUT28y%RZgKbONERLK2Y$J~HTqa^xFc-^=$=L+dZXE;8gQL>%98K!Tt&fB@8TRXbu7>${3s!@I<4S)P~Wem;V(C?<}O&+?g^;7ZmQIXtU`sq7ouAC%^$%b({GP5fgq}7Kv=Z_{F%fXi~N^^B}Kf4}pDavDAb<+wT4y)YoX7HD9aQeODjTBwclgD>v*sn|sKN&iFT`Wj7RiaHi-FrXbFf5ALb47LC#gVT1HO1;d$NapiI4dzl^?T4*_wo3hM-<ro@n3y?EKMFB`}p|-1~u?-_6Cjp@wzDa6)p9P^6t+%;K^SxS8NZb<96oaFWuU8jdDMm5`!T4S&i>O3Ehnf>_MH;!!dqxJG0OF^Y2V`!_QpU<@-8)&}9(9;}3fJspzf@$oUaV<At5Q!Ydblq+&mgTRNkkE_TjiY5PlW&c6EmFQaVfr0ih7&$9J@+5P*dW`bTeLcF4;mI_3zYG|_joKIUI($YdC;#A{;-qnq-t&!PC$@NbC;K;K;{uLk~d`mWVKZvd5@9N2;sYdoCt6)n4U6!1Ra2wDC*c;<K%ES^uFEuDg|EO{nh(^<H2DvoJQ=k)@r;U_-&R^X^aYK50t-KE}ofNdy1xUkN0jcP65i1kLdkqDjN^0-W1H<ualfowGi*jkeWkHw=zpr?FMLeJ<OwUV^GoQOMQ3i4;J19*#60cWcS4JhWjV5iMzbGY0&-BA~K|0+ETcO&ehyZ7kPs8zyf8u#$J)f|B@H|<Mn0ky{>ZxQsd3IMPWId3!eq*wp1$;_0_qX}^V+gA!ll4H`r9GzUx!E3b^rQmH-uv+J(+b)(MsZ~4q1yPxnl=ED){t8--=L$N=UiVA6p4P(KZfV1sL^$W-qaU*)9PwFdjk7;6NtzTrF|kjwf@{r>c%}~1uHJgY&c#$o!hh>ksJ-#m6zQF(PY+-WzR&YU6`<%dcbHd5Sx1SL1U?RBcka^#HOhbn=YS6Y+9YbnF4_w;k^Mn{>5ilkOSo|XspmQxTC1X)-)m@%Rz+ljP9!gR2XtliL0pv6<$XJzsiH!&1^?d^ZE|9V;Kx#4dJmy)Cs}NxD1B~n~UKf@Hlj9Qj}8ht>zQ%mQ*{-bMxMHD}X1vJbx?K?NF-URTO82yjid%8~C_(;f7p1^@do9#`T}L-+LqF(L8+XC&Q)%-llxqlJ`cM_E?8wWj>5o4XA{Hr`hQrpzbsmAEgx!6zcPw<P;pA;-_KD!IctC1tk#N><1t<<GZf(R+;!Ywm@>!g<=gN=prW2YCn;k(Nz_$fQpf0v|zk;bC`8}I>4I50^G2v$!4uwf=u+x8*o#~`vzd}Obj_GU?w5tVW;3w<ZIpy?MaD;t*pDEKG#=xLPueF+F5tu!X*jUkckKvh8vIm?|tCeRK?n#n@ugTaP4F^K>{aQuft?EdCjKe)cJe@$On^ONRLdYhPHZ~O>}h{%_b!k&Q2)7eMF&I8Dcw?2^Ec4xlE{{eemo#Rh2nampK&&*p1GB8>t|+8)AEAW<guAwwZN1*(kDK^%~Ra=7S;t{oi?4!pmp7MvCzAGWqx{;pJ)LNKswxI!QPV(jqg}Wq+c&9H@%yhj}XLz`@=j&=FA=xj=xyvlZTGl9Da1omjdv-6Ufl$+IRV&M@mHsY*8q5VtlL0!K-b4eBOYGPxQRR@e;XHZW}~NwR<w;pL*b{Af>gb87hB{|x;f-qfTvrM2l+9CZ9w1Smz~wLNKVs(qQHf!v+G$PL%@{Bv-Xjp?+tNlHT<zj0zuC2^MevkgwhzYc0PFNNJeJT%F9;(R+E+MGa$1|8g$zHw#5K9o6!-@oGRq`^?GIpdP=WIdUWR^uC3a+zSw>*EfAOq4iKBLOvbmh{lpMSrB2FY*Fvt8sGeNkT8xS*+Ft=Yx2j7N8z#=(Obde(TQDoV~w!^q;-vJo=1mNv}PR>XR8XFg#gvoWBuL9h2yI25o3rBzoJLbBB4fR2Mmfo=+!ENSZQfm@kwc&KGs>?iq65c_@dho$ZO>GP|?ROHe3nz^s}`I>{$b)lk|3K5#VFwG49tp|N<{Yrx%a`Lq`w`cbDpe1BdT#li#l2$6f~{9J0A#DOy}td3F{$EKFg*}`#TNQB0(A`C5KVS+n&n%p4p<Pna+1*=SV$-FSmEZU1uLi&KbMl&$fAw4m3xRP3bC@>vLe;jwBXktV3xf)pwR+eh*Yu3;v*Kgd{s<N-8yss5~9FxXKVQDRrLzM?shWcRQ)Ac@1_BB$b&i6G_)_~pV=uy)DT1~j-^0!xwxnQEg9d@_&Oz*`xxBmT4)xtHG$NvXU<C^R99h~KwbD)j(=eg$Uk!$WO(HsWaHnOd%x<iAmOJY($A0c}nxFaBeo7_TXXrtVr^%kVc#9hcQHzSveg<LMq$>la;mP^by#2LSwO`nC>D<U>RC!#q@)0IX6JT7##VU8^GHq;~NGo5oRt{L6jQgm|(&UZpiEVc)CE3Uc!(;mnz4ae~VDOLl|gret(&t$<Nug*Od?!tO3`Eo|9!5SlSAb~q4YjZJ(iC%r}QKWrzi$REczNNbJQf-l^Tbo=YnOd=}VC8H?1yxh(7dth)>U{SM=$IZ0uqp5_0x7G4<mWL{TE=~$2ue3Cl8B9;2oOhcqMBL3eYB*NW5f>$ZFXL_?6*<?$SiZz#fbN+_N5Dq|JD=#xDwx4z*<<~ky7V~_Jzd=y-7n8!q7pXQcoJ>NxfSHb4(gZw>y)1jAUQwSmLpsGUW@Yz~1newh0Fr8ahtP`Xb5p@`%iY9utgPWkx5QkNB)jDEW79asG_^Ex*`tc7MaS_ZKqb`O5DwN#lJK{Q<ITw=r*yaZOLLqM^AZxGEYefz_QPa4@7O%J0=GY`|z37dI#Y98|Yc$2WHY5i4MVt{l1yr2t$RD`mO~horM<lA;B_Yu(KvCUyO=QgGLk(Ai7oe7vyOhwtM^&_LurwYP$e;w~!DN#p6^fN$K#Md#Y(5X$jR!4vP=HP*_52p|Hkvk{CVs(u0M)`DF+#y#xXZ0!I3y9%{?Pv`%9s11JaXNB5ai}gvgz3B=~L;Iv?TaYbqlTN*o8Y`BWAZ*u#r%AnllOP*Qbf5zS4}urvAs-Z*0HbV>*0w>oC(*XzZ$HH1ldwC^+>?{Y+laXfmP5g}r=HQ%BX7uLTjYH^iM*RQx+jOn+>_?(kRE!zdvZ#JD=KpHo}cfYK$&l{-)+J84k<PFh<j4gJ!vnvC+VDfq6HkgA;p6n=@s|HE2Eg7GfN%PS$m3aa)k;PJ4lQ6;kGTl$t@<@t#0#gy^#@lF3U?XA{EmIG$M1NmrF)O3FcEHf-(j}n{>s3V5CpzUJ7wqTN23w<IB{1IEKJ^Xp?LQlf=lg7|w5QL5wRd5A0@4+0BBQ=Cai|Y!Jao=iHkr2&&{cf?GP%>6EcZXGvcugEoK{cR|!IsBPRfq5vIvU%DCZ3z8{?X2w)I<avEK0vH1I-fV-b5!XCpZdMqBac)k-Zf$VP_1oNRG2txircXW2O+Gq=-3@m)Qr+4H2acgq`Dj2k1n8ij#oX<5cLO`iNg16sMG-t^s7elG{PvZ&uT{y2LKF_uv$CYJHXYeV%}O{wiIZ2h^89R#v-rCstwT*pJYiF<&02LdKkjajE|Ao{_QY1gd?-`S^2)W%TnoV$^o(7oEddDj`txq_q)`6hH@F}A-;|;+zB3P7_NDq1dNQnJdzXFtPn=&+3%Q33z56PpKibATk9v-K4?L1z5*xY<e%ZibXe+phtB9?kuTsx)f_BWj4!$#Not(A`Bq8zDxZT#*%Op7&)#iK^QKNU^$KHMBO|u#m?HK+@6NrNqbGTqS0aWBzGTGXOe+aHTw#bH6`&aqnls8aTyQ26J)QRc)b_6S_dR0?G2Gd{76P%uKl$yMN5L+?j1#i12vKs|4awK@}t#Z2%)H3E`BAjW=3gcEXnFO-~Dvs!{VJ(v4_1K`L_rf65DUxjomur|oMFp5VBq_}*Itx0e70Jvyt|~YT3@Y(^@=CE06ejixtPs4z$T2$`Vk2n@vZn3{B-kY>RfBaZWvgSEi2%`)$Pj)bI1C(;sInFq=9>76(YWYXti+$bE2_^*!YB$eQ=>tyU2A133OR5}7{4ij_6p2B>HPCOelNHcP5&!#lzS7;y(QFPO(y<*0WBvLlfWe{VR-Nc<|qCt;+E@}goTM%&Den`OiYe-XF?=gH~hMHu@HYb?;L%OIwbk@;IY&OAJbFssfz7B9q#=Sab8+(MV&1Y9p~57$z?X<vyHEf>LK2B7=i2zm?XV-y9LM<{Q_kY@X%E8o*v~lnPANCdTte;!QqJ6W>qX-=Re-J(iY=z(rAJWtPNk)1s<5<$IM0$0uIPRo_Ak?!;MV!P!dX2iXV}1quG%3gCT*`)d@rdysILGs!*+;P_-z^C(S#`os-~LUYeiEIzu#vU{ZdB=%{Qu$c@$-gCPq)G5!<ouaf!f7xId7?L9b*ItNH-{%L<?k`O6}t`Asd-2+IUG$Zrz>CP=o=r}D3v^alI?^m4G!(oep<AM#ncQ-C9ACM?Hxb*o0<hFYLzI-qp_J2IP1P^eUcMlYPbm3bMVE+LJ6ffrc_&C00_24KN5I)<3RA%`%-&LX?PRCQK*H80?D{9oADPWIT{&OL<S5PpEsv}eF#V4*NK5@JhQaiE274)f)6@k2hr2;8pN~QZd^NAUrj6SgolNxrI*03kJendk(po_~!KC!Hy+ck8B>6GXDy5a}l$`5YwobxKWZ7i}6a~8zg!JF`5-x7e~rfK~T?Fx^u3XwOz#@vK9SM!|d354@3Sc_>$VVx^QC8UJw3p2E0?sh;~B%!~Pq3!D_CI|&7Oww4o_!^t11P_i=btLSJM}(cQQH8UU50<iRK>8(NDhfQfz%5)Hfn`$h8}dG95Es=sC=lwLEl|_>x;vz)xgDS`#SccxYaGRH!uV90twn`;>&gcEM8aN6jeS_^uk^dGQ|Gv(bF@8E;lNKjls9BF&0KcZSz<R<&rqbYkazBj+EIHfb<|386m!`Lq7R5dHhM->cOo)6%(YcX^yCdOsXh?}@JVqfPQb++CQe`}B46mF6v0+WU-Y$-UaPc#4Row7B&V*oYJoqYvP!9>{cB-!=yrT)Y|g(j`fU%;gv<7>tpHu^31Gz!fdusf=)>;r6iuZ5PI^o+`yijMh-`^*--Xr6F&$48Bvf1AbAN~WkXU2D8^l943%&XFo)00y*TsVT<^vahJ|-W(vn```Lpv#3EdZPe-OkA2ZKk6_6Yo3<VA(aian`~}A@AUK2FA+Aew-lr{3)XIgsu4&k9S1{)jN^6?L0kEI&&$k`v`vP98|7CSc1Ma8=d<|`b}PH9)#5&{A6J8E))iy2*cBZmFW(ozn-N|S_9x6yD)sPmkI+Bz?N}e@MmCn+78AI;t?1gsHTZkP}{EPoVo7R5UXOq5e%<k+pSkmPjj&nuzNx!;5t@x^I^A)UwuDVg~eD5D5~u7DqLY!4=8&C3RTlR;+z~FZTpZ~&QnbLi0T1NsRy(t^#BW%=URBaXyGO5y$_ILse;zY<nW{|8t<~%FZcxRXuf$&4)0Lp@czsh#{EOYC@n=HpI;W<{qIb8_w)OAB$1Z+<&o(i%6UEtp*9Zi-gfy`4w#@1)&ni*H7NGe4bPcOwyNgBTMSJ3w>p)n?16@#u?8;^#z^9~yF%EX@Mh3Q)^-y84xs=s_fyEz8ply!W{|SCYYtXmeo$9atoIVvCF4H7dZ(uCyJ-0HJE73A_I4`zKG3Z^6c_mxsVabj50ZQ?clUd*<1?*cpU<p;Y(1N+K2sjc+AG)GxjCHw)Mr{zhxWv0+6?O<px19ieAJfCHo)NEGaYg2XM-G1eI}wgX#HYMpD7;sOhpvC_SIlo2cIdavBV^Fv^lG*v_1u8P+ynMATBRK$d`x=7W8i>sb|c!l6t<8MdjXcIs5#9Q_tyN8wDFaJG<wX4ZoQrEcO>_t2bK1v;y_aq5_=}C-sqnK#e>&uDO#V1cYBY1D@u;5~m}qmjQraWvl{H>uhwzvSGy6jmDF}ihQXH?Bm&$h)hInr0AWEVF%;6=Sqe~#y#*LL}~yanHPCSbDAFLztn6P8%v}FZtX!Eo>I(@G~3(Vue^of)XH3G9-kdf<jhmxh@yv@$&g9G`gl+QzTmhDpcP6oJRd`=Pp%8R#JFNCT~%4$JAb6&J8Xi^z7$GiiD+?LLt;BQ3r77Co>0dOPS;}TLRo>8pR}TVp-2_JQzQ^wpz<jqt+WQTDc>p<(%N-eLP<C@XmjLy+$VX<9{Hk`?QhHc@=w0k8LaV+mj}B7vMh8blh{TYL8Hy!+J<?Y#5_|DZqulSOH4t<>03EHa@8@=z2t`(%;~#w^<px8Tl793n2fFW7{yk=)I_BVkm84%dYrrUm+n7B!>0Q8A2^N&W`7(v5{EASv2(M7hAg00QDzgP8Sia0Ys%f`AO&I&`fEPy#tlgmytCwOFGHuNd>e$0Ym47Zq8%15I<c@o7&nj6s<aMZ;0PR)gl=}4wMWBfF5#d<lD-8uJbm2!CPZl=;1k4@ja_P|s`*m81zVyCN)Cae&r$^+bJ#|VU5=H|n#v2S7%BvBq}O;aMUg&<$$@40@?*ba7px+lYckpvQ~s?OOJX%uG12jxecTSC;1g;s97Az92<D-KYfcbag9<sWU;$?0xbO?>-x_1R&)>{S<<aP99G7z-di3k+A__fj41c~5{(L2{?+8BcD#0^KG{=}|gq<^hp47i*fb;x+$hIUw&0%zg-adp;)T^x~P;+?6EOn>S*jGC6thdh-^_doehqIF1VVbD82gFU9l4et+g^tBWs8z-o$T#(f>~BhHS%vDU!yQ?33%8MoS0+|M(Y;-9a#hAIw98-kpS%CiSKmjEbROf1p?(OK;ZZi-dSkOScu3h^`$5*20XN8bl12ZiQWihLQBGQ0j*2dLS@Q`bN&_LXY(PqZ+U(Xrk=hfdDHlBN1{D>WQ&F?#zXDfc^I51|8iElkNg^2384G65^ZLn_$v8e>TNT!4+m=duNg{_u_@OHa_XX;rNd*8p?)kQM`T4JyKq0e%r#H&K!e#di>+$azY5%3yr}*vLK#uu*qjU+`Zi?H#!KMDdTQb<<mK`?Ed+F<{k{nQ2;`t5E$4G<WQ2s$&1_KntwO+b+iG|2Jq6<q#7u&!KW?T`(92mntJ1b9iOmj)uD5XAe#nx7#M2?F_HE*?jw%)(sKCgm6Tn%$dd3biW5CO`+f6vAK9&8QyTk=Z&c*`M=%2wfkuWln(lZu1!Vb5YG|MbIzG4OaMOjV`$=@uj5i?llmcP`u=knH*V)_r1ulCSSz4%Sut<Q5y7-@>11iFVoF0nhrmBOw6iT-q8U8hNVxa6WnpTw?jY;1Zv0IjD>Ch>7fSe>q1?yqY2=O7qqLnn)}GK!#<Gn@9t0BJuY}5EGBXB|PC0ivZjHsz}XE;Sz8X@?A98DhHrM+b|Ijgs=fAUrla~^(j6g7&zj~0*+|s;0S7!0HA}4TnL|DMn=@c+ULdJ7g)r@1QyX2SVYS(515F>2^u0j2895SJN+WQ5A){~{$Q$T0pIip@FC1l54}(i-2i#8o#N|)didv_gv8Gy^gW-*c9ec(3@~}3^>;K}fd(QEL-s}+$HZ-{^Ss+?;$R{?+#r2Rcq@F>8X2GPF~k{h(+@O;kf2%zDqe-J)Nzsb%w@P^8U=razaJKL_`)L%<(VF0qewYm1>%5?C5ifOkTT@uC9LiQ4MQe?Zm@j_o}cdU4iYDS{jIh6PF$r~dnSA)be&vn^Hq;80tsxJ4HjEnmpn@-J-&eF(P64CHTXL2`jZ~te%hz08CH6HPaAyUi_#`~KW*@B)ZnY`-WjRJ476&gZI*!<z)N9;U7uB0Ec5<`W#3tW7N$yCc%aOvtbWzPV{;23U3@qk)Q(Q&;zD{*^EP~(6|9oLu$l{O2#p`S_xEqVS7d69oimR*2)NE7Q&}Le3QK3c_ZgN0#*cEy!?e7@X*(~zTjI;8&ZaB}gpeK+9q^rz*oB*#vNl#tuLhBz8Kuj-^8R{62lV8Z=3{vSo)Rw`EFWle2b4q;>rj)|Q^i_53oX84k)=}U3f(U-MOCS=v`DL?U^K0;gp+c7?>JLo-Yd0&hS~J=g-`aKPtRX*znwiPUk!v!d3W8Rdb-m_uwoC>CXaJMkQdT!L$bmovaFb*;)d*uy10+s9VXo_-^xBP{T3BLE|tm;wAek?`4_<cqHtRgv(_;~)VNT{S1ooxB*G-hL!OWOuwfBoh^e#LUvRKL&GRP0kH+&yJ~r$VFh;FHB<gc7Xz;%5#3W_3tKhC{!$(YqRSE~9Yj4RTLocI6Q%8>HB>fH-36Quw;tTai)C$2?M%*fjz(7YeJCzOistS)HlT7Kq`yegiBT>(jTg3B?)F&<C-OwW5UP9zpi}*ZTC#Gu>u_v{Nj|~;2OPp1YS)+JF=6xEyGudVVd>om1W&u1K%+C~Go0(}qfT&v-WBblmi!re0m-;GBV*9RGfgBMg<H2Tu2UXHAX$#M@9u+@tg`}a>iZ!25ehlmtr{9U>PgKlb8<`{?<sW~lqxRt93bKLq$1dJuDsKpU>Tj)vrh+p3o}E=6cbKWMzR!zCxS;I4xwr)qDX@{S-XrmL$AGLx#mbPH4@5x2>x!YrdcdUrf;IO%Hff36x|*LBH2Ytg9%uI3#-drrQ{icU%mu8E=UKletz!O)J6}-A{Kh>pUf91@c{(tzwtQjgC6fJbxZkA9m4AMowcRb&RRfZV62m#-LK+nRnq9&9TJFLl+hB)bk~JR@PMt%Ftx0%i`-UV&5{D(I-17T5(CKe@AKbv!%Dg5Jk_f#moMpb1yZp-y#;m0|0*g;%V#LFL&Xe+E)|aX^znw6X1r1J~*;QjHlr|~Rk&P{ii})^x6(fO|HU^Z%rRr3XnGGC_fnPX=yxBPen<mq*%K5C=qC&0JJaNc^87=c@K}iVzz~wW32(SnkBHt2NB$(K@Alf5j#GmUWjRPd!nQ-n=J82b80EH*CO=PL_$>abh2omNBtC3!8!Y#(+a6Ez)(sP>HG5-`UCqlM^;YA29l#6pB4o=`W8r83Nlx{7L$yl9~Ra^Ez3hz{G;W?~qNB$Ng?fW{kjrsInx!>>>rTxI=h_sb*K>l}E)D>On0)UJ-ukc$SEvY}z@YDVDNd;#lq$Bb_n`|8b*Nh_J2KPh<M;C+G7$dGv1uo$WKrDZXm71VUo0vP6nXngq>Bw*IS-;#u(l&|x&gh|8tQ)w=EsF-AX%ss=sTi?P@_9-=S+#GS#4~xx93Hl~*5WN~T<SwniW&XpX-mLAADz?`Qqj1SJ_K3l5s5~V9}OSljKp<w&cg=uxSJ(`k|2KB7`HyNs^qwD$?=(#R>#OSDYA;?>jk-xS#|+lc0tl-_$x`dBjS7{Th6|IG?J0&nF0f~=v<ZCVXH3OzCZjRJ@P1+Jjb-P-Q#vGxWd+S!Kf((kfe4zv1kw+Pikf^@maBGX@J5xE|D-p!)X$m35asbuJY17)ttfoQp6_xRpsG@mP~F4+PuJVm^Y;eLwrAO+<dhf74gVwYX17&;HW(l``UgTn0x+p_g8%X6=vLy9MbXDb-#dN-Y|Q(eIOxN#I~=dmY}Dx@jdxzX%N7&zU8g74wa%jHb!{O=nV%%(=Vz~1%^kM&j6+`BAPkgPRc9z$PQH_I<zoJ`S?3{v)S9?Gq;e7N9KoggVKYDyo2&lA$*?ybPs1I=&E*Ju-gDO?Fdfwnwt^Xqmy{Rc~0C~4T|0TJli$yqE=g!3S9>vUTdqgp|z#H1A9D5rZ;@-v@fU#|KIQ+%Z^Z!pLp02VrwpUA6N!I;4%`Ze7ryCPre??;6bq${Z)9nEcP|@s1hR8=-s5TR&YONq`6Lfts)Q%jffstCqrUv(9W^0tJZ`COjgJ8vaC)k5Vg`EZ2?Pe6*Dl}U__^?6KWf81$GLgMvnG%waP%I!4uTv6&XH!8bXyyp*wIx^V1(;4-|wm6G(!5St$Lq^uDCkEG8BtUna*yZ?`j*3$mB7=wWzk5<*=(j9)a-Fc@`)<|pAhcBIHYbdn(Q;xH3JDB{ZnEj9qjQZx=@W+&o<pP$(zuqny2&@so?Gn_ftnKk5IB)>G+cGs%riWMysX6)Ic9E7&LU0x3-+p`i8zxcPGO2czN(J{*4i?Hz%SNno}HDW<nSI{agR78rA9D)tPV`Nbdeb}^xl837<d#Ky(2<E`f2z)Ez(fvJMuKE0SFkWiSg(=BfK)>flB3#J@HdZX-%8=UlIshw`IPStf(mA92;sMJp^eZ@>VwDS4`Hzb(e6^OJ65B4%W!HC(5g|fY_7%knF<WFG8g}h3lqT}72=u^@Z$WSzV~19OiqUYlM(IA${jQE|_^1A?p*gTpRgX?5e(J;o7$aBoqtYm#=*~Ak3uvY-*c)HKA;|NvC}kv6@)U^>LPp|7i-y>nhRwfu*Py&bZJ8Enz_ZIgXa?KdYWT9Iucs_;ZTXg>@1900R@_AF+LdxVn#6IYWgh0LBX|^K0qjfW)NGt=R*+F(Hm-z7e)u{+P}UCLXcw>VN~Nc-PD;WW6*HI6%*yoT!jdulyHO*>DCx_}bY>ZYlHgj#aWE@ddm$8N>QH1~PE}UMH;YLM=0kgP*4n8J<+YWETdskH-g>YXI$<_R(VzLE;Z1SX7tNXBm&IU7y?4ioZ6OVBiorrE5cbs)pb3VRn%;H%Lfx049Hxy*6F|0a9B|{MI8~~V78bQxkV5$JuV)Xws(t-^?*A<lKsVsp$3pQ*fDfU(^T72nRp8o!y{p-fs7yBeVB~J%V#`+1f`h@bBQ_L1#f{Q+Ug+|qN18v=lVdOykoaDi1G-M^=8o!5)L}uTd7K1dCOsulf(33mzGnJn!?OVbe?y!KVI4)P3Q&%U2%g9XmCa|xn(`0n$H^)ClsyKGc+Wbv9NKC`)@sA^+-*=`^rc;)Q|CZK{6bB?Kd^>MxabBEiKj*d$xvACWycleZYY&e=^M+^%YkQ#V@9d|q0&k9k1pfc1$L+(!K2kTClrUJp#$ct66FLos$Sqilk=bxBvLoVT)q$;#tFjRi(q-pHg}c%gHasT(kZa^Ko-sNBVu>4Z)`}~Xja3Loq}3T?H%Vmu{FghQ|$|R8NfY=40J_akTB8$=#p7q$v0%$8%Zd>Kd>Uo2^OBTD*lDCsxb-80n@jdXi>F(yf9nm(Y(LHY=n<@4AxqO{H8W#;ePN+E!jPq8H(eL57~VCAvs$p#;7XtTd9myh*Rqz*Ty$8A52|ZEyA9r>7dn<fnrUMm)JnYqp=E`Z3cr)l+5L+?v>Y-H1<y7?ax9*nE_?Hs`902sQcJ2uh`L1f=7)u&&dLVhm_QNEKcVO{BJDnk^R9>pWIk-dm+`a!6r1WMHx*IjS|(ej_fK4Dn%nrcD|)#XKbQuDe<h%(E6yQWI3gzE?p%{Vyv0NYQ2a<V}s&LX~U&t$2Ncl>9`FSegYdynAFIw99;%$DOm+7kxAH6D64H@{`6x0WWbfIlcZG@iFTadRp>nzr1Z>}*Kzi3-~fZeGhFD|?oI4*24Gk+*%01ivf&^8TG14Je3_;wU;D#zKzDuuy31P&?f7}VqT2Y1D8i)B{`r(e?I~pu72&FLtVO*Fitz-A$1EP;g2LmaAqG1G$xB9AB-F=~P<fS5c~xms93go)=PRq|;+!i|7Ig)i*Ako83!BGd44xNFA6LA&;3&wCbqdu({Ull@BoKg$#IC{i+Edt`n*Z<&!y$WNUMb=^elL=ak()x5o)6(G#GT$1Sc}!MiRdFHKs-k2>x1YksDcd#zof6@Ie>rLq-^N%G#Zzmx&OBEWh&aMAO|omEXzU+LyRh!vi4G-G}Ibg6w5k9pz;=??g&Qmg85Zp%n~yyowq!Fh1u;0tiXb3h$Lt`ZGwUeanw72307{vt{G=tEWjd!Muf`|a1fdbA73YfVMxReSK2@yvC+)M2~C`OrKq0?#q1ic43};!9fAeydzU)%^exk~a2<OWz!0vCH1sU6WAsDMzu<bL9dBxN1Y!j*X~*|_bAekorj&bl1qS&S@9#U@_y0XaN*iB)gHQedKQ0|S`JP6-wp~D4xL>2cC@4$J!ZaGhdSVqGEII-xrUouWm2;pF_7<G<R_i8QhoXWE37iBS@TaXP&X^fi+W}Hd`0VF8K=h{wjY?cp7X_WXo7d3@P)hf%+B!XhC|uXxxMRMl2#R4o@g$r<m?}XXq4sqxK^?92Re#E@q>9#>go{|i8281q#-5&!>B&zm+EA2DoO%Kv5}2ZbKx?PCGYM#V-_|<hnQihMRT`RzjidEdYiX+V`|qkcb%ky!_;vjjm{;+Bua1td1@mew%&Xm;WolZEs?W1bu_6^g^xcI4H^>~4S4j~|`G%6Jai~1CI2e^D61u7KbcJv=K1R4&eQ=7YzxH^YL`Gzp>d!F0@>)j&RyAfS<=Js(RI0?DMvk*Zd~ZUslTJCLSe3c6LN{tlBxiy*K_A0y`J7wJC@EP^y)2@u3miGEjFSZ(({hrbZ|M35Y!+$)u(&TtzK=bJg0-!=U49(K&jMZ;+17$Iikl|>)p9kY7h9$^$Ld6!=lkNA;L8*5W~jXnS-<jcC1Xd!r_ISvkDMG9<rJ&aFpS4c|K*V^$T559r`2Q_hoB~+sI;<5SS4{0$_-ixSle`P!~41gv0;7dzkZtyr(1E2q0XPQ#k6LJ6N#=c(WsJ~h)1o5wo|&!VGs<+A17j~T>z@5vL>}b(M-rDQ|5{m)T+QUB{5yV``CKe1y{3xkFb&XhTiFeo*N)~pDDCK51yHENc@!+N<xe2q!@j-5R43XB~qh*fQxW?0->bbmB9j$hg8a$fx}5EKWQe#G)~b7AC2$S1hFRtJg=O;`dI8sX=+*M!Ic9?)M&)et>BW%Zl&~4vdRiP$mW)R+S05l_t0Z>sI^Ucg}?9?xZbs$t$FR&>0Kz&P`l@<(Oji>>7hDu#O+daXb4c9aJxvTBu|sZPo-$oIpGX$R*T++5fjhPekk7(^J1WfQ?B=HB{xh_<T<z#O&s%|XagrlT%4pCdXc=iLM}vKAIWVXEiG*M>rdt#dBVeal&h`DarSeF+6u-uScd2<R~tES_^hf&=-LF{R{!rc#<paT%VW~EDAG33uhDn#1C(WroKZcf#c+)^GwQYiXc<r!!L`zrDJi7HeiwleF}xAD(8G+|>8V73Uk3%y_+PwE?(x#(>ZNpZjR=r}B+r{)waqUtlIP8Ia-qH`t~O?)ADdiCyM%O=3lMsLN7D-41X>yZgP)MvtS9nAk=O$5V|mmna;T~mTS#*4bX19;M~uXY&7;BvcvI$4!#1(1&`Q?snAFCAQOt{hgHrMke#mX3Eu*FU+i^0xHt}|R(QlohlKP0=MQ1>Pa960LzF^&m^Wq`kutW_Vw21Gqf%GcI01)jJO6CKI@sUD&2qnWtxOiOb=>-H)LD10coX~*1IJ0=)A1i`{2w{*tCvctBI&nlDN)SQ#!p}M5xEd%0>H?3__XhG>ZJ1416b$_5f-fAbFw+_9RSc$Zgz{fu$qHZKOQi;EB_$O!;~-;n5cieAN_E1uT`=R0JHhWIc*N`6ThC<YbvwlB--$8H-zgQccN;gPMJxpx{`C7MzNwAgNg-n`?i2)_3^!Zw-GqVfrXmGPKQP^JhY|X~c!UCjG$*tqSXgQl35LBIHm4zbnbZ&ql~9^e3FYatFjm*Z8$sF%`3m@?*-|u1eD<IRcu(D@>_m2gAo#5w-7@T3+GKxBc2m72x~9j6nPfNOJ<u>;=et=<#bz&%-HgL5oX$XYgJqe`)X3O0@ZFpp<7LbTBcC2{sZ=`!VfxbJYB0Kam^ay)xW1x?Z(a^7a%=3OHxs(1#V4+43uPPm-FN73#>f55vfpGMd8sXD>TebW*4B^~t?e|D{5Z=fSg7<)6oyg}KumK1L>ZwYMnUsB*Qe5l#p?`4Dp*teH|-$Ts@B|2L;}mFk_sZG`DY$ybL}{9A7IGt?#;G>=Hh`9_TGIiLXHQl_54(}_wGTe!Y=&y-cfNq-tCP<X~*>%9xzTh+{+PVMMDfL9P_F0{`LVKAD^hR>>eP}1t-;RkNEDJco`R5(4s;K_kLe^Wa@k7Gxap?tRZg8zwY*?t~^Ak2w4BkXJGO|Yy`{G=D5RvB0G2Q#J7(<=$4okZEZJ9)|<E@cSFXMHL($WANmUB6@3i|c~Az@PFEVW@{U991;lKzTQS1sCdkqlz%Bj&()<WU>WGQE!)~&)x(~deALN4%U}q1EFOXE^<64VgP{6@exPvEyp2<G@4vk$vP{d?7KY#-LD(nF!0Vif!0967FNj25U5Z~H96$*vq%=P?F+`k&rr!joaF?gUIOvqpNq6o+~zf)d?t#v{YHjvD%DJ8;L6XjhgKN~hoXVioRd8jQ&`HoH*VK!y+%&Rd`nSpsQ?$|X6*YSt|?Wrlcn*hc^d3Z;PnCOK9G!$hlK1IEvXN;<uE!$7I)r0qD5sYVwEAey3YwH;5H#qYbatb!+J`>bW#Ljyyn;U+%GAIQoT>y+!F^(-p2F?rOnXi}@gJ-$mM?$Ii<o6o@CY#DtwdG?)a+R&`vW;EE?3vfexh*YXQ5teB>n^bsLZV<iaPnvjTs_O7tWN8%@z<_~70<Np-XIOf*1ak5Mf8jKn04PeWfs_6HP0qk95F#Mu*t7Iw(F8WCCe4&{kU~P5qq%c2|dSZt!M`vCi;#-f}&^vFf=mKVM!=uVDid>(E*6epOq6-eFSQPetLnW)pb6tO4QI|#ik=3+5IH5;M8?*?DHd`>@Pjb?!|qiXb;DUW(1}72v@nI|I)LZ#Uc!r<%SiN(1nIf*ll)z^ZwL^)iSPc&_!8mg|HCVtk5EYMoom-vG2mBH-UL@@2<i_n=M#ecR6}vNky3-kiDR8mmkuP$R@r%n5*2gkV%{f;<@kKMwq)E?MR({mVWJ4;eFV%kEIgZ7?TSNbnvpa&dcxwAxN?G3kjR9QJoQRY9P;>*}DJseRP{QG-wl#eH0`oS;DNjNg+4tb|vIijfjLDv+@yW6s7x#EJ=Mt@=Y;dctLHcARQ~Cv4^~Hd*(SX7Llr%Ah{U%Rt$Pc_>O?Wy3H$VXv*Jx<BIO55YJcGPonuzruM)(7$>bd8eo1KF2z>zt%j8KNY2()K^A5#$6t9P9T}SkKGLCCiOp7za?MJsvfV~+b{_U~;R+$!pTC;tJGPnG9cuSv>}+s3g9@0Cm_0d*JM)5Z`t{mR6{UNvTUyA4EM)%d+RL9f&bPLsV02BspO!L3k--J{f8&^J&C{VNMA|#UKN6u&3?53odU_3KoWsuA28wp}XwDqywD+Ve@hk9u<c~8JEE~At&qG?X83ByIw48TNJlyzWLiQoDAYMnahgcq4K9D3}W40P>Ukp$+#-IQ4vl$w*6}q|FbGUp)!(qI&V(#McR>Pq(G^yk^gIEw(pd_`Y?S*yWIK`gxct0W9LgO{TUC)-q)LoX;wFYQ)KU*T|wEG#v4?WuptFjb3%!=Dms2yqZ3uj}tZl0WtmPoZNU}S4VrtrI8E9hLCW2#f=oHv*wY=u#;JQYA!PXKi421=|3)!@(|fG${rp9P*12D?-Mbg2O7(p3h#G%(nCNHHKp40v2DOPT(dI#n)`*l~8n_+%=(6Wm-n!Of+Dn+s%2o<iq%F-L56WHX!)+WlY(nwt~awT}_nokhm^BF^F;W47DBF0)-aX14Q!^1LEU{A&S)`}L>oWzP{8x=^iJ2qrkGCLHf;8!_WsPxgW!6mC6d)P%x?3IaPTIQuHr4yyBogY1Q!Q4q@OusK&Ukmq0IgF>l6HK#oI5^uvXrD{Mg56S{*(n4Lju?7>lBp37`wOY2knUzFw{I9%g9tOJTgi_!7!X!op22O77CI%dmyu*UMF(ncT>Mg`dOUj3YkMrtWQn4VoMQMG516pG|tWe(}zTG5iiCf0#2LdT}6(vRxi)iP3P$F?1sWjuoI}BfR$-)oJr+I8RY>A=Z-kLh~s}eGo*JO(Fl4%<Rlo5`;VL}>Oi4kVTx_Zr*AwGs!OkQ3pJ*2b{NDu`IpZZ(wW8QQgh30Gw(Sjp8G4d9EDdd-yWPVEKXsR~xhI-9cqLR)@aqzrC-B}u}r~qL?gVjWNJ;%g&a*pz}A`mDX@yNgrnsMW`UTBZ=+<4UyHy*PYZNa!z(s@fKGDMY1{St+Fi}ZL5I^)E3YDD2>>a9W?$j_b#5K+7~u^2t&j`0I`Ox|eN+z<0XV?py%)y9z5T-P94jC?WGC_46mm>mD^d*y9=ZN<+kD9qM6{QW5qlhR1XG$B!~tR}~)<U;9T)wE?<c>>KmLmA@qy}mAzib9P|XKr26;B#itr|KyhKBg|S)j*j5bc=DjrW(QE?#Ii*ih~Ad9*SES(}CLPB0zKRW*VT?hvhXo_$NX$p?sO@Eq`xHPkDnf3ua^hsajm|8OiNN*@m=2hTu#FTPr_-m^g6+WebQ#bK<)5M5a$a@>H0xCO9tQ1NTHRU{F;Vy??Am2)t-|4l=KY!c9>z<7|Jj23;3S1p#S5J%3Z3rIG!#P<hpCs*H^iJ*<@kIdfD950=Z06OIU<Mp}kYa8?ps_(Dy%5`ZR&pmmT3<N6>%sdPf~F1|>{ju=ZfW-ESb!I*=v$_jN%*whOZI^s3`02Lj7XHnD-ecNm*YR6V-3NTN*`O_3~sx8}`S!3!*1Gk3ScPB3m8aR?~*tbN}zru6g(Bn&d5Q;r!kW+fZa#O~0dT&%DbPtzY%VFBBuKw>?7dUZ+dB(z56?g0GQp4m^>IF>$@qoUTliZ$QOn+hQqxr_$FAb0JgX#y|=A())7efdysCyEYQ+~E($Hbm;rhbsl)eq|4q6mK>iop0au)=8V5(p9XxDosgB5sBj%a&+OKcEq3Wdi~pv;By+5A8xKbpq_#%ULRAiB!sfBEq#T=@_8Qzo*iP!p0wc-Lfh5Tg|5U3)z&h9Z?NaNxg_~M+v}BlmN~oQO>p?*1_`GPt*fo^5aVLVLEC)oJazsF^MwoKMY9QuELl~c{SArnDrm(e$g3!aOZL=Jf76z@VJ`rNb_M^nh)>Pd{~RI>ZJ3~vrhN?&cpptmgVc&ZTJt~nQm;sB))s;*pW5ws(S2%3e<Q&&xdg6LX|Iko<T2681zE4BGVAaRiit6MoHFMP;?E!M}N6lX-WkeNx+*Fr!hHL4H4ah?VM4C_r^gmxXGZA563Fx#@fOzO!0lq6v=xdT(DFSul$Kv<PWST{o7+pWWaRBURQb4c!(o=C|!|x=5{@S6TLNirdYZolCOFOau227kNt!Y$cP3<!=mZbYT{MtHL!pFY(?y61=e3<zS_b!T+oPQ+qzc&VJ)ZzVJgAMtOQX0!ux%mJWH=C+MXZ|Q5NHZ8HOkFo_yQ;hXpf!5G2Ddy_3)#wWY;!tcq8fIBvQU@&=j?>%f{6tff~XYI(=qa|0kFBk_}CTNBn)FTe&x{%X-V=Z~P-Rxl60V|o!Pfb60R_);8CZ3t!_lNECEdTDwEoS0erf6D!iuUfzPG1`l^J;7t4{F@K^1;bAD58N~#Tz3PSXDsZ9wY|P`2c`uB6d=Q=gjMCg=9}*Cxy@xOUF&RQ12hi-ol2c$DuvKVXr5(_mm+swigjNC3LL^cPY#?GjKy6x-TNVlitk$Nk-o&j;APzH@=MVJ;ja)kuCVpQ2M~5wf3I;?(qe~CvND<da`gVo%h!APGM?}H<;w`ajPT0{zr1`I;n#T?-pb4H?9bNE`D^_yuKA5$z9;|TWtP6jv8~_Uchx`3V;i3R*>v^gvp)N?GqAzG(aZ3bUe-^3$(~jtvee7zRq5sMSO1Kcv)}!beos>Oi$&%yKILDR{JA$%`K5aLsgxZ*^RMAyVkuXZm&}RSFNI6R4?n|aN5cOj_WOZ5RUjO{WywsMEEMnzg$|qoSA<-UHMl`RhvdH~Iq*~!zeLC(br~?H9t@@_T2+&gFM>5uZ29H)7!4p`Kh`+rl8S5dAM42~^$dISR%C5@X&)RKxQ;%1>E*!5E|szI^7Q7i0I_*~7sfl99I1+p-Bjcx8E(ohDNR1*$4?bu9qay9*S0uQ&_mBks|tCn@J>GB$6=p71*##;?kh?$!R}(beH&6=?x;KnCy6}o#;2ph(sbNxHQCE@N%Ol9=aEzM^{8k#z3kaL<K3Oy7f&)gpvfZ;L$SztjnQ{H8T|2N7&(jQ(<b=Y2lb6AI+qJT=^R=7)@CV6Ny&cKkJohu`(=2i6uYfBm)Jcuz8UQud`p~MAz#k^4R(Na@t1e>FF_9H|8)I>!(Y#Qyq%oiKla(P2l)BPk8jEl`p0+bFJIE5*ZhXJJUt+sIpFA1DV`g4|CD<l4><o<4*vAB!!MVn(789mz_mR)EZ93f%uaZ8w&7IaweIWELw9AX(UlCxPmg@YnbYwBX9sO|hTyIoV@ZQD6s}BETkrE>e8M9T@}WFyfAa5~Jv<aPta-`lcb`nG^me#!*41-}Z{o<RRG(*6ngCAT3hRyFH{m>l{VbW%49Fg5DE9Ug#ZHKxAnYO-Y?t{GX885C6nj^vd^aaW%k(uMP)dL485}y_VgWu+u}Bt$TPm=n81IBUV#WPV2^!SSjYEe`)tf>nV{#W@>I2aX!Cpq7)9xilMBRu&gYaPVG%@VM#1-?ZjtvAlqQV*6CKSjbdicfOAZ6a3$72Ps2~x-R#WDR7lm~#DTT|{{6j|asu!}(l{GFjA3eRfbEeilX=m4NFi!<Lz@CQ#`8iDnl=`gegxCWVy9<@F5ofFGzTbK)yYP0|I*Lt;+dT?0q{>>Kr6FJoKny-_jtIn_ahHE~=Yt1Xwym_Ub5U7P&|H`C!<s9Xer&5VZ)aqfpxq?dXq7*7$6^fP*X#)N&n_2nBfBucRfntH)EN9)^pQ?!)O%oHu%|pQ`cD`-Y$608X9CU{X3Gk*Vr!}^*ZV16xT5{cRR(iDfvN1FfZUsD<0030a4Voa7m+8gYEd|tu4WJ9Q&a2^mMYI5fz|`9km=9ndABjQRhG5Si;tujMJx~{n{9%-g^ayko=($d<K#6D@Yzre3=Ioz%Yoksbvq%*BIOLbwbSvN9`jylSp*;b`K_HyES<^h|n0li(t0_R8C-gA(wVH5DpB2D`WjzuFq0cB4E+#PI5@yW@n4j~OG^+b5ENW1L)XEzyLq}L+HXb-Xd%X{N<aV+?TzxyNC}1IWKK-emhQSNY#J=X^*UZPSF5}mo8^3Noert|jw+3P+k6)8`dDIh<OeHNIvF>%aZ8@BPUV+b}`H}lo_aFG`=LyVe0l8xz7uKD>0iO+=;#I2mo=pGfh_Be9PBcG76o`MWE0EBr`6e!@QPF}+R7lsFrdeC3g4%jbR^fq?nc}O$FO$BBe0dC~z+}<jfY0+gw`pN4`-up6ti|soNOrLS#O+=9v_}s%<?!&=9|m^Nq{1ODD)79mx3IDjEFv=z$xj<GYI?D9erZX3&3U|OI#;I76E?R0K|c_<+}=yX>#IoF;Jp-=p*VzDO@*Sw{Rx(`QS(;e`1$46+3R~(f7=~=AyHVlLm?5%e`-oAOd<Luzd7j;VxF&^sfJ-s=kug65{%qdM6<oywN$8zY-#RY$Co>MiM#3HLWi~VcF>y-el_U3CQ}P;DQ{mht=D#8xg@)cS~as7-ShnfT8M)~Z)l37*xy(thlxZ#=yig-rDY&RBHRsIlCtF>F+RqANiS?4K+L#+Yl8>1aFPv<=^wj}1^<S3-<V^;fAlV~;IFQV(tP`hC`~*A0q+R`&zA3!9F3A>Pe6fRlcVX*$<c_cXL(MMrW@ekWX_y-){_d*ORRImg{N!H^=_w@gsZwVZGnb&M9!U}!>8&r^{7sRt33jUe{umJ4iALmuyF+=F5qo*0VxhR^D$C9O_1WPkm4bT<4fq^N5SIt02W`sYyN4&i~s$1h8MrqJ6R>N5WO*2eAAhlN!vbx6fX)EQx+m)KN-;BjVlyH1sYyYq2c5xo|2)k`I=!+5wWNSjQ9y9N*a29t!>K<YDR5=iN_<D_>?e3g&n%>Y>!e$j#rDCpy6z%*DU6zS~A`Z=x~<KxI(R=atN{db1Lf>Sc^V<a>f6z@3r5TR(ZypRhyhn{f5k0jIWNEv;5PUvsx-7oM+Cm#>Of}ak6=%&0>M6FlRM<$dV&x2j^6EW$a>T%Jd8~$rX0@QcE2{+rkfOv%;V!watTR*GD6Smx6`3)FPbOt(EO|p;VVZ{*b@S;{7ylQfQ}BG9vj?iSyY){t2CyScCW|-}!v}-S;;imFzoWa;su#g_+OCmPvqiG9Noq1BGYI$2VniqyJ-5l6<TKlUsYj<QBvx72Lp(J+qrpEIKEYZrsY#Kr}@cX!$gY*^qTroweERHEAQd3RcfNWJ3w}Rt#^$#PnAt=GZ-BhB9hOE?g>Xsor#0OMNEKhF^kokHU-}f;+5UU|&dkc7qR^;|o$Q-cX07DcUO=#dnNx9-w=5z`ktF4vQReZrQS#7^6`mtOQ)yYqK}w26-JFgCFWbeVL5e6x=PnNrNTvr$Rc#aeJjqdD6jrI194CN%L5e$t@$Lmc}K8d!05PTm_jAQS#bpv**sf9EA6I?XJjOs*s+2wrfQiIr`#Z`P(6H+?%Rmt1h1#MzBS(4UD&cW0u@_qF~0Q{Kix;gW@yuWG{jzOUzaNcyT7<)x-Mi7%KY763v&qQbwOk^h~jb-i^4Y=|;e_lxt2;9p4KA9Qgh4lDMeIgahxOV=uef>a$yI608+`dS+!uPHL~PVPQfvkt#&SoKIO|F>qpPw9#m4qGS*zMAcx<!8h&!BO!!=t+brGE<g4PWSYLM)mqMTE|Am{D|w0*5>(u1&M+;?wwHBS9m)MN&RH<6M3OUH#-69DoyoV>TAUR83B{2K?<Yn4hd=qww=oXBrt?ktxc1cZp7QFP^SNur!4vJc@QBYHXAXBab-2R`Nnub5^_knp;)=ITHSl>&vo1dO<|o4E{*Bkko$W~}w5P0G;?_nf_L?lC$of-pE-1rb#o|0YO~sVT@FKv%IAznK%o?fFI6@*K2_q$gUpXYCI7u4-0h~aGOE*CXusN~MCWemBhI|$v!=?mVs}hnov};ZN<V79UN*fqLo#%m=3m$B53=k|+VrEiXlX(lt+@&sv<WdCqZ3<%7uPSZCxbg$jExyOgK%y7P#kUm7RWs#^6*i=sZ*Xf1vd`8<<OS^Q<N`BbgviwLd%t>~#%&MJ*eCW%%DMQqC)*>b#=a*R7q=r<TfY`~i}Y|Q^tuBV<SgVz+Sk?%EqOn(O<8FEz%#@i2S-t>i2%DP;xBoQEV+NBd@v7ltWG9#B6P4>5G2t+$o>`o`pIx+IusjTRUWE?3*Xh7d$);X&X=|mwi`w&75VmCGcI`&-IhjjJVvsirDSCVBR}yHn8#zRMBveje<+X<PQRd<g&G*k4XEKlF&gLG{*xo4_D7tApIGNIR#9F&`HHI4e?J>)pPyy-0K1lL{^lOJ)lJ^0_fSXZ^ZnoA67u}$THIQV-PLWj6roNWxeeM@KgmxQ2ZYb_^xBeQ2C2*RO)3NAxTyzw9;yQOAhE|*TQ?ZFdywt>JoV{VhJE&>mY9FHT&L?AHW^;gjoUP+2ehov8C{fjrpc1u{GDg)Z(Zs?^X(tuG~FP*8c7Qt4_E?iK$$sla(rTiB2cvWp=$2k4U2~$-R*qa$|k^um=DwsDyIl{*Cdz0rq>HyA{}EaoTWsD!h`{C;v}u;Bw;zMiepr{k7R=>T-**RpgrcwhS4>yAM!tVc_%uX6)5qLk>}o0A1n)a82H!@tk;m(YB`U4+l5I1L^s!<fB!}9+Up4~y}7E-bz*9GFnQXY_hS~`xOh&znJS9ornODuf=>fkhzk&lyd%{U4nbNt=F=Ho)Pv?UO@5-IbDXPT%<Q?B=ebtfR8j$3UTEvAB54eR!<-5ur66Q;nYvli12F%S_+X6W2^q!Gwiit_`XbTN?(rmYzQiq9m9iMUbn1eK&<z<!I$W0Cp>flkT3bqI#?su6OcZ!bwPKP2+cDlPf8qB^6oe`s#xTexLTt$S!d9_#mvfV>8DhRSrggTRM&0j!P5hS^X;VL*(7fe&_bu4s#CC%M>!ry{F5g_9iT#puTnOqayW*i<GW-TxMUeD0oJo@cNoAXI!MYO+BO$K1fMN&pd_7cIw9R(fT_v8$BGf%KTP0{v(H)WJymcf`pYF+ZDBWEkGohWuT=*n=FgNmJ%C@XeMMH4cERTJM@gJnE_I4zgE?QKzaRMe`5@GQ|z9&+}HbqfEh$MKD3lt;`1`Y?+3!TQv8?6Qx47N|t(}17moaOz$u_Y_Yy1@%bMWR)*@u<zw`y&w^;jBjE<?Es&Q;VtN|M(fJs<4nuj^Za3R%V1dcxu&^ATK^G!V8l6rm4D?wm!o|?<ZE?6ZfW2FI@@sTwzqb5baINE6bm#@=E%DZSt;J?R<*3>=5v6NRU>|X0DmSa}u*4eMz!$wvVr?qA#ALI7{5?pirSR#Oa1E^&Z>Pk;`7w>n35LT+)Hz8=*%@qt${?(isGhG7w@Xz>Bby6*+<{@xRkU#Pv{Cg1bNS<`7uP$E=b;E88&3q^$(Li6RmzM2?UHBD7i<%aTQGxrw)uJoH7Tfnn~jYlmTnh0~R9N=ly8X0qO{g2Ob`ASeYHM=-->@24z_L7B1kEV;PKG`!7vQNY=VID)EFV_JOSe1T}L9V+_6G*3q*8|_qN>|TaKP*~j9@Ij{hFT3CNVCor!&$GX|LoshBRLKekKW?2^Gqd5p-#ckyH)^%qlEu2szd7*?Mv_Y9=zPKKd9}xmxfetm{7T`Ff(i`KHSMu~Z6ixn6l%p|1km3#1o`Fwdfmfayk(|f>5b})Q3_*P5k(;%5q>T~@J;aO9O*tRnM+P61AQBX8Mozf$lrL^XY*`GgC<yST%gJ}p_p!+NKpkhl?4%8f*u8+IjAcbjjMsJw?<1vUBVRw!d&T)`&;j$L`H_H^I}Ia8mRKLM3%rmRi9EcyZA)0BP@m*a-gv~u98)@A>tR(kh`WL-@CO79_t-N6>e*i6_Z@HX7RKX%A7b+OYIi%iD=-=5jm;dR#$4bQ7SCr+y{U$-=MiLQZ43U&iiQWBp*+}uK@Yl?3M=d-vl!RN^Mf3594t26S3d@Zy(ZGYuq4w{Rn+{h3)u^vsS5gdm#%C*+K%u%EWBXPE01^<0VfG5*9uVyv-`yYF1)~77Znvn37`w4B!%?;M%O*fOfWPL|lsqW|8L(KikF=+QYUuUj#&#&eMS`94F0Q+ii2q6rOj<+hH<RVV`D9;mwC-3TIZq|I+cUl*i)k+^&>;m?}N&#XXr2cIAJ!RLtXTRTQKIXn)V;&7ypsef<_;&I7k3Yz@8Jv`BRYA_RK+3&8s_^7^#(3+!=WEp;hsB4^w8ao#Sf@L7T_s377OnWPJ!Q=l(T+fR6a=bN=o&I+VYmPuVu=9&_dn%a6F2<7~Ew~WQ=o-HZS%D_#+UpbeM1P@Z)+v4PbK3DIB0cY6TV*lV~WcJJc^cQW}M~I-l5udbj4V&{)!);v(!}VDuN+MykjjJlWG5<A;f@=n9Nv#ofWA7L=?lA`J{E^Dn5R_JQF`pth4B0iyC_!yl{!2B=t~Ju2NMYG?PQ^iUn1aJaM-pozAKk$sEVD=01J+|DTN1}lm4}y79!?aX!81pn8qu<>jr`4@5=hM@f1yRO;{v3n;As*xMGa4*T4aIL7%Wjd2@UK1apEQrUL$K<$xRqAiNP%4MTtb&<f(u|RUlqPBGFqwVR657uPehIBA$twr+z2{VJFg%sWs!aC{n{;SpGy|5C8U0hO=-%YXlRsFI9VYU2BBS0`;4kqlwwhltr3wf|sSNNSjK0X-yHP6f*(K+E+^%XX74$AI{LRIflwxj3twU={#sMM&wSHZl)~q6t7`dL<KLo3{!EDTN<@O)%>;b8vd;H9j~!-<bW{`AR1;rLAM6`b7Nj-R9er!sP<Tze?P)LETN5-O~gGpQP?AFa@p`C)OyT~y>;pUqB@4UiEoXHcu`buk$E{lb8}-LeRLM@)T2boxsR>88Sgw;Lot)Jycl2X<DLoH9lk>9Ty_$Z70)Z|&KhNR>MXufV>0%j&pmEGvgdZE2ZBVE+E%Ryz2?2}gT{EWK8yv7HQLe~if%h>j%sPjHzGv8QKkIxCn+Z9HTl4ukV)1S{+H`?b$QFYXL3p6Jc%^ZT<X}I?+nX?WKl(t)mq{pnCscl+)0k)4yL#xq0n-JzdoS6h?CrHaVxjn;7qn7ucD>pyODfH893Z;kk(zQt4tZ2Ivmz++lGES%F6J&ksMg8xO7F_aKk)8L?vr*4Z>Fa$ebhxKE40Q{Z+sGvFjgvMU@`v%%}dx5=l(lKjnT5<StM9$u9qc%foK}-NAF7oaDm4xBTAWBXqGg-hRTtuIfowg2BMF-V}3J`OE*U87({Tj$b_Ch7H-1>xnEC;~h*{e8uwg+HP?f(T)k--6)`&9vzL-+guaN0?5JqKQtd=34Je*(w}>4@+>_)>NNMIV{xRJmYq4$x5bO*zE^J?I~<2pFP-PsI<%rZXKq0?!`U1_v>P_@*oH%ItU@*`C|YVq=NZCPlUDhPm7mdV9x$L1$!cxXQPy9Zi?4NZ)^m<5fo9J+vdB_!$MpVAJ?FgEI4#$=SozhTdv-K)s!+_V@)X^A8qL&Cie?zfZ1o(xto0bgPzA^0n2I{ZjN(cc`f&u4&O|T_U%H_z4)1pszEsSdcjKf#kfs2w2W}p|q{;9zaOv*CVTf8T4SXsg%K?}e+|=*?l!&=sX-Sb(%RFRhp4gQ#?E;uKrkv|aX~(V<Q=t;H>XF8jc-)oZtt*8-TWL&b7|FCOw5wfPF-om|lm%76(Hu4Qqg0cAl<EonC^xfy6bn=0`;1Zk$E&9J%{Wbn*c=H>_+$r8le*~0$M^`XNo|-(maoE`(}bCg${DRmd_x|iU}=!3dM(>7t-8hnTQ}B`ud*4jX-?RIz&e!>k!>hdX*!dL$)n&qfDoZ(7NAg`*J&vSV+JkFbRJWg5Kti=6AN+4W|HR-dMGft(tDjs>Cc|wG0MS22aA*L3xm-&^H`>D=O=v6jN7fSquD`bg$wqMp}>LR1sRO!RKbpXqV8g6ganDvKqmu4AZ>nmAZ*qbZUYIcz-bGj3$kDW-Lvqi!rd)oLw3q7(y#AGYqUGq4qsS{7!@B3Vw9irn!g-)D#Z|1P|~R=KhpDJFcWsXo#?j&!|K8od&3CVywsiEbY)}?`Cx0)P{MC>@9J_kCg;gfB!Z&9@sj}}nd<Pqz1D!HMQ>LLhO8n{g|fUm7}k~pqe1}%8c{8a(wlZ_Nzs|{5CpbP6p~44Smf9dT1sL@@=CNx6}2F|&>~29+mc?)3E;+kvW<xv(xC~+MI^eX!L*&R3!trq&>*jNvI@|aP5s)903SO0^>^NAN_KQ8KWz4^g}WIqmCEKmPCN5)9?O0miRun@GImCdMY6GHrT92cOnpruOw|O!lu8;bTFtB-5@64%nJtz5%3CT5`=P&{0IR}n`dTKye&;p%RN~%O`KE7d-c_u18{f-~yCtHmN)#w28Yi0&sj{jOv{n*`>%8uu(^*q&tEci7;vnG>nV)a4i?W2n*ybiljSM-H$}7<T=GvM-VM_cGcf`4gEKN&t92EWd6%1#@O1&Vae?jD8OZ<~+c<OgCs#_Jz3L~+RGbUq@j*0VE9X1F7@r3ym0H&ycg2g|!<48-lMTZE(I<G!Xe$a{4i2Zw{`(ZEzdneIqr!EhymCBhqX{t@k?1oNrTFXA-n)Ae5aDL$y{`(g}t@kCU6<$wd;N|6O>odH(d=Y$mk#c$&;TN&27qP4tv8)%dtQWDY7qP4tv8<mtv8?y|@7oc`k^s^0S%`F9lF6F4ALXArb?zn8#bVaD<`19<NY}d5VX9TtC|T~Ca-J~NG79X_dR!eVTu{gA-6&6Vq>fd)nUYn-v-N@#KcbFBt@bw($eOAx9cz3^C#t_Jja9_x=U>W4*1B`rR{Yb-N-hB@*f`V03XkbxO)s9PC2Dq*dz{?DsEAd$SOj5?FaBhN**|mk%JD=v72}|JB_vr?x6AmB-A*`vFEcHynGjZQ8efk}U`;-Ldf2f97O`&5B(U%V)z@Pc$|)d6JS);k(>qhmE9XZYp{cUa6_p-e6s63ioQo{^@-kEf^Ltgw>B^suC7z-?`qcP~KmO$rrKxjrL*w1~vQJ%6!3xFTKl9=*9q_Eb3Kntlr*P(jN7o##-qHN8F1hQ9SfglFI4@)6?ENsjGiWYN54(1%iDc8W?!|`4mpOU#aKmFy_L;I^!<$bZ<m>WQ_71r;X79vvqkTGPGfA#N3+{r{)$lJ%SMy5AUwhA*H*NAm<?i)Ft~T#f<SLa;>@#XNtRW`R8cs1GlDZl3WT7IiC5<{aEz82oiM-Vya?>sWJQ|9?YqIeRXHZ`%0*~4@CT!DwsD8;`%hRW-ef@pIRD!){544dVz=6aZ-f%)KdxF~*taD|j5Xe1od~g6BY`<?&L1!QJVkB5@S46ukOhTqjuD_ux5K*GcAFXdtB9l8Po{23V2%LshfnhpBql<mDHWX~E?|g-q;S09jQ-ve2ktb5-py0|A`q%(&H$@63ww5ozdjO89dLe`vzTzuhWEg)?+7lyXmB#@Hd4mOS$%+cjS+vzesyT#y>Es9|3UB}{PfSFWVqRqOTcVv=JfggJcGM+M3J^|J8|f*|@jtz$<i+aTQg6{>eQ~K*lz^ao!};E+)78Et6s+`4*_uz2)jm*=lm*|g^&^j*Nfg<F7h;4<E=>?4(*@s)aiJ{xTGR_i3!cIu9-VLFf?pU2j4~Zwv<gHD6iwH7q;NH1P;eBMMRT|$CcIF>5Id+~9uC29rqH=+&VvjWXP_WqLle+^C=+lA7FM+F?x|hyElso%3OtyMU7jrIBWfL>FGDo8R7uGLe}D#!uvy7EG9-gg&|{1SwsMyD{4Ux83EM#h4}dDDy`|Eb@+rR^qIFT6Sq2E(BJR&e#@ZzC#J<7#>!`AaFEvh$ZIQIw2n|RPIwA(G5iVI5N#0pNQbdMX(x8{Sz?wZ^qmf>ouA#ppaTw*6>w6$SR-iBT`SI2VV|WY93e<bvMSkb+zAIQ5cJhlDob$>}mx+bi?ihX34Xi?pS%NEUe3w~;L@Yg}6v~sON!R#<$nW_yGNBW;G+&s6+9Kp#2wP^%X=k`%3y*>jF+>qbFh}}#=h)I(F?0cvQ@t*S&<r&Cwc=Fxe_lWuFCdK<EWyjmmxcc_!Y?EIg4THKWq6H`zW_E~02?oWjTgYi3t-~~u<-)ecs5|;<mUvZVObFUR7S89Jab?yh8u~mpc=>&N%OQbZa0!h8Wp)`aed(mr7~J_Rc-f^`nyWZkApX&AqT8leT?6*61>Xv(|_%pL~i(@5MLK8$4UY-7eN~2#5;cH2*u&g0Xe3JA(J#YiQQ2>J4UxQy)R$LREKLAzRMR58eckl^v)C@;g2v9E8{<B%F9oo9Xitc<9|!_++L1Ik2Hlt_>z8~06Zo)Wk?U*Y@FQY<2P8A-Y`m&ThpC7ky+|CTLZl$0VVt#<6$&<!<(*jgt~BY<97Ubk`aP3zHj#!2HXpC(*^YrPi9g1h=D8oc(cPj4tG6HU|~fD42FSKh!~M%J5!a3Ial;pS^uqpItGY{3h1hyPyf9FqOgAlxWainLpVZf9D^K=fF<b>XooZL`Z-2r@@ARpvjdKfybc$+h820V=zsN2uN~lL2VA*@N5D2|a+29$Bx=3@8VSePiSvIwI%a^598HhmfTOu|3}7fA2bV?w$?#Y2M{J3opd*|=1BCDsAjHuHT){XU-}?*@5*|JN8a^bRhg5~hg#~|p%un$-!>rRl;WpDa2m?TiMC9nDoDNQyEb1#r5`P3H@sIp6|2NE&{l9MIs2d+XJ6nq?g{bDTrsj-zhz0oNjOS)MsA<;o2Jrmm?Wq3NwZ3hRh;66`+Osf)c3kciiN&N9Mc;hUtM`(xcjRP`bqA7|mfrG~2!lptWYmpWXR1(oLR}xM13@}KEx81AaFm{@*!jUs9`@dF4Alx%9~StnZd6Be7K8&xq^s(qXw@S4b0u}zP6|b06xo7Zq;<y7)8w&TK^3kwRX7r!tY~N(2kyIHeVdQ#hR@0qnNrWFqKHY9@ByW?;^c|(__*dH0<Sfo4J?^X9$G$tU?0*$vAUnXqMJXlP##yL*a)Q@@?+Un_N)j%2FH{=sD#Vu_>{uQQ^Hs;jq3%#j~)D@$_R<jB0WBqg>;U>p+yndsG_z`waW;-QwYH2Ik~UTKZi{o^FRMip2JYK1yq_PMp6%qqUEVPgqv7}@&sBAKXF&%6VRH0`Y;$1<XNT7RNl&4wUR3~f(MrzU0f||I%6n@SM>RkGqoJhPhkzzD5Z0?bmIzH6#WWYB$cRw6oG&SMvEjr$+V?EIawIp@F++SSwla>Eq7NJ!@uyBAHvjXwdY3twhZ}ZI^A)-tpt6OB*a`l8)+Nn1-jwc-ak;GtvI<W7=#B#bsW)<7L)`e9AYme^#r^`pJ(lZTMPoaFdDAbAknZaR)FyAzTy7VQ^_oU4)hZ(Shql9**m|CvA-4XnzSeIOX@@01(64{cs?VNJo}TU-=eh&_W9#$Aa;VY{S^ckZGlG)A6bOEPD;WN0-quDHw0!Ap8@a(lpph?#rg)I>=5=EYupeV>9B{5`9jJE_pmYe(*xmJlK-h8k4WGcz4|7E4K{<Nhb1vFH}DL_`VZa}OB}Y&3oLQbG<BX%5m%EUF3c(7I?<K19EL;*=o5-KT*ibxg?ijV8xY$?HtG`JOqB3Q7grZTl{y$>+(4*eu7~&%Q{Ll7IgC`~FvPDCkEyN)RL2=Ty!s5Pqp-&{MjaQ4x>|}ij&`UPbzC4V+?%n-3BBP(C;PP`ko)B)E&hB52VfNA10Y(fJeyXeQOfgh%?$~>=#)1)2+U*Xu*KeF6I)^?8x1)Jxb8#U;Zw~`SQ8kFSrd#b3r74V+<9Oo7es+|2U2Dcj0KrZV5Th2tVvg#ZC+``flE+DqAOS7p^75)0md@#C@a{SRBVlOzk~u3X3ZpaNeS#RBjV;j)@ed?(4nzqI?SXDBXETI-!1MX0PTefm<{u<jke(P*WG(;@$&+=9K!Y)i$7b6Y?f_95;J7Yio;~hr(w<8<|Il!?i|^*Xl$uh&g89vy`=JN;zpH#w>n+PNJ`daCAY_G*tGdbu$LC|#pwvIY9J4>E-Mq`ytCEVXf@vC|CM!^-z37<mSVEyx0GT*1>jqwg_nwlP+8_@mCyOlKW{U<cgB<`5ey&mF1+z0(^R}6f3+}ex13~^CLcYc{M&7K(2astRk<HaiKX%j9zqR^5xej)53W3AH~09g;>h~WiKT2$*eofv2|mt8l4+VSXk#+#xved@CHk#V^%W{_(D9HSDsMpK63?#GpMKJ)+yFx;WG$57mVkZN56~~Ft2`HdwTao1KoFtzRUL($ttqz(4>gfRw&pQasF#6);dseChnU@#&L}~BZ3`G9u7O&?)gnr~x6@bDfdE3N*)$CgXhCh%#F(c-1sP#}uyR#HG-$L2g4XdPZ1$`7v7;&ye(yoIl|SBgI8_2k6kx3lz|t-cKUP@{@!<wL2BfE{d52(x;tp6Ld4l%%h-)b|+yL)Q7214~JgfiGRS5Sv{PqSsYZpk?7$={CxASuVBfmRU$%@A8TVm`rg<8n|GzDz?K~Jw5(b`zlHPPB`iq@uNZp(NfK;uHbY$Me$@<SO&yQNE9$U0{T?Zr8GcBwPuprZ*>c=kDLHX!S+stP1~9S-V9U<9(PXS~17KBfU#8A)(9w-SgZe$M|UaN#vKj~w)1BBsz+EZRi(3CS*(M85Vd9@<wS{n0#M^E#ms>=}en>&P#IUp63gYbz}3RrX#}ggiKxrJj7A0^b>?fCxxA3-at~vk$+`i!G6$GfAE#KjNMwh_65jAC(&xF8x)*grT2FHUf@YhaNMB;OY=wMF{C2!Ou+ct9+6iWj3V`#OIJJQrneEfvOTPgh6<o*T0vl3eU`0uxPT+i5^_;IYdNL)h34ud4eEWT`?k*xx@5gI|r6W4(~B^h!RpzPCZ7GZ-i4$QI<#qKDRzE3CXp$16nJvW8>m=!b0ZXzbr0mUiJ%`%WNRF%(3KCZGbbzFLhGBs3ar6@QN8(Gpc5Rg+2tWPg^PyXp8|p8q5R|BHZ3;_8K&}_w;H3v0TB$7gVp!x50ol{vwMArqqbqnforMGc-(T!0)l|fi=HLeifjb71(X$IVC(5!fIOeJiYQweJ{8biThs3m~w&(c8nPtK!Lt5b+jaBxTD-MKcy;Y-cnwXQ#Wr5uL|4wiZrSDPG30_7;HzEmEZU-9M}Kl?MGLqiAlAl%z4rC0n6m$G|zI<`ck#%%?X`#zhI7MucJF=;x?B{#<VR6c}+tOZ9aX~k1<v~sJU4iv-LfsBcjT=%%J?RDwsNSJw{X`2X|K%!6cS4TRg?ar{gGU%%N3EcCX>6?TVw8XrEJF5zCTBlfe64w1FlhX!!{;D?bW%_a7YY{%g<Pqc1u0`JMHIeV?k+Ij9!<{<0Da>SKE}io33!bWw&lq1Xlms(JF5CLFDKI~C@RT(BfP+c0gLG*cL<$krNpFOs83gdk-L$1N01KRA>%a*Un=nF|^hFN%0k>5^9x+M*|WG`4-Qb~E!@uO<ysJ)HkK+PnbmC4w!w@so+5dz@|4fAOU?;RRFwf=7ON`7**UBm6SLFI@{S9Fs3C3qQ-S`j>u%mwttpeubZ{eg*1}JhkD#o$GQK-gM9Ffw<7SU{aRP>|L<Ei6k3OY+{&nFnFQ@hbD&LBvTAPhm#C?5G!Gmg7V}@BuMZp&L}6NpSCPq=~p;zR_KJ=I{vYAw|WT50b%VY(DE5)<j6R9`p&e~APr)*vt#Bolk<=JSyO`Zv+F-<hL~|!k`_+&_>d+Y9$Qd=xZtM)Xn*npq}`9${P}H$cGAh==i@N67ZkCkDU0N^9l=ci_>tPtc9E%E$;wkpbJj6%dcntBnBkQBGkAY~h)xIp_~mh%LM*s)BNoCpL%nLs4H>2+kyE_Cn}CAP@ZN<JjQ<?SKLFB?K=)^{?N9wveg3e==_DsO^iz&N!|&I}e>#5o{Of-ce#f)j5*KM5{WZ42*_-VX*c|;ue!(&;!Z8xxUt?{Yg3X^urWj}Bh38u?o=ea;{&g6WbOO>JdIHW3so8;Z2Uz%A{xlmp?_xS0&!e%LzAQI>^sj#6yq55Z|4pyzYyAVTE!77u=X{bKiix$ipPo<9H>pM?Ig->W)jfr@@r^*T03K3vUtN)54;2Jd>S&dt$gXrP!v+|<DTBxIi%2(p4-haUtALx5C^-fp8Ys^wdiz3QCitF2_&Q1Y3cDk<*TkO?r6*O>w!x&KKmY@8I}Z>E{8M0Cm$5ttvD;x6@swDmUl0VALFbuSbV3xOvE>HALZs-95?7GGIxpi>*;=p9a%+kM&nC-Q!K*M9lC!OV$iV5&0PubgGcT<2mVS$FlX{^%GH8b(A*p;B=~v=}fKA)5OtzO4YzHgfC66Y4=~?3DB?(|QoZ0p?{1!U`Q6z$kDvOktdGT>LC$KZ|A!(pcy&tZ8?*ZM>IHckDXjc+BdpK-Sou4c+OIhrAljH{n>QXDr0iGWPfy76k6G{@WQ0~-odf475m~Sw0ML+1vn~Mj);n2hgL>~YB;{SSApxf4D#p@%=G-4Ur;MeuMARJ;nB|mM$qK?9L19uyIyJF>*g*Bq`fS2tmQKs<$MjK;##{xxCbK9$&2gF_7YUEJ4o5FAvF(&&|>2e{SK>n_9Qjlg2vs!T?>Wg23LS`Ij+Y^~A3;MPmpto@#Q9F;jJ;$cTDxo1c$azhKg!N;}&4+maVP}k1KuklAk{VO_6?JqCv0&;3Evko3fN-|W5C>RE_%Pfofl~o&2OmeqZHek`l%Zmm4gUQY3W%@-Yanv`LI_5~G-K_)qDLlvP$faK0jN4$(kqs!D?%TtQjTWScT`NiR%iCtFcUugyY9DrpNHoMBp&>vxPv=@yL;>wsa~;5;{o6Nu!BjeQd(xiy@gUQfXYzib)Zk(gJKW1ckl0<Q6mz%fGU1ZslPnEZ{S+mXIt6}7&U@u7kpez0I^*pf9I#r`SX1;ZuUI%TVaX>-lx&b|9z29z9p!eN`#F%t>im}(lObRkC!!VZUtCF`Au;G=Hr?&<$(<7iGXMfH_F1bBYGXPv`fD3!LR9Y60fgL)L%?3V#NwjNWfsg(1<fxi08Evw3M*tqKV|3G|9siJCCudj7bn1&A;S+liPa!`FT(&*EhsY?9pM<3nH+HjT5XIFL&C?`560>Fu;I*gbYKUT)&E1T5E7dg5<d7j@FSsmH<eQUjlFdrp$o3n=ly`Y!W!^X$~S`C%v^<<$v!JY*Qlg4uqP$uPS0cXm0W^;InOgwFM4fM|Fm716<XfMfc``FqMNX`@FE5iVlni<Rk8Ro+@e?qcLTN9+cK1KW{P#zyGd`_Ec#0s8b^NWmQl-Z>3oR!*$dzF>97+&ooPj?UGYxkeg+{+6Ch*u%QSkqd(Ug(Uhrwg5`P4IFE|6gkIC$VZ{RUjzNy3UNu}#UQ!F7#Gcd?k<Yli+!Qge-A2P^Pnseqh5mlqA<{qnboh78B_Hz=1>`&S`)I7QB9>TV0^~vZDDMv&z+bnn@W-wJ<Q|dR_sElgw{#6S6se@q(k1DMw5Rt|XdWI)NS^MoQ>_L3rcqs&zNKy1%xf}kw|ukLQ@V!*LBABQLCtyTz}fdJc^xhkjO6F>5!d7%e9U#7)>xj|65uDVi@M>O%)@ZYUpP;sX`5~t%QO(Rz=TjYcx2F#|J`txr9X=E?}!*>yc}0FGJ!hTRoL;m@~Qzpbpm=c+lREYR9{UJgt{TnlGYN-uR_!Ct^&fT6&!WJG+{nT1C(R0K&Hk3FEQsrM^rglM1eMkE_e_ioc&|g=9x^`oAkvnLW%aGid=gY^_U43WLHS2Hjv5%GBg5+9_X^*#4WUa@gG}dv9+S1x|s}l!y%6x@;uV}JnF#D(fVaeiU=?Hd!{cr<ic@c$Zyag5X)e9OeS?4fYk8KY`kwd38HJ49Q95BSw5LP#(q6miB|Vby_*{URtr3nPJOqG;PEEm#`-VYHzMMxeIrqJ{J#%{nu4t1G(<>dQ&O0YEfBd&3=GCqt+zne2JQNZJi8_=OkXorY%dP9*CI#vd{z~)$P{6xYB2|vnKK%|Y=N=GC8F{ONCTP@V73a@iQPi9&r#pVD*>LE^8yKV7yr?xM(jY3=S2bxF!|(9!u1|Y$S)ZBVl?75O;Xc*O4-J5yAqE@v8OX*jg~25m<bmjV)!VHYM20YcKlf6@=6Og*vh2n!d7(5PJn~cEPq}zh9~-v8IlkRFADcb;)F^20pwt<hII@-)<r`fIV!qK<G(eP%4;oo#%yQ}l@XJZ=dkL=<BfP=;30@ZV80-wT!b`6yrJN5_{Q>)^4X$;R08J0bHF$}SOm*`o94s$f#oH{WATj=^AE?A69&7CVDWGXlE)7YCk(+)K1k@U4sM4Scyid%&j@Mkge9F};rAqeVe$D86|*TrTSMjSE8_5_ObTpE!0(6bNg2sJL{)7_avfi`A<dRpzOH2XV(f=YP0nJ|BygzywS3C9WG>RcFEX_Dx>));IHW_C>Kr@8L>EOR04umWAdeHffB6D$Jr-8F<HF7B<J*O_K8H$yy!H2`fiX|LJv^A6=nQP>cUIn6_^_j!os?MeV6tx|A#rcrR6Ewnu=gGqBB-;9l;CT!!lyf<y(h9B@3glg(tDJ`f(3>b8}BVX17*P-z5;<XuQ14cgtr2ZpuK1I0g4-uE{vKP8HDj+A&YTf|K{Ee0%=L<@c-Ss@$3VA`eYS}+Y27}25#v^6^U%3)kj_Vb?~*DSR&f8hEe=^If)yBW=2kTam=%87tKM$n-~1P<&)IE;jvG(gQCpBN{Lmp#(Vka*ybYDWokQMA-5cP2{6-dc_jIm&MD1AXT1<snTdIS?Cb&%1DT<uRb8n~g%{5x37QPjCM-#kQ1L4&b%_KsUbNc~QIUtA7o%xXcu&vYuFX$-pgf390+jT40UVQ7#3E~|?=d=9atGfMt-rkFtM^v5qKjSt*b9tXH;f*Be~*6qpG3%=hv7%A|A=e*n@oo22feR(q*MRkYW{QwzmAx*{hDoud4Tec+~b(K@i!Gdl_Octd@x(CF!vwWNrVkpNtYFz6p;bsac&o!ee7fWh+|OQhqi_ijMB=1U7U#F>1#Y}&|Q^(ZXLcu9A+za7IguwVYT>BNQSYa=a8S+%@&FEJ<cf`0R_NX{2Ud-&^++)w%j7R^;-QQVYSJB_3U!YcY$}d_iESTw7NkyVWZxw|M&$m{{oqR0mHt$d>P@F5q=rr7s&hzWc~#*{{oqRfy}=^=3gN5KkbnD0q~CMeEl5Myg&D5D!)`8jPZZ?tnl*AyJN_FJc7&<U+=fUkj}g=RK!)9STHGxd@2)OJ`v1W@bZPtegdF=Pk8y=310pxx&J9r{_Ib_O+O?^r<nJ-P{DZF1%W<rcg=o;f9Zssnhep65R6gfAa?<ZK1J3K2=sCbcAa5<g(Il{QM`P84749nh_!*`^-G#z|Bk8lC+`@~zV7t&Uw4*dKg=2S{ZwzDFzlb;=)=h|v){cf^U2qd*D0aM0gw<=rq*0?7GHltsXxU>AH&Sgap)gG!UqEPDct_)|Gpl$K0Jo6KPD*mBk2ATgZv0ozkI1z!1CcO0q`en3fF-4PlcAB!0k@~<3~{ODQf-{Xn%?jKl<$O@+_YHq9(z~`_t|RckY1m(D(v!zw(XO!S&aW^`Q{ZPnHZTP{+V|e+s2fZi=#>VCsh=>gk*1XI3HDc~-Sh9=KG}Qr&&d+k>2YZy?U2+E#s23R}*&xWPO*5TeWQL{(m>8jyU!q<fa_C8~_CP@yDFDqNA(tFVTkG0BYuD&jMr*0xmG4z`(lU+Sa8E@W%f6*egpC)2b?&J`?X8L&d>2?!ir0xbyAECcMp!n2TRz9Cak94lX5C>a!!3^gAr1LIpIUIh@M!iX7TJ?5qu9#80+FJ&oDNq3c^!39r<T3d*Qv?HOMBj+THXmPujASq@H!_vOjBxc54(c2^QWi-5s`M~m!qYVskZjhVNDydYVXK~Q8ltzNLuoP8M<y3kLla2}xj1t@>s-BMpwS4Se_*xXALR}gf?IDH%0%w%8EeXd9?BzX`)#4w#D*^H;HuFS)yh@%Zu_tSgFNg!3Ymjd`g5SyxK2lg;)F1~SsC5$!a<Zzm;j#vKV!8E_06F_GMh$Yo%$0VW;4uZX^+lCFUu;)^nQ;cpEHdOemH0c2Q7eeH5#`@lM7O2_<Sf5yRVNXdzm^91Vp;_LI%$ym-@8i6b^*1p1vdN4-0Xd<E~6HRWm;DzPSW`q_1`f}VPjeg13OziHQ$uIXwyid+VTu-jg5gl6~@ulu<G2f%qtUI0UiN-@EPy{p9v7%LLO9wRyB!MHE5sCtD)iC3c~yLB3C8I0B$b(E}~gd>#L5Icdfl3hP1817Bq}c0OAEMFgE#o<7`@xIllCZ;exLc{Q;NyA!pOS^Caldw@C5n)93k7KSXhdllVM_Lm^PM(Tep3y91y@Kn9s^MHs_hEL4JtkPF!q@r$&#R90)!brR0tM7zUb3*m#ryULH$cY?%*Elw2|J40@-X^*6mmd{fiIJro2jH|jO){%_nhdks5wv;)8?g{tQ8x|?*8OAlB{R!9z9&;-U96q>I!_kg@Wgsp3EyWRn-LgTP_}4&&_>^LOYk%!P)NQ>>oINr9Mqb`k?d$InyO{Ts&xp@J<BCBpcloC#iD2WpWlXCwzyRo?*<WgLAgsqW!Dy|el#8{T0J0o6SO92ld@%Ox9=()Y{5?;IyTGVC(8Bl27?zYJv0_qOw0zF3kq=1ZL|?JU?##~Go7BzSCqZS^2uDz2GWKsYd1~l@B;+sH)DYY(`0-XqIrW>kw9~-=XY-e2NXVMLOT7(M%L`tBA2DCyCRhRv{UqFc(uRK`>c7fXBT?xBy#;tUY0Z!oz7dg}?Ayz;y=^$(8=RqC7``+=!>T5Se!hr5HtU7SCU;SKVFZ{>*;x>V9CNFgw8OMJFbwzF81vzux=nJMEiSpOm}1CNU}e29wg3Owdy`n(y7f9}&0@_}?6u3YPx1cy|Nnb_evY53KrF?I;2?UmphF7<iBc#DLI}wYGD>3X5U`ObWg9yrAQ1%zp@a^?4H|&3l+Z+?5n2fl1<?d4h%R%C@y%82;uQDZ|K4Z&Tpb<lyU*HduQk`4-~5X4jZyfl<>?X+7)_?fA7V8O=yU0IOkdH$L_%y<N1E3B=A9tFL_Ps`PjXb+u9^}cy)5>?@fg7Pj!yxgjl<e4@$kUuxgNc@Roqpy)x<fjDz&l#c^oROuJmU<f+mf&thKEBa{^7HM-?v%G&Mz_DUJ$3wFxx&6M?3t(n+kJh3T5alL3a67Sc5^*hwtZXs*IMZtxt6KvTX>csy83e0qHc!gz=>u@^Ccmz!;``DQloU}6Jg`z-<-#vGffuf_JCml*BIjygAf5(7#_3<#L5AFlp|*U|jnQQWE#*?)e%80%A}|NOJUJ-3uQVjmW}--;$^+5--D0J@I<J$gE`gmK>E{RgqA=YiZ|C<VeBba4K|O*L49B5~h)VRo?xe?eC|$xz`io--eFhco;Eyyl;d_><S44%qHJo!>8EC#txu#P`b;9MXo^dNq7{zxg9iW8a$-?0d^L5w35SU)PNI2;xs255W6utIf6sy<l|8-9ltmP<18tt^1sqOt$m^;qO60i?u95b0OeEX-LmQ@|6NH&iUlWnJ@S|zX;Gh1Dzx7-MA4<Pa`J^ZFA58$Zbl4Djl(!F#3FCCkVKkeiGYLgpxM=Z$7LxN8c6KAEfHsnkfj!=4#>5{S>W_+4|C^>Xld^W_kvm_T~6!JUCvcLq@oM9_L!am~#dD9!m4)c#<@IwW3b`mwn1%0&SOkf>)1;{kBQOZLjsyVPm*``i`GvZYs77jc4%Fx4SDqaF!{SZ>HHe%r3yq19L^$a$vn--wpomXTRN;!B~Eybsm?_<q4hd-Pnb%D671)5VRT}N0_~?yf$?|Mrf5^oWwfdEjz>ZJNISf|4`8(%@60{x2qR+sjOo5qr!J)Uu6>kF4`fU3O+j_+$(z_z&qLF8QywZrWPzAk{{98qUHB&dctbxLs@)N^9AO9)ZC>0L!;`HvwmPP8mQG9J6xJh*uqNs6ie!h9VKK9@NCxf!PEgv(MRPO9b<Du{XJ|6j&ZswwtK|3uoQWA)3s4I&TeIj>w1b^hr(76W=$n7+GzvZbmg1HSh_IEZ*@(LR!5`^aXvm#kwvNdm5VpFe|1cg3Shji5KHG^nvPe|<2(OR-u{N4pyPDU*>Ov@@ru!L1#fy7cf$_sBI$<ROL;V)LW7paFdAz($?9L`@4c~>x0()tQ8ssdxWhNtcQmbhMZp<*L}~C%T^))BYQr-JfZ%1&NiCu^plqyKMS@9pa8*Qzyf943Prma6U#m%oHJ*n4e7+dZDWEkL6H9N(N^)VbX-rLRTw^u-y18XH3lhvItE-~c@@{55E20T-qbV;hdZx$|&w$B8364e|v20My>`p2jw!X+RcqV>w+<@2r%Qw|G-5~98nwx`{k3PKYdZ!ch1NtKivWpxT)>GfKAEgh-!e&y440T#cQzf^|(3Pw;HszTBf--bX>6=zhG(8kt+o=Eo^JS9;f<(jVPGFxulR;?Uwb{0QCWA0FO*bVs=cnA<B!iGBC7MrnP}S5U9~afyypmoO{jXb=to;QIgn7Dcbv@m-`@9K~A9-5-=G(6NHhB6c`I|rZP0HVV`$_qm?>!-ZBhH1QeG?g~4b;BLtE4O1H&NO*RHzx{Z?OM!`;!7rccy^j&J}QKoO~{V(=J7DddwH?jIY$eiKhxUO;Nz9Y5t{vQ=0-#wNZY%h~Tt^Ghi-)6N?B=q6p5mo)mEM#`1WofK!Q4A{7OkZl-_(#R&+}O!7C)W%-*YwQp$Uk$<Y=Pvg6xvUI9?gIjo^@XfQTH}GG6Q1ov8wdyxr{o{y0Q_EdDKl2B){)F4A&nEtXnqC_+P0&w4hdvB2-8XcPBQUg?bt^}~x_{7O*D5B&PB$RY5fQx-kwOvz^e1M25F17qJM>^KG1=Lcm_POXytPEKodmTn!);lWkEfgB338iOR_yD5b2eBYQ26+QN`8GwaebSCAMDHu2i)<^4HIMejH}9j6^u84opnlda#P6{xhCfTcO5@63`BY(O;vLp*DQYc{TQA(E5iIw-&D~Hg@vm{uQqaHeR<J~n_{|L_u??L7wTTkOX^;UL^>qFxmx;SV{mi5`qh-`mwQ?DE1guoV%}cKO!QHzUu5DK3t;}F09FZq0F(D@4eZLMYy~jMinco?+pXN(tAd>W`ztoHw$6Y13GJZSY<i+b#k96*2hFm5z9}JCHcg3y2UCs8w1Y}@igh65?VN(L&J_XFR$A$l_zS8|1vVsBJ@X~jN(%>y8Ns&dxZRIAKS}qf_#|LuY)nC@h1o~S1YZ%v_n;>XUkp24<yS4!bpZ?wPHaSON?@#oFCdSG@37CVvd!3-UJ#V8R|`$Q<FWA2v7uHRGwltY(hUuG__twTe+Ex|oh(H{2n)A`+Qk)PoFR`8jBR2>;MOE5Lu_4j_rx5M6$*`{lv6Sw;ucx?SQqS~XL>(xaj_Ep-5}Cj<je3nPdCmq>kUUB-g8GwDEW9R1@Tn*BiXkGT}ZL6UVrs>5r)wVIpYg3$^OdH(ZOiZJZQr(gTKtrk?M|hCHxA8dABp+rX)hFgk8qbtFC3(L&bJq(0o}5i{L<gJJ+M%L*5r;V_Smy#Ozl05^OBl1#ZaQp1ZNC-y_uX7i`(&=k*gGwrn6tJd@m-FB|8KLB)|F=EAa}JFAtmJ6$%hEE{h;zNN0K;%7ePmL_*vHe_z${WZf(<(;WwCdbRlfpltMQaM{i^81kjh08`phLlYkmTjZP6c@SW0*E(Q9_^jq&>}UgJb{#XHOb@V-S|j~uYJT0f?~^Ue)#lk{`FUneV+a6OJm=Qx9Zuk*XD2{cZM<Tmt*f{WADg=M(Qlv@L{zu_VjEieO6lhZTPz}eB|(Nt`EPThM(8goeuvEN^B}GJTvx5f@Y0z=#9glIQ-l5;s5RGSEpoNeP1=9B=f$QW%BZN_``@!(vM&nf%qm?x7m(nL%UMFj(D^>513D@pj?-DZ31&<1Gd>%Qf~6`xRXg^)vJ2#zcql+1xd9i`^s&bdA>GahrY+cuJR+zu?(qS2zv^el9nCDM~qd0?|{80lI#SAAB=bT_`R?7aYp{+zty!N9*Z0Ry@+%ISMWbsnI=W5KLoCXDI1gjk59$Qz`%vrBwx(dc)7+zKXYwseg!KaQ5h$rPAex=hP`Oo#R7LzqE>cZOq2v6t6yI<4Xo%E$i2WJjwP|WvV=lZVJ@N~E5TAcfu_1=eI1vxx0E;buD|gy!7rn5@Co=O(M@HZkMOJ|{^gpFdX9f#Rs<`=ky3TUzX+9;UAQOlFR|cXqVO+tN(}<D#J>bcWn%t9@;#kEV8mX8FKD=2<oYLwO(Xtj4F$twBolBmEX)LiY3KABd}OIHsxYmvx+x-t^e3BenFp`E<Wi>3j;Z>)zlX!1OYlDzMuF82iG;8|0ozCgLVJn>^yb;blQ2jVZH5DEpT+^Iy77`QsDM4(#{dCd%SwKBWmfm|)o;1sr*OOJ9oZQls?|?os~WVIKB&&F<{)CH?rg292Ti#sIJ~TG90mF4kuInkL98PCjBpG-a&X*6kqHUb?_)fu`LBmttEwjbm-FHdZg9m~hAbDhydB3ow03-_D`fiXjw0pRmrmBuWWfSFK6%dNcJR=)Tr~7bRK*+A)p9qUvob+e9f^dAsCm7+6>k+ipnQ*eex$b5Iq<Rt&#K?cA<yPu|AgN1H|CHtWHq0>7J>y1dHT2xd7=~K&K&ZjAokQLtmzaU%_*cePN>S$4mo+qLj3PO3tetq6O#QJx?E4X+!N7j2AK3C0Chbt`;?jwNUAQDeTvf#Y&J_kW6ek8<wO;!?8AyD6tAPz4grEv_mw$$1-?Trb7KG8JTJAN%WdY?c+O>xbV}81oNE4_9IztF<zsgkO9D9Ek}($+oDp@tlY^`-%Z+~hDmUS*9MlVIS*ck>t_rEJgZo9pQGTB}<fasVwK6@*z7OE4th&1b70vUHy*i+e2fs5cL#PV-IXK8jAI55I<W$Z+5GhBc`b=Z!t*--pG91)AK6$Vo;8bz;JG9vZ%G!JN+5rKkHE&kY6@qYdO+45#yJOf#9&B<hcC??Y<R%^oD}Ae2CJJ%zg(Reu5N-iS49w`?&{)7Z-QlpIoSD!!lozlv29b~|mI)S$uc}t9pd{AwV!+<vuLJfH)E~kMjL8_t|5&ScWPC;Wu`s^o;otBHv>t4`7TyURnV;2xph(T01BuL-N^2l>4LDrO930?nL>IS8N2N-zZt;ty6%fC}z4^ep>Y;<FiNTH;=zi4*<cuTC^Z3Tuo+A#}zQt+9)F)=wY%}p<sG>qWg1(f9RCnH%A4i<(NuA4L5>ayIgn@f~O&Gkl$gd__U0(^%g=ckWaoIiBXUpmojQn8oGBpwC`TBcP`Kq-3^T8{Aq*GZL#tQ?jF2BxrYvm4bgrgx;;D>oYM~OmoC~K^kwIn^T|KC4_HSWsheQu3IDE4Y;jj<H5_Co1KaITc%ogvdtZ8BGH@TQQkG|Tk2Q&p$aYJ7WQma`?4#DsD07vs#mG!%@ICyb-^FwRzo=S<;BHI<2Gw9HQ3T9*s*^KyZoQ<$>~#b6W9lyN$V59KP!r%|=c(>^Ep!)BjNL;}c1IX%TOrV$!mS+19392SnT5JY&s-?(G^OYf5)c%YPk1HuZcrN@$}SqI3zPE7!h>xit+cMv(WY;^;ra-#Rfd?@g%0FJ=>%2qJD)7d)IEGBc;6>~O%CjqY>m=0h;*gE~f#z2-WS$k#b69Yj{xRaDV*8CGeWc1khSA=B^nd=!{v3Cc5tp_hm7Fr{Mus_%WAepp+1@Q>iL*5x%7;xY58?&X(UvV3`ymr+pR)n)S<h5BnQme}ioA=uMSth>r!j%5f@1`VnRT8Q7H<rYnYCmR^v1pGAhk3^=+K7#eoN+mbMX_h_w<CV0#U{L{_nbJ-Hz@Pq*8ZkFgu(gmKDQD?aDPv&p5fASScyl$#7zhd=K<;ytKCNXw!3VfPg}*-q~^9%8TOf;Mfydn*i?*T?JHu>Z-u)jDXekUmTXyT*|Mtf%T_U%Am#7`bjqK>kmvKaWM^+80c~u=0kk8P3>oHc=~7K<^Tm(KJcMF8adY&{PKvPBjY?_^Eg`l-gr^KUcJ)zcNX+iua;Eskngpjbo)KGyKQ@-2sJ#I`6VulDX5U@wE9;rk3)VATXluFJYm6t#A)k`1_E$cdE!b3QG=It#)Z*fQ(iWg7O;?X;hdiO4v<Tv%f66GdmyCk+rNALFmWA7=j6yT3Y_;(@yD-*)2kix}8J(J^t-}GMv{jDiufKS!e8I!HmP?;Cl3vKAKix};GmGwp8Fex(Y){)s`Fv<5n&&!7%|^s$+DY5`VlSyB(vda|B|EuMBWWS5W{tZM)yJh2dKy#cl@87eo2?_#+@LG&mx=UO<t0CRb8`F-tKUGhG5k0;h%a&fKpp}X5D)oQ*RehV!Uqoe+mR`W6YZ8wpFZ9m3*WxHR*IQquWKhJeYoO${z@|R>g2#<R8=%jp)ZAeVIIIoA_){fQ5z(OfX0@^mQVvrguHF$Nr3~p9-nPX8*s07nfydoq93wAeHgnuqyG+NGzR7wJ)`RlJ-l^Zp`Gqg;#`;!eKh1ZB{+Zv)A=`Q6Y%K$68NkYXt0HR*a3M1UZJ2J9&fH8h3N+|@?>)|c#9qLkvJEQ*-@d)=%^TKVMwFpSYh@4R`uuc(AvU{mHts|NoyEY=Syo7#683go?m?1xqW`T7;MBts7+D?Q>8;hPNmgg>~v!Cd1RwVia!~&Ct~9jHV2YKfPgE=!t&;<l7J1FU{A~qb|I+vP5+jm*oK@<VZx#c;DHR8k&zSZSz9LzWFOSzQ|n0Yg<}os$f6PA<AU{xm7#mQvnXricC)U8X!vVs{MBlT@z|>qp?acr=}h7S8+N{(?jT-!4AD>-K1^|Ew(47EY&KAbqnHjEw32mg6}WeP+Q>7-4xmza!+BDyfxGc*j(>u^lhBCVASZ3p5RGO{t?ukZFtNa-mYY`Hrrc5qzco((O{Kup7v)ooA<y3l!ygnBF^HhWAN!FSuIrSRJwm0kL%~HmO4R(1pP21{HMtKWJlMV`;el0q+o#zMBGY0Qw<kKE>@_?s@`CDs1!cydzL3UT-<uHQE_e>KF|Fqt6Q7dyru7RzgWJzrF#DZ1uK!QP_3z)00`={`Z;}abWaw`r{Py3s5&ryy{w1;Y#_9jY>HoXTd2nyE{%^GYZ?yiuKWY76L*@VRem}?K{{)HuW%~Z$PPqF=R+}^W{u^VLkd&~<aqCL3I^bDF)#I3_38wk$f)bQXDe#G3YC+{+)zy2l`OoP1PssE~_W6lkzvc-y%=(2T+q?1g&EBc!{O|6Z<-a;Pes)48^-e!7u<Z2WjNE@AMGz;td_R=I8AoiRY+zfNR_OHC`M{Fms5*J`^imC@RL$iF>__Cp;`bk_D_2`c@aGrYo_?t(7AP7KP`T9EHIKRl;~kw|_TsP^vwv7J`;WxWC*=PA>f<&bwL6(YRdloex@zR>pIu}ydZaQ4j%|=m6QB@QUE}(%E^+-|rjmb>YF`WtPtg5e<><f0dVl4=(+hXu#Zxi>Gm8AGFu6NFX#jBfU!kNAXO|bMXIcBN9q>N4a7}B$O<D`5LIp3E2RM7;RjjTZP|e10{(CMOF^U%Wa*@&usM7M7Fny{DGfMrFQ~AXgg|ipWC?72UT9h8x@q0}Vz(4<|i?ikG+PQw($}a|R90&Q{r-KtN49>OTa!VQUr(aCJ)#JCwrvJt2S7DcW=jxv*tZ5P=7P_~IN0HP5-GDa6t^pHb+OfM_Sk9dzu$deOURZmm_$HQ?YO-6#o<N)40KSdsPh(f_^wd@~Y25aQ%7gXPp%V-BGHbOqMmIEEwUso1BMW)Gt5zMmAU#mCDX8j%FY3MV+9%*;u@|8nS?H=dzAyGbd|k^r9Rc;AoFL~$YEVi8XCjL$VN0+F)siK)4cwsUXH-EJPn$ph#)alZq85QO#{IT6PTtdJiQ=o%k*uS|BuFXI=B%KpaWxVcji#PtZJVyc!Rj^@4TM^_-7hcj^1CW+_(-?LJ50PhSpf!cq}Ad>;--q)Z$mb=yBS`7q|zcU3rkZ%&0`E(g5n3^<vlw<t*sv%KzaO#UPf`h-uuLcq<n64*2G{WxT;JM<eu)0q_~X$D(1TywxATv*WRY!YjAQpmZ!h6rj<bT>tLjNE!)a!uf8ZZYSD|sZe0}~NI)~2wi;U0gykKkO0?p>Z1W-QSc&JxYg+A|;LsX$73gI1=%99lCUkU@(y<z%UH=9=p_RBuF=>A1JwexBx%MXsmbd3XU@NQtiLIhxiJ(fZC=qy4$+!h|ZpUJ7eNz7v_Ov6kdxozLqDveIv_8=z0JOBg(g#chawrK3i1BNQc1j}EMm2t{iyE#^uJRyo)eb&JV_+;kZIBT=V^MX2SP?bN>S(q#w-^TjcJL4yF)2HL=fMR|4l`n-h`t|)09%n1E8Vh^O<d2!WY)8qnN10)kn))y{j&ZUD$qCAY~(o6kpJ}9oWEV=Yt?MZk8VeI{iC4x7wv7LW+vXGCC7G|WxG6U1QeBrn_hzD7w)6#I*{YE^<^wSpBT~A%jvc=ay?e|TlO&&M1LxX{$6Gr4W?)|ZD<$UIk}$7@NCaeH@nP*;YsPE!x9qON0_(m6qmvKV$%yFm0qYx@;lM}IP0JH!isBR@_m2?2r($#uGyGde^pKV@oh_U8ZL0{y}MSS&vS4<Q_tt0o`32iFocgYanEVEIz@?!P}8QKSvOi*QU!^0Lq5o8(L_Yu3enNhn0r~Ss&rP46H25T)kw5~DIbh5&M0$w0D@v8oKp}#O-p!g?6R}tkIr_+v@v8!fKEYCNyvxo816DMmPyK<l%~@3z$w7AVkfI$fk(7tFSx-Ed3b-Q`n4BvgYQYj7Rb)=qcWKyq6cgYSlk*duk<uDg03dvd<_c@_oE?68rb_<+-FP1!9?H-yN~kY8Tog)ArK}6|EC3T6MhsMH3xlf{!|jv9zNALZ5n_`fsaUElotr7xBb9=4P6f%JUNqCJ_DNCNj*V{0rq$0Js~t+U&I#H=!g)<2YF7glqa$;M)t}@z)ATjXP=6^sTz&)fPYC6DIYM@0{Y-j9U)a<ABCP{rDk0;fB}$BG%vl@?8G!pK0ePF$YKp_3~7k6LqFg@{1j1nGm)kc!AE%7oUVK@u5!{5#?*%aC`?K+7Im|U6PcaG9kXdzM6|Dw&u3_>kx1M)$rCt`zTa4HrzL%8%?>&z&_w2tCKHG>9`co}Y(3Fdc<~XBJmfmk=w=Q5N#bCc<jOd`qp(aysvm4x@nj-9jz)PcVgg6-^q?<tZZG8rDomWDAfp?zknH{vErJ)dw>1EYT^AP^7p&$dNlc5c=x+K#WabN3&G^}6GL#Og8)?b)f{|Mo|65W{_P6n4A~v_X4olkeIZL^>e5kif)5!Q@9c*qSfLSuPo9NqgN%8cOl4+K4oMVYg^)#z+H{FrFQ?hKX=!F`1cceOZ686!($4T_{Qe-QBppk)`S+R-0+RZ7@ZSs_dRpd9__*vp}MUZ1(w;-R_2eUmEXHy}ZM@v~D%lO0pMOBpgRx@BD8T#?M7GrDP&TAlS(+F=oCm0aCF>=IK)*w-jTVjvzYza<IPCPqu3uvYTdqudnq>UG$XwUwGwj*#;BCXE0M05K?wV~r9){&ZBZGP-(SMwmRC|_+37S*=X(4C4zA?C3QHM;C#Wm~0(!c0}Sf*kUM#wAV7-R$Lru^E#oR&D_K@>)a(T$-I&oG2sFiY&_?7+M*p2yeuZcGIZb_(hh3pxN~zkAr$G1|~41Z4Uk(Xi99RjWgPIAu)?s0nL5Bo;~7-{GnS9D+o;cpv@T*`Ia7)`)lukYW3^{SEFL$yhp1Ndle}vF|{j3Xkvjr%Ori_!+DLSj2f0Oo;#wteDW<Ck8+so*|6lL?+j;XL-JB@UG?l(;s_B?kNH1fbA$&TOb4Q6mn3X1^DGFG**{Ki+EztN0+?9YED+O`-s<H=@%T-VRWJ;>T5bSZ_Uedk6nzyVLRO+mPSrr^VJ8bhP6D%CjfjLX57_d}upr|7+Cb^_{F%?+(BsV>LXE(XZJYU%d$1I$<s%4IFNk#>hn3_Wea(3mcYHJZUM9_gHpw0oHP#RSr{jM%6L9l!Lb0@LsD38SPcQ4%D{+3h5`NJ!KJBBHR2C91jYVDaIKQci%T~=o{gKuDG}<?dgU-s@+W$Z~#n!p?7<(DF#WUeoT7+L@GT)PdM(G;vTeo7h5T!YSBVglW@wd~hg;~QCW~pU<YSKBn(?me(6=Pv8JbJn1p92W}-!4qgH_^i1&&YaCTKE-golm-!=B8cp=!am$%`YQVX{d`)x7XVCXC(S9`{K_?^xep&Qlv;~_Cj+a%k^PZvGC}7K65n|J;9?tZ`)TF{M5P6Ipy{fmHsK4iWq&e!Rox^aIFNq4UQX1L;KQDm=~!0`h9tP$=Tsm2Lb6EVm2&@|Ly(fO9DIQ<@wS(h}WI)qG5l(qPw8Ug6B}?OKbWHr<$mAIxtz#iC-;}LN2He6iL1YA>=vr&Y31ErbBzeyQ68s>>$!IwZH-*-4QFa+~heIn)r3fZxK8&qa2M8;)1DKa-orcCoWl`qb2XXMBcqLTF+Ra{ZbRvFX_<Ik`C>C=h0_t?fCy}hHi)oc}Xkl=t+|sEY%nG&~&Mxl`go7`j$}I)I|p<x{b{vC+bzE6L^L&-&l>ZReLKe+Q!7wjDMyY*(0+}TnebNJcX_zZ#W6=vurHN)466w#KLeoS&Ug)&iAc|$^#BtkF7@3wr+~H^?KZA6PzqfMk+G0D^@M~aw=Fek*cOO<kM_Ky2axrD_99H$;B1CwqCIz<Z(>?(mH2FJL%N%Tmr^0i=@W3`RLk7pmjz{35i6jF61@Rutb(G@(#I(Wxk$4=w{hMUoSUnMR{bL!Nshc0yj&M#?La-|K2B^=1pmdqg%AOHo?8k?m@FV?;D^@$B_dm7%|7UqiG%|IA`~Aj<+XsJlgCYX!Mbu(**ZrcGHI%%It10&Tc?|785+4P4IX!!JXT^V0I5|)axWSSWUBA<Wh^KaHq!6YF&6CNPqeAd5uAUCS*TN>K(6qAm_8Dw&=iMf(!BL$pnw{3BJOOY#609v&xjHUE2nxNj&L$XObV^`0W107bT+e0Nzze^20~)f`K6Bt~yY<yxUp*SVjlQ(h!hm262Sn7QIZ*m7Ml|Lux49R>#_-uSWkg<a_VYZ;cu@V>i6s<{1}4vxb-OF2Yo)Xq`jnX77(Y;VlD_e8P=M*Mi~s9b?9|RmTivmapL<I+Yxv6a@3Nt^EU27rW)v?$}NKZ5G!XzGJsTm11XCf_8ZwoGlts)0O*H1sUemMqR&z8$`>{ES|t`J?H4XSfO<c2FCgeC4iuIUoYJ{Tzg?Z-v$*>z{UX=OB4{)WtR6}tD?**j2L0qbeviU|2RMQ<7Q5rhkOpI$kYZXf(=Y5N2YFS_<-hr$#+Ym<7O$LvBNtkDNTq&wsgH%ZmXq_=4U>da#2dClg`MfVTzB|iL!R^gHqXZLM}OIb>Zqxek%tJ0t;m3s;v~jiie5Tqa1z{q6L^>2LY}?MIXlt28x79sC-dB^Ad5Z)enZa)sH<XZk1-@R>&`gQ)R11DO)w#$dGcnre>AS)vTI@lvP)xtQ@7RG>INdmUpgWwRNf%UY4>N6s|1QtYT5K>St<JO;NMjOMuRsnw2xj^o5#LSJbQqZd>{Fmoq`D+61j|=46WoXFfom7Ft3>k+pi9%Uba;DO<I{ZhuRr`rB+f<N`NmDp!@2%{&WWfG3G)FqrgJydZtWRW4)=o~OSHP@>I?xSeZY(NB;JR{I_@Sd5w%N?5ExQVh!=%0DQ2SpV1i2jEW-lb<JSX2j%{BK*N8CZ|ywxye1b8?LD|Q6wS6ml2c4Gh%XyAjX$SG*txw#&Sq=U8qR~E`&W-RGNNwla&9txu8e9&z|cgL67gd_(KBZn_4MM@Mzhy$&1xtLyUaucP%346s&}X^0mk`1@mzdZDW<E_4g5<1^>nX%Nv7zxu}<vr@Ou3_8POtRLG<XTWnwH<feKWir9_NW|5QY-O;DsGB*;FZ?FJj=O-w0RO6fx<X5#Qgk{AX3t)`6vJKJ~i6F;$**nuxRiY@5!sB=Ro@7HXsWn8Iz6B1TYQ3YyYzcrQCCJwisEzC|iEp_5<?4@zxWNykQSRNKUV|^d{0I|~=jknL5&^IgZrVig=3^cLAiciOc)p_<gz`KOYdwxRRzEcIh%hdb0Pk>g$*A7(rbj?W;HP7Nc{ClaRJuYs(aPsXSXkQgUw4Fg`dhl`G{Q0#1CNZig#5A_NPRRy#iR6g;H`-RN<=yAhG^|<cK(jh5Xw%s5Oqq%n5xr)I=>rTOAQ(?yBno{CH3b7fE~MOd=69&Qk1WFk**L%-H?o4H}Y4n$rCfOgoV#<ud}OlqD{Obym78goW0sLxQub7dkPKDwTX#*L@1O8n>M_!jI#z9o~>uh;!{B(B#kk>=Z*w4YgbehH~fm0U=BWWV2Nr@>l&rBXwT4uX0i$Gq(8huVHaP@ojI?`L+NzP1DHR4Fy<r};jZ^gc~_|;ix|6IqG=YZZi{=2?3k1GjZk@#*P25vwv<STWUH2lXPBga3bfnMBs4@4ry)a>^`iNL!|-NbnnaSQNbCX0EQ#XA)p_zhOGY~s)pWJ2HHtK9m}?1xvl3B-KMFku0d~J~aYKT`JTQMhhNOAOQv<UN)4gN()7Zdopv-_B{vrQqh24Hz87k&GpaUlpb>-yU-c|8%$C>5qcRuWU`NbVlBq~LGng6@<5`S$9fcb~+h(PB_jsa=3{6+a5zI&95X~~Y`p~#%Ga=W|7N05HJ6}fa34G!)5W5whS3%o1JS(BHWS4GG4?|vgr&+lzDmNSp%RE^~cT}tzNMyH2(h9?AB-cOpcSJrE($<nBoLNd_{1tDjo>@QLf`ph!XfBhARj*)HmntWUf9`q?GD-bmx8aaOD!{Pd$N~yCnip|qx$rQ{}kijd9B`Y_jT}_w@Q`J%`Mpd?C+a*t#q%SF0Pw6>4HiA3+oN#v#;a)*Uv!wyMi4~qsIm^hT2{?~KzIG{3)fVP5@_<G{jhqx3qfI$UkF5j(B7mg!tnm?1mr!{IZJ8BF$=|%<{l0sd|NNQf)X&<ckgw|<NXiFp2Vg6&fXxBfErn~gQt!#{?ufYO*05uf%W!Yl;|CqHg`XGA#pNEc4-yEJiB9IeWXA~-$B0o@@nAbeh;ZUUDlOJu=SjWw1eB?R3d{T}<nb}s5!z5d^Z=>akO;Ac!jH$^6xdias<)aNkMJ0gX}f$dS#nu)-BR}39GRkMbgR;m2`uNCHEg9dLS@l>o|{QNG?o{=ywW>Ypm$f-YUwC<6b<#Yr981;2?Kk!Zqt5INpV2X72r8B*WMZOaZu+K6B=@c!d0$8n{eHhc(!1qlf+TcwO$qp)nf1G@KV0n1<=#CT;ySfKNYMp7_1T-koK%b7~4?bmcSDedL_u8Gw`gMoEmSv7NZ`GlhjYN)7JVTot$YaCgm`5-P9Z!+7W%}rVd1DqEL)LM44XgJcZ^^IC=@6OgBFEFmg2XVywAT3!EmCZc)ep26o=?W+tKQM}|sYPD}T*(Z$r%2_n|e8QUfyP6NtMjnV<J+|d#TVCU3}+9H&j)3T(MY$RAI^EB$<tYw>4#+$kOgyt#y&Zp2~9H}`Ql^;JcFQ;Gfa;llE^+Fb2pyo_&G1J>6J7>eGJrZ=*>;PpI26HyDHt0(SkS7y;9-7re&?$5>Yczpm#)jHdu8}Ez8bR1Q<fe_IGm5|#O+e;Ad15JVOSRjTITbJOcgD`yeXgDE-^f#Gh-^O1yIYHP$2OH5kuTan4R(Zd#J+ZSuQFO(-H{<WGUr2l<vklh6O?Qvf`;I-Bc^@Lrh`DWmLK!Nle<-9Fi(JIo+@&be>m@@qDbAClhuoxnAqMtoIku~7o7ub^w%ouaw5Zpp?aAsl4m(aTPdl10}J(SvyX@pSJdD$!-vVmFf~>`c~eoT)wS$G#R`KC22rkcu^Joc5MaXK;1+3yA7}h3Li#Op{1zEIXi0QRjOF*b>JQ59G~&^aXU|CH7oS|!r<CyFo`u+`m0VVJn0CXVm+aC4FGI5a8H!-iJ}$z?`7$?-ZNwu%e_6e)VFRRqWUIF|GHnLoej`<#75YyB14z}V1>LId-ykKCeTtSzvLJeRR70$ex1kH7U7=$RGwRxyU31b|B%08h?pHvkP+N5aZ2nGel=l+N0?@s3s~w2=lesV?q#jFiwKX~*lkzv+Z@QIx<<BF`&cz?4O&a~g*>Y0))h*kE@=tg64iCeR{xsM*Eg^I9Uw+pAP{k_z>Ca*OdAA_=smo8Ae$0HO7yRxn{$5SjaCq`3EmB6)HFV{tFG;QRg5TYR-|olqi$PrI{^{TK>~}N!-Ohj46s^N%0g0E$-!)V_@%w?v=mC{2{w~+Qvh2_Myy&jH7{(XvIALHOwoEf^EhCE;9Z9OrUxek0SYFiSg}$qCrta32v}-HRt$=70;VRqFvbg?%kBqvg@z`3{WOUq0O54ZT@0!26*>9a{Q+|ghe)pDO9JRt<GEZ#W&VP40o7&YVHCGBGaz(7ckk{GpIvcXSKleNDG+w+Jg+<<ePn2~fOMLR8z5YUxQ1|2u)H_yI6B1MT6F-DmNL&2!?^?ev{rK_czXl=34R`r(vA5M>K0r$E)=>xEOev$|I1HHV^^kw6wrC-T-tcp=H*l4Eu%?zel%|!P<aW6gZ4Jm{s&%ZC^z4@uq`<Ef^+QjxEoT_0?uf)CResx0He;exy+qyVXe%v%u)4S)mP4Qj!@J5hr@&%a;%*wCZ|VPl5;>78+x!6a@x#K1(BZo*X;5mCMUL9iRQXRoHoM=HQ2qyyBH9NJC>!vDU8%CLl8|@Yhr+ypTy!IiN`~ISGBmxe8JG(?1g*heJ8ypl2D}rxJn#B;JznoC4qO-EO>gvD`fuZlQXsqd+Eh^xp1GHQA5&xN(zi>Xvf}K}Ub;8N6p^OjJ?5hE43B8T6$u-Bl^(?vi9IFh9J3ykC=kyquuToG?&v)a4mL03?I2=Uu_2BVWLv~a@!1t3oHR;@dJcf-W0*4eQU~t@$inS@QI5oQ3|@_FspyFwq$e76C6On`r@k!j2XuF{{oC8Dfy2(0Z>5?Cx^SIJk5Y)G7Ze$>AnO~ge=zPU<<D2;uPtS}2|Td~C#biLQH>uT*UF@c^O{iH;{Q_hpA~oIyNvG-{C&rFHt4NH4wB0_O3Y;O`l%mx&z5@?wtq?#ZES2libP00`bdsc$sWe?gARhN1sGAH<*J0TEiyio^!(l%?Iiade3npH7wuuja)#hc*};AWn-`G{bs+z-gRAn}6{v%cJMJ1(6^x|bDEyrB!=~fiak_G}rx5-&p5M=|>hkYvKRgqO>7*mW<E63b=D)`uFhOBz{F4Y>q8k)N=BIOXZH;bsG`81qSd;ta2Gxn%d#2%03k~U(u?2v0*a;tyWee>s=GhK>3&Q4c)ww)r?0|Sg0uF%Gp!I-2<!k-*UO@NokmHsc+sE?V{5WHaha1fA98j%7wLSXpx$5=-Tf>87Tfqf{bXtsf2maj-X@fys!2#WB41$0;RcgT>(N?s|LDAMaIik8HbL{!2t6yU*CWe4)6Yf+@B||`Kay|o=O&qpH41kbL0wH@Fq$0Y6Re8&{MmRK)t9!>CMubc&)2CBu3FSmdH4R?9l!2-LLxjj+p6B0<(iQgk`3<uJRE8s0rwLViYl!#v_7U1K7JBDrW^us2J+V_P|GvrF%@K$O=-+mg{xoi|`7ZD&P*SmZH6lONwt{#d#nbWQh!LUdn8Rv#LR*3~^VS`$-0BK906V;X;Uhq4PpC{B8gr~-8C3~l`a4lzI81_fVIN4l!JxUM!b<-f#DfE2Eu9!AWNYUnChTrWLb_ngoOs6OY$k-9+tSNd5;&rH%c>1Q%T`Rz-PqE$g4Tp7hA3<xH@e!jEs(K!Y4^c5TW-Cix5?iE-1Xktk?L+#i|0FgzeS~yDKaLk63Ix(9pvKAeIsKZ=_Ab=Y2g-nbpf96$<Qx~kaD$$P=~soGh_jZEKkPI9zv79Vs(j3CNKGJk`^R>m0Uz(l4)@XU1@;z7inZV63Dnv7xtJC=F~BB-WV0cP;|*xw?{>exj^v7kTmAcef-f~ko36Tsomp3cXGJ#$%>a#o;S?Lm99dFBI#j1zl?5LPI0vk8dXordgt}|9n1V~Y<|x<d&E&l1dK50H6FO~ay>P`#P6DC`E7m@TfMefewz*H23<3n=tF1ZJvk;^?E$q=mvA$R`<?LjtgD{~dg!OB;ajxVUo5jV#Zh0i5h&{H2EL=|q;h&)y9P6x&tvUYXzQ{b0tM8_hOTJqxns9|Hq&Tf&7bW+riceKB<1V`zb368RM*|1;&1NH1Lb#vlIY$Uv(6gupAG-pi7N?5qOV5jg!KmBxQ@tG!&XtLIB#}`<Ql18=dWu~1j>)<TSmi@-4K|B8`hc{hU)o#fioIh!!rykUJ@$6*af@7*|HwsFFL`C^_xy4_^|*lbHjg?XMQ_VvyU@1`)qbvjkgC{YsG5WN;>w$fEstl4%o9*Ps=!1KUAmue(S;tDy~5M1NP3GT`M&^LYG*=%g67>CagQ5-58+;*Y3elu&Dt2HZPD4Xi};(NpKMGx!|Q{DQ64GV9$)Gyo_2=cf&xV@r(ii!0Qnn%QLfl;);5n`49OaY?O5_Gbl$(krk~(&JChyK%+oc1c0rM3kQajiu9V^ja@e8ZKDO)h^7N)uA`xM!|3ux3AoY|&mZha!67HOz`InZL#QP_Wrcd8`t|sr6WJ&-j{+`O8YvQ$E^v!9WeGSl5_4I>caBg#_xL5o{%Y4!UUCmC+eas9^hfS0kAx1fnpb|S7Pfa%b4QCbKeEL~&_>{EeGt!?)e8UU^n>x>3oM>T&!SkT);*TS&T1|=a^-rC<zr3M584_GSi<}jaqep#U<o%|p)6X<G8I}{I+j?t7w;%I7;!sF(@}HYg><68T3atZ+wO7jhRLPJ#L-S(4LOaP2^31ON|Eo&^7rgb-$h*5+LE_Czz)M->7(HtXB`ieblw{KtFr_ADmVg&aH?K(Pqj#8aI25bpeA*thCeJOt7)UB#69X;SYE<TLTdR?a^R2Us=Db)G>kT?`x)Y?t^C-YiUx&i3ePi)O3(QCGh$SR|D$@3r7(a1*v7!YeR*an2;Z<;E(K(S+#@wrH`;*QxEin^+G@EPWHh_$tHHT`^W18vML#iJ<Z?BjcNG3_V`}o3R)ZU=8N0xOf#PLLfoqY|%6bIzny8uJ$|L_6U$PY3O=V+Z`NlktR<m`$_t}p+=Rd2I;buJ%MyTZmdb$o!j{+Vdbgx_lu`Ghshb@A}8+J#qUkYNzpPvHZpF)V2r(xbz^9;gn(txX4GPfyT$$>spWR5fMJG;CcTOfR&&F+^~w-@cE6W~05$?iySd$i~kCu#h5STqhpp6_%}VX&ACs0q$)Z5R9EK}cQ&w%m3FLk%ON9(aq}2zv*TYl3j_*{$46ZrL8W7nVuT^9pw<`i>u2vx<UUuVo-d-le$qdAr3hx9oYWjBYIwhZ|W=$M)Bo2g2x^E%y9W4(emHp4GUc@~Z-{ycqt?S9J1{(yGml=@DTj*4w>ES#pGdWa|$};lZO>A>PWhVUw?lw7lK^$Zf8)YjUT+z%Vi3Hb;T+4P=%`h1uQ`gheI-{C8b#FaeR!VpoYB)`N{SD03;Gh=`kdVqU)#sGraaHAdvqb$q8~u2eCpy4K(vA8}!=UB*~($3<>$s#dKP4vmI6F7|76X_CVPh9mT~8+I(*h~u5bDdbl6;!Us)PpLyJtlM7$@9(R^1l>~&Cl6=NlOP8ITO-RSIUyp59H28~n8gbnGs20%m<JG*IZ}F-Bw|*LMRF6HXx3PsWy1Hc@PF`XK9~88v~t~=lmu3rWsJ~+;srqj{oN^!sAmyG5~3fSd!PpB#Q^G#4BK%%-XD&z8=atdDvs^k9i7oT$|-k>6jtE<%9nfag<hB0-LRSAN%>u7sV0a`)f#N;Gvi6aKmHV5D3gJ1toH-3x#S8Z{VSFPp#$0-SOK%@Yuc%YM>K;JNFqnRY6oa&@RqUNV0#5TUa0`p*SVi_0r$wT3F&9Z^48FL`OGB!a)Q{Qo7qp?I=zl*ED>jt(qbxgBby`hHic+YeH~)|Gm^+y4jX@a=L)~m_^jyGV%IHD%&OomodF$n!Z_j#FN!SaV4*IZG+bJ*!mTmEh_2E|F+=%CoSjWjBB@7>xW`bg-@8%fPlPez-L$I;%L^NMF{kS^{!KUXD2<GsLA;`;1fq7!UR@wgRE>Vl0~%&u;il0r=22&W%#qj6SVH6SQ+Dt~H7f2U*UXqxW4WsFhnJVi^|vEgXf#?9g)y_^UD437%kZO!Mqwev*tWU?!AhMU=}u3^bCTf@e-DoA;`A+}M7kXuCK}f`7v?zmDSTz~M~V4hlPV0W-y`8_>-uJL(3NA_xo<3DB@cXq9d2Zl!TyUx74ue~I&`f;jFx}A9CUf@gm`)PiWs)B7*>w^?2E=2mXj^21Fm}BeQ#zlEb#G#fu^wrO+3nB>BP(M%mJv~>DGuDvUi_oYwZ6xS}lI8%G=)X1zRotK6>f`q1<389P(~Q9;Fbb7RjzgC1qgTKji)WfToEpmQ;?g{BVa%aisRhA$#YyPEkY)hDmZN@gy7e<*7=Tr%~QUcU#e`t5F8;AGXM;Df;uJ{@F8@JT}BXfWp8aOYM$ZLc`qFk&X>hhl+`|bo%4kk#yRv_XJ$oE@HZds39Jis^i-7B&AFD)dt^)mcwYw$T9uw`(&WAtG(eUc5XGCd69%{TuD5Wew|uAW8xVJ$!*nzONr-WVRTjEIp6yJ6^Uo$^9PXxA@Pi05MHetI(!jmfaE#OlFdoU=7=tZ>>jiw-<+2D=DcpREneiC%kxpn8QfO?Yg4_+K7aFixo?B;CRF}5!f*e58{xMR{=xgN|0w_Uul{U$&0o_uam^q6-%sQ}yv@>2IJW8IeOLPZJhuMTpN&uc_f?<${WGxMeb9gXNBVDi@qgJ(raX-OcYam+@Ay~uivKQNyBEDiZGoLoFaC{BU3fE=7ximS=r8~F1p{OWSIX$v`@O(N)!519B{Vbp?}?h1rO(H7dn~lj_4u0oY{Vlm6RZM@8iJ#eJM1o>LFhMYwtr0mTB0~bebX7M@F+)r^53A_6ltw~$cRU}xJlxE{v&O|xthICrmb`$ckh>q_s)-mYULgG)PJ?bPv2q<_>~&5=hxsKs`*z3KGVSIG2WE!>*NCLBd&Bxr*Q!JErX~jY68#f&2aXkBEa;HH*MSL%A0abso2{4!5WbC<CagMC=<^|rc#>L&fuIb*uJh@K$JceQ`3b1SLatdn<{ow)*!Zgt>5+$`|C6-ruU~OczU%blV|oo?XNa0ZZ_Xsu?*97R?!*!+m}IzVgbQ(O6*H6pK^AL>duDYo5`e);_&X8V7s3V(CaYMX%FR867n-udA$gy?_B$>qRrFCoc}(#p6OePn7p~fbA@>~y@QYJt_svYb*a~H#~4}0*Z#th(}i983LQ`eWK#I@vs=JxzxeFgEeNsjk~hacjT2xz%y>M<iB#U1-VAoUxWR2;+r^QNP0ji}|Lo$Ja(;K|I-j^~o4Vz(5}i1EZFgiuKbN1id&L00=z6Y<{CKs~U3YFALth5O&yGKNbNsk>r@zMm91E@U7xR7g;sLgstA4wv5dAZ+D01AoqPz(Fj6V=Ovs)r(j%TnLFqN~^ftm_HsYJ`5HMFY>PG+ojptA>i(Mkvz&-RTOJO(@4zF=eWF$EYC&VeyI_!e8%Exy-Nv1OmX(KjR}Z+d^|L3G&MRx5REvO^?n*d9WhbXbFGApJ!3bFUgBkh8Im1Zb;=DiM4F2=;&?vQ>n3D9gk(G<>%pxcA-B-IuoEU2rC}w`F$?lSl`a;tJiq{2?O<E2Bedu4(v9t5t9YZX`m=`%Mt6N|<m|yvRWZckTg7BY1R81j$F6Tpon{NHAoc3XDRR?eLL&Jg9AWPIrU<He~F1V4GF9^Ec6T52&%C@v4^yguAW$aX_c+AVQ(Pa^8NB$Bfbz=xuCW+>ow!U{6X!r#4aX?@-*51WzmYBY2@*{{XaA6I^=)jK=064*)Y830zRc?Hzj+#IfP56Et8lu%}lnv+U+1ORH2<BC$BwjfLc7Z=SjfI<W&vLuX$}6$VTI;woX2Lm;K9-j5>I0UMlC-P2j~DNfQm1NTtPg`B0XfH|U3DMb>QuH-y&;7zEFauSgb*&J#%@2ZoFnhW3{#Lc>jZOjth_3C*iHneI53u3RJCpy5W35n@d4+edAE<>mAq^M2QKy}n)3R0cdk<yvX$mnp2<dS+);d#N{(o)`;JdP7;%Zq7;z%4K6R7|4pw2>wn;DJv#C=?_JN`mu(S2^Qw?49*@Y=|l`bPy#_QMg9`2BHy==f_}`<RF_-^mPj_oqk6*!x}YCSTc60xS=mpG6qAMA!Jf{$TKFpLL7`KIa&PGxVC5i;?nf<Bz*t@72SICc-<UaWVG-iumqfC(k_nUcaM9C;9*ONX11xf!vx>*!IjO%_JQ&BbUWTnpt3n8Z3O=iP9S*I$vBMnP;h9%6pf0<)2Hl<yfow_nr*Vbo|W;r=Jol2lMu_Lrm&#91)^!hmD!urPdoY|GrPb(&GB7!{@U1+9iiy3jSu8U-TmC_a0flLXPiM=>v2nN+=^@jrx=7S_~HzG(9Y4Tj^Zn2OAZu<&E{h}LmzmclIr7C+(CVYJ4o7<$(?Yl2vl8@M`6SrC>zk>BScSP<W_kr$v4sfR?vXN6L8Y7cMYT!smYASP5?>(nGG}O0mL|fV{U{%C1Haj+`DbS6B+-@_reUjY`#KmNa@%UguiuWL3k5+TrUhZ={pK?xQu#z0viSZs-9tnJ7I>s0fzSk496K@*cXo|jDX=tHZl4|{yJuupe?^{{CaI@;k?Q3g%-|Z)``Ee3Wpg^n1-n-Cb8RAhZ+I5F&aZCswi@Cbv<6d2?OH9b_U>~;%9{l`#&oXe|#Fm4^Gr7>`Z+Vu5RHo$yZCni}(;l^Wuw66?yQ%yywyiSe>@^JJ5Upc}Ai-_;wLIs}qp~j3)>_{H_-tgqDF=8Ax$LD4wUcl;20QuoJA?54Vm&N|-Wh@tNe$AEf{dyC4Gv$A?~sGuD~1Z&Wjzx^+V2lhpM3zcn<hntOH;Iq}v|gLBl1diozbL6AOpCA#Vh5dzH7RlL}f^>*IYYjW7u;+fRnJBvEv1kE2YR))^M(BFF<X0@8btXksoqdT?>m{k)>b1$+Jl)#10>=N--cb<za2rcCgN7pckmLgkuX8paEH08tG?y$7-3HA*X+R)JZCto+T_XMR?);ityPxejsRbeMx4Dd<=OnEDJGQbd<R#^A32RIv<759@11MHQ7)BqnzwsAVZ2lR=*&jA0CXWI>I$mO`6^%`^np+@T5L(Y;?JX#$@xbrD7;}=Yzooac;4DL&!99;-?@h60wk5ZDt|5nZjWi|l&8L+=qrn4enWo4gpR3Zbcl2AiEZBZD3h=)Sa<SmEUi3Zgq22&2L^Y)ctRD}ecSYh9pF(=02MjBjyhClZPJ2!tX6n`m90DHcJVdx5a-<;LCXFK}0Gd~u$BhCf6+1_H~xm}uE+)y0Ixb#$g7<rz}iu!_+Us%%7r7u?%W^Z0f&D0bokm`Y5NnCi0)9aJbC<N5rFE7;weD+0lnB3yx$unw<>LxIP>1q7!i+nlH6W7DfL=$e9H#N8!m|wm<oaBZNPeFpwM2AzSdfBXT+Fjyjzk{1Mwpf`>#e?IYdTGnvy}5ePJjp8Dy1dcV2ej{XAsYvmZunPBdHgq9x^{<-fR-&9>ufV`tf*uOb03rl5+~K66fYVPpWh;3axjriyuZ4&a^%j74lBsc?v5ioTCH%?@BY^C<mw1e^{2lj?;^G1HrXRSN-l?dGAu)Mc@MtD0>uIQ;7j9(=5n?<-E9S$mu!bfyPYTsFAC*h?~K=8w6#<eT=-aj`8|m{5+ayZgnl>BT)Y6DZb}QDT%{VP>*xU0*(gMM(G1I(kti*Ap1!mJso8%Q=tv*W+U`a#+Fx;@8}Q|H<f4)POaeo5q4TvheMPlCBoaDqJ!?MpJI9{rsD`_$V|EQLv^0H81I?EQHR^&GmOd<c?r>&y-k~NYf!ojJPRGA;P2`ExV#X6VjP$$GdBSKRFA=HamiJA}#XX;V&E(%uanA{1Ed3rU)lPcS9p__^^8<yGI!}!8CQ9}Ruz6=}k)q~PiLAw<#k%)4(k=OLu)%g!oqShxWYd7CQcgrfPY%+2HBS^9FI8ypipXYCelgUZ8uqM@ra)y>#J3&OT_SOgR2YwBa#sIap!za}+X^F!GYegNvIcvT7y}<nEpjFv5vHQMK9O29^d{vWY@3@MP^%OfqB3AgI+G7E|EXjBP_@d01fnP;<#o^~M2W5=^2=8e{_=aem|Endt;_~?xDYLu6`uH=TH*6JnI6g%D*Jhyyhu}w%iDrv=)_=!hwy?v2}H<jI8i%0#>j8^oRcrz5{#9HAQn_~#Wb~?ORo0BrQTFM8*8&mItsNkjS?5uMs&L*0@$50*fWdyS!3q->#uv-lxf;-T&+AwTORv)leL$VTBbmYX|g5Q1i{6u!+L{xiRX{r>c$U#_WY?M{`3@BSoj8V!^4r!T!DZiLC+RUc|VfS#Wif08-XyYi%=GG-^=^(gG8|XW{V{PlP7+woj*Xi4wm_W5B9M~952!Ahd9ZQpFF_y$sXXJsNN&vB^sy-kFiww^xP`JA6}YOoQK>Jmj_8Bs(dH=u+vl8KuzbVO}K>#Jc2lad8~x&6nv>{v?0NWAg{)g!OHI_QG)Vdj`nJQXc$?5jt+7WeoP(S*}j@UpWrnsV`9eekG<N~1$Rtk%xbsVUCLBE9Z0w8i@g>|PYePt4WaAP;JGWobF1L_h}^&YjHC`QhRTYWxtmcu=>Vzk4(tqYQ{I*F+cQWWW<hfL)z?-{kycaHv_pcYPL!FD-H2B#21?A>Q?nyK&A++b2xmqkj5`J_#)fgm?pDk*>X=4An@4YQ1=k$HynA?U4teS@iMj=4MPIq^<dBekj{9sJR=#PKv}P+E_A)2BbTbz>*kuR${*T_RqltRu9WQ^~vASw5+D~RK{=&!J-Hmn?&*~++JDjbh^PXMi=92U7ZEMdTG0u$Zp8L3?cVsoJBfWKU;|)E%b?)D5?ce#Y-nQ^g+!(Vhd=-gYD_lM&TlnUJ=o-Ax&)5bWfBSWhG~eliRKl1R)Q?|o<OfI9W<1})U3cVKWUp*Zvc28*atJ*<yPbbfsJ7-8?ei|tLR7*E9-*WQ=^CT#5#1(Pcp)tYn7(Z(fgp0@n_>zds~`fw#8L<WO%-UOU6~h~r5N9$A`(hs9(qY|^9T0>;3fRp2gPzL&YD-oa;*Zn4oZ)nG_cW7mh(Ukb72bMJcv{}f>^OLBnYF%R#^}{F(fB?MArF$K3V(*5M=;A8=fsp31hzoSp|&0g?Zp$L^2lYM5YfXVXmV52!7HK+$g{neL*@0CTjz)u;{!ciH0%~14cD5I3z!Z0YRzS&_H6B*w0px9maH|08eC-@qR?Bk`E+;sv(HXxM3FW54m3>3njBl`E=iNVTeHU0P`J;MPgvawLwO@I{NsB+mHj8n);|i0~&>azTH3I-9OlXO{=Y;7Sx51Vi@W;kZVd);K9WonPjX;JCw5P2eGcE0S#WeLUQ^MB>^Uw>M&T}Kb|M!qe{qlM#_F@K<*Goq$HdUJh$YB<i4Z;Yrc|gzS<;;dEDvGID}$3eqV8MY`FNqcqw2YVIZ|=HnT&(a}LT+6Qlq_yJ&(<Eym1~beHHAmdH9|#lq9e4;DKS$ueq76p~0<H1yo;3JFDs`DO$6xTpjw&fErmdqA8H*hnq#2`RmFN7#;}td0+2#_$Z^jmBD+=SMF&2&%Q|Mz;LY74bPn`Olnp;B}H^BPJ7EGpdf3Nz+G3UeI8XH#qynF;Tg6=i_7Vx6!mK`#|joDEWdp>Zh6iYm7T61Ob|8qN3$vL#k0vAW}<u?@r3_f|?<RFT2TfS-zd`L-H@sTvo*Nn-0cJVQI^^v&%NLfW#%*?n$TM@Il99m`;w{Od*QeBOr{c#8i+6>5*oXvU8(7<@bIQR`oYNLNfF`PjW32x=e!(^^0?$zU-<M!sDlQ)qVyYNOYsxsv)^#j+s}?c&^5bCv#5Ssv4lu%lce(n(OS&yr-3l53>Xacq2Zq_w<)0jG_n_zeV$OG^E<m#SL;mk*t;Zx1`3Pg&>S#nyHpG2M~(o#nCfN6?a&>sYD^KZLTFE4d1vHKHLcN2tj18gDbijwebbFJ!LZ*Q4+H{*b-Pss$!w|@*W2sMz3t3w<RQ0U$82HV24R8D79n&SQe6HX)xFF1{&GH5t%NnO=ZULp$5NWQ4srMl#YEiEh?V*W)ObP)O<+8g77CF)+A6sswSUrqwaA%b!)^=;D-+YJvP~|NRXi8z`{gEv7tpWJVp^H!$x#Y07w)v1yl4?0l<rn=~3Q2ga>Nx|IZgKS0w(hV(TLj%A0DcdG*+?h3{)=`nZ4%WT;1d$xDVmDu{HT2+@k1Fp0y6#au%x+P~0C_O@KHFZ#2L=UCQkY;CvW+BVn+WX7x~rm~i>v6wikw-z*=smBtC>?tHsraW#cUvLlX=Y)G3+p5b~_&MxuWM&)r+4!O#u}CHHp>l2)=8C!|mgeVBzEJIxRcRT%IjRQ3%Zl*P@fG)H9EbbSQ*X;v2Up}r?8Rd#7Cd_M1jwZYx3hI-l3dZ-{RVB*fBuQ<Z7c3F+0HlIW#D%_Q*6r<)7-8Rsh&3li{SFCM6#vo)+H4m1*Zo2aW)DAD2Pb1&63*<X)CkSw`IvKl#*M|l3U^iw0pATh8DN8ZOEN%LpM_pk4<VPbqa<YpSR@Z|MnYs(x)O%dK=X@Hk7v!e*5p+2)~W+?;*~l;^VyP<MkVD(i?5k8*S1XZPFWU(uYmjH|C@tAm*gyo8LTh()1!dPo6{sP)TfggSnSp3)LodL_jXosUai+KcN<d6jbOM)hQrvgL(}S+!GrRo5#d|Luh&BCaRmldg4YFqRP$4dqN>VI%OLw#6R(bLdpAP!Ovu5MN9sqr~g~|Q}U#VbO#l(iT25jtU@!6BGqrtIg^&mJ(U4s9o0A0PGG;WI`F&pVyrh2U+Z$VCWL8t-GY=z=a~*zUVmxlm~Nq(5hK|{8CjI{PMAHB!bntwkymEonwm(boI9BVo>+z=r%|08P{?Bzw{XIow4hv?-JP*vP0UFWCE+#CNRq}Em76A;a|_C)%Wp1Nse;`C-$d1O>g_?#Ptp3gz??L_Sze26WzIQtl|N}DnmXhAIcG?kD3qRKPP#@i6lNEBLSJ-#z~wVI<5-%Qbxz5Fp5oLw{oYW$_Od_ZfH@CS<xd9FpN{JC3C?Mdo+e4U#{DxMFupJfpCx~i_lrn220ya<*whL($6Q$a_nb3n;#HbY(b<b9?(y0kIk$N9XNP(Bno&BLDjzb)*Zvv{d*3*K7*fx$v`|k~p}ID7^LMIp!jtj5+?zM2R`RpoBNNAIvj3lWExW+1pYFWR?#jPr`QLO2XdhpE&gK%Xc2=E4d-`;60rN$x*>$t#ySkL{nrcC(G5yzH0Q|XGH@*FAF5~~Kmt#Cz`vM?f>*pLM!-b)qX+oX<JLM-K{X{7>=KI|mi2`ds7yA}<M^;@0R_AhG{N--PYcH0+XOD7%EwWWO%=MKjJ*>)I{{8e%b*TI)2@A*%Dv4A1`QsD75$(@{Lc;AmZFE_DV{shHf79}>?xIT6$w*pp7L{2y$BXE%{U>jm`5V=*F51K)l@qK}99QBN&Ekn5%k*u{1uVfqoR%DN(2K0$>eDa8Ia;hg3f8Hk1^^D8vvCP%0m59P+c#>DqfgdZ=Mj8l3s=+?hTlZw0TY)(B{y`vE6v-CBSJ9loE4>``e@XSy$cO0u_kdHe2H^{RHZ6(*h!Ht00=p#6Ws#?hJtww!KVDNy*$NW-{<_;I8CS|Nz1S|gwO>D);5Gyt{YJm_y>Ie#pysU9N_&-#4q7#2ldb^FyJt27iWuIzHtK9@?Ee$%Xn#aoPb;IA*8OT*$YU1IP4rG5Qr4n#s%LxYvW_99D}!5APLZ{3N>GDjChIKZWR0tCi51+1(ffx!ME2U%V68X0ar*}wO{x_!<2~tZGFvH6IK>3Hr|~e%Qo&vS}r!#l4OQzte_XET)#n-+C)>doa4*dSoKSMSu&b6Jb_bm{@As??6F($(f|wV*Qqp8R_Fx+vD+_Izlmj8Yxo;Zqb=wi4#L4gp)I6`O2lvvM<IWJS|Sx%9F92(4^7MYgFqEW4vzihqU5Wr(K6Dz0qsft-W~c8V7+ewh3x%3*zrtg-mmfs6txfa>xp*C7t*)>3w)((TAx;7sKYQ+YW9baTcFTva9@J%4*1uBc%2CDKP>jaK$1|m&zCu%OP1d_gnn>eQbP(Wr>9jKnH=~*O8ercC29*9io#tN15nbfG-X@z2}Tn%%zrYLHuTenq|M8hR&%(5l;!;kpK}4EW#=gw8V59!U7!8WdMKLuXiOj;xlH{;K-pzzWi$ri3EA?V=t?Y-?Pu>W{qH}@R+$e5dU<8S#o39}ZrQM}3;d(;Y^&@<><0LtB+43!UfVv|nHu4kW4XFjZal*bXAC0j?C#{U0FlJxL~Z*mX&3_O&ur^Ea(?05(bqsiB4L4#N8+rR<Vm9tsbzu6GP9FZ<iF$r3=dXb+aMO!DzCiS51rdb2>yPNZ+VT|0nQVUZn%uA$h|uoj$qptCk-|?5zJF?oL!nGk;k8nZwAW(^`vmMOeVI4sFt0!xc)nRDukNDm={>j9L<*SMlAAvOq24<D8;Q5B0-^S-$0vUlqO)SM8SJmggjZA7h8mm=-1IA<Q=1aUzl}=nYDcuW<3;`byHy0V7kC+1a*{Q-K6xnY*>>;$QFcsE$2qzykTvBsbOvNSs~ZqmtXNnzlW<D*lsOW3@A^E>&_c^lQa<(`IweK$2}%!-YN;N1-q;09BNn(XDd3;)o5U5Yi>#_(a6#}sT;Nndt+sb1AQH^<6`A@BRzvdTW&`l6$Ll>{LMPAcKGVXYKYz%PPD<VTlVXyND!b0-Ebq_MbHShVp@V9;R~aK32hDx(pLG*QGqg7Uc|*9rjKaQK^z=O5f{KqoHw1==vE0L-vQW7Wdu<5!ewaL((8=)fjwfddv~vI6C0@MdAUt&-XjJ-u;%_(t4D0jC&ZB3m_C?>!15yx$l8df3fYHNtW#?kjAX}fsa><FszQ@_r)IGggeW?NT9LBfZIIJ0f)8x7Y~4ar5P+x@A1;A7Qz78yKs-YG-?1-;p#fM&mCAQxMaRwLrLCA#DNM;xRP4NF;G7~PF#7V{jO|16+P)l<Z+oaH4L+w>^)lgfoeU_A;R90*cxj?`hf0X=;4ERvb~DvRnwJutt+*$5eC#KR>e<9Kcqn~<du&46wK16G?@gM%BZ*lwa>CAPR`d+p%A~ymS-_)_O-=Nzl~3cXhias`>fDTlY@WMFShU_5r{WMrj|fs^KQb|objw9SyU1jVOKqkMUgXplADI!dEi|}C?p&U*CcztLhY<C%>kLbwa0dTjWKNq?mbv-lS`zjy7{kJ73XAsljGV2gnd=IpJE7dYNGvu!IMIs*@weJNhG`gGJY(*ivmaAqwhc4BxN|m1c6j8usP>9NSUqDQi^fG}y63YQa()-maHk}8;mjGycl>mDUcGA0O-bJv9{=oX_a^WF5nlpIlnukav%M)@+MCb_)T47|<w*j|T?rrRY(G+v)Qd4b7W3X14c|S#Hy*hedB1T|KK6c(KEj&ahdd!jFWN-%d60eQ#fn~Be`I_H*M?DV-uQa(ZEy!+n+>TfBX2>Sotu`L;*|x9db0;(pGP+lr%51}tw`Du>vuzsIfJ@&BViRUPVR6d2L!hvCV-4CPD$L=fBHJN?}oGz=tZO3w=QlUYlo+t5_0>{aeT&8fCdGe2NKfV((}vDWObQj>~-N_VmR22;UGqFm)BQcBEkgM7lZ{35*p}@Ar6C#Csj&09IOTr7LczIYR!yj(({BvqUwc-{+tov|MS-6@Fo%c24sHw@7oB!jquwDzqLDj;&z8OmFTy2hqrczw|0lOc852W=r@(<59@V!iAwYY_o{gwqZJI6)&qSEQ%I)W;4P~eg^sGH1R$Crm_pnz@rV+hlplgX_cPc#Q(bMrw$HVqNA!J|IvysJ_q_GNP0G!}*Bb!eq+}OL&*Q-omd1;|(1<NT?kBK!e@Q)BT>@^7mp^NaaABcc?dsDrFNBKAJubAFeRcY~C{oY=yMX^ws#*L#aYHoJ77x&~IzR6rcv@I`rXKBlI1|`*r;^g%UAl62`n$}W@(7yh;x%9`HAQ!e$}o!yPK%a^lb@3Yh|<5p#u0CXX7hH3YB@>H+a~7YKi8r@y*oGSkg(PhDqH#jIIC44BVCgv<rke0qjv8cjeY`nzt8{?u6IAgGpK$%?H+LLlYI=A`Xt64op~F?6EB`^hN$WZ5%12LA&Tz!^Lo<NiEy=lu9d+*fAP=sLxfpB#G)0$pI+GPnqP&%A2pBXFUDi4WhX@C&l(rv^p1cbQZyN1`-|73R&>04PIn2v@2*^D<)3WnnElnAG(faZHG(|dCUR}`PC7_Rnd$O>uf49WcSww*1R}=yP@naYEE_4@yrE=1$m1o&a20}n4kKU4@htNC|Cq_~d|j;`T>I{d98X`RgX+vx_jMIWEDHg!U6qEa1D7vkp%0DU+@ZMA`f9iVuk*_J%>gxW>i7Z(5w|$F%kST#fUyJ7Ch9Kv{cWAk3H)OmP-PjS-%+Wf+xksg9V^$@gf1U2ysHN4SDRS%E$jr~Ty51wk87iN*EaagT5>oL(75?Cuc%D@B!$c#SPnm+__B(pTwLJX>&enrI@pK@L2m}`rU!9$DDu%nsQ{uP#aTy9Jb-VFMw6weJt(sU80iHi*#ia86ckC&IIX=<o|_SE6@0z+gv&UcLHf^~H^<Rx$qlYS1<8DOTS^+PBa8j~)MjVpK`~2^mk&qg^E5p_#R}np1=9TF0a0Pe6z+uwVX|*2uTc5p5nlX2+cEsR)vr^u>B~wai0O{>jJy!K`jfKoE>EThQF;NTki^%wB8HqG8-u7&&=#EZ12Ke~sv~jh7ARKm>qZpFh#&Vx!3coiK#u8XNE&_+c$y873{9k<q!+Ct85tuR?g$tVYFt`x>~Zmi^^N?2f{o~0iSr{tqul#LLE)xqfkW^V-u4omo*@(3M0s*PlU3`)2ifwHf(r3u_RP1YYNsZKz$WT0Z~*Nv^~4gYU{7N`yFf3<9J?0UxpXi6v#%DO_eFKS;ry6OQXDU-t|nB^qx2|P<Tv5@-cbb-h1+%%p5InYkgx)My<3WWW16|)fMTr_-i9@l8UVrG04*knS-o;Q5@oiO;;nm#i>x9L)-3u<a=vQU)D*g_R#Kvj?mG?=qo@{pf8^M#DqrtRdIG<{Tm26ouCFwLt>SZ>+{#p#C{jLv8tI9yJ3#EDPXteAEm=k334<S*xdZq?ljm?(LS0pPfxtl5obV9~8i>vTaD=D`2=g}<09OE`FR7k!RSnL0kpJ8i8Fm6~a7@BSFrV|2jw13bpeeR=3^Z4mH0Y|pW3WI1mL`-xc`;r#(IQ(0zt(+{mv*m~<@`APHJxZ{R+{2j5kd;I6)zk=kA>N+ke^HNQw%(PS8$WkiX@q&xGwl#2w_B(dA2xpt_Vc(0uXNet1lM3<)z&izb42{xxQfDb}+|zCJhe~B*PqmWvxt{3Jliyog1i29oX`Nc>$Q1HW=GHhHOgi*`7#3McntnB<DO)#dng!%MWX3ikErIzEj%<PKb81JYRNfO~}s>hVXzLC{L3wEfdeaf!m5~jR3&s-2_^`gqCox0_Zs(AhdVnjY!6U&5I$qiKg`QA7w7`=OYip#ZyEt{d=ziqO2x{)0K!CCW#$U^2(SBRzv8x!pZ|sk(&ylAz;kMMhG)A1WV?6AWvN&6)<o&d2ZbR=r(vRl{`}^^D=5FVD18w?Yp4P!0ZqK@I#F>(!m#c*0q!`J4B;&f()9<*d859c?<LfJPZG?RYwPLNu84#sP?u4-^7;I3MY$oSCg+CdX_K-6i6;8A)xev*`}doU#otKB0F)R(Cr9Y+q`w~5f~vmm`HNiTK`+Gdsdzegtu(4Wk#wQ%%Q&`U^dEqdoTbeqK9g1B&TxUCvC9)jLsKJ>Xo_|*w7$-k>}+O&mVIno8Lq{QGOG$GZB2eU7%Qn$41o;>MAkH)Wj@jO(aqFakJM}Q&V}UA&15GB7_P}3%5u7@b9icifXtz0~y+9`WD!f04e%pnl}H*>z?^m`a{-BZ7Y*3&ZiH&J5zR_1H~#d2e@h>?%wKA=dsyd?i-pO^|OLDHBn-<ZxM!g$tu@_LBzI|$cTv&TM;G3E&=T%Ejk#We$uz4f0xj~d}J_jx@Wrtkf!ZED@rW<%1iZKZ^79P4UE0(negj($QlO<QN&w!6Qr-ejSG9Ax?|u54Ukc-!Vy9X*r_EC%^hrWbkc5Zi~J;ZhJCR=iYWMg3#nCq6V<U)%|%@E`$t$OlYz|^cAy^ov1QX>G!^H(DgI<W_%=WDK-pOI^=*3TzAB#*xM%7ze93hNc*o2a--WQ-%PvTe$uwg}J#O^iZeVm<_}alnqYn{W;bHK0U-xP|LWdrA;F8K*Je+^=)tZ5$>fFKAt5H6UZt>xw-durauCRCItII34vz1l}6pI565*)E*mX^zGu9TK$Yb=dxEMV0h8(3XJg%SMc^_;C=YS|6K?ap^@+qxBCm}GJHRsMLMm-&9sxtZ77)&?&X$+Yzy=D}WzNBuRlx}m1(+%HzYM%?`fz5fai1kONX(0fL_oaOn413W}_xaE)J$sKe6{IMJX4^&A<95BFuY+^RjuHAXfFvPwQu~HtGcMhLyVVNnNnvZPxS77%2SLjftvp-M;Me?cxY4?HC$M3Is%)m$Cg*az#V^3>9*#MJ9iPB*qaX*yLI5Dv0*M4KJVE%T60*GrHdN~_h43vT7h_=~qwS^TP-I~Z*peH#$rEG`uWeo7)slA$Q6u#P<W5HyRqXNOsR*^SEc4+_N>t^sCKA~+I{=+s6Hh0c94MP`aKYI6^gz>YRMl|h?c8wh)k7$lr^M>q<lpk*L78l`~v9C-rDrju+hZWTSY{v){9J95Q;4cWF-CXJ`+kV!*GXJMv?FzU_*zR>tHOzG|X~OHXr%I&@Ies7XR6Qgo^NyaM>W+^K!oeHYCu?BM*Wc{;wDnYLsyP-hGtXu-Jks=G&$AKJi&I~h7{##1z7nZ_M+c0_0}MQMWb-DxYR1GU!=w|iJ{|1~qJm5XC%82>@Qs#JU$w1i4O|B6LoVftWbn!G5AMiBG}45g{h9%<4Xoc4b-`HF1*Hz0s16+9j5Q6U#h?z{zQO^M7jm+kd?hB0PvwLCJFgS^bhg=>+~;dGf|txhFID_>ICv3XQSnoJDp+RQSy*+4%+X4sz!3lSKT74_FPU1G9594F`DWf-H#exaXrUb-^X1YC8&NAQV0M?Od+mnXRCiSoSWirkYd+o|<3ar+FY=W0ef$KC(mk_3_gocsmKJ8;B$Fl&U>Slpb%Q*C`r078%&|$%Kjg=AgCKs8XZm2y&+dWy8)Uu2^I%<XNRmD%r{lv7+#p0Ecb>{|7;?{u#ognf#UHn1zyFgLe54xQ1zJq!d;$5Vry$dTld|LdyNT+Den1@}AW4B^m=;yt0x~6Vjo=JsKZM>$ahcfB=#XU1z6bT+@=b%vqalSx%VWBVpQ30}T$%TBx68*MblTvUklh&km3feFWsgM(8vW_UT+y2cmKr2nmalFQbtMOkoSt=uUiQxXD`aZ3J5tjff&m^}_Ei(}g}8EEQUsa?s(nSV4Im9#ZncQwZ2!vZ%yx~|`qQ<1zf=b$Fd@6|n`?5>-LyeE_C}(DvZ1K=OximwO*Q7txhp@@bvK88lT9@WbZD)ob|Z^4><A-lqivz^*Hdkd+?x>ah4yZMYE{}`dpmeGqH$CAYsA^;{Pw0El;`vIj#8pflE&277cptrvA<XSI;F$jxx55&sQ&o%lZ){Ij(Ez^P+}(PP?`CZTJnHkflnP|GWt^<yp~DrO>IaxYI!LeCuKcWsi311^0erCX6%tS%w8dzVFMX8JQ)%yJqmObVm&xa9VeQS%J^zvK|$w)mSV?qqGm|80ny`$MusyFuKbF<vPhdIw`2a2`ha|%Y)T9YvS?KrhekxDCxF4IjZjJbs!AVni$GpKk*gJK6B6EH4xH>)eC<uoQDk(|NnBIowhP9=man{zxY`vFWsM1)i)^J*c{5K^W<#00va+3Vmo?1q@cuwRfPrQvH?iee#49RLduC4t<<sy;U>`Bsyz9X{035TWA@?&s;2?svr6)F~vp-`xrvGm~yjm6K)Br0=!-gd_0OZtBKI;qYXk#L>s6KV2GyrdKYg(;=#<rdD0;Jv#1$hJw+7%W=3Mx;9Y(DZ%pXYe0$r^yVF+aQZ!Vfk9r58JRO(G==Y>^Vk%d#IT2Kv$t)(k2g_&y|~U-KcH03lUU8B4pQ|02nyV`_nCvx1M91%k0RqJV@8Huf|gFAv5$V<(GPnqW3ison$KrV@0XkI7j9%1zzZrg7Uacn_pV5U&C5I;etY!&`pyDxLCZMp`X#QO`V4`dihD2?hK+BM}J9;d2J#;bnJ3`FvS~4IB7t<syuUIwB3k2I9EJLWd!%RcRc1!ey(8A1(MkflKeBPwZfBjm80MGI0eakrE}Hq%yoI&6Zx=5nw^u9jmgVNm^8q^bsh<i0iB?$uM%?VSdmfu~7oWN+1tcXtNCJ6qvVY#p<AO6OzwY<7JF|0V>D%sUcr{5xDX}O4qF4OpuZp>$n{stc#wOlrKV6`s&Y4t55MGb!CdJ`gZHgAFs;JOg3;M^pI&Igh*G=5WHKLbNcF75mM54U+4ja2H|E$7lw(YnoL2pG%E#@tn3D<iED(eOtU!gUIfV{{^s06PUo94b!-_|#bIBihDl#CU8Dg<YuG|o6D74qNnaFA%{|?N*(@Efq2PzyPT2<K?WU#cfhtLjI!lgS_+Kz8Hjb6_2x|o)X700j1?1`3L?*UsEJ8a53{psbwG!t8cM<k(&@bip*V^|3FF;6~d<M_s4GGa8=yuf5ro?mJ2YK2ypA7=g;}^jM;JYBHu8VYyPT2C|@uq&$$dcNMKjiNqdb=grNxo&B5Embmt;3RRd3-}4N>eMpE^`LA4u7I}sRlFqSdEu6n4=Q9$baXhR)(A<Nrq+zItY>GM!5%^>-oRgLvN9=m07fKCtJZ4!&GBB$s>p4P>f|B*Bv<uXku2}nw5$98hm6@RF!Hd-Kf?BQR0<c^VBpZTF2ZdL`0>hfj&o^)Hr>#*{_Sw-~PbOloSn%!$u_md#6y?8Zx~VZo-fM4%A0&jrXE5l8;!ZR_F(NQkX=#MWj7D`(7HRNjtPMXie+q*EU`u^Z{g9YTJNRS9awB?BGxsS;`}`K0KvRr+XaFTwomnLPw^ZllQ?d4-4YcDReJJ?ypKSCSW`{bC@+o6oweGoZ5qvvpoL_d*b9*`T93<Jb+C3_p`5$(5WT&Qt%_w9e<NLC)~#SJ0hX1+!I$Ehmqjs_G?^Y@2f51La;^>@Ex*E`B4;c=`EP9y>Ac5FnuK(TC`G8?P`6u;x0j4+IRDcYTQ8_M`Gn6oNVn_^VyYI<^7R2mb^iD2V)`$%FJLs#xO7@rh9@lEQiNTzDFhz^Wr9m-RcVlHbce65Aq|!cJy?tG2<%1jJBl0+-jrTfd+|;LdFs7r6ayYnWE3n<Y?I>;g;5}7^ceL_JX%YJt8865Y>a`vihnqu>Ph1){`@2LHfU69oBt`Yo~Oqdt{dIkvXJC&SU$nC~q$a2>hUqAIXpRF+s52clsbepwf|lT>QZQr<^)HHjDKv-!hze?@&wM$g9rh^m0lD(IS$2ucK6YTraNBNoP99dN2SSXpN&^2i=jU#IVSAa2a{`VXT)OH>lV*T)m!0ZW#4E64;XGQr@0=Y0w+NDaY1_wpC=uYapm(t3TNRtbf}%aleoBX;J0c+2)^3_9K#fm>rK;G$0gqwRp($8L(DblUsp1^N7XI5zq;<6F;yH>`Ywvv0T7(j17?u6au{+zI#n%iV}OZH}~YHIr~zlgzxePkBo&YCI|(ky8VVjx$d8PDQxV)xg##BLjljVcVZbOz%XC%j+sA*1!EQ<zN7#8MYc7K&&KY+5_MGcSNYuy;9ilLlX&l?<a<<wafQ-#Ii98?z-G`Cg4!sL%0nKZJNP3<nd^Kc6OA4eoc=rdqN9b^IFAQq^O2e{SjP9#4rYoE*m4m;hy2x0cMnE9haA8mAIXpWTZ@(dl5EcYQYyz`s5%&_ys#P6L}H0*OPVBQ32LJ%YWB)(<Kx-zdLnobUocs7K$Z-d2tXRPSc)yTu<Syo&6Jlh!E`5ZE52n|F%dJR&iq<r;|x~?Qx@neM0>445`S1IA!A<IvA3H2mU(sLQxyJ21+Vl_M$ofTCl%68`fIieevLZtjR!ie_DtK1?S;{1SvKrPCN@A7xCQ?b;=X@=^5mb)Tn>w(1dy>Nrm!R8ehXYyJ-9j%Sfk1l;AuEACITPntiswci@6y}@)D!NrJC2k)_}!;{%ldBvg#fW7?idQZcxrLVRo)byVXWJKloN#Un84{XSiKaU!K6(RqM0Y4%B>YS^B=k#UL%(Fc2Wn{#}^(f3s!GU$iAR_1&NUM!1xx3eBs@#GhhLC6jo1mN|7@m{U_>PVLRvUJ--eFn4rLqznep_a{<DBKY&7q2kYegn19lE$2N!|48P~pY3ew=io4pz0LbjO?mq=^}#2+o#pL`i^#sq>gpO`v2>ogk0*-(8Pah*q_Q419VrxBV}WiNI)DcnMFCqI+BG*6G#DCIyBmB5Jxu?OS+u%5+wBf+0UCxHvc^^J_OHBdo!sZZl18H-2hP@s5LmP7bs{F_yn2oG0Czr**<z`zs;0qG>8nLy<g|vJU@R}!uxI6wsgk|Mi0190LE8!Q@XR4KY_&C>=^BV*57;sap$!qd1y{he)Kt3!Wf0$5e!J!_y=shCTS@p^&fxmVMKyfh74=WOUzbXlcd5inEh^htbBd~8-p!YgwWS;uJt-3^ggq&n(vw0P=)Yh%G;F}oNN*sAH)ae2s2BZr6{NRpOId>=7(ifQesegC78q>#hr6mPEh_n(VO{0(ABlQQr8xy2&ma2;V{@&8r{)34F645Rur%@XvnHO-ns^KjHt_O8a|!cD6VWbVe_96EzPPn_9K2m%my`qUy~_i3kM<1o_hj33K+O!PRJ8S|#JU)>BxogvEhGZ_{^f6c*qX(d^`+>lG4r&?8n%avy-%oW<~th43>zdYG|}&aE7Oit*Bm+A)-X0iaoXik$)gUdMVD?1AT3DL&u3nqb9uD7nkQ$++;E&)q~>F}X0Vn`Qd_$R&$0ZYKY&v(&Bt;xAIQbBZEe|RH?xdfnQ&`-H7C>7rCT-wakk~CB3sSo-sV|r56YN5^T5P^>6<cFH3O5;V&%ui&BI?bT6<L3XZyZslblT~&Y}Ixl8sZU>`eVwxGy6ldxm|P#pwepgEhm=NC%+ZqZo{um3E^%xg$#UfH~Y2!^ZRPJa?T#-c9i>`@PV$F8<S>c!g?8%~t5?lsaimd}cl|usa{KX;$@Y1Ds8)bU-ZtQWJMo<EH7AmtMoAr`ti&FW=ygR)69>g9e8(ToYMJXK{1I^uS58b7I5twCq+GppFr1O(T+8;uy*pi9Wrxt<v)MFy=ef5@wUF**_gRuo1hW^nw~(^8}+5i1OUfVA<ov9%Wc-g-txBfr?d?*yA=2w|4X-vt8Ra*@;AkX!w6$ohp35;8`Atl2BJug{%Rvx{UZdtd`kAi=o{kg*i4hc&9l-^$tIhIs`dGXY2cN!Z1hMn`Oe#30UW-`*9^_I3^4Ye^*gdB!J`pJZ&iJR<c3~jqiM_HM9_FCikM!hGp7M2}9;Nm6t=yT6TVVO#3{5J09<zN*LnB4O4B|OV7{dv1AK7^zG=vkQ;ieNh41gmPcOaW6_O#bfOt2N}v#@TdI)BtSi|<sYe9C<fvqY3B~x+GPM0E2*eN|$Lb=q@YDIstKeQc!H<YD$6L=1>eUIp$|K3Coum8qbarRk{oK@^&FdOqqO0?|aeez-BD^yg)P;GiM0k#JQ8R$kq<LMRro#z?YT2b_ri%U|$S8E?7iPp!AJN4Omei|q-2PaxF&f%zPp8HOdQo0n6;A|ztJ=vPJc=X&=~JxKc7m&LVF^bY7K<Q^=cg<{GF5Ux0GI3F+9DvZ3yYvNY}CH7)zC<Fbrv`tFGHeEq0vI)xlgqex>q(qLGA6E+$c#<pH@$8lujFE<?H=3qN->)fJT|u&}y&Tp6!)~V2!}=0rD{$&n`9FE5mHB+%NY^WLF#aA$ujW_1DX4uI!T6%W5p%=kY5R1S36K6T?q-nDkfeNXvG^Vn^f=@7$G|nl&I^G9|DzR!7fI?~*A2LIVwpL{yUVLnSs;T;NdiN!Ax_3UL6<#X?)03T;E=4(ljZ={Q_Zm)n@XYWWjnS-8=+1W~LwKFwHtBN~bT8<`cE7+f&hgb5h(i%03qM$mx9>U}KBV3y^EdEU<Y-SHfUxpBGBckwxQ*x^5ToeTL@Rd4Z3LHDvHDUR6TR;VYU6Zw{lmNjn)BcW`Q=S8aeXj*nO-~jj4v_CK?$<@-a1ho*CI+MIPP=p9bL}GHqD$%y3xSh&Km<XT~%1;~NGvp;p?^)3qSs7}WYyutiCkw9z0W((UXuRNDrXiE!h<Nk9NMbdphcL2c7dwiH!7>evIDuL-SPj=Yp)8mlO<%w{MBTB%?0R-F<nOLmJPBJr(*a9aRpNZ*H#-W2>Z;h^kl)|jm?66-6!Y+chnBsW2NYP+y>{SWv;S$V0D!Mz<UtQ_IyY^qilS=nB_>m>n@pQre^0j+zp03ea(f=d<gc5#-u1Pax#5bt)Skrv-7*HCBqH+v{VWF96ayy)#`Xj~5VgXKMa!d9j9Po*DA54PD2%5PaHjP(AX`XWKV{U8>ZfLlN&ccdkymkYn#S<pmJX4czEd((!DBEkCua;Vvc(!4gp*^mP`f9w1(gAd9xLJ6xoylq29eFiMR?o4BV=XaE3r4lESiM6xrld$evyV6?(|W=3)p?MboD3eEz4i}cU~PY-yvUXrk+eK&-(y1^0<qI0(6)?w<{5ag~{ndg5~p|BF7Bvm7s##y~5IYuzcnTC{k8vaULwc7-Ms`^$*<o!wa|m?IN7W-*sun=gbP{J3fY`rD3=nPM}kVkc1cS_$GzfQw^y?);g3f*ZM4$5Kq)x5D96>MWZXc5hGD2E{Az+_X9Fj{fV!7HcuOj`iDBLt73PqIjx|Lzy>`KUU%7Pr2rtDR>BR{10=Q!Wr3;8_j<q8$nrFK>9jhS_!s!CjD-{Z)-dy1Df-#+fY~gjtsH0Z<hoi=9GnHk@oX07$A)i-ubahgHj5Dv*JDJ?!2kbe?@eN?>C*I|I76HmZrmYn-n^Or_kZ=*U)6v0P~BaW3n(l|mWGW54HC3uAwXcTWo$qOWZ{;(Wh}fvEU*E)#R7qZ5f}?LASPijEWCvsLdX&bK`&szu<-)Jd7kGz5pk!?o8Q>goqvCwb;r07C(iJm_kD)b(Dfo!=yL|J-Curb0E;NdGqcGp&3uU1<2>^=Ip7K07o#)oZ7(+si@_fyg#4o~$VfM`4i86zhwprDs+(|tWRO%#TsnQ`B$z>}F%3`{Jq%{Zuj4N+$uv|&%{wjPq_D7HkRSY_T^h5N1Gc03tu+CtkAg5FCMf|4F<|!yKQIDfTMYxcAxWqhItE)TqF9~)+D<y<47#N%<2}{!dcdA!tT^zKkA;?&TO-oY0K6E6G&^h#E|Ho)mBv%<R&U=i%3g9`RHE$g{!w-`;hJZo?4S_h6GYjTk)#G?eb6fp)9eh58`L$=2HKlv1MQOBUYbuhjy91oUlwk&YkR-XBV%zk(3WUZo=J=T@Pzwj#H}KKWnRe_f^Mu@?-+5H896Sh`LEaR>Hxe25^jAMdg}q(!Nyagn^N15YCdHEUfZb36V-RGi)sd_3O<gpLHA_AYC-+W3k9oZQ~F&#**vM$(xCki0k}g#^SNpj8NE>Uuoyg^8%f;$5#H_(!f=0OFvE1<P|jqaoJwm9Zw#RDJmy`T<}!4+t6z8`^SW7X-)V#AWi%1J1u&heSoKkX%l_45!X~Ejf(;!Uvwt#x8T=$SM|AQOhA*!O!=)Ygc?D0pKm9CGu)9PQgqC^Wi>DO9d}CeHlWWIi8u{D?u>@YE{9>Wrfk2o*5fmlQ*no|=eED_AfcdD`naoQQA<)fPeE3QL^f1R5gD8A?^njZa3QG_O=32tmF*Zyq>riC<xtcm&NG|5z4R$`#N2?<~#*^ez$Y2EW1M$0w@b5U1{lJ6_0#+f>C{7^3jyy={{m2aT<TrW}DM>ZVUj!`>T<s=+1KF6dw^gb3JmL6%z6&idP}z$LXgTg#6RDohq8GZpa9a`XlSegY1DZeqB^UA<u$&or*QBgAQJi2b7M)P}QJ?XIT^ipIWWRu2suyD3jdtD>r!M!IRNFe0KXOa1_((__3Be+sanEZ~1EWOo=x;vqbj?+~GVgTq=YZH1%1dDX&R(8=1t&b%kxg>`?7^e`MDe#bo^dLS$C*d@WL9p%ZH4HlQx7wGp>GRi*@-StnLxUcEz6-oAw$l-J1ReWH@4(-=3#ys)8EmDNUF|8AUye)leBvniP7ocu(}qbahAi{gV8gands6ErudtC`p2ubKT#rM9@#yEC7D&pezR8FW2v^kFvFm=cubEmFm%(pyncDX9SdnQ%PokTA7;6Q7Z%)+Tc}@<TiDL4?Xyz*5%J-)8kWw8`hD7h*nj`x9PwCKxm;D55(`c~5XvoFE~#A1Gg$7ebH~|+GowKXhiQX%ZK`4QM5^InBWLeE9_-&N=P+15WzJ!$k7&0x<sZ0hJ4`+Vf7e=f))8!bHU~(B3Hh|-q1x(T-=!f^&yo^-NlNH88HKVWy&f6K=I}E=?j<1lxl<6s|5m*s77h>#23JTQ5U%h<!D50yv6n@2LwF~w0tyzbIQ$<7tKi=Wt1uj56`C1VVf8##!5^f08<S>Pn7kRzqsyOz3_(4(^xa~c^S}ZQ@(dOf->Cl%)#71tg{r;Hk4Rk6PDfhE^+ExcS8_Yi$^+xPs~QTx=PgHqGAAGeCUC*mbKgwV8c3}^iROGGp#c4>nF<O<<KEB}gyh_+XGH!Ls|fZ1UT!q^Hh)if4hTaHB#D{GhS;zaDWFOtia8RI2&P2Qn0XF^lQ8=hT}L8yzS?N9M5~n-1Ua6AuGbrKKoKYq1&XY_sSkj9=dJ3+tqwoKR;3=nq)Gq@9-_z*>O`jZJJT+H2k7NH%svggkq%~`+US)ZW&&C`>61UNLGb=~Defg(Y0uSCUV3>j$YRcExwK=sG`+lBx-8|Uv*prsp<G%&Q7*;y)mRuWjt4dGgv;^ZnGzF$mY+2wZ2w^O=iKo9YEYTtOZ0S@l~IWlWb|8h1d3Dc_mZ21QCyzX9;CLptCZv0QMer4zXtCzQcEr`Q(MN5k}kw6jfXl})Ycf2^H=ms%3T%RDp=>*%3?S|B$y0K|I_)EU0}M<dn2xy2H;A?fEqs?X!7+nZ%7(Sevm$Z!yTsMURs5W#ofM&re<E`yZFhplaVg^K<@5oTUo#06p6CWEm{4%fe<+PQ&<=Bocz;V6jGILsQr!x!<@2TRs$^5T++uW5@`bOtEvlbaR-()5AP-N0O2HWd{AevRMd5`ZG9a74mv3eNH>|jcy*vyQW5auvju{w4{ovZePP6j-yP;(k5n<>O7W$%hBmf3P&mex6|6Gco)_UG)9mqDV)D(WjT@(Q5TWf1k)T9oDsdCPAkL_(w00D^G@Y|_S)~F5Q3fpRSPkPOtd{g{q8W>vCGv4LrY3AQYXfp{z}j)L({|6-p9g?Ht^z;t7<_ct=s!eOz)$6_cgPB?E@cJS&do6l-^)Vr>8wB`(ldTK7(O<~pBIK7|Cj3%zd0I?UsSx!OytTximAf|Z?vTWl^!%L6j>-jv6e1ToH&ZOTb*JmR?uqoRf**5R@q(rU6a(0?5|W@Tj?zN2NrLl!9?heML}_=uOo}=Ku+>Gq{j^FW;sbWx;;v23vyPRI3%3P$x%`+dYlpkYk5(UX$y8h+KR@a49ZNnB_T$sNN-79XHL`3tfj4|nWLY5;N)+~23NQI+l}$QvYoVSSGra8p6FzCXI5#`(ZcL^OWw7Gc(~kl49+`mC7BdRsxz3)wn<eV9MH)z9-w1o;OU~o`Th9F#c^I=uasxR)W0yPIO*8Tt`TDwJBR$%-LGDyyu`v%Hx`z*AuX$VVI?IHPlK!1a1w%AWbc}KCOH|9i$N79xOGka@Q4p2&(Gw?(woeYF^w5pm6zI4lM?%mq;e6JBUvA!dO+@vH&_f7K@yUZnWS1Ib5;15E3%QKxS$A>PbT5u$*M;l8qyT5ZURIiTY$Hnv?^mWehl>!l!C<dg$B1DIx<;tG><|W=9r2VBddq8ZWNlN?_%_{jQb)lE&Vf-9N#_aaYu4|a>hdy?~8c<5QnV=FJWbpes4i^ukJbw)5wVIYdYk#_Ym=n9Hms&qyDb*U%Ak7ysd5|neMhR<TY`%5`?(=UJg)hSO-OQ2cKWm4ppcd4`<4K^{oohRuErb`nt0L8R(ng&DFj74h>~JQT#$Uv}5Os5Khl)Nk=Vo4inrcB-U6u9#twmDP_46ZxzTqRNpRk_Zsc2)>jXqXlD|>Api5aASdGAQ~ev*^RIu1xMMR=+R&H3`3QfV{2<)`cLkrr_3j3`Jc#Hh$hO*7chYs>DRh;8dv8-g4&;V=tktWEauv0CBMpA0qzLI6Ovr5|_5U1@$6-YRalpo#KZMi%Zhl?IzeQiq3-A68Zf$+A-|BbOB8sQ!H~i#&3%@)eh^TV{Ojf8XZBoNSwRP2YWx?52T8hZ9{iJTxf6H;3UIuVJ<u<VejxeH~tUSx^J-!I+EPYA$jvIJ?m^fU81F&dw4lH_zxIjnxoMoL~aQ})H4g6+~MShwng`Q204T#d93>}6R!)52=-`Iw{=WnPqH!%M<u*v^s@BWqszGPV0eC}nrPvx~G4$#o^8gqH@eQ%Oor8!1IP*}4d7NI<XO=3iKBVvzG!KQ#XLjUuWc-MMP%9Q^_hyrli%{?&*n9LVOKP2}yK*jLKaB#zgG`!452aTmX)9u;FD{PRd5s51ePPWImhY?<$;>%FMIxh`<f(Gb-c7oVb;@}t<fWR8qLDd{7(i+Vym14-W6{|dH#E3Q!^F=jsz2<5XfD%d2RAWKXd*Q7p6@fv+ZED^h<b|A@f+&9l)^~{U5XVb-wmt|U2kFm80Z|!Qtyx9S2Y<^*gz~FK?}y}&9M3%rRS*so)no1@qc+^~Uti>VS7T9Xe0=QvI+{mmkCwqTF1hICndC>5Pc)TJ#Jbhb2oy-m#r%u+Ap6805$Lj{{I`Gwj$J~9fjfGC&=nQGolop%eYGTdkJ77R?<2^&b<lO(vHZWuqm2T(`3)@?@V%x_>LXJKxq%-8t~4)=8sZd0gfmeJ!l}tuV;q9vgINU~J&m6NVQ`Mme+9zeCxg=e49MVWN`IJ9`rid%P$>P)5vBhO!r-c0!b=eb@i39Fnk5pNtN8pBF8;jKg}?Oip#~q9!|)<h!2yB67f1mXLIMIvT6ipsg<p7%u`tX*0~^a>8(ks)Ry)xZmJ?lp8o!6IfE%-zKZFGYqcl8@EQJa?zLDsdTV|J+;rb#<;FF=MyFZGw`qrhlJTG>WNX_3d6}8p62Gg*ZcG$u)zix&DaYunlIh)*YFXT}&4J+(Ju;&X>8MNZ0f=6m(8G5g-Wv~SODWsg_4i!numf$e=gPUMhtC00szymhY5CCU`VBf#VYh@FO0*31woXKDhOVl%uMz2=?wS%=5PGdo6N|gV*9L!V>N5307Iz<hfbO`>;uSELlG>JhSjcOM;f<nE(^?cgWQLQE89KWKNKf$+DuJ-*OsQw+-|Bx@-lT5tEuJC~y`XTqdAG-F7YPbh6-rZB%hYxxR41?**NaUfYCg)9K$LwV*<Da~wFA=7xMv|NDyAE!R5c%N9QK&eeWP%0&<})fWjEnB6fhr;Shli?X<q$WdmqsXZDBKjoP?!}(|7~ri`O~c^{k7jS%8M%obPY2y(#yWnInY>+TXIKrtH^!sm)!Fp26@2s`Wv%Sh{b>Ei~QpMT78zfvhe>;?Ntl@AA42q-JjU52G<YIt^Y&Wr9QF#qgIHBc_7QEwjkAqgY7Ck#ON?*tj4-}S!sC$|3mFw`2UKLpC7J5{s)0B;;83?UTj6>1K7Vdr|p?-X?wUWb;s*JM?gIx|F7DOwq|j%35NXlR}*j-&#wHn#VqK;|4H>PA0++5mX%57{c*7yRv_jsk@P4_-!Q}OnD;|@jom7Lt+Q-eOBhB9q-@bmsf*m-Eds?=3Ctx&K3~Kt`kQsglP&T=l$uBlvShhQcLb8S;%b8NkGHV3^Zb0*Vpu4Z91QS{+;a{G_t+SQJeB051pt*Q?MfVkzpEa3Itgf6SGtwIcgV*N3Ez;BJw|PAy*I62t^GENgey}q`H(WbmmsJZCI9Z|uE!*y*OrIdQg2XdG!0h<#SzqIT+rjJ2<OxKidY3N(@C~!ci@7C<Y<i}r)YLHNJY9}`td9QV;hAP5^3N(=dZEXrtel2Yo*~?jKPHj0kd(xfRpn`V<KYm<~_aqz12S(`~&}WN=}EoZlraUdyLC3-T+9Hrw)FG5BLho<u~~bpx@(ecQ_H47Re{%2GiEQK_}x|SXLH%MNcJ?^Z?`lJ|GKo+}kF<7ze(>&j4ERAioiu9zK>ovk(Y@ufPVaK}n!y@PyNDSnj6+Q(m^Zh9ADc6>lKIthcaL$&vStXP8%Gtf>v#i7`c<J|5I&Ev`{!d;ZsKEm-Ges2bkpmGjI(&_O~s4hcSh?MAl9RoEBT%2aiWVph3utHhY2I2<5jwv{O*rh@!5PnUQ%AjjC#+n}RyOK8Dmghvu}$#Rg?E=VStJaJGRKtL-(xA=kqqS_k*QoY$rLPa@RF%KWBkto6Hw;bzliP;Hm?0TZbAX3{ieaDL2z^^A?RE`)d04M0tGys*+ISB30`*orUFB1c-7Fxo1kQkPD0E4?H%<M+}m@XS{{-IAK@v6(ZR^s&;v0KxqE~XN1@{22M9R^EkBEOVBldpSI!vd{_0VmbZmJm;dm{`IVG2MdDw55mH%^kA#VQjVy6v^sc5pn&8e~YP8`%!vLvaWdsfaR-Oda%T#8<&GQnnXf_7<$2L(n~8SdLPKTF8r3$c;Y-3|H04HrA~yXtyi59PafExyf3m#C=gLlc*n+IzAzFv8s)Ybj2{8NS(fiSw-epBFsM=cV+}Dtu9-Zsdr2Jub+aMKFfsUD?OfAT?QQkzdDd$cN>D#5eL<2JPZYCdgO=Ln=o?$NxDE0;&5JAz;T{yg3CvSz(d=)TF1|-_1|h0jMDJ=iL?5?qqwpR{N?>7ODA1r|p!3|K9B(^$IW05pNh~UDn7^zk_M7hzh4zpeCQt$Hb8tL`z6S11-2l;*ml0?!*P7j|aM;sDARk;NrjDsc&y0YGeTiVB$muo`ir_gBGuGg?qV~e1)kOHR3p%-++NM)UbRe!O$!yutO2xke$Fw5LPv|a%6|9c(X6LEDtt80ATrwfKp`$K#O;^{B+Ql`tRe10xKZ@fCw<_=FcyivxL4u63KB0x%6*dkt50r+$1K6M-fWm|!iL-n$sC=vtNHx)Lf--OrbmQ0$h0f@-M3LjQiLgCK4yume=R)+|5NFY_^oB_44}GkAvYg$JMY$X8;jIW9#&#dh-2^kAIp;j{WZRqn3>&^t!_#^?f8H9NCexjS%9r%a$XAr8yup@MP!I@hFoz7J0nl020+kOcFd~P8S>u<EDrVmtR?H-ZJg=C2Q7UGAshFh?R58mpyJN*H%_?R|6*JCwDw_4&ZG`Gf-7H<Io3S|a<9yDirL%^vS?<cxnQWNPSI@em>Y2lof)UFJdGllqt(A~SI4z?gR)P%|PAo`5YF1BUd50ynwrqM2t7=XO+{En*R=p@Hg4NbysjUrxZdx!#M|8Vjs>cb9#R_^nsIc+Aa2Z7_mF+P~ZTc1NiY`~%U_sV!_xwmgNM2&rTsTyD%by;qplGUvLM<{oseYpVhHY=YLATI{V#LhTYuL@doLAwr78^+inZ;6z!@YjC97kUEK`m}jEiSiS%_9dL97VZ)EXsM_veUX;@$~tm)w#d_YM;I;td#-bY2G;%l(5qFIT)+fk^#Eqd`i>O2#h@DxHmiYdOq$6VrO~^NqAi47JIkWo9Q0rINCn#38-i`NT6=mZTI;nc7<o?3D`j!19lb{{%grx+*{(S&7o9B<*vME-64ls6J7#h{2k4iINt<9P$1z`aUS1VmOTGr{Nr<>hW4CL1K?>P4!6X%6EugvTg17I(3~}1fe9Q}oV0c{Y_15DLsXj>W~F3sHeuyjua6N=$G`|UHN?nhwzi>fu^UwyDAXWJ;~;q5Owyro%xJnnFg*}9QLf|1=&%BC0<xF@)_I+Vc`E1QEYZMlL~UA3z=_-@=p-b%HPf)!L?rs+PR%Vu!#kXhmhVHu^-KRYR0v50Qr8h>FExgas5&I%6*X3{&Z+;*i*^@gipXL`4vFiYH=!*{z1|JtYq$j24>NQHNdui2y$U-r?F0hd$?{}=lP7Zvyz&&WWm<uj5!H>X=5B!9nl@r<2ocz7ugz=3!GTYbPgd^kwO=MY)@r|`VjcDpjq3)uFT#gpgJHlXrzc5+>0-Ntn1|78Ze>U^1yYd#eC`Y@h5$qT`B|;;Uw>JAcAK}D^utJQ-Iw6Zn|0+BpN-aM$f}-LpTTb&z)_Tly2F?`M;427E`g)zS&kRl3#MoFq21Xc&;1Cbn4y~4o%NOEJr>E+n;mgN?+zUU8%B8W?4HWn3p$y{qG@xDY2f1XTAclxpUv5h`@P|uvt8F*-V*6%Hpuy{o0oao<rsd;J~el<^K`SzHy8KT1XtW$ew-M1H`S(L6>WZ#8;H4Ry&q0)^6j_>>csUl9t1_h0qMwBv1|<4_lab@{ume#t`tLdRa!CmFi^#=GmmiqWoy<zR&iM1hGQOXfkgmHRvK;(NZJL3Ml>a;aS!3DyJMa-v^F{CrX3ph9p}G_6(H3V`{xqG<ymzV9KnAb%_LYN0dX*YKvtN@;Ek+2Ge^v*1u_N$L)mr^>04ZH9wbUnj|rgGWKy>II2#jG(ZLt7AdR;bGcy3;1e&5Qbs;-Tdbbh^Ur|?FkC{o!^FnGWSuS8<S~03t_a}z~qv7AH{#A_n)4WmI5>}p=E<*JmNwRH>+nO!?z+g<v-HwSY53JcnxuO;%=&kZJ`Es`cMDwEayBoiNq#TnU*pTsed#uM~>{wz+&Pghk^~@gij!E+TR;~R+r8+581DPLc8YI>rKhiSkf>MtqK_d}E*jm+?hq?T+vgM8VXq5NS`nNJQ_{g$mj_sk)M66`24Hf5{C6*#7HN*ih`$e`PWrr#z`SH8P+G0XTKnFerQ=gk8hPw?$KB}UmdJIYxmfR9Fby$km9VW@2D>nD-d5(yzVv)7S8dneqQ71!>EQX_=`;wX)M118xxNd@F!Q?$-pfd)%B|}}$f+0@7J-Y8fRMa0tMd#B|X-r35IrsACcD-*~rbN7%9^qQh$RGo7cZ!eQF*O?obdx=IvtBnOFSa>g>Z>i(3TWPn!Q)jRSaB*|a4Oy&PQ}|f{HM1i*PZauB9`1wwch>()z2^^1e*@hY&v-09%X^8ly#6DRmOmxsbl&=dn6ZCYt3)$>9$_Uo7<Gxu*y}IOpZI_6bDUfTeIxWGjQT2w+Cp*twg7)<le;%c)_OUftP=xrH5W5eJFvOtgkQy&5?t>5%Dk$#AuPn?`URyYqN~~Yw2d&QG#LV<**Lym#>w<0LmprQF?d|iTVzanR=$IBhRFFnzN8nPbxTjTK+1(p#e`4pQF|T=Aw@EP5M<B&zeX$&qc>85$GfqibHw+%7SdI9k#v&TfnKwi<)c66P`fBIcQl4)<9J}acnSo1(OKlDE$|%-J0Hr!NlF^U5>!8Gt{QE8C*jdlDrPr+Hl4q?UxXBjZfKf*a0F{M()+PFRfd|y)Ba{owk2W^K*AfE)}+yR3T*6%?M&Gx28#wf9@v#(8@l8Ri==?;<%5cWMNBWPAAe<&s}9DsX>Vt;`KUl^X#-kCIvr&=@_H-pX%Q_hrIpf2^UIQEsJQDT<uJx4+x!YuN^o)uidGLVB?SC^AZrmxBg7^`$JrX*oF8FY7VISf0>`M>Ys1ry)cjYT|)J${5Rw~2&mJpq*y|L4xh474hI2%>`n_cuoDU2VhtWcG%5=5{2NJ6GBHuDE_WD9ED_QEO{cLNk7nqBme`E`mggBuP{5?*3daoo&ge<es?qo%L&)nX!Kx$vs8u#|rwg};S0$XDNlYEE^(INf7O<RMEYudF`}n$H%gW3mx>;2YGQryPIOOI^(xVpO<j#r6S@Ul`f#H_21*EC~N|n#;t~~wq->j9MkK%2Ark0}}%%a+;2=uPT_KVLg<`Mt#>fd$!TWnm0o%|MZd}B8gw{ca~54<ybCM4hBLCpvTQTyHv4*@t@sP6dvs#*~h1PUOM+W~2U#z1s6^U5m}9gz<IcD@y$Zw5%_Zm=*SbVpYU%&+<Tq1sy67I38%t0g)9Zg}tq4>9DL_>G2NS#7F278VHS4K?c5!W?3BIp(U9xQRQIBifz8o*f1l;AP0-MpOI89a{$xlbwz*{)K{pjbzVbM*YffG*ywIL=+jN&0QWGz5e?2-JZU-=f{5f+QP3b{My2=PhVU3U7q?6^VGk?*V9YhO&{g7-}mV!3L#!Q>L+a5^x=Lh{dR6!|Kjh)C!fA{+Iho{jpGmBed$yGfu5$TpE8|YTo$xFot>4Qj_<k`JUw{qu6i7k`BGf{w>tNg@x|(82lVIvQkT;#EA)WNA3+Vh6vN8XP#%;I=p5{^KmI3ktTBZpKsIukE*Sd^xKyxze6&10Z%v>89090c?ADdE&<M7pdK&+iC!$p{sQ%Ayc%@)hm9+1~8q+^LE;$dDswfi$c((qDCN}#@P{%ucCCv_di*Fr$VE**z>*G__{Hy82oc+*v&i1;5Ip-Im;^*OEgE8CqIM@)-bva#Q`G6%ePac~f9Z$&=wuUhe%(gYo0QrNYLxgkxDqoGaLwCV$)9n0@n#=3maw94m%d`99%ZVM{5jD<q?at|hC1qRA!As=T=y;QUSQRc`!t}16F2PS%;hF3`xVhDMRwt)-)Hm#}vvV#gt@_2H|4j*xC|{u%%1B}jn179M&wH&0c%2qGda)dHdeQ#+!wA#c=k0;gc(Sqc)91&hrw>m59)C9-JgwZ5PscMqJ^1X>POeM7dnXs`>?fW$+tQ<+e|LVI>fD3VcaN@g-sXpG<t1-_dcAfD(e&@<FCIND5}d~`9=~Fe7Uew41MjRO=>vK^y~t_XUW_6;m5vwfyYA%gcm$oBUOD=eqX&L=O5=Hs5B#~iJiS|&2eEu{_U_S#&m1RS`$;=hUtM~7sln%ePnt!{>uTQYW5bTEJ^$kQ7ybN{P9B))<H=uN{vH%Ue$Tt{^!zoH#zfx4A*FF~L}~0$Gm36TY21<};ovC<B-NdY85Fe;0W?t%;hr_Aok4k^f!Vl4>+6N{UjjJHnU#v=H^7Vndc3bF0a6%?JA-MgrAn|NZ}Gd;zl9e0c~ps$3bJ<q;GmZ3Rg;}HO$YJEbc>lC1-UyzHURQ{!*;22E5L6-I5~@h)*;k_M6l$V2w!LsCQ%f!63mNYr9f@84aoSaPJ%(#@|vMKgQ8$=&6N%^pgKd>H=uZdJm`4Yi<oR>BoDBoekMXGG<iz^wj*b|iPjepo;5)lYUmbJACM+zBUu1vZfAIw50a=;Cuwu=Jxung6~`acamNq1F=W)gAgF}wxao20OfbqhKk}_TiI=$@sAwy_1#bWduM+{9L`N&cd=;|B;D((aINVY7P;1cNHHouQUIZAA4S)s*;;i`wKEyq=T--Mtf5U@M_tlocayI};gBmq7@^RGm!9SS)Wr+7SH1n<Q?+wl3=yxK>*?JEM$EpN_Ka_aG#!j%khd7lCh~*@jdwx&O(QprVRBqk%hNn%4!!Iz#Z13G0F3bH6{SlDNom)~b0bS#NdXZ^i7)=Wy{S&_<cC|@X7qdHU3kZj3i)3{^$xa&g!4?q6^lZT6X{ddXq#-N5k#zgXsvL!`-Q=)GNkX<z9m<B`<YU73+1^PKvT<f<c>33wS_sG1Q^%BpZV_@WpK+zL>M}3<%Bka@%n~CJRrQlUEe-78PmetPqVS5cEtp-1$p=dYn@C8_%*O|D=0tP$C#I*S!Rt+<P*Q5sCue4c<0rlOQWC4-E%J-OPoYwAcl5K{ls^q@!mm9;LOMb-g}HEbmG;nnj)iN}+z|M)4JKJlL`99M3zL;JuNvY^Aza-CI-Lp7L^-UE6q_U$)DeFKu3D3S7n2IHLLG2y4L><_KoTVYI6}cL0a_u!X@ZG7U{f?jCFuqzM4c6|LIHYaRJo>9b^@x%B&!M2qr4sF1#t4CebN-H;f_oWiA1v7K**Bek{W&8+)l?A`4_*7{q-(C_`NR!y6o}G*g@7MB&gkD!v*9hB<N-U(uEV$Ig()5b`vY3(}GEeOA0dr{}IHc@+NL@3E$FE@}q*vUE4vhDG!ouTcv^d4-(#+8-ZK6DhBO*0n6Ctc4!F~8_-$53<UwYLBKH3wZL)BPk;X9ge1tN0hZju!HR1Y(2k9p#Zx!u+K=jAXJNR<M2N$-1YBq&Cka9A<}h4Yn-<(qEL<gNZJce|L=%=Y0}vS*+;2fDtD2T<$b2~)z~@9-+S4(>Gc+?E^19k4-WIW!Qq}gHZe(@-6dBw?sAEU6PY)*gtCN`7_L*MLwPHJ0L6T-n7CibQX=X{7kL%U9`q)-kgUM-co-pb=@X0chtnS6;eE13JZPT0&9eI1bH&!HBsz{5qM{ayUTPJFmMUjeKCwW$qiYHkz`eCK$Miahpy$1?Soo{0$DZQta4~WwI%*eTJXX3s06sx<rqQ65!Ega~UlFWWdx^(LDs~ovf|I9t<l1dl7)ztCT>*s$lyN!0Kc~OA5puao_de_%B2!;!Tpj{q|`gLUlc=Fs6m89kds<RPbDNJZ!*GFcmhl8Mkjls-S^<*4y5|2DobY#$yGh{;(Cacd3h%K{&=DC^x2kyC}8fAXRk#T2kf*~Dm<V=bFF_;e);qIXP*5e2e4WGZ5^oui_)^N4-JSP1Wc-oF|Q>+l&IvtD~SWK3ogK=4n;&UVEHGYnv1L2w9VWVfy*z@LDioI+1WRj095vgAD#GqM{A4sjFE}aY-A|Osyi_;NvqJ-TsTz*gEhD9;2IyY`GHA6|r#3y<hXdI6o2|P*<lWgoIVX4yqawh21T~@{H&lxUCA2tvW>ze{+f5}LyrI1akM@Tk$$}j@KWN-r9AC9Vds?K`ian8<3KDNB&xgVR4Ho3GUcW%Hz@fd_C-@atPX>l^6D*NXdJFA8vb&BDHts3X+R(<ewCykA&lxUo>SpBq~!D;X_SS<g^m&I>+<h{*NEjE(KeXVdqk_l#lVj1Wu)ok601J^}yA6TtwJapFB@oMsUV)@t5@`z@wc@N8=-kI1U2r;*A6-6cVo53xVc;F#>>JcKZw3^%wTjs>5)!@IkvCVp*#T!IhdkjR1p4e7Ci53rL48p1%T_>p;j2H>l#md%2d5#(NQ;uRCa!=kb$xR}aqb+r=)j(f^#*uzTX*sg28j@oZnXx_j1IEIvK*2x}_HR1U9r^)vhtfHxj^=_>N4%gr)V*AHsG;uAL2qW0Cdv>kPGpF-*omq7H^~s)K5O4WLex4`a*LGYi`aZWk{FS9H}$cPM=WAQv4|1nBd@XLGbJKrLGpw8(8{A`uC$Xo1l>GvC(Q-tSd6F*+JGCa2ZkO&JlJDTk61iCBBKI%dT{=l)Q4ns>?AbLgM9a*p$F#fH8_Br#A}HT9awopOF$ZR$!vI-17s#R#-cA&gOC=Z+&s_%F`gQF(5Py3^N2GwA(`Cdo2YJ?pv8x)TAuUqkYMfgRvw1JIFt|SkF7j7U0(9>U>5w7iUs{~W3{b9Zax16S#1uww#M%YAhwYa7?9=02H!>-m}B>3SQXY;j!$x2^bMChGGeIAE0JY(oGo8zZ%F`SK06iDttcuQvKdDD+Em6ylS*O&ch2r78YY-fiVy}6rXih-4y)#!s|~QA327IpeT<7}??f}><sh{gBE5W(gi+c)-`hQc+;$&)kk&A5e@neN3LE2s$a~Iy0^wP(BlEEP@m;1$@^NmfP#_DTKo;VEejrSJPx`xX1*aMPFO?Ohbc%E#H*P4B)Ojk86=!)d;a!AcG$zE*i)4#}12v_Q>A`vBDSg!h*PB!}^yP*kSOC@NJmK=@*M2t``X>)F?2(wyr1^OWqd>F-plNxCD8Q&lML{|cvlK-04tdh2ifJgW>}C=awXiD22$Q%p#GgTVc56%$e4Pp}=%iJQR#@}GTLQl{1S-Gswbl&SMZ;97TKdsKO!=~FVvWggQhxlKf2+6Exlsc<!-NFJLHKeou@lC!SQ&B7-fJq@Ou!pzz!$*+S2AIS?IE_tQC1stc4+-X=t?YjlDg4!>-&@`s|LwIev3h8v5upN{|D0I|9l?rp?JKf4`COl0?F!y2Jig9p%(wl;JrO(5!aa(ze=M{&FE(a?`<@Fr59-Na~*A^#m{lP_)tRpA9Vxp`)vboOZxm-1#;;=hB$OoAkUK>afpkC%lFm-x^x38b<-%$({Bs(L6rT8sgYAz<v{<MHa#o5QFt*LK493OJlck$uaa+Ehs-=G>pTwRCuf;?1OkEa3uJWJxw?wwWE7cVp4@vo)ZLn&X(->G?|=UAt%<J&+S>P05sRK&bhqkJOY0MrxGED}LGSn@FWx%+EKE5t+wM$h(e_PioJ%j4&y~ALMLeRFM2bvPq|`1fV_taZ>8c%5FV{ECv5;f$IghMzdvJ~YVZo7LiP`W9f+^<r+CAm=SYo+CGEo~@Y6oL-7;x*h+)*^LGlGVRJdgY>L)taVxlKouU&}~=IwviE{fqpRlFfHi4(e__g|;PZrGO+~J6Y%z%!qcZ?GJ>iV9NMCF90ft!OzL?YhsA{2fzk$OXoYCL#}*%-=h&~ZnB>O#(*->c|&`Ty+Cf1HzV|7z?tnH(2zgNBiwV@f!hB)KKWDm*LP0J$qGkyaZ<`xm~Q?RG-j}Wl+@qyMaV!EBtyDKlu;{~+hYx^=}P9PlR4yH<<g%YH-CB(&kiRFNHqi#wg4ERjdI)UIE2|+0P*+-?S~|YZu;JNid?Mm)IVsAmn@ExEKk3}{z)orrg}xo<95mUdkLOBz}7Waa`utbaJ>>VOvc)TFh?RENV{fttWh%SO3;HvzA;^#h+-M_Nh*|+10>9VqGCK{o2pn8z7_gN5f&jss~r$OO8HGFU9r5Wy%)y;Wy~W|5&=HQyg9NYDxncx6cUJgyFfQuy&F4<DcOdsie~A7{aV!5S(A2@Xa?4mJ7P^24=@=1(6&EVBs!&+7Uyh##yY_{+rKH);22yzY5UiGAlpCBxmmV<@e12NdDU*BqJfv#{*^dm1A!i><UF!iHoV;P4{=5_k24s7Yxf?<l7Kw_(5jl=q0&pQq3C8+vuF`@AdbbAP-F3As4>hu|5}*ZSi<FeoN=I-2aT3>5zTW&LM$Y{Ui6y$$Bs6BX{?~p?(>;tb7&!|*HF(NN;HT(a->??Llra*yi3DEYlx?GzcOu?Y%vADTR~mqczkFzepK0>K1KFlJ=p}FA1<<`UOqEoE*8`(1u7)va6_BmdWN;ByHH%S`i?V<nvjZyTXIG*v7%e;H%wI47m9AjL#ir9S;R2ZMhJkVPHRbR{#G=8Or)Ea46gKIhgJCUn3Gf;1yX9(5(LZObRc-IrIiZ*M&Mtyk~jp#);3t>V5~GWR-c&qIPR(3Vz@6TMFmU5ja58XO~bvE#PeytxP-U%A_l>(N=9`wsww}1mmpAcI+|IE7<Jbe<yl!pPFAi!%8Wl$P<e+{KX!>wer_r-eB|Mt+x+i65X;OX_}f^b8r)(I^aeo-&0FHoN6KNkbc@(cGK>!o?j}dz3z}3gZ2;tH(a7{vksc^fwy*sD0m&sqh&Py5@&a?uPrl7T-<~tgXy2uOTw^SvjHoxP?rE2(cbC4VZ2;E#Tldx}F~xB#QM9%Bqzw8DfAoQ?S6oU!66u}z|Gr?SfSn)JLURCcTS*|vx>1mW--V1r1EY?PGx-<>46~U|!N>&zU`=p`Xqo4xwtjV7_S~A_-MQ4mX)u7DvlYig$V$sgHo&vbv?U~{r-EmDwGH61KnDgDJbQYsUIm`P(_8pIVg<^($$`H<831!~CrvNJ1(G|m`;ER#L&ffolM8VG%O~xA0rH=hC8f2B-0i#q=`JB>g1@Pc3|g6A_>|SfU#<SElS@kaekC1JxU*{iyn{^cR$=cF+qZ{1(=(%qH{9nQfN^qtq`=cg*+P1;;hs}-3X)>fcw*2W3EtlljNeMgZNPe$HwWnN8(%khm&+16Gs^>#(V-dOF3IW@EJ5-Q0o_M$0&P&!NRC|j2TT~~i7j?+?q|GDra#9;fsWFig)nTLC6<aq1(UTJ+;^d%NP*M{MXD%KH&{o)->)xSb;})E%Y4)tc7j3X*R>g^5)zNR6IMGG>^b8w_k}Iz?>MR=e(&W~#JW@wf9&1woK+Ermsb%VH%@$vM|dV3*9^bq$fIym!SJgq3WoWozX!-WtA%sllHm67`BEW$OPGN47kx|Ok#9*$G--XNNGQjWkz9%*;U&A05F~Xu^D4oXcA={%b;4L&N>-&7qiW%3QIcjBC8yQGx7@{@RttGX#gHT(yOG30HxjEB`uKQSDpW<(Pu0S6-Xko-lQnbCn&FQe5ZFt9u59REP%v!Rl1Bx@?zmvcO2(5l!%uB6@_)ZLXLwY2sF94k7z3c70u*zB%O1x7h#$@e0Anfuw{e0#y(9*h?QJZ{{;2fc@`-E!^8lJ;mzS~uw3Iwu{Vf$>=E{%7&+puFPa|}P<vv}z{ipbRS?=>pHEsi1CKHpE(FH391Y~ut)DpNY(e*amD!8$h!1%s@3Vc)qnQzU}m+Ays;$3H&lJi0WQ^&CGJ8x_8>A<mn;2i}*$p>hn6n({>V4nSm0I<NQ?hXkQHCw25riz{ptu^DMz<pp7*}-9PVp61MnG`+lNuF+&`7KIZ*Q7|SNaIl+T}+BwF)6I7i?4%85n<9CsMtR;DQ*s#6uBFw|Mpc%@>NRmRV429>1zwWw(x5Uze-8IN=d#-Nxn)+zDh~{BuYuf->wb&Dkb@er6k?C7h`!)e*h^-t3qERB{@E*M=8mtbR?}{n~I=ht$fD@34B(jsbVR19IO333+a?VQr);JI+dnqvWonUXD;wS3ecMhm?=fhr4{{L;P0G#<bkN-?C&U9cpw)jiAJwXdu6JEkwDk8@`$5;VmwxUJp1q9{3)b4UV<w}Fd{=d5RRN*(Rp1<CwVpg1dHU>t9wZ}!JE-b@?|EfSd`r^zcQDw^wyn<2hVglMJ8|3i!68E?u*@vlLnu@s5|J~C?PsO4XT30BXvkO8SYK;kw=%Kr!G{ZY9w(7^Il|E;oSK<c&Zn9@RW6rNe|TNl`s-Likgpkg^lKC0=XPKJyMW#2iklle)oiS<YkFQH(kXAX-Ho^p%i)gUDux%i##u|c<HB~5{@jwdFis)-{s3Oq|6iVx(iyCb45u1r26Ff5BQ5pk%wA@&uSN5{J^1P;k>JOe;_+}_=-RMz+9K`nHS4X&vhivXk7ZI<RFhebExom+_8_<A^i(l#$EB?>_PkmIZJzY)+RdPxxnjO@^yTA@Rh?;ojra|0#eKCu>|D*F%{!(uS4X%ov9H#t=|DeuHd+rC2PEZ)yFkB72phj+WH<vD^txoUxr)3xbZ6f&sc*aBjAj1O}wC5(;iB7P%JCD7h!QBJ~DEC9$EHZKVOCeP&RHxIRRYzVy;(H7oLv;+}DLtg}x+KGrU|0V1wUY5{;v>a1yr`U>k{^0G2w#*w6~N)ZM@c`q(g=-~FDbT3`{DF9z01nkJk=YSC8@Ahkryo}y|EQtPBkBNd4eL|uP$RBdZ;je@E*P^oDP<P+#FE7-UKvNh<bu&;~}m(hk7HxMXOzYD^)z-vSKp;+QIQ=c^8m_cn**-<=lhtQBb@&wd27N~7QsI8lTwI*C>&Z-4ki~sKqAhnBgkXlX5wzr{_)R8bwDggQShtzJo;b}F?Cjo`m+C^Y?xqA*tTbodbx20>=0#1a%2}8?EuzNuvU<RV&DE|~l+Vsj>{ZPEsSa_@T`}0<#K{VDc=dHTJTWzl6ttR8G3TR^Y&OoJww>k>3xhuxdaz<SRn1UwqNnDW=R*4vfa{{Y27oU^8`nzAO;_b``ep2y{=Onz>B<A%#|635#H%O!#5EB4Qg)({2i&POF9^9}irtJ^X@21%{5#kgjz`UzDZfGI#)^6RR#$<%ZWnI<5b#H7_3~jO-8gk#d<{$k4SNRgH^5ICUJYicl;%ack%c`r7aWx^2)#kw2-f%U>HmpXzuIDt-th{7zaPSp|G*;ULwbG^o2LSfcQNpBExT$)G&O$3Q?W&$UR8vUE@2cl@+~qH^x(|Q%NADS3MbPF^=QwVsJZ*0wHOEF;Vek+4R2EfViSXe?8*IT(10ym)yEgT?L%3V4RG2t&=V&8l^4^;W_#29g_5kbViOi^6m|=eT<6U>F>z?`ty7%c7*Y!-bb_KCr^@)Kh_8!_#B#$nfUjsL-9#F5{k}3@`LaM&L$s>qTz38>p34Gp$EL{7>88nVj(wjR?TA-x{BI<Kc5Pzon6LVAebWTP&6d7geDLd)1N_{^4Ohun}lTpsGNh0#HUO{&_iP}4WzS<I;jBphu^2MK>0#ZP}2V%fS!R5R><-SQj_argp4!TF!rI@_3$gKb};wQYz_ld^wls`tO4mhqk(L*~P!peXX*A?`X`C-W)=M&DYmWo7jly(&@<|A5}hizp95B1%S8YHoZDN`;8bd;o5IvF6Kt%99ARE`=3$PMlg#Bb|X#`pQG03!#MINzhc!(A!64vDpxfJWyl1MZTL-95#9Q6f;ZofLVC*38KG7U2N6-+}Q?Z@%ihjh4L>WyA3=QQf|;y(Kd%Cv`V7WAeQD%)8?)8qb4d&NKscneBH0a7H+UK%@0WU)6rxL}nIV0&=m~{j_fMM8USlljm#-s&Q0auT%t(+9OGf2wVKf_>!V|bmPI@7<qHA;7df#XoafeeyU(h`<4T-y@McFP2|f?KnH9?A=<^6A6D6lxZ)?I6Xqp&3%hl|F^M&8r6eU^xgx4&X>4x{J$Ym4!;uG)R{FSUDd+D_{s!k~E+L-LTr592doXhn8QbAFw`3cnpm#$PCV6|hKREAaOiN#`$QnEFTyRQV7&m*;5flC0F5J&HQGR}s<*mrhS;uNR^HG!DjW^VGgVtL_7xcwzOvR<6ZdQ&z3KqJv+(OIHmlr3_p>{{X|H<lKbM^16HmQQzwQ1!cdIhOxS1s}g&XaUYNwmD++;G~(B7mVBR}m8~nPFioEo=l5Ce%j)Iv9hjorsB_ScJ<##sWD)>0yN&NK^WXG#~t^xdnJE049S4ounnYGaCjKx>cUpR#2XZG-v2pUh-w@7kNsmZ8xlTG$91&Fk4*S=lL01C+rFvTG0>8Zc|SIp>V!@vXJR{!DRz$(9Y@{b!8SGjxTz=0`)1#b&(}>hp011I4<&)$WRfu_$^M4lNvq@a|P$_DOZaL<!_xYg-@k8zt2li@rYUwEfrC2?x{GTUD&;QgNOrCFk3zdd#rsMy|@zz3DnEgtq-+j>nL==e!oIl5Vwpl>V9uV5ADW_pDi5*|GPND{HO13Nt2tBshx1im4>BGn{jv52wP}JW15;q2AH+PYUDi&5<YQhS+SjpNr?xSG*YTX#uABNp{yZ(sim7t4wkx7AjR_6YD<a}!*{(I*2JE1AN5xPC!R>btyVdHq}Oo?2$pKeZ<Ra{avb0-$GT*tC`v(wSed{hKQmNC(y}tG3_H~L&nVZ?ayigYR7QlIkn=EqAWSAGmhxjKHBK|17x^-0riRk40R>LtGs>NnRFgUEFiX+a<4F}`6ATIT%E(V9$<XB=_|<28Gp0m7q<lc&*qNOULIy;#<jru;yl|lA1(Oz&nUCj9tI{?{yGkyQlCpQ~jJP0ZUqjf1yL6x9JcuJ9*fA!DRjebAgL|I8xUkaxpsw^_hg#}Tn7i;4bm^T-s!LZWA*3?>rg7rG#aYSfQ141akK;Bl2ZR}{;{jEyP1B0OTe(7DCp?7L2|#^@9hp^PCFi_NS!7~To6r67fk;nFQ>js*Cr`$CAGF7<SZo|!8{AvU(F_m1zpb`76eQ^r3Di3gsPp~V<KBOzQM5<P4UQ7m_h4g4vN#_BXO!>l4g>EEga@lsni)c?yWGSvpWCptNEOuC=)S*2=le3>04yePanJ5rSKEB@t!cgf09>8W|3H3ONP6T;{$6xnZ`l7Vn8RUrd>nrE`am}v1-hX`xj`B{c|z05uFt?e#LdFL5_IuFJP1@Q24>U>3Sesi2u+75<yGcA)N}?#H6<PkWLkMCZR45-s5@X57oo+=;E2!;uBRmj9c*-CdTianf3zD2V{TUs!q)R8_z7C_HQSK;tKi3t4-UQFtTrnZDTtF%jj*vuY;snW&PlLv)Rn)EdFZ6q!z}ojlrm;N#E3VQSClSC$P&wW`dPrnfGU(!z8g(uov~D-CdzrS!5o!lKN_vz<!3L}>ec0IzVd$F#AA%=Lt8vgjYaBgUhq6;YsN4MY|rE~W<V#ZDYm5~W4{tyL1B!+pY$xM5wFsS-X4pmZJ9PyfIW&ZEl~Fgq$ylhSGIA$?$#au$9^6xI+dCReq;C#UtG%_9T~iP>{*a>^J<q>nkZ~XO?i+h-QG&L6OD4~{bN(zae_z<(jFHXlX-j-mt@`w(dPUdh4NkMea%GSbH@QKG6$I5%uIpN$G{l!xGEc!%bpV1^i9C{sH?(~bmTz}NaE|1)>36LHFlf^F66GFR~ueznfT6;*Ou~ZOUF9uT~Ty%Q<=1@jkEa3gmp7kTb$qds)Z@qffK<jWjt3S`3RZfA0KhyfBKLMKS)er#)bc)aN&o-g-;h0wcmjY-;oO+$%T(6T=?(gCN~7vM2G*T(BadZ4xbLhvwsk(I!Rb?#)bDtF$46;+q=@%x{%_VLW)l_{p`V#7Z*wK$w=`AJD7O!)X#3tQ{(A$Nb8SLKl_LsKd>N~iiGx@8oxrDOw{<MP~$BGv$T~e4$PhvUVI<Wzl;|Tbq6W7aRs6tqFgjtUQu?*2=b8PJ}0N0W(0X8;y6VuAOwGoBOjk($D`$a;l-!w%L`iCH!suDKIX-zV_rO_+BFrmo&QZkjd$*)Gk6Y6H>H+EVbRNIoP2R3Am^Mu-ZP|lmNaXnzuuV?KdWj+6ge)F;x+G+8sA+a#Zv(SRbdV|f69x$N)M+k6~aI{zFP5YH>u)WrIHt?s^+4o@x~ctzAs1^B@v@anxjNsZE884spZ(e1q1xV!tRy&c)rMNdFtcct|t<`f1;ila1ME^)6ii`8sRdnF-XtSAPyh9%)j`jC$+3!L^2~SQPXGw>`0~H$w3hFAV_y*Ot53-y;JS;k}cURpGS>$*m+UzSg6R2SVy;ykk++aMI*s&CUFRZfwIv8Z_$>P8ylKN#z3dw)+<}N70PL#W{v`<j+;}0+Ys2~?zym1j6Q?<L1PS@1;ulq&P^@J4K!}6hROA=GHIRI;^do+lgxb2FG{^TUulqbFe7CspGq>GseBkTtYxt)Ra~k7X(Qjgc#7Ge%5&Wm<CHw;-e-zwSviPLN^k~7kw?N?r>a{u<%2IyF=l23A<pR9r-e8pvsa$3R{lVHi`xVH)^#XAvnRlvtdSL}38H8@*W6q)*CeOKU2F7RV_TG&4woPG^z|8P!a_UfkyW<YL}Q*oLQn*6b8buFS${Q%!i}PwdHRSIlqNapbWG}Kz8Ic^Qkb9P=Yvx8n*(#Z?RDeh7Am9HVq)QG$A#FR_p}RFd)jrTQBxqYPkY+cOxv1CmyMWlUEV(_RX0KgiD@9<Xo+I?#!t||RT(Y`+P3VE{%~XFRe3yb%+;Qt0Eg1!l2n>n(~dR+u`B$zc8<a|bhdMSv939G-!e<FL6F1~AG_|dk6m{?To3N1Gcc_~b`Y(hrJyQSb{AFbEM0&i3bV;|5k7llEb++tU_To%%_sA;YhJvZyg<=;hQo`81Lfr)yw&^L*IkXnldki*wS+i4q%XX*oXhw?*tMY+-{7teT@S2Ki{}m35*dH_YoO)C6tw&oG(HqrGtabehmI0awcm@55?#TOPBE-7dDy^LM&2l4Z2v6kyx2+H32P{!I%QX$G?j3ldm$PA=s^s-Lj;8wHlILa@FR-5a&YY8u%Oy$1=&T2-y_*gW!F2_?U=C6V`xE@*J0FsrB-}uO*%e*@_|W=2b$5wLE@{D{VJY74Y4b%=j{pXiNz}jI*U-dW2nn~F#<*eq<$9>pSBxr|HEW2(DLh;xOvRQfMQ-?E*^oZOx+?~trr~1JQ<`}_{Fx!&nD&T`80ovF&oOus4MU2Sw6rHr!kK@s}<uLs-)ze@@og}eFHOXtc);qf<`798;GHp@-(zAn+G=e?$+=#5Y6o%7RqggxgD7WJc3QXVoZ+{-$-H-r`%G0+zSuO!5q<G+z&JkIsZJ?gF(YLy5a_9kvvp}mMzq>_Sn$>P@lBhf+LKjfv<EE)@FE>$_X^$4e<=`SPX5;(=sWb;W0!vm}N8?;~J;k#sDJ`@Bpk6ZR8RdVe(LG8wg8!0C@79$)|&&TtT6zqKZNIw>?w($~WXT?jPJY4sH~vPO-qU&7J!W+nJxa_21-f#K-Fm`~x;DQ0;b5YTw>s-p)(F{x))YgxxJ_8n;C<dXI^iOJe?6_oLeo4LOpdGuhR#`Xnx{5Cy8_@bf?WP~Gj&+rHVLZF+vJPRA?TSznmfmF@jkwx=AvKgqK8oKe!pUDhl+qy5ou?q%(F{idoRJgy0<=AwG3lJG4`c^_30zB*e;IC0|qUZ`4t!coqfiU|!X%kDr}w>zmJTqCU8U92JSN-xOkCZes|BCp%d3J4A4b;a}XXj(6GC0|<^L0N5#TID=XiV4-Aq{yMjZk$<i5_VFG2|)-&ACGl*1;}6}0VgbO(s{LAD<%+qCc$0S6Nppr5#y$vmlUv53zC9x&lDDFvzMamE@G%jd3Tr>8N3-$75!bA+g?#;@E3{<x!cq{W~gL#{>Vk8mI^OLEzVUN7z}*kg2O*${+(TjKh3(-7jzfuWWb3aQJLWQjg~#4gC5Yk<Gpza23ksi4zgE7tJhi8y>-bK#tyTxto;%bNRZEiKDIM-P%2%%ojg0uO06w+o=hqMXRRNSCN8}~kq_W*o~LaYj$me@cft)|p=||llVj+eaf*<~-4ULIF2-!x9p}>muRwIZ$7GO3-HHdM4es(W=^^>Ryv}U_Q2k+qq<M1r0eJ}dBEB;*5D*igVL*+^-4oo?dk(gmsk4ErGaa{p)w@A3ko)uvd_@VlNp4uv4TzT9Lx*N>c@q|GrQlztI55HL5lNvEkeKI;;Flz%b*R01=cyfQI0@BMaxcG0)F7xV@r>;Q2f0dzd6mC`d2ZGD;z*8wj?ry!HxBOtc_T+m0i(f}_VR?vQ`XI@+Irt6L?bs9X4QPPk+xO<Y*NDbHebR6yU)V4y}>fmU#or##AP3p_V-Lsc1Zhc3hmFo2kmeD4&m60_P2b}t}<P+t7I>0=3bSI!W1ONtGz0>^C&D#)v>$hy(%#W9mZd{r~=*i`1;cSK=p6C;pd2|<7$(>z`y`NkvW3!)@>hn>u!+(Smqg_7k1GxZwmUv!#(i?ced+QwPwxvd0V3zh5SOJ$|^Q)V#&4)zVgT7y}9EG?%dz-WLPkux}0C%S&kqdVY^2QEtsCn8~D`<b8haB19a<Y{mG87x)*8;2h8&t7(U$Rd*aFSE;+75sL+nm`+X&s_}gve^@@0y|Idp7P&@2aUtllign>Gl7skStKU>w3Tll-w&b4K`xx!JVJ1A@!Y^rUEIXmwtquM#3yRkasC{tg*Sreivf3ndWVF~)@ZERt5@79I2aMw(ZGHG;_aqyO2Bci26RefY8XS2YfF3{X7B`qS>qq~m3$jv}~npqrE@HPbi=lj|AUw`7Dch9<Zx`gfff|J6^Tvp{>88!@4^8@xEfca`L#o$XB$XN8CueDoJ8Ws1*Ei>;;hO=1&*DhHv55ycT3Eqg<t!&ucJk=CbKFxz4^j8&5y(~nqj^M!xol9!+kq+JJN*i`1slaKHUlb0Q9Ee(BCgCfpO$u21R>4W!7ewsf9cZ-0aB%7R1<ml<F}ci8vS`!eC$`uNAmks=HE#6l3GBn+m#-z0l>3m@b`#9*cUy%uCXv;w`L_W%HYg6zHn?v*8NP(9*KqL8XSX8i9}tDkTeO6D)wMTh+7<Sxd@7c4GJmA4-p$iiZoC`60<RKt_-)Ex#GViN);zwq0CzX^lFAMCu*USUPIT4DQ^~SgRDR!Ad87?ru@!&iDD4+FuAO_*<_CFw*u_13$KpbO>A~HQ0<gNtr^7|bbFv3;M%MEfp0q`GUvo*%v1sm9Lk#W4e+8SNyuIgsy_J!=(QV`maeL#xByv5)kh@M85JPD92s_#2zd(5D{Q`aN8!8FrkNLH<@*<3qx5fuvMFc(YcWI3Gl|OXrgm`!N!U{83iL^7S^$K&0d+DRpMDIBh4ncUuSxY)p?G1W$ZuFKZif@5E%V{M4;84AZW;vf<>B<IZ`QIHm-?nnT#X1cWxh4-IZZEcx_?9Txe1t(96;A}9kt1iLFJcVh|I#hr^|sr=fW1M%!I$~~jy~89EzcCRdqs#8Yonq7A`^}K4#Z%ndL|91Ux!{b_Xdt=6aWv`#Ovj$qo>lQV@}2^RUXji2GMqC{hTN;(-u|^MI9@N7AhD^$h}}_MIrbiCcuc^p~VD?61Z00OP;Iew8G-Am?WM)xV9y)ndpYg7HXX`1je>z!G(R0n=aES`4%-~v!nstjhGU`-B}N*TS3r0sL3^~mwOv^@B@n_6oVZII}wvnf(n2w6%7fG2O@I?61aRhLZiA0vtIO2!X%$B3OOHCay&3}VY(tI#2~RlO+@->l@<%WHe5kb!1*7mIi&+yDuvSVX2$1OL}c)2z?>gXWDXGGu@FFbu`UcJj8B*Ds#X%EwN35qwlZ=6i#=F5qCwra1$XaR*{H<^Mh9`SSocQNFCsj|??-WPRSrlN&E{wKNeo?vj^2-Mn7P%OND+{BVu*@<p;bqp&-d_v)H~z*j%3r3IZCR5ljUWgJb)h$RZUu`<waVTF*5{Pv(E5lab(20LJkmVZEb|J(FRl{qk7h58qSZY7J@>VQOmmNV^IeQ_Um<_mDFUF7U{SmMv2IYZ?WT8WHD4{uPBtJ)5)N$*Ummk3Uw$a8G0Tzl%8IB)7dOsktFYGhw1h1pSu(fonMEy7@1g0m*?W4{A;Tc548+FN?v%#Yw~UihF0f-q0#g)j`7f>0)pPS$<0#(>`hm3YG1Srh9V>jEaVPePGMstBqQ>T{JU%Tbg!8aa>cm3Nuw$plEjO~^fVlyi=8r>H34AJdP$R~-GP-$@Tv$EUHdy`G~1~jp|mx#(#SDkZVifi>EUxD>t8CSEdFZsJ`j*AB?M0sG6D~O`i)o1i0vsiPiK2CxG^z5^JK+r7;(#C)))LsYGvAfMS3;06P9qee*4u==!$-}{kj9@1KB=9MmaDH*42d_SgdOIk~&z-{VuPhZow(J^<H`SCwE|sB0ggh<`16%b_^_o69k@nx@g(P#=fPwC%bA|v2GU3(-(Qf9T&j}wrsxcHRrcg0bBS2iBNGq39&(WA8h^=_G`WfjL$g*c-C$5ZG7k$uMw_Hj0kZUL=t1tMX}EBISU{o%;X%wAJjkzm2^Jx@9y(tF^Jqo_UF2~<9RlG-4G$s)|7lVRMS8NUo&DF&@W6xq{9+?qgeJ9D3MrrZ2qrQzXfn)KcQJ&p7Z+MitOt%w1*dEbx&&R{FNf+CbW;gI=9;#R@j%b^ltlndUrOhH0a|uEq<u~M-H~R8k0aC74O~<(+1nz-Mve1A^(uKy9;JgmQ84l_*sp5&)9}R=!v-ejlZErBsU+SMpRoZRQ6q?R|1K`1fFR6xsg{w{4Pl<ZLq^q`EhfH4D17!{0)m|V0GU*2_|$c?jSt@ur^62nMp74#35dkJH;<ruuJ@gG&Nc3ixiZCHqk2gEU+Hheg5fu8r2VTOJnIVQw7#%-Roff+$EaL`wV7{WDsL70A-?3(j3Oz>0l%mnd#)r0@Tf_G}_07t4Fdw9Lby6NUonB$?mjJBMzbeR9Knz?>rDB-d`~eZlNcK;IiQkl3B?kHR5nljo7Yi>=6<iIvX(uM$G-0h#8Iai2I7}P*j_qkDE>FfZIdI9rsg%rh?V^a~uQCaZtD6L<#iaMIGWaO7PCr4NL{hFUj_Qh8B22KX65aICzt)DN@IiI+dx66(NSmfY?#%arr!p$CKA*d+t$vU{aoOlNf=EGGRHOE-a<ETTMM$iHBzPSaQJmn{!G-kaVgHdZ#gJBu3?7(n~~$$^G%v#w!V<lK)Uk`tf8a1DBZ6x=3{hNWcZ#_s=pYMUBf>qu!Q@?Mp9;lzJv?n<9-+TE>6ux@_*!|MPp*9+6|bV$BOcbiO;Uj{DZ9cy*2I+vnCiENM@W>hh+Nj5;oOPciDK`(!&`4#ybZVa;PQenN?2ZAjtzEiiliFkAMhE3v5O%O1O!Tvx`_7MrUsYA{NtPv+MphJ`$VX&sG2>iO}MMlKy!zM+{`zV3>ZuOt6+w)i3CgNTpWn&$VtTpJb1;Cu|9W8KB5qs#Q*sX}UZtfRY_baa^pJkp1i5)b{U7w@5?E8BBPHY^F8?{d#t0s@trxn8=uue#)##y80~b=7r#+k*>?YG?l9l5(n%KYat2gO+jw(5c%1us?iJ{TJ1hx<(76^>Q?wkWGpWi;(>wuc`=j+tzfGkd-5-Etv(CyIUc8M$&w#<;AuP@K~!0u7Wz8C^RH=SY-!O?)pK}am<?slb6X&vy+mT_8kPQ=H{<~AQ5g8lA^LW%Of{1A-il*1!zqQGMe6_WR6;!k^@VR=wks1F(;{pM4t}6m84XO*~5x-b`bq@O7)_Z^9Sm>$Z1B)wk!KkQ=uqKN{`cDX4_otrTpm>0@Pk-G9Je?g1qwY%;^T}tmRDDXzu7Is4U3yVK$t6%*L54<CzarBDbE7iI&X&`r3W-AHSD?9|*O;=uQHD3wFaE0N7{L`+DrUp}&ElN9n!=>sM^N9K-hoU+hQqKGbh~51P121H@0(gx_)B&XhD1Z|sKxs3AZTBJ>nQhkZsGyW^32B87=$-U^o4<VY86PAJ8)kjV4oS9-#h6ANO<SFsvaQ9~+K>|eOi+O@I;uzQM?`CEySV(~#VWxmLbo~CZoyAy4jJzo)=CV1~80w`;>pw&$sR-bWZ>S0jG#+e<ExS3QQ!Hc1&_|>df#?EHZ5)XMq4V9G6xk5Z1Ve7vkw!S}ytsh>9tzW(zTfd|}Pd=X?ql|crs{eUc-P&HxAoag^0;x}PNIfvthN}N@KH*x066xgNlD{ZIJvZE!5nErzzdMhx=dyrZjKS+AQhgC&Pd&=ke9>~h`_2V;J%9%U)*mYKNXYuUEYIqUED!bfs!5sWy9G?&&cO6}Q~Summ$K%9)E6~jU}z6f_2{52Io{>?2zQ5qr>8z$Y&p}lMVzOt%?M9mdK|ntk?3LQHpkP)Q#^gGs#y{0VG8N2R!<^KKXG4n1%{pugS^FaBz=2Et_Ka(6HNbvVo&(Q0Q$d>!~TAT#}HKnt+O#m#umEvz+rDZao>rf?Op|!m`vGQqM!s7<p+C+R1wpO;Aw(kcs*s=NSzm?JjijbRQC;>taJM{RuhL-gkcp_D#$wsXm?`XX&As!vvzPsg2++Yuy7_DZZ>?F+*{!p5KuDP)nIh5Bmf@3AA|{K%L1dXDDh9BKXD>D%n%KGZf+&WwD-h~5T4QVw0kDeI3b#W8tMnug^(1hrFAafz+~Y8N@fjF96Z}NYJK101OS2XgupjiCJlqpmFhB6u9RKn1_~F5ZpHJIhN#R{A&swXx+?Mc2nMC_YUKZ`n%mNxg@kpOd=cUv$nNp)xe};7Hu1eGTvCiUgr9EDRzc?~5m%Q$hco*>COkR6=fTF5jdW)@%?;S__3?}*L?`c_W2L@P3c{HiRK)UdDh08e7db~A2!`k{)q#Mp5BsLCEJb-&1k`vA)iPWs|KI~N<Nk(aPyJkd1>`ghmBj3a8Qy%y{<s*EAh1JmeSJwMaB^Jw=zPC_;su+<eHFeWfQil-bqzR_CiZZfFV5hb(@qidg6fTVr^wlA0l;Mrd%KoU)VfmCHu-9-t1irZHF9I`RN28KfhjDH-X*t*eA<;g;xO(Jd%r}95|PHPHyFznRSlOvnHRNnhnvt9N=tqvUr|2bddN#2_T=!DXoWNLs^~0~t=sZ0x#_Pj6Afa6J1XJ)wdbdaPc6LU+Ui7msd{dX(Ej}CG|_X~OPf)9slF)hCURFks|HRQ@1yPJB=6NKK~%p`+s(OkV?|C8%NL6iVYf-utyDNiZ8xZq&V}79JH$i=nTcIV4Uw~T4Rjr;p~V%{mCoOo-e~oCsVj^B?ApHn1!j;dmPqUSNH;B>6Q@1OiTdN!P^Ov(Dz&TmB8VTtax)3ljztUHu2Q$a3Z)4M>j-<OucTFbX8CKYi(0iqS@@c{YbX<|-v&`wsd@A`snouqGbf5%MWq(%xX2-dv~kp=MJnjV&9u7i4C0!vrDKw^_Q2rmo?Lo9nXpjz$F73d=N7m_;Y>)TdIhjdNB1V|{-RslJ4rw1uR*GV!E5q)FYE@wYBs%Dr9+aV^=rfFg6NU&$_?evL8aW7o;XF@{C0&IYD>O!l!G(%fGL5DCfrE~e+lT#x)PpPM(0MTZI}KBi_k1hA#Ev}p^@rF>+h!aUsEEaUIa)P<Uzfu9wY@n=4Pm`?+oI`<1cuZYD#<Xl5>##75APwwrhd*5{K0!1Km;E|I#&UKKxUE4p4_(Ucet<!?kE3GPYU+PP7K06UnK(wB|-#0dbFJUII_y7i)LR-_LLD*0QO`>zjK$_Pb5hH95AzDwZ4aYd%&x?epW#f6>yP0FRm8&94K$@89ItmjsaJ?bjx64e+D=1|9uP!=C_ixDsJ3i7K2Q|9>xAmS3?7?~hdgAbo~Ca#lTU30G)76r(g*1u<O>S8xTc@KWH>`;ba+J};^Ck5qro4c{kEATULpXNWH-5Aom@dlHf=_=Jd>hwR3UWf_7iq|yhXUGFUE&*YC0I+2N3(=-jKZj3sxK*^*ZOb-|LVIU>KpexMe<jC-C2ZzCqOJ&Op&z9fSw?-$>uhz^3us)h9VI+**Aybjfs!B~Ieh`&V{o4crR+>(=qEQl0i~+pJsTAw>y9E{lUrHLhKrm<rM#G%Ei1A#4TcTqwHWdc|t~wEw5&r8BTn3o=_|(t(__Vb03CxP{MOai2vd`4!VHsedTxsFuSq*^gU2F0*F@?|~n~#iPZ!|2hTIl10L@Ws!$W|u8QXENZ1+~$FZpN6oVZnf3Z|gBpV>kk4Uxh32vW8OLofMhMoVI=C3RcDYDFiQ$JhIx6QKnNd2#MvHYfmwgX1WzZsiv;#3vND;0O2QdpL`$3+Q4WTHY+>`vggbj9ZOO&d!o~Sfe64T|K_R$6wOpcplt~rH+67-_J{%2k;sLgLbM`JN9andD3ZKw0aZkM?U^z}LMaBTS-9@|m^ni*$`???12x^;C=k!A*ot~^rCT8})+l>N)9qwYYsVu{_++}Y-bvw|_20pFe6ctOGDX+X{f~!AOvPbI>ap0h;@WWG%TZSzI=cT+{4kUm#S-%!^=jcNh^@IF4MxlePPHT~SgeRy#YcD3t7=mWOwfPPN{LCwgwNM35=A+p$;~gn*g9X@hoUcRC<<OgDg@`pH7=IW7+ev}Z^>6jSN_%N*D;;ex{VK1iN=~%K&2iiDGZNIRkujP?%`>M5+iRyls<=?N{2{$v{>zwb<aP$@x@06PluK$a{0*liZ<YRQb6zivWAvVYy4OYs=*nlB&y>^x1vKp{=iMFZg^w+fl*9Z0#e`ssn7aVtnMP|6FQU1Q^(qG8*Ha~y%_xp&YRVPz7_p`p`)>X1!M<2%INgdTI8S?^HG=EjUVgiI_@{*w#G_S4dj?NU}Y{CZm^~fxw?V(-&O<-tsfaQZ_f(O%@r}<9<YW<<2TA1=yK$@gh3YqyBhF<<D_jEzh2_MVtP4?|4wKuE$S+PDpD5%!H#g>`dyMU-8>dlX2y$NdXUw%aFFp0BSKP<0(LN#qB&0QUK<g%&it$_vPgvV(4oR&)+@5Tb;;O(-joy_TEdr}duK&}N4B2OWYg0yBl5L{+UGS<`{PWpD@B1ZSzH2235`=LuDwn%_y`3XXP!YM-EFugD#~0ON(a|-JY9Y8#iI<RnH)JqqJE}rKyC6*o^D?J`lLqnO&}C2_*)_v2G);%3JEhr1b3X*DvsAY$R8Zuy)}2ambz6UQ6<JT@vhj|`MAZ<(S{NkT&R9lvK&MOSB`~#XVFl;S1XH*s<5}^FP5-U=7)-ppaHelCKW=IgMP7SVU2@kC<0b-C(fxQ1x((Gr!h$5i3+e=303*(&NQry^22)qA<a-y2C;NrWV-L>M~+mCqlMqz_8^=I*fRUk;7^BQ%($O4uQqmdSY7?v8K@(a1jOFPvC_|mPRhUd?@!qq<q^KLB*KG~0qP29gr<O~+Nyg?oz}#ZUZ}Q9PGqdxg#qoic1C+_C~2`}s5aznNP|!q({xR}1nNoz(h*WrEdU|%GJkPXB?&52Dy%zz%KIE%TNMkHg&>kSoNpqbMH|*?5SUWOvSGLuoYg)NCJ@!2_{_=0k8{Mp1Csm%J%+&<_I2U4G0EYzK?xN^babxCn;khj4#_tSGJ?)o<h866z9XL!7$oMm`XB}^YNArj%ai6C6+yWZT{sA}=X+hp$vZic7TPdQZK=x9L#+$O3b`kK0g#bVRuUo5iNsabs*BO9bJP5&3A({VU$zrUM)9{^(<_!<p$qy?8Wn_oS)S;aF}Jcf<#p9Bpn`lt!7j2sK5KfV{TGkfW4pYKrUbRRe~iHLJ;eP396HBc;aA_L-XAqH@}ecMUl<+E*_;oA7Gd;%;lCfLxMvCgL9m5X<N_SkRq~<UIt13=1+U#^pF|<QUYN?hOmp<+m8JPZtlmV_NQ6ewjv{~VX0+lACZ3=@vXj6GEe*eYZ_eq_COex}@L*L9S_)nDm2n`P^a1f{2nYfYn1h|caspM4EuXr10I-%HT&@Y&Yl{cFSP)EH+-e(;+q$j(dhT#)s1Qa4O}^+!Vps5|&V(Khj5VZ%nVaptXkq?Tq{?c(D}fe6TtyWpL9<a#G+bSGlO4B1ibt!fV3Jcfu;wRQTSfW${j@BvnW0)uCyTvRyu&irX_F;g1nF7cD$P}D4HQ^WIp}MBU_WNq>;us9MB>ggFeskl-$*2TUj)P@&$=5|c%imT)L|<*+7gV6j=?pnOo_`xN!D4?&k1wE>WtPb1TTAO{5cAmpiKs)9~`tfRU9cUv`iuGk06tegiH<vGO58hhfF^D_;>*_2@A}3gG`D?DMexkAmvB|xA(D<#wUT3EFy8TIzUZ6K5c23KY*3-M1nX_r#(I+L7X&`j{wQ$EHn}ufQM0exJHW|<09h)P-Js89MV6Ff}H#bADD4_dk*~gDDa~{fIUh^c$mQ+7Y2JI=CO61KLI>a)afbp;QBdF!uS$+<Dp9MaExuFEbv)8WBAx$M)&xKu8GbT^XM!UHM3BnunwK{NK7sVrch1^a6)F0on1+uWqBRBW%%xAnkhZ{b?j|v+eE)v<~yWZt!bvTG}-G~z<L@g%XgO2mTHmDKixKnbQoWFl|?s{d2@-YiSwbXo@-(xZ#S6Ha&X-jxR-*acI*1u-}RVc{T%Mo(<qOkTu?&ku>;BXXZYt|P_R~^<c)FP!VcVd@Elm&-L%Ngu)hY?EQSS)ZF_>;^AeU%CEl={8EmqRlXh~x5-K;}K;1z(=)6X>o!<_cBh2HMQ#3Y_+uM-F!ZdJGkY@Hp6=yp5_|*Gv2xr1Ro7-h{pWCstttH8RrL}YnN(HNdUzfUi3zEqO(_&z|Vq&V7RUIv9DPL+Vmk8mpK-9I;l0o;UlSRmF@o8s0;GlE=eJ^G@3An$dPgWe6PUmP&R9wBxbRx~Ey@+31=(gM$!72B=VM|eG2vZTrwnJ_`w1h1o`OPX%p7HVyd<U!5rnb%sDKH!sGBVwLr5$jddB4tI%pVR_{)yezqzkc}zODXXZWpAT*VQWTyKhkJa|9)?wysXJoV=w_5^~;@HedjkYQ$oQ2C%t9qb!E1U&KL<8Qdx_$ijHw-VkOdo1*+wOl=T&>@jVwsC1GKo_B6<8REqy_KcE-<E=uRv)xsVQ$pB7=34G10j?eSN8fmmua>;v-42^Kt21e&;$4ymqPx?UV}sT4w%C^BbGx}SuI*}vQ|f5<f-U6=(@D(*OtZPfs3eh{1Elm<jx!ujASG(t&`_uhNE_6}%iAk%1Y<1{qFS?GO%%I@gOU?TWObNz!cJ;3+>x7EfMceVQk*P5<ykT>i>rVV3uc$P5=v={@``)lw^|(&&{#uOwld-FY=aie(VjBFu~72(-2rO(&e05RkRdmSYAy$0dsbE?3fx5~QF`HAS_o5-`o=7Ug9Lb#U$Iabz+l_F#c~2WId!de_!V<E*s&S%uP=z3hrws@WPeMUz6B%Sv_f}|l?IFdR<zI+h?F&uo3bUL4j~>(FTPuwUfZcJTXW8r4K-OnrT{M)QB%P9EO79a7ye02*?#3^ee-VWn6;?r8`J0uJBh_|7R()R<6JnL2${2Eri@`7Cqi{Ph!@qkN16h~1#Ed^+l{H!)3y`wWJ^8Bh54>p7jx`lagC_6=Xx*@(Ytm<<}BaXfv~!o5|a6b=g!!;WmMdXDWDFeHcZbw>{T~-J<r5DDrV(_=N4JOFa`@+k`!7G?Tc=v2s`Yn#uU(O<8<Q%bY_+QKRVUrjGW){a+l-Cp5(d}O=sIe0>MHXitwS*fE#D3YxhE|^6=Xnpj%2fmMkdtj{(R46t;N!Qk?W<9dAANVl8*h98um-u$21soNgRI*M(amHD2jRIl7gQoE5w|f{lunPKZ@jUu(?6jWOY<+T)d)#w6^3SD@^sv}$dCQcAeNTz2sa&(oK3Zpo(F2G$~#;KlGVaai)|k_xa3A5_nmdSY~j@k+J<$1e`f7%ZI3sjVe@Tqg%$F9M=`5RwuZEE;>Py>-LcGuYtAcBJu~l)cGeR@{k2j+F|FH&0MF0Pp|OyRH|2c{s`@GIhq5Sdq`{QDAmQ>q5^JA*mP-k|)-J_S`~HhNbX^G!Zi`!vXF#Wg+M-^lQp05HGC)(QDY}#k@b7|82x_&>|0Q`A;wLX9ypI+SW!Cu|1E_Y5?;us%#S3K(7bmDL;D)?l4vdWcqtB3_6j3g1^u6#Q-2;V=|Wrg!2E4Sw!5QfP}g%Y8S*^U)G&NA*`-W5wV|IQzrdOmoP-5p`hw3!wUgK=>$E5ijSZ}8^ZzJyFz~_D5hOk$}zDZQRu@F0F>x$oG%h5{F*tV)|*)}C!?Nt*1neNEuuY1#kQTY)WrBeR0T0v%e$8s8VY+;PM8ezR*?(iATKzFIK1dDtkUF7A9wei=xFpOW6qqHOhtt?;!PgkjY2HObVjz*NTF0u4F|BI{6^E@Ox!qIk@pfvE7r^&{+riff6cImAuhaWIN%wcx?p2IxKdQon2%+^JJSwWF^&ZIfWv;_7%_9$gQZw=*rW1SNfx0Amj9G!@*Rg+nhpNdiRffKFCi>gfG_D&_o)gA!_OUMJAeMrd`+dOx%t|z5X9?}?W`|kJG-m1oh>t9x!)%e#Oov5HG$=kt~|(d-d<t2R(t;?4cFR}Z0G)pY$pxZo^e}Sl!RyhWWqC*F+cZNJEVi-Mtoi9;Bl7!Y|qod-C1L`i&;>C4$q}P6GbV&pL*I)4NR%gOpV&g`7s9mG4s1o)~C9d4vm%$^_0?`Jk-u4ML8v0XPt&k+`H#R-6uCn+qie0$H^o%V5q@#O)j;7T_>gSnlO~2YhnU0PNL;>9n<1_F!gisu66J+8Bnytl57c>4+!Z!)`MvDO|1%bSryXLs{+5c;707+!oV$FHR-H$WqG(6mxpMAU%otO%L7*=;yt59gpK86(<)MI{Ti;_4W~&hB)!2k)M%61n&%?qsBr9TX~FAzzT2Oi&-ja0dF6K(6y2AZi2z)7H<b@7E0Bs|T7lwh1=@_l@_~TsIH}Da{B(6h)S|0IDDS%Q0cL<t?G^gBf4t>t_@K+xw@#L;Yy3fl4*Fi+jU;SH-qj*hDXnKMLd&8B6^zLu^zovG35G(Hdtt!p)t#<ho>jeK5jwBo^-rx~OtyQj2eXwd5o>a|l0iIO7NL}N5}f>CN&6elE@?XWMVC-601(2haNlcp>xxk*Wa9lA+X7qUoEEu&&j9Y1k6d4_`MJ@v)9o-<G6xRr2<#8eNu79wppA}PJ-6m@n>Aco_89t<l@Bi4PkV(5pqC7h^9dKizxYnMMP|Ig^`_}k!wpT%4Nb=lO>>&uMtw)NGC2Zl(`+{bz#wg3YNfllhDE`sNc5a7V7;3qwApJcn_VBSTO9uNeCf*fs=2hG;kwmm6T=k?J5quKBSt?;Re6eMerO@AoYUfg6-d0Y25J}XF33}!6Gn%<OCFsIFC`P~X%=};v%u@}f`I}|!ydOVdBA+f*Tp<_ILTw&j9ZyOh+o^#KqAwJmePW9w#vP$Ccf|EEeXw^f1jEOcGj^}ODa@~WjI>*2ZDt4@?5pVJ1OTYf<oxsmLdr}W-i7>W?|E)JTj%M5i&1vz;)qtTjZ0!I3NW*w5)+}UMF#`lFd%;V$j#=oM7hnOe73<0I%g4<ZEUdcMbQw#C;&?0YIm0kx;bDm;4}eTMzw<j@kNJsaMuze=J&eMY08A?W*-|*^Z$CkPDE^Y(F)pyZ*1<JsH9*d+zCp93vQjtq>z)?ifyzAv6>NB^<!etCJzle9O)RzYMyYcB+KM=fd8heRA$-Pm&?3gyp{rj^trXhG5l}J`}-vsCB7LmO-vD>=${WNq*H#wJsz>$c}ECk^^ll6GEskVz9Qvp=r#4QbB2)KGsiXLOwZ|a`?x<RsBwtR@mp{VS|{WLA@HTcuNfO^uSd^XoWks^&GDBF-=zD0xfa7b$g^8eSM3Y3>v0nM%fW+;^_tg(3VPi<|$*v5TI3wz>Q?R_RjpR8I_<O(%vvdTUk{HP^CLPU|kaStLV8y@oG<d%)J}F+uq~+cO!g{NWiz!<Ju5gU#n;gEJ@AN#;w_wtrS^~c@teH;BxXpbhnd&wUHd+uNd)cL`ER%Yk1UwtTRND4}cqPcD%vS*cO`|pu~>&&$!8ZRrG+qC6d07M}g`aX!XU46Ci-3FWwQ_h{_G+f3^9|Q*a>qM7CX?qJe-Lw%q%)wxP?7-D5}03<?k4)2zf>b{{a!xS@U&+ic;*^>A%#lA`M%K&;cGpNG~L0lypX1N`Fn)4LskDWsOA4Pr+lZsr4RXp&NibqcTWX5%*c09#!<KW`F&ux{kuyOL3O`XAnX-irk&z|DO~!kzF75qcMOYlMY5o?G`?;u&n+6KDq&)Ti(Pw(imSLTtsurB74hFkAr(m`#TJCldh2umEp_i<XQsZp098wbTYkEkRQpIkz4)gkuCiuz0TJreHxJ#}O1@uL_fD|M@3YL<1<sk}DRW04=K0h?~}i2Eb~p{dzcCE;?jtjhriW)eR*<$1QvKOtM~!-*~Te7|0*eA2<{-&jd3QLFF?snCyfdKTcF>5SpYOJ4;hgFqHp9udK&j*_z(Ktvl$OfnV&z?<Ei^cT{0lyqEK1OoQRkB%}`oy0Me8TGj!79;uPZ@?s6bjdj@5-kMM=H0@T(W7agZk5FnvZv~;!nQErl-A4%w8m=AO#sDS-2zf1`__!8a&car9>%aM&zo=P%BL09!$Rl11d9x-!FAl)voB11ZdsLu8$H&K%zykVf>dVYv<abvL7Kv=xA8r<ub;{?Re@>-z{Ae|98S<XvSQ2P4>$YEi?8QIdum94}s(DQRR5iSH?H6;LC6`A+Eurb1*T#f8X+BdJPUIHd9y<Ru?758r97A6$dONI3dCpjo)Rav0kw^%KL`gTQDUzi=c+&2A>JxhdquQ2KTns7=wXF<dDVuFRJOFwEvrH+)SerC{W77C&@=^1wbJBxC1-oTr;lz$@u>Q%dN2D+KD}a?tKd+!60{T%OEQ!!d1_64n#(DMLOeUn?sx+pIlu7FVlRBSeZBQDn7I|{qPD1r7xOZa#IOL&nPHg;Iy(W%xA2uKenp%K)K3Puk@qcfs0{@`4r`YS|!O`olPv7n7YkPj|r>`yi+QP3b{QC5@h2Q0=|1eMeJA6I8<lXd9PWyeIexeZKwWEH*woM=Ix6*Itw)HRmZhZ3Ti@y8Ys?+-Sd+I;X({%My&wRa`J)NJGo{sOj7d$<9?5=u@N&qn@SO2Y4AU=LEmIw7q4(QMSH5<)PtR89eVXyZ^Z6LVuIA{KuqD3{=e>5Qyhz~Lk$?PRxY50W4m5rINDXK%(Mu;Yp=;d1r-mRtKR}{Y#2gEF)m@Hw&GmNI3{4A|?Scv5<KuTG}TcL5BJ=W6@%8Q{qb>;5}=8{a5JN_H&!lwh8Zz=PoOcFWi9UuJS;nVT!R*li|{rO)!`gK1)$=P*{KUz)(?JuP(`;2*g;!39r_p_h&Po0L$i-NOi9L=6MMiSp@J0}8Ixg&aT@Yj{EoAr#n65P~`2Uipino+k^C$DP>#Q<WuqAQz`KWagjn{}bUENm>7Fg^&?`765o*Uz5X`I{(Wv1`-g-pz0B{PrE+&1dhCVKB#r6)aSGjEy9Dixv>esH`K>$LHeTz`vDU&h(1?^<@Vni5Fqm%47Y-p&EO|x$+>KyfPeoi%m3p>d!x&zCJ$imtT3}Tdq32(kf1meffY)k<K)QzTytf^QudD`m7EgRQ}@eQBW%%8*f2*h2`S;S5D4+YylS!uFf6a_vvGoADsR})qnQXjV;+)XBZz(pBX!kJ9ywqJ5RT4{@711p1(WCFOp|};cgx^#S_hPedC-yu;t^V4Xdd!QQkjlQa5XA=MP%usFmWVW#wnK+Q<Ig<?lfv|M$U(HMsNxmM?RAd}pd!3dAr-c>95pTa{}lCIDNZ4LDMRXm6E=nn_+!X_S#_s?2U3bp$E1*Sh_t`l|8}Y9O9_+Y@R;Y=EjkExp_F7q|DM%<+rsJYjbxNv@eq_F=IoNE5+PJ$Qe!2htso+g>WusEW!qvWeBr4N9WkjWVQWqnjTuYvLh19BoMjMs??bP~7Fc`%;P>Faj~5bO0&-V)Y&r229x-XVANi^8=w*`Ha>_=qqW35N_9)=;fRh{uKJEc5!)xvLpHm#PAOXy&~Emo`qiJ=BH;yKAW~63{a$P&VjD-SrMtcTFyaN;;qsyZ$JYM!8~Tg0-zcY)F@wwyK*PED}UpP9*X<;xT}BiT~WV=TXQP_vr;k@fn&5@4~R7hD1Jiv4wF-~`Upfq)<;+rH>_Pe!t%-~I=Hp`zeW;bzVi_35v_#eE)qh8709=G)!~4ym3Ay8At=J)S&x0g9<eaNfC6YIF>}3^%#Q!ki2P-{TCNeH+5k)HO`scH<sSaBRkCl{s83b0X%IlhFC4+TbCvAe)oN+KPG#&s(H&H>sj;)7b|qTKJz2&k#L|;k8BOoxu#!z#Zckd#RLQ0!Q$D!r&@JH+&5@cVtSS#H*-O*;m)}B5a0rUo^+_>Xs=F5T^0ZfwEbT`8gK%bwEU3KeqHqo>W@9#PDA&myUZC200IoL{CHe>*gVjuG5;8lcHVKX?M};hYFRD#yqi|}Q^vNpR@i$&8+^-ex*V@(V)7K9C+JRqN__e(KTHbywZ@-qeU(4IC<?Yw<_G@|jC#t+Xe&DFWeN^6dR^cw??O4j&j^}MghWK(cG0(<|ol&|m-i*#Y>)b*4X;vebB=Px?geKF(Qr-OjYdg2yNMRTZ6DJ(fp#y{3)oPz>@B0Lm`u<nNzfEvB&#HTa7(hefn1lG@|4(>QbSL9E<W6KX;a;f-TtGw$+w>RkwXkekzp0RT8$d)hWSlZP`?@{mpAXo!p2+ZWhWc^$uWU~by1B_sXP&JleE5PIHQE%*RH>2TzlXGUd3H1%@fpmvBwK4k43$5J@rhwmVOt_CS6nSk3K@@I_N6S=%-%!8FHLR`Xw4_8Gy${*(=XBWdW^14FK{m7)=5_fBMW<BEiuCtQV7FVfIVT<J&c{uTB5mb0Rl;B8ExQI%Bby{TQ^7CT1RIMgWUxpZlLcpWhC2fQEp*-=M5RvjfBMBW|^nN`YA-cUZDeM?WV`pv}HP&^lo#3SlcB%kE?CA5M`WIqB>Jp+Tzw>UT!kly==7fdV6-o$pMFBdSUsGxO%6x&Rj&=?4avT2DCn6*krEXb<oJo&);l?_IGJjD1K%i??0~C6;#%)0D?lkht%k;@CSAU9m-Q@3=4&w$Q(`h+HdhE7_^MmniEtoCt!tl2pQa2_ykz3<VtNWf4`4EG5N|f9UWu#T2m9Ti(E%sJ<Gn)?0euI9u6BNmi(}wfo-^5{6nJTT(VvRYiqyZcKSj^*|W@Q^YyfwLmr+ZH-`!m8o8T8yW!@r3fN@mFd3OZ(&3fektKL7i&Ozfk{VKq2XEEV*rdU6@Ceo^DR`_ZU2{kfJT`p@H9W=}7h8903Kl&U>EnRoJCTwA;ryk33nDr-c8zTy`l12P9LB?Xu5|8+TSb3=Afn-iv+cH%ZCsz-v94QS?;{#>qD6$p@I1!%icVhj*ebHFz~U=5rg`z)=>R{?%Dds6C8*xG3$FS6|M_IX01t9eIG%$6z4SRA59XtDNbbxdQyK-EM&OZzObTG!p+ue`nP`zr5$-f&GO-m8izgtB)H_5JwE0Tx&(i1tGXu9uqi<JUSG5'
_V92_P_INDEX = [(0, 26488), (26488, 14995), (41483, 22870), (64353, 36903), (101256, 36571), (137827, 12613), (150440, 26202), (176642, 10064), (186706, 19694), (206400, 15668), (222068, 26533), (248601, 28135), (276736, 21736), (298472, 41143), (339615, 19704), (359319, 22831), (382150, 20863), (403013, 13917), (416930, 18830), (435760, 18716), (454476, 18185), (472661, 25404), (498065, 32250), (530315, 30091), (560406, 32549), (592955, 19662), (612617, 17789), (630406, 25612), (656018, 14767), (670785, 30710), (701495, 30012), (731507, 16428), (747935, 19267), (767202, 18602), (785804, 16214), (802018, 13910), (815928, 16565), (832493, 23277), (855770, 13844), (869614, 26160), (895774, 21425), (917199, 23786), (940985, 15989), (956974, 15693), (972667, 29078), (1001745, 21194), (1022939, 22767), (1045706, 27862), (1073568, 14471), (1088039, 18163), (1106202, 19157), (1125359, 34996), (1160355, 26356), (1186711, 23580), (1210291, 18368), (1228659, 12427), (1241086, 32380), (1273466, 14485), (1287951, 22259), (1310210, 14230), (1324440, 24271), (1348711, 21836), (1370547, 13513), (1384060, 25681)]
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
