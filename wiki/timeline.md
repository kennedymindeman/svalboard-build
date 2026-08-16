---
type: Timeline
title: Timeline
description: Dated Svalboard product news, policy and firmware announcements from November 2025 to August 2026.
tags: [svalboard, discord, timeline]
source: "discord #general 1124364902811844739, 2025-10-17..2026-08-15"
---

# Timeline

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-1124364902811844739.jsonl`; agreement counts are floor estimates.

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
