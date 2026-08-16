---
type: Reference
title: Suppliers and parts
description: Part numbers and sources for magnets, sliders, bearings, balls, BTUs, cables, connectors, fasteners, tools, mounting hardware and cases.
tags: [svalboard, discord, parts]
source: "discord #general 1124364902811844739, 2023-09-07..2026-08-15 (gap 2025-08-10..2025-10-17)"
---

# Suppliers and parts

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-1124364902811844739.jsonl`; a few 6-digit suffixes collide in the 41k-message export, so disambiguate by date if a lookup returns two hits. Agreement counts are floor estimates.

## Magnets and sliders

- **Magnets**: N35, **2 mm dia × 1.5 mm thick** (2×1 N52 substitutes). N## is the neodymium grade; N52
  is the strongest claussen has sourced, N25 "was trash and not usefully weaker", and N35 covers the
  whole useful force range (089941, 442056, 187080). AliExpress magnets are fine for sample clusters
  but not production — inconsistent strength means inconsistent key force; production magnets come
  with the kit (663048, 219851, 356018) and are also a shop SKU: "aliexpress vendors are a really
  hit-miss affair on magnet strengths" (855050, 957018). The AliExpress spec people buy anyway is
  2 × 1.5 mm N35 (511570, 483085).
- **The kit's 200 magnets are spares**, "just for spares if you want to experiment with different key
  forces", so skip the extra-magnets add-on on a kit build (962324, 375143, 112478). claussen
  estimates ~100,000 magnets on hand (103592).
- **Slider force is marked with dots on the key base — more dots = lighter**: 1/2/3/4 dots =
  1.2/1.5/1.8/2.1 mm nominal offset (045477), later moved to the back so it is hidden once installed
  (950986). Measured centre-key force map (2023-11, pre-2.x geometry): zero-offset gapped sliders at
  0.4 / 0.6 / 0.8 / 1.0 mm gap give **29 / 25 / 18 / 13 g**, claussen's pick 0.8 mm ≈ 18 g; paired
  1 × 1 mm N50 cylinders give ~12 g (214692, 649469, 484682). See
  [ergonomics-and-fit](/ergonomics-and-fit.md).
- **Loose key magnet, claussen's repair**: paper over another key's magnet, set the loose one on it to
  get polarity right, lift with a flat blade screwdriver, dip in CA, press into the well, squeeze
  flush with parallel pliers (260830).

## Balls, bearings and BTUs

- **Bearings**: 1/8" (3.175 mm) G5 ZrO2, e.g. amazon.com/dp/`B0CH749H5S` (~50 for $10) (619072). The
  older docs-page default was 3 mm zirconia G5, uxcell `B081SPLWT5` / `B081SNH8J5` (534200, 136032).
- **Balls**: Sanwa 44 mm amazon.com/dp/`B0F1SWBL69`, Aramith snooker at 50.8 mm, or the shop (536348,
  148692). Sanwa off Amazon is what people actually buy; claussen rated the red 44 mm "really
  nice-looking" while the shipping default stayed Perixx black (486549, 021570, 283324). See
  [pointing-devices](/pointing-devices.md).
- **BTUs**: Bosch Rexroth `R053010810` / `KU-B8-OFK` from shop.nilsson.co.at (EU ~€8),
  store.boschrexroth.com, efog.tech (often out of stock), nextdayfittings.com (US), or uxcell 8 mm on
  Amazon, which "fit perfectly into the svalball 44mm btu model." **Avoid VCN310s** — "glue some
  sandpaper to your statics and go spin your ball on that" (443995, 469454, 076911, 236144, 075989).
  Earlier US sources for the same Rexroth part: store.livhaven.com at $11.35 with free US shipping,
  vxb.com Iguchi IS-05SNM at ~$20 each (214850, 490737). Ploopy Nano BTU-mod mechanicals are a
  starting point for a home-made cradle, github.com/gbrnt/ploopy-nano (214850).
- **DIY pointing parts**: Azoteq TPS43 PCBA direct from Mouser, 6-pin FPC into the pointing connector
  (473970, 817293). **The trackpoint housing has no screw mount** — 3M double-sided tape, masking
  tape, or Dual Lock; "Trackpoint slot mount not done yet" (778118, 038618, 205706). **3M Dual Lock
  Thin `SJ4570`** mounts a second trackball, SJ3560 is far too thick (286281); 3M friction tape
  `B0093CQQNQ` gives magnet-mount grip (291166). The trackball holder CAD is public on Onshape,
  everything else is customer-only (487084).

## Cables, connectors and ports

- **The cables are not proprietary — plain USB-C at the board.** The magnetic ones are off-the-shelf
  "540 degree" cables, "proprietary only in the sense that they have the Svalboard logo printed on
  them" (077342, 595062); the magnetic ends are just adapters, and to remove one, "grab it with your
  fingernails and pull" (246130, 344400). claussen sources his directly, won't sell them separately,
  but will add them to any other order (033917, 612526).
- **Magnetic USB adapters** for the kit's cables: amazon.com/dp/`B0C5JXHTFY`, `B0CXF5LNDC`,
  `B0B3RYDQ3Q`; otherwise search "540deg magnetic USB data cable" or "540 magnetic USB c adapter",
  ~£5 each (926666, 344973, 398695, 289385). Older 7-pin picks: Amazon UK 3-pack `B0CDLWNJXT`, US
  `B0B4JJ4FM7` (762897, 768819); right-angle `B0BNHPC5CS` was rejected on reviews (767881).
- **They are 7-pin on the Sval; 9-pin adapters won't fit** — count contacts in product photos (933417,
  123776). Check magnet diameter too: a spare wouldn't interoperate "because the magnet was a slightly
  smaller diameter" (713432, 000744), and buy the data cable, not the 2-conductor charging-only
  version (012594, 865588). The 9-pin STATIK/statico and AUFU ecosystems are better built and hold
  harder, but gave onlyforresearch random sub-half dropouts and are harder to clear of debris (066863,
  413898). **The stock magnetic end is 3 rings plus a centre dot = 4 contacts: +5 V, 0 V, D+, D−**
  (368854, 610805); twist the connectors to clear grit when a half stops responding (731950).
- **Cyrus runs magnetic on both ends of the inter-half cable** via generic adapters, which
  interoperate with the Svalboard-branded ones; the magnetic end is a removable nugget in an ordinary
  USB-C port, and "the failure rate in use is significant anyway" — plain USB-C always works (143992,
  616843, 567014, 276026, 696544). Converting a Sval cable's USB-C end into a second magnet and
  leaving nuggets in both halves means "there's almost no chance of damaging the MCUs", and lets you
  flash a different keymap per half, so whichever side takes the master cable decides the keymap
  (195054, 601474). Nuggets in all four connectors also give a seating check — the sub connector's
  blue LED tells you the host side is live (058297).
- **Lengths as shipped: 1 m between halves, 2 m to host**; claussen will drop an extra 2 m into an
  order on request (473665, 198423). The split-cable poll settled on 1 m because "1m is the standard
  for magnetics, which is what I'm sourcing" (205671, 924362). **The kit includes one C-C cable for
  joining the halves; you supply the host cable** (197097, 505061). For boards pressed against a
  monitor, AliExpress right-angle ribbon USB-C "seems very likely to just work"; avoid the Chenyang
  unit on Amazon, "the reviews are horrible" (010100, 012954, 948293).
- **Port labels: U = host USB, S = split/serial**, printed on the back edge of each board and **not
  mirrored**, at 0.3 mm feature size because "everyone knows what U and S look like"; mixing them up
  "won't even hurt the boards" (286972, 454573, 879890, 208477, 639132). On an assembled board the
  host cable goes to the non-split side, the cable on the right on both hands (719694). No USB logo
  on the case, ever: "it's a trademarked thing. Zero chance I'll ever certify." (048434)
- **The inter-half link is not USB, just the connector** — serial TX/RX plus power and ground, the
  USB-C connector used as a robust replaceable 4-conductor carrier at a much lower data rate (575552,
  758677, 687572), so a USB-over-wireless dongle cannot bridge the halves (023188). Real USB for a
  split would be "weird and inappropriate from an embedded timing POV", and on the alternative, "TRRS
  is duuuumb" (997524, 090237).
- **FFC/FPC spec** for longer internal cables: 8- and 10-position, 0.5 mm pitch, stiffener length
  ≤3.5 mm, same-side contacts (Type A); +150 mm changes nothing measurable, though claussen doesn't
  test for it (321282, 521626). **All internal connectors are FFC, 0.5 mm pitch, A-to-A always** —
  "If we do JST/Dupont it'll be debugging", and "There will never be a wire connector except for the
  non-existent battery" (757625, 244465, 314943). It is a commodity off Amazon; only the pointer
  boards are custom (398490). FFC was a design requirement, not a cost choice: ultra-flexible so it
  doesn't backdrive the fitment mechanisms, and low-inertia under shock (922472, 343542).
- **Thumb ports are 8-pin except the Azoteq ("Azo") port, which is 6** (705536, 732853); an encoder
  alongside a trackball needs a 6-pin FFC breakout, one replacing the trackball needs 8 (891537). On
  the TC3.12L only the 10-pin connector is needed — the 8-pin is back-compatibility only (871204).
  Skip the thumb-cluster cable management: "Just stuff it all in, it'll be fine and easier to rework
  later" (191644). On newer cases the pitched left-hand ball holder "eats up a good 40mm of cable just
  getting down to the plate" — slot the top plate or route through the pointing accessory slot
  (826005, 111522).
- **Board suddenly dead, LEDs off? Suspect the cable or the mag adapter first** — "we haven't had an
  MCU failure out of the blue yet" (861093, 800233). One board dropping power on light bumps turned
  out to be a cracked USB connector solder joint, not the magnetic cable (487168, 575539).
  Intermittent dead or stuck key: debris before solder — pull the slider and cap, block the light path
  with something opaque to prove the electronics work, scrape the cluster's centre gap. It has hit
  "maybe 1-2% of people, once" (589312, 375218, 607090).

## Power, hubs and wireless

- **Suspect power before firmware**: "First guess is ALWAYS power. Powered hub has been a big help for
  various folks having KVM-related issues" (609667). One KVM problem was fixed by swapping the hub's
  wall wart from 5 V/1 A to 5 V/3 A (511250, 880869); unplug everything else from the hub first
  (955227); on a Mac, go straight into the machine with a plain Apple USB-C→A adapter (746335,
  188244). Measured draw is **~250 mA at 5 V, ±20 mA** with no pointing device, vs ~162 mA for an OG
  DataHand, "so 500 mA off a PC port should be fine" (671390, 946109); the trackpoint pulls 1.38 mA
  and total LED draw across both hands is ~150 mA (834765).
- **Wireless means a Handheld Scientific USB Bluetooth adapter plus a battery bank**, and is
  discouraged. The **BT600** is the tested unit — full pointer support plus 2D scroll in BT mode on
  Windows and NixOS; "for USB passthrough, it is absolute crap", and the BT500 had issues (579133,
  456424, 764864); the HD-600 is also tested over BT (324466). You still need the cable between
  halves plus your own USB-C cable into the adapter (526794). Optical sensing draws ~300-500 mW, so
  10,000 mAh lasts "a few days" — "only really suitable for fixed chair mounts or lapdesk IMO", and
  "The wire between halves isn't going away" (613534, 935097, 391034).

## Fasteners, tools and glue

- **Kit screwdriver is T10** (was 2.5 mm hex, 508160); a **T6** bit ships in the spares kit — steel, so
  it takes a magnet — and the holder screws are T10 (804672, 516542).
- **Fasteners are M3 and M2 only, M3×6 mm, black oxide carbon steel; the self-tapping M3 are
  galvanized**, and the square nuts are DIN562 M3 (686288, 896144, 627841). On stainless: "Stainless
  brings other problems in manufacturing… and is sofffft", plus "So far zero people have reported rust
  on any fasteners" (131807, 126460).
- **Knipex parallel pliers are the magnet-seating tool** (e.g. `amazon.se/dp/B0001P0CJS`, 847298);
  claussen ground his tips narrower, "and the results are A+" (948100), while smaller Knipex have
  worse angles and cheap Irwins "were unfortunately not good at staying parallel" (292724). His
  magnet-assembly screwdriver is a **Klein Tools A131-2, 1/8" flat head** (118322); what matters is a
  2" blade, ~4" total so the end sits in your palm rather than through your hand, and a flat taper
  with no radius at the tip so a slip doesn't change the angle (292410, 490323).
- **CA glue**: Bob Smith Industries is "much better value and quality than the loctite/crazy glue CA"
  (770308); claussen uses Starbond and has used BSI — "It's mostly a question of viscosity" (877190).
  Molecular-sieve desiccant stops CA going off (140940). See [printing](/printing.md).
- **Rechargeable compressed-air duster** `B0BMG7P86R` (541386) — but dust only as needed, a key well
  "maybe once or twice a year" (120445).
- **Foot pedals**: a plain industrial foot switch, not sewing-machine gear priced for a captive market
  (143251); Adafruit 423 is what people bought, with six-plus spare GPIOs free (761942, 385209). River
  argues pedals suit press-and-hold, infrequent, big-muscle actions only: "I tried one for left click
  once and even with very light springs I think it would have taken my leg off" (707116).

## Mounting hardware, rests and feet

- **Mounting is CAMVATE-style C-clamps with SmallRig rosette arms**, on Amazon or B&H — "the $35 one
  is right" (476624, 283155). dmfay: "look for the rosette arms specifically, they're sturdier than
  smallrig's basic magic arm" (101696), and ziasquinn cheaped out first, then understood why, "esp the
  ability to attach and detatch the heads with your thumb" (311888). Other links bought: `B0BR7L53ZG`,
  `B018RLY6B2` (237888), SmallRig 7" `B0CFPZFZ5K` (853678), Neewer folding stands — too small for one
  buyer, "it tilts" (775529, 119141) — and frostyllama's `B0CK28KNS7` dual arm, whose 1/4" ARRI points
  on both clamps beat a C-clamp without them (925910).
- **The clamps are the weak link**, not the arms: CAMVATE is "tolerable, not fantastic" and lacks the
  ARRI anti-twist holes (417216); two clamps for spaciousness, one for travel (007583, 812241).
  **Clamp wobble is compliance, not friction** — the vinyl dip is "very squidgy", so cut it off or
  hard-mount to the desk (279637, 431425). Watch the arm lock direction; OwlWithAPipe nearly dropped a
  board when the post unscrewed (977896). **MagSafe pucks are a trap**: Zach Valenti "ended up spiking
  it to the floor a couple times", and the adhesive rings, not the magnets, are the failure point
  (696724, 909801); his survey rates Arca-Swiss as more secure but slower, HawkLock-type releases as
  having significant play, and **Triad Orbit as the only quick-release system without play** (783119).
- **1/4-20 threads**: carrier plates (svalboard.com/products/carrier-plates) exist because a 1/4-20
  thread in a printed part fails — "Too much torque on layered parts no bueno" (988345, 467650). The
  bolts are annoying to source in Europe, though most camera arms ship with the screw (857404,
  308753); claussen's alternative is using the M5 inserts to hold the board to a plate (820039).
  Printed steel towers are in the self-print repo, metal ones on the shop (779757); the stainless
  towers are laser cut, bent and sandblasted (725919).
- **Palm rests**: TPU Humpbacks are the shipped option; claussen's easy softening test is 7 mm wetsuit
  neoprene glued on, and the silicone rests he teased are "20x too expensive" to sell in that form
  (302480, 347530, 666176). His TPU-for-AMS (~70D) prototypes print "incredibly clean" but are too
  hard (049748, 252073). **No TPU nub ships with kits** — models are in the repo, print at 95A (854396,
  152670). For wrists, cloth-covered gel rests rather than bare gummy plastic, e.g.
  amazon.com/gp/product/`B0BJ98RT8L`; avoid the cheap blue plastic-covered ones, "your hand can't
  slide around" (279844, 403345).
- **Rubber feet**: AliExpress `FC-036-DCW-PT` (570810); non-slip via a keyboard mat or shelf liner
  (197589).

## Cases, spares and buying

- **Travel case: Nanuk 910** (389542), sold as a shop add-on at
  svalboard.com/products/nanuk-910-case-add-on (712676); ~$56 on Amazon `B00BP8URVS`, and you want the
  pluck foam (304381, 981517). Cheaper: the empty case plus an old memory-foam pillow (777146), or the
  earlier $35 Monoprice 11×8×7 hard case `B013Z73TWA` with the middle foam removed, clamping both
  halves against a printed bracket (075520, 675442). A case design contest produced designs but
  "nothing actually built" (799454).
- **Broken or melted parts: claussen ships spare plastics from the parts bin at cost of shipping**,
  "because the whole point of the design of the product is survivability" — trustno1 melted half a
  board against a car heater and rebuilt it (688450, 593759).
- **There is no PCB-only, electronics-only, or files-plus-shopping-list SKU**, and the price wouldn't
  move: "The price for a kit without fasteners would be the same as the price for a kit with
  fasteners". Fasteners are custom-ordered, heat-set insert dimensions aren't consistent across
  sources, and the electronics are "entirely custom" (794112, 559114). **Prices are not coming down**:
  "volumes remain low and the parts remain numerous and fiddly" (679957).
- **Try before buying with the sample cluster**, svalboard.com/products/sample-cluster (362913) —
  forces and colours are random from the bin, and the long tab goes north, the other three are the
  same (073682).
- **There is effectively no second-hand market** — used boards get posted in the channel first (562345,
  673775), and claussen occasionally sells a "mule", a dev daily-driver with mismatched spare or blem
  parts (095957). People buy on the **return policy**, which claussen calls "amazing" and says makes
  resale moot (723305). Self-print repo access is a GitHub invite tied to the username on your order
  (637286); see [printing](/printing.md).
- **Shipping**: from California, 3-5 days by UPS (655886); Western Europe ~$60 plus local duty and
  typically 3-5 days (679957, 419785); Canada ~$60 plus duty, cheaper via a cross-border pickup shop
  (426139); Australia is express-only (658078); Germany is not prepaid, so expect a customs letter
  (411666). First Class is cheapest and slowest (082024). Cyrus is a de facto UK parts depot just
  north of London with spare thumb modules and MCUs (942353, 622164).

## History

- **Double-ended magnetic cables were "impossible" until members routed around it.** From 2024-01 to
  2025-04 the standing answer was that magnetic-to-magnetic cables don't exist — suppliers "found it
  would result in unstable connection", "Double ended isn't manufactured", and the manufacturer told
  claussen they don't meet data-rate specs (408279, 579154, 554837, 373530, 149754). The sanctioned
  workaround was a USB-C-to-magnetic **adapter** (559296), improvised as early as 2024-01 from two
  USB-A-to-magnetic cables (844516); the 2024-05 framing of magnetic-both-ends as "a wish, not a
  product" (293442, 190433) is superseded by the adapter pattern now in use (195054).
- **Pre-540° magnetic pair, 2023-09**: AUFU `amazon.com/dp/B08RD6HGH5` for master↔slave plus an "A.S"
  `amazon.com/dp/B07WSM9YP5` for host — the mounts differ slightly in size, so you can mount the A.S
  ends in the AUFU cables but not the reverse (864707). claussen's settled position is that "generally
  speaking the 7-pin 540° style all seem to come from the same place", though not all are
  cross-compatible (344973).
- **Cable lengths were corrected**: wejn settled on 0.5 m as "the perfect interconnect" (499866), and
  Cyrus's "0.5 m and 1 m" summary (042174) was wrong — corrected to the shipping 1 m / 2 m in 2025-01.
  Black FFCs were sourced 2023-10-12 (384164).
- **ESP32-era wiring (superseded)**: left port of the left half to host, right port to right port,
  "Not mirrored", and "Won't damage anything if you get it wrong" (891678, 567872) — replaced by the
  U/S labelling.
- **Plate 1.1g** (2024-06) added the second thumb-tower slot, a 7th closure screw stiffening the new
  N-inner 1/4-20 location, and much bigger closure-screw pylons; backwards compatible (298115,
  237119).
- **Accessories were undocumented until 2024-05**, when claussen said "Need a recommended accessories
  page on the shop" and Jolly was "deputized with edit access to the docs for his sins" (486886,
  848815); before that, links lived only in channel pins.
