---
type: Reference
title: Suppliers and parts
description: Part numbers and sources for magnets, bearings, balls, BTUs, cables, adapters and accessories.
tags: [svalboard, discord, parts]
source: "discord #general 1124364902811844739, 2025-10-17..2026-08-15"
---

# Suppliers and parts

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-1124364902811844739.jsonl`; agreement counts are floor estimates.

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
