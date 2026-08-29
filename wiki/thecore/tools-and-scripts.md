---
type: Reference
title: Tools and scripts
description: The layout converter, visualizers, AutoHotkey and other remapping software, editors, trainers, spreadsheets and member-hosted sites used with TheCore, 2019-2026.
tags: [thecore, starcraft, discord, tools]
source: "TheCore Discord #general 389438169520799746, 2019-08-24..2026-08-27"
---

# Tools and scripts

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-389438169520799746.jsonl`; a few 6-digit suffixes collide in the 23k-message export, so disambiguate by date if a lookup returns two hits. Agreement counts are floor estimates.

## The layout converter

- **TheCoreConverter (github.com/JaKaTaK/TheCoreConverter) is the supported route to AZERTY,
  QWERTZ, Colemak, UK and other national layouts** — JaKaTaK's Python scripts, generating every
  per-locale and per-hand file from a seed (385488, 823874). Since 2023-11: add a layout
  definition to `KeyboardLayouts.ini`, run it with the Juuce US QWERTY file as seed (466400,
  419016, 418431). In 2020 the seed was the Drive's 6g file and one run emitted all locales
  (ScaryMouse 628867); a copy also sat on the project's GitHub (Siaal 806146). Poletes ran it
  (417493). Through early 2020 there was no generator and non-US files were made by hand (736856,
  987486).
- **It handles AltGr for you**: "it just changes all the stuff bound to alt to be bound to
  alt+ctrl" (JaKaTaK 438559), the problem French users hit (763931). Siaal fixed a bug where
  anything on US backslash should have become `#` on UK QWERTY and did not (788372, 261780).
- `KeyboardLayouts.ini` format is `qwerty button = other layout button`, using the key names SC2
  writes into `.SC2Hotkeys` files (Poletes 729281); Altafen read the code and found it fine, the
  layout data being what is wrong (469061). It came from Jak's team, not JuicyJuuce (594472);
  whether it is buggy was disputed and unresolved in early 2023 (840401, 392627).

## Regional conversions that are broken

- **Scandinavian and Swiss right-hand files come out wrong and were never fixed.** Poletes tried a
  follow-up in summer 2020; the compiler would not run for Scandinavian or Swiss, and he does not
  code, so it stopped there (623848, 387094, 417493). Unresolved as of 2020-09-27, and **the same
  parser is why campaign and co-op files were never published** (632640).
- Minty on the Swedish 6.0 Right file: commands belonging on the US key between backspace and
  enter land on `§`; commands on the key right of `L` (US `;`) also land on `§`; commands meant
  for `-` (US `/`) land on `+` (US `-`) (992391, 943481). jaydik read the code — "I'm actually
  kinda shocked the Scandinavian works even a little bit... the mapping isn't even close" (939840)
  — and planned a Linux VM with every language installed (996555), no follow-up. Poletes doubts
  the theory that his own missing language packs caused it (673985).
- Altafen's draft `[Scandinavia]` block, still needing Blizzard's key names substituted (122278):
  `AltGr=1` / `Equals=Grave` / `Minus=Equals` / `BackSlash=Apostrophe` / `BracketClose=~` /
  `BracketOpen=å` / `Apostrophe=ä` / `SemiColon=ö` / `Slash=Minus`. kbdlayout.info/KBDSW/ shows
  the real Swedish layout (362202).
- **Manual fallback**: search-replace keys with their counterparts in a working file, via an
  intermediate placeholder so replacements do not overlap — an hour at most (Liësa 860029). See
  [hotkey-file-editing](/hotkey-file-editing.md).
- **andylytical's generator (Aug 2021)**, the one alternative built here: a spreadsheet you plan
  in, exported to CSV, plus code emitting an `.SC2Hotkeys` file, written after a straight core6g
  remap for the X-Bows proved unsatisfying (153898). He also found Enter can be remapped (639637).

## Visualizers

- **Current: syfogidas.github.io/thecorevisualizer/visualizer/ — upload your `.SC2Hotkeys` file,
  then select it from the Hotkeys dropdown.** Edennil announced it in 2022 (847592, 940294);
  Syfogidas built it after asking for a "custom SC2HOTKEYS" dropdown option (298944, 816778).
  Third channel pin (481558), still the recommendation in 2024-2026 (000978, 240472). **The
  uploaded file is not auto-selected** (483292, 813, 432717, 958), a step people miss (656, 267).
  It shows only "abilities that existed at the time the original was created" (947157); some
  abilities are missing (481558).
- **Edennil's keylens.edennil.dev**, in beta over 2024-2026, also takes uploaded custom keyboard
  layouts (721402).
- **Superseded: jakatak.github.io/thecorevisualizer/visualizer/, mirrored at
  ivanvolosyuk.github.io.** In 2020 it was the maintained copy and the mirror was out of date
  (Sora 687436, 116314); a Flash page simulating the keyboard, source still on git, already many
  versions behind (Siaal 411498, 786162). By 2022 it was pinned as v3-era — "there hasn't been a
  visualizer in ~5 years or so" (200512, 527690), dated to 2014 by JuicyJuuce (017365) — v3 being
  "the last version that had race and hand-size specific layouts" (730217, 417354, 162563). The
  official site renders an older layout (009735); the old web demo should not be used to learn
  current binds (dtwd 150465, SwordSmith 636648). Newcomers keep landing on it (256842, 528095).
- **There is no visualizer for 6g** (Mutaller 863764, JaKaTaK 647460).

## AutoHotkey: the modifier remap

- **Current script is JuicyJuuce's, left running all the time** (675146), posted in full at 694394:

  ```
  #IfWinActive StarCraft II
  $*RShift::Send {RCtrl Down}
  $*RShift Up::Send {RCtrl Up}
  $*AppsKey::Send {RShift Down}
  $*AppsKey Up::Send {RShift Up}
  $*RCtrl::Send {LAlt Down}
  $*RCtrl Up::Send {LAlt Up}
  #IfWinActive
  ```

  The down/up form is what fixes the stuck modifiers of earlier scripts (452185). Circulated
  unscoped from 2023 (607367, 506738); JuicyJuuce adopted it after testing (326363) and it cured
  his stuck-modifier bug (101159). High repeat rates may need an extra guard (273118).
- **Core+ is Shift -> Control, Control -> Alt, and Windows or List (whichever is adjacent to Ctrl)
  -> Shift** (499989; Edennil 280020; JaKaTaK 233311); the Core+ document in the Drive holds the
  setup and its known bugs (504714, 217860). **You only need external software if you want to move
  the physical location of your modifiers** (Mell00yell00 574450); ScaryMouse runs without any
  remap (493618). Syntax is physical::desired, e.g. `RAlt::RCtl` (609482).
- Earlier scripts. RoboZerg's, verbatim (318248), TheCore+ variant commented out at the bottom:

  ```
  #NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
  #HotkeyInterval 0
  ; #Warn  ; Enable warnings to assist with detecting common errors.
  SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
  SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
  ;v2
  Appskey::RControl
  RControl::RShift
  RShift::RAlt
  LControl & Esc::ExitApp

  ;TheCore+ Recommendation
  ;Appskey::RShift
  ;RControl::RAlt
  ;RShift::RControl
  ```

  Siaal's TheCore+ mapping (480855): `Appskey :: RShift`, `RShift :: RControl`,
  `RControl :: LAlt`, restated as "ctrl->alt / apps->shift / shift->control" (408771). Lv35
  Chungus's block (690910), known to misbehave with two modifiers plus left click (436557):

      #IfWinActive StarCraft II
      RShift::LControl
      AppsKey::LShift
      RControl::LAlt
      #IfWinActive

  Gizmo's one-liner `< :: shift` (235742); his fuller target was Spacebar -> AltGr, AltGr ->
  RCtrl, `,<` -> RShift via SharpKeys with AHK to revert, which with FTYU gives a standard Core
  shifted one key left (550485). Bitstorm remapped AltGr to left Alt (358896).
- **`#HotkeyInterval 0` silences AHK's "too many keys sent" error** (699414), necessary for SC2
  where you legitimately fire keys fast enough to trip AHK's rate limit.
- **Scope it so the remap does not follow you into Windows.** `#IfWinNotActive, ahk_exe
  SC2_x64.exe` (985896) beats `#IfWinActive StarCraft II` (402193) because the exe form survives
  window-title changes (940484); the title form is what most posted scripts use (480897, 170099).
  `#IfWinNotActive StarCraft II` on the first line keeps one script resident while reverting your
  modifiers whenever SC2 is unfocused (synister 912542). Mell00yell00 autostarts his SC and SC2
  files (648051, 940820); autostart means dropping the script in
  `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup` (813121).

## Stuck modifiers and the 2021 Windows update

- **Stuck modifiers are a documented AHK bug with no universal fix** (805447, 914728). AHK
  misbehaves when modifiers are pressed and released in quick succession (Heliac 944065;
  SwordSmith 965888); TheMaster42's swap left ctrl stuck down about once per game (901161,
  333973); Gizmo's pure-AHK setup made the keyboard randomly change function mid-session (981568).
  **Hence the advice through 2023: SharpKeys for the SC2 remap, AHK only to switch back outside
  the game** (736667, 910742; Edennil 497037, 493365; Heliac 629996; jaydik 839958). JuicyJuuce's
  down/up script is the 2023-onward answer that makes full-time AHK workable.
- **April 2021: a Windows update broke AutoHotkey — scripts exit a few seconds into a game.**
  Role-pinged fix: update AHK, add `#Persistent` at the top, re-add the script to startup
  (Mell00yell00 827870). Altafen's caveat: `#Persistent` should be a no-op in a script defining
  hotkeys, since those stay resident anyway (990816). Scripts were later reported deleted outright
  (566996).

## Other AutoHotkey uses

- Rebinding keys Windows will not (188690); making alt+J emit plain J (Edennil 118770; Siaal
  749569 offers it untested for the v5 inject/alt problem); pulling Alt in or running macros when
  the keyboard cannot (Siaal 766834, no script posted); a single-key trash control group on Z
  (630987).
- **Scroll-wheel remap** (Altafen 801222), which insar89 warns works in game but leaves the mouse
  broken on the desktop until reboot (756816):

  ```
  #ifwinactive StarCraft II
  wheeldown::q
  wheelleft::tab
  ;etc
  ```

- **The Fn key cannot be remapped by AHK** — it never reaches the OS (393908). **AltGr also
  resists remapping**: Gizmo's r/AutoHotkey thread went unresolved (956416) and Bitstorm only
  solved it by moving to hardware key mapping (753157).
- **No Linux/X11 Core+ script exists here**; the request went unanswered (Malina 177152).

## SharpKeys, PowerToys, Karabiner and firmware

- **The options for the Core+ modifier remap are SharpKeys (permanent, registry level),
  AutoHotkey, keyboard firmware, PowerToys Keyboard Manager, or Karabiner Elements on macOS**
  (287454, 821545, 209439, 767754). In 2020 the preference order was SharpKeys (PY 686451), QMK
  firmware (Poletes 733837), AutoHotkey (748292); AHK plus a key remapper is the common route for
  people who will not flash firmware (110402, 213623).
- **SharpKeys beats AHK for moving modifier keys** — easier, permanent across reboots, and it
  avoids a remapped ctrl being read as ctrl+alt (175814, 136277, 237761, 377120, 404265). It
  writes the remap into the registry; AHK does it at script level. **Being permanent at registry
  level, it means AHK sees the remapped keys, not the originals** — deine's "why do I have two
  Alts" was resolved by also remapping the original Alt in SharpKeys (653888, 353792, 901512,
  069056).
- SharpKeys or AHK also fixes an unusable Alt Gr on UK layouts: rebind the key between ctrl and
  alt gr (usually Windows) to send alt gr (ScaryMouse 152542, 975681); likewise a dead key next to
  ctrl mapped to alt (SwordSmith 211212; lolersunited 991104).
- **Microsoft PowerToys Keyboard Manager (github.com/microsoft/PowerToys)** does the same modifier
  moves as official, free Microsoft software (Fang Xianfu 320897). Proposed as better than AHK in
  2021, with nobody yet using it and the core docs predating it (Tamaskan 660383, 910144; 768490);
  endorsed by 2024-2026 — "Much easier and more reliable than AutoHotkey!" (WaterMagi 167391), and
  it does not get modifiers stuck (986462). **The tradeoff, raised by JuicyJuuce and unrefuted: it
  cannot switch configurations by focused application, so you toggle it by hand** (738491, 782494).
- **SC2 only supports three modifiers, so any fourth combination requires an external remap**
  (767754, 747034). Karabiner is the macOS answer (456193); QMK layers vs combos vs key sequences
  is discussed as a design tradeoff (750589), see
  [keyboards-and-hardware](/keyboards-and-hardware.md); Razer Synapse and Logitech G Hub cover
  mouse buttons (717810, 260989).

## What is allowed

- **Macro software violates the Blizzard ToS; rapid fire does not.** "1 button press on your
  keyboard sending a sequence of buttons (or multiple buttons) to sc2 is what isn't allowed"
  (189429, 423353, 212861). Rapid fire is fine because "rapid-fire is a hotkey in starcraft
  already" (934845) and "is still just sending 1 signal to sc2 when you press 1 button on your
  keyboard" (916825). Plain remapping, one key producing one different key, is also fine (121736
  confirming 377261).
- Edennil on the AHK remap: "The way it's being used is legal... as long as you keep 1 button = 1
  button, you're good. It's the same thing as if you had used your keyboard firmware to move the
  position of the keys around" — but probably not allowed at a LAN (953651, 926016, 418482). Same
  in 2021: **fine on ladder, one key press for one key press, unusable at offline tournaments
  where you cannot install it** (981312).

## Hotkey file editors

- **jcfields.gitlab.io browser hotkey editor** — pinned in the hotkey channel, and it **covers
  campaign and co-op as well as ladder** (Mell00yell00 093718; Siaal 267029), so it is the pick
  for adding co-op and campaign bindings yourself (065971). Workflow: upload your Core version,
  then save a variant per campaign or commander (876267).
- **CascLib was an abandoned attempt at a better editor.** Moss started an out-of-game editor
  pulling data from Blizzard's servers instead of manual entry, then gave up on the XML (370247).
  The two features he wanted, which nothing else provides: **hotkey groups/tethering** (roach and
  Stukov's banshee burrow as one key) and **warnings naming which keys would be unbound** (089866).
- For sharing whole files: Pastebin (542170), and Discord triple-backtick code blocks so Discord
  does not alter pasted lines (SwordSmith 263455).

## Trainers, mods and practice tools

- **Darglein's multitask trainer** (zerg only as of 2020-05, 727004) and **CGT**, "not bad" for
  control groups (streetplay 716645).
- **SALT ("Save And Load Tool")**, a mod for viewing build orders in game, needs an AI opponent —
  very easy is fine — or the game instantly declares a win; the embot mod suppresses the "you win"
  screen (jaydik 371840, 548928; Altafen 099698). Load it via custom, then melee, then "create
  with mod" (ScaryMouse 007904). **Overwolf is the modern replacement** (Mell00yell00 759124).
- JaKaTaK's mechanics reset playlist is on an old core version but "the principles are still
  good", though the spreadsheet is better (Poletes 030312); the Probe video is what to link when
  someone asks "should I switch from version x to y" (307627; jaydik 036244). See
  [learning-and-practice](/learning-and-practice.md).
- **scelight and sc2replaystats** for keypress-frequency analysis of your own replays (311552,
  071307). **ggtracker is dead** and nothing computes its spending quotient metric anymore, so
  adapt the old staircase guide rather than following it literally (661002, 716480, 248724); the
  old "Keyscores" spreadsheet is archived (359296).

## Spreadsheets

- **TheCore 6.0 / v6 spreadsheet is the reference for picking binds — authoritative but
  unmaintained and outdated in places** (569499, 646260, 899516; Edennil 314960). It carries the
  rapid-fire column and control group recommendations on the far right (569499, 646260), and its
  abilities tab is ordered with more efficient keys further left, which is the method for binding
  leftover commands: first pass, most efficient key still available; second pass, adjust for
  synergy (628968, 770631). It beats the prose — the handbook still describes v5 finger positions,
  "but the v6 spreadsheet does work to tell you specifics" (Deleted User 026132; SwordSmith
  050921).
- **Two sheet ids, and a contradiction the channel never resolved.** In 2020 jaydik gives
  `1CiJwE46S_Kt_ZkVNyXnrjMD15ZSZlv3JSG8nkpjHHtc` as the v6 sheet
  ([link](https://docs.google.com/spreadsheets/d/1CiJwE46S_Kt_ZkVNyXnrjMD15ZSZlv3JSG8nkpjHHtc/edit?usp=sharing),
  673920) and calls the `1zN7ufgH...` sheet a newcomer found the v5 one (ConquestAce 028649;
  jaydik 976960). In 2023-2024 the labels are reversed: `1CiJwE46S_Kt...` is v5 suggested control
  groups, still valid (745754, 794515), and `1zN7ufgH79t6uaCXorX6cs3mWfkMKFC_6VTtZ7vH_9-s` the
  two-tab v6 sheet.
- Also in circulation: "the staircase" `1ZVfn8u6zYFWcuq6xPb6svABp_Q0hbyvrTrlx9tzr3Vk` (146610); a
  newcomer learning sheet `1LhbxeYdkukOzYw030qNYQgLI1p3WUAbSTiuy1emeJSc` (873589); the community
  keybind spreadsheet, "not 100% up to date" per the person who posted it, and Jak's control-group
  spreadsheet (663978, 570462); The Course and the key-difficulty sheet (Luna Cancels 656640;
  Siaal 543573); Edennil's own ergo layout as a Sheet (166037). The Drive layout spreadsheet was
  the 2020 reference, its 6g sheet current as of 2020-05-05 (ScaryMouse 761105).
- **Make your own copy of the datasheet to declutter it** — nobody here has edit access and you
  cannot freeze rows in read-only (HoboWizard 561777).
- **Errata in Edennil's unbounds file**: the entry reading

      Stargate
          Tectonic Destablizers (New Command): Change to [ (same key as Tempest production)

  should say Fleet Beacon, not Stargate (724354, 835819, 734942).

## Cheat sheets and layout diagrams

- **DeathDealer's per-race hotkey graphics**, a redraw of the v6 release image with every button
  labelled: zerg first (297676), Terran from 821788/449588, Protoss from 490280. Edennil pinned
  them and planned an FAQ post (055521, 051536, 925771).
- **keyboard-layout-editor.com** for your own printable cheat sheet or layout image; its ISO
  preset matters for the non-US users the pinned charts do not fit (Siaal 989683; used by yjzhou
  847389; also 375566, 602146). **cyanophage.github.io** for general layout theory (517707).

## Where the files and documents live

- **Jak's Google Drive is unmaintained; use JuicyJuuce's folder** (303189, 678494, 770813). The
  Drive (`goo.gl/wQwQp7`) holds every version's files and spreadsheets including the 6g folder and
  TheCourse (Poletes 792006, 008562), organised by version, handedness and national layout
  (Hoplite 406334; Luna Cancels 679265; Sora 923403), and was the distribution point for the
  datasheet, "The Course", the FAQ and the customization doc — whose opening-sequence guide is 5.0
  or older and must be translated to 6.0 by hand (jaydik 913030).
- **Where every historical version lives** (308114): spreadsheets under `Information and Data
  Sheets` (v1-4 in `OLD VERSIONS -> OBSOLETE VERSIONS: TheCoreArchive`, dozens of tabs of Jak's
  notes); files under `Download TheCore`, with v1-4 again under `OLD VERSIONS`.
- **JuicyJuuce's TheCore6g with co-op and campaign hotkeys**, released 2022-08-06 with a writeup
  of the burrow/cloak tradeoff and three ways to handle it (282591); a UK QWERTY build too
  (589634).
- **TheCore Lite** is a GitHub repo (github.com/bobo38/TheCoreLite) whose README explains its Ctrl
  and Ctrl+Shift group and mouse synergies (666646, 600139; posted again by ghhggyvvdx 063376 as
  the lighter-weight option). See [layouts-and-variants](/layouts-and-variants.md).
- **A GitHub-hosted landing page is the plan, not the reality.** JuicyJuuce, 2023-02-22: organize
  everything in a GitHub repo using its markdown pages, with quick links, better version
  descriptions, how to choose, and an FAQ, and point everyone at thecorehotkeys.github.io (248075,
  177031). Bose volunteered to help (612594); the blocker is not permissions but "effort" (096252,
  260004).

## Odds and ends

- **Registry hacks raise the key repeat rate and lower the repeat delay** past the Windows
  slider's floor, bounded by the computer staying usable (Sora 172072; Siaal 579506).
- diffchecker is the community's stand-in for a beta changelog (Bitstorm 505294). Poletes polled
  the discord's races with a strawpoll (849599); results never posted.
