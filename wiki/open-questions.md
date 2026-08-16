---
type: Reference
title: Open questions
description: Contested or unresolved topics — wireless, BTUs versus statics, armrests, layout resets, wake-from-sleep.
tags: [svalboard, discord, open-questions]
source: "discord #general 1124364902811844739, 2025-10-17..2026-08-15"
---

# Open questions

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-1124364902811844739.jsonl`; agreement counts are floor estimates.

- **Wireless** — the most-repeated request of all ten months, with no first-party answer: "Bluetooth
  hell," optical-sensor power draw (the firmware polls 24/7 with no sleep mode), batteries complicating
  support, ~100 hrs of work, and claussen's own ZMK Corne was "miserable… pairing difficulties were never
  ending." What works: a Handheld Scientific **BT600** plus a battery bank, or **SterlingKey Hawk** over
  2.4 GHz — trackballs lag badly over plain Bluetooth (929340, 211439, 367157, 243827, 752020).
- **BTUs vs static bearings** — unresolved throughout: low static friction and smoothness (claussen and
  phreaker both daily-drive BTUs) vs noise ("with three, it's horrible"), graininess and skipping. Framed
  at the end as a wear tradeoff — "BTUs are wear items, much more so than statics" (phreaker) vs "statics
  make the ball a wear item" (claussen) (149142, 879697, 548242, 182447).
- **Armrests, trays and mounts.** Cyrus: no armrests at all, the mount takes the full weight of your
  arms, resting elbows "will almost instantly give you cubital tunnel issues," and "keyboard trays suck.
  Unless you have no legs." claussen answers "Tray." Chair vs desk mount splits the same way — claussen
  spent a week chair mounting without finding a position (826668, 414589, 778351, 022761).
- **Trackball-as-SpaceMouse / 6-DOF from the second ball** — raised at least four times and shot down
  each time (a running joke by mid-2026): claussen built it, "not worth the extra complexity, bulk and
  cost"; phreaker wrote the firmware and "it really doesn't work well with the sval." A dual-sensor
  twist-to-scroll ball failed the same way (448128, 789649, 238339, 150474).
- **Traditional switches in a cluster**: none is small enough, and mechanical switches would need
  injurious splay, force and travel (797349). **Multi-stage keys** died because magnetic force drops as
  you press, making a 50–60 g tact hard *not* to actuate (526079, 883890).
- **Touch-to-enter-mouse-layer** (metal/charged ball, capacitive sensing) keeps being tinkered with;
  claussen doubts touch is a good signal and phreaker says layer-15 binding already solves it (932,
  845154, 199725).
- **Should scrolling activate the mouse layer, and can the mouse be disabled per layer for gaming?**
  Wanted by several, still unsupported; workarounds are removing the ball or disabling auto-mouse, and
  everyone agrees such toggles belong on a config page — Cyrus estimates ~70% of support requests are
  accidental setting changes (920074, 1094, 358624).
- **Random layout resets to the flashed default** — reuven, Ben Vallack and Lilijoy all saw it, always
  after a power cycle, with no explanation from claussen or phreaker ("cosmic ray?"); export your `.vil`
  (777030, 294090, 364567, 216251).
- **Sval doesn't reliably wake a sleeping Mac or Windows box** — trackball motion never wakes it,
  keypresses sometimes do after 4–20 s; open and undiagnosed as of February 2026 (041297, 533592,
  990695).
- **Repo file sharing** (community reading, not a ruling): sharing files with the friend who prints for
  you is fine, a side business printing Sval parts is not, and access is permanent unless you transfer
  the board (540490, 095656, 836477).
- **Price vs the Azeron Cyborg II** (~4×): defended on scale, modularity, custom optical/magnetic
  switches (1 PCB per side vs 6) and lifetime support; claussen's one-word answer was "Value" (096937,
  208121, 523442).
- **Odds and ends**: keymap-tampering lockdown doesn't survive contact with rawHID (761242); Bambu vs
  Prusa is a genuine split — Bambu "respects my time immensely" vs a Core One printing so well magnets
  don't need glue (483359, 673919); roller-bearing trackball mods were tried and dropped (833, 919285);
  Apple Touch ID is impossible (894423); there is no layer-indicator desktop app, only drpngx's thockflow
  (923196, 136922); and phreaker argues tutorials imply a maturity the product lacks (234493).
