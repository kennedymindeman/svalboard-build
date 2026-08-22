---
type: Reference
title: Gaming
description: Gaming-layer setup, WASD placement, which genres work on trackballs, and the gaming-keypad comparisons.
tags: [svalboard, discord, gaming]
source: "discord #general 1124364902811844739, 2023-09-07..2026-08-15 (gap 2025-08-10..2025-10-17)"
---

# Gaming

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-1124364902811844739.jsonl`; a few 6-digit suffixes collide in the 43k-message export, so disambiguate by date if a lookup returns two hits. Agreement counts are floor estimates.

- **Gaming layer recipe**: switch to the mouse layer (14/15), then press the automouse-toggle key so
  trackball motion can't yank you back to layer 0 (phreaker binds it into a macro), and **turn off
  autoshift** (612489, 139654, 982748, 849768, 321419). History: through 2024 there was no stock way to
  keep the ball live while suppressing automouse — whitelynx and phreaker said it needed custom C
  (068196, 195798, 552923), and RufusRed's workaround was **mouse-layer timeout infinite with its keys
  transparent over a gaming base layer** (452198, 621002).
- **Strip QMK cleverness off the gaming layer.** No home-row mods (phreaker 316392), no one-shot mods
  (018053); dataangel's reason is that most games assume WASD and behaviours like combos misfire in-game
  (283391). A **toggled/locking layer** is the standard binding — claussen relayed JesusFreke seeing "no
  difference" gaming on lal, and phreaker wanted `TG` for the first time in years (437698, 612554,
  859456, 626774, 592018). Editing the layout mid-game with Vial open on a second monitor is "100%
  normal" (095709). See [firmware-and-config](/firmware-and-config.md) for the mouse-layer settings.
- **One gaming layer or one per game — the channel does both.** phreaker keeps a single layer so crouch
  lands on the same key everywhere (345115, 516765, 554972); myxfit and later CwD keep a base gaming
  layer and fork it per title, with movement on the centers and quickbar actions on the souths of a mode
  layer (108156, 198057, 419931, 872690, 644359). Illum's reframe: "instead of thinking of it as a
  keyboard, flip it around and see it as a controller" — rebind in-game so a key *is* the inventory key
  (950312). If you type an alt layout, **keep a QWERTY left-hand layer for gaming** (phreaker 890540).
- **WASD**: A/S/D on south keys with W on the middle-finger center; hold center keys, not north, and let
  OS key-repeat work. **High-APM (Tetris/osu) is unresolved** — 6.7 cps on a Sval vs 6.9 on a Wooting
  (489416, 856650, 609447); phreaker has never pitched it as a gaming board — "Is it the best gaming
  board? Probably not. Wooting puts a ton of effort into their boards" (942945). This placement has been
  stable since 2024: phreaker's Fallout 4 map adds Q on
  center ring and E on center index (339404, 225480, 240243, 157231, 829826, 702251, 792449), Sc0tTy
  plays Counter-Strike with S on south and WAD on the home row — "putting that on the north is really
  bad" (130017, 754446, 089052), and Raven System warns against collapsing WASD onto one finger's
  cluster, "that just becomes cursor diamond and is a recipe for RSI" (369527, 797555). Mock the layout
  on paper before flashing it (980682, 658938, 432168). Early on, myxfit's "straight across" home-row
  mapping and Arska's "Jesus' order" (strongest finger forward) were the competing schemes (311592,
  162691, 823908, 549460, 653814).
- **Sim and slower games work; twitch shooters are unproven.** phreaker finished Elden Ring (on 52 mm
  balls; would use 44 today, see [pointing-devices](/pointing-devices.md)) and most of CP2077 on
  trackballs; HazardousChurch played 4 h of Arma 3 but isn't accurate enough for headshot-reward games.
  Real mouse for FPS; accel curve matters more than hardware (468032, 424514, 246476, 637514, 484646,
  738021, 001961, 461128). CwD's tiers: "Sval + external pointing device: Great, *at least* on par with a
  normal KBM setup... Sval only: Workable with little learning if you're already a trackball gamer...
  Will almost definitely need a gaming layer" (510865). Raven System: fine for "95 percent of games",
  "anywhere from impossible to use (Osu) to a vast improvement (WoW)" (426264, 154449, 583319, 460692).
  HazardousChurch on realistic shooters: 0–50 m fine, 50–300 m difficult, Tarkov no (982190). Titles
  played fully on Svals: Elden Ring, Fallout 4, Skyrim, Darktide, Doom, Baldur's Gate 3, Last Epoch,
  HITMAN "100% playable", Epistory, Counter-Strike, and Valheim/Vintage Story/Factorio/HotS with no
  matchmaking dip since Feb 2025 (587328, 166346, 953604, 399895, 135578, 743096, 673480, 238813, 527486,
  412851, 276000, 746828).
- **The common setup is Sval left hand plus a real mouse right hand.** claussen: "Lots of folks gaming on
  Sval, but generally one-handed with mouse for that high-precision high-speed stuff" (132796, 303060);
  phreaker uses a Pulsar X2 Mini and reserves full-Sval play for turn-based (730721, 603290, 119661,
  743096, 708513, 269771, 065597). Raven System: a mouse "can't be beaten for games" while "for office
  use, ball is better" (440638, 037146, 071221, 009638). **Make the half whose keys you press the
  master** for competitive play (phreaker 974367); ziasquinn keeps a second master-left config as the FPS
  layout (057867, 158503). The cost of going Sval-only is that you can't type one-handed, so moving off
  the mouse is slower (426264). Don't plan to game on the trackpoint — "It will never be as fast or
  precise as a mouse or suitable for gaming" (claussen 887327).
- **History — trackball-for-FPS was argued both ways in 2024–25.** Axel used one "at a somewhat
  competitive level" (001447), and OwlWithAPipe posted the loudest results: 14/15 headshots in an Apex
  training match vs 9/15 on his vertical mouse (618979, 388810, 913896), then Ultrakill at his normal
  difficulty with the left ball removed — headshot accuracy better than his gaming mouse, twitch and
  long-distance accuracy worse (396648, 833921, 311366; footage youtu.be/7_VetFUR5CQ 875657). Sc0tTy at a
  LAN: "competitive Counter-Strike is just so much better with the Sval... No cramp at al after 24hrs"
  (456036, 252482). The current recommendation is still a real mouse for FPS.
- **The point is playing longer, not playing faster.** phreaker got his first trigger finger from console
  Diablo 3 and games on the Sval to reduce damage (078800, 282439, 944024); his Elden Ring headline is "0
  days of play lost due to pain so far" (995847); OwlWithAPipe's is "I was able to game for 5 hours today
  when normally I could only do at most one" (396648). **Light keys are part of the argument** — "I can't
  game on heavy boards... when you want to run forward or whatever, for 5m, it matters" (959956, 622100,
  592838, 188533). Counterpoint from CwD: Sval switches are deliberately not "optimized for repeating the
  same click rapidly (and shouldn't be)" (958616), and sixtysixone notes gaming peripherals eat abuse the
  Sval isn't built for — "Go left harder! I don't care that 'A' is already pressed" (681697). As of
  2024-01 claussen had built rigs for a Counter-Strike para-esports team with Duchenne's MD in Växjö,
  where shorter throw and lower force are the selling point (813352, 988965, 930187).
- **Trackball-as-joystick and joystick thumb mods are a recurring dead end.** boogerlad.'s set-and-hold
  direction idea founders on the ball having no deadzone to snap back to — Jaarx: "a trackball doesn't
  have a static state that says 'move'" (409384, 653120, 948746, 467965). A joystick thumb cluster has
  been asked for repeatedly and nobody has built one (329024, 483429, 736597); pekudzu warns a stick out
  of the thumb cluster's plane invites de Quervain's (068950, 998869; prior art
  github.com/dschil138/Fulcrum 258848). claussen on an Azeron-style gaming Sval: asked "a few dozen times
  over the last year", hard on "development and SKU proliferation", and hot-swapping such a module is out
  because it would need reflashing (851073, 766236, 894522, 656092); phreaker is more open — "If joystick
  support comes, we'll figure out the software" (237461, 601070). Gamepad output with SOCD cleaning
  exists only on tomatosoup's fork, github.com/tomatosoupcan/vial-qmk/tree/joy (000033, 373900, 091451).
- **Against the gaming keypads: nobody here who owns an Azeron Cyborg recommends it.** Raven System: "I
  love my svalboard and despise my Azeron", "Don't do it. 😬", awful adjustment mechanism, switches in
  unusable positions, mini USB, closed firmware (085993, 752128, 975229, 862408, 022686, 439903); the
  knuckle "scorpion tail" keys are "wildly unsuccessful" (544266, 002819, 762625). claussen's is "already
  in a shipping box waiting to go to its next victim" (822089) but he refuses the category comparison —
  "Not the same product category... I love Azeron, I think they're a great company serving a totally
  different market" (902240, 585172, 918346); the **Razer Tartarus is the closer analogue** — "I love my
  Tartarus, but no typeeeee" (951401, 149756). Practical differences: ~13 easily-hit switches per hand vs
  ~23 on a Sval, "good for MMOs, but it's not a keyboard alternative", and "The sval is way easier to
  'land' on than the cyborg" (244511, 047804, 257266, 087535, 498654, 215922, 965168). CwD's working
  answer is two devices — losing the Sval's thumb keys "would lose a ***lot*** of usability as a
  keyboard" (109440).
- **Hardware caveats, time-bound to 2024**: matrix polling is ~700 Hz, pointer lag was never
  characterised, and debounce/latency were untuned (claussen 760445, 055570; phreaker 345115, 869006).
  A single hand sells as a gaming macropad (667551), and Vark bought one as a left-hand gaming keypad —
  "my entire purpose of the svalboard is to make it a gaming device" (584092, 287976). Under-desk mounts
  still need a mouse surface: get a tray (claussen 981968) or davejones' 4-foot shelf panel with an XL
  mousepad cut to fit (220276); an arm-mounted board plus mouse remains unsolved, so phreaker keeps his
  gaming board on the desk (525258, 952806, 708378).
