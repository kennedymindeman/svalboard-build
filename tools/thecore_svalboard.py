#!/usr/bin/env python3
"""Compute a Svalboard mapping for TheCore, one left hand, and draw it.

Usage: python3 tools/thecore_svalboard.py [--markdown] [--coop-blend W]

`--coop-blend W` (issue #27, default off) mixes co-op load into the ranking:
each key's load becomes (1-W) x its 1v1 per-minute rate + W x its co-op rate,
and the bigram rates blend the same way.  The co-op rate is the mean over all
18 commanders, equally weighted, of that commander's per-minute rate from
`thecore/coop-summary.json` (rates averaged, raw counts never pooled: corpus
sizes differ 26 to 158 player-games).  Constraints, finger weights, slot order
and the optimizer are untouched; only the load and pair inputs change.

`--coop-normalize` (default off) scales the co-op aggregate before mixing so
the two corpora contribute equal total mass at weight 0.5: co-op per-minute
rates are about ten times smaller than 1v1 rates, so the raw blend gives
co-op far less than half the influence.  The per-key co-op loads are scaled
by (sum of 1v1 key loads / sum of co-op key loads) and the co-op pair rates
by the analogous ratio over pair totals.

The premise (wiki/thecore-method-on-a-svalboard.md section 4c, the user's
decision): the LEFT hand is on the Svalboard and the RIGHT hand is on an
ordinary mouse, so mouse clicks cost no keys and the only room beyond the 20
left finger keys is a held layer under the thumb Nail.  That is 40 slots.

Nothing here is hand-picked.  The mapping is computed from three inputs:

1. The two shipped hotkey files (`thecore/*.SC2Hotkeys`), parsed as
   `tools/thecore_keys.py` does.  The unit of assignment is one TheCore
   physical key with every modifier variant it carries, exactly as TheCore
   keeps them together.
2. Replay load from `thecore/sequences-summary.json` (see
   `wiki/sc2-command-sequences.md`): events per minute per TheCore key, summed
   over Terran, Zerg and Protoss, and the top bigrams per race.
3. The Svalboard rules in section 4a (speed zones) and 4c (finger roles).

Placement rule, applied in this order:

* Slot difficulty = (zone - 1) + (1 if the slot needs the Nail layer held)
  + a per-finger weight (`FINGER_WEIGHT`, an assumption, see the constant),
  i.e. a held layer costs about one zone step and a pinky key costs half of
  one.  Sorting the 40 slots by difficulty, base before layer, gives roughly
  base zone 1, base zone 2, layer zone 1, base zone 3, layer zone 2, layer
  zone 3, with index and middle ahead of ring and pinky inside each band.
  Inside a zone, centre before south and inward before north (section 4a's
  ordering), pinky north forced last as "the worst key on the board"
  (S:283944), then index, middle, ring, pinky.
* Role is a hard constraint (section 4c): `Command n` keys only on index and
  pinky, camera / idle-worker keys only on middle and ring.
  Classes are derived per file from that file's own bindings (see `classify`),
  so 6.0's merged keys land where 6.0 puts them.
* The control-group floor: the ten keys carrying `ControlGroupRecall0..9` each
  get a base-plane middle or ring slot.  Middle and ring have exactly ten base
  slots, so the ten control groups own them outright: no control group sits
  anywhere else and no other key sits there, camera keys and command cards
  included.  Higher-load groups take the easier of the ten.  This class wins
  over the `Command n` rule where 6.0 stacks a group on a command-card key.
* Greedy: TheCore keys in descending replay load (ties: more bindings first,
  then key name) each take the best free slot their role allows.
* Then a hill climb: swap the two placed keys whose exchange lowers the cost
  most, as long as each one's role still allows its new finger, until no swap
  helps. Cost is

      cost = sum over bigrams of rate * [same finger, different key]
                                      * (1.0 same plane, 0.5 across the layer)
           + sum over keys of load * slot difficulty

  Both terms are events per minute, so no weighting constant is needed.
  Same-key repeats are not a cost; the summary counts those separately.

Some same-finger work is forced, not a failure of the search: the control
group floor puts all ten groups on middle and ring, so five hot control groups
share two fingers.  The climb spends the cheap escape it does have, the half-price
cross-plane transition, on the heaviest pairs.

Everything the tool decides is printed: the load table, the slot order, the
placement, the swap count, the final cost, the unplaced list and the markdown
table for section 4d.  `EXPECTED_UNPLACED` guards each file against a silent
change.
"""
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from thecore_keymap import (  # noqa: E402
    COMMANDERS, FACTIONS, MELEE, factions_for, parse_entries,
)
from sc2_sequences import build_map, load_hotkeys  # noqa: E402

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = [
    ("TheCore 5.0 Right Plus", "thecore/TheCore_5.0_Right_Plus.SC2Hotkeys"),
    ("TheCore 6.0 Right", "thecore/TheCore6g_right_US_qwerty.SC2Hotkeys"),
]
SUMMARY = "thecore/sequences-summary.json"
COOP = "thecore/coop-summary.json"
OUT = "thecore/svalboard-keymap.html"

FINGERS = ["index", "middle", "ring", "pinky"]
POSITIONS = ["centre", "south", "inward", "north", "outward"]
PLANES = ["base", "layer"]

# ASSUMPTION, not replay evidence.  The wiki's speed zones (section 4a) rank
# positions within one finger; nothing there ranks the fingers against each
# other.  These weights are added to a slot's difficulty so that high-frequency
# keys prefer index and middle over ring and pinky: a pinky centre slot costs
# 0.5 where an index centre slot costs 0.0.  Change them here if better
# evidence turns up.
FINGER_WEIGHT = {"index": 0.0, "middle": 0.0, "ring": 0.2, "pinky": 0.5}

# The control-group floor: the fingers and plane reserved for the ten keys
# carrying ControlGroupRecall0..9, and theirs alone.
CG_COMMAND = "ControlGroupRecall"
CG_FINGERS = ("middle", "ring")
CG_PLANE = "base"

# Section 4c's finger roles, as the fingers each role class may use.
ROLE_FINGERS = {
    "cg": CG_FINGERS,
    "command": ("index", "pinky"),
    "group": ("middle", "ring"),
    "free": tuple(FINGERS),
}
ROLE_NAMES = {
    "cg": "control group (middle/ring, base plane)",
    "command": "Command n (index/pinky)",
    "group": "camera, idle worker (middle/ring)",
    "free": "unconstrained",
}
# A key is a group key if it carries one of these slots; a key with 5 or more
# ordinary command-card bindings is a Command n key whatever else it carries
# (6.0 stacks ControlGroupRecall1 on J's 196 command bindings).
GROUP_PREFIXES = ("ControlGroup", "CameraView", "CameraSave")
GROUP_EXACT = {"IdleWorker", "TownCamera"}
COMMAND_MIN = 5
BANISHED = "Alt+Control+Shift"
MODIFIER_KEYS = {"Control", "Shift", "Alt"}
MOUSE_KEYS = {"LeftMouseButton", "RightMouseButton",
              "ForwardMouseButton", "BackMouseButton"}

# Named global commands worth showing in a key's label, in display order.
NOTABLE = [
    "IdleWorker", "TownCamera", "Attack", "Move", "MovePatrol",
    "MoveHoldPosition", "HoldPosition", "Stop", "StopGenerateCreep", "Rally",
    "RallySCV", "RallyEgg", "Land", "Lift", "Cancel", "SelectBuilder",
    "Larva", "ArmySelect", "SubgroupNext", "SubgroupPrev", "BurrowUp",
    "BurrowDown", "CameraTurnLeft", "CameraTurnRight", "CameraFollow",
    "ChatDefault", "ChatAllies", "MenuGame", "Spray",
]

KEY_LABELS = {
    "Minus": "-", "Equals": "=", "BracketOpen": "[", "BracketClose": "]",
    "BackSlash": "\\", "SemiColon": ";", "Apostrophe": "'", "Comma": ",",
    "Period": ".", "Slash": "/", "Grave": "`",
    "LeftMouseButton": "Left mouse", "RightMouseButton": "Right mouse",
    "ForwardMouseButton": "Forward mouse", "BackMouseButton": "Back mouse",
}
# TheCore key name -> the QMK/Vial keycode the firmware must emit for it
# (section 4e: the hotkey file stays TheCore's, only the firmware changes).
KEYCODES = {
    "Minus": "KC_MINS", "Equals": "KC_EQL", "BracketOpen": "KC_LBRC",
    "BracketClose": "KC_RBRC", "BackSlash": "KC_BSLS", "SemiColon": "KC_SCLN",
    "Apostrophe": "KC_QUOT", "Comma": "KC_COMM", "Period": "KC_DOT",
    "Slash": "KC_SLSH", "Grave": "KC_GRV", "Backspace": "KC_BSPC",
    "Enter": "KC_ENT", "Escape": "KC_ESC", "Tab": "KC_TAB", "Space": "KC_SPC",
    "CapsLock": "KC_CAPS",
}

# Modifier combo as parse_entries reports it -> filter label.
COMBOS = [
    ("plain", "plain"),
    ("Control", "Ctrl (Pad)"),
    ("Shift", "Shift (Down)"),
    ("Alt", "Alt (Knuckle)"),
    ("Control+Shift", "Ctrl+Shift (Pad+Down)"),
    ("Alt+Control", "Ctrl+Alt (Pad+Knuckle)"),
    ("Alt+Shift", "Shift+Alt (Down+Knuckle)"),
    (BANISHED, "Ctrl+Shift+Alt (Pad+Down+Knuckle, banished)"),
]

THUMB = [
    ("pad", "Ctrl"), ("nail", "Nail: hold for the layer"), ("down", "Shift"),
    ("knuckle", "Alt"), ("up", "gaming-layer lock"),
]

# Keys that must come out unplaced, as a guard on the computation.
EXPECTED_UNPLACED = {
    "TheCore 5.0 Right Plus": {
        "3", "4", "6", "7", "Alt", "BackMouseButton", "CapsLock", "Control",
        "F8", "ForwardMouseButton", "LeftMouseButton", "RightMouseButton", "V",
    },
    "TheCore 6.0 Right": {
        "3", "4", "6", "Alt", "BackMouseButton", "CapsLock", "Escape", "F10",
        "F3", "F8", "ForwardMouseButton", "Grave", "LeftMouseButton",
        "RightMouseButton", "T", "Tab", "V",
    },
}


def label(key):
    return KEY_LABELS.get(key, key)


def keycode(key):
    if key in KEYCODES:
        return KEYCODES[key]
    if len(key) == 1 and (key.isalpha() or key.isdigit()):
        return "KC_" + key.upper()
    if key.startswith("F") and key[1:].isdigit():
        return "KC_" + key.upper()
    return "?"


def is_group_command(cmd):
    return cmd.startswith(GROUP_PREFIXES) or cmd in GROUP_EXACT


def zone_of(finger, pos):
    """Speed zone of a Svalboard position (section 4a): 1 easiest, 3 hardest."""
    if pos in ("centre", "south"):
        return 1
    if pos == "outward":
        return 3
    if pos == "north" and finger == "pinky":
        return 3
    return 2


def build_slots():
    """The 40 slots, easiest first, with zone, plane and difficulty."""
    slots = []
    for plane in PLANES:
        for finger in FINGERS:
            for pos in POSITIONS:
                zone = zone_of(finger, pos)
                # Inside a zone the wiki's order is centre, south, inward,
                # north, outward; pinky north is named the worst key on the
                # board (S:283944), so it sorts after every outward key.
                rank = POSITIONS.index(pos)
                if finger == "pinky" and pos == "north":
                    rank = len(POSITIONS)
                slots.append({
                    "plane": plane, "finger": finger, "pos": pos, "zone": zone,
                    "difficulty": ((zone - 1) + PLANES.index(plane)
                                   + FINGER_WEIGHT[finger]),
                    "sort": (zone, rank, FINGERS.index(finger)),
                })
    slots.sort(key=lambda s: (s["difficulty"], PLANES.index(s["plane"]),
                              s["sort"]))
    for i, s in enumerate(slots):
        s["order"] = i
        s["id"] = "%s-%s-%s" % (s["plane"], s["finger"], s["pos"])
    return slots


def read_file(path):
    """{key: {'bindings': [(combo, cmd, raw)], 'class': .., 'label': ..}}."""
    keys = collections.OrderedDict()
    for cmd, key, combo, raw in parse_entries(path):
        keys.setdefault(key, []).append((combo, cmd, raw))
    out = collections.OrderedDict()
    for key, binds in keys.items():
        out[key] = {"bindings": binds, "class": classify(binds),
                    "label": key_label(binds), "n": len(binds)}
    return out


def classify(binds):
    """Role class of a key, from its own bindings (section 4c)."""
    if any(cmd.startswith(CG_COMMAND) for _, cmd, _ in binds):
        # The control-group floor outranks the Command n rule: 6.0 stacks
        # ControlGroupRecall1 on J's 196 command bindings, and the group wins.
        return "cg"
    ordinary = sum(1 for combo, cmd, _ in binds
                   if combo != BANISHED and not is_group_command(cmd))
    if ordinary >= COMMAND_MIN:
        return "command"
    if any(is_group_command(cmd) for _, cmd, _ in binds):
        return "group"
    return "free"


def key_label(binds):
    """A human label for a key, derived from that file's own bindings."""
    cmds = [cmd for _, cmd, _ in binds]
    groups, cams = set(), set()
    for cmd in cmds:
        if cmd.startswith("ControlGroup"):
            groups.add(cmd[-1])
        elif cmd.startswith(("CameraView", "CameraSave")):
            cams.add(cmd[-1])
    bits = []
    if groups:
        bits.append("CG " + "/".join(sorted(groups)))
    if cams:
        bits.append("Cam " + "/".join(sorted(cams)))
    for name in NOTABLE:
        if name in cmds:
            bits.append(words(name))
    card = sum(1 for combo, cmd, _ in binds
               if combo == "plain" and not is_group_command(cmd))
    if card >= COMMAND_MIN:
        bits.append("command card (%d)" % card)
    return ", ".join(bits[:3]) or "misc"


def words(name):
    out = []
    for i, ch in enumerate(name):
        if i and ch.isupper() and not name[i - 1].isupper():
            out.append(" ")
        out.append(ch)
    return "".join(out)


def replay_load(summary, path):
    """(load per key, bigram rate per key pair, notes) for one hotkey file.

    Per-key load is events per minute over all three races: every top-ability
    row in the summary mapped through this file's own bindings (the summary
    ships only the 5.0 projection, so 6.0 is recomputed the same way with
    sc2_sequences.load_hotkeys / build_map), plus every control-group set, add,
    steal, delete and recall on the key that file gives the group.  Right
    clicks are the mouse and are dropped.  Camera jumps are in the summary but
    replays never say which key moved the camera, so camera keys get no load.
    """
    races = summary["races"]
    minutes = sum(races[r]["minutes"] for r in races)
    index, _ = load_hotkeys(os.path.join(HERE, path))
    abilities = sorted({row[0] for r in races for row in races[r]["top_abilities"]})
    amap = build_map(abilities, index)
    cg = {}
    for cmd, key, _combo, _raw in parse_entries(os.path.join(HERE, path)):
        if cmd.startswith("ControlGroupRecall"):
            cg[cmd[len("ControlGroupRecall"):]] = key
    load = collections.Counter()
    for race in races:
        for name, count, _pm, _s, _cs in races[race]["top_abilities"]:
            if name == "RightClick":
                continue
            if name in amap:
                load[amap[name][0]] += count
        for row, (count, _pg) in races[race]["control_groups"].items():
            group = row.split("/")[1]
            if group in cg:
                load[cg[group]] += count

    def token_key(tok):
        if tok.startswith("CG") and tok[2:] in cg:
            return cg[tok[2:]]
        if tok == "RightClick":
            return None
        return amap[tok][0] if tok in amap else None

    pairs = collections.Counter()
    for race in races:
        for pair, count, _pg in races[race]["top_bigrams"]:
            a, b = pair.split(" > ")
            ka, kb = token_key(a), token_key(b)
            if ka and kb and ka != kb:
                pairs[(ka, kb)] += count
    return ({k: c / minutes for k, c in load.items()},
            {p: c / minutes for p, c in pairs.items()},
            {"minutes": minutes})


def coop_load(summary, path):
    """Equal-commander per-minute (load, pairs) for one hotkey file.

    Mirrors replay_load, except each commander's counts are divided by that
    commander's own minutes and the per-minute rates are averaged with equal
    weight across the 18 commanders.
    """
    cmdrs = summary["races"]
    index, _ = load_hotkeys(os.path.join(HERE, path))
    abilities = sorted({row[0] for c in cmdrs for row in cmdrs[c]["top_abilities"]})
    amap = build_map(abilities, index)
    cg = {}
    for cmd, key, _combo, _raw in parse_entries(os.path.join(HERE, path)):
        if cmd.startswith(CG_COMMAND):
            cg[cmd[len(CG_COMMAND):]] = key

    def token_key(tok):
        if tok.startswith("CG") and tok[2:] in cg:
            return cg[tok[2:]]
        if tok == "RightClick":
            return None
        return amap[tok][0] if tok in amap else None

    load = collections.Counter()
    pairs = collections.Counter()
    share = 1.0 / len(cmdrs)
    for c in cmdrs:
        minutes = cmdrs[c]["minutes"]
        for row in cmdrs[c]["top_abilities"]:
            name, count = row[0], row[1]
            if name != "RightClick" and name in amap:
                load[amap[name][0]] += share * count / minutes
        for row, vals in cmdrs[c]["control_groups"].items():
            group = row.split("/")[1]
            if group in cg:
                load[cg[group]] += share * vals[0] / minutes
        for pair, count, _pg in cmdrs[c]["top_bigrams"]:
            a, b = pair.split(" > ")
            ka, kb = token_key(a), token_key(b)
            if ka and kb and ka != kb:
                pairs[(ka, kb)] += share * count / minutes
    return dict(load), dict(pairs)


def normalized(load, pairs, cload, cpairs):
    """Scale the co-op dicts so their totals match the 1v1 totals."""
    kscale = sum(load.values()) / sum(cload.values())
    pscale = sum(pairs.values()) / sum(cpairs.values())
    return ({k: v * kscale for k, v in cload.items()},
            {k: v * pscale for k, v in cpairs.items()})


def mix(a, b, w):
    """(1 - w) * a + w * b over the sorted union of keys (order-stable sums)."""
    return {k: (1.0 - w) * a.get(k, 0.0) + w * b.get(k, 0.0)
            for k in sorted(set(a) | set(b))}


def cost(place, slots, load, pairs):
    """Events per minute of same-finger work plus load-weighted slot difficulty."""
    finger, plane = {}, {}
    for key, i in place.items():
        finger[key] = slots[i]["finger"]
        plane[key] = slots[i]["plane"]
    same = 0.0
    for (a, b), rate in pairs.items():
        if a in finger and b in finger and finger[a] == finger[b]:
            same += rate * (1.0 if plane[a] == plane[b] else 0.5)
    zones = sum(load.get(k, 0.0) * slots[i]["difficulty"]
                for k, i in place.items())
    return same, zones


def legal(cls, slot):
    """May a key of this role class sit in this slot?

    The ten base-plane middle and ring slots are the control-group floor: only
    the ten ControlGroupRecall keys may use them, and they may use nothing else.
    """
    reserved = (slot["plane"] == CG_PLANE and slot["finger"] in CG_FINGERS)
    if cls == "cg":
        return reserved
    return not reserved and slot["finger"] in ROLE_FINGERS[cls]


def assign(keys, load, pairs, slots, log):
    """Greedy by load, then a legal-swap hill climb. Returns the placement."""
    order = sorted(keys, key=lambda k: (-load.get(k, 0.0), -keys[k]["n"], k))
    place, taken = {}, set()
    unplaced = []
    for key in order:
        cls = keys[key]["class"]
        for slot in slots:
            if slot["order"] not in taken and legal(cls, slot):
                place[key] = slot["order"]
                taken.add(slot["order"])
                break
        else:
            unplaced.append(key)
    log.append("greedy placed %d keys, %d unplaced" % (len(place), len(unplaced)))
    same, zones = cost(place, slots, load, pairs)
    log.append("cost after greedy: %.2f same-finger + %.2f zone = %.2f"
               % (same, zones, same + zones))
    swaps = 0
    while True:
        base = sum(cost(place, slots, load, pairs))
        best, best_pair = base, None
        items = sorted(place)
        for i, a in enumerate(items):
            for b in items[i + 1:]:
                if (not legal(keys[a]["class"], slots[place[b]])
                        or not legal(keys[b]["class"], slots[place[a]])):
                    continue
                place[a], place[b] = place[b], place[a]
                trial = sum(cost(place, slots, load, pairs))
                place[a], place[b] = place[b], place[a]
                if trial < best - 1e-9:
                    best, best_pair = trial, (a, b)
        if best_pair is None:
            break
        a, b = best_pair
        place[a], place[b] = place[b], place[a]
        swaps += 1
    same, zones = cost(place, slots, load, pairs)
    log.append("hill climb: %d swaps accepted" % swaps)
    log.append("final cost: %.2f same-finger + %.2f zone = %.2f"
               % (same, zones, same + zones))
    return place, unplaced, order, swaps, (same, zones)


def exclude(keys):
    """Drop keys the left hand on a mouse-partnered board cannot or need not own.

    Reasons, all printed: the three modifier names are the thumb keys
    themselves (finding 6 - a modifier-only binding such as
    `CameraCenter=Control` is a chord, not a key of its own, so it is never
    drawn on Pad/Down/Knuckle); the four mouse buttons stay on the mouse; a key
    whose every binding is Ctrl+Shift+Alt is banished by TheCore and stays
    banished, reachable as Pad+Down+Knuckle on whatever key it shares.
    """
    reasons = {}
    for key in list(keys):
        if key in MODIFIER_KEYS:
            reasons[key] = "modifier itself: this is a thumb key (4b)"
        elif key in MOUSE_KEYS:
            reasons[key] = "stays on the mouse"
        elif all(combo == BANISHED for combo, _, _ in keys[key]["bindings"]):
            reasons[key] = "banished: every binding is Ctrl+Shift+Alt"
        else:
            continue
        del keys[key]
    return reasons


def bigram_check(summary, place, slots, amap):
    """Top 10 bigrams per race and whether the pair lands on different fingers."""
    rows = []
    for race in sorted(summary["races"]):
        for pair, count, per_game in summary["races"][race]["top_bigrams"][:10]:
            a, b = pair.split(" > ")
            ka, kb = amap(a), amap(b)
            if ka is None or kb is None:
                verdict = "off the board (mouse or unmapped)"
            elif ka == kb:
                verdict = "same key (repeat, not a cost)"
            else:
                fa = slots[place[ka]]["finger"] if ka in place else None
                fb = slots[place[kb]]["finger"] if kb in place else None
                if fa is None or fb is None:
                    verdict = "unplaced key"
                elif fa == fb:
                    verdict = "SAME FINGER (%s)" % fa
                else:
                    verdict = "different fingers (%s / %s)" % (fa, fb)
            rows.append((race, pair, count, per_game, ka or "none", kb or "none", verdict))
    return rows


def markdown_table(name, slots, place, keys, load):
    """The section 4d table for one file, as markdown."""
    at = {i: k for k, i in place.items()}
    out = ["| Svalboard key | Zone | TheCore key | Vial keycode | Carries | Load /min |",
           "| --- | --- | --- | --- | --- | --- |"]
    for plane in PLANES:
        out.append("| **%s** | | | | | |"
                   % ("Base" if plane == "base" else "Nail layer held"))
        for slot in sorted([s for s in slots if s["plane"] == plane],
                           key=lambda s: (FINGERS.index(s["finger"]),
                                          POSITIONS.index(s["pos"]))):
            key = at.get(slot["order"])
            out.append("| %s %s | %d | %s | `%s` | %s | %.1f |" % (
                slot["finger"], slot["pos"], slot["zone"],
                label(key) if key else "—",
                keycode(key) if key else "—",
                keys[key]["label"] if key else "—",
                load.get(key, 0.0) if key else 0.0))
    return "\n".join(out)


def build_entries(path):
    """[[ability, unit, faction indices, key, combo, raw], ...] for the page."""
    idx = {f: i for i, f in enumerate(FACTIONS)}
    entries = []
    for cmd, key, combo, raw in parse_entries(path):
        ability, unit = (cmd.split("/", 1) + [None])[:2] if "/" in cmd else (cmd, None)
        entries.append([ability, unit or "", [idx[f] for f in factions_for(unit)],
                        key, combo, raw])
    return entries


def main():
    argv = sys.argv[1:]
    markdown = "--markdown" in argv
    weight = float(argv[argv.index("--coop-blend") + 1]) if "--coop-blend" in argv else 0.0
    normalize = "--coop-normalize" in argv
    with open(os.path.join(HERE, SUMMARY), encoding="utf-8") as f:
        summary = json.load(f)
    coop = None
    if weight:
        with open(os.path.join(HERE, COOP), encoding="utf-8") as f:
            coop = json.load(f)
    slots = build_slots()
    print("Slot order (difficulty = (zone - 1) + finger weight"
          " + 1 if the Nail layer is held):")
    for slot in slots:
        print("  %2d  %-6s %-6s %-7s zone %d  difficulty %.1f"
              % (slot["order"], slot["plane"], slot["finger"], slot["pos"],
                 slot["zone"], slot["difficulty"]))

    data = {"factions": FACTIONS, "melee": MELEE, "commanders": COMMANDERS,
            "combos": COMBOS, "labels": KEY_LABELS, "thumb": THUMB,
            "slots": slots, "fingers": FINGERS, "positions": POSITIONS,
            "files": {}, "order": []}
    tables = []
    for name, rel in FILES:
        path = os.path.join(HERE, rel)
        keys = read_file(path)
        total = sum(k["n"] for k in keys.values())
        nkeys = len(keys)
        load, pairs, notes = replay_load(summary, rel)
        if weight:
            cload, cpairs = coop_load(coop, rel)
            if normalize:
                cload, cpairs = normalized(load, pairs, cload, cpairs)
            load = mix(load, cload, weight)
            pairs = mix(pairs, cpairs, weight)
            print("co-op blend %.2f%s: load = %.2f x 1v1 + %.2f x"
                  " equal-commander co-op mean"
                  % (weight, ", normalized to equal total mass" if normalize
                     else "", 1.0 - weight, weight))
        print("\n=== %s: %d bindings on %d keys, %.0f replay minutes"
              % (name, total, len(keys), notes["minutes"]))
        reasons = exclude(keys)
        counts = collections.Counter(k["class"] for k in keys.values())
        print("role classes: %s"
              % ", ".join("%s %d" % (c, counts[c])
                          for c in ("cg", "command", "group", "free")))
        print("replay load, events per minute, all three races:")
        ranked = sorted(keys, key=lambda k: (-load.get(k, 0.0), -keys[k]["n"], k))
        for key in ranked:
            print("  %-16s %8.2f  %-9s %3d bindings  %s"
                  % (label(key), load.get(key, 0.0), keys[key]["class"],
                     keys[key]["n"], keys[key]["label"]))
        log = []
        place, unfitted, order, swaps, (same, zones) = assign(
            keys, load, pairs, slots, log)
        print("placement order (load, then binding count, then name): %s"
              % ", ".join(label(k) for k in order))
        for line in log:
            print(line)
        for key in unfitted:
            reasons[key] = ("no free %s slot left" % ROLE_NAMES[keys[key]["class"]])
        print("unplaced (%d):" % len(reasons))
        for key in sorted(reasons):
            print("  %-16s load %.2f/min  %s" % (label(key), load.get(key, 0.0),
                                                 reasons[key]))
        assert len(set(place.values())) == len(place), (
            "two TheCore keys landed on one Svalboard slot")
        hot = [k for k, v in load.items() if v > 0 and k not in place]
        print("keys with replay load > 0 that are unplaced: %s"
              % (", ".join(sorted(hot)) if hot else "none"))
        if set(reasons) != EXPECTED_UNPLACED[name]:
            raise SystemExit(
                "unplaced keys for %s are %s, expected %s: the inputs or the "
                "rules changed, check the placement before updating the guard"
                % (name, sorted(reasons), sorted(EXPECTED_UNPLACED[name])))

        index, _ = load_hotkeys(path)
        races = summary["races"]
        abilities = sorted({row[0] for r in races
                            for row in races[r]["top_abilities"]})
        amap = build_map(abilities, index)
        cg = {c[len("ControlGroupRecall"):]: k
              for c, k, _co, _r in parse_entries(path)
              if c.startswith("ControlGroupRecall")}

        def token(tok, cg=cg, amap=amap):
            if tok.startswith("CG") and tok[2:] in cg:
                return cg[tok[2:]]
            key = amap[tok][0] if tok in amap else None
            return None if key in MOUSE_KEYS else key

        print("anti-repetition check, top 10 bigrams per race:")
        for race, pair, count, per_game, ka, kb, verdict in bigram_check(
                summary, place, slots, token):
            print("  %-8s %-28s %6d  %-6s %-6s %s"
                  % (race, pair, count, label(ka), label(kb), verdict))
        tables.append((name, markdown_table(name, slots, place, keys, load)))

        at = {i: k for k, i in place.items()}
        drawn = []
        for slot in slots:
            key = at.get(slot["order"])
            s = dict(slot)
            s["key"] = key
            s["klabel"] = label(key) if key else None
            s["role"] = keys[key]["label"] if key else "free"
            s["code"] = keycode(key) if key else None
            drawn.append(s)
        data["files"][name] = {
            "source": os.path.basename(rel),
            "entries": build_entries(path),
            "slots": drawn,
            "unplaced": [{"key": k, "label": label(k), "reason": reasons[k],
                          "load": round(load.get(k, 0.0), 2)}
                         for k in sorted(reasons)],
            "stats": {"bindings": total, "keys": nkeys, "swaps": swaps,
                      "same": round(same, 2), "zone": round(zones, 2),
                      "minutes": round(notes["minutes"], 1)},
        }
        data["order"].append(name)

    if markdown:
        for name, table in tables:
            print("\n### %s\n\n%s" % (name, table))
        return
    html = TEMPLATE.replace("__DATA__", json.dumps(data, separators=(",", ":")))
    if weight:
        marker = ('187 pro replays (<a href="../wiki/sc2-command-sequences.md">'
                  'wiki/sc2-command-sequences.md</a>), places')
        assert marker in html
        html = html.replace(marker, marker[:-7] + (
            ' blended %.0f/%.0f with per-minute rates averaged equally across '
            'the 18 co-op commanders of\n<a href="coop-summary.json">'
            'coop-summary.json</a>%s (<code>--coop-blend %g%s</code>), places'
            % (100 * (1 - weight), 100 * weight,
               ', the co-op side normalized to equal total load before the mix'
               if normalize else '',
               weight, ' --coop-normalize' if normalize else '')))
    out = os.path.join(HERE, OUT)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("\nwrote %s (%.0f KB)" % (OUT, os.path.getsize(out) / 1024.0))


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>TheCore on one Svalboard hand</title>
<style>
:root { --pinky:#e8d5f0; --ring:#d6e4f7; --middle:#d9f0d9; --index:#fbe6cf; --thumb:#f7d7d7;
        --z1:#dcf0da; --z2:#fbeacd; --z3:#f8d9d9; }
* { box-sizing: border-box; }
body { margin: 0; padding: 16px 20px 40px; font: 14px/1.4 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1a1a1a; }
h1 { font-size: 20px; margin: 0 0 4px; }
p.lede { margin: 0 0 14px; color: #555; max-width: 92ch; }
.bar { border: 1px solid #ddd; border-radius: 6px; padding: 10px 12px; margin-bottom: 14px; background: #fafafa; }
.row { display: flex; flex-wrap: wrap; align-items: center; gap: 6px; margin-bottom: 8px; }
.row:last-child { margin-bottom: 0; }
.row b { font-size: 11px; text-transform: uppercase; letter-spacing: .06em; color: #666; width: 84px; flex: none; }
button.t { font: inherit; padding: 3px 9px; border: 1px solid #ccc; background: #fff; border-radius: 4px; cursor: pointer; }
button.t:hover { border-color: #888; }
button.t.on { background: #1f6feb; border-color: #1f6feb; color: #fff; }
input[type=text] { font: inherit; padding: 3px 8px; border: 1px solid #ccc; border-radius: 4px; width: 260px; }
select { font: inherit; padding: 3px; }
.legend { display: flex; gap: 10px; flex-wrap: wrap; font-size: 12px; color: #555; margin: 0 0 10px 0; align-items: center; }
.legend span { padding: 2px 8px; border-radius: 3px; border: 1px solid #0002; }
.z1 { background: var(--z1); } .z2 { background: var(--z2); } .z3 { background: var(--z3); }
.planes { display: flex; gap: 46px; flex-wrap: wrap; align-items: flex-start; }
.plane { display: flex; flex-direction: column; gap: 10px; }
.plane > .ttl { font-size: 13px; text-transform: uppercase; letter-spacing: .06em; color: #666; }
.fingers { display: flex; gap: 10px; }
.thumbrow { display: flex; justify-content: flex-end; }
.cluster { display: flex; flex-direction: column; gap: 3px; }
.cluster > .cl { font-size: 11px; text-transform: uppercase; letter-spacing: .06em; text-align: center;
                 border-radius: 3px; padding: 1px 0; }
.cl-pinky { background: var(--pinky); } .cl-ring { background: var(--ring); }
.cl-middle { background: var(--middle); } .cl-index { background: var(--index); }
.cl-thumb { background: var(--thumb); }
.grid { display: grid; grid-template-columns: repeat(3, 152px); gap: 4px; }
.slot { min-height: 118px; }
.slot.blank { border: none; }
.key { height: 100%; border: 1px solid #bbb; border-radius: 5px; padding: 3px 5px; cursor: pointer; overflow: hidden; }
.key:hover { border-color: #1f6feb; }
.key.dim { opacity: .45; }
.key.none { cursor: default; opacity: .6; }
.key .kn { font-weight: 600; display: flex; justify-content: space-between; font-size: 12px; }
.key .kn .c { font-weight: 400; color: #444; font-size: 11px; }
.key .role { font-size: 11px; color: #234; }
.key .src { font-size: 10px; color: #888; margin-bottom: 2px; }
.key .e { font-size: 10.5px; color: #333; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.key .e u { color: #666; text-decoration: none; }
.key .more { font-size: 10.5px; color: #777; }
h2 { font-size: 13px; text-transform: uppercase; letter-spacing: .06em; color: #666; margin: 22px 0 6px; }
#unplaced { display: flex; gap: 4px; flex-wrap: wrap; }
#unplaced .slot { width: 152px; }
table.map { border-collapse: collapse; font-size: 12px; }
table.map th, table.map td { border: 1px solid #ddd; padding: 2px 8px; text-align: left; }
table.map th { background: #f4f4f4; font-weight: 600; }
table.map td.code { font-family: ui-monospace, Menlo, monospace; }
ul.notes { max-width: 92ch; color: #444; font-size: 13px; padding-left: 18px; }
#panel { position: fixed; top: 0; right: 0; width: 420px; height: 100%; background: #fff; border-left: 1px solid #ccc; box-shadow: -4px 0 14px #0001; padding: 14px 16px; overflow: auto; display: none; }
#panel.open { display: block; }
#panel h3 { margin: 0 0 2px; font-size: 17px; }
#panel .sub { color: #666; margin: 0 0 12px; font-size: 12px; }
#panel .grp { font-size: 12px; text-transform: uppercase; letter-spacing: .05em; color: #1f6feb; margin: 12px 0 4px; border-bottom: 1px solid #eee; }
#panel .ent { margin-bottom: 6px; }
#panel .ent .a { font-weight: 600; }
#panel .ent .u { color: #555; }
#panel .ent code { display: block; font-size: 11px; color: #777; }
#close { float: right; }
</style>
<body>
<h1>TheCore on one Svalboard hand</h1>
<p class="lede">The left hand is on the Svalboard, the right hand is on an ordinary mouse, so the whole of TheCore has
to fit on 20 left finger keys plus a layer held under the thumb Nail. This mapping is computed, not hand-picked:
<a href="../tools/thecore_svalboard.py">tools/thecore_svalboard.py</a> orders TheCore's keys by how often they fire in
187 pro replays (<a href="../wiki/sc2-command-sequences.md">wiki/sc2-command-sequences.md</a>), places each one on the
easiest free key well its finger role allows, then swaps pairs while that lowers same-finger work. Rules and citations
are in <a href="../wiki/thecore-method-on-a-svalboard.md">wiki/thecore-method-on-a-svalboard.md</a> sections 4a-4d.
The drawing is schematic: real key wells are cupped clusters, not flat squares. Click a key for its full binding list.</p>

<div class="bar">
  <div class="row"><b>File</b><select id="file"></select><span id="src" style="color:#777;font-size:12px"></span></div>
  <div class="row"><b>View</b><span id="views"></span></div>
  <div class="row"><b>Melee</b><span id="fac-melee"></span></div>
  <div class="row"><b>Co-op</b><span id="fac-coop"></span></div>
  <div class="row"><b>Other</b><span id="fac-other"></span></div>
  <div class="row"><b>Modifier</b><span id="mods"></span></div>
  <div class="row"><b>Search</b><input type="text" id="q" placeholder="ability or unit name"><span id="stat" style="color:#555"></span></div>
</div>
<div class="legend" id="legend"></div>
<div class="planes" id="planes"></div>
<h2>Left thumb cluster</h2>
<div class="planes" id="thumb"></div>
<h2 id="unplacedh">TheCore keys with no Svalboard slot</h2>
<div id="unplaced"></div>
<h2>Vial keycodes</h2>
<p class="lede">The hotkey file stays TheCore's own; only the firmware changes. Every slot below should emit the
keycode in the last column, the Nail-layer slots from layer 1 of the same well.</p>
<table class="map" id="maptable"></table>
<h2>Notes</h2>
<ul class="notes" id="notes"></ul>
<div id="panel"><button class="t" id="close">close</button><div id="pbody"></div></div>

<script>
var DATA = __DATA__;
var FAC = DATA.factions, GI = FAC.indexOf("Global"), UI = FAC.indexOf("Unclassified");
var ZONE_NAME = { 1: "zone 1 (easiest)", 2: "zone 2", 3: "zone 3 (hardest)" };
var PLANE_NAME = { base: "Base", layer: "Nail layer held" };
var VIEWS = [["both", "both"], ["base", "base only"], ["layer", "layer only"]];

var state = { file: DATA.order[0], faction: "Terran", mod: "any", q: "", view: "both" };

function words(s) {
  return s.replace(/_/g, " ").replace(/([a-z0-9])([A-Z])/g, "$1 $2")
          .replace(/([A-Z]+)([A-Z][a-z])/g, "$1 $2").trim();
}
function label(k) { return DATA.labels[k] || k; }
function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }

function visible(e) {
  var fi = FAC.indexOf(state.faction), f = e[2];
  if (state.faction === "Global") { if (f.indexOf(GI) < 0) return false; }
  else if (state.faction === "Unclassified") { if (f.indexOf(UI) < 0) return false; }
  else if (f.indexOf(fi) < 0 && f.indexOf(GI) < 0) return false;
  if (state.q) {
    var q = state.q.toLowerCase();
    if ((e[0] + " " + e[1] + " " + words(e[0]) + " " + words(e[1])).toLowerCase().indexOf(q) < 0) return false;
  }
  return true;
}
function modOk(e) { return state.mod === "any" || e[4] === state.mod; }

function byKey(useMod) {
  var m = {};
  DATA.files[state.file].entries.forEach(function (e) {
    if (!visible(e)) return;
    if (useMod && !modOk(e)) return;
    (m[e[3]] = m[e[3]] || []).push(e);
  });
  return m;
}

function sortEntries(list) {
  return list.slice().sort(function (a, b) { return a[0] < b[0] ? -1 : (a[0] > b[0] ? 1 : 0); });
}

function keyCell(slot, list, title) {
  var n = list ? list.length : 0, k = slot.key;
  if (!k) {
    return '<div class="slot"><div class="key none z' + slot.zone + '">' +
           '<div class="kn"><span>' + esc(title || slot.pos) + "</span></div>" +
           '<div class="role">free</div><div class="src">no TheCore key</div></div></div>';
  }
  var h = '<div class="slot"><div class="key z' + slot.zone + (n ? "" : " dim") + '" data-k="' + esc(k) +
          '" title="' + esc(label(k) + " · " + (slot.id || "") + " · " + ZONE_NAME[slot.zone]) + '">';
  h += '<div class="kn"><span>' + esc(title || slot.pos) + '</span><span class="c">' + n + "</span></div>";
  h += '<div class="role">' + esc(slot.role) + "</div>";
  h += '<div class="src">← ' + esc(label(k)) + (slot.code ? " / " + esc(slot.code) : "") + "</div>";
  var sorted = sortEntries(list || []);
  sorted.slice(0, 5).forEach(function (e) {
    h += '<div class="e" title="' + esc(e[5]) + '">' + esc(words(e[0])) +
         (e[1] ? ' <u>· ' + esc(words(e[1])) + "</u>" : "") + "</div>";
  });
  if (sorted.length > 5) h += '<div class="more">+' + (sorted.length - 5) + " more</div>";
  return h + "</div></div>";
}

// A left-hand cluster is drawn as a plus: north on top, outward-centre-inward,
// then south. The left hand's outward side is to the left of centre.
function clusterCells(by) {
  return [null, by.north, null, by.outward, by.centre, by.inward, null, by.south, null];
}

function renderPlanes(m) {
  var html = "";
  ["base", "layer"].forEach(function (plane) {
    if (state.view !== "both" && state.view !== plane) return;
    html += '<div class="plane"><div class="ttl">' + PLANE_NAME[plane] + " · left hand</div>";
    var fingers = "";
    DATA.fingers.slice().reverse().forEach(function (finger) {
      var by = {};
      DATA.files[state.file].slots.forEach(function (s) {
        if (s.plane === plane && s.finger === finger) by[s.pos] = s;
      });
      fingers += '<div class="cluster"><div class="cl cl-' + finger + '">' + finger + "</div><div class=\"grid\">";
      clusterCells(by).forEach(function (s) {
        fingers += s ? keyCell(s, s.key ? m[s.key] : null) : '<div class="slot blank"></div>';
      });
      fingers += "</div></div>";
    });
    html += '<div class="fingers">' + fingers + "</div></div>";
  });
  return html;
}

// The thumb keys are the modifiers themselves (section 4b), so they never
// carry bindings of their own: a binding written `CameraCenter=Control` is a
// chord on some other key, not a command on the Pad.
function renderThumb() {
  var by = {};
  DATA.thumb.forEach(function (t) { by[t[0]] = t[1]; });
  var order = [null, "up", null, "nail", "down", "pad", null, "knuckle", null];
  var h = '<div class="plane"><div class="thumbrow"><div class="cluster"><div class="cl cl-thumb">thumb</div>' +
          '<div class="grid">';
  order.forEach(function (p) {
    if (!p) { h += '<div class="slot blank"></div>'; return; }
    h += '<div class="slot"><div class="key none z1"><div class="kn"><span>' + esc(p) + "</span></div>" +
         '<div class="role">' + esc(by[p]) + "</div>" +
         '<div class="src">modifier, no bindings</div></div></div>';
  });
  return h + "</div></div></div></div>";
}

function render() {
  var m = byKey(true), f = DATA.files[state.file], shown = 0;
  Object.keys(m).forEach(function (k) { shown += m[k].length; });
  document.getElementById("stat").textContent =
    shown + " of " + f.entries.length + " bindings";
  document.getElementById("src").textContent =
    f.source + " · " + f.stats.bindings + " bindings on " + f.stats.keys +
    " keys · " + f.stats.swaps + " swaps · cost " +
    (f.stats.same + f.stats.zone).toFixed(2);
  document.getElementById("planes").innerHTML = renderPlanes(m);
  document.getElementById("thumb").innerHTML = renderThumb();
  var uh = "";
  f.unplaced.forEach(function (u) {
    uh += keyCell({ id: u.key, pos: u.label, role: u.reason, zone: 3, key: u.key },
                  m[u.key], u.label);
  });
  document.getElementById("unplaced").innerHTML = uh || "<p>None.</p>";
  Array.prototype.forEach.call(document.querySelectorAll(".key"), function (el) {
    var k = el.getAttribute("data-k");
    if (k) el.onclick = function () { openKey(k); };
  });
  var rows = "<tr><th>Plane</th><th>Finger</th><th>Position</th><th>Zone</th>" +
             "<th>TheCore key</th><th>Carries</th><th>Vial keycode</th></tr>";
  f.slots.forEach(function (s) {
    rows += "<tr><td>" + esc(PLANE_NAME[s.plane]) + "</td><td>" + esc(s.finger) + "</td><td>" +
            esc(s.pos) + "</td><td>" + s.zone + "</td><td>" +
            (s.key ? esc(label(s.key)) : "&mdash;") + "</td><td>" + esc(s.role) +
            '</td><td class="code">' + (s.code ? esc(s.code) : "&mdash;") + "</td></tr>";
  });
  document.getElementById("maptable").innerHTML = rows;
  Array.prototype.forEach.call(document.querySelectorAll("button.t[data-f]"), function (b) {
    b.className = "t" + (b.getAttribute("data-f") === state.faction ? " on" : "");
  });
  Array.prototype.forEach.call(document.querySelectorAll("button.t[data-m]"), function (b) {
    b.className = "t" + (b.getAttribute("data-m") === state.mod ? " on" : "");
  });
  Array.prototype.forEach.call(document.querySelectorAll("button.t[data-v]"), function (b) {
    b.className = "t" + (b.getAttribute("data-v") === state.view ? " on" : "");
  });
}

function where(k) {
  var s = null;
  DATA.files[state.file].slots.forEach(function (x) { if (x.key === k) s = x; });
  if (s) return PLANE_NAME[s.plane] + " · " + s.finger + " " + s.pos + " · " + ZONE_NAME[s.zone];
  var r = "not on the board";
  DATA.files[state.file].unplaced.forEach(function (u) { if (u.key === k) r = u.reason; });
  return r;
}

function openKey(k) {
  var m = byKey(false)[k] || [];
  var h = "<h3>" + esc(label(k)) + "</h3><p class=\"sub\">" + esc(where(k)) + " · " +
          m.length + " bindings · " + esc(state.faction) + "</p>";
  DATA.combos.forEach(function (c) {
    var list = m.filter(function (e) { return e[4] === c[0]; });
    if (!list.length) return;
    list = sortEntries(list);
    h += '<div class="grp">' + esc(c[1]) + " (" + list.length + ")</div>";
    list.forEach(function (e) {
      h += '<div class="ent"><span class="a" title="' + esc(e[0]) + '">' + esc(words(e[0])) + "</span>" +
           (e[1] ? ' <span class="u" title="' + esc(e[1]) + '">· ' + esc(words(e[1])) + "</span>" : "") +
           "<code>" + esc(e[5]) + "</code></div>";
    });
  });
  document.getElementById("pbody").innerHTML = h;
  document.getElementById("panel").className = "open";
  document.getElementById("close").onclick = function () { document.getElementById("panel").className = ""; };
}

function facButton(name) {
  return '<button class="t" data-f="' + esc(name) + '">' + esc(name) + "</button>";
}
function init() {
  var sel = document.getElementById("file");
  sel.innerHTML = DATA.order.map(function (n) { return "<option>" + n + "</option>"; }).join("");
  sel.onchange = function () { state.file = sel.value; render(); };
  var counts = {};
  DATA.order.forEach(function (n) {
    DATA.files[n].entries.forEach(function (e) { e[2].forEach(function (i) { counts[i] = 1; }); });
  });
  document.getElementById("views").innerHTML = VIEWS.map(function (v) {
    return '<button class="t" data-v="' + v[0] + '">' + v[1] + "</button>";
  }).join(" ");
  document.getElementById("fac-melee").innerHTML = DATA.melee.map(facButton).join(" ");
  document.getElementById("fac-coop").innerHTML = Object.keys(DATA.commanders).map(facButton).join(" ");
  var other = ["Global"];
  if (counts[UI]) other.push("Unclassified");
  document.getElementById("fac-other").innerHTML = other.map(facButton).join(" ");
  document.getElementById("mods").innerHTML =
    DATA.combos.map(function (c) { return '<button class="t" data-m="' + c[0] + '">' + c[1] + "</button>"; })
      .join(" ") + ' <button class="t" data-m="any">any</button>';
  Array.prototype.forEach.call(document.querySelectorAll("button.t[data-f]"), function (b) {
    b.onclick = function () { state.faction = b.getAttribute("data-f"); render(); };
  });
  Array.prototype.forEach.call(document.querySelectorAll("button.t[data-m]"), function (b) {
    b.onclick = function () { state.mod = b.getAttribute("data-m"); render(); };
  });
  Array.prototype.forEach.call(document.querySelectorAll("button.t[data-v]"), function (b) {
    b.onclick = function () { state.view = b.getAttribute("data-v"); render(); };
  });
  document.getElementById("q").oninput = function (ev) { state.q = ev.target.value; render(); };
  document.getElementById("legend").innerHTML =
    "<span class=\"z1\">zone 1 &mdash; easiest</span><span class=\"z2\">zone 2</span>" +
    "<span class=\"z3\">zone 3 &mdash; hardest</span>";
  document.getElementById("notes").innerHTML = [
    "<b>Banished commands stay banished.</b> TheCore parks the commands it never wants pressed by accident on " +
    "Ctrl+Shift+Alt, which this board can only make as Pad+Down+Knuckle. Nothing here changes that.",
    "<b>A firmware escape hatch exists, and is not taken in this pass.</b> SC2 accepts F13, F14 and up as hotkeys " +
    "and no ordinary board can send them, which is why TheCore's own community used them as a dumping ground " +
    "(wiki/thecore/hotkey-file-editing.md, Edennil 191702, 384532) and macroed Fn+key to unused F-keys to get a " +
    "one-press inject (wiki/thecore/keyboards-and-hardware.md, H:256033, H:157574, H:130369). The firmware could " +
    "emit F13-F24 from layer slots and free a banished command from the three-thumb-key contortion. Not done here.",
    "<b>Camera keys carry no replay load.</b> Replays record where the camera went, never which key moved it, so " +
    "camera view, camera save, Idle Worker and Town Camera all score zero and sort to the tail of the order. " +
    "They are placed on whatever middle and ring wells the control-group floor leaves, which is the Nail layer, and " +
    "the two or three that do not fit are listed above; that is a limit of the evidence, not a judgement that they " +
    "are unused.",
    "<b>The ten control groups own the middle and ring base keys.</b> Middle and ring have exactly ten base-plane " +
    "wells, and the ten ControlGroupRecall keys take all ten: no group sits elsewhere and nothing else sits there. " +
    "Slot difficulty also carries a per-finger weight (index 0.0, middle 0.0, ring 0.2, pinky 0.5). That weight is " +
    "an assumption, not replay evidence: the Svalboard wiki ranks positions within a finger, never fingers against " +
    "each other.",
    "<b>Some same-finger work is forced.</b> The control-group floor puts all ten groups on middle and ring, and " +
    "five control groups carry most of the load, so pairs such as CG1 &gt; CG3 land on one finger whatever the " +
    "search does. The layer is the escape the mapping does have: a transition that crosses into the Nail layer " +
    "is counted at half cost, and the climb spends that on the heaviest pairs.",
    "<b>The right hand is on a mouse.</b> Left click, right click and the two side buttons are not on the board " +
    "at all, and the thumb keys are the modifiers themselves, so they carry no commands of their own."
  ].map(function (s) { return "<li>" + s + "</li>"; }).join("");
  render();
}
init();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
