#!/usr/bin/env python3
"""Measure command frequency, control-group use and event sequences in SC2 replays.

Two subcommands:

  extract  parse .SC2Replay files into a JSONL event stream
  report   aggregate that stream into a wiki page and a JSON summary

Parsing is sc2reader at load_level=4 (s2protocol is not needed: sc2reader read
every replay in the set).  sc2reader does not install on system python 3.14, so
run it under 3.12:

  uv run --python 3.12 --with sc2reader python tools/sc2_sequences.py \
      extract replays/iem-katowice-2024 -o ~/scratch/thecore/events.jsonl.gz

  uv run --python 3.12 --with sc2reader python tools/sc2_sequences.py \
      report ~/scratch/thecore/events.jsonl.gz \
      -o wiki/sc2-command-sequences.md --summary thecore/sequences-summary.json \
      --replay-set "IEM Katowice 2024 main event" \
      --parse-note "All 187 replays in the pack parsed; none failed, ..."

The committed numbers were produced with a venv kept outside the repo,
/Users/kennedy/scratch/thecore/venv-replays (python 3.12, sc2reader 1.9.0):

  /Users/kennedy/scratch/thecore/venv-replays/bin/python tools/sc2_sequences.py ...

Co-op replays go through the same two steps with `--coop` on both, which groups
by commander instead of melee race and keeps only the human players (see
`extract_replay` and `solo_commanders`):

  uv run --python 3.12 --with sc2reader python tools/sc2_sequences.py \
      extract ~/scratch/thecore/coop/replays --coop \
      -o ~/scratch/thecore/coop/events.jsonl.gz

  uv run --python 3.12 --with sc2reader python tools/sc2_sequences.py \
      report ~/scratch/thecore/coop/events.jsonl.gz --coop \
      -o wiki/sc2-coop-sequences.md --summary thecore/coop-summary.json

`report` also accepts the summary JSON in place of the event stream, so the page
rebuilds without the replays (and without sc2reader, on any python 3):

  python3 tools/sc2_sequences.py report thecore/sequences-summary.json \
      -o wiki/sc2-command-sequences.md

Event stream: the first line of each replay is a `kind: "game"` record (map,
length, patch, players) so `report` can compute per-game and per-minute rates;
every other line is one event.  Paths ending in .gz are read/written gzipped.

Times are real seconds.  LotV on "Faster" runs 22.4 game loops per real second
(LOOPS_PER_SECOND below), so an event's frame divided by that is the wall-clock
time a viewer sees; `extract` refuses replays that are not LotV/Faster.
"""
import argparse
import collections
import gzip
import hashlib
import json
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from thecore_keys import FINGERS  # noqa: E402
from thecore_keymap import (MELEE, GLOBAL, COMMANDERS, UNIT_FACTIONS,  # noqa: E402
                            factions_for, own_factions, parse_entries)

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOTKEYS = os.path.join(HERE, "thecore", "TheCore_5.0_Right_Plus.SC2Hotkeys")

# A camera move is counted as a hotkey-style jump above this distance in map
# units.  Chosen from the measured distribution: successive camera positions
# have a dense scroll mode below ~8 units, a trough at 14-20 and a second mode
# above it (see wiki/sc2-command-sequences.md).
JUMP_UNITS = 20.0

# LotV "Faster" runs 22.4 game loops per real second; sc2reader's `real_length`
# uses the same factor.  Event frames are game loops, so frame / 22.4 is seconds.
LOOPS_PER_SECOND = 22.4

# Consecutive events by the same player closer than this (seconds) count as a
# pair for the bigram, trigram and same-finger numbers.
WINDOW = 1.0

# Tail lengths kept in the summary JSON.
TOP_ABILITIES, TOP_BIGRAMS, TOP_TRIGRAMS, TOP_PAIRS, TOP_UNMAPPED = 120, 200, 120, 60, 80

# sc2reader ability names that no rule below reaches from a command name in the
# .SC2Hotkeys file.  Built by hand from the names this replay set produced;
# every name the rules and this table miss is counted as unmapped and listed in
# the report.
ALIASES = {
    "RightClick": None,          # Smart Command: the mouse, not a key
    "ScanMove": "Attack",        # a-move
    "HoldPosition": "MoveHoldPosition",
    "Patrol": "MovePatrol",
    "Gather": "GatherProt",      # the file has one Gather binding, shared by all races
    "GatherProtoss": "GatherProt",
    "GatherTerran": "GatherProt",
    "GatherZerg": "GatherProt",
    "ScannerSweep": "Scan",
    "ExtraSupplies": "SupplyDrop",
    "CancelLast": "Cancel",
    "CancelSlot": "Cancel",
    "CancelBuilding": "Cancel",
    "PsionicStorm": "PsiStorm",
    "EMPRound": "EMP",
    "Consume": "ViperConsume",
    "SetWorkerRally": "RallySCV",
    "SetRallyPoint": "Rally",
    "SetRallyUnit": "Rally",
    "TrainViking": "VikingFighter",
    "LiberatorAGTarget": "LiberatorAGMode",
    "LiberatorAATarget": "LiberatorAAMode",
    "Revelation": "OracleRevelation",
    "BuildOracleStasisTrap": "OracleBuildStasisTrap",
    "OracleWeapon": "OracleWeaponOn",
    "BurrowWidowMine": "BurrowDown",
    "UnburrowWidowMine": "BurrowUp",
    "BurrowLurker": "LurkerBurrowDown",
    "UnburrowLurker": "LurkerBurrowUp",
    "LowerSupplyDepot": "Lower",
    "RaiseSupplyDepot": "Raise",
    "TankMode": "Unsiege",
    "UnloadAll": "CommandCenterUnloadAll",
    "UnloadAllBunker": "BunkerUnloadAll",
    "RootSporeCrawler": "SporeCrawlerRoot",
    "UprootSporeCrawler": "SporeCrawlerUproot",
    "RootSpineCrawler": "SpineCrawlerRoot",
    "MorphToLurker": "LurkerMP",
    "ResearchCombatShield": "ResearchShieldWall",
    "EvolveGlialReconstitution": "EvolveGlialRegeneration",
    "ResearchConcussiveShells": "ResearchPunisherGrenades",
    "ResearchZergGroundArmorsLevel1": "zerggroundarmor1",
    "EvolveMetabolicBoost": "zerglingmovementspeed",
    "UprootSpineCrawler": "SpineCrawlerUproot",
}

# Counted apart from key bindings: the mouse buttons, which have no finger in
# TheCore's chart.
MOUSE = {"RightClick"}


# ---------------------------------------------------------------- extract


def open_out(path):
    return gzip.open(path, "wt", encoding="utf-8") if path.endswith(".gz") \
        else open(path, "w", encoding="utf-8")


def open_in(path):
    return gzip.open(path, "rt", encoding="utf-8") if path.endswith(".gz") \
        else open(path, "r", encoding="utf-8")


def file_digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def replay_paths(inputs):
    out = []
    for item in inputs:
        if os.path.isdir(item):
            for root, _, files in os.walk(item):
                out += [os.path.join(root, f) for f in files
                        if f.lower().endswith(".sc2replay")]
        else:
            out.append(item)
    return sorted(out)


# The hotkey file's spelling of a commander sc2reader names differently.
COOP_ALIASES = {"Horner": "Han & Horner", "Han and Horner": "Han & Horner"}


def _norm(name):
    return re.sub(r"[^a-z0-9]", "", name.lower())


def solo_commanders(set_name, present):
    """For a `<Commander> Solo` directory, the commanders whose players count.

    A "solo" run in the archive still has two human slots: the runner and an
    ally who idles (usually a Raynor doing nothing, which is why counting both
    buries Raynor's real numbers under 700 idle games).  The directory names the
    commander of the run, so in a `... Solo` directory only that commander's
    players are kept; `-Co-Op` and anything unrecognised keep both humans.
    Returns None when no filtering applies, and an empty list for a Solo
    directory none of whose players plays the commander it names (a misfiled
    replay, which `extract` then skips rather than silently counting both
    humans).
    """
    if not set_name:
        return None
    n = _norm(set_name)
    if not n.endswith("solo"):
        return None
    n = n[: -len("solo")]
    return [c for c in present if _norm(c) in n or n in _norm(c)]


def set_of(path, roots):
    """The immediate directory a replay sits in under one of the input roots.

    The co-op archive files runs by commander ("Dehaka Solo", "Alarak-Co-Op"),
    which is provenance worth keeping even though the commander used for the
    counts comes from the replay itself.
    """
    path = os.path.abspath(path)
    for root in roots:
        if path.startswith(root + os.sep):
            rel = os.path.relpath(os.path.dirname(path), root)
            if rel != ".":
                return rel
    return None


HEX_ABILITY = "ability:0x%04X"
HEX_PREFIX = "ability:0x"

CG_KINDS = {0: "cg_set", 1: "cg_add", 2: "cg_get", 3: "cg_del",
            4: "cg_steal", 5: "cg_steal"}


class Misfiled(Exception):
    """A Solo-directory replay none of whose players plays that commander."""


def extract_replay(path, sc2reader, coop=False, set_name=None):
    """Yield JSON-able records for one replay: a game record, then its events.

    In `coop` mode the grouping key in every record (the `race` field) is the
    player's co-op commander instead of their melee race, and only players who
    have one are kept: that is what tells the two humans of a co-op game apart
    from Amon's computer players.  `replay.cooperative` is not used, because it
    is 0 on plenty of genuine co-op replays.
    """
    replay = sc2reader.load_replay(path, load_level=4)
    if replay.expansion != "LotV" or replay.speed != "Faster":
        raise ValueError(
            "%s is %s on %s; this tool only reads LotV replays on Faster, where "
            "one second is %g game loops"
            % (os.path.basename(path), replay.expansion, replay.speed,
               LOOPS_PER_SECOND))
    game = os.path.splitext(os.path.basename(path))[0]
    races = {}
    for p in replay.players:
        if coop:
            commander = (getattr(p, "commander", "") or "").strip()
            if not commander:
                continue          # Amon's computer players have no commander
            races[p.pid] = COOP_ALIASES.get(commander, commander)
        else:
            races[p.pid] = (p.play_race or "?")
    if coop and not races:
        raise ValueError("%s: no player has a commander, so it is not a co-op "
                         "replay" % os.path.basename(path))
    solo = solo_commanders(set_name, set(races.values())) if coop else None
    if solo == []:
        raise Misfiled(
            "%s: no player plays the commander its directory %r names, so it is "
            "misfiled and cannot be attributed" % (os.path.basename(path), set_name))
    if solo:
        races = {pid: c for pid, c in races.items() if c in solo}
    kept = [p for p in replay.players if p.pid in races]
    rec = {"kind": "game", "game": game, "map": replay.map_name,
           "patch": ".".join(str(n) for n in replay.versions[1:5]),
           "build": replay.build,
           "seconds": replay.game_length.seconds,
           "players": [{"pid": p.pid, "name": p.name, "race": races[p.pid],
                        "result": p.result} for p in kept]}
    if coop:
        rec["mode"] = "coop"
        rec["set"] = set_name
        rec["solo"] = bool(solo)
        rec["humans"] = len(kept)
    yield rec
    last_cam = {}
    for e in replay.events:
        pid = getattr(getattr(e, "player", None), "pid", None)
        if pid not in races:
            continue
        name = type(e).__name__
        rec = {"game": game, "player": pid, "race": races[pid],
               "t": round(e.frame / LOOPS_PER_SECOND, 3)}
        if name.endswith("CommandEvent"):
            rec["kind"] = "command_update" if name.startswith("Update") else "command"
            # A third of the commander-specific co-op abilities have no name in
            # sc2reader's data; their numeric id is stable within a build, so in
            # co-op mode it becomes the token instead of being thrown away.
            rec["ability"] = e.ability_name or (
                HEX_ABILITY % e.ability_id if coop and e.ability_id else None)
            rec["target"] = ("point" if "TargetPoint" in name else
                             "unit" if "TargetUnit" in name else "none")
        elif name.endswith("ControlGroupEvent"):
            rec["kind"] = CG_KINDS.get(e.update_type, "cg_other")
            rec["group"] = e.control_group
        elif name == "CameraEvent":
            rec["kind"] = "camera"
            prev = last_cam.get(pid)
            if prev is not None:
                rec["dist"] = round(math.hypot(e.x - prev[0], e.y - prev[1]), 2)
            last_cam[pid] = (e.x, e.y)
        else:
            continue
        yield rec


def cmd_extract(args):
    import sc2reader

    paths = replay_paths(args.inputs)
    roots = [os.path.abspath(i) for i in args.inputs if os.path.isdir(i)]
    parsed = failed = events = duplicate = misfiled = 0
    errors = []
    seen_digests = {}
    with open_out(args.out) as out:
        for i, path in enumerate(paths, 1):
            try:
                # The archive saves some runs twice under different names;
                # `paths` is sorted, so the first path of each byte-identical
                # group wins and the rest are skipped in the same order every
                # run.  Hashing sits inside the try so an unreadable file
                # counts as failed instead of aborting the run.
                digest = file_digest(path)
                if digest in seen_digests:
                    duplicate += 1
                    print("DUP  %s == %s" % (path, seen_digests[digest]),
                          file=sys.stderr)
                    continue
                seen_digests[digest] = path
                recs = list(extract_replay(path, sc2reader, coop=args.coop,
                                           set_name=set_of(path, roots)))
            except Misfiled as exc:
                misfiled += 1
                print("SKIP %s" % exc, file=sys.stderr)
                continue
            except Exception as exc:  # a replay sc2reader cannot read
                failed += 1
                errors.append("%s: %s: %s" % (os.path.basename(path),
                                              type(exc).__name__, exc))
                print("FAIL %s: %s" % (path, exc), file=sys.stderr)
                continue
            parsed += 1
            events += len(recs) - 1
            for r in recs:
                out.write(json.dumps(r, separators=(",", ":")) + "\n")
            if i % 25 == 0 or i == len(paths):
                print("  %d/%d replays, %d events" % (i, len(paths), events),
                      file=sys.stderr)
    print("parsed %d of %d files (%d duplicate, %d misfiled, %d failed), "
          "%d events -> %s"
          % (parsed, len(paths), duplicate, misfiled, failed, events, args.out),
          file=sys.stderr)
    for e in errors:
        print("  " + e, file=sys.stderr)


# ---------------------------------------------- TheCore key/finger mapping


def load_hotkeys(path=HOTKEYS):
    """Command name -> key, using only melee and global bindings.

    The file also binds ~17 co-op commanders, whose units reuse ability names
    (Blink/Stalker=J but Blink/SuperWarpGate=Y).  Entries whose unit is not
    Terran/Zerg/Protoss or global are dropped; the rest are grouped by the
    ability part of `Ability/Unit`, and the key most bindings agree on wins.
    """
    keys = collections.defaultdict(collections.Counter)
    for cmd, key, combo, _raw in parse_entries(path):
        ability, unit = (cmd.split("/", 1) + [None])[:2] if "/" in cmd else (cmd, None)
        facs = own_factions(unit)
        if not any(f in MELEE or f == GLOBAL for f in facs):
            continue
        keys[ability][key] += 1
    index, ambiguous = {}, {}
    for ability, counter in keys.items():
        index[ability] = counter.most_common(1)[0][0]
        if len(counter) > 1:
            ambiguous[ability] = counter.most_common()
    return index, ambiguous


def commander_hotkeys(commander, path=HOTKEYS):
    """Command name -> key for one co-op commander (its units plus global).

    The name is the one `extract` writes, already mapped through
    COOP_ALIASES to the hotkey file's spelling.

    Same majority vote as `load_hotkeys`, over a different slice of the file:
    the commander's own units and the melee units its race also fields, which is
    what `factions_for` in tools/thecore_keymap.py already computes for
    thecore/keymap.html.  A commander the file has no units for (Mengsk) keeps
    only the global bindings.
    """
    keys = collections.defaultdict(collections.Counter)
    for cmd, key, combo, _raw in parse_entries(path):
        ability, unit = (cmd.split("/", 1) + [None])[:2] if "/" in cmd else (cmd, None)
        if unit is None:
            facs = [GLOBAL]
        else:
            facs = factions_for(unit)
        if commander not in facs and GLOBAL not in facs:
            continue
        keys[ability][key] += 1
    return {a: c.most_common(1)[0][0] for a, c in keys.items()}


PREFIXES = ("Train", "Build", "WarpIn", "Warpin", "Use", "MorphTo", "Morph",
            "Research", "Calldown", "UpgradeTo", "Upgrade")
SIBLINGS = ("Train", "Build", "WarpIn", "Morph", "MorphTo")

# Stripping a unit name off a prefixed form can leave the prefix alone
# ("WarpInBarracksTechLab" -> "WarpIn"), and the file binds some of those as
# real global commands (WarpIn=Control+Shift+Alt+F10).  A bare prefix says
# nothing about which ability was used, so it is never a candidate on its own.
BARE_PREFIXES = {p.lower() for p in PREFIXES + SIBLINGS}
UNIT_NAMES = sorted((u for u in UNIT_FACTIONS if len(u) >= 3), key=len, reverse=True)


def _expand(name):
    """One name plus its prefix-swapped, Level-numbered, Mode-less and burrow forms."""
    out = [name]
    for p in PREFIXES:
        if name.startswith(p) and len(name) > len(p):
            rest = name[len(p):]
            out.append(rest)
            out += [q + rest for q in SIBLINGS]
            break
    out += [x[:-1] + "Level" + x[-1] for x in list(out) if x and x[-1].isdigit()]
    out += [x[:-6] + x[-1] for x in list(out) if x[-6:-1] == "Level"]
    out += [x[:-4] for x in list(out) if x.endswith("Mode") and len(x) > 4]
    if name.startswith("Unburrow"):
        out.append("BurrowUp")
    elif name.startswith("Burrow"):
        out.append("BurrowDown")
    return out


def candidates(ability):
    """Command names in the hotkey file that this sc2reader ability may be.

    Rules, in order: the name itself; the name with a Train/Build/WarpIn/Morph/
    Research/Upgrade prefix stripped or swapped for a sibling (sc2reader says
    TrainCyclone where the file says BuildCyclone/Factory); UpgradeX1 as
    XLevel1; then the same set again with a leading and with a trailing unit
    name removed (SCVRepair -> Repair, LiftBarracks -> Lift,
    BuildBarracksReactor -> Reactor).  A form that is nothing but a bare prefix
    is dropped (see BARE_PREFIXES).  Matching is exact first, then
    case-insensitive, since the file mixes MorphTo, Morphto and lower case.
    """
    if ability in ALIASES:
        alias = ALIASES[ability]
        return [] if alias is None else [alias]
    forms = _expand(ability)
    for f in list(forms):
        for unit in UNIT_NAMES:
            if f.startswith(unit) and len(f) > len(unit):
                forms += _expand(f[len(unit):])
    for f in list(forms):
        for unit in UNIT_NAMES:
            if f.endswith(unit) and len(f) > len(unit):
                forms += _expand(f[: -len(unit)])
    # Drop bare prefixes before the race forms are built, or "WarpIn" comes
    # back as "ProtossWarpIn"/"ProtossBuild", which the file does bind.
    forms = [f for f in forms if f and (f.lower() not in BARE_PREFIXES
                                        or f == ability)]
    forms += [r + f for f in list(forms) for r in ("Protoss", "Terran", "Zerg")]
    seen, uniq = set(), []
    for c in forms:
        if c and c not in seen:
            seen.add(c)
            uniq.append(c)
    return uniq


def key_for(ability, index, lower):
    cands = candidates(ability)
    for cand in cands:
        if cand in index:
            return index[cand], cand
    for cand in cands:
        hit = lower.get(cand.lower())
        if hit:
            return index[hit], hit
    return None, None


def build_map(abilities, index):
    """{sc2reader ability: (key, finger, matched command)} for what maps."""
    finger_of = {k: f for f, keys in FINGERS.items() for k in keys}
    lower = {}
    for name in index:
        lower.setdefault(name.lower(), name)
    mapping = {}
    for ability in abilities:
        key, cand = key_for(ability, index, lower)
        if key:
            mapping[ability] = (key, finger_of.get(key, "other"), cand)
    return mapping


def cg_keys(path=HOTKEYS):
    """{group: (recall key, finger)} from ControlGroupRecall<n>."""
    finger_of = {k: f for f, keys in FINGERS.items() for k in keys}
    out = {}
    for cmd, key, combo, _raw in parse_entries(path):
        if cmd.startswith("ControlGroupRecall"):
            out[int(cmd[-1])] = (key, finger_of.get(key, "other"))
    return out


# The normalisation is a pile of string rules, so these cases are checked on
# every `report` run (and by `--selftest`).  The six F10 entries are the ones a
# bare `WarpIn` candidate used to swallow; the rest are rules worth pinning.
NORMALISATION_CASES = {
    "TrainDisruptor": ("BracketOpen", "WarpinDisruptor"),
    "BuildBarracksTechLab": None,
    "BuildFactoryTechLab": None,
    "BuildStarportTechLab": None,
    "BuildLurkerDenMP": None,
    "MorphSwarmHost": None,
    "Revelation": ("BracketOpen", "OracleRevelation"),
    "SetWorkerRally": ("F", "RallySCV"),
    "BurrowLurker": ("J", "LurkerBurrowDown"),
    "RightClick": None,
    "TrainCyclone": ("BracketOpen", "BuildCyclone"),
    "ScanMove": ("P", "Attack"),
}


def selftest(index=None):
    """Check NORMALISATION_CASES; return a list of failure strings."""
    if index is None:
        index, _ = load_hotkeys()
    lower = {}
    for name in index:
        lower.setdefault(name.lower(), name)
    bad = []
    for ability, want in sorted(NORMALISATION_CASES.items()):
        key, cand = key_for(ability, index, lower)
        got = (key, cand) if key else None
        if got != want:
            bad.append("%s: expected %s, got %s" % (ability, want, got))
    return bad


def check_normalisation(index=None):
    bad = selftest(index)
    if bad:
        raise AssertionError("normalisation selftest failed:\n  "
                             + "\n  ".join(bad))
    print("selftest: %d normalisation cases OK" % len(NORMALISATION_CASES),
          file=sys.stderr)


# ----------------------------------------------------------------- report


def token(rec):
    """The sequence token for an event, or None if it is not in the stream."""
    if rec["kind"] == "command":
        return rec.get("ability") or "?unnamed"
    if rec["kind"] == "cg_get":
        return "CG%d" % rec["group"]
    return None


def aggregate(path):
    games = {}
    # per race
    R = lambda: {"player_games": 0, "seconds": 0, "commands": 0, "command_updates": 0,
                 "unnamed": 0, "abilities": collections.Counter(),
                 "cg": collections.Counter(), "camera": 0, "camera_jumps": 0,
                 "bigrams": collections.Counter(), "trigrams": collections.Counter(),
                 "pairs": 0, "games": set(), "players": set()}
    races = collections.defaultdict(R)
    streams = collections.defaultdict(list)   # (game, pid) -> [(t, token)]
    seen = set()
    with open_in(path) as f:
        for line in f:
            rec = json.loads(line)
            if rec["kind"] == "game":
                games[rec["game"]] = rec
                continue
            if rec["game"] not in games:
                raise ValueError(
                    "event for game %r before its `kind: \"game\"` record; the "
                    "stream must open each game with that record, and `extract` "
                    "writes a game's events only after it"
                    % rec["game"])
            race, kind = rec["race"], rec["kind"]
            r = races[race]
            key = (rec["game"], rec["player"])
            r["games"].add(rec["game"])
            if key not in seen:
                seen.add(key)
                r["player_games"] += 1
                r["seconds"] += games[rec["game"]]["seconds"]
                for p in games[rec["game"]]["players"]:
                    if p["pid"] == rec["player"]:
                        r["players"].add(p["name"])
            if kind == "command":
                r["commands"] += 1
                ability = rec.get("ability")
                if ability:
                    r["abilities"][ability] += 1
                else:
                    r["unnamed"] += 1
            elif kind == "command_update":
                r["command_updates"] += 1
            elif kind.startswith("cg_"):
                r["cg"]["%s/%d" % (kind, rec["group"])] += 1
            elif kind == "camera":
                r["camera"] += 1
                if rec.get("dist", 0) > JUMP_UNITS:
                    r["camera_jumps"] += 1
            tok = token(rec)
            if tok:
                streams[key].append((rec["t"], tok, race))
    return games, races, streams


def sequence_stats(races, streams, mappings, cg_finger):
    """Fill in bigrams, trigrams and the per-finger and same-finger numbers.

    `mappings` is {race or commander: {ability: (key, finger, command)}}; in
    melee every race shares one map, in co-op each commander has its own.
    """
    fingers = collections.defaultdict(collections.Counter)      # race -> finger
    keycount = collections.defaultdict(collections.Counter)     # race -> key
    # race -> [same finger, scored pairs, same key]; same key is a subset of
    # same finger, so "same finger, different key" is the difference.
    same = collections.defaultdict(lambda: [0, 0, 0])
    offenders = collections.defaultdict(collections.Counter)    # race -> pair
    mapped = collections.defaultdict(lambda: [0, 0])            # race -> [mapped, total]
    unmapped = collections.defaultdict(collections.Counter)

    def place(race, tok):
        """(key, finger) for a token, or (None, None) if it maps to neither."""
        if tok.startswith("CG") and tok[2:].isdigit():
            return cg_finger[int(tok[2:])]
        hit = mappings[race].get(tok)
        return (hit[0], hit[1]) if hit else (None, None)

    for (_game, _pid), stream in streams.items():
        # No sort: the stream is already in replay order, and events sharing a
        # frame have no other order to give them.  Sorting by token would
        # invent a direction for the ~8% of pairs that are same-frame.
        race = stream[0][2]
        r = races[race]
        for i, (t, tok, _) in enumerate(stream):
            k, f = place(race, tok)
            mapped[race][1] += 1
            if f:
                mapped[race][0] += 1
                fingers[race][f] += 1
                keycount[race][k] += 1
            else:
                unmapped[race][tok] += 1
            if i == 0:
                continue
            pt, ptok, _ = stream[i - 1]
            if t - pt > WINDOW:
                continue
            r["bigrams"]["%s > %s" % (ptok, tok)] += 1
            r["pairs"] += 1
            pk, pf = place(race, ptok)
            if f and pf:
                same[race][1] += 1
                if f == pf:
                    same[race][0] += 1
                    if k == pk:
                        # The same key twice: a repeat no layout can move away.
                        same[race][2] += 1
                    else:
                        offenders[race]["%s > %s (%s)" % (ptok, tok, f)] += 1
            if i > 1:
                ppt, pptok, _ = stream[i - 2]
                if pt - ppt <= WINDOW:
                    r["trigrams"]["%s > %s > %s" % (pptok, ptok, tok)] += 1
    return fingers, keycount, same, offenders, mapped, unmapped


def summarise(events_path, replay_set, parse_note, coop=False):
    index, ambiguous = load_hotkeys()
    check_normalisation(index)
    cg_finger = cg_keys()
    games, races, streams = aggregate(events_path)
    mappings, mapping = {}, {}
    for race, r in races.items():
        idx = commander_hotkeys(race) if coop else index
        mappings[race] = build_map(set(r["abilities"]), idx)
        mapping.update(mappings[race])
    fingers, keycount, same, offenders, mapped, unmapped = sequence_stats(
        races, streams, mappings, cg_finger)

    patches = collections.Counter(g["patch"] for g in games.values())
    out = {
        "mode": "coop" if coop else "melee",
        "replay_set": replay_set,
        "games": len(games),
        "patches": patches.most_common(),
        "parse": parse_note,
        "window_seconds": WINDOW,
        "loops_per_second": LOOPS_PER_SECOND,
        "jump_units": JUMP_UNITS,
        "hotkeys": os.path.relpath(HOTKEYS, HERE),
        "ambiguous_commands": len(ambiguous),
        "control_group_keys": {str(g): list(v) for g, v in sorted(cg_finger.items())},
        "races": {},
    }
    finger_of_key = {k: f for f, keys in FINGERS.items() for k in keys}
    for race, r in sorted(races.items()):
        pg, mins = r["player_games"], r["seconds"] / 60.0
        cmd_mapped = sum(c for a, c in r["abilities"].items()
                         if a in mappings[race])
        cmd_mouse = sum(c for a, c in r["abilities"].items() if a in MOUSE)
        cmd_hex = sum(c for a, c in r["abilities"].items()
                      if a.startswith(HEX_PREFIX))
        by_finger = fingers[race]
        s_same, s_pairs, s_key = same[race]
        s_diff = s_same - s_key
        pct = lambda n: round(100.0 * n / s_pairs, 1) if s_pairs else None
        out["races"][race] = {
            "player_games": pg,
            "games": len(r["games"]),
            # A count only: the handles themselves stay out of the repo.
            "distinct_players": len(r["players"]),
            "minutes": round(mins, 1),
            "commands": r["commands"],
            "commands_per_game": round(r["commands"] / pg, 1),
            "commands_per_minute": round(r["commands"] / mins, 1),
            "command_updates": r["command_updates"],
            "unnamed_commands": r["unnamed"],
            "distinct_abilities": len(r["abilities"]),
            "top_abilities": [[a, c, round(c / pg, 2), round(c / mins, 2),
                               round(100.0 * c / r["commands"], 2)]
                              for a, c in r["abilities"].most_common(TOP_ABILITIES)],
            "top_share": round(100.0 * sum(c for _, c in r["abilities"].most_common(40))
                               / r["commands"], 1),
            "control_groups": {k: [v, round(v / pg, 2), round(v / mins, 3)]
                               for k, v in sorted(r["cg"].items())},
            "control_group_events_per_minute": round(
                sum(r["cg"].values()) / mins, 2),
            "camera_events_per_game": round(r["camera"] / pg, 1),
            "camera_jumps_per_game": round(r["camera_jumps"] / pg, 1),
            "camera_jumps_per_minute": round(r["camera_jumps"] / mins, 2),
            "sequence_events": mapped[race][1],
            "pairs": r["pairs"],
            "pairs_per_game": round(r["pairs"] / pg, 1),
            "top_bigrams": [[b, c, round(c / pg, 2)]
                            for b, c in r["bigrams"].most_common(TOP_BIGRAMS)],
            "top_trigrams": [[b, c, round(c / pg, 2)]
                             for b, c in r["trigrams"].most_common(TOP_TRIGRAMS)],
            "mapped_commands": cmd_mapped,
            "mapped_command_share": round(100.0 * cmd_mapped / r["commands"], 1),
            "mouse_commands": cmd_mouse,
            "mouse_command_share": round(100.0 * cmd_mouse / r["commands"], 1),
            "hex_commands": cmd_hex,
            "hex_command_share": round(100.0 * cmd_hex / r["commands"], 1),
            "unmapped_command_share": round(
                100.0 * (r["commands"] - cmd_mapped - cmd_mouse) / r["commands"], 1),
            "mapped_sequence_events": mapped[race][0],
            "mapped_sequence_share": round(100.0 * mapped[race][0] / mapped[race][1], 1),
            "finger_share": {f: round(100.0 * c / sum(by_finger.values()), 1)
                             for f, c in by_finger.most_common()},
            "finger_counts": dict(by_finger.most_common()),
            "key_events_per_minute": [[k, finger_of_key.get(k, "other"), c,
                                       round(c / mins, 2)]
                                      for k, c in keycount[race].most_common()],
            "same_finger_pairs": s_same,
            "scored_pairs": s_pairs,
            "same_finger_rate": pct(s_same),
            "same_key_pairs": s_key,
            "same_key_rate": pct(s_key),
            "same_finger_diff_key_pairs": s_diff,
            "same_finger_diff_key_rate": pct(s_diff),
            "top_same_finger": [[p, c, round(c / pg, 2)]
                                for p, c in offenders[race].most_common(TOP_PAIRS)],
            "top_unmapped": [[a, c] for a, c in unmapped[race].most_common(TOP_UNMAPPED)],
            "unmapped_events": mapped[race][1] - mapped[race][0],
        }
    out["ability_key_map"] = {a: [v[0], v[1], v[2]] for a, v in sorted(mapping.items())}
    out["ambiguous_examples"] = sorted(ambiguous)[:40]
    return out


# ------------------------------------------------------------- markdown


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    for row in rows:
        out.append("| " + " | ".join(str(c) for c in row) + " |")
    return out


def render(s):
    races = s["races"]
    order = [r for r in ("Terran", "Protoss", "Zerg") if r in races] + \
            [r for r in sorted(races) if r not in ("Terran", "Protoss", "Zerg")]
    L = []
    L.append("---")
    L.append("type: Reference")
    L.append("title: SC2 command sequences, measured")
    L.append("description: Command frequencies, control-group and camera use, "
             "and event sequences measured from %d professional StarCraft II "
             "replays, projected onto TheCore 5.0's keys and fingers."
             % s["games"])
    L.append("tags: [starcraft, thecore, gaming, measurement, hotkeys]")
    L.append('source: "%s; measured with tools/sc2_sequences.py"' % s["replay_set"])
    L.append("---")
    L.append("")
    L.append("# SC2 command sequences, measured")
    L.append("")
    if len(s["patches"]) == 1:
        patches = s["patches"][0][0]
    else:
        patches = ", ".join("%s (%d games)" % (p, n) for p, n in s["patches"])
    L.append(("Every number on this page is measured from replays, not estimated. "
              "The set is **%s**: %d games, patch %s, parsed with sc2reader at "
              "`load_level=4`."
              % (s["replay_set"], s["games"], patches)).rstrip())
    L.append("")
    L.append("Co-op Commanders are measured separately, one set of numbers per "
             "commander, in [SC2 co-op command sequences, measured]"
             "(sc2-coop-sequences.md).")
    L.append("")
    L.append("`tools/sc2_sequences.py` produced both this page and "
             "`thecore/sequences-summary.json`, which holds the same aggregates; "
             "the page can be rebuilt from that file alone, without the replays. "
             "`replays/README.md` says how to fetch the set again.")
    L.append("")
    L.append("## What is counted")
    L.append("")
    L.append("- **Command**: one `CommandEvent` in the replay, i.e. one ability "
             "the player issued. Right-clicks (`RightClick`) are in the counts "
             "and are a mouse action, not a key.")
    L.append("- Follow-up `UpdateTargetPoint`/`UpdateTargetUnit` events (a target "
             "dragged while the mouse is down) are counted separately and left "
             "out of every rate below; including them would roughly double the "
             "right-click count.")
    L.append("- **Control group**: `set` (Shift+key in TheCore), `add` "
             "(Shift+Alt+key), `steal` (Ctrl+key, the steal-and-add and "
             "steal-and-set update types), `recall` (the bare key).")
    L.append("- **Camera jump**: two successive camera positions more than "
             "%g map units apart. The distribution of that distance is bimodal, "
             "with scrolling below ~8 units, a trough at 14-20 and a second mode "
             "above it, so %g sits in the trough. Replays record where the camera "
             "went, never which key moved it, so minimap clicks and follow-unit "
             "land in the same bucket: read jumps as an upper bound on camera "
             "hotkey presses." % (s["jump_units"], s["jump_units"]))
    L.append("- **Sequence**: consecutive events by the same player no more than "
             "%g s apart, over a stream of commands and control-group recalls "
             "(the two things a hand does between camera moves). Times come "
             "from the replay's game loops at %g loops per second, the LotV "
             "\"Faster\" rate every game in this set was played at, so they are "
             "real seconds a viewer would count. Events that share a loop keep "
             "the order the replay records them in; nothing is re-sorted."
             % (s["window_seconds"], s.get("loops_per_second", LOOPS_PER_SECOND)))
    L.append("- **TheCore projection**: sc2reader ability names normalised to the "
             "command names in `%s`, then to that file's key and to the finger "
             "that presses it (`FINGERS` in `tools/thecore_keys.py`). Modifiers "
             "ride the thumb in TheCore, so a modified binding is counted on the "
             "finger of its base key." % s["hotkeys"])
    L.append("")
    L.append("## Coverage")
    L.append("")
    if s["parse"]:
        L.append(s["parse"])
        L.append("")
    rows = []
    for race in order:
        r = races[race]
        rows.append([race, r["player_games"], r["commands"], r["distinct_abilities"],
                     "%s%%" % r["mapped_command_share"],
                     "%s%%" % r["mouse_command_share"],
                     "%s%%" % r["unmapped_command_share"], r["unnamed_commands"]])
    L += table(["Race", "Player-games", "Commands", "Distinct abilities",
                "On a TheCore key", "Mouse (right-click)", "No binding found",
                "Unnamed by sc2reader"], rows)
    L.append("")
    L.append("Right-clicking is the mouse and has no key in the file, so it is "
             "its own column. What is left over is ability names the file does "
             "not bind under any name the normalisation reaches: mostly upgrades "
             "at tech buildings, and a few sizeable gaps (`SpawnLarva`, the "
             "queen inject, is the largest). The biggest unmapped names per race "
             "are listed with each race below. The hotkey file also binds 17 co-op commanders "
             "whose units share ability names with the melee ones (%d command "
             "names carry more than one key); only Terran/Zerg/Protoss and global "
             "bindings are used here." % s["ambiguous_commands"])
    L.append("")

    for race in order:
        r = races[race]
        L.append("## %s" % race)
        L.append("")
        L.append("%d player-games, %.0f minutes played, %d commands: "
                 "**%s per game, %s per minute**. Control-group and camera "
                 "numbers are per game."
                 % (r["player_games"], r["minutes"], r["commands"],
                    r["commands_per_game"], r["commands_per_minute"]))
        L.append("")
        L.append("### Top 40 abilities")
        L.append("")
        L.append("These 40 are %s%% of all %s commands." % (r["top_share"], race))
        L.append("")
        rows = [[i + 1, a, c, per_game, per_min, "%s%%" % share]
                for i, (a, c, per_game, per_min, share)
                in enumerate(r["top_abilities"][:40])]
        L += table(["#", "Ability", "Count", "Per game", "Per minute", "Share"], rows)
        L.append("")
        L.append("### Control groups")
        L.append("")
        actions = [("cg_set", "set"), ("cg_add", "add"), ("cg_steal", "steal"),
                   ("cg_get", "recall")]
        rows = []
        for g in range(10):
            row = [g]
            for kind, _label in actions:
                row.append(r["control_groups"].get("%s/%d" % (kind, g), [0, 0])[1])
            rows.append(row)
        totals = ["all"]
        for kind, _label in actions:
            totals.append(round(sum(v[1] for k, v in r["control_groups"].items()
                                    if k.startswith(kind + "/")), 2))
        rows.append(totals)
        L += table(["Group", "Set/game", "Add/game", "Steal/game", "Recall/game"], rows)
        L.append("")
        L.append("### Camera")
        L.append("")
        L.append("%s camera events per game, of which %s are jumps over %g map "
                 "units (%s per minute)."
                 % (r["camera_events_per_game"], r["camera_jumps_per_game"],
                    s["jump_units"], r["camera_jumps_per_minute"]))
        L.append("")
        L.append("### Sequences")
        L.append("")
        L.append("%d consecutive pairs within %gs, %s per game."
                 % (r["pairs"], s["window_seconds"], r["pairs_per_game"]))
        L.append("")
        L.append("Top 30 bigrams:")
        L.append("")
        L += table(["#", "Pair", "Count", "Per game"],
                   [[i + 1, b, c, pg] for i, (b, c, pg)
                    in enumerate(r["top_bigrams"][:30])])
        L.append("")
        L.append("Top 20 trigrams:")
        L.append("")
        L += table(["#", "Triple", "Count", "Per game"],
                   [[i + 1, b, c, pg] for i, (b, c, pg)
                    in enumerate(r["top_trigrams"][:20])])
        L.append("")
        L.append("### TheCore 5.0 projection")
        L.append("")
        L.append("%s%% of the %d sequence events (commands plus control-group "
                 "recalls) map to a key. Share of those events per finger:"
                 % (r["mapped_sequence_share"], r["sequence_events"]))
        L.append("")
        L += table(["Finger", "Share of mapped events", "Events"],
                   [[f, "%s%%" % sh, r["finger_counts"][f]]
                    for f, sh in r["finger_share"].items()])
        L.append("")
        L.append("**Same-finger repetition: %s%%** of the %d within-%gs pairs "
                 "where both events map to a key land on the same finger. That "
                 "splits into %s%% the same key twice (a repeat no layout can "
                 "move apart, mostly a control group recalled again) and "
                 "**%s%% the same finger on a different key**, which is the "
                 "part a layout controls."
                 % (r["same_finger_rate"], r["scored_pairs"], s["window_seconds"],
                    r["same_key_rate"], r["same_finger_diff_key_rate"]))
        L.append("")
        L.append("Worst pairs (same finger, different key):")
        L.append("")
        L += table(["#", "Pair (finger)", "Count", "Per game"],
                   [[i + 1, p, c, pg] for i, (p, c, pg)
                    in enumerate(r["top_same_finger"][:15])])
        L.append("")
        L.append("Largest unmapped names: %s."
                 % ", ".join("`%s` (%d)" % (a, c) for a, c in r["top_unmapped"][:10]))
        L.append("")
    L.append("## Reproducing")
    L.append("")
    L.append("```")
    L.append("# fetch the replays: see replays/README.md")
    L.append("uv run --python 3.12 --with sc2reader python tools/sc2_sequences.py \\")
    L.append("    extract replays/ -o ~/scratch/thecore/events.jsonl.gz")
    L.append("uv run --python 3.12 --with sc2reader python tools/sc2_sequences.py \\")
    L.append("    report ~/scratch/thecore/events.jsonl.gz \\")
    L.append("    -o wiki/sc2-command-sequences.md --summary thecore/sequences-summary.json")
    L.append("# or rebuild this page from the committed summary alone:")
    L.append("python3 tools/sc2_sequences.py report thecore/sequences-summary.json \\")
    L.append("    -o wiki/sc2-command-sequences.md")
    L.append("```")
    L.append("")
    return "\n".join(L)


def render_coop(s):
    """The co-op page: same measurements, keyed by commander instead of race."""
    coms = s["races"]
    order = sorted(coms, key=lambda c: -coms[c]["player_games"])
    builds = [p for p, _ in s["patches"]]
    L = []
    L.append("---")
    L.append("type: Reference")
    L.append("title: SC2 co-op command sequences, measured")
    L.append("description: Command frequencies, control-group use and event "
             "sequences measured from %d StarCraft II Co-op speedrun replays, "
             "one set of numbers per commander." % s["games"])
    L.append("tags: [starcraft, thecore, gaming, measurement, hotkeys, coop]")
    L.append('source: "%s; measured with tools/sc2_sequences.py"' % s["replay_set"])
    L.append("---")
    L.append("")
    L.append("# SC2 co-op command sequences, measured")
    L.append("")
    L.append("The companion to [SC2 command sequences, measured]"
             "(sc2-command-sequences.md), which measures 1v1 pro play. This page "
             "measures **Co-op Commanders** instead: %d replays, %d player-games, "
             "%d commanders, %s minutes played. Co-op is where a hotkey layout is "
             "stressed differently: every commander has its own calldowns and top-bar "
             "abilities on top of the melee kit."
             % (s["games"], sum(c["player_games"] for c in coms.values()),
                len(coms), format(round(sum(c["minutes"] for c in coms.values())), ",")))
    L.append("")
    L.append("## Where the replays come from")
    L.append("")
    L.append("The set is the community **co-op speedrun archive**: the replays "
             "behind the clear-time leaderboards on "
             "[starcraft2coop.com](https://starcraft2coop.com/), kept in the public "
             "Google Drive folder "
             "[0B0kAPEv3WqAeZlhmbzN5NWlDc1E]"
             "(https://drive.google.com/drive/folders/0B0kAPEv3WqAeZlhmbzN5NWlDc1E), "
             "one directory per commander (`Dehaka Solo`, `Alarak-Co-Op`, ...). "
             "These are record attempts, not average games, so read every rate as "
             "the fast end of what a player does, not the median.")
    L.append("")
    L.append("The archive is old and wide: %d distinct game builds, %s to %s. "
             "`replays/README.md` says how to fetch it and where it lives locally."
             % (len(builds), min(builds, key=lambda p: int(p.rsplit(".", 1)[-1])),
                max(builds, key=lambda p: int(p.rsplit(".", 1)[-1]))))
    L.append("")
    L.append("## What is counted")
    L.append("")
    L.append("Definitions (command, control-group action, camera jump, sequence "
             "pair, the TheCore projection) are the ones on the "
             "[1v1 page](sc2-command-sequences.md#what-is-counted), with three "
             "co-op-specific points:")
    L.append("")
    L.append("- **Who is a player.** A co-op replay has two player slots and a pile "
             "of Amon computer players. Human players are the ones with a commander; "
             "`replay.cooperative` is not used, because it is 0 on plenty of these "
             "replays. In a two-human run each player is counted under their own "
             "commander, so one replay can feed two commanders' numbers.")
    L.append("- **Hex-id tokens.** sc2reader has no name for many "
             "commander-specific abilities, so about %s%% of commands here arrive as "
             "a numeric ability id, written `ability:0x....`. They are kept verbatim "
             "rather than dropped: the id is stable inside a build, so it counts and "
             "sequences correctly, and only the label is missing. Because the archive "
             "spans %d builds, the same id can mean different abilities in different "
             "years \u2014 treat a hex token as a within-commander shape, not a name."
             % (round(100.0 * sum(c["hex_commands"] for c in coms.values())
                      / max(1, sum(c["commands"] for c in coms.values())), 1),
                len(builds)))
    L.append("- **Camera hotkeys are invisible.** A replay records where the camera "
             "went, never which key sent it there, and co-op players lean on camera "
             "hotkeys and the minimap hard. The camera-jump counts below are an upper "
             "bound on camera hotkey presses, and no camera key appears in the "
             "sequences at all, so the real same-finger load is higher than the "
             "numbers here.")
    L.append("")
    L.append("## Commanders")
    L.append("")
    if s["parse"]:
        L.append(s["parse"])
        L.append("")
    rows = []
    for c in order:
        r = coms[c]
        rows.append([c, r["games"], r["player_games"], r["distinct_players"],
                     round(r["minutes"]), r["commands"], r["commands_per_minute"],
                     r["control_group_events_per_minute"],
                     r["camera_jumps_per_minute"], r["distinct_abilities"],
                     "%s%%" % r["hex_command_share"],
                     "%s%%" % r["mapped_command_share"]])
    L += table(["Commander", "Replays", "Player-games", "Players", "Minutes",
                "Commands", "Commands/min", "CG actions/min", "Camera jumps/min",
                "Distinct abilities", "Hex-id share", "On a TheCore key"], rows)
    L.append("")
    by_cg = sorted(order, key=lambda c: -coms[c]["control_group_events_per_minute"])
    hi, lo = by_cg[0], by_cg[-1]
    L.append("Control-group load is the number that varies most, and not with "
             "command rate: %s runs %s control-group actions a minute (mostly "
             "recalls, on %.0f minutes of play) against %s's %s. That spread "
             "may be the runner rather than the commander. The \"Players\" "
             "column counts the distinct handles behind the player-games, and "
             "the counts are small: %s's %d player-games come from %d players "
             "and %s's %d from %d, with two or three runners holding a large "
             "share of the rows in every commander. Per-player rates inside one "
             "commander are about as spread out as the rates between "
             "commanders, so each row describes a handful of record holders at "
             "least as much as it describes the commander."
             % (hi, coms[hi]["control_group_events_per_minute"],
                coms[hi]["minutes"], lo,
                coms[lo]["control_group_events_per_minute"],
                hi, coms[hi]["player_games"], coms[hi]["distinct_players"],
                lo, coms[lo]["player_games"], coms[lo]["distinct_players"]))
    L.append("")
    L.append("\"On a TheCore key\" uses only the bindings the hotkey file gives that "
             "commander (its own units, its race's melee units, and the global "
             "commands), so it is a fair per-commander coverage figure. The rest "
             "of each commander's commands are three things: right-clicks, which "
             "are a mouse action and no layout's business (%s%% of all commands "
             "here); hex-id commands, which have no name to look up (%s%%); and "
             "named commands the hotkey file does not bind (%s%%). Right-clicks "
             "are the largest of the three for %d of the %d commanders, so most "
             "of the gap is the mouse, not the missing names."
             % (round(100.0 * sum(c["mouse_commands"] for c in coms.values())
                      / max(1, sum(c["commands"] for c in coms.values())), 1),
                round(100.0 * sum(c["hex_commands"] for c in coms.values())
                      / max(1, sum(c["commands"] for c in coms.values())), 1),
                round(100.0 * sum(c["commands"] - c["mapped_commands"]
                                  - c["mouse_commands"] - c["hex_commands"]
                                  for c in coms.values())
                      / max(1, sum(c["commands"] for c in coms.values())), 1),
                sum(1 for c in coms.values()
                    if c["mouse_command_share"] >= max(
                        c["hex_command_share"],
                        c["unmapped_command_share"] - c["hex_command_share"])),
                len(coms)))
    L.append("")
    for c in order:
        r = coms[c]
        L.append("### %s" % c)
        L.append("")
        L.append("%d replays, %d player-games, %.0f minutes, %d commands: "
                 "**%s commands per minute** (%s per game). "
                 "%s control-group actions and %s camera jumps per minute. "
                 "%s%% of commands are hex ids."
                 % (r["games"], r["player_games"], r["minutes"], r["commands"],
                    r["commands_per_minute"], r["commands_per_game"],
                    r["control_group_events_per_minute"],
                    r["camera_jumps_per_minute"], r["hex_command_share"]))
        L.append("")
        L.append("Top abilities, per minute:")
        L.append("")
        L += table(["#", "Ability", "Per minute", "Share of commands"],
                   [[i + 1, a, pm, "%s%%" % sh] for i, (a, _c, _pg, pm, sh)
                    in enumerate(r["top_abilities"][:15])])
        L.append("")
        L.append("Control groups, actions per minute:")
        L.append("")
        actions = [("cg_set", "Set"), ("cg_add", "Add"), ("cg_steal", "Steal"),
                   ("cg_get", "Recall")]
        rows = []
        for g in range(10):
            row = [g]
            for kind, _label in actions:
                row.append(r["control_groups"].get("%s/%d" % (kind, g),
                                                   [0, 0, 0])[2])
            if any(v for v in row[1:]):
                rows.append(row)
        rows.append(["all"] + [round(sum(v[2] for k, v in r["control_groups"].items()
                                         if k.startswith(kind + "/")), 2)
                               for kind, _l in actions])
        L += table(["Group", "Set/min", "Add/min", "Steal/min", "Recall/min"], rows)
        L.append("")
        L.append("Busiest TheCore keys (of the %s%% of sequence events that map to "
                 "one):" % r["mapped_sequence_share"])
        L.append("")
        L += table(["Key", "Finger", "Events/min"],
                   [[k, f, pm] for k, f, _c, pm in r["key_events_per_minute"][:10]])
        L.append("")
        L.append("Top pairs within %gs (%s per minute over %d pairs):"
                 % (s["window_seconds"], round(r["pairs"] / r["minutes"], 1),
                    r["pairs"]))
        L.append("")
        L += table(["#", "Pair", "Count", "Per game"],
                   [[i + 1, b, n, pg] for i, (b, n, pg)
                    in enumerate(r["top_bigrams"][:12])])
        L.append("")
        if r["same_finger_rate"] is not None:
            L.append("Same finger on the next key: **%s%%** of the %d pairs where "
                     "both events map to a key. Of those same pairs, %s%% are the "
                     "same key twice (a repeat no layout can move apart) and "
                     "**%s%% are the same finger on a different key**."
                     % (r["same_finger_rate"], r["scored_pairs"],
                        r["same_key_rate"], r["same_finger_diff_key_rate"]))
            L.append("")
    L.append("## Reproducing")
    L.append("")
    L.append("```")
    L.append("# fetch the archive: see replays/README.md")
    L.append("uv run --python 3.12 --with sc2reader python tools/sc2_sequences.py \\")
    L.append("    extract ~/scratch/thecore/coop/replays --coop \\")
    L.append("    -o ~/scratch/thecore/coop/events.jsonl.gz")
    L.append("uv run --python 3.12 --with sc2reader python tools/sc2_sequences.py \\")
    L.append("    report ~/scratch/thecore/coop/events.jsonl.gz --coop \\")
    L.append("    -o wiki/sc2-coop-sequences.md --summary thecore/coop-summary.json \\")
    L.append("    --replay-set ... --parse-note ...   # exact text: replays/README.md")
    L.append("# or rebuild this page from the committed summary alone:")
    L.append("python3 tools/sc2_sequences.py report thecore/coop-summary.json \\")
    L.append("    -o wiki/sc2-coop-sequences.md")
    L.append("```")
    L.append("")
    L.append("The full aggregates, including the top %d bigrams and the top %d "
             "abilities per commander, are in `thecore/coop-summary.json`; the "
             "replays and the event stream stay out of the repo."
             % (TOP_BIGRAMS, TOP_ABILITIES))
    L.append("")
    return "\n".join(L)


def cmd_report(args):
    if args.input.endswith(".json"):
        check_normalisation()
        with open(args.input, encoding="utf-8") as f:
            summary = json.load(f)
    else:
        summary = summarise(args.input, args.replay_set, args.parse_note,
                            coop=args.coop)
    if args.summary:
        with open(args.summary, "w", encoding="utf-8") as f:
            json.dump(summary, f, separators=(",", ":"), sort_keys=False)
        print("wrote %s (%.0f KB)" % (args.summary,
                                      os.path.getsize(args.summary) / 1024.0),
              file=sys.stderr)
    renderer = render_coop if summary.get("mode") == "coop" else render
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(renderer(summary))
    print("wrote %s" % args.out, file=sys.stderr)


def cmd_selftest(_args):
    bad = selftest()
    for line in bad:
        print("FAIL " + line, file=sys.stderr)
    print("%d of %d normalisation cases OK"
          % (len(NORMALISATION_CASES) - len(bad), len(NORMALISATION_CASES)))
    return sys.exit(1) if bad else None


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("extract", help="parse replays into a JSONL event stream")
    e.add_argument("inputs", nargs="+", help=".SC2Replay files or directories")
    e.add_argument("-o", "--out", required=True, help="output .jsonl or .jsonl.gz")
    e.add_argument("--coop", action="store_true",
                   help="co-op replays: group by commander, keep only the "
                        "human players (those with one)")
    e.set_defaults(func=cmd_extract)
    r = sub.add_parser("report", help="aggregate a stream into a page and a summary")
    r.add_argument("input", help="events .jsonl[.gz], or a summary .json to re-render")
    r.add_argument("-o", "--out", required=True, help="output markdown page")
    r.add_argument("--summary", help="output summary JSON")
    r.add_argument("--replay-set", default="IEM Katowice 2024 main event",
                   help="name of the replay set, for the page")
    r.add_argument("--parse-note", default="", help="one sentence on parse coverage")
    r.add_argument("--coop", action="store_true",
                   help="co-op stream: group by commander and render the co-op page")
    r.set_defaults(func=cmd_report)
    t = sub.add_parser("selftest", help="check the ability-name normalisation")
    t.set_defaults(func=cmd_selftest)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
