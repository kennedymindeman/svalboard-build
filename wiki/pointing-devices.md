---
type: Reference
title: Pointing devices
description: Trackball size, sourcing and holder tuning, bearings versus BTUs, trackpad and trackpoint limits, friction fixes, and how the recommendations changed from 2023 to 2026.
tags: [svalboard, discord, trackball]
source: "discord #general 1124364902811844739, 2023-06-30..2026-08-15 (gap 2025-08-10..2025-10-17)"
---

# Pointing devices

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-1124364902811844739.jsonl`; a few 6-digit suffixes collide in the 43k-message export, so disambiguate by date if a lookup returns two hits. Agreement counts are floor estimates.

## Which device

- **Dual trackball is the default by a wide margin** — "the Meta"; "enough so that if I stopped selling
  the others it would make no difference to me." Convention: scroll on the non-dominant hand, point on
  the dominant, swappable in firmware; dry_serial and dmfay dissent with one (135043, 979468, 296465,
  798003). The house answer since mid-2024: "At least half of builds going out lately are dual ball or
  point/ball", "Trackball outsells everything else by a huge margin"; people who expect to prefer the pad
  or point tend to order a second ball within a week (673097, 937751, 940341, 448467, 311912).
- **phreaker's ranking: trackball >>>>>> trackpad >> trackpoint.** Trackpoints drift enough to need a
  "Fix Drift" key; the trackpad's limits are firmware — QMK driver only (tap = click, two-finger tap =
  secondary, two-finger drag = scroll), no haptics, not PTP, capped ~100 Hz, two fingers wide (422937,
  044899, 544044, 400468). Same ordering in 2025-03, trackpoint last for injury reasons not taste
  (099162). **One device per hand, two total** (832003).

## Ball size

- **44 mm, near-unanimously, for the whole ten months.** claussen: "Go with 44." 52 mm "impacts fit a
  lot," wants a hand over 20 cm wrist-crease-to-fingertip plus custom holders, and static stiction
  scales with ball weight ∝ d³, so a 40 can beat a 44; phreaker went 52 → 44 with 190 mm hands. 34 mm
  (the first Svals) and 38 mm are too small; undershoot and upsize later (751734, 458562, 628269,
  984528, 907701). Agreed since late 2024 — phreaker at 190 mm middle-fingertip-to-palm "BARELY clear a
  52" (467808) — and 44 is standard partly because it is an easy size to source (201914).
- **Fit beats size; typing is fit priority #1.** claussen: "I discourage people from going big at the
  start so they can explore fit prefs without the ball as part of it" (780924, 313444); after a 57 and a
  52 he went back to stock 44: "Fit is everything" (534927). **You should
  not hit the ball while typing** — a fit problem, not a size problem: curl the fingers more, move the
  ball toward the palm, and roll with the phalange rather than the fingertip (437691, 716036). Placement
  is usually index/middle (627216). See [ergonomics-and-fit](/ergonomics-and-fit.md).
- **Above 44 mm you are on your own.** 50 mm and up need a printed holder or extra height; phreaker
  daily-drove 52 mm (Elecom Huge size) but rejected 55 and warns newcomers off (459230, 229960, 345657).
  55 mm is the largest anyone has made work, huge hands only (577012); 46 mm needs "Godzilla spec hands"
  (883806). **Each printed holder fits exactly one size**, but the CAD is parametric — "I bet if
  you just changed '44' to '46' in the onshape it'll come out just fine"; only the plastic holder
  changes, not the sensor harness (384272, 974697, 755390). **Perceived clearance is holder height, not
  diameter** — shim up rather than downsize; claussen runs a 44 with a 4 mm shim on small-side-of-average
  male hands (613706, 239567, 039228).

## Ball sourcing, colour and material

- **Ball sourcing**: Sanwa 44 mm on Amazon `B0F1SWBL69` is the build-guide default; standard red balls
  are identical to Sanwa/LZYDD 44 mm, silver is shop-exclusive, and black 44 mm are on the shop while red
  is reserved for full-build production. **Aramith is the only snooker brand worth using**, and **avoid
  pearl, glitter/flake or mixed clear+solid** — variable focal depth breaks tracking. On color, claussen
  first said "silver tracks identically to red" (Oct 2025), then by mid-2026 that silver "tracks better
  than anything on the market," with factory builds tuned per color (551636, 918239, 308205, 681226).
  The **shop-exclusive 44 mm bright silver launched 2025-01-22**, and phreaker's verdict then was
  "Sanwa vs. the Silver? Nothing I've noticed" (356392, 020507, 094162).
- **Balls and bearings have never been in the kit**; the add-on is the PCBA and cable only (252966,
  264160, 678658). **Non-red colours mean gutting a cheap trackball mouse** — "nobody does fun colours in
  small quantities": Nulea 44 mm blue/green, PORLEI `B0DHSDTXMX`, or Cursor Controls (UK) 38/50 mm, who
  resist selling singles (684465, 775144, 557117, 328864). **"Don't sacrifice size for color"** (123388).
- **Weight is the hidden spec**: red Sanwa 40 mm = 40.27 g (026384), Nulea 44 mm = 54 g (004575), a
  55 mm = 100+ g (892071). **Steel balls do not work** — ~1 lb at 44 mm, too heavy for BTUs and binding
  on statics, "Unusable, binds up. Statics need light" (403137, 816338, 418717) — nor does anything not
  "super round and super polished" (594521). **Polish only if the ball is marred**, and **not below 1000
  grit** (975016, 991902); balls are consumables, the bearings are not the wear item (665994, 673695).

## Bearings: statics versus BTUs

- **Statics are the answer: 1/8" (3.175 mm) G5 zirconia, four per holder, eight for a dual-ball build,
  sold in packs of 25**; "Grade 10 is noticeably worse"; ~$5-10 for 20 on Amazon (081396, 909002, 959434,
  372518). In Europe search **"ceramic bearing balls"**, not a caged bearing — amazon.de `B0F48M1MN1`
  (zirconia) / `B0F48JGD5K` (silicon nitride); the repo has 3 mm holders when 1/8" is a six-week lead
  time (088139, 375242, 388314).
- **Zirconia over silicon nitride; grade matters less than people think.** phreaker owns both: "ZrO2 is
  the winner on my rig... the Si3N4 gives a more gritty feel" (169300, 964029). claussen was "squarely in
  camp Silicon Nitride" in early 2024 (178704), switched to G5 zirconia by 2024-11, and still dissents on
  the premise: "you're overestimating the role of bearing material in low speed/load operation" (596042,
  572132). Bearings need not even be round, only "a single contact point which is low friction and hard"
  (243813, 304193). **Glue them in with CA and wait 1-2 hours before fitting the ball**
  (072592); **never sand a ceramic bearing** (919014).
- **Cyrus's bearing design-space rules (525972)**, the densest technical post in the backfill: fewer
  bearings means less friction but more clack; the bearings **must enclose more than 180° or the ball
  falls out**; you want the largest possible triangle of bearings under the rest position so the ball
  can't topple; the stock four-bearing config is "an excellent compromise" that works fully inverted.
  Geometry is **75° around the bottom, 150° over the top**, the same in angular terms for a bottom- or
  angle-mounted sensor — "above 75 things degrade quickly" (334079, 396844, 180340).
- **BTUs (Bosch Rexroth ball transfer units)**, `R053010810` / `KU-B8-OFK`, 8 mm, six for two hands,
  ~€8–9 in the EU and ~$12–16 each in the US: lower static friction, but noisier, grainier, "a bit harder
  to control," and they skip because a 44 mm ball doesn't load them enough. Sealed assembly — flush with
  lube, don't disassemble (443995, 879565, 736906, 758918). Longstanding: **three per holder** (052419),
  Bosch Rexroth over uxcell, "worth the premium... lower friction and way lower stiction" (607424), and
  about half the US price in the EU (692594).
- **Nothing about BTUs has ever stuck.** claussen: "BTUs be LOUD" (020328); "ultimately they're just a
  big ball bearing resting on a bunch of tiny ball bearings, which ultimately determine the overall level
  of friction" (547466); "Statics will never be beaten for smooth" (846801). **Smaller BTUs get
  exponentially worse** (805888, 539646), **cheap plastic BTUs are a dead end** (031022), and **BTUs
  break automouse**, because the changing static friction produces accidental movement (170390, 475435).
  A **bottom-BTU hybrid** survives in the repo as branch B2, "Bottom BTU Hack" — +10 mm height, mainly
  viable at 34 mm (032680, 882228). phreaker: "for 90%+ of users, statics are the right answer" (877880,
  456647). And **don't leave the ZrO2 balls unglued to fake a BTU** — the keepers aren't retained against
  static friction (847165, 566036).

## Sensor, gap and holder tuning

- **Non-standard 44 mm balls often need a shim** (black "definitely want a shim, try 0.6 mm"); no shims
  ship by default, the repo has them. The **sensor-to-ball gap is 1.6–2 mm for red or silver and is
  engraved on the bottom of your holder** — the datasheet spec is *not* what works, because of ball
  curvature and per-color tracking differences; shim rather than heat-bend (050688, 392800, 093300,
  496882). The gap has always been the fiddly variable: 2024 holders were cut to the PMW3360's nominal
  2.4 mm (485659), then to a `trackinggap` of 1 mm for 34-44 mm balls and 2 mm for 55 mm (109738, 805977).
- **Why the gap is touchy: the usable focus window is about 0.5 mm.** The 2.4 mm nominal is for a *flat*
  surface, so "We use 2 mm for everything 50 mm and up, and 1mm for 44mm," because curvature shifts the
  focus (671086, 062158); Cyrus, "The distance to the sensor is the most important variable... it has to
  be in focus" (971589). NickeaTea's green Nulea ball only tracked several mm out, fixed by heat-bending
  the holder's PCB mount (342490). Current sensors are PMW3389, far less finicky about gap and ball type
  than the 3360 (931986, 859918, 668830).
- **Setting ball pressure — kantlivelong's recipe** (084816), endorsed by claussen "minus the first two
  steps" (989270): bottom arms into good contact; tighten the top arm until the ball is hard to move;
  **0.3 mm (three sheets of printer paper) between ball and top bearing**; heat and hold until cool. Warm
  the keeper in hot water or with a heat gun, holder off the board (197210, 441809). It is undocumented
  on purpose — "you gotta learn deeply about the process" (959397).
- **The keeper should be a hair off the ball, not touching** — "don't want it in steady contact or it
  gets really draggy" (040266) — and there must be **zero contact between ball and the plastic beneath
  it**; if there is, the holder is bad and gets replaced rather than tuned (463170). **Current holders
  retain the ball fully, even inverted** (418755, 901852), and a **staggered-bearing-height holder**
  shipped as a shop upgrade on 2025-06-08, "really a lot better than the earlier 'all bearings at same
  height' version" (763428).
- **The neutral axis is pitched roughly 45-50° forward and the sensor is not under the ball**, so lateral
  sensitivity is lower than a standalone trackball would suggest and several users find themselves
  *twisting* rather than rolling; removing "~10mm of stack height under the ball made this product
  possible" (954676, 400989).
- **Sourcing and CAD**: the PMW3389 beats the 3360 and the small lens is **LOAE-LSI1**, ~$0.75 from
  AliExpress; trackball CAD lives in the OnShape "All Trackball Holders" doc, not the GitHub repo. Cheap
  BTU experiments: HazardousChurch's printed BTU, printables.com/model/1740316 (751890, 286064, 205198).
  The historical entry point is `svalboard.com/trackball-repo`, public OnShape, free to copy — export
  STEP not STL (944646, 545728, 639390); split holder files to objects in Bambu Studio and each part
  comes out named with its size, also embossed on the bottom face (821295). Rolling your own sensor PCB
  is not worth it — the lens is hard to source alone (449299, 952347). See [printing](/printing.md).

## Mounting and swapping

- **Pointing devices are field-swappable in ~10 minutes** — unscrew, unplug/replug the FFC, reflash. A
  0.5 mm-pitch female-to-female FFC adapter daisy-chained outside the case, or leaving the rear cover
  off and unplugging at the sensor PCB, is what claussen and phreaker actually do (533962, 174466). True
  since the beginning: devices can be **added or changed at any time after purchase** over the same
  8-pin FFC the clusters use — "just screws and a cable" — and changing ball size is a holder reprint
  plus a ball (762516, 093797, 313444). The catch, from 2023-09: that is only true **if you accept a
  position that fits around the current key layout**. Wanting the ball where thumb keys are — Arska
  proposed dropping the pad and up keys of one thumb — means a new thumb-cluster design, not a bolt-on
  (986846, 632781).
- **Connector map: trackball → `TrkPt`; touchpad → `Azo` (Azoteq)** — not both at once; lift the latch,
  slide in with no force, close it. **Jitter that flips you out of text mode is usually mechanical** —
  the thumb cluster bumping the trackball holder (711323, 712627, 432306).
- **The FFC latch is a hinge, not a slider**: nail under the lip on the side away from the cable, flip it
  up 90°, push down to relock. **Contacts down, blue reinforcement up** on almost every component (the
  trackpoint module is the exception), and leave more slack than you think (288937, 845230). The cable is
  **8-pin, 0.5 mm pitch, contacts same side (Type A)** (308913, 451260).
- **Mount holders with adhesive, not slots or brackets** — tape or 3M Dual Lock keeps the position
  adjustable, and claussen ships Dual Lock in the box (478825, 424512). **Ball mounts are fine to roughly
  25-45° of tenting** depending on holder; past that, tweak or hot-water-form it (639390, 909250, 503596).

## Trackpad

- **A custom glass overlay on an Azoteq TPS43 module**, on its own **6-pin FPC** on the latest MCU; you
  can buy a TPS43 PCBA direct from Mouser and supply your own overlay, max ~45 mm (105657, 473970,
  740961). It **does not work with the alpha PCB**, which has no 6-pin connector (200339), and the
  glass-bonded part is EOL at Azoteq (122702), and **the FFC into the pad is touchy** (087838).
- **It enumerates as an ordinary mouse, not a precision touchpad**, so gestures exist only if firmware
  implements them — no three-finger swipe ("The sensor is capable of it but QMK is not"), no smooth
  scroll (blocked on upstream QMK/Vial merges), no OS driver passthrough, weak drag; accuracy is solid
  and two-finger scroll sends both axes (222360, 436107, 825819). Its niche is clicking and scrolling —
  Sc0tTy uses it for click/right-click because "using the keys for clicking gives me the same pain as I
  have with mice" (268658), and it is the one device that two-finger-scrolls without a mode switch
  (953045).
- **Dated**: the pad was pulled from the shop around 2024-12 over a firmware bug in a batch of Azoteq
  modules — symptom **a right click 1.5-2 s after a move** (301642, 913849).

## Trackpoint

- **The module is a Sprintek SK8707-51 force sensor** — 2-axis, senses Z badly, interpreted inside QMK,
  with no distinct Linux device name to hang udev rules on (962418, 405193). It is not a ThinkPad
  trackpoint: the nub is ~12 mm against Lenovo's ~2 mm (976668). **Nub geometry is concave, not convex**,
  radius ~10-12 mm (859604, 235058); run high sensitivity, which reduces torque on the last finger joint
  (310054). It mounts under the middle finger on tape, deliberately (732261, 386365). Both choices were
  made in 2023-08, before the product existed: the case already had a slot for a trackpoint bracket,
  like the ones holding the finger clusters, index/middle was "an easy fit", and claussen's own
  preference was between the middle finger and the palm rest. Concave over nub was reasoned, not inherited — "I hate having to go to the opposite side to
  move in a direction, and I don't like how much force Thinkpad trackpoints take" (616185, 053733,
  018648).
- **Drift is the defining defect and a hardware property of the module.** claussen, 2024-04: "Drift is
  inducible on all trackpoints, but this is exceptionally severe for many, though not all, folks"
  (734639), with at least five users reporting it that window (451536, 994588). Still applicable: **two
  distinct drifts** — "it wobbles like it is drunk" means dirty USB power, a straight-line takeoff
  opposite your last motion is the module's baseline calibration (129700); **try host power first**,
  direct or a powered hub (157022); **removing the nub changes nothing** (918712); Sprintek's
  XY-drift-averaging registers are
  largely unimplemented, confirmed by the vendor (405787). The **"Fix Drift" key is the shipped answer**
  (866492). **Z-tap is deliberately disabled** — "flaky and annoying, and we have mouse keys" (760862).
- **Its surviving edge is proportional scrolling** — claussen ran ball-right, trackpoint-left locked in
  scroll mode for years; Raven System keeps one because "trackpoints can scroll infinitely without needing
  to move your hand" (372584, 029181, 848650). Standing recommendation: **trackpoint only if you already
  like trackpoints** (251605, 557267).

## Dual-pointer setups, scroll and clicking

- **The second ball is a scroll device, not a second cursor** — "Poor man's spacemouse," pan and point at
  once, and better than an encoder, "dramatically nicer because of the fine control" (046498, 597889,
  093653); the two balls combine into **one** mouse (794152). A ~45° mount scrolls both axes at once, and
  **single-axis scroll lock does not exist** (010332, 461504). One ball plus a hold-to-scroll key is a
  real alternative to two (868679, 366056).
- **CPI split: left 200 for scroll, right 800 for pointing**, changed live with the DPI keys or
  momentarily with the Sniper keys, which sit on the mouse layer by default, south keys pinky through
  middle; `svalboard.com/scroll` is the documentation (572084, 583421, 384713, 459892, 283016). See
  [firmware-and-config](/firmware-and-config.md).
- **The ball has no click; clicks come from the auto mouse layer on the opposite hand.** phreaker: "the
  ability for all of the buttons to be on your off hand… is WAY under appreciated" (486292, 088898).
  claussen uses opposite-hand index/middle/ring South and argues same-hand thumb clicking "encourages
  finger/wrist movement... which in my case is a carpal tunnel issue" (638009, 628460); the thumb-key
  minority is real — Cyrus's "pad for left click, nail for right click" suits CAD (808129, 786058).

## Friction, cleaning and lube

- **Friction is almost always dirt, not lubrication** — clean the ball *and* wipe the statics, then
  apply fresh face grease; that fixed vin's board instantly after face grease alone failed. No solvents
  but isopropyl, and Renaissance Wax helps less than fit does (309718, 149801, 803402).
- **Sticky-ball triage, in claussen's order**: clean and lightly lubricate the ball; scrape CA glue and
  grime off the bearing surfaces with a fingernail or knife edge (never sand); then check whether the top
  keeper ball is dragging and, if so, heat-bend the keeper arm with a sheet or two of paper as a gap shim
  (599071, 219466, 433557). Routine cleaning is a microfiber wipe every few days, bearings included
  (034216, 595570).
- **The house lubricant is your own face oil.** "Just some forehead oil goes a long way" (871164);
  phreaker: "side of the nose and forehead... I oil mine every few days" (758794); claussen: "lube the
  ball, clean the bearings. nose oil" (296781) — the first thing to try when a ball stops tracking
  (544956). Counterexample: chorf's forehead oil was tacky and made his ball *stickier*; nose-corner oil
  worked (087221). Alternatives: dimethicone (650371) and **Renaissance Wax**, Eylon's 2024-09 find, a
  microcrystalline wax that hardens on the surface (433554).

## Alternatives people tried

- **No thumb trackballs.** phreaker: "I've never heard a thumbball story not end in tears," and it is
  "one of the few things I've absolutely refused to work on" (155153, 837332); Raven System: "an RSI
  nightmare for many people" (986191, 211776); claussen: "Thumb ball vs svalball is no contest" (071967).
  3+ agree, 0 dissent; a thumb *pad* is not ruled out (297685). **A joystick in
  place of the right thumb cluster is a bad trade** — "you can have a trackpoint and not lose 5 important
  thumb keys" (833914) — and **cheap I2C trackball breakouts (Pimoroni) are not an option**, "hot
  garbage", ~2 DPI against the PMW sensor's 20000 (087562, 397820).
- **Eye tracking and key-driven mouse cursors were the 2023 answers for people who wanted no pointing
  device at all.** On gaze: "Tobii is the only real game in town, but it's not linux friendly" — the
  4C is 60 Hz and Linux-capable but discontinued with a high failure rate, the Tobii 5 is 30 Hz and
  reliable; usable to about a 24" screen, best on a 14-16" laptop panel, poor across multiple monitors,
  and Talon's Tobii 5 integration was called "a life [saver]" (925204, 523052, 560130, 841162). On keys:
  warpd is "pretty damn good", with hint2 one-shot mode the mode people actually use — macOS and Linux
  only, no Windows (569252, 547903).
- **Sticking a whole separate pointing device to the case works better than it sounds.** cryptanon taped
  an orbital trackpad onto his Svalboard in 2023-08 — "quite comfortable to use", with the dead driver
  software, jitter on precise selection with acceleration off, and a half-second wake delay as the
  drawbacks (849148, 950244). Cirque Glidepoint was suggested the same summer; claussen: "it's pretty
  easy to retrofit a ctrackpad onto a Svalboard board even without customization. There's a lot of room
  to just put another USB device in there to prototype", but "track pads are really really bad for my
  specific RSI issues so it hasn't been a priority for me" (829684, 312400).
- **"The whole keyboard is the mouse" — slip-stick — is the oldest idea here and is still unbuilt.**
  Vulcan proposed an optical sensor under a half with friction elements that engage only when the half
  is fully loaded, so pointing uses wrist and shoulder instead of fingers; claussen: "This was actually
  the plan for the original Datahand, believe it or not. DH was WAY too heavy for it to not suck, but
  Svalboard is light enough" — 277 g/side, with maybe 200 g reachable, "only an ounce more than my
  normal mouse". The unsolved part is mode switching for stability (695840, 446420, 988192, 621481).
- **Wireless with a pointing device is unsupported** — the LEDs and optical sensors draw current
  continuously. carcosa's Handheld Scientific adapter on MCU 1.0 types but won't reflash or appear in the
  config tool (439824, 616846, 119637). See [open-questions](/open-questions.md).

## History

- **Ball size moved 34 → 40 → 44 mm over 2024, and the older advice is still findable in the channel.**
  2023-11: OrdovicianOperand, the only person running one, went 55 → 52 → 44 — "Typing is a bit nicer,
  since I'm not arching my hand nearly as much" (819065). 2024-03/04: the shipping ball was **34 mm** —
  "No, 34 is current recommendation... start with 34 for easier fit" (874560) — while phreaker ran 2x44
  and backed out: "Was the 44mm the better ball as a ball? Absolutely. Within the system as a whole? Not
  for my money" (542348). 2024-05 to 2024-08: **34-40 mm**, claussen "I don't
  really see practical benefits beyond 34 or maybe 40" (412757). From 2024-09: **44 mm** is the default
  (514238, 726181, 059986), shipping on prebuilts from 2025 (646187). The inversion is geometry, not
  taste — the sensor stack got ~10 mm shorter, so "that 40 is as high as a modern 44" (874845).
- **Bearings started as an open question and closed on statics.** 2023-09: four users argued static
  ceramic over roller bearings, with BTUs as "the expensive smooth option" (029632, 093760, 086716).
  2023-11 to 2024-06: BTUs got real prototypes and real angles from OrdovicianOperand — 105° front and
  110° rear uppers, ~57.5° for height, 4.0 mm Bosch bearing depth, "make at least one top bearing
  removable" (767047) — but claussen parked the mount "until there's a sunken case option that goes all
  the way to the table" (649600). From 2024-11 the answer is flatly statics (270430).
- **The connector plan predates every product, 2023-07.** The MCU headers were laid out for "pimoroni,
  bkb-style SPI trackball, [trackball] and trackpoint all in one. And I guess some dumb ps2 trackpad if
  you're into that kind of thing", the architecture covering SPI, I2C and PS/2 (970142, 061561). Of
  those, the Pimoroni option was later rejected outright — see the I2C breakout note above.
- **PS/2 on the RP2040 was the trackpoint's real blocker.** Every trackpoint claussen could source was
  PS/2 (565359), and QMK's then-new official RP2040 PS/2 driver **required the clock pin to be exactly
  one higher than the data pin** — "(WTF)" — which the v1 MCU pinout did not satisfy (224070). wolfwood
  explained why it was not just a code fix: the PIO program works on contiguous virtual pins with a base
  pin number, so swapping the two pins means reassembling the PIO program, and "the patch authors are
  cowards and just inserted the pre-assembled binary as a `#define` instead of adding the whole RP2040
  toolchain to qmk" (900156). claussen's fix was hardware: v2 MCU boards ordered 2023-08 with a
  PS/2-friendly pinout, against a bag of 20-odd trackpoints already on the shelf (366720). See
  [firmware-and-config](/firmware-and-config.md).
- **The 2023-08 fitment survey for balls, before any mount existed**: at least a 40 mm ball fits with no
  modification, more if you sink it into a concavity in the baseplate, though the thumb cluster starts to
  interfere; a 33 mm perixx ball on a bkb Charybdis mount fits too. The constraint is the **53 mm of
  unshaped height under the centre of the palm rest**, about 27 mm at the thumb corner (250816, 094948,
  190154).
- **The pointing devices are younger than the board.** 2023-09: the trackball was "already fully
  validated" in firmware but had no product-quality mount or PCBA (150236, 939304). The PMW3360 board
  went to fab 2023-11-14 and **ran on the first try on 2023-11-26** (176462, 405531). Early trackpoint
  boards needed **two 5k-8k resistors soldered on the MCU**, factory-fitted and then designed out of the
  next batch (345603, 509242). Ball colour was scarce until the shop stocked it — through 2024 red Sanwa
  was effectively the only standalone option (336701), whereas today red is deliberately *not* stocked,
  being the easiest colour to buy elsewhere (975090). See [suppliers-and-parts](/suppliers-and-parts.md).
