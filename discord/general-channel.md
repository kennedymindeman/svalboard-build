# Svalboard general channel — distilled reference (2026-06-21 to 2026-08-15)

Source: Discord channel `1124364902811844739`, 1,309 messages, distilled 2026-08-15 by
an LLM pass over `raw/channel-1124364902811844739.jsonl`. Message ids are the last 6
digits of the snowflake. Agreement counts are floor estimates (who spoke up), not polls.

## 1. What this channel is about

The general / open discussion channel for the Svalboard, a DataHand-inspired finger-keywell
keyboard with magnetic breakaway switches and integrated trackballs, designed and sold by
**claussen** (Morgan Venable, founder; inferred from 634238→739891, 1080, 1294). It is not the
support channel: build problems get redirected to the closed troubleshooting channel and to
customer-service tickets (264, 533, 803, 1240). Content: pre-purchase questions,
3D-printing/self-build advice, trackball/pointing-device debate, ergonomics/adaptation,
hardware mods. Recurring voices: claussen (founder), phreaker (firmware dev, author of the
"Viable" firmware, volunteer; 458250, 211439), Hugin&Munin, HazardousChurch, Cyrus
(experienced self-builders), lumbduck (works in assembly with claussen; 043542).

## 2. Recurring recommendations

### Firmware / software / keymaps
- Program it with **Vial** (desktop) or **vial.rocks** (web); **Keybard**
  (captdeaf.github.io/keybard) is the newer alpha tool. claussen; endorsed via bot command by
  HazardousChurch (311742, 308596, 573–575, 1167).
- **LGui = Command on Mac**; there is no separate Command key. GUI/Super/Win/Command are one
  keycode. phreaker, Moo, Hugin&Munin agree (224564, 726146, 315).
- For very low typing / one-handed use, **voice coding** (Talon + Cursorless). claussen,
  dyamito; 3+ endorse (984210, 435546, 223).

### Printing / materials
- **Plain PLA for keys/clusters, especially the first build**: "prints so cleanly and it's so
  easy to thermoform"; only reason to use anything else is slumping in heat. claussen + 3
  others (385/386, 923157, 366878, 836810).
- **Bambu printers are "cheat codes"**: P1S/A1 print parts with near-zero post-processing.
  4 agree (494/453818, 064288, 345257, 115909). Open-source setups (Voron Trident + BoxTurtle)
  also work (frostyllama 399/400).
- **Print labs are not viable**: they won't guarantee the tolerances the Sval needs; buy a
  printer, use a library/makerspace, or buy prebuilt. Hugin&Munin, Antwane (867081, 338398).
- **Dimensional accuracy is critical; elephant foot is normal**: lower first layer / use the
  compensation setting. claussen, Cyrus, HazardousChurch (866237, 150072, 867).
- **ABS vs PETG for bases**: ABS prints easier but has a shiny/slippery finish; PETG is
  darker/shinier. Ambrosia matte ABS recommended. Cyrus, frostyllama (597027, 388/971017).
- **Chamber heater (Panda Breath) strongly recommended for ABS/ASA** large parts. claussen
  (001300, 845, 495419).

### Trackballs / pointing devices
- **Two trackballs is the conventional / "peak" recommendation**; pointing devices can be
  swapped later. flesh.priest, ziasquinn (575685, 124200, 662621).
- **Red (the resin ball Sval ships) tracks best; silver "tracks better than anything on the
  market."** Factory builds are tuned for whatever color you pick, so color is a non-issue.
  vin, claussen, phreaker (912003, 760/764, 766, 227850).
- **BTUs (Bosch Rexroth ball transfer units, ~$100)**: much lower static friction but noisier
  and jumpier than statics; personal preference. claussen daily-drives Bosch BTUs; phreaker
  "lift my hand to click" (883–887, 821773). HazardousChurch's printed-BTU alternative is
  cheaper (printables.com/model/1740316; 896/205198).
- **Lubrication is essential; face grease beats Renaissance wax.** claussen (855–858).

### Ergonomics / adaptation
- **Don't buy expecting to type faster**: "Buy it because you're in pain or you want to
  protect your hands." Near-universal: equal-or-slower burst speed (often 10–30% slower) but
  all-day pain-free use. claussen, Cyrus, drpngx, HazardousChurch, lax3r (806/807, 800,
  991164, 904362, 1185).
- **Mounting: two C-clamps + two magic arms; splay the halves** (like an MS Natural), don't
  keep them vertical or too close; remove chair armrests; most desks are too low. Cyrus
  (252648, 798, 783).
- **Don't alternate between Sval and a normal keyboard during the learning period**; it
  slows adaptation. Cyrus (772372).
- **Default key weight 0.7; go stiffer (1.0–1.2) for gaming and "swole"/climber fingers**;
  lighter center keys are available. HazardousChurch, Jaboo36, claussen (559, 551, 560,
  976087).

### Suppliers / parts
- Rubber feet: AliExpress **FC-036-DCW-PT** (C. 570810) or generic silicone stick-on
  stoppers (phreaker 737482).
- BTU hardware: M2 countersunk screws, 3mm/3.175mm **G5 ceramic** bearings (HazardousChurch
  822442/627834).
- Travel case: **Nanuk 910** (steventeddy 389542).

## 3. Contested or open questions

- **Wireless Sval**: repeatedly requested (xelra 302680); claussen and phreaker say no
  near-term: "Bluetooth hell," optical-sensor power draw, ~100 hrs of firmware work (929340,
  211439, 003841).
- **Per-layer trackball/mouse disable** (gaming): wanted by several, not supported yet;
  workaround is removing the ball or disabling the auto-mouse layer. Max Hendriks, beep
  (1094, 358624).
- **BTUs vs static bearings**: genuine split (smooth/quiet vs low-friction/jumpy).
- **Home-row mods on Sval**: some love them, some find the timing/trigger point off versus a
  physical key. C. vs phreaker (203152, 831526).
- **Metal / hollow trackball + capacitance touch-to-switch-layer**: NickeaTea and
  HazardousChurch tinkering; claussen skeptical that touch is a good signal (932, 955).
- **Roller-bearing trackball mod**: tried and disliked by phreaker and robflop; poor off-axis
  performance; not in the official repo, no plans (833/834, 826, 839).
- **Layer-indicator desktop app**: doesn't exist; only prototype firmware. claussen (923196).

## 4. Notable links / resources

- svalboard.com/build — official build guide (bot `!build`, 532).
- captdeaf.github.io/keybard — Keybard alpha config tool (574).
- svalboard.com/scroll — pointing-device / scroll setup docs (`!point`, 501371).
- svalboard.com/chooser — color chooser (currently down; 30, 290).
- vial.rocks — web keymap editor (308596).
- svalboard.com/pages/trial-program, /policies/refund-policy, /policies/shipping-policy,
  /pages/3d-printable-parts-repo-access-policy (636, 638, 1253, 1242).
- youtube.com/watch?v=fa_BZ1AKQVk — community build-guide video (468).
- printables.com/model/1740316-printedbtu — HazardousChurch's printed BTU mod (205198);
  OnShape BTU repo owned by claussen (838/838747).
- ambrosiafilament.com matte ABS; flashforge.com Burnt Titanium filament (390).
- github.com/input-leap/input-leap (Deskflow) — share one Sval across two PCs; Deskflow
  maintainer Nick Bolton chimed in (587, 599).
- youtu.be/97TcZ7lD_oc — Svalboard at SF keyboard meetup (treeform, 1268).

## 5. Newcomer FAQ (asked more than once)

- **Do you type faster on a Sval?** (547952, 799, 249080) → No. Buy for pain relief; expect
  equal-or-slower speed and all-day comfort. claussen (806/900887).
- **Do I need a printer? Print lab? Kit vs prebuilt?** (303461, 103141, 638855) → Print files
  are reserved to kit/prebuilt customers; print labs won't hold tolerances; from scratch it's
  an ~80-hour project; "Nobody regrets buying a pre-built." claussen (312906, 817).
- **What do I use to program it?** (569, 1166) → Vial, plus vial.rocks and Keybard (alpha).
  claussen (311742).
- **Return policy / can I resell mine?** (451262, 625) → Kits are not returnable; prebuilts
  per site policy; reselling self-print kit builds for profit is discouraged. claussen
  (757222, 1243).
- **Which pointing device for RSI?** (355742, 1157) → Two trackballs, swappable later.
  flesh.priest (575685).
- **Can keys be held for gaming/WASD?** (613837) → Yes with OS key-repeat; use a gaming layer
  and hold center (not north) keys. ziasquinn, lax3r (856650, 850).
- **Where's the color chooser?** (30, 290) → svalboard.com/chooser is offline; use an LLM or
  manual image coloring instead. claussen (264425, 716068).

## Gaps
- Channel name unknown (export carries ids only); "general" is inferred.
- claussen = Morgan Venable / founder is inferred, never stated outright.
- Attachment URLs are expiring Discord CDN links; image-only claims rest on the surrounding text.
- External product/spec claims (trackball colors, BTU pricing) are community assertions, unverified.
