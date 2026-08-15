# Svalboard general channel — distilled reference (2025-10-17 to 2026-08-15)

Source: Discord channel `1124364902811844739`, 8,921 messages, distilled 2026-08-15 by LLM passes
over `raw/channel-1124364902811844739.jsonl` (seven chunks, merged). Message ids are the last 6
digits of the snowflake and are unique across the export. Agreement counts are floor estimates (who
spoke up), not polls. Where advice changed over the ten months, the bullet says what changed and when.

## 1. What this channel is about

The general / open channel for the Svalboard, a DataHand-inspired finger-keywell keyboard with
magnetic-retention optical switches and integrated trackballs, designed and sold by **claussen** (Morgan
Venable, founder; 20 years managing SW/EE/ME and AI research at Google — 399551, 741204; identity
inferred from 634238→739891). Not the support channel: build problems go to the closed
troubleshooting/supporters channel, layouts to the layouts channel, orders to tickets (304503, 843620,
597625). Content: pre-purchase questions, self-print advice, trackball debate, fit, firmware, mods.

Recurring voices: **claussen** (founder; product, policy, print tolerances; posts prototypes near-daily
through 2026, 109949). **phreaker** (volunteer firmware maintainer, "I am not part of Svalboard the
company" 532992; author of the "Viable" QMK fork and its Rust successor; highest message volume).
**Cyrus** ("resident fit nerd," hand-rehab background, UK; ergonomics and parts, keeps UK stock of balls
and sample clusters 565699). **Raven System** and **Hugin&Munin** (experienced self-builders who field
most newcomer questions). **lumbduck** (staff — sales, shipping, assembly; 551636, 043542). Also
**HazardousChurch** (gaming/mounting mods), **gyordanov**, **Atto**, **Lydie**, **ziasquinn**,
**robflop**, **Moo**, **flesh.priest**, **xsznix**, **lax3r**, **randomized_beaver**, **Lima/nocoffei**
(firmware mods). **Ben Vallack**'s November 2025 review drove a new-buyer wave (366059, 244480, 635129).

## 2. Recurring recommendations

### Firmware / software / keymaps

- **Boards ship without firmware** — POST only. Flash the latest release of
  `github.com/svalboard/vial-qmk` yourself. claussen (450890, 992539).
- **What to run today: `v2025-11-01`.** History: `v2025-11-01` (smooth scroll) → a Christmas 2025 RC
  with a new UI (Azoteq/trackpad users had to skip it) → phreaker's C "Viable" fork (daily-driven from
  Jan 2026, never released, now dead) → **viable-rs**, a Rust/`embassy` rewrite from 2026-03-22.
  phreaker: **don't wait for viable-rs**, it's pre-alpha with no UI and no trackpad drivers (701286,
  090304, 432602, 318558, 229928).
- **Vial, not VIA**, and **Keybard (captdeaf.github.io/keybard) is the config tool to use** — an alpha
  "faster than Vial" in Nov 2025, the recommendation by 2026: swaps whole layers, binds a key by
  typing it, exports layouts, backs up and restores keymaps. Svalboard keeps its own vial-qmk fork and
  "is not in QMK, and does not plan to be." phreaker, claussen (849753, 162951, 079090, 311742).
- **Web tools need a Chromium-family browser** (Firefox lacks WebHID), **close desktop Vial first** (a
  second tool holding the device is why a config "won't load"), and on Linux install the Vial udev rules.
  Cabling: **halves joined via `S`, host into either half's `U`** — host into `S` gives power but nothing
  works, so suspect the cable first (192313, 538683, 441328, 681384, 239720).
- **The master side holds the whole keymap** — right = master by convention (or the pointing hand if
  lefty), marked by the USB-C end of the inter-half cable; flash both halves if you swap. Make the
  pointing hand master: it polls ~400 Hz stock (peak ~465, 550–600 with turbo) versus a steady ~200 Hz
  on the sub side plus half-to-half latency. phreaker (883702, 927552, 898615, 789978).
- **The mouse layer is owned by the board and is always the top layer (14/15).** For a persistent one,
  copy 15→14 in Keybard and `TO(14)`; to type without falling out, bind keys on layer 15 or use an
  infinite auto-mouse timeout plus an escape key. The **automouse toggle disables the auto layer switch,
  not the trackballs** — don't put it where you can hit it, since with no mouse buttons bound you need a
  physical mouse to recover (466301, 199725, 881003, 432306, 833468).
- **Pointing settings live under "User" in Vial** (mouse/scroll swap, per-axis scroll lock, automouse
  toggle, DPI), all at svalboard.com/scroll; slow scrolling by lowering DPI, and **DPI keys must not live
  on the mouse layer**, which is why they seem dead (312914, 715924, 055348).
- **Smooth scroll shipped in `v2025-11-01`, Linux/Windows only** (Mac needs Mos or Smart Scroll), and
  **do that first update with Keybard, not Vial** — an undocumented 5-key → 5+6-key change makes Vial
  error out. The `Output Status` keycode dumps firmware version and pointer settings into a text field:
  `svalboard/trackball/pmw3389/right:vial @ v2025-11-01` (275032, 136278, 871902, 174082).
- **Optical switches are normally-closed, so a pulled-out key autofires** — blank that position on
  every layer. No debounce, so latency beats anything else you own; the **thumb-down key is two-stage**
  (optical, then a physical switch at bottom-out), which is the "6th" thumb key Vial shows (965436,
  362365, 652938).
- **Odds and ends**: everything layer-wise is stock QMK (tap dances, MO/TT, `DF(x)`/`TO(x)`, Alt
  Repeat), but a *custom* keycode means editing the Vial JSON and recompiling, and flashing wipes your
  config (816735, 828031); **macros can't be held** — put a modifier on the mouse layer as a normal key
  (255938); keep the keymap in version control, since layouts have reset to the flashed default
  unexplained (773480, 777030); **LGui = Command on Mac**, with no Fn/globe key possible (224564); steno
  works via Plover (096457); practice on **Svalbr** (`!svalbr`, r-tae.github.io/keybr.com), which renders
  your real keymap off the device (170801, 406144).

### Printing / materials / printers

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

### Trackballs / pointing devices

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

### Ergonomics / adaptation / mounting

- **Don't change your alpha layout at the same time as the board** — a multi-month commitment that
  raises the odds you quit; use what you already touch-type (claussen still types QWERTY after 25 years),
  and if you must optimize, Hands Down Neu or HD Promethium, flipping N/S because S keys beat N on a Sval
  (280360, 820933, 586853).
- **"This is a fit issue, not a force issue."** If you feel like you're hovering, raise the hand or
  lower the clusters; claussen's test is adding a few mm on the palm rest and watching preload change.
  Bottoming out every key is expected at first; hunting for bottom means too much preload (803008, 022660).
- **Fit order (Cyrus)**: wrists straight and flat → middle-finger orientation and palm-rest distance →
  index → ring/little → thumb → pointing device last. Common failures: living at one end of the
  adjustment range, and squaring the board to the desk edge instead of twisting the baseplates (547230,
  407537, 848370).
- **Clusters should not be parallel** — fingers are rays converging at the wrist, each finger roughly
  perpendicular to its center key at rest (N = extension, S = flexion, E/W = splay). **North keys are a
  flick upward, not an outward extension.** **Don't tilt clusters toward the palm** (the Azeron ask):
  no muscle makes a finger longer, so at the extreme you can't press center at all (372621, 378344,
  340535).
- **Clusters deliberately don't pitch north-south** — bend the metal towers or print the
  pitch-adjustable ones, but don't add degrees of freedom before you're adapted (942065, 028865).
- **If every cluster is twisted the same direction in a photo, rotate the whole base instead.** Pinky
  fixes in order: raise the pinky cluster a hair so fingers "just touch"; shim under the outside of the
  cluster arm with paper; add pinky stagger; heat-bend the pinky S key; bend or reprint the tower
  (673577, 267235, 176670, 550306).
- **Key weight: ~20 gf default, set by the magnet offset baked into the key** — 0.7 mm ≈ 20 g, 1.0 mm ≈
  ~10 g, zero offset 60 g+, and a 0.1–0.2 mm change is huge. Changing weight means new **keys**, not
  clusters or magnets; go stiffer (1.0–1.2) for gaming (725607, 162743, 471865, 559).
- **Slim clusters for narrow hands** — mix with standard, print one first to test-fit, and pair opposite
  "missing corners" to squeeze tighter; slim clusters need slim PCBAs, no going back after purchase.
  **Laterals**: inward are light and quick to learn, outward awkward, worst on the ring (498001, 224460).
- **Palm rests**: 5 mm shims by default, removable — "there's no right fit, there's just what fits you."
  **Rest the palm, don't hover.** **Don't build a cradle under the outer edge of the palm — that's
  Guyon's canal**; add traction instead. The Sval needs ~1 cm less splay than a DataHand (628081, 405875,
  451700, 150410).
- **Mounting is the biggest fit lever.** Two C-clamps plus two magic arms — **SmallRig 11" rosette arm
  (the rigid one; the light one wobbles under palm-rest load) and a CAMVATE C-clamp**, roughly half price
  on AliExpress. Sizing: no carrier plates → 11"; with plates → 7"; standing desk plus plates → maybe 5".
  The 1/4-20 threads are in the case bottom and carrier plates are laser-cut aluminum (292 g/pair),
  because a 1/4-20 in an off-center printed part fails under that torque; splay the halves wide and
  desk-mount on a sit-stand desk (252648, 479121, 383176, 661048, 396096).
- **Cheapest adjustable tenting is M5 screws in assorted lengths** (the M5 inserts aren't obstructed at
  the top); cattongue tape stops a tented board sliding. **Every desk is too high** — remove chair
  armrests, raise the chair to meet the board, elbows ~70–90°, or use an under-desk tray or lap desk
  (048321, 855037, 033967, 642069, 114391).
- **Trackball tendon pain comes from curling fingers** — use the middle phalanges, flatten the hand and
  slide south so contact is ~30° forward of apogee; raising the ball helps big hands (claussen ran an
  8 mm riser for a year). Skin flakes jamming the ball: moisturize (995248, 619124, 430484, 963296).
- **Foam-silenced center keys are a validated mod**: ~0.5 mm foam pads at the key's bottom plus a model
  with the IR window moved down by the foam thickness; dyamito said it "eliminated an entire symptom" of
  his RSI. Measured noise: Sval 51 dB vs Gateron browns 52. A mat and wrist strap is enough ESD gear, but
  treadmill desks are "literal Van de Graaff generators" (368980, 431794, 576642, 049458, 286578).

### Gaming

- **Gaming layer recipe**: switch to the mouse layer (14/15), then press the automouse-toggle key so
  trackball motion can't yank you back to layer 0 (phreaker binds it into a macro), and **turn off
  autoshift** (612489, 139654, 982748).
- **Sim and slower games work; twitch shooters are unproven.** phreaker finished Elden Ring (on 52 mm
  balls; would use 44 today) and most of CP2077 on trackballs; HazardousChurch played 4 h of Arma 3 but
  isn't accurate enough for headshot-reward games. Real mouse for FPS; accel curve matters more than
  hardware (468032, 424514, 246476, 637514).
- **WASD**: A/S/D on south keys with W on the middle-finger center; hold center keys, not north, and let
  OS key-repeat work. **High-APM (Tetris/osu) is unresolved** — 6.7 cps on a Sval vs 6.9 on a Wooting
  (489416, 856650, 609447).

### Suppliers / parts / part numbers

- **Magnets**: N35, **2 mm dia × 1.5 mm thick** (2×1 N52 substitutes). AliExpress magnets are fine for
  sample clusters but not production — inconsistent strength means inconsistent key force; production
  magnets come with the kit (663048, 219851, 356018).
- **Bearings**: 1/8" (3.175 mm) G5 ZrO2, e.g. amazon.com/dp/`B0CH749H5S` (~50 for $10); **balls**: Sanwa
  44 mm amazon.com/dp/`B0F1SWBL69`, Aramith snooker at 50.8 mm, or the shop (619072, 536348, 148692).
- **BTUs**: Bosch Rexroth `R053010810` / `KU-B8-OFK` from shop.nilsson.co.at (EU ~€8),
  store.boschrexroth.com, efog.tech (often out of stock), nextdayfittings.com (US), or uxcell 8 mm on
  Amazon, which "fit perfectly into the svalball 44mm btu model." **Avoid VCN310s** — "glue some
  sandpaper to your statics and go spin your ball on that" (443995, 469454, 076911, 236144, 075989).
- **Magnetic USB adapters** for the kit's cables: amazon.com/dp/`B0C5JXHTFY`, `B0CXF5LNDC`,
  `B0B3RYDQ3Q`. They are **7-pin on the Sval; 9-pin adapters won't fit** — count contacts in product
  photos. Cyrus runs magnetic on **both** ends of the inter-half cable; the magnetic end is a removable
  nugget in an ordinary USB-C port, and "the failure rate in use is significant anyway" — plain USB-C
  always works (926666, 933417, 143992, 616843, 567014).
- **FFC/FPC spec** for longer cables: 8- and 10-position, 0.5 mm pitch, stiffener length ≤3.5 mm,
  same-side contacts (Type A); +150 mm changes nothing measurable, though claussen doesn't test for it
  (321282, 521626).
- **Kit screwdriver is T10** (was 2.5 mm hex, 508160). Rubber feet: AliExpress `FC-036-DCW-PT` (570810);
  non-slip via keyboard mat or shelf liner (197589). **3M Dual Lock Thin `SJ4570`** mounts a second
  trackball, SJ3560 is far too thick (286281). Travel case: **Nanuk 910** (389542). Printed steel towers
  are in the self-print repo, metal ones on the shop (779757).

## 3. Product news / announcements — dated timeline

### November 2025
- **11-01 — firmware `v2025-11-01`** (github.com/svalboard/vial-qmk/releases/tag/v2025-11-01), announced
  by phreaker with "remember to back up your current layout." Headline: smooth scroll (Linux/Windows
  only); carries the 5-key → 5+6-key Vial breaking change (701286, 992236, 871902).
- **11-03 / 11-07 — Ben Vallack's review**: members-only short, then the public video; phreaker
  "Amazing video." It drove a new-buyer wave, and the "winter cohort" of self-print kit orders landed
  11-10..12 (430439, 366059, 244480, 047872).
- **11-14 and 11-25 — repo/Supporters access passes**: a manual, roughly weekly sweep of all outstanding
  orders at once; automation was blocked on a security review of community code, and LLM agents were a
  "hard no" (005194, 009754, 600074). **11-18 — lead times**: existing orders 2–3 weeks, new orders 4–5,
  with accurate product-page lead times (848638). **11-22** — a plug for the palm-rest adjustment-screw
  access hole is announced for the repo (999947).
- **11-28 (Black Friday) — no sales, ever.** "I don't change anything for Black Friday, I don't do sales,
  this is just a steady little boutique situation" (616842, 189544).
- **Late November — new default layout starts shipping**: arrow keys on the right-hand South keys plus a
  combined nav + numbers + symbols layer on right-thumb-down; existing owners get it by flashing latest
  firmware (837387, 468746, 338484).
- **Prebuilts are now V2** — V2.0 keys/clusters aren't cross-compatible with V1.x plastics, but PCBAs and
  hardware are unchanged, so a June '25 kit works with new prints (957603, 567343). **6-key / "2S"
  clusters** exist but are in testing, not in the shop (876170).

### December 2025
- **Early December — prebuilt lead time moved 2–3 → 4–5 weeks**, on holidays plus the wider audience from
  the videos (577369, 850088).
- **Alternate 1/4-20 mounting holes removed from the case** — not durable, too much torque; carrier plates
  replaced the idea, with hole positions unchanged on 1.2.8 (356822).
- **Self-print kits ship standard (not slim) finger PCBAs**, so 16 mm is the shortest cluster height;
  11 mm laterals make fitting "*much* fussier" and aren't production-suitable (666240).
- **Black keys are default at no upcharge**, only non-black costs extra (437684); **no TPU soft-part SKU
  for now** — it prints unreliably and the noise reduction "while noticeable, is not a big deal" (552592);
  **no metal Svalboard planned**, a flat "No," though the files are open if you want to make one (685464).
- **svalboard.com/chooser is back up** (`!picker`) and the Google Slides parts deck is deprecated in favour
  of svalboard.com/manual (883064, 337271). **Nanuk 910 repriced ~$100 → ~$120** — it exists only so a
  board can ship in it with cut foam; buying your own is cheaper (981379, 322253).
- **Christmas firmware RC** lands with a new UI in the firmware-channel pins — **Azoteq / trackpad users
  must not use it** until the next release (090304, 210429).

### January – February 2026
- **2026-01-09 — three years of Svalboard** (363070). **No published roadmap, by policy** — "I am always
  actively developing product"; phreaker: "No roadmap. I'm lucky if I can find a few stars to guide me
  by" (821610, 332599).
- **No injection-molded Sval**: ~$100k tooling plus millions in stock, and freezing the design "so it
  slowly bleeds out over 20 years… is the literal Datahand story" (811949). Restated at ~$30,000 tooling
  in March, never reconciled (590639).
- **The "Winter '25/'26" kit label is batch scheduling, not an end-of-life** — spring kits are coming, and
  **2S clusters are sold separately and strictly experimental**, not part of the self-print kit (990684,
  819180, 931960).
- **2026-02-13 — phreaker has daily-driven the C "Viable" fork for ~a month**; releasing it breaks the
  Vial tools, and the goal is that 95%+ of users never build firmware (432602, 793577).

### March – April 2026
- **2026-03-07 — the fingertip sizing PDF gets more explicit instructions** (206447).
- **2026-03-22 — viable-rs, the Rust/`embassy` rewrite, flashed to phreaker's daily driver**; by 03-29 it
  had run a week with macros, layers, mouse layer, LEDs, combos and mod-taps, and the C "viable" was
  declared dead (017655, 905048, 318558). As of **04-02** it is not public, with no UI and no trackpad
  drivers; planned are a configurable report rate, home-row-mod work and PTP touchpad support (067866,
  999938).
- **2026-04-14 — Bambu X2D launched**: dual nozzle, chamber heating, $899 combo; claussen rates the
  dedicated support nozzle and more even ABS chamber heat as the real wins (694171, 546343).
- **Thumb Up key fragility fixed** — half a millimetre added to its thickness, none broken since (469161).
  **V2 pushed in the thumb side keys**; the older thumb cluster with the Up key behind the top-right key
  is gone for good — different PCBA, hosed trackball fit (968655, 680608).
- **Shop prices are the real prices, duties included**; prebuilt lead times are configuration-agnostic
  except custom colors; kit orders ship in FIFO batches, not on request (587543, 630562, 094254).

### May – June 2026
- **Square-nut retention cantilevers replace M3 heat-set inserts in the baseplate** — 30 torque cycles
  with no delamination, surviving deliberate over-torque, "very significant reduction in assembly
  annoyance"; nuts insert **from the back**, removing top-plate holes and long bridges in the T area, but
  not for the M5 / 1/4-20 tenting mounts, which need torsional stiffness (109949, 546979, 202327).
- **Soft molded palm rest in development** — molded, not filament; even 15A durometer tested "wayyyy too
  hard." An **adjustable spherical-bearing palm-rest carrier** (M3x12 screw) has "adjustment range on
  this is bananas," with fuzzy skin on the joint interface so ABS joints lock down (182029, 974031,
  402646).
- **New trackball holder variant** moves the south bearings up and the north bearing down to reduce
  "capsize to the south" clack (workaround: tape up the anti-clack nub); **38 mm holders are no longer
  maintained** (585459, 584626, 207810).
- **Carrier plates now have a stiffening bend**; side-screw mounting is rejected because splitting
  torque destroys cases with side heat sets (367969, 760120).
- **6-key PCBAs are available to self-builders but unlisted** — open a ticket. **Kit screwdriver changed
  to T10.** **Black 44 mm balls are on the shop; red stock is reserved for full-build production.**
  Sawed-off (no palm rest) is not a standard option (188873, 508160, 148692, 731964).
- **2026-06-10 — repo-access automation broke again**; claussen ran a manual pass and was on vacation that
  week (817684, 225524).

### June – August 2026
- **svalboard.com/chooser is offline again** — use an LLM or manual image coloring meanwhile (30, 290,
  264425).
- **Policy restated**: kits are not returnable, prebuilts follow the site refund/shipping policies,
  reselling self-print kit builds for profit is discouraged, and repo access is governed by the
  3D-printable-parts access policy page (757222, 1243, 1242). The Svalboard also turned up at an SF
  keyboard meetup (youtu.be/97TcZ7lD_oc, 1268).

## 4. Contested or open questions

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

## 5. Notable links / resources

**Official** — svalboard.com/build (`!build`), /manual, /scroll (pointing and scroll settings, the
most-cited link of all), /chooser (`!picker`, intermittently offline), /pages/key-mechanism (532, 616832,
437789, 883064, 696819); /products/sample-cluster, /carrier-plates, /humpback-palm-prototypes, /touchpad,
/trackball-upgrade-kit (664728, 906555, 328549, 544044, 636353); /pages/trial-program,
/policies/refund-policy, /pages/3d-printable-parts-repo-access-policy (636, 638, 1242). Build/fit manual,
"Choosing Key Width": docs.google.com/document/d/1Um4EAIK-GLQGw-9xHUFe-aCtHJDENYUSzhcqQi9ppwU (577263);
Substack: open.substack.com/pub/svalboard/p/size-matters (splay vs DataHand, 205501) and
svalboard.substack.com/p/work-work-work-work-work-work (cluster/force profile, 539763).

**Code and CAD** — github.com/svalboard/vial-qmk, releases/tag/v2025-11-01, and the flashing doc at
.../keyboards/svalboard/docs/flashing_firmware.md (992539, 701286, 548094);
github.com/svalboard/svalboard-configs (436739); github.com/orgs/svalboard/invitation, where a missing
repo invite hides (193381); github.com/svalboard/svalboard-open-trackball (slim PCB) and
svalboard.com/trackball-repo (deprecated) — current trackball CAD is the OnShape "All Trackball Holders"
doc, with cad.onshape.com/documents/72acc93b552744d39375cf5c the updated 38 mm holder (286064, 207810);
printables.com/model/1740316 (printed BTU, 205198); printables.com/model/320000 (standalone Mac Touch ID
module, 762997); github.com/Caldis/Mos and marcmoini.com/sx_en.html (Mac scroll, 136278, 838540);
docs.qmk.fm/feature_layers (141671); get.vial.today /manual/linux-udev.html, /docs/custom_keycode.html
(441328, 828031).

**Config, practice and video** — captdeaf.github.io/keybard, with a dummy/demo keyboard mode (574);
vial.rocks (308596); r-tae.github.io/keybr.com — Svalbr, the keymap-aware keybr fork, also at
svalboard.com/svalbr (`!svalbr`, 170801, 406144); thockflow.drpng.net — drpngx's layout + matrix viewer
(136922); keyboard-layout-editor.com/#/gists/42183d74f1503c7e6a6c83aee184cc7b — the default layout in KLE
(021661); github.com/input-leap/input-leap (Deskflow) to share one Sval across two PCs (587, 599).
youtu.be/-Lz_FNoYHNM — Ben Vallack's review (366059); youtube.com/watch?v=ArXnZVQM3LM (playlist
PL_Jqu5bq_U_CQBhYryllArikWe-ns3g8q), the Svalboard Fit playlist (`!fitvid`, 250853, 848370);
youtube.com/@svalboard, watch?v=a0s-XjzEFkY (intro/Vial walkthrough, 824392), watch?v=MlILG3Jew2w
(tenting/mounting, 267712), youtu.be/g2qnoPZ-qYs (single-BTU undermount, 406810), watch?v=fa_BZ1AKQVk
(community build guide, 468), youtu.be/97TcZ7lD_oc (SF meetup, 1268);
note.com/myomyomyo4256/n/ne78090d0e7a9 — a thorough Japanese review, "a labor of love" (371543);
f261b0d1-layouts-wiki.xsznix.workers.dev/guides/start/recommendations/#why-these — HD vs AKL (403604).

**Parts sources** — amazon.com/dp/B0F1SWBL69 (Sanwa 44 mm balls), /B0CH749H5S (ZrO2 G5 1/8" bearings),
/B0C5JXHTFY, /B0CXF5LNDC, /B0B3RYDQ3Q (magnetic USB adapters) (536348, 619072, 926666, 520397, 407722);
store.boschrexroth.com/en/us/p/ball-transfer-unit-r053010810, shop.nilsson.co.at,
efog.tech/products/bosch-rexroth-btu, nextdayfittings.com (988810, 443995, 469454, 076911) and
elecom.co.jp/products/M-TU03SS via Buyee (834483); ambrosiafilament.com matte ABS (390);
store.idryer.org iheater-kit-200w chamber heater (002942); antistat.com ESD heel grounders (892969); NYC
makerspaces fatcatfablab.org, nycresistor.com and NYPL free access (527142, 485845).

## 6. Newcomer FAQ (asked more than once)

- **Do you type faster on a Sval?** (547952, 799, 249080) → No. Buy for pain relief; expect
  equal-or-slower burst speed, far lower effort and much higher endurance (806, 278221).
- **How long until I'm proficient?** (557854, 868041) → One week to one month; 1–2 weeks if you already
  run a split with thumb clusters (225925, 307530).
- **Do I need a printer? Can a service, library or makerspace do it?** (303461, 733861, 875436, 244133)
  → No third-party service will hold the tolerances and the license is explicit; buy a used A1 mini or
  P1S, use a makerspace, or buy prebuilt — "Nobody regrets buying a pre-built" (382096, 666782, 817).
- **Where do I get the print files?** (178522, 575536, 932157, 408057) → A private GitHub repo; the
  invite email usually lands in spam, or hides at github.com/orgs/svalboard/invitation. Access is
  customer-only and granted in a manual ~weekly pass — give claussen or lumbduck your order number if
  automation missed you (466778, 193381, 739200).
- **What material, and can I resin-print?** (681330, 949109, 136396) → FDM, plain PLA (ABS supported too,
  PETG for some); resin is out — not skin-safe, brittle (740672, 191973, 031350).
- **How much filament, and will it fit my printer?** (952096, 206411, 227412) → Under 1 kg for both
  halves; Bambu P1S or X1C is the reference; the A1 mini needs the case split (665494, 793783, 093888).
- **What magnets and bearings do I need?** (090634, 371963, 706992) → N35 2 mm × 1.5 mm magnets; 1/8"
  (3.175 mm) G5 ZrO2 bearings, 3–4 per side (663048, 865893, 636353).
- **Does the self-print kit include trackballs?** (082059, 632544, 915290) → No. "+2x Trackball PCBAs"
  means sensor boards only — source ball and bearings yourself; prebuilts include them (541298, 241600).
- **44 mm or 52 mm ball?** (971998, 393842, 213882) → 44. 52 needs hands over 20 cm, compromises fit and
  wants custom holders (984528, 628269).
- **One trackball or two? Which pointing device for RSI?** (641007, 024660, 355742) → Two: one to point,
  one to scroll; swappable later (296465, 135043, 575685).
- **Does it ship with firmware, and what programs it?** (688121, 569, 1166) → No, POST only; flash the
  latest vial-qmk release, then use Keybard, Vial or vial.rocks (450890, 992539, 311742).
- **Do I have to measure my fingertips, and what if the size is wrong?** (963860, 749556, 948725) → Yes,
  and trust the sizer: it only sets NSEW key thickness, those keys swap out, and thickness isn't
  adjustable afterwards; round up when borderline (500507, 052999, 931812).
- **Is the self-print kit going away? What are lead times?** (990684, 239958, 913530) → Batches, not
  EOL; each product page carries current lead times, which moved from 2–3 to 4–5 weeks in December 2025
  (265113, 819180, 579660).
- **Is there a Black Friday sale or discount code?** (710036, 654346, 830292) → No. Svalboard runs no
  sales, ever (616842, 189544).
- **Return policy / can I resell mine?** (451262, 625) → Kits are not returnable; prebuilts per site
  policy; reselling self-print kit builds for profit is discouraged (757222, 1243).
- **V1 vs V2 printed parts — do I reprint?** (762481, 905628) → Print 2.0: V2 keys/clusters aren't
  cross-compatible with V1 plastics, but PCBAs and hardware are unchanged (957603, 877762).
- **Sval vs Glove80?** (986945, 206411) → Different families: Glove80 continues the Kinesis line, Sval
  the Datahand; wired-only, and the 20 g switches plus integrated pointing are the selling point (665494,
  718202).
- **My board is stuck repeating one character.** (516097) → Find the key in the matrix view, check for a
  loose key or cluster magnet, blow out debris; a cracked opto-interrupter trace or failed magnet is
  possible, and a pulled key autofires because the switches are normally-closed (013242, 965436).

## Gaps

- Channel name is inferred ("general"); the export carries ids only, and claussen = Morgan Venable /
  founder is inferred, never stated outright.
- Attachment URLs are expiring Discord CDN links, so image-only claims — fit photos, PCB damage,
  V1-vs-V2 comparisons, claussen's key/palm-rest studies, Lydie's foam mod — rest on the surrounding text
  (906890, 588691, 716683, 368980, 283615).
- Many answers point into channels not in this export (troubleshooting, layouts, mounts, supporters,
  firmware, tickets), so their resolutions aren't visible — including the firmware RC's new UI and the
  "new square baseplate" announcement (577633, 833387).
- **Firmware version names are loose and were never reconciled** in-channel: "latest FW", "11-01
  sources", "the x-mas release", "viable", "viable-rs", "viable-qmk" (601559, 347977, 533592); viable-rs
  status here is as of 2026-04-02 (067866). Open bugs at the end of the range: the Mac/Windows
  wake-from-sleep failure (990695) and the random layout reset, with no root cause (216251).
- Prices, lead times and sourcing claims (BTUs, Nanuk, bearings, sample-cluster shipping, printer
  prices) are user reports at a moment in time across several countries, and are unverified — as are
  external product claims (Sanwa/Aramith ball quality, P2S/X2D specs) (033181, 458024, 496130, 194495).
  Repo-sharing answers come from phreaker and Zach Valenti, not claussen (540490), and polling-rate
  numbers are phreaker's own estimates (789978).
- Whether the square-nut baseplate retention (546979) actually shipped to the repo is not stated
  in-channel, and phreaker's "how to buy a Svalboard" guide (475209, 612538) was never published here.
