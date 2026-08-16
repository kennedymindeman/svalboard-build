---
type: Timeline
title: Timeline
description: Dated Svalboard product news, policy and firmware announcements from September 2023 to August 2026.
tags: [svalboard, discord, timeline]
source: "discord #general 1124364902811844739, 2023-09-07..2026-08-15 (gap 2025-08-10..2025-10-17)"
---

# Timeline

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-1124364902811844739.jsonl`; a few 6-digit suffixes collide in the 41k-message export, so disambiguate by date if a lookup returns two hits. Agreement counts are floor estimates.

### September – December 2023
- **09-07 — self-print repo access goes live**, still churning: "things will flicker" (497701, 875454).
- **09-08** — cluster magnets move to N35, with a 0.6→0.8 mm offset equivalent for owners (253732).
- **09-14 — new thumb cluster PCBA inverts the centre key to blocked=active**, with a 4-layer board for
  opacity; ~80 tested at ~97% yield (358460, 786270).
- **09-24 — kits become batch-only**: after the current ~15, no date — ~10 at a time is the minimum worth
  the logistics (063441, 114400). **09-30 — the Vial build is re-synced from upstream** (927440).
- **10-17/18 — an "Alpha all-star edition" ships**, and Alpha builds start offering several key widths
  plus alternate lower-force centre sliders, mixable across fingers (721558, 827290).
- **10-20 — the organization repo goes public** at github.com/svalboard/vial-qmk, with the
  svalboard.substack.com newsletter, first post "State of the Svalboard" (858959, 854046, 774811).
- **10-21 — why it is still labelled Alpha**: bootstrapping and SLA supplier risk, "the bar for me to take
  that Alpha label off is very high," and "I still need co-explorers" (300392, 816766).
- **10-29 — the durability answer for a commercial buyer**: 275 g per side, all PCBs professionally
  SMT-assembled, every board replaceable in under five minutes; first failure is likely magnet glue, then
  ESD to the optical sensors (808218, 916863, 075068).
- **11-15/17 — sample clusters go on sale** with the switch force-profile substack post, and the fingertip
  sizer PDF is published (787877, 201652).
- **11-20 — full colour customization ends.** Default becomes galaxy black or white silk cases with black
  clusters and keys, full colour key/palm sets an upcharge — to batch production and lock down magnet and
  mechanism parameters. Full-rig lead time is ~7–10 days but stock is nearly gone (611652, 425585, 486949).
- **11-26 — PMW3360 trackball firmware works**; the build emits both trackpoint and pmw3360 artifacts
  (405531, 781678). **11-27 — no integrated wireless**: the sensor LEDs need ~300–500 mW (833546).
- **12-09 — self-print kits go on hold until at least Q2 2024**, "too much distraction"; full builds
  continue (063346, 270668). **12-12 — standard builds move to galaxy black only** (158585).

### January – April 2024
- **01-02 — the $300 kit price is defended at length**: low-volume goods are priced on value, and the
  Datahand "was worth every penny of $1200 in 1995 dollars -- that would be ~$2400 today" (202677, 327337).
- **01-04 — first unit sold through the formal "Trackpoint Option"**; ~a dozen trackpoint Svals had already
  shipped in kit form. **No more split-key-colour builds without a substantial upcharge** (470022, 656104).
- **01-18 — the first official Svalboard Lightly ships**, after "fifty or sixty times through the wringer,"
  introducing **stainless steel towers** that Alpha owners can buy separately; launch post on
  r/MechanicalKeyboards, ~25 kits in the wild (863465, 152084, 540679, 097630).
- **02-14 — Hackaday feature**, "Inputs Of Interest: The Svalboard Could Be Your Salvation" (697130).
- **02-15 — the open-source position, in full**: "open source for customers — free as in speech, not as in
  beer." Kit and full-build buyers get all the STLs; EE hardware is deliberately closed, and Hackaday
  wording implying unconditional availability is corrected same-day (704192, 149846, 599017). **Orbital is
  not coming back in the near future** (960808).
- **02-27..03-07 — the trackball module is prototyped in public**: static-bearing "tentacle" mount, then
  Bosch Rexroth BTUs, then a parameterized 45° mount — "Finally nailed it!" (406884, 591986, 829064).
- **03-02 — trackball module pricing floated at $100 with static bearings, ~$150 with BTUs**, retrofittable
  to most existing builds, with **KiCad and the module design fully open hardware** (013514, 806559,
  265293).
- **03-02 — claussen quits his day job** (034148), and states the trial policy plainly: "It's literally
  cheaper to try and return a Sval after two months than it is to buy a Glove80" (452648).
- **03-05 — Alpha vs Lightly, officially**: geometry tweaks plus stainless towers, but "the vast majority
  of it is simply tolerance tuning to make Lightly viable for small scale serial production" — not worth
  upgrading for. Next kit batch slated late April (713587, 719080).
- **03-13 — owners get STEP files; the OnShape repo is not open**, though many subcomponents are; a reviews
  forum is created the same day (692496, 083599, 383726).
- **03-23/24 — dual trackball works on both hands**, gated on trackball PCBAs; ballpoint/pointball lands in
  `svalboard/vial-qmk:vial`, and **Orbital v2 touch modules arrive** for dev/test samples (252891, 441361,
  681034).
- **03-29 — trackball holder redesign**: asymmetric bearings and a **top-install sensor holder that deletes
  the bottom cover** — two fewer screws, FFC serviceable without pulling the PCB (389992).
- **04-11 — Orbital v2 is BLE-native**, 150 mAh in-case; 45 units of electronics on hand, and **the first
  1k-unit build needs a Kickstarter, ~5 months out** (945160, 169850).
- **04-13 — pointing devices become standalone store items**, priced the same bundled or not (213927,
  030064). **04-15/17 — a prototype slim low-profile 34 mm ball mount**, a build option or easy retrofit on
  the same sensor board and bearings (279192, 626837).
- **04-28 — a public commitment on trackpoint drift**: bad modules go to Sprintek, "worst case a new module
  source or SKU is needed, best case there's a FW fix" (734639). The build guide lands at
  svalboard.com/build and beep starts a video build guide (767258, 323044).

### May – August 2024
- **05-01 — a new PCBA batch ships**: post-processing fixes plus groundwork for **layer indication**, and
  **100% backwards compatible with Lightly** (103828, 144759).
- **05-08 — dual-trackball is added to the shop**; build time about a week (667803, 543720). **05-10 — an
  "Ultralightly" prototype**: 44 keys, "possible to get literally zero splay," ~8–10 g laterals (353249,
  487135).
- **05-17..05-20 — the centre-key mechanism search resolves.** A 1.7 mm offset steel slug at ~25 g binds on
  the south edge — "not good enough to make the cut" — and the winner is **a direct-mate 2 mm steel ball
  against the usual N35 cylinder**, ~1.2 mm travel, "prolly 28gf and insanely snappy," a trivial retrofit
  for self-printers (108811, 093376, 634493, 833325).
- **05-28 — the MCU redesign is announced** — moving the MCU out from under the pointing area to simplify
  assembly, open case variants and allow >40 mm balls — and it "definitely won't go out in kits before
  Sept, if not end of year." This kit batch gets slim thumbs with layer LEDs (232515, 444640).
- **06-02 — trackpads: "all boards from here on out have them"**, immediately qualified — the touch module
  is end-of-life and "If I can't guarantee a future supply, it's not a good idea to ship it" (068736,
  646016).
- **06-12/13 — layer lights become standard on all builds**, DIY kit included (681234, 773434). Licensing
  restated: "Open source SW for everything, open solid model files for customers, hacker-friendly but not
  open HW" (532718, 014656). The answer to "should I wait?" is modularity — "there's nothing cast in stone
  by hard tooling" — and the trial program is confirmed still in effect (863289, 747743).
- **06-30 — self-print kit orders close for the June batch and the listing moves to late August**; ~20 kits
  against ~15 orders, and regular full builds are *not* batched this way. An MCU shortage had already
  pushed kit shipping to ~9 July (710441, 586430, 538250, 958743).
- **07-03 — a new, smaller trackball sensor lands in `Pitched V3 WIP`** — "not functionally different, just
  a smaller shape" — so claussen can stop hand-soldering them; no impact on existing mounts (492900,
  624110).
- **07-08 — the new centre-key mechanism is shown on video** (youtube.com/watch?v=PPbxJTgOujs). **It needs
  all-new cluster plastics; the PCB is unchanged** — "no free tickets to 2nd/3rd-class lever utopia"
  (972733, 720421, 156466).
- **07-20 — an ultra-slim cluster prototype**: 0.5 mm less well-top travel, with **slugs in the clusters
  instead of magnets** to restore tactility — "Still in alpha but promising enough that I'm getting them in
  some hands" (337897, 786106).
- **Repo access rules, mid-2024**: the self-print repo is for kit buyers — DM claussen; buying an assembled
  board also gets the files and future updates; **the DIY trackball/pointer kit's Onshape repos are fully
  public** (178852, 612361, 431922).
- **07-31 — the new centre keys are already shipping** and are "fully backwards compatible with the
  standard finger PCBA," so existing boards can be upgraded (546204, 529398).
- **08-20 — "pitched v3 wip" is renamed svalball**: the new sensor is done and for sale, and the DIY
  "PCBA+cable only" option ships with the lens installed (966895, 500702).
- **08-22 — beep publishes the 47-minute kit build guide video**, youtu.be/fa_BZ1AKQVk — already behind the
  hardware (new thumb cluster, extra case screws, new key jigs) (532160, 715251, 241984).
- **08-23 — the pricing rationale, in full**: keyboard-only is $750, and the self-print kit exists "to
  allow people who put a low value on their time to have a way to get on Sval"; a shipping coverage map
  offers free shipping plus $200 off for the first order to actual Svalbard (255740, 951036).
- **08-29 — Shopify Managed Markets goes live**, calculating import duty and VAT at checkout with DHL as
  the only carrier — "painful margin hit but hey, I love you guys" (689427, 895618). A private channel for
  recent order placers is populated by hand (279037, 782460).

### September – December 2024
- **09-04 — the Blood Promise**: "my Blood Promise to open source the full hardware if this business stops
  operating permanently," motivated by Datahand orphaning its users. Core hardware stays closed while the
  company operates; firmware stays open, and prebuilt buyers get repo access too (139495, 808841, 269974).
- **09-13 — all new sample clusters ship with the tipping centre key mechanism**; the stash of old ones ran
  out (408015).
- **09-21 — the self-print kit's purpose, stated outright**: it exists "to ensure that the promise of a
  self-maintainable, self-repairable device remains authentic", is "not a very substantial portion of
  revenue" and is "deliberately not presented as a consumer option" (502130, 049004).
- **10-04 — the October batch closes early** on long-lead part stock; orders are refundable until they
  ship (266612, 456151).
- **10-08 — stiffer and lighter side-key STEP files hit the repo** within an hour of being asked, and the
  open palm-rest repo is reworked around a tripod mount with a single front post (994556, 005322).
- **10-09 — 0.9 offset tipping centers become the shipping standard**: "we'll see over a month if anyone
  finds it too light. I think it's fine." Employers do buy these — "Lockheed, Facebook, Google, etc"
  (731379, 073278).
- **10-15 — the modularity doctrine**: interconnects aren't meant to change and clusters and pointing
  devices swap in — "It's a Ship of Theseus sort of affair"; "My goal isn't repeat sales, it's to create
  the ne plus ultra of low-effort, hands-down input that will live forever through repairability and
  modularity" (187156, 589875).
- **10-22..10-24 — the next self-print kit batch is planned for late December 2024**; prebuilt lead time is
  1–2 days pending a trackball PCBA restock, with a new sensor vendor being verified (888650, 312203,
  772448).
- **11-29 — no Black Friday sale, ever**: "American consumerism doesn't change my economics"; "Sales are
  for people who keep inventory." Ship dates live at the top of the product page; the UK kit is £292
  (698763, 326289, 884929, 797564).
- **11-30..12-06 — the trackpad is blocked on glass with a ~12-week lead time**, "Not expecting anything in
  until Jan," later "an easy swap or add-on later." **MCU 3.1 ships now and already supports it** (595520,
  357877, 476928).
- **12-02..12-06 — repo access is manual but immediate on order**: files arrive as soon as you buy, and
  **pre-built buyers get identical access** — "Just a bigger box." **Mechanical files only, not Gerber**;
  "If I stop operating the business I'll release the EE too, but I don't plan to do that" (027072, 764862,
  761234, 864296).
- **12-04 — the bootstrapping position**, against a long "why not open source / why not Kickstarter" push:
  bootstrapped "to maintain my own freedom to design, build and sell whatever TF I think is cool without
  the constraints of investment capital"; Kickstarter — "Fuck nooooooooo 🤣" (567774, 548028).
- **12-16 — a six-key "flower" thumb cluster prototype**: six keys at individually tunable radii and
  angles, 0.4 mm magnet offset, 0.5 mm less travel — mechanical mock only, "literally unrouteable in PCB
  form in this configuration" (080916, 929686).
- **12-21 — the next self-print kit batch moves to late March 2025**, cutoffs announced ~a month ahead
  (858177, 579411). **12-29/30 — touchpads sell out and are pulled** pending a firmware/hardware fix on the
  latest Azoteq sensor batch (301642, 248228). **12-30 — CA glue gets a 3-month max shelf life** (656475).

### January – April 2025
- **01-29 — MX switches on the centre key: "Absolutely not under any circumstance."** "It's antithetical to
  the entire purpose of datahand, ergonomically," and it wouldn't fit — "spacing/splay is *everything*."
  The **$15 sample cluster** is the sanctioned way to feel the switch (178001, 663517, 355753).
- **01-29 — no cheaper PCB-less tier is planned**. **"Solid model files are always available to customers
  for their personal use. The goal is a product that is maintainable in perpetuity"** — and alpha owner
  pekudzu counts thumbs, baseplate, tipping clusters and metal towers as the only breaking changes so far
  (595925, 163079, 148028).
- **02-04 — US tariffs on Canada and Mexico are delayed 30 days**; claussen: "the hassles of small intl
  biz" (533006, 684436).
- **02-13 — prices did not change**; a UK buyer's apparent ~£100 drop was Shopify switching from
  tax-inclusive display to itemized VAT and duties (413182, 248897).
- **02-24 — a small drop sells out in 5 minutes**, and a contributed split case lands in the repo (720789,
  392040).
- **02-25 — a metal framework is mandatory for mounting**: plastic with an insert "is simply not strong
  enough" (997940). **02-28 — March brings a DIY kit restock, not a new release** (082762).
- **03-01 / 03-06 — repo access is keyed off the GitHub username field**, with a note on frequency added to
  the kit page and a permissions sweep run the same morning; self-printers want the cheaper "bare module"
  touchpad option, not the $125 assembled variant (585092, 977291, 165945).
- **03-10 — the March kit batch closes; the next target is late June.** "There's some tension between full
  build production and kits, and I honor full builds (and R&D!) as a higher priority" (153392). A
  **printable travel-case bounty** is posted, paying a qualifying community design the designer's kit
  price back; nothing submitted by 03-25 (125696, 755178).
- **03-20 — zero stock by policy**, ~1 week lead time on prebuilts; carrier plates are on a ship, "can't
  promise anything given customs chaos" (760810, 977983). **03-21 — Canadian duty charges look like a
  Shopify Managed Markets HS-code artifact**, not real duty (642985, 875533).
- **03-22 — the shipped default DH-QWERTY layouts are pinned**, reachable via the `!default` bot command
  (862046, 663297).
- **03-25/26 — the electronics are not open source**: "It's the only way to keep the business alive 🙏🏻" —
  the trackball board being the exception. The trial program, surfaced for a buyer balking at $1,050, "is
  really just a return policy" (852327, 449299, 739182, 846865).
- **03-27 — wireless is a no, on the record**: "Power consumption is impractical for any formal wireless
  product" and "wireless products are a nightmare for a boutique business." The YouTube wireless demo
  people keep linking is claussen himself (376303, 807461, 489326).
- **03-29 — the March kit batch is late on cables, not plastics**: "We got hosed on USB cable delivery by
  our brilliant global trade war." The magnetic breakaway cables aren't substitutable, and kits land from
  04-08; repo access runs as a manual weekly GitHub-invite sweep (159996, 808030, 782091, 477551).
- **04-05 — STEP only, no STL export**, for robustness and labour reasons (730007).
- **04-06 — the bus-factor question is asked directly and answered partially**: phreaker holds the
  schematics ("It isn't 1"); claussen declines a public discussion of "where and how I keep
  specific-discipline source materials secure... But rest assured, it'll be okay" (127088, 623553, 526487).
- **04-10 — RGB layer-indicator LEDs are already in all current thumb clusters**; older boards can get
  newer thumbs by arrangement (520725, 334775).
- **04-25/28 — magnets become a shop SKU**, replacing AliExpress sourcing, and a trackball holder revision
  is in flight — by 05-10, "the latest holder design is really nice" (957018, 897856, 507518).

### May – August 2025
- **05-04 — shop prices are duty-inclusive via Shopify Managed Markets**, "across a few dozen countries so
  far." India is the exception, quoted ~50% duty plus ~50% tax, $1300 → $2500 (244925, 813510).
- **05-06 — a new palm-rest prototype: a 35A additive silicone print** from a UMich lab, "definitely soft
  enough to be meaningfully compliant." Production is the blocker — "Domestic casting/molding is a joke
  price wise, and with China at 3-4x total cost vs pre-insanity times might not be viable either" (658123,
  875965).
- **05-13 — second-hand buyers can get repo access**: "The project is open source for customers. DM me to
  discuss" (169832). **05-17 — UK VAT is prepaid at checkout**, invoices via support ticket (545454,
  422676).
- **06-07 — the parts repo stays customer-only** because "there are thousands and thousands of hours of
  design time that went into it"; **the firmware is FOSS** and fully public (667508, 917013, 300161).
- **06-08 — a trackball holder upgrade comes to the shop** for owners of the older equal-height-bearing
  holder (763428). **06-10 — sharing STLs with second-hand owners is a licence violation** (446932).
- **06-26/29 — repo and Supporters-role access is a manual ~weekly batch**, answered by the `!access` bot,
  with the backlog cleared 06-29 (207337, 341650).
- **07-04 — default tenting is "about 15 total" degrees**; Canadian pricing is quoted at $600 CAD for the
  kit and $1,464 CAD assembled (308968, 878476). **07-07 — the silicone palm rest gets a video**, still not
  purchasable (803297).
- **07-08 — built to order, zero stock**: "I operate on a lean mfg/zero stock basis to keep design and
  manufacturing in close sync" (650470). **07-16 — the ~3-week prebuilt lead time on the site is
  accurate**; kits are batch-shipped and much slower (144209, 086328).
- **08-01 — shop prices include duties and taxes** and packages go "customs pre-cleared to most countries"
  (083211). **08-04 — self-print kits ordered now "will all ship by the end of September"** (881926).

*No distillation covers 2025-08-10 through 2025-10-17; the timeline has no entries for that window.*

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
