---
type: Reference
title: Printing
description: Self-print material, printer, dimensional-accuracy, bed/slicer, glue and tooling recommendations.
tags: [svalboard, discord, printing]
source: "discord #general 1124364902811844739, 2025-10-17..2026-08-15"
---

# Printing

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-1124364902811844739.jsonl`; agreement counts are floor estimates.

- **PLA is the standing self-print recommendation** — cleanest prints ("Bambu Matte especially"; matte
  "hides all types of crime") and keys/palm rests are thermoformable. PLA and ABS are officially
  supported, PETG works for some, factory boards are ABS now for heat stability (740672, 037623,
  228605, 532093).
- **Do not print trackball holders in PETG** — they flex enough that the ball skips; "printing in PLA
  was 90% of the fix," and claussen prints holders with **six walls**, not four (165649, 689704,
  833664).
- **Budget under 1 kg of filament for both halves** with no reprints — bases are ~70% of the print, so
  there's slack to redo keys and clusters; multi-color costs ~12x in purge, and **parts are sliced for a
  0.4 mm nozzle** (665494, 591820, 847933, 942809).
- **Use dark filament** — IR opacity is "always an opacity issue," nothing is opaque enough except
  claussen's black filaments; the silver-sharpie trick still applies, and a silver **edding 780** did it
  in one coat (376295, 345980, 527564).
- **Printer picks, as they evolved**: the **Bambu P1S** is the house standard throughout and everything
  is tuned for "Bambu X1/P1/P2 architecture"; a used P1S is the value pick ($350 sightings, ~€400 new
  without AMS). The A1 works, the **A1 mini** needs the case split at a seam, a well-calibrated **Ender 3
  Pro** with a 0.4 nozzle reportedly works, the **X2D** (2026-04-14) is nice-but-overkill, and AMS isn't
  worth it on a first printer (328124, 793783, 139983, 093888, 635993).
- **Dimensional accuracy is the whole game.** Elephant foot on key faces causes stuck keys — lower the
  first layer or use the compensation setting; filing won't rescue an over-extruded cluster, and "if
  magnets press-fit properly, your dimensions aren't actually true to the STEP" (866237, 852148,
  198046, 208754).
- **Bed and slicer**: Bambu Cool Plate at **65 °C first layer / 60 °C after** with no glue; Orca's
  "partially bridged counterbore holes" modifier is what the baseplate bridges want; **Bambu "Support
  for PLA" is garbage**, it fuses and rips the outer layer off — PETG is a better PLA support interface
  (965546, 489366, 143685, 712628).
- **Glue and magnets**: thicker CA "helps a LOT"; a 3–4 g tube covers ~four boards of keys and clusters;
  magnets go **flush and are never heated**; wrong-side magnet → reprint or chip the glue off, and
  **never acetone near ABS** (acetone smoothing "is not a thing" here) (633866, 560020, 001151, 852225).
- **Tools beyond the printer**: soldering iron for heat-set inserts, CA glue, **parallel pliers — buy
  Knipex** (AliExpress ones had 7 mm jaws vs Knipex's 5 mm and wouldn't fit the clusters), and a
  sacrificial screwdriver bit or spudger to pop keys. **Time budget**: ~a week, 10–20 h of prep plus
  assembly; 2–3 days as a printing novice with reprints; ~80 hours from scratch (152192, 993013,
  931235, 354132, 817).
- **Chamber heater strongly recommended for ABS/ASA** large parts, and **test-print the sample cluster
  first** — its STEP/STL is public in the pins (`!sample`), though you can't fully validate without
  magnets (001300, 002942, 417102, 117018).
- **Thermoform rather than re-CAD**: dip the key top in boiled water, print palm rests in PLA and roll
  the corner down, heat gun for ABS. **Cyrus dissents** — not required, and needing it usually means
  fitment is wrong (037623, 684576, 053607).
