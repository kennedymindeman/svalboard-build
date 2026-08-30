#!/usr/bin/env python3
"""Build thecore/svalboard-keymap.html: TheCore's bindings on a Svalboard.

Usage: python3 tools/thecore_svalboard.py

Takes the same parse and faction classification as tools/thecore_keymap.py and
transplants every binding onto the Svalboard key it would be pressed with,
using the fixed key mapping in SVALBOARD (derived in
wiki/thecore-method-on-a-svalboard.md section 4d).  Keys with no Svalboard home
are listed separately; their names are printed to stderr per file.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from thecore_keymap import (  # noqa: E402
    COMMANDERS, FACTIONS, GLOBAL, MELEE, UNCLASSIFIED, factions_for, parse_entries,
)

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = [
    ("TheCore 5.0 Right Plus", "thecore/TheCore_5.0_Right_Plus.SC2Hotkeys"),
    ("TheCore 6.0 Right", "thecore/TheCore6g_right_US_qwerty.SC2Hotkeys"),
]
OUT = "thecore/svalboard-keymap.html"

# TheCore key name (as parsed) -> (hand, finger, position).
SVALBOARD = {
    # Left hand: TheCore's one-hand core, per wiki/thecore-method-on-a-svalboard.md section 4d
    "P": ("L", "index", "centre"), "SemiColon": ("L", "index", "south"), "Minus": ("L", "index", "inward"),
    "BracketOpen": ("L", "index", "north"), "Apostrophe": ("L", "index", "outward"),
    "O": ("L", "middle", "centre"), "L": ("L", "middle", "south"), "9": ("L", "middle", "inward"),
    "0": ("L", "middle", "north"), "Period": ("L", "middle", "outward"),
    "I": ("L", "ring", "centre"), "K": ("L", "ring", "south"), "7": ("L", "ring", "inward"),
    "8": ("L", "ring", "north"), "U": ("L", "ring", "outward"),
    "J": ("L", "pinky", "centre"), "H": ("L", "pinky", "south"), "M": ("L", "pinky", "inward"),
    "N": ("L", "pinky", "outward"), "G": ("L", "pinky", "north"),
    "Control": ("L", "thumb", "pad"), "Shift": ("L", "thumb", "down"), "Alt": ("L", "thumb", "knuckle"),
    # Right hand: overflow and TheCore's off-hand keys, placed by load then zone
    "LeftMouseButton": ("R", "index", "centre"), "Equals": ("R", "index", "south"),
    "BracketClose": ("R", "index", "inward"), "D": ("R", "index", "north"), "W": ("R", "index", "outward"),
    "RightMouseButton": ("R", "middle", "centre"), "Slash": ("R", "middle", "south"),
    "X": ("R", "middle", "inward"), "R": ("R", "middle", "north"), "Backspace": ("R", "middle", "outward"),
    "Comma": ("R", "ring", "centre"), "E": ("R", "ring", "south"), "Z": ("R", "ring", "inward"),
    "F": ("R", "ring", "north"), "6": ("R", "ring", "outward"),
    "B": ("R", "pinky", "centre"), "Y": ("R", "pinky", "south"), "C": ("R", "pinky", "inward"),
    "A": ("R", "pinky", "outward"), "Q": ("R", "pinky", "north"),
    "ForwardMouseButton": ("R", "thumb", "pad"), "BackMouseButton": ("R", "thumb", "nail"),
    "Enter": ("R", "thumb", "down"), "Escape": ("R", "thumb", "knuckle"), "Tab": ("R", "thumb", "up"),
}

# Every key that must be unplaced in the 5.0 file, as a guard on the mapping.
EXPECTED_UNPLACED_50 = {"F10", "V", "F8", "3", "4", "CapsLock"}

FINGERS = ["index", "middle", "ring", "pinky"]
POSITIONS = ["centre", "south", "inward", "north", "outward"]
THUMB_POSITIONS = ["pad", "nail", "down", "knuckle", "up"]

ROLES = {
    ("L", "index"): {"centre": "Command 2", "south": "Command 3", "inward": "Command 4",
                     "north": "Command 5", "outward": "Command 7"},
    ("L", "middle"): {"centre": "CG 1", "south": "CG 3", "inward": "CG 4",
                      "north": "CG 5", "outward": "CG 10"},
    ("L", "ring"): {"centre": "CG 2", "south": "CG 6", "inward": "Idle Worker",
                    "north": "CG 7", "outward": "CG 8"},
    ("L", "pinky"): {"centre": "Command 1", "south": "Command 6", "inward": "Command 8",
                     "outward": "Command 9", "north": "Command 12"},
    ("L", "thumb"): {"pad": "Ctrl", "down": "Shift", "knuckle": "Alt",
                     "nail": "Fn layer (reserved)", "up": "Game layer lock (reserved)"},
    ("R", "index"): {"centre": "Left click", "south": "Command 10", "inward": "Command 11",
                     "north": "spare (D)", "outward": "spare (W)"},
    ("R", "middle"): {"centre": "Right click", "south": "Special Command 1", "inward": "spare (X)",
                      "north": "spare (R)", "outward": "Camera turn"},
    ("R", "ring"): {"centre": "CG 9", "south": "spare (E)", "inward": "Rally",
                    "north": "Rally SCV", "outward": "Town camera"},
    ("R", "pinky"): {"centre": "Command 13", "south": "Larva / Patrol", "inward": "spare (C)",
                     "outward": "Move", "north": "spare (Q)"},
    ("R", "thumb"): {"pad": "Subgroup next", "nail": "Subgroup prev", "down": "Chat",
                     "knuckle": "Escape / menu", "up": "Chat recipient"},
}

THUMB_ZONES = {"pad": 1, "nail": 2, "down": 2, "up": 3, "knuckle": 3}

# Modifier combo as parse_entries reports it -> filter label.
COMBOS = [
    ("plain", "plain"),
    ("Control", "Ctrl (Pad)"),
    ("Shift", "Shift (Down)"),
    ("Alt", "Alt (Knuckle)"),
    ("Control+Shift", "Ctrl+Shift (Pad+Down)"),
    ("Alt+Control", "Ctrl+Alt (Pad+Knuckle)"),
    ("Alt+Shift", "Shift+Alt (Down+Knuckle)"),
    ("Alt+Control+Shift", "Ctrl+Shift+Alt (Pad+Down+Knuckle, banished)"),
]

KEY_LABELS = {
    "Minus": "-", "Equals": "=", "Backspace": "Backspace", "BracketOpen": "[",
    "BracketClose": "]", "BackSlash": "\\", "SemiColon": ";", "Apostrophe": "'",
    "Comma": ",", "Period": ".", "Slash": "/", "Grave": "`",
    "LeftMouseButton": "Left mouse", "RightMouseButton": "Right mouse",
    "ForwardMouseButton": "Forward mouse", "BackMouseButton": "Back mouse",
}


def zone_of(finger, pos):
    """Speed zone of a Svalboard position: 1 easiest, 3 hardest."""
    if finger == "thumb":
        return THUMB_ZONES[pos]
    if pos in ("centre", "south"):
        return 1
    if pos == "outward":
        return 3
    if pos == "north" and finger == "pinky":
        return 3
    return 2


def build_layout():
    """The 50 Svalboard slots, in draw order, with role, zone and TheCore key."""
    keyof = {(h, f, p): k for k, (h, f, p) in SVALBOARD.items()}
    hands = []
    for hand in ("L", "R"):
        fingers = FINGERS[::-1] if hand == "L" else FINGERS
        clusters = []
        for finger in list(fingers) + ["thumb"]:
            positions = THUMB_POSITIONS if finger == "thumb" else POSITIONS
            slots = []
            for pos in positions:
                slots.append({
                    "id": "%s-%s-%s" % (hand, finger, pos),
                    "pos": pos,
                    "role": ROLES[(hand, finger)][pos],
                    "zone": zone_of(finger, pos),
                    "key": keyof.get((hand, finger, pos)),
                })
            clusters.append({"finger": finger, "slots": slots})
        hands.append({"hand": hand, "clusters": clusters})
    return hands


def build_file(path):
    idx = {f: i for i, f in enumerate(FACTIONS)}
    entries, unplaced = [], {}
    for cmd, key, combo, raw in parse_entries(path):
        ability, unit = (cmd.split("/", 1) + [None])[:2] if "/" in cmd else (cmd, None)
        facs = factions_for(unit)
        entries.append([ability, unit or "", [idx[f] for f in facs], key, combo, raw])
        if key not in SVALBOARD:
            unplaced[key] = unplaced.get(key, 0) + 1
    return entries, unplaced


def main():
    layout = build_layout()
    data = {
        "factions": FACTIONS, "melee": MELEE, "commanders": COMMANDERS,
        "combos": COMBOS, "labels": KEY_LABELS, "layout": layout,
        "sval": {k: list(v) for k, v in SVALBOARD.items()},
        "files": {}, "order": [],
    }
    for name, rel in FILES:
        entries, unplaced = build_file(os.path.join(HERE, rel))
        names = sorted(unplaced)
        data["files"][name] = {"source": os.path.basename(rel), "entries": entries,
                               "unplaced": names}
        data["order"].append(name)
        print("%s: %d entries, %d unplaced keys: %s"
              % (name, len(entries), len(names),
                 ", ".join("%s (%d)" % (k, unplaced[k]) for k in names) or "none"),
              file=sys.stderr)
        if rel.endswith("TheCore_5.0_Right_Plus.SC2Hotkeys") and set(names) != EXPECTED_UNPLACED_50:
            raise SystemExit(
                "unplaced keys for 5.0 are %s, expected %s: the SVALBOARD mapping is stale"
                % (sorted(names), sorted(EXPECTED_UNPLACED_50)))
    html = TEMPLATE.replace("__DATA__", json.dumps(data, separators=(",", ":")))
    out = os.path.join(HERE, OUT)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote %s (%.0f KB)" % (OUT, os.path.getsize(out) / 1024.0), file=sys.stderr)


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>TheCore on a Svalboard: first-attempt key map</title>
<style>
:root { --pinky:#e8d5f0; --ring:#d6e4f7; --middle:#d9f0d9; --index:#fbe6cf; --thumb:#f7d7d7;
        --z1:#dcf0da; --z2:#fbeacd; --z3:#f8d9d9; }
* { box-sizing: border-box; }
body { margin: 0; padding: 16px 20px 40px; font: 14px/1.4 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1a1a1a; }
h1 { font-size: 20px; margin: 0 0 4px; }
p.lede { margin: 0 0 14px; color: #555; max-width: 90ch; }
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
.hands { display: flex; gap: 46px; flex-wrap: wrap; align-items: flex-start; }
.hand { display: flex; flex-direction: column; gap: 10px; }
.hand > .ttl { font-size: 13px; text-transform: uppercase; letter-spacing: .06em; color: #666; }
.fingers { display: flex; gap: 10px; }
.thumbrow { display: flex; }
.thumbrow.right-end { justify-content: flex-end; }
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
<h1>TheCore on a Svalboard: first-attempt key map</h1>
<p class="lede">A derived mapping, not an official layout: each key of TheCore's one-hand core is assigned to a Svalboard
key well by the reasoning in <a href="../wiki/thecore-method-on-a-svalboard.md">wiki/thecore-method-on-a-svalboard.md</a>
section 4d, and every binding in the hotkey file is shown on the Svalboard key that would press it. Commander views
include all melee units of the commander's race plus the commander's own units, as on
<a href="keymap.html">keymap.html</a>. The drawing is schematic: real key wells are cupped clusters, not flat squares.
Click a key for its full binding list.</p>

<div class="bar">
  <div class="row"><b>File</b><select id="file"></select><span id="src" style="color:#777;font-size:12px"></span></div>
  <div class="row"><b>Melee</b><span id="fac-melee"></span></div>
  <div class="row"><b>Co-op</b><span id="fac-coop"></span></div>
  <div class="row"><b>Other</b><span id="fac-other"></span></div>
  <div class="row"><b>Modifier</b><span id="mods"></span></div>
  <div class="row"><b>Search</b><input type="text" id="q" placeholder="ability or unit name"><span id="stat" style="color:#555"></span></div>
</div>
<div class="legend" id="legend"></div>
<div class="hands" id="hands"></div>
<h2 id="unplacedh">Unplaced TheCore keys</h2>
<div id="unplaced"></div>
<h2>Mapping reference</h2>
<table class="map" id="maptable"></table>
<div id="panel"><button class="t" id="close">close</button><div id="pbody"></div></div>

<script>
var DATA = __DATA__;
var FAC = DATA.factions, GI = FAC.indexOf("Global"), UI = FAC.indexOf("Unclassified");
var HAND_NAME = { L: "Left hand", R: "Right hand" };
var ZONE_NAME = { 1: "zone 1 (easiest)", 2: "zone 2", 3: "zone 3 (hardest)" };

var state = { file: DATA.order[0], faction: "Terran", mod: "any", q: "" };

function words(s) {
  return s.replace(/_/g, " ").replace(/([a-z0-9])([A-Z])/g, "$1 $2")
          .replace(/([A-Z]+)([A-Z][a-z])/g, "$1 $2").trim();
}
function label(k) { return DATA.labels[k] || k; }
function esc(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
function modLabel(c) {
  for (var i = 0; i < DATA.combos.length; i++) if (DATA.combos[i][0] === c) return DATA.combos[i][1];
  return c;
}

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

function keyCell(slot, list, extra) {
  var n = list ? list.length : 0, k = slot.key;
  if (!k) {
    return '<div class="slot"><div class="key none z' + slot.zone + '">' +
           '<div class="kn"><span>' + esc(slot.pos) + "</span></div>" +
           '<div class="role">' + esc(slot.role) + "</div>" +
           '<div class="src">unmapped</div></div></div>';
  }
  var h = '<div class="slot"><div class="key z' + slot.zone + (n ? "" : " dim") + '" data-k="' + esc(k) +
          '" title="' + esc(k + " · " + slot.id + " · " + ZONE_NAME[slot.zone]) + '">';
  h += '<div class="kn"><span>' + esc(extra || slot.pos) + '</span><span class="c">' + n + "</span></div>";
  h += '<div class="role">' + esc(slot.role) + "</div>";
  h += '<div class="src">← ' + esc(label(k)) + "</div>";
  var sorted = sortEntries(list || []);
  sorted.slice(0, 5).forEach(function (e) {
    h += '<div class="e" title="' + esc(e[5]) + '">' + esc(words(e[0])) +
         (e[1] ? ' <u>· ' + esc(words(e[1])) + "</u>" : "") + "</div>";
  });
  if (sorted.length > 5) h += '<div class="more">+' + (sorted.length - 5) + " more</div>";
  return h + "</div></div>";
}

// Grid order for a cluster, as a plus: north on top, then the side row, then south.
function clusterCells(hand, finger, slots) {
  var by = {};
  slots.forEach(function (s) { by[s.pos] = s; });
  if (finger === "thumb") {
    var mid = hand === "L" ? ["nail", "down", "pad"] : ["pad", "down", "nail"];
    return [null, by.up, null, by[mid[0]], by[mid[1]], by[mid[2]], null, by.knuckle, null];
  }
  var side = hand === "L" ? ["outward", "inward"] : ["inward", "outward"];
  return [null, by.north, null, by[side[0]], by.centre, by[side[1]], null, by.south, null];
}

function renderHands(m) {
  var html = "";
  DATA.layout.forEach(function (hd) {
    html += '<div class="hand"><div class="ttl">' + HAND_NAME[hd.hand] + "</div>";
    var thumb = null, fingers = "";
    hd.clusters.forEach(function (cl) {
      var cells = clusterCells(hd.hand, cl.finger, cl.slots);
      var g = '<div class="cluster"><div class="cl cl-' + cl.finger + '">' + cl.finger + "</div>";
      g += '<div class="grid">';
      cells.forEach(function (s) {
        g += s ? keyCell(s, s.key ? m[s.key] : null) : '<div class="slot blank"></div>';
      });
      g += "</div></div>";
      if (cl.finger === "thumb") thumb = g; else fingers += g;
    });
    html += '<div class="fingers">' + fingers + "</div>";
    html += '<div class="thumbrow' + (hd.hand === "L" ? " right-end" : "") + '">' + thumb + "</div>";
    html += "</div>";
  });
  return html;
}

function render() {
  var m = byKey(true), all = DATA.files[state.file].entries;
  var shown = 0;
  Object.keys(m).forEach(function (k) { shown += m[k].length; });
  document.getElementById("stat").textContent = shown + " of " + all.length + " bindings";
  document.getElementById("src").textContent = DATA.files[state.file].source;
  document.getElementById("hands").innerHTML = renderHands(m);
  var up = DATA.files[state.file].unplaced, uh = "";
  up.forEach(function (k) {
    uh += keyCell({ id: k, pos: label(k), role: "no Svalboard key", zone: 3, key: k }, m[k], label(k));
  });
  document.getElementById("unplaced").innerHTML = uh || "<p>None.</p>";
  document.getElementById("unplacedh").style.display = up.length ? "" : "none";
  Array.prototype.forEach.call(document.querySelectorAll(".key"), function (el) {
    var k = el.getAttribute("data-k");
    if (k) el.onclick = function () { openKey(k); };
  });
  Array.prototype.forEach.call(document.querySelectorAll("button.t[data-f]"), function (b) {
    b.className = "t" + (b.getAttribute("data-f") === state.faction ? " on" : "");
  });
  Array.prototype.forEach.call(document.querySelectorAll("button.t[data-m]"), function (b) {
    b.className = "t" + (b.getAttribute("data-m") === state.mod ? " on" : "");
  });
}

function where(k) {
  var s = DATA.sval[k];
  return s ? HAND_NAME[s[0]] + " · " + s[1] + " · " + s[2] : "unplaced";
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
  return '<button class="t" data-f="' + name + '">' + name + "</button>";
}
function init() {
  var sel = document.getElementById("file");
  sel.innerHTML = DATA.order.map(function (n) { return "<option>" + n + "</option>"; }).join("");
  sel.onchange = function () { state.file = sel.value; render(); };
  var counts = {};
  DATA.order.forEach(function (n) {
    DATA.files[n].entries.forEach(function (e) { e[2].forEach(function (i) { counts[i] = 1; }); });
  });
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
  document.getElementById("q").oninput = function (ev) { state.q = ev.target.value; render(); };
  document.getElementById("legend").innerHTML =
    "<span class=\"z1\">zone 1 &mdash; easiest</span><span class=\"z2\">zone 2</span>" +
    "<span class=\"z3\">zone 3 &mdash; hardest</span>";
  var rows = "<tr><th>Svalboard key</th><th>Role</th><th>TheCore key</th></tr>";
  DATA.layout.forEach(function (hd) {
    hd.clusters.forEach(function (cl) {
      cl.slots.forEach(function (s) {
        rows += "<tr><td>" + esc(HAND_NAME[hd.hand] + " " + cl.finger + " " + s.pos) + "</td><td>" +
                esc(s.role) + "</td><td>" + (s.key ? esc(label(s.key)) : "&mdash;") + "</td></tr>";
      });
    });
  });
  document.getElementById("maptable").innerHTML = rows;
  render();
}
init();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
