---
type: Reference
title: Open questions
description: Contested or unresolved topics across three years — wireless, bearings and ball size, openness and printing rights, layouts, palm rests, firmware state.
tags: [svalboard, discord, open-questions]
source: "discord #general 1124364902811844739, 2023-06-30..2026-08-15 (gap 2025-08-10..2025-10-17)"
---

# Open questions

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-1124364902811844739.jsonl`; a few 6-digit suffixes collide in the 43k-message export, so disambiguate by date if a lookup returns two hits. Agreement counts are floor estimates.

Each item gives the arc: when the debate appeared, how positions moved, where it stands now.

## Pointing devices

- **Wireless** — asked in every window since 2024-07, never answered yes: "Not for a very long time if
  ever," because sensors pull ~500 mA, key scanning never sleeps "because QMK is dumb," and "QMK will never
  be wireless friendly no matter what we do"; the standing offer is **magnetic cables as "about 80% of the
  benefit of wireless, without all the drawbacks of BT flakiness"** (960115, 222516, 846707, 328257, 056678,
  583647). Adapters cost you Vial, and Cyrus's maintenance objection went unrebutted (439824, 982840,
  136041). Unchanged in 2026: use a **BT600** with a battery bank or **SterlingKey Hawk** over 2.4 GHz
  (929340, 211439, 367157, 243827, 752020).
- **BTUs vs static bearings vs rollers** — three years, no convergence. 2023-09 to 2024-02: statics win on
  feel, BTUs are "much much much more expensive" but sworn by, bulky and too noisy, vi wants ploopy rollers,
  Diitsuku *likes* the noise, and rollers are ruled out because their surfaces "are never well polished"
  (354386, 884590, 607424, 957450, 089546, 329309, 981071, 526234). Then controllability (the ball goes
  "almost too smooth" and trips the mouse layer), broken automouse, the 34 mm BTU's free Z spin, and another
  three-way split in 2025-07 (637898, 170390, 660288, 239631, 364344, 651879). 2026 reframes it as wear:
  "BTUs are wear items, much more so than statics" vs "statics make the ball a wear item" (149142, 879697,
  548242, 182447; AlmostRandom's ceramic-BTU synthesis stalled at MOQ 1,000, 567464, 265021).
- **Ball size — settled at 44 mm after two years of dissent**, which ranged from the 34 claussen shipped to
  the 55 OrdovicianOperand swore fit thin thumb clusters, with serp's "what is a good starter ball size?"
  going unanswered (656808, 818354, 427951, 189039, 492404, 412757, 838589, 215092). By 2025-05 claussen was
  back to 44 and measurably more accurate than on 52 or 57 (767592, 534927); 2026 is near-unanimous, "Go
  with 44" (751734, [pointing-devices](/pointing-devices.md)).
- **Trackpoint drift and trackpad limits.** Drift is open since 2024-04: Sprintek owed an analysis, nobody
  could disable baseline calibration, phreaker won't paper over a hardware defect, and dual PS/2 trackpoints
  stayed unsolved in QMK (734639, 175481, 395092, 455683). Trackpads are second-best as long — the Azoteq
  pads were phreaker's favourite and already EOL in 2024-06, gestures went unbuilt, and "most who use Sval
  land in the trackball/trackball setup" (007913, 107264, 049088, 996484, 729100). 2026 has only
  workarounds — a reversal for claussen, who called trackpoint "the right solution" before trying a
  trackball: "I dunno how you people do this" (090304, 180340, 635257, 690906).
- **The second ball: scroll, twist and 6-DOF.** "It's not like you scroll and move your cursor at the same
  time" against "CADing is a ton of pan + point"; twist died on cost, since "even their fancy new shit
  requires two sensors" (682315, 220200, 381575, 751678, 718599, 842226). SpaceMouse, proposed since
  𝕯𝖆 𝕯𝖗𝖆𝖌𝖔𝖓's 2023 module sketch, is shot down every time — claussen built it, "not worth the extra
  complexity, bulk and cost," and phreaker's firmware "really doesn't work well with the sval" (094464,
  303550, 448128, 789649, 238339, 150474). Dual ball is "the Meta" by 2026; the joke answer is "two balls,
  a gaze tracker, a foot mouse and a kick drum" (634085).
- **Holder geometry, and whether you spin the ball.** Cyrus wants zero ball movement relative to the
  sensor, claussen's rule is "as soon as you clamp everything goes draggy," and the 2025-01 keeper design
  was unfinished at window close, so holder details from then are superseded (568059, 510166, 073846). Who
  the ball is for settled it: phreaker's "Spinning the ball is pretty essential" against Cyrus's "these
  keyboards are assistive as much as they are ergonomic," which redirected the design toward the 2026 holder
  revision (509288, 409923, 585459). Adjustable acceleration curves still don't exist (753360, 372416,
  354941).

## Keys, clusters and mechanism

- **Double south (2S) and double north.** claussen daily-drove 2S in 2024-06 and ruled it out by 2024-09 —
  "The 'all motions distinct and orthogonal' aspect of DH is more important than we give it credit for" —
  while phreaker, who had a full 2S board, "wasn't using them," and Cyrus found hitting 2S instead of S on
  the way back from the trackball "pretty maddening" (467990, 112938, 842725, 324619, 151824, 644245).
  Resolved commercially: by 2026 they are sold separately, unlisted and experimental (876170, 990684).
- **The thumb-down key**, loudest complaint of 2024-05: only actuable at the tip, "too stiff and has too
  little travel for the detent to make sense," "the single most underwhelming feeling key" (890763, 661608,
  496360). claussen closed it on data — a **1–2% report rate**, and lengthening it needs a new thumb PCBA
  (945814; Dale's off-center-bar-with-magnets explanation, 834043).
- **More keys, of any kind, keep being refused**: a north thumb key ("I do not think there's a lack of
  enough keys on DH/Svalboard"), dataangel's thumb column ("the impact on trackball fit would be beastly"),
  and 45° levers hitting two adjacent keys, blocked on space (618048, 738048, 742324, 535016, 719890,
  845043). **Traditional switches** are all too big (797349), and **multi-stage keys** died because magnetic
  force drops as you press, making a 50–60 g tact hard *not* to actuate (526079, 883890).
- **Key weight, fixed clusters, and the 6-key cluster's not-quite-death.** Lighter N than S gets agreement
  in principle plus a warning about false N activations, heavier magnets get "too stiff is BAD," and a
  fixed-cluster model met the rebuttal that "the bulk of [cost] is actually the key mechanisms" (599548,
  473822, 823113, 583632, 289159, 733678). Consensus killed the 6-key cluster in 2024-12, but Cyrus
  daily-drove one and concluded "so it's not fully, 100% dead" — hence 2026's unlisted 6-key PCBAs (108817,
  715659, 188873).

- **Hall-effect sensing instead of optical: explored in 2023, never closed, never started.** claussen
  hand-built a scattergun test PCB — "just chuck various sensor footprints all over the board and see what
  sticks" — and kept hunting parts through 2023-09: Allegro right-angle SMT hall switches for sensing at
  90° to the Z axis, and TI's `TMAG5273` 3-axis part, "super low power considering what it does", though
  that would mean "one I2C device per key, basically" (725761, 491929, 610664). **The honest benefit list
  is short**: immunity to ambient IR from sunlight, which all-black units don't suffer anyway; somewhat
  lower power; and a simpler key with no flag to print, freeing up material choices. It is **not faster**
  than optical — hall sensors are slow to power up — and getting a consistent, tunable actuation point is
  the hard part (921553, 212576, 324687, 344782). Against it: hall sensors are themselves ferromagnetic
  and can drag on the mechanism, "Optical is impressively affordable", and claussen refuses to trade away
  independent sensing — "All keys should be independently senseable". His estimate: even at two sensors
  per cluster it is only 2-4x the cost of optical, but it is "a new key architecture that would probably
  take me a year to work out given that the existing design is tried and true and shipping" (632551,
  681819, 687908, 795284, 200221). **The physics were checked and they work**: AlmostRandom modelled the
  NSEW magnet pairs in magpylib — the "SHIT - Svalboard Hall-effect Integration Testbed" colab, at
  colab.research.google.com/gist/anderso/8e8935f7a289ca38f7ffb2750c3ce2c4/sbheit.ipynb — getting 2242
  resting versus 2130 triggered for one switch, which claussen read as "about 10 counts at 8-bit
  resolution, not bad"; replacing the fixed magnet with a **steel cylinder** came out of the same thread
  as a way to cut the standing field (465342, 206608, 409903, 067483, 424646). Historical note from Dale,
  the DataHand inventor: **hall effect was DataHand's preferred mass-production path**, because LEDs and
  phototransistors of the era had durability problems, and it was blocked by a Russian patent they could
  not license (130287).

## Firmware and configuration

- **Who owns the mouse layer, and should it be automatic at all.** 2024-09: phreaker infinite timeout,
  claussen 500 ms for CAD; 2025-02 makes it philosophy — "Layer 15 isn't a normal 'layer' on sval. Let the
  system manage it" vs Cyrus's "You already know that I disagree" — and JN concluded a snappy mouse→typing
  exit might be "*unsolvable*" (150185, 259947, 855018, 518198, 493966, 499694, 601680). Live in 2026 as
  **should scrolling activate the mouse layer, and can the mouse be disabled per layer for gaming?** —
  unsupported, and such toggles belong on a config page, since ~70% of support requests are accidental
  setting changes (920074, 1094, 358624).
- **Sensing that a finger is on the ball** is the hardware version of the same problem: a load cell under
  the holder, capacitive sensing through a metal ball, electroplating a normal ball — all vetoed if they
  need a press ("Trackballs are to be seen not heard") or real investment (888827, 936714, 169994, 346117,
  424306). Still tinkered with in 2026, where phreaker says layer-15 binding already solves it (932, 845154,
  199725).
- **Vial vs VIA vs vanilla QMK vs a fork** — two years of argument, settled by fiat. brc rage-quit VIA/Vial
  wanting `qmk flash`, ccotenj argued the product view ("many of us 'just type'"), and claussen's answer was
  "you can run whatever the fuck you want"; 2024 adds "Via requires reflashing, it's way harder to get
  started with," Raven System bailing to plain QMK, phreaker declining mainline QMK (342928, 154255, 229160,
  683620, 045650, 407508, 424202). 2026: Svalboard keeps its fork and Keybard is the tool
  ([firmware-and-config](/firmware-and-config.md)).
- **Firmware state that only a power cycle clears.** The 2026 report is **random layout resets to the
  flashed default** — reuven, Ben Vallack and Lilijoy, always after a power cycle, unexplained ("cosmic
  ray?"); export your `.vil` (777030, 294090, 364567, 216251). The backfill has no EEPROM diagnosis either,
  only jacg's never-reproduced stuck key-repeat and wejn's board coming up dead behind a KVM (500198,
  189963, 510400).
- **Waking a sleeping host** — fifteen months open. 2024-11, ampleyfly can't wake Windows; claussen "I've
  had issues with QMK on this as well, very curious," the QMK FAQ entry the only lead, and disabling
  Windows power-off didn't help (794186, 253235, 620706). By February 2026 it covers Macs too: trackball
  motion never wakes the host, keypresses sometimes do after 4–20 s (041297, 533592, 990695).
- **Layer indication on the board** — refused in the first window, never replaced. EricaLina's 128×64 OLED
  met refusal on power, cost, assembly and yield, and on principle: claussen gets "a lot of cognitive load
  from up/down looking," and wants a trainer, not an indicator (423007, 066992, 798564). A decal plate,
  OLED/e-paper and a live-map CLI all went unbuilt (185628, 827034, 259165); in 2026 there is still no
  layer-indicator app, only drpngx's thockflow (923196, 136922).
- **Chording and steno** — recurring, hot, never tested at length on hardware. pekudzu's 2023 critique is
  that CharaChorder has no stenographic *theory*, so `D O G` and `G O D` collide; claussen tempers it, then
  in 2024-08 doesn't: "CC approach is gross and dumb IMO srynotsry." Lord Streak, the first actual chording
  user through the channel, found the server "a lot more hostile towards CC than I'd expected" (779914,
  387018, 749459, 145967, 409138, 002293). On the Sval, "North combos are iffy, South combos are great," but
  claussen calls the area academic (930405, 652019, 046191, 682894).

## Openness, price and printing

- **How open is "open source"?** — reappears yearly, answered the same way. 2024-01 it is a docs complaint
  (the Hackaday piece omitted that access comes only after buying), fixed in documentation, not licensing
  (479391, 824404). 2024-03 is the real thread: Rudolf Adamkovič pushes full FOSS, phreaker and Raven System
  defend the **"death pact"** ("If i ever cease operation, I will fully open source everything"), and
  claussen states the constraint — "I can't afford direct competition right now… If [the market] will
  legitimately support an ecosystem of more-than-one full-time datahand architecture keyboard designers,
  ***I want to live in that world***" (818321, 526666, 627099). 2024-04 states it flatly — firmware open,
  schematics closed, the rest with purchase — and disagrees only on whether it matters (594308, 958899,
  728232).
- **Print services and third-party printing.** chorf asked in 2025-04 for a third option between owning a
  printer and a print service; phreaker: "No, and I think it'd be frowned on," softened to "Only with
  claussen's blessing and if you were local," and claussen never answered directly (997023, 034052, 490482,
  059174). The 2026 reading is the same and no more official: sharing files with the friend who prints for
  you is fine, a side business is not, access is permanent unless you transfer the board, and reselling
  builds for profit is discouraged (540490, 095656, 836477, 757222).
- **Is the price defensible, and is the kit worth it?** — asked yearly against a new comparison, always
  answered on economics: "$700 is peanuts" next to a senior dev's lost time, a 50% discount can lose money
  on physical goods, and the PCB-only option is declined because "The price is more the 10k hours of design
  work and refining than the raw materials" (503628, 638337, 571594, 115156, 367611, 583724, 018573, 041866,
  865248); kit vs prebuilt splits on prior printing experience, not budget (320835, 339314, 922536, 460639,
  958976). 2026's comparison is the Azeron Cyborg II at ~4× cheaper, answered on scale, modularity, custom
  switches and lifetime support; claussen's one-word answer was "Value" (096937, 208121, 523442, 661919).
- **Printing: material and machine.** Resin/SLA is proposed in every printing debate and never adopted —
  "Most people just use 3D printing wrong," SLA prints are "straight up brittle," tofurki's request for
  models without FDM support artifacts **got no answer at all**, and 2025-01 closes it on opacity problems
  "for daaaaays," leaving ABS/ASA vs PLA live (634816, 300392, 138975, 403044, 817876, 549352, 853554,
  851575, 172584). Bambu vs open-source printers is "a sharp divide in the community" and still split in
  2026: Bambu "respects my time immensely" vs a Core One printing so well magnets don't need glue (144715,
  686824, 778496, 483359, 673919). Printing the board on a 180 mm bed stayed unsolved (957791, 473985).

## Fit, mounting and layouts

- **Armrests, trays and mounts.** Cyrus: no armrests at all, the mount takes the full weight of your arms,
  resting elbows "will almost instantly give you cubital tunnel issues," and "keyboard trays suck. Unless
  you have no legs." claussen answers "Tray." Chair mounting is still unsolved — rigidity issues on a
  Varier, Zach Valenti giving up for desk arms, Flinch getting no clean answer (826668, 414589, 778351,
  022761, 087444, 302922, 720468). SmallRig arms are "basically identical to all the other Chinese ones but
  at a higher price" or worth it because "The little differences matter"; a CNC desk plate and a magnetic
  bottom plate stalled unfinished; **VESA holes were refused outright** (153249, 791508, 673759, 737372,
  718111, 101542).
- **Palm rests** — the most-iterated open problem of the backfill, and the only one with a 2026 answer in
  progress. ~5% go palmless, one user finds hovering actively painful, most need a rest at least while
  adapting, and how much contact is right is unsettled (506304, 668659, 167254, 490273, 555442, 935626,
  540561). Every material was tried, from a vacuum-pack bean-bag rest to printed saddles,
  silicone-in-a-mould and 95A TPU "very messy to print," and hard vs soft stayed split (481010, 030131,
  680881, 611066, 559656, 665496, 489127). 2026: a **soft molded palm rest in development**, even 15A
  durometer "wayyyy too hard" (182029).
- **Switch alpha layout at the same time as the board, or not?** — first window and still asked. cryptanon
  went QWERTY 130 → Dvorak 120 and "wouldn't do it again," against claussen's "get up and running first,
  then optimize piecewise"; 2025-03 repeats it with the sides swapped, phreaker (who did it) saying "It is
  months of work," and the accepted compromise is that non-touch-typists should switch (472272, 829939,
  408264, 270769, 370624, 469781). Whether QWERTY is defensible here is its own split — "ERT and UIO north
  keys would kill me" vs claussen staying on QWERTY (055215, 920859, 296765, 656373, 237208) — and home-row
  mods are the same argument one level down, phreaker's misfire knock against jacg's "fully embraced HRM"
  (597418, 814579, 103604, 527043, 142011).

## Settled by the later window

- **No injection-molded and no metal Svalboard.** The 2023 case for injection ran into clusters that aren't
  moldable and preorder scale nobody could deliver, and the aluminium drop-in case never shipped — "Plastic
  is basically always the right choice" (996660, 769055, 980399, 698074). Decided Dec 2025 – Jan 2026: **a
  flat "No" to a metal Svalboard, though the files are open if you want to make one** (685464), and no
  injection molding — ~$100k tooling and a frozen design that "is the literal Datahand story" (811949).
- **Smooth / hi-res scroll — shipped.** onlyforresearch pushed it through 2024-06 on RSI grounds, Cyrus
  argued the threshold implementation was fine and blamed naive apps, phreaker wanted it but not soon
  (298587, 749277, 068527). Delivered in firmware `v2025-11-01`, Linux/Windows only (871902). Still open:
  **horizontal scroll jitter** in Figma, blamed on app-side handling and stepped OS scroll APIs (813632,
  080916).
- **Which half should be master, and is the sub side worse?** "Master side is buttery smooth. Slave side is
  great for scrolling" against Cyrus's "I mouse with both sides and have never noticed a difference" on
  identical hardware, plus disagreement over which half to make master (881894, 200178, 139990, 974367).
  Answered in 2026 with numbers: make the pointing hand master, ~400 Hz there versus a steady ~200 Hz on the
  sub side (898615).

## Odds and ends

- **Support by LLM** — claussen in 2025-01: "Eventually an LLM will take over that job," and on docs, "If
  people RTFM it's all there… But people don't"; RufusRed's NotebookLM over the manual worked but couldn't
  be link-shared (014081, 012683 of 2025-01). By 2026 LLM agents are a "hard no" for repo access automation
  while the offline chooser's workaround is to ask an LLM (005194); phreaker's objection is that tutorials
  imply a maturity the product lacks (234493).
- **Keymap-tampering lockdown doesn't survive contact with rawHID** (761242); **roller-bearing trackball
  mods** were tried and dropped (833, 919285); **flakiness over USB hubs** had three theories in 2024-02
  and no resolution — power budget, the orphan PS/2 trackpoint driver, ChibiOS/QMK USB driver quality
  (488479, 128808, 491668); **layout optimisation for this key geometry** is still unsolved, "no really
  thorough layout analyzer adaptations for the svalboard" (176015, 498016); and **Mac support isn't
  awesome, but everything is very customizable**, with Touch ID impossible (975846, 894423).
