---
type: Reference
title: Pointing devices
description: Trackball size and sourcing, bearings versus BTUs, trackpad and trackpoint limits, and friction fixes.
tags: [svalboard, discord, trackball]
source: "discord #general 1124364902811844739, 2025-10-17..2026-08-15"
---

# Pointing devices

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-1124364902811844739.jsonl`; agreement counts are floor estimates.

- **44 mm, near-unanimously, for the whole ten months.** claussen: "Go with 44." 52 mm "impacts fit a
  lot," wants a hand over 20 cm wrist-crease-to-fingertip plus custom holders, and static stiction
  scales with ball weight ∝ d³, so a 40 can beat a 44; phreaker went 52 → 44 with 190 mm hands. 34 mm
  (the first Svals) and 38 mm are too small; undershoot and upsize later (751734, 458562, 628269,
  984528, 907701).
- **Ball sourcing**: Sanwa 44 mm on Amazon `B0F1SWBL69` is the build-guide default; standard red balls
  are identical to Sanwa/LZYDD 44 mm, silver is shop-exclusive, and black 44 mm are on the shop while red
  is reserved for full-build production. **Aramith is the only snooker brand worth using**, and **avoid
  pearl, glitter/flake or mixed clear+solid** — variable focal depth breaks tracking. On color, claussen
  first said "silver tracks identically to red" (Oct 2025), then by mid-2026 that silver "tracks better
  than anything on the market," with factory builds tuned per color (551636, 918239, 308205, 681226).
- **Non-standard 44 mm balls often need a shim** (black "definitely want a shim, try 0.6 mm"); no shims
  ship by default, the repo has them. The **sensor-to-ball gap is 1.6–2 mm for red or silver and is
  engraved on the bottom of your holder** — the datasheet spec is *not* what works, because of ball
  curvature and per-color tracking differences; shim rather than heat-bend (050688, 392800, 093300,
  496882).
- **Dual trackball is the default by a wide margin** — "the Meta"; "enough so that if I stopped selling
  the others it would make no difference to me." Convention: scroll on the non-dominant hand, point on
  the dominant, swappable in firmware; dry_serial and dmfay dissent with one (135043, 979468, 296465,
  798003).
- **phreaker's ranking: trackball >>>>>> trackpad >> trackpoint.** Trackpoints drift enough to need a
  "Fix Drift" key; the trackpad's limits are firmware — QMK driver only (tap = click, two-finger tap =
  secondary, two-finger drag = scroll), no haptics, not PTP, capped ~100 Hz, two fingers wide (422937,
  044899, 544044, 400468).
- **BTUs (Bosch Rexroth ball transfer units)**, `R053010810` / `KU-B8-OFK`, 8 mm, six for two hands,
  ~€8–9 in the EU and ~$12–16 each in the US: lower static friction, but noisier, grainier, "a bit harder
  to control," and they skip because a 44 mm ball doesn't load them enough. Sealed assembly — flush with
  lube, don't disassemble (443995, 879565, 736906, 758918).
- **Friction is almost always dirt, not lubrication** — clean the ball *and* wipe the statics, then
  apply fresh face grease; that fixed vin's board instantly after face grease alone failed. No solvents
  but isopropyl, and Renaissance Wax helps less than fit does (309718, 149801, 803402).
- **Pointing devices are field-swappable in ~10 minutes** — unscrew, unplug/replug the FFC, reflash. A
  0.5 mm-pitch female-to-female FFC adapter daisy-chained outside the case, or leaving the rear cover
  off and unplugging at the sensor PCB, is what claussen and phreaker actually do (533962, 174466).
- **Connector map: trackball → `TrkPt`; touchpad → `Azo` (Azoteq)** — not both at once; lift the latch,
  slide in with no force, close it. **Jitter that flips you out of text mode is usually mechanical** —
  the thumb cluster bumping the trackball holder (711323, 712627, 432306).
- **Sourcing and CAD**: the PMW3389 beats the 3360 and the small lens is **LOAE-LSI1**, ~$0.75 from
  AliExpress; trackball CAD lives in the OnShape "All Trackball Holders" doc, not the GitHub repo. Cheap
  BTU experiments: HazardousChurch's printed BTU, printables.com/model/1740316 (751890, 286064, 205198).
