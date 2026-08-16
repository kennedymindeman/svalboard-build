---
type: Reference
title: Firmware and config
description: Which firmware release to run, Keybard versus Vial, flashing and building from source, mouse-layer and pointing settings, layer and modifier idioms, and how the answers changed from 2023 to 2026.
tags: [svalboard, discord, firmware]
source: "discord #general 1124364902811844739, 2023-09-07..2026-08-15 (gap 2025-08-10..2025-10-17)"
---

# Firmware and config

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-1124364902811844739.jsonl`; a few 6-digit suffixes collide in the 41k-message export, so disambiguate by date if a lookup returns two hits. Agreement counts are floor estimates.

## What to run

- **Boards ship without firmware** — POST only. Flash the latest release of
  `github.com/svalboard/vial-qmk` yourself. claussen (450890, 992539). *History: from 2024 to at least
  mid-2025 boards shipped with Vial already flashed, and the oldest mule took the same build as the
  newest hardware — phreaker: "all svals do… if you are asking, you have vial" (177833, 195264).*
- **What to run today: `v2025-11-01`.** History: `v2025-11-01` (smooth scroll) → a Christmas 2025 RC
  with a new UI (Azoteq/trackpad users had to skip it) → phreaker's C "Viable" fork (daily-driven from
  Jan 2026, never released, now dead) → **viable-rs**, a Rust/`embassy` rewrite from 2026-03-22.
  phreaker: **don't wait for viable-rs**, it's pre-alpha with no UI and no trackpad drivers (701286,
  090304, 432602, 318558, 229928). The Rust thread starts in Dec 2024 with whitelynx's RMK port and
  claussen calling QMK "a massive albatross for us" (166675, 316676).
- **"Update to the latest firmware" is the first debugging step** — claussen's opening question in
  three separate reports (923677, 801696, 607816); releases have been downloadable `.uf2`s on GitHub
  since Dec 2024 (707338, 307413). Older tags still cited in old threads: `v0.002sv` (May 2024,
  trackpoint drift fix) (141093), `v24.10`, and `v25.02.12` (159487, 417574).
- **The fork is not going upstream and never was.** It moved from claussen's private fork to
  `github.com/svalboard/vial-qmk` on 2023-10-20, branch `vial`, merges by PR only (858959, 330041);
  claussen spent 2023 asking for help driving a QMK mainline PR and nobody took it (877500, 456666).
  phreaker's reason is structural — "I don't think QMK will accept" the pointing-device rework — so
  **fork Svalboard, not QMK** (317205, 112745, 628021). The fork trails upstream by ~2-3 months and
  carries special hacks (017481). The software is 100% FOSS; the electronics are closed (016081).

## Config tools: Keybard and Vial

- **Vial, not VIA**, and **Keybard (captdeaf.github.io/keybard) is the config tool to use** — an alpha
  "faster than Vial" in Nov 2025, the recommendation by 2026: swaps whole layers, binds a key by
  typing it, exports layouts, backs up and restores keymaps. Svalboard keeps its own vial-qmk fork and
  "is not in QMK, and does not plan to be." phreaker, claussen (849753, 162951, 079090, 311742).
- *History.* 2023-2024 was Vial-only — claussen: "Vial is not VIA… no submitting your code to the QMK
  style/linter authoritarians" (305833) — with known gaps: `caps_word` invisible to the UI (876699),
  string macros working but not shown (097364), no layer-copy (616661), a GUI unusable below ~1300x700
  (497374). Keybard appears Sep 2024 as "where this is going" (081664) and is the answer by Feb 2025
  (093088, 376000, 400390); Vial was rotting anyway, broken on macOS 15.3.1 and un-installable on Linux
  because its Python is gone (553018, 060861). By mid-2025 Keybard is "essentially superior in every
  way," ~98% feature parity, and Cyrus had seen Vial corrupt Keybard-edited configs (194952, 483476).
- **Keybard runs with no board attached** (`Menu → Sample .kbis`), so you can build a layout before
  delivery; Vial cannot (820615, 923915). The same trick restores one wrecked layer: copy it as JSON
  from a sample, reconnect, paste onto the right layer (River 784967, 549559).
- **Web tools need a Chromium-family browser** (Firefox lacks WebHID), **close desktop Vial first** (a
  second tool holding the device is why a config "won't load"), and on Linux install the Vial udev
  rules. Cabling: **halves joined via `S`, host into either half's `U`** — host into `S` gives power but
  nothing works, so suspect the cable first (192313, 538683, 441328, 681384, 239720).
- **"Run one tool at a time" is the most repeated support answer in the archive** — claussen: "Vial and
  Keybard deffo stomp on each other" (406235) — covering most won't-connect, won't-write and
  vanishing-edit reports (923550, 385906, 515468); Svalbr counts as a second tool (838784, 537203), and
  a disconnect/reconnect mid-edit silently drops bindings (987412). Details: Vial's udev rules on Linux
  or the NixOS `vial` package (025213, 853599, 965709), and **Brave blocks Keybard's downloads** via
  the File System Access API — use Chrome or ungoogled-chromium (790302, 596403).
- **There is no save button**: edits go straight to EEPROM, and the keymap lives in MCU flash rather
  than in the firmware, so a configured board is plug-and-play on any host with nothing installed
  (493380, 614952, 812136). Vial is also safe for corporate IT — raw HID only, mass storage only in
  bootloader mode (Moo 630889, 099733).
- **Keep the keymap in version control**, since layouts have reset to the flashed default unexplained
  (773480, 777030); committed exports suffice (pekudzu 168397). **Prefer `.vil` to `.kbi`** — `.vil`
  moves between both tools, `.kbi` is Keybard-only and phreaker rates "nothing worth using KBI right
  now" (869116, 233852). Recovery is double-tap RESET, then reload a default `.vil` from the
  svalboard-configs repo (600715, 741002).
- **Keybard's matrix tester separates a fit problem from a firmware one** and is bookmarkable
  (`.../keybard/launchers/index.html?launch=matrixtester`); Vial has one as a tab (285376, 938209,
  795479). A trap lives next door: a stray click in Keybard's QMK Settings sets QMK "Magic" modifier
  swaps, because the settings row is a `<label>` for its checkbox — whitelynx's board emitted LCtrl for
  LGui until sixtysixone traced it (925941, 802419).

## Halves, master side and flashing

- **The master side holds the whole keymap** — right = master by convention (or the pointing hand if
  lefty), marked by the USB-C end of the inter-half cable; flash both halves if you swap. Make the
  pointing hand master: it polls ~400 Hz stock (peak ~465, 550–600 with turbo) versus a steady ~200 Hz
  on the sub side plus half-to-half latency. phreaker (883702, 927552, 898615, 789978). The rule is as
  old as the board — the sub "just sends the matrix" — and each half stores a *complete* keymap, which
  is both a feature (Windows map one side, Mac map the other) and the usual cause of "my layout changed
  by itself" (972772, 401349, 946699). The **sub-side ball tracks as if it had lower DPI at identical
  CPI**, so re-bias when you swap sides (915082, 354430).
- **The halves talk full-duplex USART over the USB-C connector, not USB**; either side can be master and
  one half runs alone (`EE_HANDS`) (607994, 721862, 003178). **Since the 2024-03 move to ~500 kbps full
  duplex you must flash both halves**, and again whenever you change the number of layers — Raven
  System's "left hand dead" bug bisected to the full-duplex commit `5c545fe` (252891, 990337). Half
  duplex had destroyed fast trackball tracking; full duplex cost scan rate ~750 → ~700 Hz (636874).
- **Flashing**: back up the layout; one image per half; USB into the **U** port, **double-press the
  reset button on the underside** (or bind `QK_BOOT`), and the half enumerates as an `RP2 Boot`
  mass-storage drive — drop the `.uf2` on it, repeat on the other half, halves need not be disconnected
  (DanWest 654066, 982683, 854697). **Flashing wipes your config**, and a *custom* keycode means editing
  the Vial JSON and recompiling (816735, 828031). If only one half works afterwards, reflash and then
  suspect the cable — flipped cables and grit on the contacts are the usual causes (325520); wiring
  restated, **S to S, U to the machine** (967017).
- **Pick the `pmw3389` build** unless you bought roughly a year before Feb 2025; the 3360 is deprecated,
  and the wrong build breaks nothing permanently, it just doesn't work until you reflash
  (`keyboards/svalboard/docs/flashing_firmware.md`) (Raven System 820264, 826015, claussen 258049) —
  see [pointing-devices](/pointing-devices.md). **Variant names encode device positions**: `trackball`
  = one or two balls, `ballpoint` = ball left / trackpoint right, `pointball` = the reverse (038541,
  441361, 929632).

## The mouse layer

- **The mouse layer is owned by the board and is always the top layer (14/15).** For a persistent one,
  copy 15→14 in Keybard and `TO(14)`; to type without falling out, bind keys on layer 15 or use an
  infinite auto-mouse timeout plus an escape key. The **automouse toggle disables the auto layer switch,
  not the trackballs** — don't put it where you can hit it, since with no mouse buttons bound you need a
  physical mouse to recover (466301, 199725, 881003, 432306, 833468). It has been layer 15 in every
  build since 2024, entered on any pointing-device movement (078451, 321030, 845044).
- **Automouse does not gate the mouse; it re-maps the other keys** — OwlWithAPipe's realisation, the one
  that unblocks most [gaming](/gaming.md) setups (015977, 295771). **Anything bound on layer 15 keeps
  you there, anything else drops you out instantly** (exceptions: `KC_TRNS`, `KC_NO` and EEPROM-writing
  keys), so typing leaves the layer and no habit key is needed; which keys held you used to be compiled
  in and "nuanced" before the rule loosened (843871, 233932, 161522). Docs:
  `keyboards/svalboard/docs/pointing_devices.md#by-button-press` (178024).
- **Don't `TO(15)`** — GooseClip's "layers get stuck on" bug was exactly that, and only bit once he
  typed fast enough; phreaker: "let the system manage it" (357440, 022059, 259947). The pre-2026
  equivalent of the 15→14 copy was to duplicate every mouse-layer key onto a spare layer and transit to
  that (482567, 577617). **Turning automouse off**: bind `SV_TOGGLE_AUTOMOUSE` and press it once —
  merged around 2025-02-07, under `Mouse & Special Keys → Keyboard's Custom Keys` in Keybard or Vial's
  User tab; if it isn't there you're on old firmware (Raven System 747596, 128959). *Before that key
  you emptied layer 15 or made it fully transparent so the board fell straight back out* (971092,
  854270, 847679). A mouse layer that never activates usually means you hit that toggle by accident —
  claussen: "it's happened to me" (852967, 826847).
- **Infinite mouse timeout is the house favourite** — phreaker: "once you go infinite mouse timer, you
  never go back"; pair it with a *small* mouse layer (mods and buttons only) so ordinary typing exits it
  90%+ of the time (545920, 330142, 121403, 462387). claussen keeps 500 ms because in EECAD "suddenly
  hitting x while moving the mouse is impossible" (524021). The timeout is **a fixed cycle on a bindable
  key, not a number you type** — Mouse Key Timer, in Vial's User tab or Keybard's "mouse and special
  keys"; `Output Status` prints it, and `-1` is infinite (134815, 733195, 687740). *The cycle itself
  moved: inf → 500 → 300 in mid-2024, 300 → 500 → inf later that year, -1 / 300 / 500 / 800 by 2025*
  (160170, 615069, 866186, 852166).
- **Keys that write EEPROM are forbidden on the mouse layer** — DPI +/-, the sided scroll toggles and
  the timer key silently exit automouse instead of firing, deliberately, "so we don't burn the flash";
  that is the whole explanation for dead DPI keys (415062, 439761, 934165, 314263).
- **Mouse buttons go on whichever cluster your modifiers aren't on** — phreaker runs mods on thumbs and
  clicks on index/middle/ring souths; with home-row mods, buttons go on the thumbs, and clicking with
  the *other* hand is "100x more ergonomic" (204741, 219595, 382400). **Clicks default to Center now,
  previously South** (057237). **Spurious entry into the layer is usually mechanical** — a loosened or
  rotated thumb cluster brushing the ball puts you there on every space (449074, 412681).

## Pointing settings

- **Pointing settings live under "User" in Vial** (mouse/scroll swap, per-axis scroll lock, automouse
  toggle, DPI), all at svalboard.com/scroll; slow scrolling by lowering DPI, and **DPI keys must not live
  on the mouse layer**, which is why they seem dead (312914, 715924, 055348). There is no settings UI —
  you bind keys — and phreaker treats the existence of the `!scroll` bot as evidence something is
  sub-optimal (892222, 288402); Raven System, who wrote the doc, asks people to read it start to finish
  (592552).
- **Making one ball a scroll ball**: bind `scroll left toggle` / `scroll right toggle` on a layer that
  is *not* the mouse layer, press it once on the physical board, then unbind it so you can't hit it by
  accident; it persists in EEPROM across power cycles, and `Output Status` shows `scroll: yes` when it
  took. claussen, Cyrus, 4+ agree (898660, 180636, 758977, 930219). The **sided toggles are permanent;
  the unsided Scroll Toggle and Scroll Toggle Hold are temporary** and act on both halves (417396,
  479890, 335390), joined later by non-persistent swap keys that flip point↔scroll on hold without
  burning flash (479850, 192706). On dual-ball boards the **left ball has defaulted to scroll since
  2024-10** (174528, 952220).
- **DPI is a board setting, not an OS one, capped at 2400** — "set at the limit of what I think a human
  can control." Stock is 800 and the key steps `{200, 400, 800, 1200, 1600, 2400}`; phreaker runs 200
  cpi scroll / 400-800 pointer (849165, 107439, 604702, 750495, 386270). *Balls booted at 5000 DPI in
  early 2024, until live DPI adjustment landed* (037255). **There is no trackball acceleration** — set
  DPI and let the OS curve do the rest (289243) — and **DPI only works on trackballs**; trackpad and
  trackpoint sensitivity is OS-side (321923, 498928). **Sniper keys are not DPI keys**: DPI is
  persistent EEPROM state, sniper a volatile 2x/3x/5x drop applying only while held, for small targets
  under a high traversal DPI (926686, 526014, 793501, 199366).
- **Smooth scroll shipped in `v2025-11-01`, Linux/Windows only** (Mac needs Mos or Smart Scroll), and
  **do that first update with Keybard, not Vial** — an undocumented 5-key → 5+6-key change makes Vial
  error out. The `Output Status` keycode dumps firmware version and pointer settings into a text field:
  `svalboard/trackball/pmw3389/right:vial @ v2025-11-01` (275032, 136278, 871902, 174082). *History:
  open for two years. Scroll emitted real HID scroll events but was quantized "due to limitations in
  QMK" — a deliberate ~20x step-down, fixed at 200 dpi, needing report-descriptor changes plus a
  feature report upstream hadn't taken; self-builders raised `SCROLL_DIVISOR` in `keymap_support.c` and
  macOS users bought Smart Scroll ($14)* (141679, 909949, 297799, 126682, 736371, 450256). Slow *drag*
  scroll landed far earlier, 2024-05-03, as a Ploopy-derived accumulator/divisor of 10 (653746,
  803935); `DRAGSCROLL` itself is stock QMK (227330).
- **Bind `Output Status` for support** — it types firmware version, per-ball scroll flag and cpi,
  achordion state and the MH keys timer into any text field: `Left Ptr: Scroll yes, cpi: 200, Right
  Ptr: Scroll no, cpi: 800` / `Achordion: yes, MH Keys: yes, MH Keys Timer: -1` (017055, 306197,
  572084).

## Layers, mods and keymaps

- **Everything layer-wise is stock QMK** — tap dances, MO/TT, `DF(x)`/`TO(x)`, Alt Repeat, key
  overrides (claussen on `"` → `?`: "that's just an override") — with tapping term settable per tap
  dance, though not for a `MOD_T(KC_X)` picked from the menu (816735, 828031, 390858, 081724, 688660).
  **Macros can't be held** — put a modifier on the mouse layer as a normal key (255938). Vial's repeat
  key is raw hex `0x7C79`; Keybard exposes it under mouse and special keys, and it is the standard fix
  for double letters on north keys (745429, 357813).
- **Prefer momentary layers to toggles.** phreaker's four states cover 95% of daily use — right thumb
  down = NAS, left thumb down = movement, both = function keys, all `MO()`; violuma: "if you never
  toggle, you don't have to care" about layer awareness. Toggles are for [gaming](/gaming.md) (111792,
  591836, 575430, 958396). Keep an escape hatch: left thumb up bound to layer 0 only, or the same
  `MO()` on every layer, transparent on the mouse layer (995265, 858078, 647043). **"My keys stopped
  working" is nearly always a layer you `TO()`'d into and can't leave** (015400, 801298), and **you
  cannot `TO()`/`TG()`/`TT()` into a layer you are already momentarily in** — QMK behaviour, not a Sval
  bug; a lock on the right thumb-down push-through needs a duplicated destination layer, which is also
  why `TG(4)` in the shipped map "doesn't work" (136074, 016421, 710416, 203541).
- **Capacity is no longer the constraint it was.** RP2040 with ~2 MB exposed of a 128 Mbit Winbond part:
  current builds default to ~10 layers and "100 of just about everything else," against 4 layers / 31
  tap dances / 15 macros on the earliest rigs. **Max layers is 16**, tap dance caps at 49, combos and
  macros at 50; raising any of them means a custom build and dropping layers to ~10 (537428, 775252,
  749407, 899858, 290773, 922075, 746252, 413840).
- **Bottom-row mods beat home-row mods on a Svalboard**, "because south is so good on sval" — phreaker,
  who now runs all four mods on thumbs instead and rates "BRM is tolerable. HRM was not"; drpngx's
  keypress-timing visualizer convinced him he could never use mod-tap reliably. The alternatives that
  dodge the problem entirely are mods on thumbs (the DH way for 30 years), one-shot mods, or
  Callum-style OSM layers (349754, 645618, 894791, 103604, 284347, 527043, 667792, 435156). Use
  `OSM(MOD_LGUI)`, not `OSM(KC_LGUI)` — Vial accepts the latter but it is a different keycode (0x52E3
  vs 0x52A8) and reloads as raw hex (828572).
- **Achordion is built into the tree and is the out-of-the-box HRM fix**, but it blocks same-hand
  mod-tap chords by default and is hard-wired against the physical matrix, so per-combination control
  means building your own firmware — that default is what makes a same-hand bottom-row mod look broken
  (Raven System 527219, 487401, 248214, 879553); `CHORDIAL_HOLD` is the intended replacement, in tree
  but unconverted (128331). phreaker's tap-hold settings, under Keybard's `Menu → QMK settings →
  Tap-Hold`: permissive hold on, tapping force hold on, ignore mod-tap interrupt off, retro tapping off,
  tapping toggle 2 (827407, 230559). **Turn key repeat off for letters** — it is part of what makes
  hold-for-mod feel ambiguous (874638, 307295).
- **Layouts: qwerty is fine.** "The fastest typists on Sval are on qwerty right now AFAIK" — only ~4
  keys move from normal qwerty, 2 from Dvorak, by pushing centre-column reaches to the inward laterals;
  there is no premade Colemak port, you adapt it the same way, and on Colemak **use ASRT, not ARST**
  (648779, 577042, 844923, 668151, 676180). The shipped default is DH-Dvorak (`Menu → Sample .kbis →
  DH-dvorak`) since phreaker's map merged 2024-05-14, over an earlier 3-layer DH-QWERTY default (035528,
  824594, 316466); HD Promethium is the community-favourite alternative, usually north/south swapped
  (575579, 736084). **Don't learn a new alpha layout and the board at once** — cutover is "months of
  work" against 1-2 weeks of Sval adaptation, unless you can't already touch type (270769, 242955,
  282922) — and while fitting, **turn on Monkeytype's "indicate typos — below"**, which separates
  key-order errors from missed keys (723162).
- **Chording works but stays unpopular**: QMK combos give 3D corner chords and NKRO is real, but
  claussen — "basically every week somebody comes in asking about this and nobody ever does it" — and
  cross-petal diagonals are physically hard, since once a key breaks away the force drops steeply and
  the finger takes the path of least resistance (740670, 500801, 737768, 294661).
- **Odds and ends**: **LGui = Command on Mac**, with no Fn/globe key possible (224564), and bind the
  modifier — `LGUI(kc)` — rather than Vial's "copy"/"paste" keycodes, which don't send on macOS
  (542168); **emoji and long text are host-side problems**, since the board only sends keycodes —
  espanso or editor snippets, not QMK unicode (906957, 786946); steno works via Plover (096457);
  practice on **Svalbr** (`!svalbr`, r-tae.github.io/keybr.com), which renders your real keymap off the
  device (170801, 406144, 479336); claussen's `!` bot shortcuts, added 2025-01-23 — `!chooser`, `!fw`,
  `!point`, `!scroll`, `!sizer`, `!keybard`, `!manual` — are the canonical answer to most FAQs here
  (820679, 477661).

## Building your own firmware

- **Almost nobody needs to**: phreaker's estimate is "95%+ of users do not need to build their own
  firmware," since tap dance, macros, layers and HRM/BRM are all reachable from Keybard; the culture is
  to share `.vil` files, not forks (714316, 116186, 864064).
- **Use the CI, not a local toolchain**: fork the repo, push a tag, GitHub Actions builds it (claussen
  468093, 891083). Locally: fresh clone with submodules populated (`hardware/flash.h: No such file`
  means they aren't), then `make svalboard/trackball/pmw3389/right:vial`, and copy
  `keyboards/svalboard/keymaps/vial` rather than running `qmk new-keymap`, which throws `'NoneType'
  object has no attribute 'exists'` (876806, 388426). On Windows use WSL, not msys (917038, 782420).
  The default keymap is `svalboard/keymaps/vial/keymap.c`, not the `.vil` or `keymap.json` files
  (219861).
- **You can build the fork with Vial off and hard-code your keymap** — phreaker: "nothing forces vial.
  You can do you"; Raven System does exactly that (`github.com/SiriusStarr/keyboard-layouts`) (653120,
  877682, 012001, 128522). Two gotchas that cost people days: **don't enable LTO**, which breaks the
  firmware with a `raw_matrix` type mismatch (271528), and **the Sval matrix is transposed**, so QMK
  code checking "same row" needs same col (538482). To turn off `VIAL_INSECURE`, wejn's working config
  is `VIAL_UNLOCK_COMBO_ROWS { 0, 0, 5, 5 }` / `VIAL_UNLOCK_COMBO_COLS { 2, 5, 2, 5 }`, flashed to both
  units (880838).
- **Per-layer LED colours are not settable from the GUI** — phreaker and Raven System set them from
  Keybard's JS console over rawhid, unsupported; the only working brightness keys are
  `RGB_VAI`/`RGB_VAD` ("Bright+"/"Bright-"), and dimming resets to max on layer switch (101990, 046210,
  407232, 052169). Layer indicator LEDs are on every current thumb module (802086).

## Hardware facts that shape the config

- **Optical switches are normally-closed, so a pulled-out key autofires** — blank that position on
  every layer. No debounce, so latency beats anything else you own; the **thumb-down key is two-stage**
  (optical, then a physical switch at bottom-out), which is the "6th" thumb key Vial shows (965436,
  362365, 652938). An empty key position reads as permanently pressed because nothing blocks the beam
  (945217). *History: debounce was 5 ms stock with ~700 Hz polling in Aug 2024, when phreaker offered
  no-debounce test images; by Oct 2024 the answer is "there is no debouncing — cuz they don't bounce!"
  Cyrus's caveat from the electronics side: you still want some, for the LED turn-on ramp and to avoid
  scan-period beating with 50/60 Hz lighting* (345115, 614227, 997073, 007270).
- **The two stages of the thumb-down key cannot be separated** — claussen: "they're electrically
  independent but mechanically sequenced" — so a deep press arrives as LShift down → CapsLock down →
  CapsLock up → LShift up. Many bind the double-press to Caps Word rather than CapsLock; alternatives
  are a Vial combo with negative modifiers or an OS remap (488646, 349241, 768978, 437744, 623188).
- **Switches are binary and force is set at print time**: actuation is optical occlusion, so there is
  no software sensitivity — force comes from key/tab prints and magnet offsets (0.7 mm offset ≈ 20 g,
  dropping 2-3 g per further 0.1 mm; 0.9 mm is the default print). Wooting-style rapid trigger doesn't
  port: the force breakaway is too extreme to hold a key part-way (023131, 465775, 730305, 120144) —
  see [ergonomics-and-fit](/ergonomics-and-fit.md).
- **The trackpad is presented to the host as a plain QMK mouse** — no OS touch digitizer, no libinput
  smooth scroll, no macOS three-finger swipe — and you can mix one pointing device per hand by loading
  Azoteq firmware on one half and PMW on the other (539356, 497918, 354113).
- **No Bluetooth and no host-side layer indicator.** Wireless means a HandheldSci adapter
  (handheldsci.com/kb/), confirmed working in BT mode on `25.02.12`, but not its USB passthrough;
  native BT would mean ZMK (253819, 877798, 362162). An on-screen layer overlay has been asked for
  since 2023 and still doesn't exist: neither Vial's protocol nor QMK reports the active layer, and RAW
  HID is already occupied by Vial. claussen relays that Dale, the Datahand's creator, "swore this was
  one of the biggest roadblocks for adoption," and once offered a free Svalboard for a cross-platform
  layer indicator (652625, 282248, 446324, 122866, 654523).
- **The trackpoint has always been a second-class device**: a Sprintek 8707-51 on PS/2, which Vial
  "never picked up," so the earliest owners built plain QMK (833546, 301575). Direction is a rotation,
  not an axis flip (`#define PS2_MOUSE_ROTATE 90` for a north cable exit on the right) (386705,
  398824); it must sit on the master half with the host cable in that half, and twin trackpoints are
  impossible because QMK can't init the sub-side one (472728, 990640). The cursor jump and phantom
  click on plug-in is a PS/2 init artifact — the board writes commands and never reads the ack bytes,
  so the replies surface as input (975869, 844170); drift is fixable in firmware, config in
  `svalboard.c` (178132, 980097). **Dual trackball only landed 2024-03-23**, once inter-half comms went
  full duplex (741120, 292070), and the **pointing-device layer is Svalboard-specific middleware, not
  stock QMK** — phreaker is "99.9% sure upstream won't want it or take it," which is the root of the
  no-mainline story (578192, 847514).
