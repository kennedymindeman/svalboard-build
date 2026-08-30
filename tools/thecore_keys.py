#!/usr/bin/env python3
"""Per-key and per-finger load of a TheCore .SC2Hotkeys file.

Usage: tools/thecore_keys.py thecore/TheCore_5.0_Right_Plus.SC2Hotkeys [--commands]

For every physical key the file binds, prints how many command bindings land on
it, which modifier combinations it carries, and (with --commands) the commands.
Keys are grouped by the finger that presses them in TheCore 5.0 Right
(thecore/finger-chart-5.0.png). Keys not on the chart are listed as "other".
"""
import collections
import sys

FINGERS = {
    # Colour groups of thecore/finger-chart-5.0.png, named by the finger letters
    # in the 5.0 spreadsheet (J=p, I/K=r, O/L=m, P/;=i): the left hand sits on the
    # right side of the keyboard with the thumb on right Shift/Alt/Ctrl, so the
    # pinky is nearest the middle of the board.  The sheet puts U and 7 on the
    # ring finger; the chart colours them with the pinky group, kept here.
    "pinky": "7 Y U G H J B N M".split(),
    "ring": ["8", "I", "K", "Comma"],
    "middle": ["9", "O", "L", "Period"],
    "index": "0 Minus Equals Backspace P BracketOpen BracketClose BackSlash SemiColon Apostrophe Slash".split(),
    "thumb": ["Shift", "Alt", "Control"],
}
MODS = {"Control", "Shift", "Alt"}


def parse(path):
    """Yield (command, key, modifier-combo) for every alternate in [Hotkeys] and [Commands]."""
    section = None
    with open(path, encoding="utf-8-sig") as f:
        lines = f.read().splitlines()
    for line in lines:
        line = line.strip()
        if line.startswith("["):
            section = line
            continue
        if "=" not in line or section not in ("[Hotkeys]", "[Commands]"):
            continue
        cmd, val = line.split("=", 1)
        for alt in val.split(","):
            parts = [p for p in alt.split("+") if p]
            if not parts:
                continue
            base = [p for p in parts if p not in MODS]
            if base:
                key, mods = base[-1], [p for p in parts if p in MODS]
            else:
                # Modifier-only binding (CameraCenter=Alt): the last modifier is
                # the key, any others are held with it.
                key, mods = parts[-1], parts[:-1]
            combo = "+".join(sorted(mods)) or "plain"
            yield cmd, key, combo


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    show = "--commands" in sys.argv
    if len(args) != 1:
        sys.exit(__doc__)
    bindings = collections.defaultdict(list)
    for cmd, key, combo in parse(args[0]):
        bindings[key].append((combo, cmd))
    finger_of = {k: f for f, keys in FINGERS.items() for k in keys}
    groups = collections.defaultdict(list)
    for key in bindings:
        groups[finger_of.get(key, "other")].append(key)
    total = sum(len(v) for v in bindings.values())
    print(f"{args[0]}: {total} bindings on {len(bindings)} keys")
    for finger in list(FINGERS) + ["other"]:
        keys = sorted(groups[finger], key=lambda k: -len(bindings[k]))
        print(f"\n{finger}: {len(keys)} keys")
        for key in keys:
            combos = collections.Counter(c for c, _ in bindings[key])
            summary = " ".join(f"{c}:{n}" for c, n in combos.most_common())
            print(f"  {key:12} {len(bindings[key]):4}  {summary}")
            if show:
                for combo, cmd in sorted(bindings[key]):
                    print(f"      {combo:22} {cmd}")


if __name__ == "__main__":
    main()
