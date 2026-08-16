---
type: Reference
title: Firmware and config
description: Which firmware release to run, Keybard versus Vial, mouse-layer and pointing settings, and the flashing gotchas.
tags: [svalboard, discord, firmware]
source: "discord #general 1124364902811844739, 2025-10-17..2026-08-15"
---

# Firmware and config

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-1124364902811844739.jsonl`; agreement counts are floor estimates.

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
