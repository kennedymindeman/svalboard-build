---
type: Reference
title: Printing
description: Self-print material, printer and build-volume choices, dimensional accuracy, IR opacity, slicer/plate settings, magnets, glue and tooling, and how the advice changed from 2023 to 2026.
tags: [svalboard, discord, printing]
source: "discord #general 1124364902811844739, 2023-06-30..2026-08-15 (gap 2025-08-10..2025-10-17)"
---

# Printing

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-1124364902811844739.jsonl`; a few 6-digit suffixes collide in the 43k-message export, so disambiguate by date if a lookup returns two hits. Agreement counts are floor estimates.

## Material

- **PLA is the standing self-print recommendation** and has been since 2023 — cleanest prints
  ("Bambu Matte especially"; matte "hides all types of crime"), and keys/palm rests are
  thermoformable. PLA and ABS are officially supported, PETG works for some, factory boards are ABS
  now for heat stability (740672, 037623, 228605, 532093). claussen's 2024 material poll landed the
  same way: PLA is "really tough to beat" for stiffness and FDM resolving power, PETG "too soft IMO",
  ASA "similar to ABS but less good", nylon "a hygro nightmare" (462026, 469967, 346304, 850525). Its
  one real weakness is the ~55 °C glass transition — no hot cars, no direct sun (348487, 794459); the
  oldest PLA key of this design is ~5 years old and still in use (455063).
- **ABS/ASA are the heat answer, at the cost of ventilation.** ABS prints at 0.15 mm layers to PLA's
  0.12, is glossier, and survives a summer car (622040, 323969); ASA is "kinda just ABS but better,
  but also twice the price" (886651) and "not much safer than ABS", styrene being the problem
  (709479). Run either only in uninhabited space and vent outdoors — "anything you don't want to
  breathe should be vented outdoors" (764026, 570392). An A1 mini can't do ABS at all (545056).
  **PLA parts mix freely into an ABS build**, "Zero issue" (400824).
- **PETG: fine for a self-build, never for a prebuilt.** "It's too flexible IMO for long term
  customer support and it hates CA glue… Repeated microflex in keys will crack magnets out" (086428,
  104128), and PETG keys shed magnets more than PLA (313088). It is dramatically quieter, "eerie"
  (974833, 711755) — but Bambu **PETG-HF**, the less fiddly print, is "much more PLA like than PETG
  like" and loses the quiet (969631, 266607).
- **Do not print trackball holders in PETG** — they flex enough that the ball skips and can bottom
  out; "printing in PLA was 90% of the fix," and claussen prints holders with **six walls**, not four
  (165649, 689704, 833664). Standing exception since 2025-02: "(Except that you STILL can't print
  holders out of it. Grr.)" (979591, 649598). See [pointing-devices](/pointing-devices.md).
- **No resin/SLA, no structural TPU, no filled filament against skin.** Resin keys "will shatter if
  an assembled cluster is dropped from waist height onto a wood floor" and aren't safe for prolonged
  skin contact (905535, 324473). TPU flexes too much for anything with glued-in magnets (402257,
  315392); it belongs in palm rests (5% gyroid infill, not 15% — 266066) and 10 mm trackpoint nubs
  (064498), where **Bambu TPU 95A HF beats NinjaTek Cheetah 95A**, 12+ mm³/s vs 3.6 (989056).
  CF/GF-filled filament in keys "will feel hideous to rest your fingers on" (293372).
- **Filament moisture shows up as stringing, and warm air is what makes it bite.** claussen,
  2023-09: "PLA really takes on moisture fast when it's warm and humid", while "interestingly cold
  and humid has very low impact" (000474, 403698). His first two questions for a stringy print are
  layer height and whether the spool is fresh out of the dryer; one builder's stringing cleared
  simply by swapping to a drier (if older) spool (364028, 767018, 213652, 227098). **Silk is the
  worst offender** — "Silk definitely strings way worse, it has crazy high surface tension, look how
  it shrinks up when oozing"; a temperature tower finds a given silk's window, and most slicers now
  generate one without gcode fiddling (047185, 461183, 041819).

## Printer and build volume

- **Printer picks, as they evolved**: the **Bambu P1S** is the house standard throughout and
  everything is tuned for "Bambu X1/P1/P2 architecture"; a used P1S is the value pick ($350
  sightings, ~€400 new without AMS). The A1 works, the **A1 mini** needs the case split at a seam, a
  well-calibrated **Ender 3 Pro** with a 0.4 nozzle reportedly works, the **X2D** (2026-04-14) is
  nice-but-overkill, and AMS isn't worth it on a first printer (328124, 793783, 139983, 093888,
  635993). Production has run on an all-X1C fleet since 2024 (583764, 802711); the rule of thumb is
  "if you have any Bambu or Prusa printer Mk3 or more recent, it's not that difficult to get it
  right" (272081). Ender 3 builds get finished but need "a significant amount of post work on the
  keys" (333235, 722342).
- **Build volume: everything except the case and baseplate fits a 180 mm bed.** The baseplate is
  200 mm long (316837, 205978); the original target was the MK3S's ~250 × 210 × 210 mm bed (060865).
  **A1 mini owners use the repo's split case and baseplate**, contributed by self-builders (392040,
  548732); claussen: "I don't support it, but it works if that's what you're working with" (813713).
  Tilting the case to fit instead took one build from 70 g to 200 g of supports over ~9 h (021568).
  Don't shorten the rear of the baseplate — it is tip prevention (085516).
- **Do not order the parts from a third-party print service**: "No one will guarantee the tolerances"
  (972808, 985918, 835631). A friend's or library's printer works only if you'll tune it together
  (392553).
- **Ambient heat can beat the extruder, and the fix is airflow plus current, not settings** (2023-08,
  MK3S era): claussen chased bad key prints to "my barely warm garage is just a bit too warm, and my
  stepper torque on my MK3S's can't quite keep up with the heat creep. A big box fan and an increased
  current startup gcode seems to have resolved the issue" (481150).

## Dimensional accuracy

- **Dimensional accuracy is the whole game.** Elephant foot on key faces causes stuck keys — lower
  the first layer or use the compensation setting; filing won't rescue an over-extruded cluster, and
  "if magnets press-fit properly, your dimensions aren't actually true to the STEP" (852148,
  198046, 208754). The number to hit is **±0.05 mm on critical dimensions** — "We're talking about
  20ths of a millimeter" (073896, 142420). Calibrate first with cubes, temperature and retraction
  towers (426017, 590430); elephant foot has been the cluster failure mode since 2023, stiffening key
  insertion and shortening travel (120400).
- **Magnet holes printing too tight — the checklist**: disable detect-thin-walls (Arachne→Classic in
  PrusaSlicer), calibrate pressure advance and e-steps before touching flow, and accept that "hole
  sizes will not print nominal" (325572, 921407, 188480); claussen's blunt version is to try a
  cluster with extrusion turned down a bit (151130).
- **Wavy build-up on flat tops after a few layers is over-extrusion**, not adhesion — drop the
  extrusion multiplier to 0.95 (725643). **Gouging near the end of a big flat part is corner lift**;
  add a 5 mm brim to prove it, since 0.02 mm of liftoff is enough (119623).
- **Print orientations are not yours to change**: "Everything in the design is the way it is for a
  reason, especially print orientations" (831157). Don't raft the keys either — "the backs will be
  all janky" — fix bed adhesion instead (505350).
- **Test-print the sample cluster first** — its STEP/STL is public in the pins (`!sample`), though
  you can't fully validate without magnets (417102, 117018). Expect iteration: phreaker printed 3-4
  sets of clusters on his first build, and there is no fallback SKU for printed parts (251658,
  632623).
- **Tolerances are per-filament, not better-or-worse** (2023-08): "it's not so much that the
  tolerances are worse, just different per filament", with "Prusa is definitely sharpest, they
  produce the tightest tolerance on diameter. But I've made everything work" (229818, 994852). A
  sparkle PLA "prints just a bit tighter than the other filaments so a couple of the center key
  sliders are out of tolerance" (582467). myxfit caught eSun changing factories from a ~3% density
  jump, 1.24 → 1.28 g/cm³, because part of his QA was weighing every part (844810, 132846).
- **A sticking key has three causes, checked in order: debris in the keywell, a rough back bottom
  edge, or a key a hair too wide.** "Check the back bottom edge first, and sand it just a tiny bit at
  45 degrees (don't shorten the key by sanding the bottom flat!) to remove any over-extruded first
  layer material"; if that doesn't do it, "very gently sand one side of the key, check, then the
  other" (654814, 380872, 408326). Separately, "FDM keys with inward slopes can be a little snaggy,
  you may want to sand them" (789487).

## IR opacity

- **Use dark filament** — IR opacity is "always an opacity issue," nothing is opaque enough except
  claussen's black filaments; the silver-sharpie trick still applies, and a silver **edding 780** did
  it in one coat (376295, 345980, 527564). It is the most repeated fix in the archive — "Almost no
  common filaments are opaque enough to infrared" (262474) — and explains phantom held keys and keys
  that fire the wrong code (276540, 936465).
- **Why the flag is L-shaped**: the vertical tab does the interrupting; the horizontal leg is there
  "mostly [for] rigidity — no way that 0.6 nominal feature would survive without some add'l stiffness",
  with blocking light from above in extreme ambient IR as the secondary reason (308446, 698523, 369111).
- **Silver Sharpie beats black, on the key's L-shaped flag**: silver is "usually one and done"
  against 2-3 passes for black (164554, 399308, 944981, 826705); paint pens are "gunky, can clog opto
  slot" (637001). 3+ agree.
- **Few materials need no coating**: eSun black, Prusa black and Prusament Galaxy black are what
  claussen has qualified (639296), plus Polymaker Cold White PLA Pro (799444). Silks are
  IR-transparent even in dark colours, and every Galaxy colour *except* black is "extremely
  transparent" (332715, 681903).
- **Clusters are where opacity matters; case and baseplate colour genuinely does not** (524497,
  509196). Transparent cases work because "the slot optos have their own shielding, as long as the
  flag is opaque", but finger clusters need paint or AMS'd black to shield the centre-key sensors
  (880420); a third fix is inking the tops of the centre IR parts on the PCB (052222). Sensor LEDs
  are IR at **940 nm, 10 mA** (810170).
- **A key that reads permanently pressed is usually a print defect, not electronics**: the 'L' flag
  tab sits too high from bridging in the key well; file a slight bevel off the front lower edge so
  flags sit approximately flush with the cluster top (819856, 336679). Diagnose with the firmware's
  matrix tester — Vial's in 2024 (754739); see [firmware-and-config](/firmware-and-config.md) for
  current tooling.

## Slicer, plate and supports

- **Bed and slicer**: Bambu Cool Plate at **65 °C first layer / 60 °C after** with no glue; Orca's
  "partially bridged counterbore holes" modifier is what the baseplate bridges want; **Bambu "Support
  for PLA" is garbage**, it fuses and rips the outer layer off — PETG is a better PLA support
  interface (965546, 489366, 143685, 712628). claussen and phreaker both moved to Orca over
  2024-12/2025-01, and the shipped 3MFs error in PrusaSlicer 2.9.0 (482589, 249317). **Use the repo's
  supplied 3mf/Orca profiles rather than porting settings by hand** (897546); otherwise leave
  settings stock (032768).
- **Layer heights and infill**: 0.4 mm nozzle, case at 0.2-0.3 mm, keys at 0.1 mm, ~15% infill, add a
  brim (537407). claussen prints PLA keys at 0.12 and ABS at 0.15; 0.08 is both too slow and too
  finicky except in PLA (075132). Print centre keys on their sides — "it feels so much smoother"
  (246549) — and keys two at a time with cooling cranked, or you melt the flags (230510).
- **Plate choice: smooth or engineering for sliders, never full textured** (762142) — Fabreeko
  **Honey Badger** semi-satin is claussen's pick (362758, 254972). By 2025 this softened to a looks
  question, textured hiding layer lines (674250, 472576). **Clean the plate with dish detergent, not
  alcohol**, which "tends to smear oil around" (904306).
- **Supports: manual/painted, not automatic, on the tipping centre keys** — auto ignores your paint
  and fills the magnet holes and light passages (339049); mode keys need supports, not rafts
  (127538). Palm rests print on their sides with tree supports and a light brim, and want
  PrusaSlicer's **"avoid curled overhangs"** on (805895, 313744); trackball holders want tree
  supports on the overhang (207976). **Stringing is a speed problem first**, and silks want *lower*
  temps, 230 °C on an X1C (679071).
- **2023-era slicing notes, from when the house printer was an MK3S**: PrusaSlicer 2.6's organic
  supports were the headline improvement ("Organic supports are amazing"), with a known bug that
  started laying supports in midair (411347, 826047, 544650). Keys printed at 0.1 mm layers with a
  10 mm inner radius and "roughly 6:1 slope on E/W/S key faces" (543185). A 0.2 mm nozzle was tried
  and rejected — it "quadruples print times", and "changing key orientation would be a bigger benefit
  IMO. Aligned layers with finger movement feel sooo nice" (155537). Wide-fingertip clusters cost
  "like 25% longer to print due to all the supports" (556736), and gk got a cluster down to 15 min on
  klipper at v400 by holding bridges, outer walls and top/bottom layers to 50 mm/s while running the
  rest at 200 mm/s (867496).
- **Get a filament dryer; it counts as basic starting equipment** (683038) — claussen runs a Sunlu
  S4 and says **4A molecular sieve beats silica** (279498, 959976). PLA also needs ambient air: a
  sealed enclosure plus a heated bed invites clogs (279723). pnewb's mechanics, from 2023-09 and
  still true of any heated dryer: **never park a spool over the centre vent** — "the air coming out
  of the heater is significantly hotter than PLA can handle, even at 'low' temps" — throw a
  temperature probe in to check the display against reality, and move dried filament into a sealed
  container to keep it dry (600240, 109146). Cheap two-spool Amazon dryers are what claussen actually
  runs (391130, 746361).

## Magnets, glue and key force

- **Glue and magnets**: thicker CA "helps a LOT"; a 3-4 g tube covers ~four boards of keys and
  clusters; magnets go **flush and are never heated**; wrong-side magnet → reprint or chip the glue
  off, and **never acetone near ABS** (acetone smoothing "is not a thing" here) (633866, 560020,
  001151, 852225). **Every magnet is glued** — press fits hold "at first" but "they WILL come out"
  (958015). Build-guide default is Starbond CA, "Stick with what the build guide says" (493489,
  415680); Cyrus prefers **VA250**, a black rubber-filled CA that stays slightly flexible (206163).
  claussen traced a run of loose magnets to an aged bottle and **set a 3-month shelf life on CA**
  (656475).
- **Excess glue is the number one new-builder fault** — misfiring keys twice traced to "a fine film
  of glue on the surface" (607263) — and **magnet flushness is the make-or-break tolerance**: one
  builder had 5/10 clusters failing from proud magnets (877845). Key magnets are the exception; they
  are *supposed* to sit proud of the well, "Bigger offset, less force" (534500).
- **The magnets are 2 mm dia × 1.5 mm N35 cylinders**, one commodity size for the whole board
  (910656, 511570, 621214); see [suppliers-and-parts](/suppliers-and-parts.md). **Polarity only has
  to be self-consistent**, until you mix in parts from claussen or another builder (112458, 916139).
  claussen's install method: magnet on the *back* of a key, lift it off with a small flat-blade
  screwdriver, dip in medium CA, press home (358147); phreaker prints the "keys" and "clusters"
  magnet-staging jigs (222152).
- **Key force is a print-time choice — magnet offset, not magnet strength.** The number on the back
  of a key is that offset in millimetres and **higher means lighter**, because it reduces magnet-face
  overlap: 0.7 mm ("medium") is stock at roughly 20 g, 0.8 mm the usual "a bit lighter", 1.0 mm
  ("XXlight", ~8 g) standard for N keys (011648, 797265, 885147). ~40 g is reachable on stock N35 at
  ~0.4-0.5 offset — **you do not need N52** (514675, 187080). The leading number in a key filename is
  **key height**; 6 mm is the standard side key (462532, 583036). See
  [ergonomics-and-fit](/ergonomics-and-fit.md).
- **Reprinting is cheap because the hardware comes back out**: magnets, square nuts and heat-set
  inserts are all reusable — soak PLA parts in boiling water until soft, pinch the magnets out with
  pliers, scrape the glue off (673515, 478196, 599450, 818036).

## Tools, time and cost

- **Tools beyond the printer**: soldering iron for heat-set inserts, CA glue, **parallel pliers — buy
  Knipex** (AliExpress ones had 7 mm jaws vs Knipex's 5 mm and wouldn't fit the clusters), and a
  sacrificial screwdriver bit or spudger to pop keys. **Time budget**: ~a week, 10-20 h of prep plus
  assembly; 2-3 days as a printing novice with reprints; ~80 hours from scratch (152192, 993013,
  931235, 354132, 817). Buy the **180 mm** Knipex — wide tips, so you don't crush parts (354399).
  They aren't strictly required: Cyrus does clusters by sticking magnets to a scalpel blade, adding a
  drop of glue and sliding them in (041574, 106142).
- **Heat-set inserts: ~200 °C slow and low in ABS, ~280 °C in PLA; drive to ~90%, then press the face
  flat against a work surface.** A tapered iron tip goes straight through the M3 baseplate inserts,
  so use a proper insert tip (095027, 143120); there is **zero soldering** otherwise (769664). Other
  hardware: palm-rest screws are **T10, M3 × 6 mm × 0.5 mm** (736661); each cluster takes **only 2 M2
  thread-cutting screws, on a diagonal** (700409); you get 9 rubber feet and need the outer 4 corners
  (503898). **Chamber heater strongly recommended for ABS/ASA** large parts (001300, 002942).
- **Budget under 1 kg of filament for both halves** with no reprints — bases are ~70% of the print,
  so there's slack to redo keys and clusters; multi-color costs ~12x in purge, and **parts are sliced
  for a 0.4 mm nozzle** (665494, 591820, 847933, 942809). Measured actuals sit well under that
  headline: beep weighed **410.41 g of PLA for one complete Lightly** (109617, 288448) and claussen
  quoted **~500 g for a pair**, "that's actual parts, not tuning obviously" (981362), ~220 g of it
  the two cases and plates (700126). A roll is under $15 (577698).
- **Print time**: 2-3 days on a P1S (708807), or a bare minimum of 24 h on older machines and
  "probably several times that as you dial things in" (799256); a case + plate is ~4 h at 0.2 mm on
  an X1C (722141, 169173). "The prints are the hard part. Specifically the keys" (017704) — assembly
  is "just tinker toys and glue... WAY less of a PITA than handwiring a dactyl" (294063, 296778).
  The 2023 numbers were the same shape: "the whole rig is like 36hrs I think?", of which the plates
  and cases were "about 16 hrs of print time in total" (266943, 976256).
- **Mass, and where it goes** (2023-07): a finished side weighed **277 g** on claussen's scale — case
  77 g, baseplate with towers and fasteners but no clusters 87 g. "Everything is like 15%-20% infill
  but the case walls are only 2mm to begin with", and the design trend was toward *heavier* for
  rigidity (797744, 182810, 978886). See [ergonomics-and-fit](/ergonomics-and-fit.md) for what that
  weight means for slip-stick mousing.
- **A hot air station beats a flame for cleaning up stringing** — "easier and tidier" (953363).
- **Self-printing is not a money-saver** — "if you value your time at >=$5/hr, you're definitely not
  saving money", though it's "an *excellent* gateway to 3D printing" (540978, 608122). claussen's
  rule: **"if you have pain, just buy a full build. you can tune later"** (313334).

## Finishing and thermoforming

- **Thermoform rather than re-CAD**: dip the key top in boiled water, print palm rests in PLA and
  roll the corner down, heat gun for ABS. **Cyrus dissents** — not required, and needing it usually
  means fitment is wrong (037623, 684576, 053607). A heat gun is "a bit much for PLA — just dip the
  tip to get it soft and pop the ball in, then blow on it to cool" (643302). Rolling the palm rest's
  front lip down buys 5-10 mm of fit range, but parts "won't survive too many cycles given the layer
  orientation" (071616, 625455).
- **Do not chemically smooth the parts.** claussen, flatly: "do not do this" — isopropyl does nothing
  to ABS or PLA, acetone on ABS gave "mostly comical" results, and vapour-smoothing wrecks the
  accuracy of the functional features (421643, 144860). Sanding PLA is "very very slow due to low
  glass temp", and one builder's full-infill-plus-automotive-grit route cost 40-45 min *per keycap*
  and still blew the tolerances (005014, 718038). The house position: **"FDM parts are always going
  to look like FDM parts, and that's okay"** (886033). Ironing works only on dead flats (278132), and
  keys clean up with a little dish soap, gently — the flags are delicate (258607).

## Files and repo

- **Files ship as STEP with some 3mf examples**, so Cura users need PrusaSlicer or Bambu Studio
  (730007, 142762). **Repo access is manual and customers-only** — DM claussen your GitHub handle
  (325333, 717343) — the STLs are not for redistribution (491149), and the kit gets you PCBs, files,
  magnets and FFCs but **not gerbers** (022758). Build guide: svalboard.com/build (638953). **Hold
  off printing until your kit is close to shipping**; files pick up QoL tweaks right up to release
  (330695, 517268).

## History

- **The filament budget drifted upward in the telling, not in reality.** claussen's 2023-07 working
  figure was "prolly 600g-700g" per build, bought as a fresh reel each time (010527); measured builds
  in 2024-05 and 2025-02 came in at 410-500 g (109617, 981362); the later "under 1 kg" headline
  (665494) is a shopping budget with reprint slack, not a parts weight. Keep 1 kg as the number to
  buy.
- **PLA-only is a 2023 decision that never moved much.** "I only use PLA as it has great properties,
  colors, and is low occupational-hazard", and, asked what the alpha units were printed in: "PLA. I
  don't mess with the smelly stuff" (344141, 606272). ABS arrived later as the factory material for
  heat stability, not as a self-print default.
- **Resin/SLA was a live option from 2023-07 to 2024 and is now closed.** In 2023-07 claussen was
  enthusiastic: "SLA keys have a slightly smoother action at least initially", "the resin clusters
  i've used have have been very enjoyable", and he hoped "to be able sell complete SLA keysets with
  magnets pre-installed as a turnkey offering once I get a vendor validated" (020720, 864192). The
  caveats even then were that SLA buys nothing outside the keys, costs you the colours, needs the
  magnet holes resized, won't take heat-set inserts (screw in instead) and can't be thermoformed
  (020720, 037865, 384977, 542871, 830248, 003570). **The drop test that later gets quoted as
  settled fact happened on 2023-09-03**: "One of the SLA keys shattered at the magnet hole on impact
  with the ground from waist height. PLA would never do so -- this was just generic JLC resin…
  Concerned about UV embrittlement over time with resin" (421578). 2023-09: the objection was
  dimensional accuracy for the magnets, and claussen offered parts with reduced magnet holes for SLA
  (191499, 484234); by 2023-11 he was daily-driving an SLA prototype, blocked only on finding "a
  supplier who can actually deliver volume and quality" (300392). 2024-08: he printed full SLA
  clusters that "work beautifully" but wouldn't sell them, ~6 mm² key cross-sections with big stress
  risers (481724, 421976). By 2025 the objection is durability plus skin-contact safety (905535).
  SLA is also not thermoformable (427795) and can't take heat-set inserts (506058).
- **File versions**: v1.1b (2024-04) swapped heat-sets for alignment holes and slots on the cluster
  mounts (394304); v1.2 was "a strict improvement" in 2024-07 and absorbed the experimental tipping
  clusters and centres in 2024-10 (741568, 348826); by 2024-12 v1.3's extras were back-ported into it
  (518727). Print whatever the repo currently calls latest (335629).
- **Slider naming and force defaults moved repeatedly in 2023-2024.** Sliders were dot-coded — one to
  four dots = 0.4/0.6/0.8/1.0 mm back gap — 0.6 the 2024-01 default, gap sliders facets-N and offset
  sliders facets-S (205507, 702623); claussen's 2024-03 numbers were 0.8 gap ≈ 10 g, 0.6 gap ≈ 20 g,
  1.2 offset ≈ 25-30 g, an offset key installed backwards ≈ 120 g (137034). Production moved to gap
  sliders, and the manual's slider pages went dead once tipping centres landed (825926, 988531).
  Cluster magnets dropped from N52 to N35 in 2023-10, existing N52 owners compensating with
  0.6 → 0.8 mm offset on the finger NSEW keys (253732). Present guidance is the offset numbering
  above.
- **Standard colour has been galaxy/plain black with optional coloured centre keys since 2023-12**
  (158585); qualifying a new material or even a new colour is expensive (559079).
