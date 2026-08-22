---
type: Reference
title: "Svalboard Discord #general — overview"
description: "What the Svalboard Discord #general channel is across three years, how the product and the recurring voices changed, and what the distillation does not cover."
tags: [svalboard, discord]
source: "discord #general 1124364902811844739, 2023-06-30..2026-08-15 (gap 2025-08-10..2025-10-17)"
---

# Svalboard Discord #general — overview

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-1124364902811844739.jsonl`; a few 6-digit suffixes collide in the 43k-message export, so disambiguate by date if a lookup returns two hits. Agreement counts are floor estimates.

## Source

Discord channel `1124364902811844739`, distilled by LLM passes over
`discord/raw/channel-1124364902811844739.jsonl`: seven chunks covering 2025-10-17..2026-08-15 (8,921
messages, distilled 2026-08-15), 25 backfill chunks covering 2023-09-07..2025-08-10, and four chunks
covering 2023-06-30..2023-09-06 (1,776 messages, the channel's founding months, distilled 2026-08-22),
merged. Coverage is 42,861 of the channel's ~48,135 messages; captured **2023-06-30..2025-08-10** and
**2025-10-17..2026-08-15**, uncovered **2025-08-10..2025-10-17**. Agreement counts are floor estimates
(who spoke up), not polls. Advice changed a lot over three years, so bullets say what changed and when;
read anything undated as "as of the end of the range."

## What the channel is about

The general / open channel for the Svalboard, a DataHand-inspired finger-keywell keyboard with
magnetic-retention optical switches and integrated trackballs, designed and sold by **claussen** (Morgan
Venable, founder; 20 years managing SW/EE/ME and AI research at Google — 399551, 741204; identity
inferred from 634238→739891). Not the support channel: build problems go to the closed
troubleshooting/supporters channel, layouts to the layouts channel, orders to tickets (304503, 843620,
597625, 879803). Content: pre-purchase questions, self-print advice, trackball debate, fit, firmware, mods.

The mix shifts with the era. In 2023-24 it is half R&D lab notebook, half new-owner fitting clinic —
claussen posts an experiment most mornings and answers every question himself, being the only person
who has built more than one board (566993). By 2025-26 it is mostly pre-purchase interrogation,
adaptation diaries and firmware Q&A answered by volunteers, with claussen's prototype stream
continuing alongside (109949).

## Era guide

Where a cited message sits in the product's history. See [timeline](/timeline.md) for dated events in
the 2025-11..2026-08 span.

- **2023-06..09 — the channel's founding months.** claussen splits #general off from the lalboard
  world on 2023-06-30 because "there are now likely more Svalboards in the world than lalboards" (569192);
  rigs are still ESP32-based until the RP2040 MCU boards land 2023-08-18 (049660, 726786), palm rests are
  thermoformed by hand (428712), self-print kit orders open 2023-08-25 (995149), and Dale — the DataHand's
  inventor — joins on 2023-08-01 (173607). No shop pointing device, no public firmware repo.
- **2023-09..10 — hand-built "Svalboard Alpha."** One-man Prusa MK3S print farm, units announced with
  "Typed on <user>'s Svalboard Alpha!" (072201, 553578); no shop link (355796), no trackball or
  trackpoint product, ~15 DIY kits outstanding (063441); clusters named by slider-offset generation
  ("your clusters are from the 0.9 offset era", claussen 524166).
- **2023-10..11 — repo and trackball groundwork.** The firmware repo goes public, the trackball PCBA is
  designed, fabbed and first booted, and the fingertip sizer is published (262486).
- **2023-11..2024-01 — deep alpha.** Kits $300, assembled ~$700; "Svalboard is a business... you're
  paying my meager 'salary'" (claussen 202677). Still **no trackball product** — trackpoint add-on or
  DIY ball mount, **OrdovicianOperand** farthest along (741610); ESP32 boards still in the field (010048).
- **2024-01-18 — the first official Svalboard *Lightly* ships** (863465); the Alpha is retired and
  flash-sold (182848), ~25 self-print kits are in the wild (097630), trackpoint still needs a
  hand-soldered resistor mod.
- **2024-03-02 — claussen goes full-time**, having quit his day job a week earlier (034148).
- **2024-03..05 — the trackball arrives.** Dual-ball lands 2024-03-23 (252891) and reaches the shop
  mid-May (435026); phreaker calls it "a fairly new offering" (757376). Firmware `v0.002sv` fixes
  Sprintek trackpoint drift (141093); clusters are Lightly FDM V1.1.
- **2024-06..07 — dual-ball becomes the majority build** (673097), layer lights standard (014087),
  recommended balls **34 and 40 mm, not 44** (059986); self-print moves to v1.2 while the guide stays
  on v1.1 (741568) and kit shipping stalls on an MCU shortage (538250).
- **2024-07..09 — the center key changes.** Tipping center-key rollout (546204) while sliders are still
  in sample boxes (551101); "svalball" naming (966895); 40 mm standard (780924); prebuilt $750 / ~$850
  dual-ball (951036), $975-1,050 by late August (030001). Tipping becomes standard on sample clusters
  (408015), sliders deprecated (348826), 34 mm phased out (753704).
- **2024-09..10 — Keybard appears**, "a work in progress" (081664) alongside Vial, written by
  **sixtysixone** (850257); PMW3389 sensors (931986), 1-2 day lead time (312203), repo access still a
  manual claussen ping — "I still need an automation for that" (162409).
- **2024-11..12 — shipping product, still one man.** "This is a one-man project on the hardware and
  commercialization end of things" (280177), Discord ~1500 (978570); MCU 3.1 ships (476928); the
  trackpad is blocked on a 12-week glass lead time (595520); boards report `v24.09.05` / `v24.10.24`
  (983810). claussen pings **Ben Vallack and gets no reply** (255263), so read "nobody has reviewed us"
  lines here as time-bound.
- **2024-12..2025-01 — Keybard becomes the recommendation** (281282), firmware moves to prebuilt uf2s
  on GitHub Releases (307413), and the touchpad reaches early release then is pulled over a
  sensor-batch defect (457309).
- **2025-02..03 — pre-sales peak.** Order numbering crosses 2000, though the counter eats "every beer,
  every customer service ticket" (873743); firmware is `v25.02.12` (159487); "We generally run zero
  stock, lead time is about a week right now" (760810).
- **2025-04..06 — tariffs.** claussen, 2025-03-29: "We got hosed on USB cable delivery by our brilliant
  global trade war" (549090); kits land from 2025-04-08 (782091); the Bambu A1 mini jumps to $359
  (620288), breaking the standard "just buy an A1 mini" advice (676113); the narrow finger cluster is
  new (116024).
- **2025-06..08 — steady state before the gap.** Prebuilts made to order at ~3-week lead time (643010),
  kits batch-shipped with the next promised end of September (881926), trackpad shipping "for a while"
  (151208), and no firmware release between `v25.02.12` and the gap (343041).
- **2025-11..2026-08 — the Keybard/Viable era.** Ben Vallack's November 2025 review lands and drives a
  new-buyer wave (366059, 244480, 635129); firmware is the "Viable" QMK fork and its Rust successor
  (601559, 067866); a new square baseplate is announced (833387, 546979).

## How the recurring voices changed

- **2023 — claussen answers everything**, posting 406 of the first chunk's 1,287 messages, because
  nobody else has built more than one board (072201). Around him: **pekudzu** (Australia, first ABS
  self-print, steno), **ang3l12** (board arrives 2023-10-17), **𝕯𝖆 𝕯𝖗𝖆𝖌𝖔𝖓** (German buyer, later a CNC
  aluminium case), **EricaLina** (Hands Down, OLEDs), **myxfit** — who is **JesusFreke, the lalboard's
  designer** (156532) — **Atomic** (first complete self-print build, 2023-10-16), **OrdovicianOperand**
  (early trackball engineering), **wejn** and **gk** (20-year DataHand owners), **Moo** and **wolfwood**
  (QMK/PS2 internals), **Manna Harbour** (Miryoku author), **DanWest**.
- **2024 — the volunteer bench forms.** **Raven System**'s board arrives 2024-02-03 and he becomes the
  docs voice (pointing-device docs 700511, svalboard.com/scroll 091048). **Cyrus** appears in early 2024
  as a DataHand user shopping for a replacement, gets his Sval 2024-05-07, immediately re-CADs the
  trackball holder, and by 2025 is the hand-anatomy authority ("after, over time, tearing *all* the
  sagittal bands on both hands!" 852497). **phreaker** joins 2024-02-05 as an ex-DataHand Dvorak user on
  a Glove80, sent from the Glove80 Discord (569331), and **only gets his own Sval on 2024-02-16**
  (482953) — a very different role from later windows.
- **2024-04 onward — phreaker becomes the firmware voice**, ~40% of messages by that April (155649) and
  disclaiming affiliation in every window since: "Claussen is the kahuna, I'm just a software guy here
  having fun" (887673), "I am a volonteer as a firmware dev. I do not represent Svalboard, claussen, or
  anyone except myself" (876133), through to "I am not part of Svalboard the company" (532992) in
  2025-26. claussen credits him with "basically all of the FW awesomeness other than the initial launch"
  (439051); editor.svalboard.app is his (234400). Other tool authors and outside contributors arrive
  from late 2024: **whitelynx** (an RMK port, 583169), **drpngx** (first outside firmware PRs, 694214),
  **JeremyC** ("I am the original author of Auto Shift" 877271), **RufusRed**, **River**, **Invi**.
- **2025-26 — a four-voice core plus staff.** **phreaker** (highest message volume, 316439), **claussen**
  (product, policy, print tolerances), **Cyrus** ("resident fit nerd," UK; keeps UK stock of balls and
  sample clusters 565699; designed the mini/triangle palm rests 350488), **Raven System** and
  **Hugin&Munin** (experienced self-builders who field most newcomer questions), plus **lumbduck** as
  staff — sales, shipping, assembly (551636, 043542). Also **HazardousChurch** (gaming/mounting mods),
  **gyordanov**, **Atto**, **Lydie**, **ziasquinn**, **robflop**, **Moo**, **flesh.priest**, **xsznix**,
  **lax3r**, **randomized_beaver**, **Lima/nocoffei** (firmware mods), **CwD**, **Zach Valenti**.
- **Attribution decays backwards.** Deleted accounts render as **"Deleted User"**, heaviest mid-2024 to
  early 2025: a force-and-materials questioner in 2024-06 (417538), 72 messages of 3D-combo/numpad
  experiments in 2024-10, a long automouse debugging thread in 2024-11 (436605 through 774280), and much
  of the best newcomer content in 2025-02/03. Dual-ball enthusiasm (920627) and Colemak-mod-DH roll
  claims (296765) are unattributable for the same reason.

## Gaps

- Channel name is inferred ("general"); the export carries ids only, and claussen = Morgan Venable /
  founder is inferred, never stated outright.
- **6-digit ids collide** in a 43k-message export — `608671` appears on both 2024-04-16 and 2024-05-02 —
  so disambiguate any lookup by date.
- **Attachment URLs are expiring Discord CDN links**, the largest single loss: claussen's prototype
  stream is photo-with-one-line-caption for three years, so fit photos, PCB damage, V1-vs-V2
  comparisons, key/palm-rest studies, Lydie's foam mod and the whole trackball design arc rest on
  surrounding text (906890, 588691, 716683, 368980, 283615). Some claussen messages are empty because
  they were image- or poll-only, including the 2025-05-02 colour poll (525067).
- **Many answers point outside this export** — troubleshooting, layouts, mounts, supporters, firmware,
  order-holders and tickets channels, plus bare `discord.com/channels/...` permalinks and pins this
  export cannot resolve — so their resolutions aren't visible, including the firmware RC's new UI and
  the "new square baseplate" announcement (577633, 833387, 279037, 879803, 994068).
- **Firmware version names are loose and were never reconciled** in-channel: 2023-24 builds are one-off
  files claussen hands out as Discord attachments with no version at all (819109), then self-reported
  strings (983810, 159487, 343041), then "latest FW", "11-01 sources", "the x-mas release", "viable",
  "viable-rs", "viable-qmk" (601559, 347977, 533592); viable-rs status here is as of 2026-04-02
  (067866). Open bugs at the end of the range: the Mac/Windows wake-from-sleep failure (990695) and the
  random layout reset, with no root cause (216251).
- Prices, lead times and sourcing claims (BTUs, Nanuk, bearings, sample-cluster shipping, printer
  prices) are user reports at a moment in time across several countries, and are unverified — as are
  external product claims (Sanwa/Aramith ball quality, P2S/X2D specs, the N35 working temperature
  840698, the India duty screenshot 813510, Kinesis volumes inferred from eBay serials, and the
  CharaChorder litigation claims dataangel searched for and could not find 963694) (033181, 458024,
  496130, 194495). Repo-sharing answers come from phreaker and Zach Valenti, not claussen (540490), and
  polling-rate numbers are phreaker's own estimates (789978).
- **Pre-2025 hardware specifics are history, not guidance**: slider offsets and the snug/wide/backset
  vocabulary, N52-vs-N35 magnets, the 52 mm ball ceiling, 34/40 mm as the ball default, V1.1/V1.2/V1.3
  cluster paths, the Azoteq trackpad path on an EOL part (068736), the trackpoint resistor mod, Vial as
  the only config tool, and the "Alpha"/"svalball" labels (524166, 059986, 966895). Slider weight
  figures (10/20/25-30 g) are claussen's chat estimates, not measurements.
- **Threads that open and never close in-window**: "trackpoint fully validated in about a month"
  (939304); trackpoint drift (137472) and wejn's KVM boot failure (510400); trustno1's runaway South key
  with key, lube and PCB all swapped (427940); Cyrus's HID-only enumeration / VID-PID question (726208);
  fred's magnetic-cable brand question (708481); preland's Plover-on-Linux question (640966). Whether the
  square-nut baseplate retention (546979) actually shipped to the repo is not stated in-channel, and
  phreaker's "how to buy a Svalboard" guide (475209, 612538) was never published in the channel.
